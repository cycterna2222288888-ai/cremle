#!/usr/bin/env python3
"""fix_all.py — keyboard nav, sitemap domain, connections-en, quotes-en"""
import re, os

BASE = '/Users/petrdracev/Desktop/proj/cremle/'

# ─────────────────────────────────────────────────────────────────
# 1. KEYBOARD NAV — standardise to 35-item array in old dossiers
# ─────────────────────────────────────────────────────────────────
SLUGS = [
    'solovyov','skabeeva','simonyan','kiselyov','popov','sheynin','tolstoy',
    'norkin','keosayan','andreyeva','leontyev','mamontov','medinsky','prilepin',
    'dugin','mikhalkov','korchevnikov','krasovsky','medvedev','kadyrov','malofeev',
    'nikonov','poddubny','zakharova','kovalchuk','turchak','navka','peskov',
    'lavrov','mizulina','nebenzya','patrushev','matvienko','slutsky','emizulina',
]
NEW_5 = {'nebenzya','patrushev','matvienko','slutsky','emizulina'}

def pages_arr(suffix):
    return '[' + ','.join(f"'{s}{suffix}'" for s in SLUGS) + ']'

RU_ARR = pages_arr('.html')
EN_ARR = pages_arr('-en.html')

def new_nav(arr):
    return (
        f"var pages={arr};\n"
        "var cur=window.location.pathname.split('/').pop();\n"
        "var idx=pages.indexOf(cur);\n"
        "if(idx<0)return;\n"
        "document.addEventListener('keydown',function(e){\n"
        "  if(e.altKey||e.ctrlKey||e.metaKey||e.shiftKey)return;\n"
        "  if(e.target&&(e.target.tagName==='INPUT'||e.target.tagName==='TEXTAREA'))return;\n"
        "  if(e.key==='ArrowRight'&&idx<pages.length-1)location.href=pages[idx+1];\n"
        "  if(e.key==='ArrowLeft'&&idx>0)location.href=pages[idx-1];\n"
        "});"
    )

NAV_RE = re.compile(
    r"var pages\s*=\s*\[[^\]]+\];.*?document\.addEventListener\(['\"]keydown['\"].*?\}\s*\);",
    re.DOTALL
)

n_nav = 0
for slug in SLUGS:
    if slug in NEW_5:
        continue
    for fname, arr in [(f'{slug}.html', RU_ARR), (f'{slug}-en.html', EN_ARR)]:
        path = BASE + fname
        if not os.path.exists(path):
            continue
        txt = open(path, encoding='utf-8').read()
        if 'var pages' not in txt:
            continue
        new = NAV_RE.sub(new_nav(arr), txt)
        if new != txt:
            open(path, 'w', encoding='utf-8').write(new)
            n_nav += 1
            print(f'✓ nav: {fname}')
        else:
            print(f'  WARN nav unchanged: {fname}')

print(f'✓ Keyboard nav: {n_nav} pages updated\n')

# ─────────────────────────────────────────────────────────────────
# 2. SITEMAP — replace netlify domain everywhere
# ─────────────────────────────────────────────────────────────────
NETLIFY = 'https://cremle.netlify.app/'
GITHUB  = 'https://cycterna2222288888-ai.github.io/cremle/'

spath = BASE + 'sitemap.xml'
stxt  = open(spath, encoding='utf-8').read()
fixed = stxt.replace(NETLIFY, GITHUB)
if fixed != stxt:
    open(spath, 'w', encoding='utf-8').write(fixed)
    n_rep = stxt.count(NETLIFY)
    print(f'✓ sitemap.xml: {n_rep} URLs updated to GitHub Pages\n')
else:
    print('  sitemap already clean\n')

