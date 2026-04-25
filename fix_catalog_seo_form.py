#!/usr/bin/env python3
"""
Fix three issues at once:
  1. Unified catalog — people.js, fix random-btn drift, missing EN cards,
     submit dropdowns, build-index.js
  2. Form end-to-end — submit-en.html gets action attr, Netlify junk removed,
     placeholder detection added to both forms
  3. SEO / a11y — twitter:image on 10 new dossiers, meaningful alt on hero
     photos, og:image+hreflang on about/timeline, <main>+skip-link on key pages
"""

import re, pathlib, textwrap

BASE = pathlib.Path(__file__).parent

# ─── 1.  CANONICAL CATALOG ────────────────────────────────────────────────────

PEOPLE = [
    # slug, nameRU, nameEN, channel
    ("solovyov",     "Владимир Соловьёв",   "Vladimir Solovyov",        "rossiya1"),
    ("skabeeva",     "Ольга Скабеева",       "Olga Skabeeva",            "rossiya1"),
    ("kiselyov",     "Дмитрий Киселёв",     "Dmitry Kiselyov",          "rt"),
    ("simonyan",     "Маргарита Симоньян",   "Margarita Simonyan",       "rt"),
    ("popov",        "Евгений Попов",        "Yevgeny Popov",            "rossiya1"),
    ("sheynin",      "Артём Шейнин",         "Artyom Sheynin",           "perviy"),
    ("tolstoy",      "Пётр Толстой",         "Pyotr Tolstoy",            "vlast"),
    ("norkin",       "Андрей Норкин",        "Andrey Norkin",            "ntv"),
    ("keosayan",     "Тигран Кеосаян",       "Tigran Keosayan",          "rt"),
    ("andreyeva",    "Екатерина Андреева",   "Yekaterina Andreyeva",     "perviy"),
    ("mamontov",     "Аркадий Мамонтов",     "Arkady Mamontov",          "rossiya1"),
    ("prilepin",     "Захар Прилепин",       "Zakhar Prilepin",          "vlast"),
    ("leontyev",     "Михаил Леонтьев",      "Mikhail Leontyev",         "perviy"),
    ("korchevnikov", "Борис Корчевников",    "Boris Korchevnikov",       "rossiya1"),
    ("medinsky",     "Владимир Мединский",   "Vladimir Medinsky",        "vlast"),
    ("mikhalkov",    "Никита Михалков",      "Nikita Mikhalkov",         "kultura"),
    ("dugin",        "Александр Дугин",      "Alexander Dugin",          "ideolog"),
    ("krasovsky",    "Антон Красовский",     "Anton Krasovsky",          "rt"),
    ("medvedev",     "Дмитрий Медведев",     "Dmitry Medvedev",          "vlast"),
    ("kadyrov",      "Рамзан Кадыров",       "Ramzan Kadyrov",           "vlast"),
    ("malofeev",     "Константин Малофеев",  "Konstantin Malofeev",      "ideolog"),
    ("nikonov",      "Вячеслав Никонов",     "Vyacheslav Nikonov",       "vlast"),
    ("poddubny",     "Евгений Поддубный",    "Evgeny Poddubny",          "rt"),
    ("zakharova",    "Мария Захарова",       "Maria Zakharova",          "vlast"),
    ("kovalchuk",    "Юрий Ковальчук",       "Yuri Kovalchuk",           "vlast"),
    ("turchak",      "Андрей Турчак",        "Andrei Turchak",           "vlast"),
    ("navka",        "Татьяна Навка",        "Tatiana Navka",            "kultura"),
    ("peskov",       "Дмитрий Песков",       "Dmitry Peskov",            "vlast"),
    ("lavrov",       "Сергей Лавров",        "Sergei Lavrov",            "vlast"),
    ("mizulina",     "Елена Мизулина",       "Elena Mizulina",           "vlast"),
    ("nebenzya",     "Василий Небензя",      "Vasily Nebenzya",          "vlast"),
    ("patrushev",    "Николай Патрушев",     "Nikolai Patrushev",        "vlast"),
    ("matvienko",    "Валентина Матвиенко",  "Valentina Matvienko",      "vlast"),
    ("slutsky",      "Леонид Слуцкий",       "Leonid Slutsky",           "vlast"),
    ("emizulina",    "Екатерина Мизулина",   "Yekaterina Mizulina",      "vlast"),
]

