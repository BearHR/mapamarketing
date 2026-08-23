# -*- coding: utf-8 -*-
"""Aplica las correcciones pedidas a index.html."""
import pathlib, sys

p = pathlib.Path('/home/claude/mapa/index.html')
s = p.read_text(encoding='utf-8')
n = 0

def rep(old, new):
    global s, n
    if old not in s:
        print('NO ENCONTRADO:', old[:90].replace('\n', ' '))
        sys.exit(1)
    s = s.replace(old, new, 1)
    n += 1

# ---------------------------------------------------------------- 1. HERO SVG
rep('<circle cx="260" cy="260" r="56" fill="#25D366"/>',
    '<circle cx="260" cy="260" r="60" fill="#25D366"/>')
rep('<text class="core-t" x="260" y="256" data-l="en">YOUR SHOP</text>',
    '<text class="core-t core-t--en" x="260" y="256" data-l="en">YOUR BUSINESS</text>')
rep('aria-label="Diagrama: tu negocio al centro conectado a Google Maps, la búsqueda de Google, Apple Maps, Bing Places, Yelp y directorios.">',
    'aria-label="Diagrama: tu negocio al centro conectado a Google Maps, la búsqueda de Google, Apple Maps, Bing Places, Yelp y directorios.">')

# ---------------------------------------------------------------- 2. TIRA DEL HERO
rep('''        <span data-l="es">Sitios rápidos</span><span data-l="en">Fast websites</span>
        <span data-l="es">Cuatro mapas</span><span data-l="en">Four maps</span>
        <span data-l="es">Contenido cada mes</span><span data-l="en">Content every month</span>
        <span data-l="es">En tu idioma</span><span data-l="en">In your language</span>''',
    '''        <span data-l="es">Sitio web rápido</span><span data-l="en">Fast website</span>
        <span data-l="es">Dominio de los mapas</span><span data-l="en">Map domination</span>
        <span data-l="es">Presencia en IA</span><span data-l="en">AI presence</span>''')

# ---------------------------------------------------------------- 3. SERVICIOS: UN PROGRAMA
rep('''      <h2><span data-l="es">Dos cosas. Bien hechas.</span><span data-l="en">Two things. Done properly.</span></h2>
      <p class="lede">
        <span data-l="es">Primero te construimos la base: un sitio que carga rápido y está armado para que Google entienda qué vendes y dónde. Luego lo empujamos cada mes hasta que el mapa te reconoce.</span>
        <span data-l="en">First we build the foundation: a fast site structured so Google understands what you sell and where. Then we push it every month until the map recognizes you.</span>
      </p>''',
    '''      <h2><span data-l="es">Un programa. Dos fases.</span><span data-l="en">One program. Two phases.</span></h2>
      <p class="lede">
        <span data-l="es">Un sitio web solo, sin nada detrás, casi nunca mueve el teléfono. Por eso no vendemos páginas: construimos la base y después la empujamos mes con mes hasta que el mapa te reconoce. <b>El sitio va incluido cuando arrancas con seis meses de trabajo mensual.</b></span>
        <span data-l="en">A website on its own, with nothing behind it, almost never moves the phone. So we don't sell pages: we build the foundation and then push it month after month until the map recognizes you. <b>The site is included when you start with six months of ongoing work.</b></span>
      </p>''')

rep('<span class="offer__tag"><span data-l="es">Pago único</span><span data-l="en">One-time</span></span>',
    '<span class="offer__tag"><span data-l="es">Fase 1 · Incluida</span><span data-l="en">Phase 1 · Included</span></span>')
rep('<span class="offer__tag"><span data-l="es">Cada mes</span><span data-l="en">Every month</span></span>',
    '<span class="offer__tag"><span data-l="es">Fase 2 · Cada mes</span><span data-l="en">Phase 2 · Every month</span></span>')

# Páginas de servicio + ciudad combinadas (estructura correcta)
rep('''          <li><b><span data-l="es">Una página por servicio</span><span data-l="en">A page per service</span></b>
              <span data-l="es">Cada servicio con su propia página, no una lista escondida.</span>
              <span data-l="en">Every service gets its own page, not a buried list.</span></li>
          <li><b><span data-l="es">Una página por ciudad</span><span data-l="en">A page per city</span></b>
              <span data-l="es">Contenido real de cada zona donde trabajas.</span>
              <span data-l="en">Real content for each area you serve.</span></li>''',
    '''          <li><b><span data-l="es">Una página por servicio y ciudad</span><span data-l="en">A page per service and city</span></b>
              <span data-l="es">No una de servicios y otra de ciudades: una para «destape de drenajes en Katy» y otra para «destape de drenajes en Sugar Land». Así es como busca la gente.</span>
              <span data-l="en">Not one services page and one city page: one for "drain cleaning in Katy" and another for "drain cleaning in Sugar Land." That's how people actually search.</span></li>
          <li><b><span data-l="es">Textos escritos para tu cliente</span><span data-l="en">Copy written for your customer</span></b>
              <span data-l="es">Su problema primero, tu historia después.</span>
              <span data-l="en">Their problem first, your history second.</span></li>''')

