# K0: The Experiment / Project CHAOS — Auditoría de coherencia y decisiones pendientes

**Fecha:** 2026-11-07  
**Base:** documentación de Project CHAOS v0.8 aportada en el proyecto; repositorio GitHub `akumanomi1988/k0-the-experiment`, rama `main`, documentación v2.2.  
**Alcance:** revisión estática documental y de catálogos; **no** es una auditoría de código ejecutable, integración LIVE ni prueba de balance.  
**Regla:** no abrir nuevas rondas de preguntas. Las propuestas siguientes no sustituyen automáticamente las 92 decisiones históricas.

## Diagnóstico ejecutivo

El repositorio declara 62 capítulos de especificación, catálogos numéricos, esquema SQL y contratos JSON/OpenAPI. Su README establece expresamente **sin aplicación implementada**; `docs/60` clasifica el diseño como **D1 ampliado**, no D2/D3/D4. No se ha verificado un motor que complete una temporada real. Aun cuando existen 13 eras, 130 definiciones de edificios básicos, 39 proyectos, 13 maravillas, 30 opciones de habilidad y 39 tipos de unidades, esas cifras son **inventario documental**, no funcionalidad terminada.

### Inventario de hallazgos y resolución propuesta

| ID | Prioridad | Hallazgo sustentado | Corrección recomendada | Prueba de cierre |
|---|---|---|---|---|
| C-01 | CRÍTICA | `docs/03` cierra votos antes de producción/avance de era; `docs/42` los cierra después. En simultaneidad, cambia el ganador o qué votos se aceptan. | Unificar una especificación normativa del ciclo de ejecución; motor y tests deben consumir idéntica secuencia. | Replays con voto/obra/hito/victoria en el mismo instante producen idéntico estado y hash. |
| C-02 | CRÍTICA | `docs/04` emplea `deltaEconomySeconds` para minutos efectivos y también incluye `economyBp` en fórmula; `docs/06` puede multiplicar otra vez la XP offline por 0,2. Hay riesgo de aplicar 20 % dos veces (4 %). | Derivar **un solo** `economyDelta` de wall time × factor y usarlo en producción, hambre, XP y obra, sin aplicar de nuevo el factor. | Un intervalo de 60 s offline produce exactamente 20 % del equivalente LIVE, salvo topes y redondeo comprobable. |
| C-03 | CRÍTICA | Los hitos `knowledge_production` exigen `requiresTechnologyId=tech_{era}`, pero todas las tecnologías en `data/technologies.v2.json` declaran `isRequiredForMilestone=false`. | Eliminar propiedad redundante `isRequiredForMilestone` o generarla desde referencias de hitos; no aceptar dos autoridades contradictorias. | Validador de catálogo detecta todos los prerrequisitos y no permite referencias cruzadas inconsistentes. |
| C-04 | CRÍTICA | `docs/19` define estado `PAUSED` en votaciones; `architecture/001_schema_v2.sql` restringe estados de `votes` a `QUEUED, OPEN, RESOLVED, CANCELLED, PAYMENT_BLOCKED`. | Versión única de estados para motor, SQL y API; migraciones idempotentes. | Caso `LIVE→UNCERTAIN→LIVE` mantiene papeletas y segundos restantes, sin excepciones SQL. |
| C-05 | ALTA | `docs/03` envía comando al siguiente tick de 5 s y `docs/55` promete latencia P95 de ingreso→aplicación inferior a 1 s. | Desacoplar `CommandProcessor` de tick económico (aplicar enseguida tras persistir y ordenar) o modificar SLO explícitamente. | Prueba de carga con hora de recepción, ingestSeq, commit y P95 real. |
| C-06 | ALTA | 3 proyectos por era, pero Consejo exige 3 opciones no construidas; al construir una quedan 2. `docs/44` dice que las otras pueden presentarse en futuros Consejos aunque la elegibilidad sea solo la era actual. | Especificar **un Consejo por nación y era**; tras decidir, cerrar la terna y dejar los perdedores como alternativas descartadas para esa temporada, salvo evento extra expresamente definido. | 2.º Consejo de misma era es rechazado con causa `COUNCIL_ALREADY_RESOLVED`. |
| C-07 | ALTA | SQL usa `nations.nation_id uuid` y `faction_id`; OpenAPI/JSON Schema usa `nationId` enum `micelios/runicos/ferrinos`; `NationDelta` también difiere entre OpenAPI y esquema JSON. | `NationId` UUID interno y `FactionId`/`nationSlug` explícito en DTO público. Generar OpenAPI y JSON schemas de una única fuente de contratos. | Round trip DB→DTO→client sin IDs ambiguos y contrato CI sin drift. |
| C-08 | ALTA | El evento RPS solo empieza con 3 naciones LIVE, pero cada nación tiene reloj LIVE propio. Si una cae a mitad de ronda las ventanas pueden desincronizarse. | Añadir `CompetitionLiveClock` global que avance solo cuando **todas** estén LIVE; una caída congela el evento entero y un timeout operativo puede cancelarlo sin sanción. | Desconectar nación B a los 40 s: A/B/C conservan 50 s restantes de la ronda. |
| C-09 | ALTA | Históricamente el oro financiaba proyectos estratégicos (v0.8); revisión v2.2 asigna `gold=0` a todos, reservándolo a cosméticos. Es una sustitución de diseño material, no una cifra menor. | Adoptar la corrección gratuita **sin ocultar** el cambio: documentar override explícito de la decisión histórica y diferenciar `CouncilProject` gratuito de `CosmeticSponsorship` monetizado y no competitivo. | Trazabilidad 1–92 y prueba de temporada de 0 oro con Consejo funcional. |
| C-10 | ALTA | `docs/07` declara fin de temporada al entrar en Interestelar; los catálogos todavía contienen 10 edificios, 3 proyectos, 5 hitos, 3 tecnologías y 1 maravilla interestelares. | Tratar Interestelar como epílogo, con `availability=EPILOGUE_ONLY`, sin órdenes competitivas; no producir assets operativos inútiles antes de lanzar. | Ningún autoplanner/Consejo/elección se abre después de `SeasonCompleted`. |
| C-11 | ALTA | Misiones diarias/semanales se consumen una vez por período UTC; la barra exige una misión *en cada era*. Un progreso muy rápido puede bloquearse esperando el siguiente período. | Introducir `EraMission` colectiva, renovada al entrar en una era y completada por NPC, distinta de recompensas diarias/semanales; conserva el hito gratuito. | Con 0/10k participantes, dos eras consecutivas pueden avanzar sin depender del siguiente cambio de día UTC. |
| C-12 | ALTA | El reparto de trabajo humano usa 100 trabajadores al 100 % y otros al 25 % hasta 2.500 **por oficio** en docs 04/06, mientras `ruleset.citizens.activeHumanWorkersSoftCap=2500` no declara alcance. Rendimiento total puede superar masivamente a 24 NPC. | Definir inequívocamente cap por nación y distribución por oficio; calibrar hitos con perfiles 0/10/100/1000/10k. Evitar que ingresos o audiencia compren progresión. | P10/P50/P90 de duraciones de 12 eras y desigualdad entre comunidades; topes documentados y medidos. |
| C-13 | MEDIA | `data/strategic_projects.v2.json.candidatePool` dice literalmente `no gold means no vote`, contrario a v2.2. `docs/05` aún menciona reversión de oro en Consejo, aunque coste oro=0. | Corregir documentación y cadenas de datos; validador textual de términos deprecados y tabla de autoridad. | No aparecen reglas monetarias antiguas en catálogos activos. |
| C-14 | ALTA | `architecture/002_extensiones_diseno_v2.2.sql` explica que la compra de cosméticos necesita extender CHECK de `resource_ledger`, y OpenAPI/SQL v2.2 no están integrados. No hay migraciones ejecutadas. | Integrar DDL y contratos en primera migración versionada **antes** de escribir módulos dependientes; no activar monetización. | CI crea esquema limpio, migra/revierte en desarrollo, prueba deuda, ledger, voto y patrocinio. |
| C-15 | MEDIA | El oficio `build` solo gana XP si hay trabajo real y el autoplanner limita obras; puede sufrir mucho tiempo improductivo respecto a `food/research`. | Medir utilización; si hay periodos vacíos, introducir tareas de mantenimiento real con utilidad acotada (no XP ficticia) sin cambiar profesión. | Distribución XP/h por oficio y tiempo ocioso medidos en 12 eras. |
| C-16 | MEDIA | `data/ruleset.v2.json.status=IMPLEMENTATION_BASELINE`, aunque README confirma que no existe implementación. | Renombrar a `DESIGN_BASELINE_CANDIDATE` y mantener estados D0–D4 como evidencias separadas. | CI y docs no anuncian “implementado” donde solo hay JSON. |
| C-17 | ALTA (LANZAMIENTO) | El modelo vigente exige 3 fuentes de chat distintas, una por nación; no contempla una sola cuenta LIVE para tres facciones. TikTok LIVE está bloqueado hasta permisos comprobados. | P0 en tres fuentes sintéticas; P1 un adaptador real en entorno controlado; temporada pública competitiva solo con tres fuentes verificadas. El modo un canal/tres naciones sería **otro producto/ADR**, no una suposición. | Tres canales independientes, reconexión, políticas de overlay y trazabilidad de comandos por nación. |
| C-18 | MEDIA | `docs/60` exige para D2 una temporada completa simulada de 13 eras aun cuando el vertical slice P0 del documento histórico solo implementa 1–3 eras. | Dividir `READY_FOR_P0` y `READY_FOR_PUBLIC_SEASON`; no bloquear ingeniería del slice por balance de toda la temporada, pero sí el lanzamiento. | P0 probado con Paleolítico; primer lanzamiento solo con simulación completa 1–12. |

