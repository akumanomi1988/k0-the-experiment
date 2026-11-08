# Instrucciones de trabajo para K0

Autoridad documental: [CURRENT](CURRENT.md) y [especificación normativa v2.5](v2.5/ESPECIFICACION_MAESTRA_v2.5.md). Fuente de versión: data/active_documentation.json. El registro histórico de 67 capítulos y 92 decisiones NO debe reescribirse como si fuera la norma activa.

Antes de cada PR: verificar autoridad con python3 tools/check_active_spec.py --check, y validar catálogos y archivo histórico con python3 tools/validate_design_catalogs.py y python3 tools/validate_v25_consolidation.py. Si cambia la versión documental, primero actualizar el puntero activo y luego regenerar CURRENT.md con --write.

Requisitos de identidad: nationId público = UUID y factionId = slug. Tres naciones distintas, un backend central. Cupo humano por profesión y nación, rotación hash reproducible por ventana de 600s LIVE, XP de trabajo solo por actividad efectiva aceptada. !join requiere identidad del proveedor autenticada, NO ciudadano anterior; !work sí necesita ciudadano registrado. Economía offline al 20% una sola vez. Consejo y maravillas sin consumo de oro.

No fusionar el PR #1 obsoleto de v2.2 sobre la especificación v2.5: introduce otro ámbito de cuota y otro significado de nationId. No tocar temporadas RUNNING. No inventar permisos LIVE, resultados de simulación, migraciones productivas, assets, licencias o software construido.

La CI comprueba consistencia documental dentro de su alcance, pero no sustituye pruebas de aplicación ni protege por sí misma main si se omiten las verificaciones.
