#!/usr/bin/env python3
"""Final comprehensive fix: photos, sanctions-en, sources, quotes, manifest, dark mode, search."""

import re, pathlib, glob, json

BASE = pathlib.Path(__file__).parent

IMG_STYLE = ('position:absolute;inset:0;width:100%;height:100%;'
             'object-fit:cover;object-position:top center;'
             'opacity:0.88;')
IMG_TAG = '<img loading="lazy" src="{url}" alt="{name}" style="' + IMG_STYLE + '" onerror="this.style.display=\'none\'">'

# ── PHOTOS (26 persons found) ─────────────────────────────────────────────────
PHOTOS = {
    'solovyov':    'https://upload.wikimedia.org/wikipedia/commons/4/40/%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80_%D0%A1%D0%BE%D0%BB%D0%BE%D0%B2%D1%8C%D0%B5%D0%B2_%28cropped%29.jpg',
    'simonyan':    'https://upload.wikimedia.org/wikipedia/commons/4/4d/%D0%9C%D0%B0%D1%80%D0%B3%D0%B0%D1%80%D0%B8%D1%82%D0%B0_%D0%A1%D0%B8%D0%BC%D0%BE%D0%BD%D1%8C%D1%8F%D0%BD_%2812-02-2026%29.jpg',
    'kiselyov':    'https://upload.wikimedia.org/wikipedia/commons/b/b5/Opening_of_Sputnik_hub_in_Ethiopia_06_%28cropped%29.jpg',
    'popov':       'https://upload.wikimedia.org/wikipedia/commons/e/e4/Evgeny_Popov_%28deputy%29.jpg',
    'sheynin':     'https://upload.wikimedia.org/wikipedia/commons/e/e2/%D0%90%D1%80%D1%82%D0%B5%D0%BC_%D0%A8%D0%B5%D0%B9%D0%BD%D0%B8%D0%BD_-_03_%2806-08-2025%29_%28cropped%29.jpg',
    'tolstoy':     'https://upload.wikimedia.org/wikipedia/commons/9/97/Pyotr_Tolstoy_2018.jpg',
    'keosayan':    'https://upload.wikimedia.org/wikipedia/commons/d/d2/Tigran_Keosayan_%282018-10-12%29.jpg',
    'prilepin':    'https://upload.wikimedia.org/wikipedia/commons/4/4a/Zahar-Prilepin_%281%29.jpg',
    'medinsky':    'https://upload.wikimedia.org/wikipedia/commons/b/b7/Vladimir_Medinsky_2025-06-05_%28cropped%29.jpg',
    'mikhalkov':   'https://upload.wikimedia.org/wikipedia/commons/9/90/%D0%9D%D0%B8%D0%BA%D0%B8%D1%82%D0%B0_%D0%9C%D0%B8%D1%85%D0%B0%D0%BB%D0%BA%D0%BE%D0%B2_%D0%BF%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82_%28cropped%29.jpg',
    'dugin':       'https://upload.wikimedia.org/wikipedia/commons/b/bd/Aleksandr_Dugin_2023_%283x4_cropped%29.jpg',
    'krasovsky':   'https://upload.wikimedia.org/wikipedia/commons/6/66/Anton_Krasovsky_2022.png',
    'medvedev':    'https://upload.wikimedia.org/wikipedia/commons/7/75/Dmitry_Medvedev_%282026-02-06%29.jpg',
    'kadyrov':     'https://upload.wikimedia.org/wikipedia/commons/d/db/Ramzan_Kadyrov_May_2024.jpg',
    'malofeev':    'https://upload.wikimedia.org/wikipedia/commons/a/aa/%D0%9C%D0%B0%D0%BB%D0%BE%D1%84%D0%B5%D0%B5%D0%B2_%28cropped%29.jpg',
    'nikonov':     'https://upload.wikimedia.org/wikipedia/commons/4/41/Vyacheslav_Nikonov.jpg',
    'poddubny':    'https://upload.wikimedia.org/wikipedia/commons/c/c8/Yevgeny_Poddubny_%282023%29.jpg',
    'lavrov':      'https://upload.wikimedia.org/wikipedia/commons/5/5b/%D0%A1%D0%B5%D1%80%D0%B3%D0%B5%D0%B9_%D0%9B%D0%B0%D0%B2%D1%80%D0%BE%D0%B2_%28cropped%29.jpg',
    'peskov':      'https://upload.wikimedia.org/wikipedia/commons/b/b1/Dmitry_Peskov_portrait.jpg',
    'zakharova':   'https://upload.wikimedia.org/wikipedia/commons/f/f4/%D0%9C%D0%B0%D1%80%D0%B8%D1%8F_%D0%97%D0%B0%D1%85%D0%B0%D1%80%D0%BE%D0%B2%D0%B0_%2828-11-2024%29_%28cropped%29.jpg',
    'navka':       'https://upload.wikimedia.org/wikipedia/commons/7/76/Tatyana_Navka-edit.jpg',
    'mizulina':    'https://upload.wikimedia.org/wikipedia/commons/c/c3/Elena_Mizulina%2C_2016.jpg',
    'leontyev':    'https://upload.wikimedia.org/wikipedia/commons/5/51/Mikhail_Leontyev_08.jpg',
    'mamontov':    'https://upload.wikimedia.org/wikipedia/commons/c/c4/Arkady_Mamontov_%28cropped%29.jpg',
    'korchevnikov':'https://upload.wikimedia.org/wikipedia/commons/9/92/2019_Boris_Korchevnikov.jpg',
    'turchak':     'https://upload.wikimedia.org/wikipedia/commons/4/44/Andrey_Turchak_%282023-04-24%29_2.jpg',
}

