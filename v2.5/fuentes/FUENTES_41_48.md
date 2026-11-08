# Fuentes íntegras v2.5 — capítulos 41–48

> **Archivo de preservación de contenido completo (encabezados reindentados).** No es una segunda autoridad: la [especificación maestra](../ESPECIFICACION_MAESTRA_v2.5.md) resuelve reglas sustituidas. Los enlaces relativos del texto interno pertenecen al documento original citado; para navegar, abra ese archivo de origen.

---

## Fuente 41 — `docs/41_AUDITORIA_DE_COMPLETITUD_Y_JERARQUIA_v2.2.md`

**Blob original:** `20f18b88d46f6512568a724acb87a4485d988a87`.

> **Nota de vigencia:** auditoría histórica de revisión v2.2. Las enmiendas posteriores y el diseño multistreamer están registrados en [CURRENT_SPEC v2.3](CURRENT_SPEC.md), [arquitectura distribuida](63_ARQUITECTURA_MULTISTREAMER_v2.3.md) y [blueprint QA](67_BLUEPRINT_IMPLEMENTACION_Y_PRUEBAS_v2.3.md). No asumir que los gates se han validado.

## 41 — Auditoría de completitud, decisiones y jerarquía v2.2

**Estado: REVISIÓN DOCUMENTAL, NO VERIFICACIÓN DE PRODUCTO.** Este archivo es el índice de riesgo vigente. No debe publicarse la expresión «100 % terminado», «balance certificado» o «arte final» sin evidencia. K0: The Experiment es el nombre público de trabajo; Project CHAOS permanece en identificadores heredados.

### Qué está definido y qué no

| Eje | Especificado | Evidencia que todavía falta | Criterio de cierre |
|---|---|---|---|
| Visión y usuarios | Tres facciones, temporadas, chat, NPC, directo, Doctor K-0 | Prueba con espectadores nuevos | Cinco sesiones moderadas sin intervención explicativa |
| Reglas principales | 13 eras, 5 oficios, 5 hitos, cronómetros LIVE, votos, RPS | Consistencia entre reglas y eventos reales | Modelo de referencia reproducible + aceptación de escenarios |
| Economía | Valores exactos propuestos en ruleset y catálogos | Balance de todas las eras con 0/10/100/1000/10k humanos | 100 simulaciones por perfil, sin bloqueo y distribución publicada |
| Obras y Consejo | 130 básicos, 39 proyectos, 13 maravillas | Comportamiento ante saturación de espacios/colas | Completar rutas con 0 aportaciones; no hay Consejo invocable sin 3 opciones pagables |
| Ejército | Catálogo nuevo de 39 unidades por era/rol, evento automático propuesto en v2.2 | Comprobación de fórmulas y dramaturgia | 3 pares, empates y penalizaciones deterministas |
| Interfaz | Escenas, HUD, proporciones y layout base | Aprobación de wireframes y accesibilidad con contenido real | Capturas vertical/horizontal revisadas a resolución destino |
| Arte | Pixel art 2:1, reglas de silueta, paletas de facción | Sprites, tiles, efectos y diseño final de K-0 | Style frames de 3 facciones, 3 eras muestra y assets testados |
| Audio | Contratos de cue y guion, pauta v2.2 | Voz/licencias y mezcla real | Escucha en móvil, subtítulos y fallback sin TTS |
| Integraciones | Bindings y contratos | Permisos, cuotas, autenticación y políticas de proveedores | Matriz de proveedor verificada por cuenta |
| Backend | Responsabilidades, transacciones, SQL propuesto | Migraciones y carga real | SQL ejecutable, tests de integridad y recuperación |
| Seguridad/legal | Principios y amenazas | Dictamen contextual y verificación de jurisdicción | Evidencia aprobada; nunca inferir permiso de una API |
| Negocio | Hipótesis de juego y futuro SaaS | Costes reales, adquisición, marca, políticas | Plan financiero y viabilidad ajustados a datos |

### Hallazgos auditados y resolución documental

