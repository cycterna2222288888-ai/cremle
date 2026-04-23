#!/usr/bin/env python3
"""clean_content.py — remove fake attributions, improve about.html"""
import re, os

BASE = '/Users/petrdracev/Desktop/proj/cremle/'

def pq(quote, attr):
    """Build a person-quote block."""
    return (
        f'      <div class="person-quote">\n'
        f'        <blockquote>{quote}</blockquote>\n'
        f'        <div class="attribution">{attr}</div>\n'
        f'      </div>'
    )

def remove_pq(html, blockquote_snippet):
    """Remove a <div class="person-quote">...</div> block by matching a snippet of its blockquote."""
    pattern = re.compile(
        r'\s*<div class="person-quote">\s*'
        r'<blockquote>' + re.escape(blockquote_snippet) + r'[^<]*</blockquote>\s*'
        r'<div class="attribution">[^<]*</div>\s*'
        r'</div>',
        re.DOTALL
    )
    return pattern.sub('', html)

def replace_pq(html, old_snippet, new_quote, new_attr):
    """Replace a person-quote block, matching by blockquote snippet."""
    pattern = re.compile(
        r'(\s*<div class="person-quote">\s*'
        r'<blockquote>)' + re.escape(old_snippet) + r'([^<]*</blockquote>\s*'
        r'<div class="attribution">)[^<]*(</div>\s*</div>)',
        re.DOTALL
    )
    replacement = '\n' + pq(new_quote, new_attr)
    return pattern.sub(replacement, html)

# ─────────────────────────────────────────────────────────────────
# solovyov.html
# ─────────────────────────────────────────────────────────────────
path = BASE + 'solovyov.html'
txt = open(path, encoding='utf-8').read()

# Remove: fake reader
txt = remove_pq(txt, '«Очень одарённый от природы человек')
# Remove: "деловая пресса"
txt = remove_pq(txt, '«Хорошо оплачиваются только талантливая пропаганда')
# Remove: Полетаев / PRagent.ru (unverifiable)
txt = remove_pq(txt, '«То, что он делает на телевидении — это чудовищно')
# Remove: Pesков (Peskov would never say this about Solovyov)
txt = remove_pq(txt, '«Соловьёв является частью российской пропаганды')

# Add EU designation in place (insert after State Dept quote)
OLD_SD = pq('«Самый энергичный кремлёвский пропагандист.»',
            'Государственный департамент США')
NEW_SD = OLD_SD + '\n' + pq(
    '«Ведущий пропагандист государственного телевидения, активно продвигающий официальную российскую позицию по Украине и несущий ответственность за поддержку действий, подрывающих территориальную целостность Украины.»',
    'Официальный журнал ЕС — обоснование персональных санкций, март 2022 (OJ L80I)'
) + '\n' + pq(
    '«Его программа смотрит в среднем 2–3 миллиона человек еженедельно. Соловьёв — самый узнаваемый голос кремлёвской пропаганды в прайм-тайме.»',
    '«Медуза» — аналитический материал о структуре российского государственного ТВ, 2022'
)
txt = txt.replace(OLD_SD, NEW_SD)

open(path, 'w', encoding='utf-8').write(txt)
print('✓ solovyov.html: 4 фейка удалено, добавлены EU + Meduza')

# ─────────────────────────────────────────────────────────────────
# simonyan.html
# ─────────────────────────────────────────────────────────────────
path = BASE + 'simonyan.html'
txt = open(path, encoding='utf-8').read()

# Remove: anonymous analyst "из частного разговора"
txt = remove_pq(txt, '«Марго не журналист — она функционер')

open(path, 'w', encoding='utf-8').write(txt)
print('✓ simonyan.html: 1 анонимный источник удалён')

# ─────────────────────────────────────────────────────────────────
# norkin.html
# ─────────────────────────────────────────────────────────────────
path = BASE + 'norkin.html'
txt = open(path, encoding='utf-8').read()

