# -*- coding: utf-8 -*-
"""Convierte las páginas bilingües de _src/ en dos sitios de un solo idioma:

    /            -> español  (canónico)
    /en/         -> inglés

Cada salida queda con un solo H1, un solo idioma, hreflang recíproco,
canonical y JSON-LD. Ejecutar después de pages.py / toolpages.py / guide.py.
"""
import json, pathlib, re, shutil
from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / '_src'
EN = ROOT / 'en'

# Cambia esto cuando conectes tu dominio propio.
SITE = 'https://mapamarketing.com'
WA = 'https://wa.me/17262556888'
BRAND = 'MAPA Marketing'

# --------------------------------------------------------------------------
# Metadatos por página y por idioma
# --------------------------------------------------------------------------
META = {
    'index.html': {
        'es': ('SEO local y diseño web para negocios de servicio latinos en EE. UU. | MAPA Marketing',
               'Hacemos sitios web y SEO local para negocios de servicio latinos en Estados Unidos. Google, Apple Maps, Bing Places y Yelp trabajando a tu favor. Escríbenos por WhatsApp.'),
        'en': ('Local SEO and Web Design for Latino-Owned Service Businesses | MAPA Marketing',
               'We build websites and run local SEO for Latino-owned service businesses across the US. Google, Apple Maps, Bing Places and Yelp working for you. Message us on WhatsApp.'),
        'nav': 'Inicio', 'nav_en': 'Home'},
    'servicios.html': {
        'es': ('Servicios: sitio web y marketing local mensual | MAPA Marketing',
               'Qué incluye el programa: sitio web optimizado incluido más trabajo mensual en Google, Apple Maps, Bing Places, Yelp, contenido, citaciones y enlaces locales.'),
        'en': ('Services: Website and Monthly Local Marketing | MAPA Marketing',
               'What the program includes: an optimized website plus monthly work on Google, Apple Maps, Bing Places, Yelp, content, citations and local links.'),
        'nav': 'Servicios', 'nav_en': 'Services'},
    'proceso.html': {
        'es': ('Nuestro proceso de SEO local, semana por semana | MAPA Marketing',
               'Del primer mensaje al mes doce: diagnóstico, plan de páginas, construcción del sitio, distribución en cuatro mapas y el ritmo mensual de contenido, fotos y enlaces.'),
        'en': ('Our Local SEO Process, Week by Week | MAPA Marketing',
               'From first message to month twelve: diagnosis, page plan, site build, distribution across four maps, and the monthly rhythm of content, photos and links.'),
        'nav': 'Proceso', 'nav_en': 'Process'},
    'guia.html': {
        'es': ('Guía de marketing local para negocios de servicio | MAPA Marketing',
               'Guía gratuita en español: estructura del sitio, SEO local, Perfil de Negocio de Google, Apple Maps, Bing Places, Yelp, citaciones NAP, contenido, enlaces y búsqueda con IA.'),
        'en': ('Local Marketing Guide for Service Businesses | MAPA Marketing',
               'Free guide: site structure, local SEO, Google Business Profile, Apple Maps, Bing Places, Yelp, NAP citations, content, local links and AI search.'),
        'nav': 'Guía', 'nav_en': 'Guide'},
    'herramientas.html': {
        'es': ('Herramientas gratis de SEO local para negocios de servicio | MAPA Marketing',
               'Cinco herramientas gratuitas: diagnóstico de visibilidad local, calculadora de valor por cliente, generador de publicaciones de Google, respuestas a reseñas y control de citaciones NAP.'),
        'en': ('Free Local SEO Tools for Service Businesses | MAPA Marketing',
               'Five free tools: local visibility check, customer value calculator, Google post generator, review reply writer and NAP citation tracker.'),
        'nav': 'Herramientas', 'nav_en': 'Tools'},
    'diagnostico.html': {
        'es': ('Diagnóstico de visibilidad local gratis | MAPA Marketing',
               'Responde 18 preguntas y descubre qué tan visible es tu negocio de servicio en Google, Apple Maps, Bing y Yelp. Calificación sobre 100 y lista priorizada de arreglos.'),
        'en': ('Free Local Visibility Check | MAPA Marketing',
               'Answer 18 questions and find out how visible your service business is on Google, Apple Maps, Bing and Yelp. Score out of 100 and a prioritized fix list.'),
        'nav': 'Diagnóstico', 'nav_en': 'Visibility check', 'tool': True},
    'calculadora.html': {
        'es': ('Calculadora: cuánto vale un cliente nuevo | MAPA Marketing',
               'Calcula gratis cuánto vale cada contacto para tu negocio de servicio y cuánto representarían tres, seis o doce contactos más al mes.'),
        'en': ('Calculator: What a New Customer Is Worth | MAPA Marketing',
               'Work out for free what each lead is worth to your service business, and what three, six or twelve extra leads a month would mean.'),
        'nav': 'Calculadora', 'nav_en': 'Calculator', 'tool': True},
    'publicaciones.html': {
        'es': ('Generador de publicaciones para el Perfil de Negocio de Google | MAPA Marketing',
               'Genera gratis las publicaciones mensuales de tu Perfil de Negocio de Google, en español o inglés, adaptadas a tu oficio y tu ciudad.'),
        'en': ('Google Business Profile Post Generator | MAPA Marketing',
               'Generate your monthly Google Business Profile posts for free, in Spanish or English, tailored to your trade and your city.'),
        'nav': 'Publicaciones', 'nav_en': 'Post generator', 'tool': True},
    'resenas.html': {
        'es': ('Generador de respuestas a reseñas de Google y Yelp | MAPA Marketing',
               'Escribe gratis la respuesta a una reseña de 1 a 5 estrellas, en español o inglés, para tu Perfil de Negocio de Google o tu perfil de Yelp.'),
        'en': ('Google and Yelp Review Reply Generator | MAPA Marketing',
               'Write a free reply to any 1 to 5 star review, in Spanish or English, for your Google Business Profile or your Yelp listing.'),
        'nav': 'Reseñas', 'nav_en': 'Review replies', 'tool': True},
    'citaciones.html': {
        'es': ('Citaciones locales y datos NAP: lista de 30 directorios | MAPA Marketing',
               'Arma tu bloque NAP consistente y lleva el control de los 30 directorios donde tu negocio de servicio debería estar listado en Estados Unidos.'),
        'en': ('Local Citations and NAP Data: 30-Directory Checklist | MAPA Marketing',
               'Build a consistent NAP block and track the 30 directories where your service business should be listed in the United States.'),
        'nav': 'Citaciones', 'nav_en': 'Citations', 'tool': True},
    '404.html': {
        'es': ('Página no encontrada | MAPA Marketing', 'Esta página no existe. Vuelve al inicio o escríbenos por WhatsApp.'),
        'en': ('Page not found | MAPA Marketing', 'This page does not exist. Go back home or message us on WhatsApp.'),
        'nav': '404', 'nav_en': '404', 'noindex': True},
}

