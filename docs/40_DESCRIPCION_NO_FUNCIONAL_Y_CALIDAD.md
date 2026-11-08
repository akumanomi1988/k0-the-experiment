# 40 — Requisitos no funcionales y calidad de producto

**Criterios de entrega acordados:** motor de **12 eras jugables completo** antes de plataformas reales, arte de todas esas eras y epílogo antes del piloto, overlays español vertical/horizontal, y narración LLM/TTS con fallback seguro; los tests deben demostrarlo, no solo describirlo. Aceptación pública: mercado España/UE general con controles para menores y retención operativa 30 días salvo obligaciones legales. Techo objetivo 100 €/mes, a verificar bajo carga.

**Estado:** criterios de diseño y validación futura. No se incluyen Docker, YAML de CI/CD ni scripts. Los números de rendimiento de `docs/22` son objetivos de diseño, no resultados de medición.

## Invariantes de experiencia

Una transición de era debe ser comprensible desde una escena vertical; una desconexión debe señalarse; una elección no puede completarse sin sus segundos LIVE correspondientes; las diferencias de hardware gráfico no afectan economía ni ganador; toda respuesta de comando puede presentarse sin permiso de escribir en chat externo.

## Integridad

Las identidades se basan en IDs de proveedor estables, las aportaciones en eventos verificados y el estado económico en operaciones autoritativas. No existe rollback parcial que descuente materiales y deje de crear una construcción. Un restart de OBS no tiene consecuencias económicas. Los secretos de canal no aparecen en el overlay ni en exportaciones de auditoría pública.

## Escalabilidad

Aumentar de 100 a 10.000 ciudadanos no puede exigir dibujar 10.000 sprites simultáneamente. Se agregan capacidades productivas por cohortes matemáticamente equivalentes. El renderer está desacoplado del simulador y puede reducir partículas y densidad de personajes sin disminuir producción.

## Persistencia

Snapshots, Inbox, Outbox, ledger y reglas versionadas se consideran responsabilidades conceptuales necesarias; SQL es diseño del esquema, no evidencia de migración. Las copias de seguridad deben ser restaurables en entorno de pruebas antes de monetizar. RPO y RTO definitivos deben medirse y documentarse tras desplegar infraestructura real.

## Privacidad y moderación

Minimizar identificadores y datos, usar pseudonimización en exportaciones, diferenciar público/operador, respetar bloqueo de exhibición de nombres ofensivos, atender revocaciones y conservar auditoría necesaria con política de retención específica aprobada. La elección de proveedor y jurisdicción condicionan requisitos legales; no inventar una política RGPD universal en abstracto.

## Compatibilidad

Escenas visuales de 360×640 y 640×360, render objetivo 30 FPS, escalado entero donde el formato final lo permita y modo subtitulado sin audio. Ninguna autorización de TikTok/Twitch/YouTube se presupone por el mero hecho de soportar adaptadores conceptuales.

## Gestión de calidad

Antes de aceptar una temporada pública: ensayo completo de historia, pruebas de estrés, recuperación, seguridad, inclusión de HUD, moderación, corrección de elecciones y monetización verificada si se activa. Los requisitos no funcionales se aprueban con evidencia y no con una declaración de diseño.