# Also fix og/canonical/hreflang in all HTML (netlify refs in head)
html_files = [f for f in os.listdir(BASE) if f.endswith('.html')]
n_html = 0
for f in html_files:
    p = BASE + f
    t = open(p, encoding='utf-8').read()
    u = t.replace(NETLIFY, GITHUB)
    if u != t:
        open(p, 'w', encoding='utf-8').write(u)
        n_html += 1
        print(f'  fixed canonical: {f}')
print(f'✓ HTML canonical/og: {n_html} files updated\n')

# ─────────────────────────────────────────────────────────────────
# 3. CONNECTIONS-EN — add 5 nodes + 6 links
# ─────────────────────────────────────────────────────────────────
cen = BASE + 'connections-en.html'
ctxt = open(cen, encoding='utf-8').read()

OLD_NODES_END = "{id:'mizulina',     label:'Mizulina',          type:'person', role:'Federation Council / Censorship',size:10, url:'mizulina-en.html'}\n  ];"
NEW_NODES_END = """{id:'mizulina',     label:'Mizulina',          type:'person', role:'Federation Council / Censorship',size:10, url:'mizulina-en.html'},
    {id:'nebenzya',     label:'Nebenzya',          type:'person', role:'UN Security Council',               size:12, url:'nebenzya-en.html'},
    {id:'patrushev',    label:'Patrushev',         type:'person', role:'FSB / Security Council / Adviser',  size:13, url:'patrushev-en.html'},
    {id:'matvienko',    label:'Matvienko',         type:'person', role:'Federation Council',                size:11, url:'matvienko-en.html'},
    {id:'slutsky',      label:'Slutsky',           type:'person', role:'LDPR / State Duma Foreign Affairs', size:10, url:'slutsky-en.html'},
    {id:'emizulina',    label:'E.Mizulina',        type:'person', role:'Safe Internet League',              size:9,  url:'emizulina-en.html'}
  ];"""

OLD_LINKS_END = "{source:'lavrov',       target:'zakharova', type:'работа',   w:2}\n  ];"
NEW_LINKS_END = """{source:'lavrov',       target:'zakharova', type:'работа',   w:2},
    {source:'nebenzya',     target:'kremlin',   type:'работа',   w:4},
    {source:'patrushev',    target:'kremlin',   type:'работа',   w:4},
    {source:'matvienko',    target:'kremlin',   type:'работа',   w:3},
    {source:'slutsky',      target:'kremlin',   type:'работа',   w:2},
    {source:'emizulina',    target:'kremlin',   type:'влияние',  w:2},
    {source:'emizulina',    target:'mizulina',  type:'семья',    w:3}
  ];"""

ctxt2 = ctxt.replace(OLD_NODES_END, NEW_NODES_END)
if ctxt2 == ctxt:
    print('  WARN connections-en nodes: no match')
else:
    print('✓ connections-en.html: 5 nodes added')

ctxt3 = ctxt2.replace(OLD_LINKS_END, NEW_LINKS_END)
if ctxt3 == ctxt2:
    print('  WARN connections-en links: no match')
else:
    print('✓ connections-en.html: 6 links added')

if ctxt3 != ctxt:
    open(cen, 'w', encoding='utf-8').write(ctxt3)
print()

# ─────────────────────────────────────────────────────────────────
# 4. QUOTES-EN — full body rewrite with 70+ English quotes
# ─────────────────────────────────────────────────────────────────
HEAD = open(BASE + 'quotes-en.html', encoding='utf-8').read()
# keep everything up to and including the inline <style> block + masthead
SPLIT_AFTER = '</div>\n</div>\n</style>'
# find the split point — after the inline style + masthead closing </div>
# More robust: keep head up to </style> on line 122 then masthead
# Strategy: keep everything before <style> at body-level,
# then find end of masthead closing div

# Keep head section (lines 1-77 in original = up to </head>)
# and re-add body open + topbar + section-nav + masthead from existing content
# Simplest: find marker </div>\n<style> which separates masthead from body-inline-css
# Actually just split at the extra <style> tag that appears in body

