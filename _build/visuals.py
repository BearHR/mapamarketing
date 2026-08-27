# -*- coding: utf-8 -*-
"""Figuras SVG compartidas por la guía y la auditoría.
Todas devuelven SVG en línea; WeasyPrint las dibuja como vectores.
"""

INK, SUN, WA, CLAY, RULE, MUTED = '#0E2233', '#F0A81C', '#25D366', '#DD4B34', '#D8DED2', '#55665F'
PAPER, GREYB = '#EFF1EC', '#B9C2BA'

CSS_FIG = """
.fig{width:100%;height:auto;margin:5mm 0 6mm;display:block;page-break-inside:avoid}
.fig .lbl{font-family:'DM Mono';font-size:11px;letter-spacing:1.6px;fill:#55665F}
.fig .cap{font-family:'Public Sans';font-size:12px;fill:#55665F}
.fig .row{font-family:'Public Sans';font-size:15px;font-weight:600;fill:#0E2233}
.fig .stp{font-family:Archivo;font-size:14px;font-weight:700;fill:#0E2233}
.fig .pin{font-family:Archivo;font-size:13px;font-weight:800;fill:#fff;text-anchor:middle}
.fig .val{font-family:Archivo;font-size:15px;font-weight:800;fill:#0E2233}
.fig .big{font-family:Archivo;font-size:21px;font-weight:900;fill:#0E2233}
.fig .cell{font-family:'Public Sans';font-size:11.5px;fill:#0E2233}
.fig .hd{font-family:'DM Mono';font-size:11px;letter-spacing:1.2px;fill:#55665F}
.sev{width:16mm;height:auto;flex:none;margin-top:1.5mm}
.figcap{font-family:'DM Mono';font-size:7pt;letter-spacing:.16em;text-transform:uppercase;
  color:#55665F;margin:-3mm 0 6mm}
"""

T = {
    'es': dict(puedes='LO QUE PUEDES HACER', llega='LO QUE TE ESTÁ LLEGANDO',
               dejando='lo que estás dejando ir', hoy='Hoy', mes='Mes',
               clientes='CLIENTES QUE TE ENCUENTRAN SOLOS'),
    'en': dict(puedes='WHAT YOU CAN HANDLE', llega='WHAT IS ACTUALLY COMING IN',
               dejando='what you are leaving behind', hoy='Now', mes='Month',
               clientes='CUSTOMERS WHO FIND YOU ON THEIR OWN'),
}


def sev(n):
    """Tres puntos de gravedad."""
    out = ''.join(f'<circle cx="{9+i*22}" cy="9" r="7" fill="{CLAY if i < n else RULE}"/>'
                  for i in range(3))
    return f'<svg viewBox="0 0 62 18" class="sev">{out}</svg>'


def caminos(lang='es'):
    """Los cuatro caminos por los que llega un cliente."""
    if lang == 'en':
        items = [('The map', 'The top three'), ('Search', 'The results'),
                 ('Other maps', 'Apple · Bing · Yelp'), ('AI', 'The assistants')]
        head = 'HOW A CUSTOMER REACHES YOU'
    else:
        items = [('El mapa', 'Los 3 de arriba'), ('La búsqueda', 'Los resultados'),
                 ('Otros mapas', 'Apple · Bing · Yelp'), ('La IA', 'Los asistentes')]
        head = 'POR DÓNDE TE ENCUENTRA UN CLIENTE'
    bw, gap = 138, 16
    out = f'<text x="0" y="12" class="lbl">{head}</text>'
    for i, (t, s) in enumerate(items):
        x = i * (bw + gap)
        out += (f'<rect x="{x}" y="26" width="{bw}" height="82" rx="8" fill="{PAPER}" '
                f'stroke="{RULE}" stroke-width="1.5"/>'
                f'<circle cx="{x+bw/2}" cy="52" r="13" fill="{SUN if i==0 else INK}"/>'
                f'<text x="{x+bw/2}" y="57" class="pin">{i+1}</text>'
                f'<text x="{x+bw/2}" y="82" class="stp" text-anchor="middle">{t}</text>'
                f'<text x="{x+bw/2}" y="98" class="cap" text-anchor="middle" '
                f'style="font-size:11px">{s}</text>')
        if i < 3:
            out += (f'<path d="M{x+bw+3},67 L{x+bw+gap-3},67" stroke="{RULE}" '
                    f'stroke-width="2"/>')
    out += (f'<rect x="0" y="122" width="600" height="34" rx="8" fill="{INK}"/>'
            f'<text x="300" y="144" class="stp" text-anchor="middle" fill="#EFF1EC">'
            f'{"YOUR BUSINESS" if lang=="en" else "TU NEGOCIO"}</text>')
    for i in range(4):
        x = i * (bw + gap) + bw / 2
        out += f'<path d="M{x},108 L{x},122" stroke="{WA}" stroke-width="2.5"/>'
    return f'<svg viewBox="0 0 600 160" class="fig">{out}</svg>'


