# Fuentes íntegras v2.5 — capítulos 57–64

> **Archivo de preservación de contenido completo (encabezados reindentados).** No es una segunda autoridad: la [especificación maestra](../ESPECIFICACION_MAESTRA_v2.5.md) resuelve reglas sustituidas. Los enlaces relativos del texto interno pertenecen al documento original citado; para navegar, abra ese archivo de origen.

---

## Fuente 57 — `docs/57_MATRIZ_DE_PRUEBAS_Y_CRITERIOS_DE_ACEPTACION_v2.2.md`

**Blob original:** `8b7298e761b6a6ee048bda5283c3a53f867b5e72`.

> **Enmienda normativa v2.3 (multistreamer distribuido):** nuevos tests MS-01..MS-08: tres ordenadores/proveedores autorizados, caída OBS aislada, reloj global RPS, revocación de invitados/tokens y reconexión sin afectar hash del motor. Ver docs 63–67. [Especificación vigente](CURRENT_SPEC.md).

## 57 — Matriz de cobertura de pruebas y aceptación futura

**Estado: catálogo de pruebas que se deberán ejecutar, no resultados de test.** Evita confundir «caso escrito» con «software probado».

### Nivel 1: consistencia documental

| ID | Entrada | Resultado esperable |
|---|---|---|
| DOC-01 | Catálogos de 13 eras, 5 profesiones, 130 básicos | Referencias de ID únicas y eras existentes |
| DOC-02 | Cada `requiresTechId` | Existe tecnología anterior/coherente con su edificio; nunca hay ciclo productor de conocimiento |
| DOC-03 | 39 proyectos y 13 maravillas v2.2 | Coste `gold=0`, precio ordinario positivo, sin bonus de producción/era |
| DOC-04 | 30 habilidades | Familia válida y destino (`food`, `wood`, `mine`, `buildWork`, `knowledge`, `xp`) consistente con texto de UI |
| DOC-05 | 5 hitos por era 1–12 | Suman 100, cada trigger único, no obtienen puntos de oro |
| DOC-06 | 3 roles × 13 eras combate | 39 tipos, 3 skins sin divergencia estadística, no hay muerte permanente |
| DOC-07 | Textos de canal | Ninguno promete una sola cuenta como tres chat sources distintas |
| DOC-08 | Arte | Tamaño, pivote y acciones consistentes entre todas las facciones |

### Nivel 2: reglas y concurrencia (para implementación futura)

| ID | Escenario | Verificación de estado |
|---|---|---|
| SIM-01 | 0 espectadores, 24 NPC, 0 oro | Todas las eras 1–12 progresan vía ruta gratuita con LIVE disponible |
| SIM-02 | 10.000 espectadores, 45 sprites verticales | Todos los votos legítimos son contabilizables; productividad capada; 30 FPS no altera economía |
| SIM-03 | Tick partido por desconexión | Exactamente el porcentaje de economía correspondiente y cero segundos LIVE ficticios |
| SIM-04 | Dos años de replay lógico comprimido | Estado y hash idénticos al resultado sin replay usando mismo ruleset |
| SIM-05 | Consejo con tres opciones y reserva vectorial | Un único cargo del ganador; ningún doble cargo por retransmisión |
| SIM-06 | Evento de oro verificado duplicado y luego revertido | Una acreditación, una deuda compensatoria, saldo no negativo |
| SIM-07 | Tres naciones alcanzan final | Un único ganador persistido por orden transaccional |
| SIM-08 | RPS A=rock B=paper C=scissors | Ciclo 2 puntos por nación por ronda y sin ganador ficticio |
| SIM-09 | Guarniciones iguales en torneo automático | Tres empates y cero sanciones |
| SIM-10 | Bonus militar | Solo defensa de combate automático; no RPS ni producción |
| SIM-11 | Misiones UTC cruzan cambio de día | Una recompensa por periodo, sin duplicar hitos |
| SIM-12 | DB caída tras cobrar proyecto antes de Outbox | Restauración sin desajuste de saldo ni obra ausente |

### Nivel 3: emisiones, UX, seguridad y arte

- **UX-01** usuario novato aprende `!join`, profesión y `!active` sin texto externo; **UX-02** rechazo de voto tras cierre; **UX-03** estado `UNCERTAIN` visible; **UX-04** vertical de 360×640 con subtítulos y 45 sprites sin tapar la escena.
- **ART-01** tres siluetas distinguibles en escala 1× y monocromo; **ART-02** 10 familias reconocibles entre tres eras; **ART-03** K-0 es claramente cyborg; **ART-04** 4 orientaciones × 9 acciones por personaje según contrato; **ART-05** todas las licencias verificadas.
- **SEC-01** prompt injection en nombre/chat no altera narrador ni economía; **SEC-02** operador sin permiso no puede acreditar oro; **SEC-03** token revocado no acepta eventos; **SEC-04** persona sin consentimiento no aparece nombrada en placa; **SEC-05** público nunca recibe ID secreto ni OAuth token.
- **OPS-01** caída del proveedor congela votos y se recupera sin reinicio de etapa; **OPS-02** reinicio OBS no altera estado; **OPS-03** restore de snapshot y logs reproduce el mismo cierre.

### Criterio de firma

Un caso pasa a **PASS** solo cuando se indica entorno, versión del ruleset, commit de código (cuando exista), datos iniciales, entradas, estado final, evidencia capturada, responsable y fecha. Hasta entonces su estado es **NOT_RUN**. No usar la palabra «validado» para un documento sin evidencias.


---

## Fuente 58 — `docs/58_IDENTIDAD_DE_PRODUCTO_Y_DESCUBRIMIENTO_v2.2.md`

**Blob original:** `0a08d509770cb32dda8ad26a3c49de11dc0c3006`.

## 58 — Identidad de marca, narrativa pública y descubrimiento

**Marca de trabajo:** **K0: The Experiment**. No existe confirmación de registro de marca, dominio o handles. Los identificadores técnicos `CHAOS` son históricos y no obligan a enseñar ese nombre al público.

### Mensaje de producto

Una experiencia de juego y espectáculo donde tres civilizaciones fantásticas avanzan desde la prehistoria hasta la era interestelar mientras la audiencia participa desde el chat, trabaja en su nación y vota decisiones colectivas. Doctor K-0 actúa como presentador científico cyborg imparcial. El juego sigue vivo gracias a NPC cuando la audiencia se ausenta; el espectáculo ocurre en directo.

### Jerarquía de marca

- Título en splash/stream: `K0: THE EXPERIMENT`.
- Presentador: `Doctor K-0` (nombre con guion en el universo, alias técnico `doctor_k0` solo si disponible).
- Primer modo: `Civilizations`/`Civilizaciones` como descriptor de la campaña, no como nombre de franquicia registrada.
- Facciones: Micelios, Rúnicos, Ferrinos; sus nombres propios no necesitan traducirse.
- Nombre interno de ingeniería e histórico: `Project CHAOS`.

### Tono editorial

Humor científico, épica de pequeñas decisiones colectivas y sorpresa histórica; no distopía cruel, violencia gráfica, apuestas ni intimidación para donar. Slogan de trabajo en inglés: “Three civilizations. One experiment. Your actions shape history.” Español: «Tres civilizaciones. Un experimento. Tus decisiones cambian la historia.» El slogan no atribuye control sobre todos los resultados a cada comentario casual: solo comandos y votos válidos lo alteran.

### Captación y recorrido

El primer fotograma útil del directo debe mostrar: nación, época, un ciudadano trabajando y comando de alta. Un clip corto se entiende sin historial del canal: incluye «qué pasó», «qué decidió la gente», «qué ha cambiado» y una pantalla de resultado. Reutilización de clips, nombres y chats estará sujeta a consentimiento y políticas de plataforma. Retención se mide por ciudadanos que vuelven, tasa `join→work`, audiencia participativa y completitud de votaciones, no por dinero aportado.

### Riesgos de comercialización

No afirmar disponibilidad legal de K0 ni de Doctor K-0 sin búsqueda registral específica; proteger obra gráfica, música, voz, fuentes y licencias comerciales. Un repositorio público exhibe las ideas y valores, pero no sustituye acuerdos de propiedad intelectual. No publicar material de espectadores o acuerdos confidenciales. El futuro SaaS es una hipótesis separada que requiere validar producto principal antes de prometer planes.


---

