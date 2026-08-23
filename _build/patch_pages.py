# -*- coding: utf-8 -*-
"""Correcciones a los generadores: programa combinado, sin cifras concretas,
y estructura correcta de páginas (servicio + ciudad)."""
import pathlib, sys

BASE = pathlib.Path('/home/claude/mapa/_build')
count = 0

def patch(fname, pairs):
    global count
    p = BASE / fname
    s = p.read_text(encoding='utf-8')
    for old, new in pairs:
        if old not in s:
            print('NO ENCONTRADO en %s: %s' % (fname, old[:100].replace('\n', ' ')))
            sys.exit(1)
        s = s.replace(old, new, 1)
        count += 1
    p.write_text(s, encoding='utf-8')


# =====================================================================
# pages.py — SERVICIOS
# =====================================================================
patch('pages.py', [
    # --- hero de servicios
    ("""    "Dos servicios. Uno construye la base, el otro la mantiene creciendo. Se pueden contratar juntos o por separado, y aquí está exactamente qué incluye cada uno.",
    "Two services. One builds the foundation, the other keeps it growing. Hire them together or separately, and here's exactly what each one includes." """.rstrip() + "\n",
     """    "Un programa en dos fases. La primera construye la base, la segunda la hace rendir. El sitio web va incluido cuando arrancas con seis meses de trabajo mensual, y aquí está exactamente qué pasa en cada fase.",
    "One program in two phases. The first builds the foundation, the second makes it pay off. The website is included when you start with six months of ongoing work, and here's exactly what happens in each phase."
"""),

    # --- etiqueta fase 1
    ('<span data-l="es">Servicio 01 · Pago único</span><span data-l="en">Service 01 · One-time</span>',
     '<span data-l="es">Fase 1 · Incluida en el programa</span><span data-l="en">Phase 1 · Included in the program</span>'),

    # --- bloque 01: estructura correcta
    ('"Antes de escoger un color decidimos qué páginas van a existir. Una por cada servicio que vendes, una por cada ciudad donde trabajas, y las de apoyo: sobre el negocio, área de servicio, reseñas, contacto.",\n  "Before picking a color we decide which pages will exist. One per service you sell, one per city you serve, plus the support pages: about, service area, reviews, contact.",',
     '"Antes de escoger un color decidimos qué páginas van a existir. Y no son una de servicios y otra de ciudades: es una página para cada servicio en cada ciudad. Destape de drenajes en Katy. Destape de drenajes en Sugar Land. Calentadores en Katy. Más las de apoyo: sobre el negocio, reseñas y contacto.",\n  "Before picking a color we decide which pages will exist. And it isn\'t one services page plus one city page: it\'s one page for each service in each city. Drain cleaning in Katy. Drain cleaning in Sugar Land. Water heaters in Katy. Plus the support pages: about, reviews and contact.",'),

    ('"Google no puede mandar a alguien que busca «destape de drenaje en Katy» a una página que dice «servicios generales». Necesita una página que trate exactamente de eso.",\n  "Google can\'t send someone searching “drain cleaning in Katy” to a page that says “general services.” It needs a page about exactly that.")',
     '"Google no puede mandar a alguien que busca «destape de drenaje en Katy» a una página que dice «servicios generales», ni a una que solo habla de Katy en general. Necesita una página que trate exactamente de ese servicio en esa ciudad, y esa es la que se lleva la llamada.",\n  "Google can\'t send someone searching “drain cleaning in Katy” to a page that says “general services,” or to one that just talks about Katy in general. It needs a page about exactly that service in that city, and that\'s the page that takes the call.")'),

    # --- entrega final fase 1
    ('<span data-l="es">El sitio en línea, el dominio y el hospedaje a tu nombre, los accesos completos, la medición conectada y una llamada por WhatsApp donde te explicamos cómo editarlo tú mismo si quieres. Es tuyo. Pago único.</span>',
     '<span data-l="es">El sitio en línea, el dominio y el hospedaje a tu nombre, los accesos completos, la medición conectada y una explicación por WhatsApp de cómo editarlo tú mismo si quieres. Es tuyo desde el primer día.</span>'),
    ("<span data-l=\"en\">The site live, the domain and hosting in your name, full access credentials, analytics connected, and a WhatsApp walkthrough on how to edit it yourself if you want. It's yours. One payment.</span>",
     "<span data-l=\"en\">The site live, the domain and hosting in your name, full access credentials, analytics connected, and a WhatsApp walkthrough on how to edit it yourself if you want. It's yours from day one.</span>"),

    ('''      "Hola MAPA, quiero un sitio web nuevo. ¿Cuánto sería para mi negocio?",
      "Hi MAPA, I want a new website. How much would it be for my business?",
      "Pedir precio del sitio", "Ask about website pricing")''',
     '''      "Hola MAPA, me interesa el programa completo. ¿Me explican cómo funciona lo del sitio incluido?",
      "Hi MAPA, I'm interested in the full program. Can you explain how the included website works?",
      "Preguntar por el programa", "Ask about the program")'''),

    # --- etiqueta fase 2
    ('<span data-l="es">Servicio 02 · Cada mes</span><span data-l="en">Service 02 · Monthly</span>',
     '<span data-l="es">Fase 2 · Cada mes</span><span data-l="en">Phase 2 · Every month</span>'),

    # --- tiles mensuales sin cifras
    ('<h3><span data-l="es">3 artículos al mes</span><span data-l="en">3 articles a month</span></h3>',
     '<h3><span data-l="es">Artículos nuevos cada mes</span><span data-l="en">New articles every month</span></h3>'),

    ('<h3><span data-l="es">4 publicaciones y perfil optimizado</span><span data-l="en">4 posts and profile optimization</span></h3>',
     '<h3><span data-l="es">Publicaciones y perfil optimizado</span><span data-l="en">Posts and profile optimization</span></h3>'),
    ('<p><span data-l="es">Cuatro publicaciones al mes en tu Perfil de Negocio, cada una con foto y llamada a la acción. Y una revisión continua de lo que decide el ranking:',
     '<p><span data-l="es">Publicaciones periódicas en tu Perfil de Negocio, cada una con foto y llamada a la acción. Y una revisión continua de lo que decide el ranking:'),
    ('<span data-l="en">Four posts a month on your Business Profile, each with a photo and a call to action. Plus continuous review of what actually decides ranking:',
     '<span data-l="en">Regular posts on your Business Profile, each with a photo and a call to action. Plus continuous review of what actually decides ranking:'),

    ('<span class="tile__n">06 · <span data-l="es">AUTORIDAD</span><span data-l="en">AUTHORITY</span></span>\n        <h3><span data-l="es">Citaciones y 1 enlace al mes</span><span data-l="en">Citations and 1 link a month</span></h3>',
     '<span class="tile__n">06 · <span data-l="es">AUTORIDAD</span><span data-l="en">AUTHORITY</span></span>\n        <h3><span data-l="es">Citaciones y enlaces locales</span><span data-l="en">Citations and local links</span></h3>'),
    ('<p><span data-l="es">Construimos y corregimos tus citaciones (tu nombre, dirección y teléfono en los directorios que Google consulta) y conseguimos un enlace nuevo al mes desde un sitio real: una cámara de comercio, un proveedor, un patrocinio local, una nota de prensa. Uno bueno vale más que cincuenta basura.</span>',
     '<p><span data-l="es">Las citaciones (tu nombre, dirección y teléfono en los directorios que Google consulta) se construyen y se limpian durante los primeros meses; después solo se vigilan. Los enlaces los conseguimos de sitios reales cuando tu zona lo pide: una cámara de comercio, un proveedor, un patrocinio local, una nota de prensa. No compramos paquetes, y no forzamos enlaces que no necesitas.</span>'),
    ("<span data-l=\"en\">We build and correct your citations (your name, address and phone across the directories Google checks) and earn one new link a month from a real site: a chamber of commerce, a supplier, a local sponsorship, a press mention. One good link beats fifty junk ones.</span>",
     "<span data-l=\"en\">Citations (your name, address and phone across the directories Google checks) get built and cleaned up over the first months; after that they're just monitored. Links we earn from real sites when your area calls for it: a chamber of commerce, a supplier, a local sponsorship, a press mention. We don't buy packages, and we don't force links you don't need.</span>"),

    ('''      "Hola MAPA, quiero saber el costo del servicio mensual.",
      "Hi MAPA, I want to know the cost of the monthly service.",
      "Preguntar por el mensual", "Ask about the monthly plan")''',
     '''      "Hola MAPA, quiero empezar con el programa. Mi negocio es ___ y trabajo en ___.",
      "Hi MAPA, I want to start the program. My business is ___ and I work in ___.",
      "Quiero empezar", "I want to start")'''),

    # --- CTA final de servicios
    ('''cta("¿Cuál de los dos necesitas?", "Which of the two do you need?",
  "Si no estás seguro, mándanos el nombre de tu negocio y tu ciudad. Le echamos un ojo y te decimos por dónde empezaríamos nosotros, aunque no nos contrates.",
  "If you're not sure, send us your business name and your city. We'll take a look and tell you where we'd start, even if you don't hire us.",
  "Hola MAPA. Mi negocio es ___ en ___. No sé si necesito sitio nuevo o el servicio mensual. ¿Me orientan?",
  "Hi MAPA. My business is ___ in ___. I'm not sure if I need a new site or the monthly service. Can you point me?")''',
     '''cta("¿Empezamos?", "Shall we start?",
  "Mándanos el nombre de tu negocio y tu ciudad. Le echamos un ojo, te decimos qué encontramos y te explicamos cómo funciona el programa, aunque al final no nos contrates.",
  "Send us your business name and your city. We'll take a look, tell you what we find and explain how the program works, even if you end up not hiring us.",
  "Hola MAPA. Mi negocio es ___ en ___. Cuéntenme cómo funciona el programa.",
  "Hi MAPA. My business is ___ in ___. Tell me how the program works.")'''),

    # --- descripción meta de servicios
    ('"Qué incluye exactamente nuestro sitio web optimizado y nuestro servicio mensual de SEO local: Google, Apple Maps, Bing, Yelp, contenido, citaciones y enlaces."',
     '"Qué incluye nuestro programa de marketing local: sitio web optimizado incluido más trabajo mensual en Google, Apple Maps, Bing Places, Yelp, contenido, citaciones y enlaces."'),
    ('"Servicios — Sitio web y marketing local mensual | MAPA Marketing"',
     '"El programa — Sitio web incluido y marketing local mensual | MAPA Marketing"'),
])


