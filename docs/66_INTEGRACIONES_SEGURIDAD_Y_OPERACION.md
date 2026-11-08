> **Documento de detalle.** La fuente normativa vigente es [ESPECIFICACION_MAESTRA.md](../ESPECIFICACION_MAESTRA.md). Este capítulo no prevalece ante una regla corregida en la especificación; versiones anteriores en Git.

# 66 — Integraciones LIVE, seguridad, despliegue y operación multistreamer (v2.3)

**Normativo para desarrollo, proveedor pendiente de pruebas.** Esta especificación completa docs 14,16,31,32,53,54 y 59. Consulta documental oficial a 2026-11-08; no constituye autorización concedida a cuentas reales.

## 1. Integraciones por capacidades, no por promesa de plataforma

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

## 2. OAuth, invitaciones y roles

Portal K0 usa OIDC propio o proveedor de identidad verificado, auth code + PKCE; OWNER y OPERATOR con MFA. Cada streamer vincula **su cuenta**, concede los scopes mínimos y ve claramente qué se lee/publica. Tokens OAuth y refresh tokens:
- Cifrado en reposo por KMS/KeyVault o equivalente, claves rotadas, segregados por conexión.
- Nunca al navegador OBS ni al frontend del propietario, no en URL, audit export o error.
- Revocación manual y automática; deshabilitar una sola cuenta sin detener las restantes.
- Callback OAuth valida state, PKCE, nonce/issuer y session usuario; asociación comprobada del canal real a identidad conectada.
- La invitación caduca en 24h, hash de token almacenado, single-use transaccional, scope exacto campaign+season+nation+role; el propietario puede revocar.
- Separación de permisos: BROADCASTER no cambia semillas, reglas, importes ni ganador; MODERATOR no puede operar contabilidad; OPERATOR no puede autorizar monetización por sí solo.

## 3. Overlay por streamer sin software local

El mínimo cliente es OBS Browser Source HTTPS. URL de setup contiene solo identificador público y **secreto revocable de lectura**; preferible fragmento de URL para que no aparezca en logs HTTP, con posterior intercambio por sesión read-only de corta duración. El secreto es un credential: no enviarlo por capturas/chat, guardarlo hasheado en backend y permitir rotación inmediata. No insertar refresh token de proveedores en OBS; no abrir puertos entrantes en equipos de streamer. La pantalla renderizada se suscribe con su outputId y allowedNationIds; heartbeat de overlay SOLO indica conexión visual.

Seguridad de cliente: CSP cerrada para scripts/medios autorizados, SRI cuando corresponda, HTTPS/WSS, anti-clickjacking del panel, rate limits en intercambio de token, expiración/rotación, no mezclar capacidades de operador con vistas públicas. Si secret overlay se filtra: revocar y emitir URL nueva; no afecta cuentas o estado lógico.

## 4. Privacidad y redifusión

- Los IDs reales de proveedor no salen de backend en proyecciones públicas. Pseudónimos moderados y consentimiento por contexto; evitar mezclar nombres/chat de plataformas diferentes.
- No publicar mensajes crudos, donaciones, perfiles o avatares de canal B en canal A por defecto. Resúmenes competitivos agregados pueden mostrarse según política verificada.
- Minimización de Inbox: payload/metadata estrictamente necesarios, política de expiración y borrado; retención real debe documentarse con justificación legal y jurisdicción antes de LIVE.
- Derechos de acceso/borrado, portabilidad cuando aplique, menores, moderación, registro del consentimiento de homenajes, y encargados del tratamiento: gate jurídico, no «resuelto» automáticamente.
- Establecer acuerdos del operador/campaña para límites de moderación, responsabilidad de contenidos y contacto de incidentes. No almacenar datos bancarios del espectador.

## 5. Estado de salud y runbook por tres emisores

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

## 6. Despliegue base

Recomendación de referencia: API ASP.NET Core .NET 10 y worker de simulación central con PostgreSQL 16+ gestionada, reverse proxy HTTPS, secrets manager, logs estructurados, métricas, trazas y backup automatizado en región elegida. Frontend overlay estático con React/TypeScript + Phaser probado específicamente con versión de OBS CEF del hardware de destino. Conexión internet saliente normal en PCs de streamers. No P2P ni NAT traversal.

- Hosting mínimo: un entorno STAGING que replica conexiones simuladas, un entorno PROD con secretos/DB separados. Despliegue inmoviliza engineVersion y manifests de temporadas RUNNING; rollback sin cambiar hash.
- No confiar en reloj local de cada PC: servidor calcula UTC y segundos LIVE mediante provider health autenticado.
- No desplegar Redis, Kafka, RabbitMQ, Kubernetes ni servidor de juego dedicado por streamer inicialmente.
- Ingress multi-proveedor puede escalar a procesos separables sin mover la autoridad del motor ni los datos.
- Backups cifrados y restauración programada; hasta pruebas no se anuncian RPO/RTO numéricos como realizados.

## 7. Presupuesto, costes y SaaS futuro

Costes por unidad: horas de worker .NET, Postgres almacenamiento/IOPS/backups, WebSockets/egress por output, llamadas/quotas de cada proveedor, TTS/LLM si habilitado, producción pixel art, moderación y operación. Registrar campaignId/seasonId, hourly operational cost, input_events_count, connection hours y TTS chars para coste por partida y streamer. No confundir «tres streamers» con tres servicios backend. Una instancia central multiplica coste por campañas concurrentes y eventos, no por hardware de cada PC.

Fase piloto: un dueño de campaña y tres streamers autorizados. SaaS/licencias a otros creadores solo después de medir demanda, retención, costes y gobernanza multi-tenant; entonces añadir billing, límites por plan, izolación empresarial y soporte contractual. No realizar modificaciones de arquitectura de alto coste por hipótesis de ventas.

## 8. Monetización y seguridad financiera

Todos los tipos reales de aportación están DISABLED al principio. Si alguna cuenta verifica eventos económicos:
- Creditar oro **solo** tras autenticación, identificador único, regla de conversión específica aprobada, estado final permitido y ledger transaccional.
- La reversión puede generar GoldDebt separado; no editar asiento histórico.
- Ningún streamer puede introducir manualmente oro verificable, comprar votos, acelerar investigación, atacar por pago o transferir ganancias.
- Escena de agradecimiento es cosmética; consentimiento explícito y moderación, jamás ventaja de nación.
- Verificar políticas por proveedor, jurisdicción, fiscalidad y reembolsos. No publicitar monetización antes de esas pruebas.

## 9. Pruebas de seguridad y operación

SEC-M01 invitación caducada/usada doble rechazada; SEC-M02 token de streamer A no puede leer conexiones/credenciales B; SEC-M03 overlay A no puede invocar mutaciones ni ver PII B; SEC-M04 OAuth revocado deshabilita chat/presence reales; SEC-M05 replay de webhook y race con binding revision no duplica comandos; SEC-M06 cross-platform raw chat censurado por defecto; SEC-M07 nombres/chat con prompt injection no controlan K-0; SEC-M08 un único winner frente a competencia concurrente; OPS-M01 reconexión de tres PCs; OPS-M02 fallo de backend; OPS-M03 un streamer termina antes y los otros siguen; OPS-M04 RPS global se congela; OPS-M05 restore backup coincide con snapshot hash.

**Resultado de esas pruebas hoy: NOT_RUN.** Falta evidenciar soporte y permisos específicos para cada cuenta real antes de una prueba pública.
