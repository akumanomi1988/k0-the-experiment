# Fuentes íntegras v2.5 — capítulos 33–40

 > **Archivo de preservación de contenido completo (encabezados reindentados).** No es una segunda autoridad: la [especificación maestra](../ESPECIFICACION_MAESTRA_v2.5.md) resuelve reglas sustituidas. Los enlaces relativos del texto interno pertenecen al documento original citado, por lo que debe abrirse ese archivo para navegar sus enlaces.

---

## Fuente 33 — `docs/33_NEGOCIO_MONETIZACION_PRIVACIDAD_Y_FUTURO_SAAS.md`

**Blob original:** `07fbdaf415570192a5d0fb8f7e3c66891b859d03`.

## 33 — Modelo de negocio y límites de monetización

**Estado:** especificación de producto y riesgos. No constituye un dictamen fiscal ni garantiza acceso a ingresos externos.

### Dos modelos diferentes

**Juego para el creador:** espectadores participan gratuitamente en una competición de civilizaciones; algunas aportaciones monetarias autorizadas se transforman en oro de prestigio opcional. El oro no concede ninguna ventaja de victoria, investigación ni trabajo. El operador ve la procedencia y elegibilidad de un evento, sin mostrar públicamente datos personales del pagador.

**Producto de software futuro:** el creador de CHAOS podría licenciar o suscribir el sistema a otros streamers. Esa es una línea de negocio distinta de las aportaciones de sus espectadores. El MVP se diseña para una campaña única, con opción de introducir multi-tenant y facturación de software solo después de probar retención, operación y estabilidad.

### Principios de producto

1. Experiencia competitiva completa con 0 € y 0 espectadores gracias a los NPC.
2. Compra exclusivamente de reconocimientos visuales opcionales independientes. Desde v2.2, proyectos del Consejo y maravillas son gratuitos en oro; nunca se vende poder de victoria.
3. No pedir importes individualizados ni forzar que el público pague para desbloquear épocas.
4. El valor del oro depende de capacidad verificable del proveedor; no fingir conversiones de monetización.
5. El oro no se retira a dinero real ni se transfiere entre naciones, cuentas o temporadas como moneda funcional.
6. Reversos, duplicados y eventos no elegibles no pueden acreditar oro neto dos veces.
7. La privacidad y los términos locales tienen prioridad sobre la exhibición del donante.

### Oferta comercial futura (no implementada)

Para un producto licenciable, separar: licencia mensual por campaña/creador; límite de cuentas/canales autorizados según plan; marca de creador personalizable sin alterar el balance; exportación de estadísticas; tema visual bajo contrato; soporte y recuperación; cuotas de TTS y almacenamiento; política de uso y moderación. No prometer un precio, ROI o infraestructura específica sin investigación comercial.

### Decisiones que dependen de evidencia real

Permisos LIVE por proveedor, detalle de eventos monetarios, autorización de replay de mensajes, RGPD y retención, tratamiento de menores, impuestos y devoluciones. Estas cuestiones se registran como *gates* y no como texto de «cumplimiento resuelto». El diseño general sí puede establecer los principios de minimización, retención temporal, secretos protegidos y revocación de permisos.


---

## Fuente 34 — `docs/34_CATALOGO_LEGIBLE_EDIFICIOS.md`

**Blob original:** `6e1cf3dfae5b954f8570af1ce479eac9ca721352`.

> **Enmienda v2.3:** los 10 edificios de Interestelar son fichas de epílogo visual; ningún edificio se construye después de SeasonCompleted. Las eras 1–12 siguen según catálogo. [CURRENT_SPEC](CURRENT_SPEC.md).

## 34 — Catálogo legible de los 130 edificios básicos

**Estado:** transcripción documental del catálogo canónico `data/buildings.v2.json`; los números no son recomendaciones nuevas. **Unidad:** recursos ordinarios; `gold` no se usa en la construcción básica. Cualquier ajuste exige revisar el JSON fuente y registrar la revisión.

Desde v2.2, edificios de familias taller y centro de saber exigen completar `tech_{era}` (tecnología troncal correspondiente); el resto mantiene los prerrequisitos del catálogo.

Desde v2.2, edificios de familias taller y centro de saber exigen completar `tech_{era}` (tecnología troncal correspondiente); el resto mantiene los prerrequisitos del catálogo.

Cada edificio mantiene el mismo efecto lógico para las tres facciones; solo cambia la apariencia. Los edificios de épocas anteriores no se eliminan al avanzar de era: se les aplica el modificador de edificios antiguos previsto por las reglas. La cola automática obedece a límites de capacidad, recursos y emplazamiento; no construye si la operación compromete su propia precondición de coste.


### Era 1: Paleolítico

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `paleolithic_housing` | Habitáculos — Paleolítico | wood:50, stone:10 | 170 | [2, 2] | npcCapacity=8 |
| `paleolithic_food_production` | Centro alimentario — Paleolítico | wood:70, stone:15 | 190 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `paleolithic_forestry` | Estación de biomasa — Paleolítico | wood:65, stone:15 | 170 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `paleolithic_extraction` | Cantera y mina — Paleolítico | wood:65, stone:25 | 220 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `paleolithic_workshop` | Taller de herramientas — Paleolítico | wood:100, stone:50 | 260 | [3, 2] | facilityBoostBp=300; requiere tech_paleolithic |
| `paleolithic_research` | Centro de saber — Paleolítico | wood:80, stone:50 | 250 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300; requiere tech_paleolithic |
| `paleolithic_storage` | Almacén regional — Paleolítico | wood:90, stone:65 | 180 | [3, 3] | capacityAddEachResource=1500 |
| `paleolithic_infrastructure` | Vía logística — Paleolítico | wood:30, stone:35 | 90 | [1, 2] | logisticCapacity=12 |
| `paleolithic_civic` | Ágora comunitaria — Paleolítico | wood:130, stone:80 | 320 | [3, 3] | civicCapacity=1 |
| `paleolithic_defense` | Puesto defensivo — Paleolítico | wood:100, stone:95 | 280 | [2, 2] | defensePoints=14 |

### Era 2: Neolítico

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `neolithic_housing` | Habitáculos — Neolítico | wood:59, stone:11 | 195 | [2, 2] | npcCapacity=8 |
| `neolithic_food_production` | Centro alimentario — Neolítico | wood:82, stone:17 | 218 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `neolithic_forestry` | Estación de biomasa — Neolítico | wood:76, stone:17 | 195 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `neolithic_extraction` | Cantera y mina — Neolítico | wood:76, stone:29 | 253 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `neolithic_workshop` | Taller de herramientas — Neolítico | wood:118, stone:59 | 299 | [3, 2] | facilityBoostBp=300; requiere tech_neolithic |
| `neolithic_research` | Centro de saber — Neolítico | wood:94, stone:59 | 287 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300; requiere tech_neolithic |
| `neolithic_storage` | Almacén regional — Neolítico | wood:106, stone:76 | 207 | [3, 3] | capacityAddEachResource=1850 |
| `neolithic_infrastructure` | Vía logística — Neolítico | wood:35, stone:41 | 103 | [1, 2] | logisticCapacity=12 |
| `neolithic_civic` | Ágora comunitaria — Neolítico | wood:153, stone:94 | 368 | [3, 3] | civicCapacity=1 |
| `neolithic_defense` | Puesto defensivo — Neolítico | wood:118, stone:112 | 322 | [2, 2] | defensePoints=18 |

### Era 3: Edad del Cobre

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `copper_housing` | Habitáculos — Edad del Cobre | wood:68, stone:13 | 221 | [2, 2] | npcCapacity=8 |
| `copper_food_production` | Centro alimentario — Edad del Cobre | wood:95, stone:20 | 247 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `copper_forestry` | Estación de biomasa — Edad del Cobre | wood:88, stone:20 | 221 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `copper_extraction` | Cantera y mina — Edad del Cobre | wood:88, stone:34, ore:6 | 286 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `copper_workshop` | Taller de herramientas — Edad del Cobre | wood:136, stone:68, ore:20 | 338 | [3, 2] | facilityBoostBp=300; requiere tech_copper |
| `copper_research` | Centro de saber — Edad del Cobre | wood:108, stone:68, ore:27 | 325 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300; requiere tech_copper |
| `copper_storage` | Almacén regional — Edad del Cobre | wood:122, stone:88, ore:13 | 234 | [3, 3] | capacityAddEachResource=2200 |
| `copper_infrastructure` | Vía logística — Edad del Cobre | wood:40, stone:47, ore:6 | 117 | [1, 2] | logisticCapacity=12 |
| `copper_civic` | Ágora comunitaria — Edad del Cobre | wood:176, stone:108, ore:34 | 416 | [3, 3] | civicCapacity=1 |
| `copper_defense` | Puesto defensivo — Edad del Cobre | wood:136, stone:129, ore:47 | 364 | [2, 2] | defensePoints=22 |

