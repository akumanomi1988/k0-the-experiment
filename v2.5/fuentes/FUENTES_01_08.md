# Fuentes íntegras v2.5 — capítulos 1–8

 > **Archivo de preservación de contenido completo (encabezados reindentados).** No es una segunda autoridad: la [especificación maestra](../ESPECIFICACION_MAESTRA_v2.5.md) resuelve reglas sustituidas. Los enlaces relativos del texto interno pertenecen al documento original citado, por lo que debe abrirse ese archivo para navegar sus enlaces.


---

## Fuente 01 — `docs/01_VISION_Y_ALCANCE.md`

**Blob de origen:** `b74c9d3d7b58bbd7f713e1b04a1ace9f2a104afa`.

> **Enmienda normativa v2.3 (multistreamer distribuido):** tres streamers pueden competir desde tres equipos/redes distintos; servidor K0 central y overlays OBS independientes; un canal por nación, mismas reglas sin instalación del motor local. [Especificación vigente](CURRENT_SPEC.md).

## 01 — Producto, alcance y principios no negociables (v2.0)

### Identidad y promesa al espectador
K0: The Experiment (título público de trabajo; antes Project CHAOS) es un juego-espectáculo permanente por temporadas: tres naciones inteligentes no humanas, representadas con pixel art 2D de baja resolución en proyección oblicua 2:1, evolucionan del Paleolítico a la Era Interestelar. Doctor K-0, científico cyborg, sarcástico y neutral, presenta el experimento. La audiencia participa mediante comandos de chat desde uno de los canales asociados. La nación no es la plataforma: los canales son **fuentes intercambiables**. Se admiten tres canales de Twitch, tres cuentas TikTok, YouTube, una mezcla, o modo local; todas las configuraciones dependen del acceso permitido y comprobado al proveedor.

### Decisiones heredadas, no negociables
- Tres naciones independientes: Micelios, Rúnicos y Ferrinos. No existen Corálidos. Misma base matemática, sin bonificaciones por especie/bioma.
- Cinco profesiones permanentes por temporada (`food`, `wood`, `mine`, `build`, `research`) y evolución estética por era.
- `!join` y `!work` para crear ciudadano/elegir oficio. `!active` o `!work` válido renuevan 2 horas de actividad real; el chat normal no.
- NPC mantienen el mundo vivo sin espectadores; la simulación fuera de emisión funciona a velocidad reducida.
- Recursos colectivos, comida sin muerte individual, almacenes limitados, edificios básicos automáticos, proyectos estratégicos votados entre **tres alternativas financiables** durante diez minutos; sus costes se descuentan al aprobar.
- Elecciones de gobiernos NPC: tres arquetipos, un gobernante, una hora de voto, segunda vuelta de tres minutos ante empate. Votación separada de prioridad tecnológica.
- Barra de historia por hitos únicos de puntuación fija; era lista fuera de emisión espera al LIVE. Primera nación en entrar a era final gana la temporada.
- Torneos solo programados: primer minijuego RPS triangular con elección oculta; penaltis territoriales de 30 minutos **activos en directo**; cero transferencia de oro.
- Oro solo desde aportaciones económicas verificadas; jamás por NPC, misiones, chat ni operaciones de explotación. Permanencia solo de historial, estadísticas, logros y prestigio visual entre temporadas.

### Cierre de definición de v2.0 y revisión v2.2 y revisión v2.2
Valores desconocidos de balance y reglas ambiguas pasan a convertirse en **defaults de producto v2.0**. Son decisiones técnicas/de producto tomadas en virtud de la autorización del usuario de este turno, *no respuestas históricas atribuidas al usuario*. Se pueden versionar antes de abrir una temporada; nunca alterarse a mitad de temporada sin migración explícita y auditoría.

No existe en este documento ninguna autorización implícita para extraer datos con APIs no oficiales ni para simular un beneficio monetario. Tampoco confundir especificación de sprites con haberlos creado; `art_spec.v2.json` es especificación, y las integraciones LIVE reales se mantienen bloqueadas hasta pruebas verificables.

### El juego no es pay-to-win
El oro se usa exclusivamente en proyectos opcionales de estética/prestigio, monumentos y homenajes. Todos los umbrales de historia y el motor de investigación son gratuitos. Para evitar la ventaja matemática por riqueza, un proyecto financiado con oro no aporta puntos históricos, capacidad productiva, voto extra, velocidad científica ni fuerza militar. Una maravilla entrega prestigio y reconocimiento visual, no economía. Este ajuste solventa el riesgo de que una donación sea la condición tácita de victoria.

### Criterios de éxito del diseño
Dos implementaciones que compartan `ruleset_hash`, `content_manifest_hash`, `season_seed`, la secuencia canónica de eventos y UTC segmentado deben producir el mismo estado lógico, incluido el ganador. Los viewers y la máquina OBS solo consumen proyecciones. Ningún NPC ni sprite tiene permisos de cambiar el ledger de recursos por vía gráfica.


