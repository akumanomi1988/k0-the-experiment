# 50 — Ciclo de usuario: comandos, tutorial, errores y fidelización

## Principio

Un espectador debe entender en 30 segundos tres cosas: qué nación ve, qué puede escribir y qué cambiará. La participación debe dar feedback aunque la cámara no muestre su sprite por límites de LOD. No exigir una web, registro adicional ni pago para entrar al juego.

## Primer contacto

1. Entra a un canal asignado a exactamente una nación. HUD explica «Únete: !join». 2. En `!join` válido se crea un ciudadano idéntico por reintentos del mismo evento. 3. Recibe «Elige una profesión» + cinco etiquetas sin revelar códigos internos innecesarios. 4. En `!work food` (u otra) se fija el oficio de temporada y empieza periodo de actividad real de 2h. 5. Ve confirmación del contador de actividad y producción colectiva, no una promesa de sprite individual siempre visible. 6. Al superar niveles 3/7/12, `!skill <id>` selecciona uno de dos skills habilitados por tramo y profesión. 7. Al volver a otro directo, `!active` reanuda actividad tras cooldown; el chat casual no renueva trabajo.

## Contrato de respuesta a cada comando

| Entrada | Aceptado cuando | Feedback positivo | Rechazo visible |
|---|---|---|---|
| `!join` | Cuenta de proveedor reconocida y canal autorizado | Ciudadano creado o ya registrado | Fuente sin permisos o evento ilegítimo |
| `!work` | Ciudadano registrado, profesión válida y no bloqueada | Oficio y actividad 2h | Profesión distinta ya elegida; código inválido |
| `!active` | Profesión fijada, cooldown terminado | Actividad hasta hora UTC | Sin oficio; cooldown |
| `!skill` | Nivel/tier permitido y sin elección previa | Habilidad seleccionada | Habilidad de otra profesión o tramo consumido |
| `!gov` | Ventana abierta, elegible | Papeleta registrada/modificada | Fuera de plazo, opción inválida |
| `!priority` | Ventana abierta, elegible | Papeleta registrada/modificada | Inhabilitado por reloj LIVE |
| `!build` | Consejo abierto, id presente entre tres opciones | Papeleta registrada/modificada | Id no disponible/edificio fuera de catálogo |
| `!rps` | Ronda abierta, primer voto | Se confirma voto secreto sin revelar opción al público | Voto previo irrevocable, ronda cerrada |

El feedback privado/en chat es **best effort**; el evento de juego puede confirmarse aun si el proveedor prohíbe respuestas públicas. La ausencia de confirmación externa no autoriza duplicar operación. La UI de administración sí registra estado real con `sourceKey`.

## Interrupción o inactividad

Cuando el usuario no está activo, su avatar puede descansar, pero la ciudadanía no desaparece ni produce con eficiencia gratuita. No se cambia profesión entre streamings. Si el canal se desconecta, `!active` no se atribuye a otra nación y la ventana LIVE no avanza. Si la fuente se reconecta tarde, los comandos con antigüedad superior a `maximumInboundMessageAgeSeconds` se rechazan o quedan en cuarentena según catálogo. No reprocesar retransmisiones de chat como input nuevo.

## Recompensa y retención sin presión

El valor es persistencia de nombre/historial y pertenencia, no una compra: panel de «tu oficio» cuando está presente, fichas de logro, ceremonia de participación, ranking de contribución **no monetaria** y resumen de temporada. Sin leaderboard que compare dinero pagado con productividad; no falsear actividad o número de espectadores. El descanso de dos horas puede recordarse sin notificaciones externas no consentidas.

## Prueba documental de UX

Tres recorridos: novato (0 conocimiento), repetidor (vuelve 3 días después), espectador que solo observa. Para cada uno simular 0, 1 y 10k ciudadanos concurrentes; el estado económico y el derecho al voto se mantiene aunque su sprite deje de renderizarse. Rechazos deben explicar acción concreta y no mostrar secretos de proveedor, SQL, hashes internos ni stack traces.