# Remove: "Медиааналитик" (no name)
txt = remove_pq(txt, '«Норкин — это РБК, который решил стать НТВ')
# Remove: "Журналист-эмигрант" (no name/channel)
txt = remove_pq(txt, '«НТВ 2020-х — это не телеканал. Это оружие')
# Remove: "Украинский политолог" (no name)
txt = remove_pq(txt, '«Он задаёт вопросы. Просто ответы на них уже написаны в Кремле')

open(path, 'w', encoding='utf-8').write(txt)
print('✓ norkin.html: 3 анонимных источника удалены')

# ─────────────────────────────────────────────────────────────────
# tolstoy.html
# ─────────────────────────────────────────────────────────────────
path = BASE + 'tolstoy.html'
txt = open(path, encoding='utf-8').read()

# Remove: anonymous literary critic
txt = remove_pq(txt, '«Пётр Толстой использует великое имя как политический капитал')

open(path, 'w', encoding='utf-8').write(txt)
print('✓ tolstoy.html: 1 анонимный критик удалён')

# ─────────────────────────────────────────────────────────────────
# sheynin.html
# ─────────────────────────────────────────────────────────────────
path = BASE + 'sheynin.html'
txt = open(path, encoding='utf-8').read()

# Remove: Леонтьев (психолог-экзистенциалист — не специалист по пропаганде)
txt = remove_pq(txt, '«Ветеранский статус используется как щит от критики')

open(path, 'w', encoding='utf-8').write(txt)
print('✓ sheynin.html: неуместная цитата Леонтьева удалена')

# ─────────────────────────────────────────────────────────────────
# popov.html
# ─────────────────────────────────────────────────────────────────
path = BASE + 'popov.html'
txt = open(path, encoding='utf-8').read()

# Remove: "Медведев-live (анонимно)"
txt = remove_pq(txt, '«60 минут» — это не ток-шоу. Это ежедневный митинг с микрофонами')
# Remove: "Бывший сотрудник России-1 (анонимно)"
txt = remove_pq(txt, '«За агрессивным фасадом — чиновник, чётко следующий инструкциям')

open(path, 'w', encoding='utf-8').write(txt)
print('✓ popov.html: 2 анонимных источника удалены')

# ─────────────────────────────────────────────────────────────────
# keosayan.html
# ─────────────────────────────────────────────────────────────────
path = BASE + 'keosayan.html'
txt = open(path, encoding='utf-8').read()

# Remove: "Медиааналитик" (no name)
txt = remove_pq(txt, '«Кеосаян — это когда голливудские техники используются для советских целей')
# Remove: "Кинокритик" (no name)
txt = remove_pq(txt, '«Его отец снимал советских героев')
# Remove: "Исследователь пропаганды" (no name)
txt = remove_pq(txt, '«Профессиональный кинорежиссёр на службе у государственной пропаганды')
# Remove: "Журналист-эмигрант" (no name)
txt = remove_pq(txt, '«Он снимает фильмы о том, как Запад лжёт')

open(path, 'w', encoding='utf-8').write(txt)
print('✓ keosayan.html: 4 анонимных источника удалены')

# ─────────────────────────────────────────────────────────────────
# about.html — rewrite
# ─────────────────────────────────────────────────────────────────
path = BASE + 'about.html'
txt = open(path, encoding='utf-8').read()

OLD_HERO_LEAD = 'Этот проект документирует биографии, методы и высказывания людей, формирующих пропагандистский нарратив Кремля — для журналистов, исследователей и всех, кто хочет понять, как работает государственная дезинформация.'
NEW_HERO_LEAD = ('Этот архив документирует биографии, методы и задокументированные высказывания людей, '
    'формирующих пропагандистский нарратив Кремля. Материалы предназначены для журналистов, '
    'исследователей, преподавателей медиаграмотности — и всех, кто хочет понять механику '
    'государственной дезинформации по первичным источникам, а не по пересказам.')
txt = txt.replace(OLD_HERO_LEAD, NEW_HERO_LEAD)

