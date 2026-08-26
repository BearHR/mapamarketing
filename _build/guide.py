# -*- coding: utf-8 -*-
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from common import page, wa
import visuals as V

# En el sitio el fondo es claro: el neutro de las figuras se oscurece un punto
V.PAPER = '#E4E8E0'



SVC_ES = ['Reparación de fugas', 'Destape de drenajes', 'Calentadores']
SVC_EN = ['Leak repair', 'Drain cleaning', 'Water heaters']
CIU = ['Houston', 'Katy', 'Sugar Land']


def fig(es_svg, en_svg, pie_es, pie_en):
    """Una figura por idioma; split.py se queda con la que toca."""
    return ('<div class="figwrap" data-l="es">%s<p class="figcap">%s</p></div>'
            '<div class="figwrap" data-l="en">%s<p class="figcap">%s</p></div>'
            % (es_svg, pie_es, en_svg, pie_en))


def figuras_web():
    return {
        'c1': fig(V.caminos('es') + V.factores('es'), V.caminos('en') + V.factores('en'),
                  'Los cuatro caminos, y los tres factores que ordenan el mapa',
                  'The four paths, and the three factors that order the map'),
        'c2': fig(V.matriz(SVC_ES, CIU, 'es'), V.matriz(SVC_EN, CIU, 'en'),
                  'Servicios por ciudades: de ahí sale tu número de páginas',
                  'Services times cities: that is where your page count comes from'),
        'c5': fig(V.perfil('es'), V.perfil('en'),
                  'Anatomía del Perfil de Negocio de Google',
                  'Anatomy of the Google Business Profile'),
        'c7': fig(V.nap('es'), V.nap('en'),
                  'El mismo negocio, escrito bien y escrito mal',
                  'The same business, written right and written wrong'),
        'c9': fig(V.enlaces('es'), V.enlaces('en'),
                  'Por qué uno bueno le gana a cincuenta comprados',
                  'Why one good link beats fifty bought ones'),
        'c11': fig(V.scorecard('es'), V.scorecard('en'),
                   'El tablero de una hoja, cada mes',
                   'The one-page dashboard, every month'),
    }


CH = []

def ch(cid, t_es, t_en, es, en):
    CH.append((cid, t_es, t_en, es, en))

def note(es, en, msg_es, msg_en, label_es="Que lo hagamos nosotros", label_en="Have us do it"):
    return ('<div class="prose-note"><b><span data-l="es">Cómo lo hacemos nosotros</span>'
            '<span data-l="en">How we handle it</span></b>'
            f'<span data-l="es">{es}</span><span data-l="en">{en}</span><br><br>'
            + wa(msg_es, msg_en, label_es, label_en, cls="btn btn--wa btn--sm", icon=False) + '</div>')

def take(es, en):
    return ('<div class="keytake"><b><span data-l="es">En corto</span><span data-l="en">In short</span></b>'
            f'<span data-l="es">{es}</span><span data-l="en">{en}</span></div>')


# ======================================================= 1
ch("c1", "Cómo te encuentran hoy tus clientes", "How your customers find you today",
"""
<p>Hace quince años, un negocio de servicio vivía de la sección amarilla y de que el vecino te recomendara. La recomendación del vecino sigue mandando, pero hoy pasa por una pantalla: te recomiendan y la persona <em>de todos modos</em> te busca en Google antes de marcarte. Si no encuentra nada, o encuentra algo abandonado, se le enfría el interés.</p>

<h3>Los cuatro caminos</h3>
<p>Cuando alguien en Estados Unidos necesita un plomero, un techero o alguien que le limpie la casa, casi siempre llega por uno de estos cuatro caminos:</p>
<ol>
  <li><b>El mapa.</b> Escribe “plumber near me” y Google le muestra un mapa con tres negocios arriba de todo. Ese bloque de tres se lleva la mayoría de las llamadas. Se llama el paquete local.</li>
  <li><b>Los resultados normales.</b> Debajo del mapa vienen los sitios web. Aquí es donde ganan las páginas que responden preguntas específicas: “cuánto cuesta cambiar un calentador de agua en Houston”.</li>
  <li><b>Los otros mapas.</b> Quien tiene iPhone y le pregunta a Siri no está usando Google: está usando Apple Maps. Quien busca contratistas por costumbre a veces abre Yelp directo.</li>
  <li><b>La IA.</b> Cada vez más gente le pregunta a ChatGPT o al asistente del teléfono. Esas respuestas se arman leyendo mapas, directorios, reseñas y sitios web.</li>
</ol>

<h3>Los tres factores que ordenan el mapa</h3>
<p>Google publica cómo decide el orden del paquete local. Son tres cosas:</p>
<ul>
  <li><b>Relevancia:</b> qué tanto coincide tu negocio con lo que la persona escribió. La categoría de tu perfil y las páginas de tu sitio definen esto.</li>
  <li><b>Distancia:</b> qué tan cerca estás de quien busca, o del lugar que mencionó. No lo controlas del todo, pero sí controlas cómo declaras tu área de servicio.</li>
  <li><b>Prominencia:</b> qué tan conocido eres. Reseñas, menciones en otros sitios, enlaces, consistencia de datos. Es la parte que más se puede trabajar y la que casi nadie trabaja.</li>
</ul>
<p>Todo lo que viene en esta guía empuja una de esas tres palancas. Si algo no empuja ninguna, no lo hagas.</p>

<h3>Una advertencia sobre la impaciencia</h3>
<p>El trabajo del perfil de Google puede moverse en semanas. El posicionamiento del sitio en búsquedas suele tomar de tres a seis meses de trabajo constante. No es lento porque alguien lo esté haciendo mal: es lento porque la prominencia se acumula. Quien te prometa el primer lugar en 30 días te está vendiendo humo.</p>
""",
"""
<p>Fifteen years ago a service business lived off the Yellow Pages and the neighbor's referral. The neighbor's referral still rules, but now it goes through a screen: your neighbor recommends you and the person looks you up on Google <em>anyway</em> before calling. If they find nothing, or find something abandoned, the referral cools off.</p>

<h3>The four paths</h3>
<p>When someone in the United States needs a plumber, a roofer or a house cleaner, they almost always arrive by one of four paths:</p>
<ol>
  <li><b>The map.</b> They type “plumber near me” and Google shows a map with three businesses on top. That block of three takes most of the calls. It's called the local pack.</li>
  <li><b>The regular results.</b> Below the map come the websites. This is where pages that answer specific questions win: “how much to replace a water heater in Houston”.</li>
  <li><b>The other maps.</b> Someone with an iPhone asking Siri isn't using Google: they're using Apple Maps. Someone in the habit of vetting contractors may open Yelp directly.</li>
  <li><b>AI.</b> More and more people ask ChatGPT or their phone assistant. Those answers get assembled by reading maps, directories, reviews and websites.</li>
</ol>

<h3>The three factors that order the map</h3>
<p>Google publishes how it decides local pack order. Three things:</p>
<ul>
  <li><b>Relevance:</b> how well your business matches what the person typed. Your profile category and your site's pages define this.</li>
  <li><b>Distance:</b> how close you are to the searcher, or to the place they named. You don't fully control it, but you do control how you declare your service area.</li>
  <li><b>Prominence:</b> how well known you are. Reviews, mentions on other sites, links, data consistency. It's the most workable part and the part almost nobody works.</li>
</ul>
<p>Everything in this guide pushes one of those three levers. If something pushes none of them, don't do it.</p>

<h3>A warning about impatience</h3>
<p>Google profile work can move in weeks. Ranking the website in search usually takes three to six months of consistent effort. It's not slow because someone is doing it wrong: it's slow because prominence accumulates. Anyone promising first place in 30 days is selling smoke.</p>
""")

