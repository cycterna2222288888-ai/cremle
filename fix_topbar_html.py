import glob
import re

files = glob.glob("*.html")
patched = 0

for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Remove the bad CSS hack we added earlier
    if '<style id="topbar-mobile-fix">' in content:
        content = re.sub(r'<style id="topbar-mobile-fix">.*?</style>\n', '', content, flags=re.DOTALL)
    
    # Fix the old mobile-fixes if they exist, specifically flex-wrap: wrap !important
    if 'flex-wrap: wrap !important; gap: 10px !important;' in content:
        content = content.replace('flex-wrap: wrap !important; gap: 10px !important;', 'flex-wrap: nowrap !important; gap: 6px !important; overflow-x: auto !important;')

    # Ensure index.html specific flex-wrap is also removed or fixed
    if 'flex-wrap: wrap; gap: 4px;' in content:
        content = content.replace('flex-wrap: wrap; gap: 4px;', 'flex-wrap: nowrap; gap: 6px; overflow-x: auto;')

    # Add back a cleaner CSS fix
    clean_css = """<style id="topbar-clean-fix">
  @media (max-width: 480px) {
    .topbar { flex-wrap: nowrap !important; gap: 8px !important; overflow-x: auto !important; padding: 10px 16px !important; white-space: nowrap; -webkit-overflow-scrolling: touch; scrollbar-width: none; }
    .topbar::-webkit-scrollbar { display: none; }
    .topbar-left { flex-shrink: 0; }
    .topbar-right { flex-shrink: 0; gap: 8px !important; }
    .hide-on-mobile { display: none !important; }
    #theme-toggle { padding: 6px 8px !important; font-size: 9px !important; border: 1px solid var(--rule) !important; }
    .lang-switch a { padding: 6px 8px !important; font-size: 9px !important; }
    .report-link { display: none !important; }
  }
</style>
</head>"""

    if '<style id="topbar-clean-fix">' not in content:
        content = content.replace("</head>", clean_css)

    # Now replace the text inside topbar-left a
    def replacer(match):
        href = match.group(1)
        text = match.group(2)
        # if there's already a span, skip
        if '<span' in text:
            return match.group(0)
            
        text = text.replace('← ', '').replace('←', '')
        text = text.strip()
        
        if text:
            return f'<div class="topbar-left"><a href="{href}">← <span class="hide-on-mobile">{text}</span></a></div>'
        else:
            return match.group(0)

    # find <div class="topbar-left"><a href="...">TEXT</a></div>
    new_content = re.sub(r'<div class="topbar-left">\s*<a href="([^"]+)">(.*?)</a>\s*</div>', replacer, content)
    
    # Specifically for index.html spans in topbar
    if '<span>Досье · Открытые источники</span>' in new_content:
        new_content = new_content.replace('<span>Досье · Открытые источники</span>', '<span class="hide-on-mobile">Досье · Открытые источники</span>')
        new_content = new_content.replace('<span>Архив российской пропаганды</span>', '<span class="hide-on-mobile">Архив российской пропаганды</span>')
    if '<span>Dossiers · Open Sources</span>' in new_content:
        new_content = new_content.replace('<span>Dossiers · Open Sources</span>', '<span class="hide-on-mobile">Dossiers · Open Sources</span>')
        new_content = new_content.replace('<span>Archive of Russian Propaganda</span>', '<span class="hide-on-mobile">Archive of Russian Propaganda</span>')

    with open(f, "w", encoding="utf-8") as file:
        file.write(new_content)
    patched += 1

print(f"Patched {patched} files with clean HTML.")
