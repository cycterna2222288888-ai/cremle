#!/usr/bin/env python3
"""
Site upgrade:
1. robots.txt
2. 404.html (RU + EN)
3. OG meta on utility pages (compare, quotes, sanctions, connections)
4. Text search on index.html + index-en.html
5. Quotes filter (JS) on quotes.html + quotes-en.html
6. Sanctions stats bar chart on sanctions.html + sanctions-en.html
7. about.html + about-en.html
8. timeline.html + timeline-en.html
9. Keyboard nav on peskov/lavrov/mizulina pages
"""
import re, os

BASE = '/Users/petrdracev/Desktop/proj/cremle/'

SITE_CSS = """  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500&display=swap');
  :root { --ink:#080808; --paper:#ede8dc; --red:#8b1a1a; --red-dim:#5c1111; --light-gray:#bab3a0; --rule:#1c1c1c; --card-bg:#0e0e0e; }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:var(--ink); color:var(--paper); font-family:'Inter',sans-serif; font-weight:300; line-height:1.75; min-height:100vh; }
  .topbar { padding:14px 60px; border-bottom:1px solid var(--rule); background:var(--ink); display:flex; justify-content:space-between; align-items:center; }
  .topbar a { font-size:10px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); text-decoration:none; }
  .topbar a:hover { opacity:0.6; }
  .footer { padding:48px 60px; display:flex; justify-content:space-between; align-items:center; font-size:11px; letter-spacing:0.15em; text-transform:uppercase; color:#333; border-top:1px solid var(--rule); }
  @media(max-width:768px){ .topbar { padding:12px 20px; } .footer { padding:32px 20px; flex-direction:column; gap:12px; } }"""

# ── 1. ROBOTS.TXT ─────────────────────────────────────────────────────────
robots = """User-agent: *
Allow: /

Sitemap: https://cycterna2222288888-ai.github.io/cremle/sitemap.xml
"""
with open(BASE + 'robots.txt', 'w') as f:
    f.write(robots)
print('✓ robots.txt')

# ── 2. 404.HTML ───────────────────────────────────────────────────────────
page_404 = """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>404 — Страница не найдена · Голоса Кремля</title>
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700&family=Inter:wght@300;400&display=swap');
  :root { --ink:#080808; --paper:#ede8dc; --red:#8b1a1a; --rule:#1c1c1c; }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:var(--ink); color:var(--paper); font-family:'Inter',sans-serif; font-weight:300; min-height:100vh; display:flex; flex-direction:column; }
  .topbar { padding:14px 60px; border-bottom:1px solid var(--rule); display:flex; justify-content:space-between; align-items:center; }
  .topbar a { font-size:10px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); text-decoration:none; }
  .center { flex:1; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:80px 40px; text-align:center; }
  .num { font-family:'Playfair Display',serif; font-size:clamp(6rem,20vw,14rem); font-weight:700; color:#1c1c1c; line-height:1; }
  .msg { font-family:'Playfair Display',serif; font-size:clamp(1.2rem,3vw,2rem); color:var(--paper); margin:24px 0; }
  .sub { font-size:13px; color:#555; max-width:400px; line-height:1.8; margin-bottom:40px; }
  .btn { font-size:10px; letter-spacing:0.25em; text-transform:uppercase; text-decoration:none; color:var(--paper); border:1px solid #333; padding:14px 28px; transition:all 0.2s; }
  .btn:hover { border-color:var(--red); color:var(--red); }
  .footer { padding:32px 60px; border-top:1px solid var(--rule); font-size:11px; letter-spacing:0.15em; text-transform:uppercase; color:#333; text-align:center; }
  @media(max-width:768px){ .topbar { padding:12px 20px; } }
</style>
</head>
<body>
<div class="topbar">
  <a href="index.html">← Голоса Кремля</a>
</div>
<div class="center">
  <div class="num">404</div>
  <div class="msg">Страница не найдена</div>
  <p class="sub">Возможно, досье было перемещено или ещё не создано. Вернитесь к списку всех материалов.</p>
  <a href="index.html" class="btn">← Все досье</a>
</div>
<div class="footer">Голоса Кремля · Архив пропаганды</div>
</body>
</html>"""

with open(BASE + '404.html', 'w', encoding='utf-8') as f:
    f.write(page_404)
print('✓ 404.html')

# ── 3. OG META ON UTILITY PAGES ──────────────────────────────────────────
UTIL_OG = {
    'compare.html': ('Сравнить пропагандистов — Голоса Кремля',
        'Сравните двух пропагандистов по биографии, методам, санкциям и цитатам.'),
    'compare-en.html': ('Compare Propagandists — Kremlin Voices',
        'Compare two propagandists side by side: biography, method, sanctions, quotes.'),
    'quotes.html': ('Цитаты — Голоса Кремля',
        'Прямые цитаты российских пропагандистов: угрозы, ложь, оправдание войны.'),
    'quotes-en.html': ('Quotes — Kremlin Voices',
        'Direct quotes from Russian propagandists: threats, lies, war justifications.'),
    'sanctions.html': ('Санкции — Голоса Кремля',
        'Кто из российских пропагандистов попал под санкции ЕС, США, Великобритании и Канады.'),
    'sanctions-en.html': ('Sanctions — Kremlin Voices',
        'Which Russian propagandists are sanctioned by the EU, USA, UK and Canada.'),
    'connections.html': ('Связи — Голоса Кремля',
        'Граф связей: кто с кем работает и влияет в медиапространстве Кремля.'),
    'connections-en.html': ('Connections — Kremlin Voices',
        'Network graph: who works with and influences whom in the Kremlin media ecosystem.'),
}