---

## Fuente 02 — `docs/02_CANALES_CUENTAS_Y_NACIONES.md`

**Blob de origen:** `74792705d5cf0b24476dc94f526331a76485ce81`.

> **Enmienda normativa v2.3 (multistreamer distribuido):** StreamerSeat, ProviderConnection, BroadcastOutput y ProviderLiveSession son entidades distintas; cada streamer autentica y autoriza su propio canal. La señal OBS no acredita LIVE; ver capítulo 63. [Especificación vigente](CURRENT_SPEC.md).

## 02 — Topología configurable de canales y ciudadanía

### Modelo obligatorio
`Campaign` (creador/propietario), `Season`, `Nation` (exactamente tres), `ChannelBinding` (plataforma+cuenta/canal), `ProviderIdentity` (usuario auténtico de proveedor), `Citizen` (persona jugable en una nación/temporada) y `BroadcastOutput` (overlay con filtros). `NationId` nunca deriva de `provider`, no puede ser nombre de plataforma, y es inmutable dentro de una temporada. `ChannelBinding` tiene roles explícitos: `commands`, `live_health`, `contributions`, `display_feed`. Cada nación designa exactamente un canal con `isClockAuthority=true`, `role=live_health`; su señal autenticada define el LiveClock de esa nación para no sumarlo dos veces si existen cuentas secundarias. Otras fuentes aportan chat y métricas pero no alargan el reloj. El operador puede cambiar la fuente de reloj solo pausando y auditando la revisión; en simulación hay control manual auditado.

### Ejemplos admitidos
1. Micelios=Twitch canal A, Rúnicos=Twitch canal B, Ferrinos=Twitch canal C.
2. Micelios=TikTok cuenta A, Rúnicos=TikTok cuenta B, Ferrinos=TikTok cuenta C (únicamente si la integración autorizada expone los eventos necesarios).
3. Micelios=YouTube canal A, Rúnicos=Twitch B, Ferrinos=TikTok C.
4. Una nación puede recibir dos canales distintos, por ejemplo streaming principal más un canal secundario, sin duplicar la identidad de un mismo usuario del mismo proveedor. Nunca asignar **el mismo canal** a dos naciones en una temporada: riesgo de votos/copias ambiguas.
5. Simulador local admite exactamente tres fuentes `simulated`, una por nación, sin fingir que son aportaciones monetarias reales.

### Persistencia de ciudadanía
Clave de usuario de proveedor = `(provider, providerUserId)`; nunca nombre visible. Ciudadano = `(seasonId, nationId, provider, providerUserId)` unívoco. Varios canales de **igual proveedor** asignados a misma nación producen **un solo ciudadano**. Una misma identidad del proveedor **sí puede crear ciudadanos distintos en naciones diferentes** cuando participa en sus respectivos canales, igual que en el diseño original podía participar con identidades de plataformas distintas; la clave lógica incluye `nationId`. Esto no permite duplicar ciudadanía dentro de la misma nación aunque el usuario aparezca en varios canales de esa nación. El sistema no promete impedir identidades alternativas entre proveedores.

**Criterio de migración:** cambiar la plataforma/cuenta asociada a una nación durante temporada activa es un cambio privilegiado que requiere pausa de entrada, drenaje de Inbox, grabar estado y `BindingRevision`; el ciudadano anterior mantiene su nación y stats; no se mueve automáticamente a otra. Cambios de binding requieren origen autorizado, usuario operador MFA y log. Cambiar de nación una misma cuenta ya registrada está prohibido durante la temporada.

### Entrada y permisos
Un adaptador `IPlatformAdapter` convierte `(provider, channel_id, event_id, received_utc, provider_user_id, capability, payload)` a `NormalizedEventV2`. El enrutador `BindingResolver` usa `(seasonId, provider, providerChannelId)` para obtener una sola nación; si no existe una asignación activa, `DROP_UNMAPPED` auditable. Mensajes de chat, estado LIVE y aportaciones son tres capacidades separadas; si no hay permisos para una, se desactiva solo esa capacidad. Un `binding` nunca puede autohabilitar monetización.

### LIVE y relojes por nación
Cada nación puede estar `LIVE_CONFIRMED`, `OFFLINE_CONFIRMED` o `UNCERTAIN`. `UNCERTAIN` cuenta como offline para economía y pausa votaciones; no consume tiempo de penalización de torneo. Para abrir una ceremonia de nueva era se requiere `LIVE_CONFIRMED` de la propia nación. Para un torneo simultáneo se requieren las tres naciones LIVE y un `broadcastSession` compatible. Ninguna nación debe quedar bloqueada para siempre por una cuenta desconectada: sigue simulando offline y acumula `EraReadyPending` hasta próxima emisión confirmada.

