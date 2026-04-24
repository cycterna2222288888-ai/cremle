#!/usr/bin/env python3
"""Fix2: glossary-en, media-empire-en, 404.html, quotes year filter, sanctions stats."""
import re, os

BASE = '/Users/petrdracev/Desktop/proj/cremle/'

# ─────────────────────────────────────────────
# 1. GLOSSARY-EN: add 11 missing terms + section 2
# ─────────────────────────────────────────────
NEW_TERMS = """
    <div class="term-card"><div class="term">Forced Measures</div><div class="term-ru">Вынужденные меры</div><div class="definition">Any Russian military or repressive action framed as a response to external threat, removing Russia's agency and responsibility: "we didn't want this, but we were forced." Applied to describe the invasion, nuclear threats, and domestic repressions. Norkin's standard formula on "Mesto Vstrechi."</div></div>
    <div class="term-card"><div class="term">Demilitarization</div><div class="term-ru">Демилитаризация</div><div class="definition">The second stated goal of the invasion alongside "denazification" — destruction of Ukraine's military potential: army, equipment, infrastructure. In practice also includes strikes on civilian infrastructure (power plants, bridges, residential areas) described on state TV as "strikes on military infrastructure."</div></div>
    <div class="term-card"><div class="term">Information Warfare</div><div class="term-ru">Информационная война</div><div class="definition">Any Western reporting on Russia that contradicts the Kremlin narrative. The term allows any fact to be dismissed: "this isn't truth, this is an information attack." Paradoxically deployed by channels that are themselves instruments of information warfare — RT, Rossiya Segodnya. Also used to justify internal censorship.</div></div>
    <div class="term-card"><div class="term">Multipolar World</div><div class="term-ru">Многополярный мир</div><div class="definition">A world without US/Western dominance — in practice, a world where authoritarian regimes (Russia, China, Iran) maintain spheres of influence without international oversight of human rights. "Multipolarity" is used as the antonym of "unipolar Western diktat" but really means the absence of international mechanisms protecting against aggression.</div></div>
    <div class="term-card"><div class="term">Nazis / Nazi Regime</div><div class="term-ru">Нацисты / нацистский режим</div><div class="definition">The designation for the Ukrainian government and armed forces. Used systematically to dehumanize the enemy and embed the war in the "anti-fascism" narrative. Ukrainian president Zelensky is Jewish and was democratically elected with 73% of votes. Ukraine is a parliamentary democracy. The term has no factual basis.</div></div>
    <div class="term-card"><div class="term">Ours / Our Guys</div><div class="term-ru">Наши</div><div class="definition">Russian military forces. The term creates emotional identification between viewer and army, depersonalizing the enemy. "Ours" are always heroes; the other side always aggressors. Journalistic standards require neutral designations for conflict parties — "ours" is a marker of propaganda, not reporting.</div></div>
    <div class="term-card"><div class="term">Provocation</div><div class="term-ru">Провокация</div><div class="definition">Any Ukrainian or Western action framed as the cause of Russian actions, removing Russia's responsibility and casting it as victim. Strikes on Ukrainian cities are explained by "provocations"; arms deliveries to Ukraine are "provoking war." Russia always "responds," never "initiates." Used by Skabeeva and Popov constantly on "60 Minutes."</div></div>
    <div class="term-card"><div class="term">Russian World</div><div class="term-ru">Русский мир / Russkiy Mir</div><div class="definition">An ideological concept uniting all Russian-speakers and "spiritually connected" peoples under Moscow's patronage into an extraterritorial community. Used to justify Russian interference in other states (Ukraine, Georgia, Moldova, Baltic states) under the pretext of "protecting" this community. The concept denies the sovereignty of other states over their own citizens.</div></div>
    <div class="term-card"><div class="term">Sovereignty / Non-interference</div><div class="term-ru">Суверенитет и невмешательство</div><div class="definition">A principle Russia invokes when facing criticism of its domestic policy (human rights, elections). The same principle is ignored when Russia intervenes in Ukraine, Georgia, Moldova, Belarus. The double standard is a conscious rhetorical instrument — invoked selectively based on whether Russia is the subject or object of international pressure.</div></div>
    <div class="term-card"><div class="term">Traditional Values</div><div class="term-ru">Традиционные ценности</div><div class="definition">Russian "traditions" (restrictions on LGBTQ+ rights, gender inequality, state control of religion) contrasted with "Western decadence." Used to construct an ideological alternative to Western liberal values and mobilize conservative constituencies both domestically and internationally. Kiselyov's standard frame after his 2013 gay propaganda comments.</div></div>
    <div class="term-card"><div class="term">Junta</div><div class="term-ru">Хунта</div><div class="definition">The designation for the Ukrainian government that came to power after Maidan 2014. "Junta" means a military dictatorship that seized power illegally — the word deliberately evokes Latin American dictatorships. Ignores that Zelensky won presidential elections in 2019 with 73% of votes. Solovyov's standard term since 2014.</div></div>
    <div class="term-card"><div class="term">Escalation</div><div class="term-ru">Эскалация</div><div class="definition">Any Ukrainian or allied defensive action is declared "escalation" rather than defense. The term inverts logic: the aggressor threatens "escalation" in response to the victim's resistance. Used to pressure Western governments to limit military aid to Ukraine, with nuclear rhetoric as the implicit or explicit threat behind the warning.</div></div>"""

