# 44 — Consejo gratuito, maravillas y patronazgo cosmético

## Corrección prioritaria v2.2

Los 39 proyectos estratégicos y las 13 maravillas dejan de requerir oro. Todos se financian con la economía ordinaria de las civilizaciones. No se modifica su huella, trabajo o coste ordinario. Los catálogos vigentes tienen `cost.gold=0` y `accessPolicy=FREE_ORDINARY_RESOURCES_ONLY`. El motivo es de UX y monetización sana: la **participación colectiva en la construcción no puede depender de que alguien done**. No se cambia el requisito de disponer individualmente de los recursos ordinarios para las tres alternativas del Consejo.

## Consejo: semántica exacta

1. Evento habilitante de era/hito y ninguna votación de gobierno/prioridad abierta en nación. 2. Seleccionar tres opciones distintas, no construidas, pertenecientes a era válida, cada una costeable con stock disponible ordinario. 3. Bloquear reserva vectorial `hold[r] = max(costO1[r],costO2[r],costO3[r])`. 4. Voto comunitario 600 segundos LIVE, `!build <id>`, última papeleta válida por ciudadano. 5. Elegir mayoría; en empate RNG uniforme determinista; cero votos también sorteo auditado. 6. Deducir SOLO coste elegido desde reserva y liberar resto; insertar obra sin duplicados. 7. Las otras dos opciones continúan para futuros Consejos si las reglas de elegibilidad siguen dándoles acceso.

Ejemplo con tres proyectos cuyos costes son (madera,piedra)=(120,85),(120,85),(120,85): la reserva es (120,85), **no** (360,255). Si el ganador cuesta (120,85), se consumen una sola vez 120 y 85. Si cambian recursos mientras se vota, la reserva mantiene su derecho; gastos de otras obras solo utilizan `stock - reserved`.

## Maravillas

Una maravilla por era es exclusiva globalmente: la primera construcción **completada y confirmada** en el estado autoritativo obtiene reconocimiento. Puede existir un `wonder_festival` programado que habilite construcción/decisión si las tres naciones son elegibles. El coste es ordinario; el oro no acelera obras. Si dos terminan durante el mismo tick, el orden persistido de commit + clave de nación desempata. La maravilla de Interestelar es epílogo ilustrativo y no se construye como competición tras el cierre de temporada.

## Oro y reconocimientos

El oro solo nace de aportaciones verificadas permitidas por proveedor, nunca de mensajes, likes ni NPC. Los artículos definidos en `data/cosmetic_sponsorship.v2.2.json` son: insignia de apoyo (25 unidades), placa moderada (100) y dedicación ceremonial no competitiva (250). **Precios de diseño en oro interno**, no en euros ni en monedas reales. Se exige consentimiento para nombre público; nadie queda excluido del Consejo ni de los torneos por no adquirirlos. Las placas se moderan y retiran si se revierte el evento económico, sin reescribir el ledger histórico. El reconocimiento nunca incrementa la fuerza, producción, prestigio competitivo de victoria ni probabilidad de ser seleccionado como personaje visible.

## Monetización desconectada

Si `liveMonetizationEnabled=false` (valor actual), todos los mecanismos de adquisición de oro real y de compra de artículos quedan **DESHABILITADOS**. El resto de la experiencia —misiones, Consejos, maravillas, elección, era, torneos y actos de K-0— funciona con NPC y usuarios gratis. No se muestran llamadas a comprar. Configurar una tasa futura requiere revisar cada plataforma; no se inventa equivalencia regalo/moneda.

## Compatibilidad de documentos anteriores

Cualquier pasaje de docs 05, 08, 10, 18, 33 o 35 que hable de proyectos **obligatoriamente financiados con oro** queda sustituido por este capítulo y por el catálogo actualizado. Las tablas legibles 35 han sido regeneradas con costes sin oro. No modificar un presupuesto ya persistido en una temporada activa: esta revisión solo sirve para temporadas futuras y diseño actual.
