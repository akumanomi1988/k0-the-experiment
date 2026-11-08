# Fuentes íntegras v2.5 — capítulos 65–67

> **Archivo de preservación de contenido completo (encabezados reindentados).** No es una segunda autoridad: la [especificación maestra](../ESPECIFICACION_MAESTRA_v2.5.md) resuelve reglas sustituidas. Los enlaces relativos del texto interno pertenecen al documento original citado; para navegar, abra ese archivo de origen.

---

## Fuente 65 — `docs/65_DISENO_STREAMER_OVERLAYS_Y_ARTE_v2.3.md`

**Blob original:** `3eb193f85efe3a38d3f47b327360b22fc8d91887`.

## 65 — Diseño de producto, experiencia del streamer, overlays y arte (v2.3)

**Normativo para las nuevas experiencias multistreamer.** Complementa 20,24–30,46–50,61–62; **no sustituye** manuales artísticos ni implica que se hayan dibujado sprites o aprobado capturas. Mismo mundo lógico; cada streamer tiene una vista y un canal propios.

### 1. Experiencias y pantallas

#### Portal del propietario
1. Nueva campaña: nombre público, idioma, zona editorial, formato de carrera y 3 naciones fijas.
2. Nueva temporada DRAFT: selección de catálogo inmutable versionado, seed, política de emisión y calendario sugerido (no obliga horarios).
3. Sala de convocatoria: tres asientos de streamer con nación, invitación, fecha expiración, rol, estado de cuenta, chat, stream_presence, overlay y conexión de prueba; propietario puede revocar antes de empezar.
4. Validación: matriz preflight con pruebas de permiso por canal y lista de riesgos; botón START desactivado sin tres fuentes válidas en PUBLIC_LIVE.
5. Cockpit RUNNING: estado de tres LiveClocks, progreso, Inbox lag, latencia, salud DB, colas, votaciones, torneos, OBS clients, streamers online, eventos, log de cambios.
6. Post-temporada: campeón, hashes, ledger auditable, historial de narración, recuperación y exportación permitida.

#### Portal del streamer invitado
1. Invitación por enlace one-use de 24h, nombre de campaña/nación, descripción clara de permiso y alcance; requiere autenticación K0.
2. Enlazar cuenta del proveedor **que controla**. Solicitar scopes mínimos; mostrar pantalla de privacidad y estado; negarse a fingir conexión si falta API.
3. Probar capacidad de chat con mensaje de diagnóstico y confirmación de fuente; test de stream_presence separado de OBS; monetización siempre desactivada salvo habilitación expresa posterior.
4. Elegir overlay vertical (360×640 lógico) u horizontal (640×360 lógico); preview, copiar URL read-only, regenerar clave y abrir test seguro con datos SIMULATED.
5. Copiar a OBS Browser Source (solo URL) y ajustar resolución real a 1080×1920 o 1920×1080; indicación de que la fuente web es solo visual y la partida seguirá aunque OBS se reinicie.
6. Durante LIVE: ver mi nación, estado global, comando actual, próxima escena, errores de proveedor, notificaciones moderadas y estado real del overlay.
7. Desconexión: mostrar dónde falló (OBS, navegador, chat, credencial, stream) con acciones de reintento que no modifiquen la simulación.

#### Espectador del canal A/B/C
- Ve primordialmente su nación; siempre identifica facción, era, progreso, evento actual, estado LIVE real y comandos válidos.
- Nunca se le exige visitar otra plataforma para participar; el chat del canal determina automáticamente nación.
- Puede ver resumen público de rivales sin mostrar chat crudo, nombres no consentidos, avatares o métricas privadas de esos canales.
- Inicio: explicación breve de !join, !work <oficio>, !active; durante eventos, opciones y duración; respuestas a comandos por canal si message_write autorizado, y siempre acuse visible en overlay cuando proceda.
- Permite mirar sin chat ni audio y comprender el estado. Los mensajes de K-0 están subtitulados.

### 2. Sistemas de vistas, escenas y transiciones

Cada BroadcastOutput tiene outputId, allowedNationIds, primaryNationId (si NATION_FOCUS), layoutMode, locale, moderationPolicyVersion, overlayPolicyVersion y outputRevision.

Modos aprobados:
- NATION_FOCUS: vista de una nación + resúmenes públicos y evento global; default del streamer.
- SHARED_WORLD: montaje de las tres naciones, para propietario o distribución autorizada; no agrega control del chat ni redistribuye mensajes crudos.
- EVENT_STAGE: marcador RPS/batalla de las tres, sin datos privados.
- SAFE_SCENE: escena informativa durante problema técnico.

