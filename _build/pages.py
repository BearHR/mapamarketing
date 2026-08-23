# -*- coding: utf-8 -*-
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from common import page, wa

def phero(legend_es, legend_en, h1_es, h1_en, sub_es, sub_en):
    return f'''<section class="deep grid-bg sec sec--tight">
  <div class="wrap">
    <p class="legend"><span data-l="es">{legend_es}</span><span data-l="en">{legend_en}</span></p>
    <h1 style="max-width:16ch"><span data-l="es">{h1_es}</span><span data-l="en">{h1_en}</span></h1>
    <p class="lede"><span data-l="es">{sub_es}</span><span data-l="en">{sub_en}</span></p>
  </div>
</section>'''

def cta(h_es, h_en, p_es, p_en, msg_es, msg_en, b_es="Escribir por WhatsApp", b_en="Message on WhatsApp"):
    return f'''<section class="sec sec--tight">
  <div class="wrap">
    <div class="cta reveal"><div class="cta__in">
      <p class="legend"><span data-l="es">Siguiente paso</span><span data-l="en">Next step</span></p>
      <h2><span data-l="es">{h_es}</span><span data-l="en">{h_en}</span></h2>
      <p><span data-l="es">{p_es}</span><span data-l="en">{p_en}</span></p>
      {wa(msg_es, msg_en, b_es, b_en)}
    </div></div>
  </div>
</section>'''


# =====================================================================
# SERVICIOS
# =====================================================================
def block(n, t_es, t_en, p_es, p_en, why_es, why_en):
    return f'''<div class="route__stop reveal">
  <div class="route__n">{n}</div>
  <div class="route__body">
    <h3><span data-l="es">{t_es}</span><span data-l="en">{t_en}</span></h3>
    <p><span data-l="es">{p_es}</span><span data-l="en">{p_en}</span></p>
    <p style="margin-top:.7rem;font-size:.9rem"><b><span data-l="es">Por qué importa: </span><span data-l="en">Why it matters: </span></b>
      <span data-l="es">{why_es}</span><span data-l="en">{why_en}</span></p>
  </div>
</div>'''