def factores(lang='es'):
    """Relevancia, distancia, prominencia — con cuánto puedes influir en cada una."""
    if lang == 'en':
        rows = [('Relevance', 'How well you match the search', 100),
                ('Distance', 'How close you are', 35),
                ('Prominence', 'How known you are', 100)]
        head, note = 'THE THREE FACTORS', 'HOW MUCH YOU CAN CONTROL'
    else:
        rows = [('Relevancia', 'Qué tanto coincides con la búsqueda', 100),
                ('Distancia', 'Qué tan cerca estás', 35),
                ('Prominencia', 'Qué tan conocido eres', 100)]
        head, note = 'LOS TRES FACTORES', 'CUÁNTO PUEDES CONTROLAR'
    out = (f'<text x="0" y="12" class="lbl">{head}</text>'
           f'<text x="600" y="12" class="lbl" text-anchor="end">{note}</text>')
    for i, (t, s, pct) in enumerate(rows):
        y = 30 + i * 58
        out += (f'<text x="0" y="{y+14}" class="stp">{t}</text>'
                f'<text x="0" y="{y+32}" class="cap">{s}</text>'
                f'<rect x="330" y="{y+4}" width="270" height="26" rx="6" fill="{PAPER}"/>'
                f'<rect x="330" y="{y+4}" width="{270*pct/100}" height="26" rx="6" '
                f'fill="{WA if pct > 50 else GREYB}"/>')
        if i < 2:
            out += f'<line x1="0" y1="{y+46}" x2="600" y2="{y+46}" stroke="{RULE}" stroke-width="1"/>'
    return f'<svg viewBox="0 0 600 {30+3*58}" class="fig">{out}</svg>'


def matriz(servicios, ciudades, lang='es'):
    """Servicios × ciudades = las páginas que necesitas."""
    servicios = servicios[:4]; ciudades = ciudades[:4]
    cw, rh, lw = 112, 34, 176
    celda = '1 page' if lang == 'en' else '1 página'
    W = lw + len(ciudades) * cw
    H = 34 + len(servicios) * rh + 34
    out = ''
    for j, c in enumerate(ciudades):
        out += (f'<text x="{lw+j*cw+cw/2}" y="20" class="hd" text-anchor="middle">'
                f'{c[:12].upper()}</text>')
    for i, s in enumerate(servicios):
        y = 30 + i * rh
        out += f'<text x="0" y="{y+22}" class="cell">{s[:20]}</text>'
        for j in range(len(ciudades)):
            x = lw + j * cw
            out += (f'<rect x="{x+4}" y="{y+4}" width="{cw-8}" height="{rh-8}" rx="5" '
                    f'fill="rgba(37,211,102,.16)" stroke="{WA}" stroke-width="1.2"/>'
                    f'<text x="{x+cw/2}" y="{y+21}" class="cap" text-anchor="middle" '
                    f'fill="{INK}">{celda}</text>')
    n = len(servicios) * len(ciudades)
    txt = (f'{len(servicios)} × {len(ciudades)} = {n} '
           + ('pages to build' if lang == 'en' else 'páginas que construir'))
    out += (f'<rect x="0" y="{H-26}" width="{W}" height="26" rx="6" fill="{INK}"/>'
            f'<text x="{W/2}" y="{H-8}" class="stp" text-anchor="middle" fill="#EFF1EC">{txt}</text>')
    return f'<svg viewBox="0 0 {W} {H}" class="fig">{out}</svg>'


