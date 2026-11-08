# Fuentes íntegras v2.5 — capítulos 9–16

> **Anexo de preservación literal**, no nuevo conjunto de reglas. Contiene los textos completos que se habían definido, incluso redacciones heredadas. En caso de contradicción manda [norma unificada](../ESPECIFICACION_MAESTRA_v2.5.md). Los valores ejecutables se consultan en JSON canónicos.

---

## Fuente 09 — `docs/09_TORNEOS_EVENTOS_Y_MISIONES.md`

**Blob original:** `987f08d03f3a86ef64e8da55b49479ee46a6ddef`.

> **Enmienda v2.3:** torneos triangulares requieren CompetitionLiveClock global que se congela si deja de estar LIVE cualquiera de las tres naciones. Consultar [64](64_RELOJES_EVENTOS_Y_CONTRATOS_v2.3.md).

## 09 — Torneos, sanciones, eventos y misiones

### RPS triangular exacto
Se anuncia un torneo programado solo cuando las tres naciones están LIVE confirmadas; cada encuentro tiene 5 rondas de 90s LIVE de voto y descansos de 30s LIVE, más máximo 2 rondas extraordinarias para desempate de la cabeza. Cada nación toma el `rock/paper/scissors` mayoritario entre ciudadanos únicos (`!rps` primera papeleta válida irrevocable); no se muestra ninguna distribución antes del cierre, solo el número total de votantes. Empate interno: RNG uniforme reproducible entre opciones empatadas. Sin votos, opción `PASS`, nunca voto NPC inventado.

### Sistema triangular
Resolver **tres enfrentamientos por parejas** A-B, B-C y C-A. En cada enfrentamiento victoria=2 puntos, empate misma elección=1 a cada nación, derrota=0; opción PASS pierde frente a una opción válida (0–2), PASS vs PASS da 0–0. Cuando las tres naciones escogen rock-paper-scissors distintas, cada una gana una vez y pierde otra, por tanto 2 puntos, no se inventa ganador. Se suman puntos de 5 rondas, y solo si hay empate por primer puesto se disputan 2 rondas extraordinarias. Si continúa el empate, declarar victoria compartida sin castigos y sin «moneda al aire». La mayoría interna no multiplica puntos por total de espectadores, eliminando la ventaja automática de audiencia bruta.

### Derrota y territorio
Solo hay sanción material a una nación con menos puntos que **un ganador único**; derrota = pérdida del 2 % de `wood/stone` **disponibles** con redondeo hacia abajo y tope en saldo; jamás oro, conocimiento, edificios ni ciudadanos. Sanción territorial: elegir sector no esencial con máximo 10 % del output ordinario de la nación; ese sector no produce durante 1800s `NationActivePenaltyClock`, que solo avanza cuando la nación está LIVE, no offline. Si no hay sector secundario válido se muestra penalización visual y no se corta una fuente natural obligatoria para progresar. Un empate no genera penalización.

### Eventos fuera de torneos
Únicamente eventos preautorizados de `events.v2.json` activados por `ShowDirector` u operador, con anuncio previo y cooldown; nada de agresiones automáticas, fauna hostil permanente o desastres espontáneos. `catchup_challenge` se ofrece solo a naciones al menos 2 eras retrasadas, máximo 2 veces en temporada, +5 % NPC durante 30 minutos LIVE, sin puntos históricos directos ni oro. `resource_storm` es evento anunciado de reducción temporal moderada, frecuencia máxima cada 12 horas LIVE; `wildlife_parade` cosmético; `wonder_festival` abre actividad especial de maravilla si las reglas lo admiten.

### Misiones
Tres tipos diarios y dos semanales definidos en `missions.v2.json`; aparte, una misión productiva por era jugable (`era_missions.v2.3.json`) que puede cumplir NPC sin depender del cambio de día UTC. Periodos UTC completos: día desde 00:00 UTC; semana desde lunes 00:00 UTC. Los NPC pueden progresar y completar objetivos colectivos cuando no hay público; recompensas automáticas por nación una sola vez por instancia; al expirar la ventana se descarta misión no completada. Recompensas son materiales ordinarios no restringidos por monetización y **no añaden puntos a la barra de hitos**. Recompensas que excedan almacén se recortan con `rewardOverflowDiscarded`, auditado.

