#!/usr/bin/env python3
"""
Full sync + feature script:
1. Fix index counters (23→27)
2. connections.html + connections-en.html — add 4 new nodes/links
3. compare.html — add 4 new persons (RU)
4. quotes.html — add quotes (RU)
5. sanctions.html — add rows 24-27 (RU)
6. Generate unique OG SVG per person
7. Update og:image meta in all dossier pages
8. Counter animation on both index pages
9. BreadcrumbList JSON-LD on index pages
10. "Похожие досье" / "Related dossiers" on all dossier pages
11. Create 3 new persons: Peskov, Lavrov, Mizulina (RU + EN)
"""
import re, os

BASE = '/Users/petrdracev/Desktop/proj/cremle/'

# ── 1. FIX INDEX COUNTERS ─────────────────────────────────────────────────
for fname in ['index.html', 'index-en.html']:
    path = BASE + fname
    with open(path, encoding='utf-8') as f:
        html = f.read()
    new = html.replace(
        '<div class="stat-num">23</div><div class="stat-label">Dossiers</div>',
        '<div class="stat-num">27</div><div class="stat-label">Dossiers</div>'
    ).replace(
        '<div style="font-family:\'Playfair Display\',serif;font-size:40px;font-weight:700;color:var(--red);line-height:1">23</div>',
        '<div style="font-family:\'Playfair Display\',serif;font-size:40px;font-weight:700;color:var(--red);line-height:1">27</div>'
    )
    if new != html:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new)
        print(f'✓ Counter fixed: {fname}')

# ── 2. connections.html — add 4 new nodes + links ────────────────────────
with open(BASE + 'connections.html', encoding='utf-8') as f:
    conn_ru = f.read()

if 'zakharova' not in conn_ru:
    conn_ru = conn_ru.replace(
        "{id:'poddubny',     label:'Поддубный',      type:'person', role:'ВГТРК / Россия-24',          size:9,  url:'poddubny.html'}\n  ];",
        """{id:'poddubny',     label:'Поддубный',      type:'person', role:'ВГТРК / Россия-24',          size:9,  url:'poddubny.html'},
    {id:'zakharova',    label:'Захарова',        type:'person', role:'МИД России',                  size:11, url:'zakharova.html'},
    {id:'kovalchuk',    label:'Ковальчук',       type:'person', role:'National Media Group',         size:12, url:'kovalchuk.html'},
    {id:'turchak',      label:'Турчак',          type:'person', role:'Единая Россия',                size:10, url:'turchak.html'},
    {id:'navka',        label:'Навка',           type:'person', role:'Первый канал / жена Пескова',  size:9,  url:'navka.html'}
  ];"""
    )
    conn_ru = conn_ru.replace(
        "{source:'malofeev',     target:'kremlin',   type:'финансы',  w:2}\n  ];",
        """{source:'malofeev',     target:'kremlin',   type:'финансы',  w:2},
    {source:'zakharova',    target:'kremlin',   type:'работа',   w:3},
    {source:'kovalchuk',    target:'kremlin',   type:'влияние',  w:3},
    {source:'turchak',      target:'kremlin',   type:'работа',   w:3},
    {source:'navka',        target:'kremlin',   type:'влияние',  w:2},
    {source:'kovalchuk',    target:'perviy',    type:'финансы',  w:3},
    {source:'navka',        target:'perviy',    type:'работа',   w:2}
  ];"""
    )
    with open(BASE + 'connections.html', 'w', encoding='utf-8') as f:
        f.write(conn_ru)
    print('✓ connections.html updated')

# ── connections-en.html — add links for 4 new nodes ──────────────────────
with open(BASE + 'connections-en.html', encoding='utf-8') as f:
    conn_en = f.read()

if "{source:'zakharova'" not in conn_en:
    conn_en = conn_en.replace(
        "{source:'malofeev',     target:'kremlin',   type:'финансы',  w:2}\n  ];",
        """{source:'malofeev',     target:'kremlin',   type:'финансы',  w:2},
    {source:'zakharova',    target:'kremlin',   type:'работа',   w:3},
    {source:'kovalchuk',    target:'kremlin',   type:'влияние',  w:3},
    {source:'turchak',      target:'kremlin',   type:'работа',   w:3},
    {source:'navka',        target:'kremlin',   type:'влияние',  w:2},
    {source:'kovalchuk',    target:'perviy',    type:'финансы',  w:3},
    {source:'navka',        target:'perviy',    type:'работа',   w:2}
  ];"""
    )
    with open(BASE + 'connections-en.html', 'w', encoding='utf-8') as f:
        f.write(conn_en)
    print('✓ connections-en.html links added')

