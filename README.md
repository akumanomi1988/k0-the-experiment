# K0: The Experiment — Project CHAOS

> **Documentación consolidada v2.5 — diseño de producto y desarrollo.** No existe todavía motor de videojuego funcional ni despliegue público certificado. Ni los permisos LIVE por cuenta ni el arte final ni el balance integral están validados. El repositorio es especificación y contenido, no el ejecutable de K0.

## Fuente de verdad: v2.5

**[Leer la ESPECIFICACIÓN MAESTRA v2.5](v2.5/ESPECIFICACION_MAESTRA_v2.5.md)** — toda la definición vigente del producto, reglas, mecánicas, UX, diseño, personajes, estilo, infraestructura, integración y operación.

Complementos de la versión:

- [Registro de consolidación y conflictos resueltos](v2.5/REGISTRO_DE_CONSOLIDACION_v2.5.md) — cada enmienda, antes/después, estado y prueba.
- [Índice de cobertura integral](v2.5/INDICE_DE_COBERTURA_v2.5.md) — los 67 capítulos completos, las 92 decisiones y catálogos/contratos estructurados.
- [Índice original y navegable de las 67 fuentes](DOCS_INDEX_v2.5.md).
- [Registro histórico de decisiones 1–92](v2.5/fuentes/DECISIONES_1_92.md).
- [Compendio original v2.1 preservado íntegramente](v2.5/fuentes/COMPENDIO_HISTORICO_INTEGRO_v2.1.md).
- [Catálogos declarativos vigentes](data/content_manifest.v2.3.json); [validador estático](tools/validate_design_catalogs.py) y [validador de consolidación](tools/validate_v25_consolidation.py).

**Regla de interpretación:** solamente la especificación maestra v2.5 actúa como autoridad textual para los conflictos corregidos; para valores y listas detalladas se usa el catálogo JSON activo. Los 67 capítulos y el compendio anterior son fuentes íntegras y quedan conservados por trazabilidad, no como otra fuente paralela que pueda reactivar cambios antiguos. El esquema de reglas/catálogos sigue usando identificadores v2/v2.3 hasta existir cambio real de ruleset, contrato y migración. No confundir versión **documental v2.5** con versión **del motor** ni **de API**.

## Producto y arquitectura

Tres civilizaciones no humanas: **Micelios, Rúnicos y Ferrinos**, con estadísticas simétricas y estética pixel art 2D retro, vista oblicua 2:1; Doctor K-0 es un presentador científico **cyborg** y neutral. Las naciones progresan desde Paleolítico hasta la entrada en Interestelar; la primera entrada confirmada gana la temporada. Cinco profesiones, NPC autónomos, edificios básicos automáticos, Consejos gratuitos por voto, gobiernos NPC, misiones por era, RPS y batallas automáticas programadas.

El producto admite **tres streamers distintos en tres ordenadores/redes diferentes**: cada uno emite con su cuenta de proveedor y OBS Browser Source, sin motor instalado. Las tres naciones existen en un **backend autoritativo único** (diseño ASP.NET Core .NET 10, PostgreSQL 16+, SignalR, React/TypeScript + Phaser). También puede existir modo de operador único con tres cuentas de canal. La nación no se asigna permanentemente a Twitch, YouTube o TikTok; cada canal tiene binding exclusivo y autorización por cuenta.

El backend conserva el estado aunque caiga OBS; sus relojes LIVE se basan en evidencia real del proveedor, no en que la ventana del streamer esté abierta. Un torneo global se congela cuando no están confirmados los tres LIVE. Se evita P2P, motores locales y microservicios por emisor durante el MVP.

## Qué existe y qué falta

**Existe:** 67 capítulos históricos completos, 92 decisiones trazadas, especificación maestra v2.5, reglas y catálogos declarativos (130 básicos, 39 proyectos, 13 maravillas, 39 roles de unidad, 13 eras conceptuales, 5 oficios, habilidades, misiones e hitos), contratos JSON/OpenAPI propuestos, DDL de diseño, validadores textuales y roadmap de ingeniería.

**NO existe acreditado:** simulador funcionando, migraciones reales de PostgreSQL y sus pruebas, overlays OBS terminados, arte/audio/voz final, pruebas de rendimiento con tres streamers, certificados de acceso a APIs LIVE, equilibrio total de temporada, política legal aprobada y software comercial. Los catálogos son **candidatos de balance**, las APIs sujetas a pruebas por cuenta, y la monetización real permanece apagada. Especialmente TikTok LIVE no se presume autorizado.

El criterio de avanzar de diseño a implementación y lanzamiento continúa explicitado en [DoR/gates](docs/60_DEFINITION_OF_READY_Y_GATES_DE_CIERRE_v2.2.md) y [registro v2.5](v2.5/REGISTRO_DE_CONSOLIDACION_v2.5.md).

## Desarrollo recomendado

Primero núcleo determinista/DB y una era plenamente funcional con tres naciones sintéticas; después overlays y tres emisores en tres PCs; seguidamente las 12 eras jugables, contenido, política, torneos, balance y proveedor autorizado; por último piloto público y eventual monetización/licencias. El código deberá consumir el manifiesto de contenido y cumplir invariantes de ledger/idempotencia. Nunca asumir que redactar una especificación equivale a pasar QA.

**Seguridad/derechos:** repositorio público. No publicar tokens de plataforma, secretos OBS, PII de espectadores, chat privado, material de terceros sin licencia, voces o música no autorizadas. La marca K0 y las obligaciones comerciales/jurídicas siguen sujetas a comprobación externa.
