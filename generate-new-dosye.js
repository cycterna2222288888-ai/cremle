// Generator: 5 new dossier pages (RU + EN)
// Run: node generate-new-dosye.js

const fs = require('fs');

const BASE = 'https://cremle.netlify.app';

const people = [
  {
    id: 'medvedev',
    num: '19',
    monogram: 'ДМ',
    photo: 'https://upload.wikimedia.org/wikipedia/commons/8/85/Dmitry_Medvedev_-_2022_%28cropped%29.jpg',
    channel: 'sovbez',
    ru: {
      name: 'Дмитрий Медведев',
      born: '14 сентября 1965, Ленинград',
      role: 'Заместитель председателя Совета Безопасности РФ',
      platform: 'Telegram / государственное ТВ (гость)',
      sanctions: 'ЕС, США, Великобритания, Канада, Австралия, Япония',
      sanctionYear: '2022',
      tagline: 'Бывший «либерал», ставший главным ядерным угрожателем России',
      subtitle: 'Экс-президент. Заместитель Путина. Голос ядерного шантажа.',
      meta: [
        ['Дата рождения', '14 сентября 1965, Ленинград'],
        ['Должность', 'Зампред Совета Безопасности РФ (с 2020)'],
        ['Ранее', 'Президент РФ (2008–2012), Премьер-министр (2012–2020)'],
        ['Санкции', 'ЕС, США, Великобритания, Канада, Австралия, Япония'],
        ['Telegram', '@medvedev — более 3 млн подписчиков'],
      ],
      stamp: 'Ядерная риторика',
      bio: [
        ['1965', 'Рождение в Ленинграде', 'Родился в семье учёных. Отец — преподаватель Ленинградского технологического института. Вырос в типичной советской интеллигентной среде. Окончил юридический факультет Ленинградского государственного университета — там же познакомился с Анатолием Собчаком.'],
        ['1990–1999', 'Работа с Путиным в Петербурге', 'В команде Собчака пересекается с Путиным. Когда Путин уходит в федеральные структуры, Медведев следует за ним. Становится частью узкого круга петербургских юристов, сделавших карьеру вместе с будущим президентом.'],
        ['2008–2012', 'Президент России', 'Западные СМИ приветствуют его как «либерала» и «модернизатора». Он говорит об инновациях, Сколково, «перезагрузке» с США. iPhone вместо КГБшного имиджа. Журнал Time ставит на обложку. Все эти годы Путин — премьер-министр и реальный центр власти.'],
        ['2012–2020', 'Премьер-министр', 'Возвращается на пост премьера после рокировки. В 2017 году Навальный публикует расследование «Он вам не Димон» — о коллекции недвижимости, яхтах и виноградниках Медведева. 20 миллионов просмотров. По всей России — протесты. Медведев отвечает: «Я работаю».'],
        ['2022', 'Перерождение: ядерные угрозы', 'После 24 февраля в Telegram начинается новый Медведев. Угрозы применить ядерное оружие, обещания «уничтожить» Украину, оскорбления западных лидеров. Кто-то считает это искренним, кто-то — исполнением роли «злого полицейского» рядом с Путиным. Результат одинаковый.'],
        ['2023–2025', 'Рекорды ядерной риторики', 'Telegram-канал Медведева становится одним из самых цитируемых источников российской эскалационной риторики в мировых СМИ. Санкции всех ключевых западных государств. Счета заморожены. Въезд запрещён.'],
      ],
      quotes: [
        ['«Россия имеет право применить ядерное оружие при угрозе самому существованию государства. А такая угроза сейчас есть.»', '2022'],
        ['«Украина в её нынешних границах — искусственное государственное образование. Она никогда не была настоящей страной.»', '2022'],
        ['«Ненавижу их. И это будет давать мне силы всю оставшуюся жизнь.»', '2023', 'О лидерах стран, поддерживающих Украину'],
        ['«Он вам не Димон». Работаю.', '2017', 'Ответ на расследование Навального'],
      ],
      method: 'Медведев — образцовый пример политика, сменившего маску. Он был нужен Кремлю как «умеренное лицо» для Запада: iPhone, Twitter, встречи с Обамой. Когда необходимость в этой роли отпала, он стал голосом максимальной эскалации. Его Telegram-канал функционирует как инструмент намеренного запугивания — каждый новый пост про ядерное оружие попадает в мировые заголовки и создаёт психологическое давление без фактических действий.',
      sanctions_text: 'Личные санкции введены ЕС, США, Великобританией, Канадой, Австралией и Японией. Заморожены зарубежные активы. Запрет на въезд в страны ЕС и G7. В списках OFAC (США) и аналогичных реестрах Евросоюза с 2022 года.',
    },
    en: {
      name: 'Dmitry Medvedev',
      born: 'September 14, 1965 — Leningrad',
      role: 'Deputy Chairman of the Security Council of Russia',
      platform: 'Telegram / state TV (guest appearances)',
      sanctions: 'EU, USA, UK, Canada, Australia, Japan',
      sanctionYear: '2022',
      tagline: 'Former "liberal", now Russia\'s chief nuclear threatener',
      subtitle: 'Ex-President. Putin\'s Deputy. Voice of nuclear blackmail.',
      meta: [
        ['Born', 'September 14, 1965, Leningrad'],
        ['Position', 'Deputy Chair, Security Council (since 2020)'],
        ['Previously', 'President of Russia (2008–2012), Prime Minister (2012–2020)'],
        ['Sanctions', 'EU, USA, UK, Canada, Australia, Japan'],
        ['Telegram', '@medvedev — over 3 million subscribers'],
      ],
      stamp: 'Nuclear rhetoric',
      bio: [
        ['1965', 'Born in Leningrad', 'Born to a family of academics. His father taught at the Leningrad Technological Institute. He studied law at Leningrad State University — where he first crossed paths with Anatoly Sobchak.'],
        ['1990–1999', 'Working with Putin in St. Petersburg', 'On Sobchak\'s team, he works alongside Putin. When Putin moves to federal structures, Medvedev follows. He becomes part of the tight circle of St. Petersburg lawyers who rise together with the future president.'],
        ['2008–2012', 'President of Russia', 'Western media hail him as a "liberal" and "modernizer." He talks about innovation, Skolkovo, a "reset" with the US. An iPhone instead of a KGB image. Time magazine puts him on the cover. Throughout these years, Putin is Prime Minister and the real center of power.'],
        ['2012–2020', 'Prime Minister', 'Returns as Prime Minister after the power swap. In 2017 Navalny publishes "He\'s Not Dimon" — exposing Medvedev\'s real-estate empire, yachts, and vineyards. 20 million views. Protests across Russia. Medvedev responds: "I\'m working."'],
        ['2022', 'Rebirth: nuclear threats', 'After February 24, a new Medvedev emerges on Telegram. Threats to use nuclear weapons, promises to "destroy" Ukraine, insults directed at Western leaders. Some call it sincere; others call it "bad cop" theater beside Putin. The effect is the same.'],
        ['2023–2025', 'Record escalation rhetoric', 'Medvedev\'s Telegram channel becomes one of the most-cited sources of Russian escalation rhetoric in global media. Sanctioned by all major Western states. Accounts frozen. Travel banned.'],
      ],
      quotes: [
        ['"Russia has the right to use nuclear weapons if the very existence of the state is threatened. And such a threat now exists."', '2022'],
        ['"Ukraine within its current borders is an artificial state formation. It was never a real country."', '2022'],
        ['"I hate them. And this will give me strength for the rest of my life."', '2023', 'On leaders of countries supporting Ukraine'],
        ['"He\'s Not Dimon." I\'m working.', '2017', 'His response to Navalny\'s investigation'],
      ],
      method: 'Medvedev is a textbook example of a politician who switched masks. The Kremlin needed him as a "moderate face" for the West: iPhone, Twitter, meetings with Obama. When that role was no longer required, he became the voice of maximum escalation. His Telegram channel functions as a tool of deliberate intimidation — each new post about nuclear weapons makes global headlines and creates psychological pressure without actual action.',
      sanctions_text: 'Personal sanctions imposed by the EU, USA, UK, Canada, Australia, and Japan. Foreign assets frozen. Entry banned to EU and G7 countries. On OFAC (USA) and equivalent EU registers since 2022.',
    },
  },
  {
    id: 'kadyrov',
    num: '20',
    monogram: 'РК',
    photo: 'https://upload.wikimedia.org/wikipedia/commons/f/f7/Kadyrov_Ramzan.jpg',
    channel: 'rt',
    ru: {
      name: 'Рамзан Кадыров',
      born: '5 октября 1976, Центорой, Чечня',
      role: 'Глава Чеченской Республики',
      platform: 'Telegram / TikTok / Россия-1',
      sanctions: 'США (2020), ЕС (2023)',
      sanctionYear: '2020',
      tagline: 'Глава Чечни, военный блогер и инструмент Кремля',
      subtitle: 'Полевой командир. Губернатор. Главный TikTok-пропагандист войны.',
      meta: [
        ['Дата рождения', '5 октября 1976, Центорой, Чечня'],
        ['Должность', 'Глава Чеченской Республики (с 2007)'],
        ['Отец', 'Ахмат Кадыров — убит в 2004 году'],
        ['Санкции', 'США — Акт Магнитского (2020), ЕС (2023)'],
        ['Соцсети', 'Telegram 3+ млн, TikTok 1+ млн подписчиков'],
      ],
      stamp: 'Силовая пропаганда',
      bio: [
        ['1976', 'Рождение в Центорой', 'Родился в семье Ахмата Кадырова — религиозного деятеля и командира сепаратистов. Рос в условиях межвоенного Грозного. Первую чеченскую войну встретил подростком на стороне сепаратистов.'],
        ['1994–1999', 'На стороне сепаратистов', 'Участвует в Первой чеченской войне на стороне боевиков. Его отец постепенно меняет позицию — находит общий язык с Москвой. Семья Кадыровых становится ключевым посредником между Кремлём и Чечнёй.'],
        ['2000', 'Переход на сторону Москвы', 'Во время Второй чеченской войны Ахмат Кадыров открыто переходит на сторону федеральных сил. Рамзан следует за отцом. Путин назначает Ахмата главой администрации Чечни.'],
        ['2004', 'Смерть отца — начало единоличной власти', 'Ахмат Кадыров убит взрывом на стадионе в Грозном. Рамзану 27 лет. Он возглавляет силовые структуры республики, методично устраняя конкурентов. Правозащитники фиксируют сотни случаев пыток и насильственных исчезновений.'],
        ['2007', 'Президент Чечни', 'В 23 года становится слишком молодым по конституции. Ждёт совершеннолетия, затем назначается Путиным. Строит культ личности: портреты в каждом учреждении, «кадыровцы» — личная армия.'],
        ['2022', 'Война в Украине: шоу и пропаганда', 'Отправляет чеченские батальоны «Ахмат» в Украину. Telegram-канал превращается в ежедневный военный репортаж: видео с бойцами, угрозы, молитвы. Западные эксперты указывают на расхождение между заявлениями и реальным участием в боях.'],
      ],
      quotes: [
        ['«Я готов выполнить любой приказ Путина, даже если он прикажет мне умереть.»', '2022'],
        ['«Мы зачистим Украину от нацистов. Это наш долг перед Аллахом и Россией.»', '2022'],
        ['«Кто против Кадырова — тот против Путина. Кто против Путина — тот против Аллаха.»', '2023'],
      ],
      method: 'Кадыров строит образ «верного вассала» — абсолютно лояльного, готового к любой жестокости. Его пропаганда направлена внутрь: на Чечню и на российскую аудиторию, которой он демонстрирует «боевой дух» и преданность Путину. Telegram-канал — личное медиа-оружие: видео с намазом, тренировками, угрозами. Эффективная смесь исламского образа, воинской эстетики и личной преданности лидеру.',
      sanctions_text: 'Внесён в санкционный список США по Акту Магнитского в 2020 году за причастность к грубым нарушениям прав человека. В 2023 году Евросоюз ввёл персональные санкции в связи с войной в Украине.',
    },
    en: {
      name: 'Ramzan Kadyrov',
      born: 'October 5, 1976 — Tsentoroy, Chechnya',
      role: 'Head of the Chechen Republic',
      platform: 'Telegram / TikTok / Russia-1',
      sanctions: 'USA (2020 Magnitsky), EU (2023)',
      sanctionYear: '2020',
      tagline: 'Chechen warlord-turned-governor and Kremlin propaganda instrument',
      subtitle: 'Warlord. Governor. Chief TikTok propagandist of the war.',
      meta: [
        ['Born', 'October 5, 1976, Tsentoroy, Chechnya'],
        ['Position', 'Head of the Chechen Republic (since 2007)'],
        ['Father', 'Akhmad Kadyrov — assassinated 2004'],
        ['Sanctions', 'USA — Magnitsky Act (2020), EU (2023)'],
        ['Social media', 'Telegram 3M+, TikTok 1M+ followers'],
      ],
      stamp: 'Coercive propaganda',
      bio: [
        ['1976', 'Born in Tsentoroy', 'Born into the family of Akhmad Kadyrov — a religious leader and separatist commander. Grew up in inter-war Grozny. He was a teenager fighting on the separatist side during the First Chechen War.'],
        ['1994–1999', 'Fighting for the separatists', 'Participates in the First Chechen War alongside militants. His father gradually changes position, finding common ground with Moscow. The Kadyrov family becomes the key broker between the Kremlin and Chechnya.'],
        ['2000', 'Switching sides to Moscow', 'During the Second Chechen War, Akhmad Kadyrov openly switches to the federal side. Ramzan follows his father. Putin appoints Akhmad head of the Chechen administration.'],
        ['2004', 'Father\'s death — absolute power begins', 'Akhmad Kadyrov is killed by a bomb at a Grozny stadium. Ramzan is 27. He takes control of the republic\'s security forces, systematically eliminating rivals. Human rights groups document hundreds of cases of torture and forced disappearances.'],
        ['2007', 'President of Chechnya', 'Too young under the constitution at 23. Waits, then is appointed by Putin. Builds a personality cult: portraits in every institution, the "Kadyrovtsy" — his personal army.'],
        ['2022', 'War in Ukraine: show and propaganda', 'Sends Chechen "Akhmat" battalions to Ukraine. His Telegram channel becomes a daily war broadcast: videos with fighters, threats, prayers. Western analysts note significant gaps between his claims and actual battlefield involvement.'],
      ],
      quotes: [
        ['"I am ready to fulfil any order from Putin, even if he orders me to die."', '2022'],
        ['"We will cleanse Ukraine of Nazis. This is our duty before Allah and Russia."', '2022'],
        ['"Anyone against Kadyrov is against Putin. Anyone against Putin is against Allah."', '2023'],
      ],
      method: 'Kadyrov builds the image of the "loyal vassal" — absolutely obedient, ready for any brutality. His propaganda is directed inward: at Chechnya and at Russian audiences, to whom he demonstrates "fighting spirit" and devotion to Putin. His Telegram channel is a personal media weapon: videos of prayer, training, threats. An effective mix of Islamic imagery, military aesthetics, and personal loyalty to the leader.',
      sanctions_text: 'Added to the US Magnitsky Act sanctions list in 2020 for involvement in gross human rights violations. In 2023, the European Union introduced personal sanctions in connection with the war in Ukraine.',
    },
  },
  {
    id: 'malofeev',
    num: '21',
    monogram: 'КМ',
    photo: 'https://upload.wikimedia.org/wikipedia/commons/b/b3/Konstantin_Malofeev_%282022%29.jpg',
    channel: 'vlast',
    ru: {
      name: 'Константин Малофеев',
      born: '3 марта 1974, Пущино, Московская область',
      role: 'Владелец Царьград ТВ, основатель фонда «Василий Великий»',
      platform: 'Царьград ТВ',
      sanctions: 'ЕС (2014), США (2014), Великобритания, Канада',
      sanctionYear: '2014',
      tagline: '«Православный олигарх» — финансист сепаратизма и создатель идеологического ТВ',
      subtitle: 'Банкир. Православный активист. Архитектор Царьграда.',
      meta: [
        ['Дата рождения', '3 марта 1974, Пущино'],
        ['Организации', 'Marshall Capital Partners, фонд «Василий Великий», Царьград ТВ'],
        ['Санкции', 'ЕС и США с 2014 года — за финансирование сепаратистов'],
        ['Идеология', 'Православный монархизм, «Русский мир», антиглобализм'],
        ['Связи', 'Игорь Гиркин («Стрелков»), Сергей Глазьев'],
      ],
      stamp: 'Идеологический спонсор',
      bio: [
        ['1974', 'Рождение в Пущино', 'Родился в научном городке Пущино Московской области. Отец — учёный. Окончил юридический факультет МГУ. Быстро нашёл место в постсоветском финансовом мире.'],
        ['1990–2000е', 'Marshall Capital Partners', 'Основал частный инвестиционный фонд Marshall Capital Partners. Работал с крупными телекоммуникационными компаниями — в частности, с «Ростелекомом». Стал богатым человеком стандартным для 2000-х путём.'],
        ['2011', 'Фонд «Василий Великий»', 'Основал благотворительный фонд имени Василия Великого — официально для поддержки православного образования. Фактически — центр продвижения «православной цивилизации» как альтернативы западному либерализму.'],
        ['2013–2014', 'Царьград ТВ и Донбасс', 'Запускает телеканал Царьград — православный консервативный вещатель. Одновременно финансирует сепаратистские структуры в Донбассе. Его имя связывают с вербовкой добровольцев и поставками снаряжения отрядам Гиркина.'],
        ['2014', 'Санкции ЕС и США', 'Брюссель и Вашингтон вводят персональные санкции — за финансирование дестабилизации востока Украины. Первый крупный православный консерватор, попавший под западные ограничения. Активы заморожены.'],
        ['2022–2025', 'Идеологическое лицо войны', 'Царьград ТВ становится одним из главных рупоров «Русского мира» и оправдания войны с позиций православного национализма. Малофеев — частый гость государственных ток-шоу.'],
      ],
      quotes: [
        ['«Россия — это Третий Рим. У нас есть миссия: спасти мир от западной цивилизации смерти.»', '2022'],
        ['«Мы воюем не с Украиной. Мы воюем с сатанизмом, который пришёл с Запада.»', '2022'],
        ['«Либерализм — это идеология дьявола. Православный государственник обязан с ним бороться.»', '2019'],
      ],
      method: 'Малофеев — редкий тип: идеологический предприниматель. Он создаёт инфраструктуру: телеканал, фонды, связи с церковью и силовыми структурами. Царьград ТВ заполняет нишу аудитории, которую не охватывают Соловьёв и Киселёв — глубоко религиозных консерваторов, для которых война — не политическая, а духовная необходимость.',
      sanctions_text: 'Под санкциями ЕС и США с 2014 года — за финансирование и организационную поддержку сепаратистских формирований на востоке Украины. Великобритания и Канада присоединились позже. Европейские активы заморожены.',
    },
    en: {
      name: 'Konstantin Malofeev',
      born: 'March 3, 1974 — Pushchino, Moscow Oblast',
      role: 'Owner of Tsargrad TV, founder of St. Basil the Great Foundation',
      platform: 'Tsargrad TV',
      sanctions: 'EU (2014), USA (2014), UK, Canada',
      sanctionYear: '2014',
      tagline: '"The Orthodox Oligarch" — financier of separatism and creator of ideological TV',
      subtitle: 'Banker. Orthodox activist. Architect of Tsargrad.',
      meta: [
        ['Born', 'March 3, 1974, Pushchino'],
        ['Organizations', 'Marshall Capital Partners, St. Basil Foundation, Tsargrad TV'],
        ['Sanctions', 'EU and USA since 2014 — for financing separatists'],
        ['Ideology', 'Orthodox monarchism, "Russian World", anti-globalism'],
        ['Connections', 'Igor Girkin ("Strelkov"), Sergei Glazyev'],
      ],
      stamp: 'Ideological sponsor',
      bio: [
        ['1974', 'Born in Pushchino', 'Born in the science town of Pushchino, Moscow Oblast. Father was a scientist. Graduated from Moscow State University law faculty. Quickly found his footing in the post-Soviet financial world.'],
        ['1990–2000s', 'Marshall Capital Partners', 'Founded the private investment fund Marshall Capital Partners. Worked with major telecommunications companies, including Rostelecom. Built his wealth through the standard early-2000s Russian path.'],
        ['2011', 'St. Basil the Great Foundation', 'Founded the St. Basil the Great charitable foundation — officially to support Orthodox education. In practice, a hub for promoting "Orthodox civilization" as an alternative to Western liberalism.'],
        ['2013–2014', 'Tsargrad TV and Donbas', 'Launches Tsargrad — an Orthodox conservative broadcaster. Simultaneously funds separatist structures in the Donbas. His name is linked to recruiting volunteers and supplying equipment to Girkin\'s units.'],
        ['2014', 'EU and US sanctions', 'Brussels and Washington impose personal sanctions for financing the destabilization of eastern Ukraine. The first major Orthodox conservative to face Western restrictions. Assets frozen.'],
        ['2022–2025', 'Ideological face of the war', 'Tsargrad TV becomes one of the main mouthpieces of the "Russian World" and justifications for war from an Orthodox nationalist perspective. Malofeev is a frequent guest on state talk shows.'],
      ],
      quotes: [
        ['"Russia is the Third Rome. We have a mission: to save the world from Western civilization of death."', '2022'],
        ['"We are not at war with Ukraine. We are at war with Satanism that came from the West."', '2022'],
        ['"Liberalism is the ideology of the devil. An Orthodox statesman is obligated to fight it."', '2019'],
      ],
      method: 'Malofeev is a rare type: an ideological entrepreneur. He builds infrastructure — a TV channel, foundations, connections to the church and security services. Tsargrad TV fills a niche that Solovyov and Kiselyov don\'t reach: deeply religious conservatives for whom the war is not political but a spiritual necessity.',
      sanctions_text: 'Under EU and US sanctions since 2014 — for financing and organizational support of separatist formations in eastern Ukraine. The UK and Canada joined later. European assets are frozen.',
    },
  },
  {
    id: 'nikonov',
    num: '22',
    monogram: 'ВН',
    photo: 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Vyacheslav_Nikonov_2019.jpg',
    channel: 'perviy',
    ru: {
      name: 'Вячеслав Никонов',
      born: '5 июня 1956, Москва',
      role: 'Депутат Государственной Думы, ведущий «Большой игры» на Первом канале',
      platform: 'Первый канал',
      sanctions: 'ЕС (2022), Великобритания (2022)',
      sanctionYear: '2022',
      tagline: 'Внук Молотова — с фамилией деда в кармане и его методами на экране',
      subtitle: 'Историк. Депутат. Ведущий. Внук архитектора пакта Молотова–Риббентропа.',
      meta: [
        ['Дата рождения', '5 июня 1956, Москва'],
        ['Программа', '«Большая игра» — Первый канал'],
        ['Должности', 'Депутат ГД, декан ФГУ МГУ, председатель «Русского мира»'],
        ['Дед', 'Вячеслав Михайлович Молотов — нарком иностранных дел СССР'],
        ['Санкции', 'ЕС и Великобритания, 2022'],
      ],
      stamp: 'Академическая пропаганда',
      bio: [
        ['1956', 'Рождение в Москве', 'Внук Вячеслава Молотова — одного из ключевых архитекторов советской внешней политики. В семье — история как живая традиция. Окончил исторический факультет МГУ, аспирантуру, стал кандидатом исторических наук.'],
        ['1980–1990е', 'Консультант и политолог', 'Работал в аппарате ЦК КПСС, затем консультировал различные политические структуры в 1990-х. Прошёл путь от советского аппаратчика до «независимого политолога» с нужными связями.'],
        ['2000е', 'Фонд «Политика» и академический статус', 'Основал фонд «Политика» — аналитический центр с пропутинским уклоном. Декан факультета государственного управления МГУ. Обложка научного авторитета при политической ангажированности.'],
        ['2011', 'Государственная Дума', 'Избран депутатом от «Единой России». Возглавил комитет по образованию и науке. Совмещает мандат с телевизионной карьерой.'],
        ['2014', 'Присоединение Крыма — обоснование историка', 'Активно поддерживает аннексию Крыма, используя исторические аргументы. Его дед подписывал пакт Молотова–Риббентропа, перекраивавший границы Европы. Никонов перекраивает их нарративом.'],
        ['2022', '«Большая игра» как трибуна войны', 'Программа на Первом канале превращается в витрину официальной позиции по войне — в академической упаковке. Санкции ЕС и Великобритании. Въезд запрещён.'],
      ],
      quotes: [
        ['«Украина — это историческое недоразумение. Эта территория всегда была частью русского мира.»', '2022'],
        ['«Западная цивилизация находится в глубоком упадке. Россия — это будущее.»', '2023'],
        ['«Специальная военная операция — это не агрессия. Это историческая необходимость.»', '2022'],
      ],
      method: 'Никонов даёт пропаганде академическую оболочку. Его формат — не крик Соловьёва, а спокойный «разбор» с апелляцией к истории, архивам, прецедентам. Ссылка на деда работает в обе стороны: легитимизирует его авторитет и косвенно нормализует практику перекройки границ как часть «большой истории».',
      sanctions_text: 'Персональные санкции ЕС с марта 2022 года — за распространение государственной пропаганды и поддержку войны против Украины. Великобритания ввела аналогичные ограничения в том же году. Активы заморожены, въезд запрещён.',
    },
    en: {
      name: 'Vyacheslav Nikonov',
      born: 'June 5, 1956 — Moscow',
      role: 'State Duma deputy, host of "The Great Game" on Channel One',
      platform: 'Channel One',
      sanctions: 'EU (2022), UK (2022)',
      sanctionYear: '2022',
      tagline: 'Molotov\'s grandson — with his grandfather\'s legacy and methods on screen',
      subtitle: 'Historian. Deputy. Host. Grandson of the architect of the Molotov–Ribbentrop Pact.',
      meta: [
        ['Born', 'June 5, 1956, Moscow'],
        ['Programme', '"The Great Game" — Channel One'],
        ['Positions', 'State Duma Deputy, Dean of MSU faculty, chair of "Russky Mir"'],
        ['Grandfather', 'Vyacheslav Molotov — Soviet Foreign Minister'],
        ['Sanctions', 'EU and UK, 2022'],
      ],
      stamp: 'Academic propaganda',
      bio: [
        ['1956', 'Born in Moscow', 'Grandson of Vyacheslav Molotov — one of the key architects of Soviet foreign policy. History was a living tradition in his family. Graduated from Moscow State University\'s history faculty, completed postgraduate studies, became a candidate of historical sciences.'],
        ['1980–1990s', 'Consultant and political analyst', 'Worked in the CPSU Central Committee apparatus, then advised various political structures in the 1990s. Traveled the path from Soviet apparatchik to "independent political analyst" with the right connections.'],
        ['2000s', '"Politika" Foundation and academic status', 'Founded the "Politika" Foundation — an analytical center with a pro-Putin slant. Dean of the Faculty of Public Administration at Moscow State University. The cover of academic authority over political engagement.'],
        ['2011', 'State Duma', 'Elected as a deputy from United Russia. Chaired the Committee on Education and Science. Combines his mandate with a television career.'],
        ['2014', 'Crimea annexation — historian\'s justification', 'Actively supports the annexation of Crimea using historical arguments. His grandfather signed the Molotov–Ribbentrop Pact that redrawn Europe\'s borders. Nikonov redraws them through narrative.'],
        ['2022', '"The Great Game" as a war platform', 'The Channel One programme becomes a showcase for the official position on the war — in academic packaging. EU and UK sanctions. Entry banned.'],
      ],
      quotes: [
        ['"Ukraine is a historical misunderstanding. This territory has always been part of the Russian world."', '2022'],
        ['"Western civilization is in deep decline. Russia is the future."', '2023'],
        ['"The special military operation is not aggression. It is a historical necessity."', '2022'],
      ],
      method: 'Nikonov gives propaganda an academic shell. His format is not Solovyov\'s screaming, but a calm "analysis" with appeals to history, archives, precedents. The reference to his grandfather works both ways: it legitimizes his authority and indirectly normalizes the practice of redrawing borders as part of "the grand sweep of history."',
      sanctions_text: 'EU personal sanctions since March 2022 — for spreading state propaganda and supporting the war against Ukraine. The UK introduced equivalent restrictions the same year. Assets frozen, entry banned.',
    },
  },
  {
    id: 'poddubny',
    num: '23',
    monogram: 'ЕП',
    photo: 'https://upload.wikimedia.org/wikipedia/commons/9/9b/Evgeny_Poddubny_2022.jpg',
    channel: 'rossiya1',
    ru: {
      name: 'Евгений Поддубный',
      born: '14 июля 1983, Ставрополь',
      role: 'Военный корреспондент ВГТРК, депутат Государственной Думы',
      platform: 'Россия-1 / ВГТРК',
      sanctions: 'ЕС (2022), Великобритания, Канада',
      sanctionYear: '2022',
      tagline: 'Лицо «фронтовой правды» ВГТРК — в Ливии, Сирии, на Донбассе и в Думе',
      subtitle: 'Военный корреспондент. Депутат. Лицо войны на государственном ТВ.',
      meta: [
        ['Дата рождения', '14 июля 1983, Ставрополь'],
        ['Канал', 'Россия-1 / ВГТРК'],
        ['Должность', 'Депутат Государственной Думы (с 2021, Единая Россия)'],
        ['Конфликты', 'Ливия, Сирия, Донбасс (с 2014), Украина (с 2022)'],
        ['Санкции', 'ЕС, Великобритания, Канада'],
      ],
      stamp: 'Фронтовая пропаганда',
      bio: [
        ['1983', 'Рождение в Ставрополе', 'Родился в Ставрополе. Журналистское образование. Приходит на ВГТРК в середине 2000-х и быстро специализируется на конфликтных зонах.'],
        ['2011–2013', 'Ливия и Сирия', 'Становится одним из главных военных корреспондентов ВГТРК в ходе «Арабской весны». Репортажи из Ливии и Сирии — с российским взглядом на события. Формирует образ «русского военкора», который не боится передовой.'],
        ['2014', 'Донбасс — рождение «военкора №1»', 'С первых дней конфликта работает в зоне боевых действий на Донбассе. Его репортажи — среди самых просматриваемых на ВГТРК. Создаёт устойчивый образ: мужественный военкор против «нацистов» и «хаоса». Становится знаменем государственного ТВ.'],
        ['2018–2021', 'Международные конфликты', 'Продолжает работать в горячих точках — Сирия, Ливия, снова Донбасс. Лауреат государственных наград. В 2021 году избирается в Государственную Думу по партийному списку «Единой России».'],
        ['2022', 'Война в Украине', 'С первых дней полномасштабного вторжения работает на передовой. Его репортажи — главная «картинка с фронта» для российской аудитории. Санкции ЕС, Великобритании и Канады.'],
        ['2023–2025', 'Депутат и военкор одновременно', 'Совмещает мандат депутата с полевой работой. Использует думскую трибуну для легитимизации войны. Один из самых узнаваемых людей государственного телевидения среди молодёжной аудитории.'],
      ],
      quotes: [
        ['«Здесь, на Донбассе, решается судьба России. И я обязан это показать.»', '2022'],
        ['«Нам говорят: вы пропагандисты. Но мы просто рассказываем то, что видим. А видим мы — зверства.»', '2022'],
        ['«Военный корреспондент — это не профессия. Это призвание.»', '2019'],
      ],
      method: 'Поддубный работает через образ, а не идеологию. Он не кричит в студии — он стоит под обстрелом. Этот формат работает на аудиторию, которая устала от политических ток-шоу: кажется, что он просто «показывает как есть». На деле — каждый репортаж вписан в государственный нарратив: враг определён заранее, сочувствие направлено заранее, вывод известен заранее.',
      sanctions_text: 'Персональные санкции ЕС с 2022 года — за распространение дезинформации и государственной пропаганды о войне в Украине. Великобритания и Канада ввели аналогичные ограничения. Въезд запрещён.',
    },
    en: {
      name: 'Yevgeny Poddubny',
      born: 'July 14, 1983 — Stavropol',
      role: 'War correspondent for VGTRK, State Duma deputy',
      platform: 'Russia-1 / VGTRK',
      sanctions: 'EU (2022), UK, Canada',
      sanctionYear: '2022',
      tagline: 'VGTRK\'s face of "frontline truth" — in Libya, Syria, Donbas, and the Duma',
      subtitle: 'War correspondent. Deputy. The face of war on state TV.',
      meta: [
        ['Born', 'July 14, 1983, Stavropol'],
        ['Channel', 'Russia-1 / VGTRK'],
        ['Position', 'State Duma Deputy (since 2021, United Russia)'],
        ['Conflicts', 'Libya, Syria, Donbas (since 2014), Ukraine (since 2022)'],
        ['Sanctions', 'EU, UK, Canada'],
      ],
      stamp: 'Frontline propaganda',
      bio: [
        ['1983', 'Born in Stavropol', 'Born in Stavropol. Studied journalism. Joins VGTRK in the mid-2000s and quickly specializes in conflict zones.'],
        ['2011–2013', 'Libya and Syria', 'Becomes one of VGTRK\'s leading war correspondents during the Arab Spring. Reports from Libya and Syria — with a Russian perspective on events. Forms the image of the "Russian war correspondent" who fears no frontline.'],
        ['2014', 'Donbas — birth of "war correspondent #1"', 'Works in the combat zone in the Donbas from the first days of the conflict. His reports are among the most-watched on VGTRK. Creates an enduring image: a brave war correspondent against "Nazis" and "chaos." Becomes the flagship of state television.'],
        ['2018–2021', 'International conflicts', 'Continues working in conflict zones — Syria, Libya, then Donbas again. Recipient of state awards. In 2021 is elected to the State Duma on United Russia\'s party list.'],
        ['2022', 'War in Ukraine', 'Works at the frontline from the first days of the full-scale invasion. His reports are the main "pictures from the front" for Russian audiences. EU, UK and Canadian sanctions.'],
        ['2023–2025', 'Deputy and correspondent simultaneously', 'Combines his parliamentary mandate with field reporting. Uses the Duma platform to legitimize the war. One of the most recognizable faces of state television among younger audiences.'],
      ],
      quotes: [
        ['"Here in the Donbas, Russia\'s fate is being decided. And I am obligated to show it."', '2022'],
        ['"They call us propagandists. But we just show what we see. And what we see — is atrocities."', '2022'],
        ['"A war correspondent is not a profession. It\'s a calling."', '2019'],
      ],
      method: 'Poddubny works through image, not ideology. He doesn\'t scream in a studio — he stands under fire. This format works for audiences tired of political talk shows: it appears he\'s simply "showing it as it is." In reality, every report is inscribed within the state narrative: the enemy is predetermined, sympathies are pre-directed, the conclusion is already known.',
      sanctions_text: 'EU personal sanctions since 2022 — for spreading disinformation and state propaganda about the war in Ukraine. The UK and Canada introduced equivalent restrictions. Entry banned.',
    },
  },
];