SECTION2 = """
<div class="container" style="padding-top:80px; padding-bottom:80px; border-top:1px solid var(--rule)">
  <div style="font-size:10px;letter-spacing:0.35em;text-transform:uppercase;color:var(--red);margin-bottom:40px;display:flex;align-items:center;gap:20px">How to Recognize Propaganda <span style="flex:1;height:1px;background:var(--rule);display:block"></span></div>
  <p style="font-size:15px;color:var(--light-gray);line-height:1.9;max-width:720px;margin-bottom:48px">Several markers that identify a propaganda text or statement — regardless of the source.</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:2px;background:var(--rule)">
    <div style="background:var(--ink);padding:40px">
      <div style="font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);margin-bottom:12px">Signal 1</div>
      <div style="font-family:'Playfair Display',serif;font-size:18px;color:var(--paper);margin-bottom:12px;font-weight:700">Dehumanizing the Enemy</div>
      <p style="font-size:13px;color:var(--light-gray);line-height:1.8">The opponent is referred to through group labels ("Nazis," "junta," "the West") rather than specific names and roles. This strips them of individual human characteristics and simplifies demonization.</p>
    </div>
    <div style="background:var(--ink);padding:40px">
      <div style="font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);margin-bottom:12px">Signal 2</div>
      <div style="font-family:'Playfair Display',serif;font-size:18px;color:var(--paper);margin-bottom:12px;font-weight:700">Victimhood Rhetoric</div>
      <p style="font-size:13px;color:var(--light-gray);line-height:1.8">The aggressor presents itself as victim ("forced measures," "response to provocation"). This removes moral responsibility and reframes aggression as self-defense. Russia never initiates — it only "responds."</p>
    </div>
    <div style="background:var(--ink);padding:40px">
      <div style="font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);margin-bottom:12px">Signal 3</div>
      <div style="font-family:'Playfair Display',serif;font-size:18px;color:var(--paper);margin-bottom:12px;font-weight:700">Language Substitution</div>
      <p style="font-size:13px;color:var(--light-gray);line-height:1.8">War → "special operation." Occupation → "liberation." Killing civilians → "strike on military infrastructure." Renaming changes the perception of reality without changing reality itself — the core technique of state euphemism.</p>
    </div>
    <div style="background:var(--ink);padding:40px">
      <div style="font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);margin-bottom:12px">Signal 4</div>
      <div style="font-family:'Playfair Display',serif;font-size:18px;color:var(--paper);margin-bottom:12px;font-weight:700">False Binary</div>
      <p style="font-size:13px;color:var(--light-gray);line-height:1.8">"Either with us or against us." Complex political situations are reduced to binary choice. A neutral position is declared impossible or treasonous. Any criticism is framed as support for the enemy — eliminating the space for nuance.</p>
    </div>
    <div style="background:var(--ink);padding:40px">
      <div style="font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);margin-bottom:12px">Signal 5</div>
      <div style="font-family:'Playfair Display',serif;font-size:18px;color:var(--paper);margin-bottom:12px;font-weight:700">Historical Appeal</div>
      <p style="font-size:13px;color:var(--light-gray);line-height:1.8">Current events are embedded in a historical narrative ("like 1941," "centuries-long war against Russia"). Historical analogies grant moral authority without requiring proof of their applicability to the current situation.</p>
    </div>
    <div style="background:var(--ink);padding:40px">
      <div style="font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);margin-bottom:12px">Signal 6</div>
      <div style="font-family:'Playfair Display',serif;font-size:18px;color:var(--paper);margin-bottom:12px;font-weight:700">Emotion Over Argument</div>
      <p style="font-size:13px;color:var(--light-gray);line-height:1.8">High emotional intensity, shouting, personal attacks — replace factual argumentation. Audiences perceive intensity as persuasiveness. Sheynin and Solovyov have mastered this technique. The louder the delivery, the weaker the underlying evidence.</p>
    </div>
  </div>
</div>"""

path = BASE + 'glossary-en.html'
with open(path) as f: h = f.read()

# Insert new terms before closing </div> of glossary-grid
h = h.replace(
    '    <div class="term-card"><div class="term">Whataboutism</div>',
    NEW_TERMS + '\n    <div class="term-card"><div class="term">Whataboutism</div>'
)
# Insert section 2 before footer
h = h.replace('<div class="footer">', SECTION2 + '\n<div class="footer">')

with open(path, 'w') as f: f.write(h)
print('✓ glossary-en.html: 11 terms + section 2 added')


