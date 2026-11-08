> **Regla vigente:** los 10 edificios de Interestelar son fichas de epílogo visual; ningún edificio se construye después de SeasonCompleted. Las eras 1–12 siguen según catálogo. [especificación vigente](ESPECIFICACION.md).

# 34 — Catálogo legible de los 130 edificios básicos

**Estado:** transcripción documental del catálogo canónico `data/buildings.json`; los números no son recomendaciones nuevas. **Unidad:** recursos ordinarios; `gold` no se usa en la construcción básica. Cualquier ajuste exige revisar el JSON fuente y registrar la revisión.

Desde v2.2, edificios de familias taller y centro de saber exigen completar `tech_{era}` (tecnología troncal correspondiente); el resto mantiene los prerrequisitos del catálogo.

Desde v2.2, edificios de familias taller y centro de saber exigen completar `tech_{era}` (tecnología troncal correspondiente); el resto mantiene los prerrequisitos del catálogo.

Cada edificio mantiene el mismo efecto lógico para las tres facciones; solo cambia la apariencia. Los edificios de épocas anteriores no se eliminan al avanzar de era: se les aplica el modificador de edificios antiguos previsto por las reglas. La cola automática obedece a límites de capacidad, recursos y emplazamiento; no construye si la operación compromete su propia precondición de coste.


## Era 1: Paleolítico

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

## Era 2: Neolítico

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

## Era 3: Edad del Cobre

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

## Era 4: Edad del Bronce

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

## Era 5: Edad del Hierro

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

## Era 6: Antigüedad

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

## Era 7: Edad Media

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

## Era 8: Renacimiento

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

## Era 9: Era Industrial

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

## Era 10: Era Moderna

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

## Era 11: Era Digital

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

## Era 12: Era Espacial

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

## Era 13: Era Interestelar

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

## Reglas de lectura

El coste se descuenta una vez por construcción aprobada/planificada, antes de ejecutar la obra, con garantías transaccionales; el trabajo es una magnitud de progreso de obra y no segundos de pantalla. Las huellas son ocupación en tiles, no dimensiones de una ilustración. Las cifras proceden del catálogo y no demuestran que los valores estén equilibrados en un directo real.
