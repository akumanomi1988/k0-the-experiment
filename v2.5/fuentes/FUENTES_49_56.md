# Fuentes íntegras v2.5 — capítulos 49–56

> **Transcripción íntegra histórica**; consultar [norma v2.5](../ESPECIFICACION_MAESTRA_v2.5.md) para resolver cualquier regla sustituida. Aprobación artística y balance no se certifican por esta copia.

---

## Fuente 49 — `docs/49_AUDIO_ACCESIBILIDAD_E_IDIOMAS_v2.2.md`

**Blob original:** `15eeb4845f56d627842090633efff2b689973abd`.

## 49 — Audio, música, accesibilidad y localización

**Estado: especificación editorial, no bandas sonoras ni locuciones producidas.** El juego no debe depender de voz o música para que las reglas se entiendan.

### Identidad sonora

La firma de K0 combina chasquidos mecánicos breves, pitidos de terminal y percusión ligera; tono de laboratorio retro, no horror. **Tres capas separadas:** ambiente de mundo (mecánica/bioma), interacción (votos, construcción, evolución, peligro) y locución/subtítulos de Doctor K-0. Las transiciones de era evolucionan instrumentos: Paleolítico percusión seca, Neolítico flautas/superficies, Cobre-Bronce resonancias metálicas, Hierro-Antigüedad conjunto de campanas, Media-Renacimiento instrumentos de cámara, Industrial percusión de máquinas, Moderna analógico, Digital síntesis chiptune, Espacial drones orbitales, Interestelar síntesis amplia. Es una descripción compositiva ORIGINAL, no licencia de música ajena.

### Mezcla propuesta

Medidor de salida del stream objetivo -16 LUFS integrado con limitador a -1 dBTP, por verificar en la plataforma elegida. Locución prioriza inteligibilidad mediante sidechain/ducking de música de ~-9 dB durante frase, y del ambiente de -4 dB. Picos de alertas no sobrepasan los picos de voz; sonidos de error no repiten indefinidamente. El operador dispone de silenciar voz, música y efectos por buses separados, además de modo seguro silencioso.

### Catálogo de cues mínimos

| ID | Disparador | Audio | Subtítulo obligatorio |
|---|---|---|---|
| `citizen_join` | Join confirmado | Click suave 0.2s | Sí, puede ser condensado |
| `work_confirmed` | Oficio fijado | Herramienta 0.4s | Sí |
| `milestone` | Hito persistido | Fanfarria 1.5s | Sí |
| `vote_open` | Votación abierta | Campana 0.8s | Sí |
| `vote_close` | Commit resultado | Golpe 0.6s | Sí |
| `rps_result` | Ronda cerrada | Percusión 1.0s | Sí |
| `era_transition` | Nueva era persistida | Tema 4–6s | Sí |
| `live_uncertain` | Se pierde autoridad | Alerta corta una vez | Sí, persistente |
| `season_winner` | Ganador confirmado | Tema 6–9s | Sí |
| `tts_failed` | Voz no disponible | Ninguno | Sí, fallback legible |

### Accesibilidad funcional

Todos los eventos se expresan también por texto, icono y contexto; no únicamente color o sonido. Subtítulos de máximo dos líneas, salvo pantalla dedicada con scroll controlado; no tapar votos ni mapa crítico. Animación de victoria configurable como `reducedMotion`: sin destellos rápidos, flash o movimiento excesivo. Contraste verificable y daltónicos: iconos de facción y patrones distintos. La UI contempla niños y audiencias diversas; no solicita identificación personal ni expone chat ofensivo sin moderación.

### Localización

El paquete editorial de salida deberá admitir `es-ES` y `en-US`; IDs de comandos (`!join`, `!work`, etc.) permanecen invariantes inicialmente para reducir ambigüedad. Todos los textos de UI y narración se almacenan por clave, con variables tipadas como `nation`, `era`, `remainingLiveSeconds`, `points`, `displayNameModerated`. Ningún nombre visible se traduce de forma automática (nombre propio K-0, Micelios, Rúnicos, Ferrinos). Todo texto de HUD debe tener versión abreviada y versión de accesibilidad. No concatenar gramaticalmente frases dependientes del género sin plantillas correctas.

### Gate

Aprobar voz, mezcla y títulos requiere audio real bajo carga, auriculares y altavoz de móvil, derechos de autor/ejecución pública y pruebas de subtítulos con transmisiones reales. Los números de este documento son **objetivos de diseño**, no medidas de emisiones.


