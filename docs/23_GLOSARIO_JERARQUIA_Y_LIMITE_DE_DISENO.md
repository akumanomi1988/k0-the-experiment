# 23 — Glosario, jerarquía de decisiones y alcance documental

**Estado:** glosario normativo actualizado para el baseline v2.2. Fuentes actuales en [CURRENT](CURRENT.md) y [política de contratos](../contracts/IDENTITY_AND_VERSION_POLICY.md); las reglas v2.0/v2.1 permanecen como referencias históricas cuando estén sustituidas.

## Diccionario obligatorio

- **Campaña:** experiencia de un organizador con tres naciones, configuración editorial, canales y temporadas. No equivale a plataforma.
- **Temporada:** competición limitada entre tres naciones con instante de inicio, semilla, versión de reglas, progreso, ganador y cierre.
- **Nación:** instancia de facción (`micelios`, `runicos`, `ferrinos`) con estado económico, tecnología y gobierno propios; es una entidad estable de dominio.
- **Facción:** identidad cultural y estética; no altera las estadísticas base.
- **Cuenta/canal:** origen externo de mensajes, presencia en directo y, si está autorizado, aportaciones verificadas; se asigna con `ChannelBinding`.
- **Ciudadano:** participación jugable de una identidad en nación y temporada; diferente del avatar representado.
- **Avatar/sprite:** representación visual opcional de un ciudadano, NPC u objeto; nunca origen de operaciones económicas.
- **NPC:** población autónoma no monetizada que mantiene activa la economía y puede alcanzar los hitos gratuitos.
- **Profesión:** una de cinco familias productivas; la decisión del jugador dura una temporada.
- **Era:** etapa histórica lógica que define catálogos desbloqueables, títulos y estilo visual.
- **Hito:** objetivo único por era que aporta 20 puntos históricos una sola vez.
- **Misión:** reto diario o semanal recurrente; su finalización puede satisfacer el hito de tipo misión una vez por era, pero no concede puntos repetidamente.
- **Edificio básico:** construcción automática de la civilización, financiada con recursos ordinarios.
- **Proyecto estratégico:** obra opcional seleccionada en Consejo con votación entre tres opciones financiables.
- **Maravilla:** obra de prestigio visual opcional, globalmente exclusiva cuando así la define el catálogo.
- **Oro:** saldo interno vinculado únicamente a aportaciones autorizadas y verificadas; no tiene convertibilidad real y no mejora la carrera histórica.
- **Directo confirmado:** estado de emisión autenticado que habilita cronómetros y ceremonias; distinto de tener una ventana OBS abierta.
- **Regla canónica:** obligación de comportamiento que prevalece sobre ejemplos, prototipos o textos promocionales.
- **Gate externo:** condición verificable de plataforma, licencia, hardware, privacidad o integración que no puede darse por cumplida por redactar un documento.

## Jerarquía de fuentes

1. Última instrucción explícita del propietario del proyecto.
2. Decisiones originales registradas (92) que no hayan sido sustituidas expresamente.
3. Enmiendas aceptadas y ADR aprobadas v2.2; las propuestas en PR aún no equivalen a decisiones históricas del propietario.
4. Reglas, catálogos y contratos de `data/` y `contracts/`, salvo contradicción con una decisión superior.
5. Capítulos 01–62 como explicación vigente únicamente cuando concuerdan con el baseline activo.
6. Compendios y ejemplos antiguos v2.0/v2.1 solo para trazabilidad, no para restaurar una regla sustituida.

Si una tabla descriptiva y el JSON canónico difieren en una cifra, **no se improvisa**: se registra una discrepancia, se congela el cambio y se adopta una revisión consistente. No existe una jerarquía en la que un documento de estética autorice a conceder recursos, oro, votos o puntos.

## Qué significa «completado»

Una mecánica se considera documentada cuando identifica sujeto, disparador, entradas, condiciones, resultado, límites, errores, persistencia, pantalla y su criterio de aceptación. La documentación podrá ser exhaustiva en intención y decisiones, pero **no certifica** que una API externa funcione, que el servidor escale o que un sprite tenga calidad artística. Esos hechos pertenecen a validación futura.

## Fuera de alcance de esta fase

**Contexto histórico v2.1:** en la fase documental inicial se excluyeron backend, cliente, scripts Python, CI y ejecución de SQL. **Enmienda de alcance de la consolidación v2.2:** el propietario ha solicitado pasar a validación técnica; están autorizados validadores, tests automatizados, PostgreSQL aislado y simulaciones conservadoras de referencia, **sin desarrollar el juego completo ni afirmar D2–D4**. La documentación no se debe confundir con una aplicación funcional.