- **D-01 — Alta:** todos los proyectos de Consejo y maravillas exigían oro, a pesar de que los eventos monetarios reales están apagados. Corrección de diseño v2.2: los costes de oro de esos elementos pasan a **cero**. Se mantiene el coste de recursos ordinarios y el prestigio; la participación gratuita deja de depender de donaciones. Las compras de oro se reservan para reconocimientos cosméticos separados. Ver `data/strategic_projects.v2.json`, `data/cosmetic_sponsorship.v2.2.json`, capítulo 44.
- **D-02 — Alta:** tecnologías afirmaban desbloquear talleres y centros de investigación mientras el catálogo de edificios tenía `requiresTechId=null`. Corrección v2.2: las dos familias por era requieren ahora su tecnología básica. La producción natural de conocimiento evita dependencia circular. Ver capítulos 07/45.
- **D-03 — Alta:** el registro histórico confirma ejércitos automáticos, pero no había unidades ni combate detallado. Propuesta parametrizada v2.2: `data/combat_units.v2.2.json` + capítulo 43. No afirmamos balance real.
- **D-04 — Media:** habilidades con nombres de ahorro/reparación implicaban efectos nacionales que su JSON no tenía. Se han cambiado **descripciones**, no efectos; el `effect.target` sigue siendo la fuente de verdad. Revisión futura de UX necesaria para que nombres no induzcan a error.
- **D-05 — Alta:** `BALANCE_SIMULATION_REFERENCE.json` es un modelo grueso, incluye `milestonesAchieved:0` en escenarios que llegan al final; no constituye una verificación de los cinco hitos ni del motor. Queda marcado **HISTÓRICO NO AUTORITATIVO**.
- **D-06 — Media:** se habla de un árbol tecnológico, pero el contenido está formado por tres ramas homogéneas por era. Se concreta el lenguaje artístico/narrativo en capítulo 45, manteniendo bonos existentes. Una verdadera diversificación mecánica requeriría otro balance.
- **D-07 — Alta:** no existían wireframes pixel-precisos aprobados ni un pase de accesibilidad. Capítulos 46–50 concretan contratos visuales, pero **no sustituyen un art test físico**.
- **D-08 — Media:** `Project CHAOS` y `K0: The Experiment` se mezclaban. Se declara K0 como marca de trabajo visible; nombres de archivo y contratos CHAOS quedan por compatibilidad hasta migración futura, no como dos marcas de producto.
- **D-09 — Alta:** el producto requiere tres canales únicos, no un chat único para tres naciones. Este límite se mantiene explícito. No prometemos asignación multi-nación de un solo chat.
- **D-10 — Alta:** el SQL es un esquema propuesto y puede no soportar aún los nuevos catálogos de ejército/patrocinio. Se ha redactado el anexo `architecture/002_extensiones_diseno_v2.2.sql` y contratos conceptuales, pero deben integrarse como **migraciones y APIs versionadas** antes de desarrollo, sin declarar compatibilidad automática.

### Autoridad cuando hay contradicción

1. Mensaje explícito posterior del propietario. 2. Decisiones históricas 1–92 salvo sustitución documentada. 3. Decisiones v2.2 de esta revisión *solo para el alcance listado* D-01–D-10. 4. JSON de datos vigente y contratos. 5. Documentos 01–40 de v2.1; cualquier texto que afirme que el Consejo requiere oro se considera histórico. 6. Documentos de versiones previas.

Cada cambio de regla debe incluir `id`, antes, después, razón, impacto, archivos, necesidad de migración y pruebas; una temporada activa jamás cambia de versión sin cierre auditado.

### Semántica de los estados de cierre

- **LOCKED_DESIGN**: decisión exacta documentada, aún no necesariamente probada.
- **CANDIDATE_BALANCE**: cifra reproducible propuesta, modificable solo entre temporadas, pendiente de simulación.
- **VISUAL_BRIEF**: orden de producción, no aprobación de arte.
- **PROVIDER_GATE**: capacidad externa no acreditada; debe permanecer deshabilitada.
- **IMPLEMENTATION_GATE**: se requiere software y pruebas reales, imposible cerrar con prosa.
- **APPROVED**: existe evidencia técnica, artística o legal trazable. Ningún módulo del repositorio puede presumir `APPROVED` por figurar en una tabla.


---

## Fuente 42 — `docs/42_CONTRATOS_DE_ESTADOS_Y_TIEMPO_v2.2.md`

**Blob original:** `00e3ab5ee4d628188eda6927f863f9cc0f14bae1`.

## 42 — Contratos temporales, prioridades y semántica determinista

**Normativo para diseño.** Concreta escenarios de frontera y orden de eventos; no implementa el motor.

### Relojes separados

| Reloj | Unidad | Avanza con LIVE confirmado | Avanza offline | Usos |
|---|---|---|---|---|
| `UtcWallClock` | ms UTC | Sí | Sí | Timestamps, 2 h de actividad humana, periodos diarios/semanales |
| `NationEconomyClock` | segundos de simulación | 100 % de tiempo real | 20 % de tiempo real | Producción, mantenimiento, autoplanner |
| `NationLiveClock` | segundos LIVE | Sí | No | Elecciones, Consejo, prioridades, penalización territorial |
| `CompetitionLiveClock` | segundos de evento | Solo con 3 naciones LIVE confirmadas a la vez | No | RPS, descansos, batallas programadas |
| `SeasonClock` | secuencia lógica | Sí | Según evento de sistema | Orden de commits, snapshots y desempates |
| `PresentationClock` | frames | Sí | Sí cuando render está activo | Animación/subtítulos, jamás decide recursos |

La señal de proveedor incierta NO se interpreta como LIVE. Los temporizadores de elección/voto/torneo se congelan, la economía usa perfil conservador offline cuando se confirma desconexión y, en `UNCERTAIN`, aplica la política de seguridad del capítulo 29 hasta recuperar señal. Un reinicio de OBS no cambia tiempos de economía ni estado competitivo.

### Orden lógico de un tick de 5 segundos (enmienda v2.3)

Prevalece el orden exacto de [doc 64](64_RELOJES_EVENTOS_Y_CONTRATOS_v2.3.md): entrada LIVE/Inbox idempotente → comandos y papeletas válidos → cierres de votos/torneos → comida/economía/XP → obras/investigación/misiones → hitos/era → ganador/maravillas → commit y deltas. El tick se particiona por fronteras reales; recibidos exactamente en el límite LIVE de cierre son rechazados. Una elección pausada **no** tiene deadline UTC absoluto fijo; computar su tiempo restante en NationLiveClock.

