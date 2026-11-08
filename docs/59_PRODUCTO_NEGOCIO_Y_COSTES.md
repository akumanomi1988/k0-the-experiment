# 59 — Modelo económico del producto, infraestructura y límites de monetización

## Distinción de dos economías

1. **Economía del videojuego:** comida, madera, piedra, mineral, conocimiento, trabajo, oro de prestigio. No hay relación directa entre apoyo monetario y resultado competitivo.
2. **Economía del creador/empresa:** coste de servidores, uso de APIs, TTS, arte, moderación, licencias, legal y soporte; eventual facturación mediante suscripción/licencia del software. Las tasas no se confunden ni se convierten automáticamente unas en otras.

## Cost drivers

| Coste | Unidad a presupuestar | Instrumentación necesaria |
|---|---|---|
| Instancia .NET worker | horas de cómputo + CPU pico | `tick_duration_ms`, uso medio y P99 |
| PostgreSQL | GB almacenados + IOPS + backups | write rate, retención y restauración |
| Adaptadores | cuotas/eventos/minuto y canal | API rate limits por proveedor |
| SignalR/overlays | conexiones simultáneas y bytes emitidos | snapshots/deltas por segundo |
| Doctor K-0 | caracteres TTS, tokens LLM si hay | coste por minuto emitido y tasa de caché |
| Streaming/OBS | CPU/GPU/red por salida | FPS, bitrate, horas de emisión |
| Producción artística | skins × acciones × frames | inventario de assets aprobados |
| Operación | horas de moderación/soporte | incidentes y horas de emisión |
| Derechos/legal | licencia o servicio | titulares, territorios, documentos |

## Cálculo de capacidad, no tarifa real

Con un tick cada 5 s se ejecutan `86400/5=17.280` ticks por nación por día continuo; tres naciones implican `51.840` ticks de motor por día. Esto es un contador teórico de oportunidades de tick, **no** una medición de CPU ni facturación. Si cada nación emite un snapshot lógico cada 15 s, habrá hasta `3×86400/15=17.280` snapshots/día antes de considerar compactación, caídas de conexión y deltas. Dimensionar tráfico después de medir tamaño real de mensajes y conexiones OBS, no asignar euros ficticios.

## Estrategia recomendada

**Fase 1**: único operador y campaña, economía gratuita completa, tokens y pagos desactivados, OBS controlado. **Fase 2**: tres canales reales verificados, métricas de retención y experiencia. **Fase 3**: monetización solo decorativa, y únicamente bajo aprobación del proveedor. **Fase 4**: considerar licencia de software a creadores externos; multi-tenant, billing, SLA y personalización son extensiones, no requisitos de primer directo. Se prohíbe vender «plataformas soportadas» sin probar las cuentas y sus capacidades.

## Métricas de negocio

Visitantes→`!join`, `!join`→oficio, activos tras 1/7/30 días, votos válidos por sesión, sesiones LIVE sin incidencia, duración P50 de eras, coste TTS/stream por hora, coste operativo por campaña, ingresos **netos realmente abonados** (no equivalencia de oro). Condiciones de éxito comercial y break-even requieren inversión inicial y precios de terceros actuales, que no forman parte de este diseño cerrado.
