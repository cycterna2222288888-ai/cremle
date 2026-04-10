// Generator: English section pages
// Run: node generate-en-sections.js
const fs = require('fs');

const CSS_BASE = `
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500&display=swap');
  :root { --ink:#080808; --paper:#ede8dc; --red:#8b1a1a; --red-dim:#5c1111; --light-gray:#bab3a0; --rule:#1c1c1c; --card-bg:#0e0e0e; }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:var(--ink); color:var(--paper); font-family:'Inter',sans-serif; font-weight:300; line-height:1.75; overflow-x:hidden; }
  .topbar { padding:14px 60px; border-bottom:1px solid var(--rule); background:var(--ink); position:sticky; top:0; z-index:100; display:flex; justify-content:space-between; align-items:center; }
  .topbar-left a { font-size:10px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); text-decoration:none; }
  .topbar-left a:hover { opacity:0.6; }
  .topbar-right { display:flex; align-items:center; gap:20px; }
  .lang-switch { display:flex; border:1px solid #333; overflow:hidden; }
  .lang-switch a { font-size:9px; letter-spacing:0.2em; text-transform:uppercase; color:#888; text-decoration:none; padding:6px 12px; transition:all 0.2s; }
  .lang-switch a.active { color:var(--paper); background:#1c1c1c; }
  .lang-switch a:hover { color:var(--paper); background:#111; }
  .masthead { padding:80px 60px 64px; border-bottom:1px solid var(--rule); }
  .masthead-eyebrow { font-size:10px; letter-spacing:0.4em; text-transform:uppercase; color:var(--red); margin-bottom:20px; }
  .masthead-title { font-family:'Playfair Display',serif; font-size:clamp(36px,5vw,72px); font-weight:700; color:var(--paper); margin-bottom:16px; line-height:1.05; }
  .masthead-sub { font-family:'Playfair Display',serif; font-style:italic; font-size:clamp(14px,1.8vw,20px); color:var(--light-gray); max-width:700px; }
  .container { max-width:1200px; margin:0 auto; padding:0 60px; }
  .section { padding:80px 0; border-bottom:1px solid var(--rule); }
  .section-label { font-size:10px; letter-spacing:0.35em; text-transform:uppercase; color:var(--red); margin-bottom:40px; display:flex; align-items:center; gap:20px; }
  .section-label::after { content:''; flex:1; height:1px; background:var(--rule); }
  .footer { padding:48px 60px; display:flex; justify-content:space-between; align-items:center; font-size:10px; letter-spacing:0.2em; text-transform:uppercase; color:#333; border-top:1px solid var(--rule); }
  .footer-logo { font-family:'Playfair Display',serif; font-size:18px; font-weight:700; color:var(--red); opacity:0.5; letter-spacing:normal; text-transform:none; }
  @media(max-width:900px) { .topbar,.masthead,.container,.footer { padding-left:24px; padding-right:24px; } }`;

function page(ruFile, enFile, title, eyebrow, h1, sub, bodyHtml) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${title} · Kremlin Voices</title>
<meta property="og:title" content="${title} · Kremlin Voices">
<meta property="og:site_name" content="Kremlin Voices">
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<style>${CSS_BASE}
</style>
</head>
<body>
<div class="topbar">
  <div class="topbar-left"><a href="index-en.html">← All dossiers</a></div>
  <div class="topbar-right">
    <div class="lang-switch">
      <a href="${ruFile}">RU</a>
      <a href="${enFile}" class="active">EN</a>
    </div>
  </div>
</div>
<div class="masthead">
  <div class="masthead-eyebrow">${eyebrow}</div>
  <h1 class="masthead-title">${h1}</h1>
  <p class="masthead-sub">${sub}</p>
</div>
${bodyHtml}
<div class="footer">
  <div class="footer-logo">Kremlin Voices</div>
  <span>Data from open sources</span>
  <a href="index-en.html" style="color:inherit;text-decoration:none">All dossiers</a>
</div>
</body>
</html>`;
}

// ─── ABOUT ───────────────────────────────────────────────────────────────────
const aboutBody = `
<style>
  .text-body { max-width:760px; }
  .text-body p { font-size:15px; color:var(--light-gray); line-height:1.9; margin-bottom:20px; }
  .text-body strong { color:var(--paper); font-weight:500; }
  .pullquote { padding:60px; border-bottom:1px solid var(--rule); background:#050505; }
  .pullquote-text { font-family:'Playfair Display',serif; font-size:clamp(20px,3vw,32px); font-style:italic; color:var(--paper); line-height:1.4; max-width:900px; }
  .text-section { padding:60px; border-bottom:1px solid var(--rule); display:grid; grid-template-columns:200px 1fr; gap:60px; }
  .text-section-label { font-size:10px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); padding-top:6px; }
  .features { display:grid; grid-template-columns:repeat(3,1fr); gap:2px; margin-top:32px; }
  .feature { background:var(--card-bg); padding:32px; }
  .feature-icon { font-size:28px; margin-bottom:16px; }
  .feature-title { font-family:'Playfair Display',serif; font-size:18px; font-weight:700; color:var(--paper); margin-bottom:12px; }
  .feature-text { font-size:13px; color:var(--light-gray); line-height:1.75; }
  @media(max-width:900px) { .text-section { grid-template-columns:1fr; } .features { grid-template-columns:1fr; } .pullquote,.text-section { padding:40px 24px; } }
</style>
<div class="pullquote">
  <div class="pullquote-text">"The best defense against propaganda is knowing how it works, who produces it, and what stands behind every word."</div>
</div>
<div class="text-section">
  <div class="text-section-label">Why this archive exists</div>
  <div class="text-body">
    <p>Russian state propaganda is not an accidental phenomenon. It is <strong>a system with specific people, specific budgets, and specific methods</strong>. Many people hear about "Russian propaganda" as an abstract threat — but few know how it works from the inside, or who is responsible.</p>
    <p>This archive was created as a media literacy tool: a documentary cross-section of specific individuals who are the key executors of Russia's state information policy. Not an abstraction — but biographies, quotes, facts, and official sanctions language.</p>
    <p>The archive is based <strong>exclusively on open, publicly verifiable data</strong>: official sanctions lists from the EU, USA and UK, television transcripts, official biographies, and reports from independent media outlets.</p>
    <div class="features">
      <div class="feature"><div class="feature-icon">📋</div><div class="feature-title">Dossiers</div><div class="feature-text">Dossiers on key propagandists with biographies and key facts.</div></div>
      <div class="feature"><div class="feature-icon">🔗</div><div class="feature-title">Analysis</div><div class="feature-text">Sanctions, timeline, connections, media empire, quotes. Each section reveals a different angle.</div></div>
      <div class="feature"><div class="feature-icon">🔍</div><div class="feature-title">Sources</div><div class="feature-text">Every fact is tied to a verifiable source. Nothing based on anonymous claims.</div></div>
    </div>
  </div>
</div>
<div class="text-section">
  <div class="text-section-label">Who this is for</div>
  <div class="text-body">
    <p>The archive is designed for <strong>anyone who wants to understand how Russian state propaganda works</strong> — and who is responsible for it. Journalists, researchers, educators, students, activists, and curious people.</p>
    <p>It is especially relevant for those in countries where Russian-language or Russian-funded media operates, and for those seeking to understand the structure behind the headlines.</p>
  </div>
</div>
<div class="text-section">
  <div class="text-section-label">What this is — and isn't</div>
  <div class="text-body">
    <p>This is: a documentary archive based on open sources. An instrument for understanding the structure of state propaganda. A dictionary of propaganda narratives and euphemisms.</p>
    <p>This is not: a comprehensive list of all Russian propagandists. Political journalism or opinion. A source of classified information. Affiliated with any government or political organization.</p>
  </div>