servicios = phero(
    "Servicios", "Services",
    "Todo lo que hacemos, sin letra chica.",
    "Everything we do, no fine print.",
    "Dos servicios. Uno construye la base, el otro la mantiene creciendo. Se pueden contratar juntos o por separado, y aquí está exactamente qué incluye cada uno.",
    "Two services. One builds the foundation, the other keeps it growing. Hire them together or separately, and here's exactly what each one includes."
) + '''

<section class="sec">
  <div class="wrap">
    <div class="sechead reveal">
      <p class="legend"><span data-l="es">Servicio 01 · Pago único</span><span data-l="en">Service 01 · One-time</span></p>
      <h2><span data-l="es">El sitio web</span><span data-l="en">The website</span></h2>
      <p class="lede">
        <span data-l="es">Un sitio de negocio de servicio tiene un solo trabajo: que la persona que llegó buscando ayuda te escriba o te llame. Todo lo demás es decoración. Así lo construimos.</span>
        <span data-l="en">A service business website has one job: get the person who arrived looking for help to message or call you. Everything else is decoration. Here's how we build it.</span>
      </p>
    </div>
    <div class="route">
''' + block("01", "Arquitectura antes que diseño", "Architecture before design",
  "Antes de escoger un color decidimos qué páginas van a existir. Una por cada servicio que vendes, una por cada ciudad donde trabajas, y las de apoyo: sobre el negocio, área de servicio, reseñas, contacto.",
  "Before picking a color we decide which pages will exist. One per service you sell, one per city you serve, plus the support pages: about, service area, reviews, contact.",
  "Google no puede mandar a alguien que busca «destape de drenaje en Katy» a una página que dice «servicios generales». Necesita una página que trate exactamente de eso.",
  "Google can't send someone searching “drain cleaning in Katy” to a page that says “general services.” It needs a page about exactly that.") + block(
  "02", "Textos escritos para tu cliente, no para ti", "Copy written for your customer, not for you",
  "Cada página abre con el problema del cliente, no con la historia de la empresa. Qué haces, en cuánto llegas, qué pasa después de que escribes, cuánto cuesta más o menos.",
  "Every page opens with the customer's problem, not the company's history. What you do, how fast you arrive, what happens after they message, roughly what it costs.",
  "La persona con agua en el piso no quiere leer «fundada en 2011 con pasión por la excelencia». Quiere saber si llegas hoy.",
  "The person with water on the floor doesn't want “founded in 2011 with a passion for excellence.” They want to know if you can come today.") + block(
  "03", "Velocidad en celular", "Mobile speed",
  "Imágenes comprimidas, código mínimo, nada de plantillas infladas con veinte funciones que no usas. Medimos en condiciones reales, con datos móviles, no en una computadora con fibra óptica.",
  "Compressed images, minimal code, none of those bloated templates with twenty features you never use. We measure in real conditions, on mobile data, not on a desktop with fiber.",
  "Cada segundo de carga se lleva visitantes. Y en emergencias, la gente no espera: se regresa al mapa y llama al siguiente.",
  "Every second of load time costs visitors. In an emergency nobody waits: they go back to the map and call the next one.") + block(
  "04", "Diseño que empuja al contacto", "Design that pushes contact",
  "Botón de llamada y de WhatsApp fijos en móvil, visibles sin bajar la pantalla. Formulario corto, no un interrogatorio. Prueba visual: fotos de trabajos reales, tu camioneta, tu equipo.",
  "Call and WhatsApp buttons pinned on mobile, visible without scrolling. A short form, not an interrogation. Visual proof: photos of real jobs, your truck, your crew.",
  "Un sitio bonito que esconde el teléfono es un folleto caro. La conversión se diseña, no se espera.",
  "A pretty site that hides the phone number is an expensive brochure. Conversion is designed, not hoped for.") + block(
  "05", "Estructura técnica para buscadores", "Technical structure for search engines",
  "Títulos y descripciones únicos por página, encabezados en orden, datos estructurados de negocio local, mapa del sitio, imágenes con texto alternativo y URLs limpias.",
  "Unique titles and descriptions per page, headings in order, local business structured data, sitemap, image alt text and clean URLs.",
  "Es la parte que nadie ve y que decide si Google entiende quién eres, qué vendes y dónde. También es de lo que se alimentan las respuestas de IA.",
  "It's the part nobody sees, and it decides whether Google understands who you are, what you sell and where. It's also what AI answers feed on.") + block(
  "06", "Español, inglés o los dos", "Spanish, English or both",
  "Decidimos contigo según a quién le vendes. A veces conviene todo el sitio en inglés con páginas clave en español; a veces al revés. Lo que no hacemos es traducir con un botón automático y dejarlo ahí.",
  "We decide with you based on who you sell to. Sometimes the whole site works in English with key pages in Spanish; sometimes the reverse. What we don't do is slap on an auto-translate widget and walk away.",
  "Un texto mal traducido comunica descuido, y el descuido cuesta trabajos.",
  "Badly translated copy signals carelessness, and carelessness costs jobs.") + '''
    </div>
    <div class="keytake reveal" style="margin-top:2rem">
      <b><span data-l="es">Al final te entregamos</span><span data-l="en">What you end up with</span></b>
      <span data-l="es">El sitio en línea, el dominio y el hospedaje a tu nombre, los accesos completos, la medición conectada y una llamada por WhatsApp donde te explicamos cómo editarlo tú mismo si quieres. Es tuyo. Pago único.</span>
      <span data-l="en">The site live, the domain and hosting in your name, full access credentials, analytics connected, and a WhatsApp walkthrough on how to edit it yourself if you want. It's yours. One payment.</span>
    </div>
    <div class="btnrow reveal" style="margin-top:1.6rem">''' + wa(
      "Hola MAPA, quiero un sitio web nuevo. ¿Cuánto sería para mi negocio?",
      "Hi MAPA, I want a new website. How much would it be for my business?",
      "Pedir precio del sitio", "Ask about website pricing") + '''</div>
  </div>
</section>

<section class="sec dark grid-bg">
  <div class="wrap">
    <div class="sechead reveal">
      <p class="legend"><span data-l="es">Servicio 02 · Cada mes</span><span data-l="en">Service 02 · Monthly</span></p>
      <h2><span data-l="es">Marketing continuo</span><span data-l="en">Ongoing marketing</span></h2>
      <p class="lede">
        <span data-l="es">Tener el sitio hecho es como tener la camioneta rotulada: ya te ven, pero solo si sales a la calle. Esto es lo que hacemos cada mes para que salgas.</span>
        <span data-l="en">Having the site built is like having your truck wrapped: people can see you, but only if you drive out. This is what we do every month so you do.</span>
      </p>
    </div>

    <div class="tiles tiles--2">
      <div class="tile reveal">
        <span class="tile__n">01 · <span data-l="es">SITIO</span><span data-l="en">SITE</span></span>
        <h3><span data-l="es">Mapas de calor y optimización</span><span data-l="en">Heatmaps and optimization</span></h3>
        <p><span data-l="es">Instalamos mapas de calor y grabaciones de sesión para ver exactamente hasta dónde baja la gente, qué botón ignoran y en qué párrafo se aburren. Cada mes movemos algo con base en eso: subir el botón, acortar un texto, cambiar una foto.</span>
           <span data-l="en">We install heatmaps and session recordings to see exactly how far people scroll, which button they ignore, and which paragraph loses them. Every month we change something based on that: move a button up, shorten a block, swap a photo.</span></p>
      </div>
      <div class="tile reveal">
        <span class="tile__n">02 · <span data-l="es">CONTENIDO</span><span data-l="en">CONTENT</span></span>
        <h3><span data-l="es">3 artículos al mes</span><span data-l="en">3 articles a month</span></h3>
        <p><span data-l="es">Escritos sobre preguntas que tus clientes hacen de verdad: cuánto cuesta cambiar un calentador, cómo saber si el techo tiene daño de granizo, cada cuándo hay que limpiar los ductos. Con tu zona y tu forma de trabajar, no texto genérico.</span>
           <span data-l="en">Written around questions your customers actually ask: how much a water heater swap costs, how to spot hail damage on a roof, how often ducts need cleaning. Grounded in your area and how you work, not generic filler.</span></p>
      </div>
      <div class="tile reveal">
        <span class="tile__n">03 · GOOGLE</span>
        <h3><span data-l="es">4 publicaciones y perfil optimizado</span><span data-l="en">4 posts and profile optimization</span></h3>
        <p><span data-l="es">Cuatro publicaciones al mes en tu Perfil de Negocio, cada una con foto y llamada a la acción. Y una revisión continua de lo que decide el ranking: categoría principal, categorías secundarias, lista de servicios, descripción, atributos, horario, área de servicio y preguntas frecuentes.</span>
           <span data-l="en">Four posts a month on your Business Profile, each with a photo and a call to action. Plus continuous review of what actually decides ranking: primary category, secondary categories, service list, description, attributes, hours, service area and Q&amp;A.</span></p>
      </div>
      <div class="tile reveal">
        <span class="tile__n">04 · <span data-l="es">OTROS MAPAS</span><span data-l="en">OTHER MAPS</span></span>
        <h3><span data-l="es">Apple Maps, Bing Places y Yelp</span><span data-l="en">Apple Maps, Bing Places and Yelp</span></h3>
        <p><span data-l="es">Reclamamos y completamos Apple Business Connect (que es lo que ve todo iPhone y todo Siri), Bing Places (que alimenta a varios asistentes de IA) y Yelp, donde mucha gente todavía busca contratistas. Mismos datos, mismas fotos, misma categoría.</span>
           <span data-l="en">We claim and complete Apple Business Connect (what every iPhone and every Siri query sees), Bing Places (which feeds several AI assistants) and Yelp, where plenty of people still look for contractors. Same data, same photos, same category.</span></p>
      </div>
      <div class="tile reveal">
        <span class="tile__n">05 · <span data-l="es">FOTOS</span><span data-l="en">PHOTOS</span></span>
        <h3><span data-l="es">Fotos nuevas cada mes</span><span data-l="en">New photos every month</span></h3>
        <p><span data-l="es">Tú nos mandas fotos por WhatsApp durante el mes; nosotros las limpiamos, les ponemos nombre y datos, y las subimos a Google, Apple Maps y Yelp. Antes y después, equipo trabajando, camioneta, herramienta.</span>
           <span data-l="en">You send us photos over WhatsApp during the month; we clean them up, name and tag them, and upload them to Google, Apple Maps and Yelp. Before and after, crew working, truck, tools.</span></p>
      </div>
      <div class="tile reveal">
        <span class="tile__n">06 · <span data-l="es">AUTORIDAD</span><span data-l="en">AUTHORITY</span></span>
        <h3><span data-l="es">Citaciones y 1 enlace al mes</span><span data-l="en">Citations and 1 link a month</span></h3>
        <p><span data-l="es">Construimos y corregimos tus citaciones (tu nombre, dirección y teléfono en los directorios que Google consulta) y conseguimos un enlace nuevo al mes desde un sitio real: una cámara de comercio, un proveedor, un patrocinio local, una nota de prensa. Uno bueno vale más que cincuenta basura.</span>
           <span data-l="en">We build and correct your citations (your name, address and phone across the directories Google checks) and earn one new link a month from a real site: a chamber of commerce, a supplier, a local sponsorship, a press mention. One good link beats fifty junk ones.</span></p>
      </div>
    </div>

    <div class="keytake reveal" style="margin-top:2rem;background:rgba(239,241,236,.05);border-color:rgba(239,241,236,.15)">
      <b><span data-l="es">Y cada mes recibes</span><span data-l="en">And every month you get</span></b>
      <span data-l="es">Un reporte por WhatsApp con lo que se hizo, cómo se movió tu posición en el mapa, cuántas veces te llamaron o pidieron indicaciones desde Google, y qué sigue el mes que entra. En español si quieres.</span>
      <span data-l="en">A WhatsApp report with what was done, how your map position moved, how many people called or asked for directions from Google, and what's next. In Spanish if you prefer.</span>
    </div>
    <div class="btnrow reveal" style="margin-top:1.6rem">''' + wa(
      "Hola MAPA, quiero saber el costo del servicio mensual.",
      "Hi MAPA, I want to know the cost of the monthly service.",
      "Preguntar por el mensual", "Ask about the monthly plan") + '''</div>
  </div>
</section>

<section class="sec tint">
  <div class="wrap">
    <div class="tiles tiles--2">
      <div class="reveal">
        <p class="legend"><span data-l="es">Tu parte</span><span data-l="en">Your part</span></p>
        <h2 style="font-size:clamp(1.6rem,1.3rem + 1.4vw,2.3rem)"><span data-l="es">Qué necesitamos de ti</span><span data-l="en">What we need from you</span></h2>
        <ul class="deliv">
          <li><b><span data-l="es">Fotos del trabajo</span><span data-l="en">Job photos</span></b><span data-l="es">Con el celular basta. Mándalas por WhatsApp cuando puedas.</span><span data-l="en">Phone quality is fine. Send them over WhatsApp whenever.</span></li>
          <li><b><span data-l="es">Media hora al mes</span><span data-l="en">Half an hour a month</span></b><span data-l="es">Para revisar el reporte y decirnos qué servicio quieres empujar.</span><span data-l="en">To review the report and tell us which service to push.</span></li>
          <li><b><span data-l="es">Que pidas reseñas</span><span data-l="en">That you ask for reviews</span></b><span data-l="es">Nosotros te damos el enlace y el mensaje; el cliente te lo tiene que dar a ti.</span><span data-l="en">We give you the link and the wording; the customer has to give it to you.</span></li>
          <li><b><span data-l="es">Que contestes rápido</span><span data-l="en">That you answer fast</span></b><span data-l="es">Podemos traerte contactos, pero si no contestas en la primera hora se van con otro.</span><span data-l="en">We can bring you leads, but if you don't reply within the hour they go elsewhere.</span></li>
        </ul>
      </div>
      <div class="reveal">
        <p class="legend"><span data-l="es">Lo que no hacemos</span><span data-l="en">What we don't do</span></p>
        <h2 style="font-size:clamp(1.6rem,1.3rem + 1.4vw,2.3rem)"><span data-l="es">Cosas que otros venden y nosotros no</span><span data-l="en">Things others sell and we don't</span></h2>
        <ul class="deliv">
          <li><b><span data-l="es">Reseñas compradas</span><span data-l="en">Bought reviews</span></b><span data-l="es">Es la forma más rápida de perder tu perfil.</span><span data-l="en">The fastest way to lose your profile.</span></li>
          <li><b><span data-l="es">Paquetes de mil enlaces</span><span data-l="en">Thousand-link packages</span></b><span data-l="es">Enlaces basura que hoy no sirven y mañana te penalizan.</span><span data-l="en">Junk links that don't help today and penalize you tomorrow.</span></li>
          <li><b><span data-l="es">Garantías de primer lugar</span><span data-l="en">First-place guarantees</span></b><span data-l="es">Nadie controla el algoritmo. Quien lo garantice, miente.</span><span data-l="en">Nobody controls the algorithm. Anyone guaranteeing it is lying.</span></li>
          <li><b><span data-l="es">Anuncios pagados</span><span data-l="en">Paid ads</span></b><span data-l="es">No es lo nuestro. Nos enfocamos en lo que sigue funcionando cuando dejas de pagar.</span><span data-l="en">Not our thing. We focus on what keeps working after you stop paying.</span></li>
          <li><b><span data-l="es">Contenido inventado por máquina y publicado sin leer</span><span data-l="en">Machine-written content published unread</span></b><span data-l="es">Usamos IA como herramienta, no como reemplazo de saber de qué hablamos.</span><span data-l="en">We use AI as a tool, not as a substitute for knowing the trade.</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>
''' + cta("¿Cuál de los dos necesitas?", "Which of the two do you need?",
  "Si no estás seguro, mándanos el nombre de tu negocio y tu ciudad. Le echamos un ojo y te decimos por dónde empezaríamos nosotros, aunque no nos contrates.",
  "If you're not sure, send us your business name and your city. We'll take a look and tell you where we'd start, even if you don't hire us.",
  "Hola MAPA. Mi negocio es ___ en ___. No sé si necesito sitio nuevo o el servicio mensual. ¿Me orientan?",
  "Hi MAPA. My business is ___ in ___. I'm not sure if I need a new site or the monthly service. Can you point me?")

