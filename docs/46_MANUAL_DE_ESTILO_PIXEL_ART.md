# 46 — Manual de estilo visual y control de consistencia

**Estado: contrato de diseño pixel art, no assets aprobados.** Define restricciones reproductibles para artistas y futuras herramientas. No debe copiar sprites, paletas ni animaciones ajenas; Terraria es referencia de densidad/lectura, no un catálogo reutilizable.

## Gramática de pixel art

- Proyección de terreno oblicua **2:1**; tile romboidal de **32 × 16 píxeles lógicos**. Personas: frame base **16 × 24**, cuatro direcciones NE/SE/SW/NW. Sin rotación libre de sprites, bilinear, anti-aliasing ni escalas fraccionarias en escenas pixel-perfect. Bordes de 1 píxel, sombras de suelo separadas, hasta 24 colores por spritesheet de personaje.
- Escala vertical lógica **360 × 640** a 1080 × 1920; horizontal **640 × 360** a 1920 × 1080; `nearest-neighbor`; 30 FPS objetivo. El arte nunca contiene texto integrado que deba localizarse; rotulaciones en UI.
- Luz principal común desde arriba-izquierda (dirección proyectada NW); sombras de contacto de 1–2 píxeles con alfa discreta. Sombras de edificios no pueden ocultar la celda de acceso ni texto. No utilizar partículas permanentes encima de votaciones.
- El pixel no es una limitación estética opcional: curvas y contornos deben seguir escalones limpios de 1/2/3 píxeles, sin texturas ruidosas subpíxel. La claridad de forma prevalece sobre detalle ornamental.

## Paleta y códigos cromáticos

| Facción | Color ancla | Contorno | Relación de formas | Material primario |
|---|---|---|---|---|
| Micelios | `#6FAD78` | `#20262C` | Cúpulas y tallos orgánicos | Fibras, esporas, micelio iluminado |
| Rúnicos | `#769BCB` | `#20262C` | Prisma, plano quebrado y monolito | Mineral segmentado y runa |
| Ferrinos | `#C17B59` | `#20262C` | Articulaciones, triángulos y placas | Exoesqueleto bioférreo, no robot |

Colores ancla ya fijados en el catálogo. Las sombras, medios tonos y acentos secundarios deben derivarse de una **paleta maestra de 24 posiciones** aprobada visualmente; **no se inventa aquí una paleta final de 24 colores sin ver cómo funciona sobre sprites reales**. El éxito se juzga en monocromo y a resolución de salida, no solo por su hexadecimal.

## Siluetas y lectura

**Micelio:** capuchón grande e identificable a 1×, torso blando, dos miembros cortos, bioluminiscencia en articulaciones, sin tentáculos marinos ni coral. **Rúnico:** cabeza prismática, torso denso, 2 hombros escalonados; líneas rúnicas se leen como acento, no como láser. **Ferrino:** cabeza trapezoidal con visor orgánico, cintura estrecha, placas de oxidación; no usar cascos militares humanos. **Doctor K-0:** científico cyborg de silueta asimétrica, un ojo óptico, mandíbula segmentada, brazo parcialmente industrial, bata o insignia de laboratorio corta; nunca una mascota alienígena blanda.

## Módulos visuales repetibles

Los 130 edificios mantienen 10 familias reconocibles (vivienda, alimentación, biomasa, extracción, taller, saber, almacén, infraestructura, cívico, defensa) y 13 épocas. El artista crea una **forma base por familia y facción**; el cambio de época añade materiales/tecnología visibles (ver capítulo 26) sin reescribir todas las siluetas. Cada obra tiene cuatro etapas: cimientos (15 %), estructura (40 %), obras (70 %), final (100 %); fase 4 no se representa antes del commit económico. Todas las parcelas respetan `footprintTiles` y su pivote.

## Especificación de animación

Frames y FPS exactos en `data/art_spec.json`: idle 4@4FPS, walk 6@8, gather 5@6, haul 6@8, build 5@6, research 5@6, celebrate 5@6, rest 2@1, react 4@6. Animación de trabajo visible siempre es derivada del estado lógico, sin añadir output económico. Cuatro direcciones en todas las acciones. Evitar clonación robótica: variación cosmética por fase/semilla, sin mover hitbox ni alterar tick.

## Criterios de aceptación de arte

1. Identificar facción y profesión en cinco segundos con sprite a 1× sin etiqueta. 2. La miniatura de una obra se distingue de las otras nueve familias. 3. En escenario vertical con 45 ciudadanos, 90 % de observadores de prueba reconocen el evento principal. 4. Nadie confunde datos de nación por el color exclusivamente. 5. Se prueba contraste en desaturado y diferentes fondos. 6. No hay uso de imágenes, fuentes, músicas o personajes de terceros sin licencia comercial verificable. 7. Anclas, huellas, animaciones y exportación son consistentes en atlas para las tres facciones.

La palabra **FINAL** se reserva a sprites/aprobaciones reales. Este documento especifica un estilo; no acredita todavía la producción artística.