# ─────────────────────────────────────────────
# 2. MEDIA-EMPIRE-EN: full expansion
# ─────────────────────────────────────────────
HIER_SECTION = """<div class="section-wrap" style="padding:60px;border-bottom:1px solid var(--rule)">
  <div class="section-label" style="font-size:10px;letter-spacing:0.35em;text-transform:uppercase;color:var(--red);margin-bottom:32px">01 · Power Hierarchy</div>
  <div style="background:var(--card-bg);border:1px solid var(--rule);padding:48px">
    <div style="text-align:center;margin-bottom:0">
      <div style="display:inline-block;border:1px solid var(--red-dim);padding:16px 32px;background:#050505">
        <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:var(--paper)">Kremlin · Presidential Administration</div>
        <div style="font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);margin-top:4px">Media Policy · Editorial Lines · Funding</div>
      </div>
    </div>
    <div style="height:40px;display:flex;justify-content:center;align-items:center"><span style="width:1px;height:40px;background:var(--rule);display:block"></span></div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2px;background:var(--rule)">
      <div style="background:var(--card-bg);padding:24px;text-align:center">
        <div style="font-family:'Playfair Display',serif;font-size:15px;font-weight:700;color:var(--paper);margin-bottom:6px">VGTRK</div>
        <div style="font-size:10px;color:var(--light-gray);line-height:1.4;margin-bottom:8px">Russia-1, Russia-24, Vesti</div>
        <div style="font-size:8px;letter-spacing:0.15em;text-transform:uppercase;color:var(--red)"><a href="solovyov-en.html" style="color:var(--red);text-decoration:none">Solovyov</a> · <a href="skabeeva-en.html" style="color:var(--red);text-decoration:none">Skabeeva</a> · <a href="popov-en.html" style="color:var(--red);text-decoration:none">Popov</a></div>
      </div>
      <div style="background:var(--card-bg);padding:24px;text-align:center">
        <div style="font-family:'Playfair Display',serif;font-size:15px;font-weight:700;color:var(--paper);margin-bottom:6px">MIA Rossiya Segodnya</div>
        <div style="font-size:10px;color:var(--light-gray);line-height:1.4;margin-bottom:8px">RT, Sputnik, RIA Novosti</div>
        <div style="font-size:8px;letter-spacing:0.15em;text-transform:uppercase;color:var(--red)"><a href="kiselyov-en.html" style="color:var(--red);text-decoration:none">Kiselyov</a> · <a href="simonyan-en.html" style="color:var(--red);text-decoration:none">Simonyan</a> · <a href="keosayan-en.html" style="color:var(--red);text-decoration:none">Keosayan</a></div>
      </div>
      <div style="background:var(--card-bg);padding:24px;text-align:center">
        <div style="font-family:'Playfair Display',serif;font-size:15px;font-weight:700;color:var(--paper);margin-bottom:6px">Channel One (PAO)</div>
        <div style="font-size:10px;color:var(--light-gray);line-height:1.4;margin-bottom:8px">Pervy Kanal · 51% state-owned</div>
        <div style="font-size:8px;letter-spacing:0.15em;text-transform:uppercase;color:var(--red)"><a href="sheynin-en.html" style="color:var(--red);text-decoration:none">Sheynin</a> · <a href="andreyeva-en.html" style="color:var(--red);text-decoration:none">Andreyeva</a></div>
      </div>
    </div>
    <div style="height:40px;display:flex;justify-content:center;align-items:center"><span style="width:1px;height:40px;background:var(--rule);display:block"></span></div>
    <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:2px;background:var(--rule)">
      <div style="background:var(--card-bg);padding:24px;text-align:center">
        <div style="font-family:'Playfair Display',serif;font-size:15px;font-weight:700;color:var(--paper);margin-bottom:6px">State Duma · United Russia</div>
        <div style="font-size:10px;color:var(--light-gray);line-height:1.4;margin-bottom:8px">Media deputies with parliamentary immunity</div>
        <div style="font-size:8px;letter-spacing:0.15em;text-transform:uppercase;color:var(--red)"><a href="tolstoy-en.html" style="color:var(--red);text-decoration:none">Tolstoy</a> · <a href="popov-en.html" style="color:var(--red);text-decoration:none">Popov</a> · <a href="slutsky-en.html" style="color:var(--red);text-decoration:none">Slutsky</a></div>
      </div>
      <div style="background:var(--card-bg);padding:24px;text-align:center">
        <div style="font-family:'Playfair Display',serif;font-size:15px;font-weight:700;color:var(--paper);margin-bottom:6px">NTV (Gazprom-Media)</div>
        <div style="font-size:10px;color:var(--light-gray);line-height:1.4;margin-bottom:8px">Holding controlled by Gazprom state monopoly</div>
        <div style="font-size:8px;letter-spacing:0.15em;text-transform:uppercase;color:var(--red)"><a href="norkin-en.html" style="color:var(--red);text-decoration:none">Norkin</a></div>
      </div>
    </div>
  </div>
</div>"""

