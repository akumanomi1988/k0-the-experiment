> **Documento de detalle.** La fuente normativa vigente es [ESPECIFICACION_MAESTRA.md](../ESPECIFICACION_MAESTRA.md). Este capítulo no prevalece ante una regla corregida en la especificación; versiones anteriores en Git.

# 26 — Biblia visual: legibilidad, tres culturas y 13 eras

**Estado:** especificación conceptual cerrada para orientar la producción artística; no implica que los assets estén dibujados o aprobados. Fuentes cuantitativas: `data/art_spec.v2.json`, `data/factions.v2.json` y `docs/12`.

## Gramática gráfica común

Pixel art de baja resolución, proyección oblicua 2:1, tiles 32 × 16, personaje de referencia 16 × 24, bordes de 1 píxel y hasta 24 colores por spritesheet. Se prohíben suavizado de píxel, contornos de grosor variable no justificados por escala y escenas con modelos 3D disfrazados de pixel art. Misma huella y anclajes por rol equivalente entre facciones.

La prioridad de legibilidad es: (1) silueta de facción, (2) animación de trabajo, (3) herramienta/oficio, (4) nivel de época, (5) identidad de jugador; ningún detalle cosmético puede hacer imposible identificar el trabajo a resolución vertical.

## Lenguaje de siluetas

| Facción | Silueta primaria | Volumen secundario | Motivo arquitectónico | Lo que hay que evitar |
|---|---|---|---|---|
| Micelios | Capuchón orgánico dominante, piernas cortas | Esporas discretas y fibras | Cúpulas de raíces, bóvedas de micelio | Coral, tentáculos marinos, aspecto gelatinoso indistinto |
| Rúnicos | Cabeza y torso poliédricos, hombros quebrados | Grietas/líneas luminosas | Monolitos, paneles facetados, resonadores | Humanos con armadura, magia con ventaja funcional |
| Ferrinos | Exoesqueleto articulado, cabeza compacta, placas | Bisagras, crestas y remaches | Arcos metálicos, forjas, nervios estructurales | Robots puros, coral metálico, soldados humanos genéricos |

La paleta propia puede intensificarse de era en era, pero el contorno y la silueta permanecen reconocibles. Las tres naciones comparten indicadores de estado y sistema de cámara para que no haya ventaja perceptiva.

## Evolución visual por época

| Era | Entorno y materiales | Micelios | Rúnicos | Ferrinos |
|---|---|---|---|---|
| Paleolítico | Refugios, útiles pétreos, fuego | Capuchones naturales y cabañas de fibras | Rocas talladas, monolitos primarios | Placas naturales y fogones minerales |
| Neolítico | Aldeas, parcelas, estructuras permanentes | Invernaderos fúngicos elementales | Terrazas geométricas y depósitos pétreos | Talleres de barro ferruginoso y empalizadas |
| Cobre | Metalurgia inicial | Esporas guiadas en moldes metálicos | Grabados conductores sobre mineral | Forjas cortas y remaches sencillos |
| Bronce | Fundiciones y organización gremial | Arcos fibrometálicos | Pórticos de piedra y bronce | Corazas ornamentales, talleres estructurados |
| Hierro | Hornos mayores, fortificación | Raíces reforzadas y herramientas ferrosas | Talladores de precisión con anillos | Placas de hierro y chimeneas compactas |
| Antigüedad | Monumentos y espacios cívicos | Cúpulas vivas y plazas radiales | Columnatas prismáticas y bibliotecas | Ágoras mecánicas y acueductos de placas |
| Edad Media | Gremios y ciudades densas | Torres de micelio y talleres de esporas | Castillos facetados y archivos rúnicos | Fortines, puentes y bastiones remachados |
| Renacimiento | Instrumentos, cartografía y academia | Observatorios bioluminiscentes | Óptica de cristal y geométrica | Instrumentos articulados y cúpulas de ingeniería |
| Industrial | Máquinas, logística y producción | Conductos de biomasa y calderas orgánicas | Motores cristalinos y redes de energía | Prensas, raíles y forjas mayores |
| Moderna | Electricidad, laboratorios, logística | Biopaneles y módulos de investigación | Paneles de información y cristales | Sistemas electromecánicos y edificios modulares |
| Digital | Redes, automatización, señalética | Circuitos bioluminiscentes | Nodos de datos tallados y holografía discreta | Microactuadores y redes de control |
| Espacial | Hábitats orbitales y lanzadores | Cápsulas bioherméticas | Estaciones cristalinas presurizadas | Módulos orbitables y trajes de exoesqueleto |
| Interestelar | Símbolo de logro y epílogo | Jardines de fotones estelares | Arcos rúnicos de navegación | Estructuras ferruginosas de tránsito estelar |

## Iluminación y composición

La lectura del avatar no depende solo de color: se refuerza con forma y animación. El equipo de arte define un contraste mínimo de personaje/fondo por fase de emisión y verifica manualmente HUD en 360 × 640 y 640 × 360. Se evita saturar pantalla con partículas cuando hay votación, lectura de subtítulos o cierre de temporada. Una celebración de fase no puede tapar el recuento ni el nombre del ganador.

## Aprobación

El documento fija el encargo artístico, **no entrega imágenes finales**. Las decisiones que necesitan aprobación visual posterior están registradas como evidencia de arte, no como fallos de diseño: retrato K-0, sprites base de cada facción, vestuario de cinco profesiones y muestra de edificios en tres épocas (temprana/media/futura). Hasta entonces el estado de los assets es `DESCRITO_NO_PRODUCIDO`.