def nap(lang='es'):
    """NAP consistente contra NAP roto."""
    ok = ['Ramirez Plumbing LLC', '1420 Bellaire Boulevard', 'Houston, TX 77081',
          '(713) 555-0142']
    bad = ['Ramirez Plumbing', '1420 Bellaire Blvd.', 'Houston TX 77081', '713-555-0142']
    hl = ('CORRECT · THE SAME EVERYWHERE', 'INCONSISTENT · GOOGLE HESITATES') if lang == 'en' \
        else ('BIEN · IGUAL EN TODOS LADOS', 'MAL · GOOGLE DUDA')
    out = (f'<text x="0" y="12" class="lbl" fill="{WA}">{hl[0]}</text>'
           f'<text x="310" y="12" class="lbl" fill="{CLAY}">{hl[1]}</text>'
           f'<rect x="0" y="22" width="285" height="112" rx="8" fill="rgba(37,211,102,.10)" '
           f'stroke="{WA}" stroke-width="1.5"/>'
           f'<rect x="310" y="22" width="285" height="112" rx="8" fill="rgba(221,75,52,.08)" '
           f'stroke="{CLAY}" stroke-width="1.5"/>')
    for i in range(4):
        y = 46 + i * 24
        out += (f'<text x="16" y="{y}" class="cell">{ok[i]}</text>'
                f'<text x="326" y="{y}" class="cell" fill="{CLAY}">{bad[i]}</text>')
    return f'<svg viewBox="0 0 600 140" class="fig">{out}</svg>'


def perfil(lang='es'):
    """Anatomía del Perfil de Negocio de Google."""
    if lang == 'en':
        parts = [('Primary category', 'Weighs most of all'),
                 ('Services list', 'Almost nobody fills it in'),
                 ('Photos', 'New ones every month'),
                 ('Posts', 'Keeps the profile alive'),
                 ('Reviews & replies', 'Moves the map and the decision')]
        head = 'WHAT ACTUALLY DECIDES YOUR RANKING'
    else:
        parts = [('Categoría principal', 'Lo que más pesa de todo'),
                 ('Lista de servicios', 'Casi nadie la llena'),
                 ('Fotos', 'Nuevas cada mes'),
                 ('Publicaciones', 'Mantienen vivo el perfil'),
                 ('Reseñas y respuestas', 'Mueven el mapa y la decisión')]
        head = 'LO QUE DE VERDAD DECIDE TU POSICIÓN'
    out = f'<text x="0" y="12" class="lbl">{head}</text>'
    for i, (t, s) in enumerate(parts):
        y = 26 + i * 42
        w_ = 600 - i * 46
        out += (f'<rect x="0" y="{y}" width="{w_}" height="34" rx="7" fill="{PAPER}" '
                f'stroke="{RULE}" stroke-width="1.2"/>'
                f'<rect x="0" y="{y}" width="6" height="34" rx="3" '
                f'fill="{SUN if i == 0 else INK}"/>'
                f'<text x="18" y="{y+16}" class="stp">{t}</text>'
                f'<text x="18" y="{y+29}" class="cap">{s}</text>')
    return f'<svg viewBox="0 0 600 {26+5*42}" class="fig">{out}</svg>'


