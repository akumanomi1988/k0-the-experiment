# Fuentes íntegras v2.5 — capítulos 25–32

> **Anexo de preservación literal** para cobertura integral. Los textos se mantienen íntegros, incluyendo decisiones históricas superadas. [Norma v2.5](../ESPECIFICACION_MAESTRA_v2.5.md) resuelve sus conflictos; este anexo no los reactiva.

---

## Fuente 25 — `docs/25_BIBLIA_NARRATIVA_UNIVERSO_Y_PERSONAJES.md`

**Blob original:** `ff747f83ac77f91b4dc0eac2abd4f33cdbd85e89`.

## 25 — Biblia narrativa del experimento

**Estado:** dirección narrativa editorial v2.1. Expande la presentación sin introducir mecánicas nuevas. El tono es ciencia ficción cómica, no simulación de historia humana literal. Las 13 eras representan analogías de avance tecnológico para especies propias.

### Premisa

Project CHAOS es un experimento competitivo televisado sobre tres civilizaciones inteligentes que comienzan con recursos y tecnologías elementales. La pregunta dramática es qué comunidad aprende antes a dominar su entorno y alcanzar el horizonte interestelar. El espectáculo lo presenta Doctor K-0, investigador cyborg obsesionado con registrar resultados, sorpresas y comportamientos emergentes. Nunca se usa la narración para falsear los números de la partida.

### Doce reglas de continuidad de ficción

1. Las tres naciones son especies inteligentes, nunca versiones humanas con orejas postizas.
2. No comparten un ejército, una economía ni un gobierno; no se trasladan recursos entre naciones.
3. La competencia es científica, cultural y económica; puede haber torneos, pero no agresiones persistentes no definidas.
4. Ninguna facción nace con ventaja real, ni por especie ni por bioma. Las diferencias son visuales, arquitectónicas y lingüísticas.
5. Las épocas son equivalentes funcionales entre facciones; una era espacial micélica no tiene por qué parecer ingeniería humana contemporánea.
6. Los ciudadanos participantes son miembros de la sociedad, no monederos o clientes de Doctor K-0.
7. Los NPC son ciudadanos de pleno derecho para la simulación, pero nunca inventan votos de espectadores ni generan oro.
8. Los gobiernos son NPC recurrentes con tres orientaciones pasivas; ningún gobernante ejerce autoridad absoluta.
9. Una pérdida en torneo provoca penalizaciones acotadas, no exterminio, esclavitud o desaparición de jugadores.
10. La falta de público no detiene el mundo; la civilización continúa a menor ritmo con sus NPC.
11. El avance interestelar culmina la temporada y abre una ceremonia, no un nivel de combate infinito.
12. Doctor K-0 puede opinar, celebrar o bromear, pero no altera resultados, tasas, votos o el oro.

### Micelios

Criaturas fungoides terrestres, anatomía compacta y silueta con capuchón esporado. Su cultura considera el territorio una red de colaboración y transformación. Arquitectura de fibras, raíces, membranas y biofotones. No son corales ni un pueblo submarino; no obtienen ventajas de producción agrícola sobre las demás. El léxico editorial gira en torno a «red», «brotes», «tejidos», «cultivo» y «simbiosis», sin sugerir que son una mente colmena que invalida a los ciudadanos individuales.

### Rúnicos

Seres minerales inteligentes de cuerpos geométricos, grietas luminosas y marcas rúnicas. Su arquitectura evoluciona desde menhires y talleres pétreos hasta complejos cristalinos y computación de patrones. La estética no debe convertir sus runas en magia que conceda poderes inexistentes: «runa» designa su lenguaje visual de conocimiento y memoria. Su léxico incluye «grabado», «resonancia», «estrato», «archivo» y «forma».

### Ferrinos

Criaturas biológicas recubiertas por exoesqueletos ferruginosos con articulaciones expresivas, no robots ni corales. Sus ciudades muestran remaches, pliegues, forjas y, en eras avanzadas, superficies orgánicas metalizadas. El metal es identidad visual, no un multiplicador minero oculto. Léxico recomendado: «forja», «coraza», «horno», «articulación», «alianza».

