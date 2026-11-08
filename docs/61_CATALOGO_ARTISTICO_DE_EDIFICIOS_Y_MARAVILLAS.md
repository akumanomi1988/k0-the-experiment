# 61 — Catálogo de dirección artística para 130 edificios y 13 maravillas

**Estado VISUAL_BRIEF, no sprites finales.** Cada fila vincula familia, época y edificio concreto (`data/buildings.v2.json`); la silueta final debe mantener **la huella lógica exacta** y las cuatro etapas de obra. Las tres facciones usan misma regla y colisión, pero diferente arquitectura.

## Transformadores culturales de cualquier edificio

- **Micelios:** cubierta de micelio tejido, pilares orgánicos, entramados de raíces, esporas luminosas discretas. Evitar coral marino, aspecto viscoso indiferenciado y ventaja botánica funcional.
- **Rúnicos:** pilares mineral-poliedro, juntas facetadas, runas geométricas de luz azul, tecnología cristalina. Evitar humanos con armadura y efectos que den ventaja de minería.
- **Ferrinos:** placas bioférricas remachadas, articulaciones, oxidación controlada, arcos de metal vivo. Evitar máquinas totalmente robóticas y coral metálico.

Cada diseño debe producir `faction/era/entity`, cuatro estados de construcción (15/40/70/100 %) y sombras/pivote estables. Las variaciones no añaden edificios extra ni coste lógico.

## Matriz visual completa: 130 edificios básicos

