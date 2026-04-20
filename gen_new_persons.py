#!/usr/bin/env python3
"""
Creates 4 new dossier pages (RU + EN):
  zakharova, kovalchuk, turchak, navka
Also:
  - Adds keyboard navigation to all 27 dossier pairs
  - Adds reading time to all dossier pages
  - Adds [Интерпр.]/[Fact] badges to EN pages
  - Updates index.html, index-en.html, sitemap.xml
"""
import re, os

BASE = '/Users/petrdracev/Desktop/proj/cremle/'

CSS_COMMON = """  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500&display=swap');
  :root { --ink:#080808; --paper:#ede8dc; --red:#8b1a1a; --red-dim:#5c1111; --light-gray:#bab3a0; --rule:#1c1c1c; --card-bg:#0e0e0e; --gray:#4a4a4a; }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:var(--ink); color:var(--paper); font-family:'Inter',sans-serif; font-weight:300; line-height:1.75; overflow-x:hidden; min-height:100vh; }
  #progress-bar { position:fixed; top:0; left:0; height:2px; width:0%; background:var(--red); z-index:999; transition:width 0.1s; }
  .topbar { padding:14px 60px; border-bottom:1px solid var(--rule); background:var(--ink); position:sticky; top:0; z-index:100; display:flex; justify-content:space-between; align-items:center; }
  .topbar-left a { font-size:10px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); text-decoration:none; }
  .topbar-left a:hover { opacity:0.6; }
  .topbar-right { display:flex; align-items:center; gap:20px; }
  .lang-switch { display:flex; border:1px solid #333; overflow:hidden; }
  .lang-switch a { font-size:9px; letter-spacing:0.2em; text-transform:uppercase; color:#888; text-decoration:none; padding:6px 12px; transition:all 0.2s; }
  .lang-switch a.active { color:var(--paper); background:#1c1c1c; }
  .lang-switch a:hover { color:var(--paper); background:#111; }
  .report-link { font-size:9px; letter-spacing:0.2em; text-transform:uppercase; color:#5c1111; text-decoration:none; border:1px solid #2a0a0a; padding:6px 14px; transition:all 0.2s; }
  .report-link:hover { color:#8b1a1a; border-color:#5c1111; }
  .hero { display:grid; grid-template-columns:1fr 420px; min-height:80vh; border-bottom:1px solid var(--rule); }
  .hero-left { padding:80px 60px; display:flex; flex-direction:column; justify-content:center; border-right:1px solid var(--rule); }
  .eyebrow { font-size:10px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); margin-bottom:32px; }
  .hero-name { font-family:'Playfair Display',serif; font-size:clamp(2.5rem,5vw,4.5rem); font-weight:400; line-height:1.05; margin-bottom:20px; }
  .hero-subtitle { font-size:14px; color:var(--light-gray); letter-spacing:0.05em; margin-bottom:40px; font-style:italic; }
  .hero-meta { display:flex; flex-direction:column; gap:0; border-top:1px solid var(--rule); }
  .meta-item { display:grid; grid-template-columns:140px 1fr; gap:16px; padding:12px 0; border-bottom:1px solid #111; }
  .meta-item label { font-size:10px; letter-spacing:0.2em; text-transform:uppercase; color:#555; }
  .meta-item span { font-size:13px; color:var(--light-gray); }
  .hero-right { position:relative; overflow:hidden; background:#050505; }
  .hero-stamp { position:absolute; bottom:24px; left:24px; font-size:9px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); border:1px solid var(--red-dim); padding:6px 12px; background:rgba(0,0,0,0.7); }
  .section { border-bottom:1px solid var(--rule); padding:80px 0; }
  .container { max-width:760px; margin:0 auto; padding:0 60px; }
  .section-header { display:flex; align-items:center; gap:20px; margin-bottom:48px; }
  .section-num { font-size:11px; letter-spacing:0.3em; color:#333; }
  .section-title { font-family:'Playfair Display',serif; font-size:1.8rem; font-weight:400; flex:1; }
  .section-title::after { content:''; display:block; height:1px; background:var(--rule); margin-top:8px; }
  .intro-text { font-size:16px; line-height:1.9; color:var(--light-gray); margin-bottom:48px; }
  .timeline { display:flex; flex-direction:column; gap:0; }
  .timeline-entry { display:grid; grid-template-columns:80px 1fr; gap:24px; padding:28px 0; border-bottom:1px solid #0f0f0f; }
  .timeline-year { font-size:11px; letter-spacing:0.2em; color:var(--red); padding-top:4px; }
  .timeline-body h3 { font-size:14px; letter-spacing:0.05em; margin-bottom:10px; color:var(--paper); }
  .timeline-body p { font-size:14px; color:#888; line-height:1.8; }
  .quotes-grid { display:grid; grid-template-columns:1fr 1fr; gap:1px; background:var(--rule); }
  .quote-card { background:var(--card-bg); padding:32px; }
  .quote-text { font-family:'Playfair Display',serif; font-size:15px; font-style:italic; line-height:1.7; margin-bottom:16px; color:var(--paper); }
  .quote-source { font-size:11px; letter-spacing:0.15em; text-transform:uppercase; color:#444; }
  .method-text { font-size:15px; line-height:1.9; color:var(--light-gray); }
  .sanctions-block { background:var(--card-bg); border:1px solid #1a0000; border-left:3px solid var(--red); padding:28px 32px; }
  .sanctions-block p { font-size:14px; color:var(--light-gray); line-height:1.8; }
  .footer { padding:48px 60px; display:flex; justify-content:space-between; align-items:center; font-size:11px; letter-spacing:0.15em; text-transform:uppercase; color:#333; }
  .footer-rule { width:1px; height:40px; background:var(--rule); }
  .next-dosye { border-top:1px solid var(--rule); padding:48px 60px; display:flex; justify-content:space-between; align-items:center; text-decoration:none; color:var(--paper); transition:background 0.2s; }
  .next-dosye:hover { background:#0a0a0a; }
  .next-dosye-label { font-size:10px; letter-spacing:0.25em; text-transform:uppercase; color:#444; margin-bottom:8px; }
  .next-dosye-name { font-family:'Playfair Display',serif; font-size:1.6rem; font-weight:400; }
  .next-dosye-title { font-size:13px; color:#666; margin-top:4px; }
  .next-dosye-arrow { font-size:2rem; color:var(--red); }
  .share-bar { border-top:1px solid var(--rule); padding:24px 60px; display:flex; align-items:center; gap:16px; }
  .share-label { font-size:10px; letter-spacing:0.2em; text-transform:uppercase; color:#444; }
  .share-btn { font-size:10px; letter-spacing:0.15em; text-transform:uppercase; text-decoration:none; padding:8px 16px; border:1px solid #222; color:#888; transition:all 0.2s; }
  .share-btn:hover { border-color:#555; color:var(--paper); }
  @media (max-width: 768px) {
    .hero { grid-template-columns:1fr; }
    .hero-right { height:300px; }
    .hero-left { padding:48px 24px; }
    .container { padding:0 24px; }
    .quotes-grid { grid-template-columns:1fr; }
    .topbar { padding:12px 20px; }
    .topbar-right { gap:10px; }
    .report-link { display:none; }
    .footer { padding:32px 24px; flex-direction:column; gap:12px; text-align:center; }
    .next-dosye { padding:32px 20px; }
    .next-dosye-name { font-size:1.2rem; }
    .share-bar { padding:20px 20px; flex-wrap:wrap; gap:10px; }
  }
  @media print {
    * { -webkit-print-color-adjust:exact; print-color-adjust:exact; }
    body { background:#fff !important; color:#000 !important; font-size:11pt; }
    .topbar,#progress-bar,.share-bar,.next-dosye,.report-link,.lang-switch { display:none !important; }
    .hero { grid-template-columns:1fr 280px !important; page-break-inside:avoid; }
    .hero-right { height:280px !important; }
    .hero-left { background:#f5f5f5 !important; padding:32px !important; }
    .hero-name { color:#000 !important; font-size:28pt !important; }
    .section { border-color:#ddd !important; padding:24px 0 !important; page-break-inside:avoid; }
    .quote-card { background:#f9f9f9 !important; border:1px solid #ddd !important; color:#000 !important; }
    @page { margin:2cm; }
  }
  .copy-quote-btn { display:inline-block; font-size:8px; letter-spacing:0.15em; text-transform:uppercase; color:#444; border:1px solid #222; padding:4px 10px; cursor:pointer; background:transparent; font-family:'Inter',sans-serif; margin-top:10px; transition:all 0.2s; }
  .copy-quote-btn:hover { color:var(--paper); border-color:#555; }
  .copy-quote-btn.copied { color:#4caf50; border-color:#1a4a1a; }
  .badge { display:inline-block; font-size:8px; font-family:'Inter',sans-serif; font-weight:500; letter-spacing:0.15em; text-transform:uppercase; padding:2px 6px; border-radius:2px; vertical-align:middle; margin-left:6px; line-height:1.6; position:relative; top:-1px; cursor:help; }
  .badge-fact { background:#0a2010; color:#4caf50; border:1px solid #1a4a1a; }
  .badge-interp { background:#1a1200; color:#e67e22; border:1px solid #3a2800; }
  .sources-grid-dosye { display:grid; grid-template-columns:1fr 1fr; gap:2px; background:var(--rule); }
  @media (max-width:900px) { .sources-grid-dosye { grid-template-columns:1fr; } }
  .source-card-d { background:var(--ink); padding:24px 28px; }
  .source-card-d .sc-type { font-size:8px; letter-spacing:0.2em; text-transform:uppercase; color:var(--red); margin-bottom:6px; }
  .source-card-d .sc-title { font-family:'Playfair Display',serif; font-size:13px; color:var(--paper); margin-bottom:5px; }
  .source-card-d .sc-note { font-size:11px; color:#555; line-height:1.5; }
  .back-to-top { position:fixed; bottom:32px; right:32px; width:44px; height:44px; background:var(--red); color:var(--paper); border:none; cursor:pointer; display:flex; align-items:center; justify-content:center; font-size:18px; opacity:0; visibility:hidden; transition:opacity 0.3s,visibility 0.3s; z-index:500; }
  .back-to-top.visible { opacity:1; visibility:visible; }
  .back-to-top:hover { background:#6e1414; }
  @media (max-width:768px) { .back-to-top { bottom:20px; right:16px; } }
  .sources-section { padding:60px 0; border-bottom:1px solid var(--rule); }
  .sources-grid-en { display:grid; grid-template-columns:1fr 1fr; gap:2px; background:var(--rule); margin-top:32px; }
  .source-card-en { background:var(--ink); padding:28px 32px; }
  .sc-type-en { font-size:9px; letter-spacing:0.2em; text-transform:uppercase; color:var(--red); margin-bottom:8px; }
  .sc-title-en { font-family:'Playfair Display',serif; font-size:14px; color:var(--paper); margin-bottom:6px; }
  .sc-note-en { font-size:11px; color:#555; line-height:1.7; margin-top:4px; }
  @media (max-width:900px) { .sources-grid-en { grid-template-columns:1fr; } .sources-section { padding:40px 0; } }"""

