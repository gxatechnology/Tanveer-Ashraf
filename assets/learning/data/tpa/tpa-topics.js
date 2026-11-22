/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Judicial Learning Academy Data Module
 */
(function(global) {
  'use strict';

  const DATA = [
  {
    "id": "top-tpa-01-01",
    "chapterId": "ch-tpa-01",
    "subjectId": "law-tpa",
    "title": "Meaning and Scope of Transfer (Sections 1–5: Act Inter Vivos)",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 3,
    "estimatedMinutes": 20
  },
  {
    "id": "top-tpa-01-02",
    "chapterId": "ch-tpa-01",
    "subjectId": "law-tpa",
    "title": "What May Be Transferred & Non-Transferable Properties (Section 6)",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 3,
    "estimatedMinutes": 20
  },
  {
    "id": "top-tpa-01-03",
    "chapterId": "ch-tpa-01",
    "subjectId": "law-tpa",
    "title": "Competency to Transfer & Operation of Transfer (Sections 7, 8)",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-tpa-02-01",
    "chapterId": "ch-tpa-02",
    "subjectId": "law-tpa",
    "title": "Conditions Restraining Alienation: Absolute vs Partial (Section 10)",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 3,
    "estimatedMinutes": 22
  },
  {
    "id": "top-tpa-02-02",
    "chapterId": "ch-tpa-02",
    "subjectId": "law-tpa",
    "title": "Transfer for Benefit of Unborn Persons & Prior Life Estate (Section 13)",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 21
  },
  {
    "id": "top-tpa-02-03",
    "chapterId": "ch-tpa-02",
    "subjectId": "law-tpa",
    "title": "Rule Against Perpetuity & Accumulation of Income (Sections 14, 17)",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-tpa-03-01",
    "chapterId": "ch-tpa-03",
    "subjectId": "law-tpa",
    "title": "Vested Interest vs Contingent Interest (Sections 19, 21)",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 3,
    "estimatedMinutes": 20
  },
  {
    "id": "top-tpa-03-02",
    "chapterId": "ch-tpa-03",
    "subjectId": "law-tpa",
    "title": "Conditional Transfers: Condition Precedent vs Subsequent (Sections 25–34)",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-tpa-03-03",
    "chapterId": "ch-tpa-03",
    "subjectId": "law-tpa",
    "title": "Doctrine of Election: Foundation & Operation (Section 35)",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-tpa-04-01",
    "chapterId": "ch-tpa-04",
    "subjectId": "law-tpa",
    "title": "Doctrine of Notice: Actual vs Constructive Notice (Section 3)",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-tpa-04-02",
    "chapterId": "ch-tpa-04",
    "subjectId": "law-tpa",
    "title": "Transfer by Ostensible Owner & Benami Transactions (Section 41)",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 3,
    "estimatedMinutes": 22
  },
  {
    "id": "top-tpa-04-03",
    "chapterId": "ch-tpa-04",
    "subjectId": "law-tpa",
    "title": "Doctrine of Feeding the Grant by Estoppel (Section 43)",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 21
  },
  {
    "id": "top-tpa-05-01",
    "chapterId": "ch-tpa-05",
    "subjectId": "law-tpa",
    "title": "Doctrine of Lis Pendens & Pendente Lite Transfers (Section 52)",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 3,
    "estimatedMinutes": 22
  },
  {
    "id": "top-tpa-05-02",
    "chapterId": "ch-tpa-05",
    "subjectId": "law-tpa",
    "title": "Fraudulent Transfer & Protection of Creditors (Section 53)",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 21
  },
  {
    "id": "top-tpa-05-03",
    "chapterId": "ch-tpa-05",
    "subjectId": "law-tpa",
    "title": "Doctrine of Part Performance: Equitable Shield (Section 53A)",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-tpa-06-01",
    "chapterId": "ch-tpa-06",
    "subjectId": "law-tpa",
    "title": "Concept and Essentials of Sale (Section 54: Sale vs Contract to Sell)",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 18
  },
  {
    "id": "top-tpa-06-02",
    "chapterId": "ch-tpa-06",
    "subjectId": "law-tpa",
    "title": "Rights and Liabilities of Buyer and Seller (Section 55)",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 19
  },
  {
    "id": "top-tpa-06-03",
    "chapterId": "ch-tpa-06",
    "subjectId": "law-tpa",
    "title": "Exchange of Immovable Property (Sections 118–121)",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-tpa-07-01",
    "chapterId": "ch-tpa-07",
    "subjectId": "law-tpa",
    "title": "Concept of Mortgage & 6 Statutory Forms of Mortgage (Section 58)",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-tpa-07-02",
    "chapterId": "ch-tpa-07",
    "subjectId": "law-tpa",
    "title": "Right of Redemption & Clog on Equity of Redemption (Section 60)",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-tpa-07-03",
    "chapterId": "ch-tpa-07",
    "subjectId": "law-tpa",
    "title": "Rights of Mortgagee, Subrogation (s. 92) & Charges (Section 100)",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 21
  },
  {
    "id": "top-tpa-08-01",
    "chapterId": "ch-tpa-08",
    "subjectId": "law-tpa",
    "title": "Leases of Immovable Property & Determination of Lease (Sections 105–117)",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-tpa-08-02",
    "chapterId": "ch-tpa-08",
    "subjectId": "law-tpa",
    "title": "Gifts: Essentials, Onerous Gifts & Revocation (Sections 122–129)",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-tpa-08-03",
    "chapterId": "ch-tpa-08",
    "subjectId": "law-tpa",
    "title": "Transfer of Actionable Claims: Assignment & Notice (Sections 130–137)",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  }
];

  global.TPA_TOPICS = DATA;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = DATA;
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
