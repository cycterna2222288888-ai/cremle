#!/usr/bin/env python3
import re
from pathlib import Path

BASE = Path(__file__).parent

# 1. Умный поиск папки с картинками
folder_name = "templates"
for f in ['templates', 'temlpates', 'photos']:
    if (BASE / f).exists():
        folder_name = f
        break

img_dir = BASE / folder_name

images = {}
if img_dir.exists():
    for f in img_dir.iterdir():
        if f.is_file() and f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.webp']:
            images[f.stem.lower()] = f.name

updated = 0

print("=== Приводим все карточки к единому стилю ===")

for filepath in BASE.glob('*.html'):
    if filepath.name.startswith('index') or filepath.name == 'googlec2551b38ace60f0f.html' or filepath.name == 'submit.html':
        continue

    # Имя для поиска картинки
    person_id = filepath.name.replace('-en.html', '').replace('.html', '')
    html = filepath.read_text('utf-8')

    start_idx = html.find('<div class="hero-right">')
    if start_idx == -1:
        continue

    # 2. Ищем штамп, чтобы аккуратно сохранить его
    stamp_match = re.search(r'(<div class="hero-stamp"[^>]*>.*?</div>)', html[start_idx:start_idx+3000], re.DOTALL)
    if not stamp_match:
        continue
    
    stamp_code = stamp_match.group(1)
    # Добавим z-index, чтобы текст не перекрывался градиентом
    if 'z-index' not in stamp_code:
        stamp_code = stamp_code.replace('class="hero-stamp"', 'class="hero-stamp" style="z-index:2;"')

    # Ищем конец блока hero-right (закрывающий div сразу после штампа)
    stamp_end_idx = html.find(stamp_match.group(0), start_idx) + len(stamp_match.group(0))
    div_close_idx = html.find('</div>', stamp_end_idx) + 6

    # 3. Вытягиваем инициалы из заголовка (для стильной фоновой подложки)
    name_match = re.search(r'<h1 class="hero-name">(.*?)</h1>', html, re.DOTALL)
    initials = ""
    if name_match:
        raw_name = name_match.group(1).replace('<br>', ' ').replace('\n', ' ')
        raw_name = re.sub(r'<[^>]+>', '', raw_name).strip() # Убираем теги
        words = [w for w in raw_name.split() if w]
        if len(words) >= 2:
            initials = (words[0][0] + words[1][0]).upper()
        elif len(words) == 1:
            initials = words[0][:2].upper()

    # 4. Формируем путь к картинке
    img_file = images.get(person_id, f"{person_id}.jpg") # Фолбэк на .jpg если не найдено в словаре
    img_path = f"{folder_name}/{img_file}"

    # 5. Собираем идеальный блок hero-right
    img_tag = f'<img loading="lazy" src="{img_path}" alt="{person_id}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top center;opacity:0.85;z-index:0;" onerror="this.style.display=\'none\'">'

    svg_overlay = f'''<svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;z-index:1;">
      <defs>
        <radialGradient id="rg_{person_id}" cx="50%" cy="35%" r="60%">
          <stop offset="0%" stop-color="#1a0000" stop-opacity="0.4"/>
          <stop offset="100%" stop-color="#000" stop-opacity="0.9"/>
        </radialGradient>
      </defs>
      <rect width="100%" height="100%" fill="url(#rg_{person_id})"/>
      <line x1="50%" y1="20%" x2="50%" y2="80%" stroke="#8b1a1a" stroke-width="0.5" opacity="0.4"/>
      <line x1="20%" y1="50%" x2="80%" y2="50%" stroke="#8b1a1a" stroke-width="0.5" opacity="0.4"/>
      <circle cx="50%" cy="38%" r="80" fill="none" stroke="#8b1a1a" stroke-width="0.5" opacity="0.3"/>
      <circle cx="50%" cy="38%" r="140" fill="none" stroke="#8b1a1a" stroke-width="0.5" opacity="0.12"/>
      <g opacity="0.06">
        <line x1="0" y1="10%" x2="100%" y2="10%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="20%" x2="100%" y2="20%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="30%" x2="100%" y2="30%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="40%" x2="100%" y2="40%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="50%" x2="100%" y2="50%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="60%" x2="100%" y2="60%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="70%" x2="100%" y2="70%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="80%" x2="100%" y2="80%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="90%" x2="100%" y2="90%" stroke="#c8c0b0" stroke-width="1"/>
      </g>
      <text x="50%" y="42%" text-anchor="middle" dominant-baseline="middle" font-family="Georgia,serif" font-size="140" fill="#8b1a1a" opacity="0.15" font-weight="700">{initials}</text>
    </svg>'''

    new_hero_right = f'<div class="hero-right">\n    {img_tag}\n    {svg_overlay}\n    {stamp_code}\n  </div>'

    # Заменяем старый блок на новый
    new_html = html[:start_idx] + new_hero_right + html[div_close_idx:]

    if new_html != html:
        filepath.write_text(new_html, 'utf-8')
        updated += 1
        print(f"✓ Обновлен стиль (Инициалы {initials}): {filepath.name}")

print(f"\nГотово! Приведены к единому крутому стилю {updated} файлов.")
