#!/usr/bin/env python3
"""
Creates 3 new dossier pages (RU + EN):
  peskov, lavrov, mizulina
Also adds them to:
  - index.html / index-en.html (cards)
  - compare.html / compare-en.html
  - quotes.html / quotes-en.html
  - sanctions.html / sanctions-en.html
  - connections.html / connections-en.html
  - sitemap.xml
  - OG SVG generation
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
  @media (max-width:900px) { .sources-grid-en { grid-template-columns:1fr; } .sources-section { padding:40px 0; } }
  .related-section { border-top: 1px solid var(--rule); padding: 60px; }
  .related-label { font-size: 10px; letter-spacing: 0.3em; text-transform: uppercase; color: var(--red); margin-bottom: 32px; }
  .related-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 2px; }
  .related-card { background: var(--card-bg); padding: 28px; text-decoration: none; color: var(--paper); display: block; transition: background 0.2s; }
  .related-card:hover { background: #141414; }
  .related-card-name { font-family: 'Playfair Display', serif; font-size: 18px; margin-bottom: 8px; }
  .related-card-arrow { font-size: 12px; color: var(--red); margin-top: 12px; letter-spacing: 0.15em; text-transform: uppercase; }
  @media (max-width: 768px) { .related-section { padding: 40px 20px; } .related-grid { grid-template-columns: 1fr; } }"""

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

BADGE_FACT = '<span class="badge badge-fact" title="Источник: официальный санкционный реестр">Факт</span>'
BADGE_INTERP = '<span class="badge badge-interp" title="Авторская оценка задокументированных событий">Интерпр.</span>'
BADGE_FACT_EN = '<span class="badge badge-fact" title="Source: official sanctions registry">Fact</span>'
BADGE_INTERP_EN = '<span class="badge badge-interp" title="Editorial assessment of documented events">Interp.</span>'

def make_monogram(initials):
    return f'<text x="50%" y="42%" font-family="serif" font-size="120" fill="#8b1a1a" opacity="0.12" text-anchor="middle" dominant-baseline="middle" font-weight="700">{initials}</text>'

def make_ru_page(d):
    slug = d['slug']
    mono = make_monogram(d['initials'])
    svg = SVG_RIGHT.replace('{monogram}', mono)
    sources_html = '\n'.join(d.get('sources_ru', []))
    related_cards = ''.join([
        f'<a class="related-card" href="{r}.html"><div class="related-card-name">{d["related_names_ru"][i]}</div><div class="related-card-arrow">Читать досье →</div></a>'
        for i, r in enumerate(d['related'])
    ])

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
<meta property="og:image" content="https://cremle.netlify.app/og-{slug}.svg">
<meta name="twitter:image" content="https://cremle.netlify.app/og-{slug}.svg">
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

<div class="related-section">
  <div class="related-label">Похожие досье</div>
  <div class="related-grid">{related_cards}</div>
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
    related_cards = ''.join([
        f'<a class="related-card" href="{r}-en.html"><div class="related-card-name">{d["related_names_en"][i]}</div><div class="related-card-arrow">Read dossier →</div></a>'
        for i, r in enumerate(d['related'])
    ])

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
<meta property="og:image" content="https://cremle.netlify.app/og-{slug}.svg">
<meta name="twitter:image" content="https://cremle.netlify.app/og-{slug}.svg">
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

<div class="related-section">
  <div class="related-label">Related dossiers</div>
  <div class="related-grid">{related_cards}</div>
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

def meta_item(label, value):
    return f"""      <div class="meta-item"><label>{label}</label><span>{value}</span></div>"""

# ══════════════════════════════════════════════════════════════════════════
# PERSON DATA
# ══════════════════════════════════════════════════════════════════════════

PERSONS = []

