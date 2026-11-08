# 03 — Relojes, scheduler, replay y estados

## Relojes tipados
- `UtcClock`: tiempo físico, monotónico verificado contra reloj de sistema; expiraciones de ciudadanos (+7200s), caducidades de OAuth, misiones UTC. Se almacena la fecha absoluta además del evento.
- `NationLiveClock`: integra exclusivamente segundos `LIVE_CONFIRMED`; elección 3600s, segunda vuelta 180s, proyecto 600s, prioridad 300s, bonus prioridad 5400s. Se congela en `UNCERTAIN`, `PAUSED` o `OFFLINE_CONFIRMED`.
- `CompetitionLiveClock`: global por evento programado, avanza 1s solo cuando las tres naciones están LIVE confirmadas; RPS 90s y descansos 30s; congelación conjunta ante cualquier caída.
- `NationEconomyClock`: 1 segundo equivalente en LIVE, 0,2 en OFFLINE/UNCERTAIN; sin doble aplicar al recuperar.
- `NationActivePenaltyClock`: avanza 1s solo en LIVE; una región penalizada consume exactamente 1800s activos; NUNCA consume segundos fuera de emisión.

No sumar segundos a ciegas: cada segmento `[lastProcessedUtc, nowUtc)` se particiona por cambios de estado LIVE, expiraciones de trabajadores, cierre de sesiones y vencimientos de comandos. La producción y experiencia se calculan en el mismo segmento. Un comando entra al tick siguiente; `receivedUtc` decide si se admite en una votación abierta cuando se recibió durante intervalo. Eventos con `providerTimestamp` fuera de tolerancia se ponen en cuarentena.

## Orden canónico por tick (enmienda v2.3)

**Fuente normativa:** [64 — Relojes y eventos](64_RELOJES_EVENTOS_Y_CONTRATOS_v2.3.md). Durante cada subsegmento se procesan: (1) eventos autenticados con ingestSeq y cambios LIVE; (2) comandos/papeletas recibidos antes del límite del reloj LIVE; (3) cierres de voto/competición vencidos; (4) alimentación, economía, XP; (5) edificios, investigación, misiones; (6) hitos y transición de era; (7) arbitraje global de ganador/maravillas; (8) commit de estado/ledger/outbox, y publicación posterior. Las subfronteras temporales se preservan para un replay exacto.

**Economía:** el delta efectivo es tiempo UTC segmentado × factor LIVE 100 % u OFFLINE/UNCERTAIN 20 % una sola vez. No se vuelve a multiplicar al calcular output ni XP. La aceptación de un comando (ACK) puede preceder al siguiente tick productivo; la mutación de economía no promete latencia inferior al tick de 5 s.

**Competición:** RPS y batalla automática usan CompetitionLiveClock global solo con tres LIVE confirmados; ante caída de una nación se congela en las tres.

## Idempotencia y replay
`sourceEventKey=SHA256(provider + bindingId + originalEventId + eventType)`; `commandId` se asigna una vez tras inbox. `rulesetHash`, `contentHash`, `seasonSeed`, `engineVersion`, `remainderVectors` se guardan en snapshot. RNG `sha256-counter-64-v1`: `sha256(seed||domain||counter_be64)`, valor uniforme por rechazo para evitar sesgo (`limit = floor(2^64/n)*n`). Counters separados por dominio (`elections`, `tournaments`, `map`, `events`) y nación; este detalle evita cambios de resultados al añadir más narración.

Replay desde snapshot requiere mismo runtime numérico y mismo orden de eventos/segmentos. Un bug de versión no se corrige editando transacciones pasadas: abrir migración/compensación con evento auditable.

## Caída larga
Hasta siete días de interrupción se integra economía offline exactamente por segmentos y checkpoints. A partir de siete días el sistema entra en `NEEDS_OPERATOR_REVIEW` y no aplica catch-up adicional hasta que un operador resuelva y audite la decisión. Ninguna transición de era ocurre automáticamente en catch-up. Las ventanas electorales quedan congeladas si no hay LIVE confirmado.

## Inicio y fin de temporada
`DRAFT → PREPARED → RUNNING → COMPLETED → ARCHIVED`, con derivaciones `PAUSED`, `RECOVERY_REQUIRED`. Start a hora UTC única y seed inmutable. Las tres naciones arrancan en Paleolítico en el mismo commit. En cuanto `EraAdvanced` de una nación entra en Interestelar, un `SeasonWinnerClaim` atómico fija ganador, finaliza la producción competitiva y prepara ceremonia de cierre; empate mismo instante resuelto por secuencia de commit, no aleatoriedad. Estadísticas, historia, prestigio y logros persisten; economía no se transfiere.