L = {'es': {'home': 'Inicio', 'lang_name': 'Español', 'locale': 'es_US'},
     'en': {'home': 'Home', 'lang_name': 'English', 'locale': 'en_US'}}


def url_for(fn, lang):
    base = SITE + ('/' if lang == 'es' else '/en/')
    return base if fn == 'index.html' else base + fn


# --------------------------------------------------------------------------
# Filtrado de idioma
# --------------------------------------------------------------------------
UNWRAP = {'span', 'div', 'p', 'b', 'strong', 'em'}

def filter_lang(soup, lang):
    other = 'en' if lang == 'es' else 'es'
    for el in soup.select('[data-l="%s"]' % other):
        el.decompose()
    for el in soup.select('[data-l="%s"]' % lang):
        # Sólo se quita el atributo. No se desenvuelve el elemento: varios
        # <span> son celdas de grid (.deliv li) y perderían su posición.
        del el['data-l']
    # Atributos traducidos
    for attr, target in (('ph', 'placeholder'), ('al', 'aria-label')):
        for el in soup.select('[data-%s-%s]' % (attr, lang)):
            el[target] = el['data-%s-%s' % (attr, lang)]
        for el in soup.select('[data-%s-es], [data-%s-en]' % (attr, attr)):
            el.attrs.pop('data-%s-es' % attr, None)
            el.attrs.pop('data-%s-en' % attr, None)
    # Mensajes de WhatsApp: se queda uno solo, como data-msg
    for el in soup.select('[data-msg-es], [data-msg-en]'):
        msg = el.get('data-msg-%s' % lang) or el.get('data-msg-es') or ''
        el.attrs.pop('data-msg-es', None)
        el.attrs.pop('data-msg-en', None)
        if msg:
            el['data-msg'] = msg


