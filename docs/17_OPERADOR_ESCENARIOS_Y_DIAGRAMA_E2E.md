# 17 — Runbook del operador y flujos E2E

## Preparación
Crear temporada DRAFT y asignar 3 facciones. Elegir tres canales distintos, o simulados, y comprobar health por rol. Crear mapas a partir del mismo `seasonSeed` pero visualmente distintos por bioma. Revisar documentalmente que reglas y catálogos concuerden, y dejar constancia de los cambios antes de abrir una temporada. Registrar `rulesetHash`, `contentHash`, versión de motor y modo monetario. Iniciar solo tras ver 3 naciones PREPARED y snapshots iniciales.

## Secuencia A — ciudadano
Llega evento chat verificado `!join` → persistir inbox unique → resolver canal a nación → crear `Citizen` si no existe → emitir `CitizenJoined` → respuesta visual K-0. `!work food` → fijar profesión si nula → `activeUntilUtc=now+7200` → participa en la economía en siguiente segmento → XP desde trabajo efectivo, nunca por el chat. Duplicar mismo evento: `EVENT_DUPLICATE` sin segundo ciudadano/XP. Repetir `!work mine` después de seleccionar food: rechazo sin renovar actividad.

## Secuencia B — transición de era
5 hitos se completan, otorgando 20 puntos cada uno. Si offline, `EraReadyPending`; en próxima señal LIVE confirmada, tomar lock nación y temporada, comprobar que no está COMPLETED, hacer `EraAdvanced` transaccional, extender mapa, recalcular etiquetas de profesión y abrir elecciones por 3600s LIVE. Después prioridad 300s, sin solapar con Consejo. Si `EraAdvanced` entra en interstellar, emitir `SeasonCompleted` y **no** abrir elección nueva.

## Secuencia C — gasto estratégico
Tres opciones financiables → tomar hold vectorial → abrir Consejo durante 600s LIVE → registrar/reemplazar votos → cerrar con recuento → validar hold vectorial de recursos ordinarios sin depender de oro ni reversos → gastar una sola vez ganador con ledger → crear `ConstructionQueued` → liberar hold restante → emitir Outbox al OBS. Si se cae la señal, se congela ventana; si la reserva ordinaria no es consistente, impedir el commit y auditar el error; nunca bloquear el Consejo por reversos de oro.

## Secuencia D — fallo de proveedor
`HEALTHY → UNCERTAIN` ante ausencia de heartbeat/credenciales; detener ingreso de votos de fuente sin autoridad, pausar LiveClock y penalizaciones; offline economy 20 % y conservar último snapshot. Reautorizar y volver LIVE con evento auditado sin inventar comandos perdidos. Reintentos de webhook deduplicados. Si todas las fuentes no están confirmadas, torneo global se aplaza.

## Secuencia E — operador
Botón `EmergencyStop` inhibe nuevos eventos y congela escrituras de juego de forma ordenada; permitir persistencia/outbox ya confirmada. `Resume` exige health y DB reconciliada. `AbortSeason` no borra movimientos; cambia estado con motivo y resultado vacío. `PublishScene` solo modifica presentación, nunca saldos.