Escenas canónicas heredadas: BOOT_CHECK, WORLD, GOV_VOTE, PRIORITY_VOTE, COUNCIL_VOTE, TOURNAMENT, ERA_TRANSITION, SEASON_END, más CONNECTING, CHANNEL_REVOKED, MULTISTREAMER_WAITING, GLOBAL_EVENT_PAUSED y RECOVERING.

**Regla:** las escenas visuales no alteran reglas ni relojes. Una nación puede seguir produciendo mientras su overlay está en SAFE_SCENE. Un evento compartido se representa en los tres equipos con el mismo eventId/resultado, pero puede iniciar animación con pequeña variación de latencia. No se sincroniza nada con captura de pantalla de OBS ni audio local.

### 3. Pixel art y sistema de arte

- Pixel art retro 2D de baja resolución, proyección oblicua de suelo **2:1**, tiles lógicos **32×16**, sprites de ciudadano **16×24** como unidad inicial de contrato. Pivote inferior centrado, sombras discretas, escalado entero, texturas sin suavizado.
- Micelios, Rúnicos y Ferrinos son culturas claramente distintas en silueta, lenguaje material y paleta; **mismas estadísticas** de partida, el bioma es cosmético.
- Doctor K-0 es cyborg visualmente inequívoco y neutral, legible a tamaño pequeño; evita figura genérica de médico humano. Animaciones cortas de 2D recortado y ciclos sencillos (idle, gesto, aviso, ceremonia) antes de invertir en 3D.
- Los oficios son cinco familias mecánicas fijas; nombres, instrumentos y ropa evolucionan por era sin cambiar IDs, XP ni perks.
- Edificios: 10 familias × 13 eras de catálogo, 4 etapas visuales de construcción heredadas; 39 proyectos y 13 maravillas. Para prototipo dibujar un subconjunto comprobable y mantener placeholders etiquetados, nunca anunciar 130 sprites aprobados.
- Era 13 INTERSTELLAR es epílogo visual y no economía jugable. Sus assets no son bloqueo para el primer vertical slice.
- 39 tipos de unidad de combate son definiciones por era/rol con 3 skins por especie; para prototipo de batalla usar figuras legibles con animación teatral, no simulación gráfica de impacto autoritativa.
- Mantener un inventario de assets con artId, factionId, eraId, resolution, pivot, animationFrames, frameRate, license, author, status (BRIEF/DRAFT/REVIEWED/APPROVED), revisión, dependencias y hashes. Ningún asset marcado APPROVED sin captura en OBS.

### 4. Layout y responsive

**Vertical 360×640 lógico:**
- x0 y0 w360 h90: estado de nación/era/progreso y conexión LIVE.
- x0 y90 w360 h422: mundo pixel art, ruta/cámara; máximo sugerido 45 ciudadanos visibles con LOD.
- x0 y512 w360 h128: recursos, misión, eventos/comandos.
- K-0 subtitulado x16 y410 w328 h86 como capa contextual; no tapa votación ni ganador.
- Safe areas por plataforma deben verificarse con capturas nativas, no confiar en un número teórico común.

**Horizontal 640×360 lógico:**
- x0 y0 w467 h360 mundo.
- x467 y0 w173 h360 HUD.
- Subtítulos K-0 x20 y284 w425 h52.
- Máximo sugerido 90 sprites visibles. Ni el ratio ni los tamaños de fuente se interpretan como píxeles físicos; la fuente debe leerse a escala de móvil.

Cada output mantiene campos accesibles: broadcasterAlias moderado, factionName, era, statusText, liveClockState, remainingLiveSeconds, lastConfirmedAtUtc y connectionState. LIVE no debe mostrarse si solo está conectado el Browser Source pero falta stream_presence.

### 5. Reglas de interacción y anti-confusión

- Una persona que entra en Twitch B no debe creer que el comando dirige la nación de Twitch A; mostrar de forma persistente canal asociado y la facción.
- Comandos existentes !join, !work, !active, !gov, !priority, !build, !rps, !skill. No crear comandos nuevos del stream principal sin contrato.
- Voto en RPS no revela distribución por opción antes de cierre; en elecciones/Consejo se pueden mostrar barras autorizadas. Una papeleta no puede aparecer aceptada si Inbox no confirmó.
- Voto pausado muestra segundos LIVE congelados, banner «esperando confirmación de transmisión» y origen afectado sin exponer datos sensibles.
- Si un streamer abandona la temporada, se mantiene nación e historial, entra política de reasignación de asiento/binding auditada; no transfiere usuarios a otro canal silenciosamente.
- No conceder notoriedad visual competitiva por donaciones; patrocinio cosmético sin efectos y con consentimiento/moderación.

### 6. Sonido, K-0 y transmisión cruzada

