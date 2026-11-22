/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Judicial Learning Academy Data Module
 */
(function(global) {
  'use strict';

  const DATA = [
  {
    "id": "top-jur-01-01",
    "chapterId": "ch-jur-01",
    "subjectId": "law-jurisprudence",
    "title": "Meaning, Nature and Scope of Jurisprudence",
    "order": 1,
    "mcqsCount": 8,
    "pyqsCount": 2,
    "estimatedMinutes": 18
  },
  {
    "id": "top-jur-01-02",
    "chapterId": "ch-jur-01",
    "subjectId": "law-jurisprudence",
    "title": "Law, Morality and Justice (Hart-Fuller & Hart-Devlin Debates)",
    "order": 2,
    "mcqsCount": 8,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-jur-01-03",
    "chapterId": "ch-jur-01",
    "subjectId": "law-jurisprudence",
    "title": "Classifications of Law & General vs Particular Jurisprudence",
    "order": 3,
    "mcqsCount": 8,
    "pyqsCount": 2,
    "estimatedMinutes": 17
  },
  {
    "id": "top-jur-02-01",
    "chapterId": "ch-jur-02",
    "subjectId": "law-jurisprudence",
    "title": "Custom as a Source of Law: Essentials & Theories",
    "order": 1,
    "mcqsCount": 8,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-jur-02-02",
    "chapterId": "ch-jur-02",
    "subjectId": "law-jurisprudence",
    "title": "Judicial Precedent, Stare Decisis & Ratio Decidendi",
    "order": 2,
    "mcqsCount": 8,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-jur-02-03",
    "chapterId": "ch-jur-02",
    "subjectId": "law-jurisprudence",
    "title": "Legislation, Codification & Principles of Interpretation",
    "order": 3,
    "mcqsCount": 8,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-jur-03-01",
    "chapterId": "ch-jur-03",
    "subjectId": "law-jurisprudence",
    "title": "Classical & Medieval Natural Law (Aquinas & Stoics)",
    "order": 1,
    "mcqsCount": 8,
    "pyqsCount": 1,
    "estimatedMinutes": 22
  },
  {
    "id": "top-jur-03-02",
    "chapterId": "ch-jur-03",
    "subjectId": "law-jurisprudence",
    "title": "Social Contract Theory (Hobbes, Locke & Rousseau)",
    "order": 2,
    "mcqsCount": 8,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-jur-03-03",
    "chapterId": "ch-jur-03",
    "subjectId": "law-jurisprudence",
    "title": "Revival of Natural Law in the 20th Century (Fuller, Stammler & Finnis)",
    "order": 3,
    "mcqsCount": 8,
    "pyqsCount": 2,
    "estimatedMinutes": 23
  },
  {
    "id": "top-jur-04-01",
    "chapterId": "ch-jur-04",
    "subjectId": "law-jurisprudence",
    "title": "Jeremy Bentham: Utilitarianism & Censorial Jurisprudence",
    "order": 1,
    "mcqsCount": 7,
    "pyqsCount": 2,
    "estimatedMinutes": 18
  },
  {
    "id": "top-jur-04-02",
    "chapterId": "ch-jur-04",
    "subjectId": "law-jurisprudence",
    "title": "John Austin & the Command Theory of Sovereign Law",
    "order": 2,
    "mcqsCount": 8,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-jur-04-03",
    "chapterId": "ch-jur-04",
    "subjectId": "law-jurisprudence",
    "title": "H.L.A. Hart: Concept of Law, Primary & Secondary Rules",
    "order": 3,
    "mcqsCount": 8,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-jur-04-04",
    "chapterId": "ch-jur-04",
    "subjectId": "law-jurisprudence",
    "title": "Hans Kelsen: Pure Theory of Law & the Grundnorm Hierarchy",
    "order": 4,
    "mcqsCount": 7,
    "pyqsCount": 2,
    "estimatedMinutes": 17
  },
  {
    "id": "top-jur-05-01",
    "chapterId": "ch-jur-05",
    "subjectId": "law-jurisprudence",
    "title": "Friedrich Carl von Savigny & the Doctrine of Volksgeist",
    "order": 1,
    "mcqsCount": 9,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-jur-05-02",
    "chapterId": "ch-jur-05",
    "subjectId": "law-jurisprudence",
    "title": "Sir Henry Maine: Status to Contract & Anthropological Law",
    "order": 2,
    "mcqsCount": 9,
    "pyqsCount": 2,
    "estimatedMinutes": 23
  },
  {
    "id": "top-jur-06-01",
    "chapterId": "ch-jur-06",
    "subjectId": "law-jurisprudence",
    "title": "Foundations: Ihering, Ehrlich's Living Law & Duguit's Solidarity",
    "order": 1,
    "mcqsCount": 9,
    "pyqsCount": 2,
    "estimatedMinutes": 25
  },
  {
    "id": "top-jur-06-02",
    "chapterId": "ch-jur-06",
    "subjectId": "law-jurisprudence",
    "title": "Roscoe Pound: Theory of Social Engineering & Jural Postulates",
    "order": 2,
    "mcqsCount": 9,
    "pyqsCount": 2,
    "estimatedMinutes": 25
  },
  {
    "id": "top-jur-07-01",
    "chapterId": "ch-jur-07",
    "subjectId": "law-jurisprudence",
    "title": "American Realism: Oliver Wendell Holmes Jr. & Jerome Frank",
    "order": 1,
    "mcqsCount": 8,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-jur-07-02",
    "chapterId": "ch-jur-07",
    "subjectId": "law-jurisprudence",
    "title": "Scandinavian Realism & Comparative Jurisprudential Synthesis",
    "order": 2,
    "mcqsCount": 8,
    "pyqsCount": 1,
    "estimatedMinutes": 23
  },
  {
    "id": "top-jur-08-01",
    "chapterId": "ch-jur-08",
    "subjectId": "law-jurisprudence",
    "title": "Concept of Legal Rights and Duties: Salmond's Formula",
    "order": 1,
    "mcqsCount": 8,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-jur-08-02",
    "chapterId": "ch-jur-08",
    "subjectId": "law-jurisprudence",
    "title": "Hohfeld's Analysis: Jural Correlatives & Jural Opposites",
    "order": 2,
    "mcqsCount": 8,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-jur-08-03",
    "chapterId": "ch-jur-08",
    "subjectId": "law-jurisprudence",
    "title": "Classification of Legal Rights (In Rem, In Personam, Proprietary)",
    "order": 3,
    "mcqsCount": 8,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-jur-09-01",
    "chapterId": "ch-jur-09",
    "subjectId": "law-jurisprudence",
    "title": "Legal Personality: Natural Persons, Unborn, Dead & Animals",
    "order": 1,
    "mcqsCount": 9,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-jur-09-02",
    "chapterId": "ch-jur-09",
    "subjectId": "law-jurisprudence",
    "title": "Corporate Personality, Theories & Piercing the Corporate Veil",
    "order": 2,
    "mcqsCount": 9,
    "pyqsCount": 1,
    "estimatedMinutes": 23
  },
  {
    "id": "top-jur-10-01",
    "chapterId": "ch-jur-10",
    "subjectId": "law-jurisprudence",
    "title": "Concept & Essentials of Possession: Corpus & Animus",
    "order": 1,
    "mcqsCount": 8,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-jur-10-02",
    "chapterId": "ch-jur-10",
    "subjectId": "law-jurisprudence",
    "title": "Concept & Characteristics of Ownership (Salmond & Austin)",
    "order": 2,
    "mcqsCount": 8,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-jur-10-03",
    "chapterId": "ch-jur-10",
    "subjectId": "law-jurisprudence",
    "title": "Relationship Between Ownership and Possession & Remedies",
    "order": 3,
    "mcqsCount": 8,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-jur-11-01",
    "chapterId": "ch-jur-11",
    "subjectId": "law-jurisprudence",
    "title": "Nature of Legal Liability: Acts, Omissions, Mens Rea & Negligence",
    "order": 1,
    "mcqsCount": 7,
    "pyqsCount": 1,
    "estimatedMinutes": 17
  },
  {
    "id": "top-jur-11-02",
    "chapterId": "ch-jur-11",
    "subjectId": "law-jurisprudence",
    "title": "Strict, Absolute & Vicarious Liability in Jurisprudence",
    "order": 2,
    "mcqsCount": 7,
    "pyqsCount": 0,
    "estimatedMinutes": 16
  },
  {
    "id": "top-jur-11-03",
    "chapterId": "ch-jur-11",
    "subjectId": "law-jurisprudence",
    "title": "Administration of Justice & Modern Theories of Punishment",
    "order": 3,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 17
  }
];

  global.JURISPRUDENCE_TOPICS = DATA;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = DATA;
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
