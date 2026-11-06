# 51 — Generación de mapa, distribución y simulación visual

**Objetivo:** que todos los escenarios produzcan un mundo estable, legible y reproducible sin convertir pathfinding en lógica económica.

## Reglas territoriales

Base inicial por nación: 48×48 tiles lógicos de 32×16; expansión de margen de ocho tiles por era, máximo 256×256. Tres facciones comienzan con **la misma capacidad matemática** de fuentes naturales de comida, madera, piedra, conocimiento y trabajo; mineral aparece desde era 3. Los biomas son cosméticos. El generador recibe `seasonSeed`, `nationId`, `eraIndex`, `mapGeneratorVersion`; usa un generador determinista, sin consultar hora local ni `Math.random()`.

## Orden de construcción del mapa

1. Reservar núcleo cívico común y acceso de caminos. 2. Establecer zonas naturales garantizadas para las cinco profesiones, incluso en caso de bioma adverso. 3. Colocar masas de decoración sin bloquear futuras parcelas esenciales. 4. Crear pasillos que conecten fuentes y asentamiento. 5. Reservar parcelas para edificios básicos obligatorios y huellas máximas. 6. Colocar variaciones estéticas de facción por seed. 7. Ordenar candidatos de parcela por distancia a núcleo, compatibilidad de huella, accesibilidad y coordenadas (desempate lexical); nunca hacer depender resultado de una animación. 8. Al pasar de era, expandir anillos y conservar edificios antiguos con su dirección y estado.

## Proyección y render

Proyección oblicua con relación 2:1: el eje del suelo es rombo 32×16, y la altura de objeto se añade al eje visual vertical, no al costo lógico. El orden de dibujo depende de profundidad lógica y anclaje de suelo, con desempate por ID para evitar flicker. Los sprites caminan por rutas entre puntos de interés; la posición visual es interpolada y puede diferir del «trabajador lógico» sin afectar su tasa de producción. Un ciudadano cuya ruta gráfica se bloquea se teletransporta tras una ventana cosmética segura; no pierde economía por problemas de colisión gráfica.

## Edificios y parcelas saturadas

En caso de no existir parcela actual, mostrar `WAITING_PLOT` y buscar el siguiente sector expandible; no descontar recursos antes de reservar obra y ubicación atómicas. Nunca colocar un objeto en fuente natural obligatoria que impida generación mínima. Los edificios anteriores se preservan (sin destrucción por transición); las nuevas eras aumentan densidad hasta el máximo territorial. Política de fallback visual: skyline/centro de obra representado en panel lateral si no queda parcela factible, con advertencia de operador; **no** fingir obra completada.

## Densidad y LOD

Máximo sugerido 45 ciudadanos visibles en vertical y 90 en horizontal; prioridad persona propia si verificable, participantes recientes, premiados y muestra semillada. El resto se agrega en contadores. Dos salidas render pueden mostrar diferentes sprites sin modificar la misma nación en backend. La expresión «10.000 habitantes» no implica 10.000 entidades de animación/IA de cliente.

## Pruebas mínimas del diseño

Misma seed+versión produce mismas parcelas, aunque se cambie hardware, FPS, resolución o plataforma. Distintas seeds pueden variar decoración, nunca permisos económicos. Zona natural inicial no queda oculta por infraestructura. Al llegar al máximo 256×256 se emite alerta con estrategia de fallback no destructiva. Ninguna transición invalida la ruta de ciudad al sector cívico. Estos son **criterios** de prueba, no una generación de mapa realizada en esta revisión.