---

## Fuente 50 — `docs/50_EXPERIENCIA_DE_CIUDADANO_Y_FEEDBACK_v2.2.md`

**Blob original:** `3f28951f31af853af00487d15a36921491d41529`.

## 50 — Ciclo de usuario: comandos, tutorial, errores y fidelización

### Principio

Un espectador debe entender en 30 segundos tres cosas: qué nación ve, qué puede escribir y qué cambiará. La participación debe dar feedback aunque la cámara no muestre su sprite por límites de LOD. No exigir una web, registro adicional ni pago para entrar al juego.

### Primer contacto

1. Entra a un canal asignado a exactamente una nación. HUD explica «Únete: !join». 2. En `!join` válido se crea un ciudadano idéntico por reintentos del mismo evento. 3. Recibe «Elige una profesión» + cinco etiquetas sin revelar códigos internos innecesarios. 4. En `!work food` (u otra) se fija el oficio de temporada y empieza periodo de actividad real de 2h. 5. Ve confirmación del contador de actividad y producción colectiva, no una promesa de sprite individual siempre visible. 6. Al superar niveles 3/7/12, `!skill <id>` selecciona uno de dos skills habilitados por tramo y profesión. 7. Al volver a otro directo, `!active` reanuda actividad tras cooldown; el chat casual no renueva trabajo.

### Contrato de respuesta a cada comando

| Entrada | Aceptado cuando | Feedback positivo | Rechazo visible |
|---|---|---|---|
| `!join` | Cuenta de proveedor reconocida y canal autorizado | Ciudadano creado o ya registrado | Fuente sin permisos o evento ilegítimo |
| `!work` | Ciudadano registrado, profesión válida y no bloqueada | Oficio y actividad 2h | Profesión distinta ya elegida; código inválido |
| `!active` | Profesión fijada, cooldown terminado | Actividad hasta hora UTC | Sin oficio; cooldown |
| `!skill` | Nivel/tier permitido y sin elección previa | Habilidad seleccionada | Habilidad de otra profesión o tramo consumido |
| `!gov` | Ventana abierta, elegible | Papeleta registrada/modificada | Fuera de plazo, opción inválida |
| `!priority` | Ventana abierta, elegible | Papeleta registrada/modificada | Inhabilitado por reloj LIVE |
| `!build` | Consejo abierto, id presente entre tres opciones | Papeleta registrada/modificada | Id no disponible/edificio fuera de catálogo |
| `!rps` | Ronda abierta, primer voto | Se confirma voto secreto sin revelar opción al público | Voto previo irrevocable, ronda cerrada |

El feedback privado/en chat es **best effort**; el evento de juego puede confirmarse aun si el proveedor prohíbe respuestas públicas. La ausencia de confirmación externa no autoriza duplicar operación. La UI de administración sí registra estado real con `sourceKey`.

### Interrupción o inactividad

Cuando el usuario no está activo, su avatar puede descansar, pero la ciudadanía no desaparece ni produce con eficiencia gratuita. No se cambia profesión entre streamings. Si el canal se desconecta, `!active` no se atribuye a otra nación y la ventana LIVE no avanza. Si la fuente se reconecta tarde, los comandos con antigüedad superior a `maximumInboundMessageAgeSeconds` se rechazan o quedan en cuarentena según catálogo. No reprocesar retransmisiones de chat como input nuevo.

### Recompensa y retención sin presión

El valor es persistencia de nombre/historial y pertenencia, no una compra: panel de «tu oficio» cuando está presente, fichas de logro, ceremonia de participación, ranking de contribución **no monetaria** y resumen de temporada. Sin leaderboard que compare dinero pagado con productividad; no falsear actividad o número de espectadores. El descanso de dos horas puede recordarse sin notificaciones externas no consentidas.

### Prueba documental de UX

Tres recorridos: novato (0 conocimiento), repetidor (vuelve 3 días después), espectador que solo observa. Para cada uno simular 0, 1 y 10k ciudadanos concurrentes; el estado económico y el derecho al voto se mantiene aunque su sprite deje de renderizarse. Rechazos deben explicar acción concreta y no mostrar secretos de proveedor, SQL, hashes internos ni stack traces.


---

## Fuente 51 — `docs/51_GENERACION_MAPA_Y_PRESENTACION_SIMULADA_v2.2.md`