page("servicios.html",
     "Servicios — Sitio web y marketing local mensual | MAPA Marketing",
     "Qué incluye exactamente nuestro sitio web optimizado y nuestro servicio mensual de SEO local: Google, Apple Maps, Bing, Yelp, contenido, citaciones y enlaces.",
     servicios)


# =====================================================================
# PROCESO
# =====================================================================
proceso = phero(
    "Proceso", "Process",
    "Cómo trabajamos, semana por semana.",
    "How we work, week by week.",
    "Sin misterio y sin vocabulario de agencia. Esto es lo que pasa desde que nos escribes hasta el mes doce.",
    "No mystery and no agency vocabulary. Here's what happens from the moment you message us through month twelve."
) + '''

<section class="sec">
  <div class="wrap">
    <div class="route">
      <div class="route__stop reveal">
        <div class="route__n">00<small><span data-l="es">HOY</span><span data-l="en">TODAY</span></small></div>
        <div class="route__body">
          <h3><span data-l="es">Nos escribes</span><span data-l="en">You message us</span></h3>
          <p><span data-l="es">Por WhatsApp, con el nombre de tu negocio y tu ciudad. Nada de formularios de doce campos ni «agenda una llamada de descubrimiento». Contestamos con preguntas concretas: qué servicios vendes, hasta dónde manejas, si ya tienes sitio y perfil de Google.</span>
             <span data-l="en">On WhatsApp, with your business name and your city. No twelve-field forms, no "book a discovery call." We reply with concrete questions: what services you sell, how far you drive, whether you already have a site and a Google profile.</span></p>
        </div>
      </div>
      <div class="route__stop reveal">
        <div class="route__n">01<small><span data-l="es">DÍA 1–3</span><span data-l="en">DAY 1–3</span></small></div>
        <div class="route__body">
          <h3><span data-l="es">Diagnóstico</span><span data-l="en">Diagnosis</span></h3>
          <p><span data-l="es">Revisamos cuatro cosas: tu sitio (velocidad, estructura, textos), tus perfiles en los cuatro mapas, tus citaciones y tus reseñas, y a los tres negocios que hoy salen arriba de ti cuando alguien busca tu servicio en tu ciudad.</span>
             <span data-l="en">We check four things: your site (speed, structure, copy), your profiles on the four maps, your citations and reviews, and the three businesses currently ranking above you when someone searches your service in your city.</span></p>
          <p><span data-l="es">Te lo mandamos por WhatsApp en lenguaje normal: esto tienes, esto te falta, esto tienen ellos que tú no.</span>
             <span data-l="en">We send it over WhatsApp in plain language: here's what you have, here's what's missing, here's what they have that you don't.</span></p>
          <div class="route__meta"><span class="pill"><span data-l="es">Gratis</span><span data-l="en">Free</span></span><span class="pill"><span data-l="es">Sin compromiso</span><span data-l="en">No obligation</span></span></div>
        </div>
      </div>
      <div class="route__stop reveal">
        <div class="route__n">02<small><span data-l="es">SEMANA 1</span><span data-l="en">WEEK 1</span></small></div>
        <div class="route__body">
          <h3><span data-l="es">El mapa del sitio</span><span data-l="en">The site map</span></h3>
          <p><span data-l="es">Aquí decidimos la estructura: qué páginas se hacen, en qué orden y para qué búsqueda es cada una. Investigamos qué escribe la gente en tu zona, en español y en inglés, porque no siempre buscan lo mismo con las mismas palabras.</span>
             <span data-l="en">Here we lock the structure: which pages get built, in what order, and which search each one targets. We research what people actually type in your area, in both Spanish and English, because they don't always search the same way.</span></p>
          <p><span data-l="es">Sales de esta etapa con una lista clara: por ejemplo seis páginas de servicio, tres de ciudad y cuatro de apoyo, cada una con su título y su objetivo.</span>
             <span data-l="en">You leave this stage with a clear list: say six service pages, three city pages and four support pages, each with its title and its job.</span></p>
        </div>
      </div>
      <div class="route__stop reveal">
        <div class="route__n">03<small><span data-l="es">SEMANAS 2–4</span><span data-l="en">WEEKS 2–4</span></small></div>
        <div class="route__body">
          <h3><span data-l="es">Construcción y revisión</span><span data-l="en">Build and review</span></h3>
          <p><span data-l="es">Escribimos los textos, armamos el diseño y montamos el sitio. A la mitad te mandamos un enlace de vista previa para que lo veas en tu celular y nos digas qué cambiar. No lanzamos nada que no hayas aprobado.</span>
             <span data-l="en">We write the copy, build the design and assemble the site. Halfway through we send a preview link so you can open it on your phone and tell us what to change. Nothing launches without your approval.</span></p>
          <p><span data-l="es">Antes de salir al aire: prueba de velocidad en celular, prueba de que todos los botones marcan bien, y medición conectada para poder contar llamadas y mensajes desde el día uno.</span>
             <span data-l="en">Before going live: mobile speed test, a check that every button dials correctly, and analytics connected so calls and messages get counted from day one.</span></p>
        </div>
      </div>
      <div class="route__stop reveal">
        <div class="route__n">04<small><span data-l="es">SEMANA 4</span><span data-l="en">WEEK 4</span></small></div>
        <div class="route__body">
          <h3><span data-l="es">Distribución en los cuatro mapas</span><span data-l="en">Distribution across the four maps</span></h3>
          <p><span data-l="es">Reclamamos o arreglamos Google, Apple Maps, Bing Places y Yelp. Fijamos un solo formato de nombre, dirección y teléfono, y lo replicamos idéntico en los directorios principales. Donde encontramos datos viejos o duplicados, los corregimos o pedimos que los borren.</span>
             <span data-l="en">We claim or fix Google, Apple Maps, Bing Places and Yelp. We lock one format for name, address and phone, and replicate it identically across the main directories. Where we find stale data or duplicates, we correct them or request removal.</span></p>
        </div>
      </div>
      <div class="route__stop reveal">
        <div class="route__n">05<small><span data-l="es">MES 2 EN ADELANTE</span><span data-l="en">MONTH 2 ONWARD</span></small></div>
        <div class="route__body">
          <h3><span data-l="es">El ritmo mensual</span><span data-l="en">The monthly rhythm</span></h3>
          <p><span data-l="es">Aquí es donde se gana el mapa. Cada mes: tres artículos, cuatro publicaciones en Google, fotos nuevas en los tres mapas que las aceptan, un enlace nuevo, más citaciones, revisión de mapas de calor y ajustes al sitio.</span>
             <span data-l="en">This is where the map gets won. Every month: three articles, four Google posts, new photos on the three maps that take them, one new link, more citations, heatmap review and site tweaks.</span></p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec dark grid-bg">
  <div class="wrap">
    <div class="sechead reveal">
      <p class="legend"><span data-l="es">El calendario</span><span data-l="en">The calendar</span></p>
      <h2><span data-l="es">Cómo se ve un mes cualquiera</span><span data-l="en">What a normal month looks like</span></h2>
    </div>
    <div class="tiles tiles--4">
      <div class="tile reveal"><span class="tile__n"><span data-l="es">SEMANA 1</span><span data-l="en">WEEK 1</span></span>
        <h3><span data-l="es">Revisión y plan</span><span data-l="en">Review and plan</span></h3>
        <p><span data-l="es">Leemos los mapas de calor y los datos del mes anterior. Definimos los tres temas del mes y qué se va a ajustar en el sitio.</span><span data-l="en">We read last month's heatmaps and data. We pick the month's three topics and what gets adjusted on the site.</span></p></div>
      <div class="tile reveal"><span class="tile__n"><span data-l="es">SEMANA 2</span><span data-l="en">WEEK 2</span></span>
        <h3><span data-l="es">Contenido</span><span data-l="en">Content</span></h3>
        <p><span data-l="es">Se escriben y publican los artículos. Salen las primeras dos publicaciones de Google con foto.</span><span data-l="en">Articles get written and published. The first two Google posts go out with photos.</span></p></div>
      <div class="tile reveal"><span class="tile__n"><span data-l="es">SEMANA 3</span><span data-l="en">WEEK 3</span></span>
        <h3><span data-l="es">Mapas y fotos</span><span data-l="en">Maps and photos</span></h3>
        <p><span data-l="es">Suben las fotos del mes a Google, Apple Maps y Yelp. Se revisan categorías, horarios y servicios en los cuatro perfiles.</span><span data-l="en">The month's photos go up on Google, Apple Maps and Yelp. Categories, hours and services get reviewed on all four profiles.</span></p></div>
      <div class="tile reveal"><span class="tile__n"><span data-l="es">SEMANA 4</span><span data-l="en">WEEK 4</span></span>
        <h3><span data-l="es">Autoridad y reporte</span><span data-l="en">Authority and report</span></h3>
        <p><span data-l="es">Se cierra el enlace del mes, se suman citaciones nuevas, salen las últimas dos publicaciones y te llega el reporte.</span><span data-l="en">The month's link closes, new citations get added, the last two posts go out, and your report arrives.</span></p></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap" style="max-width:820px">
    <div class="sechead reveal">
      <p class="legend"><span data-l="es">Expectativas</span><span data-l="en">Expectations</span></p>
      <h2><span data-l="es">Qué esperar mes con mes</span><span data-l="en">What to expect month by month</span></h2>
      <p class="lede"><span data-l="es">Esto es un rango típico del trabajo de SEO local, no una promesa. Tu zona, tu competencia y qué tan seguido contestes el teléfono cambian mucho el resultado.</span>
        <span data-l="en">This is a typical range for local SEO work, not a promise. Your area, your competition and how fast you answer the phone change the outcome a lot.</span></p>
    </div>
    <table class="table reveal">
      <thead><tr>
        <th><span data-l="es">Periodo</span><span data-l="en">Period</span></th>
        <th><span data-l="es">Qué se suele mover</span><span data-l="en">What usually moves</span></th>
      </tr></thead>
      <tbody>
        <tr><td><span data-l="es">Mes 1</span><span data-l="en">Month 1</span></td>
            <td><span data-l="es">Perfiles completos y consistentes. Suele aparecer un aumento en vistas del perfil de Google y en solicitudes de indicaciones, porque el perfil por fin está bien puesto.</span>
                <span data-l="en">Profiles complete and consistent. Google profile views and direction requests often tick up simply because the profile is finally set up correctly.</span></td></tr>
        <tr><td><span data-l="es">Meses 2–3</span><span data-l="en">Months 2–3</span></td>
            <td><span data-l="es">El sitio empieza a aparecer para búsquedas de cola larga (preguntas específicas). Los artículos comienzan a traer visitas. El mapa se mueve en las zonas más cercanas a ti.</span>
                <span data-l="en">The site starts appearing for long-tail searches (specific questions). Articles begin bringing visits. The map moves in the areas closest to you.</span></td></tr>
        <tr><td><span data-l="es">Meses 4–6</span><span data-l="en">Months 4–6</span></td>
            <td><span data-l="es">Es cuando normalmente se nota en el teléfono. Las páginas de servicio y ciudad empiezan a rankear, y la acumulación de reseñas, fotos y enlaces empieza a pesar en el mapa.</span>
                <span data-l="en">This is usually when the phone notices. Service and city pages start ranking, and the accumulation of reviews, photos and links starts to weigh on the map.</span></td></tr>
        <tr><td><span data-l="es">Meses 7–12</span><span data-l="en">Months 7–12</span></td>
            <td><span data-l="es">Se amplía el radio: empiezas a salir en ciudades vecinas donde antes eras invisible. El contenido viejo sigue trayendo visitas sin costo adicional.</span>
                <span data-l="en">The radius widens: you start showing up in neighboring cities where you were invisible. Older content keeps bringing visits at no extra cost.</span></td></tr>
      </tbody>
    </table>
    <div class="prose-note reveal">
      <b><span data-l="es">Importante</span><span data-l="en">Important</span></b>
      <span data-l="es">Si alguien te promete el primer lugar en 30 días, o te garantiza un número exacto de llamadas, está adivinando o mintiendo. Nosotros preferimos decirte el rango real y cumplirlo.</span>
      <span data-l="en">If anyone promises you first place in 30 days, or guarantees an exact number of calls, they're guessing or lying. We'd rather tell you the real range and hit it.</span>
    </div>
  </div>
</section>
''' + cta("¿Empezamos por el diagnóstico?", "Shall we start with the diagnosis?",
  "Es gratis y no compromete a nada. Mándanos el nombre de tu negocio y tu ciudad, y en un par de días te decimos exactamente dónde estás parado.",
  "It's free and commits you to nothing. Send us your business name and your city, and in a couple of days we'll tell you exactly where you stand.",
  "Hola MAPA, quiero el diagnóstico gratis. Mi negocio es ___ y trabajo en ___.",
  "Hi MAPA, I'd like the free diagnosis. My business is ___ and I work in ___.")

