/* people.js — единый каталог 36 фигурантов / canonical 36-person catalog
   Kremlin Voices · https://cycterna2222288888-ai.github.io/cremle/
   Используется: навигация, random, submit-dropdown, build-index, RSS, sitemap */
var PEOPLE = [
  {slug:"solovyov",nameRU:"Владимир Соловьёв",nameEN:"Vladimir Solovyov",channel:"rossiya1"},
  {slug:"skabeeva",nameRU:"Ольга Скабеева",nameEN:"Olga Skabeeva",channel:"rossiya1"},
  {slug:"kiselyov",nameRU:"Дмитрий Киселёв",nameEN:"Dmitry Kiselyov",channel:"rt"},
  {slug:"simonyan",nameRU:"Маргарита Симоньян",nameEN:"Margarita Simonyan",channel:"rt"},
  {slug:"popov",nameRU:"Евгений Попов",nameEN:"Yevgeny Popov",channel:"rossiya1"},
  {slug:"sheynin",nameRU:"Артём Шейнин",nameEN:"Artyom Sheynin",channel:"perviy"},
  {slug:"tolstoy",nameRU:"Пётр Толстой",nameEN:"Pyotr Tolstoy",channel:"vlast"},
  {slug:"norkin",nameRU:"Андрей Норкин",nameEN:"Andrey Norkin",channel:"ntv"},
  {slug:"keosayan",nameRU:"Тигран Кеосаян",nameEN:"Tigran Keosayan",channel:"rt"},
  {slug:"andreyeva",nameRU:"Екатерина Андреева",nameEN:"Yekaterina Andreyeva",channel:"perviy"},
  {slug:"mamontov",nameRU:"Аркадий Мамонтов",nameEN:"Arkady Mamontov",channel:"rossiya1"},
  {slug:"prilepin",nameRU:"Захар Прилепин",nameEN:"Zakhar Prilepin",channel:"vlast"},
  {slug:"leontyev",nameRU:"Михаил Леонтьев",nameEN:"Mikhail Leontyev",channel:"perviy"},
  {slug:"korchevnikov",nameRU:"Борис Корчевников",nameEN:"Boris Korchevnikov",channel:"rossiya1"},
  {slug:"medinsky",nameRU:"Владимир Мединский",nameEN:"Vladimir Medinsky",channel:"vlast"},
  {slug:"mikhalkov",nameRU:"Никита Михалков",nameEN:"Nikita Mikhalkov",channel:"kultura"},
  {slug:"dugin",nameRU:"Александр Дугин",nameEN:"Alexander Dugin",channel:"ideolog"},
  {slug:"krasovsky",nameRU:"Антон Красовский",nameEN:"Anton Krasovsky",channel:"rt"},
  {slug:"medvedev",nameRU:"Дмитрий Медведев",nameEN:"Dmitry Medvedev",channel:"vlast"},
  {slug:"kadyrov",nameRU:"Рамзан Кадыров",nameEN:"Ramzan Kadyrov",channel:"vlast"},
  {slug:"malofeev",nameRU:"Константин Малофеев",nameEN:"Konstantin Malofeev",channel:"ideolog"},
  {slug:"nikonov",nameRU:"Вячеслав Никонов",nameEN:"Vyacheslav Nikonov",channel:"vlast"},
  {slug:"poddubny",nameRU:"Евгений Поддубный",nameEN:"Evgeny Poddubny",channel:"rt"},
  {slug:"zakharova",nameRU:"Мария Захарова",nameEN:"Maria Zakharova",channel:"vlast"},
  {slug:"kovalchuk",nameRU:"Юрий Ковальчук",nameEN:"Yuri Kovalchuk",channel:"vlast"},
  {slug:"turchak",nameRU:"Андрей Турчак",nameEN:"Andrei Turchak",channel:"vlast"},
  {slug:"navka",nameRU:"Татьяна Навка",nameEN:"Tatiana Navka",channel:"kultura"},
  {slug:"peskov",nameRU:"Дмитрий Песков",nameEN:"Dmitry Peskov",channel:"vlast"},
  {slug:"lavrov",nameRU:"Сергей Лавров",nameEN:"Sergei Lavrov",channel:"vlast"},
  {slug:"mizulina",nameRU:"Елена Мизулина",nameEN:"Elena Mizulina",channel:"vlast"},
  {slug:"nebenzya",nameRU:"Василий Небензя",nameEN:"Vasily Nebenzya",channel:"vlast"},
  {slug:"patrushev",nameRU:"Николай Патрушев",nameEN:"Nikolai Patrushev",channel:"vlast"},
  {slug:"matvienko",nameRU:"Валентина Матвиенко",nameEN:"Valentina Matvienko",channel:"vlast"},
  {slug:"slutsky",nameRU:"Леонид Слуцкий",nameEN:"Leonid Slutsky",channel:"vlast"},
  {slug:"emizulina",nameRU:"Екатерина Мизулина",nameEN:"Yekaterina Mizulina",channel:"vlast"},
  {slug:"kirill",nameRU:"Патриарх Кирилл",nameEN:"Patriarch Kirill",channel:"ideolog"}
];
/* helpers */
var SLUGS_RU = PEOPLE.map(function(p){return p.slug+'.html';});
var SLUGS_EN = PEOPLE.map(function(p){return p.slug+'-en.html';});