## Fuente 59 — `docs/59_PRODUCTO_NEGOCIO_Y_COSTES_v2.2.md`

**Blob original:** `ef1a56b7ecde0b3fd6350ce04941f277283b1a61`.

## 59 — Modelo económico del producto, infraestructura y límites de monetización

### Distinción de dos economías

1. **Economía del videojuego:** comida, madera, piedra, mineral, conocimiento, trabajo, oro de prestigio. No hay relación directa entre apoyo monetario y resultado competitivo.
2. **Economía del creador/empresa:** coste de servidores, uso de APIs, TTS, arte, moderación, licencias, legal y soporte; eventual facturación mediante suscripción/licencia del software. Las tasas no se confunden ni se convierten automáticamente unas en otras.

### Cost drivers

| Coste | Unidad a presupuestar | Instrumentación necesaria |
|---|---|---|
| Instancia .NET worker | horas de cómputo + CPU pico | `tick_duration_ms`, uso medio y P99 |
| PostgreSQL | GB almacenados + IOPS + backups | write rate, retención y restauración |
| Adaptadores | cuotas/eventos/minuto y canal | API rate limits por proveedor |
| SignalR/overlays | conexiones simultáneas y bytes emitidos | snapshots/deltas por segundo |
| Doctor K-0 | caracteres TTS, tokens LLM si hay | coste por minuto emitido y tasa de caché |
| Streaming/OBS | CPU/GPU/red por salida | FPS, bitrate, horas de emisión |
| Producción artística | skins × acciones × frames | inventario de assets aprobados |
| Operación | horas de moderación/soporte | incidentes y horas de emisión |
| Derechos/legal | licencia o servicio | titulares, territorios, documentos |

### Cálculo de capacidad, no tarifa real

Con un tick cada 5 s se ejecutan `86400/5=17.280` ticks por nación por día continuo; tres naciones implican `51.840` ticks de motor por día. Esto es un contador teórico de oportunidades de tick, **no** una medición de CPU ni facturación. Si cada nación emite un snapshot lógico cada 15 s, habrá hasta `3×86400/15=17.280` snapshots/día antes de considerar compactación, caídas de conexión y deltas. Dimensionar tráfico después de medir tamaño real de mensajes y conexiones OBS, no asignar euros ficticios.

### Estrategia recomendada

**Fase 1**: único operador y campaña, economía gratuita completa, tokens y pagos desactivados, OBS controlado. **Fase 2**: tres canales reales verificados, métricas de retención y experiencia. **Fase 3**: monetización solo decorativa, y únicamente bajo aprobación del proveedor. **Fase 4**: considerar licencia de software a creadores externos; multi-tenant, billing, SLA y personalización son extensiones, no requisitos de primer directo. Se prohíbe vender «plataformas soportadas» sin probar las cuentas y sus capacidades.

### Métricas de negocio

Visitantes→`!join`, `!join`→oficio, activos tras 1/7/30 días, votos válidos por sesión, sesiones LIVE sin incidencia, duración P50 de eras, coste TTS/stream por hora, coste operativo por campaña, ingresos **netos realmente abonados** (no equivalencia de oro). Condiciones de éxito comercial y break-even requieren inversión inicial y precios de terceros actuales, que no forman parte de este diseño cerrado.


---

## Fuente 60 — `docs/60_DEFINITION_OF_READY_Y_GATES_DE_CIERRE_v2.2.md`

**Blob original:** `c2e4bcc7c3d54cf1b1cb55467ea0f02ab32f51dd`.

> **Enmienda normativa v2.3 (multistreamer distribuido):** incorporar aceptación de 3 streamers remotos y separar evidencia documental de pruebas reales. No confundir v2.3 con producto cerrado. [Especificación vigente](CURRENT_SPEC.md).

## 60 — Definition of Ready: qué significa realmente «todo definido»

### Niveles de preparación

**D0 — IDEA:** intención, referencias y grandes reglas. **D1 — DISEÑO DOCUMENTAL:** entidades, comandos, números candidatos, UX, narrativa, arte objetivo y casos límite definidos. **D2 — DISEÑO CERRADO PARA PROTOTIPO:** referencias visuales aprobadas, invariantes sin contradicciones, modelos económicos reproducibles de principio a fin, responsabilidades y contratos consistentes, elección de proveedor objetivo. **D3 — IMPLEMENTACIÓN VERIFICADA:** motor, SQL, UI, integración, seguridad, arte final y pruebas reales operativas. **D4 — LANZAMIENTO AUTORIZADO:** cuentas LIVE permitidas, monetización (si aplica) conforme a términos, datos/privacidad/propiedad intelectual revisados y operación ensayada.

**Estado demostrado hoy: D1 ampliado; no D2, D3 ni D4.** Esta clasificación es deliberadamente estricta.

### Gate de cierre funcional

- [ ] 92 decisiones históricas reproducidas y toda sustitución explicada; las reglas vigentes no están contradichas por tablas legibles.
- [ ] Una temporada completa con 0 espectadores, 0 oro y 24 NPC por nación alcanza Interestelar sin bloqueo usando los **cinco hitos reales de cada era**.
- [ ] Todas las elecciones, Consejos, RPS, batallas y maravillas tienen estados, tiempos, empates y reintentos validados.
- [ ] Simultaneidad y recuperación no duplican votos, oro, edificios o ganador.
- [ ] El usuario novato entiende chat, oficio, actividad, retorno y misiones sin ayuda externa.

### Gate de cierre artístico

- [ ] Captura/arte conceptual final aprobado de Micelios, Rúnicos, Ferrinos y K-0.
- [ ] Tres eras representativas (Paleolítico, Industrial y Espacial) diseñadas para las tres especies.
- [ ] Sprite 16×24, 32×16 tile, sombras, paletas, variantes, HUD y animaciones probados a 1× y en stream vertical.
- [ ] Fuente, sonido, música, voz y derechos comerciales acreditados.
- [ ] Texto y subtítulos legibles sin depender de audio; safe areas verificadas por plataforma.

### Gate de cierre técnico

- [ ] Anexo SQL v2.2 integrado y validado para combate, patrocinios y demás nuevos estados; migraciones reales ejecutadas con tests transaccionales.
- [ ] Contratos REST/SignalR actualizados a las entidades efectivas y sus versiones.
- [ ] Ingesta idempotente, escritura única, determinismo, replays y backups restaurados con evidencia.
- [ ] Pruebas de carga y mediciones de costes con perfiles realistas y 30 FPS OBS estable.
- [ ] Autorización del proveedor, cuotas, política LIVE y límites de monetización comprobados por **cuenta**, no por idea.

### Gate multistreamer distribuido v2.3

- [ ] Una campaña de tres streamers independientes se completa desde 3 equipos y redes distintos sin ejecutar motor local en ninguno.
- [ ] Tres cuentas de mismo proveedor verificadas y tres overlays separados; mezclas de proveedores solo cuando los permisos reales lo demuestren.
- [ ] OBS de un streamer cae sin alterar LIVE certificado ni economía; desconexión LIVE de una nación congela simultáneamente reloj global de RPS en tres viewers.
- [ ] Invitaciones, scopes, OAuth, revocación, aislamiento de identidades y salida pública minimizada probados.
- [ ] CURRENT_SPEC, catálogos, API, SQL y versiones de reglas concuerdan; CI verde y migraciones PostgreSQL realmente ejecutadas.
- [ ] Cuenta real de proveedor, volumen de audiencia, arte, legal y restore con evidencia verificable, no texto.

**El estado permanece D1 ampliado; este añadido no demuestra D2 ni un juego implementado.**

### Gate de cierre comercial y normativo

- [ ] Distintividad registral/uso de K0 y Doctor K-0 comprobada en territorios elegidos.
- [ ] Titularidad/licencias de sprites, tipografías, voz, música y contenidos confirmadas.
- [ ] Política real de datos, acceso, retención y solicitudes de usuarios aprobada para la jurisdicción.
- [ ] Presupuesto de infraestructura, moderación, marketing, mantenimiento y operación basado en tarifas/uso verificables.
- [ ] Reglas de contribución económica verificadas con reversos reales o mantenidas apagadas.

### Política de aprobación

Cada casilla requiere documento, evidencia, responsable, fecha y versión. No «marcar completado» por haber escrito su intención. El propietario puede congelar un baseline **para desarrollo** sin que eso signifique que ya existe producto terminado. Las dependencias externas no son defectos que puedan arreglarse escribiendo más Markdown; deben mostrarse como gates, jamás como supuestos ocultos.