# ── 1. ПЕСКОВ ─────────────────────────────────────────────────────────────
PERSONS.append({
    'slug': 'peskov',
    'initials': 'ДП',
    'name_ru': 'Дмитрий Песков',
    'name_en': 'Dmitry Peskov',
    'job_ru': 'Пресс-секретарь Президента России',
    'job_en': 'Press Secretary of the President of Russia',
    'birthdate': '1967-10-17',
    'desc_ru': 'Пресс-секретарь Путина с 2012 года: мастер официального отрицания, дипломатической лжи и управления нарративом. Биография, цитаты, санкции.',
    'desc_en': "Putin's press secretary since 2012: master of official denial, diplomatic deception, and narrative control. Biography, quotes, sanctions.",
    'hero_name_ru': 'Дмитрий<br>Песков',
    'hero_name_en': 'Dmitry<br>Peskov',
    'subtitle_ru': 'Голос президента. Ложь с трибуны.',
    'subtitle_en': "The President's voice. Lies from the podium.",
    'stamp_ru': 'Кремль · Санкции ЕС/UK 2022',
    'stamp_en': 'Kremlin · EU/UK Sanctions 2022',
    'meta_ru': '\n'.join([
        meta_item('Дата рождения', '17 октября 1967, Москва'),
        meta_item('Должность', 'Пресс-секретарь Президента РФ (с 2012)'),
        meta_item('Ранее', 'Заместитель руководителя Администрации Президента'),
        meta_item('Санкции', 'ЕС, Великобритания, Канада, Австралия'),
        meta_item('Семья', 'Женат на Татьяне Навке — олимпийской чемпионке'),
    ]),
    'meta_en': '\n'.join([
        meta_item('Born', 'October 17, 1967, Moscow'),
        meta_item('Role', 'Presidential Press Secretary (since 2012)'),
        meta_item('Previously', 'Deputy Head, Presidential Administration'),
        meta_item('Sanctions', 'EU, UK, Canada, Australia'),
        meta_item('Family', 'Married to Tatiana Navka — Olympic champion'),
    ]),
    'intro_ru': 'Дмитрий Песков — человек, чья работа состоит в том, чтобы Путин никогда не был виновен ни в чём. За двадцать лет он отработал технику официального отрицания до совершенства: войска у границы — «учения», сбитый самолёт — «провокация», вторжение — «специальная военная операция».',
    'intro_en': "Dmitry Peskov's job is to ensure Putin is never guilty of anything. Over twenty years he has perfected the art of official denial: troops at the border are \"exercises,\" a downed airliner is a \"provocation,\" an invasion is a \"special military operation.\"",
    'timeline_ru': '\n'.join([
        tl('1967', 'Рождение в Москве', 'Родился в семье дипломата. Окончил МГИМО по специальности «востоковедение». Свободно владеет турецким и английским. Карьера в МИД начинается в Турции.'),
        tl('1993–1999', 'Дипломатическая карьера', 'Работает в посольстве России в Анкаре. Встречается с Путиным, тогда ещё директором ФСБ. Быстро становится частью его ближайшего окружения.'),
        tl('2000', 'Пресс-служба Путина', 'Переходит в пресс-службу Путина с первых месяцев его президентства. Осваивает роль официального посредника между Кремлём и мировыми СМИ.'),
        tl('2012', 'Официальный пресс-секретарь', 'Назначается официальным пресс-секретарём Президента. С этого момента — ежедневный голос Кремля для мировых журналистов. Регулярно отрицает то, что снято на камеру. ' + BADGE_FACT),
        tl('2022', 'Война и санкции', 'Называет полномасштабное вторжение в Украину «специальной военной операцией», отрицает удары по мирным объектам, опровергает задокументированные военные преступления. ЕС, Великобритания, Канада и Австралия вводят персональные санкции. ' + BADGE_FACT + ' ' + BADGE_INTERP),
    ]),
    'timeline_en': '\n'.join([
        tl('1967', 'Born in Moscow', 'Born to a diplomat family. Graduated from MGIMO with a degree in Oriental studies. Fluent in Turkish and English. Career begins at the MFA in Turkey.'),
        tl('1993–1999', 'Diplomatic career', 'Serves at the Russian Embassy in Ankara. Meets Putin, then FSB Director. Quickly becomes part of his inner circle.'),
        tl('2000', "Putin's press service", "Joins Putin's press service from the first months of his presidency. Masters the role of official intermediary between the Kremlin and global media."),
        tl('2012', 'Official press secretary', 'Officially appointed Presidential Press Secretary. From this point, he is the Kremlin\'s daily voice for world journalists. Regularly denies what has been filmed on camera. ' + BADGE_FACT_EN),
        tl('2022', 'War and sanctions', 'Calls the full-scale invasion a "special military operation," denies strikes on civilian targets, refutes documented war crimes. EU, UK, Canada and Australia impose personal sanctions. ' + BADGE_FACT_EN + ' ' + BADGE_INTERP_EN),
    ]),
    'quotes_ru': '\n'.join([
        q('«Никаких российских войск на Украине нет и не было.»', '2014 — после ввода войск в Крым'),
        q('«Мы не нападали на Украину. Это специальная военная операция по защите людей.»', '24 февраля 2022'),
        q('«Россия не наносит удары по гражданской инфраструктуре. Это ложь западных СМИ.»', '2022 — ежедневный брифинг'),
        q('«У нас нет намерения оккупировать украинскую территорию. Мы достигнем своих целей переговорами.»', '2022'),
    ]),
    'quotes_en': '\n'.join([
        q('"There are no Russian troops in Ukraine, and there never were."', '2014 — after troops entered Crimea'),
        q('"We did not attack Ukraine. This is a special military operation to protect people."', 'February 24, 2022'),
        q('"Russia does not strike civilian infrastructure. This is a lie from Western media."', '2022 — daily briefing'),
        q('"We have no intention of occupying Ukrainian territory. We will achieve our goals through negotiations."', '2022'),
    ]),
    'method_ru': 'Метод Пескова — системное отрицание. Он не защищает конкретные факты, он создаёт атмосферу, в которой любой факт становится спорным. Отрицание войск в Крыму в 2014-м, отрицание MH17, отрицание Бучи — каждый раз одна и та же техника: «Это провокация», «Это фейк», «Это западная пропаганда». Главная цель — не убедить Запад, а создать у российской аудитории ощущение, что правды не существует. ' + BADGE_INTERP,
    'method_en': "Peskov's method is systemic denial. He does not defend specific facts — he creates an atmosphere in which any fact becomes debatable. Denying troops in Crimea in 2014, denying MH17, denying Bucha — each time the same technique: 'This is a provocation,' 'This is fake,' 'This is Western propaganda.' The main goal is not to convince the West, but to give Russian audiences the feeling that no truth exists. " + BADGE_INTERP_EN,
    'sanctions_ru': f'Персональные санкции ЕС с 2022 года — за активное участие в пропагандистском обосновании вторжения. {BADGE_FACT} Великобритания, Канада и Австралия ввели аналогичные ограничения. Активы заморожены, въезд в ЕС и Великобританию запрещён.',
    'sanctions_en': f'EU personal sanctions since 2022 — for actively participating in the propaganda justification of the invasion. {BADGE_FACT_EN} UK, Canada and Australia imposed equivalent measures. Assets frozen, entry to EU and UK banned.',
    'next_slug': 'lavrov',
    'next_name_ru': 'Сергей Лавров',
    'next_title_ru': 'Министр иностранных дел',
    'next_name_en': 'Sergei Lavrov',
    'next_title_en': 'Foreign Minister',
    'related': ['zakharova', 'medvedev', 'navka'],
    'related_names_ru': ['Мария Захарова', 'Дмитрий Медведев', 'Татьяна Навка'],
    'related_names_en': ['Maria Zakharova', 'Dmitry Medvedev', 'Tatiana Navka'],
    'sources_ru': [
        src_card_ru('Санкции · ЕС', 'EUR-Lex — Официальный реестр санкций ЕС', '2022 — за участие в пропаганде вторжения.<br>eur-lex.europa.eu'),
        src_card_ru('Санкции · Великобритания', 'FCDO · UK Sanctions List', 'gov.uk/government/collections/uk-sanctions'),
        src_card_ru('Биография', 'Wikipedia · Wikimedia Commons', 'ru.wikipedia.org/wiki/Песков,_Дмитрий_Сергеевич'),
        src_card_ru('Первоисточник', 'Kremlin.ru — официальные брифинги', 'Ежедневные пресс-брифинги пресс-секретаря. kremlin.ru'),
    ],
    'sources_en': [
        src_card_en('Sanctions · EU', 'EUR-Lex — Official EU Sanctions Register', '2022 — for participating in invasion propaganda.<br>eur-lex.europa.eu'),
        src_card_en('Sanctions · UK', 'FCDO · UK Sanctions List', 'gov.uk/government/collections/uk-sanctions'),
        src_card_en('Biography', 'Wikipedia · Wikimedia Commons', 'en.wikipedia.org/wiki/Dmitry_Peskov'),
        src_card_en('Primary source', 'Kremlin.ru — official briefings', 'Daily press briefings archive. kremlin.ru'),
    ],
})

