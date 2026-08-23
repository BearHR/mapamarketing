# -*- coding: utf-8 -*-
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from common import page, wa

TOOLS_JS = '<script src="assets/js/tools.js"></script>\n'

def thero(k_es, k_en, h_es, h_en, s_es, s_en):
    return f'''<section class="deep grid-bg sec sec--tight">
  <div class="wrap">
    <p class="legend"><span data-l="es">{k_es}</span><span data-l="en">{k_en}</span></p>
    <h1 style="max-width:18ch;font-size:clamp(2.1rem,1.4rem + 3vw,3.6rem)"><span data-l="es">{h_es}</span><span data-l="en">{h_en}</span></h1>
    <p class="lede"><span data-l="es">{s_es}</span><span data-l="en">{s_en}</span></p>
  </div>
</section>'''

BACK = '''<section class="sec sec--tight tint">
  <div class="wrap" style="text-align:center">
    <p style="color:var(--muted);font-size:.94rem">
      <span data-l="es">Todas nuestras herramientas son gratis y corren en tu navegador. <a href="herramientas.html">Ver las otras cuatro</a> o <a href="guia.html">leer la guía completa</a>.</span>
      <span data-l="en">All our tools are free and run in your browser. <a href="herramientas.html">See the other four</a> or <a href="guia.html">read the full guide</a>.</span>
    </p>
  </div>
</section>'''


# ---------------------------------------------------------------- 01
diag = thero("Herramienta 01", "Tool 01",
  "¿Qué tan visible eres en tu ciudad?",
  "How visible are you in your city?",
  "Dieciocho preguntas de sí o no. Al final tienes una calificación sobre 100, el desglose por área y los seis arreglos que más te van a mover. Nada se guarda ni se manda a nadie.",
  "Eighteen yes-or-no questions. At the end you get a score out of 100, a breakdown by area, and the six fixes that will move you most. Nothing is stored or sent anywhere.") + '''

<section class="sec">
  <div class="wrap" style="max-width:900px">
    <div class="qgrid" id="auditList"></div>
    <div class="btnrow" style="margin-top:1.8rem">
      <button class="btn btn--wa" id="auditRun" type="button">
        <span data-l="es">Ver mi calificación</span><span data-l="en">See my score</span>
      </button>
      <span style="font-size:.85rem;color:var(--muted)">
        <span data-l="es">Las que dejes en blanco cuentan como “No”.</span>
        <span data-l="en">Anything left blank counts as “No”.</span>
      </span>
    </div>

    <div class="result" id="auditResult" hidden>
      <p class="legend"><span data-l="es">Tu resultado</span><span data-l="en">Your result</span></p>
      <div class="score"><span class="score__n" id="auditScore">0</span><span class="score__d">/ 100</span></div>
      <div class="bar"><div class="bar__f" id="auditBar"></div></div>
      <p id="auditVerdict" style="font-size:1.05rem"></p>

      <h3 style="margin-top:2rem;font-size:1.1rem"><span data-l="es">Por área</span><span data-l="en">By area</span></h3>
      <div class="brk" id="auditBreak"></div>

      <div id="auditFixWrap">
        <h3 style="font-size:1.1rem"><span data-l="es">Arregla esto primero, en este orden</span><span data-l="en">Fix these first, in this order</span></h3>
        <ul class="todo" id="auditFixes"></ul>
      </div>

      <a class="btn btn--wa wa" id="auditWA" href="https://wa.me/527711150327"
         data-msg-es="Hola MAPA, hice el diagnóstico en su sitio."
         data-msg-en="Hi MAPA, I took the check on your site.">
        <span data-l="es">Mandar mi resultado por WhatsApp</span><span data-l="en">Send my result on WhatsApp</span>
      </a>
      <p style="font-size:.85rem;color:var(--muted);margin-top:.9rem">
        <span data-l="es">Te contestamos con lo que haríamos primero en tu caso. Sin costo y sin compromiso.</span>
        <span data-l="en">We'll reply with what we'd tackle first in your case. Free, no obligation.</span>
      </p>
    </div>
  </div>
</section>
''' + BACK

page("diagnostico.html",
     "Diagnóstico de visibilidad local gratis | MAPA Marketing",
     "18 preguntas para saber qué tan visible es tu negocio de servicio en Google, Apple Maps, Bing y Yelp. Calificación sobre 100 y lista priorizada de arreglos.",
     diag, extrascript=TOOLS_JS)