### Doctor K-0

Es el hilo conductor del espectáculo: científico cyborg con elementos mecánicos inequívocos en cabeza, rostro y extremidades, silueta reconocible como sprite de baja resolución y retrato HUD. Personalidad irónica y teatral, pero siempre imparcial. No ridiculiza a una persona identificable, no expone pagos ni datos sensibles y no sugiere gasto como obligación para competir. Sus frases se generan o seleccionan a partir de hechos autorizados, siempre con versión subtitulada. La improvisación narrativa no forma parte del estado autoritativo.

### Arco por temporada

**Apertura:** presentación de las tres naciones y reglas. **Desarrollo:** oficios, primeras construcciones, retos y evolución estética. **Tensión:** elecciones, hitos próximos, torneos y posibilidades de remontada. **Clímax:** una nación entra en Era Interestelar. **Epílogo:** comparación, ceremonia de prestigio, museo de temporada y reinicio limpio de economía. No hay traspaso de oro o ventajas competitivas entre temporadas.

### Límites editoriales

Evitar referencias textuales o gráficas a franquicias externas, símbolos religiosos reales usados como facción, propaganda, humillación de donantes, lenguaje discriminatorio y afirmaciones de patrocinio no autorizado. Toda escena narrativa ha de poder emitirse con audio desactivado y subtítulos visibles.


---

## Fuente 26 — `docs/26_BIBLIA_VISUAL_FACCIONES_EPOCAS_Y_SILUETAS.md`

**Blob original:** `0db816589c85d7dc24c2eba5ccab62beb7f32e57`.

## 26 — Biblia visual: legibilidad, tres culturas y 13 eras

**Estado:** especificación conceptual cerrada para orientar la producción artística; no implica que los assets estén dibujados o aprobados. Fuentes cuantitativas: `data/art_spec.v2.json`, `data/factions.v2.json` y `docs/12`.

### Gramática gráfica común

Pixel art de baja resolución, proyección oblicua 2:1, tiles 32 × 16, personaje de referencia 16 × 24, bordes de 1 píxel y hasta 24 colores por spritesheet. Se prohíben suavizado de píxel, contornos de grosor variable no justificados por escala y escenas con modelos 3D disfrazados de pixel art. Misma huella y anclajes por rol equivalente entre facciones.

La prioridad de legibilidad es: (1) silueta de facción, (2) animación de trabajo, (3) herramienta/oficio, (4) nivel de época, (5) identidad de jugador; ningún detalle cosmético puede hacer imposible identificar el trabajo a resolución vertical.

### Lenguaje de siluetas

| Facción | Silueta primaria | Volumen secundario | Motivo arquitectónico | Lo que hay que evitar |
|---|---|---|---|---|
| Micelios | Capuchón orgánico dominante, piernas cortas | Esporas discretas y fibras | Cúpulas de raíces, bóvedas de micelio | Coral, tentáculos marinos, aspecto gelatinoso indistinto |
| Rúnicos | Cabeza y torso poliédricos, hombros quebrados | Grietas/líneas luminosas | Monolitos, paneles facetados, resonadores | Humanos con armadura, magia con ventaja funcional |
| Ferrinos | Exoesqueleto articulado, cabeza compacta, placas | Bisagras, crestas y remaches | Arcos metálicos, forjas, nervios estructurales | Robots puros, coral metálico, soldados humanos genéricos |

La paleta propia puede intensificarse de era en era, pero el contorno y la silueta permanecen reconocibles. Las tres naciones comparten indicadores de estado y sistema de cámara para que no haya ventaja perceptiva.

### Evolución visual por época

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

### Iluminación y composición

La lectura del avatar no depende solo de color: se refuerza con forma y animación. El equipo de arte define un contraste mínimo de personaje/fondo por fase de emisión y verifica manualmente HUD en 360 × 640 y 640 × 360. Se evita saturar pantalla con partículas cuando hay votación, lectura de subtítulos o cierre de temporada. Una celebración de fase no puede tapar el recuento ni el nombre del ganador.

### Aprobación