def fix_paths(soup, lang):
    """En /en/ los recursos viven un nivel arriba."""
    if lang != 'en':
        return
    for el in soup.find_all(href=True):
        if el['href'].startswith('assets/'):
            el['href'] = '../' + el['href']
    for el in soup.find_all(src=True):
        if el['src'].startswith('assets/'):
            el['src'] = '../' + el['src']


def swap_toggle(soup, fn, lang):
    tog = soup.select_one('.langtog')
    if not tog:
        return
    tog.clear()
    for code, label in (('es', 'ES'), ('en', 'EN')):
        if code == 'es':
            href = ('index.html' if fn == 'index.html' else fn) if lang == 'es' else ('../' + ('' if fn == 'index.html' else fn) or '../index.html')
            if lang == 'en':
                href = '../index.html' if fn == 'index.html' else '../' + fn
        else:
            href = ('en/' + fn) if lang == 'es' else fn
        a = soup.new_tag('a', href=href, hreflang=code)
        a['title'] = L[code]['lang_name']
        if code == lang:
            a['aria-current'] = 'true'
        a.string = label
        tog.append(a)


# --------------------------------------------------------------------------
# JSON-LD
# --------------------------------------------------------------------------
def business_node(lang):
    return {
        '@type': ['ProfessionalService', 'Organization'],
        '@id': SITE + '/#business',
        'name': BRAND,
        'url': SITE + '/',
        'logo': {'@type': 'ImageObject', '@id': SITE + '/#logo',
                 'url': SITE + '/assets/img/favicon.svg', 'contentUrl': SITE + '/assets/img/favicon.svg'},
        'image': {'@id': SITE + '/#logo'},
        'description': (
            'Agencia de marketing digital especializada en negocios de servicio latinos en Estados Unidos: '
            'diseño web, SEO local y optimización de perfiles en Google, Apple Maps, Bing Places y Yelp.'
            if lang == 'es' else
            'Digital marketing agency for Latino-owned service businesses in the United States: web design, '
            'local SEO and profile optimization across Google, Apple Maps, Bing Places and Yelp.'),
        'areaServed': {'@type': 'Country', 'name': 'United States'},
        'knowsLanguage': ['es', 'en'],
        'availableLanguage': [{'@type': 'Language', 'name': 'Spanish', 'alternateName': 'es'},
                              {'@type': 'Language', 'name': 'English', 'alternateName': 'en'}],
        'contactPoint': [{
            '@type': 'ContactPoint',
            'contactType': 'customer service' if lang == 'en' else 'atención al cliente',
            'url': WA,
            'availableLanguage': ['Spanish', 'English'],
            'areaServed': 'US'}],
        'knowsAbout': ['Local SEO', 'Google Business Profile', 'Apple Business Connect',
                       'Bing Places', 'Yelp', 'NAP citations', 'Web design', 'Local link building'],
    }


def service_nodes(lang):
    es = lang == 'es'
    return [{
        '@type': 'Service',
        '@id': SITE + '/#service-web',
        'name': 'Diseño de sitio web optimizado' if es else 'Optimized website design',
        'serviceType': 'Web design' if not es else 'Diseño web',
        'provider': {'@id': SITE + '/#business'},
        'areaServed': {'@type': 'Country', 'name': 'United States'},
        'audience': {'@type': 'BusinessAudience',
                     'name': 'Latino-owned local service businesses'},
        'description': (
            'Sitio web con una página por cada servicio en cada ciudad, velocidad en celular, '
            'datos estructurados y llamadas a la acción hacia WhatsApp. Incluido al contratar el trabajo mensual.'
            if es else
            'A website with one page for each service in each city, mobile speed, structured data and '
            'WhatsApp calls to action. Included when you take on the monthly work.'),
    }, {
        '@type': 'Service',
        '@id': SITE + '/#service-monthly',
        'name': 'Marketing local mensual' if es else 'Monthly local marketing',
        'serviceType': 'Local SEO' if not es else 'SEO local',
        'provider': {'@id': SITE + '/#business'},
        'areaServed': {'@type': 'Country', 'name': 'United States'},
        'audience': {'@type': 'BusinessAudience',
                     'name': 'Latino-owned local service businesses'},
        'description': (
            'Mapas de calor y ajustes al sitio, contenido nuevo, publicaciones y optimización del Perfil de '
            'Negocio de Google, Apple Maps, Bing Places y Yelp, fotos mensuales, citaciones y enlaces locales.'
            if es else
            'Heatmaps and site tweaks, new content, posts and optimization across Google Business Profile, '
            'Apple Maps, Bing Places and Yelp, monthly photos, citations and local links.'),
    }]


