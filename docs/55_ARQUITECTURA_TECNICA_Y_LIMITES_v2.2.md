# 55 — Arquitectura técnica de producción propuesta

**No es código ni infraestructura creada.** Se mantienen las tecnologías ya discutidas: motor autoritativo .NET/C#, PostgreSQL como almacenamiento transaccional, entrada por adaptadores de streaming, API/SignalR de solo proyección, cliente Phaser/React para OBS.

## Responsabilidades y límites

| Subsistema | Responsabilidad | No debe hacer |
|---|---|---|
| `CampaignConfiguration` | Facciones, temporada, reglas inmutables y bindings | Cambiar estado de partida en directo sin aprobación |
| `ProviderIngress` | Validar origen, evento, permisos, idempotencia | Crear recursos o acreditar oro |
| `NationSimulation` | Tick de 5s, economía, ciudadanía, obras, investigación | Renderizar sprites, llamar APIs externas durante transacción |
| `PoliticalScheduler` | Elecciones y Consejos con reloj LIVE | Abrir dos votaciones políticas incompatibles |
| `CompetitionEngine` | RPS y batallas programadas | Activar ataque espontáneo |
| `ContributionLedger` | Aportaciones verificadas, devoluciones y deuda | Confiar en texto de chat |
| `ShowDirector` | Cues autorizados y modulación narrativa | Elegir ganador o cambiar balance |
| `ProjectionAPI` | DTO público/versionado y snapshots; slug público distinto del UUID SQL | Exponer identificadores y secretos de proveedor |
| `OverlayClient` | Render 2D/LOD, animación y subtítulos | Autorizar gastos/posiciones económicas |
| `OperatorConsole` | Control auditado/pausas/escena segura | Saltarse restricciones del motor |

## Consistencia y concurrencia

Escritor único lógico por nación, más arbitraje global por temporada para primera maravilla y ganador. Inbox y Outbox permiten idempotencia y entrega eventual; los deltas de HUD son proyección, no verdad. Todas las mutaciones económicas usan ledger, locks/versiones y commit atómico. Baseline: PostgreSQL 16+ como referencia del SQL propuesto; hay smoke tests de DDL 001–003 en CI, pero no upgrade de datos históricos ni recuperación del motor. Cada entrada lleva secuencia para replay; el RNG estable depende de seed y contador, no de reloj ni entorno.

## Entidades clave

`Campaign`, `Season`, `Nation`, `ChannelBinding`, `ProviderIdentity`, `Citizen`, `CitizenSkill`, `ResourceBalance`, `ResourceLedger`, `GoldDebt`, `Building`, `TechnologyProgress`, `MilestoneProgress`, `MissionPeriod`, `GovernmentElection`, `StrategicBallot`, `RpsRound`, `CompetitionEvent`, `WonderClaim`, `NarrationCue`, `AuditLog`, `Snapshot`, `Inbox`, `Outbox`. V2.2 introduce además estados conceptuales `GarrisonUnit`, `AutomatedBattle`, `CosmeticSponsorship`; **el DDL base y los anexos `architecture/002_extensiones_diseno_v2.2.sql` y `architecture/003_integridad_v2.2.sql` superaron smoke tests en PostgreSQL 16 vacío; no existe migración ejecutada sobre datos preexistentes ni motor integrado**. Ninguna nueva entidad necesita un microservicio propio en fase 1.

## API y presencia

El cliente OBS solo consume snapshots y deltas con secuencia; en reconexión solicita snapshot base y reanuda del último confirmado, nunca inventa recursos. Eventos de chat no se envían desde frontend como autoridad. API admin se protege de forma distinta de API overlay; los endpoints declarados en `contracts/openapi.v2.yaml` incluyen lecturas de guarniciones, batallas y patrocinios, pero siguen siendo contratos de diseño sin endpoints ejecutados; módulos pendientes en `contracts/CONSOLIDATION_GAPS_V2_2.md`. El backend no publica directamente tokens de proveedor al cliente.

## Despliegue de referencia (no ejecutado)

Un backend .NET modular + worker de simulación + PostgreSQL gestionado + UI overlay y consola, con monitorización de señales LIVE, logs estructurados y backups. No añadir colas distribuidas, CQRS completo o contenedores por facción sin datos de carga que los justifiquen. Separar proceso web y worker cuando rendimiento lo exija; diseñar frontera desde el principio para mantener determinismo y evitar caídas de FPS que alteren estado.

## SLO propuestos, no logrados

Tick de 5s con CPU interna objetivo de 50 ms por nación a carga de referencia; P95 de Inbox→aplicación <1s; P95 delta visible <2s; escena 30 FPS; RPO/RTO solo se fijan tras ensayar backups y recuperación. La alta disponibilidad de un proveedor no se presume. Meter 100k ciudadanos en DB no implica 100k entidades renderizadas.

## Contratos de diseño ampliados y prueba de DDL

El fichero `contracts/openapi.v2.yaml` se ha ampliado con recursos de lectura de guarnición y batalla, agenda de combate y moderación de patrocinios (**info.version 2.2.0, contrato de diseño, no rutas desplegadas**). El protocolo público de eventos está tipado en `contracts/signalr_events.v2.2.schema.json` con fixtures en `contracts/examples/`.

Los tres scripts SQL de `architecture/` cuentan con una prueba en PostgreSQL 16 aislado que protege los holds ordinarios y guarniciones; **no** demuestra idempotencia del motor, idempotencia concurrente de todas las transacciones, recuperación real ni una migración sobre datos históricos. Consultar `contracts/CONSOLIDATION_GAPS_V2_2.md`.
