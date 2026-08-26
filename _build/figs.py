# -*- coding: utf-8 -*-
"""Gráficos SVG reutilizables para los PDF (guía, auditoría, propuesta).

Todos devuelven SVG en línea con las clases .fig / .lbl / .cap etc., que se
estilan desde FIG_CSS. WeasyPrint los dibuja como vectores, así que se ven
nítidos impresos y pesan poco.
"""

INK, SUN, WA, CLAY, RULE, MUTED = '#0E2233', '#F0A81C', '#25D366', '#DD4B34', '#D8DED2', '#55665F'
PAPER, DIM = '#EFF1EC', '#B9C2BA'

FIG_CSS = """
.fig{width:100%;height:auto;margin:5mm 0 6mm;display:block}
.fig .lbl{font-family:'DM Mono';font-size:11px;letter-spacing:1.6px;fill:#55665F}
.fig .cap{font-family:'Public Sans';font-size:12px;fill:#55665F}
.fig .capw{font-family:'Public Sans';font-size:12px;fill:#EFF1EC}
.fig .row{font-family:'Public Sans';font-size:15px;font-weight:600;fill:#0E2233}
.fig .stp{font-family:Archivo;font-size:14px;font-weight:700;fill:#0E2233}
.fig .pin{font-family:Archivo;font-size:13px;font-weight:800;fill:#fff;text-anchor:middle}
.fig .val{font-family:Archivo;font-size:15px;font-weight:800;fill:#0E2233}
.fig .big{font-family:Archivo;font-size:21px;font-weight:900;fill:#0E2233}
.fig .huge{font-family:Archivo;font-size:72px;font-weight:900;fill:#0E2233}
.fig .tiny{font-family:'DM Mono';font-size:10px;letter-spacing:1.2px;fill:#55665F}
.sev{width:16mm;height:auto;flex:none;margin-top:1.5mm}
"""


def severidad(n):
    """Tres puntos: qué tan grave es un hallazgo."""
    out = ''.join(f'<circle cx="{9+i*22}" cy="9" r="7" fill="{CLAY if i < n else RULE}"/>'
                  for i in range(3))
    return f'<svg viewBox="0 0 62 18" class="sev">{out}</svg>'


def marcador(score):
    """Arco de calificación sobre 100."""
    import math
    r, cx, cy = 120, 150, 150
    a = math.pi * (1 - score / 100)
    ex, ey = cx + r * math.cos(a) * -1, cy - r * math.sin(a)
    large = 1 if score > 50 else 0
    col = WA if score >= 70 else (SUN if score >= 40 else CLAY)
    verd = 'Bien' if score >= 70 else ('A medias' if score >= 40 else 'Hay trabajo')
    return f'''<svg viewBox="0 0 300 190" class="fig" style="max-width:88mm;margin:0 auto">
      <path d="M30,150 A120,120 0 0,1 270,150" fill="none" stroke="{RULE}"
            stroke-width="22" stroke-linecap="round"/>
      <path d="M30,150 A120,120 0 {large},1 {ex:.1f},{ey:.1f}" fill="none" stroke="{col}"
            stroke-width="22" stroke-linecap="round"/>
      <text x="150" y="150" class="huge" text-anchor="middle" style="font-size:78px;font-family:Archivo;font-weight:900;fill:#0E2233">{score}</text>
      <text x="150" y="180" class="cap" text-anchor="middle" style="font-size:15px">de 100 · {verd}</text>
    </svg>'''


def barras_cat(cats):
    """Desglose por área: [(etiqueta, 0-100)]."""
    rows, y = '', 0
    for lbl, pct in cats:
        col = WA if pct >= 70 else (SUN if pct >= 40 else CLAY)
        rows += (f'<text x="0" y="{y+13}" class="row">{lbl}</text>'
                 f'<rect x="230" y="{y+2}" width="300" height="16" rx="8" fill="{PAPER}"/>'
                 f'<rect x="230" y="{y+2}" width="{3*pct}" height="16" rx="8" fill="{col}"/>'
                 f'<text x="600" y="{y+15}" class="val" text-anchor="end">{pct}</text>')
        y += 34
    return f'<svg viewBox="0 0 600 {y}" class="fig">{rows}</svg>'


