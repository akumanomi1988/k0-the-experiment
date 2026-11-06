# 06 — Ciudadanos, profesión única, XP y especializaciones

`!join` registra una identidad verificada de canal; no asigna oficio ni inicia producción. `!work <familia>` elige única familia durante temporada. Repetir la misma familia o `!active` prolonga `activeUntilUtc=receivedUtc+7200s` tras validación y cooldown de 60s; escoger otra familia devuelve `PROFESSION_LOCKED` sin renovar. El tiempo de trabajo no se acumula: renovar no añade dos horas al saldo previo. Una inscripción tardía puede participar en votos mientras el período esté abierto.

## Niveles
Al terminar cada segmento de trabajo efectivo, `xp += floor(6 * effectiveWorkMinutes)` con resto persistido; la XP off-live recibe factor 0,2. Nivel N requiere XP acumulada `250*(N-1)^2`, hasta nivel 20. Activación, voto, chat, caminar y renderizar no dan XP. Las recompensas de misión pueden otorgar XP si están explícitas; default de v2.2: misiones colectivas solo recursos, no XP adicional, para no duplicar. Los NPC no suben niveles ni desbloquean skills.

## Árboles
Tres elecciones irreversibles en niveles 3, 7 y 12; dos opciones exactas por bifurcación. `data/skills.v2.json` fija 30 habilidades, cada una con efecto objetivo y `additiveBp`. Los efectos son **personales**: no existen auras de reducción colectiva que crezcan sin techo con miles de usuarios. Habilidades históricas de 'rationing', 'reuse' e 'innovator' se redefinen como productividad/eficiencia individual equivalente sin impacto monetario, manteniendo intención temática pero eliminando exploit de multiplicación global. Máximo acumulado +1800bp por ciudadano. Sin `!skill`, no se asigna nada. Al volver a temporada siguiente se conserva historial de elecciones en museo, no se conserva bonus.

## Familias
- food: alimento de terreno o edificio según era, con sprite cazador→síntesis.
- wood: madera/biomasa; la etiqueta cambia, el resourceId `wood` no cambia.
- mine: piedra y mineral (mineral desde era 3), sin material por época arbitrario.
- build: aporta `buildWorkMilli` a obras comprometidas; si no hay obras, no crea recursos, pero puede hacer animación de mantenimiento y no gana XP por tarea ficticia.
- research: genera conocimiento con acumulación y desbloqueos automatizados gratuitos de tecnología.

## Control de audiencia masiva
Cada identidad puede tener un ciudadano por nación/temporada dentro de reglas de asignación de canales. Para trabajo agregado hay 100 plazas de contribución plena por profesión y 2400 plazas marginales al 25 %. Un humano fuera del tope sigue apareciendo, votando y alcanzando logros sin crear recursos ficticios; para evitar falsos mensajes de progreso se le muestra explícitamente el estado «turno visual / lista de trabajo saturada» y no se le abona XP de trabajo inexistente. El algoritmo de cuotas deterministic permite rotación por bloques de 10 minutos de LIVE para que los últimos usuarios no queden siempre sin producción; orden de rotación `(hash(citizenId,rotationIndex),citizenId)`.

## Trabajo y sueño
El ciudadano descansa exactamente al caducar `activeUntilUtc`. Un evento de plataforma retrasado no vuelve a activar una ventana del pasado más allá del límite de tolerancia. No hay muerte permanente ni barras de hambre individuales. El nombre visual es moderado; se registra ID interno separadamente del displayName público.
