# Extensiones conceptuales de contratos v2.2 — Ejército y patrocinios

**No hay endpoints operativos.** Estos diseños deberán incorporarse a una nueva versión semántica del contrato OpenAPI y SignalR antes del desarrollo; `openapi.v2.yaml` continúa como baseline v2.0 histórico. No debemos llamar a estas rutas «disponibles».

## Lectura pública de guarnición

`GET /api/v2/public/seasons/{seasonId}/nations/{nationId}/garrison` (propuesto). Solo campos públicos: `{seasonId,nationId,eraIndex,aggregateUnitCount,roleCounts:[{role,count}],combatReadiness,generatedAtUtc,sequence}`. No exponer identidades ni patrón de gasto de donantes. La respuesta es proyección eventual y puede requerir snapshot ante cursor vencido.

## Lectura de batalla

`GET /api/v2/public/seasons/{seasonId}/battles/{battleId}` (propuesto). Salida `{battleId,state,startedAtUtc,resolvedAtUtc,participants:[{nationId,strength,points}],jointWinners,penalties:[{nationId,kind,amount}],eventSequence}`. Mientras evento está `RUNNING`, omitir resultados no persistidos y cualquier dato que el director haya marcado oculto para preservar suspense sin mentir sobre estado.

## Compra de reconocimiento cosmético

No crear endpoint público para convertir dinero real en oro. Atribución de aportaciones entra exclusivamente por adaptador autenticado y ledger. Tras crédito verificado, el ciudadano puede adquirir un artículo simbólico conforme a la política del proveedor. Comando de compra no está definido entre los ocho comandos de v2, por tanto **se mantiene como funcionalidad futura sin activación** hasta establecer interfaz autorizada y consentimiento. La moderación del operador podría gestionar estado aprobado/rechazado por ID sin alterar saldos directamente.

## Eventos SignalR propuestos

`garrison.changed` `{nationId,sequence,roleCounts}`; `battle.scheduled` `{battleId,sourceNationIds}`; `battle.result` `{battleId,sequence,resultDigest,participants}`; `cosmetic.acknowledgement` `{nationId,itemId,moderatedText}`. Versionar esquemas; usar Inbox/Outbox; ninguna animación o narración crea efectos autoritativos.

## Gate de contrato

Definir formalmente seguridad, scopes, errores, tipos, límites, idempotency y JSON Schema para los mensajes antes de implementar. Actualizar `contracts/openapi.v2.yaml` a la versión acordada y `contracts/signalr.v2.md` o sustituirlos por contratos v3 versionados. La presencia de este anexo **no acredita consistencia con SQL en PostgreSQL**.
