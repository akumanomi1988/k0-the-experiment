# K0: The Experiment — Project CHAOS

**Estado:** especificación de diseño, sin motor del videojuego desplegado ni permisos LIVE acreditados. La documentación tiene **nombres estables**: la evolución se conserva en Git, no mediante copias `_v2.2`/`_v2.5`.

## Punto de entrada único

**[ESPECIFICACION_MAESTRA.md](ESPECIFICACION_MAESTRA.md)** es la fuente normativa de diseño. El [índice](DOCS_INDEX.md) contiene los 67 capítulos de detalle. [Registro de decisiones](REGISTRO_DE_DECISIONES.md) y [cobertura documental](COBERTURA_DOCUMENTAL.md) explican trazabilidad y alcance; no son versiones paralelas de la especificación.

Las 92 decisiones originales continúan disponibles en [JSON](data/legacy_user_decisions_1_92.json). Los catálogos canónicos para valores de contenido se consultan mediante [el manifiesto de diseño](data/content_manifest.v2.3.json). Los números `schemaVersion`, los contratos de API y los scripts SQL son identificadores técnicos de compatibilidad, **no versiones de documentos**.

## Producto

Tres civilizaciones no humanas —Micelios, Rúnicos y Ferrinos— compiten por llegar a Interestelar en una temporada compartida. Doctor K-0 es el presentador cyborg; cinco profesiones, NPC autónomos, proyectos de Consejo sin oro, elecciones, misiones y combates automáticos. Pixel art 2D retro oblicuo.

Admite tres streamers independientes, en tres PCs y redes distintas, con un backend autoritativo común. Arquitectura objetivo: ASP.NET Core .NET, PostgreSQL, SignalR, React/TypeScript y Phaser. El OBS Browser Source de cada emisor es una vista, no un motor.

## Forma de trabajar

1. Editar el **mismo documento**, sin crear `_vN`, duplicados `_final` ni carpetas de versiones.
2. Si la norma cambia, modificar `ESPECIFICACION_MAESTRA.md`, las reglas JSON afectadas, el capítulo de detalle correspondiente, y las pruebas de consistencia.
3. Ejecutar `python3 tools/validate_documentation.py` y `python3 tools/validate_design_catalogs.py`. La CI bloquea enlaces rotos, duplicados históricos y cambios de normativa incompatibles con los datos estructurados.
4. Consultar `git log --follow`, `git blame` y `git show` para consultar cualquier versión anterior. No regenerar archivos históricos dentro de la rama activa.

**No implementado/acreditado:** motor funcional, balance integral, arte final, permisos LIVE por cuenta, migraciones productivas, pruebas OBS en tres equipos, cumplimiento legal y lanzamiento.
