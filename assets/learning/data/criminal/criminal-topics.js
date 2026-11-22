/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Judicial Learning Academy Data Module
 */
(function(global) {
  'use strict';

  const DATA = [
  {
    "id": "top-crim-01-01",
    "chapterId": "ch-crim-01",
    "subjectId": "law-criminal",
    "title": "Title, Territorial Scope & Commencement (1 July 2024)",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-01-02",
    "chapterId": "ch-crim-01",
    "subjectId": "law-criminal",
    "title": "Statutory Definitions & Interpretations in BNS & IPC",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-01-03",
    "chapterId": "ch-crim-01",
    "subjectId": "law-criminal",
    "title": "Actus Reus, Mens Rea & Strict Liability in Penal Law",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-02-01",
    "chapterId": "ch-crim-02",
    "subjectId": "law-criminal",
    "title": "Sentencing Framework & Community Service under BNS",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-crim-02-02",
    "chapterId": "ch-crim-02",
    "subjectId": "law-criminal",
    "title": "Solitary Confinement, Commutation & Limit of Punishments",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 23
  },
  {
    "id": "top-crim-03-01",
    "chapterId": "ch-crim-03",
    "subjectId": "law-criminal",
    "title": "Mistake of Fact vs Mistake of Law & Judicial Acts",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 3,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-03-02",
    "chapterId": "ch-crim-03",
    "subjectId": "law-criminal",
    "title": "Infancy (Doli Incapax) & Insanity: M'Naghten Rules",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 3,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-03-03",
    "chapterId": "ch-crim-03",
    "subjectId": "law-criminal",
    "title": "Involuntary vs Voluntary Intoxication (Basdev Doctrine)",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-03-04",
    "chapterId": "ch-crim-03",
    "subjectId": "law-criminal",
    "title": "Consent, Good Faith Medical Acts & Trivial Acts (De Minimis)",
    "order": 4,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-04-01",
    "chapterId": "ch-crim-04",
    "subjectId": "law-criminal",
    "title": "Nature, Scope and Statutory Limits of Private Defence",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-04-02",
    "chapterId": "ch-crim-04",
    "subjectId": "law-criminal",
    "title": "Private Defence of Body: When Extends to Causing Death",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 3,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-04-03",
    "chapterId": "ch-crim-04",
    "subjectId": "law-criminal",
    "title": "Private Defence of Property: Extent and Causing Death",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-05-01",
    "chapterId": "ch-crim-05",
    "subjectId": "law-criminal",
    "title": "Common Intention vs Common Object: Joint Criminal Liability",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 3,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-05-02",
    "chapterId": "ch-crim-05",
    "subjectId": "law-criminal",
    "title": "Abetment: Instigation, Conspiracy & Intentional Aiding",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-05-03",
    "chapterId": "ch-crim-05",
    "subjectId": "law-criminal",
    "title": "Criminal Conspiracy: Agreement, Mens Rea & Evidence",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-05-04",
    "chapterId": "ch-crim-05",
    "subjectId": "law-criminal",
    "title": "Criminal Attempt: Preparation vs Attempt & Proximity Test",
    "order": 4,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 15
  },
  {
    "id": "top-crim-06-01",
    "chapterId": "ch-crim-06",
    "subjectId": "law-criminal",
    "title": "Culpable Homicide vs Murder: S. 100/101 BNS & S. 299/300 IPC",
    "order": 1,
    "mcqsCount": 15,
    "pyqsCount": 5,
    "estimatedMinutes": 25
  },
  {
    "id": "top-crim-06-02",
    "chapterId": "ch-crim-06",
    "subjectId": "law-criminal",
    "title": "The Five Exceptions to Murder & Provocation Doctrine",
    "order": 2,
    "mcqsCount": 15,
    "pyqsCount": 4,
    "estimatedMinutes": 25
  },
  {
    "id": "top-crim-06-03",
    "chapterId": "ch-crim-06",
    "subjectId": "law-criminal",
    "title": "Rash & Negligent Death: S. 106(1) & S. 106(2) BNS Caveat",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 3,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-06-04",
    "chapterId": "ch-crim-06",
    "subjectId": "law-criminal",
    "title": "Dowry Death, Abetment of Suicide & Mob Lynching Provisions",
    "order": 4,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-07-01",
    "chapterId": "ch-crim-07",
    "subjectId": "law-criminal",
    "title": "Hurt and Grievous Hurt: Eight Statutory Clauses & Acid Attack",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-07-02",
    "chapterId": "ch-crim-07",
    "subjectId": "law-criminal",
    "title": "Wrongful Restraint & Wrongful Confinement",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-07-03",
    "chapterId": "ch-crim-07",
    "subjectId": "law-criminal",
    "title": "Kidnapping vs Abduction & Human Trafficking Framework",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-08-01",
    "chapterId": "ch-crim-08",
    "subjectId": "law-criminal",
    "title": "Rape: Definition, Consent, Age Thresholds & Aggravated Offences",
    "order": 1,
    "mcqsCount": 15,
    "pyqsCount": 3,
    "estimatedMinutes": 25
  },
  {
    "id": "top-crim-08-02",
    "chapterId": "ch-crim-08",
    "subjectId": "law-criminal",
    "title": "Outraging Modesty, Sexual Harassment, Voyeurism & Stalking",
    "order": 2,
    "mcqsCount": 15,
    "pyqsCount": 3,
    "estimatedMinutes": 25
  },
  {
    "id": "top-crim-08-03",
    "chapterId": "ch-crim-08",
    "subjectId": "law-criminal",
    "title": "Cruelty by Husband/Relatives & Deceitful Marriage Offences",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 25
  },
  {
    "id": "top-crim-09-01",
    "chapterId": "ch-crim-09",
    "subjectId": "law-criminal",
    "title": "Theft, Extortion, Robbery & Dacoity: The Gradation Spectrum",
    "order": 1,
    "mcqsCount": 15,
    "pyqsCount": 3,
    "estimatedMinutes": 25
  },
  {
    "id": "top-crim-09-02",
    "chapterId": "ch-crim-09",
    "subjectId": "law-criminal",
    "title": "Criminal Misappropriation & Criminal Breach of Trust",
    "order": 2,
    "mcqsCount": 15,
    "pyqsCount": 3,
    "estimatedMinutes": 25
  },
  {
    "id": "top-crim-09-03",
    "chapterId": "ch-crim-09",
    "subjectId": "law-criminal",
    "title": "Cheating, Mischief, Criminal Trespass & House-breaking",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 25
  },
  {
    "id": "top-crim-10-01",
    "chapterId": "ch-crim-10",
    "subjectId": "law-criminal",
    "title": "Acts Endangering Sovereignty & Integrity of India (S. 152 BNS)",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-10-02",
    "chapterId": "ch-crim-10",
    "subjectId": "law-criminal",
    "title": "Terrorism & Organised Crime in BNS (S. 111, 112, 113)",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-10-03",
    "chapterId": "ch-crim-10",
    "subjectId": "law-criminal",
    "title": "Unlawful Assembly, Rioting & Affray",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crim-11-01",
    "chapterId": "ch-crim-11",
    "subjectId": "law-criminal",
    "title": "Giving and Fabricating False Evidence: Perjury & Sanctions",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-crim-11-02",
    "chapterId": "ch-crim-11",
    "subjectId": "law-criminal",
    "title": "Contempt of Lawful Authority of Public Servants",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 23
  },
  {
    "id": "top-crim-12-01",
    "chapterId": "ch-crim-12",
    "subjectId": "law-criminal",
    "title": "Forgery, False Documents & Electronic Records (BNS S. 336)",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 22
  },
  {
    "id": "top-crim-12-02",
    "chapterId": "ch-crim-12",
    "subjectId": "law-criminal",
    "title": "Criminal Intimidation, Insult, Annoyance & Defamation",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 23
  }
];

  global.CRIMINAL_TOPICS = DATA;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = DATA;
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