# ======================================================= 2
ch("c2", "La estructura de tu sitio", "Your site's structure",
"""
<p>El error más caro que comete un negocio de servicio con su sitio web es tener una sola página llamada “Servicios” con una lista de todo lo que hace. Se siente ordenado. Y es la razón número uno por la que no aparece en búsquedas.</p>
<p>El segundo error más caro es el arreglo que casi todos intentan después: hacer una página por servicio y aparte una página por ciudad. Suena lógico y no funciona.</p>

<h3>La gente no busca un servicio. Busca un servicio en un lugar</h3>
<p>Nadie escribe “destape de drenajes”. Escribe <span class="mono">destape de drenajes en Katy</span>. Y Google manda a la gente a páginas, no a sitios: busca una página que trate exactamente de destapar drenajes en Katy.</p>
<p>Si tienes una página de “destape de drenajes” (que no menciona ninguna ciudad en concreto) y otra de “Katy” (que habla de los seis servicios que ofreces ahí), ninguna de las dos coincide del todo con lo que la persona escribió. Compites a medias en dos frentes en vez de ganar en uno.</p>
<p>La regla real es esta: <b>una página por cada servicio en cada ciudad.</b> Servicios × ciudades. Ese es tu mapa de páginas.</p>

<h3>Cómo se ve una estructura que sí gana</h3>
<pre style="background:var(--paper-2);border:1px solid var(--rule);border-radius:4px;padding:1rem;overflow:auto;font-family:var(--mono);font-size:.8rem;line-height:1.7">Inicio
├── Servicios  (índice, solo para navegar)
│   ├── Destape de drenajes en Houston
│   ├── Destape de drenajes en Katy
│   ├── Destape de drenajes en Sugar Land
│   ├── Reparación de fugas en Houston
│   ├── Reparación de fugas en Katy
│   ├── Reparación de fugas en Sugar Land
│   ├── Calentadores de agua en Houston
│   └── … y así con cada combinación
├── Área de servicio  (mapa general, enlaza a todas)
├── Nosotros
├── Reseñas
└── Blog</pre>
<p>La página de “Servicios” y la de “Área de servicio” siguen existiendo, pero cambian de trabajo: ya no intentan posicionar, solo organizan y enlazan hacia las que sí posicionan.</p>

<h3>Haz la cuenta antes de emocionarte</h3>
<p>Seis servicios en tres ciudades son dieciocho páginas. Ocho servicios en cinco ciudades son cuarenta. Eso es mucho trabajo si cada página tiene que ser buena, y tienen que ser buenas.</p>
<p>Por eso el orden importa más que el volumen:</p>
<ol>
  <li>Empieza por el servicio que más dinero te deja, en la ciudad donde más trabajas. Esa página se hace excelente.</li>
  <li>Luego el mismo servicio en tu segunda y tercera ciudad.</li>
  <li>Luego tu segundo servicio más rentable, en las mismas ciudades.</li>
  <li>Los servicios que casi no vendes pueden esperar, o quedarse dentro del índice sin página propia.</li>
</ol>
<p>Cinco páginas de servicio y ciudad bien hechas valen más que cuarenta plantillas rellenadas.</p>

<h3>El peligro obvio: copiar y cambiar el nombre</h3>
<p>La tentación es escribir “destape de drenajes en Houston”, duplicarla y cambiar Houston por Katy. Eso es contenido duplicado, Google lo detecta sin esfuerzo, y lo que es peor: no convence a nadie que la lea.</p>
<p>Una página de servicio y ciudad que sirve tiene cosas que solo pueden estar en ella:</p>
<ul>
  <li>En cuánto tiempo llegas a esa zona y desde dónde sales.</li>
  <li>Problemas típicos de ahí (casas viejas con tubería de hierro, colonias nuevas con presión baja, agua dura, suelo que se mueve).</li>
  <li>Trabajos de ese servicio hechos en esa ciudad, con foto.</li>
  <li>Reseñas de clientes de esa ciudad.</li>
  <li>Colonias y puntos de referencia que la gente de ahí reconoce.</li>
  <li>Precios o rangos, si aplican distinto por zona.</li>
</ul>
<p>Si no puedes escribir eso sobre una combinación, todavía no deberías tener esa página.</p>

<h3>Cómo se enlazan entre ellas</h3>
<p>Cada página de servicio y ciudad debe enlazar hacia el índice de servicios, hacia el mismo servicio en las ciudades vecinas, y hacia los otros servicios que ofreces en esa misma ciudad. Así una persona que llegó buscando una fuga en Katy encuentra fácil que también cambias calentadores en Katy.</p>
""" + take("Una página por cada servicio en cada ciudad, no una de servicios y otra de ciudades. Empieza por la combinación que más dinero te deja y hazla de verdad, no copiando.",
            "One page for each service in each city, not one services page plus one city page. Start with the combination that makes you the most money and write it properly, not by copying."),
"""
<p>The most expensive mistake a service business makes with its website is having one page called “Services” with a list of everything it does. It feels tidy. And it's the number one reason the site doesn't show up in search.</p>
<p>The second most expensive mistake is the fix almost everyone attempts next: one page per service, plus separate pages per city. It sounds logical and it doesn't work.</p>

<h3>People don't search for a service. They search for a service in a place</h3>
<p>Nobody types “drain cleaning”. They type <span class="mono">drain cleaning in Katy</span>. And Google sends people to pages, not sites: it looks for a page about drain cleaning in Katy specifically.</p>
<p>If you have a “drain cleaning” page (that names no particular city) and a “Katy” page (that covers all six services you offer there), neither one fully matches what the person typed. You compete halfway on two fronts instead of winning on one.</p>
<p>The real rule is this: <b>one page for each service in each city.</b> Services × cities. That's your page map.</p>

<h3>What a structure that actually wins looks like</h3>
<pre style="background:var(--paper-2);border:1px solid var(--rule);border-radius:4px;padding:1rem;overflow:auto;font-family:var(--mono);font-size:.8rem;line-height:1.7">Home
├── Services  (index, for navigation only)
│   ├── Drain cleaning in Houston
│   ├── Drain cleaning in Katy
│   ├── Drain cleaning in Sugar Land
│   ├── Leak repair in Houston
│   ├── Leak repair in Katy
│   ├── Leak repair in Sugar Land
│   ├── Water heaters in Houston
│   └── … and so on for each combination
├── Service area  (overview map, links to all)
├── About
├── Reviews
└── Blog</pre>
<p>The “Services” and “Service area” pages still exist, but their job changes: they're no longer trying to rank, just to organize and link through to the ones that do.</p>

<h3>Do the math before you get excited</h3>
<p>Six services across three cities is eighteen pages. Eight services across five cities is forty. That's a lot of work if every page has to be good, and they do have to be good.</p>
<p>Which is why order matters more than volume:</p>
<ol>
  <li>Start with the service that makes you the most money, in the city you work most. Make that page excellent.</li>
  <li>Then the same service in your second and third cities.</li>
  <li>Then your second most profitable service, in the same cities.</li>
  <li>Services you barely sell can wait, or live inside the index without their own page.</li>
</ol>
<p>Five well-built service-and-city pages beat forty filled-in templates.</p>

<h3>The obvious trap: copy and swap the name</h3>
<p>The temptation is to write “drain cleaning in Houston”, duplicate it, and change Houston to Katy. That's duplicate content, Google spots it without effort, and worse: it convinces nobody who reads it.</p>
<p>A service-and-city page that works contains things that could only be on that page:</p>
<ul>
  <li>How long it takes you to reach that area and where you drive from.</li>
  <li>Problems typical of there (older homes with cast iron, new subdivisions with low pressure, hard water, shifting soil).</li>
  <li>Jobs of that service done in that city, with photos.</li>
  <li>Reviews from customers in that city.</li>
  <li>Neighborhoods and landmarks locals recognize.</li>
  <li>Pricing or ranges, if they differ by area.</li>
</ul>
<p>If you can't write that about a combination, you shouldn't have that page yet.</p>

<h3>How they link to each other</h3>
<p>Each service-and-city page should link to the services index, to the same service in neighboring cities, and to your other services in that same city. That way someone who arrived looking for a leak in Katy easily discovers you also replace water heaters in Katy.</p>
""" + take("One page for each service in each city, not one services page plus one city page. Start with the combination that makes you the most money and write it properly, not by copying.",
            "One page for each service in each city, not one services page plus one city page. Start with the combination that makes you the most money and write it properly, not by copying."))

