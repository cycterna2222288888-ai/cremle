'use strict';
// Строит data/search-index.json из канонического каталога people.js и HTML-файлов досье.
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const peopleContext = {};
vm.runInNewContext(fs.readFileSync(path.join(__dirname, 'people.js'), 'utf8'), peopleContext);

const PEOPLE = peopleContext.PEOPLE || [];
const DOSSIERS = PEOPLE.flatMap((person) => ([
  {
    file: `${person.slug}.html`,
    lang: 'ru',
    name: person.nameRU,
    channel: person.channel,
    tags: [],
  },
  {
    file: `${person.slug}-en.html`,
    lang: 'en',
    name: person.nameEN,
    channel: person.channel,
    tags: [],
  },
]));

function stripTags(html) {
  return html
    .replace(/<[^>]+>/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function extractText(html) {
  return html
    .replace(/<style[\s\S]*?<\/style>/gi, '')
    .replace(/<script[\s\S]*?<\/script>/gi, '')
    .replace(/<svg[\s\S]*?<\/svg>/gi, '')
    .replace(/<[^>]+>/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
    .slice(0, 3000);
}

function extractQuotes(html) {
  const quotes = [];
  const quotePattern = /<[^>]+class="[^"]*(?:meme-text|quote-text)[^"]*"[^>]*>([\s\S]*?)<\/[^>]+>/gi;
  let match;
  while ((match = quotePattern.exec(html)) !== null) {
    const text = stripTags(match[1]);
    if (text) quotes.push(text);
  }
  return quotes.slice(0, 5);
}

const index = DOSSIERS.map(({ file, lang, name, channel, tags }) => {
  const htmlPath = path.join(__dirname, file);
  let bio = '';
  let quotes = [];
  try {
    const html = fs.readFileSync(htmlPath, 'utf8');
    bio = extractText(html);
    quotes = extractQuotes(html);
  } catch (e) {
    console.warn(`  не найден: ${file}`);
  }
  return { file, lang, name, channel, tags, bio, quotes };
});

fs.mkdirSync(path.join(__dirname, 'data'), { recursive: true });
fs.writeFileSync(
  path.join(__dirname, 'data', 'search-index.json'),
  JSON.stringify(index, null, 2)
);
console.log(`Индекс построен: ${index.length} страниц досье (${PEOPLE.length} персон)`);