### Salidas y cumplimiento
Cada salida OBS tiene `OutputId`, `BindingId` emisor y una política `allowedNations`. Por defecto muestra solo elementos de ese canal, agregados del mundo permitidos y resultados del propio juego sin reproducir mensajes/reacciones crudos de plataformas ajenas. Mezclar chat, mensajes o referencias cruzadas requiere aprobación de política por proveedor. Ver `docs/16_INTEGRACIONES_Y_CUMPLIMIENTO.md`.


---

## Fuente 03 — `docs/03_TIEMPOS_SIMULACION_Y_DETERMINISMO.md`

**Blob de origen:** `3b73d8fd690a10099f2222a2c4a3260227f7afc8`.

## 03 — Relojes, scheduler, replay y estados

### Relojes tipados
- `UtcClock`: tiempo físico, monotónico verificado contra reloj de sistema; expiraciones de ciudadanos (+7200s), caducidades de OAuth, misiones UTC. Se almacena la fecha absoluta además del evento.
- `NationLiveClock`: integra exclusivamente segundos `LIVE_CONFIRMED`; elección 3600s, segunda vuelta 180s, proyecto 600s, prioridad 300s, bonus prioridad 5400s. Se congela en `UNCERTAIN`, `PAUSED` o `OFFLINE_CONFIRMED`.
- `CompetitionLiveClock`: global por evento programado, avanza 1s solo cuando las tres naciones están LIVE confirmadas; RPS 90s y descansos 30s; congelación conjunta ante cualquier caída.
- `NationEconomyClock`: 1 segundo equivalente en LIVE, 0,2 en OFFLINE/UNCERTAIN; sin doble aplicar al recuperar.
- `NationActivePenaltyClock`: avanza 1s solo en LIVE; una región penalizada consume exactamente 1800s activos; NUNCA consume segundos fuera de emisión.

No sumar segundos a ciegas: cada segmento `[lastProcessedUtc, nowUtc)` se particiona por cambios de estado LIVE, expiraciones de trabajadores, cierre de sesiones y vencimientos de comandos. La producción y experiencia se calculan en el mismo segmento. Un comando entra al tick siguiente; `receivedUtc` decide si se admite en una votación abierta cuando se recibió durante intervalo. Eventos con `providerTimestamp` fuera de tolerancia se ponen en cuarentena.

### Orden canónico por tick (enmienda v2.3)

**Fuente normativa:** [64 — Relojes y eventos](64_RELOJES_EVENTOS_Y_CONTRATOS_v2.3.md). Durante cada subsegmento se procesan: (1) eventos autenticados con ingestSeq y cambios LIVE; (2) comandos/papeletas recibidos antes del límite del reloj LIVE; (3) cierres de voto/competición vencidos; (4) alimentación, economía, XP; (5) edificios, investigación, misiones; (6) hitos y transición de era; (7) arbitraje global de ganador/maravillas; (8) commit de estado/ledger/outbox, y publicación posterior. Las subfronteras temporales se preservan para un replay exacto.

**Economía:** el delta efectivo es tiempo UTC segmentado × factor LIVE 100 % u OFFLINE/UNCERTAIN 20 % una sola vez. No se vuelve a multiplicar al calcular output ni XP. La aceptación de un comando (ACK) puede preceder al siguiente tick productivo; la mutación de economía no promete latencia inferior al tick de 5 s.

**Competición:** RPS y batalla automática usan CompetitionLiveClock global solo con tres LIVE confirmados; ante caída de una nación se congela en las tres.

### Idempotencia y replay
`sourceEventKey=SHA256(provider + bindingId + originalEventId + eventType)`; `commandId` se asigna una vez tras inbox. `rulesetHash`, `contentHash`, `seasonSeed`, `engineVersion`, `remainderVectors` se guardan en snapshot. RNG `sha256-counter-64-v1`: `sha256(seed||domain||counter_be64)`, valor uniforme por rechazo para evitar sesgo (`limit = floor(2^64/n)*n`). Counters separados por dominio (`elections`, `tournaments`, `map`, `events`) y nación; este detalle evita cambios de resultados al añadir más narración.

Replay desde snapshot requiere mismo runtime numérico y mismo orden de eventos/segmentos. Un bug de versión no se corrige editando transacciones pasadas: abrir migración/compensación con evento auditable.

### Caída larga
Hasta siete días de interrupción se integra economía offline exactamente por segmentos y checkpoints. A partir de siete días el sistema entra en `NEEDS_OPERATOR_REVIEW` y no aplica catch-up adicional hasta que un operador resuelva y audite la decisión. Ninguna transición de era ocurre automáticamente en catch-up. Las ventanas electorales quedan congeladas si no hay LIVE confirmado.

