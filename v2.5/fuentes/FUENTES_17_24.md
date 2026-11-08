# Fuentes íntegras v2.5 — capítulos 17–24

> **Anexo de preservación literal** para no perder ninguna decisión o explicación histórica, incluidas las sustituidas. No añade normativa por sí mismo: prevalece [ESPECIFICACION_MAESTRA_v2.5](../ESPECIFICACION_MAESTRA_v2.5.md).

---

## Fuente 17 — `docs/17_OPERADOR_ESCENARIOS_Y_DIAGRAMA_E2E.md`

**Blob original:** `75c7fb27e6e7948f869cf368a2e02b63882eb86e`.

## 17 — Runbook del operador y flujos E2E

### Preparación
Crear temporada DRAFT y asignar 3 facciones. Elegir tres canales distintos, o simulados, y comprobar health por rol. Crear mapas a partir del mismo `seasonSeed` pero visualmente distintos por bioma. Revisar documentalmente que reglas y catálogos concuerden, y dejar constancia de los cambios antes de abrir una temporada. Registrar `rulesetHash`, `contentHash`, versión de motor y modo monetario. Iniciar solo tras ver 3 naciones PREPARED y snapshots iniciales.

### Secuencia A — ciudadano
Llega evento chat verificado `!join` → persistir inbox unique → resolver canal a nación → crear `Citizen` si no existe → emitir `CitizenJoined` → respuesta visual K-0. `!work food` → fijar profesión si nula → `activeUntilUtc=now+7200` → participa en la economía en siguiente segmento → XP desde trabajo efectivo, nunca por el chat. Duplicar mismo evento: `EVENT_DUPLICATE` sin segundo ciudadano/XP. Repetir `!work mine` después de seleccionar food: rechazo sin renovar actividad.

### Secuencia B — transición de era
5 hitos se completan, otorgando 20 puntos cada uno. Si offline, `EraReadyPending`; en próxima señal LIVE confirmada, tomar lock nación y temporada, comprobar que no está COMPLETED, hacer `EraAdvanced` transaccional, extender mapa, recalcular etiquetas de profesión y abrir elecciones por 3600s LIVE. Después prioridad 300s, sin solapar con Consejo. Si `EraAdvanced` entra en interstellar, emitir `SeasonCompleted` y **no** abrir elección nueva.

### Secuencia C — gasto estratégico
Tres opciones financiables → tomar hold vectorial → abrir Consejo durante 600s LIVE → registrar/reemplazar votos → cerrar con recuento → validar hold+saldo tras posibles reversos → gastar una sola vez ganador con ledger → crear `ConstructionQueued` → liberar hold restante → emitir Outbox al OBS. Si se cae la señal, se congela ventana; si no se dispone de oro suficiente al cerrar, marcar `PaymentBlocked` y no crear obra.

### Secuencia D — fallo de proveedor
`HEALTHY → UNCERTAIN` ante ausencia de heartbeat/credenciales; detener ingreso de votos de fuente sin autoridad, pausar LiveClock y penalizaciones; offline economy 20 % y conservar último snapshot. Reautorizar y volver LIVE con evento auditado sin inventar comandos perdidos. Reintentos de webhook deduplicados. Si todas las fuentes no están confirmadas, torneo global se aplaza.

### Secuencia E — operador
Botón `EmergencyStop` inhibe nuevos eventos y congela escrituras de juego de forma ordenada; permitir persistencia/outbox ya confirmada. `Resume` exige health y DB reconciliada. `AbortSeason` no borra movimientos; cambia estado con motivo y resultado vacío. `PublishScene` solo modifica presentación, nunca saldos.


---

## Fuente 18 — `docs/18_DECISIONES_DE_BASE_CORREGIDAS.md`

**Blob original:** `fa74efa7527a3e7bd9f016a5cc629a2d5c6824e6`.

## 18 — Correcciones estructurales realizadas en v2.0

### Ajustes deliberados y por qué