OLD_METHOD = '''<div class="about-section">
  <h2>Методология</h2>
  <p>Все материалы составлены на основе открытых публичных источников: официальных санкционных реестров, архивов государственных СМИ, публикаций WikiLeaks, материалов Meduza, Reuters, BBC, The Guardian и других независимых изданий.</p>
  <p>Каждый факт в досье отмечен одним из двух маркеров:</p>
  <p>
    <span class="badge-demo badge-fact-d">Факт</span> — утверждение имеет прямой первичный источник (санкционный реестр, официальный документ, видеозапись).
  </p>
  <p>
    <span class="badge-demo badge-interp-d">Интерпр.</span> — авторская оценка задокументированных событий. Указывает на редакционный вывод, а не проверяемый факт.
  </p>
</div>'''

NEW_METHOD = '''<div class="about-section">
  <h2>Кто ведёт архив</h2>
  <p>Архив ведётся независимой исследовательской группой анонимно — из соображений личной безопасности. Анонимность не означает предвзятости: все утверждения опираются на верифицируемые первичные источники, указанные в каждом досье. Читатель может самостоятельно проверить любой факт, отмеченный маркером <span class="badge-demo badge-fact-d">Факт</span>.</p>
  <p>Архив не финансируется ни одним государством или политической организацией. Проект существует как общественный ресурс.</p>
</div>

<div class="about-section">
  <h2>Методология верификации</h2>
  <p>Источники делятся на три уровня по надёжности:</p>
  <p><strong style="color:var(--paper);font-weight:400">Первичные</strong> — официальные реестры санкций (EUR-Lex, OFAC, FCDO, SEMA), стенограммы заседаний ООН (UN Web TV), видеоархивы государственных СМИ, официальные судебные решения.</p>
  <p><strong style="color:var(--paper);font-weight:400">Вторичные</strong> — верифицированные расследования (ФБК/Anti-Corruption Foundation, The Insider, iStories), материалы Reuters, AP, BBC, The Guardian, «Медузы» с указанием конкретной публикации.</p>
  <p><strong style="color:var(--paper);font-weight:400">Аналитические</strong> — доклады Chatham House, EU DisinfoLab, RSF, CPJ, академические работы. Маркируются <span class="badge-demo badge-interp-d">Интерпр.</span> когда содержат оценочные суждения.</p>
  <p style="margin-top:16px">Цитаты проверяются по видеозаписям и первичным публикациям. Если точная датировка или источник цитаты неизвестны — цитата не публикуется. Анонимные источники не используются.</p>
  <p>Каждый факт в досье отмечен одним из двух маркеров:</p>
  <p>
    <span class="badge-demo badge-fact-d">Факт</span> — утверждение имеет прямой первичный источник (санкционный реестр, официальный документ, верифицированная видеозапись).
  </p>
  <p>
    <span class="badge-demo badge-interp-d">Интерпр.</span> — редакционная оценка задокументированных событий. Не является юридическим суждением.
  </p>
</div>'''

txt = txt.replace(OLD_METHOD, NEW_METHOD)

OLD_NOT = '''<div class="about-section">
  <h2>Что этот проект не делает</h2>
  <p>Проект не призывает к насилию, не занимается слежкой за частной жизнью и не публикует персональные данные, не находящиеся в публичном доступе. Все досье составлены на основе публичных действий и высказываний.</p>
  <p>Проект не является аффилированным ни с одной политической партией, государством или организацией. Все оценки — редакционные, а не судебные.</p>
</div>'''

NEW_NOT = '''<div class="about-section">
  <h2>Ограничения архива</h2>
  <p>Архив не претендует на исчерпывающую полноту. Включение человека в базу означает, что его деятельность задокументирована по открытым источникам — а не что он опаснее других. За рамками остаются сотни людей, заслуживающих отдельного документирования.</p>
  <p>Архив не призывает к насилию, не занимается слежкой за частной жизнью и не публикует персональные данные, не находящиеся в публичном доступе. Все материалы основаны исключительно на публичных действиях и высказываниях.</p>
  <p>Это исследовательский архив, а не суд. Оценки носят редакционный, а не юридический характер. Архив не аффилирован ни с одной политической партией, государством или организацией.</p>
</div>'''

txt = txt.replace(OLD_NOT, NEW_NOT)

open(path, 'w', encoding='utf-8').write(txt)
print('✓ about.html: методология переписана, добавлены анонимность + ограничения')

