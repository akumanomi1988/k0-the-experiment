# 57 — Matriz de cobertura de pruebas y aceptación futura

**Estado: catálogo de pruebas que se deberán ejecutar, no resultados de test.** Evita confundir «caso escrito» con «software probado».

## Nivel 1: consistencia documental

| ID | Entrada | Resultado esperable |
|---|---|---|
| DOC-01 | Catálogos de 13 eras, 5 profesiones, 130 básicos | Referencias de ID únicas y eras existentes |
| DOC-02 | Cada `requiresTechId` | Existe tecnología anterior/coherente con su edificio; nunca hay ciclo productor de conocimiento |
| DOC-03 | 39 proyectos y 13 maravillas v2.2 | Coste `gold=0`, precio ordinario positivo, sin bonus de producción/era |
| DOC-04 | 30 habilidades | Familia válida y destino (`food`, `wood`, `mine`, `buildWork`, `knowledge`, `xp`) consistente con texto de UI |
| DOC-05 | 5 hitos por era 1–12 | Suman 100, cada trigger único, no obtienen puntos de oro |
| DOC-06 | 3 roles × 13 eras combate | 39 tipos, 3 skins sin divergencia estadística, no hay muerte permanente |
| DOC-07 | Textos de canal | Ninguno promete una sola cuenta como tres chat sources distintas |
| DOC-08 | Arte | Tamaño, pivote y acciones consistentes entre todas las facciones |

## Nivel 2: reglas y concurrencia (para implementación futura)

| ID | Escenario | Verificación de estado |
|---|---|---|
| SIM-01 | 0 espectadores, 24 NPC, 0 oro | Todas las eras 1–12 progresan vía ruta gratuita con LIVE disponible |
| SIM-02 | 10.000 espectadores, 45 sprites verticales | Todos los votos legítimos son contabilizables; productividad capada; 30 FPS no altera economía |
| SIM-03 | Tick partido por desconexión | Exactamente el porcentaje de economía correspondiente y cero segundos LIVE ficticios |
| SIM-04 | Dos años de replay lógico comprimido | Estado y hash idénticos al resultado sin replay usando mismo ruleset |
| SIM-05 | Consejo con tres opciones y reserva vectorial | Un único cargo del ganador; ningún doble cargo por retransmisión |
| SIM-06 | Evento de oro verificado duplicado y luego revertido | Una acreditación, una deuda compensatoria, saldo no negativo |
| SIM-07 | Tres naciones alcanzan final | Un único ganador persistido por orden transaccional |
| SIM-08 | RPS A=rock B=paper C=scissors | Ciclo 2 puntos por nación por ronda y sin ganador ficticio |
| SIM-09 | Guarniciones iguales en torneo automático | Tres empates y cero sanciones |
| SIM-10 | Bonus militar | Solo defensa de combate automático; no RPS ni producción |
| SIM-11 | Misiones UTC cruzan cambio de día | Una recompensa por periodo, sin duplicar hitos |
| SIM-12 | DB caída tras cobrar proyecto antes de Outbox | Restauración sin desajuste de saldo ni obra ausente |

## Nivel 3: emisiones, UX, seguridad y arte

- **UX-01** usuario novato aprende `!join`, profesión y `!active` sin texto externo; **UX-02** rechazo de voto tras cierre; **UX-03** estado `UNCERTAIN` visible; **UX-04** vertical de 360×640 con subtítulos y 45 sprites sin tapar la escena.
- **ART-01** tres siluetas distinguibles en escala 1× y monocromo; **ART-02** 10 familias reconocibles entre tres eras; **ART-03** K-0 es claramente cyborg; **ART-04** 4 orientaciones × 9 acciones por personaje según contrato; **ART-05** todas las licencias verificadas.
- **SEC-01** prompt injection en nombre/chat no altera narrador ni economía; **SEC-02** operador sin permiso no puede acreditar oro; **SEC-03** token revocado no acepta eventos; **SEC-04** persona sin consentimiento no aparece nombrada en placa; **SEC-05** público nunca recibe ID secreto ni OAuth token.
- **OPS-01** caída del proveedor congela votos y se recupera sin reinicio de etapa; **OPS-02** reinicio OBS no altera estado; **OPS-03** restore de snapshot y logs reproduce el mismo cierre.

## Criterio de firma

Un caso pasa a **PASS** solo cuando se indica entorno, versión del ruleset, commit de código (cuando exista), datos iniciales, entradas, estado final, evidencia capturada, responsable y fecha. Hasta entonces su estado es **NOT_RUN**. No usar la palabra «validado» para un documento sin evidencias.
