# ⚡ Quick Reference Card

## 🚀 Start Commands

```bash
# Windows
start.bat

# Mac/Linux  
docker compose up

# Stop
stop.bat  # Windows
docker compose down  # Mac/Linux
```

## 🌐 URLs

```
Local Frontend:  http://localhost:3000
Local Backend:   http://localhost:8000
API Docs:        http://localhost:8000/docs
Health Check:    http://localhost:8000/health
```

## 📱 Deploy Commands

```bash
# Render (Free)
git push → render.com → New Blueprint

# Netlify (Free)
netlify deploy --prod --dir=frontend

# Railway ($5/mo)
git push → railway.app → New Project

# Fly.io (~$3/mo)
fly launch
```

## 📂 Important Files

```
frontend/
├── index.html          # Main app
├── manifest.json       # PWA config
├── sw.js              # Service worker
├── icon-192.png       # App icon (replace!)
├── icon-512.png       # App icon (replace!)
└── generate-icons.html # Icon generator

backend/
├── app/main.py        # API server
└── requirements.txt   # Dependencies

.env                   # Environment variables
docker-compose.yml     # Docker config
```

## 🎨 Customization

```bash
# Icons
Open: frontend/generate-icons.html
Download: icon-192.png, icon-512.png
Replace: In frontend/ folder

# Colors
Edit: frontend/manifest.json
  "theme_color": "#4f6df5"
  "background_color": "#f8f9fb"

# API Key
Edit: .env
  GEMINI_API_KEY=your_key_here
```

## 🧪 Testing

```bash
# Local
start.bat
Open: http://localhost:3000

# Mobile (same WiFi)
ipconfig  # Get your IP
Open: http://YOUR_IP:3000

# Lighthouse
DevTools → Lighthouse → Generate Report
```

## 🐛 Troubleshooting

```bash
# Docker not running
→ Start Docker Desktop

# Port in use
→ docker compose down

# Can't access from phone
→ Check same WiFi
→ Check firewall
→ Use IP not localhost

# PWA not installing
→ Must use HTTPS
→ Deploy to cloud first
```

## 📊 File Limits

```
Images:  50MB (JPG, PNG)
Videos:  8 seconds (MP4, MOV, WebM)
Audio:   30 seconds (MP3, WAV, M4A)
Text:    10,000 characters
```

## 🔒 Environment Variables

```bash
# Required
GEMINI_API_KEY=your_key  # Optional, uses mock if not set
API_SECRET_KEY=random    # Auto-generated

# Optional
MAX_UPLOAD_SIZE_MB=50
FILE_RETENTION_SECONDS=300
REDIS_URL=redis://redis:6379/0
```

## 📱 PWA Installation

```
iOS:
1. Safari → Share → Add to Home Screen

Android:
1. Chrome → Menu → Add to Home Screen

Or wait for automatic prompt!
```

## 🎯 Deployment Platforms

| Platform | Cost | Time | Best For |
|----------|------|------|----------|
| Render | Free | 5min | Full stack |
| Netlify | Free | 1min | Frontend |
| Railway | $5/mo | 2min | Easiest |
| Fly.io | $3/mo | 3min | Performance |

## 📚 Documentation

```
QUICKSTART.md      → 5-minute setup
DEPLOY.md          → Deployment guide
MOBILE.md          → Mobile details
MOBILE-READY.md    → Checklist
SUMMARY.md         → Complete overview
README.md          → Main docs
```

## 🔗 Useful Links

```
Render:     https://render.com
Netlify:    https://netlify.com
Railway:    https://railway.app
Fly.io:     https://fly.io
Gemini API: https://makersuite.google.com/app/apikey
Icon Gen:   https://realfavicongenerator.net
```

## ⚡ One-Liners

```bash
# Quick start
start.bat && start http://localhost:3000

# Quick deploy
git add . && git commit -m "Deploy" && git push

# Quick test
curl http://localhost:8000/health

# Quick logs
docker compose logs -f

# Quick restart
docker compose restart

# Quick clean
docker compose down -v
```

## 🎨 Color Scheme

```css
Primary:    #4f6df5  (Blue)
Background: #f8f9fb  (Light Gray)
Text:       #1a1d26  (Dark)
Success:    #22c55e  (Green)
Warning:    #f59e0b  (Orange)
Danger:     #ef4444  (Red)
```

## 📱 Breakpoints

```css
Small:      320px - 375px
Mobile:     375px - 480px
Tablet:     480px - 768px
Desktop:    768px+
```

## 🚀 Performance Targets

```
Lighthouse:     90+
First Paint:    <1s
Interactive:    <2s
PWA:            ✓ Installable
```

## 🎯 API Endpoints

```
POST /analyze/text    - Analyze text
POST /analyze/image   - Analyze image
POST /analyze/audio   - Analyze audio
POST /analyze/video   - Analyze video
GET  /health          - Health check
GET  /docs            - API documentation
```

## 💡 Quick Tips

```
✓ Test locally first
✓ Replace placeholder icons
✓ Add API key for production
✓ Deploy to HTTPS for PWA
✓ Test on real devices
✓ Monitor with Lighthouse
✓ Keep it simple
✓ Deploy often
```

---

**Need more details?** See `QUICKSTART.md` or `SUMMARY.md`

**Ready to start?** Run `start.bat` (Windows) or `docker compose up` (Mac/Linux)

**Ready to deploy?** Push to GitHub → render.com → New Blueprint