Se deriva una sola vez economyDelta a partir del intervalo real y el multiplicador 100 %/20 %. En RPS/batalla, CompetitionLiveClock avanza solo cuando las tres naciones están LIVE; pérdida de una congela tiempo y resultado global, sin votos ni sanciones ficticios.

### Identidad, experiencia y estados

- `citizenId` es específico de `(season,nation,provider,providerUserId)`; una persona puede tener ciudadanos diferentes entre canales, nunca sumar votos en una nación por reintentos del mismo evento.
- Descansar no impide votar; sí impide contribuir producción humana sin renovar `!active` o repetir `!work` válido tras cooldown.
- La profesión no cambia durante temporada. Los niveles 3, 7, 12 permiten una habilidad por tramo; ausencia de selección = no perk, no elección automática.
- Avance de era cambia la etiqueta del oficio, nunca la profesión ni su XP. Los edificios permanecen en el mapa; los antiguos reciben factor de eficiencia cuando corresponde.
- Ningún evento estético, lectura de nombre, voz TTS, caída de FPS o reproducción atrasada de HUD modifica estado autoritativo.

### Reglas de salida de eventos múltiples

Si se alcanzan a la vez hitos, una elección y una obra, las mutaciones se confirman primero; la presentación prioriza victoria > era > resultado de voto > torneo > hambre > cosmética. Cola narrativa no altera orden de commits. Si un cronómetro reanuda tras 5 horas OFFLINE, conserva exactamente los segundos LIVE pendientes, sin «rellenar» votos ficticios.

### Ejemplos de aceptación

- Voto a `close - 1ms`: aceptable si válido y autenticado; a `close`: rechazado; mismo `sourceKey` repetido: un solo efecto.
- Desconexión con 47s restantes: mostrar 47s hasta confirmar nuevo LIVE; no avanzar si OBS sigue reproduciendo vídeo pregrabado.
- Usuario `!active` dos veces en 10s: primer comando renueva 2h, segundo no; chat casual no hace nada.
- Almacén lleno justo antes de un gasto: liberar capacidad y producir en siguiente segmento válido, no anticipar recursos inexistentes.
- Fin de temporada en tick concurrente con patrocinio: si el cierre se confirma primero, el patrocinio no compra ya un artículo de temporada cerrada; su evento se trata según política verificable sin perder trazabilidad.


---

## Fuente 43 — `docs/43_EJERCITOS_Y_COMBATE_AUTOMATICO_v2.2.md`

**Blob original:** `a6e83ccaec6392d26bce23fbe2418280cf05ef12`.

## 43 — Ejército, guarniciones y batallas automáticas

**Estado: regla de diseño v2.2, balance no simulado.** Resuelve las decisiones históricas 25, 26, 27 y 30 sin añadir ataques libres ni micromanagement de guerra. Fuente estructurada: `data/combat_units.v2.2.json`.

### Rol del ejército

El ejército es una capacidad automática de defensa territorial construida por infraestructura defensiva. No existe comando para atacar por chat ni guerras permanentes. Solo se disputa una **batalla automática programada** con las tres naciones LIVE confirmadas, separada del torneo inaugural de piedra/papel/tijera. El ganador de la temporada sigue siendo la primera nación que entra en Interestelar: la guerra nunca da puntos históricos ni oro.

### Unidades y escala

Cada una de las 13 eras tiene tres tipos de unidad equivalentes entre facciones: guardia (multiplicador 100 %), explorador (85 %) y especialista (115 %). Se generan 39 definiciones de rol/era; cada una tiene tres variantes visuales con siluetas y herramientas específicas de Micelios, Rúnicos y Ferrinos. **No son 117 estadísticas distintas:** el combate es simétrico entre especies. Fuerza base por unidad de era `e`: `10 + 2e` puntos enteros. Fuerza individual efectiva: `floor(base * rolePowerBp/10000)`.

Cada edificio defensivo completado puede sostener hasta seis unidades y genera **como máximo una cada 1.200 segundos LIVE**, alternando guardia→explorador→especialista. Límite total de nación: 120 unidades. No crecen offline. Una unidad cuesta materiales ordinarios descritos por era en el JSON, siempre después de proteger las reservas para alimento NPC y la siguiente obra cívica obligatoria. Nunca se gasta oro. Si el saldo es insuficiente, la producción militar espera; ningún NPC se ve obligado a abandonar comida/obras/hitos para reclutar. Las unidades permanecen al cambiar era; su ID y fuerza no se reescriben retroactivamente.

### Cálculo por encuentro

