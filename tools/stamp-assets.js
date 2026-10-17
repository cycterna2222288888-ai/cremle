'use strict';
// Appends a content hash to every css/ and js/ reference in the HTML pages
// (css/kv.css -> css/kv.css?v=1a2b3c4d), so a deploy never pairs new markup
// with a stylesheet the browser still has cached.
// Run after editing anything in css/ or js/:  node tools/stamp-assets.js
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const ROOT = path.join(__dirname, '..');
const hash = (f) => crypto.createHash('md5').update(fs.readFileSync(path.join(ROOT, f))).digest('hex').slice(0, 8);

const assets = {};
for (const dir of ['css', 'js']) {
  for (const f of fs.readdirSync(path.join(ROOT, dir))) assets[`${dir}/${f}`] = hash(`${dir}/${f}`);
}

let changed = 0;
for (const page of fs.readdirSync(ROOT).filter((f) => f.endsWith('.html'))) {
  const file = path.join(ROOT, page);
  const html = fs.readFileSync(file, 'utf8');
  const out = html.replace(/(href|src)="((?:css|js)\/[^"?]+)(?:\?v=[0-9a-f]+)?"/g, (m, attr, ref) =>
    assets[ref] ? `${attr}="${ref}?v=${assets[ref]}"` : m);
  if (out !== html) { fs.writeFileSync(file, out); changed++; }
}
console.log(`stamped ${Object.keys(assets).length} assets in ${changed} pages`);
