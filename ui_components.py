# File: ui_components.py
"""
UI Components for Quiz App using Streamlit
"""

import streamlit as st
from config import DIFFICULTY_LEVELS
import re


class UIComponents:
    """Handles all UI components"""
    
    @staticmethod
    def format_code_blocks(text):
        """Convert markdown code blocks to HTML code blocks for proper mobile rendering"""
        # Convert triple backtick code blocks to HTML pre/code
        # Pattern: ```language\ncode\n``` or ```language\ncode```
        def replace_code_block(match):
            language = match.group(1) if match.group(1) else ''
            code = match.group(2)
            # Escape HTML in code
            code = code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            return f'<pre><code>{code}</code></pre>'
        
        # Replace triple backtick code blocks (with or without trailing newline)
        text = re.sub(r'```(\w+)?\s*\n(.*?)```', replace_code_block, text, flags=re.DOTALL)
        
        # Convert inline code (single backticks) to HTML code tags
        def replace_inline_code(match):
            code = match.group(1)
            # Escape HTML in code
            code = code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            return f'<code>{code}</code>'
        
        # Replace inline code (avoid already converted code in pre tags)
        text = re.sub(r'`([^`]+)`', replace_inline_code, text)
        
        return text
    
    @staticmethod
    def render_sidebar(api_key_value="", topic_value="", num_questions_value=5, difficulty_value="Medium 🎯"):
        """Render sidebar with configuration options"""
        with st.sidebar:
            st.markdown("## 📝 Quiz Settings")
            
            # Quiz topic
            topic = st.text_input(
                "Enter Quiz Topic:",
                value=topic_value,
                placeholder="e.g., Python, Machine Learning, History..."
            )
            
            # Difficulty level with radio buttons
            st.markdown("**Select Difficulty Level:**")
            difficulty = st.radio(
                "Difficulty:",
                options=list(DIFFICULTY_LEVELS.keys()),
                index=list(DIFFICULTY_LEVELS.keys()).index(difficulty_value),
                label_visibility="collapsed",
                help="Choose the difficulty level for your quiz"
            )
            
            # Show difficulty description
            difficulty_desc = DIFFICULTY_LEVELS[difficulty]["description"]
            st.caption(f"📌 {difficulty_desc}")
            
            # Number of questions
            num_questions = st.slider(
                "Number of Questions:",
                min_value=3,
                max_value=15,
                value=num_questions_value,
                step=1
            )
            
            st.markdown("---")
            
            # API Key section (collapsed by default)
            with st.expander("⚙️ Advanced Settings (Optional)", expanded=False):
                st.markdown("**API Configuration**")
                api_key = st.text_input(
                    "Custom Google Gemini API Key:",
                    value=api_key_value,
                    type="password",
                    help="Leave empty to use default key, or enter your own"
                )
                st.info("💡 Using default free API key. You can add your own key from [Google AI Studio](https://makersuite.google.com/app/apikey)")
            
            # Use default API key if none provided
            if not api_key:
                api_key = api_key_value if api_key_value else None
            
            return api_key, topic, num_questions, difficulty
    
    @staticmethod
    def render_question(idx, question_data, quiz_submitted, user_answers):
        """Render a single question with enhanced styling"""
        st.markdown(f'<div class="question-box">', unsafe_allow_html=True)
        
        # Question number badge
        st.markdown(f'<span class="question-number">Question {idx + 1}</span>', unsafe_allow_html=True)
        
        # Question text with code block formatting
        formatted_question = UIComponents.format_code_blocks(question_data["question"])
        st.markdown(f'<div class="question-text">{formatted_question}</div>', unsafe_allow_html=True)
        
        if not quiz_submitted:
            # Radio button for options - before submission
            options_list = [f"{key}: {value}" for key, value in question_data['options'].items()]
            
            # Create container to prevent extra boxes
            container = st.container()
            with container:
                selected = st.radio(
                    "Select your answer:",
                    options_list,
                    key=f"q_{idx}",
                    index=None,
                    label_visibility="collapsed"
                )
                if selected:
                    user_answers[idx] = selected[0]  # Store just the letter
        else:
            # Show results after submission
            user_answer = user_answers.get(idx, None)
            correct_answer = question_data['correct_answer']
            
            for key, value in question_data['options'].items():
                option_text = f"{key}: {value}"
                if key == correct_answer:
                    st.markdown(f'<div class="option-button correct-answer"><span class="checkmark">✓</span> {option_text} <strong>(Correct Answer)</strong></div>', unsafe_allow_html=True)
                elif key == user_answer and user_answer != correct_answer:
                    st.markdown(f'<div class="option-button wrong-answer">✗ {option_text} <strong>(Your Answer)</strong></div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="option-button">{option_text}</div>', unsafe_allow_html=True)
            
            # Show explanation with better styling
            formatted_explanation = UIComponents.format_code_blocks(question_data["explanation"])
            st.markdown(f'<div class="explanation-box"><strong>💡 Explanation:</strong> {formatted_explanation}</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div style="margin-bottom: 0.5rem;"></div>', unsafe_allow_html=True)
    
    @staticmethod
    def render_score_card(correct, total, percentage, message):
        """Render enhanced score card with stats and confetti"""
        import random
        
        # Confetti effect for perfect score
        confetti_html = ""
        if percentage == 100:
            confetti_colors = ['#6c5ce7', '#a29bfe', '#fd79a8', '#00cec9', '#fdcb6e']
            confetti_html = '<div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 9999;">'
            for _ in range(50):
                color = random.choice(confetti_colors)
                left = random.randint(0, 100)
                delay = random.uniform(0, 2)
                confetti_html += f'<div class="confetti" style="left: {left}%; background: {color}; animation-delay: {delay}s;"></div>'
            confetti_html += '</div>'
        
        # Performance emoji
        if percentage == 100:
            emoji = "🏆"
        elif percentage >= 80:
            emoji = "🌟"
        elif percentage >= 60:
            emoji = "👍"
        else:
            emoji = "📚"
        
        st.markdown(confetti_html, unsafe_allow_html=True)
        
        st.markdown(f"""
            <div class='score-card'>
                <h2 style='color: white !important; margin: 0; font-size: 2.5rem;'>{emoji} Quiz Complete! {emoji}</h2>
                <h1 style='font-size: 5rem; margin: 1.5rem 0; animation: fadeInScale 0.5s ease-out;'>{correct}/{total}</h1>
                <p style='font-size: 2rem; margin: 0; font-weight: 700;'>Score: {percentage:.1f}%</p>
                <p style='margin-top: 1rem; font-size: 1.5rem;'>{message}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Stats breakdown
        incorrect = total - correct
        accuracy = percentage
        
        st.markdown(f"""
        <div class="stats-card">
            <div class="stat-item">
                <div class="stat-value">✅ {correct}</div>
                <div class="stat-label">Correct</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">❌ {incorrect}</div>
                <div class="stat-label">Incorrect</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">{accuracy:.0f}%</div>
                <div class="stat-label">Accuracy</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">📊 {total}</div>
                <div class="stat-label">Total Questions</div>
            </div>
        </div>
        """, unsafe_allow_html=True)