## Pendientes externos que NO se resuelven con otra ronda de preguntas

**Integración:** permisos/scopes, estabilidad, reglas de simulcast y mensajes por proveedor y cuenta; evidencia especial para TikTok. **Arte:** sprites/tiles/UI aprobados a resoluciones OBS reales, siluetas definitivas, personaje K-0. **Calidad de producto:** que espectadores nuevos entiendan onboarding y recuerden volver, latencia efectiva, 30 FPS en hardware objetivo. **Negocio/legal:** derechos de marca K0, música, voz, sprites, privacidad, RGPD, monetización y costes reales. Son *gates*, no características implementadas.

## Decisiones técnicas recomendadas sin pedir nuevas respuestas

**A. Fuente de verdad.** Crear `docs/CURRENT_SPEC.md` breve con jerarquía e IDs de ADR; conservar documentos antiguos como `historical`. Toda regla activa debe tener un único origen de verdad y los JSON validados en CI.

**B. Backend.** .NET 10 monolito modular, un escritor lógico por nación, arbitraje global para ganador/maravilla, PostgreSQL desde desarrollo para igualar concurrencia y migraciones de producción. No microservicios ni cola externa en P0.

**C. Modelo temporal.** Ingesta asíncrona idempotente; comandos ordenados por `ingestSeq`; economía determinista por segmentos de tiempo; cómputo de voto basado en reloj LIVE acumulado y recepción persistida, no un `closeUtc` fijo si una votación puede pausarse. RPS usa reloj global de evento.

