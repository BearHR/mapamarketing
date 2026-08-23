/* MAPA MARKETING — tools.js
   Lógica de las cinco herramientas. Todo corre en el navegador.
   Cada herramienta termina en un mensaje de WhatsApp listo para enviar. */

(function () {
  'use strict';
  var T = function (es, en) { return MAPA.t(es, en); };
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* =====================================================================
     1. DIAGNÓSTICO DE VISIBILIDAD LOCAL
     ===================================================================== */
  var AUDIT = [
    { c: 'web', w: 3,
      es: 'Tu sitio web carga en menos de 3 segundos en el celular.',
      en: 'Your website loads in under 3 seconds on a phone.',
      hes: 'Pruébalo con datos móviles, no con wifi.', hen: 'Test it on mobile data, not wifi.',
      fes: 'Medir la velocidad real en celular y arreglar lo que la frena (imágenes pesadas, código de más).',
      fen: 'Measure real mobile speed and fix what slows it down (heavy images, extra code).' },
    { c: 'web', w: 3,
      es: 'Tienes una página distinta para cada servicio que vendes.',
      en: 'You have a separate page for every service you sell.',
      hes: 'No una sola página de "Servicios" con una lista.', hen: 'Not one "Services" page with a list.',
      fes: 'Crear una página por servicio, con su propio título, contenido y llamada a la acción.',
      fen: 'Build one page per service, each with its own title, content and call to action.' },
    { c: 'web', w: 2,
      es: 'Tienes una página por cada ciudad donde trabajas.',
      en: 'You have a page for each city you serve.',
      fes: 'Crear páginas de ciudad reales (no copias): referencias locales, trabajos, tiempos de llegada.',
      fen: 'Build real city pages (not copies): local references, jobs, response times.' },
    { c: 'web', w: 2,
      es: 'El botón de contacto se ve sin bajar la pantalla, en celular.',
      en: 'Your contact button is visible without scrolling, on mobile.',
      fes: 'Poner llamada y WhatsApp fijos arriba y abajo en móvil.',
      fen: 'Pin call and WhatsApp buttons top and bottom on mobile.' },
    { c: 'web', w: 2,
      es: 'Sabes en qué parte de tu sitio la gente se va sin contactarte.',
      en: 'You know where on your site people leave without contacting you.',
      hes: 'Esto se ve con mapas de calor y grabaciones.', hen: 'Heatmaps and session recordings show this.',
      fes: 'Instalar mapas de calor y revisar mes a mes dónde se pierde la gente.',
      fen: 'Install heatmaps and review monthly where visitors drop off.' },

    { c: 'gbp', w: 3,
      es: 'Tu Perfil de Negocio de Google está verificado y lo controlas tú.',
      en: 'Your Google Business Profile is verified and you control it.',
      fes: 'Reclamar y verificar el perfil. Sin esto, nada más del mapa funciona.',
      fen: 'Claim and verify the profile. Nothing else on the map works without it.' },
    { c: 'gbp', w: 3,
      es: 'Tu categoría principal es la más específica que existe para tu oficio.',
      en: 'Your primary category is the most specific one that exists for your trade.',
      hes: 'Ej. "Plomero" es mejor que "Contratista".', hen: 'E.g. "Plumber" beats "Contractor".',
      fes: 'Revisar la categoría principal y las secundarias contra las de los tres que salen arriba.',
      fen: 'Audit primary and secondary categories against the three ranking above you.' },
    { c: 'gbp', w: 2,
      es: 'Publicas en tu Perfil de Google al menos una vez por semana.',
      en: 'You post to your Google profile at least once a week.',
      fes: 'Cuatro publicaciones al mes, con foto y llamada a la acción.',
      fen: 'Four posts a month, each with a photo and a call to action.' },
    { c: 'gbp', w: 2,
      es: 'Subes fotos nuevas de trabajos reales cada mes.',
      en: 'You upload new photos of real jobs every month.',
      fes: 'Diez a quince fotos al mes: antes, durante, después, equipo, camioneta.',
      fen: 'Ten to fifteen photos a month: before, during, after, crew, truck.' },

    { c: 'mapas', w: 2,
      es: 'Tu negocio aparece en Apple Maps con la información correcta.',
      en: 'Your business is on Apple Maps with correct information.',
      hes: 'Más de la mitad de los teléfonos en EE.UU. son iPhone.', hen: 'Over half of US phones are iPhones.',
      fes: 'Reclamar Apple Business Connect: horario, fotos, categoría, área de servicio.',
      fen: 'Claim Apple Business Connect: hours, photos, category, service area.' },
    { c: 'mapas', w: 1,
      es: 'Tienes tu ficha en Bing Places al día.',
      en: 'Your Bing Places listing is up to date.',
      fes: 'Reclamar Bing Places. Es la fuente de varios asistentes de IA.',
      fen: 'Claim Bing Places. It feeds several AI assistants.' },
    { c: 'mapas', w: 2,
      es: 'Tu perfil de Yelp está reclamado, con fotos y servicios completos.',
      en: 'Your Yelp profile is claimed, with photos and full service list.',
      fes: 'Completar Yelp: horarios, área, servicios, fotos y respuesta a reseñas.',
      fen: 'Complete Yelp: hours, area, services, photos and review replies.' },
    { c: 'mapas', w: 3,
      es: 'Tu nombre, dirección y teléfono son idénticos en todos lados.',
      en: 'Your name, address and phone are identical everywhere.',
      hes: 'Ave. vs Avenue, Suite 2 vs #2 — eso cuenta.', hen: 'Ave. vs Avenue, Suite 2 vs #2 — that counts.',
      fes: 'Fijar un formato único de NAP y corregir cada directorio donde no coincida.',
      fen: 'Lock one NAP format and correct every directory that disagrees.' },

    { c: 'resenas', w: 3,
      es: 'Pides reseñas a todos tus clientes de forma sistemática.',
      en: 'You ask every customer for a review, systematically.',
      fes: 'Un proceso fijo: mensaje con el enlace directo el mismo día del trabajo.',
      fen: 'A fixed process: text the direct review link the same day as the job.' },
    { c: 'resenas', w: 2,
      es: 'Respondes a todas las reseñas, buenas y malas, en menos de 48 horas.',
      en: 'You reply to every review, good and bad, within 48 hours.',
      fes: 'Responder todo. La respuesta la leen los que aún no te contratan.',
      fen: 'Reply to everything. The reply is read by people who haven\'t hired you yet.' },

    { c: 'contenido', w: 2,
      es: 'Publicas contenido nuevo en tu sitio todos los meses.',
      en: 'You publish new content on your site every month.',
      fes: 'Tres artículos al mes que respondan preguntas reales de clientes.',
      fen: 'Three articles a month answering real customer questions.' },
    { c: 'contenido', w: 2,
      es: 'Otros sitios locales enlazan al tuyo.',
      en: 'Other local websites link to yours.',
      hes: 'Cámara de comercio, proveedores, patrocinios, prensa local.', hen: 'Chamber of commerce, suppliers, sponsorships, local press.',
      fes: 'Un enlace local nuevo al mes, ganado, no comprado.',
      fen: 'One new local link per month, earned, not bought.' },
    { c: 'contenido', w: 1,
      es: 'Sabes si apareces cuando alguien le pregunta a ChatGPT por tu servicio.',
      en: 'You know whether you appear when someone asks ChatGPT for your service.',
      fes: 'Probar las búsquedas con IA y reforzar las fuentes de donde beben (mapas, reseñas, directorios).',
      fen: 'Test AI searches and reinforce the sources they pull from (maps, reviews, directories).' }
  ];

  var CATS = {
    web: { es: 'Sitio web', en: 'Website' },
    gbp: { es: 'Perfil de Google', en: 'Google profile' },
    mapas: { es: 'Otros mapas', en: 'Other maps' },
    resenas: { es: 'Reseñas', en: 'Reviews' },
    contenido: { es: 'Contenido y enlaces', en: 'Content & links' }
  };

  function initAudit(root) {
    var list = $('#auditList', root);
    AUDIT.forEach(function (q, i) {
      var row = document.createElement('div');
      row.className = 'q';
      row.innerHTML =
        '<div class="q__t">' +
          '<span data-l="es">' + q.es + '</span><span data-l="en">' + q.en + '</span>' +
          (q.hes ? '<small><span data-l="es">' + q.hes + '</span><span data-l="en">' + q.hen + '</span></small>' : '') +
        '</div>' +
        '<div class="opts" role="group">' +
          opt(i, 2, 'Sí', 'Yes') + opt(i, 1, 'Más o menos', 'Sort of') + opt(i, 0, 'No', 'No') +
        '</div>';
      list.appendChild(row);
    });

    function opt(i, v, es, en) {
      var id = 'q' + i + '_' + v;
      return '<input type="radio" name="q' + i + '" id="' + id + '" value="' + v + '">' +
        '<label for="' + id + '"><span data-l="es">' + es + '</span><span data-l="en">' + en + '</span></label>';
    }

    $('#auditRun', root).addEventListener('click', function () {
      var got = 0, max = 0, byCat = {}, fixes = [];
      AUDIT.forEach(function (q, i) {
        var sel = $('input[name="q' + i + '"]:checked', root);
        var v = sel ? parseInt(sel.value, 10) : 0;
        byCat[q.c] = byCat[q.c] || { g: 0, m: 0 };
        byCat[q.c].g += v * q.w; byCat[q.c].m += 2 * q.w;
        got += v * q.w; max += 2 * q.w;
        if (v < 2) fixes.push({ w: q.w * (2 - v), es: q.fes, en: q.fen });
      });
      var score = Math.round((got / max) * 100);
      var res = $('#auditResult', root);
      res.hidden = false;
      $('#auditScore', root).textContent = score;
      setTimeout(function () { $('#auditBar', root).style.width = score + '%'; }, 60);

      var verdict = $('#auditVerdict', root);
      var v = score >= 80
        ? ['Vas muy bien. Lo que falta son detalles que deciden entre el primer y el cuarto lugar.', 'You are in good shape. What is left are the details that decide first place versus fourth.']
        : score >= 55
          ? ['Tienes la base puesta pero estás dejando llamadas en la mesa cada semana.', 'The foundation is there, but you are leaving calls on the table every week.']
          : score >= 30
            ? ['Estás a medias. Tus competidores con menos experiencia te están ganando por presencia, no por calidad.', 'You are halfway. Less experienced competitors are beating you on presence, not on quality.']
            : ['Ahora mismo eres prácticamente invisible en el mapa. La buena noticia: casi todo esto se arregla en semanas.', 'Right now you are close to invisible on the map. The good news: most of this is fixable in weeks.'];
      verdict.innerHTML = '<span data-l="es">' + v[0] + '</span><span data-l="en">' + v[1] + '</span>';

      var brk = $('#auditBreak', root); brk.innerHTML = '';
      Object.keys(CATS).forEach(function (k) {
        var p = byCat[k] ? Math.round((byCat[k].g / byCat[k].m) * 100) : 0;
        var r = document.createElement('div');
        r.className = 'brk__row';
        r.innerHTML = '<div><span data-l="es">' + CATS[k].es + '</span><span data-l="en">' + CATS[k].en + '</span></div>' +
          '<div class="brk__bar"><i style="width:' + p + '%"></i></div><div class="brk__v">' + p + '%</div>';
        brk.appendChild(r);
      });

      fixes.sort(function (a, b) { return b.w - a.w; });
      var top = fixes.slice(0, 6);
      var ul = $('#auditFixes', root); ul.innerHTML = '';
      top.forEach(function (f) {
        var li = document.createElement('li');
        li.innerHTML = '<span data-l="es">' + f.es + '</span><span data-l="en">' + f.en + '</span>';
        ul.appendChild(li);
      });
      $('#auditFixWrap', root).hidden = top.length === 0;

      var msgEs = 'Hola MAPA. Hice el diagnóstico de visibilidad en su sitio y saqué ' + score + '/100.\n\nLo más flojo:\n' +
        top.slice(0, 4).map(function (f, i) { return (i + 1) + '. ' + f.es; }).join('\n') +
        '\n\nQuiero saber cómo lo arreglarían.';
      var msgEn = 'Hi MAPA. I took the visibility check on your site and scored ' + score + '/100.\n\nWeakest points:\n' +
        top.slice(0, 4).map(function (f, i) { return (i + 1) + '. ' + f.en; }).join('\n') +
        '\n\nI would like to know how you would fix this.';
      var link = $('#auditWA', root);
      link.setAttribute('data-msg-es', msgEs);
      link.setAttribute('data-msg-en', msgEn);
      MAPA.refreshWA();
      res.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  }

  /* =====================================================================
     2. CALCULADORA DE TRABAJOS PERDIDOS
     ===================================================================== */
  function money(n) {
    return '$' + Math.round(n).toLocaleString('en-US');
  }

  function initCalc(root) {
    var run = function () {
      var job = parseFloat($('#cTicket', root).value) || 0;
      var close = (parseFloat($('#cClose', root).value) || 0) / 100;
      var leads = parseFloat($('#cLeads', root).value) || 0;
      var repeat = parseFloat($('#cRepeat', root).value) || 1;

      var perLead = job * close * repeat;
      var now = perLead * leads;
      var rows = [3, 6, 12];
      var box = $('#cOut', root); box.innerHTML = '';
      rows.forEach(function (extra) {
        var gain = perLead * extra;
        var c = document.createElement('div');
        c.className = 'money__c';
        c.innerHTML = '<div class="money__k">+' + extra +
          '<span data-l="es"> contactos/mes</span><span data-l="en"> leads/mo</span></div>' +
          '<div class="money__v">' + money(gain) + '</div>' +
          '<div class="money__s">' + money(gain * 12) +
          '<span data-l="es"> al año</span><span data-l="en"> per year</span></div>';
        box.appendChild(c);
      });
      $('#cPerLead', root).textContent = money(perLead);
      $('#cNow', root).textContent = money(now);
      $('#calcResult', root).hidden = false;

      var msgEs = 'Hola MAPA. Corrí la calculadora en su sitio.\n\nTrabajo promedio: ' + money(job) +
        '\nCierro el ' + Math.round(close * 100) + '% de los contactos\nContactos hoy: ' + leads + ' al mes' +
        '\nCada contacto vale ' + money(perLead) + ' para mí.\n\nSi me trajeran 6 contactos más al mes serían ' +
        money(perLead * 6 * 12) + ' al año. Quiero platicar de eso.';
      var msgEn = 'Hi MAPA. I ran the calculator on your site.\n\nAverage job: ' + money(job) +
        '\nI close ' + Math.round(close * 100) + '% of leads\nLeads today: ' + leads + '/month' +
        '\nEach lead is worth ' + money(perLead) + ' to me.\n\n6 extra leads a month would be ' +
        money(perLead * 6 * 12) + ' a year. I want to talk about that.';
      var link = $('#calcWA', root);
      link.setAttribute('data-msg-es', msgEs);
      link.setAttribute('data-msg-en', msgEn);
      MAPA.refreshWA();
    };
    $$('#calcForm input', root).forEach(function (i) { i.addEventListener('input', run); });
    $('#calcRun', root).addEventListener('click', run);
    run();
  }

  /* =====================================================================
     3. GENERADOR DE PUBLICACIONES PARA EL PERFIL DE GOOGLE
     ===================================================================== */
  var TRADES = {
    plomeria: {
      es: { n: 'Plomería', s: ['reparación de fugas', 'destape de drenajes', 'cambio de calentador'],
            tip: 'Cierra la llave de paso y mira el medidor de agua. Si sigue girando con todo cerrado, tienes una fuga escondida.',
            job: 'Cambiamos un calentador de agua de 40 galones en una casa de %CITY% en la misma mañana.',
            urg: 'una fuga a media noche' },
      en: { n: 'Plumbing', s: ['leak repair', 'drain cleaning', 'water heater replacement'],
            tip: 'Shut the main valve and watch the water meter. If it keeps moving with everything off, you have a hidden leak.',
            job: 'We swapped a 40-gallon water heater at a %CITY% home in a single morning.',
            urg: 'a midnight leak' }
    },
    hvac: {
      es: { n: 'Aire y calefacción', s: ['mantenimiento de A/C', 'reparación de calefacción', 'instalación de equipos'],
            tip: 'Cambia el filtro cada 60 a 90 días. Un filtro sucio sube el recibo de luz y mata el compresor antes de tiempo.',
            job: 'Dejamos un A/C de 3 toneladas enfriando otra vez en una casa de %CITY% el mismo día de la llamada.',
            urg: 'quedarte sin aire en pleno julio' },
      en: { n: 'HVAC', s: ['A/C tune-ups', 'heating repair', 'system installation'],
            tip: 'Change the filter every 60 to 90 days. A dirty filter raises your power bill and kills the compressor early.',
            job: 'We had a 3-ton A/C cooling again at a %CITY% home the same day they called.',
            urg: 'losing your A/C in July' }
    },
    techos: {
      es: { n: 'Techos', s: ['reparación de goteras', 'techo nuevo', 'inspección tras tormenta'],
            tip: 'Después de una granizada, revisa los canalones: si encuentras gránulos como arena, tu teja ya está perdiendo capa.',
            job: 'Reemplazamos un techo completo en %CITY% en dos días, con limpieza el mismo día.',
            urg: 'una gotera después de la tormenta' },
      en: { n: 'Roofing', s: ['leak repair', 'roof replacement', 'storm inspection'],
            tip: 'After hail, check the gutters: sand-like granules mean your shingles are already losing their coating.',
            job: 'We replaced a full roof in %CITY% in two days, with same-day cleanup.',
            urg: 'a leak after the storm' }
    },
    jardineria: {
      es: { n: 'Jardinería y paisajismo', s: ['mantenimiento semanal', 'diseño de jardín', 'sistemas de riego'],
            tip: 'Riega temprano, antes de las 9 de la mañana. Regar de noche deja la raíz húmeda y provoca hongo.',
            job: 'Rediseñamos el frente de una casa en %CITY%: riego nuevo, grava y plantas que aguantan el calor.',
            urg: 'un jardín seco antes de vender la casa' },
      en: { n: 'Landscaping', s: ['weekly maintenance', 'landscape design', 'irrigation systems'],
            tip: 'Water before 9 a.m. Watering at night leaves roots damp and invites fungus.',
            job: 'We redid a %CITY% front yard: new irrigation, gravel and heat-tolerant plants.',
            urg: 'a dry yard right before you sell' }
    },
    limpieza: {
      es: { n: 'Limpieza', s: ['limpieza profunda', 'limpieza de mudanza', 'servicio recurrente'],
            tip: 'Limpia de arriba hacia abajo y deja los pisos al final. Al revés terminas limpiando dos veces.',
            job: 'Entregamos una limpieza de salida en %CITY% a tiempo para la inspección del casero.',
            urg: 'una inspección mañana' },
      en: { n: 'Cleaning', s: ['deep cleaning', 'move-out cleaning', 'recurring service'],
            tip: 'Clean top to bottom and save floors for last. Any other order means cleaning twice.',
            job: 'We finished a %CITY% move-out clean in time for the landlord walkthrough.',
            urg: 'an inspection tomorrow' }
    },
    electricidad: {
      es: { n: 'Electricidad', s: ['cambio de panel', 'instalación de luces', 'diagnóstico de cortos'],
            tip: 'Si un breaker se bota más de una vez al mes, no es el breaker: es el circuito pidiendo ayuda.',
            job: 'Cambiamos un panel de 100 a 200 amperios en %CITY% con permiso e inspección incluidos.',
            urg: 'un corto que te deja sin luz' },
      en: { n: 'Electrical', s: ['panel upgrades', 'lighting installation', 'short-circuit diagnosis'],
            tip: 'If a breaker trips more than once a month, it is not the breaker. It is the circuit asking for help.',
            job: 'We upgraded a %CITY% panel from 100 to 200 amps, permit and inspection included.',
            urg: 'a short that kills your power' }
    },
    remodelacion: {
      es: { n: 'Remodelación', s: ['remodelación de baño', 'cocinas', 'pisos'],
            tip: 'Pide siempre el estimado por escrito con marcas y modelos. "Materiales incluidos" no dice nada.',
            job: 'Terminamos un baño completo en %CITY% en tres semanas, sin pasarnos del presupuesto.',
            urg: 'un baño a medias desde hace meses' },
      en: { n: 'Remodeling', s: ['bathroom remodels', 'kitchens', 'flooring'],
            tip: 'Always get the estimate in writing with brands and model numbers. "Materials included" says nothing.',
            job: 'We finished a full %CITY% bathroom in three weeks, on budget.',
            urg: 'a half-finished bathroom' }
    },
    plagas: {
      es: { n: 'Control de plagas', s: ['tratamiento de cucarachas', 'termitas', 'servicio trimestral'],
            tip: 'Sella la línea donde el muro toca el piso. La mayoría de las cucarachas entran por ahí, no por la puerta.',
            job: 'Cortamos una infestación de cucarachas en un restaurante de %CITY% en dos visitas.',
            urg: 'ver una cucaracha frente a un cliente' },
      en: { n: 'Pest control', s: ['roach treatment', 'termites', 'quarterly service'],
            tip: 'Seal the line where wall meets floor. Most roaches come in there, not through the door.',
            job: 'We shut down a roach problem at a %CITY% restaurant in two visits.',
            urg: 'a roach in front of a customer' }
    }
  };

  function initPosts(root) {
    var sel = $('#pTrade', root);
    Object.keys(TRADES).forEach(function (k) {
      var o = document.createElement('option');
      o.value = k;
      o.textContent = TRADES[k].es.n + ' / ' + TRADES[k].en.n;
      sel.appendChild(o);
    });

    function build() {
      var lang = MAPA.lang();
      var t = TRADES[sel.value][lang] || TRADES[sel.value].es;
      var city = ($('#pCity', root).value || '').trim() || T('tu ciudad', 'your city');
      var biz = ($('#pBiz', root).value || '').trim() || T('tu negocio', 'your business');
      var offer = ($('#pOffer', root).value || '').trim();
      var fill = function (s) { return s.replace(/%CITY%/g, city); };

      var posts = lang === 'en' ? [
        { k: 'Post 1 — Service reminder',
          h: t.s[0].charAt(0).toUpperCase() + t.s[0].slice(1) + ' in ' + city,
          b: 'Need ' + t.s[0] + ' in ' + city + '? ' + biz + ' answers, shows up, and tells you the price before we start. No surprises on the invoice.\n\nWe serve ' + city + ' and nearby areas. Message us and we will tell you today whether we can help.' },
        { k: 'Post 2 — Useful tip',
          h: 'A tip that saves you money',
          b: t.tip + '\n\nWe post one of these every week. If you would rather have someone look at it, ' + biz + ' is a message away.' },
        { k: 'Post 3 — Recent job',
          h: 'Recent job in ' + city,
          b: fill(t.job) + '\n\nEvery job gets photos before and after. Ask us for the ones like yours.' },
        { k: 'Post 4 — ' + (offer ? 'Offer' : 'Urgency'),
          h: offer ? offer : 'Do not wait on ' + t.urg,
          b: (offer
              ? offer + ' for ' + city + ' customers. Mention this post when you contact us.'
              : 'Waiting on ' + t.urg + ' only makes the repair bigger. ' + biz + ' can look at it fast.') +
             '\n\nCall or message ' + biz + ' today.' }
      ] : [
        { k: 'Post 1 — Recordatorio de servicio',
          h: t.s[0].charAt(0).toUpperCase() + t.s[0].slice(1) + ' en ' + city,
          b: '¿Necesitas ' + t.s[0] + ' en ' + city + '? En ' + biz + ' contestamos, llegamos y te decimos el precio antes de empezar. Sin sorpresas en la cuenta.\n\nAtendemos ' + city + ' y alrededores. Escríbenos y hoy mismo te decimos si podemos ayudarte.' },
        { k: 'Post 2 — Consejo útil',
          h: 'Un consejo que te ahorra dinero',
          b: t.tip + '\n\nCada semana subimos uno de estos. Y si prefieres que alguien lo revise, en ' + biz + ' estamos a un mensaje.' },
        { k: 'Post 3 — Trabajo reciente',
          h: 'Trabajo reciente en ' + city,
          b: fill(t.job) + '\n\nDe cada trabajo tomamos fotos de antes y después. Pídenos las que se parezcan al tuyo.' },
        { k: 'Post 4 — ' + (offer ? 'Oferta' : 'Urgencia'),
          h: offer ? offer : 'No dejes pasar ' + t.urg,
          b: (offer
              ? offer + ' para clientes de ' + city + '. Menciona esta publicación cuando nos escribas.'
              : 'Dejar pasar ' + t.urg + ' solo hace la reparación más cara. En ' + biz + ' lo revisamos rápido.') +
             '\n\nLlama o escribe hoy a ' + biz + '.' }
      ];

      var box = $('#pOut', root); box.innerHTML = '';
      posts.forEach(function (p) {
        var d = document.createElement('div');
        d.className = 'out';
        d.innerHTML = '<p class="out__k">' + p.k + '</p>' +
          '<button class="copy" type="button">' + T('COPIAR', 'COPY') + '</button>' +
          '<p data-copy><strong>' + p.h + '</strong>\n\n' + p.b + '</p>';
        box.appendChild(d);
      });
      $('#pResult', root).hidden = false;

      var link = $('#pWA', root);
      link.setAttribute('data-msg-es', 'Hola MAPA. Usé el generador de publicaciones para ' + biz + ' en ' + city + '. Me gustaría que ustedes se encarguen de las 4 publicaciones al mes y de las fotos.');
      link.setAttribute('data-msg-en', 'Hi MAPA. I used the post generator for ' + biz + ' in ' + city + '. I would like you to handle the 4 monthly posts and the photos.');
      MAPA.refreshWA();
    }
    $('#pRun', root).addEventListener('click', build);
    document.addEventListener('mapa:lang', function () { if (!$('#pResult', root).hidden) build(); });
  }

  /* =====================================================================
     4. RESPUESTAS A RESEÑAS
     ===================================================================== */
  function initReviews(root) {
    $('#rRun', root).addEventListener('click', function () {
      var lang = MAPA.lang();
      var stars = parseInt($('#rStars', root).value, 10);
      var name = ($('#rName', root).value || '').trim();
      var biz = ($('#rBiz', root).value || '').trim() || T('nuestro equipo', 'our team');
      var svc = ($('#rSvc', root).value || '').trim() || T('el servicio', 'the service');
      var note = ($('#rNote', root).value || '').trim();
      var hi = name ? (lang === 'en' ? 'Hi ' + name + ',' : 'Hola ' + name + ',') : (lang === 'en' ? 'Hi,' : 'Hola,');
      var out = [];

      if (stars >= 4) {
        out = lang === 'en' ? [
          { k: 'Warm', t: hi + ' thank you for taking the time to write this. Knowing ' + svc + ' went well is exactly why we do this. If anything comes up later, you know where to find us. — ' + biz },
          { k: 'Specific', t: hi + ' we appreciate you mentioning ' + svc + '. That part is where we put the most care, so it means a lot that you noticed. Thank you for trusting ' + biz + '.' },
          { k: 'Referral-friendly', t: hi + ' thank you. Reviews like yours are how neighbors find us, and we do not take that lightly. If someone you know needs ' + svc + ', send them our way. — ' + biz }
        ] : [
          { k: 'Cercana', t: hi + ' gracias por tomarse el tiempo de escribir esto. Saber que ' + svc + ' salió bien es justo por lo que hacemos este trabajo. Si más adelante se ofrece algo, aquí estamos. — ' + biz },
          { k: 'Específica', t: hi + ' le agradecemos que mencione ' + svc + '. Es la parte a la que le ponemos más cuidado, así que significa mucho que lo haya notado. Gracias por confiar en ' + biz + '.' },
          { k: 'Para recomendación', t: hi + ' muchas gracias. Reseñas como la suya son la forma en que los vecinos nos encuentran, y eso no lo tomamos a la ligera. Si conoce a alguien que necesite ' + svc + ', mándelo con nosotros. — ' + biz }
        ];
      } else if (stars === 3) {
        out = lang === 'en' ? [
          { k: 'Own the gap', t: hi + ' thank you for the honest feedback. Three stars tells us ' + svc + ' was acceptable but not what we aim for' + (note ? ', and you are right about ' + note.toLowerCase() : '') + '. We would like to make it right. — ' + biz },
          { k: 'Invite offline', t: hi + ' we appreciate you telling us. We would rather hear this than not. Please reach out directly so we can go over ' + svc + ' and fix what fell short. — ' + biz }
        ] : [
          { k: 'Reconocer', t: hi + ' gracias por su honestidad. Tres estrellas nos dicen que ' + svc + ' estuvo aceptable pero no como buscamos' + (note ? ', y tiene razón en lo de ' + note.toLowerCase() : '') + '. Nos gustaría corregirlo. — ' + biz },
          { k: 'Llevar aparte', t: hi + ' le agradecemos que nos lo diga. Preferimos escucharlo a no saberlo. Escríbanos directo para revisar ' + svc + ' y arreglar lo que faltó. — ' + biz }
        ];
      } else {
        out = lang === 'en' ? [
          { k: 'Short and calm', t: hi + ' this is not the experience we want anyone to have with ' + biz + '. ' + (note ? 'You raised ' + note.toLowerCase() + ', and we are looking into it today. ' : 'We are looking into what happened. ') + 'Please contact us directly so we can resolve it.' },
          { k: 'Accountable', t: hi + ' we fell short on ' + svc + ' and we are not going to argue about it here. ' + (note ? 'We are reviewing ' + note.toLowerCase() + ' with the crew that was on site. ' : 'We are reviewing it with the crew that was on site. ') + 'Reach out and we will make it right. — ' + biz },
          { k: 'Facts, no blame', t: hi + ' thank you for the review. Our record of the visit differs from what is described here, so we would like to compare notes directly rather than in public. Please contact ' + biz + ' and we will go through it with you.' }
        ] : [
          { k: 'Corta y serena', t: hi + ' esta no es la experiencia que queremos que nadie tenga con ' + biz + '. ' + (note ? 'Menciona ' + note.toLowerCase() + ' y hoy mismo lo estamos revisando. ' : 'Estamos revisando qué pasó. ') + 'Le pedimos que nos contacte directo para resolverlo.' },
          { k: 'Responsable', t: hi + ' fallamos en ' + svc + ' y no vamos a discutirlo aquí. ' + (note ? 'Estamos revisando lo de ' + note.toLowerCase() + ' con el equipo que estuvo en el lugar. ' : 'Lo estamos revisando con el equipo que estuvo en el lugar. ') + 'Contáctenos y lo corregimos. — ' + biz },
          { k: 'Hechos, sin pleito', t: hi + ' gracias por su reseña. Nuestro registro de la visita no coincide con lo que se describe, así que preferimos comparar la información con usted directamente y no en público. Escríbanos a ' + biz + ' y lo vemos juntos.' }
        ];
      }

      var box = $('#rOut', root); box.innerHTML = '';
      out.forEach(function (o) {
        var d = document.createElement('div');
        d.className = 'out';
        d.innerHTML = '<p class="out__k">' + o.k + '</p><button class="copy" type="button">' + T('COPIAR', 'COPY') + '</button><p data-copy>' + o.t + '</p>';
        box.appendChild(d);
      });
      $('#rResult', root).hidden = false;
    });
  }

  /* =====================================================================
     5. CITACIONES Y NAP
     ===================================================================== */
  var DIRS = [
    ['Google Business Profile', 'https://business.google.com/', 'crítico'],
    ['Apple Business Connect', 'https://businessconnect.apple.com/', 'crítico'],
    ['Bing Places', 'https://www.bingplaces.com/', 'crítico'],
    ['Yelp for Business', 'https://biz.yelp.com/', 'crítico'],
    ['Facebook Page', 'https://www.facebook.com/business', 'crítico'],
    ['Better Business Bureau', 'https://www.bbb.org/', 'alta'],
    ['Angi', 'https://www.angi.com/', 'alta'],
    ['Thumbtack', 'https://www.thumbtack.com/', 'alta'],
    ['Nextdoor Business', 'https://business.nextdoor.com/', 'alta'],
    ['HomeAdvisor', 'https://www.homeadvisor.com/', 'alta'],
    ['Houzz', 'https://www.houzz.com/', 'alta'],
    ['Yellow Pages', 'https://www.yellowpages.com/', 'media'],
    ['Superpages', 'https://www.superpages.com/', 'media'],
    ['Manta', 'https://www.manta.com/', 'media'],
    ['Foursquare', 'https://foursquare.com/', 'media'],
    ['MapQuest', 'https://www.mapquest.com/', 'media'],
    ['Hotfrog', 'https://www.hotfrog.com/', 'media'],
    ['Brownbook', 'https://www.brownbook.net/', 'media'],
    ['Cylex', 'https://www.cylex.us.com/', 'media'],
    ['EZlocal', 'https://ezlocal.com/', 'media'],
    ['ChamberofCommerce.com', 'https://www.chamberofcommerce.com/', 'media'],
    ['Alignable', 'https://www.alignable.com/', 'media'],
    ['Merchant Circle', 'https://www.merchantcircle.com/', 'media'],
    ['Local.com', 'https://www.local.com/', 'media'],
    ['Citysearch', 'https://www.citysearch.com/', 'media'],
    ['Yellowbook', 'https://www.yellowbook.com/', 'media'],
    ['Judy\'s Book', 'https://www.judysbook.com/', 'baja'],
    ['iBegin', 'https://www.ibegin.com/', 'baja'],
    ['Tupalo', 'https://tupalo.com/', 'baja'],
    ['ShowMeLocal', 'https://www.showmelocal.com/', 'baja']
  ];

  function initCitations(root) {
    var list = $('#dirList', root);
    DIRS.forEach(function (d, i) {
      var key = 'mapa_dir_' + i;
      var row = document.createElement('div');
      row.className = 'dirrow';
      var id = 'dir' + i;
      row.innerHTML = '<input type="checkbox" id="' + id + '"><a href="' + d[1] + '" target="_blank" rel="noopener nofollow">' + d[0] + '</a>' +
        '<span class="mono">' + d[2] + '</span>';
      list.appendChild(row);
      var cb = row.querySelector('input');
      cb.checked = MAPA.store.get(key) === '1';
      cb.addEventListener('change', function () {
        MAPA.store.set(key, cb.checked ? '1' : '0');
        prog();
      });
    });

    function prog() {
      var all = $$('#dirList input', root);
      var done = all.filter(function (c) { return c.checked; }).length;
      $('#dirCount', root).textContent = done + ' / ' + all.length;
      $('#dirBar', root).style.width = (done / all.length * 100) + '%';
    }
    prog();

    function nap() {
      var g = function (id) { return ($('#' + id, root).value || '').trim(); };
      var lines = [
        g('nName'),
        g('nStreet') + (g('nSuite') ? ', ' + g('nSuite') : ''),
        g('nCity') + ', ' + g('nState') + ' ' + g('nZip'),
        g('nPhone'),
        g('nSite'),
        g('nHours')
      ].filter(function (l) { return l && l.replace(/[,\s]/g, ''); });
      $('#napOut', root).textContent = lines.join('\n');
      $('#napBox', root).hidden = lines.length < 2;
      var link = $('#citWA', root);
      link.setAttribute('data-msg-es', 'Hola MAPA. Quiero que ustedes construyan y corrijan mis citaciones. Mi NAP es:\n\n' + lines.join('\n'));
      link.setAttribute('data-msg-en', 'Hi MAPA. I want you to build and clean up my citations. My NAP is:\n\n' + lines.join('\n'));
      MAPA.refreshWA();
    }
    $$('#napForm input', root).forEach(function (i) { i.addEventListener('input', nap); });
    nap();

    $('#dirReset', root).addEventListener('click', function () {
      $$('#dirList input', root).forEach(function (c, i) { c.checked = false; MAPA.store.set('mapa_dir_' + i, '0'); });
      prog();
    });
  }

  /* ---------- Arranque ---------- */
  document.addEventListener('DOMContentLoaded', function () {
    if ($('#auditList')) initAudit(document);
    if ($('#calcForm')) initCalc(document);
    if ($('#pOut')) initPosts(document);
    if ($('#rOut')) initReviews(document);
    if ($('#dirList')) initCitations(document);
  });
})();
