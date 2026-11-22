/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * CPC Topics Metadata Module
 */
(function(global) {
  "use strict";

  const DATA = [
  {
    "id": "top-cpc-01-01",
    "chapterId": "ch-cpc-01",
    "subjectId": "law-cpc",
    "title": "Nature, Scheme & Structure of CPC: Substantive vs Procedural Law",
    "order": 1,
    "mcqsCount": 7,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-01-02",
    "chapterId": "ch-cpc-01",
    "subjectId": "law-cpc",
    "title": "Section 2 Definitions: Decree, Preliminary vs Final & Deemed Decree",
    "order": 2,
    "mcqsCount": 7,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-cpc-01-03",
    "chapterId": "ch-cpc-01",
    "subjectId": "law-cpc",
    "title": "Orders, Judgments, Legal Representative, Mesne Profits & Foreign Judgment",
    "order": 3,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-cpc-02-01",
    "chapterId": "ch-cpc-02",
    "subjectId": "law-cpc",
    "title": "Jurisdiction of Civil Courts under Section 9: Suits of Civil Nature & Bars",
    "order": 1,
    "mcqsCount": 7,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-02-02",
    "chapterId": "ch-cpc-02",
    "subjectId": "law-cpc",
    "title": "Pecuniary & Territorial Jurisdiction: Place of Suing (Sections 15\u201320)",
    "order": 2,
    "mcqsCount": 7,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-02-03",
    "chapterId": "ch-cpc-02",
    "subjectId": "law-cpc",
    "title": "Objections to Jurisdiction (Section 21) & Transfer of Suits (Sections 22\u201325)",
    "order": 3,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-cpc-03-01",
    "chapterId": "ch-cpc-03",
    "subjectId": "law-cpc",
    "title": "Stay of Suit: Doctrine of Res Sub Judice under Section 10",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-03-02",
    "chapterId": "ch-cpc-03",
    "subjectId": "law-cpc",
    "title": "Doctrine of Res Judicata under Section 11: Essential Conditions & Scope",
    "order": 2,
    "mcqsCount": 7,
    "pyqsCount": 2,
    "estimatedMinutes": 24
  },
  {
    "id": "top-cpc-03-03",
    "chapterId": "ch-cpc-03",
    "subjectId": "law-cpc",
    "title": "The 8 Explanations of Section 11, Constructive Res Judicata & Co-Defendants",
    "order": 3,
    "mcqsCount": 7,
    "pyqsCount": 1,
    "estimatedMinutes": 22
  },
  {
    "id": "top-cpc-04-01",
    "chapterId": "ch-cpc-04",
    "subjectId": "law-cpc",
    "title": "Institution of Suits under Section 26 & Order IV: Affidavits & Verification",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 22
  },
  {
    "id": "top-cpc-04-02",
    "chapterId": "ch-cpc-04",
    "subjectId": "law-cpc",
    "title": "Cause of Action, Framing of Suit & Order II Rule 2 Bar on Splitting Claims",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 24
  },
  {
    "id": "top-cpc-05-01",
    "chapterId": "ch-cpc-05",
    "subjectId": "law-cpc",
    "title": "Parties to Suit: Joinder, Necessary vs Proper Parties & Non-Joinder (Order I)",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 25
  },
  {
    "id": "top-cpc-05-02",
    "chapterId": "ch-cpc-05",
    "subjectId": "law-cpc",
    "title": "Representative Suits (Order I Rule 8) & Adding/Striking Parties (Order I Rule 10)",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 25
  },
  {
    "id": "top-cpc-06-01",
    "chapterId": "ch-cpc-06",
    "subjectId": "law-cpc",
    "title": "Pleadings: Material Facts, Verification & Striking Out Pleadings (Order VI)",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 24
  },
  {
    "id": "top-cpc-06-02",
    "chapterId": "ch-cpc-06",
    "subjectId": "law-cpc",
    "title": "Amendment of Pleadings under Order VI Rule 17 & Due Diligence Proviso",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 2,
    "estimatedMinutes": 26
  },
  {
    "id": "top-cpc-07-01",
    "chapterId": "ch-cpc-07",
    "subjectId": "law-cpc",
    "title": "Plaint: Return of Plaint (O. VII R. 10) vs Rejection of Plaint (O. VII R. 11)",
    "order": 1,
    "mcqsCount": 7,
    "pyqsCount": 2,
    "estimatedMinutes": 24
  },
  {
    "id": "top-cpc-07-02",
    "chapterId": "ch-cpc-07",
    "subjectId": "law-cpc",
    "title": "Written Statement & Time Limits under Order VIII Rule 1 (30 to 90 Days)",
    "order": 2,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-07-03",
    "chapterId": "ch-cpc-07",
    "subjectId": "law-cpc",
    "title": "Set-Off (Legal & Equitable) vs Counter-Claim (Order VIII Rules 6 & 6A\u20136G)",
    "order": 3,
    "mcqsCount": 7,
    "pyqsCount": 2,
    "estimatedMinutes": 22
  },
  {
    "id": "top-cpc-08-01",
    "chapterId": "ch-cpc-08",
    "subjectId": "law-cpc",
    "title": "Summons to Defendant: Modes of Service & Substituted Service (Order V)",
    "order": 1,
    "mcqsCount": 7,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-08-02",
    "chapterId": "ch-cpc-08",
    "subjectId": "law-cpc",
    "title": "Appearance & Non-Appearance: Dismissal for Default & Remedies (Order IX)",
    "order": 2,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-08-03",
    "chapterId": "ch-cpc-08",
    "subjectId": "law-cpc",
    "title": "Ex Parte Decrees: Remedies & Setting Aside under Order IX Rule 13",
    "order": 3,
    "mcqsCount": 7,
    "pyqsCount": 1,
    "estimatedMinutes": 22
  },
  {
    "id": "top-cpc-09-01",
    "chapterId": "ch-cpc-09",
    "subjectId": "law-cpc",
    "title": "Examination of Parties (Order X) & Discovery and Interrogatories (Order XI)",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 22
  },
  {
    "id": "top-cpc-09-02",
    "chapterId": "ch-cpc-09",
    "subjectId": "law-cpc",
    "title": "Admissions (Order XII) & Production and Return of Documents (Order XIII)",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 22
  },
  {
    "id": "top-cpc-10-01",
    "chapterId": "ch-cpc-10",
    "subjectId": "law-cpc",
    "title": "Settlement of Issues (Order XIV) & Disposal at First Hearing (Order XV)",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 24
  },
  {
    "id": "top-cpc-10-02",
    "chapterId": "ch-cpc-10",
    "subjectId": "law-cpc",
    "title": "Witness Attendance (Order XVI), Adjournments (Order XVII) & Trial (Order XVIII)",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 26
  },
  {
    "id": "top-cpc-11-01",
    "chapterId": "ch-cpc-11",
    "subjectId": "law-cpc",
    "title": "Judgment and Decree under Section 33 & Order XX: Distinction & Timelines",
    "order": 1,
    "mcqsCount": 7,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-11-02",
    "chapterId": "ch-cpc-11",
    "subjectId": "law-cpc",
    "title": "Statutory Interest under Section 34: Commercial, Pendente Lite & Future Interest",
    "order": 2,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-cpc-11-03",
    "chapterId": "ch-cpc-11",
    "subjectId": "law-cpc",
    "title": "Costs: General (S. 35), Compensatory (S. 35A), Delay Costs (S. 35B) & Order XXA",
    "order": 3,
    "mcqsCount": 7,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-12-01",
    "chapterId": "ch-cpc-12",
    "subjectId": "law-cpc",
    "title": "Executing Court Powers, Jurisdiction & Transfer of Decrees (Sections 36\u201346)",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-12-02",
    "chapterId": "ch-cpc-12",
    "subjectId": "law-cpc",
    "title": "Modes of Execution: Arrest & Detention (S. 51, 55, 58 & S. 56 Bar on Women)",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-12-03",
    "chapterId": "ch-cpc-12",
    "subjectId": "law-cpc",
    "title": "Attachment of Property: Section 60 Exemptions & Garnishee Orders (O. XXI)",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-12-04",
    "chapterId": "ch-cpc-12",
    "subjectId": "law-cpc",
    "title": "Objections to Execution (O. XXI R. 58) & Resistance to Delivery (O. XXI R. 97\u2013106)",
    "order": 4,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-13-01",
    "chapterId": "ch-cpc-13",
    "subjectId": "law-cpc",
    "title": "Arrest & Attachment Before Judgment under Order XXXVIII (Rules 1\u201313)",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-cpc-13-02",
    "chapterId": "ch-cpc-13",
    "subjectId": "law-cpc",
    "title": "Temporary Injunctions under Order XXXIX Rules 1\u20135: The Triple Test",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 2,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-13-03",
    "chapterId": "ch-cpc-13",
    "subjectId": "law-cpc",
    "title": "Interlocutory Orders, Receivers (Order XL) & Caveat Petitions (Section 148A)",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-cpc-13-04",
    "chapterId": "ch-cpc-13",
    "subjectId": "law-cpc",
    "title": "Inherent Powers of Court (Section 151) & Amendments of Decrees (Sections 152\u2013153)",
    "order": 4,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-cpc-14-01",
    "chapterId": "ch-cpc-14",
    "subjectId": "law-cpc",
    "title": "Death, Marriage & Insolvency of Parties: Abatement & Substitution (Order XXII)",
    "order": 1,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 22
  },
  {
    "id": "top-cpc-14-02",
    "chapterId": "ch-cpc-14",
    "subjectId": "law-cpc",
    "title": "Withdrawal of Suits (Order XXIII Rule 1) & Lawful Compromise (O. XXIII R. 3)",
    "order": 2,
    "mcqsCount": 10,
    "pyqsCount": 1,
    "estimatedMinutes": 22
  },
  {
    "id": "top-cpc-15-01",
    "chapterId": "ch-cpc-15",
    "subjectId": "law-cpc",
    "title": "Suits By or Against Government & Public Officers (Sections 79\u201382 & Order XXVII)",
    "order": 1,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-cpc-15-02",
    "chapterId": "ch-cpc-15",
    "subjectId": "law-cpc",
    "title": "Suits By or Against Minors & Persons of Unsound Mind (Order XXXII)",
    "order": 2,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-cpc-15-03",
    "chapterId": "ch-cpc-15",
    "subjectId": "law-cpc",
    "title": "Suits by Indigent Persons (Order XXXIII) & Appeals by Indigents (Order XLIV)",
    "order": 3,
    "mcqsCount": 5,
    "pyqsCount": 0,
    "estimatedMinutes": 18
  },
  {
    "id": "top-cpc-15-04",
    "chapterId": "ch-cpc-15",
    "subjectId": "law-cpc",
    "title": "Interpleader Suits (Section 88 & Order XXXV) & Summary Suits (Order XXXVII)",
    "order": 4,
    "mcqsCount": 5,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-cpc-16-01",
    "chapterId": "ch-cpc-16",
    "subjectId": "law-cpc",
    "title": "First Appeal under Section 96 & Order XLI: Rights, Powers & Consent Bar",
    "order": 1,
    "mcqsCount": 7,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-16-02",
    "chapterId": "ch-cpc-16",
    "subjectId": "law-cpc",
    "title": "Second Appeal under Section 100 & Order XLII: Substantial Question of Law",
    "order": 2,
    "mcqsCount": 7,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-16-03",
    "chapterId": "ch-cpc-16",
    "subjectId": "law-cpc",
    "title": "Appeals from Orders under Sections 104\u2013106 & Order XLIII",
    "order": 3,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 18
  },
  {
    "id": "top-cpc-17-01",
    "chapterId": "ch-cpc-17",
    "subjectId": "law-cpc",
    "title": "Reference to High Court under Section 113 & Order XLVI",
    "order": 1,
    "mcqsCount": 6,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-cpc-17-02",
    "chapterId": "ch-cpc-17",
    "subjectId": "law-cpc",
    "title": "Review of Judgment under Section 114 & Order XLVII: Grounds & Limitations",
    "order": 2,
    "mcqsCount": 7,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-17-03",
    "chapterId": "ch-cpc-17",
    "subjectId": "law-cpc",
    "title": "Revisional Jurisdiction under Section 115 vs Article 227 Supervisory Jurisdiction",
    "order": 3,
    "mcqsCount": 7,
    "pyqsCount": 0,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-18-01",
    "chapterId": "ch-cpc-18",
    "subjectId": "law-cpc",
    "title": "Section 89 & Alternative Dispute Resolution (ADR) Mechanisms: Afcons Analysis",
    "order": 1,
    "mcqsCount": 7,
    "pyqsCount": 0,
    "estimatedMinutes": 18
  },
  {
    "id": "top-cpc-18-02",
    "chapterId": "ch-cpc-18",
    "subjectId": "law-cpc",
    "title": "Commissions under Sections 75\u201378 & Order XXVI: Powers & Evidentiary Value",
    "order": 2,
    "mcqsCount": 7,
    "pyqsCount": 1,
    "estimatedMinutes": 18
  },
  {
    "id": "top-cpc-18-03",
    "chapterId": "ch-cpc-18",
    "subjectId": "law-cpc",
    "title": "Doctrine of Restitution under Section 144: Obligation & Conditions",
    "order": 3,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 16
  },
  {
    "id": "top-cpc-19-01",
    "chapterId": "ch-cpc-19",
    "subjectId": "law-cpc",
    "title": "UP State Amendments: Section 115 Revisional Bifurcation (District Court vs HC)",
    "order": 1,
    "mcqsCount": 7,
    "pyqsCount": 1,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-19-02",
    "chapterId": "ch-cpc-19",
    "subjectId": "law-cpc",
    "title": "UP Order XV Rule 5: Striking Off Defence for Failure to Deposit Rent",
    "order": 2,
    "mcqsCount": 7,
    "pyqsCount": 0,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-19-03",
    "chapterId": "ch-cpc-19",
    "subjectId": "law-cpc",
    "title": "Allahabad High Court General Rules (Civil) 1957 & Subordinate Court Practice",
    "order": 3,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 18
  },
  {
    "id": "top-cpc-20-01",
    "chapterId": "ch-cpc-20",
    "subjectId": "law-cpc",
    "title": "High-Yield Section, Order & Rule Rapid Recall Matrix",
    "order": 1,
    "mcqsCount": 7,
    "pyqsCount": 1,
    "estimatedMinutes": 22
  },
  {
    "id": "top-cpc-20-02",
    "chapterId": "ch-cpc-20",
    "subjectId": "law-cpc",
    "title": "Essential Procedural Distinctions & Common Prelims Traps",
    "order": 2,
    "mcqsCount": 7,
    "pyqsCount": 0,
    "estimatedMinutes": 20
  },
  {
    "id": "top-cpc-20-03",
    "chapterId": "ch-cpc-20",
    "subjectId": "law-cpc",
    "title": "Landmark Supreme Court & Allahabad High Court Precedents in CPC",
    "order": 3,
    "mcqsCount": 6,
    "pyqsCount": 0,
    "estimatedMinutes": 20
  }
];

  if (typeof module !== "undefined" && module.exports) {
    module.exports = DATA;
  }
  if (typeof window !== "undefined") {
    global.CPC_TOPICS = DATA;
  }
})(typeof window !== "undefined" ? window : global);