SLUGS     = [p[0] for p in PEOPLE]
NAMES_RU  = [p[1] for p in PEOPLE]
NAMES_EN  = [p[2] for p in PEOPLE]
CHANNELS  = [p[3] for p in PEOPLE]

BASE_URL = "https://cycterna2222288888-ai.github.io/cremle"

# ── 1a. Write people.js ───────────────────────────────────────────────────────

js_entries = []
for slug, nameRU, nameEN, channel in PEOPLE:
    js_entries.append(
        f'  {{slug:"{slug}",nameRU:"{nameRU}",nameEN:"{nameEN}",channel:"{channel}"}}'
    )

PEOPLE_JS = """\
/* people.js — единый каталог 35 фигурантов / canonical 35-person catalog
   Kremlin Voices · https://cycterna2222288888-ai.github.io/cremle/
   Используется: навигация, random, submit-dropdown, build-index, RSS, sitemap */
var PEOPLE = [
""" + ",\n".join(js_entries) + """
];
/* helpers */
var SLUGS_RU = PEOPLE.map(function(p){return p.slug+'.html';});
var SLUGS_EN = PEOPLE.map(function(p){return p.slug+'-en.html';});
"""
(BASE / "people.js").write_text(PEOPLE_JS, "utf-8")
print("✓ people.js written")

# ── 1b. Fix index.html random button (23 → 35 pages) ─────────────────────────

html = (BASE / "index.html").read_text("utf-8")
old_pages_pat = re.compile(
    r"var pages = \['solovyov\.html'.*?'poddubny\.html'\];", re.DOTALL
)
slugs_js = ",".join(f"'{s}.html'" for s in SLUGS)
new_pages = f"var pages = [{slugs_js}];"
html_new, n = old_pages_pat.subn(new_pages, html)
if n:
    (BASE / "index.html").write_text(html_new, "utf-8")
    print(f"✓ index.html: random button updated ({n} replacement)")
else:
    print("⚠ index.html: random button pattern not found — skipping")

# ── 1c. Add 5 missing EN cards to index-en.html ──────────────────────────────

