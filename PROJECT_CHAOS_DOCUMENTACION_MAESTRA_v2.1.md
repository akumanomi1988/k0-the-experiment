# PROJECT CHAOS — DOCUMENTACIÓN MAESTRA v2.1

**Propósito:** documento de lectura de todas las reglas y definiciones de producto. **No contiene implementación ejecutable.** Los catálogos extensos, los contratos y el SQL se entregan como anexos separados para no ocultar identificadores y valores bajo prosa.

## Índice de capítulos

- [01 — Producto, alcance y principios no negociables (v2.0)](docs/01_VISION_Y_ALCANCE.md)
- [02 — Topología configurable de canales y ciudadanía](docs/02_CANALES_CUENTAS_Y_NACIONES.md)
- [03 — Relojes, scheduler, replay y estados](docs/03_TIEMPOS_SIMULACION_Y_DETERMINISMO.md)
- [04 — Reglas numéricas del motor económico](docs/04_ECONOMIA_Y_BALANCE.md)
- [05 — Construcciones básicas, proyectos y mapa](docs/05_EDIFICIOS_Y_MAPA.md)
- [06 — Ciudadanos, profesión única, XP y especializaciones](docs/06_PROFESIONES_HABILIDADES_Y_XP.md)
- [07 — Progresión histórica, investigación y temporadas](docs/07_PROGRESION_TECNOLOGICA_Y_TEMPORADAS.md)
- [08 — Elecciones NPC, prioridades y Consejo de Construcción](docs/08_GOBIERNO_VOTACIONES_Y_CONSEJO.md)
- [09 — Torneos, sanciones, eventos y misiones](docs/09_TORNEOS_EVENTOS_Y_MISIONES.md)
- [10 — Monetización verificable, ledger y límites](docs/10_MONETIZACION_LEDGER_Y_CONTRIBUCIONES.md)
- [11 — Doctor K-0, narrativa y control de actos](docs/11_DIRECTOR_DOCTOR_K0_Y_MODERACION.md)
- [12 — Diseño visual y producción de assets](docs/12_UX_PIXELART_Y_ASSETS.md)
- [13 — Arquitectura modular, dominio y APIs](docs/13_ARQUITECTURA_APIS_Y_ESTADOS.md)
- [14 — Seguridad, privacidad, infraestructura y continuidad](docs/14_SEGURIDAD_PRIVACIDAD_Y_OPERACION.md)
- [15 — Pruebas automáticas y criterios de aceptación](docs/15_PRUEBAS_Y_CIERRE_DE_DEFINICION.md)
- [16 — Capacidades LIVE verificables y políticas](docs/16_INTEGRACIONES_Y_CUMPLIMIENTO.md)
- [17 — Runbook del operador y flujos E2E](docs/17_OPERADOR_ESCENARIOS_Y_DIAGRAMA_E2E.md)
- [18 — Correcciones estructurales realizadas en v2.0](docs/18_DECISIONES_DE_BASE_CORREGIDAS.md)
- [19 — Máquinas de estados y rechazos (contrato de dominio)](docs/19_MAQUINAS_DE_ESTADO_Y_ERRORES.md)
- [20 — UX de jugador, escenas OBS y panel de operador](docs/20_PANTALLAS_PANEL_OPERADOR_Y_ROLES.md)
- [21 — Generación de mapa completamente determinista](docs/21_MAPAS_Y_SEMILLAS_DETERMINISTAS.md)
- [22 — Plan cuantitativo de balance, carga y latencia](docs/22_METRICAS_CARGA_Y_CALIBRACION.md)
- [23 — Glosario, jerarquía de decisiones y alcance documental](docs/23_GLOSARIO_JERARQUIA_Y_LIMITE_DE_DISENO.md)
- [24 — Recorridos del espectador y experiencia del ciudadano](docs/24_RECORRIDOS_ESPECTADOR_Y_CIUDADANIA.md)
- [25 — Biblia narrativa del experimento](docs/25_BIBLIA_NARRATIVA_UNIVERSO_Y_PERSONAJES.md)
- [26 — Biblia visual: legibilidad, tres culturas y 13 eras](docs/26_BIBLIA_VISUAL_FACCIONES_EPOCAS_Y_SILUETAS.md)
- [27 — Especificación de escenas, pantallas y estados visibles](docs/27_ESCENAS_PANTALLAS_Y_SECUENCIAS_PUBLICAS.md)
- [28 — Libro de estilo y protocolo narrativo de Doctor K-0](docs/28_NARRACION_K0_Y_DIRECCION_DEL_ESPECTACULO.md)
- [29 — Matriz de casos límite y degradación funcional](docs/29_ESTADOS_EXTREMOS_Y_FALLOS_EN_DIRECTO.md)
- [30 — Lista de entregables de arte, animación, mapa y audio](docs/30_ENTREGABLES_ARTISTICOS_Y_CRITERIOS_APROBACION.md)
- [31 — Diseño de emisión con una, dos o tres plataformas](docs/31_DISENO_OPERATIVO_CUENTAS_Y_EMISIONES.md)
- [32 — Responsabilidades del operador y gobierno del experimento](docs/32_OPERADOR_GOBERNANZA_Y_CAMBIOS_EN_VIVO.md)
- [33 — Modelo de negocio y límites de monetización](docs/33_NEGOCIO_MONETIZACION_PRIVACIDAD_Y_FUTURO_SAAS.md)
- [34 — Catálogo legible de los 130 edificios básicos](docs/34_CATALOGO_LEGIBLE_EDIFICIOS.md)
- [35 — Proyectos estratégicos y maravillas: catálogo legible](docs/35_CATALOGO_LEGIBLE_PROYECTOS_Y_MARAVILLAS.md)
- [36 — Tecnologías, hitos y misión de la barra histórica](docs/36_CATALOGO_LEGIBLE_TECNOLOGIAS_E_HITOS.md)
- [37 — Profesiones, habilidades y gobiernos: catálogo legible](docs/37_CATALOGO_LEGIBLE_PROFESIONES_HABILIDADES_GOBIERNOS.md)
- [38 — Casos de aceptación funcional sin código](docs/38_PRUEBAS_ACEPTACION_EN_LENGUAJE_NATURAL.md)
- [39 — Registro de cierre documental y validaciones externas](docs/39_REGISTRO_DE_CIERRE_Y_VALIDACIONES_EXTERNAS.md)
- [40 — Requisitos no funcionales y calidad de producto](docs/40_DESCRIPCION_NO_FUNCIONAL_Y_CALIDAD.md)

---



---


<!-- Documento fuente: docs/01_VISION_Y_ALCANCE.md -->


# 01 — Producto, alcance y principios no negociables (v2.0)

## Identidad y promesa al espectador
Project CHAOS — El Experimento de las Civilizaciones es un juego-espectáculo permanente por temporadas: tres naciones inteligentes no humanas, representadas con pixel art 2D de baja resolución en proyección oblicua 2:1, evolucionan del Paleolítico a la Era Interestelar. Doctor K-0, científico cyborg, sarcástico y neutral, presenta el experimento. La audiencia participa mediante comandos de chat desde uno de los canales asociados. La nación no es la plataforma: los canales son **fuentes intercambiables**. Se admiten tres canales de Twitch, tres cuentas TikTok, YouTube, una mezcla, o modo local; todas las configuraciones dependen del acceso permitido y comprobado al proveedor.

## Decisiones heredadas, no negociables
- Tres naciones independientes: Micelios, Rúnicos y Ferrinos. No existen Corálidos. Misma base matemática, sin bonificaciones por especie/bioma.
- Cinco profesiones permanentes por temporada (`food`, `wood`, `mine`, `build`, `research`) y evolución estética por era.
- `!join` y `!work` para crear ciudadano/elegir oficio. `!active` o `!work` válido renuevan 2 horas de actividad real; el chat normal no.
- NPC mantienen el mundo vivo sin espectadores; la simulación fuera de emisión funciona a velocidad reducida.
- Recursos colectivos, comida sin muerte individual, almacenes limitados, edificios básicos automáticos, proyectos estratégicos votados entre **tres alternativas financiables** durante diez minutos; sus costes se descuentan al aprobar.
- Elecciones de gobiernos NPC: tres arquetipos, un gobernante, una hora de voto, segunda vuelta de tres minutos ante empate. Votación separada de prioridad tecnológica.
- Barra de historia por hitos únicos de puntuación fija; era lista fuera de emisión espera al LIVE. Primera nación en entrar a era final gana la temporada.
- Torneos solo programados: primer minijuego RPS triangular con elección oculta; penaltis territoriales de 30 minutos **activos en directo**; cero transferencia de oro.
- Oro solo desde aportaciones económicas verificadas; jamás por NPC, misiones, chat ni operaciones de explotación. Permanencia solo de historial, estadísticas, logros y prestigio visual entre temporadas.

## Cierre de definición de v2.0
Valores desconocidos de balance y reglas ambiguas pasan a convertirse en **defaults de producto v2.0**. Son decisiones técnicas/de producto tomadas en virtud de la autorización del usuario de este turno, *no respuestas históricas atribuidas al usuario*. Se pueden versionar antes de abrir una temporada; nunca alterarse a mitad de temporada sin migración explícita y auditoría.

No existe en este documento ninguna autorización implícita para extraer datos con APIs no oficiales ni para simular un beneficio monetario. Tampoco confundir especificación de sprites con haberlos creado; `art_spec.v2.json` es especificación, y las integraciones LIVE reales se mantienen bloqueadas hasta pruebas verificables.

## El juego no es pay-to-win
El oro se usa exclusivamente en proyectos opcionales de estética/prestigio, monumentos y homenajes. Todos los umbrales de historia y el motor de investigación son gratuitos. Para evitar la ventaja matemática por riqueza, un proyecto financiado con oro no aporta puntos históricos, capacidad productiva, voto extra, velocidad científica ni fuerza militar. Una maravilla entrega prestigio y reconocimiento visual, no economía. Este ajuste solventa el riesgo de que una donación sea la condición tácita de victoria.

## Criterios de éxito del diseño
Dos implementaciones que compartan `ruleset_hash`, `content_manifest_hash`, `season_seed`, la secuencia canónica de eventos y UTC segmentado deben producir el mismo estado lógico, incluido el ganador. Los viewers y la máquina OBS solo consumen proyecciones. Ningún NPC ni sprite tiene permisos de cambiar el ledger de recursos por vía gráfica.



---


<!-- Documento fuente: docs/02_CANALES_CUENTAS_Y_NACIONES.md -->


# 02 — Topología configurable de canales y ciudadanía

## Modelo obligatorio
`Campaign` (creador/propietario), `Season`, `Nation` (exactamente tres), `ChannelBinding` (plataforma+cuenta/canal), `ProviderIdentity` (usuario auténtico de proveedor), `Citizen` (persona jugable en una nación/temporada) y `BroadcastOutput` (overlay con filtros). `NationId` nunca deriva de `provider`, no puede ser nombre de plataforma, y es inmutable dentro de una temporada. `ChannelBinding` tiene roles explícitos: `commands`, `live_health`, `contributions`, `display_feed`. Cada nación designa exactamente un canal con `isClockAuthority=true`, `role=live_health`; su señal autenticada define el LiveClock de esa nación para no sumarlo dos veces si existen cuentas secundarias. Otras fuentes aportan chat y métricas pero no alargan el reloj. El operador puede cambiar la fuente de reloj solo pausando y auditando la revisión; en simulación hay control manual auditado.

## Ejemplos admitidos
1. Micelios=Twitch canal A, Rúnicos=Twitch canal B, Ferrinos=Twitch canal C.
2. Micelios=TikTok cuenta A, Rúnicos=TikTok cuenta B, Ferrinos=TikTok cuenta C (únicamente si la integración autorizada expone los eventos necesarios).
3. Micelios=YouTube canal A, Rúnicos=Twitch B, Ferrinos=TikTok C.
4. Una nación puede recibir dos canales distintos, por ejemplo streaming principal más un canal secundario, sin duplicar la identidad de un mismo usuario del mismo proveedor. Nunca asignar **el mismo canal** a dos naciones en una temporada: riesgo de votos/copias ambiguas.
5. Simulador local admite exactamente tres fuentes `simulated`, una por nación, sin fingir que son aportaciones monetarias reales.

## Persistencia de ciudadanía
Clave de usuario de proveedor = `(provider, providerUserId)`; nunca nombre visible. Ciudadano = `(seasonId, nationId, provider, providerUserId)` unívoco. Varios canales de **igual proveedor** asignados a misma nación producen **un solo ciudadano**. Una misma identidad del proveedor **sí puede crear ciudadanos distintos en naciones diferentes** cuando participa en sus respectivos canales, igual que en el diseño original podía participar con identidades de plataformas distintas; la clave lógica incluye `nationId`. Esto no permite duplicar ciudadanía dentro de la misma nación aunque el usuario aparezca en varios canales de esa nación. El sistema no promete impedir identidades alternativas entre proveedores.

**Criterio de migración:** cambiar la plataforma/cuenta asociada a una nación durante temporada activa es un cambio privilegiado que requiere pausa de entrada, drenaje de Inbox, grabar estado y `BindingRevision`; el ciudadano anterior mantiene su nación y stats; no se mueve automáticamente a otra. Cambios de binding requieren origen autorizado, usuario operador MFA y log. Cambiar de nación una misma cuenta ya registrada está prohibido durante la temporada.

## Entrada y permisos
Un adaptador `IPlatformAdapter` convierte `(provider, channel_id, event_id, received_utc, provider_user_id, capability, payload)` a `NormalizedEventV2`. El enrutador `BindingResolver` usa `(seasonId, provider, providerChannelId)` para obtener una sola nación; si no existe una asignación activa, `DROP_UNMAPPED` auditable. Mensajes de chat, estado LIVE y aportaciones son tres capacidades separadas; si no hay permisos para una, se desactiva solo esa capacidad. Un `binding` nunca puede autohabilitar monetización.

## LIVE y relojes por nación
Cada nación puede estar `LIVE_CONFIRMED`, `OFFLINE_CONFIRMED` o `UNCERTAIN`. `UNCERTAIN` cuenta como offline para economía y pausa votaciones; no consume tiempo de penalización de torneo. Para abrir una ceremonia de nueva era se requiere `LIVE_CONFIRMED` de la propia nación. Para un torneo simultáneo se requieren las tres naciones LIVE y un `broadcastSession` compatible. Ninguna nación debe quedar bloqueada para siempre por una cuenta desconectada: sigue simulando offline y acumula `EraReadyPending` hasta próxima emisión confirmada.

## Salidas y cumplimiento
Cada salida OBS tiene `OutputId`, `BindingId` emisor y una política `allowedNations`. Por defecto muestra solo elementos de ese canal, agregados del mundo permitidos y resultados del propio juego sin reproducir mensajes/reacciones crudos de plataformas ajenas. Mezclar chat, mensajes o referencias cruzadas requiere aprobación de política por proveedor. Ver `docs/16_INTEGRACIONES_Y_CUMPLIMIENTO.md`.



---


<!-- Documento fuente: docs/03_TIEMPOS_SIMULACION_Y_DETERMINISMO.md -->


# 03 — Relojes, scheduler, replay y estados

## Relojes tipados
- `UtcClock`: tiempo físico, monotónico verificado contra reloj de sistema; expiraciones de ciudadanos (+7200s), caducidades de OAuth, misiones UTC. Se almacena la fecha absoluta además del evento.
- `NationLiveClock`: integra exclusivamente segundos `LIVE_CONFIRMED`; elección 3600s, segunda vuelta 180s, proyecto 600s, prioridad 300s, RPS 90s, bonus prioridad 5400s. Se congela en `UNCERTAIN`, `PAUSED` o `OFFLINE_CONFIRMED`.
- `NationEconomyClock`: 1 segundo equivalente en LIVE, 0,2 en OFFLINE/UNCERTAIN; sin doble aplicar al recuperar.
- `NationActivePenaltyClock`: avanza 1s solo en LIVE; una región penalizada consume exactamente 1800s activos; NUNCA consume segundos fuera de emisión.

No sumar segundos a ciegas: cada segmento `[lastProcessedUtc, nowUtc)` se particiona por cambios de estado LIVE, expiraciones de trabajadores, cierre de sesiones y vencimientos de comandos. La producción y experiencia se calculan en el mismo segmento. Un comando entra al tick siguiente; `receivedUtc` decide si se admite en una votación abierta cuando se recibió durante intervalo. Eventos con `providerTimestamp` fuera de tolerancia se ponen en cuarentena.

## Orden canónico por tick
1. Consumir `Inbox` autenticado y deduplicado y ordenar por `ingestSeq` (no reloj del proveedor cuando contradiga secuencia persistida).
2. Aplicar cambios de `LIVE` auditados con sello de instante.
3. Aplicar comandos de ciudadanos y papeletas llegadas antes del cierre.
4. Cerrar ventanas exactas de voto cuyo LiveClock alcanzó su deadline; una papeleta en instante de cierre se rechaza.
5. Aplicar disponibilidad de trabajadores (segmentada); gastos de comida y mantenimiento; producción limitada a capacidad; XP.
6. Resolver planificación automática, avances de construcción, tecnologías y misiones.
7. Reconocer hitos únicos y transición de era (solo LIVE). La entrada a la última era genera evento global terminal.
8. Registrar estados, ledger, outbox y checksum antes de notificar clientes. Actualizar snapshots cada 60 segundos de economía o 100 eventos críticos, lo que suceda primero.

## Idempotencia y replay
`sourceEventKey=SHA256(provider + bindingId + originalEventId + eventType)`; `commandId` se asigna una vez tras inbox. `rulesetHash`, `contentHash`, `seasonSeed`, `engineVersion`, `remainderVectors` se guardan en snapshot. RNG `sha256-counter-64-v1`: `sha256(seed||domain||counter_be64)`, valor uniforme por rechazo para evitar sesgo (`limit = floor(2^64/n)*n`). Counters separados por dominio (`elections`, `tournaments`, `map`, `events`) y nación; este detalle evita cambios de resultados al añadir más narración.

Replay desde snapshot requiere mismo runtime numérico y mismo orden de eventos/segmentos. Un bug de versión no se corrige editando transacciones pasadas: abrir migración/compensación con evento auditable.

## Caída larga
Hasta siete días de interrupción se integra economía offline exactamente por segmentos y checkpoints. A partir de siete días el sistema entra en `NEEDS_OPERATOR_REVIEW` y no aplica catch-up adicional hasta que un operador resuelva y audite la decisión. Ninguna transición de era ocurre automáticamente en catch-up. Las ventanas electorales quedan congeladas si no hay LIVE confirmado.

## Inicio y fin de temporada
`DRAFT → PREPARED → RUNNING → COMPLETED → ARCHIVED`, con derivaciones `PAUSED`, `RECOVERY_REQUIRED`. Start a hora UTC única y seed inmutable. Las tres naciones arrancan en Paleolítico en el mismo commit. En cuanto `EraAdvanced` de una nación entra en Interestelar, un `SeasonWinnerClaim` atómico fija ganador, finaliza la producción competitiva y prepara ceremonia de cierre; empate mismo instante resuelto por secuencia de commit, no aleatoriedad. Estadísticas, historia, prestigio y logros persisten; economía no se transfiere.



---


<!-- Documento fuente: docs/04_ECONOMIA_Y_BALANCE.md -->


# 04 — Reglas numéricas del motor económico

## Unidades y precisión
Todas las cantidades ordinarias se almacenan como `BIGINT` en **milésimas de recurso**; las tarifas en milésimas por minuto de trabajador. Los porcentajes son puntos básicos (`10000 = 100 %`). Todos los cálculos son enteros y guardan resto por `(nationId,resourceId,workerPoolId)` para que cambiar el tamaño de tick no cambie sistemáticamente la producción. Nunca usar `double`, `float` ni `Math.random()` para estado persistente. El oro se guarda en unidades indivisibles por asiento de ledger. Toda tasa depende del `rulesetHash` fijado al iniciar temporada.

