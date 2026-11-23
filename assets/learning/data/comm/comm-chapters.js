/**
 * Tanveer Ashraf Judicial Prep - Communications Chapters (Paper I General Knowledge)
 */
(function(global) {
  'use strict';
  var COMM_CHAPTERS = [
  {
    "id": "ch-comm-01",
    "subjectId": "gk-comm",
    "number": 1,
    "order": 1,
    "title": "Principles of Telecommunications & Electromagnetic Spectrum",
    "description": "Radio frequency spectrum, frequency bands (VHF, UHF, microwave), modulation (AM, FM, QAM), bandwidth, propagation modes (ground, sky, space waves).",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-comm-02",
    "subjectId": "gk-comm",
    "number": 2,
    "order": 2,
    "title": "Cellular Mobile Communications: 1G to 5G & 6G Roadmap",
    "description": "Evolution from analog 1G to 5G New Radio (NR), sub-6 GHz vs mmWave, massive MIMO, beamforming, network slicing, and Bharat 6G Vision.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-comm-03",
    "subjectId": "gk-comm",
    "number": 3,
    "order": 3,
    "title": "Optical Fiber Networks & BharatNet Architecture",
    "description": "Total internal reflection in glass fibers, single-mode vs multi-mode, DWDM, BharatNet rural broadband, submarine communications cables.",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-comm-04",
    "subjectId": "gk-comm",
    "number": 4,
    "order": 4,
    "title": "Satellite Communications, Ground Stations & NavIC",
    "description": "Geostationary vs LEO communications constellations, transponders (C-band, Ku-band, Ka-band), VSAT networks, NavIC / IRNSS positioning architecture.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-comm-05",
    "subjectId": "gk-comm",
    "number": 5,
    "order": 5,
    "title": "Internet Infrastructure, Protocols & Web Standards",
    "description": "TCP/IP protocol suite, IPv4 vs IPv6 address exhaustion, Domain Name System (DNS), internet exchange points (NIXI), net neutrality regulations.",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-comm-06",
    "subjectId": "gk-comm",
    "number": 6,
    "order": 6,
    "title": "Broadcasting, DTH & Over-The-Top (OTT) Media",
    "description": "Terrestrial TV (Prasar Bharati / Doordarshan), Direct-To-Home (DTH) Ku-band satellite TV, digital radio (DRM), OTT streaming platforms regulation.",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-comm-07",
    "subjectId": "gk-comm",
    "number": 7,
    "order": 7,
    "title": "Telecommunications Regulatory Architecture & Telecom Act 2023",
    "description": "Telecommunications Act 2023 repealing Indian Telegraph Act 1885, TRAI Act 1997, Digital Bharat Nidhi (replacing USOF), spectrum allocation rules.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-comm-08",
    "subjectId": "gk-comm",
    "number": 8,
    "order": 8,
    "title": "Emergency Communications, Disaster Alert & Public Safety",
    "description": "Common Alerting Protocol (CAP), Cell Broadcast Alert System (CBAS), National Disaster Management Services, HAM radio (amateur radio).",
    "estimatedMinutes": 45
  }
];
  global.COMM_CHAPTERS = COMM_CHAPTERS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { chapters: COMM_CHAPTERS, COMM_CHAPTERS: COMM_CHAPTERS };
  }
})(typeof window !== 'undefined' ? window : global);
