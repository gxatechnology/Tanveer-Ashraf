/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Judicial Learning Academy Data Module
 */
(function(global) {
  'use strict';

  const DATA = [
  {
    "id": "top-evi-01-01",
    "chapterId": "ch-evi-01",
    "subjectId": "law-evidence",
    "title": "Scope, Commencement (1 July 2024), Court, Fact & Fact in Issue",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 3,
    "estimatedMinutes": 20
  },
  {
    "id": "top-evi-01-02",
    "chapterId": "ch-evi-01",
    "subjectId": "law-evidence",
    "title": "Relevant Fact, Document & Electronic Record Definitions",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 3,
    "estimatedMinutes": 20
  },
  {
    "id": "top-evi-01-03",
    "chapterId": "ch-evi-01",
    "subjectId": "law-evidence",
    "title": "Proved, Disproved, Not Proved & Presumption Standards",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-evi-02-01",
    "chapterId": "ch-evi-02",
    "subjectId": "law-evidence",
    "title": "Doctrine of Res Gestae: Facts Forming Part of Same Transaction",
    "order": 1,
    "mcqsCount": 12,
    "pyqsCount": 4,
    "estimatedMinutes": 20
  },
  {
    "id": "top-evi-02-02",
    "chapterId": "ch-evi-02",
    "subjectId": "law-evidence",
    "title": "Occasion, Cause, Effect, Opportunity & Motive/Conduct",
    "order": 2,
    "mcqsCount": 11,
    "pyqsCount": 3,
    "estimatedMinutes": 20
  },
  {
    "id": "top-evi-02-03",
    "chapterId": "ch-evi-02",
    "subjectId": "law-evidence",
    "title": "Test Identification Parade (TIP) & Explanatory Facts",
    "order": 3,
    "mcqsCount": 11,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-evi-02-04",
    "chapterId": "ch-evi-02",
    "subjectId": "law-evidence",
    "title": "Conspiracy Proof (S. 8 BSA / S. 10 IEA) & Plea of Alibi",
    "order": 4,
    "mcqsCount": 11,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-evi-03-01",
    "chapterId": "ch-evi-03",
    "subjectId": "law-evidence",
    "title": "Admissions Defined & Persons Qualified to Make Admissions",
    "order": 1,
    "mcqsCount": 11,
    "pyqsCount": 3,
    "estimatedMinutes": 20
  },
  {
    "id": "top-evi-03-02",
    "chapterId": "ch-evi-03",
    "subjectId": "law-evidence",
    "title": "Confessions Under Inducement, Threat or Promise (S. 22 BSA / S. 24 IEA)",
    "order": 2,
    "mcqsCount": 11,
    "pyqsCount": 3,
    "estimatedMinutes": 20
  },
  {
    "id": "top-evi-03-03",
    "chapterId": "ch-evi-03",
    "subjectId": "law-evidence",
    "title": "Confession to Police Officers & In Police Custody",
    "order": 3,
    "mcqsCount": 11,
    "pyqsCount": 3,
    "estimatedMinutes": 20
  },
  {
    "id": "top-evi-03-04",
    "chapterId": "ch-evi-03",
    "subjectId": "law-evidence",
    "title": "Discovery Statements: S. 23(2) BSA / S. 27 IEA (Pulukuri Kottaya)",
    "order": 4,
    "mcqsCount": 12,
    "pyqsCount": 4,
    "estimatedMinutes": 20
  },
  {
    "id": "top-evi-04-01",
    "chapterId": "ch-evi-04",
    "subjectId": "law-evidence",
    "title": "Dying Declarations: S. 26(a) BSA / S. 32(1) IEA (Pakala Narayana Swami)",
    "order": 1,
    "mcqsCount": 13,
    "pyqsCount": 5,
    "estimatedMinutes": 28
  },
  {
    "id": "top-evi-04-02",
    "chapterId": "ch-evi-04",
    "subjectId": "law-evidence",
    "title": "Statements Against Interest, Course of Business & Prior Evidence",
    "order": 2,
    "mcqsCount": 12,
    "pyqsCount": 3,
    "estimatedMinutes": 27
  },
  {
    "id": "top-evi-05-01",
    "chapterId": "ch-evi-05",
    "subjectId": "law-evidence",
    "title": "Relevancy of Judgments: Res Judicata, In Rem & In Personam",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-evi-05-02",
    "chapterId": "ch-evi-05",
    "subjectId": "law-evidence",
    "title": "Expert Opinions: Science, Art, Fingerprints & Digital Evidence",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 3,
    "estimatedMinutes": 20
  },
  {
    "id": "top-evi-05-03",
    "chapterId": "ch-evi-05",
    "subjectId": "law-evidence",
    "title": "Character Evidence in Civil & Criminal Proceedings",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-evi-06-01",
    "chapterId": "ch-evi-06",
    "subjectId": "law-evidence",
    "title": "Facts Judicially Noticeable & Facts Admitted",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-evi-06-02",
    "chapterId": "ch-evi-06",
    "subjectId": "law-evidence",
    "title": "Oral Evidence Must Be Direct & Exceptions to Hearsay",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 3,
    "estimatedMinutes": 23
  },
  {
    "id": "top-evi-07-01",
    "chapterId": "ch-evi-07",
    "subjectId": "law-evidence",
    "title": "Primary vs Secondary Evidence & Admissibility Criteria",
    "order": 1,
    "mcqsCount": 12,
    "pyqsCount": 3,
    "estimatedMinutes": 24
  },
  {
    "id": "top-evi-07-02",
    "chapterId": "ch-evi-07",
    "subjectId": "law-evidence",
    "title": "Electronic Records Admissibility: BSA S. 63 vs IEA S. 65B Certificate",
    "order": 2,
    "mcqsCount": 12,
    "pyqsCount": 2,
    "estimatedMinutes": 24
  },
  {
    "id": "top-evi-07-03",
    "chapterId": "ch-evi-07",
    "subjectId": "law-evidence",
    "title": "Public Documents, Certified Copies & Presumptions as to Documents",
    "order": 3,
    "mcqsCount": 11,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-evi-08-01",
    "chapterId": "ch-evi-08",
    "subjectId": "law-evidence",
    "title": "Exclusion of Oral by Documentary Evidence (Best Evidence Rule S. 91)",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 25
  },
  {
    "id": "top-evi-08-02",
    "chapterId": "ch-evi-08",
    "subjectId": "law-evidence",
    "title": "Exclusion of Evidence of Oral Agreement & The Six Provisos (S. 92)",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 25
  },
  {
    "id": "top-evi-09-01",
    "chapterId": "ch-evi-09",
    "subjectId": "law-evidence",
    "title": "Burden of Proof vs Evidential Onus & Special Knowledge (S. 106 IEA)",
    "order": 1,
    "mcqsCount": 12,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-evi-09-02",
    "chapterId": "ch-evi-09",
    "subjectId": "law-evidence",
    "title": "Presumption of Death, Legitimacy (S. 112 IEA) & Dowry Death",
    "order": 2,
    "mcqsCount": 12,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-evi-09-03",
    "chapterId": "ch-evi-09",
    "subjectId": "law-evidence",
    "title": "Court Presumptions: S. 114 IEA / S. 117 BSA & Absence of Consent",
    "order": 3,
    "mcqsCount": 11,
    "pyqsCount": 2,
    "estimatedMinutes": 21
  },
  {
    "id": "top-evi-10-01",
    "chapterId": "ch-evi-10",
    "subjectId": "law-evidence",
    "title": "Doctrine of Estoppel: Rules, Promissory & Tenant Estoppel",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-evi-10-02",
    "chapterId": "ch-evi-10",
    "subjectId": "law-evidence",
    "title": "Competency of Witnesses, Child/Dumb Witnesses & Privileged Comms",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-evi-10-03",
    "chapterId": "ch-evi-10",
    "subjectId": "law-evidence",
    "title": "Order of Examination: Chief, Cross, Re-Exam & Leading Questions",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-evi-10-04",
    "chapterId": "ch-evi-10",
    "subjectId": "law-evidence",
    "title": "Impeaching Credit, Hostile Witnesses & Refreshing Memory",
    "order": 4,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 15
  }
];

  global.EVIDENCE_TOPICS = DATA;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = DATA;
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
