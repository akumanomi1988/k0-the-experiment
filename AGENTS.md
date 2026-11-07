# Instrucciones para agentes — K0: The Experiment / Project CHAOS

**Estado:** diseño documental v2.2 (D1 ampliado). No existe motor, cliente, CI de producto, infraestructura ejecutada, arte final ni autorización acreditada de plataformas. Este archivo no eleva el estado a D2–D4.

## Entrada rápida y fuentes autoritativas

1. Leer [README.md](README.md), [índice](DOCS_INDEX_v2.2.md) y [gates](docs/60_DEFINITION_OF_READY_Y_GATES_DE_CIERRE_v2.2.md).
2. Para las decisiones funcionales, consultar [las 92 respuestas originales](data/legacy_user_decisions_1_92.json), [enmiendas v2.2](docs/41_AUDITORIA_DE_COMPLETITUD_Y_JERARQUIA_v2.2.md) y [trazabilidad](audit/decision_traceability.json).
3. Prioridad: **última decisión explícita del propietario** > 92 decisiones confirmadas no sustituidas > enmiendas trazadas v2.2 > datos canónicos de `data/` y contratos coherentes > texto histórico 01–40 cuando no esté enmendado > compendios/manifiestos v2.1. Ante conflicto NO escoger por azar ni presentar una suposición como aprobación; registrar un hallazgo y bloquear la mutación conflictiva.
4. Los números provienen de `data/ruleset.v2.json` y catálogos JSON; los textos legibles no son otra fuente editable de cifras. Las temporadas fijan `rulesetHash` y `contentHash`.

## Restricciones de producto

- Tres naciones independientes: Micelios, Rúnicos, Ferrinos. Tres fuentes de chat diferenciadas, no un único chat asignado a tres naciones.
- Cinco familias profesionales; actividad humana explícita de 7200 segundos; NPC permiten la ruta gratuita y progreso sin donaciones.
- Consejo, proyectos y maravillas usan **únicamente recursos ordinarios** desde v2.2 (`gold=0`). El oro verificado, actualmente deshabilitado, solo financia reconocimientos cosméticos, nunca progreso, votos o ejército.
- Doctor K-0, narración, OBS y renderer no son fuentes de verdad. Motor .NET autoritativo, enteros, relojes LIVE/económico separados, operaciones idempotentes y ledger transaccional.
- No inventar endpoints oficiales, permisos reales de TikTok/YouTube/Twitch, balance validado, licencias, marcas o assets aprobados.
- El estilo definido es pixel art retro 2D con proyección oblicua 2:1, sin ventaja estadística entre especies.

## Protocolo de modificación

1. Crear rama; identificar commit inicial y escribir objetivo de cambio y archivos impactados. No editar `main` directamente ni subir secretos.
2. Antes de tocar un comportamiento, localizar todas sus referencias (reglas, JSON, `docs/`, `architecture/`, `contracts/`, `audit/`, tests). Conservar las 92 decisiones y registrar sustituciones.
3. Cambios de balance requieren justificación, revisión de efectos, nueva huella de reglas/contenidos y pruebas; jamás mutar una temporada RUNNING.
4. Cambios de catálogos requieren IDs únicos, eras, dependencias válidas, coste gratuito y coherencia con los catálogos legibles. Cambios de contrato requieren migración/versionado y pruebas de compatibilidad.
5. Ejecutar `python -m pip install -r tools/requirements-validation.txt` y `python tools/validate_repo.py` antes de presentar una PR. La CI valida estructura y contratos **declarativos**; no sustituye una simulación completa ni test de PostgreSQL.
6. Si se cambian archivos, regenerar el manifiesto mediante `python tools/validate_repo.py --write-manifest` y volver a ejecutar el validador. Mantener históricos etiquetados, no eliminarlos.
7. Documentar evidencia real con comando, salida, commit, fecha y entorno. Marcar cualquier trabajo no ejecutado como `NOT_RUN` y no como `PASS`.

## Decisiones abiertas y gates

- **AUD2-01:** se adopta `nation_total` como decisión de diseño propuesta en esta consolidación, documentada y versionada, con revisión de propietario mediante PR. Los 2.500 trabajadores son un límite por nación, nunca por oficio; aún exige revisión de balance y política explícita de XP residual.
- La simulación histórica `audit/BALANCE_SIMULATION_REFERENCE.json` no prueba los cinco hitos por era; los contratos REST/SQL v2.2 son propuestas pendientes de consolidación y ejecución.
- Arte de facciones y K-0, integraciones LIVE, jurisdicción, licencias y pruebas de carga siguen pendientes; consultar `docs/41`, `docs/57`, `docs/60` y `audit/EXTERNAL_GATES.md`.
- No iniciar la implementación completa del videojuego al realizar una auditoría documental. Los validadores y pruebas aisladas sí están dentro de alcance.

El objetivo es **reducir ambigüedad y deuda técnica**, no producir más capítulos genéricos.

## Evidencia automatizada añadida (no sustituye D2)

- `python -m unittest discover -s tests -p 'test_*.py' -v`: golden tests de cuotas, cinco hitos, reproducción y LIVE/offline mediante un modelo **conservador**.
- `python tools/balance_matrix.py`: 20 casos de perfil de audiencia/actividad y salida JSON; las seeds no impactan en el modelo simplificado (el mapa de competición no se modela).
- `architecture/001_schema_v2.sql` → `002_extensiones_diseno_v2.2.sql` → `003_integridad_v2.2.sql`; los casos `tests/sql/integrity_v2.2.sql` se ejecutan en PostgreSQL 16 de CI.
- `contracts/openapi.v2.yaml` declara contrato **de diseño** 2.2.0 y `contracts/signalr_events.v2.2.schema.json` tipa eventos públicos. Ningún endpoint está desplegado.

Consultar [ADR-0001](audit/ADR_0001_WORKER_CAP_AND_VERSIONS.md) sobre ámbito nacional y versionado.