### Segunda modalidad de evento definida en v2.2

Además de RPS existe un **torneo automático de guarniciones** exclusivamente programado y con las tres naciones LIVE. Su catálogo de 39 roles/era, formación, costes ordinarios, combate sin azar y penalización no acumulativa se detalla en [`docs/43_EJERCITOS_Y_COMBATE_AUTOMATICO_v2.2.md`](43_EJERCITOS_Y_COMBATE_AUTOMATICO_v2.2.md). La simulación de esa modalidad todavía no está ejecutada.


---

## Fuente 10 — `docs/10_MONETIZACION_LEDGER_Y_CONTRIBUCIONES.md`

**Blob original:** `e11216e3ad2c96672ced181608bb689156ac4ff8`.

## 10 — Monetización verificable, ledger y límites

### Criterio de elegibilidad
`ContributionEvent` proviene de canal con `contributions` habilitado por operador; se requiere autenticación del origen, identificador estable, evidencia verificable del tipo/importe, estado económico final admisible y `conversionRuleVersion` activa para esa **plataforma, canal, tipo y moneda/unidad**. No se deduce equivalencia por texto libre, reacción, follower ni cantidad de likes. El proveedor puede cambiar campos, permisos, elegibilidad y reglas. Por defecto **todos los tipos reales de monetización están deshabilitados**, y no hay cambio automático a habilitado sin prueba con cuenta real. El juego gratuito funciona íntegramente así.

### Conversión y ejemplos
Conversión exacta por `provider, eventType, unit, ruleVersion`: `goldUnits=floor(verifiedAmountMinorUnits * numerator / denominator)`; guardar resto solo dentro del evento y sin inventar crédito. La configuración demo exclusivamente sintética define `provider=simulated, unit=DEMO, eventType=test_contribution, numerator=1, denominator=1`, a usar únicamente bajo `mode=SIMULATION`, jamás en entorno LIVE. Para plataformas reales se publica tabla tras revisar APIs y términos, no se escriben tasas falsas ni se atribuyen precios a regalos. Nunca se hacen conversiones genéricas entre monedas de proveedores.

### Estados de ingreso
`RECEIVED → AUTHENTICATED → VERIFIED → CREDITED` o `REJECTED`; también `REVERSED` tras `CREDITED` si existe evidencia de devolución/cancelación. Un evento reintentado produce un solo crédito gracias a unique `(provider, eventId, channelId, eventType)`. `CREDITED` añade al ledger oro y a tesorería de nación, no al bolsillo individual del donante. Cambio posterior de reglas no recalcula histórico.

### Reversos tras gasto
Si una reversión deja sin cobertura el hold de una votación abierta, la votación se cancela en la misma transacción y el hold se libera antes del asiento de reverso. Si se revierte el oro ya gastado, el saldo disponible se reduce hasta cero y el resto se registra como `goldDebtUnits` sin saldo negativo y sin tocar construcciones completadas; los siguientes ingresos verificables pagan deuda primero. El patronazgo queda marcado `reversed` y puede perder el reconocimiento visual conforme a política anunciada; no hay devolución automática por el videojuego ni política de compensación externa. La contabilidad interna del oro nunca reclama ser un balance de dinero fiduciario.

### Protección de jugador y monetización sana
Prohibido transferir oro, convertirlo en dinero real, apuestas, premios de valor real, bonificación de voto o condición de avanzar de era. Los proyectos de Consejo y maravillas pasan a `gold=0` en v2.2; el oro se destina únicamente a reconocimientos cosméticos independientes especificados en `data/cosmetic_sponsorship.v2.2.json`. Ganar no se compra. UI muestra claramente si la cuenta no tiene donaciones habilitadas. Mostrar estado de agradecimiento privado y nombres solo con moderación y criterios de privacidad. Cualquier funcionamiento de monetización requiere revisión legal, fiscal, de proveedor y tests de auditoría; estas condiciones no son definibles por documentos internos.


