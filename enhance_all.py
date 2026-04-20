#!/usr/bin/env python3
"""
Adds to all dossier pages:
 - Scroll-to-top button (EN + RU, 46 pages)
 - EN Sources section (23 EN dossier pages)
"""
import re, os

BASE = '/Users/petrdracev/Desktop/proj/cremle/'

# ── Scroll-to-top CSS + HTML + JS ──────────────────────────────────────────
SCROLLTOP_CSS = """
  .back-to-top {
    position: fixed;
    bottom: 32px;
    right: 32px;
    width: 44px;
    height: 44px;
    background: var(--red);
    color: var(--paper);
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.3s, visibility 0.3s;
    z-index: 500;
  }
  .back-to-top.visible { opacity: 1; visibility: visible; }
  .back-to-top:hover { background: #6e1414; }
  @media (max-width: 768px) { .back-to-top { bottom: 20px; right: 16px; } }
"""

SCROLLTOP_HTML = '<button class="back-to-top" id="back-to-top" aria-label="Back to top">↑</button>\n'

SCROLLTOP_JS = """<script>
(function(){
  var btn = document.getElementById('back-to-top');
  if (!btn) return;
  window.addEventListener('scroll', function(){
    if (window.scrollY > 300) { btn.classList.add('visible'); }
    else { btn.classList.remove('visible'); }
  }, { passive: true });
  btn.addEventListener('click', function(){
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
})();
</script>
"""

