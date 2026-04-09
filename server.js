'use strict';

const express = require('express');
const helmet  = require('helmet');
const cors    = require('cors');
const rateLimit = require('express-rate-limit');
const Database  = require('better-sqlite3');
const path      = require('path');
const { randomUUID } = require('crypto');

// ── DB ──────────────────────────────────────────────────────────────────────
const db = new Database(path.join(__dirname, 'data', 'tips.db'));
db.exec(`
  CREATE TABLE IF NOT EXISTS tips (
    id          TEXT PRIMARY KEY,
    subject     TEXT NOT NULL,
    body        TEXT NOT NULL,
    contact     TEXT,
    ip_hash     TEXT,
    created_at  TEXT NOT NULL DEFAULT (datetime('now'))
  );
  CREATE TABLE IF NOT EXISTS searches (
    query      TEXT NOT NULL,
    count      INTEGER DEFAULT 1,
    PRIMARY KEY (query)
  );
`);

const insertTip = db.prepare(`
  INSERT INTO tips (id, subject, body, contact, ip_hash)
  VALUES (@id, @subject, @body, @contact, @ip_hash)
`);
const allTips = db.prepare(`SELECT * FROM tips ORDER BY created_at DESC`);
const deleteTip = db.prepare(`DELETE FROM tips WHERE id = ?`);

// ── SEARCH INDEX ─────────────────────────────────────────────────────────────
// Loaded once at startup from a static JSON file
let searchIndex = [];
try {
  searchIndex = require('./data/search-index.json');
} catch {
  console.warn('search-index.json not found — run npm run build-index');
}

// ── APP ──────────────────────────────────────────────────────────────────────
const app = express();

app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      styleSrc:   ["'self'", "'unsafe-inline'", "https://fonts.googleapis.com"],
      fontSrc:    ["'self'", "https://fonts.gstatic.com"],
      imgSrc:     ["'self'", "data:", "https://upload.wikimedia.org"],
      scriptSrc:  ["'self'", "'unsafe-inline'"],
    },
  },
}));
app.use(cors());
app.use(express.json({ limit: '32kb' }));
app.use(express.static(path.join(__dirname), {
  index: 'index.html',
  extensions: ['html'],
}));

// ── RATE LIMITS ───────────────────────────────────────────────────────────────
const tipLimit = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 min
  max: 5,
  message: { error: 'Слишком много запросов. Попробуйте через 15 минут.' },
});
const searchLimit = rateLimit({
  windowMs: 60 * 1000,
  max: 30,
});

// ── UTIL ──────────────────────────────────────────────────────────────────────
function hashIP(ip) {
  const { createHash } = require('crypto');
  return createHash('sha256').update(ip + process.env.IP_SALT || 'salt').digest('hex').slice(0, 16);
}

// ── API: SUBMIT TIP ───────────────────────────────────────────────────────────
app.post('/api/tips', tipLimit, (req, res) => {
  const { subject, body, contact } = req.body || {};

  if (!subject || typeof subject !== 'string' || subject.trim().length < 3) {
    return res.status(400).json({ error: 'Укажите тему сообщения.' });
  }
  if (!body || typeof body !== 'string' || body.trim().length < 10) {
    return res.status(400).json({ error: 'Сообщение слишком короткое.' });
  }
  if (subject.length > 200 || body.length > 5000) {
    return res.status(400).json({ error: 'Сообщение слишком длинное.' });
  }

  const ip = req.headers['x-forwarded-for']?.split(',')[0] ?? req.ip ?? '';
  insertTip.run({
    id:      randomUUID(),
    subject: subject.trim().slice(0, 200),
    body:    body.trim().slice(0, 5000),
    contact: contact ? contact.trim().slice(0, 200) : null,
    ip_hash: hashIP(ip),
  });

  res.json({ ok: true, message: 'Сообщение получено. Спасибо.' });
});