El documento fija el encargo artístico, **no entrega imágenes finales**. Las decisiones que necesitan aprobación visual posterior están registradas como evidencia de arte, no como fallos de diseño: retrato K-0, sprites base de cada facción, vestuario de cinco profesiones y muestra de edificios en tres épocas (temprana/media/futura). Hasta entonces el estado de los assets es `DESCRITO_NO_PRODUCIDO`.


---

## Fuente 27 — `docs/27_ESCENAS_PANTALLAS_Y_SECUENCIAS_PUBLICAS.md`

**Blob original:** `e580400112a14dfd3899c00e4469234903390400`.

## 27 — Especificación de escenas, pantallas y estados visibles

**Objetivo:** definir qué se debe ver en cada momento sin entregar componentes React, escenas Phaser ni archivos OBS. Las dimensiones son lógicas y se escalan con píxel más próximo.

### Matriz de escenas públicas

| Escena | Cuándo aparece | Elementos obligatorios | Información prohibida/oculta | Fin de escena |
|---|---|---|---|---|
| Visión general | Inicio de emisión, entre segmentos | Tres naciones, sus eras, historial del torneo, estados LIVE | Chat crudo de otro proveedor sin permiso | Selección editorial de nación |
| Nación vertical | Emisión principal 9:16 | Mundo, era, barra, oficios, recursos, narración subtitulada | Datos financieros personales | Cambio de segmento |
| Nación horizontal | Emisión 16:9 | Mundo, panel lateral y el mismo estado autoritativo | Reglas diferentes por layout | Cambio de segmento |
| Elección NPC | Ventana electoral LIVE | Tres candidatos, orientación, tiempo restante, información electoral permitida | Votos atribuidos erróneamente | Resultado confirmado |
| Prioridad | Tras elección, ventana de prioridad | Opciones de prioridad, tiempo y explicación de bonus | Suposiciones de bono permanente | Publicación del resultado |
| Consejo | Tres alternativas financiables | Coste por recurso, naturaleza opcional, 10 minutos LIVE | Proyectos no elegibles | Cobro atómico y obra seleccionada |
| Torneo RPS | Evento programado con tres LIVE | Equipos, ronda, tiempo, votos totales, puntuación por parejas | Opciones RPS antes del cierre | Resolución y penalizaciones |
| Ceremonia de era | La nación alcanzó 100 puntos y está LIVE | Era saliente/entrante, cambios estéticos, progreso | Transición simulada fuera de LIVE | Era confirmada |
| Final de temporada | Primera entrada en Interestelar | Ganador, secuencia final, resumen, museo | Transferencia de oro o recursos | Archivado |
| Escena segura | Fallo grave, moderación o suspensión | Marca del juego, pausa explicada, enlace/help si procede | Mundo congelado como si produjera | Reanudación supervisada |

### HUD vertical 360 × 640

Reserva conceptual del documento fuente: 14 % superior (aprox. 90 píxeles lógicos), 66 % mundo (aprox. 422) y 20 % inferior (aprox. 128). Esto es una distribución de espacio, no coordenadas definitivas de sprites. El área superior nunca debe esconder la barra histórica; el área inferior prioriza comandos, votaciones y subtítulos; los eventos emergentes se apilan y caducan para no bloquear el centro.

**Jerarquía de información estable:** identidad de nación → era y barra → evento con tiempo límite → recursos relevantes → ciudadanos activos por oficio → narración/efectos. No mostrar simultáneamente barras de progreso contradictorias o mensajes que parezcan atribuir un chat a otra nación.

### HUD horizontal 640 × 360

Aproximadamente 73 % del ancho para el mundo y 27 % para panel lateral; mantiene las mismas métricas y estados, reorganizados. No se cambian reglas por proporción. La cámara puede mostrar más ciudadanos (objetivo 90 frente a 45), pero ambos visores consumen el mismo snapshot.

### Estados universales que todo componente debe representar

