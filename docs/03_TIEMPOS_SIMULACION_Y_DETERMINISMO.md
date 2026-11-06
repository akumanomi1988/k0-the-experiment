# 03 — Relojes, scheduler, replay y estados

## Relojes tipados
- `UtcClock`: tiempo físico, monotónico verificado contra reloj de sistema; expiraciones de ciudadanos (+7200s), caducidades de OAuth, misiones UTC. Se almacena la fecha absoluta además del evento.
- `NationLiveClock`: integra exclusivamente segundos `LIVE_CONFIRMED`; elección 3600s, segunda vuelta 180s, proyecto 600s, prioridad 300s, RPS 90s, bonus prioridad 5400s. Se congela en `UNCERTAIN`, `PAUSED` o `OFFLINE_CONFIRMED`.
- `NationEconomyClock`: 1 segundo equivalente en LIVE, 0,2 en OFFLINE/UNCERTAIN; sin doble aplicar al recuperar.
- `NationActivePenaltyClock`: avanza 1s solo en LIVE; una región penalizada consume exactamente 1800s activos; NUNCA consume segundos fuera de emisión.

No sumar segundos a ciegas: cada segmento `[lastProcessedUtc, nowUtc)` se particiona por cambios de estado LIVE, expiraciones de trabajadores, cierre de sesiones y vencimientos de comandos. La producción y experiencia se calculan en el mismo segmento. Un comando entra al tick siguiente; `receivedUtc` decide si se admite en una votación abierta cuando se recibió durante intervalo. Eventos con `providerTimestamp` fuera de tolerancia se ponen en cuarentena.

## Orden canónico por tick
1. Consumir `Inbox` autenticado y deduplicado y ordenar por `ingestSeq` (no reloj del proveedor cuando contradiga secuencia persistida).
2. Aplicar cambios de `LIVE` auditados con sello de instante.
3. Aplicar comandos de ciudadanos y papeletas llegadas antes del cierre.
4. Cerrar ventanas exactas de voto cuyo LiveClock alcanzó su deadline; una papeleta en instante de cierre se rechaza.
5. Aplicar disponibilidad de trabajadores (segmentada); gastos de comida y mantenimiento; producción limitada a capacidad; XP.
6. Resolver planificación automática, avances de construcción, tecnologías y misiones.
7. Reconocer hitos únicos y transición de era (solo LIVE). La entrada a la última era genera evento global terminal.
8. Registrar estados, ledger, outbox y checksum antes de notificar clientes. Actualizar snapshots cada 60 segundos de economía o 100 eventos críticos, lo que suceda primero.

## Idempotencia y replay
`sourceEventKey=SHA256(provider + bindingId + originalEventId + eventType)`; `commandId` se asigna una vez tras inbox. `rulesetHash`, `contentHash`, `seasonSeed`, `engineVersion`, `remainderVectors` se guardan en snapshot. RNG `sha256-counter-64-v1`: `sha256(seed||domain||counter_be64)`, valor uniforme por rechazo para evitar sesgo (`limit = floor(2^64/n)*n`). Counters separados por dominio (`elections`, `tournaments`, `map`, `events`) y nación; este detalle evita cambios de resultados al añadir más narración.

Replay desde snapshot requiere mismo runtime numérico y mismo orden de eventos/segmentos. Un bug de versión no se corrige editando transacciones pasadas: abrir migración/compensación con evento auditable.

## Caída larga
Hasta siete días de interrupción se integra economía offline exactamente por segmentos y checkpoints. A partir de siete días el sistema entra en `NEEDS_OPERATOR_REVIEW` y no aplica catch-up adicional hasta que un operador resuelva y audite la decisión. Ninguna transición de era ocurre automáticamente en catch-up. Las ventanas electorales quedan congeladas si no hay LIVE confirmado.

## Inicio y fin de temporada
`DRAFT → PREPARED → RUNNING → COMPLETED → ARCHIVED`, con derivaciones `PAUSED`, `RECOVERY_REQUIRED`. Start a hora UTC única y seed inmutable. Las tres naciones arrancan en Paleolítico en el mismo commit. En cuanto `EraAdvanced` de una nación entra en Interestelar, un `SeasonWinnerClaim` atómico fija ganador, finaliza la producción competitiva y prepara ceremonia de cierre; empate mismo instante resuelto por secuencia de commit, no aleatoriedad. Estadísticas, historia, prestigio y logros persisten; economía no se transfiere.
