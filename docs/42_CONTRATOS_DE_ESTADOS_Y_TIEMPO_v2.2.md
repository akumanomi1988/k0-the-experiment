# 42 — Contratos temporales, prioridades y semántica determinista

**Normativo para diseño.** Concreta escenarios de frontera y orden de eventos; no implementa el motor.

## Relojes separados

| Reloj | Unidad | Avanza con LIVE confirmado | Avanza offline | Usos |
|---|---|---|---|---|
| `UtcWallClock` | ms UTC | Sí | Sí | Timestamps, 2 h de actividad humana, periodos diarios/semanales |
| `NationEconomyClock` | segundos de simulación | 100 % de tiempo real | 20 % de tiempo real | Producción, mantenimiento, autoplanner |
| `NationLiveClock` | segundos LIVE | Sí | No | Elecciones, Consejo, prioridades, torneos, penalización territorial |
| `SeasonClock` | secuencia lógica | Sí | Según evento de sistema | Orden de commits, snapshots y desempates |
| `PresentationClock` | frames | Sí | Sí cuando render está activo | Animación/subtítulos, jamás decide recursos |

La señal de proveedor incierta NO se interpreta como LIVE. Los temporizadores de elección/voto/torneo se congelan, la economía usa perfil conservador offline cuando se confirma desconexión y, en `UNCERTAIN`, aplica la política de seguridad del capítulo 29 hasta recuperar señal. Un reinicio de OBS no cambia tiempos de economía ni estado competitivo.

## Orden lógico de un tick de 5 segundos (enmienda v2.3)

Prevalece el orden exacto de [doc 64](64_RELOJES_EVENTOS_Y_CONTRATOS_v2.3.md): entrada LIVE/Inbox idempotente → comandos y papeletas válidos → cierres de votos/torneos → comida/economía/XP → obras/investigación/misiones → hitos/era → ganador/maravillas → commit y deltas. El tick se particiona por fronteras reales; recibidos exactamente en el límite LIVE de cierre son rechazados. Una elección pausada **no** tiene deadline UTC absoluto fijo; computar su tiempo restante en NationLiveClock.

Se deriva una sola vez economyDelta a partir del intervalo real y el multiplicador 100 %/20 %. En RPS/batalla, CompetitionLiveClock avanza solo cuando las tres naciones están LIVE; pérdida de una congela tiempo y resultado global, sin votos ni sanciones ficticios.

## Identidad, experiencia y estados

- `citizenId` es específico de `(season,nation,provider,providerUserId)`; una persona puede tener ciudadanos diferentes entre canales, nunca sumar votos en una nación por reintentos del mismo evento.
- Descansar no impide votar; sí impide contribuir producción humana sin renovar `!active` o repetir `!work` válido tras cooldown.
- La profesión no cambia durante temporada. Los niveles 3, 7, 12 permiten una habilidad por tramo; ausencia de selección = no perk, no elección automática.
- Avance de era cambia la etiqueta del oficio, nunca la profesión ni su XP. Los edificios permanecen en el mapa; los antiguos reciben factor de eficiencia cuando corresponde.
- Ningún evento estético, lectura de nombre, voz TTS, caída de FPS o reproducción atrasada de HUD modifica estado autoritativo.

## Reglas de salida de eventos múltiples

Si se alcanzan a la vez hitos, una elección y una obra, las mutaciones se confirman primero; la presentación prioriza victoria > era > resultado de voto > torneo > hambre > cosmética. Cola narrativa no altera orden de commits. Si un cronómetro reanuda tras 5 horas OFFLINE, conserva exactamente los segundos LIVE pendientes, sin «rellenar» votos ficticios.

## Ejemplos de aceptación

- Voto a `close - 1ms`: aceptable si válido y autenticado; a `close`: rechazado; mismo `sourceKey` repetido: un solo efecto.
- Desconexión con 47s restantes: mostrar 47s hasta confirmar nuevo LIVE; no avanzar si OBS sigue reproduciendo vídeo pregrabado.
- Usuario `!active` dos veces en 10s: primer comando renueva 2h, segundo no; chat casual no hace nada.
- Almacén lleno justo antes de un gasto: liberar capacidad y producir en siguiente segmento válido, no anticipar recursos inexistentes.
- Fin de temporada en tick concurrente con patrocinio: si el cierre se confirma primero, el patrocinio no compra ya un artículo de temporada cerrada; su evento se trata según política verificable sin perder trazabilidad.