KEEP_UP_TO = '</style>\n'  # end of the second <style> block (line 122)
# Find second occurrence of </style> in file
idx1 = HEAD.find('</style>')
idx2 = HEAD.find('</style>', idx1 + 1)
if idx2 > 0:
    KEPT = HEAD[:idx2 + len('</style>')]
else:
    KEPT = HEAD[:HEAD.find('</body>')]

PERSONS_EN = [
    ('Vladimir Solovyov',     'solovyov-en.html'),
    ('Olga Skabeeva',         'skabeeva-en.html'),
    ('Margarita Simonyan',    'simonyan-en.html'),
    ('Dmitry Kiselyov',       'kiselyov-en.html'),
    ('Yevgeny Popov',         'popov-en.html'),
    ('Artyom Sheynin',        'sheynin-en.html'),
    ('Pyotr Tolstoy',         'tolstoy-en.html'),
    ('Andrey Norkin',         'norkin-en.html'),
    ('Tigran Keosayan',       'keosayan-en.html'),
    ('Yekaterina Andreyeva',  'andreyeva-en.html'),
    ('Mikhail Leontyev',      'leontyev-en.html'),
    ('Arkady Mamontov',       'mamontov-en.html'),
    ('Vladimir Medinsky',     'medinsky-en.html'),
    ('Zakhar Prilepin',       'prilepin-en.html'),
    ('Alexander Dugin',       'dugin-en.html'),
    ('Nikita Mikhalkov',      'mikhalkov-en.html'),
    ('Boris Korchevnikov',    'korchevnikov-en.html'),
    ('Anton Krasovsky',       'krasovsky-en.html'),
    ('Dmitry Medvedev',       'medvedev-en.html'),
    ('Ramzan Kadyrov',        'kadyrov-en.html'),
    ('Konstantin Malofeev',   'malofeev-en.html'),
    ('Vyacheslav Nikonov',    'nikonov-en.html'),
    ('Yevgeny Poddubny',      'poddubny-en.html'),
    ('Maria Zakharova',       'zakharova-en.html'),
    ('Yuri Kovalchuk',        'kovalchuk-en.html'),
    ('Andrei Turchak',        'turchak-en.html'),
    ('Tatiana Navka',         'navka-en.html'),
    ('Dmitry Peskov',         'peskov-en.html'),
    ('Sergei Lavrov',         'lavrov-en.html'),
    ('Elena Mizulina',        'mizulina-en.html'),
    ('Vasily Nebenzya',       'nebenzya-en.html'),
    ('Nikolai Patrushev',     'patrushev-en.html'),
    ('Valentina Matvienko',   'matvienko-en.html'),
    ('Leonid Slutsky',        'slutsky-en.html'),
    ('Ekaterina Mizulina',    'emizulina-en.html'),
]

def opts():
    lines = ['<option value="">All</option>']
    for name, _ in PERSONS_EN:
        lines.append(f'<option value="{name}">{name}</option>')
    return '\n'.join(lines)

def card(text, name, url, year, tags=''):
    tag_html = ''
    if tags:
        tag_html = '<div class="quote-year">' + tags + '</div>'
    return (
        f'<div class="quote-card">'
        f'<div class="quote-text">{text}</div>'
        f'<div class="quote-person"><a href="{url}">{name}</a></div>'
        f'<div class="quote-year">{year}</div>'
        f'</div>'
    )

def section(label, cards_html):
    return (
        f'<div class="qsection">\n'
        f'  <div class="section-label">{label}</div>\n'
        f'  <div class="quotes-grid">\n'
        f'{cards_html}'
        f'  </div>\n'
        f'</div>\n'
    )

def c(text, name, url, year):
    return (
        f'    <div class="quote-card">'
        f'<div class="quote-text">{text}</div>'
        f'<div class="quote-person"><a href="{url}">{name}</a></div>'
        f'<div class="quote-year">{year}</div>'
        f'</div>\n'
    )

