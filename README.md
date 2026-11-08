# K0: The Experiment — Project CHAOS

**La documentación vigente está en [docs/ESPECIFICACION.md](docs/ESPECIFICACION.md).** Solo existe un archivo por tema; **Git es el control de versiones**, no los nombres de los documentos.

[Índice por temas](docs/INDICE.md) · [Instrucciones para agentes](AGENTS.md) · [Decisiones confirmadas](data/legacy_user_decisions_1_92.json) · [Catálogos activos](data/content_manifest.json)

Project CHAOS es un juego competitivo para directos con tres naciones (Micelios, Rúnicos y Ferrinos), cinco profesiones, NPC autónomos, trece eras conceptuales y Doctor K-0. La arquitectura prevista utiliza un backend central .NET, PostgreSQL, SignalR y overlays OBS independientes para tres streamers. Diseño pixel art 2D retro oblicuo.

**Estado verificable:** especificación, catálogos y contratos de diseño. El juego completo, el arte final, las integraciones LIVE y el balance competitivo no están certificados; ninguna validación documental sustituye esas pruebas.

## Cómo mantener el repositorio

Se **edita el archivo actual**. No se crean `nombre_v1.md`, `nombre_v2.5.md`, carpetas `v2.5/`, manifiestos históricos ni índices duplicados. Los anteriores estados se consultan con `git log`, `git blame` y el historial de PR. `schemaVersion` dentro de JSON conserva significado técnico; los números de scripts SQL indican orden de dependencia, no versiones del documento.

Verificar antes de fusionar:

```bash
python3 tools/check_active_spec.py --check
python3 tools/validate_design_catalogs.py
python3 tools/validate_documentation.py
```

## Alcance decidido por el propietario

Las **20 decisiones de producto confirmadas el 8 de noviembre de 2026** están integradas en la [especificación única](docs/ESPECIFICACION.md): 12 eras completas antes de proveedores, primer piloto como operador único, YouTube Live prioritario, duración 45–90 días, cuota nacional 2.500, identidad por cuenta K0 sin fricción de chat, arte completo, narración dinámica y presupuesto de infraestructura de 100 €/mes. Son decisiones normativas, no software ni autorizaciones ya acreditados.
