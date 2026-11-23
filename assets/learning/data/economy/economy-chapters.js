/**
 * Tanveer Ashraf Judicial Prep - Indian Economy Chapters (Paper I General Knowledge)
 */

(function(global) {
  'use strict';

  var ECONOMY_CHAPTERS = [
  {
    "id": "ch-econ-01",
    "subjectId": "gk-economy",
    "number": 1, "order": 1,
    "title": "Structure of Indian Economy & National Income Accounting",
    "description": "Primary, Secondary, Tertiary sectors, GDP, GNP, NNP, GVA, Real vs Nominal, and NSO Base Year calculations.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-econ-02",
    "subjectId": "gk-economy",
    "number": 2, "order": 2,
    "title": "Economic Planning, Five-Year Plans & 1991 Economic Reforms",
    "description": "Historical trajectory of Five-Year Plans, Harrod-Domar, Mahalanobis models, 1991 LPG crisis, and NITI Aayog.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-econ-03",
    "subjectId": "gk-economy",
    "number": 3, "order": 3,
    "title": "Poverty, Inequality & Unemployment in India",
    "description": "Tendulkar & Rangarajan poverty methodologies, Gini coefficient, Lorenz curve, and structural types of unemployment.",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-econ-04",
    "subjectId": "gk-economy",
    "number": 4, "order": 4,
    "title": "Money, Banking & Financial System of India",
    "description": "Reserve Bank of India (1935), Bank Nationalisation (1969 & 1980), Commercial Banks, NBFCs, and Basel Norms.",
    "estimatedMinutes": 55
  },
  {
    "id": "ch-econ-05",
    "subjectId": "gk-economy",
    "number": 5, "order": 5,
    "title": "Monetary Policy, Inflation & Price Stability",
    "description": "Repo, Reverse Repo, SDF, MSF, CRR, SLR, WPI vs CPI, Flexible Inflation Targeting (4% ± 2%), and the MPC.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-econ-06",
    "subjectId": "gk-economy",
    "number": 6, "order": 6,
    "title": "Public Finance, Union Budget & Fiscal Policy",
    "description": "Direct and Indirect taxes, Revenue/Fiscal/Primary Deficits, FRBM Act 2003, and the unified GST architecture.",
    "estimatedMinutes": 55
  },
  {
    "id": "ch-econ-07",
    "subjectId": "gk-economy",
    "number": 7, "order": 7,
    "title": "Capital Markets, Money Market & Financial Regulators",
    "description": "SEBI statutory oversight, BSE/NSE, Treasury Bills, Commercial Paper, Mutual Funds, IRDAI, and PFRDA.",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-econ-08",
    "subjectId": "gk-economy",
    "number": 8, "order": 8,
    "title": "Agriculture, Food Security & Rural Economy",
    "description": "MSP determination (CACP), NFSA 2013, Public Distribution System, PM-KISAN, NABARD, and Priority Sector Lending.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-econ-09",
    "subjectId": "gk-economy",
    "number": 9, "order": 9,
    "title": "Industrial Sector, MSMEs & Disinvestment",
    "description": "Industrial policy resolutions (1948, 1956, 1991), revised MSME criteria (2020), Maharatna/Navratna CPSEs, and DIPAM.",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-econ-10",
    "subjectId": "gk-economy",
    "number": 10, "order": 10,
    "title": "Services Sector, Digital Economy & Infrastructure",
    "description": "IT-BPM dominance, UPI digital transactions (NPCI), PM Gati Shakti, National Infrastructure Pipeline, and InVITs.",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-econ-11",
    "subjectId": "gk-economy",
    "number": 11, "order": 11,
    "title": "External Sector, Balance of Payments & Foreign Trade",
    "description": "Current Account, Capital Account, Forex Reserves, Foreign Trade Policy, FDI automatic vs approval route, and FPI.",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-econ-12",
    "subjectId": "gk-economy",
    "number": 12, "order": 12,
    "title": "International Economic Organisations & Trade Pacts",
    "description": "Bretton Woods sisters (IMF & World Bank), WTO agreements (AoA, TRIPS), BRICS NDB, Asian Infrastructure Investment Bank.",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-econ-13",
    "subjectId": "gk-economy",
    "number": 13, "order": 13,
    "title": "Economy of Uttar Pradesh: Growth, ODOP & Fiscal Health",
    "description": "UP One Trillion Dollar economy vision, GSDP dynamics, One District One Product (ODOP), and UP State Budget priorities.",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-econ-14",
    "subjectId": "gk-economy",
    "number": 14, "order": 14,
    "title": "Sustainable Development, Green Economy & Financial Inclusion",
    "description": "NITI Aayog SDG India Index, Panchamrit net-zero commitments, Pradhan Mantri Jan Dhan Yojana (JAM Trinity), and PM MUDRA.",
    "estimatedMinutes": 45
  }
];

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { chapters: ECONOMY_CHAPTERS };
  } else {
    global.ECONOMY_CHAPTERS = ECONOMY_CHAPTERS;
  }
})(typeof window !== 'undefined' ? window : global);