def paquete(competidores, negocio, pos_txt):
    """El paquete de tres del mapa, con el cliente fuera."""
    rows = ''
    for i, (n, r, _) in enumerate(competidores[:3]):
        y = i * 52
        rows += (f'<rect x="0" y="{y}" width="600" height="42" rx="6" fill="{PAPER}"/>'
                 f'<circle cx="26" cy="{y+21}" r="13" fill="#9AA69E"/>'
                 f'<text x="26" y="{y+26}" class="pin">{i+1}</text>'
                 f'<text x="56" y="{y+26}" class="row">{n}</text>'
                 f'<text x="590" y="{y+26}" class="row" text-anchor="end" fill="{MUTED}">{r}</text>')
    y = 3 * 52 + 14
    rows += (f'<rect x="0" y="{y}" width="600" height="42" rx="6" fill="none" '
             f'stroke="{CLAY}" stroke-width="2.5"/>'
             f'<circle cx="26" cy="{y+21}" r="13" fill="{CLAY}"/>'
             f'<text x="26" y="{y+26}" class="pin">?</text>'
             f'<text x="56" y="{y+26}" class="row" fill="{CLAY}">{negocio}</text>'
             f'<text x="590" y="{y+26}" class="row" text-anchor="end" fill="{CLAY}">{pos_txt}</text>')
    return f'<svg viewBox="0 0 600 {y+52}" class="fig">{rows}</svg>'


