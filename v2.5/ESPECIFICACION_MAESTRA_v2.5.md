# K0: The Experiment / Project CHAOS — Especificación maestra unificada v2.5

**Fecha de consolidación:** 2026-11-08.  
**Clase:** diseño normativo consolidado para implementar el videojuego y producir su arte.  
**Estado verificable:** DESIGN_BASELINE / NO IMPLEMENTADO / NO CERTIFICADO PARA LIVE PÚBLICO.  
**Alcance:** reglas de juego, identidad, arte, UX, contenido, operadores, multistreamer, integraciones, motor, datos, seguridad, negocio y validación.

> Esta versión **no abre una nueva ronda de decisiones ni incorpora mecánicas arbitrarias**. Concilia decisiones de usuario 1–92, las correcciones v2.0–v2.2, la arquitectura multistreamer v2.3 y los catálogos existentes. Cuando una decisión histórica fue sustituida, **la v2.5 identifica expresamente su reemplazo**. Las propuestas de balance y los requisitos externos se mantienen como tales; documentar no significa ejecutar o aprobar.

## 0. Cómo leer y desarrollar a partir de v2.5

Esta es la **única entrada normativa**. Los archivos del directorio [fuentes](fuentes/) reproducen **íntegros** los 67 capítulos anteriores y las 92 decisiones para preservar toda la información. Son trazabilidad histórica, no 67 autoridades simultáneas. Las tablas numéricas, definiciones exactas de edificios, tecnologías, profesiones, hitos, misiones, NPC, unidades, sprites y eventos permanecen en los JSON de [data](../data/); sus identificadores y números son autoridad estructurada mientras no contradigan una enmienda documentada en este archivo. API/SQL de [contracts](../contracts/) y [architecture](../architecture/) son **diseños**, no contratos compilados o migraciones ejecutadas.

**Orden de prevalencia:**

1. Instrucciones explícitas posteriores del propietario, trazadas en revisión versionada.
2. Esta especificación v2.5 en los conflictos que resuelve expresamente y sus [enmiendas](REGISTRO_DE_CONSOLIDACION_v2.5.md).
3. Decisiones confirmadas 1–92 que no estén expresamente sustituidas.
4. Catálogos estructurados activos (costes, IDs, valores, cantidades) y contratos asociados, validados por versión.
5. Capítulos 01–67 preservados como fuente histórica y de detalle artístico/técnico no contradicho.
6. Ejemplos ilustrativos, simulaciones simplificadas y compilaciones antiguas.

Si una mecánica necesita nuevo valor, no se inventa silenciosamente en código: se crea cambio versionado de reglas + prueba. Una temporada RUNNING fija seed, ruleset, contenido, motor y versiones de proveedor; nunca cambia retrospectivamente por editar GitHub.

## 1. Visión y experiencia de producto

**Nombre de trabajo visible:** K0: The Experiment. **Nombre histórico de desarrollo:** Project CHAOS. El juego es un **espectáculo competitivo y participativo**, no una app con tres partidas separadas sin relación: tres civilizaciones inteligentes no humanas compiten simultáneamente por alcanzar la Era Interestelar. La audiencia se une a una nación desde el chat de un canal autorizado, realiza un oficio, participa en elecciones, vota proyectos y coopera en desafíos; NPC mantienen la continuidad cuando no hay usuarios.

El presentador **Doctor K-0** es científico cyborg neutral, sarcástico y teatral. No es una mascota blanda ni sustituye las acciones del público. La carrera se representa con **pixel art retro 2D de baja resolución, proyección oblicua 2:1**. El tono es ciencia ficción cómica, evolución cultural, cooperación y rivalidad deportiva; nunca apuestas, humillación, violencia gráfica ni pay-to-win.

La nación **no equivale a plataforma**. El supuesto v0.8 que fijaba TikTok=Micelios, Twitch=Rúnicos, YouTube=Ferrinos se conserva únicamente como ejemplo histórico: hoy las naciones son independientes de proveedor, canal, idioma y equipo físico.

### 1.1 Facciones simétricas

| Facción | Biología, cultura y silueta | Gramática arquitectónica | Exclusiones |
|---|---|---|---|
| **Micelios** | Seres fungoides compactos con capuchón esporado; redes, simbiosis, tejidos | Raíces, fibras, bóvedas orgánicas, membranas y biofotones | No corales, no gelatina genérica, no mente colmena obligatoria |
| **Rúnicos** | Seres minerales poliédricos con grietas luminosas y memoria grabada | Menhires, geometrías prismáticas, cristales, resonadores | No humanos con armadura ni magia que altere estadísticas |
| **Ferrinos** | Seres biológicos con exoesqueleto ferruginoso articulado | Placas, remaches, forjas, bisagras, metal orgánico | No robots puros ni Corálidos |

**Corálidos descartados.** Las facciones tienen **idéntica economía, límites, árbol funcional, fuerza base y capacidad territorial**. Diferencias de bioma son estéticas. Prohibido conceder ventajas ocultas de madera/comida/minería/combate por especie.

## 2. Producto multistreamer distribuido — requisito fundamental

Existe **una partida central compartida** (Campaign→Season→tres Nation), no tres motores instalados en PC de streamers. Pueden competir tres creadores independientes desde equipos, redes y cuentas de la misma plataforma o de plataformas distintas:

- **SINGLE_OPERATOR:** un responsable controla las tres fuentes de chat distintas, incluso en una misma plataforma; puede usar una escena combinada.
- **MULTI_STREAMER:** tres cuentas K0 **distintas** son responsables primarias, una por nación, con invitación aceptada, canal propio y Browser Source OBS independiente. El propietario de campaña arbitra permisos, no votos/resultados. Cofundadores o cohosts pueden observar o presentar sin crear otro controlador de la nación.
- Una cuenta/canal de origen se asigna a **una única nación por temporada**. Un solo chat que controle simultáneamente las tres naciones NO es una capacidad admitida.
- Mismo proveedor, tres canales diferentes, está admitido en el **modelo** (Twitch A/B/C, YouTube A/B/C, o TikTok A/B/C únicamente si hay permiso real). También configuraciones mixtas con capacidades por cuenta verificadas.
- Los streamers no hospedan servidor, PostgreSQL, simulador ni adaptadores privados en sus equipos. Solo acceden por HTTPS/WSS al overlay y panel; nadie necesita abrir puertos entrantes.
- El backend .NET autoritativo recibe eventos de proveedor, valida identidad y binding, procesa simulación y publica snapshots/deltas/cues. El OBS local solo dibuja la vista de esa salida.
- **Que se caiga OBS/Browser Source no significa que el proveedor haya dejado de estar LIVE**. El motor continúa si existe presencia LIVE auténtica. El overlay recupera snapshot y eventos vigentes; no altera horas de trabajo ni relojes.
- Que termine el LIVE de una nación desacelera **esa** economía, congela **sus** votos/progreso de era y pausa todos los torneos compartidos que requieran tres LIVE; no desconecta B/C ni invalida sus culturas.
- Las distintas horas emitidas pueden crear **asimetría de progresión**. La regla vigente la permite (100 % LIVE / 20 % offline); no está acreditada como equilibrio perfecto. El tiempo de emisión debe ser visible y analizarse antes de lanzar.
- Un mismo espectador puede tener ciudadanos distintos si interactúa desde distintas cuentas y naciones; **no** deduplicar cuentas de Twitch y YouTube por alias. Los nombres públicos son moderados, nunca claves de identidad.
- El operador puede asignar distintas políticas de presentación por salida, pero no mezclar mensajes o avatares crudos entre plataformas sin permisos.

**Modelo de identidad:** AccountUser, CampaignMembership, StreamerSeat, ProviderConnection, ChannelBinding, ProviderLiveSession, BroadcastOutput, ViewerCitizen. NationId interno UUID; FactionId estable micelios/runicos/ferrinos. OutputId ≠ BindingId ≠ ProviderSessionId. Roles de owner/operator/broadcaster/moderator/auditor; broadcaster no puede modificar economía ni ganar la partida desde su panel.

**Flujo de alta:** campaña DRAFT → tres Nation → invitaciones de un solo uso con caducidad → aceptación por cada streamer → autorización de su canal mediante proveedor → prueba de permisos CHAT_READ y LIVE_PRESENCE independientes → seleccionar overlay vertical/horizontal y copiar URL revocable → preflight → PREPARED/RUNNING. La cuenta OAuth no se entrega a OBS.

[Diseño de referencia de entidades, fallos y sesiones](../docs/63_ARQUITECTURA_MULTISTREAMER_v2.3.md); [semántica distribuida](../docs/64_RELOJES_EVENTOS_Y_CONTRATOS_v2.3.md).

## 3. Temporadas, historia y condición de victoria

Cada temporada comienza con **cero recursos, cero edificios y 24 NPC por nación**, pero con fuentes naturales de comida, madera, piedra, conocimiento y capacidad virtual inicial suficientes para no bloquearse. Tres naciones arrancan bajo el mismo ruleset/seed de temporada y simetría económica; mapas independientes con terreno igualmente utilizable.

**13 eras previstas, 12 jugables y una terminal:** Paleolítico, Neolítico, Cobre, Bronce, Hierro, Antigüedad, Edad Media, Renacimiento, Industrial, Moderna, Digital, Espacial, **Interestelar**. La primera nación que confirma en el estado autoritativo la **entrada** en Interestelar gana; no exige jugar un ciclo de edificios, hitos, investigación, Consejo o elección interestelar. El contenido de era 13 que sigue apareciendo en catálogos se preserva como **epílogo artístico/histórico**, no desbloqueo jugable tras terminar. Único ganador global persistido por transacción/sequence; si dos llegan simultáneamente, orden de commit global y clave de nación definen un único ganador, con finalista registrado si procede.

Cada era 1–12 se completa por **cinco hitos distintos de 20 puntos cada uno**: producción acumulada de alimento, producción de madera Y piedra, conocimiento con tecnología troncal completada, edificio cívico representativo completado y **misión colectiva de esa era**. Todos suman 100, se registran una sola vez, y el oro nunca concede puntos. Si se llega a 100 mientras no existe LIVE confirmado, se marca EraReadyPending; el cambio de era espera próximo LIVE. No desbloquear por una barra repetible, misión diaria duplicada o aportación económica.

**Tecnologías:** 39 definiciones (troncal + opción económica + opción defensiva por era conceptual). Los talleres y centros de investigación de una era requieren la tecnología troncal de su era; conocimiento empieza en fuente natural para evitar ciclo. Las opcionales son gratuitas en oro y tienen pequeños bonuses acotados definidos en catálogo. Identificadores numéricos y prerrequisitos exactos: [tecnologías](../data/technologies.v2.json), [hitos](../data/milestones.v2.json), [eras](../data/eras.v2.json).