---

## Fuente 61 — `docs/61_CATALOGO_ARTISTICO_DE_EDIFICIOS_Y_MARAVILLAS_v2.2.md`

**Blob original:** `4cc44495f75f16c742f1fc95cda2164b1b364d69`.

## 61 — Catálogo de dirección artística para 130 edificios y 13 maravillas

**Estado VISUAL_BRIEF, no sprites finales.** Cada fila vincula familia, época y edificio concreto (`data/buildings.v2.json`); la silueta final debe mantener **la huella lógica exacta** y las cuatro etapas de obra. Las tres facciones usan misma regla y colisión, pero diferente arquitectura.

### Transformadores culturales de cualquier edificio

- **Micelios:** cubierta de micelio tejido, pilares orgánicos, entramados de raíces, esporas luminosas discretas. Evitar coral marino, aspecto viscoso indiferenciado y ventaja botánica funcional.
- **Rúnicos:** pilares mineral-poliedro, juntas facetadas, runas geométricas de luz azul, tecnología cristalina. Evitar humanos con armadura y efectos que den ventaja de minería.
- **Ferrinos:** placas bioférricas remachadas, articulaciones, oxidación controlada, arcos de metal vivo. Evitar máquinas totalmente robóticas y coral metálico.

Cada diseño debe producir `faction/era/entity`, cuatro estados de construcción (15/40/70/100 %) y sombras/pivote estables. Las variaciones no añaden edificios extra ni coste lógico.

### Matriz visual completa: 130 edificios básicos

| Era | Familia | Edificio ID | Silueta/objeto dominante a dibujar |
|---|---|---|---|
| Paleolítico | `housing` | `paleolithic_housing` | Refugio de pieles y roca |
| Paleolítico | `food_production` | `paleolithic_food_production` | Fogón comunitario de caza |
| Paleolítico | `forestry` | `paleolithic_forestry` | Bosque señalizado con cestas |
| Paleolítico | `extraction` | `paleolithic_extraction` | Frente de cantera con cinceles |
| Paleolítico | `workshop` | `paleolithic_workshop` | Mesa de hueso y sílex |
| Paleolítico | `research` | `paleolithic_research` | Círculo oral junto al fuego |
| Paleolítico | `storage` | `paleolithic_storage` | Fosa protegida con techo |
| Paleolítico | `infrastructure` | `paleolithic_infrastructure` | Sendero de piedra suelta |
| Paleolítico | `civic` | `paleolithic_civic` | Círculo del Consejo alrededor del fuego |
| Paleolítico | `defense` | `paleolithic_defense` | Puesto de guardia con empalizada |
| Neolítico | `housing` | `neolithic_housing` | Cabaña con huerto |
| Neolítico | `food_production` | `neolithic_food_production` | Granero de siembra y molino |
| Neolítico | `forestry` | `neolithic_forestry` | Vivero vallado y cobertizo |
| Neolítico | `extraction` | `neolithic_extraction` | Excavación de piedra con rampa |
| Neolítico | `workshop` | `neolithic_workshop` | Banco de alfarería y telares |
| Neolítico | `research` | `neolithic_research` | Casa de símbolos y calendario |
| Neolítico | `storage` | `neolithic_storage` | Granero comunitario de barro |
| Neolítico | `infrastructure` | `neolithic_infrastructure` | Camino con acequias y marcas |
| Neolítico | `civic` | `neolithic_civic` | Plaza de elección de clan |
| Neolítico | `defense` | `neolithic_defense` | Vigía de madera y foso |
| Edad del Cobre | `housing` | `copper_housing` | Casa de adobe con hebillas de cobre |
| Edad del Cobre | `food_production` | `copper_food_production` | Secadero de grano y conductos de cobre |
| Edad del Cobre | `forestry` | `copper_forestry` | Aserradero de herramientas cobrizas |
| Edad del Cobre | `extraction` | `copper_extraction` | Pozo y mena con apoyos de cobre |
| Edad del Cobre | `workshop` | `copper_workshop` | Taller de cinceles de cobre |
| Edad del Cobre | `research` | `copper_research` | Tablillas y estantería de cobre |
| Edad del Cobre | `storage` | `copper_storage` | Depósito sellado de cobre |
| Edad del Cobre | `infrastructure` | `copper_infrastructure` | Calzada primitiva con carriles cobrizos |
| Edad del Cobre | `civic` | `copper_civic` | Ágora de cobre con tótems |
| Edad del Cobre | `defense` | `copper_defense` | Torreta de escudo cobrizo |
| Edad del Bronce | `housing` | `bronze_housing` | Vivienda con tejado de aleación |
| Edad del Bronce | `food_production` | `bronze_food_production` | Horno comunal con silo |
| Edad del Bronce | `forestry` | `bronze_forestry` | Taller de madera aleada |
| Edad del Bronce | `extraction` | `bronze_extraction` | Fundición de mineral a pie de mina |
| Edad del Bronce | `workshop` | `bronze_workshop` | Horno de aleación y moldes |
| Edad del Bronce | `research` | `bronze_research` | Archivo de escritura y aleaciones |
| Edad del Bronce | `storage` | `bronze_storage` | Almacén de ánforas y bronce |
| Edad del Bronce | `infrastructure` | `bronze_infrastructure` | Camino de carros reforzados |
| Edad del Bronce | `civic` | `bronze_civic` | Foro de bronce |
| Edad del Bronce | `defense` | `bronze_defense` | Bastión de bronce en terrazas |
| Edad del Hierro | `housing` | `iron_housing` | Casa de fundidor y adobe rojo |
| Edad del Hierro | `food_production` | `iron_food_production` | Almacén de cereal con arado férreo |
| Edad del Hierro | `forestry` | `iron_forestry` | Cobertizo de sierras de hierro |
| Edad del Hierro | `extraction` | `iron_extraction` | Mina reforzada con vigas ferrosas |
| Edad del Hierro | `workshop` | `iron_workshop` | Fragua con yunques |
| Edad del Hierro | `research` | `iron_research` | Cámara de experimentación férrea |
| Edad del Hierro | `storage` | `iron_storage` | Depósito de hierro modular |
| Edad del Hierro | `infrastructure` | `iron_infrastructure` | Puente de vigas de hierro |
| Edad del Hierro | `civic` | `iron_civic` | Gran sala de decisiones férreas |
| Edad del Hierro | `defense` | `iron_defense` | Torre de hierro y almenas |
| Antigüedad | `housing` | `antiquity_housing` | Domus con patio interior |
| Antigüedad | `food_production` | `antiquity_food_production` | Terraza agrícola irrigada |
| Antigüedad | `forestry` | `antiquity_forestry` | Bosque gestionado con vías |
| Antigüedad | `extraction` | `antiquity_extraction` | Cantera de columnas y poleas |
| Antigüedad | `workshop` | `antiquity_workshop` | Taller de hidráulica cívica |
| Antigüedad | `research` | `antiquity_research` | Biblioteca cívica con pergaminos |
| Antigüedad | `storage` | `antiquity_storage` | Almacén cívico con arcos |
| Antigüedad | `infrastructure` | `antiquity_infrastructure` | Calzada cívica con acueducto |
| Antigüedad | `civic` | `antiquity_civic` | Foro clásico de asamblea |
| Antigüedad | `defense` | `antiquity_defense` | Fortín y formación de muralla |
| Edad Media | `housing` | `medieval_housing` | Casas gremiales compactas |
| Edad Media | `food_production` | `medieval_food_production` | Huerta amurallada de monasterio |
| Edad Media | `forestry` | `medieval_forestry` | Leñera del gremio |
| Edad Media | `extraction` | `medieval_extraction` | Galería con elevador de contrapesos |
| Edad Media | `workshop` | `medieval_workshop` | Forja gremial de dos pisos |
| Edad Media | `research` | `medieval_research` | Scriptorium y telescopio primario |
| Edad Media | `storage` | `medieval_storage` | Bodega gremial con torre |
| Edad Media | `infrastructure` | `medieval_infrastructure` | Camino de adoquín y puente levadizo |
| Edad Media | `civic` | `medieval_civic` | Salón de gremios |
| Edad Media | `defense` | `medieval_defense` | Castillo facetado y atalaya |
| Renacimiento | `housing` | `renaissance_housing` | Palacio-casa con logia |
| Renacimiento | `food_production` | `renaissance_food_production` | Invernadero renacentista |
| Renacimiento | `forestry` | `renaissance_forestry` | Jardín botánico y banco de semillas |
| Renacimiento | `extraction` | `renaissance_extraction` | Observatorio de minerales con bombas |
| Renacimiento | `workshop` | `renaissance_workshop` | Laboratorio artesanal con engranajes |
| Renacimiento | `research` | `renaissance_research` | Academia con lentes y observatorio |
| Renacimiento | `storage` | `renaissance_storage` | Almacén de cajas y polipastos |
| Renacimiento | `infrastructure` | `renaissance_infrastructure` | Vía cartografiada y canal |
| Renacimiento | `civic` | `renaissance_civic` | Palacio de ciencia cívica |
| Renacimiento | `defense` | `renaissance_defense` | Baluarte geométrico de ingeniería |
| Era Industrial | `housing` | `industrial_housing` | Bloque obrero con chimenea |
| Era Industrial | `food_production` | `industrial_food_production` | Planta de molienda a vapor |
| Era Industrial | `forestry` | `industrial_forestry` | Aserradero de poleas de vapor |
| Era Industrial | `extraction` | `industrial_extraction` | Pozo industrial y vagón |
| Era Industrial | `workshop` | `industrial_workshop` | Factoría de cadenas y engranajes |
| Era Industrial | `research` | `industrial_research` | Laboratorio químico a vapor |
| Era Industrial | `storage` | `industrial_storage` | Nave de distribución ferroviaria |
| Era Industrial | `infrastructure` | `industrial_infrastructure` | Tramo ferroviario de vapor |
| Era Industrial | `civic` | `industrial_civic` | Ayuntamiento de ladrillo industrial |
| Era Industrial | `defense` | `industrial_defense` | Puesto industrial con reflector |
| Era Moderna | `housing` | `modern_housing` | Barrio de módulos electrificados |
| Era Moderna | `food_production` | `modern_food_production` | Estación de riego eléctrico |
| Era Moderna | `forestry` | `modern_forestry` | Instalación forestal electrificada |
| Era Moderna | `extraction` | `modern_extraction` | Complejo de extracción motorizado |
| Era Moderna | `workshop` | `modern_workshop` | Taller de precisión electromecánica |
| Era Moderna | `research` | `modern_research` | Centro científico electrificado |
| Era Moderna | `storage` | `modern_storage` | Centro logístico de contenedores |
| Era Moderna | `infrastructure` | `modern_infrastructure` | Carretera asfaltada y cableado |
| Era Moderna | `civic` | `modern_civic` | Centro de decisión luminoso |
| Era Moderna | `defense` | `modern_defense` | Centro de protección electromecánico |
| Era Digital | `housing` | `digital_housing` | Hábitat domótico conectado |
| Era Digital | `food_production` | `digital_food_production` | Cultivo automatizado vertical |
| Era Digital | `forestry` | `digital_forestry` | Cultivo de biomasa en red |
| Era Digital | `extraction` | `digital_extraction` | Mina robotizada de cristal |
| Era Digital | `workshop` | `digital_workshop` | Fábrica CNC miniaturizada |
| Era Digital | `research` | `digital_research` | Centro de datos en miniatura |
| Era Digital | `storage` | `digital_storage` | Almacén automatizado de datos/cargas |
| Era Digital | `infrastructure` | `digital_infrastructure` | Red de transporte automatizada |
| Era Digital | `civic` | `digital_civic` | Nexo público de datos |
| Era Digital | `defense` | `digital_defense` | Nexo de defensa de información |
| Era Espacial | `housing` | `space_housing` | Cúpula presurizada residencial |
| Era Espacial | `food_production` | `space_food_production` | Biorreactor hidropónico orbital |
| Era Espacial | `forestry` | `space_forestry` | Jardín de biomasa en cápsula |
| Era Espacial | `extraction` | `space_extraction` | Extractor de regolito presurizado |
| Era Espacial | `workshop` | `space_workshop` | Forja modular de vacío |
| Era Espacial | `research` | `space_research` | Observatorio orbital compartimentado |
| Era Espacial | `storage` | `space_storage` | Módulo de depósito orbital |
| Era Espacial | `infrastructure` | `space_infrastructure` | Pasarela de gravedad orbital |
| Era Espacial | `civic` | `space_civic` | Cámara de consejo espacial |
| Era Espacial | `defense` | `space_defense` | Torre orbital de observación |
| Era Interestelar | `housing` | `interstellar_housing` | Nido interestelar de luz sólida |
| Era Interestelar | `food_production` | `interstellar_food_production` | Sintetizador de nutrientes estelares |
| Era Interestelar | `forestry` | `interstellar_forestry` | Fábrica de biopolímeros sintéticos |
| Era Interestelar | `extraction` | `interstellar_extraction` | Recolector de fragmentos estelares |
| Era Interestelar | `workshop` | `interstellar_workshop` | Ingeniería de metamateriales |
| Era Interestelar | `research` | `interstellar_research` | Laboratorio cuántico interestelar |
| Era Interestelar | `storage` | `interstellar_storage` | Bóveda de inventario interestelar |
| Era Interestelar | `infrastructure` | `interstellar_infrastructure` | Corredor de tránsito fotónico |
| Era Interestelar | `civic` | `interstellar_civic` | Plaza ceremonial de las eras |
| Era Interestelar | `defense` | `interstellar_defense` | Escudo espacial ceremonial |