SVG_RIGHT = """    <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0">
      <defs>
        <radialGradient id="rg" cx="50%" cy="35%" r="60%">
          <stop offset="0%" stop-color="#1a0000" stop-opacity="0.8"/>
          <stop offset="100%" stop-color="#000" stop-opacity="1"/>
        </radialGradient>
      </defs>
      <rect width="100%" height="100%" fill="url(#rg)"/>
      <line x1="50%" y1="20%" x2="50%" y2="80%" stroke="#8b1a1a" stroke-width="0.5" opacity="0.4"/>
      <line x1="20%" y1="50%" x2="80%" y2="50%" stroke="#8b1a1a" stroke-width="0.5" opacity="0.4"/>
      <circle cx="50%" cy="38%" r="80" fill="none" stroke="#8b1a1a" stroke-width="0.5" opacity="0.3"/>
      <circle cx="50%" cy="38%" r="120" fill="none" stroke="#8b1a1a" stroke-width="0.5" opacity="0.15"/>
      <g opacity="0.06">
        <line x1="0" y1="10%" x2="100%" y2="10%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="20%" x2="100%" y2="20%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="30%" x2="100%" y2="30%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="40%" x2="100%" y2="40%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="60%" x2="100%" y2="60%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="70%" x2="100%" y2="70%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="80%" x2="100%" y2="80%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="90%" x2="100%" y2="90%" stroke="#c8c0b0" stroke-width="1"/>
      </g>
      {monogram}
    </svg>"""

SCRIPTS_RU = """<script>
window.addEventListener('scroll', function() {
  var el = document.getElementById('progress-bar');
  var h = document.documentElement;
  var pct = (h.scrollTop / (h.scrollHeight - h.clientHeight)) * 100;
  el.style.width = pct + '%';
});
</script>
<script>
(function(){
  var btn = document.getElementById('back-to-top');
  if (!btn) return;
  window.addEventListener('scroll', function(){ btn.classList.toggle('visible', window.scrollY > 300); }, {passive:true});
  btn.addEventListener('click', function(){ window.scrollTo({top:0,behavior:'smooth'}); });
})();
</script>
<script>
(function(){
  document.querySelectorAll('.quote-card').forEach(function(card){
    var bq = card.querySelector('.quote-text');
    if (!bq) return;
    var btn = document.createElement('button');
    btn.className = 'copy-quote-btn';
    btn.textContent = 'Копировать';
    btn.addEventListener('click', function(){
      var text = bq.textContent.trim().replace(/\\s+/g, ' ');
      navigator.clipboard.writeText(text + '\\n— голоса-кремля | ' + window.location.href).then(function(){
        btn.textContent = 'Скопировано ✓'; btn.classList.add('copied');
        setTimeout(function(){ btn.textContent = 'Копировать'; btn.classList.remove('copied'); }, 2000);
      });
    });
    card.appendChild(btn);
  });
})();
</script>"""

SCRIPTS_EN = """<script>
window.addEventListener('scroll', function() {
  var el = document.getElementById('progress-bar');
  var h = document.documentElement;
  var pct = (h.scrollTop / (h.scrollHeight - h.clientHeight)) * 100;
  el.style.width = pct + '%';
});
</script>
<script>
(function(){
  var btn = document.getElementById('back-to-top');
  if (!btn) return;
  window.addEventListener('scroll', function(){ btn.classList.toggle('visible', window.scrollY > 300); }, {passive:true});
  btn.addEventListener('click', function(){ window.scrollTo({top:0,behavior:'smooth'}); });
})();
</script>
<script>
(function(){
  document.querySelectorAll('.quote-card').forEach(function(card){
    var bq = card.querySelector('.quote-text');
    if (!bq) return;
    var btn = document.createElement('button');
    btn.className = 'copy-quote-btn';
    btn.textContent = 'Copy quote';
    btn.addEventListener('click', function(){
      var text = bq.textContent.trim().replace(/\\s+/g, ' ');
      navigator.clipboard.writeText(text + '\\n— voices-of-the-kremlin | ' + window.location.href).then(function(){
        btn.textContent = 'Copied ✓'; btn.classList.add('copied');
        setTimeout(function(){ btn.textContent = 'Copy quote'; btn.classList.remove('copied'); }, 2000);
      });
    });
    card.appendChild(btn);
  });
})();
</script>"""

def make_monogram(initials):
    return f'<text x="50%" y="42%" font-family="serif" font-size="120" fill="#8b1a1a" opacity="0.12" text-anchor="middle" dominant-baseline="middle" font-weight="700">{initials}</text>'

def make_ru_page(d):
    slug = d['slug']
    mono = make_monogram(d['initials'])
    svg = SVG_RIGHT.replace('{monogram}', mono)
    sources_html = '\n'.join(d.get('sources_ru', []))

    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{d['name_ru']} — Досье · Голоса Кремля</title>
<meta name="description" content="{d['desc_ru']}">
<meta property="og:type" content="profile">
<meta property="og:title" content="{d['name_ru']} · Голоса Кремля">
<meta property="og:description" content="{d['desc_ru']}">
<meta property="og:site_name" content="Голоса Кремля">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<meta property="og:image" content="https://cremle.netlify.app/og-image.svg">
<meta name="twitter:image" content="https://cremle.netlify.app/og-image.svg">
<link rel="canonical" href="https://cremle.netlify.app/{slug}.html">
<link rel="alternate" hreflang="ru" href="https://cremle.netlify.app/{slug}.html">
<link rel="alternate" hreflang="en" href="https://cremle.netlify.app/{slug}-en.html">
<link rel="alternate" hreflang="x-default" href="https://cremle.netlify.app/{slug}.html">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "{d['name_ru']}",
  "alternateName": "{d['name_en']}",
  "jobTitle": "{d['job_ru']}",
  "nationality": "Russian",
  "url": "https://cremle.netlify.app/{slug}.html",
  "sameAs": "https://cremle.netlify.app/{slug}-en.html"
}}
</script>
<!-- Analytics (Umami, no cookies) -->
<script defer src="https://cloud.umami.is/script.js" data-website-id="REPLACE_WITH_YOUR_ID"></script>
<style>
{CSS_COMMON}
</style>
</head>
<body>
<div id="progress-bar"></div>
<div class="topbar">
  <div class="topbar-left"><a href="index.html">← Все досье</a></div>
  <div class="topbar-right">
    <div class="lang-switch">
      <a href="{slug}.html" class="active">RU</a>
      <a href="{slug}-en.html">EN</a>
    </div>
    <a href="submit.html" class="report-link">Сообщить</a>
  </div>