# ======================================================= 3
ch("c3", "Diseño que convierte la visita en mensaje", "Design that turns a visit into a message",
"""
<p>Traer visitas es la mitad del trabajo. La otra mitad es que esa visita te escriba. Un sitio con mil visitas al mes y dos llamadas está roto, y no lo arregla más tráfico.</p>

<h3>Lo primero que se ve, sin bajar la pantalla</h3>
<p>En el celular tienes más o menos tres segundos y una pantalla. En esa pantalla tiene que caber:</p>
<ul>
  <li>Qué haces y dónde. “Plomería de emergencia en Houston”, no “Soluciones integrales para su hogar”.</li>
  <li>Una razón para confiar: años de experiencia, licencia, número de reseñas.</li>
  <li>Un botón para llamar y uno para mandar mensaje, grandes, visibles, que se queden fijos cuando la persona baje.</li>
</ul>

<h3>El teléfono tiene que marcar solo</h3>
<p>El número escrito como texto no sirve en móvil. Tiene que ser un enlace que marque al tocarlo. Suena obvio y falla en la mitad de los sitios de negocios locales que revisamos.</p>

<h3>Formularios cortos o nada</h3>
<p>Cada campo que agregas a un formulario tira la conversión. Nombre, teléfono y una línea de “¿qué necesita?” es suficiente. No pidas apellido, código postal, tipo de propiedad ni “cómo nos conoció”. Eso lo preguntas cuando ya estén hablando contigo.</p>
<p>Y si tu clientela es de gente que vive en WhatsApp, un botón directo a WhatsApp convierte mejor que cualquier formulario, porque no le pides que confíe antes de hablar: le das una conversación.</p>

<h3>Mapas de calor: dejar de adivinar</h3>
<p>Un mapa de calor es una imagen de tu propia página que muestra dónde hizo clic la gente, hasta dónde bajó y dónde se detuvo a leer. Las grabaciones de sesión muestran el recorrido completo de una visita anónima.</p>
<p>Con eso dejas de discutir opiniones. Cosas que descubres siempre:</p>
<ul>
  <li>Que casi nadie baja más allá de la segunda pantalla, así que todo lo importante que pusiste abajo no existe.</li>
  <li>Que la gente le hace clic a fotos que no son enlaces, porque quiere verlas más grandes.</li>
  <li>Que un párrafo largo a la mitad de la página es exactamente donde se van.</li>
  <li>Que el botón de “Contacto” del menú se usa mucho menos que el botón de llamar del encabezado.</li>
</ul>
<p>La forma correcta de usarlos es cambiar una cosa al mes y volver a mirar. Cambiar cinco cosas a la vez no te dice cuál sirvió.</p>

<h3>Prueba, no adjetivos</h3>
<p>“Servicio de calidad con años de experiencia” no convence a nadie porque lo dice todo el mundo. Lo que convence: fotos de trabajos reales tuyos, con tu camioneta y tu gente; reseñas con nombre y ciudad; la licencia y el seguro visibles; y decir cuánto cuesta más o menos, aunque sea un rango.</p>
""" + take("Botón de contacto visible sin bajar, formularios cortos, fotos reales, y mapas de calor para dejar de adivinar dónde se pierde la gente.",
            "Contact button visible without scrolling, short forms, real photos, and heatmaps so you stop guessing where people drop off."),
"""
<p>Bringing in visits is half the job. The other half is getting that visit to message you. A site with a thousand visits a month and two calls is broken, and more traffic won't fix it.</p>

<h3>What's visible without scrolling</h3>
<p>On a phone you have roughly three seconds and one screen. That screen has to fit:</p>
<ul>
  <li>What you do and where. “Emergency plumbing in Houston”, not “Integrated solutions for your home”.</li>
  <li>A reason to trust you: years in business, license, review count.</li>
  <li>A call button and a message button, large, visible, and pinned as the person scrolls.</li>
</ul>

<h3>The phone number has to dial itself</h3>
<p>A number written as plain text is useless on mobile. It has to be a link that dials on tap. Sounds obvious, and it fails on half the local business sites we review.</p>

<h3>Short forms or none</h3>
<p>Every field you add to a form drops conversion. Name, phone, and one line of “what do you need?” is enough. Don't ask for last name, ZIP, property type or “how did you hear about us”. Ask that once they're already talking to you.</p>
<p>And if your customers live in WhatsApp, a direct WhatsApp button converts better than any form, because you're not asking them to trust before talking: you're handing them a conversation.</p>

<h3>Heatmaps: stop guessing</h3>
<p>A heatmap is a picture of your own page showing where people clicked, how far they scrolled, and where they paused to read. Session recordings show the full path of an anonymous visit.</p>
<p>With that you stop arguing opinions. Things you always discover:</p>
<ul>
  <li>That almost nobody scrolls past the second screen, so everything important you put down low doesn't exist.</li>
  <li>That people click photos that aren't links, because they want to see them bigger.</li>
  <li>That one long paragraph mid-page is exactly where they leave.</li>
  <li>That the menu's “Contact” link gets used far less than the call button in the header.</li>
</ul>
<p>The right way to use them is to change one thing a month and look again. Changing five things at once tells you nothing about which one worked.</p>

<h3>Proof, not adjectives</h3>
<p>“Quality service with years of experience” convinces nobody because everyone says it. What convinces: photos of your real jobs, with your truck and your crew; reviews with a name and a city; license and insurance visible; and telling people roughly what it costs, even as a range.</p>
""" + take("Contact button visible without scrolling, short forms, real photos, and heatmaps so you stop guessing where people drop off.",
            "Contact button visible without scrolling, short forms, real photos, and heatmaps so you stop guessing where people drop off."))

# ======================================================= 4
ch("c4", "Velocidad y las bases técnicas", "Speed and the technical basics",
"""
<p>Nadie contrata a una agencia por “datos estructurados”. Pero si esto está mal, todo lo demás rinde menos. Son pocas cosas y se arreglan una vez.</p>

<h3>Velocidad</h3>
<p>Casi todos tus visitantes te van a abrir desde el celular, muchas veces con señal mediocre. Cada segundo de espera te cuesta gente, y en emergencias te cuesta el trabajo completo: se regresan al mapa y llaman al siguiente.</p>
<p>Lo que más pesa, en orden:</p>
<ul>
  <li><b>Imágenes sin comprimir.</b> Una foto de 4 MB directa del celular es la causa número uno de un sitio lento. Se comprimen y se sirven en formatos modernos.</li>
  <li><b>Plantillas y plugins de más.</b> Muchos sitios cargan código de veinte funciones que el negocio nunca usa.</li>
  <li><b>Tipografías y videos pesados.</b> Un video de fondo se ve bonito en la computadora del diseñador y mata la página en un teléfono.</li>
</ul>
<p>Mídelo con datos móviles, no con wifi, y desde un teléfono normal, no el más caro del mercado.</p>

<h3>Títulos y descripciones</h3>
<p>Cada página necesita su propio título (lo que se ve en azul en Google) y su propia descripción. Si diez páginas comparten el mismo título, Google no sabe cuál mostrar.</p>
<p>Un buen título de página de servicio: <span class="mono">Destape de drenajes en Katy, TX | Nombre del negocio</span>. Servicio, ciudad, negocio. Sin adornos.</p>

<h3>Encabezados en orden</h3>
<p>Un solo H1 por página, que diga de qué trata. Los subtítulos en H2 y H3, en orden. No uses encabezados solo porque se ven grandes.</p>

<h3>Datos estructurados</h3>
<p>Es un pedacito de código invisible que le dice a Google en su propio idioma: este negocio se llama así, está aquí, atiende de tal hora a tal hora, cobra en este rango, ofrece estos servicios. Para un negocio local es de lo más rentable que existe, porque también es de donde beben las respuestas de IA.</p>

<h3>Lo básico que no puede faltar</h3>
<ul>
  <li>Certificado de seguridad (que la dirección empiece con https).</li>
  <li>Mapa del sitio enviado a Google Search Console y a Bing Webmaster Tools.</li>
  <li>Una sola versión del sitio (con www o sin www, no las dos).</li>
  <li>Texto alternativo en las imágenes, describiendo lo que se ve.</li>
  <li>Medición instalada, para saber cuántas llamadas y mensajes salen del sitio.</li>
</ul>
""" + take("Comprime las fotos, dale a cada página su título propio, pon datos estructurados y mide desde un celular con datos móviles.",
            "Compress the photos, give every page its own title, add structured data, and measure from a phone on mobile data."),
"""
<p>Nobody hires an agency for “structured data”. But if this is wrong, everything else underperforms. It's a short list and it gets fixed once.</p>

<h3>Speed</h3>
<p>Almost all your visitors will open the site on a phone, often on mediocre signal. Every second of waiting costs you people, and in an emergency it costs you the whole job: they go back to the map and call the next one.</p>
<p>What weighs most, in order:</p>
<ul>
  <li><b>Uncompressed images.</b> A 4 MB photo straight off a phone is the number one cause of a slow site. They get compressed and served in modern formats.</li>
  <li><b>Bloated templates and plugins.</b> Many sites load the code for twenty features the business never uses.</li>
  <li><b>Heavy fonts and videos.</b> A background video looks great on the designer's desktop and kills the page on a phone.</li>
</ul>
<p>Measure it on mobile data, not wifi, and from a normal phone, not the most expensive one on the market.</p>

<h3>Titles and descriptions</h3>
<p>Every page needs its own title (the blue line in Google) and its own description. If ten pages share a title, Google doesn't know which one to show.</p>
<p>A good service page title: <span class="mono">Drain Cleaning in Katy, TX | Business Name</span>. Service, city, business. No decoration.</p>

<h3>Headings in order</h3>
<p>One H1 per page, stating what it's about. Subheads in H2 and H3, in order. Don't use headings just because they look big.</p>

<h3>Structured data</h3>
<p>It's a small piece of invisible code that tells Google in its own language: this business is called this, it's here, it's open these hours, it charges in this range, it offers these services. For a local business it's among the highest-return work there is, because it's also what AI answers drink from.</p>

<h3>The basics that can't be missing</h3>
<ul>
  <li>A security certificate (the address starts with https).</li>
  <li>A sitemap submitted to Google Search Console and Bing Webmaster Tools.</li>
  <li>One single version of the site (with www or without, not both).</li>
  <li>Alt text on images, describing what's actually shown.</li>
  <li>Analytics installed, so you know how many calls and messages come from the site.</li>
</ul>
""" + take("Compress the photos, give every page its own title, add structured data, and measure from a phone on mobile data.",
            "Compress the photos, give every page its own title, add structured data, and measure from a phone on mobile data."))