---

## Fuente 11 — `docs/11_DIRECTOR_DOCTOR_K0_Y_MODERACION.md`

**Blob original:** `0c4ca91ec8116bcdfea11d89708e6b0fbb537b59`.

## 11 — Doctor K-0, narrativa y control de actos

Doctor K-0 es un cyborg científico físico dentro de las tres representaciones del mundo, con rostro mecánico, un ojo óptico, extremidades de ingeniería y cápsula de voz, nunca mascota blanda o Corálido. Su voz es sarcástica/provocadora, neutra respecto a las facciones y nunca utiliza insultos discriminatorios, burlas a donantes por no pagar ni afirmaciones falsas sobre apoyo económico.

### Arquitectura del show
`ShowDirector` decide eventos dentro de whitelist y cooldown; genera `Cue` tipado (`era_ready`, `government_open`, `government_result`, `priority_open`, `strategic_available`, `strategic_result`, `tournament_start`, `tournament_result`, `food_crisis`, `storage_full`, `season_completed`, `safe_idle`). `NarrationService` produce texto desde plantillas primero; LLM opcional solo reescribe tonos dentro de plantilla permitida, no crea reglas, saldos, ganadores ni acciones. `TTS` reemplazable con caché por hash de frase y voz; si falla, subtítulo y sonido local. Estado de narración `PENDING → READY → PLAYING → DONE | SKIPPED`, y límite 1 cue prioritario cada 20 segundos con cola máxima 20, descartando cosméticos viejos y nunca eventos financieros.

### Moderación y datos personales
DisplayName se sanitiza (control chars, URLs, PII básica y palabras prohibidas) antes de entrar a sprite, placa o speech; retener el identificador estable internamente con seudonimización/criptografía. Comandos y regalos no permiten inyectar instrucciones al LLM. No envíe chat bruto a LLM salvo consentimiento/configuración aprobada; preferir datos agregados. Perfiles, stats y nombres borrables/redactables sin romper ledger contable. Errores de comunicación a chat son *best effort*, no deben provocar reintento de transacción de juego.

### Plantillas canónicas
- `join`: «¡{displayName}! Bienvenido al experimento. Elige oficio: food, wood, mine, build o research con !work.»
- `profession_locked`: «Profesión fijada esta temporada. Usa !active para volver al trabajo.»
- `era_ready`: «La ciencia empuja a {nationName} al límite... esperaremos al directo para cambiar de era.»
- `vote_open`: «Tres obras financiables. Solo una será aprobada. ¡Tenéis diez minutos de emisión!»
- `season_end`: «El experimento tiene ganador: {nationName}. Todo queda registrado. No hay reinicio de memoria histórica.»

El operador tiene siempre botón `MuteNarration`, `PauseSource`, `CancelEvent`, `SafeScene`, `EmergencyStop`. Todas las acciones quedan registradas con actor, motivo y timestamp.


---

## Fuente 12 — `docs/12_UX_PIXELART_Y_ASSETS.md`

**Blob original:** `75e93d2371d6d6d53531fb007d0a83b94d8245df`.

## 12 — Diseño visual y producción de assets

### Dirección artística cerrada
Pixel art retro de baja resolución, tiles de 32×16 proyección oblicua 2:1, personaje de 16×24 píxeles, contorno de 1 px, hasta 24 colores por spritesheet, sin filtrado bilineal. Micelios: fungoides vivos y tecnología biofotónica. Rúnicos: cuerpos minerales con runas. Ferrinos: seres orgánicos con exoesqueleto ferruginoso, **no** robots ni corales. Siluetas deben diferenciarse claramente a 360×640 canvas lógico vertical. Para cada era la misma funcionalidad y collider en todas las naciones; solo cambian apariencia y FX.

