# 36 — Tecnologías, hitos y misión de la barra histórica

**Estado:** índice de lectura derivado de `technologies.v2.json`, `milestones.v2.json`, `eras.v2.json` y `missions.v2.json`. La barra requiere cinco hitos únicos de 20 puntos: alimentación, materiales, conocimiento, edificio representativo y misión colectiva. Las misiones diarias y semanales repetibles no otorgan puntos históricos.


## Era 1: Paleolítico

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_paleolithic` | Investigación de Paleolítico | 290 | — | paleolithic_workshop, paleolithic_research |
| `tech_paleolithic_economy` | Logística de Paleolítico | 170 | tech_paleolithic | — |
| `tech_paleolithic_defense` | Protección de Paleolítico | 170 | tech_paleolithic | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `paleolithic_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=6400 | 20 |
| `paleolithic_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 4750, 'stone': 3420} | 20 |
| `paleolithic_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=2650; requiresTechnologyId=tech_paleolithic | 20 |
| `paleolithic_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=paleolithic_civic | 20 |
| `paleolithic_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 2: Neolítico

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_neolithic` | Investigación de Neolítico | 380 | tech_paleolithic | neolithic_workshop, neolithic_research |
| `tech_neolithic_economy` | Logística de Neolítico | 220 | tech_neolithic | — |
| `tech_neolithic_defense` | Protección de Neolítico | 220 | tech_neolithic | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `neolithic_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=7000 | 20 |
| `neolithic_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 5200, 'stone': 3740} | 20 |
| `neolithic_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=2900; requiresTechnologyId=tech_neolithic | 20 |
| `neolithic_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=neolithic_civic | 20 |
| `neolithic_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 3: Edad del Cobre

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_copper` | Investigación de Edad del Cobre | 470 | tech_neolithic | copper_workshop, copper_research |
| `tech_copper_economy` | Logística de Edad del Cobre | 270 | tech_copper | — |
| `tech_copper_defense` | Protección de Edad del Cobre | 270 | tech_copper | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `copper_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=7600 | 20 |
| `copper_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 5650, 'stone': 4060} | 20 |
| `copper_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=3150; requiresTechnologyId=tech_copper | 20 |
| `copper_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=copper_civic | 20 |
| `copper_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 4: Edad del Bronce

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_bronze` | Investigación de Edad del Bronce | 560 | tech_copper | bronze_workshop, bronze_research |
| `tech_bronze_economy` | Logística de Edad del Bronce | 320 | tech_bronze | — |
| `tech_bronze_defense` | Protección de Edad del Bronce | 320 | tech_bronze | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `bronze_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=8200 | 20 |
| `bronze_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 6100, 'stone': 4380} | 20 |
| `bronze_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=3400; requiresTechnologyId=tech_bronze | 20 |
| `bronze_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=bronze_civic | 20 |
| `bronze_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 5: Edad del Hierro

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_iron` | Investigación de Edad del Hierro | 650 | tech_bronze | iron_workshop, iron_research |
| `tech_iron_economy` | Logística de Edad del Hierro | 370 | tech_iron | — |
| `tech_iron_defense` | Protección de Edad del Hierro | 370 | tech_iron | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `iron_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=8800 | 20 |
| `iron_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 6550, 'stone': 4700} | 20 |
| `iron_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=3650; requiresTechnologyId=tech_iron | 20 |
| `iron_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=iron_civic | 20 |
| `iron_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 6: Antigüedad

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_antiquity` | Investigación de Antigüedad | 740 | tech_iron | antiquity_workshop, antiquity_research |
| `tech_antiquity_economy` | Logística de Antigüedad | 420 | tech_antiquity | — |
| `tech_antiquity_defense` | Protección de Antigüedad | 420 | tech_antiquity | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `antiquity_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=9400 | 20 |
| `antiquity_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 7000, 'stone': 5020} | 20 |
| `antiquity_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=3900; requiresTechnologyId=tech_antiquity | 20 |
| `antiquity_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=antiquity_civic | 20 |
| `antiquity_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 7: Edad Media

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_medieval` | Investigación de Edad Media | 830 | tech_antiquity | medieval_workshop, medieval_research |
| `tech_medieval_economy` | Logística de Edad Media | 470 | tech_medieval | — |
| `tech_medieval_defense` | Protección de Edad Media | 470 | tech_medieval | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `medieval_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=10000 | 20 |
| `medieval_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 7450, 'stone': 5340} | 20 |
| `medieval_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=4150; requiresTechnologyId=tech_medieval | 20 |
| `medieval_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=medieval_civic | 20 |
| `medieval_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 8: Renacimiento

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_renaissance` | Investigación de Renacimiento | 920 | tech_medieval | renaissance_workshop, renaissance_research |
| `tech_renaissance_economy` | Logística de Renacimiento | 520 | tech_renaissance | — |
| `tech_renaissance_defense` | Protección de Renacimiento | 520 | tech_renaissance | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `renaissance_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=10600 | 20 |
| `renaissance_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 7900, 'stone': 5660} | 20 |
| `renaissance_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=4400; requiresTechnologyId=tech_renaissance | 20 |
| `renaissance_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=renaissance_civic | 20 |
| `renaissance_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 9: Era Industrial

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_industrial` | Investigación de Era Industrial | 1010 | tech_renaissance | industrial_workshop, industrial_research |
| `tech_industrial_economy` | Logística de Era Industrial | 570 | tech_industrial | — |
| `tech_industrial_defense` | Protección de Era Industrial | 570 | tech_industrial | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `industrial_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=11200 | 20 |
| `industrial_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 8350, 'stone': 5980} | 20 |
| `industrial_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=4650; requiresTechnologyId=tech_industrial | 20 |
| `industrial_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=industrial_civic | 20 |
| `industrial_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 10: Era Moderna

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_modern` | Investigación de Era Moderna | 1100 | tech_industrial | modern_workshop, modern_research |
| `tech_modern_economy` | Logística de Era Moderna | 620 | tech_modern | — |
| `tech_modern_defense` | Protección de Era Moderna | 620 | tech_modern | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `modern_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=11800 | 20 |
| `modern_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 8800, 'stone': 6300} | 20 |
| `modern_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=4900; requiresTechnologyId=tech_modern | 20 |
| `modern_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=modern_civic | 20 |
| `modern_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 11: Era Digital

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_digital` | Investigación de Era Digital | 1190 | tech_modern | digital_workshop, digital_research |
| `tech_digital_economy` | Logística de Era Digital | 670 | tech_digital | — |
| `tech_digital_defense` | Protección de Era Digital | 670 | tech_digital | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `digital_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=12400 | 20 |
| `digital_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 9250, 'stone': 6620} | 20 |
| `digital_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=5150; requiresTechnologyId=tech_digital | 20 |
| `digital_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=digital_civic | 20 |
| `digital_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 12: Era Espacial

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_space` | Investigación de Era Espacial | 1280 | tech_digital | space_workshop, space_research |
| `tech_space_economy` | Logística de Era Espacial | 720 | tech_space | — |
| `tech_space_defense` | Protección de Era Espacial | 720 | tech_space | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `space_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=13000 | 20 |
| `space_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 9700, 'stone': 6940} | 20 |
| `space_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=5400; requiresTechnologyId=tech_space | 20 |
| `space_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=space_civic | 20 |
| `space_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Era 13: Era Interestelar