# ---------------------------------------------------------------- 02
calc = thero("Herramienta 02", "Tool 02",
  "¿Cuánto vale realmente un cliente nuevo?",
  "What is a new customer actually worth?",
  "La mayoría de los dueños subestima esta cifra, y por eso les parece caro invertir en que los encuentren. Pon tus números y mira lo que representan tres contactos más al mes.",
  "Most owners underestimate this number, which is why getting found feels expensive. Put in your numbers and see what three extra leads a month actually mean.") + '''

<section class="sec">
  <div class="wrap" style="max-width:760px">
    <div id="calcForm">
      <div class="field">
        <label for="cTicket"><span data-l="es">Trabajo promedio (dólares)</span><span data-l="en">Average job (dollars)</span></label>
        <input id="cTicket" type="number" min="0" step="50" value="450" inputmode="numeric">
        <div class="field__hint"><span data-l="es">Lo que cobras en un trabajo típico, no el más grande del año.</span><span data-l="en">What you charge on a typical job, not your biggest one of the year.</span></div>
      </div>
      <div class="field">
        <label for="cClose"><span data-l="es">De cada 100 personas que te contactan, ¿cuántas te contratan?</span><span data-l="en">Out of every 100 people who contact you, how many hire you?</span></label>
        <input id="cClose" type="number" min="1" max="100" step="1" value="40" inputmode="numeric">
      </div>
      <div class="field">
        <label for="cLeads"><span data-l="es">Contactos que recibes hoy al mes</span><span data-l="en">Leads you get per month today</span></label>
        <input id="cLeads" type="number" min="0" step="1" value="12" inputmode="numeric">
      </div>
      <div class="field">
        <label for="cRepeat"><span data-l="es">Trabajos promedio por cliente en su vida (1 si nunca regresan)</span><span data-l="en">Average jobs per customer over their lifetime (1 if they never return)</span></label>
        <input id="cRepeat" type="number" min="1" step="0.5" value="1.5" inputmode="decimal">
        <div class="field__hint"><span data-l="es">Un plomero de emergencia puede poner 1.2. Un jardinero con contrato mensual, mucho más.</span><span data-l="en">An emergency plumber might put 1.2. A landscaper on monthly contract, much more.</span></div>
      </div>
      <button class="btn btn--wa" id="calcRun" type="button">
        <span data-l="es">Calcular</span><span data-l="en">Calculate</span>
      </button>
    </div>

    <div class="result" id="calcResult" hidden>
      <p class="legend"><span data-l="es">Tus números</span><span data-l="en">Your numbers</span></p>
      <p style="font-size:1.05rem">
        <span data-l="es">Cada persona que te contacta vale </span><span data-l="en">Every person who contacts you is worth </span>
        <b id="cPerLead">$0</b>
        <span data-l="es"> en promedio. Hoy tus contactos representan </span><span data-l="en"> on average. Today your leads represent </span>
        <b id="cNow">$0</b>
        <span data-l="es"> al mes.</span><span data-l="en"> per month.</span>
      </p>
      <h3 style="margin-top:1.8rem;font-size:1.1rem"><span data-l="es">Lo que valdrían más contactos</span><span data-l="en">What extra leads would be worth</span></h3>
      <div class="money" id="cOut"></div>
      <p style="font-size:.9rem;color:var(--muted);margin-bottom:1.4rem">
        <span data-l="es">Esto es una estimación con tus propios números, no una promesa de resultados. Sirve para una cosa: decidir si vale la pena que te encuentren.</span>
        <span data-l="en">This is an estimate built from your own numbers, not a promise of results. It's good for one thing: deciding whether being found is worth it.</span>
      </p>
      <a class="btn btn--wa wa" id="calcWA" href="https://wa.me/527711150327"
         data-msg-es="Hola MAPA, corrí la calculadora en su sitio."
         data-msg-en="Hi MAPA, I ran the calculator on your site.">
        <span data-l="es">Mandar mis números por WhatsApp</span><span data-l="en">Send my numbers on WhatsApp</span>
      </a>
    </div>
  </div>
</section>
''' + BACK

page("calculadora.html",
     "Calculadora: cuánto vale un cliente nuevo | MAPA Marketing",
     "Calcula cuánto vale cada contacto para tu negocio de servicio y cuánto representarían tres, seis o doce contactos más al mes.",
     calc, extrascript=TOOLS_JS)