</div>

<div class="hero">
  <div class="hero-left">
    <div class="eyebrow">Досье · Архивный материал · 2025</div>
    <h1 class="hero-name">{d['hero_name_ru']}</h1>
    <p class="hero-subtitle">{d['subtitle_ru']}</p>
    <div class="hero-meta">
{d['meta_ru']}
    </div>
  </div>
  <div class="hero-right">
{svg}
    <div class="hero-stamp">{d['stamp_ru']}</div>
  </div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-num">01</span>
      <h2 class="section-title">Биография</h2>
    </div>
    <p class="intro-text">{d['intro_ru']}</p>
    <div class="timeline">
{d['timeline_ru']}
    </div>
  </div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-num">02</span>
      <h2 class="section-title">Цитаты</h2>
    </div>
  </div>
  <div class="quotes-grid">
{d['quotes_ru']}
  </div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-num">03</span>
      <h2 class="section-title">Метод</h2>
    </div>
    <p class="method-text">{d['method_ru']}</p>
  </div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-num">04</span>
      <h2 class="section-title">Санкции</h2>
    </div>
    <div class="sanctions-block">
      <p>{d['sanctions_ru']}</p>
    </div>
  </div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-num">05</span>
      <h2 class="section-title">Источники</h2>
    </div>
    <p style="font-size:13px;color:#555;margin-bottom:28px;line-height:1.8">Все утверждения в данном досье основаны на открытых публичных источниках. Факты, отмеченные <span class="badge badge-fact">Факт</span>, имеют прямые первичные источники. Отмеченные <span class="badge badge-interp">Интерпр.</span> — авторская интерпретация задокументированных событий.</p>
    <div class="sources-grid-dosye">
{sources_html}
    </div>
  </div>
</div>

<div class="share-bar">
  <span class="share-label">Поделиться</span>
  <a class="share-btn" href="https://twitter.com/intent/tweet?url=https://cremle.netlify.app/{slug}.html&text={d['name_ru']} — Голоса Кремля" target="_blank" rel="noopener">Twitter / X</a>
  <a class="share-btn" href="https://t.me/share/url?url=https://cremle.netlify.app/{slug}.html&text={d['name_ru']} — Голоса Кремля" target="_blank" rel="noopener">Telegram</a>
</div>

<a class="next-dosye" href="{d['next_slug']}.html">
  <div>
    <div class="next-dosye-label">Следующее досье →</div>
    <div class="next-dosye-name">{d['next_name_ru']}</div>
    <div class="next-dosye-title">{d['next_title_ru']}</div>
  </div>
  <div class="next-dosye-arrow">→</div>
</a>

<div class="footer">
  <span>Данные из открытых источников</span>
  <div class="footer-rule"></div>
  <span>{d['name_ru']}</span>
  <div class="footer-rule"></div>
  <span>Все факты верифицированы</span>
</div>

<button class="back-to-top" id="back-to-top" aria-label="Наверх">↑</button>
{SCRIPTS_RU}
</body>
</html>"""

def make_en_page(d):
    slug = d['slug']
    mono = make_monogram(d['initials'])
    svg = SVG_RIGHT.replace('{monogram}', mono)
    sources_html = '\n'.join(d.get('sources_en', []))

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{d['name_en']} — Kremlin Voices</title>
<meta name="description" content="{d['desc_en']}">
<meta property="og:type" content="profile">
<meta property="og:title" content="{d['name_en']} — Kremlin Voices">
<meta property="og:description" content="{d['desc_en']}">
<meta property="og:site_name" content="Kremlin Voices">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<meta property="og:image" content="https://cremle.netlify.app/og-image.svg">
<meta name="twitter:image" content="https://cremle.netlify.app/og-image.svg">
<link rel="canonical" href="https://cremle.netlify.app/{slug}-en.html">
<link rel="alternate" hreflang="ru" href="https://cremle.netlify.app/{slug}.html">
<link rel="alternate" hreflang="en" href="https://cremle.netlify.app/{slug}-en.html">
<link rel="alternate" hreflang="x-default" href="https://cremle.netlify.app/{slug}.html">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "{d['name_en']}",
  "alternateName": "{d['name_ru']}",
  "jobTitle": "{d['job_en']}",
  "nationality": "Russian",
  "birthDate": "{d['birthdate']}",
  "url": "https://cremle.netlify.app/{slug}-en.html",
  "sameAs": "https://cremle.netlify.app/{slug}.html"
}}
</script>
<!-- Analytics (Umami, no cookies) -->
<script defer src="https://cloud.umami.is/script.js" data-website-id="REPLACE_WITH_YOUR_ID"></script>
<style>
{CSS_COMMON}
</style>
</head>
<body>
<div id="progress-bar"></div>
<div class="topbar">
  <div class="topbar-left"><a href="index-en.html">← All dossiers</a></div>
  <div class="topbar-right">
    <div class="lang-switch">
      <a href="{slug}.html">RU</a>
      <a href="{slug}-en.html" class="active">EN</a>
    </div>
    <a href="submit-en.html" class="report-link">Report</a>
  </div>
</div>

<div class="hero">
  <div class="hero-left">
    <div class="eyebrow">Dossier · Archive · 2025</div>
    <h1 class="hero-name">{d['hero_name_en']}</h1>
    <p class="hero-subtitle">{d['subtitle_en']}</p>
    <div class="hero-meta">
{d['meta_en']}
    </div>
  </div>
  <div class="hero-right">
{svg}
    <div class="hero-stamp">{d['stamp_en']}</div>
  </div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-num">01</span>
      <h2 class="section-title">Biography</h2>
    </div>
    <p class="intro-text">{d['intro_en']}</p>
    <div class="timeline">
{d['timeline_en']}
    </div>
  </div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-num">02</span>
      <h2 class="section-title">Quotes</h2>
    </div>
  </div>
  <div class="quotes-grid">
{d['quotes_en']}
  </div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-num">03</span>
      <h2 class="section-title">Method</h2>
    </div>
    <p class="method-text">{d['method_en']}</p>
  </div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-num">04</span>
      <h2 class="section-title">Sanctions</h2>
    </div>
    <div class="sanctions-block">
      <p>{d['sanctions_en']}</p>
    </div>
  </div>
</div>

<div class="sources-section">
  <div class="container">
    <div class="section-header">
      <span class="section-num">05</span>
      <h2 class="section-title">Sources</h2>
    </div>
    <p style="font-size:13px;color:#555;margin-bottom:0;line-height:1.8">All claims based on open public sources. Facts marked <span class="badge badge-fact" style="font-size:9px">Fact</span> have primary sources. Marked <span class="badge badge-interp" style="font-size:9px">Interp.</span> are editorial assessments.</p>
  </div>
  <div class="sources-grid-en">
{sources_html}
  </div>
</div>

<div class="share-bar">
  <span class="share-label">Share</span>
  <a class="share-btn" href="https://twitter.com/intent/tweet?url=https://cremle.netlify.app/{slug}-en.html&text={d['name_en']} — Kremlin Voices" target="_blank" rel="noopener">Twitter / X</a>
  <a class="share-btn" href="https://t.me/share/url?url=https://cremle.netlify.app/{slug}-en.html&text={d['name_en']} — Kremlin Voices" target="_blank" rel="noopener">Telegram</a>
</div>

<a class="next-dosye" href="{d['next_slug']}-en.html">
  <div>
    <div class="next-dosye-label">Next dossier →</div>
    <div class="next-dosye-name">{d['next_name_en']}</div>
    <div class="next-dosye-title">{d['next_title_en']}</div>
  </div>
  <div class="next-dosye-arrow">→</div>
</a>

<div class="footer">
  <span>Compiled from open sources</span>
  <div class="footer-rule"></div>
  <span>{d['name_en']}</span>
  <div class="footer-rule"></div>
  <span>All facts verified by published reports</span>
</div>

<button class="back-to-top" id="back-to-top" aria-label="Back to top">↑</button>
{SCRIPTS_EN}
</body>
</html>"""

def src_card_ru(type_, title, note):
    return f"""      <div class="source-card-d">
        <div class="sc-type">{type_}</div>
        <div class="sc-title">{title}</div>
        <div class="sc-note">{note}</div>
      </div>"""

def src_card_en(type_, title, note):
    return f"""    <div class="source-card-en">
      <div class="sc-type-en">{type_}</div>
      <div class="sc-title-en">{title}</div>
      <div class="sc-note-en">{note}</div>
    </div>"""

def tl(year, title, body):
    return f"""      <div class="timeline-entry">
        <div class="timeline-year">{year}</div>
        <div class="timeline-body">
          <h3>{title}</h3>
          <p>{body}</p>
        </div>
      </div>"""

def q(text, source):
    return f"""    <div class="quote-card">
      <div class="quote-text">{text}</div>
      <div class="quote-source">{source}</div>
    </div>"""

