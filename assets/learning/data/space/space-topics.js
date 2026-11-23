/**
 * Tanveer Ashraf Judicial Prep - Space Science Topics (Paper I General Knowledge)
 */
(function(global) {
  'use strict';
  var SPACE_TOPICS = [
  {
    "id": "top-space-01-01",
    "subjectId": "gk-space",
    "chapterId": "ch-space-01",
    "number": 1,
    "order": 1,
    "title": "Kepler's Laws & Principles of Orbital Motion",
    "summary": "Kepler's first law (elliptical orbits with Sun at one focus), second law (areal velocity is constant), third law (T^2 ∝ r^3), orbital speed and period.",
    "keyProvisions": [
      "Kepler's Three Laws of Planetary Motion",
      "Orbital Velocity formula: v = √(GM/r)",
      "Escape Velocity formula: ve = √(2GM/R) = 11.2 km/s"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-01-02",
    "subjectId": "gk-space",
    "chapterId": "ch-space-01",
    "number": 2,
    "order": 2,
    "title": "Classification of Orbits: LEO, MEO, GEO & SSO",
    "summary": "Low Earth Orbit (160 - 2,000 km), Medium Earth Orbit (navigation constellations ~20,000 km), Geostationary Orbit (35,786 km, period 24 hours), Sun-Synchronous Polar Orbit (SSO ~600-800 km, constant local solar time).",
    "keyProvisions": [
      "LEO (ISS, remote sensing)",
      "GEO altitude exactly ~35,786 km above equator",
      "SSO retrograde inclination ~98 degrees"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-01-03",
    "subjectId": "gk-space",
    "chapterId": "ch-space-01",
    "number": 3,
    "order": 3,
    "title": "Lagrange Points & Gravitational Equilibrium",
    "summary": "Five Lagrangian equilibrium points in a two-body orbital system, collinear points (L1, L2, L3) vs stable triangular points (L4, L5), Sun-Earth L1 (Aditya-L1 halo orbit) and L2 (JWST).",
    "keyProvisions": [
      "Sun-Earth L1 point distance ~1.5 million km from Earth",
      "Uninterrupted solar observation at L1",
      "Halo orbit around L1"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-02-01",
    "subjectId": "gk-space",
    "chapterId": "ch-space-02",
    "number": 4,
    "order": 4,
    "title": "Rocket Propulsion Principles & Propellant Stages",
    "summary": "Tsiolkovsky rocket equation, solid propellants (HTPB - high thrust, non-throttleable), liquid propellants (UDMH/N2O4, hypergolic), cryogenic propellants (liquid hydrogen LH2 at -253°C and liquid oxygen LOX at -183°C).",
    "keyProvisions": [
      "Specific impulse (Isp) measure of efficiency",
      "Cryogenic upper stages (CE-20 indigenous engine)",
      "Vikas engine (liquid fuel, Nambi Narayanan)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-02-02",
    "subjectId": "gk-space",
    "chapterId": "ch-space-02",
    "number": 5,
    "order": 5,
    "title": "PSLV: The Workhorse of Indian Space",
    "summary": "Polar Satellite Launch Vehicle (4-stage vehicle: solid-liquid-solid-liquid), variants (PSLV-CA, PSLV-XL), launch of Chandrayaan-1 (PSLV-C11), Mars Orbiter Mission (PSLV-C25), record 104 satellites in single launch (PSLV-C37).",
    "keyProvisions": [
      "PSLV 4-stage configuration (S-L-S-L)",
      "PSLV-C37 record 104 satellites (2017)",
      "Payload capacity: 1,750 kg to SSO"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-02-03",
    "subjectId": "gk-space",
    "chapterId": "ch-space-02",
    "number": 6,
    "order": 6,
    "title": "LVM3, GSLV & Small Satellite Launch Vehicle (SSLV)",
    "summary": "Geosynchronous Satellite Launch Vehicle Mk II, LVM3 / GSLV Mk III (heavy lifter, 2 solid strap-ons S200, liquid core L110, cryogenic upper stage C25; payload 4,000 kg to GTO, 8,000 kg to LEO), SSLV 3-stage all-solid vehicle for rapid commercial deployment.",
    "keyProvisions": [
      "LVM3 heaviest Indian rocket (launched Chandrayaan-2, Chandrayaan-3, OneWeb)",
      "SSLV payload 500 kg to LEO",
      "Semi-cryogenic engine (SCE-200 kerosene-LOX development)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-03-01",
    "subjectId": "gk-space",
    "chapterId": "ch-space-03",
    "number": 7,
    "order": 7,
    "title": "Genesis of Indian Space Programme & Dr. Vikram Sarabhai",
    "summary": "INCOSPAR established 1962 under Department of Atomic Energy, first sounding rocket launch from Thumba (TERLS, Kerala) November 21, 1963, formation of ISRO on August 15, 1969, Department of Space (DOS) created 1972.",
    "keyProvisions": [
      "Dr. Vikram Sarabhai father of Indian Space Programme",
      "Aryabhata first Indian satellite launched April 19, 1975 from Kapustin Yar",
      "SITE experiment 1975-76"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-03-02",
    "subjectId": "gk-space",
    "chapterId": "ch-space-03",
    "number": 8,
    "order": 8,
    "title": "Major ISRO Centres, Roles & Launch Infrastructure",
    "summary": "Vikram Sarabhai Space Centre (VSSC, Thiruvananthapuram - launch vehicle design), Satish Dhawan Space Centre (SDSC SHAR, Sriharikota, Andhra Pradesh - spaceport), UR Rao Satellite Centre (URSC, Bengaluru - satellite fabrication), Space Applications Centre (SAC, Ahmedabad).",
    "keyProvisions": [
      "SDSC Sriharikota launchpads (First & Second Launch Pads)",
      "Kulasekarapattinam (Tamil Nadu) upcoming second spaceport for SSLV",
      "ISTRAC Bengaluru telemetry and tracking"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-04-01",
    "subjectId": "gk-space",
    "chapterId": "ch-space-04",
    "number": 9,
    "order": 9,
    "title": "Chandrayaan-1: Discovery of Water on the Moon",
    "summary": "Launched October 22, 2008 by PSLV-C11, lunar orbiter carrying 11 scientific payloads, Moon Impact Probe (MIP) struck Shackleton crater November 14, 2008, Moon Mineralogy Mapper (M3) confirmed presence of hydroxyl (OH) and water molecules (H2O).",
    "keyProvisions": [
      "Chandrayaan-1 launch date: 22 October 2008",
      "Discovery of water on Moon confirmed by NASA M3 and MIP",
      "Terrain Mapping Camera (TMC)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-04-02",
    "subjectId": "gk-space",
    "chapterId": "ch-space-04",
    "number": 10,
    "order": 10,
    "title": "Chandrayaan-2 Mission Architecture & Orbiter Data",
    "summary": "Launched July 22, 2019 by GSLV Mk III-M1, composite architecture: Orbiter, Vikram lander, and Pragyan rover; hard landing of Vikram, flawless operation of Orbiter carrying highest resolution optical camera (OHRC).",
    "keyProvisions": [
      "Launch vehicle: GSLV Mk III-M1",
      "Orbiter 100 km lunar orbit with 7+ year operational life",
      "Dual-frequency Synthetic Aperture Radar (DFSAR)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-04-03",
    "subjectId": "gk-space",
    "chapterId": "ch-space-04",
    "number": 11,
    "order": 11,
    "title": "Chandrayaan-3 Historic South Pole Soft-Landing",
    "summary": "Launched July 14, 2023 by LVM3-M4, historic soft landing near lunar south pole (~69.37° S) on August 23, 2023 (celebrated as National Space Day), landing site named 'Shiv Shakti Point', Chandrayaan-2 crash site named 'Tiranga Point', Pragyan rover confirmed sulphur (S).",
    "keyProvisions": [
      "Soft landing date: August 23, 2023 (National Space Day)",
      "Shiv Shakti Point coordinates: 69.37° S, 32.35° E",
      "ChaSTE, ILSA, and LIBS payloads on lander and rover"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-space-05-01",
    "subjectId": "gk-space",
    "chapterId": "ch-space-05",
    "number": 12,
    "order": 12,
    "title": "Mars Orbiter Mission (Mangalyaan) Success & Scientific Findings",
    "summary": "Launched November 5, 2013 by PSLV-C25, Mars orbital insertion September 24, 2014, India became first nation to reach Mars orbit on maiden attempt and first Asian nation to reach Mars, extremely cost-effective (~$74 million / INR 450 Cr).",
    "keyProvisions": [
      "Launch: 5 Nov 2013; Mars Orbit Insertion: 24 Sept 2014",
      "Mars Colour Camera (MCC)",
      "Methane Sensor for Mars (MSM)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-05-02",
    "subjectId": "gk-space",
    "chapterId": "ch-space-05",
    "number": 13,
    "order": 13,
    "title": "Venus Orbiter Mission (Shukrayaan) & Planetary Roadmap",
    "summary": "Approved September 2024 by Union Cabinet, studying Venusian atmosphere, surface geology, subsurface radar probing, atmospheric chemistry, scheduled for 2028 launch window.",
    "keyProvisions": [
      "Venus Orbiter Mission approved outlay: INR 1,236 Cr",
      "Synthetic Aperture Radar for Venusian clouds penetration",
      "Launch vehicle: LVM3"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-06-01",
    "subjectId": "gk-space",
    "chapterId": "ch-space-06",
    "number": 14,
    "order": 14,
    "title": "Aditya-L1: India's First Solar Observatory",
    "summary": "Launched September 2, 2023 by PSLV-C57, halo orbit around Sun-Earth L1 point (1.5 million km from Earth), 7 payloads studying solar corona, chromosphere, photosphere, solar wind, and coronal mass ejections (CMEs).",
    "keyProvisions": [
      "Aditya-L1 halo orbit around L1 Lagrange point",
      "Visible Emission Line Coronagraph (VELC) primary payload",
      "Solar Ultraviolet Imaging Telescope (SUIT)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-space-06-02",
    "subjectId": "gk-space",
    "chapterId": "ch-space-06",
    "number": 15,
    "order": 15,
    "title": "Space Astronomy: AstroSat & XPoSat Missions",
    "summary": "AstroSat (launched 2015, India's first dedicated multi-wavelength space telescope, simultaneous UV/optical/X-ray observation), XPoSat (X-ray Polarimeter Satellite, launched Jan 1, 2024, studying cosmic X-ray polarization from black holes and neutron stars).",
    "keyProvisions": [
      "AstroSat multi-wavelength capability",
      "XPoSat POLIX and XSPECT payloads",
      "World's second satellite-based X-ray polarimetry mission after NASA IXPE"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-07-01",
    "subjectId": "gk-space",
    "chapterId": "ch-space-07",
    "number": 16,
    "order": 16,
    "title": "Gaganyaan Mission Architecture & Crew Module Systems",
    "summary": "Human Spaceflight Mission carrying 3 astronauts to 400 km LEO for a 3-day mission, human-rated LVM3 (HLVM3), Crew Module (CM) and Service Module (SM), life support systems (ECLSS), crew escape system.",
    "keyProvisions": [
      "Gaganyaan human spaceflight target 400 km LEO",
      "HLVM3 human-rated launch vehicle",
      "Astronaut-designates trained at Yuri Gagarin Cosmonaut Center and ISRO"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-space-07-02",
    "subjectId": "gk-space",
    "chapterId": "ch-space-07",
    "number": 17,
    "order": 17,
    "title": "Gaganyaan Test Flights & Vyommitra Humanoid Robot",
    "summary": "TV-D1 (Test Vehicle Demonstration 1) successful crew escape abort test in October 2023, Vyommitra half-humanoid robot designed by ISRO to simulate human parameters in uncrewed test flights.",
    "keyProvisions": [
      "TV-D1 inflight abort test success",
      "Vyommitra AI humanoid robot features",
      "Parachute deployment deceleration sequence"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-07-03",
    "subjectId": "gk-space",
    "chapterId": "ch-space-07",
    "number": 18,
    "order": 18,
    "title": "Bharatiya Antariksh Station (BAS) & Long-Term Space Vision",
    "summary": "Approved by Cabinet in 2024, BAS-1 first module launch planned for 2028, operational 52-tonne modular space station in LEO by 2035, Indian human lunar landing targeted by 2040.",
    "keyProvisions": [
      "BAS-1 initial module target: 2028",
      "Full space station operational target: 2035",
      "Indian astronaut Moon landing vision: 2040"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-08-01",
    "subjectId": "gk-space",
    "chapterId": "ch-space-08",
    "number": 19,
    "order": 19,
    "title": "Earth Observation Satellites: Cartosat, RISAT & Oceansat",
    "summary": "Cartosat series (high resolution panchromatic and multispectral cartographic imaging, sub-meter resolution), RISAT series (all-weather Day-and-Night Synthetic Aperture Radar / SAR), Oceansat ocean state forecasting.",
    "keyProvisions": [
      "Cartosat sub-meter spatial resolution",
      "RISAT C-band and X-band radar penetration through clouds",
      "Oceansat ocean color monitor"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-08-02",
    "subjectId": "gk-space",
    "chapterId": "ch-space-08",
    "number": 20,
    "order": 20,
    "title": "Meteorological Space Assets & BHUVAN Geo-Portal",
    "summary": "INSAT-3D, INSAT-3DR, and INSAT-3DS advanced meteorological satellites in geostationary orbit carrying sounders and imagers, BHUVAN 3D geoportal developed by NRSC for geospatial governance.",
    "keyProvisions": [
      "INSAT-3DS launched February 2024 by GSLV-F14",
      "BHUVAN Indian counterpart to Google Earth",
      "Disaster management support system"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-09-01",
    "subjectId": "gk-space",
    "chapterId": "ch-space-09",
    "number": 21,
    "order": 21,
    "title": "Indian Space Policy 2023 & Non-Government Entities",
    "summary": "Notified April 2023, delineating roles: ISRO (R&D and exploration), IN-SPACe (autonomous regulator and single-window clearance for NGEs), NSIL (commercialization and manufacturing), private sector end-to-end space activities.",
    "keyProvisions": [
      "Indian Space Policy 2023 institutional pillars",
      "100% FDI in space sector under amended policy 2024",
      "Non-Government Entities (NGEs) authorization"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-09-02",
    "subjectId": "gk-space",
    "chapterId": "ch-space-09",
    "number": 22,
    "order": 22,
    "title": "IN-SPACe & Commercial Mandate of NSIL",
    "summary": "Indian National Space Promotion and Authorization Centre (IN-SPACe, Ahmedabad), single-window agency, NewSpace India Limited (NSIL, CPSE under DOS, commercial launch of OneWeb satellites via LVM3).",
    "keyProvisions": [
      "IN-SPACe single window portal",
      "NSIL commercial operator of GSAT satellites",
      "Commercial LVM3 launches"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-09-03",
    "subjectId": "gk-space",
    "chapterId": "ch-space-09",
    "number": 23,
    "order": 23,
    "title": "Private Space Startups & Suborbital Launches",
    "summary": "Skyroot Aerospace (Vikram-S launched Nov 2022, India's first privately developed rocket), Agnikul Cosmos (Agnibaan SOrTeD launched May 2024, world's first single-piece 3D-printed semi-cryogenic engine).",
    "keyProvisions": [
      "Vikram-S maiden private launch (Mission Prarambh)",
      "Agnibaan SOrTeD 3D-printed Agnilet engine",
      "Private launchpads at Sriharikota"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-10-01",
    "subjectId": "gk-space",
    "chapterId": "ch-space-10",
    "number": 24,
    "order": 24,
    "title": "Outer Space Treaty 1967 & Foundational UN Treaties",
    "summary": "Treaty on Principles Governing the Activities of States in the Exploration and Use of Outer Space, including the Moon and Other Celestial Bodies (1967): space is province of all mankind, non-appropriation by claim of sovereignty (Article II), ban on nuclear weapons or weapons of mass destruction in orbit (Article IV).",
    "keyProvisions": [
      "Outer Space Treaty 1967 (Magna Carta of Space Law)",
      "Non-appropriation principle (Article II)",
      "State international responsibility for national space activities (Article VI)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-space-10-02",
    "subjectId": "gk-space",
    "chapterId": "ch-space-10",
    "number": 25,
    "order": 25,
    "title": "Liability Convention 1972 & Registration Convention 1975",
    "summary": "Convention on International Liability for Damage Caused by Space Objects 1972 (absolute liability on launching state for surface damage; fault liability in outer space), Registration Convention 1975, Rescue Agreement 1968.",
    "keyProvisions": [
      "Liability Convention 1972 (Absolute vs Fault liability)",
      "Registration Convention 1975 (UN Register of Space Objects)",
      "Rescue Agreement 1968"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-space-10-03",
    "subjectId": "gk-space",
    "chapterId": "ch-space-10",
    "number": 26,
    "order": 26,
    "title": "Space Debris, Kessler Syndrome & Project NETRA",
    "summary": "Space debris proliferation in LEO, Kessler syndrome runaway cascade collision theory, ISRO Project NETRA (Network for space object Tracking and Analysis) for optical and radar tracking of collision threats, Artemis Accords (India signed June 2023).",
    "keyProvisions": [
      "Project NETRA space situational awareness (SSA)",
      "Kessler Syndrome concept (Donald Kessler 1978)",
      "India became 27th signatory to Artemis Accords (2023)"
    ],
    "estimatedMinutes": 20
  }
];
  global.SPACE_TOPICS = SPACE_TOPICS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { topics: SPACE_TOPICS, SPACE_TOPICS: SPACE_TOPICS };
  }
})(typeof window !== 'undefined' ? window : global);
