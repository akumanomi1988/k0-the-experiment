# K0: The Experiment — especificación vigente y autoridad (baseline v2.3)

**Fecha:** 2026-11-08. **Estado:** especificación de diseño para implementación; NO software construido, balance validado, arte aprobado ni acceso LIVE autorizado. **Propósito:** impedir que 62 capítulos históricos se interpreten como 62 fuentes simultáneas de verdad.

## Visión cerrada y producto

K0 es una competición narrativa por temporadas entre EXACTAMENTE tres naciones: Micelios, Rúnicos y Ferrinos. Cada nación representa una facción, no una plataforma. Tres streamers independientes pueden competir desde **tres ordenadores y redes diferentes**, en tres canales del mismo proveedor o de proveedores distintos. Doctor K-0 presenta; chat y espectadores trabajan, votan y participan. El mundo existe en un **backend central autoritativo**; OBS es exclusivamente una vista remota. La topología no requiere instalación local de servidor, base de datos ni motor en los ordenadores de los streamers. **No hay sincronización P2P**.

## Índice normativo por dominio

| Dominio | Documento vigente | Catálogo / contrato |
|---|---|---|
| Prioridad, estado y decisiones | Este archivo | Registro v2.3 de este documento |
| Operación multistreamer y modelo de propiedad | [63 — Arquitectura distribuida](63_ARQUITECTURA_MULTISTREAMER_v2.3.md) | [Schema multistreamer](../contracts/multistreamer.v2.3.schema.json) |
| Reglas de simultaneidad, eventos y APIs | [64 — Semántica y contratos](64_RELOJES_EVENTOS_Y_CONTRATOS_v2.3.md) | [SQL 003 de diseño](../architecture/003_multistreamer_diseno_v2.3.sql) |
| Arte/HUD/experiencia de cada broadcaster | [65 — Diseño y UX](65_DISENO_STREAMER_OVERLAYS_Y_ARTE_v2.3.md) | Capítulos 25–30, 46–50, 61–62 |
| Proveedores, seguridad, operación y despliegue | [66 — Integraciones y operación](66_INTEGRACIONES_SEGURIDAD_Y_OPERACION_v2.3.md) | Capítulos 14,16,53,54; audit/EXTERNAL_GATES |
| Ruta de ingeniería y tests de cierre | [67 — Blueprint e implementación](67_BLUEPRINT_IMPLEMENTACION_Y_PRUEBAS_v2.3.md) | docs/57 y docs/60 |
| Catálogos de juego | Docs 01–12, 34–45 (salvo enmiendas explícitas abajo) | data/*.json v2 y v2.2 |

## Precedencia y control de cambios

1. Instrucción explícita más reciente del propietario.
2. Enmiendas v2.3 **solo en los temas enumerados aquí** y documentos 63–67.
3. Decisiones confirmadas 1–92, salvo sustituciones trazadas.
4. Enmiendas v2.2 D-01–D-10.
5. Datos estructurados validados que no contradigan una decisión superior.
6. Documentos 01–62, compendios 2.1 y anteriores.

No se autoriza reinterpretar libremente una decisión histórica. Una regla solo se considera congelada para una temporada cuando el creador guarda el manifiesto de contenido versionado, hash de reglas y seed. Los cambios materiales de diseño aquí documentados requieren implementación y validación antes de rotularse APPROVED.

## Decisiones de diseño adoptadas v2.3

- **K0-231 — Multiplayer remoto:** campaña/temporada compartida en servidor central; una cuenta de streamer autorizada por canal, cada emisor con OBS y overlay propios. Un canal jamás asignado a dos naciones en una temporada. El campo Season.broadcastMode es SINGLE_OPERATOR o MULTI_STREAMER. En MULTI_STREAMER se exigen tres cuentas K0 diferentes aceptadas, cada una como broadcaster primario de su nación antes de PREPARED; co-presentadores secundarios no tienen autoridad competitiva. SINGLE_OPERATOR permite un dueño y tres canales.
- **K0-232 — Atribución de chat:** canal y proveedor autenticados determinan nación; un chat único no controla simultáneamente tres facciones. Un jugador puede tener ciudadano separado en diferentes naciones si participa desde canales distintos, conforme a las reglas v2.2. Identificadores de proveedor no se mezclan.
- **K0-233 — Reloj y autonomía:** cada nación conserva LIVE propio; 100 % economía en su LIVE confirmado y 20 % fuera de LIVE. Esto significa **disponibilidad asimétrica conocida**, no promesa de simetría por horas emitidas. Para torneos compartidos se crea reloj global de competición que solo avanza con tres LIVE confirmados; una caída congela las tres rondas.
- **K0-234 — Autoridad:** ni navegador OBS, ni streamer ni adaptador cambian balances, recursos, hitos, votos o ganador. Solo motor .NET central con escritor único lógico y commit transaccional. Un stream caído no apaga los demás; caída del backend sí suspende entrada competitiva.
- **K0-235 — Aprobación de canales:** presencia LIVE, chat y contribuciones son permisos separados por canal. TikTok solo se habilita si la cuenta dispone de acceso autorizado verificable; nunca se presupone API LIVE pública o scraping lícito.
- **K0-236 — Orden temporal:** una única secuencia de recepción/commit, separación de CommandProcessor y tick de economía de 5 s. Economía deriva un solo delta efectivo offline; NO se aplica dos veces el factor 20 %. Fecha UTC fija no determina expiración de una ventana de LIVE pausada. Detalle en doc 64.
- **K0-237 — Consejo:** por nación y era jugable, una terna de tres proyectos gratuitos y un único Consejo resuelto. Al construir uno, la terna queda consumida; no abrir segundo Consejo de esa era sin nuevo cambio explícito de catálogo.
- **K0-238 — Eras:** 1–12 jugables; Interestelar = entrada terminal y epílogo, sin acciones competitivas posteriores. Catálogos de la era 13 se conservan como referencias de exposición, no se activan automáticamente.
- **K0-239 — Hitos y misiones:** crear misión de era colectiva propia, elegible por NPC y reiniciada al entrar en era; diarias/semanales siguen siendo contenido separado. Hasta que el catálogo de hitos y motor se modifiquen y pasen tests, NO se considera regla implementada.
- **K0-240 — ID:** NationId interno es UUID por temporada y FactionId es etiqueta estable (micelios/runicos/ferrinos); DTO públicos muestran ambos campos cuando corresponda, no confunden uno con otro.
- **K0-241 — Votos pausados:** estados incluyen PAUSED; el SQL base necesita migración versionada antes de implementación; nunca registrar votos nuevos durante UNCERTAIN.
- **K0-242 — Monetización:** Consejo y maravillas cuestan oro cero; aportaciones económicas apagadas por defecto; oro solo para reconocimiento cosmético permitido y verificado. No se crean ventajas competitivas.
- **K0-243 — Renderer distribuido:** cada overlay, uno por streamer/output, selecciona su perspectiva y formato. Sincronía visual aproximada por cue con instante UTC futuro, pero la verdad se decide solo en commit global. Degradación con snapshot y UI de recuperación.
- **K0-244 — Alcance productivo:** primero un prototipo local de 3 naciones y primera era; luego prueba distribuida real con tres streamers/equipos; después temporada completa. No crear multi-tenant SaaS, billing ni agentes instalados de escritorio en fase inicial.
- **K0-245 — Balance masivo:** los límites humanos actuales son candidatos, no balance aprobado; hasta calibración se mantiene literalmente el alcance por profesión descrito en docs 04/06. Requiere decisión de balance basada en simulación, no cambio arbitrario sin datos.
- **K0-246 — Arquetipos y arte:** mismas reglas matemáticas para especies; pixel art 2D baja resolución, suelo oblicuo 2:1, K-0 cyborg. Ninguna ilustración artística se declara aprobada sin sprite/overlay real.
- **K0-247 — Términos de disponibilidad:** en caso de desconexión de un broadcaster con proveedor aún LIVE, el juego sigue y su vista es recuperable; no se genera actividad ficticia ni se cambia su estado LIVE por estado del navegador.

## Contradicciones corregidas conceptualmente vs artefactos por actualizar

Esta versión **adopta reglas normativas**, pero NO acredita que el DDL, OpenAPI, JSON antiguos, costes y algoritmos ya las implementen. Cambios pendientes de migración y generación de contratos se listan con criterios PASS/NOT_RUN en el doc 67. El registro anterior [auditoría C-01 a C-18](../audit/AUDITORIA_K0_PROJECT_CHAOS_V2_2.md) permanece como traza; este documento no lo borra.

## Definición estricta de cerrado

- **DESIGN_DECIDED:** conducta descrita de forma normativa con prueba esperable.
- **READY_FOR_PROTOTYPE:** decisiones coherentes y slice construible; no supone servicio real.
- **IMPLEMENTED:** código, migraciones y tests en CI.
- **EXTERNALLY_APPROVED:** proveedor, licencias, calidad OBS, políticas y datos certificados con evidencia.
- **PUBLIC_READY:** temporada completa simulada con 0 audiencia/0 oro, redes distintas y tres cuentas reales probadas.

**Estado actual de v2.3:** DESIGN_DECIDED para la nueva topología y flujo, NO READY_FOR_PROTOTYPE global ni PUBLIC_READY. Es un baseline de desarrollo, no una garantía de ausencia de bugs o riesgos externos.
