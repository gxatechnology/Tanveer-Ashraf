import json

# 20 Chapters with exact PYQ counts summing to 60, MCQs summing to 400, Topics summing to 57
chapters = [
  {
    'id': 'ch-cpc-01',
    'subjectId': 'law-cpc',
    'number': 1,
    'title': 'Introduction, Nature, Structure & Key Definitions',
    'scope': 'Nature, purpose and scheme of CPC, substantive vs procedural law, Sections vs Orders & Rules, Section 2 definitions: decree, preliminary/final/deemed decree, order, judgment, mesne profits, legal representative, foreign judgment',
    'topicsCount': 3,
    'mcqsCount': 20,
    'pyqsCount': 5,
    'estimatedMinutes': 60,
    'weightage': 'Very High'
  },
  {
    'id': 'ch-cpc-02',
    'subjectId': 'law-cpc',
    'number': 2,
    'title': 'Civil Court Jurisdiction & Place of Suing',
    'scope': 'Section 9 jurisdiction over civil suits, express and implied bars, subject-matter, pecuniary and territorial jurisdiction, place of suing (Sections 15–20), Section 21 objections to jurisdiction, transfer of suits (Sections 22–25)',
    'topicsCount': 3,
    'mcqsCount': 20,
    'pyqsCount': 4,
    'estimatedMinutes': 55,
    'weightage': 'Very High'
  },
  {
    'id': 'ch-cpc-03',
    'subjectId': 'law-cpc',
    'number': 3,
    'title': 'Res Sub Judice & Res Judicata',
    'scope': 'Section 10 stay of suit (Res Sub Judice), Section 11 Res Judicata essential elements, 8 Explanations, Constructive Res Judicata (Explanation IV), res judicata between co-defendants, Section 12 bar to further suit',
    'topicsCount': 3,
    'mcqsCount': 20,
    'pyqsCount': 5,
    'estimatedMinutes': 65,
    'weightage': 'Very High'
  },
  {
    'id': 'ch-cpc-04',
    'subjectId': 'law-cpc',
    'number': 4,
    'title': 'Institution of Civil Suits & Cause of Action',
    'scope': 'Section 26 and Order IV institution of suits by plaint, verification and affidavits (Section 26(2)), cause of action elements, framing of suit, Order II Rule 2 splitting of claims and joinder of causes of action',
    'topicsCount': 2,
    'mcqsCount': 20,
    'pyqsCount': 3,
    'estimatedMinutes': 45,
    'weightage': 'High'
  },
  {
    'id': 'ch-cpc-05',
    'subjectId': 'law-cpc',
    'number': 5,
    'title': 'Parties to Suits & Representative Proceedings',
    'scope': 'Order I: Joinder of plaintiffs and defendants, necessary vs proper parties, non-joinder and misjoinder (Rule 9 and 13), representative suits under Order I Rule 8, adding or striking out parties under Rule 10',
    'topicsCount': 2,
    'mcqsCount': 20,
    'pyqsCount': 2,
    'estimatedMinutes': 50,
    'weightage': 'High'
  },
  {
    'id': 'ch-cpc-06',
    'subjectId': 'law-cpc',
    'number': 6,
    'title': 'Pleadings & Amendment of Pleadings',
    'scope': 'Order VI general rules of pleadings: material facts not evidence (Rule 2), signing and verification (Rule 14-15), amendment of pleadings under Order VI Rule 17-18, proviso regarding due diligence, striking out scandalous pleadings (Rule 16)',
    'topicsCount': 2,
    'mcqsCount': 20,
    'pyqsCount': 3,
    'estimatedMinutes': 50,
    'weightage': 'Very High'
  },
  {
    'id': 'ch-cpc-07',
    'subjectId': 'law-cpc',
    'number': 7,
    'title': 'Plaint, Rejection, Return, Written Statement, Set-off & Counterclaim',
    'scope': 'Order VII plaint particulars, return of plaint (Rule 10), rejection of plaint (Rule 11 grounds), Order VIII written statement filing timelines (Rule 1), legal set-off (Rule 6) vs equitable set-off, counterclaim (Rules 6A–6G)',
    'topicsCount': 3,
    'mcqsCount': 20,
    'pyqsCount': 5,
    'estimatedMinutes': 65,
    'weightage': 'Very High'
  },
  {
    'id': 'ch-cpc-08',
    'subjectId': 'law-cpc',
    'number': 8,
    'title': 'Summons, Service, Appearance & Non-Appearance',
    'scope': 'Order V summons to defendant, personal, postal, electronic and substituted service (Rule 20), Order IX appearance, dismissal for default and restoration (Rules 2-4, 8-9), ex-parte decree (Rule 6), setting aside ex-parte decree (Rule 13)',
    'topicsCount': 3,
    'mcqsCount': 20,
    'pyqsCount': 4,
    'estimatedMinutes': 60,
    'weightage': 'Very High'
  },
  {
    'id': 'ch-cpc-09',
    'subjectId': 'law-cpc',
    'number': 9,
    'title': 'Discovery, Inspection, Admissions & Production of Documents',
    'scope': 'Order X court examination of parties, Order XI interrogatories and discovery of documents, inspection, Order XII notice to admit and judgment on admissions (Rule 6), Order XIII production, impounding and return of documents',
    'topicsCount': 2,
    'mcqsCount': 20,
    'pyqsCount': 2,
    'estimatedMinutes': 45,
    'weightage': 'Medium'
  },
  {
    'id': 'ch-cpc-10',
    'subjectId': 'law-cpc',
    'number': 10,
    'title': 'Framing of Issues, Adjournments & Civil Trial',
    'scope': 'Order XIV framing of issues of fact and law, disposal at first hearing (Order XV), summoning witnesses (Order XVI/XVI-A), Order XVII adjournments (Rule 1 limit), Order XVIII hearing of suit and examination of witnesses',
    'topicsCount': 2,
    'mcqsCount': 20,
    'pyqsCount': 2,
    'estimatedMinutes': 50,
    'weightage': 'High'
  },
  {
    'id': 'ch-cpc-11',
    'subjectId': 'law-cpc',
    'number': 11,
    'title': 'Judgment, Decree, Interest & Costs',
    'scope': 'Section 33 and Order XX judgment and decree pronouncement timelines, preliminary vs final decree, Section 34 interest (contractual, pendente lite, future 6%), Section 35 general costs, Section 35A compensatory costs, Section 35B delay costs, Order XXA',
    'topicsCount': 3,
    'mcqsCount': 20,
    'pyqsCount': 3,
    'estimatedMinutes': 55,
    'weightage': 'High'
  },
  {
    'id': 'ch-cpc-12',
    'subjectId': 'law-cpc',
    'number': 12,
    'title': 'Execution of Decrees: Principles, Attachment, Sale & Arrest',
    'scope': 'Sections 36–74 & Order XXI execution: executing court powers, transfer, modes of execution, arrest & detention (S. 51, 55, 58 & S. 56 bar on women), Section 60 property exempt from attachment, Precepts (S. 46), Garnishee orders (R. 46A-46I), objections (R. 58), resistance (R. 97-106)',
    'topicsCount': 4,
    'mcqsCount': 20,
    'pyqsCount': 5,
    'estimatedMinutes': 75,
    'weightage': 'Very High'
  },
  {
    'id': 'ch-cpc-13',
    'subjectId': 'law-cpc',
    'number': 13,
    'title': 'Temporary Injunctions, Interlocutory Orders & Inherent Powers',
    'scope': 'Sections 94-95, Order XXXVIII arrest and attachment before judgment, Order XXXIX temporary injunctions (Rules 1-2, 3A, 4) triple test, Order XL receivers, Section 148A caveat petitions, Section 151 inherent powers, Section 148 enlargement of time, Section 152-153 amendments',
    'topicsCount': 4,
    'mcqsCount': 20,
    'pyqsCount': 5,
    'estimatedMinutes': 70,
    'weightage': 'Very High'
  },
  {
    'id': 'ch-cpc-14',
    'subjectId': 'law-cpc',
    'number': 14,
    'title': 'Death of Parties, Abatement, Withdrawal & Compromise of Suits',
    'scope': 'Order XXII death, marriage and insolvency of parties, survival of right to sue, abatement, setting aside abatement, Order XXIII withdrawal of suit (Rule 1), compromise of suit (Rule 3), bar to fresh suit on compromise (Rule 3A)',
    'topicsCount': 2,
    'mcqsCount': 20,
    'pyqsCount': 2,
    'estimatedMinutes': 45,
    'weightage': 'High'
  },
  {
    'id': 'ch-cpc-15',
    'subjectId': 'law-cpc',
    'number': 15,
    'title': 'Special Civil Suits: Government, Minors, Indigents, Interpleader & Summary Suits',
    'scope': 'Suits by/against Government and Public Officers (Sections 79–82, Order XXVII, Section 80 notice), suits by/against minors and unsound mind (Order XXXII), indigent persons (Order XXXIII), Interpleader suits (Section 88, Order XXXV), Summary Procedure (Order XXXVII)',
    'topicsCount': 4,
    'mcqsCount': 20,
    'pyqsCount': 3,
    'estimatedMinutes': 60,
    'weightage': 'High'
  },
  {
    'id': 'ch-cpc-16',
    'subjectId': 'law-cpc',
    'number': 16,
    'title': 'Appeals from Original Decrees, Appellate Decrees & Orders',
    'scope': 'First Appeal under Section 96 & Order XLI (grounds, powers of appellate court, S. 96(3) bar against consent decree, S. 96(4) petty suits), Second Appeal under Section 100 & Order XLII (substantial question of law, S. 102 bar), Appeals from Orders (Sections 104-106, Order XLIII)',
    'topicsCount': 3,
    'mcqsCount': 20,
    'pyqsCount': 2,
    'estimatedMinutes': 60,
    'weightage': 'Very High'
  },
  {
    'id': 'ch-cpc-17',
    'subjectId': 'law-cpc',
    'number': 17,
    'title': 'Reference, Review, Revision & Supervisory Jurisdiction',
    'scope': 'Section 113 & Order XLVI Reference to High Court, Section 114 & Order XLVII Review of Judgment (error apparent on face of record, discovery of new evidence), Section 115 Revisional Jurisdiction, distinction between Revision and Article 227 supervisory writ',
    'topicsCount': 3,
    'mcqsCount': 20,
    'pyqsCount': 2,
    'estimatedMinutes': 55,
    'weightage': 'Very High'
  },
  {
    'id': 'ch-cpc-18',
    'subjectId': 'law-cpc',
    'number': 18,
    'title': 'Alternative Dispute Resolution, Commissions & Restitution',
    'scope': 'Section 89 ADR processes (arbitration, conciliation, judicial settlement, Lok Adalat, mediation), Sections 75–78 & Order XXVI Commissions (witnesses, local investigations, accounts, scientific inquiries), Section 144 Doctrine of Restitution',
    'topicsCount': 3,
    'mcqsCount': 20,
    'pyqsCount': 1,
    'estimatedMinutes': 50,
    'weightage': 'High'
  },
  {
    'id': 'ch-cpc-19',
    'subjectId': 'law-cpc',
    'number': 19,
    'title': 'CPC in Uttar Pradesh: High Court Rules & State Amendments',
    'scope': 'Applicable Uttar Pradesh local amendments: UP amendment to Section 115 (bifurcation between District Court and High Court revision), UP Order XV Rule 5 (striking off defence for failure to deposit rent), Allahabad High Court General Rules (Civil) 1957 and civil court practice in UP',
    'topicsCount': 3,
    'mcqsCount': 20,
    'pyqsCount': 1,
    'estimatedMinutes': 50,
    'weightage': 'Very High'
  },
  {
    'id': 'ch-cpc-20',
    'subjectId': 'law-cpc',
    'number': 20,
    'title': 'Comprehensive Civil Procedure Mastery, Procedural Distinctions & Revision',
    'scope': 'High-yield Section, Order and Rule recall matrix, essential procedural distinctions (Res Judicata vs Issue Estoppel, Set-off vs Counterclaim, Return vs Rejection, Review vs Appeal vs Revision), landmark Supreme Court and Allahabad High Court precedents, prelims traps',
    'topicsCount': 3,
    'mcqsCount': 20,
    'pyqsCount': 1,
    'estimatedMinutes': 60,
    'weightage': 'Very High'
  }
]

