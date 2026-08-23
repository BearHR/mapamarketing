# MAPA Marketing — sitio web

Sitio estático (HTML, CSS y JavaScript puro). No necesita build, ni Node, ni base de datos.
Se publica tal cual en GitHub Pages.

---

## 1. Publicar en GitHub Pages

1. Crea un repositorio nuevo en GitHub (público).
2. Sube **todo el contenido de esta carpeta** a la raíz del repo (no dentro de una subcarpeta).
3. Ve a **Settings → Pages**.
4. En *Source* elige **Deploy from a branch**, rama `main`, carpeta `/ (root)`. Guarda.
5. En 1–2 minutos el sitio queda en `https://TU-USUARIO.github.io/TU-REPO/`.

El archivo `.nojekyll` ya está incluido para que GitHub no procese nada raro.

### Dominio propio
1. Compra el dominio.
2. En **Settings → Pages → Custom domain** escribe tu dominio y guarda (GitHub creará un archivo `CNAME`).
3. En tu proveedor de dominio apunta los registros A de GitHub Pages, o un CNAME a `TU-USUARIO.github.io`.
4. Activa **Enforce HTTPS**.

---

## 2. Lo primero que debes cambiar

| Qué | Dónde |
|---|---|
| **Número de WhatsApp** | `assets/js/main.js`, línea `MAPA.PHONE = '527711150327'` — solo dígitos, con código de país, sin `+` ni espacios. |
| Enlaces `href` de respaldo | Busca y reemplaza `wa.me/527711150327` en todos los `.html` (funcionan si el JS no carga). |
| Dominio en `sitemap.xml` y `robots.txt` | Reemplaza `https://TU-DOMINIO.com` por el real. |

Comando rápido para cambiar el número en todo el proyecto (Mac/Linux):

```bash
grep -rl '527711150327' . | xargs sed -i '' 's/527711150327/TUNUEVONUMERO/g'   # macOS
grep -rl '527711150327' . | xargs sed -i  's/527711150327/TUNUEVONUMERO/g'      # Linux
```

---

## 3. Estructura

```
index.html          Inicio (español)
en/                 El sitio completo en inglés (11 páginas)
_src/               Fuentes bilingües — NO se editan los HTML generados
servicios.html      Detalle de los dos servicios
proceso.html        Cómo trabajamos, semana por semana
guia.html           La guía de 11 capítulos (pilar de contenido)
herramientas.html   Hub de herramientas
diagnostico.html    Herramienta 01 — auditoría de visibilidad
calculadora.html    Herramienta 02 — valor de un cliente
publicaciones.html  Herramienta 03 — publicaciones de Google
resenas.html        Herramienta 04 — respuestas a reseñas
citaciones.html     Herramienta 05 — NAP y 30 directorios
404.html            Página de error
robots.txt · sitemap.xml · .nojekyll
assets/css/style.css
assets/js/main.js   Idioma, nav, enlaces de WhatsApp, animaciones
assets/js/tools.js  Lógica de las 5 herramientas
assets/img/favicon.svg
_build/             Scripts de Python que generaron las páginas (opcional, no se publica)
```

`_build/` solo sirve para regenerar las páginas manteniendo el nav y el footer iguales
en todas. Si editas el nav en `index.html` puedes correr:

```bash
python3 _build/pages.py && python3 _build/toolpages.py && python3 _build/guide.py
```

Si prefieres editar cada HTML a mano, borra la carpeta `_build/` sin problema.

---

## 4. Cómo funciona el bilingüe

Cada idioma tiene **su propia URL**:

| Idioma | URL |
|---|---|
| Español (canónico) | `/`, `/servicios.html`, `/guia.html`… |
| Inglés | `/en/`, `/en/servicios.html`, `/en/guia.html`… |

Cada página sale con un solo idioma, un solo `<h1>`, su `canonical` y las tres etiquetas
`hreflang` (`es`, `en`, `x-default`). El selector ES/EN del menú son enlaces entre las dos
versiones, no JavaScript.

### Regenerar el sitio

