/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Judicial Learning Academy Data Module
 */
(function(global) {
  'use strict';

  const DATA = [
  {
    "id": "ch-crim-01",
    "subjectId": "law-criminal",
    "number": 1,
    "title": "Introduction, Territorial Application & General Explanations",
    "scope": "Title, commencement (1 July 2024), territorial jurisdiction, extra-territorial offences, and cardinal statutory definitions under BNS & IPC",
    "topicsCount": 3,
    "mcqsCount": 30,
    "pyqsCount": 6,
    "estimatedMinutes": 60,
    "weightage": "High"
  },
  {
    "id": "ch-crim-02",
    "subjectId": "law-criminal",
    "number": 2,
    "title": "Punishments & Sentencing Framework",
    "scope": "Theories of punishment, death penalty, life imprisonment, solitary confinement, community service under BNS, commutation, and remission",
    "topicsCount": 2,
    "mcqsCount": 20,
    "pyqsCount": 4,
    "estimatedMinutes": 45,
    "weightage": "Medium"
  },
  {
    "id": "ch-crim-03",
    "subjectId": "law-criminal",
    "number": 3,
    "title": "General Exceptions: Excusable & Justifiable Acts",
    "scope": "Mistake of fact, judicial acts, infancy (doli incapax), insanity (M'Naghten rules), intoxication, consent, communication in good faith, and trivial acts",
    "topicsCount": 4,
    "mcqsCount": 40,
    "pyqsCount": 10,
    "estimatedMinutes": 80,
    "weightage": "Very High"
  },
  {
    "id": "ch-crim-04",
    "subjectId": "law-criminal",
    "number": 4,
    "title": "Right of Private Defence of Body & Property",
    "scope": "Nature and limits of private defence, commencement and continuance, when defence extends to causing death of body and property",
    "topicsCount": 3,
    "mcqsCount": 30,
    "pyqsCount": 7,
    "estimatedMinutes": 60,
    "weightage": "Very High"
  },
  {
    "id": "ch-crim-05",
    "subjectId": "law-criminal",
    "number": 5,
    "title": "Inchoate Crimes: Joint Liability, Abetment, Conspiracy & Attempt",
    "scope": "Joint liability (S. 3(5) BNS vs S. 34 IPC), Common object (S. 190 BNS vs S. 149 IPC), Abetment, Criminal Conspiracy, and Attempt to commit offences",
    "topicsCount": 4,
    "mcqsCount": 40,
    "pyqsCount": 9,
    "estimatedMinutes": 75,
    "weightage": "Very High"
  },
  {
    "id": "ch-crim-06",
    "subjectId": "law-criminal",
    "number": 6,
    "title": "Offences Against Human Body: Homicide, Murder & Fatal Injuries",
    "scope": "Culpable homicide vs Murder (S. 100/101 BNS vs S. 299/300 IPC), 5 Exceptions, Rarest of rare doctrine, Rash/negligent death (S. 106 caveat), Dowry death, and Mob lynching",
    "topicsCount": 4,
    "mcqsCount": 50,
    "pyqsCount": 14,
    "estimatedMinutes": 90,
    "weightage": "Very High"
  },
  {
    "id": "ch-crim-07",
    "subjectId": "law-criminal",
    "number": 7,
    "title": "Offences Against Human Body: Hurt, Restraint & Kidnapping",
    "scope": "Hurt and Grievous hurt (8 clauses), Acid attack, Wrongful restraint & confinement, Kidnapping vs Abduction, and Human trafficking",
    "topicsCount": 3,
    "mcqsCount": 30,
    "pyqsCount": 6,
    "estimatedMinutes": 60,
    "weightage": "High"
  },
  {
    "id": "ch-crim-08",
    "subjectId": "law-criminal",
    "number": 8,
    "title": "Offences Against Women & Children",
    "scope": "Rape (S. 63 BNS vs S. 375 IPC), Consent & Age thresholds, Assault/criminal force to woman, Voyeurism, Stalking, Cruelty by husband (S. 84 BNS vs S. 498A IPC)",
    "topicsCount": 3,
    "mcqsCount": 40,
    "pyqsCount": 8,
    "estimatedMinutes": 75,
    "weightage": "Very High"
  },
  {
    "id": "ch-crim-09",
    "subjectId": "law-criminal",
    "number": 9,
    "title": "Offences Against Property: Theft, Extortion, Robbery & Dacoity",
    "scope": "Theft, Extortion, Robbery, Dacoity, Criminal misappropriation, Criminal breach of trust, Cheating, Mischief, and Criminal trespass",
    "topicsCount": 3,
    "mcqsCount": 40,
    "pyqsCount": 8,
    "estimatedMinutes": 75,
    "weightage": "Very High"
  },
  {
    "id": "ch-crim-10",
    "subjectId": "law-criminal",
    "number": 10,
    "title": "Offences Against State & Public Tranquility",
    "scope": "Endangering sovereignty, unity & integrity of India (S. 152 BNS), Terrorism (S. 113 BNS), Organised crime (S. 111 BNS), Unlawful assembly, Rioting, and Affray",
    "topicsCount": 3,
    "mcqsCount": 30,
    "pyqsCount": 4,
    "estimatedMinutes": 60,
    "weightage": "High"
  },
  {
    "id": "ch-crim-11",
    "subjectId": "law-criminal",
    "number": 11,
    "title": "Offences Against Public Justice & False Evidence",
    "scope": "Giving and fabricating false evidence (Perjury), Offences against public justice, Contempt of lawful authority of public servants, and Harboring offenders",
    "topicsCount": 2,
    "mcqsCount": 20,
    "pyqsCount": 3,
    "estimatedMinutes": 45,
    "weightage": "Medium"
  },
  {
    "id": "ch-crim-12",
    "subjectId": "law-criminal",
    "number": 12,
    "title": "Offences Affecting Reputation, Documents & Criminal Intimidation",
    "scope": "Forgery, Making false document/electronic records, Criminal intimidation, Insult, Annoyance, Defamation and Community service sanctions",
    "topicsCount": 2,
    "mcqsCount": 20,
    "pyqsCount": 3,
    "estimatedMinutes": 45,
    "weightage": "Medium"
  }
];

  global.CRIMINAL_CHAPTERS = DATA;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = DATA;
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