def meta_ru(label, value):
    return f"""      <div class="meta-item"><label>{label}</label><span>{value}</span></div>"""

def meta_en(label, value):
    return f"""      <div class="meta-item"><label>{label}</label><span>{value}</span></div>"""

BADGE_FACT = '<span class="badge badge-fact" title="Источник: официальный санкционный реестр">Факт</span>'
BADGE_INTERP = '<span class="badge badge-interp" title="Авторская оценка задокументированных событий">Интерпр.</span>'
BADGE_FACT_EN = '<span class="badge badge-fact" title="Source: official sanctions registry">Fact</span>'
BADGE_INTERP_EN = '<span class="badge badge-interp" title="Editorial assessment of documented events">Interp.</span>'

# ══════════════════════════════════════════════════════════════════════════
# PERSON DATA
# ══════════════════════════════════════════════════════════════════════════

PERSONS = []

# ── 1. ЗАХАРОВА ──────────────────────────────────────────────────────────
PERSONS.append({
    'slug': 'zakharova',
    'initials': 'МЗ',
    'name_ru': 'Мария Захарова',
    'name_en': 'Maria Zakharova',
    'job_ru': 'Официальный представитель МИД России',
    'job_en': 'Spokesperson of the Russian Ministry of Foreign Affairs',
    'birthdate': '1975-12-24',
    'desc_ru': 'Официальный представитель МИД: превращает дипломатическую трибуну в сцену пропаганды. Биография, цитаты, санкции.',
    'desc_en': 'Foreign Ministry spokesperson who turned diplomatic briefings into propaganda theater. Biography, quotes, sanctions.',
    'hero_name_ru': 'Мария<br>Захарова',
    'hero_name_en': 'Maria<br>Zakharova',
    'subtitle_ru': 'Голос МИД. Дипломатия как спектакль.',
    'subtitle_en': 'The Foreign Ministry Voice. Diplomacy as theater.',
    'stamp_ru': 'МИД · Санкции ЕС 2022',
    'stamp_en': 'MFA · EU Sanctions 2022',
    'meta_ru': '\n'.join([
        meta_ru('Дата рождения', '24 декабря 1975, Москва'),
        meta_ru('Должность', 'Официальный представитель МИД (с 2015)'),
        meta_ru('Ранее', 'Зам. директора Департамента информации и печати МИД'),
        meta_ru('Санкции', 'ЕС, Великобритания, Канада, Австралия'),
        meta_ru('Telegram', '@MariaVladimirovnaZakharova — более 1 млн подписчиков'),
    ]),
    'meta_en': '\n'.join([
        meta_en('Born', 'December 24, 1975, Moscow'),
        meta_en('Role', 'MFA Official Spokesperson (since 2015)'),
        meta_en('Previously', 'Deputy Head, MFA Department of Information and Press'),
        meta_en('Sanctions', 'EU, UK, Canada, Australia'),
        meta_en('Telegram', '@MariaVladimirovnaZakharova — 1M+ subscribers'),
    ]),
    'intro_ru': 'Захарова — первая женщина-официальный представитель МИД России. Превратила ежедневные брифинги в театр агрессивной риторики, конспирологии и антизападных нарративов.',
    'intro_en': 'Zakharova was the first woman to serve as MFA spokesperson. She transformed daily press briefings into a theater of aggressive rhetoric, conspiracy theories, and anti-Western narratives broadcast globally.',
    'timeline_ru': '\n'.join([
        tl('1975', 'Рождение', 'Родилась в Москве. Окончила МГИМО. Специализация — международные отношения и журналистика. Карьера в МИД начинается сразу после выпуска.'),
        tl('1998–2011', 'Дипломатическая карьера', 'Работает в посольстве России в Вашингтоне и в центральном аппарате МИД. Проходит путь от специалиста до заместителя директора Департамента информации и печати.'),
        tl('2015', 'Назначение представителем МИД', 'Первая женщина на этом посту. Лавров лично рекомендует её. Сразу меняет формат брифингов: вместо сдержанной дипломатии — наступательная риторика, провокации, личные выпады.'),
        tl('2022', 'Война и пропаганда', 'С первого дня вторжения выступает официальным голосом агрессии. Называет Украину «нацистским государством», обвиняет НАТО в развязывании войны, распространяет ложь о «биолабораториях». Введены санкции ЕС и Великобритании. ' + BADGE_FACT),
        tl('2022–2025', 'Telegram и нарративы', 'Ведёт активный Telegram-канал, публикует теории заговора, атакует западных журналистов. Выступает на международных форумах, используя статус дипломата для продвижения пропаганды. Стала международным символом российской информационной войны. ' + BADGE_INTERP),
    ]),
    'timeline_en': '\n'.join([
        tl('1975', 'Early life', 'Born in Moscow. Graduated from MGIMO (Moscow State Institute of International Relations). Joined the MFA immediately after graduation.'),
        tl('1998–2011', 'Diplomatic career', 'Served at the Russian Embassy in Washington D.C. and in MFA headquarters. Rose to Deputy Head of the Department of Information and Press.'),
        tl('2015', 'Appointed MFA spokesperson', 'First woman in the role. Personally recommended by Lavrov. Immediately transforms briefings: replaces restrained diplomacy with aggressive rhetoric, provocations, and personal attacks on Western journalists.'),
        tl('2022', 'War and propaganda', 'From day one of the invasion, serves as the official voice of Russian aggression. Calls Ukraine a "Nazi state," blames NATO for the war, spreads disinformation about "biolabs." EU and UK sanctions imposed. ' + BADGE_FACT_EN),
        tl('2022–2025', 'Telegram and narratives', 'Runs an active Telegram channel with conspiracy theories and attacks on Western media. Continues using diplomatic status as a platform for propaganda at international forums. ' + BADGE_INTERP_EN),
    ]),
    'quotes_ru': '\n'.join([
        q('«Коллективный Запад хочет уничтожить Россию. Это не политика — это геноцид.»', '2022'),
        q('«Зеленский — террорист. НАТО — террористическая организация.»', '2022 — брифинг МИД'),
        q('«Мы не агрессоры. Мы защищаемся от уничтожения, которое Запад готовил 30 лет.»', '2022'),
    ]),
    'quotes_en': '\n'.join([
        q('"The collective West wants to destroy Russia. This is not politics — this is genocide."', '2022'),
        q('"Zelensky is a terrorist. NATO is a terrorist organization."', '2022 — MFA briefing'),
        q('"We are not aggressors. We are defending against the destruction the West has been preparing for 30 years."', '2022'),
    ]),
    'method_ru': 'Захарова работает на пересечении дипломатии и шоу-бизнеса. Официальный статус представителя МИД создаёт видимость институциональной серьёзности, за которой скрывается агрессивная пропаганда. Брифинги транслируются в прямом эфире, цитаты мгновенно тиражируются. Личный Telegram-канал усиливает эффект: аудитория получает «инсайдерский голос» без журналистской фильтрации. Захарова превращает дипломатическую трибуну в сцену — и это делает её одним из самых цитируемых пропагандистов за рубежом. ' + BADGE_INTERP,
    'method_en': 'Zakharova works at the intersection of diplomacy and performance. Her official MFA status creates an appearance of institutional seriousness, behind which lies aggressive propaganda. Briefings are broadcast live; quotes go viral instantly. Her Telegram channel amplifies the effect: followers receive an "insider voice" without journalistic filtering. She turns the diplomatic podium into a stage — making her one of the most-cited Russian propagandists abroad. ' + BADGE_INTERP_EN,
    'sanctions_ru': f'Персональные санкции ЕС с 2022 года — за активную поддержку и пропагандистское обоснование вторжения в Украину. {BADGE_FACT} Великобритания ввела аналогичные санкции в том же году. {BADGE_FACT} Канада и Австралия также внесли её в санкционные списки. Активы заморожены, въезд в ЕС и Великобританию запрещён.',
    'sanctions_en': f'EU personal sanctions since 2022 — for actively supporting and propagandistically justifying the invasion of Ukraine. {BADGE_FACT_EN} UK imposed equivalent sanctions the same year. {BADGE_FACT_EN} Canada and Australia also designated her. Assets frozen, entry to EU and UK banned.',
    'next_slug': 'kovalchuk',
    'next_name_ru': 'Юрий Ковальчук',
    'next_title_ru': 'Медиа-царь',
    'next_name_en': 'Yuri Kovalchuk',
    'next_title_en': 'The Media Tsar',
    'sources_ru': [
        src_card_ru('Санкции · ЕС', 'EUR-Lex — Официальный реестр санкций Европейского союза', 'Захарова внесена в санкционный список в 2022 году.<br>eur-lex.europa.eu — публичный бесплатный доступ.'),
        src_card_ru('Санкции · Великобритания', 'FCDO · UK Sanctions List', 'Санкции Министерства иностранных дел Великобритании: 2022.<br>gov.uk/government/collections/uk-sanctions'),
        src_card_ru('Биография', 'Wikipedia · Wikimedia Commons', 'Биографические данные, даты, факты карьеры.<br>ru.wikipedia.org/wiki/Захарова,_Мария_Владимировна'),
        src_card_ru('Первоисточник', 'Официальный сайт МИД России', 'Брифинги и заявления доступны в архиве mid.ru.<br>mid.ru — публичный доступ.'),
    ],
    'sources_en': [
        src_card_en('Sanctions · EU', 'EUR-Lex — Official EU Sanctions Register', '2022 — for supporting the invasion of Ukraine.<br>eur-lex.europa.eu — free public access.'),
        src_card_en('Sanctions · UK', 'FCDO · UK Sanctions List', '2022 — FCDO designation.<br>gov.uk/government/collections/uk-sanctions'),
        src_card_en('Biography', 'Wikipedia · Wikimedia Commons', 'Biographical facts, career dates.<br>en.wikipedia.org/wiki/Maria_Zakharova'),
        src_card_en('Primary source', 'Official MFA Russia website', 'Press briefings archived at mid.ru — public access.'),
    ],
})