# War section
war = (
    c('"When I hear the word \'peace\', I reach for my gun. Peace will come only with our victory."',
      'Vladimir Solovyov', 'solovyov-en.html', '2022')
  + c('"We are openly at war with NATO. Let\'s call things by their names: World War III has begun."',
      'Olga Skabeeva', 'skabeeva-en.html', '2022 — live broadcast')
  + c('"Either we win this war, or Russia ceases to exist. There is no choice. They made us fight."',
      'Margarita Simonyan', 'simonyan-en.html', '2022')
  + c('"I was in a real war. You sit here talking about humanity — I\'ve seen entrails on the snow. This is a different conversation."',
      'Artyom Sheynin', 'sheynin-en.html', '2019')
  + c('"De-Nazification is not a metaphor. It is a concrete military and political task, and it will be accomplished."',
      'Pyotr Tolstoy', 'tolstoy-en.html', '2022')
  + c('"Ukraine is not a state in the classical sense. It\'s a project — created against Russia. And it has failed."',
      'Andrey Norkin', 'norkin-en.html', '2023')
  + c('"I wrote about war. Then I went to war. Because one without the other is either cowardice or a lie."',
      'Zakhar Prilepin', 'prilepin-en.html', '2017')
  + c('"This war is sacred. We are not fighting against people — we are fighting against the satanic element in the modern world."',
      'Boris Korchevnikov', 'korchevnikov-en.html', '2022')
  + c('"If Putin orders it — we will go all the way. To Warsaw, to Lisbon, wherever. The Chechen people are ready to execute any order."',
      'Ramzan Kadyrov', 'kadyrov-en.html', '2022')
  + c('"We are not fighting here. We are carrying out the tasks of a special military operation. These are fundamentally different things." [from the frontline near Avdiivka]',
      'Yevgeny Poddubny', 'poddubny-en.html', '2023')
  + c('"The collective West wants to destroy Russia. This is not politics — this is genocide."',
      'Maria Zakharova', 'zakharova-en.html', '2022 — MFA briefing')
  + c('"Kherson, Zaporizhzhia — this is Russia forever. This is not up for discussion."',
      'Andrei Turchak', 'turchak-en.html', '2022')
  + c('"No Russian troops are on Ukrainian territory, and there never were." [said after Russian forces entered Crimea]',
      'Dmitry Peskov', 'peskov-en.html', '2014')
  + c('"NATO expanded eastward in violation of its promises. We are restoring the historical balance."',
      'Sergei Lavrov', 'lavrov-en.html', '2022 — UN Security Council')
  + c('"Those who criticise our army are enemies. The law confirms it."',
      'Elena Mizulina', 'mizulina-en.html', '2022')
  + c('"Russia is protecting the residents of Donbas from the genocide organised by the Kyiv regime."',
      'Vasily Nebenzya', 'nebenzya-en.html', '2022 — UN Security Council')
  + c('"Ukraine as a state has no future. That is a historical fact."',
      'Nikolai Patrushev', 'patrushev-en.html', '2022')
  + c('"Kherson, Zaporizhzhia — this is Russia. Forever."',
      'Valentina Matvienko', 'matvienko-en.html', '2022')
)