| Era | Familia | Edificio ID | Silueta/objeto dominante a dibujar |
|---|---|---|---|
| Paleolítico | `housing` | `paleolithic_housing` | Refugio de pieles y roca |
| Paleolítico | `food_production` | `paleolithic_food_production` | Fogón comunitario de caza |
| Paleolítico | `forestry` | `paleolithic_forestry` | Bosque señalizado con cestas |
| Paleolítico | `extraction` | `paleolithic_extraction` | Frente de cantera con cinceles |
| Paleolítico | `workshop` | `paleolithic_workshop` | Mesa de hueso y sílex |
| Paleolítico | `research` | `paleolithic_research` | Círculo oral junto al fuego |
| Paleolítico | `storage` | `paleolithic_storage` | Fosa protegida con techo |
| Paleolítico | `infrastructure` | `paleolithic_infrastructure` | Sendero de piedra suelta |
| Paleolítico | `civic` | `paleolithic_civic` | Círculo del Consejo alrededor del fuego |
| Paleolítico | `defense` | `paleolithic_defense` | Puesto de guardia con empalizada |
| Neolítico | `housing` | `neolithic_housing` | Cabaña con huerto |
| Neolítico | `food_production` | `neolithic_food_production` | Granero de siembra y molino |
| Neolítico | `forestry` | `neolithic_forestry` | Vivero vallado y cobertizo |
| Neolítico | `extraction` | `neolithic_extraction` | Excavación de piedra con rampa |
| Neolítico | `workshop` | `neolithic_workshop` | Banco de alfarería y telares |
| Neolítico | `research` | `neolithic_research` | Casa de símbolos y calendario |
| Neolítico | `storage` | `neolithic_storage` | Granero comunitario de barro |
| Neolítico | `infrastructure` | `neolithic_infrastructure` | Camino con acequias y marcas |
| Neolítico | `civic` | `neolithic_civic` | Plaza de elección de clan |
| Neolítico | `defense` | `neolithic_defense` | Vigía de madera y foso |
| Edad del Cobre | `housing` | `copper_housing` | Casa de adobe con hebillas de cobre |
| Edad del Cobre | `food_production` | `copper_food_production` | Secadero de grano y conductos de cobre |
| Edad del Cobre | `forestry` | `copper_forestry` | Aserradero de herramientas cobrizas |
| Edad del Cobre | `extraction` | `copper_extraction` | Pozo y mena con apoyos de cobre |
| Edad del Cobre | `workshop` | `copper_workshop` | Taller de cinceles de cobre |
| Edad del Cobre | `research` | `copper_research` | Tablillas y estantería de cobre |
| Edad del Cobre | `storage` | `copper_storage` | Depósito sellado de cobre |
| Edad del Cobre | `infrastructure` | `copper_infrastructure` | Calzada primitiva con carriles cobrizos |
| Edad del Cobre | `civic` | `copper_civic` | Ágora de cobre con tótems |
| Edad del Cobre | `defense` | `copper_defense` | Torreta de escudo cobrizo |
| Edad del Bronce | `housing` | `bronze_housing` | Vivienda con tejado de aleación |
| Edad del Bronce | `food_production` | `bronze_food_production` | Horno comunal con silo |
| Edad del Bronce | `forestry` | `bronze_forestry` | Taller de madera aleada |
| Edad del Bronce | `extraction` | `bronze_extraction` | Fundición de mineral a pie de mina |
| Edad del Bronce | `workshop` | `bronze_workshop` | Horno de aleación y moldes |
| Edad del Bronce | `research` | `bronze_research` | Archivo de escritura y aleaciones |
| Edad del Bronce | `storage` | `bronze_storage` | Almacén de ánforas y bronce |
| Edad del Bronce | `infrastructure` | `bronze_infrastructure` | Camino de carros reforzados |
| Edad del Bronce | `civic` | `bronze_civic` | Foro de bronce |
| Edad del Bronce | `defense` | `bronze_defense` | Bastión de bronce en terrazas |
| Edad del Hierro | `housing` | `iron_housing` | Casa de fundidor y adobe rojo |
| Edad del Hierro | `food_production` | `iron_food_production` | Almacén de cereal con arado férreo |
| Edad del Hierro | `forestry` | `iron_forestry` | Cobertizo de sierras de hierro |
| Edad del Hierro | `extraction` | `iron_extraction` | Mina reforzada con vigas ferrosas |
| Edad del Hierro | `workshop` | `iron_workshop` | Fragua con yunques |
| Edad del Hierro | `research` | `iron_research` | Cámara de experimentación férrea |
| Edad del Hierro | `storage` | `iron_storage` | Depósito de hierro modular |
| Edad del Hierro | `infrastructure` | `iron_infrastructure` | Puente de vigas de hierro |
| Edad del Hierro | `civic` | `iron_civic` | Gran sala de decisiones férreas |
| Edad del Hierro | `defense` | `iron_defense` | Torre de hierro y almenas |
| Antigüedad | `housing` | `antiquity_housing` | Domus con patio interior |
| Antigüedad | `food_production` | `antiquity_food_production` | Terraza agrícola irrigada |
| Antigüedad | `forestry` | `antiquity_forestry` | Bosque gestionado con vías |
| Antigüedad | `extraction` | `antiquity_extraction` | Cantera de columnas y poleas |
| Antigüedad | `workshop` | `antiquity_workshop` | Taller de hidráulica cívica |
| Antigüedad | `research` | `antiquity_research` | Biblioteca cívica con pergaminos |
| Antigüedad | `storage` | `antiquity_storage` | Almacén cívico con arcos |
| Antigüedad | `infrastructure` | `antiquity_infrastructure` | Calzada cívica con acueducto |
| Antigüedad | `civic` | `antiquity_civic` | Foro clásico de asamblea |
| Antigüedad | `defense` | `antiquity_defense` | Fortín y formación de muralla |
| Edad Media | `housing` | `medieval_housing` | Casas gremiales compactas |
| Edad Media | `food_production` | `medieval_food_production` | Huerta amurallada de monasterio |
| Edad Media | `forestry` | `medieval_forestry` | Leñera del gremio |
| Edad Media | `extraction` | `medieval_extraction` | Galería con elevador de contrapesos |
| Edad Media | `workshop` | `medieval_workshop` | Forja gremial de dos pisos |
| Edad Media | `research` | `medieval_research` | Scriptorium y telescopio primario |
| Edad Media | `storage` | `medieval_storage` | Bodega gremial con torre |
| Edad Media | `infrastructure` | `medieval_infrastructure` | Camino de adoquín y puente levadizo |
| Edad Media | `civic` | `medieval_civic` | Salón de gremios |
| Edad Media | `defense` | `medieval_defense` | Castillo facetado y atalaya |
| Renacimiento | `housing` | `renaissance_housing` | Palacio-casa con logia |
| Renacimiento | `food_production` | `renaissance_food_production` | Invernadero renacentista |
| Renacimiento | `forestry` | `renaissance_forestry` | Jardín botánico y banco de semillas |
| Renacimiento | `extraction` | `renaissance_extraction` | Observatorio de minerales con bombas |
| Renacimiento | `workshop` | `renaissance_workshop` | Laboratorio artesanal con engranajes |
| Renacimiento | `research` | `renaissance_research` | Academia con lentes y observatorio |
| Renacimiento | `storage` | `renaissance_storage` | Almacén de cajas y polipastos |
| Renacimiento | `infrastructure` | `renaissance_infrastructure` | Vía cartografiada y canal |
| Renacimiento | `civic` | `renaissance_civic` | Palacio de ciencia cívica |
| Renacimiento | `defense` | `renaissance_defense` | Baluarte geométrico de ingeniería |
| Era Industrial | `housing` | `industrial_housing` | Bloque obrero con chimenea |
| Era Industrial | `food_production` | `industrial_food_production` | Planta de molienda a vapor |
| Era Industrial | `forestry` | `industrial_forestry` | Aserradero de poleas de vapor |
| Era Industrial | `extraction` | `industrial_extraction` | Pozo industrial y vagón |
| Era Industrial | `workshop` | `industrial_workshop` | Factoría de cadenas y engranajes |
| Era Industrial | `research` | `industrial_research` | Laboratorio químico a vapor |
| Era Industrial | `storage` | `industrial_storage` | Nave de distribución ferroviaria |
| Era Industrial | `infrastructure` | `industrial_infrastructure` | Tramo ferroviario de vapor |
| Era Industrial | `civic` | `industrial_civic` | Ayuntamiento de ladrillo industrial |
| Era Industrial | `defense` | `industrial_defense` | Puesto industrial con reflector |
| Era Moderna | `housing` | `modern_housing` | Barrio de módulos electrificados |
| Era Moderna | `food_production` | `modern_food_production` | Estación de riego eléctrico |
| Era Moderna | `forestry` | `modern_forestry` | Instalación forestal electrificada |
| Era Moderna | `extraction` | `modern_extraction` | Complejo de extracción motorizado |
| Era Moderna | `workshop` | `modern_workshop` | Taller de precisión electromecánica |
| Era Moderna | `research` | `modern_research` | Centro científico electrificado |
| Era Moderna | `storage` | `modern_storage` | Centro logístico de contenedores |
| Era Moderna | `infrastructure` | `modern_infrastructure` | Carretera asfaltada y cableado |
| Era Moderna | `civic` | `modern_civic` | Centro de decisión luminoso |
| Era Moderna | `defense` | `modern_defense` | Centro de protección electromecánico |
| Era Digital | `housing` | `digital_housing` | Hábitat domótico conectado |
| Era Digital | `food_production` | `digital_food_production` | Cultivo automatizado vertical |
| Era Digital | `forestry` | `digital_forestry` | Cultivo de biomasa en red |
| Era Digital | `extraction` | `digital_extraction` | Mina robotizada de cristal |
| Era Digital | `workshop` | `digital_workshop` | Fábrica CNC miniaturizada |
| Era Digital | `research` | `digital_research` | Centro de datos en miniatura |
| Era Digital | `storage` | `digital_storage` | Almacén automatizado de datos/cargas |
| Era Digital | `infrastructure` | `digital_infrastructure` | Red de transporte automatizada |
| Era Digital | `civic` | `digital_civic` | Nexo público de datos |
| Era Digital | `defense` | `digital_defense` | Nexo de defensa de información |
| Era Espacial | `housing` | `space_housing` | Cúpula presurizada residencial |
| Era Espacial | `food_production` | `space_food_production` | Biorreactor hidropónico orbital |
| Era Espacial | `forestry` | `space_forestry` | Jardín de biomasa en cápsula |
| Era Espacial | `extraction` | `space_extraction` | Extractor de regolito presurizado |
| Era Espacial | `workshop` | `space_workshop` | Forja modular de vacío |
| Era Espacial | `research` | `space_research` | Observatorio orbital compartimentado |
| Era Espacial | `storage` | `space_storage` | Módulo de depósito orbital |
| Era Espacial | `infrastructure` | `space_infrastructure` | Pasarela de gravedad orbital |
| Era Espacial | `civic` | `space_civic` | Cámara de consejo espacial |
| Era Espacial | `defense` | `space_defense` | Torre orbital de observación |
| Era Interestelar | `housing` | `interstellar_housing` | Nido interestelar de luz sólida |
| Era Interestelar | `food_production` | `interstellar_food_production` | Sintetizador de nutrientes estelares |
| Era Interestelar | `forestry` | `interstellar_forestry` | Fábrica de biopolímeros sintéticos |
| Era Interestelar | `extraction` | `interstellar_extraction` | Recolector de fragmentos estelares |
| Era Interestelar | `workshop` | `interstellar_workshop` | Ingeniería de metamateriales |
| Era Interestelar | `research` | `interstellar_research` | Laboratorio cuántico interestelar |
| Era Interestelar | `storage` | `interstellar_storage` | Bóveda de inventario interestelar |
| Era Interestelar | `infrastructure` | `interstellar_infrastructure` | Corredor de tránsito fotónico |
| Era Interestelar | `civic` | `interstellar_civic` | Plaza ceremonial de las eras |
| Era Interestelar | `defense` | `interstellar_defense` | Escudo espacial ceremonial |