Las fuentes bilingües viven en `_src/` y llevan marcas `data-l="es"` / `data-l="en"`.
No edites los HTML del raíz ni de `/en/`: se sobrescriben. Edita `_src/index.html` o los
generadores y vuelve a correr:

```bash
python3 _build/pages.py
python3 _build/toolpages.py
python3 _build/guide.py
python3 _build/split.py      # <- genera / y /en/, sitemap.xml y robots.txt
python3 _build/make_pdf.py   # <- genera los dos PDF de la guía en assets/
```

Necesita Python 3 con `beautifulsoup4` y `weasyprint` (`pip3 install beautifulsoup4 weasyprint`).

### La guía en PDF
`_build/make_pdf.py` toma el contenido de `guia.html` y `en/guia.html` y arma los libros:

- `assets/guia-marketing-local-mapa-marketing.pdf` (25 páginas, español)
- `assets/local-marketing-guide-mapa-marketing.pdf` (25 páginas, inglés)

Llevan portada, índice con números de página, numeración y una página de cierre con el
WhatsApp. Si editas un capítulo, vuelve a correr `guide.py`, `split.py` y `make_pdf.py` en
ese orden. El enlace para mandar por WhatsApp es:

```
https://TU-DOMINIO.com/assets/guia-marketing-local-mapa-marketing.pdf
```

### Al conectar tu dominio
Abre `_build/split.py` y cambia la constante `SITE` al inicio del archivo. Vuelve a correr
`python3 _build/split.py` y se actualizan solos todos los `canonical`, los `hreflang`,
el `sitemap.xml`, el `robots.txt` y el JSON-LD.

## 4b. Schema (JSON-LD)

Cada página lleva un bloque `@graph` generado por `_build/split.py`:

- `ProfessionalService` + `Organization` — el negocio, con `areaServed` Estados Unidos,
  idiomas y el WhatsApp como `contactPoint`.
- `WebSite` y `WebPage` con `inLanguage`.
- `BreadcrumbList` en todas las páginas.
- `FAQPage` en la portada (toma las preguntas del acordeón automáticamente).
- `Service` × 2 en la portada y en servicios.
- `Article` en la guía, con la lista de capítulos en `articleSection`.
- `WebApplication` en cada herramienta e `ItemList` en el hub de herramientas.

Para comprobarlo: pega cualquier URL en <https://search.google.com/test/rich-results>.

---

## 5. Cómo funcionan los CTA de WhatsApp

Cualquier enlace con `class="wa"` se convierte automáticamente en un enlace de WhatsApp con
mensaje prellenado:

```html
<a class="wa" href="https://wa.me/527711150327"
   data-msg-es="Hola MAPA, quiero información."
   data-msg-en="Hi MAPA, I'd like some info.">Escríbenos</a>
```

Si el visitante escribió su ciudad en el campo del inicio, se agrega sola al mensaje.
No hay formularios, ni correo, ni teléfono en todo el sitio: todo empuja a WhatsApp.

---

## 6. Pendientes recomendados

- [ ] Cambiar el número de WhatsApp por uno de Estados Unidos (ver notas abajo).
- [ ] Conectar Google Analytics 4 o Plausible (falta a propósito, no quisimos meter scripts sin tu permiso).
- [ ] Crear una imagen `og-image.png` de 1200×630 y añadir `<meta property="og:image">` en cada página.
- [ ] Revisar y ajustar las promesas de la sección "Hablemos claro" del inicio y del FAQ para que
      coincidan exactamente con lo que vas a ofrecer (contratos, propiedad del sitio, reseñas).
- [ ] Cuando tengas los primeros clientes: añadir una página de casos de estudio con números reales.

### Sobre el número +52
El sitio va dirigido a dueños de negocio en Estados Unidos. Un número con lada de México (+52)
puede generar dudas en ese público. Vale la pena conseguir un número de EE. UU. (por ejemplo un
número virtual) y usarlo con WhatsApp Business, que además te da perfil de empresa, catálogo,
mensaje de bienvenida y respuestas rápidas.