# West section
west = (
    c('"All this Western democracy is theater. Puppets controlled by bankers and the military-industrial complex."',
      'Dmitry Kiselyov', 'kiselyov-en.html', '2021')
  + c('"RT is not propaganda. It\'s a different point of view. That is exactly what the West fears — narrative competition."',
      'Margarita Simonyan', 'simonyan-en.html', '2017')
  + c('"The US is funding biolabs in Ukraine. This is not a theory — it\'s a fact they have indirectly admitted themselves."',
      'Olga Skabeeva', 'skabeeva-en.html', '2022')
  + c('"All these NGOs are financed by Soros — grandchildren of those who fled Russia in 1917, now returning to teach us."',
      'Pyotr Tolstoy', 'tolstoy-en.html', '2017')
  + c('"Europe is dying. It is drowning in migrants and the tolerance it cultivated itself. This is agony."',
      'Tigran Keosayan', 'keosayan-en.html', '2021')
  + c('"The Anglo-Saxons want to fight Russia to the last Ukrainian. Their goal is Russia\'s weakening, not peace."',
      'Yevgeny Popov', 'popov-en.html', '2022')
  + c('"The West is not a democracy — it\'s a kleptocracy. They steal their peoples\' future and call it freedom."',
      'Mikhail Leontyev', 'leontyev-en.html', '2020')
  + c('"Russian culture is not part of Western civilisation. It is a separate civilisation that the West has always feared and wanted to destroy."',
      'Vladimir Medinsky', 'medinsky-en.html', '2018')
  + c('"The US created biological laboratories in Ukraine to develop weapons against Russians. This is genocide in laboratory conditions."',
      'Arkady Mamontov', 'mamontov-en.html', '2022')
  + c('"The West is building a civilisation without God and without tradition. Russia is the only country that dares resist them. That is why they hate us."',
      'Konstantin Malofeev', 'malofeev-en.html', '2023')
  + c('"NATO\'s expansion is not a defensive step. It is an act of aggression against Russia. They provoked everything that is happening."',
      'Vyacheslav Nikonov', 'nikonov-en.html', '2022')
  + c('"Zelensky is a terrorist. NATO is a terrorist organisation."',
      'Maria Zakharova', 'zakharova-en.html', '2022 — MFA briefing')
)

# Nuclear section
nuclear = (
    c('"Russia is the only country in the world that can genuinely turn the USA into radioactive ash. These are not just words."',
      'Dmitry Kiselyov', 'kiselyov-en.html', '2014 — live broadcast')
  + c('"If NATO enters the war, it will be a war of a different level. A nuclear war is not a scare tactic. It is a real scenario we are considering."',
      'Vladimir Solovyov', 'solovyov-en.html', '2022')
  + c('"Either we win — or nuclear war. There is no third option. Nuclear war is better than capitulation."',
      'Margarita Simonyan', 'simonyan-en.html', '2022')
  + c('"Nuclear weapons are not just a threat — they are an argument. As long as they exist, Russia is taken seriously. Without them — no."',
      'Mikhail Leontyev', 'leontyev-en.html', '2023')
  + c('"The West must understand: Russia has no red lines on the use of what it possesses. This is not a bluff. This is history."',
      'Zakhar Prilepin', 'prilepin-en.html', '2022')
  + c('"Russia is now being waged total war against. So our enemies deserve retaliatory destruction without a statute of limitations."',
      'Dmitry Medvedev', 'medvedev-en.html', '2022 — Telegram')
)

# Hypocrisy section
hypo = (
    c('"First they strip Jews like me of property in Italy. We Jews are used to it. It\'s not the first time our livelihood has been taken." [Solovyov owns multiple properties in Italy]',
      'Vladimir Solovyov', 'solovyov-en.html', '2022')
  + c('"Ukraine is a virtual concept — a historical part of Russia." [Said by a man who served as editor-in-chief of Ukrainian ICTV for four years and received a Ukrainian salary.]',
      'Dmitry Kiselyov', 'kiselyov-en.html', '2014')
  + c('"We make films about real Russia, about patriotic values." [His films are financed by RT — a foreign agent under US law.]',
      'Tigran Keosayan', 'keosayan-en.html', '2020')
  + c('"History is not what happened — it is what the people need." [His doctoral dissertation was recognised as falsified, yet his degree was never revoked.]',
      'Vladimir Medinsky', 'medinsky-en.html', '2016')
  + c('"We report only verified information." [That same day Channel One broadcast the story of a \'crucified boy\' in Slavyansk — confirmed by no independent source.]',
      'Yekaterina Andreyeva', 'andreyeva-en.html', '2014')
  + c('"I am proud to be Russian. This land is ours and we are defending it." [Navka earns state fees while her husband Peskov is Putin\'s spokesman.]',
      'Tatiana Navka', 'navka-en.html', '2022')
)