rep('''             data-msg-es="Hola MAPA, quiero un sitio web nuevo para mi negocio. ¿Me pasan los detalles y el precio?"
             data-msg-en="Hi MAPA, I want a new website for my business. Can you send me details and pricing?">
            <span data-l="es">Pedir detalles y precio</span><span data-l="en">Ask for details and pricing</span>''',
    '''             data-msg-es="Hola MAPA, me interesa el programa completo (sitio web + trabajo mensual). ¿Me pasan los detalles?"
             data-msg-en="Hi MAPA, I'm interested in the full program (website + ongoing work). Can you send me the details?">
            <span data-l="es">Preguntar por el programa</span><span data-l="en">Ask about the program</span>''')

# Entregables mensuales sin números
rep('''          <li><b><span data-l="es">3 artículos al mes</span><span data-l="en">3 articles a month</span></b>
              <span data-l="es">Respuestas a lo que tus clientes buscan de verdad.</span>
              <span data-l="en">Answers to what your customers actually search for.</span></li>
          <li><b><span data-l="es">4 publicaciones en Google</span><span data-l="en">4 Google posts</span></b>
              <span data-l="es">Tu perfil activo, no abandonado desde 2022.</span>
              <span data-l="en">An active profile, not one abandoned since 2022.</span></li>''',
    '''          <li><b><span data-l="es">Artículos nuevos cada mes</span><span data-l="en">New articles every month</span></b>
              <span data-l="es">Respuestas a lo que tus clientes buscan de verdad.</span>
              <span data-l="en">Answers to what your customers actually search for.</span></li>
          <li><b><span data-l="es">Publicaciones en tu Perfil de Google</span><span data-l="en">Posts on your Google profile</span></b>
              <span data-l="es">Tu perfil activo, no abandonado desde 2022.</span>
              <span data-l="en">An active profile, not one abandoned since 2022.</span></li>''')

rep('''          <li><b><span data-l="es">Citaciones</span><span data-l="en">Citations</span></b>
              <span data-l="es">Tus datos idénticos en los directorios que Google consulta.</span>
              <span data-l="en">Your details identical across the directories Google checks.</span></li>
          <li><b><span data-l="es">1 enlace nuevo al mes</span><span data-l="en">1 new backlink a month</span></b>
              <span data-l="es">Conseguido, no comprado. Sitios reales que hablan de ti.</span>
              <span data-l="en">Earned, not bought. Real sites that mention you.</span></li>''',
    '''          <li><b><span data-l="es">Citaciones</span><span data-l="en">Citations</span></b>
              <span data-l="es">Se construyen y se limpian al arrancar, y después solo se mantienen.</span>
              <span data-l="en">Built and cleaned up at the start, then simply maintained.</span></li>
          <li><b><span data-l="es">Enlaces locales</span><span data-l="en">Local links</span></b>
              <span data-l="es">Conseguidos, no comprados, y solo cuando tu zona lo pide.</span>
              <span data-l="en">Earned, not bought, and only when your area calls for it.</span></li>''')

rep('''             data-msg-es="Hola MAPA, me interesa el servicio mensual. ¿Qué incluye exactamente y cuánto es?"
             data-msg-en="Hi MAPA, I'm interested in the monthly service. What exactly is included and how much?">
            <span data-l="es">Preguntar por el plan mensual</span><span data-l="en">Ask about the monthly plan</span>''',
    '''             data-msg-es="Hola MAPA, quiero empezar con el trabajo mensual y el sitio incluido. ¿Cómo funciona?"
             data-msg-en="Hi MAPA, I want to start with the monthly work and the site included. How does it work?">
            <span data-l="es">Quiero empezar</span><span data-l="en">I want to start</span>''')

