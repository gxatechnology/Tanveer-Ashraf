/**
 * Tanveer Ashraf Judicial Prep - Indian Polity Topics (Paper I General Knowledge)
 */

(function(global) {
  'use strict';

  var POLITY_TOPICS = [
  {
    "id": "top-pol-01-01",
    "chapterId": "ch-pol-01",
    "order": 1,
    "title": "Constitutional Milestones Under the British Raj: 1773 to 1935 Acts & Indian Independence Act 1947",
    "estimatedMinutes": 22
  },
  {
    "id": "top-pol-01-02",
    "chapterId": "ch-pol-01",
    "order": 2,
    "title": "The Constituent Assembly: Drafting Committee, Enactment, National Symbols & Global Sources Borrowed",
    "estimatedMinutes": 24
  },
  {
    "id": "top-pol-02-01",
    "chapterId": "ch-pol-02",
    "order": 1,
    "title": "The Preamble to the Constitution: Ideals, Objectives, Amendability & 42nd Amendment Additions",
    "estimatedMinutes": 22
  },
  {
    "id": "top-pol-02-02",
    "chapterId": "ch-pol-02",
    "order": 2,
    "title": "Salient Features of the Indian Constitution: Rigid-Flexible Blend, Quasi-Federalism & Fundamental Rights",
    "estimatedMinutes": 23
  },
  {
    "id": "top-pol-03-01",
    "chapterId": "ch-pol-03",
    "order": 1,
    "title": "The Union and Its Territory (Articles 1 to 4) & Linguistic Reorganisation of States (Fazl Ali Commission)",
    "estimatedMinutes": 18
  },
  {
    "id": "top-pol-03-02",
    "chapterId": "ch-pol-03",
    "order": 2,
    "title": "Citizenship Under the Constitution (Articles 5 to 11) & The Citizenship Act, 1955",
    "estimatedMinutes": 18
  },
  {
    "id": "top-pol-03-03",
    "chapterId": "ch-pol-03",
    "order": 3,
    "title": "Fundamental Rights Overview (Articles 12 to 35): Six Broad Freedoms, Limitations & Judicial Writs",
    "estimatedMinutes": 19
  },
  {
    "id": "top-pol-04-01",
    "chapterId": "ch-pol-04",
    "order": 1,
    "title": "Directive Principles of State Policy (Articles 36 to 51): Socialistic, Gandhian & Liberal Principles",
    "estimatedMinutes": 22
  },
  {
    "id": "top-pol-04-02",
    "chapterId": "ch-pol-04",
    "order": 2,
    "title": "Fundamental Duties (Article 51A): Swaran Singh Committee, 42nd & 86th Amendments & Civic Ethics",
    "estimatedMinutes": 23
  },
  {
    "id": "top-pol-05-01",
    "chapterId": "ch-pol-05",
    "order": 1,
    "title": "President of India: Election Method, Qualifications, Term, Impeachment & Executive Powers",
    "estimatedMinutes": 19
  },
  {
    "id": "top-pol-05-02",
    "chapterId": "ch-pol-05",
    "order": 2,
    "title": "Legislative Powers (Article 123 Ordinances) & Pardoning Powers (Article 72) of the President",
    "estimatedMinutes": 18
  },
  {
    "id": "top-pol-05-03",
    "chapterId": "ch-pol-05",
    "order": 3,
    "title": "Vice-President of India, Prime Minister & The Union Council of Ministers (Cabinet System)",
    "estimatedMinutes": 18
  },
  {
    "id": "top-pol-06-01",
    "chapterId": "ch-pol-06",
    "order": 1,
    "title": "Parliamentary Structure: Composition & Powers of Rajya Sabha (Council of States) & Lok Sabha (House of People)",
    "estimatedMinutes": 19
  },
  {
    "id": "top-pol-06-02",
    "chapterId": "ch-pol-06",
    "order": 2,
    "title": "Legislative Procedure in Parliament: Ordinary Bills, Money Bills (Article 110), Finance Bills & Joint Sitting",
    "estimatedMinutes": 18
  },
  {
    "id": "top-pol-06-03",
    "chapterId": "ch-pol-06",
    "order": 3,
    "title": "Parliamentary Committees: Public Accounts Committee (PAC), Estimates Committee & Committee on Public Undertakings",
    "estimatedMinutes": 18
  },
  {
    "id": "top-pol-07-01",
    "chapterId": "ch-pol-07",
    "order": 1,
    "title": "Governor of a State: Appointment, Discretionary Powers, Ordinance Making (Art 213) & Constitutional Role",
    "estimatedMinutes": 17
  },
  {
    "id": "top-pol-07-02",
    "chapterId": "ch-pol-07",
    "order": 2,
    "title": "Chief Minister, State Council of Ministers & Administrative Machinery of Uttar Pradesh",
    "estimatedMinutes": 16
  },
  {
    "id": "top-pol-07-03",
    "chapterId": "ch-pol-07",
    "order": 3,
    "title": "State Legislature: Vidhan Sabha (403 Members in UP) & Vidhan Parishad (100 Members in UP)",
    "estimatedMinutes": 17
  },
  {
    "id": "top-pol-08-01",
    "chapterId": "ch-pol-08",
    "order": 1,
    "title": "The Supreme Court of India: Jurisdiction (Original, Appellate, Advisory - Art 143), Collegium & Judicial Review",
    "estimatedMinutes": 25
  },
  {
    "id": "top-pol-08-02",
    "chapterId": "ch-pol-08",
    "order": 2,
    "title": "High Courts & Subordinate Courts: Article 226 Writs, Judicial Independence & Allahabad High Court Jurisdiction",
    "estimatedMinutes": 25
  },
  {
    "id": "top-pol-09-01",
    "chapterId": "ch-pol-09",
    "order": 1,
    "title": "Legislative & Administrative Relations Between Union and States: Seventh Schedule Lists (Union, State, Concurrent)",
    "estimatedMinutes": 17
  },
  {
    "id": "top-pol-09-02",
    "chapterId": "ch-pol-09",
    "order": 2,
    "title": "Financial Relations, Finance Commission (Article 280) & Goods and Services Tax (GST) Council",
    "estimatedMinutes": 16
  },
  {
    "id": "top-pol-09-03",
    "chapterId": "ch-pol-09",
    "order": 3,
    "title": "Commissions on Centre-State Relations: Sarkaria Commission, Punchhi Commission & Inter-State Council (Art 263)",
    "estimatedMinutes": 17
  },
  {
    "id": "top-pol-10-01",
    "chapterId": "ch-pol-10",
    "order": 1,
    "title": "Evolution of Panchayati Raj: Balwant Rai Mehta, Ashok Mehta Committees & The 73rd Constitutional Amendment Act, 1992",
    "estimatedMinutes": 23
  },
  {
    "id": "top-pol-10-02",
    "chapterId": "ch-pol-10",
    "order": 2,
    "title": "Urban Local Bodies (74th Amendment Act, 1992), 12th Schedule & Uttar Pradesh Panchayati Raj Act Framework",
    "estimatedMinutes": 22
  },
  {
    "id": "top-pol-11-01",
    "chapterId": "ch-pol-11",
    "order": 1,
    "title": "Constitutional Bodies: Election Commission of India (Art 324), UPSC (Art 315) & Comptroller and Auditor General (Art 148)",
    "estimatedMinutes": 19
  },
  {
    "id": "top-pol-11-02",
    "chapterId": "ch-pol-11",
    "order": 2,
    "title": "Statutory Regulatory Authorities & Planning Bodies: NITI Aayog (Evolution from Planning Commission) & Finance Commission",
    "estimatedMinutes": 18
  },
  {
    "id": "top-pol-11-03",
    "chapterId": "ch-pol-11",
    "order": 3,
    "title": "Ombudsman Institutions: Lokpal and Lokayuktas Act, 2013 & The Lokayukta of Uttar Pradesh",
    "estimatedMinutes": 18
  },
  {
    "id": "top-pol-12-01",
    "chapterId": "ch-pol-12",
    "order": 1,
    "title": "Electoral Framework: Representation of the People Acts (1950 & 1951), Model Code of Conduct & EVM/VVPAT",
    "estimatedMinutes": 23
  },
  {
    "id": "top-pol-12-02",
    "chapterId": "ch-pol-12",
    "order": 2,
    "title": "Anti-Defection Law (Tenth Schedule, 52nd & 91st Amendments), Right to Information (RTI Act 2005) & Citizen Charters",
    "estimatedMinutes": 22
  }
];

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { topics: POLITY_TOPICS };
  } else {
    global.POLITY_TOPICS = POLITY_TOPICS;
  }
})(typeof window !== 'undefined' ? window : global);
