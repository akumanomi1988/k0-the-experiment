# K0 / Project CHAOS — Registro de consolidación y excepciones v2.5

**Este documento hace auditable el merge.** No es una promesa de arte terminado, balance demostrado ni permiso de proveedor. Cada enmienda indica la fuente anterior, la interpretación vigente, el impacto y el trabajo de verificación pendiente. La [especificación maestra](ESPECIFICACION_MAESTRA_v2.5.md) es normativa; los [anexos](fuentes/) conservan todos los textos y las 92 decisiones sin borrado.

## A. Cambios consolidados que sustituyen reglas anteriores

| ID | Fuente histórica / contradicción | Norma única desde v2.5 | Impacto de desarrollo | Verificación |
|---|---|---|---|---|
| V25-01 | v0.8 fija TikTok/Micelios, Twitch/Rúnicos, YouTube/Ferrinos; docs 02/31 y v2.3 generalizan | Facción independiente de proveedor; tres bindings distintos; canales del mismo proveedor o mixtos si autorizados | Modelar Season/Nation separadas de Account/Binding | 3 channels same provider + mixed |
| V25-02 | v0.8 concibe juego distribuido no claramente remoto | Backend central .NET/PG; 3 streamers pueden vivir en PCs/redes distintas; OBS read-only | Identity, StreamerSeat, OAuth, OverlayOutput, invitations | 3-PC remote E2E |
| V25-03 | 3 naciones por un único chat parecía admisible en algunas explicaciones | No soportado: un canal pertenece a una nación/temporada | Enforce UNIQUE binding; mensajes sin nación se rechazan | Error routing test |
| V25-04 | Concepto de operador propietario de tres canales vs tres streamers | Season.broadcastMode SINGLE_OPERATOR o MULTI_STREAMER; segundo exige 3 cuentas K0 primarias distintas aceptadas | Preflight y RBAC por seat | No iniciar 2 accounts duplicate |
| V25-05 | v0.8 y antiguas decisiones asignaban oro a proyectos estratégicos | Consejo y maravillas: gold=0, todos accesibles con recursos ordinarios; oro solo cosméticos no competitivos | Eliminar GOLD en holds; ledgers separados | zero-donations full era |
| V25-06 | Varios Consejos posibles con solo 3 candidatos/era | Un único Consejo ordinario por nación/era; perdedores de terna no se reofertan ese ciclo | Idempotencia (nation,era), scheduler | Rechazar segundo Consejo |
| V25-07 | Hitos de misión ligados a rewards diarios/semanales y UTC | 12 misiones específicas de era; daily/weekly independientes | MissionEngine y catálogo v2.3 | 2 eras consecutivas en mismo día |
| V25-08 | En data/technologies isRequiredForMilestone=false para todas; milestones exige troncal | Flag true únicamente troncales eras 1–12; era 13 ceremonial | Catalog consistency / schema | 12 required IDs sin contradicción |
| V25-09 | Antiguos textos interpretan Interestelar como ciclo jugable | Era 13 terminal/epílogo; solo entrar en ella proclama ganador | Runtime postseason read-only | No obras/votos post-win |
| V25-10 | Docs 03/42 ordenan cierre de votos y economía de modo divergente | Secuencia única de fronteras: evento/commands→cierres→economía→obras/tech/misiones→hitos/era→global arbiter→commit/outbox | Deterministic engine | Test boundary replay hash |
| V25-11 | Fórmulas podían multiplicar 0.2 dos veces (4 % en vez de 20 %) | Factor OFFLINE 0.2 se aplica **solo** al delta temporal efectivo para economía/XP/comida | Integer accumulator | offline 60s=12s econ |
| V25-12 | RPS de tres streams podía avanzar con tres NationLiveClock diferentes | CompetitionLiveClock global único, avanza solo con 3 LIVE; cae una, se congela todo evento | Event clock + operator pause | 50 s restantes en A/B/C |
| V25-13 | OBS conectado equiparado implícitamente con LIVE | Fuente OBS independiente del estado proveedor; UI puede fallar sin alterar partida | ProviderHealth vs OverlayHealth | OBS crash isolation |
| V25-14 | IDs públicos NationId usaban nombre de facción, SQL usa UUID | NationId UUID interno/público de DTO, FactionId string separada | Contract validation, migrations | DB→API round-trip |
| V25-15 | Docs 19 state votes.PAUSED vs SQL CHECK sin PAUSED | PAUSED adoptado en diseño, solo tras migración real | DDL/DTO/updater | DB integration state transitions |
| V25-16 | P95 entrada→aplicación <1s vs tick económico 5s | P95 <1s como objetivo de ACK, no aplicación del tick; economía hasta siguiente tick | Separate ingress vs worker | Latency metrics |
| V25-17 | v0.8 proponía SQLite local como primera DB | PostgreSQL 16+ desde primer slice (con workers e Inbox/Outbox centrales) | Central ACID DB | Real SQL migrations |
| V25-18 | Público 10000 humanos y 24 NPC sin calibración | Control marginal de trabajo por profesión/nación según ruleset, todavía balance candidato | Cohort simulator | P10/P50/P90 by audience |
| V25-19 | Históricos menciones de gobierno elegible por espectadores | 3 NPC por nación/era, 1 cargo, 60m LIVE, 3m segunda vuelta; elección ciudadanos para NPC | Politics module | Ballot/tie deterministic |
| V25-20 | Personaje alien / coral y Doctor K-0 poco cyborg | Solo Micelios/Rúnicos/Ferrinos; K-0 claramente cyborg con ojo óptico y brazo mecánico | Art direction | Silhouette real test |
| V25-21 | Guerra continua, ataques o PvP libre no se especificaron consistentemente | Solo RPS triangular y batalla automática programados, 3 LIVE, daños acotados y sin muerte permanente | Competition Engine | Match+penalty tests |
| V25-22 | Monetización y políticas de plataformas tratadas como garantías | Cada capability + cuenta tiene evidence; TikTok no se presume accesible; monetización default OFF | Account security/platforms | Real platform gate |
| V25-23 | Catálogo de era 13 incluye edificios, misiones y tecnologías | Conservación íntegra como exposición/arte, NO acciones tras SeasonCompleted | Content availability filter | Terminal gating |
| V25-24 | "Implementado" en flags de diseño mientras sin código | Cambiar a design candidate; PASS solo con evidencia (commit, entorno, inputs, outputs, fecha) | Documentation gating | CI and engine test |
| V25-25 | Antiguas referencias de gold BUILD_COST en DDL | COSMETIC_SPEND es único consumo monetario habilitable en futuro, no BUILD_COST estratégico | DDL ledger upgrade | DB ledger tests |
| V25-26 | Narrador LLM aparentemente capaz de organizar y decidir reglas | ShowDirector whitelist+cooldown, LLM solo texto, resultados exclusivamente desde backend | Security boundary | Prompt injection and mutation rejection |

