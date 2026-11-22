/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * CPC Chapters Metadata Module
 */
(function(global) {
  "use strict";

  const DATA = [
  {
    "id": "ch-cpc-01",
    "subjectId": "law-cpc",
    "number": 1,
    "title": "Introduction, Nature, Structure & Key Definitions",
    "scope": "Nature, purpose and scheme of CPC, substantive vs procedural law, Sections vs Orders & Rules, Section 2 definitions: decree, preliminary/final/deemed decree, order, judgment, mesne profits, legal representative, foreign judgment",
    "topicsCount": 3,
    "mcqsCount": 20,
    "pyqsCount": 5,
    "estimatedMinutes": 60,
    "weightage": "Very High"
  },
  {
    "id": "ch-cpc-02",
    "subjectId": "law-cpc",
    "number": 2,
    "title": "Civil Court Jurisdiction & Place of Suing",
    "scope": "Section 9 jurisdiction over civil suits, express and implied bars, subject-matter, pecuniary and territorial jurisdiction, place of suing (Sections 15\u201320), Section 21 objections to jurisdiction, transfer of suits (Sections 22\u201325)",
    "topicsCount": 3,
    "mcqsCount": 20,
    "pyqsCount": 4,
    "estimatedMinutes": 55,
    "weightage": "Very High"
  },
  {
    "id": "ch-cpc-03",
    "subjectId": "law-cpc",
    "number": 3,
    "title": "Res Sub Judice & Res Judicata",
    "scope": "Section 10 stay of suit (Res Sub Judice), Section 11 Res Judicata essential elements, 8 Explanations, Constructive Res Judicata (Explanation IV), res judicata between co-defendants, Section 12 bar to further suit",
    "topicsCount": 3,
    "mcqsCount": 20,
    "pyqsCount": 5,
    "estimatedMinutes": 65,
    "weightage": "Very High"
  },
  {
    "id": "ch-cpc-04",
    "subjectId": "law-cpc",
    "number": 4,
    "title": "Institution of Civil Suits & Cause of Action",
    "scope": "Section 26 and Order IV institution of suits by plaint, verification and affidavits (Section 26(2)), cause of action elements, framing of suit, Order II Rule 2 splitting of claims and joinder of causes of action",
    "topicsCount": 2,
    "mcqsCount": 20,
    "pyqsCount": 3,
    "estimatedMinutes": 45,
    "weightage": "High"
  },
  {
    "id": "ch-cpc-05",
    "subjectId": "law-cpc",
    "number": 5,
    "title": "Parties to Suits & Representative Proceedings",
    "scope": "Order I: Joinder of plaintiffs and defendants, necessary vs proper parties, non-joinder and misjoinder (Rule 9 and 13), representative suits under Order I Rule 8, adding or striking out parties under Rule 10",
    "topicsCount": 2,
    "mcqsCount": 20,
    "pyqsCount": 2,
    "estimatedMinutes": 50,
    "weightage": "High"
  },
  {
    "id": "ch-cpc-06",
    "subjectId": "law-cpc",
    "number": 6,
    "title": "Pleadings & Amendment of Pleadings",
    "scope": "Order VI general rules of pleadings: material facts not evidence (Rule 2), signing and verification (Rule 14-15), amendment of pleadings under Order VI Rule 17-18, proviso regarding due diligence, striking out scandalous pleadings (Rule 16)",
    "topicsCount": 2,
    "mcqsCount": 20,
    "pyqsCount": 3,
    "estimatedMinutes": 50,
    "weightage": "Very High"
  },
  {
    "id": "ch-cpc-07",
    "subjectId": "law-cpc",
    "number": 7,
    "title": "Plaint, Rejection, Return, Written Statement, Set-off & Counterclaim",
    "scope": "Order VII plaint particulars, return of plaint (Rule 10), rejection of plaint (Rule 11 grounds), Order VIII written statement filing timelines (Rule 1), legal set-off (Rule 6) vs equitable set-off, counterclaim (Rules 6A\u20136G)",
    "topicsCount": 3,
    "mcqsCount": 20,
    "pyqsCount": 5,
    "estimatedMinutes": 65,
    "weightage": "Very High"
  },
  {
    "id": "ch-cpc-08",
    "subjectId": "law-cpc",
    "number": 8,
    "title": "Summons, Service, Appearance & Non-Appearance",
    "scope": "Order V summons to defendant, personal, postal, electronic and substituted service (Rule 20), Order IX appearance, dismissal for default and restoration (Rules 2-4, 8-9), ex-parte decree (Rule 6), setting aside ex-parte decree (Rule 13)",
    "topicsCount": 3,
    "mcqsCount": 20,
    "pyqsCount": 4,
    "estimatedMinutes": 60,
    "weightage": "Very High"
  },
  {
    "id": "ch-cpc-09",
    "subjectId": "law-cpc",
    "number": 9,
    "title": "Discovery, Inspection, Admissions & Production of Documents",
    "scope": "Order X court examination of parties, Order XI interrogatories and discovery of documents, inspection, Order XII notice to admit and judgment on admissions (Rule 6), Order XIII production, impounding and return of documents",
    "topicsCount": 2,
    "mcqsCount": 20,
    "pyqsCount": 2,
    "estimatedMinutes": 45,
    "weightage": "Medium"
  },
  {
    "id": "ch-cpc-10",
    "subjectId": "law-cpc",
    "number": 10,
    "title": "Framing of Issues, Adjournments & Civil Trial",
    "scope": "Order XIV framing of issues of fact and law, disposal at first hearing (Order XV), summoning witnesses (Order XVI/XVI-A), Order XVII adjournments (Rule 1 limit), Order XVIII hearing of suit and examination of witnesses",
    "topicsCount": 2,
    "mcqsCount": 20,
    "pyqsCount": 2,
    "estimatedMinutes": 50,
    "weightage": "High"
  },
  {
    "id": "ch-cpc-11",
    "subjectId": "law-cpc",
    "number": 11,
    "title": "Judgment, Decree, Interest & Costs",
    "scope": "Section 33 and Order XX judgment and decree pronouncement timelines, preliminary vs final decree, Section 34 interest (contractual, pendente lite, future 6%), Section 35 general costs, Section 35A compensatory costs, Section 35B delay costs, Order XXA",
    "topicsCount": 3,
    "mcqsCount": 20,
    "pyqsCount": 3,
    "estimatedMinutes": 55,
    "weightage": "High"
  },
  {
    "id": "ch-cpc-12",
    "subjectId": "law-cpc",
    "number": 12,
    "title": "Execution of Decrees: Principles, Attachment, Sale & Arrest",
    "scope": "Sections 36\u201374 & Order XXI execution: executing court powers, transfer, modes of execution, arrest & detention (S. 51, 55, 58 & S. 56 bar on women), Section 60 property exempt from attachment, Precepts (S. 46), Garnishee orders (R. 46A-46I), objections (R. 58), resistance (R. 97-106)",
    "topicsCount": 4,
    "mcqsCount": 20,
    "pyqsCount": 5,
    "estimatedMinutes": 75,
    "weightage": "Very High"
  },
  {
    "id": "ch-cpc-13",
    "subjectId": "law-cpc",
    "number": 13,
    "title": "Temporary Injunctions, Interlocutory Orders & Inherent Powers",
    "scope": "Sections 94-95, Order XXXVIII arrest and attachment before judgment, Order XXXIX temporary injunctions (Rules 1-2, 3A, 4) triple test, Order XL receivers, Section 148A caveat petitions, Section 151 inherent powers, Section 148 enlargement of time, Section 152-153 amendments",
    "topicsCount": 4,
    "mcqsCount": 20,
    "pyqsCount": 5,
    "estimatedMinutes": 70,
    "weightage": "Very High"
  },
  {
    "id": "ch-cpc-14",
    "subjectId": "law-cpc",
    "number": 14,
    "title": "Death of Parties, Abatement, Withdrawal & Compromise of Suits",
    "scope": "Order XXII death, marriage and insolvency of parties, survival of right to sue, abatement, setting aside abatement, Order XXIII withdrawal of suit (Rule 1), compromise of suit (Rule 3), bar to fresh suit on compromise (Rule 3A)",
    "topicsCount": 2,
    "mcqsCount": 20,
    "pyqsCount": 2,
    "estimatedMinutes": 45,
    "weightage": "High"
  },
  {
    "id": "ch-cpc-15",
    "subjectId": "law-cpc",
    "number": 15,
    "title": "Special Civil Suits: Government, Minors, Indigents, Interpleader & Summary Suits",
    "scope": "Suits by/against Government and Public Officers (Sections 79\u201382, Order XXVII, Section 80 notice), suits by/against minors and unsound mind (Order XXXII), indigent persons (Order XXXIII), Interpleader suits (Section 88, Order XXXV), Summary Procedure (Order XXXVII)",
    "topicsCount": 4,
    "mcqsCount": 20,
    "pyqsCount": 3,
    "estimatedMinutes": 60,
    "weightage": "High"
  },
  {
    "id": "ch-cpc-16",
    "subjectId": "law-cpc",
    "number": 16,
    "title": "Appeals from Original Decrees, Appellate Decrees & Orders",
    "scope": "First Appeal under Section 96 & Order XLI (grounds, powers of appellate court, S. 96(3) bar against consent decree, S. 96(4) petty suits), Second Appeal under Section 100 & Order XLII (substantial question of law, S. 102 bar), Appeals from Orders (Sections 104-106, Order XLIII)",
    "topicsCount": 3,
    "mcqsCount": 20,
    "pyqsCount": 2,
    "estimatedMinutes": 60,
    "weightage": "Very High"
  },
  {
    "id": "ch-cpc-17",
    "subjectId": "law-cpc",
    "number": 17,
    "title": "Reference, Review, Revision & Supervisory Jurisdiction",
    "scope": "Section 113 & Order XLVI Reference to High Court, Section 114 & Order XLVII Review of Judgment (error apparent on face of record, discovery of new evidence), Section 115 Revisional Jurisdiction, distinction between Revision and Article 227 supervisory writ",
    "topicsCount": 3,
    "mcqsCount": 20,
    "pyqsCount": 2,
    "estimatedMinutes": 55,
    "weightage": "Very High"
  },
  {
    "id": "ch-cpc-18",
    "subjectId": "law-cpc",
    "number": 18,
    "title": "Alternative Dispute Resolution, Commissions & Restitution",
    "scope": "Section 89 ADR processes (arbitration, conciliation, judicial settlement, Lok Adalat, mediation), Sections 75\u201378 & Order XXVI Commissions (witnesses, local investigations, accounts, scientific inquiries), Section 144 Doctrine of Restitution",
    "topicsCount": 3,
    "mcqsCount": 20,
    "pyqsCount": 1,
    "estimatedMinutes": 50,
    "weightage": "High"
  },
  {
    "id": "ch-cpc-19",
    "subjectId": "law-cpc",
    "number": 19,
    "title": "CPC in Uttar Pradesh: High Court Rules & State Amendments",
    "scope": "Applicable Uttar Pradesh local amendments: UP amendment to Section 115 (bifurcation between District Court and High Court revision), UP Order XV Rule 5 (striking off defence for failure to deposit rent), Allahabad High Court General Rules (Civil) 1957 and civil court practice in UP",
    "topicsCount": 3,
    "mcqsCount": 20,
    "pyqsCount": 1,
    "estimatedMinutes": 50,
    "weightage": "Very High"
  },
  {
    "id": "ch-cpc-20",
    "subjectId": "law-cpc",
    "number": 20,
    "title": "Comprehensive Civil Procedure Mastery, Procedural Distinctions & Revision",
    "scope": "High-yield Section, Order and Rule recall matrix, essential procedural distinctions (Res Judicata vs Issue Estoppel, Set-off vs Counterclaim, Return vs Rejection, Review vs Appeal vs Revision), landmark Supreme Court and Allahabad High Court precedents, prelims traps",
    "topicsCount": 3,
    "mcqsCount": 20,
    "pyqsCount": 1,
    "estimatedMinutes": 60,
    "weightage": "Very High"
  }
];

  if (typeof module !== "undefined" && module.exports) {
    module.exports = DATA;
  }
  if (typeof window !== "undefined") {
    global.CPC_CHAPTERS = DATA;
  }
})(typeof window !== "undefined" ? window : global);