CHANNELS_SECTION = """<div class="section-wrap" style="padding:60px;border-bottom:1px solid var(--rule)">
  <div class="section-label" style="font-size:10px;letter-spacing:0.35em;text-transform:uppercase;color:var(--red);margin-bottom:32px">02 · Channels &amp; Programs</div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:2px;background:var(--rule)">
    <div style="background:var(--card-bg);padding:0">
      <div style="padding:24px 28px;border-bottom:1px solid var(--rule)">
        <div style="font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);margin-bottom:4px">Domestic</div>
        <div style="font-family:'Playfair Display',serif;font-size:16px;color:var(--paper)">Russia · For domestic audiences</div>
      </div>
      <div style="padding:20px 28px;border-bottom:1px solid #0d0d0d">
        <div style="font-size:13px;color:var(--paper);margin-bottom:4px">Evening with Solovyov</div>
        <div style="font-size:11px;color:#555;line-height:1.5;margin-bottom:6px">Russia-1 · Daily · Prime time. The country's flagship propaganda talk show.</div>
        <div style="font-size:8px;letter-spacing:0.15em;text-transform:uppercase;color:var(--red)"><a href="solovyov-en.html" style="color:var(--red);text-decoration:none">Solovyov</a></div>
      </div>
      <div style="padding:20px 28px;border-bottom:1px solid #0d0d0d">
        <div style="font-size:13px;color:var(--paper);margin-bottom:4px">60 Minutes</div>
        <div style="font-size:11px;color:#555;line-height:1.5;margin-bottom:6px">Russia-1 · Daily · 2 hours. Married couple's aggressive propaganda duet.</div>
        <div style="font-size:8px;letter-spacing:0.15em;text-transform:uppercase;color:var(--red)"><a href="skabeeva-en.html" style="color:var(--red);text-decoration:none">Skabeeva</a> · <a href="popov-en.html" style="color:var(--red);text-decoration:none">Popov</a></div>
      </div>
      <div style="padding:20px 28px;border-bottom:1px solid #0d0d0d">
        <div style="font-size:13px;color:var(--paper);margin-bottom:4px">Vesti Nedeli (Weekly News)</div>
        <div style="font-size:11px;color:#555;line-height:1.5;margin-bottom:6px">Russia-1 · Sunday flagship. Deputy DG — author of the "radioactive ash" phrase.</div>
        <div style="font-size:8px;letter-spacing:0.15em;text-transform:uppercase;color:var(--red)"><a href="kiselyov-en.html" style="color:var(--red);text-decoration:none">Kiselyov</a></div>
      </div>
      <div style="padding:20px 28px;border-bottom:1px solid #0d0d0d">
        <div style="font-size:13px;color:var(--paper);margin-bottom:4px">Time Will Tell</div>
        <div style="font-size:11px;color:#555;line-height:1.5;margin-bottom:6px">Channel One · Daily. Sheynin controls the studio with a microphone mute button.</div>
        <div style="font-size:8px;letter-spacing:0.15em;text-transform:uppercase;color:var(--red)"><a href="sheynin-en.html" style="color:var(--red);text-decoration:none">Sheynin</a></div>
      </div>
      <div style="padding:20px 28px">
        <div style="font-size:13px;color:var(--paper);margin-bottom:4px">Meeting Place</div>
        <div style="font-size:11px;color:#555;line-height:1.5;margin-bottom:6px">NTV · Daily. Norkin runs it as a tribunal for "traitors."</div>
        <div style="font-size:8px;letter-spacing:0.15em;text-transform:uppercase;color:var(--red)"><a href="norkin-en.html" style="color:var(--red);text-decoration:none">Norkin</a></div>
      </div>
    </div>
    <div style="background:var(--card-bg);padding:0">
      <div style="padding:24px 28px;border-bottom:1px solid var(--rule)">
        <div style="font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);margin-bottom:4px">International</div>
        <div style="font-family:'Playfair Display',serif;font-size:16px;color:var(--paper)">RT · Sputnik · Global reach</div>
      </div>
      <div style="padding:20px 28px;border-bottom:1px solid #0d0d0d">
        <div style="font-size:13px;color:var(--paper);margin-bottom:4px">RT (Russia Today)</div>
        <div style="font-size:11px;color:#555;line-height:1.5;margin-bottom:6px">100+ countries · EN, AR, ES, DE, FR. EU-banned 2022. Registered foreign agent in US since 2017.</div>
        <div style="font-size:8px;letter-spacing:0.15em;text-transform:uppercase;color:var(--red)"><a href="simonyan-en.html" style="color:var(--red);text-decoration:none">Simonyan</a></div>
      </div>
      <div style="padding:20px 28px;border-bottom:1px solid #0d0d0d">
        <div style="font-size:13px;color:var(--paper);margin-bottom:4px">Sputnik</div>
        <div style="font-size:11px;color:#555;line-height:1.5;margin-bottom:6px">International news agency. Websites, radio, social media. Designated as disinformation in dozens of countries.</div>
        <div style="font-size:8px;letter-spacing:0.15em;text-transform:uppercase;color:var(--red)"><a href="simonyan-en.html" style="color:var(--red);text-decoration:none">Simonyan</a></div>
      </div>
      <div style="padding:20px 28px;border-bottom:1px solid #0d0d0d">
        <div style="font-size:13px;color:var(--paper);margin-bottom:4px">RT Arabic</div>
        <div style="font-size:11px;color:#555;line-height:1.5;margin-bottom:6px">Arab-speaking audiences · Middle East, North Africa. 75M+ views/month.</div>
        <div style="font-size:8px;letter-spacing:0.15em;text-transform:uppercase;color:var(--red)"><a href="simonyan-en.html" style="color:var(--red);text-decoration:none">Simonyan</a></div>
      </div>
      <div style="padding:20px 28px;border-bottom:1px solid #0d0d0d">
        <div style="font-size:13px;color:var(--paper);margin-bottom:4px">RT Doc / RT Cinema</div>
        <div style="font-size:11px;color:#555;line-height:1.5;margin-bottom:6px">Documentary films for international audiences. Propaganda formatted as artistic cinema.</div>
        <div style="font-size:8px;letter-spacing:0.15em;text-transform:uppercase;color:var(--red)"><a href="keosayan-en.html" style="color:var(--red);text-decoration:none">Keosayan</a></div>
      </div>
      <div style="padding:20px 28px">
        <div style="font-size:13px;color:var(--paper);margin-bottom:4px">Ruptly</div>
        <div style="font-size:11px;color:#555;line-height:1.5;margin-bottom:6px">Video agency selling content to world media. Calibrated "neutral" footage of events.</div>
        <div style="font-size:8px;letter-spacing:0.15em;text-transform:uppercase;color:var(--red)"><a href="simonyan-en.html" style="color:var(--red);text-decoration:none">Simonyan</a></div>
      </div>
    </div>
    <div style="background:var(--card-bg);padding:0">
      <div style="padding:24px 28px;border-bottom:1px solid var(--rule)">
        <div style="font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);margin-bottom:4px">Political Platform</div>
        <div style="font-family:'Playfair Display',serif;font-size:16px;color:var(--paper)">Duma · PACE · Official positions</div>
      </div>
      <div style="padding:20px 28px;border-bottom:1px solid #0d0d0d">
        <div style="font-size:13px;color:var(--paper);margin-bottom:4px">State Duma, United Russia</div>
        <div style="font-size:11px;color:#555;line-height:1.5;margin-bottom:6px">Deputy mandate provides immunity and official status for propaganda talking points.</div>
        <div style="font-size:8px;letter-spacing:0.15em;text-transform:uppercase;color:var(--red)"><a href="tolstoy-en.html" style="color:var(--red);text-decoration:none">Tolstoy</a> · <a href="popov-en.html" style="color:var(--red);text-decoration:none">Popov</a> · <a href="slutsky-en.html" style="color:var(--red);text-decoration:none">Slutsky</a></div>
      </div>
      <div style="padding:20px 28px;border-bottom:1px solid #0d0d0d">
        <div style="font-size:13px;color:var(--paper);margin-bottom:4px">PACE (until 2022)</div>
        <div style="font-size:11px;color:#555;line-height:1.5;margin-bottom:6px">Parliamentary Assembly of the Council of Europe. Platform for broadcasting Russian narratives to European audiences.</div>
        <div style="font-size:8px;letter-spacing:0.15em;text-transform:uppercase;color:var(--red)"><a href="tolstoy-en.html" style="color:var(--red);text-decoration:none">Tolstoy</a></div>
      </div>
      <div style="padding:20px 28px;border-bottom:1px solid #0d0d0d">
        <div style="font-size:13px;color:var(--paper);margin-bottom:4px">Moscow · Kremlin · Putin</div>
        <div style="font-size:11px;color:#555;line-height:1.5;margin-bottom:6px">Russia-1 · Sunday. Official Putin narrative. De facto state biography broadcast.</div>
        <div style="font-size:8px;letter-spacing:0.15em;text-transform:uppercase;color:var(--red)"><a href="solovyov-en.html" style="color:var(--red);text-decoration:none">Solovyov</a></div>
      </div>
      <div style="padding:20px 28px;border-bottom:1px solid #0d0d0d">
        <div style="font-size:13px;color:var(--paper);margin-bottom:4px">Duma Culture Committee</div>
        <div style="font-size:11px;color:#555;line-height:1.5;margin-bottom:6px">Control over cultural policy: film, media, publishing. Legislative umbrella for propaganda.</div>
        <div style="font-size:8px;letter-spacing:0.15em;text-transform:uppercase;color:var(--red)"><a href="tolstoy-en.html" style="color:var(--red);text-decoration:none">Tolstoy</a></div>
      </div>
      <div style="padding:20px 28px">
        <div style="font-size:13px;color:var(--paper);margin-bottom:4px">RIA Novosti</div>
        <div style="font-size:11px;color:#555;line-height:1.5;margin-bottom:6px">Russia's largest news agency. Primary source for official narratives across all state media.</div>
        <div style="font-size:8px;letter-spacing:0.15em;text-transform:uppercase;color:var(--red)"><a href="kiselyov-en.html" style="color:var(--red);text-decoration:none">Kiselyov</a></div>
      </div>
    </div>
  </div>
</div>"""