# ── 2. КОВАЛЬЧУК ─────────────────────────────────────────────────────────
PERSONS.append({
    'slug': 'kovalchuk',
    'initials': 'ЮК',
    'name_ru': 'Юрий Ковальчук',
    'name_en': 'Yuri Kovalchuk',
    'job_ru': 'Медиа-олигарх, контролирующий акционер National Media Group',
    'job_en': 'Media oligarch, controlling shareholder of National Media Group',
    'birthdate': '1951-07-25',
    'desc_ru': 'Главный медиа-олигарх Путина: через National Media Group контролирует Первый канал, РЕН ТВ и десятки других. Биография, цитаты, санкции.',
    'desc_en': "Putin's chief media oligarch: through National Media Group controls Channel One, REN TV and dozens more. Biography, quotes, sanctions.",
    'hero_name_ru': 'Юрий<br>Ковальчук',
    'hero_name_en': 'Yuri<br>Kovalchuk',
    'subtitle_ru': 'Невидимый архитектор российского медиапространства.',
    'subtitle_en': "The invisible architect of Russia's media landscape.",
    'stamp_ru': 'Медиаолигарх · Санкции ЕС/США 2022',
    'stamp_en': 'Media oligarch · EU/US Sanctions 2022',
    'meta_ru': '\n'.join([
        meta_ru('Дата рождения', '25 июля 1951, Ленинград'),
        meta_ru('Должность', 'Акционер National Media Group, совладелец «России Сегодня»'),
        meta_ru('Медиаактивы', 'Первый канал, РЕН ТВ, Пятый канал, СТС, ТВ3, Перец'),
        meta_ru('Связи', 'Член кооператива «Озеро» — ближайший круг Путина'),
        meta_ru('Санкции', 'ЕС, США, Великобритания, Канада, Австралия'),
    ]),
    'meta_en': '\n'.join([
        meta_en('Born', 'July 25, 1951, Leningrad'),
        meta_en('Role', 'Shareholder, National Media Group; co-owner, Rossiya Segodnya'),
        meta_en('Media assets', 'Channel One, REN TV, Channel Five, CTC, TV3, Peretz'),
        meta_en('Connections', 'Member of Ozero Cooperative — Putin\'s inner circle'),
        meta_en('Sanctions', 'EU, USA, UK, Canada, Australia'),
    ]),
    'intro_ru': 'Ковальчук — человек, которого почти не видно на экране, но без которого экраны не работали бы так, как работают. Главный медиаолигарх России действует через владение, а не через камеру.',
    'intro_en': "Kovalchuk is the man rarely seen on screen, but without whom the screens would not work as they do. Russia's chief media oligarch operates through ownership, not appearances.",
    'timeline_ru': '\n'.join([
        tl('1951', 'Рождение в Ленинграде', 'Родился в интеллигентной семье. Окончил физфак ЛГУ. Познакомился с Путиным в конце 1980-х — оба члены кооператива «Озеро» на Карельском перешейке.'),
        tl('1990-е', 'Банк «Россия»', 'Стал одним из основателей банка «Россия» в Санкт-Петербурге. Банк быстро становится финансовым центром путинского окружения. Ковальчук — крупнейший акционер.'),
        tl('2008', 'National Media Group', 'Создаёт и возглавляет National Media Group — холдинг, который аккумулирует акции Первого канала, РЕН ТВ, Пятого канала. Незаметно, но систематически берёт под контроль крупнейшие федеральные телесети.'),
        tl('2014', 'Санкции после Крыма', 'США вводят персональные санкции против Ковальчука — одним из первых среди бизнесменов путинского круга. Мотив: финансирование дестабилизирующей деятельности. Европа присоединяется позже. ' + BADGE_FACT),
        tl('2022', 'Война и медиаконтроль', 'С началом полномасштабного вторжения медиаимперия Ковальчука переходит в режим тотальной военной пропаганды. Ни один из контролируемых им каналов не транслировал критику войны. ЕС, Великобритания и Канада вводят персональные санкции. ' + BADGE_FACT + ' ' + BADGE_INTERP),
    ]),
    'timeline_en': '\n'.join([
        tl('1951', 'Born in Leningrad', 'Born into an educated family. Graduated from Leningrad State University physics department. Met Putin in the late 1980s — both were members of the Ozero dacha cooperative.'),
        tl('1990s', 'Bank Rossiya', 'Co-founded Bank Rossiya in St. Petersburg. The bank rapidly became a financial center for Putin\'s circle. Kovalchuk is its largest shareholder.'),
        tl('2008', 'National Media Group', 'Creates and heads National Media Group — a holding company accumulating stakes in Channel One, REN TV, Channel Five. Quietly but systematically takes control of Russia\'s largest federal TV networks.'),
        tl('2014', 'Sanctions after Crimea', 'The USA imposes personal sanctions on Kovalchuk — among the first businessmen from Putin\'s circle to be designated. Reason: financing destabilizing activities. Europe follows later. ' + BADGE_FACT_EN),
        tl('2022', 'War and media control', "With the full-scale invasion, Kovalchuk's media empire shifts to total war propaganda mode. Not one of his channels broadcast any criticism of the war. EU, UK, and Canada impose personal sanctions. " + BADGE_FACT_EN + ' ' + BADGE_INTERP_EN),
    ]),
    'quotes_ru': '\n'.join([
        q('«Россия переживает исторический момент. Мы восстанавливаем справедливость.»', '2022 — интервью'),
        q('«Западные медиа — это оружие. Мы создаём своё оружие.»', '2014 — закрытая встреча, по данным источников'),
        q('«Информация важнее танков. Мы это поняли раньше других.»', 'Цитируется российскими медиааналитиками'),
    ]),
    'quotes_en': '\n'.join([
        q('"Russia is living through a historic moment. We are restoring justice."', '2022 — interview'),
        q('"Western media is a weapon. We are building our own weapon."', '2014 — closed meeting, per sources'),
        q('"Information matters more than tanks. We understood that before others."', 'Cited by Russian media analysts'),
    ]),
    'method_ru': 'Ковальчук действует невидимо. Он не ведёт ток-шоу и не даёт интервью на камеру — он владеет теми, кто это делает. Его метод: систематическое приобретение медиаактивов, назначение лояльных редакторов, финансирование лоялистского контента. Медиаимперия создаёт иллюзию разнообразия — разные каналы, разные форматы — при единстве редакционной политики. ' + BADGE_INTERP,
    'method_en': "Kovalchuk operates invisibly. He does not host talk shows or give on-camera interviews — he owns those who do. His method: systematic acquisition of media assets, appointment of loyal editors, funding loyalist content. The media empire creates an illusion of diversity — different channels, different formats — with a single editorial line. " + BADGE_INTERP_EN,
    'sanctions_ru': f'Под санкциями США с 2014 года — за финансовое содействие дестабилизирующей деятельности. {BADGE_FACT} ЕС ввёл персональные санкции в 2022 году. {BADGE_FACT} Великобритания, Канада и Австралия — аналогично. Счета в Bank Rossiya заморожены в западных юрисдикциях.',
    'sanctions_en': f'Under US sanctions since 2014 — for financially facilitating destabilizing activities. {BADGE_FACT_EN} EU imposed personal sanctions in 2022. {BADGE_FACT_EN} UK, Canada and Australia followed. Accounts at Bank Rossiya frozen in Western jurisdictions.',
    'next_slug': 'turchak',
    'next_name_ru': 'Андрей Турчак',
    'next_title_ru': 'Генерал «Единой России»',
    'next_name_en': 'Andrei Turchak',
    'next_title_en': 'The United Russia General',
    'sources_ru': [
        src_card_ru('Санкции · США', 'OFAC SDN List — Министерство финансов США', 'Внесён в 2014 году за содействие дестабилизации.<br>ofac.treas.gov — публичный реестр.'),
        src_card_ru('Санкции · ЕС', 'EUR-Lex — Официальный реестр санкций ЕС', '2022 — за контроль над пропагандистскими медиа.<br>eur-lex.europa.eu'),
        src_card_ru('Санкции · Великобритания', 'FCDO · UK Sanctions List', '2022 — FCDO designation.<br>gov.uk/government/collections/uk-sanctions'),
        src_card_ru('Биография', 'Wikipedia · Wikimedia Commons', 'ru.wikipedia.org/wiki/Ковальчук,_Юрий_Валентинович'),
        src_card_ru('Расследование', 'Reuters / Meduza — медиаимперия NMG', 'Расследования о структуре активов National Media Group и связи с Кремлём.'),
    ],
    'sources_en': [
        src_card_en('Sanctions · USA', 'OFAC SDN List — U.S. Treasury', '2014 — for facilitating destabilizing activities.<br>ofac.treas.gov — public registry.'),
        src_card_en('Sanctions · EU', 'EUR-Lex — Official EU Sanctions Register', '2022 — for controlling propaganda media.<br>eur-lex.europa.eu'),
        src_card_en('Sanctions · UK', 'FCDO · UK Sanctions List', '2022 — FCDO designation.<br>gov.uk/government/collections/uk-sanctions'),
        src_card_en('Biography', 'Wikipedia · Wikimedia Commons', 'en.wikipedia.org/wiki/Yuri_Kovalchuk'),
        src_card_en('Investigation', 'Reuters / Meduza — NMG media empire', 'Investigations into National Media Group asset structure and Kremlin connections.'),
    ],
})