og_fixed = 0
for fname, (title, desc) in UTIL_OG.items():
    path = BASE + fname
    if not os.path.exists(path): continue
    with open(path, encoding='utf-8') as f:
        html = f.read()

    OG_BLOCK = f"""<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="https://cycterna2222288888-ai.github.io/cremle/og-image.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">"""

    if 'og:title' not in html:
        html = html.replace('</head>', OG_BLOCK + '\n</head>', 1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        og_fixed += 1

print(f'✓ OG meta added to {og_fixed} utility pages')

# ── 4. TEXT SEARCH ON INDEX PAGES ────────────────────────────────────────
SEARCH_CSS = """
  .search-bar { padding:20px 60px 0; }
  .search-input { width:100%; max-width:500px; background:#0e0e0e; border:1px solid #222; color:var(--paper); font-family:'Inter',sans-serif; font-size:13px; font-weight:300; padding:12px 18px; outline:none; transition:border 0.2s; }
  .search-input::placeholder { color:#444; }
  .search-input:focus { border-color:#555; }
  .search-empty { display:none; padding:60px; font-size:13px; color:#444; letter-spacing:0.1em; }
  @media(max-width:768px){ .search-bar { padding:16px 20px 0; } }"""

SEARCH_JS_RU = """<script>
(function(){
  var inp = document.getElementById('card-search');
  if (!inp) return;
  var empty = document.getElementById('search-empty');
  inp.addEventListener('input', function(){
    var q = this.value.trim().toLowerCase();
    var cards = document.querySelectorAll('.card');
    var visible = 0;
    cards.forEach(function(c){
      var name = (c.querySelector('.card-name')||{}).textContent||'';
      var role = (c.querySelector('.card-title')||{}).textContent||'';
      var match = !q || name.toLowerCase().includes(q) || role.toLowerCase().includes(q);
      c.style.display = match ? '' : 'none';
      if (match) visible++;
    });
    if (empty) empty.style.display = visible === 0 ? 'block' : 'none';
  });
})();
</script>"""

SEARCH_JS_EN = """<script>
(function(){
  var inp = document.getElementById('card-search');
  if (!inp) return;
  var empty = document.getElementById('search-empty');
  inp.addEventListener('input', function(){
    var q = this.value.trim().toLowerCase();
    var cards = document.querySelectorAll('.card');
    var visible = 0;
    cards.forEach(function(c){
      var name = (c.querySelector('.card-name')||{}).textContent||'';
      var role = (c.querySelector('.card-title')||{}).textContent||'';
      var match = !q || name.toLowerCase().includes(q) || role.toLowerCase().includes(q);
      c.style.display = match ? '' : 'none';
      if (match) visible++;
    });
    if (empty) empty.style.display = visible === 0 ? 'block' : 'none';
  });
})();
</script>"""

for fname, js, ph in [
    ('index.html', SEARCH_JS_RU, 'Поиск по имени или описанию…'),
    ('index-en.html', SEARCH_JS_EN, 'Search by name or description…'),
]:
    path = BASE + fname
    with open(path, encoding='utf-8') as f:
        html = f.read()

    if 'card-search' not in html:
        html = html.replace('</style>', SEARCH_CSS + '\n</style>', 1)
        # Insert search bar before first card appearance
        html = html.replace(
            '<div id="search-empty"', 'SKIP'
        )
        # Add search input before the cards grid
        html = re.sub(
            r'(<div[^>]*class="[^"]*cards[^"]*"[^>]*>)',
            r'<div class="search-bar"><input class="search-input" id="card-search" type="text" placeholder="' + ph + r'" autocomplete="off"></div><div id="search-empty" class="search-empty">' + ('Ничего не найдено' if 'RU' in fname or fname == 'index.html' else 'No results found') + r'</div>\1',
            html, count=1
        )
        html = html.replace('</body>', js + '</body>')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'✓ Search added: {fname}')

# ── 5. QUOTES FILTER ──────────────────────────────────────────────────────
QUOTES_FILTER_CSS = """
  .quotes-filter { padding:0 60px 40px; display:flex; gap:16px; align-items:center; flex-wrap:wrap; }
  .qf-label { font-size:10px; letter-spacing:0.25em; text-transform:uppercase; color:#444; }
  .qf-select { background:#0e0e0e; border:1px solid #222; color:var(--paper); font-family:'Inter',sans-serif; font-size:11px; font-weight:300; padding:8px 14px; outline:none; cursor:pointer; }
  .qf-select:focus { border-color:#555; }
  .qf-input { background:#0e0e0e; border:1px solid #222; color:var(--paper); font-family:'Inter',sans-serif; font-size:11px; padding:8px 14px; outline:none; width:200px; }
  .qf-input::placeholder { color:#444; }
  @media(max-width:768px){ .quotes-filter { padding:0 20px 32px; } .qf-input { width:140px; } }"""

QUOTES_FILTER_JS = """<script>
(function(){
  var sel = document.getElementById('qf-person');
  var inp = document.getElementById('qf-text');
  function filter(){
    var person = sel ? sel.value : '';
    var text = inp ? inp.value.trim().toLowerCase() : '';
    document.querySelectorAll('.quote-card').forEach(function(card){
      var pname = (card.querySelector('.qc-person')||{}).textContent||'';
      var qtext = (card.querySelector('.quote-text')||{}).textContent||'';
      var qdate = (card.querySelector('.qc-date')||{}).textContent||'';
      var matchP = !person || pname.trim() === person;
      var matchT = !text || qtext.toLowerCase().includes(text) || qdate.toLowerCase().includes(text);
      card.style.display = (matchP && matchT) ? '' : 'none';
    });
  }
  if (sel) sel.addEventListener('change', filter);
  if (inp) inp.addEventListener('input', filter);
})();
</script>"""