El operador programa el evento como máximo una vez cada 24 horas LIVE de campaña. Todos deben estar ONLINE/LIVE y disponer de edificio defensivo; si alguna nación está más de dos eras por detrás, se pospone para no convertir la sesión en paliza estructural. Tres encuentros A-B, B-C y C-A, uno por pareja. Para cada pareja se usa la suma de fuerzas de sus guarniciones: la defensa aplica el bono de gobierno militar (+500bp) y, si corresponde en el `NationLiveClock`, prioridad defensiva (+800bp), respetando el tope general de bonificaciones. Sin factores aleatorios de daño; si ambas fuerzas son iguales, empate. Victoria/empate/derrota por pareja = 2/1/0 puntos; tablas públicas muestran fuerza numérica sin revelar IDs privados de espectadores.

**Ejemplo:** dos guardias de era 1 dan `2 × floor(12 × 10000/10000)=24` puntos. Frente a una unidad especialista de era 1 (`floor(12 × 11500/10000)=13`), gana la fuerza 24 antes de aplicar bonificación defensiva. Es un ejemplo aritmético, no un resultado de balance completo.

### Consecuencias y límites

- Un ganador único puede infligir **la misma penalización máxima del sistema RPS**, únicamente a naciones que terminen por debajo: hasta 2 % de madera/piedra disponibles y sector secundario sin producción durante 30 minutos LIVE. Se aplica una vez por evento, sin sumarla dos veces cuando exista otra penalización territorial; si hay penalización activa se conserva la fecha de fin más tardía y nunca se bloquea producción básica esencial.
- Empate en primer lugar: ganadores compartidos sin sanción. No hay robo de oro, vidas, edificios, progreso tecnológico ni XP; no hay muertes permanentes de unidades.
- Ningún espectador elige golpes ni gasta oro para aumentar fuerza. La estrategia está en priorizar infraestructuras y economía de manera indirecta; el tamaño bruto del chat no determina por sí solo el resultado.
- Este tipo de evento ya está declarado en `data/events.v2.json` (revisión v2.2), **sin afirmar que exista un motor capaz de ejecutarlo**. Antes del desarrollo hay que versionar ese catálogo y ampliar SQL/contratos conforme a esta especificación.

### Presentación y accesibilidad

60 s de introducción, 15 s de lectura de fortalezas, máximo 3 escenas de 25 s por pareja, 10 s de resultado general y tabla de penalizaciones. Los visuales son una representación teatral: agentes y proyectiles son cosméticos; el resultado se decide al cerrar el cálculo autoritativo. Subtítulos de Doctor K-0 siempre disponibles. Sin sangre, amputaciones, armas realistas ni apuestas.

### Pruebas obligatorias

`B-01` tres fuerzas iguales = todos empate y cero sanciones. `B-02` gobierno militar afecta solo defensa de combate, nunca RPS. `B-03` recurso bajo reserva: no se crea unidad. `B-04` origen offline: no se recluta. `B-05` 120 unidades: no se sobrepasa. `B-06` un directo interrumpido: evento se congela/cancela según operador, sin saldo parcialmente descontado. `B-07` mismo evento reintentado: ninguna pérdida duplicada. `B-08` falta de defensa y gap>2: torneo se pospone documentando razón.


---

## Fuente 44 — `docs/44_CONSEJO_GRATUITO_PATROCINIO_Y_ECONOMIA_v2.2.md`

**Blob original:** `3a7dab2acc5bb5786a0675b42d6f385550428305`.

> **Enmienda v2.3:** la terna ofrece **un único Consejo ordinario por nación/era jugable**; mantener decisiones históricas sobre coste oro=0. Ver [CURRENT_SPEC](CURRENT_SPEC.md).

## 44 — Consejo gratuito, maravillas y patronazgo cosmético

### Corrección prioritaria v2.2

Los 39 proyectos estratégicos y las 13 maravillas dejan de requerir oro. Todos se financian con la economía ordinaria de las civilizaciones. No se modifica su huella, trabajo o coste ordinario. Los catálogos vigentes tienen `cost.gold=0` y `accessPolicy=FREE_ORDINARY_RESOURCES_ONLY`. El motivo es de UX y monetización sana: la **participación colectiva en la construcción no puede depender de que alguien done**. No se cambia el requisito de disponer individualmente de los recursos ordinarios para las tres alternativas del Consejo.

### Consejo: semántica exacta

1. Evento habilitante de era/hito y ninguna votación de gobierno/prioridad abierta en nación. 2. Seleccionar tres opciones distintas, no construidas, pertenecientes a era válida, cada una costeable con stock disponible ordinario. 3. Bloquear reserva vectorial `hold[r] = max(costO1[r],costO2[r],costO3[r])`. 4. Voto comunitario 600 segundos LIVE, `!build <id>`, última papeleta válida por ciudadano. 5. Elegir mayoría; en empate RNG uniforme determinista; cero votos también sorteo auditado. 6. Deducir SOLO coste elegido desde reserva y liberar resto; insertar obra sin duplicados. 7. Las otras dos opciones quedan descartadas para esa nación durante esa era. No se abre un segundo Consejo ordinario de la misma era: los tres candidatos se consumen como terna al resolver una única votación.

Ejemplo con tres proyectos cuyos costes son (madera,piedra)=(120,85),(120,85),(120,85): la reserva es (120,85), **no** (360,255). Si el ganador cuesta (120,85), se consumen una sola vez 120 y 85. Si cambian recursos mientras se vota, la reserva mantiene su derecho; gastos de otras obras solo utilizan `stock - reserved`.

