/* MAPA MARKETING — main.js
   Idioma, navegación, enlaces de WhatsApp y animaciones de entrada. */

(function () {
  'use strict';

  /* ---------- Configuración ---------- */
  window.MAPA = window.MAPA || {};
  MAPA.PHONE = '19805164214'; // <-- cambia aquí el número (solo dígitos, con código de país)

  /* Almacenamiento tolerante a fallos (modo incógnito, iframes, etc.) */
  var mem = {};
  MAPA.store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return mem[k] || null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) { mem[k] = v; } }
  };

  /* ---------- WhatsApp ---------- */
  MAPA.waLink = function (msg) {
    return 'https://wa.me/' + MAPA.PHONE + (msg ? '?text=' + encodeURIComponent(msg) : '');
  };

  MAPA.openWA = function (msg) {
    window.open(MAPA.waLink(msg), '_blank', 'noopener');
  };

  /* Rellena cada <a class="wa"> con el mensaje del idioma activo.
     data-msg-es / data-msg-en. Si el usuario escribió su ciudad, se añade. */
  MAPA.refreshWA = function () {
    var lang = document.documentElement.getAttribute('data-lang') || 'es';
    var city = (MAPA.store.get('mapa_city') || '').trim();
    document.querySelectorAll('a.wa').forEach(function (a) {
      var msg = a.getAttribute('data-msg-' + lang) || a.getAttribute('data-msg') ||
                a.getAttribute('data-msg-es') || '';
      if (city && msg) {
        msg += (lang === 'en' ? ' My business is in ' : ' Mi negocio está en ') + city + '.';
      }
      a.setAttribute('href', MAPA.waLink(msg));
      a.setAttribute('target', '_blank');
      a.setAttribute('rel', 'noopener');
    });
  };

  /* ---------- Idioma ----------
     Cada idioma tiene su propia URL (/ y /en/). El documento ya viene con el
     idioma correcto, así que aquí sólo lo leemos. */
  MAPA.lang = function () { return document.documentElement.getAttribute('data-lang') || 'es'; };
  MAPA.t = function (es, en) { return MAPA.lang() === 'en' ? en : es; };
  MAPA.refreshWA();

  /* ---------- Navegación móvil ---------- */
  var burger = document.querySelector('.burger');
  var links = document.querySelector('.nav__links');
  if (burger && links) {
    burger.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      burger.setAttribute('aria-expanded', String(open));
    });
    links.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') { links.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); }
    });
  }

  /* Marca la página actual */
  var here = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav__links a[href]').forEach(function (a) {
    if (a.getAttribute('href') === here) a.setAttribute('aria-current', 'page');
  });

  /* ---------- Ciudad del héroe ---------- */
  var cityInput = document.getElementById('cityInput');
  if (cityInput) {
    var saved = MAPA.store.get('mapa_city');
    if (saved) cityInput.value = saved;
    var label = document.getElementById('mapCity');
    var paint = function () {
      var v = cityInput.value.trim();
      MAPA.store.set('mapa_city', v);
      if (label) label.textContent = (v ? v.toUpperCase().slice(0, 16) : MAPA.t('TU CIUDAD', 'YOUR CITY'));
      MAPA.refreshWA();
    };
    cityInput.addEventListener('input', paint);
    paint();
    document.addEventListener('mapa:lang', paint);
  }

  /* ---------- Animaciones de entrada ---------- */
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var targets = document.querySelectorAll('.reveal');
  if (reduce || !('IntersectionObserver' in window)) {
    targets.forEach(function (t) { t.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: .08 });
    targets.forEach(function (t) { io.observe(t); });
  }

  /* ---------- Botones de copiar ---------- */
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('.copy');
    if (!btn) return;
    var box = btn.closest('.out');
    var txt = box ? (box.querySelector('[data-copy]') || box.querySelector('p')).innerText : '';
    var done = function () {
      var old = btn.textContent;
      btn.textContent = MAPA.t('COPIADO', 'COPIED');
      setTimeout(function () { btn.textContent = old; }, 1600);
    };
    if (navigator.clipboard) { navigator.clipboard.writeText(txt).then(done, done); }
    else {
      var ta = document.createElement('textarea');
      ta.value = txt; document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); } catch (err) {}
      document.body.removeChild(ta); done();
    }
  });

  /* ---------- Barra de progreso de lectura (guía) ---------- */
  var prog = document.querySelector('.progress');
  if (prog) {
    var onScroll = function () {
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      prog.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + '%';
    };
    document.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Índice activo (guía) ---------- */
  var tocLinks = document.querySelectorAll('.toc a[href^="#"]');
  if (tocLinks.length && 'IntersectionObserver' in window) {
    var map = {};
    tocLinks.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var io2 = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          tocLinks.forEach(function (a) { a.classList.remove('active'); });
          if (map[en.target.id]) map[en.target.id].classList.add('active');
        }
      });
    }, { rootMargin: '-15% 0px -70% 0px' });
    document.querySelectorAll('.chapter[id]').forEach(function (c) { io2.observe(c); });
  }

  /* Año en el pie */
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