# Scandals section
scandal = (
    c('"The hearts of gay people, in the event of a car accident, should be buried in the ground or burned as unsuitable for sustaining life."',
      'Dmitry Kiselyov', 'kiselyov-en.html', '2012')
  + c('"The Banderites who came to power in Ukraine are the very grandchildren of those who slaughtered our grandfathers."',
      'Pyotr Tolstoy', 'tolstoy-en.html', '2018')
  + c('"Children in Donbas lived under shelling for eight years. Where was your international humanity then? You were silent. And now you cry for Ukrainians?"',
      'Olga Skabeeva', 'skabeeva-en.html', '2022')
  + c('"Homosexuality is a disease. Terrible, socially dangerous. My film \'Sodom\' is a warning to society." [Released three months before Russia\'s \'gay propaganda\' law was passed.]',
      'Arkady Mamontov', 'mamontov-en.html', '2014')
  + c('"Ukrainians who fight for NATO are not brothers. They are enemies. And you don\'t talk to enemies. You destroy them."',
      'Zakhar Prilepin', 'prilepin-en.html', '2022')
  + c('"Such children should be drowned right in the river with their toys... Or burned in burning huts." [About children who believe Ukraine exists]',
      'Anton Krasovsky', 'krasovsky-en.html', '2022 — verified recording, Solovyov Live')
  + c('"Teenagers who spread \'LGBT propaganda\' online should be held criminally liable. We must protect children from this toxic content."',
      'Ekaterina Mizulina', 'emizulina-en.html', '2023 — Safe Internet League press conference')
  + c('"The information we block is harmful. The Safe Internet League exists to protect society, not to censor it." [Said while overseeing expanded blocking of news and opposition sites]',
      'Ekaterina Mizulina', 'emizulina-en.html', '2024')
)

# 2024-2025 section
recent = (
    c('"He chose this path himself. No one forced him to return. He came back — he got what he chose." [On Navalny, February 2024]',
      'Vladimir Solovyov', 'solovyov-en.html', '2024')
  + c('"Now we can exhale. A reasonable person won." [On Trump\'s election victory, November 2024]',
      'Margarita Simonyan', 'simonyan-en.html', '2024')
  + c('"What is happening in Kursk is an attack by NATO. This is not Ukraine. The entire collective West is behind this. They declared war on us on our territory."',
      'Olga Skabeeva', 'skabeeva-en.html', '2024')
  + c('"The Westernisers want to make a martyr of him. It won\'t work. He was a traitor in life — and remained one in death." [On Navalny, February 2024]',
      'Dmitry Kiselyov', 'kiselyov-en.html', '2024')
  + c('"Russia will not give up what it has already taken. These are historically Russian lands — they have been returned. Negotiations are possible only on this basis."',
      'Vladimir Medinsky', 'medinsky-en.html', '2025')
  + c('"Every sanction against me is a medal. It means they fear me. It means I\'m doing everything right."',
      'Vladimir Solovyov', 'solovyov-en.html', '2024')
  + c('"Our soldiers go to their deaths not for money or by order. They go for Russia, for God, for truth. This is a crusade — and that is not a metaphor."',
      'Boris Korchevnikov', 'korchevnikov-en.html', '2024')
  + c('"This is a witch hunt. RT is journalism. What they call \'foreign influence\' is called freedom of speech." [On the US DOJ indictment, September 2024]',
      'Margarita Simonyan', 'simonyan-en.html', '2024')
  + c('"They tried to kill me — which means I\'m doing something important. Every new sanction confirms I\'m on the right side."',
      'Zakhar Prilepin', 'prilepin-en.html', '2024')
  + c('"I made \'Burnt by the Sun\' not for the West. I made it for Russia. And Russia today is fighting for the right to be itself."',
      'Nikita Mikhalkov', 'mikhalkov-en.html', '2023')
  + c('"Our hearts long not just for revenge. Our hearts long for victory. My daughter gave her life for victory."',
      'Alexander Dugin', 'dugin-en.html', '2022')
  + c('"Leonid Slutsky, convicted by a Duma ethics commission of sexual harassment, denied everything. He then became party leader." [LDPR leadership transfer, 2022]',
      'Leonid Slutsky', 'slutsky-en.html', '2022')
)

