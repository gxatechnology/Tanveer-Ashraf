/**
 * Tanveer Ashraf Judicial Prep - Current National Issues Topics (Paper I General Knowledge)
 */
(function(global) {
  'use strict';
  var CURRENT_TOPICS = [
  {
    "id": "top-curr-01-01",
    "chapterId": "ch-curr-01",
    "subjectId": "gk-current",
    "title": "Public Service Delivery Reforms, Citizen Charters & Mission Karmayogi",
    "subtitle": "Capacity Building Commission, iGOT Karmayogi Portal, Janhit Guarantee & Administrative Accountability"
  },
  {
    "id": "top-curr-01-02",
    "chapterId": "ch-curr-01",
    "subjectId": "gk-current",
    "title": "Good Governance Index (GGI) & Centralized Public Grievance Redressal (CPGRAMS)",
    "subtitle": "DARPG Governance Framework, 10 Sectors GGI, Sevottam Model & 30-Day Redressal Mandate"
  },
  {
    "id": "top-curr-02-01",
    "chapterId": "ch-curr-02",
    "subjectId": "gk-current",
    "title": "Landmark Supreme Court Verdicts on Federalism, Article 370 & Electoral Bonds",
    "subtitle": "In Re Article 370 (Asymmetric Federalism), ADR v. UOI (Right to Information & Section 29C RPA), Governor Assent Timelines"
  },
  {
    "id": "top-curr-02-02",
    "chapterId": "ch-curr-02",
    "subjectId": "gk-current",
    "title": "Reservation Jurisprudence: Sub-Classification of SCs/STs & Creamy Layer",
    "subtitle": "State of Punjab v. Davinder Singh (7-Judge Bench Overruling E.V. Chinnaiah), Art. 341/342 & Affirmative Action Nuances"
  },
  {
    "id": "top-curr-02-03",
    "chapterId": "ch-curr-02",
    "subjectId": "gk-current",
    "title": "Constitutional Dimensions of Same-Sex Marriage & Right to Privacy Precedents",
    "subtitle": "Supriyo v. Union of India (SMA Interpretation), Recognition of Civil Unions & Article 21 Dignity Jurisprudence"
  },
  {
    "id": "top-curr-03-01",
    "chapterId": "ch-curr-03",
    "subjectId": "gk-current",
    "title": "Implementation of Bharatiya Nyaya Sanhita (BNS), BNSS & BSA 2023",
    "subtitle": "Effective 1 July 2024 (Except S. 106(2) BNS), Mandatory Videography (S. 105 BNSS), Zero FIR, Electronic Records (S. 61 BSA)"
  },
  {
    "id": "top-curr-03-02",
    "chapterId": "ch-curr-03",
    "subjectId": "gk-current",
    "title": "Digital Personal Data Protection (DPDP) Act 2023: Rights, Duties & Data Protection Board",
    "subtitle": "Data Fiduciary Obligations, Consent Framework, Rights of Data Principal, Cross-Border Transfers & Section 33 Penalties"
  },
  {
    "id": "top-curr-03-03",
    "chapterId": "ch-curr-03",
    "subjectId": "gk-current",
    "title": "Telecommunications Act 2023 & e-Courts Mission Mode Project Phase III",
    "subtitle": "Repeal of 1885 Act, Biometric Verification, Unified Spectrum Framework, NJDG Upgrades & AI in Judicial Administration"
  },
  {
    "id": "top-curr-04-01",
    "chapterId": "ch-curr-04",
    "subjectId": "gk-current",
    "title": "Union Budget Framework & Capital Expenditure (Capex) Thrust",
    "subtitle": "Fiscal Deficit Consolidation Path, Capex Growth (INR 11.11 Lakh Cr), Tax Slab Rationalisation & Infrastructure Multipliers"
  },
  {
    "id": "top-curr-04-02",
    "chapterId": "ch-curr-04",
    "subjectId": "gk-current",
    "title": "PM Gati Shakti National Master Plan, Logistics Policy & Production Linked Incentives (PLI)",
    "subtitle": "Multi-Modal Connectivity, 14 Strategic PLI Sectors, National Logistics Policy Targets & Logistics Performance Index (LPI)"
  },
  {
    "id": "top-curr-05-01",
    "chapterId": "ch-curr-05",
    "subjectId": "gk-current",
    "title": "Ayushman Bharat PM-JAY & Digital Health Mission (ABDM)",
    "subtitle": "INR 5 Lakh Health Cover, Ayushman Arogya Mandir, ABHA Health IDs, Universal Healthcare Coverage for Citizens 70+"
  },
  {
    "id": "top-curr-05-02",
    "chapterId": "ch-curr-05",
    "subjectId": "gk-current",
    "title": "Welfare Architectures: Jal Jeevan Mission, PM Awas Yojana & PM Vishwakarma",
    "subtitle": "Har Ghar Jal Targets, Housing for All (Gramin & Urban), Traditional Artisans Credit Support & Collateral-Free Loans"
  },
  {
    "id": "top-curr-05-03",
    "chapterId": "ch-curr-05",
    "subjectId": "gk-current",
    "title": "Social Empowerment Schemes for Women, Senior Citizens & Divyangjan",
    "subtitle": "PM Matru Vandana Yojana, Lakhpati Didi, Atal Vayo Abhyuday Yojana (AVYAY) & Accessible India Campaign Standards"
  },
  {
    "id": "top-curr-06-01",
    "chapterId": "ch-curr-06",
    "subjectId": "gk-current",
    "title": "India's Panchamrit Climate Pledges, Nationally Determined Contributions (NDCs) & Mission LiFE",
    "subtitle": "Net-Zero by 2070, 500 GW Non-Fossil Capacity by 2030, 45% Emission Intensity Cut & Lifestyle for Environment"
  },
  {
    "id": "top-curr-06-02",
    "chapterId": "ch-curr-06",
    "subjectId": "gk-current",
    "title": "National Green Hydrogen Mission & Renewable Energy Transition",
    "subtitle": "5 MMT Annual Production Target by 2030, SIGHT Programme, PM Surya Ghar Muft Bijli Yojana & Solar Parks"
  },
  {
    "id": "top-curr-06-03",
    "chapterId": "ch-curr-06",
    "subjectId": "gk-current",
    "title": "Wildlife Conservation: 50 Years of Project Tiger, Project Cheetah & NGT Precedents",
    "subtitle": "National Tiger Conservation Authority (NTCA), Kuno National Park Cheetah Reintroduction & Key Ecological Directives"
  },
  {
    "id": "top-curr-07-01",
    "chapterId": "ch-curr-07",
    "subjectId": "gk-current",
    "title": "Digital Public Infrastructure (DPI): Global Expansion of UPI, DigiLocker & ONDC",
    "subtitle": "Cross-Border UPI Links (Singapore PayNow, UAE, France), Open Network for Digital Commerce (ONDC) & DPI Leadership"
  },
  {
    "id": "top-curr-07-02",
    "chapterId": "ch-curr-07",
    "subjectId": "gk-current",
    "title": "National Quantum Mission (NQM), Semiconductor Mission & ANRF Act 2023",
    "subtitle": "Quantum Computing/QKD Hubs, India Semiconductor Mission (ISM), Micron Sanand Plant & R&D Funding Restructuring"
  },
  {
    "id": "top-curr-08-01",
    "chapterId": "ch-curr-08",
    "subjectId": "gk-current",
    "title": "Uttar Pradesh Governance: One Trillion Dollar Economy Roadmap & ODOP Scaling",
    "subtitle": "Sectoral Growth Targets, UP Global Investors Summit Realisations, One District One Product (ODOP) & Export Hubs"
  },
  {
    "id": "top-curr-08-02",
    "chapterId": "ch-curr-08",
    "subjectId": "gk-current",
    "title": "UP Infrastructure: Expressways, Defence Industrial Corridor & Airport Network",
    "subtitle": "Purvanchal, Bundelkhand & Ganga Expressways, 6 Defence Nodes (Aligarh, Agra, Kanpur, Lucknow, Jhansi, Chitrakoot), Jewar Airport"
  },
  {
    "id": "top-curr-08-03",
    "chapterId": "ch-curr-08",
    "subjectId": "gk-current",
    "title": "UP Judicial Administration: Allahabad High Court Digitisation & Fast Track Courts",
    "subtitle": "Fast Track Special Courts (FTSC POCSO), Digital Courtrooms, District Judiciary Infrastructure & UP Janhit Guarantee"
  },
  {
    "id": "top-curr-09-01",
    "chapterId": "ch-curr-09",
    "subjectId": "gk-current",
    "title": "NITI Aayog National Multidimensional Poverty Index (MPI) & SDG India Index",
    "subtitle": "13.5 Crore Escaped Multidimensional Poverty (2015-16 to 2019-21), 12 MPI Indicators, UP's Steepest Poverty Reduction"
  },
  {
    "id": "top-curr-09-02",
    "chapterId": "ch-curr-09",
    "subjectId": "gk-current",
    "title": "Law Commission of India: 22nd Commission Reports & Judicial Reform Recommendations",
    "subtitle": "Simultaneous Elections (One Nation One Election), Criminal Law Reforms, Adverse Possession, Civil Law Upgrades"
  },
  {
    "id": "top-curr-10-01",
    "chapterId": "ch-curr-10",
    "subjectId": "gk-current",
    "title": "Chronological Legal & National Events Dossier (Recent Milestone Developments)",
    "subtitle": "Constitutional Appointments, Important High-Level Committees, National Honours (Bharat Ratna), Major Inter-State River Tribunals"
  },
  {
    "id": "top-curr-10-02",
    "chapterId": "ch-curr-10",
    "subjectId": "gk-current",
    "title": "High-Yield Facts Capsule: Prelims Rapid Recall for Current National Issues",
    "subtitle": "Key Headings, Chairpersons, Statutorily Mandated Deadlines, International Summits Hosted by India & Key Treaties"
  }
];
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { topics: CURRENT_TOPICS, CURRENT_TOPICS: CURRENT_TOPICS };
  } else {
    global.CURRENT_TOPICS = CURRENT_TOPICS;
  }
})(typeof window !== 'undefined' ? window : global);