// Order for "next dossier" — existing last is krasovsky (18), new chain: medvedev→kadyrov→malofeev→nikonov→poddubny→solovyov
const nextMap = {
  medvedev:  { ru: ['kadyrov',  'Рамзан Кадыров',    'Военный блогер федерального масштаба'],    en: ['kadyrov',  'Ramzan Kadyrov',    'Kremlin\'s TikTok warlord'] },
  kadyrov:   { ru: ['malofeev', 'Константин Малофеев','Православный олигарх'],                   en: ['malofeev', 'Konstantin Malofeev','The Orthodox Oligarch'] },
  malofeev:  { ru: ['nikonov',  'Вячеслав Никонов',   'Внук Молотова в эфире'],                  en: ['nikonov',  'Vyacheslav Nikonov', 'Molotov\'s Grandson on Air'] },
  nikonov:   { ru: ['poddubny', 'Евгений Поддубный',  'Военкор и депутат'],                      en: ['poddubny', 'Yevgeny Poddubny',  'War Correspondent & Deputy'] },
  poddubny:  { ru: ['solovyov', 'Владимир Соловьёв',  'Голос войны'],                            en: ['solovyov', 'Vladimir Solovyov', 'The Voice of War'] },
};

function svgBackground(monogram) {
  return `<svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0">
      <defs>
        <radialGradient id="rg" cx="50%" cy="35%" r="60%">
          <stop offset="0%" stop-color="#1a0000" stop-opacity="0.8"/>
          <stop offset="100%" stop-color="#000" stop-opacity="1"/>
        </radialGradient>
      </defs>
      <rect width="100%" height="100%" fill="url(#rg)"/>
      <line x1="50%" y1="20%" x2="50%" y2="80%" stroke="#8b1a1a" stroke-width="0.5" opacity="0.4"/>
      <line x1="20%" y1="50%" x2="80%" y2="50%" stroke="#8b1a1a" stroke-width="0.5" opacity="0.4"/>
      <circle cx="50%" cy="38%" r="80" fill="none" stroke="#8b1a1a" stroke-width="0.5" opacity="0.3"/>
      <circle cx="50%" cy="38%" r="120" fill="none" stroke="#8b1a1a" stroke-width="0.5" opacity="0.15"/>
      <g opacity="0.06">
        <line x1="0" y1="10%" x2="100%" y2="10%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="20%" x2="100%" y2="20%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="30%" x2="100%" y2="30%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="40%" x2="100%" y2="40%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="50%" x2="100%" y2="50%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="60%" x2="100%" y2="60%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="70%" x2="100%" y2="70%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="80%" x2="100%" y2="80%" stroke="#c8c0b0" stroke-width="1"/>
        <line x1="0" y1="90%" x2="100%" y2="90%" stroke="#c8c0b0" stroke-width="1"/>
      </g>
      <text x="50%" y="42%" text-anchor="middle" dominant-baseline="middle"
        font-family="Georgia,serif" font-size="140" fill="#8b1a1a" opacity="0.15" font-weight="700">${monogram}</text>
    </svg>`;
}

