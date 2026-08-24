# -*- coding: utf-8 -*-
"""Convierte guia.html en un PDF con portada, índice y numeración.
Uso: python3 _build/make_pdf.py
"""
import pathlib, re, sys
from bs4 import BeautifulSoup
from weasyprint import HTML

ROOT = pathlib.Path('/home/claude/mapa')
FONTS = pathlib.Path('/home/claude/ads/fonts')
WA_NUM = '+1 (726) 255-6888'
WA_URL = 'https://wa.me/17262556888'

T = {
 'es': dict(
    src='guia.html', out='assets/guia-marketing-local-mapa-marketing.pdf',
    kicker='GUÍA GRATIS · 11 CAPÍTULOS', title='Cómo llenar tu semana de trabajo',
    sub='La guía de marketing local para negocios de servicio: cómo hacer que los clientes de tu zona te encuentren primero',
    chapters='11 capítulos', by='MAPA MARKETING',
    toc='Contenido', chapter='Capítulo',
    introh='Antes de empezar',
    intro=[
      'Esta guía es, literalmente, lo que hacemos por nuestros clientes. No es un adelanto ni un resumen: es el método completo, escrito para que puedas seguirlo tú mismo si tienes el tiempo.',
      'Está pensada para dueños de negocios de servicio en Estados Unidos: plomería, techos, aire acondicionado, jardinería, limpieza, remodelación, electricidad, control de plagas y oficios parecidos. Si atiendes clientes en una zona concreta y vives de que suene el teléfono, es para ti.',
      'No hay atajos aquí y no hay trucos. Hay un orden de trabajo. Si haces las cosas en el orden en que están, funcionan; si empiezas por el capítulo nueve, no.',
      'Hacerlo bien son entre diez y quince horas al mes, todos los meses, además de correr tu negocio. Si tienes esas horas, tómalas. Si no, ya sabes dónde estamos.'],
    ctah='¿Prefieres que lo hagamos nosotros?',
    ctap=['Mándanos el nombre de tu negocio y tu ciudad por WhatsApp. Te revisamos gratis tu sitio, tu Perfil de Negocio de Google, Apple Maps, Bing Places y Yelp, y te decimos qué encontramos y qué haríamos primero.',
          'Sin llamadas, sin presentaciones y sin compromiso. Aunque no nos contrates, te quedas con la revisión.'],
    ctab='Escríbenos por WhatsApp', us='Solo negocios de servicio en Estados Unidos · Atendemos en español y en inglés',
    note='Cómo lo hacemos nosotros', short='En corto'),
 'en': dict(
    src='en/guia.html', out='assets/local-marketing-guide-mapa-marketing.pdf',
    kicker='FREE GUIDE · 11 CHAPTERS', title='How to fill your week with work',
    sub='The local marketing guide for service businesses: how to get customers in your area to find you first',
    chapters='11 chapters', by='MAPA MARKETING',
    toc='Contents', chapter='Chapter',
    introh='Before you start',
    intro=[
      'This guide is, literally, what we do for our clients. It is not a preview or a summary: it is the whole method, written so you can follow it yourself if you have the time.',
      'It is written for owners of service businesses in the United States: plumbing, roofing, HVAC, landscaping, cleaning, remodeling, electrical, pest control and similar trades. If you serve a specific area and you live off the phone ringing, this is for you.',
      'There are no shortcuts here and no tricks. There is an order of work. Do things in the order they appear and they work; start at chapter nine and they will not.',
      'Doing it properly is ten to fifteen hours a month, every month, on top of running your business. If you have those hours, take them. If not, you know where we are.'],
    ctah='Would you rather we did it?',
    ctap=['Send us your business name and your city on WhatsApp. We will check your site, your Google Business Profile, Apple Maps, Bing Places and Yelp for free, and tell you what we find and what we would do first.',
          'No calls, no presentations, no obligation. Even if you never hire us, the review is yours.'],
    ctab='Message us on WhatsApp', us='US service businesses only · We work in Spanish and English',
    note='How we handle it', short='In short'),
}