### Era 4: Edad del Bronce

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `bronze_housing` | Habitáculos — Edad del Bronce | wood:77, stone:15 | 246 | [2, 2] | npcCapacity=8 |
| `bronze_food_production` | Centro alimentario — Edad del Bronce | wood:107, stone:23 | 275 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `bronze_forestry` | Estación de biomasa — Edad del Bronce | wood:100, stone:23 | 246 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `bronze_extraction` | Cantera y mina — Edad del Bronce | wood:100, stone:38, ore:7 | 319 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `bronze_workshop` | Taller de herramientas — Edad del Bronce | wood:154, stone:77, ore:23 | 377 | [3, 2] | facilityBoostBp=300; requiere tech_bronze |
| `bronze_research` | Centro de saber — Edad del Bronce | wood:123, stone:77, ore:30 | 362 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300; requiere tech_bronze |
| `bronze_storage` | Almacén regional — Edad del Bronce | wood:138, stone:100, ore:15 | 261 | [3, 3] | capacityAddEachResource=2550 |
| `bronze_infrastructure` | Vía logística — Edad del Bronce | wood:46, stone:53, ore:7 | 130 | [1, 2] | logisticCapacity=12 |
| `bronze_civic` | Ágora comunitaria — Edad del Bronce | wood:200, stone:123, ore:38 | 464 | [3, 3] | civicCapacity=1 |
| `bronze_defense` | Puesto defensivo — Edad del Bronce | wood:154, stone:146, ore:53 | 406 | [2, 2] | defensePoints=26 |

### Era 5: Edad del Hierro

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `iron_housing` | Habitáculos — Edad del Hierro | wood:86, stone:17 | 272 | [2, 2] | npcCapacity=8 |
| `iron_food_production` | Centro alimentario — Edad del Hierro | wood:120, stone:25 | 304 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `iron_forestry` | Estación de biomasa — Edad del Hierro | wood:111, stone:25 | 272 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `iron_extraction` | Cantera y mina — Edad del Hierro | wood:111, stone:43, ore:8 | 352 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `iron_workshop` | Taller de herramientas — Edad del Hierro | wood:172, stone:86, ore:25 | 416 | [3, 2] | facilityBoostBp=300; requiere tech_iron |
| `iron_research` | Centro de saber — Edad del Hierro | wood:137, stone:86, ore:34 | 400 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300; requiere tech_iron |
| `iron_storage` | Almacén regional — Edad del Hierro | wood:154, stone:111, ore:17 | 288 | [3, 3] | capacityAddEachResource=2900 |
| `iron_infrastructure` | Vía logística — Edad del Hierro | wood:51, stone:60, ore:8 | 144 | [1, 2] | logisticCapacity=12 |
| `iron_civic` | Ágora comunitaria — Edad del Hierro | wood:223, stone:137, ore:43 | 512 | [3, 3] | civicCapacity=1 |
| `iron_defense` | Puesto defensivo — Edad del Hierro | wood:172, stone:163, ore:60 | 448 | [2, 2] | defensePoints=30 |

### Era 6: Antigüedad

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `antiquity_housing` | Habitáculos — Antigüedad | wood:95, stone:19 | 297 | [2, 2] | npcCapacity=8 |
| `antiquity_food_production` | Centro alimentario — Antigüedad | wood:133, stone:28 | 332 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `antiquity_forestry` | Estación de biomasa — Antigüedad | wood:123, stone:28 | 297 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `antiquity_extraction` | Cantera y mina — Antigüedad | wood:123, stone:47, ore:9 | 385 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `antiquity_workshop` | Taller de herramientas — Antigüedad | wood:190, stone:95, ore:28 | 455 | [3, 2] | facilityBoostBp=300; requiere tech_antiquity |
| `antiquity_research` | Centro de saber — Antigüedad | wood:152, stone:95, ore:38 | 437 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300; requiere tech_antiquity |
| `antiquity_storage` | Almacén regional — Antigüedad | wood:171, stone:123, ore:19 | 315 | [3, 3] | capacityAddEachResource=3250 |
| `antiquity_infrastructure` | Vía logística — Antigüedad | wood:57, stone:66, ore:9 | 157 | [1, 2] | logisticCapacity=12 |
| `antiquity_civic` | Ágora comunitaria — Antigüedad | wood:247, stone:152, ore:47 | 560 | [3, 3] | civicCapacity=1 |
| `antiquity_defense` | Puesto defensivo — Antigüedad | wood:190, stone:180, ore:66 | 490 | [2, 2] | defensePoints=34 |

### Era 7: Edad Media

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `medieval_housing` | Habitáculos — Edad Media | wood:104, stone:20 | 323 | [2, 2] | npcCapacity=8 |
| `medieval_food_production` | Centro alimentario — Edad Media | wood:145, stone:31 | 361 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `medieval_forestry` | Estación de biomasa — Edad Media | wood:135, stone:31 | 323 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `medieval_extraction` | Cantera y mina — Edad Media | wood:135, stone:52, ore:10 | 418 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `medieval_workshop` | Taller de herramientas — Edad Media | wood:208, stone:104, ore:31 | 494 | [3, 2] | facilityBoostBp=300; requiere tech_medieval |
| `medieval_research` | Centro de saber — Edad Media | wood:166, stone:104, ore:41 | 475 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300; requiere tech_medieval |
| `medieval_storage` | Almacén regional — Edad Media | wood:187, stone:135, ore:20 | 342 | [3, 3] | capacityAddEachResource=3600 |
| `medieval_infrastructure` | Vía logística — Edad Media | wood:62, stone:72, ore:10 | 171 | [1, 2] | logisticCapacity=12 |
| `medieval_civic` | Ágora comunitaria — Edad Media | wood:270, stone:166, ore:52 | 608 | [3, 3] | civicCapacity=1 |
| `medieval_defense` | Puesto defensivo — Edad Media | wood:208, stone:197, ore:72 | 532 | [2, 2] | defensePoints=38 |

### Era 8: Renacimiento

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `renaissance_housing` | Habitáculos — Renacimiento | wood:113, stone:22 | 348 | [2, 2] | npcCapacity=8 |
| `renaissance_food_production` | Centro alimentario — Renacimiento | wood:158, stone:33 | 389 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `renaissance_forestry` | Estación de biomasa — Renacimiento | wood:146, stone:33 | 348 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `renaissance_extraction` | Cantera y mina — Renacimiento | wood:146, stone:56, ore:11 | 451 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `renaissance_workshop` | Taller de herramientas — Renacimiento | wood:226, stone:113, ore:33 | 533 | [3, 2] | facilityBoostBp=300; requiere tech_renaissance |
| `renaissance_research` | Centro de saber — Renacimiento | wood:180, stone:113, ore:45 | 512 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300; requiere tech_renaissance |
| `renaissance_storage` | Almacén regional — Renacimiento | wood:203, stone:146, ore:22 | 369 | [3, 3] | capacityAddEachResource=3950 |
| `renaissance_infrastructure` | Vía logística — Renacimiento | wood:67, stone:79, ore:11 | 184 | [1, 2] | logisticCapacity=12 |
| `renaissance_civic` | Ágora comunitaria — Renacimiento | wood:293, stone:180, ore:56 | 656 | [3, 3] | civicCapacity=1 |
| `renaissance_defense` | Puesto defensivo — Renacimiento | wood:226, stone:214, ore:79 | 574 | [2, 2] | defensePoints=42 |

### Era 9: Era Industrial

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `industrial_housing` | Habitáculos — Era Industrial | wood:122, stone:24 | 374 | [2, 2] | npcCapacity=8 |
| `industrial_food_production` | Centro alimentario — Era Industrial | wood:170, stone:36 | 418 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `industrial_forestry` | Estación de biomasa — Era Industrial | wood:158, stone:36 | 374 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `industrial_extraction` | Cantera y mina — Era Industrial | wood:158, stone:61, ore:12 | 484 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `industrial_workshop` | Taller de herramientas — Era Industrial | wood:244, stone:122, ore:36 | 572 | [3, 2] | facilityBoostBp=300; requiere tech_industrial |
| `industrial_research` | Centro de saber — Era Industrial | wood:195, stone:122, ore:48 | 550 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300; requiere tech_industrial |
| `industrial_storage` | Almacén regional — Era Industrial | wood:219, stone:158, ore:24 | 396 | [3, 3] | capacityAddEachResource=4300 |
| `industrial_infrastructure` | Vía logística — Era Industrial | wood:73, stone:85, ore:12 | 198 | [1, 2] | logisticCapacity=12 |
| `industrial_civic` | Ágora comunitaria — Era Industrial | wood:317, stone:195, ore:61 | 704 | [3, 3] | civicCapacity=1 |
| `industrial_defense` | Puesto defensivo — Era Industrial | wood:244, stone:231, ore:85 | 616 | [2, 2] | defensePoints=46 |