# ======================================================= 5
ch("c5", "El Perfil de Negocio de Google, a fondo", "The Google Business Profile, in depth",
"""
<p>Si solo pudieras arreglar una cosa este mes, sería esta. El Perfil de Negocio de Google es lo que decide si sales en el mapa, y es gratis.</p>

<h3>Categoría principal: la decisión más importante</h3>
<p>Tu categoría principal pesa más que casi cualquier otra cosa en el perfil. Tiene que ser la más específica que exista para lo que haces. “Plomero” gana sobre “Contratista”. “Contratista de techos” gana sobre “Servicio de reparación de viviendas”.</p>
<p>Cómo escogerla bien: busca tu servicio en tu ciudad, mira los tres que salen arriba, y revisa qué categoría usan. No estás copiando: estás leyendo lo que Google ya premió en tu zona.</p>
<p>Puedes agregar categorías secundarias, pero con cuidado. Meter diez categorías dispersas diluye la relevancia en vez de sumarla.</p>

<h3>Servicios y descripciones</h3>
<p>Dentro del perfil hay una sección de servicios donde puedes listar cada cosa que haces, con una descripción corta cada una. Casi nadie la llena. Llénala completa, con el nombre que la gente usa (“destape de drenaje”, no “desobstrucción hidrosanitaria”).</p>

<h3>Área de servicio o dirección</h3>
<p>Si atiendes a domicilio y no recibes clientes en tu casa, Google tiene una configuración específica para eso: declaras las ciudades que cubres y ocultas la dirección. Es totalmente permitido y es lo correcto. Lo que no está permitido es inventar una dirección en una ciudad donde no estás, ni rentar un buzón para simular una sucursal: eso te puede costar el perfil entero.</p>

<h3>Fotos</h3>
<p>Sube fotos cada mes, no una vez al año. Fotos reales: el trabajo antes y después, tu gente trabajando, la camioneta, la herramienta, el equipo instalado. Diez o quince al mes es un buen ritmo. Nada de imágenes de banco: se notan y no ayudan.</p>

<h3>Publicaciones</h3>
<p>Las publicaciones del perfil son cortas, llevan foto y un botón. Una por semana es un ritmo razonable. Sirven para dos cosas: mantener el perfil activo y ocupar más espacio visual cuando alguien te busca por nombre.</p>
<p>Qué publicar sin quedarte sin ideas: un servicio con su llamada a la acción, un consejo útil de tu oficio, un trabajo reciente con foto, y una oferta o recordatorio de temporada.</p>

<h3>Reseñas</h3>
<p>Las reseñas mueven el mapa y mueven la decisión de llamarte. Tres reglas:</p>
<ul>
  <li><b>Pídelas siempre, el mismo día.</b> Manda un mensaje con el enlace directo mientras el trabajo está fresco. Una semana después ya nadie se acuerda.</li>
  <li><b>Contesta todas, en menos de 48 horas.</b> La respuesta no es para quien la escribió: es para los que la van a leer.</li>
  <li><b>Nunca las compres ni las inventes.</b> Es la forma más rápida de perder el perfil, y se detecta.</li>
</ul>
<p>Ante una reseña mala: no discutas los detalles en público, reconoce lo que se pueda reconocer, e invita a seguir la conversación en privado. Una respuesta serena a una reseña de una estrella vende más que diez reseñas de cinco.</p>
""" + note("Optimizamos el perfil completo (categorías, servicios, atributos, área, horarios), lo mantenemos activo con publicaciones y foto, y subimos fotos nuevas cada mes.",
           "We optimize the whole profile (categories, services, attributes, area, hours), keep it active with posts and photos, and upload new photos every month.",
           "Hola MAPA, quiero que revisen y optimicen mi Perfil de Negocio de Google.",
           "Hi MAPA, I want you to review and optimize my Google Business Profile."),
"""
<p>If you could fix only one thing this month, this would be it. The Google Business Profile decides whether you appear on the map, and it's free.</p>

<h3>Primary category: the most important decision</h3>
<p>Your primary category outweighs almost everything else on the profile. It has to be the most specific one that exists for what you do. “Plumber” beats “Contractor”. “Roofing contractor” beats “Home repair service”.</p>
<p>How to choose well: search your service in your city, look at the three ranking on top, and check what category they use. You're not copying: you're reading what Google already rewarded in your area.</p>
<p>You can add secondary categories, but carefully. Ten scattered categories dilute relevance rather than adding to it.</p>

<h3>Services and descriptions</h3>
<p>Inside the profile there's a services section where you can list every job you do, each with a short description. Almost nobody fills it in. Fill it completely, using the words people actually use (“drain cleaning”, not “hydro-sanitary unblocking”).</p>

<h3>Service area or address</h3>
<p>If you travel to customers and don't receive them at home, Google has a specific setting for that: you declare the cities you cover and hide the address. It's fully allowed and it's the correct setup. What isn't allowed is inventing an address in a city you're not in, or renting a mailbox to fake a branch: that can cost you the entire profile.</p>

<h3>Photos</h3>
<p>Upload photos every month, not once a year. Real photos: the job before and after, your crew working, the truck, the tools, the installed equipment. Ten to fifteen a month is a good rhythm. No stock images: they're obvious and they don't help.</p>

<h3>Posts</h3>
<p>Profile posts are short, carry a photo and a button. Once a week is a reasonable rhythm. They do two things: keep the profile active and take up more visual space when someone searches your name.</p>
<p>What to post without running out of ideas: a service with its call to action, a useful tip from your trade, a recent job with a photo, and a seasonal offer or reminder.</p>

<h3>Reviews</h3>
<p>Reviews move the map and move the decision to call you. Three rules:</p>
<ul>
  <li><b>Always ask, the same day.</b> Send a message with the direct link while the job is fresh. A week later nobody remembers.</li>
  <li><b>Reply to all of them, within 48 hours.</b> The reply isn't for the writer: it's for the people who will read it.</li>
  <li><b>Never buy or invent them.</b> It's the fastest way to lose the profile, and it gets caught.</li>
</ul>
<p>Facing a bad review: don't argue details in public, acknowledge what can be acknowledged, and invite the conversation to continue privately. A calm reply to a one-star review sells more than ten five-star ones.</p>
""" + note("We optimize the whole profile (categories, services, attributes, area, hours), keep it active with posts and photos, and upload new photos every month.",
           "We optimize the whole profile (categories, services, attributes, area, hours), keep it active with posts and photos, and upload new photos every month.",
           "Hola MAPA, quiero que revisen y optimicen mi Perfil de Negocio de Google.",
           "Hi MAPA, I want you to review and optimize my Google Business Profile."))

