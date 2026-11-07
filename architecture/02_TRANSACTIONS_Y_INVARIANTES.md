# 02 — Protocolos de transacción críticos

## Modelo de escritura
Un `NationWriter` consume Inbox por `ingest_seq` bajo exclusividad de `(season_id,nation_id,writer_epoch)`. Para escalar usar fencing DB; un `writer_epoch` viejo no puede hacer commit después de que otro escritor haya adquirido lease. Un mismo comando tiene `source_key` globalmente único y `event_id` persistido; se marca `APPLIED` en la misma transacción que las mutaciones. `Outbox` se inserta antes del commit y se puede publicar repetidamente sin volver a ejecutar el dominio.

## Cierre de votación estratégica
Transacción con orden de bloqueo fijo: `seasons` → `nations` → `votes` → `nation_resource_balances` ordenadas por `resource_id` → `buildings`. Releer `vote.state=OPEN` y deadline LiveClock, computar votos más recientes válidos, elegir opción por mayoría y RNG registrado, comprobar hold vector y saldos. Gastar el vector **del ganador**, liberar reserva completa, crear instancia de obra `QUEUED`, insertar entradas de ledger `BUILD_COST` por `cause_id = vote.id` con unique y publicar `StrategicApproved`. Cambiar vote a RESOLVED. Si un reintento encuentra `RESOLVED`, devolver resultado existente sin recobrar. Las reservas del Consejo son solo de recursos ordinarios: ningún reverso de oro puede invalidarlas. Si hay una anomalía de saldo o reserva ordinaria, no confirmar obra ni gasto; registrar el conflicto, mantener trazabilidad y llevar la operación a recuperación antes de reintentar.

## Reversión de contribución y deuda cosmética
La reversión afecta exclusivamente a la cuenta interna de oro y a los reconocimientos cosméticos. No bloquear ni cancelar Consejos: desde v2.2 solo reservan recursos ordinarios. Transacción: bloquear la nación y el saldo de oro, identificar la aportación acreditada, impedir doble reverso por clave idempotente, descontar como máximo el oro disponible y registrar el resto en `gold_debt`. Insertar asiento compensatorio y estado `reversed` de patrocinios vinculados cuando corresponda. Un reverso nunca puede producir oro negativo ni modificar edificios, votos, hitos o ganador.

## Creditar oro en deuda
Una aportación adicional verificada de 12 gold con deuda 7 produce `DebtSettled=7`, oro disponible `+5`. Ambas entradas pertenecen a misma contribución crediticia y se reconcilian por un identificador único y una compensación explícita; **no** registrar ficticiamente `+12` en stock si solo quedan +5 disponibles. El ledger de obligación registra el importe total respaldado y la deducción para deuda. No hay emisión sin evidencia de origen.

## Gasto básico y overflow
El AutoPlanner calcula coste vectorial, bloquea saldos, reserva/disminuye el saldo una sola vez, registra `BUILD_COST` con `causeId=constructionId`, guarda `ConstructionQueued`. Si falta recurso, no cambia nada y deja intención `WAITING_RESOURCES` sin bloquear stock. Las misiones y producción no pueden superar cap; `overflow` se mide pero no se acumula en balances. Los recursos `knowledge` usan las mismas milésimas y cap lógico, no `gold`.

## Ganador y maravilla
`SeasonWinnerClaim` UNIQUE por temporada. `INSERT ... ON CONFLICT DO NOTHING` bajo lock de temporada después de evento `EraAdvanced final` gana el primer commit. Si ya hay winner no iniciar nuevos procesos políticos. `WondersGlobal` UNIQUE por `(season_id,wonder_id)`, y se concede solo si una obra está COMPLETED al intentar insertar; edificio perdedor sigue visible como monumento normal y se notifica. Si hay caída entre commit y WS, Outbox asegura notificación eventual.

## Test de estado imposible
- No duplicar el recurso por replay de Inbox.
- No votar con ciudadano de nación distinta (FK compuesta).
- No permitir reservas de oro en ninguna votación estratégica o maravilla de v2.2.
- No aceptar edición de `rulesetHash` durante temporada RUNNING.
- No mutar un proyecto de otro `NationId` por UID existente.
- No transformar reverso ya creditado en cancelación silenciosa.
