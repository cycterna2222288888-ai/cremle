'use strict';
// Rebuilds index.html / index-en.html in the editorial layout.
// Content (dossier cards, facts, quotes, stats, copy) is read from the pre-redesign
// homepage in git (REF, default 2e1765f) so nothing is retyped by hand.
// Usage: node tools/build-home.js [ref]
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const { siteHeader, siteFooter, FONT_LINK } = require('./redesign.js');

const ROOT = path.join(__dirname, '..');
const REF = process.argv[2] || '2e1765f';
const original = (f) => execSync(`git show ${REF}:${f}`, { cwd: ROOT, encoding: 'utf8', maxBuffer: 1 << 26 });
const strip = (s) => s.replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();
const esc = (s) => s.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;');

function portrait(slug) {
  const f = path.join(ROOT, `${slug}.html`);
  if (!fs.existsSync(f)) return '';
  const m = fs.readFileSync(f, 'utf8').match(/class="hero-right[^"]*">\s*<img[^>]*src="([^"]+)"/);
  return m ? m[1] : '';
}

function parseCards(html) {
  const cards = [];
  const re = /<a class="card" data-channel="([^"]*)" href="([^"]+)">([\s\S]*?)<\/a>/g;
  let m;
  while ((m = re.exec(html))) {
    const body = m[3];
    const pick = (cls) => { const r = body.match(new RegExp(`class="${cls}">([\\s\\S]*?)</(?:div|span)>`)); return r ? r[1].trim() : ''; };
    const facts = [];
    body.replace(/<li><span>([\s\S]*?)<\/span><span>([\s\S]*?)<\/span><\/li>/g, (x, k, v) => { facts.push([k.trim(), v.trim()]); return x; });
    const q = body.match(/<blockquote>([\s\S]*?)<\/blockquote>/);
    const slug = m[2].replace(/(-en)?\.html$/, '');
    cards.push({
      channel: m[1], href: m[2], slug,
      num: strip(pick('card-num')).replace(/^\D+/, ''),
      name: pick('card-name'), title: pick('card-title'),
      facts, quote: q ? q[1].trim() : '', img: portrait(slug),
    });
  }
  return cards;
}

function headOf(html) {
  return html.slice(0, html.indexOf('</head>'))
    .replace(/<style[^>]*>[\s\S]*?<\/style>\s*/gi, '')
    .replace(/\n{3,}/g, '\n\n');
}

const C = {
  ru: {
    file: 'index.html', other: 'index-en.html',
    skip: 'Перейти к содержимому',
    meta: ['Документальный архив', 'Тридцать шесть персонажей · Одна система'],
    title: '<span class="l1">Голоса</span><span class="l2">Кремля</span>',
    sub: 'Досье на лица государственной пропаганды России',
    cue: 'К архиву досье',
    big: ['40', 'досье'],
    intro: [
      'Перед вами архив досье на ключевых пропагандистов российского государственного телевидения. Каждое досье составлено на основе открытых источников: биография, ключевые скандалы, цитаты о них их же коллег, руководителей, западных правительств.',
      'Разные биографии, разные таланты, разные пути к экрану и к власти. Но один результат: война, поданная как необходимость, насилие — как добродетель, ложь — как государственный язык.',
    ],
    stats: [['6', 'государств ввели санкции'], ['2014', 'первые санкции (Киселёв)'], ['100+', 'стран охвата RT'], ['8', 'разделов архива']],
    indexLabel: 'Разделы архива',
    filters: [['all', 'Все'], ['rossiya1', 'Россия-1'], ['perviy', 'Первый канал'], ['rt', 'RT'], ['ntv', 'НТВ'], ['vlast', 'Власть / Политика'], ['kultura', 'Культура'], ['ideolog', 'Идеология']],
    random: 'Случайное досье', randomTitle: 'Открыть случайное досье',
    search: 'Поиск по имени или описанию…', searchLabel: 'Поиск',
    none: 'Ничего не найдено',
    catLabel: 'Персонажи архива', catTitle: 'Досье', open: 'Открыть досье', shown: 'показано',
    band: { slug: 'kiselyov', quote: '«Новый стиль пропаганды направлен на возбуждение и мобилизацию аудитории, разжигание ненависти и страха.»', cite: 'The Economist — о Киселёве' },
    said: [
      ['«Самый энергичный кремлёвский пропагандист.»', 'Государственный департамент США — о Соловьёве'],
      ['«Она осознаёт свою циничную роль в российской пропагандистской машине вместе со своим мужем.»', 'Официальный журнал ЕС — о Скабеевой'],
    ],
    saidLabel: 'Что о них говорят',
    cta: { label: 'Источники и информация', title: '<span>Есть что</span> <span>рассказать?</span>', text: 'Если вы располагаете информацией об одном из фигурантов архива — передайте её анонимно. Мы изучим каждое сообщение.', href: 'submit.html', more: [['about.html', 'О проекте'], ['sources.html', 'Методология и источники']] },
  },
  en: {
    file: 'index-en.html', other: 'index.html',
    skip: 'Skip to content',
    meta: ['Documentary Archive · Open Sources · 2025', 'Thirty-six figures · One system'],
    title: '<span class="l1">Voices</span><span class="l0">of the</span><span class="l2">Kremlin</span>',
    sub: '',
    cue: 'To the dossiers',
    big: ['36', 'Dossiers'],
    intro: ['Different biographies, different talents, different paths to the screen and to power. But one result: war presented as necessity, violence as virtue, lies as the language of the state.'],
    stats: [['6+', 'Sanctioning jurisdictions'], ['2014', 'First sanctions'], ['0', 'Times the word "war" was used']],
    indexLabel: 'Archive sections',
    filters: [['all', 'All'], ['rossiya1', 'Russia-1'], ['perviy', 'Channel One'], ['rt', 'RT'], ['ntv', 'NTV'], ['vlast', 'Politics'], ['kultura', 'Culture'], ['ideolog', 'Ideology']],
    random: 'Random dossier', randomTitle: 'Open a random dossier',
    search: 'Search by name or description…', searchLabel: 'Search',
    none: 'No results found',
    catLabel: 'Figures in the archive', catTitle: 'Dossiers', open: 'Open dossier', shown: 'shown',
    band: { slug: 'kiselyov', quote: '«Russia is the only country capable of turning the USA into radioactive ash.»', cite: 'Kiselyov' },
    said: [
      ['«Russia does not start wars — Russia ends them.»', 'Solovyov'],
      ['«Either victory or nuclear war. There is no third option.»', 'Simonyan'],
      ['«Ukraine as a state has no geopolitical meaning.»', 'Dugin, 1997'],
      ['«This is not a war. This is a special military operation.»', 'all state channels'],
    ],
    saidLabel: 'In their own words',
    cta: { label: 'Sources &amp; Information', title: '<span>Have something</span> <span>to share?</span>', text: 'If you have information about one of the subjects in this archive — submit it anonymously. We review every submission.', href: 'submit-en.html', more: [['about-en.html', 'About'], ['sources-en.html', 'Methodology &amp; sources']] },
  },
};

// [slug, label RU, title RU, desc RU, label EN, title EN, desc EN]
const SECTIONS = [
  ['connections', 'Аналитика', 'Связи', 'Кто с кем работает, семейные и деловые связи между персонажами', 'Analysis', 'Connections', 'Who works with whom: family and business ties between the figures'],
  ['timeline', 'Хронология', 'Таймлайн', 'Ключевые события 1954–2024: назначения, скандалы, санкции, цитаты', 'Chronology', 'Timeline', 'Key events 1954–2024: appointments, scandals, sanctions, quotes'],
  ['tv-propaganda', 'Аналитика', 'Механизмы', 'Как телевизор залез в мозг вашим родителям (М. Кац*)', 'Analysis', 'Mechanisms', 'How television got inside your parents’ heads (M. Katz*)'],
  ['sanctions', 'Досье', 'Санкции', 'Кто под какими санкциями, с датами и официальными обоснованиями', 'Dossier', 'Sanctions', 'Who is under which sanctions, with dates and official grounds'],
  ['glossary', 'Медиаграмотность', 'Словарь', 'Эвфемизмы пропаганды: что говорят и что это означает на деле', 'Media literacy', 'Glossary', 'Propaganda euphemisms: what is said and what it actually means'],
  ['assets', 'OSINT', 'Финансовый след', 'База недвижимости, активов и арестованных вилл пропагандистов', 'OSINT', 'Assets', 'Real estate, assets and seized villas of propagandists'],
  ['quotes', 'Цитатник', 'Говорят сами', 'Дословные цитаты о войне, Западе, ядерных угрозах и лицемерии', 'Quote book', 'Quotes', 'Verbatim quotes on war, the West, nuclear threats and hypocrisy'],
  ['media-empire', 'Структура', 'Медиаимперия', 'Кто чем управляет, откуда деньги, сколько людей смотрят', 'Structure', 'Media Empire', 'Who runs what, where the money comes from, how many people watch'],
  ['sources', 'Методология', 'Источники', 'Принципы работы, библиография и верификация всех фактов', 'Methodology', 'Sources', 'Working principles, bibliography and verification of every fact'],
  ['about', 'Проект', 'О проекте', 'Зачем создан архив, кому предназначен и как устроен', 'Project', 'About', 'Why the archive exists, who it is for and how it works'],
  ['compare', 'Инструмент', 'Сравнение', 'Выберите двух персонажей и сравните досье бок о бок', 'Tool', 'Compare', 'Pick two figures and compare their dossiers side by side'],
];

function build(lang) {
  const c = C[lang];
  const src = original(c.file);
  const cards = parseCards(src);
  const head = headOf(src).replace(/<title>/, '<title>');
  const footInner = (src.match(/<div class="footer">([\s\S]*?)\n<\/div>/) || ['', ''])[1].trim();
  const en = lang === 'en';
  const pad = (n) => String(n).padStart(2, '0');

  const strip = cards.slice(0, 6).map((k, i) => `
      <a class="strip-item" href="${k.href}" style="--i:${i}">
        <img src="${k.img}" alt="${esc(strip0(k.name))}"${i > 2 ? ' loading="lazy"' : ''}>
        <span class="strip-cap"><b>${pad(k.num)}</b>${strip0(k.name)}</span>
      </a>`).join('');

  const index = SECTIONS.map((s, i) => `
      <li><a href="${en ? s[0] + '-en' : s[0]}.html">
        <span class="ix-num">${pad(i + 1)}</span>
        <span class="ix-title">${en ? s[5] : s[2]}</span>
        <span class="ix-label">${en ? s[4] : s[1]}</span>
        <span class="ix-desc">${en ? s[6] : s[3]}</span>
        <span class="ix-arrow" aria-hidden="true">↗</span>
      </a></li>`).join('');

  const rows = cards.map((k) => `
    <a class="card entry" data-channel="${k.channel}" href="${k.href}" data-img="${k.img}">
      <span class="e-num">${pad(k.num)}</span>
      <span class="e-ph" aria-hidden="true"><img src="${k.img}" alt="" loading="lazy"></span>
      <span class="e-head"><span class="card-name">${k.name}</span><span class="card-title">${k.title}</span></span>
      <span class="e-facts">${k.facts.map(([a, b]) => `<span class="e-fact"><span class="e-k">${a}</span><span class="e-v">${b}</span></span>`).join('')}</span>
      ${k.quote ? `<span class="e-quote">${k.quote}</span>` : ''}
      <span class="e-open">${c.open} <span aria-hidden="true">↗</span></span>
    </a>`).join('');

  const said = c.said.map((q, i) => `
    <blockquote class="said-q said-${i + 1}" data-rv>
      <p>${q[0]}</p>
      <cite>— ${q[1]}</cite>
    </blockquote>`).join('');

  const header = siteHeader(c.file, lang, 'home');
  const footer = siteFooter(lang, footInner);
  const bandImg = portrait(c.band.slug);

  return `${head}${FONT_LINK}
<link rel="stylesheet" href="css/kv.css">
<link rel="stylesheet" href="css/home.css">
<script>try{document.documentElement.dataset.theme=localStorage.getItem('theme')||'dark'}catch(e){}</script>
<script src="js/kv.js" defer></script>
</head>

<body class="page-home">
<a class="skip-link" href="#main-content">${c.skip}</a>
${header}

<main id="main-content">

<!-- A · masthead: headline left, portrait strip right, metadata on its own line -->
<section class="h-hero">
  <div class="h-meta label"><span class="dot"></span>${c.meta[0]}<br><span class="muted">${c.meta[1]}</span></div>
  <h1 class="h-title">${c.title}</h1>
  ${c.sub ? `<p class="h-sub">${c.sub}</p>` : ''}
  <a class="h-cue label" href="#catalogue"><span class="h-cue-n">${c.big[0]}</span> ${c.cue} <span aria-hidden="true">↓</span></a>
  <div class="h-strip">${strip}
  </div>
</section>

<!-- B · one big number + a narrow column -->
<section class="h-count">
  <div class="hc-big rv-line" aria-label="${c.big[0]} ${c.big[1]}"><span>${c.big[0]}</span><small class="label">${c.big[1]}</small></div>
  <div class="hc-text">
    ${c.intro.map((p, i) => `<p class="${i === 0 ? 'hc-lead' : ''}" data-rv>${p}</p>`).join('\n    ')}
  </div>
  <dl class="hc-stats">
    ${c.stats.map((s) => `<div data-rv><dt>${s[0]}</dt><dd>${s[1]}</dd></div>`).join('\n    ')}
  </dl>
</section>

<!-- C · dense index of the archive -->
<section class="h-index">
  <h2 class="label label--accent">${c.indexLabel}</h2>
  <ol class="ix">${index}
  </ol>
</section>

<!-- the catalogue -->
<section class="h-cat" id="catalogue">
  <div class="cat-head">
    <h2 class="cat-title">${c.catTitle}<sup>${cards.length}</sup></h2>
    <p class="label">${c.catLabel} · <span id="cat-count">${cards.length}</span> ${c.shown}</p>
  </div>
  <div class="filter-bar">
    <div class="flt">${c.filters.map((f, i) => `<button type="button" class="flt-btn${i === 0 ? ' active' : ''}" data-filter="${f[0]}">${f[1]}</button>`).join('')}</div>
    <label class="search-wrap"><span class="label">${c.searchLabel}</span><input type="search" id="search-input" placeholder="${c.search}" autocomplete="off"></label>
    <button type="button" class="rnd" id="btn-random" title="${c.randomTitle}">${c.random} <span aria-hidden="true">⇄</span></button>
  </div>
  <div class="entries">${rows}
  </div>
  <div class="no-results" id="no-results">${c.none}</div>
</section>

<!-- D · full-bleed photograph with a caption -->
<figure class="h-band">
  <div class="hb-img"><img src="${bandImg}" alt="" loading="lazy" data-parallax="0.12"></div>
  <figcaption>
    <blockquote>${c.band.quote}</blockquote>
    <cite class="label">— ${c.band.cite}</cite>
  </figcaption>
</figure>

<!-- E · text only -->
<section class="h-said">
  <h2 class="label">${c.saidLabel}</h2>${said}
</section>

<!-- F · closing call -->
<section class="h-cta">
  <p class="label label--accent">${c.cta.label}</p>
  <a class="cta-link" href="${c.cta.href}"><span class="cta-t">${c.cta.title}</span><span class="cta-arrow" aria-hidden="true">→</span></a>
  <p class="cta-text">${c.cta.text}</p>
  <p class="cta-more">${c.cta.more.map((m) => `<a class="u-link" href="${m[0]}">${m[1]}</a>`).join('')}</p>
</section>

</main>
${footer}

<div class="hover-preview" id="hover-preview" aria-hidden="true"><img alt=""></div>

<script>
(function(){
  var cards = Array.prototype.slice.call(document.querySelectorAll('.entry'));
  var input = document.getElementById('search-input');
  var none = document.getElementById('no-results');
  var count = document.getElementById('cat-count');
  var activeFilter = 'all';
  var searchIndex = null;
  fetch('data/search-index.json').then(function(r){ return r.json(); }).then(function(d){ searchIndex = d; }).catch(function(){});

  function matchingFiles(q) {
    if (!searchIndex || !q) return null;
    var out = new Set();
    searchIndex.forEach(function(e){
      if ((e.name && e.name.toLowerCase().includes(q)) ||
          (e.bio && e.bio.toLowerCase().includes(q)) ||
          (e.tags && e.tags.some(function(t){ return t.toLowerCase().includes(q); })) ||
          (e.quotes && e.quotes.some(function(t){ return t.toLowerCase().includes(q); }))) out.add(e.file);
    });
    return out;
  }
  function apply() {
    var q = input.value.toLowerCase().trim();
    var files = q.length >= 2 ? matchingFiles(q) : null;
    var visible = 0;
    cards.forEach(function(c){
      var text = c.querySelector('.e-head').textContent.toLowerCase();
      var okCh = activeFilter === 'all' || c.dataset.channel === activeFilter;
      var okQ = !q || text.includes(q) || (files && files.has(c.getAttribute('href')));
      var show = okCh && okQ;
      c.hidden = !show;
      if (show) visible++;
    });
    none.style.display = visible ? 'none' : 'block';
    count.textContent = visible;
  }
  document.querySelectorAll('.flt-btn').forEach(function(b){
    b.addEventListener('click', function(){
      document.querySelectorAll('.flt-btn').forEach(function(x){ x.classList.remove('active'); x.setAttribute('aria-pressed','false'); });
      b.classList.add('active'); b.setAttribute('aria-pressed','true');
      activeFilter = b.dataset.filter;
      apply();
    });
  });
  input.addEventListener('input', apply);
  var q0 = new URLSearchParams(location.search).get('q');
  if (q0) { input.value = q0; apply(); }
  document.getElementById('btn-random').addEventListener('click', function(){
    var pool = cards.filter(function(c){ return !c.hidden; });
    if (!pool.length) pool = cards;
    location.href = pool[Math.floor(Math.random() * pool.length)].getAttribute('href');
  });
})();
</script>
</body>
</html>
`;
}
function strip0(s) { return s.replace(/<br\s*\/?>/g, ' ').replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim(); }

for (const lang of ['ru', 'en']) {
  fs.writeFileSync(path.join(ROOT, C[lang].file), build(lang));
  console.log('wrote', C[lang].file);
}
