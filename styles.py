"""
CSS styles for the Quiz App
"""

CUSTOM_CSS = """
<style>
/* Modern dark theme with glassmorphism */
.main {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    min-height: 100vh;
}

.stApp {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
}

/* Remove all white boxes and streamlit containers */
.block-container {
    padding: 2rem 1rem !important;
    max-width: 1200px !important;
}

div[data-testid="stVerticalBlock"] > div {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

.element-container {
    background: transparent !important;
}

/* Hide empty containers */
.element-container:empty {
    display: none !important;
}

/* Fix radio button container - remove white background */
.stRadio {
    background: transparent !important;
    padding: 0 !important;
}

div[data-testid="stRadio"] {
    background: transparent !important;
}

/* Glassmorphism container */
.quiz-container {
    background: rgba(255, 255, 255, 0.05) !important;
    backdrop-filter: blur(10px);
    padding: 0 !important;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    margin: 1rem 0;
}

/* Modern question card */
.question-box {
    background: rgba(255, 255, 255, 0.08) !important;
    backdrop-filter: blur(10px);
    padding: 1.8rem;
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    margin: 1.2rem 0;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
}

.question-box:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
}

.question-text {
    color: #ffffff !important;
    font-size: 1.25rem;
    font-weight: 600;
    margin-bottom: 1.2rem;
    line-height: 1.6;
    text-shadow: 0 2px 4px rgba(0,0,0,0.2);
}

/* Modern option buttons */
.option-button {
    background: rgba(255, 255, 255, 0.1);
    border: 2px solid rgba(255, 255, 255, 0.2);
    padding: 1rem 1.5rem;
    border-radius: 12px;
    margin: 0.7rem 0;
    color: #e0e0e0;
    font-size: 1.05rem;
    font-weight: 500;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.option-button:hover {
    background: rgba(255, 255, 255, 0.15);
    transform: translateX(5px);
}

.correct-answer {
    background: linear-gradient(135deg, #00b894 0%, #00cec9 100%) !important;
    border-color: #00b894 !important;
    color: white !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 15px rgba(0, 184, 148, 0.4) !important;
}

.wrong-answer {
    background: linear-gradient(135deg, #ff7675 0%, #d63031 100%) !important;
    border-color: #ff7675 !important;
    color: white !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 15px rgba(255, 118, 117, 0.4) !important;
}

/* Explanation box with modern styling */
.explanation-box {
    background: linear-gradient(135deg, rgba(255, 193, 7, 0.15) 0%, rgba(255, 152, 0, 0.15) 100%);
    border-left: 4px solid #ffc107;
    padding: 1.2rem;
    border-radius: 10px;
    margin-top: 1.2rem;
    color: #ffd54f;
    backdrop-filter: blur(10px);
}

.explanation-box strong {
    color: #ffe082;
    font-size: 1.1rem;
}

/* Animated score card */
.score-card {
    background: linear-gradient(135deg, #6c5ce7 0%, #a29bfe 50%, #fd79a8 100%);
    color: white;
    padding: 2.5rem;
    border-radius: 20px;
    text-align: center;
    font-size: 1.5rem;
    margin: 2rem 0;
    box-shadow: 0 10px 40px rgba(108, 92, 231, 0.4);
    animation: fadeInScale 0.5s ease-out;
}

@keyframes fadeInScale {
    from {
        opacity: 0;
        transform: scale(0.9);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

/* Headers with glow effect */
h1 {
    color: #ffffff !important;
    text-align: center;
    font-size: 3.5rem !important;
    margin-bottom: 0.5rem !important;
    text-shadow: 0 0 20px rgba(108, 92, 231, 0.5), 0 0 40px rgba(108, 92, 231, 0.3);
    font-weight: 800 !important;
    letter-spacing: -1px;
}

h2 {
    color: #e0e0e0 !important;
    text-shadow: 0 2px 4px rgba(0,0,0,0.3);
}

h3 {
    color: #b8b8b8 !important;
}

/* Modern buttons with animations */
.stButton>button {
    width: 100%;
    background: linear-gradient(135deg, #6c5ce7 0%, #a29bfe 100%);
    color: white;
    border: none;
    padding: 1rem 2.5rem;
    border-radius: 12px;
    font-size: 1.15rem;
    font-weight: 700;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(108, 92, 231, 0.4);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.stButton>button:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 25px rgba(108, 92, 231, 0.6);
    background: linear-gradient(135deg, #5f4dd1 0%, #8d85e8 100%);
}

.stButton>button:active {
    transform: translateY(-1px);
}

/* Radio buttons styling */
.stRadio > label {
    color: #e0e0e0 !important;
    font-weight: 600 !important;
    font-size: 1.05rem !important;
}

.stRadio div[role="radiogroup"] {
    background: transparent !important;
}

/* Text input styling */
.stTextInput input {
    background: rgba(255, 255, 255, 0.1) !important;
    border: 2px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 10px !important;
    color: white !important;
    font-size: 1.05rem !important;
    padding: 0.8rem !important;
}

.stTextInput input:focus {
    border-color: #6c5ce7 !important;
    box-shadow: 0 0 15px rgba(108, 92, 231, 0.3) !important;
}

.stTextInput label {
    color: #e0e0e0 !important;
    font-weight: 600 !important;
}

/* Slider styling */
.stSlider {
    padding: 1rem 0 !important;
}

.stSlider label {
    color: #e0e0e0 !important;
    font-weight: 600 !important;
}

/* Remove Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Success/Warning/Error messages */
.stSuccess, .stWarning, .stError, .stInfo {
    background: rgba(255, 255, 255, 0.1) !important;
    backdrop-filter: blur(10px);
    border-radius: 10px !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    padding: 1rem !important;
    color: white !important;
}

/* Spinner overlay */
.stSpinner > div {
    border-color: #6c5ce7 !important;
}

/* Code block styling for mobile responsiveness */
pre {
    background: rgba(0, 0, 0, 0.4) !important;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    padding: 1rem;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    max-width: 100%;
    margin: 0.5rem 0;
}

pre code {
    background: transparent !important;
    color: #a8e6cf !important;
    font-family: 'Courier New', Courier, monospace;
    font-size: 0.9rem;
    line-height: 1.5;
    white-space: pre;
    display: block;
}

code {
    background: rgba(108, 92, 231, 0.2) !important;
    color: #a8e6cf !important;
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-family: 'Courier New', Courier, monospace;
    font-size: 0.9em;
    word-wrap: break-word;
    white-space: pre-wrap;
}

/* Progress bar */
.progress-container {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 50px;
    padding: 0.5rem;
    margin: 1.5rem 0;
    backdrop-filter: blur(10px);
}

.progress-bar {
    background: linear-gradient(90deg, #6c5ce7 0%, #a29bfe 50%, #fd79a8 100%);
    height: 20px;
    border-radius: 50px;
    transition: width 0.5s ease;
    box-shadow: 0 0 20px rgba(108, 92, 231, 0.5);
    position: relative;
    overflow: hidden;
}

.progress-bar::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    animation: shimmer 2s infinite;
}

@keyframes shimmer {
    0% { left: -100%; }
    100% { left: 100%; }
}

.progress-text {
    color: #ffffff;
    text-align: center;
    margin-top: 0.5rem;
    font-weight: 600;
    font-size: 0.9rem;
    text-shadow: 0 2px 4px rgba(0,0,0,0.3);
}

/* Difficulty badges */
.difficulty-badge {
    display: inline-block;
    padding: 0.5rem 1rem;
    border-radius: 25px;
    font-weight: 700;
    font-size: 0.9rem;
    margin: 0.5rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    animation: pulse 2s infinite;
}

.badge-easy {
    background: linear-gradient(135deg, #00b894 0%, #00cec9 100%);
    color: white;
}

.badge-medium {
    background: linear-gradient(135deg, #fdcb6e 0%, #f39c12 100%);
    color: white;
}

.badge-hard {
    background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
    color: white;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}

/* Confetti animation */
.confetti {
    position: fixed;
    width: 10px;
    height: 10px;
    background: #f0f;
    position: absolute;
    animation: confetti-fall 3s linear;
}

@keyframes confetti-fall {
    to {
        transform: translateY(100vh) rotate(360deg);
        opacity: 0;
    }
}

/* Stats card */
.stats-card {
    background: linear-gradient(135deg, rgba(108, 92, 231, 0.15) 0%, rgba(162, 155, 254, 0.15) 100%);
    backdrop-filter: blur(15px);
    padding: 1.5rem;
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    margin: 1rem 0;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
}

.stat-item {
    text-align: center;
    padding: 1rem;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 10px;
}

.stat-value {
    font-size: 2rem;
    font-weight: 700;
    color: #a29bfe;
    text-shadow: 0 2px 10px rgba(162, 155, 254, 0.5);
}

.stat-label {
    color: #b8b8b8;
    font-size: 0.9rem;
    margin-top: 0.5rem;
}

/* Question number badge */
.question-number {
    display: inline-block;
    background: linear-gradient(135deg, #6c5ce7 0%, #a29bfe 100%);
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 25px;
    font-weight: 700;
    margin-bottom: 1rem;
    box-shadow: 0 4px 15px rgba(108, 92, 231, 0.4);
}

/* Animated checkmark */
.checkmark {
    display: inline-block;
    animation: checkmark-pop 0.3s ease-out;
}

@keyframes checkmark-pop {
    0% { transform: scale(0); }
    50% { transform: scale(1.2); }
    100% { transform: scale(1); }
}

/* Timer badge */
.timer-badge {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    padding: 0.8rem 1.5rem;
    border-radius: 25px;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 1.1rem;
    font-weight: 600;
    color: #ffffff;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    animation: timer-pulse 1s infinite;
}

@keyframes timer-pulse {
    0%, 100% { box-shadow: 0 4px 15px rgba(108, 92, 231, 0.4); }
    50% { box-shadow: 0 4px 25px rgba(108, 92, 231, 0.6); }
}

/* Topic badge */
.topic-badge {
    background: linear-gradient(135deg, rgba(253, 121, 168, 0.2) 0%, rgba(162, 155, 254, 0.2) 100%);
    backdrop-filter: blur(10px);
    padding: 1rem 2rem;
    border-radius: 15px;
    display: inline-block;
    margin: 1rem 0;
    border: 1px solid rgba(253, 121, 168, 0.3);
}

.topic-badge h3 {
    color: #fd79a8 !important;
    margin: 0;
    font-size: 1.5rem;
    text-shadow: 0 2px 10px rgba(253, 121, 168, 0.5);
}

/* Mobile responsive layout */
@media (max-width: 768px) {
    .block-container {
        padding: 1rem 0.5rem !important;
    }
    
    pre {
        font-size: 0.75rem;
        padding: 0.75rem;
    }
    
    pre code {
        font-size: 0.75rem;
    }
    
    code {
        font-size: 0.85em;
        padding: 0.15rem 0.3rem;
    }
    
    .question-text {
        font-size: 1.05rem;
        line-height: 1.5;
    }
}

@media (max-width: 480px) {
    pre {
        font-size: 0.7rem;
        padding: 0.5rem;
    }
    
    pre code {
        font-size: 0.7rem;
    }
    
    code {
        font-size: 0.8em;
    }
}
</style>
"""