`LOADING`, `LIVE_CONFIRMED`, `OFFLINE_CONFIRMED`, `UNCERTAIN`, `PAUSED`, `DISCONNECTED`, `RECOVERING`, `DEGRADED`, `COMPLETED`. El operador tiene diagnóstico adicional; un espectador recibe mensajes comprensibles. Cada componente con un reloj distingue explícitamente **tiempo de directo** y **tiempo real**: nunca etiquetar «10 minutos» como tiempo UTC si una votación está pausada.

### Secuencias de interacción

**Al crear ciudadano:** pulso de llegada → confirmación de oficio pendiente → estado de actividad. **Al terminar edificio:** mejora visible de obra en etapas ya especificadas → evento de completado → icono de capacidad añadida. **Al entrar en era:** transición histórica sin borrado de recursos → cambio de paleta/estructuras → retomada de estado. **Al terminar temporada:** detener decisiones competitivas → animación final → museo → estado de campaña preparada para siguiente temporada.

### Reglas de accesibilidad visual

El color nunca es el único indicador; cada progreso tiene texto y forma. Las pistas sonoras tienen subtítulos equivalentes. Los controles de operador disponen de foco, labels y confirmaciones. Para personas sensibles al movimiento, priorizar reducción de destellos y cámara estable durante anuncios importantes.


---

## Fuente 28 — `docs/28_NARRACION_K0_Y_DIRECCION_DEL_ESPECTACULO.md`

**Blob original:** `de97cd06e46224919b7e6460e6ba029326fbc778`.

## 28 — Libro de estilo y protocolo narrativo de Doctor K-0

**Estado:** especificación editorial. K-0 es narrador y agente de presentación; **no** autoriza comandos de dominio.

### Carácter fijo

Doctor K-0 es un científico cyborg reconocible, teatral, irónico y observador. No es villano, árbitro encubierto ni gestor de las aportaciones. Puede expresar sorpresa ante victorias inesperadas, burlarse suavemente de la complejidad de sus propias hipótesis y celebrar hitos de cualquier nación con el mismo entusiasmo base. Su neutralidad es requisito del espectáculo.

### Jerarquía de situaciones narrables

| Prioridad | Evento | Propósito | Contenido mínimo |
|---:|---|---|---|
| 1 | Incidente de seguridad o emisión | Evitar información engañosa | Estado, qué se pausa y qué continúa |
| 2 | Ganador de temporada | Cierre de carrera | Nación ganadora, era, hito y carácter definitivo |
| 3 | Resultado torneo | Claridad competitiva | Ganadores, puntos y sanciones vigentes |
| 4 | Transición histórica | Sentido de avance | Nueva era, significado y elementos visibles |
| 5 | Cierre de elección o Consejo | Transparencia de voto | Opción ganadora, costes y efectos autorizados |
| 6 | Edificio/tecnología completados | Señal de progreso | Nombre y efecto concreto |
| 7 | Reacciones ambientales | Variedad de emisión | Narración libre sin afirmaciones factuales inventadas |

Si dos eventos compiten por el mismo espacio, se encola o resume el de prioridad inferior. Nunca ocultar un aviso de pausa por una broma. El texto de pantalla refleja el evento persistido, no predicciones del LLM.

### Estructura de una intervención

**Entrada:** tipo de evento, nación, era, efectos autorizados, métricas agregadas y contexto visible. **Composición:** frase introductoria + hecho verificable + comentario breve opcional + cierre/llamada a participación si existe una acción válida. **Salida:** texto revisado/sanitizado, identificador de evento, duración estimada, subtítulos y pista de audio opcional. Evitar referencias a identidad personal o monto individual de una aportación.

**Ejemplo de tono, no texto fijo obligatorio:** «Registro del experimento: los Rúnicos han alcanzado una nueva era. Mis modelos ya están solicitando vacaciones». La narración de un resultado se ajusta a su estado y no concede bonus por el mero acto de pronunciarlo.

### Restricciones estrictas

No inventar resultados, victorias, gobiernos, tasas o datos de donación; no mostrar nombres ofensivos; no hacer afirmaciones médicas/financieras; no introducir instrucciones de gasto compulsivo; no producir logos ajenos sin derechos; no narrar mensajes externos en un overlay donde la política de plataforma lo prohíba. Un fallo de LLM/TTS se resuelve con plantilla determinista y subtítulos, sin detener la simulación.

