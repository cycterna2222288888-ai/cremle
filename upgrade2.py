#!/usr/bin/env python3
"""upgrade2.py — submit fix, search-index, RSS, random button,
   last-updated, print CSS, umami removal, PWA manifest"""
import re, os, json
from datetime import datetime

BASE   = '/Users/petrdracev/Desktop/proj/cremle/'
DOMAIN = 'https://cycterna2222288888-ai.github.io/cremle'
NOW    = 'апрель 2026'
NOW_EN = 'April 2026'
RFC822 = 'Wed, 22 Apr 2026 12:00:00 +0000'

SLUGS = ['solovyov','skabeeva','simonyan','kiselyov','popov','sheynin','tolstoy',
         'norkin','keosayan','andreyeva','leontyev','mamontov','medinsky','prilepin',
         'dugin','mikhalkov','korchevnikov','krasovsky','medvedev','kadyrov','malofeev',
         'nikonov','poddubny','zakharova','kovalchuk','turchak','navka','peskov',
         'lavrov','mizulina','nebenzya','patrushev','matvienko','slutsky','emizulina']

CHANNEL = {
    'solovyov':'rossiya1','skabeeva':'rossiya1','simonyan':'rt','kiselyov':'rt',
    'popov':'rossiya1','sheynin':'perviy','tolstoy':'vlast','norkin':'ntv',
    'keosayan':'rt','andreyeva':'perviy','leontyev':'perviy','mamontov':'rossiya1',
    'medinsky':'vlast','prilepin':'vlast','dugin':'ideolog','mikhalkov':'kultura',
    'korchevnikov':'rossiya1','krasovsky':'rt','medvedev':'vlast','kadyrov':'vlast',
    'malofeev':'ideolog','nikonov':'vlast','poddubny':'rt','zakharova':'vlast',
    'kovalchuk':'ideolog','turchak':'vlast','navka':'kultura','peskov':'vlast',
    'lavrov':'vlast','mizulina':'vlast','nebenzya':'vlast','patrushev':'vlast',
    'matvienko':'vlast','slutsky':'vlast','emizulina':'vlast',
}

# ─────────────────────────────────────────────────────────────────
# 1. FIX submit.html + submit-en.html (replace broken Netlify form)
# ─────────────────────────────────────────────────────────────────

NEW_PERSONS_RU = [
    'Мария Захарова','Юрий Ковальчук','Андрей Турчак','Татьяна Навка',
    'Дмитрий Песков','Сергей Лавров','Елена Мизулина','Василий Небензя',
    'Николай Патрушев','Валентина Матвиенко','Леонид Слуцкий','Екатерина Мизулина',
]
NEW_PERSONS_EN = [
    'Maria Zakharova','Yuri Kovalchuk','Andrei Turchak','Tatiana Navka',
    'Dmitry Peskov','Sergei Lavrov','Elena Mizulina','Vasily Nebenzya',
    'Nikolai Patrushev','Valentina Matvienko','Leonid Slutsky','Ekaterina Mizulina',
]

def fix_submit(path, new_options_html, lang='ru'):
    if not os.path.exists(path): return
    txt = open(path, encoding='utf-8').read()

    # 1) Remove Netlify attributes from <form>
    txt = re.sub(r'\s*data-netlify="true"', '', txt)
    txt = re.sub(r'\s*data-netlify-honeypot="bot-field"', '', txt)
    txt = txt.replace('<input type="hidden" name="form-name" value="tips">\n', '')
    txt = txt.replace('<p style="display:none"><input name="bot-field"></p>\n', '')

    # 2) Add Formspree action
    txt = txt.replace(
        '<form id="tip-form" name="tips" method="POST">',
        '<!-- To activate: create free account at formspree.io and replace FORMSPREE_ID -->\n'
        '    <form id="tip-form" action="https://formspree.io/f/FORMSPREE_ID" method="POST">'
    )

    # 3) Update JS: replace fetch('/') with fetch to form action
    old_js = '''  try {
    const res = await fetch('/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams(new FormData(form)).toString(),
    });'''
    new_js = '''  try {
    const res = await fetch(form.action, {
      method: 'POST',
      headers: { 'Accept': 'application/json' },
      body: new FormData(form),
    });'''
    txt = txt.replace(old_js, new_js)

    # 4) Add missing persons to dropdown
    INSERT_AFTER = '<option value="Общее">Общее / Несколько фигурантов</option>' if lang=='ru' else '<option value="General">General / Multiple subjects</option>'
    extra = '\n'.join(f'        <option>{p}</option>' for p in new_options_html)
    txt = txt.replace(
        '        <option value="Евгений Поддубный">Евгений Поддубный</option>\n        <option value="Общее">',
        '        <option value="Евгений Поддубный">Евгений Поддубный</option>\n' + extra + '\n        <option value="Общее">'
    ) if lang == 'ru' else txt

    open(path, 'w', encoding='utf-8').write(txt)