# Names for alt text (RU / EN)
NAMES_RU = {
    'solovyov':'Владимир Соловьёв','simonyan':'Маргарита Симоньян','kiselyov':'Дмитрий Киселёв',
    'popov':'Евгений Попов','sheynin':'Артём Шейнин','tolstoy':'Пётр Толстой',
    'keosayan':'Тигран Кеосаян','prilepin':'Захар Прилепин','medinsky':'Владимир Мединский',
    'mikhalkov':'Никита Михалков','dugin':'Александр Дугин','krasovsky':'Антон Красовский',
    'medvedev':'Дмитрий Медведев','kadyrov':'Рамзан Кадыров','malofeev':'Константин Малофеев',
    'nikonov':'Вячеслав Никонов','poddubny':'Евгений Поддубный','lavrov':'Сергей Лавров',
    'peskov':'Дмитрий Песков','zakharova':'Мария Захарова','navka':'Татьяна Навка',
    'mizulina':'Елена Мизулина','leontyev':'Михаил Леонтьев','mamontov':'Аркадий Мамонтов',
    'korchevnikov':'Борис Корчевников','turchak':'Андрей Турчак',
}
NAMES_EN = {
    'solovyov':'Vladimir Solovyov','simonyan':'Margarita Simonyan','kiselyov':'Dmitry Kiselyov',
    'popov':'Yevgeny Popov','sheynin':'Artyom Sheynin','tolstoy':'Pyotr Tolstoy',
    'keosayan':'Tigran Keosayan','prilepin':'Zakhar Prilepin','medinsky':'Vladimir Medinsky',
    'mikhalkov':'Nikita Mikhalkov','dugin':'Alexander Dugin','krasovsky':'Anton Krasovsky',
    'medvedev':'Dmitry Medvedev','kadyrov':'Ramzan Kadyrov','malofeev':'Konstantin Malofeev',
    'nikonov':'Vyacheslav Nikonov','poddubny':'Yevgeny Poddubny','lavrov':'Sergei Lavrov',
    'peskov':'Dmitry Peskov','zakharova':'Maria Zakharova','navka':'Tatiana Navka',
    'mizulina':'Yelena Mizulina','leontyev':'Mikhail Leontyev','mamontov':'Arkady Mamontov',
    'korchevnikov':'Boris Korchevnikov','turchak':'Andrei Turchak',
}

