# 45 — Matriz de identidad tecnológica de las 13 eras

**Estado:** dirección de contenido normativa, beneficios numéricos todavía candidatos. `data/technologies.json` contiene tres tecnologías por era y conserva sus identificadores; este capítulo les da intención temática y lenguaje audiovisual para que las 39 no parezcan la misma tecnología renombrada. No se inventan nuevas bonificaciones económicas.

## Cadena y desbloqueos

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

## Experiencia de árbol de investigación

Cada pantalla de una era muestra exactamente tres nodos: **troncal arriba**, economía izquierda, defensa derecha. La troncal indica condición automática, coste restante y edificios futuros; las opcionales muestran coste de conocimiento y bonus exacto expresado en % + duración. Una tecnología futura bloqueada no debe figurar como disponible. La interfaz no promete 39 decisiones manuales: 13 son troncales automáticas y 26 opcionales sujetas a reglas.

Las investigaciones opcionales no cambian el calendario de era obligatorio ni introducen dependencia circular. La descripción artística no se interpreta como sistema nuevo (un «vehículo» dibujado no aumenta velocidad si no hay regla). El diseñador debe poder listar por ID: entrada, prerrequisitos, coste, efecto, caducidad y estado visual.

## Limitación creativa explícita

Aunque las escenas y metáforas anteriores ya están especificadas, los efectos lúdicos de las 26 investigaciones opcionales siguen siendo homogéneos y lineales. Para una experiencia estratégica profunda haría falta introducir efectos diversos y recalcular balance; **no se declara un árbol ramificado complejo** hasta que exista tal catálogo con pruebas. Evitar etiquetar esta matriz como «árbol tecnológico diverso validado» en marketing.
