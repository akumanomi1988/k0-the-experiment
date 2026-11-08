# 67 — Blueprint de implementación, entregas y matriz de verificación (v2.3)

**Normativo para planificación de desarrollo; estados de tests NOT_RUN.** Describe cómo desarrollar todo el producto sin inventar evidencias. Complementa docs 15,38,40,57,60 y auditoría C-01 a C-18.

## 1. Producto objetivo y límites

Producto de referencia: 3 naciones (Micelios, Rúnicos, Ferrinos), 13 eras (1–12 jugables, 13 epílogo), 5 profesiones, NPC que completan ruta gratuita, 130 edificios básicos, 39 proyectos, 13 maravillas, 39 definiciones de unidad/rol/era, gobiernos/equipo político, RPS y combate programado, Doctor K-0, mapas persistentes pixel art y economía no pay-to-win. Tres streamers reales en tres PCs distintos y tres fuentes de chat válidas, mezclables entre proveedores autorizados. Una temporada puede continuar con horarios LIVE distintos; torneos exigen tres LIVE simultáneos.

No se pretende construir de golpe: la evidencia de cierre se acumula por gates y módulos; no se prometen APIs que un proveedor no ofrezca.

## 2. Stack congelado para prototipo

- .NET 10 / C#: monolito modular con API ASP.NET Core y BackgroundService worker. Separar ensamblados Domain, Application, Infrastructure, Api, Simulation y Contracts con interfaces claras, sin reflejar capas por cada entidad si no aportan valor.
- PostgreSQL 16+: migraciones reproducibles desde DB vacía, transacciones ACID, versión optimista y advisory/row locks; nunca SQLite como DB real.
- React + TypeScript + Phaser (versión compatible con OBS CEF que supere prueba) para overlay, panel propietario y portal del streamer. SignalR como transporte.
- JSON Schema/OpenAPI generados/validados en CI, DTO .NET tipados; contratos versionados y hash de contenido.
- Integración de Twitch EventSub / YouTube oficial desde backend; TikTok bloqueado hasta contrato y prueba. Local adapter sintético para desarrollo y tests.
- Tests xUnit o equivalente, Testcontainers PostgreSQL para integración, browser tests Playwright y OBS hardware test manual reproducible.
- Sin servicios de pago, TTS obligatorio, Redis, Kafka, Kubernetes ni multi-tenant SaaS en primera entrega.

## 3. Estructura de repositorio objetivo

    /src/K0.Domain                         # invariantes, estados, relojes, recursos
    /src/K0.Application                    # commands/queries, casos de uso, permisos
    /src/K0.Infrastructure                 # PostgreSQL, inbox, outbox, provider auth
    /src/K0.Simulation                     # segmentador, economy tick, RNG, arbitraje
    /src/K0.Api                            # REST, OIDC, SignalR, health
    /src/K0.ConnectorWorker                # adaptadores LIVE y polling/webhooks
    /web/overlay                           # Phaser/React escenas streamers
    /web/portal                            # invitaciones, propietario, operator
    /contracts                             # OpenAPI y schemas generados
    /data                                  # content manifests y reglas versionadas
    /architecture                          # migraciones versionadas; scripts 001/002/003 son históricos de DISEÑO
    /test/K0.UnitTests
    /test/K0.IntegrationTests
    /test/K0.SimulationTests
    /test/K0.ContractTests
    /test/K0.BrowserTests
    /docs                                  # specs y ADR
    /.github/workflows                    # CI build/test/contract/format

Un cambio de juego empieza en contrato/manifest/test; lógica y UI solo consumen esas fuentes. No duplicar umbrales a mano entre servidor, TS y JSON.

## 4. Modelo y algoritmos mínimos de producción

