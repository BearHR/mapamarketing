import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
IDX = (ROOT / "index.html").read_text(encoding="utf-8")

def between(start, end, s=IDX):
    i = s.index(start); j = s.index(end, i)
    return s[i:j+len(end)]

SKIP = between('<a class="skip"', '</a>')
NAV = between('<header class="nav">', '</header>')
FOOT = between('<footer class="foot">', '</footer>')
FLOAT = between('<a class="wafloat', '</a>\n')

HEAD = """<!DOCTYPE html>
<html lang="es" data-lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#0E2233">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=DM+Mono:wght@400;500&family=Public+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
{extrahead}</head>
<body>
"""

WA_ICON = ('<svg width="19" height="19" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
           '<path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38a9.9 9.9 0 0 0 '
           '4.79 1.22h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm5.8 14.16c-.24.68-1.42 1.3-1.96 '
           '1.35-.5.05-1.14.07-1.83-.11-.42-.13-.96-.31-1.66-.61-2.92-1.26-4.83-4.2-4.98-4.4-.14-.2-1.19-1.58-1.19-3.01 '
           '0-1.43.75-2.13 1.02-2.42.27-.29.58-.36.78-.36h.56c.18 0 .42-.07.66.5.24.58.82 2 .89 2.15.07.14.12.31.02.5-.1.2-.15.32-.29.49-.15.17-.31.38-.44.51-.15.14-.3.3-.13.59.17.29.75 1.24 1.61 '
           '2.01 1.11.99 2.04 1.3 2.33 1.44.29.15.46.12.63-.07.17-.2.73-.85.92-1.14.2-.29.39-.24.66-.15.27.1 1.69.8 1.98.94.29.15.48.22.55.34.07.12.07.7-.17 1.38z"/></svg>')


def wa(msg_es, msg_en, label_es, label_en, cls="btn btn--wa", icon=True, eid=None):
    return (f'<a class="{cls} wa"{" id="+chr(34)+eid+chr(34) if eid else ""} href="https://wa.me/527711150327" '
            f'data-msg-es="{msg_es}" data-msg-en="{msg_en}">'
            f'{WA_ICON if icon else ""}'
            f'<span data-l="es">{label_es}</span><span data-l="en">{label_en}</span></a>')


def page(fn, title, desc, body, extrahead="", extrascript=""):
    html = HEAD.format(title=title, desc=desc, extrahead=extrahead)
    html += SKIP + "\n\n" + NAV + "\n\n<main id=\"main\">\n" + body + "\n</main>\n\n" + FOOT + "\n\n" + FLOAT + "\n"
    html += '<script src="assets/js/main.js"></script>\n' + extrascript + "</body>\n</html>\n"
    (ROOT / fn).write_text(html, encoding="utf-8")
    print("wrote", fn, len(html))