page("proceso.html",
     "Proceso — Cómo trabajamos, semana por semana | MAPA Marketing",
     "Del primer mensaje al mes doce: diagnóstico, plan de páginas, construcción del sitio, distribución en cuatro mapas y el ritmo mensual de contenido, fotos y enlaces.",
     proceso)


# =====================================================================
# HERRAMIENTAS (hub)
# =====================================================================
def toolcard(href, k_es, k_en, t_es, t_en, d_es, d_en, go_es, go_en, dark=False):
    style = ' style="background:var(--ink);color:var(--paper);border-color:var(--ink)"' if dark else ''
    h3s = ' style="color:var(--paper)"' if dark else ''
    ps = ' style="color:var(--muted-inv)"' if dark else ''
    gs = ' style="color:var(--wa)"' if dark else ''
    return f'''<a class="toolcard reveal" href="{href}"{style}>
  <span class="toolcard__k"><span data-l="es">{k_es}</span><span data-l="en">{k_en}</span></span>
  <h3{h3s}><span data-l="es">{t_es}</span><span data-l="en">{t_en}</span></h3>
  <p{ps}><span data-l="es">{d_es}</span><span data-l="en">{d_en}</span></p>
  <span class="toolcard__go"{gs}><span data-l="es">{go_es}</span><span data-l="en">{go_en}</span></span>
</a>'''