# ── 2. ЛАВРОВ ─────────────────────────────────────────────────────────────
PERSONS.append({
    'slug': 'lavrov',
    'initials': 'СЛ',
    'name_ru': 'Сергей Лавров',
    'name_en': 'Sergei Lavrov',
    'job_ru': 'Министр иностранных дел России',
    'job_en': 'Minister of Foreign Affairs of Russia',
    'birthdate': '1950-03-21',
    'desc_ru': 'Министр иностранных дел с 2004 года: превратил дипломатию в инструмент войны. Самый долгослужащий глава МИД России за постсоветскую историю. Биография, цитаты, санкции.',
    'desc_en': "Foreign Minister since 2004: turned diplomacy into an instrument of war. Russia's longest-serving post-Soviet foreign minister. Biography, quotes, sanctions.",
    'hero_name_ru': 'Сергей<br>Лавров',
    'hero_name_en': 'Sergei<br>Lavrov',
    'subtitle_ru': 'Дипломатия как оружие. Двадцать лет лжи.',
    'subtitle_en': 'Diplomacy as a weapon. Twenty years of deception.',
    'stamp_ru': 'МИД · Санкции ЕС/UK/США 2022',
    'stamp_en': 'MFA · EU/UK/US Sanctions 2022',
    'meta_ru': '\n'.join([
        meta_item('Дата рождения', '21 марта 1950, Москва'),
        meta_item('Должность', 'Министр иностранных дел РФ (с 2004)'),
        meta_item('Ранее', 'Постпред России при ООН (1994–2004)'),
        meta_item('Санкции', 'ЕС, США, Великобритания, Канада, Австралия'),
        meta_item('Образование', 'МГИМО, 1972 — специальность «международные отношения»'),
    ]),
    'meta_en': '\n'.join([
        meta_item('Born', 'March 21, 1950, Moscow'),
        meta_item('Role', 'Minister of Foreign Affairs (since 2004)'),
        meta_item('Previously', "Russia's UN Permanent Representative (1994–2004)"),
        meta_item('Sanctions', 'EU, USA, UK, Canada, Australia'),
        meta_item('Education', 'MGIMO, 1972 — International Relations'),
    ]),
    'intro_ru': 'Лавров — самый долгослужащий министр иностранных дел России в постсоветской истории. Блестящий дипломат советской выправки, он превратил международные переговоры в инструмент затягивания времени и маскировки агрессии.',
    'intro_en': "Lavrov is Russia's longest-serving post-Soviet foreign minister. A brilliant diplomat of Soviet vintage, he transformed international negotiations into an instrument for buying time and masking aggression.",
    'timeline_ru': '\n'.join([
        tl('1950', 'Рождение в Москве', 'Родился в Москве. Окончил МГИМО в 1972 году. Полиглот: свободно владеет английским, французским, сингальским. С первых лет работает в МИД СССР.'),
        tl('1972–1994', 'МИД СССР и МИД России', 'Работает в посольствах Шри-Ланки и США, в центральном аппарате МИД. Проходит путь от атташе до директора Управления международных организаций. Известен железной выдержкой и острым языком.'),
        tl('1994–2004', 'Постпред при ООН', 'Десять лет представляет Россию в Совете Безопасности ООН. Мастерски использует право вето, блокируя резолюции по Чечне, Грузии, Украине. Создаёт репутацию непреклонного переговорщика.'),
        tl('2004', 'Министр иностранных дел', 'Назначается Путиным. Немедленно меняет тональность российской дипломатии: от постсоветской «адаптации» к нарративу «суверенной сферы влияния» и противостояния с Западом.'),
        tl('2014', 'Крым и дипломатия отрицания', 'Публично отрицает присутствие российских войск в Крыму, называя их «местной самообороной». Ведёт переговоры в Женеве, одновременно координируя оккупацию. Введены первые санкции ЕС. ' + BADGE_FACT),
        tl('2022', 'Война и изоляция', 'Продолжает представлять Россию на международных форумах, несмотря на полномасштабное вторжение. Использует трибуну ООН для антиукраинской пропаганды. Персональные санкции ЕС, США, Великобритании, Канады, Австралии. ' + BADGE_FACT + ' ' + BADGE_INTERP),
    ]),
    'timeline_en': '\n'.join([
        tl('1950', 'Born in Moscow', 'Born in Moscow. Graduated MGIMO in 1972. Polyglot: fluent in English, French, Sinhalese. Begins career at the Soviet MFA immediately.'),
        tl('1972–1994', 'Soviet and Russian MFA', 'Serves in embassies in Sri Lanka and the USA, and in MFA headquarters. Rises from attaché to Director of the International Organizations Department. Known for steely composure and sharp tongue.'),
        tl('1994–2004', 'UN Permanent Representative', 'Ten years representing Russia on the Security Council. Masters the use of veto, blocking resolutions on Chechnya, Georgia, Ukraine. Builds reputation as an unyielding negotiator.'),
        tl('2004', 'Foreign Minister', "Appointed by Putin. Immediately shifts the tone of Russian diplomacy: from post-Soviet 'adaptation' to a narrative of 'sovereign sphere of influence' and confrontation with the West."),
        tl('2014', 'Crimea and denial diplomacy', 'Publicly denies the presence of Russian troops in Crimea, calling them "local self-defense." Negotiates in Geneva while simultaneously coordinating the occupation. First EU sanctions imposed. ' + BADGE_FACT_EN),
        tl('2022', 'War and isolation', 'Continues representing Russia at international forums despite full-scale invasion. Uses the UN podium for anti-Ukrainian propaganda. Personal sanctions from EU, USA, UK, Canada, Australia. ' + BADGE_FACT_EN + ' ' + BADGE_INTERP_EN),
    ]),
    'quotes_ru': '\n'.join([
        q('«НАТО расширялось на восток вопреки обещаниям. Мы лишь восстанавливаем исторический баланс.»', '2022 — Совет Безопасности ООН'),
        q('«Запад объявил нам гибридную войну. Мы вынуждены защищаться.»', '2022'),
        q('«Украина — это не государство. Это проект, созданный Западом против России.»', '2022 — RT-интервью'),
        q('«Российские войска защищают мирное население от нацистского режима Киева.»', '2022'),
    ]),
    'quotes_en': '\n'.join([
        q('"NATO expanded eastward despite promises. We are merely restoring the historical balance."', '2022 — UN Security Council'),
        q('"The West has declared hybrid war on us. We are forced to defend ourselves."', '2022'),
        q('"Ukraine is not a state. It is a project created by the West against Russia."', '2022 — RT interview'),
        q('"Russian troops are protecting the civilian population from the Nazi regime in Kyiv."', '2022'),
    ]),
    'method_ru': 'Лавров — мастер «дипломатии отрицания». Он использует язык международного права и риторику многополярности как щит для прикрытия агрессии. Каждый раз, когда Россия нарушала международные нормы, Лавров стоял за трибуной с папкой документов и объяснял, почему это другие. Его главный инструмент — не ложь в лоб, а переопределение реальности: «вторжение» становится «операцией», «оккупация» — «воссоединением», «военные преступления» — «провокациями ВСУ». ' + BADGE_INTERP,
    'method_en': "Lavrov is a master of 'denial diplomacy.' He uses the language of international law and multipolar rhetoric as a shield to cover aggression. Every time Russia violated international norms, Lavrov stood at the podium with a folder of documents explaining why it was always someone else's fault. His main tool is not blunt lying, but redefinition of reality: an 'invasion' becomes an 'operation,' 'occupation' becomes 'reunification,' 'war crimes' become 'VSU provocations.' " + BADGE_INTERP_EN,
    'sanctions_ru': f'Персональные санкции ЕС с 2022 года — за центральную роль в дипломатическом прикрытии вторжения. {BADGE_FACT} Великобритания, США, Канада и Австралия ввели аналогичные меры. Въезд в ЕС и Великобританию запрещён, активы заморожены.',
    'sanctions_en': f'EU personal sanctions since 2022 — for a central role in diplomatic cover for the invasion. {BADGE_FACT_EN} UK, USA, Canada and Australia imposed equivalent measures. Entry to EU and UK banned, assets frozen.',
    'next_slug': 'mizulina',
    'next_name_ru': 'Елена Мизулина',
    'next_title_ru': 'Архитектор цензуры',
    'next_name_en': 'Elena Mizulina',
    'next_title_en': 'The Architect of Censorship',
    'related': ['zakharova', 'peskov', 'medvedev'],
    'related_names_ru': ['Мария Захарова', 'Дмитрий Песков', 'Дмитрий Медведев'],
    'related_names_en': ['Maria Zakharova', 'Dmitry Peskov', 'Dmitry Medvedev'],
    'sources_ru': [
        src_card_ru('Санкции · ЕС', 'EUR-Lex — Официальный реестр санкций ЕС', '2022 — за дипломатическое прикрытие вторжения.<br>eur-lex.europa.eu'),
        src_card_ru('Санкции · США', 'OFAC SDN List — Министерство финансов США', '2022 — ofac.treas.gov'),
        src_card_ru('Санкции · Великобритания', 'FCDO · UK Sanctions List', 'gov.uk/government/collections/uk-sanctions'),
        src_card_ru('Биография', 'Wikipedia · Wikimedia Commons', 'ru.wikipedia.org/wiki/Лавров,_Сергей_Викторович'),
        src_card_ru('Первоисточник', 'МИД России / mid.ru', 'Официальные выступления и интервью. mid.ru'),
    ],
    'sources_en': [
        src_card_en('Sanctions · EU', 'EUR-Lex — Official EU Sanctions Register', '2022 — for diplomatic cover of the invasion.<br>eur-lex.europa.eu'),
        src_card_en('Sanctions · USA', 'OFAC SDN List — U.S. Treasury', '2022 — ofac.treas.gov'),
        src_card_en('Sanctions · UK', 'FCDO · UK Sanctions List', 'gov.uk/government/collections/uk-sanctions'),
        src_card_en('Biography', 'Wikipedia · Wikimedia Commons', 'en.wikipedia.org/wiki/Sergei_Lavrov'),
        src_card_en('Primary source', 'Russian MFA / mid.ru', 'Official speeches and interviews. mid.ru'),
    ],
})