| ADR | Antes | Ahora | Motivo | Impacto |
|---|---|---|---|---|
| V2-001 | Nación equivale a una plataforma | Nación independiente de canal; bindings configurables | tres cuentas en una misma plataforma | cambio de clave de datos y DTO |
| V2-002 | Oro estratégico podría mejorar carrera | solo visual/prestigio | evitar ventaja de pago sobre victoria | cambia magnitud de mejoras estratégicas; no el voto |
| V2-003 | Era final con posible elección y temporada acabada | entrada final cierra inmediatamente; sin gobierno final | eliminar estado imposible de juego cerrado y elección | excepción ceremonial documentada |
| V2-004 | Técnicas/effects `null` | reglas completas con valores v2 | permitir implementación inequívoca | balance candidato versionado |
| V2-005 | Skills colectivas multiplicables | efectos personales con techo | evitar beneficio infinito 10k ciudadanos | reinterpretación de descripciones temáticas |
| V2-006 | Proyectos con 3 candidatos quizá no accesibles | En v2.0 requerían oro, aunque no eran obligatorios para avanzar; **v2.2 sustituye ese supuesto por tres alternativas con recursos ordinarios y oro=0** | Consejo jugable sin aportaciones | decisión v2.2 D-01, `docs/44` |
| V2-007 | Mundo comienza sin infraestructura, podría no producir | zonas naturales gratuitas con capacidad de supervivencia | evitar deadlock de primera madera/piedra | se mantiene evolución desde cero recursos y edificios |
| V2-008 | Economía y penalización fuera de emisión ambiguas | UTC/live/economy/activePenalty separados | reanudación consistente | semántica estable |
| V2-009 | Reversos pueden causar saldo negativo | deuda separada de reversos | mantener invariante de no-negativos | ledger adicional |
| V2-010 | Candidata Ferrina `Perla` evocaba coral | pasa a `Nera`, demás nombres heredados | evitar diseño Corálido descartado | nombre artístico propuesto cerrado v2 |
| V2-011 | Falta exactitud de RPS cíclico | puntuación 2-1-0 por pares y empates compartidos | no inventar ganador en ciclo | reglamento completo |
| V2-012 | Simular todos los usuarios físicamente | trabajo por cohortes, sprites LOD | reducir CPU y minimizar ventaja de masa | representación consistente |

### Enmienda v2.2

Esta tabla guarda la historia; para Consejo/Maravillas y dependencia tecnológica prevalecen las decisiones D-01/D-02 de `docs/41_AUDITORIA_DE_COMPLETITUD_Y_JERARQUIA_v2.2.md`. No aplicar retrospectivamente a temporadas ya iniciadas.

### Enmienda v2.2

Esta tabla guarda la historia; para Consejo/Maravillas y dependencia tecnológica prevalecen las decisiones D-01/D-02 de `docs/41_AUDITORIA_DE_COMPLETITUD_Y_JERARQUIA_v2.2.md`. No aplicar retrospectivamente a temporadas ya iniciadas.

### Jerarquía
Las 92 decisiones originales se preservan literalmente en `data/legacy_user_decisions_1_92.json` y se relacionan en `audit/decision_traceability.json`. La **nueva instrucción expresa del usuario** modifica la asignación rígida plataformas→naciones (antiguos supuestos); no reemplaza el número de naciones, las tres facciones, las reglas sociales ni la independencia de los mundos. Ninguna otra regla original se cambia sin registrar su motivo.

### Qué sigue fuera de posibilidad de un texto
No se puede validar por escrito la licencia de API de una cuenta, tasas financieras reales, carga del hardware de emisión, arte final aprobado ni obligaciones jurídicas sin información externa específica. Eso queda en `audit/EXTERNAL_GATES.md` y NO supone un agujero en la definición de reglas del juego.


---

## Fuente 19 — `docs/19_MAQUINAS_DE_ESTADO_Y_ERRORES.md`

**Blob original:** `0f00607859e6db7a401df8b4ed59bef4c7909a00`.

## 19 — Máquinas de estados y rechazos (contrato de dominio)

### Ciudadano
`UNREGISTERED --!join--> JOINED_NO_PROFESSION --!work(valid)--> ACTIVE --UTC expiry--> RESTING --!active or !work(same)--> ACTIVE`. `!work(different)` desde ACTIVE/RESTING rechaza `PROFESSION_LOCKED`. Ciudadanos no se borran por desconexión ni falta de alimentos. En cierre, `ARCHIVED` conserva historial y stats; siguiente temporada crea ciudadano nuevo.

