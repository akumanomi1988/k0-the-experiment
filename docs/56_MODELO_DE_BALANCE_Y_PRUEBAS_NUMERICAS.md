# 56 — Modelo económico, cálculos y metodología de balance

**Coherencia de cuotas:** un solo cupo de **2.500 humanos efectivos por nación**, las cinco profesiones comparten los primeros 100 al 100 % y los siguientes 2.400 al 25 %. Rotación nacional cada 600 s LIVE. Medir escenarios de distribución de oficios y horarios asimétricos, sin compensación de horas; los números son objetivo a validar, no simulaciones ya ejecutadas.

**Estado: CANDIDATE_BALANCE, NO VALIDADO.** Esta hoja de cálculo mental y reglas reproducibles no sustituyen un motor de simulación. Las cifras canónicas están en `data/ruleset.json` y catálogos v2.2.

## Parámetros fijados

Tick 5s; recurso en milésimas; basis points 10.000=100%; NPC 24 de inicio distribuidos 7 comida/5 madera/4 mina/4 obra/4 ciencia; offline al 20%; ventana humana activa 7.200s. Output base por trabajador/min: food 2,4; wood 1,8; stone 1,4; ore 0,65; knowledge 1,2; buildWork 1,2. Mantenimiento alimentario 0,15 por NPC y minuto de economía, más humanos efectivos hasta tope. Capacidad inicial por recurso común 3500 unidades, conocimiento 15000. Cinco hitos por era a 20 puntos cada uno.

## Cálculos de control aritmético (teóricos, sin bonos ni capacidades)

- **Producción alimentaria inicial 60s LIVE:** `7 × 2,4 = 16,8` comida. **Consumo NPC:** `24 × 0,15 = 3,6`; balance bruto +13,2 comida/min, si hay capacidad y no hay eventos. No implica duración de temporada.
- **Madera inicial 60s LIVE:** `5 × 1,8 = 9` unidades. **Piedra antes de era 3:** `4 × 1,4 = 5,6`. **Investigación:** `4 × 1,2 = 4,8`. **Construcción:** `4 × 1,2 = 4,8` unidades de obra.
- **Offline base 60s reales con multiplicador 20 %:** producción alimentaria nominal `16,8 × 0,2 = 3,36`; mantenimiento NPC nominal `3,6 × 0,2 = 0,72`, antes de aplicar capacidad/hambre/factores.
- **Duración mínima de 1ª investigación troncal con 4 NPC científicos y 0 ventajas:** 290 / 4,8 = 60,4167 minutos LIVE equivalentes de ciencia, si conocimiento no se consume en otra cosa y las reglas de prioridad lo permiten. No incluye ticks, edificación ni requisito histórico.
- **Coste estratégico Paleolítico v2.2:** 120 madera + 85 piedra + 20 conocimiento + **0 oro** por proyecto. El holding entre tres opciones de coste idéntico es ese vector una sola vez, no triple.

Los cálculos anteriores son algebraicos, no evidencia de que un NPC en una temporada real llegue de Paleolítico a Interestelar con todos los bloqueos resueltos. La antigua simulación simplificada registra `milestonesAchieved:0` a la vez que llega a era 13; por eso **no sirve para certificar los hitos** y queda archivada como referencia insuficiente.

## Modelo obligatorio de evaluación de una temporada futura

Para cada perfil de participación de (0, 10, 100, 1000, 10000 ciudadanos), cruzar distribución de oficios equilibrada y sesgada × sesiones 0/1/4/24h LIVE día × disponibilidad de cada nación (simultánea, asimétrica, una desconectada) × 0 aportaciones económicas × 3 seeds de mapa × eventos de crisis/penalización. Para aceptación de balance, ninguna nación con 24 NPC debe quedar bloqueada en las eras 1–12 por falta estructural de recursos o dependencias, y ninguna aportación debe acelerar victoria.

## Métricas por escenario

`elapsedWallDays`, `nationLiveSeconds`, `economyEffectiveMinutes`, `eraEntryCommittedAt`, `milestonePoints`, `missionPeriodsCompleted`, `foodShortageSeconds`, `capacityBlocked`, `outstandingReservations`, `goldVerified`, `npcPopulation`, `humanEffectiveWorkers`, `buildingBacklog`, `techBacklog`, `wonderEligibility`, `combatPenaltySeconds` y `per-tick stateHash`.

## Criterios de calibración (propuestos)

**Objetivo de producto confirmado:** temporada completa de **45–90 días naturales**, mediana orientativa 66 días (≈5,5 días por cada una de las 12 eras jugables). No forzar evolución artificialmente para cuadrar el calendario. No adoptar tolerancia hasta ver distribución: documentar P10/P50/P90 por perfil y exposición LIVE. Si P90 queda bloqueado, priorizar corregir dependencias o reserva antes de subir por sistema las tasas. Balancear tres facciones con mismas condiciones y RNG de juego equivalente; no dar ventaja silenciosa al canal con más público. Congelar cambios al comenzar temporada; revisar únicamente entre temporadas.

## Invariantes que deben poder demostrarse

Comida/recursos nunca negativos; ledger suma saldos; evento monetario duplicado no multiplica oro; no existe progreso pagado; todas las etapas de era 1–12 pueden completarse gratis; todas las obras obligatorias tienen ruta material desde zonas naturales; cambios de tick y FPS no alteran resultados; misma entrada ordenada+seed+versión reproduce exactamente estado persistido.
