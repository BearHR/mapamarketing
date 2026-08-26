# -*- coding: utf-8 -*-
"""Revisión de visibilidad — el entregable gratis que prometen los anuncios.

Llena NEGOCIO y corre:
    python3 _build/make_audit.py
Salida: auditorias/revision-<negocio>.pdf   (6 páginas, para mandar por WhatsApp)
"""
import pathlib, datetime, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from weasyprint import HTML
import figs

ROOT = pathlib.Path('/home/claude/mapa')
FONTS = pathlib.Path('/home/claude/ads/fonts')
OUTDIR = ROOT / 'auditorias'; OUTDIR.mkdir(exist_ok=True)
WA_NUM = '+1 (726) 255-6888'

# ===========================================================================
# LLENA ESTO
# ===========================================================================
NEGOCIO = dict(
    negocio  = 'Ramírez Plumbing',
    contacto = 'Luis',
    oficio   = 'plomería',
    ciudad   = 'Houston',
    fecha    = None,

    # Calificación global y por área (0–100)
    score = 34,
    areas = [('Sitio web', 30), ('Perfil de Google', 45), ('Otros mapas', 10),
             ('Reseñas', 40), ('Contenido y enlaces', 20)],

    # Los cuatro mapas: (nombre, estado, nota corta)
    # estado: True = bien · 'medio' = existe pero incompleto · False = no está
    mapas = [('Google', 'medio', 'Categoría mal'), ('Apple Maps', False, 'No existe'),
             ('Bing Places', False, 'No existe'), ('Yelp', 'medio', 'Sin fotos')],

    # Competencia
    competidores = [('Competidor 1', '128 reseñas', ''),
                    ('Competidor 2', '86 reseñas', ''),
                    ('Competidor 3', '54 reseñas', '')],
    tu_posicion = 'Fuera del mapa',

    # Hallazgos: (título, explicación, gravedad 1–3)
    hallazgos = [
        ('El sitio tarda 6.4 segundos en abrir en celular',
         'Más de la mitad de la gente se va antes de que cargue. Como casi todos te buscan '
         'desde el teléfono, esa es la puerta principal del negocio y está atorada.', 3),
        ('Una sola página de “Servicios” para los cuatro trabajos',
         'Google manda gente a páginas, no a sitios. Sin una página por servicio y ciudad no '
         'hay nada que pueda salir cuando alguien busca “destape de drenajes en Katy”.', 3),
        ('Tu Perfil de Google tiene la categoría equivocada',
         'Está como “Contratista general”. La categoría principal es lo que más pesa en el '
         'paquete de tres, y esa sola línea te deja fuera de las búsquedas de plomería.', 3),
        ('No apareces en Apple Maps ni en Bing Places',
         'Quien usa iPhone y le pregunta a Siri no te ve. Bing además alimenta a varios '
         'asistentes de IA, así que también te deja fuera de ahí.', 2),
        ('Tu teléfono aparece de tres maneras distintas',
         'Google no está seguro de cuál eres tú y, ante la duda, te baja en el mapa.', 2),
        ('La última reseña es de hace 14 meses y hay 3 sin responder',
         'Las reseñas mueven el mapa y mueven la decisión de llamarte. Están apagadas.', 2),
    ],

    # Qué arreglar primero: (acción, impacto 1–3)
    prioridades = [
        ('Corregir la categoría del Perfil de Google', 3),
        ('Reclamar Apple Maps y Bing Places', 3),
        ('Una página por cada servicio en cada ciudad', 3),
        ('Comprimir imágenes y acelerar el sitio', 2),
        ('Un solo formato de teléfono en todos lados', 2),
        ('Volver a pedir reseñas y responder las viejas', 1),
    ],
)