- Guion y cues de K-0 son producidos por servidor tras eventos confirmados; texto y subtítulos se envían como datos.
- El audio de K-0 es configurable por output para impedir el eco o doble TTS si el streamer ya usa una mezcla externa. No publicar audio/captura del streamer A en B sin autorización explícita y revisión de política.
- Cada salida OBS elige niveles audio y fuente local; nunca se extrae audio remoto como parte de la autoridad de juego. Si TTS no funciona, subtítulos obligatorios y flujo normal.
- Versionar pistas, licencias comerciales, idioma y variantes. La música no debe enmascarar resultado ni dar ventaja de información a un canal.

### 7. Prueba de arte y aceptación UX

- UX-M01: tres streamers sin ayuda configuran URL OBS desde tres PCs y entienden su propia nación.
- UX-M02: 0 espectadores y 45 sprites visibles en vertical a 30 FPS reales, con subtítulos, sin tapar los cinco hitos.
- UX-M03: A pierde overlay; B/C continúan y A regresa sin recibir escenas antiguas como actuales.
- UX-M04: dos espectadores de canales distintos reciben instrucciones y agradecimientos exclusivamente en su canal.
- UX-M05: jugadores entienden diferencia OFFLINE vs OBS_DISCONNECTED vs RPS_GLOBAL_PAUSED.
- ART-M01: siluetas de 3 facciones identificables en monocromo y 1×; K-0 reconociblemente cyborg.
- ART-M02: 3 style frames (Paleolítico, Industrial, Espacial) x 3 culturas, contrastados en 360×640 y 640×360.
- ART-M03: 4 orientaciones y 9 acciones del contrato original solo se aprueban cuando estén dibujadas, animadas y comprobadas, no por describirlas.

### 8. Orden de producción con máximo ROI

1. Wireframes reales de sala de campaña, invitación, conexión de proveedor, streamer portal y cockpit OWNER.
2. Una escena vertical/horizontal con Micelios, Rúnicos y Ferrinos + K-0 cyborg, HUD y estado de conexión.
3. Sprite sheet mínimo de 5 profesiones y 10 familias básicas de Paleolítico.
4. Una elección, un Consejo y una transición, con escenas y subtítulos en los tres outputs.
5. Biblioteca de tiles/animaciones y skins por era restante después de validar lectura y desempeño de audiencia.


---

## Fuente 66 — `docs/66_INTEGRACIONES_SEGURIDAD_Y_OPERACION_v2.3.md`

**Blob original:** `1a2a860d4bee66288d23aed2d9d83da3e43d0f8e`.

## 66 — Integraciones LIVE, seguridad, despliegue y operación multistreamer (v2.3)

**Normativo para desarrollo, proveedor pendiente de pruebas.** Esta especificación completa docs 14,16,31,32,53,54 y 59. Consulta documental oficial a 2026-11-08; no constituye autorización concedida a cuentas reales.

### 1. Integraciones por capacidades, no por promesa de plataforma

Cada cuenta de streamer tiene permiso/configuración independiente para: CHAT_READ, LIVE_PRESENCE, CHAT_WRITE, EVENTS_MONETARY, EVENTS_REVERSAL, CURSOR_RESUME, ACCOUNT_IDENTITY, OUTPUT_DISTRIBUTION_POLICY. Cada capacidad tiene estado DISABLED, PENDING_VERIFICATION, VERIFIED, REVOKED o NOT_AVAILABLE, con evidencia URL, scopes, fecha, accountId y operator.

| Proveedor | Chat y presencia | Modo de implementación | Regla de activación |
|---|---|---|---|
| Twitch | EventSub para channel.chat.message y stream online/offline según autorización | Webhook público firmado recibido en servidor; reintentos deduplicados en Inbox | Scopes y prueba por cada cuenta de los tres streamers, más límites de cuota |
| YouTube | LiveChatMessages.streamList o list con cursores/cadencia documentada | Worker backend server-to-server con reconexión y límite de cuotas | OAuth del propietario; comprobar broadcast/liveChatId y acceso real |
| TikTok | Capacidad de API LIVE chat/regalos **NO asumida** | Solo un adaptador con autorización documentada y permiso explícito para cada cuenta | DESHABILITADO hasta proveedor/account evidence; no scraping no oficial |
| Local simulator | Chat/presencia/inputs sintéticos | Tres bindings simulados y evidencia de origen SIMULATED | Solo local/test; monetización real imposible |

