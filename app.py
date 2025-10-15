import streamlit as st
from quiz_generator import QuizGenerator
from quiz_manager import QuizManager
from ui_components import UIComponents
from config import PAGE_TITLE, PAGE_ICON, DEFAULT_QUESTIONS, DEFAULT_API_KEY, DEFAULT_DIFFICULTY, DIFFICULTY_LEVELS
from styles import CUSTOM_CSS, WELCOME_SCREEN

# Page configuration
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
)

# Apply custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Initialize session state
if 'quiz_generated' not in st.session_state:
    st.session_state.quiz_generated = False
if 'quiz_data' not in st.session_state:
    st.session_state.quiz_data = None
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
if 'difficulty' not in st.session_state:
    st.session_state.difficulty = DEFAULT_DIFFICULTY
if 'quiz_submitted' not in st.session_state:
    st.session_state.quiz_submitted = False

# === Title ===
st.markdown("<h1>🧠 AI Quiz Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #b8b8b8; font-size: 1.2rem; margin-bottom: 2rem;'>✨ Generate custom quizzes on any topic using AI ✨</p>", unsafe_allow_html=True)

# === Quiz Settings ===
with st.container():
    st.markdown("## 📝 Quiz Settings")

    # Quiz topic input
    topic = st.text_input(
        "Enter Quiz Topic:",
        placeholder="e.g., Python, Machine Learning, History..."
    )

    # Difficulty selection
    difficulty = st.radio(
        "Select Difficulty Level:",
        options=list(DIFFICULTY_LEVELS.keys()),
        index=list(DIFFICULTY_LEVELS.keys()).index(st.session_state.difficulty),
        label_visibility="visible",
        help="Choose the difficulty level for your quiz"
    )
    st.session_state.difficulty = difficulty
    st.caption(f"📌 {DIFFICULTY_LEVELS[difficulty]['description']}")

    # Number of questions
    num_questions = st.slider(
        "Number of Questions:",
        min_value=3,
        max_value=15,
        value=DEFAULT_QUESTIONS,
        step=1
    )

    # Optional API key
    with st.expander("⚙️ Advanced Settings (Optional)", expanded=False):
        from config import API_KEY_POOL
        from quiz_generator import QuizGenerator
        from datetime import datetime, timedelta
        
        # Calculate truly available keys (after cooldown check)
        if hasattr(QuizGenerator, "is_key_available"):
            truly_available = sum(1 for k in API_KEY_POOL if QuizGenerator.is_key_available(k))
        else:
            # Backward compatibility: fall back to simple count
            truly_available = len(API_KEY_POOL) - len(getattr(QuizGenerator, "failed_keys", []))

        failed_keys_ref = getattr(QuizGenerator, "failed_keys", {})
        failed_count = len(failed_keys_ref)
        in_cooldown = failed_count  # Keys in cooldown
        
        st.markdown("**🔑 API Key Pool Status**")
        
        if failed_count == 0:
            st.success(f"✅ All {len(API_KEY_POOL)} keys are available and ready to use!")
        else:
            st.warning(f"⚠️ {truly_available}/{len(API_KEY_POOL)} keys available. {in_cooldown} key(s) in {QuizGenerator.RETRY_COOLDOWN_HOURS}h cooldown.")
            
            # Show details about failed keys
            if failed_keys_ref:
                st.caption("**Failed keys will auto-retry after cooldown period:**")
                for key, fail_time in failed_keys_ref.items():
                    if hasattr(datetime, "now") and isinstance(fail_time, datetime):
                        time_since = datetime.now() - fail_time
                        minutes_ago = int(time_since.total_seconds() / 60)
                        retry_in = getattr(QuizGenerator, "RETRY_COOLDOWN_HOURS", 1) * 60 - minutes_ago
                        if retry_in > 0:
                            st.caption(f"  • Key ...{key[-6:]}: Failed {minutes_ago}m ago, retries in {retry_in}m")
                        else:
                            st.caption(f"  • Key ...{key[-6:]}: Ready to retry now")
                    else:
                        st.caption(f"  • Key ...{key[-6:]}: In cooldown")
        
        st.caption("💡 System automatically rotates to next key when quota is reached. Keys auto-retry after cooldown.")
        
        # Reset all keys button
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Reset All Keys", help="Manually reset all failed keys (useful after daily quota reset)"):
                if hasattr(QuizGenerator, "reset_all_keys"):
                    QuizGenerator.reset_all_keys()
                else:
                    # Backward compatibility: clear failed key tracking manually
                    if hasattr(QuizGenerator, "failed_keys"):
                        if isinstance(QuizGenerator.failed_keys, dict):
                            QuizGenerator.failed_keys.clear()
                        elif isinstance(QuizGenerator.failed_keys, set):
                            QuizGenerator.failed_keys.clear()
                    QuizGenerator.current_key_index = 0
                st.success("✅ All keys reset!")
                st.rerun()
        
        st.markdown("---")
        
        api_key = st.text_input(
            "Custom Google Gemini API Key (Optional):",
            value="",
            type="password",
            help="Enter your own API key to bypass the pool, or leave empty to use automatic rotation"
        )
        
        # Clear question history button
        st.markdown("---")
        st.markdown("**Question History Management**")
        st.caption("The system tracks previously asked questions to avoid repetition. Clear history to start fresh.")
        if st.button("🗑️ Clear Question History"):
            try:
                import os
                history_file = "quiz_history.json"
                if os.path.exists(history_file):
                    os.remove(history_file)
                    from quiz_generator import QuizGenerator
                    QuizGenerator.previous_questions_store = {}
                    st.success("✅ Question history cleared successfully!")
                else:
                    st.info("ℹ️ No history to clear.")
            except Exception as e:
                st.error(f"❌ Error clearing history: {str(e)}")
    
    # Generate Quiz button
    if st.button("🚀 Generate Quiz", disabled=not topic):
        try:
            with st.spinner(f"🧠 Generating {num_questions} {difficulty} questions about {topic}..."):
                # Pass api_key only if user provided one
                generator = QuizGenerator(api_key if api_key else None)
                quiz_data = generator.generate_quiz(topic, num_questions, difficulty)

                if quiz_data:
                    st.session_state.quiz_data = quiz_data
                    st.session_state.quiz_generated = True
                    st.session_state.user_answers = {}
                    st.session_state.quiz_submitted = False
                    
                    # Show success with count verification
                    if len(quiz_data) == num_questions:
                        st.success(f"✅ Quiz generated successfully! Generated {len(quiz_data)}/{num_questions} questions.")
                    else:
                        st.warning(f"⚠️ Generated {len(quiz_data)} questions (requested {num_questions}). Some were filtered due to duplicates.")
        except Exception as e:
            error_message = str(e)
            # Make error messages more user-friendly
            if "click" in error_message.lower() or "again" in error_message.lower() or "retry" in error_message.lower():
                st.error(f"⚠️ {error_message}")
                st.info("💡 **Tip:** This usually happens during API key rotation. Just click the button again!")
            else:
                st.error(f"❌ {error_message}")

    # Reset quiz button
    if st.session_state.quiz_generated:
        if st.button("🔄 Generate New Quiz"):
            st.session_state.quiz_generated = False
            st.session_state.quiz_data = None
            st.session_state.user_answers = {}
            st.session_state.quiz_submitted = False
            st.rerun()  # Force immediate rerun