### Las 13 maravillas con identidad propia

| Era | ID | Nombre | Dirección artística distintiva |
|---|---|---|---|
| Paleolítico | `wonder_paleolithic` | **El Primer Fuego** | Tres fuentes del Primer Fuego rodeadas por estelas ancestrales; la llama no extingue otras naciones. |
| Neolítico | `wonder_neolithic` | **El Gran Semillero** | Jardín elevado con tres coronas de semillas, puertas rituales y suelo agrícola en anillos. |
| Edad del Cobre | `wonder_copper` | **La Forja del Alba** | Gran crisol de cobre sostenido por arcos, reflejos que remiten al amanecer. |
| Edad del Bronce | `wonder_bronze` | **El Crisol de los Tres** | Tres hornos de aleación convergentes sobre una plaza de bronce; no representar victoria de una especie concreta. |
| Edad del Hierro | `wonder_iron` | **El Bastión de las Chispas** | Bastión remachado con cinco chimeneas, fortaleza simbólica sin efecto de defensa competitivo. |
| Antigüedad | `wonder_antiquity` | **La Biblioteca del Primer Reino** | Archivo monumental de estanterías/tablillas con pórticos cívicos y columna central. |
| Edad Media | `wonder_medieval` | **La Aguja de los Juramentos** | Aguja de piedra y metal con cintas de juramentos, mirador y campanas. |
| Renacimiento | `wonder_renaissance` | **El Observatorio de las Tres Lunas** | Observatorio circular con tres lentes y bóveda de las lunas, instrumentos no funcionales. |
| Era Industrial | `wonder_industrial` | **El Corazón de Vapor** | Motor de vapor central dentro de cúpula de vidrio y engranajes monumentales. |
| Era Moderna | `wonder_modern` | **La Torre de Resonancia** | Antena-torre de resonancia con anillos eléctricos suaves y plataforma de museo. |
| Era Digital | `wonder_digital` | **El Archivo de las Mil Voces** | Biblioteca de datos pública con pantallas de píxeles, columnas de información y techo abstracto. |
| Era Espacial | `wonder_space` | **La Puerta del Horizonte** | Arco de horizonte orbital con vacío estrellado visible detrás de su marco. |
| Era Interestelar | `wonder_interstellar` | **El Umbral Interestelar** | Portal interestelar de tres símbolos y luz contenida; únicamente epílogo tras victoria. |

### Proyectos estratégicos de cada era

El trío de Consejo mantiene tres conceptos funcionalmente cosméticos en todas las eras: **Memorial** (monumento vertical con nombres moderados de fundadores), **Espectáculo** (plaza abierta de ceremonia con zona visible de espectadores) y **Archivo** (edificio de memoria/historia con símbolos de la era). Para los 39 casos, el transformador cultural anterior se aplica a la tecnología y material de la fila de la era; coste exacto y trabajo están en `docs/35`. Dos proyectos de la misma época deben distinguirse por silueta vertical/plaza horizontal/volumen de libros-datos, respectivamente.

