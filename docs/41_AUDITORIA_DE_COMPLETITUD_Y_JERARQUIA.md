> **Nota de vigencia:** auditoría histórica de revisión v2.2. Las enmiendas posteriores y el diseño multistreamer están registrados en [especificación vigente](ESPECIFICACION.md), [arquitectura distribuida](63_ARQUITECTURA_MULTISTREAMER.md) y [blueprint QA](67_BLUEPRINT_IMPLEMENTACION_Y_PRUEBAS.md). No asumir que los gates se han validado.

**Vigencia:** la autoridad actual es `docs/ESPECIFICACION.md` y sus veinte decisiones ratificadas, no esta auditoría histórica. La cuota humana es **única por nación**, no por profesión. Primera entrega: doce eras antes de proveedores; YouTube Live después de comprobar permisos. Esta auditoría describe riesgos y verificaciones, no reglas alternativas.

# 41 — Auditoría de completitud, decisiones y jerarquía v2.2

**Estado: REVISIÓN DOCUMENTAL, NO VERIFICACIÓN DE PRODUCTO.** Este archivo es el índice de riesgo vigente. No debe publicarse la expresión «100 % terminado», «balance certificado» o «arte final» sin evidencia. K0: The Experiment es el nombre público de trabajo; Project CHAOS permanece en identificadores heredados.

## Qué está definido y qué no

| Eje | Especificado | Evidencia que todavía falta | Criterio de cierre |
|---|---|---|---|
| Visión y usuarios | Tres facciones, temporadas, chat, NPC, directo, Doctor K-0 | Prueba con espectadores nuevos | Cinco sesiones moderadas sin intervención explicativa |
| Reglas principales | 13 eras, 5 oficios, 5 hitos, cronómetros LIVE, votos, RPS | Consistencia entre reglas y eventos reales | Modelo de referencia reproducible + aceptación de escenarios |
| Economía | Valores exactos propuestos en ruleset y catálogos | Balance de todas las eras con 0/10/100/1000/10k humanos | 100 simulaciones por perfil, sin bloqueo y distribución publicada |
| Obras y Consejo | 130 básicos, 39 proyectos, 13 maravillas | Comportamiento ante saturación de espacios/colas | Completar rutas con 0 aportaciones; no hay Consejo invocable sin 3 opciones pagables |
| Ejército | Catálogo nuevo de 39 unidades por era/rol, evento automático propuesto en v2.2 | Comprobación de fórmulas y dramaturgia | 3 pares, empates y penalizaciones deterministas |
| Interfaz | Escenas, HUD, proporciones y layout base | Aprobación de wireframes y accesibilidad con contenido real | Capturas vertical/horizontal revisadas a resolución destino |
| Arte | Pixel art 2:1, reglas de silueta, paletas de facción | Sprites, tiles, efectos y diseño final de K-0 | Style frames de 3 facciones, 3 eras muestra y assets testados |
| Audio | Contratos de cue y guion, pauta v2.2 | Voz/licencias y mezcla real | Escucha en móvil, subtítulos y fallback sin TTS |
| Integraciones | Bindings y contratos | Permisos, cuotas, autenticación y políticas de proveedores | Matriz de proveedor verificada por cuenta |
| Backend | Responsabilidades, transacciones, SQL propuesto | Migraciones y carga real | SQL ejecutable, tests de integridad y recuperación |
| Seguridad/legal | Principios y amenazas | Dictamen contextual y verificación de jurisdicción | Evidencia aprobada; nunca inferir permiso de una API |
| Negocio | Hipótesis de juego y futuro SaaS | Costes reales, adquisición, marca, políticas | Plan financiero y viabilidad ajustados a datos |

## Hallazgos auditados y resolución documental

