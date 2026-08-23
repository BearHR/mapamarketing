# -*- coding: utf-8 -*-
import pathlib, sys

p = pathlib.Path('/home/claude/mapa/_build/guide.py')
s = p.read_text(encoding='utf-8')

# ---------------------------------------------------------------------------
# 1. Reemplazo completo del capítulo 2
# ---------------------------------------------------------------------------
start = s.index('# ======================================================= 2')
end = s.index('# ======================================================= 3')

NEW_C2 = '''# ======================================================= 2
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

'''

s = s[:start] + NEW_C2 + s[end:]

# ---------------------------------------------------------------------------
# 2. Quitar cifras de servicio de las cajas "Cómo lo hacemos nosotros"
# ---------------------------------------------------------------------------
pairs = [
    # cap. 5 — perfil de Google
    ('"Optimizamos el perfil completo (categorías, servicios, atributos, área, horarios), publicamos cuatro veces al mes con foto, y subimos fotos nuevas cada mes.",\n           "We optimize the whole profile (categories, services, attributes, area, hours), post four times a month with photos, and upload new photos monthly.",',
     '"Optimizamos el perfil completo (categorías, servicios, atributos, área, horarios), lo mantenemos activo con publicaciones y foto, y subimos fotos nuevas cada mes.",\n           "We optimize the whole profile (categories, services, attributes, area, hours), keep it active with posts and photos, and upload new photos every month.",'),
    ('"We optimize the whole profile (categories, services, attributes, area, hours), post four times a month with photos, and upload new photos monthly.",\n           "We optimize the whole profile (categories, services, attributes, area, hours), post four times a month with photos, and upload new photos monthly.",',
     '"We optimize the whole profile (categories, services, attributes, area, hours), keep it active with posts and photos, and upload new photos every month.",\n           "We optimize the whole profile (categories, services, attributes, area, hours), keep it active with posts and photos, and upload new photos every month.",'),

    # cap. 7 — citaciones
    ('"Fijamos tu NAP, construimos citaciones nuevas cada mes y buscamos y corregimos las fichas viejas con datos equivocados.",\n           "We lock your NAP, build new citations every month, and hunt down and correct old listings with wrong data.",',
     '"Fijamos tu NAP, construimos tus citaciones durante los primeros meses y buscamos y corregimos las fichas viejas con datos equivocados. Después solo hay que vigilarlas.",\n           "We lock your NAP, build out your citations over the first months, and hunt down and correct old listings with wrong data. After that they just need monitoring.",'),
    ('"We lock your NAP, build new citations every month, and hunt down and correct old listings with wrong data.",\n           "We lock your NAP, build new citations every month, and hunt down and correct old listings with wrong data.",',
     '"We lock your NAP, build out your citations over the first months, and hunt down and correct old listings with wrong data. After that they just need monitoring.",\n           "We lock your NAP, build out your citations over the first months, and hunt down and correct old listings with wrong data. After that they just need monitoring.",'),

    # cap. 8 — contenido
    ('"Escribimos y publicamos tres artículos al mes, sobre las preguntas reales de tu oficio y tu zona, enlazados a tus páginas de servicio.",\n           "We write and publish three articles a month, on the real questions in your trade and your area, linked to your service pages.",',
     '"Escribimos y publicamos contenido nuevo cada mes, sobre las preguntas reales de tu oficio y tu zona, enlazado a tus páginas de servicio y ciudad.",\n           "We write and publish new content every month, on the real questions in your trade and your area, linked to your service-and-city pages.",'),
    ('"We write and publish three articles a month, on the real questions in your trade and your area, linked to your service pages.",\n           "We write and publish three articles a month, on the real questions in your trade and your area, linked to your service pages.",',
     '"We write and publish new content every month, on the real questions in your trade and your area, linked to your service-and-city pages.",\n           "We write and publish new content every month, on the real questions in your trade and your area, linked to your service-and-city pages.",'),
    ('"Hola MAPA, quiero los tres artículos al mes para mi sitio.",\n           "Hi MAPA, I want the three monthly articles for my site."),',
     '"Hola MAPA, quiero que ustedes lleven el contenido de mi sitio.",\n           "Hi MAPA, I want you to handle the content on my site."),'),
    ('"Hola MAPA, quiero los tres artículos al mes para mi sitio.",\n           "Hi MAPA, I want the three monthly articles for my site."))',
     '"Hola MAPA, quiero que ustedes lleven el contenido de mi sitio.",\n           "Hi MAPA, I want you to handle the content on my site."))'),

    # cap. 9 — enlaces
    ('"Conseguimos un enlace local nuevo cada mes, de sitios reales relacionados con tu oficio y tu ciudad. Nada de paquetes ni granjas de enlaces.",\n           "We earn one new local link every month, from real sites related to your trade and your city. No packages, no link farms.",',
     '"Conseguimos enlaces locales de sitios reales relacionados con tu oficio y tu ciudad, cuando tu competencia y tu zona lo piden. Nada de paquetes ni granjas de enlaces, y nada de forzar enlaces que no necesitas.",\n           "We earn local links from real sites related to your trade and your city, when your competition and your area call for it. No packages, no link farms, and no forcing links you don\'t need.",'),
    ('"We earn one new local link every month, from real sites related to your trade and your city. No packages, no link farms.",\n           "We earn one new local link every month, from real sites related to your trade and your city. No packages, no link farms.",',
     '"We earn local links from real sites related to your trade and your city, when your competition and your area call for it. No packages, no link farms, and no forcing links you don\'t need.",\n           "We earn local links from real sites related to your trade and your city, when your competition and your area call for it. No packages, no link farms, and no forcing links you don\'t need.",'),

    # cap. 11 — reporte
    ('"Cada mes te mandamos el reporte por WhatsApp con estos números y con lo que se hizo, en lenguaje normal y en tu idioma.",\n           "Every month we send you the report over WhatsApp with these numbers and what was done, in plain language and in your language.",',
     '"Cada mes te mandamos el reporte por WhatsApp con estos números y con lo que se hizo, en lenguaje normal y en tu idioma.",\n           "Every month we send you the report over WhatsApp with these numbers and what was done, in plain language and in your language.",'),

    # cap. 8 — título y encabezado interno
    ('ch("c8", "Contenido: tres artículos al mes que sí sirven", "Content: three monthly articles that actually work",',
     'ch("c8", "Contenido que sí sirve", "Content that actually works",'),
    ('<h3>Por qué tres al mes y no diez</h3>\n<p>Porque tres bien hechos, cada mes, sin fallar, superan a diez de golpe y luego seis meses de silencio.',
     '<h3>Por qué la constancia gana al volumen</h3>\n<p>Porque unos cuantos bien hechos, cada mes, sin fallar, superan a diez de golpe y luego seis meses de silencio.'),
    ('<h3>Why three a month and not ten</h3>\n<p>Because three done well, every month, without fail, beats ten at once followed by six months of silence.',
     '<h3>Why consistency beats volume</h3>\n<p>Because a few done well, every month, without fail, beat ten at once followed by six months of silence.'),

    # cap. 9 — consejo de ritmo
    ('<h3>Uno al mes es suficiente</h3>\n<p>No necesitas veinte enlaces al mes. Necesitas uno bueno, conseguido de verdad, todos los meses. Doce enlaces locales reales al año es más de lo que tiene la mayoría de tus competidores, y no se te cae ninguno cuando cambie el algoritmo.</p>',
     '<h3>Pocos y buenos</h3>\n<p>No necesitas veinte enlaces al mes. Necesitas unos pocos, conseguidos de verdad, a lo largo del año. Un puñado de enlaces locales reales es más de lo que tiene la mayoría de tus competidores, y no se te cae ninguno cuando cambie el algoritmo. En zonas poco peleadas puede que ya tengas los que necesitas y el esfuerzo rinda más en otro lado.</p>'),
    ('<h3>One a month is enough</h3>\n<p>You don\'t need twenty links a month. You need one good one, genuinely earned, every month. Twelve real local links a year is more than most of your competitors have, and none of them disappear when the algorithm changes.</p>',
     '<h3>Few and good</h3>\n<p>You don\'t need twenty links a month. You need a few, genuinely earned, across the year. A handful of real local links is more than most of your competitors have, and none of them disappear when the algorithm changes. In a low-competition area you may already have what you need, and the effort pays off better elsewhere.</p>'),

    # cap. 5 — consejo sobre publicaciones (se mantiene como consejo, sin cifra dura)
    ('<p>Las publicaciones del perfil son cortas, llevan foto y un botón. Cuatro al mes es el mínimo razonable.',
     '<p>Las publicaciones del perfil son cortas, llevan foto y un botón. Una por semana es un ritmo razonable.'),
    ('<p>Profile posts are short, carry a photo and a button. Four a month is the reasonable minimum.',
     '<p>Profile posts are short, carry a photo and a button. Once a week is a reasonable rhythm.'),

    # descripción del capítulo 2 en el hero de la guía
    ('sitio web, diseño que convierte, el Perfil de Google, Apple Maps, Bing, Yelp, citaciones, contenido, enlaces, búsqueda con IA y qué medir cada mes.',
     'estructura del sitio, diseño que convierte, el Perfil de Google, Apple Maps, Bing, Yelp, citaciones, contenido, enlaces, búsqueda con IA y qué medir cada mes.'),
]

miss = 0
for old, new in pairs:
    if old in s:
        s = s.replace(old, new, 1)
    else:
        print('no encontrado:', old[:80].replace('\n', ' '))
        miss += 1

p.write_text(s, encoding='utf-8')
print('capítulo 2 reescrito; %d de %d reemplazos fallaron' % (miss, len(pairs)))
