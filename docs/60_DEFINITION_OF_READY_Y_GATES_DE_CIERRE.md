> **Regla vigente:** incorporar aceptación de 3 streamers remotos y separar evidencia documental de pruebas reales. No confundir v2.3 con producto cerrado. [Especificación vigente](ESPECIFICACION.md).

**Criterio de aceptación comprometido:** antes de integración real de plataformas debe existir motor para **doce eras jugables** y entrada terminal a Interestelar, con PostgreSQL, 3 naciones, repetibilidad y ruta 0 chat/0 oro. **Antes del primer piloto**, arte real completo de las 12 eras/facciones y epílogo; Doctor K-0 LLM/TTS dinámico con fallback, HUD vertical/horizontal ES. Primer modo SINGLE_OPERATOR y YouTube Live posterior solo con cuentas verificadas. Las 20 decisiones están en `docs/ESPECIFICACION.md`; ninguna casilla puede marcarse sin ejecución y prueba.

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
- [ ] **Arte producido y aprobado para las 12 eras jugables y el epílogo Interestelar** en las tres facciones, con overlays vertical/horizontal ES; no bastan tres muestras.
- [ ] Sprite 16×24, 32×16 tile, sombras, paletas, variantes, HUD y animaciones probados a 1× y en stream vertical.
- [ ] Fuente, sonido, música, voz y derechos comerciales acreditados.
- [ ] Texto y subtítulos legibles sin depender de audio; safe areas verificadas por plataforma.

## Gate de cierre técnico

- [ ] **Migraciones de datos existentes probadas** con tests de concurrencia y rollback. Los scripts 001–003 pasan en PostgreSQL 16 **vacío**; este PASS aislado no certifica upgrade, handlers ni restore.
- [ ] Contratos REST/SignalR actualizados a las entidades efectivas y sus versiones.
- [ ] Ingesta idempotente, escritura única, determinismo, replays y backups restaurados con evidencia.
- [ ] Pruebas de carga y mediciones de costes con perfiles realistas y 30 FPS OBS estable.
- [ ] Autorización del proveedor, cuotas, política LIVE y límites de monetización comprobados por **cuenta**, no por idea.

## Gate multistreamer distribuido v2.3

- [ ] Una campaña de tres streamers independientes se completa desde 3 equipos y redes distintos sin ejecutar motor local en ninguno.
- [ ] Tres cuentas de mismo proveedor verificadas y tres overlays separados; mezclas de proveedores solo cuando los permisos reales lo demuestren.
- [ ] OBS de un streamer cae sin alterar LIVE certificado ni economía; desconexión LIVE de una nación congela simultáneamente reloj global de RPS en tres viewers.
- [ ] Invitaciones, scopes, OAuth, revocación, aislamiento de identidades y salida pública minimizada probados.
- [ ] `docs/ESPECIFICACION.md`, ruleset, catálogos, OpenAPI y SQL concuerdan; CI verde, migraciones PostgreSQL con datos históricos y restauración realmente ejecutadas.
- [ ] Cuenta real de proveedor, volumen de audiencia, arte, legal y restore con evidencia verificable, no texto.

**El estado permanece D1 ampliado; este añadido no demuestra D2 ni un juego implementado.**

## Gates de retorno, balance y coste

- [ ] Retorno del mismo broadcaster verificado y aprobado por OWNER **antes** del límite de 7 días; el retorno en igualdad de deadline se rechaza y `ABORTED` es terminal; segundo abandono genera nuevo incidente, sin doble Outbox.
- [ ] Torneo pausado caduca a las 72 horas UTC sin sanción y **no reabre** aunque posteriormente se reanude la temporada.
- [ ] El motor completo (no el simulador simplificado) alcanza 12 eras/5 hitos por era sin oro y con 24 NPC, **100 seeds** y perfiles 0/10/100/1000/10000; para 4 h LIVE/día el P50 de temporada está entre **45–90 días**. 0 h LIVE no debe avanzar era; publicar P10/P50/P90 y casos sin ruta.
- [ ] Infraestructura y LLM/TTS: **coste realmente medido ≤100 €/mes** en perfil de referencia de tres canales; fallback de narración automático ante presupuesto, cuotas o seguridad, sin degradar reglas. Publicar métricas y precio efectivo del proveedor, no una estimación sin pruebas.

## Gate de cierre comercial y normativo

- [ ] Distintividad registral/uso de K0 y Doctor K-0 comprobada en territorios elegidos.
- [ ] Titularidad/licencias de sprites, tipografías, voz, música y contenidos confirmadas.
- [ ] Política real de datos, acceso, retención y solicitudes de usuarios aprobada para la jurisdicción.
- [ ] Presupuesto de infraestructura, moderación, marketing, mantenimiento y operación basado en tarifas/uso verificables.
- [ ] Reglas de contribución económica verificadas con reversos reales o mantenidas apagadas.

## Política de aprobación

Cada casilla requiere documento, evidencia, responsable, fecha y versión. No «marcar completado» por haber escrito su intención. El propietario puede congelar un baseline **para desarrollo** sin que eso signifique que ya existe producto terminado. Las dependencias externas no son defectos que puedan arreglarse escribiendo más Markdown; deben mostrarse como gates, jamás como supuestos ocultos.