NEW_CARDS_EN = """
  <!-- NEBENZYA -->
  <a class="card" data-channel="vlast" href="nebenzya-en.html">
    <div class="card-monogram">VN</div>
    <div class="card-top">
      <div class="card-num">Dossier № 31</div>
      <div class="card-name">Vasily Nebenzya</div>
      <div class="card-title">Russia's UN envoy. The veto as a weapon.</div>
      <ul class="card-facts">
        <li><span>Born</span><span>1962, Moscow</span></li>
        <li><span>Position</span><span>Russia's UN Permanent Representative</span></li>
        <li><span>Sanctions</span><span>EU, UK</span></li>
        <li><span>Since</span><span>2017</span></li>
        <li><span>Vetoes</span><span>20+ UN Security Council resolutions blocked</span></li>
      </ul>
    </div>
    <div class="card-quote"><blockquote>"Russia is protecting Donbas residents from the genocide organised by the Kyiv regime."</blockquote></div>
    <div class="card-bottom"><span class="card-cta">Open dossier</span><span class="card-arrow">↗</span></div>
  </a>

  <!-- PATRUSHEV -->
  <a class="card" data-channel="vlast" href="patrushev-en.html">
    <div class="card-monogram">NP</div>
    <div class="card-top">
      <div class="card-num">Dossier № 32</div>
      <div class="card-name">Nikolai Patrushev</div>
      <div class="card-title">The Grey Cardinal of the Kremlin.</div>
      <ul class="card-facts">
        <li><span>Born</span><span>1951, Leningrad</span></li>
        <li><span>Position</span><span>Presidential Adviser; former Security Council Secretary</span></li>
        <li><span>Sanctions</span><span>EU, USA, UK</span></li>
        <li><span>FSB director</span><span>1999–2008</span></li>
        <li><span>2021</span><span>Published article denying Ukrainian statehood</span></li>
      </ul>
    </div>
    <div class="card-quote"><blockquote>"Ukraine as a state has no future."</blockquote></div>
    <div class="card-bottom"><span class="card-cta">Open dossier</span><span class="card-arrow">↗</span></div>
  </a>

  <!-- MATVIENKO -->
  <a class="card" data-channel="vlast" href="matvienko-en.html">
    <div class="card-monogram">VM</div>
    <div class="card-top">
      <div class="card-num">Dossier № 33</div>
      <div class="card-name">Valentina Matvienko</div>
      <div class="card-title">Born in Ukraine. Voted for its invasion.</div>
      <ul class="card-facts">
        <li><span>Born</span><span>1949, Shepetivka, Ukraine</span></li>
        <li><span>Position</span><span>Speaker, Federation Council</span></li>
        <li><span>Sanctions</span><span>EU, USA, UK, Canada, Australia</span></li>
        <li><span>22 Feb 2022</span><span>Authorized use of armed forces in Ukraine</span></li>
        <li><span>Oct 2022</span><span>Ratified annexation of 4 regions</span></li>
      </ul>
    </div>
    <div class="card-quote"><blockquote>"The residents of Donbas have chosen Russia. We have taken them in — forever."</blockquote></div>
    <div class="card-bottom"><span class="card-cta">Open dossier</span><span class="card-arrow">↗</span></div>
  </a>

  <!-- SLUTSKY -->
  <a class="card" data-channel="vlast" href="slutsky-en.html">
    <div class="card-monogram">LS</div>
    <div class="card-top">
      <div class="card-num">Dossier № 34</div>
      <div class="card-name">Leonid Slutsky</div>
      <div class="card-title">LDPR leader. Diplomacy as cover.</div>
      <ul class="card-facts">
        <li><span>Born</span><span>1968, Moscow</span></li>
        <li><span>Position</span><span>LDPR leader; Duma International Affairs Committee chair</span></li>
        <li><span>Sanctions</span><span>EU, USA, UK</span></li>
        <li><span>Feb–Mar 2022</span><span>Led Russia's "peace talks" delegation</span></li>
        <li><span>2018</span><span>Cleared by Duma ethics committee after harassment reports</span></li>
      </ul>
    </div>
    <div class="card-quote"><blockquote>"We have reached significant progress in the negotiations."</blockquote></div>
    <div class="card-bottom"><span class="card-cta">Open dossier</span><span class="card-arrow">↗</span></div>
  </a>

  <!-- EMIZULINA -->
  <a class="card" data-channel="vlast" href="emizulina-en.html">
    <div class="card-monogram">EM</div>
    <div class="card-top">
      <div class="card-num">Dossier № 35</div>
      <div class="card-name">Yekaterina Mizulina</div>
      <div class="card-title">League of Safe Internet. Censorship as a family business.</div>
      <ul class="card-facts">
        <li><span>Born</span><span>1985</span></li>
        <li><span>Position</span><span>Director, League of Safe Internet</span></li>
        <li><span>Sanctions</span><span>EU (2024)</span></li>
        <li><span>Founded LBI</span><span>2011</span></li>
        <li><span>Method</span><span>Crowdsourced censorship via Telegram (500k+ followers)</span></li>
      </ul>
    </div>
    <div class="card-quote"><blockquote>"Safe internet means Russian internet."</blockquote></div>
    <div class="card-bottom"><span class="card-cta">Open dossier</span><span class="card-arrow">↗</span></div>
  </a>
"""

html_en = (BASE / "index-en.html").read_text("utf-8")
# Insert before the closing </div> of the .cards block (which is followed by quote-strip)
anchor = '\n\n</div>\n\n<div class="quote-strip">'
if anchor in html_en and "nebenzya-en.html" not in html_en:
    html_en_new = html_en.replace(anchor, NEW_CARDS_EN + anchor)
    (BASE / "index-en.html").write_text(html_en_new, "utf-8")
    print("✓ index-en.html: 5 EN cards added")
elif "nebenzya-en.html" in html_en:
    print("  index-en.html: EN cards already present")
else:
    print("⚠ index-en.html: anchor not found — skipping")

# ── 1d. Fix submit.html select options (24 → 35) ─────────────────────────────

def make_select_options_ru():
    opts = ['<option value="">— Выберите фигуранта —</option>']
    for slug, nameRU, _, _ in PEOPLE:
        opts.append(f'        <option value="{slug}">{nameRU}</option>')
    opts.append('        <option value="general">Общее / Несколько фигурантов</option>')
    return "\n".join(opts)

