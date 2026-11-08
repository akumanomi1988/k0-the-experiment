# Documentación vigente — K0: The Experiment

<!-- GENERADO: python3 tools/check_active_spec.py --write -->

**Especificación documental activa: v2.5.** Diseño no implementado ni certificado para LIVE.

- Norma: [v2.5/ESPECIFICACION_MAESTRA_v2.5.md](v2.5/ESPECIFICACION_MAESTRA_v2.5.md)
- Enmiendas: [v2.5/REGISTRO_DE_CONSOLIDACION_v2.5.md](v2.5/REGISTRO_DE_CONSOLIDACION_v2.5.md)
- Cobertura histórica: [v2.5/INDICE_DE_COBERTURA_v2.5.md](v2.5/INDICE_DE_COBERTURA_v2.5.md)
- Índice histórico: [DOCS_INDEX_v2.5.md](DOCS_INDEX_v2.5.md)
- Ruleset: data/ruleset.v2.json (schema 2.3.0)
- Manifiesto de catálogos: data/content_manifest.v2.3.json (schema 2.3.0)
- Cuota humana: PER_PROFESSION_PER_NATION_DESIGN_CANDIDATE
- Rotación: deterministic_hash_rotation_per_profession_live_600s
- XP de trabajo: accepted_effective_work_only

Contratos v2.5: nationId es UUID; factionId es slug independiente. El comando !join no requiere ciudadanía previa.

Los 67 capítulos originales y otras versiones son fuentes históricas, no normas paralelas.
Para actualizar este archivo: python3 tools/check_active_spec.py --write. La CI ejecuta --check.
Esta CI no valida motor, arte, autorizaciones de proveedores, migraciones reales ni balance global.
