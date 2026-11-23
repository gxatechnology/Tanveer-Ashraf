/**
 * Tanveer Ashraf Judicial Prep - International Affairs and Institutions Topics (Paper I General Knowledge)
 */
(function(global) {
  'use strict';
  var INTERNATIONAL_TOPICS = [
  {
    "id": "top-intl-01-01",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-01",
    "number": 1,
    "order": 1,
    "title": "Genesis of the United Nations & UN Charter Architecture",
    "summary": "League of Nations collapse, Atlantic Charter 1941, Yalta Conference, San Francisco Conference 1945, Charter ratification October 24, 1945.",
    "keyProvisions": [
      "UN Charter Preamble",
      "Articles 1 & 2 (Purposes and Principles)",
      "Sovereign equality Article 2(1)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-01-02",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-01",
    "number": 2,
    "order": 2,
    "title": "UN General Assembly: Composition, Powers & Resolutions",
    "summary": "All 193 member states representation, one-state-one-vote, Article 18 voting rules (two-thirds majority on important questions), Uniting for Peace Res 377A.",
    "keyProvisions": [
      "UN Charter Articles 9-22",
      "Uniting for Peace Resolution 377A (1950)",
      "Annual General Debate"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-01-03",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-01",
    "number": 3,
    "order": 3,
    "title": "UN Security Council: Permanent Members, Veto & Sanctions",
    "summary": "P5 permanent members, 10 non-permanent members elected for 2-year terms, double veto, Chapter VI pacific settlement, Chapter VII enforcement action.",
    "keyProvisions": [
      "UN Charter Articles 23, 27 (Veto Power), 39, 41 (Sanctions), 42 (Military Force)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-02-01",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-02",
    "number": 4,
    "order": 4,
    "title": "International Court of Justice: Structure & Judicial Mandate",
    "summary": "Seat at Peace Palace The Hague, 15 independent judges elected by GA and SC for 9-year terms, no two nationals from same state, ad hoc judges.",
    "keyProvisions": [
      "ICJ Statute Articles 2-15",
      "Article 31 (Judges Ad Hoc)",
      "Peace Palace, The Hague, Netherlands"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-02-02",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-02",
    "number": 5,
    "order": 5,
    "title": "ICJ Jurisdiction: Contentious Cases, Advisory Opinions & Precedents",
    "summary": "Contentious jurisdiction requires state consent (compromissory clauses, special agreements, optional clause Art 36(2)); Advisory opinions (Art 96 UN Charter); Kulbhushan Jadhav case.",
    "keyProvisions": [
      "ICJ Statute Articles 36(2), 38(1), 65",
      "UN Charter Article 94 (Enforcement by SC)",
      "Jadhav Case (India v. Pakistan 2019)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-intl-03-01",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-03",
    "number": 6,
    "order": 6,
    "title": "Global Health & Labour Agencies: WHO & ILO",
    "summary": "World Health Organization (Geneva, World Health Assembly, International Health Regulations), International Labour Organization (Geneva, tripartite structure, 1919 Versailles).",
    "keyProvisions": [
      "WHO Constitution 1948",
      "ILO Constitution 1919 (Nobel Peace Prize 1969)",
      "Core Labour Conventions"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-03-02",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-03",
    "number": 7,
    "order": 7,
    "title": "UNESCO, FAO & Intellectual Property: Mandates & Headquarters",
    "summary": "UNESCO (Paris, World Heritage Committee), FAO (Rome, World Food Day Oct 16), WIPO (Geneva, PCT, Berne/Paris Conventions).",
    "keyProvisions": [
      "World Heritage Convention 1972",
      "FAO mandate",
      "WIPO Copyright and Patent treaties"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-03-03",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-03",
    "number": 8,
    "order": 8,
    "title": "UN Funds & Programmes: UNDP, UNEP & UNHCR",
    "summary": "UNDP (Human Development Report, HDI), UNEP (Nairobi, Global Environment Outlook), UNHCR (Geneva, 1951 Refugee Convention and 1967 Protocol).",
    "keyProvisions": [
      "UNEP headquarters in Nairobi, Kenya",
      "1951 Refugee Convention",
      "UNDP Human Development Index metrics"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-04-01",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-04",
    "number": 9,
    "order": 9,
    "title": "Bretton Woods Institutions: IMF & World Bank Group",
    "summary": "1944 Bretton Woods Conference, IMF (Special Drawing Rights, balance of payments assistance), World Bank Group (IBRD, IDA concessional window, IFC, MIGA, ICSID).",
    "keyProvisions": [
      "IMF Articles of Agreement",
      "Special Drawing Rights (SDR basket)",
      "World Bank Washington D.C. headquarters"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-04-02",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-04",
    "number": 10,
    "order": 10,
    "title": "World Trade Organization (WTO): Rules, TRIPS & Dispute Settlement",
    "summary": "Marrakesh Agreement 1994, Geneva, Most Favoured Nation (MFN), National Treatment, Agreement on Agriculture (Amber/Blue/Green boxes), TRIPS patent protections.",
    "keyProvisions": [
      "Marrakesh Agreement 1994",
      "TRIPS Agreement 20-year patent term",
      "WTO Dispute Settlement Body (DSB) Appellate Body"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-04-03",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-04",
    "number": 11,
    "order": 11,
    "title": "Emerging Development Banks: NDB, AIIB & ADB",
    "summary": "New Development Bank (BRICS Bank, Shanghai), Asian Infrastructure Investment Bank (Beijing, India 2nd largest shareholder), Asian Development Bank (Manila 1966).",
    "keyProvisions": [
      "NDB Fortaleza Declaration 2014",
      "AIIB Articles of Agreement 2015",
      "ADB headquarters in Mandaluyong/Manila"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-05-01",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-05",
    "number": 12,
    "order": 12,
    "title": "Universal Declaration of Human Rights 1948 & Core Covenants",
    "summary": "Adoption on December 10, 1948 (Human Rights Day), 30 articles, Eleanor Roosevelt, International Bill of Rights (UDHR, ICCPR 1966, ICESCR 1966).",
    "keyProvisions": [
      "UDHR Articles 1-30",
      "ICCPR (Civil & Political Rights)",
      "ICESCR (Economic, Social & Cultural Rights)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-05-02",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-05",
    "number": 13,
    "order": 13,
    "title": "UN Human Rights Council & Specialized Human Rights Treaties",
    "summary": "UNHRC Geneva (47 member states, Universal Periodic Review), CEDAW 1979, CRC 1989, Convention Against Torture (CAT), UN Special Rapporteurs.",
    "keyProvisions": [
      "UNGA Resolution 60/251 (establishing UNHRC)",
      "CEDAW 1979",
      "Universal Periodic Review (UPR) mechanism"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-06-01",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-06",
    "number": 14,
    "order": 14,
    "title": "Nuclear Non-Proliferation Treaty (NPT) & Comprehensive Test Ban (CTBT)",
    "summary": "NPT 1968 three pillars (non-proliferation, disarmament, peaceful use), 5 recognized nuclear states, non-signatories (India, Pakistan, Israel), CTBT 1996 Annex 2.",
    "keyProvisions": [
      "NPT 1968 entered into force 1970",
      "CTBT 1996 Annex 2 ratification requirement",
      "IAEA safeguards"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-06-02",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-06",
    "number": 15,
    "order": 15,
    "title": "Multilateral Export Control Regimes: MTCR, Wassenaar, Australia & NSG",
    "summary": "Missile Technology Control Regime (MTCR, 300 km/500 kg threshold, India joined 2016), Wassenaar Arrangement (dual-use goods), Australia Group (chemical/biological), Nuclear Suppliers Group (NSG).",
    "keyProvisions": [
      "MTCR guidelines",
      "Wassenaar Arrangement",
      "India accession to 3 of 4 regimes (except NSG)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-07-01",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-07",
    "number": 16,
    "order": 16,
    "title": "UNFCCC, Kyoto Protocol & Paris Climate Agreement",
    "summary": "UNFCCC 1992, Kyoto Protocol 1997 (Annex I binding emission cuts, Clean Development Mechanism), Paris Agreement 2015 (COP21, 1.5°C/2°C target, NDCs, CBDR-RC).",
    "keyProvisions": [
      "Paris Agreement 2015 Article 2",
      "Common But Differentiated Responsibilities (CBDR)",
      "Nationally Determined Contributions (NDCs)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-07-02",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-07",
    "number": 17,
    "order": 17,
    "title": "Biodiversity & Ozone Protection Treaties: CBD, Ramsar & Montreal",
    "summary": "Convention on Biological Diversity (CBD, Nagoya Protocol on ABS, Kunming-Montreal Framework), Ramsar Convention on Wetlands 1971, Montreal Protocol 1987 and Kigali Amendment 2016.",
    "keyProvisions": [
      "Montreal Protocol 1987 (HFC phase-down Kigali 2016)",
      "Ramsar Convention 1971 (Wetlands of International Importance)",
      "CBD Nagoya Protocol"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-08-01",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-08",
    "number": 18,
    "order": 18,
    "title": "The G20 Architecture & New Delhi Leaders' Declaration 2023",
    "summary": "G20 origin 1999/2008, Troika system, India's Presidency 2023 ('Vasudhaiva Kutumbakam'), admission of African Union (AU) as permanent member, Global Biofuels Alliance.",
    "keyProvisions": [
      "New Delhi Leaders Declaration 2023",
      "African Union permanent entry",
      "Green Development Pact for a Sustainable Future"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-08-02",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-08",
    "number": 19,
    "order": 19,
    "title": "BRICS Expansion & Shanghai Cooperation Organisation (SCO)",
    "summary": "BRICS origin (O'Neill acronym 2001, South Africa 2010), Johannesburg Summit 2023 expansion (Egypt, Ethiopia, Iran, UAE, Saudi Arabia), SCO origin 2001 (India and Pakistan joined 2017).",
    "keyProvisions": [
      "BRICS+ framework",
      "SCO Charter and RATS (Regional Anti-Terrorist Structure in Tashkent)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-08-03",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-08",
    "number": 20,
    "order": 20,
    "title": "Regional Formations: ASEAN, BIMSTEC, SAARC & Quad",
    "summary": "ASEAN (Bangkok Declaration 1967, 10 members), BIMSTEC (Bangkok Declaration 1997, 7 members), SAARC (Dhaka 1985, Kathmandu secretariat), Quad (India, US, Japan, Australia).",
    "keyProvisions": [
      "ASEAN Charter",
      "BIMSTEC Charter 2022",
      "SAARC Charter",
      "Quad Leaders joint vision for Free and Open Indo-Pacific"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-09-01",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-09",
    "number": 21,
    "order": 21,
    "title": "UNCLOS Maritime Zones & Coastal State Rights",
    "summary": "Baselines, Internal Waters, Territorial Sea (12 nautical miles, innocent passage), Contiguous Zone (24 nm, fiscal/customs/sanitary enforcement), Exclusive Economic Zone (200 nm sovereign rights over living/non-living resources).",
    "keyProvisions": [
      "UNCLOS 1982 Articles 3, 33, 56, 57",
      "Right of Innocent Passage (Article 17)",
      "Freedom of navigation on High Seas (Article 87)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-intl-09-02",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-09",
    "number": 22,
    "order": 22,
    "title": "Continental Shelf, High Seas & International Seabed Authority",
    "summary": "Continental Shelf up to 350 nm, High Seas as res communis, Common Heritage of Mankind doctrine for the Area, International Seabed Authority (ISA, Kingston, Jamaica).",
    "keyProvisions": [
      "UNCLOS Articles 76, 136 (Common Heritage of Mankind)",
      "International Seabed Authority (ISA)",
      "BBNJ High Seas Treaty 2023"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-10-01",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-10",
    "number": 23,
    "order": 23,
    "title": "India's Neighborhood First Policy & Maritime Doctrine (SAGAR)",
    "summary": "Neighborhood First priority development assistance, SAGAR (Security and Growth for All in the Region), Project Mausam, development partnerships with Nepal, Bhutan, Bangladesh, Sri Lanka.",
    "keyProvisions": [
      "SAGAR doctrine announced in Mauritius 2015",
      "Line of Credit development assistance",
      "Indo-Pacific Oceans Initiative (IPOI)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-10-02",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-10",
    "number": 24,
    "order": 24,
    "title": "Strategic Bilateral Ties & Foundational Defense Pacts",
    "summary": "India-US 2+2 Ministerial Dialogue, 4 foundational defense agreements: GSOMIA (2002), LEMOA (2016), COMCASA (2018), and BECA (2020); Strategic ties with France, Russia, Japan.",
    "keyProvisions": [
      "LEMOA (Logistics Exchange Memorandum of Agreement)",
      "COMCASA (Communications Compatibility and Security Agreement)",
      "BECA (Basic Exchange and Cooperation Agreement)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-11-01",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-11",
    "number": 25,
    "order": 25,
    "title": "Geneva Conventions 1949 & International Humanitarian Law",
    "summary": "Four Geneva Conventions 1949 (Wounded/Sick on land, at sea, Prisoners of War, Protection of Civilians), Common Article 3, Additional Protocols I, II, and III, Red Cross role.",
    "keyProvisions": [
      "Geneva Conventions I to IV of 1949",
      "Common Article 3 minimum humanitarian baseline",
      "Distinction and proportionality principles"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-11-02",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-11",
    "number": 26,
    "order": 26,
    "title": "UN Peacekeeping Operations & Responsibility to Protect (R2P)",
    "summary": "Chapter VI-and-a-half peacekeeping, three principles (consent of parties, impartiality, non-use of force except self-defense/mandate defense), India as largest cumulative troop contributor, R2P 2005 World Summit.",
    "keyProvisions": [
      "UN Department of Peace Operations (DPO)",
      "Blue Helmets mandate",
      "R2P pillars adopted at 2005 World Summit"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-11-03",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-11",
    "number": 27,
    "order": 27,
    "title": "International Criminal Court (ICC) & Rome Statute 1998",
    "summary": "Rome Statute 1998, ICC seat in The Hague, four core crimes (genocide, crimes against humanity, war crimes, aggression), principle of complementarity (Article 17).",
    "keyProvisions": [
      "Rome Statute of the ICC 1998",
      "Article 5 (Jurisdiction)",
      "Article 17 (Complementarity principle)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-12-01",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-12",
    "number": 28,
    "order": 28,
    "title": "Vienna Convention on Diplomatic Relations 1961: Core Principles",
    "summary": "Establishment of diplomatic missions, functions of mission (Art 3), inviolability of mission premises (Art 22), diplomatic pouch (Art 27), persona non grata (Art 9).",
    "keyProvisions": [
      "VCDR 1961 Articles 9, 22, 27, 29, 31",
      "Inviolability of diplomatic agent",
      "Immunity from criminal jurisdiction"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-12-02",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-12",
    "number": 29,
    "order": 29,
    "title": "Consular Relations & Vienna Convention on Consular Relations 1963",
    "summary": "Distinction between diplomatic and consular functions, Article 36 VCCR (consular communication and notification upon arrest of a foreign national), LaGrand case, Avena case, Jadhav case.",
    "keyProvisions": [
      "VCCR 1963 Article 36",
      "LaGrand Case (Germany v. US 2001)",
      "Jadhav Case (India v. Pakistan 2019)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-intl-12-03",
    "subjectId": "gk-international",
    "chapterId": "ch-intl-12",
    "number": 30,
    "order": 30,
    "title": "Territorial & Diplomatic Asylum: Principles & State Practice",
    "summary": "Territorial asylum (exercised within state territory pursuant to territorial sovereignty), diplomatic asylum (extra-territorial, recognized in Latin American regional law, Asylum Case - Colombia v. Peru 1950).",
    "keyProvisions": [
      "Asylum Case (Colombia v. Peru, ICJ 1950)",
      "Article 14 Universal Declaration of Human Rights",
      "Principle of Non-Refoulement"
    ],
    "estimatedMinutes": 20
  }
];
  global.INTERNATIONAL_TOPICS = INTERNATIONAL_TOPICS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { topics: INTERNATIONAL_TOPICS, INTERNATIONAL_TOPICS: INTERNATIONAL_TOPICS };
  }
})(typeof window !== 'undefined' ? window : global);