**D. Contenido.** Hacer jugable una sola era con cinco profesiones, cinco hitos reales, misión de era, NPC, autoconstrucción, un Consejo gratuito, overlay y K-0 textual. Segunda fase 2–3 eras y gobierno; tercera fase 12 eras competitivas con epílogo Interestelar. Mantener arte modular por facción y época.

**E. Monetización.** `gold` sin efecto mecánico y disabled por defecto. Patrocinios cosméticos únicamente después de validación real y revisión legal. Nunca usar el texto de chat para acreditar valor.

## Plan de implementación y aceptación

| Orden | Entrega | Gate |
|---|---|---|
| 1 | Correcciones C-01–C-14 que afectan contratos/reglas, y reglas normativas v2.3 | Validación estática de datos, SQL local, test de estados y replay corto |
| 2 | Vertical slice local: una era de tres naciones y entradas sintéticas | Sin duplicados, cinco hitos reales, ninguna vía pagada, OBS funcional |
| 3 | Modelo de balance reproducible y segunda/tercera eras, misiones, política, competencia | Replay misma seed/eventos, escenarios 0/10/100/1000/10k, ausencia de deadlocks |
| 4 | Una integración LIVE autorizada, visuales y seguridad del operador | Evidencia por cuenta y fallos de red controlados |
| 5 | Temporada pública completa de doce eras jugables más epílogo | Pruebas de balance/recuperación, legal, plataforma, arte, costes y operativa acreditadas |

