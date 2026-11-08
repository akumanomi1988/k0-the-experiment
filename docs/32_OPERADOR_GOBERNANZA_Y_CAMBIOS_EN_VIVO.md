> **Regla vigente:**** OWNER controla la campaña, BROADCASTER controla exclusivamente su propia emisión, MODERATOR modera y OPERATOR opera eventos auditados. Invitaciones y revocaciones por temporada, sin permisos económicos para el broadcaster. [Especificación vigente](ESPECIFICACION.md).

# 32 — Responsabilidades del operador y gobierno del experimento

**Objetivo:** que el directo sea administrable sin controles capaces de alterar resultados arbitrariamente. No es una especificación de interfaz implementada.

## Roles de producto

- **Propietario:** configura temporada, reglas futuras, canales autorizados y condiciones de uso; no puede reescribir ledger histórico.
- **Operador:** abre/cierra escenas, programa eventos permitidos, atiende incidentes, pausa y reanuda; todas sus acciones críticas quedan auditadas.
- **Moderador de emisión:** interviene en contenido visible y nombres ofensivos; no cambia recursos, votos o victoria.
- **Observador técnico:** consulta diagnósticos sin capacidad de decidir resultados.
- **Ciudadano/espectador:** interactúa por sus comandos y votaciones; no tiene acceso a control interno ni credenciales.

## Límites de intervención

No se incluye un botón para crear oro, saltar de era, asignar ganador, alterar distribución RPS o forzar votos NPC. Las herramientas de operador autorizadas son las ya previstas: preparar/iniciar/pausar/reanudar temporada, programar evento y torneo, cancelar votación con motivo, silenciar K-0, cambiar a escena segura, detener ante emergencia y exportar auditoría.

Las correcciones extraordinarias usan un evento de compensación o una revisión de temporada y explican quién, cuándo, motivo y antes/después, en lugar de editar silenciosamente el estado. El panel debe distinguir `planeado`, `en curso`, `confirmado`, `fallido`, `cancelado` y `reintentable`.

## Libro de operación de un directo

**Antes:** comprobar fuente LIVE de cada nación, cuentas conectadas, estado de sincronización, versión de reglas, disponibilidad de voz/OBS, panel y backups. **Durante:** monitorizar latencia, cola, saturación, recursos y timers; anunciar resultados persistidos; resolver incidentes mediante escena segura. **Después:** cierre editorial, guardar resumen y revisar anomalías sin transferir saldos entre temporadas.

## Gestión de interrupciones

Una interrupción conocida de plataforma se declara `UNCERTAIN` cuando no puede demostrarse LIVE; los cronómetros se congelan aunque la audiencia crea ver vídeo. Cambiar autoridad de reloj exige transición privilegiada. El objetivo no es mantener apariencia de continuidad a cualquier coste, sino no causar perjuicio a votaciones por un fallo técnico.

## Métricas editoriales que interesa observar

Ciudadanos únicos por nación/temporada, tasa de creación a profesión, activos en últimas dos horas, ratio de completitud de misiones, tiempo hasta era, retraso en respuesta a comandos, porcentajes de abstención en votaciones, proporción de escenas informativas frente a simulación, incidentes de plataforma, eventos TTS fallidos y cambios de binding. Las métricas no sustituyen las reglas ni son instrucciones para manipular resultados.