WELCOME_SCREEN = """<div style="background: linear-gradient(135deg, rgba(108, 92, 231, 0.15) 0%, rgba(162, 155, 254, 0.15) 100%); backdrop-filter: blur(15px); padding: 3.5rem; border-radius: 25px; margin-top: 2rem; border: 1px solid rgba(255, 255, 255, 0.2); box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);">
    <div style="text-align: center; margin-bottom: 2rem;">
        <div style="font-size: 4rem; margin-bottom: 1rem;">🧠</div>
        <h2 style="color: #ffffff; font-size: 2.5rem; font-weight: 700; margin-bottom: 0.5rem; text-shadow: 0 2px 10px rgba(108, 92, 231, 0.5);">Welcome to AI Quiz Generator!</h2>
        <p style="color: #b8b8b8; font-size: 1.2rem; margin: 0;">Test your knowledge on any topic with AI-powered quizzes</p>
    </div>
    <hr style="border: none; border-top: 1px solid rgba(255, 255, 255, 0.1); margin: 2rem 0;">
    <h3 style="color: #a29bfe; font-size: 1.5rem; margin-bottom: 1.5rem; font-weight: 600;">✨ Features</h3>
    <div style="display: grid; gap: 1rem;">
        <div style="background: rgba(255, 255, 255, 0.05); padding: 1rem 1.5rem; border-radius: 12px; border-left: 4px solid #6c5ce7;">
            <span style="color: #ffffff; font-size: 1.1rem; font-weight: 500;">🎯 Smart Questions</span>
            <p style="color: #b8b8b8; margin: 0.5rem 0 0 0;">AI generates unique questions every time - no repeats!</p>
        </div>
        <div style="background: rgba(255, 255, 255, 0.05); padding: 1rem 1.5rem; border-radius: 12px; border-left: 4px solid #a29bfe;">
            <span style="color: #ffffff; font-size: 1.1rem; font-weight: 500;">📊 Instant Feedback</span>
            <p style="color: #b8b8b8; margin: 0.5rem 0 0 0;">Get detailed explanations for every answer</p>
        </div>
        <div style="background: rgba(255, 255, 255, 0.05); padding: 1rem 1.5rem; border-radius: 12px; border-left: 4px solid #fd79a8;">
            <span style="color: #ffffff; font-size: 1.1rem; font-weight: 500;">⚡ Lightning Fast</span>
            <p style="color: #b8b8b8; margin: 0.5rem 0 0 0;">Generate 3-15 questions in seconds with 6 API keys rotation</p>
        </div>
        <div style="background: rgba(255, 255, 255, 0.05); padding: 1rem 1.5rem; border-radius: 12px; border-left: 4px solid #00cec9;">
            <span style="color: #ffffff; font-size: 1.1rem; font-weight: 500;">🎓 Any Topic</span>
            <p style="color: #b8b8b8; margin: 0.5rem 0 0 0;">From Python to History, Science to Literature</p>
        </div>
    </div>
    <div style="background: linear-gradient(135deg, rgba(108, 92, 231, 0.2) 0%, rgba(162, 155, 254, 0.2) 100%); padding: 1.5rem; border-radius: 15px; margin-top: 2rem; border: 1px solid rgba(108, 92, 231, 0.4); text-align: center;">
        <p style="color: #ffffff; margin: 0; font-size: 1.15rem; font-weight: 600;">🚀 <strong>Ready?</strong> Enter a topic above and click Generate Quiz!</p>
        <p style="color: #b8b8b8; margin: 0.5rem 0 0 0; font-size: 0.95rem;">Try: Python Programming, World War II, Human Biology, Machine Learning</p>
    </div>
</div>"""
