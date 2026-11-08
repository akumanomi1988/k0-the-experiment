> **Documento de detalle.** La fuente normativa vigente es [ESPECIFICACION_MAESTRA.md](../ESPECIFICACION_MAESTRA.md). Este capítulo no prevalece ante una regla corregida en la especificación; versiones anteriores en Git.

> **Enmienda normativa v2.3 (multistreamer distribuido):** se exige CapabilityEvidence por cada cuenta de los tres streamers. Tres cuentas del mismo proveedor son tres autorizaciones distintas. No hay crédito de oro real ni integración TikTok sin aprobación específica. [Especificación vigente](../ESPECIFICACION_MAESTRA.md).

# 53 — Matriz de proveedores LIVE y atribución de eventos

**Estado: arquitectura de integración, no permisos acreditados.** Revisión documental de fuentes públicas: 6 de noviembre de 2026. La documentación de un API no demuestra acceso al recurso para la cuenta ni autoriza usos comerciales concretos.

## Capacidades contrastadas y pendientes

| Plataforma | Lectura de chat | Presencia LIVE | Eventos económicos | Estado para producto |
|---|---|---|---|---|
| Twitch | Existe EventSub `channel.chat.message`; sujeto a autorización y scopes concretos | Debe verificarse en canal con permisos y estado | Existen tipos de notificación, pero cada aportación necesita evidencia, semántica y reversos | **GATE POR CUENTA** |
| YouTube | API `liveChatMessages.streamList` (preferida por baja latencia) o `list` con `pollingIntervalMillis` | Depende del broadcast/chat autorizado | `liveChatMessage` puede incluir eventos de financiación; no equivale a dinero irrevocable | **GATE POR CUENTA** |
| TikTok | No se afirma disponibilidad de una API pública universal de chat LIVE en esta revisión | Debe obtenerse confirmación oficial y permisos de la cuenta | No se inventa endpoint/importe/verificación de regalos | **BLOQUEADO HASTA EVIDENCIA** |
| Simulación local | Eventos sintéticos `provider=simulated` | Reloj sintético | `DEMO`, nunca dinero real | **Solo pruebas de diseño** |

Referencias oficiales para estudio futuro: Twitch EventSub https://dev.twitch.tv/docs/eventsub/eventsub-subscription-types/ ; YouTube `streamList` https://developers.google.com/youtube/data/live/reference/rest/v3/liveChatMessages/streamList ; YouTube `list` https://developers.google.com/youtube/data/live/reference/rest/v3/liveChatMessages/list ; catálogo de mensajes https://developers.google.com/youtube/data/live/reference/rest/v3/liveChatMessages . Revalidar estas URLs, versiones y scopes justo antes de desarrollo.

## Permisos y contrato del adaptador

Cada `ChannelBinding` contiene proveedor, canal exacto, consentimiento/verificación del propietario, roles `commands`, `live_health`, `contributions`, `display_feed`, autoridad de reloj y revisión. Habilitar un rol solo si la prueba de cuenta ha pasado y existe base de permiso. Son datos por canal, no por nación: tres canales de la misma plataforma pueden representar tres naciones distintas. Un canal no puede representar dos naciones dentro de la misma temporada.

Cada evento se normaliza a `(provider,channelId,providerEventId,providerUserId,receivedUtc,payloadDigest,authorizationStatus,eventType)` y adquiere `sourceKey` idempotente. Un adaptador no puede inferir moneda a partir de un texto de chat; debe aportar evento autenticado y estado verificable. Ante duda, `REJECT/QUARANTINE`, no otorgar oro.

## Matriz de pruebas externas obligatorias

1. Conectar tres canales diferentes y demostrar que los mensajes no se cruzan. 2. Revocar credenciales de uno y comprobar que los demás mantienen su nación, sin falsear LIVE. 3. Reintentar el mismo evento 100 veces: un solo comando económico. 4. Desactivar chat: HUD lo explica, la temporada no interpreta mensajes perdidos como votos. 5. Contar límites de cuota y coste mensual de polling/stream. 6. Confirmar un LIVE desde la fuente propia, no solo por OBS. 7. Evaluar uso cruzado de chat, nombres y datos entre plataformas según política y consentimiento. 8. Para monetización, test de devolución/cancelación y regla legal por proveedor. 9. Registrar versiones exactas de APIs, scopes y captura de autorización.

## Decisión de lanzamiento recomendada

Elegir **un solo proveedor con APIs y permisos realmente comprobados** para las primeras tres fuentes. Desarrollar el motor en modo simulado antes de conectar cuentas reales. El adaptador TikTok no se considera listo por encontrar bibliotecas de scraping no oficiales: eso añade riesgo operativo y contractual y no pertenece a la especificación autorizada.
