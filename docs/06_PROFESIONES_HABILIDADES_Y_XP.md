# 06 — Ciudadanos, profesión única, XP y especializaciones

`!join` crea o recupera un ciudadano desde una identidad de proveedor autenticada en un canal autorizado; no exige ciudadanía previa; no asigna oficio ni inicia producción. `!work <familia>` elige única familia durante temporada. Repetir la misma familia o `!active` prolonga `activeUntilUtc=receivedUtc+7200s` tras validación y cooldown de 60s; escoger otra familia devuelve `PROFESSION_LOCKED` sin renovar. El tiempo de trabajo no se acumula: renovar no añade dos horas al saldo previo. Una inscripción tardía puede participar en votos mientras el período esté abierto.

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
El límite humano **es global por nación**, nunca por oficio: puestos 1–100 al 100 %, 101–2500 al 25 %, posteriores al 0 %. Todas las profesiones comparten los mismos 2500 puestos; los NPC no ocupan cuota humana. Orden determinista `(activeSinceUtc,citizenId)` sobre ciudadanos con profesión y actividad vigente; se actualiza al entrar/salir de actividad, **sin rotación por hash ni turnos de diez minutos**. La actividad sigue vigente durante 7200 s aunque el cupo se agote.

**XP de trabajo:** solo se concede por minutos efectivos de actividad productiva aceptada y con peso positivo, usando la misma cuota, multiplicador LIVE/offline y restos enteros por ciudadano. Sin tarea real, sin producción aceptada (almacén lleno), o fuera de cupo, la XP de trabajo es **cero**. El ciudadano conserva su representación, participación, voto, historial y logros no laborales; no se inventa XP residual. El HUD muestra «actividad registrada, sin producción: cupo nacional completo» cuando corresponda.

## Trabajo y sueño
El ciudadano descansa exactamente al caducar `activeUntilUtc`. Un evento de plataforma retrasado no vuelve a activar una ventana del pasado más allá del límite de tolerancia. No hay muerte permanente ni barras de hambre individuales. El nombre visual es moderado; se registra ID interno separadamente del displayName público.
