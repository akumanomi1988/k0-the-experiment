> **Regla vigente:**** StreamerSeat, ProviderConnection, BroadcastOutput y ProviderLiveSession son entidades distintas; cada streamer autentica y autoriza su propio canal. La señal OBS no acredita LIVE; ver capítulo 63. [Especificación vigente](ESPECIFICACION.md).

# 02 — Topología configurable de canales y ciudadanía

## Modelo obligatorio
`Campaign` (creador/propietario), `Season`, `Nation` (exactamente tres), `ChannelBinding` (plataforma+cuenta/canal), `ProviderIdentity` (usuario auténtico de proveedor), `Citizen` (persona jugable en una nación/temporada) y `BroadcastOutput` (overlay con filtros). `NationId` es UUID y `FactionId` es un slug de facción distinto. `NationId` nunca deriva de `provider`, no puede ser nombre de plataforma, y es inmutable dentro de una temporada. `ChannelBinding` tiene roles explícitos: `commands`, `live_health`, `contributions`, `display_feed`. Cada nación designa exactamente un canal con `isClockAuthority=true`, `role=live_health`; su señal autenticada define el LiveClock de esa nación para no sumarlo dos veces si existen cuentas secundarias. Otras fuentes aportan chat y métricas pero no alargan el reloj. El operador puede cambiar la fuente de reloj solo pausando y auditando la revisión; en simulación hay control manual auditado.

## Ejemplos admitidos
1. Micelios=Twitch canal A, Rúnicos=Twitch canal B, Ferrinos=Twitch canal C.
2. Micelios=TikTok cuenta A, Rúnicos=TikTok cuenta B, Ferrinos=TikTok cuenta C (únicamente si la integración autorizada expone los eventos necesarios).
3. Micelios=YouTube canal A, Rúnicos=Twitch B, Ferrinos=TikTok C.
4. Una nación puede recibir dos canales distintos, por ejemplo streaming principal más un canal secundario, sin duplicar la identidad de un mismo usuario del mismo proveedor. Nunca asignar **el mismo canal** a dos naciones en una temporada: riesgo de votos/copias ambiguas.
5. Simulador local admite exactamente tres fuentes `simulated`, una por nación, sin fingir que son aportaciones monetarias reales.

## Persistencia de ciudadanía
Clave de usuario de proveedor = `(provider, providerUserId)`; nunca nombre visible. Ciudadano = `(seasonId, accountId)` único, con correspondencia de identidad de origen verificada `(provider,providerUserId)`; `nationId` queda fijado y no cambia en la temporada. Varios canales de **igual proveedor** asignados a misma nación producen **un solo ciudadano**. **Una cuenta K0 queda adscrita a UNA nación por temporada**, incluso si escribe en otros canales; el intento incompatible devuelve `NATION_LOCKED` y no genera otro ciudadano. El primer `!join` autenticado autoaprovisiona una cuenta K0 interna a partir de `(provider,providerUserId)` sin formulario ni contraseña; se fija la nación en transacción con índice `UNIQUE(season_id,account_id)` y deduplicación de origen. Si se verifica que dos identidades de proveedor pertenecen a una misma cuenta K0, comparten su adscripción; **sin vinculación verificada no se garantiza reconocer a la misma persona entre plataformas**, y jamás se infiere por alias/IP. Una fusión de cuentas con adscripciones contradictorias se rechaza mientras la temporada esté activa. El pseudónimo público es generado; alias real de plataforma solo tras consentimiento revocable y moderación.

**Criterio de migración:** cambiar la plataforma/cuenta asociada a una nación durante temporada activa es un cambio privilegiado que requiere pausa de entrada, drenaje de Inbox, grabar estado y `BindingRevision`; el ciudadano anterior mantiene su nación y stats; no se mueve automáticamente a otra. Cambios de binding requieren origen autorizado, usuario operador MFA y log. Cambiar de nación una misma cuenta ya registrada está prohibido durante la temporada.

## Entrada y permisos
Un adaptador `IPlatformAdapter` convierte `(provider, channel_id, event_id, received_utc, provider_user_id, capability, payload)` a `NormalizedEventV2`. El enrutador `BindingResolver` usa `(seasonId, provider, providerChannelId)` para obtener una sola nación; si no existe una asignación activa, `DROP_UNMAPPED` auditable. Mensajes de chat, estado LIVE y aportaciones son tres capacidades separadas; si no hay permisos para una, se desactiva solo esa capacidad. Un `binding` nunca puede autohabilitar monetización.

## LIVE y relojes por nación
Cada nación puede estar `LIVE_CONFIRMED`, `OFFLINE_CONFIRMED` o `UNCERTAIN`. `UNCERTAIN` cuenta como offline para economía y pausa votaciones; no consume tiempo de penalización de torneo. Para abrir una ceremonia de nueva era se requiere `LIVE_CONFIRMED` de la propia nación. Para un torneo simultáneo se requieren las tres naciones LIVE y un `broadcastSession` compatible. Ninguna nación debe quedar bloqueada para siempre por una cuenta desconectada: sigue simulando offline y acumula `EraReadyPending` hasta próxima emisión confirmada.

## Salidas y cumplimiento
Cada salida OBS tiene `OutputId`, `BindingId` emisor y una política `allowedNations`. Por defecto muestra solo elementos de ese canal, agregados del mundo permitidos y resultados del propio juego sin reproducir mensajes/reacciones crudos de plataformas ajenas. Mezclar chat, mensajes o referencias cruzadas requiere aprobación de política por proveedor. Ver `docs/16_INTEGRACIONES_Y_CUMPLIMIENTO.md`.
