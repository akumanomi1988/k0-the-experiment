# 09 — Torneos, sanciones, eventos y misiones

## RPS triangular exacto
Se anuncia un torneo programado solo cuando las tres naciones están LIVE confirmadas; cada encuentro tiene 5 rondas de 90s LIVE de voto y descansos de 30s LIVE, más máximo 2 rondas extraordinarias para desempate de la cabeza. Cada nación toma el `rock/paper/scissors` mayoritario entre ciudadanos únicos (`!rps` primera papeleta válida irrevocable); no se muestra ninguna distribución antes del cierre, solo el número total de votantes. Empate interno: RNG uniforme reproducible entre opciones empatadas. Sin votos, opción `PASS`, nunca voto NPC inventado.

## Sistema triangular
Resolver **tres enfrentamientos por parejas** A-B, B-C y C-A. En cada enfrentamiento victoria=2 puntos, empate misma elección=1 a cada nación, derrota=0; opción PASS pierde frente a una opción válida (0–2), PASS vs PASS da 0–0. Cuando las tres naciones escogen rock-paper-scissors distintas, cada una gana una vez y pierde otra, por tanto 2 puntos, no se inventa ganador. Se suman puntos de 5 rondas, y solo si hay empate por primer puesto se disputan 2 rondas extraordinarias. Si continúa el empate, declarar victoria compartida sin castigos y sin «moneda al aire». La mayoría interna no multiplica puntos por total de espectadores, eliminando la ventaja automática de audiencia bruta.

## Derrota y territorio
Solo hay sanción material a una nación con menos puntos que **un ganador único**; derrota = pérdida del 2 % de `wood/stone` **disponibles** con redondeo hacia abajo y tope en saldo; jamás oro, conocimiento, edificios ni ciudadanos. Sanción territorial: elegir sector no esencial con máximo 10 % del output ordinario de la nación; ese sector no produce durante 1800s `NationActivePenaltyClock`, que solo avanza cuando la nación está LIVE, no offline. Si no hay sector secundario válido se muestra penalización visual y no se corta una fuente natural obligatoria para progresar. Un empate no genera penalización.

## Eventos fuera de torneos
Únicamente eventos preautorizados de `events.v2.json` activados por `ShowDirector` u operador, con anuncio previo y cooldown; nada de agresiones automáticas, fauna hostil permanente o desastres espontáneos. `catchup_challenge` se ofrece solo a naciones al menos 2 eras retrasadas, máximo 2 veces en temporada, +5 % NPC durante 30 minutos LIVE, sin puntos históricos directos ni oro. `resource_storm` es evento anunciado de reducción temporal moderada, frecuencia máxima cada 12 horas LIVE; `wildlife_parade` cosmético; `wonder_festival` abre actividad especial de maravilla si las reglas lo admiten.

## Misiones
Tres tipos diarios y dos semanales definidos en `missions.v2.json`. Periodos UTC completos: día desde 00:00 UTC; semana desde lunes 00:00 UTC. Los NPC pueden progresar y completar objetivos colectivos cuando no hay público; recompensas automáticas por nación una sola vez por instancia; al expirar la ventana se descarta misión no completada. Recompensas son materiales ordinarios no restringidos por monetización y **no añaden puntos a la barra de hitos**. Recompensas que excedan almacén se recortan con `rewardOverflowDiscarded`, auditado.
