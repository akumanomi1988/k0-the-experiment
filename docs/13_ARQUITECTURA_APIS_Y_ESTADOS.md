> **Documento de detalle.** La fuente normativa vigente es [ESPECIFICACION_MAESTRA.md](../ESPECIFICACION_MAESTRA.md). Este capítulo no prevalece ante una regla corregida en la especificación; versiones anteriores en Git.

> **Enmienda normativa v2.3 (multistreamer distribuido):** backend .NET compartido en hosting central; tres Browser Sources en PCs diferentes, un escritor por nación, Inbox/Outbox y global SeasonArbiter. No servidores locales ni P2P. [Especificación vigente](../ESPECIFICACION_MAESTRA.md).

# 13 — Arquitectura modular, dominio y APIs

## Despliegue de referencia
Monolito modular en .NET 10 con tres procesos lógicos `ApiHost`, `SimulationWorker` y `ConnectorWorker` (en MVP pueden ser un ejecutable con HostedServices), PostgreSQL, SignalR, React/TypeScript y Phaser (versión sujeta a prueba de OBS CEF). No usar Kafka, RabbitMQ, Redis, Kubernetes ni event sourcing completo hasta demostrarse necesidad. Inbox/Outbox PostgreSQL permite idempotencia y recuperación.

## Módulos y dependencias
`IdentityAndBindings` (asignación canal y cuentas), `Citizens` (usuarios/oficios/XP), `Simulation` (scheduler, clocks, work aggregation), `Economy` (balances/consumo/ledger), `Buildings` (autoplanner y construcción), `History` (hitos/eras), `Politics` (elección y prioridad), `StrategicCouncil` (holds/votos), `Competitions` (RPS/sanciones), `MissionEngine`, `ShowDirector`, `PlatformAdapters`, `ReadModels` y `Operator`. Cada módulo expone comandos y eventos, no acceso directo a repositorio de otro módulo. Core no importa Phaser ni SDK de plataforma. IDs UUID y referencia a `season_id + nation_id` en cualquier agregado perteneciente a nación.

## Consistencia
`Inbox` guarda el raw mínimo + `sourceKey` único; actor lógico single-writer por nación y lock de exclusividad en la DB; las operaciones compartidas de maravillas/ganador tienen transacción global y lock de temporada. `Outbox` publica evento con id estable tras commit; duplicaciones de emisión no afectan estado. Ante despliegue horizontal posterior usar lease-epoch/fencing antes de levantar otro escritor. Nunca ejecutar dos instancias con escritores sin fencing. Recursos en milésimas, oro en unidades enteras separadas.

## API y SignalR
Contratos en `contracts/openapi.v2.yaml`, `contracts/normalized_event.schema.json`, `contracts/nation_delta.schema.json`, `contracts/channel_binding.schema.json`, `contracts/ruleset.schema.json`; JSON v2 con `schemaVersion`, `eventId`, `seasonId`, `nationId`, `sequence`, UTC ISO8601. `/api/v2/operator` exige acceso privilegiado; `/api/v2/public` ofrece únicamente proyecciones. SignalR grupos `season:{id}:nation:{id}:public`, `season:{id}:operator` y `output:{id}`; no publicar IDs de proveedor ni texto raw. Clientes reconectan enviando `lastSequence`, recuperan snapshot y deltas posteriores; si hueco fuera del retention, solicitan snapshot completo.

## Contratos de error
Respuesta estándar `{code,message,correlationId,retryable}`; códigos predecibles `NOT_REGISTERED`, `PROFESSION_LOCKED`, `VOTE_NOT_OPEN`, `OUT_OF_WINDOW`, `EVENT_DUPLICATE`, `SOURCE_UNAUTHORIZED`, `BALANCE_HOLD_CONFLICT`, `GOLD_RULE_DISABLED`, `LIVE_NOT_CONFIRMED`, `CONTENT_HASH_MISMATCH`, `RULESET_INVALID`, `RUNNING_SEASON_IMMUTABLE`. Prohibido devolver secretos o payload de chat bruto.