# Nota de abajo: se sustituye "se pueden contratar por separado"
rep('''    <p class="reveal" style="margin-top:1.4rem;font-size:.92rem;color:var(--muted)">
      <span data-l="es">Los dos servicios se pueden contratar por separado. Ver el <a href="servicios.html">detalle completo de cada uno</a>.</span>
      <span data-l="en">Both services can be hired separately. See the <a href="servicios.html">full breakdown of each</a>.</span>
    </p>''',
    '''    <div class="prose-note reveal" style="margin-top:1.6rem">
      <b><span data-l="es">Por qué van juntas</span><span data-l="en">Why they go together</span></b>
      <span data-l="es">Un sitio nuevo no se posiciona solo: necesita meses de contenido, perfiles cuidados y señales acumulándose. Por eso el sitio web va incluido cuando arrancas con seis meses de trabajo mensual, y por eso no te vamos a vender una página bonita y desearte suerte. Ver el <a href="servicios.html">detalle completo del programa</a>.</span>
      <span data-l="en">A new site doesn't rank on its own: it needs months of content, maintained profiles and signals stacking up. That's why the website is included when you start with six months of ongoing work, and why we won't sell you a pretty page and wish you luck. See the <a href="servicios.html">full program breakdown</a>.</span>
    </div>''')

# ---------------------------------------------------------------- 4. RUTA: PASTILLAS SIN NÚMEROS
rep('''            <span class="pill">3 <span data-l="es">artículos</span><span data-l="en">articles</span></span>
            <span class="pill">4 <span data-l="es">publicaciones</span><span data-l="en">posts</span></span>
            <span class="pill">1 <span data-l="es">enlace</span><span data-l="en">link</span></span>''',
    '''            <span class="pill"><span data-l="es">Artículos</span><span data-l="en">Articles</span></span>
            <span class="pill"><span data-l="es">Publicaciones</span><span data-l="en">Posts</span></span>
            <span class="pill"><span data-l="es">Enlaces</span><span data-l="en">Links</span></span>''')

rep('''          <p><span data-l="es">Contenido, publicaciones, fotos, un enlace nuevo, revisión de mapas de calor y un reporte que puedas entender sin diccionario. Mes tras mes.</span>
             <span data-l="en">Content, posts, photos, a new link, heatmap review, and a report you can read without a dictionary. Month after month.</span></p>''',
    '''          <p><span data-l="es">Contenido, publicaciones, fotos, enlaces cuando hacen falta, revisión de mapas de calor y un reporte que puedas entender sin diccionario. Mes tras mes.</span>
             <span data-l="en">Content, posts, photos, links where they're needed, heatmap review, and a report you can read without a dictionary. Month after month.</span></p>''')

rep('''          <div class="route__meta">
            <span class="pill">Google · Apple · Bing · Yelp</span>
            <span class="pill"><span data-l="es">Citaciones</span><span data-l="en">Citations</span></span>
          </div>''',
    '''          <div class="route__meta">
            <span class="pill">Google · Apple · Bing · Yelp</span>
            <span class="pill"><span data-l="es">Citaciones</span><span data-l="en">Citations</span></span>
            <span class="pill"><span data-l="es">Limpieza de fichas viejas</span><span data-l="en">Old listing cleanup</span></span>
          </div>''')

# ---------------------------------------------------------------- 5. SEÑALES
rep('''          <li><span data-l="es">Una página por servicio y por ciudad</span><span data-l="en">One page per service and per city</span></li>
          <li><span data-l="es">3 artículos al mes sobre lo que preguntan</span><span data-l="en">3 monthly articles on what they ask</span></li>''',
    '''          <li><span data-l="es">Una página por cada servicio en cada ciudad</span><span data-l="en">One page for each service in each city</span></li>
          <li><span data-l="es">Contenido nuevo sobre lo que preguntan</span><span data-l="en">New content on what they ask</span></li>''')

rep('''          <li><span data-l="es">Páginas de ciudad con contenido propio</span><span data-l="en">City pages with their own content</span></li>''',
    '''          <li><span data-l="es">Páginas de servicio y ciudad con contenido propio</span><span data-l="en">Service-and-city pages with their own content</span></li>''')

rep('''          <li><span data-l="es">Un enlace local nuevo cada mes</span><span data-l="en">A new local link every month</span></li>''',
    '''          <li><span data-l="es">Enlaces locales de sitios reales</span><span data-l="en">Local links from real sites</span></li>''')

# ---------------------------------------------------------------- 6. GUÍA: 11 CAPÍTULOS
rep('<span data-l="es">Diez capítulos sobre sitios web, Google, los otros mapas, contenido, enlaces e IA.</span>\n           <span data-l="en">Ten chapters on websites, Google, the other maps, content, links and AI.</span>',
    '<span data-l="es">Once capítulos sobre sitios web, Google, los otros mapas, contenido, enlaces e IA.</span>\n           <span data-l="en">Eleven chapters on websites, Google, the other maps, content, links and AI.</span>')