**Blob original:** `d1a737e7fbc7727968b61b25c11ddfa732a9008f`.

## 51 — Generación de mapa, distribución y simulación visual

**Objetivo:** que todos los escenarios produzcan un mundo estable, legible y reproducible sin convertir pathfinding en lógica económica.

### Reglas territoriales

Base inicial por nación: 48×48 tiles lógicos de 32×16; expansión de margen de ocho tiles por era, máximo 256×256. Tres facciones comienzan con **la misma capacidad matemática** de fuentes naturales de comida, madera, piedra, conocimiento y trabajo; mineral aparece desde era 3. Los biomas son cosméticos. El generador recibe `seasonSeed`, `nationId`, `eraIndex`, `mapGeneratorVersion`; usa un generador determinista, sin consultar hora local ni `Math.random()`.

### Orden de construcción del mapa

1. Reservar núcleo cívico común y acceso de caminos. 2. Establecer zonas naturales garantizadas para las cinco profesiones, incluso en caso de bioma adverso. 3. Colocar masas de decoración sin bloquear futuras parcelas esenciales. 4. Crear pasillos que conecten fuentes y asentamiento. 5. Reservar parcelas para edificios básicos obligatorios y huellas máximas. 6. Colocar variaciones estéticas de facción por seed. 7. Ordenar candidatos de parcela por distancia a núcleo, compatibilidad de huella, accesibilidad y coordenadas (desempate lexical); nunca hacer depender resultado de una animación. 8. Al pasar de era, expandir anillos y conservar edificios antiguos con su dirección y estado.

### Proyección y render

Proyección oblicua con relación 2:1: el eje del suelo es rombo 32×16, y la altura de objeto se añade al eje visual vertical, no al costo lógico. El orden de dibujo depende de profundidad lógica y anclaje de suelo, con desempate por ID para evitar flicker. Los sprites caminan por rutas entre puntos de interés; la posición visual es interpolada y puede diferir del «trabajador lógico» sin afectar su tasa de producción. Un ciudadano cuya ruta gráfica se bloquea se teletransporta tras una ventana cosmética segura; no pierde economía por problemas de colisión gráfica.

### Edificios y parcelas saturadas

En caso de no existir parcela actual, mostrar `WAITING_PLOT` y buscar el siguiente sector expandible; no descontar recursos antes de reservar obra y ubicación atómicas. Nunca colocar un objeto en fuente natural obligatoria que impida generación mínima. Los edificios anteriores se preservan (sin destrucción por transición); las nuevas eras aumentan densidad hasta el máximo territorial. Política de fallback visual: skyline/centro de obra representado en panel lateral si no queda parcela factible, con advertencia de operador; **no** fingir obra completada.

### Densidad y LOD

Máximo sugerido 45 ciudadanos visibles en vertical y 90 en horizontal; prioridad persona propia si verificable, participantes recientes, premiados y muestra semillada. El resto se agrega en contadores. Dos salidas render pueden mostrar diferentes sprites sin modificar la misma nación en backend. La expresión «10.000 habitantes» no implica 10.000 entidades de animación/IA de cliente.

### Pruebas mínimas del diseño

Misma seed+versión produce mismas parcelas, aunque se cambie hardware, FPS, resolución o plataforma. Distintas seeds pueden variar decoración, nunca permisos económicos. Zona natural inicial no queda oculta por infraestructura. Al llegar al máximo 256×256 se emite alerta con estrategia de fallback no destructiva. Ninguna transición invalida la ruta de ciudad al sector cívico. Estos son **criterios** de prueba, no una generación de mapa realizada en esta revisión.


---

## Fuente 52 — `docs/52_CALENDARIO_DE_EMISION_Y_EVENTOS_v2.2.md`

**Blob original:** `ba634efe00b0a3db7abece088a0372e726498493`.

> **Enmienda normativa v2.3 (multistreamer distribuido):** cada streamer puede emitir en horarios distintos; la economía LIVE/OFFLINE es local a su nación, y los torneos compartidos requieren tres LIVE simultáneos y congelación global en desconexión. El plan de 4h es ejemplo editorial, no reloj obligatorio. [Especificación vigente](CURRENT_SPEC.md).

## 52 — Operación editorial, calendario de emisión y ritmo de espectáculo

### Objetivo

