'use strict';
// Строит data/search-index.json из HTML-файлов досье
const fs   = require('fs');
const path = require('path');

const DOSYE = [
  { file: 'solovyov.html', name: 'Владимир Соловьёв', channel: 'rossiya1', tags: [] },
  { file: 'skabeeva.html', name: 'Ольга Скабеева', channel: 'rossiya1', tags: [] },
  { file: 'kiselyov.html', name: 'Дмитрий Киселёв', channel: 'rt', tags: [] },
  { file: 'simonyan.html', name: 'Маргарита Симоньян', channel: 'rt', tags: [] },
  { file: 'popov.html', name: 'Евгений Попов', channel: 'rossiya1', tags: [] },
  { file: 'sheynin.html', name: 'Артём Шейнин', channel: 'perviy', tags: [] },
  { file: 'tolstoy.html', name: 'Пётр Толстой', channel: 'vlast', tags: [] },
  { file: 'norkin.html', name: 'Андрей Норкин', channel: 'ntv', tags: [] },
  { file: 'keosayan.html', name: 'Тигран Кеосаян', channel: 'rt', tags: [] },
  { file: 'andreyeva.html', name: 'Екатерина Андреева', channel: 'perviy', tags: [] },
  { file: 'mamontov.html', name: 'Аркадий Мамонтов', channel: 'rossiya1', tags: [] },
  { file: 'prilepin.html', name: 'Захар Прилепин', channel: 'vlast', tags: [] },
  { file: 'leontyev.html', name: 'Михаил Леонтьев', channel: 'perviy', tags: [] },
  { file: 'korchevnikov.html', name: 'Борис Корчевников', channel: 'rossiya1', tags: [] },
  { file: 'medinsky.html', name: 'Владимир Мединский', channel: 'vlast', tags: [] },
  { file: 'mikhalkov.html', name: 'Никита Михалков', channel: 'kultura', tags: [] },
  { file: 'dugin.html', name: 'Александр Дугин', channel: 'ideolog', tags: [] },
  { file: 'krasovsky.html', name: 'Антон Красовский', channel: 'rt', tags: [] },
  { file: 'medvedev.html', name: 'Дмитрий Медведев', channel: 'vlast', tags: [] },
  { file: 'kadyrov.html', name: 'Рамзан Кадыров', channel: 'vlast', tags: [] },
  { file: 'malofeev.html', name: 'Константин Малофеев', channel: 'ideolog', tags: [] },
  { file: 'nikonov.html', name: 'Вячеслав Никонов', channel: 'vlast', tags: [] },
  { file: 'poddubny.html', name: 'Евгений Поддубный', channel: 'rt', tags: [] },
  { file: 'zakharova.html', name: 'Мария Захарова', channel: 'vlast', tags: [] },
  { file: 'kovalchuk.html', name: 'Юрий Ковальчук', channel: 'vlast', tags: [] },
  { file: 'turchak.html', name: 'Андрей Турчак', channel: 'vlast', tags: [] },
  { file: 'navka.html', name: 'Татьяна Навка', channel: 'kultura', tags: [] },
  { file: 'peskov.html', name: 'Дмитрий Песков', channel: 'vlast', tags: [] },
  { file: 'lavrov.html', name: 'Сергей Лавров', channel: 'vlast', tags: [] },
  { file: 'mizulina.html', name: 'Елена Мизулина', channel: 'vlast', tags: [] },
  { file: 'nebenzya.html', name: 'Василий Небензя', channel: 'vlast', tags: [] },
  { file: 'patrushev.html', name: 'Николай Патрушев', channel: 'vlast', tags: [] },
  { file: 'matvienko.html', name: 'Валентина Матвиенко', channel: 'vlast', tags: [] },
  { file: 'slutsky.html', name: 'Леонид Слуцкий', channel: 'vlast', tags: [] },
  { file: 'emizulina.html', name: 'Екатерина Мизулина', channel: 'vlast', tags: [] }
];

function extractText(html) {
  return html
    .replace(/<style[\s\S]*?<\/style>/gi, '')
    .replace(/<script[\s\S]*?<\/script>/gi, '')
    .replace(/<[^>]+>/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
    .slice(0, 3000);
}

function extractQuotes(html) {
  const matches = html.match(/class="meme-text"[^>]*>([\s\S]*?)<\/p>/g) || [];
  return matches.map(m => m.replace(/<[^>]+>/g, '').trim()).slice(0, 5);
}

const index = DOSYE.map(({ file, name, channel, tags }) => {
  const htmlPath = path.join(__dirname, file);
  let bio = '', quotes = [];
  try {
    const html = fs.readFileSync(htmlPath, 'utf8');
    bio    = extractText(html);
    quotes = extractQuotes(html);
  } catch (e) {
    console.warn(`  не найден: ${file}`);
  }
  return { file, name, channel, tags, bio, quotes };
});

fs.writeFileSync(
  path.join(__dirname, 'data', 'search-index.json'),
  JSON.stringify(index, null, 2)
);
console.log(`Индекс построен: ${index.length} досье`);
