# Auditoría independiente de consistencia y completitud — K0 v2.2

**Corte de revisión:** 2026-11-07. **Referencia:** `main` de `akumanomi1988/k0-the-experiment`, observado en el commit `fc9cc2602e9380871863b8255733f1696c3a7ada` antes de esta auditoría. **Ámbito:** documentación y catálogos, no prueba del software. Este informe no reabre las 92 decisiones históricas ni modifica el ruleset.

## 1. Verificaciones estructurales que sí se han hecho

Se han leído directamente desde GitHub las reglas, eras, edificios, proyectos, tecnologías, hitos, profesiones, habilidades y unidades de combate actuales y se han comprobado los siguientes invariantes declarativos:

| Comprobación | Resultado |
|---|---|
| Eras enumeradas | 13 |
| Edificios básicos | 130 |
| Proyectos estratégicos | 39 |
| Maravillas | 13 |
| Tecnologías | 39 |
| Hitos de catálogo | 65, incluidos los cinco de la era final de epílogo |
| Profesiones | 5 |
| Habilidades | 30 |
| Unidades de combate v2.2 | 39, sin IDs duplicados |
| `requiresTechId` de edificios → tecnología existente | Sin referencias rotas en muestra completa del catálogo |
| `eraId` de edificios, tecnologías, hitos, proyectos y maravillas | Sin referencias a eras inexistentes |
| Oro como coste de Consejo y maravillas v2.2 | Los 52 elementos consultados tienen `cost.gold = 0` |

**Límite de estas comprobaciones:** consistencia de IDs y conteos no demuestra alcanzabilidad, saldo correcto, bloqueo de concurrencia, ausencia de sesgos por audiencia, permiso de API ni calidad artística. La nueva v2.2 ya corrigió la obligación de oro para los proyectos y añadió unidades de combate; **no usar el diagnóstico anterior de v2.1 como si siguiera vigente**.

## 2. Punto funcional pendiente de decisión explícita

**AUD2-01 — Productividad humana máxima, severidad P1.** `data/ruleset.v2.json` define `activeHumanWorkersSoftCap: 2500` sin especificar su ámbito por nación o por profesión, mientras `docs/04_ECONOMIA_Y_BALANCE.md` explica los tramos de la curva como «primeros 100 activos por oficio» y «101 al 2500 por oficio». La aplicación literal por oficio permitiría cinco poblaciones separadas de hasta 2500 humanos con productividad marginal positiva, que no es necesariamente igual a un tope de 2500 para toda la nación.

**Consecuencia:** dos implementadores podrían calcular producciones distintas con los mismos espectadores y la misma distribución de oficios; las temporadas dejarían de ser reproducibles entre versiones. **Decisión recomendada:** si el objetivo económico es evitar ventaja por audiencia masiva, establecer explícitamente el ámbito `nation_total`, la regla de asignación determinista entre oficios y los criterios de redondeo. **No cambiar el JSON sin cerrar esa semántica y recalcular el balance.** Referencia: `docs/41_AUDITORIA_DE_COMPLETITUD_Y_JERARQUIA_v2.2.md`, que no fija este ámbito.

## 3. Cálculos que son aritméticos pero no validan una temporada

Derivación verificable del ruleset para el primer minuto sin bonificaciones, suficientes recursos/almacenes y sin hambre: 7 NPC de alimento × 2,4 = 16,8 comida/min LIVE; 24 NPC × 0,15 = 3,6 de mantenimiento/minuto de economía; saldo teórico +13,2. En un minuto real OFFLINE al 20 %: producción 3,36 y mantenimiento 0,72; saldo +2,64. **Este ejemplo no representa automáticamente el primer tick real**, que empieza con stock cero y necesita aplicar las reglas de hambre y orden de gastos. Ver `docs/56_MODELO_DE_BALANCE_Y_PRUEBAS_NUMERICAS_v2.2.md`.

**AUD2-02 — Duración de temporada, P0 para promesas comerciales.** El histórico `audit/BALANCE_SIMULATION_REFERENCE.json` registra `milestonesAchieved: 0` en escenarios que simulan una victoria; **no demuestra** que un juego real complete cinco hitos por cada una de las 12 eras jugables. Toda cifra de duración basada únicamente en ese JSON es **no autorizada como promesa de lanzamiento**. La v2.2 reconoce correctamente esta limitación. El cierre requiere motor autoritativo o simulador matemáticamente equivalente con replay, eventos, edificio cívico, misión y tecnologías, perfiles 0/10/100/1000/10000 ciudadanos y evidencia reproducible.

## 4. Contratos y datos: cobertura no equivale a completitud

