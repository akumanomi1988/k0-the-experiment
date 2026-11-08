# 19 — Máquinas de estados y rechazos (contrato de dominio)

## Ciudadano
`UNREGISTERED --!join--> JOINED_NO_PROFESSION --!work(valid)--> ACTIVE --UTC expiry--> RESTING --!active or !work(same)--> ACTIVE`. `!work(different)` desde ACTIVE/RESTING rechaza `PROFESSION_LOCKED`. Ciudadanos no se borran por desconexión ni falta de alimentos. En cierre, `ARCHIVED` conserva historial y stats; siguiente temporada crea ciudadano nuevo.

## Elecciones y votaciones
`QUEUED → OPEN → RESOLVED`; `OPEN → PAUSED` si nación LIVE desaparece, `PAUSED → OPEN` cuando regresa; `OPEN/PAUSED → CANCELLED` solo por operador con motivo. **El Consejo no admite `PAYMENT_BLOCKED` por oro**: usa solo recursos ordinarios. Si una reserva de madera/piedra/conocimiento es inconsistente, la transacción falla con causa auditable y no se crea el proyecto ni se cobra parcialmente. `BALLOT` debe referenciar voto abierto, opción admisible, ciudadano de nación, input deduplicado y sello LIVE válido. En `RPS`, una primera papeleta válida es irrevocable; en `GOVERNMENT`, `PRIORITY` y `STRATEGIC` la última papeleta válida sustituye la anterior en la misma fila. `GOVERNMENT_RUNOFF` solo ofrece previamente empatados.

## Obra
`WAITING_RESOURCES → WAITING_PLOT → QUEUED → BUILDING → COMPLETED`; una obra puede saltar WAITING_PLOT si parcela disponible, pero nunca saltarse el pago. Costes se comprometen atómicamente una vez al entrar QUEUED; construcción por tramos visuales; `CANCELLED` antes de pagar libera reserva, después de pagar solo permitido por fallo grave y con compensación auditable que no deshaga trabajos anteriores.

## Cuenta monetaria
`RECEIVED → AUTHENTICATED → VERIFIED → CREDITED → REVERSED` o ramas a `REJECTED`; no se puede ir de `REJECTED` a `CREDITED` sin evento nuevo firmado y referencia a rectificación. `REVERSED` no reabre `CREDITED`. Todos los movimientos contabilizados con causa estable; una segunda notificación del mismo proveedor no crea oro.

## Sesión de directo
`OFFLINE_CONFIRMED → LIVE_CONFIRMED` requiere evidencia y TTL, `LIVE_CONFIRMED → UNCERTAIN` si señal/autoridad pierde health, `UNCERTAIN → LIVE_CONFIRMED` solo al recuperar evidencia. `UNCERTAIN → OFFLINE_CONFIRMED` tras confirmación de fin de emisión o caducidad de TTL. Manual override solo para modo SIMULATED o con autorización operador auditada; un override no valida contribuciones financieras.

## Abandono de streamer y torneos
`BROADCASTER_PRIMARY_LEFT` confirmado por OWNER → temporada `PAUSED` global sin progreso económico, político o competitivo. Plazo de siete días de reloj UTC real desde confirmación; a la expiración `ABORTED` sin ganador ni premios. OFFLINE temporal o OBS caído no son abandono. Un torneo `PAUSED` por indisponibilidad de un LIVE no consume reloj de competición y expira tras 72 horas UTC desde la pausa inicial: `CANCELLED` sin sanción; si se recupera antes, reanuda votos y tiempo restante. Las transiciones de expiración son idempotentes.

## Fin de carrera
`RUNNING` con tres naciones activas → `EraAdvanced to interstellar` → `SeasonWinnerClaim` (unique season) → `COMPLETED`; winner se registra antes de guardar Outbox. Los ticks posteriores no pueden reabrir gobierno ni extender construcción competitiva. `COMPLETED → ARCHIVED` tras cierre y snapshot; no existe `COMPLETED → RUNNING`.

## Errores canónicos
`IDENTITY_NOT_VERIFIED`, `BINDING_NOT_FOUND`, `BINDING_DUPLICATE`, `BINDING_IMMUTABLE`, `CITIZEN_NOT_JOINED`, `PROFESSION_ALREADY_ASSIGNED`, `PROFESSION_LOCKED`, `ACTIVITY_COOLDOWN`, `ACTIVITY_EXPIRED`, `SKILL_LEVEL_LOW`, `SKILL_TIER_ALREADY_CHOSEN`, `SKILL_WRONG_FAMILY`, `VOTE_NOT_OPEN`, `OUT_OF_WINDOW`, `BALLOT_INVALID_OPTION`, `RPS_ALREADY_VOTED`, `EVENT_DUPLICATE`, `EVENT_TOO_OLD`, `STREAM_NOT_CONFIRMED`, `SOURCE_UNAUTHORIZED`, `PROJECT_NOT_AFFORDABLE`, `PROJECT_THREE_OPTIONS_REQUIRED`, `HOLD_CONFLICT`, `CONTRIBUTION_NOT_VERIFIED`, `GOLD_CONVERSION_DISABLED`, `GOLD_REVERSAL_UNBACKED`, `SEASON_ALREADY_COMPLETED`, `RULESET_HASH_MISMATCH`, `MIGRATION_REQUIRED`, `WRITER_FENCING_ERROR`. La respuesta pública describe el motivo sin IDs privados ni detalles financieros.
