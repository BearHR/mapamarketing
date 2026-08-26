# Cómo usar la propuesta

La propuesta se genera desde `_build/make_proposal.py`. Todo lo que cambia por cliente está
en el diccionario `CLIENTE`, hasta arriba del archivo. No hay que tocar nada más.

```bash
python3 _build/make_proposal.py
# -> propuestas/propuesta-<negocio>.pdf
```

Necesita `weasyprint` (`pip3 install weasyprint`).

## Qué llenar, campo por campo

| Campo | Qué poner |
|---|---|
| `negocio`, `contacto` | Nombre del negocio y nombre de pila del dueño. El nombre aparece en la portada y en el cierre. |
| `oficio`, `ciudad`, `ciudades` | Su oficio y las ciudades que cubre. De aquí sale el conteo de páginas. |
| `servicios` | Los servicios que vende. **servicios × ciudades = las páginas que le vas a construir**, y esa cifra aparece sola en el plan y en la inversión. |
| `equipo` | "3 personas", "el dueño y 2 técnicos". |
| `meta` | Lo que él te dijo que quiere lograr, **en sus palabras**. Se le repite de vuelta en la primera página. Es la parte que más hace que sienta que la propuesta es suya. |
| `hallazgos` | De 4 a 7 pares (título, explicación) de la auditoría. Concretos y con números donde se pueda. |
| `competidores`, `tu_posicion` | Los tres que salen arriba de él. Puedes usar nombres reales o "Competidor 1". |
| `ticket`, `cierre`, `repeticion` | Los números que él te dio. De aquí sale el punto de equilibrio. |
| `precio_web`, `precio_mensual`, `meses_compromiso` | $1,500 · $1,200 · 4 meses. |
| `oferta` | `'ambas'`, `'programa'` o `'separado'`. Ver abajo. |

## Cuando no tienes los datos

La propuesta funciona igual con información incompleta. No hay que borrar secciones a mano:

| Si dejas… | Pasa esto |
|---|---|
| `hallazgos = []` | La sección "Qué encontramos" se cambia sola por **"Qué vamos a revisar"**, que lista todo lo que cubre la auditoría gratis. Sirve para mandar la propuesta *antes* de auditar. |
| `competidores = []` | La sección de competencia se omite completa. |
| `ticket = None` | Se omite la página del punto de equilibrio. |
| `servicios = []` | El plan deja de dar el número de páginas y lo describe en general. |
| `equipo = None`, `meta = None` | Esas filas no aparecen en la primera tabla. |

Con todo lleno son 11 páginas; con lo mínimo, 8. Las dos versiones se leen completas.

## Las tres opciones de oferta

Cambia `oferta` según el trato:

**`'ambas'` — por defecto y la que más cierra.** Muestra las dos rutas y una tabla que las
compara. Como el mes 1 de la Opción B se va completo en el sitio, en los primeros 4 meses la
Opción A sale **más barata y con un mes más de trabajo mensual**. Esa tabla vende sola, sin
que tengas que presionar.

| | Opción A · 4 meses | Opción B · sin compromiso |
|---|---|---|
| Sitio web | Incluido | $1,500 |
| Mensual | $1,200 | $1,200 |
| Mes 1 | Sitio + trabajo mensual | Solo el sitio |
| Meses de marketing en los primeros 4 | 4 | 3 |
| Total 4 meses | **$4,800** | $5,100 |

**`'programa'`** — solo la Opción A. Úsalo si ya acordaron el compromiso y no quieres abrir
la puerta a la otra.

**`'separado'`** — solo la Opción B. Para quien ya dijo que no se compromete: el mes 1 se
dedica completo al sitio y el mensual arranca en el mes 2.

## Las tres partes que cierran la venta

**1. "Lo que nos dijiste" (página 2).** Antes de venderle nada le repites su propia meta.
Cuando alguien ve su objetivo escrito con sus palabras, deja de leer un folleto y empieza a
leer un plan.

**2. "Qué encontramos" (página 3).** Los hallazgos son lo único que ninguna otra agencia le
mandó. Entre más específicos, mejor: *"tarda 6.4 segundos"* vale diez veces más que
*"el sitio está lento"*. Sácalos de la auditoría real, aunque te tome media hora.

**3. El punto de equilibrio.** El número se calcula solo con sus cifras. Cuando ve
"3.7 contactos más al mes y esto se paga solo", el precio deja de ser un gasto y se vuelve una
cuenta. Es lo más persuasivo del documento porque no es una promesa tuya: es su propia
aritmética.

## Sobre los 4 meses

Cuatro meses es el mínimo con el que se puede saber algo, no el tiempo en el que el trabajo
termina. La página de tiempos lo dice tal cual: los primeros dos meses paga y ve poco, al mes
4 ya se ve la tendencia, y el trabajo local sigue creciendo después. Decirlo así te evita al
cliente que llega al mes 4 esperando el resultado final y se decepciona.

## Consejos

- Mándalo **por WhatsApp como archivo**, no por correo. Es donde te contestan.
- No lo mandes antes de la llamada. Esto es un cierre, no una presentación.
- Si el cliente pide bajar el precio, no bajes: quita ciudades o servicios y baja el conteo
  de páginas. El precio por trabajo se mantiene y el valor no se devalúa.
- La propuesta dice que vence en 30 días. Cúmplelo.