### Elecciones y votaciones
`QUEUED → OPEN → RESOLVED`; `OPEN → PAUSED` si nación LIVE desaparece, `PAUSED → OPEN` cuando regresa; `OPEN/PAUSED → CANCELLED` solo por operador con motivo. Consejo además `RESOLVED → PAYMENT_BLOCKED` si reverso simultáneo invalida la reserva; no se crea proyecto. `BALLOT` debe referenciar voto abierto, opción admisible, ciudadano de nación, input deduplicado y sello LIVE válido. En `RPS`, una primera papeleta válida es irrevocable; en `GOVERNMENT`, `PRIORITY` y `STRATEGIC` la última papeleta válida sustituye la anterior en la misma fila. `GOVERNMENT_RUNOFF` solo ofrece previamente empatados.

### Obra
`WAITING_RESOURCES → WAITING_PLOT → QUEUED → BUILDING → COMPLETED`; una obra puede saltar WAITING_PLOT si parcela disponible, pero nunca saltarse el pago. Costes se comprometen atómicamente una vez al entrar QUEUED; construcción por tramos visuales; `CANCELLED` antes de pagar libera reserva, después de pagar solo permitido por fallo grave y con compensación auditable que no deshaga trabajos anteriores.

### Cuenta monetaria
`RECEIVED → AUTHENTICATED → VERIFIED → CREDITED → REVERSED` o ramas a `REJECTED`; no se puede ir de `REJECTED` a `CREDITED` sin evento nuevo firmado y referencia a rectificación. `REVERSED` no reabre `CREDITED`. Todos los movimientos contabilizados con causa estable; una segunda notificación del mismo proveedor no crea oro.

### Sesión de directo
`OFFLINE_CONFIRMED → LIVE_CONFIRMED` requiere evidencia y TTL, `LIVE_CONFIRMED → UNCERTAIN` si señal/autoridad pierde health, `UNCERTAIN → LIVE_CONFIRMED` solo al recuperar evidencia. `UNCERTAIN → OFFLINE_CONFIRMED` tras confirmación de fin de emisión o caducidad de TTL. Manual override solo para modo SIMULATED o con autorización operador auditada; un override no valida contribuciones financieras.

### Fin de carrera
`RUNNING` con tres naciones activas → `EraAdvanced to interstellar` → `SeasonWinnerClaim` (unique season) → `COMPLETED`; winner se registra antes de guardar Outbox. Los ticks posteriores no pueden reabrir gobierno ni extender construcción competitiva. `COMPLETED → ARCHIVED` tras cierre y snapshot; no existe `COMPLETED → RUNNING`.

### Errores canónicos
`IDENTITY_NOT_VERIFIED`, `BINDING_NOT_FOUND`, `BINDING_DUPLICATE`, `BINDING_IMMUTABLE`, `CITIZEN_NOT_JOINED`, `PROFESSION_ALREADY_ASSIGNED`, `PROFESSION_LOCKED`, `ACTIVITY_COOLDOWN`, `ACTIVITY_EXPIRED`, `SKILL_LEVEL_LOW`, `SKILL_TIER_ALREADY_CHOSEN`, `SKILL_WRONG_FAMILY`, `VOTE_NOT_OPEN`, `OUT_OF_WINDOW`, `BALLOT_INVALID_OPTION`, `RPS_ALREADY_VOTED`, `EVENT_DUPLICATE`, `EVENT_TOO_OLD`, `STREAM_NOT_CONFIRMED`, `SOURCE_UNAUTHORIZED`, `PROJECT_NOT_AFFORDABLE`, `PROJECT_THREE_OPTIONS_REQUIRED`, `HOLD_CONFLICT`, `CONTRIBUTION_NOT_VERIFIED`, `GOLD_CONVERSION_DISABLED`, `GOLD_REVERSAL_UNBACKED`, `SEASON_ALREADY_COMPLETED`, `RULESET_HASH_MISMATCH`, `MIGRATION_REQUIRED`, `WRITER_FENCING_ERROR`. La respuesta pública describe el motivo sin IDs privados ni detalles financieros.


---

## Fuente 20 — `docs/20_PANTALLAS_PANEL_OPERADOR_Y_ROLES.md`

**Blob original:** `f2639e3214d8116246f0c298c821d4f5ececdc54`.

## 20 — UX de jugador, escenas OBS y panel de operador