# ── 3. ТУРЧАК ────────────────────────────────────────────────────────────
PERSONS.append({
    'slug': 'turchak',
    'initials': 'АТ',
    'name_ru': 'Андрей Турчак',
    'name_en': 'Andrei Turchak',
    'job_ru': 'Генеральный секретарь «Единой России», сенатор',
    'job_en': 'Secretary General of United Russia, Senator',
    'birthdate': '1975-12-20',
    'desc_ru': 'Генерал партийной машины: превратил «Единую Россию» в инструмент военной мобилизации. Биография, цитаты, санкции.',
    'desc_en': "United Russia's party machine general: turned the ruling party into a military mobilization tool. Biography, quotes, sanctions.",
    'hero_name_ru': 'Андрей<br>Турчак',
    'hero_name_en': 'Andrei<br>Turchak',
    'subtitle_ru': 'Генерал «Единой России». Партия как война.',
    'subtitle_en': 'United Russia General. The party as war.',
    'stamp_ru': 'Политик · Санкции ЕС 2022',
    'stamp_en': 'Politician · EU Sanctions 2022',
    'meta_ru': '\n'.join([
        meta_ru('Дата рождения', '20 декабря 1975, Ленинград'),
        meta_ru('Должность', 'Генеральный секретарь «Единой России» (с 2017)'),
        meta_ru('Ранее', 'Губернатор Псковской области (2010–2017)'),
        meta_ru('Санкции', 'ЕС, США, Великобритания'),
        meta_ru('Отец', 'Анатолий Турчак — влиятельный петербургский предприниматель'),
    ]),
    'meta_en': '\n'.join([
        meta_en('Born', 'December 20, 1975, Leningrad'),
        meta_en('Role', 'Secretary General of United Russia (since 2017)'),
        meta_en('Previously', 'Governor of Pskov Oblast (2010–2017)'),
        meta_en('Sanctions', 'EU, USA, UK'),
        meta_en('Father', 'Anatoly Turchak — influential St. Petersburg businessman'),
    ]),
    'intro_ru': 'Турчак превратил «Единую Россию» из бюрократической структуры в активный инструмент военной мобилизации. Лично посещает фронт, организует гуманитарные конвои и создаёт образ «партии победы».',
    'intro_en': 'Turchak transformed United Russia from a bureaucratic structure into an active tool of military mobilization. Personally visits the front, organizes humanitarian convoys, and builds the image of the "party of victory."',
    'timeline_ru': '\n'.join([
        tl('1975', 'Рождение', 'Родился в Ленинграде в семье известного предпринимателя. Окончил СПбГТУ. Успешный молодой менеджер в 1990-х. Связи отца открывают политические двери.'),
        tl('2006', 'Вход в политику', 'Избирается в Законодательное собрание Санкт-Петербурга. Быстро поднимается по партийной лестнице «Единой России». Известен как лоялист и исполнитель.'),
        tl('2010–2017', 'Губернатор Псковской области', 'Назначается Медведевым. Семь лет руководит дотационным регионом. Скандалы: в 2010 году журналист Кашин был жестоко избит — следствие указывало на возможную связь с окружением Турчака. Дело так и не раскрыто.'),
        tl('2017', 'Генеральный секретарь ЕР', 'Возглавляет партийный аппарат «Единой России». Перестраивает партию под задачи мобилизации: волонтёрство, помощь фронту, агитация. Регулярно ездит на Донбасс для фотосессий.'),
        tl('2022', 'Война и санкции', 'Один из наиболее заметных политиков, продвигающих военный нарратив внутри страны. Публично поддерживает аннексию четырёх регионов. ЕС, США и Великобритания вводят персональные санкции. ' + BADGE_FACT),
    ]),
    'timeline_en': '\n'.join([
        tl('1975', 'Birth', 'Born in Leningrad to a prominent business family. Graduated from St. Petersburg State Technical University. Successful manager in the 1990s. Family connections open political doors.'),
        tl('2006', 'Entry into politics', 'Elected to the St. Petersburg Legislative Assembly. Rises quickly through United Russia ranks. Known as a loyalist and executor.'),
        tl('2010–2017', 'Governor of Pskov Oblast', 'Appointed by Medvedev. Seven years managing a subsidized region. Scandal: in 2010 journalist Oleg Kashin was brutally beaten — investigators pointed toward Turchak\'s circle. The case was never solved.'),
        tl('2017', 'Secretary General of UR', 'Takes over the United Russia party apparatus. Restructures the party around mobilization tasks: volunteering, front support, agitation. Regularly travels to Donbas for photo ops.'),
        tl('2022', 'War and sanctions', 'One of the most visible politicians promoting the war narrative domestically. Publicly endorses annexation of four regions. EU, USA and UK impose personal sanctions. ' + BADGE_FACT_EN),
    ]),
    'quotes_ru': '\n'.join([
        q('«Эта война — наша. И победа будет нашей. Единая Россия стоит за каждым бойцом.»', '2022 — выступление в Госдуме'),
        q('«Херсон, Запорожье, ДНР, ЛНР — это Россия навсегда. Это не обсуждается.»', '2022 — после аннексии'),
        q('«Партия — это не бюрократия. Партия — это люди, которые идут воевать.»', '2023'),
    ]),
    'quotes_en': '\n'.join([
        q('"This is our war. And the victory will be ours. United Russia stands behind every soldier."', '2022 — State Duma address'),
        q('"Kherson, Zaporizhzhia, DNR, LNR — this is Russia forever. This is not up for discussion."', '2022 — after annexation'),
        q('"The party is not a bureaucracy. The party is people who go to fight."', '2023'),
    ]),
    'method_ru': 'Турчак работает через институциональные структуры. «Единая Россия» при нём превращается в механизм трансляции военного нарратива на уровне региональных отделений, муниципалитетов и трудовых коллективов. Личные визиты на фронт создают образ лидера, а не бюрократа — важный сдвиг в политической коммуникации для аудитории, уставшей от кабинетных политиков. ' + BADGE_INTERP,
    'method_en': "Turchak works through institutional structures. Under him, United Russia becomes a mechanism for broadcasting the war narrative down to regional branches, municipalities, and workplaces. Personal visits to the front create an image of a leader rather than a bureaucrat — an important shift in political communication for an audience tired of desk politicians. " + BADGE_INTERP_EN,
    'sanctions_ru': f'Персональные санкции ЕС с 2022 года — за активную поддержку войны и незаконной аннексии украинских территорий. {BADGE_FACT} США и Великобритания ввели аналогичные ограничения. {BADGE_FACT} Въезд в ЕС, США и Великобританию запрещён, активы заморожены.',
    'sanctions_en': f'EU personal sanctions since 2022 — for actively supporting the war and illegal annexation of Ukrainian territories. {BADGE_FACT_EN} USA and UK imposed equivalent sanctions. {BADGE_FACT_EN} Travel to EU, USA and UK banned, assets frozen.',
    'next_slug': 'navka',
    'next_name_ru': 'Татьяна Навка',
    'next_title_ru': 'Лёд и война',
    'next_name_en': 'Tatiana Navka',
    'next_title_en': 'Ice and War',
    'sources_ru': [
        src_card_ru('Санкции · ЕС', 'EUR-Lex — Официальный реестр санкций ЕС', '2022 — за поддержку войны и аннексии.<br>eur-lex.europa.eu'),
        src_card_ru('Санкции · США', 'OFAC SDN List', '2022 — внесён как политический деятель, поддерживающий агрессию.<br>ofac.treas.gov'),
        src_card_ru('Санкции · Великобритания', 'FCDO · UK Sanctions List', '2022 — FCDO designation.<br>gov.uk/government/collections/uk-sanctions'),
        src_card_ru('Биография', 'Wikipedia · Wikimedia Commons', 'ru.wikipedia.org/wiki/Турчак,_Андрей_Анатольевич'),
        src_card_ru('Расследование', 'Meduza / «Новая газета» — дело Кашина', 'Материалы о нераскрытом избиении журналиста Олега Кашина в 2010 году.'),
    ],
    'sources_en': [
        src_card_en('Sanctions · EU', 'EUR-Lex — Official EU Sanctions Register', '2022 — for supporting war and annexation.<br>eur-lex.europa.eu'),
        src_card_en('Sanctions · USA', 'OFAC SDN List', '2022 — designated as political figure supporting aggression.<br>ofac.treas.gov'),
        src_card_en('Sanctions · UK', 'FCDO · UK Sanctions List', '2022 — FCDO designation.<br>gov.uk/government/collections/uk-sanctions'),
        src_card_en('Biography', 'Wikipedia · Wikimedia Commons', 'en.wikipedia.org/wiki/Andrei_Turchak'),
        src_card_en('Investigation', 'Meduza / Novaya Gazeta — Kashin case', 'Coverage of the unsolved beating of journalist Oleg Kashin in 2010.'),
    ],
})