### Era 10: Era Moderna

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `modern_housing` | Habitáculos — Era Moderna | wood:131, stone:26 | 399 | [2, 2] | npcCapacity=8 |
| `modern_food_production` | Centro alimentario — Era Moderna | wood:183, stone:39 | 446 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `modern_forestry` | Estación de biomasa — Era Moderna | wood:170, stone:39 | 399 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `modern_extraction` | Cantera y mina — Era Moderna | wood:170, stone:65, ore:13 | 517 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `modern_workshop` | Taller de herramientas — Era Moderna | wood:262, stone:131, ore:39 | 611 | [3, 2] | facilityBoostBp=300; requiere tech_modern |
| `modern_research` | Centro de saber — Era Moderna | wood:209, stone:131, ore:52 | 587 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300; requiere tech_modern |
| `modern_storage` | Almacén regional — Era Moderna | wood:235, stone:170, ore:26 | 423 | [3, 3] | capacityAddEachResource=4650 |
| `modern_infrastructure` | Vía logística — Era Moderna | wood:78, stone:91, ore:13 | 211 | [1, 2] | logisticCapacity=12 |
| `modern_civic` | Ágora comunitaria — Era Moderna | wood:340, stone:209, ore:65 | 752 | [3, 3] | civicCapacity=1 |
| `modern_defense` | Puesto defensivo — Era Moderna | wood:262, stone:248, ore:91 | 658 | [2, 2] | defensePoints=50 |

### Era 11: Era Digital

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `digital_housing` | Habitáculos — Era Digital | wood:140, stone:28 | 425 | [2, 2] | npcCapacity=8 |
| `digital_food_production` | Centro alimentario — Era Digital | wood:196, stone:42 | 475 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `digital_forestry` | Estación de biomasa — Era Digital | wood:182, stone:42 | 425 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `digital_extraction` | Cantera y mina — Era Digital | wood:182, stone:70, ore:14 | 550 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `digital_workshop` | Taller de herramientas — Era Digital | wood:280, stone:140, ore:42 | 650 | [3, 2] | facilityBoostBp=300; requiere tech_digital |
| `digital_research` | Centro de saber — Era Digital | wood:224, stone:140, ore:56 | 625 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300; requiere tech_digital |
| `digital_storage` | Almacén regional — Era Digital | wood:252, stone:182, ore:28 | 450 | [3, 3] | capacityAddEachResource=5000 |
| `digital_infrastructure` | Vía logística — Era Digital | wood:84, stone:98, ore:14 | 225 | [1, 2] | logisticCapacity=12 |
| `digital_civic` | Ágora comunitaria — Era Digital | wood:364, stone:224, ore:70 | 800 | [3, 3] | civicCapacity=1 |
| `digital_defense` | Puesto defensivo — Era Digital | wood:280, stone:266, ore:98 | 700 | [2, 2] | defensePoints=54 |

### Era 12: Era Espacial

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `space_housing` | Habitáculos — Era Espacial | wood:149, stone:29 | 450 | [2, 2] | npcCapacity=8 |
| `space_food_production` | Centro alimentario — Era Espacial | wood:208, stone:44 | 503 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `space_forestry` | Estación de biomasa — Era Espacial | wood:193, stone:44 | 450 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `space_extraction` | Cantera y mina — Era Espacial | wood:193, stone:74, ore:14 | 583 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `space_workshop` | Taller de herramientas — Era Espacial | wood:298, stone:149, ore:44 | 689 | [3, 2] | facilityBoostBp=300; requiere tech_space |
| `space_research` | Centro de saber — Era Espacial | wood:238, stone:149, ore:59 | 662 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300; requiere tech_space |
| `space_storage` | Almacén regional — Era Espacial | wood:268, stone:193, ore:29 | 477 | [3, 3] | capacityAddEachResource=5350 |
| `space_infrastructure` | Vía logística — Era Espacial | wood:89, stone:104, ore:14 | 238 | [1, 2] | logisticCapacity=12 |
| `space_civic` | Ágora comunitaria — Era Espacial | wood:387, stone:238, ore:74 | 848 | [3, 3] | civicCapacity=1 |
| `space_defense` | Puesto defensivo — Era Espacial | wood:298, stone:283, ore:104 | 742 | [2, 2] | defensePoints=58 |

### Era 13: Era Interestelar

| Identificador | Nombre | Coste | Trabajo | Huella | Efecto definido |
|---|---|---|---:|---|---|
| `interstellar_housing` | Habitáculos — Era Interestelar | wood:158, stone:31 | 476 | [2, 2] | npcCapacity=8 |
| `interstellar_food_production` | Centro alimentario — Era Interestelar | wood:221, stone:47 | 532 | [3, 2] | workerCapacityFood=8; facilityBoostBp=300 |
| `interstellar_forestry` | Estación de biomasa — Era Interestelar | wood:205, stone:47 | 476 | [2, 2] | workerCapacityWood=8; facilityBoostBp=300 |
| `interstellar_extraction` | Cantera y mina — Era Interestelar | wood:205, stone:79, ore:15 | 616 | [3, 2] | workerCapacityMine=8; facilityBoostBp=300 |
| `interstellar_workshop` | Taller de herramientas — Era Interestelar | wood:316, stone:158, ore:47 | 728 | [3, 2] | facilityBoostBp=300; requiere tech_interstellar |
| `interstellar_research` | Centro de saber — Era Interestelar | wood:252, stone:158, ore:63 | 700 | [3, 2] | workerCapacityResearch=8; facilityBoostBp=300; requiere tech_interstellar |
| `interstellar_storage` | Almacén regional — Era Interestelar | wood:284, stone:205, ore:31 | 504 | [3, 3] | capacityAddEachResource=5700 |
| `interstellar_infrastructure` | Vía logística — Era Interestelar | wood:94, stone:110, ore:15 | 252 | [1, 2] | logisticCapacity=12 |
| `interstellar_civic` | Ágora comunitaria — Era Interestelar | wood:410, stone:252, ore:79 | 896 | [3, 3] | civicCapacity=1 |
| `interstellar_defense` | Puesto defensivo — Era Interestelar | wood:316, stone:300, ore:110 | 784 | [2, 2] | defensePoints=62 |

### Reglas de lectura

El coste se descuenta una vez por construcción aprobada/planificada, antes de ejecutar la obra, con garantías transaccionales; el trabajo es una magnitud de progreso de obra y no segundos de pantalla. Las huellas son ocupación en tiles, no dimensiones de una ilustración. Las cifras proceden del catálogo y no demuestran que los valores estén equilibrados en un directo real.


---

## Fuente 35 — `docs/35_CATALOGO_LEGIBLE_PROYECTOS_Y_MARAVILLAS.md`

**Blob original:** `283a806f5642466df2de35f2887b4c08398297eb`.

> **Enmienda v2.3:** un Consejo por nación y era jugable (una terna de tres proyectos, solo uno construido). Las dos opciones descartadas no se vuelven a votar en esa era. El contenido interestelar es ceremonial, no construible tras ganar. [CURRENT_SPEC](CURRENT_SPEC.md).

## 35 — Catálogo legible: proyectos de Consejo y maravillas (v2.2)

**Derivado de `data/strategic_projects.v2.json`.** Costes expresados en recursos ordinarios; **ninguna obra exige oro**. Todas tienen efectos estéticos y de prestigio, nunca producción, ciencia o puntos históricos competitivos.

### 39 proyectos estratégicos: tres por era

