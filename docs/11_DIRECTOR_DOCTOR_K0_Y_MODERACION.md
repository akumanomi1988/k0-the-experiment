# 11 — Doctor K-0, narrativa y control de actos

Doctor K-0 es un cyborg científico físico dentro de las tres representaciones del mundo, con rostro mecánico, un ojo óptico, extremidades de ingeniería y cápsula de voz, nunca mascota blanda o Corálido. Su voz es sarcástica/provocadora, neutra respecto a las facciones y nunca utiliza insultos discriminatorios, burlas a donantes por no pagar ni afirmaciones falsas sobre apoyo económico.

## Arquitectura del show
`ShowDirector` decide eventos dentro de whitelist y cooldown; genera `Cue` tipado (`era_ready`, `government_open`, `government_result`, `priority_open`, `strategic_available`, `strategic_result`, `tournament_start`, `tournament_result`, `food_crisis`, `storage_full`, `season_completed`, `safe_idle`). `NarrationService` produce texto desde plantillas primero; LLM opcional solo reescribe tonos dentro de plantilla permitida, no crea reglas, saldos, ganadores ni acciones. `TTS` reemplazable con caché por hash de frase y voz; si falla, subtítulo y sonido local. Estado de narración `PENDING → READY → PLAYING → DONE | SKIPPED`, y límite 1 cue prioritario cada 20 segundos con cola máxima 20, descartando cosméticos viejos y nunca eventos financieros.

## Moderación y datos personales
DisplayName se sanitiza (control chars, URLs, PII básica y palabras prohibidas) antes de entrar a sprite, placa o speech; retener el identificador estable internamente con seudonimización/criptografía. Comandos y regalos no permiten inyectar instrucciones al LLM. No envíe chat bruto a LLM salvo consentimiento/configuración aprobada; preferir datos agregados. Perfiles, stats y nombres borrables/redactables sin romper ledger contable. Errores de comunicación a chat son *best effort*, no deben provocar reintento de transacción de juego.

## Plantillas canónicas
- `join`: «¡{displayName}! Bienvenido al experimento. Elige oficio: food, wood, mine, build o research con !work.»
- `profession_locked`: «Profesión fijada esta temporada. Usa !active para volver al trabajo.»
- `era_ready`: «La ciencia empuja a {nationName} al límite... esperaremos al directo para cambiar de era.»
- `vote_open`: «Tres obras financiables. Solo una será aprobada. ¡Tenéis diez minutos de emisión!»
- `season_end`: «El experimento tiene ganador: {nationName}. Todo queda registrado. No hay reinicio de memoria histórica.»

El operador tiene siempre botón `MuteNarration`, `PauseSource`, `CancelEvent`, `SafeScene`, `EmergencyStop`. Todas las acciones quedan registradas con actor, motivo y timestamp.