# ======================================================= 6
ch("c6", "Los otros tres mapas: Apple, Bing y Yelp", "The other three maps: Apple, Bing and Yelp",
"""
<p>Casi todo el mundo trabaja Google y deja los otros tres abandonados. Ahí hay ventaja, porque la competencia tampoco los está trabajando.</p>

<h3>Apple Business Connect</h3>
<p>Cada iPhone trae Apple Maps de fábrica. Cuando alguien le pregunta a Siri por un plomero, o busca en el mapa desde su iPhone, no está consultando a Google. Si tu ficha en Apple Maps está mal, incompleta o no existe, todo ese público no te ve.</p>
<p>Apple Business Connect es gratis y se reclama parecido a Google. Lo que hay que dejar completo:</p>
<ul>
  <li>Categoría correcta y datos idénticos a los de Google.</li>
  <li>Área de servicio, si trabajas a domicilio.</li>
  <li>Fotos y logo.</li>
  <li>Enlaces de acción: llamar, sitio web, pedir cita.</li>
</ul>

<h3>Bing Places</h3>
<p>Bing tiene menos usuarios que Google, y aun así vale la pena por una razón que crece cada mes: varios asistentes de IA se apoyan en el índice de Bing para responder preguntas locales. Reclamar Bing Places es media hora de trabajo y te mete en esa fuente.</p>
<p>Se puede importar directo desde tu perfil de Google, lo cual ayuda a que los datos queden idénticos.</p>

<h3>Yelp</h3>
<p>A muchos contratistas Yelp no les cae bien, y no siempre sin razón. Pero mucha gente en Estados Unidos todavía busca ahí, y Yelp aparece muy arriba cuando alguien busca tu nombre. Tener un perfil abandonado con datos viejos es peor que no tener nada.</p>
<p>Lo mínimo: reclamarlo, poner horarios y área correctos, llenar la lista de servicios, subir fotos y contestar las reseñas. No necesitas pagarles publicidad para tener el perfil en orden.</p>

<h3>La regla que une a los cuatro</h3>
<p>El mismo nombre, la misma dirección, el mismo teléfono, la misma categoría y las mismas fotos en los cuatro. La consistencia entre plataformas es en sí misma una señal de confianza: le dice a los buscadores que este negocio es real y que la información es fiable.</p>
""" + note("Reclamamos y mantenemos los cuatro perfiles con los mismos datos y las mismas fotos, y subimos fotos nuevas cada mes a Google, Apple Maps y Yelp.",
           "We claim and maintain all four profiles with the same data and the same photos, and upload new photos monthly to Google, Apple Maps and Yelp.",
           "Hola MAPA, quiero que me pongan en orden Apple Maps, Bing Places y Yelp.",
           "Hi MAPA, I want you to get Apple Maps, Bing Places and Yelp in order."),
"""
<p>Almost everyone works Google and leaves the other three abandoned. There's an advantage there, because your competition isn't working them either.</p>

<h3>Apple Business Connect</h3>
<p>Every iPhone ships with Apple Maps. When someone asks Siri for a plumber, or searches the map from their iPhone, they aren't querying Google. If your Apple Maps listing is wrong, incomplete or missing, that whole audience doesn't see you.</p>
<p>Apple Business Connect is free and gets claimed much like Google. What to complete:</p>
<ul>
  <li>Correct category and data identical to Google's.</li>
  <li>Service area, if you travel to customers.</li>
  <li>Photos and logo.</li>
  <li>Action links: call, website, request an appointment.</li>
</ul>

<h3>Bing Places</h3>
<p>Bing has fewer users than Google, and it's still worth it for a reason that grows monthly: several AI assistants lean on Bing's index to answer local questions. Claiming Bing Places is half an hour of work and it puts you in that source.</p>
<p>You can import directly from your Google profile, which helps keep the data identical.</p>

<h3>Yelp</h3>
<p>Plenty of contractors dislike Yelp, not always without reason. But many people in the United States still search there, and Yelp ranks high when someone searches your name. An abandoned profile with stale data is worse than nothing.</p>
<p>The minimum: claim it, set correct hours and area, fill the service list, upload photos, and reply to reviews. You don't need to buy their ads to keep the profile in order.</p>

<h3>The rule that ties all four together</h3>
<p>Same name, same address, same phone, same category and same photos across all four. Cross-platform consistency is itself a trust signal: it tells search engines this business is real and its information is reliable.</p>
""" + note("We claim and maintain all four profiles with the same data and the same photos, and upload new photos monthly to Google, Apple Maps and Yelp.",
           "We claim and maintain all four profiles with the same data and the same photos, and upload new photos monthly to Google, Apple Maps and Yelp.",
           "Hola MAPA, quiero que me pongan en orden Apple Maps, Bing Places y Yelp.",
           "Hi MAPA, I want you to get Apple Maps, Bing Places and Yelp in order."))

# ======================================================= 7
ch("c7", "Citaciones y datos NAP", "Citations and NAP data",
"""
<p>Una citación es cualquier lugar en internet donde aparece el nombre, la dirección y el teléfono de tu negocio, aunque no haya enlace. NAP son esas tres palabras en inglés: Name, Address, Phone.</p>

<h3>Por qué importan</h3>
<p>Los buscadores confirman que un negocio existe cruzando información de muchas fuentes. Si en veinte lugares apareces igual, eres un negocio real y confiable. Si apareces con tres teléfonos distintos y dos direcciones, el buscador tiene que decidir cuál es la buena, y ante la duda te baja.</p>

<h3>Consistencia significa idéntico</h3>
<p>Y con idéntico queremos decir idéntico, hasta en lo que parece no importar:</p>
<table class="table">
  <thead><tr><th>Correcto</th><th>Inconsistente</th></tr></thead>
  <tbody>
    <tr><td>1420 Bellaire Boulevard</td><td>1420 Bellaire Blvd.</td></tr>
    <tr><td>Suite 210</td><td>#210 / Ste 210</td></tr>
    <tr><td>(713) 555-0142</td><td>713-555-0142 / 7135550142</td></tr>
    <tr><td>Ramirez Plumbing LLC</td><td>Ramirez Plumbing / Ramirez Plumbing Houston</td></tr>
  </tbody>
</table>
<p>Escoge un formato, escríbelo una vez y úsalo siempre. Nuestra <a href="citaciones.html">herramienta de citaciones</a> te lo arma y te deja copiarlo.</p>

<h3>Un detalle que casi nadie considera: el nombre</h3>
<p>Meter palabras clave en el nombre del negocio (“Ramirez Plumbing Houston Emergency 24/7”) es tentador porque a veces funciona a corto plazo. También es contra las reglas de Google, cualquier competidor lo puede reportar, y cuando te lo corrigen pierdes lo que habías ganado. Usa el nombre real, el que está en tus papeles y en tu camioneta.</p>

<h3>El orden de trabajo</h3>
<ol>
  <li><b>Los cinco críticos:</b> Google, Apple, Bing, Yelp y Facebook.</li>
  <li><b>Los grandes de servicios en casa:</b> BBB, Angi, Thumbtack, Nextdoor, HomeAdvisor, Houzz.</li>
  <li><b>Los directorios generales:</b> Yellow Pages, Superpages, Manta, Foursquare, MapQuest y compañía.</li>
  <li><b>Los locales de tu ciudad:</b> cámara de comercio, asociaciones de tu gremio, directorios de tu condado. Estos suelen valer más que cinco directorios genéricos.</li>
</ol>

<h3>Limpiar vale más que dar de alta</h3>
<p>Muchos negocios ya tienen fichas viejas que ellos nunca crearon, con el teléfono anterior o la dirección de hace tres mudanzas. Buscar esas fichas y corregirlas o pedir que las borren suele mover más la aguja que registrarse en veinte directorios nuevos.</p>
""" + note("Fijamos tu NAP, construimos tus citaciones durante los primeros meses y buscamos y corregimos las fichas viejas con datos equivocados. Después solo hay que vigilarlas.",
           "We lock your NAP, build out your citations over the first months, and hunt down and correct old listings with wrong data. After that they just need monitoring.",
           "Hola MAPA, quiero que revisen y arreglen mis citaciones.",
           "Hi MAPA, I want you to review and fix my citations."),
"""
<p>A citation is any place on the internet where your business name, address and phone appear, even without a link. NAP is those three words: Name, Address, Phone.</p>

<h3>Why they matter</h3>
<p>Search engines confirm a business exists by cross-checking many sources. If you appear identically in twenty places, you're a real, trustworthy business. If you appear with three different phone numbers and two addresses, the engine has to decide which is right, and when in doubt it ranks you lower.</p>

<h3>Consistent means identical</h3>
<p>And by identical we mean identical, down to what seems not to matter:</p>
<table class="table">
  <thead><tr><th>Correct</th><th>Inconsistent</th></tr></thead>
  <tbody>
    <tr><td>1420 Bellaire Boulevard</td><td>1420 Bellaire Blvd.</td></tr>
    <tr><td>Suite 210</td><td>#210 / Ste 210</td></tr>
    <tr><td>(713) 555-0142</td><td>713-555-0142 / 7135550142</td></tr>
    <tr><td>Ramirez Plumbing LLC</td><td>Ramirez Plumbing / Ramirez Plumbing Houston</td></tr>
  </tbody>
</table>
<p>Pick a format, write it once, use it always. Our <a href="citaciones.html">citations tool</a> builds it and lets you copy it.</p>

<h3>A detail almost nobody considers: the name</h3>
<p>Stuffing keywords into the business name (“Ramirez Plumbing Houston Emergency 24/7”) is tempting because it sometimes works short term. It's also against Google's rules, any competitor can report it, and when it gets corrected you lose whatever you gained. Use the real name, the one on your paperwork and on your truck.</p>

<h3>The order of work</h3>
<ol>
  <li><b>The five critical ones:</b> Google, Apple, Bing, Yelp and Facebook.</li>
  <li><b>The home-services majors:</b> BBB, Angi, Thumbtack, Nextdoor, HomeAdvisor, Houzz.</li>
  <li><b>General directories:</b> Yellow Pages, Superpages, Manta, Foursquare, MapQuest and company.</li>
  <li><b>Local ones in your city:</b> chamber of commerce, trade associations, county directories. These usually beat five generic directories.</li>
</ol>

<h3>Cleaning up beats signing up</h3>
<p>Many businesses already have old listings they never created, with a previous phone number or an address from three moves ago. Finding those and correcting them or requesting removal usually moves the needle more than registering on twenty new directories.</p>
""" + note("We lock your NAP, build out your citations over the first months, and hunt down and correct old listings with wrong data. After that they just need monitoring.",
           "We lock your NAP, build out your citations over the first months, and hunt down and correct old listings with wrong data. After that they just need monitoring.",
           "Hola MAPA, quiero que revisen y arreglen mis citaciones.",
           "Hi MAPA, I want you to review and fix my citations."))

