# 🧠 AI Quiz Generator
https://ai-quiz-generator-wgrn5hnhretaapncetynyk.streamlit.app/

A modern, feature-rich quiz application powered by Google Gemini AI with beautiful glassmorphism UI design.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.31+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

### Core Functionality
- 🤖 **AI-Powered** - Uses Google Gemini 2.0 Flash for intelligent question generation
- 🎯 **3 Difficulty Levels** - Easy, Medium, and Hard
- 📊 **Customizable** - Generate 3-15 questions per quiz
- 💡 **Instant Feedback** - Detailed explanations for every answer
- 🔄 **No Repeats** - Smart duplicate detection prevents question repetition

### Smart Features
- 🔑 **6 API Keys Rotation** - 300 requests/day capacity with automatic failover
- 📈 **Progress Tracking** - Animated progress bar shows your completion status
- 📊 **Detailed Statistics** - Comprehensive performance breakdown after each quiz
- 🎉 **Confetti Celebration** - Special animation for perfect scores!
- ✓ **Animated Feedback** - Smooth animations and visual effects

### Modern UI/UX
- 🎨 **Glassmorphism Design** - Beautiful frosted glass effect
- 🌙 **Dark Theme** - Navy gradient background reduces eye strain
- ⚡ **Smooth Animations** - 60fps transitions and hover effects
- 🎯 **Difficulty Badges** - Color-coded visual indicators
- 📚 **Topic Badges** - Prominent topic display
- 🔢 **Question Numbers** - Stylish purple gradient badges

## 🚀 Live Demo

[Live Demo Link](your-streamlit-app-url-here) _(will be available after deployment)_

## 📸 Screenshots

### Home Screen
Beautiful welcome screen with feature showcase

### Quiz Interface
Modern dark theme with glassmorphism effects

### Results Screen
Detailed statistics with confetti celebration for perfect scores!

## 🛠️ Technologies Used

- **Frontend:** Streamlit
- **AI Model:** Google Gemini 2.0 Flash Exp
- **Framework:** LangChain
- **Language:** Python 3.8+
- **Styling:** Custom CSS (Glassmorphism)

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key (get it free at [Google AI Studio](https://aistudio.google.com/app/apikey))

### Local Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd QUIZ\ generator
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure API keys**
Edit `config.py` and add your API keys:
```python
API_KEY_POOL = [
    "YOUR_API_KEY_1",
    "YOUR_API_KEY_2",
    # Add up to 6 keys for maximum capacity
]
```

5. **Run the application**
```bash
streamlit run app.py
```

6. **Open in browser**
Navigate to `http://localhost:8501`

## ⚙️ Configuration

### API Keys
Add your Google Gemini API keys in `config.py`:
- **Free Tier:** 50 requests/day per key
- **Recommended:** Use 3-6 keys for optimal performance
- **Total Capacity:** Up to 300 requests/day with 6 keys

### Quiz Settings
Customize in `config.py`:
```python
MIN_QUESTIONS = 3
MAX_QUESTIONS = 15
DEFAULT_QUESTIONS = 5
```

### Styling
Modify colors and animations in `styles.py`

## 📊 Features Breakdown

### 1. API Key Rotation System
- Automatic switching when quota is reached
- No downtime between key switches
- Real-time status display ("X/6 keys available")

### 2. Duplicate Prevention
- Persistent question history in `quiz_history.json`
- 80% similarity threshold for detection
- Stores last 100 questions per topic
- Smart filtering with retry logic

### 3. Progress Tracking
- Animated gradient progress bar
- Real-time update as you answer
- Shimmer effect for visual appeal

### 4. Score Celebration
- Confetti animation for 100% scores
- Detailed statistics breakdown
- Performance-based emoji indicators

## 🎨 UI Components

### Color Palette
- **Primary:** #6c5ce7 (Purple)
- **Secondary:** #a29bfe (Light Purple)
- **Accent:** #fd79a8 (Pink)
- **Success:** #00b894 (Green)
- **Error:** #ff7675 (Red)
- **Background:** #1a1a2e → #0f3460 (Navy Gradient)

### Design Features
- Glassmorphism effects
- Smooth 60fps animations
- Hover transitions
- Color-coded difficulty badges
- Responsive layout

## 📈 Performance

- **Quiz Generation:** 3-5 seconds
- **Page Load:** <1 second
- **Animations:** Hardware accelerated (60fps)
- **Success Rate:** 95%+ with retries
- **Duplicate Rate:** <5%

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini AI for powerful language model
- Streamlit for amazing web framework
- LangChain for AI integration tools

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: [Your Email]

## 🎯 Roadmap

- [ ] User accounts and progress tracking
- [ ] Quiz history and analytics
- [ ] Leaderboard system
- [ ] Social sharing features
- [ ] Mobile app version
- [ ] Multiple language support

## ⭐ Star History

If you find this project useful, please consider giving it a star!

---

**Made with ❤️ using Streamlit and Google Gemini AI**
Here’s your content with properly formatted Markdown syntax:

