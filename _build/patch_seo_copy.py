# -*- coding: utf-8 -*-
"""Encabezados optimizados + pasada de naturalidad en los dos idiomas.

Se aplica sobre los generadores (_build/*.py) y sobre _src/index.html,
para que los cambios sobrevivan a una reconstrucción.
"""
import pathlib, sys

ROOT = pathlib.Path('/home/claude/mapa')
applied = 0
missing = []

def edit(path, pairs, required=True):
    global applied
    p = ROOT / path
    s = p.read_text(encoding='utf-8')
    for old, new in pairs:
        if old in s:
            s = s.replace(old, new, 1)
            applied += 1
        elif required:
            missing.append((path, old[:80].replace('\n', ' ')))
    p.write_text(s, encoding='utf-8')


# =====================================================================
# INDEX — encabezados
# =====================================================================
edit('_src/index.html', [
    # H1: palabra clave al frente, sigue leyéndose como titular
    ('''        <span data-l="es">Tu negocio,<br>primero en <em>el mapa</em>.</span>
        <span data-l="en">Your business,<br>first on <em>the map</em>.</span>''',
     '''        <span data-l="es">SEO local para que salgas<br>primero en <em>el mapa</em></span>
        <span data-l="en">Local SEO that puts you<br>first on <em>the map</em></span>'''),

    # H2 1 — problema
    ('''        <span data-l="es">Haces buen trabajo. El teléfono no lo sabe.</span>
        <span data-l="en">You do good work. The phone doesn't know that.</span>''',
     '''        <span data-l="es">Haces buen trabajo, pero no sales en el mapa de Google</span>
        <span data-l="en">You do good work, but you're not on the Google map</span>'''),

    # H2 2 — servicios
    ('<h2><span data-l="es">Un programa. Dos fases.</span><span data-l="en">One program. Two phases.</span></h2>',
     '<h2><span data-l="es">Sitio web y marketing local en un solo programa</span><span data-l="en">Website and local marketing in one program</span></h2>'),

    # H2 3 — ruta
    ('<h2><span data-l="es">Cinco paradas, en este orden</span><span data-l="en">Five stops, in this order</span></h2>',
     '<h2><span data-l="es">Cómo trabajamos: el proceso en cinco pasos</span><span data-l="en">How we work: the process in five steps</span></h2>'),

    # H2 4 — por qué funciona
    ('''      <h2><span data-l="es">Google decide con tres cosas. Nosotros trabajamos las tres.</span>
          <span data-l="en">Google decides with three things. We work all three.</span></h2>''',
     '''      <h2><span data-l="es">Cómo decide Google quién sale primero en el mapa</span>
          <span data-l="en">How Google decides who shows up first on the map</span></h2>'''),

    # H2 5 — sectores
    ('''      <h2><span data-l="es">Negocios de servicio. Dueños latinos. En Estados Unidos.</span>
          <span data-l="en">Service businesses. Latino owners. In the United States.</span></h2>''',
     '''      <h2><span data-l="es">Para qué negocios de servicio trabajamos</span>
          <span data-l="en">The service businesses we work with</span></h2>'''),

    # H2 6 — herramientas
    ('''      <h2><span data-l="es">Llévate esto gratis, aunque nunca nos escribas</span>
          <span data-l="en">Take this for free, even if you never message us</span></h2>''',
     '''      <h2><span data-l="es">Herramientas y guía gratis de marketing local</span>
          <span data-l="en">Free local marketing tools and guide</span></h2>'''),

    # H2 7 — honestidad
    ('''        <h2><span data-l="es">Somos nuevos. Lo decimos nosotros antes de que lo averigües tú.</span>
            <span data-l="en">We're new. We'd rather say it than have you find out.</span></h2>''',
     '''        <h2><span data-l="es">Somos nuevos y preferimos decírtelo nosotros</span>
            <span data-l="en">We're new, and we'd rather tell you ourselves</span></h2>'''),

    # H2 8 — FAQ
    ('<h2><span data-l="es">Lo que nos preguntan siempre</span><span data-l="en">What we always get asked</span></h2>',
     '<h2><span data-l="es">Preguntas frecuentes</span><span data-l="en">Frequently asked questions</span></h2>'),
])

# =====================================================================
# INDEX — naturalidad
# =====================================================================
edit('_src/index.html', [
    ('<span data-l="es">Construimos y posicionamos el sitio web de negocios de servicio latinos en Estados Unidos. Google, Apple, Bing y Yelp apuntando al mismo lugar: a ti.</span>',
     '<span data-l="es">Hacemos sitios web para negocios de servicio latinos en Estados Unidos y nos encargamos de que Google los encuentre. Google, Apple, Bing y Yelp apuntando al mismo lugar: a ti.</span>'),
    ('<span data-l="en">We build and position websites for Latino-owned service businesses across the United States. Google, Apple, Bing and Yelp all pointing to one place: you.</span>',
     '<span data-l="en">We build websites for Latino-owned service businesses across the US, then do the work to get them found. Google, Apple, Bing and Yelp all pointing to one place: you.</span>'),

    ('<span data-l="es">Dominio de los mapas</span><span data-l="en">Map domination</span>',
     '<span data-l="es">Primero en los mapas</span><span data-l="en">Map domination</span>'),

    # lede del problema: recupera el gancho que quitamos del H2
    ('<span data-l="es">Casi nadie compara diez plomeros. La gente saca el celular, mira los tres primeros del mapa y llama al que se ve más serio. Si no estás ahí, tu calidad no entra a la conversación.</span>',
     '<span data-l="es">Casi nadie compara diez plomeros. La gente saca el celular, mira los tres primeros del mapa y le llama al que se ve más serio. Si no estás ahí, lo bueno que seas trabajando nunca sale a la conversación.</span>'),
    ("<span data-l=\"en\">Almost nobody compares ten plumbers. People pull out a phone, look at the top three on the map, and call whoever looks most solid. If you're not there, your quality never enters the conversation.</span>",
     "<span data-l=\"en\">Almost nobody compares ten plumbers. People pull out their phone, look at the top three on the map, and call whoever looks most solid. If you're not up there, how good you are never comes up.</span>"),

    ('<span data-l="es">Tu perfil activo, no abandonado desde 2022.</span>',
     '<span data-l="es">Un perfil que se ve vivo, no uno que nadie toca desde 2022.</span>'),
    ('<span data-l="en">An active profile, not one abandoned since 2022.</span>',
     '<span data-l="en">A profile that looks alive, not one nobody has touched since 2022.</span>'),

    ('<span data-l="es">El posicionamiento local no se instala, se mantiene. Esto es lo que pasa cada mes.</span>',
     '<span data-l="es">Esto no se instala una vez y ya. Hay que darle de comer todos los meses. Esto es lo que pasa cada uno.</span>'),
    ("<span data-l=\"en\">Local ranking isn't installed, it's maintained. Here's what happens monthly.</span>",
     "<span data-l=\"en\">This isn't something you install once and forget. It needs feeding every month. Here's what that looks like.</span>"),

    ('<span data-l="es">Qué hicimos, qué cambió y qué sigue. Sin gráficas de humo.</span>',
     '<span data-l="es">Qué hicimos, qué cambió y qué sigue. Sin gráficas bonitas que no dicen nada.</span>'),
    ("<span data-l=\"en\">What we did, what changed, what's next. No smoke charts.</span>",
     "<span data-l=\"en\">What we did, what changed, what's next. No pretty charts that say nothing.</span>"),

    ('<span data-l="es">Ese bloque de tres negocios se lleva la mayoría de las llamadas. Aparecer en el lugar catorce es lo mismo que no aparecer.</span>',
     '<span data-l="es">Ese bloque de tres negocios se lleva la mayoría de las llamadas. Salir en el lugar catorce es igual que no salir.</span>'),

    ('<span data-l="es">Un teléfono viejo aquí, una dirección abreviada allá. Google duda de quién eres y te baja.</span>',
     '<span data-l="es">Un teléfono viejo por aquí, la dirección abreviada por allá. Google ya no sabe cuál eres tú, y ante la duda te baja.</span>'),
    ('<span data-l="en">An old phone here, an abbreviated address there. Google doubts who you are and ranks you lower.</span>',
     "<span data-l=\"en\">An old phone number here, a shortened address there. Google stops being sure which one is you, and when it's unsure it ranks you lower.</span>"),

    ('<span data-l="es">Nos especializamos ahí a propósito. Conocemos el mercado, hablamos los dos idiomas y sabemos que tus clientes no son solo los que hablan español.</span>',
     '<span data-l="es">Nos enfocamos ahí a propósito. Conocemos el mercado, trabajamos en los dos idiomas y sabemos que tus clientes no son solo los que hablan español.</span>'),

    ('<span data-l="es">Un sitio web solo, sin nada detrás, casi nunca mueve el teléfono. Por eso no vendemos páginas: construimos la base y después la empujamos mes con mes hasta que el mapa te reconoce. <b>El sitio va incluido cuando arrancas con seis meses de trabajo mensual.</b></span>',
     '<span data-l="es">Un sitio web solo, sin nada detrás, casi nunca hace sonar el teléfono. Por eso no vendemos páginas sueltas: primero armamos la base y luego la empujamos mes con mes hasta que el mapa te toma en serio. <b>El sitio va incluido cuando arrancas con seis meses de trabajo mensual.</b></span>'),
    ("<span data-l=\"en\">A website on its own, with nothing behind it, almost never moves the phone. So we don't sell pages: we build the foundation and then push it month after month until the map recognizes you. <b>The site is included when you start with six months of ongoing work.</b></span>",
     "<span data-l=\"en\">A website on its own, with nothing behind it, almost never makes the phone ring. So we don't sell pages on their own: we build the foundation, then push it month after month until the map takes you seriously. <b>The site is included when you start with six months of ongoing work.</b></span>"),
])


# =====================================================================
# GENERADORES — encabezados de página (H1) y naturalidad
# =====================================================================
edit('_build/pages.py', [
    # H1 servicios
    ('"Todo lo que hacemos, sin letra chica.",\n    "Everything we do, no fine print.",',
     '"Servicios: sitio web y marketing local mensual",\n    "Services: website and monthly local marketing",'),
    # H1 proceso
    ('"Cómo trabajamos, semana por semana.",\n    "How we work, week by week.",',
     '"Nuestro proceso de SEO local, semana por semana",\n    "Our local SEO process, week by week",'),
    # H1 herramientas
    ('"Cinco herramientas gratis. Sin correo, sin registro.",\n    "Five free tools. No email, no signup.",',
     '"Herramientas gratis de SEO local para negocios de servicio",\n    "Free local SEO tools for service businesses",'),
    # sub de herramientas recupera el gancho
    ('"Todo corre en tu navegador y nada se guarda en nuestros servidores. Úsalas aunque nunca nos escribas: preferimos que un dueño de negocio sepa qué le falta a que no lo sepa nadie.",',
     '"Cinco herramientas, sin correo y sin registro. Todo corre en tu navegador y nada se guarda en nuestros servidores. Úsalas aunque nunca nos escribas: preferimos que un dueño de negocio sepa qué le falta a que no lo sepa nadie.",'),
    ('"Everything runs in your browser and nothing is stored on our servers. Use them even if you never message us: we\'d rather a business owner know what\'s missing than nobody know."',
     '"Five tools, no email and no signup. Everything runs in your browser and nothing is stored on our servers. Use them even if you never message us: we\'d rather a business owner know what\'s missing than nobody know."'),
    # naturalidad
    ('"La persona con agua en el piso no quiere leer «fundada en 2011 con pasión por la excelencia». Quiere saber si llegas hoy.",',
     '"A la persona que tiene agua en el piso no le importa leer «fundada en 2011 con pasión por la excelencia». Quiere saber si puedes llegar hoy.",'),
    ('"Un sitio bonito que esconde el teléfono es un folleto caro. La conversión se diseña, no se espera.",',
     '"Un sitio bonito que esconde el teléfono es un folleto caro. Que la gente te escriba se diseña a propósito; no pasa solo.",'),
    ('"A pretty site that hides the phone number is an expensive brochure. Conversion is designed, not hoped for.")',
     '"A pretty site that hides the phone number is an expensive brochure. Getting people to reach out is something you design on purpose; it doesn\'t just happen.")'),
    ('"Tener el sitio hecho es como tener la camioneta rotulada: ya te ven, pero solo si sales a la calle. Esto es lo que hacemos cada mes para que salgas.",',
     '"Tener el sitio hecho es como tener la camioneta rotulada: sirve, pero solo si sales a la calle. Esto es lo que hacemos cada mes para que salgas.",'),
    ('"Es la parte que nadie ve y que decide si Google entiende quién eres, qué vendes y dónde. También es de lo que se alimentan las respuestas de IA.",',
     '"Es la parte que nadie ve y de la que depende que Google entienda quién eres, qué vendes y dónde. También es de donde sacan la información las respuestas de IA.",'),
], required=False)

