# 39 — Registro de cierre documental y validaciones externas

**Estado:** registro histórico v2.1 ampliado por `docs/41` y `docs/60` de v2.2; diseño, no validación de implementación. La definición es suficientemente detallada para orientar implementación, pero no se declara producto al 100 % probado. Se conserva distinción entre decisiones cerradas, supuestos de balance y hechos externos.

## Diseñado y expresado documentalmente

Tres naciones independientes de plataforma; 92 respuestas históricas preservadas; cinco profesiones; 13 eras; condición de victoria; rutas gratuitas NPC; recursos, tasas y almacenes; gobiernos, elecciones y prioridades; Consejo estratégico; RPS triangular; contribuciones y oro limitado a prestigio; narrador neutral; estados LIVE y de economía; contratos y esquema relacional propuestos; catálogo numérico de edificios, proyectos, maravillas, tecnologías, hitos, misiones y habilidades; estilo pixel art y escenas OBS; mecanismos de operador y recuperación.

## No resuelto por escribir más páginas

**Integración:** derechos y capacidad efectiva de APIs LIVE para cada cuenta, recuperación real de mensajes, eventos monetarios auditables y condiciones del proveedor. **Arte:** elección y aprobación de sprites, retratos, animación final de K-0 y voces originales. **Implementación:** migraciones SQL ejecutadas, reproducibilidad del motor .NET, rendimiento en OBS, sincronización real y restauración probada. **Comercial:** términos de licencia, pricing y contratación de futuros creadores. **Legal:** cumplimiento y obligaciones específicas de jurisdicción.

## Hipótesis numéricas, no certezas

Las tasas, costes, puntos y límites definidos por `ruleset.v2.json` son un diseño candidato. No han pasado una batería de temporadas reales. Deben calibrarse **antes de abrir una temporada pública** con evidencia cuantitativa y datos de audiencia reales; una vez abierta, los valores permanecen congelados para evitar una carrera injusta.

## Limitaciones del sistema de tres naciones

El esquema de canales admite tres cuentas del mismo proveedor, distintas plataformas y canales secundarios por nación. **No** admite sin revisión una sola cuenta de chat que controle simultáneamente las tres naciones: no está especificado el lenguaje de asignación de nación para cada acción. Si el modelo comercial requiriese «un único LIVE compartido por las tres», eso sería una ampliación de producto con nuevas reglas y no debería inferirse desde la configuración actual.

## Criterios mínimos para fase de desarrollo

- Aprobación de los textos que reformulan decisiones previas (documento 18).
- Identidad visual final de las tres especies y del presentador, suficiente para un prototipo artístico.
- Declaración de proveedor/cuentas que se probarán primero.
- Confirmación legal y técnica de las capacidades de chat previstas.
- Revisión de hipótesis de balance con simulación real antes de prometer calendarios de temporada.

El diseño puede congelarse como baseline de desarrollo sin afirmar que esos hechos externos han ocurrido.