### Maravillas

Una maravilla por era es exclusiva globalmente: la primera construcción **completada y confirmada** en el estado autoritativo obtiene reconocimiento. Puede existir un `wonder_festival` programado que habilite construcción/decisión si las tres naciones son elegibles. El coste es ordinario; el oro no acelera obras. Si dos terminan durante el mismo tick, el orden persistido de commit + clave de nación desempata. La maravilla de Interestelar es epílogo ilustrativo y no se construye como competición tras el cierre de temporada.

### Oro y reconocimientos

El oro solo nace de aportaciones verificadas permitidas por proveedor, nunca de mensajes, likes ni NPC. Los artículos definidos en `data/cosmetic_sponsorship.v2.2.json` son: insignia de apoyo (25 unidades), placa moderada (100) y dedicación ceremonial no competitiva (250). **Precios de diseño en oro interno**, no en euros ni en monedas reales. Se exige consentimiento para nombre público; nadie queda excluido del Consejo ni de los torneos por no adquirirlos. Las placas se moderan y retiran si se revierte el evento económico, sin reescribir el ledger histórico. El reconocimiento nunca incrementa la fuerza, producción, prestigio competitivo de victoria ni probabilidad de ser seleccionado como personaje visible.

### Monetización desconectada

Si `liveMonetizationEnabled=false` (valor actual), todos los mecanismos de adquisición de oro real y de compra de artículos quedan **DESHABILITADOS**. El resto de la experiencia —misiones, Consejos, maravillas, elección, era, torneos y actos de K-0— funciona con NPC y usuarios gratis. No se muestran llamadas a comprar. Configurar una tasa futura requiere revisar cada plataforma; no se inventa equivalencia regalo/moneda.

### Compatibilidad de documentos anteriores

Cualquier pasaje de docs 05, 08, 10, 18, 33 o 35 que hable de proyectos **obligatoriamente financiados con oro** queda sustituido por este capítulo y por el catálogo actualizado. Las tablas legibles 35 han sido regeneradas con costes sin oro. No modificar un presupuesto ya persistido en una temporada activa: esta revisión solo sirve para temporadas futuras y diseño actual.


---

## Fuente 45 — `docs/45_TECNOLOGIAS_Y_IDENTIDAD_POR_ERA_v2.2.md`

**Blob original:** `c7a65c3ebfa8b6adcb739112db576386fb97cbf0`.

## 45 — Matriz de identidad tecnológica de las 13 eras

**Estado:** dirección de contenido normativa, beneficios numéricos todavía candidatos. `data/technologies.v2.json` contiene tres tecnologías por era y conserva sus identificadores; este capítulo les da intención temática y lenguaje audiovisual para que las 39 no parezcan la misma tecnología renombrada. No se inventan nuevas bonificaciones económicas.

### Cadena y desbloqueos

Una tecnología troncal `tech_{era}` cuesta conocimiento y se completa automáticamente cuando existen puntos disponibles, tras respetar las reservas materiales acordadas. Desbloquea taller y centro de saber de SU era. Desde v2.2 los dos edificios requieren `requiresTechId=tech_{era}`; el conocimiento puede producirse desde el emplazamiento natural inicial. Los cinco hitos por era incluyen un hito científico que exige la tecnología troncal, pero ninguna investigación depende de un edificio que ella misma desbloquea. Las dos opcionales de cada era siguen sin oro ni puntos históricos directos; economía añade +200bp al output económico y defensa +200bp a defensa en torneos automáticos; estas bonificaciones persisten solo con el alcance/stack del ruleset, sin efectos mágicos no definidos.

| Era | Tecnología central: significado en ficción | Economía: representación de «Logística» | Defensa: representación de «Protección» | Icono narrativo |
|---|---|---|---|---|
| Paleolítico | Dominio de herramientas y registro oral | Rutas entre recolección y campamento | Vigilancia de refugios | Piedra tallada |
| Neolítico | Agricultura organizada y asentamiento | Graneros y calendarios de cosecha | Empalizadas | Semilla |
| Cobre | Conductividad y primera forja | Pesaje y rutas de metal | Escudos y avisos de campamento | Lingote |
| Bronce | Aleaciones, escritura y talleres | Comercio de talleres especializados | Fortines reforzados | Crisol |
| Hierro | Herramienta resistente e infraestructura | Vías de forja y transporte | Puestos de guardia | Yunque |
| Antigüedad | Ciudad, administración y método | Redes cívicas y almacenes | Formaciones ciudadanas | Columna |
| Edad Media | Gremios, fortificación y archivo | Mercados y caravanas | Torre de vigilancia | Torre |
| Renacimiento | Instrumento, cartografía y experimentación | Rutas cartografiadas | Ingeniería de defensa | Compás |
| Industrial | Energía mecánica y producción | Cadenas de suministro | Máquinas defensivas | Engranaje |
| Moderna | Electricidad, comunicaciones y control | Vehículos y distribución | Red de alerta | Bobina |
| Digital | Información, simulación y automatización | Optimización logística de datos | Seguridad de sistemas | Chip |
| Espacial | Ingeniería orbital y supervivencia | Abastecimiento en vacío | Escudos de estación | Órbita |
| Interestelar | Navegación entre sistemas y epílogo | Representación ceremonial sin nueva carrera | Representación ceremonial | Estrella |

