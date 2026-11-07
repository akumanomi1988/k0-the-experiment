# 60 — Definition of Ready: qué significa realmente «todo definido»

## Niveles de preparación

**D0 — IDEA:** intención, referencias y grandes reglas. **D1 — DISEÑO DOCUMENTAL:** entidades, comandos, números candidatos, UX, narrativa, arte objetivo y casos límite definidos. **D2 — DISEÑO CERRADO PARA PROTOTIPO:** referencias visuales aprobadas, invariantes sin contradicciones, modelos económicos reproducibles de principio a fin, responsabilidades y contratos consistentes, elección de proveedor objetivo. **D3 — IMPLEMENTACIÓN VERIFICADA:** motor, SQL, UI, integración, seguridad, arte final y pruebas reales operativas. **D4 — LANZAMIENTO AUTORIZADO:** cuentas LIVE permitidas, monetización (si aplica) conforme a términos, datos/privacidad/propiedad intelectual revisados y operación ensayada.

**Estado demostrado hoy: D1 ampliado; no D2, D3 ni D4.** Esta clasificación es deliberadamente estricta.

## Gate de cierre funcional

- [ ] 92 decisiones históricas reproducidas y toda sustitución explicada; las reglas vigentes no están contradichas por tablas legibles.
- [ ] Una temporada completa con 0 espectadores, 0 oro y 24 NPC por nación alcanza Interestelar sin bloqueo usando los **cinco hitos reales de cada era**.
- [ ] Todas las elecciones, Consejos, RPS, batallas y maravillas tienen estados, tiempos, empates y reintentos validados.
- [ ] Simultaneidad y recuperación no duplican votos, oro, edificios o ganador.
- [ ] El usuario novato entiende chat, oficio, actividad, retorno y misiones sin ayuda externa.

## Gate de cierre artístico

- [ ] Captura/arte conceptual final aprobado de Micelios, Rúnicos, Ferrinos y K-0.
- [ ] Tres eras representativas (Paleolítico, Industrial y Espacial) diseñadas para las tres especies.
- [ ] Sprite 16×24, 32×16 tile, sombras, paletas, variantes, HUD y animaciones probados a 1× y en stream vertical.
- [ ] Fuente, sonido, música, voz y derechos comerciales acreditados.
- [ ] Texto y subtítulos legibles sin depender de audio; safe areas verificadas por plataforma.

## Gate de cierre técnico

- [ ] Anexo SQL v2.2 integrado y validado para combate, patrocinios y demás nuevos estados; migraciones reales ejecutadas con tests transaccionales.
- [ ] Contratos REST/SignalR actualizados a las entidades efectivas y sus versiones.
- [ ] Ingesta idempotente, escritura única, determinismo, replays y backups restaurados con evidencia.
- [ ] Pruebas de carga y mediciones de costes con perfiles realistas y 30 FPS OBS estable.
- [ ] Autorización del proveedor, cuotas, política LIVE y límites de monetización comprobados por **cuenta**, no por idea.

## Gate de cierre comercial y normativo

- [ ] Distintividad registral/uso de K0 y Doctor K-0 comprobada en territorios elegidos.
- [ ] Titularidad/licencias de sprites, tipografías, voz, música y contenidos confirmadas.
- [ ] Política real de datos, acceso, retención y solicitudes de usuarios aprobada para la jurisdicción.
- [ ] Presupuesto de infraestructura, moderación, marketing, mantenimiento y operación basado en tarifas/uso verificables.
- [ ] Reglas de contribución económica verificadas con reversos reales o mantenidas apagadas.

## Política de aprobación

Cada casilla requiere documento, evidencia, responsable, fecha y versión. No «marcar completado» por haber escrito su intención. El propietario puede congelar un baseline **para desarrollo** sin que eso signifique que ya existe producto terminado. Las dependencias externas no son defectos que puedan arreglarse escribiendo más Markdown; deben mostrarse como gates, jamás como supuestos ocultos.


## Seguimiento de cierre (auditoría 2026-11-07)

Ver [acta de consolidación](../audit/CONSOLIDACION_D2_2026-11-07.md) y [matriz de contratos](../contracts/CONSOLIDATION_GAPS_V2_2.md). El gate D2 permanece **ABIERTO**: se propone el ámbito por nación de `activeHumanWorkersSoftCap` en esta rama, pendiente de revisión del propietario y de balance del motor (XP residual cerrada en cero); demostrar una temporada con cinco hitos reales por era; consolidar y probar contratos/migraciones; aprobar muestras de arte y verificar el primer proveedor por cuenta.

La CI de integridad del repositorio solo acredita invariantes **declarativas**. Un PASS no convierte las casillas anteriores en aprobadas.

**Evidencia parcial posterior al baseline:** la migración de integridad SQL 001–003 pasa en PostgreSQL 16 aislado y 20 escenarios de `tools/reference_simulation.py` llegan a Interestelar con 60 hitos; consultar [informe](../audit/REFERENCE_BALANCE_MATRIX_2026-11-07.md). No representan una partida completa del motor real. La prueba de balance final continúa pendiente; los parámetros de trabajadores por nación son propuesta bajo [ADR-0001](../audit/ADR_0001_WORKER_CAP_AND_VERSIONS.md), a revisar antes de D2.


**Fuente única de versión y hashes:** [CURRENT generado](CURRENT.md); [política de tipos de nación y compatibilidad](../contracts/IDENTITY_AND_VERSION_POLICY.md). Un PASS de sincronización confirma documentación coherente, no condiciones externas ni D2–D4.
