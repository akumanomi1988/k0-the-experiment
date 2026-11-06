# 07 — Progresión histórica, investigación y temporadas

## Eras y victoria
13 épocas (orden congelado en `eras.v2.json`): paleolithic, neolithic, copper, bronze, iron, antiquity, medieval, renaissance, industrial, modern, digital, space, interstellar. Todos los mundos inician la primera época en un commit global. `EraReadyPending` se alcanza al reunir 100 puntos y se confirma nueva era únicamente con nación LIVE. La **primera entrada confirmada en `interstellar`** fija ganador y termina la competición de inmediato. La era final sirve como epílogo visual y archivo, **no abre elecciones ni un nuevo ciclo jugable**, excepción imprescindible para no contradecir el cierre al entrar en ella.

## Hitos y barra
Cada era jugable (1–12) tiene cinco hitos únicos de 20 puntos: producción de comida; producción de madera **y** piedra; conocimiento + investigación básica completada; finalización del ágora cívica automática; y primera misión colectiva completada durante esa era. La misión puede ser diaria o semanal, pero solo puntúa una vez por era. Los objetivos cuantitativos son `data/milestones.v2.json`. Se contabilizan unidades **producidas efectivamente y aceptadas** en esa era, no entradas de misiones ni consumos, y por eso no pueden repetirse para acelerar. Los 100 puntos no se multiplican por audiencia ni por donaciones. Los hitos cumplidos fuera de emisión se guardan; la ceremonia queda pendiente. El hito de era interestelar está materializado como catálogo de epílogo, no es exigido para ganar.

## Árbol tecnológico
Para cada era: 1 investigación automática de ruta gratuita `tech_{era}` y 2 opcionales de economía/defensa, todas sin oro. Conocimiento producido se almacena y gasta; la investigación automática se inicia si hay conocimiento después de respetar reservas de obras. Ninguna tecnología es prerrequisito circular de los hitos del mismo período. Las ramas optionales se anuncian; no retrasan la entrada a era siguiente. La prioridad votada no bloquea caminos, solo bonifica temporalmente una categoría.

## Rendimiento y duración
El objetivo narrativo son 2–3 días por era, no una promesa técnica. El baseline fija 20 % de economía offline y umbrales lineales; el balance real depende de horas de directo, espectadores y distribución de profesiones. Para reducir dependencia de audiencia masiva, los hitos no escalonan por cantidad de participantes, y el trabajo extra tiene rendimiento marginal decreciente. Solo se cambiarán valores entre temporadas tras una simulación completa de todos los hitos; cambios intratemporada requieren evento de migración auditado y anuncio.

## Cierre y persistencia
Al cerrar temporada se publica `SeasonCompleted`: nación ganadora, fecha, reglas y hashes, estadísticas de trabajo, economía, obras, elecciones y torneos; se convierte oro sin gastar en puntuación de prestigio visual 1:1, sin opción de canje y sin bonus en la siguiente carrera. No migran recursos, edificios, XP ni profesiones; sí identidad de proveedor para facilitar recuperar usuario, historial de logros, badges y estadísticas. Los ciudadanos de la nueva temporada son registros nuevos asociados a la identidad previa.
