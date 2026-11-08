# 43 — Ejército, guarniciones y batallas automáticas

**Estado: regla de diseño v2.2, balance no simulado.** Resuelve las decisiones históricas 25, 26, 27 y 30 sin añadir ataques libres ni micromanagement de guerra. Fuente estructurada: `data/combat_units.json`.

## Rol del ejército

El ejército es una capacidad automática de defensa territorial construida por infraestructura defensiva. No existe comando para atacar por chat ni guerras permanentes. Solo se disputa una **batalla automática programada** con las tres naciones LIVE confirmadas, separada del torneo inaugural de piedra/papel/tijera. El ganador de la temporada sigue siendo la primera nación que entra en Interestelar: la guerra nunca da puntos históricos ni oro.

## Unidades y escala

Cada una de las 13 eras tiene tres tipos de unidad equivalentes entre facciones: guardia (multiplicador 100 %), explorador (85 %) y especialista (115 %). Se generan 39 definiciones de rol/era; cada una tiene tres variantes visuales con siluetas y herramientas específicas de Micelios, Rúnicos y Ferrinos. **No son 117 estadísticas distintas:** el combate es simétrico entre especies. Fuerza base por unidad de era `e`: `10 + 2e` puntos enteros. Fuerza individual efectiva: `floor(base * rolePowerBp/10000)`.

Cada edificio defensivo completado puede sostener hasta seis unidades y genera **como máximo una cada 1.200 segundos LIVE**, alternando guardia→explorador→especialista. Límite total de nación: 120 unidades. No crecen offline. Una unidad cuesta materiales ordinarios descritos por era en el JSON, siempre después de proteger las reservas para alimento NPC y la siguiente obra cívica obligatoria. Nunca se gasta oro. Si el saldo es insuficiente, la producción militar espera; ningún NPC se ve obligado a abandonar comida/obras/hitos para reclutar. Las unidades permanecen al cambiar era; su ID y fuerza no se reescriben retroactivamente.

## Cálculo por encuentro

El operador programa el evento como máximo una vez cada 24 horas LIVE de campaña. Todos deben estar ONLINE/LIVE y disponer de edificio defensivo; si alguna nación está más de dos eras por detrás, se pospone para no convertir la sesión en paliza estructural. Tres encuentros A-B, B-C y C-A, uno por pareja. Para cada pareja se usa la suma de fuerzas de sus guarniciones: la defensa aplica el bono de gobierno militar (+500bp) y, si corresponde en el `NationLiveClock`, prioridad defensiva (+800bp), respetando el tope general de bonificaciones. Sin factores aleatorios de daño; si ambas fuerzas son iguales, empate. Victoria/empate/derrota por pareja = 2/1/0 puntos; tablas públicas muestran fuerza numérica sin revelar IDs privados de espectadores.

**Ejemplo:** dos guardias de era 1 dan `2 × floor(12 × 10000/10000)=24` puntos. Frente a una unidad especialista de era 1 (`floor(12 × 11500/10000)=13`), gana la fuerza 24 antes de aplicar bonificación defensiva. Es un ejemplo aritmético, no un resultado de balance completo.

## Consecuencias y límites

- Un ganador único puede infligir **la misma penalización máxima del sistema RPS**, únicamente a naciones que terminen por debajo: hasta 2 % de madera/piedra disponibles y sector secundario sin producción durante 30 minutos LIVE. Se aplica una vez por evento, sin sumarla dos veces cuando exista otra penalización territorial; si hay penalización activa se conserva la fecha de fin más tardía y nunca se bloquea producción básica esencial.
- Empate en primer lugar: ganadores compartidos sin sanción. No hay robo de oro, vidas, edificios, progreso tecnológico ni XP; no hay muertes permanentes de unidades.
- Ningún espectador elige golpes ni gasta oro para aumentar fuerza. La estrategia está en priorizar infraestructuras y economía de manera indirecta; el tamaño bruto del chat no determina por sí solo el resultado.
- Este tipo de evento ya está declarado en `data/events.json` (revisión v2.2), **sin afirmar que exista un motor capaz de ejecutarlo**. Antes del desarrollo hay que versionar ese catálogo y ampliar SQL/contratos conforme a esta especificación.

## Presentación y accesibilidad

60 s de introducción, 15 s de lectura de fortalezas, máximo 3 escenas de 25 s por pareja, 10 s de resultado general y tabla de penalizaciones. Los visuales son una representación teatral: agentes y proyectiles son cosméticos; el resultado se decide al cerrar el cálculo autoritativo. Subtítulos de Doctor K-0 siempre disponibles. Sin sangre, amputaciones, armas realistas ni apuestas.

## Pruebas obligatorias

`B-01` tres fuerzas iguales = todos empate y cero sanciones. `B-02` gobierno militar afecta solo defensa de combate, nunca RPS. `B-03` recurso bajo reserva: no se crea unidad. `B-04` origen offline: no se recluta. `B-05` 120 unidades: no se sobrepasa. `B-06` un directo interrumpido: evento se congela/cancela según operador, sin saldo parcialmente descontado. `B-07` mismo evento reintentado: ninguna pérdida duplicada. `B-08` falta de defensa y gap>2: torneo se pospone documentando razón.