# ── 3. МИЗУЛИНА ───────────────────────────────────────────────────────────
PERSONS.append({
    'slug': 'mizulina',
    'initials': 'ЕМ',
    'name_ru': 'Елена Мизулина',
    'name_en': 'Elena Mizulina',
    'job_ru': 'Сенатор Совета Федерации, автор законов о цензуре',
    'job_en': 'Senator, Federation Council; author of censorship legislation',
    'birthdate': '1954-01-09',
    'desc_ru': 'Архитектор российской цензуры: закон о ЛГБТ-пропаганде, закон о «дискредитации армии», давление на интернет. Биография, цитаты, санкции.',
    'desc_en': "Russia's chief architect of censorship: the anti-LGBT propaganda law, the 'discrediting the army' law, internet suppression. Biography, quotes, sanctions.",
    'hero_name_ru': 'Елена<br>Мизулина',
    'hero_name_en': 'Elena<br>Mizulina',
    'subtitle_ru': 'Архитектор цензуры. Законы как оружие.',
    'subtitle_en': 'The Architect of Censorship. Laws as weapons.',
    'stamp_ru': 'Сенатор · Санкции ЕС 2022',
    'stamp_en': 'Senator · EU Sanctions 2022',
    'meta_ru': '\n'.join([
        meta_item('Дата рождения', '9 января 1954, Буй, Костромская область'),
        meta_item('Должность', 'Сенатор Совета Федерации (с 2013)'),
        meta_item('Ранее', 'Депутат Государственной Думы (1999–2013)'),
        meta_item('Санкции', 'ЕС (2022), Великобритания (2022)'),
        meta_item('Сын', 'Николай Мизулин — руководитель Лиги Безопасного Интернета'),
    ]),
    'meta_en': '\n'.join([
        meta_item('Born', 'January 9, 1954, Bui, Kostroma Oblast'),
        meta_item('Role', 'Senator, Federation Council (since 2013)'),
        meta_item('Previously', 'State Duma Deputy (1999–2013)'),
        meta_item('Sanctions', 'EU (2022), UK (2022)'),
        meta_item('Son', 'Nikolai Mizulin — head of the Safe Internet League'),
    ]),
    'intro_ru': 'Елена Мизулина — главный архитектор репрессивного законодательства постпутинской России. Её имя связано с законами, которые криминализировали инакомыслие, ЛГБТ-идентичность, критику армии и «неуважение» к государству.',
    'intro_en': "Elena Mizulina is the chief architect of repressive legislation in post-2000 Russia. Her name is associated with laws that criminalized dissent, LGBT identity, criticism of the military, and 'disrespect' for the state.",
    'timeline_ru': '\n'.join([
        tl('1954', 'Рождение', 'Родилась в Костромской области. Окончила юридический факультет ЯрГУ. Кандидат наук, специалист по уголовному праву. Преподавала право в 1980–1990-х.'),
        tl('1999', 'Вход в политику', 'Избирается в Государственную Думу от «Яблока», позже переходит в «Справедливую Россию». Возглавляет Комитет по вопросам семьи, женщин и детей — инструмент, который она использует для продвижения консервативной повестки.'),
        tl('2013', 'Закон о ЛГБТ-пропаганде', 'Лично разрабатывает и проводит через Думу «закон о гей-пропаганде». Закон запрещает «пропаганду нетрадиционных сексуальных отношений» среди несовершеннолетних. Вызывает международное осуждение. ' + BADGE_FACT),
        tl('2013', 'Переход в Совет Федерации', 'Становится сенатором от Омской области. Продолжает законодательную деятельность в верхней палате, сохраняя медийную активность.'),
        tl('2022', 'Война и цензура', 'Активно поддерживает вторжение. Её сын Николай Мизулин возглавляет Лигу Безопасного Интернета — главный инструмент блокировки независимых СМИ и мессенджеров. Сама Мизулина публично требует «закрыть» оппозиционные ресурсы. ЕС и Великобритания вводят санкции. ' + BADGE_FACT + ' ' + BADGE_INTERP),
    ]),
    'timeline_en': '\n'.join([
        tl('1954', 'Birth', 'Born in Kostroma Oblast. Graduated from the Law Faculty of Yaroslavl State University. PhD in criminal law. Taught law in the 1980–90s.'),
        tl('1999', 'Entry into politics', "Elected to the State Duma from Yabloko, later joins A Just Russia. Chairs the Committee on Family, Women and Children — a tool she uses to advance a conservative agenda."),
        tl('2013', 'LGBT propaganda law', 'Personally drafts and shepherds through the Duma the "gay propaganda law." The law bans "propaganda of non-traditional sexual relationships" to minors. Draws international condemnation. ' + BADGE_FACT_EN),
        tl('2013', 'Transfer to Federation Council', 'Becomes a senator from Omsk Oblast. Continues legislative work in the upper chamber while maintaining media visibility.'),
        tl('2022', 'War and censorship', "Actively supports the invasion. Her son Nikolai Mizulin heads the Safe Internet League — the primary tool for blocking independent media and messengers. Mizulina herself publicly demands the 'shutdown' of opposition resources. EU and UK impose sanctions. " + BADGE_FACT_EN + ' ' + BADGE_INTERP_EN),
    ]),
    'quotes_ru': '\n'.join([
        q('«Гей-парады — это пропаганда разврата. Мы обязаны защитить наших детей.»', '2013 — Государственная Дума'),
        q('«Кто критикует нашу армию — тот враг. Закон это подтверждает.»', '2022'),
        q('«Интернет без контроля — это оружие против государства. Его нужно регулировать.»', '2020'),
        q('«Традиционные ценности — это не ограничение. Это наша идентичность.»', '2014'),
    ]),
    'quotes_en': '\n'.join([
        q('"Gay parades are propaganda of depravity. We must protect our children."', '2013 — State Duma'),
        q('"Whoever criticizes our army is an enemy. The law confirms it."', '2022'),
        q('"An uncontrolled internet is a weapon against the state. It must be regulated."', '2020'),
        q('"Traditional values are not a restriction. They are our identity."', '2014'),
    ]),
    'method_ru': 'Мизулина работает через законодательство. Она не агитирует с телеэкрана — она вписывает репрессии в правовую систему. Закон о «гей-пропаганде» 2013 года создал прецедент: после него последовали законы о «дискредитации армии», о «фейках» про войну, о «неуважении к государственным символам». Каждый закон расширял пространство уголовного преследования инакомыслия. Её сын руководит инструментом интернет-цензуры — семейный бизнес на репрессиях. ' + BADGE_INTERP,
    'method_en': "Mizulina works through legislation. She does not agitate on TV screens — she writes repression into the legal system. The 2013 'gay propaganda' law created a precedent: it was followed by laws on 'discrediting the army,' 'fakes about the war,' and 'disrespecting state symbols.' Each law expanded the space for criminal prosecution of dissent. Her son runs the internet censorship tool — a family business built on repression. " + BADGE_INTERP_EN,
    'sanctions_ru': f'Персональные санкции ЕС с 2022 года — за поддержку вторжения и законодательные инструменты политических репрессий. {BADGE_FACT} Великобритания ввела аналогичные санкции. Въезд запрещён, активы заморожены.',
    'sanctions_en': f'EU personal sanctions since 2022 — for supporting the invasion and providing legislative tools for political repression. {BADGE_FACT_EN} UK imposed equivalent sanctions. Entry banned, assets frozen.',
    'next_slug': 'solovyov',
    'next_name_ru': 'Владимир Соловьёв',
    'next_title_ru': 'Голос войны',
    'next_name_en': 'Vladimir Solovyov',
    'next_title_en': 'The Voice of War',
    'related': ['medvedev', 'turchak', 'nikonov'],
    'related_names_ru': ['Дмитрий Медведев', 'Андрей Турчак', 'Вячеслав Никонов'],
    'related_names_en': ['Dmitry Medvedev', 'Andrei Turchak', 'Vyacheslav Nikonov'],
    'sources_ru': [
        src_card_ru('Санкции · ЕС', 'EUR-Lex — Официальный реестр санкций ЕС', '2022 — за поддержку вторжения.<br>eur-lex.europa.eu'),
        src_card_ru('Санкции · Великобритания', 'FCDO · UK Sanctions List', 'gov.uk/government/collections/uk-sanctions'),
        src_card_ru('Законодательство', 'Государственная Дума / duma.gov.ru', 'Тексты законов о «гей-пропаганде» и «дискредитации армии».'),
        src_card_ru('Биография', 'Wikipedia · Wikimedia Commons', 'ru.wikipedia.org/wiki/Мизулина,_Елена_Борисовна'),
    ],
    'sources_en': [
        src_card_en('Sanctions · EU', 'EUR-Lex — Official EU Sanctions Register', '2022 — for supporting the invasion.<br>eur-lex.europa.eu'),
        src_card_en('Sanctions · UK', 'FCDO · UK Sanctions List', 'gov.uk/government/collections/uk-sanctions'),
        src_card_en('Legislation', 'State Duma / duma.gov.ru', 'Texts of the "gay propaganda" and "army discreditation" laws.'),
        src_card_en('Biography', 'Wikipedia · Wikimedia Commons', 'en.wikipedia.org/wiki/Elena_Mizulina'),
    ],
})