# ---------------------------------------------------------------- 03
posts = thero("Herramienta 03", "Tool 03",
  "Las cuatro publicaciones del mes, en un minuto",
  "This month's four posts, in one minute",
  "Google premia los perfiles activos. Cuatro publicaciones al mes es el ritmo mínimo razonable, y esta herramienta te las escribe: una de servicio, una de consejo, una de trabajo reciente y una de oferta o urgencia.",
  "Google rewards active profiles. Four posts a month is the minimum sensible rhythm, and this writes them for you: one service post, one tip, one recent job, and one offer or urgency post.") + '''

<section class="sec">
  <div class="wrap" style="max-width:800px">
    <div class="field">
      <label for="pTrade"><span data-l="es">Tu oficio</span><span data-l="en">Your trade</span></label>
      <select id="pTrade"></select>
    </div>
    <div class="field">
      <label for="pCity"><span data-l="es">Ciudad principal</span><span data-l="en">Main city</span></label>
      <input id="pCity" type="text" placeholder="Houston" data-ph-es="Houston" data-ph-en="Houston">
    </div>
    <div class="field">
      <label for="pBiz"><span data-l="es">Nombre de tu negocio</span><span data-l="en">Your business name</span></label>
      <input id="pBiz" type="text" data-ph-es="Ej. Servicios Ramírez" data-ph-en="e.g. Ramirez Services" placeholder="Ej. Servicios Ramírez">
    </div>
    <div class="field">
      <label for="pOffer"><span data-l="es">Oferta del mes (opcional)</span><span data-l="en">This month's offer (optional)</span></label>
      <input id="pOffer" type="text" data-ph-es="Ej. Inspección gratis en septiembre" data-ph-en="e.g. Free inspection in September" placeholder="Ej. Inspección gratis en septiembre">
      <div class="field__hint"><span data-l="es">Si lo dejas vacío, la cuarta publicación se escribe con enfoque de urgencia.</span><span data-l="en">Leave it blank and the fourth post is written with an urgency angle.</span></div>
    </div>
    <button class="btn btn--wa" id="pRun" type="button">
      <span data-l="es">Generar las 4 publicaciones</span><span data-l="en">Generate the 4 posts</span>
    </button>

    <div class="result" id="pResult" hidden>
      <p class="legend"><span data-l="es">Listas para copiar</span><span data-l="en">Ready to copy</span></p>
      <p style="font-size:.9rem;color:var(--muted);margin-bottom:1.2rem">
        <span data-l="es">Pégalas en tu Perfil de Negocio de Google, una por semana. A cada una súbele una foto real de tu trabajo: las publicaciones con foto se ven muchísimo más.</span>
        <span data-l="en">Paste them into your Google Business Profile, one per week. Add a real photo of your work to each: posts with photos get seen far more.</span>
      </p>
      <div id="pOut"></div>
      <a class="btn btn--wa wa" id="pWA" href="https://wa.me/527711150327"
         data-msg-es="Hola MAPA, usé el generador de publicaciones."
         data-msg-en="Hi MAPA, I used the post generator.">
        <span data-l="es">Que ustedes las hagan cada mes</span><span data-l="en">Have you do these every month</span>
      </a>
    </div>
  </div>
</section>
''' + BACK

page("publicaciones.html",
     "Generador de publicaciones para el Perfil de Negocio de Google | MAPA Marketing",
     "Genera gratis las cuatro publicaciones mensuales de tu Perfil de Negocio de Google, en español o inglés, adaptadas a tu oficio y tu ciudad.",
     posts, extrascript=TOOLS_JS)