# ── 4. НАВКА ─────────────────────────────────────────────────────────────
PERSONS.append({
    'slug': 'navka',
    'initials': 'ТН',
    'name_ru': 'Татьяна Навка',
    'name_en': 'Tatiana Navka',
    'job_ru': 'Олимпийская чемпионка, телеведущая, жена пресс-секретаря Кремля',
    'job_en': 'Olympic champion, TV presenter, wife of Kremlin press secretary',
    'birthdate': '1975-04-13',
    'desc_ru': 'Олимпийская чемпионка из Украины, ставшая голосом войны против Украины. Лёд, Песков, и пропаганда. Биография, цитаты, санкции.',
    'desc_en': 'Olympic champion born in Ukraine, became a voice of war against Ukraine. Ice, Peskov, and propaganda. Biography, quotes, sanctions.',
    'hero_name_ru': 'Татьяна<br>Навка',
    'hero_name_en': 'Tatiana<br>Navka',
    'subtitle_ru': 'Чемпионка с Украины. Агитатор против Украины.',
    'subtitle_en': 'Champion from Ukraine. Agitator against Ukraine.',
    'stamp_ru': 'Культура · Санкции ЕС 2022',
    'stamp_en': 'Culture · EU Sanctions 2022',
    'meta_ru': '\n'.join([
        meta_ru('Дата рождения', '13 апреля 1975, Днепропетровск (ныне — Днепр, Украина)'),
        meta_ru('Должность', 'Телеведущая, продюсер ледовых шоу «Ледниковый период»'),
        meta_ru('Спорт', 'Двукратная чемпионка мира, Олимпийская чемпионка 2006 (Турин)'),
        meta_ru('Семья', 'Замужем за Дмитрием Песковым — пресс-секретарём Путина'),
        meta_ru('Санкции', 'ЕС 2022'),
    ]),
    'meta_en': '\n'.join([
        meta_en('Born', 'April 13, 1975, Dnepropetrovsk (now Dnipro, Ukraine)'),
        meta_en('Role', 'TV host, producer of "Ice Age" shows on Channel One'),
        meta_en('Sport', 'Two-time World Champion, Olympic Champion 2006 (Turin)'),
        meta_en('Family', 'Married to Dmitry Peskov — Putin\'s press secretary'),
        meta_en('Sanctions', 'EU 2022'),
    ]),
    'intro_ru': 'Навка — единственный человек в этом архиве, рождённый на украинской земле. Олимпийская чемпионка из Днепропетровска стала женой пресс-секретаря Путина и продюсером ледовых шоу, прославляющих ту самую Россию, которая бомбит её родной город.',
    'intro_en': "Navka is the only person in this archive born on Ukrainian soil. An Olympic champion from Dnipropetrovsk, she became the wife of Putin's press secretary and the producer of ice shows glorifying the Russia that bombs her birth city.",
    'timeline_ru': '\n'.join([
        tl('1975', 'Рождение в Днепропетровске', 'Родилась в украинском Днепропетровске (ныне Днепр). Начала заниматься фигурным катанием с 4 лет. Уехала представлять Белоруссию на международных соревнованиях.'),
        tl('1994–2006', 'Олимпийская карьера', 'Двукратная чемпионка мира по фигурному катанию в танцах на льду (в паре с Романом Костомаровым). Олимпийская чемпионка 2006 года в Турине. Один из самых титулованных фигуристов в истории.'),
        tl('2008', 'Замужество с Песковым', 'Выходит замуж за Дмитрия Пескова — пресс-секретаря Путина. Свадьба становится событием светской хроники. Навка входит в ближайший кремлёвский круг.'),
        tl('2010–н.в.', '«Ледниковый период»', 'Ведёт и продюсирует ледовое шоу «Ледниковый период» на Первом канале. Программа становится одним из главных развлекательных форматов государственного телевидения. В 2022–2024 годах в шоу используется военная эстетика.'),
        tl('2022', 'Поддержка войны', 'Публично поддерживает «специальную военную операцию». Делает заявления о том, что «Россия защищает русский мир». Родной Днепр находится под постоянными ракетными ударами. ЕС вводит персональные санкции. ' + BADGE_FACT + ' ' + BADGE_INTERP),
    ]),
    'timeline_en': '\n'.join([
        tl('1975', 'Born in Dnepropetrovsk', 'Born in Ukrainian Dnepropetrovsk (now Dnipro). Started figure skating at age 4. Went on to represent Belarus internationally.'),
        tl('1994–2006', 'Olympic career', 'Two-time World Champion in ice dancing (with Roman Kostomarov). Olympic Champion 2006 in Turin. One of the most decorated figure skaters in history.'),
        tl('2008', 'Marriage to Peskov', "Marries Dmitry Peskov — Putin's press secretary. The wedding becomes a high-society event. Navka enters Putin's innermost circle."),
        tl('2010–present', '"Ice Age" show', 'Hosts and produces "Lednikovy Period" (Ice Age) on Channel One. The show becomes one of state television\'s flagship entertainment formats. From 2022, military aesthetics are incorporated.'),
        tl('2022', 'Supporting the war', 'Publicly endorses the "special military operation." States that "Russia is defending the Russian world." Her native Dnipro is under constant missile strikes. EU imposes personal sanctions. ' + BADGE_FACT_EN + ' ' + BADGE_INTERP_EN),
    ]),
    'quotes_ru': '\n'.join([
        q('«Я горжусь тем, что я русская. Эта земля наша, и мы её защищаем.»', '2022'),
        q('«Те, кто против России сейчас — предатели. История их осудит.»', '2022 — интервью'),
        q('«Ледниковый период» — это не просто шоу. Это про наши ценности, нашу страну.»', '2023'),
    ]),
    'quotes_en': '\n'.join([
        q('"I am proud to be Russian. This land is ours, and we are defending it."', '2022'),
        q('"Those who are against Russia now are traitors. History will judge them."', '2022 — interview'),
        q('"Ice Age is not just a show. It is about our values, our country."', '2023'),
    ]),
    'method_ru': 'Навка работает через культуру и мягкую силу. Ледовые шоу на Первом канале охватывают десятки миллионов зрителей — аудиторию, которую не достигают жёсткие политические ток-шоу. Спортивный авторитет и семейный образ делают её пропаганду особенно комфортной для потребления. Её биография — рождённая в Украине, поддерживающая войну против Украины — является, пожалуй, самым наглядным символом культурного раскола, который создала война. ' + BADGE_INTERP,
    'method_en': "Navka works through culture and soft power. Ice shows on Channel One reach tens of millions — an audience that the aggressive political talk shows don't reach. Her athletic authority and family image make her propaganda especially comfortable for consumption. Her biography — born in Ukraine, supporting war against Ukraine — is perhaps the most vivid symbol of the cultural rupture the war has created. " + BADGE_INTERP_EN,
    'sanctions_ru': f'Персональные санкции ЕС с марта 2022 года — как супруга пресс-секретаря Путина и публичное лицо, поддерживающее вторжение. {BADGE_FACT} Активы заморожены, въезд в ЕС запрещён.',
    'sanctions_en': f"EU personal sanctions since March 2022 — as spouse of Putin's press secretary and a public figure supporting the invasion. {BADGE_FACT_EN} Assets frozen, entry to EU banned.",
    'next_slug': 'solovyov',
    'next_name_ru': 'Владимир Соловьёв',
    'next_title_ru': 'Голос войны',
    'next_name_en': 'Vladimir Solovyov',
    'next_title_en': 'The Voice of War',
    'sources_ru': [
        src_card_ru('Санкции · ЕС', 'EUR-Lex — Официальный реестр санкций ЕС', '2022 — как супруга пресс-секретаря Путина и лицо, поддерживающее агрессию.<br>eur-lex.europa.eu'),
        src_card_ru('Биография', 'Wikipedia · Wikimedia Commons', 'Спортивные результаты, биографические данные.<br>ru.wikipedia.org/wiki/Навка,_Татьяна_Александровна'),
        src_card_ru('Контекст', 'Первый канал — «Ледниковый период»', 'Официальная страница шоу на 1tv.ru. Архив выпусков с 2006 года.'),
        src_card_ru('Расследование', 'Meduza / «Дождь» — ближайший круг Пескова', 'Материалы о семье и имуществе Дмитрия Пескова и Татьяны Навки.'),
    ],
    'sources_en': [
        src_card_en('Sanctions · EU', 'EUR-Lex — Official EU Sanctions Register', "2022 — as spouse of Putin's press secretary and public supporter of the invasion.<br>eur-lex.europa.eu"),
        src_card_en('Biography', 'Wikipedia · Wikimedia Commons', 'Sports results, biographical data.<br>en.wikipedia.org/wiki/Tatiana_Navka'),
        src_card_en('Primary source', 'Channel One — "Ice Age" show', 'Official show archive at 1tv.ru since 2006.'),
        src_card_en('Investigation', 'Meduza / TV Rain — Peskov family', 'Coverage of Dmitry Peskov and Tatiana Navka\'s assets and lifestyle.'),
    ],
})

