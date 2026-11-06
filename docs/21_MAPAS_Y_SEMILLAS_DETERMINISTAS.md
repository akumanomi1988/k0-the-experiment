# 21 — Generación de mapa completamente determinista

## Reglas de terreno
El mapa es una **cuadrícula lógica universal edificable**. El bioma inicial cambia exclusivamente el aspecto y nunca las coordenadas disponibles. Tamaño inicial 48×48 casillas (`x=0..47`,`y=0..47`), centro = `(23,23)`. Al desbloquear era N el ancho y alto pasan a `48 + 16*(N-1)`, centrando la región inicial sin mover los edificios existentes en coordenadas de mundo; límite absoluto 256×256 (era 13 = 240×240). Las coordenadas lógicas absolutas pueden ser negativas al expandir a ambos lados de (0,0); no serializar offsets de cámara como coordenadas de edificio.

## Determinismo de decoración
`terrainVariant = SHA256(utf8('{seasonSeed}|{nationId}|{x}|{y}|terrain'))[0] % 4` ; `decorationPresent = SHA256(utf8('{seasonSeed}|{nationId}|{x}|{y}|deco'))[0] % 10 == 0`; `decorationVariant = digest[1] % 8`. Todos los hashes se computan en UTF-8 con IDs normalizados, bytes iniciales sin signo. Las decoraciones no impiden construir y desaparecen si la parcela se ocupa; se guarda en evento de presentación para animar. No se utiliza ruido Perlin, dependencia de motor gráfico o `Random()` para elegir recursos económicos.

## Ubicación de edificios
Se reserva un rectángulo de `footprintTiles` sin solapamientos de otras parcelas de edificios ni la plaza de arranque (3×3 libre alrededor de `(23,23)`). Buscar en orden `(distance=abs(x-23)+abs(y-23), y, x)` dentro de los límites, con `x/y` representando la esquina inferior izquierda de la huella; el primero que cabe gana. Al expandir, el edificio anterior conserva coordenadas y parcela. Si no cabe aún, `WAITING_PLOT` hasta expansión; no gastar materiales antes de disponer de parcela. Las obras automáticas obligatorias pueden tener reservados 2 slots de emergencia alrededor de área central para impedir bloqueo por obras cosméticas; esos slots se desbloquean al acabar la era.

## Reproducción visual
El cliente puede desplazar cámara y LOD libremente; nunca enviar coordenadas de render como verdad económica. Misma semilla y mismos edificios deben reproducir el mismo mapa lógico con cualquier proveedor de streaming. La apariencia de cada bioma usa paleta propia pero límites de construcción iguales.
