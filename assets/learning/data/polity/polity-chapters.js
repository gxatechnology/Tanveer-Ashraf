/**
 * Tanveer Ashraf Judicial Prep - Indian Polity Chapters (Paper I General Knowledge)
 */

(function(global) {
  'use strict';

  var POLITY_CHAPTERS = [
  {
    "id": "ch-pol-01",
    "subjectId": "gk-polity",
    "number": 1, "order": 1,
    "title": "Historical Evolution & Making of the Constitution",
    "description": "Constitutional milestones under the British Raj (1773–1947), Constituent Assembly, Drafting Committee, and Adoption.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-pol-02",
    "subjectId": "gk-polity",
    "number": 2, "order": 2,
    "title": "Preamble, Salient Features & Constitutional Philosophy",
    "description": "Sovereignty, Socialist, Secular, Democratic Republic, Justice, Liberty, Equality, and Unitary-Federal Balance.",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-pol-03",
    "subjectId": "gk-polity",
    "number": 3, "order": 3,
    "title": "Union & Its Territory, Citizenship & Fundamental Rights",
    "description": "State reorganization, Citizenship Act 1955, and the core civic framework of Fundamental Rights (Articles 12–35).",
    "estimatedMinutes": 55
  },
  {
    "id": "ch-pol-04",
    "subjectId": "gk-polity",
    "number": 4, "order": 4,
    "title": "Directive Principles of State Policy & Fundamental Duties",
    "description": "Socio-economic welfare blueprint (Articles 36–51), 42nd Amendment, Swaran Singh Committee & Article 51A Duties.",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-pol-05",
    "subjectId": "gk-polity",
    "number": 5, "order": 5,
    "title": "Union Executive: President, Vice-President & Prime Minister",
    "description": "Electoral College, executive powers, ordinance making (Art 123), pardoning power (Art 72), and Cabinet governance.",
    "estimatedMinutes": 55
  },
  {
    "id": "ch-pol-06",
    "subjectId": "gk-polity",
    "number": 6, "order": 6,
    "title": "Union Parliament: Structure, Powers & Committees",
    "description": "Bicameral legislature (Lok Sabha & Rajya Sabha), legislative procedure, Money Bills, and Parliamentary Financial Committees.",
    "estimatedMinutes": 55
  },
  {
    "id": "ch-pol-07",
    "subjectId": "gk-polity",
    "number": 7, "order": 7,
    "title": "State Executive & Legislature: Focus on Uttar Pradesh",
    "description": "Governor's role, Chief Minister, Vidhan Sabha (403 seats), Vidhan Parishad (100 seats), and UP Administrative Secretariat.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-pol-08",
    "subjectId": "gk-polity",
    "number": 8, "order": 8,
    "title": "Indian Judicial System: Supreme Court & High Courts",
    "description": "Judicial independence, Collegium system, advisory jurisdiction (Art 143), PIL, and Allahabad High Court jurisdiction.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-pol-09",
    "subjectId": "gk-polity",
    "number": 9, "order": 9,
    "title": "Federal Structure & Centre-State Relations",
    "description": "Seventh Schedule legislative distribution, financial relations, Sarkaria and Punchhi commissions, and Inter-State Council.",
    "estimatedMinutes": 50
  },
  {
    "id": "ch-pol-10",
    "subjectId": "gk-polity",
    "number": 10, "order": 10,
    "title": "Local Self-Government: Panchayati Raj & Municipalities",
    "description": "73rd and 74th Constitutional Amendments, Balwant Rai Mehta, 11th and 12th Schedules, and UP Panchayati Raj Act.",
    "estimatedMinutes": 45
  },
  {
    "id": "ch-pol-11",
    "subjectId": "gk-polity",
    "number": 11, "order": 11,
    "title": "Constitutional & Non-Constitutional Statutory Bodies",
    "description": "Election Commission of India, UPSC, CAG, Finance Commission, NITI Aayog, NHRC, and Lokayukta of Uttar Pradesh.",
    "estimatedMinutes": 55
  },
  {
    "id": "ch-pol-12",
    "subjectId": "gk-polity",
    "number": 12, "order": 12,
    "title": "Elections, Political Parties & Good Governance",
    "description": "RPA Acts 1950 & 1951, Tenth Schedule Anti-Defection, EVM/VVPAT, RTI Act 2005, and Citizen Charters.",
    "estimatedMinutes": 45
  }
];

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { chapters: POLITY_CHAPTERS };
  } else {
    global.POLITY_CHAPTERS = POLITY_CHAPTERS;
  }
})(typeof window !== 'undefined' ? window : global);