# =====================================================================
# pages.py — PROCESO
# =====================================================================
patch('pages.py', [
    ('<p><span data-l="es">Sales de esta etapa con una lista clara: por ejemplo seis páginas de servicio, tres de ciudad y cuatro de apoyo, cada una con su título y su objetivo.</span>\n             <span data-l="en">You leave this stage with a clear list: say six service pages, three city pages and four support pages, each with its title and its job.</span></p>',
     '<p><span data-l="es">Sales de esta etapa con una lista clara. Si vendes seis servicios en tres ciudades, no son nueve páginas: son dieciocho páginas de servicio y ciudad, más las de apoyo. Priorizamos las que más dinero te dejan y las construimos en ese orden.</span>\n             <span data-l="en">You leave this stage with a clear list. If you sell six services across three cities, that isn\'t nine pages: it\'s eighteen service-and-city pages, plus the support ones. We prioritize the ones that make you the most money and build in that order.</span></p>'),

    ('<p><span data-l="es">Aquí es donde se gana el mapa. Cada mes: tres artículos, cuatro publicaciones en Google, fotos nuevas en los tres mapas que las aceptan, un enlace nuevo, más citaciones, revisión de mapas de calor y ajustes al sitio.</span>\n             <span data-l="en">This is where the map gets won. Every month: three articles, four Google posts, new photos on the three maps that take them, one new link, more citations, heatmap review and site tweaks.</span></p>',
     '<p><span data-l="es">Aquí es donde se gana el mapa. Cada mes: artículos nuevos, publicaciones en Google, fotos nuevas en los tres mapas que las aceptan, revisión de mapas de calor y ajustes al sitio. Y cuando tu zona lo pide, enlaces locales.</span>\n             <span data-l="en">This is where the map gets won. Every month: new articles, Google posts, fresh photos on the three maps that take them, heatmap review and site tweaks. And when your area calls for it, local links.</span></p>'),

    ('<p><span data-l="es">Leemos los mapas de calor y los datos del mes anterior. Definimos los tres temas del mes y qué se va a ajustar en el sitio.</span><span data-l="en">We read last month\'s heatmaps and data. We pick the month\'s three topics and what gets adjusted on the site.</span></p>',
     '<p><span data-l="es">Leemos los mapas de calor y los datos del mes anterior. Definimos los temas del mes y qué se va a ajustar en el sitio.</span><span data-l="en">We read last month\'s heatmaps and data. We pick the month\'s topics and what gets adjusted on the site.</span></p>'),

    ('<p><span data-l="es">Se escriben y publican los artículos. Salen las primeras dos publicaciones de Google con foto.</span><span data-l="en">Articles get written and published. The first two Google posts go out with photos.</span></p>',
     '<p><span data-l="es">Se escriben y publican los artículos del mes. Empiezan a salir las publicaciones de Google con foto.</span><span data-l="en">The month\'s articles get written and published. Google posts start going out with photos.</span></p>'),

    ('<h3><span data-l="es">Autoridad y reporte</span><span data-l="en">Authority and report</span></h3>\n        <p><span data-l="es">Se cierra el enlace del mes, se suman citaciones nuevas, salen las últimas dos publicaciones y te llega el reporte.</span><span data-l="en">The month\'s link closes, new citations get added, the last two posts go out, and your report arrives.</span></p>',
     '<h3><span data-l="es">Autoridad y reporte</span><span data-l="en">Authority and report</span></h3>\n        <p><span data-l="es">Se cierran los enlaces que estuvieran en marcha, se revisan las citaciones, salen las últimas publicaciones y te llega el reporte.</span><span data-l="en">Any links in progress get closed, citations get checked, the last posts go out, and your report arrives.</span></p>'),

    # tabla de expectativas: quitar cifra implícita de páginas
    ('<td><span data-l="es">El sitio empieza a aparecer para búsquedas de cola larga (preguntas específicas). Los artículos comienzan a traer visitas. El mapa se mueve en las zonas más cercanas a ti.</span>',
     '<td><span data-l="es">El sitio empieza a aparecer para búsquedas de cola larga (preguntas específicas). Los artículos comienzan a traer visitas. El mapa se mueve en las zonas más cercanas a ti.</span>'),
    ('<td><span data-l="es">Es cuando normalmente se nota en el teléfono. Las páginas de servicio y ciudad empiezan a rankear',
     '<td><span data-l="es">Es cuando normalmente se nota en el teléfono. Las páginas de servicio y ciudad empiezan a rankear'),
])


# =====================================================================
# pages.py — HERRAMIENTAS
# =====================================================================
patch('pages.py', [
    ('"Diez capítulos sobre sitios web, el Perfil de Google, Apple Maps, Bing, Yelp, citaciones, contenido, enlaces y cómo aparecer en las respuestas de IA.",\n      "Ten chapters on websites, the Google profile, Apple Maps, Bing, Yelp, citations, content, links and how to show up in AI answers.",',
     '"Once capítulos sobre sitios web, el Perfil de Google, Apple Maps, Bing, Yelp, citaciones, contenido, enlaces y cómo aparecer en las respuestas de IA.",\n      "Eleven chapters on websites, the Google profile, Apple Maps, Bing, Yelp, citations, content, links and how to show up in AI answers.",'),
])

print('%d reemplazos aplicados' % count)