**AUD2-03 — Integración de esquemas v2.2, P1 para implementación.** `architecture/002_extensiones_diseno_v2.2.sql` y `contracts/extensiones_lectura_v2.2.md` amplían la definición, pero siguen siendo anexos conceptuales; la `openapi.v2.yaml` principal todavía necesita consolidarse con combate, patrocinio y estados nuevos antes de convertirse en contrato implementable completo. La v2.2 lo reconoce en `docs/55_ARQUITECTURA_TECNICA_Y_LIMITES_v2.2.md` y `docs/60_DEFINITION_OF_READY_Y_GATES_DE_CIERRE_v2.2.md`.

**AUD2-04 — Versionado y enmiendas, P1 de gobernanza.** `data/content_manifest.v2.json` ya es v2.2; `data/ruleset.v2.json` mantiene `schemaVersion: 2.0.0` aunque se han introducido enmiendas de producto. Esto puede ser legítimo si `schemaVersion` identifica el **esquema** y el hash identifica el **contenido de las reglas**. Hay que escribir explícitamente ese contrato de compatibilidad antes de serializar temporadas; no renombrar por estética ni afirmar que es un defecto de hashes sin comprobación de bytes.

## 5. Diseño y estilo: definidos como brief, no aprobados como producción

La v2.2 ya tiene `docs/46`, `47`, `48`, `49`, `61`, `62`: pixel art, coordenadas de HUD, Doctor K-0, sonido, catálogo de 130 edificios, 13 maravillas y gobernantes. **Lo que falta no es otra tabla genérica**; faltan assets comprobables y decisiones visuales cerradas en ejemplos reales.

| Elemento | Documento de diseño existente | Gate no superado |
|---|---|---|
| K-0 cyborg | `docs/48`, `docs/25`, `docs/28` | Retrato y sprite de mundo aprobados en distintas emociones, silueta y pronunciación |
| Tres facciones | `docs/26`, `docs/46`, `data/factions.v2.json` | Sprites base y prueba de legibilidad en monocromo y móvil |
| Construcciones 13 eras | `docs/61`, `data/buildings.v2.json` | Muestras de edificios por familia/era con etapas, pivotes y licencias |
| 9 gobernantes, vestuario evolutivo | `docs/62`, `data/governments.v2.json` | Retratos y variantes reales con criterio de aprobación |
| HUD 9:16 y 16:9 | `docs/47`, `docs/50` | Capturas en OBS sobre interfaz nativa de plataformas; safe areas y accesibilidad |
| Sonido y voz | `docs/49`, `docs/48` | Voz sin riesgo de derechos, licencias, balance sonoro y subtítulos en emisión |
| Marca comercial | `docs/58` | Distintividad legal y dominios; K0 sigue título de trabajo |

No conviene producir toda la matriz artística sin primero aprobar un **vertical slice** que muestre K-0, una profesión de cada facción, un edificio y una votación tanto vertical como horizontal. No incluir música, tipografías ni sprites de terceros sin licencia comercial verificada.

## 6. Externos y operación (no resolubles por documentación)

- Validación de lectura de chat, presencia LIVE, cuotas, autenticidad de eventos y políticas **por cuenta concreta** de Twitch, YouTube o TikTok; tres cuentas iguales no equivalen a un solo chat para tres naciones.
- Monetización externa deshabilitada hasta verificar permisos, eventos, conversiones y reversos. Esta decisión **no bloquea** un lanzamiento sin monetización.
- Pruebas reales de PostgreSQL, inbox/outbox, idempotencia, fencing, restore, FPS/OBS, latencia, carga, privacidad y seguridad del operador.
- Validación editorial con usuarios reales: comprender `!join`, profesión, actividad dos horas, votos y resultados sin instrucciones fuera de pantalla.
- Derecho de marca, IP, privacidad, menores, retención y obligaciones fiscales del lugar de lanzamiento.

## 7. Puerta de cierre recomendada

Para avanzar desde **D1 (documentado)** a **D2 (diseño cerrado para prototipo)**, según `docs/60`: resolver AUD2-01 con versión de reglas, quitar contradicciones en los textos históricos afectados, producir y aprobar los golden samples artísticos, disponer de una simulación que demuestre hitos reales y seleccionar el primer proveedor de prueba. **D3 y D4 dependen de implementación, pruebas y permisos externos.**

**Conclusión:** la v2.2 es una especificación muy amplia, con catálogos estructurados y mejores controles de diseño que la v2.1, pero no puede declararse «absolutamente definida y calculada» sin resolver los gates anteriores. Este documento es un informe de auditoría, no certificación del producto.
