# 27 — Especificación de escenas, pantallas y estados visibles

**Objetivo:** definir qué se debe ver en cada momento sin entregar componentes React, escenas Phaser ni archivos OBS. Las dimensiones son lógicas y se escalan con píxel más próximo.

## Matriz de escenas públicas

| Escena | Cuándo aparece | Elementos obligatorios | Información prohibida/oculta | Fin de escena |
|---|---|---|---|---|
| Visión general | Inicio de emisión, entre segmentos | Tres naciones, sus eras, historial del torneo, estados LIVE | Chat crudo de otro proveedor sin permiso | Selección editorial de nación |
| Nación vertical | Emisión principal 9:16 | Mundo, era, barra, oficios, recursos, narración subtitulada | Datos financieros personales | Cambio de segmento |
| Nación horizontal | Emisión 16:9 | Mundo, panel lateral y el mismo estado autoritativo | Reglas diferentes por layout | Cambio de segmento |
| Elección NPC | Ventana electoral LIVE | Tres candidatos, orientación, tiempo restante, información electoral permitida | Votos atribuidos erróneamente | Resultado confirmado |
| Prioridad | Tras elección, ventana de prioridad | Opciones de prioridad, tiempo y explicación de bonus | Suposiciones de bono permanente | Publicación del resultado |
| Consejo | Tres alternativas financiables | Coste por recurso, naturaleza opcional, 10 minutos LIVE | Proyectos no elegibles | Cobro atómico y obra seleccionada |
| Torneo RPS | Evento programado con tres LIVE | Equipos, ronda, tiempo, votos totales, puntuación por parejas | Opciones RPS antes del cierre | Resolución y penalizaciones |
| Ceremonia de era | La nación alcanzó 100 puntos y está LIVE | Era saliente/entrante, cambios estéticos, progreso | Transición simulada fuera de LIVE | Era confirmada |
| Final de temporada | Primera entrada en Interestelar | Ganador, secuencia final, resumen, museo | Transferencia de oro o recursos | Archivado |
| Escena segura | Fallo grave, moderación o suspensión | Marca del juego, pausa explicada, enlace/help si procede | Mundo congelado como si produjera | Reanudación supervisada |

## HUD vertical 360 × 640

Reserva conceptual del documento fuente: 14 % superior (aprox. 90 píxeles lógicos), 66 % mundo (aprox. 422) y 20 % inferior (aprox. 128). Esto es una distribución de espacio, no coordenadas definitivas de sprites. El área superior nunca debe esconder la barra histórica; el área inferior prioriza comandos, votaciones y subtítulos; los eventos emergentes se apilan y caducan para no bloquear el centro.

**Jerarquía de información estable:** identidad de nación → era y barra → evento con tiempo límite → recursos relevantes → ciudadanos activos por oficio → narración/efectos. No mostrar simultáneamente barras de progreso contradictorias o mensajes que parezcan atribuir un chat a otra nación.

## HUD horizontal 640 × 360

Aproximadamente 73 % del ancho para el mundo y 27 % para panel lateral; mantiene las mismas métricas y estados, reorganizados. No se cambian reglas por proporción. La cámara puede mostrar más ciudadanos (objetivo 90 frente a 45), pero ambos visores consumen el mismo snapshot.

## Estados universales que todo componente debe representar

`LOADING`, `LIVE_CONFIRMED`, `OFFLINE_CONFIRMED`, `UNCERTAIN`, `PAUSED`, `DISCONNECTED`, `RECOVERING`, `DEGRADED`, `COMPLETED`. El operador tiene diagnóstico adicional; un espectador recibe mensajes comprensibles. Cada componente con un reloj distingue explícitamente **tiempo de directo** y **tiempo real**: nunca etiquetar «10 minutos» como tiempo UTC si una votación está pausada.

## Secuencias de interacción

**Al crear ciudadano:** pulso de llegada → confirmación de oficio pendiente → estado de actividad. **Al terminar edificio:** mejora visible de obra en etapas ya especificadas → evento de completado → icono de capacidad añadida. **Al entrar en era:** transición histórica sin borrado de recursos → cambio de paleta/estructuras → retomada de estado. **Al terminar temporada:** detener decisiones competitivas → animación final → museo → estado de campaña preparada para siguiente temporada.

## Reglas de accesibilidad visual

El color nunca es el único indicador; cada progreso tiene texto y forma. Las pistas sonoras tienen subtítulos equivalentes. Los controles de operador disponen de foco, labels y confirmaciones. Para personas sensibles al movimiento, priorizar reducción de destellos y cámara estable durante anuncios importantes.