def build_graph(soup, fn, lang, title, desc):
    page_url = url_for(fn, lang)
    graph = [business_node(lang),
             {'@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/',
              'name': BRAND, 'publisher': {'@id': SITE + '/#business'},
              'inLanguage': lang}]

    crumbs = [{'@type': 'ListItem', 'position': 1, 'name': L[lang]['home'],
               'item': url_for('index.html', lang)}]
    if fn != 'index.html':
        crumbs.append({'@type': 'ListItem', 'position': 2,
                       'name': META[fn]['nav' if lang == 'es' else 'nav_en'],
                       'item': page_url})
    graph.append({'@type': 'BreadcrumbList', '@id': page_url + '#breadcrumb',
                  'itemListElement': crumbs})

    page_types = ['WebPage']
    page = {'@type': page_types, '@id': page_url + '#webpage', 'url': page_url,
            'name': title, 'description': desc,
            'isPartOf': {'@id': SITE + '/#website'},
            'about': {'@id': SITE + '/#business'},
            'breadcrumb': {'@id': page_url + '#breadcrumb'},
            'inLanguage': lang}

    # --- FAQ (portada)
    faqs = []
    for d in soup.select('.faq details'):
        q = d.find('summary')
        a = d.select_one('.faq__a')
        if q and a:
            faqs.append({'@type': 'Question', 'name': q.get_text(' ', strip=True),
                         'acceptedAnswer': {'@type': 'Answer', 'text': a.get_text(' ', strip=True)}})
    if faqs:
        page_types.append('FAQPage')
        page['mainEntity'] = faqs

    # --- Guía: artículo
    if fn == 'guia.html':
        sections = [h.get_text(' ', strip=True) for h in soup.select('.chapter > h2')]
        graph.append({
            '@type': 'Article', '@id': page_url + '#article',
            'headline': title.split(' | ')[0], 'description': desc,
            'inLanguage': lang, 'articleSection': sections,
            'author': {'@id': SITE + '/#business'},
            'publisher': {'@id': SITE + '/#business'},
            'mainEntityOfPage': {'@id': page_url + '#webpage'},
            'isAccessibleForFree': True})
        page['significantLink'] = [page_url + '#' + c['id'] for c in soup.select('.chapter[id]')][:11]

    # --- Herramientas: lista
    if fn == 'herramientas.html':
        items = []
        for i, card in enumerate(soup.select('.toolcard'), 1):
            h = card.find(['h2', 'h3'])
            if h:
                items.append({'@type': 'ListItem', 'position': i,
                              'name': h.get_text(' ', strip=True),
                              'url': url_for(card['href'], lang)})
        if items:
            graph.append({'@type': 'ItemList', '@id': page_url + '#tools',
                          'name': title.split(' | ')[0], 'itemListElement': items})

    # --- Cada herramienta: WebApplication
    if META[fn].get('tool'):
        h1 = soup.find('h1')
        graph.append({
            '@type': 'WebApplication', '@id': page_url + '#app',
            'name': h1.get_text(' ', strip=True) if h1 else title.split(' | ')[0],
            'description': desc, 'url': page_url,
            'applicationCategory': 'BusinessApplication',
            'operatingSystem': 'Any (web browser)',
            'browserRequirements': 'Requires JavaScript',
            'inLanguage': lang,
            'isAccessibleForFree': True,
            'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'},
            'publisher': {'@id': SITE + '/#business'}})

    # --- Servicios
    if fn == 'servicios.html':
        graph.extend(service_nodes(lang))
        page['mainEntity'] = [{'@id': SITE + '/#service-web'}, {'@id': SITE + '/#service-monthly'}]

    if fn == 'index.html':
        graph.extend(service_nodes(lang))
        for n in graph:
            if n.get('@id') == SITE + '/#business':
                n['hasOfferCatalog'] = {
                    '@type': 'OfferCatalog',
                    'name': 'Marketing local' if lang == 'es' else 'Local marketing',
                    'itemListElement': [
                        {'@type': 'Offer', 'itemOffered': {'@id': SITE + '/#service-web'}},
                        {'@type': 'Offer', 'itemOffered': {'@id': SITE + '/#service-monthly'}}]}

    graph.append(page)
    return {'@context': 'https://schema.org', '@graph': graph}