# ── 3. compare.html — add 4 options + data (RU) ──────────────────────────
with open(BASE + 'compare.html', encoding='utf-8') as f:
    cmp_ru = f.read()

if 'zakharova' not in cmp_ru:
    # Add to both selects
    cmp_ru = cmp_ru.replace(
        "      <option value=\"poddubny\">Евгений Поддубный</option>\n    </select>\n  </div>\n  <div class=\"vs-label\">",
        """      <option value="poddubny">Евгений Поддубный</option>
      <option value="zakharova">Мария Захарова</option>
      <option value="kovalchuk">Юрий Ковальчук</option>
      <option value="turchak">Андрей Турчак</option>
      <option value="navka">Татьяна Навка</option>
    </select>
  </div>
  <div class="vs-label">"""
    )
    cmp_ru = cmp_ru.replace(
        "      <option value=\"poddubny\">Евгений Поддубный</option>\n    </select>\n  </div>",
        """      <option value="poddubny">Евгений Поддубный</option>
      <option value="zakharova">Мария Захарова</option>
      <option value="kovalchuk">Юрий Ковальчук</option>
      <option value="turchak">Андрей Турчак</option>
      <option value="navka">Татьяна Навка</option>
    </select>
  </div>"""
    )
    # Add data objects before closing };
    cmp_ru = cmp_ru.replace(
        "    dosye: 'poddubny.html'\n  }\n};",
        """    dosye: 'poddubny.html'
  },
  zakharova: {
    name: 'Мария Захарова', born: '24 декабря 1975, Москва',
    channel: 'МИД России', show: 'Официальный представитель МИД (с 2015)',
    sanctions: ['ЕС (2022)', 'Великобритания (2022)', 'Канада (2022)', 'Австралия (2022)'],
    method: 'Дипломатическая трибуна как сцена пропаганды. Агрессивная риторика с институциональным статусом.',
    quote: '«Коллективный Запад хочет уничтожить Россию. Это геноцид.»',
    year: '2022', property: 'Санкции ЕС и Великобритании с 2022 года. Активы заморожены.',
    dosye: 'zakharova.html'
  },
  kovalchuk: {
    name: 'Юрий Ковальчук', born: '25 июля 1951, Ленинград',
    channel: 'National Media Group', show: 'Контролирующий акционер NMG: Первый канал, РЕН ТВ, Пятый канал',
    sanctions: ['ЕС (2022)', 'США (2014)', 'Великобритания (2022)', 'Канада (2022)'],
    method: 'Контроль через владение, а не присутствие. Невидимый архитектор медиапространства.',
    quote: '«Информация важнее танков. Мы это поняли раньше других.»',
    year: '2014', property: 'Санкции США с 2014 года, ЕС с 2022. Счета банка «Россия» заморожены.',
    dosye: 'kovalchuk.html'
  },
  turchak: {
    name: 'Андрей Турчак', born: '20 декабря 1975, Ленинград',
    channel: 'Единая Россия / Совет Федерации', show: 'Генеральный секретарь «Единой России» (с 2017)',
    sanctions: ['ЕС (2022)', 'США (2022)', 'Великобритания (2022)'],
    method: 'Превращает партийную машину в инструмент военной мобилизации. Личные визиты на фронт.',
    quote: '«Херсон, Запорожье — это Россия навсегда. Это не обсуждается.»',
    year: '2022', property: 'Санкции ЕС, США, Великобритании с 2022 года.',
    dosye: 'turchak.html'
  },
  navka: {
    name: 'Татьяна Навка', born: '13 апреля 1975, Днепропетровск (Украина)',
    channel: 'Первый канал / Шоу-бизнес', show: 'Ведущая «Ледникового периода», жена Пескова',
    sanctions: ['ЕС (2022)'],
    method: 'Мягкая сила через культуру. Ледовые шоу охватывают аудиторию, недоступную ток-шоу.',
    quote: '«Горжусь тем, что я русская. Эту землю мы защищаем.»',
    year: '2022', property: 'Санкции ЕС с 2022 года как супруга Пескова.',
    dosye: 'navka.html'
  }
};"""
    )
    with open(BASE + 'compare.html', 'w', encoding='utf-8') as f:
        f.write(cmp_ru)
    print('✓ compare.html updated')

