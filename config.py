# File: config.py
"""
Configuration settings for the Quiz App
"""

# API Configuration
import streamlit as st

# Try to load from Streamlit secrets (for production deployment)
try:
    API_KEY_POOL = [
        st.secrets["api_keys"]["key1"],
        st.secrets["api_keys"]["key2"],
        st.secrets["api_keys"]["key3"],
        st.secrets["api_keys"]["key4"],
        st.secrets["api_keys"]["key5"],
        st.secrets["api_keys"]["key6"],
        st.secrets["api_keys"]["key7"],
        st.secrets["api_keys"]["key8"],
        st.secrets["api_keys"]["key9"],
        st.secrets["api_keys"]["key10"],
    ]
    DEFAULT_API_KEY = API_KEY_POOL[0]
except:
    # Fallback to hardcoded keys (for local development)
    DEFAULT_API_KEY = "AIzaSyCKyXe8weTP27n1fi9G88hfCcl3HhxQICQ"
    
    # Multiple API Keys for automatic rotation when quota is reached
    API_KEY_POOL = [
        "AIzaSyCKyXe8weTP27n1fi9G88hfCcl3HhxQICQ",
        "AIzaSyAHUsalutCvdP-PGar81EwbBiad-Ehd1lc",
        "AIzaSyDu5aXqH9sMOvPB7kaZZ1VDMgHufZuUg-s",
        "AIzaSyCHGrz-idIbQ7MVUacOLgsuWaUyqxvMQFw",
        "AIzaSyBj6KT3TJNE7BNTO3mj3w1bbYNxQdGmgzs",
        "AIzaSyAQEa_ois1vVQTiz62bWxUqZv1AF45hiAc",
        "AIzaSyDq1YzszK5nNCVssXvbKveo_hB6jDkLuv0",
        "AIzaSyBErYtFt0pVceGIDkVMTUXoy2njNw2rHD4",
        "AIzaSyDW1q1iiRZ1WybjW2PIovA_qkDnynSrSCw",
        "AIzaSyAOnO0vcxZvnqjnltU0qXgSmwuogd3t4FQ",
    ]

DEFAULT_MODEL = "gemini-2.0-flash-exp"  # Updated to working model
DEFAULT_TEMPERATURE = 0.7

# Quiz Configuration
MIN_QUESTIONS = 3
MAX_QUESTIONS = 15
DEFAULT_QUESTIONS = 5

# Difficulty Levels
DIFFICULTY_LEVELS = {
    "Easy 😊": {
        "description": "Basic concepts and straightforward questions",
        "prompt_modifier": "easy difficulty with straightforward questions suitable for beginners. Focus on fundamental concepts and basic understanding."
    },
    "Medium 🎯": {
        "description": "Moderate difficulty with some challenging aspects",
        "prompt_modifier": "medium difficulty with balanced, moderately challenging questions. Focus on practical understanding and application of intermediate concepts. Questions should be clear and concise, not overly verbose. Mix different question types: conceptual understanding (30%), practical applications (30%), 'what is the output of this code' (20%), best practices (10%), and comparisons (10%)."
    },
    "Hard 🔥": {
        "description": "Advanced questions requiring deep knowledge",
        "prompt_modifier": "hard difficulty with advanced and challenging questions. Include complex scenarios, edge cases, and questions that require deep understanding and critical thinking."
    }
}

DEFAULT_DIFFICULTY = "Medium 🎯"

# UI Configuration
PAGE_TITLE = "AI Quiz Generator"
PAGE_ICON = "🧠"

# Prompt Template
QUIZ_GENERATION_PROMPT = """You are an expert quiz creator. Generate exactly {num_questions} multiple-choice questions about {topic} at {difficulty_level}.

SIMPLIFIED APPROACH - FOLLOW EXACTLY:
1. Your response must be ONLY a JSON array: [question1, question2, ...]
2. Each question is a JSON object with: question, options, correct_answer, explanation
3. ALL values must be simple strings - no complex formatting
4. For code questions: put code in question text using simple formatting
5. Keep options SHORT and SIMPLE - no code blocks in options
6. Use this EXACT format for code questions:

"question": "What will this code output?\\n\\nclass Example:\\n    def method(self):\\n        return 'hello'\\n\\nobj = Example()\\nprint(obj.method())\\n\\nChoose the output:"

DIFFICULTY REQUIREMENT: {difficulty_description}

CRITICAL VARIETY REQUIREMENT:
- Every time generate different questions, even if the topic is the same (most important)
- If any question is similar to the above, REJECT and regenerate
- Focus on DIFFERENT aspects and concepts, including real-world scenarios, edge cases, and creative applications
- Generate UNIQUE questions that are not typical textbook examples
- Avoid the most common/obvious questions that everyone asks
- Think creatively and test deeper understanding
- Make sure questions are not repeated from previous quizzes

SIMPLE FORMATTING RULES:
1. Question text: Use \\n for line breaks, NO backticks or special formatting
2. Code in questions: Write as plain text with \\n for new lines
3. Options: Always simple strings - "hello", "5", "True", "AttributeError"
4. NO code blocks anywhere - use plain text only
5. NO complex formatting, NO backticks, NO special characters

QUESTION TYPES FOR MEDIUM DIFFICULTY:
- Conceptual understanding (30%)
- Practical applications (30%) 
- Code output prediction (20%)
- Best practices (10%)
- Comparisons (10%)

GUIDELINES:
- Keep questions clear and concise
- Test understanding, not memorization
- Include 1-2 code output questions per quiz
- Focus on practical knowledge

SIMPLE EXAMPLES - NO COMPLEX FORMATTING:

EXAMPLE 1 - Code output question (SIMPLE FORMAT):
[
  {{
    "question": "What will this code output?\\n\\nclass Test:\\n    def __init__(self):\\n        self.value = 5\\n\\nobj = Test()\\nprint(obj.value)",
    "options": {{
      "A": "5",
      "B": "Test",
      "C": "None", 
      "D": "AttributeError"
    }},
    "correct_answer": "A",
    "explanation": "The code creates an object and prints its value attribute, which is 5."
  }}
]

EXAMPLE 2 - Conceptual question (NO CODE):
[
  {{
    "question": "What is the main purpose of Python decorators?",
    "options": {{
      "A": "To modify or enhance function behavior",
      "B": "To create new classes",
      "C": "To handle exceptions",
      "D": "To import modules"
    }},
    "correct_answer": "A", 
    "explanation": "Decorators are used to modify or enhance the behavior of functions or classes."
  }}
]

CRITICAL RULES:
- Use PLAIN TEXT only - no backticks, no special formatting
- Code in questions: use \\n for line breaks
- Options: simple strings only
- NO [object Object], NO undefined, NO complex structures

FINAL INSTRUCTIONS:
1. Generate ONLY valid JSON - nothing else
2. Use simple plain text formatting
3. NO backticks, NO code blocks, NO complex structures
4. Code in questions: plain text with \\n line breaks
5. Options: simple strings like "5", "hello", "True", "AttributeError"
6. Include 1-2 code output questions per quiz
7. Keep questions concise and focused

Your response must be a clean JSON array with no extra text."""
