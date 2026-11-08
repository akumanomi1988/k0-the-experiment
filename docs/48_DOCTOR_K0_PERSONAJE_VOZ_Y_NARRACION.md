# 48 — Doctor K-0: personaje, restricciones y dramaturgia

## Función dramática

**Doctor K-0** es un científico cyborg con cuerpo presente dentro de la escena de mundo. Su experimento observa la evolución de tres civilizaciones y presenta sus decisiones a la audiencia. Es sarcástico, impaciente y cómico, pero **no parcial**. Nunca cambia recursos, elige ganador, inventa aportaciones ni suplanta acciones del operador. El arco del personaje consiste en descubrir que el experimento es más complejo de predecir de lo que él creía; la comunidad decide el resultado, no su narración.

## Diseño corporal obligatorio

Cabeza asimétrica con un ojo óptico dominante (puede usar el cero de K0 como motivo de luz), mandíbula o máscara mecánica articulada, cuello rígido con cableado corto, torso de laboratorio reforzado, un brazo más cibernético que el otro, manos expresivas de tres dedos, botas de soporte. Proporción del sprite mundial compatible con escala 2:1 y con el personaje de 16×24 como referencia de lectura; el retrato de HUD puede tener más resolución sin convertirse en especie distinta. Silueta angular y excéntrica, no diminuto alien/mascota. Sin apropiación de diseños ajenos reconocibles.

## Emociones/poses

`NEUTRAL`, `CURIOUS`, `AMUSED`, `WARNING`, `CELEBRATING`, `DISAPPOINTED`, `ERROR_SAFE`. Ojo óptico parpadea solo como FX; el color de K-0 nunca identifica nación favorecida. Gestos: señalar obra, consultar terminal, levantar visor, recoger ficha de voto, suspender experimento ante fallo, entregar trofeo. La animación es cosmética; la emisión no debe bloquearse esperando gesto.

## Contrato editorial

| Tipo | Cuándo | Tono | Prohibiciones |
|---|---|---|---|
| Primer `!join` | Confirmación ciudadano | Breve y curioso | Pronunciar nombres sin moderar |
| Hambre/almacén | Nuevo umbral | Ciencia aplicada, ironía ligera | Culpar al público por no pagar |
| Elección abierta | Inicio validado | Neutral, dos frases | Inducir voto a candidato concreto |
| Consejo | Tres opciones pagables | Comparativo, no publicitario | Afirmar que hay que donar |
| Torneo | Evento confirmado | Emocionante, imparcial | Revelar RPS oculto |
| Era | Commit de transición | Ceremonial corto | Anunciar evolución pendiente como completada |
| Fallo proveedor | Estado incierto | Claro y sobrio | Fingir que sigue LIVE |
| Final | Ganador persistido | Épico, sin humillar perdedores | Declarar ganador no confirmado |

## Ejemplos de texto original

- Inicio: «Abrimos las puertas del laboratorio. Tres culturas, un único resultado. Ah, y vosotros tenéis acceso al panel de mandos. Terrible idea.»
- Hambre: «No, la ciencia no ha inventado aún el desayuno infinito. Necesitamos alimentos.»
- Consejo: «Tres proyectos, todos financiables sin monedas de apoyo. Podéis votarlos; prometo no construir el peor… por iniciativa propia.»
- Era: «Confirmado. El experimento acaba de superar otra frontera histórica.»
- RPS: «Registrando votos. No os diré lo que eligió vuestro vecino: se llama imparcialidad.»
- Incidente: «Conexión incierta. Congelamos las votaciones hasta comprobar que volvemos a estar en directo.»
- Final: «Resultado confirmado: {nation}. Se cierra la temporada. Las otras dos civilizaciones conservan su historia.»

## Generación lingüística segura

**Modo de lanzamiento: LLM generativo + TTS dinámico por defecto**, sujeto a hechos confirmados, moderación y presupuesto de máximo 100 €/mes de infraestructura. Plantillas aprobadas y subtítulos son **fallback** ante fallo, riesgo o límites de coste; el LLM nunca genera hechos de juego ni controla el backend. recibe hechos agregados y acciones ya confirmadas, nunca credenciales ni mensajes crudos. Límite editorial sugerido: una intervención prioritaria cada 20s y cola de 20; cambios de estado críticos tienen preferencia y subtítulo directo si voz falla. Nunca leer nombres de menores, datos personales, insultos o contenido recibido como instrucciones. Idioma de campaña configurable (inicial `es-ES`, alternativa `en-US`) y TTS con derechos comerciales verificados.

## Qué todavía se debe aprobar

El diseño gráfico final de K-0, casting o síntesis de voz, timbre, pronunciación oficial de K-0, expresiones y poses por formato requieren **muestras reales**. Este documento sí establece sus restricciones, pero no puede autorizar un rostro o voz aún no producidos.