## Producción por grupo y minuto efectivo
Para cada familia `f`, `EffectiveWorkerMinutes = NPC_count + sum(human_weight)` multiplicado por `deltaEconomySeconds/60`. El trabajador humano recién unido y NPC tienen la misma tasa base; veteranos añaden exclusivamente sus perks individuales. Base por minuto: alimento 2,400; madera 1,800; piedra 1,400; mineral 650; conocimiento 1,200; trabajo de construcción 1,200 (milésimas). Minero divide su capacidad: desde era 3, 75 % en piedra y 25 % en mineral, con reasignación si uno está al máximo o no hay necesidad. Antes de era 3, 100 % piedra.

`OutputMilli = floor((workerSeconds * rateMilliPerMinute * economyBp * eraFacilityBp * governmentBp * priorityBp * starvationBp * penaltyBp) / (60 * 10000^N) + persistedRemainder)`, con cada término calculado en entero y redondeo final único; orden de multiplicadores fijo. La producción de humanos aplica perk de manera individual/por cohortes con mismo conjunto de perks, no a población entera. `facilityBoostBp` se suma para un máximo +3000bp. Bonificaciones de oficio individual con tope +1800bp; el total compuesto final de todos los bonus se recorta a 15000bp. Los NPC no obtienen habilidades.

## Desaceleración de masas
Cada ciudadano humano activo contribuye al trabajo agregado, pero su eficiencia marginal se atenúa para evitar ventaja lineal de 10.000 espectadores. Primeros 100 activos por oficio al 100%; del 101 al 2500 al 25%; a partir del 2501 solo representación y progreso personal reducido si estaba activo, sin creación adicional de recursos. El orden de asignación de cuotas es `(activeSinceUtc, citizenId)` determinista, reponderado cada tick; se conserva XP conforme a contribución efectiva. Los números no determinan resultados de torneo, que usan una decisión por nación.

## Mantenimiento, hambre y bloqueo
La población inicial tiene 24 NPC, repartidos 7/5/4/4/4. Mantenimiento alimentario: 150 milésimas por NPC y por unidad de trabajador humano **efectivo** y por minuto de economía, con máximo de 50 unidades humanas imputables al mantenimiento para que un gran chat no produzca inanición por participación visual sin trabajo. Primero se consume alimento; si hay déficit parcial, se aplica productividad colectiva 65 % al segmento posterior. Nunca hay muertes. Las misiones no regalan oro. Los NPC pueden construir todas las obras básicas. Las fuentes naturales siempre permiten producir `food`, `wood`, `stone`, `knowledge` desde el comienzo sin edificios, para evitar el bloqueo circular «no hay edificio para producir materiales necesarios para construir un edificio». `ore` se desbloquea en era 3.

## Capacidad y planificador
Capacidades base por nación: food/wood/stone/ore = 3500 unidades; knowledge = 15000 unidades. `storage` agrega +1500 unidades en todos los almacenes ordinarios, +350 por era posterior. No se produce un recurso que alcanzó máximo; NPC se reasignan a recurso válido (prioridad comida, materiales necesarios, investigación, construcción); el humano conserva familia y no produce cuando su output está saturado. Nunca se pierde silenciosamente una producción: contabilizar `blockedByCapacity` separado de `produced` y de XP.

## Bootstrap y progresión
Se empieza con **cero recursos y cero edificios**, pero una zona natural de cada profesión, 24 habitantes NPC y capacidad de almacén base virtual (terreno/capacidad de supervivencia). El `Autoplanner` arranca edificios en cuanto exista material y trabajo; reservas y commit de costes son atómicos. La economía offline al 20 % permite completar la ruta gratuita de cinco hitos por era sin humanos, aunque tardará significativamente más; el cambio de era requiere volver a LIVE.

## Invariantes contables
`stock >= reserved >= 0`; `stock = initial + sum(verified productive events + mission rewards - consumption - building spends - penalties)`. Cada evento se aplica una sola vez. La falta de suministro no hace stock negativo. `gold` no participa en fórmulas de producción, ejército, progreso ni votaciones ciudadanas. Reversiones generan asiento corrector, jamás eliminación de asientos originales. El subledger oro se reconcilia contra contributions identificadas; la deuda de reversos se almacena aparte cuando ya no hay saldo.

## Balance candidato y ciclo de ajustes
Era 1 exige producir 6.400 alimento, 4.750 madera, 3.420 piedra y 2.650 conocimiento, además de la tecnología básica, del edificio cívico automático y de una misión colectiva; cada una de las cinco categorías da 20 puntos. Eras sucesivas aumentan umbrales linealmente. Progresión objetivo aproximada de 2,5 días/era es hipótesis de diseño y puede no cumplirse con cualquier reparto: antes de LIVE se ejecutan simulaciones de 7/24, 24/0, 100/0 y 10000/0 humanos/NPC, buffers bajos, hambre, offline al 20 %. Toda nueva calibración versiona `rulesetId`; nunca aplicar ajustes económicos mid-season sin regla de migración públicamente comunicada.



---


<!-- Documento fuente: docs/05_EDIFICIOS_Y_MAPA.md -->


# 05 — Construcciones básicas, proyectos y mapa

## Catálogos
`data/buildings.v2.json` declara 130 edificios básicos explícitos (10 familias x 13 eras), cada uno con precio por recurso, trabajo, 4 etapas, era de desbloqueo, capacidad, footprint y efecto. `data/strategic_projects.v2.json` declara 39 proyectos optativos (3 x era) más 13 maravillas exclusivas opcionales. Todos los edificios anteriores permanecen y conservan sus efectos con productividad relativa de 80 % al quedar obsoletos; no se destruyen automáticamente.

## Algoritmo de autoconstrucción básico
Cada 60s de reloj de economía (o cuando se desbloquea nueva era), el planificador inspecciona y añade como máximo dos planes básicos, respetando `maxConcurrentWorks=5` y `maxAutoQueued=2`. Prioridades ordenadas: `food_production` si comida insuficiente/capacidad de trabajo, `storage` si utilización de cualquier stock > 75 %, `housing` si NPC en límite y alimentación sostenible, `extraction/forestry` si faltan materiales para obra pendiente, `research` si conocimiento insuficiente, `workshop` si facility boost bajo, `civic` de era actual si pendiente, `defense` después, `infrastructure` al final. A igual prioridad elegir costo menor y después `buildingId` lexical. Siempre que una obra obligatoria resulte materialmente imposible por su propia dependencia, usar fuente natural gratuita y guardar `WaitingResources` sin crear materiales sintéticos. `civic` de cada era no necesita una tecnología que requiera completar su mismo hito.

El costo ordinario se reserva al planificar y se descuenta **una vez** cuando empieza la obra; producción de construcción separada en `buildWorkUnits`, no compra materiales otra vez. Fallos de arranque cancelan reserva antes del commit; edificios que no encuentran parcela esperan en `WaitingPlot` y generan expansión determinista, nunca se pierden recursos.

## Estrategias
Cada era ofrece hasta tres alternativas de su familia de proyectos (`memorial/spectacle/archive`). El Consejo **solo abre** si hay tres alternativas distintas sin construir, todas individualmente financiables con saldo *disponible*. La reserva durante voto es el máximo componente a componente de cada vector de coste (`max(costO1[r], costO2[r], costO3[r])`). Si durante la votación no llega papeleta, se selecciona una de las tres de modo uniforme, auditado por RNG y seed; el coste ganador se descuenta de la misma reserva vectorial y el exceso se libera. Votación = 600s LIVE por nación. Nadie puede comprar votos. Si el voto pierde financiación por reverso oro, cierre = `PaymentBlocked` y se cancela sin descontar, con anuncio.

Como se pueden aprobar varias obras en distintos ciclos, hasta cinco obras avanzan simultáneamente si hay trabajadores. Una sola votación estratégica está abierta por nación para evitar dobles reservas. Las maravillas son proyectos separados de festival (no consumen una de las tres alternativas del Consejo) y requieren su propio evento programado; primera nación en completar y reclamar atómicamente obtiene la única maravilla global. Las otras pueden conservar la obra como monumento no exclusivo sin premio de exclusividad y sin reembolso, informado antes de construir.

## Construcción visual
Cuatro etapas según progreso de trabajo: 0–15 % parcela/cimientos, 15–40 % armazón, 40–70 % obra, 70–100 % remate. En 100 % se añade `BuildingCompleted` y se activa efecto. Se renderiza sin pathfinding por cada NPC, y la animación jamás determina productividad. `BuildingInstance` conserva era de origen, nivel, transform y slot de trama estable.

## Mapa procedural y representación
Semilla de temporada, mapa inicial 48×48 casillas, proyección de tile 32×16 y altura de capas decorativas. Expansión en un margen de ocho casillas por lado por era, con tope 256×256. Algoritmo reproducible: hash de `(seed,nation,x,y,layer)`, ruido de 2 octavas en celdas, máscara de terreno totalmente edificable en al menos 70 % del mapa; todas las naciones tienen igual **número y disponibilidad de parcelas lógicas**, bioma solo estético. Parcelas y colisiones de servicios son compartidas, efectos de área normalizados por nación. Si no cabe construir, expandir y buscar primera parcela libre `(distanceFromCenter, y, x)`; no bloquear progreso por cosmética.

## Retrocompatibilidad
La persistencia de edificio histórico no autoriza producir por encima de la capacidad de almacén. Los nuevos edificios hacen más eficiente a cada familia con techo +3000bp, y el antiguo conserva un factor relativo de 80 % para que lo nuevo tenga sentido sin castigar al espectador con destrucciones visuales.



---


<!-- Documento fuente: docs/06_PROFESIONES_HABILIDADES_Y_XP.md -->


# 06 — Ciudadanos, profesión única, XP y especializaciones

`!join` registra una identidad verificada de canal; no asigna oficio ni inicia producción. `!work <familia>` elige única familia durante temporada. Repetir la misma familia o `!active` prolonga `activeUntilUtc=receivedUtc+7200s` tras validación y cooldown de 60s; escoger otra familia devuelve `PROFESSION_LOCKED` sin renovar. El tiempo de trabajo no se acumula: renovar no añade dos horas al saldo previo. Una inscripción tardía puede participar en votos mientras el período esté abierto.

## Niveles
Al terminar cada segmento de trabajo efectivo, `xp += floor(6 * effectiveWorkMinutes)` con resto persistido; la XP off-live recibe factor 0,2. Nivel N requiere XP acumulada `250*(N-1)^2`, hasta nivel 20. Activación, voto, chat, caminar y renderizar no dan XP. Las recompensas de misión pueden otorgar XP si están explícitas; default de v2.0: misiones colectivas solo recursos, no XP adicional, para no duplicar. Los NPC no suben niveles ni desbloquean skills.

## Árboles
Tres elecciones irreversibles en niveles 3, 7 y 12; dos opciones exactas por bifurcación. `data/skills.v2.json` fija 30 habilidades, cada una con efecto objetivo y `additiveBp`. Los efectos son **personales**: no existen auras de reducción colectiva que crezcan sin techo con miles de usuarios. Habilidades históricas de 'rationing', 'reuse' e 'innovator' se redefinen como productividad/eficiencia individual equivalente sin impacto monetario, manteniendo intención temática pero eliminando exploit de multiplicación global. Máximo acumulado +1800bp por ciudadano. Sin `!skill`, no se asigna nada. Al volver a temporada siguiente se conserva historial de elecciones en museo, no se conserva bonus.

## Familias
- food: alimento de terreno o edificio según era, con sprite cazador→síntesis.
- wood: madera/biomasa; la etiqueta cambia, el resourceId `wood` no cambia.
- mine: piedra y mineral (mineral desde era 3), sin material por época arbitrario.
- build: aporta `buildWorkMilli` a obras comprometidas; si no hay obras, no crea recursos, pero puede hacer animación de mantenimiento y no gana XP por tarea ficticia.
- research: genera conocimiento con acumulación y desbloqueos automatizados gratuitos de tecnología.

## Control de audiencia masiva
Cada identidad puede tener un ciudadano por nación/temporada dentro de reglas de asignación de canales. Para trabajo agregado hay 100 plazas de contribución plena por profesión y 2400 plazas marginales al 25 %. Un humano fuera del tope sigue apareciendo, votando y alcanzando logros sin crear recursos ficticios; para evitar falsos mensajes de progreso se le muestra explícitamente el estado «turno visual / lista de trabajo saturada» y no se le abona XP de trabajo inexistente. El algoritmo de cuotas deterministic permite rotación por bloques de 10 minutos de LIVE para que los últimos usuarios no queden siempre sin producción; orden de rotación `(hash(citizenId,rotationIndex),citizenId)`.

## Trabajo y sueño
El ciudadano descansa exactamente al caducar `activeUntilUtc`. Un evento de plataforma retrasado no vuelve a activar una ventana del pasado más allá del límite de tolerancia. No hay muerte permanente ni barras de hambre individuales. El nombre visual es moderado; se registra ID interno separadamente del displayName público.



---


<!-- Documento fuente: docs/07_PROGRESION_TECNOLOGICA_Y_TEMPORADAS.md -->


# 07 — Progresión histórica, investigación y temporadas

## Eras y victoria
13 épocas (orden congelado en `eras.v2.json`): paleolithic, neolithic, copper, bronze, iron, antiquity, medieval, renaissance, industrial, modern, digital, space, interstellar. Todos los mundos inician la primera época en un commit global. `EraReadyPending` se alcanza al reunir 100 puntos y se confirma nueva era únicamente con nación LIVE. La **primera entrada confirmada en `interstellar`** fija ganador y termina la competición de inmediato. La era final sirve como epílogo visual y archivo, **no abre elecciones ni un nuevo ciclo jugable**, excepción imprescindible para no contradecir el cierre al entrar en ella.

## Hitos y barra
Cada era jugable (1–12) tiene cinco hitos únicos de 20 puntos: producción de comida; producción de madera **y** piedra; conocimiento + investigación básica completada; finalización del ágora cívica automática; y primera misión colectiva completada durante esa era. La misión puede ser diaria o semanal, pero solo puntúa una vez por era. Los objetivos cuantitativos son `data/milestones.v2.json`. Se contabilizan unidades **producidas efectivamente y aceptadas** en esa era, no entradas de misiones ni consumos, y por eso no pueden repetirse para acelerar. Los 100 puntos no se multiplican por audiencia ni por donaciones. Los hitos cumplidos fuera de emisión se guardan; la ceremonia queda pendiente. El hito de era interestelar está materializado como catálogo de epílogo, no es exigido para ganar.

## Árbol tecnológico
Para cada era: 1 investigación automática de ruta gratuita `tech_{era}` y 2 opcionales de economía/defensa, todas sin oro. Conocimiento producido se almacena y gasta; la investigación automática se inicia si hay conocimiento después de respetar reservas de obras. Ninguna tecnología es prerrequisito circular de los hitos del mismo período. Las ramas optionales se anuncian; no retrasan la entrada a era siguiente. La prioridad votada no bloquea caminos, solo bonifica temporalmente una categoría.

## Rendimiento y duración
El objetivo narrativo son 2–3 días por era, no una promesa técnica. El baseline fija 20 % de economía offline y umbrales lineales; el balance real depende de horas de directo, espectadores y distribución de profesiones. Para reducir dependencia de audiencia masiva, los hitos no escalonan por cantidad de participantes, y el trabajo extra tiene rendimiento marginal decreciente. Solo se cambiarán valores entre temporadas tras una simulación completa de todos los hitos; cambios intratemporada requieren evento de migración auditado y anuncio.

## Cierre y persistencia
Al cerrar temporada se publica `SeasonCompleted`: nación ganadora, fecha, reglas y hashes, estadísticas de trabajo, economía, obras, elecciones y torneos; se convierte oro sin gastar en puntuación de prestigio visual 1:1, sin opción de canje y sin bonus en la siguiente carrera. No migran recursos, edificios, XP ni profesiones; sí identidad de proveedor para facilitar recuperar usuario, historial de logros, badges y estadísticas. Los ciudadanos de la nueva temporada son registros nuevos asociados a la identidad previa.



---


<!-- Documento fuente: docs/08_GOBIERNO_VOTACIONES_Y_CONSEJO.md -->


# 08 — Elecciones NPC, prioridades y Consejo de Construcción

## Gobiernos
Tres candidatos NPC recurrentes por nación y era jugable: económico, militar y científico. No son espectadores, no ocupan tres cargos simultáneos y no vetan decisiones comunitarias. La elección se abre al entrar en era 2–12, durante 3600s de LiveClock. En era 1 se abre inmediatamente al comenzar la temporada con LIVE; en era 13 se omite, ya que la temporada concluye al entrar. Pueden votar todos los ciudadanos registrados en esa nación antes del cierre, incluso si están descansando; una papeleta vigente por ciudadano, actualizable mediante `!gov economy|military|science`. En igualdad de máximos se abre segunda vuelta solo entre empatados durante 180s LIVE; en igualdad persistente se usa sorteo uniforme, auditado; sin un solo voto se sortea uniformemente entre los tres.

## Bonificaciones exactas
Gobierno económico: +300bp (3 %) al output ordinario `food/wood/stone/ore`. Gobierno científico: +300bp a `knowledge`. Gobierno militar: +500bp a puntos **defensivos de unidades NPC** durante eventos programados; no afecta RPS. Estos efectos no conceden puntos históricos automáticos ni cambian votos, oro, costes de proveedor o economía de otra nación. El bono permanece durante la era a partir del cierre de elección; antes de cierre no existe bonus. Los títulos y ropa evolucionan según época sin sustituir identidad del NPC.

## Prioridad de nación
Tras resolverse la elección (incluida segunda vuelta), se abre votación independiente de 300s LIVE `!priority economy|science|defense`. Un ciudadano puede cambiar su voto antes de cierre. Prioridad económica: +800bp a recursos ordinarios; ciencia: +800bp a conocimiento; defensa: +800bp a defensa NPC de eventos programados. Dura 5400s de LiveClock desde cierre y expira aunque se haya cambiado de era (si hay transición temprana, se cancela al comenzar nueva era). Sin votos: elección por rotación reproducible entre ramas, sin sesgo de audiencia. En empate: sorteo uniforme entre empatadas. No se concede nada si termina la temporada.

## Consejo Estratégico
Doctor K-0 puede convocar un Consejo cuando hay exactamente 3 opciones distintas, desbloqueadas, sin construir y **costeables individualmente**, con al menos 3 proyectos disponibles según catálogo. Si no se satisfacen condiciones, muestra «proyectos pendientes de recursos» y no abre votación. Durante 600s LIVE cada ciudadano puede votar/reemplazar `!build projectId`; al cerrar se selecciona mayoría o desempate determinista, se cobra **solo** el proyecto vencedor y se libera la diferencia de la reserva vectorial. Si no hay votos, sorteo uniforme entre 3. Una sola votación estratégica abierta por nación; varias **construcciones** aprobadas pueden progresar a la vez. Las elecciones NPC, prioridades y Consejos no se solapan dentro de la misma nación: `PoliticalScheduler` serializa elección→prioridad→Consejo en cola. Las sanciones de torneo no alteran ventanas de voto.

## Conflictos y reloj
Votos con `receivedUtc < closeUtc` y LIVE Confirmed en recepción entran. Votos retrasados o duplicados no cambian resultado. Si cae fuente LIVE, la ventana se congela y puede reanudarse. Un cierre se hace en transacción con lock de votación y certificado de resultado (`counts`, `eligible`, `seedCounter`, `rulesetHash`). Una transacción no puede cargar oro dos veces ni crear una construcción mientras el Consejo permanezca OPEN.



---


<!-- Documento fuente: docs/09_TORNEOS_EVENTOS_Y_MISIONES.md -->


# 09 — Torneos, sanciones, eventos y misiones

## RPS triangular exacto
Se anuncia un torneo programado solo cuando las tres naciones están LIVE confirmadas; cada encuentro tiene 5 rondas de 90s LIVE de voto y descansos de 30s LIVE, más máximo 2 rondas extraordinarias para desempate de la cabeza. Cada nación toma el `rock/paper/scissors` mayoritario entre ciudadanos únicos (`!rps` primera papeleta válida irrevocable); no se muestra ninguna distribución antes del cierre, solo el número total de votantes. Empate interno: RNG uniforme reproducible entre opciones empatadas. Sin votos, opción `PASS`, nunca voto NPC inventado.