| Era | Proyecto | ID | Materiales ordinarios | Trabajo | Prestigio |
|---|---|---|---|---:|---:|
| Paleolítico | Memorial de los Fundadores — Paleolítico | `paleolithic_memorial` | wood: 120, stone: 85, knowledge: 20 | 590 | 40 |
| Paleolítico | Plaza del Gran Espectáculo — Paleolítico | `paleolithic_spectacle` | wood: 120, stone: 85, knowledge: 20 | 590 | 40 |
| Paleolítico | Archivo de la Memoria — Paleolítico | `paleolithic_archive` | wood: 120, stone: 85, knowledge: 20 | 590 | 40 |
| Neolítico | Memorial de los Fundadores — Neolítico | `neolithic_memorial` | wood: 150, stone: 110, knowledge: 40 | 730 | 50 |
| Neolítico | Plaza del Gran Espectáculo — Neolítico | `neolithic_spectacle` | wood: 150, stone: 110, knowledge: 40 | 730 | 50 |
| Neolítico | Archivo de la Memoria — Neolítico | `neolithic_archive` | wood: 150, stone: 110, knowledge: 40 | 730 | 50 |
| Edad del Cobre | Memorial de los Fundadores — Edad del Cobre | `copper_memorial` | wood: 180, stone: 135, ore: 15, knowledge: 60 | 870 | 60 |
| Edad del Cobre | Plaza del Gran Espectáculo — Edad del Cobre | `copper_spectacle` | wood: 180, stone: 135, ore: 15, knowledge: 60 | 870 | 60 |
| Edad del Cobre | Archivo de la Memoria — Edad del Cobre | `copper_archive` | wood: 180, stone: 135, ore: 15, knowledge: 60 | 870 | 60 |
| Edad del Bronce | Memorial de los Fundadores — Edad del Bronce | `bronze_memorial` | wood: 210, stone: 160, ore: 30, knowledge: 80 | 1010 | 70 |
| Edad del Bronce | Plaza del Gran Espectáculo — Edad del Bronce | `bronze_spectacle` | wood: 210, stone: 160, ore: 30, knowledge: 80 | 1010 | 70 |
| Edad del Bronce | Archivo de la Memoria — Edad del Bronce | `bronze_archive` | wood: 210, stone: 160, ore: 30, knowledge: 80 | 1010 | 70 |
| Edad del Hierro | Memorial de los Fundadores — Edad del Hierro | `iron_memorial` | wood: 240, stone: 185, ore: 45, knowledge: 100 | 1150 | 80 |
| Edad del Hierro | Plaza del Gran Espectáculo — Edad del Hierro | `iron_spectacle` | wood: 240, stone: 185, ore: 45, knowledge: 100 | 1150 | 80 |
| Edad del Hierro | Archivo de la Memoria — Edad del Hierro | `iron_archive` | wood: 240, stone: 185, ore: 45, knowledge: 100 | 1150 | 80 |
| Antigüedad | Memorial de los Fundadores — Antigüedad | `antiquity_memorial` | wood: 270, stone: 210, ore: 60, knowledge: 120 | 1290 | 90 |
| Antigüedad | Plaza del Gran Espectáculo — Antigüedad | `antiquity_spectacle` | wood: 270, stone: 210, ore: 60, knowledge: 120 | 1290 | 90 |
| Antigüedad | Archivo de la Memoria — Antigüedad | `antiquity_archive` | wood: 270, stone: 210, ore: 60, knowledge: 120 | 1290 | 90 |
| Edad Media | Memorial de los Fundadores — Edad Media | `medieval_memorial` | wood: 300, stone: 235, ore: 75, knowledge: 140 | 1430 | 100 |
| Edad Media | Plaza del Gran Espectáculo — Edad Media | `medieval_spectacle` | wood: 300, stone: 235, ore: 75, knowledge: 140 | 1430 | 100 |
| Edad Media | Archivo de la Memoria — Edad Media | `medieval_archive` | wood: 300, stone: 235, ore: 75, knowledge: 140 | 1430 | 100 |
| Renacimiento | Memorial de los Fundadores — Renacimiento | `renaissance_memorial` | wood: 330, stone: 260, ore: 90, knowledge: 160 | 1570 | 110 |
| Renacimiento | Plaza del Gran Espectáculo — Renacimiento | `renaissance_spectacle` | wood: 330, stone: 260, ore: 90, knowledge: 160 | 1570 | 110 |
| Renacimiento | Archivo de la Memoria — Renacimiento | `renaissance_archive` | wood: 330, stone: 260, ore: 90, knowledge: 160 | 1570 | 110 |
| Era Industrial | Memorial de los Fundadores — Era Industrial | `industrial_memorial` | wood: 360, stone: 285, ore: 105, knowledge: 180 | 1710 | 120 |
| Era Industrial | Plaza del Gran Espectáculo — Era Industrial | `industrial_spectacle` | wood: 360, stone: 285, ore: 105, knowledge: 180 | 1710 | 120 |
| Era Industrial | Archivo de la Memoria — Era Industrial | `industrial_archive` | wood: 360, stone: 285, ore: 105, knowledge: 180 | 1710 | 120 |
| Era Moderna | Memorial de los Fundadores — Era Moderna | `modern_memorial` | wood: 390, stone: 310, ore: 120, knowledge: 200 | 1850 | 130 |
| Era Moderna | Plaza del Gran Espectáculo — Era Moderna | `modern_spectacle` | wood: 390, stone: 310, ore: 120, knowledge: 200 | 1850 | 130 |
| Era Moderna | Archivo de la Memoria — Era Moderna | `modern_archive` | wood: 390, stone: 310, ore: 120, knowledge: 200 | 1850 | 130 |
| Era Digital | Memorial de los Fundadores — Era Digital | `digital_memorial` | wood: 420, stone: 335, ore: 135, knowledge: 220 | 1990 | 140 |
| Era Digital | Plaza del Gran Espectáculo — Era Digital | `digital_spectacle` | wood: 420, stone: 335, ore: 135, knowledge: 220 | 1990 | 140 |
| Era Digital | Archivo de la Memoria — Era Digital | `digital_archive` | wood: 420, stone: 335, ore: 135, knowledge: 220 | 1990 | 140 |
| Era Espacial | Memorial de los Fundadores — Era Espacial | `space_memorial` | wood: 450, stone: 360, ore: 150, knowledge: 240 | 2130 | 150 |
| Era Espacial | Plaza del Gran Espectáculo — Era Espacial | `space_spectacle` | wood: 450, stone: 360, ore: 150, knowledge: 240 | 2130 | 150 |
| Era Espacial | Archivo de la Memoria — Era Espacial | `space_archive` | wood: 450, stone: 360, ore: 150, knowledge: 240 | 2130 | 150 |
| Era Interestelar | Memorial de los Fundadores — Era Interestelar | `interstellar_memorial` | wood: 480, stone: 385, ore: 165, knowledge: 260 | 2270 | 160 |
| Era Interestelar | Plaza del Gran Espectáculo — Era Interestelar | `interstellar_spectacle` | wood: 480, stone: 385, ore: 165, knowledge: 260 | 2270 | 160 |
| Era Interestelar | Archivo de la Memoria — Era Interestelar | `interstellar_archive` | wood: 480, stone: 385, ore: 165, knowledge: 260 | 2270 | 160 |

### 13 maravillas exclusivas

| Era | Maravilla | ID | Materiales ordinarios | Trabajo | Prestigio del primero |
|---|---|---|---|---:|---:|
| Paleolítico | El Primer Fuego | `wonder_paleolithic` | wood: 245, stone: 195, knowledge: 40 | 1500 | 300 |
| Neolítico | El Gran Semillero | `wonder_neolithic` | wood: 290, stone: 240, knowledge: 80 | 1750 | 350 |
| Edad del Cobre | La Forja del Alba | `wonder_copper` | wood: 335, stone: 285, ore: 25, knowledge: 120 | 2000 | 400 |
| Edad del Bronce | El Crisol de los Tres | `wonder_bronze` | wood: 380, stone: 330, ore: 50, knowledge: 160 | 2250 | 450 |
| Edad del Hierro | El Bastión de las Chispas | `wonder_iron` | wood: 425, stone: 375, ore: 75, knowledge: 200 | 2500 | 500 |
| Antigüedad | La Biblioteca del Primer Reino | `wonder_antiquity` | wood: 470, stone: 420, ore: 100, knowledge: 240 | 2750 | 550 |
| Edad Media | La Aguja de los Juramentos | `wonder_medieval` | wood: 515, stone: 465, ore: 125, knowledge: 280 | 3000 | 600 |
| Renacimiento | El Observatorio de las Tres Lunas | `wonder_renaissance` | wood: 560, stone: 510, ore: 150, knowledge: 320 | 3250 | 650 |
| Era Industrial | El Corazón de Vapor | `wonder_industrial` | wood: 605, stone: 555, ore: 175, knowledge: 360 | 3500 | 700 |
| Era Moderna | La Torre de Resonancia | `wonder_modern` | wood: 650, stone: 600, ore: 200, knowledge: 400 | 3750 | 750 |
| Era Digital | El Archivo de las Mil Voces | `wonder_digital` | wood: 695, stone: 645, ore: 225, knowledge: 440 | 4000 | 800 |
| Era Espacial | La Puerta del Horizonte | `wonder_space` | wood: 740, stone: 690, ore: 250, knowledge: 480 | 4250 | 850 |
| Era Interestelar | El Umbral Interestelar | `wonder_interstellar` | wood: 785, stone: 735, ore: 275, knowledge: 520 | 4500 | 900 |

