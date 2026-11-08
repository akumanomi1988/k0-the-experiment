> **Documento de detalle.** La fuente normativa vigente es [ESPECIFICACION_MAESTRA.md](../ESPECIFICACION_MAESTRA.md). Este capítulo no prevalece ante una regla corregida en la especificación; versiones anteriores en Git.

# 37 — Profesiones, habilidades y gobiernos: catálogo legible

**Estado:** derivación de las definiciones canónicas `data/professions.v2.json`, `data/skills.v2.json`, `data/governments.v2.json` y `data/eras.v2.json`. La profesión se elige una única vez por temporada; el oficio cambia su denominación estética según la era, sin cambiar de familia funcional.

## Etiquetas de oficio por época

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

## Habilidades (30)

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

## Candidaturas de gobierno (9)

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

## Límites

Las habilidades aplican al ciudadano que las obtuvo, salvo indicación contraria explícita en el catálogo; el mismo bono no puede multiplicarse ilimitadamente por número de jugadores. Los gobernantes no sustituyen decisiones del Consejo ni tienen poder para conceder oro, alterar el ganador o saltar hitos. Los valores reflejan el catálogo de diseño, pendientes de calibración tras un motor funcional.