# ======================================================= 8
ch("c8", "Contenido que sí sirve", "Content that actually works",
"""
<p>“Hay que hacer un blog” es uno de los consejos que peor se ejecutan en el marketing local. La mayoría de los blogs de negocios de servicio son tres notas de 2019 sobre “la importancia del mantenimiento preventivo”. Eso no sirve para nada.</p>

<h3>De dónde salen los temas buenos</h3>
<p>No de una lista de palabras clave descargada: de tu teléfono. Las preguntas que te hacen tus clientes antes de contratarte son exactamente lo que otros están escribiendo en Google.</p>
<ul>
  <li>“¿Cuánto cuesta cambiar un calentador de agua?”</li>
  <li>“¿Cómo sé si el granizo dañó mi techo?”</li>
  <li>“¿Cada cuánto hay que limpiar los ductos?”</li>
  <li>“¿Necesito permiso para cambiar el panel eléctrico?”</li>
  <li>“¿Qué hago mientras llega el plomero?”</li>
</ul>
<p>Apunta cada pregunta que te hagan durante un mes. Ahí tienes un año de contenido.</p>

<h3>Los tres tipos que funcionan</h3>
<ol>
  <li><b>Precios.</b> Casi nadie los publica por miedo, y por eso son las búsquedas más frecuentes y menos atendidas. Publica rangos honestos y explica de qué depende. Filtra clientes que no te convienen y atrae a los que sí.</li>
  <li><b>Diagnóstico.</b> “Cómo saber si…”. La gente busca esto justo antes de decidir que necesita ayuda profesional. Si tú se lo explicas, tú eres a quien llama.</li>
  <li><b>Proceso.</b> “Qué esperar cuando…”. Reduce la ansiedad de contratar a un desconocido que va a entrar a su casa.</li>
</ol>

<h3>Cómo escribirlos</h3>
<ul>
  <li>Responde la pregunta en el primer párrafo. No hagas esperar.</li>
  <li>Escribe como hablas con un cliente en la puerta de su casa, no como un folleto.</li>
  <li>Usa ejemplos de tu zona y de tus trabajos.</li>
  <li>Pon una foto tuya trabajando, no una de banco.</li>
  <li>Cierra con una invitación clara a escribirte, y un enlace a la página del servicio correspondiente.</li>
</ul>

<h3>Por qué la constancia gana al volumen</h3>
<p>Porque unos cuantos bien hechos, cada mes, sin fallar, superan a diez de golpe y luego seis meses de silencio. La constancia es la señal: un sitio que se actualiza es un negocio que sigue vivo. Y porque cada artículo bueno sigue trayendo visitas años después, sin costo adicional.</p>

<h3>Sobre escribir con IA</h3>
<p>Es una herramienta útil para investigar temas, ordenar ideas y hacer un primer borrador. No es una herramienta para publicar sin leer. Un artículo genérico que podría ser de cualquier plomero del país no posiciona, y lo más importante: no convence a nadie de llamarte. El valor está en lo que solo tú sabes.</p>
""" + note("Escribimos y publicamos contenido nuevo cada mes, sobre las preguntas reales de tu oficio y tu zona, enlazado a tus páginas de servicio y ciudad.",
           "We write and publish new content every month, on the real questions in your trade and your area, linked to your service-and-city pages.",
           "Hola MAPA, quiero que ustedes lleven el contenido de mi sitio.",
           "Hi MAPA, I want you to handle the content on my site."),
"""
<p>“You should have a blog” is one of the worst-executed pieces of advice in local marketing. Most service business blogs are three posts from 2019 about “the importance of preventive maintenance”. That does nothing.</p>

<h3>Where good topics come from</h3>
<p>Not from a downloaded keyword list: from your phone. The questions customers ask you before hiring are exactly what other people are typing into Google.</p>
<ul>
  <li>“How much does it cost to replace a water heater?”</li>
  <li>“How do I know if hail damaged my roof?”</li>
  <li>“How often should ducts be cleaned?”</li>
  <li>“Do I need a permit to upgrade my electrical panel?”</li>
  <li>“What do I do while I wait for the plumber?”</li>
</ul>
<p>Write down every question you get asked for a month. That's a year of content.</p>

<h3>The three types that work</h3>
<ol>
  <li><b>Pricing.</b> Almost nobody publishes it out of fear, which is why these are the most frequent and least served searches. Publish honest ranges and explain what changes them. It filters out customers you don't want and attracts the ones you do.</li>
  <li><b>Diagnosis.</b> “How to tell if…”. People search this right before deciding they need a professional. If you're the one who explained it, you're the one they call.</li>
  <li><b>Process.</b> “What to expect when…”. It lowers the anxiety of hiring a stranger who's going to walk into their home.</li>
</ol>

<h3>How to write them</h3>
<ul>
  <li>Answer the question in the first paragraph. Don't make people wait.</li>
  <li>Write the way you talk to a customer at their front door, not like a brochure.</li>
  <li>Use examples from your area and your jobs.</li>
  <li>Add a photo of you working, not a stock image.</li>
  <li>Close with a clear invitation to message you, and a link to the matching service page.</li>
</ul>

<h3>Why consistency beats volume</h3>
<p>Because a few done well, every month, without fail, beat ten at once followed by six months of silence. Consistency is the signal: a site that updates is a business that's still alive. And because each good article keeps bringing visits years later, at no extra cost.</p>

<h3>On writing with AI</h3>
<p>It's a useful tool for researching topics, organizing ideas and drafting. It is not a tool for publishing unread. A generic article that could belong to any plumber in the country doesn't rank, and more importantly: it convinces nobody to call you. The value is in what only you know.</p>
""" + note("We write and publish new content every month, on the real questions in your trade and your area, linked to your service-and-city pages.",
           "We write and publish new content every month, on the real questions in your trade and your area, linked to your service-and-city pages.",
           "Hola MAPA, quiero que ustedes lleven el contenido de mi sitio.",
           "Hi MAPA, I want you to handle the content on my site."))

# ======================================================= 9
ch("c9", "Enlaces locales", "Local links",
"""
<p>Un enlace es cuando otro sitio pone la dirección del tuyo en una de sus páginas. Para los buscadores es un voto: alguien más considera que vale la pena mandarte gente.</p>

<h3>Uno bueno vale más que cincuenta malos</h3>
<p>Todavía se venden paquetes de “500 backlinks por $99”. Son enlaces de sitios basura que existen solo para vender enlaces. En el mejor de los casos no hacen nada; en el peor te meten en problemas y luego hay que pagar para limpiarlos.</p>
<p>Un enlace de la cámara de comercio de tu ciudad vale más que quinientos de esos, porque es real, es local y tiene que ver con tu negocio.</p>

<h3>De dónde salen los enlaces buenos para un negocio local</h3>
<ul>
  <li><b>Cámara de comercio local</b> y cámaras de comercio hispanas de tu ciudad o condado.</li>
  <li><b>Asociaciones de tu gremio</b> y organismos que otorgan certificaciones.</li>
  <li><b>Proveedores y fabricantes.</b> Muchos tienen un buscador de “instaladores autorizados”. Si trabajas con una marca, pide que te incluyan.</li>
  <li><b>Patrocinios.</b> El equipo de fútbol infantil, la iglesia, la escuela, la carrera del vecindario. Casi todos publican a sus patrocinadores con enlace.</li>
  <li><b>Prensa local y boletines de barrio.</b> Un negocio con una historia (abriste durante la pandemia, contrataste a un aprendiz, hiciste un trabajo gratis para una familia) es una nota fácil para un periódico chico.</li>
  <li><b>Negocios vecinos que no compiten contigo.</b> Un electricista y un plomero se pueden recomendar mutuamente en sus páginas de “profesionales que recomendamos”.</li>
</ul>

<h3>Pocos y buenos</h3>
<p>No necesitas veinte enlaces al mes. Necesitas unos pocos, conseguidos de verdad, a lo largo del año. Un puñado de enlaces locales reales es más de lo que tiene la mayoría de tus competidores, y no se te cae ninguno cuando cambie el algoritmo. En zonas poco peleadas puede que ya tengas los que necesitas y el esfuerzo rinda más en otro lado.</p>

<h3>Cómo pedirlos sin sonar a spam</h3>
<p>El error es mandar un correo genérico pidiendo un enlace. Lo que funciona es dar algo primero: patrocina de verdad, participa de verdad, ofrece un descuento a los miembros de la asociación, o escribe algo útil que ellos quieran publicar. El enlace viene solo cuando hay una relación real detrás.</p>
""" + note("Conseguimos enlaces locales de sitios reales relacionados con tu oficio y tu ciudad, cuando tu competencia y tu zona lo piden. Nada de paquetes ni granjas de enlaces, y nada de forzar enlaces que no necesitas.",
           "We earn local links from real sites related to your trade and your city, when your competition and your area call for it. No packages, no link farms, and no forcing links you don't need.",
           "Hola MAPA, quiero que trabajen los enlaces locales de mi negocio.",
           "Hi MAPA, I want you to work on local links for my business."),
"""
<p>A link is when another site puts your address on one of its pages. To search engines it's a vote: someone else thinks you're worth sending people to.</p>

<h3>One good link beats fifty bad ones</h3>
<p>People still sell “500 backlinks for $99” packages. Those are links from junk sites that exist only to sell links. At best they do nothing; at worst they get you in trouble and then you pay to clean them up.</p>
<p>A link from your city's chamber of commerce beats five hundred of those, because it's real, it's local, and it's about your business.</p>

<h3>Where good links come from for a local business</h3>
<ul>
  <li><b>Local chamber of commerce</b> and Hispanic chambers of commerce in your city or county.</li>
  <li><b>Trade associations</b> and certifying bodies.</li>
  <li><b>Suppliers and manufacturers.</b> Many run an “authorized installer” finder. If you work with a brand, ask to be listed.</li>
  <li><b>Sponsorships.</b> The youth soccer team, the church, the school, the neighborhood race. Almost all of them publish sponsors with a link.</li>
  <li><b>Local press and neighborhood newsletters.</b> A business with a story (you opened during the pandemic, you took on an apprentice, you did a job free for a family) is an easy piece for a small paper.</li>
  <li><b>Neighboring businesses that don't compete with you.</b> An electrician and a plumber can recommend each other on their “pros we trust” pages.</li>
</ul>

<h3>Few and good</h3>
<p>You don't need twenty links a month. You need a few, genuinely earned, across the year. A handful of real local links is more than most of your competitors have, and none of them disappear when the algorithm changes. In a low-competition area you may already have what you need, and the effort pays off better elsewhere.</p>

<h3>How to ask without sounding like spam</h3>
<p>The mistake is sending a generic email asking for a link. What works is giving something first: actually sponsor, actually participate, offer a discount to association members, or write something useful they'd want to publish. The link follows on its own when there's a real relationship behind it.</p>
""" + note("We earn local links from real sites related to your trade and your city, when your competition and your area call for it. No packages, no link farms, and no forcing links you don't need.",
           "We earn local links from real sites related to your trade and your city, when your competition and your area call for it. No packages, no link farms, and no forcing links you don't need.",
           "Hola MAPA, quiero que trabajen los enlaces locales de mi negocio.",
           "Hi MAPA, I want you to work on local links for my business."))