# ── Sources data per person ─────────────────────────────────────────────────
# Keys: eu, eu_note, us, us_note, uk, uk_note, wiki, extra
SOURCES = {
  'solovyov': {
    'name': 'Vladimir Solovyov',
    'eu': 'February 28, 2022 — first EU package for supporting the war.',
    'us': 'Included in the OFAC SDN List as a disinformation spreader.',
    'uk': '2022 — UK Global Human Rights Sanctions Regulations.',
    'wiki': 'ru.wikipedia.org/wiki/Соловьёв,_Владимир_Рудольфович',
    'extra': 'Investigation: Forbes Russia reported on his villas in Lake Como (Italy), seized under EU sanctions.'
  },
  'skabeeva': {
    'name': 'Olga Skabeeva',
    'eu': '2022 — for systematic disinformation and war propaganda.',
    'us': None,
    'uk': '2022 — UK designation for spreading pro-Kremlin narratives.',
    'wiki': 'ru.wikipedia.org/wiki/Скабеева,_Ольга_Владимировна',
    'extra': None
  },
  'simonyan': {
    'name': 'Margarita Simonyan',
    'eu': '2022 — Editor-in-Chief of RT, designated for disinformation.',
    'us': '2022 — OFAC designation for RT-linked influence operations.',
    'uk': '2022 — FCDO designation for RT propaganda activities.',
    'wiki': 'ru.wikipedia.org/wiki/Симоньян,_Маргарита_Симоновна',
    'extra': 'RT (Russia Today) was banned from YouTube and EU platforms in March 2022.'
  },
  'kiselyov': {
    'name': 'Dmitry Kiselyov',
    'eu': '2014 — among the first wave after Crimea annexation. Extended 2022.',
    'us': '2022 — OFAC SDN List for disinformation and propaganda activities.',
    'uk': '2022 — FCDO designation.',
    'wiki': 'ru.wikipedia.org/wiki/Киселёв,_Дмитрий_Константинович',
    'extra': 'Rossia Segodnya — his state media group — operates TASS, RIA Novosti, Sputnik.'
  },
  'popov': {
    'name': 'Vladimir Popov',
    'eu': '2022 — for spreading pro-war narratives on Rossiya-1.',
    'us': None,
    'uk': None,
    'wiki': 'ru.wikipedia.org/wiki/Попов,_Владимир_Викторович_(журналист)',
    'extra': None
  },
  'sheynin': {
    'name': 'Artyom Sheynin',
    'eu': '2022 — for hosting pro-war talk shows on Channel One.',
    'us': None,
    'uk': None,
    'wiki': 'ru.wikipedia.org/wiki/Шейнин,_Артём_Геннадьевич',
    'extra': None
  },
  'tolstoy': {
    'name': 'Pyotr Tolstoy',
    'eu': '2022 — designated for anti-Ukrainian rhetoric and EU denialism.',
    'us': None,
    'uk': '2022 — FCDO designation.',
    'wiki': 'ru.wikipedia.org/wiki/Толстой,_Пётр_Олегович',
    'extra': None
  },
  'norkin': {
    'name': 'Andrey Norkin',
    'eu': '2022 — for systematically denying Ukrainian statehood on NTV.',
    'us': None,
    'uk': None,
    'wiki': 'ru.wikipedia.org/wiki/Норкин,_Андрей_Владимирович',
    'extra': None
  },
  'keosayan': {
    'name': 'Tigran Keosayan',
    'eu': '2022 — designated as director of pro-war propaganda films.',
    'us': None,
    'uk': None,
    'wiki': 'ru.wikipedia.org/wiki/Кеосаян,_Тигран_Эдмондович',
    'extra': None
  },
  'andreyeva': {
    'name': 'Ekaterina Andreyeva',
    'eu': '2014 — initial designation for coverage of Maidan and Crimea. Extended 2022.',
    'us': None,
    'uk': '2022 — FCDO designation.',
    'wiki': 'ru.wikipedia.org/wiki/Андреева,_Екатерина_Васильевна_(журналист)',
    'extra': None
  },
  'leontyev': {
    'name': 'Mikhail Leontyev',
    'eu': '2022 — for anti-Western rhetoric on Kommersant TV and Rossiya-1.',
    'us': None,
    'uk': '2022 — FCDO designation.',
    'wiki': 'ru.wikipedia.org/wiki/Леонтьев,_Михаил_Владимирович',
    'extra': None
  },
  'mamontov': {
    'name': 'Arkady Mamontov',
    'eu': '2022 — for spreading conspiracy theories and disinformation.',
    'us': None,
    'uk': None,
    'wiki': 'ru.wikipedia.org/wiki/Мамонтов,_Аркадий_Викторович',
    'extra': None
  },
  'medinsky': {
    'name': 'Vladimir Medinsky',
    'eu': '2022 — for rewriting history and cultural weaponization.',
    'us': None,
    'uk': '2022 — FCDO designation.',
    'wiki': 'ru.wikipedia.org/wiki/Мединский,_Владимир_Ростиславович',
    'extra': 'Led Russian delegation at Belarus peace talks; resigned from Culture Ministry 2020.'
  },
  'prilepin': {
    'name': 'Zakhar Prilepin',
    'eu': '2022 — for fighting in Donbas and incitement through literary prestige.',
    'us': None,
    'uk': None,
    'wiki': 'ru.wikipedia.org/wiki/Прилепин,_Захар',
    'extra': 'Survived a car bomb attack in May 2023; investigation ongoing.'
  },
  'dugin': {
    'name': 'Alexander Dugin',
    'eu': '2022 — for ideological foundation of Russian aggression.',
    'us': None,
    'uk': '2022 — FCDO designation.',
    'wiki': 'ru.wikipedia.org/wiki/Дугин,_Александр_Гельевич',
    'extra': 'His daughter Darya Dugina was killed in a car bomb in August 2022.'
  },
  'mikhalkov': {
    'name': 'Nikita Mikhalkov',
    'eu': '2022 — for Besogon TV conspiracy content and support of the war.',
    'us': None,
    'uk': None,
    'wiki': 'ru.wikipedia.org/wiki/Михалков,_Никита_Сергеевич',
    'extra': None
  },
  'korchevnikov': {
    'name': 'Boris Korchevnikov',
    'eu': '2022 — for hosting Kremlin propaganda and religious war framing.',
    'us': None,
    'uk': None,
    'wiki': 'ru.wikipedia.org/wiki/Корчевников,_Борис_Вячеславович',
    'extra': None
  },
  'krasovsky': {
    'name': 'Anton Krasovsky',
    'eu': '2022 — suspended from RT after calling to drown Ukrainian children; sanctions maintained.',
    'us': None,
    'uk': None,
    'wiki': 'ru.wikipedia.org/wiki/Красовский,_Антон_Николаевич',
    'extra': 'Statement calling for drowning of Ukrainian children recorded October 22, 2022 on Solovyov Live. RT suspended him temporarily then reinstated.'
  },
  'medvedev': {
    'name': 'Dmitry Medvedev',
    'eu': '2022 — for escalation rhetoric and political support of the invasion.',
    'us': '2022 — OFAC SDN List.',
    'uk': '2022 — FCDO designation.',
    'wiki': 'ru.wikipedia.org/wiki/Медведев,_Дмитрий_Анатольевич',
    'extra': 'Additional designations by Canada, Australia, Japan — 2022. Former President (2008–2012) and Prime Minister.'
  },
  'kadyrov': {
    'name': 'Ramzan Kadyrov',
    'eu': '2023 — for military participation in Ukraine and human rights violations.',
    'us': '2020 — Magnitsky Act designation for gross human rights violations.',
    'uk': '2022 — FCDO designation.',
    'wiki': 'ru.wikipedia.org/wiki/Кадыров,_Рамзан_Ахматович',
    'extra': 'Human Rights Watch and Memorial have documented hundreds of cases of torture and enforced disappearances in Chechnya.'
  },
  'malofeev': {
    'name': 'Konstantin Malofeev',
    'eu': '2014 — for financing separatist forces in Donbas. Extended 2022.',
    'us': '2014 — OFAC designation for destabilizing Ukraine.',
    'uk': '2022 — FCDO designation.',
    'wiki': 'ru.wikipedia.org/wiki/Малофеев,_Константин_Валерьевич',
    'extra': 'Canada also designated him in 2022. Linked to Igor Girkin (Strelkov) through Donbas operations.'
  },
  'nikonov': {
    'name': 'Vyacheslav Nikonov',
    'eu': '2022 — for spreading state propaganda in academic packaging.',
    'us': None,
    'uk': '2022 — FCDO designation.',
    'wiki': 'ru.wikipedia.org/wiki/Никонов,_Вячеслав_Алексеевич',
    'extra': 'Grandson of Vyacheslav Molotov, co-signatory of the Molotov-Ribbentrop Pact.'
  },
  'poddubny': {
    'name': 'Yevgeny Poddubny',
    'eu': '2022 — for embedding state war narrative into field reporting.',
    'us': None,
    'uk': None,
    'wiki': 'ru.wikipedia.org/wiki/Поддубный,_Евгений_Валерьевич_(журналист)',
    'extra': None
  },
}