**Misiones:** tres tipos diarios y dos semanales siguen en ciclos UTC para recompensas ordinarias; no vuelven a dar puntos históricos por repetición. Para cada era 1–12 hay una **misión propia** (12 instancias posibles), completada por trabajo productivo real de NPC/humanos en esa era, independiente del corte diario; diseñada para que cero espectadores no bloquee el progreso. Objetivos del catálogo de misiones son **candidatos de balance**, no resultados simulados.

Al cerrar temporada se conservan historial, estadísticas, logros, memoria narrativa y prestigio cosmético; se reinician saldos ordinarios, nivel, habilidades y economía competitiva para la siguiente. No hay importación de ventajas desde el campeón anterior. No hay muerte permanente de ciudadano.

## 4. Ciudadanos, trabajo, habilidades y NPC

Un ciudadano nace con !join, sin oficio. !work [food|wood|mine|build|research] fija un **único oficio para la temporada** y activa 2 h de trabajo; !active o repetir el mismo !work renueva la ventana de 7200 segundos de reloj UTC después de un cooldown de 60 s, nunca suma dos horas acumuladas. Chat casual, likes y ver el vídeo no producen trabajo. Al caducar la ventana, el ciudadano descansa, conserva su identidad, puede votar válidamente si está registrado y puede reactivarse en un directo posterior. Cambiar a otro oficio rechaza PROFESSION_LOCKED y no renueva.

| Familia lógica | Recursos o actividad | Evolución |
|---|---|---|
| food | alimento | Cazador → agricultura y síntesis en eras futuras |
| wood | madera/biomasa | Recolector → ingeniero de biomasa |
| mine | piedra y mineral desde era 3 | Tallador → extractor de mineral avanzado |
| build | trabajo de construcción, no recurso almacenable de libre venta | Constructores progresivamente tecnificados |
| research | conocimiento que avanza investigaciones | Explorador → científico de tecnología avanzada |

El oficio cambia **nombre, ropa, herramienta y acciones visuales** con era, pero no su ID ni XP. Niveles 1–20 con umbrales XP acumulada 250×(nivel−1)²; trabajo efectivo aporta 6 XP por minuto-trabajador efectivo con restos enteros persistentes. Tres elecciones de habilidad en niveles 3, 7 y 12, con dos alternativas por bifurcación y un máximo personal de +1800 basis points de bonus; no se autoelige si el ciudadano no usa !skill. Las habilidades son personales, no auras globales multiplicables por audiencia. Los NPC no suben de nivel, no obtienen habilidades ni generan votos ficticios.

Los 24 NPC iniciales se distribuyen 7 comida, 5 madera, 4 minería, 4 obras y 4 ciencia. Cap NPC de nación 120; crecimiento candidato +2 por era y +1 por cuatro horas LIVE si comida/vivienda lo permiten. Usuarios humanos permitidos hasta 100 000 registrados y productividad marginal escalonada: primeros 100 activos por oficio al 100 %, siguientes hasta 2500 por oficio/nación al 25 %, más allá solo representación/participación según reglas de XP reales. Es **balance candidato**; no asegurar equidad a gran escala sin simulaciones. LOD de sprites desacoplado de población: que haya 10k ciudadanos no implica 10k agentes visuales.

Comandos de ciudadano y política exacta: [capítulo 06](../docs/06_PROFESIONES_HABILIDADES_Y_XP.md), [catálogos](../data/professions.v2.json) y [skills](../data/skills.v2.json).

## 5. Relojes, simulación determinista y orden

Motor autoritativo con **tick económico base de 5 s**, enteros BIGINT milésimas y porcentajes en basis points (10000=100 %), RNG determinista por hash+contador; no usar floats ni Math.random para estado competitivo.

| Reloj | Qué mide | En desconexión |
|---|---|---|
| UtcWallClock | timestamps, actividad dos horas, periodos diarios/semanales | continúa |
| NationEconomyClock por nación | producción, comida, obras, investigación y XP | 100 % LIVE / 20 % OFFLINE o UNCERTAIN |
| NationLiveClock por nación | elección, prioridad, Consejo, transición de era | congelado sin LIVE confirmado |
| CompetitionLiveClock global por evento | RPS y batalla programada con A, B y C | congelado si una nación no LIVE |
| SeasonSequence y global arbiter | orden total de commits, primer ganador y maravillas | no depende de frames |
| PresentationClock por salida | sprites, cámara, animación, cues y subtítulos | puede avanzar, nunca muta recursos |

**Regla contra doble penalización offline:** para un intervalo real se calcula una sola vez deltaEconomy = deltaUTC × 1 o × 0.2, con residuo persistido. Producción, alimento, XP y trabajo consumen ese delta ya ralentizado; ninguna fórmula posterior vuelve a multiplicar por 0.2. Pausas por incertidumbre de proveedor nunca se maquillan como LIVE.