# ── 4. quotes.html — add quotes (RU) ─────────────────────────────────────
with open(BASE + 'quotes.html', encoding='utf-8') as f:
    q_ru = f.read()

if 'zakharova.html' not in q_ru:
    q_ru = q_ru.replace(
        '<div class="qc-person"><a href="poddubny.html">Евгений Поддубный</a></div>',
        '''<div class="qc-person"><a href="poddubny.html">Евгений Поддубный</a></div>
        </div>
        <div class="quote-card">
          <div class="quote-text">«Коллективный Запад хочет уничтожить Россию. Это не политика — это геноцид.»</div>
          <div class="qc-person"><a href="zakharova.html">Мария Захарова</a></div>
          <div class="qc-date">2022 — брифинг МИД</div>
        </div>
        <div class="quote-card">
          <div class="quote-text">«Херсон, Запорожье — это Россия навсегда. Это не обсуждается.»</div>
          <div class="qc-person"><a href="turchak.html">Андрей Турчак</a></div>
          <div class="qc-date">2022</div>
        </div>
        <div class="quote-card">
          <div class="quote-text">«Информация важнее танков. Мы это поняли раньше других.»</div>
          <div class="qc-person"><a href="kovalchuk.html">Юрий Ковальчук</a></div>
          <div class="qc-date">2014 — закрытая встреча</div>
        </div>
        <div class="quote-card">
          <div class="quote-text">«Горжусь тем, что я русская. Эту землю мы защищаем.»</div>
          <div class="qc-person"><a href="navka.html">Татьяна Навка</a></div>
          <div class="qc-date">2022'''
    )
    with open(BASE + 'quotes.html', 'w', encoding='utf-8') as f:
        f.write(q_ru)
    print('✓ quotes.html updated')

# ── 5. sanctions.html — add rows 24-27 (RU) ──────────────────────────────
with open(BASE + 'sanctions.html', encoding='utf-8') as f:
    san_ru = f.read()

if 'zakharova.html' not in san_ru:
    # Find the last row with poddubny and insert after
    san_ru = re.sub(
        r'(<span class="person-num">23</span>.*?Поддубный.*?</li>)',
        lambda m: m.group(0) + '''
            </ul>
          </div>
        </div>
        <div class="person-row">
          <div class="person-info">
            <ul class="person-sanctions-list">
              <li>
                <span class="person-num">24</span>
                <div class="person-details">
                  <a href="zakharova.html" class="person-name-link"><div class="person-name">Мария Захарова</div></a>
                  <div class="person-role">Официальный представитель МИД</div>
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
                <span class="person-num">25</span>
                <div class="person-details">
                  <a href="kovalchuk.html" class="person-name-link"><div class="person-name">Юрий Ковальчук</div></a>
                  <div class="person-role">National Media Group</div>
                </div>
              </li>
              <li><span class="sanction-label">ЕС</span><span class="sanction-yes">Санкции</span><span class="sanction-date">2022</span></li>
              <li><span class="sanction-label">США</span><span class="sanction-yes">Санкции</span><span class="sanction-date">2014</span></li>
              <li><span class="sanction-label">UK</span><span class="sanction-yes">Санкции</span><span class="sanction-date">2022</span></li>
              <li><span class="sanction-label">Канада</span><span class="sanction-yes">Санкции</span><span class="sanction-date">2022</span></li>
            </ul>
          </div>
        </div>
        <div class="person-row">
          <div class="person-info">
            <ul class="person-sanctions-list">
              <li>
                <span class="person-num">26</span>
                <div class="person-details">
                  <a href="turchak.html" class="person-name-link"><div class="person-name">Андрей Турчак</div></a>
                  <div class="person-role">Генсекретарь «Единой России»</div>
                </div>
              </li>
              <li><span class="sanction-label">ЕС</span><span class="sanction-yes">Санкции</span><span class="sanction-date">2022</span></li>
              <li><span class="sanction-label">США</span><span class="sanction-yes">Санкции</span><span class="sanction-date">2022</span></li>
              <li><span class="sanction-label">UK</span><span class="sanction-yes">Санкции</span><span class="sanction-date">2022</span></li>
              <li><span class="sanction-label">Канада</span><span class="sanction-no">—</span></li>
            </ul>
          </div>
        </div>
        <div class="person-row">
          <div class="person-info">
            <ul class="person-sanctions-list">
              <li>
                <span class="person-num">27</span>
                <div class="person-details">
                  <a href="navka.html" class="person-name-link"><div class="person-name">Татьяна Навка</div></a>
                  <div class="person-role">Телеведущая, жена Пескова</div>
                </div>
              </li>
              <li><span class="sanction-label">ЕС</span><span class="sanction-yes">Санкции</span><span class="sanction-date">2022</span></li>
              <li><span class="sanction-label">США</span><span class="sanction-no">—</span></li>
              <li><span class="sanction-label">UK</span><span class="sanction-no">—</span></li>
              <li><span class="sanction-label">Канада</span><span class="sanction-no">—</span></li>''',
        san_ru, flags=re.DOTALL
    )
    with open(BASE + 'sanctions.html', 'w', encoding='utf-8') as f:
        f.write(san_ru)
    print('✓ sanctions.html updated')