### Catálogo editorial mínimo

Diseñar variantes de frase para: inicio de temporada, bienvenida por nación, nuevo ciudadano, profesión seleccionada, subida de nivel, habilidad disponible, saturación de almacén, escasez de comida, construcción iniciada y completada, elecciones abiertas y resueltas, Consejo retrasado por recursos, voto cerrado, torneo anunciado, ronda RPS resuelta, sanción territorial y expiración, misión diaria/semana completada, era preparada offline, era avanzada, maravilla reclamada, señal LIVE incierta, pausa de operador, reconexión, ganador y créditos. Cada variante posee gravedad, prioridad, longitud, idioma, subtítulo y caducidad de presentación.

### Sonido y subtítulos

La voz puede ser sintetizada o pregrabada; se debe conservar texto de subtítulo como fuente principal de accesibilidad. Los efectos críticos (voto, fin de era, error, torneo) requieren alternativa visual. Estilo sonoro: sintetizadores retro discretos, percusión suave, señales diferenciadas por facción sin convertir sonidos en ventajas competitivas. Las librerías musicales quedan fuera del alcance hasta verificar licencias.


---

## Fuente 29 — `docs/29_ESTADOS_EXTREMOS_Y_FALLOS_EN_DIRECTO.md`

**Blob original:** `a6e852eb21efcedfe271bcf45798c2504e2b4c75`.

## 29 — Matriz de casos límite y degradación funcional

**Propósito:** especificar qué debe ocurrir cuando el mundo no está en las condiciones ideales; el diseño debe seguir siendo coherente con ausencia de público, sin oro y con proveedores intermitentes.

| Incidente | Continúa | Se congela | Acción del operador / audiencia |
|---|---|---|---|
| Ningún espectador en las tres cuentas | NPC y economía; era lista puede prepararse | Votos humanos no se inventan | Ninguna acción exigida |
| Una nación no emite | Economía offline de esa nación | Su LiveClock, elección/Consejo y penalización activa | Reanudar al confirmar LIVE |
| Las tres naciones no emiten | Economía offline segmentada | Torneos; avance de era; votos | Esperar a DIRECTO confirmado |
| Un canal secundario desconectado | Fuentes restantes y autoridad de reloj original | Solo capacidad de ese canal | Reparar binding, sin reatribuir eventos |
| Estado LIVE `UNCERTAIN` | Economía degradada/offline | Votaciones y sanción territorial | Confirmar fuente; auditar transición |
| Ingesta de chat duplicada | Ninguna doble acción | Nada adicional | Deduplicación automática |
| Ingesta retrasada tras cerrar votación | Estado general de nación | Valor de la papeleta fuera de plazo | Rechazo auditable; mensaje neutro |
| Almacenes llenos | Consumo, investigación con capacidad, eventos admisibles | Producción que sobrepasa capacidad | Incentivar inversión de recursos ordinarios |
| Comida insuficiente | Progreso a rendimiento reducido previsto | No se elimina ciudadanía | HUD de escasez, recuperación económica |
| No existen tres proyectos estratégicos costeables | Economía, edificios básicos y eras | Convocatoria de Consejo | Mostrar aplazamiento, nunca forzar donación |
| Torneo sin papeletas | Ronda con PASS donde corresponda | Nunca inventar votos de NPC | Mostrar resultado según reglas |
| Tres opciones cíclicas RPS | Puntuación por parejas 2-1-0 | No inventar ganador de ronda | Continuar calendario |
| Empate final de torneo tras extras | Reconocimiento compartido | Penalizaciones | Mostrar empate justo |
| Cierre simultáneo de eventos globales | Secuencia serializada global | Recompensa doble | Aplicar orden de commit y auditoría |
| Reverso de contribución ya gastada | Ledger y deuda independiente | Saldos negativos | Sin compensar con recursos normales |
| Reinicio de OBS o navegador | Simulación del servidor | Solo representación | Reconectar a último snapshot |
| Fallo del servidor | Ninguna simulación nueva sin writer | Emisión se considera degradada | Restaurar snapshot + Inbox/Outbox |
| Interrupción mayor de siete días | Estado persistido | Catch-up a partir de límite | Revisión documentada del operador |
| Fin de temporada mientras hay votación | Resultado final y archivo | Nuevos votos, gastos no comprometidos | Cierre/cancelación auditable |