print('=== 1. PHOTOS ===')
photo_pat = re.compile(r'(<div class="hero-right">)\s*(<svg)', re.DOTALL)
added = 0
for name, url in PHOTOS.items():
    for suffix, names in [('.html', NAMES_RU), ('-en.html', NAMES_EN)]:
        p = BASE / (name + suffix)
        if not p.exists():
            continue
        html = p.read_text('utf-8')
        hero_idx = html.find('class="hero-right"')
        svg_idx = html.find('<svg', hero_idx)
        segment = html[hero_idx:svg_idx]
        if '<img' in segment:
            continue  # already has photo
        alt = names.get(name, name)
        img = IMG_TAG.format(url=url, name=alt)
        new_html, n = photo_pat.subn(r'\1\n    ' + img + r'\n    \2', html)
        if n:
            p.write_text(new_html, 'utf-8')
            added += 1
print(f'  ✓ {added} dossier files got photos')

# ── 2. SANCTIONS-EN: fix stat + add sections 02 & 03 ─────────────────────────
print('\n=== 2. sanctions-en.html ===')
p = BASE / 'sanctions-en.html'
html = p.read_text('utf-8')

# Fix stale stat: 18 → 35
html = html.replace(
    '<div class="stat-cell"><div class="stat-num">18</div><div class="stat-label">Dossiers</div></div>',
    '<div class="stat-cell"><div class="stat-num">35</div><div class="stat-label">Dossiers</div></div>'
)