**Tecnologías**

| Identificador | Nombre | Coste conocimiento | Requisitos | Desbloqueos |
|---|---|---:|---|---|
| `tech_interstellar` | Investigación de Era Interestelar | 1370 | tech_space | interstellar_workshop, interstellar_research |
| `tech_interstellar_economy` | Logística de Era Interestelar | 770 | tech_interstellar | — |
| `tech_interstellar_defense` | Protección de Era Interestelar | 770 | tech_interstellar | — |

**Hitos históricos**

| ID | Tipo | Objetivo | Puntos |
|---|---|---|---:|
| `interstellar_food_production` | food_production | triggerKind=food_production; repeatable=False; requiresGold=False; targetProductionUnits=13600 | 20 |
| `interstellar_materials_production` | materials_production | triggerKind=materials_production; repeatable=False; requiresGold=False; targetProductionByResourceUnits={'wood': 10150, 'stone': 7260} | 20 |
| `interstellar_knowledge_production` | knowledge_production | triggerKind=knowledge_production; repeatable=False; requiresGold=False; targetProductionUnits=5650; requiresTechnologyId=tech_interstellar | 20 |
| `interstellar_signature_basic_building_completed` | signature_basic_building_completed | triggerKind=signature_basic_building_completed; repeatable=False; requiresGold=False; targetCount=1; targetBuildingId=interstellar_civic | 20 |
| `interstellar_mission_completed` | mission_completed | triggerKind=mission_completed; repeatable=False; requiresGold=False; targetCount=1; eligibleMissionIds=['daily_supply', 'daily_materials', 'daily_discovery', 'weekly_builder', 'weekly_population'] | 20 |

## Condiciones de transición

El motor reconoce cada hito una sola vez por nación, era y clave canónica. Alcanzar 100 puntos fuera de emisión marca la era como `EraReadyPending`; no inicia ceremonia ni avanza automáticamente. La primera transición confirmada a Interestelar termina la carrera. Los catálogos deben permanecer inmutables durante la temporada: ningún ajuste de objetivo puede aplicarse retroactivamente sin migración explícita.
