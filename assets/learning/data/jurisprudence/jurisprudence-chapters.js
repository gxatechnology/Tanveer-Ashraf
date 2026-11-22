/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Judicial Learning Academy Data Module
 */
(function(global) {
  'use strict';

  const DATA = [
  {
    "id": "ch-jur-01",
    "subjectId": "law-jurisprudence",
    "number": 1,
    "title": "Nature, Scope & Classification of Jurisprudence",
    "scope": "Meaning, definitions, grammar of law, law and morality, classifications of law",
    "topicsCount": 3,
    "mcqsCount": 24,
    "pyqsCount": 6,
    "estimatedMinutes": 55,
    "weightage": "High"
  },
  {
    "id": "ch-jur-02",
    "subjectId": "law-jurisprudence",
    "number": 2,
    "title": "Sources of Law: Custom, Precedent & Legislation",
    "scope": "Custom essentials, stare decisis, ratio decidendi, obiter dicta, statutory codification",
    "topicsCount": 3,
    "mcqsCount": 24,
    "pyqsCount": 5,
    "estimatedMinutes": 60,
    "weightage": "High"
  },
  {
    "id": "ch-jur-03",
    "subjectId": "law-jurisprudence",
    "number": 3,
    "title": "Natural Law School & Philosophical Foundations",
    "scope": "Classical Greek/Roman, Medieval Aquinas, Social Contract, 20th century revival (Fuller, Finnis)",
    "topicsCount": 3,
    "mcqsCount": 24,
    "pyqsCount": 4,
    "estimatedMinutes": 65,
    "weightage": "Very High"
  },
  {
    "id": "ch-jur-04",
    "subjectId": "law-jurisprudence",
    "number": 4,
    "title": "Analytical & Positivist School: Austin, Hart & Kelsen",
    "scope": "Bentham's Utilitarianism, Austin's Command Theory, Hart's Rules, Kelsen's Pure Theory & Grundnorm",
    "topicsCount": 4,
    "mcqsCount": 30,
    "pyqsCount": 8,
    "estimatedMinutes": 75,
    "weightage": "Very High"
  },
  {
    "id": "ch-jur-05",
    "subjectId": "law-jurisprudence",
    "number": 5,
    "title": "Historical School of Jurisprudence: Savigny & Maine",
    "scope": "Savigny's Volksgeist, opposition to codification, Maine's Status to Contract, Ancient Law",
    "topicsCount": 2,
    "mcqsCount": 18,
    "pyqsCount": 4,
    "estimatedMinutes": 45,
    "weightage": "High"
  },
  {
    "id": "ch-jur-06",
    "subjectId": "law-jurisprudence",
    "number": 6,
    "title": "Sociological School: Ihering, Ehrlich, Duguit & Pound",
    "scope": "Ihering's purpose, Ehrlich's living law, Duguit's social solidarity, Pound's social engineering & jural postulates",
    "topicsCount": 2,
    "mcqsCount": 18,
    "pyqsCount": 4,
    "estimatedMinutes": 50,
    "weightage": "Very High"
  },
  {
    "id": "ch-jur-07",
    "subjectId": "law-jurisprudence",
    "number": 7,
    "title": "Realist School & Modern Critical Jurisprudence",
    "scope": "American Realism (Holmes, Frank, Llewellyn), Scandinavian Realism (Olivecrona, Ross), Comparative schools",
    "topicsCount": 2,
    "mcqsCount": 16,
    "pyqsCount": 3,
    "estimatedMinutes": 45,
    "weightage": "Medium"
  },
  {
    "id": "ch-jur-08",
    "subjectId": "law-jurisprudence",
    "number": 8,
    "title": "Legal Rights and Duties: Salmond & Hohfeldian Analysis",
    "scope": "Essentials of legal rights, correlation with duties, Hohfeld's tables of jural correlatives & opposites, classification of rights",
    "topicsCount": 3,
    "mcqsCount": 24,
    "pyqsCount": 4,
    "estimatedMinutes": 60,
    "weightage": "Very High"
  },
  {
    "id": "ch-jur-09",
    "subjectId": "law-jurisprudence",
    "number": 9,
    "title": "Legal Personality: Natural & Juristic Persons",
    "scope": "Status of unborn, dead, animals, idols; Corporate personality theories (Fiction, Realist, Bracket, Purpose), veil lifting",
    "topicsCount": 2,
    "mcqsCount": 18,
    "pyqsCount": 3,
    "estimatedMinutes": 45,
    "weightage": "High"
  },
  {
    "id": "ch-jur-10",
    "subjectId": "law-jurisprudence",
    "number": 10,
    "title": "Concepts of Ownership and Possession",
    "scope": "Corpus & animus, Savigny vs Salmond, possession in fact and law, ownership bundle of rights, possessory remedies",
    "topicsCount": 3,
    "mcqsCount": 24,
    "pyqsCount": 3,
    "estimatedMinutes": 60,
    "weightage": "High"
  },
  {
    "id": "ch-jur-11",
    "subjectId": "law-jurisprudence",
    "number": 11,
    "title": "Liability, Obligations & Administration of Justice",
    "scope": "Civil and criminal liability, remedial and penal, strict & absolute liability, theories of punishment",
    "topicsCount": 3,
    "mcqsCount": 20,
    "pyqsCount": 1,
    "estimatedMinutes": 50,
    "weightage": "Medium"
  }
];

  global.JURISPRUDENCE_CHAPTERS = DATA;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = DATA;
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