herramientas = phero(
    "Herramientas", "Tools",
    "Cinco herramientas gratis. Sin correo, sin registro.",
    "Five free tools. No email, no signup.",
    "Todo corre en tu navegador y nada se guarda en nuestros servidores. Úsalas aunque nunca nos escribas: preferimos que un dueño de negocio sepa qué le falta a que no lo sepa nadie.",
    "Everything runs in your browser and nothing is stored on our servers. Use them even if you never message us: we'd rather a business owner know what's missing than nobody know."
) + '''

<section class="sec">
  <div class="wrap">
    <div class="tiles tiles--3">
''' + toolcard("diagnostico.html", "Herramienta 01", "Tool 01",
      "Diagnóstico de visibilidad local", "Local visibility check",
      "18 preguntas sobre tu sitio, tus perfiles, tus reseñas y tus enlaces. Te da una calificación sobre 100, el desglose por área y los seis arreglos más urgentes en orden.",
      "18 questions about your site, profiles, reviews and links. You get a score out of 100, a breakdown by area, and the six most urgent fixes in order.",
      "Hacer el diagnóstico", "Run the check") + toolcard(
      "calculadora.html", "Herramienta 02", "Tool 02",
      "Cuánto vale un cliente nuevo", "What a new customer is worth",
      "Pon tu trabajo promedio y cuántos contactos cierras. Te dice cuánto vale cada contacto y cuánto dinero al año representan tres, seis o doce contactos más al mes.",
      "Enter your average job and how many leads you close. It tells you what each lead is worth and what three, six or twelve extra leads a month mean per year.",
      "Calcular", "Calculate") + toolcard(
      "publicaciones.html", "Herramienta 03", "Tool 03",
      "Generador de publicaciones para Google", "Google Business post writer",
      "Escoge tu oficio y tu ciudad y te arma las cuatro publicaciones del mes para tu Perfil de Negocio, en español o inglés, listas para copiar y pegar.",
      "Pick your trade and your city and it drafts the month's four Business Profile posts, in Spanish or English, ready to copy and paste.",
      "Generar publicaciones", "Generate posts") + toolcard(
      "resenas.html", "Herramienta 04", "Tool 04",
      "Respuestas a reseñas", "Review reply writer",
      "Tres formas distintas de contestar según las estrellas. Especialmente útil para la reseña de una estrella que te dieron ganas de contestar enojado.",
      "Three different ways to reply depending on the stars. Especially useful for the one-star review you felt like answering angry.",
      "Escribir una respuesta", "Write a reply") + toolcard(
      "citaciones.html", "Herramienta 05", "Tool 05",
      "Citaciones y datos NAP", "Citations and NAP",
      "Arma tu bloque oficial de nombre, dirección y teléfono, y lleva el control de treinta directorios donde deberías estar. Se guarda en tu navegador.",
      "Build your official name, address and phone block, and track thirty directories you should be listed in. Saved in your browser.",
      "Abrir la lista", "Open the list") + toolcard(
      "guia.html", "La guía completa", "The full guide",
      "Marketing local, capítulo por capítulo", "Local marketing, chapter by chapter",
      "Diez capítulos sobre sitios web, el Perfil de Google, Apple Maps, Bing, Yelp, citaciones, contenido, enlaces y cómo aparecer en las respuestas de IA.",
      "Ten chapters on websites, the Google profile, Apple Maps, Bing, Yelp, citations, content, links and how to show up in AI answers.",
      "Leer la guía", "Read the guide", dark=True) + '''
    </div>
  </div>
</section>

<section class="sec sec--tight tint">
  <div class="wrap" style="max-width:760px">
    <div class="reveal">
      <p class="legend"><span data-l="es">Por qué las regalamos</span><span data-l="en">Why we give these away</span></p>
      <h2 style="font-size:clamp(1.5rem,1.25rem + 1.3vw,2.2rem)">
        <span data-l="es">Porque el problema nunca fue la información</span>
        <span data-l="en">Because information was never the problem</span></h2>
      <p><span data-l="es">Nada de lo que hacemos es secreto. Está documentado por Google, discutido en foros y explicado en mil videos. El problema es el tiempo: hacer esto bien son entre diez y quince horas al mes, todos los meses, además de correr tu negocio.</span>
         <span data-l="en">None of what we do is secret. Google documents it, forums discuss it, a thousand videos explain it. The problem is time: doing it properly is ten to fifteen hours a month, every month, on top of running your business.</span></p>
      <p><span data-l="es">Si tienes esas horas, tómalas y hazlo tú. Estas herramientas y la guía te sirven igual. Si no las tienes, ya sabes dónde estamos.</span>
         <span data-l="en">If you have those hours, take them and do it yourself. These tools and the guide work the same either way. If you don't, you know where we are.</span></p>
    </div>
  </div>
</section>
''' + cta("¿Prefieres que lo hagamos nosotros?", "Rather have us do it?",
  "Escríbenos con el nombre de tu negocio y tu ciudad. Te decimos qué encontramos y qué haríamos primero.",
  "Message us with your business name and your city. We'll tell you what we find and what we'd do first.",
  "Hola MAPA, usé sus herramientas y prefiero que ustedes se encarguen.",
  "Hi MAPA, I used your tools and I'd rather you handled this.")

