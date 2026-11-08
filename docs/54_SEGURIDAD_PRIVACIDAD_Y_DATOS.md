# 54 — Seguridad, privacidad, abuso y retención

**Estado: política técnica propuesta, no dictamen jurídico.** El producto puede recibir IDs estables, mensajes, nombres y eventos monetarios. No almacenar texto de chat íntegro sin necesidad operativa o base legal aplicable.

## Fronteras de confianza

`ProviderAdapter` recibe datos externos hostiles: no confiar en displayName, contenido, hora remota, donación anunciada en chat o permisos autodeclarados. `Ingress` valida firma/token/canal, tamaño, antigüedad, rate limit, ID de evento y autorización antes de `Inbox`. `Engine` procesa eventos tipados y nunca ejecuta instrucciones de mensaje ni devuelve datos sensibles al overlay. `Admin` usa identidad de operador separada, MFA cuando se implante, roles mínimos y auditoría. `OBS/Phaser` solo lee deltas públicos o seudonimizados.

## Riesgos y mitigaciones verificables

| Riesgo | Medida de diseño | Gate de prueba |
|---|---|---|
| Chat malicioso/prompt injection | LLM sin permisos de transacción; variables escapadas; plantillas primero | Intentos de instruir K-0 para otorgar oro fallan |
| Falso regalo | Únicamente origen autenticado + regla de conversión aprobada | Evento falso o duplicado no acredita |
| Replay de comandos | `sourceKey` único; timestamp y canal | Mismo evento 100 reintentos, una aplicación |
| Cruce de naciones | FK compuesta `(season,nation)` y binding único | Nunca se muta otra nación |
| Operador malicioso | RBAC, doble verificación para cambios críticos, audit append-only | Operador no puede cambiar ganador/ledger |
| Filtrado de datos personales | Moderación antes de mostrar/leer voz | Nombres con URLs/PII no se emiten |
| Caída de proveedor | `UNCERTAIN`, freeze timers, modo seguro | No se contabiliza segundo LIVE ficticio |
| Robo de claves | Secret store fuera de repo, rotación, scopes mínimos | No hay tokens en logs/snapshots/overlays |
| Saturación o bots | Rate limit por cuenta/canal/tipo + IP/gateway cuando proceda | 10k emisores no colapsan orden de votos |

## Retención inicial confirmada, condicionada a revisión legal

Separar `identity` (IDs de proveedor), `ledger` (integridad económica), `publicProfile` (nombre moderado), `contentTelemetry` y `rawMessage`. Valor inicial de diseño: **no persistir mensaje bruto en sistema de negocio**; mantener digest del evento y referencia durante ventana de diagnóstico mínima. Guardar perfiles de temporada solo hasta que exista una política formal de conservación/borrado. **Objetivo: 30 días de datos operativos**; excepciones explícitas para registros fiscales/contables y otras obligaciones legales. La ejecución de purga, derechos de acceso/borrado y tratamientos de menores exige diseño y revisión formal para España/UE, público general. Anonimizar exportaciones históricas al ejercerse derechos aplicables, preservando asientos contables que legalmente deban retenerse mediante seudónimo no reversible.

## Repositorio público

GitHub contiene diseño y catálogos sin credenciales. Prohibido incorporar claves de TikTok/Google/Twitch, tokens OAuth, webhooks con secretos, mensajes reales, emails de espectadores, datos de pago o archivos de sesión. No usar secretos ficticios que puedan confundirse con los de producción. Derechos de explotación de las especies, diseños, arte y marcas no se deducen de haber hecho público el repo; decidir licencia de código/documentación cuando corresponda.

## Operación segura

Plan de incidentes con severidades: P0 estado competitivo o fondos comprometidos (pausar y no reanudar sin auditoría); P1 incapacidad de fuente LIVE; P2 caída de narración/animación; P3 cosmética. Recuperación mediante snapshot confirmado y ledger inmutable, sin reejecutar pagos por intuición. El cierre de seguridad exige pruebas de restauración, permisos efectivos y respuesta a abuso, no solo declaraciones.
