'use strict';
// One-off migration: moves every page onto the shared design system in css/ + js/.
// - strips legacy inline <style> blocks and the per-page theme-init scripts
// - replaces .topbar/.section-nav with the shared site header + index sheet
// - replaces .footer with the shared site footer (original footer text kept as colophon)
// - rebuilds the dossier hero portrait (removes decorative SVG overlay)
// - maps hard-coded legacy colours/fonts in inline style attributes onto tokens
// Usage: node tools/redesign.js [files...]   (defaults to every *.html except index pages)
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const exists = (f) => fs.existsSync(path.join(ROOT, f));

const SECTIONS = [
  ['quotes', 'Цитатник', 'Quotes'],
  ['sanctions', 'Санкции', 'Sanctions'],
  ['timeline', 'Хронология', 'Timeline'],
  ['connections', 'Связи', 'Connections'],
  ['compare', 'Сравнить', 'Compare'],
  ['tv-propaganda', 'Пропаганда', 'Propaganda'],
  ['media-empire', 'Медиаимперия', 'Media Empire'],
  ['assets', 'Владения', 'Assets'],
  ['glossary', 'Глоссарий', 'Glossary'],
  ['sources', 'Источники', 'Sources'],
  ['about', 'О проекте', 'About'],
];
const HEAD_NAV = ['quotes', 'sanctions', 'timeline', 'connections'];

const T = {
  ru: {
    brand: 'Голоса <i>Кремля</i>', brandSub: 'Документальный архив', word: 'Голоса <i>Кремля</i>',
    archive: 'Досье', index: 'Указатель', close: 'Закрыть', tip: 'Сообщить', home: 'Главная',
    navLabel: 'Разделы архива', rss: 'RSS', note: 'Все материалы составлены на основе открытых источников. Факты верифицированы публикациями СМИ.',
    noteLabel: 'Независимый архив',
  },
  en: {
    brand: 'Kremlin <i>Voices</i>', brandSub: 'Documentary archive', word: 'Kremlin <i>Voices</i>',
    archive: 'Dossiers', index: 'Index', close: 'Close', tip: 'Submit a tip', home: 'Home',
    navLabel: 'Archive sections', rss: 'RSS', note: 'Compiled from open sources. All facts verified by published media reports.',
    noteLabel: 'Independent archive',
  },
};

const href = (slug, lang) => (lang === 'en' ? `${slug}-en.html` : `${slug}.html`);

function counterpart(file, lang) {
  const base = file.replace(/\.html$/, '');
  if (lang === 'en') {
    const ru = base.replace(/-en$/, '') + '.html';
    return exists(ru) ? ru : 'index.html';
  }
  const en = base + '-en.html';
  return exists(en) ? en : 'index-en.html';
}

function siteHeader(file, lang, current) {
  const t = T[lang];
  const home = lang === 'en' ? 'index-en.html' : 'index.html';
  const other = counterpart(file, lang);
  const ruHref = lang === 'ru' ? file : other;
  const enHref = lang === 'en' ? file : other;
  const nav = [`<a href="${home}#catalogue"${current === 'dossier' ? ' class="is-on"' : ''}>${t.archive}</a>`]
    .concat(HEAD_NAV.map((s) => {
      const sec = SECTIONS.find((x) => x[0] === s);
      return `<a href="${href(s, lang)}"${current === s ? ' class="is-on"' : ''}>${lang === 'en' ? sec[2] : sec[1]}</a>`;
    }));
  const sheet = [`<li><a href="${home}"${current === 'home' ? ' class="is-on"' : ''}><span>00</span>${t.home}</a></li>`]
    .concat(SECTIONS.map((sec, i) => `<li><a href="${href(sec[0], lang)}"${current === sec[0] ? ' class="is-on"' : ''}><span>${String(i + 1).padStart(2, '0')}</span>${lang === 'en' ? sec[2] : sec[1]}</a></li>`));
  const submit = href('submit', lang);
  return `<header class="site-head">
  <a class="brand" href="${home}"><span class="brand-mark">${t.brand}</span><span class="brand-sub">${t.brandSub}</span></a>
  <nav class="site-nav" aria-label="${t.navLabel}">${nav.join('')}<button type="button" class="menu-link" data-menu-open aria-controls="menu" aria-expanded="false">${t.index} +</button></nav>
  <div class="site-tools">
    <a class="tip-link" href="${submit}">${t.tip}</a>
    <div class="lang"><a href="${ruHref}" hreflang="ru"${lang === 'ru' ? ' class="is-on" aria-current="true"' : ''}>RU</a><a href="${enHref}" hreflang="en"${lang === 'en' ? ' class="is-on" aria-current="true"' : ''}>EN</a></div>
    <button type="button" id="theme-toggle"></button>
    <button type="button" class="menu-btn" data-menu-open aria-controls="menu" aria-expanded="false">${t.index}<span class="bars"></span></button>
  </div>
</header>
<div class="menu-sheet" id="menu" role="dialog" aria-modal="true" aria-label="${t.navLabel}">
  <div class="ms-top"><span class="brand-mark">${t.brand}</span><button type="button" class="ms-close" data-menu-close>${t.close} ✕</button></div>
  <ol>${sheet.join('')}</ol>
  <div class="ms-foot label"><a href="${home}#catalogue">${t.archive} →</a><a href="${submit}">${t.tip} →</a><span><a href="${ruHref}">RU</a> / <a href="${enHref}">EN</a></span></div>
</div>`;
}