### Experiencia de árbol de investigación

Cada pantalla de una era muestra exactamente tres nodos: **troncal arriba**, economía izquierda, defensa derecha. La troncal indica condición automática, coste restante y edificios futuros; las opcionales muestran coste de conocimiento y bonus exacto expresado en % + duración. Una tecnología futura bloqueada no debe figurar como disponible. La interfaz no promete 39 decisiones manuales: 13 son troncales automáticas y 26 opcionales sujetas a reglas.

Las investigaciones opcionales no cambian el calendario de era obligatorio ni introducen dependencia circular. La descripción artística no se interpreta como sistema nuevo (un «vehículo» dibujado no aumenta velocidad si no hay regla). El diseñador debe poder listar por ID: entrada, prerrequisitos, coste, efecto, caducidad y estado visual.

### Limitación creativa explícita

Aunque las escenas y metáforas anteriores ya están especificadas, los efectos lúdicos de las 26 investigaciones opcionales siguen siendo homogéneos y lineales. Para una experiencia estratégica profunda haría falta introducir efectos diversos y recalcular balance; **no se declara un árbol ramificado complejo** hasta que exista tal catálogo con pruebas. Evitar etiquetar esta matriz como «árbol tecnológico diverso validado» en marketing.


---

## Fuente 46 — `docs/46_MANUAL_DE_ESTILO_PIXEL_ART_v2.2.md`

**Blob original:** `eecbb5d3fb1391469dbd740bb0c05dd862aad975`.

## 46 — Manual de estilo visual y control de consistencia

**Estado: contrato de diseño pixel art, no assets aprobados.** Define restricciones reproductibles para artistas y futuras herramientas. No debe copiar sprites, paletas ni animaciones ajenas; Terraria es referencia de densidad/lectura, no un catálogo reutilizable.

### Gramática de pixel art

- Proyección de terreno oblicua **2:1**; tile romboidal de **32 × 16 píxeles lógicos**. Personas: frame base **16 × 24**, cuatro direcciones NE/SE/SW/NW. Sin rotación libre de sprites, bilinear, anti-aliasing ni escalas fraccionarias en escenas pixel-perfect. Bordes de 1 píxel, sombras de suelo separadas, hasta 24 colores por spritesheet de personaje.
- Escala vertical lógica **360 × 640** a 1080 × 1920; horizontal **640 × 360** a 1920 × 1080; `nearest-neighbor`; 30 FPS objetivo. El arte nunca contiene texto integrado que deba localizarse; rotulaciones en UI.
- Luz principal común desde arriba-izquierda (dirección proyectada NW); sombras de contacto de 1–2 píxeles con alfa discreta. Sombras de edificios no pueden ocultar la celda de acceso ni texto. No utilizar partículas permanentes encima de votaciones.
- El pixel no es una limitación estética opcional: curvas y contornos deben seguir escalones limpios de 1/2/3 píxeles, sin texturas ruidosas subpíxel. La claridad de forma prevalece sobre detalle ornamental.

### Paleta y códigos cromáticos

| Facción | Color ancla | Contorno | Relación de formas | Material primario |
|---|---|---|---|---|
| Micelios | `#6FAD78` | `#20262C` | Cúpulas y tallos orgánicos | Fibras, esporas, micelio iluminado |
| Rúnicos | `#769BCB` | `#20262C` | Prisma, plano quebrado y monolito | Mineral segmentado y runa |
| Ferrinos | `#C17B59` | `#20262C` | Articulaciones, triángulos y placas | Exoesqueleto bioférreo, no robot |

Colores ancla ya fijados en el catálogo. Las sombras, medios tonos y acentos secundarios deben derivarse de una **paleta maestra de 24 posiciones** aprobada visualmente; **no se inventa aquí una paleta final de 24 colores sin ver cómo funciona sobre sprites reales**. El éxito se juzga en monocromo y a resolución de salida, no solo por su hexadecimal.

### Siluetas y lectura

**Micelio:** capuchón grande e identificable a 1×, torso blando, dos miembros cortos, bioluminiscencia en articulaciones, sin tentáculos marinos ni coral. **Rúnico:** cabeza prismática, torso denso, 2 hombros escalonados; líneas rúnicas se leen como acento, no como láser. **Ferrino:** cabeza trapezoidal con visor orgánico, cintura estrecha, placas de oxidación; no usar cascos militares humanos. **Doctor K-0:** científico cyborg de silueta asimétrica, un ojo óptico, mandíbula segmentada, brazo parcialmente industrial, bata o insignia de laboratorio corta; nunca una mascota alienígena blanda.

### Módulos visuales repetibles

Los 130 edificios mantienen 10 familias reconocibles (vivienda, alimentación, biomasa, extracción, taller, saber, almacén, infraestructura, cívico, defensa) y 13 épocas. El artista crea una **forma base por familia y facción**; el cambio de época añade materiales/tecnología visibles (ver capítulo 26) sin reescribir todas las siluetas. Cada obra tiene cuatro etapas: cimientos (15 %), estructura (40 %), obras (70 %), final (100 %); fase 4 no se representa antes del commit económico. Todas las parcelas respetan `footprintTiles` y su pivote.