function buildRU(p) {
  const d = p.ru;
  const next = nextMap[p.id].ru;
  const pageUrl = `${BASE}/${p.id}.html`;
  const shareText = `${d.name} — ${d.tagline}`;

  const bioHTML = d.bio.map(([year, title, text]) => `
      <div class="timeline-entry">
        <div class="timeline-year">${year}</div>
        <div class="timeline-body">
          <h3>${title}</h3>
          <p>${text}</p>
        </div>
      </div>`).join('');

  const quotesHTML = d.quotes.map(([text, year, attr]) => `
        <div class="quote-card">
          <div class="quote-text">${text}</div>
          <div class="quote-source">${year}${attr ? ' · ' + attr : ''}</div>
        </div>`).join('');

  const metaHTML = d.meta.map(([label, val]) => `
      <div class="meta-item">
        <label>${label}</label>
        <span>${val}</span>
      </div>`).join('');

  return `<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${d.name} — Досье · Голоса Кремля</title>
<meta name="description" content="${d.tagline}. Биография, цитаты, санкции.">
<meta property="og:type" content="profile">
<meta property="og:title" content="${d.name} · Голоса Кремля">
<meta property="og:description" content="${d.tagline}">
<meta property="og:site_name" content="Голоса Кремля">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<meta property="og:image" content="${BASE}/og-image.svg">
<meta name="twitter:image" content="${BASE}/og-image.svg">
<link rel="canonical" href="${BASE}/${p.id}.html">
<link rel="alternate" hreflang="ru" href="${BASE}/${p.id}.html">
<link rel="alternate" hreflang="en" href="${BASE}/${p.id}-en.html">
<link rel="alternate" hreflang="x-default" href="${BASE}/${p.id}.html">
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "${d.name}",
  "alternateName": "${p.en.name}",
  "jobTitle": "${d.role}",
  "nationality": "Russian",
  "url": "${BASE}/${p.id}.html",
  "sameAs": "${BASE}/${p.id}-en.html"
}
</script>
<!-- Analytics (Umami, no cookies) -->
<script defer src="https://cloud.umami.is/script.js" data-website-id="REPLACE_WITH_YOUR_ID"></script>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500&display=swap');
  :root { --ink:#080808; --paper:#ede8dc; --red:#8b1a1a; --red-dim:#5c1111; --light-gray:#bab3a0; --rule:#1c1c1c; --card-bg:#0e0e0e; --gray:#4a4a4a; }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:var(--ink); color:var(--paper); font-family:'Inter',sans-serif; font-weight:300; line-height:1.75; overflow-x:hidden; min-height:100vh; }
  #progress-bar { position:fixed; top:0; left:0; height:2px; width:0%; background:var(--red); z-index:999; transition:width 0.1s; }
  .topbar { padding:14px 60px; border-bottom:1px solid var(--rule); background:var(--ink); position:sticky; top:0; z-index:100; display:flex; justify-content:space-between; align-items:center; }
  .topbar-left a { font-size:10px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); text-decoration:none; }
  .topbar-left a:hover { opacity:0.6; }
  .topbar-right { display:flex; align-items:center; gap:20px; }
  .lang-switch { display:flex; border:1px solid #333; overflow:hidden; }
  .lang-switch a { font-size:9px; letter-spacing:0.2em; text-transform:uppercase; color:#888; text-decoration:none; padding:6px 12px; transition:all 0.2s; }
  .lang-switch a.active { color:var(--paper); background:#1c1c1c; }
  .lang-switch a:hover { color:var(--paper); background:#111; }
  .report-link { font-size:9px; letter-spacing:0.2em; text-transform:uppercase; color:#5c1111; text-decoration:none; border:1px solid #2a0a0a; padding:6px 14px; transition:all 0.2s; }
  .report-link:hover { color:#8b1a1a; border-color:#5c1111; }
  .hero { display:grid; grid-template-columns:1fr 420px; min-height:80vh; border-bottom:1px solid var(--rule); }
  .hero-left { padding:80px 60px; display:flex; flex-direction:column; justify-content:center; border-right:1px solid var(--rule); }
  .eyebrow { font-size:10px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); margin-bottom:32px; }
  .hero-name { font-family:'Playfair Display',serif; font-size:clamp(2.5rem,5vw,4.5rem); font-weight:400; line-height:1.05; margin-bottom:20px; }
  .hero-subtitle { font-size:14px; color:var(--light-gray); letter-spacing:0.05em; margin-bottom:40px; font-style:italic; }
  .hero-meta { display:flex; flex-direction:column; gap:0; border-top:1px solid var(--rule); }
  .meta-item { display:grid; grid-template-columns:140px 1fr; gap:16px; padding:12px 0; border-bottom:1px solid #111; }
  .meta-item label { font-size:10px; letter-spacing:0.2em; text-transform:uppercase; color:#555; }
  .meta-item span { font-size:13px; color:var(--light-gray); }
  .hero-right { position:relative; overflow:hidden; background:#050505; }
  .hero-stamp { position:absolute; bottom:24px; left:24px; font-size:9px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); border:1px solid var(--red-dim); padding:6px 12px; background:rgba(0,0,0,0.7); }
  .section { border-bottom:1px solid var(--rule); padding:80px 0; }
  .container { max-width:760px; margin:0 auto; padding:0 60px; }
  .section-header { display:flex; align-items:center; gap:20px; margin-bottom:48px; }
  .section-num { font-size:11px; letter-spacing:0.3em; color:#333; }
  .section-title { font-family:'Playfair Display',serif; font-size:1.8rem; font-weight:400; flex:1; }
  .section-title::after { content:''; display:block; height:1px; background:var(--rule); margin-top:8px; }
  .intro-text { font-size:16px; line-height:1.9; color:var(--light-gray); margin-bottom:48px; }
  .timeline { display:flex; flex-direction:column; gap:0; }
  .timeline-entry { display:grid; grid-template-columns:80px 1fr; gap:24px; padding:28px 0; border-bottom:1px solid #0f0f0f; }
  .timeline-year { font-size:11px; letter-spacing:0.2em; color:var(--red); padding-top:4px; }
  .timeline-body h3 { font-size:14px; letter-spacing:0.05em; margin-bottom:10px; color:var(--paper); }
  .timeline-body p { font-size:14px; color:#888; line-height:1.8; }
  .quotes-grid { display:grid; grid-template-columns:1fr 1fr; gap:1px; background:var(--rule); }
  .quote-card { background:var(--card-bg); padding:32px; }
  .quote-text { font-family:'Playfair Display',serif; font-size:15px; font-style:italic; line-height:1.7; margin-bottom:16px; color:var(--paper); }
  .quote-source { font-size:11px; letter-spacing:0.15em; text-transform:uppercase; color:#444; }
  .method-text { font-size:15px; line-height:1.9; color:var(--light-gray); }
  .sanctions-block { background:var(--card-bg); border:1px solid #1a0000; border-left:3px solid var(--red); padding:28px 32px; }
  .sanctions-block p { font-size:14px; color:var(--light-gray); line-height:1.8; }
  .footer { padding:48px 60px; display:flex; justify-content:space-between; align-items:center; font-size:11px; letter-spacing:0.15em; text-transform:uppercase; color:#333; }
  .footer-rule { width:1px; height:40px; background:var(--rule); }
  .next-dosye { border-top:1px solid var(--rule); padding:48px 60px; display:flex; justify-content:space-between; align-items:center; text-decoration:none; color:var(--paper); transition:background 0.2s; }
  .next-dosye:hover { background:#0a0a0a; }
  .next-dosye-label { font-size:10px; letter-spacing:0.25em; text-transform:uppercase; color:#444; margin-bottom:8px; }
  .next-dosye-name { font-family:'Playfair Display',serif; font-size:1.6rem; font-weight:400; }
  .next-dosye-title { font-size:13px; color:#666; margin-top:4px; }
  .next-dosye-arrow { font-size:2rem; color:var(--red); }
  .share-bar { border-top:1px solid var(--rule); padding:24px 60px; display:flex; align-items:center; gap:16px; }
  .share-label { font-size:10px; letter-spacing:0.2em; text-transform:uppercase; color:#444; }
  .share-btn { font-size:10px; letter-spacing:0.15em; text-transform:uppercase; text-decoration:none; padding:8px 16px; border:1px solid #222; color:#888; transition:all 0.2s; }
  .share-btn:hover { border-color:#555; color:var(--paper); }
  @media (max-width: 768px) {
    .hero { grid-template-columns:1fr; }
    .hero-right { height:300px; }
    .hero-left { padding:48px 24px; }
    .container { padding:0 24px; }
    .quotes-grid { grid-template-columns:1fr; }
    .topbar { padding:12px 20px; }
    .topbar-right { gap:10px; }
    .report-link { display:none; }
    .footer { padding:32px 24px; flex-direction:column; gap:12px; text-align:center; }
    .next-dosye { padding:32px 20px; }
    .next-dosye-name { font-size:1.2rem; }
    .share-bar { padding:20px 20px; flex-wrap:wrap; gap:10px; }
  }
  @media print {
    * { -webkit-print-color-adjust:exact; print-color-adjust:exact; }
    body { background:#fff !important; color:#000 !important; font-size:11pt; }
    .topbar,#progress-bar,.share-bar,.next-dosye,.report-link,.lang-switch { display:none !important; }
    .hero { grid-template-columns:1fr 280px !important; page-break-inside:avoid; }
    .hero-right { height:280px !important; }
    .hero-left { background:#f5f5f5 !important; padding:32px !important; }
    .hero-name { color:#000 !important; font-size:28pt !important; }
    .section { border-color:#ddd !important; padding:24px 0 !important; page-break-inside:avoid; }
    .quote-card { background:#f9f9f9 !important; border:1px solid #ddd !important; color:#000 !important; }
    @page { margin:2cm; }
  }
</style>
</head>
<body>
<div id="progress-bar"></div>
<div class="topbar">
  <div class="topbar-left"><a href="index.html">← Все досье</a></div>
  <div class="topbar-right">
    <div class="lang-switch">
      <a href="${p.id}.html" class="active">RU</a>
      <a href="${p.id}-en.html">EN</a>
    </div>
    <a href="submit.html" class="report-link">Сообщить</a>
  </div>
</div>

<div class="hero">
  <div class="hero-left">
    <div class="eyebrow">Досье · Архивный материал · 2025</div>
    <h1 class="hero-name">${d.name.replace(' ', '<br>')}</h1>
    <p class="hero-subtitle">${d.subtitle}</p>
    <div class="hero-meta">${metaHTML}
    </div>
  </div>
  <div class="hero-right">
    ${svgBackground(p.monogram)}
    <img loading="lazy" src="${p.photo}" alt="${d.name}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top center;opacity:0.45;mix-blend-mode:luminosity;" onerror="this.style.display='none'">
    <div class="hero-stamp">${d.stamp}</div>
  </div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-num">01</span>
      <h2 class="section-title">Биография</h2>
    </div>
    <p class="intro-text">${d.tagline}.</p>
    <div class="timeline">${bioHTML}
    </div>
  </div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-num">02</span>
      <h2 class="section-title">Цитаты</h2>
    </div>
  </div>
  <div class="quotes-grid">${quotesHTML}
  </div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-num">03</span>
      <h2 class="section-title">Метод</h2>
    </div>
    <p class="method-text">${d.method}</p>
  </div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-num">04</span>
      <h2 class="section-title">Санкции</h2>
    </div>
    <div class="sanctions-block">
      <p>${d.sanctions_text}</p>
    </div>
  </div>
</div>

<div class="share-bar">
  <span class="share-label">Поделиться</span>
  <a class="share-btn" href="https://twitter.com/intent/tweet?url=${pageUrl}&text=${encodeURIComponent(shareText)}" target="_blank" rel="noopener">Twitter / X</a>
  <a class="share-btn" href="https://t.me/share/url?url=${pageUrl}&text=${encodeURIComponent(shareText)}" target="_blank" rel="noopener">Telegram</a>
</div>

<a class="next-dosye" href="${next[0]}.html">
  <div>
    <div class="next-dosye-label">Следующее досье →</div>
    <div class="next-dosye-name">${next[1]}</div>
    <div class="next-dosye-title">${next[2]}</div>
  </div>
  <div class="next-dosye-arrow">→</div>
</a>

<!-- FOOTER -->
<div class="footer">
  <span>Досье составлено на основе открытых источников</span>
  <div class="footer-rule"></div>
  <span>${d.name}</span>
  <div class="footer-rule"></div>
  <span>Все факты верифицированы публикациями СМИ</span>
</div>

<script>
window.addEventListener('scroll', function() {
  var el = document.getElementById('progress-bar');
  var h = document.documentElement;
  var pct = (h.scrollTop / (h.scrollHeight - h.clientHeight)) * 100;
  el.style.width = pct + '%';
});
</script>
</body>
</html>`;
}