# ======================================================= 10
ch("c10", "Aparecer en las respuestas de IA", "Showing up in AI answers",
"""
<p>Cada vez más gente hace la pregunta directamente: “necesito un plomero cerca de Sugar Land que trabaje fines de semana, ¿a quién me recomiendas?”. Y recibe una respuesta con dos o tres nombres, sin lista de diez resultados azules.</p>

<h3>Eso cambia menos de lo que parece</h3>
<p>La buena noticia para un negocio local es que las respuestas de IA no se inventan los negocios: los leen. Y leen exactamente las mismas fuentes que ya estamos trabajando: los perfiles de los mapas, los directorios, las reseñas y los sitios web que dicen con claridad quién eres, qué haces y dónde.</p>
<p>Es decir: el trabajo que te hace salir en el mapa es en gran medida el mismo que te hace salir en una respuesta de IA. No son dos estrategias.</p>

<h3>Qué pesa especialmente para la IA</h3>
<ul>
  <li><b>Consistencia total de tus datos.</b> Un modelo que ve tres teléfonos distintos para el mismo negocio no se arriesga a recomendarlo.</li>
  <li><b>Datos estructurados en tu sitio.</b> Es literalmente información escrita en un formato pensado para que las máquinas la lean sin equivocarse.</li>
  <li><b>Respuestas explícitas en texto.</b> Si tu página dice “abrimos sábados de 8 a 2 y atendemos emergencias las 24 horas en Sugar Land, Missouri City y Stafford”, eso es citable. Si lo dices solo en una imagen bonita, no lo es.</li>
  <li><b>Reseñas y su contenido.</b> No solo el promedio de estrellas: lo que la gente dice. Reseñas que mencionan “llegó el mismo día” o “habla español” alimentan respuestas a esas preguntas exactas.</li>
  <li><b>Presencia en Bing.</b> Varios asistentes se apoyan en ese índice.</li>
</ul>

<h3>Cómo comprobar dónde estás</h3>
<p>Es gratis y toma diez minutos: pregúntale a ChatGPT, a Gemini y al asistente de tu teléfono por tu servicio en tu ciudad, como lo preguntaría un cliente. Anota quién sale. Si sale tu competencia y tú no, revisa qué tienen ellos: casi siempre es más reseñas, datos más consistentes o un sitio que explica mejor lo básico.</p>

<h3>Qué no hacer</h3>
<p>No hay un truco para “hackear” la IA, y quien venda uno está inventando. Tampoco sirve llenar el sitio de texto escondido o de frases repetidas: los modelos que responden estas preguntas se apoyan en fuentes verificables, no en trucos de los años dos mil.</p>
""" + take("Las respuestas de IA leen tus perfiles, tus reseñas, tus directorios y tu sitio. Arreglar eso es la estrategia; no hay otra aparte.",
            "AI answers read your profiles, your reviews, your directories and your site. Fixing those is the strategy; there is no separate one."),
"""
<p>More and more people ask the question directly: “I need a plumber near Sugar Land who works weekends, who do you recommend?” And they get an answer with two or three names, no list of ten blue results.</p>

<h3>That changes less than it seems</h3>
<p>The good news for a local business is that AI answers don't invent businesses: they read them. And they read exactly the same sources we're already working: map profiles, directories, reviews and websites that state clearly who you are, what you do and where.</p>
<p>In other words: the work that gets you on the map is largely the same work that gets you into an AI answer. These are not two strategies.</p>

<h3>What weighs especially for AI</h3>
<ul>
  <li><b>Total data consistency.</b> A model seeing three different phone numbers for the same business won't risk recommending it.</li>
  <li><b>Structured data on your site.</b> It's literally information written in a format designed for machines to read without error.</li>
  <li><b>Explicit answers in text.</b> If your page says “we're open Saturdays 8 to 2 and handle 24-hour emergencies in Sugar Land, Missouri City and Stafford”, that's quotable. If you only say it inside a pretty image, it isn't.</li>
  <li><b>Reviews and what's in them.</b> Not just the star average: what people say. Reviews mentioning “came the same day” or “speaks Spanish” feed answers to those exact questions.</li>
  <li><b>Presence on Bing.</b> Several assistants lean on that index.</li>
</ul>

<h3>How to check where you stand</h3>
<p>It's free and takes ten minutes: ask ChatGPT, Gemini and your phone assistant for your service in your city, the way a customer would. Note who shows up. If your competition appears and you don't, look at what they have: it's almost always more reviews, more consistent data, or a site that explains the basics better.</p>

<h3>What not to do</h3>
<p>There's no trick to “hack” AI, and anyone selling one is making it up. Filling your site with hidden text or repeated phrases doesn't work either: the models answering these questions lean on verifiable sources, not on tricks from the 2000s.</p>
""" + take("AI answers read your profiles, your reviews, your directories and your site. Fixing those is the strategy; there is no separate one.",
            "AI answers read your profiles, your reviews, your directories and your site. Fixing those is the strategy; there is no separate one."))