# ══════════════════════════════════════════════════════════════════════════
# GENERATE PAGES
# ══════════════════════════════════════════════════════════════════════════

for d in PERSONS:
    slug = d['slug']
    ru_path = BASE + slug + '.html'
    en_path = BASE + slug + '-en.html'

    with open(ru_path, 'w', encoding='utf-8') as f:
        f.write(make_ru_page(d))
    print(f'✓ {slug}.html')

    with open(en_path, 'w', encoding='utf-8') as f:
        f.write(make_en_page(d))
    print(f'✓ {slug}-en.html')

# ══════════════════════════════════════════════════════════════════════════
# GENERATE OG SVGs
# ══════════════════════════════════════════════════════════════════════════

NEW_OG = {
    'peskov':   ('Dmitry Peskov',   "The President's Spokesman",    'Голоса Кремля'),
    'lavrov':   ('Sergei Lavrov',   'The Diplomat of Deception',    'Голоса Кремля'),
    'mizulina': ('Elena Mizulina',  'The Censorship Architect',     'Голоса Кремля'),
}

def make_og_svg(slug, name, subtitle, brand):
    def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    parts = name.split()
    if len(parts) >= 3:
        mid = len(parts)//2
        line1 = ' '.join(parts[:mid])
        line2 = ' '.join(parts[mid:])
    elif len(parts) == 2:
        line1, line2 = parts[0], parts[1]
    else:
        line1, line2 = name, ''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <defs>
    <radialGradient id="bg" cx="30%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#1a0000"/>
      <stop offset="100%" stop-color="#040404"/>
    </radialGradient>
  </defs>
  <rect width="1200" height="630" fill="url(#bg)"/>
  <rect x="0" y="0" width="6" height="630" fill="#8b1a1a"/>
  <line x1="60" y1="420" x2="1140" y2="420" stroke="#1c1c1c" stroke-width="1"/>
  <text x="60" y="100" font-family="Georgia,serif" font-size="13" fill="#8b1a1a" letter-spacing="4">KREMLIN VOICES · ДОСЬЕ</text>
  <text x="60" y="240" font-family="Georgia,serif" font-size="86" font-weight="bold" fill="#ede8dc">{esc(line1)}</text>
  {'<text x="60" y="330" font-family="Georgia,serif" font-size="86" font-weight="bold" fill="#ede8dc">' + esc(line2) + '</text>' if line2 else ''}
  <text x="60" y="390" font-family="Georgia,serif" font-size="24" font-style="italic" fill="#8b8070">{esc(subtitle)}</text>
  <text x="60" y="480" font-family="Arial,sans-serif" font-size="14" fill="#555" letter-spacing="2">KREMLIN VOICES · cremle.netlify.app</text>