# ---------------------------------------------------------------- 04
rev = thero("Herramienta 04", "Tool 04",
  "Qué contestar a una reseña",
  "What to say to a review",
  "La respuesta no es para quien la escribió: es para los cincuenta que la van a leer antes de decidir a quién llamar. Aquí tienes tres formas de contestar según las estrellas.",
  "The reply isn't for the person who wrote it: it's for the fifty people who'll read it before deciding who to call. Here are three ways to answer depending on the stars.") + '''

<section class="sec">
  <div class="wrap" style="max-width:800px">
    <div class="field">
      <label for="rStars"><span data-l="es">Estrellas que te dieron</span><span data-l="en">Stars they gave you</span></label>
      <select id="rStars">
        <option value="5">5 ★★★★★</option>
        <option value="4">4 ★★★★</option>
        <option value="3">3 ★★★</option>
        <option value="2">2 ★★</option>
        <option value="1">1 ★</option>
      </select>
    </div>
    <div class="field">
      <label for="rName"><span data-l="es">Nombre del cliente (opcional)</span><span data-l="en">Customer's name (optional)</span></label>
      <input id="rName" type="text" data-ph-es="María" data-ph-en="Maria" placeholder="María">
    </div>
    <div class="field">
      <label for="rBiz"><span data-l="es">Nombre de tu negocio</span><span data-l="en">Your business name</span></label>
      <input id="rBiz" type="text" data-ph-es="Ej. Servicios Ramírez" data-ph-en="e.g. Ramirez Services" placeholder="Ej. Servicios Ramírez">
    </div>
    <div class="field">
      <label for="rSvc"><span data-l="es">Qué servicio le diste</span><span data-l="en">What service you provided</span></label>
      <input id="rSvc" type="text" data-ph-es="la instalación del calentador" data-ph-en="the water heater install" placeholder="la instalación del calentador">
    </div>
    <div class="field">
      <label for="rNote"><span data-l="es">De qué se quejó, en pocas palabras (opcional)</span><span data-l="en">What they complained about, briefly (optional)</span></label>
      <input id="rNote" type="text" data-ph-es="la demora del segundo día" data-ph-en="the delay on the second day" placeholder="la demora del segundo día">
    </div>
    <button class="btn btn--wa" id="rRun" type="button">
      <span data-l="es">Escribir respuestas</span><span data-l="en">Write replies</span>
    </button>

    <div class="result" id="rResult" hidden>
      <p class="legend"><span data-l="es">Tres opciones</span><span data-l="en">Three options</span></p>
      <p style="font-size:.9rem;color:var(--muted);margin-bottom:1.2rem">
        <span data-l="es">Léelas, escoge una y cámbiale lo que haga falta para que suene a ti. Contesta en menos de 48 horas y nunca discutas los detalles del caso en público.</span>
        <span data-l="en">Read them, pick one, and adjust it so it sounds like you. Reply within 48 hours and never argue case details in public.</span>
      </p>
      <div id="rOut"></div>
      <div class="prose-note">
        <b><span data-l="es">Regla de oro</span><span data-l="en">Rule of thumb</span></b>
        <span data-l="es">Nunca menciones datos privados del cliente en una respuesta pública, y nunca ofrezcas dinero a cambio de que borre la reseña. Invita a seguir la conversación en privado y ahí resuélvelo.</span>
        <span data-l="en">Never mention a customer's private details in a public reply, and never offer money to have a review removed. Invite them to continue privately and resolve it there.</span>
      </div>
      ''' + wa("Hola MAPA, quiero que ustedes se encarguen de responder mis reseñas y de pedirlas a mis clientes.",
               "Hi MAPA, I want you to handle replying to my reviews and requesting them from customers.",
               "Que ustedes lo manejen", "Have you handle it") + '''
    </div>
  </div>
</section>
''' + BACK

page("resenas.html",
     "Cómo responder reseñas: generador gratis | MAPA Marketing",
     "Genera respuestas a reseñas de 1 a 5 estrellas, en español o inglés, para tu Perfil de Negocio de Google o Yelp.",
     rev, extrascript=TOOLS_JS)


# ---------------------------------------------------------------- 05
def fld(i, es, en, ph="", t="text"):
    return f'''<div class="field">
  <label for="{i}"><span data-l="es">{es}</span><span data-l="en">{en}</span></label>
  <input id="{i}" type="{t}" placeholder="{ph}">
</div>'''

