> **Enmienda normativa v2.3 (multistreamer distribuido):** cada output remoto puede usar NATION_FOCUS, SHARED_WORLD o EVENT_STAGE (solo si policy lo permite). Tres clientes renderizan el mismo estado, con clocks y secuencias de servidor; sus FPS no cambian el motor. [Especificación vigente](CURRENT_SPEC.md).

# 47 — Wireframes textuales, HUD y comportamiento de pantalla

**Estado: design token de layout, pendiente de test visual.** Las medidas son píxeles lógicos; la UI debe soportar 360×640 vertical y 640×360 horizontal, escalables enteros a 1080×1920 y 1920×1080.

## Vertical 360 × 640

| Área | Rectángulo aproximado `x,y,w,h` | Función | Prioridad |
|---|---|---|---|
| Franja superior | `0,0,360,90` | Emisión, nación, era, puntos de historia, estado LIVE | Máxima |
| Ventana de mundo | `0,90,360,422` | Ciudad, caminos, unidades, K-0 en escena | Central |
| Panel inferior | `0,512,360,128` | Recursos condensados, evento activo, comandos de participación | Máxima |
| Cartela K-0 | `16,410,328,86` | Subtítulo flotante **solo si** no oculta voto/resultado | Contextual |

Se reserva mínimo 8px de padding lógico externo y 4px de separación interior. Nunca se dibuja contenido crítico a menos de 24px de los extremos de salida final adaptados a controles del proveedor (safe areas deben medirse por plataforma). El mundo puede reducirse más ante overlays nativos de chat; la interfaz presenta modo compacto si no cabe.

## Horizontal 640 × 360

| Área | Rectángulo `x,y,w,h` | Función |
|---|---|---|
| Mundo | `0,0,467,360` | Escenario 2:1, cámara principal, Doctor K-0 |
| Panel lateral | `467,0,173,360` | Era, hitos, recursos y eventos |
| Subtítulo K-0 | `20,284,425,52` | Texto de dos líneas, sin tapar panel |

Estos rectángulos concretan el objetivo anterior de aprox. 73 % mundo y 27 % panel. En eventos críticos (voto, torneo, evolución) se permite un modal de escena que sustituya HUD secundario, jamás el indicador de nación, el temporizador ni el estado LIVE.

## Tipografía y contenido

Encabezados 12–14px lógicos, recursos 10–12px, subtítulo 12px mínimo en superficie equivalente; los tamaños son **punto de partida de prototipo**, sujetos a pruebas de legibilidad real en móvil. Fuente de píxel abierta/licenciada comercialmente, con conjunto de glifos español/inglés, acentos y números tabulares. No se licencia aquí ninguna fuente concreta. Nunca animar contador tan rápido que deje de leerse; recursos pueden abreviarse 1.2k pero sus valores exactos quedan en detalle.

## Ocho escenas obligatorias

1. `BOOT_CHECK`: marca, estado de canales, sin simular ganador. 2. `WORLD`: ciudad y actividad, estado nación y era. 3. `GOV_VOTE`: tres gobernantes NPC, barras de votos mostrables y segundos LIVE restantes. 4. `PRIORITY_VOTE`: ramas economía/ciencia/defensa, bonus expresado como % real. 5. `COUNCIL_VOTE`: tres proyectos diferenciados, coste ordinario, votos por opción y temporizador. 6. `TOURNAMENT`: RPS con recuento de participantes pero **sin distribución de elecciones** hasta cierre, luego marcador. 7. `ERA_TRANSITION`: ceremonia y nuevo inventario visual, nunca adelanta era sin commit. 8. `SEASON_END`: ganador y archivos históricos; se cierran inputs competitivos.

## Estados transversales

`LIVE`, `OFFLINE`, `UNCERTAIN`, `WAITING_FOR_PLAYERS`, `VOTE_PAUSED`, `OPERATOR_PAUSED`, `READ_ONLY_RECOVERY`, `SAFE_SCENE`. Para cada estado deben existir banner, texto explicativo, accesibilidad subtitulada y colores/íconos distinguibles sin depender del color. Un voto abierto muestra: nombre, regla, opciones, tiempo LIVE, mensaje de confirmación/rechazo, número total de votantes. No mostrar donaciones como requisito para participar.

## Experiencia sin chat

Toda salida debe poder leerse sin sonido y sin escribir: al menos nombre y estado de nación, era, progreso, evento y próximo punto de acción. La escena no debe diseñarse para que el espectador necesite un panel web externo. El público que mira desde otra plataforma recibe información pública permitida, nunca identidad cruzada no consentida.

## Criterios visuales de aprobación

Capturas obligatorias por escena y formato en condiciones: primera era, era digital, 0/45/90 avatares, vote tie, fin de temporada, modo seguro, subtítulo máximo, texto inglés más largo y safe-area nativa. Medir truncados, solapamientos, contraste y lectura desde móvil a tamaño real; un wireframe textual no equivale a dichas capturas.