## Sistema triangular
Resolver **tres enfrentamientos por parejas** A-B, B-C y C-A. En cada enfrentamiento victoria=2 puntos, empate misma elección=1 a cada nación, derrota=0; opción PASS pierde frente a una opción válida (0–2), PASS vs PASS da 0–0. Cuando las tres naciones escogen rock-paper-scissors distintas, cada una gana una vez y pierde otra, por tanto 2 puntos, no se inventa ganador. Se suman puntos de 5 rondas, y solo si hay empate por primer puesto se disputan 2 rondas extraordinarias. Si continúa el empate, declarar victoria compartida sin castigos y sin «moneda al aire». La mayoría interna no multiplica puntos por total de espectadores, eliminando la ventaja automática de audiencia bruta.

## Derrota y territorio
Solo hay sanción material a una nación con menos puntos que **un ganador único**; derrota = pérdida del 2 % de `wood/stone` **disponibles** con redondeo hacia abajo y tope en saldo; jamás oro, conocimiento, edificios ni ciudadanos. Sanción territorial: elegir sector no esencial con máximo 10 % del output ordinario de la nación; ese sector no produce durante 1800s `NationActivePenaltyClock`, que solo avanza cuando la nación está LIVE, no offline. Si no hay sector secundario válido se muestra penalización visual y no se corta una fuente natural obligatoria para progresar. Un empate no genera penalización.

## Eventos fuera de torneos
Únicamente eventos preautorizados de `events.v2.json` activados por `ShowDirector` u operador, con anuncio previo y cooldown; nada de agresiones automáticas, fauna hostil permanente o desastres espontáneos. `catchup_challenge` se ofrece solo a naciones al menos 2 eras retrasadas, máximo 2 veces en temporada, +5 % NPC durante 30 minutos LIVE, sin puntos históricos directos ni oro. `resource_storm` es evento anunciado de reducción temporal moderada, frecuencia máxima cada 12 horas LIVE; `wildlife_parade` cosmético; `wonder_festival` abre actividad especial de maravilla si las reglas lo admiten.

## Misiones
Tres tipos diarios y dos semanales definidos en `missions.v2.json`. Periodos UTC completos: día desde 00:00 UTC; semana desde lunes 00:00 UTC. Los NPC pueden progresar y completar objetivos colectivos cuando no hay público; recompensas automáticas por nación una sola vez por instancia; al expirar la ventana se descarta misión no completada. Recompensas son materiales ordinarios no restringidos por monetización y **no añaden puntos a la barra de hitos**. Recompensas que excedan almacén se recortan con `rewardOverflowDiscarded`, auditado.



---


<!-- Documento fuente: docs/10_MONETIZACION_LEDGER_Y_CONTRIBUCIONES.md -->


# 10 — Monetización verificable, ledger y límites

## Criterio de elegibilidad
`ContributionEvent` proviene de canal con `contributions` habilitado por operador; se requiere autenticación del origen, identificador estable, evidencia verificable del tipo/importe, estado económico final admisible y `conversionRuleVersion` activa para esa **plataforma, canal, tipo y moneda/unidad**. No se deduce equivalencia por texto libre, reacción, follower ni cantidad de likes. El proveedor puede cambiar campos, permisos, elegibilidad y reglas. Por defecto **todos los tipos reales de monetización están deshabilitados**, y no hay cambio automático a habilitado sin prueba con cuenta real. El juego gratuito funciona íntegramente así.

## Conversión y ejemplos
Conversión exacta por `provider, eventType, unit, ruleVersion`: `goldUnits=floor(verifiedAmountMinorUnits * numerator / denominator)`; guardar resto solo dentro del evento y sin inventar crédito. La configuración demo exclusivamente sintética define `provider=simulated, unit=DEMO, eventType=test_contribution, numerator=1, denominator=1`, a usar únicamente bajo `mode=SIMULATION`, jamás en entorno LIVE. Para plataformas reales se publica tabla tras revisar APIs y términos, no se escriben tasas falsas ni se atribuyen precios a regalos. Nunca se hacen conversiones genéricas entre monedas de proveedores.

## Estados de ingreso
`RECEIVED → AUTHENTICATED → VERIFIED → CREDITED` o `REJECTED`; también `REVERSED` tras `CREDITED` si existe evidencia de devolución/cancelación. Un evento reintentado produce un solo crédito gracias a unique `(provider, eventId, channelId, eventType)`. `CREDITED` añade al ledger oro y a tesorería de nación, no al bolsillo individual del donante. Cambio posterior de reglas no recalcula histórico.

## Reversos tras gasto
Si una reversión deja sin cobertura el hold de una votación abierta, la votación se cancela en la misma transacción y el hold se libera antes del asiento de reverso. Si se revierte el oro ya gastado, el saldo disponible se reduce hasta cero y el resto se registra como `goldDebtUnits` sin saldo negativo y sin tocar construcciones completadas; los siguientes ingresos verificables pagan deuda primero. El patronazgo queda marcado `reversed` y puede perder el reconocimiento visual conforme a política anunciada; no hay devolución automática por el videojuego ni política de compensación externa. La contabilidad interna del oro nunca reclama ser un balance de dinero fiduciario.

## Protección de jugador y monetización sana
Prohibido transferir oro, convertirlo en dinero real, apuestas, premios de valor real, bonificación de voto o condición de avanzar de era. Los proyectos con oro son puramente estéticos/prestigio; ganar no se compra. UI muestra claramente si la cuenta no tiene donaciones habilitadas. Mostrar estado de agradecimiento privado y nombres solo con moderación y criterios de privacidad. Cualquier funcionamiento de monetización requiere revisión legal, fiscal, de proveedor y tests de auditoría; estas condiciones no son definibles por documentos internos.



---


<!-- Documento fuente: docs/11_DIRECTOR_DOCTOR_K0_Y_MODERACION.md -->


# 11 — Doctor K-0, narrativa y control de actos

Doctor K-0 es un cyborg científico físico dentro de las tres representaciones del mundo, con rostro mecánico, un ojo óptico, extremidades de ingeniería y cápsula de voz, nunca mascota blanda o Corálido. Su voz es sarcástica/provocadora, neutra respecto a las facciones y nunca utiliza insultos discriminatorios, burlas a donantes por no pagar ni afirmaciones falsas sobre apoyo económico.

## Arquitectura del show
`ShowDirector` decide eventos dentro de whitelist y cooldown; genera `Cue` tipado (`era_ready`, `government_open`, `government_result`, `priority_open`, `strategic_available`, `strategic_result`, `tournament_start`, `tournament_result`, `food_crisis`, `storage_full`, `season_completed`, `safe_idle`). `NarrationService` produce texto desde plantillas primero; LLM opcional solo reescribe tonos dentro de plantilla permitida, no crea reglas, saldos, ganadores ni acciones. `TTS` reemplazable con caché por hash de frase y voz; si falla, subtítulo y sonido local. Estado de narración `PENDING → READY → PLAYING → DONE | SKIPPED`, y límite 1 cue prioritario cada 20 segundos con cola máxima 20, descartando cosméticos viejos y nunca eventos financieros.

## Moderación y datos personales
DisplayName se sanitiza (control chars, URLs, PII básica y palabras prohibidas) antes de entrar a sprite, placa o speech; retener el identificador estable internamente con seudonimización/criptografía. Comandos y regalos no permiten inyectar instrucciones al LLM. No envíe chat bruto a LLM salvo consentimiento/configuración aprobada; preferir datos agregados. Perfiles, stats y nombres borrables/redactables sin romper ledger contable. Errores de comunicación a chat son *best effort*, no deben provocar reintento de transacción de juego.

## Plantillas canónicas
- `join`: «¡{displayName}! Bienvenido al experimento. Elige oficio: food, wood, mine, build o research con !work.»
- `profession_locked`: «Profesión fijada esta temporada. Usa !active para volver al trabajo.»
- `era_ready`: «La ciencia empuja a {nationName} al límite... esperaremos al directo para cambiar de era.»
- `vote_open`: «Tres obras financiables. Solo una será aprobada. ¡Tenéis diez minutos de emisión!»
- `season_end`: «El experimento tiene ganador: {nationName}. Todo queda registrado. No hay reinicio de memoria histórica.»

El operador tiene siempre botón `MuteNarration`, `PauseSource`, `CancelEvent`, `SafeScene`, `EmergencyStop`. Todas las acciones quedan registradas con actor, motivo y timestamp.



---


<!-- Documento fuente: docs/12_UX_PIXELART_Y_ASSETS.md -->


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



---


<!-- Documento fuente: docs/13_ARQUITECTURA_APIS_Y_ESTADOS.md -->


# 13 — Arquitectura modular, dominio y APIs

## Despliegue de referencia
Monolito modular en .NET 10 con tres procesos lógicos `ApiHost`, `SimulationWorker` y `ConnectorWorker` (en MVP pueden ser un ejecutable con HostedServices), PostgreSQL, SignalR, React/TypeScript y Phaser 4 sujeto a prueba de OBS CEF. No usar Kafka, RabbitMQ, Redis, Kubernetes ni event sourcing completo hasta demostrarse necesidad. Inbox/Outbox PostgreSQL permite idempotencia y recuperación.

## Módulos y dependencias
`IdentityAndBindings` (asignación canal y cuentas), `Citizens` (usuarios/oficios/XP), `Simulation` (scheduler, clocks, work aggregation), `Economy` (balances/consumo/ledger), `Buildings` (autoplanner y construcción), `History` (hitos/eras), `Politics` (elección y prioridad), `StrategicCouncil` (holds/votos), `Competitions` (RPS/sanciones), `MissionEngine`, `ShowDirector`, `PlatformAdapters`, `ReadModels` y `Operator`. Cada módulo expone comandos y eventos, no acceso directo a repositorio de otro módulo. Core no importa Phaser ni SDK de plataforma. IDs UUID y referencia a `season_id + nation_id` en cualquier agregado perteneciente a nación.

## Consistencia
`Inbox` guarda el raw mínimo + `sourceKey` único; actor lógico single-writer por nación y lock de exclusividad en la DB; las operaciones compartidas de maravillas/ganador tienen transacción global y lock de temporada. `Outbox` publica evento con id estable tras commit; duplicaciones de emisión no afectan estado. Ante despliegue horizontal posterior usar lease-epoch/fencing antes de levantar otro escritor. Nunca ejecutar dos instancias con escritores sin fencing. Recursos en milésimas, oro en unidades enteras separadas.

## API y SignalR
Contratos en `contracts/openapi.v2.yaml`, `contracts/normalized_event.schema.json`, `contracts/nation_delta.schema.json`, `contracts/channel_binding.schema.json`, `contracts/ruleset.schema.json`; JSON v2 con `schemaVersion`, `eventId`, `seasonId`, `nationId`, `sequence`, UTC ISO8601. `/api/v2/operator` exige acceso privilegiado; `/api/v2/public` ofrece únicamente proyecciones. SignalR grupos `season:{id}:nation:{id}:public`, `season:{id}:operator` y `output:{id}`; no publicar IDs de proveedor ni texto raw. Clientes reconectan enviando `lastSequence`, recuperan snapshot y deltas posteriores; si hueco fuera del retention, solicitan snapshot completo.

## Contratos de error
Respuesta estándar `{code,message,correlationId,retryable}`; códigos predecibles `NOT_REGISTERED`, `PROFESSION_LOCKED`, `VOTE_NOT_OPEN`, `OUT_OF_WINDOW`, `EVENT_DUPLICATE`, `SOURCE_UNAUTHORIZED`, `BALANCE_HOLD_CONFLICT`, `GOLD_RULE_DISABLED`, `LIVE_NOT_CONFIRMED`, `CONTENT_HASH_MISMATCH`, `RULESET_INVALID`, `RUNNING_SEASON_IMMUTABLE`. Prohibido devolver secretos o payload de chat bruto.



---


<!-- Documento fuente: docs/14_SEGURIDAD_PRIVACIDAD_Y_OPERACION.md -->


# 14 — Seguridad, privacidad, infraestructura y continuidad

## Amenazas críticas
Eventos simulados como aportaciones, abuso de chat, replay, doble aprobación de obras, cambio no autorizado de binding, spoofing de canal, privilegios de operador, inyección por displayName a TTS/LLM y pérdida del estado. Todos los accesos externos pasan por validación, autenticidad del proveedor y `sourceKey` deduplicado. Secrets en un gestor de secretos o variables inyectadas por orquestación, nunca en JSON distribuido. Tiempos UTC; firewall DB no expuesta; TLS en endpoint público; MFA para operador; red mínima entre procesos.

## Acceso y segregación
Roles `viewer`, `moderator` (silenciar nombres), `operator` (iniciar/detener/votar eventos autorizados), `owner` (modificar bindings y tasas de monetización), `auditor` (solo lectura ledger). Todas las acciones mutadoras con `idempotencyKey`, actor, razón y registro append-only. `Contributions` solo pasa a Verified desde adaptador con `capability` habilitada y prueba de autoridad; la UI del operador NO dispone de botón para crear oro real. En simulación puede inyectarse oro demo a un ledger namespace separado que jamás se fusiona con producción.

## Retención
Minimizar PII: hash estable de ID del proveedor para correlación y token cifrado en vault; displayName moderado no es clave. Retención propuesta: eventos de chat sin relevancia 7 días, raw validado de comandos 30 días, métricas agregadas 13 meses, ledger y eventos financieros según obligación legal aplicable (no fijar periodo sin asesoría jurisdiccional). Permitir anonimizar nombres públicos sin reescribir ledger. Publicación de política de privacidad y procedimiento de eliminación antes del primer directo real.

## Hosting y backups
Docker Compose local con PostgreSQL. Inicialmente una VM única EU con servicios separados por contenedor, volumen PostgreSQL y backups diarios cifrados fuera del host; respaldos de WAL/PITR si la pérdida tolerable obliga. RPO objetivo de diseño 15 min y RTO 2h, NO garantías demostradas. Cada 30 días realizar restauración simulada contra DB vacía y comparar cuentas, ledger y checksum de snapshot. Cualquier test fallido bloquea monetización. Nunca compartir tokens OBS o OAuth en repositorio.

## Despliegue y rollback
Pipeline: lint/json-schema → tests de contenido → tests del motor → migración en staging → snapshot DB → arranque versión con contrato compatible → health gates → rollout controlado. No migrar esquema mientras se procesa inbox sin compatibilidad. Para cambios de `rulesetHash` detener nueva temporada y crear ruleset nuevo; las temporadas RUNNING quedan fijadas. Feature flags por canal no deben alterar las reglas ya congeladas de una nación.

## Costes e IA
Presupuestos sólo estimables tras benchmark de CPU, nº de canales/eventos y TTS. Cada mensaje narrado puede salir por plantilla offline; LLM es opcional con límite de gasto diario y fallo seguro. La infraestructura no debe quedar funcionando 24/7 sin supervisión del operador durante la fase de pruebas monetizadas.



---


<!-- Documento fuente: docs/15_PRUEBAS_Y_CIERRE_DE_DEFINICION.md -->


# 15 — Pruebas automáticas y criterios de aceptación

## Tests contractuales necesarios
V2-T01 92 decisiones preservadas; V2-T02 tres facciones exactamente y sin atributos de ventaja; V2-T03 cualquier mezcla de tres canales válida y duplicación del mismo canal rechazada; V2-T04 13 eras con cinco profesiones; V2-T05 todas las eras 1–12 tienen 5 hitos sumando 100 y camino sin gold; V2-T06 cada era tiene al menos tres proyectos estratégicos + 10 edificios básicos; V2-T07 30 skills, elegir máximo una por tier, límite de bp; V2-T08 todas las recetas con costes enteros ≥0 y sin oro en básicos; V2-T09 golpes RPS 3 elecciones distintas empatan, primera papeleta única, cero sin espectadores no inventa votos; V2-T10 ventana !active 7200s UTC, caduca offline; V2-T11 gobierno 3600s, runoff 180s, Consejo 600s, penalización 1800s live-only; V2-T12 ningún recurso negativo ni pago duplicado; V2-T13 primera entrada a última era cierra temporada sin abrir elecciones; V2-T14 auditoría de determinismo al repetir mismo flujo y seed.

## Matriz de carga y fallos antes de LIVE
- Carga de 24 NPC, +10/100/1000/10000 activos; CPU, memoria, latencia de inbox y delta, latencia OBS, límites de sprites.
- Caída a mitad de una papeleta, reconexión Twitch sin replay, YouTube cursor caducado, eventos duplicados, origen no autenticado, segundos perdidos en `UNCERTAIN`, reinicio de DB.
- Proyecto votado y tres transacciones concurrentes (oro reversado y edificio automático): debe haber una sola deducción, sin saldos negativos.
- dos naciones compiten en completar maravilla/era final simultáneamente: exactamente un ganador en DB.
- 7 días offline con hambre y capacidad saturada: no deadlock permanente y no saltar de era si no hay LIVE.
- Restauración PITR de base de datos en entorno aislado, verificación de hashes, reconciliación de ledger; se mide RPO/RTO real.
- Políticas Twitch, TikTok y YouTube revisadas en fecha de directo para canales concretos; sin este gate monetización/simulcasting OFF.

## Criterio de '100 % definido'
El canon funcional puede considerarse cerrado cuando cada entidad y comando tenga contrato, cada output numérico tenga regla y cada transición tenga test. **Eso no equivale a producto terminado**. Siguen pendientes pruebas externas (credenciales/capacidades LIVE reales, validez legal, rendimiento de Phaser en versión CEF de OBS, sprites visualmente aprobados). Se listan en `audit/EXTERNAL_GATES.md`, no como valores `null` del ruleset.



---


<!-- Documento fuente: docs/16_INTEGRACIONES_Y_CUMPLIMIENTO.md -->


# 16 — Capacidades LIVE verificables y políticas

## Principio de proveedor intercambiable
La simulación no incluye SDKs de plataformas. `IPlatformAdapter` declara capacidades independientes `chat_read`, `stream_presence`, `message_write`, `monetary_events`, `verification`, `cursor_resume` y `identity_stability`. El operador no puede activar una función si el adaptador y la autorización de canal no demuestran ambos soporte. Ningún fallback a scraping ilegítimo. `ChannelBinding` es configuración, no garantía de acceso LIVE.

## Twitch
EventSub es at-least-once, puede repetir `message_id` y **no garantiza replay de eventos perdidos durante una desconexión total de WebSocket**; por eso inbox deduplicada, re-suscripción, health state `UNCERTAIN` y no fabricar papeletas. Documentación: https://dev.twitch.tv/docs/eventsub/ y https://dev.twitch.tv/docs/eventsub/handling-websocket-events/ . Las capacidades de bits/cheers son independientes de chat y requieren permisos adecuados, configuración y prueba. Las políticas de simulcast deben revisarse antes de mostrar mensajes de otras plataformas en una salida Twitch: https://help.twitch.tv/s/article/simulcasting-guidelines .

## YouTube
El chat LIVE se puede consultar mediante `liveChatMessages.streamList` o `list` con `nextPageToken` cuando esté disponible; no se asume historial ilimitado ni que el token resuelva todas las desconexiones. Documentación: https://developers.google.com/youtube/v3/live/docs/liveChatMessages/list . Monetización requiere visibilidad y permisos de canal, con validación por evento concreto. Un mensaje que parezca pagado no se considera verificado por texto.

## TikTok
No dar por hecho una API LIVE pública que entregue chat y regalos con acceso comercial general a cualquier cuenta. Cada conector debe mostrar evidencia documental y permisos para la cuenta concreta, o quedar en `NOT_AVAILABLE`. Queda prohibido activar créditos de oro con librerías no oficiales sin revisión de legitimidad, integridad y términos. El modo con tres cuentas TikTok es **topológicamente compatible**, no necesariamente integrable hoy sin acceso autorizado.