### Sprite contract
Cada combinación `(faction, era, profession)` tiene direcciones `NE,SE,SW,NW`; acciones `idle,walk,gather,haul,build,research,celebrate,rest,react`; frames por acción, fps y naming en `data/art_spec.v2.json`. Las 13 eras x 5 profesiones x 3 facciones requieren 195 combinaciones de vestuario profesional, con reutilización de esqueletos, paletas y herramientas. 39 combinaciones de K-0 **no** son necesarias: cuerpo único más accesorios y proyecciones de época. Gobiernos: 3 candidatos x 3 facciones x 13 épocas = 117 variantes de vestuario, generadas a partir de 9 bases. Edificios básicos: 130 definiciones x 3 facciones = 390 skins con reutilización de las 10 familias y cuatro etapas.

### Cámara y HUD
Resolución lógica vertical 360×640, salida 1080×1920. Horizontal 640×360, salida 1920×1080. `nearestNeighbor=true`, objetivo 30 FPS y nunca inferir latencia del servidor desde FPS. Vertical: 14 % HUD superior, 66 % mundo, 20 % inferior; horizontal: 73 % mundo y 27 % panel lateral. HUD siempre muestra era, barra 0–100, próximos hitos, recursos esenciales, estado LIVE por nación, cuenta regresiva de votación, total de papeletas pero no opciones ocultas de RPS, y eventos de K-0 subtitulados. No mezclar identidad de canales de otras plataformas salvo política aprobada.

### Densidad de población
Vertical render objetivo máximo 45 ciudadanos, horizontal 90, LOD por FPS con prioridad `(self_if_known, recentlyActive, recentlyJoined, awarded, seededSample)`. El resto no desaparecen del sistema: se muestran agregados por oficio y sprites cosméticos NPC. No hay sprite real por ciudadano obligatoriamente; las animaciones extrapolan eventos de servidor y no alteran el estado real.

### Matriz de acceptance visual
Cada asset necesita archivo PNG con transparencia, spritesheet, JSON atlas, origen/sombra estándar, paleta, silueta comprobada en 360×640/640×360, cuatro orientaciones, 9 acciones, licencias verificadas y aprobación visual. **Estos archivos no están dibujados por esta especificación**. El diseño visual puede estar definido en texto; su calidad final y la aceptación artística no son un hecho hasta existir imágenes reales.


---

## Fuente 13 — `docs/13_ARQUITECTURA_APIS_Y_ESTADOS.md`

**Blob original:** `2a44215051735b3d3f407b9233db3ee01b1778b4`.

> **Enmienda normativa v2.3 (multistreamer distribuido):** backend .NET compartido en hosting central; tres Browser Sources en PCs diferentes, un escritor por nación, Inbox/Outbox y global SeasonArbiter. No servidores locales ni P2P. [Especificación vigente](CURRENT_SPEC.md).

## 13 — Arquitectura modular, dominio y APIs

### Despliegue de referencia
Monolito modular en .NET 10 con tres procesos lógicos `ApiHost`, `SimulationWorker` y `ConnectorWorker` (en MVP pueden ser un ejecutable con HostedServices), PostgreSQL, SignalR, React/TypeScript y Phaser (versión sujeta a prueba de OBS CEF). No usar Kafka, RabbitMQ, Redis, Kubernetes ni event sourcing completo hasta demostrarse necesidad. Inbox/Outbox PostgreSQL permite idempotencia y recuperación.

### Módulos y dependencias
`IdentityAndBindings` (asignación canal y cuentas), `Citizens` (usuarios/oficios/XP), `Simulation` (scheduler, clocks, work aggregation), `Economy` (balances/consumo/ledger), `Buildings` (autoplanner y construcción), `History` (hitos/eras), `Politics` (elección y prioridad), `StrategicCouncil` (holds/votos), `Competitions` (RPS/sanciones), `MissionEngine`, `ShowDirector`, `PlatformAdapters`, `ReadModels` y `Operator`. Cada módulo expone comandos y eventos, no acceso directo a repositorio de otro módulo. Core no importa Phaser ni SDK de plataforma. IDs UUID y referencia a `season_id + nation_id` en cualquier agregado perteneciente a nación.

