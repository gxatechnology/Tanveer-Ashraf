/**
 * Tanveer Ashraf Judicial Prep - Space Science Chapters (Paper I General Knowledge)
 */
(function(global) {
  'use strict';
  var SPACE_CHAPTERS = [
  {
    "id": "ch-space-01",
    "subjectId": "gk-space",
    "number": 1,
    "order": 1,
    "title": "Orbital Mechanics, Celestial Physics & Types of Orbits",
    "description": "Kepler's laws, Low Earth Orbit (LEO), Medium Earth Orbit (MEO), Geostationary Earth Orbit (GEO), Sun-Synchronous Polar Orbit (SSO), Lagrange points (L1 to L5).",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-space-02",
    "subjectId": "gk-space",
    "number": 2,
    "order": 2,
    "title": "Rocket Propulsion & Indian Launch Vehicle Evolution",
    "description": "Rocket equation, solid vs liquid vs cryogenic propellants, SLV-3, ASLV, PSLV (workhorse), GSLV Mk II, LVM3 (GSLV Mk III), SSLV, and semi-cryogenic engines.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-space-03",
    "subjectId": "gk-space",
    "number": 3,
    "order": 3,
    "title": "ISRO Architecture, Key Space Centres & Policy Vision",
    "description": "Genesis under Dr. Vikram Sarabhai, INCOSPAR 1962, ISRO 1969, DOS, key centres: VSSC (Thiruvananthapuram), SDSC SHAR (Sriharikota), URSC (Bengaluru), SAC (Ahmedabad), NRSC (Hyderabad), IPRC (Mahendragiri).",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-space-04",
    "subjectId": "gk-space",
    "number": 4,
    "order": 4,
    "title": "Lunar Exploration Missions: Chandrayaan-1, 2, 3 & 4",
    "description": "Chandrayaan-1 (discovery of water molecules on Moon, MIP), Chandrayaan-2 (Orbiter, Vikram lander, Pragyan rover), Chandrayaan-3 historic South Pole landing (Shiv Shakti Point), Chandrayaan-4 sample return.",
    "estimatedMinutes": 55
  },
  {
    "id": "ch-space-05",
    "subjectId": "gk-space",
    "number": 5,
    "order": 5,
    "title": "Planetary Exploration: Mangalyaan (MOM) & Shukrayaan",
    "description": "Mars Orbiter Mission (Mangalyaan, PSLV-C25, maiden attempt success, methane sensor), Venus Orbiter Mission (Shukrayaan), Mars Lander Mission (Mangalyaan-2).",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-space-06",
    "subjectId": "gk-space",
    "number": 6,
    "order": 6,
    "title": "Solar & Deep Space Astronomy Observatories",
    "description": "Aditya-L1 halo orbit around Sun-Earth L1 point, seven payloads (VELC, SUIT, ASPEX), AstroSat (India's first multi-wavelength space observatory), XPoSat (X-ray polarimetry).",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-space-07",
    "subjectId": "gk-space",
    "number": 7,
    "order": 7,
    "title": "Human Spaceflight Programme: Gaganyaan & Space Station",
    "description": "Gaganyaan 3-member crew to 400 km LEO for 3 days, crew module, environmental control (ECLSS), TV-D1 abort test, Vyommitra humanoid robot, Bharatiya Antariksh Station (BAS).",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-space-08",
    "subjectId": "gk-space",
    "number": 8,
    "order": 8,
    "title": "Earth Observation, Remote Sensing & Disaster Monitoring",
    "description": "IRS series, Cartosat (high resolution cartography), RISAT (radar imaging, synthetic aperture radar), Oceansat, INSAT-3DR/3DS meteorological satellites, BHUVAN geo-portal.",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-space-09",
    "subjectId": "gk-space",
    "number": 9,
    "order": 9,
    "title": "Indian Space Policy 2023, IN-SPACe & Commercial Space Ecosystem",
    "description": "Indian Space Policy 2023, IN-SPACe (single window authorization for private sector), NewSpace India Limited (NSIL commercial arm), private launch vehicles (Vikram-S, Agnibaan).",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-space-10",
    "subjectId": "gk-space",
    "number": 10,
    "order": 10,
    "title": "Space Law, Outer Space Treaties & Space Debris Mitigation",
    "description": "Outer Space Treaty 1967 (res communis omnium, non-weaponization of celestial bodies), Rescue Agreement, Liability Convention 1972, Registration Convention 1975, Artemis Accords, Kessler syndrome, Project NETRA.",
    "estimatedMinutes": 50
  }
];
  global.SPACE_CHAPTERS = SPACE_CHAPTERS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { chapters: SPACE_CHAPTERS, SPACE_CHAPTERS: SPACE_CHAPTERS };
  }
})(typeof window !== 'undefined' ? window : global);