SOURCES_CSS = """
  .sources-section { padding: 60px 0; border-bottom: 1px solid var(--rule); }
  .sources-grid-en { display: grid; grid-template-columns: 1fr 1fr; gap: 2px; background: var(--rule); margin-top: 32px; }
  .source-card-en { background: var(--ink); padding: 28px 32px; }
  .sc-type-en { font-size: 9px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--red); margin-bottom: 8px; }
  .sc-title-en { font-family: 'Playfair Display', serif; font-size: 14px; color: var(--paper); margin-bottom: 6px; }
  .sc-note-en { font-size: 11px; color: #555; line-height: 1.7; margin-top: 4px; }
  .sc-note-en a { color: #555; }
  .sc-note-en a:hover { color: var(--light-gray); }
  @media (max-width: 900px) { .sources-grid-en { grid-template-columns: 1fr; } .sources-section { padding: 40px 0; } }
"""

def build_sources_section(slug):
    d = SOURCES.get(slug)
    if not d:
        return ''
    cards = []

    if d.get('eu'):
        cards.append(f'''      <div class="source-card-en">
        <div class="sc-type-en">Sanctions · EU</div>
        <div class="sc-title-en">EUR-Lex — Official EU Sanctions Register</div>
        <div class="sc-note-en">{d['eu']}<br>eur-lex.europa.eu — free public access.</div>
      </div>''')

    if d.get('us'):
        cards.append(f'''      <div class="source-card-en">
        <div class="sc-type-en">Sanctions · USA</div>
        <div class="sc-title-en">OFAC SDN List — U.S. Treasury Department</div>
        <div class="sc-note-en">{d['us']}<br>ofac.treas.gov — public registry.</div>
      </div>''')

    if d.get('uk'):
        cards.append(f'''      <div class="source-card-en">
        <div class="sc-type-en">Sanctions · UK</div>
        <div class="sc-title-en">FCDO · UK Sanctions List</div>
        <div class="sc-note-en">{d['uk']}<br>gov.uk/government/collections/uk-sanctions</div>
      </div>''')

    cards.append(f'''      <div class="source-card-en">
        <div class="sc-type-en">Biography</div>
        <div class="sc-title-en">Wikipedia · Wikimedia Commons</div>
        <div class="sc-note-en">Biographical facts, dates, career history. Photos from Wikimedia Commons (CC license).<br>{d['wiki']}</div>
      </div>''')

    if d.get('extra'):
        cards.append(f'''      <div class="source-card-en">
        <div class="sc-type-en">Investigation</div>
        <div class="sc-title-en">Open Sources &amp; Investigative Reports</div>
        <div class="sc-note-en">{d['extra']}</div>
      </div>''')

    cards_html = '\n'.join(cards)
    return f'''\n<div class="sources-section">
  <div class="container">
    <div class="section-header">
      <span class="section-num">05</span>
      <h2 class="section-title">Sources</h2>
    </div>
    <p style="font-size:13px;color:#555;margin-bottom:0;line-height:1.8">All claims in this dossier are based on open public sources. Facts marked <span class="badge badge-fact" style="font-size:9px">Fact</span> have direct primary sources. Marked <span class="badge badge-interp" style="font-size:9px">Interp.</span> are editorial assessments of documented events.</p>
  </div>
  <div class="sources-grid-en">
{cards_html}
  </div>
</div>\n'''