### Condiciones de construcción

Tres opciones distintas de Consejo, del mismo período habilitado, no construidas, cada una individualmente costeable. Reserva vectorial por máximo componente, voto durante 600s LIVE, cargo del ganador una sola vez. Ninguna donación es requisito de convocatoria.

Las maravillas se habilitan solo mediante evento separado cuando la campaña permite la competencia y son exclusivas globalmente por primer commit de finalización. La maravilla interestelar se considera pieza de epílogo; no puede abrir otra carrera tras el cierre.

Ver `docs/44_CONSEJO_GRATUITO_PATROCINIO_Y_ECONOMIA_v2.2.md`. Este catálogo está sujeto a revisión de balance y de representación gráfica; sus números no fueron ensayados en motor .NET.


---

## Fuente 36 — `docs/36_CATALOGO_LEGIBLE_TECNOLOGIAS_E_HITOS.md`

**Blob original:** `bb9d1013b58699da5f23061633d470005a7d406e`.

## 36 — Catálogo legible de tecnologías, hitos y misiones por era (v2.3)

**Generado a partir de los datos vigentes v2.3**: tecnologías, hitos, misiones de era y eras. No es un test de jugabilidad ni sustituye al balance simulado.

Las eras 1–12 tienen 5 hitos únicos × 20 puntos, incluido el de misión específica por era; las misiones diarias/semanales NO completan el hito histórico. Cada hito de ciencia exige la tecnología troncal de su era. La 13.ª era (Interestelar) es epílogo visual y cierra la carrera al entrar, sin nuevo progreso. Proyectos y maravillas no requieren oro.

### Era 1: Paleolítico

| Tecnología | Tipo | Conocimiento | Prerrequisitos | Requerida en hito científico |
|---|---|---:|---|---|
| tech_paleolithic — Investigación de Paleolítico | MANDATORY_FREE | 290 | — | Sí |
| tech_paleolithic_economy — Logística de Paleolítico | OPTIONAL_FREE | 170 | tech_paleolithic | No |
| tech_paleolithic_defense — Protección de Paleolítico | OPTIONAL_FREE | 170 | tech_paleolithic | No |

| Hito | Condición exacta | Puntos |
|---|---|---:|
| paleolithic_food_production | 6400 comida producida | 20 |
| paleolithic_materials_production | 4750 madera y 3420 piedra producidas | 20 |
| paleolithic_knowledge_production | 2650 conocimiento producido + tech_paleolithic completada | 20 |
| paleolithic_signature_basic_building_completed | Completar paleolithic_civic | 20 |
| paleolithic_mission_completed | Completar era_mission_paleolithic | 20 |

**Misión por era:** Esfuerzo colectivo — Paleolítico; 1000 minutos-trabajador **productivos efectivos** (NPC/humanos), sin oro, una vez en esta era, independiente del calendario diario/semanal. Sus valores son candidatos de balance.

### Era 2: Neolítico

| Tecnología | Tipo | Conocimiento | Prerrequisitos | Requerida en hito científico |
|---|---|---:|---|---|
| tech_neolithic — Investigación de Neolítico | MANDATORY_FREE | 380 | tech_paleolithic | Sí |
| tech_neolithic_economy — Logística de Neolítico | OPTIONAL_FREE | 220 | tech_neolithic | No |
| tech_neolithic_defense — Protección de Neolítico | OPTIONAL_FREE | 220 | tech_neolithic | No |

| Hito | Condición exacta | Puntos |
|---|---|---:|
| neolithic_food_production | 7000 comida producida | 20 |
| neolithic_materials_production | 5200 madera y 3740 piedra producidas | 20 |
| neolithic_knowledge_production | 2900 conocimiento producido + tech_neolithic completada | 20 |
| neolithic_signature_basic_building_completed | Completar neolithic_civic | 20 |
| neolithic_mission_completed | Completar era_mission_neolithic | 20 |

**Misión por era:** Esfuerzo colectivo — Neolítico; 1200 minutos-trabajador **productivos efectivos** (NPC/humanos), sin oro, una vez en esta era, independiente del calendario diario/semanal. Sus valores son candidatos de balance.

### Era 3: Edad del Cobre

| Tecnología | Tipo | Conocimiento | Prerrequisitos | Requerida en hito científico |
|---|---|---:|---|---|
| tech_copper — Investigación de Edad del Cobre | MANDATORY_FREE | 470 | tech_neolithic | Sí |
| tech_copper_economy — Logística de Edad del Cobre | OPTIONAL_FREE | 270 | tech_copper | No |
| tech_copper_defense — Protección de Edad del Cobre | OPTIONAL_FREE | 270 | tech_copper | No |

| Hito | Condición exacta | Puntos |
|---|---|---:|
| copper_food_production | 7600 comida producida | 20 |
| copper_materials_production | 5650 madera y 4060 piedra producidas | 20 |
| copper_knowledge_production | 3150 conocimiento producido + tech_copper completada | 20 |
| copper_signature_basic_building_completed | Completar copper_civic | 20 |
| copper_mission_completed | Completar era_mission_copper | 20 |

**Misión por era:** Esfuerzo colectivo — Edad del Cobre; 1400 minutos-trabajador **productivos efectivos** (NPC/humanos), sin oro, una vez en esta era, independiente del calendario diario/semanal. Sus valores son candidatos de balance.

### Era 4: Edad del Bronce

| Tecnología | Tipo | Conocimiento | Prerrequisitos | Requerida en hito científico |
|---|---|---:|---|---|
| tech_bronze — Investigación de Edad del Bronce | MANDATORY_FREE | 560 | tech_copper | Sí |
| tech_bronze_economy — Logística de Edad del Bronce | OPTIONAL_FREE | 320 | tech_bronze | No |
| tech_bronze_defense — Protección de Edad del Bronce | OPTIONAL_FREE | 320 | tech_bronze | No |

| Hito | Condición exacta | Puntos |
|---|---|---:|
| bronze_food_production | 8200 comida producida | 20 |
| bronze_materials_production | 6100 madera y 4380 piedra producidas | 20 |
| bronze_knowledge_production | 3400 conocimiento producido + tech_bronze completada | 20 |
| bronze_signature_basic_building_completed | Completar bronze_civic | 20 |
| bronze_mission_completed | Completar era_mission_bronze | 20 |

**Misión por era:** Esfuerzo colectivo — Edad del Bronce; 1600 minutos-trabajador **productivos efectivos** (NPC/humanos), sin oro, una vez en esta era, independiente del calendario diario/semanal. Sus valores son candidatos de balance.

### Era 5: Edad del Hierro

| Tecnología | Tipo | Conocimiento | Prerrequisitos | Requerida en hito científico |
|---|---|---:|---|---|
| tech_iron — Investigación de Edad del Hierro | MANDATORY_FREE | 650 | tech_bronze | Sí |
| tech_iron_economy — Logística de Edad del Hierro | OPTIONAL_FREE | 370 | tech_iron | No |
| tech_iron_defense — Protección de Edad del Hierro | OPTIONAL_FREE | 370 | tech_iron | No |

| Hito | Condición exacta | Puntos |
|---|---|---:|
| iron_food_production | 8800 comida producida | 20 |
| iron_materials_production | 6550 madera y 4700 piedra producidas | 20 |
| iron_knowledge_production | 3650 conocimiento producido + tech_iron completada | 20 |
| iron_signature_basic_building_completed | Completar iron_civic | 20 |
| iron_mission_completed | Completar era_mission_iron | 20 |

**Misión por era:** Esfuerzo colectivo — Edad del Hierro; 1800 minutos-trabajador **productivos efectivos** (NPC/humanos), sin oro, una vez en esta era, independiente del calendario diario/semanal. Sus valores son candidatos de balance.

### Era 6: Antigüedad

| Tecnología | Tipo | Conocimiento | Prerrequisitos | Requerida en hito científico |
|---|---|---:|---|---|
| tech_antiquity — Investigación de Antigüedad | MANDATORY_FREE | 740 | tech_iron | Sí |
| tech_antiquity_economy — Logística de Antigüedad | OPTIONAL_FREE | 420 | tech_antiquity | No |
| tech_antiquity_defense — Protección de Antigüedad | OPTIONAL_FREE | 420 | tech_antiquity | No |

