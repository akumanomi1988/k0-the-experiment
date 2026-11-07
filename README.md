# K0: The Experiment — Game Design & Technical Specification

> **Estado: DISEÑO DOCUMENTAL v2.2 / SIN JUEGO IMPLEMENTADO.** Repositorio canónico público. Google Drive queda como respaldo histórico. No hay código de aplicación ni infraestructura de juego desplegada. Sí existen scripts de validación, una simulación económica de referencia y GitHub Actions; no son el motor del juego.

Tres civilizaciones no humanas — **Micelios, Rúnicos y Ferrinos** — evolucionan desde el Paleolítico hasta la Era Interestelar en un espectáculo interactivo presentado por **Doctor K-0**, científico cyborg neutral. Los espectadores participan desde tres fuentes de chat diferenciadas (mismo proveedor o varios, cuando existan permisos). Estilo propuesto: pixel art retro 2D de baja resolución, proyección oblicua 2:1.

## Empieza aquí

1. **[Auditoría de alcance y correcciones v2.2](docs/41_AUDITORIA_DE_COMPLETITUD_Y_JERARQUIA_v2.2.md)** — qué está y no está cerrado.
2. **[Índice de los 62 capítulos](DOCS_INDEX_v2.2.md)** — navegación de todo el diseño.
3. **[Visión y reglas de base](docs/01_VISION_Y_ALCANCE.md)**, **[economía](docs/04_ECONOMIA_Y_BALANCE.md)**, **[progresión](docs/07_PROGRESION_TECNOLOGICA_Y_TEMPORADAS.md)**.
4. **[Universo y personajes](docs/25_BIBLIA_NARRATIVA_UNIVERSO_Y_PERSONAJES.md)**, **[estilo visual](docs/46_MANUAL_DE_ESTILO_PIXEL_ART_v2.2.md)**, **[HUD](docs/47_LAYOUT_HUD_Y_ESCENAS_PIXEL_PERFECT_v2.2.md)**.
5. **[Contratos de integridad](docs/42_CONTRATOS_DE_ESTADOS_Y_TIEMPO_v2.2.md)**, **[arquitectura](docs/55_ARQUITECTURA_TECNICA_Y_LIMITES_v2.2.md)** y **[criterios de cierre](docs/60_DEFINITION_OF_READY_Y_GATES_DE_CIERRE_v2.2.md)**.

## Directorios

| Ruta | Contenido |
|---|---|
| [`docs/`](docs/) | 62 capítulos Markdown (01–40 históricos vigentes salvo enmiendas; 41–62 nuevos y normativos donde se indique) |
| [`data/`](data/) | Catálogos declarativos JSON, no lógica ejecutable |
| [`architecture/`](architecture/) | DDL de referencia 001–003 ejecutada en PostgreSQL 16 aislado por CI; faltan migraciones de producción y transacciones del motor |
| [`contracts/`](contracts/) | JSON Schema/OpenAPI/SignalR de diseño y anexo v2.2, aún no consolidados en versión API operativa |
| [`audit/`](audit/) | Registro histórico, riesgos, checksums y simulación simplificada no autoritativa |
| [`PROJECT_CHAOS_DOCUMENTACION_MAESTRA_v2.1.md`](PROJECT_CHAOS_DOCUMENTACION_MAESTRA_v2.1.md) | Compendio **histórico v2.1**, no prevalece sobre correcciones v2.2 |

## Revisiones relevantes v2.2

- Todos los **39 proyectos de Consejo** y **13 maravillas** tienen coste de oro igual a **cero** para mantener participación gratuita. El oro verificado, si se habilita, se dedica a cosméticos no competitivos.
- Tecnologías troncales ahora se corresponden con prerrequisitos reales de talleres y centros de investigación.
- Nueva definición de **guarniciones y 39 unidades de combate automático**; **no** es código funcional ni balance probado.
- Manuales ampliados de estética, sonido, composición de pantalla, K-0, UX, streaming, proveedores, seguridad, arquitectura, balance, QA y aceptación.

## Jerarquía de decisiones

Mensaje explícito posterior del propietario → 92 decisiones originales confirmadas (salvo sustituciones trazadas) → enmiendas documentadas v2.2 → datos canónicos → documentos heredados 01–40 → históricos anteriores. Las enmiendas D-01–D-10 se explican en `docs/41`.

**No se presume que todo esté validado.** Los artefactos visuales siguen sin dibujar/aprobar; el juego no está programado; el SQL no está ejecutado; las APIs de proveedores no se han autorizado para las cuentas; la simulación simplificada anterior no prueba los cinco hitos de cada era. Todos los gates están inventariados en `docs/60`.

## Repositorio público y derechos

No subir tokens, credenciales, emails de espectadores, conversaciones privadas, material de terceros sin derechos ni datos de pago. La denominación **K0: The Experiment** está pendiente de comprobación registral; publicar documentación no garantiza exclusividad comercial. No existe licencia explícita para uso por terceros: decidirla antes de invitar contribuciones externas.


## Mantenimiento documental y contribuciones

- [Guía para agentes de IA y desarrolladores](AGENTS.md).
- [Acta de consolidación y bloqueantes D2 (2026-11-07)](audit/CONSOLIDACION_D2_2026-11-07.md).
- [Matriz de contratos pendientes de consolidación](contracts/CONSOLIDATION_GAPS_V2_2.md).
- [Workflow de integridad](.github/workflows/documentation-integrity.yml): verifica sintaxis JSON, esquemas, OpenAPI interno, enlaces, recuentos, dependencias e inventario de SHA-256.

Para validar localmente:

```bash
python -m pip install -r tools/requirements-validation.txt
python tools/validate_repo.py
```

Tras cualquier cambio documental, regenerar inventario y volver a validar con `python tools/validate_repo.py --write-manifest`. La validación declarativa no prueba balance, arte, integraciones, migraciones PostgreSQL ni lanzamiento. **Se mantiene D1 ampliado hasta evidenciar los gates D2.**

Pruebas adicionales: `python -m unittest discover -s tests -p 'test_*.py' -v`, `python tools/balance_matrix.py` y `tests/sql/integrity_v2.2.sql` en el job PostgreSQL 16. Los 20 escenarios de la matriz económica son **modelos conservadores**, no validación del software inexistente.

Resultados reproducibles y riesgos de la matriz de 20 escenarios: [informe de balance de referencia](audit/REFERENCE_BALANCE_MATRIX_2026-11-07.md). El reparto sesgado de oficios puede alargar significativamente las temporadas, incluso si todas las rutas siguen siendo gratuitas.