def enlaces(lang='es'):
    """Un enlace bueno contra cincuenta comprados. Texto en líneas cortas
    para que nunca se salga de su caja."""
    if lang == 'en':
        ta, tb = 'One local link', 'Fifty bought links'
        la = ['Chamber of commerce,', 'supplier, sponsorship']
        lb = ['Sites that exist only', 'to sell links']
        fa, fb = 'Works, and keeps working', 'No help now, penalties later'
        vs = 'beats'
    else:
        ta, tb = 'Un enlace local', 'Cincuenta comprados'
        la = ['Cámara de comercio,', 'proveedor, patrocinio']
        lb = ['Sitios que solo existen', 'para vender enlaces']
        fa, fb = 'Sirve hoy y sigue sirviendo', 'Hoy no sirven, mañana penalizan'
        vs = 'vale más que'

    bw, gapc = 262, 76
    xr = bw + gapc
    out = (f'<rect x="0" y="14" width="{bw}" height="132" rx="8" '
           f'fill="rgba(37,211,102,.10)" stroke="{WA}" stroke-width="1.5"/>'
           f'<rect x="{xr}" y="14" width="{bw}" height="132" rx="8" fill="{PAPER}" '
           f'stroke="{RULE}" stroke-width="1.5"/>')
    for x0, num, col, t, lines, foot, fcol in (
            (0, '1', WA, ta, la, fa, WA),
            (xr, '50', '#9AA69E', tb, lb, fb, CLAY)):
        out += (f'<circle cx="{x0+34}" cy="48" r="17" fill="{col}"/>'
                f'<text x="{x0+34}" y="54" class="pin" style="font-size:15px">{num}</text>'
                f'<text x="{x0+62}" y="54" class="stp">{t}</text>')
        for k, ln in enumerate(lines):
            out += (f'<text x="{x0+18}" y="{86+k*17}" class="cap" '
                    f'style="font-size:11px">{ln}</text>')
        out += (f'<line x1="{x0+18}" y1="{124}" x2="{x0+bw-18}" y2="124" '
                f'stroke="{RULE}" stroke-width="1"/>'
                f'<text x="{x0+18}" y="139" class="cap" style="font-size:11px" '
                f'fill="{fcol}">{foot}</text>')
    cx = bw + gapc / 2
    out += (f'<text x="{cx}" y="72" style="font-family:Archivo;font-size:26px;'
            f'font-weight:900;fill:{INK}" text-anchor="middle">&gt;</text>'
            f'<text x="{cx}" y="92" class="cap" style="font-size:10px" '
            f'text-anchor="middle">{vs}</text>')
    return f'<svg viewBox="0 0 600 158" class="fig">{out}</svg>'


def scorecard(lang='es'):
    """El tablero de una hoja."""
    if lang == 'en':
        rows = [('Calls from the site', '14', '9'), ('Calls from Google', '31', '22'),
                ('New reviews', '4', '2'), ('Jobs closed', '12', '10')]
        h1, h2 = 'THIS MONTH', 'LAST MONTH'
    else:
        rows = [('Llamadas desde el sitio', '14', '9'), ('Llamadas desde Google', '31', '22'),
                ('Reseñas nuevas', '4', '2'), ('Trabajos cerrados', '12', '10')]
        h1, h2 = 'ESTE MES', 'MES PASADO'
    out = (f'<text x="380" y="12" class="lbl" text-anchor="middle">{h1}</text>'
           f'<text x="510" y="12" class="lbl" text-anchor="middle">{h2}</text>')
    for i, (t, a, b) in enumerate(rows):
        y = 22 + i * 40
        up = int(a) > int(b)
        out += (f'<rect x="0" y="{y}" width="600" height="32" rx="6" fill="{PAPER}"/>'
                f'<text x="16" y="{y+21}" class="row">{t}</text>'
                f'<text x="380" y="{y+22}" class="big" text-anchor="middle" '
                f'fill="{WA if up else INK}">{a}</text>'
                f'<text x="510" y="{y+21}" class="row" text-anchor="middle" fill="{MUTED}">{b}</text>'
                f'<text x="575" y="{y+21}" class="row" fill="{WA if up else CLAY}">'
                f'{"↑" if up else "↓"}</text>')
    return f'<svg viewBox="0 0 600 {22+4*40}" class="fig">{out}</svg>'