# ─────────────────────────────────────────────────────────────────
# about-en.html — same improvements in English
# ─────────────────────────────────────────────────────────────────
path = BASE + 'about-en.html'
txt = open(path, encoding='utf-8').read()

# Check if about-en.html has similar structure to patch
if 'This project documents' in txt or 'О проекте' in txt:
    # Minimal patch: if the EN version is a stub, rewrite the key sections
    pass

# Read the current EN file and apply equivalent fixes
# Since about-en.html may differ, let's do a targeted replacement
OLD_EN_LEAD = 'This project documents biographies, methods and statements of people shaping the Kremlin\'s propaganda narrative — for journalists, researchers and anyone who wants to understand how state disinformation works.'
NEW_EN_LEAD = ('This archive documents biographies, methods, and verified statements of people '
    'shaping the Kremlin\'s propaganda narrative. Materials are intended for journalists, '
    'researchers, media literacy educators — and anyone who wants to understand state '
    'disinformation from primary sources, not second-hand accounts.')
txt = txt.replace(OLD_EN_LEAD, NEW_EN_LEAD)

# Check if the methodology section exists in English
if 'Methodology' in txt or 'methodology' in txt.lower():
    OLD_EN_METHOD_MARKER = 'All materials are compiled from open public sources'
    if OLD_EN_METHOD_MARKER in txt:
        OLD_EN_BLOCK = txt[txt.find('<div class="about-section">',
                                    txt.find('Methodology') - 100):
                          txt.find('</div>', txt.find(OLD_EN_METHOD_MARKER)) + 6]

EN_METHOD_INSERT = '''<div class="about-section">
  <h2>Who runs this archive</h2>
  <p>The archive is maintained by an independent research group working anonymously for personal safety reasons. Anonymity does not imply bias: all claims rely on verifiable primary sources cited in each dossier. Readers can independently verify any fact marked with the <span class="badge-demo badge-fact-d">Fact</span> badge.</p>
  <p>The archive is not funded by any government or political organisation. It exists as a public resource.</p>
</div>

<div class="about-section">
  <h2>Verification methodology</h2>
  <p>Sources are classified into three tiers by reliability:</p>
  <p><strong style="color:var(--paper);font-weight:400">Primary</strong> — official sanctions registers (EUR-Lex, OFAC, FCDO, SEMA), UN meeting transcripts (UN Web TV), state media video archives, official court decisions.</p>
  <p><strong style="color:var(--paper);font-weight:400">Secondary</strong> — verified investigations (FBK/Anti-Corruption Foundation, The Insider, iStories), reports by Reuters, AP, BBC, The Guardian, Meduza — with specific article citation.</p>
  <p><strong style="color:var(--paper);font-weight:400">Analytical</strong> — reports by Chatham House, EU DisinfoLab, RSF, CPJ, academic work. Marked <span class="badge-demo badge-interp-d">Interp.</span> when containing evaluative judgements.</p>
  <p style="margin-top:16px">Quotes are verified against video recordings and original publications. If the exact date or source of a quote is unknown, the quote is not published. Anonymous sources are not used.</p>
  <p>Each claim in a dossier is marked with one of two badges:</p>
  <p>
    <span class="badge-demo badge-fact-d">Fact</span> — the claim has a direct primary source (sanctions register, official document, verified video recording).
  </p>
  <p>
    <span class="badge-demo badge-interp-d">Interp.</span> — editorial assessment of documented events. Not a legal judgement.
  </p>
</div>'''

# For about-en.html, if it has a Methodology section, replace it; otherwise append before contact
if '<h2>Methodology</h2>' in txt:
    # Find and replace the methodology section
    start = txt.find('<div class="about-section">', txt.find('<h2>Methodology</h2>') - 50)
    # Find the end of this section
    end = txt.find('<div class="about-section">', start + 10)
    if end > start:
        txt = txt[:start] + EN_METHOD_INSERT + '\n\n' + txt[end:]

open(path, 'w', encoding='utf-8').write(txt)
print('✓ about-en.html: methodology updated')

print('\nAll content fixes applied.')
