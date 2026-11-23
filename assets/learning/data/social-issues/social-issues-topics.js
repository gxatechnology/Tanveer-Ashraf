/**
 * Tanveer Ashraf Judicial Prep - Issues of Social Relevance Topics (Paper I General Knowledge)
 */
(function(global) {
  'use strict';
  var SOCIAL_ISSUES_TOPICS = [
  {
    "id": "top-sociss-01-01",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-01",
    "number": 1,
    "order": 1,
    "title": "Constitutional Guarantees & Legislative Framework for Women",
    "summary": "Special provisions under Art 15(3), equal pay Art 39(d), maternity relief Art 42, and statutory protection against domestic violence and workplace harassment.",
    "keyProvisions": [
      "Articles 15(3), 16, 21, 39(d), 42",
      "Protection of Women from Domestic Violence Act 2005",
      "POSH Act 2013"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sociss-01-02",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-01",
    "number": 2,
    "order": 2,
    "title": "Nari Shakti Vandan Adhiniyam & Political Representation",
    "summary": "106th Constitutional Amendment Act 2023, 33% reservation for women in Lok Sabha and State Legislative Assemblies, Articles 239AA, 330A, 332A, 334A.",
    "keyProvisions": [
      "106th Constitutional Amendment Act 2023",
      "Articles 330A, 332A, 334A",
      "Sunset clause 15 years"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sociss-01-03",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-01",
    "number": 3,
    "order": 3,
    "title": "National Commission for Women & Welfare Schemes",
    "summary": "NCW Act 1990 powers, Beti Bachao Beti Padhao, Mission Shakti (Sambal and Samarthya), and One Stop Centres (Sakhi).",
    "keyProvisions": [
      "National Commission for Women Act 1990",
      "Mission Shakti guidelines",
      "Pradhan Mantri Matru Vandana Yojana (PMMVY)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sociss-02-01",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-02",
    "number": 4,
    "order": 4,
    "title": "Juvenile Justice & Child Protection Legal Architecture",
    "summary": "Juvenile Justice (Care and Protection of Children) Act 2015, distinction between CNCP and CCL, JJB, CWC, and District Child Protection Units.",
    "keyProvisions": [
      "JJ Act 2015 Sections 2(14), 2(15), 15",
      "Child Welfare Committees",
      "Juvenile Justice Boards"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sociss-02-02",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-02",
    "number": 5,
    "order": 5,
    "title": "Protection Against Sexual Offences & Child Labour Elimination",
    "summary": "POCSO Act 2012 gender-neutral child sexual abuse protections, Child and Adolescent Labour (Prohibition and Regulation) Act 1986.",
    "keyProvisions": [
      "POCSO Act 2012 Sections 3, 5, 7, 9, 19, 21",
      "Child Labour Act 1986 as amended 2016",
      "Pencil Portal"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sociss-02-03",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-02",
    "number": 6,
    "order": 6,
    "title": "NCPCR Mandates & National Child Nutrition Policies",
    "summary": "Commissions for Protection of Child Rights Act 2005, POSHAN Abhiyaan (National Nutrition Mission), and PM POSHAN (Mid-Day Meal Scheme).",
    "keyProvisions": [
      "CPCR Act 2005",
      "PM POSHAN Guidelines",
      "POSHAN Tracker application"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sociss-03-01",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-03",
    "number": 7,
    "order": 7,
    "title": "Statutory Maintenance & Tribunal Architecture for Elders",
    "summary": "Maintenance and Welfare of Parents and Senior Citizens Act 2007, Maintenance Tribunals, eviction orders, and voiding of conditional property transfers.",
    "keyProvisions": [
      "MWPSC Act 2007 Sections 4, 9, 23",
      "Appellate Tribunals",
      "S. Vanitha v. Deputy Commissioner (2020)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sociss-03-02",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-03",
    "number": 8,
    "order": 8,
    "title": "National Policy for Older Persons & Welfare Frameworks",
    "summary": "Atal Vayo Abhyuday Yojana (AVYAY), Rashtriya Vayoshri Yojana (assisted living devices), Seniorcare Ageing Growth Engine (SAGE), and Elderline (14567).",
    "keyProvisions": [
      "National Policy on Older Persons 1999",
      "Elderline 14567 toll-free helpline",
      "SAGE portal"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sociss-04-01",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-04",
    "number": 9,
    "order": 9,
    "title": "Rights of Persons with Disabilities Act 2016 & Benchmark Disabilities",
    "summary": "Evolution from PwD Act 1995 to RPwD Act 2016 complying with UNCRPD, 21 notified disability categories, definition of benchmark disability (40%+).",
    "keyProvisions": [
      "RPwD Act 2016 Sections 2(r), 34, 38",
      "21 specified conditions in Schedule",
      "4% public employment reservation"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-sociss-04-02",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-04",
    "number": 10,
    "order": 10,
    "title": "Accessible India Campaign & Judicial Enforcement of Rights",
    "summary": "Sugamya Bharat Abhiyan built environment, transport, and ICT accessibility; Rajive Raturi v. Union of India and Vikash Kumar v. UPSC judicial directives.",
    "keyProvisions": [
      "Sugamya Bharat Abhiyan",
      "Reasonable accommodation doctrine",
      "Universal accessibility standards"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sociss-05-01",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-05",
    "number": 11,
    "order": 11,
    "title": "SC & ST Prevention of Atrocities Act 1989 & Special Courts",
    "summary": "Statutory architecture of PoA Act 1989, Section 18/18A bar on anticipatory bail, Special Courts, Exclusive Special Courts, and Prathvi Raj Chauhan ruling.",
    "keyProvisions": [
      "PoA Act 1989 Sections 3, 14, 18, 18A",
      "Subhash Kashinath Mahajan (2018)",
      "Prathvi Raj Chauhan (2020)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-sociss-05-02",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-05",
    "number": 12,
    "order": 12,
    "title": "Constitutional Safeguards & National Commissions (NCSC & NCST)",
    "summary": "Articles 338 and 338A, civil court powers of Commissions during investigations, Article 341 and 342 Presidential notifications.",
    "keyProvisions": [
      "89th Constitutional Amendment Act 2003",
      "Articles 338, 338A, 341, 342",
      "NCSC and NCST investigation powers"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sociss-05-03",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-05",
    "number": 13,
    "order": 13,
    "title": "Sub-Classification Jurisprudence & Forest Rights Act 2006",
    "summary": "State of Punjab v. Davinder Singh (2024) 7-judge bench ruling on inter-se backwardness; Scheduled Tribes and Other Traditional Forest Dwellers Act 2006 (FRA).",
    "keyProvisions": [
      "State of Punjab v. Davinder Singh (2024)",
      "E.V. Chinnaiah overruled",
      "FRA 2006 Section 3, Gram Sabha powers"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sociss-06-01",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-06",
    "number": 14,
    "order": 14,
    "title": "National Food Security Act 2013 & Targeted PDS",
    "summary": "NFSA 2013 legal entitlement: 5 kg grains/person/month for Priority Households, 35 kg for Antyodaya (AAY), Pradhan Mantri Garib Kalyan Anna Yojana (PMGKAY).",
    "keyProvisions": [
      "NFSA 2013 Sections 3, 4, 7, 12",
      "TPDS reforms",
      "One Nation One Ration Card (ONORC)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-sociss-06-02",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-06",
    "number": 15,
    "order": 15,
    "title": "Poverty Estimation Methodologies & Multidimensional Poverty Index",
    "summary": "Expert groups (Lakdawala, Tendulkar, Rangarajan), NITI Aayog National MPI 3 dimensions and 12 indicators, poverty reduction trajectories.",
    "keyProvisions": [
      "Tendulkar Committee 2009 (MRP basket)",
      "Rangarajan Committee 2014",
      "NITI Aayog National MPI (Oxford OPHI method)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sociss-07-01",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-07",
    "number": 16,
    "order": 16,
    "title": "Ayushman Bharat PM-JAY & Health Systems Architecture",
    "summary": "Pradhan Mantri Jan Arogya Yojana INR 5 lakh secondary and tertiary coverage per family per year, Ayushman Arogya Mandirs (Health & Wellness Centres).",
    "keyProvisions": [
      "Ayushman Bharat PM-JAY",
      "National Health Authority (NHA)",
      "Ayushman Bharat Digital Mission (ABDM) / ABHA ID"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sociss-07-02",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-07",
    "number": 17,
    "order": 17,
    "title": "Sanitation Framework & Swachh Bharat Mission",
    "summary": "Swachh Bharat Mission (Grameen & Urban) Phase I and Phase II, ODF, ODF Plus, and ODF Plus Model village criteria, solid and liquid waste management.",
    "keyProvisions": [
      "SBM Guidelines",
      "ODF Plus protocols",
      "Prohibition of Employment as Manual Scavengers Act 2013"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sociss-07-03",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-07",
    "number": 18,
    "order": 18,
    "title": "Mental Health Rights & Mental Healthcare Act 2017",
    "summary": "Right to access mental healthcare, decriminalization of suicide attempt under Section 115, advance directives, Mental Health Review Boards.",
    "keyProvisions": [
      "Mental Healthcare Act 2017 Sections 5, 18, 115",
      "Overriding Section 309 IPC",
      "Mental Health Review Boards"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sociss-08-01",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-08",
    "number": 19,
    "order": 19,
    "title": "National Education Policy 2020: Structure & Legal Foundations",
    "summary": "5+3+3+4 school curricular structure replacing 10+2, foundational literacy & numeracy (NIPUN Bharat), mother tongue instruction, PARAKH, and ABC bank.",
    "keyProvisions": [
      "NEP 2020 Pillars (Access, Equity, Quality, Affordability, Accountability)",
      "Academic Bank of Credits (ABC)",
      "PARAKH national assessment centre"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sociss-08-02",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-08",
    "number": 20,
    "order": 20,
    "title": "Right to Education Act 2009 & Skill Development Architecture",
    "summary": "Article 21A, RTE Act 2009 Section 12(1)(c) 25% disadvantaged quota, no detention policy amendment, National Apprenticeship Promotion Scheme, PMKVY.",
    "keyProvisions": [
      "Article 21A Constitution",
      "RTE Act 2009 Sections 12(1)(c), 16",
      "Pradhan Mantri Kaushal Vikas Yojana (PMKVY 4.0)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sociss-09-01",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-09",
    "number": 21,
    "order": 21,
    "title": "Minority Rights & Educational Protections (Arts 29 & 30)",
    "summary": "Distinct language, script or culture (Art 29), right of religious and linguistic minorities to establish and administer educational institutions (Art 30).",
    "keyProvisions": [
      "Articles 29(1), 29(2), 30(1), 30(1A), 30(2)",
      "T.M.A. Pai Foundation (2002)",
      "P.A. Inamdar (2005)"
    ],
    "estimatedMinutes": 25
  },
  {
    "id": "top-sociss-09-02",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-09",
    "number": 22,
    "order": 22,
    "title": "National Commission for Minorities & Prime Minister 15-Point Programme",
    "summary": "National Commission for Minorities Act 1992, 6 notified minority communities, Sachar Committee report, PM 15-Point Programme for minorities welfare.",
    "keyProvisions": [
      "NCM Act 1992",
      "Notified minorities: Muslims, Christians, Sikhs, Buddhists, Parsis, Jains",
      "Sachar Committee (2006)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sociss-09-03",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-10",
    "number": 23,
    "order": 23,
    "title": "Panchayati Raj & Rural Local Self-Governance",
    "summary": "73rd Constitutional Amendment Act 1992, Part IX, 11th Schedule 29 functional items, mandatory 3-tier structure, State Election Commission, State Finance Commission.",
    "keyProvisions": [
      "Articles 243-243O",
      "11th Schedule 29 subjects",
      "Article 243D reservation for women (1/3rd minimum)"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sociss-10-01",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-10",
    "number": 24,
    "order": 24,
    "title": "Self-Help Groups & National Rural Livelihoods Mission",
    "summary": "DAY-NRLM (Aajeevika), women SHG federations, SHG-Bank Linkage Project (NABARD), Lakhpati Didi initiative, and social mobilization.",
    "keyProvisions": [
      "DAY-NRLM core principles",
      "Lakhpati Didi scheme target",
      "Priority Sector Lending for SHGs"
    ],
    "estimatedMinutes": 20
  },
  {
    "id": "top-sociss-10-02",
    "subjectId": "gk-social",
    "chapterId": "ch-sociss-10",
    "number": 25,
    "order": 25,
    "title": "Urban Social Welfare, Housing & Basic Amenities",
    "summary": "74th Amendment Act 1992, Part IXA, 12th Schedule 18 functional items, Pradhan Mantri Awas Yojana (Urban), AMRUT 2.0, and PM SVANidhi for street vendors.",
    "keyProvisions": [
      "Articles 243P-243ZG",
      "12th Schedule 18 subjects",
      "PM Street Vendor's AtmaNirbhar Nidhi (PM SVANidhi)"
    ],
    "estimatedMinutes": 20
  }
];
  global.SOCIAL_ISSUES_TOPICS = SOCIAL_ISSUES_TOPICS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { topics: SOCIAL_ISSUES_TOPICS, SOCIAL_ISSUES_TOPICS: SOCIAL_ISSUES_TOPICS };
  }
})(typeof window !== 'undefined' ? window : global);