Fuentes normativas externas para consultar antes de cada integración:
- Twitch: https://dev.twitch.tv/docs/eventsub/eventsub-subscription-types/ ; https://dev.twitch.tv/docs/chat/authenticating/ ; https://dev.twitch.tv/docs/eventsub/handling-webhook-events/
- YouTube: https://developers.google.com/youtube/data/live/reference/rest/v3/liveChatMessages/streamList ; https://developers.google.com/youtube/data/live/reference/rest/v3/liveChatMessages/list
- TikTok: https://developers.tiktok.com/ y documentación/contrato otorgado a la cuenta concreta cuando exista. Este documento no certifica un endpoint LIVE.
- Políticas de retransmisión cruzada, atribución, retención y monetización se revisan el día de despliegue por plataforma y cuenta.

**No hay fallback clandestino:** fallo de OAuth/permisos/cursor → capability deshabilitada, no lectura por cookies ni reenvío de chat entre cuentas.

### 2. OAuth, invitaciones y roles

Portal K0 usa OIDC propio o proveedor de identidad verificado, auth code + PKCE; OWNER y OPERATOR con MFA. Cada streamer vincula **su cuenta**, concede los scopes mínimos y ve claramente qué se lee/publica. Tokens OAuth y refresh tokens:
- Cifrado en reposo por KMS/KeyVault o equivalente, claves rotadas, segregados por conexión.
- Nunca al navegador OBS ni al frontend del propietario, no en URL, audit export o error.
- Revocación manual y automática; deshabilitar una sola cuenta sin detener las restantes.
- Callback OAuth valida state, PKCE, nonce/issuer y session usuario; asociación comprobada del canal real a identidad conectada.
- La invitación caduca en 24h, hash de token almacenado, single-use transaccional, scope exacto campaign+season+nation+role; el propietario puede revocar.
- Separación de permisos: BROADCASTER no cambia semillas, reglas, importes ni ganador; MODERATOR no puede operar contabilidad; OPERATOR no puede autorizar monetización por sí solo.

### 3. Overlay por streamer sin software local

El mínimo cliente es OBS Browser Source HTTPS. URL de setup contiene solo identificador público y **secreto revocable de lectura**; preferible fragmento de URL para que no aparezca en logs HTTP, con posterior intercambio por sesión read-only de corta duración. El secreto es un credential: no enviarlo por capturas/chat, guardarlo hasheado en backend y permitir rotación inmediata. No insertar refresh token de proveedores en OBS; no abrir puertos entrantes en equipos de streamer. La pantalla renderizada se suscribe con su outputId y allowedNationIds; heartbeat de overlay SOLO indica conexión visual.

Seguridad de cliente: CSP cerrada para scripts/medios autorizados, SRI cuando corresponda, HTTPS/WSS, anti-clickjacking del panel, rate limits en intercambio de token, expiración/rotación, no mezclar capacidades de operador con vistas públicas. Si secret overlay se filtra: revocar y emitir URL nueva; no afecta cuentas o estado lógico.

### 4. Privacidad y redifusión

- Los IDs reales de proveedor no salen de backend en proyecciones públicas. Pseudónimos moderados y consentimiento por contexto; evitar mezclar nombres/chat de plataformas diferentes.
- No publicar mensajes crudos, donaciones, perfiles o avatares de canal B en canal A por defecto. Resúmenes competitivos agregados pueden mostrarse según política verificada.
- Minimización de Inbox: payload/metadata estrictamente necesarios, política de expiración y borrado; retención real debe documentarse con justificación legal y jurisdicción antes de LIVE.
- Derechos de acceso/borrado, portabilidad cuando aplique, menores, moderación, registro del consentimiento de homenajes, y encargados del tratamiento: gate jurídico, no «resuelto» automáticamente.
- Establecer acuerdos del operador/campaña para límites de moderación, responsabilidad de contenidos y contacto de incidentes. No almacenar datos bancarios del espectador.

### 5. Estado de salud y runbook por tres emisores

Preflight antes de iniciar PUBLIC_LIVE:
1. Tres streamers aceptaron asiento (o owner en modo solo), tres bindings únicos, una fuente de reloj LIVE autorizada por nación.
2. Verificación de scopes y auth por canal; lectura de mensaje real y providerUserId estable; prueba de stream_presence independiente.
3. OBS Browser Source en cada PC: 360×640 o 640×360 lógico, FPS en hardware real, reconexión y validación de snapshot.
4. DB backups/restore ensayados, un solo writer, hash manifiesto, seed, reloj servidor UTC, logs/alertas y dashboard OPERATIONS.
5. Moderación, subtítulos, fallback sin voz y safe scene; vínculos de chat no cruzados; política vigente de distribución de proveedor.
6. Simulación con tres fuentes sintéticas y fallos de red controlados; nunca conceder oro con gifts sintéticos en PUBLIC_LIVE.

