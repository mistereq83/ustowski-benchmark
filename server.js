const express = require('express');
const multer = require('multer');
const sharp = require('sharp');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;

// --- Config ---
const API_TOKEN = process.env.ADMIN_TOKEN || 'ustowski-admin-2026';
const DATA_FILE = path.join(__dirname, 'data', 'content.json');
const UPLOADS_DIR = path.join(__dirname, 'public', 'images', 'projects');

// Ensure dirs exist
fs.mkdirSync(UPLOADS_DIR, { recursive: true });
fs.mkdirSync(path.join(__dirname, 'data'), { recursive: true });

// --- Middleware ---
app.use(express.json({ limit: '50mb' }));
app.use(express.static('public'));

// CORS for admin panel
app.use('/api', (req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  res.header('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS');
  if (req.method === 'OPTIONS') return res.sendStatus(200);
  next();
});

// Auth middleware
const auth = (req, res, next) => {
  const token = req.headers.authorization?.replace('Bearer ', '');
  if (token !== API_TOKEN) return res.status(401).json({ error: 'Unauthorized' });
  next();
};

// --- Helper ---
function readContent() {
  try { return JSON.parse(fs.readFileSync(DATA_FILE, 'utf8')); }
  catch { return { pricing: { lastUpdated: '', services: [] }, reviews: [], projects: [] }; }
}

function writeContent(data) {
  fs.writeFileSync(DATA_FILE, JSON.stringify(data, null, 2), 'utf8');
}

// --- Public API (no auth) ---

// Get content (for frontend loader)
app.get('/api/content', (req, res) => {
  res.json(readContent());
});

// --- Admin API (auth required) ---

// Save full content
app.post('/api/content', auth, (req, res) => {
  try {
    const data = req.body;
    data.pricing.lastUpdated = new Date().toISOString().split('T')[0];
    writeContent(data);
    res.json({ ok: true, message: 'Zapisano' });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

// Upload image (before/after for projects)
const upload = multer({ storage: multer.memoryStorage(), limits: { fileSize: 20 * 1024 * 1024 } });

app.post('/api/upload', auth, upload.single('image'), async (req, res) => {
  try {
    if (!req.file) return res.status(400).json({ error: 'Brak pliku' });
    
    const id = req.body.projectId || `img-${Date.now()}`;
    const type = req.body.type || 'after'; // 'before' or 'after'
    const filename = `${id}-${type}.webp`;
    const filepath = path.join(UPLOADS_DIR, filename);
    
    // Convert to WebP, resize to max 1600px wide
    await sharp(req.file.buffer)
      .resize(1600, null, { withoutEnlargement: true })
      .webp({ quality: 82 })
      .toFile(filepath);
    
    const url = `/images/projects/${filename}`;
    res.json({ ok: true, url, filename });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

// Delete project image
app.delete('/api/upload/:filename', auth, (req, res) => {
  const filepath = path.join(UPLOADS_DIR, path.basename(req.params.filename));
  try { fs.unlinkSync(filepath); } catch {}
  res.json({ ok: true });
});

// --- Health check ---
app.get('/api/health', (req, res) => {
  res.json({ ok: true, pages: fs.readdirSync(path.join(__dirname, 'public')).filter(f => f.endsWith('.html')).length });
});

// --- SPA fallback: serve index.html for non-file routes ---
app.get('*', (req, res) => {
  const file = path.join(__dirname, 'public', req.path);
  if (fs.existsSync(file)) return res.sendFile(file);
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`🏠 Ustowski server running on port ${PORT}`);
  console.log(`📄 ${fs.readdirSync(path.join(__dirname, 'public')).filter(f => f.endsWith('.html')).length} HTML pages`);
  console.log(`🔑 Admin token: ${API_TOKEN.substring(0, 8)}...`);
});
