> **Regla vigente:**** las tres cuentas pueden pertenecer a tres personas distintas y ejecutarse desde PCs/OBS diferentes. Cada broadcaster dispone de asiento, auth, Browser Source y estado de emisión propios; ningún PC aloja el motor. [Especificación vigente](ESPECIFICACION.md).

# 31 — Diseño de emisión con una, dos o tres plataformas

**Propósito:** separar por completo las naciones de las plataformas y documentar cómo configurar cuentas sin inferir permisos reales de lectura LIVE.

## Modelo conceptual

- Cada temporada contiene exactamente tres naciones, pero cualquier plataforma puede aportar 0, 1, 2 o 3 cuentas; el máximo permitido por nación se rige por la regla canónica de `ChannelBinding`.
- Un `ChannelBinding` identifica proveedor, canal, permisos observados, fecha y revisión; no es el identificador de una nación.
- La autoridad de reloj de cada nación se establece expresamente en una fuente autenticada; dos cuentas no duplican segundos LIVE.
- Los visores OBS son salidas y pueden publicarse donde la cuenta tenga permiso; un visor no concede acceso al chat ni a monetización.
- Un mismo canal no se asigna a dos naciones en una temporada, evitando ciudadanía/votos ambiguos.

## Configuraciones previstas

| Modo | M | R | F | Observación |
|---|---|---|---|---|
| Tres cuentas del mismo proveedor | Twitch A | Twitch B | Twitch C | Tres identidades de canal distintas |
| Tres cuentas TikTok | TikTok A | TikTok B | TikTok C | Solo si lectura LIVE está autorizada y verificada |
| Tres canales YouTube | YouTube A | YouTube B | YouTube C | Una señal de reloj independiente por nación |
| Mixto | Twitch A | YouTube B | TikTok C | El overlay respeta las políticas de cada proveedor |
| Local de diseño | Simulado A | Simulado B | Simulado C | Sin identidad real ni donaciones ficticias válidas |

**Recomendación de producto:** elegir la topología de cuentas antes de preparar la temporada y congelarla al comenzar. Si cambia un canal por necesidad operativa, usar transición auditada y conservar ciudadanos existentes; no regenerar población y no cambiar la nación asignada a una cuenta ya utilizada.

## Ficha de configuración que debe cumplimentar un creador

Campaña y temporada; nación; proveedor; identificador del canal; dueño/autorización; capacidad de chat; capacidad de LIVE; capacidad de eventos económicos verificables; límite de términos de uso; canal de salida OBS; autoridad de reloj; zona horaria editorial; idiomas y permisos de moderación. Campos de permisos no verificados quedan `NO_CONFIRMED` y bloquean la funcionalidad dependiente, no se rellenan con valores de demostración.

## Si solo hay una emisión disponible

La experiencia puede mostrar las tres naciones en una misma escena pública **solo como presentación**, pero eso no resuelve cómo atribuir comandos a tres naciones dentro de un chat único. La regla canónica vigente exige que cada canal pertenezca a una única nación. Por lo tanto, una campaña con una sola cuenta para tres naciones requeriría **una decisión de producto adicional** (por ejemplo, prefijos de nación y votación por contexto), que NO está aprobada ni se presume implementada. En la versión documentada se usan tres fuentes para atribución clara, aunque todas sean del mismo proveedor.

## Seguridad, términos y comercialización

El diseño es compatible con adaptadores intercambiables, no con permisos universales inventados. Algunos servicios no facilitan de forma oficial todos los eventos que CHAOS desearía. La vinculación de una cuenta exige credenciales segregadas y consentimiento adecuado; revocar una cuenta desactiva sus capacidades sin destruir el estado histórico de la nación. Nunca prometer multistream, resúmenes cruzados de chat, lectura de regalos ni publicación automática si la plataforma no lo autoriza.