def make_select_options_en():
    opts = ['<option value="">— Select a subject —</option>']
    for slug, _, nameEN, _ in PEOPLE:
        opts.append(f'        <option value="{slug}">{nameEN}</option>')
    opts.append('        <option value="general">General / Multiple subjects</option>')
    return "\n".join(opts)

select_pat = re.compile(
    r'<select id="subject" name="subject" required>\s*<option[^>]*>.*?</select>',
    re.DOTALL
)

for fname, opts_fn in [("submit.html", make_select_options_ru),
                        ("submit-en.html", make_select_options_en)]:
    html_s = (BASE / fname).read_text("utf-8")
    new_select = f'<select id="subject" name="subject" required>\n        {opts_fn()}\n      </select>'
    html_s_new, n = select_pat.subn(new_select, html_s)
    if n:
        (BASE / fname).write_text(html_s_new, "utf-8")
        print(f"✓ {fname}: select updated ({n} replacement, 35 options)")
    else:
        print(f"⚠ {fname}: select pattern not found")

# ── 1e. Fix build-index.js — add 11 missing entries ──────────────────────────

bijs = (BASE / "build-index.js").read_text("utf-8")
# Find the DOSYE array closing bracket
# Replace entire DOSYE array with full 35-person version
new_dosye_entries = []
for slug, nameRU, nameEN, channel in PEOPLE:
    new_dosye_entries.append(
        f'  {{ file: \'{slug}.html\', name: \'{nameRU}\', channel: \'{channel}\', tags: [] }}'
    )
new_array = "const DOSYE = [\n" + ",\n".join(new_dosye_entries) + "\n];"
bijs_new = re.sub(r'const DOSYE = \[.*?\];', new_array, bijs, flags=re.DOTALL)
if bijs_new != bijs:
    (BASE / "build-index.js").write_text(bijs_new, "utf-8")
    print("✓ build-index.js: DOSYE array updated to 35 persons")
else:
    print("⚠ build-index.js: DOSYE array pattern not found")

# ─── 2.  FORM END-TO-END ─────────────────────────────────────────────────────

# ── 2a. submit-en.html: add action=Formspree, remove Netlify hidden input ─────

html_en_s = (BASE / "submit-en.html").read_text("utf-8")

# Fix: add action attribute to form (it has no action, uses dead Netlify method)
html_en_s = html_en_s.replace(
    '<form id="tip-form" name="tips-en" method="POST">',
    '<form id="tip-form" action="https://formspree.io/f/FORMSPREE_ID" method="POST">'
)
# Remove Netlify form-name hidden input
html_en_s = re.sub(
    r'\s*<input type="hidden" name="form-name" value="tips-en">\s*\n',
    "\n",
    html_en_s
)
(BASE / "submit-en.html").write_text(html_en_s, "utf-8")
print("✓ submit-en.html: action set to Formspree, Netlify remnant removed")

# ── 2b. Both forms: detect unconfigured FORMSPREE_ID and show inline notice ───

PLACEHOLDER_DETECT_JS = """\
<script>
(function(){
  var form = document.getElementById('tip-form');
  if (!form) return;
  if (form.action && form.action.includes('FORMSPREE_ID')) {
    var btn = document.getElementById('submit-btn');
    if (btn) { btn.disabled = true; btn.title = 'Form not yet configured'; }
    var notice = document.createElement('div');
    notice.style.cssText = 'margin:16px 0;padding:12px 16px;background:#1a0a00;border-left:3px solid #8b1a1a;color:#bab3a0;font-size:13px';
    notice.textContent = '⚠ Форма не активирована. Зарегистрируйтесь на formspree.io и замените FORMSPREE_ID в коде.';
    form.insertBefore(notice, form.firstChild);
  }
})();
</script>"""

PLACEHOLDER_DETECT_JS_EN = PLACEHOLDER_DETECT_JS.replace(
    '⚠ Форма не активирована. Зарегистрируйтесь на formspree.io и замените FORMSPREE_ID в коде.',
    '⚠ Form not yet activated. Register at formspree.io and replace FORMSPREE_ID in the source.'
)

for fname, detect_js in [("submit.html", PLACEHOLDER_DETECT_JS),
                          ("submit-en.html", PLACEHOLDER_DETECT_JS_EN)]:
    html_s = (BASE / fname).read_text("utf-8")
    if 'FORMSPREE_ID' in detect_js and 'placeholder-detect' not in html_s:
        html_s = html_s.replace("</body>", detect_js + "\n</body>")
        (BASE / fname).write_text(html_s, "utf-8")
        print(f"✓ {fname}: placeholder detection added")

