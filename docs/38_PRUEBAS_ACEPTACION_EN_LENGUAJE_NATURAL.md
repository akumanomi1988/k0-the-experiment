> **Documento de detalle.** La fuente normativa vigente es [ESPECIFICACION_MAESTRA.md](../ESPECIFICACION_MAESTRA.md). Este capítulo no prevalece ante una regla corregida en la especificación; versiones anteriores en Git.

# 38 — Casos de aceptación funcional sin código

**Propósito:** convertir reglas en ejemplos observables para el día que se implemente el motor. No hay scripts, frameworks ni código fuente. Los escenarios usan valores establecidos en v2.0; su ejecución futura será un trabajo diferente.

## Ciudadanía y actividad

**Caso C-01:** una cuenta nueva envía `!join` dos veces debido a reintento del proveedor. Resultado esperado: un ciudadano, una identidad y ningún recurso extraordinario. **C-02:** el ciudadano elige `food`; cuando intenta `mine` en la misma temporada, el sistema conserva `food` y explica la restricción. **C-03:** una acción válida renueva actividad por dos horas reales tras cooldown; el chat casual no prolonga actividad.

## Economía y progreso

**E-01:** una nación tiene 24 NPC iniciales y ningún humano, ninguna aportación y ningún oro. La economía produce y consume según tablas; existe una ruta de avance gratuita sin desbloqueos de pago. **E-02:** cuando se llena madera, la producción no produce inventario por encima de capacidad; los restos y contadores de redondeo se conservan según regla. **E-03:** durante tiempo fuera de emisión la economía utiliza el multiplicador reducido; una votación abierta no consume minutos LIVE. **E-04:** un hito ya cobrado no concede de nuevo 20 puntos al cumplir objetivo repetido.

## Eras y gobierno

**H-01:** cinco hitos distintos de 20 puntos alcanzan 100; la nación sin LIVE confirmado queda preparada pero no pasa de era. **H-02:** al confirmar LIVE la nación avanza exactamente una vez; cambio de nombre de oficio no reasigna la profesión. **G-01:** elección de tres candidatos dura una hora de emisión; el empate activa la segunda vuelta durante tres minutos LIVE. **G-02:** un gobernador militar aplica solo el bono definido, sin capacidad de ordenar ataques automáticos.

## Consejo y oro

**V-01:** el Consejo tiene tres opciones elegibles, con recursos disponibles para cada una por separado, pero no para la suma de las tres. Se reserva el vector máximo previsto; al cierre se cobra solo el proyecto ganador. **V-02:** dos cierres concurrentes no pueden cobrar el mismo voto/obra ni dejar inventarios negativos. **O-01:** un proveedor reintenta un evento monetario idéntico: una sola acreditación. **O-02:** la aportación es revocada tras gastar oro; aparece deuda compensatoria sin saldo negativo en el wallet.

## Torneo

**T-01:** los tres equipos eligen rock, paper, scissors respectivamente; cada equipo gana y pierde una pareja, total dos puntos: no existe un ganador ficticio de esa ronda. **T-02:** una nación no recibe votos y juega PASS. **T-03:** tras dos rondas extra continúa el empate primero: se anuncian ganadores compartidos sin penalización. **T-04:** la penalización territorial consume exactamente 30 minutos de LIVE y se pausa durante desconexión.

## Integraciones y presentación

**I-01:** tres canales del mismo proveedor asignados a tres naciones no mezclan mensajes. **I-02:** retirar una capacidad de monetización no desactiva chat permitido. **I-03:** reconectar OBS no modifica inventarios. **I-04:** ocultar un avatar por LOD no desactiva la producción de su ciudadano. **I-05:** la escena vertical y la horizontal muestran idéntico ganador y era.

## Integridad y final

**F-01:** dos naciones alcanzan Interestelar en eventos casi simultáneos; la adjudicación se resuelve por secuencia de commit global, persistida. **F-02:** una vez completada la temporada no se aceptan nuevas operaciones competitivas ni se arrastran recursos. **F-03:** restaurar un snapshot y reproducir entradas ordenadas produce el mismo checksum del estado lógico con el mismo ruleset y versión de motor.

## Criterio formal

Para declarar completado cada escenario en implementación futura habrá que registrar condiciones iniciales, eventos, sello de tiempo, estado final, asientos de ledger, salida HUD y evidencia observada. **Estar escrito aquí no significa que se haya probado en software.**