// ── API: SEARCH ───────────────────────────────────────────────────────────────
app.get('/api/search', searchLimit, (req, res) => {
  const q = (req.query.q || '').trim().toLowerCase();
  if (!q || q.length < 2) return res.json({ results: [] });

  const results = searchIndex
    .map(entry => {
      let score = 0;
      if (entry.name.toLowerCase().includes(q)) score += 10;
      if (entry.tags?.some(t => t.toLowerCase().includes(q))) score += 5;
      if (entry.bio?.toLowerCase().includes(q)) score += 2;
      if (entry.quotes?.some(qt => qt.toLowerCase().includes(q))) score += 3;
      return { ...entry, score };
    })
    .filter(e => e.score > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, 10)
    .map(({ score, bio, quotes, ...rest }) => rest); // strip heavy fields

  res.json({ results });
});

// ── ADMIN ─────────────────────────────────────────────────────────────────────
const ADMIN_PASS = process.env.ADMIN_PASS || 'change-me-in-env';

function basicAuth(req, res, next) {
  const auth = req.headers['authorization'];
  if (!auth || !auth.startsWith('Basic ')) {
    res.set('WWW-Authenticate', 'Basic realm="Admin"');
    return res.status(401).send('Требуется авторизация');
  }
  const [, user, pass] = Buffer.from(auth.slice(6), 'base64').toString().match(/^([^:]*):(.*)$/);
  if (user === 'admin' && pass === ADMIN_PASS) return next();
  res.set('WWW-Authenticate', 'Basic realm="Admin"');
  res.status(401).send('Неверный пароль');
}

app.get('/admin/tips', basicAuth, (req, res) => {
  const tips = allTips.all();
  const html = `<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<title>Входящие сообщения</title>
<style>
  body { font-family: monospace; background: #0a0a0a; color: #e0d8c8; padding: 40px; }
  h1 { color: #8b1a1a; margin-bottom: 24px; }
  .tip { border: 1px solid #2a2a2a; padding: 20px; margin-bottom: 16px; border-radius: 4px; }
  .tip-meta { color: #666; font-size: 12px; margin-bottom: 8px; }
  .tip-subject { color: #c8b08a; font-size: 14px; font-weight: bold; margin-bottom: 8px; }
  .tip-body { white-space: pre-wrap; font-size: 13px; }
  .tip-contact { color: #6a9a6a; font-size: 12px; margin-top: 8px; }
  form.del { display:inline; }
  button { background:#5c1111; color:#fff; border:none; padding:4px 10px; cursor:pointer; border-radius:2px; font-size:11px; }
  .empty { color: #444; font-style: italic; }
  .count { color: #555; margin-bottom: 32px; }
</style>
</head>
<body>
<h1>Голоса Кремля — Входящие</h1>
<p class="count">${tips.length} сообщений</p>
${tips.length === 0
  ? '<p class="empty">Сообщений нет.</p>'
  : tips.map(t => `
  <div class="tip">
    <div class="tip-meta">${t.created_at} · id: ${t.id.slice(0,8)}</div>
    <div class="tip-subject">Тема: ${escHtml(t.subject)}</div>
    <div class="tip-body">${escHtml(t.body)}</div>
    ${t.contact ? `<div class="tip-contact">Контакт: ${escHtml(t.contact)}</div>` : ''}
    <form class="del" method="POST" action="/admin/tips/${t.id}/delete" onsubmit="return confirm('Удалить?')">
      <button type="submit">Удалить</button>
    </form>
  </div>`).join('')}
</body></html>`;
  res.send(html);
});

app.post('/admin/tips/:id/delete', basicAuth, (req, res) => {
  deleteTip.run(req.params.id);
  res.redirect('/admin/tips');
});

function escHtml(str) {
  return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

// ── 404 ───────────────────────────────────────────────────────────────────────
app.use((req, res) => {
  res.status(404).sendFile(path.join(__dirname, '404.html'));
});

// ── START ─────────────────────────────────────────────────────────────────────
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Голоса Кремля запущены на http://localhost:${PORT}`));
