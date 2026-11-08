# Instrucciones para agentes de Project CHAOS

1. **Fuente normativa única:** [docs/ESPECIFICACION.md](docs/ESPECIFICACION.md). Los [67 documentos por tema](docs/INDICE.md) la desarrollan. La decisión explícita más reciente del propietario prevalece; no restaurar reglas de commits anteriores sin autorización.
2. **Versiones:** editar siempre un archivo existente; nunca crear documentación `_vN.md`, `vN/`, índices o manifiestos históricos duplicados. Git ya preserva el historial. Conservar `schemaVersion` de API/JSON y el orden de scripts SQL por compatibilidad técnica.
3. **Datos:** [catálogo activo](data/content_manifest.json) y contratos de `contracts/`. Cada cambio de regla exige actualización simultánea de especificación, catálogo, referencias y pruebas; las temporadas RUNNING conservan su contenido congelado.
4. **Reglas críticas:** `!join` requiere autenticación de proveedor, sin ciudadanía previa; `!work` sí exige ciudadano. `nationId` es UUID, `factionId` es slug. Límite humano **global de 2.500 puestos por nación entre todas las profesiones**, con rotación determinista cada 600 s LIVE y XP únicamente por trabajo aceptado. Consejo y maravillas no consumen oro.
5. **Pruebas:** ejecutar los tres validadores del README y revisar los checks de PR. No afirmar que el motor, migraciones productivas, proveedores, balance, OBS ni arte están aprobados por haber pasado la CI de diseño.

## Decisiones confirmadas del propietario (8-11-2026)

Consultar la tabla de veinte decisiones de `docs/ESPECIFICACION.md`: **12 eras jugables antes de proveedores**, primer modo **SINGLE_OPERATOR**, primer proveedor **YouTube Live** condicionado a permisos, temporada objetivo **45–90 días**, 100 % LIVE/20 % OFFLINE **sin compensación** y horas públicas, arranque multistreamer con **tres canales autorizados sin LIVE simultáneo**, abandono confirmado **PAUSED→ABORTED en 7 días UTC**, torneo congelado **CANCELLED en 72 h UTC**, cupo nacional único **2.500**, **una nación por cuenta K0** sin login obligatorio para el chat, pseudónimo por defecto y alias con opt-in, monetización solo tras validar juego, **LLM/TTS dinámico** seguro, **arte de las 12 eras y epílogo** antes del piloto, overlays ES vertical/horizontal, España/UE público general con protección de menores, retención operativa **30 días** salvo ley, priorizar show propio, **techo 100 €/mes**.

No crear otra especificación ni documentos con sufijos de versión. El usuario confirmó estas decisiones; no reabrirlas sin que lo pida.
