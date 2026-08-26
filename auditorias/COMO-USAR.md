# La revisión gratis

Es lo que mandas por WhatsApp cuando alguien contesta al anuncio. Seis páginas, se lee en
el teléfono en dos minutos y termina en una sola pregunta.

```bash
python3 _build/make_audit.py     # -> auditorias/revision-<negocio>.pdf
```

## Qué llenar

Todo está en el diccionario `NEGOCIO`, arriba de `_build/make_audit.py`.

| Campo | Qué poner |
|---|---|
| `areas` | Cinco calificaciones de 0 a 100. **El total se calcula solo** y el veredicto cambia según el número. |
| `mapas` | Estado en cada plataforma: `True` (bien), `'medio'` (existe pero incompleto), `False` (no está). |
| `competidores`, `tu_posicion` | Los tres que salen arriba y dónde apareces tú. |
| `hallazgos` | `(gravedad 1-3, título, explicación)`. La gravedad dibuja los puntos rojos. |
| `prioridades` | `(texto, impacto 1-3)`. El impacto dibuja la barra de la derecha. |

## Cómo puntuar sin complicarte

No busques precisión: busca que el número refleje la realidad. Una guía rápida:

- **0–25** — no existe o está roto (sin perfil, sin sitio, categoría mal).
- **26–50** — existe pero a medias (perfil reclamado y abandonado, sitio lento).
- **51–75** — funciona, le faltan detalles.
- **76–100** — bien trabajado.

Con cinco áreas puntuadas así, el total sale solo y casi siempre cae donde debe.

## Por qué funciona como cierre

**La calificación es lo primero que ve.** Un número bajo en rojo duele más que un párrafo
explicando lo mismo, y es imposible discutirlo porque sale de su propio negocio.

**Las tarjetas de los cuatro mapas** son la página que más reacción provoca. Ver dos taches
rojos en Apple y Bing hace la pregunta sola: *¿y desde cuándo llevo así?*

**La última página no vende.** Ofrece la guía gratis primero y solo después pregunta si
quiere que lo hagan ustedes. Quien acaba de ver su calificación en 34 rara vez elige hacerlo
solo, pero dejarle la puerta abierta es lo que hace que confíe en el número.

## Consejos

- Mándalo como archivo por WhatsApp, no como enlace.
- Tarda entre 20 y 30 minutos hacerlo bien. No lo hagas en cinco: los hallazgos genéricos
  se notan y matan el efecto.
- Un hallazgo con número (*"6.4 segundos"*, *"14 meses sin reseñas"*) vale por tres
  hallazgos vagos.
- No mandes más de seis hallazgos aunque encuentres doce. La lista larga abruma y diluye
  lo urgente.
