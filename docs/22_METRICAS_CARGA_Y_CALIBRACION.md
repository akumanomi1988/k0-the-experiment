# 22 — Plan cuantitativo de balance, carga y latencia

**Balance objetivo confirmado:** temporada de **45–90 días naturales**, referencia de 5,5 días/era; publicar P10/P50/P90 y horas LIVE por nación. La producción **100 % LIVE / 20 % OFFLINE no se compensa por desigualdad de horarios**. Medir el gasto real con un techo objetivo de **100 €/mes** de infraestructura, incluida voz/LLM; los objetivos no son evidencia.

## Métricas obligatorias
`chaos_inbox_lag_seconds`, `chaos_inbound_duplicate_rate`, `chaos_tick_duration_ms`, `chaos_nation_simulated_seconds`, `chaos_rule_rejections_total{code}`, `chaos_era_duration_hours`, `chaos_era_cumulative_resource_produced`, `chaos_worker_effective_units`, `chaos_hunger_segments`, `chaos_storage_blocked_units`, `chaos_outbox_pending`, `chaos_gold_credit_unique`, `chaos_gold_debt_units`, `chaos_vote_close_lag_ms`, `chaos_obs_fps`, `chaos_tts_spend`, `chaos_backup_last_success`, `chaos_lease_epoch`. No usar IDs de usuario en etiquetas de métricas para evitar cardinalidad alta y filtraciones.

## Umbrales operativos iniciales, no evidencia medida
Tick CPU objetivo <50ms por nación a carga mediana, P95 entrada→ACK persistido <1s (aplicación económica hasta tick de 5s), P95 public delta <2s, cola outbox sin crecer durante 15min de carga, 30 FPS OBS estable durante 1 hora por salida con baseline 90 sprites horizontales /45 verticales; permitir degradación visual progresiva sin alterar economía. Estas cifras son SLO **propuestos** para implementar tests, no garantías.

## Balance de carrera
Correr tres mundos con la misma seed y perfiles (0 humanos/24 NPC, 10/24, 100/24, 1000/24, 10000/24). Medir **12 cambios de era jugable hasta entrada terminal en Interestelar** con 1h LIVE/día, 4h LIVE/día y 24h LIVE/día; simular pausas, capacidad máxima y misión diaria que vence antes del hito. Criterio de liveness: el escenario 0 humanos/24 NPC no queda bloqueado por falta de oro, madera, piedra, conocimiento ni edificios; solo puede esperar a LIVE para confirmar cambio de era. Criterio de justicia de torneo: tamaño de audiencia no cambia puntuación RPS dado mismo reparto relativo de votos.

## Optimización
Conservar `NationSimulation` de escritor único. Agrupar humanos por `(profession,bonusSet,activeTo,quotaClass)` y remanentes enteros por grupo, no iterar 100.000 sprites. Construcción y pathfinding client-side aproximados. Primero medir DB contention, CPU del escritor y coste de SignalR; separar process worker/web y añadir fencing antes de considerar colas externas.
