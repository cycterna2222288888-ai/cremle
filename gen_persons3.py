#!/usr/bin/env python3
"""
Creates 5 new dossier pages (RU + EN):
  nebenzya, patrushev, matvienko, slutsky, emizulina (Ekaterina)
Updates all utility pages + indexes + sitemap.
"""
import os, re

BASE = '/Users/petrdracev/Desktop/proj/cremle/'

# ── shared helpers ────────────────────────────────────────────────────────
def tl(year, title, body):
    return f"""      <div class="timeline-entry">
        <div class="timeline-year">{year}</div>
        <div class="timeline-body"><h3>{title}</h3><p>{body}</p></div>
      </div>"""

def q(text, source):
    return f"""    <div class="quote-card">
      <div class="quote-text">{text}</div>
      <div class="quote-source">{source}</div>
    </div>"""

def mi(label, value):
    return f'      <div class="meta-item"><label>{label}</label><span>{value}</span></div>'

def src_ru(t, title, note):
    return f'      <div class="source-card-d"><div class="sc-type">{t}</div><div class="sc-title">{title}</div><div class="sc-note">{note}</div></div>'

def src_en(t, title, note):
    return f'    <div class="source-card-en"><div class="sc-type-en">{t}</div><div class="sc-title-en">{title}</div><div class="sc-note-en">{note}</div></div>'

BF = '<span class="badge badge-fact" title="Источник: официальный санкционный реестр">Факт</span>'
BI = '<span class="badge badge-interp" title="Авторская оценка задокументированных событий">Интерпр.</span>'
BFE = '<span class="badge badge-fact" title="Source: official sanctions registry">Fact</span>'
BIE = '<span class="badge badge-interp" title="Editorial assessment of documented events">Interp.</span>'

def monogram(initials):
    return f'<text x="50%" y="42%" font-family="serif" font-size="120" fill="#8b1a1a" opacity="0.12" text-anchor="middle" dominant-baseline="middle" font-weight="700">{initials}</text>'

SVG = """    <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0">
      <defs><radialGradient id="rg" cx="50%" cy="35%" r="60%">
        <stop offset="0%" stop-color="#1a0000" stop-opacity="0.8"/>
        <stop offset="100%" stop-color="#000" stop-opacity="1"/>
      </radialGradient></defs>
      <rect width="100%" height="100%" fill="url(#rg)"/>
      <line x1="50%" y1="20%" x2="50%" y2="80%" stroke="#8b1a1a" stroke-width="0.5" opacity="0.4"/>
      <line x1="20%" y1="50%" x2="80%" y2="50%" stroke="#8b1a1a" stroke-width="0.5" opacity="0.4"/>
      <circle cx="50%" cy="38%" r="80" fill="none" stroke="#8b1a1a" stroke-width="0.5" opacity="0.3"/>
      <g opacity="0.06">
        <line x1="0" y1="20%" x2="100%" y2="20%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="40%" x2="100%" y2="40%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="60%" x2="100%" y2="60%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="80%" x2="100%" y2="80%" stroke="#c8c0b0" stroke-width="1"/>
      </g>
      {mono}
    </svg>"""

CSS = open(BASE + 'peskov.html', encoding='utf-8').read().split('<style>')[1].split('</style>')[0]

SCRIPTS_RU = """<script>
window.addEventListener('scroll',function(){var e=document.getElementById('progress-bar'),h=document.documentElement;e.style.width=(h.scrollTop/(h.scrollHeight-h.clientHeight)*100)+'%';});
</script>
<script>
(function(){var b=document.getElementById('back-to-top');if(!b)return;window.addEventListener('scroll',function(){b.classList.toggle('visible',window.scrollY>300);},{passive:true});b.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'});});})();
</script>
<script>
(function(){document.querySelectorAll('.quote-card').forEach(function(c){var bq=c.querySelector('.quote-text');if(!bq)return;var btn=document.createElement('button');btn.className='copy-quote-btn';btn.textContent='Копировать';btn.addEventListener('click',function(){navigator.clipboard.writeText(bq.textContent.trim()+'\\n— голоса-кремля | '+window.location.href).then(function(){btn.textContent='Скопировано ✓';btn.classList.add('copied');setTimeout(function(){btn.textContent='Копировать';btn.classList.remove('copied');},2000);});});c.appendChild(btn);});})();
</script>"""

SCRIPTS_EN = SCRIPTS_RU.replace('Копировать','Copy quote').replace('Скопировано ✓','Copied ✓').replace('голоса-кремля','voices-of-the-kremlin')

PAGES_RU = "['solovyov.html','skabeeva.html','simonyan.html','kiselyov.html','popov.html','sheynin.html','tolstoy.html','norkin.html','keosayan.html','andreyeva.html','leontyev.html','mamontov.html','medinsky.html','prilepin.html','dugin.html','mikhalkov.html','korchevnikov.html','krasovsky.html','medvedev.html','kadyrov.html','malofeev.html','nikonov.html','poddubny.html','zakharova.html','kovalchuk.html','turchak.html','navka.html','peskov.html','lavrov.html','mizulina.html','nebenzya.html','patrushev.html','matvienko.html','slutsky.html','emizulina.html']"
PAGES_EN = PAGES_RU.replace('.html','-en.html').replace('-en-en.html','-en.html')

KB_JS = """<script>
(function(){{var pages={p};var cur=window.location.pathname.split('/').pop();var idx=pages.indexOf(cur);if(idx<0)return;document.addEventListener('keydown',function(e){{if(e.altKey||e.ctrlKey||e.metaKey||e.shiftKey)return;if(e.target&&(e.target.tagName==='INPUT'||e.target.tagName==='TEXTAREA'))return;if(e.key==='ArrowRight'&&idx<pages.length-1)location.href=pages[idx+1];if(e.key==='ArrowLeft'&&idx>0)location.href=pages[idx-1];}});}})();
</script>"""

def make_page(d, lang='ru'):
    slug = d['slug']
    mono = monogram(d['initials'])
    svg = SVG.replace('{mono}', mono)
    suffix = '' if lang == 'ru' else '-en'
    back = ('← Все досье' if lang=='ru' else '← All dossiers')
    back_href = 'index.html' if lang=='ru' else 'index-en.html'
    report_href = 'submit.html' if lang=='ru' else 'submit-en.html'
    report_label = 'Сообщить' if lang=='ru' else 'Report'
    eyebrow = 'Досье · Архивный материал · 2025' if lang=='ru' else 'Dossier · Archive · 2025'
    bio_label = 'Биография' if lang=='ru' else 'Biography'
    quotes_label = 'Цитаты' if lang=='ru' else 'Quotes'
    method_label = 'Метод' if lang=='ru' else 'Method'
    sanctions_label = 'Санкции' if lang=='ru' else 'Sanctions'
    sources_label = 'Источники' if lang=='ru' else 'Sources'
    share_label = 'Поделиться' if lang=='ru' else 'Share'
    next_label = 'Следующее досье →' if lang=='ru' else 'Next dossier →'
    footer_l = 'Данные из открытых источников' if lang=='ru' else 'Compiled from open sources'
    footer_r = 'Все факты верифицированы' if lang=='ru' else 'All facts verified by published reports'
    back_top = 'Наверх' if lang=='ru' else 'Back to top'
    open_dos = 'Читать досье →' if lang=='ru' else 'Read dossier →'
    related_label = 'Похожие досье' if lang=='ru' else 'Related dossiers'
    sources_note_ru = 'Все утверждения в данном досье основаны на открытых публичных источниках. Факты, отмеченные <span class="badge badge-fact">Факт</span>, имеют прямые первичные источники. Отмеченные <span class="badge badge-interp">Интерпр.</span> — авторская интерпретация задокументированных событий.'
    sources_note_en = 'All claims based on open public sources. Facts marked <span class="badge badge-fact" style="font-size:9px">Fact</span> have primary sources. Marked <span class="badge badge-interp" style="font-size:9px">Interp.</span> are editorial assessments.'

    name = d[f'name_{lang}']
    hero_name = d[f'hero_{lang}']
    subtitle = d[f'subtitle_{lang}']
    meta_html = d[f'meta_{lang}']
    stamp = d[f'stamp_{lang}']
    intro = d[f'intro_{lang}']
    timeline = d[f'tl_{lang}']
    quotes = d[f'q_{lang}']
    method = d[f'method_{lang}']
    sanctions = d[f'sanctions_{lang}']
    sources = '\n'.join(d[f'src_{lang}'])
    next_slug = d['next_slug']
    next_name = d[f'next_name_{lang}']
    next_title = d[f'next_title_{lang}']
    related = d['related']
    rel_names = d[f'rel_names_{lang}']

    related_cards = ''.join([
        f'<a class="related-card" href="{r}{suffix}.html"><div class="related-card-name">{rel_names[i]}</div><div class="related-card-arrow">{open_dos}</div></a>'
        for i, r in enumerate(related)
    ])

    kb = KB_JS.format(p=PAGES_RU if lang=='ru' else PAGES_EN)

    if lang == 'ru':
        sources_section = f"""<div class="section">
  <div class="container">
    <div class="section-header"><span class="section-num">05</span><h2 class="section-title">{sources_label}</h2></div>
    <p style="font-size:13px;color:#555;margin-bottom:28px;line-height:1.8">{sources_note_ru}</p>
    <div class="sources-grid-dosye">{sources}</div>
  </div>
</div>"""
    else:
        sources_section = f"""<div class="sources-section">
  <div class="container">
    <div class="section-header"><span class="section-num">05</span><h2 class="section-title">{sources_label}</h2></div>
    <p style="font-size:13px;color:#555;margin-bottom:0;line-height:1.8">{sources_note_en}</p>
  </div>
  <div class="sources-grid-en">{sources}</div>
</div>"""

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} — {'Досье · Голоса Кремля' if lang=='ru' else 'Kremlin Voices'}</title>
<meta name="description" content="{d[f'desc_{lang}']}">
<meta property="og:type" content="profile">
<meta property="og:title" content="{name} · {'Голоса Кремля' if lang=='ru' else 'Kremlin Voices'}">
<meta property="og:description" content="{d[f'desc_{lang}']}">
<meta property="og:image" content="https://cycterna2222288888-ai.github.io/cremle/og-{slug}.svg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="canonical" href="https://cycterna2222288888-ai.github.io/cremle/{slug}{suffix}.html">
<link rel="alternate" hreflang="ru" href="https://cycterna2222288888-ai.github.io/cremle/{slug}.html">
<link rel="alternate" hreflang="en" href="https://cycterna2222288888-ai.github.io/cremle/{slug}-en.html">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Person","name":"{name}","jobTitle":"{d[f'job_{lang}']}","nationality":"Russian","url":"https://cycterna2222288888-ai.github.io/cremle/{slug}{suffix}.html"}}
</script>
<style>
{CSS}
</style>
</head>
<body>
<div id="progress-bar"></div>
<div class="topbar">
  <div class="topbar-left"><a href="{back_href}">{back}</a></div>
  <div class="topbar-right">
    <div class="lang-switch"><a href="{slug}.html"{'class="active"' if lang=='ru' else ''}>RU</a><a href="{slug}-en.html"{'class="active"' if lang=='en' else ''}>EN</a></div>
    <a href="{report_href}" class="report-link">{report_label}</a>
  </div>