# --------------------------------------------------------------------------
# Figuras para la auditoría
# --------------------------------------------------------------------------
def gauge(score, lang='es'):
    """Calificación general sobre 100."""
    col = WA if score >= 70 else (SUN if score >= 40 else CLAY)
    lab = ('YOUR SCORE' if lang == 'en' else 'TU CALIFICACIÓN')
    return f'''<svg viewBox="0 0 600 108" class="fig">
      <text x="0" y="14" class="lbl">{lab}</text>
      <text x="0" y="82" style="font-family:Archivo;font-size:62px;font-weight:900;
        fill:{col}">{score}</text>
      <text x="{28+len(str(score))*36}" y="82" style="font-family:'DM Mono';font-size:20px;
        fill:{MUTED}">/ 100</text>
      <rect x="0" y="94" width="600" height="12" rx="6" fill="{PAPER}"/>
      <rect x="0" y="94" width="{6*score}" height="12" rx="6" fill="{col}"/>
    </svg>'''


def areas(items, lang='es'):
    """Desglose por área: [(nombre, 0-100)]."""
    out = ''
    for i, (t, pct) in enumerate(items):
        y = i * 44
        col = WA if pct >= 70 else (SUN if pct >= 40 else CLAY)
        out += (f'<text x="0" y="{y+20}" class="row">{t}</text>'
                f'<rect x="250" y="{y+8}" width="290" height="18" rx="5" fill="{PAPER}"/>'
                f'<rect x="250" y="{y+8}" width="{290*pct/100}" height="18" rx="5" fill="{col}"/>'
                f'<text x="600" y="{y+22}" class="val" text-anchor="end">{pct}</text>')
    return f'<svg viewBox="0 0 600 {len(items)*44}" class="fig">{out}</svg>'


def rank(competidores, negocio, pos_txt):
    """Paquete de tres del mapa con el cliente fuera."""
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


def mapas4(estado, lang='es'):
    """Estado en los cuatro mapas: dict nombre -> True/False."""
    out = ''
    bw, gap = 138, 16
    for i, (n, ok) in enumerate(estado.items()):
        x = i * (bw + gap)
        col = WA if ok else CLAY
        out += (f'<rect x="{x}" y="10" width="{bw}" height="74" rx="8" fill="{PAPER}" '
                f'stroke="{col}" stroke-width="2"/>'
                f'<circle cx="{x+bw/2}" cy="36" r="14" fill="{col}"/>')
        if ok:
            out += (f'<path d="M{x+bw/2-6},36 L{x+bw/2-1},41 L{x+bw/2+7},32" stroke="#fff" '
                    f'stroke-width="3" fill="none" stroke-linecap="round"/>')
        else:
            out += (f'<path d="M{x+bw/2-5},31 L{x+bw/2+5},41 M{x+bw/2+5},31 '
                    f'L{x+bw/2-5},41" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')
        out += f'<text x="{x+bw/2}" y="72" class="stp" text-anchor="middle">{n}</text>'
    return f'<svg viewBox="0 0 600 94" class="fig">{out}</svg>'


def ruta(pasos):
    """Línea de tiempo horizontal con paradas: [(título, subtítulo)]."""
    n = len(pasos)
    x0, x1 = 72, 528
    out = f'<line x1="{x0}" y1="26" x2="{x1}" y2="26" stroke="{RULE}" stroke-width="3"/>'
    for i, (t, sub) in enumerate(pasos):
        cx = x0 + (x1 - x0) / (n - 1) * i if n > 1 else 300
        col = SUN if i == 0 else INK
        out += (f'<circle cx="{cx}" cy="26" r="13" fill="{col}"/>'
                f'<text x="{cx}" y="31" class="pin">{i+1}</text>'
                f'<text x="{cx}" y="60" class="stp" text-anchor="middle">{t}</text>'
                f'<text x="{cx}" y="77" class="cap" text-anchor="middle">{sub}</text>')
    return f'<svg viewBox="0 0 600 88" class="fig">{out}</svg>'