### Política de claridad

La interfaz no debe afirmar «todo sigue en directo» si el origen está incierto. Una cámara congelada no significa economía congelada, ni una economía offline significa ventanas de voto abiertas. Para cada incidente se emite estado comprensible y diagnóstico técnico solo en panel del operador.

### Recuperación y doble aplicación

La recuperación parte de snapshot validado y eventos no comprometidos; si se desconoce si una operación económica se confirmó, se consulta su clave de idempotencia y asiento de ledger antes de actuar. Nunca se repiten manualmente aportaciones o votos «por si acaso». Los eventos de narración pueden reproducirse como comentario histórico, pero no reactivar efectos.

### Prueba documental exigida

Cada fila se transforma en un futuro caso de aceptación con un antes, evento, después, efectos permitidos, efectos prohibidos y criterio de observabilidad. Esta tabla no implica que ya existan pruebas ejecutadas.


---

## Fuente 30 — `docs/30_ENTREGABLES_ARTISTICOS_Y_CRITERIOS_APROBACION.md`

**Blob original:** `9dee2d733122562f650cc6d71c97cbe77370b8ce`.

## 30 — Lista de entregables de arte, animación, mapa y audio

**Estado:** encargo artístico completo en intención; no se entregan sprites, voces ni música. El arte es un producto futuro y debe pasar revisión humana antes de considerarse aprobado.

### Matriz de sprites requerida

- **Ciudadanos:** 3 facciones × 13 eras × 5 profesiones = 195 combinaciones visuales; 4 orientaciones por combinación. Las herramientas evolucionan según profesión y época sin alterar colisiones.
- **Animaciones de ciudadano:** 9 acciones (`idle`, `walk`, `gather`, `haul`, `build`, `research`, `celebrate`, `rest`, `react`) con número de cuadros y FPS fijado en `art_spec.v2.json`.
- **Gobernantes:** 9 personajes base recurrentes (3 orientaciones por facción) con 13 variaciones de vestuario = 117 diseños de apariencia; reutilizar rigs y siluetas.
- **Edificios básicos:** 130 definiciones × 3 facciones = 390 skins de edificios, con cuatro etapas de construcción (umbrales oficiales).
- **Proyectos estratégicos:** 39 × 3 facciones = 117 skins si una pieza global requiere variante local; revisar la política de unicidad antes de producción.
- **Maravillas:** 13 × 3 facciones = 39 variantes visuales concebidas; la adjudicación lógica puede limitar su construcción efectiva.
- **Doctor K-0:** retrato grande HUD, sprite de mundo, estados emocionales básicos, gestos y accesorios por época; se evita producir 39 personajes completamente distintos.

### Elementos de escenario

Para cada facción: suelo base, transición de bioma, tres tipos de vegetación/roca decorativa por era visual cuando proceda, caminos, zonas de recurso natural, sombras consistentes, señales de almacén, aldeanos NPC, partículas de trabajo discretas, banderas/estandartes y efectos de hito. La selección estética no modifica el rendimiento de las parcelas o biomas.

### Ficha obligatoria por asset

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

### Criterios de aceptación por fase

**Fase de concepto:** tres fichas de facción y K-0 diferenciables sin etiquetas. **Fase de muestras:** un personaje por oficio, cuatro direcciones y una animación representativa. **Fase de época:** prueba visual de Paleolítico, Edad Media y Espacial para todas las facciones. **Fase de juego:** matriz completa, cámara vertical y horizontal, escenas con veinte sprites y con LOD alto. **Fase de emisión:** capturas OBS reales, subtítulos y partículas bajo carga. Ninguna fase se marca como entregada solo porque exista este documento.

### Limitación de alcance