### Inicio y fin de temporada
`DRAFT → PREPARED → RUNNING → COMPLETED → ARCHIVED`, con derivaciones `PAUSED`, `RECOVERY_REQUIRED`. Start a hora UTC única y seed inmutable. Las tres naciones arrancan en Paleolítico en el mismo commit. En cuanto `EraAdvanced` de una nación entra en Interestelar, un `SeasonWinnerClaim` atómico fija ganador, finaliza la producción competitiva y prepara ceremonia de cierre; empate mismo instante resuelto por secuencia de commit, no aleatoriedad. Estadísticas, historia, prestigio y logros persisten; economía no se transfiere.


---

## Fuente 04 — `docs/04_ECONOMIA_Y_BALANCE.md`

**Blob de origen:** `fab7a96a5f5668b6d7ecf59c42145cc8eced1032`.

> **Enmienda v2.3:** evitar doble ralentización offline; [semántica de reloj única](64_RELOJES_EVENTOS_Y_CONTRATOS_v2.3.md).

## 04 — Reglas numéricas del motor económico

### Unidades y precisión
Todas las cantidades ordinarias se almacenan como `BIGINT` en **milésimas de recurso**; las tarifas en milésimas por minuto de trabajador. Los porcentajes son puntos básicos (`10000 = 100 %`). Todos los cálculos son enteros y guardan resto por `(nationId,resourceId,workerPoolId)` para que cambiar el tamaño de tick no cambie sistemáticamente la producción. Nunca usar `double`, `float` ni `Math.random()` para estado persistente. El oro se guarda en unidades indivisibles por asiento de ledger. Toda tasa depende del `rulesetHash` fijado al iniciar temporada.

### Producción por grupo y minuto efectivo
Para cada familia `f`, `EffectiveWorkerMinutes = NPC_count + sum(human_weight)` multiplicado por `deltaEconomySeconds/60` donde deltaEconomySeconds YA incorpora el factor LIVE/OFFLINE. El trabajador humano recién unido y NPC tienen la misma tasa base; veteranos añaden exclusivamente sus perks individuales. Base por minuto: alimento 2,400; madera 1,800; piedra 1,400; mineral 650; conocimiento 1,200; trabajo de construcción 1,200 (milésimas). Minero divide su capacidad: desde era 3, 75 % en piedra y 25 % en mineral, con reasignación si uno está al máximo o no hay necesidad. Antes de era 3, 100 % piedra.

`OutputMilli = floor((workerSeconds * rateMilliPerMinute * eraFacilityBp * governmentBp * priorityBp * starvationBp * penaltyBp) / (60 * 10000^N) + persistedRemainder)`, con cada término calculado en entero y redondeo final único; orden de multiplicadores fijo. La producción de humanos aplica perk de manera individual/por cohortes con mismo conjunto de perks, no a población entera. `facilityBoostBp` se suma para un máximo +3000bp. Bonificaciones de oficio individual con tope +1800bp; el total compuesto final de todos los bonus se recorta a 15000bp. Los NPC no obtienen habilidades.

### Desaceleración de masas
Cada ciudadano humano activo contribuye al trabajo agregado, pero su eficiencia marginal se atenúa para evitar ventaja lineal de 10.000 espectadores. Primeros 100 activos por oficio al 100%; del 101 al 2500 al 25%; a partir del 2501 solo representación y progreso personal reducido si estaba activo, sin creación adicional de recursos. El orden de asignación de cuotas es `(activeSinceUtc, citizenId)` determinista, reponderado cada tick; se conserva XP conforme a contribución efectiva. Los números no determinan resultados de torneo, que usan una decisión por nación.

### Mantenimiento, hambre y bloqueo
La población inicial tiene 24 NPC, repartidos 7/5/4/4/4. Mantenimiento alimentario: 150 milésimas por NPC y por unidad de trabajador humano **efectivo** y por minuto de economía, con máximo de 50 unidades humanas imputables al mantenimiento para que un gran chat no produzca inanición por participación visual sin trabajo. Primero se consume alimento; si hay déficit parcial, se aplica productividad colectiva 65 % al segmento posterior. Nunca hay muertes. Las misiones no regalan oro. Los NPC pueden construir todas las obras básicas. Las fuentes naturales siempre permiten producir `food`, `wood`, `stone`, `knowledge` desde el comienzo sin edificios, para evitar el bloqueo circular «no hay edificio para producir materiales necesarios para construir un edificio». `ore` se desbloquea en era 3.

### Capacidad y planificador
Capacidades base por nación: food/wood/stone/ore = 3500 unidades; knowledge = 15000 unidades. `storage` agrega +1500 unidades en todos los almacenes ordinarios, +350 por era posterior. No se produce un recurso que alcanzó máximo; NPC se reasignan a recurso válido (prioridad comida, materiales necesarios, investigación, construcción); el humano conserva familia y no produce cuando su output está saturado. Nunca se pierde silenciosamente una producción: contabilizar `blockedByCapacity` separado de `produced` y de XP.

