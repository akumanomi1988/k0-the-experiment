# Validaciones externas no sustituibles por documentación

**Prioridades confirmadas:** YouTube Live es la primera integración propuesta, **después de motor para 12 eras**. El primer piloto incluye arte terminado de 12 eras/epílogo, LLM/TTS moderado, dos layouts ES y 0 monetización hasta validación. Mercado inicial España/UE general con protección de menores; retención operativa 30 días salvo ley; coste de infraestructura objetivo ≤100 €/mes. Estos son gates que requieren evidencia real.

Estos puntos no constituyen ambigüedad del diseño sino dependencias de acceso, pruebas o hechos externos. Están **bloqueados**, no resueltos arbitrariamente:

- `LIVE-01` Autorización real de lectura y (si existe) respuesta chat por cada canal/cuenta, especialmente TikTok; evidencia y términos archivados.
- `LIVE-02` Disponibilidad y verificabilidad de aportaciones reales y reversos por tipo de evento de cada plataforma; tasas de oro por proveedor y moneda aprobadas, inicialmente inactivas.
- `LIVE-03` Compatibilidad de configuración específica con políticas de simulcasting y visualización de mensajes de otros proveedores; revisar el día de lanzamiento.
- `GRAPH-01` Render Phaser 4 dentro de OBS Browser Source en hardware y versión CEF reales a 30 FPS y calidad visual.
- `ART-01` **Assets finales para las doce eras jugables y el epílogo Interestelar**, tres facciones, ambos layouts ES, animaciones, Doctor K-0 y licencias comerciales acreditadas.
- `DATA-01` Aplicación efectiva de migraciones SQL en PostgreSQL y test de integridad y deadlocks; SQL actual referencia, no migración aprobada.
- `PERF-01` Motor autoritativo completo con cinco hitos/era y ruta sin oro: **100 semillas**, 24 NPC por nación, audiencias 0/10/100/1000/10000, profesiones sesgadas y horarios 0/1/4/24 h LIVE/día; P10/P50/P90 publicado. Perfil editorial 4 h/día: P50 de temporada **45–90 días** sin bloquear progreso gratuito; 0 h LIVE no avanza era.
- `OPS-01` Restauración probada: RPO medido, RTO medido, failover ensayado, monitorización y roles operator/owner MFA.
- `PRIVACY-01` Condiciones de privacidad, RGPD, retención de datos, impuestos y términos comerciales revisados con jurisdicción y cuenta reales.

- `RETURN-01` Evidencia del mismo broadcaster/OWNER y capabilities verificadas, retorno a T−1 ms permitido y a T exacto denegado, reintento idempotente, segundo incidente independiente y competición CANCELLED no reabierta.
- `COST-01` Factura/telemetría del entorno objetivo de tres canales y LLM/TTS dinámico: **≤100 €/mes** en infraestructura (impuestos incluidos si aplican), degradación segura al tope; arte, desarrollo y honorarios fuera de esa partida pero contabilizados por separado.
- `IDENTITY-01` Alta chat→cuenta K0 sin login, `UNIQUE(season,account)`, identidad de dos proveedores solo por enlace probado y rechazo de fusión de naciones incompatibles.

**Regla de activación:** el modo LOCAL_SIMULATION puede funcionar sin estos gates salvo pruebas básicas; `PUBLIC_LIVE` exige `LIVE-01,GRAPH-01,ART-01,DATA-01,PERF-01,OPS-01,PRIVACY-01,RETURN-01,COST-01,IDENTITY-01`, y `MONETIZED_LIVE` añade `LIVE-02, LIVE-03` y política legal aprobada. Un gate vacío bloquea la feature, nunca se sustituye por un valor ficticio.