# ======================================================= 11
ch("c11", "Qué medir cada mes", "What to measure every month",
"""
<p>El error clásico es medir lo que se ve bonito en una gráfica. Las visitas al sitio no son un número de negocio. Las llamadas sí.</p>

<h3>Los cinco números que importan</h3>
<ol>
  <li><b>Llamadas y mensajes desde el sitio.</b> El número final. Todo lo demás es intermedio.</li>
  <li><b>Llamadas y solicitudes de indicaciones desde tu Perfil de Google.</b> Google te lo da directo en el panel del perfil. Es la señal más rápida de que el trabajo en el mapa está funcionando.</li>
  <li><b>Posición en el mapa para tus tres o cuatro búsquedas principales.</b> Ojo: búscalas desde distintos puntos de tu área, no solo desde tu casa. El mapa cambia según dónde esté la persona.</li>
  <li><b>Reseñas nuevas en el mes.</b> Cuántas pediste y cuántas llegaron.</li>
  <li><b>Trabajos cerrados y de dónde vinieron.</b> Pregúntale a cada cliente cómo te encontró y anótalo. Es el dato más valioso y el que casi nadie recoge.</li>
</ol>

<h3>Lo que no vale la pena mirar cada mes</h3>
<ul>
  <li><b>Visitas totales.</b> Suben con tráfico que nunca te iba a contratar.</li>
  <li><b>Posición promedio general.</b> Un promedio de trescientas búsquedas no te dice nada accionable.</li>
  <li><b>Seguidores en redes.</b> Para un negocio de servicio local casi nunca se traducen en trabajos.</li>
  <li><b>“Impresiones”.</b> Cuántas veces apareciste sin que nadie hiciera nada.</li>
</ul>

<h3>Un tablero de una hoja</h3>
<p>Cada mes, cinco líneas:</p>
<pre style="background:var(--paper-2);border:1px solid var(--rule);border-radius:4px;padding:1rem;overflow:auto;font-family:var(--mono);font-size:.8rem;line-height:1.9">Llamadas desde el sitio ....... 14  (mes pasado: 9)
Llamadas desde Google ......... 31  (mes pasado: 22)
Reseñas nuevas ................  4  (pedidas: 11)
Trabajos cerrados ............. 12
De dónde vinieron ............. 7 Google, 3 recomendación, 2 sitio</pre>
<p>Si esas cinco líneas mejoran trimestre con trimestre, el trabajo está funcionando, sin importar lo que digan las gráficas de colores.</p>

<h3>Y lo más importante de todo</h3>
<p>Contesta rápido. Podemos ponerte en el primer lugar del mapa y aun así perder el trabajo si tardas tres horas en devolver el mensaje. En servicios locales, quien contesta primero gana la mayoría de las veces. Ninguna estrategia de marketing arregla eso.</p>
""" + note("Cada mes te mandamos el reporte por WhatsApp con estos números y con lo que se hizo, en lenguaje normal y en tu idioma.",
           "Every month we send you the report over WhatsApp with these numbers and what was done, in plain language and in your language.",
           "Hola MAPA, quiero empezar. Mi negocio es ___ y trabajo en ___.",
           "Hi MAPA, I want to get started. My business is ___ and I work in ___.",
           "Empezar por WhatsApp", "Start on WhatsApp"),
"""
<p>The classic mistake is measuring what looks good on a chart. Website visits is not a business number. Calls are.</p>

<h3>The five numbers that matter</h3>
<ol>
  <li><b>Calls and messages from the site.</b> The final number. Everything else is intermediate.</li>
  <li><b>Calls and direction requests from your Google profile.</b> Google gives it to you directly in the profile dashboard. It's the fastest signal that the map work is landing.</li>
  <li><b>Map position for your three or four main searches.</b> Note: search them from different points in your area, not just from your house. The map changes with the searcher's location.</li>
  <li><b>New reviews this month.</b> How many you asked for and how many arrived.</li>
  <li><b>Jobs closed and where they came from.</b> Ask every customer how they found you and write it down. It's the most valuable data point and the one almost nobody collects.</li>
</ol>

<h3>What's not worth checking monthly</h3>
<ul>
  <li><b>Total visits.</b> They rise with traffic that was never going to hire you.</li>
  <li><b>Overall average position.</b> An average across three hundred searches tells you nothing actionable.</li>
  <li><b>Social followers.</b> For a local service business they almost never turn into jobs.</li>
  <li><b>“Impressions”.</b> How many times you appeared while nobody did anything.</li>
</ul>

<h3>A one-page dashboard</h3>
<p>Every month, five lines:</p>
<pre style="background:var(--paper-2);border:1px solid var(--rule);border-radius:4px;padding:1rem;overflow:auto;font-family:var(--mono);font-size:.8rem;line-height:1.9">Calls from the site ........... 14  (last month: 9)
Calls from Google ............. 31  (last month: 22)
New reviews ...................  4  (asked: 11)
Jobs closed ................... 12
Where they came from .......... 7 Google, 3 referral, 2 website</pre>
<p>If those five lines improve quarter over quarter, the work is working, whatever the colorful charts say.</p>

<h3>And the most important thing of all</h3>
<p>Answer fast. We can put you first on the map and still lose the job if you take three hours to reply. In local services, whoever answers first wins most of the time. No marketing strategy fixes that.</p>
""" + note("Every month we send you the report over WhatsApp with these numbers and what was done, in plain language and in your language.",
           "Every month we send you the report over WhatsApp with these numbers and what was done, in plain language and in your language.",
           "Hola MAPA, quiero empezar. Mi negocio es ___ y trabajo en ___.",
           "Hi MAPA, I want to get started. My business is ___ and I work in ___.",
           "Empezar por WhatsApp", "Start on WhatsApp"))


# ======================================================= assemble
toc = "".join(
    f'<li><a href="#{cid}"><span data-l="es">{t_es}</span><span data-l="en">{t_en}</span></a></li>'
    for cid, t_es, t_en, _, _ in CH)

FIGS = figuras_web()


import re as _re


def con_figura(cuerpo, cid):
    f = FIGS.get(cid)
    if cid == 'c11':      # el tablero ya está dibujado; sobra el bloque de texto
        cuerpo = _re.sub(r'<pre.*?</pre>', '', cuerpo, flags=_re.S)
    if not f:
        return cuerpo
    k = cuerpo.find('</p>')
    return (cuerpo[:k + 4] + f + cuerpo[k + 4:]) if k > 0 else f + cuerpo


chapters = ""
for i, (cid, t_es, t_en, es, en) in enumerate(CH, 1):
    chapters += f'''<article class="chapter" id="{cid}">
  <span class="chapter__n"><span data-l="es">Capítulo {i:02d}</span><span data-l="en">Chapter {i:02d}</span></span>
  <h2><span data-l="es">{t_es}</span><span data-l="en">{t_en}</span></h2>
  <div data-l="es">{con_figura(es, cid)}</div>
  <div data-l="en">{con_figura(en, cid)}</div>
</article>
'''

body = f'''<div class="progress" aria-hidden="true"></div>

<section class="deep grid-bg sec sec--tight">
  <div class="wrap">
    <p class="legend"><span data-l="es">La guía · 11 capítulos</span><span data-l="en">The guide · 11 chapters</span></p>
    <h1 style="max-width:17ch"><span data-l="es">Guía de marketing local para negocios de servicio</span>
      <span data-l="en">Local marketing guide for service businesses</span></h1>
    <p class="lede"><span data-l="es">Todo lo que hacemos por nuestros clientes, explicado completo y gratis: estructura del sitio, diseño que convierte, el Perfil de Google, Apple Maps, Bing, Yelp, citaciones, contenido, enlaces, búsqueda con IA y qué medir cada mes.</span>
      <span data-l="en">Everything we do for clients, explained in full and for free: website, design that converts, the Google profile, Apple Maps, Bing, Yelp, citations, content, links, AI search, and what to measure each month.</span></p>
    <div class="btnrow" style="margin-top:1.8rem">
      {wa("Hola MAPA, leí su guía y prefiero que ustedes lo hagan. Mi negocio es ___ en ___.",
          "Hi MAPA, I read your guide and I'd rather you did it. My business is ___ in ___.",
          "Que lo hagan ustedes", "Have you do it")}
      <a class="btn btn--ghost" href="assets/guia-marketing-local-mapa-marketing.pdf" download data-l="es">Descargar en PDF</a>
      <a class="btn btn--ghost" href="assets/local-marketing-guide-mapa-marketing.pdf" download data-l="en">Download the PDF</a>
      <a class="btn btn--ghost" href="herramientas.html"><span data-l="es">Ver las herramientas</span><span data-l="en">See the tools</span></a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap guide">
    <aside class="toc">
      <p class="legend"><span data-l="es">Capítulos</span><span data-l="en">Chapters</span></p>
      <ol>{toc}</ol>
    </aside>
    <div>{chapters}</div>
  </div>
</section>

<section class="sec sec--tight">
  <div class="wrap">
    <div class="cta reveal"><div class="cta__in">
      <p class="legend"><span data-l="es">Terminaste la guía</span><span data-l="en">You finished the guide</span></p>
      <h2><span data-l="es">Ahora son entre diez y quince horas al mes. Todos los meses.</span>
          <span data-l="en">Now it's ten to fifteen hours a month. Every month.</span></h2>
      <p><span data-l="es">Si las tienes, hazlo tú: aquí está todo lo que necesitas y no te vamos a esconder nada. Si prefieres estar arriba de un techo y no frente a una pantalla, escríbenos.</span>
         <span data-l="en">If you have them, do it yourself: everything you need is here and we're not hiding anything. If you'd rather be on a roof than in front of a screen, message us.</span></p>
      {wa("Hola MAPA, leí la guía completa. Mi negocio es ___ y trabajo en ___. ¿Por dónde empezamos?",
          "Hi MAPA, I read the whole guide. My business is ___ and I work in ___. Where do we start?",
          "Escribir por WhatsApp", "Message on WhatsApp")}
    </div></div>
  </div>
</section>'''

page("guia.html",
     "Guía de marketing local para negocios de servicio | MAPA Marketing",
     "Guía completa y gratuita en español: sitio web, SEO local, Perfil de Negocio de Google, Apple Maps, Bing Places, Yelp, citaciones NAP, contenido, enlaces locales y búsqueda con IA.",
     body)