La simulación puede existir offline, pero el espectáculo requiere sesiones programadas. El calendario editorial debe proteger la equidad de las tres naciones y no prometer actividad LIVE cuando no está confirmada.

### Secuencia recomendada de una sesión de cuatro horas

| Minuto editorial relativo | Escena prevista | Condición real |
|---|---|---|
| 0–5 | Boot, estado de canales, resumen offline | Solo con fuente autenticada |
| 5–25 | Mundo y ciudadanos; tutorial `!join`, `!work` | No falsificar votos |
| 25–55 | Ventana abierta para eventos no solapados y narración | Puede variar si hay elecciones de una hora |
| 55–75 | Consejo si hay tres opciones costeables | Si no hay tres, escena alternativa informativa |
| 75–100 | Eventos/estado de investigación | Sin avance artificial de era |
| 100–140 | Torneo RPS o batalla automática **si programado y permitido** | Requiere las tres naciones LIVE; priorizar una modalidad |
| 140–205 | Resumen, misiones, hitos y eventos cosméticos | No adelantar progreso por show |
| 205–240 | Final editorial, métricas, próximos hitos, operador cierra stream | No implica cerrar temporada |

El horario no altera valores del reloj. Elecciones duran 60 minutos de LIVE + eventual segunda vuelta; si la edición de la sesión no permite ese tiempo, continúa abierta a la próxima emisión, nunca se acorta artificialmente. El orden funcional elección→prioridad→Consejo tiene preferencia sobre agenda editorial.

### Frecuencias máximas, no cuotas mínimas

- RPS según planificación del operador; no se ejecuta «porque faltan espectadores» sin las tres fuentes LIVE.
- Batalla automática, por defecto, máximo una por 24h LIVE de campaña; no se superpone con RPS ni con una elección crítica.
- `catchup_challenge` máximo dos por nación/temporada y solo si retraso ≥2 eras, duración 30 minutos LIVE. `resource_storm` máximo una cada 12h LIVE. `wildlife_parade` máximo una cada 4h LIVE; sin efectos de estado. `wonder_festival` máximo una cada 24h LIVE con elegibilidad real.
- Si hay múltiples cues, orden: ganador de temporada, transición era, resultados de elecciones, incidente proveedor, torneo, misión y cosmética. No bombardear al espectador con notificaciones cada tick.

### Dependencias de producción

La campaña necesita tres fuentes de atribución distintas, que pueden ser tres canales del mismo proveedor. Una sola señal de vídeo puede mostrar las tres naciones, pero **un único chat no puede emitir acciones para las tres** según la regla actual. Publicación de multicámara y mezcla de chat entre plataformas quedan sujetas a permisos. Ninguna programación justifica una conversión de regalos no verificada.

### Runbook

**Pre-LIVE:** comprobar conexión por cuenta, salud del token y permisos, reloj de cada nación, versión de reglas, snapshots, moderación, audio/OBS, modo seguro y escena de contingencia. **Durante:** vigilar Inbox, votos y contadores LIVE, colas, recursos, latencia, TTS, logs de moderación y reloj UTC. **Post-LIVE:** congelar relojes, publicar resumen solo de estados confirmados, revisar eventos pendientes, respaldos y notas de incidente. Cambio crítico de reglas o credenciales requiere operador autorizado y registro de auditoría.


---

## Fuente 53 — `docs/53_MATRIZ_DE_INTEGRACIONES_LIVE_v2.2.md`

**Blob original:** `28abf54be351a05d7b10114f9e56e0ae8190f42f`.

> **Enmienda normativa v2.3 (multistreamer distribuido):** se exige CapabilityEvidence por cada cuenta de los tres streamers. Tres cuentas del mismo proveedor son tres autorizaciones distintas. No hay crédito de oro real ni integración TikTok sin aprobación específica. [Especificación vigente](CURRENT_SPEC.md).

## 53 — Matriz de proveedores LIVE y atribución de eventos

**Estado: arquitectura de integración, no permisos acreditados.** Revisión documental de fuentes públicas: 6 de noviembre de 2026. La documentación de un API no demuestra acceso al recurso para la cuenta ni autoriza usos comerciales concretos.

### Capacidades contrastadas y pendientes

