/* Голоса Кремля — shared interactions: theme, header, index sheet, reveals, parallax */
(function () {
  'use strict';
  var root = document.documentElement;
  var lang = (root.lang || 'ru').slice(0, 2);
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  root.classList.add('js');

  /* ---------- Theme ---------- */
  var L = lang === 'ru'
    ? { light: 'Светлая', dark: 'Тёмная', toLight: 'Включить светлую тему', toDark: 'Включить тёмную тему' }
    : { light: 'Light', dark: 'Dark', toLight: 'Switch to light', toDark: 'Switch to dark' };
  function getTheme() { try { return localStorage.getItem('theme') || 'dark'; } catch (e) { return 'dark'; } }
  function paintToggle(t) {
    var b = document.getElementById('theme-toggle');
    if (!b) return;
    b.textContent = t === 'light' ? L.dark : L.light;
    b.title = t === 'light' ? L.toDark : L.toLight;
  }
  function setTheme(t) {
    root.dataset.theme = t;
    try { localStorage.setItem('theme', t); } catch (e) {}
    paintToggle(t);
  }
  root.dataset.theme = getTheme();

  function ready(fn) { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn); else fn(); }

  ready(function () {
    paintToggle(root.dataset.theme);
    var tb = document.getElementById('theme-toggle');
    if (tb) tb.addEventListener('click', function () { setTheme(root.dataset.theme === 'light' ? 'dark' : 'light'); });

    /* ---------- Header: border once scrolled, hide on fast scroll down ---------- */
    var head = document.querySelector('.site-head');
    var lastY = window.scrollY, ticking = false;
    function onScroll() {
      var y = window.scrollY;
      if (head) {
        head.classList.toggle('is-scrolled', y > 8);
        if (!document.body.classList.contains('menu-open')) {
          head.classList.toggle('is-hidden', y > 320 && y > lastY + 2);
          if (y < lastY - 2) head.classList.remove('is-hidden');
        }
      }
      lastY = y;
      parallax();
      ticking = false;
    }
    window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });

    /* ---------- Index sheet ---------- */
    var sheet = document.getElementById('menu');
    var openers = document.querySelectorAll('[data-menu-open]');
    function closeSheet() {
      if (!sheet) return;
      sheet.classList.remove('is-open');
      document.body.classList.remove('menu-open');
      openers.forEach(function (b) { b.setAttribute('aria-expanded', 'false'); });
    }
    if (sheet) {
      openers.forEach(function (b) {
        b.addEventListener('click', function () {
          sheet.classList.add('is-open');
          document.body.classList.add('menu-open');
          b.setAttribute('aria-expanded', 'true');
          var first = sheet.querySelector('a');
          if (first) setTimeout(function () { first.focus({ preventScroll: true }); }, 300);
        });
      });
      sheet.querySelectorAll('[data-menu-close]').forEach(function (b) { b.addEventListener('click', closeSheet); });
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeSheet(); });
    }

    /* ---------- Reveals ---------- */
    var auto = [
      '.section-header', '.timeline-entry', '.quote-card', '.person-quote', '.meme-card', '.grid-card',
      '.roots-card', '.stat-card', '.interview-row', '.quote-pull', '.source-card-d', '.source-card-en',
      '.related-card', '.about-section', '.about-card', '.principle-card', '.source-card', '.tl-entry',
      '.term-entry', '.term-card', '.asset-card', '.conn-card', '.channel-row', '.flow-card', '.content-block',
      '.ov-card', '.stat-cell', '.ss-cell', '.empire-col', '.qsection', '.theme-section', '.film-row', '.property-card',
      '.sanction-item', '.method-text', '.intro-text', '[data-rv]'
    ].join(',');
    var els = Array.prototype.slice.call(document.querySelectorAll(auto));
    els.forEach(function (el) { if (!el.classList.contains('rv-line') && !el.classList.contains('rv-img')) el.classList.add('rv'); });
    var all = document.querySelectorAll('.rv, .rv-line, .rv-img');
    if (!('IntersectionObserver' in window) || reduce) {
      all.forEach(function (el) { el.classList.add('in'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        var batch = 0;
        entries.forEach(function (en) {
          if (!en.isIntersecting) return;
          var el = en.target;
          if (!el.style.getPropertyValue('--d')) el.style.setProperty('--d', Math.min(batch, 5) * 0.07 + 's');
          el.classList.add('in');
          batch++;
          io.unobserve(el);
        });
      }, { threshold: 0.06, rootMargin: '0px 0px -6% 0px' });
      all.forEach(function (el) { io.observe(el); });
      // safety: never leave content hidden (e.g. print, anchors)
      window.addEventListener('beforeprint', function () { all.forEach(function (el) { el.classList.add('in'); }); });
    }

    /* ---------- Parallax ---------- */
    var px = Array.prototype.slice.call(document.querySelectorAll('[data-parallax]'));
    function parallax() {
      if (reduce || !px.length) return;
      var vh = window.innerHeight;
      px.forEach(function (el) {
        var r = el.parentElement.getBoundingClientRect();
        if (r.bottom < 0 || r.top > vh) return;
        var k = parseFloat(el.getAttribute('data-parallax')) || 0.08;
        var off = (r.top + r.height / 2 - vh / 2) * -k;
        el.style.transform = 'translate3d(0,' + off.toFixed(1) + 'px,0) scale(1.08)';
      });
    }
    onScroll();

    /* ---------- Cursor-follow preview (catalogue rows with data-img) ---------- */
    var pv = document.getElementById('hover-preview');
    if (pv && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
      var pimg = pv.querySelector('img');
      var tx = 0, ty = 0, cx = 0, cy = 0, raf = null;
      function loop() {
        cx += (tx - cx) * 0.16; cy += (ty - cy) * 0.16;
        pv.style.transform = 'translate3d(' + cx.toFixed(1) + 'px,' + cy.toFixed(1) + 'px,0)';
        raf = (Math.abs(tx - cx) > .3 || Math.abs(ty - cy) > .3) ? requestAnimationFrame(loop) : null;
      }
      document.querySelectorAll('[data-img]').forEach(function (row) {
        row.addEventListener('mouseenter', function () {
          var src = row.getAttribute('data-img');
          if (pimg.getAttribute('src') !== src) pimg.setAttribute('src', src);
          pv.classList.add('on');
        });
        row.addEventListener('mouseleave', function () { pv.classList.remove('on'); });
        row.addEventListener('mousemove', function (e) {
          tx = e.clientX + 28; ty = e.clientY - 120;
          if (tx + 230 > window.innerWidth) tx = e.clientX - 258;
          if (!raf) raf = requestAnimationFrame(loop);
        });
      });
    }
  });
})();