CSS = ("""
@font-face{font-family:Archivo;src:url('file://__F__/Archivo-700.ttf');font-weight:700}
@font-face{font-family:Archivo;src:url('file://__F__/Archivo-800.ttf');font-weight:800}
@font-face{font-family:Archivo;src:url('file://__F__/Archivo-900.ttf');font-weight:900}
@font-face{font-family:'Public Sans';src:url('file://__F__/PublicSans-400.ttf');font-weight:400}
@font-face{font-family:'Public Sans';src:url('file://__F__/PublicSans-600.ttf');font-weight:600}
@font-face{font-family:'DM Mono';src:url('file://__F__/DMMono-500.ttf');font-weight:500}

@page{size:Letter;margin:19mm 18mm 16mm 18mm;
  @bottom-left{content:'MAPA MARKETING · REVISIÓN GRATIS';font-family:'DM Mono';
    font-size:6.8pt;letter-spacing:.16em;color:#9AA69E}
  @bottom-right{content:counter(page);font-family:'DM Mono';font-size:8pt;color:#55665F}}
@page cover{margin:0;@bottom-left{content:''}@bottom-right{content:''}}

body{font-family:'Public Sans';font-size:10.3pt;line-height:1.6;color:#12212E;margin:0}
h1,h2,h3{font-family:Archivo;letter-spacing:-.022em;line-height:1.1;color:#0E2233}
p{margin:0 0 .75em}
.sec{page-break-before:always}
.kick{font-family:'DM Mono';font-size:7.4pt;letter-spacing:.22em;color:#F0A81C;margin-bottom:3.5mm}
h2{font-size:22pt;font-weight:800;margin:0 0 6mm;padding-bottom:4mm;border-bottom:1.5pt solid #0E2233}
h3{font-size:11.6pt;font-weight:700;margin:7mm 0 2mm;page-break-after:avoid}
.lede{font-size:11.2pt;color:#44554E;max-width:150mm;margin-bottom:6mm}

.cover{page:cover;background:#07161F;color:#EFF1EC;width:215.9mm;height:279.4mm;
  position:relative;overflow:hidden;page-break-after:always}
.cover .g{position:absolute;inset:0;background-image:
  linear-gradient(rgba(239,241,236,.05) 1px,transparent 1px),
  linear-gradient(90deg,rgba(239,241,236,.05) 1px,transparent 1px);background-size:24mm 24mm}
.cover .in{position:absolute;left:22mm;right:22mm;top:28mm;bottom:22mm}
.cover .k{font-family:'DM Mono';font-size:8pt;letter-spacing:.3em;color:#93A7B2}
.cover .rule{width:26mm;border-top:2.4pt solid #F0A81C;margin:5mm 0 0}
.cover h1{font-size:38pt;font-weight:800;color:#EFF1EC;margin:60mm 0 0}
.cover .for{font-size:14pt;color:#25D366;margin-top:6mm;font-weight:600}
.cover .sub{font-size:11pt;color:#93A7B2;margin-top:3mm;max-width:130mm}
.cover .meta{position:absolute;bottom:0;left:0;right:0;font-family:'DM Mono';font-size:8pt;
  letter-spacing:.18em;color:#93A7B2;border-top:.6pt solid rgba(239,241,236,.22);padding-top:5mm}
.cover .meta span{float:right;color:#F0A81C}

.find{display:flex;gap:4mm;border-bottom:.5pt solid #D8DED2;padding-bottom:4mm;margin-bottom:4mm;
  page-break-inside:avoid}
.find .txt{flex:1}
.find h4{font-family:Archivo;font-size:11.2pt;font-weight:700;margin:0 0 1.5mm}
.find p{color:#44554E;font-size:9.9pt;margin:0}

.box{border:.6pt solid #C3CBBE;background:#EFF1EC;border-radius:2pt;padding:5mm 5.5mm;
  margin:5mm 0;page-break-inside:avoid}
.box b{display:block;font-family:'DM Mono';font-size:7.2pt;letter-spacing:.18em;
  text-transform:uppercase;color:#55665F;margin-bottom:2mm;font-weight:500}
.green{border-left:2.2pt solid #25D366;background:#EAF7EF;border-radius:0 2pt 2pt 0;
  padding:5mm 5.5mm;margin:5mm 0;page-break-inside:avoid}
.green b{display:block;font-family:'DM Mono';font-size:7.2pt;letter-spacing:.18em;
  text-transform:uppercase;color:#0E7C42;margin-bottom:2mm;font-weight:500}

.cta{background:#0E2233;color:#EFF1EC;border-radius:3pt;padding:11mm 10mm;margin-top:6mm}
.cta h3{color:#EFF1EC;font-size:18pt;margin:0 0 4mm}
.cta p{color:#93A7B2}
.cta .btn{display:inline-block;background:#25D366;color:#04231A;font-family:Archivo;
  font-weight:800;font-size:12pt;padding:4.4mm 9mm;border-radius:30pt;margin-top:4mm}
.cta .num{font-family:'DM Mono';font-size:11pt;color:#F0A81C;margin-top:5mm;letter-spacing:.08em}
""" + figs.FIG_CSS).replace('__F__', str(FONTS))


