> **Regla vigente:**** el límite de 2500 trabajadores humanos efectivos aplica **a toda la nación**, entre todas las profesiones hasta revisar el balance; la XP usa deltaEconomy efectivo una sola vez. Ver [CURRENT_SPEC](ESPECIFICACION.md) y [doc 64](64_RELOJES_EVENTOS_Y_CONTRATOS.md).

# 06 — Ciudadanos, profesión única, XP y especializaciones

`!join` crea o recupera ciudadanía desde una identidad autenticada del proveedor en un canal autorizado, sin registro previo; no asigna oficio ni inicia producción. `!work <familia>` elige única familia durante temporada. Repetir la misma familia o `!active` prolonga `activeUntilUtc=receivedUtc+7200s` tras validación y cooldown de 60s; escoger otra familia devuelve `PROFESSION_LOCKED` sin renovar. El tiempo de trabajo no se acumula: renovar no añade dos horas al saldo previo. Una inscripción tardía puede participar en votos mientras el período esté abierto.

## Niveles
Al terminar cada segmento de trabajo efectivo, `xp += floor(6 * effectiveWorkMinutes)` con resto persistido; la XP en OFFLINE deriva del tiempo de economía efectivo al 20 %, **sin volver a aplicar 0,2**. Nivel N requiere XP acumulada `250*(N-1)^2`, hasta nivel 20. Activación, voto, chat, caminar y renderizar no dan XP. Las recompensas de misión pueden otorgar XP si están explícitas; default de v2.2: misiones colectivas solo recursos, no XP adicional, para no duplicar. Los NPC no suben niveles ni desbloquean skills.

## Árboles
Tres elecciones irreversibles en niveles 3, 7 y 12; dos opciones exactas por bifurcación. `data/skills.json` fija 30 habilidades, cada una con efecto objetivo y `additiveBp`. Los efectos son **personales**: no existen auras de reducción colectiva que crezcan sin techo con miles de usuarios. Habilidades históricas de 'rationing', 'reuse' e 'innovator' se redefinen como productividad/eficiencia individual equivalente sin impacto monetario, manteniendo intención temática pero eliminando exploit de multiplicación global. Máximo acumulado +1800bp por ciudadano. Sin `!skill`, no se asigna nada. Al volver a temporada siguiente se conserva historial de elecciones en museo, no se conserva bonus.

## Familias
- food: alimento de terreno o edificio según era, con sprite cazador→síntesis.
- wood: madera/biomasa; la etiqueta cambia, el resourceId `wood` no cambia.
- mine: piedra y mineral (mineral desde era 3), sin material por época arbitrario.
- build: aporta `buildWorkMilli` a obras comprometidas; si no hay obras, no crea recursos, pero puede hacer animación de mantenimiento y no gana XP por tarea ficticia.
- research: genera conocimiento con acumulación y desbloqueos automatizados gratuitos de tecnología.

## Control de audiencia masiva
**Una cuenta K0 tiene exactamente un ciudadano y una nación por temporada.** `!join` crea internamente su cuenta desde identidad de proveedor verificada; otro canal/nación devuelve `NATION_LOCKED`. Si se usan proveedores distintos, solo una vinculación de identidad voluntaria y verificada permite imponer la unicidad cruzada. **El cupo de trabajo es nacional**, de 100 puestos plenos más 2.400 al 25 % para todas las profesiones sumadas; fuera de 2.500 no se produce ni se gana XP laboral. Rotación cada 600 s LIVE de la nación por ranking `(SHA256(seasonSeed,nationId,rotationIndex,citizenId),citizenId)`; `professionId` no participa en la selección. Al ciudadano sin cupo se le muestra actividad visual sin falso progreso. Pseudónimo generado por defecto; alias de plataforma solo con opt-in explícito revocable.

## Trabajo y sueño
El ciudadano descansa exactamente al caducar `activeUntilUtc`. Un evento de plataforma retrasado no vuelve a activar una ventana del pasado más allá del límite de tolerancia. No hay muerte permanente ni barras de hambre individuales. El nombre visual es moderado; se registra ID interno separadamente del displayName público.
