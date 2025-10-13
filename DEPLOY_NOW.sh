#!/bin/bash

# 🚀 AI Quiz Generator - Quick Deploy Script
# This script helps you deploy your app to GitHub

echo "🚀 AI Quiz Generator - Deployment Helper"
echo "=========================================="
echo ""

# Step 1: Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📝 Initializing Git repository..."
    git init
    echo "✅ Git initialized"
else
    echo "✅ Git already initialized"
fi

# Step 2: Add all files
echo ""
echo "📦 Adding files to Git..."
git add .
echo "✅ Files added"

# Step 3: Commit
echo ""
echo "💾 Creating commit..."
git commit -m "AI Quiz Generator - Ready for deployment with modern UI and features"
echo "✅ Commit created"

# Step 4: Instructions for GitHub
echo ""
echo "=========================================="
echo "🎯 NEXT STEPS:"
echo "=========================================="
echo ""
echo "1. Create a new repository on GitHub:"
echo "   👉 Go to: https://github.com/new"
echo "   👉 Repository name: ai-quiz-generator"
echo "   👉 Click 'Create repository'"
echo ""
echo "2. Run these commands (replace YOUR_USERNAME):"
echo ""
echo "   git remote add origin https://github.com/YOUR_USERNAME/ai-quiz-generator.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. Deploy on Streamlit Cloud:"
echo "   👉 Go to: https://share.streamlit.io"
echo "   👉 Sign in with GitHub"
echo "   👉 Click 'New app'"
echo "   👉 Select your repository"
echo "   👉 Main file: app.py"
echo "   👉 Add secrets (see DEPLOYMENT_GUIDE.md)"
echo "   👉 Click 'Deploy'"
echo ""
echo "=========================================="
echo "📚 Documentation:"
echo "=========================================="
echo ""
echo "- QUICK_DEPLOY.md          - Fast deployment (5 mins)"
echo "- DEPLOYMENT_GUIDE.md      - Complete guide"
echo "- DEPLOYMENT_CHECKLIST.md  - Step-by-step checklist"
echo ""
echo "✨ Your app is ready to deploy!"
echo "=========================================="
