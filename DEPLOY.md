# Publicar el sitio

Este paquete es el repositorio completo. Sube **todo lo que está aquí dentro** a la raíz
de `bearhr/mapamarketing`, incluidos los archivos ocultos.

## Antes de subir, revisa que existan

- **`.nojekyll`** — archivo vacío, sin él GitHub ignora carpetas que empiezan con `_`.
  En Mac se ve con `Cmd+Shift+.` en Finder; en Windows, activando "Elementos ocultos".
- **`CNAME`** — debe decir `mapamarketing.com` y nada más.

Los dos venían faltando o mal en la versión anterior.

## Qué cambió respecto a lo que tenías subido

**Todos los `canonical` y `hreflang` apuntaban a `bearhr.github.io/mapamarketing`** aunque
tu dominio ya es `mapamarketing.com`. Eso le dice a Google que la versión buena es la de
github.io y que la de tu dominio es una copia. Ya está corregido en las 22 páginas, en el
`sitemap.xml` y en el `robots.txt`.

## Estructura

```
index.html, servicios.html, …   El sitio en español (canónico)
en/                             El mismo sitio en inglés
assets/css · js · img           Estilos, scripts, favicon
assets/*.pdf                    La guía, enlazada desde guia.html
_src/                           Fuentes bilingües (NO se publican solas)
_build/                         Scripts para regenerar
CNAME · .nojekyll · robots.txt · sitemap.xml
```

## Regenerar después de editar

Edita `_src/index.html` o los scripts de `_build/`, nunca los HTML de la raíz ni de `en/`:
se sobrescriben.

```bash
pip3 install beautifulsoup4 weasyprint

python3 _build/pages.py        # servicios, proceso, herramientas, 404
python3 _build/toolpages.py    # las 5 herramientas
python3 _build/guide.py        # la guía
python3 _build/split.py        # genera / y /en/, sitemap y robots
python3 _build/make_pdf.py     # regenera los PDF de la guía en assets/
```

Si algún día cambias de dominio, cambia `SITE` al inicio de `_build/split.py` y vuelve a
correr `split.py`: se actualizan solos los canonical, los hreflang, el sitemap y el JSON-LD.
