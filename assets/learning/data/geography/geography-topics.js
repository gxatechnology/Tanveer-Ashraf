/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Indian Geography Topics Metadata Module (Paper I — General Knowledge)
 * Covers 32 Topics across 12 Chapters.
 */
(function(global) {
  "use strict";

  const DATA = [
  {
    "id": "top-geo-01-01",
    "chapterId": "ch-geo-01",
    "subjectId": "gk-geography",
    "title": "Latitudinal/Longitudinal Extent, Standard Meridian (82\u00b030' E Mirzapur UP), Borders & Maritime Zones"
  },
  {
    "id": "top-geo-01-02",
    "chapterId": "ch-geo-01",
    "subjectId": "gk-geography",
    "title": "Major Physiographic Divisions: Northern Mountains, Great Plains, Peninsular Plateau, Coastal Plains & Islands"
  },
  {
    "id": "top-geo-01-03",
    "chapterId": "ch-geo-01",
    "subjectId": "gk-geography",
    "title": "Physical Geography of Uttar Pradesh: Bhabhar, Terai, Ganga-Yamuna Doab & Bundelkhand Plateau"
  },
  {
    "id": "top-geo-02-01",
    "chapterId": "ch-geo-02",
    "subjectId": "gk-geography",
    "title": "The Himalayan Mountain System: Himadri (Greater), Himachal (Lesser), Shivaliks & Purvanchal Hills"
  },
  {
    "id": "top-geo-02-02",
    "chapterId": "ch-geo-02",
    "subjectId": "gk-geography",
    "title": "Strategic Mountain Passes of India: Karakoram, Zoji La, Shipki La, Lipulekh, Nathu La & Bomdi La"
  },
  {
    "id": "top-geo-02-03",
    "chapterId": "ch-geo-02",
    "subjectId": "gk-geography",
    "title": "Geological Evolution, Plate Tectonics, Earthquakes & Seismic Vulnerability Zonation"
  },
  {
    "id": "top-geo-03-01",
    "chapterId": "ch-geo-03",
    "subjectId": "gk-geography",
    "title": "Himalayan River Systems: Indus, Ganga (Bhagirathi-Alaknanda Panch Prayags) & Brahmaputra Basin"
  },
  {
    "id": "top-geo-03-02",
    "chapterId": "ch-geo-03",
    "subjectId": "gk-geography",
    "title": "Peninsular River Systems: East-Flowing (Godavari, Krishna, Cauvery) & West-Flowing (Narmada, Tapti)"
  },
  {
    "id": "top-geo-03-03",
    "chapterId": "ch-geo-03",
    "subjectId": "gk-geography",
    "title": "River Drainage Network of Uttar Pradesh: Ganga, Yamuna, Ghaghara, Gomti, Sarda, Betwa, Ken & Son"
  },
  {
    "id": "top-geo-04-01",
    "chapterId": "ch-geo-04",
    "subjectId": "gk-geography",
    "title": "Southwest Monsoon Mechanism: Thermal Low, Somali Jet, Tropical Easterly Jet, Tibetan Plateau & ITCZ"
  },
  {
    "id": "top-geo-04-02",
    "chapterId": "ch-geo-04",
    "subjectId": "gk-geography",
    "title": "ENSO (El Ni\u00f1o/La Ni\u00f1a), Indian Ocean Dipole (IOD) & Western Disturbances (Winter Rains in UP)"
  },
  {
    "id": "top-geo-04-03",
    "chapterId": "ch-geo-04",
    "subjectId": "gk-geography",
    "title": "Koeppen's Climate Classification of India & Annual Seasons (Summer Loo, Retreating Monsoon)"
  },
  {
    "id": "top-geo-05-01",
    "chapterId": "ch-geo-05",
    "subjectId": "gk-geography",
    "title": "Major Soil Groups of India (ICAR 8 Groups): Alluvial, Black (Regur), Red & Yellow, Laterite, Arid, Saline"
  },
  {
    "id": "top-geo-05-02",
    "chapterId": "ch-geo-05",
    "subjectId": "gk-geography",
    "title": "Soils of Uttar Pradesh: Khadar (New Alluvium), Bhangar (Old Alluvium), Bhabhar, Terai & Bundelkhand Mar/Kabar"
  },
  {
    "id": "top-geo-06-01",
    "chapterId": "ch-geo-06",
    "subjectId": "gk-geography",
    "title": "Natural Vegetation & Forest Types of India (Champion & Seth): Tropical Evergreen, Deciduous, Thorn & Mangroves"
  },
  {
    "id": "top-geo-06-02",
    "chapterId": "ch-geo-06",
    "subjectId": "gk-geography",
    "title": "India State of Forest Report (ISFR) & Protected Area Network (National Parks, Biosphere Reserves, Tigers)"
  },
  {
    "id": "top-geo-06-03",
    "chapterId": "ch-geo-06",
    "subjectId": "gk-geography",
    "title": "Forests, Wildlife Sanctuaries & National Parks of UP: Dudhwa National Park, Pilibhit Tiger Reserve & Ramsar Wetlands"
  },
  {
    "id": "top-geo-07-01",
    "chapterId": "ch-geo-07",
    "subjectId": "gk-geography",
    "title": "Major Multipurpose River Valley Projects of India: Bhakra Nangal, Hirakud, Tehri, Sardar Sarovar & Damodar"
  },
  {
    "id": "top-geo-07-02",
    "chapterId": "ch-geo-07",
    "subjectId": "gk-geography",
    "title": "Irrigation Canals & Dams of UP: Upper Ganga Canal, Sharda Sahayak, Rihand Dam (Pant Sagar) & Ken-Betwa Link"
  },
  {
    "id": "top-geo-08-01",
    "chapterId": "ch-geo-08",
    "subjectId": "gk-geography",
    "title": "Metallic & Non-Metallic Mineral Belts of India: Iron Ore, Bauxite, Manganese, Mica, Copper & Limestone"
  },
  {
    "id": "top-geo-08-02",
    "chapterId": "ch-geo-08",
    "subjectId": "gk-geography",
    "title": "Fossil Fuels & Energy Resources: Gondwana Coalfields, Petroleum Basins (Bombay High, Digboi), Solar & Nuclear"
  },
  {
    "id": "top-geo-08-03",
    "chapterId": "ch-geo-08",
    "subjectId": "gk-geography",
    "title": "Mineral Resources & Energy Geography of UP: Sonbhadra Singrauli Coal/Thermal, Bauxite, Glass-sand & DMIC"
  },
  {
    "id": "top-geo-09-01",
    "chapterId": "ch-geo-09",
    "subjectId": "gk-geography",
    "title": "Major Foodgrain & Cash Crops of India: Rice, Wheat, Millets, Sugarcane, Cotton, Jute, Tea & Coffee"
  },
  {
    "id": "top-geo-09-02",
    "chapterId": "ch-geo-09",
    "subjectId": "gk-geography",
    "title": "Agricultural Profile of Uttar Pradesh: Sugarcane Belt, Wheat-Potato Leadership, Mango Belts & 9 Agro-Climatic Zones"
  },
  {
    "id": "top-geo-09-03",
    "chapterId": "ch-geo-09",
    "subjectId": "gk-geography",
    "title": "Agricultural Revolutions: Green Revolution (M.S. Swaminathan), Operation Flood (White), Blue Revolution & Sustainable Agriculture"
  },
  {
    "id": "top-geo-10-01",
    "chapterId": "ch-geo-10",
    "subjectId": "gk-geography",
    "title": "Indian Railways, Dedicated Freight Corridors (EDFC & WDFC) & National Highways (Golden Quadrilateral)"
  },
  {
    "id": "top-geo-10-02",
    "chapterId": "ch-geo-10",
    "subjectId": "gk-geography",
    "title": "Inland Waterways (National Waterway 1: Prayagraj to Haldia on Ganga) & Major Seaports of India"
  },
  {
    "id": "top-geo-10-03",
    "chapterId": "ch-geo-10",
    "subjectId": "gk-geography",
    "title": "Expressways & Civil Aviation Network of Uttar Pradesh: Purvanchal, Bundelkhand, Ganga Expressways & Jewar Airport"
  },
  {
    "id": "top-geo-11-01",
    "chapterId": "ch-geo-11",
    "subjectId": "gk-geography",
    "title": "Population, Density, Sex Ratio, Literacy, Child Sex Ratio & Scheduled Castes/Tribes in India (Census)"
  },
  {
    "id": "top-geo-11-02",
    "chapterId": "ch-geo-11",
    "subjectId": "gk-geography",
    "title": "Demographic Profile of Uttar Pradesh: Population Totals, Density, Sex Ratio, Literacy & District Comparisons"
  },
  {
    "id": "top-geo-12-01",
    "chapterId": "ch-geo-12",
    "subjectId": "gk-geography",
    "title": "Natural Hazards in India: Floods, Droughts, Tropical Cyclones, Landslides, Tsunami & NDMA Framework"
  },
  {
    "id": "top-geo-12-02",
    "chapterId": "ch-geo-12",
    "subjectId": "gk-geography",
    "title": "Disaster Vulnerability Profile of Uttar Pradesh: Eastern Terai Floods, Bundelkhand Droughts & Seismic Zones"
  }
];

  global.GEOGRAPHY_TOPICS = DATA;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { topics: DATA, default: DATA };
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
