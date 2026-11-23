/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Indian Geography Chapters Metadata Module (Paper I — General Knowledge)
 * Covers 12 Comprehensive Thematic Chapters.
 */
(function(global) {
  "use strict";

  const DATA = [
  {
    "id": "ch-geo-01",
    "subjectId": "gk-geography",
    "number": 1,
    "title": "Physical Setting, Frontiers & Physiographic Divisions of India",
    "description": "Astronomical extent, standard meridian, international land borders, maritime zones, and physical geography of Uttar Pradesh."
  },
  {
    "id": "ch-geo-02",
    "subjectId": "gk-geography",
    "number": 2,
    "title": "The Himalayan Mountain System & Mountain Passes",
    "description": "Tectonic origin, parallel ranges (Himadri, Himachal, Shivaliks), strategic mountain passes, and seismic hazard zones."
  },
  {
    "id": "ch-geo-03",
    "subjectId": "gk-geography",
    "number": 3,
    "title": "River Drainage Systems of India: Himalayan & Peninsular",
    "description": "Indus, Ganga (Panch Prayags), Brahmaputra, peninsular river basins, and the river drainage network of Uttar Pradesh."
  },
  {
    "id": "ch-geo-04",
    "subjectId": "gk-geography",
    "number": 4,
    "title": "Climate, Monsoon Mechanism & Seasons of India",
    "description": "Southwest monsoon dynamics, ITCZ, jet streams, ENSO, Indian Ocean Dipole, Western Disturbances, and Koeppen climate zones."
  },
  {
    "id": "ch-geo-05",
    "subjectId": "gk-geography",
    "number": 5,
    "title": "Soil Types, Distribution & Soil Degradation in India & UP",
    "description": "ICAR 8 soil classes, Khadar vs Bhangar alluvial soils, Bhabhar-Terai zones, and Bundelkhand soils in Uttar Pradesh."
  },
  {
    "id": "ch-geo-06",
    "subjectId": "gk-geography",
    "number": 6,
    "title": "Natural Vegetation, Forests & Wildlife Conservation",
    "description": "Champion & Seth forest types, ISFR forest cover, National Parks, Tiger Reserves, Ramsar wetlands, and Dudhwa National Park UP."
  },
  {
    "id": "ch-geo-07",
    "subjectId": "gk-geography",
    "number": 7,
    "title": "Water Resources, Multipurpose Irrigation & Hydropower Projects",
    "description": "Major dam projects (Bhakra, Tehri, Hirakud, Sardar Sarovar), UP canals, Rihand Dam, and the Ken-Betwa river linking project."
  },
  {
    "id": "ch-geo-08",
    "subjectId": "gk-geography",
    "number": 8,
    "title": "Mineral Resources, Energy & Industrial Geography of India",
    "description": "Metallic/non-metallic mineral belts, Gondwana coalfields, petroleum basins, Singrauli energy hub, and industrial corridors."
  },
  {
    "id": "ch-geo-09",
    "subjectId": "gk-geography",
    "number": 9,
    "title": "Agricultural Geography, Cropping Patterns & Green Revolution",
    "description": "Food and cash crops, agro-climatic zones, agricultural strengths of Uttar Pradesh (sugarcane, wheat, potato), and agricultural revolutions."
  },
  {
    "id": "ch-geo-10",
    "subjectId": "gk-geography",
    "number": 10,
    "title": "Transport Networks & Communication Geography",
    "description": "Indian Railways, Golden Quadrilateral, National Waterway 1 (Ganga), major seaports, and the expressways network of UP."
  },
  {
    "id": "ch-geo-11",
    "subjectId": "gk-geography",
    "number": 11,
    "title": "Population, Demography & Human Geography (Census Data)",
    "description": "Demographic trends, density, sex ratio, literacy, urbanization, and district-level demographic analysis of Uttar Pradesh."
  },
  {
    "id": "ch-geo-12",
    "subjectId": "gk-geography",
    "number": 12,
    "title": "Environmental Issues, Natural Hazards & Disaster Management",
    "description": "Floods, droughts, cyclones, landslides, seismic zonation, UP disaster vulnerability (Terai floods, Bundelkhand droughts), and NDMA framework."
  }
];

  global.GEOGRAPHY_CHAPTERS = DATA;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { chapters: DATA, default: DATA };
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