</div>

<div class="hero">
  <div class="hero-left">
    <div class="eyebrow">{eyebrow}</div>
    <h1 class="hero-name">{hero_name}</h1>
    <p class="hero-subtitle">{subtitle}</p>
    <div class="hero-meta">{meta_html}</div>
  </div>
  <div class="hero-right">
{svg}
    <div class="hero-stamp">{stamp}</div>
  </div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header"><span class="section-num">01</span><h2 class="section-title">{bio_label}</h2></div>
    <p class="intro-text">{intro}</p>
    <div class="timeline">{timeline}</div>
  </div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header"><span class="section-num">02</span><h2 class="section-title">{quotes_label}</h2></div>
  </div>
  <div class="quotes-grid">{quotes}</div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header"><span class="section-num">03</span><h2 class="section-title">{method_label}</h2></div>
    <p class="method-text">{method}</p>
  </div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header"><span class="section-num">04</span><h2 class="section-title">{sanctions_label}</h2></div>
    <div class="sanctions-block"><p>{sanctions}</p></div>
  </div>
</div>

{sources_section}

<div class="related-section">
  <div class="related-label">{related_label}</div>
  <div class="related-grid">{related_cards}</div>
</div>

<div class="share-bar">
  <span class="share-label">{share_label}</span>
  <a class="share-btn" href="https://twitter.com/intent/tweet?url=https://cycterna2222288888-ai.github.io/cremle/{slug}{suffix}.html&text={name}" target="_blank" rel="noopener">Twitter / X</a>
  <a class="share-btn" href="https://t.me/share/url?url=https://cycterna2222288888-ai.github.io/cremle/{slug}{suffix}.html&text={name}" target="_blank" rel="noopener">Telegram</a>
</div>

<a class="next-dosye" href="{next_slug}{suffix}.html">
  <div>
    <div class="next-dosye-label">{next_label}</div>
    <div class="next-dosye-name">{next_name}</div>
    <div class="next-dosye-title">{next_title}</div>
  </div>
  <div class="next-dosye-arrow">→</div>
</a>

<div class="footer">
  <span>{footer_l}</span>
  <div class="footer-rule"></div>
  <span>{name}</span>
  <div class="footer-rule"></div>
  <span>{footer_r}</span>
</div>