## Política de salida por canal
La nación se asocia a `providerChannelId`. Una salida puede mostrar la propia facción y resumen agregado de rivales, pero no mezcla automáticamente chat crudo, mensajes, avatares o llamadas a seguir otro canal. `overlayPolicyVersion` se valida según destino. Los regalos de otra cuenta no se atribuyen a la nación receptora, aunque el broadcast los vea: autoridad siempre basada en `binding` del origen.

## Checklist para habilitar canal
1. Documentación oficial vigente revisada.
2. Token con scopes mínimos por canal (cuando proceda).
3. Mensaje real leído, deduplicado y asociado a UserId estable.
4. Pérdida de conexión y reconexión manejadas sin replay fingido.
5. Mensaje de escritura, si existe, probada de forma opcional.
6. Aportación real verificada, reverso y regla de conversión aprobada, o `monetizationEnabled=false`.
7. Revisión de cumplimiento de salida y moderación.
8. Registro `CapabilityEvidence` versionado con fecha, URL y operador que lo certificó.



---


<!-- Documento fuente: docs/17_OPERADOR_ESCENARIOS_Y_DIAGRAMA_E2E.md -->


# 17 — Runbook del operador y flujos E2E

## Preparación
Crear temporada DRAFT y asignar 3 facciones. Elegir tres canales distintos, o simulados, y comprobar health por rol. Crear mapas a partir del mismo `seasonSeed` pero visualmente distintos por bioma. Revisar documentalmente que reglas y catálogos concuerden, y dejar constancia de los cambios antes de abrir una temporada. Registrar `rulesetHash`, `contentHash`, versión de motor y modo monetario. Iniciar solo tras ver 3 naciones PREPARED y snapshots iniciales.

## Secuencia A — ciudadano
Llega evento chat verificado `!join` → persistir inbox unique → resolver canal a nación → crear `Citizen` si no existe → emitir `CitizenJoined` → respuesta visual K-0. `!work food` → fijar profesión si nula → `activeUntilUtc=now+7200` → participa en la economía en siguiente segmento → XP desde trabajo efectivo, nunca por el chat. Duplicar mismo evento: `EVENT_DUPLICATE` sin segundo ciudadano/XP. Repetir `!work mine` después de seleccionar food: rechazo sin renovar actividad.

## Secuencia B — transición de era
5 hitos se completan, otorgando 20 puntos cada uno. Si offline, `EraReadyPending`; en próxima señal LIVE confirmada, tomar lock nación y temporada, comprobar que no está COMPLETED, hacer `EraAdvanced` transaccional, extender mapa, recalcular etiquetas de profesión y abrir elecciones por 3600s LIVE. Después prioridad 300s, sin solapar con Consejo. Si `EraAdvanced` entra en interstellar, emitir `SeasonCompleted` y **no** abrir elección nueva.

## Secuencia C — gasto estratégico
Tres opciones financiables → tomar hold vectorial → abrir Consejo durante 600s LIVE → registrar/reemplazar votos → cerrar con recuento → validar hold+saldo tras posibles reversos → gastar una sola vez ganador con ledger → crear `ConstructionQueued` → liberar hold restante → emitir Outbox al OBS. Si se cae la señal, se congela ventana; si no se dispone de oro suficiente al cerrar, marcar `PaymentBlocked` y no crear obra.

## Secuencia D — fallo de proveedor
`HEALTHY → UNCERTAIN` ante ausencia de heartbeat/credenciales; detener ingreso de votos de fuente sin autoridad, pausar LiveClock y penalizaciones; offline economy 20 % y conservar último snapshot. Reautorizar y volver LIVE con evento auditado sin inventar comandos perdidos. Reintentos de webhook deduplicados. Si todas las fuentes no están confirmadas, torneo global se aplaza.

## Secuencia E — operador
Botón `EmergencyStop` inhibe nuevos eventos y congela escrituras de juego de forma ordenada; permitir persistencia/outbox ya confirmada. `Resume` exige health y DB reconciliada. `AbortSeason` no borra movimientos; cambia estado con motivo y resultado vacío. `PublishScene` solo modifica presentación, nunca saldos.



---


<!-- Documento fuente: docs/18_DECISIONES_DE_BASE_CORREGIDAS.md -->


# 18 — Correcciones estructurales realizadas en v2.0

## Ajustes deliberados y por qué

| ADR | Antes | Ahora | Motivo | Impacto |
|---|---|---|---|---|
| V2-001 | Nación equivale a una plataforma | Nación independiente de canal; bindings configurables | tres cuentas en una misma plataforma | cambio de clave de datos y DTO |
| V2-002 | Oro estratégico podría mejorar carrera | solo visual/prestigio | evitar ventaja de pago sobre victoria | cambia magnitud de mejoras estratégicas; no el voto |
| V2-003 | Era final con posible elección y temporada acabada | entrada final cierra inmediatamente; sin gobierno final | eliminar estado imposible de juego cerrado y elección | excepción ceremonial documentada |
| V2-004 | Técnicas/effects `null` | reglas completas con valores v2 | permitir implementación inequívoca | balance candidato versionado |
| V2-005 | Skills colectivas multiplicables | efectos personales con techo | evitar beneficio infinito 10k ciudadanos | reinterpretación de descripciones temáticas |
| V2-006 | Proyectos con 3 candidatos quizá no accesibles | exactamente 3 proyectos estratégicos por era, si hay oro; ruta gratuita separada | votaciones no bloquean progreso | contenido cerrado |
| V2-007 | Mundo comienza sin infraestructura, podría no producir | zonas naturales gratuitas con capacidad de supervivencia | evitar deadlock de primera madera/piedra | se mantiene evolución desde cero recursos y edificios |
| V2-008 | Economía y penalización fuera de emisión ambiguas | UTC/live/economy/activePenalty separados | reanudación consistente | semántica estable |
| V2-009 | Reversos pueden causar saldo negativo | deuda separada de reversos | mantener invariante de no-negativos | ledger adicional |
| V2-010 | Candidata Ferrina `Perla` evocaba coral | pasa a `Nera`, demás nombres heredados | evitar diseño Corálido descartado | nombre artístico propuesto cerrado v2 |
| V2-011 | Falta exactitud de RPS cíclico | puntuación 2-1-0 por pares y empates compartidos | no inventar ganador en ciclo | reglamento completo |
| V2-012 | Simular todos los usuarios físicamente | trabajo por cohortes, sprites LOD | reducir CPU y minimizar ventaja de masa | representación consistente |

## Jerarquía
Las 92 decisiones originales se preservan literalmente en `data/legacy_user_decisions_1_92.json` y se relacionan en `audit/decision_traceability.json`. La **nueva instrucción expresa del usuario** modifica la asignación rígida plataformas→naciones (antiguos supuestos); no reemplaza el número de naciones, las tres facciones, las reglas sociales ni la independencia de los mundos. Ninguna otra regla original se cambia sin registrar su motivo.

## Qué sigue fuera de posibilidad de un texto
No se puede validar por escrito la licencia de API de una cuenta, tasas financieras reales, carga del hardware de emisión, arte final aprobado ni obligaciones jurídicas sin información externa específica. Eso queda en `audit/EXTERNAL_GATES.md` y NO supone un agujero en la definición de reglas del juego.



---


<!-- Documento fuente: docs/19_MAQUINAS_DE_ESTADO_Y_ERRORES.md -->


# 19 — Máquinas de estados y rechazos (contrato de dominio)

## Ciudadano
`UNREGISTERED --!join--> JOINED_NO_PROFESSION --!work(valid)--> ACTIVE --UTC expiry--> RESTING --!active or !work(same)--> ACTIVE`. `!work(different)` desde ACTIVE/RESTING rechaza `PROFESSION_LOCKED`. Ciudadanos no se borran por desconexión ni falta de alimentos. En cierre, `ARCHIVED` conserva historial y stats; siguiente temporada crea ciudadano nuevo.

## Elecciones y votaciones
`QUEUED → OPEN → RESOLVED`; `OPEN → PAUSED` si nación LIVE desaparece, `PAUSED → OPEN` cuando regresa; `OPEN/PAUSED → CANCELLED` solo por operador con motivo. Consejo además `RESOLVED → PAYMENT_BLOCKED` si reverso simultáneo invalida la reserva; no se crea proyecto. `BALLOT` debe referenciar voto abierto, opción admisible, ciudadano de nación, input deduplicado y sello LIVE válido. En `RPS`, una primera papeleta válida es irrevocable; en `GOVERNMENT`, `PRIORITY` y `STRATEGIC` la última papeleta válida sustituye la anterior en la misma fila. `GOVERNMENT_RUNOFF` solo ofrece previamente empatados.

## Obra
`WAITING_RESOURCES → WAITING_PLOT → QUEUED → BUILDING → COMPLETED`; una obra puede saltar WAITING_PLOT si parcela disponible, pero nunca saltarse el pago. Costes se comprometen atómicamente una vez al entrar QUEUED; construcción por tramos visuales; `CANCELLED` antes de pagar libera reserva, después de pagar solo permitido por fallo grave y con compensación auditable que no deshaga trabajos anteriores.

## Cuenta monetaria
`RECEIVED → AUTHENTICATED → VERIFIED → CREDITED → REVERSED` o ramas a `REJECTED`; no se puede ir de `REJECTED` a `CREDITED` sin evento nuevo firmado y referencia a rectificación. `REVERSED` no reabre `CREDITED`. Todos los movimientos contabilizados con causa estable; una segunda notificación del mismo proveedor no crea oro.

## Sesión de directo
`OFFLINE_CONFIRMED → LIVE_CONFIRMED` requiere evidencia y TTL, `LIVE_CONFIRMED → UNCERTAIN` si señal/autoridad pierde health, `UNCERTAIN → LIVE_CONFIRMED` solo al recuperar evidencia. `UNCERTAIN → OFFLINE_CONFIRMED` tras confirmación de fin de emisión o caducidad de TTL. Manual override solo para modo SIMULATED o con autorización operador auditada; un override no valida contribuciones financieras.

## Fin de carrera
`RUNNING` con tres naciones activas → `EraAdvanced to interstellar` → `SeasonWinnerClaim` (unique season) → `COMPLETED`; winner se registra antes de guardar Outbox. Los ticks posteriores no pueden reabrir gobierno ni extender construcción competitiva. `COMPLETED → ARCHIVED` tras cierre y snapshot; no existe `COMPLETED → RUNNING`.

## Errores canónicos
`IDENTITY_NOT_VERIFIED`, `BINDING_NOT_FOUND`, `BINDING_DUPLICATE`, `BINDING_IMMUTABLE`, `CITIZEN_NOT_JOINED`, `PROFESSION_ALREADY_ASSIGNED`, `PROFESSION_LOCKED`, `ACTIVITY_COOLDOWN`, `ACTIVITY_EXPIRED`, `SKILL_LEVEL_LOW`, `SKILL_TIER_ALREADY_CHOSEN`, `SKILL_WRONG_FAMILY`, `VOTE_NOT_OPEN`, `OUT_OF_WINDOW`, `BALLOT_INVALID_OPTION`, `RPS_ALREADY_VOTED`, `EVENT_DUPLICATE`, `EVENT_TOO_OLD`, `STREAM_NOT_CONFIRMED`, `SOURCE_UNAUTHORIZED`, `PROJECT_NOT_AFFORDABLE`, `PROJECT_THREE_OPTIONS_REQUIRED`, `HOLD_CONFLICT`, `CONTRIBUTION_NOT_VERIFIED`, `GOLD_CONVERSION_DISABLED`, `GOLD_REVERSAL_UNBACKED`, `SEASON_ALREADY_COMPLETED`, `RULESET_HASH_MISMATCH`, `MIGRATION_REQUIRED`, `WRITER_FENCING_ERROR`. La respuesta pública describe el motivo sin IDs privados ni detalles financieros.



---


<!-- Documento fuente: docs/20_PANTALLAS_PANEL_OPERADOR_Y_ROLES.md -->


# 20 — UX de jugador, escenas OBS y panel de operador

## Escenas públicas
- **UniverseOverview**: tres naciones en miniatura, era, barra 0–100 y estado LIVE, ganador o empate; solo metadatos agregados compartibles.
- **NationWorldVertical**: mundo 66 %, HUD superior 14 %, HUD inferior 20 %; zona de cámara sigue obras/visitas de K-0, viewport lógico 360x640.
- **NationWorldHorizontal**: 73 % viewport, 27 % panel lateral, 640x360 lógico; componentes reposicionados, no escalados arbitrariamente.
- **ElectionOverlay**: tres candidatos, tiempo LIVE restante, recuento total y porcentajes permitidos después de cierre.
- **StrategicCouncilOverlay**: tres alternativas, costes ordinarios y oro, aviso «opcional/estético», timer 10min y estado de reserva.
- **TournamentOverlay**: tres equipos, votos totales por nación, ocultación de opciones hasta cierre, puntuación de duelos por parejas y penalizaciones activas.
- **SeasonFinale**: ganador, estadísticas y museo con historial sin saldo de oro como moneda útil.

## Controles de operador
Login MFA con rol; tabla de cuentas asociadas (provider/channel, LiveHealth, capabilities, token TTL con secretos ocultos), reglas hash, versión de cada adaptador, simulación clock, health DB y outbox, backlog de eventos, contador de reintentos, gastos TTS. Acciones: PREPARE, START, PAUSE, RESUME, SCHEDULE_EVENT, SCHEDULE_TOURNAMENT, CANCEL_VOTE (motivo), SAFE_SCENE, MUTE_K0, EMERGENCY_STOP, ARCHIVE, EXPORT_AUDIT. Toda acción exige idempotencyKey, confirmación UI cuando tiene efecto económico y log; no existe botón para «dar oro» en producción.

## Onboarding para monetizar a otros creadores
Primera edición de producto es un solo creador/campaña con exactamente tres facciones. Cuando se comercialice, añadir `Tenant`, billing/licencias, aislamiento de credenciales por tenant, cuota de canales, RLS/particionamiento si hay evidencia. No diseñar cross-tenant billing en MVP. Cada creador puede escoger qué tres cuentas conectar, sin alterar los oficios ni las identidades de facción.

## Accesibilidad y degradación
Narración siempre subtitulada; no comunicar éxito únicamente por color, feedback de comandos válido en HUD incluso si la plataforma no autoriza responder al chat. Reducir efectos luminosos y FPS en OBS bajo carga sin tocar tick backend. El lector de pantalla del panel de operador accede a etiquetas y countdown; overlays públicos son imágenes audiovisuales pero acompañados de panel textual.



---


<!-- Documento fuente: docs/21_MAPAS_Y_SEMILLAS_DETERMINISTAS.md -->


# 21 — Generación de mapa completamente determinista

## Reglas de terreno
El mapa es una **cuadrícula lógica universal edificable**. El bioma inicial cambia exclusivamente el aspecto y nunca las coordenadas disponibles. Tamaño inicial 48×48 casillas (`x=0..47`,`y=0..47`), centro = `(23,23)`. Al desbloquear era N el ancho y alto pasan a `48 + 16*(N-1)`, centrando la región inicial sin mover los edificios existentes en coordenadas de mundo; límite absoluto 256×256 (era 13 = 240×240). Las coordenadas lógicas absolutas pueden ser negativas al expandir a ambos lados de (0,0); no serializar offsets de cámara como coordenadas de edificio.

## Determinismo de decoración
`terrainVariant = SHA256(utf8('{seasonSeed}|{nationId}|{x}|{y}|terrain'))[0] % 4` ; `decorationPresent = SHA256(utf8('{seasonSeed}|{nationId}|{x}|{y}|deco'))[0] % 10 == 0`; `decorationVariant = digest[1] % 8`. Todos los hashes se computan en UTF-8 con IDs normalizados, bytes iniciales sin signo. Las decoraciones no impiden construir y desaparecen si la parcela se ocupa; se guarda en evento de presentación para animar. No se utiliza ruido Perlin, dependencia de motor gráfico o `Random()` para elegir recursos económicos.

## Ubicación de edificios
Se reserva un rectángulo de `footprintTiles` sin solapamientos de otras parcelas de edificios ni la plaza de arranque (3×3 libre alrededor de `(23,23)`). Buscar en orden `(distance=abs(x-23)+abs(y-23), y, x)` dentro de los límites, con `x/y` representando la esquina inferior izquierda de la huella; el primero que cabe gana. Al expandir, el edificio anterior conserva coordenadas y parcela. Si no cabe aún, `WAITING_PLOT` hasta expansión; no gastar materiales antes de disponer de parcela. Las obras automáticas obligatorias pueden tener reservados 2 slots de emergencia alrededor de área central para impedir bloqueo por obras cosméticas; esos slots se desbloquean al acabar la era.

## Reproducción visual
El cliente puede desplazar cámara y LOD libremente; nunca enviar coordenadas de render como verdad económica. Misma semilla y mismos edificios deben reproducir el mismo mapa lógico con cualquier proveedor de streaming. La apariencia de cada bioma usa paleta propia pero límites de construcción iguales.



---


<!-- Documento fuente: docs/22_METRICAS_CARGA_Y_CALIBRACION.md -->


# 22 — Plan cuantitativo de balance, carga y latencia

## Métricas obligatorias
`chaos_inbox_lag_seconds`, `chaos_inbound_duplicate_rate`, `chaos_tick_duration_ms`, `chaos_nation_simulated_seconds`, `chaos_rule_rejections_total{code}`, `chaos_era_duration_hours`, `chaos_era_cumulative_resource_produced`, `chaos_worker_effective_units`, `chaos_hunger_segments`, `chaos_storage_blocked_units`, `chaos_outbox_pending`, `chaos_gold_credit_unique`, `chaos_gold_debt_units`, `chaos_vote_close_lag_ms`, `chaos_obs_fps`, `chaos_tts_spend`, `chaos_backup_last_success`, `chaos_lease_epoch`. No usar IDs de usuario en etiquetas de métricas para evitar cardinalidad alta y filtraciones.

## Umbrales operativos iniciales, no evidencia medida
Tick CPU objetivo <50ms por nación a carga mediana, P95 Inbox-to-simulation <1s, P95 public delta <2s, cola outbox sin crecer durante 15min de carga, 30 FPS OBS estable durante 1 hora por salida con baseline 90 sprites horizontales /45 verticales; permitir degradación visual progresiva sin alterar economía. Estas cifras son SLO **propuestos** para implementar tests, no garantías.

## Balance de carrera
Correr tres mundos con la misma seed y perfiles (0 humanos/24 NPC, 10/24, 100/24, 1000/24, 10000/24). Medir 13 cambios de era con 1h LIVE/día, 4h LIVE/día y 24h LIVE/día; simular pausas, capacidad máxima y misión diaria que vence antes del hito. Criterio de liveness: el escenario 0 humanos/24 NPC no queda bloqueado por falta de oro, madera, piedra, conocimiento ni edificios; solo puede esperar a LIVE para confirmar cambio de era. Criterio de justicia de torneo: tamaño de audiencia no cambia puntuación RPS dado mismo reparto relativo de votos.

## Optimización
Conservar `NationSimulation` de escritor único. Agrupar humanos por `(profession,bonusSet,activeTo,quotaClass)` y remanentes enteros por grupo, no iterar 100.000 sprites. Construcción y pathfinding client-side aproximados. Primero medir DB contention, CPU del escritor y coste de SignalR; separar process worker/web y añadir fencing antes de considerar colas externas.



---


<!-- Documento fuente: docs/23_GLOSARIO_JERARQUIA_Y_LIMITE_DE_DISENO.md -->


# 23 — Glosario, jerarquía de decisiones y alcance documental

**Estado:** definición documental v2.1. No se propone código ni una nueva mecánica. Fuente principal: reglas históricas 1–92, documentos 01–22 de v2.0 y catálogos de `data/`.

## Diccionario obligatorio

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

## Jerarquía de fuentes