cit = thero("Herramienta 05", "Tool 05",
  "Un solo formato de datos. En todos lados.",
  "One data format. Everywhere.",
  "Si tu teléfono aparece de tres maneras distintas en internet, Google no sabe cuál eres tú. Aquí armas tu bloque oficial y llevas el control de los treinta directorios donde deberías estar.",
  "If your phone number appears three different ways online, Google doesn't know which one is you. Build your official block here and track the thirty directories you should be listed in.") + '''

<section class="sec">
  <div class="wrap" style="max-width:860px">
    <div class="sechead">
      <h2 style="font-size:clamp(1.4rem,1.2rem + 1vw,1.9rem)"><span data-l="es">1. Tu bloque NAP oficial</span><span data-l="en">1. Your official NAP block</span></h2>
      <p style="color:var(--muted);font-size:.95rem">
        <span data-l="es">NAP significa nombre, dirección y teléfono. Escríbelo una vez, exactamente como quieres que aparezca en todos lados, y no lo cambies nunca. Escribe la calle completa (“Avenue”, no “Ave.”) y el teléfono siempre en el mismo formato.</span>
        <span data-l="en">NAP means name, address and phone. Write it once, exactly as you want it everywhere, and never change it. Spell the street out (“Avenue”, not “Ave.”) and keep the phone in one consistent format.</span>
      </p>
    </div>
    <div id="napForm">
      ''' + fld("nName", "Nombre exacto del negocio", "Exact business name", "Ramirez Plumbing LLC") + fld(
             "nStreet", "Calle y número", "Street address", "1420 Bellaire Boulevard") + fld(
             "nSuite", "Suite o local (opcional)", "Suite or unit (optional)", "Suite 210") + '''
      <div class="tiles tiles--3" style="gap:.9rem">
        ''' + fld("nCity", "Ciudad", "City", "Houston") + fld("nState", "Estado", "State", "TX") + fld("nZip", "Código postal", "ZIP", "77081") + '''
      </div>
      ''' + fld("nPhone", "Teléfono (un solo formato)", "Phone (one single format)", "(713) 555-0142", "tel") + fld(
             "nSite", "Sitio web", "Website", "https://") + fld(
             "nHours", "Horario", "Hours", "Mon–Sat 7:00 AM – 7:00 PM") + '''
    </div>

    <div class="out" id="napBox" hidden style="margin-top:1.2rem">
      <h4><span data-l="es">Copia esto y pégalo igual en cada directorio</span><span data-l="en">Copy this and paste it identically into every directory</span></h4>
      <button class="copy" type="button">COPY</button>
      <p id="napOut" data-copy></p>
    </div>

    <hr class="rule">

    <div class="sechead">
      <h2 style="font-size:clamp(1.4rem,1.2rem + 1vw,1.9rem)"><span data-l="es">2. Los treinta directorios</span><span data-l="en">2. The thirty directories</span></h2>
      <p style="color:var(--muted);font-size:.95rem">
        <span data-l="es">En orden de importancia. Empieza por los cinco críticos y no bajes hasta terminarlos. Tus marcas se guardan en este navegador.</span>
        <span data-l="en">In order of importance. Start with the five critical ones and don't move down until they're done. Your checkmarks are saved in this browser.</span>
      </p>
    </div>
    <div style="display:flex;align-items:center;gap:1rem;margin-bottom:1rem">
      <span class="mono" id="dirCount">0 / 30</span>
      <div class="bar" style="flex:1;margin:0"><div class="bar__f" id="dirBar"></div></div>
      <button class="btn btn--ghost btn--sm" id="dirReset" type="button"><span data-l="es">Reiniciar</span><span data-l="en">Reset</span></button>
    </div>
    <div class="dirlist" id="dirList"></div>

    <div class="prose-note" style="margin-top:2rem">
      <b><span data-l="es">Lo más importante</span><span data-l="en">The most important part</span></b>
      <span data-l="es">No basta con darte de alta: hay que buscar y corregir las fichas viejas que ya existen con datos equivocados. Ese trabajo de limpieza suele valer más que veinte altas nuevas.</span>
      <span data-l="en">Signing up isn't enough: you have to hunt down and correct old listings that already exist with wrong data. That cleanup work is usually worth more than twenty new signups.</span>
    </div>

    <a class="btn btn--wa wa" id="citWA" href="https://wa.me/527711150327"
       data-msg-es="Hola MAPA, quiero que ustedes construyan y corrijan mis citaciones."
       data-msg-en="Hi MAPA, I want you to build and clean up my citations.">
      <span data-l="es">Que ustedes lo hagan por mí</span><span data-l="en">Have you do it for me</span>
    </a>
  </div>
</section>
''' + BACK

page("citaciones.html",
     "Citaciones y datos NAP: lista de 30 directorios | MAPA Marketing",
     "Arma tu bloque NAP consistente y lleva el control de los 30 directorios donde tu negocio de servicio debería estar listado en Estados Unidos.",
     cit, extrascript=TOOLS_JS)