# Add sections 02 & 03 before footer
SECTIONS_EN = """
<div class="container section">
  <div class="section-label">Official Justifications (Selected)</div>
  <table class="sanctions-table">
    <thead><tr><th>Person</th><th>Authority</th><th>Official statement of reasons</th></tr></thead>
    <tbody>
      <tr><td><a href="kiselyov-en.html" style="color:var(--paper);text-decoration:none;font-family:'Playfair Display',serif;font-weight:700">Kiselyov</a></td><td style="font-size:12px;color:var(--light-gray)">EU — March 2014</td><td style="font-size:13px;color:var(--light-gray)">"Central figure of the state propaganda supporting the deployment of Russian forces in Ukraine and destabilisation of the country."</td></tr>
      <tr><td><a href="solovyov-en.html" style="color:var(--paper);text-decoration:none;font-family:'Playfair Display',serif;font-weight:700">Solovyov</a></td><td style="font-size:12px;color:var(--light-gray)">US State Dept — 2022</td><td style="font-size:13px;color:var(--light-gray)">"The most energetic Kremlin propagandist, systematically spreading false narratives about Ukraine and the West."</td></tr>
      <tr><td><a href="skabeeva-en.html" style="color:var(--paper);text-decoration:none;font-family:'Playfair Display',serif;font-weight:700">Skabeeva</a></td><td style="font-size:12px;color:var(--light-gray)">EU — 2022</td><td style="font-size:13px;color:var(--light-gray)">"Consciously plays her cynical role in Russia's propaganda machinery alongside her spouse; actively supports actions against Ukraine."</td></tr>
      <tr><td><a href="simonyan-en.html" style="color:var(--paper);text-decoration:none;font-family:'Playfair Display',serif;font-weight:700">Simonyan</a></td><td style="font-size:12px;color:var(--light-gray)">UK FCDO — 2022</td><td style="font-size:13px;color:var(--light-gray)">"RT is an instrument of the Russian government's information war. Simonyan is its chief architect and executor."</td></tr>
      <tr><td><a href="tolstoy-en.html" style="color:var(--paper);text-decoration:none;font-family:'Playfair Display',serif;font-weight:700">Tolstoy</a></td><td style="font-size:12px;color:var(--light-gray)">EU — 2022</td><td style="font-size:13px;color:var(--light-gray)">"Responsible for the systematic dissemination of state propaganda supporting actions undermining the sovereignty and territorial integrity of Ukraine."</td></tr>
      <tr><td><a href="prilepin-en.html" style="color:var(--paper);text-decoration:none;font-family:'Playfair Display',serif;font-weight:700">Prilepin</a></td><td style="font-size:12px;color:var(--light-gray)">EU, US, UK — 2022</td><td style="font-size:13px;color:var(--light-gray)">"Commanded a battalion within the separatist DPR forces in eastern Ukraine; actively supports and promotes actions undermining the sovereignty and territorial integrity of Ukraine."</td></tr>
      <tr><td><a href="medinsky-en.html" style="color:var(--paper);text-decoration:none;font-family:'Playfair Display',serif;font-weight:700">Medinsky</a></td><td style="font-size:12px;color:var(--light-gray)">EU, US, UK, Canada — 2022</td><td style="font-size:13px;color:var(--light-gray)">"As Putin's adviser and head of the peace delegation, responsible for maintaining conditions incompatible with Ukraine's sovereignty; systematically rewrites history to justify aggression."</td></tr>
      <tr><td><a href="dugin-en.html" style="color:var(--paper);text-decoration:none;font-family:'Playfair Display',serif;font-weight:700">Dugin</a></td><td style="font-size:12px;color:var(--light-gray)">US — 2015; EU, UK — 2022</td><td style="font-size:13px;color:var(--light-gray)">"Ideological architect of Russian expansionism; provided philosophical underpinning for the annexation of Ukrainian territory and the denial of Ukrainian national identity."</td></tr>
      <tr><td><a href="kadyrov-en.html" style="color:var(--paper);text-decoration:none;font-family:'Playfair Display',serif;font-weight:700">Kadyrov</a></td><td style="font-size:12px;color:var(--light-gray)">US Magnitsky — 2017; EU — 2022</td><td style="font-size:13px;color:var(--light-gray)">"Responsible for gross violations of human rights in Chechnya; deployed Chechen forces in Ukraine and publicly incited violence against Ukrainian civilians."</td></tr>
      <tr><td><a href="malofeev-en.html" style="color:var(--paper);text-decoration:none;font-family:'Playfair Display',serif;font-weight:700">Malofeev</a></td><td style="font-size:12px;color:var(--light-gray)">US — 2014; EU, UK, Canada — 2022</td><td style="font-size:13px;color:var(--light-gray)">"Provided financial and material support to the separatists in Donetsk and Luhansk in 2014; continued to fund Russian nationalist and separatist networks."</td></tr>
    </tbody>
  </table>
</div>

<div class="container section">
  <div class="section-label">Special Restrictions &amp; Asset Seizures</div>
  <table class="sanctions-table">
    <thead><tr><th>Person</th><th>Type</th><th>Details</th></tr></thead>
    <tbody>
      <tr><td><a href="kiselyov-en.html" style="color:var(--paper);text-decoration:none;font-family:'Playfair Display',serif;font-weight:700">Kiselyov</a></td><td style="font-size:12px;color:var(--light-gray)">Persona non grata</td><td style="font-size:13px;color:var(--light-gray)">Declared persona non grata in Moldova. Stripped of a Lithuanian state decoration. Bank accounts frozen in Switzerland.</td></tr>
      <tr><td><a href="solovyov-en.html" style="color:var(--paper);text-decoration:none;font-family:'Playfair Display',serif;font-weight:700">Solovyov</a></td><td style="font-size:12px;color:var(--light-gray)">Asset seizure</td><td style="font-size:13px;color:var(--light-gray)">Italian authorities seized property valued at approximately €8 million: 5+ real estate objects on Lake Como, a yacht. Part of the property was set on fire by unknown persons in 2022.</td></tr>
      <tr><td><a href="tolstoy-en.html" style="color:var(--paper);text-decoration:none;font-family:'Playfair Display',serif;font-weight:700">Tolstoy</a></td><td style="font-size:12px;color:var(--light-gray)">Persona non grata</td><td style="font-size:13px;color:var(--light-gray)">Declared persona non grata in Latvia and Estonia. Expelled from the PACE delegation after Russia's exclusion from the Council of Europe in March 2022.</td></tr>
      <tr><td><a href="simonyan-en.html" style="color:var(--paper);text-decoration:none;font-family:'Playfair Display',serif;font-weight:700">Simonyan / RT</a></td><td style="font-size:12px;color:var(--light-gray)">Media ban</td><td style="font-size:13px;color:var(--light-gray)">RT blocked in most EU countries; London and Berlin offices closed. RT America registered as a foreign agent in the US. RT's bank accounts frozen across Europe.</td></tr>
      <tr><td><a href="medvedev-en.html" style="color:var(--paper);text-decoration:none;font-family:'Playfair Display',serif;font-weight:700">Medvedev</a></td><td style="font-size:12px;color:var(--light-gray)">Asset freeze</td><td style="font-size:13px;color:var(--light-gray)">Assets frozen in all six sanctioning jurisdictions. Travel ban imposed by EU, US, UK, Canada, Australia and Japan simultaneously — the broadest multilateral restriction among archive subjects.</td></tr>
    </tbody>
  </table>
</div>
"""