**Orden por subsegmento:** (1) entrada autenticada y deduplicación/estado LIVE; (2) comandos y papeletas anteriores a su frontera de cierre; (3) resolver cierre de votaciones/torneos; (4) alimento, hambre, producción, XP; (5) construcción, investigación y misiones; (6) hitos y transición de era; (7) arbitraje global ganador/maravilla; (8) commit de ledger, estado y Outbox, y publicación después. Un evento exactamente en frontera de cierre se rechaza; clocks LIVE pausables no usan una hora UTC absoluta ficticia. Dividir tick por fronteras de recepción/estado mantiene replay y permite ACK antes de siguiente producción económica.

**Competiciones entre tres directos** deben utilizar reloj COMPARTIDO: si B se desconecta en una ronda faltando 50 s, A/B/C conservarán 50 s, y la ronda se reanudará/cancelará según operación auditada sin puntuaciones ficticias. Tener OBS abierto sin LIVE no valida reloj.

**Objetivos SLO propuestos (NO medidos):** recepción→ACK P95 menor que 1 s, delta visual P95 menor que 2 s, tick CPU objetivo 50 ms por nación en carga de referencia, render 30 FPS. Mutaciones de recursos pueden tardar hasta siguiente tick de 5 s; no prometer P95 <1 s para la economía con esa cadencia.

## 6. Economía, recursos, hambre, almacenes y producción

Recursos ordinarios: alimento (food), madera (wood), piedra (stone), mineral (ore desde era 3), conocimiento (knowledge), además de buildWork como acumulador de obra y oro como subledger separado. **Ningún recurso ordinario ni oro puede quedar negativo.**

Producción base por trabajador y minuto de economía (unidades): alimento 2,4; madera 1,8; piedra 1,4; mineral 0,65; conocimiento 1,2; trabajo de obra 1,2. El minero divide 75 % piedra / 25 % mineral desde era 3. La población consume 0,15 alimento por NPC/minuto efectivo, más humanos efectivos con máximo 50 unidades humanas de mantenimiento. Sin comida suficiente la productividad del segmento cae al 65 %; no se mata ni borra ciudadanos. Almacenes iniciales: 3500 unidades por recurso ordinario salvo conocimiento 15000; storage añade 1500 y escala con eras conforme a catálogo. Capacidad llena bloquea producción y registra blockedByCapacity; NPC se reasignan a trabajos útiles, humanos mantienen oficio y no ganan XP inexistente.

Gobiernos, prioridades, habilidades y edificios dan bonuses sobre fórmulas en basis points. El techo compuesto final +50 % (15000bp), bonos de infraestructura +3000bp y habilidades individuales +1800bp se aplican en orden fijo, sin explotar auras de 10000 usuarios. El balance debe calibrarse sin aumentar linealmente la potencia de comunidades mayores.

El resource ledger es auditable y causa-idempotente. Producción, comida, obras, misiones, daños y correcciones generan entradas atómicas; retención/compensación no borra historia. Oro no entra en fórmulas de recursos, ciencia, defensa, progreso, votos ni prioridad.

[Reglas numéricas](../data/ruleset.v2.json), [economía de referencia](../docs/04_ECONOMIA_Y_BALANCE.md) y [evaluación del balance](../docs/56_MODELO_DE_BALANCE_Y_PRUEBAS_NUMERICAS_v2.2.md).

## 7. Mapas, edificios y Consejo

**Mundo procedural estable por nación**: semilla versionada, mapa inicial 48×48 tiles lógicos, proyección visual 32×16, margen de expansión 8 tiles por era, máximo 256×256; al menos 70 % de terreno utilizable, fuentes naturales obligatorias garantizadas y ninguna ventaja estadística de bioma. Orden de parcela determinista por cercanía al núcleo, coordenadas y desempate estable. Animación y pathfinding gráfico jamás deciden producción. Persisten edificios antiguos, reduciendo eficiencia relativa a 80 % cuando corresponde.

**130 edificios básicos** = 10 familias×13 eras conceptuales: housing, food_production, forestry, extraction, workshop, research, storage, infrastructure, civic, defense. Los edificios de era 13 son catálogo ceremonial no jugable. Coste ordinario y trabajo propios, footprint, cuatro fases de obra, tope de instancias y efectos declarados por ID en [data/buildings.v2.json](../data/buildings.v2.json). Básicos se planifican automáticamente cada 60 s de economía o por avance de era: como máximo 2 autoqueued, 5 obras concurrentes y orden de necesidades alimento→almacén→vivienda→materias→ciencia→taller→cívico→defensa→infraestructura. Los bloqueos por falta de materiales/parcela se mantienen como estados visibles sin recursos sintéticos ni doble pago.

**Consejo Estratégico**: 39 proyectos = tres por era conceptual, 12 ternas jugables. **Un Consejo por nación y era jugable** cuando las tres alternativas actuales no construidas y desbloqueadas son cada una costeable con recursos ordinarios; si no, esperar recursos. Voto público !build projectId por 600 segundos LIVE, última papeleta válida por ciudadano; empate/sin votos resuelto por RNG determinista auditado. Durante votación se reserva **componente a componente el máximo** de los tres vectores de coste, nunca la suma de los tres; al cerrar solo se consume el coste del ganador, una vez, y se libera sobrante. Las alternativas perdedoras no se reofertan en el mismo Consejo/era. **Oro=0** para todos estos proyectos desde revisión v2.2. Nunca bloquear participación a quien no dona.

