> **Documento de detalle.** La fuente normativa vigente es [ESPECIFICACION_MAESTRA.md](../ESPECIFICACION_MAESTRA.md). Este capítulo no prevalece ante una regla corregida en la especificación; versiones anteriores en Git.

# 49 — Audio, música, accesibilidad y localización

**Estado: especificación editorial, no bandas sonoras ni locuciones producidas.** El juego no debe depender de voz o música para que las reglas se entiendan.

## Identidad sonora

La firma de K0 combina chasquidos mecánicos breves, pitidos de terminal y percusión ligera; tono de laboratorio retro, no horror. **Tres capas separadas:** ambiente de mundo (mecánica/bioma), interacción (votos, construcción, evolución, peligro) y locución/subtítulos de Doctor K-0. Las transiciones de era evolucionan instrumentos: Paleolítico percusión seca, Neolítico flautas/superficies, Cobre-Bronce resonancias metálicas, Hierro-Antigüedad conjunto de campanas, Media-Renacimiento instrumentos de cámara, Industrial percusión de máquinas, Moderna analógico, Digital síntesis chiptune, Espacial drones orbitales, Interestelar síntesis amplia. Es una descripción compositiva ORIGINAL, no licencia de música ajena.

## Mezcla propuesta

Medidor de salida del stream objetivo -16 LUFS integrado con limitador a -1 dBTP, por verificar en la plataforma elegida. Locución prioriza inteligibilidad mediante sidechain/ducking de música de ~-9 dB durante frase, y del ambiente de -4 dB. Picos de alertas no sobrepasan los picos de voz; sonidos de error no repiten indefinidamente. El operador dispone de silenciar voz, música y efectos por buses separados, además de modo seguro silencioso.

## Catálogo de cues mínimos

| ID | Disparador | Audio | Subtítulo obligatorio |
|---|---|---|---|
| `citizen_join` | Join confirmado | Click suave 0.2s | Sí, puede ser condensado |
| `work_confirmed` | Oficio fijado | Herramienta 0.4s | Sí |
| `milestone` | Hito persistido | Fanfarria 1.5s | Sí |
| `vote_open` | Votación abierta | Campana 0.8s | Sí |
| `vote_close` | Commit resultado | Golpe 0.6s | Sí |
| `rps_result` | Ronda cerrada | Percusión 1.0s | Sí |
| `era_transition` | Nueva era persistida | Tema 4–6s | Sí |
| `live_uncertain` | Se pierde autoridad | Alerta corta una vez | Sí, persistente |
| `season_winner` | Ganador confirmado | Tema 6–9s | Sí |
| `tts_failed` | Voz no disponible | Ninguno | Sí, fallback legible |

## Accesibilidad funcional

Todos los eventos se expresan también por texto, icono y contexto; no únicamente color o sonido. Subtítulos de máximo dos líneas, salvo pantalla dedicada con scroll controlado; no tapar votos ni mapa crítico. Animación de victoria configurable como `reducedMotion`: sin destellos rápidos, flash o movimiento excesivo. Contraste verificable y daltónicos: iconos de facción y patrones distintos. La UI contempla niños y audiencias diversas; no solicita identificación personal ni expone chat ofensivo sin moderación.

## Localización

El paquete editorial de salida deberá admitir `es-ES` y `en-US`; IDs de comandos (`!join`, `!work`, etc.) permanecen invariantes inicialmente para reducir ambigüedad. Todos los textos de UI y narración se almacenan por clave, con variables tipadas como `nation`, `era`, `remainingLiveSeconds`, `points`, `displayNameModerated`. Ningún nombre visible se traduce de forma automática (nombre propio K-0, Micelios, Rúnicos, Ferrinos). Todo texto de HUD debe tener versión abreviada y versión de accesibilidad. No concatenar gramaticalmente frases dependientes del género sin plantillas correctas.

## Gate

Aprobar voz, mezcla y títulos requiere audio real bajo carga, auriculares y altavoz de móvil, derechos de autor/ejecución pública y pruebas de subtítulos con transmisiones reales. Los números de este documento son **objetivos de diseño**, no medidas de emisiones.