# --------------------------------------------------------------------------
# Cabecera
# --------------------------------------------------------------------------
def rewrite_head(soup, fn, lang, title, desc):
    head = soup.head
    for sel in ['title', 'meta[name="description"]', 'meta[property^="og:"]',
                'link[rel="canonical"]', 'link[rel="alternate"]',
                'script[type="application/ld+json"]']:
        for el in head.select(sel):
            el.decompose()

    t = soup.new_tag('title'); t.string = title; head.append(t)

    def meta(**kw):
        m = soup.new_tag('meta')
        for k, v in kw.items():
            m[k.replace('_', ':')] = v
        head.append(m)

    meta(name='description', content=desc)
    if META[fn].get('noindex'):
        meta(name='robots', content='noindex, follow')

    canon = url_for(fn, lang)
    for rel, href, hl in [('canonical', canon, None),
                          ('alternate', url_for(fn, 'es'), 'es'),
                          ('alternate', url_for(fn, 'en'), 'en'),
                          ('alternate', url_for(fn, 'es'), 'x-default')]:
        if META[fn].get('noindex') and rel == 'alternate':
            continue
        link = soup.new_tag('link', rel=rel, href=href)
        if hl:
            link['hreflang'] = hl
        head.append(link)

    meta(og_type='article' if fn == 'guia.html' else 'website')
    meta(og_title=title)
    meta(og_description=desc)
    meta(og_url=canon)
    meta(og_site_name=BRAND)
    meta(og_locale=L[lang]['locale'])
    meta(og_locale_alternate=L['en' if lang == 'es' else 'es']['locale'])
    meta(name='twitter:card', content='summary_large_image')

    if not META[fn].get('noindex'):
        s = soup.new_tag('script', type='application/ld+json')
        s.string = json.dumps(build_graph(soup, fn, lang, title, desc),
                              ensure_ascii=False, indent=None)
        head.append(s)


# --------------------------------------------------------------------------
# Proceso principal
# --------------------------------------------------------------------------
def build(fn, lang):
    soup = BeautifulSoup((SRC / fn).read_text(encoding='utf-8'), 'html.parser')
    filter_lang(soup, lang)
    swap_toggle(soup, fn, lang)
    fix_paths(soup, lang)

    html = soup.find('html')
    html['lang'] = lang
    html['data-lang'] = lang

    # El pie usaba <h4> para menús: no son encabezados de contenido.
    for h in soup.select('.foot h4'):
        h.name = 'p'
        h['class'] = h.get('class', []) + ['foot__h']

    rewrite_head(soup, fn, lang, *META[fn][lang])

    out = (ROOT if lang == 'es' else EN) / fn
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(str(soup), encoding='utf-8')
    return out


if EN.exists():
    shutil.rmtree(EN)
EN.mkdir()

for fn in META:
    for lang in ('es', 'en'):
        build(fn, lang)

# --------------------------------------------------------------------------
# sitemap + robots
# --------------------------------------------------------------------------
rows = []
for fn in META:
    if META[fn].get('noindex'):
        continue
    for lang in ('es', 'en'):
        alts = '\n'.join(
            '    <xhtml:link rel="alternate" hreflang="%s" href="%s"/>' % (hl, url_for(fn, l2))
            for hl, l2 in (('es', 'es'), ('en', 'en'), ('x-default', 'es')))
        rows.append('  <url>\n    <loc>%s</loc>\n%s\n  </url>' % (url_for(fn, lang), alts))

(ROOT / 'sitemap.xml').write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<!-- Generado por _build/split.py. Cambia SITE en ese archivo al conectar tu dominio. -->\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
    '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    + '\n'.join(rows) + '\n</urlset>\n', encoding='utf-8')

(ROOT / 'robots.txt').write_text(
    'User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % SITE, encoding='utf-8')

print('generadas %d páginas (%d ES + %d EN)' % (len(META) * 2, len(META), len(META)))
