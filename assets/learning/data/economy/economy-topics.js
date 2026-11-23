/**
 * Tanveer Ashraf Judicial Prep - Indian Economy Topics (Paper I General Knowledge)
 */

(function(global) {
  'use strict';

  var ECONOMY_TOPICS = [
  {
    "id": "top-econ-01-01",
    "chapterId": "ch-econ-01",
    "order": 1,
    "title": "Sectors of the Indian Economy: Primary, Secondary, Tertiary & Quaternary Transitions",
    "estimatedMinutes": 17
  },
  {
    "id": "top-econ-01-02",
    "chapterId": "ch-econ-01",
    "order": 2,
    "title": "National Income Aggregates: GDP, GNP, NNP, National Income at Factor Cost vs Market Price",
    "estimatedMinutes": 17
  },
  {
    "id": "top-econ-01-03",
    "chapterId": "ch-econ-01",
    "order": 3,
    "title": "Gross Value Added (GVA), Real vs Nominal GDP, GDP Deflator & NSO Base Year Methodology",
    "estimatedMinutes": 16
  },
  {
    "id": "top-econ-02-01",
    "chapterId": "ch-econ-02",
    "order": 1,
    "title": "Evolution of Economic Planning in India: National Planning Committee (1938), Bombay Plan & First Three FYPs",
    "estimatedMinutes": 17
  },
  {
    "id": "top-econ-02-02",
    "chapterId": "ch-econ-02",
    "order": 2,
    "title": "Five-Year Plans from 4th to 12th Plan: Gadgil Formula, Rolling Plan & Target Achievements",
    "estimatedMinutes": 17
  },
  {
    "id": "top-econ-02-03",
    "chapterId": "ch-econ-02",
    "order": 3,
    "title": "The 1991 Economic Crisis, Balance of Payments Shock & LPG Structural Reforms (Rao-Manmohan Model)",
    "estimatedMinutes": 16
  },
  {
    "id": "top-econ-03-01",
    "chapterId": "ch-econ-03",
    "order": 1,
    "title": "Poverty Estimation in India: Lakdawala, Suresh Tendulkar & C. Rangarajan Methodologies & Multi-dimensional Poverty (MPI)",
    "estimatedMinutes": 23
  },
  {
    "id": "top-econ-03-02",
    "chapterId": "ch-econ-03",
    "order": 2,
    "title": "Inequality & Unemployment: Lorenz Curve, Gini Coefficient, Types of Unemployment & PLFS Survey Metrics",
    "estimatedMinutes": 22
  },
  {
    "id": "top-econ-04-01",
    "chapterId": "ch-econ-04",
    "order": 1,
    "title": "Reserve Bank of India (RBI): Hilton Young Commission, RBI Act 1934, Central Banking Functions & Balance Sheet",
    "estimatedMinutes": 19
  },
  {
    "id": "top-econ-04-02",
    "chapterId": "ch-econ-04",
    "order": 2,
    "title": "Commercial Banking in India: 14 Banks Nationalisation (1969), 1980 Wave, Consolidation & Regional Rural Banks (RRBs)",
    "estimatedMinutes": 18
  },
  {
    "id": "top-econ-04-03",
    "chapterId": "ch-econ-04",
    "order": 3,
    "title": "Non-Performing Assets (NPAs), Insolvency and Bankruptcy Code (IBC 2016), SARFAESI Act & Basel III Capital Norms",
    "estimatedMinutes": 18
  },
  {
    "id": "top-econ-05-01",
    "chapterId": "ch-econ-05",
    "order": 1,
    "title": "Monetary Policy Instruments: Quantitative Tools (CRR, SLR, Repo, Reverse Repo, SDF, MSF & Open Market Operations)",
    "estimatedMinutes": 17
  },
  {
    "id": "top-econ-05-02",
    "chapterId": "ch-econ-05",
    "order": 2,
    "title": "Monetary Policy Committee (MPC), Flexible Inflation Targeting (4% ± 2%) & Urjit Patel Committee Framework",
    "estimatedMinutes": 16
  },
  {
    "id": "top-econ-05-03",
    "chapterId": "ch-econ-05",
    "order": 3,
    "title": "Inflation Dynamics in India: Wholesale Price Index (WPI) vs Consumer Price Index (CPI), Headline vs Core Inflation",
    "estimatedMinutes": 17
  },
  {
    "id": "top-econ-06-01",
    "chapterId": "ch-econ-06",
    "order": 1,
    "title": "Structure of Union Budget: Revenue Account, Capital Account, Direct Taxes & Indirect Tax Architecture",
    "estimatedMinutes": 19
  },
  {
    "id": "top-econ-06-02",
    "chapterId": "ch-econ-06",
    "order": 2,
    "title": "Deficit Indicators: Revenue Deficit, Effective Revenue Deficit, Fiscal Deficit, Primary Deficit & Deficit Financing",
    "estimatedMinutes": 18
  },
  {
    "id": "top-econ-06-03",
    "chapterId": "ch-econ-06",
    "order": 3,
    "title": "Fiscal Responsibility and Budget Management Act (FRBM 2003), N.K. Singh Review & Goods and Services Tax (GST)",
    "estimatedMinutes": 18
  },
  {
    "id": "top-econ-07-01",
    "chapterId": "ch-econ-07",
    "order": 1,
    "title": "Money Market Instruments in India: Call Money, Treasury Bills (91, 182, 364 Days), Commercial Paper & Certificates of Deposit",
    "estimatedMinutes": 23
  },
  {
    "id": "top-econ-07-02",
    "chapterId": "ch-econ-07",
    "order": 2,
    "title": "Capital Markets & Regulators: SEBI (1992), Primary vs Secondary Markets, BSE, NSE, Derivatives, IRDAI & PFRDA",
    "estimatedMinutes": 22
  },
  {
    "id": "top-econ-08-01",
    "chapterId": "ch-econ-08",
    "order": 1,
    "title": "Minimum Support Price (MSP): Commission for Agricultural Costs and Prices (CACP), Formulae (A2, A2+FL, C2) & Fair Remunerative Price (FRP)",
    "estimatedMinutes": 17
  },
  {
    "id": "top-econ-08-02",
    "chapterId": "ch-econ-08",
    "order": 2,
    "title": "Food Security & Public Distribution: Food Corporation of India (FCI), National Food Security Act 2013 & Buffer Stock Norms",
    "estimatedMinutes": 17
  },
  {
    "id": "top-econ-08-03",
    "chapterId": "ch-econ-08",
    "order": 3,
    "title": "Agricultural Credit, NABARD (1982), Kisan Credit Card (KCC), Priority Sector Lending (PSL) & PM-KISAN",
    "estimatedMinutes": 16
  },
  {
    "id": "top-econ-09-01",
    "chapterId": "ch-econ-09",
    "order": 1,
    "title": "Industrial Policy Evolution: IPR 1948, 1956 (Socialistic Pattern), New Industrial Policy 1991 & Disinvestment (DIPAM)",
    "estimatedMinutes": 23
  },
  {
    "id": "top-econ-09-02",
    "chapterId": "ch-econ-09",
    "order": 2,
    "title": "Central Public Sector Enterprises (CPSEs): Maharatna, Navratna, Miniratna Status & MSMED Act 2006 (Revised 2020 Criteria)",
    "estimatedMinutes": 22
  },
  {
    "id": "top-econ-10-01",
    "chapterId": "ch-econ-10",
    "order": 1,
    "title": "Services Sector Growth: IT-BPM Industry, Financial Services, Tourism & Gig/Platform Economy Dynamics",
    "estimatedMinutes": 23
  },
  {
    "id": "top-econ-10-02",
    "chapterId": "ch-econ-10",
    "order": 2,
    "title": "Digital Public Infrastructure & Logistics: Unified Payments Interface (UPI - NPCI), PM Gati Shakti & National Logistics Policy",
    "estimatedMinutes": 22
  },
  {
    "id": "top-econ-11-01",
    "chapterId": "ch-econ-11",
    "order": 1,
    "title": "Balance of Payments (BoP): Current Account, Capital Account, Current Account Deficit (CAD) & Foreign Exchange Reserves",
    "estimatedMinutes": 23
  },
  {
    "id": "top-econ-11-02",
    "chapterId": "ch-econ-11",
    "order": 2,
    "title": "Foreign Investment & Trade Policy: Foreign Direct Investment (FDI Automatic vs Approval Route), FPI, Foreign Trade Policy & SEZs",
    "estimatedMinutes": 22
  },
  {
    "id": "top-econ-12-01",
    "chapterId": "ch-econ-12",
    "order": 1,
    "title": "Bretton Woods Institutions: International Monetary Fund (IMF, SDRs, Quotas) & World Bank Group (IBRD, IDA, IFC, MIGA, ICSID)",
    "estimatedMinutes": 23
  },
  {
    "id": "top-econ-12-02",
    "chapterId": "ch-econ-12",
    "order": 2,
    "title": "World Trade Organization (WTO): Marrakesh Agreement, Agreements on Agriculture (Amber/Blue/Green Boxes), TRIPS, NDB & AIIB",
    "estimatedMinutes": 22
  },
  {
    "id": "top-econ-13-01",
    "chapterId": "ch-econ-13",
    "order": 1,
    "title": "Macroeconomic Profile of Uttar Pradesh: GSDP Trajectory, Sectoral Composition & UP One Trillion Dollar Economy Roadmap",
    "estimatedMinutes": 23
  },
  {
    "id": "top-econ-13-02",
    "chapterId": "ch-econ-13",
    "order": 2,
    "title": "One District One Product (ODOP), MSME Dominance, Industrial Corridors & Fiscal Indicators of Uttar Pradesh Budget",
    "estimatedMinutes": 22
  },
  {
    "id": "top-econ-14-01",
    "chapterId": "ch-econ-14",
    "order": 1,
    "title": "Sustainable Development Goals (SDGs): 17 Global Goals, NITI Aayog SDG India Index & Green Energy Transition (Panchamrit)",
    "estimatedMinutes": 23
  },
  {
    "id": "top-econ-14-02",
    "chapterId": "ch-econ-14",
    "order": 2,
    "title": "Financial Inclusion in India: Pradhan Mantri Jan Dhan Yojana (PMJDY), JAM Trinity, Microfinance & PM MUDRA Yojana",
    "estimatedMinutes": 22
  }
];

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { topics: ECONOMY_TOPICS };
  } else {
    global.ECONOMY_TOPICS = ECONOMY_TOPICS;
  }
})(typeof window !== 'undefined' ? window : global);