### Gate artístico

Para elevar esta especificación a arte aprobado hacen falta al menos: cuatro siluetas principales en 1× (3 naciones y K-0), 10 familias × 3 eras muestra, una maravilla por rol visual, un test de HUD con 45 ciudadanos y una auditoría de licencias. Los **390 skins básicos**, **117 skins de proyectos**, **39 variantes de maravilla** y **117 skins de unidades de combate** son entregables futuros, no PNG ya producidos.


---

## Fuente 62 — `docs/62_PERSONAJES_NPC_Y_EVOLUCION_ESTETICA_v2.2.md`

**Blob original:** `62515331ded2bf8be9c661a2e6fb240e9a582e84`.

## 62 — Biblia de gobernantes NPC y evolución de sus vestuarios

**Estado: diseño narrativo y visual, no retratos aprobados.** Los 9 candidatos recurrentes son personajes del universo, no ciudadanos reales. Cambian ropas y herramientas entre eras pero preservan rostro/silueta. Solo existe un gobernante activo por nación y era jugable, elegido mediante voto colectivo.

### Micelios

#### Morga — candidata económica

Figura fungoide robusta, sombrero ancho en tres capas, bolsa de semillas y una lupa de cobre que se convierte con las eras en dispositivo bioeconómico. Actitud paciente, protectora de reservas y obras. Paleta base verde musgo con acentos ámbar. Voz imaginada grave, pragmática. En campaña presenta presupuestos y transporte, pero **no controla recursos autónomamente**. En Paleolítico porta granero de corteza; Industrial, arnés de tuberías; Digital, brazalete de biomasa; Espacial, cinturón de cultivo presurizado.

#### Bruk — candidato militar

Fungoide alto con capuchón estrecho, espinas secas decorativas y extremidades largas; silueta de defensor sin parecer depredador. Carga estandarte o escudo ornamental, nunca arma realista. Habla en frases cortas. Su bono es +500bp a defensa automática durante eventos programados; jamás a RPS, al trabajo ni a ataques libres. Vestuario de piel primitiva, armadura de fibras, grebas metálicas, escudo biomecánico, exoesqueleto de protección orbital según época.

#### Espora — candidata científica

Fungoide delgado, capuchón asimétrico que recuerda a una campana de laboratorio, frascos de esporas y filamentos luminosos. Sus efectos son solo +300bp conocimiento; no crea tecnologías ni puntos de historia por diálogo. Evolución: tablillas, lentes, ábaco, microscopio, visor computacional y microscopía cuántica visual.

### Rúnicos

#### Dorrik — candidato económico

Cuerpo minero de placas trapezoidales, tres líneas rúnicas verticales en torso y gran cinturón de llaves/contratos, no martillo de batalla. Silueta cuadrada estable. Evolución: sellos de piedra, balanza, libro de rutas, prensa industrial, tablet de cristal y mapa de suministro estelar. Bono únicamente +300bp a recursos económicos; no ventajas por ser de piedra.

#### Kraag — candidato militar

Figura mineral baja y ancha, hombros prismáticos pronunciados, runa de guardia en forma de escudo; lenguaje físico de protector, no agresor humano. No brilla permanentemente: efectos limitados cuando habla. Escudos de piedra, bronce, fortaleza gótica, blindaje técnico y campo estelar decorativo según era. Su aporte cuantitativo sigue las mismas reglas que Bruk y Rokka.

#### Zyn — candidato científico

Rúnico de cráneo alargado en punta cristalina, inscripciones finas en brazos, anillo de observación flotante solo como FX, no magia funcional. Habla de hipótesis y patrones. Pasa de pictogramas tallados a mapas celestes, lentes, procesadores cristalinos y observadores interestelares. Bono ciencia +300bp, igual a Espora y Neri.

### Ferrinos

#### Nera — candidata económica

Ferrina de exoesqueleto biológico cobrizo, cabeza compacta triangular con dos ojos expresivos, vientre de placas de almacenamiento y herramientas de logística. No robot industrial humano ni recuerdo a los Corálidos descartados. Evolución: balanza, alforja metálica, máquina de estampación, aparato eléctrico y red de transporte orbital. Mismas estadísticas que Morga y Dorrik.

#### Rokka — candidato militar

Ferrino de placas anchas superpuestas, centro corporal estrecho y protector frontal curvado. Avanza hacia exoprotección tecnológica, no armadura de soldado realista. Actitud ceremoniosa; evita lenguaje de muerte. Defensa +500bp solamente durante eventos apropiados. No determina directamente el campeón ni retira recursos por decisión propia.

#### Neri — candidato científico

Ferrina estilizada con una antena orgánica corta, mandíbulas articuladas y tubo de instrumentos, ojos cálidos visibles. Científica curiosa de la evolución material; herramientas desde pruebas minerales a nanosondas y instrumentos astrales. Bono ciencia +300bp, sin beneficio extra por naturaleza ferruginosa.

### Gramática de vestuario por era para los nueve

| Era | Accesorio común por rol | Anacronismos prohibidos |
|---|---|---|
| Paleolítico | Cuerda/bastón, escudo de corteza, tablilla | Piezas electrónicas funcionales |
| Neolítico | Granero/semillas, empalizada, calendario | Pantallas y energía moderna |
| Cobre | Balanza, escudo de cobre, ficha metálica | Acero industrial |
| Bronce | Remaches, insignia, escritura | Plástico y holografía |
| Hierro | Herramientas férreas y banderines | Armas contemporáneas |
| Antigüedad | Toga/estola cultural, placa cívica, instrumento | Iconografía religiosa real apropiada |
| Media | Gremio, escudo, pergamino | Uniformes nacionales reconocibles |
| Renacimiento | Cartografía, óptica, brújula | Instrumentos digitales |
| Industrial | Conductos, maquinaria, placas de laboratorio | Visores cuánticos |
| Moderna | Electrificación, señalización, bata técnica | Holograma omnipresente |
| Digital | Paneles de datos y circuitos | Ruido visual no legible a 1× |
| Espacial | Soporte presurizado y antenas | Siluetas indistinguibles entre roles |
| Interestelar | Atuendo ceremonial de epílogo | Nuevas elecciones tras final de temporada |

### Composición y equidad

Para cada candidato preparar retrato de votación, sprite de mundo, gesto neutral y gesto de anuncio. Mantener la posición del icono económico/militar/científico consistente en todos los paneles. Los nombres de los NPC se anuncian en neutralidad estricta; cualquier emoción de K-0 o personaje no puede alterar voto. La paleta, anclajes y estadísticas de los tres arquetipos son equivalentes por facción.

### Aceptación

Diseñar nueve siluetas monocromas distinguibles y sus tres poses principales; realizar tres variaciones de época de referencia (Paleolítico, Industrial, Espacial). La identidad debe mantenerse sin dependencia de una textura HD. Los 117 looks (9×13) y retratos no existen todavía, y el estado de estos personajes sigue siendo **VISUAL_BRIEF** hasta su aprobación artística.


---

## Fuente 63 — `docs/63_ARQUITECTURA_MULTISTREAMER_v2.3.md`

**Blob original:** `285a7c36c368cbfa7021c2bf9dc941a0fec229b8`.

## 63 — Arquitectura multistreamer distribuida (v2.3)

**Normativo para diseño, no implementación validada.** Esta especificación amplía docs 02,13,31,32,55. La nación no equivale a streamer ni a proveedor. Cada emisor puede estar en otro PC, ciudad, sistema operativo o red; la conexión pública HTTPS al servicio K0 es el único requisito de red del cliente de emisión.

### 1. Topologías admisibles

- **Solo operador:** un propietario controla tres canales distintos (reales o simulados); las tres naciones y salidas se crean en la misma campaña. Puede emitir una escena combinada.
- **Tres streamers, mismo proveedor:** Twitch A/B/C (o YouTube A/B/C), cada uno con propiedad y credenciales propias, PC/OBS independientes. El servidor recibe los tres chats, cada uno vinculado a UNA nación.
- **Tres streamers, proveedores mixtos:** Twitch A, YouTube B y otra plataforma C solamente si existe adaptador/autorización válida para esa cuenta concreta.
- **Co-stream:** varias salidas/streamers pueden mostrar la misma nación cuando lo autorice el dueño de campaña, pero un binding tiene exactamente una nación. Un único canal no puede representar dos naciones.
- **Varias campañas:** cada Campaign/Season tiene namespace, hashes, seed, roles, canales y base de datos lógica aislada. No se unen temporadas distintas por coincidir streamer, plataforma o alias.
- **No soportado v2.3:** tres naciones votando desde un solo chat sin asignación verificable; servidor autoritativo instalado por cada streamer; P2P con consenso entre OBS; traducción automática de regalos a oro.