- Asignación: Campaign→Season→3 Nation + StreamerSeats→ProviderConnection→ChannelBindings→ProviderLiveSession→BroadcastOutputs.
- Inbox: guardar sourceKey único con transacción; validar firma, timestamp, binding y rol; normalizar; secuencia de ingesta; event outbox tras commit. At-least-once en transporte, exactamente una mutación por clave/cause.
- SimulationClock: relojes tipados, partición de segmento a fronteras, deltas de 5s, enteros milésimas/bp con restos persistentes y RNG counters por dominio/nación.
- Economy: población NPC/humana efectiva por profesión y era, hambre, almacenes, reserva/consumo, autoplanner, XP, tecnologías, hitos, era/misión.
- Governance: votaciones OPEN/PAUSED/RESOLVED, deadline LiveClock, empates RNG reproducible, prioridad, único Consejo/nación/era, cobro atómico de vector hold del ganador.
- Competition: RPS y batalla automática programados, ThreeNationLiveGate y CompetitionLiveClock; sin pago y sin sanción por caída de proveedor.
- SeasonArbiter: SeasonSequence global serializable; único ganador interestelar, exclusividad global de maravillas y frozen post-season.
- Views: snapshots con versions/hash, deltas contiguos y presentación desacoplada. Un overlay conectado nunca es origen de comandos financieros.
- Security: membresías, OAuth, minimización de datos, scopes, revocación por canal/output, auditoría; provider token server-only.

## 5. Migración de esquema necesaria

Los SQL 001 (base), 002 (ejércitos/patrocinio) y 003 (multistreamer) documentan **intención**, no constituyen una cadena de migraciones ya ejecutada. Para implementación:
1. Convertirlos en migrations numeradas nuevas y autocontenidas; revisar type/FK de NationId, FactionId y estados; evitar asumir columna/constraint names sin ejecutar.
2. Integrar PAUSED para votes, estados batalla y licencias/streamer; extender resource_ledger con COSMETIC_SPEND sin permitir BUILD_COST de oro legado.
3. Agregar CampaignMembership, StreamerSeat, ProviderConnection, ProviderLiveSession, BroadcastOutput, OutputSession, PresentationCue, AuthorityAudit y limits de UNIQUE.
4. Probar el conjunto en PostgreSQL real: levantar vacío, seed de 3 naciones, rollback en DB de test, constraints y locks; realizar restore/snapshot con recursos.
5. Separar schema de dominio de proyecciones; SQL no se deriva de la posición de sprites.

## 6. Orden de entrega con artefactos y aceptación

| Fase | Entregable verificable | Criterio de salida |
|---|---|---|
| **P0 — Contratos** | CURRENT_SPEC, validadores JSON y contratos TS/C#, migraciones reales, CI, matrices C-01–C-18 | Cero referencias huérfanas/ciclos de progreso; tests en verde |
| **P1 — Simulación** | 3 naciones en memoria + PostgreSQL, 24 NPC cada una, 5 oficios, Paleolítico y todos sus hitos | 0 chat/0 oro completa primera era bajo LIVE sintético |
| **P2 — Experiencia** | Overlays 360×640/640×360, K-0 textual, portales, escenas, Consejo/elecciones | 3 Browser Sources sincronizados por evento y reconnect |
| **P3 — Remoto** | Invitación, OAuth de K0, roles, 3 streamers de 3 redes, tres bindings simulados | OBS de uno cae sin modificar economía/torneo ajeno |
| **P4 — Contenido** | Eras 2–12, arte modular, 130 básicos, proyectos, maravillas, batallas, políticas | Simulación íntegra 12 eras, sin deadlock, hash reproducible |
| **P5 — Proveedores** | Twitch/YouTube (los que demuestren permisos), LIVE health, reconexión, cuota, uso cruzado | 3 canales reales y cuentas autorizadas, failover ensayado |
| **P6 — Lanzamiento** | QA arte/accesibilidad, 30 FPS OBS, privacidad/licencias, backups/alertas, balance y costes | D4/public gate con evidencias, no checklist teórico |
| **P7 — SaaS eventual** | Campañas de terceros, billing, aislamiento multi-tenant, SDK/adaptadores | Solo después de validación de retención y ROI |

**P1/P2 son desarrollo incremental**, no garantía de que K0 completo esté validado; D2 de temporada completa y D4 siguen siendo distintos.

## 7. Auditoría C-01–C-18: estado de remediación