FUNDING_SECTION = """<div class="section-wrap" style="padding:60px;border-bottom:1px solid var(--rule)">
  <div class="section-label" style="font-size:10px;letter-spacing:0.35em;text-transform:uppercase;color:var(--red);margin-bottom:32px">03 · Funding</div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2px;background:var(--rule)">
    <div style="background:var(--card-bg);padding:32px;position:relative">
      <div style="font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);margin-bottom:12px">Source</div>
      <div style="font-family:'Playfair Display',serif;font-size:20px;font-weight:700;color:var(--paper);margin-bottom:8px;line-height:1.2">Russian Federal Budget</div>
      <div style="font-family:'Playfair Display',serif;font-size:28px;font-weight:700;color:var(--red);line-height:1;margin-bottom:8px">~$400M</div>
      <div style="font-size:11px;color:var(--light-gray);line-height:1.5">Annual funding for RT and MIA Rossiya Segodnya from the state budget. Figures from official Duma reports.</div>
    </div>
    <div style="background:var(--card-bg);padding:32px">
      <div style="font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);margin-bottom:12px">Recipient 1</div>
      <div style="font-family:'Playfair Display',serif;font-size:20px;font-weight:700;color:var(--paper);margin-bottom:8px;line-height:1.2">MIA Rossiya Segodnya</div>
      <div style="font-family:'Playfair Display',serif;font-size:28px;font-weight:700;color:var(--red);line-height:1;margin-bottom:8px">~$280M</div>
      <div style="font-size:11px;color:var(--light-gray);line-height:1.5">Largest state media holding. Includes RT, Sputnik, RIA Novosti, Ruptly. Director-General: <a href="kiselyov-en.html" style="color:var(--red);text-decoration:none">Kiselyov</a>.</div>
    </div>
    <div style="background:var(--card-bg);padding:32px">
      <div style="font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);margin-bottom:12px">Recipient 2</div>
      <div style="font-family:'Playfair Display',serif;font-size:20px;font-weight:700;color:var(--paper);margin-bottom:8px;line-height:1.2">VGTRK</div>
      <div style="font-family:'Playfair Display',serif;font-size:28px;font-weight:700;color:var(--red);line-height:1;margin-bottom:8px">~$120M</div>
      <div style="font-size:11px;color:var(--light-gray);line-height:1.5">All-Russia State Television and Radio. Russia-1, Russia-24, Kultura. 100% state-owned.</div>
    </div>
    <div style="background:var(--card-bg);padding:32px">
      <div style="font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);margin-bottom:12px">Hidden Funding</div>
      <div style="font-family:'Playfair Display',serif;font-size:20px;font-weight:700;color:var(--paper);margin-bottom:8px;line-height:1.2">Gazprom-Media</div>
      <div style="font-family:'Playfair Display',serif;font-size:28px;font-weight:700;color:var(--red);line-height:1;margin-bottom:8px">N/A</div>
      <div style="font-size:11px;color:var(--light-gray);line-height:1.5">NTV, TNT and others. Gazprom is a state monopoly. Formally corporate funding — effectively state funding.</div>
    </div>
  </div>
  <p style="margin-top:20px;font-size:12px;color:#444">Sources: Federal budget law, Rosstat, RT annual reports (pre-2022). Figures are estimates based on available public data.</p>
</div>"""

