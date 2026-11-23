/**
 * Tanveer Ashraf Judicial Prep - Technology Topics (Paper I General Knowledge)
 */
(function(global) {
  'use strict';
  var TECH_TOPICS = [
  {
    "id": "top-tech-01-01",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-01",
    "number": 1,
    "order": 1,
    "title": "Fundamentals of Artificial Intelligence & Machine Learning",
    "summary": "Distinction between AI, ML, Deep Learning, supervised vs unsupervised learning, neural network layers, natural language processing (NLP).",
    "keyProvisions": [
      "AI hierarchy",
      "Supervised vs Unsupervised ML",
      "IndiaAI Mission 2024 (INR 10,372 Cr outlay)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-01-02",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-01",
    "number": 2,
    "order": 2,
    "title": "Generative AI, Large Language Models & Responsible AI",
    "summary": "Transformer architecture, generative pre-trained models, hallucinations, deepfakes, copyright in AI training data, NITI Aayog Responsible AI principles.",
    "keyProvisions": [
      "Generative AI transformers",
      "Deepfake regulations under IT Rules",
      "NITI Aayog Responsible AI for All (2021)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-01-03",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-01",
    "number": 3,
    "order": 3,
    "title": "AI in Public Administration & Judicial Operations",
    "summary": "SUVAS (Supreme Court Vidhik Anuvaad Software) translation tool, SUPACE (Supreme Court Portal for Assistance in Court's Efficiency), automated case management.",
    "keyProvisions": [
      "SUVAS AI vernacular translation",
      "SUPACE efficiency portal",
      "Phase III e-Courts AI integration"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-02-01",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-02",
    "number": 4,
    "order": 4,
    "title": "Aadhaar & The Identity Layer of India Stack",
    "summary": "Aadhaar Act 2016, 12-digit unique biometric identification, UIDAI, Virtual ID, offline verification, K.S. Puttaswamy (Aadhaar 2018) constitutionality ruling.",
    "keyProvisions": [
      "Aadhaar Act 2016 as amended 2019",
      "UIDAI statutory authority",
      "Justice K.S. Puttaswamy v. UOI (2018) 5-judge bench"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-02-02",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-02",
    "number": 5,
    "order": 5,
    "title": "Unified Payments Interface (UPI) & Digital Payments Architecture",
    "summary": "NPCI architecture, immediate real-time payments, virtual payment address (VPA), 2-factor authentication, UPI 123Pay, UPI Lite, international cross-border linkages.",
    "keyProvisions": [
      "NPCI (umbrella organization under Payment and Settlement Systems Act 2007)",
      "UPI interoperability",
      "Cross-border UPI-PayNow linkage"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-02-03",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-02",
    "number": 6,
    "order": 6,
    "title": "Data Exchange Layer: DigiLocker & Account Aggregator",
    "summary": "DigiLocker legal validity under Rule 9A of IT Rules 2016, cloud storage of authentic documents, RBI Account Aggregator (AA) framework for consented financial data sharing.",
    "keyProvisions": [
      "DigiLocker (IT Rules 2016 Rule 9A equivalency to original)",
      "Account Aggregator framework (RBI)",
      "ONDC open e-commerce protocol"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-03-01",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-03",
    "number": 7,
    "order": 7,
    "title": "e-Courts Project: Architecture, Phases & Funding",
    "summary": "e-Committee of the Supreme Court of India, Phase I (computerisation), Phase II (cloud infrastructure & VC), Phase III (INR 7,210 Cr outlay, paperless courts, open APIs).",
    "keyProvisions": [
      "e-Committee Supreme Court of India",
      "e-Courts Phase III Cabinet approval (2023)",
      "Centrally Sponsored Scheme"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-03-02",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-03",
    "number": 8,
    "order": 8,
    "title": "National Judicial Data Grid (NJDG) & Virtual Courts",
    "summary": "Real-time case tracking, pendency monitoring, NJDG integration with Supreme Court portal, virtual traffic courts, online summary disposal.",
    "keyProvisions": [
      "NJDG national portal",
      "Virtual Courts under Motor Vehicles Act Section 208",
      "e-Pay judicial court fee integration"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-03-03",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-03",
    "number": 9,
    "order": 9,
    "title": "Interoperable Criminal Justice System (ICJS)",
    "summary": "Seamless data exchange across the five pillars: Police (CCTNS), e-Forensics, e-Prosecution, e-Courts, and e-Prisons under Ministry of Home Affairs.",
    "keyProvisions": [
      "ICJS Phase II implementation",
      "CCTNS integration",
      "MHA project oversight"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-04-01",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-04",
    "number": 10,
    "order": 10,
    "title": "Cyber Threat Vectors: Ransomware, Spyware & Zero-Day Exploits",
    "summary": "Malware taxonomy, ransomware extortion models (WannaCry), spyware (Pegasus), trojans, distributed denial of service (DDoS), phishing, social engineering.",
    "keyProvisions": [
      "Malware vs Ransomware definition",
      "Zero-day vulnerability lifecycle",
      "NCIIPC Critical Information Infrastructure protection"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-04-02",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-04",
    "number": 11,
    "order": 11,
    "title": "CERT-In Mandates & National Cybersecurity Framework",
    "summary": "Indian Computer Emergency Response Team (CERT-In) under Section 70B of IT Act, mandatory 6-hour cybersecurity incident reporting, log retention rules.",
    "keyProvisions": [
      "Section 70B IT Act 2000",
      "CERT-In 2022 cybersecurity directions (6-hour reporting)",
      "National Cyber Coordination Centre (NCCC)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-05-01",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-05",
    "number": 12,
    "order": 12,
    "title": "Information Technology Act 2000: Architecture & Penal Provisions",
    "summary": "Enacted May 2000 based on UNCITRAL Model Law, legal recognition of electronic records, cyber offenses: hacking (Sec 66), identity theft (Sec 66C), voyeurism (Sec 66E), cyber terrorism (Sec 66F).",
    "keyProvisions": [
      "IT Act 2000 Sections 2, 4, 65, 66, 66C, 66E, 66F",
      "UNCITRAL Model Law on Electronic Commerce 1996"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-05-02",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-05",
    "number": 13,
    "order": 13,
    "title": "Intermediary Liability & Shreya Singhal Jurisprudence",
    "summary": "Section 79 safe harbor for online intermediaries, Section 66A struck down in Shreya Singhal v. Union of India (2015), Section 69A blocking orders, IT Intermediary Rules 2021.",
    "keyProvisions": [
      "Shreya Singhal v. Union of India (2015) 5 SCC 1",
      "Section 66A invalidation under Art 19(1)(a)",
      "IT Intermediary Rules 2021 (grievance officer, compliance)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-05-03",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-05",
    "number": 14,
    "order": 14,
    "title": "Electronic Evidence & Digital Forensics Standards",
    "summary": "Admissibility of electronic records (former Section 65B Indian Evidence Act 1872, now Section 63 Bharatiya Sakshya Adhiniyam 2023), Arjun Panditrao Khotkar precedent, chain of custody.",
    "keyProvisions": [
      "Section 63 BSA 2023 (replacing Sec 65B IEA)",
      "Arjun Panditrao Khotkar v. Kailash Kushanrao Gorantyal (2020) 3-judge bench",
      "Hash value integrity"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-tech-06-01",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-06",
    "number": 15,
    "order": 15,
    "title": "Digital Personal Data Protection Act 2023: Key Principles",
    "summary": "Enacted August 2023, applies to digital personal data, key actors: Data Principal, Data Fiduciary, Significant Data Fiduciary, Consent Manager, lawful processing grounds, notice requirements.",
    "keyProvisions": [
      "DPDP Act 2023 Sections 2, 4, 6, 8, 10",
      "Notice and Consent framework",
      "Child personal data processing safeguards (Section 9)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-06-02",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-06",
    "number": 16,
    "order": 16,
    "title": "Data Protection Board of India & Cross-Border Transfers",
    "summary": "Data Protection Board of India (DPBI) constitution, powers of adjudication, financial penalties up to INR 250 Cr for significant breaches, blacklisting/whitelisting mechanism for cross-border data flows.",
    "keyProvisions": [
      "DPDP Act 2023 Sections 18-28 (DPBI)",
      "Penalties Schedule (up to Rs 250 crore)",
      "Appeals to TDSAT (Section 29)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-07-01",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-07",
    "number": 17,
    "order": 17,
    "title": "Blockchain Architecture & Smart Contracts",
    "summary": "Distributed ledger technology, cryptographic hashing (SHA-256), immutability, consensus algorithms (Proof of Work vs Proof of Stake), smart contracts self-executing code.",
    "keyProvisions": [
      "Blockchain block structure (hash, previous hash, timestamp, data)",
      "Consensus protocols",
      "Smart contract enforceability under Indian Contract Act 1872"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-07-02",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-07",
    "number": 18,
    "order": 18,
    "title": "Central Bank Digital Currency (CBDC) & Crypto Regulation",
    "summary": "RBI Digital Rupee (e-Rupee), legal tender under RBI Act 1934 Section 22 amended, Wholesale (e₹-W) and Retail (e₹-R) pilots, Internet and Mobile Association of India v. RBI (2020), 30% tax on VDAs under Income Tax Act Section 115BBH.",
    "keyProvisions": [
      "RBI Act 1934 Section 22 amendment (CBDC legal tender)",
      "IMAI v. RBI (2020) banking circular struck down",
      "Finance Act 2022 Section 115BBH (30% VDA tax)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-08-01",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-08",
    "number": 19,
    "order": 19,
    "title": "CRISPR-Cas9 Gene Editing & Recombinant DNA",
    "summary": "Clustered Regularly Interspaced Short Palindromic Repeats, Cas9 molecular scissors, guide RNA, Nobel Prize in Chemistry 2020 (Doudna and Charpentier), genetic disease therapeutics.",
    "keyProvisions": [
      "CRISPR-Cas9 mechanism",
      "2020 Nobel Prize in Chemistry",
      "Somatic vs germline gene editing ethical boundaries"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-08-02",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-08",
    "number": 20,
    "order": 20,
    "title": "Genetically Modified Organisms & Regulatory Oversight",
    "summary": "Genetic Engineering Appraisal Committee (GEAC) under Ministry of Environment, Forest and Climate Change, Bt Cotton commercial release, DMH-11 hybrid mustard clearance.",
    "keyProvisions": [
      "Environment (Protection) Act 1986 Rules 1989",
      "GEAC statutory authority",
      "Bt Cotton (Cry1Ac and Cry2Ab genes)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-09-01",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-09",
    "number": 21,
    "order": 21,
    "title": "India Semiconductor Mission & Chip Fabrication",
    "summary": "Semiconductor supply chain, silicon wafers, photolithography, front-end fabrication vs back-end ATMP/OSAT, India Semiconductor Mission (ISM) INR 76,000 Cr incentive scheme.",
    "keyProvisions": [
      "India Semiconductor Mission (ISM)",
      "Fiscal support up to 50% project cost",
      "Dholera and Sanand semiconductor facilities"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-09-02",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-09",
    "number": 22,
    "order": 22,
    "title": "National Supercomputing Mission (NSM)",
    "summary": "Joint initiative of MeitY and DST, executed by C-DAC and IISc Bangalore, indigenous supercomputers (PARAM Shivay, PARAM Shakti, PARAM Pravega, PARAM Siddhi-AI), PetaFLOPS benchmarks.",
    "keyProvisions": [
      "National Supercomputing Mission",
      "C-DAC indigenous assembly",
      "PARAM series computing capability"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-09-03",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-09",
    "number": 23,
    "order": 23,
    "title": "National Quantum Mission (NQM) & Quantum Computing",
    "summary": "Quantum mechanics principles: superposition, quantum entanglement, qubits, National Quantum Mission approved 2023 (INR 6,003 Cr outlay), quantum communication, QKD (Quantum Key Distribution).",
    "keyProvisions": [
      "National Quantum Mission 2023-2031",
      "Superposition and Entanglement principles",
      "Quantum Key Distribution (QKD)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-10-01",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-10",
    "number": 24,
    "order": 24,
    "title": "National Green Hydrogen Mission & Electrolyser Tech",
    "summary": "Green hydrogen produced via water electrolysis using renewable power, Green Hydrogen Mission (INR 19,744 Cr outlay, 5 MMT annual production by 2030), SIGHT program.",
    "keyProvisions": [
      "National Green Hydrogen Mission 2023",
      "SIGHT (Strategic Interventions for Green Hydrogen Transition)",
      "Types: Grey, Blue, Green Hydrogen"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-10-02",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-10",
    "number": 25,
    "order": 25,
    "title": "Electric Mobility & Battery Energy Storage Technologies",
    "summary": "FAME India scheme (Faster Adoption and Manufacturing of Electric Vehicles), lithium-ion batteries (cathode materials LiCoO2, LFP), solid-state batteries, PLI scheme for Advanced Chemistry Cells (ACC).",
    "keyProvisions": [
      "FAME II Scheme guidelines",
      "PLI Scheme for National Programme on Advanced Chemistry Cell (ACC)",
      "Battery safety standards (AIS 038 & AIS 156)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-tech-10-03",
    "subjectId": "gk-tech",
    "chapterId": "ch-tech-10",
    "number": 26,
    "order": 26,
    "title": "Solar Photovoltaic & Renewable Energy Technologies",
    "summary": "Solar PV cells (silicon p-n junction, photoelectric effect), PM Surya Ghar Muft Bijli Yojana, floating solar power plants, International Solar Alliance (ISA, Gurugram).",
    "keyProvisions": [
      "PM Surya Ghar Muft Bijli Yojana (1 crore households)",
      "International Solar Alliance (ISA) headquarters in Gurugram, India",
      "500 GW non-fossil energy target by 2030"
    ],
    "estimatedMinutes": 20
  }
];
  global.TECH_TOPICS = TECH_TOPICS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { topics: TECH_TOPICS, TECH_TOPICS: TECH_TOPICS };
  }
})(typeof window !== 'undefined' ? window : global);