# ==========================================================================
# Variantes estrechas: la misma información apilada, para pantallas chicas.
# No se hace scroll horizontal; cada figura se rearma en una columna.
# ==========================================================================
NW = 360


def caminos_n(lang='es'):
    if lang == 'en':
        items = [('The map', 'The top three'), ('Search', 'The results'),
                 ('Other maps', 'Apple · Bing · Yelp'), ('AI', 'The assistants')]
        head, mine = 'HOW A CUSTOMER REACHES YOU', 'YOUR BUSINESS'
    else:
        items = [('El mapa', 'Los 3 de arriba'), ('La búsqueda', 'Los resultados'),
                 ('Otros mapas', 'Apple · Bing · Yelp'), ('La IA', 'Los asistentes')]
        head, mine = 'POR DÓNDE TE ENCUENTRA UN CLIENTE', 'TU NEGOCIO'
    out = f'<text x="0" y="13" class="lbl">{head}</text>'
    rh = 52
    for i, (t, s_) in enumerate(items):
        y = 26 + i * rh
        out += (f'<rect x="0" y="{y}" width="{NW}" height="44" rx="8" fill="{PAPER}" '
                f'stroke="{RULE}" stroke-width="1.5"/>'
                f'<circle cx="26" cy="{y+22}" r="13" fill="{SUN if i==0 else INK}"/>'
                f'<text x="26" y="{y+27}" class="pin">{i+1}</text>'
                f'<text x="52" y="{y+19}" class="stp">{t}</text>'
                f'<text x="52" y="{y+35}" class="cap">{s_}</text>')
    y = 26 + 4 * rh + 6
    out += (f'<rect x="0" y="{y}" width="{NW}" height="38" rx="8" fill="{INK}"/>'
            f'<text x="{NW/2}" y="{y+24}" class="stp" text-anchor="middle" '
            f'fill="#EFF1EC">{mine}</text>')
    return f'<svg viewBox="0 0 {NW} {y+44}" class="fig">{out}</svg>'


def factores_n(lang='es'):
    if lang == 'en':
        rows = [('Relevance', 'How well you match the search', 100),
                ('Distance', 'How close you are', 35),
                ('Prominence', 'How known you are', 100)]
        head = 'THE THREE FACTORS · HOW MUCH YOU CONTROL'
    else:
        rows = [('Relevancia', 'Qué tanto coincides con la búsqueda', 100),
                ('Distancia', 'Qué tan cerca estás', 35),
                ('Prominencia', 'Qué tan conocido eres', 100)]
        head = 'LOS TRES FACTORES · CUÁNTO CONTROLAS'
    out = f'<text x="0" y="13" class="lbl">{head}</text>'
    rh = 74
    for i, (t, s_, pct) in enumerate(rows):
        y = 30 + i * rh
        out += (f'<text x="0" y="{y+14}" class="stp">{t}</text>'
                f'<text x="0" y="{y+31}" class="cap">{s_}</text>'
                f'<rect x="0" y="{y+40}" width="{NW}" height="20" rx="5" fill="{PAPER}"/>'
                f'<rect x="0" y="{y+40}" width="{NW*pct/100}" height="20" rx="5" '
                f'fill="{WA if pct > 50 else GREYB}"/>')
    return f'<svg viewBox="0 0 {NW} {30+3*rh}" class="fig">{out}</svg>'