# ─── 3.  SEO / ACCESSIBILITY ─────────────────────────────────────────────────

OG_IMAGE_GENERIC = f"{BASE_URL}/og-image.svg"

# ── 3a. twitter:image on all 10 new dossiers ─────────────────────────────────

NEW_DOSSIER_META = {
    "nebenzya":   {"nameRU": "Василий Небензя",      "nameEN": "Vasily Nebenzya"},
    "patrushev":  {"nameRU": "Николай Патрушев",     "nameEN": "Nikolai Patrushev"},
    "matvienko":  {"nameRU": "Валентина Матвиенко",  "nameEN": "Valentina Matvienko"},
    "slutsky":    {"nameRU": "Леонид Слуцкий",       "nameEN": "Leonid Slutsky"},
    "emizulina":  {"nameRU": "Екатерина Мизулина",   "nameEN": "Yekaterina Mizulina"},
}

for slug, names in NEW_DOSSIER_META.items():
    og_img_url = f"{BASE_URL}/og-{slug}.svg"
    for suffix, lang_name in [(".html", names["nameRU"]), ("-en.html", names["nameEN"])]:
        fpath = BASE / (slug + suffix)
        if not fpath.exists():
            continue
        html_d = fpath.read_text("utf-8")
        changed = False

        # Add twitter:image after twitter:card
        if 'twitter:image' not in html_d and 'twitter:card' in html_d:
            html_d = html_d.replace(
                '<meta name="twitter:card" content="summary_large_image">',
                '<meta name="twitter:card" content="summary_large_image">\n'
                f'<meta name="twitter:image" content="{og_img_url}">'
            )
            changed = True

        # Fix empty alt on hero photo → person's name
        hero_img_pat = re.compile(
            r'(<img loading="lazy" src="[^"]+https://upload\.wikimedia[^"]+")[^>]*alt=""([^>]*>)',
            re.DOTALL
        )
        html_d, n_alt = hero_img_pat.subn(
            r'\1 alt="' + lang_name + r'"\2',
            html_d
        )
        if n_alt:
            changed = True

        if changed:
            fpath.write_text(html_d, "utf-8")
            print(f"✓ {slug+suffix}: twitter:image added, alt fixed")

# ── 3b. about.html / about-en.html — add og:image, twitter:card/image ────────

ABOUT_PAGES = [
    ("about.html",    "О проекте — Голоса Кремля",       "ru",
     "О проекте — независимый архив пропаганды", OG_IMAGE_GENERIC,
     f"{BASE_URL}/about.html", f"{BASE_URL}/about-en.html"),
    ("about-en.html", "About — Kremlin Voices",           "en",
     "About the project — independent propaganda archive", OG_IMAGE_GENERIC,
     f"{BASE_URL}/about.html", f"{BASE_URL}/about-en.html"),
]

for fname, title, lang, desc, img_url, ru_url, en_url in ABOUT_PAGES:
    fpath = BASE / fname
    if not fpath.exists():
        continue
    html_a = fpath.read_text("utf-8")
    changed = False

    # og:image
    if 'og:image' not in html_a:
        html_a = html_a.replace(
            '<meta property="og:description"',
            f'<meta property="og:image" content="{img_url}">\n'
            '<meta property="og:description"'
        )
        changed = True

    # twitter:card + twitter:image
    if 'twitter:card' not in html_a:
        insert = (
            f'<meta name="twitter:card" content="summary_large_image">\n'
            f'<meta name="twitter:image" content="{img_url}">\n'
        )
        html_a = html_a.replace('<link rel="icon"', insert + '<link rel="icon"')
        changed = True

    if changed:
        fpath.write_text(html_a, "utf-8")
        print(f"✓ {fname}: og:image + twitter meta added")

# ── 3c. timeline.html / timeline-en.html — og:image, twitter, hreflang ───────

TIMELINE_PAGES = [
    ("timeline.html",    "ru", f"{BASE_URL}/timeline.html",    f"{BASE_URL}/timeline-en.html",
     "Хронология · Голоса Кремля", f"{BASE_URL}/og-image.svg"),
    ("timeline-en.html", "en", f"{BASE_URL}/timeline-en.html", f"{BASE_URL}/timeline.html",
     "Timeline · Kremlin Voices",  f"{BASE_URL}/og-image.svg"),
]

