> **Documento de detalle.** La fuente normativa vigente es [ESPECIFICACION_MAESTRA.md](../ESPECIFICACION_MAESTRA.md). Este capítulo no prevalece ante una regla corregida en la especificación; versiones anteriores en Git.

# 20 — UX de jugador, escenas OBS y panel de operador

## Escenas públicas
- **UniverseOverview**: tres naciones en miniatura, era, barra 0–100 y estado LIVE, ganador o empate; solo metadatos agregados compartibles.
- **NationWorldVertical**: mundo 66 %, HUD superior 14 %, HUD inferior 20 %; zona de cámara sigue obras/visitas de K-0, viewport lógico 360x640.
- **NationWorldHorizontal**: 73 % viewport, 27 % panel lateral, 640x360 lógico; componentes reposicionados, no escalados arbitrariamente.
- **ElectionOverlay**: tres candidatos, tiempo LIVE restante, recuento total y porcentajes permitidos después de cierre.
- **StrategicCouncilOverlay**: tres alternativas, costes ordinarios y oro, aviso «opcional/estético», timer 10min y estado de reserva.
- **TournamentOverlay**: tres equipos, votos totales por nación, ocultación de opciones hasta cierre, puntuación de duelos por parejas y penalizaciones activas.
- **SeasonFinale**: ganador, estadísticas y museo con historial sin saldo de oro como moneda útil.

## Controles de operador
Login MFA con rol; tabla de cuentas asociadas (provider/channel, LiveHealth, capabilities, token TTL con secretos ocultos), reglas hash, versión de cada adaptador, simulación clock, health DB y outbox, backlog de eventos, contador de reintentos, gastos TTS. Acciones: PREPARE, START, PAUSE, RESUME, SCHEDULE_EVENT, SCHEDULE_TOURNAMENT, CANCEL_VOTE (motivo), SAFE_SCENE, MUTE_K0, EMERGENCY_STOP, ARCHIVE, EXPORT_AUDIT. Toda acción exige idempotencyKey, confirmación UI cuando tiene efecto económico y log; no existe botón para «dar oro» en producción.

## Onboarding para monetizar a otros creadores
Primera edición de producto es un solo creador/campaña con exactamente tres facciones. Cuando se comercialice, añadir `Tenant`, billing/licencias, aislamiento de credenciales por tenant, cuota de canales, RLS/particionamiento si hay evidencia. No diseñar cross-tenant billing en MVP. Cada creador puede escoger qué tres cuentas conectar, sin alterar los oficios ni las identidades de facción.

## Accesibilidad y degradación
Narración siempre subtitulada; no comunicar éxito únicamente por color, feedback de comandos válido en HUD incluso si la plataforma no autoriza responder al chat. Reducir efectos luminosos y FPS en OBS bajo carga sin tocar tick backend. El lector de pantalla del panel de operador accede a etiquetas y countdown; overlays públicos son imágenes audiovisuales pero acompañados de panel textual.
