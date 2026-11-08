> **Documento de detalle.** La fuente normativa vigente es [ESPECIFICACION_MAESTRA.md](../ESPECIFICACION_MAESTRA.md). Este capítulo no prevalece ante una regla corregida en la especificación; versiones anteriores en Git.

# 29 — Matriz de casos límite y degradación funcional

**Propósito:** especificar qué debe ocurrir cuando el mundo no está en las condiciones ideales; el diseño debe seguir siendo coherente con ausencia de público, sin oro y con proveedores intermitentes.

| Incidente | Continúa | Se congela | Acción del operador / audiencia |
|---|---|---|---|
| Ningún espectador en las tres cuentas | NPC y economía; era lista puede prepararse | Votos humanos no se inventan | Ninguna acción exigida |
| Una nación no emite | Economía offline de esa nación | Su LiveClock, elección/Consejo y penalización activa | Reanudar al confirmar LIVE |
| Las tres naciones no emiten | Economía offline segmentada | Torneos; avance de era; votos | Esperar a DIRECTO confirmado |
| Un canal secundario desconectado | Fuentes restantes y autoridad de reloj original | Solo capacidad de ese canal | Reparar binding, sin reatribuir eventos |
| Estado LIVE `UNCERTAIN` | Economía degradada/offline | Votaciones y sanción territorial | Confirmar fuente; auditar transición |
| Ingesta de chat duplicada | Ninguna doble acción | Nada adicional | Deduplicación automática |
| Ingesta retrasada tras cerrar votación | Estado general de nación | Valor de la papeleta fuera de plazo | Rechazo auditable; mensaje neutro |
| Almacenes llenos | Consumo, investigación con capacidad, eventos admisibles | Producción que sobrepasa capacidad | Incentivar inversión de recursos ordinarios |
| Comida insuficiente | Progreso a rendimiento reducido previsto | No se elimina ciudadanía | HUD de escasez, recuperación económica |
| No existen tres proyectos estratégicos costeables | Economía, edificios básicos y eras | Convocatoria de Consejo | Mostrar aplazamiento, nunca forzar donación |
| Torneo sin papeletas | Ronda con PASS donde corresponda | Nunca inventar votos de NPC | Mostrar resultado según reglas |
| Tres opciones cíclicas RPS | Puntuación por parejas 2-1-0 | No inventar ganador de ronda | Continuar calendario |
| Empate final de torneo tras extras | Reconocimiento compartido | Penalizaciones | Mostrar empate justo |
| Cierre simultáneo de eventos globales | Secuencia serializada global | Recompensa doble | Aplicar orden de commit y auditoría |
| Reverso de contribución ya gastada | Ledger y deuda independiente | Saldos negativos | Sin compensar con recursos normales |
| Reinicio de OBS o navegador | Simulación del servidor | Solo representación | Reconectar a último snapshot |
| Fallo del servidor | Ninguna simulación nueva sin writer | Emisión se considera degradada | Restaurar snapshot + Inbox/Outbox |
| Interrupción mayor de siete días | Estado persistido | Catch-up a partir de límite | Revisión documentada del operador |
| Fin de temporada mientras hay votación | Resultado final y archivo | Nuevos votos, gastos no comprometidos | Cierre/cancelación auditable |

## Política de claridad

La interfaz no debe afirmar «todo sigue en directo» si el origen está incierto. Una cámara congelada no significa economía congelada, ni una economía offline significa ventanas de voto abiertas. Para cada incidente se emite estado comprensible y diagnóstico técnico solo en panel del operador.

## Recuperación y doble aplicación

La recuperación parte de snapshot validado y eventos no comprometidos; si se desconoce si una operación económica se confirmó, se consulta su clave de idempotencia y asiento de ledger antes de actuar. Nunca se repiten manualmente aportaciones o votos «por si acaso». Los eventos de narración pueden reproducirse como comentario histórico, pero no reactivar efectos.

## Prueba documental exigida

Cada fila se transforma en un futuro caso de aceptación con un antes, evento, después, efectos permitidos, efectos prohibidos y criterio de observabilidad. Esta tabla no implica que ya existan pruebas ejecutadas.