### Bootstrap y progresión
Se empieza con **cero recursos y cero edificios**, pero una zona natural de cada profesión, 24 habitantes NPC y capacidad de almacén base virtual (terreno/capacidad de supervivencia). El `Autoplanner` arranca edificios en cuanto exista material y trabajo; reservas y commit de costes son atómicos. La economía offline al 20 % (aplicada una sola vez al delta temporal efectivo, también para XP y hambre) permite completar la ruta gratuita de cinco hitos por era sin humanos, aunque tardará significativamente más; el cambio de era requiere volver a LIVE.

### Invariantes contables
`stock >= reserved >= 0`; `stock = initial + sum(verified productive events + mission rewards - consumption - building spends - penalties)`. Cada evento se aplica una sola vez. La falta de suministro no hace stock negativo. `gold` no participa en fórmulas de producción, ejército, progreso ni votaciones ciudadanas. Reversiones generan asiento corrector, jamás eliminación de asientos originales. El subledger oro se reconcilia contra contributions identificadas; la deuda de reversos se almacena aparte cuando ya no hay saldo.

### Balance candidato y ciclo de ajustes
Era 1 exige producir 6.400 alimento, 4.750 madera, 3.420 piedra y 2.650 conocimiento, además de la tecnología básica, del edificio cívico automático y de una misión colectiva; cada una de las cinco categorías da 20 puntos. Eras sucesivas aumentan umbrales linealmente. Progresión objetivo aproximada de 2,5 días/era es hipótesis de diseño y puede no cumplirse con cualquier reparto: antes de LIVE se ejecutan simulaciones de 7/24, 24/0, 100/0 y 10000/0 humanos/NPC, buffers bajos, hambre, offline al 20 %. Toda nueva calibración versiona `rulesetId`; nunca aplicar ajustes económicos mid-season sin regla de migración públicamente comunicada.


---

## Fuente 05 — `docs/05_EDIFICIOS_Y_MAPA.md`

**Blob de origen:** `ba7c2c787f8b3c2fc5bf2ef196573313deefa6a0`.

> **Enmienda v2.3:** un Consejo por nación y era jugable, tres alternativas financiables sin oro; las dos no elegidas se descartan para esa era. Las obras ordinarias siguen siendo automáticas. [Norma actual](CURRENT_SPEC.md).

## 05 — Construcciones básicas, proyectos y mapa

### Catálogos
`data/buildings.v2.json` declara 130 edificios básicos explícitos (10 familias x 13 eras), cada uno con precio por recurso, trabajo, 4 etapas, era de desbloqueo, capacidad, footprint y efecto. `data/strategic_projects.v2.json` declara 39 proyectos optativos (3 x era) más 13 maravillas exclusivas opcionales. **Desde la revisión v2.2 ambos catálogos cuestan solo recursos ordinarios, con `gold=0`.** **Desde la revisión v2.2 ambos catálogos cuestan solo recursos ordinarios, con `gold=0`.** Todos los edificios anteriores permanecen y conservan sus efectos con productividad relativa de 80 % al quedar obsoletos; no se destruyen automáticamente.

### Algoritmo de autoconstrucción básico
Cada 60s de reloj de economía (o cuando se desbloquea nueva era), el planificador inspecciona y añade como máximo dos planes básicos, respetando `maxConcurrentWorks=5` y `maxAutoQueued=2`. Prioridades ordenadas: `food_production` si comida insuficiente/capacidad de trabajo, `storage` si utilización de cualquier stock > 75 %, `housing` si NPC en límite y alimentación sostenible, `extraction/forestry` si faltan materiales para obra pendiente, `research` si conocimiento insuficiente, `workshop` si facility boost bajo, `civic` de era actual si pendiente, `defense` después, `infrastructure` al final. A igual prioridad elegir costo menor y después `buildingId` lexical. Siempre que una obra obligatoria resulte materialmente imposible por su propia dependencia, usar fuente natural gratuita y guardar `WaitingResources` sin crear materiales sintéticos. `civic` de cada era no necesita una tecnología que requiera completar su mismo hito. Los edificios de familias `workshop` y `research` de cada era sí requieren su tecnología troncal `tech_{era}` según el catálogo corregido v2.2. Los edificios de familias `workshop` y `research` de cada era sí requieren su tecnología troncal `tech_{era}` según el catálogo corregido v2.2.

El costo ordinario se reserva al planificar y se descuenta **una vez** cuando empieza la obra; producción de construcción separada en `buildWorkUnits`, no compra materiales otra vez. Fallos de arranque cancelan reserva antes del commit; edificios que no encuentran parcela esperan en `WaitingPlot` y generan expansión determinista, nunca se pierden recursos.