1. Última instrucción explícita del propietario del proyecto.
2. Decisiones originales registradas (92) que no hayan sido sustituidas expresamente.
3. Reglas canónicas de v2.0 y correcciones registradas en `docs/18`.
4. Datos estructurados con valores numéricos (`data/ruleset.v2.json` y catálogos canónicos).
5. Ampliaciones documentales de v2.1, exclusivamente cuando aclaren el diseño sin cambiar su semántica.
6. Ejemplos ilustrativos y propuestas futuras (no prevalecen).

Si una tabla descriptiva y el JSON canónico difieren en una cifra, **no se improvisa**: se registra una discrepancia, se congela el cambio y se adopta una revisión consistente. No existe una jerarquía en la que un documento de estética autorice a conceder recursos, oro, votos o puntos.

## Qué significa «completado»

Una mecánica se considera documentada cuando identifica sujeto, disparador, entradas, condiciones, resultado, límites, errores, persistencia, pantalla y su criterio de aceptación. La documentación podrá ser exhaustiva en intención y decisiones, pero **no certifica** que una API externa funcione, que el servidor escale o que un sprite tenga calidad artística. Esos hechos pertenecen a validación futura.

## Fuera de alcance de esta fase

No crear repositorios, backend, cliente, scripts Python, tests ejecutables, Docker Compose, CI/CD ni configuraciones con secretos. Es válido conservar SQL como **modelo de datos propuesto** y JSON/YAML de contratos y catálogos como **definición declarativa**, sin ejecutar ninguno. La documentación no se debe confundir con una aplicación funcional.



---


<!-- Documento fuente: docs/24_RECORRIDOS_ESPECTADOR_Y_CIUDADANIA.md -->


# 24 — Recorridos del espectador y experiencia del ciudadano

**Objetivo:** cerrar la experiencia observable por un usuario en chat sin depender de cómo se implemente la integración. Se mantiene una identidad de ciudadanía por nación y temporada; la existencia de distintas cuentas no altera la pertenencia de la nación.

## Usuario nuevo

1. Descubre un directo asociado a una nación y ve en el HUD: nombre de la civilización, era, progreso, estado actual y ayuda de comandos.
2. Emite `!join` desde una identidad reconocida por el proveedor y el sistema crea o devuelve su ciudadano, sin duplicados por reintento.
3. Si no eligió oficio, la interfaz invita a usar `!work food`, `!work wood`, `!work mine`, `!work build` o `!work research` (adaptar los alias a los comandos registrados, sin alterar semántica).
4. La profesión elegida se mantiene hasta fin de temporada. Volver a usar el mismo oficio renueva actividad cuando cumple cooldown; cambiar a otra familia debe producir rechazo comprensible.
5. Si el usuario está activo, trabaja durante su ventana real de dos horas. El avatar puede no estar entre los sprites visibles porque existen límites de densidad: nunca se interpreta como expulsión de la economía.

**Feedback visual mínimo:** confirmación de alta, profesión válida, duración restante de actividad, nivel, habilidades disponibles y resultado de cualquier comando. Si el proveedor prohíbe respuesta por chat, el feedback se presenta en la UI del juego; no se inventa un mensaje enviable.

## Usuario recurrente

Al volver al directo, el usuario recupera identidad por identificador estable del proveedor, no por nombre visible; conserva progreso durante la temporada. `!active` renueva actividad tras validación. Si cambió su nombre público, no se crea otro ciudadano. Si cambia de dispositivo sin cambiar de cuenta, tampoco. No se promete fusionar automáticamente identidades de TikTok, Twitch y YouTube.

## Usuario con varias cuentas o canales

Un canal concreto se asigna a una sola nación por temporada. La misma cuenta del proveedor puede participar en naciones diferentes solo cuando sus canales correspondientes se asignan a ellas; las estadísticas permanecen separadas. Varias cuentas de un mismo ser humano no son identificables con certeza y no debe prometerse prevención absoluta del multicuenta.

Una cuenta de creador puede aparecer en distintas escenas OBS; ello no implica que los espectadores adquieran identidades compartidas entre canales.

## Participación política y social

Durante elecciones, el HUD ofrece tres candidaturas NPC, su categoría (economía, ejército, ciencia), el tiempo LIVE restante y la forma de votar. Un usuario tiene como máximo una papeleta efectiva que puede reemplazar según la regla canónica. Los empates pasan a segunda vuelta; el resultado y las bonificaciones se hacen públicos al cerrarse. La prioridad tecnológica se vota en una ventana independiente y breve. No se debe sugerir que el gobernador controla la economía a voluntad: únicamente concede el bono pasivo definido.

En Consejo, el usuario ve tres **proyectos elegibles y costeables**, sus costes, el carácter opcional y la cuenta atrás de diez minutos LIVE. El usuario vota; al cierre se carga únicamente el vencedor, no las tres opciones. Si la nación no tiene recursos para tres propuestas, el Consejo se pospone; no se reemplaza por una oferta imposible ni por una petición obligatoria de donaciones.

En torneo, el usuario ve `!rps`, las tres opciones y la regla de voto irrevocable. La distribución exacta de elecciones se mantiene oculta hasta el cierre para evitar arrastre estratégico. Las decisiones de la audiencia no cambian la potencia base de las especies ni el cálculo del ranking de puntos por pareja.

## Situaciones de excepción y mensajes orientados al usuario

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

## Aceptación editorial

Las etiquetas de profesión, era y edificaciones deben diferenciarse de las claves internas; los errores no enseñan UUID, tokens ni SQL. Todo cambio autoritativo relevante se representa con una señal visible o texto subtitulado: alta, subida de nivel, inicio y fin de votación, edificio terminado, nueva era, penalización y victoria.



---


<!-- Documento fuente: docs/25_BIBLIA_NARRATIVA_UNIVERSO_Y_PERSONAJES.md -->


# 25 — Biblia narrativa del experimento

**Estado:** dirección narrativa editorial v2.1. Expande la presentación sin introducir mecánicas nuevas. El tono es ciencia ficción cómica, no simulación de historia humana literal. Las 13 eras representan analogías de avance tecnológico para especies propias.

## Premisa

Project CHAOS es un experimento competitivo televisado sobre tres civilizaciones inteligentes que comienzan con recursos y tecnologías elementales. La pregunta dramática es qué comunidad aprende antes a dominar su entorno y alcanzar el horizonte interestelar. El espectáculo lo presenta Doctor K-0, investigador cyborg obsesionado con registrar resultados, sorpresas y comportamientos emergentes. Nunca se usa la narración para falsear los números de la partida.

## Doce reglas de continuidad de ficción

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

## Micelios

Criaturas fungoides terrestres, anatomía compacta y silueta con capuchón esporado. Su cultura considera el territorio una red de colaboración y transformación. Arquitectura de fibras, raíces, membranas y biofotones. No son corales ni un pueblo submarino; no obtienen ventajas de producción agrícola sobre las demás. El léxico editorial gira en torno a «red», «brotes», «tejidos», «cultivo» y «simbiosis», sin sugerir que son una mente colmena que invalida a los ciudadanos individuales.

## Rúnicos

Seres minerales inteligentes de cuerpos geométricos, grietas luminosas y marcas rúnicas. Su arquitectura evoluciona desde menhires y talleres pétreos hasta complejos cristalinos y computación de patrones. La estética no debe convertir sus runas en magia que conceda poderes inexistentes: «runa» designa su lenguaje visual de conocimiento y memoria. Su léxico incluye «grabado», «resonancia», «estrato», «archivo» y «forma».

## Ferrinos

Criaturas biológicas recubiertas por exoesqueletos ferruginosos con articulaciones expresivas, no robots ni corales. Sus ciudades muestran remaches, pliegues, forjas y, en eras avanzadas, superficies orgánicas metalizadas. El metal es identidad visual, no un multiplicador minero oculto. Léxico recomendado: «forja», «coraza», «horno», «articulación», «alianza».

## Doctor K-0

Es el hilo conductor del espectáculo: científico cyborg con elementos mecánicos inequívocos en cabeza, rostro y extremidades, silueta reconocible como sprite de baja resolución y retrato HUD. Personalidad irónica y teatral, pero siempre imparcial. No ridiculiza a una persona identificable, no expone pagos ni datos sensibles y no sugiere gasto como obligación para competir. Sus frases se generan o seleccionan a partir de hechos autorizados, siempre con versión subtitulada. La improvisación narrativa no forma parte del estado autoritativo.

## Arco por temporada

**Apertura:** presentación de las tres naciones y reglas. **Desarrollo:** oficios, primeras construcciones, retos y evolución estética. **Tensión:** elecciones, hitos próximos, torneos y posibilidades de remontada. **Clímax:** una nación entra en Era Interestelar. **Epílogo:** comparación, ceremonia de prestigio, museo de temporada y reinicio limpio de economía. No hay traspaso de oro o ventajas competitivas entre temporadas.

## Límites editoriales

Evitar referencias textuales o gráficas a franquicias externas, símbolos religiosos reales usados como facción, propaganda, humillación de donantes, lenguaje discriminatorio y afirmaciones de patrocinio no autorizado. Toda escena narrativa ha de poder emitirse con audio desactivado y subtítulos visibles.



---


<!-- Documento fuente: docs/26_BIBLIA_VISUAL_FACCIONES_EPOCAS_Y_SILUETAS.md -->


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



---


<!-- Documento fuente: docs/27_ESCENAS_PANTALLAS_Y_SECUENCIAS_PUBLICAS.md -->


# 27 — Especificación de escenas, pantallas y estados visibles

**Objetivo:** definir qué se debe ver en cada momento sin entregar componentes React, escenas Phaser ni archivos OBS. Las dimensiones son lógicas y se escalan con píxel más próximo.

## Matriz de escenas públicas

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

## HUD vertical 360 × 640

Reserva conceptual del documento fuente: 14 % superior (aprox. 90 píxeles lógicos), 66 % mundo (aprox. 422) y 20 % inferior (aprox. 128). Esto es una distribución de espacio, no coordenadas definitivas de sprites. El área superior nunca debe esconder la barra histórica; el área inferior prioriza comandos, votaciones y subtítulos; los eventos emergentes se apilan y caducan para no bloquear el centro.

**Jerarquía de información estable:** identidad de nación → era y barra → evento con tiempo límite → recursos relevantes → ciudadanos activos por oficio → narración/efectos. No mostrar simultáneamente barras de progreso contradictorias o mensajes que parezcan atribuir un chat a otra nación.

## HUD horizontal 640 × 360

Aproximadamente 73 % del ancho para el mundo y 27 % para panel lateral; mantiene las mismas métricas y estados, reorganizados. No se cambian reglas por proporción. La cámara puede mostrar más ciudadanos (objetivo 90 frente a 45), pero ambos visores consumen el mismo snapshot.

## Estados universales que todo componente debe representar

`LOADING`, `LIVE_CONFIRMED`, `OFFLINE_CONFIRMED`, `UNCERTAIN`, `PAUSED`, `DISCONNECTED`, `RECOVERING`, `DEGRADED`, `COMPLETED`. El operador tiene diagnóstico adicional; un espectador recibe mensajes comprensibles. Cada componente con un reloj distingue explícitamente **tiempo de directo** y **tiempo real**: nunca etiquetar «10 minutos» como tiempo UTC si una votación está pausada.

## Secuencias de interacción

**Al crear ciudadano:** pulso de llegada → confirmación de oficio pendiente → estado de actividad. **Al terminar edificio:** mejora visible de obra en etapas ya especificadas → evento de completado → icono de capacidad añadida. **Al entrar en era:** transición histórica sin borrado de recursos → cambio de paleta/estructuras → retomada de estado. **Al terminar temporada:** detener decisiones competitivas → animación final → museo → estado de campaña preparada para siguiente temporada.

## Reglas de accesibilidad visual

El color nunca es el único indicador; cada progreso tiene texto y forma. Las pistas sonoras tienen subtítulos equivalentes. Los controles de operador disponen de foco, labels y confirmaciones. Para personas sensibles al movimiento, priorizar reducción de destellos y cámara estable durante anuncios importantes.



---


<!-- Documento fuente: docs/28_NARRACION_K0_Y_DIRECCION_DEL_ESPECTACULO.md -->


# 28 — Libro de estilo y protocolo narrativo de Doctor K-0

**Estado:** especificación editorial. K-0 es narrador y agente de presentación; **no** autoriza comandos de dominio.

## Carácter fijo

Doctor K-0 es un científico cyborg reconocible, teatral, irónico y observador. No es villano, árbitro encubierto ni gestor de las aportaciones. Puede expresar sorpresa ante victorias inesperadas, burlarse suavemente de la complejidad de sus propias hipótesis y celebrar hitos de cualquier nación con el mismo entusiasmo base. Su neutralidad es requisito del espectáculo.

## Jerarquía de situaciones narrables

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

## Estructura de una intervención

**Entrada:** tipo de evento, nación, era, efectos autorizados, métricas agregadas y contexto visible. **Composición:** frase introductoria + hecho verificable + comentario breve opcional + cierre/llamada a participación si existe una acción válida. **Salida:** texto revisado/sanitizado, identificador de evento, duración estimada, subtítulos y pista de audio opcional. Evitar referencias a identidad personal o monto individual de una aportación.

**Ejemplo de tono, no texto fijo obligatorio:** «Registro del experimento: los Rúnicos han alcanzado una nueva era. Mis modelos ya están solicitando vacaciones». La narración de un resultado se ajusta a su estado y no concede bonus por el mero acto de pronunciarlo.

## Restricciones estrictas

No inventar resultados, victorias, gobiernos, tasas o datos de donación; no mostrar nombres ofensivos; no hacer afirmaciones médicas/financieras; no introducir instrucciones de gasto compulsivo; no producir logos ajenos sin derechos; no narrar mensajes externos en un overlay donde la política de plataforma lo prohíba. Un fallo de LLM/TTS se resuelve con plantilla determinista y subtítulos, sin detener la simulación.

## Catálogo editorial mínimo

Diseñar variantes de frase para: inicio de temporada, bienvenida por nación, nuevo ciudadano, profesión seleccionada, subida de nivel, habilidad disponible, saturación de almacén, escasez de comida, construcción iniciada y completada, elecciones abiertas y resueltas, Consejo retrasado por recursos, voto cerrado, torneo anunciado, ronda RPS resuelta, sanción territorial y expiración, misión diaria/semana completada, era preparada offline, era avanzada, maravilla reclamada, señal LIVE incierta, pausa de operador, reconexión, ganador y créditos. Cada variante posee gravedad, prioridad, longitud, idioma, subtítulo y caducidad de presentación.

## Sonido y subtítulos

La voz puede ser sintetizada o pregrabada; se debe conservar texto de subtítulo como fuente principal de accesibilidad. Los efectos críticos (voto, fin de era, error, torneo) requieren alternativa visual. Estilo sonoro: sintetizadores retro discretos, percusión suave, señales diferenciadas por facción sin convertir sonidos en ventajas competitivas. Las librerías musicales quedan fuera del alcance hasta verificar licencias.



---


<!-- Documento fuente: docs/29_ESTADOS_EXTREMOS_Y_FALLOS_EN_DIRECTO.md -->


# 29 — Matriz de casos límite y degradación funcional

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

## Política de claridad

La interfaz no debe afirmar «todo sigue en directo» si el origen está incierto. Una cámara congelada no significa economía congelada, ni una economía offline significa ventanas de voto abiertas. Para cada incidente se emite estado comprensible y diagnóstico técnico solo en panel del operador.

## Recuperación y doble aplicación

La recuperación parte de snapshot validado y eventos no comprometidos; si se desconoce si una operación económica se confirmó, se consulta su clave de idempotencia y asiento de ledger antes de actuar. Nunca se repiten manualmente aportaciones o votos «por si acaso». Los eventos de narración pueden reproducirse como comentario histórico, pero no reactivar efectos.

## Prueba documental exigida

Cada fila se transforma en un futuro caso de aceptación con un antes, evento, después, efectos permitidos, efectos prohibidos y criterio de observabilidad. Esta tabla no implica que ya existan pruebas ejecutadas.



---


<!-- Documento fuente: docs/30_ENTREGABLES_ARTISTICOS_Y_CRITERIOS_APROBACION.md -->


# 30 — Lista de entregables de arte, animación, mapa y audio

**Estado:** encargo artístico completo en intención; no se entregan sprites, voces ni música. El arte es un producto futuro y debe pasar revisión humana antes de considerarse aprobado.

## Matriz de sprites requerida

- **Ciudadanos:** 3 facciones × 13 eras × 5 profesiones = 195 combinaciones visuales; 4 orientaciones por combinación. Las herramientas evolucionan según profesión y época sin alterar colisiones.
- **Animaciones de ciudadano:** 9 acciones (`idle`, `walk`, `gather`, `haul`, `build`, `research`, `celebrate`, `rest`, `react`) con número de cuadros y FPS fijado en `art_spec.v2.json`.
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



---


<!-- Documento fuente: docs/31_DISENO_OPERATIVO_CUENTAS_Y_EMISIONES.md -->


# 31 — Diseño de emisión con una, dos o tres plataformas

**Propósito:** separar por completo las naciones de las plataformas y documentar cómo configurar cuentas sin inferir permisos reales de lectura LIVE.

## Modelo conceptual

- Cada temporada contiene exactamente tres naciones, pero cualquier plataforma puede aportar 0, 1, 2 o 3 cuentas; el máximo permitido por nación se rige por la regla canónica de `ChannelBinding`.
- Un `ChannelBinding` identifica proveedor, canal, permisos observados, fecha y revisión; no es el identificador de una nación.
- La autoridad de reloj de cada nación se establece expresamente en una fuente autenticada; dos cuentas no duplican segundos LIVE.
- Los visores OBS son salidas y pueden publicarse donde la cuenta tenga permiso; un visor no concede acceso al chat ni a monetización.
- Un mismo canal no se asigna a dos naciones en una temporada, evitando ciudadanía/votos ambiguos.

## Configuraciones previstas

| Modo | M | R | F | Observación |
|---|---|---|---|---|
| Tres cuentas del mismo proveedor | Twitch A | Twitch B | Twitch C | Tres identidades de canal distintas |
| Tres cuentas TikTok | TikTok A | TikTok B | TikTok C | Solo si lectura LIVE está autorizada y verificada |
| Tres canales YouTube | YouTube A | YouTube B | YouTube C | Una señal de reloj independiente por nación |
| Mixto | Twitch A | YouTube B | TikTok C | El overlay respeta las políticas de cada proveedor |
| Local de diseño | Simulado A | Simulado B | Simulado C | Sin identidad real ni donaciones ficticias válidas |

**Recomendación de producto:** elegir la topología de cuentas antes de preparar la temporada y congelarla al comenzar. Si cambia un canal por necesidad operativa, usar transición auditada y conservar ciudadanos existentes; no regenerar población y no cambiar la nación asignada a una cuenta ya utilizada.

## Ficha de configuración que debe cumplimentar un creador

Campaña y temporada; nación; proveedor; identificador del canal; dueño/autorización; capacidad de chat; capacidad de LIVE; capacidad de eventos económicos verificables; límite de términos de uso; canal de salida OBS; autoridad de reloj; zona horaria editorial; idiomas y permisos de moderación. Campos de permisos no verificados quedan `NO_CONFIRMED` y bloquean la funcionalidad dependiente, no se rellenan con valores de demostración.

## Si solo hay una emisión disponible

La experiencia puede mostrar las tres naciones en una misma escena pública **solo como presentación**, pero eso no resuelve cómo atribuir comandos a tres naciones dentro de un chat único. La regla canónica vigente exige que cada canal pertenezca a una única nación. Por lo tanto, una campaña con una sola cuenta para tres naciones requeriría **una decisión de producto adicional** (por ejemplo, prefijos de nación y votación por contexto), que NO está aprobada ni se presume implementada. En la versión documentada se usan tres fuentes para atribución clara, aunque todas sean del mismo proveedor.

## Seguridad, términos y comercialización

El diseño es compatible con adaptadores intercambiables, no con permisos universales inventados. Algunos servicios no facilitan de forma oficial todos los eventos que CHAOS desearía. La vinculación de una cuenta exige credenciales segregadas y consentimiento adecuado; revocar una cuenta desactiva sus capacidades sin destruir el estado histórico de la nación. Nunca prometer multistream, resúmenes cruzados de chat, lectura de regalos ni publicación automática si la plataforma no lo autoriza.



