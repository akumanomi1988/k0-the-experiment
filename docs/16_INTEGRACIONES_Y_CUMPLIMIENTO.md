> **Regla vigente:** la conexión OAuth y evidencia de cada capacidad corresponde a cada streamer/canal. Twitch/YouTube solo bajo scopes propios y TikTok no se afirma disponible; consulta 66 para onboarding, seguridad y permisos. [Especificación vigente](ESPECIFICACION.md).

**Primer proveedor elegido:** YouTube Live, exclusivamente tras completar las doce eras en simulación, validar permisos de cuenta/canal, cuotas y políticas reales. Primer operador SINGLE_OPERATOR con tres canales, multistreamer posteriormente. TikTok/Twitch siguen disponibles solo en modelos contractuales, no se les atribuyen permisos no probados.

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