fix_submit(BASE + 'submit.html', NEW_PERSONS_RU, 'ru')
fix_submit(BASE + 'submit-en.html', NEW_PERSONS_EN, 'en')
print('✓ submit.html + submit-en.html: Netlify → Formspree, missing persons added')

# ─────────────────────────────────────────────────────────────────
# 2. REBUILD search-index.json (add missing 24 entries)
# ─────────────────────────────────────────────────────────────────

def extract_dossier(fpath):
    if not os.path.exists(fpath): return None
    txt = open(fpath, encoding='utf-8').read()
    fname = os.path.basename(fpath)
    is_en = fname.endswith('-en.html')

    # name from <title>
    m = re.search(r'<title>([^·<]+)', txt)
    name = m.group(1).strip() if m else fname.replace('.html','').replace('-en','')

    # bio: first hero paragraph or first p with >40 chars
    m = re.search(r'class="hero-sub[^"]*"[^>]*>([^<]{40,})', txt)
    if not m: m = re.search(r'class="masthead-sub[^"]*"[^>]*>([^<]{40,})', txt)
    bio = m.group(1).strip()[:200] if m else ''

    # tags: extract from card-facts or badge texts
    tags = re.findall(r'class="card-fact[^"]*"[^>]*>([^<]+)', txt)[:6]
    if not tags:
        tags = re.findall(r'class="badge[^"]*"[^>]*>([^<]+)', txt)[:6]
    tags = [t.strip() for t in tags if len(t.strip()) > 2]

    # quotes: blockquotes + qc-text
    raw = re.findall(r'<blockquote>([^<]{10,})</blockquote>', txt)[:3]
    raw += re.findall(r'class="qc-text"[^>]*>([^<]{10,})', txt)[:3]
    quotes = [q.strip() for q in raw][:4]

    slug_base = fname.replace('-en.html','').replace('.html','')
    ch = CHANNEL.get(slug_base, 'vlast')

    return {
        'file': fname,
        'name': name,
        'channel': ch,
        'tags': tags,
        'bio': bio,
        'quotes': quotes,
    }

idx_path = BASE + 'data/search-index.json'
existing = json.load(open(idx_path, encoding='utf-8'))
existing_files = {e['file'] for e in existing}

added = 0
for slug in SLUGS:
    for suffix in ['.html', '-en.html']:
        fname = slug + suffix
        if fname not in existing_files:
            entry = extract_dossier(BASE + fname)
            if entry:
                existing.append(entry)
                added += 1

# Sort by slug order
order = {slug+sfx: i*2 + (1 if sfx=='-en.html' else 0)
         for i, slug in enumerate(SLUGS) for sfx in ['.html','-en.html']}
existing.sort(key=lambda e: order.get(e['file'], 999))