# Write cpc-chapters.js
with open('assets/learning/data/cpc/cpc-chapters.js', 'w', encoding='utf-8') as f:
    f.write('/**\n * TANVEER ASHRAF — JUDICIAL PREP 2026–27\n * CPC Chapters Metadata Module\n */\n')
    f.write('(function(global) {\n  "use strict";\n\n')
    f.write('  const DATA = ' + json.dumps(chapters, indent=2) + ';\n\n')
    f.write('  if (typeof module !== "undefined" && module.exports) {\n    module.exports = DATA;\n  }\n')
    f.write('  if (typeof window !== "undefined") {\n    global.CPC_CHAPTERS = DATA;\n  }\n')
    f.write('})(typeof window !== "undefined" ? window : global);\n')

print(f"Generated cpc-chapters.js with {len(chapters)} chapters.")
print(f"Total topics: {sum(c['topicsCount'] for c in chapters)}")
print(f"Total MCQs: {sum(c['mcqsCount'] for c in chapters)}")
print(f"Total PYQs: {sum(c['pyqsCount'] for c in chapters)}")

# Now author all 57 topics
topics = [
  # Chapter 1
  {"id": "top-cpc-01-01", "chapterId": "ch-cpc-01", "subjectId": "law-cpc", "title": "Nature, Scheme & Structure of CPC: Substantive vs Procedural Law", "order": 1, "mcqsCount": 7, "pyqsCount": 2, "estimatedMinutes": 20},
  {"id": "top-cpc-01-02", "chapterId": "ch-cpc-01", "subjectId": "law-cpc", "title": "Section 2 Definitions: Decree, Preliminary vs Final & Deemed Decree", "order": 2, "mcqsCount": 7, "pyqsCount": 2, "estimatedMinutes": 22},
  {"id": "top-cpc-01-03", "chapterId": "ch-cpc-01", "subjectId": "law-cpc", "title": "Orders, Judgments, Legal Representative, Mesne Profits & Foreign Judgment", "order": 3, "mcqsCount": 6, "pyqsCount": 1, "estimatedMinutes": 18},
  
  # Chapter 2
  {"id": "top-cpc-02-01", "chapterId": "ch-cpc-02", "subjectId": "law-cpc", "title": "Jurisdiction of Civil Courts under Section 9: Suits of Civil Nature & Bars", "order": 1, "mcqsCount": 7, "pyqsCount": 2, "estimatedMinutes": 20},
  {"id": "top-cpc-02-02", "chapterId": "ch-cpc-02", "subjectId": "law-cpc", "title": "Pecuniary & Territorial Jurisdiction: Place of Suing (Sections 15–20)", "order": 2, "mcqsCount": 7, "pyqsCount": 1, "estimatedMinutes": 20},
  {"id": "top-cpc-02-03", "chapterId": "ch-cpc-02", "subjectId": "law-cpc", "title": "Objections to Jurisdiction (Section 21) & Transfer of Suits (Sections 22–25)", "order": 3, "mcqsCount": 6, "pyqsCount": 1, "estimatedMinutes": 18},
  
  # Chapter 3
  {"id": "top-cpc-03-01", "chapterId": "ch-cpc-03", "subjectId": "law-cpc", "title": "Stay of Suit: Doctrine of Res Sub Judice under Section 10", "order": 1, "mcqsCount": 6, "pyqsCount": 2, "estimatedMinutes": 20},
  {"id": "top-cpc-03-02", "chapterId": "ch-cpc-03", "subjectId": "law-cpc", "title": "Doctrine of Res Judicata under Section 11: Essential Conditions & Scope", "order": 2, "mcqsCount": 7, "pyqsCount": 2, "estimatedMinutes": 24},
  {"id": "top-cpc-03-03", "chapterId": "ch-cpc-03", "subjectId": "law-cpc", "title": "The 8 Explanations of Section 11, Constructive Res Judicata & Co-Defendants", "order": 3, "mcqsCount": 7, "pyqsCount": 1, "estimatedMinutes": 22},
  
  # Chapter 4
  {"id": "top-cpc-04-01", "chapterId": "ch-cpc-04", "subjectId": "law-cpc", "title": "Institution of Suits under Section 26 & Order IV: Affidavits & Verification", "order": 1, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 22},
  {"id": "top-cpc-04-02", "chapterId": "ch-cpc-04", "subjectId": "law-cpc", "title": "Cause of Action, Framing of Suit & Order II Rule 2 Bar on Splitting Claims", "order": 2, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 24},
  
  # Chapter 5
  {"id": "top-cpc-05-01", "chapterId": "ch-cpc-05", "subjectId": "law-cpc", "title": "Parties to Suit: Joinder, Necessary vs Proper Parties & Non-Joinder (Order I)", "order": 1, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 25},
  {"id": "top-cpc-05-02", "chapterId": "ch-cpc-05", "subjectId": "law-cpc", "title": "Representative Suits (Order I Rule 8) & Adding/Striking Parties (Order I Rule 10)", "order": 2, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 25},
  
  # Chapter 6
  {"id": "top-cpc-06-01", "chapterId": "ch-cpc-06", "subjectId": "law-cpc", "title": "Pleadings: Material Facts, Verification & Striking Out Pleadings (Order VI)", "order": 1, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 24},
  {"id": "top-cpc-06-02", "chapterId": "ch-cpc-06", "subjectId": "law-cpc", "title": "Amendment of Pleadings under Order VI Rule 17 & Due Diligence Proviso", "order": 2, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 26},
  
  # Chapter 7
  {"id": "top-cpc-07-01", "chapterId": "ch-cpc-07", "subjectId": "law-cpc", "title": "Plaint: Return of Plaint (O. VII R. 10) vs Rejection of Plaint (O. VII R. 11)", "order": 1, "mcqsCount": 7, "pyqsCount": 2, "estimatedMinutes": 24},
  {"id": "top-cpc-07-02", "chapterId": "ch-cpc-07", "subjectId": "law-cpc", "title": "Written Statement & Time Limits under Order VIII Rule 1 (30 to 90 Days)", "order": 2, "mcqsCount": 6, "pyqsCount": 1, "estimatedMinutes": 20},
  {"id": "top-cpc-07-03", "chapterId": "ch-cpc-07", "subjectId": "law-cpc", "title": "Set-Off (Legal & Equitable) vs Counter-Claim (Order VIII Rules 6 & 6A–6G)", "order": 3, "mcqsCount": 7, "pyqsCount": 2, "estimatedMinutes": 22},
  
  # Chapter 8
  {"id": "top-cpc-08-01", "chapterId": "ch-cpc-08", "subjectId": "law-cpc", "title": "Summons to Defendant: Modes of Service & Substituted Service (Order V)", "order": 1, "mcqsCount": 7, "pyqsCount": 2, "estimatedMinutes": 20},
  {"id": "top-cpc-08-02", "chapterId": "ch-cpc-08", "subjectId": "law-cpc", "title": "Appearance & Non-Appearance: Dismissal for Default & Remedies (Order IX)", "order": 2, "mcqsCount": 6, "pyqsCount": 1, "estimatedMinutes": 20},
  {"id": "top-cpc-08-03", "chapterId": "ch-cpc-08", "subjectId": "law-cpc", "title": "Ex Parte Decrees: Remedies & Setting Aside under Order IX Rule 13", "order": 3, "mcqsCount": 7, "pyqsCount": 1, "estimatedMinutes": 22},
  
  # Chapter 9
  {"id": "top-cpc-09-01", "chapterId": "ch-cpc-09", "subjectId": "law-cpc", "title": "Examination of Parties (Order X) & Discovery and Interrogatories (Order XI)", "order": 1, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 22},
  {"id": "top-cpc-09-02", "chapterId": "ch-cpc-09", "subjectId": "law-cpc", "title": "Admissions (Order XII) & Production and Return of Documents (Order XIII)", "order": 2, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 22},
  
  # Chapter 10
  {"id": "top-cpc-10-01", "chapterId": "ch-cpc-10", "subjectId": "law-cpc", "title": "Settlement of Issues (Order XIV) & Disposal at First Hearing (Order XV)", "order": 1, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 24},
  {"id": "top-cpc-10-02", "chapterId": "ch-cpc-10", "subjectId": "law-cpc", "title": "Witness Attendance (Order XVI), Adjournments (Order XVII) & Trial (Order XVIII)", "order": 2, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 26},
  
  # Chapter 11
  {"id": "top-cpc-11-01", "chapterId": "ch-cpc-11", "subjectId": "law-cpc", "title": "Judgment and Decree under Section 33 & Order XX: Distinction & Timelines", "order": 1, "mcqsCount": 7, "pyqsCount": 1, "estimatedMinutes": 20},
  {"id": "top-cpc-11-02", "chapterId": "ch-cpc-11", "subjectId": "law-cpc", "title": "Statutory Interest under Section 34: Commercial, Pendente Lite & Future Interest", "order": 2, "mcqsCount": 6, "pyqsCount": 1, "estimatedMinutes": 18},
  {"id": "top-cpc-11-03", "chapterId": "ch-cpc-11", "subjectId": "law-cpc", "title": "Costs: General (S. 35), Compensatory (S. 35A), Delay Costs (S. 35B) & Order XXA", "order": 3, "mcqsCount": 7, "pyqsCount": 1, "estimatedMinutes": 20},
  
  # Chapter 12
  {"id": "top-cpc-12-01", "chapterId": "ch-cpc-12", "subjectId": "law-cpc", "title": "Executing Court Powers, Jurisdiction & Transfer of Decrees (Sections 36–46)", "order": 1, "mcqsCount": 5, "pyqsCount": 1, "estimatedMinutes": 20},
  {"id": "top-cpc-12-02", "chapterId": "ch-cpc-12", "subjectId": "law-cpc", "title": "Modes of Execution: Arrest & Detention (S. 51, 55, 58 & S. 56 Bar on Women)", "order": 2, "mcqsCount": 5, "pyqsCount": 2, "estimatedMinutes": 20},
  {"id": "top-cpc-12-03", "chapterId": "ch-cpc-12", "subjectId": "law-cpc", "title": "Attachment of Property: Section 60 Exemptions & Garnishee Orders (O. XXI)", "order": 3, "mcqsCount": 5, "pyqsCount": 1, "estimatedMinutes": 20},
  {"id": "top-cpc-12-04", "chapterId": "ch-cpc-12", "subjectId": "law-cpc", "title": "Objections to Execution (O. XXI R. 58) & Resistance to Delivery (O. XXI R. 97–106)", "order": 4, "mcqsCount": 5, "pyqsCount": 1, "estimatedMinutes": 20},
  
  # Chapter 13
  {"id": "top-cpc-13-01", "chapterId": "ch-cpc-13", "subjectId": "law-cpc", "title": "Arrest & Attachment Before Judgment under Order XXXVIII (Rules 1–13)", "order": 1, "mcqsCount": 5, "pyqsCount": 1, "estimatedMinutes": 18},
  {"id": "top-cpc-13-02", "chapterId": "ch-cpc-13", "subjectId": "law-cpc", "title": "Temporary Injunctions under Order XXXIX Rules 1–5: The Triple Test", "order": 2, "mcqsCount": 5, "pyqsCount": 2, "estimatedMinutes": 20},
  {"id": "top-cpc-13-03", "chapterId": "ch-cpc-13", "subjectId": "law-cpc", "title": "Interlocutory Orders, Receivers (Order XL) & Caveat Petitions (Section 148A)", "order": 3, "mcqsCount": 5, "pyqsCount": 1, "estimatedMinutes": 18},
  {"id": "top-cpc-13-04", "chapterId": "ch-cpc-13", "subjectId": "law-cpc", "title": "Inherent Powers of Court (Section 151) & Amendments of Decrees (Sections 152–153)", "order": 4, "mcqsCount": 5, "pyqsCount": 1, "estimatedMinutes": 18},
  
  # Chapter 14
  {"id": "top-cpc-14-01", "chapterId": "ch-cpc-14", "subjectId": "law-cpc", "title": "Death, Marriage & Insolvency of Parties: Abatement & Substitution (Order XXII)", "order": 1, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 22},
  {"id": "top-cpc-14-02", "chapterId": "ch-cpc-14", "subjectId": "law-cpc", "title": "Withdrawal of Suits (Order XXIII Rule 1) & Lawful Compromise (O. XXIII R. 3)", "order": 2, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 22},
  
  # Chapter 15
  {"id": "top-cpc-15-01", "chapterId": "ch-cpc-15", "subjectId": "law-cpc", "title": "Suits By or Against Government & Public Officers (Sections 79–82 & Order XXVII)", "order": 1, "mcqsCount": 5, "pyqsCount": 1, "estimatedMinutes": 18},
  {"id": "top-cpc-15-02", "chapterId": "ch-cpc-15", "subjectId": "law-cpc", "title": "Suits By or Against Minors & Persons of Unsound Mind (Order XXXII)", "order": 2, "mcqsCount": 5, "pyqsCount": 1, "estimatedMinutes": 18},
  {"id": "top-cpc-15-03", "chapterId": "ch-cpc-15", "subjectId": "law-cpc", "title": "Suits by Indigent Persons (Order XXXIII) & Appeals by Indigents (Order XLIV)", "order": 3, "mcqsCount": 5, "pyqsCount": 0, "estimatedMinutes": 18},
  {"id": "top-cpc-15-04", "chapterId": "ch-cpc-15", "subjectId": "law-cpc", "title": "Interpleader Suits (Section 88 & Order XXXV) & Summary Suits (Order XXXVII)", "order": 4, "mcqsCount": 5, "pyqsCount": 1, "estimatedMinutes": 18},
  
  # Chapter 16
  {"id": "top-cpc-16-01", "chapterId": "ch-cpc-16", "subjectId": "law-cpc", "title": "First Appeal under Section 96 & Order XLI: Rights, Powers & Consent Bar", "order": 1, "mcqsCount": 7, "pyqsCount": 1, "estimatedMinutes": 20},
  {"id": "top-cpc-16-02", "chapterId": "ch-cpc-16", "subjectId": "law-cpc", "title": "Second Appeal under Section 100 & Order XLII: Substantial Question of Law", "order": 2, "mcqsCount": 7, "pyqsCount": 1, "estimatedMinutes": 20},
  {"id": "top-cpc-16-03", "chapterId": "ch-cpc-16", "subjectId": "law-cpc", "title": "Appeals from Orders under Sections 104–106 & Order XLIII", "order": 3, "mcqsCount": 6, "pyqsCount": 0, "estimatedMinutes": 18},
  
  # Chapter 17
  {"id": "top-cpc-17-01", "chapterId": "ch-cpc-17", "subjectId": "law-cpc", "title": "Reference to High Court under Section 113 & Order XLVI", "order": 1, "mcqsCount": 6, "pyqsCount": 1, "estimatedMinutes": 18},
  {"id": "top-cpc-17-02", "chapterId": "ch-cpc-17", "subjectId": "law-cpc", "title": "Review of Judgment under Section 114 & Order XLVII: Grounds & Limitations", "order": 2, "mcqsCount": 7, "pyqsCount": 1, "estimatedMinutes": 20},
  {"id": "top-cpc-17-03", "chapterId": "ch-cpc-17", "subjectId": "law-cpc", "title": "Revisional Jurisdiction under Section 115 vs Article 227 Supervisory Jurisdiction", "order": 3, "mcqsCount": 7, "pyqsCount": 0, "estimatedMinutes": 20},
  
  # Chapter 18
  {"id": "top-cpc-18-01", "chapterId": "ch-cpc-18", "subjectId": "law-cpc", "title": "Section 89 & Alternative Dispute Resolution (ADR) Mechanisms: Afcons Analysis", "order": 1, "mcqsCount": 7, "pyqsCount": 0, "estimatedMinutes": 18},
  {"id": "top-cpc-18-02", "chapterId": "ch-cpc-18", "subjectId": "law-cpc", "title": "Commissions under Sections 75–78 & Order XXVI: Powers & Evidentiary Value", "order": 2, "mcqsCount": 7, "pyqsCount": 1, "estimatedMinutes": 18},
  {"id": "top-cpc-18-03", "chapterId": "ch-cpc-18", "subjectId": "law-cpc", "title": "Doctrine of Restitution under Section 144: Obligation & Conditions", "order": 3, "mcqsCount": 6, "pyqsCount": 0, "estimatedMinutes": 16},
  
  # Chapter 19
  {"id": "top-cpc-19-01", "chapterId": "ch-cpc-19", "subjectId": "law-cpc", "title": "UP State Amendments: Section 115 Revisional Bifurcation (District Court vs HC)", "order": 1, "mcqsCount": 7, "pyqsCount": 1, "estimatedMinutes": 20},
  {"id": "top-cpc-19-02", "chapterId": "ch-cpc-19", "subjectId": "law-cpc", "title": "UP Order XV Rule 5: Striking Off Defence for Failure to Deposit Rent", "order": 2, "mcqsCount": 7, "pyqsCount": 0, "estimatedMinutes": 20},
  {"id": "top-cpc-19-03", "chapterId": "ch-cpc-19", "subjectId": "law-cpc", "title": "Allahabad High Court General Rules (Civil) 1957 & Subordinate Court Practice", "order": 3, "mcqsCount": 6, "pyqsCount": 0, "estimatedMinutes": 18},
  
  # Chapter 20
  {"id": "top-cpc-20-01", "chapterId": "ch-cpc-20", "subjectId": "law-cpc", "title": "High-Yield Section, Order & Rule Rapid Recall Matrix", "order": 1, "mcqsCount": 7, "pyqsCount": 1, "estimatedMinutes": 22},
  {"id": "top-cpc-20-02", "chapterId": "ch-cpc-20", "subjectId": "law-cpc", "title": "Essential Procedural Distinctions & Common Prelims Traps", "order": 2, "mcqsCount": 7, "pyqsCount": 0, "estimatedMinutes": 20},
  {"id": "top-cpc-20-03", "chapterId": "ch-cpc-20", "subjectId": "law-cpc", "title": "Landmark Supreme Court & Allahabad High Court Precedents in CPC", "order": 3, "mcqsCount": 6, "pyqsCount": 0, "estimatedMinutes": 20}
]

# Write cpc-topics.js
with open('assets/learning/data/cpc/cpc-topics.js', 'w', encoding='utf-8') as f:
    f.write('/**\n * TANVEER ASHRAF — JUDICIAL PREP 2026–27\n * CPC Topics Metadata Module\n */\n')
    f.write('(function(global) {\n  "use strict";\n\n')
    f.write('  const DATA = ' + json.dumps(topics, indent=2) + ';\n\n')
    f.write('  if (typeof module !== "undefined" && module.exports) {\n    module.exports = DATA;\n  }\n')
    f.write('  if (typeof window !== "undefined") {\n    global.CPC_TOPICS = DATA;\n  }\n')
    f.write('})(typeof window !== "undefined" ? window : global);\n')

print(f"Generated cpc-topics.js with {len(topics)} topics.")
print(f"Total MCQs across topics: {sum(t['mcqsCount'] for t in topics)}")
print(f"Total PYQs across topics: {sum(t['pyqsCount'] for t in topics)}")