### Consistencia
`Inbox` guarda el raw mínimo + `sourceKey` único; actor lógico single-writer por nación y lock de exclusividad en la DB; las operaciones compartidas de maravillas/ganador tienen transacción global y lock de temporada. `Outbox` publica evento con id estable tras commit; duplicaciones de emisión no afectan estado. Ante despliegue horizontal posterior usar lease-epoch/fencing antes de levantar otro escritor. Nunca ejecutar dos instancias con escritores sin fencing. Recursos en milésimas, oro en unidades enteras separadas.

### API y SignalR
Contratos en `contracts/openapi.v2.yaml`, `contracts/normalized_event.schema.json`, `contracts/nation_delta.schema.json`, `contracts/channel_binding.schema.json`, `contracts/ruleset.schema.json`; JSON v2 con `schemaVersion`, `eventId`, `seasonId`, `nationId`, `sequence`, UTC ISO8601. `/api/v2/operator` exige acceso privilegiado; `/api/v2/public` ofrece únicamente proyecciones. SignalR grupos `season:{id}:nation:{id}:public`, `season:{id}:operator` y `output:{id}`; no publicar IDs de proveedor ni texto raw. Clientes reconectan enviando `lastSequence`, recuperan snapshot y deltas posteriores; si hueco fuera del retention, solicitan snapshot completo.

### Contratos de error
Respuesta estándar `{code,message,correlationId,retryable}`; códigos predecibles `NOT_REGISTERED`, `PROFESSION_LOCKED`, `VOTE_NOT_OPEN`, `OUT_OF_WINDOW`, `EVENT_DUPLICATE`, `SOURCE_UNAUTHORIZED`, `BALANCE_HOLD_CONFLICT`, `GOLD_RULE_DISABLED`, `LIVE_NOT_CONFIRMED`, `CONTENT_HASH_MISMATCH`, `RULESET_INVALID`, `RUNNING_SEASON_IMMUTABLE`. Prohibido devolver secretos o payload de chat bruto.


---

## Fuente 14 — `docs/14_SEGURIDAD_PRIVACIDAD_Y_OPERACION.md`

**Blob original:** `059e2fd4675e15c336f83faed89a18a9e598725e`.

## 14 — Seguridad, privacidad, infraestructura y continuidad

### Amenazas críticas
Eventos simulados como aportaciones, abuso de chat, replay, doble aprobación de obras, cambio no autorizado de binding, spoofing de canal, privilegios de operador, inyección por displayName a TTS/LLM y pérdida del estado. Todos los accesos externos pasan por validación, autenticidad del proveedor y `sourceKey` deduplicado. Secrets en un gestor de secretos o variables inyectadas por orquestación, nunca en JSON distribuido. Tiempos UTC; firewall DB no expuesta; TLS en endpoint público; MFA para operador; red mínima entre procesos.

### Acceso y segregación
Roles `viewer`, `moderator` (silenciar nombres), `operator` (iniciar/detener/votar eventos autorizados), `owner` (modificar bindings y tasas de monetización), `auditor` (solo lectura ledger). Todas las acciones mutadoras con `idempotencyKey`, actor, razón y registro append-only. `Contributions` solo pasa a Verified desde adaptador con `capability` habilitada y prueba de autoridad; la UI del operador NO dispone de botón para crear oro real. En simulación puede inyectarse oro demo a un ledger namespace separado que jamás se fusiona con producción.

### Retención
Minimizar PII: hash estable de ID del proveedor para correlación y token cifrado en vault; displayName moderado no es clave. Retención propuesta: eventos de chat sin relevancia 7 días, raw validado de comandos 30 días, métricas agregadas 13 meses, ledger y eventos financieros según obligación legal aplicable (no fijar periodo sin asesoría jurisdiccional). Permitir anonimizar nombres públicos sin reescribir ledger. Publicación de política de privacidad y procedimiento de eliminación antes del primer directo real.