### Escenas públicas
- **UniverseOverview**: tres naciones en miniatura, era, barra 0–100 y estado LIVE, ganador o empate; solo metadatos agregados compartibles.
- **NationWorldVertical**: mundo 66 %, HUD superior 14 %, HUD inferior 20 %; zona de cámara sigue obras/visitas de K-0, viewport lógico 360x640.
- **NationWorldHorizontal**: 73 % viewport, 27 % panel lateral, 640x360 lógico; componentes reposicionados, no escalados arbitrariamente.
- **ElectionOverlay**: tres candidatos, tiempo LIVE restante, recuento total y porcentajes permitidos después de cierre.
- **StrategicCouncilOverlay**: tres alternativas, costes ordinarios y oro, aviso «opcional/estético», timer 10min y estado de reserva.
- **TournamentOverlay**: tres equipos, votos totales por nación, ocultación de opciones hasta cierre, puntuación de duelos por parejas y penalizaciones activas.
- **SeasonFinale**: ganador, estadísticas y museo con historial sin saldo de oro como moneda útil.

### Controles de operador
Login MFA con rol; tabla de cuentas asociadas (provider/channel, LiveHealth, capabilities, token TTL con secretos ocultos), reglas hash, versión de cada adaptador, simulación clock, health DB y outbox, backlog de eventos, contador de reintentos, gastos TTS. Acciones: PREPARE, START, PAUSE, RESUME, SCHEDULE_EVENT, SCHEDULE_TOURNAMENT, CANCEL_VOTE (motivo), SAFE_SCENE, MUTE_K0, EMERGENCY_STOP, ARCHIVE, EXPORT_AUDIT. Toda acción exige idempotencyKey, confirmación UI cuando tiene efecto económico y log; no existe botón para «dar oro» en producción.

### Onboarding para monetizar a otros creadores
Primera edición de producto es un solo creador/campaña con exactamente tres facciones. Cuando se comercialice, añadir `Tenant`, billing/licencias, aislamiento de credenciales por tenant, cuota de canales, RLS/particionamiento si hay evidencia. No diseñar cross-tenant billing en MVP. Cada creador puede escoger qué tres cuentas conectar, sin alterar los oficios ni las identidades de facción.

### Accesibilidad y degradación
Narración siempre subtitulada; no comunicar éxito únicamente por color, feedback de comandos válido en HUD incluso si la plataforma no autoriza responder al chat. Reducir efectos luminosos y FPS en OBS bajo carga sin tocar tick backend. El lector de pantalla del panel de operador accede a etiquetas y countdown; overlays públicos son imágenes audiovisuales pero acompañados de panel textual.


---

## Fuente 21 — `docs/21_MAPAS_Y_SEMILLAS_DETERMINISTAS.md`

**Blob original:** `6f29712a2b18631442aa7cf44c08a27c8d953bb2`.

## 21 — Generación de mapa completamente determinista

### Reglas de terreno
El mapa es una **cuadrícula lógica universal edificable**. El bioma inicial cambia exclusivamente el aspecto y nunca las coordenadas disponibles. Tamaño inicial 48×48 casillas (`x=0..47`,`y=0..47`), centro = `(23,23)`. Al desbloquear era N el ancho y alto pasan a `48 + 16*(N-1)`, centrando la región inicial sin mover los edificios existentes en coordenadas de mundo; límite absoluto 256×256 (era 13 = 240×240). Las coordenadas lógicas absolutas pueden ser negativas al expandir a ambos lados de (0,0); no serializar offsets de cámara como coordenadas de edificio.

### Determinismo de decoración
`terrainVariant = SHA256(utf8('{seasonSeed}|{nationId}|{x}|{y}|terrain'))[0] % 4` ; `decorationPresent = SHA256(utf8('{seasonSeed}|{nationId}|{x}|{y}|deco'))[0] % 10 == 0`; `decorationVariant = digest[1] % 8`. Todos los hashes se computan en UTF-8 con IDs normalizados, bytes iniciales sin signo. Las decoraciones no impiden construir y desaparecen si la parcela se ocupa; se guarda en evento de presentación para animar. No se utiliza ruido Perlin, dependencia de motor gráfico o `Random()` para elegir recursos económicos.

