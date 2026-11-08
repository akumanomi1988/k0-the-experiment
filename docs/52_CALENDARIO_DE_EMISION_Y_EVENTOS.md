> **Regla vigente:** cada streamer puede emitir en horarios distintos; la economía LIVE/OFFLINE es local a su nación, y los torneos compartidos requieren tres LIVE simultáneos y congelación global en desconexión. El plan de 4h es ejemplo editorial, no reloj obligatorio. [Especificación vigente](ESPECIFICACION.md).

**Temporada objetivo de 45–90 días naturales.** El arranque multistreamer requiere tres canales autorizados, **no** tres directos simultáneos. Un torneo pausado por ausencia de un LIVE vence a las **72 h UTC** sin sanciones. El abandono definitivo confirmado congela toda la temporada y provoca cancelación a los **7 días UTC**, salvo retorno del **mismo responsable primario** aprobado por OWNER y reautorizado **antes** del vencimiento. No se genera producción retroactiva ni se reabren torneos ya cancelados.

# 52 — Operación editorial, calendario de emisión y ritmo de espectáculo

## Objetivo

La simulación puede existir offline, pero el espectáculo requiere sesiones programadas. Se permite que una nación acumule más horas LIVE y avance más; no se compensan horas de emisión. Mostrar horas LIVE por nación y no prometer actividad cuando no está confirmada.

## Secuencia recomendada de una sesión de cuatro horas

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

## Frecuencias máximas, no cuotas mínimas

- RPS según planificación del operador; no se ejecuta «porque faltan espectadores» sin las tres fuentes LIVE.
- Batalla automática, por defecto, máximo una por 24h LIVE de campaña; no se superpone con RPS ni con una elección crítica.
- `catchup_challenge` máximo dos por nación/temporada y solo si retraso ≥2 eras, duración 30 minutos LIVE. `resource_storm` máximo una cada 12h LIVE. `wildlife_parade` máximo una cada 4h LIVE; sin efectos de estado. `wonder_festival` máximo una cada 24h LIVE con elegibilidad real.
- Si hay múltiples cues, orden: ganador de temporada, transición era, resultados de elecciones, incidente proveedor, torneo, misión y cosmética. No bombardear al espectador con notificaciones cada tick.

## Dependencias de producción

La campaña necesita tres fuentes de atribución distintas, que pueden ser tres canales del mismo proveedor. Una sola señal de vídeo puede mostrar las tres naciones, pero **un único chat no puede emitir acciones para las tres** según la regla actual. Publicación de multicámara y mezcla de chat entre plataformas quedan sujetas a permisos. Ninguna programación justifica una conversión de regalos no verificada.

## Runbook

**Pre-LIVE:** comprobar conexión por cuenta, salud del token y permisos, reloj de cada nación, versión de reglas, snapshots, moderación, audio/OBS, modo seguro y escena de contingencia. **Durante:** vigilar Inbox, votos y contadores LIVE, colas, recursos, latencia, TTS, logs de moderación y reloj UTC. **Post-LIVE:** congelar relojes, publicar resumen solo de estados confirmados, revisar eventos pendientes, respaldos y notas de incidente. Cambio crítico de reglas o credenciales requiere operador autorizado y registro de auditoría.