## Las 13 maravillas con identidad propia

| Era | ID | Nombre | Dirección artística distintiva |
|---|---|---|---|
| Paleolítico | `wonder_paleolithic` | **El Primer Fuego** | Tres fuentes del Primer Fuego rodeadas por estelas ancestrales; la llama no extingue otras naciones. |
| Neolítico | `wonder_neolithic` | **El Gran Semillero** | Jardín elevado con tres coronas de semillas, puertas rituales y suelo agrícola en anillos. |
| Edad del Cobre | `wonder_copper` | **La Forja del Alba** | Gran crisol de cobre sostenido por arcos, reflejos que remiten al amanecer. |
| Edad del Bronce | `wonder_bronze` | **El Crisol de los Tres** | Tres hornos de aleación convergentes sobre una plaza de bronce; no representar victoria de una especie concreta. |
| Edad del Hierro | `wonder_iron` | **El Bastión de las Chispas** | Bastión remachado con cinco chimeneas, fortaleza simbólica sin efecto de defensa competitivo. |
| Antigüedad | `wonder_antiquity` | **La Biblioteca del Primer Reino** | Archivo monumental de estanterías/tablillas con pórticos cívicos y columna central. |
| Edad Media | `wonder_medieval` | **La Aguja de los Juramentos** | Aguja de piedra y metal con cintas de juramentos, mirador y campanas. |
| Renacimiento | `wonder_renaissance` | **El Observatorio de las Tres Lunas** | Observatorio circular con tres lentes y bóveda de las lunas, instrumentos no funcionales. |
| Era Industrial | `wonder_industrial` | **El Corazón de Vapor** | Motor de vapor central dentro de cúpula de vidrio y engranajes monumentales. |
| Era Moderna | `wonder_modern` | **La Torre de Resonancia** | Antena-torre de resonancia con anillos eléctricos suaves y plataforma de museo. |
| Era Digital | `wonder_digital` | **El Archivo de las Mil Voces** | Biblioteca de datos pública con pantallas de píxeles, columnas de información y techo abstracto. |
| Era Espacial | `wonder_space` | **La Puerta del Horizonte** | Arco de horizonte orbital con vacío estrellado visible detrás de su marco. |
| Era Interestelar | `wonder_interstellar` | **El Umbral Interestelar** | Portal interestelar de tres símbolos y luz contenida; únicamente epílogo tras victoria. |

## Proyectos estratégicos de cada era

El trío de Consejo mantiene tres conceptos funcionalmente cosméticos en todas las eras: **Memorial** (monumento vertical con nombres moderados de fundadores), **Espectáculo** (plaza abierta de ceremonia con zona visible de espectadores) y **Archivo** (edificio de memoria/historia con símbolos de la era). Para los 39 casos, el transformador cultural anterior se aplica a la tecnología y material de la fila de la era; coste exacto y trabajo están en `docs/35`. Dos proyectos de la misma época deben distinguirse por silueta vertical/plaza horizontal/volumen de libros-datos, respectivamente.

## Gate artístico

Para elevar esta especificación a arte aprobado hacen falta al menos: cuatro siluetas principales en 1× (3 naciones y K-0), 10 familias × 3 eras muestra, una maravilla por rol visual, un test de HUD con 45 ciudadanos y una auditoría de licencias. Los **390 skins básicos**, **117 skins de proyectos**, **39 variantes de maravilla** y **117 skins de unidades de combate** son entregables futuros, no PNG ya producidos.
