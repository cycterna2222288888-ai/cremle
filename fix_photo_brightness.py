#!/usr/bin/env python3
"""Make hero photos more visible: higher opacity, lighter SVG gradient overlay."""

import re, pathlib

BASE = pathlib.Path(__file__).parent

DOSSIERS = [
    'nebenzya', 'nebenzya-en',
    'patrushev', 'patrushev-en',
    'matvienko', 'matvienko-en',
    'slutsky', 'slutsky-en',
    'emizulina', 'emizulina-en',
]

# Fix 1: img style — raise opacity, drop luminosity blend
OLD_IMG_STYLE = 'opacity:0.45;mix-blend-mode:luminosity;'
NEW_IMG_STYLE = 'opacity:0.88;'

# Fix 2: SVG radial gradient — lighten the overlay so photo shows through
OLD_GRAD = (
    '<stop offset="0%" stop-color="#1a0000" stop-opacity="0.8"/>\n'
    '        <stop offset="100%" stop-color="#000" stop-opacity="1"/>'
)
NEW_GRAD = (
    '<stop offset="0%" stop-color="#1a0000" stop-opacity="0.25"/>\n'
    '        <stop offset="100%" stop-color="#000" stop-opacity="0.55"/>'
)

for name in DOSSIERS:
    p = BASE / f'{name}.html'
    if not p.exists():
        print(f'  skip {p.name}')
        continue
    html = p.read_text('utf-8')
    n1 = html.count(OLD_IMG_STYLE)
    n2 = html.count(OLD_GRAD)
    html = html.replace(OLD_IMG_STYLE, NEW_IMG_STYLE)
    html = html.replace(OLD_GRAD, NEW_GRAD)
    p.write_text(html, 'utf-8')
    print(f'✓ {p.name}: img={n1} grad={n2}')

print('\n✓ Done.')