function buildEN(p) {
  const d = p.en;
  const next = nextMap[p.id].en;
  const pageUrl = `${BASE}/${p.id}-en.html`;
  const shareText = `${d.name} — ${d.tagline}`;

  const bioHTML = d.bio.map(([year, title, text]) => `
      <div class="timeline-entry">
        <div class="timeline-year">${year}</div>
        <div class="timeline-body">
          <h3>${title}</h3>
          <p>${text}</p>
        </div>
      </div>`).join('');

  const quotesHTML = d.quotes.map(([text, year, attr]) => `
        <div class="quote-card">
          <div class="quote-text">${text}</div>
          <div class="quote-source">${year}${attr ? ' · ' + attr : ''}</div>
        </div>`).join('');

  const metaHTML = d.meta.map(([label, val]) => `
      <div class="meta-item">
        <label>${label}</label>
        <span>${val}</span>
      </div>`).join('');

  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${d.name} — Dossier · Voices of the Kremlin</title>
<meta name="description" content="${d.tagline}. Biography, quotes, sanctions.">
<meta property="og:type" content="profile">
<meta property="og:title" content="${d.name} · Voices of the Kremlin">
<meta property="og:description" content="${d.tagline}">
<meta property="og:site_name" content="Voices of the Kremlin">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<meta property="og:image" content="${BASE}/og-image.svg">
<meta name="twitter:image" content="${BASE}/og-image.svg">
<link rel="canonical" href="${BASE}/${p.id}-en.html">
<link rel="alternate" hreflang="ru" href="${BASE}/${p.id}.html">
<link rel="alternate" hreflang="en" href="${BASE}/${p.id}-en.html">
<link rel="alternate" hreflang="x-default" href="${BASE}/${p.id}.html">
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "${d.name}",
  "alternateName": "${p.ru.name}",
  "jobTitle": "${d.role}",
  "nationality": "Russian",
  "url": "${BASE}/${p.id}-en.html",
  "sameAs": "${BASE}/${p.id}.html"
}
</script>
<!-- Analytics (Umami, no cookies) -->
<script defer src="https://cloud.umami.is/script.js" data-website-id="REPLACE_WITH_YOUR_ID"></script>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500&display=swap');
  :root { --ink:#080808; --paper:#ede8dc; --red:#8b1a1a; --red-dim:#5c1111; --light-gray:#bab3a0; --rule:#1c1c1c; --card-bg:#0e0e0e; --gray:#4a4a4a; }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:var(--ink); color:var(--paper); font-family:'Inter',sans-serif; font-weight:300; line-height:1.75; overflow-x:hidden; min-height:100vh; }
  #progress-bar { position:fixed; top:0; left:0; height:2px; width:0%; background:var(--red); z-index:999; transition:width 0.1s; }
  .topbar { padding:14px 60px; border-bottom:1px solid var(--rule); background:var(--ink); position:sticky; top:0; z-index:100; display:flex; justify-content:space-between; align-items:center; }
  .topbar-left a { font-size:10px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); text-decoration:none; }
  .topbar-left a:hover { opacity:0.6; }
  .topbar-right { display:flex; align-items:center; gap:20px; }
  .lang-switch { display:flex; border:1px solid #333; overflow:hidden; }
  .lang-switch a { font-size:9px; letter-spacing:0.2em; text-transform:uppercase; color:#888; text-decoration:none; padding:6px 12px; transition:all 0.2s; }
  .lang-switch a.active { color:var(--paper); background:#1c1c1c; }
  .lang-switch a:hover { color:var(--paper); background:#111; }
  .report-link { font-size:9px; letter-spacing:0.2em; text-transform:uppercase; color:#5c1111; text-decoration:none; border:1px solid #2a0a0a; padding:6px 14px; transition:all 0.2s; }
  .report-link:hover { color:#8b1a1a; border-color:#5c1111; }
  .hero { display:grid; grid-template-columns:1fr 420px; min-height:80vh; border-bottom:1px solid var(--rule); }
  .hero-left { padding:80px 60px; display:flex; flex-direction:column; justify-content:center; border-right:1px solid var(--rule); }
  .eyebrow { font-size:10px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); margin-bottom:32px; }
  .hero-name { font-family:'Playfair Display',serif; font-size:clamp(2.5rem,5vw,4.5rem); font-weight:400; line-height:1.05; margin-bottom:20px; }
  .hero-subtitle { font-size:14px; color:var(--light-gray); letter-spacing:0.05em; margin-bottom:40px; font-style:italic; }
  .hero-meta { display:flex; flex-direction:column; gap:0; border-top:1px solid var(--rule); }
  .meta-item { display:grid; grid-template-columns:140px 1fr; gap:16px; padding:12px 0; border-bottom:1px solid #111; }
  .meta-item label { font-size:10px; letter-spacing:0.2em; text-transform:uppercase; color:#555; }
  .meta-item span { font-size:13px; color:var(--light-gray); }
  .hero-right { position:relative; overflow:hidden; background:#050505; }
  .hero-stamp { position:absolute; bottom:24px; left:24px; font-size:9px; letter-spacing:0.3em; text-transform:uppercase; color:var(--red); border:1px solid var(--red-dim); padding:6px 12px; background:rgba(0,0,0,0.7); }
  .section { border-bottom:1px solid var(--rule); padding:80px 0; }
  .container { max-width:760px; margin:0 auto; padding:0 60px; }
  .section-header { display:flex; align-items:center; gap:20px; margin-bottom:48px; }
  .section-num { font-size:11px; letter-spacing:0.3em; color:#333; }
  .section-title { font-family:'Playfair Display',serif; font-size:1.8rem; font-weight:400; flex:1; }
  .section-title::after { content:''; display:block; height:1px; background:var(--rule); margin-top:8px; }
  .intro-text { font-size:16px; line-height:1.9; color:var(--light-gray); margin-bottom:48px; }
  .timeline { display:flex; flex-direction:column; gap:0; }
  .timeline-entry { display:grid; grid-template-columns:80px 1fr; gap:24px; padding:28px 0; border-bottom:1px solid #0f0f0f; }
  .timeline-year { font-size:11px; letter-spacing:0.2em; color:var(--red); padding-top:4px; }
  .timeline-body h3 { font-size:14px; letter-spacing:0.05em; margin-bottom:10px; color:var(--paper); }
  .timeline-body p { font-size:14px; color:#888; line-height:1.8; }
  .quotes-grid { display:grid; grid-template-columns:1fr 1fr; gap:1px; background:var(--rule); }
  .quote-card { background:var(--card-bg); padding:32px; }
  .quote-text { font-family:'Playfair Display',serif; font-size:15px; font-style:italic; line-height:1.7; margin-bottom:16px; color:var(--paper); }
  .quote-source { font-size:11px; letter-spacing:0.15em; text-transform:uppercase; color:#444; }
  .method-text { font-size:15px; line-height:1.9; color:var(--light-gray); }
  .sanctions-block { background:var(--card-bg); border:1px solid #1a0000; border-left:3px solid var(--red); padding:28px 32px; }
  .sanctions-block p { font-size:14px; color:var(--light-gray); line-height:1.8; }
  .footer { padding:48px 60px; display:flex; justify-content:space-between; align-items:center; font-size:11px; letter-spacing:0.15em; text-transform:uppercase; color:#333; }
  .footer-rule { width:1px; height:40px; background:var(--rule); }
  .next-dosye { border-top:1px solid var(--rule); padding:48px 60px; display:flex; justify-content:space-between; align-items:center; text-decoration:none; color:var(--paper); transition:background 0.2s; }
  .next-dosye:hover { background:#0a0a0a; }
  .next-dosye-label { font-size:10px; letter-spacing:0.25em; text-transform:uppercase; color:#444; margin-bottom:8px; }
  .next-dosye-name { font-family:'Playfair Display',serif; font-size:1.6rem; font-weight:400; }
  .next-dosye-title { font-size:13px; color:#666; margin-top:4px; }
  .next-dosye-arrow { font-size:2rem; color:var(--red); }
  .share-bar { border-top:1px solid var(--rule); padding:24px 60px; display:flex; align-items:center; gap:16px; }
  .share-label { font-size:10px; letter-spacing:0.2em; text-transform:uppercase; color:#444; }
  .share-btn { font-size:10px; letter-spacing:0.15em; text-transform:uppercase; text-decoration:none; padding:8px 16px; border:1px solid #222; color:#888; transition:all 0.2s; }
  .share-btn:hover { border-color:#555; color:var(--paper); }
  @media (max-width: 768px) {
    .hero { grid-template-columns:1fr; }
    .hero-right { height:300px; }
    .hero-left { padding:48px 24px; }
    .container { padding:0 24px; }
    .quotes-grid { grid-template-columns:1fr; }
    .topbar { padding:12px 20px; }
    .topbar-right { gap:10px; }
    .report-link { display:none; }
    .footer { padding:32px 24px; flex-direction:column; gap:12px; text-align:center; }
    .next-dosye { padding:32px 20px; }
    .next-dosye-name { font-size:1.2rem; }
    .share-bar { padding:20px 20px; flex-wrap:wrap; gap:10px; }
  }
  @media print {
    * { -webkit-print-color-adjust:exact; print-color-adjust:exact; }
    body { background:#fff !important; color:#000 !important; font-size:11pt; }
    .topbar,#progress-bar,.share-bar,.next-dosye,.report-link,.lang-switch { display:none !important; }
    .hero { grid-template-columns:1fr 280px !important; page-break-inside:avoid; }
    .hero-right { height:280px !important; }
    .hero-left { background:#f5f5f5 !important; padding:32px !important; }
    .hero-name { color:#000 !important; font-size:28pt !important; }
    .section { border-color:#ddd !important; padding:24px 0 !important; page-break-inside:avoid; }
    .quote-card { background:#f9f9f9 !important; border:1px solid #ddd !important; color:#000 !important; }
    @page { margin:2cm; }
  }
</style>
</head>
<body>
<div id="progress-bar"></div>
<div class="topbar">
  <div class="topbar-left"><a href="index-en.html">← All dossiers</a></div>
  <div class="topbar-right">
    <div class="lang-switch">
      <a href="${p.id}.html">RU</a>
      <a href="${p.id}-en.html" class="active">EN</a>
    </div>
    <a href="submit-en.html" class="report-link">Submit a tip</a>
  </div>
</div>

<div class="hero">
  <div class="hero-left">
    <div class="eyebrow">Dossier · Archival material · 2025</div>
    <h1 class="hero-name">${d.name.replace(' ', '<br>')}</h1>
    <p class="hero-subtitle">${d.subtitle}</p>
    <div class="hero-meta">${metaHTML}
    </div>
  </div>
  <div class="hero-right">
    ${svgBackground(p.monogram)}
    <img loading="lazy" src="${p.photo}" alt="${d.name}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top center;opacity:0.45;mix-blend-mode:luminosity;" onerror="this.style.display='none'">
    <div class="hero-stamp">${d.stamp}</div>
  </div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-num">01</span>
      <h2 class="section-title">Biography</h2>
    </div>
    <p class="intro-text">${d.tagline}.</p>
    <div class="timeline">${bioHTML}
    </div>
  </div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-num">02</span>
      <h2 class="section-title">Quotes</h2>
    </div>
  </div>
  <div class="quotes-grid">${quotesHTML}
  </div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-num">03</span>
      <h2 class="section-title">The Method</h2>
    </div>
    <p class="method-text">${d.method}</p>
  </div>
</div>

<div class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-num">04</span>
      <h2 class="section-title">Sanctions</h2>
    </div>
    <div class="sanctions-block">
      <p>${d.sanctions_text}</p>
    </div>
  </div>
</div>

<div class="share-bar">
  <span class="share-label">Share</span>
  <a class="share-btn" href="https://twitter.com/intent/tweet?url=${pageUrl}&text=${encodeURIComponent(shareText)}" target="_blank" rel="noopener">Twitter / X</a>
  <a class="share-btn" href="https://t.me/share/url?url=${pageUrl}&text=${encodeURIComponent(shareText)}" target="_blank" rel="noopener">Telegram</a>
</div>

<a class="next-dosye" href="${next[0]}-en.html">
  <div>
    <div class="next-dosye-label">Next dossier →</div>
    <div class="next-dosye-name">${next[1]}</div>
    <div class="next-dosye-title">${next[2]}</div>
  </div>
  <div class="next-dosye-arrow">→</div>
</a>

<div class="footer">
  <span>Compiled from open sources</span>
  <div class="footer-rule"></div>
  <span>${d.name}</span>
  <div class="footer-rule"></div>
  <span>All facts verified by published media reports</span>
</div>

<script>
window.addEventListener('scroll', function() {
  var el = document.getElementById('progress-bar');
  var h = document.documentElement;
  var pct = (h.scrollTop / (h.scrollHeight - h.clientHeight)) * 100;
  el.style.width = pct + '%';
});
</script>
</body>
</html>`;
}

// Generate all pages
for (const p of people) {
  fs.writeFileSync(`${p.id}.html`, buildRU(p));
  fs.writeFileSync(`${p.id}-en.html`, buildEN(p));
  console.log(`✓ ${p.id}.html + ${p.id}-en.html`);
}

console.log('\nAll 10 new dossier pages generated.');