La cifra de skins es una cobertura conceptual, **no** una promesa de 700 archivos únicos: los spritesheets pueden reutilizar capas, paletas y herramientas. La autoridad está en el efecto de juego; los assets deben ser intercambiables sin migrar el estado persistente.

### Ampliación v2.2: ejército y 13 maravillas individualizadas

El catálogo de combate requiere **39 formas rol/era × 3 culturas = 117 skins** adicionales, con tres siluetas de rol definidas y reutilización de rig. Las trece maravillas tienen nombres propios y motivos visuales exclusivos en `docs/61_CATALOGO_ARTISTICO_DE_EDIFICIOS_Y_MARAVILLAS_v2.2.md`. No se cuentan como PNG entregados o aprobados.


---

## Fuente 31 — `docs/31_DISENO_OPERATIVO_CUENTAS_Y_EMISIONES.md`

**Blob original:** `6fc7cdc8b73ab5b20c28c45bd035aa02ca8f09e2`.

> **Enmienda normativa v2.3 (multistreamer distribuido):** las tres cuentas pueden pertenecer a tres personas distintas y ejecutarse desde PCs/OBS diferentes. Cada broadcaster dispone de asiento, auth, Browser Source y estado de emisión propios; ningún PC aloja el motor. [Especificación vigente](CURRENT_SPEC.md).

## 31 — Diseño de emisión con una, dos o tres plataformas

**Propósito:** separar por completo las naciones de las plataformas y documentar cómo configurar cuentas sin inferir permisos reales de lectura LIVE.

### Modelo conceptual

- Cada temporada contiene exactamente tres naciones, pero cualquier plataforma puede aportar 0, 1, 2 o 3 cuentas; el máximo permitido por nación se rige por la regla canónica de `ChannelBinding`.
- Un `ChannelBinding` identifica proveedor, canal, permisos observados, fecha y revisión; no es el identificador de una nación.
- La autoridad de reloj de cada nación se establece expresamente en una fuente autenticada; dos cuentas no duplican segundos LIVE.
- Los visores OBS son salidas y pueden publicarse donde la cuenta tenga permiso; un visor no concede acceso al chat ni a monetización.
- Un mismo canal no se asigna a dos naciones en una temporada, evitando ciudadanía/votos ambiguos.

### Configuraciones previstas

| Modo | M | R | F | Observación |
|---|---|---|---|---|
| Tres cuentas del mismo proveedor | Twitch A | Twitch B | Twitch C | Tres identidades de canal distintas |
| Tres cuentas TikTok | TikTok A | TikTok B | TikTok C | Solo si lectura LIVE está autorizada y verificada |
| Tres canales YouTube | YouTube A | YouTube B | YouTube C | Una señal de reloj independiente por nación |
| Mixto | Twitch A | YouTube B | TikTok C | El overlay respeta las políticas de cada proveedor |
| Local de diseño | Simulado A | Simulado B | Simulado C | Sin identidad real ni donaciones ficticias válidas |

**Recomendación de producto:** elegir la topología de cuentas antes de preparar la temporada y congelarla al comenzar. Si cambia un canal por necesidad operativa, usar transición auditada y conservar ciudadanos existentes; no regenerar población y no cambiar la nación asignada a una cuenta ya utilizada.

### Ficha de configuración que debe cumplimentar un creador

Campaña y temporada; nación; proveedor; identificador del canal; dueño/autorización; capacidad de chat; capacidad de LIVE; capacidad de eventos económicos verificables; límite de términos de uso; canal de salida OBS; autoridad de reloj; zona horaria editorial; idiomas y permisos de moderación. Campos de permisos no verificados quedan `NO_CONFIRMED` y bloquean la funcionalidad dependiente, no se rellenan con valores de demostración.

### Si solo hay una emisión disponible

La experiencia puede mostrar las tres naciones en una misma escena pública **solo como presentación**, pero eso no resuelve cómo atribuir comandos a tres naciones dentro de un chat único. La regla canónica vigente exige que cada canal pertenezca a una única nación. Por lo tanto, una campaña con una sola cuenta para tres naciones requeriría **una decisión de producto adicional** (por ejemplo, prefijos de nación y votación por contexto), que NO está aprobada ni se presume implementada. En la versión documentada se usan tres fuentes para atribución clara, aunque todas sean del mismo proveedor.

