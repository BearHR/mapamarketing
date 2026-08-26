# -*- coding: utf-8 -*-
"""Propuesta para cliente — MAPA Marketing.

Llena el diccionario CLIENTE de abajo y corre:
    python3 _build/make_proposal.py
Salida: propuestas/propuesta-<negocio>.pdf  (y la versión en inglés si IDIOMAS lo pide)
"""
import pathlib, datetime
from weasyprint import HTML

ROOT = pathlib.Path('/home/claude/mapa')
FONTS = pathlib.Path('/home/claude/ads/fonts')
OUTDIR = ROOT / 'propuestas'; OUTDIR.mkdir(exist_ok=True)

WA_NUM = '+1 (726) 255-6888'
WA_URL = 'https://wa.me/17262556888'

# ===========================================================================
# LLENA ESTO PARA CADA CLIENTE
# ===========================================================================
CLIENTE = dict(
    negocio      = 'Ramírez Plumbing',
    contacto     = 'Luis',
    oficio       = 'plomería',
    ciudad       = 'Houston',
    ciudades     = ['Houston', 'Katy', 'Sugar Land'],
    servicios    = ['Reparación de fugas', 'Destape de drenajes',
                    'Calentadores de agua', 'Remodelación de baño'],
    equipo       = '3 personas',
    fecha        = None,                 # None = hoy

    # Lo que te dijo que quiere lograr, en sus palabras. Déjalo en None si no lo tienes.
    meta         = 'meter a un técnico más sin que el trabajo se caiga en los meses flojos',

    # --- HALLAZGOS DE LA AUDITORÍA ---------------------------------------
    # Lista vacía [] si todavía no auditaste: la sección se cambia sola por
    # "qué vamos a revisar" y la propuesta sigue funcionando.
    hallazgos = [
        ('El sitio tarda 6.4 segundos en cargar en celular',
         'Más de la mitad de la gente se va antes de que termine de abrir. Y como casi todos '
         'te buscan desde el teléfono, esa es la puerta principal del negocio.'),
        ('Hay una sola página de “Servicios” para los cuatro trabajos',
         'Google manda a la gente a páginas, no a sitios. Sin una página por servicio y ciudad, '
         'no hay nada que pueda salir cuando alguien busca “destape de drenajes en Katy”.'),
        ('El Perfil de Negocio de Google tiene la categoría equivocada',
         'Está como “Contratista general”. La categoría principal es lo que más pesa en el '
         'paquete de tres del mapa, y esa sola línea te deja fuera de las búsquedas de plomería.'),
        ('No apareces en Apple Maps ni en Bing Places',
         'Todo el que usa iPhone y le pregunta a Siri no te ve. Bing además alimenta a varios '
         'asistentes de IA, así que también te deja fuera de ahí.'),
        ('Tu teléfono aparece de tres maneras distintas en internet',
         'Google no está seguro de cuál eres tú y, ante la duda, te baja en el mapa.'),
    ],

    # --- COMPETENCIA -----------------------------------------------------
    # Lista vacía [] y la sección se omite completa.
    competidores = [
        ('Competidor 1', '128 reseñas', 'Sale 1º en el mapa'),
        ('Competidor 2', '86 reseñas',  'Sale 2º en el mapa'),
        ('Competidor 3', '54 reseñas',  'Sale 3º en el mapa'),
    ],
    tu_posicion = 'Fuera del mapa · página 3 en búsqueda',

    # --- NÚMEROS PARA EL PUNTO DE EQUILIBRIO -----------------------------
    # Pon ticket = None si no te dio cifras: se omite la página de la cuenta.
    ticket       = 450,
    cierre       = 40,
    repeticion   = 1.5,

    # --- LA OFERTA -------------------------------------------------------
    # 'ambas'     = muestra las dos opciones (recomendado, la comparación vende sola)
    # 'programa'  = solo el compromiso con sitio incluido
    # 'separado'  = solo sitio aparte + mensual sin compromiso
    oferta           = 'ambas',
    precio_web       = 1500,
    precio_mensual   = 1200,
    meses_compromiso = 4,
)

IDIOMAS = ['es']          # ['es'] o ['es', 'en']


