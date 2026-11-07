# ADR-0001 — Ámbito nacional de trabajadores humanos y versiones

**Fecha:** 2026-11-07  
**Estado:** PROPUESTA A REVISAR EN PR; NO CONFUNDIR CON DECISIÓN ORIGINAL 1–92.  
**Motivo:** solicitud del propietario de continuar con la consolidación de ingeniería, sin escoger expresamente entre dos ámbitos posibles.

## Contexto

`activeHumanWorkersSoftCap=2500` aparecía sin ámbito en el ruleset; `docs/04` lo describía por oficio, por lo que cinco profesiones podían aplicar hasta 12.500 cuotas marginalmente productivas en vez de 2.500 por nación. El balance de dos implementaciones podía divergir significativamente.

## Resolución propuesta

`activeHumanWorkersScope = nation_total`. Cada nación considera todos sus humanos activos con profesión, ordenados por `(activeSinceUtc, citizenId)` ascendente, de forma estable en cada frontera de actividad. Puestos 1–100: 100 %; puestos 101–2500: 25 %; posteriores: 0 % de output. Los NPC quedan fuera de la cuota. La productividad y los cuidados se calculan en enteros; los 50 equivalentes máximos imputables a mantenimiento se aplican DESPUÉS de la ponderación. La profesión nunca cambia por salir de cuota.

**Trade-off:** algunas profesiones podrían quedar infrarrepresentadas en cuotas tras entrar tarde; la ruta autónoma NPC debe funcionar de todas maneras. Un algoritmo futuro de cuotas por profesión sería otro diseño y requeriría nuevo hash y balance. El XP residual de participantes sin productividad requiere una decisión complementaria antes de motor autoritativo.

## Versiones

- `ruleset.schemaVersion: 2.2.0` identifica el contrato estructural obligatorio, no una afirmación de que existe un ejecutable.
- `rulesetId: chaos-default-2026-11-nation-total-v22` identifica la revisión lógica candidata para futuras temporadas.
- `rulesetHash` = SHA-256 de bytes exactos de `data/ruleset.v2.json`, inmovilizado al crear temporada.
- `contentHash` = SHA-256 del JSON UTF-8 compacto de la lista ordenada `[filename, data]` con keys ordenadas y arrays en su orden original. Contiene 16 catálogos, sin el propio ruleset.
- Versión de esquema, versión de contenido, hash y `engineVersion` son campos distintos. No comparar versiones textuales para inferir igualdad de reglas.

**Impacto:** actualización sincronizada de ruleset, schema, docs 04/56, hashes, modelo de referencia y CI. No se alteran números base, las 92 decisiones originales ni temporadas activas (el producto aún no está implementado).

## Validación

Comparar perfiles 0, 10, 100, 1000, 10000, reparto equilibrado/sesgado y 4/24h LIVE mediante `tools/reference_simulation.py`. Verificar compilación semántica del motor real, orden de actividad, XP, sesgos y reproducibilidad antes de cerrar D2.

**Revisión requerida:** el propietario debe revisar este ADR junto al PR; no declarar D2 a partir de la propuesta únicamente.