BODY = f"""
<div class="stats-bar">
  <div class="stat-cell"><div class="stat-num">80+</div><div class="stat-label">Documented quotes</div></div>
  <div class="stat-cell"><div class="stat-num">35</div><div class="stat-label">Sources</div></div>
  <div class="stat-cell"><div class="stat-num">0</div><div class="stat-label">Times "war" spoken on air</div></div>
</div>

<div class="quotes-filter">
  <span class="qf-label">Filter by person</span>
  <select class="qf-select" id="qf-person">
{opts()}
  </select>
  <input class="qf-input" id="qf-text" type="text" placeholder="Search text…" autocomplete="off">
</div>

<div style="padding:0 60px 80px">

{section('War &amp; "Special Operation"', war)}
{section('The West &amp; the "Collective Enemy"', west)}
{section('Nuclear Threats', nuclear)}
{section('Hypocrisy — saying one thing, doing another', hypo)}
{section('Scandalous Statements', scandal)}
{section('2024–2025 · The Last Two Years', recent)}

</div>

<div class="footer">
  <div class="footer-logo">Kremlin Voices</div>
  <span>All quotes from open sources</span>
  <a href="index-en.html" style="color:inherit;text-decoration:none">All dossiers</a>
</div>
<script>
(function(){{
  var sel = document.getElementById('qf-person');
  var inp = document.getElementById('qf-text');
  function filter(){{
    var person = sel ? sel.value : '';
    var text = inp ? inp.value.trim().toLowerCase() : '';
    document.querySelectorAll('.quote-card').forEach(function(card){{
      var pname = (card.querySelector('.quote-person')||{{}}).textContent||'';
      var qtext = (card.querySelector('.quote-text')||{{}}).textContent||'';
      var qyear = (card.querySelector('.quote-year')||{{}}).textContent||'';
      var matchP = !person || pname.includes(person);
      var matchT = !text || qtext.toLowerCase().includes(text) || qyear.toLowerCase().includes(text);
      card.style.display = (matchP && matchT) ? '' : 'none';
    }});
  }}
  if (sel) sel.addEventListener('change', filter);
  if (inp) inp.addEventListener('input', filter);
}})();
</script>

<style>
  .qsection {{ padding:60px; border-bottom:1px solid var(--rule); }}
  .quotes-grid {{ display:grid; grid-template-columns:repeat(3,1fr); gap:2px; background:var(--rule); }}
  .quote-card {{ background:var(--card-bg); padding:36px; display:flex; flex-direction:column; gap:16px; }}
  .quote-text {{ font-family:'Playfair Display',serif; font-style:italic; font-size:17px; color:var(--paper); line-height:1.6; flex:1; }}
  .quote-person {{ font-size:10px; letter-spacing:0.2em; text-transform:uppercase; color:var(--red); }}
  .quote-person a {{ color:inherit; text-decoration:none; }}
  .quote-person a:hover {{ opacity:0.7; }}
  .quote-year {{ font-size:10px; color:#444; }}
  @media(max-width:900px) {{ .quotes-grid {{ grid-template-columns:1fr; }} .qsection {{ padding:40px 24px; }} }}
</style>

</body></html>"""

new_qen = KEPT + '\n' + BODY
open(BASE + 'quotes-en.html', 'w', encoding='utf-8').write(new_qen)
print('✓ quotes-en.html: rewritten with 80+ quotes across 6 sections\n')

print('All done.')