CSS = """
@font-face{font-family:Archivo;src:url('file://__F__/Archivo-700.ttf');font-weight:700}
@font-face{font-family:Archivo;src:url('file://__F__/Archivo-800.ttf');font-weight:800}
@font-face{font-family:Archivo;src:url('file://__F__/Archivo-900.ttf');font-weight:900}
@font-face{font-family:'Public Sans';src:url('file://__F__/PublicSans-400.ttf');font-weight:400}
@font-face{font-family:'Public Sans';src:url('file://__F__/PublicSans-600.ttf');font-weight:600}
@font-face{font-family:'DM Mono';src:url('file://__F__/DMMono-500.ttf');font-weight:500}

@page{
  size:Letter; margin:20mm 19mm 18mm 19mm;
  @bottom-left{content:'MAPA MARKETING';font-family:'DM Mono';font-size:7pt;
    letter-spacing:.16em;color:#8A968E}
  @bottom-right{content:counter(page);font-family:'DM Mono';font-size:8pt;color:#55665F}
}
@page cover{margin:0; @bottom-left{content:''} @bottom-right{content:''}}
@page nofoot{ @bottom-left{content:''} @bottom-right{content:''}}

body{font-family:'Public Sans';font-size:10.2pt;line-height:1.62;color:#12212E;margin:0}
h1,h2,h3{font-family:Archivo;letter-spacing:-.02em;line-height:1.1;color:#0E2233}
p{margin:0 0 .78em}
a{color:#0E7C42;text-decoration:none}
strong,b{font-weight:600}
em{font-style:italic}

/* ---------- portada ---------- */
.cover{page:cover;background:#07161F;color:#EFF1EC;height:279.4mm;width:215.9mm;
  position:relative;overflow:hidden;page-break-after:always}
.cover .g{position:absolute;inset:0;
  background-image:linear-gradient(rgba(239,241,236,.055) 1px,transparent 1px),
    linear-gradient(90deg,rgba(239,241,236,.055) 1px,transparent 1px);
  background-size:24mm 24mm}
.cover .in{position:absolute;left:22mm;right:22mm;top:26mm;bottom:22mm}
.cover .k{font-family:'DM Mono';font-size:8.5pt;letter-spacing:.30em;color:#93A7B2}
.cover .rule{width:26mm;height:0;border-top:2.4pt solid #F0A81C;margin:5mm 0 0}
.cover h1{font-size:40pt;font-weight:800;color:#EFF1EC;margin:52mm 0 0;letter-spacing:-.03em}
.cover .sub{font-size:13pt;color:#93A7B2;font-weight:400;margin-top:7mm;max-width:135mm;
  line-height:1.42}
.cover .meta{position:absolute;bottom:0;left:0;right:0;font-family:'DM Mono';font-size:8.5pt;
  letter-spacing:.20em;color:#93A7B2;border-top:.6pt solid rgba(239,241,236,.22);padding-top:5mm}
.cover .meta span{float:right;color:#F0A81C}
.pin{position:absolute;right:20mm;top:34mm}

/* ---------- interiores ---------- */
.plain{page:nofoot;page-break-after:always}
.intro h2,.cta h2{font-size:21pt;font-weight:800;margin:0 0 7mm}
.intro{padding-top:6mm}
.intro p{font-size:11pt;line-height:1.68;max-width:150mm}
.intro .kick,.cta .kick{font-family:'DM Mono';font-size:7.5pt;letter-spacing:.22em;
  color:#F0A81C;margin-bottom:4mm}

.toc{page-break-after:always;padding-top:6mm}
.toc h2{font-size:21pt;font-weight:800;margin:0 0 8mm}
.toc ol{list-style:none;margin:0;padding:0;counter-reset:t}
.toc li{counter-increment:t;border-bottom:.5pt solid #D8DED2;padding:3.1mm 0;
  font-size:10.6pt;display:flex}
.toc li a{color:#12212E;flex:1}
.toc li a::before{content:counter(t,decimal-leading-zero);font-family:'DM Mono';
  font-size:8pt;color:#F0A81C;margin-right:6mm}
.toc li a::after{content:target-counter(attr(href), page);font-family:'DM Mono';
  font-size:8.5pt;color:#55665F;float:right}

.chapter{page-break-before:always}
.chapter .num{font-family:'DM Mono';font-size:7.5pt;letter-spacing:.22em;color:#F0A81C}
.chapter h2{font-size:23pt;font-weight:800;margin:3mm 0 7mm;padding-bottom:5mm;
  border-bottom:1.6pt solid #0E2233}
.chapter h3{font-size:12.4pt;font-weight:700;margin:8mm 0 2.6mm;page-break-after:avoid}
.chapter ul,.chapter ol{margin:0 0 .9em;padding-left:5.4mm}
.chapter li{margin-bottom:1.6mm;padding-left:1mm}
.chapter li::marker{color:#8A968E}

pre{background:#EFF1EC;border:.5pt solid #D8DED2;border-radius:2pt;padding:4.5mm 5mm;
  font-family:'DM Mono';font-size:7.6pt;line-height:1.62;white-space:pre-wrap;
  page-break-inside:avoid;margin:4mm 0}
.mono{font-family:'DM Mono';font-size:9pt;background:#EFF1EC;padding:.4mm 1.4mm}

table{width:100%;border-collapse:collapse;font-size:9.3pt;margin:4mm 0;
  page-break-inside:avoid}
th,td{text-align:left;padding:2.4mm 2.6mm;border-bottom:.5pt solid #D8DED2;
  vertical-align:top}
th{font-family:'DM Mono';font-size:7.4pt;letter-spacing:.13em;text-transform:uppercase;
  color:#55665F;font-weight:500;border-bottom:1pt solid #0E2233}

.keytake{border:.6pt solid #C3CBBE;background:#EFF1EC;border-radius:2pt;
  padding:4.5mm 5mm;margin:6mm 0;page-break-inside:avoid;font-size:10pt}
.keytake b{display:block;font-family:'DM Mono';font-size:7.2pt;letter-spacing:.18em;
  text-transform:uppercase;color:#55665F;margin-bottom:2mm;font-weight:500}
.prose-note{border-left:2.2pt solid #25D366;background:#EAF7EF;padding:4.5mm 5mm;
  margin:6mm 0;page-break-inside:avoid;font-size:10pt}
.prose-note b{display:block;font-family:'DM Mono';font-size:7.2pt;letter-spacing:.18em;
  text-transform:uppercase;color:#0E7C42;margin-bottom:2mm;font-weight:500}
.prose-note .wa{display:block;margin-top:3mm;font-family:Archivo;font-weight:700;
  font-size:9.6pt;color:#0E7C42}

/* ---------- cierre ---------- */
.cta{page-break-before:always;padding-top:8mm}
.cta .box{background:#0E2233;color:#EFF1EC;border-radius:3pt;padding:12mm 11mm;margin-top:6mm}
.cta .box h2{color:#EFF1EC;font-size:22pt;margin:0 0 6mm}
.cta .box p{color:#93A7B2;font-size:10.6pt;max-width:135mm}
.cta .btn{display:inline-block;background:#25D366;color:#04231A;font-family:Archivo;
  font-weight:800;font-size:12pt;padding:4.6mm 9mm;border-radius:30pt;margin-top:5mm}
.cta .num{font-family:'DM Mono';font-size:11pt;color:#F0A81C;margin-top:6mm;
  letter-spacing:.10em}
.cta .fine{font-family:'DM Mono';font-size:7.6pt;letter-spacing:.14em;color:#93A7B2;
  margin-top:7mm;border-top:.5pt solid rgba(239,241,236,.2);padding-top:5mm}
""".replace("__F__", str(FONTS))

