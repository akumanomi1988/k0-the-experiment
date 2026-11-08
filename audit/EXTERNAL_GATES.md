# Validaciones externas no sustituibles por documentación

**Prioridades confirmadas:** YouTube Live es la primera integración propuesta, **después de motor para 12 eras**. El primer piloto incluye arte terminado de 12 eras/epílogo, LLM/TTS moderado, dos layouts ES y 0 monetización hasta validación. Mercado inicial España/UE general con protección de menores; retención operativa 30 días salvo ley; coste de infraestructura objetivo ≤100 €/mes. Estos son gates que requieren evidencia real.

Estos puntos no constituyen ambigüedad del diseño sino dependencias de acceso, pruebas o hechos externos. Están **bloqueados**, no resueltos arbitrariamente:

- `LIVE-01` Autorización real de lectura y (si existe) respuesta chat por cada canal/cuenta, especialmente TikTok; evidencia y términos archivados.
- `LIVE-02` Disponibilidad y verificabilidad de aportaciones reales y reversos por tipo de evento de cada plataforma; tasas de oro por proveedor y moneda aprobadas, inicialmente inactivas.
- `LIVE-03` Compatibilidad de configuración específica con políticas de simulcasting y visualización de mensajes de otros proveedores; revisar el día de lanzamiento.
- `GRAPH-01` Render Phaser 4 dentro de OBS Browser Source en hardware y versión CEF reales a 30 FPS y calidad visual.
- `ART-01` Revisión visual final de sprites Micelios, Rúnicos, Ferrinos, 13 eras, fondos y Doctor K-0, licencias de assets.
- `DATA-01` Aplicación efectiva de migraciones SQL en PostgreSQL y test de integridad y deadlocks; SQL actual referencia, no migración aprobada.
- `PERF-01` Simulación full season 24 NPC y 10/100/1000/10000 humanos por nación con >7 días offline y recursos saturados; calibrar progresión 2,5 días/era.
- `OPS-01` Restauración probada: RPO medido, RTO medido, failover ensayado, monitorización y roles operator/owner MFA.
- `PRIVACY-01` Condiciones de privacidad, RGPD, retención de datos, impuestos y términos comerciales revisados con jurisdicción y cuenta reales.

**Regla de activación:** el modo LOCAL_SIMULATION puede funcionar sin estos gates salvo pruebas básicas; `PUBLIC_LIVE` exige `LIVE-01,GRAPH-01,DATA-01,PERF-01,OPS-01,PRIVACY-01`, y `MONETIZED_LIVE` añade `LIVE-02, LIVE-03` y política legal aprobada. Un gate vacío bloquea la feature, nunca se sustituye por un valor ficticio.