### Estrategias
La participación en el Consejo NO depende de aportar dinero. La participación en el Consejo NO depende de aportar dinero. Cada era ofrece tres alternativas de su familia de proyectos (`memorial/spectacle/archive`). El Consejo **solo abre** si hay tres alternativas distintas sin construir, todas individualmente financiables con saldo *disponible*. La reserva durante voto es el máximo componente a componente de cada vector de coste (`max(costO1[r], costO2[r], costO3[r])`). Si durante la votación no llega papeleta, se selecciona una de las tres de modo uniforme, auditado por RNG y seed; el coste ganador se descuenta de la misma reserva vectorial y el exceso se libera. Votación = 600s LIVE por nación. Nadie puede comprar votos. No existen reversos de oro aplicables al Consejo: sus tres opciones son gratuitas respecto a oro. Una reserva ordinaria válida se confirma solo una vez; conflicto transaccional de recursos se audita y cancela sin doble cargo.

Como se pueden aprobar obras en distintos ciclos de eras posteriores, hasta cinco obras avanzan simultáneamente si hay trabajadores. Una sola votación estratégica está abierta por nación para evitar dobles reservas. Las maravillas son proyectos separados de festival (no consumen una de las tres alternativas del Consejo) y requieren su propio evento programado; primera nación en completar y reclamar atómicamente obtiene la única maravilla global. Las otras pueden conservar la obra como monumento no exclusivo sin premio de exclusividad y sin reembolso, informado antes de construir.

### Construcción visual
Cuatro etapas según progreso de trabajo: 0–15 % parcela/cimientos, 15–40 % armazón, 40–70 % obra, 70–100 % remate. En 100 % se añade `BuildingCompleted` y se activa efecto. Se renderiza sin pathfinding por cada NPC, y la animación jamás determina productividad. `BuildingInstance` conserva era de origen, nivel, transform y slot de trama estable.

### Mapa procedural y representación
Semilla de temporada, mapa inicial 48×48 casillas, proyección de tile 32×16 y altura de capas decorativas. Expansión en un margen de ocho casillas por lado por era, con tope 256×256. Algoritmo reproducible: hash de `(seed,nation,x,y,layer)`, ruido de 2 octavas en celdas, máscara de terreno totalmente edificable en al menos 70 % del mapa; todas las naciones tienen igual **número y disponibilidad de parcelas lógicas**, bioma solo estético. Parcelas y colisiones de servicios son compartidas, efectos de área normalizados por nación. Si no cabe construir, expandir y buscar primera parcela libre `(distanceFromCenter, y, x)`; no bloquear progreso por cosmética.

### Retrocompatibilidad
La persistencia de edificio histórico no autoriza producir por encima de la capacidad de almacén. Los nuevos edificios hacen más eficiente a cada familia con techo +3000bp, y el antiguo conserva un factor relativo de 80 % para que lo nuevo tenga sentido sin castigar al espectador con destrucciones visuales.


---

## Fuente 06 — `docs/06_PROFESIONES_HABILIDADES_Y_XP.md`

**Blob de origen:** `7c3b66408efb66ee2541760681fb29214bf8c294`.

> **Enmienda v2.3:** el límite de 2500 trabajadores humanos de diseño aplica **por profesión y nación** hasta revisar el balance; la XP usa deltaEconomy efectivo una sola vez. Ver [CURRENT_SPEC](CURRENT_SPEC.md) y [doc 64](64_RELOJES_EVENTOS_Y_CONTRATOS_v2.3.md).

## 06 — Ciudadanos, profesión única, XP y especializaciones

`!join` registra una identidad verificada de canal; no asigna oficio ni inicia producción. `!work <familia>` elige única familia durante temporada. Repetir la misma familia o `!active` prolonga `activeUntilUtc=receivedUtc+7200s` tras validación y cooldown de 60s; escoger otra familia devuelve `PROFESSION_LOCKED` sin renovar. El tiempo de trabajo no se acumula: renovar no añade dos horas al saldo previo. Una inscripción tardía puede participar en votos mientras el período esté abierto.

### Niveles
Al terminar cada segmento de trabajo efectivo, `xp += floor(6 * effectiveWorkMinutes)` con resto persistido; la XP en OFFLINE deriva del tiempo de economía efectivo al 20 %, **sin volver a aplicar 0,2**. Nivel N requiere XP acumulada `250*(N-1)^2`, hasta nivel 20. Activación, voto, chat, caminar y renderizar no dan XP. Las recompensas de misión pueden otorgar XP si están explícitas; default de v2.2: misiones colectivas solo recursos, no XP adicional, para no duplicar. Los NPC no suben niveles ni desbloquean skills.

### Árboles
Tres elecciones irreversibles en niveles 3, 7 y 12; dos opciones exactas por bifurcación. `data/skills.v2.json` fija 30 habilidades, cada una con efecto objetivo y `additiveBp`. Los efectos son **personales**: no existen auras de reducción colectiva que crezcan sin techo con miles de usuarios. Habilidades históricas de 'rationing', 'reuse' e 'innovator' se redefinen como productividad/eficiencia individual equivalente sin impacto monetario, manteniendo intención temática pero eliminando exploit de multiplicación global. Máximo acumulado +1800bp por ciudadano. Sin `!skill`, no se asigna nada. Al volver a temporada siguiente se conserva historial de elecciones en museo, no se conserva bonus.