| ID | Decisión normativa v2.3 | Trabajo pendiente |
|---|---|---|
| C-01 | Orden canónico doc 64 | Test frontera y cambiar docs 03/42/SQL |
| C-02 | Un solo economyDelta offline 0.2 | Quitar doble factor de código y XP, test 60s |
| C-03 | Referencias de hitos son autoridad de tech | Generar propiedad derivada o eliminar campo contradictorio |
| C-04 | Votes PAUSED | Migración SQL y contratos |
| C-05 | ACK rápido, economía cada 5s | SLO separado y prueba de latencia |
| C-06 | Un Consejo por era/nación | Scheduler y rechazo al repetir |
| C-07 | NationId UUID, FactionId slug | Actualizar contratos/DTO/DB |
| C-08 | CompetitionLiveClock global | Integración y desconexión real |
| C-09 | Proyectos y maravillas gratuitos | Trace histórica y tests zero-gold |
| C-10 | Interestelar epílogo | Gating de contenido y eventos terminales |
| C-11 | EraMission propia | Catálogos, scheduler, prueba de dos eras mismo día |
| C-12 | Balance de humanos candidato | Simular perfiles y decidir límites después |
| C-13 | Texto viejo sobre oro inválido | Limpiar docs y JSON con CI |
| C-14 | SQL 001/002/003 no migrado | Migrations y test transaccional |
| C-15 | Constructor XP ocioso | Instrumentación y ajuste tras simulación |
| C-16 | IMPLEMENTATION_BASELINE engañoso | Renombrar status a design candidate |
| C-17 | Tres canales distintos | Pruebas de proveedor y modo simulado |
| C-18 | Gate de prototipo ≠ gate público | Gates separados y evidencias |

Las decisiones de diseño quedan explícitas; **no marcar como corrección IMPLEMENTED** hasta que se modifiquen catálogos y código y pase su prueba. Los hallazgos y los gates están en [audit/](../audit/).

## 8. Matriz de pruebas concretas

| Suite | Casos |
|---|---|
| CONTRACT | schema JSON + OpenAPI + SQL compilan y no divergen, IDs único, tech/milestone lookup, 5 hitos×12 eras, oro estratégico cero, era 13 terminal |
| SIM | 0/10/100/1000/10000 humanos, 24 NPC, 3 seeds, distribuciones equilibradas/sesgadas, horarios LIVE 0/1/4/24h, periodos UTC cambiantes, >7d outage |
| DETERMINISM | misma seed + ruleset/content hash + segmentos + entrada canónica generan mismo stateHash y winner; tick 5s vs particiones compatibles |
| VOTES | exactamente deadline, pausa, reintento, cambio de voto válido, salida LIVE, noVotes/tie, Council hold y un solo cobro |
| COMPETITION | 3 transmisiones LIVE, pérdida de una, reanudación/cancelación, ciclo RPS 2-2-2, empates y penalizaciones no acumuladas |
| MS | 3 streamers, mismo proveedor, proveedores mixtos con capacidad, otros PCs/redes, invitados expirados, permisos, token revocado, reconnect OBS |
| SECURITY | OAuth PKCE, firmas webhook, PII redaction, prompt injection en nombre, accesos cruzados y secretos, CSRF/CSP, rate limits |
| OPS | rollback, restart, restore real DB, doble worker/fencing, outbox duplicado, alerta de stream y OBS, capacidad real con 30 FPS |

Cada prueba PASS exige commit, entorno, versión de catálogo, datos/seed/entradas, resultado, timestamp y evidencia. Mientras falte, estado NOT_RUN. Suite de balance debe publicar P10/P50/P90 para duración por era y por perfil; evitar afirmar «2,5 días por era» como hecho.

## 9. Gates externos y definición del producto

No se puede escribir en GitHub una licencia de marca, permiso LIVE, desempeño de hardware, consentimiento real ni resultado de una simulación que todavía no existe. Mantener estas dependencias rastreables: proveedor/cuenta, legal/privacidad, arte/licencias, infraestructura/backup, rendimiento OBS, economía completa, costes reales y experimento con usuarios. Cada gate lleva responsable, evidencia, fecha, URL/documento y estado; ningún gate se cierra con prosa.

## 10. Condición para decir «especificación definitiva»

Una especificación documental se puede declarar **congelada para desarrollar** cuando (a) no hay normas contradictorias, (b) todos los catálogos y contratos generan/verifican referencias, (c) casos funcionales tienen entradas/salidas y (d) el owner acepta el alcance. No equivale a «juego completo» ni a soporte LIVE certificado.

**Estado de este commit:** diseño multistreamer propuesto en v2.3 y plan de ejecución definido; implementación y evidencias aún pendientes. El trabajo que sigue debe ser software, pruebas y arte real, no expansión narrativa indefinida.
