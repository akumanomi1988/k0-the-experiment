# Persistencia, invariantes y arquitectura

`001_schema.sql` es el **modelo relacional de referencia**, no una migración ya ejecutada ni probada en un PostgreSQL real. La implementación debe convertirlo a migraciones versionadas y ejecutar tests de FKs compuestas y concurrencia con PostgreSQL 16+ antes de LIVE.

## Límites de transacción
- `Citizen` + `Inbox` y `Ballot` bajo transacción por evento con `source_key` único.
- Economía por nación: adquirir el escritor lógico, leer balances con `SELECT ... FOR UPDATE`, insertar ledger idempotente y actualizar stock; confirmar Outbox en mismo commit.
- Consejo: bloquear saldos, apartar `max(costOption)` por recurso, deducir SOLO ganador al cerrar y liberar restante, sin operaciones fuera de la transacción.
- `SeasonWinnerClaim` y `WonderClaim` solo mediante `INSERT ... ON CONFLICT DO NOTHING` bajo lock compartido de temporada; el primer commit efectivo gana y el segundo obtiene resultado registrado.
- Reverso: no eliminar ni modificar asientos; asiento compensatorio y deuda remanente separada.

## Cosas que SQL por sí solo no garantiza
Que el estado de una elección sea legal, que un evento de proveedor esté realmente verificado, que las tres cuentas hayan sido autorizadas, que un voto esté en rango de LiveClock, que la habilidad pertenezca a la profesión, que exista stock suficiente al consumir simultáneamente. Eso requiere invariantes de dominio + tests + permisos DB de la aplicación. Cualquier acceso directo de usuario a tablas de saldo se deniega; separar rol migrador y rol runtime con permisos mínimos.

## Clave compuesta
Toda entidad de nación contiene `(season_id,nation_id)` y referencia con FK compuesta para impedir mover por UUID una construcción o papeleta entre naciones. `channel_bindings` da resolución inequívoca `(season_id,provider,provider_channel_id)`. Al iniciar temporada una DB CHECK no puede exigir exactamente 3 naciones; implementar ese gate antes de `RUNNING`.