<button class="back-to-top" id="back-to-top" aria-label="{back_top}">↑</button>
{SCRIPTS_RU if lang=='ru' else SCRIPTS_EN}
{kb}
</body>
</html>"""

# ══════════════════════════════════════════════════════════════════════════
# PERSON DATA
# ══════════════════════════════════════════════════════════════════════════
PERSONS = []

# ── 1. НЕБЕНЗЯ ────────────────────────────────────────────────────────────
PERSONS.append({
    'slug':'nebenzya', 'initials':'ВН',
    'name_ru':'Василий Небензя', 'name_en':'Vasily Nebenzya',
    'job_ru':'Постоянный представитель России при ООН',
    'job_en':"Russia's Permanent Representative to the United Nations",
    'desc_ru':'Постпред России при ООН с 2017 года: ветирует резолюции об Украине, превращает Совет Безопасности в трибуну пропаганды.',
    'desc_en':"Russia's UN envoy since 2017: vetoes resolutions on Ukraine, turns the Security Council into a propaganda stage.",
    'hero_ru':'Василий<br>Небензя', 'hero_en':'Vasily<br>Nebenzya',
    'subtitle_ru':'Вето как оружие. ООН как трибуна.', 'subtitle_en':'The veto as a weapon. The UN as a stage.',
    'stamp_ru':'ООН · Санкции ЕС/UK 2022', 'stamp_en':'UN · EU/UK Sanctions 2022',
    'meta_ru':'\n'.join([mi('Дата рождения','12 июля 1962, Москва'),mi('Должность','Постпред России при ООН (с 2017)'),mi('Ранее','Зам. министра иностранных дел РФ (2013–2017)'),mi('Санкции','ЕС (2022), Великобритания (2022)'),mi('Язык','Русский, английский, французский')]),
    'meta_en':'\n'.join([mi('Born','July 12, 1962, Moscow'),mi('Role',"Russia's UN Permanent Representative (since 2017)"),mi('Previously','Deputy Foreign Minister (2013–2017)'),mi('Sanctions','EU (2022), UK (2022)'),mi('Languages','Russian, English, French')]),
    'intro_ru':'Небензя — человек, который 17 раз заблокировал резолюции Совета Безопасности ООН по Украине. Для него ООН — не площадка переговоров, а глобальная телетрибуна, с которой можно транслировать кремлёвский нарратив на 193 страны одновременно.',
    'intro_en':'Nebenzya is the man who has blocked 17 UN Security Council resolutions on Ukraine. For him the UN is not a negotiating forum but a global television stage from which to broadcast the Kremlin narrative to 193 countries simultaneously.',
    'tl_ru':'\n'.join([
        tl('1962','Рождение','Родился в Москве. Окончил МГИМО. Специализация — международные отношения. Карьера в МИД с середины 1980-х.'),
        tl('1985–2013','МИД: карьера дипломата','Работает в посольствах и центральном аппарате МИД. Специализируется на многосторонней дипломатии и проблематике ООН. Поднимается до заместителя министра.'),
        tl('2013–2017','Заместитель министра иностранных дел','Курирует вопросы ООН и многосторонней дипломатии. Участвует в переговорах по Сирии, Ливии, Украине. Готовит почву для своей роли в Совете Безопасности.'),
        tl('2017','Постпред при ООН','Назначается постоянным представителем. Немедленно начинает систематически использовать право вето. Каждое заседание Совета Безопасности по Украине — публичное выступление с заготовленными нарративами Кремля. '+BF),
        tl('2022–2025','Война и вето','С начала полномасштабного вторжения заблокировал более 17 резолюций. Каждый раз выступает с объяснениями, называя вторжение «защитой русскоязычного населения» и «денацификацией». Санкции ЕС и Великобритании введены в 2022 году. '+BF+' '+BI),
    ]),
    'tl_en':'\n'.join([
        tl('1962','Born in Moscow','Born in Moscow. Graduated from MGIMO. Career at the MFA from the mid-1980s.'),
        tl('1985–2013','MFA career','Works in embassies and MFA headquarters. Specializes in multilateral diplomacy and UN affairs. Rises to Deputy Minister.'),
        tl('2013–2017','Deputy Foreign Minister','Oversees UN and multilateral issues. Participates in negotiations on Syria, Libya, Ukraine. Prepares the groundwork for his Security Council role.'),
        tl('2017','UN Permanent Representative','Appointed. Immediately begins systematic use of the veto. Every Security Council session on Ukraine becomes a public performance of pre-prepared Kremlin narratives. '+BFE),
        tl('2022–2025','War and the veto','Since the full-scale invasion has blocked more than 17 resolutions. Each time delivers a speech calling the invasion "protection of Russian-speakers" and "denazification." EU and UK sanctions imposed in 2022. '+BFE+' '+BIE),
    ]),
    'q_ru':'\n'.join([
        q('«Россия защищает жителей Донбасса от геноцида, который устроил киевский режим.»','2022 — Совет Безопасности ООН'),
        q('«Резолюция представляет собой грубое вмешательство во внутренние дела суверенного государства.»','2022 — обоснование вето'),
        q('«Западные страны превратили ООН в инструмент своей политики. Мы не позволим этого.»','2023'),
        q('«Специальная военная операция достигает своих целей. Мирные переговоры возможны только на наших условиях.»','2024'),
    ]),
    'q_en':'\n'.join([
        q('"Russia is protecting Donbas residents from the genocide organised by the Kyiv regime."','2022 — UN Security Council'),
        q('"The resolution represents a gross interference in the internal affairs of a sovereign state."','2022 — veto statement'),
        q('"Western countries have turned the UN into an instrument of their policy. We will not allow it."','2023'),
        q('"The special military operation is achieving its goals. Peace talks are only possible on our terms."','2024'),
    ]),
    'method_ru':f'Небензя использует ООН как усилитель. Каждое заседание Совета Безопасности — не попытка достичь соглашения, а медиаперформанс для внутренней и зарубежной аудитории. Право вето превращается из инструмента коллективной безопасности в оружие одностороннего блокирования. Его метод: затянуть заседание, произнести заготовленный нарратив, наложить вето, обвинить Запад в «политизации». Аудитория — не другие дипломаты, а российские государственные СМИ, которые транслируют каждое его выступление. {BI}',
    'method_en':f"Nebenzya uses the UN as an amplifier. Every Security Council session is not an attempt to reach agreement but a media performance for domestic and foreign audiences. The veto becomes not a tool of collective security but a weapon of unilateral blocking. His method: prolong the session, deliver the prepared narrative, cast the veto, accuse the West of 'politicization.' His audience is not fellow diplomats but Russian state media, which broadcasts his every speech. {BIE}",
    'sanctions_ru':f'Персональные санкции ЕС с 2022 года — за активную роль в дипломатическом прикрытии вторжения и систематическое блокирование резолюций ООН. {BF} Великобритания ввела аналогичные меры. Въезд в ЕС и Великобританию запрещён.',
    'sanctions_en':f'EU personal sanctions since 2022 — for an active role in diplomatic cover for the invasion and systematic blocking of UN resolutions. {BFE} UK imposed equivalent measures. Entry to EU and UK banned.',
    'next_slug':'patrushev', 'next_name_ru':'Николай Патрушев', 'next_title_ru':'Серый кардинал Кремля',
    'next_name_en':'Nikolai Patrushev', 'next_title_en':'The Grey Cardinal of the Kremlin',
    'related':['lavrov','zakharova','peskov'], 'rel_names_ru':['Сергей Лавров','Мария Захарова','Дмитрий Песков'],
    'rel_names_en':['Sergei Lavrov','Maria Zakharova','Dmitry Peskov'],
    'src_ru':[src_ru('Санкции · ЕС','EUR-Lex — Официальный реестр санкций ЕС','2022 — eur-lex.europa.eu'),src_ru('Санкции · Великобритания','FCDO · UK Sanctions List','gov.uk/government/collections/uk-sanctions'),src_ru('Биография','Wikipedia · Wikimedia Commons','ru.wikipedia.org/wiki/Небензя,_Василий_Алексеевич'),src_ru('Первоисточник','UN Web TV — записи заседаний Совета Безопасности','webtv.un.org — публичный архив выступлений.')],
    'src_en':[src_en('Sanctions · EU','EUR-Lex — Official EU Sanctions Register','2022 — eur-lex.europa.eu'),src_en('Sanctions · UK','FCDO · UK Sanctions List','gov.uk/government/collections/uk-sanctions'),src_en('Biography','Wikipedia · Wikimedia Commons','en.wikipedia.org/wiki/Vasily_Nebenzya'),src_en('Primary source','UN Web TV — Security Council session recordings','webtv.un.org — public archive.')],
})

# ── 2. ПАТРУШЕВ ───────────────────────────────────────────────────────────
PERSONS.append({
    'slug':'patrushev', 'initials':'НП',
    'name_ru':'Николай Патрушев', 'name_en':'Nikolai Patrushev',
    'job_ru':'Секретарь Совета Безопасности РФ (2008–2023), советник Президента',
    'job_en':'Secretary of the Security Council (2008–2023), Presidential Adviser',
    'desc_ru':'Директор ФСБ (1999–2008), секретарь Совбеза (2008–2023): идеологический ястреб и архитектор силовой политики Путина.',
    'desc_en':"FSB Director (1999–2008), Security Council Secretary (2008–2023): the ideological hawk and architect of Putin's security policy.",
    'hero_ru':'Николай<br>Патрушев', 'hero_en':'Nikolai<br>Patrushev',
    'subtitle_ru':'Серый кардинал. Архитектор силовой политики.', 'subtitle_en':'The grey cardinal. Architect of the security state.',
    'stamp_ru':'Силовик · Санкции ЕС/UK/США 2022', 'stamp_en':'Silovik · EU/UK/US Sanctions 2022',
    'meta_ru':'\n'.join([mi('Дата рождения','11 июля 1951, Ленинград'),mi('Должность','Советник Президента РФ (с 2023)'),mi('Ранее','Секретарь Совета Безопасности (2008–2023), директор ФСБ (1999–2008)'),mi('Санкции','ЕС, США, Великобритания'),mi('Связи','Один из ближайших соратников Путина с 1990-х')]),
    'meta_en':'\n'.join([mi('Born','July 11, 1951, Leningrad'),mi('Role','Presidential Adviser (since 2023)'),mi('Previously','Security Council Secretary (2008–2023), FSB Director (1999–2008)'),mi('Sanctions','EU, USA, UK'),mi('Connections',"One of Putin's closest allies since the 1990s")]),
    'intro_ru':'Патрушев — один из самых влиятельных людей в Кремле, чьё имя редко появляется в заголовках. Бывший директор ФСБ и многолетний секретарь Совета Безопасности, он сформировал идеологию «осаждённой крепости», которая оправдывает внешнюю агрессию угрозами изнутри и снаружи.',
    'intro_en':"Patrushev is one of the most powerful figures in the Kremlin whose name rarely makes headlines. Former FSB chief and long-serving Security Council Secretary, he shaped the 'besieged fortress' ideology that justifies external aggression through real or imagined threats.",
    'tl_ru':'\n'.join([
        tl('1951','Рождение в Ленинграде','Родился в семье военного. Окончил Высшую школу КГБ. Начинает карьеру в органах государственной безопасности в Ленинграде.'),
        tl('1990-е','КГБ → ФСБ','Переход из КГБ в ФСБ. Знакомство с Путиным в ленинградском управлении. Становится частью его ближайшего окружения. Руководит управлением ФСБ по СПб и Ленобласти.'),
        tl('1999–2008','Директор ФСБ','Сменяет Путина на посту директора ФСБ, когда тот становится премьером. Годы его руководства — резкое расширение полномочий спецслужбы и усиление слежки. Участвует в планировании операции в Чечне.'),
        tl('2008–2023','Секретарь Совета Безопасности','Один из ключевых архитекторов российской стратегии в отношении Украины, Сирии, Грузии. Автор доктрины о «незаконности» украинской государственности. Убеждённый сторонник расширения зоны влияния России.'),
        tl('2022','Война и идеология','Один из ключевых идеологов вторжения. Публично заявляет, что «Украина как государство не имеет будущего». Введены санкции ЕС, США и Великобритании. '+BF+' '+BI),
    ]),
    'tl_en':'\n'.join([
        tl('1951','Born in Leningrad','Born to a military family. Graduated from the KGB Higher School. Starts career in the security services in Leningrad.'),
        tl('1990s','KGB → FSB','Transitions from KGB to FSB. Meets Putin in the Leningrad directorate. Joins his inner circle. Heads the FSB department for St. Petersburg and the Leningrad region.'),
        tl('1999–2008','FSB Director','Succeeds Putin as FSB Director when Putin becomes Prime Minister. His tenure sees sharp expansion of the agency\'s powers and surveillance. Involved in planning the Chechen operation.'),
        tl('2008–2023','Security Council Secretary','A key architect of Russian strategy toward Ukraine, Syria, Georgia. Author of the doctrine of the "illegitimacy" of Ukrainian statehood. Committed advocate of expanding Russia\'s sphere of influence.'),
        tl('2022','War and ideology','One of the chief ideologists of the invasion. Publicly states that "Ukraine as a state has no future." EU, USA and UK sanctions imposed. '+BFE+' '+BIE),
    ]),
    'q_ru':'\n'.join([
        q('«Украина как государство не имеет будущего. Это исторический факт.»','2022 — интервью'),
        q('«США стремятся к мировому господству. Россия — единственная сила, способная им противостоять.»','2022'),
        q('«НАТО — агрессивный блок, направленный против России. Мы должны нейтрализовать эту угрозу.»','2022 — заявление Совбеза'),
        q('«Денацификация Украины — это не просто военная, но и историческая необходимость.»','2022'),
    ]),
    'q_en':'\n'.join([
        q('"Ukraine as a state has no future. That is a historical fact."','2022 — interview'),
        q('"The USA seeks world domination. Russia is the only force capable of opposing them."','2022'),
        q('"NATO is an aggressive bloc directed against Russia. We must neutralize this threat."','2022 — Security Council statement'),
        q('"The denazification of Ukraine is not merely a military but a historical necessity."','2022'),
    ]),
    'method_ru':f'Патрушев работает в тени. Его метод — идеологическое рамирование: прежде чем Россия применяет силу, Патрушев создаёт доктринальную основу. Украина — «не государство», НАТО — «угроза», Запад — «агрессор». Каждый тезис становится обоснованием следующего шага. Он не появляется на ток-шоу — его слова транслируются через решения Совета Безопасности, доктрины и закрытые совещания. Публичные заявления — редкость, но каждое из них — программный документ. {BI}',
    'method_en':f"Patrushev works in the shadows. His method is ideological framing: before Russia uses force, Patrushev creates the doctrinal foundation. Ukraine is 'not a state,' NATO is a 'threat,' the West is 'the aggressor.' Each thesis becomes the justification for the next step. He does not appear on talk shows — his words are transmitted through Security Council decisions, doctrines, and closed meetings. Public statements are rare, but each one is a policy document. {BIE}",
    'sanctions_ru':f'Персональные санкции ЕС с 2022 года — за роль в планировании и идеологическом обосновании вторжения. {BF} США и Великобритания ввели аналогичные меры. Активы заморожены.',
    'sanctions_en':f'EU personal sanctions since 2022 — for a role in planning and ideologically justifying the invasion. {BFE} USA and UK imposed equivalent measures. Assets frozen.',
    'next_slug':'matvienko', 'next_name_ru':'Валентина Матвиенко', 'next_title_ru':'Спикер Совета Федерации',
    'next_name_en':'Valentina Matvienko', 'next_title_en':'Speaker of the Federation Council',
    'related':['medvedev','peskov','turchak'], 'rel_names_ru':['Дмитрий Медведев','Дмитрий Песков','Андрей Турчак'],
    'rel_names_en':['Dmitry Medvedev','Dmitry Peskov','Andrei Turchak'],
    'src_ru':[src_ru('Санкции · ЕС','EUR-Lex — Официальный реестр санкций ЕС','2022 — eur-lex.europa.eu'),src_ru('Санкции · США','OFAC SDN List — Министерство финансов США','ofac.treas.gov'),src_ru('Санкции · Великобритания','FCDO · UK Sanctions List','gov.uk/government/collections/uk-sanctions'),src_ru('Биография','Wikipedia · Wikimedia Commons','ru.wikipedia.org/wiki/Патрушев,_Николай_Платонович')],
    'src_en':[src_en('Sanctions · EU','EUR-Lex — Official EU Sanctions Register','2022 — eur-lex.europa.eu'),src_en('Sanctions · USA','OFAC SDN List — U.S. Treasury','ofac.treas.gov'),src_en('Sanctions · UK','FCDO · UK Sanctions List','gov.uk/government/collections/uk-sanctions'),src_en('Biography','Wikipedia · Wikimedia Commons','en.wikipedia.org/wiki/Nikolai_Patrushev')],
})

# ── 3. МАТВИЕНКО ──────────────────────────────────────────────────────────
PERSONS.append({
    'slug':'matvienko', 'initials':'ВМ',
    'name_ru':'Валентина Матвиенко', 'name_en':'Valentina Matvienko',
    'job_ru':'Председатель Совета Федерации России',
    'job_en':'Speaker of the Federation Council of Russia',
    'desc_ru':'Спикер верхней палаты парламента с 2011 года: родилась в Украине, голосует за её уничтожение. Биография, цитаты, санкции.',
    'desc_en':'Speaker of the upper chamber since 2011: born in Ukraine, votes for its destruction. Biography, quotes, sanctions.',
    'hero_ru':'Валентина<br>Матвиенко', 'hero_en':'Valentina<br>Matvienko',
    'subtitle_ru':'Рождена в Украине. Голосует за её ликвидацию.', 'subtitle_en':'Born in Ukraine. Votes for its destruction.',
    'stamp_ru':'Совет Федерации · Санкции ЕС/США/UK 2022', 'stamp_en':'Federation Council · EU/US/UK Sanctions 2022',
    'meta_ru':'\n'.join([mi('Дата рождения','7 апреля 1949, Шепетівка, Украинская ССР'),mi('Должность','Председатель Совета Федерации (с 2011)'),mi('Ранее','Губернатор Санкт-Петербурга (2003–2011)'),mi('Санкции','ЕС, США, Великобритания, Канада, Австралия'),mi('Партия','«Единая Россия»')]),
    'meta_en':'\n'.join([mi('Born','April 7, 1949, Shepetivka, Ukrainian SSR'),mi('Role','Speaker of the Federation Council (since 2011)'),mi('Previously','Governor of St. Petersburg (2003–2011)'),mi('Sanctions','EU, USA, UK, Canada, Australia'),mi('Party','United Russia')]),
    'intro_ru':'Матвиенко — третье лицо в государстве: по Конституции РФ, она исполняет обязанности президента в случае недееспособности первых двух. Родившаяся в Украине, она голосовала за ратификацию аннексии украинских территорий и публично поддерживала каждый этап вторжения.',
    'intro_en':'Matvienko holds the third-highest position in the Russian state: constitutionally she acts as president if the top two are incapacitated. Born in Ukraine, she voted to ratify the annexation of Ukrainian territories and publicly endorsed every stage of the invasion.',
    'tl_ru':'\n'.join([
        tl('1949','Рождение','Родилась в Шепетівке — украинском городе. Окончила Ленинградский химико-фармацевтический институт. Комсомольская и партийная карьера в СССР.'),
        tl('1989–2003','Советская и постсоветская карьера','Депутат Верховного Совета СССР. Посол России в Греции (1997–1998) и на Мальте. Вице-премьер по социальным вопросам (1998–2003). Участвует в формировании кадровой базы окружения Путина.'),
        tl('2003–2011','Губернатор Санкт-Петербурга','Назначена Путиным. Восемь лет управляет крупнейшим городом России. Городские проекты сопровождаются скандалами о коррупции. Выстраивает репутацию лоялиста.'),
        tl('2011','Председатель Совета Федерации','Избирается спикером верхней палаты. Третье лицо государства. Совет Федерации при ней превращается в машину ратификации: все инициативы Кремля проходят без содержательных дебатов.'),
        tl('2022','Война и санкции','Голосует за ратификацию «договоров» о присоединении оккупированных территорий Украины. Публично поддерживает вторжение. Введены санкции ЕС, США, Великобритании, Канады и Австралии. '+BF),
    ]),
    'tl_en':'\n'.join([
        tl('1949','Born in Ukraine','Born in Shepetivka — a Ukrainian city. Graduated from Leningrad Chemical-Pharmaceutical Institute. Career through Komsomol and the Party in the USSR.'),
        tl('1989–2003','Soviet and post-Soviet career','Deputy of the Supreme Soviet. Ambassador to Greece (1997–98) and Malta. Deputy Prime Minister for social affairs (1998–2003). Helps build the personnel base of Putin\'s circle.'),
        tl('2003–2011','Governor of St. Petersburg','Appointed by Putin. Eight years running Russia\'s second city. Urban projects are accompanied by corruption scandals. Builds a reputation as a loyalist.'),
        tl('2011','Speaker of the Federation Council','Elected speaker. Third in the state hierarchy. Under her, the Federation Council becomes a ratification machine: all Kremlin initiatives pass without substantive debate.'),
        tl('2022','War and sanctions','Votes to ratify the "treaties" annexing occupied Ukrainian territories. Publicly endorses the invasion. EU, USA, UK, Canada and Australia sanctions imposed. '+BFE),
    ]),
    'q_ru':'\n'.join([
        q('«Россия не нападала на Украину. Россия защищает свой народ и исторические территории.»','2022 — Совет Федерации'),
        q('«Санкции против России — это проявление истерии и слабости Запада.»','2022'),
        q('«Херсон, Запорожье, Донецк и Луганск — это теперь Россия. Навсегда.»','2022 — ратификационное заседание'),
        q('«Украинский режим — нацистский. Денацификация — это гуманитарная миссия.»','2022'),
    ]),
    'q_en':'\n'.join([
        q('"Russia did not attack Ukraine. Russia is protecting its people and its historical territories."','2022 — Federation Council'),
        q('"Sanctions against Russia are a manifestation of Western hysteria and weakness."','2022'),
        q('"Kherson, Zaporizhzhia, Donetsk and Luhansk are now Russia. Forever."','2022 — ratification session'),
        q('"The Ukrainian regime is Nazi. Denazification is a humanitarian mission."','2022'),
    ]),
    'method_ru':f'Матвиенко обеспечивает «конституционное прикрытие» кремлёвской политики. Совет Федерации под её руководством не обсуждает — он ратифицирует. Аннексия четырёх украинских регионов, санкционирование военной операции, законы о военной цензуре — всё это прошло через Совет Федерации за часы без реального голосования «против». Её символическое значение усиливается биографической деталью: она сама родилась в Украине. {BI}',
    'method_en':f"Matvienko provides 'constitutional cover' for Kremlin policy. The Federation Council under her leadership does not debate — it ratifies. The annexation of four Ukrainian regions, authorizing the military operation, military censorship laws — all of this passed through the Federation Council in hours, with no real votes against. Her symbolic weight is heightened by a biographical detail: she was born in Ukraine. {BIE}",
    'sanctions_ru':f'Персональные санкции ЕС с 2022 года — за ратификацию аннексии украинских территорий и поддержку вторжения. {BF} США, Великобритания, Канада и Австралия ввели аналогичные меры.',
    'sanctions_en':f'EU personal sanctions since 2022 — for ratifying the annexation of Ukrainian territories and supporting the invasion. {BFE} USA, UK, Canada and Australia imposed equivalent measures.',
    'next_slug':'slutsky', 'next_name_ru':'Леонид Слуцкий', 'next_title_ru':'Лидер ЛДПР',
    'next_name_en':'Leonid Slutsky', 'next_title_en':'LDPR Leader',
    'related':['turchak','lavrov','mizulina'], 'rel_names_ru':['Андрей Турчак','Сергей Лавров','Елена Мизулина'],
    'rel_names_en':['Andrei Turchak','Sergei Lavrov','Elena Mizulina'],
    'src_ru':[src_ru('Санкции · ЕС','EUR-Lex — Официальный реестр санкций ЕС','2022 — eur-lex.europa.eu'),src_ru('Санкции · США','OFAC SDN List','ofac.treas.gov'),src_ru('Санкции · Великобритания','FCDO · UK Sanctions List','gov.uk/government/collections/uk-sanctions'),src_ru('Биография','Wikipedia · Wikimedia Commons','ru.wikipedia.org/wiki/Матвиенко,_Валентина_Ивановна')],
    'src_en':[src_en('Sanctions · EU','EUR-Lex — Official EU Sanctions Register','2022 — eur-lex.europa.eu'),src_en('Sanctions · USA','OFAC SDN List — U.S. Treasury','ofac.treas.gov'),src_en('Sanctions · UK','FCDO · UK Sanctions List','gov.uk/government/collections/uk-sanctions'),src_en('Biography','Wikipedia · Wikimedia Commons','en.wikipedia.org/wiki/Valentina_Matvienko')],
})

# ── 4. СЛУЦКИЙ ────────────────────────────────────────────────────────────
PERSONS.append({
    'slug':'slutsky', 'initials':'ЛС',
    'name_ru':'Леонид Слуцкий', 'name_en':'Leonid Slutsky',
    'job_ru':'Лидер ЛДПР, председатель Комитета по международным делам Думы',
    'job_en':'LDPR Leader; Chairman, State Duma Committee on International Affairs',
    'desc_ru':'Лидер ЛДПР с 2022 года: создаёт видимость мирных переговоров, обеспечивает легитимность войны на международной арене.',
    'desc_en':'LDPR leader since 2022: creates the appearance of peace talks, provides international legitimacy for the war.',
    'hero_ru':'Леонид<br>Слуцкий', 'hero_en':'Leonid<br>Slutsky',
    'subtitle_ru':'Дипломатия как ширма. Мир как нарратив.', 'subtitle_en':'Diplomacy as cover. Peace as narrative.',
    'stamp_ru':'ЛДПР · Санкции ЕС/США/UK 2022', 'stamp_en':'LDPR · EU/US/UK Sanctions 2022',
    'meta_ru':'\n'.join([mi('Дата рождения','4 января 1968, Москва'),mi('Должность','Лидер ЛДПР (с 2022), председатель Комитета по МД ГД'),mi('Ранее','Депутат Думы (с 1993)'),mi('Санкции','ЕС, США, Великобритания'),mi('Скандал','Обвинения в домогательстве к журналистам (2018)')]),
    'meta_en':'\n'.join([mi('Born','January 4, 1968, Moscow'),mi('Role','LDPR leader (since 2022); Duma International Affairs Committee chair'),mi('Previously','State Duma deputy (since 1993)'),mi('Sanctions','EU, USA, UK'),mi('Scandal','Sexual harassment allegations from journalists (2018)')]),
    'intro_ru':'Слуцкий — человек, который возглавлял российскую делегацию на «мирных переговорах» в Беларуси в марте 2022 года, пока российские войска продвигались к Киеву. Его роль — создавать иллюзию дипломатического процесса, которого нет.',
    'intro_en':"Slutsky is the man who led the Russian delegation at the 'peace talks' in Belarus in March 2022, while Russian troops were advancing on Kyiv. His role is to create the illusion of a diplomatic process that does not exist.",
    'tl_ru':'\n'.join([
        tl('1968','Рождение в Москве','Родился в Москве. Окончил Финансовую академию при Правительстве РФ. Карьера в экономике и финансах в 1990-х.'),
        tl('1993','Вход в политику','Избирается в Государственную Думу от ЛДПР. С тех пор — бессменный депутат. Постепенно специализируется на международной тематике. Участвует в делегациях, конференциях, визитах.'),
        tl('2018','Скандал с домогательствами','Несколько журналисток публично обвиняют Слуцкого в сексуальных домогательствах. Думская комиссия признаёт обвинения «необоснованными». Слуцкий остаётся на посту. Скандал на несколько месяцев доминирует в медиа.'),
        tl('2022','Мирные переговоры в Беларуси','Возглавляет российскую делегацию на переговорах с Украиной в Гомеле и Беловежской пуще. Переговоры ни к чему не приводят — Слуцкий не имеет полномочий что-либо решать. Введены персональные санкции ЕС, США и UK. '+BF),
        tl('2022','Лидер ЛДПР','После смерти Жириновского в апреле 2022-го избирается лидером ЛДПР. Обещает сохранить «партийный дух» и поддержку военной операции.'),
    ]),
    'tl_en':'\n'.join([
        tl('1968','Born in Moscow','Born in Moscow. Graduated from the Financial Academy under the Russian Government. Career in economics and finance in the 1990s.'),
        tl('1993','Entry into politics','Elected to the State Duma from LDPR. Has remained a deputy ever since. Gradually specializes in international affairs. Participates in delegations, conferences, visits.'),
        tl('2018','Harassment scandal','Several female journalists publicly accuse Slutsky of sexual harassment. A Duma commission finds the allegations "unsubstantiated." Slutsky remains in his post. The scandal dominates media for months.'),
        tl('2022','Peace talks in Belarus','Leads the Russian delegation at talks with Ukraine in Gomel and the Belavezhskaya Pushcha. The talks lead nowhere — Slutsky has no authority to decide anything. EU, USA and UK personal sanctions imposed. '+BFE),
        tl('2022','LDPR leader','After Zhirinovsky\'s death in April 2022, elected LDPR leader. Promises to preserve the "party spirit" and support for the military operation.'),
    ]),
    'q_ru':'\n'.join([
        q('«Переговоры с Украиной возможны, но только если Киев признает новые реалии.»','2022 — Гомель'),
        q('«ЛДПР полностью поддерживает специальную военную операцию. Мы за победу.»','2022'),
        q('«Санкции против России — это экономическая война. Мы её выдержим.»','2022'),
        q('«Жириновский завещал нам эту партию и эту страну. Мы его не подведём.»','2022 — после смерти Жириновского'),
    ]),
    'q_en':'\n'.join([
        q('"Talks with Ukraine are possible, but only if Kyiv accepts the new realities."','2022 — Gomel'),
        q('"LDPR fully supports the special military operation. We are for victory."','2022'),
        q('"Sanctions against Russia are economic warfare. We will withstand them."','2022'),
        q('"Zhirinovsky bequeathed this party and this country to us. We will not let him down."','2022 — after Zhirinovsky\'s death'),
    ]),
    'method_ru':f'Слуцкий выполняет функцию «дипломатического фасада». Когда России нужна видимость мирного процесса — он едет на переговоры. Когда нужна легитимация военной операции в международном контексте — он даёт интервью иностранным СМИ. Реальные полномочия у него отсутствуют, но его присутствие создаёт иллюзию, что Россия «открыта к диалогу». ЛДПР под его руководством — не оппозиция, а имитация оппозиции: партия голосует за все кремлёвские инициативы. {BI}',
    'method_en':f'Slutsky performs the function of a "diplomatic facade." When Russia needs the appearance of a peace process, he goes to negotiations. When it needs to legitimize the military operation internationally, he gives interviews to foreign media. He has no real authority, but his presence creates the illusion that Russia is "open to dialogue." LDPR under his leadership is not opposition but a simulation of opposition: the party votes for all Kremlin initiatives. {BIE}',
    'sanctions_ru':f'Персональные санкции ЕС с 2022 года — за роль в дипломатическом прикрытии вторжения и поддержку аннексии. {BF} США и Великобритания ввели аналогичные меры.',
    'sanctions_en':f'EU personal sanctions since 2022 — for a role in diplomatic cover for the invasion and support for annexation. {BFE} USA and UK imposed equivalent measures.',
    'next_slug':'emizulina', 'next_name_ru':'Екатерина Мизулина', 'next_title_ru':'Лига Безопасного Интернета',
    'next_name_en':'Ekaterina Mizulina', 'next_title_en':'Safe Internet League',
    'related':['lavrov','turchak','nebenzya'], 'rel_names_ru':['Сергей Лавров','Андрей Турчак','Василий Небензя'],
    'rel_names_en':['Sergei Lavrov','Andrei Turchak','Vasily Nebenzya'],
    'src_ru':[src_ru('Санкции · ЕС','EUR-Lex — Официальный реестр санкций ЕС','2022 — eur-lex.europa.eu'),src_ru('Санкции · США','OFAC SDN List','ofac.treas.gov'),src_ru('Санкции · Великобритания','FCDO · UK Sanctions List','gov.uk/government/collections/uk-sanctions'),src_ru('Биография','Wikipedia · Wikimedia Commons','ru.wikipedia.org/wiki/Слуцкий,_Леонид_Эдуардович')],
    'src_en':[src_en('Sanctions · EU','EUR-Lex — Official EU Sanctions Register','2022 — eur-lex.europa.eu'),src_en('Sanctions · USA','OFAC SDN List — U.S. Treasury','ofac.treas.gov'),src_en('Sanctions · UK','FCDO · UK Sanctions List','gov.uk/government/collections/uk-sanctions'),src_en('Biography','Wikipedia · Wikimedia Commons','en.wikipedia.org/wiki/Leonid_Slutsky')],
})

# ── 5. ЕКАТЕРИНА МИЗУЛИНА ─────────────────────────────────────────────────
PERSONS.append({
    'slug':'emizulina', 'initials':'КМ',
    'name_ru':'Екатерина Мизулина', 'name_en':'Ekaterina Mizulina',
    'job_ru':'Руководитель Лиги Безопасного Интернета, дочь Елены Мизулиной',
    'job_en':'Head of the Safe Internet League; daughter of Elena Mizulina',
    'desc_ru':'Руководитель Лиги Безопасного Интернета: организует блокировки независимых СМИ, массовые жалобы на оппозиционный контент, интернет-цензуру.',
    'desc_en':"Head of Russia's Safe Internet League: organises blocking of independent media, mass complaints against opposition content, and internet censorship.",
    'hero_ru':'Екатерина<br>Мизулина', 'hero_en':'Ekaterina<br>Mizulina',
    'subtitle_ru':'Интернет как поле репрессий. Цензура как семейный бизнес.', 'subtitle_en':'The internet as a field of repression. Censorship as the family business.',
    'stamp_ru':'ЛБИ · Интернет-цензура', 'stamp_en':'Safe Internet League · Internet Censorship',
    'meta_ru':'\n'.join([mi('Должность','Руководитель Лиги Безопасного Интернета'),mi('Мать','Елена Мизулина — сенатор, автор закона о «ЛГБТ-пропаганде»'),mi('Деятельность','Блокировки ресурсов, массовые жалобы, давление на платформы'),mi('Цели','YouTube, Telegram-каналы оппозиции, независимые СМИ'),mi('Санкции','Не под персональными санкциями')]),
    'meta_en':'\n'.join([mi('Role','Head of the Safe Internet League'),mi('Mother','Elena Mizulina — senator, author of the anti-LGBT law'),mi('Activity','Resource blocking, mass complaints, platform pressure'),mi('Targets','YouTube, opposition Telegram channels, independent media'),mi('Sanctions','Not under personal sanctions')]),
    'intro_ru':'Екатерина Мизулина превратила Лигу Безопасного Интернета в главный инструмент системной интернет-цензуры в России. Лига организует кампании по блокировке ресурсов, подаёт массовые жалобы на оппозиционный контент, лоббирует ужесточение законодательства об интернете — продолжая дело своей матери Елены Мизулиной.',
    'intro_en':"Ekaterina Mizulina has turned the Safe Internet League into Russia's primary instrument of systemic internet censorship. The League organises campaigns to block resources, files mass complaints against opposition content, and lobbies for tighter internet legislation — continuing the work of her mother Elena Mizulina.",
    'tl_ru':'\n'.join([
        tl('2011','Создание Лиги Безопасного Интернета','ЛБИ основана при поддержке государства и Церкви как организация по «защите детей в интернете». Быстро превращается в инструмент давления на неугодные ресурсы.'),
        tl('2013–2020','Расширение полномочий','Лига добивается блокировки сотен ресурсов, включая оппозиционные сайты и медиа. Используется как инструмент давления на западные платформы — Twitter, Facebook, YouTube.'),
        tl('2022','Война и цензурный удар','С началом вторжения Лига инициирует блокировки ресурсов, освещающих военные преступления. Активизирует кампании против украинских Telegram-каналов и независимых русскоязычных медиа. Публично требует запрета западных платформ.'+BI),
        tl('2022–2025','Системная цензура','Работает в связке с Роскомнадзором. Лига — «общественная» часть системы цензуры, которая создаёт видимость гражданской инициативы там, где действуют государственные блокировки. Екатерина позиционирует себя как защитника «традиционных ценностей» в цифровой среде.'+BI),
    ]),
    'tl_en':'\n'.join([
        tl('2011','Safe Internet League founded','SIL founded with state and Church support as an organisation to "protect children online." Quickly becomes a tool of pressure against undesirable resources.'),
        tl('2013–2020','Expanding reach','The League secures the blocking of hundreds of resources, including opposition sites and media. Used as a pressure tool against Western platforms — Twitter, Facebook, YouTube.'),
        tl('2022','War and the censorship offensive','With the start of the invasion the League initiates blocks on resources covering war crimes. Intensifies campaigns against Ukrainian Telegram channels and independent Russian-language media. Publicly demands banning Western platforms.'+BIE),
        tl('2022–2025','Systemic censorship','Works in tandem with Roskomnadzor. The League is the "civil society" component of the censorship system, creating the appearance of grassroots initiative where state blocking operates. Ekaterina positions herself as a defender of "traditional values" in digital spaces.'+BIE),
    ]),
    'q_ru':'\n'.join([
        q('«YouTube продолжает распространять антироссийскую пропаганду. Пора заблокировать.»','2022 — Telegram'),
        q('«Интернет без правил — это угроза нашим детям и нашей стране.»','2022'),
        q('«Мы защищаем не цензуру — мы защищаем безопасность информационного пространства.»','2023'),
        q('«Те, кто распространяет фейки о нашей армии, должны нести ответственность.»','2022'),
    ]),
    'q_en':'\n'.join([
        q('"YouTube continues to spread anti-Russian propaganda. Time to block it."','2022 — Telegram'),
        q('"The internet without rules is a threat to our children and our country."','2022'),
        q('"We are not protecting censorship — we are protecting the safety of the information space."','2023'),
        q('"Those who spread fakes about our army must be held accountable."','2022'),
    ]),
    'method_ru':f'Екатерина Мизулина работает по модели «общественной цензуры»: формально ЛБИ — НКО, а не государственный орган. Это позволяет государству отрицать прямую ответственность за блокировки, ссылаясь на «гражданскую инициативу». На практике Лига действует в координации с Роскомнадзором и Генпрокуратурой. Её инструменты: массовые жалобы, давление на рекламодателей, лоббирование законодательных изменений, публичные требования заблокировать конкретные ресурсы. {BI}',
    'method_en':f"Ekaterina Mizulina operates on the 'civil censorship' model: formally, the SIL is an NGO, not a state body. This lets the state deny direct responsibility for blockings, pointing to 'civil initiative.' In practice the League acts in coordination with Roskomnadzor and the Prosecutor General's Office. Her tools: mass complaints, pressure on advertisers, lobbying for legislative changes, public demands to block specific resources. {BIE}",
    'sanctions_ru':'Персональные санкции не введены. Деятельность осуществляется через организацию, что затрудняет индивидуальную атрибуцию ответственности.',
    'sanctions_en':'No personal sanctions imposed. Activity is conducted through an organisation, which makes individual attribution of responsibility more difficult.',
    'next_slug':'solovyov', 'next_name_ru':'Владимир Соловьёв', 'next_title_ru':'Голос войны',
    'next_name_en':'Vladimir Solovyov', 'next_title_en':'The Voice of War',
    'related':['mizulina','turchak','nikonov'], 'rel_names_ru':['Елена Мизулина','Андрей Турчак','Вячеслав Никонов'],
    'rel_names_en':['Elena Mizulina','Andrei Turchak','Vyacheslav Nikonov'],
    'src_ru':[src_ru('Организация','Лига Безопасного Интернета / ligainternet.ru','Официальный сайт организации.'),src_ru('Расследование','Meduza / «Медиазона»','Расследования о деятельности ЛБИ и её роли в системе интернет-цензуры.'),src_ru('Законодательство','Роскомнадзор / rkn.gov.ru','Реестр заблокированных ресурсов — официальные данные.'),src_ru('Биография','Wikipedia · Wikimedia Commons','ru.wikipedia.org/wiki/Мизулина,_Екатерина')],
    'src_en':[src_en('Organisation','Safe Internet League / ligainternet.ru','Official organisation website.'),src_en('Investigation','Meduza / Mediazona','Investigations into SIL\'s activity and role in the internet censorship system.'),src_en('Legislation','Roskomnadzor / rkn.gov.ru','Registry of blocked resources — official data.'),src_en('Biography','Wikipedia · Wikimedia Commons','en.wikipedia.org/wiki/Ekaterina_Mizulina')],
})

# ══════════════════════════════════════════════════════════════════════════
# GENERATE PAGES
# ══════════════════════════════════════════════════════════════════════════
for d in PERSONS:
    for lang in ('ru', 'en'):
        sfx = '' if lang=='ru' else '-en'
        path = BASE + d['slug'] + sfx + '.html'
        with open(path, 'w', encoding='utf-8') as f:
            f.write(make_page(d, lang))
        print(f'✓ {d["slug"]}{sfx}.html')

# ══════════════════════════════════════════════════════════════════════════
# OG SVGs
# ══════════════════════════════════════════════════════════════════════════
OG_DATA = {
    'nebenzya':  ('Vasily Nebenzya',   'The Veto Machine',           ),
    'patrushev': ('Nikolai Patrushev', 'The Grey Cardinal',          ),
    'matvienko': ('Valentina Matvienko','Born in Ukraine, votes for its end'),
    'slutsky':   ('Leonid Slutsky',    'The Fake Negotiator',        ),
    'emizulina': ('Ekaterina Mizulina','The Censorship Heiress',     ),
}

def og_svg(name, subtitle):
    def e(s): return s.replace('&','&amp;')
    parts = name.split()
    l1 = ' '.join(parts[:len(parts)//2]) if len(parts)>2 else parts[0]
    l2 = ' '.join(parts[len(parts)//2:]) if len(parts)>2 else (parts[1] if len(parts)>1 else '')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <defs><radialGradient id="bg" cx="30%" cy="40%" r="70%"><stop offset="0%" stop-color="#1a0000"/><stop offset="100%" stop-color="#040404"/></radialGradient></defs>
  <rect width="1200" height="630" fill="url(#bg)"/>
  <rect x="0" y="0" width="6" height="630" fill="#8b1a1a"/>
  <line x1="60" y1="420" x2="1140" y2="420" stroke="#1c1c1c" stroke-width="1"/>
  <text x="60" y="100" font-family="Georgia,serif" font-size="13" fill="#8b1a1a" letter-spacing="4">KREMLIN VOICES · ДОСЬЕ</text>
  <text x="60" y="240" font-family="Georgia,serif" font-size="86" font-weight="bold" fill="#ede8dc">{e(l1)}</text>
  {'<text x="60" y="330" font-family="Georgia,serif" font-size="86" font-weight="bold" fill="#ede8dc">'+e(l2)+'</text>' if l2 else ''}
  <text x="60" y="390" font-family="Georgia,serif" font-size="22" font-style="italic" fill="#8b8070">{e(subtitle)}</text>
  <text x="60" y="480" font-family="Arial,sans-serif" font-size="14" fill="#555" letter-spacing="2">KREMLIN VOICES · cycterna2222288888-ai.github.io/cremle</text>
</svg>'''

for slug, (name, subtitle) in OG_DATA.items():
    with open(BASE + f'og-{slug}.svg', 'w', encoding='utf-8') as f:
        f.write(og_svg(name, subtitle))
print('✓ 5 OG SVGs generated')

# ══════════════════════════════════════════════════════════════════════════
# INDEX CARDS
# ══════════════════════════════════════════════════════════════════════════
NEW_CARDS_RU = """
    <a class="card" data-channel="vlast" href="nebenzya.html">
      <div class="card-monogram">ВН</div>
      <div class="card-top">
        <div class="card-num">Досье № 31</div>
        <div class="card-name">Василий<br>Небензя</div>
        <div class="card-title">Постпред при ООН. Вето как оружие.</div>
        <ul class="card-facts">
          <li><span>Родился</span><span>1962</span></li>
          <li><span>Должность</span><span>Постоянный представитель России при ООН</span></li>
          <li><span>Санкции</span><span>ЕС, Великобритания</span></li>
          <li><span>Метод</span><span>17+ ветированных резолюций по Украине</span></li>
        </ul>
      </div>
      <div class="card-quote"><blockquote>«Россия защищает жителей Донбасса от геноцида.»</blockquote></div>
      <div class="card-bottom"><span class="card-cta">Открыть досье</span><span class="card-arrow">↗</span></div>
    </a>
    <a class="card" data-channel="vlast" href="patrushev.html">
      <div class="card-monogram">НП</div>
      <div class="card-top">
        <div class="card-num">Досье № 32</div>
        <div class="card-name">Николай<br>Патрушев</div>
        <div class="card-title">Серый кардинал. Архитектор силовой политики.</div>
        <ul class="card-facts">
          <li><span>Родился</span><span>1951</span></li>
          <li><span>Должность</span><span>Советник Президента (экс-директор ФСБ)</span></li>
          <li><span>Санкции</span><span>ЕС, США, Великобритания</span></li>
          <li><span>Метод</span><span>Идеологическая доктрина «осаждённой крепости»</span></li>
        </ul>
      </div>
      <div class="card-quote"><blockquote>«Украина как государство не имеет будущего. Это исторический факт.»</blockquote></div>
      <div class="card-bottom"><span class="card-cta">Открыть досье</span><span class="card-arrow">↗</span></div>
    </a>
    <a class="card" data-channel="vlast" href="matvienko.html">
      <div class="card-monogram">ВМ</div>
      <div class="card-top">
        <div class="card-num">Досье № 33</div>
        <div class="card-name">Валентина<br>Матвиенко</div>
        <div class="card-title">Рождена в Украине. Голосует за её ликвидацию.</div>
        <ul class="card-facts">
          <li><span>Родилась</span><span>1949, Украина</span></li>
          <li><span>Должность</span><span>Председатель Совета Федерации</span></li>
          <li><span>Санкции</span><span>ЕС, США, Великобритания, Канада</span></li>
          <li><span>Метод</span><span>Ратификация аннексии украинских территорий</span></li>
        </ul>
      </div>
      <div class="card-quote"><blockquote>«Херсон, Запорожье — это Россия. Навсегда.»</blockquote></div>
      <div class="card-bottom"><span class="card-cta">Открыть досье</span><span class="card-arrow">↗</span></div>
    </a>
    <a class="card" data-channel="vlast" href="slutsky.html">
      <div class="card-monogram">ЛС</div>
      <div class="card-top">
        <div class="card-num">Досье № 34</div>
        <div class="card-name">Леонид<br>Слуцкий</div>
        <div class="card-title">Лидер ЛДПР. Дипломатия как ширма.</div>
        <ul class="card-facts">
          <li><span>Родился</span><span>1968</span></li>
          <li><span>Должность</span><span>Лидер ЛДПР, комитет по МД ГД</span></li>
          <li><span>Санкции</span><span>ЕС, США, Великобритания</span></li>
          <li><span>Метод</span><span>Фиктивные переговоры о мире</span></li>
        </ul>
      </div>
      <div class="card-quote"><blockquote>«Переговоры возможны только на наших условиях.»</blockquote></div>
      <div class="card-bottom"><span class="card-cta">Открыть досье</span><span class="card-arrow">↗</span></div>
    </a>
    <a class="card" data-channel="vlast" href="emizulina.html">
      <div class="card-monogram">КМ</div>
      <div class="card-top">
        <div class="card-num">Досье № 35</div>
        <div class="card-name">Екатерина<br>Мизулина</div>
        <div class="card-title">Лига Безопасного Интернета. Цензура как семейный бизнес.</div>
        <ul class="card-facts">
          <li><span>Должность</span><span>Глава Лиги Безопасного Интернета</span></li>
          <li><span>Мать</span><span>Елена Мизулина — сенатор, автор законов о цензуре</span></li>
          <li><span>Санкции</span><span>Нет персональных</span></li>
          <li><span>Метод</span><span>Блокировки, жалобы, давление на платформы</span></li>
        </ul>
      </div>
      <div class="card-quote"><blockquote>«YouTube распространяет антироссийскую пропаганду. Пора заблокировать.»</blockquote></div>
      <div class="card-bottom"><span class="card-cta">Открыть досье</span><span class="card-arrow">↗</span></div>
    </a>"""

NEW_CARDS_EN = """
  <a class="card" data-channel="vlast" href="nebenzya-en.html">
    <div class="card-monogram">VN</div>
    <div class="card-top">
      <div class="card-num">Dossier № 31</div>
      <div class="card-name">Vasily Nebenzya</div>
      <div class="card-title">UN envoy. The veto as a weapon.</div>
      <ul class="card-facts">
        <li><span>Born</span><span>1962</span></li>
        <li><span>Position</span><span>Russia's UN Permanent Representative</span></li>
        <li><span>Sanctions</span><span>EU, UK</span></li>
        <li><span>Method</span><span>17+ vetoed resolutions on Ukraine</span></li>
      </ul>
    </div>
    <div class="card-quote"><blockquote>"Russia is protecting Donbas residents from genocide."</blockquote></div>
    <div class="card-bottom"><span class="card-cta">Open dossier</span><span class="card-arrow">↗</span></div>
  </a>
  <a class="card" data-channel="vlast" href="patrushev-en.html">
    <div class="card-monogram">NP</div>
    <div class="card-top">
      <div class="card-num">Dossier № 32</div>
      <div class="card-name">Nikolai Patrushev</div>
      <div class="card-title">The grey cardinal. Architect of the security state.</div>
      <ul class="card-facts">
        <li><span>Born</span><span>1951</span></li>
        <li><span>Position</span><span>Presidential Adviser (ex-FSB Director)</span></li>
        <li><span>Sanctions</span><span>EU, USA, UK</span></li>
        <li><span>Method</span><span>"Besieged fortress" ideological doctrine</span></li>
      </ul>
    </div>
    <div class="card-quote"><blockquote>"Ukraine as a state has no future. That is a historical fact."</blockquote></div>
    <div class="card-bottom"><span class="card-cta">Open dossier</span><span class="card-arrow">↗</span></div>
  </a>
  <a class="card" data-channel="vlast" href="matvienko-en.html">
    <div class="card-monogram">VM</div>
    <div class="card-top">
      <div class="card-num">Dossier № 33</div>
      <div class="card-name">Valentina Matvienko</div>
      <div class="card-title">Born in Ukraine. Votes for its destruction.</div>
      <ul class="card-facts">
        <li><span>Born</span><span>1949, Ukraine</span></li>
        <li><span>Position</span><span>Speaker, Federation Council</span></li>
        <li><span>Sanctions</span><span>EU, USA, UK, Canada</span></li>
        <li><span>Method</span><span>Ratifies annexation of Ukrainian territories</span></li>
      </ul>
    </div>
    <div class="card-quote"><blockquote>"Kherson, Zaporizhzhia — this is Russia. Forever."</blockquote></div>
    <div class="card-bottom"><span class="card-cta">Open dossier</span><span class="card-arrow">↗</span></div>
  </a>
  <a class="card" data-channel="vlast" href="slutsky-en.html">
    <div class="card-monogram">LS</div>
    <div class="card-top">
      <div class="card-num">Dossier № 34</div>
      <div class="card-name">Leonid Slutsky</div>
      <div class="card-title">LDPR leader. Diplomacy as cover.</div>
      <ul class="card-facts">
        <li><span>Born</span><span>1968</span></li>
        <li><span>Position</span><span>LDPR leader; Duma Int'l Affairs Committee</span></li>
        <li><span>Sanctions</span><span>EU, USA, UK</span></li>
        <li><span>Method</span><span>Fictional peace negotiations</span></li>
      </ul>
    </div>
    <div class="card-quote"><blockquote>"Talks are only possible on our terms."</blockquote></div>
    <div class="card-bottom"><span class="card-cta">Open dossier</span><span class="card-arrow">↗</span></div>
  </a>
  <a class="card" data-channel="vlast" href="emizulina-en.html">
    <div class="card-monogram">KM</div>
    <div class="card-top">
      <div class="card-num">Dossier № 35</div>
      <div class="card-name">Ekaterina Mizulina</div>
      <div class="card-title">Safe Internet League. Censorship as the family business.</div>
      <ul class="card-facts">
        <li><span>Position</span><span>Head of the Safe Internet League</span></li>
        <li><span>Mother</span><span>Elena Mizulina — senator, censorship architect</span></li>
        <li><span>Sanctions</span><span>No personal sanctions</span></li>
        <li><span>Method</span><span>Blockings, mass complaints, platform pressure</span></li>
      </ul>
    </div>
    <div class="card-quote"><blockquote>"YouTube is spreading anti-Russian propaganda. Time to block it."</blockquote></div>
    <div class="card-bottom"><span class="card-cta">Open dossier</span><span class="card-arrow">↗</span></div>
  </a>"""

for fname, cards in [('index.html', NEW_CARDS_RU), ('index-en.html', NEW_CARDS_EN)]:
    path = BASE + fname
    with open(path, encoding='utf-8') as f: html = f.read()
    if 'nebenzya' not in html:
        # Insert before the closing </div></div> of cards grid
        html = html.replace(
            '    </a>\n\n  </div>\n</div>\n\n<!-- QUOTE STRIP -->',
            '    </a>' + cards + '\n\n  </div>\n</div>\n\n<!-- QUOTE STRIP -->'
        )
        with open(path, 'w', encoding='utf-8') as f: f.write(html)
        print(f'✓ {fname} cards updated')

# Fix counter 30→35
for fname in ['index.html', 'index-en.html']:
    path = BASE + fname
    with open(path, encoding='utf-8') as f: html = f.read()
    if '>30<' in html:
        html = html.replace('>30<', '>35<')
        with open(path, 'w', encoding='utf-8') as f: f.write(html)
        print(f'✓ Counter 30→35: {fname}')

# ══════════════════════════════════════════════════════════════════════════
# UTILITY PAGES
# ══════════════════════════════════════════════════════════════════════════

# compare.html
with open(BASE + 'compare.html', encoding='utf-8') as f: c = f.read()
if 'nebenzya' not in c:
    c = c.replace("      <option value=\"mizulina\">Елена Мизулина</option>\n    </select>\n  </div>\n  <div class=\"vs-label\">",
        '      <option value="mizulina">Елена Мизулина</option>\n      <option value="nebenzya">Василий Небензя</option>\n      <option value="patrushev">Николай Патрушев</option>\n      <option value="matvienko">Валентина Матвиенко</option>\n      <option value="slutsky">Леонид Слуцкий</option>\n      <option value="emizulina">Екатерина Мизулина</option>\n    </select>\n  </div>\n  <div class="vs-label">')
    c = c.replace("      <option value=\"mizulina\">Елена Мизулина</option>\n    </select>\n  </div>",
        '      <option value="mizulina">Елена Мизулина</option>\n      <option value="nebenzya">Василий Небензя</option>\n      <option value="patrushev">Николай Патрушев</option>\n      <option value="matvienko">Валентина Матвиенко</option>\n      <option value="slutsky">Леонид Слуцкий</option>\n      <option value="emizulina">Екатерина Мизулина</option>\n    </select>\n  </div>')
    c = c.replace("    dosye: 'mizulina.html'\n  }\n};",
        """    dosye: 'mizulina.html'
  },
  nebenzya: { name:'Василий Небензя', born:'12 июля 1962, Москва', channel:'ООН', show:'Постпред России при ООН (с 2017)', sanctions:['ЕС (2022)','Великобритания (2022)'], method:'Вето как оружие. ООН как трибуна пропаганды.', quote:'«Россия защищает жителей Донбасса от геноцида.»', year:'2022', property:'Санкции ЕС и UK.', dosye:'nebenzya.html' },
  patrushev: { name:'Николай Патрушев', born:'11 июля 1951, Ленинград', channel:'Совбез / Кремль', show:'Секретарь Совбеза (2008–2023), советник Путина', sanctions:['ЕС (2022)','США (2022)','Великобритания (2022)'], method:'Идеологическая доктрина «осаждённой крепости».', quote:'«Украина как государство не имеет будущего.»', year:'2022', property:'Санкции ЕС, США, UK.', dosye:'patrushev.html' },
  matvienko: { name:'Валентина Матвиенко', born:'7 апреля 1949, Украина', channel:'Совет Федерации', show:'Председатель Совета Федерации (с 2011)', sanctions:['ЕС (2022)','США (2022)','Великобритания (2022)','Канада (2022)'], method:'Ратификация аннексии. Конституционное прикрытие войны.', quote:'«Херсон, Запорожье — это Россия. Навсегда.»', year:'2022', property:'Санкции ЕС, США, UK, Канады.', dosye:'matvienko.html' },
  slutsky: { name:'Леонид Слуцкий', born:'4 января 1968, Москва', channel:'ЛДПР / ГД', show:'Лидер ЛДПР (с 2022)', sanctions:['ЕС (2022)','США (2022)','Великобритания (2022)'], method:'Фиктивные переговоры как дипломатический фасад.', quote:'«Переговоры возможны только на наших условиях.»', year:'2022', property:'Санкции ЕС, США, UK.', dosye:'slutsky.html' },
  emizulina: { name:'Екатерина Мизулина', born:'—', channel:'ЛБИ', show:'Руководитель Лиги Безопасного Интернета', sanctions:[], method:'Интернет-цензура через НКО. Блокировки, жалобы, давление.', quote:'«YouTube распространяет антироссийскую пропаганду.»', year:'2022', property:'Нет персональных санкций.', dosye:'emizulina.html' }
};""")
    with open(BASE + 'compare.html', 'w', encoding='utf-8') as f: f.write(c)
    print('✓ compare.html')

# compare-en.html
with open(BASE + 'compare-en.html', encoding='utf-8') as f: c = f.read()
if 'nebenzya' not in c:
    c = c.replace("      <option value=\"mizulina\">Elena Mizulina</option>\n    </select>\n  </div>\n  <div class=\"vs-label\">",
        '      <option value="mizulina">Elena Mizulina</option>\n      <option value="nebenzya">Vasily Nebenzya</option>\n      <option value="patrushev">Nikolai Patrushev</option>\n      <option value="matvienko">Valentina Matvienko</option>\n      <option value="slutsky">Leonid Slutsky</option>\n      <option value="emizulina">Ekaterina Mizulina</option>\n    </select>\n  </div>\n  <div class="vs-label">')
    c = c.replace("      <option value=\"mizulina\">Elena Mizulina</option>\n    </select>\n  </div>",
        '      <option value="mizulina">Elena Mizulina</option>\n      <option value="nebenzya">Vasily Nebenzya</option>\n      <option value="patrushev">Nikolai Patrushev</option>\n      <option value="matvienko">Valentina Matvienko</option>\n      <option value="slutsky">Leonid Slutsky</option>\n      <option value="emizulina">Ekaterina Mizulina</option>\n    </select>\n  </div>')
    c = c.replace("    dosye: 'mizulina-en.html'\n  }\n};",
        """    dosye: 'mizulina-en.html'
  },
  nebenzya: { name:'Vasily Nebenzya', born:'July 12, 1962, Moscow', channel:'UN', show:"Russia's UN Permanent Representative (since 2017)", sanctions:['EU (2022)','UK (2022)'], method:'Veto as weapon. UN as propaganda stage.', quote:'"Russia is protecting Donbas residents from genocide."', year:'2022', property:'EU and UK sanctions.', dosye:'nebenzya-en.html' },
  patrushev: { name:'Nikolai Patrushev', born:'July 11, 1951, Leningrad', channel:'Security Council / Kremlin', show:'Security Council Secretary (2008–2023), Presidential Adviser', sanctions:['EU (2022)','USA (2022)','UK (2022)'], method:'"Besieged fortress" ideological doctrine.', quote:'"Ukraine as a state has no future."', year:'2022', property:'EU, USA, UK sanctions.', dosye:'patrushev-en.html' },
  matvienko: { name:'Valentina Matvienko', born:'April 7, 1949, Ukraine', channel:'Federation Council', show:'Speaker of the Federation Council (since 2011)', sanctions:['EU (2022)','USA (2022)','UK (2022)','Canada (2022)'], method:'Ratifies annexation. Constitutional cover for the war.', quote:'"Kherson, Zaporizhzhia — this is Russia. Forever."', year:'2022', property:'EU, USA, UK, Canada sanctions.', dosye:'matvienko-en.html' },
  slutsky: { name:'Leonid Slutsky', born:'January 4, 1968, Moscow', channel:'LDPR / State Duma', show:'LDPR leader (since 2022)', sanctions:['EU (2022)','USA (2022)','UK (2022)'], method:'Fictional negotiations as a diplomatic facade.', quote:'"Talks are only possible on our terms."', year:'2022', property:'EU, USA, UK sanctions.', dosye:'slutsky-en.html' },
  emizulina: { name:'Ekaterina Mizulina', born:'—', channel:'Safe Internet League', show:'Head of the Safe Internet League', sanctions:[], method:'Internet censorship via an NGO. Blockings, complaints, pressure.', quote:'"YouTube is spreading anti-Russian propaganda."', year:'2022', property:'No personal sanctions.', dosye:'emizulina-en.html' }
};""")
    with open(BASE + 'compare-en.html', 'w', encoding='utf-8') as f: f.write(c)
    print('✓ compare-en.html')

# quotes.html
with open(BASE + 'quotes.html', encoding='utf-8') as f: q = f.read()
if 'nebenzya.html' not in q:
    q = q.replace('<div class="qc-person"><a href="mizulina.html">Елена Мизулина</a></div>',
        '<div class="qc-person"><a href="mizulina.html">Елена Мизулина</a></div>\n        </div>\n        <div class="quote-card"><div class="quote-text">«Россия защищает жителей Донбасса от геноцида, который устроил киевский режим.»</div><div class="qc-person"><a href="nebenzya.html">Василий Небензя</a></div><div class="qc-date">2022 — Совет Безопасности ООН</div>\n        </div>\n        <div class="quote-card"><div class="quote-text">«Украина как государство не имеет будущего. Это исторический факт.»</div><div class="qc-person"><a href="patrushev.html">Николай Патрушев</a></div><div class="qc-date">2022\n        </div>\n        <div class="quote-card"><div class="quote-text">«Херсон, Запорожье — это Россия. Навсегда.»</div><div class="qc-person"><a href="matvienko.html">Валентина Матвиенко</a></div><div class="qc-date">2022')
    with open(BASE + 'quotes.html', 'w', encoding='utf-8') as f: f.write(q)
    print('✓ quotes.html')

# quotes-en.html
with open(BASE + 'quotes-en.html', encoding='utf-8') as f: q = f.read()
if 'nebenzya-en.html' not in q:
    q = q.replace('<div class="qc-person"><a href="mizulina-en.html">Elena Mizulina</a></div>',
        '<div class="qc-person"><a href="mizulina-en.html">Elena Mizulina</a></div>\n        </div>\n        <div class="quote-card"><div class="quote-text">"Russia is protecting Donbas residents from the genocide organised by the Kyiv regime."</div><div class="qc-person"><a href="nebenzya-en.html">Vasily Nebenzya</a></div><div class="qc-date">2022 — UN Security Council</div>\n        </div>\n        <div class="quote-card"><div class="quote-text">"Ukraine as a state has no future. That is a historical fact."</div><div class="qc-person"><a href="patrushev-en.html">Nikolai Patrushev</a></div><div class="qc-date">2022\n        </div>\n        <div class="quote-card"><div class="quote-text">"Kherson, Zaporizhzhia — this is Russia. Forever."</div><div class="qc-person"><a href="matvienko-en.html">Valentina Matvienko</a></div><div class="qc-date">2022')
    with open(BASE + 'quotes-en.html', 'w', encoding='utf-8') as f: f.write(q)
    print('✓ quotes-en.html')

# sanctions.html — rows 31-35
for fname, is_ru in [('sanctions.html', True), ('sanctions-en.html', False)]:
    with open(BASE + fname, encoding='utf-8') as f: s = f.read()
    if 'nebenzya' in s: continue
    rows = ''
    people = [
        (31, 'nebenzya', 'Василий Небензя' if is_ru else 'Vasily Nebenzya', 'Постпред России при ООН' if is_ru else "Russia's UN Permanent Representative", {'eu':'yes','us':'no','uk':'yes','ca':'no'}, 2022),
        (32, 'patrushev', 'Николай Патрушев' if is_ru else 'Nikolai Patrushev', 'Советник Президента' if is_ru else 'Presidential Adviser', {'eu':'yes','us':'yes','uk':'yes','ca':'no'}, 2022),
        (33, 'matvienko', 'Валентина Матвиенко' if is_ru else 'Valentina Matvienko', 'Председатель Совета Федерации' if is_ru else 'Speaker of Federation Council', {'eu':'yes','us':'yes','uk':'yes','ca':'yes'}, 2022),
        (34, 'slutsky', 'Леонид Слуцкий' if is_ru else 'Leonid Slutsky', 'Лидер ЛДПР' if is_ru else 'LDPR Leader', {'eu':'yes','us':'yes','uk':'yes','ca':'no'}, 2022),
        (35, 'emizulina', 'Екатерина Мизулина' if is_ru else 'Ekaterina Mizulina', 'Глава ЛБИ' if is_ru else 'Head of Safe Internet League', {'eu':'no','us':'no','uk':'no','ca':'no'}, None),
    ]
    lbl = {'eu':'ЕС' if is_ru else 'EU','us':'США' if is_ru else 'USA','uk':'UK','ca':'Канада' if is_ru else 'Canada'}
    suf = '' if is_ru else '-en'
    san_lbl = 'Санкции' if is_ru else 'Sanctions'
    no_lbl = '—'
    for num, slug, name, role, san, yr in people:
        rows += f'<div class="person-row"><div class="person-info"><ul class="person-sanctions-list"><li><span class="person-num">{num}</span><div class="person-details"><a href="{slug}{suf}.html" class="person-name-link"><div class="person-name">{name}</div></a><div class="person-role">{role}</div></div></li>'
        for k, v in lbl.items():
            if san[k] == 'yes':
                rows += f'<li><span class="sanction-label">{v}</span><span class="sanction-yes">{san_lbl}</span><span class="sanction-date">{yr}</span></li>'
            else:
                rows += f'<li><span class="sanction-label">{v}</span><span class="sanction-no">{no_lbl}</span></li>'
        rows += '</ul></div></div>'
    s = s.replace('</div>\n      </div>\n    </div>\n  </section>', rows + '\n</div>\n      </div>\n    </div>\n  </section>', 1)
    with open(BASE + fname, 'w', encoding='utf-8') as f: f.write(s)
    print(f'✓ {fname}')

# connections.html
with open(BASE + 'connections.html', encoding='utf-8') as f: cn = f.read()
if 'nebenzya' not in cn:
    cn = cn.replace("{id:'mizulina',     label:'Мизулина',        type:'person', role:'Совет Федерации / цензура',    size:10, url:'mizulina.html'}\n  ];",
        "{id:'mizulina',     label:'Мизулина',        type:'person', role:'Совет Федерации / цензура',    size:10, url:'mizulina.html'},\n    {id:'nebenzya',     label:'Небензя',         type:'person', role:'ООН / Совет Безопасности',      size:12, url:'nebenzya.html'},\n    {id:'patrushev',    label:'Патрушев',        type:'person', role:'ФСБ / Совбез / Советник',        size:13, url:'patrushev.html'},\n    {id:'matvienko',    label:'Матвиенко',       type:'person', role:'Совет Федерации',                size:11, url:'matvienko.html'},\n    {id:'slutsky',      label:'Слуцкий',         type:'person', role:'ЛДПР / ГД МИД',                  size:10, url:'slutsky.html'},\n    {id:'emizulina',    label:'Е.Мизулина',      type:'person', role:'Лига Безопасного Интернета',     size:9,  url:'emizulina.html'}\n  ];")
    cn = cn.replace("{source:'peskov',       target:'navka',     type:'семья',    w:2}\n  ];",
        "{source:'peskov',       target:'navka',     type:'семья',    w:2},\n    {source:'nebenzya',     target:'kremlin',   type:'работа',   w:4},\n    {source:'patrushev',    target:'kremlin',   type:'работа',   w:4},\n    {source:'matvienko',    target:'kremlin',   type:'работа',   w:3},\n    {source:'slutsky',      target:'kremlin',   type:'работа',   w:2},\n    {source:'emizulina',    target:'kremlin',   type:'работа',   w:2},\n    {source:'emizulina',    target:'mizulina',  type:'семья',    w:3}\n  ];")
    with open(BASE + 'connections.html', 'w', encoding='utf-8') as f: f.write(cn)
    print('✓ connections.html')

# connections-en.html
with open(BASE + 'connections-en.html', encoding='utf-8') as f: cn = f.read()
if 'nebenzya' not in cn:
    cn = cn.replace("{id:'mizulina',     label:'Mizulina',          type:'person', role:'Federation Council / Censorship',size:10, url:'mizulina-en.html'},",
        "{id:'mizulina',     label:'Mizulina',          type:'person', role:'Federation Council / Censorship',size:10, url:'mizulina-en.html'},\n    {id:'nebenzya',     label:'Nebenzya',          type:'person', role:'UN Security Council',             size:12, url:'nebenzya-en.html'},\n    {id:'patrushev',    label:'Patrushev',         type:'person', role:'FSB / Security Council',          size:13, url:'patrushev-en.html'},\n    {id:'matvienko',    label:'Matvienko',         type:'person', role:'Federation Council Speaker',       size:11, url:'matvienko-en.html'},\n    {id:'slutsky',      label:'Slutsky',           type:'person', role:'LDPR / Duma Foreign Affairs',      size:10, url:'slutsky-en.html'},\n    {id:'emizulina',    label:'E.Mizulina',        type:'person', role:'Safe Internet League',             size:9,  url:'emizulina-en.html'},")
    cn = cn.replace("{source:'emizulina',    target:'mizulina',  type:'семья',    w:3}\n  ];", "{source:'emizulina',    target:'mizulina',  type:'семья',    w:3},\n    {source:'nebenzya',     target:'kremlin',   type:'работа',   w:4},\n    {source:'patrushev',    target:'kremlin',   type:'работа',   w:4},\n    {source:'matvienko',    target:'kremlin',   type:'работа',   w:3},\n    {source:'slutsky',      target:'kremlin',   type:'работа',   w:2}\n  ];")
    with open(BASE + 'connections-en.html', 'w', encoding='utf-8') as f: f.write(cn)
    print('✓ connections-en.html')

# sitemap.xml
with open(BASE + 'sitemap.xml', encoding='utf-8') as f: sm = f.read()
new_e = ''
for slug in ['nebenzya','patrushev','matvienko','slutsky','emizulina']:
    for sfx in ['','-en']:
        fn = slug + sfx + '.html'
        if fn not in sm:
            new_e += f'\n  <url><loc>https://cycterna2222288888-ai.github.io/cremle/{fn}</loc><lastmod>2026-04-21</lastmod><priority>0.8</priority><changefreq>monthly</changefreq></url>'
for extra in ['about.html','about-en.html','timeline.html','timeline-en.html','404.html']:
    if extra not in sm:
        new_e += f'\n  <url><loc>https://cycterna2222288888-ai.github.io/cremle/{extra}</loc><lastmod>2026-04-21</lastmod><priority>0.6</priority><changefreq>monthly</changefreq></url>'
if new_e:
    sm = sm.replace('</urlset>', new_e + '\n</urlset>')
    with open(BASE + 'sitemap.xml', 'w', encoding='utf-8') as f: f.write(sm)
    print('✓ sitemap.xml')

print('\nAll 5 new persons generated + utility pages updated.')