for fname, lang, canonical, alt_url, title, img_url in TIMELINE_PAGES:
    fpath = BASE / fname
    if not fpath.exists():
        continue
    html_t = fpath.read_text("utf-8")
    changed = False

    # hreflang
    if 'hreflang' not in html_t:
        ru_url = f"{BASE_URL}/timeline.html"
        en_url = f"{BASE_URL}/timeline-en.html"
        hreflang_block = (
            f'<link rel="canonical" href="{canonical}">\n'
            f'<link rel="alternate" hreflang="ru" href="{ru_url}">\n'
            f'<link rel="alternate" hreflang="en" href="{en_url}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{ru_url}">\n'
        )
        html_t = html_t.replace('<link rel="icon"', hreflang_block + '<link rel="icon"')
        changed = True

    # og:type + og:title + og:description + og:image
    if 'og:image' not in html_t:
        og_block = (
            f'<meta property="og:type" content="website">\n'
            f'<meta property="og:title" content="{title}">\n'
            f'<meta property="og:image" content="{img_url}">\n'
        )
        html_t = html_t.replace('<link rel="icon"', og_block + '<link rel="icon"')
        changed = True

    # twitter
    if 'twitter:card' not in html_t:
        tw_block = (
            f'<meta name="twitter:card" content="summary_large_image">\n'
            f'<meta name="twitter:image" content="{img_url}">\n'
        )
        html_t = html_t.replace('<link rel="icon"', tw_block + '<link rel="icon"')
        changed = True

    if changed:
        fpath.write_text(html_t, "utf-8")
        print(f"✓ {fname}: og:image + twitter + hreflang added")

# ── 3d. <main> + skip-link on key pages ──────────────────────────────────────

SKIP_LINK_CSS = """\
<style>
.skip-link{position:absolute;left:-9999px;top:auto;width:1px;height:1px;overflow:hidden}
.skip-link:focus{position:fixed;left:16px;top:16px;width:auto;height:auto;padding:8px 16px;background:var(--red);color:var(--paper);font-size:13px;z-index:9999;text-decoration:none;outline:2px solid var(--paper)}
</style>"""

SKIP_LINK_HTML = '<a class="skip-link" href="#main-content">Перейти к содержимому</a>'
SKIP_LINK_HTML_EN = '<a class="skip-link" href="#main-content">Skip to content</a>'

KEY_PAGES = [
    ("index.html",      SKIP_LINK_HTML,    "topbar"),
    ("index-en.html",   SKIP_LINK_HTML_EN, "topbar"),
    ("about.html",      SKIP_LINK_HTML,    "topbar"),
    ("about-en.html",   SKIP_LINK_HTML_EN, "topbar"),
    ("timeline.html",   SKIP_LINK_HTML,    "tl-header"),
    ("timeline-en.html",SKIP_LINK_HTML_EN, "tl-header"),
    ("submit.html",     SKIP_LINK_HTML,    "container"),
    ("submit-en.html",  SKIP_LINK_HTML_EN, "container"),
]

for fname, skip_html, main_anchor_class in KEY_PAGES:
    fpath = BASE / fname
    if not fpath.exists():
        continue
    html_k = fpath.read_text("utf-8")
    changed = False

    # Add skip-link CSS if not present
    if 'skip-link' not in html_k:
        html_k = html_k.replace('</head>', SKIP_LINK_CSS + '\n</head>')
        changed = True

    # Add skip-link element right after <body>
    if 'class="skip-link"' not in html_k:
        html_k = html_k.replace('<body>', '<body>\n' + skip_html)
        changed = True

    # Add id="main-content" to the first main anchor class element
    anchor_pat = re.compile(r'(<div class="' + re.escape(main_anchor_class) + r'")')
    if 'id="main-content"' not in html_k:
        html_k, n = anchor_pat.subn(r'<main id="main-content">\n\1', html_k, count=1)
        # Close main before footer or last script
        if n:
            html_k = html_k.replace('\n</body>', '\n</main>\n</body>', 1)
            changed = True

    if changed:
        fpath.write_text(html_k, "utf-8")
        print(f"✓ {fname}: skip-link + <main> added")

print("\n✓ All done.")