**Modo de temporada obligatorio:** Season.broadcastMode = SINGLE_OPERATOR o MULTI_STREAMER. SINGLE_OPERATOR admite una cuenta K0 como responsable de los tres canales; MULTI_STREAMER exige tres cuentas K0 **distintas** como broadcaster primario, cada una con un asiento aceptado en una nación diferente. Co-streamers no sustituyen el primario. El sistema valida esta invariante en DRAFT→PREPARED dentro de transacción antes de habilitar una temporada pública.

### 2. Arquitectura lógica y despliegue

Diagrama de flujo:

    Streamer A OBS (Browser Source) ---HTTPS/WSS--\
    Streamer B OBS (Browser Source) ---HTTPS/WSS---+--> API / Projections / SignalR
    Streamer C OBS (Browser Source) ---HTTPS/WSS--/             |
                                                             Postgres
    Twitch/YouTube/TikTok autorizados -> ProviderIngress -> Inbox -> CommandProcessor
                                                                   |
                                                 NationSimulation (.NET 10)
                                                   + CompetitionEngine
                                                   + SeasonArbiter
                                                                   |
                                                        Ledger + Outbox
                                                                   |
                                                            ShowDirector

- El servidor .NET es único lógicamente. Módulos: Campaigns, Accounts, Streamers, Memberships, ChannelBindings, ProviderIngress, Inbox/Outbox, Citizens, Economy, NationSimulation, PoliticalScheduler, Competition, GlobalArbiter, Projection, OverlayAuth, ShowDirector, Operator.
- **PostgreSQL 16+** como persistencia ACID, no SQLite central ni almacenamiento local en OBS. Mismo motor de SQL de dev y producción; transacciones y hashes versionados.
- Un writer por nación y un coordinador de temporada para ganador/maravillas/competición. Se asigna lease/fencing por nación si hay más de un proceso desplegado; por defecto un worker; no usar microservicios ni brokers externos sin necesidad medida.
- El cliente web React + Phaser pinta HUD/mundo; datos llegan por snapshot y deltas SignalR; no recibe credenciales de proveedor.
- El usuario puede abrir un panel web seguro desde su PC para gestionar emisión. El navegador del espectador no es obligado para participar: chat nativo de la plataforma.

### 3. Modelo de entidades e identidad

| Entidad | Clave lógica | Propósito |
|---|---|---|
| AccountUser | UUID interno + proveedor de login | Usuario autenticado de K0; no confundir con espectador/chat |
| Campaign | UUID | Producto/campaña bajo control de owner |
| CampaignMembership | (campaignId,userId) | OWNER, OPERATOR, BROADCASTER, MODERATOR, AUDITOR |
| Season | UUID + campaignId + manifest | Una competición de 3 naciones y reglas congeladas |
| Nation | (seasonId, nationId UUID) | Estado competitivo; factionId estable |
| StreamerSeat | (seasonId,nationId,userId) | Invitación/aceptación de broadcaster principal y cohosts |
| ProviderConnection | (userId,provider,accountId) | OAuth/credencial propiedad del streamer, cifrada |
| ChannelBinding | (seasonId,provider,channelId) único | Ruta de eventos a una nación, roles y clock authority |
| ProviderLiveSession | (bindingId,providerSessionId) | Evidencia LIVE, lastSeen, health, TTL y revisión |
| BroadcastOutput | (outputId,seasonId,viewerScope) | Vista OBS, escena, formato, permisos y token revocable |
| PresentationCue | (seasonId,sequence,cueId) | Presentación global o específica sin efectos de economía |
| ViewerCitizen | (seasonId,nationId,provider,userId) | Identidad del jugador por canal/nación, no el streamer |

No equiparar BroadcastOutput, ChannelBinding y ProviderLiveSession: una fuente de chat puede alimentar varios overlays autorizados; un overlay no acredita que la plataforma esté LIVE.

### 4. Invitaciones, propiedad y permisos

1. OWNER crea Campaign/Season DRAFT y tres Nation asignadas a facciones.
2. OWNER invita a cada streamer mediante enlace expirable de un solo uso, restringido a temporada/nación/rol; la invitación no expone tokens.
3. El streamer inicia sesión en K0, acepta condiciones y enlaza su propia cuenta del proveedor vía OAuth cuando exista. La identidad del streamer debe corresponder a un canal que controla o para el que tiene autorización verificable.
4. El OWNER ve estado de **permiso de lectura de chat**, **verificación LIVE**, **contribuciones**, **overlay** por separado. Ninguna capability no verificada se activa automáticamente.
5. OWNER congela asientos, bindings, autoridades de reloj, seed y manifiesto antes de PREPARED→RUNNING. Cambios posteriores requieren pausa de ingreso + drenaje Inbox + BindingRevision + auditoría y revalidación del originador.
6. Cada broadcaster genera su URL de overlay con un secreto de solo lectura, lo configura como Browser Source en OBS local y puede revocarlo.
7. OWNER controla start/pause/abort; BROADCASTER controla su propia escena y puede informar incidente, nunca asignar ganador ni regalar recursos. MODERATOR filtra contenidos. AUDITOR solo consulta.

**Invariantes:** una cuenta/canal no aparece en dos bindings activos de naciones diferentes en una temporada; una nación tiene exactamente una fuente autorizada de LIVE activa o queda OFFLINE/UNCERTAIN; cada nación tiene al menos un broadcaster primario en modo multistreamer; en modo solo el propietario puede ocupar las tres plazas. Una persona no obtiene control ADMIN por ser streamer.

### 5. Autonomía de tres ordenadores

Cada PC debe poder:
- Encender OBS, cargar una URL HTTPS específica, ver estado remoto y emitir sin instalar motor ni abrir puertos entrantes.
- Recibir snapshots y deltas de su nación y estados agregados de rivales. No accede a balances internos restringidos de otras naciones.
- Recuperar visualización tras reiniciar OBS, perder Wi-Fi o cambiar resolución, sin modificar resultado del juego.
- Cambiar escena visual localmente sin manipular cuándo termina una elección; puede silenciar la voz local de K-0.
- Mostrar contador de conexión del overlay separado de estado real de STREAM; una fuente proveedor LIVE sigue LIVE aunque OBS Browser Source esté desconectado.

**El equipo del streamer no almacena** hashes de contraseñas, claves de otras cuentas, SQLite autoritativa, payloads financieros, tokens OAuth del proveedor ni logs de espectadores de otra nación.

### 6. Independencia de directos y política de equidad

Una temporada puede tener A LIVE, B OFFLINE, C LIVE. Se aplica a cada nación su NationEconomyClock original (100 % LIVE; 20 % offline). Los votos de B y su avance de era esperan su LIVE confirmado. La carrera puede favorecer al streamer que emite más horas: **es una consecuencia explícita del diseño histórico, no un bug oculto**. Se publicará tiempo LIVE acumulado por nación y advertencia al crear campaña. Modalidades con paridad estricta por horas o caps diarios serían un ADR distinto, no un valor implícito.

RPS y batallas programadas se activan exclusivamente con los tres LIVE confirmados y su **CompetitionLiveClock global**. Si uno cae, se congelan las tres ventanas y el operador puede cancelar sin penalización tras un plazo de incidencia; ninguna nación queda castigada por la caída. El evento se reanuda con los mismos votos y tiempo pendiente si la evidencia vuelve y aún está dentro de la política de sesión.

### 7. Control de espectadores multicanal

- Cada entrada trae provider, channelId, providerEventId, providerUserId, receivedUtc y prueba del permiso/autoridad.
- Routing lookup preciso (seasonId,provider,channelId)→nationId; si el canal no está vinculado o la autorización no vale, DROP/QUARANTINE y motivo auditado.
- Reintentos no crean un segundo ciudadano/voto; nombres visibles no identifican al usuario. Cambios de alias no crean otra cuenta.
- Mismo espectador en dos canales de dos naciones puede crear dos ciudadanos conforme a la regla histórica. No se promete deduplicación transversal entre Twitch y YouTube.
- Acciones son visibles solo en la salida correspondiente según las políticas de proveedor; los resultados de juego agregados se pueden publicar si están permitidos. Nunca reenviar chat crudo cruzado por defecto.