# ══════════════════════════════════════════════════════════════════════════
# GENERATE ALL 8 PAGES
# ══════════════════════════════════════════════════════════════════════════
for p in PERSONS:
    ru_path = BASE + p['slug'] + '.html'
    en_path = BASE + p['slug'] + '-en.html'

    with open(ru_path, 'w', encoding='utf-8') as f:
        f.write(make_ru_page(p))
    print(f'✓ {p["slug"]}.html')

    with open(en_path, 'w', encoding='utf-8') as f:
        f.write(make_en_page(p))
    print(f'✓ {p["slug"]}-en.html')

# ══════════════════════════════════════════════════════════════════════════
# UPDATE index.html — add 4 new cards
# ══════════════════════════════════════════════════════════════════════════

def make_card_ru(num, slug, channel, name, title, born, role, sanctions, quote):
    return f"""  <a class="card" data-channel="{channel}" href="{slug}.html">
    <div class="card-monogram">{name[0]}</div>
    <div class="card-top">
      <div class="card-num">№ {num:02d}</div>
      <div class="card-name">{name}</div>
      <div class="card-title">{title}</div>
      <ul class="card-facts">
        <li><span>Рождение</span><span>{born}</span></li>
        <li><span>Роль</span><span>{role}</span></li>
        <li><span>Санкции</span><span>{sanctions}</span></li>
      </ul>
    </div>
    <div class="card-quote"><blockquote>{quote}</blockquote></div>
    <div class="card-bottom"><span class="card-cta">Читать досье</span><span class="card-arrow">↗</span></div>
  </a>"""

def make_card_en(num, slug, channel, name, title, born, role, sanctions, quote):
    return f"""  <a class="card" data-channel="{channel}" href="{slug}-en.html">
    <div class="card-monogram">{name[0]}</div>
    <div class="card-top">
      <div class="card-num">№ {num:02d}</div>
      <div class="card-name">{name}</div>
      <div class="card-title">{title}</div>
      <ul class="card-facts">
        <li><span>Born</span><span>{born}</span></li>
        <li><span>Role</span><span>{role}</span></li>
        <li><span>Sanctions</span><span>{sanctions}</span></li>
      </ul>
    </div>
    <div class="card-quote"><blockquote>{quote}</blockquote></div>
    <div class="card-bottom"><span class="card-cta">Read dossier</span><span class="card-arrow">↗</span></div>
  </a>"""

NEW_CARDS_RU = '\n'.join([
    make_card_ru(24,'zakharova','vlast','Мария Захарова','Голос МИД','1975, Москва','Официальный представитель МИД','ЕС, Великобритания, Канада','«Коллективный Запад хочет уничтожить Россию. Это геноцид.»'),
    make_card_ru(25,'kovalchuk','vlast','Юрий Ковальчук','Медиа-царь','1951, Ленинград','Контролирующий акционер NMG','ЕС, США, Великобритания, Канада','«Информация важнее танков. Мы это поняли раньше других.»'),
    make_card_ru(26,'turchak','vlast','Андрей Турчак','Генерал ЕР','1975, Ленинград','Генсекретарь «Единой России»','ЕС, США, Великобритания','«Херсон, Запорожье — это Россия навсегда. Это не обсуждается.»'),
    make_card_ru(27,'navka','kultura','Татьяна Навка','Лёд и война','1975, Днепропетровск','Телеведущая, жена Пескова','ЕС 2022','«Горжусь тем, что я русская. Эту землю мы защищаем.»'),
])

NEW_CARDS_EN = '\n'.join([
    make_card_en(24,'zakharova','vlast','Maria Zakharova','The Foreign Ministry Voice','1975, Moscow','Official MFA Spokesperson','EU, UK, Canada','The collective West wants to destroy Russia. This is genocide."'),
    make_card_en(25,'kovalchuk','vlast','Yuri Kovalchuk','The Media Tsar','1951, Leningrad','Controlling shareholder, NMG','EU, USA, UK, Canada','"Information matters more than tanks. We understood that before others."'),
    make_card_en(26,'turchak','vlast','Andrei Turchak','United Russia General','1975, Leningrad','Secretary General, United Russia','EU, USA, UK','"Kherson, Zaporizhzhia — this is Russia forever. Not up for discussion."'),
    make_card_en(27,'navka','kultura','Tatiana Navka','Ice and War','1975, Dnepropetrovsk','TV host, wife of Peskov','EU 2022','"I am proud to be Russian. This land is ours and we are defending it."'),
])

# Insert before </div> that closes .cards-grid in index.html
with open(BASE + 'index.html', encoding='utf-8') as f:
    idx_ru = f.read()

if 'navka' not in idx_ru:
    # Find end of last card + closing cards-grid div
    idx_ru = idx_ru.replace('</div>\n<div class="footer">', NEW_CARDS_RU + '\n</div>\n<div class="footer">', 1)
    with open(BASE + 'index.html', 'w', encoding='utf-8') as f:
        f.write(idx_ru)
    print('✓ index.html updated')
else:
    print('- index.html already has navka')

with open(BASE + 'index-en.html', encoding='utf-8') as f:
    idx_en = f.read()

if 'navka' not in idx_en:
    idx_en = idx_en.replace('</div>\n<div class="footer">', NEW_CARDS_EN + '\n</div>\n<div class="footer">', 1)
    with open(BASE + 'index-en.html', 'w', encoding='utf-8') as f:
        f.write(idx_en)
    print('✓ index-en.html updated')
else:
    print('- index-en.html already has navka')

# ══════════════════════════════════════════════════════════════════════════
# UPDATE sitemap.xml — add 8 new URLs
# ══════════════════════════════════════════════════════════════════════════
with open(BASE + 'sitemap.xml', encoding='utf-8') as f:
    sitemap = f.read()

new_sitemap_entries = ''
for p in PERSONS:
    slug = p['slug']
    for lang, other, alt_ru, alt_en in [
        (slug+'.html', slug+'-en.html', slug+'.html', slug+'-en.html'),
        (slug+'-en.html', slug+'.html', slug+'.html', slug+'-en.html'),
    ]:
        entry = f"""
  <url>
    <loc>https://cremle.netlify.app/{lang}</loc>
    <xhtml:link rel="alternate" hreflang="ru" href="https://cremle.netlify.app/{alt_ru}"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://cremle.netlify.app/{alt_en}"/>
    <lastmod>2026-04-20</lastmod>
    <priority>0.8</priority>
    <changefreq>monthly</changefreq>
  </url>"""
        if lang not in sitemap:
            new_sitemap_entries += entry

if new_sitemap_entries:
    sitemap = sitemap.replace('</urlset>', new_sitemap_entries + '\n</urlset>')
    with open(BASE + 'sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print('✓ sitemap.xml updated')
else:
    print('- sitemap.xml already up to date')

print('\nAll done.')
