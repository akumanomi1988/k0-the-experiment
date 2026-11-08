# 63 — Arquitectura multistreamer distribuida (v2.3)

**Normativo para diseño, no implementación validada.** Esta especificación amplía docs 02,13,31,32,55. La nación no equivale a streamer ni a proveedor. Cada emisor puede estar en otro PC, ciudad, sistema operativo o red; la conexión pública HTTPS al servicio K0 es el único requisito de red del cliente de emisión.

## 1. Topologías admisibles

- **Solo operador:** un propietario controla tres canales distintos (reales o simulados); las tres naciones y salidas se crean en la misma campaña. Puede emitir una escena combinada.
- **Tres streamers, mismo proveedor:** Twitch A/B/C (o YouTube A/B/C), cada uno con propiedad y credenciales propias, PC/OBS independientes. El servidor recibe los tres chats, cada uno vinculado a UNA nación.
- **Tres streamers, proveedores mixtos:** Twitch A, YouTube B y otra plataforma C solamente si existe adaptador/autorización válida para esa cuenta concreta.
- **Co-stream:** varias salidas/streamers pueden mostrar la misma nación cuando lo autorice el dueño de campaña, pero un binding tiene exactamente una nación. Un único canal no puede representar dos naciones.
- **Varias campañas:** cada Campaign/Season tiene namespace, hashes, seed, roles, canales y base de datos lógica aislada. No se unen temporadas distintas por coincidir streamer, plataforma o alias.
- **No soportado v2.3:** tres naciones votando desde un solo chat sin asignación verificable; servidor autoritativo instalado por cada streamer; P2P con consenso entre OBS; traducción automática de regalos a oro.

**Modo de temporada obligatorio:** Season.broadcastMode = SINGLE_OPERATOR o MULTI_STREAMER. SINGLE_OPERATOR admite una cuenta K0 como responsable de los tres canales; MULTI_STREAMER exige tres cuentas K0 **distintas** como broadcaster primario, cada una con un asiento aceptado en una nación diferente. Co-streamers no sustituyen el primario. El sistema valida esta invariante en DRAFT→PREPARED dentro de transacción antes de habilitar una temporada pública.

## 2. Arquitectura lógica y despliegue

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

## 3. Modelo de entidades e identidad

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

## 4. Invitaciones, propiedad y permisos

1. OWNER crea Campaign/Season DRAFT y tres Nation asignadas a facciones.
2. OWNER invita a cada streamer mediante enlace expirable de un solo uso, restringido a temporada/nación/rol; la invitación no expone tokens.
3. El streamer inicia sesión en K0, acepta condiciones y enlaza su propia cuenta del proveedor vía OAuth cuando exista. La identidad del streamer debe corresponder a un canal que controla o para el que tiene autorización verificable.
4. El OWNER ve estado de **permiso de lectura de chat**, **verificación LIVE**, **contribuciones**, **overlay** por separado. Ninguna capability no verificada se activa automáticamente.
5. OWNER congela asientos, bindings, autoridades de reloj, seed y manifiesto antes de PREPARED→RUNNING. Cambios posteriores requieren pausa de ingreso + drenaje Inbox + BindingRevision + auditoría y revalidación del originador.
6. Cada broadcaster genera su URL de overlay con un secreto de solo lectura, lo configura como Browser Source en OBS local y puede revocarlo.
7. OWNER controla start/pause/abort; BROADCASTER controla su propia escena y puede informar incidente, nunca asignar ganador ni regalar recursos. MODERATOR filtra contenidos. AUDITOR solo consulta.

**Invariantes:** una cuenta/canal no aparece en dos bindings activos de naciones diferentes en una temporada; una nación tiene exactamente una fuente autorizada de LIVE activa o queda OFFLINE/UNCERTAIN; cada nación tiene al menos un broadcaster primario en modo multistreamer; en modo solo el propietario puede ocupar las tres plazas. Una persona no obtiene control ADMIN por ser streamer.

## 5. Autonomía de tres ordenadores

