#!/bin/bash
# Quick deployment script for Sentinel AI

echo "🚀 Sentinel AI - Quick Deploy"
echo "=============================="
echo ""

# Check if git is initialized
if [ ! -d .git ]; then
    echo "📦 Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit - Sentinel AI"
fi

echo "Choose deployment platform:"
echo "1) Render (Free - Recommended)"
echo "2) Railway ($5/month)"
echo "3) Fly.io (Pay as you go)"
echo "4) Netlify (Frontend only)"
echo "5) Docker (Local/VPS)"
echo ""
read -p "Enter choice (1-5): " choice

case $choice in
    1)
        echo ""
        echo "📋 Render Deployment Steps:"
        echo "1. Push code to GitHub:"
        echo "   git remote add origin YOUR_GITHUB_URL"
        echo "   git push -u origin main"
        echo ""
        echo "2. Go to https://render.com"
        echo "3. Click 'New' → 'Blueprint'"
        echo "4. Connect your GitHub repo"
        echo "5. Render will auto-deploy using render.yaml"
        echo ""
        echo "✅ Done! Your app will be live in ~5 minutes"
        ;;
    2)
        echo ""
        echo "📋 Railway Deployment Steps:"
        echo "1. Push code to GitHub:"
        echo "   git remote add origin YOUR_GITHUB_URL"
        echo "   git push -u origin main"
        echo ""
        echo "2. Go to https://railway.app"
        echo "3. Click 'New Project' → 'Deploy from GitHub'"
        echo "4. Select your repo"
        echo "5. Add environment variables in dashboard"
        echo ""
        echo "✅ Done! Your app will be live instantly"
        ;;
    3)
        echo ""
        echo "📋 Fly.io Deployment:"
        if ! command -v flyctl &> /dev/null; then
            echo "Installing flyctl..."
            curl -L https://fly.io/install.sh | sh
        fi
        echo ""
        echo "Logging in to Fly.io..."
        fly auth login
        echo ""
        echo "Deploying backend..."
        cd backend
        fly launch --config ../fly.toml
        echo ""
        read -p "Enter your GEMINI_API_KEY: " api_key
        fly secrets set GEMINI_API_KEY=$api_key
        echo ""
        echo "✅ Backend deployed!"
        echo "Deploy frontend to Netlify (option 4)"
        ;;
    4)
        echo ""
        echo "📋 Netlify Deployment:"
        if ! command -v netlify &> /dev/null; then
            echo "Installing Netlify CLI..."
            npm install -g netlify-cli
        fi
        echo ""
        echo "Deploying frontend..."
        netlify deploy --prod --dir=frontend
        echo ""
        echo "✅ Frontend deployed!"
        echo "Update API URL in frontend/js/api.js if needed"
        ;;
    5)
        echo ""
        echo "🐳 Starting Docker containers..."
        docker compose up --build -d
        echo ""
        echo "✅ App running at:"
        echo "   Frontend: http://localhost:3000"
        echo "   Backend:  http://localhost:8000"
        echo "   API Docs: http://localhost:8000/docs"
        ;;
    *)
        echo "Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "📚 For detailed instructions, see DEPLOY.md"