### Ubicación de edificios
Se reserva un rectángulo de `footprintTiles` sin solapamientos de otras parcelas de edificios ni la plaza de arranque (3×3 libre alrededor de `(23,23)`). Buscar en orden `(distance=abs(x-23)+abs(y-23), y, x)` dentro de los límites, con `x/y` representando la esquina inferior izquierda de la huella; el primero que cabe gana. Al expandir, el edificio anterior conserva coordenadas y parcela. Si no cabe aún, `WAITING_PLOT` hasta expansión; no gastar materiales antes de disponer de parcela. Las obras automáticas obligatorias pueden tener reservados 2 slots de emergencia alrededor de área central para impedir bloqueo por obras cosméticas; esos slots se desbloquean al acabar la era.

### Reproducción visual
El cliente puede desplazar cámara y LOD libremente; nunca enviar coordenadas de render como verdad económica. Misma semilla y mismos edificios deben reproducir el mismo mapa lógico con cualquier proveedor de streaming. La apariencia de cada bioma usa paleta propia pero límites de construcción iguales.


---

## Fuente 22 — `docs/22_METRICAS_CARGA_Y_CALIBRACION.md`

**Blob original:** `0ba4084e681d8367bfce5d73eed3180a915d8fdd`.

## 22 — Plan cuantitativo de balance, carga y latencia

### Métricas obligatorias
`chaos_inbox_lag_seconds`, `chaos_inbound_duplicate_rate`, `chaos_tick_duration_ms`, `chaos_nation_simulated_seconds`, `chaos_rule_rejections_total{code}`, `chaos_era_duration_hours`, `chaos_era_cumulative_resource_produced`, `chaos_worker_effective_units`, `chaos_hunger_segments`, `chaos_storage_blocked_units`, `chaos_outbox_pending`, `chaos_gold_credit_unique`, `chaos_gold_debt_units`, `chaos_vote_close_lag_ms`, `chaos_obs_fps`, `chaos_tts_spend`, `chaos_backup_last_success`, `chaos_lease_epoch`. No usar IDs de usuario en etiquetas de métricas para evitar cardinalidad alta y filtraciones.

### Umbrales operativos iniciales, no evidencia medida
Tick CPU objetivo <50ms por nación a carga mediana, P95 Inbox-to-simulation <1s, P95 public delta <2s, cola outbox sin crecer durante 15min de carga, 30 FPS OBS estable durante 1 hora por salida con baseline 90 sprites horizontales /45 verticales; permitir degradación visual progresiva sin alterar economía. Estas cifras son SLO **propuestos** para implementar tests, no garantías.

### Balance de carrera
Correr tres mundos con la misma seed y perfiles (0 humanos/24 NPC, 10/24, 100/24, 1000/24, 10000/24). Medir 13 cambios de era con 1h LIVE/día, 4h LIVE/día y 24h LIVE/día; simular pausas, capacidad máxima y misión diaria que vence antes del hito. Criterio de liveness: el escenario 0 humanos/24 NPC no queda bloqueado por falta de oro, madera, piedra, conocimiento ni edificios; solo puede esperar a LIVE para confirmar cambio de era. Criterio de justicia de torneo: tamaño de audiencia no cambia puntuación RPS dado mismo reparto relativo de votos.

### Optimización
Conservar `NationSimulation` de escritor único. Agrupar humanos por `(profession,bonusSet,activeTo,quotaClass)` y remanentes enteros por grupo, no iterar 100.000 sprites. Construcción y pathfinding client-side aproximados. Primero medir DB contention, CPU del escritor y coste de SignalR; separar process worker/web y añadir fencing antes de considerar colas externas.


---

## Fuente 23 — `docs/23_GLOSARIO_JERARQUIA_Y_LIMITE_DE_DISENO.md`

**Blob original:** `6d2443ac43e7a4744ab26a51d85142793bd6a2ff`.

## 23 — Glosario, jerarquía de decisiones y alcance documental

**Estado:** definición documental v2.1. No se propone código ni una nueva mecánica. Fuente principal: reglas históricas 1–92, documentos 01–22 de v2.0 y catálogos de `data/`.

### Diccionario obligatorio