---


<!-- Documento fuente: docs/32_OPERADOR_GOBERNANZA_Y_CAMBIOS_EN_VIVO.md -->


# 32 — Responsabilidades del operador y gobierno del experimento

**Objetivo:** que el directo sea administrable sin controles capaces de alterar resultados arbitrariamente. No es una especificación de interfaz implementada.

## Roles de producto

- **Propietario:** configura temporada, reglas futuras, canales autorizados y condiciones de uso; no puede reescribir ledger histórico.
- **Operador:** abre/cierra escenas, programa eventos permitidos, atiende incidentes, pausa y reanuda; todas sus acciones críticas quedan auditadas.
- **Moderador de emisión:** interviene en contenido visible y nombres ofensivos; no cambia recursos, votos o victoria.
- **Observador técnico:** consulta diagnósticos sin capacidad de decidir resultados.
- **Ciudadano/espectador:** interactúa por sus comandos y votaciones; no tiene acceso a control interno ni credenciales.

## Límites de intervención

No se incluye un botón para crear oro, saltar de era, asignar ganador, alterar distribución RPS o forzar votos NPC. Las herramientas de operador autorizadas son las ya previstas: preparar/iniciar/pausar/reanudar temporada, programar evento y torneo, cancelar votación con motivo, silenciar K-0, cambiar a escena segura, detener ante emergencia y exportar auditoría.

Las correcciones extraordinarias usan un evento de compensación o una revisión de temporada y explican quién, cuándo, motivo y antes/después, en lugar de editar silenciosamente el estado. El panel debe distinguir `planeado`, `en curso`, `confirmado`, `fallido`, `cancelado` y `reintentable`.

## Libro de operación de un directo

**Antes:** comprobar fuente LIVE de cada nación, cuentas conectadas, estado de sincronización, versión de reglas, disponibilidad de voz/OBS, panel y backups. **Durante:** monitorizar latencia, cola, saturación, recursos y timers; anunciar resultados persistidos; resolver incidentes mediante escena segura. **Después:** cierre editorial, guardar resumen y revisar anomalías sin transferir saldos entre temporadas.

## Gestión de interrupciones

Una interrupción conocida de plataforma se declara `UNCERTAIN` cuando no puede demostrarse LIVE; los cronómetros se congelan aunque la audiencia crea ver vídeo. Cambiar autoridad de reloj exige transición privilegiada. El objetivo no es mantener apariencia de continuidad a cualquier coste, sino no causar perjuicio a votaciones por un fallo técnico.

## Métricas editoriales que interesa observar

Ciudadanos únicos por nación/temporada, tasa de creación a profesión, activos en últimas dos horas, ratio de completitud de misiones, tiempo hasta era, retraso en respuesta a comandos, porcentajes de abstención en votaciones, proporción de escenas informativas frente a simulación, incidentes de plataforma, eventos TTS fallidos y cambios de binding. Las métricas no sustituyen las reglas ni son instrucciones para manipular resultados.



---


<!-- Documento fuente: docs/33_NEGOCIO_MONETIZACION_PRIVACIDAD_Y_FUTURO_SAAS.md -->


# 33 — Modelo de negocio y límites de monetización

**Estado:** especificación de producto y riesgos. No constituye un dictamen fiscal ni garantiza acceso a ingresos externos.

## Dos modelos diferentes

**Juego para el creador:** espectadores participan gratuitamente en una competición de civilizaciones; algunas aportaciones monetarias autorizadas se transforman en oro de prestigio opcional. El oro no concede ninguna ventaja de victoria, investigación ni trabajo. El operador ve la procedencia y elegibilidad de un evento, sin mostrar públicamente datos personales del pagador.

**Producto de software futuro:** el creador de CHAOS podría licenciar o suscribir el sistema a otros streamers. Esa es una línea de negocio distinta de las aportaciones de sus espectadores. El MVP se diseña para una campaña única, con opción de introducir multi-tenant y facturación de software solo después de probar retención, operación y estabilidad.

## Principios de producto

1. Experiencia competitiva completa con 0 € y 0 espectadores gracias a los NPC.
2. Compra de reconocimiento visual y proyectos opcionales, nunca poder de victoria.
3. No pedir importes individualizados ni forzar que el público pague para desbloquear épocas.
4. El valor del oro depende de capacidad verificable del proveedor; no fingir conversiones de monetización.
5. El oro no se retira a dinero real ni se transfiere entre naciones, cuentas o temporadas como moneda funcional.
6. Reversos, duplicados y eventos no elegibles no pueden acreditar oro neto dos veces.
7. La privacidad y los términos locales tienen prioridad sobre la exhibición del donante.

## Oferta comercial futura (no implementada)

Para un producto licenciable, separar: licencia mensual por campaña/creador; límite de cuentas/canales autorizados según plan; marca de creador personalizable sin alterar el balance; exportación de estadísticas; tema visual bajo contrato; soporte y recuperación; cuotas de TTS y almacenamiento; política de uso y moderación. No prometer un precio, ROI o infraestructura específica sin investigación comercial.

## Decisiones que dependen de evidencia real

Permisos LIVE por proveedor, detalle de eventos monetarios, autorización de replay de mensajes, RGPD y retención, tratamiento de menores, impuestos y devoluciones. Estas cuestiones se registran como *gates* y no como texto de «cumplimiento resuelto». El diseño general sí puede establecer los principios de minimización, retención temporal, secretos protegidos y revocación de permisos.



---


<!-- Documento fuente: docs/34_CATALOGO_LEGIBLE_EDIFICIOS.md -->


# 34 — Catálogo legible de los 130 edificios básicos

**Estado:** transcripción documental del catálogo canónico `data/buildings.v2.json`; los números no son recomendaciones nuevas. **Unidad:** recursos ordinarios; `gold` no se usa en la construcción básica. Cualquier ajuste exige revisar el JSON fuente y registrar la revisión.

Cada edificio mantiene el mismo efecto lógico para las tres facciones; solo cambia la apariencia. Los edificios de épocas anteriores no se eliminan al avanzar de era: se les aplica el modificador de edificios antiguos previsto por las reglas. La cola automática obedece a límites de capacidad, recursos y emplazamiento; no construye si la operación compromete su propia precondición de coste.


## Era 1: Paleolítico

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `paleolithic_housing` | Habitáculos — Paleolítico | wood:50, stone:10 | 170 | [2, 2] | npcCapacity=8 |
| `paleolithic_food_production` | Centro alimentario — Paleolítico | wood:70, stone:15 | 190 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `paleolithic_forestry` | Estación de biomasa — Paleolítico | wood:65, stone:15 | 170 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `paleolithic_extraction` | Cantera y mina — Paleolítico | wood:65, stone:25 | 220 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `paleolithic_workshop` | Taller de herramientas — Paleolítico | wood:100, stone:50 | 260 | [3, 2] | facilityBoostBp=300 |
| `paleolithic_research` | Centro de saber — Paleolítico | wood:80, stone:50 | 250 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300 |
| `paleolithic_storage` | Almacén regional — Paleolítico | wood:90, stone:65 | 180 | [3, 3] | capacityAddEachResource=1500 |
| `paleolithic_infrastructure` | Vía logística — Paleolítico | wood:30, stone:35 | 90 | [1, 2] | logisticCapacity=12 |
| `paleolithic_civic` | Ágora comunitaria — Paleolítico | wood:130, stone:80 | 320 | [3, 3] | civicCapacity=1 |
| `paleolithic_defense` | Puesto defensivo — Paleolítico | wood:100, stone:95 | 280 | [2, 2] | defensePoints=14 |

## Era 2: Neolítico

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `neolithic_housing` | Habitáculos — Neolítico | wood:59, stone:11 | 195 | [2, 2] | npcCapacity=8 |
| `neolithic_food_production` | Centro alimentario — Neolítico | wood:82, stone:17 | 218 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `neolithic_forestry` | Estación de biomasa — Neolítico | wood:76, stone:17 | 195 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `neolithic_extraction` | Cantera y mina — Neolítico | wood:76, stone:29 | 253 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `neolithic_workshop` | Taller de herramientas — Neolítico | wood:118, stone:59 | 299 | [3, 2] | facilityBoostBp=300 |
| `neolithic_research` | Centro de saber — Neolítico | wood:94, stone:59 | 287 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300 |
| `neolithic_storage` | Almacén regional — Neolítico | wood:106, stone:76 | 207 | [3, 3] | capacityAddEachResource=1850 |
| `neolithic_infrastructure` | Vía logística — Neolítico | wood:35, stone:41 | 103 | [1, 2] | logisticCapacity=12 |
| `neolithic_civic` | Ágora comunitaria — Neolítico | wood:153, stone:94 | 368 | [3, 3] | civicCapacity=1 |
| `neolithic_defense` | Puesto defensivo — Neolítico | wood:118, stone:112 | 322 | [2, 2] | defensePoints=18 |

## Era 3: Edad del Cobre

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `copper_housing` | Habitáculos — Edad del Cobre | wood:68, stone:13 | 221 | [2, 2] | npcCapacity=8 |
| `copper_food_production` | Centro alimentario — Edad del Cobre | wood:95, stone:20 | 247 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `copper_forestry` | Estación de biomasa — Edad del Cobre | wood:88, stone:20 | 221 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `copper_extraction` | Cantera y mina — Edad del Cobre | wood:88, stone:34, ore:6 | 286 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `copper_workshop` | Taller de herramientas — Edad del Cobre | wood:136, stone:68, ore:20 | 338 | [3, 2] | facilityBoostBp=300 |
| `copper_research` | Centro de saber — Edad del Cobre | wood:108, stone:68, ore:27 | 325 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300 |
| `copper_storage` | Almacén regional — Edad del Cobre | wood:122, stone:88, ore:13 | 234 | [3, 3] | capacityAddEachResource=2200 |
| `copper_infrastructure` | Vía logística — Edad del Cobre | wood:40, stone:47, ore:6 | 117 | [1, 2] | logisticCapacity=12 |
| `copper_civic` | Ágora comunitaria — Edad del Cobre | wood:176, stone:108, ore:34 | 416 | [3, 3] | civicCapacity=1 |
| `copper_defense` | Puesto defensivo — Edad del Cobre | wood:136, stone:129, ore:47 | 364 | [2, 2] | defensePoints=22 |

## Era 4: Edad del Bronce

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `bronze_housing` | Habitáculos — Edad del Bronce | wood:77, stone:15 | 246 | [2, 2] | npcCapacity=8 |
| `bronze_food_production` | Centro alimentario — Edad del Bronce | wood:107, stone:23 | 275 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `bronze_forestry` | Estación de biomasa — Edad del Bronce | wood:100, stone:23 | 246 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `bronze_extraction` | Cantera y mina — Edad del Bronce | wood:100, stone:38, ore:7 | 319 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `bronze_workshop` | Taller de herramientas — Edad del Bronce | wood:154, stone:77, ore:23 | 377 | [3, 2] | facilityBoostBp=300 |
| `bronze_research` | Centro de saber — Edad del Bronce | wood:123, stone:77, ore:30 | 362 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300 |
| `bronze_storage` | Almacén regional — Edad del Bronce | wood:138, stone:100, ore:15 | 261 | [3, 3] | capacityAddEachResource=2550 |
| `bronze_infrastructure` | Vía logística — Edad del Bronce | wood:46, stone:53, ore:7 | 130 | [1, 2] | logisticCapacity=12 |
| `bronze_civic` | Ágora comunitaria — Edad del Bronce | wood:200, stone:123, ore:38 | 464 | [3, 3] | civicCapacity=1 |
| `bronze_defense` | Puesto defensivo — Edad del Bronce | wood:154, stone:146, ore:53 | 406 | [2, 2] | defensePoints=26 |

## Era 5: Edad del Hierro

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `iron_housing` | Habitáculos — Edad del Hierro | wood:86, stone:17 | 272 | [2, 2] | npcCapacity=8 |
| `iron_food_production` | Centro alimentario — Edad del Hierro | wood:120, stone:25 | 304 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `iron_forestry` | Estación de biomasa — Edad del Hierro | wood:111, stone:25 | 272 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `iron_extraction` | Cantera y mina — Edad del Hierro | wood:111, stone:43, ore:8 | 352 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `iron_workshop` | Taller de herramientas — Edad del Hierro | wood:172, stone:86, ore:25 | 416 | [3, 2] | facilityBoostBp=300 |
| `iron_research` | Centro de saber — Edad del Hierro | wood:137, stone:86, ore:34 | 400 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300 |
| `iron_storage` | Almacén regional — Edad del Hierro | wood:154, stone:111, ore:17 | 288 | [3, 3] | capacityAddEachResource=2900 |
| `iron_infrastructure` | Vía logística — Edad del Hierro | wood:51, stone:60, ore:8 | 144 | [1, 2] | logisticCapacity=12 |
| `iron_civic` | Ágora comunitaria — Edad del Hierro | wood:223, stone:137, ore:43 | 512 | [3, 3] | civicCapacity=1 |
| `iron_defense` | Puesto defensivo — Edad del Hierro | wood:172, stone:163, ore:60 | 448 | [2, 2] | defensePoints=30 |

## Era 6: Antigüedad

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `antiquity_housing` | Habitáculos — Antigüedad | wood:95, stone:19 | 297 | [2, 2] | npcCapacity=8 |
| `antiquity_food_production` | Centro alimentario — Antigüedad | wood:133, stone:28 | 332 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `antiquity_forestry` | Estación de biomasa — Antigüedad | wood:123, stone:28 | 297 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `antiquity_extraction` | Cantera y mina — Antigüedad | wood:123, stone:47, ore:9 | 385 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `antiquity_workshop` | Taller de herramientas — Antigüedad | wood:190, stone:95, ore:28 | 455 | [3, 2] | facilityBoostBp=300 |
| `antiquity_research` | Centro de saber — Antigüedad | wood:152, stone:95, ore:38 | 437 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300 |
| `antiquity_storage` | Almacén regional — Antigüedad | wood:171, stone:123, ore:19 | 315 | [3, 3] | capacityAddEachResource=3250 |
| `antiquity_infrastructure` | Vía logística — Antigüedad | wood:57, stone:66, ore:9 | 157 | [1, 2] | logisticCapacity=12 |
| `antiquity_civic` | Ágora comunitaria — Antigüedad | wood:247, stone:152, ore:47 | 560 | [3, 3] | civicCapacity=1 |
| `antiquity_defense` | Puesto defensivo — Antigüedad | wood:190, stone:180, ore:66 | 490 | [2, 2] | defensePoints=34 |

## Era 7: Edad Media

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `medieval_housing` | Habitáculos — Edad Media | wood:104, stone:20 | 323 | [2, 2] | npcCapacity=8 |
| `medieval_food_production` | Centro alimentario — Edad Media | wood:145, stone:31 | 361 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `medieval_forestry` | Estación de biomasa — Edad Media | wood:135, stone:31 | 323 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `medieval_extraction` | Cantera y mina — Edad Media | wood:135, stone:52, ore:10 | 418 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `medieval_workshop` | Taller de herramientas — Edad Media | wood:208, stone:104, ore:31 | 494 | [3, 2] | facilityBoostBp=300 |
| `medieval_research` | Centro de saber — Edad Media | wood:166, stone:104, ore:41 | 475 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300 |
| `medieval_storage` | Almacén regional — Edad Media | wood:187, stone:135, ore:20 | 342 | [3, 3] | capacityAddEachResource=3600 |
| `medieval_infrastructure` | Vía logística — Edad Media | wood:62, stone:72, ore:10 | 171 | [1, 2] | logisticCapacity=12 |
| `medieval_civic` | Ágora comunitaria — Edad Media | wood:270, stone:166, ore:52 | 608 | [3, 3] | civicCapacity=1 |
| `medieval_defense` | Puesto defensivo — Edad Media | wood:208, stone:197, ore:72 | 532 | [2, 2] | defensePoints=38 |

## Era 8: Renacimiento

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `renaissance_housing` | Habitáculos — Renacimiento | wood:113, stone:22 | 348 | [2, 2] | npcCapacity=8 |
| `renaissance_food_production` | Centro alimentario — Renacimiento | wood:158, stone:33 | 389 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `renaissance_forestry` | Estación de biomasa — Renacimiento | wood:146, stone:33 | 348 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `renaissance_extraction` | Cantera y mina — Renacimiento | wood:146, stone:56, ore:11 | 451 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `renaissance_workshop` | Taller de herramientas — Renacimiento | wood:226, stone:113, ore:33 | 533 | [3, 2] | facilityBoostBp=300 |
| `renaissance_research` | Centro de saber — Renacimiento | wood:180, stone:113, ore:45 | 512 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300 |
| `renaissance_storage` | Almacén regional — Renacimiento | wood:203, stone:146, ore:22 | 369 | [3, 3] | capacityAddEachResource=3950 |
| `renaissance_infrastructure` | Vía logística — Renacimiento | wood:67, stone:79, ore:11 | 184 | [1, 2] | logisticCapacity=12 |
| `renaissance_civic` | Ágora comunitaria — Renacimiento | wood:293, stone:180, ore:56 | 656 | [3, 3] | civicCapacity=1 |
| `renaissance_defense` | Puesto defensivo — Renacimiento | wood:226, stone:214, ore:79 | 574 | [2, 2] | defensePoints=42 |

## Era 9: Era Industrial

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `industrial_housing` | Habitáculos — Era Industrial | wood:122, stone:24 | 374 | [2, 2] | npcCapacity=8 |
| `industrial_food_production` | Centro alimentario — Era Industrial | wood:170, stone:36 | 418 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `industrial_forestry` | Estación de biomasa — Era Industrial | wood:158, stone:36 | 374 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `industrial_extraction` | Cantera y mina — Era Industrial | wood:158, stone:61, ore:12 | 484 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `industrial_workshop` | Taller de herramientas — Era Industrial | wood:244, stone:122, ore:36 | 572 | [3, 2] | facilityBoostBp=300 |
| `industrial_research` | Centro de saber — Era Industrial | wood:195, stone:122, ore:48 | 550 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300 |
| `industrial_storage` | Almacén regional — Era Industrial | wood:219, stone:158, ore:24 | 396 | [3, 3] | capacityAddEachResource=4300 |
| `industrial_infrastructure` | Vía logística — Era Industrial | wood:73, stone:85, ore:12 | 198 | [1, 2] | logisticCapacity=12 |
| `industrial_civic` | Ágora comunitaria — Era Industrial | wood:317, stone:195, ore:61 | 704 | [3, 3] | civicCapacity=1 |
| `industrial_defense` | Puesto defensivo — Era Industrial | wood:244, stone:231, ore:85 | 616 | [2, 2] | defensePoints=46 |

## Era 10: Era Moderna

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `modern_housing` | Habitáculos — Era Moderna | wood:131, stone:26 | 399 | [2, 2] | npcCapacity=8 |
| `modern_food_production` | Centro alimentario — Era Moderna | wood:183, stone:39 | 446 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `modern_forestry` | Estación de biomasa — Era Moderna | wood:170, stone:39 | 399 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `modern_extraction` | Cantera y mina — Era Moderna | wood:170, stone:65, ore:13 | 517 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `modern_workshop` | Taller de herramientas — Era Moderna | wood:262, stone:131, ore:39 | 611 | [3, 2] | facilityBoostBp=300 |
| `modern_research` | Centro de saber — Era Moderna | wood:209, stone:131, ore:52 | 587 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300 |
| `modern_storage` | Almacén regional — Era Moderna | wood:235, stone:170, ore:26 | 423 | [3, 3] | capacityAddEachResource=4650 |
| `modern_infrastructure` | Vía logística — Era Moderna | wood:78, stone:91, ore:13 | 211 | [1, 2] | logisticCapacity=12 |
| `modern_civic` | Ágora comunitaria — Era Moderna | wood:340, stone:209, ore:65 | 752 | [3, 3] | civicCapacity=1 |
| `modern_defense` | Puesto defensivo — Era Moderna | wood:262, stone:248, ore:91 | 658 | [2, 2] | defensePoints=50 |

