#!/usr/bin/env python3
"""Normalised portrait crops for the homepage.

The source photos in templates/ have very different framing (TV stills, press
shots, full-length figures). Cropping them all with one CSS object-position puts
faces at random sizes and heights. This script crops every photo around its
face so that portraits line up: same aspect ratio, eyes on the same line.

Face boxes live in data/portrait-faces.json (x, y, fw, fh in source pixels).
They were measured with OpenCV's Haar detector; entries marked "manual" were
corrected by hand. Re-detect with --detect (needs opencv-python-headless<5);
otherwise only Pillow is required.

Output
  templates/portraits/<name>.jpg        3:4, 480x640, catalogue rows and hover preview
  templates/portraits/hero-<name>.jpg   4:5, up to 880x1100, homepage masthead (shared framing)
Both are grayscale with normalised contrast, matching how the site displays them.

It also writes a per-photo focal point (object-position) onto the dossier
hero portraits, so faces sit right of centre at a common height instead of
wherever a fixed 50% 18% happens to land.

Usage: python3 tools/portraits.py [--detect]
"""
import glob
import re
import json
import os
import sys

from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'templates')
OUT = os.path.join(SRC, 'portraits')
FACES = os.path.join(ROOT, 'data', 'portrait-faces.json')

EYE = 0.40          # eye line, share of crop height
EYE_IN_BOX = 0.40   # eyes sit ~40% down a Haar face box
HERO_SLUGS = ['keosayan.jpg', 'dugin.jpg', 'krasovsky.png', 'medvedev.jpg', 'kovalchuk.jpg', 'patrushev.jpg']
HERO_FACE = 0.77    # face width / crop width, identical for every hero portrait
THUMB_FACE = 0.60   # preferred face share for catalogue crops (looser if the photo allows)


def detect(files):
    import cv2
    import numpy as np
    front = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    side = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')
    faces = json.load(open(FACES)) if os.path.exists(FACES) else {}
    for name in files:
        if faces.get(name, {}).get('manual'):
            continue
        im = Image.open(os.path.join(SRC, name)).convert('RGB')
        w, h = im.size
        g = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2GRAY)
        found = list(front.detectMultiScale(g, 1.08, 6, minSize=(max(24, w // 25),) * 2))
        if not found:
            found = list(side.detectMultiScale(g, 1.08, 5, minSize=(24, 24)))
        if not found:
            found = [(w - x - fw, y, fw, fh) for (x, y, fw, fh) in side.detectMultiScale(cv2.flip(g, 1), 1.08, 5, minSize=(24, 24))]
        if not found:
            print('no face:', name)
            continue
        x, y, fw, fh = max(found, key=lambda r: r[2] * r[3])
        faces[name] = dict(w=w, h=h, x=int(x), y=int(y), fw=int(fw), fh=int(fh))
    json.dump(faces, open(FACES, 'w'), indent=1, ensure_ascii=False)
    return faces


def crop_box(f, aspect, face_share, eye=EYE):
    """Largest crop of the given aspect (w/h) with the eyes on `eye`, the face
    roughly centred and the face no smaller than `face_share` of the width."""
    W, H = f['w'], f['h']
    cx = f['x'] + f['fw'] / 2
    ey = f['y'] + EYE_IN_BOX * f['fh']
    cw = min(W, H * aspect, f['fw'] / face_share)
    while cw > 16:
        ch = cw / aspect
        top = ey - eye * ch
        left = min(max(cx - cw / 2, 0), W - cw)
        if top >= 0 and top + ch <= H and abs(left + cw / 2 - cx) <= 0.12 * cw:
            return (round(left), round(top), round(left + cw), round(top + ch))
        cw -= 1
    # photo too tight for the eye line: fall back to a centred crop
    cw = min(W, H * aspect)
    ch = cw / aspect
    left = min(max(cx - cw / 2, 0), W - cw)
    top = min(max(ey - eye * ch, 0), H - ch)
    return (round(left), round(top), round(left + cw), round(top + ch))


def save(im, box, size, path):
    """Crop, downscale, and even out tone: the site shows portraits in
    grayscale, so files are stored that way with matched black/white points."""
    out = im.crop(box)
    out = out.resize(size, Image.LANCZOS) if out.width > size[0] else out
    out = ImageOps.autocontrast(ImageOps.grayscale(out), cutoff=(0.6, 0.4))
    out.save(path, 'JPEG', quality=80, optimize=True, progressive=True)


def focal_point(f, box_w=678, box_h=842, at_x=0.56, at_eye=0.36):
    """object-position (in %) that puts the face centre at `at_x` of the dossier
    hero panel and the eyes at `at_eye` of its height. The panel is ~678x842 at
    1440px wide; its image is 112% tall (parallax), offset by -6%."""
    W, H = f['w'], f['h']
    img_h = box_h * 1.12
    scale = max(box_w / W, img_h / H)
    dw, dh = W * scale, H * scale
    fx = (f['x'] + f['fw'] / 2) * scale
    fy = (f['y'] + EYE_IN_BOX * f['fh']) * scale
    def pct(slack, want):
        return 50 if abs(slack) < 1 else max(0, min(100, round(100 * want / slack)))
    return pct(box_w - dw, at_x * box_w - fx), pct(img_h - dh, (at_eye + 0.06) * box_h - fy)


def tag_dossiers(faces):
    for page in sorted(glob.glob(os.path.join(ROOT, '*.html'))):
        html = open(page, encoding='utf-8').read()
        m = re.search(r'<img data-parallax="0.06"[^>]*src="templates/([^"]+)"[^>]*>', html)
        if not m or m.group(1) not in faces:
            continue
        x, y = focal_point(faces[m.group(1)])
        tag = re.sub(r'\sstyle="[^"]*"', '', m.group(0))
        tag = tag.replace('<img ', f'<img style="object-position:{x}% {y}%" ', 1)
        if tag != m.group(0):
            open(page, 'w', encoding='utf-8').write(html.replace(m.group(0), tag, 1))


def main():
    files = sorted(f for f in os.listdir(SRC) if os.path.isfile(os.path.join(SRC, f)))
    faces = detect(files) if '--detect' in sys.argv else json.load(open(FACES))
    os.makedirs(OUT, exist_ok=True)
    for name in files:
        f = faces.get(name)
        if not f:
            continue
        im = Image.open(os.path.join(SRC, name)).convert('RGB')
        stem = os.path.splitext(name)[0]
        save(im, crop_box(f, 3 / 4, THUMB_FACE), (480, 640), os.path.join(OUT, stem + '.jpg'))
        if name in HERO_SLUGS:
            box = crop_box(f, 4 / 5, HERO_FACE)
            share = f['fw'] / (box[2] - box[0])
            if abs(share - HERO_FACE) > 0.01:
                print(f'warning: {name} hero framing {share:.2f} != {HERO_FACE}')
            save(im, box, (880, 1100), os.path.join(OUT, 'hero-' + stem + '.jpg'))
    tag_dossiers(faces)
    print('portraits written to', os.path.relpath(OUT, ROOT), '· dossier focal points updated')


if __name__ == '__main__':
    main()