| Plataforma | Lectura de chat | Presencia LIVE | Eventos económicos | Estado para producto |
|---|---|---|---|---|
| Twitch | Existe EventSub `channel.chat.message`; sujeto a autorización y scopes concretos | Debe verificarse en canal con permisos y estado | Existen tipos de notificación, pero cada aportación necesita evidencia, semántica y reversos | **GATE POR CUENTA** |
| YouTube | API `liveChatMessages.streamList` (preferida por baja latencia) o `list` con `pollingIntervalMillis` | Depende del broadcast/chat autorizado | `liveChatMessage` puede incluir eventos de financiación; no equivale a dinero irrevocable | **GATE POR CUENTA** |
| TikTok | No se afirma disponibilidad de una API pública universal de chat LIVE en esta revisión | Debe obtenerse confirmación oficial y permisos de la cuenta | No se inventa endpoint/importe/verificación de regalos | **BLOQUEADO HASTA EVIDENCIA** |
| Simulación local | Eventos sintéticos `provider=simulated` | Reloj sintético | `DEMO`, nunca dinero real | **Solo pruebas de diseño** |

Referencias oficiales para estudio futuro: Twitch EventSub https://dev.twitch.tv/docs/eventsub/eventsub-subscription-types/ ; YouTube `streamList` https://developers.google.com/youtube/data/live/reference/rest/v3/liveChatMessages/streamList ; YouTube `list` https://developers.google.com/youtube/data/live/reference/rest/v3/liveChatMessages/list ; catálogo de mensajes https://developers.google.com/youtube/data/live/reference/rest/v3/liveChatMessages . Revalidar estas URLs, versiones y scopes justo antes de desarrollo.

### Permisos y contrato del adaptador

Cada `ChannelBinding` contiene proveedor, canal exacto, consentimiento/verificación del propietario, roles `commands`, `live_health`, `contributions`, `display_feed`, autoridad de reloj y revisión. Habilitar un rol solo si la prueba de cuenta ha pasado y existe base de permiso. Son datos por canal, no por nación: tres canales de la misma plataforma pueden representar tres naciones distintas. Un canal no puede representar dos naciones dentro de la misma temporada.

Cada evento se normaliza a `(provider,channelId,providerEventId,providerUserId,receivedUtc,payloadDigest,authorizationStatus,eventType)` y adquiere `sourceKey` idempotente. Un adaptador no puede inferir moneda a partir de un texto de chat; debe aportar evento autenticado y estado verificable. Ante duda, `REJECT/QUARANTINE`, no otorgar oro.

### Matriz de pruebas externas obligatorias

1. Conectar tres canales diferentes y demostrar que los mensajes no se cruzan. 2. Revocar credenciales de uno y comprobar que los demás mantienen su nación, sin falsear LIVE. 3. Reintentar el mismo evento 100 veces: un solo comando económico. 4. Desactivar chat: HUD lo explica, la temporada no interpreta mensajes perdidos como votos. 5. Contar límites de cuota y coste mensual de polling/stream. 6. Confirmar un LIVE desde la fuente propia, no solo por OBS. 7. Evaluar uso cruzado de chat, nombres y datos entre plataformas según política y consentimiento. 8. Para monetización, test de devolución/cancelación y regla legal por proveedor. 9. Registrar versiones exactas de APIs, scopes y captura de autorización.

### Decisión de lanzamiento recomendada

Elegir **un solo proveedor con APIs y permisos realmente comprobados** para las primeras tres fuentes. Desarrollar el motor en modo simulado antes de conectar cuentas reales. El adaptador TikTok no se considera listo por encontrar bibliotecas de scraping no oficiales: eso añade riesgo operativo y contractual y no pertenece a la especificación autorizada.


---

## Fuente 54 — `docs/54_SEGURIDAD_PRIVACIDAD_Y_DATOS_v2.2.md`

**Blob original:** `f08b5b36c1591281de49682bb939da9a3d2510e2`.

## 54 — Seguridad, privacidad, abuso y retención

**Estado: política técnica propuesta, no dictamen jurídico.** El producto puede recibir IDs estables, mensajes, nombres y eventos monetarios. No almacenar texto de chat íntegro sin necesidad operativa o base legal aplicable.

### Fronteras de confianza

`ProviderAdapter` recibe datos externos hostiles: no confiar en displayName, contenido, hora remota, donación anunciada en chat o permisos autodeclarados. `Ingress` valida firma/token/canal, tamaño, antigüedad, rate limit, ID de evento y autorización antes de `Inbox`. `Engine` procesa eventos tipados y nunca ejecuta instrucciones de mensaje ni devuelve datos sensibles al overlay. `Admin` usa identidad de operador separada, MFA cuando se implante, roles mínimos y auditoría. `OBS/Phaser` solo lee deltas públicos o seudonimizados.

