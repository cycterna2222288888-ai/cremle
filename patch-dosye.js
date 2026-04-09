'use strict';
// Добавляет OG-теги, прогресс-бар чтения и ссылку "Сообщить" во все досье-страницы
const fs = require('fs');

const DOSYE = [
  { file: 'solovyov.html',    name: 'Владимир Соловьёв',    desc: 'Ведущий «России-1», самый высокооплачиваемый пропагандист Кремля. Санкции ЕС, США, Великобритании.' },
  { file: 'skabeeva.html',    name: 'Ольга Скабеева',       desc: 'Ведущая «60 минут» на «России-1». «Кукла Кремля» — биография, цитаты, санкции.' },
  { file: 'simonyan.html',    name: 'Маргарита Симоньян',   desc: 'Главный редактор RT. Архитектор российской дезинформации за рубежом. Санкции ЕС, США, Великобритании.' },
  { file: 'kiselyov.html',    name: 'Дмитрий Киселёв',      desc: 'Ведущий «Вести недели». Первый журналист России под санкциями ЕС. Ядерная риторика и 11 лет в списках.' },
  { file: 'popov.html',       name: 'Владимир Попов',       desc: 'Соведущий «60 минут» на «России-1», депутат Госдумы. Биография, цитаты, санкции.' },
  { file: 'sheynin.html',     name: 'Артём Шейнин',         desc: 'Ведущий «Время покажет» на Первом канале. Биография, методы пропаганды, санкции.' },
  { file: 'tolstoy.html',     name: 'Пётр Толстой',         desc: 'Вице-спикер Госдумы, потомок классика. Скандалы в ПАСЕ, санкции четырёх государств.' },
  { file: 'norkin.html',      name: 'Андрей Норкин',        desc: 'Ведущий «Место встречи» на НТВ. От независимого ТВ 1990-х к государственной пропаганде войны.' },
  { file: 'keosayan.html',    name: 'Тигран Кеосаян',       desc: 'Режиссёр и ведущий RT, муж Симоньян. Документальная пропаганда и санкции трёх государств.' },
  { file: 'andreyeva.html',   name: 'Екатерина Андреева',   desc: 'Главный диктор Первого канала. Голос государства — биографии, военные сводки, санкции.' },
  { file: 'mamontov.html',    name: 'Аркадий Мамонтов',     desc: 'Документалист «России-1». Главный хроникёр «специальной операции» на российском телевидении.' },
  { file: 'prilepin.html',    name: 'Захар Прилепин',       desc: 'Писатель, комбатант, пропагандист. Воевал на Донбассе с 2014 года, пережил покушение в 2023-м.' },
  { file: 'leontyev.html',    name: 'Михаил Леонтьев',      desc: 'Пресс-секретарь «Роснефти», телеведущий Первого канала. Геополитик и голос нефтяного национализма.' },
  { file: 'korchevnikov.html',name: 'Борис Корчевников',    desc: 'Ведущий «Спаса» и «Первого канала». Религиозное обоснование войны — «священная миссия России».' },
  { file: 'medinsky.html',    name: 'Владимир Мединский',   desc: 'Экс-министр культуры, главный переговорщик России. Исторические претензии как инструмент дипломатии.' },
];

const PROGRESS_BAR_CSS = `
  /* READING PROGRESS */
  #progress-bar {
    position: fixed;
    top: 0; left: 0;
    height: 2px;
    width: 0%;
    background: #8b1a1a;
    z-index: 9999;
    transition: width 0.1s linear;
  }`;

const PROGRESS_BAR_HTML = `<div id="progress-bar"></div>`;

const PROGRESS_BAR_JS = `
<script>
(function() {
  var bar = document.getElementById('progress-bar');
  if (!bar) return;
  window.addEventListener('scroll', function() {
    var doc = document.documentElement;
    var scrolled = doc.scrollTop || document.body.scrollTop;
    var total = doc.scrollHeight - doc.clientHeight;
    bar.style.width = total > 0 ? (scrolled / total * 100) + '%' : '0%';
  }, { passive: true });
})();
</script>`;

const SUBMIT_LINK = `<a href="submit.html" style="margin-left:auto;font-size:10px;letter-spacing:0.2em;text-transform:uppercase;color:#5c1111;text-decoration:none;border:1px solid #2a0a0a;padding:5px 12px;border-radius:2px;transition:all 0.2s" onmouseover="this.style.color='#8b1a1a';this.style.borderColor='#5c1111'" onmouseout="this.style.color='#5c1111';this.style.borderColor='#2a0a0a'">Сообщить</a>`;

let updated = 0;

for (const { file, name, desc } of DOSYE) {
  let html = fs.readFileSync(file, 'utf8');

  // 1. OG meta tags — insert after <title> if not present
  if (!html.includes('og:title')) {
    html = html.replace(
      `<title>${name} — досье</title>`,
      `<title>${name} — досье | Голоса Кремля</title>\n` +
      `<meta name="description" content="${desc}">\n` +
      `<meta property="og:type" content="article">\n` +
      `<meta property="og:title" content="${name} — Голоса Кремля">\n` +
      `<meta property="og:description" content="${desc}">\n` +
      `<meta property="og:site_name" content="Голоса Кремля">\n` +
      `<meta name="twitter:card" content="summary">\n` +
      `<meta name="twitter:title" content="${name} — Голоса Кремля">\n` +
      `<meta name="twitter:description" content="${desc}">\n` +
      `<link rel="icon" type="image/svg+xml" href="favicon.svg">`
    );
  }

  // 2. Reading progress bar CSS — inject before closing </style>
  if (!html.includes('progress-bar')) {
    html = html.replace(/(<\/style>)(?![\s\S]*<\/style>)/, PROGRESS_BAR_CSS + '\n$1');
  }

  // 3. Progress bar HTML — after <body>
  if (!html.includes('id="progress-bar"')) {
    html = html.replace('<body>', '<body>\n' + PROGRESS_BAR_HTML);
  }

  // 4. "Сообщить" link in nav-back
  if (!html.includes('submit.html') && html.includes('class="nav-back"')) {
    html = html.replace(
      /(<div class="nav-back">)([\s\S]*?)(<\/div>)/,
      '$1$2' + SUBMIT_LINK + '$3'
    );
  }

  // 5. Progress bar JS — before </body>
  if (!html.includes('progress-bar')) {
    html = html.replace('</body>', PROGRESS_BAR_JS + '\n</body>');
  }

  fs.writeFileSync(file, html);
  updated++;
  console.log(`  ✓ ${file}`);
}

console.log(`\nОбновлено: ${updated} файлов`);