## Era 11: Era Digital

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `digital_housing` | Habitáculos — Era Digital | wood:140, stone:28 | 425 | [2, 2] | npcCapacity=8 |
| `digital_food_production` | Centro alimentario — Era Digital | wood:196, stone:42 | 475 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `digital_forestry` | Estación de biomasa — Era Digital | wood:182, stone:42 | 425 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `digital_extraction` | Cantera y mina — Era Digital | wood:182, stone:70, ore:14 | 550 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `digital_workshop` | Taller de herramientas — Era Digital | wood:280, stone:140, ore:42 | 650 | [3, 2] | facilityBoostBp=300 |
| `digital_research` | Centro de saber — Era Digital | wood:224, stone:140, ore:56 | 625 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300 |
| `digital_storage` | Almacén regional — Era Digital | wood:252, stone:182, ore:28 | 450 | [3, 3] | capacityAddEachResource=5000 |
| `digital_infrastructure` | Vía logística — Era Digital | wood:84, stone:98, ore:14 | 225 | [1, 2] | logisticCapacity=12 |
| `digital_civic` | Ágora comunitaria — Era Digital | wood:364, stone:224, ore:70 | 800 | [3, 3] | civicCapacity=1 |
| `digital_defense` | Puesto defensivo — Era Digital | wood:280, stone:266, ore:98 | 700 | [2, 2] | defensePoints=54 |

## Era 12: Era Espacial

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `space_housing` | Habitáculos — Era Espacial | wood:149, stone:29 | 450 | [2, 2] | npcCapacity=8 |
| `space_food_production` | Centro alimentario — Era Espacial | wood:208, stone:44 | 503 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `space_forestry` | Estación de biomasa — Era Espacial | wood:193, stone:44 | 450 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `space_extraction` | Cantera y mina — Era Espacial | wood:193, stone:74, ore:14 | 583 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `space_workshop` | Taller de herramientas — Era Espacial | wood:298, stone:149, ore:44 | 689 | [3, 2] | facilityBoostBp=300 |
| `space_research` | Centro de saber — Era Espacial | wood:238, stone:149, ore:59 | 662 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300 |
| `space_storage` | Almacén regional — Era Espacial | wood:268, stone:193, ore:29 | 477 | [3, 3] | capacityAddEachResource=5350 |
| `space_infrastructure` | Vía logística — Era Espacial | wood:89, stone:104, ore:14 | 238 | [1, 2] | logisticCapacity=12 |
| `space_civic` | Ágora comunitaria — Era Espacial | wood:387, stone:238, ore:74 | 848 | [3, 3] | civicCapacity=1 |
| `space_defense` | Puesto defensivo — Era Espacial | wood:298, stone:283, ore:104 | 742 | [2, 2] | defensePoints=58 |

## Era 13: Era Interestelar

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `interstellar_housing` | Habitáculos — Era Interestelar | wood:158, stone:31 | 476 | [2, 2] | npcCapacity=8 |
| `interstellar_food_production` | Centro alimentario — Era Interestelar | wood:221, stone:47 | 532 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `interstellar_forestry` | Estación de biomasa — Era Interestelar | wood:205, stone:47 | 476 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `interstellar_extraction` | Cantera y mina — Era Interestelar | wood:205, stone:79, ore:15 | 616 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `interstellar_workshop` | Taller de herramientas — Era Interestelar | wood:316, stone:158, ore:47 | 728 | [3, 2] | facilityBoostBp=300 |
| `interstellar_research` | Centro de saber — Era Interestelar | wood:252, stone:158, ore:63 | 700 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300 |
| `interstellar_storage` | Almacén regional — Era Interestelar | wood:284, stone:205, ore:31 | 504 | [3, 3] | capacityAddEachResource=5700 |
| `interstellar_infrastructure` | Vía logística — Era Interestelar | wood:94, stone:110, ore:15 | 252 | [1, 2] | logisticCapacity=12 |
| `interstellar_civic` | Ágora comunitaria — Era Interestelar | wood:410, stone:252, ore:79 | 896 | [3, 3] | civicCapacity=1 |
| `interstellar_defense` | Puesto defensivo — Era Interestelar | wood:316, stone:300, ore:110 | 784 | [2, 2] | defensePoints=62 |

## Reglas de lectura

El coste se descuenta una vez por construcción aprobada/planificada, antes de ejecutar la obra, con garantías transaccionales; el trabajo es una magnitud de progreso de obra y no segundos de pantalla. Las huellas son ocupación en tiles, no dimensiones de una ilustración. Las cifras proceden del catálogo y no demuestran que los valores estén equilibrados en un directo real.



---


<!-- Documento fuente: docs/35_CATALOGO_LEGIBLE_PROYECTOS_Y_MARAVILLAS.md -->


# 35 — Proyectos estratégicos y maravillas: catálogo legible

**Estado:** derivación documental de `data/strategic_projects.v2.json`; evita que un lector dependa del JSON para entender todos los proyectos. Los costes `gold` son **virtuales y proceden únicamente de aportaciones aprobadas**, por lo que no son necesarios para ganar.

## Proyectos estratégicos (39)

| Era | Proyecto | Identificador | Costes | Trabajo | Efecto |
|---|---|---|---|---:|---|
| 1 | Memorial de los Fundadores — Paleolítico | `paleolithic_memorial` | wood:120, stone:85, knowledge:20, gold:30 | 590 | prestigeOnCompletion=40; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=memorial |
| 1 | Plaza del Gran Espectáculo — Paleolítico | `paleolithic_spectacle` | wood:120, stone:85, knowledge:20, gold:30 | 590 | prestigeOnCompletion=40; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=spectacle |
| 1 | Archivo de la Memoria — Paleolítico | `paleolithic_archive` | wood:120, stone:85, knowledge:20, gold:30 | 590 | prestigeOnCompletion=40; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=archive |
| 2 | Memorial de los Fundadores — Neolítico | `neolithic_memorial` | wood:150, stone:110, knowledge:40, gold:40 | 730 | prestigeOnCompletion=50; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=memorial |
| 2 | Plaza del Gran Espectáculo — Neolítico | `neolithic_spectacle` | wood:150, stone:110, knowledge:40, gold:40 | 730 | prestigeOnCompletion=50; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=spectacle |
| 2 | Archivo de la Memoria — Neolítico | `neolithic_archive` | wood:150, stone:110, knowledge:40, gold:40 | 730 | prestigeOnCompletion=50; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=archive |
| 3 | Memorial de los Fundadores — Edad del Cobre | `copper_memorial` | wood:180, stone:135, ore:15, knowledge:60, gold:50 | 870 | prestigeOnCompletion=60; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=memorial |
| 3 | Plaza del Gran Espectáculo — Edad del Cobre | `copper_spectacle` | wood:180, stone:135, ore:15, knowledge:60, gold:50 | 870 | prestigeOnCompletion=60; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=spectacle |
| 3 | Archivo de la Memoria — Edad del Cobre | `copper_archive` | wood:180, stone:135, ore:15, knowledge:60, gold:50 | 870 | prestigeOnCompletion=60; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=archive |
| 4 | Memorial de los Fundadores — Edad del Bronce | `bronze_memorial` | wood:210, stone:160, ore:30, knowledge:80, gold:60 | 1010 | prestigeOnCompletion=70; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=memorial |
| 4 | Plaza del Gran Espectáculo — Edad del Bronce | `bronze_spectacle` | wood:210, stone:160, ore:30, knowledge:80, gold:60 | 1010 | prestigeOnCompletion=70; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=spectacle |
| 4 | Archivo de la Memoria — Edad del Bronce | `bronze_archive` | wood:210, stone:160, ore:30, knowledge:80, gold:60 | 1010 | prestigeOnCompletion=70; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=archive |
| 5 | Memorial de los Fundadores — Edad del Hierro | `iron_memorial` | wood:240, stone:185, ore:45, knowledge:100, gold:70 | 1150 | prestigeOnCompletion=80; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=memorial |
| 5 | Plaza del Gran Espectáculo — Edad del Hierro | `iron_spectacle` | wood:240, stone:185, ore:45, knowledge:100, gold:70 | 1150 | prestigeOnCompletion=80; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=spectacle |
| 5 | Archivo de la Memoria — Edad del Hierro | `iron_archive` | wood:240, stone:185, ore:45, knowledge:100, gold:70 | 1150 | prestigeOnCompletion=80; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=archive |
| 6 | Memorial de los Fundadores — Antigüedad | `antiquity_memorial` | wood:270, stone:210, ore:60, knowledge:120, gold:80 | 1290 | prestigeOnCompletion=90; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=memorial |
| 6 | Plaza del Gran Espectáculo — Antigüedad | `antiquity_spectacle` | wood:270, stone:210, ore:60, knowledge:120, gold:80 | 1290 | prestigeOnCompletion=90; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=spectacle |
| 6 | Archivo de la Memoria — Antigüedad | `antiquity_archive` | wood:270, stone:210, ore:60, knowledge:120, gold:80 | 1290 | prestigeOnCompletion=90; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=archive |
| 7 | Memorial de los Fundadores — Edad Media | `medieval_memorial` | wood:300, stone:235, ore:75, knowledge:140, gold:90 | 1430 | prestigeOnCompletion=100; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=memorial |
| 7 | Plaza del Gran Espectáculo — Edad Media | `medieval_spectacle` | wood:300, stone:235, ore:75, knowledge:140, gold:90 | 1430 | prestigeOnCompletion=100; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=spectacle |
| 7 | Archivo de la Memoria — Edad Media | `medieval_archive` | wood:300, stone:235, ore:75, knowledge:140, gold:90 | 1430 | prestigeOnCompletion=100; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=archive |
| 8 | Memorial de los Fundadores — Renacimiento | `renaissance_memorial` | wood:330, stone:260, ore:90, knowledge:160, gold:100 | 1570 | prestigeOnCompletion=110; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=memorial |
| 8 | Plaza del Gran Espectáculo — Renacimiento | `renaissance_spectacle` | wood:330, stone:260, ore:90, knowledge:160, gold:100 | 1570 | prestigeOnCompletion=110; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=spectacle |
| 8 | Archivo de la Memoria — Renacimiento | `renaissance_archive` | wood:330, stone:260, ore:90, knowledge:160, gold:100 | 1570 | prestigeOnCompletion=110; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=archive |
| 9 | Memorial de los Fundadores — Era Industrial | `industrial_memorial` | wood:360, stone:285, ore:105, knowledge:180, gold:110 | 1710 | prestigeOnCompletion=120; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=memorial |
| 9 | Plaza del Gran Espectáculo — Era Industrial | `industrial_spectacle` | wood:360, stone:285, ore:105, knowledge:180, gold:110 | 1710 | prestigeOnCompletion=120; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=spectacle |
| 9 | Archivo de la Memoria — Era Industrial | `industrial_archive` | wood:360, stone:285, ore:105, knowledge:180, gold:110 | 1710 | prestigeOnCompletion=120; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=archive |
| 10 | Memorial de los Fundadores — Era Moderna | `modern_memorial` | wood:390, stone:310, ore:120, knowledge:200, gold:120 | 1850 | prestigeOnCompletion=130; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=memorial |
| 10 | Plaza del Gran Espectáculo — Era Moderna | `modern_spectacle` | wood:390, stone:310, ore:120, knowledge:200, gold:120 | 1850 | prestigeOnCompletion=130; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=spectacle |
| 10 | Archivo de la Memoria — Era Moderna | `modern_archive` | wood:390, stone:310, ore:120, knowledge:200, gold:120 | 1850 | prestigeOnCompletion=130; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=archive |
| 11 | Memorial de los Fundadores — Era Digital | `digital_memorial` | wood:420, stone:335, ore:135, knowledge:220, gold:130 | 1990 | prestigeOnCompletion=140; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=memorial |
| 11 | Plaza del Gran Espectáculo — Era Digital | `digital_spectacle` | wood:420, stone:335, ore:135, knowledge:220, gold:130 | 1990 | prestigeOnCompletion=140; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=spectacle |
| 11 | Archivo de la Memoria — Era Digital | `digital_archive` | wood:420, stone:335, ore:135, knowledge:220, gold:130 | 1990 | prestigeOnCompletion=140; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=archive |
| 12 | Memorial de los Fundadores — Era Espacial | `space_memorial` | wood:450, stone:360, ore:150, knowledge:240, gold:140 | 2130 | prestigeOnCompletion=150; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=memorial |
| 12 | Plaza del Gran Espectáculo — Era Espacial | `space_spectacle` | wood:450, stone:360, ore:150, knowledge:240, gold:140 | 2130 | prestigeOnCompletion=150; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=spectacle |
| 12 | Archivo de la Memoria — Era Espacial | `space_archive` | wood:450, stone:360, ore:150, knowledge:240, gold:140 | 2130 | prestigeOnCompletion=150; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=archive |
| 13 | Memorial de los Fundadores — Era Interestelar | `interstellar_memorial` | wood:480, stone:385, ore:165, knowledge:260, gold:150 | 2270 | prestigeOnCompletion=160; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=memorial |
| 13 | Plaza del Gran Espectáculo — Era Interestelar | `interstellar_spectacle` | wood:480, stone:385, ore:165, knowledge:260, gold:150 | 2270 | prestigeOnCompletion=160; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=spectacle |
| 13 | Archivo de la Memoria — Era Interestelar | `interstellar_archive` | wood:480, stone:385, ore:165, knowledge:260, gold:150 | 2270 | prestigeOnCompletion=160; visualOnly=True; economicBonusBp=0; historicalPoints=0; cosmeticCue=archive |

## Maravillas (13)

| Era | Maravilla | Identificador | Costes | Trabajo | Efecto |
|---|---|---|---|---:|---|
| 1 | Maravilla del Paleolítico | `wonder_paleolithic` | wood:245, stone:195, knowledge:40, gold:140 | 1500 |  |
| 2 | Maravilla del Neolítico | `wonder_neolithic` | wood:290, stone:240, knowledge:80, gold:180 | 1750 |  |
| 3 | Maravilla del Edad del Cobre | `wonder_copper` | wood:335, stone:285, ore:25, knowledge:120, gold:220 | 2000 |  |
| 4 | Maravilla del Edad del Bronce | `wonder_bronze` | wood:380, stone:330, ore:50, knowledge:160, gold:260 | 2250 |  |
| 5 | Maravilla del Edad del Hierro | `wonder_iron` | wood:425, stone:375, ore:75, knowledge:200, gold:300 | 2500 |  |
| 6 | Maravilla del Antigüedad | `wonder_antiquity` | wood:470, stone:420, ore:100, knowledge:240, gold:340 | 2750 |  |
| 7 | Maravilla del Edad Media | `wonder_medieval` | wood:515, stone:465, ore:125, knowledge:280, gold:380 | 3000 |  |
| 8 | Maravilla del Renacimiento | `wonder_renaissance` | wood:560, stone:510, ore:150, knowledge:320, gold:420 | 3250 |  |
| 9 | Maravilla del Era Industrial | `wonder_industrial` | wood:605, stone:555, ore:175, knowledge:360, gold:460 | 3500 |  |
| 10 | Maravilla del Era Moderna | `wonder_modern` | wood:650, stone:600, ore:200, knowledge:400, gold:500 | 3750 |  |
| 11 | Maravilla del Era Digital | `wonder_digital` | wood:695, stone:645, ore:225, knowledge:440, gold:540 | 4000 |  |
| 12 | Maravilla del Era Espacial | `wonder_space` | wood:740, stone:690, ore:250, knowledge:480, gold:580 | 4250 |  |
| 13 | Maravilla del Era Interestelar | `wonder_interstellar` | wood:785, stone:735, ore:275, knowledge:520, gold:620 | 4500 |  |

## Decisiones de uso

La selección de Consejo siempre se hace entre tres proyectos distintos, desbloqueados, no construidos y financiables individualmente. Si no existen tres, no se convoca, y la ruta de progresión histórica gratuita continúa. Una maravilla exclusiva usa adjudicación global atómica; la representación visual del premio no añade bonificación histórica o productiva. Al cambiar de era no se crean de forma ficticia proyectos de la anterior para completar el trío.



---


<!-- Documento fuente: docs/36_CATALOGO_LEGIBLE_TECNOLOGIAS_E_HITOS.md -->


# 36 — Tecnologías, hitos y misión de la barra histórica

**Estado:** índice de lectura derivado de `technologies.v2.json`, `milestones.v2.json`, `eras.v2.json` y `missions.v2.json`. La barra requiere cinco hitos únicos de 20 puntos: alimentación, materiales, conocimiento, edificio representativo y misión colectiva. Las misiones diarias y semanales repetibles no otorgan puntos históricos.