REACH_SECTION = """<div class="section-wrap" style="padding:60px;border-bottom:1px solid var(--rule)">
  <div class="section-label" style="font-size:10px;letter-spacing:0.35em;text-transform:uppercase;color:var(--red);margin-bottom:32px">04 · Reach &amp; Audience</div>
  <table style="width:100%;border-collapse:collapse;background:var(--rule);gap:2px">
    <thead>
      <tr>
        <th style="text-align:left;font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);padding:12px 20px;border-bottom:1px solid var(--rule);background:#050505">Outlet</th>
        <th style="text-align:left;font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);padding:12px 20px;border-bottom:1px solid var(--rule);background:#050505">Audience</th>
        <th style="text-align:left;font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);padding:12px 20px;border-bottom:1px solid var(--rule);background:#050505">Reach</th>
        <th style="text-align:left;font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);padding:12px 20px;border-bottom:1px solid var(--rule);background:#050505">International Status</th>
        <th style="text-align:left;font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--red);padding:12px 20px;border-bottom:1px solid var(--rule);background:#050505">Archive Link</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray);border-bottom:1px solid var(--rule);font-family:'Playfair Display',serif;font-size:14px;font-weight:700;color:var(--paper)">RT (all languages)</td>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray);border-bottom:1px solid var(--rule)">700M+ / month</td>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray);border-bottom:1px solid var(--rule)">100+ countries</td>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray);border-bottom:1px solid var(--rule)"><span style="display:inline-block;font-size:8px;letter-spacing:0.15em;text-transform:uppercase;border:1px solid var(--red-dim);color:var(--red);padding:3px 7px;margin:2px">Foreign agent (US)</span><span style="display:inline-block;font-size:8px;letter-spacing:0.15em;text-transform:uppercase;border:1px solid var(--red-dim);color:var(--red);padding:3px 7px;margin:2px">EU-banned 2022</span></td>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray);border-bottom:1px solid var(--rule)"><a href="simonyan-en.html" style="color:var(--red);text-decoration:none">Simonyan</a>, <a href="kiselyov-en.html" style="color:var(--red);text-decoration:none">Kiselyov</a></td>
      </tr>
      <tr>
        <td style="padding:16px 20px;font-size:14px;font-family:'Playfair Display',serif;font-weight:700;color:var(--paper);border-bottom:1px solid var(--rule)">Russia-1</td>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray);border-bottom:1px solid var(--rule)">~40M / day</td>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray);border-bottom:1px solid var(--rule)">Russia + CIS</td>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray);border-bottom:1px solid var(--rule)"><span style="display:inline-block;font-size:8px;letter-spacing:0.15em;text-transform:uppercase;border:1px solid var(--red-dim);color:var(--red);padding:3px 7px;margin:2px">EU sanctions</span></td>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray);border-bottom:1px solid var(--rule)"><a href="solovyov-en.html" style="color:var(--red);text-decoration:none">Solovyov</a>, <a href="skabeeva-en.html" style="color:var(--red);text-decoration:none">Skabeeva</a>, <a href="popov-en.html" style="color:var(--red);text-decoration:none">Popov</a></td>
      </tr>
      <tr>
        <td style="padding:16px 20px;font-size:14px;font-family:'Playfair Display',serif;font-weight:700;color:var(--paper);border-bottom:1px solid var(--rule)">Channel One</td>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray);border-bottom:1px solid var(--rule)">~35M / day</td>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray);border-bottom:1px solid var(--rule)">Russia + CIS</td>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray);border-bottom:1px solid var(--rule)"><span style="display:inline-block;font-size:8px;letter-spacing:0.15em;text-transform:uppercase;border:1px solid var(--red-dim);color:var(--red);padding:3px 7px;margin:2px">EU sanctions</span><span style="display:inline-block;font-size:8px;letter-spacing:0.15em;text-transform:uppercase;border:1px solid var(--red-dim);color:var(--red);padding:3px 7px;margin:2px">US sanctions</span></td>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray);border-bottom:1px solid var(--rule)"><a href="sheynin-en.html" style="color:var(--red);text-decoration:none">Sheynin</a>, <a href="andreyeva-en.html" style="color:var(--red);text-decoration:none">Andreyeva</a></td>
      </tr>
      <tr>
        <td style="padding:16px 20px;font-size:14px;font-family:'Playfair Display',serif;font-weight:700;color:var(--paper);border-bottom:1px solid var(--rule)">NTV (Gazprom)</td>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray);border-bottom:1px solid var(--rule)">~25M / day</td>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray);border-bottom:1px solid var(--rule)">Russia + CIS</td>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray);border-bottom:1px solid var(--rule)"><span style="display:inline-block;font-size:8px;letter-spacing:0.15em;text-transform:uppercase;border:1px solid var(--red-dim);color:var(--red);padding:3px 7px;margin:2px">EU sanctions</span></td>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray);border-bottom:1px solid var(--rule)"><a href="norkin-en.html" style="color:var(--red);text-decoration:none">Norkin</a></td>
      </tr>
      <tr>
        <td style="padding:16px 20px;font-size:14px;font-family:'Playfair Display',serif;font-weight:700;color:var(--paper)">Sputnik</td>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray)">~150M / month</td>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray)">30+ languages</td>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray)"><span style="display:inline-block;font-size:8px;letter-spacing:0.15em;text-transform:uppercase;border:1px solid var(--red-dim);color:var(--red);padding:3px 7px;margin:2px">Foreign agent (US)</span><span style="display:inline-block;font-size:8px;letter-spacing:0.15em;text-transform:uppercase;border:1px solid var(--red-dim);color:var(--red);padding:3px 7px;margin:2px">EU-banned</span></td>
        <td style="padding:16px 20px;font-size:12px;color:var(--light-gray)"><a href="simonyan-en.html" style="color:var(--red);text-decoration:none">Simonyan</a></td>
      </tr>
    </tbody>
  </table>
</div>"""

STATS_BAR = """<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:0;background:var(--rule);border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)">
  <div style="background:var(--card-bg);padding:32px 24px;text-align:center;border-left:1px solid var(--rule)">
    <div style="font-family:'Playfair Display',serif;font-size:40px;font-weight:700;color:var(--red);line-height:1">$400<span style="font-size:20px">M</span></div>
    <div style="font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--light-gray);margin-top:10px">RT state funding / year</div>
  </div>
  <div style="background:var(--card-bg);padding:32px 24px;text-align:center;border-left:1px solid var(--rule)">
    <div style="font-family:'Playfair Display',serif;font-size:40px;font-weight:700;color:var(--red);line-height:1">100+</div>
    <div style="font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--light-gray);margin-top:10px">countries RT reaches</div>
  </div>
  <div style="background:var(--card-bg);padding:32px 24px;text-align:center;border-left:1px solid var(--rule)">
    <div style="font-family:'Playfair Display',serif;font-size:40px;font-weight:700;color:var(--red);line-height:1">5</div>
    <div style="font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--light-gray);margin-top:10px">RT language editions</div>
  </div>
  <div style="background:var(--card-bg);padding:32px 24px;text-align:center;border-left:1px solid var(--rule)">
    <div style="font-family:'Playfair Display',serif;font-size:40px;font-weight:700;color:var(--red);line-height:1">2022</div>
    <div style="font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--light-gray);margin-top:10px">EU ban year</div>
  </div>
  <div style="background:var(--card-bg);padding:32px 24px;text-align:center;border-left:1px solid var(--rule)">
    <div style="font-family:'Playfair Display',serif;font-size:40px;font-weight:700;color:var(--red);line-height:1">35</div>
    <div style="font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--light-gray);margin-top:10px">individuals in this archive</div>
  </div>
</div>"""

