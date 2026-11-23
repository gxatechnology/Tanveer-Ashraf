/**
 * Tanveer Ashraf Judicial Prep - Communications Topics (Paper I General Knowledge)
 */
(function(global) {
  'use strict';
  var COMM_TOPICS = [
  {
    "id": "top-comm-01-01",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-01",
    "number": 1,
    "order": 1,
    "title": "Electromagnetic Spectrum & Frequency Allocation",
    "summary": "Spectrum classification: ELF, VLF, LF, MF, HF, VHF, UHF, SHF, EHF; National Frequency Allocation Plan (NFAP) governed by Wireless Planning and Coordination (WPC) Wing.",
    "keyProvisions": [
      "WPC Wing, Department of Telecommunications",
      "National Frequency Allocation Plan (NFAP)",
      "Microwave vs millimeter-wave bands"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-comm-01-02",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-01",
    "number": 2,
    "order": 2,
    "title": "Modulation Techniques & Signal Transmission",
    "summary": "Amplitude Modulation (AM), Frequency Modulation (FM), Phase Modulation (PM), digital modulation (QAM, PSK, OFDM), multiplexing (FDM, TDM, CDMA).",
    "keyProvisions": [
      "Analog vs Digital modulation",
      "Orthogonal Frequency Division Multiplexing (OFDM)",
      "Noise immunity in FM"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-comm-01-03",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-01",
    "number": 3,
    "order": 3,
    "title": "Radio Wave Propagation Modes",
    "summary": "Ground wave (surface wave for MF/AM radio), sky wave (ionospheric reflection for HF shortwave), space wave / line-of-sight (VHF, UHF, satellite).",
    "keyProvisions": [
      "Ionospheric layers (D, E, F1, F2)",
      "Critical frequency and skip distance",
      "Line-of-sight propagation formula"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-comm-02-01",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-02",
    "number": 4,
    "order": 4,
    "title": "Generational Evolution: 1G to 4G LTE & VoLTE",
    "summary": "1G (AMPS, analog voice), 2G (GSM, CDMA, SMS, GPRS), 3G (UMTS, mobile internet), 4G (LTE, all-IP, Voice over LTE / VoLTE), SIM technology.",
    "keyProvisions": [
      "GSM (900/1800 MHz) vs CDMA",
      "4G LTE standard",
      "VoLTE packet-based voice transmission"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-comm-02-02",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-02",
    "number": 5,
    "order": 5,
    "title": "5G Technology Architecture & Use Cases",
    "summary": "5G New Radio (3GPP Rel 15+), eMBB (enhanced mobile broadband), uRLLC (ultra-reliable low latency communication), mMTC (massive machine type communication), massive MIMO, beamforming.",
    "keyProvisions": [
      "5G三大场景 (eMBB, uRLLC, mMTC)",
      "Sub-6 GHz vs Millimeter Wave (mmWave)",
      "Network Slicing in 5G Core"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-comm-02-03",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-02",
    "number": 6,
    "order": 6,
    "title": "Bharat 6G Vision & Future Terahertz Wireless",
    "summary": "Bharat 6G Vision Document, Apex Council, terahertz frequencies (0.1 - 10 THz), sub-millisecond latency, integration of terrestrial and non-terrestrial networks.",
    "keyProvisions": [
      "Bharat 6G Mission 2030",
      "Terahertz communications",
      "Intelligent reflecting surfaces"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-comm-03-01",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-03",
    "number": 7,
    "order": 7,
    "title": "Optical Fiber Cable (OFC) Mechanics & Physics",
    "summary": "Core-cladding refractive index gradient, total internal reflection, numerical aperture, single-mode fiber (long-distance telecom) vs multi-mode fiber (LANs).",
    "keyProvisions": [
      "Total Internal Reflection (TIR)",
      "Attenuation windows (1310 nm and 1550 nm)",
      "Dense Wavelength Division Multiplexing (DWDM)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-comm-03-02",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-03",
    "number": 8,
    "order": 8,
    "title": "BharatNet Rural Broadband Infrastructure",
    "summary": "National Optical Fibre Network (NOFN) rebranded BharatNet, connecting 2.5 lakh Gram Panchayats with high-speed broadband, executed by BBNL / BSNL.",
    "keyProvisions": [
      "BharatNet Phase I, II, III",
      "Digital Bharat Nidhi funding",
      "Gram Panchayat last-mile Wi-Fi connectivity"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-comm-03-03",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-03",
    "number": 9,
    "order": 9,
    "title": "Submarine Communications Cable Networks",
    "summary": "Undersea fiber-optic cables carrying 99% of international data traffic, cable landing stations in India (Mumbai, Chennai, Kochi), trans-oceanic consortia.",
    "keyProvisions": [
      "Undersea repeaters and erbium-doped fiber amplifiers",
      "Mumbai and Chennai landing stations",
      "Strategic maritime cable security"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-comm-04-01",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-04",
    "number": 10,
    "order": 10,
    "title": "Satellite Communications & Orbital Transponders",
    "summary": "Geostationary communications satellites at ~35,786 km, transponders (uplink and downlink frequencies), C-band, Ku-band (DTH TV), Ka-band (high-throughput broadband).",
    "keyProvisions": [
      "Uplink vs Downlink frequencies",
      "Ku-band (12-18 GHz)",
      "GSAT communications series satellites"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-comm-04-02",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-04",
    "number": 11,
    "order": 11,
    "title": "Very Small Aperture Terminal (VSAT) Networks",
    "summary": "VSAT satellite ground terminals, dish antenna (0.75m to 2.4m), remote banking ATMs, maritime connectivity, civil aviation inflight broadband.",
    "keyProvisions": [
      "VSAT hub and star network topology",
      "In-flight and Maritime Connectivity (IFMC) licenses",
      "Remote connectivity in North-East and islands"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-comm-04-03",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-04",
    "number": 12,
    "order": 12,
    "title": "NavIC (IRNSS) & Global Satellite Positioning Systems",
    "summary": "Navigation with Indian Constellation (NavIC / IRNSS), 7 satellites (3 geostationary, 4 geosynchronous), L5 and S-band signals, comparison with GPS, GLONASS, Galileo, BeiDou.",
    "keyProvisions": [
      "NavIC 7-satellite architecture",
      "Standard Positioning Service (SPS) vs Restricted Service (RS)",
      "Position accuracy < 10 meters across India"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-comm-05-01",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-05",
    "number": 13,
    "order": 13,
    "title": "Internet Protocol Suite: TCP/IP, Routing & DNS",
    "summary": "TCP (transmission control, reliable delivery), IP (routing, packet forwarding), Domain Name System (DNS hierarchy, root servers), National Internet Exchange of India (NIXI).",
    "keyProvisions": [
      "OSI 7-layer vs TCP/IP 4-layer model",
      "DNS resolving IP addresses to domain names",
      "NIXI neutral internet peering points"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-comm-05-02",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-05",
    "number": 14,
    "order": 14,
    "title": "IPv4 vs IPv6 Addressing & Network Security",
    "summary": "IPv4 32-bit address space (4.3 billion addresses), IPv6 128-bit address space (3.4 x 10^38 addresses), India's leading global IPv6 adoption rank.",
    "keyProvisions": [
      "IPv4 32-bit vs IPv6 128-bit structure",
      "India #1 rank in global IPv6 adoption",
      "IPsec security protocols"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-comm-05-03",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-05",
    "number": 15,
    "order": 15,
    "title": "Net Neutrality Principles & Regulatory Standards",
    "summary": "TRAI 2017 Recommendations on Net Neutrality, prohibition of discriminatory treatment (blocking, throttling, paid prioritization), zero-rating controversy.",
    "keyProvisions": [
      "TRAI Prohibition of Discriminatory Tariffs for Data Services Regulations 2016",
      "Equal treatment of all internet traffic",
      "Specialized services exception"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-comm-06-01",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-06",
    "number": 16,
    "order": 16,
    "title": "Terrestrial Broadcasting & Prasar Bharati Mandate",
    "summary": "Prasar Bharati (Broadcasting Corporation of India) Act 1990, All India Radio (Akashvani), Doordarshan (DD National, DD News), Digital Radio Mondiale (DRM).",
    "keyProvisions": [
      "Prasar Bharati Act 1990",
      "Public service broadcasting mandate",
      "FM frequency range: 88 to 108 MHz"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-comm-06-02",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-06",
    "number": 17,
    "order": 17,
    "title": "Direct-To-Home (DTH) TV & OTT Media Regulation",
    "summary": "DTH satellite Ku-band television broadcasting, TRAI New Tariff Order (NTO), Information Technology (Intermediary Guidelines and Digital Media Ethics Code) Rules 2021.",
    "keyProvisions": [
      "DTH licensing policy guidelines",
      "IT Rules 2021 Part III (OTT self-regulatory 3-tier grievance mechanism)",
      "Age classification (U, U/A 7+, 13+, 16+, A)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-comm-07-01",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-07",
    "number": 18,
    "order": 18,
    "title": "Telecommunications Act 2023: Paradigm Overhaul",
    "summary": "Enacted December 2023, repealing Indian Telegraph Act 1885, Indian Wireless Telegraphy Act 1933, and Telegraph Wires (Unlawful Possession) Act 1950; authorization framework.",
    "keyProvisions": [
      "Telecommunications Act 2023 (Act No. 44 of 2023)",
      "Repeal of 1885 Telegraph Act",
      "National security interception standards"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-comm-07-02",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-07",
    "number": 19,
    "order": 19,
    "title": "Spectrum Allocation & Digital Bharat Nidhi",
    "summary": "Auction as primary mode of spectrum assignment, administrative assignment for satellite broadband (First Schedule), Digital Bharat Nidhi replacing USOF.",
    "keyProvisions": [
      "Section 4 (Spectrum assignment)",
      "First Schedule administrative assignment",
      "Digital Bharat Nidhi replacing Universal Service Obligation Fund"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-comm-07-03",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-07",
    "number": 20,
    "order": 20,
    "title": "Telecom Regulatory Authority of India (TRAI) & TDSAT",
    "summary": "TRAI Act 1997, statutory advisory and tariff fixation powers, separation of adjudicatory powers to TDSAT (2000 amendment), consumer protection.",
    "keyProvisions": [
      "TRAI Act 1997 Sections 3, 11, 14",
      "TDSAT dispute adjudication",
      "Tariff regulation and quality of service (QoS) benchmarks"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-comm-08-01",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-08",
    "number": 21,
    "order": 21,
    "title": "Cell Broadcast Alert System & Disaster Warning",
    "summary": "Common Alerting Protocol (CAP), NDMA Cell Broadcast alert messages during tsunamis, earthquakes, cyclones, multi-lingual audible siren overrides.",
    "keyProvisions": [
      "NDMA Integrated Disaster Early Warning Platform",
      "Cell Broadcast Alert System (CBAS)",
      "Disaster Management Act 2005 Section 35"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-comm-08-02",
    "subjectId": "gk-comm",
    "chapterId": "ch-comm-08",
    "number": 22,
    "order": 22,
    "title": "Amateur Radio (HAM) & Emergency Wireless",
    "summary": "Amateur Station Operator's Certificate (ASOC) issued by WPC Wing, wireless communication during infrastructure collapse, high frequency emergency networks.",
    "keyProvisions": [
      "Indian Wireless Telegraphs (Amateur Service) Rules 1978",
      "HAM radio frequency allocations",
      "Disaster relief communications role"
    ],
    "estimatedMinutes": 20
  }
];
  global.COMM_TOPICS = COMM_TOPICS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { topics: COMM_TOPICS, COMM_TOPICS: COMM_TOPICS };
  }
})(typeof window !== 'undefined' ? window : global);