**Regla de prevalencia:** ningún anexo histórico reactiva la versión anterior de un punto V25-01…V25-26. Si surge conflicto nuevo, no ocultarlo: escribirlo en este registro, cambiar catálogo/contratos, añadir test y bump de content hash.

## B. Decisiones confirmadas y preservadas sin cambio mecánico

Las 92 decisiones se preservan íntegramente en [registro](fuentes/DECISIONES_1_92.md) y en [JSON original](../data/legacy_user_decisions_1_92.json). Se mantienen: tres naciones, NPC sin público, fin al llegar primero a era final, profesiones permanentes, actividad 2h, historial entre temporadas, hambre sin muerte, almacenes con límite, obras automáticas vs estratégicas votadas, tres candidatos NPC, narrador sarcástico neutral, torneos anunciados, biomas sin ventajas, arte pixel retro y no microservicios en MVP. Los cambios históricos registrados REPLACED/PARTIALLY_REPLACED no se interpretan como norma actual.

Los capítulos [18](../docs/18_DECISIONES_DE_BASE_CORREGIDAS.md), [41](../docs/41_AUDITORIA_DE_COMPLETITUD_Y_JERARQUIA_v2.2.md) y [auditoría C-01..C-18](../audit/AUDITORIA_K0_PROJECT_CHAOS_V2_2.md) se conservan; no todos sus textos son actuales, pero constituyen la justificación documental.