Durante:
- Panel único muestra por nación: chat ingress latency, message lag, source LIVE TTL, OBS connected, economy clock, vote countdown, building backlog, resource shortages y lastConfirmedAt.
- Alarmas por fuente: pérdida de chat/health, permisos revocados, caducidad token, provider 429/quota, Inbox > umbral, Outbox backlog, latencia overlay y DB lease.
- Eventos programados requieren tres LIVE confirmados; si falla uno se congelan y aparecen mensajes en los tres overlays; un operador puede cancelar sin penalización y emitir resumen de incidente.
- Ante caída de host/DB, activar RECOVERY_REQUIRED; mostrar último estado confirmado marcado con hora, no continuaciones ficticias.

Post:
- Cerrar emisión y archivar health/evidencias; ejecutar conciliación de ledger e Inbox, snapshot y backup; medir RPO/RTO real en restauración de ensayo; preparar próximo bloque LIVE sin editar reglas de temporada.

### 6. Despliegue base

Recomendación de referencia: API ASP.NET Core .NET 10 y worker de simulación central con PostgreSQL 16+ gestionada, reverse proxy HTTPS, secrets manager, logs estructurados, métricas, trazas y backup automatizado en región elegida. Frontend overlay estático con React/TypeScript + Phaser probado específicamente con versión de OBS CEF del hardware de destino. Conexión internet saliente normal en PCs de streamers. No P2P ni NAT traversal.

- Hosting mínimo: un entorno STAGING que replica conexiones simuladas, un entorno PROD con secretos/DB separados. Despliegue inmoviliza engineVersion y manifests de temporadas RUNNING; rollback sin cambiar hash.
- No confiar en reloj local de cada PC: servidor calcula UTC y segundos LIVE mediante provider health autenticado.
- No desplegar Redis, Kafka, RabbitMQ, Kubernetes ni servidor de juego dedicado por streamer inicialmente.
- Ingress multi-proveedor puede escalar a procesos separables sin mover la autoridad del motor ni los datos.
- Backups cifrados y restauración programada; hasta pruebas no se anuncian RPO/RTO numéricos como realizados.

### 7. Presupuesto, costes y SaaS futuro

Costes por unidad: horas de worker .NET, Postgres almacenamiento/IOPS/backups, WebSockets/egress por output, llamadas/quotas de cada proveedor, TTS/LLM si habilitado, producción pixel art, moderación y operación. Registrar campaignId/seasonId, hourly operational cost, input_events_count, connection hours y TTS chars para coste por partida y streamer. No confundir «tres streamers» con tres servicios backend. Una instancia central multiplica coste por campañas concurrentes y eventos, no por hardware de cada PC.

Fase piloto: un dueño de campaña y tres streamers autorizados. SaaS/licencias a otros creadores solo después de medir demanda, retención, costes y gobernanza multi-tenant; entonces añadir billing, límites por plan, izolación empresarial y soporte contractual. No realizar modificaciones de arquitectura de alto coste por hipótesis de ventas.

### 8. Monetización y seguridad financiera

Todos los tipos reales de aportación están DISABLED al principio. Si alguna cuenta verifica eventos económicos:
- Creditar oro **solo** tras autenticación, identificador único, regla de conversión específica aprobada, estado final permitido y ledger transaccional.
- La reversión puede generar GoldDebt separado; no editar asiento histórico.
- Ningún streamer puede introducir manualmente oro verificable, comprar votos, acelerar investigación, atacar por pago o transferir ganancias.
- Escena de agradecimiento es cosmética; consentimiento explícito y moderación, jamás ventaja de nación.
- Verificar políticas por proveedor, jurisdicción, fiscalidad y reembolsos. No publicitar monetización antes de esas pruebas.

### 9. Pruebas de seguridad y operación

SEC-M01 invitación caducada/usada doble rechazada; SEC-M02 token de streamer A no puede leer conexiones/credenciales B; SEC-M03 overlay A no puede invocar mutaciones ni ver PII B; SEC-M04 OAuth revocado deshabilita chat/presence reales; SEC-M05 replay de webhook y race con binding revision no duplica comandos; SEC-M06 cross-platform raw chat censurado por defecto; SEC-M07 nombres/chat con prompt injection no controlan K-0; SEC-M08 un único winner frente a competencia concurrente; OPS-M01 reconexión de tres PCs; OPS-M02 fallo de backend; OPS-M03 un streamer termina antes y los otros siguen; OPS-M04 RPS global se congela; OPS-M05 restore backup coincide con snapshot hash.

**Resultado de esas pruebas hoy: NOT_RUN.** Falta evidenciar soporte y permisos específicos para cada cuenta real antes de una prueba pública.


---

## Fuente 67 — `docs/67_BLUEPRINT_IMPLEMENTACION_Y_PRUEBAS_v2.3.md`