path = BASE + 'media-empire-en.html'
with open(path) as f: h = f.read()

# Insert hierarchy + channels before existing "The Three Pillars"
h = h.replace(
    '<div class="section-wrap">\n  <div class="section-label">The Three Pillars</div>',
    HIER_SECTION + '\n' + CHANNELS_SECTION + '\n<div class="section-wrap">\n  <div class="section-label">The Three Pillars</div>'
)
# Replace simple funding section with rich one + reach + stats
h = h.replace(
    '<div class="section-wrap">\n  <div class="section-label">Funding Structure</div>\n  <div class="flow-grid">',
    FUNDING_SECTION + '\n' + REACH_SECTION + '\n' + STATS_BAR + '\n<div class="section-wrap" style="display:none">\n  <div class="section-label">Funding Structure</div>\n  <div class="flow-grid">'
)

with open(path, 'w') as f: f.write(h)
print('✓ media-empire-en.html: hierarchy + channels + funding + reach + stats added')


# ─────────────────────────────────────────────
# 3. 404.html — Russian version
# ─────────────────────────────────────────────
HTML_404 = '''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>404 — Голоса Кремля</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500&display=swap');
  :root { --ink:#080808; --paper:#ede8dc; --red:#8b1a1a; --light-gray:#bab3a0; --rule:#1c1c1c; }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:var(--ink); color:var(--paper); font-family:\'Inter\',sans-serif; font-weight:300; min-height:100vh; display:flex; flex-direction:column; }
  .topbar { border-bottom:1px solid var(--rule); padding:16px 60px; display:flex; justify-content:space-between; align-items:center; font-size:10px; letter-spacing:0.25em; text-transform:uppercase; color:var(--red); }
  .topbar a { color:var(--red); text-decoration:none; }
  .topbar a:hover { color:var(--paper); }
  .lang-switch { display:flex; border:1px solid #333; overflow:hidden; }
  .lang-switch a { font-size:9px; letter-spacing:0.2em; text-transform:uppercase; color:#888; text-decoration:none; padding:6px 12px; transition:all 0.2s; }
  .lang-switch a.active { color:var(--paper); background:#1c1c1c; }
  .body { flex:1; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; padding:40px; }
  .code { font-family:\'Playfair Display\',serif; font-size:clamp(6rem,20vw,12rem); color:#111; line-height:1; margin-bottom:8px; }
  .label { font-size:10px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); margin-bottom:24px; }
  h1 { font-family:\'Playfair Display\',serif; font-size:clamp(1.4rem,4vw,2.2rem); font-weight:400; margin-bottom:16px; }
  p { color:var(--light-gray); max-width:420px; font-size:15px; margin-bottom:40px; }
  .back { color:var(--paper); text-decoration:none; font-size:11px; letter-spacing:0.25em; text-transform:uppercase; border-bottom:1px solid var(--red); padding-bottom:2px; }
  .back:hover { color:var(--red); }
  @media(max-width:768px) { .topbar { padding:14px 20px; } }
</style>
<meta property="og:image" content="https://cycterna2222288888-ai.github.io/cremle/og-image.svg">
<meta name="twitter:image" content="https://cycterna2222288888-ai.github.io/cremle/og-image.svg">
<link rel="alternate" hreflang="ru" href="https://cycterna2222288888-ai.github.io/cremle/404.html">
<link rel="alternate" hreflang="en" href="https://cycterna2222288888-ai.github.io/cremle/404-en.html">
</head>
<body>

<nav class="topbar">
  <a href="index.html">← Голоса Кремля</a>
  <div class="lang-switch">
    <a href="404.html" class="active">RU</a>
    <a href="404-en.html">EN</a>
  </div>
</nav>

<div class="body">
  <div class="code">404</div>
  <div class="label">Страница не найдена</div>
  <h1>Этого досье не существует</h1>
  <p>Страница удалена, переименована или никогда не существовала.</p>
  <a href="index.html" class="back">← В архив</a>
</div>

</body>
</html>
'''
with open(BASE + '404.html', 'w') as f: f.write(HTML_404)
print('✓ 404.html: создан')


# ─────────────────────────────────────────────
# 4. QUOTES.HTML — add year filter
# ─────────────────────────────────────────────
path = BASE + 'quotes.html'
with open(path) as f: h = f.read()

YEAR_FILTER = """<div class="filter-bar" id="year-filter-bar" style="border-top:1px solid var(--rule)">
  <button class="filter-btn active" data-year="">Все годы</button>
  <button class="filter-btn" data-year="pre">До 2022</button>
  <button class="filter-btn" data-year="2022">2022</button>
  <button class="filter-btn" data-year="2023">2023</button>
  <button class="filter-btn" data-year="2024">2024</button>
  <button class="filter-btn" data-year="2025">2025</button>
</div>"""

# Insert year filter after the existing topic filter bar
h = h.replace(
    '<div class="filter-bar">\n  <button class="filter-btn active">Все темы</button>',
    '<div class="filter-bar" id="topic-filter-bar">\n  <button class="filter-btn active">Все темы</button>'
)
# Add year filter bar after closing filter-bar div
topic_close = '</div>\n<div class="quotes-wrap">'
h = h.replace(
    '<div class="quotes-wrap">',
    YEAR_FILTER + '\n<div class="quotes-wrap">',
    1  # first occurrence only
)

