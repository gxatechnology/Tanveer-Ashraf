/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Judicial Learning Academy Data Module
 */
(function(global) {
  'use strict';

  const DATA = [
  {
    "id": "ch-evi-01",
    "subjectId": "law-evidence",
    "number": 1,
    "title": "Introduction, Cardinal Definitions & Standards of Proof",
    "scope": "Commencement (1 July 2024), Court, Fact, Fact in issue, Relevant fact, Document, Electronic record, Proved, Disproved, Not proved, and Presumptions",
    "topicsCount": 3,
    "mcqsCount": 30,
    "pyqsCount": 8,
    "estimatedMinutes": 60,
    "weightage": "Very High"
  },
  {
    "id": "ch-evi-02",
    "subjectId": "law-evidence",
    "number": 2,
    "title": "Relevancy of Facts: Res Gestae, Conduct, Conspiracy & Alibi",
    "scope": "Res Gestae (S. 4 BSA / S. 6 IEA), Occasion/cause/effect, Motive, preparation, conduct, TIP, Things said/done in conspiracy, and Plea of Alibi",
    "topicsCount": 4,
    "mcqsCount": 45,
    "pyqsCount": 11,
    "estimatedMinutes": 80,
    "weightage": "Very High"
  },
  {
    "id": "ch-evi-03",
    "subjectId": "law-evidence",
    "number": 3,
    "title": "Admissions & Confessions",
    "scope": "Definition of admission, Confession under inducement/threat, Confession to police officer (S. 23(1) BSA / S. 25 IEA), Discovery statements (S. 23(2) BSA / S. 27 IEA), and Co-accused confession",
    "topicsCount": 4,
    "mcqsCount": 45,
    "pyqsCount": 13,
    "estimatedMinutes": 80,
    "weightage": "Very High"
  },
  {
    "id": "ch-evi-04",
    "subjectId": "law-evidence",
    "number": 4,
    "title": "Statements by Persons Who Cannot Be Called: Dying Declarations",
    "scope": "Dying declarations (S. 26(a) BSA / S. 32(1) IEA), Statements against interest, Statements in ordinary course of business, and Evidence in prior judicial proceedings",
    "topicsCount": 2,
    "mcqsCount": 25,
    "pyqsCount": 8,
    "estimatedMinutes": 55,
    "weightage": "Very High"
  },
  {
    "id": "ch-evi-05",
    "subjectId": "law-evidence",
    "number": 5,
    "title": "Relevancy of Judgments, Expert Opinions & Character Evidence",
    "scope": "Judgments in rem vs in personam, Fraud in judgments, Expert opinions (Science, Art, Handwriting, Digital records), and Character evidence in civil vs criminal matters",
    "topicsCount": 3,
    "mcqsCount": 30,
    "pyqsCount": 7,
    "estimatedMinutes": 60,
    "weightage": "High"
  },
  {
    "id": "ch-evi-06",
    "subjectId": "law-evidence",
    "number": 6,
    "title": "Facts Which Need Not Be Proved & Oral Evidence",
    "scope": "Judicial notice (S. 52 BSA / S. 57 IEA), Facts admitted, Oral evidence must be direct (S. 55 BSA / S. 60 IEA), and Exclusion of hearsay rule",
    "topicsCount": 2,
    "mcqsCount": 20,
    "pyqsCount": 5,
    "estimatedMinutes": 45,
    "weightage": "Medium"
  },
  {
    "id": "ch-evi-07",
    "subjectId": "law-evidence",
    "number": 7,
    "title": "Documentary Evidence & Electronic Records Admissibility",
    "scope": "Primary vs Secondary evidence, When secondary is admissible, Electronic records certification (S. 63 BSA vs S. 65B IEA), Public documents, and 30-year presumption",
    "topicsCount": 3,
    "mcqsCount": 35,
    "pyqsCount": 7,
    "estimatedMinutes": 70,
    "weightage": "Very High"
  },
  {
    "id": "ch-evi-08",
    "subjectId": "law-evidence",
    "number": 8,
    "title": "Exclusion of Oral by Documentary Evidence: The Best Evidence Rule",
    "scope": "Exclusion of oral evidence of terms of contracts/grants (S. 94 BSA / S. 91 IEA), Exclusion of evidence of oral agreement (S. 95 BSA / S. 92 IEA & 6 Provisos), and Ambiguities",
    "topicsCount": 2,
    "mcqsCount": 20,
    "pyqsCount": 4,
    "estimatedMinutes": 50,
    "weightage": "High"
  },
  {
    "id": "ch-evi-09",
    "subjectId": "law-evidence",
    "number": 9,
    "title": "Burden of Proof & Statutory Presumptions",
    "scope": "Burden of proof vs Onus of proof, Facts especially within knowledge (S. 109 BSA / S. 106 IEA), Presumption of death, Legitimacy (S. 116 BSA / S. 112 IEA), Dowry death presumption",
    "topicsCount": 3,
    "mcqsCount": 35,
    "pyqsCount": 6,
    "estimatedMinutes": 65,
    "weightage": "Very High"
  },
  {
    "id": "ch-evi-10",
    "subjectId": "law-evidence",
    "number": 10,
    "title": "Estoppel, Competency of Witnesses & Witness Examination",
    "scope": "Doctrine of Estoppel (S. 121 BSA / S. 115 IEA), Competency of witnesses, Privileged communications, Examination stages, Leading questions, and Hostile witnesses",
    "topicsCount": 4,
    "mcqsCount": 40,
    "pyqsCount": 4,
    "estimatedMinutes": 75,
    "weightage": "Very High"
  }
];

  global.EVIDENCE_CHAPTERS = DATA;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = DATA;
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