- **Campaña:** experiencia de un organizador con tres naciones, configuración editorial, canales y temporadas. No equivale a plataforma.
- **Temporada:** competición limitada entre tres naciones con instante de inicio, semilla, versión de reglas, progreso, ganador y cierre.
- **Nación:** instancia de facción (`micelios`, `runicos`, `ferrinos`) con estado económico, tecnología y gobierno propios; es una entidad estable de dominio.
- **Facción:** identidad cultural y estética; no altera las estadísticas base.
- **Cuenta/canal:** origen externo de mensajes, presencia en directo y, si está autorizado, aportaciones verificadas; se asigna con `ChannelBinding`.
- **Ciudadano:** participación jugable de una identidad en nación y temporada; diferente del avatar representado.
- **Avatar/sprite:** representación visual opcional de un ciudadano, NPC u objeto; nunca origen de operaciones económicas.
- **NPC:** población autónoma no monetizada que mantiene activa la economía y puede alcanzar los hitos gratuitos.
- **Profesión:** una de cinco familias productivas; la decisión del jugador dura una temporada.
- **Era:** etapa histórica lógica que define catálogos desbloqueables, títulos y estilo visual.
- **Hito:** objetivo único por era que aporta 20 puntos históricos una sola vez.
- **Misión:** reto diario o semanal recurrente; su finalización puede satisfacer el hito de tipo misión una vez por era, pero no concede puntos repetidamente.
- **Edificio básico:** construcción automática de la civilización, financiada con recursos ordinarios.
- **Proyecto estratégico:** obra opcional seleccionada en Consejo con votación entre tres opciones financiables.
- **Maravilla:** obra de prestigio visual opcional, globalmente exclusiva cuando así la define el catálogo.
- **Oro:** saldo interno vinculado únicamente a aportaciones autorizadas y verificadas; no tiene convertibilidad real y no mejora la carrera histórica.
- **Directo confirmado:** estado de emisión autenticado que habilita cronómetros y ceremonias; distinto de tener una ventana OBS abierta.
- **Regla canónica:** obligación de comportamiento que prevalece sobre ejemplos, prototipos o textos promocionales.
- **Gate externo:** condición verificable de plataforma, licencia, hardware, privacidad o integración que no puede darse por cumplida por redactar un documento.

### Jerarquía de fuentes

1. Última instrucción explícita del propietario del proyecto.
2. Decisiones originales registradas (92) que no hayan sido sustituidas expresamente.
3. Reglas canónicas de v2.0 y correcciones registradas en `docs/18`.
4. Datos estructurados con valores numéricos (`data/ruleset.v2.json` y catálogos canónicos).
5. Ampliaciones documentales de v2.1, exclusivamente cuando aclaren el diseño sin cambiar su semántica.
6. Ejemplos ilustrativos y propuestas futuras (no prevalecen).

Si una tabla descriptiva y el JSON canónico difieren en una cifra, **no se improvisa**: se registra una discrepancia, se congela el cambio y se adopta una revisión consistente. No existe una jerarquía en la que un documento de estética autorice a conceder recursos, oro, votos o puntos.

### Qué significa «completado»

Una mecánica se considera documentada cuando identifica sujeto, disparador, entradas, condiciones, resultado, límites, errores, persistencia, pantalla y su criterio de aceptación. La documentación podrá ser exhaustiva en intención y decisiones, pero **no certifica** que una API externa funcione, que el servidor escale o que un sprite tenga calidad artística. Esos hechos pertenecen a validación futura.

### Fuera de alcance de esta fase

No crear repositorios, backend, cliente, scripts Python, tests ejecutables, Docker Compose, CI/CD ni configuraciones con secretos. Es válido conservar SQL como **modelo de datos propuesto** y JSON/YAML de contratos y catálogos como **definición declarativa**, sin ejecutar ninguno. La documentación no se debe confundir con una aplicación funcional.


---

## Fuente 24 — `docs/24_RECORRIDOS_ESPECTADOR_Y_CIUDADANIA.md`

**Blob original:** `e9b9a03554661965586982bedb6560840e76c891`.

## 24 — Recorridos del espectador y experiencia del ciudadano

**Objetivo:** cerrar la experiencia observable por un usuario en chat sin depender de cómo se implemente la integración. Se mantiene una identidad de ciudadanía por nación y temporada; la existencia de distintas cuentas no altera la pertenencia de la nación.

### Usuario nuevo

1. Descubre un directo asociado a una nación y ve en el HUD: nombre de la civilización, era, progreso, estado actual y ayuda de comandos.
2. Emite `!join` desde una identidad reconocida por el proveedor y el sistema crea o devuelve su ciudadano, sin duplicados por reintento.
3. Si no eligió oficio, la interfaz invita a usar `!work food`, `!work wood`, `!work mine`, `!work build` o `!work research` (adaptar los alias a los comandos registrados, sin alterar semántica).
4. La profesión elegida se mantiene hasta fin de temporada. Volver a usar el mismo oficio renueva actividad cuando cumple cooldown; cambiar a otra familia debe producir rechazo comprensible.
5. Si el usuario está activo, trabaja durante su ventana real de dos horas. El avatar puede no estar entre los sprites visibles porque existen límites de densidad: nunca se interpreta como expulsión de la economía.

