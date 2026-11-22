/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Judicial Learning Academy Data Module
 */
(function(global) {
  'use strict';

  const DATA = [
  {
    "id": "top-cnt-01-01",
    "chapterId": "ch-cnt-01",
    "subjectId": "law-contract",
    "title": "Agreement and Contract (Section 2(h) & Section 10 Essentials)",
    "order": 1,
    "mcqsCount": 7,
    "pyqsCount": 3,
    "estimatedMinutes": 17
  },
  {
    "id": "top-cnt-01-02",
    "chapterId": "ch-cnt-01",
    "subjectId": "law-contract",
    "title": "Offer / Proposal: Essentials & Offer vs Invitation to Treat",
    "order": 2,
    "mcqsCount": 7,
    "pyqsCount": 4,
    "estimatedMinutes": 17
  },
  {
    "id": "top-cnt-01-03",
    "chapterId": "ch-cnt-01",
    "subjectId": "law-contract",
    "title": "Acceptance, Postal Rule & Revocation (Sections 3–9)",
    "order": 3,
    "mcqsCount": 6,
    "pyqsCount": 3,
    "estimatedMinutes": 16
  },
  {
    "id": "top-cnt-01-04",
    "chapterId": "ch-cnt-01",
    "subjectId": "law-contract",
    "title": "Intention to Create Legal Relations (Balfour v Balfour Rule)",
    "order": 4,
    "mcqsCount": 6,
    "pyqsCount": 2,
    "estimatedMinutes": 15
  },
  {
    "id": "top-cnt-02-01",
    "chapterId": "ch-cnt-02",
    "subjectId": "law-contract",
    "title": "Consideration Essentials, Types & Quid Pro Quo (Section 2(d))",
    "order": 1,
    "mcqsCount": 8,
    "pyqsCount": 4,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cnt-02-02",
    "chapterId": "ch-cnt-02",
    "subjectId": "law-contract",
    "title": "Privity of Contract vs Privity of Consideration & Exceptions",
    "order": 2,
    "mcqsCount": 8,
    "pyqsCount": 3,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cnt-02-03",
    "chapterId": "ch-cnt-02",
    "subjectId": "law-contract",
    "title": "Agreements Without Consideration & Section 25 Exceptions",
    "order": 3,
    "mcqsCount": 8,
    "pyqsCount": 3,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cnt-03-01",
    "chapterId": "ch-cnt-03",
    "subjectId": "law-contract",
    "title": "Competency to Contract & Minor's Agreements (Mohori Bibee)",
    "order": 1,
    "mcqsCount": 8,
    "pyqsCount": 4,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cnt-03-02",
    "chapterId": "ch-cnt-03",
    "subjectId": "law-contract",
    "title": "Persons of Unsound Mind & Disqualified Persons (Section 12)",
    "order": 2,
    "mcqsCount": 8,
    "pyqsCount": 2,
    "estimatedMinutes": 18
  },
  {
    "id": "top-cnt-03-03",
    "chapterId": "ch-cnt-03",
    "subjectId": "law-contract",
    "title": "Necessaries Supplied to Incompetent Persons (Section 68)",
    "order": 3,
    "mcqsCount": 8,
    "pyqsCount": 3,
    "estimatedMinutes": 17
  },
  {
    "id": "top-cnt-04-01",
    "chapterId": "ch-cnt-04",
    "subjectId": "law-contract",
    "title": "Concept of Free Consent & Consensus ad Idem (Sections 13, 14)",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 2,
    "estimatedMinutes": 15
  },
  {
    "id": "top-cnt-04-02",
    "chapterId": "ch-cnt-04",
    "subjectId": "law-contract",
    "title": "Coercion: Statutory Definition & Legal Impact (Section 15)",
    "order": 2,
    "mcqsCount": 7,
    "pyqsCount": 3,
    "estimatedMinutes": 17
  },
  {
    "id": "top-cnt-04-03",
    "chapterId": "ch-cnt-04",
    "subjectId": "law-contract",
    "title": "Undue Influence, Fiduciary Position & Unconscionability (Section 16)",
    "order": 3,
    "mcqsCount": 7,
    "pyqsCount": 4,
    "estimatedMinutes": 18
  },
  {
    "id": "top-cnt-04-04",
    "chapterId": "ch-cnt-04",
    "subjectId": "law-contract",
    "title": "Fraud: Active Concealment & When Silence is Fraud (Section 17)",
    "order": 4,
    "mcqsCount": 6,
    "pyqsCount": 2,
    "estimatedMinutes": 15
  },
  {
    "id": "top-cnt-05-01",
    "chapterId": "ch-cnt-05",
    "subjectId": "law-contract",
    "title": "Misrepresentation: Types, Remedies & Exceptions (Sections 18, 19)",
    "order": 1,
    "mcqsCount": 8,
    "pyqsCount": 3,
    "estimatedMinutes": 18
  },
  {
    "id": "top-cnt-05-02",
    "chapterId": "ch-cnt-05",
    "subjectId": "law-contract",
    "title": "Mistake of Fact: Bilateral vs Unilateral Mistake (Sections 20, 22)",
    "order": 2,
    "mcqsCount": 7,
    "pyqsCount": 2,
    "estimatedMinutes": 16
  },
  {
    "id": "top-cnt-05-03",
    "chapterId": "ch-cnt-05",
    "subjectId": "law-contract",
    "title": "Mistake of Law: Indian Law vs Foreign Law (Section 21)",
    "order": 3,
    "mcqsCount": 7,
    "pyqsCount": 2,
    "estimatedMinutes": 16
  },
  {
    "id": "top-cnt-06-01",
    "chapterId": "ch-cnt-06",
    "subjectId": "law-contract",
    "title": "Unlawful Consideration & Public Policy Doctrine (Section 23)",
    "order": 1,
    "mcqsCount": 11,
    "pyqsCount": 4,
    "estimatedMinutes": 25
  },
  {
    "id": "top-cnt-06-02",
    "chapterId": "ch-cnt-06",
    "subjectId": "law-contract",
    "title": "Specific Void Agreements: Restraint of Trade, Marriage & Wagering (Sections 26–30)",
    "order": 2,
    "mcqsCount": 11,
    "pyqsCount": 4,
    "estimatedMinutes": 25
  },
  {
    "id": "top-cnt-07-01",
    "chapterId": "ch-cnt-07",
    "subjectId": "law-contract",
    "title": "Contingent Contracts: Meaning, Rules & Enforcement (Sections 31–36)",
    "order": 1,
    "mcqsCount": 11,
    "pyqsCount": 3,
    "estimatedMinutes": 25
  },
  {
    "id": "top-cnt-07-02",
    "chapterId": "ch-cnt-07",
    "subjectId": "law-contract",
    "title": "Quasi-Contracts & Doctrine of Unjust Enrichment (Sections 68–72)",
    "order": 2,
    "mcqsCount": 11,
    "pyqsCount": 3,
    "estimatedMinutes": 25
  },
  {
    "id": "top-cnt-08-01",
    "chapterId": "ch-cnt-08",
    "subjectId": "law-contract",
    "title": "Performance of Contracts & Reciprocal Promises (Sections 37–55)",
    "order": 1,
    "mcqsCount": 9,
    "pyqsCount": 3,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cnt-08-02",
    "chapterId": "ch-cnt-08",
    "subjectId": "law-contract",
    "title": "Doctrine of Frustration & Supervening Impossibility (Section 56)",
    "order": 2,
    "mcqsCount": 8,
    "pyqsCount": 3,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cnt-08-03",
    "chapterId": "ch-cnt-08",
    "subjectId": "law-contract",
    "title": "Discharge by Novation, Rescission & Alteration (Sections 62–67)",
    "order": 3,
    "mcqsCount": 8,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cnt-09-01",
    "chapterId": "ch-cnt-09",
    "subjectId": "law-contract",
    "title": "Anticipatory Breach vs Actual Breach of Contract (Section 39)",
    "order": 1,
    "mcqsCount": 8,
    "pyqsCount": 2,
    "estimatedMinutes": 18
  },
  {
    "id": "top-cnt-09-02",
    "chapterId": "ch-cnt-09",
    "subjectId": "law-contract",
    "title": "Damages for Breach: Rule in Hadley v Baxendale (Section 73)",
    "order": 2,
    "mcqsCount": 9,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cnt-09-03",
    "chapterId": "ch-cnt-09",
    "subjectId": "law-contract",
    "title": "Liquidated Damages vs Penalty: Indian Law Position (Section 74)",
    "order": 3,
    "mcqsCount": 8,
    "pyqsCount": 1,
    "estimatedMinutes": 17
  },
  {
    "id": "top-cnt-10-01",
    "chapterId": "ch-cnt-10",
    "subjectId": "law-contract",
    "title": "Contracts of Indemnity & Guarantee: Rights & Surety Liability (Sections 124–147)",
    "order": 1,
    "mcqsCount": 8,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-cnt-10-02",
    "chapterId": "ch-cnt-10",
    "subjectId": "law-contract",
    "title": "Bailment: Duties of Bailor & Bailee, Bailee's Lien (Sections 148–171)",
    "order": 2,
    "mcqsCount": 8,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cnt-10-03",
    "chapterId": "ch-cnt-10",
    "subjectId": "law-contract",
    "title": "Pledge: Rights of Pawnee & Pledge by Non-Owners (Sections 172–181)",
    "order": 3,
    "mcqsCount": 8,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-cnt-11-01",
    "chapterId": "ch-cnt-11",
    "subjectId": "law-contract",
    "title": "Contract of Agency: Creation, Authority & Sub-Agent (Sections 182–210)",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 22
  },
  {
    "id": "top-cnt-11-02",
    "chapterId": "ch-cnt-11",
    "subjectId": "law-contract",
    "title": "Rights, Duties, Revocation & Principal's Liability (Sections 211–238)",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 23
  }
];

  global.CONTRACT_TOPICS = DATA;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = DATA;
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