- **D-01 — Alta:** todos los proyectos de Consejo y maravillas exigían oro, a pesar de que los eventos monetarios reales están apagados. Corrección de diseño v2.2: los costes de oro de esos elementos pasan a **cero**. Se mantiene el coste de recursos ordinarios y el prestigio; la participación gratuita deja de depender de donaciones. Las compras de oro se reservan para reconocimientos cosméticos separados. Ver `data/strategic_projects.json`, `data/cosmetic_sponsorship.json`, capítulo 44.
- **D-02 — Alta:** tecnologías afirmaban desbloquear talleres y centros de investigación mientras el catálogo de edificios tenía `requiresTechId=null`. Corrección v2.2: las dos familias por era requieren ahora su tecnología básica. La producción natural de conocimiento evita dependencia circular. Ver capítulos 07/45.
- **D-03 — Alta:** el registro histórico confirma ejércitos automáticos, pero no había unidades ni combate detallado. Propuesta parametrizada v2.2: `data/combat_units.json` + capítulo 43. No afirmamos balance real.
- **D-04 — Media:** habilidades con nombres de ahorro/reparación implicaban efectos nacionales que su JSON no tenía. Se han cambiado **descripciones**, no efectos; el `effect.target` sigue siendo la fuente de verdad. Revisión futura de UX necesaria para que nombres no induzcan a error.
- **D-05 — Alta:** `BALANCE_SIMULATION_REFERENCE.json` es un modelo grueso, incluye `milestonesAchieved:0` en escenarios que llegan al final; no constituye una verificación de los cinco hitos ni del motor. Queda marcado **HISTÓRICO NO AUTORITATIVO**.
- **D-06 — Media:** se habla de un árbol tecnológico, pero el contenido está formado por tres ramas homogéneas por era. Se concreta el lenguaje artístico/narrativo en capítulo 45, manteniendo bonos existentes. Una verdadera diversificación mecánica requeriría otro balance.
- **D-07 — Alta:** no existían wireframes pixel-precisos aprobados ni un pase de accesibilidad. Capítulos 46–50 concretan contratos visuales, pero **no sustituyen un art test físico**.
- **D-08 — Media:** `Project CHAOS` y `K0: The Experiment` se mezclaban. Se declara K0 como marca de trabajo visible; nombres de archivo y contratos CHAOS quedan por compatibilidad hasta migración futura, no como dos marcas de producto.
- **D-09 — Alta:** el producto requiere tres canales únicos, no un chat único para tres naciones. Este límite se mantiene explícito. No prometemos asignación multi-nación de un solo chat.
- **D-10 — Alta:** el SQL es un esquema propuesto y puede no soportar aún los nuevos catálogos de ejército/patrocinio. Se ha redactado el anexo `architecture/002_extensiones_diseno.sql` y contratos conceptuales, pero deben integrarse como **migraciones y APIs versionadas** antes de desarrollo, sin declarar compatibilidad automática.

## Autoridad cuando hay contradicción

1. Mensaje explícito posterior del propietario. 2. Decisiones históricas 1–92 salvo sustitución documentada. 3. Decisiones v2.2 de esta revisión *solo para el alcance listado* D-01–D-10. 4. JSON de datos vigente y contratos. 5. Documentos 01–40 de v2.1; cualquier texto que afirme que el Consejo requiere oro se considera histórico. 6. Documentos de versiones previas.

Cada cambio de regla debe incluir `id`, antes, después, razón, impacto, archivos, necesidad de migración y pruebas; una temporada activa jamás cambia de versión sin cierre auditado.

## Semántica de los estados de cierre

- **LOCKED_DESIGN**: decisión exacta documentada, aún no necesariamente probada.
- **CANDIDATE_BALANCE**: cifra reproducible propuesta, modificable solo entre temporadas, pendiente de simulación.
- **VISUAL_BRIEF**: orden de producción, no aprobación de arte.
- **PROVIDER_GATE**: capacidad externa no acreditada; debe permanecer deshabilitada.
- **IMPLEMENTATION_GATE**: se requiere software y pruebas reales, imposible cerrar con prosa.
- **APPROVED**: existe evidencia técnica, artística o legal trazable. Ningún módulo del repositorio puede presumir `APPROVED` por figurar en una tabla.