**Maravillas**: 13 definiciones conceptuales, una por era, con primera finalización global única y reconocimiento prestigioso. Coste ordinario oro=0, festival programado/condición válida, sin acelerar por donación; la maravilla interestelar es epílogo. Un único commit obtiene claim; rivales pueden mantener su construcción como monumento si la regla lo permite, sin premio exclusivo. Entre temporadas historial del récord se conserva, no ventaja competitiva.

[Obras y sus valores](../data/strategic_projects.v2.json), [reglas gratuitas](../docs/44_CONSEJO_GRATUITO_PATROCINIO_Y_ECONOMIA_v2.2.md).

## 8. Gobierno, elecciones, prioridades y torneos

**Gobernantes NPC, no espectadores**: cada facción posee tres candidatos recurrentes: económica, militar, científica, con apariencia que cambia de era; un solo gobernante por nación durante cada era 1–12. Nombres canónicos según catálogo: Micelios **Morga, Bruk, Espora**; Rúnicos **Dorrik, Kraag, Zyn**; Ferrinos **Nera, Rokka, Neri** (orden economía, militar, ciencia). No hay alcalde/general/científico espectadores elegidos simultáneamente; no hay poder ejecutivo para anular votaciones.

La elección de gobierno comienza en era 1 con LIVE y en las sucesivas eras jugables, dura **3600 segundos LIVE**. Todos los ciudadanos registrados pueden votar por !gov economy|military|science aunque estén descansando; última opción válida antes de cierre sustituye anterior. Empate por máximo → segunda vuelta 180 s LIVE solo entre empatados; empate persistente → sorteo uniforme RNG, sin votos → sorteo uniforme de tres. Bonos durante la era desde resolución: economía +3 % recursos, ciencia +3 % conocimiento, militar +5 % a defensa de combate automático, NO RPS.

Tras elección, votación separada de prioridad !priority economy|science|defense durante 300 s LIVE; bonus +8 % a su ámbito por 5400 s LIVE, no concede puntos históricos, se interrumpe al iniciar nueva era. Sin votos → rotación reproducible; empate → RNG entre empatados. No solapar elección, prioridad y Consejo dentro de nación.

**RPS triangular programado**: con tres naciones LIVE confirmadas, 5 rondas ordinarias de 90 s de voto por ronda y descansos de 30 s COMPETITION LIVE, hasta 2 rondas extra si empate por cabeza. Cada ciudadano puede usar !rps rock|paper|scissors una sola vez de manera irrevocable por ronda. Se elige jugada mayoritaria de cada nación, con RNG para empate interno. Sin votos = PASS, jamás un voto ficticio de NPC. Contra cada rival se asignan 2 victoria / 1 empate / 0 derrota; tres elecciones distintas crean el ciclo A>B>C>A con 2 puntos por nación, NO un ganador inventado. Empate global al final de extra rounds = vencedores compartidos sin sanciones. Recuento por población no multiplica puntos.

**Sanciones limitadas:** solo ganador único puede penalizar naciones por debajo; pérdida hasta 2 % de madera y piedra **disponibles**, sector secundario de máximo 10 % output bloqueado durante 1800 s de LIVE propio. No quitar alimentos esenciales, oro, XP, edificios o ciudadanos. Penalizaciones simultáneas se consolidan sin doble impacto.

**Batallas automáticas programadas**: defensas generan hasta 6 unidades por edificio, máximo 120/nación; hasta una cada 1200 s LIVE (no offline), roles guardia/explorador/especialista equivalentes entre facciones (100/85/115 %). Base por unidad según era e: 10+2e, truncado entero tras multiplicador de rol. Torneo no más de uno por 24h LIVE de campaña; requiere tres LIVE, edificio defensivo y diferencia máxima de dos eras o se pospone. Tres encuentros A-B, B-C, C-A, suma de fuerza y bonos defensivos, sin azar; 2/1/0 puntos; no muertes permanentes ni ataques libres. Penalización nunca se duplica con la de RPS. Su render teatral es cosmético, no un RTS táctico.

**Otros eventos permitidos:** desafío de remontada (retraso≥2 eras, máximo 2/temporada, NPC +5 % durante 30 min LIVE), tormenta moderada de recursos, desfile de fauna cosmético y festival de maravillas. Requieren whitelist, anuncio y cooldown; no hay depredadores permanentes ni desastres espontáneos fuera de director autorizado. Sin alianzas entre naciones.

[Gobiernos](../data/governments.v2.json), [eventos](../data/events.v2.json), [combate](../data/combat_units.v2.2.json).

## 9. Oro, aportaciones y monetización

**Oro solo desde aportación real autenticada y verificada si el proveedor permite el evento concreto**, nunca desde chat, likes, NPC, trabajo, evento demo o escritura del operador. **Adquisición desactivada por defecto**. Los históricos v0.8/v2.0 que lo requerían en proyectos estratégicos quedan **sustituidos**: Consejo y maravillas ordinarios son 100 % gratuitos respecto a oro, incluso con 0 donaciones.

Reconocimientos opcionales no competitivos con precios de diseño en oro interno: insignia 25, placa 100, dedicatoria ceremonial 250, sujetos a moderación y consentimiento para nombre público. Ningún pago altera probabilidades de evento, visibilidad competitiva, velocidad histórica, defensa ni votos. Conversión de regalos a oro exige tasa y permisos aprobados por proveedor/cuenta, no equiparar importes entre TikTok/Twitch/YouTube ni inventar euros. Reversos crean compensación/deuda trazable, nunca saldo negativo o eliminación del asiento. Si monetización deshabilitada, tampoco se ofrecen compras de reconocimientos.

