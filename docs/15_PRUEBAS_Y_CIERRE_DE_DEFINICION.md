# 15 — Pruebas automáticas y criterios de aceptación

## Tests contractuales necesarios
V2-T01 92 decisiones preservadas; V2-T02 tres facciones exactamente y sin atributos de ventaja; V2-T03 cualquier mezcla de tres canales válida y duplicación del mismo canal rechazada; V2-T04 13 eras con cinco profesiones; V2-T05 todas las eras 1–12 tienen 5 hitos sumando 100 y camino sin gold; V2-T06 cada era tiene al menos tres proyectos estratégicos + 10 edificios básicos; V2-T07 30 skills, elegir máximo una por tier, límite de bp; V2-T08 todas las recetas con costes enteros ≥0 y sin oro en básicos; V2-T09 golpes RPS 3 elecciones distintas empatan, primera papeleta única, cero sin espectadores no inventa votos; V2-T10 ventana !active 7200s UTC, caduca offline; V2-T11 gobierno 3600s, runoff 180s, Consejo 600s, penalización 1800s live-only; V2-T12 ningún recurso negativo ni pago duplicado; V2-T13 primera entrada a última era cierra temporada sin abrir elecciones; V2-T14 auditoría de determinismo al repetir mismo flujo y seed.

## Matriz de carga y fallos antes de LIVE
- Carga de 24 NPC, +10/100/1000/10000 activos; CPU, memoria, latencia de inbox y delta, latencia OBS, límites de sprites.
- Caída a mitad de una papeleta, reconexión Twitch sin replay, YouTube cursor caducado, eventos duplicados, origen no autenticado, segundos perdidos en `UNCERTAIN`, reinicio de DB.
- Proyecto votado y tres transacciones concurrentes (oro reversado y edificio automático): debe haber una sola deducción, sin saldos negativos.
- dos naciones compiten en completar maravilla/era final simultáneamente: exactamente un ganador en DB.
- 7 días offline con hambre y capacidad saturada: no deadlock permanente y no saltar de era si no hay LIVE.
- Restauración PITR de base de datos en entorno aislado, verificación de hashes, reconciliación de ledger; se mide RPO/RTO real.
- Políticas Twitch, TikTok y YouTube revisadas en fecha de directo para canales concretos; sin este gate monetización/simulcasting OFF.

## Criterio de '100 % definido'
El canon funcional puede considerarse cerrado cuando cada entidad y comando tenga contrato, cada output numérico tenga regla y cada transición tenga test. **Eso no equivale a producto terminado**. Siguen pendientes pruebas externas (credenciales/capacidades LIVE reales, validez legal, rendimiento de Phaser en versión CEF de OBS, sprites visualmente aprobados). Se listan en `audit/EXTERNAL_GATES.md`, no como valores `null` del ruleset.