| Hito | Condición exacta | Puntos |
|---|---|---:|
| antiquity_food_production | 9400 comida producida | 20 |
| antiquity_materials_production | 7000 madera y 5020 piedra producidas | 20 |
| antiquity_knowledge_production | 3900 conocimiento producido + tech_antiquity completada | 20 |
| antiquity_signature_basic_building_completed | Completar antiquity_civic | 20 |
| antiquity_mission_completed | Completar era_mission_antiquity | 20 |

**Misión por era:** Esfuerzo colectivo — Antigüedad; 2000 minutos-trabajador **productivos efectivos** (NPC/humanos), sin oro, una vez en esta era, independiente del calendario diario/semanal. Sus valores son candidatos de balance.

### Era 7: Edad Media

| Tecnología | Tipo | Conocimiento | Prerrequisitos | Requerida en hito científico |
|---|---|---:|---|---|
| tech_medieval — Investigación de Edad Media | MANDATORY_FREE | 830 | tech_antiquity | Sí |
| tech_medieval_economy — Logística de Edad Media | OPTIONAL_FREE | 470 | tech_medieval | No |
| tech_medieval_defense — Protección de Edad Media | OPTIONAL_FREE | 470 | tech_medieval | No |

| Hito | Condición exacta | Puntos |
|---|---|---:|
| medieval_food_production | 10000 comida producida | 20 |
| medieval_materials_production | 7450 madera y 5340 piedra producidas | 20 |
| medieval_knowledge_production | 4150 conocimiento producido + tech_medieval completada | 20 |
| medieval_signature_basic_building_completed | Completar medieval_civic | 20 |
| medieval_mission_completed | Completar era_mission_medieval | 20 |

**Misión por era:** Esfuerzo colectivo — Edad Media; 2200 minutos-trabajador **productivos efectivos** (NPC/humanos), sin oro, una vez en esta era, independiente del calendario diario/semanal. Sus valores son candidatos de balance.

### Era 8: Renacimiento

| Tecnología | Tipo | Conocimiento | Prerrequisitos | Requerida en hito científico |
|---|---|---:|---|---|
| tech_renaissance — Investigación de Renacimiento | MANDATORY_FREE | 920 | tech_medieval | Sí |
| tech_renaissance_economy — Logística de Renacimiento | OPTIONAL_FREE | 520 | tech_renaissance | No |
| tech_renaissance_defense — Protección de Renacimiento | OPTIONAL_FREE | 520 | tech_renaissance | No |

| Hito | Condición exacta | Puntos |
|---|---|---:|
| renaissance_food_production | 10600 comida producida | 20 |
| renaissance_materials_production | 7900 madera y 5660 piedra producidas | 20 |
| renaissance_knowledge_production | 4400 conocimiento producido + tech_renaissance completada | 20 |
| renaissance_signature_basic_building_completed | Completar renaissance_civic | 20 |
| renaissance_mission_completed | Completar era_mission_renaissance | 20 |

**Misión por era:** Esfuerzo colectivo — Renacimiento; 2400 minutos-trabajador **productivos efectivos** (NPC/humanos), sin oro, una vez en esta era, independiente del calendario diario/semanal. Sus valores son candidatos de balance.

### Era 9: Era Industrial

| Tecnología | Tipo | Conocimiento | Prerrequisitos | Requerida en hito científico |
|---|---|---:|---|---|
| tech_industrial — Investigación de Era Industrial | MANDATORY_FREE | 1010 | tech_renaissance | Sí |
| tech_industrial_economy — Logística de Era Industrial | OPTIONAL_FREE | 570 | tech_industrial | No |
| tech_industrial_defense — Protección de Era Industrial | OPTIONAL_FREE | 570 | tech_industrial | No |

| Hito | Condición exacta | Puntos |
|---|---|---:|
| industrial_food_production | 11200 comida producida | 20 |
| industrial_materials_production | 8350 madera y 5980 piedra producidas | 20 |
| industrial_knowledge_production | 4650 conocimiento producido + tech_industrial completada | 20 |
| industrial_signature_basic_building_completed | Completar industrial_civic | 20 |
| industrial_mission_completed | Completar era_mission_industrial | 20 |

**Misión por era:** Esfuerzo colectivo — Era Industrial; 2600 minutos-trabajador **productivos efectivos** (NPC/humanos), sin oro, una vez en esta era, independiente del calendario diario/semanal. Sus valores son candidatos de balance.

### Era 10: Era Moderna

| Tecnología | Tipo | Conocimiento | Prerrequisitos | Requerida en hito científico |
|---|---|---:|---|---|
| tech_modern — Investigación de Era Moderna | MANDATORY_FREE | 1100 | tech_industrial | Sí |
| tech_modern_economy — Logística de Era Moderna | OPTIONAL_FREE | 620 | tech_modern | No |
| tech_modern_defense — Protección de Era Moderna | OPTIONAL_FREE | 620 | tech_modern | No |

| Hito | Condición exacta | Puntos |
|---|---|---:|
| modern_food_production | 11800 comida producida | 20 |
| modern_materials_production | 8800 madera y 6300 piedra producidas | 20 |
| modern_knowledge_production | 4900 conocimiento producido + tech_modern completada | 20 |
| modern_signature_basic_building_completed | Completar modern_civic | 20 |
| modern_mission_completed | Completar era_mission_modern | 20 |

**Misión por era:** Esfuerzo colectivo — Era Moderna; 2800 minutos-trabajador **productivos efectivos** (NPC/humanos), sin oro, una vez en esta era, independiente del calendario diario/semanal. Sus valores son candidatos de balance.

### Era 11: Era Digital

| Tecnología | Tipo | Conocimiento | Prerrequisitos | Requerida en hito científico |
|---|---|---:|---|---|
| tech_digital — Investigación de Era Digital | MANDATORY_FREE | 1190 | tech_modern | Sí |
| tech_digital_economy — Logística de Era Digital | OPTIONAL_FREE | 670 | tech_digital | No |
| tech_digital_defense — Protección de Era Digital | OPTIONAL_FREE | 670 | tech_digital | No |

| Hito | Condición exacta | Puntos |
|---|---|---:|
| digital_food_production | 12400 comida producida | 20 |
| digital_materials_production | 9250 madera y 6620 piedra producidas | 20 |
| digital_knowledge_production | 5150 conocimiento producido + tech_digital completada | 20 |
| digital_signature_basic_building_completed | Completar digital_civic | 20 |
| digital_mission_completed | Completar era_mission_digital | 20 |

**Misión por era:** Esfuerzo colectivo — Era Digital; 3000 minutos-trabajador **productivos efectivos** (NPC/humanos), sin oro, una vez en esta era, independiente del calendario diario/semanal. Sus valores son candidatos de balance.

### Era 12: Era Espacial

| Tecnología | Tipo | Conocimiento | Prerrequisitos | Requerida en hito científico |
|---|---|---:|---|---|
| tech_space — Investigación de Era Espacial | MANDATORY_FREE | 1280 | tech_digital | Sí |
| tech_space_economy — Logística de Era Espacial | OPTIONAL_FREE | 720 | tech_space | No |
| tech_space_defense — Protección de Era Espacial | OPTIONAL_FREE | 720 | tech_space | No |

| Hito | Condición exacta | Puntos |
|---|---|---:|
| space_food_production | 13000 comida producida | 20 |
| space_materials_production | 9700 madera y 6940 piedra producidas | 20 |
| space_knowledge_production | 5400 conocimiento producido + tech_space completada | 20 |
| space_signature_basic_building_completed | Completar space_civic | 20 |
| space_mission_completed | Completar era_mission_space | 20 |

**Misión por era:** Esfuerzo colectivo — Era Espacial; 3200 minutos-trabajador **productivos efectivos** (NPC/humanos), sin oro, una vez en esta era, independiente del calendario diario/semanal. Sus valores son candidatos de balance.

### Era 13: Era Interestelar — EPÍLOGO

| Tecnología | Tipo | Conocimiento | Prerrequisitos | Requerida en hito científico |
|---|---|---:|---|---|
| tech_interstellar — Investigación de Era Interestelar | MANDATORY_FREE | 1370 | tech_space | No |
| tech_interstellar_economy — Logística de Era Interestelar | OPTIONAL_FREE | 770 | tech_interstellar | No |
| tech_interstellar_defense — Protección de Era Interestelar | OPTIONAL_FREE | 770 | tech_interstellar | No |

