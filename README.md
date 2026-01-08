[README.md](https://github.com/user-attachments/files/24488197/README.md)
# Live Sports Dashboard

A real-time sports scores dashboard showing NFL, NBA, and Premier League games.

## Features
- Live scores from ESPN API
- Auto-refresh every 30 seconds
- Responsive design
- Dark mode UI

## Deployment Instructions

### Deploy to Vercel (Recommended - Free)

1. **Install Vercel CLI** (optional, or use web interface):
   ```bash
   npm i -g vercel
   ```

2. **Deploy via Web**:
   - Go to [vercel.com](https://vercel.com)
   - Sign up/login with GitHub
   - Click "Add New" → "Project"
   - Import your GitHub repo or drag/drop these files
   - Vercel will auto-detect the configuration
   - Click "Deploy"

3. **Deploy via CLI**:
   ```bash
   vercel
   ```
   Follow the prompts, and your site will be live!

### Deploy to Netlify (Alternative)

1. Go to [netlify.com](https://netlify.com)
2. Drag and drop the project folder
3. Note: Netlify requires netlify.toml for redirects

### File Structure
```
├── index.html          # Main dashboard
├── vercel.json         # Vercel configuration
├── api/
│   ├── nfl.py         # NFL scores endpoint
│   ├── nba.py         # NBA scores endpoint
│   └── soccer.py      # Soccer scores endpoint
└── README.md          # This file
```

## Local Development

Run the included Python server:
```bash
python3 server.py
```

Then open http://localhost:8000/live-scores-dashboard.html

## API Endpoints

Once deployed, your API will be available at:
- `https://your-site.vercel.app/api/nfl`
- `https://your-site.vercel.app/api/nba`
- `https://your-site.vercel.app/api/soccer`

## Notes

- ESPN API is public and doesn't require authentication
- Auto-refresh is set to 30 seconds
- All times are displayed in local timezone