# === Display quiz or welcome screen ===
if not st.session_state.quiz_generated:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(WELCOME_SCREEN, unsafe_allow_html=True)
else:
    # --- Quiz Header with Topic and Difficulty ---
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f'<div class="topic-badge"><h3>📚 {topic}</h3></div>', unsafe_allow_html=True)
    with col2:
        # Difficulty badge
        difficulty_class = "badge-easy" if "Easy" in difficulty else "badge-medium" if "Medium" in difficulty else "badge-hard"
        st.markdown(f'<div class="difficulty-badge {difficulty_class}">{difficulty}</div>', unsafe_allow_html=True)
    
    # --- Progress Bar Container (Placeholder for dynamic updates) ---
    if not st.session_state.quiz_submitted:
        progress_placeholder = st.empty()
    
    # --- Quiz Questions Container ---
    st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
    for idx, question_data in enumerate(st.session_state.quiz_data):
        UIComponents.render_question(
            idx,
            question_data,
            st.session_state.quiz_submitted,
            st.session_state.user_answers
        )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # --- Update Progress Bar After Questions Rendered ---
    if not st.session_state.quiz_submitted:
        answered = len(st.session_state.user_answers)
        total = len(st.session_state.quiz_data)
        progress_percent = (answered / total) * 100
        
        with progress_placeholder.container():
            st.markdown(f"""
            <div class="progress-container">
                <div class="progress-bar" style="width: {progress_percent}%"></div>
                <div class="progress-text">Progress: {answered}/{total} questions answered</div>
            </div>
            """, unsafe_allow_html=True)

    # --- Submit Quiz button (only after quiz generated) ---
    if not st.session_state.quiz_submitted:
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("📤 Submit Quiz", type="primary"):
                if len(st.session_state.user_answers) < len(st.session_state.quiz_data):
                    st.warning("⚠️ Please answer all questions before submitting!")
                else:
                    st.session_state.quiz_submitted = True
                    st.rerun()  # Force immediate rerun to show results

    # --- Render score card immediately if submitted ---
    if st.session_state.quiz_submitted:
        correct, total = QuizManager.calculate_score(
            st.session_state.quiz_data,
            st.session_state.user_answers
        )
        percentage = (correct / total) * 100
        message = QuizManager.get_score_message(percentage)
        UIComponents.render_score_card(correct, total, percentage, message)