## Fuentes principales

- [Repositorio y README v2.2](https://github.com/akumanomi1988/k0-the-experiment)
- [41 Auditoría de completitud y jerarquía](https://github.com/akumanomi1988/k0-the-experiment/blob/main/docs/41_AUDITORIA_DE_COMPLETITUD_Y_JERARQUIA_v2.2.md)
- [60 Gates D0–D4](https://github.com/akumanomi1988/k0-the-experiment/blob/main/docs/60_DEFINITION_OF_READY_Y_GATES_DE_CIERRE_v2.2.md)
- [03 Relojes y orden](https://github.com/akumanomi1988/k0-the-experiment/blob/main/docs/03_TIEMPOS_SIMULACION_Y_DETERMINISMO.md)
- [42 Contratos temporales](https://github.com/akumanomi1988/k0-the-experiment/blob/main/docs/42_CONTRATOS_DE_ESTADOS_Y_TIEMPO_v2.2.md)
- [04 Economía](https://github.com/akumanomi1988/k0-the-experiment/blob/main/docs/04_ECONOMIA_Y_BALANCE.md)
- [07 Progresión](https://github.com/akumanomi1988/k0-the-experiment/blob/main/docs/07_PROGRESION_TECNOLOGICA_Y_TEMPORADAS.md)
- [08 Consejo y elecciones](https://github.com/akumanomi1988/k0-the-experiment/blob/main/docs/08_GOBIERNO_VOTACIONES_Y_CONSEJO.md)
- [44 Consejo gratuito](https://github.com/akumanomi1988/k0-the-experiment/blob/main/docs/44_CONSEJO_GRATUITO_PATROCINIO_Y_ECONOMIA_v2.2.md)
- [55 Arquitectura](https://github.com/akumanomi1988/k0-the-experiment/blob/main/docs/55_ARQUITECTURA_TECNICA_Y_LIMITES_v2.2.md)
- [SQL base](https://github.com/akumanomi1988/k0-the-experiment/blob/main/architecture/001_schema_v2.sql), [SQL v2.2](https://github.com/akumanomi1988/k0-the-experiment/blob/main/architecture/002_extensiones_diseno_v2.2.sql)
- [Data: hitos](https://github.com/akumanomi1988/k0-the-experiment/blob/main/data/milestones.v2.json), [tecnologías](https://github.com/akumanomi1988/k0-the-experiment/blob/main/data/technologies.v2.json), [proyectos](https://github.com/akumanomi1988/k0-the-experiment/blob/main/data/strategic_projects.v2.json)

**Seguridad del análisis:** alta para contradicciones textuales y campos inspeccionados; moderada para impacto de balance por no existir ejecución real. **Este informe documenta hallazgos y propuestas; su incorporación al repositorio no modifica por sí misma reglas de juego ni código.**