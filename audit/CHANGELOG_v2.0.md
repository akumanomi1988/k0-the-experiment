# Changelog v2.0 — 2026-11-06

## Nuevos contenidos
- Abstracción Nation ↔ ChannelBinding; admite 3 cuentas de mismo proveedor y mezclas.
- Ruleset cerrado con tasas, tiempos y límites; ninguna magnitud numérica principal `null`.
- Catálogo 13 eras con 130 edificios básicos, 39 estratégicos, 13 maravillas, 39 tecnologías, 65 hitos y 30 skills.
- Contratos JSON Schema, OpenAPI, SignalR, SQL de referencia, pruebas de coherencia y manifest SHA-256.
- Política de oro solo verificado, reversible; monetización real OFF por defecto.
- Reglas de RPS, elecciones, Consejo y prioridad con desempates y pausas formales.
- Integración de misiones en hito histórico (cumplimiento único por era), preservando decisión original.

## Cambios de modelo relevantes
- `Nation.platform` **ELIMINADO**: identidad de plataforma queda en `ChannelBinding`.
- Pasaje Interestelar se convierte en evento de victoria y epílogo; no se abre elección sin temporada activa.
- Skills que afectarían al conjunto de nación multiplicadas por espectadores se convierten en perks individuales con caps.
- Oro de espectadores no concede beneficios productivos: proyectos estratégicos de estética/prestigio.
- Arranque con cero edificios y recursos, más fuentes naturales y 24 NPC para impedir deadlock.

## Estado de la evidencia
Son definiciones coherentes y tests de datos, no validaciones de API/latencia ni arte final entregado. Ver `audit/EXTERNAL_GATES.md`.