for fname, label_all, label_filter, placeholder in [
    ('quotes.html', 'Все', 'Фильтр по персоне', 'Поиск по тексту…'),
    ('quotes-en.html', 'All', 'Filter by person', 'Search text…'),
]:
    path = BASE + fname
    with open(path, encoding='utf-8') as f:
        html = f.read()
    if 'qf-person' not in html:
        # Collect all person names from qc-person links
        names = re.findall(r'class="qc-person"><a[^>]*>([^<]+)</a>', html)
        names = sorted(set(names))
        options = f'<option value="">{label_all}</option>' + ''.join(
            f'<option value="{n}">{n}</option>' for n in names
        )
        filter_html = (
            f'<div class="quotes-filter">'
            f'<span class="qf-label">{label_filter}</span>'
            f'<select class="qf-select" id="qf-person">{options}</select>'
            f'<input class="qf-input" id="qf-text" type="text" placeholder="{placeholder}" autocomplete="off">'
            f'</div>\n'
        )
        html = html.replace('</style>', QUOTES_FILTER_CSS + '\n</style>', 1)
        # Insert filter before the first quote-section or quotes-grid
        html = re.sub(
            r'(<div[^>]*class="[^"]*quote[s]?[- ](?:section|grid)[^"]*")',
            filter_html + r'\1',
            html, count=1
        )
        html = html.replace('</body>', QUOTES_FILTER_JS + '</body>')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'✓ Quotes filter: {fname}')

# ── 6. SANCTIONS STATS BAR CHART ─────────────────────────────────────────
SANCTIONS_DATA = {
    'solovyov':     {'eu':1,'us':1,'uk':1,'ca':1},
    'skabeeva':     {'eu':1,'us':0,'uk':1,'ca':0},
    'simonyan':     {'eu':1,'us':1,'uk':1,'ca':1},
    'kiselyov':     {'eu':1,'us':1,'uk':1,'ca':1},
    'popov':        {'eu':1,'us':0,'uk':1,'ca':0},
    'sheynin':      {'eu':1,'us':0,'uk':0,'ca':0},
    'tolstoy':      {'eu':1,'us':0,'uk':1,'ca':0},
    'norkin':       {'eu':1,'us':0,'uk':0,'ca':0},
    'keosayan':     {'eu':1,'us':0,'uk':0,'ca':0},
    'andreyeva':    {'eu':1,'us':0,'uk':0,'ca':0},
    'leontyev':     {'eu':1,'us':0,'uk':1,'ca':0},
    'mamontov':     {'eu':1,'us':0,'uk':1,'ca':0},
    'medinsky':     {'eu':1,'us':0,'uk':1,'ca':0},
    'prilepin':     {'eu':1,'us':0,'uk':1,'ca':0},
    'dugin':        {'eu':1,'us':1,'uk':1,'ca':1},
    'mikhalkov':    {'eu':1,'us':0,'uk':0,'ca':0},
    'korchevnikov': {'eu':1,'us':0,'uk':0,'ca':0},
    'krasovsky':    {'eu':1,'us':0,'uk':0,'ca':0},
    'medvedev':     {'eu':1,'us':1,'uk':1,'ca':1},
    'kadyrov':      {'eu':1,'us':1,'uk':1,'ca':1},
    'malofeev':     {'eu':1,'us':1,'uk':1,'ca':1},
    'nikonov':      {'eu':1,'us':0,'uk':1,'ca':0},
    'poddubny':     {'eu':1,'us':0,'uk':1,'ca':0},
    'zakharova':    {'eu':1,'us':0,'uk':1,'ca':1},
    'kovalchuk':    {'eu':1,'us':1,'uk':1,'ca':1},
    'turchak':      {'eu':1,'us':1,'uk':1,'ca':0},
    'navka':        {'eu':1,'us':0,'uk':0,'ca':0},
    'peskov':       {'eu':1,'us':0,'uk':1,'ca':1},
    'lavrov':       {'eu':1,'us':1,'uk':1,'ca':1},
    'mizulina':     {'eu':1,'us':0,'uk':1,'ca':0},
}

total = len(SANCTIONS_DATA)
eu_n = sum(v['eu'] for v in SANCTIONS_DATA.values())
us_n = sum(v['us'] for v in SANCTIONS_DATA.values())
uk_n = sum(v['uk'] for v in SANCTIONS_DATA.values())
ca_n = sum(v['ca'] for v in SANCTIONS_DATA.values())

def pct(n, t=total): return round(n/t*100)

CHART_CSS = """
  .sanction-stats { padding:40px 60px; border-bottom:1px solid var(--rule); }
  .ss-title { font-size:10px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); margin-bottom:28px; }
  .ss-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:2px; }
  .ss-cell { background:var(--card-bg); padding:24px 20px; }
  .ss-country { font-size:9px; letter-spacing:0.25em; text-transform:uppercase; color:#555; margin-bottom:8px; }
  .ss-count { font-family:'Playfair Display',serif; font-size:2rem; color:var(--paper); line-height:1; margin-bottom:10px; }
  .ss-bar-bg { background:#111; height:3px; margin-bottom:6px; }
  .ss-bar { height:3px; background:var(--red); transition:width 0.6s; }
  .ss-pct { font-size:10px; color:#444; }
  @media(max-width:768px){ .sanction-stats { padding:32px 20px; } .ss-grid { grid-template-columns:repeat(2,1fr); } }"""

