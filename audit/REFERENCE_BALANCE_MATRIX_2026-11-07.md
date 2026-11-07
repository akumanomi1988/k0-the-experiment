# Evidencia de 20 escenarios del modelo de ruta gratuita — 2026-11-07

**Fuente de ejecución:** [GitHub Actions, reference-simulation](https://github.com/akumanomi1988/k0-the-experiment/actions/runs/42373034923).  
**Comprobación:** `MATRIX_PASS cases=20 allReachedEra=13 allRealMilestones=60`.  
**Herramienta:** `tools/balance_matrix.py` sobre `tools/reference_simulation.py`.  
**Estado:** `REFERENCE_PASS`, no `APPROVED_BALANCE` ni evidencia de juego implementado.

## Resultados (días calendario hasta entrada en Interestelar)

| Humanos activos sintéticos | 4h LIVE, equilibrado | 4h LIVE, sesgado | 24h LIVE, equilibrado | 24h LIVE, sesgado |
|---:|---:|---:|---:|---:|
| 0 | 31,00 | 31,00 | 10,13 | 10,13 |
| 10 | 22,00 | 26,00 | 7,52 | 8,66 |
| 100 | 8,00 | 22,00 | 6,01 | 7,79 |
| 1.000 | 6,00 | 22,00 | 6,05 | 7,29 |
| 10.000 | 6,05 | 22,00 | 6,05 | 7,29 |

Todas las variantes completaron 60 hitos (cinco por cada era jugable), 12 investigaciones troncales, 12 edificios cívicos y cero gastos de oro. En el escenario 0 espectadores, 4h LIVE/día, se contabilizaron 2.678.405 segundos calendario (aprox. 31 días); en 24h LIVE/día, 874.995 segundos (aprox. 10,13 días). Los tiempos son del modelo limitado; no constituyen promesas comerciales.

## Riesgos observados

- **Sesgo entre oficios:** un reparto sintético con 70 % de trabajadores de alimento y ningún investigador humano puede requerir **22 días** a 4h LIVE, frente a aproximadamente **6 días** con reparto equilibrado y audiencia alta. No es bloqueo estructural, pues los NPC sostienen investigación, pero es una diferencia estratégica y de experiencia de usuario que debe evaluarse con usuarios reales.
- **Cuota nacional:** el peso humano se satura en 100×100 % + 2400×25 %; el resto aporta cero a economía. Los 10.000 espectadores no multiplican indefinidamente la producción.
- **Capacidad de almacenamiento:** el modelo registra producción bloqueada por capacidad. No se infiere de esto que los costes o almacenamiento del motor real estén calibrados.
- **Relojes:** solo se confirma transición al existir LIVE; el 20 % de economía offline sigue produciendo recursos sin saltar épocas.

## Limitaciones fundamentales

La simulación usa **un solo modelo conservador de nación** con espectadores sintéticos siempre activos (renovación implícita), 24 NPC iniciales sin crecimiento, y construye únicamente cívicos y almacenes imprescindibles. Omite gobierno, prioridad, perks, XP, edificio de talleres, Consejo, maravillas, combate, generador real de parcelas, calendario editorial variable, imposición de eventos, tres naciones concurrentes y persistencia SQL. Las seeds están representadas en la identidad de resultados, pero no provocan variaciones económicas en este modelo porque el mapa puramente cosmético no se simula; **20 casos no equivalen a 20 seeds independientes**.

Por tanto, el hallazgo inicial AUD2-02 cambia de `NOT_RUN` a `REFERENCE_PASS / AUTHORITATIVE_NOT_RUN`, no a `APPROVED`. Para D2 se requiere al menos el mismo recorrido con las reglas completas o un motor de referencia semánticamente equivalente, y escenarios adversariales con 0/10/100/1000/10000 personas, recuperación y desbloqueos de proyectos en paralelo.

No borrar `audit/BALANCE_SIMULATION_REFERENCE.json`: sigue conservado como histórico insuficiente, explícitamente no autoritativo.