### Hosting y backups
Docker Compose local con PostgreSQL. Inicialmente una VM única EU con servicios separados por contenedor, volumen PostgreSQL y backups diarios cifrados fuera del host; respaldos de WAL/PITR si la pérdida tolerable obliga. RPO objetivo de diseño 15 min y RTO 2h, NO garantías demostradas. Cada 30 días realizar restauración simulada contra DB vacía y comparar cuentas, ledger y checksum de snapshot. Cualquier test fallido bloquea monetización. Nunca compartir tokens OBS o OAuth en repositorio.

### Despliegue y rollback
Pipeline: lint/json-schema → tests de contenido → tests del motor → migración en staging → snapshot DB → arranque versión con contrato compatible → health gates → rollout controlado. No migrar esquema mientras se procesa inbox sin compatibilidad. Para cambios de `rulesetHash` detener nueva temporada y crear ruleset nuevo; las temporadas RUNNING quedan fijadas. Feature flags por canal no deben alterar las reglas ya congeladas de una nación.

### Costes e IA
Presupuestos sólo estimables tras benchmark de CPU, nº de canales/eventos y TTS. Cada mensaje narrado puede salir por plantilla offline; LLM es opcional con límite de gasto diario y fallo seguro. La infraestructura no debe quedar funcionando 24/7 sin supervisión del operador durante la fase de pruebas monetizadas.


---

## Fuente 15 — `docs/15_PRUEBAS_Y_CIERRE_DE_DEFINICION.md`

**Blob original:** `11026e2b054ab71dbded4f0f6dde1571a4b573aa`.

## 15 — Pruebas automáticas y criterios de aceptación

### Tests contractuales necesarios
V2-T01 92 decisiones preservadas; V2-T02 tres facciones exactamente y sin atributos de ventaja; V2-T03 cualquier mezcla de tres canales válida y duplicación del mismo canal rechazada; V2-T04 13 eras con cinco profesiones; V2-T05 todas las eras 1–12 tienen 5 hitos sumando 100 y camino sin gold; V2-T06 cada era tiene al menos tres proyectos estratégicos + 10 edificios básicos; V2-T07 30 skills, elegir máximo una por tier, límite de bp; V2-T08 todas las recetas con costes enteros ≥0 y sin oro en básicos; V2-T09 golpes RPS 3 elecciones distintas empatan, primera papeleta única, cero sin espectadores no inventa votos; V2-T10 ventana !active 7200s UTC, caduca offline; V2-T11 gobierno 3600s, runoff 180s, Consejo 600s, penalización 1800s live-only; V2-T12 ningún recurso negativo ni pago duplicado; V2-T13 primera entrada a última era cierra temporada sin abrir elecciones; V2-T14 auditoría de determinismo al repetir mismo flujo y seed.

### Matriz de carga y fallos antes de LIVE
- Carga de 24 NPC, +10/100/1000/10000 activos; CPU, memoria, latencia de inbox y delta, latencia OBS, límites de sprites.
- Caída a mitad de una papeleta, reconexión Twitch sin replay, YouTube cursor caducado, eventos duplicados, origen no autenticado, segundos perdidos en `UNCERTAIN`, reinicio de DB.
- Proyecto votado y tres transacciones concurrentes (oro reversado y edificio automático): debe haber una sola deducción, sin saldos negativos.
- dos naciones compiten en completar maravilla/era final simultáneamente: exactamente un ganador en DB.
- 7 días offline con hambre y capacidad saturada: no deadlock permanente y no saltar de era si no hay LIVE.
- Restauración PITR de base de datos en entorno aislado, verificación de hashes, reconciliación de ledger; se mide RPO/RTO real.
- Políticas Twitch, TikTok y YouTube revisadas en fecha de directo para canales concretos; sin este gate monetización/simulcasting OFF.

