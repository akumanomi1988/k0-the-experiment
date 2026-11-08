# Instrucciones para agentes de Project CHAOS

1. **Fuente normativa única:** [docs/ESPECIFICACION.md](docs/ESPECIFICACION.md). Los [67 documentos por tema](docs/INDICE.md) la desarrollan. La decisión explícita más reciente del propietario prevalece; no restaurar reglas de commits anteriores sin autorización.
2. **Versiones:** editar siempre un archivo existente; nunca crear documentación `_vN.md`, `vN/`, índices o manifiestos históricos duplicados. Git ya preserva el historial. Conservar `schemaVersion` de API/JSON y el orden de scripts SQL por compatibilidad técnica.
3. **Datos:** [catálogo activo](data/content_manifest.json) y contratos de `contracts/`. Cada cambio de regla exige actualización simultánea de especificación, catálogo, referencias y pruebas; las temporadas RUNNING conservan su contenido congelado.
4. **Reglas críticas:** `!join` requiere autenticación de proveedor, sin ciudadanía previa; `!work` sí exige ciudadano. `nationId` es UUID, `factionId` es slug. Límite humano **por profesión y nación**, con rotación determinista cada 600 s LIVE y XP únicamente por trabajo aceptado. Consejo y maravillas no consumen oro.
5. **Pruebas:** ejecutar los tres validadores del README y revisar los checks de PR. No afirmar que el motor, migraciones productivas, proveedores, balance, OBS ni arte están aprobados por haber pasado la CI de diseño.