| Hito | Condición exacta | Puntos |
|---|---|---:|
| interstellar_food_production | 13600 comida producida | 20 |
| interstellar_materials_production | 10150 madera y 7260 piedra producidas | 20 |
| interstellar_knowledge_production | 5650 conocimiento producido + tech_interstellar completada | 20 |
| interstellar_signature_basic_building_completed | Completar interstellar_civic | 20 |
| interstellar_mission_completed | Epílogo, no exigido para ganar | 20 |

**Atención:** este contenido solo sirve como ficha histórica/artística. No se abre investigación, misión, construcción, Consejo o voto después de SeasonCompleted.

### Integridad del catálogo

El runtime debe usar IDs y condiciones de `data/*.json` y pruebas de `tools/validate_design_catalogs.py`. Este archivo es una vista legible, no autoridad de cálculos. Enmiendas y orden de eventos: [CURRENT_SPEC](CURRENT_SPEC.md), [doc 64](64_RELOJES_EVENTOS_Y_CONTRATOS_v2.3.md).


---

## Fuente 37 — `docs/37_CATALOGO_LEGIBLE_PROFESIONES_HABILIDADES_GOBIERNOS.md`

**Blob original:** `2acd9bee107228dbf7a151d02e9697592b7b11a3`.

## 37 — Profesiones, habilidades y gobiernos: catálogo legible

**Estado:** derivación de las definiciones canónicas `data/professions.v2.json`, `data/skills.v2.json`, `data/governments.v2.json` y `data/eras.v2.json`. La profesión se elige una única vez por temporada; el oficio cambia su denominación estética según la era, sin cambiar de familia funcional.

### Etiquetas de oficio por época

| Era | Alimentación | Biomasa | Minería | Construcción | Investigación |
|---|---|---|---|---|---|
| Paleolítico | Cazador | Recolector | Tallador | Constructor tribal | Explorador |
| Neolítico | Agricultor | Leñador | Cantero | Albañil | Sabio |
| Edad del Cobre | Agricultor | Silvicultor | Minero | Artesano | Estudioso |
| Edad del Bronce | Granjero | Leñador | Fundidor | Maestro de obras | Escriba |
| Edad del Hierro | Campesino | Forestal | Herrero | Constructor | Investigador |
| Antigüedad | Labrador | Carpintero forestal | Minero | Arquitecto | Filósofo |
| Edad Media | Agricultor | Leñador | Minero | Maestro de gremio | Erudito |
| Renacimiento | Agrónomo | Guardabosques | Metalurgista | Ingeniero | Inventor |
| Era Industrial | Operario agrícola | Maderero | Minero industrial | Ingeniero industrial | Científico |
| Era Moderna | Técnico agrícola | Técnico forestal | Operario de extracción | Técnico de obras | Investigador |
| Era Digital | Tecnólogo alimentario | Especialista en biomasa | Operador extractivo | Ingeniero de automatización | Analista |
| Era Espacial | Técnico de suministros | Cultivador espacial | Extractor planetario | Ingeniero orbital | Astrocientífico |
| Era Interestelar | Sintetizador | Ingeniero de biomasa | Extractor estelar | Arquitecto interestelar | Investigador cuántico |

### Habilidades (30)

| Profesión | Nivel requerido | Identificador | Nombre | Efecto exacto |
|---|---:|---|---|---|
| food | 3 | `expert_gathering` | Expert Gathering | target=food; additiveBp=400; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| food | 3 | `food_hauling` | Food Hauling | target=food; additiveBp=250; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| food | 7 | `efficient_production` | Efficient Production | target=food; additiveBp=500; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| food | 7 | `rationing` | Rationing | target=food; additiveBp=350; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| food | 12 | `master_foodcraft` | Master Foodcraft | target=food; additiveBp=600; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| food | 12 | `preservation` | Preservation | target=food; additiveBp=300; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| wood | 3 | `precise_cut` | Precise Cut | target=wood; additiveBp=400; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| wood | 3 | `forest_walker` | Forest Walker | target=wood; additiveBp=250; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| wood | 7 | `optimized_tools` | Optimized Tools | target=wood; additiveBp=500; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| wood | 7 | `full_utilization` | Full Utilization | target=wood; additiveBp=450; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| wood | 12 | `master_forester` | Master Forester | target=wood; additiveBp=600; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| wood | 12 | `reuse` | Reuse | target=wood; additiveBp=350; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| mine | 3 | `expert_stonecutter` | Expert Stonecutter | target=stone; additiveBp=400; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| mine | 3 | `prospector` | Prospector | target=ore; additiveBp=450; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| mine | 7 | `efficient_excavation` | Efficient Excavation | target=mine; additiveBp=500; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| mine | 7 | `heavy_load` | Heavy Load | target=mine; additiveBp=250; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| mine | 12 | `master_stonecutter` | Master Stonecutter | target=stone; additiveBp=600; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| mine | 12 | `master_miner` | Master Miner | target=ore; additiveBp=600; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| build | 3 | `fast_hands` | Fast Hands | target=buildWork; additiveBp=400; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| build | 3 | `site_organizer` | Site Organizer | target=buildWork; additiveBp=300; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| build | 7 | `expert_builder` | Expert Builder | target=buildWork; additiveBp=450; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| build | 7 | `restorer` | Restorer | target=buildWork; additiveBp=300; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| build | 12 | `master_architect` | Master Architect | target=buildWork; additiveBp=600; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| build | 12 | `civil_engineer` | Civil Engineer | target=buildWork; additiveBp=450; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| research | 3 | `curiosity` | Curiosity | target=knowledge; additiveBp=400; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| research | 3 | `methodical_study` | Methodical Study | target=knowledge; additiveBp=350; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| research | 7 | `applied_research` | Applied Research | target=knowledge; additiveBp=500; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| research | 7 | `documentation` | Documentation | target=xp; additiveBp=400; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| research | 12 | `grand_researcher` | Grand Researcher | target=knowledge; additiveBp=600; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |
| research | 12 | `innovator` | Innovator | target=knowledge; additiveBp=500; scope=INDIVIDUAL_PER_PERSON; applicableOnlyToChosenProfession=True |

### Candidaturas de gobierno (9)

| Nación | Arquetipo | Personaje | Bonificación | Campo de aplicación |
|---|---|---|---:|---|
| micelios | economy | Morga | 300 | food_wood_stone_ore |
| micelios | military | Bruk | 500 | automated_tournament_defense |
| micelios | science | Espora | 300 | knowledge |
| runicos | economy | Dorrik | 300 | food_wood_stone_ore |
| runicos | military | Kraag | 500 | automated_tournament_defense |
| runicos | science | Zyn | 300 | knowledge |
| ferrinos | economy | Nera | 300 | food_wood_stone_ore |
| ferrinos | military | Rokka | 500 | automated_tournament_defense |
| ferrinos | science | Neri | 300 | knowledge |

### Límites

Las habilidades aplican al ciudadano que las obtuvo, salvo indicación contraria explícita en el catálogo; el mismo bono no puede multiplicarse ilimitadamente por número de jugadores. Los gobernantes no sustituyen decisiones del Consejo ni tienen poder para conceder oro, alterar el ganador o saltar hitos. Los valores reflejan el catálogo de diseño, pendientes de calibración tras un motor funcional.


---

## Fuente 38 — `docs/38_PRUEBAS_ACEPTACION_EN_LENGUAJE_NATURAL.md`

**Blob original:** `1d22dffd7ff0df88886c23a19bca1eac745b0b6b`.

## 38 — Casos de aceptación funcional sin código

**Propósito:** convertir reglas en ejemplos observables para el día que se implemente el motor. No hay scripts, frameworks ni código fuente. Los escenarios usan valores establecidos en v2.0; su ejecución futura será un trabajo diferente.

### Ciudadanía y actividad

**Caso C-01:** una cuenta nueva envía `!join` dos veces debido a reintento del proveedor. Resultado esperado: un ciudadano, una identidad y ningún recurso extraordinario. **C-02:** el ciudadano elige `food`; cuando intenta `mine` en la misma temporada, el sistema conserva `food` y explica la restricción. **C-03:** una acción válida renueva actividad por dos horas reales tras cooldown; el chat casual no prolonga actividad.

### Economía y progreso

**E-01:** una nación tiene 24 NPC iniciales y ningún humano, ninguna aportación y ningún oro. La economía produce y consume según tablas; existe una ruta de avance gratuita sin desbloqueos de pago. **E-02:** cuando se llena madera, la producción no produce inventario por encima de capacidad; los restos y contadores de redondeo se conservan según regla. **E-03:** durante tiempo fuera de emisión la economía utiliza el multiplicador reducido; una votación abierta no consume minutos LIVE. **E-04:** un hito ya cobrado no concede de nuevo 20 puntos al cumplir objetivo repetido.

