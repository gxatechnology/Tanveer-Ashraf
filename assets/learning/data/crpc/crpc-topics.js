/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Judicial Learning Academy Data Module
 */
(function(global) {
  'use strict';

  const DATA = [
  {
    "id": "top-crpc-01-01",
    "chapterId": "ch-crpc-01",
    "subjectId": "law-crpc",
    "title": "Hierarchy & Classes of Criminal Courts in BNSS & CrPC",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crpc-01-02",
    "chapterId": "ch-crpc-01",
    "subjectId": "law-crpc",
    "title": "Sentencing Jurisdiction of Sessions & Magistrates",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crpc-01-03",
    "chapterId": "ch-crpc-01",
    "subjectId": "law-crpc",
    "title": "Directorate of Prosecution & Public Prosecutors",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crpc-02-01",
    "chapterId": "ch-crpc-02",
    "subjectId": "law-crpc",
    "title": "Arrest Without Warrant & Notice of Appearance (Arnesh Kumar)",
    "order": 1,
    "mcqsCount": 12,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-crpc-02-02",
    "chapterId": "ch-crpc-02",
    "subjectId": "law-crpc",
    "title": "Procedure of Arrest, Handcuff Rules & Search of Arrestee",
    "order": 2,
    "mcqsCount": 11,
    "pyqsCount": 2,
    "estimatedMinutes": 21
  },
  {
    "id": "top-crpc-02-03",
    "chapterId": "ch-crpc-02",
    "subjectId": "law-crpc",
    "title": "Rights of Arrested Persons & The 24-Hour Rule (D.K. Basu)",
    "order": 3,
    "mcqsCount": 12,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-crpc-03-01",
    "chapterId": "ch-crpc-03",
    "subjectId": "law-crpc",
    "title": "Summons & Warrants of Arrest: Form, Service & Execution",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crpc-03-02",
    "chapterId": "ch-crpc-03",
    "subjectId": "law-crpc",
    "title": "Proclamation & Attachment of Property for Absconders",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crpc-03-03",
    "chapterId": "ch-crpc-03",
    "subjectId": "law-crpc",
    "title": "Search Warrants, Summons to Produce & Impounding",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crpc-04-01",
    "chapterId": "ch-crpc-04",
    "subjectId": "law-crpc",
    "title": "Security for Keeping Peace & Good Behaviour Proceedings",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crpc-04-02",
    "chapterId": "ch-crpc-04",
    "subjectId": "law-crpc",
    "title": "Maintenance of Public Order & Urgent Injunctions (S. 144 CrPC)",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crpc-04-03",
    "chapterId": "ch-crpc-04",
    "subjectId": "law-crpc",
    "title": "Disputes as to Immovable Property: Possession Inquiries",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crpc-05-01",
    "chapterId": "ch-crpc-05",
    "subjectId": "law-crpc",
    "title": "Maintenance of Wives, Children & Parents: S. 125 CrPC / S. 144 BNSS",
    "order": 1,
    "mcqsCount": 13,
    "pyqsCount": 3,
    "estimatedMinutes": 25
  },
  {
    "id": "top-crpc-05-02",
    "chapterId": "ch-crpc-05",
    "subjectId": "law-crpc",
    "title": "Procedure, Alteration & Enforcement of Maintenance Orders",
    "order": 2,
    "mcqsCount": 12,
    "pyqsCount": 2,
    "estimatedMinutes": 25
  },
  {
    "id": "top-crpc-06-01",
    "chapterId": "ch-crpc-06",
    "subjectId": "law-crpc",
    "title": "First Information Report: S. 173 BNSS / S. 154 CrPC & Zero FIR",
    "order": 1,
    "mcqsCount": 14,
    "pyqsCount": 2,
    "estimatedMinutes": 25
  },
  {
    "id": "top-crpc-06-02",
    "chapterId": "ch-crpc-06",
    "subjectId": "law-crpc",
    "title": "Police Investigation Powers & Examination of Witnesses (S. 161 CrPC)",
    "order": 2,
    "mcqsCount": 13,
    "pyqsCount": 2,
    "estimatedMinutes": 25
  },
  {
    "id": "top-crpc-06-03",
    "chapterId": "ch-crpc-06",
    "subjectId": "law-crpc",
    "title": "Recording Confessions & Statements by Magistrate (S. 164 CrPC)",
    "order": 3,
    "mcqsCount": 13,
    "pyqsCount": 2,
    "estimatedMinutes": 25
  },
  {
    "id": "top-crpc-07-01",
    "chapterId": "ch-crpc-07",
    "subjectId": "law-crpc",
    "title": "Remand & Police Custody: S. 187 BNSS vs S. 167 CrPC & Default Bail",
    "order": 1,
    "mcqsCount": 15,
    "pyqsCount": 2,
    "estimatedMinutes": 28
  },
  {
    "id": "top-crpc-07-02",
    "chapterId": "ch-crpc-07",
    "subjectId": "law-crpc",
    "title": "Inquest Inquiries & Final Police Report (Charge-Sheet S. 173 CrPC)",
    "order": 2,
    "mcqsCount": 15,
    "pyqsCount": 2,
    "estimatedMinutes": 27
  },
  {
    "id": "top-crpc-08-01",
    "chapterId": "ch-crpc-08",
    "subjectId": "law-crpc",
    "title": "Territorial Jurisdiction of Criminal Courts for Inquiries & Trials",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crpc-08-02",
    "chapterId": "ch-crpc-08",
    "subjectId": "law-crpc",
    "title": "Cognizance of Offences by Magistrates & Statutory Sanctions",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crpc-08-03",
    "chapterId": "ch-crpc-08",
    "subjectId": "law-crpc",
    "title": "Complaints to Magistrates & Issue of Process (S. 200\u2013204 CrPC)",
    "order": 3,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crpc-09-01",
    "chapterId": "ch-crpc-09",
    "subjectId": "law-crpc",
    "title": "Form, Contents & Alteration of Charge",
    "order": 1,
    "mcqsCount": 12,
    "pyqsCount": 1,
    "estimatedMinutes": 25
  },
  {
    "id": "top-crpc-09-02",
    "chapterId": "ch-crpc-09",
    "subjectId": "law-crpc",
    "title": "Joinder of Charges & Statutory Exceptions to Separate Trials",
    "order": 2,
    "mcqsCount": 13,
    "pyqsCount": 2,
    "estimatedMinutes": 25
  },
  {
    "id": "top-crpc-10-01",
    "chapterId": "ch-crpc-10",
    "subjectId": "law-crpc",
    "title": "Trial Before Court of Session: Discharge, Opening & Verdict",
    "order": 1,
    "mcqsCount": 12,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crpc-10-02",
    "chapterId": "ch-crpc-10",
    "subjectId": "law-crpc",
    "title": "Trial of Warrant Cases by Magistrates (Police vs Complaint)",
    "order": 2,
    "mcqsCount": 11,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crpc-10-03",
    "chapterId": "ch-crpc-10",
    "subjectId": "law-crpc",
    "title": "Summons Trials & Summary Trials: Distinction & Procedure",
    "order": 3,
    "mcqsCount": 11,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crpc-10-04",
    "chapterId": "ch-crpc-10",
    "subjectId": "law-crpc",
    "title": "Plea Bargaining & Trial in Absentia of Proclaimed Offenders",
    "order": 4,
    "mcqsCount": 11,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crpc-11-01",
    "chapterId": "ch-crpc-11",
    "subjectId": "law-crpc",
    "title": "Autrefois Acquit & Autrefois Convict: Double Jeopardy in Procedure",
    "order": 1,
    "mcqsCount": 12,
    "pyqsCount": 1,
    "estimatedMinutes": 22
  },
  {
    "id": "top-crpc-11-02",
    "chapterId": "ch-crpc-11",
    "subjectId": "law-crpc",
    "title": "Examination of Accused (S. 313 CrPC) & Tender of Pardon",
    "order": 2,
    "mcqsCount": 11,
    "pyqsCount": 1,
    "estimatedMinutes": 21
  },
  {
    "id": "top-crpc-11-03",
    "chapterId": "ch-crpc-11",
    "subjectId": "law-crpc",
    "title": "Inherent Powers (S. 482 CrPC / S. 528 BNSS) & Summoning (S. 319)",
    "order": 3,
    "mcqsCount": 12,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-crpc-12-01",
    "chapterId": "ch-crpc-12",
    "subjectId": "law-crpc",
    "title": "Bailable vs Non-Bailable Offences & General Bail Principles",
    "order": 1,
    "mcqsCount": 12,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crpc-12-02",
    "chapterId": "ch-crpc-12",
    "subjectId": "law-crpc",
    "title": "Undertrial Bail Rights: S. 479 BNSS vs S. 436A CrPC",
    "order": 2,
    "mcqsCount": 11,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crpc-12-03",
    "chapterId": "ch-crpc-12",
    "subjectId": "law-crpc",
    "title": "Anticipatory Bail & Special Powers of High Court / Sessions",
    "order": 3,
    "mcqsCount": 11,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-crpc-12-04",
    "chapterId": "ch-crpc-12",
    "subjectId": "law-crpc",
    "title": "Judgments, Appeals, Reference & Revision Jurisdiction",
    "order": 4,
    "mcqsCount": 11,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  }
];

  global.CRPC_TOPICS = DATA;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = DATA;
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