function siteFooter(lang, colophon) {
  const t = T[lang];
  const links = SECTIONS.map((sec) => `<li><a href="${href(sec[0], lang)}">${lang === 'en' ? sec[2] : sec[1]}</a></li>`).join('');
  return `<footer class="site-foot">
  <div class="sf-grid">
    <p class="sf-note"><span class="label">${t.noteLabel}</span>${t.note}</p>
    <ul class="sf-links">${links}</ul>
    <div class="sf-meta"><a href="${href('submit', lang)}">${t.tip}</a><a href="${lang === 'en' ? 'rss-en.xml' : 'rss.xml'}">${t.rss}</a><a href="${lang === 'en' ? 'index.html' : 'index-en.html'}">${lang === 'en' ? 'Русская версия' : 'English version'}</a></div>
  </div>
  <div class="sf-colophon">${colophon}</div>
  <span class="sf-word" aria-hidden="true">${t.word}</span>
</footer>`;
}

// find the element that starts at `start` (an opening <div|nav ...>) and return its end index
function matchEnd(html, start, tag) {
  const re = new RegExp(`<${tag}\\b|</${tag}>`, 'gi');
  re.lastIndex = start;
  let depth = 0, m;
  while ((m = re.exec(html))) {
    if (m[0][1] === '/') { depth--; if (depth === 0) return re.lastIndex; }
    else depth++;
  }
  return -1;
}
function cutElement(html, openRe, tag) {
  const m = openRe.exec(html);
  if (!m) return null;
  const end = matchEnd(html, m.index, tag);
  if (end < 0) return null;
  return { start: m.index, end, outer: html.slice(m.index, end) };
}
const inner = (outer) => outer.replace(/^<[^>]+>/, '').replace(/<\/\w+>$/, '');