### 8. Fallos y recuperación

| Incidencia | Estado competitivo | UX de los tres overlays |
|---|---|---|
| OBS de A cae | No altera LIVE provider de A ni estado lógico | A reconnect + snapshot; B/C siguen |
| Chat provider de B cae | Se desactiva entrada B, health a UNCERTAIN si afecta reloj | B muestra chat indisponible; votos B congelados; C/A siguen |
| Emisión B termina confirmada | B OFFLINE y 20 % economía; sin avanzar era | Torneo global se congela/cancela |
| Backend reinicia | No se simula durante interrupción sin secuencias; catch-up auditado | Tres pantallas RECOVERING/read-only; reanudan desde snapshot |
| Caída de PostgreSQL | Prohibidas mutaciones sin commit | SAFE_SCENE con último estado confirmado y timestamp visible |
| Token del overlay filtrado | No altera competición, permite leer solo output | Revocar y rotar; sesiones previas caducan |
| Token del proveedor revocado | Deshabilitar capability afectada; jamás usar scraper de sustitución | Mensaje de error solo para su streamer |
| Dos naciones a Interestelar simultáneo | Arbiter global serializa ganador en DB | Todos reciben UN solo ganador y mismo resultId |

### 9. Escalabilidad progresiva

Fase 1: un proceso .NET API+Worker, una PostgreSQL, un hostname HTTPS, SignalR y workers adaptadores dentro del mismo despliegue. Fase 2: separar ConnectorWorker y SimulationWorker por carga conservando transacciones y single-writer. Fase 3: multi-campaign multi-tenant físico solo si hay monetización de licencia y necesidad medida; no adelantar billing, Kubernetes, Redis o colas.

**Presupuesto de límites candidato:** 3 naciones y 3–9 bindings por temporada; objetivo 30 FPS overlay (no garantizado); input y estado observables desde un panel único. Medir perf con 3 PCs reales + distintos proveedores antes de PUBLIC_READY.

### 10. Aceptación vinculante

- MS-01: 3 PC/redes distintas, mismo proveedor, A/B/C controlan una sola nación cada uno; ninguna máquina hospeda el motor.
- MS-02: 3 proveedores, cada uno autorizado; no cruces de chat ni IDs ni votos.
- MS-03: caída de A OBS mientras Twitch A sigue LIVE no pausa economía A ni votaciones de A.
- MS-04: un LIVE deja de estar confirmado durante RPS: tiempo restante idéntico en A/B/C y sin sanción espuria.
- MS-05: misma seed/inputs, tres overlays desconectados y reconectados: mismo hash lógico de temporada.
- MS-06: invitación caducada/reutilizada, rol sin permisos, token revocado → rechazados sin fuga.
- MS-07: cambio de binding al pausar preserva ciudadanos existentes y no duplica eventos.
- MS-08: reinicio de backend/DB no produce ganador doble ni paga dos veces.


---

## Fuente 64 — `docs/64_RELOJES_EVENTOS_Y_CONTRATOS_v2.3.md`

**Blob original:** `5b235a5abfcd4923dbb2c72c189f1f39c5b2a017`.

## 64 — Contratos de reloj, sincronización y API multistreamer (v2.3)

**Normativo para nuevos componentes y corrección de docs 03,19,42,55.** Contratos de referencia, aún no compilados ni validados contra código. Ninguna marca de tiempo aportada por el cliente OBS es autoridad.

### 1. Relojes y semántica

| Reloj | Avance | Uso |
|---|---|---|
| UTC | Tiempo físico confiable | Expiración de ciudadanía, OAuth, periodos de misión, timestamp |
| NationLiveClock[n] | Incrementa solo con proveedor de nación n en LIVE_CONFIRMED | Elección, prioridad, Consejo y ceremonia de transición |
| NationEconomyClock[n] | 1 s/s LIVE, 0.2 s/s OFFLINE o UNCERTAIN | Producción, comida, obra, conocimiento, XP |
| CompetitionLiveClock[event] | 1 s/s solo cuando **los tres** LIVE_CONFIRMED y evento RUNNING | RPS, descansos y batallas programadas |
| SeasonSequence | Contador global persistido en commit | Arbitraje de maravilla/ganador y publicación |
| PresentationClock | Animación en clientes | Sin decisiones lógicas, reiniciable |

OFFLINE y UNCERTAIN no otorgan tiempo de voto ni progreso de competición; para economía ambos aplican perfil conservador 0.2. El periodo UTC de misión no es live ni economy. Dos viewers de la misma nación nunca suman LIVE por estar ambos conectados.

### 2. Orden canónico y partición exacta

Entrada/evento almacena receivedUtc del servidor, ingestSeq monotónico, sourceKey único, bindingRevision y providerEventId. Para reproducibilidad una ventana se decide por **tiempo acumulado LIVE** y secuencia de recepción, no por comparar contra una fecha de cierre UTC calculada al abrir (puede detenerse durante horas).

Cada avance de simulación de 5 s procesa [lastCommittedUtc, targetUtc) en subsegmentos determinados por: cambios certificados LIVE, recepción de comando persistido, activación/caducidad de humano, expiración de voto en segundos LIVE, finalización de obra/tecnología y fin de período UTC. Las entradas exactamente en un límite pertenecen al subsegmento posterior. Los comandos se aceptan solo si su instante es anterior al límite de cierre expresado como LiveClock acumulado; en el límite exacto se rechazan.

En cada subsegmento se aplica orden:
1. Validación de entrada, deduplicación, binding y capacidad; ordenar ingestSeq; leer cambios de estado LIVE con timestamp efectivo certificado.
2. Procesar comandos de ciudadanía/activación y papeletas elegibles que llegaron antes del límite; registrar respuesta de aceptación/rechazo idempotente.
3. Resolver cierres de votos y eventos cuyo reloj alcanza duración. Consumir reservas y registrar resultados políticos con estado final; ningún resultado se emite antes de commit.
4. Aplicar gasto de alimentación, hambre, producción, XP, límites de almacén y trabajo mediante delta economy derivado **una sola vez**.
5. Aplicar planificador/construcción/investigación y recompensas de misión válidas.
6. Reconocer cinco hitos exactos y marcar EraReadyPending; avanzar era si nación LIVE y no ha terminado temporada.
7. Arbitrar primera entrada Interestelar / maravilla con una transacción de temporada y SeasonSequence único.
8. Persistir deltas, ledger, outbox y checksum; publicar después de commit. El renderer jamás ejecuta este orden.

**Prohibición de doble offline:** effectiveEconomyDeltaMs = wallDeltaMs × (10000 o 2000)/10000, usando entero y resto persistido. Las fórmulas posteriores toman effectiveEconomyDeltaMs sin volver a multiplicar 2000bp. Igual regla para XP de trabajo y consumo. No usar floats para estado persistido.

**Ack ≠ progreso económico:** el ingreso de comando puede producir un ACK persistido rápido; su efecto productivo se contabiliza en el segmento que corresponde al siguiente ciclo de economía. SLO <1 s aplica a ACK P95 cuando la infraestructura lo demuestre; la aplicación a producción puede tardar hasta el siguiente tick de 5 s. Ninguna promesa de <1 s para mutación económica con tick 5 s.

### 3. Estados de sesión

- Season: DRAFT→PREPARED→RUNNING→COMPLETED→ARCHIVED, con PAUSED/RECOVERY_REQUIRED/ABORTED por gestión; COMPLETE no vuelve a RUNNING.
- Binding: INVITED→PENDING_AUTH→AUTHORIZED→HEALTHY, con DEGRADED / REVOKED / DISABLED; no se etiqueta HEALTHY sin prueba real.
- ProviderLive: OFFLINE_CONFIRMED, LIVE_CONFIRMED, UNCERTAIN. Estado separado de OBS_CONNECTED / OBS_DISCONNECTED.
- Vote: QUEUED, OPEN, PAUSED, RESOLVED, CANCELLED, PAYMENT_BLOCKED. PAUSED no pierde ballot ni elapsedLiveSeconds; un cierre terminal se aplica UNA vez.
- Competition: SCHEDULED→WAITING_FOR_ALL_LIVE→RUNNING→PAUSED→RUNNING/ CANCELLED→RESOLVED. Pause congela CompetitionLiveClock para todas las naciones.
- Overlay: CONNECTING→SYNCING→LIVE_VIEW→STALE/RECONNECTING→SYNCING; tras TTL sin fuente válida muestra SAFE_SCENE, nunca inventa un ganador.
- Contribution: todo desactivado de inicio; RECEIVED→AUTHENTICATED→VERIFIED→CREDITED/REJECTED→REVERSED, solo evidencias y reversos autorizados.