edit('_build/toolpages.py', [
    ('"¿Qué tan visible eres en tu ciudad?",\n  "How visible are you in your city?",',
     '"Diagnóstico de visibilidad local, gratis",\n  "Free local visibility check",'),
    ('"Dieciocho preguntas de sí o no. Al final tienes una calificación sobre 100, el desglose por área y los seis arreglos que más te van a mover. Nada se guarda ni se manda a nadie.",',
     '"¿Qué tan visible eres hoy en tu ciudad? Dieciocho preguntas de sí o no y, al final, una calificación sobre 100, el desglose por área y los seis arreglos que más te van a mover. Nada se guarda ni se manda a nadie.",'),
    ('"Eighteen yes-or-no questions. At the end you get a score out of 100, a breakdown by area, and the six fixes that will move you most. Nothing is stored or sent anywhere.")',
     '"How visible are you in your city right now? Eighteen yes-or-no questions and, at the end, a score out of 100, a breakdown by area, and the six fixes that will move you most. Nothing is stored or sent anywhere.")'),

    ('"¿Cuánto vale realmente un cliente nuevo?",\n  "What is a new customer actually worth?",',
     '"Calculadora: cuánto vale un cliente nuevo",\n  "Calculator: what a new customer is worth",'),
    ('"La mayoría de los dueños subestima esta cifra, y por eso les parece caro invertir en que los encuentren. Pon tus números y mira lo que representan tres contactos más al mes.",',
     '"Casi todos los dueños se quedan cortos con esta cifra, y por eso les parece caro invertir en que los encuentren. Pon tus números y mira lo que significan tres contactos más al mes.",'),

    ('"Las cuatro publicaciones del mes, en un minuto",\n  "This month\'s four posts, in one minute",',
     '"Generador de publicaciones para el Perfil de Negocio de Google",\n  "Google Business Profile post generator",'),
    ('"Google premia los perfiles activos. Cuatro publicaciones al mes es el ritmo mínimo razonable, y esta herramienta te las escribe: una de servicio, una de consejo, una de trabajo reciente y una de oferta o urgencia.",',
     '"Google le da preferencia a los perfiles activos, y una publicación por semana es un ritmo razonable. Esta herramienta te escribe las del mes en un minuto: una de servicio, una de consejo, una de trabajo reciente y una de oferta o urgencia.",'),
    ('"Google rewards active profiles. Four posts a month is the minimum sensible rhythm, and this writes them for you: one service post, one tip, one recent job, and one offer or urgency post.")',
     '"Google favours profiles that stay active, and one post a week is a sensible rhythm. This writes the month\'s worth in a minute: one service post, one tip, one recent job, and one offer or urgency post.")'),

    ('"Qué contestar a una reseña",\n  "What to say to a review",',
     '"Generador de respuestas a reseñas de Google y Yelp",\n  "Google and Yelp review reply generator",'),
    ('"La respuesta no es para quien la escribió: es para los cincuenta que la van a leer antes de decidir a quién llamar. Aquí tienes tres formas de contestar según las estrellas.",',
     '"La respuesta no es para quien escribió la reseña: es para los cincuenta que la van a leer antes de decidir a quién llamarle. Aquí tienes tres formas de contestar según las estrellas.",'),

    ('"Un solo formato de datos. En todos lados.",\n  "One data format. Everywhere.",',
     '"Citaciones locales y datos NAP: 30 directorios",\n  "Local citations and NAP data: 30 directories",'),
    ('"Si tu teléfono aparece de tres maneras distintas en internet, Google no sabe cuál eres tú. Aquí armas tu bloque oficial y llevas el control de los treinta directorios donde deberías estar.",',
     '"Si tu teléfono aparece de tres maneras distintas en internet, Google deja de saber cuál eres tú. Aquí armas tu bloque oficial de datos y llevas el control de los treinta directorios donde deberías estar.",'),

    # H1 -> H2 en los resultados (no saltar niveles)
    ('<h3 style="margin-top:2rem;font-size:1.1rem"><span data-l="es">Por área</span><span data-l="en">By area</span></h3>',
     '<h2 style="margin-top:2rem;font-size:1.1rem"><span data-l="es">Por área</span><span data-l="en">By area</span></h2>'),
    ('<h3 style="font-size:1.1rem"><span data-l="es">Arregla esto primero, en este orden</span><span data-l="en">Fix these first, in this order</span></h3>',
     '<h2 style="font-size:1.1rem"><span data-l="es">Arregla esto primero, en este orden</span><span data-l="en">Fix these first, in this order</span></h2>'),
    ('<h3 style="margin-top:1.8rem;font-size:1.1rem"><span data-l="es">Lo que valdrían más contactos</span><span data-l="en">What extra leads would be worth</span></h3>',
     '<h2 style="margin-top:1.8rem;font-size:1.1rem"><span data-l="es">Lo que valdrían más contactos</span><span data-l="en">What extra leads would be worth</span></h2>'),
], required=False)

