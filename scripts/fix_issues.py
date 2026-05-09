#!/usr/bin/env python3
"""Fix all outstanding issues: hreflang x-default, connections, mobile CSS."""

import re, pathlib

BASE = pathlib.Path(__file__).parent

NEW_PERSONS = ['nebenzya', 'patrushev', 'matvienko', 'slutsky', 'emizulina']
BASE_URL = 'https://cycterna2222288888-ai.github.io/cremle'

# ── 1. hreflang x-default on 10 new dossiers ─────────────────────────────────
print('=== 1. hreflang x-default ===')
for name in NEW_PERSONS:
    for suffix, xdef_slug in [('.html', name), ('-en.html', name)]:
        p = BASE / (name + suffix)
        if not p.exists():
            continue
        html = p.read_text('utf-8')
        if 'x-default' in html:
            print(f'  skip {p.name} (already has x-default)')
            continue
        xdef = f'\n<link rel="alternate" hreflang="x-default" href="{BASE_URL}/{xdef_slug}.html">'
        html = html.replace(
            f'<link rel="alternate" hreflang="en" href="{BASE_URL}/{name}-en.html">',
            f'<link rel="alternate" hreflang="en" href="{BASE_URL}/{name}-en.html">{xdef}'
        )
        p.write_text(html, 'utf-8')
        print(f'  ✓ {p.name}')

# ── 2. connections.html — add missing links ───────────────────────────────────
print('\n=== 2. connections.html links ===')

NEW_LINKS_RU = """\
    {source:'nebenzya',     target:'kremlin',   type:'работа',   w:4},
    {source:'patrushev',    target:'kremlin',   type:'работа',   w:4},
    {source:'matvienko',    target:'kremlin',   type:'работа',   w:3},
    {source:'slutsky',      target:'kremlin',   type:'работа',   w:2},
    {source:'emizulina',    target:'kremlin',   type:'работа',   w:2},
    {source:'emizulina',    target:'mizulina',  type:'семья',    w:3},
    {source:'patrushev',    target:'medvedev',  type:'влияние',  w:2},
    {source:'matvienko',    target:'medvedev',  type:'влияние',  w:2},
    {source:'slutsky',      target:'gosduma',   type:'работа',   w:3},"""

NEW_LINKS_EN = """\
    {source:'nebenzya',     target:'kremlin',   type:'работа',   w:4},
    {source:'patrushev',    target:'kremlin',   type:'работа',   w:4},
    {source:'matvienko',    target:'kremlin',   type:'работа',   w:3},
    {source:'slutsky',      target:'kremlin',   type:'работа',   w:2},
    {source:'emizulina',    target:'kremlin',   type:'работа',   w:2},
    {source:'emizulina',    target:'mizulina',  type:'семья',    w:3},
    {source:'patrushev',    target:'medvedev',  type:'влияние',  w:2},
    {source:'matvienko',    target:'medvedev',  type:'влияние',  w:2},
    {source:'slutsky',      target:'gosduma',   type:'работа',   w:3},"""

for fname, new_links in [('connections.html', NEW_LINKS_RU), ('connections-en.html', NEW_LINKS_EN)]:
    p = BASE / fname
    html = p.read_text('utf-8')
    # Find current block for new persons and replace it
    old_pat = re.compile(
        r"(\{source:'nebenzya'.*?\{source:'emizulina',\s*target:'mizulina'.*?w:\d+\})",
        re.DOTALL
    )
    new_html, n = old_pat.subn(new_links.strip(), html)
    if n:
        p.write_text(new_html, 'utf-8')
        print(f'  ✓ {fname}: replaced links block')
    else:
        print(f'  ✗ {fname}: pattern not matched')

# ── 3. Mobile CSS improvements ────────────────────────────────────────────────
print('\n=== 3. Mobile CSS ===')

MOBILE_PATCH_DOSSIER = """
  @media (max-width: 480px) {
    .hero-left { padding: 36px 20px; }
    .hero-left h1 { font-size: clamp(1.6rem, 7vw, 2.4rem); }
    .container { padding: 0 20px; }
    .section { padding: 60px 0; }
    .section-header { margin-bottom: 36px; }
    .properties-row { grid-template-columns: 1fr; }
    .stamp { font-size: 9px; letter-spacing: 0.15em; }
    .quote-text { font-size: 15px; }
    .timeline-year { font-size: 11px; min-width: 52px; }
    .topbar-left a { font-size: 9px; }
  }"""

MOBILE_PATCH_INDEX = """
  @media (max-width: 480px) {
    .masthead { padding: 40px 20px 28px; }
    .masthead h1 { font-size: clamp(2rem, 8vw, 3rem); }
    .stats-bar { grid-template-columns: 1fr 1fr; }
    .nav-pages { overflow-x: auto; flex-wrap: nowrap; padding-bottom: 4px; -webkit-overflow-scrolling: touch; }
    .flt-btn { white-space: nowrap; flex-shrink: 0; }
    .card-num { font-size: 9px; }
    .card-name { font-size: 1rem; }
    .topbar a { font-size: 9px; }
  }"""

# Dossier pages: insert before </style>
dossier_files = []
for name in NEW_PERSONS:
    dossier_files += [name + '.html', name + '-en.html']
# Add a sample of old dossiers too (all of them)
import glob
for f in glob.glob(str(BASE / '*.html')):
    fname = pathlib.Path(f).name
    if fname not in dossier_files and fname not in [
        'index.html', 'index-en.html', 'submit.html', 'submit-en.html',
        'about.html', 'about-en.html', 'timeline.html', 'timeline-en.html',
        'connections.html', 'connections-en.html', 'quotes.html', 'quotes-en.html',
        'sources.html', 'sources-en.html', 'glossary.html', 'glossary-en.html',
        'sanctions.html', 'sanctions-en.html', 'media-empire.html', 'media-empire-en.html',
        'compare.html', 'compare-en.html', '404.html', '404-en.html',
    ] and fname.endswith('.html') and 'og-' not in fname and fname != 'googlec2551b38ace60f0f.html':
        dossier_files.append(fname)

patched_dossiers = 0
for fname in dossier_files:
    p = BASE / fname
    if not p.exists():
        continue
    html = p.read_text('utf-8')
    if 'max-width: 480px' in html:
        continue
    if '</style>' not in html:
        continue
    # Insert before first </style>
    html = html.replace('</style>', MOBILE_PATCH_DOSSIER + '\n</style>', 1)
    p.write_text(html, 'utf-8')
    patched_dossiers += 1

print(f'  ✓ {patched_dossiers} dossier pages patched with 480px breakpoint')

# Index pages
for fname in ['index.html', 'index-en.html']:
    p = BASE / fname
    html = p.read_text('utf-8')
    if 'max-width: 480px' in html:
        print(f'  skip {fname}')
        continue
    html = html.replace('</style>', MOBILE_PATCH_INDEX + '\n</style>', 1)
    p.write_text(html, 'utf-8')
    print(f'  ✓ {fname}')

print('\n✓ All done.')