page("herramientas.html",
     "Herramientas gratis de marketing local | MAPA Marketing",
     "Cinco herramientas gratuitas para negocios de servicio: diagnóstico de visibilidad local, calculadora de valor por cliente, generador de publicaciones de Google, respuestas a reseñas y control de citaciones NAP.",
     herramientas)


# =====================================================================
# 404
# =====================================================================
notfound = '''<section class="deep grid-bg sec" style="min-height:62vh;display:flex;align-items:center">
  <div class="wrap" style="text-align:center">
    <p class="legend" style="justify-content:center"><span data-l="es">Error 404</span><span data-l="en">Error 404</span></p>
    <h1><span data-l="es">Esta página está fuera del mapa.</span><span data-l="en">This page is off the map.</span></h1>
    <p class="lede" style="margin-inline:auto"><span data-l="es">El enlace no existe o cambió de lugar. Aquí abajo están las salidas.</span>
      <span data-l="en">The link doesn't exist or it moved. The exits are below.</span></p>
    <div class="btnrow" style="justify-content:center;margin-top:2rem">
      <a class="btn btn--ghost" href="index.html"><span data-l="es">Ir al inicio</span><span data-l="en">Go home</span></a>
      <a class="btn btn--ghost" href="herramientas.html"><span data-l="es">Ver herramientas</span><span data-l="en">See tools</span></a>
      ''' + wa("Hola MAPA, buscaba algo en su sitio y no lo encontré.",
               "Hi MAPA, I was looking for something on your site and couldn't find it.",
               "Preguntar por WhatsApp", "Ask on WhatsApp") + '''
    </div>
  </div>
</section>'''

page("404.html", "Página no encontrada | MAPA Marketing",
     "Esta página no existe. Vuelve al inicio o escríbenos por WhatsApp.", notfound)
