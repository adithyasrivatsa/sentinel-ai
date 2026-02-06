# App Icons Guide

Replace placeholder icons with your actual app icons.

## Required Icons

### icon-192.png
- **Size:** 192x192 pixels
- **Format:** PNG
- **Purpose:** Android home screen, app drawer
- **Background:** Should include background color

### icon-512.png
- **Size:** 512x512 pixels
- **Format:** PNG
- **Purpose:** Android splash screen, high-res displays
- **Background:** Should include background color

## Quick Icon Generation

### Option 0: Built-in Generator (Fastest!)
1. Open `frontend/generate-icons.html` in your browser
2. Customize colors and text
3. Click "Generate Icons"
4. Download both icons
5. Replace files in `frontend/` folder

**Time:** 1 minute
**No internet required!**

### Option 1: Online Generator (Easiest)
1. Go to: https://realfavicongenerator.net/
2. Upload your logo/icon (at least 512x512)
3. Configure settings:
   - iOS: Select "Add solid, plain background"
   - Android: Select "Use a distinct picture for Android"
   - Background color: #4f6df5 (or your brand color)
4. Generate and download
5. Replace files in `frontend/` folder

### Option 2: PWA Asset Generator
1. Go to: https://www.pwabuilder.com/imageGenerator
2. Upload your icon (512x512 minimum)
3. Download generated assets
4. Replace icon-192.png and icon-512.png

### Option 3: Manual Creation

Using any image editor (Photoshop, Figma, Canva):

**icon-192.png:**
- Canvas: 192x192px
- Background: #4f6df5 (or transparent)
- Icon: Centered, ~140px
- Export: PNG, optimized

**icon-512.png:**
- Canvas: 512x512px
- Background: #4f6df5 (or transparent)
- Icon: Centered, ~380px
- Export: PNG, optimized

## Design Guidelines

### iOS
- Use solid background color
- No transparency
- Icon should be simple and recognizable
- Avoid text (will be too small)

### Android
- Can use transparency
- Maskable safe zone: 80% of canvas
- Keep important elements in center
- Test with different shapes (circle, square, rounded)

## Icon Design Tips

✅ **Do:**
- Use simple, bold shapes
- High contrast
- Recognizable at small sizes
- Consistent with brand
- Test on actual devices

❌ **Don't:**
- Use photos
- Include small text
- Use gradients (unless subtle)
- Make it too complex
- Forget safe zones

## Testing Icons

### Browser DevTools
1. Open DevTools (F12)
2. Application tab → Manifest
3. Check icons load correctly
4. Verify sizes and formats

### Real Device
1. Deploy to test server (HTTPS required)
2. Add to home screen
3. Check icon appearance
4. Test on multiple devices

## Current Placeholder

The current icon files are placeholders. Replace them with:
- Your logo
- Shield icon (matches app theme)
- Custom design

## Color Scheme

Current theme:
- Primary: #4f6df5 (blue)
- Background: #f8f9fb (light gray)
- Text: #1a1d26 (dark)

Match your icons to this scheme or update the theme in:
- `frontend/manifest.json` (theme_color)
- `frontend/css/styles.css` (--color-primary)
- `frontend/index.html` (meta theme-color)

## Example Icon Concepts

### Shield (Current Theme)
- Simple shield outline
- Checkmark inside
- Blue background
- White icon

### AI Detection
- Eye icon
- Magnifying glass
- Scan lines
- Circuit pattern

### Security
- Lock icon
- Shield with star
- Fingerprint
- Badge

## Resources

- [PWA Icon Guidelines](https://web.dev/add-manifest/#icons)
- [iOS Icon Guidelines](https://developer.apple.com/design/human-interface-guidelines/app-icons)
- [Android Adaptive Icons](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive)
- [Icon Generator](https://realfavicongenerator.net/)
- [PWA Builder](https://www.pwabuilder.com/)