### Riesgos y mitigaciones verificables

| Riesgo | Medida de diseño | Gate de prueba |
|---|---|---|
| Chat malicioso/prompt injection | LLM sin permisos de transacción; variables escapadas; plantillas primero | Intentos de instruir K-0 para otorgar oro fallan |
| Falso regalo | Únicamente origen autenticado + regla de conversión aprobada | Evento falso o duplicado no acredita |
| Replay de comandos | `sourceKey` único; timestamp y canal | Mismo evento 100 reintentos, una aplicación |
| Cruce de naciones | FK compuesta `(season,nation)` y binding único | Nunca se muta otra nación |
| Operador malicioso | RBAC, doble verificación para cambios críticos, audit append-only | Operador no puede cambiar ganador/ledger |
| Filtrado de datos personales | Moderación antes de mostrar/leer voz | Nombres con URLs/PII no se emiten |
| Caída de proveedor | `UNCERTAIN`, freeze timers, modo seguro | No se contabiliza segundo LIVE ficticio |
| Robo de claves | Secret store fuera de repo, rotación, scopes mínimos | No hay tokens en logs/snapshots/overlays |
| Saturación o bots | Rate limit por cuenta/canal/tipo + IP/gateway cuando proceda | 10k emisores no colapsan orden de votos |

### Retención propuesta pendiente de revisión legal

Separar `identity` (IDs de proveedor), `ledger` (integridad económica), `publicProfile` (nombre moderado), `contentTelemetry` y `rawMessage`. Valor inicial de diseño: **no persistir mensaje bruto en sistema de negocio**; mantener digest del evento y referencia durante ventana de diagnóstico mínima. Guardar perfiles de temporada solo hasta que exista una política formal de conservación/borrado. No prometer una tabla definitiva de retención en días sin definir jurisdicción, responsabilidades y contratos de plataforma. Anonimizar exportaciones históricas al ejercerse derechos aplicables, preservando asientos contables que legalmente deban retenerse mediante seudónimo no reversible.

### Repositorio público

GitHub contiene diseño y catálogos sin credenciales. Prohibido incorporar claves de TikTok/Google/Twitch, tokens OAuth, webhooks con secretos, mensajes reales, emails de espectadores, datos de pago o archivos de sesión. No usar secretos ficticios que puedan confundirse con los de producción. Derechos de explotación de las especies, diseños, arte y marcas no se deducen de haber hecho público el repo; decidir licencia de código/documentación cuando corresponda.

### Operación segura

Plan de incidentes con severidades: P0 estado competitivo o fondos comprometidos (pausar y no reanudar sin auditoría); P1 incapacidad de fuente LIVE; P2 caída de narración/animación; P3 cosmética. Recuperación mediante snapshot confirmado y ledger inmutable, sin reejecutar pagos por intuición. El cierre de seguridad exige pruebas de restauración, permisos efectivos y respuesta a abuso, no solo declaraciones.


---

## Fuente 55 — `docs/55_ARQUITECTURA_TECNICA_Y_LIMITES_v2.2.md`

**Blob original:** `9297cb2ae3d55d88798e83fafe6632fa9590db1d`.

> **Enmienda normativa v2.3 (multistreamer distribuido):** arquitectura autoritativa central .NET/PostgreSQL, tres streamers en equipos/redes diferentes y overlays OBS read-only; detalles de identidad, sincronía y falla en capítulos 63/64. SLO distingue ACK de mutación económica. [Especificación vigente](CURRENT_SPEC.md).

## 55 — Arquitectura técnica de producción propuesta

**No es código ni infraestructura creada.** Se mantienen las tecnologías ya discutidas: motor autoritativo .NET/C#, PostgreSQL como almacenamiento transaccional, entrada por adaptadores de streaming, API/SignalR de solo proyección, cliente Phaser/React para OBS.

### Responsabilidades y límites

