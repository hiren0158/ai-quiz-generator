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
    ]
    DEFAULT_API_KEY = API_KEY_POOL[0]
except:
    # Fallback to hardcoded keys (for local development)
    DEFAULT_API_KEY = "AIzaSyBp0zPkMF15rYvtvj6XPgnw03-3a6h0CGA"
    
    # Multiple API Keys for automatic rotation when quota is reached
    API_KEY_POOL = [
        "AIzaSyBp0zPkMF15rYvtvj6XPgnw03-3a6h0CGA",
        "AIzaSyCcALpmeywfD1RQ_VbeAJSiQ815N2AaBlY",
        "AIzaSyCLXMhfUBGr1qRYWf2gzY3CjVT74DWzFAM",
        "AIzaSyB_bq-gubIukD9FdL6dKVQVAxLstfse4IQ",
        "AIzaSyDh5ovwTSzgWMIwVF1iSXEzbZJyiz8zJU4",
        "AIzaSyDfp93mJii0QYvWCFnM05kIxR1A5wpvrt4",
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
        "prompt_modifier": "medium difficulty with moderately challenging questions. Include both basic and intermediate concepts that require good understanding."
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

DIFFICULTY REQUIREMENT: {difficulty_description}

CRITICAL VARIETY REQUIREMENT:
- Every time generate different questions, even if the topic is the same (most important)
- If any question is similar to the above, REJECT and regenerate
- Focus on DIFFERENT aspects and concepts, including real-world scenarios, edge cases, and creative applications
- Generate UNIQUE questions that are not typical textbook examples
- Avoid the most common/obvious questions that everyone asks
- Think creatively and test deeper understanding
- Make sure questions are not repeated from previous quizzes

For each question, provide:
1. A clear, specific question appropriate for the difficulty level
2. Exactly 4 options (A, B, C, D)
3. The correct answer (letter only: A, B, C, or D)
4. A brief explanation for the correct answer

IMPORTANT GUIDELINES:
- For EASY difficulty: Use simple language, test basic recall and fundamental concepts, but DO NOT use the forbidden examples above
- For MEDIUM difficulty: Mix factual recall with application and understanding
- For HARD difficulty: Include scenario-based questions, edge cases, and questions requiring analysis

Format your response as a valid JSON array with this exact structure:
[
  {{
    "question": "Question text here?",
    "options": {{
      "A": "First option",
      "B": "Second option",
      "C": "Third option",
      "D": "Fourth option"
    }},
    "correct_answer": "A",
    "explanation": "Explanation here"
  }}
]

Make the questions challenging and educational according to the specified difficulty level. Ensure the JSON is properly formatted with no extra text before or after."""