**Blob original:** `b4eec239b7200a4ed2a32f05cf20b743c080de96`.

## 67 — Blueprint de implementación, entregas y matriz de verificación (v2.3)

**Normativo para planificación de desarrollo; estados de tests NOT_RUN.** Describe cómo desarrollar todo el producto sin inventar evidencias. Complementa docs 15,38,40,57,60 y auditoría C-01 a C-18.

### 1. Producto objetivo y límites

Producto de referencia: 3 naciones (Micelios, Rúnicos, Ferrinos), 13 eras (1–12 jugables, 13 epílogo), 5 profesiones, NPC que completan ruta gratuita, 130 edificios básicos, 39 proyectos, 13 maravillas, 39 definiciones de unidad/rol/era, gobiernos/equipo político, RPS y combate programado, Doctor K-0, mapas persistentes pixel art y economía no pay-to-win. Tres streamers reales en tres PCs distintos y tres fuentes de chat válidas, mezclables entre proveedores autorizados. Una temporada puede continuar con horarios LIVE distintos; torneos exigen tres LIVE simultáneos.

No se pretende construir de golpe: la evidencia de cierre se acumula por gates y módulos; no se prometen APIs que un proveedor no ofrezca.

### 2. Stack congelado para prototipo

- .NET 10 / C#: monolito modular con API ASP.NET Core y BackgroundService worker. Separar ensamblados Domain, Application, Infrastructure, Api, Simulation y Contracts con interfaces claras, sin reflejar capas por cada entidad si no aportan valor.
- PostgreSQL 16+: migraciones reproducibles desde DB vacía, transacciones ACID, versión optimista y advisory/row locks; nunca SQLite como DB real.
- React + TypeScript + Phaser (versión compatible con OBS CEF que supere prueba) para overlay, panel propietario y portal del streamer. SignalR como transporte.
- JSON Schema/OpenAPI generados/validados en CI, DTO .NET tipados; contratos versionados y hash de contenido.
- Integración de Twitch EventSub / YouTube oficial desde backend; TikTok bloqueado hasta contrato y prueba. Local adapter sintético para desarrollo y tests.
- Tests xUnit o equivalente, Testcontainers PostgreSQL para integración, browser tests Playwright y OBS hardware test manual reproducible.
- Sin servicios de pago, TTS obligatorio, Redis, Kafka, Kubernetes ni multi-tenant SaaS en primera entrega.

### 3. Estructura de repositorio objetivo

    /src/K0.Domain                         # invariantes, estados, relojes, recursos
    /src/K0.Application                    # commands/queries, casos de uso, permisos
    /src/K0.Infrastructure                 # PostgreSQL, inbox, outbox, provider auth
    /src/K0.Simulation                     # segmentador, economy tick, RNG, arbitraje
    /src/K0.Api                            # REST, OIDC, SignalR, health
    /src/K0.ConnectorWorker                # adaptadores LIVE y polling/webhooks
    /web/overlay                           # Phaser/React escenas streamers
    /web/portal                            # invitaciones, propietario, operator
    /contracts                             # OpenAPI y schemas generados
    /data                                  # content manifests y reglas versionadas
    /architecture                          # migraciones versionadas; scripts 001/002/003 son históricos de DISEÑO
    /test/K0.UnitTests
    /test/K0.IntegrationTests
    /test/K0.SimulationTests
    /test/K0.ContractTests
    /test/K0.BrowserTests
    /docs                                  # specs y ADR
    /.github/workflows                    # CI build/test/contract/format

El manifiesto congelable de entradas está en [data/content_manifest.v2.3.json](../data/content_manifest.v2.3.json). Sus hashes se computan en el build, no se fingen en documentos.

Un cambio de juego empieza en contrato/manifest/test; lógica y UI solo consumen esas fuentes. No duplicar umbrales a mano entre servidor, TS y JSON.

### 4. Modelo y algoritmos mínimos de producción