### Familias
- food: alimento de terreno o edificio según era, con sprite cazador→síntesis.
- wood: madera/biomasa; la etiqueta cambia, el resourceId `wood` no cambia.
- mine: piedra y mineral (mineral desde era 3), sin material por época arbitrario.
- build: aporta `buildWorkMilli` a obras comprometidas; si no hay obras, no crea recursos, pero puede hacer animación de mantenimiento y no gana XP por tarea ficticia.
- research: genera conocimiento con acumulación y desbloqueos automatizados gratuitos de tecnología.

### Control de audiencia masiva
Cada identidad puede tener un ciudadano por nación/temporada dentro de reglas de asignación de canales. Para trabajo agregado hay 100 plazas de contribución plena por profesión y 2400 plazas marginales al 25 %. Un humano fuera del tope sigue apareciendo, votando y alcanzando logros sin crear recursos ficticios; para evitar falsos mensajes de progreso se le muestra explícitamente el estado «turno visual / lista de trabajo saturada» y no se le abona XP de trabajo inexistente. El algoritmo de cuotas deterministic permite rotación por bloques de 10 minutos de LIVE para que los últimos usuarios no queden siempre sin producción; orden de rotación `(hash(citizenId,rotationIndex),citizenId)`.

### Trabajo y sueño
El ciudadano descansa exactamente al caducar `activeUntilUtc`. Un evento de plataforma retrasado no vuelve a activar una ventana del pasado más allá del límite de tolerancia. No hay muerte permanente ni barras de hambre individuales. El nombre visual es moderado; se registra ID interno separadamente del displayName público.


---

## Fuente 07 — `docs/07_PROGRESION_TECNOLOGICA_Y_TEMPORADAS.md`

**Blob de origen:** `00964855123b4b21b07c738a45f8e39420953052`.

> **Enmienda v2.3:** 12 eras jugables con misión propia; era 13 epílogo sin ciclo ni autoplanner. Ver [CURRENT_SPEC](CURRENT_SPEC.md) y [misiones de era](../data/era_missions.v2.3.json).

## 07 — Progresión histórica, investigación y temporadas

### Eras y victoria
13 épocas (orden congelado en `eras.v2.json`): paleolithic, neolithic, copper, bronze, iron, antiquity, medieval, renaissance, industrial, modern, digital, space, interstellar. Todos los mundos inician la primera época en un commit global. `EraReadyPending` se alcanza al reunir 100 puntos y se confirma nueva era únicamente con nación LIVE. La **primera entrada confirmada en `interstellar`** fija ganador y termina la competición de inmediato. La era final sirve como epílogo visual y archivo, **no abre elecciones ni un nuevo ciclo jugable**, excepción imprescindible para no contradecir el cierre al entrar en ella.

### Hitos y barra
Cada era jugable (1–12) tiene cinco hitos únicos de 20 puntos: producción de comida; producción de madera **y** piedra; conocimiento + investigación básica completada; finalización del ágora cívica automática; y primera misión colectiva completada durante esa era. La misión del hito es una **misión colectiva específica de cada era** (catálogo `data/era_missions.v2.3.json`), completada con trabajo productivo real de NPC o humanos. Las misiones diarias/semanales dan recompensas ordinarias independientes y no otorgan este hito. Los objetivos cuantitativos son `data/milestones.v2.json`. Se contabilizan unidades **producidas efectivamente y aceptadas** en esa era, no entradas de misiones ni consumos, y por eso no pueden repetirse para acelerar. Los 100 puntos no se multiplican por audiencia ni por donaciones. Los hitos cumplidos fuera de emisión se guardan; la ceremonia queda pendiente. El hito de era interestelar está materializado como catálogo de epílogo, no es exigido para ganar.

### Árbol tecnológico
Para cada era: 1 investigación automática de ruta gratuita `tech_{era}` y 2 opcionales de economía/defensa, todas sin oro. Conocimiento producido se almacena y gasta; la investigación automática se inicia si hay conocimiento después de respetar reservas de obras. Ninguna tecnología es prerrequisito circular de los hitos del mismo período. Las ramas optionales se anuncian; no retrasan la entrada a era siguiente. La prioridad votada no bloquea caminos, solo bonifica temporalmente una categoría.

### Rendimiento y duración
El objetivo narrativo son 2–3 días por era, no una promesa técnica. El baseline fija 20 % de economía offline y umbrales lineales; el balance real depende de horas de directo, espectadores y distribución de profesiones. Para reducir dependencia de audiencia masiva, los hitos no escalonan por cantidad de participantes, y el trabajo extra tiene rendimiento marginal decreciente. Solo se cambiarán valores entre temporadas tras una simulación completa de todos los hitos; cambios intratemporada requieren evento de migración auditado y anuncio.