El ingreso para el creador/empresa es distinto al oro del juego. Una futura licencia SaaS para otros streamers se evaluará después de medir retención, coste operativo, permisos, derechos y demanda; no requiere multi-tenant/billing en MVP.

## 10. Dirección artística, sprites, mundo y UI

**Estilo obligatorio:** low-res retro 2D pixel art, suelo oblicuo 2:1, tile 32×16, sprite ciudadano base 16×24, 4 direcciones NE/SE/SW/NW, escalado entero sin smoothing, paleta ideal máxima de 24 colores por sprite. Terreno y objetos usan profundidad/pivote compartido; efectos, luces y alturas decorativas sin colisión económica. La referencia a Terraria define legibilidad/densidad retro, **no copiar sus sprites**.

**Nueve acciones por personaje**: idle, walk, gather, haul, build, research, celebrate, rest, react; cantidad de frames y FPS por acción definidos en [art_spec](../data/art_spec.v2.json). Roles equivalentes conservan anclajes y huellas, sin ventaja perceptiva por facción. Paletas y materiales se diversifican para Micelios/Rúnicos/Ferrinos a lo largo de 13 eras; el lenguaje de cada época no necesita imitar literalmente historia humana.

**Inventario artístico conceptual:** 3×13×5 = 195 combinaciones visuales de ciudadanos, 9 gobernantes×13 atuendos=117, 130 edificios×3 facciones=390 skins, 39 estratégicos×3=117, 13 maravillas×3=39, 39 tipos/era/rol×3 skins=117 guerreros, más Doctor K-0, terrenos, partículas, iconos, retratos y sonido. Son **combinaciones de dirección artística**, no archivos producidos ni sprites aprobados. Reutilizar atlas, herramientas, paletas y rigs para controlar coste.

**Doctor K-0:** silueta inequívocamente cyborg: cabeza asimétrica, ojo óptico dominante, máscara/mandíbula mecánica, cuello cableado, torso de laboratorio reforzado, un brazo claramente cibernético, manos expresivas y botas. Sprite de mundo y retrato de HUD más detallado, sin volverse personaje distinto. Estados NEUTRAL, CURIOUS, AMUSED, WARNING, CELEBRATING, DISAPPOINTED, ERROR_SAFE. Neutral ante facciones y decisiones de voto.

**Layout de referencia vertical 360×640 lógico:** cabecera 0,0,360,90; mundo 0,90,360,422; HUD inferior 0,512,360,128; cartela de K-0 16,410,328,86 cuando no cubre un voto/resultado. **Horizontal 640×360:** mundo 0,0,467,360; HUD lateral 467,0,173,360; subtítulos 20,284,425,52. Escalado hacia 1080×1920 o 1920×1080 con safe areas reales por plataforma. LOD sugerido máximo 45 ciudadanos vertical/90 horizontal. Render/animación no modifican economía ni autoridad.

**Escenas obligatorias:** BOOT_CHECK, WORLD, GOV_VOTE, PRIORITY_VOTE, COUNCIL_VOTE, TOURNAMENT, ERA_TRANSITION, SEASON_END; en modo multistreamer también CONNECTING, MULTISTREAMER_WAITING, GLOBAL_EVENT_PAUSED, CHANNEL_REVOKED, RECOVERING, SAFE_SCENE. Output NATION_FOCUS por defecto (mi mundo + resumen público rivales), SHARED_WORLD autorizado, EVENT_STAGE y SAFE_SCENE. Distinto compositor en cada PC, mismo resultado autoritativo.

**Accesibilidad y derechos:** interfaz entendible sin chat ni audio; subtítulos y estado real LIVE/UNCERTAIN/OFFLINE; contraste y siluetas no dependen solo de color; glifos ES/EN, textos largos, tamaños móviles, licencias comerciales y control de duplicación de nombres de espectador. Capturas y style frames reales siguen pendientes de producir/aprobar.

[Manual pixel art](../docs/46_MANUAL_DE_ESTILO_PIXEL_ART_v2.2.md), [visual por eras](../docs/26_BIBLIA_VISUAL_FACCIONES_EPOCAS_Y_SILUETAS.md), [K-0](../docs/48_DOCTOR_K0_PERSONAJE_VOZ_Y_NARRACION_v2.2.md), [catálogo artístico](../docs/61_CATALOGO_ARTISTICO_DE_EDIFICIOS_Y_MARAVILLAS_v2.2.md), [NPC vestuario](../docs/62_PERSONAJES_NPC_Y_EVOLUCION_ESTETICA_v2.2.md).

## 11. Narración, audio, idiomas y ShowDirector

El ShowDirector determinista autoriza cues de gameplay por estado/evento confirmado, cooldown y prioridades. NarrationService utiliza plantillas primero; opcionalmente un LLM transforma humor/estilo **sin autoridad** para iniciar eventos, alterar resultados o interpretar chat como instrucciones. K-0 conoce hechos agregados y confirmados, no PII ni credenciales. TTS sustituible y cacheable por texto/voz, fallo seguro a subtítulos; idioma inicial es-ES, alternativa en-US cuando existan assets. Objetivo editorial: máximo una intervención prioritaria por ~20 s con cola controlada de 20; un efecto/cue narrativo caducado se omite, sin bloquear mutaciones.

