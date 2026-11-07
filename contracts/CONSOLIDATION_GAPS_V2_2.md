# Matriz de consolidación de contratos v2.2

**Estado: PENDIENTE DE IMPLEMENTACIÓN Y TEST.** Este documento identifica incompatibilidades/gaps concretos entre `architecture/001_schema_v2.sql`, `architecture/002_extensiones_diseno_v2.2.sql`, `contracts/openapi.v2.yaml`, `contracts/signalr.v2.md` y `contracts/extensiones_lectura_v2.2.md`. No sustituye las definiciones existentes ni autoriza nuevas mecánicas.

| Área | Fuente actual | Trabajo requerido antes de implementación operativa | Criterio de prueba |
|---|---|---|---|
| Guarniciones | Anexo SQL 002; capítulo 43 | Contrato público versionado y persistencia de cohorts, cadencia y límites por nación/edificio | Spawn LIVE/offline, cap 6/120, idempotencia y recursos protegidos |
| Batallas | SQL 002; contrato propuesto `/battles/{battleId}` | Operaciones de agenda/cancelación/resolución, DTO y publicación por SignalR | Tres emparejamientos, empates, cooldown, resultados por commit |
| Patrocinios cosméticos | SQL 002; data/cosmetic_sponsorship | Comando o flujo de adquisición consentido, estados, reversión, moderación y versión | Sin ventajas de competición; doble evento no acredita dos veces |
| Snapshot/delta | OpenAPI base y `signalr.v2.md` | DTOs y eventos de guarnición/batalla coherentes; reconexión con secuencia monotónica | Gap→snapshot sin extrapolación económica |
| Relojes/recuperación | Capítulo 42, 29, SQL 001 | Representación persistente de subrelojes, límites, fencing y fuentes de autoridad | Desconexión/replay obtiene mismos hashes |
| Ingresos | SQL 001, transacciones y capítulo 10 | Ledger separado de holds ordinarios; deuda de oro y reversos únicamente cosméticos | Reverso no cancela Consejo ni crea stock negativo |
| Migraciones | DDL 001 y anexo 002 | Convertir diseño a migraciones ordenadas y reversibles, con validación en PostgreSQL real | Aplicación inicial y recuperación en entorno aislado |
| Seguridad/API | OpenAPI de diseño 2.2.0 y capítulo 54 | Autorización detallada por acción y audiencia; contrato completo de errores | Pruebas 401/403, aislamiento de canales, secretos nunca en DTOs |
| Versiones | content_manifest 2.2 / ruleset schema 2.2, DTO troncales 2.0 y eventos extendidos 2.2 | Distinguir esquema, contenido y versión de ejecución congelados por temporada | Hash reproducible, handshake y lectura de snapshots antiguos |

**Regla:** el contrato activo del juego no queda completo por escribir esta matriz. Una ruta mencionada en el anexo continúa siendo **propuesta** hasta incorporarse a OpenAPI versionado y contar con tests. No habilitar una capacidad LIVE o monetaria sin pruebas y permisos de la cuenta real.

**Prioridad técnica:** cerrar AUD2-01 (ámbito de workers) antes de balance; consolidar modelos y pruebas del vertical slice antes de generar API pública completa.

## Estado parcial de esta revisión

El contrato declarativo OpenAPI 2.2 y el esquema de cuatro eventos SignalR públicos están presentes; la compatibilidad por mensaje está descrita en `IDENTITY_AND_VERSION_POLICY.md` y sus referencias/ejemplos se comprueban por CI. El SQL base más anexos y migración de integridad pasan smoke tests de PostgreSQL 16 en una base **vacía**. Los gates del cuadro relacionados con concurrencia real, migración de bases existentes, aplicación, DTO ejecutados, identidad, seguridad y proveedores continúan **NOT_RUN**. No confundir especificación de ruta con endpoint en servicio.