## Era 1: Paleolítico

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_paleolithic` | Investigación de Paleolítico | 290 | — | paleolithic_workshop, paleolithic_research |
| `tech_paleolithic_economy` | Logística de Paleolítico | 170 | tech_paleolithic | — |
| `tech_paleolithic_defense` | Protección de Paleolítico | 170 | tech_paleolithic | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `paleolithic_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=6400 | 20 |
| `paleolithic_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 4750, 'stone': 3420} | 20 |
| `paleolithic_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=2650; requiresTechnologyId=tech_paleolithic | 20 |
| `paleolithic_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=paleolithic_civic | 20 |
| `paleolithic_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 2: Neolítico

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_neolithic` | Investigación de Neolítico | 380 | tech_paleolithic | neolithic_workshop, neolithic_research |
| `tech_neolithic_economy` | Logística de Neolítico | 220 | tech_neolithic | — |
| `tech_neolithic_defense` | Protección de Neolítico | 220 | tech_neolithic | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `neolithic_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=7000 | 20 |
| `neolithic_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 5200, 'stone': 3740} | 20 |
| `neolithic_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=2900; requiresTechnologyId=tech_neolithic | 20 |
| `neolithic_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=neolithic_civic | 20 |
| `neolithic_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 3: Edad del Cobre

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_copper` | Investigación de Edad del Cobre | 470 | tech_neolithic | copper_workshop, copper_research |
| `tech_copper_economy` | Logística de Edad del Cobre | 270 | tech_copper | — |
| `tech_copper_defense` | Protección de Edad del Cobre | 270 | tech_copper | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `copper_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=7600 | 20 |
| `copper_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 5650, 'stone': 4060} | 20 |
| `copper_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=3150; requiresTechnologyId=tech_copper | 20 |
| `copper_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=copper_civic | 20 |
| `copper_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 4: Edad del Bronce

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_bronze` | Investigación de Edad del Bronce | 560 | tech_copper | bronze_workshop, bronze_research |
| `tech_bronze_economy` | Logística de Edad del Bronce | 320 | tech_bronze | — |
| `tech_bronze_defense` | Protección de Edad del Bronce | 320 | tech_bronze | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `bronze_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=8200 | 20 |
| `bronze_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 6100, 'stone': 4380} | 20 |
| `bronze_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=3400; requiresTechnologyId=tech_bronze | 20 |
| `bronze_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=bronze_civic | 20 |
| `bronze_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 5: Edad del Hierro

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_iron` | Investigación de Edad del Hierro | 650 | tech_bronze | iron_workshop, iron_research |
| `tech_iron_economy` | Logística de Edad del Hierro | 370 | tech_iron | — |
| `tech_iron_defense` | Protección de Edad del Hierro | 370 | tech_iron | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `iron_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=8800 | 20 |
| `iron_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 6550, 'stone': 4700} | 20 |
| `iron_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=3650; requiresTechnologyId=tech_iron | 20 |
| `iron_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=iron_civic | 20 |
| `iron_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 6: Antigüedad

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_antiquity` | Investigación de Antigüedad | 740 | tech_iron | antiquity_workshop, antiquity_research |
| `tech_antiquity_economy` | Logística de Antigüedad | 420 | tech_antiquity | — |
| `tech_antiquity_defense` | Protección de Antigüedad | 420 | tech_antiquity | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `antiquity_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=9400 | 20 |
| `antiquity_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 7000, 'stone': 5020} | 20 |
| `antiquity_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=3900; requiresTechnologyId=tech_antiquity | 20 |
| `antiquity_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=antiquity_civic | 20 |
| `antiquity_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 7: Edad Media

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_medieval` | Investigación de Edad Media | 830 | tech_antiquity | medieval_workshop, medieval_research |
| `tech_medieval_economy` | Logística de Edad Media | 470 | tech_medieval | — |
| `tech_medieval_defense` | Protección de Edad Media | 470 | tech_medieval | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `medieval_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=10000 | 20 |
| `medieval_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 7450, 'stone': 5340} | 20 |
| `medieval_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=4150; requiresTechnologyId=tech_medieval | 20 |
| `medieval_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=medieval_civic | 20 |
| `medieval_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 8: Renacimiento

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_renaissance` | Investigación de Renacimiento | 920 | tech_medieval | renaissance_workshop, renaissance_research |
| `tech_renaissance_economy` | Logística de Renacimiento | 520 | tech_renaissance | — |
| `tech_renaissance_defense` | Protección de Renacimiento | 520 | tech_renaissance | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `renaissance_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=10600 | 20 |
| `renaissance_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 7900, 'stone': 5660} | 20 |
| `renaissance_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=4400; requiresTechnologyId=tech_renaissance | 20 |
| `renaissance_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=renaissance_civic | 20 |
| `renaissance_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 9: Era Industrial

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_industrial` | Investigación de Era Industrial | 1010 | tech_renaissance | industrial_workshop, industrial_research |
| `tech_industrial_economy` | Logística de Era Industrial | 570 | tech_industrial | — |
| `tech_industrial_defense` | Protección de Era Industrial | 570 | tech_industrial | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `industrial_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=11200 | 20 |
| `industrial_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 8350, 'stone': 5980} | 20 |
| `industrial_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=4650; requiresTechnologyId=tech_industrial | 20 |
| `industrial_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=industrial_civic | 20 |
| `industrial_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 10: Era Moderna

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_modern` | Investigación de Era Moderna | 1100 | tech_industrial | modern_workshop, modern_research |
| `tech_modern_economy` | Logística de Era Moderna | 620 | tech_modern | — |
| `tech_modern_defense` | Protección de Era Moderna | 620 | tech_modern | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `modern_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=11800 | 20 |
| `modern_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 8800, 'stone': 6300} | 20 |
| `modern_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=4900; requiresTechnologyId=tech_modern | 20 |
| `modern_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=modern_civic | 20 |
| `modern_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 11: Era Digital

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_digital` | Investigación de Era Digital | 1190 | tech_modern | digital_workshop, digital_research |
| `tech_digital_economy` | Logística de Era Digital | 670 | tech_digital | — |
| `tech_digital_defense` | Protección de Era Digital | 670 | tech_digital | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `digital_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=12400 | 20 |
| `digital_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 9250, 'stone': 6620} | 20 |
| `digital_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=5150; requiresTechnologyId=tech_digital | 20 |
| `digital_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=digital_civic | 20 |
| `digital_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 12: Era Espacial

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_space` | Investigación de Era Espacial | 1280 | tech_digital | space_workshop, space_research |
| `tech_space_economy` | Logística de Era Espacial | 720 | tech_space | — |
| `tech_space_defense` | Protección de Era Espacial | 720 | tech_space | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `space_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=13000 | 20 |
| `space_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 9700, 'stone': 6940} | 20 |
| `space_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=5400; requiresTechnologyId=tech_space | 20 |
| `space_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=space_civic | 20 |
| `space_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 13: Era Interestelar

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_interstellar` | Investigación de Era Interestelar | 1370 | tech_space | interstellar_workshop, interstellar_research |
| `tech_interstellar_economy` | Logística de Era Interestelar | 770 | tech_interstellar | — |
| `tech_interstellar_defense` | Protección de Era Interestelar | 770 | tech_interstellar | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `interstellar_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=13600 | 20 |
| `interstellar_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 10150, 'stone': 7260} | 20 |
| `interstellar_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=5650; requiresTechnologyId=tech_interstellar | 20 |
| `interstellar_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=interstellar_civic | 20 |
| `interstellar_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Condiciones de transición

El motor reconoce cada hito una sola vez por nación, era y clave canónica. Alcanzar 100 puntos fuera de emisión marca la era como `EraReadyPending`; no inicia ceremonia ni avanza automáticamente. La primera transición confirmada a Interestelar termina la carrera. Los catálogos deben permanecer inmutables durante la temporada: ningún ajuste de objetivo puede aplicarse retroactivamente sin migración explícita.



---


<!-- Documento fuente: docs/37_CATALOGO_LEGIBLE_PROFESIONES_HABILIDADES_GOBIERNOS.md -->


# 37 — Profesiones, habilidades y gobiernos: catálogo legible

**Estado:** derivación de las definiciones canónicas `data/professions.v2.json`, `data/skills.v2.json`, `data/governments.v2.json` y `data/eras.v2.json`. La profesión se elige una única vez por temporada; el oficio cambia su denominación estética según la era, sin cambiar de familia funcional.

## Etiquetas de oficio por época

| Era | Alimentación | Biomasa | Minería | Construcción | Investigación |
|---|---|---|---|---|---|
| Paleolítico | Cazador | Recolector | Tallador | Constructor tribal | Explorador |
| Neolítico | Agricultor | Leñador | Cantero | Albañil | Sabio |
| Edad del Cobre | Agricultor | Silvicultor | Minero | Artesano | Estudioso |
| Edad del Bronce | Granjero | Leñador | Fundidor | Maestro de obras | Escriba |
| Edad del Hierro | Campesino | Forestal | Herrero | Constructor | Investigador |
| Antigüedad | Labrador | Carpintero forestal | Minero | Arquitecto | Filósofo |
| Edad Media | Agricultor | Leñador | Minero | Maestro de gremio | Erudito |
| Renacimiento | Agrónomo | Guardabosques | Metalurgista | Ingeniero | Inventor |
| Era Industrial | Operario agrícola | Maderero | Minero industrial | Ingeniero industrial | Científico |
| Era Moderna | Técnico agrícola | Técnico forestal | Operario de extracción | Técnico de obras | Investigador |
| Era Digital | Tecnólogo alimentario | Especialista en biomasa | Operador extractivo | Ingeniero de automatización | Analista |
| Era Espacial | Técnico de suministros | Cultivador espacial | Extractor planetario | Ingeniero orbital | Astrocientífico |
| Era Interestelar | Sintetizador | Ingeniero de biomasa | Extractor estelar | Arquitecto interestelar | Investigador cuántico |

## Habilidades (30)

| Profesión | Nivel requerido | Identificador | Nombre | Efecto exacto |
|---|---:|---|---|---|
| food | 3 | `expert_gathering` | Expert Gathering | target=food; additiveBp=400; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| food | 3 | `food_hauling` | Food Hauling | target=food; additiveBp=250; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| food | 7 | `efficient_production` | Efficient Production | target=food; additiveBp=500; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| food | 7 | `rationing` | Rationing | target=food; additiveBp=350; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| food | 12 | `master_foodcraft` | Master Foodcraft | target=food; additiveBp=600; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| food | 12 | `preservation` | Preservation | target=food; additiveBp=300; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| wood | 3 | `precise_cut` | Precise Cut | target=wood; additiveBp=400; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| wood | 3 | `forest_walker` | Forest Walker | target=wood; additiveBp=250; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| wood | 7 | `optimized_tools` | Optimized Tools | target=wood; additiveBp=500; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| wood | 7 | `full_utilization` | Full Utilization | target=wood; additiveBp=450; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| wood | 12 | `master_forester` | Master Forester | target=wood; additiveBp=600; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| wood | 12 | `reuse` | Reuse | target=wood; additiveBp=350; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| mine | 3 | `expert_stonecutter` | Expert Stonecutter | target=stone; additiveBp=400; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| mine | 3 | `prospector` | Prospector | target=ore; additiveBp=450; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| mine | 7 | `efficient_excavation` | Efficient Excavation | target=mine; additiveBp=500; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| mine | 7 | `heavy_load` | Heavy Load | target=mine; additiveBp=250; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| mine | 12 | `master_stonecutter` | Master Stonecutter | target=stone; additiveBp=600; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| mine | 12 | `master_miner` | Master Miner | target=ore; additiveBp=600; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| build | 3 | `fast_hands` | Fast Hands | target=buildWork; additiveBp=400; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| build | 3 | `site_organizer` | Site Organizer | target=buildWork; additiveBp=300; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| build | 7 | `expert_builder` | Expert Builder | target=buildWork; additiveBp=450; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| build | 7 | `restorer` | Restorer | target=buildWork; additiveBp=300; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| build | 12 | `master_architect` | Master Architect | target=buildWork; additiveBp=600; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| build | 12 | `civil_engineer` | Civil Engineer | target=buildWork; additiveBp=450; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| research | 3 | `curiosity` | Curiosity | target=knowledge; additiveBp=400; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| research | 3 | `methodical_study` | Methodical Study | target=knowledge; additiveBp=350; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| research | 7 | `applied_research` | Applied Research | target=knowledge; additiveBp=500; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| research | 7 | `documentation` | Documentation | target=xp; additiveBp=400; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| research | 12 | `grand_researcher` | Grand Researcher | target=knowledge; additiveBp=600; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| research | 12 | `innovator` | Innovator | target=knowledge; additiveBp=500; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |

## Candidaturas de gobierno (9)

| Nación | Arquetipo | Personaje | Bonificación | Campo de aplicación |
|---|---|---|---:|---|
| micelios | economy | Morga | 300 | food_wood_stone_ore |
| micelios | military | Bruk | 500 | automated_tournament_defense |
| micelios | science | Espora | 300 | knowledge |
| runicos | economy | Dorrik | 300 | food_wood_stone_ore |
| runicos | military | Kraag | 500 | automated_tournament_defense |
| runicos | science | Zyn | 300 | knowledge |
| ferrinos | economy | Nera | 300 | food_wood_stone_ore |
| ferrinos | military | Rokka | 500 | automated_tournament_defense |
| ferrinos | science | Neri | 300 | knowledge |

## Límites

Las habilidades aplican al ciudadano que las obtuvo, salvo indicación contraria explícita en el catálogo; el mismo bono no puede multiplicarse ilimitadamente por número de jugadores. Los gobernantes no sustituyen decisiones del Consejo ni tienen poder para conceder oro, alterar el ganador o saltar hitos. Los valores reflejan el catálogo de diseño, pendientes de calibración tras un motor funcional.



---


<!-- Documento fuente: docs/38_PRUEBAS_ACEPTACION_EN_LENGUAJE_NATURAL.md -->


# 38 — Casos de aceptación funcional sin código

**Propósito:** convertir reglas en ejemplos observables para el día que se implemente el motor. No hay scripts, frameworks ni código fuente. Los escenarios usan valores establecidos en v2.0; su ejecución futura será un trabajo diferente.

## Ciudadanía y actividad

**Caso C-01:** una cuenta nueva envía `!join` dos veces debido a reintento del proveedor. Resultado esperado: un ciudadano, una identidad y ningún recurso extraordinario. **C-02:** el ciudadano elige `food`; cuando intenta `mine` en la misma temporada, el sistema conserva `food` y explica la restricción. **C-03:** una acción válida renueva actividad por dos horas reales tras cooldown; el chat casual no prolonga actividad.

## Economía y progreso

**E-01:** una nación tiene 24 NPC iniciales y ningún humano, ninguna aportación y ningún oro. La economía produce y consume según tablas; existe una ruta de avance gratuita sin desbloqueos de pago. **E-02:** cuando se llena madera, la producción no produce inventario por encima de capacidad; los restos y contadores de redondeo se conservan según regla. **E-03:** durante tiempo fuera de emisión la economía utiliza el multiplicador reducido; una votación abierta no consume minutos LIVE. **E-04:** un hito ya cobrado no concede de nuevo 20 puntos al cumplir objetivo repetido.

## Eras y gobierno

**H-01:** cinco hitos distintos de 20 puntos alcanzan 100; la nación sin LIVE confirmado queda preparada pero no pasa de era. **H-02:** al confirmar LIVE la nación avanza exactamente una vez; cambio de nombre de oficio no reasigna la profesión. **G-01:** elección de tres candidatos dura una hora de emisión; el empate activa la segunda vuelta durante tres minutos LIVE. **G-02:** un gobernador militar aplica solo el bono definido, sin capacidad de ordenar ataques automáticos.

## Consejo y oro

**V-01:** el Consejo tiene tres opciones elegibles, con recursos disponibles para cada una por separado, pero no para la suma de las tres. Se reserva el vector máximo previsto; al cierre se cobra solo el proyecto ganador. **V-02:** dos cierres concurrentes no pueden cobrar el mismo voto/obra ni dejar inventarios negativos. **O-01:** un proveedor reintenta un evento monetario idéntico: una sola acreditación. **O-02:** la aportación es revocada tras gastar oro; aparece deuda compensatoria sin saldo negativo en el wallet.

## Torneo

**T-01:** los tres equipos eligen rock, paper, scissors respectivamente; cada equipo gana y pierde una pareja, total dos puntos: no existe un ganador ficticio de esa ronda. **T-02:** una nación no recibe votos y juega PASS. **T-03:** tras dos rondas extra continúa el empate primero: se anuncian ganadores compartidos sin penalización. **T-04:** la penalización territorial consume exactamente 30 minutos de LIVE y se pausa durante desconexión.

## Integraciones y presentación

**I-01:** tres canales del mismo proveedor asignados a tres naciones no mezclan mensajes. **I-02:** retirar una capacidad de monetización no desactiva chat permitido. **I-03:** reconectar OBS no modifica inventarios. **I-04:** ocultar un avatar por LOD no desactiva la producción de su ciudadano. **I-05:** la escena vertical y la horizontal muestran idéntico ganador y era.

## Integridad y final

**F-01:** dos naciones alcanzan Interestelar en eventos casi simultáneos; la adjudicación se resuelve por secuencia de commit global, persistida. **F-02:** una vez completada la temporada no se aceptan nuevas operaciones competitivas ni se arrastran recursos. **F-03:** restaurar un snapshot y reproducir entradas ordenadas produce el mismo checksum del estado lógico con el mismo ruleset y versión de motor.

## Criterio formal

Para declarar completado cada escenario en implementación futura habrá que registrar condiciones iniciales, eventos, sello de tiempo, estado final, asientos de ledger, salida HUD y evidencia observada. **Estar escrito aquí no significa que se haya probado en software.**



---


<!-- Documento fuente: docs/39_REGISTRO_DE_CIERRE_Y_VALIDACIONES_EXTERNAS.md -->


# 39 — Registro de cierre documental y validaciones externas

**Estado:** v2.1 diseño puro. La definición es suficientemente detallada para orientar implementación, pero no se declara producto al 100 % probado. Se conserva distinción entre decisiones cerradas, supuestos de balance y hechos externos.

## Diseñado y expresado documentalmente

Tres naciones independientes de plataforma; 92 respuestas históricas preservadas; cinco profesiones; 13 eras; condición de victoria; rutas gratuitas NPC; recursos, tasas y almacenes; gobiernos, elecciones y prioridades; Consejo estratégico; RPS triangular; contribuciones y oro limitado a prestigio; narrador neutral; estados LIVE y de economía; contratos y esquema relacional propuestos; catálogo numérico de edificios, proyectos, maravillas, tecnologías, hitos, misiones y habilidades; estilo pixel art y escenas OBS; mecanismos de operador y recuperación.

## No resuelto por escribir más páginas

**Integración:** derechos y capacidad efectiva de APIs LIVE para cada cuenta, recuperación real de mensajes, eventos monetarios auditables y condiciones del proveedor. **Arte:** elección y aprobación de sprites, retratos, animación final de K-0 y voces originales. **Implementación:** migraciones SQL ejecutadas, reproducibilidad del motor .NET, rendimiento en OBS, sincronización real y restauración probada. **Comercial:** términos de licencia, pricing y contratación de futuros creadores. **Legal:** cumplimiento y obligaciones específicas de jurisdicción.

## Hipótesis numéricas, no certezas

Las tasas, costes, puntos y límites definidos por `ruleset.v2.json` son un diseño candidato. No han pasado una batería de temporadas reales. Deben calibrarse **antes de abrir una temporada pública** con evidencia cuantitativa y datos de audiencia reales; una vez abierta, los valores permanecen congelados para evitar una carrera injusta.

## Limitaciones del sistema de tres naciones

El esquema de canales admite tres cuentas del mismo proveedor, distintas plataformas y canales secundarios por nación. **No** admite sin revisión una sola cuenta de chat que controle simultáneamente las tres naciones: no está especificado el lenguaje de asignación de nación para cada acción. Si el modelo comercial requiriese «un único LIVE compartido por las tres», eso sería una ampliación de producto con nuevas reglas y no debería inferirse desde la configuración actual.

## Criterios mínimos para fase de desarrollo

- Aprobación de los textos que reformulan decisiones previas (documento 18).
- Identidad visual final de las tres especies y del presentador, suficiente para un prototipo artístico.
- Declaración de proveedor/cuentas que se probarán primero.
- Confirmación legal y técnica de las capacidades de chat previstas.
- Revisión de hipótesis de balance con simulación real antes de prometer calendarios de temporada.

El diseño puede congelarse como baseline de desarrollo sin afirmar que esos hechos externos han ocurrido.



---


<!-- Documento fuente: docs/40_DESCRIPCION_NO_FUNCIONAL_Y_CALIDAD.md -->


# 40 — Requisitos no funcionales y calidad de producto

**Estado:** criterios de diseño y validación futura. No se incluyen Docker, YAML de CI/CD ni scripts. Los números de rendimiento de `docs/22` son objetivos de diseño, no resultados de medición.

## Invariantes de experiencia

Una transición de era debe ser comprensible desde una escena vertical; una desconexión debe señalarse; una elección no puede completarse sin sus segundos LIVE correspondientes; las diferencias de hardware gráfico no afectan economía ni ganador; toda respuesta de comando puede presentarse sin permiso de escribir en chat externo.

## Integridad

Las identidades se basan en IDs de proveedor estables, las aportaciones en eventos verificados y el estado económico en operaciones autoritativas. No existe rollback parcial que descuente materiales y deje de crear una construcción. Un restart de OBS no tiene consecuencias económicas. Los secretos de canal no aparecen en el overlay ni en exportaciones de auditoría pública.

## Escalabilidad

Aumentar de 100 a 10.000 ciudadanos no puede exigir dibujar 10.000 sprites simultáneamente. Se agregan capacidades productivas por cohortes matemáticamente equivalentes. El renderer está desacoplado del simulador y puede reducir partículas y densidad de personajes sin disminuir producción.

## Persistencia

Snapshots, Inbox, Outbox, ledger y reglas versionadas se consideran responsabilidades conceptuales necesarias; SQL es diseño del esquema, no evidencia de migración. Las copias de seguridad deben ser restaurables en entorno de pruebas antes de monetizar. RPO y RTO definitivos deben medirse y documentarse tras desplegar infraestructura real.

## Privacidad y moderación

Minimizar identificadores y datos, usar pseudonimización en exportaciones, diferenciar público/operador, respetar bloqueo de exhibición de nombres ofensivos, atender revocaciones y conservar auditoría necesaria con política de retención específica aprobada. La elección de proveedor y jurisdicción condicionan requisitos legales; no inventar una política RGPD universal en abstracto.

## Compatibilidad

Escenas visuales de 360×640 y 640×360, render objetivo 30 FPS, escalado entero donde el formato final lo permita y modo subtitulado sin audio. Ninguna autorización de TikTok/Twitch/YouTube se presupone por el mero hecho de soportar adaptadores conceptuales.

## Gestión de calidad

Antes de aceptar una temporada pública: ensayo completo de historia, pruebas de estrés, recuperación, seguridad, inclusión de HUD, moderación, corrección de elecciones y monetización verificada si se activa. Los requisitos no funcionales se aprueban con evidencia y no con una declaración de diseño.
