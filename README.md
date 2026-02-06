# Sentinel AI

**Mobile-optimized AI content checker - Deploy in 5 minutes**

Check if content is AI-generated or a scam. Works as a Progressive Web App (PWA) on mobile devices.

---

## 🚀 Quick Links

- **[⚡ Quick Start](QUICKSTART.md)** - Get running in 5 minutes
- **[📱 Mobile Ready](MOBILE-READY.md)** - Everything you need to know
- **[🚀 Deploy Guide](DEPLOY.md)** - Production deployment
- **[📋 Quick Reference](QUICK-REFERENCE.md)** - Commands & tips

---

## ✨ Features

- 📱 **Mobile-First Design** - Optimized for phones and tablets
- 🚀 **PWA Support** - Install like a native app
- 🔍 **Multi-Format Analysis** - Images, videos, audio, and text
- ⚡ **Fast Deployment** - Live in 5 minutes
- 🆓 **Free Hosting** - Deploy on free tiers

## 🚀 Quick Deploy (5 minutes)

### Step 1: Get API Keys (Free)

You'll need two free API keys:

1. **Gemini API** (Google): https://makersuite.google.com/app/apikey
2. **AssemblyAI**: https://www.assemblyai.com/dashboard/signup

### Step 2: Fastest - Render (Free)

```bash
# 1. Push to GitHub
git init
git add .
git commit -m "Initial commit"
git remote add origin YOUR_GITHUB_URL
git push -u origin main

# 2. Go to render.com → New → Blueprint
# 3. Connect your repo
# 4. Done! Auto-deploys everything
```

### Alternative: One-Click Deploy

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

**See [DEPLOY.md](DEPLOY.md) for all deployment options**

## 📱 Mobile Features

- **PWA Installation** - Add to home screen for app-like experience
- **Touch-Optimized** - Large tap targets, smooth interactions
- **Responsive Design** - Works on all screen sizes
- **Offline Support** - Service worker caching
- **Safe Area Support** - Works with notched devices

## 🎯 Supported Content

| Type | Formats | Limits |
|------|---------|--------|
| Image | JPG, PNG | 50MB |
| Video | MP4, MOV, WebM | 8 seconds |
| Audio | MP3, WAV, M4A | 30 seconds |
| Text | Plain text | 10,000 chars |

## 🏃 Local Development

```bash
# Start everything
docker compose up --build

# Access
# Frontend: http://localhost:3000
# Backend:  http://localhost:8000
# API Docs: http://localhost:8000/docs
```

## 📦 Project Structure

```
sentinel/
├── frontend/           # Mobile-optimized PWA
│   ├── manifest.json  # PWA config
│   ├── sw.js          # Service worker
│   └── ...
├── backend/           # FastAPI backend
├── DEPLOY.md         # Deployment guide
└── docker-compose.yml
```

## 🔧 Configuration

Create `.env` file:

```bash
GEMINI_API_KEY=your_key_here  # Optional
API_SECRET_KEY=random_secret
```

## 🌐 Deployment Options

| Platform | Cost | Deploy Time | Best For |
|----------|------|-------------|----------|
| **Render** | Free | 5 min | Full stack |
| **Railway** | $5/mo | 2 min | Easiest |
| **Fly.io** | ~$3/mo | 3 min | Performance |
| **Netlify** | Free | 1 min | Frontend only |
| **Vercel** | Free | 1 min | Frontend only |

## 📱 PWA Installation

After deployment:
1. Visit site on mobile browser
2. Tap "Add to Home Screen"
3. App installs like native app!

## 🔒 Security

- HTTPS enforced
- File size limits
- Input validation
- CORS protection
- Rate limiting ready

## 📊 API Example

```bash
curl -X POST https://your-app.com/api/analyze/text \
  -H "Content-Type: application/json" \
  -d '{"text": "Check this message!"}'
```

Response:
```json
{
  "risk_score": 25,
  "verdict": "Likely Safe",
  "explanations": ["Content appears authentic"],
  "action": "This looks safe to proceed"
}
```

## 🆘 Support

- 📚 [Deployment Guide](DEPLOY.md)
- 🐛 [Report Issues](https://github.com/yourusername/sentinel/issues)
- 💬 [Discussions](https://github.com/yourusername/sentinel/discussions)

## ⚠️ Disclaimer

This tool provides estimates only. Always verify important information through trusted sources.

## 📄 License

Apache License 2.0
