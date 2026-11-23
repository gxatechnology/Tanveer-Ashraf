/**
 * Tanveer Ashraf Judicial Prep - Technology Chapters (Paper I General Knowledge)
 */
(function(global) {
  'use strict';
  var TECH_CHAPTERS = [
  {
    "id": "ch-tech-01",
    "subjectId": "gk-tech",
    "number": 1,
    "order": 1,
    "title": "Artificial Intelligence, Machine Learning & Deep Learning",
    "description": "AI hierarchy, machine learning algorithms (supervised, unsupervised, reinforcement), neural networks, generative AI, LLMs, and IndiaAI Mission.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-tech-02",
    "subjectId": "gk-tech",
    "number": 2,
    "order": 2,
    "title": "Digital Public Infrastructure (DPI) & India Stack",
    "description": "Identity layer (Aadhaar), payments layer (UPI, NPCI), data exchange layer (DigiLocker, Account Aggregator), and ONDC open network commerce.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-tech-03",
    "subjectId": "gk-tech",
    "number": 3,
    "order": 3,
    "title": "E-Courts Project, Court Digitisation & Legal Tech",
    "description": "e-Courts Phases I, II, and III, National Judicial Data Grid (NJDG), Interoperable Criminal Justice System (ICJS), virtual courts, e-filing, and AI in judiciary (SUVAS, SUPACE).",
    "estimatedMinutes": 55
  },
  {
    "id": "ch-tech-04",
    "subjectId": "gk-tech",
    "number": 4,
    "order": 4,
    "title": "Cybersecurity, Threat Landscape & CERT-In Framework",
    "description": "Malware types (ransomware, spyware, trojans), phishing, zero-day vulnerabilities, CERT-In directions, National Cyber Security Policy, and critical infrastructure (NCIIPC).",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-tech-05",
    "subjectId": "gk-tech",
    "number": 5,
    "order": 5,
    "title": "Information Technology Act 2000 & Cyber Forensics",
    "description": "IT Act 2000 digital signatures, electronic governance, Section 66 offenses, Section 69A blocking orders, Section 79 intermediary guidelines, Shreya Singhal case, digital evidence.",
    "estimatedMinutes": 55
  },
  {
    "id": "ch-tech-06",
    "subjectId": "gk-tech",
    "number": 6,
    "order": 6,
    "title": "Data Privacy & Digital Personal Data Protection Act 2023",
    "description": "DPDP Act 2023 principles, Data Principal rights, Data Fiduciary obligations, Data Protection Board of India, cross-border transfers, consent mechanisms, Puttaswamy ruling.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-tech-07",
    "subjectId": "gk-tech",
    "number": 7,
    "order": 7,
    "title": "Blockchain, Cryptocurrencies & Central Bank Digital Currency",
    "description": "Distributed ledger technology, consensus mechanisms (PoW vs PoS), smart contracts, RBI Digital Rupee (e-Rupee CBDC wholesale & retail), taxation of Virtual Digital Assets.",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-tech-08",
    "subjectId": "gk-tech",
    "number": 8,
    "order": 8,
    "title": "Biotechnology, Gene Editing & CRISPR-Cas9",
    "description": "Recombinant DNA technology, CRISPR-Cas9 gene editing tool, GM crops in India (Bt Cotton, DMH-11 mustard), Genetic Engineering Appraisal Committee (GEAC).",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-tech-09",
    "subjectId": "gk-tech",
    "number": 9,
    "order": 9,
    "title": "Semiconductors, Supercomputing & Quantum Technologies",
    "description": "India Semiconductor Mission (ISM), semiconductor fabrication, National Supercomputing Mission (PARAM supercomputers - PARAM Shivay, PARAM Pravega), National Quantum Mission (NQM).",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-tech-10",
    "subjectId": "gk-tech",
    "number": 10,
    "order": 10,
    "title": "Clean Tech, Electric Vehicles & Green Hydrogen Mission",
    "description": "National Green Hydrogen Mission, FAME India scheme, battery technologies (lithium-ion, solid-state), solar photovoltaic cells, and carbon capture.",
    "estimatedMinutes": 45
  }
];
  global.TECH_CHAPTERS = TECH_CHAPTERS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { chapters: TECH_CHAPTERS, TECH_CHAPTERS: TECH_CHAPTERS };
  }
})(typeof window !== 'undefined' ? window : global);
