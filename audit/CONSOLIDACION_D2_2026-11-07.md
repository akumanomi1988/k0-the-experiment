# Acta de consolidación documental para D2 — 2026-11-07

**Rama de auditoría:** audit/consolidacion-d2-2026-11-07  
**Baseline inspeccionado:** commit `7214eb40ed64c509ad2918c27d5a2ef6d72de6c9` de `main`.  
**Alcance:** lectura, integridad declarativa, corrección editorial y validadores. **NO** se ha ejecutado el motor (inexistente), PostgreSQL, OBS ni APIs de proveedores.

## Inventario del baseline

109 archivos (incluido el manifiesto), 62 capítulos numerados, 31 JSON, 2 SQL, OpenAPI, esquemas JSON y auditorías. Los 62 capítulos están enlazados en el índice; no se detectaron enlaces Markdown internos rotos en el barrido documental. Los catálogos tienen 13 eras, 130 edificios, 39 proyectos, 13 maravillas, 39 tecnologías, 65 hitos, 5 profesiones, 30 habilidades, 39 unidades y 9 candidatos NPC. Estas cifras prueban estructura, **no** balance ni alcanzabilidad.

## Correcciones realizadas en esta rama

| ID | Tipo | Cambio | Evidencia exigida |
|---|---|---|---|
| C-01 | Coherencia | El Consejo no consume ni reserva oro; reversos se limitan a saldo de oro y patrocinios cosméticos | Capítulos 05, 10, 19, transacciones en architecture/02 |
| C-02 | Coherencia | Terminología de combate alineada con rol `heavy` del catálogo | Capítulo 43 + JSON de unidades |
| C-03 | Editorial | Duplicaciones en capítulos 05 y 34 retiradas | Diff |
| C-04 | Mantenibilidad | `AGENTS.md` con jerarquía de decisiones y protocolo de cambios | Lectura de AGENTS |
| C-05 | Prevención | Validador de documentos, JSON Schema, referencias, catálogos y hashes; GitHub Actions | `tools/validate_repo.py` y workflow |

Ninguna corrección C-01..C-05 demuestra D2 por sí sola. Las 92 decisiones originales permanecen intactas y no se han cambiado los valores del ruleset.

## Bloqueantes para declarar D2

| ID | Severidad | Estado | Responsable propuesto | Criterio de cierre / evidencia |
|---|---|---|---|---|
| AUD2-01 | P0 | **DESIGN_CANDIDATE — `nation_total`** | Propietario + diseñador de balance | En rama se concreta `nation_total` y el orden `(activeSinceUtc,citizenId)` para 100 puestos completos y 2.400 al 25 %. Revisar esta propuesta en PR, ejecutar simulación y cerrar XP residual antes de marcar D2. |
| AUD2-02 | P0 | **NOT_RUN** | Desarrollador motor | Simulador semánticamente equivalente que complete los cinco hitos reales de eras 1–12 con 0/10/100/1000/10000 espectadores, varias seeds, cero oro y sin bloqueos. Archivo de balance histórico NO es evidencia suficiente. |
| AUD2-03 | P1 | **NOT_RUN** | Arquitecto backend | Consolidar anexos SQL y API v2.2; ejecutar migraciones, FKs, concurrencia e idempotencia en PostgreSQL aislado, con resultados fechados. |
| AUD2-04 | P1 | **OPEN** | Arquitecto + propietario | Definir versión de esquema distinta de ruleset/content hash. Acreditar compatibilidad de snapshots y temporadas. |
| AUD2-05 | P1 | **NOT_RUN** | Dirección artística | Aprobar sprites de tres especies y K-0, un edificio/facción y eras 1/9/12, con escalas 1×, vertical/horizontal, HUD y subtítulos. |
| AUD2-06 | P1 | **EXTERNAL_GATE** | Operador de cuentas | Verificar por cuenta permisos LIVE, cuotas, términos, presencia e idempotencia; TikTok bloqueado hasta evidencia. |
| AUD2-07 | P1 | **NOT_RUN** | Seguridad/operación | Restore real, roles operador, separación canal/nación, protección de PII y 30 FPS con carga. |
| AUD2-08 | P2 | **OPEN** | Propietario | Elegir política de licencias para repo público y aclarar derechos de marca/arte antes de contribuciones de terceros. |

## Criterios para un vertical slice sin cerrar D2

Una era, tres naciones aisladas, cinco profesiones, 24 NPC/nación, motores por tick, snapshots y reserva vectorial de un Consejo, comandos sintéticos, transición por cinco hitos y representación pixel art de muestra. Desactivar dinero real y proveedores sin permisos. El resultado de la simulación debe reproducirse desde seed + entradas + hashes.

## Evidencia vs intención

- **PASS documental:** archivos y referencias enumerables; correcciones específicas hechas; validaciones que lleguen a ejecutarse con salida trazable.
- **NOT_RUN:** pruebas de migraciones, seguridad real, partidas completas y proveedores.
- **VISUAL_BRIEF:** estilos, listas de sprites, HUD, audio y K-0 sin aprobación de arte.
- **CANDIDATE_BALANCE:** cifras de economía hasta disponer de motor de referencia y escenarios reproducibles.

**Estado tras esta consolidación:** D1 ampliado con controles automatizables; **no declarar D2/D3/D4** sin evidencias definidas en `docs/60`.
