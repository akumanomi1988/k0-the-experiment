> **Documento de detalle.** La fuente normativa vigente es [ESPECIFICACION_MAESTRA.md](../ESPECIFICACION_MAESTRA.md). Este capítulo no prevalece ante una regla corregida en la especificación; versiones anteriores en Git.

# 24 — Recorridos del espectador y experiencia del ciudadano

**Objetivo:** cerrar la experiencia observable por un usuario en chat sin depender de cómo se implemente la integración. Se mantiene una identidad de ciudadanía por nación y temporada; la existencia de distintas cuentas no altera la pertenencia de la nación.

## Usuario nuevo

1. Descubre un directo asociado a una nación y ve en el HUD: nombre de la civilización, era, progreso, estado actual y ayuda de comandos.
2. Emite `!join` desde una identidad reconocida por el proveedor y el sistema crea o devuelve su ciudadano, sin duplicados por reintento.
3. Si no eligió oficio, la interfaz invita a usar `!work food`, `!work wood`, `!work mine`, `!work build` o `!work research` (adaptar los alias a los comandos registrados, sin alterar semántica).
4. La profesión elegida se mantiene hasta fin de temporada. Volver a usar el mismo oficio renueva actividad cuando cumple cooldown; cambiar a otra familia debe producir rechazo comprensible.
5. Si el usuario está activo, trabaja durante su ventana real de dos horas. El avatar puede no estar entre los sprites visibles porque existen límites de densidad: nunca se interpreta como expulsión de la economía.

**Feedback visual mínimo:** confirmación de alta, profesión válida, duración restante de actividad, nivel, habilidades disponibles y resultado de cualquier comando. Si el proveedor prohíbe respuesta por chat, el feedback se presenta en la UI del juego; no se inventa un mensaje enviable.

## Usuario recurrente

Al volver al directo, el usuario recupera identidad por identificador estable del proveedor, no por nombre visible; conserva progreso durante la temporada. `!active` renueva actividad tras validación. Si cambió su nombre público, no se crea otro ciudadano. Si cambia de dispositivo sin cambiar de cuenta, tampoco. No se promete fusionar automáticamente identidades de TikTok, Twitch y YouTube.

## Usuario con varias cuentas o canales

Un canal concreto se asigna a una sola nación por temporada. La misma cuenta del proveedor puede participar en naciones diferentes solo cuando sus canales correspondientes se asignan a ellas; las estadísticas permanecen separadas. Varias cuentas de un mismo ser humano no son identificables con certeza y no debe prometerse prevención absoluta del multicuenta.

Una cuenta de creador puede aparecer en distintas escenas OBS; ello no implica que los espectadores adquieran identidades compartidas entre canales.

## Participación política y social

Durante elecciones, el HUD ofrece tres candidaturas NPC, su categoría (economía, ejército, ciencia), el tiempo LIVE restante y la forma de votar. Un usuario tiene como máximo una papeleta efectiva que puede reemplazar según la regla canónica. Los empates pasan a segunda vuelta; el resultado y las bonificaciones se hacen públicos al cerrarse. La prioridad tecnológica se vota en una ventana independiente y breve. No se debe sugerir que el gobernador controla la economía a voluntad: únicamente concede el bono pasivo definido.

En Consejo, el usuario ve tres **proyectos elegibles y costeables**, sus costes, el carácter opcional y la cuenta atrás de diez minutos LIVE. El usuario vota; al cierre se carga únicamente el vencedor, no las tres opciones. Si la nación no tiene recursos para tres propuestas, el Consejo se pospone; no se reemplaza por una oferta imposible ni por una petición obligatoria de donaciones.

En torneo, el usuario ve `!rps`, las tres opciones y la regla de voto irrevocable. La distribución exacta de elecciones se mantiene oculta hasta el cierre para evitar arrastre estratégico. Las decisiones de la audiencia no cambian la potencia base de las especies ni el cálculo del ranking de puntos por pareja.

## Situaciones de excepción y mensajes orientados al usuario

| Caso | Respuesta de producto | Consecuencia interna |
|---|---|---|
| Comando desconocido | Mostrar ayuda sin mencionar detalles internos | Sin acción en dominio |
| Usuario no registrado intenta votar | Indicar participación mediante `!join` | No se guarda voto |
| Cambiar profesión ya elegida | Explicar que dura una temporada | Profesión original intacta |
| Voto fuera de ventana | Comunicar cierre de votación | Voto descartado y auditado |
| Cuenta/canal no asignado | No otorgar recursos ni crear ciudadanos | Entrada ignorada por enrutador |
| Fallo de señal LIVE | Avisar «emisión no confirmada» | Cronómetros congelados |
| Reintento duplicado | No duplicar ninguna recompensa ni voto | Idempotencia |
| Capacidad de almacén llena | Informar «capacidad saturada» | Excedente descartado o producción limitada según regla |
| Falta de espectadores | Mostrar economía NPC sin sustituir votos humanos | Continuidad del mundo |
| Fin de temporada | Congelar competición y mostrar museo | Recursos no se trasladan |

## Aceptación editorial

Las etiquetas de profesión, era y edificaciones deben diferenciarse de las claves internas; los errores no enseñan UUID, tokens ni SQL. Todo cambio autoritativo relevante se representa con una señal visible o texto subtitulado: alta, subida de nivel, inicio y fin de votación, edificio terminado, nueva era, penalización y victoria.