edit('_build/guide.py', [
    ('"Marketing local para negocios de servicio"',
     '"Guía de marketing local para negocios de servicio"'),
    ('"Local marketing for service businesses"',
     '"Local marketing guide for service businesses"'),
    ('<p>Hace quince años, un negocio de servicio vivía de la sección amarilla y de la recomendación del vecino. Hoy la recomendación del vecino sigue mandando, pero pasa por una pantalla: tu vecino te recomienda y la persona <em>igual</em> te busca en Google antes de llamarte. Si no encuentra nada, o encuentra algo abandonado, la recomendación se enfría.</p>',
     '<p>Hace quince años, un negocio de servicio vivía de la sección amarilla y de que el vecino te recomendara. La recomendación del vecino sigue mandando, pero hoy pasa por una pantalla: te recomiendan y la persona <em>de todos modos</em> te busca en Google antes de marcarte. Si no encuentra nada, o encuentra algo abandonado, se le enfría el interés.</p>'),
    ('<p>El error clásico es medir lo que se ve bonito en una gráfica. Visitas al sitio no es un número de negocio. Llamadas sí.</p>',
     '<p>El error clásico es medir lo que se ve bonito en una gráfica. Las visitas al sitio no son un número de negocio. Las llamadas sí.</p>'),
    ('<p>“Hay que hacer un blog” es de los consejos peor ejecutados del marketing local.',
     '<p>“Hay que hacer un blog” es uno de los consejos que peor se ejecutan en el marketing local.'),
], required=False)

print('%d reemplazos aplicados' % applied)
if missing:
    print('NO ENCONTRADOS (%d):' % len(missing))
    for m in missing:
        print('  ', m)