Los tres outputs pueden compartir cueId y texto, pero el audio se activa/mezcla por salida para evitar ecos o redistribución de audio de terceros. Proveedor de voz, música y derechos por adquirir y comprobar. No divulgar secretos, nombres moderados indebidamente, pagos reales o votos RPS ocultos.

## 12. Integraciones LIVE y separación de capacidades

**IPlatformAdapter** normaliza eventos por origen real (provider, providerChannelId, providerUserId, providerEventId, receivedUtc servidor, digest, authorizationStatus, eventType), firma/verificación, estado LIVE, cursor/TTL, idempotencia y error. Capabilities por cuenta y binding: CHAT_READ, LIVE_PRESENCE, CHAT_WRITE, EVENTS_MONETARY, EVENTS_REVERSAL, CURSOR_RESUME, ACCOUNT_IDENTITY, OUTPUT_DISTRIBUTION_POLICY. Cada una DISABLED/PENDING_VERIFICATION/VERIFIED/REVOKED/NOT_AVAILABLE con evidencia y versión. Salidas OBS no acreditan fuente LIVE ni chat.

- **Twitch:** EventSub/chat, autenticación del canal, webhook/WS y reconexión según documentación oficial; no asumir replay perfecto.
- **YouTube:** LiveChatMessages streamList/list cuando existe canal/broadcast autorizados y cuotas suficientes; no asumir historial ilimitado.
- **TikTok:** arquitectura preparada, pero chat LIVE/monetización **bloqueados** sin permisos oficiales verificables para cada cuenta. No activar scraper no autorizado como workaround.
- **SIMULATED:** tres cuentas/sesiones ficticias para tests; no se convierten en donaciones o presencia LIVE pública.

Cuando un streamer revoca OAuth o termina su directo, deshabilitar solo sus capabilities y roles dependientes, conservar citizens/ledger/temporada y aplicar degradación correcta. Nunca publicar mensajes crudos o avatares ajenos en otro canal por defecto. Las políticas de simulcast y distribución se revisan para la configuración concreta antes de emitir.

## 13. Arquitectura de desarrollo y persistencia

**Stack de referencia congelado para prototipo:** .NET 10 C# / ASP.NET Core, monolito modular, PostgreSQL 16+ transaccional, React/TypeScript, Phaser 2D compatible con OBS CEF real, SignalR para proyecciones, HTTPS/WSS, DB central gestionada. Las propuestas iniciales de SQLite local (v0.8) están superadas por el requisito de escritura central entre streamers. Sin microservicios, RabbitMQ, Kafka, Kubernetes, Redis ni servidores por emisor en MVP.

Módulos lógicos: CampaignConfiguration, Accounts/Memberships, ProviderIngress + ConnectorWorker, IdentityAndBindings, Citizens, Economy/ResourceLedger, NationSimulation/Clocks, Buildings/Autoplanner, History/Technologies/Missions, PoliticalScheduler/Council, CompetitionEngine + SeasonArbiter, ContributionLedger, ShowDirector/Narration, ProjectionAPI/SignalR, BroadcastOutputs/OverlayAuth, OperatorConsole.

**Principios:** un escritor lógico por nación, arbitraje transaccional global para maravillas/primera entrada interestelar; Inbox deduplicada, Outbox tras commit, sourceKey estable, idempotencia por causeId; locks/versiones, fencing para múltiples workers. No guardar estado de juego en navegador OBS, usar secuencia + hash en snapshot/delta y recuperar sobre huecos. Contratos públicos de mínimo dato por stream y rutas admin separadas con RBAC/MFA. Estado SQL 001/002/003 de repositorio es modelo no migrado; se exige crear migraciones reales, integrarlas en CI y demostrar rollback/restore antes de LIVE.

**Pipeline mínimo:** validar JSON y referencias, compilar contratos tipados C#/TS, ejecutar xUnit + Testcontainers PostgreSQL, tests de simulación determinista e integración transaccional, UI Playwright, test OBS real en tres equipos, migración staging, backups cifrados, health checks, despliegue versionado y rollback seguro. SLO, RPO/RTO se registran con medidas, no con promesas. Hosting inicial central con conectores procesados en backend, coste por temporada rastreable.

## 14. Paneles, roles y experiencia real

**Propietario:** crea campaña, programa temporada, invita y asigna streamers, elige manifiesto/seed, verifica tres autorizaciones, configura política de emisión y supervisa health. No puede inventar votos, aumentar recursos arbitrariamente ni escribir oro verificado. Operador programa eventos autorizados, pausa, reanuda, silencia K-0, cambia escena segura y aborta con motivo auditado. Moderador controla contenido visible, no ledger. Auditor lee pruebas/logs. Streamer gestiona exclusivamente su output OBS y la conexión que autoriza.

**Portal del streamer remoto:** recibe invitación, entra a K0, vincula su cuenta real, verifica capacidades, previsualiza 360×640 o 640×360, copia URL read-only revocable, configura OBS y ve diagnóstico de su canal. No recibe tokens de terceros ni estado privado competitivo de rivales.

