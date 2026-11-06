# K0: The Experiment

**Estado del proyecto:** diseño y especificación. **No existe todavía un videojuego implementado.**

K0: The Experiment es el título de trabajo del videojuego interactivo anteriormente documentado como **Project CHAOS**. Doctor K-0, un científico cyborg, presenta una competición entre tres civilizaciones que evolucionan a través de las eras bajo la influencia de los espectadores de emisiones en directo. La dirección artística prevista es pixel art retro 2D de baja resolución y perspectiva oblicua/isométrica.

> **Repositorio canónico:** este repositorio GitHub es la fuente principal de la documentación vigente. Las copias de Google Drive y los paquetes ZIP anteriores son respaldos históricos, no la fuente de modificaciones futuras.

## Contenido

| Ruta | Función |
| --- | --- |
| [`PROJECT_CHAOS_DOCUMENTACION_MAESTRA_v2.1.md`](PROJECT_CHAOS_DOCUMENTACION_MAESTRA_v2.1.md) | Especificación maestra consolidada. Conserva la denominación interna histórica. |
| [`docs/`](docs/) | **40 capítulos** de mecánicas, economía, progresión, público, narrativa, arte, operación, calidad y aceptación. |
| [`data/`](data/) | **JSON declarativos**: 3 facciones, 13 eras, 5 oficios, 130 edificios básicos, 39 proyectos, 13 maravillas, 65 hitos, 39 tecnologías, 30 habilidades, gobiernos y reglas. |
| [`architecture/`](architecture/) | Arquitectura conceptual y esquema SQL **propuesto**, no desplegado ni probado. |
| [`contracts/`](contracts/) | Contratos de diseño JSON Schema, OpenAPI y SignalR; **no** son servicios implementados. |
| [`audit/`](audit/) | Trazabilidad, decisiones, limitaciones y verificaciones aún pendientes. |
| [`MANIFIESTO_DOCUMENTAL_v2.1.md`](MANIFIESTO_DOCUMENTAL_v2.1.md) | Inventario y hashes de integridad de los archivos de documentación. |

## Orden de lectura

1. [Glosario y jerarquía de fuentes](docs/23_GLOSARIO_JERARQUIA_Y_LIMITE_DE_DISENO.md).
2. [Visión del juego](docs/01_VISION_Y_ALCANCE.md) y [decisiones corregidas](docs/18_DECISIONES_DE_BASE_CORREGIDAS.md).
3. [Funcionamiento de las tres cuentas y naciones](docs/02_CANALES_CUENTAS_Y_NACIONES.md), [economía](docs/04_ECONOMIA_Y_BALANCE.md) y [progresión](docs/07_PROGRESION_TECNOLOGICA_Y_TEMPORADAS.md).
4. [Universo y personajes](docs/25_BIBLIA_NARRATIVA_UNIVERSO_Y_PERSONAJES.md), [biblia visual](docs/26_BIBLIA_VISUAL_FACCIONES_EPOCAS_Y_SILUETAS.md) y [experiencia del espectador](docs/24_RECORRIDOS_ESPECTADOR_Y_CIUDADANIA.md).
5. [Catálogo de edificios](docs/34_CATALOGO_LEGIBLE_EDIFICIOS.md), [proyectos y maravillas](docs/35_CATALOGO_LEGIBLE_PROYECTOS_Y_MARAVILLAS.md), [tecnologías e hitos](docs/36_CATALOGO_LEGIBLE_TECNOLOGIAS_E_HITOS.md), [profesiones, habilidades y gobiernos](docs/37_CATALOGO_LEGIBLE_PROFESIONES_HABILIDADES_GOBIERNOS.md).
6. [Condiciones externas pendientes](audit/EXTERNAL_GATES.md) y [registro de cierre](docs/39_REGISTRO_DE_CIERRE_Y_VALIDACIONES_EXTERNAS.md).

## Autoridad documental

Las **92 decisiones originales** y los valores de diseño siguen conservados. Para conflictos se aplica la [jerarquía de fuentes](docs/23_GLOSARIO_JERARQUIA_Y_LIMITE_DE_DISENO.md). El nombre público **K0: The Experiment** sustituye a *Project CHAOS* como identificación del producto; los identificadores y títulos internos `CHAOS` se mantienen por trazabilidad documental hasta una revisión controlada.

La instrucción histórica de no crear repositorios, presente en documentos v2.1, queda **sustituida exclusivamente** por la decisión posterior del propietario de versionar esta documentación en GitHub. Continúa vigente la restricción de **no desarrollar código de aplicación por ahora**.

Este repositorio no contiene Python, Docker, CI/CD, secretos ni backend/frontend. Los archivos SQL, YAML y JSON son propuestas de diseño, no una implementación.

## Estado y límites

El equilibrio numérico, las integraciones con plataformas, los permisos LIVE, el cumplimiento normativo, el SQL y los assets finales requieren validación posterior. La presencia de una regla o contrato aquí **no acredita su ejecución en producción**.

**Visibilidad actual:** repositorio público. No incorporar tokens, credenciales, datos personales reales, documentación privada de terceros ni material sin derechos de publicación.