def matriz_n(servicios, ciudades, lang='es'):
    servicios, ciudades = servicios[:4], ciudades[:4]
    n = len(servicios) * len(ciudades)
    cw = (NW - 8 * (len(ciudades) - 1)) / len(ciudades)
    out, rh = '', 74
    for i, sv in enumerate(servicios):
        y = i * rh
        out += f'<text x="0" y="{y+14}" class="stp">{sv[:26]}</text>'
        for j, c in enumerate(ciudades):
            x = j * (cw + 8)
            out += (f'<rect x="{x}" y="{y+24}" width="{cw}" height="34" rx="5" '
                    f'fill="rgba(37,211,102,.16)" stroke="{WA}" stroke-width="1.2"/>'
                    f'<text x="{x+cw/2}" y="{y+45}" class="cap" text-anchor="middle" '
                    f'fill="{INK}">{c[:9]}</text>')
    txt = (f'{len(servicios)} × {len(ciudades)} = {n} '
           + ('pages' if lang == 'en' else 'páginas'))
    y = len(servicios) * rh + 4
    out += (f'<rect x="0" y="{y}" width="{NW}" height="32" rx="6" fill="{INK}"/>'
            f'<text x="{NW/2}" y="{y+22}" class="stp" text-anchor="middle" '
            f'fill="#EFF1EC">{txt}</text>')
    return f'<svg viewBox="0 0 {NW} {y+38}" class="fig">{out}</svg>'


def ruta_n(pasos):
    out, rh = '', 54
    for i, (t, sub) in enumerate(pasos):
        y = i * rh
        if i < len(pasos) - 1:
            out += (f'<line x1="20" y1="{y+34}" x2="20" y2="{y+rh+6}" '
                    f'stroke="{RULE}" stroke-width="3"/>')
        out += (f'<circle cx="20" cy="{y+20}" r="13" fill="{SUN if i==0 else INK}"/>'
                f'<text x="20" y="{y+25}" class="pin">{i+1}</text>'
                f'<text x="46" y="{y+17}" class="stp">{t}</text>'
                f'<text x="46" y="{y+33}" class="cap">{sub}</text>')
    return f'<svg viewBox="0 0 {NW} {len(pasos)*rh}" class="fig">{out}</svg>'


def nap_n(lang='es'):
    ok = ['Ramirez Plumbing LLC', '1420 Bellaire Boulevard', 'Houston, TX 77081', '(713) 555-0142']
    bad = ['Ramirez Plumbing', '1420 Bellaire Blvd.', 'Houston TX 77081', '713-555-0142']
    hl = ('CORRECT · THE SAME EVERYWHERE', 'INCONSISTENT · GOOGLE HESITATES') if lang == 'en' \
        else ('BIEN · IGUAL EN TODOS LADOS', 'MAL · GOOGLE DUDA')
    out = ''
    for k, (lab, vals, col, fill) in enumerate([
            (hl[0], ok, WA, 'rgba(37,211,102,.10)'),
            (hl[1], bad, CLAY, 'rgba(221,75,52,.08)')]):
        y = k * 132
        out += (f'<text x="0" y="{y+11}" class="lbl" fill="{col}">{lab}</text>'
                f'<rect x="0" y="{y+20}" width="{NW}" height="96" rx="8" fill="{fill}" '
                f'stroke="{col}" stroke-width="1.5"/>')
        for i, v in enumerate(vals):
            out += (f'<text x="14" y="{y+42+i*21}" class="cell" '
                    f'fill="{INK if k == 0 else CLAY}">{v}</text>')
    return f'<svg viewBox="0 0 {NW} 264" class="fig">{out}</svg>'