| Subsistema | Responsabilidad | No debe hacer |
|---|---|---|
| `CampaignConfiguration` | Facciones, temporada, reglas inmutables y bindings | Cambiar estado de partida en directo sin aprobación |
| `ProviderIngress` | Validar origen, evento, permisos, idempotencia | Crear recursos o acreditar oro |
| `NationSimulation` | Tick de 5s, economía, ciudadanía, obras, investigación | Renderizar sprites, llamar APIs externas durante transacción |
| `PoliticalScheduler` | Elecciones y Consejos con reloj LIVE | Abrir dos votaciones políticas incompatibles |
| `CompetitionEngine` | RPS y batallas programadas | Activar ataque espontáneo |
| `ContributionLedger` | Aportaciones verificadas, devoluciones y deuda | Confiar en texto de chat |
| `ShowDirector` | Cues autorizados y modulación narrativa | Elegir ganador o cambiar balance |
| `ProjectionAPI` | DTO público/versionado y snapshots | Exponer identificadores y secretos de proveedor |
| `OverlayClient` | Render 2D/LOD, animación y subtítulos | Autorizar gastos/posiciones económicas |
| `OperatorConsole` | Control auditado/pausas/escena segura | Saltarse restricciones del motor |

### Consistencia y concurrencia

Escritor único lógico por nación, más arbitraje global por temporada para primera maravilla y ganador. Inbox y Outbox permiten idempotencia y entrega eventual; los deltas de HUD son proyección, no verdad. Todas las mutaciones económicas usan ledger, locks/versiones y commit atómico. Baseline: PostgreSQL 16+ como referencia del SQL propuesto; no hay todavía pruebas de migración. Cada entrada lleva secuencia para replay; el RNG estable depende de seed y contador, no de reloj ni entorno.

### Entidades clave

`Campaign`, `Season`, `Nation`, `ChannelBinding`, `ProviderIdentity`, `Citizen`, `CitizenSkill`, `ResourceBalance`, `ResourceLedger`, `GoldDebt`, `Building`, `TechnologyProgress`, `MilestoneProgress`, `MissionPeriod`, `GovernmentElection`, `StrategicBallot`, `RpsRound`, `CompetitionEvent`, `WonderClaim`, `NarrationCue`, `AuditLog`, `Snapshot`, `Inbox`, `Outbox`. V2.2 introduce además estados conceptuales `GarrisonUnit`, `AutomatedBattle`, `CosmeticSponsorship`; **el DDL base se acompaña del anexo de diseño `architecture/002_extensiones_diseno_v2.2.sql`, todavía no ensayado ni integrado en migraciones**. Ninguna nueva entidad necesita un microservicio propio en fase 1.

### API y presencia

El cliente OBS solo consume snapshots y deltas con secuencia; en reconexión solicita snapshot base y reanuda del último confirmado, nunca inventa recursos. Eventos de chat no se envían desde frontend como autoridad. API admin se protege de forma distinta de API overlay; los endpoints declarados en `contracts/openapi.v2.yaml` aún no incluyen todos los módulos de v2.2 y no deben tratarse como contrato final. El backend no publica directamente tokens de proveedor al cliente.

### Despliegue de referencia (no ejecutado)

Un backend .NET modular + worker de simulación + PostgreSQL gestionado + UI overlay y consola, con monitorización de señales LIVE, logs estructurados y backups. No añadir colas distribuidas, CQRS completo o contenedores por facción sin datos de carga que los justifiquen. Separar proceso web y worker cuando rendimiento lo exija; diseñar frontera desde el principio para mantener determinismo y evitar caídas de FPS que alteren estado.

### SLO propuestos, no logrados

Tick de 5s con CPU interna objetivo de 50 ms por nación a carga de referencia; P95 de Inbox→ACK validado <1s como objetivo candidato; aplicación económica en tick de hasta 5s; P95 delta visible <2s; escena 30 FPS; RPO/RTO solo se fijan tras ensayar backups y recuperación. La alta disponibilidad de un proveedor no se presume. Meter 100k ciudadanos en DB no implica 100k entidades renderizadas.


---

## Fuente 56 — `docs/56_MODELO_DE_BALANCE_Y_PRUEBAS_NUMERICAS_v2.2.md`

**Blob original:** `4df4a603efdbbe70f193996509ae7b85e6a88021`.

## 56 — Modelo económico, cálculos y metodología de balance

**Estado: CANDIDATE_BALANCE, NO VALIDADO.** Esta hoja de cálculo mental y reglas reproducibles no sustituyen un motor de simulación. Las cifras canónicas están en `data/ruleset.v2.json` y catálogos v2.2.

### Parámetros fijados

