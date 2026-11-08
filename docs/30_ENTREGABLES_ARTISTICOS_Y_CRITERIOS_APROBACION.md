# 30 — Lista de entregables de arte, animación, mapa y audio

**Criterio de aceptación obligatorio del primer piloto:** arte de **las doce eras jugables completas para las tres facciones**, todas las variantes requeridas para personajes/edificios/combate y el **epílogo terminal Interestelar**; composición vertical/horizontal en español. No se reduce a una demo de una era. La reutilización de componentes es válida, pero cada era jugable debe tener assets verificables y licencias comerciales.

**Estado:** encargo artístico completo en intención; no se entregan sprites, voces ni música. El arte es un producto futuro y debe pasar revisión humana antes de considerarse aprobado.

## Matriz de sprites requerida

- **Ciudadanos:** 3 facciones × 13 eras × 5 profesiones = 195 combinaciones visuales; 4 orientaciones por combinación. Las herramientas evolucionan según profesión y época sin alterar colisiones.
- **Animaciones de ciudadano:** 9 acciones (`idle`, `walk`, `gather`, `haul`, `build`, `research`, `celebrate`, `rest`, `react`) con número de cuadros y FPS fijado en `art_spec.json`.
- **Gobernantes:** 9 personajes base recurrentes (3 orientaciones por facción) con 13 variaciones de vestuario = 117 diseños de apariencia; reutilizar rigs y siluetas.
- **Edificios básicos:** 130 definiciones × 3 facciones = 390 skins de edificios, con cuatro etapas de construcción (umbrales oficiales).
- **Proyectos estratégicos:** 39 × 3 facciones = 117 skins si una pieza global requiere variante local; revisar la política de unicidad antes de producción.
- **Maravillas:** 13 × 3 facciones = 39 variantes visuales concebidas; la adjudicación lógica puede limitar su construcción efectiva.
- **Doctor K-0:** retrato grande HUD, sprite de mundo, estados emocionales básicos, gestos y accesorios por época; se evita producir 39 personajes completamente distintos.

## Elementos de escenario

Para cada facción: suelo base, transición de bioma, tres tipos de vegetación/roca decorativa por era visual cuando proceda, caminos, zonas de recurso natural, sombras consistentes, señales de almacén, aldeanos NPC, partículas de trabajo discretas, banderas/estandartes y efectos de hito. La selección estética no modifica el rendimiento de las parcelas o biomas.

## Ficha obligatoria por asset

| Campo | Requisito |
|---|---|
| ID estable | Coincide con el identificador del catálogo o es su variante cosmética |
| Clase | Personaje, edificio, entorno, UI, VFX, retrato, icono, audio |
| Facción/era | Precisamente una combinación o declaración de reutilización |
| Resolución | Múltiplo de las unidades lógicas acordadas |
| Pivote/anclaje | Referenciado al mismo suelo/centro entre facciones |
| Huella lógica | La del objeto del catálogo; no depende del dibujo |
| Frame list | Acciones y orientaciones aprobadas |
| Paleta | Colores y contraste de silueta definidos |
| Derechos | Propiedad o licencia de uso comercial verificable |
| Revisión | Aceptado/pendiente/rechazado y motivo |

## Criterios de aceptación por fase

**Fase de concepto:** tres fichas de facción y K-0 diferenciables sin etiquetas. **Fase de muestras:** un personaje por oficio, cuatro direcciones y una animación representativa. **Fase de época:** prueba visual de Paleolítico, Edad Media y Espacial para todas las facciones. **Fase de juego:** matriz completa, cámara vertical y horizontal, escenas con veinte sprites y con LOD alto. **Fase de emisión:** capturas OBS reales, subtítulos y partículas bajo carga. Ninguna fase se marca como entregada solo porque exista este documento.

## Limitación de alcance

La cifra de skins es una cobertura conceptual, **no** una promesa de 700 archivos únicos: los spritesheets pueden reutilizar capas, paletas y herramientas. La autoridad está en el efecto de juego; los assets deben ser intercambiables sin migrar el estado persistente.

## Ampliación v2.2: ejército y 13 maravillas individualizadas

El catálogo de combate requiere **39 formas rol/era × 3 culturas = 117 skins** adicionales, con tres siluetas de rol definidas y reutilización de rig. Las trece maravillas tienen nombres propios y motivos visuales exclusivos en `docs/61_CATALOGO_ARTISTICO_DE_EDIFICIOS_Y_MARAVILLAS.md`. No se cuentan como PNG entregados o aprobados.