- Asignación: Campaign→Season→3 Nation + StreamerSeats→ProviderConnection→ChannelBindings→ProviderLiveSession→BroadcastOutputs.
- Inbox: guardar sourceKey único con transacción; validar firma, timestamp, binding y rol; normalizar; secuencia de ingesta; event outbox tras commit. At-least-once en transporte, exactamente una mutación por clave/cause.
- SimulationClock: relojes tipados, partición de segmento a fronteras, deltas de 5s, enteros milésimas/bp con restos persistentes y RNG counters por dominio/nación.
- Economy: población NPC/humana efectiva por profesión y era, hambre, almacenes, reserva/consumo, autoplanner, XP, tecnologías, hitos, era/misión.
- Governance: votaciones OPEN/PAUSED/RESOLVED, deadline LiveClock, empates RNG reproducible, prioridad, único Consejo/nación/era, cobro atómico de vector hold del ganador.
- Competition: RPS y batalla automática programados, ThreeNationLiveGate y CompetitionLiveClock; sin pago y sin sanción por caída de proveedor.
- SeasonArbiter: SeasonSequence global serializable; único ganador interestelar, exclusividad global de maravillas y frozen post-season.
- Views: snapshots con versions/hash, deltas contiguos y presentación desacoplada. Un overlay conectado nunca es origen de comandos financieros.
- Security: membresías, OAuth, minimización de datos, scopes, revocación por canal/output, auditoría; provider token server-only.

### 5. Migración de esquema necesaria

Los SQL 001 (base), 002 (ejércitos/patrocinio) y 003 (multistreamer) documentan **intención**, no constituyen una cadena de migraciones ya ejecutada. Para implementación:
1. Convertirlos en migrations numeradas nuevas y autocontenidas; revisar type/FK de NationId, FactionId y estados; evitar asumir columna/constraint names sin ejecutar.
2. Integrar PAUSED para votes, estados batalla y licencias/streamer; extender resource_ledger con COSMETIC_SPEND sin permitir BUILD_COST de oro legado.
3. Agregar CampaignMembership, StreamerSeat, ProviderConnection, ProviderLiveSession, BroadcastOutput, OutputSession, PresentationCue, AuthorityAudit y limits de UNIQUE.
4. Probar el conjunto en PostgreSQL real: levantar vacío, seed de 3 naciones, rollback en DB de test, constraints y locks; realizar restore/snapshot con recursos.
5. Separar schema de dominio de proyecciones; SQL no se deriva de la posición de sprites.

### 6. Orden de entrega con artefactos y aceptación

| Fase | Entregable verificable | Criterio de salida |
|---|---|---|
| **P0 — Contratos** | CURRENT_SPEC, validadores JSON y contratos TS/C#, migraciones reales, CI, matrices C-01–C-18 | Cero referencias huérfanas/ciclos de progreso; tests en verde |
| **P1 — Simulación** | 3 naciones en memoria + PostgreSQL, 24 NPC cada una, 5 oficios, Paleolítico y todos sus hitos | 0 chat/0 oro completa primera era bajo LIVE sintético |
| **P2 — Experiencia** | Overlays 360×640/640×360, K-0 textual, portales, escenas, Consejo/elecciones | 3 Browser Sources sincronizados por evento y reconnect |
| **P3 — Remoto** | Invitación, OAuth de K0, roles, 3 streamers de 3 redes, tres bindings simulados | OBS de uno cae sin modificar economía/torneo ajeno |
| **P4 — Contenido** | Eras 2–12, arte modular, 130 básicos, proyectos, maravillas, batallas, políticas | Simulación íntegra 12 eras, sin deadlock, hash reproducible |
| **P5 — Proveedores** | Twitch/YouTube (los que demuestren permisos), LIVE health, reconexión, cuota, uso cruzado | 3 canales reales y cuentas autorizadas, failover ensayado |
| **P6 — Lanzamiento** | QA arte/accesibilidad, 30 FPS OBS, privacidad/licencias, backups/alertas, balance y costes | D4/public gate con evidencias, no checklist teórico |
| **P7 — SaaS eventual** | Campañas de terceros, billing, aislamiento multi-tenant, SDK/adaptadores | Solo después de validación de retención y ROI |

**P1/P2 son desarrollo incremental**, no garantía de que K0 completo esté validado; D2 de temporada completa y D4 siguen siendo distintos.

### 7. Auditoría C-01–C-18: estado de remediación