html = html.replace(
    '\n<div class="footer">',
    SECTIONS_EN + '\n<div class="footer">'
)
p.write_text(html, 'utf-8')
print('  ✓ sanctions-en.html: stat fixed, sections 02+03 added')

# ── 3. sources.html: expand to match EN ───────────────────────────────────────
print('\n=== 3. sources.html ===')
p = BASE / 'sources.html'
html = p.read_text('utf-8')

EXTRA_SOURCES_RU = """
<div class="sources-wrap">
  <div class="section-label">Трансляции и архивы эфиров</div>
  <div class="sources-grid">
    <div class="source-card">
      <div class="source-type">Архив · США</div>
      <div class="source-name">Internet Archive — архив российского телевидения</div>
      <div class="source-desc">Archive.org хранит записи российского государственного телевидения: Россия-1, Первый канал, НТВ, RT. Используется для верификации цитат.</div>
      <div class="source-note">archive.org</div>
    </div>
    <div class="source-card">
      <div class="source-type">Мониторинг</div>
      <div class="source-name">Julia Davis — Russian Media Monitor</div>
      <div class="source-desc">Журналист и аналитик, мониторящий и субтитрирующий российское государственное телевидение для англоязычной аудитории. Источник переведённых цитат.</div>
      <div class="source-note">@JuliaDavisNews</div>
    </div>
    <div class="source-card">
      <div class="source-type">Стенограммы</div>
      <div class="source-name">Kremlin.ru — официальный архив стенограмм</div>
      <div class="source-desc">Официальный архив президентских речей, указов и пресс-конференций. Используется для верификации официальных заявлений и назначений.</div>
      <div class="source-note">kremlin.ru</div>
    </div>
    <div class="source-card">
      <div class="source-type">Санкции · Канада</div>
      <div class="source-name">Global Affairs Canada — Consolidated Canadian Autonomous Sanctions List</div>
      <div class="source-desc">Special Economic Measures (Russia) Regulations. Официальный канадский санкционный реестр с датами и обоснованиями.</div>
      <div class="source-note">international.gc.ca</div>
    </div>
    <div class="source-card">
      <div class="source-type">Расследования</div>
      <div class="source-name">Novaya Gazeta Europe · iStories</div>
      <div class="source-desc">Независимые издания о российской политике, медиа и войне. iStories специализируется на расследованиях имущества и связей элит.</div>
      <div class="source-note">novayagazeta.eu / istories.media</div>
    </div>
    <div class="source-card">
      <div class="source-type">Биографии · Фото</div>
      <div class="source-name">Государственная Дума · Совет Федерации · официальные сайты</div>
      <div class="source-desc">Официальные биографии депутатов и сенаторов. Используются для верификации дат, должностей и официальных заявлений.</div>
      <div class="source-note">duma.gov.ru / council.gov.ru</div>
    </div>
  </div>
</div>
"""

html = html.replace(
    '\n<!-- DISCLAIMER -->',
    EXTRA_SOURCES_RU + '\n<!-- DISCLAIMER -->'
)
p.write_text(html, 'utf-8')
print('  ✓ sources.html: 6 new source cards added')

# ── 4. quotes.html: add 3 quotes for new 5 persons ───────────────────────────
print('\n=== 4. quotes.html ===')
p = BASE / 'quotes.html'
html = p.read_text('utf-8')

NEW_QUOTES_RU = """        <div class="quote-card"><div class="quote-text">«Россия не ведёт войну. Россия проводит специальную военную операцию по защите мирных жителей Донбасса от восьми лет геноцида.»</div><div class="qc-person"><a href="patrushev.html">Николай Патрушев</a></div><div class="qc-date">2022 — заявление Совета безопасности РФ</div></div>
        <div class="quote-card"><div class="quote-text">«Мы не можем допустить появления враждебного России государства на нашей исторической территории. Это вопрос выживания.»</div><div class="qc-person"><a href="matvienko.html">Валентина Матвиенко</a></div><div class="qc-date">2022 — интервью RT</div></div>
        <div class="quote-card"><div class="quote-text">«Те, кто распространяют "ЛГБТ-пропаганду" в интернете среди несовершеннолетних, должны нести уголовную ответственность. Это не цензура — это защита детей.»</div><div class="qc-person"><a href="emizulina.html">Екатерина Мизулина</a></div><div class="qc-date">2023 — пресс-конференция ЛБИ</div></div>"""