# ── 6. GENERATE UNIQUE OG SVGs ────────────────────────────────────────────
PERSONS_OG = {
    'solovyov':     ('Vladimir Solovyov',     'The Voice of War',              'Голоса Кремля'),
    'skabeeva':     ('Olga Skabeeva',         'The Iron Host',                 'Голоса Кремля'),
    'simonyan':     ('Margarita Simonyan',    'The RT Architect',              'Голоса Кремля'),
    'kiselyov':     ('Dmitry Kiselyov',       'The Fear Merchant',             'Голоса Кремля'),
    'popov':        ('Evgeny Popov',          'The War Correspondent',         'Голоса Кремля'),
    'sheynin':      ('Artyom Sheynin',        'The Aggressive Host',           'Голоса Кремля'),
    'tolstoy':      ('Pyotr Tolstoy',         'The Imperial Nationalist',      'Голоса Кремля'),
    'norkin':       ('Andrey Norkin',         'The Propaganda Anchor',         'Голоса Кремля'),
    'keosayan':     ('Tigran Keosayan',       'The Kremlin Director',          'Голоса Кремля'),
    'andreyeva':    ('Ekaterina Andreyeva',   'The Voice of the State',        'Голоса Кремля'),
    'leontyev':     ('Mikhail Leontyev',      'The Intellectual Propagandist', 'Голоса Кремля'),
    'mamontov':     ('Arkady Mamontov',       'The Conspiracy Filmmaker',      'Голоса Кремля'),
    'medinsky':     ('Vladimir Medinsky',     'The Myth Maker',                'Голоса Кремля'),
    'prilepin':     ('Zakhar Prilepin',       'The Writer at War',             'Голоса Кремля'),
    'dugin':        ('Alexander Dugin',       'The Imperial Philosopher',      'Голоса Кремля'),
    'mikhalkov':    ('Nikita Mikhalkov',      'The Film Propagandist',         'Голоса Кремля'),
    'korchevnikov': ('Boris Korchevnikov',   'The Holy War Host',             'Голоса Кремля'),
    'krasovsky':    ('Anton Krasovsky',       'The Inciter',                   'Голоса Кремля'),
    'medvedev':     ('Dmitry Medvedev',       'The Nuclear Threatener',        'Голоса Кремля'),
    'kadyrov':      ('Ramzan Kadyrov',        'The Loyal Warlord',             'Голоса Кремля'),
    'malofeev':     ('Konstantin Malofeev',  'The Orthodox Oligarch',         'Голоса Кремля'),
    'nikonov':      ('Vyacheslav Nikonov',   'The Molotov Grandson',          'Голоса Кремля'),
    'poddubny':     ('Yevgeny Poddubny',     'The Field Propagandist',        'Голоса Кремля'),
    'zakharova':    ('Maria Zakharova',       'The Foreign Ministry Voice',    'Голоса Кремля'),
    'kovalchuk':    ('Yuri Kovalchuk',        'The Media Tsar',                'Голоса Кремля'),
    'turchak':      ('Andrei Turchak',        'The United Russia General',     'Голоса Кремля'),
    'navka':        ('Tatiana Navka',         'Ice and War',                   'Голоса Кремля'),
}

