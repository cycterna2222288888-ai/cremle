'use strict';
// Строит data/search-index.json из HTML-файлов досье
const fs   = require('fs');
const path = require('path');

const DOSYE = [
  { file: 'solovyov.html',    name: 'Владимир Соловьёв',    channel: 'Россия-1', tags: ['война','ядерная риторика','вилла в Италии'] },
  { file: 'skabeeva.html',    name: 'Ольга Скабеева',       channel: 'Россия-1', tags: ['60 минут','куклы Кремля','Курск'] },
  { file: 'simonyan.html',    name: 'Маргарита Симоньян',   channel: 'RT',       tags: ['RT','Tenet Media','пропаганда за рубежом'] },
  { file: 'kiselyov.html',    name: 'Дмитрий Киселёв',      channel: 'Россия-1', tags: ['ядерная война','Вести недели','санкции'] },
  { file: 'popov.html',       name: 'Владимир Попов',       channel: 'Россия-1', tags: ['60 минут','Госдума'] },
  { file: 'sheynin.html',     name: 'Артём Шейнин',         channel: 'Первый',   tags: ['Время покажет','ток-шоу'] },
  { file: 'tolstoy.html',     name: 'Пётр Толстой',         channel: 'Первый',   tags: ['ПАСЕ','Дума','национализм','Сорос'] },
  { file: 'norkin.html',      name: 'Андрей Норкин',        channel: 'НТВ',      tags: ['Место встречи','НТВ'] },
  { file: 'keosayan.html',    name: 'Тигран Кеосаян',       channel: 'RT',       tags: ['кино','RT','Симоньян'] },
  { file: 'andreyeva.html',   name: 'Екатерина Андреева',   channel: 'Первый',   tags: ['Новости','диктор','дезинформация'] },
  { file: 'mamontov.html',    name: 'Аркадий Мамонтов',     channel: 'Россия-1', tags: ['документалистика','расследования'] },
  { file: 'prilepin.html',    name: 'Захар Прилепин',       channel: 'Власть',   tags: ['писатель','ДНР','покушение','национализм'] },
  { file: 'leontyev.html',    name: 'Михаил Леонтьев',      channel: 'Первый',   tags: ['Роснефть','геополитика','Однако'] },
  { file: 'korchevnikov.html',name: 'Борис Корчевников',    channel: 'Спас',     tags: ['православие','священная война','Спас'] },
  { file: 'medinsky.html',    name: 'Владимир Мединский',   channel: 'Власть',   tags: ['переговоры','история','культура','министр'] },
  { file: 'mikhalkov.html',   name: 'Никита Михалков',      channel: 'Россия-1', tags: ['оскар','бесогон','культура','конспирология','режиссёр'] },
  { file: 'dugin.html',       name: 'Александр Дугин',      channel: 'Идеология',tags: ['евразийство','философия','идеолог','дугина','геополитика'] },
  { file: 'krasovsky.html',   name: 'Антон Красовский',     channel: 'RT',       tags: ['скандал','дети','восстановлен','rt'] },
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