# ===========================================================================
CSS = """
@font-face{font-family:Archivo;src:url('file://__F__/Archivo-700.ttf');font-weight:700}
@font-face{font-family:Archivo;src:url('file://__F__/Archivo-800.ttf');font-weight:800}
@font-face{font-family:Archivo;src:url('file://__F__/Archivo-900.ttf');font-weight:900}
@font-face{font-family:'Public Sans';src:url('file://__F__/PublicSans-400.ttf');font-weight:400}
@font-face{font-family:'Public Sans';src:url('file://__F__/PublicSans-600.ttf');font-weight:600}
@font-face{font-family:'DM Mono';src:url('file://__F__/DMMono-500.ttf');font-weight:500}

@page{size:Letter;margin:19mm 18mm 16mm 18mm;
  @bottom-left{content:'MAPA MARKETING · PROPUESTA';font-family:'DM Mono';font-size:6.8pt;
    letter-spacing:.16em;color:#9AA69E}
  @bottom-right{content:counter(page);font-family:'DM Mono';font-size:8pt;color:#55665F}}
@page cover{margin:0;@bottom-left{content:''}@bottom-right{content:''}}

body{font-family:'Public Sans';font-size:10.3pt;line-height:1.6;color:#12212E;margin:0}
h1,h2,h3{font-family:Archivo;letter-spacing:-.022em;line-height:1.1;color:#0E2233}
p{margin:0 0 .75em}
strong,b{font-weight:600}
.sec{page-break-before:always}
.kick{font-family:'DM Mono';font-size:7.4pt;letter-spacing:.22em;color:#F0A81C;margin-bottom:3.5mm}
h2{font-size:22pt;font-weight:800;margin:0 0 6mm;padding-bottom:4mm;border-bottom:1.5pt solid #0E2233}
h3{font-size:11.6pt;font-weight:700;margin:7mm 0 2mm;page-break-after:avoid}
.lede{font-size:11.4pt;color:#44554E;max-width:150mm;margin-bottom:6mm}

/* portada */
.cover{page:cover;background:#07161F;color:#EFF1EC;width:215.9mm;height:279.4mm;
  position:relative;overflow:hidden;page-break-after:always}
.cover .g{position:absolute;inset:0;background-image:
  linear-gradient(rgba(239,241,236,.05) 1px,transparent 1px),
  linear-gradient(90deg,rgba(239,241,236,.05) 1px,transparent 1px);background-size:24mm 24mm}
.cover .in{position:absolute;left:22mm;right:22mm;top:28mm;bottom:22mm}
.cover .k{font-family:'DM Mono';font-size:8pt;letter-spacing:.3em;color:#93A7B2}
.cover .rule{width:26mm;border-top:2.4pt solid #F0A81C;margin:5mm 0 0}
.cover h1{font-size:36pt;font-weight:800;color:#EFF1EC;margin:58mm 0 0}
.cover .for{font-size:14pt;color:#25D366;margin-top:6mm;font-weight:600}
.cover .sub{font-size:11pt;color:#93A7B2;margin-top:3mm;max-width:130mm}
.cover .meta{position:absolute;bottom:0;left:0;right:0;font-family:'DM Mono';font-size:8pt;
  letter-spacing:.18em;color:#93A7B2;border-top:.6pt solid rgba(239,241,236,.22);padding-top:5mm}
.cover .meta span{float:right;color:#F0A81C}

/* hallazgos */
.find{border-left:2.2pt solid #DD4B34;padding:0 0 0 5mm;margin:0 0 6mm;page-break-inside:avoid}
.find h4{font-family:Archivo;font-size:11.4pt;font-weight:700;margin:0 0 1.5mm;color:#0E2233}
.find p{color:#44554E;font-size:10pt;margin:0}

table{width:100%;border-collapse:collapse;font-size:9.8pt;margin:4mm 0;page-break-inside:avoid}
th,td{text-align:left;padding:2.6mm 2.8mm;border-bottom:.5pt solid #D8DED2;vertical-align:top}
th{font-family:'DM Mono';font-size:7.2pt;letter-spacing:.13em;text-transform:uppercase;
  color:#55665F;font-weight:500;border-bottom:1pt solid #0E2233}
td.n{font-family:'DM Mono';white-space:nowrap}
tr.you td{background:#FDF3E0;font-weight:600}
tr.tot td{border-top:1.2pt solid #0E2233;border-bottom:0;font-weight:600;font-size:10.6pt}

.phase{display:flex;gap:6mm;margin-bottom:5mm;page-break-inside:avoid}
.phase .num{font-family:Archivo;font-weight:900;font-size:20pt;color:#F0A81C;width:16mm;
  line-height:1;flex:none}
.phase h4{font-family:Archivo;font-size:11.6pt;font-weight:700;margin:0 0 1.5mm}
.phase p{color:#44554E;font-size:10pt;margin:0}

ul{margin:0 0 1em;padding-left:5mm}
li{margin-bottom:1.6mm}

.box{border:.6pt solid #C3CBBE;background:#EFF1EC;border-radius:2pt;padding:5mm 5.5mm;
  margin:5mm 0;page-break-inside:avoid}
.box b{display:block;font-family:'DM Mono';font-size:7.2pt;letter-spacing:.18em;
  text-transform:uppercase;color:#55665F;margin-bottom:2mm;font-weight:500}
.green{border-left:2.2pt solid #25D366;background:#EAF7EF;border-radius:0 2pt 2pt 0;
  padding:5mm 5.5mm;margin:5mm 0;page-break-inside:avoid}
.green b{display:block;font-family:'DM Mono';font-size:7.2pt;letter-spacing:.18em;
  text-transform:uppercase;color:#0E7C42;margin-bottom:2mm;font-weight:500}

.big{background:#0E2233;color:#EFF1EC;border-radius:3pt;padding:9mm 10mm;margin:6mm 0}
.big h3{color:#EFF1EC;margin:0 0 3mm;font-size:15pt}
.big p{color:#93A7B2;margin:0}
.big .price{font-family:Archivo;font-weight:900;font-size:30pt;color:#25D366;
  letter-spacing:-.03em;line-height:1;margin:4mm 0 2mm}
.big .price small{font-family:'Public Sans';font-size:11pt;color:#93A7B2;font-weight:400;
  letter-spacing:0}
.strike{color:#93A7B2;text-decoration:line-through}

.cta{background:#0E2233;color:#EFF1EC;border-radius:3pt;padding:11mm 10mm;margin-top:6mm}
.cta h3{color:#EFF1EC;font-size:18pt;margin:0 0 4mm}
.cta p{color:#93A7B2}
.cta .btn{display:inline-block;background:#25D366;color:#04231A;font-family:Archivo;
  font-weight:800;font-size:12pt;padding:4.4mm 9mm;border-radius:30pt;margin-top:4mm}
.cta .num{font-family:'DM Mono';font-size:11pt;color:#F0A81C;margin-top:5mm;letter-spacing:.08em}

/* gráficos */
.fig{width:100%;height:auto;margin:5mm 0 6mm;display:block}
.fig .lbl{font-family:'DM Mono';font-size:11px;letter-spacing:1.6px;fill:#55665F}
.fig .cap{font-family:'Public Sans';font-size:12px;fill:#55665F}
.fig .row{font-family:'Public Sans';font-size:15px;font-weight:600;fill:#0E2233}
.fig .stp{font-family:Archivo;font-size:14px;font-weight:700;fill:#0E2233}
.fig .pin{font-family:Archivo;font-size:13px;font-weight:800;fill:#fff;text-anchor:middle}
.fig .val{font-family:Archivo;font-size:15px;font-weight:800;fill:#0E2233}
.fig .big{font-family:Archivo;font-size:21px;font-weight:900;fill:#0E2233}
.sev{width:16mm;height:auto;flex:none;margin-top:1.5mm}
.find{display:flex;gap:4mm;border-left:0;padding:0;border-bottom:.5pt solid #D8DED2;
  padding-bottom:4mm;margin-bottom:4mm}
.find .txt{flex:1}
""".replace('__F__', str(FONTS))