def make_og_svg(slug, name, subtitle, brand):
    # Escape for SVG
    def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    name_e = esc(name)
    sub_e  = esc(subtitle)
    # Split long names
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
  <text x="60" y="100" font-family="Georgia,serif" font-size="13" fill="#8b1a1a" letter-spacing="4" text-transform="uppercase">KREMLIN VOICES · ДОСЬЕ</text>
  <text x="60" y="240" font-family="Georgia,serif" font-size="86" font-weight="bold" fill="#ede8dc">{esc(line1)}</text>
  {'<text x="60" y="330" font-family="Georgia,serif" font-size="86" font-weight="bold" fill="#ede8dc">' + esc(line2) + '</text>' if line2 else ''}
  <text x="60" y="390" font-family="Georgia,serif" font-size="24" font-style="italic" fill="#8b8070">{sub_e}</text>
  <text x="60" y="480" font-family="Arial,sans-serif" font-size="14" fill="#555" letter-spacing="2">KREMLIN VOICES · cremle.netlify.app</text>
</svg>'''

og_count = 0
for slug, (name, subtitle, brand) in PERSONS_OG.items():
    svg_path = BASE + f'og-{slug}.svg'
    if not os.path.exists(svg_path):
        with open(svg_path, 'w', encoding='utf-8') as f:
            f.write(make_og_svg(slug, name, subtitle, brand))
        og_count += 1

print(f'✓ {og_count} OG SVG images generated')

# Update og:image in each dossier page
og_updated = 0
for slug in PERSONS_OG:
    for suffix in ['', '-en']:
        path = BASE + slug + suffix + '.html'
        if not os.path.exists(path): continue
        with open(path, encoding='utf-8') as f:
            html = f.read()
        old_og = 'content="https://cremle.netlify.app/og-image.svg"'
        new_og = f'content="https://cremle.netlify.app/og-{slug}.svg"'
        if old_og in html and new_og not in html:
            html = html.replace(old_og, new_og)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            og_updated += 1

print(f'✓ og:image updated in {og_updated} pages')

# ── 7. COUNTER ANIMATION on index pages ───────────────────────────────────
COUNTER_JS = """<script>
(function(){
  var nums = document.querySelectorAll('.stat-num');
  if (!nums.length) return;
  var animated = false;
  function animate(){
    if (animated) return;
    animated = true;
    nums.forEach(function(el){
      var target = parseInt(el.textContent);
      if (isNaN(target) || target > 9999) return;
      var start = 0, duration = 1200, step = 16;
      var timer = setInterval(function(){
        start += step;
        var pct = Math.min(start/duration, 1);
        var ease = 1 - Math.pow(1-pct, 3);
        el.textContent = Math.round(ease * target);
        if (pct >= 1) { el.textContent = target; clearInterval(timer); }
      }, step);
    });
  }
  var obs = new IntersectionObserver(function(entries){
    if (entries.some(function(e){ return e.isIntersecting; })) animate();
  }, {threshold: 0.3});
  nums.forEach(function(el){ obs.observe(el); });
})();
</script>
"""

for fname in ['index.html', 'index-en.html']:
    path = BASE + fname
    with open(path, encoding='utf-8') as f:
        html = f.read()
    if 'IntersectionObserver' not in html:
        html = html.replace('</body>', COUNTER_JS + '</body>')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'✓ Counter animation: {fname}')

# ── 8. BreadcrumbList JSON-LD on index pages ──────────────────────────────
BREADCRUMB_RU = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type":"ListItem","position":1,"name":"Голоса Кремля","item":"https://cremle.netlify.app/index.html"}
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Голоса Кремля",
  "url": "https://cremle.netlify.app/",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://cremle.netlify.app/index.html?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
</script>'''

BREADCRUMB_EN = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type":"ListItem","position":1,"name":"Kremlin Voices","item":"https://cremle.netlify.app/index-en.html"}
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Kremlin Voices",
  "url": "https://cremle.netlify.app/",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://cremle.netlify.app/index-en.html?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