json.dump(existing, open(idx_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'✓ search-index.json: {added} записей добавлено, всего {len(existing)}')

# ─────────────────────────────────────────────────────────────────
# 3. RSS FEED
# ─────────────────────────────────────────────────────────────────

PERSON_DATA = {
    'solovyov': ('Владимир Соловьёв', 'Ведущий «России-1», самый высокооплачиваемый пропагандист Кремля'),
    'skabeeva': ('Ольга Скабеева', 'Ведущая «60 минут» на «России-1»'),
    'simonyan': ('Маргарита Симоньян', 'Главный редактор RT и МИА «Россия сегодня»'),
    'kiselyov': ('Дмитрий Киселёв', 'Гендиректор МИА «Россия сегодня», ведущий «Вестей недели»'),
    'popov': ('Евгений Попов', 'Депутат ГД, ведущий «60 минут»'),
    'sheynin': ('Артём Шейнин', 'Ведущий «Время покажет», Первый канал'),
    'tolstoy': ('Пётр Толстой', 'Вице-спикер ГД, бывший ведущий Первого канала'),
    'norkin': ('Андрей Норкин', 'Ведущий «Место встречи», НТВ'),
    'keosayan': ('Тигран Кеосаян', 'Режиссёр, документалист RT'),
    'andreyeva': ('Екатерина Андреева', 'Ведущая новостей Первого канала'),
    'leontyev': ('Михаил Леонтьев', 'Комментатор Первого канала, «Однако»'),
    'mamontov': ('Аркадий Мамонтов', 'Документалист «Россия-1»'),
    'medinsky': ('Владимир Мединский', 'Помощник Президента, экс-министр культуры'),
    'prilepin': ('Захар Прилепин', 'Писатель, политик, участник войны на Донбассе'),
    'dugin': ('Александр Дугин', 'Идеолог, основатель евразийства'),
    'mikhalkov': ('Никита Михалков', 'Режиссёр, телеведущий «Бесогон»'),
    'korchevnikov': ('Борис Корчевников', 'Ведущий «Судьба человека», «Россия-1»'),
    'krasovsky': ('Антон Красовский', 'Бывший ведущий RT, автор скандальных высказываний'),
    'medvedev': ('Дмитрий Медведев', 'Зампред Совбеза, бывший президент и премьер России'),
    'kadyrov': ('Рамзан Кадыров', 'Глава Чеченской Республики'),
    'malofeev': ('Константин Малофеев', 'Православный олигарх, основатель «Царьграда»'),
    'nikonov': ('Вячеслав Никонов', 'Депутат ГД, внук Молотова'),
    'poddubny': ('Евгений Поддубный', 'Военный корреспондент «России-1»'),
    'zakharova': ('Мария Захарова', 'Официальный представитель МИД России'),
    'kovalchuk': ('Юрий Ковальчук', 'Медиаолигарх, совладелец «Национальной медиагруппы»'),
    'turchak': ('Андрей Турчак', 'Сенатор, экс-секретарь Генсовета «Единой России»'),
    'navka': ('Татьяна Навка', 'Фигуристка, жена Пескова, ведущая государственных шоу'),
    'peskov': ('Дмитрий Песков', 'Пресс-секретарь Президента России'),
    'lavrov': ('Сергей Лавров', 'Министр иностранных дел России'),
    'mizulina': ('Елена Мизулина', 'Сенатор, автор «антигейского» закона'),
    'nebenzya': ('Василий Небензя', 'Постпред России в ООН, автор 17+ вето'),
    'patrushev': ('Николай Патрушев', 'Советник Президента, экс-директор ФСБ'),
    'matvienko': ('Валентина Матвиенко', 'Председатель Совета Федерации'),
    'slutsky': ('Леонид Слуцкий', 'Лидер ЛДПР, председатель комитета ГД по международным делам'),
    'emizulina': ('Екатерина Мизулина', 'Глава Лиги Безопасного Интернета, дочь Елены Мизулиной'),
}

items = []
for slug, (name, desc) in PERSON_DATA.items():
    items.append(f"""  <item>
    <title>Досье: {name}</title>
    <link>{DOMAIN}/{slug}.html</link>
    <description><![CDATA[{desc}]]></description>
    <guid isPermaLink="true">{DOMAIN}/{slug}.html</guid>
    <pubDate>{RFC822}</pubDate>
  </item>""")

rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Голоса Кремля — архив досье</title>
    <link>{DOMAIN}/</link>
    <description>Независимый архив биографий и методов российских пропагандистов. 35 досье, открытые источники.</description>
    <language>ru</language>
    <lastBuildDate>{RFC822}</lastBuildDate>
    <atom:link href="{DOMAIN}/rss.xml" rel="self" type="application/rss+xml"/>
    <image>
      <url>{DOMAIN}/og-image.svg</url>
      <title>Голоса Кремля</title>
      <link>{DOMAIN}/</link>
    </image>
{chr(10).join(items)}
  </channel>
</rss>"""

open(BASE + 'rss.xml', 'w', encoding='utf-8').write(rss)
print(f'✓ rss.xml: {len(items)} dosье')

# ─────────────────────────────────────────────────────────────────
# 4. RANDOM DOSSIER BUTTON — add to index.html + index-en.html
# ─────────────────────────────────────────────────────────────────

RANDOM_BTN_RU = '  <button class="flt-btn" id="btn-random" onclick="goRandom()" title="Открыть случайное досье">&#x2685; Случайное</button>'
RANDOM_BTN_EN = '  <button class="flt-btn" id="btn-random" onclick="goRandom()" title="Open a random dossier">&#x2685; Random</button>'
RANDOM_JS_RU = """<script>
function goRandom(){
  var cards=document.querySelectorAll('.card:not([style*="none"])');
  if(!cards.length) cards=document.querySelectorAll('.card');
  var c=cards[Math.floor(Math.random()*cards.length)];
  if(c) window.location.href=c.getAttribute('href');
}
</script>"""

def add_random(fpath, btn_html, js_html):
    if not os.path.exists(fpath): return
    txt = open(fpath, encoding='utf-8').read()
    if 'goRandom' in txt: return
    # Add button at end of filter-bar
    txt = txt.replace('  <div class="search-wrap">', btn_html + '\n  <div class="search-wrap">', 1)
    # Add JS before </body>
    txt = txt.replace('</body>', js_html + '\n</body>', 1)
    open(fpath, 'w', encoding='utf-8').write(txt)

add_random(BASE + 'index.html', RANDOM_BTN_RU, RANDOM_JS_RU)
add_random(BASE + 'index-en.html',
           RANDOM_BTN_EN.replace('goRandom','goRandom'),
           RANDOM_JS_RU)
print('✓ index.html + index-en.html: кнопка "Случайное досье" добавлена')

# ─────────────────────────────────────────────────────────────────
# 5. LAST-UPDATED STAMP — all 70 dossier pages
# ─────────────────────────────────────────────────────────────────

STAMP_CSS = """<style>
.updated-stamp{padding:12px 60px;font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:#2a2a2a;border-top:1px solid #111;text-align:right;}
@media(max-width:768px){.updated-stamp{padding:10px 24px;}}
</style>"""

n_stamp = 0
for slug in SLUGS:
    for suffix in ['.html', '-en.html']:
        fpath = BASE + slug + suffix
        if not os.path.exists(fpath): continue
        txt = open(fpath, encoding='utf-8').read()
        if 'updated-stamp' in txt: continue
        label = f'Досье обновлено: {NOW}' if suffix == '.html' else f'Dossier updated: {NOW_EN}'
        stamp = f'\n<div class="updated-stamp">{label}</div>\n'
        # Insert before footer or before </body>
        if '<div class="footer">' in txt:
            txt = txt.replace('<div class="footer">', stamp + '<div class="footer">', 1)
        else:
            txt = txt.replace('</body>', stamp + '</body>', 1)
        # Add CSS once before </head>
        if 'updated-stamp' not in txt.split('<body>')[0]:
            txt = txt.replace('</head>', STAMP_CSS + '</head>', 1)
        open(fpath, 'w', encoding='utf-8').write(txt)
        n_stamp += 1

print(f'✓ Last-updated stamp: {n_stamp} страниц')

# ─────────────────────────────────────────────────────────────────
# 6. PRINT CSS — all 70 dossier pages
# ─────────────────────────────────────────────────────────────────

PRINT_CSS = """<style media="print">
  .topbar,.section-nav,.nav-back,.filter-bar,.share-bar,.related-section,
  .scroll-top,.reading-time,footer,.footer,.updated-stamp,
  [class*="btn"],[class*="nav-pages"]{display:none!important;}
  body{background:#fff!important;color:#000!important;font-size:11pt;}
  a{color:#000;text-decoration:none;}
  .hero{padding:20pt 0 12pt;}
  .badge-fact,.badge-interp,.badge{border:1px solid #999;background:none!important;color:#000!important;}
  .quote-card,.qc-text,.fq-text{color:#000!important;}
  .qc-year{color:#666!important;}
  h1,h2,h3{page-break-after:avoid;}
  .timeline-item,.quote-card{page-break-inside:avoid;}
  @page{margin:2cm;}
</style>"""

n_print = 0
for slug in SLUGS:
    for suffix in ['.html', '-en.html']:
        fpath = BASE + slug + suffix
        if not os.path.exists(fpath): continue
        txt = open(fpath, encoding='utf-8').read()
        if 'media="print"' in txt: continue
        txt = txt.replace('</head>', PRINT_CSS + '\n</head>', 1)
        open(fpath, 'w', encoding='utf-8').write(txt)
        n_print += 1

print(f'✓ Print CSS: {n_print} страниц')

# ─────────────────────────────────────────────────────────────────
# 7. REMOVE UMAMI placeholder from all HTML files
# ─────────────────────────────────────────────────────────────────

UMAMI_RE = re.compile(
    r'\s*<!-- Analytics[^>]*-->\s*\n?'
    r'\s*<script defer src="https://cloud\.umami\.is/script\.js"[^>]*></script>\s*\n?',
    re.DOTALL
)

n_umami = 0
for f in os.listdir(BASE):
    if not f.endswith('.html'): continue
    fpath = BASE + f
    txt = open(fpath, encoding='utf-8').read()
    if 'umami' not in txt: continue
    new = UMAMI_RE.sub('\n', txt)
    if new != txt:
        open(fpath, 'w', encoding='utf-8').write(new)
        n_umami += 1

print(f'✓ Umami: удалён из {n_umami} файлов')

# ─────────────────────────────────────────────────────────────────
# 8. PWA MANIFEST
# ─────────────────────────────────────────────────────────────────

manifest = {
    "name": "Голоса Кремля",
    "short_name": "Кремль",
    "description": "Независимый архив кремлёвской пропаганды",
    "start_url": "/cremle/",
    "scope": "/cremle/",
    "display": "standalone",
    "background_color": "#080808",
    "theme_color": "#8b1a1a",
    "lang": "ru",
    "icons": [
        {"src": "favicon.svg", "sizes": "any", "type": "image/svg+xml", "purpose": "any maskable"}
    ]
}
json.dump(manifest, open(BASE + 'manifest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# Add <link rel="manifest"> to index pages and about pages
MANIFEST_LINK = '<link rel="manifest" href="manifest.json">'
for f in ['index.html', 'index-en.html', 'about.html', 'about-en.html']:
    fpath = BASE + f
    if not os.path.exists(fpath): continue
    txt = open(fpath, encoding='utf-8').read()
    if 'manifest' in txt: continue
    txt = txt.replace('<link rel="icon"', MANIFEST_LINK + '\n<link rel="icon"', 1)
    open(fpath, 'w', encoding='utf-8').write(txt)

print('✓ manifest.json создан, <link rel="manifest"> добавлен')

# ─────────────────────────────────────────────────────────────────
# 9. RSS link in <head> of index pages
# ─────────────────────────────────────────────────────────────────

RSS_LINK = f'<link rel="alternate" type="application/rss+xml" title="Голоса Кремля — RSS" href="rss.xml">'
RSS_LINK_EN = f'<link rel="alternate" type="application/rss+xml" title="Kremlin Voices — RSS" href="rss.xml">'

for f, link in [('index.html', RSS_LINK), ('index-en.html', RSS_LINK_EN)]:
    fpath = BASE + f
    txt = open(fpath, encoding='utf-8').read()
    if 'rss+xml' in txt: continue
    txt = txt.replace('</head>', link + '\n</head>', 1)
    open(fpath, 'w', encoding='utf-8').write(txt)

print('✓ RSS <link> добавлен в index pages')

print('\n✓ Всё готово.')