def money(n):
    return '$' + format(int(round(n)), ',d')

# ===========================================================================
# GRÁFICOS (SVG en línea — WeasyPrint los dibuja como vectores)
# ===========================================================================
INKC, SUNC, WAC, CLAYC, RULEC, MUTEDC = '#0E2233', '#F0A81C', '#25D366', '#DD4B34', '#D8DED2', '#55665F'


def svg_barras(pct_llega=45):
    """Capacidad contra demanda."""
    return f'''<svg viewBox="-14 0 628 200" class="fig">
      <text x="0" y="14" class="lbl">LO QUE PUEDES HACER</text>
      <rect x="0" y="24" width="600" height="38" rx="6" fill="#EFF1EC"/>
      <rect x="0" y="24" width="600" height="38" rx="6" fill="{WAC}"/>
      <text x="0" y="102" class="lbl">LO QUE TE ESTÁ LLEGANDO HOY</text>
      <rect x="0" y="112" width="600" height="38" rx="6" fill="#EFF1EC"/>
      <rect x="0" y="112" width="{6*pct_llega}" height="38" rx="6" fill="{SUNC}"/>
      <line x1="{6*pct_llega}" y1="106" x2="{6*pct_llega}" y2="172" stroke="{CLAYC}" stroke-width="2"/>
      <line x1="600" y1="106" x2="600" y2="172" stroke="{CLAYC}" stroke-width="2"/>
      <line x1="{6*pct_llega}" y1="168" x2="600" y2="168" stroke="{CLAYC}" stroke-width="2"/>
      <text x="{(6*pct_llega+600)/2}" y="192" class="cap" text-anchor="middle" fill="{CLAYC}">lo que estás dejando ir</text>
    </svg>'''


def svg_rank(competidores, negocio, pos_txt):
    """Paquete de tres del mapa, con el cliente fuera."""
    rows = ''
    for i, (n, r, _) in enumerate(competidores[:3]):
        y = i * 52
        rows += (f'<rect x="0" y="{y}" width="600" height="42" rx="6" fill="#EFF1EC"/>'
                 f'<circle cx="26" cy="{y+21}" r="13" fill="#9AA69E"/>'
                 f'<text x="26" y="{y+26}" class="pin">{i+1}</text>'
                 f'<text x="56" y="{y+26}" class="row">{n}</text>'
                 f'<text x="590" y="{y+26}" class="row" text-anchor="end" fill="{MUTEDC}">{r}</text>')
    y = 3 * 52 + 14
    rows += (f'<rect x="0" y="{y}" width="600" height="42" rx="6" fill="none" '
             f'stroke="{CLAYC}" stroke-width="2.5"/>'
             f'<circle cx="26" cy="{y+21}" r="13" fill="{CLAYC}"/>'
             f'<text x="26" y="{y+26}" class="pin">?</text>'
             f'<text x="56" y="{y+26}" class="row" fill="{CLAYC}">{negocio}</text>'
             f'<text x="590" y="{y+26}" class="row" text-anchor="end" fill="{CLAYC}">{pos_txt}</text>')
    return f'<svg viewBox="0 0 600 {y+52}" class="fig">{rows}</svg>'


def svg_ruta(pasos):
    """Línea de tiempo horizontal con paradas."""
    n = len(pasos)
    x0, x1 = 72, 528
    out = f'<line x1="{x0}" y1="26" x2="{x1}" y2="26" stroke="{RULEC}" stroke-width="3"/>'
    for i, (t, sub) in enumerate(pasos):
        cx = x0 + (x1 - x0) / (n - 1) * i if n > 1 else 300
        col = WAC if i == 0 else INKC
        out += (f'<circle cx="{cx}" cy="26" r="13" fill="{col}"/>'
                f'<text x="{cx}" y="31" class="pin">{i+1}</text>'
                f'<text x="{cx}" y="60" class="stp" text-anchor="middle">{t}</text>'
                f'<text x="{cx}" y="77" class="cap" text-anchor="middle">{sub}</text>')
    return f'<svg viewBox="0 0 600 88" class="fig">{out}</svg>'