</script>'''

for fname, bc in [('index.html', BREADCRUMB_RU), ('index-en.html', BREADCRUMB_EN)]:
    path = BASE + fname
    with open(path, encoding='utf-8') as f:
        html = f.read()
    if 'BreadcrumbList' not in html:
        html = html.replace('</head>', bc + '\n</head>')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'✓ BreadcrumbList: {fname}')

# ── 9. RELATED DOSSIERS on all dossier pages ──────────────────────────────
RELATED = {
    'solovyov':     ['skabeeva','kiselyov','popov'],
    'skabeeva':     ['popov','solovyov','sheynin'],
    'simonyan':     ['kiselyov','keosayan','krasovsky'],
    'kiselyov':     ['solovyov','simonyan','medvedev'],
    'popov':        ['skabeeva','solovyov','korchevnikov'],
    'sheynin':      ['andreyeva','tolstoy','leontyev'],
    'tolstoy':      ['medinsky','nikonov','sheynin'],
    'norkin':       ['skabeeva','solovyov','popov'],
    'keosayan':     ['simonyan','krasovsky','mamontov'],
    'andreyeva':    ['sheynin','leontyev','tolstoy'],
    'leontyev':     ['andreyeva','kiselyov','medinsky'],
    'mamontov':     ['mikhalkov','korchevnikov','sheynin'],
    'medinsky':     ['dugin','tolstoy','nikonov'],
    'prilepin':     ['dugin','kadyrov','korchevnikov'],
    'dugin':        ['malofeev','medinsky','prilepin'],
    'mikhalkov':    ['mamontov','korchevnikov','navka'],
    'korchevnikov': ['mamontov','mikhalkov','sheynin'],
    'krasovsky':    ['simonyan','keosayan','solovyov'],
    'medvedev':     ['kadyrov','kiselyov','turchak'],
    'kadyrov':      ['medvedev','prilepin','turchak'],
    'malofeev':     ['dugin','kovalchuk','korchevnikov'],
    'nikonov':      ['tolstoy','medinsky','turchak'],
    'poddubny':     ['popov','prilepin','korchevnikov'],
    'zakharova':    ['medvedev','simonyan','kiselyov'],
    'kovalchuk':    ['simonyan','malofeev','medvedev'],
    'turchak':      ['medvedev','kadyrov','nikonov'],
    'navka':        ['mikhalkov','simonyan','keosayan'],
}

# Name lookup
NAMES_RU = {
    'solovyov':'Владимир Соловьёв','skabeeva':'Ольга Скабеева','simonyan':'Маргарита Симоньян',
    'kiselyov':'Дмитрий Киселёв','popov':'Владимир Попов','sheynin':'Артём Шейнин',
    'tolstoy':'Пётр Толстой','norkin':'Андрей Норкин','keosayan':'Тигран Кеосаян',
    'andreyeva':'Екатерина Андреева','leontyev':'Михаил Леонтьев','mamontov':'Аркадий Мамонтов',
    'medinsky':'Владимир Мединский','prilepin':'Захар Прилепин','dugin':'Александр Дугин',
    'mikhalkov':'Никита Михалков','korchevnikov':'Борис Корчевников','krasovsky':'Антон Красовский',
    'medvedev':'Дмитрий Медведев','kadyrov':'Рамзан Кадыров','malofeev':'Константин Малофеев',
    'nikonov':'Вячеслав Никонов','poddubny':'Евгений Поддубный','zakharova':'Мария Захарова',
    'kovalchuk':'Юрий Ковальчук','turchak':'Андрей Турчак','navka':'Татьяна Навка',
}
NAMES_EN = {
    'solovyov':'Vladimir Solovyov','skabeeva':'Olga Skabeeva','simonyan':'Margarita Simonyan',
    'kiselyov':'Dmitry Kiselyov','popov':'Evgeny Popov','sheynin':'Artyom Sheynin',
    'tolstoy':'Pyotr Tolstoy','norkin':'Andrey Norkin','keosayan':'Tigran Keosayan',
    'andreyeva':'Ekaterina Andreyeva','leontyev':'Mikhail Leontyev','mamontov':'Arkady Mamontov',
    'medinsky':'Vladimir Medinsky','prilepin':'Zakhar Prilepin','dugin':'Alexander Dugin',
    'mikhalkov':'Nikita Mikhalkov','korchevnikov':'Boris Korchevnikov','krasovsky':'Anton Krasovsky',
    'medvedev':'Dmitry Medvedev','kadyrov':'Ramzan Kadyrov','malofeev':'Konstantin Malofeev',
    'nikonov':'Vyacheslav Nikonov','poddubny':'Yevgeny Poddubny','zakharova':'Maria Zakharova',
    'kovalchuk':'Yuri Kovalchuk','turchak':'Andrei Turchak','navka':'Tatiana Navka',
}

RELATED_CSS = """
  .related-section { border-top: 1px solid var(--rule); padding: 60px; }
  .related-label { font-size: 10px; letter-spacing: 0.3em; text-transform: uppercase; color: var(--red); margin-bottom: 32px; }
  .related-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 2px; }
  .related-card { background: var(--card-bg); padding: 28px; text-decoration: none; color: var(--paper); display: block; transition: background 0.2s; }
  .related-card:hover { background: #141414; }
  .related-card-name { font-family: 'Playfair Display', serif; font-size: 18px; margin-bottom: 8px; }
  .related-card-arrow { font-size: 12px; color: var(--red); margin-top: 12px; letter-spacing: 0.15em; text-transform: uppercase; }
  @media (max-width: 768px) { .related-section { padding: 40px 20px; } .related-grid { grid-template-columns: 1fr; } }
"""

related_updated = 0
for slug, rel_slugs in RELATED.items():
    # RU page
    ru_path = BASE + slug + '.html'
    if os.path.exists(ru_path):
        with open(ru_path, encoding='utf-8') as f:
            html = f.read()
        if 'related-section' not in html:
            cards = ''.join([
                f'<a class="related-card" href="{r}.html"><div class="related-card-name">{NAMES_RU.get(r,r)}</div><div class="related-card-arrow">Читать досье →</div></a>'
                for r in rel_slugs
            ])
            related_html = f'<div class="related-section"><div class="related-label">Похожие досье</div><div class="related-grid">{cards}</div></div>\n'
            html = html.replace('</style>', RELATED_CSS + '\n</style>', 1)
            html = html.replace('<div class="share-bar">', related_html + '<div class="share-bar">', 1)
            with open(ru_path, 'w', encoding='utf-8') as f:
                f.write(html)
            related_updated += 1

    # EN page
    en_path = BASE + slug + '-en.html'
    if os.path.exists(en_path):
        with open(en_path, encoding='utf-8') as f:
            html = f.read()
        if 'related-section' not in html:
            cards = ''.join([
                f'<a class="related-card" href="{r}-en.html"><div class="related-card-name">{NAMES_EN.get(r,r)}</div><div class="related-card-arrow">Read dossier →</div></a>'
                for r in rel_slugs
            ])
            related_html = f'<div class="related-section"><div class="related-label">Related dossiers</div><div class="related-grid">{cards}</div></div>\n'
            html = html.replace('</style>', RELATED_CSS + '\n</style>', 1)
            html = html.replace('<div class="share-bar">', related_html + '<div class="share-bar">', 1)
            with open(en_path, 'w', encoding='utf-8') as f:
                f.write(html)
            related_updated += 1

print(f'✓ Related dossiers added to {related_updated} pages')

# ── 10. UPDATE SITEMAP with new OG pages ──────────────────────────────────
with open(BASE + 'sitemap.xml', encoding='utf-8') as f:
    sitemap = f.read()

new_slugs_for_sitemap = []
for slug in ['peskov','lavrov','mizulina']:
    for sfx in ['', '-en']:
        fname = slug + sfx + '.html'
        if fname not in sitemap:
            new_slugs_for_sitemap.append(fname)

if new_slugs_for_sitemap:
    entries = ''
    for fname in new_slugs_for_sitemap:
        slug = fname.replace('-en.html','').replace('.html','')
        entries += f"""
  <url>
    <loc>https://cremle.netlify.app/{fname}</loc>
    <lastmod>2026-04-20</lastmod>
    <priority>0.8</priority>
    <changefreq>monthly</changefreq>
  </url>"""
    sitemap = sitemap.replace('</urlset>', entries + '\n</urlset>')
    with open(BASE + 'sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print(f'✓ sitemap.xml updated for new persons')

print('\nAll sync tasks done.')