def make_chart_html(ru=True):
    label = 'Охват санкциями' if ru else 'Sanctions coverage'
    of_label = f'из {total}' if ru else f'of {total}'
    return f"""<div class="sanction-stats">
  <div class="ss-title">{label}</div>
  <div class="ss-grid">
    <div class="ss-cell">
      <div class="ss-country">Европейский союз</div>
      <div class="ss-count">{eu_n}</div>
      <div class="ss-bar-bg"><div class="ss-bar" style="width:{pct(eu_n)}%"></div></div>
      <div class="ss-pct">{pct(eu_n)}% · {of_label}</div>
    </div>
    <div class="ss-cell">
      <div class="ss-country">{'США' if ru else 'USA'}</div>
      <div class="ss-count">{us_n}</div>
      <div class="ss-bar-bg"><div class="ss-bar" style="width:{pct(us_n)}%"></div></div>
      <div class="ss-pct">{pct(us_n)}% · {of_label}</div>
    </div>
    <div class="ss-cell">
      <div class="ss-country">{'Великобритания' if ru else 'United Kingdom'}</div>
      <div class="ss-count">{uk_n}</div>
      <div class="ss-bar-bg"><div class="ss-bar" style="width:{pct(uk_n)}%"></div></div>
      <div class="ss-pct">{pct(uk_n)}% · {of_label}</div>
    </div>
    <div class="ss-cell">
      <div class="ss-country">{'Канада' if ru else 'Canada'}</div>
      <div class="ss-count">{ca_n}</div>
      <div class="ss-bar-bg"><div class="ss-bar" style="width:{pct(ca_n)}%"></div></div>
      <div class="ss-pct">{pct(ca_n)}% · {of_label}</div>
    </div>
  </div>
</div>"""

for fname, ru in [('sanctions.html', True), ('sanctions-en.html', False)]:
    path = BASE + fname
    if not os.path.exists(path): continue
    with open(path, encoding='utf-8') as f:
        html = f.read()
    if 'sanction-stats' not in html:
        html = html.replace('</style>', CHART_CSS + '\n</style>', 1)
        # Insert chart after opening section tag
        html = re.sub(r'(<section[^>]*>)', r'\1\n' + make_chart_html(ru), html, count=1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'✓ Sanctions chart: {fname}')

# ── 7. ABOUT.HTML + ABOUT-EN.HTML ─────────────────────────────────────────
ABOUT_CSS = """
  .about-hero { padding:80px 60px; border-bottom:1px solid var(--rule); max-width:760px; }
  .about-eyebrow { font-size:10px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); margin-bottom:24px; }
  .about-title { font-family:'Playfair Display',serif; font-size:clamp(2rem,4vw,3.5rem); font-weight:400; line-height:1.1; margin-bottom:32px; }
  .about-lead { font-size:16px; color:#bab3a0; line-height:1.9; }
  .about-section { padding:60px 60px; border-bottom:1px solid var(--rule); max-width:760px; }
  .about-section h2 { font-family:'Playfair Display',serif; font-size:1.4rem; font-weight:400; margin-bottom:24px; color:var(--paper); }
  .about-section p { font-size:14px; color:#888; line-height:1.9; margin-bottom:16px; }
  .about-section p:last-child { margin-bottom:0; }
  .badge-demo { display:inline-block; font-size:9px; font-family:'Inter',sans-serif; font-weight:500; letter-spacing:0.15em; text-transform:uppercase; padding:2px 7px; border-radius:2px; vertical-align:middle; margin:0 4px; cursor:default; }
  .badge-fact-d { background:#0a2010; color:#4caf50; border:1px solid #1a4a1a; }
  .badge-interp-d { background:#1a1200; color:#e67e22; border:1px solid #3a2800; }
  .about-grid { display:grid; grid-template-columns:1fr 1fr; gap:2px; background:var(--rule); margin-top:28px; }
  .about-card { background:var(--card-bg); padding:28px; }
  .about-card-title { font-size:12px; letter-spacing:0.15em; text-transform:uppercase; color:var(--red); margin-bottom:10px; }
  .about-card-text { font-size:13px; color:#666; line-height:1.8; }
  .about-contact { padding:60px 60px; }
  .about-contact h2 { font-family:'Playfair Display',serif; font-size:1.4rem; font-weight:400; margin-bottom:20px; }
  .about-contact p { font-size:14px; color:#888; line-height:1.9; }
  @media(max-width:768px){
    .about-hero, .about-section, .about-contact { padding:48px 24px; }
    .about-grid { grid-template-columns:1fr; }
  }"""