**Elección terminada y era final misma ventana:** el cierre político válido se confirma antes de la transición si su límite LIVE se alcanza primero o en ese mismo subsegmento; después de SeasonCompleted no puede abrirse un voto nuevo. Guardar siempre orden de eventos y resultado; nunca alterar un ganador ya registrado.

### 4. IDs, orden y autenticación de eventos

- NationId es UUID inmutable dentro de Season; FactionId es string estable para assets/etiqueta. No usar FactionId como FK de movimientos.
- ChannelBinding único por (seasonId,provider,providerChannelId). Cambiar propietario del binding exige revisión auditada y nunca reusar eventos anteriores.
- sourceKey = SHA256(provider + channelId + immutableExternalEventId + eventType + immutableBindingIdentity), sin usar alias visible. BindingRevision no cambia esta clave para el mismo evento.
- Los eventos externos se autentican según proveedor, se aceptan at-least-once y se deduplican antes de aplicar; si el proveedor carece de ID estable, QUARANTINE hasta un algoritmo documentado específico de ese adaptador, no deduplicación por texto del chat.
- La marca receivedUtc de recepción es del servidor y debe preservarse en replay; providerTimestamp sirve para comprobación de tolerancia y diagnóstico.
- Un evento con identidad/nación incongruente, token revocado, input atrasado fuera de tolerancia o ventana terminada queda REJECTED/QUARANTINED con código estable.

### 5. API pública y privada propuesta

La configuración de creación de Season incluye broadcastMode=SINGLE_OPERATOR|MULTI_STREAMER. PREPARED rechaza MULTI_STREAMER si no hay tres primarios aceptados y distintos, junto con los tres bindings verificados. La API base histórica es /api/v2. Las siguientes rutas amplían ese contrato; se consolidarán en un OpenAPI operativo generado a partir de DTO .NET antes de implementación.

| Endpoint | Actor | Comportamiento |
|---|---|---|
| POST /api/v2/operator/campaigns/{campaignId}/seasons/{seasonId}/invites | OWNER | Crea enlace de invitación one-use, expirable, con nationId y rol |
| POST /api/v2/me/invites/{inviteId}/accept | STREAMER autenticado | Acepta y crea asiento/binding pendiente de OAuth |
| POST /api/v2/me/provider-connections/{provider}/authorize | STREAMER | Inicia OAuth/OIDC con PKCE cuando proveedor permita |
| GET /api/v2/me/campaign-seats | STREAMER | Sus temporadas, permisos, canal y estado de conexión |
| PUT /api/v2/operator/seasons/{seasonId}/bindings | OWNER | Revisión ETag y validación de unicidad, durante RUNNING solo pausa auditada |
| GET /api/v2/public/seasons/{seasonId}/nations/{nationId}/snapshot | Overlay autorizado | Estado público filtrado, sequence y stateHash |
| GET /api/v2/public/seasons/{seasonId}/nations/{nationId}/deltas?afterSequence=N | Overlay autorizado | Deltas contiguos o 409 SNAPSHOT_REQUIRED |
| POST /api/v2/overlay/{outputId}/session | Overlay read-only | Intercambia secreto revocable por sesión de lectura corta |
| POST /api/v2/operator/seasons/{seasonId}/actions | OWNER/OPERATOR | Start/pause/cancel event con Idempotency-Key |
| GET /api/v2/operator/seasons/{seasonId}/health | OWNER/OPERATOR | Tres proveedores, reloj, lag, overlay, inbox, errores |
| GET /api/v2/public/seasons/{seasonId}/competition | Overlay autorizado | Estado de evento y CompetitionLiveSeconds restante |

Autenticación: JWT/OIDC del usuario K0 para panel; scope por campaña/temporada/rol; token de overlay solo READ_OUTPUT para outputId; OAuth de proveedores se guarda exclusivamente en backend cifrado. Control CSRF para cookies, rate limits por cuenta/canal/IP, MFA para OWNER/OPERATOR en operaciones críticas. Un stream key de proveedor no es token de overlay. Nunca escribir tokens en logs.

### 6. SignalR / transporte de proyecciones

Grupos filtrados por autorización:
- season:{seasonId}:public-summary (estadística autorizada de tres facciones).
- season:{seasonId}:nation:{nationId}:public (mundo propio).
- output:{outputId}:presentation (cues/escenas específicas).
- season:{seasonId}:operator (solo panel autorizado).

Envelope fijo (schema en contracts/multistreamer.v2.3.schema.json):
- schemaVersion, seasonId, nationId o globalScope, sequence global, nationSequence, eventId, emittedAtUtc, type, payload, stateHash, rulesetHash y contentHash.
- Cues artísticos llevan cueId, scene, audienceScope, authoritativeEventSequence, presentationAtUtc, expiresAtUtc.
- Secuencia por commit y outbox, no instante de render. El cliente exige continuidad; gaps → snapshot + resubscription. Evento vencido se ignora visualmente, nunca se aplica otra vez.

No se difunde chat crudo, identidad de cuenta ni aportación financiera en grupos públicos. Publicar una síntesis de tres naciones no autoriza redistribuir mensajes ajenos.

### 7. Contrato de sincronización visual

Después de un evento persistido, el ShowDirector emite cue opcional con presentationAtUtc >= commitUtc + margen de presentación (baseline 3 segundos sujeto a pruebas). Cada overlay estima offset de reloj contra servidor y prepara animación. Las escenas pueden comenzar ligeramente desfasadas por latencia entre PCs: **la consistencia de resultado, no la simultaneidad exacta de fotogramas, es requisito competitivo**. Si el cue llega después de expiresAtUtc, mostrar estado actualizado sin una transición cinematográfica obsoleta. K-0 puede narrar localmente o consumir TTS caché compartida; TTS fallido nunca bloquea votos.

### 8. Recuperación, presión y semántica de entrega

- Webhooks EventSub: verificar firma y challenge; HTTP 2xx solo tras Inbox duradera. Nunca DB mutation en handler público.
- Proveedor con stream/poll: persistir cursor, token y última posición segura; no inventar mensajes perdidos que el proveedor no garantice recuperar.
- Outbox se reintenta at-least-once; overlay deduplica por (eventId,sequence).
- Si hay retraso de proyección, compactar en snapshots; nunca acumular miles de sprites/eventos narrativos caducados.
- Backend interrumpido: al reiniciar, usar snapshots + Inbox/Outbox + segments; <=7 días catch-up auditable de economía, sin avances de era offline; >7 días RECOVERY_REQUIRED y decisión de operador, tal como docs 03.
- Single writer por nación con fencing token; no simular en dos workers durante failover.

**ContentHash del diseño:** los archivos versionados que participan en el hash se enumeran en [content_manifest.v2.3.json](../data/content_manifest.v2.3.json). Cada temporada congela archivo, manifest digest, rulesetHash, seed y engineVersion; no recalcularlos con datos actuales tras una migración. Los digests aún no se han compilado.

### 9. Escenarios de prueba obligatorios

SYNC-01 voto 1 ms antes del deadline LIVE aceptado, exactamente deadline rechazado; SYNC-02 desconectar LIVE B durante voto y mantener segundos restantes; SYNC-03 RPS con B caído conserva mismo reloj A/B/C; SYNC-04 60s offline equivalen a 12s economía (sin doble factor); SYNC-05 2 workers con lease vencida no duplican trabajo; SYNC-06 Outbox duplicada no repite ganador/compra; SYNC-07 tres overlays con distintas latencias alcanzan mismo stateHash; SYNC-08 dos Interestelar simultáneas → ganador único; SYNC-09 reconexión con hueco de sequence fuerza snapshot; SYNC-10 caducidad de OAuth deshabilita solo las capacidades dependientes, sin cambiar nación.

**No afirmamos que estas pruebas estén ejecutadas.** Cada caso requiere commit de implementación y evidencia reproducible.

