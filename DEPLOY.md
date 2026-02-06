# Quick Deployment Guide

Deploy Sentinel AI to production in minutes.

## 🚀 Fastest Options (5 minutes)

### Option 1: Render (Recommended - Free tier available)

1. Push code to GitHub
2. Go to [render.com](https://render.com)
3. Click "New" → "Blueprint"
4. Connect your repo
5. Render will auto-detect `render.yaml` and deploy everything
6. Add your `GEMINI_API_KEY` in the dashboard

**Done!** Your app will be live at `https://sentinel-frontend.onrender.com`

### Option 2: Railway (Easiest - $5/month)

1. Push code to GitHub
2. Go to [railway.app](https://railway.app)
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repo
5. Add environment variables:
   - `GEMINI_API_KEY`
   - `PORT=8000`
6. Railway auto-detects and deploys

**Done!** Your backend will be live instantly.

For frontend: Deploy `frontend/` folder to Netlify (see below).

### Option 3: Fly.io (Best performance - Pay as you go)

```bash
# Install flyctl
curl -L https://fly.io/install.sh | sh

# Login
fly auth login

# Deploy backend
cd backend
fly launch --config ../fly.toml
fly secrets set GEMINI_API_KEY=your_key_here

# Deploy frontend to Netlify (see below)
```

## 📱 Frontend-Only Deployment (Static Sites)

### Netlify (Free, instant)

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Deploy
netlify deploy --prod --dir=frontend
```

Or use the web UI:
1. Go to [netlify.com](https://netlify.com)
2. Drag and drop the `frontend` folder
3. Update API URL in `frontend/js/api.js` to your backend URL

### Vercel (Free, instant)

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel --prod
```

Or use the web UI:
1. Go to [vercel.com](https://vercel.com)
2. Import your GitHub repo
3. Vercel auto-detects `vercel.json`

## 🐳 Docker Deployment (VPS/Cloud)

### DigitalOcean, AWS, GCP, Azure

```bash
# Build and push
docker compose build
docker tag sentinel-backend your-registry/sentinel-backend
docker push your-registry/sentinel-backend

# Deploy on server
docker compose up -d
```

### Docker Hub + Any VPS

```bash
# On your machine
docker compose build
docker tag sentinel-backend yourusername/sentinel-backend
docker push yourusername/sentinel-backend

# On your VPS
docker pull yourusername/sentinel-backend
docker run -d -p 8000:8000 \
  -e GEMINI_API_KEY=your_key \
  yourusername/sentinel-backend
```

## 🔧 Environment Variables

Required for backend:
- `GEMINI_API_KEY` - Your Gemini API key (optional, uses mock data if not set)
- `API_SECRET_KEY` - Random secret for API security
- `REDIS_URL` - Redis connection (auto-provided by most platforms)

Optional:
- `MAX_UPLOAD_SIZE_MB` - Default: 50
- `FILE_RETENTION_SECONDS` - Default: 300

## 📱 PWA Setup

After deployment:
1. Visit your site on mobile
2. Browser will prompt "Add to Home Screen"
3. App installs like a native app!

To customize icons:
1. Generate icons at [realfavicongenerator.net](https://realfavicongenerator.net/)
2. Replace `frontend/icon-192.png` and `frontend/icon-512.png`

## 🔒 Security Checklist

Before going live:
- [ ] Set strong `API_SECRET_KEY`
- [ ] Add your domain to CORS settings in `backend/app/main.py`
- [ ] Enable HTTPS (most platforms do this automatically)
- [ ] Set up rate limiting (optional)
- [ ] Review file upload limits

## 📊 Monitoring

Add these to your deployment:
- **Uptime**: [UptimeRobot](https://uptimerobot.com) (free)
- **Errors**: [Sentry](https://sentry.io) (free tier)
- **Analytics**: [Plausible](https://plausible.io) or Google Analytics

## 💰 Cost Estimates

| Platform | Free Tier | Paid |
|----------|-----------|------|
| Render | ✅ 750 hrs/month | $7/month |
| Railway | ❌ | $5/month |
| Fly.io | ✅ Limited | ~$3/month |
| Netlify (frontend) | ✅ 100GB/month | $19/month |
| Vercel (frontend) | ✅ 100GB/month | $20/month |

**Recommended combo**: Render (backend) + Netlify (frontend) = **FREE**

## 🆘 Troubleshooting

### Backend won't start
- Check logs: `docker compose logs backend`
- Verify environment variables are set
- Ensure Redis is running

### Frontend can't reach backend
- Update API URL in `frontend/js/api.js`
- Check CORS settings in `backend/app/main.py`
- Verify backend is accessible

### PWA not installing
- Must be served over HTTPS
- Check `manifest.json` is accessible
- Verify service worker is registered

## 🎯 Quick Test

After deployment:
```bash
# Test backend
curl https://your-backend-url.com/health

# Test text analysis
curl -X POST https://your-backend-url.com/analyze/text \
  -H "Content-Type: application/json" \
  -d '{"text": "Test message"}'
```

## 📚 Platform-Specific Guides

- [Render Docs](https://render.com/docs)
- [Railway Docs](https://docs.railway.app)
- [Fly.io Docs](https://fly.io/docs)
- [Netlify Docs](https://docs.netlify.com)
- [Vercel Docs](https://vercel.com/docs)
