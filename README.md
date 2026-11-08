# K0: The Experiment — especificación de juego multistreamer

> **Estado real: DISEÑO DOCUMENTAL v2.3; SIN JUEGO IMPLEMENTADO NI APIS LIVE AUTORIZADAS.** Este repositorio contiene el baseline técnico/narrativo y catálogos de contenido, no un servicio desplegado. Los gates de pruebas y licencias siguen abiertos.

**K0: The Experiment** (Project CHAOS, nombre de trabajo histórico) es una competición narrativa entre tres civilizaciones no humanas — **Micelios, Rúnicos y Ferrinos** — a través de 12 eras jugables hasta entrar en la 13.ª, Interestelar, que cierra la temporada. El científico cyborg **Doctor K-0** presenta el espectáculo; espectadores eligen oficios, trabajan, votan y participan mediante el chat de su nación.

## Nueva decisión clave v2.3: tres streamers, tres equipos, un mundo

K0 está diseñado para **tres streamers independientes**, con cuentas propias en la misma plataforma o en plataformas distintas, cada uno con su PC, su OBS y su Browser Source. Las tres naciones conviven en **un servidor .NET central autoritativo con PostgreSQL**: los PCs solo reciben overlays y envían participación a través de APIs oficiales de proveedor, nunca calculan recursos ni ganadores. Puede funcionar además con un único operador y tres canales distintos, o tres fuentes simuladas.

- **Twitch A + Twitch B + Twitch C** (tres streamers, mismo proveedor): diseño soportado, sujeto a autorización real de cada cuenta.
- **Twitch + YouTube + proveedor C**: diseño soportado solo cuando todas las capacidades necesarias están verificadas.
- **Tres cuentas TikTok:** topología compatible, **no** equivale a disponibilidad/permiso de una API LIVE de chat/regalos.
- **Un solo chat para tres naciones**: no es un modo admitido por las reglas actuales. Un canal se asigna a una única nación.

Que se cierre OBS en uno de los equipos no detiene los demás; que falle el LIVE de una nación cambia solo su economía/ventanas y congela los eventos competitivos globales cuando se requieren las tres transmisiones.

## Empieza aquí (fuente de verdad)

1. **[CURRENT_SPEC v2.3](docs/CURRENT_SPEC.md)**: precedencia y decisiones de producto vigentes, con indicación expresa de lo no validado.
2. **[Índice completo de 67 capítulos](DOCS_INDEX_v2.3.md)**: diseño histórico más enmiendas normativas.
3. **[Arquitectura de tres streamers remotos](docs/63_ARQUITECTURA_MULTISTREAMER_v2.3.md)** y **[relojes, sincronía y contratos](docs/64_RELOJES_EVENTOS_Y_CONTRATOS_v2.3.md)**.
4. **[Diseño de portal, overlays y pixel art](docs/65_DISENO_STREAMER_OVERLAYS_Y_ARTE_v2.3.md)** y **[integraciones, seguridad y operación](docs/66_INTEGRACIONES_SEGURIDAD_Y_OPERACION_v2.3.md)**.
5. **[Blueprint de implementación y QA](docs/67_BLUEPRINT_IMPLEMENTACION_Y_PRUEBAS_v2.3.md)**; [auditoría histórica de incoherencias](audit/AUDITORIA_K0_PROJECT_CHAOS_V2_2.md) y [gates D0–D4](docs/60_DEFINITION_OF_READY_Y_GATES_DE_CIERRE_v2.2.md).

## Inventario existente

- **docs/**: 67 capítulos de visión, economía, roles, edificios, 13 eras, gobiernos, eventos, narración, pixel art, UX, redes, emisión e ingeniería; nuevos 63–67 sobre multistreamer.
- **data/**: reglas y catálogos declarativos. 130 básicos, 39 proyectos, 13 maravillas, 39 unidades, cinco oficios, 30 opciones de habilidad, tecnologías, hitos, misiones de era, misiones diarias/semanales. **Todos son diseño, no contenido ejecutado**.
- **contracts/**: JSON Schema/OpenAPI históricos ajustados y contrato de diseño multistreamer v2.3; falta generar/verificar contratos runtime contra implementación.
- **architecture/**: SQL de diseño 001/002/003. **No son migraciones de producción probadas**.
- **tools/validate_design_catalogs.py** + **.github/workflows/design-spec-check.yml**: control estático de coherencia de catálogos; pasar este control no implica balance simulado ni código funcional.
- **audit/**: riesgos, trazabilidad y dependencias externas pendientes.

## Arquitectura recomendada

.NET 10, ASP.NET Core, PostgreSQL 16+, Inbox/Outbox, sim worker lógico único por nación y arbitraje global de ganador/maravillas, React/TypeScript + Phaser en Browser Source OBS, SignalR para snapshots/deltas y adaptadores LIVE oficiales por canal autorizado. Monolito modular y despliegue único al principio: **no microservicios ni servidor instalado por streamer**. Tres overlays pueden mostrar perspectivas diferentes del mismo estado sin cambiarlo.

## Qué NO está cerrado como hecho comprobado

Sin implementación del motor o de interfaces, sin sprites finales aprobados, sin migraciones SQL ejecutadas, sin simulaciones completas de balance y concurrencia, sin tres cuentas LIVE autorizadas, sin prueba de OBS 30 FPS en tres PCs, sin respaldo/restore ensayado ni revisión legal/comercial de marca y contenido. El estado documental continúa **D1 ampliado; no D2, D3 ni D4**. Estas dependencias no se pueden resolver añadiendo adjetivos a README: requieren evidencia trazable.

**Derechos y seguridad:** repositorio público, sin licencia explícita de reutilización de terceros; no incluir tokens, emails, chat privado, nombres no consentidos, contenidos ajenos sin derechos o datos financieros. El nombre comercial K0 está pendiente de comprobación registral.