## C. Estado real de artefactos después del merge

| Clase | Situación | Qué significa |
|---|---|---|
| 67 capítulos + 92 decisiones | Copia íntegra preservada en v2.5/fuentes | Cobertura histórica completa de definiciones y trade-offs |
| Especificación maestra v2.5 | Consolidada y normativa en lo explícito | Se puede diseñar/planificar sin acudir a 4 versiones contradictorias |
| Catálogos JSON v2/v2.2/v2.3 | Los actuales siguen siendo datos de referencia | Evitar renombrarlos engañosamente sin versión de esquema o migración |
| SQL 001/002/003 | Diseños, no cadena de migraciones ejecutadas | Integrar/versionar bajo código y PostgreSQL real |
| OpenAPI/JSON Schema | Baselines de contratos, no API implementada | Generar DTO y comprobar schema drift |
| Validador estático | Herramienta de catálogo/CI, no simulador completo | No marca balance/fall-back PASS |
| Sprites, audio, voces, HUD reales | NO PRODUCIDOS/NO APROBADOS | Spec visual != arte final |
| Integraciones LIVE y monetización | NO AUTORIZADAS POR CUENTA | Proveedor no se habilita por documentación |
| Balance de 12 eras, 3 streamers reales | NOT_RUN | Necesita motor y ensayos de desconexión |
| Licencias, RGPD, presupuestos | GATES EXTERNOS | Documentos técnicos no sustituyen contrato/legal |

## D. Riesgos y zonas donde no sería veraz declarar «sin flecos»

1. **Equidad de horas de emisión:** 100% LIVE vs 20% offline es regla vigente, pero tres streamers con horarios desiguales pueden producir carreras descompensadas. Falta experiencia empírica y simulación; no inventar sistema compensatorio.
2. **Balance/monótono por era y oficio:** las tasas y límites actuales se fijan como candidatos, no como equilibrio certificado. Simulación NPC vs público extremo pendiente.
3. **Tecnología real de proveedor:** APIs y scopes por cuentas concretas, especialmente TikTok, sujetos a políticas cambiantes; no se puede aprobar sin conexión/verificación.
4. **Phaser/OBS CEF real:** FPS, safe areas y sincronía de presentación se verifican en tres ordenadores físicos y formatos.
5. **Arte, fuentes, derechos y voz:** briefing suficiente para producción pero sin aprobación de entregables gráficos; la literalidad «final» solo se refiere a norma de diseño, no a píxeles producidos.
6. **Migraciones y esquemas:** SQL 001/002/003 sigue siendo referencia, no garantía que se haya ejecutado; uniones, CHECK y contratos de proveedor deben comprobarse con DB.
7. **Producto SaaS futuro:** pricing, tenancy, SLA y derecho comercial no son necesarios para probar el producto propio; no deben presentarse como desarrollados.

## E. Procedimiento de cambios posteriores a v2.5

Todo PR de cambio de norma debe incluir: identificador V25-xx / decisión 1–92 impactada; antes/después; impacto en gameplay, esquema, renderer, integraciones, seguridad, UX y arte; referencias del catálogo; migración si hay datos vivos; escenarios y pruebas; versión de reglas/hash y compatibilidad de temporada. Si es una mejora que depende de datos reales, estado PROPOSED/PENDING_VALIDATION hasta obtenerlos. Nunca modificar en caliente una temporada RUNNING por actualizar el Markdown.

**Definición estricta:** v2.5 puede ser **documentación consolidada**, no «software completo» ni «juego listo para producción». Ésta es una distinción contractual para evitar deuda de implementación y falsas promesas.
