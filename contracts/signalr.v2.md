# SignalR projection protocol v2.0

Hub `/hubs/v2/chaos` sends `NationSnapshotV2`, `NationDeltaV2`, `CueV2`, `VoteViewV2`, `TournamentViewV2` to authorization-filtered groups. Every message is `(schemaVersion='2.0.0', seasonId, nationId?, sequence, UTC, payload)`. Never broadcast `providerUserId`, OAuth tokens, raw chat or entire ledger to public groups.

On reconnect caller supplies `lastSequence`; if the server can replay all events from that point, it emits ordered deltas followed by `SyncCompleted`; otherwise `SnapshotRequired` asks client to call snapshot API and resume on `sequence`. Delta event IDs are idempotent; the client must ignore `sequence <= lastAppliedSequence`, and if a gap is detected, stop animation extrapolation until snapshot. Vote views for RPS expose **only total ballot count before closure**, not distribution. Chat writeback errors do not roll back game state.

Bandwidth: delta max 2 Hz/nation by default, high-frequency animation simulated in Phaser. JSON payload cap 64 KiB/frame; coalesce noncritical visuals only. Protocol breaking changes require `/v3` hub and explicit client version handshake.

## Extensión tipada v2.2 (contrato, no hub ejecutado)

Las notificaciones públicas `garrison.changed`, `battle.scheduled`, `battle.result` y `cosmetic.acknowledgement` tienen ahora esquema machine-readable en [signalr_events.v2.2.schema.json](signalr_events.v2.2.schema.json) y ejemplos en [examples/](examples/). El envelope declara `schemaVersion='2.2.0'`, `seasonId`, `nationId`, `sequence`, `serverUtc` y `payload`.

Los cambios anteriores son aditivos al protocolo 2.0; **no** implica una implementación real del hub. Antes de activar la visualización, validar los gaps de secuencia, autorización de grupos, tamaños y borrado de datos personales. Ningún payload contiene IDs de proveedor o mensajes sin moderar.