PIN = ('<svg class="pin" width="96" height="96" viewBox="0 0 40 40">'
       '<circle cx="20" cy="20" r="19" fill="none" stroke="#1F4A55" stroke-width="1" '
       'stroke-dasharray="2 3"/>'
       '<path d="M20 8.5c-4.7 0-8.5 3.7-8.5 8.3 0 6.2 8.5 14.7 8.5 14.7s8.5-8.5 8.5-14.7'
       'c0-4.6-3.8-8.3-8.5-8.3z" fill="#25D366"/>'
       '<circle cx="20" cy="16.8" r="3.2" fill="#07161F"/></svg>')


def clean(node, t):
    """Adapta el HTML del sitio al formato impreso."""
    for el in node.select('.prose-note a.wa, .prose-note a'):
        el.name = 'span'
        el['class'] = ['wa']
        el.string = '%s  ·  %s' % (t['ctab'], WA_NUM)
        for a in list(el.attrs):
            if a != 'class':
                del el[a]
    for a in node.find_all('a'):
        a.unwrap()
    for el in node.find_all(style=True):
        del el['style']
    for el in node.find_all(True):
        if el.name in ('span',) and not el.get('class'):
            el.unwrap()
    return node


def build(lang):
    t = T[lang]
    soup = BeautifulSoup((ROOT / t['src']).read_text(encoding='utf-8'), 'html.parser')
    chapters = soup.select('.chapter')
    if not chapters:
        sys.exit('no se encontraron capítulos en ' + t['src'])

    parts = []
    parts.append(
      '<div class="cover"><div class="g"></div>%s<div class="in">'
      '<div class="k">%s</div><div class="rule"></div>'
      '<h1>%s</h1><div class="sub">%s</div>'
      '<div class="meta">%s<span>%s</span></div></div></div>'
      % (PIN, t['kicker'], t['title'], t['sub'], t['by'], t['chapters'].upper()))

    parts.append('<section class="plain intro"><div class="kick">%s</div><h2>%s</h2>%s</section>'
                 % (t['kicker'], t['introh'], ''.join('<p>%s</p>' % p for p in t['intro'])))

    toc = ''.join('<li><a href="#c%d">%s</a></li>'
                  % (i, c.find('h2').get_text(' ', strip=True))
                  for i, c in enumerate(chapters, 1))
    parts.append('<section class="toc"><h2>%s</h2><ol>%s</ol></section>' % (t['toc'], toc))

    for i, c in enumerate(chapters, 1):
        title = c.find('h2').get_text(' ', strip=True)
        body = c.find('div') or BeautifulSoup('', 'html.parser')
        clean(body, t)
        inner = body.decode_contents() if hasattr(body, 'decode_contents') else ''
        parts.append('<section class="chapter" id="c%d"><div class="num">%s %02d</div>'
                     '<h2>%s</h2>%s</section>' % (i, t['chapter'].upper(), i, title, inner))

    parts.append(
      '<section class="cta"><div class="kick">%s</div><div class="box"><h2>%s</h2>%s'
      '<div class="btn">%s</div><div class="num">%s</div>'
      '<div class="fine">%s</div></div></section>'
      % (t['kicker'], t['ctah'], ''.join('<p>%s</p>' % p for p in t['ctap']),
         t['ctab'], WA_NUM, t['us'].upper()))

    html = ('<!DOCTYPE html><html lang="%s"><head><meta charset="utf-8">'
            '<title>%s</title><style>%s</style></head><body>%s</body></html>'
            % (lang, t['title'], CSS, ''.join(parts)))

    out = ROOT / t['out']
    HTML(string=html, base_url=str(ROOT)).write_pdf(out)
    print('escrito', out.name)
    return out


for lg in ('es', 'en'):
    build(lg)
