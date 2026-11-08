# 65 — Diseño de producto, experiencia del streamer, overlays y arte (v2.3)

**Normativo para las nuevas experiencias multistreamer.** Complementa 20,24–30,46–50,61–62; **no sustituye** manuales artísticos ni implica que se hayan dibujado sprites o aprobado capturas. Mismo mundo lógico; cada streamer tiene una vista y un canal propios.

## 1. Experiencias y pantallas

### Portal del propietario
1. Nueva campaña: nombre público, idioma, zona editorial, formato de carrera y 3 naciones fijas.
2. Nueva temporada DRAFT: selección de catálogo inmutable versionado, seed, política de emisión y calendario sugerido (no obliga horarios).
3. Sala de convocatoria: tres asientos de streamer con nación, invitación, fecha expiración, rol, estado de cuenta, chat, stream_presence, overlay y conexión de prueba; propietario puede revocar antes de empezar.
4. Validación: matriz preflight con pruebas de permiso por canal y lista de riesgos; botón START desactivado sin tres fuentes válidas en PUBLIC_LIVE.
5. Cockpit RUNNING: estado de tres LiveClocks, progreso, Inbox lag, latencia, salud DB, colas, votaciones, torneos, OBS clients, streamers online, eventos, log de cambios.
6. Post-temporada: campeón, hashes, ledger auditable, historial de narración, recuperación y exportación permitida.

### Portal del streamer invitado
1. Invitación por enlace one-use de 24h, nombre de campaña/nación, descripción clara de permiso y alcance; requiere autenticación K0.
2. Enlazar cuenta del proveedor **que controla**. Solicitar scopes mínimos; mostrar pantalla de privacidad y estado; negarse a fingir conexión si falta API.
3. Probar capacidad de chat con mensaje de diagnóstico y confirmación de fuente; test de stream_presence separado de OBS; monetización siempre desactivada salvo habilitación expresa posterior.
4. Elegir overlay vertical (360×640 lógico) u horizontal (640×360 lógico); preview, copiar URL read-only, regenerar clave y abrir test seguro con datos SIMULATED.
5. Copiar a OBS Browser Source (solo URL) y ajustar resolución real a 1080×1920 o 1920×1080; indicación de que la fuente web es solo visual y la partida seguirá aunque OBS se reinicie.
6. Durante LIVE: ver mi nación, estado global, comando actual, próxima escena, errores de proveedor, notificaciones moderadas y estado real del overlay.
7. Desconexión: mostrar dónde falló (OBS, navegador, chat, credencial, stream) con acciones de reintento que no modifiquen la simulación.

### Espectador del canal A/B/C
- Ve primordialmente su nación; siempre identifica facción, era, progreso, evento actual, estado LIVE real y comandos válidos.
- Nunca se le exige visitar otra plataforma para participar; el chat del canal determina automáticamente nación.
- Puede ver resumen público de rivales sin mostrar chat crudo, nombres no consentidos, avatares o métricas privadas de esos canales.
- Inicio: explicación breve de !join, !work <oficio>, !active; durante eventos, opciones y duración; respuestas a comandos por canal si message_write autorizado, y siempre acuse visible en overlay cuando proceda.
- Permite mirar sin chat ni audio y comprender el estado. Los mensajes de K-0 están subtitulados.

## 2. Sistemas de vistas, escenas y transiciones

Cada BroadcastOutput tiene outputId, allowedNationIds, primaryNationId (si NATION_FOCUS), layoutMode, locale, moderationPolicyVersion, overlayPolicyVersion y outputRevision.

Modos aprobados:
- NATION_FOCUS: vista de una nación + resúmenes públicos y evento global; default del streamer.
- SHARED_WORLD: montaje de las tres naciones, para propietario o distribución autorizada; no agrega control del chat ni redistribuye mensajes crudos.
- EVENT_STAGE: marcador RPS/batalla de las tres, sin datos privados.
- SAFE_SCENE: escena informativa durante problema técnico.

Escenas canónicas heredadas: BOOT_CHECK, WORLD, GOV_VOTE, PRIORITY_VOTE, COUNCIL_VOTE, TOURNAMENT, ERA_TRANSITION, SEASON_END, más CONNECTING, CHANNEL_REVOKED, MULTISTREAMER_WAITING, GLOBAL_EVENT_PAUSED y RECOVERING.

**Regla:** las escenas visuales no alteran reglas ni relojes. Una nación puede seguir produciendo mientras su overlay está en SAFE_SCENE. Un evento compartido se representa en los tres equipos con el mismo eventId/resultado, pero puede iniciar animación con pequeña variación de latencia. No se sincroniza nada con captura de pantalla de OBS ni audio local.

## 3. Pixel art y sistema de arte

