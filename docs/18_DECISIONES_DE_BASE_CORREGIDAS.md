# 18 — Correcciones estructurales realizadas en v2.0

## Ajustes deliberados y por qué

| ADR | Antes | Ahora | Motivo | Impacto |
|---|---|---|---|---|
| V2-001 | Nación equivale a una plataforma | Nación independiente de canal; bindings configurables | tres cuentas en una misma plataforma | cambio de clave de datos y DTO |
| V2-002 | Oro estratégico podría mejorar carrera | solo visual/prestigio | evitar ventaja de pago sobre victoria | cambia magnitud de mejoras estratégicas; no el voto |
| V2-003 | Era final con posible elección y temporada acabada | entrada final cierra inmediatamente; sin gobierno final | eliminar estado imposible de juego cerrado y elección | excepción ceremonial documentada |
| V2-004 | Técnicas/effects `null` | reglas completas con valores v2 | permitir implementación inequívoca | balance candidato versionado |
| V2-005 | Skills colectivas multiplicables | efectos personales con techo | evitar beneficio infinito 10k ciudadanos | reinterpretación de descripciones temáticas |
| V2-006 | Proyectos con 3 candidatos quizá no accesibles | exactamente 3 proyectos estratégicos por era, si hay oro; ruta gratuita separada | votaciones no bloquean progreso | contenido cerrado |
| V2-007 | Mundo comienza sin infraestructura, podría no producir | zonas naturales gratuitas con capacidad de supervivencia | evitar deadlock de primera madera/piedra | se mantiene evolución desde cero recursos y edificios |
| V2-008 | Economía y penalización fuera de emisión ambiguas | UTC/live/economy/activePenalty separados | reanudación consistente | semántica estable |
| V2-009 | Reversos pueden causar saldo negativo | deuda separada de reversos | mantener invariante de no-negativos | ledger adicional |
| V2-010 | Candidata Ferrina `Perla` evocaba coral | pasa a `Nera`, demás nombres heredados | evitar diseño Corálido descartado | nombre artístico propuesto cerrado v2 |
| V2-011 | Falta exactitud de RPS cíclico | puntuación 2-1-0 por pares y empates compartidos | no inventar ganador en ciclo | reglamento completo |
| V2-012 | Simular todos los usuarios físicamente | trabajo por cohortes, sprites LOD | reducir CPU y minimizar ventaja de masa | representación consistente |

## Jerarquía
Las 92 decisiones originales se preservan literalmente en `data/legacy_user_decisions_1_92.json` y se relacionan en `audit/decision_traceability.json`. La **nueva instrucción expresa del usuario** modifica la asignación rígida plataformas→naciones (antiguos supuestos); no reemplaza el número de naciones, las tres facciones, las reglas sociales ni la independencia de los mundos. Ninguna otra regla original se cambia sin registrar su motivo.

## Qué sigue fuera de posibilidad de un texto
No se puede validar por escrito la licencia de API de una cuenta, tasas financieras reales, carga del hardware de emisión, arte final aprobado ni obligaciones jurídicas sin información externa específica. Eso queda en `audit/EXTERNAL_GATES.md` y NO supone un agujero en la definición de reglas del juego.
