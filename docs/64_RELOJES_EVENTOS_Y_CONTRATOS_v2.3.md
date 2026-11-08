# 64 — Contratos de reloj, sincronización y API multistreamer (v2.3)

**Normativo para nuevos componentes y corrección de docs 03,19,42,55.** Contratos de referencia, aún no compilados ni validados contra código. Ninguna marca de tiempo aportada por el cliente OBS es autoridad.

## 1. Relojes y semántica

| Reloj | Avance | Uso |
|---|---|---|
| UTC | Tiempo físico confiable | Expiración de ciudadanía, OAuth, periodos de misión, timestamp |
| NationLiveClock[n] | Incrementa solo con proveedor de nación n en LIVE_CONFIRMED | Elección, prioridad, Consejo y ceremonia de transición |
| NationEconomyClock[n] | 1 s/s LIVE, 0.2 s/s OFFLINE o UNCERTAIN | Producción, comida, obra, conocimiento, XP |
| CompetitionLiveClock[event] | 1 s/s solo cuando **los tres** LIVE_CONFIRMED y evento RUNNING | RPS, descansos y batallas programadas |
| SeasonSequence | Contador global persistido en commit | Arbitraje de maravilla/ganador y publicación |
| PresentationClock | Animación en clientes | Sin decisiones lógicas, reiniciable |

OFFLINE y UNCERTAIN no otorgan tiempo de voto ni progreso de competición; para economía ambos aplican perfil conservador 0.2. El periodo UTC de misión no es live ni economy. Dos viewers de la misma nación nunca suman LIVE por estar ambos conectados.

## 2. Orden canónico y partición exacta

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

## 3. Estados de sesión

- Season: DRAFT→PREPARED→RUNNING→COMPLETED→ARCHIVED, con PAUSED/RECOVERY_REQUIRED/ABORTED por gestión; COMPLETE no vuelve a RUNNING.
- Binding: INVITED→PENDING_AUTH→AUTHORIZED→HEALTHY, con DEGRADED / REVOKED / DISABLED; no se etiqueta HEALTHY sin prueba real.
- ProviderLive: OFFLINE_CONFIRMED, LIVE_CONFIRMED, UNCERTAIN. Estado separado de OBS_CONNECTED / OBS_DISCONNECTED.
- Vote: QUEUED, OPEN, PAUSED, RESOLVED, CANCELLED, PAYMENT_BLOCKED. PAUSED no pierde ballot ni elapsedLiveSeconds; un cierre terminal se aplica UNA vez.
- Competition: SCHEDULED→WAITING_FOR_ALL_LIVE→RUNNING→PAUSED→RUNNING/ CANCELLED→RESOLVED. Pause congela CompetitionLiveClock para todas las naciones.
- Overlay: CONNECTING→SYNCING→LIVE_VIEW→STALE/RECONNECTING→SYNCING; tras TTL sin fuente válida muestra SAFE_SCENE, nunca inventa un ganador.
- Contribution: todo desactivado de inicio; RECEIVED→AUTHENTICATED→VERIFIED→CREDITED/REJECTED→REVERSED, solo evidencias y reversos autorizados.

**Elección terminada y era final misma ventana:** el cierre político válido se confirma antes de la transición si su límite LIVE se alcanza primero o en ese mismo subsegmento; después de SeasonCompleted no puede abrirse un voto nuevo. Guardar siempre orden de eventos y resultado; nunca alterar un ganador ya registrado.

## 4. IDs, orden y autenticación de eventos

- NationId es UUID inmutable dentro de Season; FactionId es string estable para assets/etiqueta. No usar FactionId como FK de movimientos.
- ChannelBinding único por (seasonId,provider,providerChannelId). Cambiar propietario del binding exige revisión auditada y nunca reusar eventos anteriores.
- sourceKey = SHA256(provider + channelId + immutableExternalEventId + eventType + immutableBindingIdentity), sin usar alias visible. BindingRevision no cambia esta clave para el mismo evento.
- Los eventos externos se autentican según proveedor, se aceptan at-least-once y se deduplican antes de aplicar; si el proveedor carece de ID estable, QUARANTINE hasta un algoritmo documentado específico de ese adaptador, no deduplicación por texto del chat.
- La marca receivedUtc de recepción es del servidor y debe preservarse en replay; providerTimestamp sirve para comprobación de tolerancia y diagnóstico.
- Un evento con identidad/nación incongruente, token revocado, input atrasado fuera de tolerancia o ventana terminada queda REJECTED/QUARANTINED con código estable.

## 5. API pública y privada propuesta

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

## 6. SignalR / transporte de proyecciones

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

## 7. Contrato de sincronización visual

Después de un evento persistido, el ShowDirector emite cue opcional con presentationAtUtc >= commitUtc + margen de presentación (baseline 3 segundos sujeto a pruebas). Cada overlay estima offset de reloj contra servidor y prepara animación. Las escenas pueden comenzar ligeramente desfasadas por latencia entre PCs: **la consistencia de resultado, no la simultaneidad exacta de fotogramas, es requisito competitivo**. Si el cue llega después de expiresAtUtc, mostrar estado actualizado sin una transición cinematográfica obsoleta. K-0 puede narrar localmente o consumir TTS caché compartida; TTS fallido nunca bloquea votos.

## 8. Recuperación, presión y semántica de entrega

- Webhooks EventSub: verificar firma y challenge; HTTP 2xx solo tras Inbox duradera. Nunca DB mutation en handler público.
- Proveedor con stream/poll: persistir cursor, token y última posición segura; no inventar mensajes perdidos que el proveedor no garantice recuperar.
- Outbox se reintenta at-least-once; overlay deduplica por (eventId,sequence).
- Si hay retraso de proyección, compactar en snapshots; nunca acumular miles de sprites/eventos narrativos caducados.
- Backend interrumpido: al reiniciar, usar snapshots + Inbox/Outbox + segments; <=7 días catch-up auditable de economía, sin avances de era offline; >7 días RECOVERY_REQUIRED y decisión de operador, tal como docs 03.
- Single writer por nación con fencing token; no simular en dos workers durante failover.

**ContentHash del diseño:** los archivos versionados que participan en el hash se enumeran en [content_manifest.v2.3.json](../data/content_manifest.v2.3.json). Cada temporada congela archivo, manifest digest, rulesetHash, seed y engineVersion; no recalcularlos con datos actuales tras una migración. Los digests aún no se han compilado.

## 9. Escenarios de prueba obligatorios

SYNC-01 voto 1 ms antes del deadline LIVE aceptado, exactamente deadline rechazado; SYNC-02 desconectar LIVE B durante voto y mantener segundos restantes; SYNC-03 RPS con B caído conserva mismo reloj A/B/C; SYNC-04 60s offline equivalen a 12s economía (sin doble factor); SYNC-05 2 workers con lease vencida no duplican trabajo; SYNC-06 Outbox duplicada no repite ganador/compra; SYNC-07 tres overlays con distintas latencias alcanzan mismo stateHash; SYNC-08 dos Interestelar simultáneas → ganador único; SYNC-09 reconexión con hueco de sequence fuerza snapshot; SYNC-10 caducidad de OAuth deshabilita solo las capacidades dependientes, sin cambiar nación.

**No afirmamos que estas pruebas estén ejecutadas.** Cada caso requiere commit de implementación y evidencia reproducible.