- Pixel art retro 2D de baja resolución, proyección oblicua de suelo **2:1**, tiles lógicos **32×16**, sprites de ciudadano **16×24** como unidad inicial de contrato. Pivote inferior centrado, sombras discretas, escalado entero, texturas sin suavizado.
- Micelios, Rúnicos y Ferrinos son culturas claramente distintas en silueta, lenguaje material y paleta; **mismas estadísticas** de partida, el bioma es cosmético.
- Doctor K-0 es cyborg visualmente inequívoco y neutral, legible a tamaño pequeño; evita figura genérica de médico humano. Animaciones cortas de 2D recortado y ciclos sencillos (idle, gesto, aviso, ceremonia) antes de invertir en 3D.
- Los oficios son cinco familias mecánicas fijas; nombres, instrumentos y ropa evolucionan por era sin cambiar IDs, XP ni perks.
- Edificios: 10 familias × 13 eras de catálogo, 4 etapas visuales de construcción heredadas; 39 proyectos y 13 maravillas. Para prototipo dibujar un subconjunto comprobable y mantener placeholders etiquetados, nunca anunciar 130 sprites aprobados.
- Era 13 INTERSTELLAR es epílogo visual y no economía jugable. Sus assets no son bloqueo para el primer vertical slice.
- 39 tipos de unidad de combate son definiciones por era/rol con 3 skins por especie; para prototipo de batalla usar figuras legibles con animación teatral, no simulación gráfica de impacto autoritativa.
- Mantener un inventario de assets con artId, factionId, eraId, resolution, pivot, animationFrames, frameRate, license, author, status (BRIEF/DRAFT/REVIEWED/APPROVED), revisión, dependencias y hashes. Ningún asset marcado APPROVED sin captura en OBS.

## 4. Layout y responsive

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

## 5. Reglas de interacción y anti-confusión

- Una persona que entra en Twitch B no debe creer que el comando dirige la nación de Twitch A; mostrar de forma persistente canal asociado y la facción.
- Comandos existentes !join, !work, !active, !gov, !priority, !build, !rps, !skill. No crear comandos nuevos del stream principal sin contrato.
- Voto en RPS no revela distribución por opción antes de cierre; en elecciones/Consejo se pueden mostrar barras autorizadas. Una papeleta no puede aparecer aceptada si Inbox no confirmó.
- Voto pausado muestra segundos LIVE congelados, banner «esperando confirmación de transmisión» y origen afectado sin exponer datos sensibles.
- Si un streamer abandona la temporada, se mantiene nación e historial, entra política de reasignación de asiento/binding auditada; no transfiere usuarios a otro canal silenciosamente.
- No conceder notoriedad visual competitiva por donaciones; patrocinio cosmético sin efectos y con consentimiento/moderación.

## 6. Sonido, K-0 y transmisión cruzada

- Guion y cues de K-0 son producidos por servidor tras eventos confirmados; texto y subtítulos se envían como datos.
- El audio de K-0 es configurable por output para impedir el eco o doble TTS si el streamer ya usa una mezcla externa. No publicar audio/captura del streamer A en B sin autorización explícita y revisión de política.
- Cada salida OBS elige niveles audio y fuente local; nunca se extrae audio remoto como parte de la autoridad de juego. Si TTS no funciona, subtítulos obligatorios y flujo normal.
- Versionar pistas, licencias comerciales, idioma y variantes. La música no debe enmascarar resultado ni dar ventaja de información a un canal.

## 7. Prueba de arte y aceptación UX

- UX-M01: tres streamers sin ayuda configuran URL OBS desde tres PCs y entienden su propia nación.
- UX-M02: 0 espectadores y 45 sprites visibles en vertical a 30 FPS reales, con subtítulos, sin tapar los cinco hitos.
- UX-M03: A pierde overlay; B/C continúan y A regresa sin recibir escenas antiguas como actuales.
- UX-M04: dos espectadores de canales distintos reciben instrucciones y agradecimientos exclusivamente en su canal.
- UX-M05: jugadores entienden diferencia OFFLINE vs OBS_DISCONNECTED vs RPS_GLOBAL_PAUSED.
- ART-M01: siluetas de 3 facciones identificables en monocromo y 1×; K-0 reconociblemente cyborg.
- ART-M02: 3 style frames (Paleolítico, Industrial, Espacial) x 3 culturas, contrastados en 360×640 y 640×360.
- ART-M03: 4 orientaciones y 9 acciones del contrato original solo se aprueban cuando estén dibujadas, animadas y comprobadas, no por describirlas.

## 8. Orden de producción con máximo ROI

1. Wireframes reales de sala de campaña, invitación, conexión de proveedor, streamer portal y cockpit OWNER.
2. Una escena vertical/horizontal con Micelios, Rúnicos y Ferrinos + K-0 cyborg, HUD y estado de conexión.
3. Sprite sheet mínimo de 5 profesiones y 10 familias básicas de Paleolítico.
4. Una elección, un Consejo y una transición, con escenas y subtítulos en los tres outputs.
5. Biblioteca de tiles/animaciones y skins por era restante después de validar lectura y desempeño de audiencia.