### Cierre y persistencia
Al cerrar temporada se publica `SeasonCompleted`: nación ganadora, fecha, reglas y hashes, estadísticas de trabajo, economía, obras, elecciones y torneos; se convierte oro sin gastar en puntuación de prestigio visual 1:1, sin opción de canje y sin bonus en la siguiente carrera. No migran recursos, edificios, XP ni profesiones; sí identidad de proveedor para facilitar recuperar usuario, historial de logros, badges y estadísticas. Los ciudadanos de la nueva temporada son registros nuevos asociados a la identidad previa.


---

## Fuente 08 — `docs/08_GOBIERNO_VOTACIONES_Y_CONSEJO.md`

**Blob de origen:** `6cedca438dbce8b6e67a287624c1b019b999ca71`.

> **Enmienda v2.3:** los plazos de voto se miden con reloj LIVE acumulado, no UTC fijo; el Consejo es uno por era y se cierra tras elegir un proyecto. Ver [64](64_RELOJES_EVENTOS_Y_CONTRATOS_v2.3.md).

## 08 — Elecciones NPC, prioridades y Consejo de Construcción

### Gobiernos
Tres candidatos NPC recurrentes por nación y era jugable: económico, militar y científico. No son espectadores, no ocupan tres cargos simultáneos y no vetan decisiones comunitarias. La elección se abre al entrar en era 2–12, durante 3600s de LiveClock. En era 1 se abre inmediatamente al comenzar la temporada con LIVE; en era 13 se omite, ya que la temporada concluye al entrar. Pueden votar todos los ciudadanos registrados en esa nación antes del cierre, incluso si están descansando; una papeleta vigente por ciudadano, actualizable mediante `!gov economy|military|science`. En igualdad de máximos se abre segunda vuelta solo entre empatados durante 180s LIVE; en igualdad persistente se usa sorteo uniforme, auditado; sin un solo voto se sortea uniformemente entre los tres.

### Bonificaciones exactas
Gobierno económico: +300bp (3 %) al output ordinario `food/wood/stone/ore`. Gobierno científico: +300bp a `knowledge`. Gobierno militar: +500bp a puntos **defensivos de unidades NPC** durante eventos programados; no afecta RPS. Estos efectos no conceden puntos históricos automáticos ni cambian votos, oro, costes de proveedor o economía de otra nación. El bono permanece durante la era a partir del cierre de elección; antes de cierre no existe bonus. Los títulos y ropa evolucionan según época sin sustituir identidad del NPC.

### Prioridad de nación
Tras resolverse la elección (incluida segunda vuelta), se abre votación independiente de 300s LIVE `!priority economy|science|defense`. Un ciudadano puede cambiar su voto antes de cierre. Prioridad económica: +800bp a recursos ordinarios; ciencia: +800bp a conocimiento; defensa: +800bp a defensa NPC de eventos programados. Dura 5400s de LiveClock desde cierre y expira aunque se haya cambiado de era (si hay transición temprana, se cancela al comenzar nueva era). Sin votos: elección por rotación reproducible entre ramas, sin sesgo de audiencia. En empate: sorteo uniforme entre empatadas. No se concede nada si termina la temporada.

### Consejo Estratégico
Doctor K-0 puede convocar **un solo Consejo por nación y era jugable**, cuando hay exactamente 3 opciones distintas, desbloqueadas, sin construir y **costeables individualmente con recursos ordinarios (oro=0 desde v2.2)**, con al menos 3 proyectos disponibles según catálogo. Si no se satisfacen condiciones, muestra «proyectos pendientes de recursos» y no abre votación. Durante 600s LIVE cada ciudadano puede votar/reemplazar `!build projectId`; al cerrar se selecciona mayoría o desempate determinista, se cobra **solo** el proyecto vencedor y se libera la diferencia de la reserva vectorial. Si no hay votos, sorteo uniforme entre 3. Una sola votación estratégica abierta por nación; varias **construcciones** aprobadas pueden progresar a la vez. Las elecciones NPC, prioridades y Consejos no se solapan dentro de la misma nación: `PoliticalScheduler` serializa elección→prioridad→Consejo en cola. Las sanciones de torneo no alteran ventanas de voto.

### Conflictos y reloj
Votos con recepción autenticada **anterior al límite acumulado NationLiveClock** y LIVE Confirmed en recepción entran; no asumir `closeUtc` fijo durante pausas. Votos retrasados o duplicados no cambian resultado. Si cae fuente LIVE, la ventana se congela y puede reanudarse. Un cierre se hace en transacción con lock de votación y certificado de resultado (`counts`, `eligible`, `seedCounter`, `rulesetHash`). Una transacción no puede cargar recursos dos veces ni crear una construcción mientras el Consejo permanezca OPEN. El oro queda fuera de las obras estratégicas desde v2.2 y solo sirve para reconocimientos cosméticos independientes.