Cada PC debe poder:
- Encender OBS, cargar una URL HTTPS específica, ver estado remoto y emitir sin instalar motor ni abrir puertos entrantes.
- Recibir snapshots y deltas de su nación y estados agregados de rivales. No accede a balances internos restringidos de otras naciones.
- Recuperar visualización tras reiniciar OBS, perder Wi-Fi o cambiar resolución, sin modificar resultado del juego.
- Cambiar escena visual localmente sin manipular cuándo termina una elección; puede silenciar la voz local de K-0.
- Mostrar contador de conexión del overlay separado de estado real de STREAM; una fuente proveedor LIVE sigue LIVE aunque OBS Browser Source esté desconectado.

**El equipo del streamer no almacena** hashes de contraseñas, claves de otras cuentas, SQLite autoritativa, payloads financieros, tokens OAuth del proveedor ni logs de espectadores de otra nación.

## 6. Independencia de directos y política de equidad

Una temporada puede tener A LIVE, B OFFLINE, C LIVE. Se aplica a cada nación su NationEconomyClock original (100 % LIVE; 20 % offline). Los votos de B y su avance de era esperan su LIVE confirmado. La carrera puede favorecer al streamer que emite más horas: **es una consecuencia explícita del diseño histórico, no un bug oculto**. Se publicará tiempo LIVE acumulado por nación y advertencia al crear campaña. Modalidades con paridad estricta por horas o caps diarios serían un ADR distinto, no un valor implícito.

RPS y batallas programadas se activan exclusivamente con los tres LIVE confirmados y su **CompetitionLiveClock global**. Si uno cae, se congelan las tres ventanas y el operador puede cancelar sin penalización tras un plazo de incidencia; ninguna nación queda castigada por la caída. El evento se reanuda con los mismos votos y tiempo pendiente si la evidencia vuelve y aún está dentro de la política de sesión.

## 7. Control de espectadores multicanal

- Cada entrada trae provider, channelId, providerEventId, providerUserId, receivedUtc y prueba del permiso/autoridad.
- Routing lookup preciso (seasonId,provider,channelId)→nationId; si el canal no está vinculado o la autorización no vale, DROP/QUARANTINE y motivo auditado.
- Reintentos no crean un segundo ciudadano/voto; nombres visibles no identifican al usuario. Cambios de alias no crean otra cuenta.
- Mismo espectador en dos canales de dos naciones puede crear dos ciudadanos conforme a la regla histórica. No se promete deduplicación transversal entre Twitch y YouTube.
- Acciones son visibles solo en la salida correspondiente según las políticas de proveedor; los resultados de juego agregados se pueden publicar si están permitidos. Nunca reenviar chat crudo cruzado por defecto.

## 8. Fallos y recuperación

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

## 9. Escalabilidad progresiva

Fase 1: un proceso .NET API+Worker, una PostgreSQL, un hostname HTTPS, SignalR y workers adaptadores dentro del mismo despliegue. Fase 2: separar ConnectorWorker y SimulationWorker por carga conservando transacciones y single-writer. Fase 3: multi-campaign multi-tenant físico solo si hay monetización de licencia y necesidad medida; no adelantar billing, Kubernetes, Redis o colas.

**Presupuesto de límites candidato:** 3 naciones y 3–9 bindings por temporada; objetivo 30 FPS overlay (no garantizado); input y estado observables desde un panel único. Medir perf con 3 PCs reales + distintos proveedores antes de PUBLIC_READY.

## 10. Aceptación vinculante

- MS-01: 3 PC/redes distintas, mismo proveedor, A/B/C controlan una sola nación cada uno; ninguna máquina hospeda el motor.
- MS-02: 3 proveedores, cada uno autorizado; no cruces de chat ni IDs ni votos.
- MS-03: caída de A OBS mientras Twitch A sigue LIVE no pausa economía A ni votaciones de A.
- MS-04: un LIVE deja de estar confirmado durante RPS: tiempo restante idéntico en A/B/C y sin sanción espuria.
- MS-05: misma seed/inputs, tres overlays desconectados y reconectados: mismo hash lógico de temporada.
- MS-06: invitación caducada/reutilizada, rol sin permisos, token revocado → rechazados sin fuga.
- MS-07: cambio de binding al pausar preserva ciudadanos existentes y no duplica eventos.
- MS-08: reinicio de backend/DB no produce ganador doble ni paga dos veces.