def fichas(items, lang='es'):
    """Cuatro plataformas con tres estados: True (bien), 'medio' (a medias), False (mal)."""
    out, w, gap = '', 138, 16
    for i, (name, ok, nota) in enumerate(items[:4]):
        x = i * (w + gap)
        medio = (ok == 'medio')
        col = SUN if medio else (WA if ok else CLAY)
        out += (f'<rect x="{x}" y="0" width="{w}" height="96" rx="8" fill="{PAPER}" '
                f'stroke="{col}" stroke-width="2"/>'
                f'<circle cx="{x+w/2}" cy="30" r="15" fill="{col}"/>')
        if medio:
            # signo de admiración: existe pero está incompleto
            out += (f'<path d="M{x+w/2},23 l0,9" stroke="#fff" stroke-width="3" '
                    f'stroke-linecap="round"/>'
                    f'<circle cx="{x+w/2}" cy="37" r="1.8" fill="#fff"/>')
        elif ok:
            out += (f'<path d="M{x+w/2-7},30 l5,6 l9,-11" fill="none" stroke="#fff" '
                    f'stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
        else:
            out += (f'<path d="M{x+w/2-6},24 l12,12 M{x+w/2+6},24 l-12,12" stroke="#fff" '
                    f'stroke-width="3" stroke-linecap="round"/>')
        out += (f'<text x="{x+w/2}" y="64" class="stp" text-anchor="middle">{name}</text>'
                f'<text x="{x+w/2}" y="82" class="cap" text-anchor="middle" fill="{col}">'
                f'{nota}</text>')
    return f'<svg viewBox="0 0 600 100" class="fig">{out}</svg>'


def prioridades(items):
    """Lista numerada con barra de impacto: [(texto, impacto 1-3)]."""
    out, y = '', 0
    for i, (txt, imp) in enumerate(items):
        col = CLAY if imp == 3 else (SUN if imp == 2 else '#9AA69E')
        out += (f'<circle cx="15" cy="{y+15}" r="14" fill="{INK}"/>'
                f'<text x="15" y="{y+20}" class="pin">{i+1}</text>'
                f'<text x="42" y="{y+20}" class="row">{txt}</text>'
                f'<text x="600" y="{y+20}" class="tiny" text-anchor="end">'
                f'{["BAJO","MEDIO","ALTO"][imp-1]}</text>'
                f'<rect x="42" y="{y+32}" width="300" height="5" rx="2.5" fill="{PAPER}"/>'
                f'<rect x="42" y="{y+32}" width="{100*imp}" height="5" rx="2.5" fill="{col}"/>')
        y += 52
    return f'<svg viewBox="0 0 600 {y}" class="fig">{out}</svg>'


def rejilla_paginas(servicios, ciudades, lang='es'):
    """Matriz servicio × ciudad: cada celda es una página."""
    cw, chh, x0, y0 = 92, 30, 150, 34
    out = ''
    for j, ciu in enumerate(ciudades[:4]):
        out += (f'<text x="{x0+j*cw+cw/2}" y="{y0-10}" class="tiny" '
                f'text-anchor="middle">{ciu[:12].upper()}</text>')
    for i, srv in enumerate(servicios[:5]):
        y = y0 + i * chh
        out += f'<text x="0" y="{y+19}" class="cap">{srv[:22]}</text>'
        for j in range(len(ciudades[:4])):
            x = x0 + j * cw
            out += (f'<rect x="{x+3}" y="{y+3}" width="{cw-6}" height="{chh-6}" rx="4" '
                    f'fill="{WA}" opacity="0.16" stroke="{WA}" stroke-width="1.5"/>'
                    f'<circle cx="{x+cw/2}" cy="{y+chh/2}" r="3.5" fill="{WA}"/>')
    tot = len(servicios[:5]) * len(ciudades[:4])
    y = y0 + len(servicios[:5]) * chh + 26
    out += (f'<text x="0" y="{y}" class="val">{tot} ' + ('páginas' if lang == 'es' else 'pages') + '</text>'
            f'<text x="104" y="{y}" class="cap">= {len(servicios[:5])} '
            + ('servicios × ' if lang == 'es' else 'services × ') + f'{len(ciudades[:4])} '
            + ('ciudades' if lang == 'es' else 'cities') + '</text>')
    return f'<svg viewBox="0 0 600 {y+12}" class="fig">{out}</svg>'


def tres_factores(lang='es'):
    """Relevancia, distancia y prominencia."""
    items = [('RELEVANCIA', 'Qué tanto coincides\ncon lo que buscó', WA, 'Lo controlas'),
             ('DISTANCIA', 'Qué tan cerca estás\nde quien busca', DIM, 'No lo controlas'),
             ('PROMINENCIA', 'Qué tan conocido\neres fuera de tu sitio', WA, 'Lo controlas')] \
            if lang == 'es' else \
            [('RELEVANCE', 'How well you match\nwhat they typed', WA, 'You control it'),
             ('DISTANCE', 'How close you are\nto the searcher', DIM, 'You do not'),
             ('PROMINENCE', 'How known you are\noutside your site', WA, 'You control it')]
    out, w, gap = '', 188, 18
    for i, (t, sub, col, foot) in enumerate(items):
        x = i * (w + gap)
        out += (f'<rect x="{x}" y="0" width="{w}" height="126" rx="8" fill="{PAPER}" '
                f'stroke="{col}" stroke-width="2"/>'
                f'<rect x="{x}" y="0" width="{w}" height="6" rx="3" fill="{col}"/>'
                f'<text x="{x+16}" y="34" class="stp">{t}</text>')
        for k, ln in enumerate(sub.split('\n')):
            out += f'<text x="{x+16}" y="{58+k*17}" class="cap">{ln}</text>'
        out += f'<text x="{x+16}" y="108" class="tiny" fill="{col if col != DIM else MUTED}">{foot.upper()}</text>'
    return f'<svg viewBox="0 0 600 132" class="fig">{out}</svg>'


def nap_compare(lang='es'):
    """NAP consistente contra NAP roto."""
    ok = ['1420 Bellaire Boulevard', 'Suite 210', '(713) 555-0142']
    bad = ['1420 Bellaire Blvd.', '#210', '713-555-0142']
    out = (f'<rect x="0" y="0" width="288" height="118" rx="8" fill="{PAPER}" '
           f'stroke="{WA}" stroke-width="2"/>'
           f'<rect x="312" y="0" width="288" height="118" rx="8" fill="{PAPER}" '
           f'stroke="{CLAY}" stroke-width="2"/>'
           f'<text x="16" y="26" class="tiny" fill="{WA}">'
           + ('ASÍ SÍ · SIEMPRE IGUAL' if lang == 'es' else 'RIGHT · ALWAYS THE SAME') + '</text>'
           f'<text x="328" y="26" class="tiny" fill="{CLAY}">'
           + ('ASÍ NO · TRES VERSIONES' if lang == 'es' else 'WRONG · THREE VERSIONS') + '</text>')
    for i, (a, b) in enumerate(zip(ok, bad)):
        y = 52 + i * 22
        out += (f'<text x="16" y="{y}" class="cap" fill="{INK}">{a}</text>'
                f'<text x="328" y="{y}" class="cap" fill="{CLAY}">{b}</text>')
    return f'<svg viewBox="0 0 600 124" class="fig">{out}</svg>'


def enlaces_calidad(lang='es'):
    """Un enlace bueno contra cincuenta basura."""
    out = (f'<rect x="0" y="0" width="288" height="128" rx="8" fill="{PAPER}" '
           f'stroke="{WA}" stroke-width="2"/>'
           f'<rect x="312" y="0" width="288" height="128" rx="8" fill="{PAPER}" '
           f'stroke="{RULE}" stroke-width="2"/>'
           f'<circle cx="60" cy="58" r="26" fill="{WA}"/>'
           f'<text x="60" y="66" class="pin" style="font-size:22px">1</text>'
           f'<text x="102" y="52" class="stp">' + ('Cámara de' if lang == 'es' else 'Local chamber') + '</text>'
           f'<text x="102" y="70" class="stp">' + ('comercio local' if lang == 'es' else 'of commerce') + '</text>'
           f'<text x="16" y="110" class="cap">'
           + ('Real, local, de tu oficio' if lang == 'es' else 'Real, local, in your trade') + '</text>')
    for i in range(50):
        cx, cy = 336 + (i % 10) * 25, 40 + (i // 10) * 15
        out += f'<circle cx="{cx}" cy="{cy}" r="4.5" fill="{DIM}"/>'
    out += (f'<text x="328" y="110" class="cap">'
            + ('50 enlaces de directorios basura' if lang == 'es' else '50 junk directory links') + '</text>')
    return f'<svg viewBox="0 0 600 134" class="fig">{out}</svg>'


def fuentes_ia(lang='es'):
    """De dónde saca la IA sus respuestas."""
    src = ['Perfil de Google', 'Apple / Bing', 'Directorios', 'Reseñas', 'Tu sitio'] if lang == 'es' \
          else ['Google profile', 'Apple / Bing', 'Directories', 'Reviews', 'Your site']
    out, w = '', 108
    for i, s in enumerate(src):
        x = i * (w + 15)
        out += (f'<rect x="{x}" y="0" width="{w}" height="46" rx="6" fill="{PAPER}" '
                f'stroke="{RULE}" stroke-width="1.5"/>'
                f'<text x="{x+w/2}" y="28" class="cap" text-anchor="middle">{s}</text>'
                f'<line x1="{x+w/2}" y1="46" x2="300" y2="84" stroke="{RULE}" '
                f'stroke-width="1.5" stroke-dasharray="3 3"/>')
    out += (f'<rect x="150" y="84" width="300" height="52" rx="8" fill="{INK}"/>'
            f'<text x="300" y="107" class="capw" text-anchor="middle" '
            f'style="font-family:Archivo;font-weight:800;font-size:15px">'
            + ('RESPUESTA DE IA' if lang == 'es' else 'AI ANSWER') + '</text>'
            f'<text x="300" y="124" class="capw" text-anchor="middle" '
            f'style="fill:#93A7B2">'
            + ('te menciona o no te menciona' if lang == 'es' else 'it names you, or it doesn\'t') + '</text>')
    return f'<svg viewBox="-12 0 624 142" class="fig">{out}</svg>'


def tablero(lang='es'):
    """Las cinco líneas que hay que mirar cada mes."""
    filas = [('Llamadas desde el sitio', '14', '9', True),
             ('Llamadas desde Google', '31', '22', True),
             ('Reseñas nuevas', '4', '2', True),
             ('Trabajos cerrados', '12', '11', True),
             ('De dónde vinieron', '7 Google', '3 referido', None)] if lang == 'es' else \
            [('Calls from the site', '14', '9', True),
             ('Calls from Google', '31', '22', True),
             ('New reviews', '4', '2', True),
             ('Jobs closed', '12', '11', True),
             ('Where they came from', '7 Google', '3 referral', None)]
    out, y = '', 0
    for lbl, a, b, up in filas:
        out += (f'<rect x="0" y="{y}" width="600" height="34" rx="5" fill="{PAPER}"/>'
                f'<text x="14" y="{y+22}" class="cap" fill="{INK}">{lbl}</text>'
                f'<text x="470" y="{y+22}" class="val" text-anchor="end">{a}</text>'
                f'<text x="590" y="{y+22}" class="cap" text-anchor="end">'
                + ('antes: ' if lang == 'es' else 'before: ') + f'{b}</text>')
        if up:
            out += (f'<path d="M488,{y+20} l7,-10 l7,10" fill="none" stroke="{WA}" '
                    f'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>')
        y += 40
    return f'<svg viewBox="0 0 600 {y}" class="fig">{out}</svg>'


def velocidad(lang='es'):
    """Qué pesa más en un sitio lento."""
    items = [('Imágenes sin comprimir', 100), ('Plantillas y plugins de más', 62),
             ('Tipografías y video', 34)] if lang == 'es' else \
            [('Uncompressed images', 100), ('Bloated templates and plugins', 62),
             ('Heavy fonts and video', 34)]
    out, y = '', 0
    for lbl, pct in items:
        out += (f'<text x="0" y="{y+13}" class="row">{lbl}</text>'
                f'<rect x="290" y="{y+2}" width="310" height="16" rx="8" fill="{PAPER}"/>'
                f'<rect x="290" y="{y+2}" width="{3.1*pct}" height="16" rx="8" fill="{SUN}"/>')
        y += 34
    return f'<svg viewBox="0 0 600 {y}" class="fig">{out}</svg>'


def caminos(lang='es'):
    """Los cuatro caminos por los que te encuentran."""
    items = [('EL MAPA', 'Los 3 de arriba'), ('BÚSQUEDA', 'Los sitios web'),
             ('OTROS MAPAS', 'Apple, Yelp'), ('LA IA', 'ChatGPT y demás')] if lang == 'es' else \
            [('THE MAP', 'The top 3'), ('SEARCH', 'The websites'),
             ('OTHER MAPS', 'Apple, Yelp'), ('AI', 'ChatGPT and co.')]
    out, w, gap = '', 138, 16
    for i, (t, sub) in enumerate(items):
        x = i * (w + gap)
        out += (f'<rect x="{x}" y="0" width="{w}" height="78" rx="8" fill="{PAPER}" '
                f'stroke="{RULE}" stroke-width="1.5"/>'
                f'<rect x="{x}" y="0" width="{w}" height="5" rx="2.5" fill="{SUN}"/>'
                f'<text x="{x+w/2}" y="38" class="stp" text-anchor="middle">{t}</text>'
                f'<text x="{x+w/2}" y="58" class="cap" text-anchor="middle">{sub}</text>')
    return f'<svg viewBox="0 0 600 84" class="fig">{out}</svg>'