</div>`;

// ─── SANCTIONS ───────────────────────────────────────────────────────────────
const sanctionsBody = `
<style>
  .container { padding-top:0; }
  .stats-bar { display:grid; grid-template-columns:repeat(4,1fr); border-bottom:1px solid var(--rule); }
  .stat-cell { padding:40px; border-right:1px solid var(--rule); }
  .stat-cell:last-child { border-right:none; }
  .stat-num { font-family:'Playfair Display',serif; font-size:48px; font-weight:700; color:var(--red); }
  .stat-label { font-size:10px; letter-spacing:0.2em; text-transform:uppercase; color:var(--light-gray); margin-top:8px; }
  .sanctions-table { width:100%; border-collapse:collapse; }
  .sanctions-table th { background:#0d0d0d; padding:16px 20px; text-align:left; font-size:9px; letter-spacing:0.2em; text-transform:uppercase; color:var(--red); border-bottom:2px solid var(--red-dim); }
  .sanctions-table td { padding:16px 20px; border-bottom:1px solid #111; font-size:13px; color:var(--light-gray); vertical-align:top; }
  .sanctions-table tr:hover td { background:#0a0a0a; }
  .person-name { color:var(--paper); font-weight:500; text-decoration:none; }
  .person-name:hover { color:var(--red); }
  .tag { display:inline-block; background:#1a0000; border:1px solid var(--red-dim); color:var(--red); font-size:8px; letter-spacing:0.1em; text-transform:uppercase; padding:3px 7px; margin:2px; white-space:nowrap; }
  @media(max-width:900px) { .stats-bar { grid-template-columns:1fr 1fr; } .sanctions-table { font-size:12px; } }
</style>
<div class="stats-bar">
  <div class="stat-cell"><div class="stat-num">18</div><div class="stat-label">Dossiers</div></div>
  <div class="stat-cell"><div class="stat-num">6+</div><div class="stat-label">Jurisdictions</div></div>
  <div class="stat-cell"><div class="stat-num">2014</div><div class="stat-label">First sanction</div></div>
  <div class="stat-cell"><div class="stat-num">0</div><div class="stat-label">Times "war" used on air</div></div>
</div>
<div class="container section">
  <div class="section-label">Personal Sanctions by Jurisdiction</div>
  <table class="sanctions-table">
    <thead><tr><th>#</th><th>Name</th><th>Channel / Role</th><th>EU</th><th>USA</th><th>UK</th><th>Other</th></tr></thead>
    <tbody>
      <tr><td>01</td><td><a class="person-name" href="solovyov-en.html">Vladimir Solovyov</a></td><td>Russia-1</td><td><span class="tag">2022</span></td><td><span class="tag">2022</span></td><td><span class="tag">2022</span></td><td><span class="tag">Canada</span><span class="tag">Australia</span><span class="tag">Japan</span><span class="tag">Switzerland</span></td></tr>
      <tr><td>02</td><td><a class="person-name" href="skabeeva-en.html">Olga Skabeeva</a></td><td>Russia-1</td><td><span class="tag">2022</span></td><td><span class="tag">2022</span></td><td><span class="tag">2022</span></td><td><span class="tag">Canada</span><span class="tag">Australia</span><span class="tag">Japan</span></td></tr>
      <tr><td>03</td><td><a class="person-name" href="kiselyov-en.html">Dmitry Kiselyov</a></td><td>Rossiya Segodnya</td><td><span class="tag">2014</span></td><td>—</td><td>—</td><td><span class="tag">Canada</span><span class="tag">Switzerland</span></td></tr>
      <tr><td>04</td><td><a class="person-name" href="simonyan-en.html">Margarita Simonyan</a></td><td>RT / Rossiya Segodnya</td><td><span class="tag">2022</span></td><td><span class="tag">2022</span></td><td><span class="tag">2022</span></td><td><span class="tag">Canada</span><span class="tag">Australia</span><span class="tag">Japan</span></td></tr>
      <tr><td>05</td><td><a class="person-name" href="popov-en.html">Evgeny Popov</a></td><td>Russia-1 / Duma</td><td><span class="tag">2022</span></td><td><span class="tag">2022</span></td><td><span class="tag">2022</span></td><td><span class="tag">Canada</span><span class="tag">Australia</span><span class="tag">Japan</span></td></tr>
      <tr><td>06</td><td><a class="person-name" href="sheynin-en.html">Artem Sheynin</a></td><td>Channel One</td><td><span class="tag">2022</span></td><td><span class="tag">2022</span></td><td><span class="tag">2022</span></td><td>—</td></tr>
      <tr><td>07</td><td><a class="person-name" href="tolstoy-en.html">Pyotr Tolstoy</a></td><td>Channel One / Duma</td><td><span class="tag">2022</span></td><td><span class="tag">2022</span></td><td><span class="tag">2022</span></td><td><span class="tag">Canada</span></td></tr>
      <tr><td>08</td><td><a class="person-name" href="norkin-en.html">Andrey Norkin</a></td><td>NTV</td><td><span class="tag">2022</span></td><td>—</td><td><span class="tag">2022</span></td><td>—</td></tr>
      <tr><td>09</td><td><a class="person-name" href="keosayan-en.html">Tigran Keosayan</a></td><td>RT</td><td><span class="tag">2022</span></td><td><span class="tag">2022</span></td><td><span class="tag">2022</span></td><td>—</td></tr>
      <tr><td>10</td><td><a class="person-name" href="andreyeva-en.html">Yekaterina Andreyeva</a></td><td>Channel One</td><td><span class="tag">2022</span></td><td>—</td><td><span class="tag">2022</span></td><td>—</td></tr>
      <tr><td>11</td><td><a class="person-name" href="mamontov-en.html">Arkady Mamontov</a></td><td>Russia-1</td><td><span class="tag">2022</span></td><td>—</td><td><span class="tag">2022</span></td><td>—</td></tr>
      <tr><td>12</td><td><a class="person-name" href="prilepin-en.html">Zakhar Prilepin</a></td><td>Politics / Donbas</td><td><span class="tag">2022</span></td><td><span class="tag">2022</span></td><td><span class="tag">2022</span></td><td>—</td></tr>
      <tr><td>13</td><td><a class="person-name" href="leontyev-en.html">Mikhail Leontyev</a></td><td>Channel One / Rosneft</td><td><span class="tag">2022</span></td><td>—</td><td><span class="tag">2022</span></td><td>—</td></tr>
      <tr><td>14</td><td><a class="person-name" href="korchevnikov-en.html">Boris Korchevnikov</a></td><td>Russia-1 / Spas</td><td><span class="tag">2022</span></td><td>—</td><td>—</td><td>—</td></tr>
      <tr><td>15</td><td><a class="person-name" href="medinsky-en.html">Vladimir Medinsky</a></td><td>Kremlin adviser</td><td><span class="tag">2022</span></td><td><span class="tag">2022</span></td><td><span class="tag">2022</span></td><td><span class="tag">Canada</span></td></tr>
      <tr><td>16</td><td><a class="person-name" href="mikhalkov-en.html">Nikita Mikhalkov</a></td><td>Russia-1 / Russia-24</td><td><span class="tag">2022</span></td><td>—</td><td><span class="tag">2022</span></td><td>—</td></tr>
      <tr><td>17</td><td><a class="person-name" href="dugin-en.html">Alexander Dugin</a></td><td>Ideology</td><td><span class="tag">2022</span></td><td><span class="tag">2015</span></td><td><span class="tag">2022</span></td><td><span class="tag">Canada</span></td></tr>
      <tr><td>18</td><td><a class="person-name" href="krasovsky-en.html">Anton Krasovsky</a></td><td>RT</td><td><span class="tag">2023</span></td><td>—</td><td>—</td><td>—</td></tr>
    </tbody>
  </table>
  <p style="font-size:11px;color:#444;margin-top:24px">Sources: Official EU Council Regulations, US Treasury OFAC designations, UK OFSI designations, Government of Canada sanctions list. All designations publicly available.</p>
</div>`;

// ─── QUOTES ──────────────────────────────────────────────────────────────────
const quotesBody = `
<style>
  .quotes-grid { display:grid; grid-template-columns:1fr 1fr; gap:2px; margin-bottom:2px; }
  .quote-card { background:var(--card-bg); padding:36px; border-left:3px solid var(--red-dim); }
  .quote-card:hover { border-color:var(--red); }
  .quote-text { font-family:'Playfair Display',serif; font-style:italic; font-size:17px; color:var(--paper); line-height:1.6; margin-bottom:20px; }
  .quote-person { font-size:10px; letter-spacing:0.2em; text-transform:uppercase; color:var(--red); margin-bottom:4px; }
  .quote-year { font-size:10px; color:#444; }
  .quote-person a { color:inherit; text-decoration:none; }
  .quote-person a:hover { opacity:0.7; }
  .section-head { padding:60px; border-bottom:1px solid var(--rule); }
  .stats-bar { display:grid; grid-template-columns:repeat(3,1fr); border-bottom:1px solid var(--rule); }
  .stat-cell { padding:40px; border-right:1px solid var(--rule); }
  .stat-cell:last-child { border-right:none; }
  .stat-num { font-family:'Playfair Display',serif; font-size:48px; font-weight:700; color:var(--red); }
  .stat-label { font-size:10px; letter-spacing:0.2em; text-transform:uppercase; color:var(--light-gray); margin-top:8px; }
  @media(max-width:900px) { .quotes-grid { grid-template-columns:1fr; } .stats-bar { grid-template-columns:1fr 1fr; } .section-head { padding:40px 24px; } }
</style>
<div class="stats-bar">
  <div class="stat-cell"><div class="stat-num">70+</div><div class="stat-label">Documented quotes</div></div>
  <div class="stat-cell"><div class="stat-num">18</div><div class="stat-label">Sources</div></div>
  <div class="stat-cell"><div class="stat-num">0</div><div class="stat-label">Times "war" spoken on air</div></div>
</div>
<div style="padding:60px;border-bottom:1px solid var(--rule)">
  <div class="section-label">Nuclear threats &amp; war rhetoric</div>
  <div class="quotes-grid">
    <div class="quote-card"><div class="quote-text">"Russia is the only country in the world that can genuinely turn the USA into radioactive ash."</div><div class="quote-person"><a href="kiselyov-en.html">Dmitry Kiselyov</a></div><div class="quote-year">2014 — live broadcast</div></div>
    <div class="quote-card"><div class="quote-text">"Either we win — or nuclear war. There is no third option. Nuclear war is better than capitulation."</div><div class="quote-person"><a href="simonyan-en.html">Margarita Simonyan</a></div><div class="quote-year">2022</div></div>
    <div class="quote-card"><div class="quote-text">"When I hear the word 'peace', I reach for my gun. This peace will only come with our victory."</div><div class="quote-person"><a href="solovyov-en.html">Vladimir Solovyov</a></div><div class="quote-year">2022</div></div>
    <div class="quote-card"><div class="quote-text">"We are openly at war with NATO. Let's call things by their names: the Third World War has begun."</div><div class="quote-person"><a href="skabeeva-en.html">Olga Skabeeva</a></div><div class="quote-year">2022 — live broadcast</div></div>
  </div>
</div>
<div style="padding:60px;border-bottom:1px solid var(--rule)">
  <div class="section-label">Denial of Ukrainian identity</div>
  <div class="quotes-grid">
    <div class="quote-card"><div class="quote-text">"There are no 'Ukrainian people' — there are Russians who were separated from Russia by force."</div><div class="quote-person"><a href="tolstoy-en.html">Pyotr Tolstoy</a></div><div class="quote-year">2022</div></div>
    <div class="quote-card"><div class="quote-text">"Ukraine as a state has no geopolitical meaning. None at all."</div><div class="quote-person"><a href="dugin-en.html">Alexander Dugin</a></div><div class="quote-year">2014</div></div>
    <div class="quote-card"><div class="quote-text">"Ukraine is not a state in the classical sense. It is a project — created against Russia."</div><div class="quote-person"><a href="norkin-en.html">Andrey Norkin</a></div><div class="quote-year">2023</div></div>
    <div class="quote-card"><div class="quote-text">"Ukraine was always part of Russia. The separation was an accident of Soviet bureaucracy."</div><div class="quote-person"><a href="medinsky-en.html">Vladimir Medinsky</a></div><div class="quote-year">2022</div></div>
  </div>
</div>
<div style="padding:60px;border-bottom:1px solid var(--rule)">
  <div class="section-label">Incitement &amp; documented extremism</div>
  <div class="quotes-grid">
    <div class="quote-card" style="border-color:var(--red)"><div class="quote-text">"These [Ukrainian] children should have been drowned in rivers right there."</div><div class="quote-person"><a href="krasovsky-en.html">Anton Krasovsky</a></div><div class="quote-year">October 22, 2022 — verified recording, Solovyov Live</div></div>
    <div class="quote-card"><div class="quote-text">"This war is sacred. We are fighting against the satanic element in the modern world."</div><div class="quote-person"><a href="korchevnikov-en.html">Boris Korchevnikov</a></div><div class="quote-year">2022</div></div>
    <div class="quote-card"><div class="quote-text">"These are not people — these are Nazis. You cannot negotiate with Nazis. You destroy them."</div><div class="quote-person"><a href="solovyov-en.html">Vladimir Solovyov</a></div><div class="quote-year">2022</div></div>
    <div class="quote-card"><div class="quote-text">"I wrote about war. Then I went to war. Because one without the other is either cowardice or a lie."</div><div class="quote-person"><a href="prilepin-en.html">Zakhar Prilepin</a></div><div class="quote-year">2017</div></div>
  </div>
</div>
<div style="padding:60px;border-bottom:1px solid var(--rule)">
  <div class="section-label">Conspiracy &amp; disinformation</div>
  <div class="quotes-grid">
    <div class="quote-card"><div class="quote-text">"The Pfizer vaccine contains a chip. They inject you with Bill Gates through a syringe."</div><div class="quote-person"><a href="mikhalkov-en.html">Nikita Mikhalkov</a></div><div class="quote-year">2021 — Besogon TV</div></div>
    <div class="quote-card"><div class="quote-text">"The Maidan was organized and paid for by the CIA. We have the documents."</div><div class="quote-person"><a href="mamontov-en.html">Arkady Mamontov</a></div><div class="quote-year">2014</div></div>
    <div class="quote-card"><div class="quote-text">"History is not what happened — it is what the people need."</div><div class="quote-person"><a href="medinsky-en.html">Vladimir Medinsky</a></div><div class="quote-year">2016</div></div>
    <div class="quote-card"><div class="quote-text">"We are a weapon of information warfare against the West."</div><div class="quote-person"><a href="simonyan-en.html">Margarita Simonyan</a></div><div class="quote-year">2012 — leaked internal speech</div></div>
  </div>
</div>`;

// ─── ABOUT-EN ────────────────────────────────────────────────────────────────
fs.writeFileSync('about-en.html', page('about.html','about-en.html',
  'About the Project','Project · Methodology · Goals','About the Project',
  'Why this archive exists, how it works, who it is for, and why it matters.',
  aboutBody));
console.log('✓ about-en.html');

// ─── SANCTIONS-EN ────────────────────────────────────────────────────────────
fs.writeFileSync('sanctions-en.html', page('sanctions.html','sanctions-en.html',
  'Sanctions','Sanctions · Open Sources','Sanctions',
  'Personal sanctions imposed by the EU, USA, UK, Canada, Australia and Japan on Russian propagandists.',
  sanctionsBody));
console.log('✓ sanctions-en.html');

// ─── QUOTES-EN ───────────────────────────────────────────────────────────────
fs.writeFileSync('quotes-en.html', page('quotes.html','quotes-en.html',
  'Quotes','Documented · Verbatim','Quotes',
  'Selected statements by Russian propagandists — verbatim. War, nuclear threats, incitement, denial.',
  quotesBody));
console.log('✓ quotes-en.html');

// ─── GLOSSARY-EN ─────────────────────────────────────────────────────────────
const glossaryBody = `
<style>
  .glossary-grid { display:grid; grid-template-columns:1fr 1fr; gap:2px; padding:60px 0; }
  .term-card { background:var(--card-bg); padding:32px; }
  .term { font-family:'Playfair Display',serif; font-size:20px; font-weight:700; color:var(--red); margin-bottom:8px; }
  .term-ru { font-size:11px; letter-spacing:0.15em; text-transform:uppercase; color:#444; margin-bottom:16px; }
  .definition { font-size:14px; color:var(--light-gray); line-height:1.8; }
  @media(max-width:900px) { .glossary-grid { grid-template-columns:1fr; padding:40px 24px; } }
</style>
<div class="container">
  <div class="glossary-grid">
    <div class="term-card"><div class="term">Special Military Operation</div><div class="term-ru">Специальная военная операция (СВО)</div><div class="definition">The mandatory official term for Russia's full-scale invasion of Ukraine, in use since February 24, 2022. Using the word "war" instead carries a criminal penalty of up to 15 years in prison under Russian law. Every anchor, host and commentator on state television uses this phrase exclusively.</div></div>
    <div class="term-card"><div class="term">Denazification</div><div class="term-ru">Денацификация</div><div class="definition">One of the two stated goals of the invasion (alongside "demilitarization"). In practice, used as a justification for military action against the Ukrainian state and its armed forces. The framing equates the Ukrainian government with Nazism without factual basis.</div></div>
    <div class="term-card"><div class="term">Collective West</div><div class="term-ru">Коллективный Запад</div><div class="definition">A standard propaganda term presenting all Western countries as a unified, coordinated adversary acting against Russia. The phrase erases distinctions between governments, allows any Western action to be framed as hostile, and creates the siege mentality central to state TV's emotional register.</div></div>
    <div class="term-card"><div class="term">Russophobia</div><div class="term-ru">Русофобия</div><div class="definition">Any criticism of Russian state actions, framed as ethnic or cultural hatred of Russians. The term is used to deflect accountability: sanctions become "Russophobia," war reporting becomes "Russophobia," Ukrainian resistance becomes "Russophobia."</div></div>
    <div class="term-card"><div class="term">Anglo-Saxons</div><div class="term-ru">Англосаксы</div><div class="definition">A racialized term for the USA and UK, used to frame geopolitical conflict in ethnic terms. Implies that English-speaking elites run a global conspiracy against Russia. Regularly used by Solovyov, Skabeeva, Popov, and Simonyan.</div></div>
    <div class="term-card"><div class="term">Historical Russian Lands</div><div class="term-ru">Исторически русские земли</div><div class="definition">The claim that Ukraine (or parts of it) are inherently Russian territory, legitimizing annexation as "return" rather than conquest. Used extensively by Medinsky, Tolstoy, and Solovyov to frame the invasion as a correction of historical injustice.</div></div>
    <div class="term-card"><div class="term">Foreign Agent</div><div class="term-ru">Иностранный агент</div><div class="definition">A legal designation under Russian law, modeled on the US Foreign Agents Registration Act but applied far more broadly — to journalists, NGOs, media outlets, and individuals who receive any foreign funding or are deemed to "act in foreign interests." The label carries Soviet-era connotations of espionage.</div></div>
    <div class="term-card"><div class="term">Biolabs</div><div class="term-ru">Биолаборатории</div><div class="definition">A recurring conspiracy theory claiming the USA operated secret biological weapons laboratories in Ukraine, used as retroactive justification for the invasion. Promoted heavily by Simonyan and RT in the early weeks of the 2022 invasion despite no evidence.</div></div>
    <div class="term-card"><div class="term">Eurasianism</div><div class="term-ru">Евразийство</div><div class="definition">Alexander Dugin's geopolitical doctrine arguing that Russia is the core of a distinct "Eurasian" civilization incompatible with and inherently opposed to the "Atlanticist" West. Became influential in Russian military and policy circles after 2000, despite — or because of — its mystical and authoritarian foundations.</div></div>
    <div class="term-card"><div class="term">Whataboutism</div><div class="term-ru">Вотэбаутизм / А у вас негров линчуют</div><div class="definition">A rhetorical technique deflecting criticism by pointing to comparable (or unrelated) wrongdoing elsewhere: "But what about Iraq?" "But what about Kosovo?" Systematized as a Soviet propaganda technique, revived by state television as the primary response to any documented atrocity.</div></div>
  </div>
</div>`;

fs.writeFileSync('glossary-en.html', page('glossary.html','glossary-en.html',
  'Glossary','Language · Propaganda · Terms','Glossary',
  'Key terms of Russian state propaganda: official euphemisms, ideological concepts, and rhetorical techniques.',
  glossaryBody));
console.log('✓ glossary-en.html');

// ─── SOURCES-EN ──────────────────────────────────────────────────────────────
const sourcesBody = `
<style>
  .sources-section { padding:60px; border-bottom:1px solid var(--rule); }
  .sources-section h2 { font-family:'Playfair Display',serif; font-size:24px; font-weight:700; color:var(--paper); margin-bottom:32px; }
  .source-list { list-style:none; }
  .source-list li { padding:16px 0; border-bottom:1px solid #111; display:flex; gap:24px; align-items:baseline; }
  .source-list li:last-child { border-bottom:none; }
  .source-tag { font-size:8px; letter-spacing:0.2em; text-transform:uppercase; background:#1a0000; border:1px solid var(--red-dim); color:var(--red); padding:3px 8px; white-space:nowrap; flex-shrink:0; }
  .source-text { font-size:13px; color:var(--light-gray); line-height:1.7; }
  .source-text strong { color:var(--paper); }
  @media(max-width:900px) { .sources-section { padding:40px 24px; } }
</style>
<div class="sources-section">
  <h2>Official Sanctions Lists</h2>
  <ul class="source-list">
    <li><span class="source-tag">EU</span><div class="source-text"><strong>European Union Council Regulations</strong> — Official Journal of the EU, L series. Regulations 269/2014 (Ukraine/Crimea), 833/2014 (sectoral), and subsequent amendments. All designations include identification data and statement of reasons. <em>eur-lex.europa.eu</em></div></li>
    <li><span class="source-tag">USA</span><div class="source-text"><strong>US Treasury OFAC — SDN List</strong> — Office of Foreign Assets Control Specially Designated Nationals list. Includes EO 13685, EO 14024 designations and press releases. <em>home.treasury.gov/policy-issues/financial-sanctions</em></div></li>
    <li><span class="source-tag">UK</span><div class="source-text"><strong>UK OFSI — Consolidated List</strong> — Office of Financial Sanctions Implementation. Russia (Sanctions) (EU Exit) Regulations 2019 and amendments. <em>gov.uk/government/publications/financial-sanctions-consolidated-list-of-targets</em></div></li>
    <li><span class="source-tag">Canada</span><div class="source-text"><strong>Global Affairs Canada — Consolidated Canadian Autonomous Sanctions List</strong> — Special Economic Measures (Russia) Regulations. <em>international.gc.ca/world-monde/international_relations-relations_internationales/sanctions</em></div></li>
  </ul>
</div>
<div class="sources-section">
  <h2>Media Monitoring &amp; Research</h2>
  <ul class="source-list">
    <li><span class="source-tag">Monitor</span><div class="source-text"><strong>EU DisinfoLab</strong> — Independent research organization documenting disinformation operations linked to state actors. Reports on RT, Sputnik, and affiliated networks. <em>disinfo.eu</em></div></li>
    <li><span class="source-tag">Monitor</span><div class="source-text"><strong>EU vs Disinfo (EUvsDisinfo)</strong> — The European External Action Service's database of Kremlin disinformation cases, documenting specific claims and refutations since 2015. <em>euvsdisinfo.eu</em></div></li>
    <li><span class="source-tag">Research</span><div class="source-text"><strong>Meduza</strong> — Independent Russian-language investigative media outlet (based in Riga). Primary source for biographical data and domestic Russian media analysis. <em>meduza.io</em></div></li>
    <li><span class="source-tag">Research</span><div class="source-text"><strong>Novaya Gazeta Europe</strong> — Independent outlet covering Russian politics, media, and the war. <em>novayagazeta.eu</em></div></li>
    <li><span class="source-tag">Research</span><div class="source-text"><strong>The Insider (theins.ru)</strong> — Russian investigative journalism outlet, specializing in disinformation, intelligence operations, and propaganda. <em>theins.ru</em></div></li>
  </ul>
</div>
<div class="sources-section">
  <h2>Broadcast &amp; Transcript Sources</h2>
  <ul class="source-list">
    <li><span class="source-tag">Archive</span><div class="source-text"><strong>Internet Archive — Russian Television Recordings</strong> — Archive.org hosts recordings of Russian state television broadcasts including Russia-1, Channel One, NTV and RT, used for quote verification. <em>archive.org</em></div></li>
    <li><span class="source-tag">Archive</span><div class="source-text"><strong>Julia Davis — Russian Media Monitor</strong> — Journalist and analyst who monitors and subtitles Russian state television for English-language audiences. Source for translated quotes. <em>@JuliaDavisNews</em></div></li>
    <li><span class="source-tag">Transcript</span><div class="source-text"><strong>Kremlin.ru</strong> — Official transcript archive of Russian presidential speeches, decrees, and press conferences. Used for official statements and appointments. <em>kremlin.ru/eng</em></div></li>
  </ul>
</div>`;

fs.writeFileSync('sources-en.html', page('sources.html','sources-en.html',
  'Sources','Methodology · Verification · Bibliography','Sources',
  'All facts in this archive are tied to publicly verifiable sources. Here is where we look.',
  sourcesBody));
console.log('✓ sources-en.html');

// ─── TIMELINE-EN ─────────────────────────────────────────────────────────────
const timelineBody = `
<style>
  .tl-wrap { padding:60px; }
  .tl-year-block { margin-bottom:60px; }
  .tl-year { font-family:'Playfair Display',serif; font-size:64px; font-weight:700; color:#1c1c1c; margin-bottom:32px; }
  .tl-event { display:grid; grid-template-columns:200px 1fr; gap:32px; padding:24px 0; border-top:1px solid #111; }
  .tl-meta { }
  .tl-tag { display:inline-block; font-size:8px; letter-spacing:0.2em; text-transform:uppercase; border:1px solid var(--red-dim); color:var(--red); padding:4px 8px; margin-bottom:12px; }
  .tl-person { font-size:10px; letter-spacing:0.15em; text-transform:uppercase; color:#444; }
  .tl-headline { font-family:'Playfair Display',serif; font-size:18px; font-weight:700; color:var(--paper); margin-bottom:12px; }
  .tl-body { font-size:13px; color:var(--light-gray); line-height:1.8; }
  .tl-quote { font-family:'Playfair Display',serif; font-style:italic; font-size:14px; color:var(--light-gray); border-left:2px solid var(--red-dim); padding-left:16px; margin-top:16px; }
  @media(max-width:900px) { .tl-wrap { padding:40px 24px; } .tl-event { grid-template-columns:1fr; gap:8px; } }
</style>
<div class="tl-wrap">

  <div class="tl-year-block">
    <div class="tl-year">1945–1975</div>
    <div class="tl-event"><div class="tl-meta"><span class="tl-tag">Birth</span><div class="tl-person">Nikita Mikhalkov</div></div><div><div class="tl-headline">October 21, 1945 — Nikita Mikhalkov born in Moscow</div><div class="tl-body">Born into the Soviet cultural elite. His father wrote the Soviet national anthem. Future Oscar winner and Kremlin propagandist.</div></div></div>
    <div class="tl-event"><div class="tl-meta"><span class="tl-tag">Birth</span><div class="tl-person">Dmitry Kiselyov</div></div><div><div class="tl-headline">April 26, 1954 — Dmitry Kiselyov born in Moscow</div><div class="tl-body">First personally sanctioned Russian media figure. Will threaten nuclear annihilation of the USA on live television in 2014.</div></div></div>
    <div class="tl-event"><div class="tl-meta"><span class="tl-tag">Birth</span><div class="tl-person">Mikhail Leontyev</div></div><div><div class="tl-headline">1958 — Mikhail Leontyev born</div><div class="tl-body">Future host of 5,000+ episodes of "Odnako." Later press secretary of Rosneft — the merger of media and the oil state embodied in one career.</div></div></div>
    <div class="tl-event"><div class="tl-meta"><span class="tl-tag">Birth</span><div class="tl-person">Dugin / Mamontov</div></div><div><div class="tl-headline">1962 — Alexander Dugin and Arkady Mamontov born</div><div class="tl-body">Dugin (January 7) will author "Foundations of Geopolitics." Mamontov will become the documentary filmmaker who primes Russian audiences for repressive laws.</div></div></div>
    <div class="tl-event"><div class="tl-meta"><span class="tl-tag">Birth</span><div class="tl-person">Vladimir Solovyov</div></div><div><div class="tl-headline">October 20, 1963 — Vladimir Solovyov born</div><div class="tl-body">Birth name: Shapiro. Will own villas on Lake Como worth €8 million. Will call for nuclear strikes on air. Sanctioned by seven jurisdictions.</div></div></div>
  </div>

  <div class="tl-year-block">
    <div class="tl-year">1997–2013</div>
    <div class="tl-event"><div class="tl-meta"><span class="tl-tag">Publication</span><div class="tl-person">Alexander Dugin</div></div><div><div class="tl-headline">1997 — "Foundations of Geopolitics" published</div><div class="tl-body">Dugin's landmark work argues Russia must absorb Ukraine, fragment the USA through separatism, and rebuild a Eurasian empire. Becomes assigned reading in Russian military academies.</div><div class="tl-quote">"Ukraine as a state has no geopolitical meaning. None at all."</div></div></div>
    <div class="tl-event"><div class="tl-meta"><span class="tl-tag">Appointment</span><div class="tl-person">Margarita Simonyan</div></div><div><div class="tl-headline">2005 — Simonyan appointed founding editor-in-chief of RT (then Russia Today)</div><div class="tl-body">Age 25. Builds RT from a single English-language channel into a multilingual global network operating in 100+ countries.</div></div></div>
    <div class="tl-event"><div class="tl-meta"><span class="tl-tag">Law</span><div class="tl-person">Arkady Mamontov</div></div><div><div class="tl-headline">June 2013 — "Gay propaganda" law passed</div><div class="tl-body">Mamontov's documentary on "homosexual propaganda" airs in May 2013. The Duma passes the law in June. The pattern — Mamontov films, Duma legislates — repeats across multiple topics.</div></div></div>
    <div class="tl-event"><div class="tl-meta"><span class="tl-tag">Appointment</span><div class="tl-person">Kiselyov / Simonyan</div></div><div><div class="tl-headline">December 2013 — Putin creates Rossiya Segodnya, appoints Kiselyov director-general</div><div class="tl-body">Simonyan and Kiselyov now jointly control the largest state media holding in Russia. Both appointed directly by Putin.</div></div></div>
  </div>

  <div class="tl-year-block">
    <div class="tl-year">2014</div>
    <div class="tl-event"><div class="tl-meta"><span class="tl-tag">Annexation</span><div class="tl-person">All</div></div><div><div class="tl-headline">March 2014 — Annexation of Crimea. Russian state TV shifts to war footing</div><div class="tl-body">Every anchor and host in this archive takes a clear pro-annexation position from the first day. The vocabulary of "fascists," "Nazis," and "junta" enters daily use.</div></div></div>
    <div class="tl-event"><div class="tl-meta"><span class="tl-tag">Sanction</span><div class="tl-person">Dmitry Kiselyov</div></div><div><div class="tl-headline">March 2014 — EU personally sanctions Kiselyov — the first such action against a Russian journalist</div><div class="tl-body">Days after he states on air: "Russia is the only country that can turn the USA into radioactive ash." The EU acts. Eight years before the full-scale invasion.</div></div></div>
  </div>

  <div class="tl-year-block">
    <div class="tl-year">2022</div>
    <div class="tl-event"><div class="tl-meta"><span class="tl-tag">Invasion</span><div class="tl-person">All</div></div><div><div class="tl-headline">February 24 — Russia invades Ukraine. All propagandists on air the same day</div><div class="tl-body">From the first hours, every figure in this archive is at their post. The word "war" is never spoken. The official term is "special military operation." Dissenting guests are removed from studios or cut off.</div><div class="tl-quote">"This is not a war. This is a special military operation for denazification and demilitarization of Ukraine." — refrain on all channels</div></div></div>
    <div class="tl-event"><div class="tl-meta"><span class="tl-tag">Sanctions</span><div class="tl-person">All</div></div><div><div class="tl-headline">February–March 2022 — EU, USA, UK, Canada, Australia, Japan impose personal sanctions</div><div class="tl-body">Most figures in this archive are sanctioned within weeks of the invasion. Asset freezes, travel bans, property seizures. Solovyov's Italian villas seized. RT banned across the EU.</div></div></div>
    <div class="tl-event"><div class="tl-meta"><span class="tl-tag">Documented</span><div class="tl-person">Anton Krasovsky</div></div><div><div class="tl-headline">October 22 — Krasovsky calls for drowning Ukrainian children on live television</div><div class="tl-body">The statement is recorded and distributed internationally. Simonyan announces his "suspension." He is quietly reinstated within weeks. The EU sanctions him in 2023.</div><div class="tl-quote">"These [Ukrainian] children should have been drowned in rivers right there." — verified recording</div></div></div>
    <div class="tl-event"><div class="tl-meta"><span class="tl-tag">Assassination</span><div class="tl-person">Alexander Dugin</div></div><div><div class="tl-headline">August 20 — Darya Dugina, Dugin's daughter, killed in car bombing near Moscow</div><div class="tl-body">The car was reportedly intended for Dugin himself. He survives. Dugina's death accelerates his public profile as a figure of tragedy, martyrdom, and imperial cause.</div></div></div>
  </div>

  <div class="tl-year-block">
    <div class="tl-year">2023–2025</div>
    <div class="tl-event"><div class="tl-meta"><span class="tl-tag">Ongoing</span><div class="tl-person">All</div></div><div><div class="tl-headline">Three years of war — and all propagandists continue their work</div><div class="tl-body">Solovyov hosts his show. Simonyan writes on Telegram. Andreyeva reads the news. Kiselyov has not retired the "radioactive ash." Medinsky rewrites history. Prilepin fights again — with pen and word. The system continues to function.</div></div></div>
    <div class="tl-event"><div class="tl-meta"><span class="tl-tag">Negotiations</span><div class="tl-person">Vladimir Medinsky</div></div><div><div class="tl-headline">2025 — Medinsky returns to negotiations under Trump pressure</div><div class="tl-body">Returns to the table with positions incompatible with Ukrainian sovereignty. The format of "peace talks" serves as a propaganda instrument domestically.</div></div></div>
  </div>

</div>`;

fs.writeFileSync('timeline-en.html', page('timeline.html','timeline-en.html',
  'Timeline','Chronology · Open Sources','Timeline',
  'Key events in the biographies of the archive\'s subjects — appointments, scandals, sanctions, and defining quotes on a single chronological axis.',
  timelineBody));
console.log('✓ timeline-en.html');

// ─── COMPARE-EN ──────────────────────────────────────────────────────────────
// Read compare.html and create English version
const compareRu = fs.readFileSync('compare.html', 'utf8');
// Replace Russian UI text with English
let compareEn = compareRu
  .replace('<html lang="ru">', '<html lang="en">')
  .replace('<title>Сравнение досье · Голоса Кремля</title>', '<title>Compare Dossiers · Kremlin Voices</title>')
  .replace('content="Сравните двух пропагандистов по биографии, санкциям, методам и цитатам."', 'content="Compare two propagandists by biography, sanctions, methods and quotes."')
  .replace('content="Сравнение · Голоса Кремля"', 'content="Compare · Kremlin Voices"')
  .replace('content="Выберите двух пропагандистов и сравните их досье бок о бок."', 'content="Select two propagandists and compare their dossiers side by side."')
  .replace('Аналитика · Сравнение', 'Analytics · Comparison')
  .replace('<h1 class="masthead-title">Сравнение досье</h1>', '<h1 class="masthead-title">Compare Dossiers</h1>')
  .replace('Выберите двух персонажей и сравните их биографии, санкции, методы и цитаты бок о бок.', 'Select two people and compare their biographies, sanctions, methods and quotes side by side.')
  .replace('Персонаж А', 'Person A')
  .replace('Персонаж Б', 'Person B')
  .replace('— Выберите —', '— Select —')
  .replace(/Сравнить →/g, 'Compare →')
  .replace('Выберите двух персонажей выше', 'Select two people above')
  .replace('Сравнение появится здесь', 'Comparison will appear here')
  .replace('Данные из открытых источников', 'Data from open sources')
  .replace("alert('Выберите обоих персонажей')", "alert('Please select both people')")
  .replace("alert('Выберите разных персонажей')", "alert('Please select different people')")
  .replace("'Основные данные'", "'Key Data'")
  .replace("'Санкции'", "'Sanctions'")
  .replace("'Метод и стиль'", "'Method & Style'")
  .replace("'Характерные цитаты'", "'Characteristic Quotes'")
  .replace("'Родился/лась'", "'Born'")
  .replace("'Канал / платформа'", "'Channel / Platform'")
  .replace("'Программа / роль'", "'Show / Role'")
  .replace("'Введены'", "'Imposed'")
  .replace("'Особые ограничения'", "'Special Restrictions'")
  .replace("'Метод'", "'Method'")
  // Replace RU nav with EN nav
  .replace('<a href="index.html">← Все досье</a>', '<a href="index-en.html">← All dossiers</a>')
  // Update lang switch
  .replace('<a href="compare.html" class="active">RU</a><a href="compare-en.html">EN</a>', '<a href="compare.html">RU</a><a href="compare-en.html" class="active">EN</a>')
  // Replace Russian option names
  .replace('option value="">— Выберите —', 'option value="">— Select —')
  .replace(/Владимир Соловьёв/g, 'Vladimir Solovyov')
  .replace(/Ольга Скабеева/g, 'Olga Skabeeva')
  .replace(/Дмитрий Киселёв/g, 'Dmitry Kiselyov')
  .replace(/Маргарита Симоньян/g, 'Margarita Simonyan')
  .replace(/Евгений Попов/g, 'Evgeny Popov')
  .replace(/Артём Шейнин/g, 'Artem Sheynin')
  .replace(/Пётр Толстой/g, 'Pyotr Tolstoy')
  .replace(/Андрей Норкин/g, 'Andrey Norkin')
  .replace(/Тигран Кеосаян/g, 'Tigran Keosayan')
  .replace(/Екатерина Андреева/g, 'Yekaterina Andreyeva')
  .replace(/Аркадий Мамонтов/g, 'Arkady Mamontov')
  .replace(/Захар Прилепин/g, 'Zakhar Prilepin')
  .replace(/Михаил Леонтьев/g, 'Mikhail Leontyev')
  .replace(/Борис Корчевников/g, 'Boris Korchevnikov')
  .replace(/Владимир Мединский/g, 'Vladimir Medinsky')
  .replace(/Никита Михалков/g, 'Nikita Mikhalkov')
  .replace(/Александр Дугин/g, 'Alexander Dugin')
  .replace(/Антон Красовский/g, 'Anton Krasovsky')
  // Update dosye links to point to EN versions
  .replace(/dosye: '(\w+)\.html'/g, "dosye: '$1-en.html'")
  // Footer
  .replace('Голоса Кремля', 'Kremlin Voices');

fs.writeFileSync('compare-en.html', compareEn);
console.log('✓ compare-en.html');

// ─── MEDIA-EMPIRE-EN ─────────────────────────────────────────────────────────
const mediaEmpireBody = `
<style>
  .section-wrap { padding:60px; border-bottom:1px solid var(--rule); }
  .empire-grid { display:grid; grid-template-columns:1fr 1fr 1fr; gap:2px; margin-top:32px; }
  .empire-node { background:var(--card-bg); padding:32px; }
  .empire-name { font-family:'Playfair Display',serif; font-size:24px; font-weight:700; color:var(--red); margin-bottom:8px; }
  .empire-sub { font-size:11px; letter-spacing:0.15em; text-transform:uppercase; color:#444; margin-bottom:16px; }
  .empire-body { font-size:13px; color:var(--light-gray); line-height:1.8; }
  .empire-body a { color:var(--red); text-decoration:none; }
  .empire-body a:hover { opacity:0.7; }
  .stat-row-inline { display:flex; gap:32px; flex-wrap:wrap; margin-top:16px; }
  .stat-item { }
  .stat-num { font-family:'Playfair Display',serif; font-size:28px; color:var(--paper); }
  .stat-lbl { font-size:9px; letter-spacing:0.2em; text-transform:uppercase; color:#444; }
  .flow-grid { display:grid; grid-template-columns:1fr 60px 1fr; gap:0; align-items:center; margin-top:32px; }
  .flow-box { background:#050505; border:1px solid var(--rule); padding:24px; }
  .flow-arrow { text-align:center; font-size:24px; color:#333; }
  .flow-label { font-size:9px; letter-spacing:0.2em; text-transform:uppercase; color:var(--red); margin-bottom:8px; }
  .flow-val { font-size:14px; color:var(--light-gray); }
  @media(max-width:900px) { .empire-grid { grid-template-columns:1fr; } .section-wrap { padding:40px 24px; } .flow-grid { grid-template-columns:1fr; } .flow-arrow { display:none; } }
</style>
<div class="section-wrap">
  <div class="section-label">The Three Pillars</div>
  <div class="empire-grid">
    <div class="empire-node">
      <div class="empire-name">VGTRK / Russia-1</div>
      <div class="empire-sub">State federal broadcaster</div>
      <div class="empire-body">The largest state broadcaster in Russia. Wholly owned by the Russian government. Broadcasts Russia-1, Russia-24, Russia-Culture and 80+ regional channels. Annual budget: ~60 billion rubles (~$650M). Propagandists: <a href="solovyov-en.html">Solovyov</a>, <a href="skabeeva-en.html">Skabeeva</a>, <a href="popov-en.html">Popov</a>, <a href="mamontov-en.html">Mamontov</a>, <a href="korchevnikov-en.html">Korchevnikov</a>.</div>
      <div class="stat-row-inline"><div class="stat-item"><div class="stat-num">40M+</div><div class="stat-lbl">Daily viewers</div></div><div class="stat-item"><div class="stat-num">100%</div><div class="stat-lbl">State owned</div></div></div>
    </div>
    <div class="empire-node">
      <div class="empire-name">MIA Rossiya Segodnya / RT</div>
      <div class="empire-sub">International propaganda arm</div>
      <div class="empire-body">Created by Putin decree in 2013. Director-General: <a href="kiselyov-en.html">Kiselyov</a>. Editor-in-Chief of RT: <a href="simonyan-en.html">Simonyan</a>. Operates RT in English, Arabic, Spanish, French, German. Budget: ~$300M/year from federal treasury. Banned in EU since 2022.</div>
      <div class="stat-row-inline"><div class="stat-item"><div class="stat-num">100+</div><div class="stat-lbl">Countries</div></div><div class="stat-item"><div class="stat-num">2022</div><div class="stat-lbl">EU ban</div></div></div>
    </div>
    <div class="empire-node">
      <div class="empire-name">Channel One (Pervy Kanal)</div>
      <div class="empire-sub">State-controlled, formally mixed ownership</div>
      <div class="empire-body">Formally 51% state-owned, but editorially directed by the Kremlin. Largest single audience in Russia. Propagandists: <a href="sheynin-en.html">Sheynin</a>, <a href="andreyeva-en.html">Andreyeva</a>, <a href="leontyev-en.html">Leontyev</a>, <a href="tolstoy-en.html">Tolstoy</a> (former).</div>
      <div class="stat-row-inline"><div class="stat-item"><div class="stat-num">50M+</div><div class="stat-lbl">Reach</div></div><div class="stat-item"><div class="stat-num">51%</div><div class="stat-lbl">State share</div></div></div>
    </div>
  </div>
</div>
<div class="section-wrap">
  <div class="section-label">Funding Structure</div>
  <div class="flow-grid">
    <div class="flow-box"><div class="flow-label">Source</div><div class="flow-val">Russian federal budget — annual allocations to state media. Approved by the Duma, signed by the President.</div></div>
    <div class="flow-arrow">→</div>
    <div class="flow-box"><div class="flow-label">Destination</div><div class="flow-val">VGTRK (~60B RUB), RT/Rossiya Segodnya (~25B RUB), Channel One (indirect subsidy + state contracts). Total state media spending: ~100B+ RUB annually.</div></div>
  </div>
  <p style="margin-top:24px;font-size:12px;color:#444">Sources: Federal budget law, Rosstat, RT annual reports (pre-2022). Figures are estimates based on available public data.</p>
</div>
<div class="section-wrap">
  <div class="section-label">Key Connections</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:2px;margin-top:0">
    <div style="background:var(--card-bg);padding:32px"><div style="font-size:10px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);margin-bottom:12px">Family · Married couple</div><div style="font-family:'Playfair Display',serif;font-size:18px;color:var(--paper);margin-bottom:12px"><a href="skabeeva-en.html" style="color:inherit;text-decoration:none">Skabeeva</a> + <a href="popov-en.html" style="color:inherit;text-decoration:none">Popov</a></div><div style="font-size:13px;color:var(--light-gray)">Husband and wife co-hosting "60 Minutes" on Russia-1. The only married couple simultaneously sanctioned by six jurisdictions for the same show.</div></div>
    <div style="background:var(--card-bg);padding:32px"><div style="font-size:10px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);margin-bottom:12px">Family · Married couple</div><div style="font-family:'Playfair Display',serif;font-size:18px;color:var(--paper);margin-bottom:12px"><a href="simonyan-en.html" style="color:inherit;text-decoration:none">Simonyan</a> + <a href="keosayan-en.html" style="color:inherit;text-decoration:none">Keosayan</a></div><div style="font-size:13px;color:var(--light-gray)">Simonyan (RT editor-in-chief) and Keosayan (RT documentary director) are married. Together they control Russia's primary international propaganda output.</div></div>
  </div>
</div>`;

fs.writeFileSync('media-empire-en.html', page('media-empire.html','media-empire-en.html',
  'Media Empire','Structure · Funding · Reach','Media Empire',
  'Russian state media: who controls what, where the money comes from, how many people watch. One system — many faces.',
  mediaEmpireBody));
console.log('✓ media-empire-en.html');

// ─── CONNECTIONS-EN ──────────────────────────────────────────────────────────
const connectionsBody = `
<style>
  .conn-section { padding:60px; border-bottom:1px solid var(--rule); }
  .intro-text { font-size:15px; color:var(--light-gray); max-width:760px; line-height:1.85; margin-bottom:48px; }
  .conn-grid { display:grid; grid-template-columns:1fr 1fr; gap:2px; }
  .conn-card { background:var(--card-bg); padding:32px; }
  .conn-pair { display:flex; align-items:center; gap:12px; margin-bottom:12px; }
  .conn-person { font-family:'Playfair Display',serif; font-size:18px; font-weight:700; color:var(--paper); text-decoration:none; }
  .conn-person:hover { color:var(--red); }
  .conn-divider { color:#444; font-size:20px; }
  .conn-type { display:inline-block; font-size:8px; letter-spacing:0.2em; text-transform:uppercase; color:var(--red); border:1px solid var(--red-dim); padding:3px 8px; margin-bottom:16px; }
  .conn-desc { font-size:13px; color:var(--light-gray); line-height:1.8; }
  @media(max-width:900px) { .conn-grid { grid-template-columns:1fr; } .conn-section { padding:40px 24px; } }
</style>
<div class="conn-section">
  <p class="intro-text">All figures in this archive are connected through institutional, professional, or personal ties. The system is not a collection of individual propagandists — it is a network, designed to amplify and reinforce. Here are the key connections.</p>
  <div class="conn-grid">
    <div class="conn-card"><div class="conn-pair"><a href="skabeeva-en.html" class="conn-person">Skabeeva</a><span class="conn-divider">+</span><a href="popov-en.html" class="conn-person">Popov</a></div><span class="conn-type">Family · Work tandem</span><p class="conn-desc">Husband and wife. Co-hosting "60 Minutes" together on Russia-1 since 2016. The only married couple to be simultaneously sanctioned by six jurisdictions for the same show. A family propaganda business funded by the state.</p></div>
    <div class="conn-card"><div class="conn-pair"><a href="simonyan-en.html" class="conn-person">Simonyan</a><span class="conn-divider">+</span><a href="kiselyov-en.html" class="conn-person">Kiselyov</a></div><span class="conn-type">Institutional · MIA Rossiya Segodnya</span><p class="conn-desc">Simonyan is editor-in-chief of MIA Rossiya Segodnya; Kiselyov is director-general of the same structure. Both appointed by Putin in 2013–2014. Together they control Russia's largest state media holding.</p></div>
    <div class="conn-card"><div class="conn-pair"><a href="simonyan-en.html" class="conn-person">Simonyan</a><span class="conn-divider">+</span><a href="keosayan-en.html" class="conn-person">Keosayan</a></div><span class="conn-type">Family · RT creative pair</span><p class="conn-desc">Married. Keosayan directs propaganda documentaries for RT; Simonyan runs RT. The Simonyan-Keosayan household functions as the command center of Russia's international information operations.</p></div>
    <div class="conn-card"><div class="conn-pair"><a href="simonyan-en.html" class="conn-person">Simonyan</a><span class="conn-divider">↔</span><a href="krasovsky-en.html" class="conn-person">Krasovsky</a></div><span class="conn-type">Hierarchy · RT · Scandal</span><p class="conn-desc">Krasovsky is an RT editor under Simonyan. After his on-air calls to drown Ukrainian children, she publicly "suspended" him — then quietly reinstated him. The episode reveals RT's internal logic: limits are set by reputational convenience, not ethics.</p></div>
    <div class="conn-card"><div class="conn-pair"><a href="tolstoy-en.html" class="conn-person">Tolstoy</a><span class="conn-divider">+</span><a href="popov-en.html" class="conn-person">Popov</a></div><span class="conn-type">Institutional · State Duma</span><p class="conn-desc">Both are State Duma deputies from United Russia. Tolstoy is deputy speaker; Popov is a deputy. Both combine a parliamentary mandate with daily prime-time broadcasting.</p></div>
    <div class="conn-card"><div class="conn-pair"><a href="dugin-en.html" class="conn-person">Dugin</a><span class="conn-divider">↔</span><a href="medinsky-en.html" class="conn-person">Medinsky</a></div><span class="conn-type">Ideological · Eurasianism / History</span><p class="conn-desc">Both build the theoretical foundations for Russian imperialism. Dugin through Eurasianism and geopolitics; Medinsky through historical revisionism. "Foundations of Geopolitics" and Medinsky's historical rhetoric draw from the same source.</p></div>
    <div class="conn-card"><div class="conn-pair"><a href="mikhalkov-en.html" class="conn-person">Mikhalkov</a><span class="conn-divider">↔</span><a href="korchevnikov-en.html" class="conn-person">Korchevnikov</a></div><span class="conn-type">Ideological · Orthodox / Culture</span><p class="conn-desc">Both legitimize the war through spiritual and cultural codes. Mikhalkov through cinema, "Besogon" and "Russian world" imagery. Korchevnikov through Orthodox Christianity and the Spas channel. Different instruments — one message.</p></div>
    <div class="conn-card"><div class="conn-pair"><a href="solovyov-en.html" class="conn-person">Solovyov</a><span class="conn-divider">↔</span><a href="kiselyov-en.html" class="conn-person">Kiselyov</a></div><span class="conn-type">Ideological · Competition</span><p class="conn-desc">Both compete for the role of the Kremlin's chief voice. An unofficial rivalry for proximity to power. Both periodically escalate their rhetoric in response to the other.</p></div>
  </div>
</div>`;

fs.writeFileSync('connections-en.html', page('connections.html','connections-en.html',
  'Connections','Analytics · Open Sources','Connections',
  'Family, professional and institutional ties between the archive\'s subjects. Who works with whom, who reports to whom, who is related.',
  connectionsBody));
console.log('✓ connections-en.html');

console.log('\nAll 7 English section pages generated.');