about_ru = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>О проекте — Голоса Кремля</title>
<meta name="description" content="Голоса Кремля: методология, источники, о проекте.">
<meta property="og:title" content="О проекте — Голоса Кремля">
<meta property="og:description" content="Независимый архив пропаганды: методология, источники, принципы работы.">
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="canonical" href="https://cycterna2222288888-ai.github.io/cremle/about.html">
<link rel="alternate" hreflang="ru" href="about.html">
<link rel="alternate" hreflang="en" href="about-en.html">
<style>
{ABOUT_CSS}
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700&family=Inter:wght@300;400;500&display=swap');
  :root {{ --ink:#080808; --paper:#ede8dc; --red:#8b1a1a; --rule:#1c1c1c; --card-bg:#0e0e0e; --light-gray:#bab3a0; }}
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ background:var(--ink); color:var(--paper); font-family:'Inter',sans-serif; font-weight:300; line-height:1.75; }}
  .topbar {{ padding:14px 60px; border-bottom:1px solid var(--rule); display:flex; justify-content:space-between; align-items:center; }}
  .topbar-left a {{ font-size:10px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); text-decoration:none; }}
  .topbar-right {{ display:flex; gap:16px; }}
  .topbar-right a {{ font-size:9px; letter-spacing:0.2em; text-transform:uppercase; color:#555; text-decoration:none; }}
  .topbar-right a:hover {{ color:var(--paper); }}
  .footer {{ padding:48px 60px; border-top:1px solid var(--rule); display:flex; justify-content:space-between; font-size:11px; letter-spacing:0.15em; text-transform:uppercase; color:#333; }}
  @media(max-width:768px){{ .topbar {{ padding:12px 20px; }} .footer {{ padding:32px 20px; flex-direction:column; gap:12px; }} }}
</style>
</head>
<body>
<div class="topbar">
  <div class="topbar-left"><a href="index.html">← Все досье</a></div>
  <div class="topbar-right">
    <a href="about.html">RU</a>
    <a href="about-en.html">EN</a>
  </div>
</div>

<div class="about-hero">
  <div class="about-eyebrow">О проекте · 2025</div>
  <h1 class="about-title">Голоса Кремля — независимый архив пропаганды</h1>
  <p class="about-lead">Этот проект документирует биографии, методы и высказывания людей, формирующих пропагандистский нарратив Кремля — для журналистов, исследователей и всех, кто хочет понять, как работает государственная дезинформация.</p>
</div>

<div class="about-section">
  <h2>Методология</h2>
  <p>Все материалы составлены на основе открытых публичных источников: официальных санкционных реестров, архивов государственных СМИ, публикаций WikiLeaks, материалов Meduza, Reuters, BBC, The Guardian и других независимых изданий.</p>
  <p>Каждый факт в досье отмечен одним из двух маркеров:</p>
  <p>
    <span class="badge-demo badge-fact-d">Факт</span> — утверждение имеет прямой первичный источник (санкционный реестр, официальный документ, видеозапись).
  </p>
  <p>
    <span class="badge-demo badge-interp-d">Интерпр.</span> — авторская оценка задокументированных событий. Указывает на редакционный вывод, а не проверяемый факт.
  </p>
</div>

<div class="about-section">
  <h2>Критерии включения</h2>
  <div class="about-grid">
    <div class="about-card">
      <div class="about-card-title">Активность</div>
      <div class="about-card-text">Персонаж активно участвует в формировании государственного нарратива через СМИ, политику или публичные высказывания.</div>
    </div>
    <div class="about-card">
      <div class="about-card-title">Документация</div>
      <div class="about-card-text">Деятельность задокументирована в открытых источниках — санкционных реестрах, архивах СМИ, официальных записях.</div>
    </div>
    <div class="about-card">
      <div class="about-card-title">Влияние</div>
      <div class="about-card-text">Персонаж оказывает значимое влияние на аудиторию или формирование информационной политики государства.</div>
    </div>
    <div class="about-card">
      <div class="about-card-title">Верифицируемость</div>
      <div class="about-card-text">Все ключевые факты могут быть проверены по первичным источникам, указанным в разделе «Источники» каждого досье.</div>
    </div>
  </div>
</div>

<div class="about-section">
  <h2>Что этот проект не делает</h2>
  <p>Проект не призывает к насилию, не занимается слежкой за частной жизнью и не публикует персональные данные, не находящиеся в публичном доступе. Все досье составлены на основе публичных действий и высказываний.</p>
  <p>Проект не является аффилированным ни с одной политической партией, государством или организацией. Все оценки — редакционные, а не судебные.</p>
</div>

<div class="about-contact">
  <h2>Связаться · Сообщить об ошибке</h2>
  <p>Если вы обнаружили фактическую ошибку, неточность или хотите предложить новый материал, воспользуйтесь <a href="submit.html" style="color:var(--red)">формой обратной связи</a>.</p>
</div>

<div class="footer">
  <span>Голоса Кремля · 2025</span>
  <span>Независимый архив · Открытые источники</span>
</div>
</body>
</html>"""

about_en = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>About — Kremlin Voices</title>
<meta name="description" content="Kremlin Voices: methodology, sources, about the project.">
<meta property="og:title" content="About — Kremlin Voices">
<meta property="og:description" content="An independent propaganda archive: methodology, sources, editorial principles.">
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="canonical" href="https://cycterna2222288888-ai.github.io/cremle/about-en.html">
<link rel="alternate" hreflang="ru" href="about.html">
<link rel="alternate" hreflang="en" href="about-en.html">
<style>
{ABOUT_CSS}
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700&family=Inter:wght@300;400;500&display=swap');
  :root {{ --ink:#080808; --paper:#ede8dc; --red:#8b1a1a; --rule:#1c1c1c; --card-bg:#0e0e0e; --light-gray:#bab3a0; }}
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ background:var(--ink); color:var(--paper); font-family:'Inter',sans-serif; font-weight:300; line-height:1.75; }}
  .topbar {{ padding:14px 60px; border-bottom:1px solid var(--rule); display:flex; justify-content:space-between; align-items:center; }}
  .topbar-left a {{ font-size:10px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); text-decoration:none; }}
  .topbar-right {{ display:flex; gap:16px; }}
  .topbar-right a {{ font-size:9px; letter-spacing:0.2em; text-transform:uppercase; color:#555; text-decoration:none; }}
  .topbar-right a:hover {{ color:var(--paper); }}
  .footer {{ padding:48px 60px; border-top:1px solid var(--rule); display:flex; justify-content:space-between; font-size:11px; letter-spacing:0.15em; text-transform:uppercase; color:#333; }}
  @media(max-width:768px){{ .topbar {{ padding:12px 20px; }} .footer {{ padding:32px 20px; flex-direction:column; gap:12px; }} }}
</style>
</head>
<body>
<div class="topbar">
  <div class="topbar-left"><a href="index-en.html">← All dossiers</a></div>
  <div class="topbar-right">
    <a href="about.html">RU</a>
    <a href="about-en.html">EN</a>
  </div>
</div>

<div class="about-hero">
  <div class="about-eyebrow">About · 2025</div>
  <h1 class="about-title">Kremlin Voices — an independent propaganda archive</h1>
  <p class="about-lead">This project documents the biographies, methods, and statements of individuals who shape the Kremlin's propaganda narrative — for journalists, researchers, and anyone seeking to understand how state disinformation operates.</p>
</div>

<div class="about-section">
  <h2>Methodology</h2>
  <p>All content is compiled from open public sources: official sanctions registries, state media archives, Meduza, Reuters, BBC, The Guardian and other independent publications.</p>
  <p>Each claim in every dossier carries one of two markers:</p>
  <p>
    <span class="badge-demo badge-fact-d">Fact</span> — the claim has a direct primary source (sanctions registry, official document, video recording).
  </p>
  <p>
    <span class="badge-demo badge-interp-d">Interp.</span> — an editorial assessment of documented events. This indicates a reasoned conclusion, not a verified fact.
  </p>
</div>

<div class="about-section">
  <h2>Inclusion criteria</h2>
  <div class="about-grid">
    <div class="about-card">
      <div class="about-card-title">Activity</div>
      <div class="about-card-text">The subject actively participates in shaping state narrative through media, politics, or sustained public statements.</div>
    </div>
    <div class="about-card">
      <div class="about-card-title">Documentation</div>
      <div class="about-card-text">Their activity is documented in open sources — sanctions registries, media archives, official records.</div>
    </div>
    <div class="about-card">
      <div class="about-card-title">Influence</div>
      <div class="about-card-text">The subject has meaningful reach over audiences or significant influence over state information policy.</div>
    </div>
    <div class="about-card">
      <div class="about-card-title">Verifiability</div>
      <div class="about-card-text">All key claims can be verified via primary sources listed in each dossier's Sources section.</div>
    </div>
  </div>
</div>

<div class="about-section">
  <h2>What this project does not do</h2>
  <p>This project does not incite violence, does not surveil private lives, and does not publish personal data not already in the public domain. All dossiers are based on public actions and statements.</p>
  <p>This project is not affiliated with any political party, government, or organization. All assessments are editorial, not judicial.</p>
</div>

<div class="about-contact">
  <h2>Contact · Report an error</h2>
  <p>If you find a factual error, inaccuracy, or want to submit new material, use the <a href="submit-en.html" style="color:var(--red)">feedback form</a>.</p>
</div>

<div class="footer">
  <span>Kremlin Voices · 2025</span>
  <span>Independent Archive · Open Sources</span>
</div>
</body>
</html>"""

with open(BASE + 'about.html', 'w', encoding='utf-8') as f:
    f.write(about_ru)
with open(BASE + 'about-en.html', 'w', encoding='utf-8') as f:
    f.write(about_en)
print('✓ about.html + about-en.html')

# ── 8. TIMELINE.HTML + TIMELINE-EN.HTML ───────────────────────────────────
TIMELINE_EVENTS_RU = [
    ('1990–1999', 'Банк «Россия» и кооператив «Озеро»', 'Ковальчук и Путин основывают банк «Россия». Формируется ядро будущего путинского окружения. Симоньян и Соловьёв начинают карьеры в журналистике.'),
    ('1999', 'Путин приходит к власти', 'ФСБ под руководством Патрушева переходит к Путину. Начинается выстраивание медиапространства под государственный контроль. Соловьёв появляется на федеральных каналах.'),
    ('2000–2003', 'Первые зачистки медиа', 'НТВ переходит под «Газпром». Киселёв остаётся — переходит в государственный лагерь. Начало системного вытеснения независимых СМИ с рынка.'),
    ('2004', 'Лавров — министр иностранных дел', 'Назначен министром. Меняет тональность российской дипломатии: от «адаптации к Западу» к концепции «суверенного пространства». Мизулина избрана в Думу.'),
    ('2005', 'RT (Russia Today) — запуск', 'Симоньян возглавляет RT. Первый иностранноязычный пропагандистский канал Кремля. Декларируется как «альтернативная точка зрения».'),
    ('2008', 'Война в Грузии', 'Первая информационная война нового типа. Соловьёв, Киселёв, Симоньян оправдывают операцию. Патрушев становится секретарём Совета Безопасности. Ковальчук создаёт National Media Group.'),
    ('2012', 'Третий срок Путина и протесты', 'Волна протестов на Болотной площади. Медведев и Шейнин усиливают пропаганду. Песков становится официальным пресс-секретарём. Начинается ужесточение законодательства.'),
    ('2013', 'Закон о «гей-пропаганде»', 'Мизулина проводит закон через Думу. Прецедент: политическая репрессия через «семейные ценности». Медведев публично поддерживает. Международное осуждение.'),
    ('2014', 'Крым и Донбасс', 'Первая волна персональных санкций. Кисилёв угрожает «радиоактивным пеплом». Захарова усиливает риторику. Ковальчук попадает под санкции США. Навка поддерживает аннексию публично.'),
    ('2015', 'Захарова — пресс-секретарь МИД', 'Первая женщина на этом посту. Сразу превращает брифинги в медиа-шоу. RT расширяется на французский рынок. Прилепин создаёт батальон «Сибирь».'),
    ('2017', 'RT признан «иностранным агентом» в США', 'Симоньян использует это как нарратив о «преследовании». Небензя сменяет Чуркина в Совете Безопасности ООН. Тurchак возглавляет аппарат «Единой России».'),
    ('2022', '24 февраля — вторжение', 'Все персонажи архива переходят в режим тотальной пропаганды. Соловьёв угрожает ядерной войной. Захарова называет это «денацификацией». Песков говорит «специальная военная операция». Введены массовые санкции ЕС, США, UK, Канады.'),
    ('2022', 'Санкционная волна', 'Более 25 персонажей досье попадают под персональные санкции. Активы заморожены. Въезд в ЕС и Великобританию запрещён. Пропаганда не прекращается.'),
    ('2022–2025', 'Информационная война продолжается', 'Кисилёв, Соловьёв, Скабеева ведут эфиры ежедневно. Медведев в Telegram угрожает ядерным оружием. Мизулина и Слуцкий продвигают закон о «дискредитации армии». Небензя ветирует резолюции ООН.'),
]

TIMELINE_EVENTS_EN = [
    ('1990–1999', 'Bank Rossiya and the Ozero Cooperative', 'Kovalchuk and Putin co-found Bank Rossiya. The nucleus of Putin\'s inner circle takes shape. Simonyan and Solovyov begin careers in journalism.'),
    ('1999', 'Putin comes to power', 'The FSB under Patrushev passes to Putin. Systematic shaping of media under state control begins. Solovyov appears on federal channels.'),
    ('2000–2003', 'First media purges', 'NTV transfers to Gazprom. Kiselyov stays — switches to the state camp. Independent media are systematically squeezed out of the market.'),
    ('2004', 'Lavrov — Foreign Minister', 'Appointed minister. Shifts the tone of Russian diplomacy from "adaptation to the West" to a concept of "sovereign space." Mizulina elected to the Duma.'),
    ('2005', 'RT (Russia Today) launches', 'Simonyan heads RT. The Kremlin\'s first foreign-language propaganda channel. Declared as an "alternative point of view."'),
    ('2008', 'War in Georgia', 'First information war of the new type. Solovyov, Kiselyov, Simonyan justify the operation. Patrushev becomes Security Council Secretary. Kovalchuk creates National Media Group.'),
    ('2012', 'Putin\'s third term and protests', 'Wave of protests at Bolotnaya Square. Medvedev and Sheynin intensify propaganda. Peskov becomes official press secretary. Legislation begins to tighten.'),
    ('2013', 'The anti-LGBT "propaganda" law', 'Mizulina steers the law through the Duma. Precedent: political repression through "family values." Medvedev publicly endorses it. International condemnation follows.'),
    ('2014', 'Crimea and Donbas', 'First wave of personal sanctions. Kiselyov threatens "radioactive ash." Zakharova sharpens the rhetoric. Kovalchuk sanctioned by the USA. Navka publicly supports annexation.'),
    ('2015', 'Zakharova — MFA spokesperson', 'First woman in the role. Immediately turns briefings into media theatre. RT expands to the French-language market. Prilepin forms the "Siberia" battalion.'),
    ('2017', 'RT designated "foreign agent" in the USA', 'Simonyan uses this as a "persecution" narrative. Nebenzya replaces Churkin at the UN Security Council. Turchak takes over the United Russia party apparatus.'),
    ('2022', 'February 24 — invasion', 'All subjects of the archive shift to total propaganda mode. Solovyov threatens nuclear war. Zakharova calls it "denazification." Peskov says "special military operation." Mass EU, USA, UK, Canada sanctions imposed.'),
    ('2022', 'Sanctions wave', 'More than 25 subjects designated under personal sanctions. Assets frozen. Entry to EU and UK banned. Propaganda does not stop.'),
    ('2022–2025', 'Information war continues', 'Kiselyov, Solovyov, Skabeeva broadcast daily. Medvedev threatens with nuclear weapons on Telegram. Mizulina and Slutsky push the "army discreditation" law. Nebenzya vetoes UN resolutions.'),
]

TL_CSS = """
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700&family=Inter:wght@300;400;500&display=swap');
  :root { --ink:#080808; --paper:#ede8dc; --red:#8b1a1a; --rule:#1c1c1c; --card-bg:#0e0e0e; }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:var(--ink); color:var(--paper); font-family:'Inter',sans-serif; font-weight:300; line-height:1.75; }
  .topbar { padding:14px 60px; border-bottom:1px solid var(--rule); display:flex; justify-content:space-between; align-items:center; }
  .topbar-left a { font-size:10px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); text-decoration:none; }
  .topbar-right { display:flex; gap:16px; }
  .topbar-right a { font-size:9px; letter-spacing:0.2em; text-transform:uppercase; color:#555; text-decoration:none; }
  .topbar-right a:hover { color:var(--paper); }
  .tl-hero { padding:80px 60px; border-bottom:1px solid var(--rule); max-width:760px; }
  .tl-eyebrow { font-size:10px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); margin-bottom:24px; }
  .tl-title { font-family:'Playfair Display',serif; font-size:clamp(2rem,4vw,3rem); font-weight:400; line-height:1.1; }
  .tl-body { max-width:760px; margin:0 auto; padding:0 60px 80px; }
  .tl-entry { display:grid; grid-template-columns:100px 1fr; gap:32px; padding:36px 0; border-bottom:1px solid #0f0f0f; }
  .tl-year { font-size:11px; letter-spacing:0.2em; color:var(--red); padding-top:4px; }
  .tl-content h3 { font-size:14px; letter-spacing:0.05em; margin-bottom:10px; color:var(--paper); }
  .tl-content p { font-size:14px; color:#666; line-height:1.9; }
  .footer { padding:48px 60px; border-top:1px solid var(--rule); display:flex; justify-content:space-between; font-size:11px; letter-spacing:0.15em; text-transform:uppercase; color:#333; }
  @media(max-width:768px){ .topbar { padding:12px 20px; } .tl-hero, .tl-body { padding:48px 20px; } .tl-entry { grid-template-columns:70px 1fr; gap:16px; } .footer { padding:32px 20px; flex-direction:column; gap:12px; } }"""

def make_timeline_page(events, lang='ru'):
    title_ru = 'Хронология · Голоса Кремля'
    title_en = 'Timeline · Kremlin Voices'
    title = title_ru if lang == 'ru' else title_en
    eyebrow = 'Хронология' if lang == 'ru' else 'Timeline'
    heading = 'Ключевые события 1999–2025' if lang == 'ru' else 'Key Events 1999–2025'
    back = '← Все досье' if lang == 'ru' else '← All dossiers'
    back_href = 'index.html' if lang == 'ru' else 'index-en.html'
    alt_href = 'timeline-en.html' if lang == 'ru' else 'timeline.html'
    alt_label = 'EN' if lang == 'ru' else 'RU'
    self_label = 'RU' if lang == 'ru' else 'EN'
    canonical = f'https://cycterna2222288888-ai.github.io/cremle/timeline{"" if lang == "ru" else "-en"}.html'
    footer_left = 'Голоса Кремля · 2025' if lang == 'ru' else 'Kremlin Voices · 2025'
    footer_right = 'Открытые источники' if lang == 'ru' else 'Open Sources'
    html_lang = lang

    entries_html = ''
    for year, head, body in events:
        entries_html += f"""    <div class="tl-entry">
      <div class="tl-year">{year}</div>
      <div class="tl-content">
        <h3>{head}</h3>
        <p>{body}</p>
      </div>
    </div>\n"""

    return f"""<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{'Хронология ключевых событий: как Кремль строил медиамашину пропаганды с 1999 по 2025 год.' if lang=='ru' else 'Timeline of key events: how the Kremlin built its propaganda media machine from 1999 to 2025.'}">
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="canonical" href="{canonical}">
<style>
{TL_CSS}
</style>
</head>
<body>
<div class="topbar">
  <div class="topbar-left"><a href="{back_href}">{back}</a></div>
  <div class="topbar-right">
    <a href="timeline.html">{('RU' if lang=='en' else '<strong>RU</strong>')}</a>
    <a href="timeline-en.html">{('EN' if lang=='ru' else '<strong>EN</strong>')}</a>
  </div>
</div>

<div class="tl-hero">
  <div class="tl-eyebrow">{eyebrow}</div>
  <h1 class="tl-title">{heading}</h1>
</div>

<div class="tl-body">
{entries_html}</div>

<div class="footer">
  <span>{footer_left}</span>
  <span>{footer_right}</span>
</div>
</body>
</html>"""

with open(BASE + 'timeline.html', 'w', encoding='utf-8') as f:
    f.write(make_timeline_page(TIMELINE_EVENTS_RU, 'ru'))
with open(BASE + 'timeline-en.html', 'w', encoding='utf-8') as f:
    f.write(make_timeline_page(TIMELINE_EVENTS_EN, 'en'))
print('✓ timeline.html + timeline-en.html')

# ── 9. KEYBOARD NAV ON PESKOV/LAVROV/MIZULINA ─────────────────────────────
KB_NAV_JS = """<script>
(function(){{
  var pages = {pages};
  var cur = window.location.pathname.split('/').pop();
  var idx = pages.indexOf(cur);
  if (idx < 0) return;
  document.addEventListener('keydown', function(e){{
    if (e.altKey || e.ctrlKey || e.metaKey || e.shiftKey) return;
    if (e.target && (e.target.tagName==='INPUT'||e.target.tagName==='TEXTAREA')) return;
    if (e.key==='ArrowRight' && idx < pages.length-1) location.href = pages[idx+1];
    if (e.key==='ArrowLeft'  && idx > 0)             location.href = pages[idx-1];
  }});
}})();
</script>"""

PAGES_RU = "['solovyov.html','skabeeva.html','simonyan.html','kiselyov.html','popov.html','sheynin.html','tolstoy.html','norkin.html','keosayan.html','andreyeva.html','leontyev.html','mamontov.html','medinsky.html','prilepin.html','dugin.html','mikhalkov.html','korchevnikov.html','krasovsky.html','medvedev.html','kadyrov.html','malofeev.html','nikonov.html','poddubny.html','zakharova.html','kovalchuk.html','turchak.html','navka.html','peskov.html','lavrov.html','mizulina.html']"
PAGES_EN = "['solovyov-en.html','skabeeva-en.html','simonyan-en.html','kiselyov-en.html','popov-en.html','sheynin-en.html','tolstoy-en.html','norkin-en.html','keosayan-en.html','andreyeva-en.html','leontyev-en.html','mamontov-en.html','medinsky-en.html','prilepin-en.html','dugin-en.html','mikhalkov-en.html','korchevnikov-en.html','krasovsky-en.html','medvedev-en.html','kadyrov-en.html','malofeev-en.html','nikonov-en.html','poddubny-en.html','zakharova-en.html','kovalchuk-en.html','turchak-en.html','navka-en.html','peskov-en.html','lavrov-en.html','mizulina-en.html']"

kb_updated = 0
for slug in ['peskov', 'lavrov', 'mizulina']:
    for sfx, pages in [('', PAGES_RU), ('-en', PAGES_EN)]:
        path = BASE + slug + sfx + '.html'
        if not os.path.exists(path): continue
        with open(path, encoding='utf-8') as f:
            html = f.read()
        if 'ArrowRight' not in html:
            nav = KB_NAV_JS.format(pages=pages)
            html = html.replace('</body>', nav + '</body>')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            kb_updated += 1

print(f'✓ Keyboard nav added to {kb_updated} pages')

# ── 10. ADD ABOUT/TIMELINE LINKS TO NAV ON BOTH INDEX PAGES ──────────────
NAV_LINKS_RU = '<a href="about.html" style="font-size:10px;letter-spacing:0.25em;text-transform:uppercase;color:#555;text-decoration:none;padding:6px 12px;border:1px solid #222;transition:all 0.2s" onmouseover="this.style.color=\'#ede8dc\'" onmouseout="this.style.color=\'#555\'">О проекте</a>'
NAV_LINKS_EN = '<a href="about-en.html" style="font-size:10px;letter-spacing:0.25em;text-transform:uppercase;color:#555;text-decoration:none;padding:6px 12px;border:1px solid #222;transition:all 0.2s" onmouseover="this.style.color=\'#ede8dc\'" onmouseout="this.style.color=\'#555\'">About</a>'

for fname, nav_link in [('index.html', NAV_LINKS_RU), ('index-en.html', NAV_LINKS_EN)]:
    path = BASE + fname
    with open(path, encoding='utf-8') as f:
        html = f.read()
    if 'about.html' not in html and 'about-en.html' not in html:
        html = html.replace('</nav>', nav_link + '</nav>', 1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)

print('\nAll upgrade tasks done.')
