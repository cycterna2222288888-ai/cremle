import glob
import re

ru_nav = """<nav class="section-nav">
  <a href="quotes.html">Цитатник</a>
  <a href="sanctions.html">Санкции</a>
  <a href="timeline.html">Хронология</a>
  <a href="connections.html">Связи</a>
  <a href="compare.html">Сравнить</a>
  <a href="media-empire.html">Медиаимперия</a>
  <a href="assets.html">Владения</a>
  <a href="glossary.html">Глоссарий</a>
  <a href="sources.html">Источники</a>
  <a href="about.html">О проекте</a>
</nav>"""

en_nav = """<nav class="section-nav">
  <a href="quotes-en.html">Quotes</a>
  <a href="sanctions-en.html">Sanctions</a>
  <a href="timeline-en.html">Timeline</a>
  <a href="connections-en.html">Connections</a>
  <a href="compare-en.html">Compare</a>
  <a href="media-empire-en.html">Media Empire</a>
  <a href="assets-en.html">Assets</a>
  <a href="glossary-en.html">Glossary</a>
  <a href="sources-en.html">Sources</a>
  <a href="about-en.html">About</a>
</nav>"""

css_block = """  .section-nav {
    border-bottom: 1px solid var(--rule);
    padding: 0 60px;
    display: flex;
    gap: 0;
    overflow-x: auto;
    background: var(--ink);
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
  }
  .section-nav::-webkit-scrollbar { display: none; }
  .section-nav a {
    font-size: 10px;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--light-gray);
    text-decoration: none;
    padding: 16px 20px;
    white-space: nowrap;
    border-bottom: 2px solid transparent;
    transition: color 0.2s, border-color 0.2s;
  }
  .section-nav a:hover { color: var(--paper); }
  .section-nav a.active { color: var(--paper); border-bottom-color: var(--red); }
  @media (max-width: 768px) { .section-nav { padding: 0 16px; } .section-nav a { padding: 12px 12px; font-size: 9px; } }
"""

files = glob.glob("*.html")

for f in files:
    # skip individual person dossiers, index files, submit files, and 404
    if f in ['index.html', 'index-en.html', 'submit.html', 'submit-en.html', '404.html', '404-en.html']:
        continue
    
    # only apply to known "section" pages
    if not any(x in f for x in ['quotes', 'sanctions', 'timeline', 'connections', 'compare', 'media-empire', 'assets', 'glossary', 'sources', 'about', 'tv-propaganda']):
        continue

    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    # 1. Update existing section-nav
    nav_to_insert = en_nav if '-en.html' in f else ru_nav
    
    if '<nav class="section-nav">' in content:
        # replace existing section-nav
        content = re.sub(r'<nav class="section-nav">.*?</nav>', nav_to_insert, content, flags=re.DOTALL)
    elif 'class="topbar"' in content:
        # add section-nav below topbar
        content = re.sub(r'(<div class="topbar">.*?</div>\n)', r'\1\n' + nav_to_insert + '\n', content, flags=re.DOTALL, count=1)
    
    # 2. Add active class to the current page link
    base_name = f
    content = content.replace(f'<a href="{base_name}">', f'<a href="{base_name}" class="active">')
    
    # 3. Ensure CSS exists
    if '.section-nav {' not in content:
        # insert before </style>
        content = content.replace('</style>', css_block + '</style>', 1)
        
    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

print("Navigation updated successfully.")