### Eras y gobierno

**H-01:** cinco hitos distintos de 20 puntos alcanzan 100; la nación sin LIVE confirmado queda preparada pero no pasa de era. **H-02:** al confirmar LIVE la nación avanza exactamente una vez; cambio de nombre de oficio no reasigna la profesión. **G-01:** elección de tres candidatos dura una hora de emisión; el empate activa la segunda vuelta durante tres minutos LIVE. **G-02:** un gobernador militar aplica solo el bono definido, sin capacidad de ordenar ataques automáticos.

### Consejo y oro

**V-01:** el Consejo tiene tres opciones elegibles, con recursos disponibles para cada una por separado, pero no para la suma de las tres. Se reserva el vector máximo previsto; al cierre se cobra solo el proyecto ganador. **V-02:** dos cierres concurrentes no pueden cobrar el mismo voto/obra ni dejar inventarios negativos. **O-01:** un proveedor reintenta un evento monetario idéntico: una sola acreditación. **O-02:** la aportación es revocada tras gastar oro; aparece deuda compensatoria sin saldo negativo en el wallet.

### Torneo

**T-01:** los tres equipos eligen rock, paper, scissors respectivamente; cada equipo gana y pierde una pareja, total dos puntos: no existe un ganador ficticio de esa ronda. **T-02:** una nación no recibe votos y juega PASS. **T-03:** tras dos rondas extra continúa el empate primero: se anuncian ganadores compartidos sin penalización. **T-04:** la penalización territorial consume exactamente 30 minutos de LIVE y se pausa durante desconexión.

### Integraciones y presentación

**I-01:** tres canales del mismo proveedor asignados a tres naciones no mezclan mensajes. **I-02:** retirar una capacidad de monetización no desactiva chat permitido. **I-03:** reconectar OBS no modifica inventarios. **I-04:** ocultar un avatar por LOD no desactiva la producción de su ciudadano. **I-05:** la escena vertical y la horizontal muestran idéntico ganador y era.

### Integridad y final

**F-01:** dos naciones alcanzan Interestelar en eventos casi simultáneos; la adjudicación se resuelve por secuencia de commit global, persistida. **F-02:** una vez completada la temporada no se aceptan nuevas operaciones competitivas ni se arrastran recursos. **F-03:** restaurar un snapshot y reproducir entradas ordenadas produce el mismo checksum del estado lógico con el mismo ruleset y versión de motor.

### Criterio formal

Para declarar completado cada escenario en implementación futura habrá que registrar condiciones iniciales, eventos, sello de tiempo, estado final, asientos de ledger, salida HUD y evidencia observada. **Estar escrito aquí no significa que se haya probado en software.**


---

## Fuente 39 — `docs/39_REGISTRO_DE_CIERRE_Y_VALIDACIONES_EXTERNAS.md`

**Blob original:** `b979be0e95f0a53261071bd2e3147e86cd3f2b0d`.

## 39 — Registro de cierre documental y validaciones externas

**Estado:** registro histórico v2.1 ampliado por `docs/41` y `docs/60` de v2.2; diseño, no validación de implementación. La definición es suficientemente detallada para orientar implementación, pero no se declara producto al 100 % probado. Se conserva distinción entre decisiones cerradas, supuestos de balance y hechos externos.

### Diseñado y expresado documentalmente

Tres naciones independientes de plataforma; 92 respuestas históricas preservadas; cinco profesiones; 13 eras; condición de victoria; rutas gratuitas NPC; recursos, tasas y almacenes; gobiernos, elecciones y prioridades; Consejo estratégico; RPS triangular; contribuciones y oro limitado a prestigio; narrador neutral; estados LIVE y de economía; contratos y esquema relacional propuestos; catálogo numérico de edificios, proyectos, maravillas, tecnologías, hitos, misiones y habilidades; estilo pixel art y escenas OBS; mecanismos de operador y recuperación.

### No resuelto por escribir más páginas

**Integración:** derechos y capacidad efectiva de APIs LIVE para cada cuenta, recuperación real de mensajes, eventos monetarios auditables y condiciones del proveedor. **Arte:** elección y aprobación de sprites, retratos, animación final de K-0 y voces originales. **Implementación:** migraciones SQL ejecutadas, reproducibilidad del motor .NET, rendimiento en OBS, sincronización real y restauración probada. **Comercial:** términos de licencia, pricing y contratación de futuros creadores. **Legal:** cumplimiento y obligaciones específicas de jurisdicción.

### Hipótesis numéricas, no certezas

Las tasas, costes, puntos y límites definidos por `ruleset.v2.json` son un diseño candidato. No han pasado una batería de temporadas reales. Deben calibrarse **antes de abrir una temporada pública** con evidencia cuantitativa y datos de audiencia reales; una vez abierta, los valores permanecen congelados para evitar una carrera injusta.

### Limitaciones del sistema de tres naciones

El esquema de canales admite tres cuentas del mismo proveedor, distintas plataformas y canales secundarios por nación. **No** admite sin revisión una sola cuenta de chat que controle simultáneamente las tres naciones: no está especificado el lenguaje de asignación de nación para cada acción. Si el modelo comercial requiriese «un único LIVE compartido por las tres», eso sería una ampliación de producto con nuevas reglas y no debería inferirse desde la configuración actual.

### Criterios mínimos para fase de desarrollo

- Aprobación de los textos que reformulan decisiones previas (documento 18).
- Identidad visual final de las tres especies y del presentador, suficiente para un prototipo artístico.
- Declaración de proveedor/cuentas que se probarán primero.
- Confirmación legal y técnica de las capacidades de chat previstas.
- Revisión de hipótesis de balance con simulación real antes de prometer calendarios de temporada.

El diseño puede congelarse como baseline de desarrollo sin afirmar que esos hechos externos han ocurrido.


---

## Fuente 40 — `docs/40_DESCRIPCION_NO_FUNCIONAL_Y_CALIDAD.md`

**Blob original:** `21f8fea38fe207eed4a86dd013d3cbe55e22ea6b`.

## 40 — Requisitos no funcionales y calidad de producto

**Estado:** criterios de diseño y validación futura. No se incluyen Docker, YAML de CI/CD ni scripts. Los números de rendimiento de `docs/22` son objetivos de diseño, no resultados de medición.

### Invariantes de experiencia

Una transición de era debe ser comprensible desde una escena vertical; una desconexión debe señalarse; una elección no puede completarse sin sus segundos LIVE correspondientes; las diferencias de hardware gráfico no afectan economía ni ganador; toda respuesta de comando puede presentarse sin permiso de escribir en chat externo.

### Integridad

Las identidades se basan en IDs de proveedor estables, las aportaciones en eventos verificados y el estado económico en operaciones autoritativas. No existe rollback parcial que descuente materiales y deje de crear una construcción. Un restart de OBS no tiene consecuencias económicas. Los secretos de canal no aparecen en el overlay ni en exportaciones de auditoría pública.

### Escalabilidad

Aumentar de 100 a 10.000 ciudadanos no puede exigir dibujar 10.000 sprites simultáneamente. Se agregan capacidades productivas por cohortes matemáticamente equivalentes. El renderer está desacoplado del simulador y puede reducir partículas y densidad de personajes sin disminuir producción.

### Persistencia

Snapshots, Inbox, Outbox, ledger y reglas versionadas se consideran responsabilidades conceptuales necesarias; SQL es diseño del esquema, no evidencia de migración. Las copias de seguridad deben ser restaurables en entorno de pruebas antes de monetizar. RPO y RTO definitivos deben medirse y documentarse tras desplegar infraestructura real.

### Privacidad y moderación

Minimizar identificadores y datos, usar pseudonimización en exportaciones, diferenciar público/operador, respetar bloqueo de exhibición de nombres ofensivos, atender revocaciones y conservar auditoría necesaria con política de retención específica aprobada. La elección de proveedor y jurisdicción condicionan requisitos legales; no inventar una política RGPD universal en abstracto.

### Compatibilidad

Escenas visuales de 360×640 y 640×360, render objetivo 30 FPS, escalado entero donde el formato final lo permita y modo subtitulado sin audio. Ninguna autorización de TikTok/Twitch/YouTube se presupone por el mero hecho de soportar adaptadores conceptuales.

### Gestión de calidad

Antes de aceptar una temporada pública: ensayo completo de historia, pruebas de estrés, recuperación, seguridad, inclusión de HUD, moderación, corrección de elecciones y monetización verificada si se activa. Los requisitos no funcionales se aprueban con evidencia y no con una declaración de diseño.