def build(c):
    fecha = c['fecha'] or datetime.date.today().strftime('%d/%m/%Y')
    graves = sum(1 for _, _, g in c['hallazgos'] if g == 3)
    P = []

    P.append(f'''<div class="cover"><div class="g"></div><div class="in">
      <div class="k">REVISIÓN DE VISIBILIDAD · {fecha}</div><div class="rule"></div>
      <h1>Cómo te ve tu ciudad hoy</h1>
      <div class="for">{c['negocio']}</div>
      <div class="sub">{c['oficio'].capitalize()} en {c['ciudad']}. Tu sitio, tu Perfil de
        Google, Apple Maps, Bing Places, Yelp y tus reseñas, revisados uno por uno.</div>
      <div class="meta">MAPA MARKETING · SIN COSTO<span>{WA_NUM}</span></div></div></div>''')

    # --------------------------------------------------------- calificación
    P.append(f'''<section class="sec"><div class="kick">01 · TU CALIFICACIÓN</div>
      <h2>Cómo saliste</h2>
      {figs.marcador(c['score'])}
      <p class="lede" style="text-align:center;margin:0 auto 8mm">Esta cifra junta todo lo que
      revisamos. No es una nota de tu trabajo: es qué tan fácil es encontrarte.</p>
      <h3>Por área</h3>
      {figs.barras_cat(c['areas'])}
      <div class="box"><b>Léelo así</b>
      Verde es que está bien y solo hay que mantenerlo. Amarillo es que existe pero está a
      medias. Rojo es que no está o está mal puesto, y ahí es donde se están yendo las
      llamadas.</div>
    </section>''')

    # --------------------------------------------------------- dónde sales
    P.append(f'''<section class="sec"><div class="kick">02 · DÓNDE SALES</div>
      <h2>El mapa de {c['ciudad']}</h2>
      <p class="lede">Esto es lo que ve alguien que busca {c['oficio']} en tu ciudad ahora
      mismo. Los tres de arriba se llevan la mayoría de las llamadas.</p>
      {figs.paquete(c['competidores'], c['negocio'], c['tu_posicion'])}
      <h3>Tus cuatro mapas</h3>
      {figs.fichas(c['mapas'])}
      <div class="box"><b>Por qué importan los cuatro</b>
      Quien trae iPhone y le pregunta a Siri está viendo Apple Maps, no Google. Bing alimenta
      a varios asistentes de IA. Y en Yelp todavía busca mucha gente contratistas. Cada mapa
      que falta es gente que no te ve existir.</div>
    </section>''')

    # --------------------------------------------------------- hallazgos
    finds = ''.join(f'<div class="find">{figs.severidad(g)}<div class="txt">'
                    f'<h4>{t}</h4><p>{d}</p></div></div>'
                    for t, d, g in c['hallazgos'])
    P.append(f'''<section class="sec"><div class="kick">03 · LO QUE ENCONTRAMOS</div>
      <h2>{len(c['hallazgos'])} cosas concretas</h2>
      <p class="lede">Los puntos rojos de la izquierda dicen qué tanto te está costando cada
      una. {graves} de estas son urgentes.</p>
      {finds}
    </section>''')

    # --------------------------------------------------------- prioridades
    P.append(f'''<section class="sec"><div class="kick">04 · POR DÓNDE EMPEZAR</div>
      <h2>En este orden</h2>
      <p class="lede">Si solo pudieras hacer tres cosas este mes, serían las tres primeras.
      La barra debajo de cada una es qué tanto mueve la aguja.</p>
      {figs.prioridades(c['prioridades'])}
      <div class="green"><b>Esto es tuyo</b>
      Esta lista es tuya, {c['contacto']}, la contrates o no. Si quieres hacerlo tú, la guía
      completa está gratis en nuestro sitio y explica cada punto paso a paso.</div>
    </section>''')

    # --------------------------------------------------------- siguiente paso
    P.append(f'''<section class="sec"><div class="kick">05 · SI QUIERES QUE LO HAGAMOS</div>
      <h2>Qué seguiría</h2>
      <p class="lede">Arreglar esto son entre diez y quince horas al mes, todos los meses,
      además de correr tu negocio. Si tienes esas horas, tómalas. Si no, esto es lo que
      haríamos nosotros.</p>
      {figs.tres_factores()}
      <p>Google ordena los resultados locales con esas tres cosas y lo publica. La distancia
      no la controlas. Las otras dos son justo las que tienes flojas, y son en las que
      trabajaríamos desde el primer mes.</p>
      <div class="cta">
        <h3>¿Te mando la propuesta, {c['contacto']}?</h3>
        <p>Con el plan completo, los tiempos y lo que cuesta. Si tienes dudas de cualquier
        punto de esta revisión, pregúntalas por WhatsApp: te contestamos el mismo día.</p>
        <div class="btn">Escríbenos por WhatsApp</div>
        <div class="num">{WA_NUM}</div>
      </div>
    </section>''')

    html = ('<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">'
            f'<title>Revisión · {c["negocio"]}</title><style>{CSS}</style></head>'
            f'<body>{"".join(P)}</body></html>')
    slug = c['negocio'].lower().replace(' ', '-')
    for ch in 'áéíóúñ':
        slug = slug.replace(ch, 'aeioun'['áéíóúñ'.index(ch)])
    out = OUTDIR / ('revision-%s.pdf' % slug)
    HTML(string=html, base_url=str(ROOT)).write_pdf(out)
    print('escrito', out.name)
    return out


if __name__ == '__main__':
    build(NEGOCIO)