**Feedback visual mínimo:** confirmación de alta, profesión válida, duración restante de actividad, nivel, habilidades disponibles y resultado de cualquier comando. Si el proveedor prohíbe respuesta por chat, el feedback se presenta en la UI del juego; no se inventa un mensaje enviable.

### Usuario recurrente

Al volver al directo, el usuario recupera identidad por identificador estable del proveedor, no por nombre visible; conserva progreso durante la temporada. `!active` renueva actividad tras validación. Si cambió su nombre público, no se crea otro ciudadano. Si cambia de dispositivo sin cambiar de cuenta, tampoco. No se promete fusionar automáticamente identidades de TikTok, Twitch y YouTube.

### Usuario con varias cuentas o canales

Un canal concreto se asigna a una sola nación por temporada. La misma cuenta del proveedor puede participar en naciones diferentes solo cuando sus canales correspondientes se asignan a ellas; las estadísticas permanecen separadas. Varias cuentas de un mismo ser humano no son identificables con certeza y no debe prometerse prevención absoluta del multicuenta.

Una cuenta de creador puede aparecer en distintas escenas OBS; ello no implica que los espectadores adquieran identidades compartidas entre canales.

### Participación política y social

Durante elecciones, el HUD ofrece tres candidaturas NPC, su categoría (economía, ejército, ciencia), el tiempo LIVE restante y la forma de votar. Un usuario tiene como máximo una papeleta efectiva que puede reemplazar según la regla canónica. Los empates pasan a segunda vuelta; el resultado y las bonificaciones se hacen públicos al cerrarse. La prioridad tecnológica se vota en una ventana independiente y breve. No se debe sugerir que el gobernador controla la economía a voluntad: únicamente concede el bono pasivo definido.

En Consejo, el usuario ve tres **proyectos elegibles y costeables**, sus costes, el carácter opcional y la cuenta atrás de diez minutos LIVE. El usuario vota; al cierre se carga únicamente el vencedor, no las tres opciones. Si la nación no tiene recursos para tres propuestas, el Consejo se pospone; no se reemplaza por una oferta imposible ni por una petición obligatoria de donaciones.

En torneo, el usuario ve `!rps`, las tres opciones y la regla de voto irrevocable. La distribución exacta de elecciones se mantiene oculta hasta el cierre para evitar arrastre estratégico. Las decisiones de la audiencia no cambian la potencia base de las especies ni el cálculo del ranking de puntos por pareja.

### Situaciones de excepción y mensajes orientados al usuario

| Caso | Respuesta de producto | Consecuencia interna |
|---|---|---|
| Comando desconocido | Mostrar ayuda sin mencionar detalles internos | Sin acción en dominio |
| Usuario no registrado intenta votar | Indicar participación mediante `!join` | No se guarda voto |
| Cambiar profesión ya elegida | Explicar que dura una temporada | Profesión original intacta |
| Voto fuera de ventana | Comunicar cierre de votación | Voto descartado y auditado |
| Cuenta/canal no asignado | No otorgar recursos ni crear ciudadanos | Entrada ignorada por enrutador |
| Fallo de señal LIVE | Avisar «emisión no confirmada» | Cronómetros congelados |
| Reintento duplicado | No duplicar ninguna recompensa ni voto | Idempotencia |
| Capacidad de almacén llena | Informar «capacidad saturada» | Excedente descartado o producción limitada según regla |
| Falta de espectadores | Mostrar economía NPC sin sustituir votos humanos | Continuidad del mundo |
| Fin de temporada | Congelar competición y mostrar museo | Recursos no se trasladan |

### Aceptación editorial

Las etiquetas de profesión, era y edificaciones deben diferenciarse de las claves internas; los errores no enseñan UUID, tokens ni SQL. Todo cambio autoritativo relevante se representa con una señal visible o texto subtitulado: alta, subida de nivel, inicio y fin de votación, edificio terminado, nueva era, penalización y victoria.