**Espectador:** lee nombre de facción, era, barra, próximos hitos, acciones disponibles, reloj/estado LIVE y escena del evento. Primer contacto muestra !join, oficio, renovación !active; votar no exige pagar ni producir. Confirmación de comando por chat es best effort según capacidad de escribir, pero el panel/Overlay tiene estado real auditado. No se muestran nombres de terceros no consentidos.

## 15. Seguridad, privacidad, recuperación y control operativo

Tokens de OAuth de proveedores cifrados en vault solo servidor; token overlay read-only revocable, preferiblemente intercambio de secreto de fragmento por sesión corta y scope outputId. OAuth con state, PKCE cuando corresponda; MFA owner/operator; scopes mínimos; webhook con firma; CSP/CSRF, rate limiting y protecciones ante prompt injection, spam y replay. Nunca subir credenciales, PII ni grabaciones no consentidas a GitHub.

Estados LIVE_CONFIRMED/OFFLINE_CONFIRMED/UNCERTAIN separados de OBS_CONNECTED/DISCONNECTED. Una interrupción puede llevar a RECOVERY_REQUIRED; no asignar segundo ganador, generar votos ficticios o dejar a streamer alternar naciones por reconexión. Si backend/DB caen, overlays muestran último snapshot confirmado con timestamp/SAFE_SCENE y luego resync. Eventos de pagos con compensación y deuda aparte; ledger append-only.

Plan de retención minimizado, derechos de usuarios y RGPD, impuestos y términos comerciales requieren revisión real en las jurisdicciones de operación. Objetivos de backup RPO 15 min y RTO 2 h citados en diseño histórico son **hipótesis**, no resultados. Restaurar base y repetir eventos con stateHash antes del lanzamiento. No operar 24/7 sin supervisión en fase piloto.

## 16. Métricas, economía de negocio y fases de desarrollo

KPIs del juego: visitante→!join, !join→oficio, activos 1/7/30 días, votos válidos, retorno entre sesiones, tiempo P10/P50/P90 por era, duración LIVE y WALL, hambre, saturación, obras/tecnologías, abandono, incidencias de proveedor, FPS de OBS, coste por hora y coste por campaña. No establecer cifras de mercado sin mediciones reales.

**Orden de ingeniería:**
1. P0 — Contratos, migraciones PostgreSQL, validación estática de datos, tests y semántica de reloj, un solo escritor.
2. P1 — Simulación local con 3 naciones sintéticas, 24 NPC cada una, primer Paleolítico con cinco hitos reales, una misión de era, construcción y Consejo gratuitos. Cero donaciones.
3. P2 — Phaser/React 2D, HUD vertical/horizontal, K-0 con plantillas y subtítulos, portal y operador, escenas básicas.
4. P3 — Tres streamers en **tres PCs/redes diferentes**, invitaciones, cuentas, autorizaciones simuladas y OBS, reconexión/fallos demostrados.
5. P4 — Eras 2–12 y epílogo, 130 edificios, facciones completas, gobiernos, eventos, RPS/guarniciones, maravillas, arte y balance completo de 0/10/100/1000/10000 ciudadanos.
6. P5 — Conector real de proveedores en cuentas verificadas, cuota, permisos, fallos, políticas cross-platform y moderación.
7. P6 — Ensayo público con rendimiento OBS real, backups restaurados, derechos de arte/audio/voz, privacidad, normas del proveedor, costes, telemetría y autorización explícita.
8. P7 — SaaS/licencias para otros creadores solo tras validar necesidad comercial/ROI, sin arrastrar multi-tenant y billing al primer producto.

**Estado actual no mejorado por esta fusión:** documentación D1 ampliada, no implementación D3 ni lanzamiento D4. El paso a D2/D3/D4 requiere evidencias de software, arte y proveedor. [Gates externos](../audit/EXTERNAL_GATES.md) y [criterios de aceptación](../docs/60_DEFINITION_OF_READY_Y_GATES_DE_CIERRE_v2.2.md).

## 17. Inventario documental, archivos fuente y reglas de versión

La carpeta [fuentes](fuentes/) contiene las **transcripciones completas** de los 67 capítulos de diseño y el registro de 92 decisiones históricas. No deben editarse como nuevas fuentes de verdad. Los 15 archivos del [content_manifest v2.3](../data/content_manifest.v2.3.json) y el catálogo de gobiernos, misiones, eventos, arte y contratos existentes siguen siendo datos de lectura y código generado; ninguna copia markdown invalida sus IDs. Un catálogo 13.ª era que exista para arte no autoriza activarlo tras SeasonCompleted. Para facilitar handoff sin omisiones, este archivo declara todas las áreas y su conexión con fuentes/JSON; los detalles artísticos y tablas grandes se leen en anexos íntegros y catálogos directamente.

**Versionado v2.5:** el presente merge publica la versión documental consolidada. No renombra migraciones históricas como si estuvieran ejecutadas, no fabrica endpoints oficiales, no genera assets y no modifica saldos/partidas reales. El nuevo baseline de referencia para desarrolladores será este archivo, seguido del registro de enmiendas y los catálogos JSON existentes. Los archivos anteriores permanecen para trazabilidad, pero su jerarquía es inferior.

**Completitud documental:** se preservan todas las fuentes localizadas en GitHub y sus decisiones históricas. **Completitud implementada o artística:** no acreditada. El alcance técnico, el diseño y los criterios de verificación están descritos, pero la inexistencia de un motor funcional o permisos LIVE impide calificar al producto como terminado.