def enlaces_n(lang='es'):
    if lang == 'en':
        blocks = [('1', 'One local link', ['Chamber of commerce,', 'supplier, sponsorship'],
                   'Works, and keeps working', WA, 'rgba(37,211,102,.10)', WA),
                  ('50', 'Fifty bought links', ['Sites that exist only', 'to sell links'],
                   'No help now, penalties later', '#9AA69E', PAPER, CLAY)]
    else:
        blocks = [('1', 'Un enlace local', ['Cámara de comercio,', 'proveedor, patrocinio'],
                   'Sirve hoy y sigue sirviendo', WA, 'rgba(37,211,102,.10)', WA),
                  ('50', 'Cincuenta comprados', ['Sitios que solo existen', 'para vender enlaces'],
                   'Hoy no sirven, mañana penalizan', '#9AA69E', PAPER, CLAY)]
    out = ''
    for k, (num, t, lines, foot, ncol, fill, fcol) in enumerate(blocks):
        y = k * 140
        out += (f'<rect x="0" y="{y}" width="{NW}" height="124" rx="8" fill="{fill}" '
                f'stroke="{ncol if k == 0 else RULE}" stroke-width="1.5"/>'
                f'<circle cx="30" cy="{y+32}" r="16" fill="{ncol}"/>'
                f'<text x="30" y="{y+38}" class="pin" style="font-size:14px">{num}</text>'
                f'<text x="56" y="{y+38}" class="stp">{t}</text>')
        for i, ln in enumerate(lines):
            out += f'<text x="16" y="{y+66+i*17}" class="cap" style="font-size:11px">{ln}</text>'
        out += (f'<line x1="16" y1="{y+100}" x2="{NW-16}" y2="{y+100}" stroke="{RULE}" '
                f'stroke-width="1"/><text x="16" y="{y+115}" class="cap" '
                f'style="font-size:11px" fill="{fcol}">{foot}</text>')
    return f'<svg viewBox="0 0 {NW} 264" class="fig">{out}</svg>'


def perfil_n(lang='es'):
    if lang == 'en':
        parts = [('Primary category', 'Weighs most of all'),
                 ('Services list', 'Almost nobody fills it in'),
                 ('Photos', 'New ones every month'),
                 ('Posts', 'Keeps the profile alive'),
                 ('Reviews & replies', 'Moves the map and the decision')]
        head = 'WHAT DECIDES YOUR RANKING'
    else:
        parts = [('Categoría principal', 'Lo que más pesa de todo'),
                 ('Lista de servicios', 'Casi nadie la llena'),
                 ('Fotos', 'Nuevas cada mes'),
                 ('Publicaciones', 'Mantienen vivo el perfil'),
                 ('Reseñas y respuestas', 'Mueven el mapa y la decisión')]
        head = 'LO QUE DECIDE TU POSICIÓN'
    out = f'<text x="0" y="13" class="lbl">{head}</text>'
    for i, (t, s_) in enumerate(parts):
        y = 26 + i * 48
        out += (f'<rect x="0" y="{y}" width="{NW}" height="40" rx="7" fill="{PAPER}" '
                f'stroke="{RULE}" stroke-width="1.2"/>'
                f'<rect x="0" y="{y}" width="6" height="40" rx="3" '
                f'fill="{SUN if i == 0 else INK}"/>'
                f'<text x="18" y="{y+18}" class="stp">{t}</text>'
                f'<text x="18" y="{y+33}" class="cap">{s_}</text>')
    return f'<svg viewBox="0 0 {NW} {26+5*48}" class="fig">{out}</svg>'


def scorecard_n(lang='es'):
    if lang == 'en':
        rows = [('Calls from the site', '14', '9'), ('Calls from Google', '31', '22'),
                ('New reviews', '4', '2'), ('Jobs closed', '12', '10')]
        prev = 'last month'
    else:
        rows = [('Llamadas desde el sitio', '14', '9'), ('Llamadas desde Google', '31', '22'),
                ('Reseñas nuevas', '4', '2'), ('Trabajos cerrados', '12', '10')]
        prev = 'mes pasado'
    out, rh = '', 58
    for i, (t, a, b) in enumerate(rows):
        y = i * rh
        up = int(a) > int(b)
        out += (f'<rect x="0" y="{y}" width="{NW}" height="50" rx="6" fill="{PAPER}"/>'
                f'<text x="14" y="{y+21}" class="row">{t}</text>'
                f'<text x="14" y="{y+39}" class="cap">{prev}: {b}</text>'
                f'<text x="{NW-38}" y="{y+34}" class="big" text-anchor="end" '
                f'fill="{WA if up else INK}">{a}</text>'
                f'<text x="{NW-14}" y="{y+33}" class="row" text-anchor="end" '
                f'fill="{WA if up else CLAY}">{"↑" if up else "↓"}</text>')
    return f'<svg viewBox="0 0 {NW} {len(rows)*rh}" class="fig">{out}</svg>'
