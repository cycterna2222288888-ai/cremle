// Generator: English dossier pages
// Run: node generate-en-dosye.js

const fs = require('fs');

const people = [
  {
    id: 'solovyov',
    num: '01',
    name: 'Vladimir Solovyov',
    born: 'October 20, 1963 — Moscow',
    channel: 'Russia-1 / VGTRK',
    show: '"Evening with Solovyov", "Moscow. Kremlin. Putin"',
    sanctions: ['EU','USA','UK','Canada','Australia','Japan','Switzerland'],
    sanctionYear: '2022',
    tagline: 'The most aggressive voice of Kremlin television',
    method: 'Rally-style aggression, personal attacks, hysterical pace. Creates a siege-fortress atmosphere — "us vs. the entire world." Owns villas on Lake Como worth €8M, seized by Italian authorities under sanctions.',
    methodTitle: 'The Method',
    stats: { year: '1963', shows: '2', sanctions: '7+' },
    bio: [
      { year: '1963–1991', title: 'Origins', text: 'Born Vladimir Solovyov in Moscow. Studies at the Institute of Steel and Alloys. Works as a journalist in the late Soviet period. Adopts a new surname (birth name: Shapiro) early in his career.' },
      { year: '1992–2004', title: 'Rise on liberal radio', text: 'Works at Radio Maximum and later Echo of Moscow. Co-hosts "We" on NTV. Builds a reputation as a sharp debate moderator — before pivoting entirely toward the state narrative.' },
      { year: '2005–2013', title: '"Evening with Solovyov" launches', text: 'Flagship talk show on Russia-1 becomes a nightly propaganda fixture. Solovyov perfects his formula: invite critics, then shout them down. Ratings soar.' },
      { year: '2014', title: 'Ukraine — the turning point', text: 'Annexation of Crimea and the Donbas war give Solovyov his defining stage. Night after night he frames the conflict as a Nazi coup backed by Washington. The show transitions from political talk to war propaganda.' },
      { year: '2022', title: 'Full-scale invasion', text: 'On the night of February 24, Solovyov opens his broadcast celebrating the "special military operation." Calls for nuclear strikes. EU, US, UK and five other jurisdictions impose personal sanctions. Italian authorities seize his Lake Como villas and yacht.' },
      { year: '2024–2025', title: 'Escalation as brand', text: 'As the war enters its third year with no end in sight, Solovyov\'s rhetoric intensifies further. He frames any peace negotiation as betrayal. His program remains in prime-time on state television every weeknight.' },
    ],
    quotes: [
      { text: '"When I hear the word \'peace\', I reach for my gun. This peace will only come with our victory."', year: '2022' },
      { text: '"Russia is the only country in the world that can genuinely turn the USA into radioactive ash."', year: '2014', attr: 'Quoting Kiselyov approvingly on air' },
      { text: '"These are not people — these are Nazis. You cannot negotiate with Nazis. You destroy them."', year: '2022' },
      { text: '"I have three children. I would rather they died free than lived under occupation."', year: '2022' },
    ],
  },
  {
    id: 'skabeeva',
    num: '02',
    name: 'Olga Skabeeva',
    born: 'December 11, 1984 — Volzhsky',
    channel: 'Russia-1',
    show: '"60 Minutes" (co-hosted with husband Evgeny Popov)',
    sanctions: ['EU','USA','UK','Canada','Australia','Japan'],
    sanctionYear: '2022',
    tagline: 'The Iron Doll of Putin\'s television',
    method: 'Cynical pressure, scripted contempt, coaching guests before air. Married to co-host Evgeny Popov — the only couple simultaneously sanctioned by six countries for joint media work.',
    methodTitle: 'The Method',
    stats: { year: '1984', shows: '1', sanctions: '6+' },
    bio: [
      { year: '1984–2006', title: 'Early career', text: 'Born in Volzhsky, Volgograd region. Studies journalism in Moscow. Begins in regional television before moving to federal channels.' },
      { year: '2007–2015', title: 'State TV correspondent', text: 'Works as a correspondent for Russia-1. Covers Crimea in 2014 with a pronounced pro-annexation line. Meets future husband Evgeny Popov on set.' },
      { year: '2016', title: '"60 Minutes" launches', text: 'Co-hosts "60 Minutes" with Popov on Russia-1. The show quickly becomes one of the most-watched propaganda talk formats: two hosts, a panel of loyalists, and a token "foreign guest" to be shouted down.' },
      { year: '2022', title: 'Third World War', text: 'On live television, Skabeeva declares: "We are openly at war with NATO. Let\'s call things by their names: the Third World War has begun." Sanctioned by EU, USA, UK, Canada, Australia and Japan.' },
      { year: '2024–2025', title: 'Permanent war footing', text: '60 Minutes airs every weekday. Skabeeva continues to frame every development — military, diplomatic or political — as a Western conspiracy against Russia. The format has not changed.' },
    ],
    quotes: [
      { text: '"We are openly at war with NATO. Let\'s call things by their names: the Third World War has begun."', year: '2022' },
      { text: '"Ukraine is not a country — it\'s a project created against Russia."', year: '2023' },
      { text: '"The Anglosaxons want to fight Russia to the last Ukrainian. That\'s not our words — that\'s their plan."', year: '2022' },
    ],
  },
  {
    id: 'kiselyov',
    num: '03',
    name: 'Dmitry Kiselyov',
    born: 'April 26, 1954 — Moscow',
    channel: 'MIA "Russia Today" / Rossiya Segodnya',
    show: '"Vesti Nedeli" (News of the Week), Director-General of Rossiya Segodnya',
    sanctions: ['EU (2014)','Canada','Switzerland'],
    sanctionYear: '2014',
    tagline: 'The first personally sanctioned propagandist — and the one who threatened nuclear war',
    method: 'Staged monumental gravity, nuclear rhetoric, the persona of "voice of the nation." First figure to be personally sanctioned by the EU — in 2014, eight years before the full-scale invasion. Frozen accounts in Switzerland. Persona non grata in Moldova.',
    methodTitle: 'The Method',
    stats: { year: '1954', shows: '1', sanctions: '3' },
    bio: [
      { year: '1954–1990', title: 'Soviet journalist', text: 'Born in Moscow. Graduates from Moscow State University journalism faculty. Works as a television journalist in the Soviet period, including a stint at Ukrainian television.' },
      { year: '1991–2008', title: 'Liberal interlude', text: 'In the 1990s, Kiselyov presents himself as a liberal journalist, covering Western culture and traveling abroad. This phase ends completely as he realigns with the Kremlin\'s trajectory.' },
      { year: '2008–2013', title: 'Chief propagandist', text: 'Becomes the anchor of "Vesti Nedeli" on Russia-1, the main Sunday evening news show. His studio monologues — mixing statistics, historical revisionism, and emotional manipulation — set the template for state television.' },
      { year: '2014', title: 'Nuclear threat on air — and sanctions', text: '"Russia is the only country that can genuinely turn the USA into radioactive ash," he states on air in March 2014, weeks after the annexation of Crimea. The EU sanctions him personally — the first such action against a Russian media figure. His Swiss accounts are frozen.' },
      { year: '2022–2025', title: 'Still at the helm', text: 'Appointed Director-General of Rossiya Segodnya (Russia Today media group) by Putin in 2013. Retains the post through the full-scale invasion. Declared persona non grata in Moldova.' },
    ],
    quotes: [
      { text: '"Russia is the only country in the world that can genuinely turn the USA into radioactive ash."', year: '2014' },
      { text: '"Russia\'s borders don\'t end anywhere."', year: '2022' },
      { text: '"Gay-propaganda is more dangerous than nuclear weapons. It kills not the body but the soul."', year: '2013' },
    ],
  },
  {
    id: 'simonyan',
    num: '04',
    name: 'Margarita Simonyan',
    born: 'April 6, 1980 — Krasnodar',
    channel: 'RT / MIA "Rossiya Segodnya"',
    show: 'Editor-in-Chief of RT and MIA "Rossiya Segodnya"',
    sanctions: ['EU','USA','UK','Canada','Australia','Japan'],
    sanctionYear: '2022',
    tagline: 'The architect of global disinformation at scale',
    method: 'Global disinformation disguised as "alternative perspective." Runs a media empire operating in 100+ countries. Married to director Tigran Keosayan, also sanctioned. RT banned across the EU; offices closed in London and Berlin.',
    methodTitle: 'The Method',
    stats: { year: '1980', shows: '3+', sanctions: '6+' },
    bio: [
      { year: '1980–2005', title: 'Prodigy journalist', text: 'Born in Krasnodar. Studies journalism. Becomes one of the youngest Kremlin pool correspondents during Putin\'s first term. Appointed founding editor-in-chief of RT (then "Russia Today") at age 25.' },
      { year: '2005–2013', title: 'Building the RT empire', text: 'Under Simonyan, RT expands from a single English-language channel into a multilingual global network (RT Arabic, RT Spanish, RT French, RT German). The model: use journalistic formats to deliver Kremlin narratives to Western audiences.' },
      { year: '2014', title: 'Crimea and the pivot', text: 'During the annexation of Crimea, Simonyan describes RT\'s role openly: "When there is a war, you don\'t want to give the enemy a microphone." RT becomes an explicit instrument of information warfare.' },
      { year: '2022', title: 'Nuclear ultimatum', text: '"Either we win — or nuclear war. There is no third option. Nuclear war is better than capitulation," she states in March 2022. Sanctioned by EU, US, UK, Canada, Australia and Japan. RT banned in the EU.' },
      { year: '2024–2025', title: 'Undeterred', text: 'Simonyan continues as editor-in-chief. RT operates via alternative distribution channels in Europe. She remains one of the most active pro-war voices on Telegram (millions of subscribers).' },
    ],
    quotes: [
      { text: '"Either we win — or nuclear war. There is no third option. Nuclear war is better than capitulation."', year: '2022' },
      { text: '"When there is a war, you don\'t want to give the enemy a microphone."', year: '2014' },
      { text: '"We are a weapon of information warfare against the West."', year: '2012', attr: 'Leaked internal speech' },
    ],
  },
  {
    id: 'popov',
    num: '05',
    name: 'Evgeny Popov',
    born: 'July 25, 1971 — Moscow',
    channel: 'Russia-1 / State Duma',
    show: '"60 Minutes" (co-hosted with wife Skabeeva), State Duma Deputy',
    sanctions: ['EU','USA','UK','Canada','Australia','Japan'],
    sanctionYear: '2022',
    tagline: 'A lawmaker by day, propagandist by night',
    method: 'Combines parliamentary mandate with daily prime-time broadcasting. A family propaganda business funded by the state. Married to co-host Olga Skabeeva — both sanctioned by six jurisdictions for the same show.',
    methodTitle: 'The Method',
    stats: { year: '1971', shows: '1', sanctions: '6+' },
    bio: [
      { year: '1971–2000', title: 'Early career', text: 'Born in Moscow. Journalism graduate. Begins working at state television in the 1990s, rising through the ranks at VGTRK.' },
      { year: '2001–2015', title: 'State TV anchor', text: 'Becomes an anchor on Russia-1. Works as a war correspondent during the 2008 war in Georgia, covering it from the Russian military\'s perspective.' },
      { year: '2016', title: '"60 Minutes" and marriage', text: 'Launches "60 Minutes" together with Skabeeva on Russia-1. The show becomes a flagship format: daily two-hour political talk with a scripted anti-Western agenda.' },
      { year: '2021', title: 'Enters parliament', text: 'Elected to the State Duma on the United Russia ticket. Becomes the only person simultaneously serving as a Duma deputy and co-hosting a daily prime-time propaganda show.' },
      { year: '2022–2025', title: 'Dual mandate', text: 'Continues both roles through the full-scale invasion. Sanctioned by six jurisdictions together with his wife. On the show: "The Anglosaxons want to fight Russia to the last Ukrainian."' },
    ],
    quotes: [
      { text: '"The Anglosaxons want to fight Russia to the last Ukrainian."', year: '2022' },
      { text: '"Ukraine is an anti-Russian project. It always was."', year: '2023' },
      { text: '"We are not at war with Ukraine. We are at war with NATO through Ukraine."', year: '2022' },
    ],
  },
  {
    id: 'sheynin',
    num: '06',
    name: 'Artem Sheynin',
    born: 'September 28, 1966 — Leningrad',
    channel: 'Channel One',
    show: '"Time Will Tell" (Vremya Pokazhet)',
    sanctions: ['EU','USA','UK'],
    sanctionYear: '2022',
    tagline: 'An Afghan War veteran turned propaganda host',
    method: 'Afghan War veteran status as moral armor. Cuts microphones of dissenting guests. Aggression performed as righteous popular anger. "I was in a real war — this is a different conversation."',
    methodTitle: 'The Method',
    stats: { year: '1966', shows: '1', sanctions: '3' },
    bio: [
      { year: '1966–1989', title: 'Military service', text: 'Born in Leningrad. Serves in the Soviet Army, including a tour in Afghanistan. The war experience becomes a permanent fixture of his public identity — moral authority through sacrifice.' },
      { year: '1990–2010', title: 'Television career', text: 'Transitions to journalism after military service. Works as a correspondent and producer at Channel One. Covers conflicts in Chechnya and other post-Soviet wars.' },
      { year: '2014', title: '"Time Will Tell" launches', text: 'Becomes the face of "Vremya Pokazhet" on Channel One — a daily political talk show with a studio audience designed to simulate popular outrage. Guests who dissent are regularly silenced or have their microphones cut.' },
      { year: '2022', title: 'Sanctioned', text: 'EU, USA and UK impose personal sanctions for systematic pro-war propaganda on state television. Sheynin does not moderate his position.' },
      { year: '2024–2025', title: 'Still broadcasting', text: '"Time Will Tell" continues its daily run on Channel One. Three years into the invasion, Sheynin\'s formula — veteran authority + manufactured rage — remains unchanged.' },
    ],
    quotes: [
      { text: '"I was in a real war. An actual war. This is a different conversation entirely."', year: '2019' },
      { text: '"These are not protesters — these are traitors. And traitors are dealt with accordingly."', year: '2022' },
      { text: '"Zelensky is a clown who was given a country. He destroyed it."', year: '2022' },
    ],
  },
  {
    id: 'tolstoy',
    num: '07',
    name: 'Pyotr Tolstoy',
    born: 'August 20, 1969 — Moscow',
    channel: 'Channel One / State Duma',
    show: 'Deputy Speaker of the State Duma, former Channel One Deputy Director-General',
    sanctions: ['EU','USA','UK','Canada'],
    sanctionYear: '2022',
    tagline: 'Great-great-grandson of Leo Tolstoy — apologist for war',
    method: 'Aristocratic surname as legitimacy. The great-great-grandson of Leo Tolstoy deploying that name in service of imperial war propaganda. Former Deputy Director-General of Channel One, now Deputy Speaker of the State Duma. Persona non grata in Latvia and Estonia.',
    methodTitle: 'The Method',
    stats: { year: '1969', shows: '1', sanctions: '4' },
    bio: [
      { year: '1969–1994', title: 'The Tolstoy name', text: 'Born into the Tolstoy family — great-great-grandson of Leo Tolstoy. Studies at Moscow State University. The family name opens doors in both literary and political circles.' },
      { year: '1994–2016', title: 'Channel One executive', text: 'Rises through Channel One to become Deputy Director-General. Hosts political programs. Becomes one of the most recognizable faces of state television\'s transition to full propaganda mode.' },
      { year: '2016', title: 'Enters parliament', text: 'Elected to the State Duma. Becomes Deputy Speaker, combining parliamentary authority with his media legacy. Advocates for restrictions on NGOs and "foreign agents."' },
      { year: '2022', title: 'Escalation — and sanctions', text: 'Calls for "denazification" of Ukraine and frames the invasion as a civilizational struggle. Sanctioned by EU, USA, UK and Canada. Declared persona non grata in Latvia and Estonia.' },
      { year: '2024–2025', title: 'Historical revisionism', text: 'Promotes the "historical Russian lands" narrative. In 2025, states that any negotiation must begin with Ukrainian recognition of Russia\'s annexations — framing surrender as precondition for talks.' },
    ],
    quotes: [
      { text: '"The Banderites are the grandchildren and great-grandchildren of those who slaughtered our grandfathers."', year: '2018' },
      { text: '"There are no \'Ukrainian people\' — there are Russians who were separated from Russia by force."', year: '2022' },
      { text: '"Donbas, Zaporizhzhia, Kherson, Kharkiv — these are Russian historical lands. This is not negotiable."', year: '2024' },
    ],
  },
  {
    id: 'norkin',
    num: '08',
    name: 'Andrey Norkin',
    born: 'November 11, 1966 — Moscow',
    channel: 'NTV',
    show: '"Meeting Place" (Mesto Vstrechi)',
    sanctions: ['EU','UK'],
    sanctionYear: '2022',
    tagline: 'A former liberal journalist who became a state inquisitor',
    method: 'Tribunal format: every guest is a defendant. Started his career as a liberal journalist at RBC before complete realignment. The contrast between his origins and current role illustrates the system\'s capacity to absorb and redirect careers.',
    methodTitle: 'The Method',
    stats: { year: '1966', shows: '1', sanctions: '2' },
    bio: [
      { year: '1966–1999', title: 'Liberal journalism', text: 'Born in Moscow. Begins career at RBC — Russia\'s main business and news channel, known in the 1990s for independent journalism. Works as a correspondent and anchor with a liberal editorial line.' },
      { year: '2000–2010', title: 'Transition to state TV', text: 'Moves to NTV after the channel\'s hostile takeover by Gazprom in 2001 strips it of its independence. Adapts to the new editorial reality.' },
      { year: '2011', title: '"Meeting Place" launches', text: 'Becomes host of "Mesto Vstrechi" — a political talk show on NTV. The format: a panel that functions as a jury, with Norkin as judge. Critics and foreign guests appear, but the verdict is predetermined.' },
      { year: '2022', title: 'Sanctions', text: 'EU and UK sanction Norkin for systematic propaganda on state television during the invasion of Ukraine. He continues broadcasting.' },
      { year: '2024–2025', title: 'War normalization', text: '"Meeting Place" continues on NTV. Three years in, Norkin\'s role is to normalize the ongoing war for a domestic audience — framing it as a necessary, inevitable, and ultimately victorious conflict.' },
    ],
    quotes: [
      { text: '"Ukraine is not a state in the classical sense. It is a project — created against Russia."', year: '2023' },
      { text: '"Every Ukrainian soldier killed is one less NATO mercenary on our border."', year: '2022' },
      { text: '"The West doesn\'t want peace. The West wants Russia destroyed."', year: '2023' },
    ],
  },
  {
    id: 'keosayan',
    num: '09',
    name: 'Tigran Keosayan',
    born: 'December 3, 1966 — Moscow',
    channel: 'RT',
    show: 'Documentary filmmaker for RT',
    sanctions: ['EU','USA','UK'],
    sanctionYear: '2022',
    tagline: 'Hollywood techniques in service of state propaganda',
    method: 'Professional film techniques deployed as propaganda weapons. Son of Soviet director Edmond Keosayan. Married to Margarita Simonyan. His documentaries use cinematic production values to give Kremlin narratives credibility with educated audiences.',
    methodTitle: 'The Method',
    stats: { year: '1966', shows: '3+', sanctions: '3' },
    bio: [
      { year: '1966–2000', title: 'Film industry', text: 'Born into a film family — son of director Edmond Keosayan. Studies at VGIK (Moscow film school). Directs feature films and television projects in the post-Soviet period.' },
      { year: '2000–2013', title: 'Mainstream director', text: 'Works across genres — comedy, drama, commercial. Builds a reputation as a technically accomplished director with broad commercial appeal.' },
      { year: '2014', title: 'Pivot to propaganda', text: 'Following the Maidan revolution, begins producing pro-Kremlin documentary content for RT and state television. His films frame Western influence in Ukraine as an existential threat to Russia.' },
      { year: '2022', title: 'RT films and sanctions', text: 'Produces war-justification documentaries for RT during the full-scale invasion. Sanctioned by EU, USA and UK. Wife Simonyan sanctioned by the same three jurisdictions.' },
      { year: '2024–2025', title: 'The RT tandem', text: 'Continues producing documentary content for RT. The Simonyan-Keosayan household functions as the command center of Russia\'s international information operations.' },
    ],
    quotes: [
      { text: '"Europe is dying. It is drowning in migrants and tolerance. What we are watching is an agony."', year: '2021' },
      { text: '"Ukraine has no culture of its own. What they call their culture is either Russian or invented."', year: '2022' },
      { text: '"I make films the way a soldier fires a rifle. It is the same war."', year: '2022' },
    ],
  },
  {
    id: 'andreyeva',
    num: '10',
    name: 'Yekaterina Andreyeva',
    born: 'March 14, 1965 — Moscow',
    channel: 'Channel One',
    show: 'News anchor since 1991',
    sanctions: ['EU','UK'],
    sanctionYear: '2022',
    tagline: 'Thirty years reading the news — three presidents, one voice',
    method: 'Neutral voice as an instrument of legitimization. An anchor who has read state news under Gorbachev, Yeltsin, and Putin — without ever using the word "war." The illusion of objectivity, perfected over three decades. The word "war" remains legally prohibited on Russian television.',
    methodTitle: 'The Method',
    stats: { year: '1965', shows: '1', sanctions: '2' },
    bio: [
      { year: '1965–1991', title: 'Journalism education', text: 'Born in Moscow. Studies journalism at Moscow State University. Begins her television career on the cusp of the Soviet collapse.' },
      { year: '1991', title: 'Channel One', text: 'Joins Channel One (then Central Television of the USSR) as a news anchor. Witnesses and reads the announcements of the August 1991 coup attempt live on air.' },
      { year: '1991–2014', title: 'Three presidents, one anchor', text: 'Andreyeva reads the evening news through the entire post-Soviet period — under Gorbachev, Yeltsin, and three Putin terms. Her consistent presence gives the state narrative an air of continuity and authority.' },
      { year: '2022', title: 'The invasion — and sanctions', text: 'On February 24, Andreyeva reads the official announcement of the "special military operation" in her characteristic measured tone. She never uses the word "war." EU and UK sanction her for systematic state propaganda.' },
      { year: '2024–2025', title: 'Still at the desk', text: 'Thirty-four years after joining Channel One, Andreyeva continues to read the evening news. The war continues. The word "war" remains unspoken.' },
    ],
    quotes: [
      { text: '"An anchor who reads lies in a neutral voice is more dangerous than one who shouts." — on Andreyeva\'s method', year: '2022', attr: 'Media analyst Yekaterina Shulman' },
      { text: '"Special military operation in Ukraine continues according to plan."', year: '2022', attr: 'Standard broadcast phrasing' },
      { text: '"Russia\'s defensive response to NATO aggression."', year: '2023', attr: 'Channel One news framing' },
    ],
  },
  {
    id: 'mamontov',
    num: '11',
    name: 'Arkady Mamontov',
    born: 'November 3, 1962 — Omsk',
    channel: 'Russia-1',
    show: '"Special Correspondent" (Spetsialny Korrespondent)',
    sanctions: ['EU','UK'],
    sanctionYear: '2022',
    tagline: 'The documentary filmmaker who primes audiences for repression',
    method: 'Pseudo-documentary format. His films about "sodomy" and "Nazis" air in the weeks before repressive legislation passes — every time. The coincidence is structural, not accidental. Mamontov provides the emotional preparation; the Duma provides the law.',
    methodTitle: 'The Method',
    stats: { year: '1962', shows: '1', sanctions: '2' },
    bio: [
      { year: '1962–1990', title: 'Early career', text: 'Born in Omsk. Studies journalism. Becomes a television correspondent in the late Soviet period, covering military and security topics.' },
      { year: '1990–2003', title: 'War correspondent', text: 'Covers both Chechen wars from the federal forces\' perspective. Wins state awards for his reporting. Builds a relationship with the security services that shapes his editorial approach.' },
      { year: '2003', title: '"Special Correspondent" launches', text: 'Begins hosting "Spetsialny Korrespondent" on Russia-1 — a documentary series that frames domestic opponents, LGBTQ+ people, and Western-linked organizations as threats to Russia.' },
      { year: '2013', title: 'The propaganda conveyor belt', text: 'His documentary on "homosexual propaganda" airs in May 2013. The State Duma passes the "gay propaganda" law in June 2013. The pattern — film, then law — repeats across multiple topics.' },
      { year: '2022–2025', title: 'War documentaries', text: 'Pivots to producing pro-war documentary content for Russia-1. EU and UK impose sanctions. He becomes one of the primary documentary voices normalizing the invasion for Russian audiences.' },
    ],
    quotes: [
      { text: '"Homosexuality is a disease. A terrible, socially dangerous disease."', year: '2014' },
      { text: '"The Maidan was organized and paid for by the CIA. We have the documents."', year: '2014' },
      { text: '"These are not civilians — these are human shields placed there by the Ukrainian military."', year: '2022' },
    ],
  },
  {
    id: 'prilepin',
    num: '12',
    name: 'Zakhar Prilepin',
    born: 'July 7, 1975 — Ryazan region',
    channel: 'Donbas / Politics',
    show: 'Writer, DPR battalion commander, co-chair of "A Just Russia — Patriots — For Truth"',
    sanctions: ['EU','USA','UK'],
    sanctionYear: '2022',
    tagline: 'The writer who went to war to prove his novels',
    method: 'A writer with a machine gun. Legitimizes war for an educated audience through literature. Intellectual nationalism. "I wrote about war. Then I went to war. Because one without the other is either cowardice or a lie."',
    methodTitle: 'The Method',
    stats: { year: '1975', shows: '2+', sanctions: '3' },
    bio: [
      { year: '1975–1996', title: 'Roots and early writing', text: 'Born in the Ryazan region. Serves in OMON (riot police) in Chechnya. Studies at Nizhny Novgorod University. Begins writing fiction with a nationalist sensibility.' },
      { year: '2000–2012', title: 'Literary recognition', text: 'Publishes "Pathologies" (2004) and "Sankya" (2006) — novels about war and nationalism that win major Russian literary prizes. Becomes associated with the National Bolshevik movement (NatBol).' },
      { year: '2014', title: 'Goes to Donbas', text: 'Joins the DPR armed formations in eastern Ukraine. Commands a battalion. Becomes the most prominent Russian intellectual to take up arms — giving the separatist cause a literary face.' },
      { year: '2022', title: 'Full-scale war — and assassination attempt', text: 'Actively supports the invasion. In May 2023, a car bomb destroys his vehicle in Nizhny Novgorod region. His driver is killed; Prilepin survives with injuries.' },
      { year: '2024–2025', title: 'Return', text: 'Recovers and returns to public life. Writes, gives interviews, and maintains his political role in "A Just Russia." His presence frames the war as a writer\'s war — intellectual, necessary, literary.' },
    ],
    quotes: [
      { text: '"I wrote about war. Then I went to war. Because one without the other is either cowardice or a lie."', year: '2017' },
      { text: '"Ukraine is not a country. It is the name of a historical mistake that must be corrected."', year: '2014' },
      { text: '"Every Russian writer who does not support this war is not a Russian writer."', year: '2022' },
    ],
  },
  {
    id: 'leontyev',
    num: '13',
    name: 'Mikhail Leontyev',
    born: 'October 6, 1958 — Moscow',
    channel: 'Channel One / Rosneft',
    show: '"Odnako" (1999–2013), Rosneft press secretary since 2013',
    sanctions: ['EU','UK'],
    sanctionYear: '2022',
    tagline: 'The intellectual commentator who merged media with the oil state',
    method: 'Intellectual commentary, not shouting. 5,000+ episodes of "Odnako" — the definitive merger of media and the corporate state. Leontyev demonstrates how state propaganda and state corporations are the same institution.',
    methodTitle: 'The Method',
    stats: { year: '1958', shows: '1', sanctions: '2' },
    bio: [
      { year: '1958–1991', title: 'Soviet journalism', text: 'Born in Moscow. Studies at Moscow State University. Works as a journalist in the Soviet period with a focus on economics and political analysis.' },
      { year: '1992–1998', title: '"Sevodnya" and liberal phase', text: 'Works at the liberal newspaper "Sevodnya" (Segodnya). Considered a market-liberal commentator in the early post-Soviet years before his pivot.' },
      { year: '1999', title: '"Odnako" launches', text: 'Begins hosting "Odnako" — a daily 3-minute editorial commentary on Channel One. Over 5,000 episodes over 14 years, making it one of the longest-running political commentary formats in Russian television history.' },
      { year: '2013', title: 'Rosneft appointment', text: 'Leaves Channel One to become press secretary of Rosneft, the state oil company headed by Igor Sechin. The transition illustrates the revolving door between state media and state corporations.' },
      { year: '2022–2025', title: 'Sanctions and retirement', text: 'Sanctioned by EU and UK. Continues in his role at Rosneft. His prolific commentary archive remains a reference document for the evolution of Kremlin messaging from 1999 to the present.' },
    ],
    quotes: [
      { text: '"The West is not a democracy — it is a kleptocracy. They steal the future from their own peoples."', year: '2020' },
      { text: '"Russia is an empire. Empires don\'t apologize for existing."', year: '2015' },
      { text: '"The liberal project in Russia failed because it was never Russian to begin with."', year: '2012' },
    ],
  },
  {
    id: 'korchevnikov',
    num: '14',
    name: 'Boris Korchevnikov',
    born: 'December 3, 1981 — Moscow',
    channel: 'Russia-1 / Spas',
    show: '"Fate of a Person" (Sudba Cheloveka), Director-General of Spas TV',
    sanctions: ['EU'],
    sanctionYear: '2022',
    tagline: 'Orthodoxy as state ideology — war as sacred duty',
    method: 'Russian Orthodox Christianity as state ideology. Religious legitimization of war. Personal cancer survivorship as a narrative of divine mission. Runs "Spas" — the Orthodox television channel — while simultaneously hosting a secular talk show on Russia-1.',
    methodTitle: 'The Method',
    stats: { year: '1981', shows: '2', sanctions: '1' },
    bio: [
      { year: '1981–2006', title: 'Early television', text: 'Born in Moscow. Studies at the Shchukin Theatre Institute. Begins his television career as an actor and presenter on youth programming.' },
      { year: '2007–2015', title: 'Cancer and conversion', text: 'Diagnosed with cancer. Survives. His public narrative of survival becomes a story of divine intervention — deepening his already strong connection to the Russian Orthodox Church. He becomes one of the most prominent Orthodox lay figures on state television.' },
      { year: '2016', title: '"Fate of a Person" and Spas', text: 'Launches "Sudba Cheloveka" on Russia-1 — a talk show about personal stories. Simultaneously becomes Director-General of Spas, the state Orthodox television channel.' },
      { year: '2022', title: 'Holy war', text: '"This war is sacred. We are fighting against the satanic element in the modern world," he states on air. Sanctioned by the EU.' },
      { year: '2024–2025', title: 'Canonization of war', text: 'Continues framing the war through the lens of Orthodox eschatology. For Korchevnikov, Russian soldiers are martyrs and the war is a spiritual cleansing.' },
    ],
    quotes: [
      { text: '"This war is sacred. We are fighting against the satanic element in the modern world."', year: '2022' },
      { text: '"A Russian soldier who dies in this war dies in a state of grace."', year: '2023' },
      { text: '"The West has chosen Satan. We have chosen God. That is the real meaning of this conflict."', year: '2022' },
    ],
  },
  {
    id: 'medinsky',
    num: '15',
    name: 'Vladimir Medinsky',
    born: 'July 18, 1970 — Smela, Ukraine',
    channel: 'Kremlin / State',
    show: 'Presidential adviser, ex-Minister of Culture 2012–2020, chief "peace" negotiator',
    sanctions: ['EU','USA','UK','Canada'],
    sanctionYear: '2022',
    tagline: 'The man who rewrote history — then negotiated surrender terms',
    method: 'Rewriting history as a state project. Culture as a weapon. His doctoral dissertation was found to contain fabrications — yet he led Russia\'s cultural policy for eight years. Born in Ukraine. Led the 2022 "peace" talks with terms designed to be rejected.',
    methodTitle: 'The Method',
    stats: { year: '1970', shows: '—', sanctions: '4' },
    bio: [
      { year: '1970–1998', title: 'Kyiv origins', text: 'Born in Smela, Ukrainian SSR. Grows up in Moscow. Studies at MGIMO (Moscow State Institute of International Relations). Later completes a doctorate in history — subsequently found by academic councils to contain systematic fabrications.' },
      { year: '1998–2012', title: 'Political career', text: 'Works in public relations and enters politics through United Russia. Becomes a Duma deputy. Develops a public profile as an author of nationalist historical revisionism ("Myths About Russia" series).' },
      { year: '2012', title: 'Minister of Culture', text: 'Appointed Minister of Culture by Putin. Over eight years, transforms cultural policy into an instrument of state ideology: film subsidies tied to patriotic narratives, monuments to Soviet figures, suppression of independent cultural institutions.' },
      { year: '2022', title: 'Lead negotiator', text: 'Heads the Russian delegation at the Belarus and Istanbul "peace" talks in February–March 2022. The terms Russia presents — Ukrainian disarmament, NATO ban, regime change — are publicly stated to be non-negotiable. The talks collapse. Sanctioned by EU, USA, UK and Canada.' },
      { year: '2024–2025', title: 'Trump-era negotiations', text: 'Returns to the negotiating table in the context of Trump\'s pressure for a settlement. Continues to represent positions incompatible with Ukrainian sovereignty.' },
    ],
    quotes: [
      { text: '"History is not what happened — it is what the people need."', year: '2016' },
      { text: '"Ukraine was always part of Russia. The separation was an accident of Soviet bureaucracy."', year: '2022' },
      { text: '"We are not at war with Ukraine. We are liberating Russia\'s historical territory."', year: '2022' },
    ],
  },
  {
    id: 'mikhalkov',
    num: '16',
    name: 'Nikita Mikhalkov',
    born: 'October 21, 1945 — Moscow',
    channel: 'Russia-1 / Russia-24',
    show: '"Besogon TV" — weekly broadcast',
    sanctions: ['EU','UK'],
    sanctionYear: '2022',
    tagline: 'An Oscar winner who became a conspiracy theorist for the Kremlin',
    method: 'Cultural authority as political shield. Uses the prestige of "Burnt by the Sun" (Academy Award 1995) to lend credibility to Kremlin narratives. "Besogon TV" episodes regularly feature Bill Gates microchip theories and anti-Western conspiracies — broadcast on state television to millions.',
    methodTitle: 'The Method',
    stats: { year: '1945', shows: '1', sanctions: '2' },
    bio: [
      { year: '1945–1970', title: 'Soviet cinema dynasty', text: 'Born into an elite Soviet cultural family (father: songwriter Sergei Mikhalkov; brother: director Andrei Konchalovsky). Studies acting and then directing at VGIK. Establishes himself as one of Soviet cinema\'s defining voices.' },
      { year: '1970–1994', title: 'International filmmaker', text: 'Directs a series of celebrated films including "Slave of Love" (1976), "Oblomov" (1980), and "Dark Eyes" (1987, Cannes Best Actor for Marcello Mastroianni). Wins the Academy Award for Best Foreign Language Film for "Burnt by the Sun" (1995).' },
      { year: '1995–2010', title: 'Political pivot', text: 'Increasingly associated with the Russian Orthodox Church and nationalist politics. Chairs the Russian Cinematographers Union. Becomes a vocal supporter of Putin\'s centralization of power and the "sovereign democracy" doctrine.' },
      { year: '2019', title: '"Besogon TV" launches', text: 'Begins producing "Besogon TV" — a weekly YouTube and state television show that mixes cultural commentary with anti-Western conspiracy theories: Bill Gates microchips in vaccines, Soros\'s agenda, "satanic" Western values.' },
      { year: '2022–2025', title: 'War support and sanctions', text: 'Publicly supports the full-scale invasion. Calls Ukrainian emigrants "misguided brothers" while advocating for confiscation of their property. Sanctioned by EU and UK.' },
    ],
    quotes: [
      { text: '"The Pfizer vaccine contains a chip. They inject you with Bill Gates through a syringe."', year: '2021' },
      { text: '"Those who left Russia — they are lost brothers. But their property should remain in Russia."', year: '2022' },
      { text: '"Western culture is a virus. More dangerous than any biological one."', year: '2023' },
    ],
  },
  {
    id: 'dugin',
    num: '17',
    name: 'Alexander Dugin',
    born: 'January 7, 1962 — Moscow',
    channel: 'Ideology / Eurasianism',
    show: 'Philosopher, founder of the Eurasian Movement, "Foundations of Geopolitics" (1997)',
    sanctions: ['EU','USA (2015)','UK','Canada'],
    sanctionYear: '2014',
    tagline: 'The philosopher who gave imperialism an academic vocabulary',
    method: 'Academic language in service of imperialism. "Foundations of Geopolitics" (1997) became a textbook in Russian military academies and shaped a generation of officers and officials. Dugin does not appear on nightly television — he provides the ideological architecture that others broadcast.',
    methodTitle: 'The Method',
    stats: { year: '1962', shows: '—', sanctions: '4' },
    bio: [
      { year: '1962–1990', title: 'Dissident fringe', text: 'Born in Moscow. Gravitates toward esoteric nationalist circles in the late Soviet period. Studies philosophy, reads widely in European fascist and traditionalist thought (Evola, Guénon, Schmitt). Becomes a founding figure of the National Bolshevik Party with Eduard Limonov.' },
      { year: '1993–2000', title: 'National Bolsheviks', text: 'Co-founds the National Bolshevik Party. The movement is fringe — but its aesthetics (black-hammer-and-sickle flag, shock tactics) attract media attention. Dugin separates and moves toward a more intellectual positioning.' },
      { year: '1997', title: '"Foundations of Geopolitics"', text: 'Publishes his landmark work, which argues that Russia must rebuild a Eurasian empire, fragment the United States by supporting separatism, and absorb Ukraine as an existential necessity. The book becomes assigned reading in Russian military and intelligence academies.' },
      { year: '2001', title: 'Eurasian Movement', text: 'Founds the International Eurasian Movement. Gains access to Kremlin circles. His ideas — stripped of their esoteric origins — enter mainstream state ideology under the name "Eurasianism."' },
      { year: '2014–2022', title: 'Donbas and sanctions', text: 'Among the first prominent figures to call for Russian military intervention in eastern Ukraine. Sanctioned by the USA in 2015, by the EU after the 2022 invasion.' },
      { year: '2022', title: 'Daughter killed', text: 'On August 20, 2022, his daughter Darya Dugina is killed when a car bomb detonates under her vehicle near Moscow. Dugin was reportedly the intended target. He continues his public activity.' },
      { year: '2024–2025', title: 'Ideological fixture', text: 'Remains one of the most cited ideological sources for Russian state positioning. His influence is diffuse — in official speeches, in military doctrine, in the rhetoric of television hosts who have never read him.' },
    ],
    quotes: [
      { text: '"Ukraine as a state has no geopolitical meaning. None at all."', year: '2014' },
      { text: '"We need to build a great Eurasia from Lisbon to Vladivostok. The Atlanticists will not allow it — so we must force them."', year: '2015' },
      { text: '"My daughter gave her life for Russia. There is only one answer to this — victory."', year: '2022' },
    ],
  },
  {
    id: 'krasovsky',
    num: '18',
    name: 'Anton Krasovsky',
    born: '1978',
    channel: 'RT',
    show: 'RT editor, Solovyov Live host',
    sanctions: ['EU (2023)'],
    sanctionYear: '2023',
    tagline: 'Documented on-air calls to drown Ukrainian children',
    method: 'Documented extremism in live broadcast. The Krasovsky case reveals the internal logic of RT: he was "suspended" by Simonyan after international outcry — then quietly reinstated. The incident demonstrates that RT\'s limits are set not by ethics but by reputational convenience.',
    methodTitle: 'What This Case Reveals',
    stats: { year: '1978', shows: '2', sanctions: '1' },
    bio: [
      { year: '1978–2012', title: 'Early career', text: 'Born 1978. Works as a journalist and television host. In 2012, publicly comes out as gay — a rare act in Russian media. Is briefly fired. Later recants and aligns entirely with state positions, including anti-LGBTQ+ legislation.' },
      { year: '2013–2021', title: 'Assimilation into state media', text: 'Works across various state and pro-Kremlin outlets. Moves to RT, where Simonyan offers a platform to provocateurs and loyalists. Builds an audience on Solovyov Live.' },
      { year: '2022 October 22', title: 'The broadcast', text: 'During a live broadcast on Solovyov Live, while discussing Soviet-era Ukrainian children\'s books, Krasovsky states: "These [Ukrainian] children should have been drowned in rivers right there." The segment is recorded and distributed internationally.' },
      { year: '2022 October', title: '"Suspension" and quiet return', text: 'Simonyan announces Krasovsky is "suspended." International coverage is extensive. Within weeks, he resumes work at RT without a formal statement of reinstatement. The suspension functions as a press release, not a consequence.' },
      { year: '2023–2025', title: 'Sanctions', text: 'The EU imposes personal sanctions in 2023. Krasovsky continues working at RT and appearing on Kremlin-aligned media.' },
    ],
    quotes: [
      { text: '"These [Ukrainian] children should have been drowned in rivers right there."', year: '2022', attr: 'Live broadcast, Solovyov Live, October 22 2022. Verified recording.' },
      { text: '"There was no Holodomor. Those who say there was are lying to destroy Russia."', year: '2022' },
      { text: '"Ukraine has no future as a state. This has been decided — by history."', year: '2023' },
    ],
  },
];

