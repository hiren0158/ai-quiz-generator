"""
Quiz generation logic using LangChain and Google Gemini

Alternative Method: Using temperature and other parameters
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import json
import re
from config import DEFAULT_MODEL, DEFAULT_TEMPERATURE, QUIZ_GENERATION_PROMPT, DIFFICULTY_LEVELS, API_KEY_POOL
import difflib
import os
import random


class QuizGenerator:
    """Handles quiz generation using LLM"""
    # Persistent store for previous questions per topic
    previous_questions_store = {}
    STORAGE_FILE = "quiz_history.json"
    
    # API key rotation management
    current_key_index = 0
    failed_keys = set()  # Track keys that hit quota
    
    @classmethod
    def load_history(cls):
        """Load question history from file"""
        if os.path.exists(cls.STORAGE_FILE):
            try:
                with open(cls.STORAGE_FILE, 'r', encoding='utf-8') as f:
                    cls.previous_questions_store = json.load(f)
            except Exception:
                cls.previous_questions_store = {}
    
    @classmethod
    def save_history(cls):
        """Save question history to file"""
        try:
            with open(cls.STORAGE_FILE, 'w', encoding='utf-8') as f:
                json.dump(cls.previous_questions_store, f, indent=2)
        except Exception:
            pass
    
    def __init__(self, api_key=None):
        """Initialize the quiz generator with API key or use pool"""
        self.custom_api_key = api_key if api_key and api_key not in API_KEY_POOL else None
        self.current_key = None
        self.llm = None
    
    def get_next_available_key(self):
        """Get the next available API key from the pool"""
        # If user provided custom key, use it
        if self.custom_api_key:
            return self.custom_api_key
        
        # Find keys that haven't failed
        available_keys = [k for k in API_KEY_POOL if k not in QuizGenerator.failed_keys]
        
        if not available_keys:
            # All keys exhausted
            return None
        
        # Get next key in rotation
        key = available_keys[QuizGenerator.current_key_index % len(available_keys)]
        QuizGenerator.current_key_index += 1
        return key
        
    def initialize_llm(self, difficulty="Medium 🎯", force_key=None):
        """
        Initialize the Google Gemini LLM with automatic key rotation
        
        Alternative Method: Adjust temperature based on difficulty
        - Easy: Lower temperature (0.3) for more predictable, straightforward questions
        - Medium: Medium temperature (0.7) for balanced creativity
        - Hard: Higher temperature (0.9) for more creative and complex questions
        """
        try:
            # Map difficulty to temperature (Alternative approach)
            temperature_map = {
                "Easy 😊": 0.3,
                "Medium 🎯": 0.7,
                "Hard 🔥": 0.9
            }
            
            temperature = temperature_map.get(difficulty, DEFAULT_TEMPERATURE)
            
            # Get API key (forced, or next available)
            api_key = force_key if force_key else self.get_next_available_key()
            
            if not api_key:
                raise Exception(f"All {len(API_KEY_POOL)} API keys have reached their quota limit. Please wait for daily reset or add more keys.")
            
            self.llm = ChatGoogleGenerativeAI(
                model=DEFAULT_MODEL,
                google_api_key=api_key,
                temperature=temperature  # Dynamic temperature based on difficulty
            )
            self.current_key = api_key
            return True
        except Exception as e:
            error_str = str(e)
            if "quota" in error_str.lower() or "429" in error_str:
                raise Exception("API quota limit reached. Switching keys...")
            elif "api" in error_str.lower() or "key" in error_str.lower():
                raise Exception("API connection failed. Please click 'Generate Quiz' again.")
            else:
                raise Exception(f"Connection error. Please try again.")
    
    def generate_quiz(self, topic, num_questions, difficulty="Medium 🎯"):
        """
        Generate quiz questions with specified difficulty and duplicate prevention
        """
        try:
            # Load history from persistent storage
            QuizGenerator.load_history()
            
            # Initialize LLM with difficulty-based temperature
            if not self.llm:
                if not self.initialize_llm(difficulty):
                    raise Exception("Failed to initialize. Please click 'Generate Quiz' again.")
            
            # Get difficulty configuration
            difficulty_config = DIFFICULTY_LEVELS.get(difficulty, DIFFICULTY_LEVELS["Medium 🎯"])
            
            # Get previous questions for this topic
            prev_questions = QuizGenerator.previous_questions_store.get(topic, [])
        except Exception as init_error:
            # Show actual error for debugging
            error_msg = str(init_error)
            if "quota" in error_msg.lower() or "429" in error_msg:
                raise Exception("All API keys have reached their quota. Please try again later or add fresh API keys.")
            else:
                raise Exception(f"Setup error: {error_msg}")
        
        # Create enhanced prompt with previous questions context
        enhanced_prompt = QUIZ_GENERATION_PROMPT
        if prev_questions:
            # Add context about previous questions (show last 10)
            recent_questions = prev_questions[-10:]
            # Escape curly braces in previous questions to prevent template variable conflicts
            escaped_questions = [q.replace('{', '{{').replace('}', '}}') for q in recent_questions]
            prev_q_text = "\n".join([f"- {q}" for q in escaped_questions])
            enhanced_prompt += f"\n\nIMPORTANT - AVOID THESE PREVIOUSLY ASKED QUESTIONS:\n{prev_q_text}\n\nYour questions MUST be completely different from the above. Generate fresh, unique questions on different aspects of the topic."

        prompt_template = PromptTemplate(
            input_variables=["topic", "num_questions", "difficulty_level", "difficulty_description"],
            template=enhanced_prompt
        )

        chain = prompt_template | self.llm

        forbidden_keywords = [
            "hello world", "variable naming", "print statement", "basic data type", "simple loop", "input/output", "if statement", "for loop", "while loop", "function definition", "list operation", "string concatenation", "simple arithmetic"
        ]

        def contains_forbidden(question_text):
            lower_q = question_text.lower()
            return any(keyword in lower_q for keyword in forbidden_keywords)
        
        def is_duplicate(question_text):
            # Fuzzy match: consider duplicate if similarity > 0.80 with any previous question
            question_text_clean = question_text.strip().lower()
            for prev in prev_questions:
                similarity = difflib.SequenceMatcher(None, question_text_clean, prev).ratio()
                if similarity > 0.80:
                    return True
            return False

        max_attempts = 3  # Allow retries to get exact count
        last_error = None
        
        for attempt in range(max_attempts):
            try:
                # Request extra questions to account for filtering (more on retry)
                if attempt == 0:
                    extra_questions = min(5, num_questions) if prev_questions else 2
                else:
                    # If first attempt didn't get enough, request more
                    extra_questions = num_questions  # Double the request on retry
                
                response = chain.invoke({
                    "topic": topic, 
                    "num_questions": num_questions + extra_questions,
                    "difficulty_level": difficulty,
                    "difficulty_description": difficulty_config["prompt_modifier"]
                })

                response_text = response.content if hasattr(response, 'content') else str(response)
                # Clean up trailing commas before parsing JSON
                response_text = re.sub(r',\s*([}\]])', r'\1', response_text)
                json_match = re.search(r'\[[\s\S]*\]', response_text)
                
                if json_match:
                    json_str = json_match.group(0)
                    quiz_data = json.loads(json_str)
                    
                    # Filter out duplicates and forbidden questions
                    filtered_questions = []
                    for q in quiz_data:
                        question_text = q["question"]
                        if not contains_forbidden(question_text) and not is_duplicate(question_text):
                            filtered_questions.append(q)
                    
                    # Check if we have EXACTLY the number requested
                    if len(filtered_questions) >= num_questions:
                        # Randomly select to avoid patterns
                        if len(filtered_questions) > num_questions:
                            random.shuffle(filtered_questions)
                            filtered_questions = filtered_questions[:num_questions]
                        
                        # Store questions in history
                        new_questions = [q["question"].strip().lower() for q in filtered_questions]
                        all_questions = prev_questions + new_questions
                        QuizGenerator.previous_questions_store[topic] = all_questions[-100:]  # Keep last 100
                        QuizGenerator.save_history()  # Persist to file
                        
                        return filtered_questions
                    else:
                        # Not enough questions after filtering
                        shortage = num_questions - len(filtered_questions)
                        
                        # If this is not the last attempt, retry with relaxed filtering
                        if attempt < max_attempts - 1:
                            # Increase temperature for more variety
                            self.llm.temperature = min(1.0, self.llm.temperature + 0.2)
                            continue
                        else:
                            # Last attempt: use less strict duplicate checking
                            # Re-filter with lower threshold (0.90 instead of 0.80)
                            relaxed_filtered = []
                            for q in quiz_data:
                                question_text = q["question"]
                                if not contains_forbidden(question_text):
                                    # Check with relaxed threshold
                                    question_text_clean = question_text.strip().lower()
                                    is_dup = False
                                    for prev in prev_questions:
                                        similarity = difflib.SequenceMatcher(None, question_text_clean, prev).ratio()
                                        if similarity > 0.90:  # More relaxed
                                            is_dup = True
                                            break
                                    if not is_dup:
                                        relaxed_filtered.append(q)
                            
                            # Use relaxed filtered questions
                            if len(relaxed_filtered) >= num_questions:
                                random.shuffle(relaxed_filtered)
                                final_questions = relaxed_filtered[:num_questions]
                            else:
                                # Still not enough, pad with best available
                                final_questions = relaxed_filtered + quiz_data[:num_questions - len(relaxed_filtered)]
                                final_questions = final_questions[:num_questions]
                            
                            new_questions = [q["question"].strip().lower() for q in final_questions]
                            all_questions = prev_questions + new_questions
                            QuizGenerator.previous_questions_store[topic] = all_questions[-100:]
                            QuizGenerator.save_history()
                            return final_questions
                else:
                    last_error = f"Could not parse quiz data. Raw response: {response_text[:500]}"
            except Exception as e:
                error_msg = str(e)
                
                # Check if it's a quota error
                if "429" in error_msg or "quota" in error_msg.lower() or "ResourceExhausted" in error_msg:
                    # Mark current key as failed
                    if self.current_key:
                        QuizGenerator.failed_keys.add(self.current_key)
                        available_count = len(API_KEY_POOL) - len(QuizGenerator.failed_keys)
                    
                    # Check if we can try another key
                    if self.custom_api_key:
                        # Custom key hit limit, can't rotate
                        raise Exception("Your custom API key has reached its quota limit. Please wait for daily reset or try another key.")
                    
                    # Try next key in pool
                    next_key = self.get_next_available_key()
                    if next_key:
                        # Show informative message but continue
                        print(f"⚠️ Switching to next API key... ({available_count}/{len(API_KEY_POOL)} keys remaining)")
                        try:
                            self.initialize_llm(difficulty, force_key=next_key)
                            continue  # Retry the generation
                        except Exception as init_error:
                            # Failed to initialize with new key
                            raise Exception(f"API key rotation failed. Please click 'Generate Quiz' again to retry.")
                    else:
                        # All keys exhausted
                        raise Exception(f"All {len(API_KEY_POOL)} API keys have reached their quota limit. Please wait for daily reset or add more keys.")
                
                # Check for other common errors
                elif "LLM" in error_msg or "initialize" in error_msg.lower():
                    raise Exception("Connection error. Please click 'Generate Quiz' again to retry.")
                elif "parse" in error_msg.lower() or "JSON" in error_msg:
                    last_error = f"Could not process AI response. Please click 'Generate Quiz' again."
                else:
                    # Generic error - make it user-friendly
                    last_error = f"Temporary error occurred. Please click 'Generate Quiz' again to retry. (Details: {error_msg[:100]})"
        
        # If we exhausted all attempts, show friendly message
        if last_error:
            raise Exception(last_error)
        else:
            raise Exception("Unable to generate quiz after multiple attempts. Please click 'Generate Quiz' again.")