| ID | Decisión normativa v2.3 | Trabajo pendiente |
|---|---|---|
| C-01 | Orden canónico doc 64 | Test frontera y cambiar docs 03/42/SQL |
| C-02 | Un solo economyDelta offline 0.2 | Quitar doble factor de código y XP, test 60s |
| C-03 | Hitos son autoridad de tech | Flags de tecnologías v2.3 ya alineados en JSON; generar desde referencias en build y probar |
| C-04 | Votes PAUSED | DDL de diseño 001 ya admite PAUSED; falta migración SQL real y test |
| C-05 | ACK rápido, economía cada 5s | SLO separado y prueba de latencia |
| C-06 | Un Consejo por era/nación | Catálogo/reglas y docs 05/08/44 alineados; falta scheduler y rechazo al repetir |
| C-07 | NationId UUID, FactionId slug | JSON Schema/OpenAPI actualizados; falta DTO C#/TS generado y prueba real |
| C-08 | CompetitionLiveClock global | Docs 03/09/42/64 y SQL003 de diseño; falta motor y desconexión real |
| C-09 | Proyectos y maravillas gratuitos | Trace histórica y tests zero-gold |
| C-10 | Interestelar epílogo | Flags de catálogo v2.3 y docs 34/35/36; falta bloquear runtime tras terminal |
| C-11 | EraMission propia | 12 misiones, hitos y doc 36 ya generados; falta scheduler y test dos eras mismo día |
| C-12 | Balance humano candidato, cap por profesión | Alcance explícito en ruleset/docs; falta simulación por perfiles y calibración |
| C-13 | Texto viejo sobre oro inválido | candidatePool y docs 05/44 ya alineados; extender limpieza de archivos legados y ejecutar CI |
| C-14 | SQL 001/002/003 no migrado | Migrations y test transaccional |
| C-15 | Constructor XP ocioso | Instrumentación y ajuste tras simulación |
| C-16 | IMPLEMENTATION_BASELINE engañoso | Status del ruleset corregido a candidato; ningún test de implementación se presume |
| C-17 | Tres canales distintos | Pruebas de proveedor y modo simulado |
| C-18 | Gate de prototipo ≠ gate público | Gates separados y evidencias |

Las decisiones de diseño quedan explícitas; **no marcar como corrección IMPLEMENTED** hasta que se modifiquen catálogos y código y pase su prueba. Los hallazgos y los gates están en [audit/](../audit/).

**Actualización de catálogos (2026-11-08):** doc 36 regenerado desde datos; tecnologías, hitos, misiones por era, eras, proyectos, ruleset y schemas v2.3 editados en GitHub; validador estático y workflow añadidos. Los cambios documentales no constituyen implementación, balance probado ni CI ejecutada.

### 8. Matriz de pruebas concretas

| Suite | Casos |
|---|---|
| CONTRACT | schema JSON + OpenAPI + SQL compilan y no divergen, IDs único, tech/milestone lookup, 5 hitos×12 eras, oro estratégico cero, era 13 terminal |
| SIM | 0/10/100/1000/10000 humanos, 24 NPC, 3 seeds, distribuciones equilibradas/sesgadas, horarios LIVE 0/1/4/24h, periodos UTC cambiantes, >7d outage |
| DETERMINISM | misma seed + ruleset/content hash + segmentos + entrada canónica generan mismo stateHash y winner; tick 5s vs particiones compatibles |
| VOTES | exactamente deadline, pausa, reintento, cambio de voto válido, salida LIVE, noVotes/tie, Council hold y un solo cobro |
| COMPETITION | 3 transmisiones LIVE, pérdida de una, reanudación/cancelación, ciclo RPS 2-2-2, empates y penalizaciones no acumuladas |
| MS | broadcastMode MULTI_STREAMER con 3 cuentas K0 primarias diferentes; mismo proveedor, proveedores mixtos con capacidad, otros PCs/redes, invitados expirados, permisos, token revocado, reconnect OBS |
| SECURITY | OAuth PKCE, firmas webhook, PII redaction, prompt injection en nombre, accesos cruzados y secretos, CSRF/CSP, rate limits |
| OPS | rollback, restart, restore real DB, doble worker/fencing, outbox duplicado, alerta de stream y OBS, capacidad real con 30 FPS |

Cada prueba PASS exige commit, entorno, versión de catálogo, datos/seed/entradas, resultado, timestamp y evidencia. Mientras falte, estado NOT_RUN. Suite de balance debe publicar P10/P50/P90 para duración por era y por perfil; evitar afirmar «2,5 días por era» como hecho.

### 9. Gates externos y definición del producto

No se puede escribir en GitHub una licencia de marca, permiso LIVE, desempeño de hardware, consentimiento real ni resultado de una simulación que todavía no existe. Mantener estas dependencias rastreables: proveedor/cuenta, legal/privacidad, arte/licencias, infraestructura/backup, rendimiento OBS, economía completa, costes reales y experimento con usuarios. Cada gate lleva responsable, evidencia, fecha, URL/documento y estado; ningún gate se cierra con prosa.

### 10. Condición para decir «especificación definitiva»

Una especificación documental se puede declarar **congelada para desarrollar** cuando (a) no hay normas contradictorias, (b) todos los catálogos y contratos generan/verifican referencias, (c) casos funcionales tienen entradas/salidas y (d) el owner acepta el alcance. No equivale a «juego completo» ni a soporte LIVE certificado.

**Estado de este commit:** diseño multistreamer propuesto en v2.3 y plan de ejecución definido; implementación y evidencias aún pendientes. El trabajo que sigue debe ser software, pruebas y arte real, no expansión narrativa indefinida.