### Criterio de '100 % definido'
El canon funcional puede considerarse cerrado cuando cada entidad y comando tenga contrato, cada output numérico tenga regla y cada transición tenga test. **Eso no equivale a producto terminado**. Siguen pendientes pruebas externas (credenciales/capacidades LIVE reales, validez legal, rendimiento de Phaser en versión CEF de OBS, sprites visualmente aprobados). Se listan en `audit/EXTERNAL_GATES.md`, no como valores `null` del ruleset.


---

## Fuente 16 — `docs/16_INTEGRACIONES_Y_CUMPLIMIENTO.md`

**Blob original:** `4eebd9d65c86247280dd7bbe4a1cdb16a21a7772`.

> **Enmienda normativa v2.3 (multistreamer distribuido):** la conexión OAuth y evidencia de cada capacidad corresponde a cada streamer/canal. Twitch/YouTube solo bajo scopes propios y TikTok no se afirma disponible; consulta 66 para onboarding, seguridad y permisos. [Especificación vigente](CURRENT_SPEC.md).

## 16 — Capacidades LIVE verificables y políticas

### Principio de proveedor intercambiable
La simulación no incluye SDKs de plataformas. `IPlatformAdapter` declara capacidades independientes `chat_read`, `stream_presence`, `message_write`, `monetary_events`, `verification`, `cursor_resume` y `identity_stability`. El operador no puede activar una función si el adaptador y la autorización de canal no demuestran ambos soporte. Ningún fallback a scraping ilegítimo. `ChannelBinding` es configuración, no garantía de acceso LIVE.

### Twitch
EventSub es at-least-once, puede repetir `message_id` y **no garantiza replay de eventos perdidos durante una desconexión total de WebSocket**; por eso inbox deduplicada, re-suscripción, health state `UNCERTAIN` y no fabricar papeletas. Documentación: https://dev.twitch.tv/docs/eventsub/ y https://dev.twitch.tv/docs/eventsub/handling-websocket-events/ . Las capacidades de bits/cheers son independientes de chat y requieren permisos adecuados, configuración y prueba. Las políticas de simulcast deben revisarse antes de mostrar mensajes de otras plataformas en una salida Twitch: https://help.twitch.tv/s/article/simulcasting-guidelines .

### YouTube
El chat LIVE se puede consultar mediante `liveChatMessages.streamList` o `list` con `nextPageToken` cuando esté disponible; no se asume historial ilimitado ni que el token resuelva todas las desconexiones. Documentación: https://developers.google.com/youtube/v3/live/docs/liveChatMessages/list . Monetización requiere visibilidad y permisos de canal, con validación por evento concreto. Un mensaje que parezca pagado no se considera verificado por texto.

### TikTok
No dar por hecho una API LIVE pública que entregue chat y regalos con acceso comercial general a cualquier cuenta. Cada conector debe mostrar evidencia documental y permisos para la cuenta concreta, o quedar en `NOT_AVAILABLE`. Queda prohibido activar créditos de oro con librerías no oficiales sin revisión de legitimidad, integridad y términos. El modo con tres cuentas TikTok es **topológicamente compatible**, no necesariamente integrable hoy sin acceso autorizado.

### Política de salida por canal
La nación se asocia a `providerChannelId`. Una salida puede mostrar la propia facción y resumen agregado de rivales, pero no mezcla automáticamente chat crudo, mensajes, avatares o llamadas a seguir otro canal. `overlayPolicyVersion` se valida según destino. Los regalos de otra cuenta no se atribuyen a la nación receptora, aunque el broadcast los vea: autoridad siempre basada en `binding` del origen.

### Checklist para habilitar canal
1. Documentación oficial vigente revisada.
2. Token con scopes mínimos por canal (cuando proceda).
3. Mensaje real leído, deduplicado y asociado a UserId estable.
4. Pérdida de conexión y reconexión manejadas sin replay fingido.
5. Mensaje de escritura, si existe, probada de forma opcional.
6. Aportación real verificada, reverso y regla de conversión aprobada, o `monetizationEnabled=false`.
7. Revisión de cumplimiento de salida y moderación.
8. Registro `CapabilityEvidence` versionado con fecha, URL y operador que lo certificó.