function sanTag(s) {
  return `<span class="sanction-tag">${s}</span>`;
}

function buildPage(p) {
  const ruLink = `${p.id}.html`;
  const enLink = `${p.id}-en.html`;

  const bioHtml = p.bio.map(b => `
        <div class="bio-block">
          <div class="bio-year">${b.year}</div>
          <div class="bio-title">${b.title}</div>
          <div class="bio-text">${b.text}</div>
        </div>`).join('');

  const quotesHtml = p.quotes.map(q => `
          <div class="quote-block">
            <div class="quote-text">${q.text}</div>
            <div class="quote-meta">${q.year}${q.attr ? ' · ' + q.attr : ''}</div>
          </div>`).join('');

  const sanctionsHtml = p.sanctions.map(s => sanTag(s)).join(' ');

  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${p.name} — Kremlin Voices</title>
<meta name="description" content="Dossier on ${p.name}: biography, sanctions, quotes, and methods. ${p.tagline}.">
<meta property="og:type" content="article">
<meta property="og:title" content="${p.name} — Kremlin Voices">
<meta property="og:description" content="${p.tagline}">
<meta property="og:site_name" content="Kremlin Voices">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${p.name} — Kremlin Voices">
<meta name="twitter:description" content="${p.tagline}">
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500&display=swap');
  :root { --ink:#080808; --paper:#ede8dc; --red:#8b1a1a; --red-dim:#5c1111; --light-gray:#bab3a0; --rule:#1c1c1c; --card-bg:#0e0e0e; }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:var(--ink); color:var(--paper); font-family:'Inter',sans-serif; font-weight:300; line-height:1.75; overflow-x:hidden; }
  #progress-bar { position:fixed; top:0; left:0; height:2px; width:0%; background:#8b1a1a; z-index:9999; transition:width 0.1s linear; }
  .topbar { padding:14px 60px; border-bottom:1px solid var(--rule); background:var(--ink); position:sticky; top:0; z-index:100; display:flex; justify-content:space-between; align-items:center; }
  .topbar-left a { font-size:10px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); text-decoration:none; }
  .topbar-left a:hover { opacity:0.6; }
  .topbar-right { display:flex; align-items:center; gap:20px; }
  .lang-switch { display:flex; gap:6px; font-size:9px; letter-spacing:0.2em; text-transform:uppercase; }
  .lang-switch a { color:var(--light-gray); text-decoration:none; padding:4px 8px; border:1px solid transparent; transition:all 0.2s; }
  .lang-switch a.active { color:var(--paper); border-color:var(--rule); }
  .lang-switch a:hover { color:var(--paper); }
  .report-link { font-size:9px; letter-spacing:0.2em; text-transform:uppercase; color:var(--red); text-decoration:none; border:1px solid var(--red-dim); padding:6px 14px; transition:background 0.2s; }
  .report-link:hover { background:#0d0000; }
  .masthead { padding:80px 60px 64px; border-bottom:1px solid var(--rule); display:grid; grid-template-columns:1fr 280px; gap:60px; align-items:end; }
  .masthead-eyebrow { font-size:10px; letter-spacing:0.4em; text-transform:uppercase; color:var(--red); margin-bottom:20px; }
  .masthead-num { font-family:'Playfair Display',serif; font-size:11px; letter-spacing:0.3em; color:var(--light-gray); margin-bottom:8px; }
  .masthead-name { font-family:'Playfair Display',serif; font-size:clamp(40px,5vw,80px); font-weight:700; color:var(--paper); line-height:1.0; margin-bottom:16px; }
  .masthead-role { font-family:'Playfair Display',serif; font-style:italic; font-size:clamp(14px,1.8vw,20px); color:var(--light-gray); margin-bottom:24px; }
  .masthead-born { font-size:11px; letter-spacing:0.2em; text-transform:uppercase; color:#444; }
  .masthead-stats { display:flex; flex-direction:column; gap:2px; border-left:1px solid var(--rule); padding-left:40px; }
  .stat-row { padding:20px 0; border-bottom:1px solid var(--rule); }
  .stat-row:last-child { border-bottom:none; }
  .stat-label { font-size:9px; letter-spacing:0.25em; text-transform:uppercase; color:var(--red); margin-bottom:4px; }
  .stat-val { font-family:'Playfair Display',serif; font-size:32px; font-weight:700; color:var(--paper); }
  section { border-bottom:1px solid var(--rule); }
  .section-inner { padding:80px 60px; }
  .section-label { font-size:10px; letter-spacing:0.35em; text-transform:uppercase; color:var(--red); margin-bottom:48px; display:flex; align-items:center; gap:20px; }
  .section-label::after { content:''; flex:1; height:1px; background:var(--rule); }
  .bio-block { padding:32px 0; border-bottom:1px solid #111; display:grid; grid-template-columns:160px 1fr; gap:40px; }
  .bio-block:last-child { border-bottom:none; }
  .bio-year { font-size:11px; letter-spacing:0.2em; text-transform:uppercase; color:var(--red); padding-top:4px; }
  .bio-title { font-family:'Playfair Display',serif; font-size:20px; font-weight:700; color:var(--paper); margin-bottom:12px; }
  .bio-text { font-size:14px; color:var(--light-gray); line-height:1.85; }
  .quotes-grid { display:grid; grid-template-columns:1fr 1fr; gap:2px; }
  .quote-block { background:var(--card-bg); padding:32px; border-left:3px solid var(--red-dim); }
  .quote-text { font-family:'Playfair Display',serif; font-style:italic; font-size:17px; color:var(--paper); line-height:1.6; margin-bottom:16px; }
  .quote-meta { font-size:10px; letter-spacing:0.2em; text-transform:uppercase; color:var(--light-gray); }
  .method-body { font-size:15px; color:var(--light-gray); line-height:1.9; max-width:800px; }
  .sanctions-grid { display:flex; flex-wrap:wrap; gap:8px; margin-top:24px; }
  .sanction-tag { display:inline-block; background:#1a0000; border:1px solid var(--red-dim); color:var(--red); font-size:9px; letter-spacing:0.15em; text-transform:uppercase; padding:6px 12px; }
  .warning-box { background:#1a0000; border:1px solid var(--red); padding:32px 40px; margin-top:32px; }
  .warning-label { font-size:9px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); margin-bottom:16px; }
  .warning-text { font-family:'Playfair Display',serif; font-style:italic; font-size:16px; color:var(--paper); line-height:1.6; }
  .footer { padding:48px 60px; display:flex; justify-content:space-between; align-items:center; font-size:10px; letter-spacing:0.2em; text-transform:uppercase; color:#333; }
  .footer-logo { font-family:'Playfair Display',serif; font-size:18px; font-weight:700; color:var(--red); opacity:0.5; letter-spacing:normal; text-transform:none; }
  @media(max-width:900px) {
    .masthead { grid-template-columns:1fr; padding:40px 24px; }
    .masthead-stats { border-left:none; border-top:1px solid var(--rule); padding-left:0; padding-top:32px; flex-direction:row; flex-wrap:wrap; gap:0; }
    .stat-row { border-right:1px solid var(--rule); padding:16px 24px; border-bottom:none; }
    .section-inner { padding:48px 24px; }
    .bio-block { grid-template-columns:1fr; gap:8px; }
    .quotes-grid { grid-template-columns:1fr; }
    .topbar { padding:14px 24px; }
    .footer { padding:32px 24px; flex-direction:column; gap:16px; text-align:center; }
  }
</style>
</head>
<body>
<div id="progress-bar"></div>

<div class="topbar">
  <div class="topbar-left">
    <a href="index-en.html">← All dossiers</a>
  </div>
  <div class="topbar-right">
    <div class="lang-switch">
      <a href="${ruLink}">RU</a>
      <a href="${enLink}" class="active">EN</a>
    </div>
    <a href="submit.html" class="report-link">Submit a tip</a>
  </div>
</div>

<div class="masthead">
  <div class="masthead-left">
    <div class="masthead-eyebrow">Kremlin Voices Archive</div>
    <div class="masthead-num">Dossier № ${p.num}</div>
    <h1 class="masthead-name">${p.name}</h1>
    <div class="masthead-role">${p.show}</div>
    <div class="masthead-born">Born: ${p.born}</div>
  </div>
  <div class="masthead-stats">
    <div class="stat-row">
      <div class="stat-label">Born</div>
      <div class="stat-val">${p.stats.year}</div>
    </div>
    <div class="stat-row">
      <div class="stat-label">Shows</div>
      <div class="stat-val">${p.stats.shows}</div>
    </div>
    <div class="stat-row">
      <div class="stat-label">Sanctions</div>
      <div class="stat-val">${p.stats.sanctions}</div>
    </div>
  </div>
</div>

<section>
  <div class="section-inner">
    <div class="section-label">Biography</div>
    ${bioHtml}
  </div>
</section>

<section>
  <div class="section-inner">
    <div class="section-label">Documented Quotes</div>
    <div class="quotes-grid">
      ${quotesHtml}
    </div>
  </div>
</section>

<section>
  <div class="section-inner">
    <div class="section-label">${p.methodTitle}</div>
    <div class="method-body">${p.method}</div>
  </div>
</section>

<section>
  <div class="section-inner">
    <div class="section-label">Sanctions</div>
    <div class="method-body">Sanctioned since ${p.sanctionYear}. All designations based on publicly available official sanctions lists.</div>
    <div class="sanctions-grid">
      ${sanctionsHtml}
    </div>
  </div>
</section>

<div class="footer">
  <div class="footer-logo">Kremlin Voices</div>
  <span>Data from open sources · Verified</span>
  <span><a href="index-en.html" style="color:inherit;text-decoration:none">All dossiers</a></span>
</div>

<script>
  var bar = document.getElementById('progress-bar');
  window.addEventListener('scroll', function() {
    var s = document.documentElement.scrollTop || document.body.scrollTop;
    var h = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    bar.style.width = (s / h * 100) + '%';
  });
</script>
</body>
</html>`;
}

let count = 0;
people.forEach(p => {
  const html = buildPage(p);
  const filename = `${p.id}-en.html`;
  fs.writeFileSync(filename, html);
  count++;
  console.log(`✓ ${filename}`);
});
console.log(`\nGenerated ${count} English dossier pages.`);