def svg_curva(meses=4):
    """Curva de qué esperar: plano al principio, arriba después."""
    pts = [(0, 96), (150, 88), (300, 68), (450, 38), (600, 10)]
    path = 'M' + ' L'.join(f'{x},{y}' for x, y in pts)
    area = path + ' L600,110 L0,110 Z'
    marks = ''
    for i, (x, y) in enumerate(pts[:5]):
        lbl = ['Hoy', 'Mes 1', 'Mes 2', f'Mes {meses-1}', f'Mes {meses}'][i]
        marks += (f'<circle cx="{x}" cy="{y}" r="5" fill="{INKC}"/>'
                  f'<text x="{x}" y="132" class="cap" text-anchor="middle">{lbl}</text>')
    return f'''<svg viewBox="-16 0 632 142" class="fig">
      <line x1="0" y1="110" x2="600" y2="110" stroke="{RULEC}" stroke-width="1.5"/>
      <path d="{area}" fill="rgba(37,211,102,.14)"/>
      <path d="{path}" fill="none" stroke="{WAC}" stroke-width="3.5" stroke-linecap="round"/>
      {marks}
      <text x="0" y="14" class="lbl">CLIENTES QUE TE ENCUENTRAN SOLOS</text>
    </svg>'''


def svg_equilibrio(valor, pm):
    """Barras: costo mensual contra lo que valen 3, 6 y 10 contactos."""
    vals = [('3 contactos', valor * 3), ('6 contactos', valor * 6), ('10 contactos', valor * 10)]
    top = max(max(v for _, v in vals), pm) * 1.12
    bars = ''
    bw, gap = 118, 42
    for i, (lbl, v) in enumerate(vals):
        x = 150 + i * (bw + gap)
        h = 150 * v / top
        bars += (f'<rect x="{x}" y="{170-h}" width="{bw}" height="{h}" rx="5" fill="{WAC}"/>'
                 f'<text x="{x+bw/2}" y="{164-h}" class="val" text-anchor="middle">'
                 f'{money(v)}</text>'
                 f'<text x="{x+bw/2}" y="190" class="cap" text-anchor="middle">{lbl}</text>')
    hc = 150 * pm / top
    return f'''<svg viewBox="0 0 600 205" class="fig">
      <line x1="0" y1="170" x2="600" y2="170" stroke="{RULEC}" stroke-width="1.5"/>
      <rect x="10" y="{170-hc}" width="{bw}" height="{hc}" rx="5" fill="{INKC}"/>
      <text x="{10+bw/2}" y="{164-hc}" class="val" text-anchor="middle">{money(pm)}</text>
      <text x="{10+bw/2}" y="190" class="cap" text-anchor="middle">lo que pagas</text>
      <line x1="0" y1="{170-hc}" x2="600" y2="{170-hc}" stroke="{INKC}"
            stroke-width="1.5" stroke-dasharray="5 5"/>
      {bars}
    </svg>'''


def svg_opciones(total_a, total_b, meses, pm, pw):
    """Comparación visual de las dos rutas."""
    top = max(total_a, total_b) * 1.16
    ha, hb = 130 * total_a / top, 130 * total_b / top
    return f'''<svg viewBox="0 0 600 210" class="fig">
      <text x="150" y="14" class="lbl" text-anchor="middle">OPCIÓN A · {meses} MESES</text>
      <text x="450" y="14" class="lbl" text-anchor="middle">OPCIÓN B · SIN COMPROMISO</text>
      <rect x="60" y="{160-ha}" width="180" height="{ha}" rx="6" fill="{WAC}"/>
      <rect x="360" y="{160-hb}" width="180" height="{hb}" rx="6" fill="#B9C2BA"/>
      <text x="150" y="{152-ha}" class="big" text-anchor="middle">{money(total_a)}</text>
      <text x="450" y="{152-hb}" class="big" text-anchor="middle">{money(total_b)}</text>
      <line x1="0" y1="160" x2="600" y2="160" stroke="{RULEC}" stroke-width="1.5"/>
      <text x="150" y="182" class="cap" text-anchor="middle">{meses} meses de marketing</text>
      <text x="150" y="200" class="cap" text-anchor="middle">sitio incluido</text>
      <text x="450" y="182" class="cap" text-anchor="middle">{meses-1} meses de marketing</text>
      <text x="450" y="200" class="cap" text-anchor="middle">sitio {money(pw)} aparte</text>
    </svg>'''


def svg_severidad(n):
    """Tres puntos de gravedad."""
    out = ''
    for i in range(3):
        col = CLAYC if i < n else '#D8DED2'
        out += f'<circle cx="{9+i*22}" cy="9" r="7" fill="{col}"/>'
    return f'<svg viewBox="0 0 62 18" class="sev">{out}</svg>'


