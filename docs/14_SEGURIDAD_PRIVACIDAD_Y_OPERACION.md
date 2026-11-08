> **Documento de detalle.** La fuente normativa vigente es [ESPECIFICACION_MAESTRA.md](../ESPECIFICACION_MAESTRA.md). Este capítulo no prevalece ante una regla corregida en la especificación; versiones anteriores en Git.

# 14 — Seguridad, privacidad, infraestructura y continuidad

## Amenazas críticas
Eventos simulados como aportaciones, abuso de chat, replay, doble aprobación de obras, cambio no autorizado de binding, spoofing de canal, privilegios de operador, inyección por displayName a TTS/LLM y pérdida del estado. Todos los accesos externos pasan por validación, autenticidad del proveedor y `sourceKey` deduplicado. Secrets en un gestor de secretos o variables inyectadas por orquestación, nunca en JSON distribuido. Tiempos UTC; firewall DB no expuesta; TLS en endpoint público; MFA para operador; red mínima entre procesos.

## Acceso y segregación
Roles `viewer`, `moderator` (silenciar nombres), `operator` (iniciar/detener/votar eventos autorizados), `owner` (modificar bindings y tasas de monetización), `auditor` (solo lectura ledger). Todas las acciones mutadoras con `idempotencyKey`, actor, razón y registro append-only. `Contributions` solo pasa a Verified desde adaptador con `capability` habilitada y prueba de autoridad; la UI del operador NO dispone de botón para crear oro real. En simulación puede inyectarse oro demo a un ledger namespace separado que jamás se fusiona con producción.

## Retención
Minimizar PII: hash estable de ID del proveedor para correlación y token cifrado en vault; displayName moderado no es clave. Retención propuesta: eventos de chat sin relevancia 7 días, raw validado de comandos 30 días, métricas agregadas 13 meses, ledger y eventos financieros según obligación legal aplicable (no fijar periodo sin asesoría jurisdiccional). Permitir anonimizar nombres públicos sin reescribir ledger. Publicación de política de privacidad y procedimiento de eliminación antes del primer directo real.

## Hosting y backups
Docker Compose local con PostgreSQL. Inicialmente una VM única EU con servicios separados por contenedor, volumen PostgreSQL y backups diarios cifrados fuera del host; respaldos de WAL/PITR si la pérdida tolerable obliga. RPO objetivo de diseño 15 min y RTO 2h, NO garantías demostradas. Cada 30 días realizar restauración simulada contra DB vacía y comparar cuentas, ledger y checksum de snapshot. Cualquier test fallido bloquea monetización. Nunca compartir tokens OBS o OAuth en repositorio.

## Despliegue y rollback
Pipeline: lint/json-schema → tests de contenido → tests del motor → migración en staging → snapshot DB → arranque versión con contrato compatible → health gates → rollout controlado. No migrar esquema mientras se procesa inbox sin compatibilidad. Para cambios de `rulesetHash` detener nueva temporada y crear ruleset nuevo; las temporadas RUNNING quedan fijadas. Feature flags por canal no deben alterar las reglas ya congeladas de una nación.

## Costes e IA
Presupuestos sólo estimables tras benchmark de CPU, nº de canales/eventos y TTS. Cada mensaje narrado puede salir por plantilla offline; LLM es opcional con límite de gasto diario y fallo seguro. La infraestructura no debe quedar funcionando 24/7 sin supervisión del operador durante la fase de pruebas monetizadas.