### Especificación de animación

Frames y FPS exactos en `data/art_spec.v2.json`: idle 4@4FPS, walk 6@8, gather 5@6, haul 6@8, build 5@6, research 5@6, celebrate 5@6, rest 2@1, react 4@6. Animación de trabajo visible siempre es derivada del estado lógico, sin añadir output económico. Cuatro direcciones en todas las acciones. Evitar clonación robótica: variación cosmética por fase/semilla, sin mover hitbox ni alterar tick.

### Criterios de aceptación de arte

1. Identificar facción y profesión en cinco segundos con sprite a 1× sin etiqueta. 2. La miniatura de una obra se distingue de las otras nueve familias. 3. En escenario vertical con 45 ciudadanos, 90 % de observadores de prueba reconocen el evento principal. 4. Nadie confunde datos de nación por el color exclusivamente. 5. Se prueba contraste en desaturado y diferentes fondos. 6. No hay uso de imágenes, fuentes, músicas o personajes de terceros sin licencia comercial verificable. 7. Anclas, huellas, animaciones y exportación son consistentes en atlas para las tres facciones.

La palabra **FINAL** se reserva a sprites/aprobaciones reales. Este documento especifica un estilo; no acredita todavía la producción artística.


---

## Fuente 47 — `docs/47_LAYOUT_HUD_Y_ESCENAS_PIXEL_PERFECT_v2.2.md`

**Blob original:** `4176ca96aec45e3e28fbd22fc04827078c478164`.

> **Enmienda normativa v2.3 (multistreamer distribuido):** cada output remoto puede usar NATION_FOCUS, SHARED_WORLD o EVENT_STAGE (solo si policy lo permite). Tres clientes renderizan el mismo estado, con clocks y secuencias de servidor; sus FPS no cambian el motor. [Especificación vigente](CURRENT_SPEC.md).

## 47 — Wireframes textuales, HUD y comportamiento de pantalla

**Estado: design token de layout, pendiente de test visual.** Las medidas son píxeles lógicos; la UI debe soportar 360×640 vertical y 640×360 horizontal, escalables enteros a 1080×1920 y 1920×1080.

### Vertical 360 × 640

| Área | Rectángulo aproximado `x,y,w,h` | Función | Prioridad |
|---|---|---|---|
| Franja superior | `0,0,360,90` | Emisión, nación, era, puntos de historia, estado LIVE | Máxima |
| Ventana de mundo | `0,90,360,422` | Ciudad, caminos, unidades, K-0 en escena | Central |
| Panel inferior | `0,512,360,128` | Recursos condensados, evento activo, comandos de participación | Máxima |
| Cartela K-0 | `16,410,328,86` | Subtítulo flotante **solo si** no oculta voto/resultado | Contextual |

Se reserva mínimo 8px de padding lógico externo y 4px de separación interior. Nunca se dibuja contenido crítico a menos de 24px de los extremos de salida final adaptados a controles del proveedor (safe areas deben medirse por plataforma). El mundo puede reducirse más ante overlays nativos de chat; la interfaz presenta modo compacto si no cabe.

### Horizontal 640 × 360

| Área | Rectángulo `x,y,w,h` | Función |
|---|---|---|
| Mundo | `0,0,467,360` | Escenario 2:1, cámara principal, Doctor K-0 |
| Panel lateral | `467,0,173,360` | Era, hitos, recursos y eventos |
| Subtítulo K-0 | `20,284,425,52` | Texto de dos líneas, sin tapar panel |

Estos rectángulos concretan el objetivo anterior de aprox. 73 % mundo y 27 % panel. En eventos críticos (voto, torneo, evolución) se permite un modal de escena que sustituya HUD secundario, jamás el indicador de nación, el temporizador ni el estado LIVE.

### Tipografía y contenido

Encabezados 12–14px lógicos, recursos 10–12px, subtítulo 12px mínimo en superficie equivalente; los tamaños son **punto de partida de prototipo**, sujetos a pruebas de legibilidad real en móvil. Fuente de píxel abierta/licenciada comercialmente, con conjunto de glifos español/inglés, acentos y números tabulares. No se licencia aquí ninguna fuente concreta. Nunca animar contador tan rápido que deje de leerse; recursos pueden abreviarse 1.2k pero sus valores exactos quedan en detalle.

### Ocho escenas obligatorias

1. `BOOT_CHECK`: marca, estado de canales, sin simular ganador. 2. `WORLD`: ciudad y actividad, estado nación y era. 3. `GOV_VOTE`: tres gobernantes NPC, barras de votos mostrables y segundos LIVE restantes. 4. `PRIORITY_VOTE`: ramas economía/ciencia/defensa, bonus expresado como % real. 5. `COUNCIL_VOTE`: tres proyectos diferenciados, coste ordinario, votos por opción y temporizador. 6. `TOURNAMENT`: RPS con recuento de participantes pero **sin distribución de elecciones** hasta cierre, luego marcador. 7. `ERA_TRANSITION`: ceremonia y nuevo inventario visual, nunca adelanta era sin commit. 8. `SEASON_END`: ganador y archivos históricos; se cierran inputs competitivos.