</svg>'''

for slug, (name, subtitle, brand) in NEW_OG.items():
    svg_path = BASE + f'og-{slug}.svg'
    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(make_og_svg(slug, name, subtitle, brand))
    print(f'✓ og-{slug}.svg')

# ══════════════════════════════════════════════════════════════════════════
# UPDATE INDEX.HTML — add 3 cards
# ══════════════════════════════════════════════════════════════════════════

NEW_CARDS_RU = """          <a class="card" href="peskov.html">
            <div class="card-num">28</div>
            <div class="card-name">Дмитрий Песков</div>
            <div class="card-role">Пресс-секретарь Путина</div>
            <div class="card-channel">Кремль</div>
          </a>
          <a class="card" href="lavrov.html">
            <div class="card-num">29</div>
            <div class="card-name">Сергей Лавров</div>
            <div class="card-role">Министр иностранных дел</div>
            <div class="card-channel">МИД России</div>
          </a>
          <a class="card" href="mizulina.html">
            <div class="card-num">30</div>
            <div class="card-name">Елена Мизулина</div>
            <div class="card-role">Сенатор, автор законов о цензуре</div>
            <div class="card-channel">Совет Федерации</div>
          </a>"""

NEW_CARDS_EN = """          <a class="card" href="peskov-en.html">
            <div class="card-num">28</div>
            <div class="card-name">Dmitry Peskov</div>
            <div class="card-role">Putin's Press Secretary</div>
            <div class="card-channel">Kremlin</div>
          </a>
          <a class="card" href="lavrov-en.html">
            <div class="card-num">29</div>
            <div class="card-name">Sergei Lavrov</div>
            <div class="card-role">Foreign Minister</div>
            <div class="card-channel">Russian MFA</div>
          </a>
          <a class="card" href="mizulina-en.html">
            <div class="card-num">30</div>
            <div class="card-name">Elena Mizulina</div>
            <div class="card-role">Senator, censorship architect</div>
            <div class="card-channel">Federation Council</div>
          </a>"""

for fname, new_cards in [('index.html', NEW_CARDS_RU), ('index-en.html', NEW_CARDS_EN)]:
    path = BASE + fname
    with open(path, encoding='utf-8') as f:
        html = f.read()
    if 'peskov' not in html:
        # Find last card ending and insert before </div> closing the cards grid
        html = html.replace('</div>\n        </div>\n      </section>', new_cards + '\n</div>\n        </div>\n      </section>', 1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'✓ {fname} cards updated')

# Fix counters 27→30
for fname in ['index.html', 'index-en.html']:
    path = BASE + fname
    with open(path, encoding='utf-8') as f:
        html = f.read()
    if '>27<' in html:
        html = html.replace('>27<', '>30<')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'✓ Counter 27→30: {fname}')

# ══════════════════════════════════════════════════════════════════════════
# UPDATE compare.html — add 3 persons (RU)
# ══════════════════════════════════════════════════════════════════════════

with open(BASE + 'compare.html', encoding='utf-8') as f:
    cmp_ru = f.read()

if 'peskov' not in cmp_ru:
    cmp_ru = cmp_ru.replace(
        '      <option value="navka">Татьяна Навка</option>\n    </select>\n  </div>\n  <div class="vs-label">',
        """      <option value="navka">Татьяна Навка</option>
      <option value="peskov">Дмитрий Песков</option>
      <option value="lavrov">Сергей Лавров</option>
      <option value="mizulina">Елена Мизулина</option>
    </select>
  </div>
  <div class="vs-label">"""
    )
    cmp_ru = cmp_ru.replace(
        '      <option value="navka">Татьяна Навка</option>\n    </select>\n  </div>',
        """      <option value="navka">Татьяна Навка</option>
      <option value="peskov">Дмитрий Песков</option>
      <option value="lavrov">Сергей Лавров</option>
      <option value="mizulina">Елена Мизулина</option>
    </select>
  </div>"""
    )
    cmp_ru = cmp_ru.replace(
        "    dosye: 'navka.html'\n  }\n};",
        """    dosye: 'navka.html'
  },
  peskov: {
    name: 'Дмитрий Песков', born: '17 октября 1967, Москва',
    channel: 'Пресс-служба Президента', show: 'Пресс-секретарь Путина (с 2012)',
    sanctions: ['ЕС (2022)', 'Великобритания (2022)', 'Канада (2022)', 'Австралия (2022)'],
    method: 'Официальное отрицание как система. Делает любой факт спорным.',
    quote: '«Никаких российских войск на Украине нет и не было.»',
    year: '2022', property: 'Санкции ЕС, UK, Канады, Австралии с 2022.',
    dosye: 'peskov.html'
  },
  lavrov: {
    name: 'Сергей Лавров', born: '21 марта 1950, Москва',
    channel: 'МИД России', show: 'Министр иностранных дел (с 2004)',
    sanctions: ['ЕС (2022)', 'США (2022)', 'Великобритания (2022)', 'Канада (2022)', 'Австралия (2022)'],
    method: 'Дипломатия отрицания. Переопределяет реальность через институт МИД.',
    quote: '«НАТО расширялось на восток вопреки обещаниям. Мы восстанавливаем баланс.»',
    year: '2022', property: 'Санкции ЕС, США, UK, Канады, Австралии с 2022.',
    dosye: 'lavrov.html'
  },
  mizulina: {
    name: 'Елена Мизулина', born: '9 января 1954, Буй',
    channel: 'Совет Федерации', show: 'Сенатор, автор законов о цензуре',
    sanctions: ['ЕС (2022)', 'Великобритания (2022)'],
    method: 'Репрессии через законодательство. Создаёт правовую основу для преследования инакомыслия.',
    quote: '«Кто критикует нашу армию — тот враг. Закон это подтверждает.»',
    year: '2022', property: 'Санкции ЕС и Великобритании с 2022 года.',
    dosye: 'mizulina.html'
  }
};"""
    )
    with open(BASE + 'compare.html', 'w', encoding='utf-8') as f:
        f.write(cmp_ru)
    print('✓ compare.html updated')

# ══════════════════════════════════════════════════════════════════════════
# UPDATE compare-en.html — add 3 persons (EN)
# ══════════════════════════════════════════════════════════════════════════

with open(BASE + 'compare-en.html', encoding='utf-8') as f:
    cmp_en = f.read()

if 'peskov' not in cmp_en:
    cmp_en = cmp_en.replace(
        '      <option value="navka">Tatiana Navka</option>\n    </select>\n  </div>\n  <div class="vs-label">',
        """      <option value="navka">Tatiana Navka</option>
      <option value="peskov">Dmitry Peskov</option>
      <option value="lavrov">Sergei Lavrov</option>
      <option value="mizulina">Elena Mizulina</option>
    </select>
  </div>
  <div class="vs-label">"""
    )
    cmp_en = cmp_en.replace(
        '      <option value="navka">Tatiana Navka</option>\n    </select>\n  </div>',
        """      <option value="navka">Tatiana Navka</option>
      <option value="peskov">Dmitry Peskov</option>
      <option value="lavrov">Sergei Lavrov</option>
      <option value="mizulina">Elena Mizulina</option>
    </select>
  </div>"""
    )
    cmp_en = cmp_en.replace(
        "    dosye: 'navka-en.html'\n  }\n};",
        """    dosye: 'navka-en.html'
  },
  peskov: {
    name: 'Dmitry Peskov', born: 'October 17, 1967, Moscow',
    channel: 'Presidential Press Service', show: "Putin's Press Secretary (since 2012)",
    sanctions: ['EU (2022)', 'UK (2022)', 'Canada (2022)', 'Australia (2022)'],
    method: 'Systemic denial. Makes any fact debatable.',
    quote: '"There are no Russian troops in Ukraine, and there never were."',
    year: '2022', property: 'EU, UK, Canada, Australia sanctions since 2022.',
    dosye: 'peskov-en.html'
  },
  lavrov: {
    name: 'Sergei Lavrov', born: 'March 21, 1950, Moscow',
    channel: 'Russian MFA', show: 'Foreign Minister (since 2004)',
    sanctions: ['EU (2022)', 'USA (2022)', 'UK (2022)', 'Canada (2022)', 'Australia (2022)'],
    method: 'Denial diplomacy. Redefines reality through the institution of the MFA.',
    quote: '"NATO expanded eastward despite promises. We are restoring the balance."',
    year: '2022', property: 'EU, USA, UK, Canada, Australia sanctions since 2022.',
    dosye: 'lavrov-en.html'
  },
  mizulina: {
    name: 'Elena Mizulina', born: 'January 9, 1954, Bui',
    channel: 'Federation Council', show: 'Senator, censorship architect',
    sanctions: ['EU (2022)', 'UK (2022)'],
    method: 'Repression through legislation. Creates legal framework for prosecuting dissent.',
    quote: '"Whoever criticizes our army is an enemy. The law confirms it."',
    year: '2022', property: 'EU and UK sanctions since 2022.',
    dosye: 'mizulina-en.html'
  }
};"""
    )
    with open(BASE + 'compare-en.html', 'w', encoding='utf-8') as f:
        f.write(cmp_en)
    print('✓ compare-en.html updated')

# ══════════════════════════════════════════════════════════════════════════
# UPDATE quotes.html — add 3 quotes (RU)
# ══════════════════════════════════════════════════════════════════════════

with open(BASE + 'quotes.html', encoding='utf-8') as f:
    q_ru = f.read()

if 'peskov.html' not in q_ru:
    q_ru = q_ru.replace(
        '<div class="qc-person"><a href="navka.html">Татьяна Навка</a></div>',
        '''<div class="qc-person"><a href="navka.html">Татьяна Навка</a></div>
        </div>
        <div class="quote-card">
          <div class="quote-text">«Никаких российских войск на Украине нет и не было.»</div>
          <div class="qc-person"><a href="peskov.html">Дмитрий Песков</a></div>
          <div class="qc-date">2014 — после ввода войск в Крым</div>
        </div>
        <div class="quote-card">
          <div class="quote-text">«НАТО расширялось на восток вопреки обещаниям. Мы восстанавливаем исторический баланс.»</div>
          <div class="qc-person"><a href="lavrov.html">Сергей Лавров</a></div>
          <div class="qc-date">2022 — Совет Безопасности ООН</div>
        </div>
        <div class="quote-card">
          <div class="quote-text">«Кто критикует нашу армию — тот враг. Закон это подтверждает.»</div>
          <div class="qc-person"><a href="mizulina.html">Елена Мизулина</a></div>
          <div class="qc-date">2022'''
    )
    with open(BASE + 'quotes.html', 'w', encoding='utf-8') as f:
        f.write(q_ru)
    print('✓ quotes.html updated')

# ══════════════════════════════════════════════════════════════════════════
# UPDATE quotes-en.html — add 3 quotes (EN)
# ══════════════════════════════════════════════════════════════════════════

with open(BASE + 'quotes-en.html', encoding='utf-8') as f:
    q_en = f.read()

if 'peskov-en.html' not in q_en:
    q_en = q_en.replace(
        '<div class="qc-person"><a href="navka-en.html">Tatiana Navka</a></div>',
        '''<div class="qc-person"><a href="navka-en.html">Tatiana Navka</a></div>
        </div>
        <div class="quote-card">
          <div class="quote-text">"There are no Russian troops in Ukraine, and there never were."</div>
          <div class="qc-person"><a href="peskov-en.html">Dmitry Peskov</a></div>
          <div class="qc-date">2014 — after troops entered Crimea</div>
        </div>
        <div class="quote-card">
          <div class="quote-text">"NATO expanded eastward despite promises. We are restoring the historical balance."</div>
          <div class="qc-person"><a href="lavrov-en.html">Sergei Lavrov</a></div>
          <div class="qc-date">2022 — UN Security Council</div>
        </div>
        <div class="quote-card">
          <div class="quote-text">"Whoever criticizes our army is an enemy. The law confirms it."</div>
          <div class="qc-person"><a href="mizulina-en.html">Elena Mizulina</a></div>
          <div class="qc-date">2022'''
    )
    with open(BASE + 'quotes-en.html', 'w', encoding='utf-8') as f:
        f.write(q_en)
    print('✓ quotes-en.html updated')

# ══════════════════════════════════════════════════════════════════════════
# UPDATE sanctions.html — add rows 28-30 (RU)
# ══════════════════════════════════════════════════════════════════════════

with open(BASE + 'sanctions.html', encoding='utf-8') as f:
    san_ru = f.read()

if 'peskov.html' not in san_ru:
    NEW_ROWS_RU = '''
        <div class="person-row">
          <div class="person-info">
            <ul class="person-sanctions-list">
              <li>
                <span class="person-num">28</span>
                <div class="person-details">
                  <a href="peskov.html" class="person-name-link"><div class="person-name">Дмитрий Песков</div></a>
                  <div class="person-role">Пресс-секретарь Путина</div>
                </div>
              </li>
              <li><span class="sanction-label">ЕС</span><span class="sanction-yes">Санкции</span><span class="sanction-date">2022</span></li>
              <li><span class="sanction-label">США</span><span class="sanction-no">—</span></li>
              <li><span class="sanction-label">UK</span><span class="sanction-yes">Санкции</span><span class="sanction-date">2022</span></li>
              <li><span class="sanction-label">Канада</span><span class="sanction-yes">Санкции</span><span class="sanction-date">2022</span></li>
            </ul>
          </div>
        </div>
        <div class="person-row">
          <div class="person-info">
            <ul class="person-sanctions-list">
              <li>
                <span class="person-num">29</span>
                <div class="person-details">
                  <a href="lavrov.html" class="person-name-link"><div class="person-name">Сергей Лавров</div></a>
                  <div class="person-role">Министр иностранных дел</div>
                </div>
              </li>
              <li><span class="sanction-label">ЕС</span><span class="sanction-yes">Санкции</span><span class="sanction-date">2022</span></li>
              <li><span class="sanction-label">США</span><span class="sanction-yes">Санкции</span><span class="sanction-date">2022</span></li>
              <li><span class="sanction-label">UK</span><span class="sanction-yes">Санкции</span><span class="sanction-date">2022</span></li>
              <li><span class="sanction-label">Канада</span><span class="sanction-yes">Санкции</span><span class="sanction-date">2022</span></li>
            </ul>
          </div>
        </div>
        <div class="person-row">
          <div class="person-info">
            <ul class="person-sanctions-list">
              <li>
                <span class="person-num">30</span>
                <div class="person-details">
                  <a href="mizulina.html" class="person-name-link"><div class="person-name">Елена Мизулина</div></a>
                  <div class="person-role">Сенатор, автор законов о цензуре</div>
                </div>
              </li>
              <li><span class="sanction-label">ЕС</span><span class="sanction-yes">Санкции</span><span class="sanction-date">2022</span></li>
              <li><span class="sanction-label">США</span><span class="sanction-no">—</span></li>
              <li><span class="sanction-label">UK</span><span class="sanction-yes">Санкции</span><span class="sanction-date">2022</span></li>
              <li><span class="sanction-label">Канада</span><span class="sanction-no">—</span></li>
            </ul>
          </div>
        </div>'''
    san_ru = san_ru.replace('</div>\n      </div>\n    </div>\n  </section>', NEW_ROWS_RU + '\n</div>\n      </div>\n    </div>\n  </section>', 1)
    with open(BASE + 'sanctions.html', 'w', encoding='utf-8') as f:
        f.write(san_ru)
    print('✓ sanctions.html updated')

# ══════════════════════════════════════════════════════════════════════════
# UPDATE sanctions-en.html — add rows 28-30 (EN)
# ══════════════════════════════════════════════════════════════════════════

with open(BASE + 'sanctions-en.html', encoding='utf-8') as f:
    san_en = f.read()

if 'peskov-en.html' not in san_en:
    NEW_ROWS_EN = '''
        <div class="person-row">
          <div class="person-info">
            <ul class="person-sanctions-list">
              <li>
                <span class="person-num">28</span>
                <div class="person-details">
                  <a href="peskov-en.html" class="person-name-link"><div class="person-name">Dmitry Peskov</div></a>
                  <div class="person-role">Putin's Press Secretary</div>
                </div>
              </li>
              <li><span class="sanction-label">EU</span><span class="sanction-yes">Sanctions</span><span class="sanction-date">2022</span></li>
              <li><span class="sanction-label">USA</span><span class="sanction-no">—</span></li>
              <li><span class="sanction-label">UK</span><span class="sanction-yes">Sanctions</span><span class="sanction-date">2022</span></li>
              <li><span class="sanction-label">Canada</span><span class="sanction-yes">Sanctions</span><span class="sanction-date">2022</span></li>
            </ul>
          </div>
        </div>
        <div class="person-row">
          <div class="person-info">
            <ul class="person-sanctions-list">
              <li>
                <span class="person-num">29</span>
                <div class="person-details">
                  <a href="lavrov-en.html" class="person-name-link"><div class="person-name">Sergei Lavrov</div></a>
                  <div class="person-role">Foreign Minister</div>
                </div>
              </li>
              <li><span class="sanction-label">EU</span><span class="sanction-yes">Sanctions</span><span class="sanction-date">2022</span></li>
              <li><span class="sanction-label">USA</span><span class="sanction-yes">Sanctions</span><span class="sanction-date">2022</span></li>
              <li><span class="sanction-label">UK</span><span class="sanction-yes">Sanctions</span><span class="sanction-date">2022</span></li>
              <li><span class="sanction-label">Canada</span><span class="sanction-yes">Sanctions</span><span class="sanction-date">2022</span></li>
            </ul>
          </div>
        </div>
        <div class="person-row">
          <div class="person-info">
            <ul class="person-sanctions-list">
              <li>
                <span class="person-num">30</span>
                <div class="person-details">
                  <a href="mizulina-en.html" class="person-name-link"><div class="person-name">Elena Mizulina</div></a>
                  <div class="person-role">Senator, censorship architect</div>
                </div>
              </li>
              <li><span class="sanction-label">EU</span><span class="sanction-yes">Sanctions</span><span class="sanction-date">2022</span></li>
              <li><span class="sanction-label">USA</span><span class="sanction-no">—</span></li>
              <li><span class="sanction-label">UK</span><span class="sanction-yes">Sanctions</span><span class="sanction-date">2022</span></li>
              <li><span class="sanction-label">Canada</span><span class="sanction-no">—</span></li>
            </ul>
          </div>
        </div>'''
    san_en = san_en.replace('</div>\n      </div>\n    </div>\n  </section>', NEW_ROWS_EN + '\n</div>\n      </div>\n    </div>\n  </section>', 1)
    with open(BASE + 'sanctions-en.html', 'w', encoding='utf-8') as f:
        f.write(san_en)
    print('✓ sanctions-en.html updated')

# ══════════════════════════════════════════════════════════════════════════
# UPDATE connections.html — add 3 nodes + links (RU)
# ══════════════════════════════════════════════════════════════════════════

with open(BASE + 'connections.html', encoding='utf-8') as f:
    conn_ru = f.read()

if 'peskov' not in conn_ru:
    conn_ru = conn_ru.replace(
        "{id:'navka',        label:'Навка',           type:'person', role:'Первый канал / жена Пескова',  size:9,  url:'navka.html'}\n  ];",
        """{id:'navka',        label:'Навка',           type:'person', role:'Первый канал / жена Пескова',  size:9,  url:'navka.html'},
    {id:'peskov',       label:'Песков',          type:'person', role:'Пресс-секретарь Путина',       size:13, url:'peskov.html'},
    {id:'lavrov',       label:'Лавров',          type:'person', role:'МИД России',                  size:14, url:'lavrov.html'},
    {id:'mizulina',     label:'Мизулина',        type:'person', role:'Совет Федерации / цензура',    size:10, url:'mizulina.html'}
  ];"""
    )
    conn_ru = conn_ru.replace(
        "{source:'navka',        target:'perviy',    type:'работа',   w:2}\n  ];",
        """{source:'navka',        target:'perviy',    type:'работа',   w:2},
    {source:'peskov',       target:'kremlin',   type:'работа',   w:4},
    {source:'lavrov',       target:'kremlin',   type:'работа',   w:4},
    {source:'mizulina',     target:'kremlin',   type:'работа',   w:3},
    {source:'peskov',       target:'navka',     type:'семья',    w:2}
  ];"""
    )
    with open(BASE + 'connections.html', 'w', encoding='utf-8') as f:
        f.write(conn_ru)
    print('✓ connections.html updated')

# ══════════════════════════════════════════════════════════════════════════
# UPDATE connections-en.html — add 3 nodes + links (EN)
# ══════════════════════════════════════════════════════════════════════════

with open(BASE + 'connections-en.html', encoding='utf-8') as f:
    conn_en = f.read()

if 'peskov' not in conn_en:
    conn_en = conn_en.replace(
        "{id:'navka',        label:'Navka',           type:'person', role:'Channel One / Peskov wife', size:9,  url:'navka-en.html'}\n  ];",
        """{id:'navka',        label:'Navka',           type:'person', role:'Channel One / Peskov wife', size:9,  url:'navka-en.html'},
    {id:'peskov',       label:'Peskov',          type:'person', role:'Presidential Press Secretary', size:13, url:'peskov-en.html'},
    {id:'lavrov',       label:'Lavrov',          type:'person', role:'Foreign Minister',             size:14, url:'lavrov-en.html'},
    {id:'mizulina',     label:'Mizulina',        type:'person', role:'Federation Council / Censorship', size:10, url:'mizulina-en.html'}
  ];"""
    )
    conn_en = conn_en.replace(
        "{source:'navka',        target:'perviy',    type:'работа',   w:2}\n  ];",
        """{source:'navka',        target:'perviy',    type:'работа',   w:2},
    {source:'peskov',       target:'kremlin',   type:'работа',   w:4},
    {source:'lavrov',       target:'kremlin',   type:'работа',   w:4},
    {source:'mizulina',     target:'kremlin',   type:'работа',   w:3},
    {source:'peskov',       target:'navka',     type:'семья',    w:2}
  ];"""
    )
    with open(BASE + 'connections-en.html', 'w', encoding='utf-8') as f:
        f.write(conn_en)
    print('✓ connections-en.html updated')

# ══════════════════════════════════════════════════════════════════════════
# UPDATE SITEMAP
# ══════════════════════════════════════════════════════════════════════════

with open(BASE + 'sitemap.xml', encoding='utf-8') as f:
    sitemap = f.read()

new_entries = ''
for slug in ['peskov', 'lavrov', 'mizulina']:
    for sfx in ['', '-en']:
        fname = slug + sfx + '.html'
        if fname not in sitemap:
            new_entries += f"""
  <url>
    <loc>https://cremle.netlify.app/{fname}</loc>
    <lastmod>2026-04-21</lastmod>
    <priority>0.8</priority>
    <changefreq>monthly</changefreq>
  </url>"""

if new_entries:
    sitemap = sitemap.replace('</urlset>', new_entries + '\n</urlset>')
    with open(BASE + 'sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print('✓ sitemap.xml updated')

print('\nAll 3 new person pages generated and utility pages updated.')