# Insert before the last </div></div> closing the last quote-section
insert_before = '</div>\n</div>\n\n</main>'
if insert_before not in html:
    insert_before = '</div>\n</div>\n\n<div class="footer">'

html = html.replace(insert_before, NEW_QUOTES_RU + '\n' + insert_before, 1)
p.write_text(html, 'utf-8')
after_count = html.count('class="quote-card"')
print(f'  ✓ quotes.html: {after_count} total quote cards')

# ── 5. manifest.json ──────────────────────────────────────────────────────────
print('\n=== 5. manifest.json ===')
manifest = {
    "name": "Kremlin Voices / Голоса Кремля",
    "short_name": "Kremlin Voices",
    "description": "Documentary archive of Kremlin propaganda voices",
    "start_url": "/cremle/",
    "scope": "/cremle/",
    "display": "standalone",
    "background_color": "#080808",
    "theme_color": "#8b1a1a",
    "icons": [
        {"src": "favicon.svg", "sizes": "any", "type": "image/svg+xml", "purpose": "any maskable"}
    ]
}
(BASE / 'manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False), 'utf-8')
print('  ✓ manifest.json: bilingual name, removed hardcoded lang')

# ── 6. DARK/LIGHT MODE ────────────────────────────────────────────────────────
print('\n=== 6. Dark/light mode ===')

LIGHT_CSS = """
<style id="light-mode-css" media="(prefers-color-scheme:light)">
  /* Injected by theme toggle — applied when data-theme="light" */
</style>
<style>
[data-theme="light"] {
  --ink: #f2ede3;
  --paper: #111;
  --light-gray: #4a4a4a;
  --rule: #ccc5b5;
  --card-bg: #e8e3d8;
}
[data-theme="light"] body { background: #f2ede3; color: #111; }
[data-theme="light"] .topbar { background: #f2ede3; border-color: #ccc5b5; }
[data-theme="light"] .card { background: #e8e3d8; border-color: #ccc5b5; }
[data-theme="light"] .card-name { color: #111; }
[data-theme="light"] .card-role { color: #4a4a4a; }
[data-theme="light"] .quote-card { background: #e8e3d8; border-color: #ccc5b5; }
[data-theme="light"] .quote-text { color: #111; }
[data-theme="light"] .section { border-color: #ccc5b5; }
[data-theme="light"] .masthead { border-color: #ccc5b5; }
[data-theme="light"] .timeline-year { border-color: #ccc5b5; }
[data-theme="light"] .hero-left { background: #f2ede3; }
[data-theme="light"] .hero-right { background: #d8d3c8; }
[data-theme="light"] .sanctions-table th { background: #e0dbd0; }
[data-theme="light"] .sanctions-table td { border-color: #ccc5b5; }
[data-theme="light"] .sanctions-table tr:hover td { background: #e8e3d8; }
[data-theme="light"] .source-card { background: #e8e3d8; border-color: #ccc5b5; }
[data-theme="light"] .footer { border-color: #ccc5b5; color: #888; }
[data-theme="light"] .nav-back { background: #f2ede3; border-color: #ccc5b5; }
[data-theme="light"] #progress-bar { background: #8b1a1a; }
</style>"""

TOGGLE_BTN = '<button id="theme-toggle" onclick="(function(){var t=document.documentElement.dataset.theme===\'light\'?\'dark\':\'light\';document.documentElement.dataset.theme=t;localStorage.setItem(\'theme\',t);document.getElementById(\'theme-toggle\').title=t===\'light\'?\'Switch to dark\':\'Switch to light\';})()" title="Switch to light" style="background:none;border:1px solid #333;color:#888;font-size:9px;letter-spacing:0.15em;text-transform:uppercase;padding:5px 10px;cursor:pointer;font-family:\'Inter\',sans-serif;transition:all 0.2s" onmouseover="this.style.color=\'var(--paper)\'" onmouseout="this.style.color=\'#888\'">☀ Light</button>'

TOGGLE_SCRIPT = """<script>
(function(){
  var t=localStorage.getItem('theme')||'dark';
  document.documentElement.dataset.theme=t;
  var btn=document.getElementById('theme-toggle');
  if(btn){btn.textContent=t==='light'?'☽ Dark':'☀ Light';btn.title=t==='light'?'Switch to dark':'Switch to light';}
})();
</script>"""

patched_theme = 0
for f in sorted(glob.glob(str(BASE / '*.html'))):
    fname = pathlib.Path(f).name
    if fname == 'googlec2551b38ace60f0f.html':
        continue
    html = pathlib.Path(f).read_text('utf-8')
    if 'theme-toggle' in html:
        continue
    changed = False
    # Add CSS before </style> (first one)
    if '</style>' in html and 'data-theme' not in html:
        html = html.replace('</head>', LIGHT_CSS + '\n</head>', 1)
        changed = True
    # Add toggle button to topbar-right or topbar
    if 'topbar-right' in html:
        html = html.replace('</div>\n</nav>', TOGGLE_BTN + '\n</div>\n</nav>', 1)
        if TOGGLE_BTN not in html:
            html = re.sub(r'(<div class="topbar-right">)', r'\1' + TOGGLE_BTN, html, count=1)
        changed = True
    elif 'class="topbar"' in html or "class='topbar'" in html:
        html = re.sub(r'(class=["\']topbar["\'][^>]*>)', r'\1' + TOGGLE_BTN, html, count=1)
        changed = True
    # Add init script before </body>
    html = html.replace('</body>', TOGGLE_SCRIPT + '\n</body>', 1)
    pathlib.Path(f).write_text(html, 'utf-8')
    patched_theme += 1

print(f'  ✓ {patched_theme} pages: dark/light toggle added')

# ── 7. SEARCH on sanctions pages ──────────────────────────────────────────────
print('\n=== 7. Sanctions search ===')

SEARCH_CSS = """
<style>
.sanctions-search { padding:16px 0 0; display:flex; gap:12px; align-items:center; flex-wrap:wrap; margin-bottom:24px; }
.sanctions-search input { background:#0e0e0e; border:1px solid #222; color:var(--paper); font-family:'Inter',sans-serif; font-size:13px; font-weight:300; padding:10px 16px; outline:none; width:280px; transition:border 0.2s; }
.sanctions-search input:focus { border-color:#555; }
.sanctions-search input::placeholder { color:#444; }
[data-theme="light"] .sanctions-search input { background:#e8e3d8; border-color:#ccc5b5; }
</style>"""

SEARCH_HTML_RU = """<div class="sanctions-search">
  <input type="text" id="sanction-q" placeholder="Поиск по имени…" oninput="filterSanctions(this.value)" autocomplete="off">
</div>"""

SEARCH_HTML_EN = """<div class="sanctions-search">
  <input type="text" id="sanction-q" placeholder="Search by name…" oninput="filterSanctions(this.value)" autocomplete="off">
</div>"""

SEARCH_JS = """<script>
function filterSanctions(q){
  q=q.toLowerCase();
  document.querySelectorAll('.sanctions-table tbody tr').forEach(function(tr){
    tr.style.display=tr.textContent.toLowerCase().includes(q)?'':'none';
  });
}
</script>"""

for fname, search_html in [('sanctions.html', SEARCH_HTML_RU), ('sanctions-en.html', SEARCH_HTML_EN)]:
    p = BASE / fname
    html = p.read_text('utf-8')
    if 'sanction-q' in html:
        print(f'  skip {fname}')
        continue
    # Add CSS before </style> first occurrence
    html = html.replace('</head>', SEARCH_CSS + '\n</head>', 1)
    # Add search box before first <table class="sanctions-table">
    html = html.replace('<table class="sanctions-table">', search_html + '\n<table class="sanctions-table">', 1)
    # Add JS before </body>
    html = html.replace('</body>', SEARCH_JS + '\n</body>', 1)
    p.write_text(html, 'utf-8')
    print(f'  ✓ {fname}: search added')

print('\n✓ All done.')
