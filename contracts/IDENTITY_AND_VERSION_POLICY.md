# Política canónica de identidad y versiones — baseline K0 v2.2

**Estado:** contrato de diseño para revisión y futura implementación. La fuente de revisión activa es [CURRENT](../docs/CURRENT.md); una ruta en OpenAPI no equivale a un endpoint desplegado.

## Identidades estrictamente diferenciadas

| Nombre | Tipo | Uso |
|---|---|---|
| `SeasonId` (`seasonId`) | UUID en API y PostgreSQL | Aislamiento entre temporadas |
| `NationDbId` (`nations.nation_id`) | UUID interno | FK, locks, balances, writer, ledger |
| `NationPublicId` (`nationId` público) | slug `micelios`, `runicos` o `ferrinos` | Parámetros HTTP, JSON público, SignalR, bindings |
| `FactionId` (`nations.faction_id`) | mismo slug público | Atributo único por temporada, identidad estética |

**No se convierte un slug en UUID.** El backend consulta `nations WHERE season_id=:seasonId AND faction_id=:nationSlug`, con `UNIQUE(season_id,faction_id)`, y solo entonces utiliza `NationDbId` para operaciones transaccionales. Cualquier consulta sin `seasonId`, nación ambigua o desconocida se rechaza. Los bindings de canales se validan contra ese UUID interno, nunca contra una etiqueta de proveedor. En cualquier DTO/contrato público v2, `nationId` significa el slug de facción, **nunca** el UUID interno. Las configuraciones demo pueden contener `seasonId` simbólico, pero **no** son entradas REST válidas.

## Compatibilidad de transportes

- `/api/v2` y `/hubs/v2/chaos`: versión **mayor del transporte**, independiente de la versión de cada mensaje.
- `contracts/openapi.v2.yaml/info.version`: `2.2.0`, revisión del contrato de diseño.
- `data/ruleset.v2.json/schemaVersion` y `data/content_manifest.v2.json/schemaVersion`: `2.2.0`. `rulesetId`, `rulesetHash`, `contentHash` y `engineVersion` se gestionan por separado.
- Proyecciones troncales `NationSummary`, `NationDeltaV2`, `NormalizedEventV2` y configuración de bindings: `schemaVersion=2.0.0`. Son DTOs del núcleo y **no** se rebautizan implícitamente a 2.2.
- Notificaciones añadidas `garrison.changed`, `battle.scheduled`, `battle.result`, `cosmetic.acknowledgement`: `schemaVersion=2.2.0`, discriminante `kind` obligatorio. Son estructuras distintas, no variantes silenciosas del DTO troncal.

El protocolo SignalR debe negociar en su handshake el conjunto de pares `(kind, schemaVersion)` admitidos y la última secuencia. No se envía un tipo desconocido a un cliente que no lo haya aceptado. Ante gaps de secuencia se exige snapshot y se prohíbe interpolar economía. Un cambio incompatible requiere versión de contrato y migración explícitas; no se habilitarán tipos nuevos por inferencia del número del hub. **Negociación y replays son requisitos de implementación aún no ejecutados.**

## Identidad del espectador y comandos

`!join` requiere identidad de proveedor **autenticada en binding autorizado**, pero NO ciudadano preexistente. Crea o devuelve el ciudadano, una sola vez por `(season,nation,provider,providerUserId)`, con evento idempotente. `!work` requiere ciudadano registrado. `!active` exige además profesión asignada. Una cuenta del proveedor no es sinónimo de ciudadano del juego.

## Sincronización futura

Los desarrolladores deben ejecutar `python tools/sync_docs.py --write` y `python tools/validate_repo.py --write-manifest` al modificar ruleset, catálogos o contratos. La CI verifica que [CURRENT](../docs/CURRENT.md), versiones, hashes y reglas normativas sigan sincronizados. **No se puede garantizar actualización automática de copias externas a GitHub ni de cambios que no pasen por esta CI.**