EN_SLUGS = [
    'solovyov','skabeeva','simonyan','kiselyov','popov','sheynin','tolstoy',
    'norkin','keosayan','andreyeva','leontyev','mamontov','medinsky','prilepin',
    'dugin','mikhalkov','korchevnikov','krasovsky','medvedev','kadyrov',
    'malofeev','nikonov','poddubny'
]

RU_SLUGS = EN_SLUGS  # same set

def inject_css(html, extra_css):
    """Insert CSS before closing </style> of the first <style> block."""
    return html.replace('</style>', extra_css + '\n</style>', 1)

def process_en_page(slug):
    path = BASE + slug + '-en.html'
    if not os.path.exists(path):
        print(f'  SKIP (not found): {path}')
        return

    with open(path, encoding='utf-8') as f:
        html = f.read()

    changed = False

    # 1. Add sources CSS if not already there
    if 'sources-section' not in html:
        html = inject_css(html, SOURCES_CSS)
        changed = True

    # 2. Add scroll-to-top CSS if not there
    if 'back-to-top' not in html:
        html = inject_css(html, SCROLLTOP_CSS)
        changed = True

    # 3. Add sources section HTML before share-bar
    if 'sources-section' not in html or '<div class="sources-section">' not in html:
        sources_html = build_sources_section(slug)
        if sources_html:
            # Insert before share-bar or footer
            if '<div class="share-bar">' in html:
                html = html.replace('<div class="share-bar">', sources_html + '<div class="share-bar">', 1)
            elif '<a class="next-dosye"' in html:
                html = html.replace('<a class="next-dosye"', sources_html + '<a class="next-dosye"', 1)
            elif '<div class="footer">' in html:
                html = html.replace('<div class="footer">', sources_html + '<div class="footer">', 1)
            changed = True

    # 4. Add scroll-to-top button before </body>
    if 'back-to-top' not in html:
        html = html.replace('</body>', SCROLLTOP_HTML + SCROLLTOP_JS + '</body>')
        changed = True
    elif 'id="back-to-top"' not in html:
        html = html.replace('</body>', SCROLLTOP_HTML + SCROLLTOP_JS + '</body>')
        changed = True

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'  ✓ EN: {slug}-en.html')
    else:
        print(f'  - EN already done: {slug}')

def process_ru_page(slug):
    path = BASE + slug + '.html'
    if not os.path.exists(path):
        print(f'  SKIP (not found): {path}')
        return

    with open(path, encoding='utf-8') as f:
        html = f.read()

    changed = False

    # Add scroll-to-top CSS if not there
    if 'back-to-top' not in html:
        html = inject_css(html, SCROLLTOP_CSS)
        changed = True

    # Add scroll-to-top button before </body>
    if 'id="back-to-top"' not in html:
        html = html.replace('</body>', SCROLLTOP_HTML + SCROLLTOP_JS + '</body>')
        changed = True

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'  ✓ RU: {slug}.html')
    else:
        print(f'  - RU already done: {slug}')

print('Processing EN dossier pages...')
for slug in EN_SLUGS:
    process_en_page(slug)

print('\nProcessing RU dossier pages...')
for slug in RU_SLUGS:
    process_ru_page(slug)

print('\nDone.')
