> **Documento de detalle.** La fuente normativa vigente es [ESPECIFICACION_MAESTRA.md](../ESPECIFICACION_MAESTRA.md). Este capítulo no prevalece ante una regla corregida en la especificación; versiones anteriores en Git.

# 12 — Diseño visual y producción de assets

## Dirección artística cerrada
Pixel art retro de baja resolución, tiles de 32×16 proyección oblicua 2:1, personaje de 16×24 píxeles, contorno de 1 px, hasta 24 colores por spritesheet, sin filtrado bilineal. Micelios: fungoides vivos y tecnología biofotónica. Rúnicos: cuerpos minerales con runas. Ferrinos: seres orgánicos con exoesqueleto ferruginoso, **no** robots ni corales. Siluetas deben diferenciarse claramente a 360×640 canvas lógico vertical. Para cada era la misma funcionalidad y collider en todas las naciones; solo cambian apariencia y FX.

## Sprite contract
Cada combinación `(faction, era, profession)` tiene direcciones `NE,SE,SW,NW`; acciones `idle,walk,gather,haul,build,research,celebrate,rest,react`; frames por acción, fps y naming en `data/art_spec.v2.json`. Las 13 eras x 5 profesiones x 3 facciones requieren 195 combinaciones de vestuario profesional, con reutilización de esqueletos, paletas y herramientas. 39 combinaciones de K-0 **no** son necesarias: cuerpo único más accesorios y proyecciones de época. Gobiernos: 3 candidatos x 3 facciones x 13 épocas = 117 variantes de vestuario, generadas a partir de 9 bases. Edificios básicos: 130 definiciones x 3 facciones = 390 skins con reutilización de las 10 familias y cuatro etapas.

## Cámara y HUD
Resolución lógica vertical 360×640, salida 1080×1920. Horizontal 640×360, salida 1920×1080. `nearestNeighbor=true`, objetivo 30 FPS y nunca inferir latencia del servidor desde FPS. Vertical: 14 % HUD superior, 66 % mundo, 20 % inferior; horizontal: 73 % mundo y 27 % panel lateral. HUD siempre muestra era, barra 0–100, próximos hitos, recursos esenciales, estado LIVE por nación, cuenta regresiva de votación, total de papeletas pero no opciones ocultas de RPS, y eventos de K-0 subtitulados. No mezclar identidad de canales de otras plataformas salvo política aprobada.

## Densidad de población
Vertical render objetivo máximo 45 ciudadanos, horizontal 90, LOD por FPS con prioridad `(self_if_known, recentlyActive, recentlyJoined, awarded, seededSample)`. El resto no desaparecen del sistema: se muestran agregados por oficio y sprites cosméticos NPC. No hay sprite real por ciudadano obligatoriamente; las animaciones extrapolan eventos de servidor y no alteran el estado real.

## Matriz de acceptance visual
Cada asset necesita archivo PNG con transparencia, spritesheet, JSON atlas, origen/sombra estándar, paleta, silueta comprobada en 360×640/640×360, cuatro orientaciones, 9 acciones, licencias verificadas y aprobación visual. **Estos archivos no están dibujados por esta especificación**. El diseño visual puede estar definido en texto; su calidad final y la aceptación artística no son un hecho hasta existir imágenes reales.
