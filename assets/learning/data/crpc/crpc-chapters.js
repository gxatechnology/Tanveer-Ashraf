/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Judicial Learning Academy Data Module
 */
(function(global) {
  'use strict';

  const DATA = [
  {
    "id": "ch-crpc-01",
    "subjectId": "law-crpc",
    "number": 1,
    "title": "Constitution & Hierarchy of Criminal Courts & Prosecutors",
    "scope": "Classes of criminal courts, territorial divisions, powers to pass sentences, separation of judiciary, and Directorate of Prosecution under BNSS & CrPC",
    "topicsCount": 3,
    "mcqsCount": 30,
    "pyqsCount": 5,
    "estimatedMinutes": 60,
    "weightage": "High"
  },
  {
    "id": "ch-crpc-02",
    "subjectId": "law-crpc",
    "number": 2,
    "title": "Powers of Police & Arrest of Persons",
    "scope": "Arrest without warrant, notice of appearance (S. 35 BNSS / S. 41A CrPC), handcuff regulation, search of arrestee, and rights of arrested persons (24-hour rule)",
    "topicsCount": 3,
    "mcqsCount": 35,
    "pyqsCount": 6,
    "estimatedMinutes": 65,
    "weightage": "Very High"
  },
  {
    "id": "ch-crpc-03",
    "subjectId": "law-crpc",
    "number": 3,
    "title": "Processes to Compel Appearance & Production of Things",
    "scope": "Summons, warrant of arrest, proclamation and attachment of property (S. 84 BNSS / S. 82 CrPC), search warrants, and impounding documents",
    "topicsCount": 3,
    "mcqsCount": 30,
    "pyqsCount": 4,
    "estimatedMinutes": 60,
    "weightage": "High"
  },
  {
    "id": "ch-crpc-04",
    "subjectId": "law-crpc",
    "number": 4,
    "title": "Security Proceedings, Public Order & Urgent Injunctions",
    "scope": "Security for keeping peace and good behaviour, unlawful assemblies, urgent orders in nuisance/danger (S. 163 BNSS / S. 144 CrPC), and immovable property disputes",
    "topicsCount": 3,
    "mcqsCount": 30,
    "pyqsCount": 4,
    "estimatedMinutes": 60,
    "weightage": "High"
  },
  {
    "id": "ch-crpc-05",
    "subjectId": "law-crpc",
    "number": 5,
    "title": "Maintenance of Wives, Children & Parents",
    "scope": "Statutory maintenance under S. 144 BNSS / S. 125 CrPC, neglected dependants, interim maintenance, alteration, enforcement, and landmark precedents",
    "topicsCount": 2,
    "mcqsCount": 25,
    "pyqsCount": 5,
    "estimatedMinutes": 50,
    "weightage": "Very High"
  },
  {
    "id": "ch-crpc-06",
    "subjectId": "law-crpc",
    "number": 6,
    "title": "Information to Police, FIR & Powers of Investigation",
    "scope": "FIR (S. 173 BNSS / S. 154 CrPC), Zero FIR, E-FIR, preliminary inquiry, investigation powers, witness examination (S. 180 BNSS / S. 161 CrPC), and confessions (S. 183 BNSS / S. 164 CrPC)",
    "topicsCount": 3,
    "mcqsCount": 40,
    "pyqsCount": 6,
    "estimatedMinutes": 75,
    "weightage": "Very High"
  },
  {
    "id": "ch-crpc-07",
    "subjectId": "law-crpc",
    "number": 7,
    "title": "Remand, Police Custody & Final Police Report",
    "scope": "Remand under S. 187 BNSS / S. 167 CrPC (15-day custody in 40/60 days), default bail, medical inquest, and police closure/charge-sheet (S. 193 BNSS / S. 173 CrPC)",
    "topicsCount": 2,
    "mcqsCount": 30,
    "pyqsCount": 4,
    "estimatedMinutes": 55,
    "weightage": "Very High"
  },
  {
    "id": "ch-crpc-08",
    "subjectId": "law-crpc",
    "number": 8,
    "title": "Jurisdiction & Cognizance of Offences by Criminal Courts",
    "scope": "Ordinary place of inquiry/trial, special territorial rules, cognizance by Magistrates (S. 210 BNSS / S. 190 CrPC), sanction for prosecution, and complaint procedure",
    "topicsCount": 3,
    "mcqsCount": 30,
    "pyqsCount": 4,
    "estimatedMinutes": 60,
    "weightage": "High"
  },
  {
    "id": "ch-crpc-09",
    "subjectId": "law-crpc",
    "number": 9,
    "title": "The Charge & Joinder of Charges",
    "scope": "Contents of charge, particulars of time/place/person, effect of errors, alteration of charge, separate trials rule, and statutory exceptions to separate trials",
    "topicsCount": 2,
    "mcqsCount": 25,
    "pyqsCount": 3,
    "estimatedMinutes": 50,
    "weightage": "High"
  },
  {
    "id": "ch-crpc-10",
    "subjectId": "law-crpc",
    "number": 10,
    "title": "Trial Procedures: Sessions, Warrant, Summons & Summary Trials",
    "scope": "Sessions trial, Warrant trial (police case vs complaint), Summons trial, Summary trial, Plea bargaining, and Trial in absentia of proclaimed offenders (S. 356 BNSS)",
    "topicsCount": 4,
    "mcqsCount": 45,
    "pyqsCount": 4,
    "estimatedMinutes": 80,
    "weightage": "Very High"
  },
  {
    "id": "ch-crpc-11",
    "subjectId": "law-crpc",
    "number": 11,
    "title": "General Provisions as to Inquiries, Trials & Inherent Powers",
    "scope": "Double jeopardy (Autrefois acquit/convict), right to legal aid, examination of accused (S. 351 BNSS / S. 313 CrPC), tender of pardon, S. 319 CrPC / S. 358 BNSS, and S. 528 BNSS / S. 482 CrPC",
    "topicsCount": 3,
    "mcqsCount": 35,
    "pyqsCount": 4,
    "estimatedMinutes": 65,
    "weightage": "Very High"
  },
  {
    "id": "ch-crpc-12",
    "subjectId": "law-crpc",
    "number": 12,
    "title": "Bail Jurisprudence, Appeals, Reference & Revision",
    "scope": "Bailable vs Non-bailable bail, undertrial release (S. 479 BNSS vs S. 436A CrPC), anticipatory bail (S. 482 BNSS / S. 438 CrPC), judgments, appeals, reference, and revision",
    "topicsCount": 4,
    "mcqsCount": 45,
    "pyqsCount": 4,
    "estimatedMinutes": 80,
    "weightage": "Very High"
  }
];

  global.CRPC_CHAPTERS = DATA;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = DATA;
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