Tick 5s; recurso en milésimas; basis points 10.000=100%; NPC 24 de inicio distribuidos 7 comida/5 madera/4 mina/4 obra/4 ciencia; offline al 20%; ventana humana activa 7.200s. Output base por trabajador/min: food 2,4; wood 1,8; stone 1,4; ore 0,65; knowledge 1,2; buildWork 1,2. Mantenimiento alimentario 0,15 por NPC y minuto de economía, más humanos efectivos hasta tope. Capacidad inicial por recurso común 3500 unidades, conocimiento 15000. Cinco hitos por era a 20 puntos cada uno.

### Cálculos de control aritmético (teóricos, sin bonos ni capacidades)

- **Producción alimentaria inicial 60s LIVE:** `7 × 2,4 = 16,8` comida. **Consumo NPC:** `24 × 0,15 = 3,6`; balance bruto +13,2 comida/min, si hay capacidad y no hay eventos. No implica duración de temporada.
- **Madera inicial 60s LIVE:** `5 × 1,8 = 9` unidades. **Piedra antes de era 3:** `4 × 1,4 = 5,6`. **Investigación:** `4 × 1,2 = 4,8`. **Construcción:** `4 × 1,2 = 4,8` unidades de obra.
- **Offline base 60s reales con multiplicador 20 %:** producción alimentaria nominal `16,8 × 0,2 = 3,36`; mantenimiento NPC nominal `3,6 × 0,2 = 0,72`, antes de aplicar capacidad/hambre/factores.
- **Duración mínima de 1ª investigación troncal con 4 NPC científicos y 0 ventajas:** 290 / 4,8 = 60,4167 minutos LIVE equivalentes de ciencia, si conocimiento no se consume en otra cosa y las reglas de prioridad lo permiten. No incluye ticks, edificación ni requisito histórico.
- **Coste estratégico Paleolítico v2.2:** 120 madera + 85 piedra + 20 conocimiento + **0 oro** por proyecto. El holding entre tres opciones de coste idéntico es ese vector una sola vez, no triple.

Los cálculos anteriores son algebraicos, no evidencia de que un NPC en una temporada real llegue de Paleolítico a Interestelar con todos los bloqueos resueltos. La antigua simulación simplificada registra `milestonesAchieved:0` a la vez que llega a era 13; por eso **no sirve para certificar los hitos** y queda archivada como referencia insuficiente.

### Modelo obligatorio de evaluación de una temporada futura

Para cada perfil de participación de (0, 10, 100, 1000, 10000 ciudadanos), cruzar distribución de oficios equilibrada y sesgada × sesiones 0/1/4/24h LIVE día × disponibilidad de cada nación (simultánea, asimétrica, una desconectada) × 0 aportaciones económicas × 3 seeds de mapa × eventos de crisis/penalización. Para aceptación de balance, ninguna nación con 24 NPC debe quedar bloqueada en las eras 1–12 por falta estructural de recursos o dependencias, y ninguna aportación debe acelerar victoria.

### Métricas por escenario

`elapsedWallDays`, `nationLiveSeconds`, `economyEffectiveMinutes`, `eraEntryCommittedAt`, `milestonePoints`, `missionPeriodsCompleted`, `foodShortageSeconds`, `capacityBlocked`, `outstandingReservations`, `goldVerified`, `npcPopulation`, `humanEffectiveWorkers`, `buildingBacklog`, `techBacklog`, `wonderEligibility`, `combatPenaltySeconds` y `per-tick stateHash`.

### Criterios de calibración (propuestos)

Objetivo narrativo: mediana de 2–3 días por era con horario editorial estándar, sin forzar. No adoptar tolerancia hasta ver distribución: documentar P10/P50/P90 por perfil y exposición LIVE. Si P90 queda bloqueado, priorizar corregir dependencias o reserva antes de subir por sistema las tasas. Balancear tres facciones con mismas condiciones y RNG de juego equivalente; no dar ventaja silenciosa al canal con más público. Congelar cambios al comenzar temporada; revisar únicamente entre temporadas.

### Invariantes que deben poder demostrarse

Comida/recursos nunca negativos; ledger suma saldos; evento monetario duplicado no multiplica oro; no existe progreso pagado; todas las etapas de era 1–12 pueden completarse gratis; todas las obras obligatorias tienen ruta material desde zonas naturales; cambios de tick y FPS no alteran resultados; misma entrada ordenada+seed+versión reproduce exactamente estado persistido.