def build(c, lang='es'):
    fecha = c['fecha'] or datetime.date.today().strftime('%d/%m/%Y')
    ciudades = ', '.join(c['ciudades']) if c.get('ciudades') else c.get('ciudad', '')
    servicios = c.get('servicios') or []
    n_pag = len(servicios) * len(c.get('ciudades') or [1]) if servicios else None
    meses = c['meses_compromiso']
    pm, pw = c['precio_mensual'], c['precio_web']
    modo = c.get('oferta', 'ambas')

    tiene_cuenta = bool(c.get('ticket'))
    if tiene_cuenta:
        valor = c['ticket'] * (c['cierre'] / 100) * c.get('repeticion', 1)
        equil = pm / valor

    # Comparación de las dos rutas en el mismo periodo
    total_a = pm * meses                      # sitio incluido, trabajo mensual desde el mes 1
    total_b = pw + pm * (meses - 1)           # mes 1 solo el sitio, mensual desde el mes 2
    P = []

    # ------------------------------------------------------------- portada
    P.append(f'''<div class="cover"><div class="g"></div><div class="in">
      <div class="k">PROPUESTA · {fecha}</div><div class="rule"></div>
      <h1>Cómo llenamos tu semana de trabajo</h1>
      <div class="for">Preparada para {c['negocio']}</div>
      <div class="sub">{c['oficio'].capitalize()} en {ciudades}. Plan de trabajo, tiempos,
        lo que incluye y lo que cuesta.</div>
      <div class="meta">MAPA MARKETING<span>{WA_NUM}</span></div></div></div>''')

    # ------------------------------------------------------- 1. de dónde partimos
    filas = [('El negocio', f"{c['negocio']}, {c['oficio']}" +
              (f", {c['equipo']}" if c.get('equipo') else ''))]
    if ciudades:
        filas.append(('Dónde trabaja', ciudades))
    if servicios:
        filas.append(('Qué vende', ', '.join(servicios)))
    filas.append(('De dónde salen<br>los clientes hoy',
                  'Recomendaciones y clientes que regresan'))
    if c.get('meta'):
        filas.append(('Qué quieres<br>lograr', f"<b>{c['meta'].capitalize()}</b>"))
    tabla = ''.join(f'<tr><th>{k}</th><td>{v}</td></tr>' for k, v in filas)
    P.append(f'''<section class="sec"><div class="kick">01 · DE DÓNDE PARTIMOS</div>
      <h2>Lo que nos dijiste</h2>
      <p class="lede">Antes de proponerte nada, esto es lo que entendimos de las
      conversaciones que tuvimos. Si algo aquí está mal, dínoslo y lo corregimos antes
      de seguir.</p>
      <table>{tabla}</table>
      {svg_barras(45)}
      <div class="box"><b>El punto</b>
      Tu problema no es hacer el trabajo. Es que el trabajo llegue solo y llegue parejo,
      para que puedas planear en vez de esperar. Todo lo que sigue va dirigido a eso.</div>
    </section>''')

    # ------------------------------------------------------- 2. hallazgos o alcance
    if c.get('hallazgos'):
        n_h = len(c['hallazgos'])
        finds = ''.join(
            '<div class="find">%s<div class="txt"><h4>%s</h4><p>%s</p></div></div>'
            % (svg_severidad(3 if i < n_h / 3 else (2 if i < 2 * n_h / 3 else 1)), t, d)
            for i, (t, d) in enumerate(c['hallazgos']))
        P.append(f'''<section class="sec"><div class="kick">02 · LA REVISIÓN</div>
          <h2>Qué encontramos</h2>
          <p class="lede">Esto es lo que vimos al revisar tu sitio, tu Perfil de Negocio de
          Google, Apple Maps, Bing Places, Yelp y tus reseñas. Son {len(c['hallazgos'])} cosas
          concretas, en orden de qué tanto te está costando cada una.</p>
          {finds}
          <div class="green"><b>La buena noticia</b>
          Ninguna de estas es un problema de tu oficio ni de tu reputación. Todas son de
          configuración y de contenido, y todas se arreglan. Ese es el trabajo que
          proponemos.</div></section>''')
    else:
        P.append('''<section class="sec"><div class="kick">02 · LA REVISIÓN</div>
          <h2>Qué vamos a revisar</h2>
          <p class="lede">Lo primero que hacemos, antes de tocar nada, es una revisión
          completa. Te la mandamos por WhatsApp en lenguaje normal: esto tienes, esto te
          falta, esto tienen los que salen arriba de ti.</p>
          <ul>
            <li><b>Tu sitio web:</b> velocidad real en celular, estructura de páginas, textos
              y qué tan fácil es contactarte.</li>
            <li><b>Tu Perfil de Negocio de Google:</b> categoría principal, servicios,
              descripción, atributos, horarios, área de servicio, fotos y publicaciones.</li>
            <li><b>Los otros tres mapas:</b> Apple Maps, Bing Places y Yelp.</li>
            <li><b>Tus datos:</b> si tu nombre, dirección y teléfono coinciden en todos lados
              y qué fichas viejas andan sueltas con información equivocada.</li>
            <li><b>Tus reseñas:</b> cuántas, qué tan recientes y cuáles están sin responder.</li>
            <li><b>La IA:</b> si te menciona cuando alguien pregunta por tu servicio.</li>
            <li><b>Tu competencia:</b> los tres que salen arriba de ti y por qué.</li>
          </ul>
          <div class="green"><b>Sin costo</b>
          Esta revisión es gratis y es tuya, la contrates o no.</div></section>''')

    # ------------------------------------------------------- 3. competencia
    if c.get('competidores'):
        comp = ''.join(f'<tr><td>{n}</td><td class="n">{r}</td><td>{pos}</td></tr>'
                       for n, r, pos in c['competidores'])
        P.append(f'''<section class="sec"><div class="kick">03 · CONTRA QUIÉN COMPITES</div>
          <h2>Dónde estás parado hoy</h2>
          <p class="lede">Estos son los negocios que salen arriba de ti cuando alguien busca
          {c['oficio']} en {c.get('ciudad','tu ciudad')}. No trabajan mejor que tú. Están mejor
          puestos.</p>
          {svg_rank(c['competidores'], c['negocio'], c.get('tu_posicion','—'))}
          <h3>Por qué ellos y no tú</h3>
          <p>Google ordena los resultados locales con tres cosas, y las publica:
          <b>relevancia</b> (qué tanto coincides con lo que la persona escribió),
          <b>distancia</b> (qué tan cerca estás) y <b>prominencia</b> (qué tan conocido eres
          fuera de tu propio sitio).</p>
          <p>La distancia no la controlas. Las otras dos sí, y son justo las que ellos tienen
          trabajadas y tú no: categorías correctas, una página por servicio y ciudad, reseñas
          recientes y datos consistentes en todas las plataformas.</p></section>''')

    # ------------------------------------------------------- 4. el plan
    pag_txt = (f'Con {len(servicios)} servicios en {len(c["ciudades"])} ciudades son '
               f'<b>{n_pag} páginas de servicio y ciudad</b>, más las de apoyo. '
               'Las priorizamos por cuál te deja más dinero.') if n_pag else \
              ('Definimos una página por cada servicio en cada ciudad donde trabajas, más las '
               'de apoyo, y las priorizamos por cuál te deja más dinero.')
    mes1 = ('<b>El sitio y el trabajo mensual arrancan juntos.</b> Mientras construimos el '
            'sitio ya estamos arreglando tu Perfil de Google y los otros mapas, así que no '
            'pierdes el primer mes.') if modo != 'separado' else \
           ('<b>El primer mes se va completo en el sitio.</b> Cuando el sitio se paga por '
            'separado, ese mes se dedica a construirlo bien; el trabajo mensual arranca '
            'en el mes 2.')
    P.append(f'''<section class="sec"><div class="kick">04 · EL PLAN</div>
      <h2>Qué haríamos, en qué orden</h2>
      <p class="lede">El orden importa. Mandar gente a un sitio que no convierte es tirar
      dinero, y arreglar perfiles sin un sitio detrás te deja a medio camino.</p>
      {svg_ruta([('Mapa de páginas','Semana 1'), ('El sitio','Semanas 2–4'),
                 ('Los 4 mapas','Semana 4'), ('El ritmo','Cada mes')])}
      <div class="phase"><div class="num">01</div><div>
        <h4>Semana 1 · El mapa de páginas</h4>
        <p>Definimos qué páginas se construyen y para qué búsqueda es cada una. {pag_txt}</p></div></div>
      <div class="phase"><div class="num">02</div><div>
        <h4>Semanas 2 a 4 · El sitio</h4>
        <p>Escribimos y construimos el sitio completo. Rápido en celular, con el botón de
        contacto siempre a la vista y armado para que Google entienda qué vendes y dónde.
        Tú lo revisas antes de que salga al aire.</p></div></div>
      <div class="phase"><div class="num">03</div><div>
        <h4>Los cuatro mapas</h4>
        <p>Arreglamos la categoría de tu Perfil de Google, reclamamos Apple Maps y Bing
        Places, ordenamos Yelp y fijamos un solo formato de nombre, dirección y teléfono.
        Buscamos y corregimos las fichas viejas con datos equivocados.</p></div></div>
      <div class="phase"><div class="num">04</div><div>
        <h4>Cada mes · El ritmo</h4>
        <p>Contenido nuevo respondiendo lo que preguntan tus clientes, publicaciones y fotos
        en los mapas, revisión de mapas de calor para mejorar el sitio, citaciones, enlaces
        locales cuando hacen falta, y un reporte que se entiende.</p></div></div>
      <div class="box"><b>Sobre el primer mes</b>{mes1}</div>
    </section>''')

    # ------------------------------------------------------- 5. tiempos
    P.append(f'''<section class="sec"><div class="kick">05 · TIEMPOS</div>
      <h2>Qué esperar, mes a mes</h2>
      <p class="lede">Esto es un rango normal para trabajo local, no una promesa. Tu zona,
      tu competencia y qué tan rápido contestes el teléfono mueven mucho el resultado.</p>
      {svg_curva(meses)}
      <table><thead><tr><th>Periodo</th><th>Qué se suele mover</th></tr></thead><tbody>
      <tr><td class="n">Mes 1</td><td>Sitio en línea y perfiles completos. Suelen subir las
        vistas del perfil de Google y las solicitudes de indicaciones, porque el perfil por
        fin está bien puesto.</td></tr>
      <tr><td class="n">Mes 2</td><td>Las primeras páginas empiezan a aparecer en búsquedas
        específicas. El mapa se mueve primero en las zonas más cercanas a ti.</td></tr>
      <tr><td class="n">Mes 3</td><td>Más páginas entrando y las señales empiezan a
        acumularse. Suele ser cuando aparecen los primeros contactos que no vienen de
        recomendación.</td></tr>
      <tr><td class="n">Mes 4</td><td>Es cuando normalmente ya se nota en el teléfono y se
        puede ver si la tendencia va para arriba.</td></tr>
      <tr><td class="n">Mes 5 en<br>adelante</td><td>Se amplía el radio: empiezas a salir en
        ciudades vecinas. El contenido viejo sigue trayendo clientes sin costo adicional.</td></tr>
      </tbody></table>
      <div class="box"><b>Sé honesto contigo mismo antes de firmar</b>
      Los primeros dos meses vas a pagar y ver poco. Es lo normal y por eso los
      {meses} meses son el mínimo: antes de eso no hay forma de saber si funciona. Al mes
      {meses} ya se ve la tendencia, aunque el trabajo local sigue creciendo después. Si
      necesitas clientes para el mes que entra, esto no es lo tuyo y preferimos decírtelo
      ahora.</div>
    </section>''')

    # ------------------------------------------------------- 6. la cuenta
    if tiene_cuenta:
        P.append(f'''<section class="sec"><div class="kick">06 · LA CUENTA</div>
          <h2>Cuánto tiene que traerte para valer la pena</h2>
          <p class="lede">Con los números que nos diste, esto es lo que necesita pasar para
          que esto se pague solo. Sin adornos.</p>
          <table><tbody>
          <tr><td>Trabajo promedio</td><td class="n">{money(c['ticket'])}</td></tr>
          <tr><td>De cada 100 que te contactan, cierras</td><td class="n">{c['cierre']}%</td></tr>
          <tr><td>Trabajos por cliente en su vida</td><td class="n">{c.get('repeticion',1)}</td></tr>
          <tr class="tot"><td>Cada contacto nuevo vale</td><td class="n">{money(valor)}</td></tr>
          </tbody></table>
          <div class="big"><h3>El punto de equilibrio</h3>
            <div class="price">{equil:.1f} <small>contactos más al mes</small></div>
            <p>Con eso el trabajo mensual se paga solo. Todo lo que llegue arriba de esa cifra
            es ganancia tuya.</p></div>
          <h3>Lo que valen más contactos, al mes</h3>
          {svg_equilibrio(valor, pm)}
          <p style="font-size:9.6pt">La línea punteada es lo que pagas. Todo lo que sobresale
          por encima es tuyo. Al año, seis contactos más al mes son
          <b>{money(valor*72)}</b>.</p>
          <p style="font-size:9.4pt;color:#55665F">Son estimaciones hechas con tus propias
          cifras, no una promesa de resultados. Sirven para una cosa: decidir si el número
          tiene sentido para tu negocio.</p></section>''')

    # ------------------------------------------------------- 7. inversión
    inc = f'''<h3>Qué incluye el trabajo mensual</h3>
      <ul>
        <li><b>Los cuatro mapas:</b> Perfil de Negocio de Google, Apple Maps, Bing Places y
          Yelp, reclamados, corregidos y mantenidos.</li>
        <li><b>Contenido cada mes</b> respondiendo lo que preguntan tus clientes.</li>
        <li><b>Publicaciones y fotos</b> nuevas cada mes en los mapas que las aceptan.</li>
        <li><b>Citaciones:</b> construcción al arrancar y limpieza de fichas viejas.</li>
        <li><b>Enlaces locales</b> de sitios reales, cuando tu zona lo pide.</li>
        <li><b>Mapas de calor</b> y ajustes al sitio con base en lo que hace la gente.</li>
        <li><b>Reporte mensual</b> por WhatsApp, en español, que se entiende sin diccionario.</li>
      </ul>
      <h3>Qué incluye el sitio web</h3>
      <p>{('Las ' + str(n_pag) + ' páginas de servicio y ciudad') if n_pag else 'Una página por cada servicio en cada ciudad'}
      más las de apoyo, rápido en celular, armado para buscadores y con el botón de contacto
      siempre a la vista. Dominio y hospedaje a tu nombre. Es tuyo desde el primer día.</p>'''

    card_a = f'''<div class="big"><h3>Opción A · {meses} meses</h3>
        <div class="price">{money(pm)}<small> al mes × {meses} meses</small></div>
        <p><b style="color:#EFF1EC">El sitio web va incluido sin costo</b> — por separado serían
        <span class="strike">{money(pw)}</span>. Se construye encima del mes 1, así que el
        trabajo mensual arranca desde el día uno.</p></div>'''

    card_b = f'''<div class="box"><b>Opción B · Sin compromiso</b>
        <p style="font-size:13pt;font-family:Archivo;font-weight:800;margin:2mm 0 3mm">
        {money(pw)} el sitio + {money(pm)} al mes</p>
        <p>Pagas el sitio por separado y el mes 1 se dedica completo a construirlo. El trabajo
        mensual arranca en el mes 2 y lo puedes parar cuando quieras.</p></div>'''

    if modo == 'ambas':
        cmp_tbl = f'''<h3>Las dos, lado a lado</h3>
          {svg_opciones(total_a, total_b, meses, pm, pw)}
          <table><thead><tr><th></th><th>Opción A · {meses} meses</th><th>Opción B · sin compromiso</th></tr></thead>
          <tbody>
          <tr><td>Sitio web</td><td class="n">Incluido</td><td class="n">{money(pw)}</td></tr>
          <tr><td>Trabajo mensual</td><td class="n">{money(pm)}</td><td class="n">{money(pm)}</td></tr>
          <tr><td>Qué pasa el mes 1</td><td>Sitio + trabajo mensual</td><td>Solo el sitio</td></tr>
          <tr><td>Meses de marketing<br>en los primeros {meses}</td><td class="n">{meses}</td><td class="n">{meses-1}</td></tr>
          <tr class="tot"><td>Total primeros {meses} meses</td><td class="n">{money(total_a)}</td><td class="n">{money(total_b)}</td></tr>
          </tbody></table>
          <p>Con la Opción A pagas <b>{money(total_b-total_a)} menos</b> y recibes un mes más de
          trabajo mensual. La única diferencia es el compromiso de {meses} meses, que de todas
          formas es el tiempo mínimo para saber si esto funciona.</p>'''
        bloque = card_a + card_b + cmp_tbl
    elif modo == 'programa':
        bloque = card_a
    else:
        bloque = card_b

    P.append(f'''<section class="sec"><div class="kick">07 · LA INVERSIÓN</div>
      <h2>Qué cuesta</h2>
      {bloque}
      {inc}
      <h3>Sin costos escondidos</h3>
      <p>No hay cuota de arranque ni costo por página adicional dentro del plan acordado. Lo
      único aparte es el dominio si todavía no tienes uno (unos $15 al año, pagado por ti y a
      tu nombre). Todos los precios son en dólares estadounidenses.</p>
      <div class="green"><b>Pase lo que pase</b>
      El sitio, el dominio y todos los perfiles son tuyos y se quedan contigo, con o sin
      nosotros. Nunca creamos tu Perfil de Google bajo nuestra cuenta.</div>
    </section>''')

    # ------------------------------------------------------- 8. claridad
    P.append('''<section class="sec"><div class="kick">08 · CLARIDAD</div>
      <h2>Lo que sí y lo que no</h2>
      <h3>Lo que prometemos</h3>
      <ul>
        <li>Que todo lo de esta propuesta se hace, cada mes, y que puedes verlo en el reporte.</li>
        <li>Que el sitio y todos tus perfiles quedan a tu nombre desde el primer día.</li>
        <li>Que te decimos la verdad aunque no nos convenga, incluso si eso significa
          recomendarte que no gastes.</li>
        <li>Que te contestamos el mismo día, en español o en inglés.</li>
      </ul>
      <h3>Lo que no prometemos</h3>
      <ul>
        <li><b>El primer lugar.</b> Nadie controla el algoritmo de Google. Quien te lo
          garantice te está mintiendo.</li>
        <li><b>Un número exacto de llamadas.</b> Podemos estimar con tus cifras, no garantizar.</li>
        <li><b>Resultados rápidos.</b> Los primeros meses son de construcción.</li>
      </ul>
      <h3>Lo que necesitamos de ti</h3>
      <ul>
        <li>Fotos de los trabajos por WhatsApp cuando puedas. Con el celular basta.</li>
        <li>Media hora al mes para revisar el reporte y decirnos qué servicio empujar.</li>
        <li>Que le pidas la reseña al cliente. Nosotros te damos el enlace y el mensaje.</li>
        <li><b>Que contestes rápido.</b> Podemos ponerte primero en el mapa y aun así perder
          el trabajo si tardas tres horas en devolver el mensaje.</li>
      </ul>
      <h3>Somos nuevos y lo decimos nosotros</h3>
      <p>MAPA Marketing acaba de arrancar. No tenemos una pared de casos de estudio y no vamos
      a inventarlos. Lo que tenemos es método: todo lo que hacemos está publicado y explicado
      en nuestro sitio, gratis, para que cualquiera lo revise. Si entras ahora te toca la mejor
      versión de nosotros: pocos clientes y atención directa.</p>
    </section>''')

    # ------------------------------------------------------- 9. siguiente paso
    P.append(f'''<section class="sec"><div class="kick">09 · SIGUIENTE PASO</div>
      <h2>Cómo arrancamos</h2>
      <p class="lede">Si esto te hace sentido, {c['contacto']}, el siguiente paso es un
      mensaje. No hay contrato de veinte páginas ni junta adicional.</p>
      <div class="phase"><div class="num">01</div><div><h4>Nos dices cuál opción</h4>
        <p>Un mensaje por WhatsApp diciendo con cuál le entramos. Te mandamos los términos
        en una página.</p></div></div>
      <div class="phase"><div class="num">02</div><div><h4>Nos das los accesos</h4>
        <p>Perfil de Google, dominio si ya tienes, y el sitio actual si aplica. Te guiamos
        paso a paso.</p></div></div>
      <div class="phase"><div class="num">03</div><div><h4>Arrancamos esa misma semana</h4>
        <p>Empezamos por el mapa de páginas y en tres o cuatro semanas tienes el sitio
        en línea.</p></div></div>
      <div class="cta">
        <h3>¿Le entramos, {c['contacto']}?</h3>
        <p>Escríbenos por WhatsApp. Si tienes dudas de cualquier parte de esta propuesta,
        pregúntalas ahí mismo: preferimos resolverlas antes que después.</p>
        <div class="btn">Escríbenos por WhatsApp</div>
        <div class="num">{WA_NUM}</div>
      </div>
      <p style="margin-top:8mm;font-size:9.4pt;color:#55665F">Esta propuesta es válida por 30
      días a partir del {fecha}.</p>
    </section>''')

    html = ('<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">'
            f'<title>Propuesta · {c["negocio"]}</title><style>{CSS}</style></head>'
            f'<body>{"".join(P)}</body></html>')

    slug = c['negocio'].lower().replace(' ', '-')
    for ch in 'áéíóúñ':
        slug = slug.replace(ch, 'aeioun'['áéíóúñ'.index(ch)])
    out = OUTDIR / ('propuesta-%s.pdf' % slug)
    HTML(string=html, base_url=str(ROOT)).write_pdf(out)
    print('escrito', out.name)
    return out


for lg in IDIOMAS:
    build(CLIENTE, lg)