### Seguridad, términos y comercialización

El diseño es compatible con adaptadores intercambiables, no con permisos universales inventados. Algunos servicios no facilitan de forma oficial todos los eventos que CHAOS desearía. La vinculación de una cuenta exige credenciales segregadas y consentimiento adecuado; revocar una cuenta desactiva sus capacidades sin destruir el estado histórico de la nación. Nunca prometer multistream, resúmenes cruzados de chat, lectura de regalos ni publicación automática si la plataforma no lo autoriza.


---

## Fuente 32 — `docs/32_OPERADOR_GOBERNANZA_Y_CAMBIOS_EN_VIVO.md`

**Blob original:** `cdbae7a24911b0ab9a8f95768dbfce57dc454c5a`.

> **Enmienda normativa v2.3 (multistreamer distribuido):** OWNER controla la campaña, BROADCASTER controla exclusivamente su propia emisión, MODERATOR modera y OPERATOR opera eventos auditados. Invitaciones y revocaciones por temporada, sin permisos económicos para el broadcaster. [Especificación vigente](CURRENT_SPEC.md).

## 32 — Responsabilidades del operador y gobierno del experimento

**Objetivo:** que el directo sea administrable sin controles capaces de alterar resultados arbitrariamente. No es una especificación de interfaz implementada.

### Roles de producto

- **Propietario:** configura temporada, reglas futuras, canales autorizados y condiciones de uso; no puede reescribir ledger histórico.
- **Operador:** abre/cierra escenas, programa eventos permitidos, atiende incidentes, pausa y reanuda; todas sus acciones críticas quedan auditadas.
- **Moderador de emisión:** interviene en contenido visible y nombres ofensivos; no cambia recursos, votos o victoria.
- **Observador técnico:** consulta diagnósticos sin capacidad de decidir resultados.
- **Ciudadano/espectador:** interactúa por sus comandos y votaciones; no tiene acceso a control interno ni credenciales.

### Límites de intervención

No se incluye un botón para crear oro, saltar de era, asignar ganador, alterar distribución RPS o forzar votos NPC. Las herramientas de operador autorizadas son las ya previstas: preparar/iniciar/pausar/reanudar temporada, programar evento y torneo, cancelar votación con motivo, silenciar K-0, cambiar a escena segura, detener ante emergencia y exportar auditoría.

Las correcciones extraordinarias usan un evento de compensación o una revisión de temporada y explican quién, cuándo, motivo y antes/después, en lugar de editar silenciosamente el estado. El panel debe distinguir `planeado`, `en curso`, `confirmado`, `fallido`, `cancelado` y `reintentable`.

### Libro de operación de un directo

**Antes:** comprobar fuente LIVE de cada nación, cuentas conectadas, estado de sincronización, versión de reglas, disponibilidad de voz/OBS, panel y backups. **Durante:** monitorizar latencia, cola, saturación, recursos y timers; anunciar resultados persistidos; resolver incidentes mediante escena segura. **Después:** cierre editorial, guardar resumen y revisar anomalías sin transferir saldos entre temporadas.

### Gestión de interrupciones

Una interrupción conocida de plataforma se declara `UNCERTAIN` cuando no puede demostrarse LIVE; los cronómetros se congelan aunque la audiencia crea ver vídeo. Cambiar autoridad de reloj exige transición privilegiada. El objetivo no es mantener apariencia de continuidad a cualquier coste, sino no causar perjuicio a votaciones por un fallo técnico.

### Métricas editoriales que interesa observar

Ciudadanos únicos por nación/temporada, tasa de creación a profesión, activos en últimas dos horas, ratio de completitud de misiones, tiempo hasta era, retraso en respuesta a comandos, porcentajes de abstención en votaciones, proporción de escenas informativas frente a simulación, incidentes de plataforma, eventos TTS fallidos y cambios de binding. Las métricas no sustituyen las reglas ni son instrucciones para manipular resultados.