### Estados transversales

`LIVE`, `OFFLINE`, `UNCERTAIN`, `WAITING_FOR_PLAYERS`, `VOTE_PAUSED`, `OPERATOR_PAUSED`, `READ_ONLY_RECOVERY`, `SAFE_SCENE`. Para cada estado deben existir banner, texto explicativo, accesibilidad subtitulada y colores/íconos distinguibles sin depender del color. Un voto abierto muestra: nombre, regla, opciones, tiempo LIVE, mensaje de confirmación/rechazo, número total de votantes. No mostrar donaciones como requisito para participar.

### Experiencia sin chat

Toda salida debe poder leerse sin sonido y sin escribir: al menos nombre y estado de nación, era, progreso, evento y próximo punto de acción. La escena no debe diseñarse para que el espectador necesite un panel web externo. El público que mira desde otra plataforma recibe información pública permitida, nunca identidad cruzada no consentida.

### Criterios visuales de aprobación

Capturas obligatorias por escena y formato en condiciones: primera era, era digital, 0/45/90 avatares, vote tie, fin de temporada, modo seguro, subtítulo máximo, texto inglés más largo y safe-area nativa. Medir truncados, solapamientos, contraste y lectura desde móvil a tamaño real; un wireframe textual no equivale a dichas capturas.


---

## Fuente 48 — `docs/48_DOCTOR_K0_PERSONAJE_VOZ_Y_NARRACION_v2.2.md`

**Blob original:** `7868bb2c693eb069199846b0c86ae8040c9e62bd`.

## 48 — Doctor K-0: personaje, restricciones y dramaturgia

### Función dramática

**Doctor K-0** es un científico cyborg con cuerpo presente dentro de la escena de mundo. Su experimento observa la evolución de tres civilizaciones y presenta sus decisiones a la audiencia. Es sarcástico, impaciente y cómico, pero **no parcial**. Nunca cambia recursos, elige ganador, inventa aportaciones ni suplanta acciones del operador. El arco del personaje consiste en descubrir que el experimento es más complejo de predecir de lo que él creía; la comunidad decide el resultado, no su narración.

### Diseño corporal obligatorio

Cabeza asimétrica con un ojo óptico dominante (puede usar el cero de K0 como motivo de luz), mandíbula o máscara mecánica articulada, cuello rígido con cableado corto, torso de laboratorio reforzado, un brazo más cibernético que el otro, manos expresivas de tres dedos, botas de soporte. Proporción del sprite mundial compatible con escala 2:1 y con el personaje de 16×24 como referencia de lectura; el retrato de HUD puede tener más resolución sin convertirse en especie distinta. Silueta angular y excéntrica, no diminuto alien/mascota. Sin apropiación de diseños ajenos reconocibles.

### Emociones/poses

`NEUTRAL`, `CURIOUS`, `AMUSED`, `WARNING`, `CELEBRATING`, `DISAPPOINTED`, `ERROR_SAFE`. Ojo óptico parpadea solo como FX; el color de K-0 nunca identifica nación favorecida. Gestos: señalar obra, consultar terminal, levantar visor, recoger ficha de voto, suspender experimento ante fallo, entregar trofeo. La animación es cosmética; la emisión no debe bloquearse esperando gesto.

### Contrato editorial

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

### Ejemplos de texto original

- Inicio: «Abrimos las puertas del laboratorio. Tres culturas, un único resultado. Ah, y vosotros tenéis acceso al panel de mandos. Terrible idea.»
- Hambre: «No, la ciencia no ha inventado aún el desayuno infinito. Necesitamos alimentos.»
- Consejo: «Tres proyectos, todos financiables sin monedas de apoyo. Podéis votarlos; prometo no construir el peor… por iniciativa propia.»
- Era: «Confirmado. El experimento acaba de superar otra frontera histórica.»
- RPS: «Registrando votos. No os diré lo que eligió vuestro vecino: se llama imparcialidad.»
- Incidente: «Conexión incierta. Congelamos las votaciones hasta comprobar que volvemos a estar en directo.»
- Final: «Resultado confirmado: {nation}. Se cierra la temporada. Las otras dos civilizaciones conservan su historia.»

### Generación lingüística segura

Plantillas validadas y variables escapadas antes que lenguaje libre. El LLM, si se activa, solo reescribe forma y humor; recibe hechos agregados y acciones ya confirmadas, nunca credenciales ni mensajes crudos. Límite editorial sugerido: una intervención prioritaria cada 20s y cola de 20; cambios de estado críticos tienen preferencia y subtítulo directo si voz falla. Nunca leer nombres de menores, datos personales, insultos o contenido recibido como instrucciones. Idioma de campaña configurable (inicial `es-ES`, alternativa `en-US`) y TTS con derechos comerciales verificados.

### Qué todavía se debe aprobar

El diseño gráfico final de K-0, casting o síntesis de voz, timbre, pronunciación oficial de K-0, expresiones y poses por formato requieren **muestras reales**. Este documento sí establece sus restricciones, pero no puede autorizar un rostro o voz aún no producidos.