# Update filter JS to include year filter
OLD_JS = '''<script>
(function(){
  var sel = document.getElementById('qf-person');
  var inp = document.getElementById('qf-text');
  function filter(){
    var person = sel ? sel.value : '';
    var text = inp ? inp.value.trim().toLowerCase() : '';
    document.querySelectorAll('.quote-card').forEach(function(card){
      var pname = (card.querySelector('.qc-person')||{}).textContent||'';
      var qtext = (card.querySelector('.quote-text')||{}).textContent||'';
      var qdate = (card.querySelector('.qc-date')||{}).textContent||'';
      var matchP = !person || pname.trim() === person;
      var matchT = !text || qtext.toLowerCase().includes(text) || qdate.toLowerCase().includes(text);
      card.style.display = (matchP && matchT) ? '' : 'none';
    });
  }
  if (sel) sel.addEventListener('change', filter);
  if (inp) inp.addEventListener('input', filter);
})();
</script>'''

NEW_JS = '''<script>
(function(){
  var sel = document.getElementById('qf-person');
  var inp = document.getElementById('qf-text');
  var activeTopic = '';
  var activeYear = '';

  // topic filter
  document.querySelectorAll('#topic-filter-bar .filter-btn').forEach(function(btn){
    btn.addEventListener('click', function(){
      document.querySelectorAll('#topic-filter-bar .filter-btn').forEach(function(b){ b.classList.remove('active'); });
      btn.classList.add('active');
      activeTopic = btn.textContent.trim() === 'Все темы' ? '' : btn.textContent.trim();
      applyFilter();
    });
  });

  // year filter
  document.querySelectorAll('#year-filter-bar .filter-btn').forEach(function(btn){
    btn.addEventListener('click', function(){
      document.querySelectorAll('#year-filter-bar .filter-btn').forEach(function(b){ b.classList.remove('active'); });
      btn.classList.add('active');
      activeYear = btn.dataset.year || '';
      applyFilter();
    });
  });

  function applyFilter(){
    var person = sel ? sel.value : '';
    var text = inp ? inp.value.trim().toLowerCase() : '';
    document.querySelectorAll('.quote-card').forEach(function(card){
      var pname = (card.querySelector('.qc-person')||{}).textContent||'';
      var qtext = (card.querySelector('.quote-text')||{}).textContent||'';
      var qdate = (card.querySelector('.qc-date')||{}).textContent||'';
      var yr = parseInt((card.querySelector('.qc-year')||{}).textContent||'0');
      var matchP = !person || pname.trim() === person;
      var matchT = !text || qtext.toLowerCase().includes(text) || qdate.toLowerCase().includes(text);
      var matchTopic = !activeTopic || (card.dataset.topic && card.dataset.topic.includes(activeTopic));
      var matchYear = true;
      if (activeYear === 'pre') matchYear = yr > 0 && yr < 2022;
      else if (activeYear) matchYear = yr === parseInt(activeYear);
      card.style.display = (matchP && matchT && matchTopic && matchYear) ? '' : 'none';
    });
    // hide empty sections
    document.querySelectorAll('.quotes-section').forEach(function(sec){
      var visible = Array.from(sec.querySelectorAll('.quote-card')).some(function(c){ return c.style.display !== 'none'; });
      sec.style.display = visible ? '' : 'none';
    });
  }

  if (sel) sel.addEventListener('change', applyFilter);
  if (inp) inp.addEventListener('input', applyFilter);
})();
</script>'''

h = h.replace(OLD_JS, NEW_JS)

with open(path, 'w') as f: f.write(h)
print('✓ quotes.html: year filter added')


# ─────────────────────────────────────────────
# 5. SANCTIONS.HTML — fix count + per-country stats
# ─────────────────────────────────────────────
SANCTION_STATS = """<div class="sanction-stats">
  <div class="ss-title">Санкции по юрисдикциям · 35 персон в архиве</div>
  <div class="ss-grid" style="display:grid;grid-template-columns:repeat(6,1fr);gap:2px;background:var(--rule)">
    <div class="ss-cell">
      <div class="ss-country">Европейский союз</div>
      <div class="ss-count">23</div>
      <div class="ss-bar-bg"><div class="ss-bar" style="width:66%"></div></div>
      <div class="ss-pct">66% · с 2014</div>
    </div>
    <div class="ss-cell">
      <div class="ss-country">Великобритания</div>
      <div class="ss-count">19</div>
      <div class="ss-bar-bg"><div class="ss-bar" style="width:54%"></div></div>
      <div class="ss-pct">54% · с 2022</div>
    </div>
    <div class="ss-cell">
      <div class="ss-country">США</div>
      <div class="ss-count">13</div>
      <div class="ss-bar-bg"><div class="ss-bar" style="width:37%"></div></div>
      <div class="ss-pct">37% · с 2017</div>
    </div>
    <div class="ss-cell">
      <div class="ss-country">Канада</div>
      <div class="ss-count">10</div>
      <div class="ss-bar-bg"><div class="ss-bar" style="width:29%"></div></div>
      <div class="ss-pct">29%</div>
    </div>
    <div class="ss-cell">
      <div class="ss-country">Австралия</div>
      <div class="ss-count">5</div>
      <div class="ss-bar-bg"><div class="ss-bar" style="width:14%"></div></div>
      <div class="ss-pct">14%</div>
    </div>
    <div class="ss-cell">
      <div class="ss-country">Япония</div>
      <div class="ss-count">5</div>
      <div class="ss-bar-bg"><div class="ss-bar" style="width:14%"></div></div>
      <div class="ss-pct">14%</div>
    </div>
  </div>
</div>"""

path = BASE + 'sanctions.html'
with open(path) as f: h = f.read()

# Fix the 23 persons count to 35
h = h.replace('<div class="stat-val">23</div>\n        <div class="stat-label">персон в архиве</div>', '<div class="stat-val">35</div>\n        <div class="stat-label">персон в архиве</div>')

# Insert stats section before the table
h = h.replace('<table class="sanctions-table">', SANCTION_STATS + '\n    <table class="sanctions-table">', 1)

with open(path, 'w') as f: f.write(h)
print('✓ sanctions.html: count fixed (23→35), per-country stats added')


print('\n✓ Всё готово.')