const STYLE_MAP = [
  [/font-family:\s*\\?'Playfair Display\\?',\s*serif/g, 'font-family:var(--serif)'],
  [/font-family:\s*\\?'Inter\\?',\s*sans-serif/g, 'font-family:var(--sans)'],
  [/#8b1a1a|#c0392b|#8b5c1a/gi, 'var(--accent)'],
  [/#ede8dc/gi, 'var(--fg)'],
  [/#888\b|#999\b|#777\b|#4a4540/gi, 'var(--fg-2)'],
  [/#555\b|#666\b|#444\b|#333\b/gi, 'var(--fg-3)'],
  [/#0d0d0d|#060606|#0e0e0e|#111\b|#141414/gi, 'var(--bg-2)'],
  [/#1a1a1a|#222\b/gi, 'var(--rule)'],
  [/border-radius:\s*[^;"]+;?/gi, ''],
];
function mapInlineStyles(html) {
  return html.replace(/style="([^"]*)"/g, (all, css) => {
    let out = css;
    for (const [re, rep] of STYLE_MAP) out = out.replace(re, rep);
    return `style="${out}"`;
  });
}

const FONT_LINK = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:ital,wght@0,400;0,500;1,400&display=swap">';

function transform(file) {
  let html = fs.readFileSync(path.join(ROOT, file), 'utf8');
  if (html.includes('css/kv.css')) return false; // already migrated
  const lang = /<html[^>]*lang="en"/.test(html) ? 'en' : 'ru';
  const isDossier = html.includes('class="hero-left"');
  const base = file.replace(/\.html$/, '').replace(/-en$/, '');
  const current = isDossier ? 'dossier' : base;

  // 1. styles out, shared system in
  html = html.replace(/<style[^>]*>[\s\S]*?<\/style>\s*/gi, '');
  const sheets = [`<link rel="stylesheet" href="css/kv.css">`];
  sheets.push(isDossier ? '<link rel="stylesheet" href="css/dossier.css">' : '<link rel="stylesheet" href="css/pages.css">');
  html = html.replace('</head>', `${FONT_LINK}\n${sheets.join('\n')}\n<script>try{document.documentElement.dataset.theme=localStorage.getItem('theme')||'dark'}catch(e){}</script>\n<script src="js/kv.js" defer></script>\n</head>`);

  // 2. legacy theme-init scripts
  html = html.replace(/<script>\s*\(function\(\)\{\s*var t=localStorage\.getItem\('theme'\)\|\|'dark';[\s\S]*?<\/script>\s*/g, '');

  // 3. body class
  html = html.replace(/<body([^>]*)>/, (m, attrs) => {
    const cls = isDossier ? 'page-dossier' : `page-${base}`;
    if (/class="/.test(attrs)) return `<body${attrs.replace(/class="/, `class="${cls} `)}>`;
    return `<body class="${cls}"${attrs}>`;
  });

  // 4. header
  let nav;
  while ((nav = cutElement(html, /<nav class="section-nav"[^>]*>/, 'nav'))) {
    html = html.slice(0, nav.start) + html.slice(nav.end);
  }
  const topTag = /<nav class="topbar"/.test(html) ? 'nav' : 'div';
  const top = cutElement(html, new RegExp(`<${topTag} class="topbar"[^>]*>`), topTag);
  const header = siteHeader(file, lang, current);
  if (top) html = html.slice(0, top.start) + header + html.slice(top.end);
  else html = html.replace(/(<body[^>]*>\s*(?:<a class="skip-link"[^>]*>[^<]*<\/a>\s*)?)/, `$1\n${header}\n`);

  // 5. footer
  const footTag = /<footer class="footer"/.test(html) ? 'footer' : 'div';
  const foot = cutElement(html, new RegExp(`<${footTag} class="footer"[^>]*>`), footTag);
  if (foot) {
    html = html.slice(0, foot.start) + siteFooter(lang, inner(foot.outer).trim()) + html.slice(foot.end);
  } else if (html.includes('</main>')) {
    html = html.replace('</main>', `${siteFooter(lang, '')}\n</main>`);
  } else {
    const anchor = html.search(/<button class="back-to-top"|<script>\s*window\.addEventListener\('scroll'|<\/body>/);
    html = html.slice(0, anchor) + siteFooter(lang, '') + '\n' + html.slice(anchor);
  }

  // 6. dossier hero portrait
  if (isDossier) {
    html = html.replace(/(<div class="hero-right")>([\s\S]*?)(<div class="hero-stamp")[^>]*>/, (m, open, body, stamp) => {
      const img = (body.match(/<img[^>]*>/) || [''])[0]
        .replace(/\sstyle="[^"]*"/, '')
        .replace(/\sloading="lazy"/, '')
        .replace(/<img/, '<img data-parallax="0.06" fetchpriority="high"');
      return `${open.replace('class="hero-right"', 'class="hero-right rv-img"')}>\n    ${img}\n    ${stamp}>`;
    });
  }

  // 7. inline style attributes → tokens
  html = mapInlineStyles(html);
  // inline hover handlers that wrote legacy colours
  html = html.replace(/\s+onmouseover="this\.style\.[^"]*"\s+onmouseout="this\.style\.[^"]*"/g, '');

  fs.writeFileSync(path.join(ROOT, file), html);
  return true;
}

if (require.main === module) {
const args = process.argv.slice(2);
const files = args.length ? args : fs.readdirSync(ROOT).filter((f) => f.endsWith('.html') && !/^index(-en)?\.html$/.test(f) && !f.startsWith('google'));
let n = 0;
for (const f of files) if (transform(f)) n++;
console.log(`migrated ${n} / ${files.length} pages`);
}

module.exports = { siteHeader, siteFooter, FONT_LINK };