# ---------------------------------------------------------------- 7. FAQ
rep('''        <div class="faq__a"><span data-l="es">Depende de cuántos servicios y cuántas ciudades tengas que cubrir. No ponemos precios en la página porque un negocio con un servicio en una ciudad y otro con seis servicios en cuatro ciudades no son el mismo trabajo. Escríbenos por WhatsApp, cuéntanos tu caso en dos minutos y te damos el número exacto en la misma conversación. Sin llamadas de descubrimiento ni presentaciones de una hora.</span>
        <span data-l="en">It depends on how many services and how many cities you need covered. We don't put prices on the page because a business with one service in one city and a business with six services in four cities are not the same job. Message us on WhatsApp, tell us your situation in two minutes, and we'll give you the exact number in that same conversation. No discovery calls, no hour-long presentations.</span></div>''',
    '''        <div class="faq__a"><span data-l="es">Hay una cuota mensual y ya está: el sitio web va incluido cuando arrancas con seis meses. El monto depende de cuántos servicios y cuántas ciudades tengas que cubrir, porque un negocio con un servicio en una ciudad y otro con seis servicios en cuatro ciudades no son el mismo trabajo. Escríbenos por WhatsApp, cuéntanos tu caso en dos minutos y te damos el número exacto en la misma conversación. Sin llamadas de descubrimiento ni presentaciones de una hora.</span>
        <span data-l="en">There's a monthly fee and that's it: the website is included when you start with six months. The amount depends on how many services and how many cities you need covered, because a business with one service in one city and a business with six services in four cities are not the same job. Message us on WhatsApp, tell us your situation in two minutes, and we'll give you the exact number in that same conversation. No discovery calls, no hour-long presentations.</span></div>''')

rep('''      <details>
        <summary><span data-l="es">¿En cuánto tiempo veo resultados?</span><span data-l="en">How long until I see results?</span></summary>''',
    '''      <details>
        <summary><span data-l="es">¿Puedo comprar solo el sitio web?</span><span data-l="en">Can I just buy the website?</span></summary>
        <div class="faq__a"><span data-l="es">Preferimos que no, y te decimos por qué con honestidad: un sitio nuevo, por bien hecho que esté, tarda meses en posicionarse y necesita contenido y perfiles trabajándose detrás. Si te entregamos la página y desaparecemos, lo más probable es que en seis meses sigas igual y pienses que el sitio no sirvió. Por eso trabajamos como programa: el sitio va incluido y el trabajo mensual es lo que lo hace rendir. Si tu caso es distinto, escríbenos y lo platicamos.</span>
        <span data-l="en">We'd rather you didn't, and here's the honest reason: a new site, however well built, takes months to rank and needs content and profiles being worked behind it. If we hand you the page and disappear, odds are you'll be in the same place six months later and conclude the site was useless. That's why we work as a program: the site is included and the monthly work is what makes it pay off. If your situation is different, message us and we'll talk it through.</span></div>
      </details>
      <details>
        <summary><span data-l="es">¿En cuánto tiempo veo resultados?</span><span data-l="en">How long until I see results?</span></summary>''')

rep('''        <div class="faq__a"><span data-l="es">No amarramos a nadie con contratos largos. Dicho eso, el trabajo mensual necesita tiempo para dar fruto: si contratas un mes y te sales, no vas a ver nada. Te explicamos los términos exactos por WhatsApp antes de que decidas cualquier cosa.</span>
        <span data-l="en">We don't lock anyone into long contracts. That said, monthly work needs time to pay off: hire for one month and quit and you'll see nothing. We'll walk you through the exact terms on WhatsApp before you decide anything.</span></div>''',
    '''        <div class="faq__a"><span data-l="es">El compromiso inicial es de seis meses, y es lo que hace posible que el sitio web vaya incluido. No es un truco para amarrarte: es el tiempo mínimo en el que el trabajo local empieza a notarse de verdad. Después de esos seis meses sigues mes a mes. Te explicamos los términos exactos por WhatsApp antes de que decidas cualquier cosa.</span>
        <span data-l="en">The initial commitment is six months, and that's what makes including the website possible. It isn't a trick to tie you down: it's the minimum window in which local work genuinely starts to show. After those six months you continue month to month. We'll walk you through the exact terms on WhatsApp before you decide anything.</span></div>''')

p.write_text(s, encoding='utf-8')
print('index.html: %d reemplazos' % n)
