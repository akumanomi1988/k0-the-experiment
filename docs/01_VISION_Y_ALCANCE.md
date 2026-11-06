# 01 — Producto, alcance y principios no negociables (v2.0)

## Identidad y promesa al espectador
K0: The Experiment (título público de trabajo; antes Project CHAOS) es un juego-espectáculo permanente por temporadas: tres naciones inteligentes no humanas, representadas con pixel art 2D de baja resolución en proyección oblicua 2:1, evolucionan del Paleolítico a la Era Interestelar. Doctor K-0, científico cyborg, sarcástico y neutral, presenta el experimento. La audiencia participa mediante comandos de chat desde uno de los canales asociados. La nación no es la plataforma: los canales son **fuentes intercambiables**. Se admiten tres canales de Twitch, tres cuentas TikTok, YouTube, una mezcla, o modo local; todas las configuraciones dependen del acceso permitido y comprobado al proveedor.

## Decisiones heredadas, no negociables
- Tres naciones independientes: Micelios, Rúnicos y Ferrinos. No existen Corálidos. Misma base matemática, sin bonificaciones por especie/bioma.
- Cinco profesiones permanentes por temporada (`food`, `wood`, `mine`, `build`, `research`) y evolución estética por era.
- `!join` y `!work` para crear ciudadano/elegir oficio. `!active` o `!work` válido renuevan 2 horas de actividad real; el chat normal no.
- NPC mantienen el mundo vivo sin espectadores; la simulación fuera de emisión funciona a velocidad reducida.
- Recursos colectivos, comida sin muerte individual, almacenes limitados, edificios básicos automáticos, proyectos estratégicos votados entre **tres alternativas financiables** durante diez minutos; sus costes se descuentan al aprobar.
- Elecciones de gobiernos NPC: tres arquetipos, un gobernante, una hora de voto, segunda vuelta de tres minutos ante empate. Votación separada de prioridad tecnológica.
- Barra de historia por hitos únicos de puntuación fija; era lista fuera de emisión espera al LIVE. Primera nación en entrar a era final gana la temporada.
- Torneos solo programados: primer minijuego RPS triangular con elección oculta; penaltis territoriales de 30 minutos **activos en directo**; cero transferencia de oro.
- Oro solo desde aportaciones económicas verificadas; jamás por NPC, misiones, chat ni operaciones de explotación. Permanencia solo de historial, estadísticas, logros y prestigio visual entre temporadas.

## Cierre de definición de v2.0 y revisión v2.2 y revisión v2.2
Valores desconocidos de balance y reglas ambiguas pasan a convertirse en **defaults de producto v2.0**. Son decisiones técnicas/de producto tomadas en virtud de la autorización del usuario de este turno, *no respuestas históricas atribuidas al usuario*. Se pueden versionar antes de abrir una temporada; nunca alterarse a mitad de temporada sin migración explícita y auditoría.

No existe en este documento ninguna autorización implícita para extraer datos con APIs no oficiales ni para simular un beneficio monetario. Tampoco confundir especificación de sprites con haberlos creado; `art_spec.v2.json` es especificación, y las integraciones LIVE reales se mantienen bloqueadas hasta pruebas verificables.

## El juego no es pay-to-win
El oro se usa exclusivamente en proyectos opcionales de estética/prestigio, monumentos y homenajes. Todos los umbrales de historia y el motor de investigación son gratuitos. Para evitar la ventaja matemática por riqueza, un proyecto financiado con oro no aporta puntos históricos, capacidad productiva, voto extra, velocidad científica ni fuerza militar. Una maravilla entrega prestigio y reconocimiento visual, no economía. Este ajuste solventa el riesgo de que una donación sea la condición tácita de victoria.

## Criterios de éxito del diseño
Dos implementaciones que compartan `ruleset_hash`, `content_manifest_hash`, `season_seed`, la secuencia canónica de eventos y UTC segmentado deben producir el mismo estado lógico, incluido el ganador. Los viewers y la máquina OBS solo consumen proyecciones. Ningún NPC ni sprite tiene permisos de cambiar el ledger de recursos por vía gráfica.
