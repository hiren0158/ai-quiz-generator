# 🚀 Deployment Guide - AI Quiz Generator

## Quick Deployment Options

### 1️⃣ Streamlit Community Cloud (Recommended - FREE)
### 2️⃣ Heroku
### 3️⃣ Railway
### 4️⃣ Render

---

## Option 1: Streamlit Community Cloud (Easiest & Free)

### ✅ Prerequisites
- GitHub account
- Your code pushed to GitHub repository
- Google Gemini API keys (free from [Google AI Studio](https://aistudio.google.com/app/apikey))

### 📝 Step-by-Step Instructions

#### Step 1: Prepare Your Repository

1. **Create a GitHub repository**
   ```bash
   # Navigate to your project folder
   cd "/Users/admin/Desktop/QUIZ generator"
   
   # Initialize git (if not already done)
   git init
   
   # Add all files
   git add .
   
   # Commit
   git commit -m "Initial commit - AI Quiz Generator"
   ```

2. **Push to GitHub**
   ```bash
   # Create a new repository on GitHub.com, then:
   git remote add origin https://github.com/YOUR_USERNAME/ai-quiz-generator.git
   git branch -M main
   git push -u origin main
   ```

#### Step 2: Deploy on Streamlit Cloud

1. **Go to [share.streamlit.io](https://share.streamlit.io)**

2. **Sign in with GitHub**

3. **Click "New app"**

4. **Fill in the details:**
   - **Repository:** Select your GitHub repo
   - **Branch:** main
   - **Main file path:** app.py
   - **App URL:** Choose your custom URL (e.g., `your-app-name.streamlit.app`)

5. **Advanced Settings** (Click "Advanced settings"):
   - **Python version:** 3.9 or higher
   - **Secrets:** Add your API keys here (see below)

#### Step 3: Configure Secrets (Important!)

In the **Secrets** section, add your API keys:

```toml
# .streamlit/secrets.toml format
[api_keys]
key1 = "AIzaSyBp0zPkMF15rYvtvj6XPgnw03-3a6h0CGA"
key2 = "AIzaSyCcALpmeywfD1RQ_VbeAJSiQ815N2AaBlY"
key3 = "AIzaSyCLXMhfUBGr1qRYWf2gzY3CjVT74DWzFAM"
key4 = "AIzaSyB_bq-gubIukD9FdL6dKVQVAxLstfse4IQ"
key5 = "AIzaSyDh5ovwTSzgWMIwVF1iSXEzbZJyiz8zJU4"
key6 = "AIzaSyDfp93mJii0QYvWCFnM05kIxR1A5wpvrt4"
```

#### Step 4: Modify config.py for Secrets

Update your `config.py` to read from Streamlit secrets in production:

```python
import streamlit as st

# Try to load from Streamlit secrets first (for deployment)
try:
    API_KEY_POOL = [
        st.secrets["api_keys"]["key1"],
        st.secrets["api_keys"]["key2"],
        st.secrets["api_keys"]["key3"],
        st.secrets["api_keys"]["key4"],
        st.secrets["api_keys"]["key5"],
        st.secrets["api_keys"]["key6"],
    ]
except:
    # Fallback to hardcoded keys (for local development)
    API_KEY_POOL = [
        "AIzaSyBp0zPkMF15rYvtvj6XPgnw03-3a6h0CGA",
        "AIzaSyCcALpmeywfD1RQ_VbeAJSiQ815N2AaBlY",
        # ... rest of your keys
    ]
```

#### Step 5: Deploy!

1. Click **"Deploy"**
2. Wait 2-3 minutes for deployment
3. Your app will be live at: `https://your-app-name.streamlit.app`

### 🎉 Done! Your app is now live!

---

## Option 2: Heroku

### Prerequisites
- Heroku account
- Heroku CLI installed

### Files Needed

1. **Procfile**
```
web: sh setup.sh && streamlit run app.py
```

2. **setup.sh**
```bash
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

3. **runtime.txt**
```
python-3.9.16
```

### Deploy Commands
```bash
heroku login
heroku create your-app-name
git push heroku main
heroku open
```

---

## Option 3: Railway

### Steps

1. Go to [railway.app](https://railway.app)
2. Click "Start a New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository
5. Railway auto-detects Streamlit
6. Add environment variables (API keys)
7. Deploy!

**Railway automatically:**
- Detects `requirements.txt`
- Installs dependencies
- Runs your app

---

## Option 4: Render

### Steps

1. Go to [render.com](https://render.com)
2. Click "New" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name:** your-app-name
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run app.py --server.port $PORT`
5. Add environment variables (API keys)
6. Deploy!

---

## 🔐 Security Best Practices

### Don't Commit API Keys!

1. **Use .gitignore**
   ```
   .streamlit/secrets.toml
   config.py  # If it contains keys
   ```

2. **Use Environment Variables**
   ```python
   import os
   API_KEY = os.getenv('GEMINI_API_KEY')
   ```

3. **Use Streamlit Secrets (Production)**
   ```python
   import streamlit as st
   API_KEY = st.secrets["api_keys"]["key1"]
   ```

---

## 📊 Post-Deployment Checklist

- [ ] App loads successfully
- [ ] API keys are secure (not in GitHub)
- [ ] Quiz generation works
- [ ] All 6 API keys are configured
- [ ] Progress bar displays correctly
- [ ] Confetti animation works
- [ ] Score card shows properly
- [ ] Mobile view is responsive
- [ ] Custom domain configured (optional)

---

## 🔧 Troubleshooting

### Problem: App won't start

**Solution:**
- Check `requirements.txt` has all dependencies
- Verify Python version (3.8+)
- Check Streamlit logs for errors

### Problem: API quota exceeded

**Solution:**
- Add more API keys
- Wait for daily reset (midnight UTC)
- Get your own free keys from Google AI Studio

### Problem: Questions repeating

**Solution:**
- Clear `quiz_history.json` (or delete it)
- Restart the app

### Problem: Slow loading

**Solution:**
- Check API key status
- Verify internet connection
- Try different difficulty level

---

## 📈 Monitoring Your App

### Streamlit Cloud Dashboard
- View app analytics
- Monitor resource usage
- Check error logs
- See visitor statistics

### Custom Analytics (Optional)
Add Google Analytics or other tracking:
```python
# In app.py, add tracking code
```

---

## 🌐 Custom Domain (Optional)

### Streamlit Cloud
1. Go to app settings
2. Add custom domain
3. Update DNS records (CNAME)
4. Wait for SSL certificate

### Other Platforms
- Heroku: Add custom domain in dashboard
- Railway: Configure in settings
- Render: Add custom domain in web service

---

## 🎯 Optimization Tips

### For Better Performance

1. **Cache Data**
   ```python
   @st.cache_data
   def load_history():
       # Your code
   ```

2. **Optimize Images**
   - Use WebP format
   - Compress images
   - Lazy loading

3. **Minimize API Calls**
   - Already implemented with rotation!
   - Use caching where possible

---

## 🆘 Getting Help

### Resources
- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Community Forum](https://discuss.streamlit.io)
- [GitHub Issues](your-repo/issues)

### Common Issues
- Check deployment logs
- Verify all dependencies installed
- Ensure API keys are correct
- Test locally first

---

## 🎉 Success!

Your AI Quiz Generator is now deployed and accessible worldwide!

**Share your app:**
- Post on social media
- Share with friends
- Add to your portfolio
- Submit to Streamlit gallery

**Next Steps:**
- Monitor usage and performance
- Collect user feedback
- Plan new features
- Update regularly

---

## 📞 Support

Need help? Contact options:
- GitHub Issues
- Email support
- Community forums

**Congratulations on deploying your app! 🚀**
