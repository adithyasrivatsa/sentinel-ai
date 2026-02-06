# ⚡ Quick Start Guide

Get Sentinel AI running in 5 minutes.

## 🎯 Choose Your Path

### Path 1: Deploy to Cloud (Recommended for Mobile)
**Best for:** Production use, mobile testing, sharing with others

```bash
# 1. Push to GitHub
git init
git add .
git commit -m "Initial commit"
git remote add origin YOUR_GITHUB_URL
git push -u origin main

# 2. Deploy to Render (Free)
# Go to: https://render.com
# Click: New → Blueprint
# Select: Your GitHub repo
# Wait: ~5 minutes
# Done: Your app is live!
```

**Result:** Live URL you can access from any device
**Time:** 5 minutes
**Cost:** FREE

---

### Path 2: Run Locally (Windows)
**Best for:** Development, testing, no internet needed

```bash
# Double-click: start.bat
# Wait: ~2 minutes for first build
# Done: Opens in browser automatically
```

**Result:** http://localhost:3000
**Time:** 2 minutes
**Cost:** FREE

---

### Path 3: Docker (All Platforms)
**Best for:** Development, full control

```bash
# Start
docker compose up --build -d

# Access
# Frontend: http://localhost:3000
# Backend:  http://localhost:8000
# API Docs: http://localhost:8000/docs

# Stop
docker compose down
```

**Time:** 2 minutes
**Cost:** FREE

---

## 📱 Mobile Setup

### After Deployment:

1. **Visit your site** on mobile browser
2. **Tap "Add to Home Screen"** when prompted
3. **Open from home screen** - works like native app!

### Features:
- ✅ Works offline
- ✅ Full screen (no browser UI)
- ✅ Fast loading
- ✅ Native feel

---

## 🔧 Configuration (Optional)

### Add Gemini API Key

1. Get key from: https://makersuite.google.com/app/apikey
2. Edit `.env` file:
   ```
   GEMINI_API_KEY=your_key_here
   ```
3. Restart app

**Note:** App works without API key (uses mock data)

---

## 🚀 Deployment Platforms

| Platform | Time | Cost | Best For |
|----------|------|------|----------|
| **Render** | 5 min | Free | Full stack |
| **Netlify** | 1 min | Free | Frontend only |
| **Railway** | 2 min | $5/mo | Easiest |
| **Fly.io** | 3 min | ~$3/mo | Performance |

### Quick Deploy Commands

**Render:**
```bash
# Just push to GitHub and use web UI
git push origin main
```

**Netlify:**
```bash
npm install -g netlify-cli
netlify deploy --prod --dir=frontend
```

**Railway:**
```bash
# Just push to GitHub and use web UI
git push origin main
```

**Fly.io:**
```bash
curl -L https://fly.io/install.sh | sh
fly launch
```

---

## 🧪 Test It Works

### Test Backend
```bash
curl http://localhost:8000/health
# Should return: {"status":"healthy"}
```

### Test Analysis
```bash
curl -X POST http://localhost:8000/analyze/text \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"Test message\"}"
```

### Test Frontend
Open browser: http://localhost:3000

---

## 🐛 Troubleshooting

### Docker not starting?
```bash
# Check Docker is running
docker info

# View logs
docker compose logs

# Restart
docker compose restart
```

### Port already in use?
```bash
# Stop existing containers
docker compose down

# Or change ports in docker-compose.yml
```

### Can't access from mobile?
```bash
# Find your IP
ipconfig  # Windows
ifconfig  # Mac/Linux

# Access from mobile
http://YOUR_IP:3000
```

### PWA not installing?
- Must use HTTPS (deploy to cloud)
- Check manifest.json is accessible
- Try different browser

---

## 📚 Next Steps

1. ✅ **Deploy** - Get it live on the internet
2. 📱 **Install** - Add to mobile home screen
3. 🎨 **Customize** - Update icons and colors
4. 🔒 **Secure** - Add API keys and secrets
5. 📊 **Monitor** - Set up analytics

---

## 🆘 Need Help?

- 📖 [Full Deployment Guide](DEPLOY.md)
- 📱 [Mobile Optimization](MOBILE.md)
- 🐛 [Report Issues](https://github.com/yourusername/sentinel/issues)

---

## ⚡ TL;DR

**Fastest way to get started:**

```bash
# Windows
start.bat

# Mac/Linux
docker compose up

# Cloud
git push → render.com → Deploy
```

**Access:** http://localhost:3000

**Done!** 🎉
