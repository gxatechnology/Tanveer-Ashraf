/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * CPC Section–Order–Rule Explorer Dataset
 * Curated High-Yield Index of CPC Sections, First Schedule Orders and Rules for UP PCS-J.
 * NOTE: This explorer is a curated high-yield index of 83 high-frequency statutory provisions
 * selected for examination relevance and judicial practice, not an exhaustive bare act directory
 * of all 158 sections and 51 orders.
 */
(function(global) {
  "use strict";

  const DATA = [
  {
    "id": "cpc-sec-001",
    "type": "section",
    "ref": "Section 1",
    "title": "Short Title, Commencement and Extent",
    "concept": "Enacted 21 March 1908; came into force 1 January 1909. Extends to whole of India except State of Nagaland and Tribal areas (subject to State Govt notification).",
    "plainEnglish": "The preliminary section specifying the code's territorial jurisdiction and commencement.",
    "conditions": [
      "Applicable to all civil court proceedings in regular courts.",
      "State Govts can extend provisions to exempted tribal areas by notification."
    ],
    "exceptions": [
      "Does not apply to Nagaland and tribal areas in Assam/NE unless notified.",
      "Does not affect special or local laws (Section 4)."
    ],
    "relatedTopicId": "top-cpc-01-01",
    "chapterId": "ch-cpc-01",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "UP PCS-J frequently tests the commencement date: 1 January 1909.",
    "highYield": true
  },
  {
    "id": "cpc-sec-002-02",
    "type": "section",
    "ref": "Section 2(2)",
    "title": "Definition of Decree",
    "concept": "Formal expression of an adjudication which conclusively determines rights of parties regarding all or any matters in controversy in the suit.",
    "plainEnglish": "A decree is the final judicial decision in a civil suit conclusively settling rights. It can be preliminary, final, or partly preliminary and partly final.",
    "conditions": [
      "Must be an adjudication in a suit.",
      "Must conclusively determine rights of parties on substantive matters in controversy.",
      "Must be formally expressed."
    ],
    "exceptions": [
      "Includes rejection of plaint under O. VII R. 11 and determination of questions under S. 144 (Restitution).",
      "DOES NOT INCLUDE: (a) any adjudication from which an appeal lies as an appeal from an order; (b) any order of dismissal for default."
    ],
    "relatedTopicId": "top-cpc-01-02",
    "chapterId": "ch-cpc-01",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Highest yield prelims trap: Dismissal for default is NOT a decree. Rejection of plaint IS a deemed decree.",
    "highYield": true
  },
  {
    "id": "cpc-sec-002-09",
    "type": "section",
    "ref": "Section 2(9)",
    "title": "Definition of Judgment",
    "concept": "Statement given by the Judge on the grounds of a decree or order.",
    "plainEnglish": "The detailed reasoning, statement of facts, points for determination, and judicial grounds upon which the final decree or order is based.",
    "conditions": [
      "Must contain concise statement of case.",
      "Must formulate points for determination, decision, and reasons (Order XX Rule 4)."
    ],
    "exceptions": [
      "In Courts of Small Causes, only points for determination and decision need be stated."
    ],
    "relatedTopicId": "top-cpc-01-03",
    "chapterId": "ch-cpc-01",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Judgment precedes and forms the reasoning for the decree (Section 33).",
    "highYield": true
  },
  {
    "id": "cpc-sec-002-11",
    "type": "section",
    "ref": "Section 2(11)",
    "title": "Definition of Legal Representative",
    "concept": "A person who in law represents the estate of a deceased person, including intermeddlers with the estate.",
    "plainEnglish": "Not restricted to biological heirs; anyone who intermeddles with the deceased's estate or represents the estate in representative suits.",
    "conditions": [
      "Represents estate in law.",
      "Includes intermeddler who takes possession of estate without lawful authority."
    ],
    "exceptions": [
      "Does not include mere trespasser without intention to represent estate."
    ],
    "relatedTopicId": "top-cpc-01-03",
    "chapterId": "ch-cpc-01",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "An intermeddler is explicitly included in Section 2(11) definition.",
    "highYield": true
  },
  {
    "id": "cpc-sec-002-12",
    "type": "section",
    "ref": "Section 2(12)",
    "title": "Definition of Mesne Profits",
    "concept": "Profits which the person in wrongful possession of property actually received or might with ordinary diligence have received, together with interest, but excluding profits due to improvements made by the wrongful possessor.",
    "plainEnglish": "Compensation payable by a wrongful occupier of land for profits earned or earnable during wrongful possession, including interest (usually up to 6%).",
    "conditions": [
      "Possession of defendant must be wrongful.",
      "Includes ordinary diligence profits + interest."
    ],
    "exceptions": [
      "EXCLUDES profits attributable to improvements made by person in wrongful possession."
    ],
    "relatedTopicId": "top-cpc-01-03",
    "chapterId": "ch-cpc-01",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Frequent question: Do mesne profits include profits from improvements? NO! Section 2(12) explicitly excludes improvements.",
    "highYield": true
  },
  {
    "id": "cpc-sec-002-14",
    "type": "section",
    "ref": "Section 2(14)",
    "title": "Definition of Order",
    "concept": "Formal expression of any decision of a Civil Court which is not a decree.",
    "plainEnglish": "Any court decision that does not conclusively determine substantive rights in controversy (e.g., procedural directions, adjournment orders).",
    "conditions": [
      "Must be a formal judicial decision by civil court.",
      "Must not satisfy the criteria of a decree."
    ],
    "exceptions": [
      "Orders are appealable only if specifically listed under Section 104 or Order XLIII Rule 1."
    ],
    "relatedTopicId": "top-cpc-01-03",
    "chapterId": "ch-cpc-01",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Every decree is appealable unless barred, but an order is appealable ONLY if expressly permitted.",
    "highYield": true
  },
  {
    "id": "cpc-sec-009",
    "type": "section",
    "ref": "Section 9",
    "title": "Courts to Try All Civil Suits Unless Barred",
    "concept": "Civil courts have plenary jurisdiction to try all suits of a civil nature, excepting suits of which their cognizance is either expressly or impliedly barred.",
    "plainEnglish": "The foundational grant of jurisdiction: A civil court can try any civil dispute unless a statute explicitly (express bar) or by necessary implication (implied bar) excludes it.",
    "conditions": [
      "Dispute must be of a civil nature (rights to property, worship, office, status).",
      "Cognizance must not be barred by statute."
    ],
    "exceptions": [
      "Explanation I: Right to property or office is civil even if dependent on religious rites.",
      "Explanation II: Irrelevant whether fees are attached to religious office."
    ],
    "relatedTopicId": "top-cpc-02-01",
    "chapterId": "ch-cpc-02",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "PMA Metropolitan v. Moran Mar Marthoma; Dhulabhai v. State of MP (tests for exclusion).",
    "highYield": true
  },
  {
    "id": "cpc-sec-010",
    "type": "section",
    "ref": "Section 10",
    "title": "Stay of Suit (Res Sub Judice)",
    "concept": "No Court shall proceed with trial of any suit in which matter in issue is directly and substantially in issue in a previously instituted suit between same parties in same or concurrent court.",
    "plainEnglish": "Prevents two courts of concurrent jurisdiction from simultaneously trying identical suits. The subsequent suit is stayed, NOT dismissed.",
    "conditions": [
      "Two suits (previously instituted and subsequent).",
      "Matter directly and substantially in issue must be identical.",
      "Same parties or parties litigating under same title.",
      "Previously instituted court must be competent to grant relief."
    ],
    "exceptions": [
      "Does not bar institution of suit, only trial.",
      "Explanation: Pendency of suit in a FOREIGN COURT does not preclude Indian court from trying suit."
    ],
    "relatedTopicId": "top-cpc-03-01",
    "chapterId": "ch-cpc-03",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Foreign court pendency does NOT bar Indian trial. The section applies to trial, not interlocutory/interim orders.",
    "highYield": true
  },
  {
    "id": "cpc-sec-011",
    "type": "section",
    "ref": "Section 11",
    "title": "Res Judicata",
    "concept": "No Court shall try any suit or issue in which matter directly and substantially in issue has been directly and substantially in issue in a former suit between same parties and heard and finally decided.",
    "plainEnglish": "A matter once decided by a competent court cannot be relitigated between the same parties. Enforces judicial finality and prevents double vexation.",
    "conditions": [
      "Matter directly and substantially in issue in former suit.",
      "Same parties or litigating under same title.",
      "Former court must be competent to try subsequent suit.",
      "Heard and finally decided."
    ],
    "exceptions": [
      "Contains 8 statutory Explanations.",
      "Explanation IV: Constructive Res Judicata (any matter which might and ought to have been made ground of defence or attack).",
      "Explanation VIII: Decision of court of limited jurisdiction operates as res judicata."
    ],
    "relatedTopicId": "top-cpc-03-02",
    "chapterId": "ch-cpc-03",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Daryao v. State of UP (applies to writ petitions); Explanation IV is Constructive Res Judicata.",
    "highYield": true
  },
  {
    "id": "cpc-sec-015",
    "type": "section",
    "ref": "Section 15",
    "title": "Court in Which Suits to Be Instituted",
    "concept": "Every suit shall be instituted in the Court of the lowest grade competent to try it.",
    "plainEnglish": "Procedural rule to prevent higher courts from being overcrowded. Pecuniary valuation determines the lowest court.",
    "conditions": [
      "Determined by valuation stated in plaint, unless fraudulent or arbitrary."
    ],
    "exceptions": [
      "Rule of procedure, does not take away inherent jurisdiction of superior court if tried without objection."
    ],
    "relatedTopicId": "top-cpc-02-02",
    "chapterId": "ch-cpc-02",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Institution in higher court is an irregularity curable under Section 99, not a nullity.",
    "highYield": true
  },
  {
    "id": "cpc-sec-016",
    "type": "section",
    "ref": "Section 16",
    "title": "Suits to Be Instituted Where Subject-Matter Situate",
    "concept": "Suits for recovery of immovable property, partition, foreclosure, sale, redemption of mortgage, or other right/interest in immovable property shall be instituted where property is situate.",
    "plainEnglish": "Immovable property suits must be filed in the court within whose local jurisdiction the property is located.",
    "conditions": [
      "Property located within territorial limits."
    ],
    "exceptions": [
      "Proviso: Suit for relief respecting immovable property held by defendant can be instituted where defendant resides if relief entirely obtainable through personal obedience."
    ],
    "relatedTopicId": "top-cpc-02-02",
    "chapterId": "ch-cpc-02",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Proviso embodies equity rule: 'Equity acts in personam'.",
    "highYield": true
  },
  {
    "id": "cpc-sec-020",
    "type": "section",
    "ref": "Section 20",
    "title": "Other Suits to Be Instituted Where Defendants Reside or Cause of Action Arises",
    "concept": "Residuary territorial rule: Suit can be filed where defendant resides, carries on business, or personally works for gain, or where cause of action arises, wholly or in part.",
    "plainEnglish": "For personal or contract disputes, plaintiff can choose: defendant's residence/business place or where cause of action arose.",
    "conditions": [
      "If multiple defendants, either leave of court or all defendants must acquiesce if some reside outside.",
      "Cause of action arises wholly or in part."
    ],
    "exceptions": [
      "Corporation deemed to carry on business at sole or principal office, or subordinate office if cause of action arose there."
    ],
    "relatedTopicId": "top-cpc-02-02",
    "chapterId": "ch-cpc-02",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Explanation II: Corporation jurisdiction requires both branch office AND cause of action at branch.",
    "highYield": true
  },
  {
    "id": "cpc-sec-021",
    "type": "section",
    "ref": "Section 21",
    "title": "Objections to Jurisdiction",
    "concept": "No objection as to place of suing or pecuniary limits allowed in appellate/revisional court unless taken in court of first instance at earliest possible opportunity and failure of justice resulted.",
    "plainEnglish": "Territorial and pecuniary objections cannot be raised for the first time in appeal unless raised early AND failure of justice occurred.",
    "conditions": [
      "Objection taken in court of first instance.",
      "Taken at earliest possible opportunity (at or before settlement of issues).",
      "Consequent failure of justice has occurred."
    ],
    "exceptions": [
      "Does NOT cure inherent lack of subject-matter jurisdiction, which goes to the root of competence."
    ],
    "relatedTopicId": "top-cpc-02-03",
    "chapterId": "ch-cpc-02",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Kiran Singh v. Chaman Paswan: Decree passed without subject-matter jurisdiction is a nullity.",
    "highYield": true
  },
  {
    "id": "cpc-sec-026",
    "type": "section",
    "ref": "Section 26",
    "title": "Institution of Suits",
    "concept": "Every suit shall be instituted by the presentation of a plaint or in such other manner as may be prescribed. Facts shall be proved by affidavit (sub-section 2).",
    "plainEnglish": "Formal statutory requirement for starting a civil suit: plaint presentation and mandatory supporting affidavit.",
    "conditions": [
      "Presentation of plaint in duplicate.",
      "Affidavit verifying facts."
    ],
    "exceptions": [
      "Sub-section (2) added by Act 46 of 1999 (effective 2002)."
    ],
    "relatedTopicId": "top-cpc-04-01",
    "chapterId": "ch-cpc-04",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Section 26(2) mandates proof of facts by affidavit in every plaint.",
    "highYield": true
  },
  {
    "id": "cpc-sec-034",
    "type": "section",
    "ref": "Section 34",
    "title": "Interest",
    "concept": "Court may award interest: (1) past interest at agreed/reasonable rate; (2) pendente lite interest at court's discretion; (3) future interest from decree to payment not exceeding 6% p.a. (contractual/commercial exception).",
    "plainEnglish": "Regulates judicial discretion in awarding interest across three periods: pre-suit, during trial, and post-decree.",
    "conditions": [
      "Future interest capped at 6% p.a. for non-commercial transactions.",
      "For commercial transactions, future interest may exceed 6% up to contractual rate or nationalised bank lending rate."
    ],
    "exceptions": [
      "Where decree is silent on future interest, court deemed to have refused it."
    ],
    "relatedTopicId": "top-cpc-11-02",
    "chapterId": "ch-cpc-11",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Silence in decree regarding future interest is deemed refusal (Section 34(2)).",
    "highYield": true
  },
  {
    "id": "cpc-sec-035A",
    "type": "section",
    "ref": "Section 35A",
    "title": "Compensatory Costs in Respect of False or Vexatious Claims or Defences",
    "concept": "Court may award compensatory costs against party making false or vexatious claim or defence, up to statutory ceiling of Rs 3,000 (or court's pecuniary limit, whichever is less).",
    "plainEnglish": "Special penalty awarded to compensate victim of false and dishonest litigation.",
    "conditions": [
      "Claim or defence must be false or vexatious to knowledge of party.",
      "Objection must be raised by other party."
    ],
    "exceptions": [
      "Does not apply to railway claims tribunal or special statutory exclusions. Ceiling Rs. 3,000 under central act."
    ],
    "relatedTopicId": "top-cpc-11-03",
    "chapterId": "ch-cpc-11",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Statutory limit under Section 35A is Rs. 3,000.",
    "highYield": true
  },
  {
    "id": "cpc-sec-056",
    "type": "section",
    "ref": "Section 56",
    "title": "Prohibition of Arrest or Detention of Women in Execution of Decree for Money",
    "concept": "Notwithstanding anything in this Part, the Court shall not order the arrest or detention in civil prison of a woman in execution of a decree for the payment of money.",
    "plainEnglish": "Absolute statutory bar: No woman can be arrested or jailed in execution of a money decree.",
    "conditions": [
      "Applies to execution of money decrees.",
      "Immunity is absolute and non-waivable."
    ],
    "exceptions": [
      "Does not apply to execution of other decrees (e.g. disobedience of injunction under O. XXXIX R. 2A)."
    ],
    "relatedTopicId": "top-cpc-12-02",
    "chapterId": "ch-cpc-12",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Tested in UP PCS-J 2013, 2018, and 2023! Absolute protection for women in money decrees.",
    "highYield": true
  },
  {
    "id": "cpc-sec-060",
    "type": "section",
    "ref": "Section 60",
    "title": "Property Liable to Attachment and Sale in Execution of Decree",
    "concept": "Enumerates property liable to attachment and gives an extensive proviso of exempt properties (wearing apparel, tools of artisans, agricultural implements, partial salary).",
    "plainEnglish": "Defines what debtor assets can be seized and what is strictly protected for debtor survival.",
    "conditions": [
      "Salaries: First Rs. 1,000 + two-thirds of remainder exempt in non-maintenance decrees.",
      "In maintenance decrees: One-third exempt; two-thirds attachable."
    ],
    "exceptions": [
      "Attachment of non-maintenance salary cannot exceed 24 months continuously."
    ],
    "relatedTopicId": "top-cpc-12-03",
    "chapterId": "ch-cpc-12",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Tested in 2015! Salary calculation: First 1,000 + 2/3 of remainder exempt in other decrees.",
    "highYield": true
  },
  {
    "id": "cpc-sec-080",
    "type": "section",
    "ref": "Section 80",
    "title": "Notice Before Institution of Suit Against Government or Public Officer",
    "concept": "Mandatory 2 months statutory notice in writing before instituting suit against Government or public officer in respect of act done in official capacity.",
    "plainEnglish": "Government must be given 60 days (2 months) notice before being sued so it can evaluate and settle genuine claims.",
    "conditions": [
      "Notice must state cause of action, name, description, place of residence, and relief claimed.",
      "Must be delivered to Secretary to Govt / Collector."
    ],
    "exceptions": [
      "Sub-section (2): Urgent or immediate relief can be sought with leave of court without notice, but no interim injunction without hearing Govt."
    ],
    "relatedTopicId": "top-cpc-15-01",
    "chapterId": "ch-cpc-15",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Notice period is exactly 2 months (not 60 days or 90 days).",
    "highYield": true
  },
  {
    "id": "cpc-sec-089",
    "type": "section",
    "ref": "Section 89",
    "title": "Settlement of Disputes Outside the Court (ADR)",
    "concept": "Court shall formulate terms of settlement and refer parties to ADR: Arbitration, Conciliation, Judicial Settlement (including Lok Adalat), or Mediation.",
    "plainEnglish": "Empowers trial courts to refer civil cases to amicable settlement outside court.",
    "conditions": [
      "Where it appears to court that elements of settlement exist."
    ],
    "exceptions": [
      "Salem Advocate Bar Association v. UOI; Afcons Infrastructure v. Cherian Varkey (landmark rules on suitable vs unsuitable cases)."
    ],
    "relatedTopicId": "top-cpc-18-01",
    "chapterId": "ch-cpc-18",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Afcons Infrastructure (2010) corrected drafting anomalies between mediation and conciliation.",
    "highYield": true
  },
  {
    "id": "cpc-sec-096",
    "type": "section",
    "ref": "Section 96",
    "title": "Appeal from Original Decree (First Appeal)",
    "concept": "Appeal lies from every decree passed by any court exercising original jurisdiction to the court authorized to hear appeals. Lies on questions of fact and law.",
    "plainEnglish": "The statutory right to file a First Appeal against an original decree on both facts and law.",
    "conditions": [
      "Must be an original decree.",
      "Can be filed against ex parte decree (Section 96(2))."
    ],
    "exceptions": [
      "Sub-section (3): NO appeal lies from a decree passed by the court with CONSENT OF PARTIES.",
      "Sub-section (4): In Court of Small Causes suits under Rs. 10,000, appeal lies only on question of law."
    ],
    "relatedTopicId": "top-cpc-16-01",
    "chapterId": "ch-cpc-16",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "UP PCS-J 2023 question: S. 96(3) prohibits appeal against consent decree.",
    "highYield": true
  },
  {
    "id": "cpc-sec-100",
    "type": "section",
    "ref": "Section 100",
    "title": "Second Appeal to High Court",
    "concept": "Second appeal lies to High Court from appellate decree only if High Court is satisfied that the case involves a SUBSTANTIAL QUESTION OF LAW.",
    "plainEnglish": "Second appeals are strictly limited to High Courts on substantial questions of law, not pure questions of fact.",
    "conditions": [
      "High Court must formulate the substantial question of law.",
      "Memorandum of appeal must precisely state the question."
    ],
    "exceptions": [
      "Section 102: No second appeal in suits for recovery of money where value does not exceed Rs 25,000."
    ],
    "relatedTopicId": "top-cpc-16-02",
    "chapterId": "ch-cpc-16",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Second appeal cannot be entertained without formulating substantial question of law.",
    "highYield": true
  },
  {
    "id": "cpc-sec-113",
    "type": "section",
    "ref": "Section 113",
    "title": "Reference to High Court",
    "concept": "Subordinate court may state a case and refer it for opinion of High Court where it entertains reasonable doubt on question of law or validity of Act/Ordinance.",
    "plainEnglish": "Trial court asks High Court for legal opinion during pending litigation before pronouncing judgment.",
    "conditions": [
      "Pending suit or appeal.",
      "Court entertains reasonable doubt on question of law.",
      "Mandatory where validity of Act, Ordinance, or Regulation is challenged."
    ],
    "exceptions": [
      "Proviso: Mandatory if court believes Act is invalid but not so declared by HC or SC."
    ],
    "relatedTopicId": "top-cpc-17-01",
    "chapterId": "ch-cpc-17",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Reference is made by the COURT, not by a party.",
    "highYield": true
  },
  {
    "id": "cpc-sec-114",
    "type": "section",
    "ref": "Section 114",
    "title": "Review",
    "concept": "Any person considering himself aggrieved by decree or order from which appeal allowed but no appeal preferred, or no appeal allowed, may apply for review to the court which passed decree.",
    "plainEnglish": "Asking the SAME judge/court to reconsider its own decision on grounds of error apparent on face of record or discovery of new evidence.",
    "conditions": [
      "Discovery of new and important matter/evidence after due diligence.",
      "Mistake or error apparent on face of the record.",
      "Any other sufficient reason."
    ],
    "exceptions": [
      "Cannot review if appeal is already pending.",
      "Cannot re-hear on merits as an appeal in disguise."
    ],
    "relatedTopicId": "top-cpc-17-02",
    "chapterId": "ch-cpc-17",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Read with Order XLVII. Review lies to the SAME court that passed decree.",
    "highYield": true
  },
  {
    "id": "cpc-sec-115",
    "type": "section",
    "ref": "Section 115",
    "title": "Revision",
    "concept": "High Court (or District Court under UP Amendment) may call for record of any case decided by subordinate court in which no appeal lies, on grounds of jurisdictional error.",
    "plainEnglish": "Supervisory check by superior court over lower court's jurisdictional errors where no appeal is available.",
    "conditions": [
      "Case decided by subordinate court.",
      "No appeal lies to High Court.",
      "Subordinate court exercised jurisdiction not vested, failed to exercise jurisdiction, or acted with material irregularity."
    ],
    "exceptions": [
      "Proviso: Revision shall not operate as a stay of suit unless stay granted. Shall not vary order unless it disposes of suit."
    ],
    "relatedTopicId": "top-cpc-17-03",
    "chapterId": "ch-cpc-17",
    "sourceLabel": "Central CPC & UP Amendment",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "CRITICAL UP EXAM NOTE: In Uttar Pradesh, Section 115 is amended to divide revisional jurisdiction between District Court and High Court depending on valuation.",
    "highYield": true
  },
  {
    "id": "cpc-sec-144",
    "type": "section",
    "ref": "Section 144",
    "title": "Application for Restitution",
    "concept": "Where decree/order is varied or reversed in appeal, revision or separate suit, court of first instance shall cause restitution to place parties in position they would have occupied.",
    "plainEnglish": "Restores the winning party to their rightful position when an erroneous decree is reversed. Act of court shall prejudice no one (Actus curiae neminem gravabit).",
    "conditions": [
      "Variation or reversal of decree.",
      "Benefit received by other party under erroneous decree."
    ],
    "exceptions": [
      "Sub-section (2): No separate suit lies for obtaining any restitution obtainable under Section 144."
    ],
    "relatedTopicId": "top-cpc-18-03",
    "chapterId": "ch-cpc-18",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Determination of question under Section 144 is explicitly a DECREE under Section 2(2).",
    "highYield": true
  },
  {
    "id": "cpc-sec-148A",
    "type": "section",
    "ref": "Section 148A",
    "title": "Right to Lodge a Caveat",
    "concept": "Any person claiming a right to appear before Court on hearing of application may lodge a caveat. Caveat remains in force for 90 days.",
    "plainEnglish": "A precautionary warning to the court: 'Hear me before passing any ex parte interim order against me.'",
    "conditions": [
      "Caveat filed by person claiming right to appear.",
      "Caveator must serve copy on expected applicant."
    ],
    "exceptions": [
      "Sub-section (5): Caveat expires automatically after 90 DAYS from date of filing."
    ],
    "relatedTopicId": "top-cpc-13-03",
    "chapterId": "ch-cpc-13",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Duration of Caveat is exactly 90 DAYS (tested in UP PCS-J 2012!).",
    "highYield": true
  },
  {
    "id": "cpc-sec-151",
    "type": "section",
    "ref": "Section 151",
    "title": "Saving of Inherent Powers of Court",
    "concept": "Nothing in this Code shall limit or affect inherent power of Court to make such orders as may be necessary for the ends of justice or to prevent abuse of the process of the Court.",
    "plainEnglish": "Courts possess natural residual power to do justice where the code is silent, without contravening express statutory provisions.",
    "conditions": [
      "To meet the ends of justice or prevent abuse of process of the court."
    ],
    "exceptions": [
      "Cannot be used when an express remedy or provision is available in the CPC. Cannot override statutory prohibitions."
    ],
    "relatedTopicId": "top-cpc-13-04",
    "chapterId": "ch-cpc-13",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Section 151 does NOT confer any new power; it merely SAVES inherent powers already possessed.",
    "highYield": true
  },
  {
    "id": "cpc-ord-01-r01",
    "type": "rule",
    "ref": "Order I Rule 1",
    "title": "Who May Be Joined as Plaintiffs",
    "concept": "All persons may be joined in one suit as plaintiffs where any right to relief arises out of same act/transaction and common question of law or fact would arise.",
    "plainEnglish": "Two or more persons can join together as co-plaintiffs if their claim arises from the same incident and shares legal/factual questions.",
    "conditions": [
      "Right to relief arises out of same act or series of acts/transactions.",
      "Common question of law or fact."
    ],
    "exceptions": [
      "Court can order separate trials under Rule 2 if joinder causes embarrassment or delay."
    ],
    "relatedTopicId": "top-cpc-05-01",
    "chapterId": "ch-cpc-05",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Twin tests of joinder: Same transaction + common question of law/fact.",
    "highYield": true
  },
  {
    "id": "cpc-ord-01-r08",
    "type": "rule",
    "ref": "Order I Rule 8",
    "title": "Representative Suit",
    "concept": "One person may sue or defend on behalf of all in same interest with permission of court. Notice to all interested persons mandatory.",
    "plainEnglish": "Allows a few persons to represent numerous people having the same common interest in a civil litigation.",
    "conditions": [
      "Numerous persons having same interest.",
      "Permission of court or direction by court.",
      "Mandatory public notice at plaintiff's expense (Rule 8(2))."
    ],
    "exceptions": [
      "Decree passed binds all persons represented under Explanation VI to Section 11."
    ],
    "relatedTopicId": "top-cpc-05-02",
    "chapterId": "ch-cpc-05",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Compromise in O. I R. 8 suit requires leave of court and notice to all interested parties (Rule 8(4)).",
    "highYield": true
  },
  {
    "id": "cpc-ord-01-r09",
    "type": "rule",
    "ref": "Order I Rule 9",
    "title": "Misjoinder and Non-Joinder of Parties",
    "concept": "No suit shall be defeated by reason of misjoinder or non-joinder of parties, EXCEPT in the case of non-joinder of a NECESSARY PARTY.",
    "plainEnglish": "Procedural mistake of adding wrong parties or forgetting proper parties will not dismiss a suit, BUT non-joinder of a NECESSARY party is fatal.",
    "conditions": [
      "General rule: Suit proceeds between parties actually before court."
    ],
    "exceptions": [
      "PROVISO: Nothing in this rule shall apply to non-joinder of a necessary party."
    ],
    "relatedTopicId": "top-cpc-05-01",
    "chapterId": "ch-cpc-05",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Proviso added in 1976: Non-joinder of a necessary party CAN defeat the suit.",
    "highYield": true
  },
  {
    "id": "cpc-ord-01-r10",
    "type": "rule",
    "ref": "Order I Rule 10",
    "title": "Striking Out or Adding Parties",
    "concept": "Court may at any stage of proceedings order name of any party improperly joined to be struck out, or necessary/proper party to be added.",
    "plainEnglish": "Court's wide discretion to add or remove parties to ensure complete adjudication of the dispute.",
    "conditions": [
      "Can be done at any stage of proceedings, with or without application."
    ],
    "exceptions": [
      "Where defendant added, plaint must be amended and summons served on new defendant."
    ],
    "relatedTopicId": "top-cpc-05-02",
    "chapterId": "ch-cpc-05",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Order I Rule 10(2) gives court power to add proper parties suo motu.",
    "highYield": true
  },
  {
    "id": "cpc-ord-02-r02",
    "type": "rule",
    "ref": "Order II Rule 2",
    "title": "Suit to Include the Whole Claim",
    "concept": "Every suit shall include whole of claim arising from cause of action. If plaintiff relinquishes or omits to sue for any portion, he cannot afterwards sue for omitted portion without leave of court.",
    "plainEnglish": "Bar against splitting claims: A plaintiff must demand all reliefs arising from one cause of action in one suit. Omitted claims cannot be sued for later.",
    "conditions": [
      "Cause of action must be identical in both suits.",
      "Plaintiff was entitled to claim relief in former suit and omitted it without leave."
    ],
    "exceptions": [
      "If plaintiff obtained leave of court in former suit to omit relief, subsequent suit is permitted."
    ],
    "relatedTopicId": "top-cpc-04-02",
    "chapterId": "ch-cpc-04",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Order II Rule 2 bars splitting of remedies and claims based on the SAME cause of action.",
    "highYield": true
  },
  {
    "id": "cpc-ord-05-r20",
    "type": "rule",
    "ref": "Order V Rule 20",
    "title": "Substituted Service",
    "concept": "Where Court is satisfied defendant is keeping out of way to avoid service, Court shall order summons to be served by affixing copy on court house and house where defendant last resided, or by newspaper publication.",
    "plainEnglish": "Alternate service methods when the defendant is deliberately evading or hiding from the process server.",
    "conditions": [
      "Satisfaction of court that defendant is intentionally evading service or cannot be served ordinarily."
    ],
    "exceptions": [
      "Newspaper advertisement must be in daily newspaper circulating in locality where defendant last resided."
    ],
    "relatedTopicId": "top-cpc-08-01",
    "chapterId": "ch-cpc-08",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Substituted service under Order V Rule 20 is as effective as personal service.",
    "highYield": true
  },
  {
    "id": "cpc-ord-06-r17",
    "type": "rule",
    "ref": "Order VI Rule 17",
    "title": "Amendment of Pleadings",
    "concept": "Court may at any stage allow either party to alter or amend pleadings in manner necessary to determine real questions in controversy. Provided no amendment allowed after trial commenced unless party could not raise matter despite due diligence.",
    "plainEnglish": "Liberal power to amend plaint or written statement to do justice, subject to the strict 'due diligence' bar once the trial commences.",
    "conditions": [
      "Amendment must be necessary to determine real questions in controversy.",
      "Cannot change fundamental nature of suit."
    ],
    "exceptions": [
      "PROVISO (added 2002): No amendment after trial commenced unless court concludes party could not raise it despite DUE DILIGENCE."
    ],
    "relatedTopicId": "top-cpc-06-02",
    "chapterId": "ch-cpc-06",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Salem Advocate Bar Association; Rajesh Kumar Aggarwal v. K.K. Modi. Proviso due diligence test.",
    "highYield": true
  },
  {
    "id": "cpc-ord-07-r10",
    "type": "rule",
    "ref": "Order VII Rule 10",
    "title": "Return of Plaint",
    "concept": "Plaint shall at any stage of the suit be returned to be presented to the Court in which the suit should have been instituted.",
    "plainEnglish": "When a court lacks territorial or pecuniary jurisdiction, it does not dismiss the case; it returns the plaint for filing in the right court.",
    "conditions": [
      "Can be returned at ANY stage of suit, including in appellate or revisional court.",
      "Judge endorses date of presentation, return, and reasons."
    ],
    "exceptions": [
      "Under Rule 10A, plaintiff can apply to have court specify date of appearance in new court."
    ],
    "relatedTopicId": "top-cpc-07-01",
    "chapterId": "ch-cpc-07",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Return of plaint is NOT a decree; it is an appealable order under Order XLIII Rule 1(a).",
    "highYield": true
  },
  {
    "id": "cpc-ord-07-r11",
    "type": "rule",
    "ref": "Order VII Rule 11",
    "title": "Rejection of Plaint",
    "concept": "Plaint shall be rejected on 6 grounds: (a) does not disclose cause of action; (b) undervalued relief not corrected; (c) insufficient stamp not corrected; (d) barred by any law; (e) not in duplicate; (f) non-compliance with statutory notice.",
    "plainEnglish": "A defective or barred plaint is thrown out at the threshold. Operates as a 'deemed decree' under Section 2(2).",
    "conditions": [
      "Court looks ONLY at allegations in plaint and accompanying documents (not written statement)."
    ],
    "exceptions": [
      "Rejection of plaint does NOT preclude plaintiff from presenting fresh plaint on same cause of action (Rule 13)."
    ],
    "relatedTopicId": "top-cpc-07-01",
    "chapterId": "ch-cpc-07",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Rejection of plaint is an appealable DECREE under Section 2(2). Cannot reject plaint in part; must be rejected as a whole.",
    "highYield": true
  },
  {
    "id": "cpc-ord-08-r01",
    "type": "rule",
    "ref": "Order VIII Rule 1",
    "title": "Written Statement Filing Timeline",
    "concept": "Defendant shall present written statement within 30 days from date of service of summons. Extendable for reasons recorded up to 90 days.",
    "plainEnglish": "Defendant must submit defence within 30 days, extendable up to 90 days. Supreme Court held 90 days is directory, not mandatory, in exceptional situations.",
    "conditions": [
      "Ordinary deadline: 30 days.",
      "Extended deadline: 90 days."
    ],
    "exceptions": [
      "Kailash v. Nanhku (2005): 90-day timeline is directory in non-commercial civil suits, but mandatory in Commercial Courts Act."
    ],
    "relatedTopicId": "top-cpc-07-02",
    "chapterId": "ch-cpc-07",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Kailash v. Nanhku is the landmark authority on directory nature of 90 days in ordinary suits.",
    "highYield": true
  },
  {
    "id": "cpc-ord-08-r06A",
    "type": "rule",
    "ref": "Order VIII Rule 6A",
    "title": "Counter-Claim by Defendant",
    "concept": "Defendant may set up counter-claim against plaintiff's claim in respect of cause of action accruing before or after filing of suit, but before defendant has delivered his defence.",
    "plainEnglish": "A cross-action by defendant treated as a plaint in a cross-suit. Proceeded with even if plaintiff's suit is stayed or dismissed.",
    "conditions": [
      "Must be within pecuniary jurisdiction of court.",
      "Must accrue before defendant delivered defence or before time limit expired."
    ],
    "exceptions": [
      "Rule 6C: Plaintiff may apply to court to exclude counter-claim to be heard in independent suit."
    ],
    "relatedTopicId": "top-cpc-07-03",
    "chapterId": "ch-cpc-07",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Counter-claim has the same effect as a cross-suit; continues even if plaintiff's suit is dismissed.",
    "highYield": true
  },
  {
    "id": "cpc-ord-09-r13",
    "type": "rule",
    "ref": "Order IX Rule 13",
    "title": "Setting Aside Decree Ex Parte Against Defendant",
    "concept": "Defendant against whom ex parte decree passed may apply to court to set it aside on grounds that summons was not duly served or he was prevented by sufficient cause from appearing.",
    "plainEnglish": "Procedure for a defendant to reopen a case decided in his absence by showing non-service of summons or genuine reason for absence.",
    "conditions": [
      "Summons not duly served OR prevented by any sufficient cause.",
      "Application filed within 30 days under Article 123 Limitation Act."
    ],
    "exceptions": [
      "Second Proviso: No decree set aside on ground of irregular service if court satisfied defendant had notice of date of hearing."
    ],
    "relatedTopicId": "top-cpc-08-03",
    "chapterId": "ch-cpc-08",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Defendant has 3 concurrent remedies: (1) O. IX R. 13; (2) First Appeal under S. 96(2); (3) Review under S. 114.",
    "highYield": true
  },
  {
    "id": "cpc-ord-15-r05-up",
    "type": "rule",
    "ref": "Order XV Rule 5 (UP Amendment)",
    "title": "Striking Off Defence for Failure to Deposit Rent",
    "concept": "In any suit by a lessor for eviction of a lessee, defendant shall deposit entire admitted rent on first hearing, failing which defence shall be struck off.",
    "plainEnglish": "Vital Uttar Pradesh local amendment protecting landlords: tenant must deposit rent at first hearing or lose right to defend the eviction suit.",
    "conditions": [
      "Applies to eviction suits in Uttar Pradesh.",
      "Tenant must deposit entire admitted rent + interest at first hearing and continue monthly deposits."
    ],
    "exceptions": [
      "Court has discretion to condone delay for representation made within 10 days."
    ],
    "relatedTopicId": "top-cpc-19-02",
    "chapterId": "ch-cpc-19",
    "sourceLabel": "Uttar Pradesh Amendment",
    "indiaCodeUrl": "https://www.allahabadhighcourt.in/rules/dc_rules.html",
    "examTips": "SPECIFIC TO UTTAR PRADESH: Frequent question in UP PCS-J Prelims and Mains.",
    "highYield": true
  },
  {
    "id": "cpc-ord-21-r58",
    "type": "rule",
    "ref": "Order XXI Rule 58",
    "title": "Adjudication of Claims to, or Objections to Attachment of, Property",
    "concept": "All claims or objections to attachment of property in execution shall be adjudicated by the executing court as a suit, not by separate suit. Order has same force as decree.",
    "plainEnglish": "Third parties claiming that attached property belongs to them must get their claim decided in execution court; separate suit is barred.",
    "conditions": [
      "Claim raised before executing court before property sold."
    ],
    "exceptions": [
      "Court may refuse to investigate if claim designedly or unnecessarily delayed."
    ],
    "relatedTopicId": "top-cpc-12-04",
    "chapterId": "ch-cpc-12",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Order passed under Order XXI Rule 58 is appealable as a DECREE.",
    "highYield": true
  },
  {
    "id": "cpc-ord-39-r01",
    "type": "rule",
    "ref": "Order XXXIX Rule 1 & 2",
    "title": "Cases in Which Temporary Injunction May Be Granted",
    "concept": "Court may grant temporary injunction where property in dispute is in danger of being wasted, damaged or alienated, or where defendant threatens to dispossess plaintiff.",
    "plainEnglish": "Interim order preserving status quo until trial ends, based on the three golden pillars: Prima Facie Case, Irreparable Injury, and Balance of Convenience.",
    "conditions": [
      "1. Prima Facie Case; 2. Irreparable Injury; 3. Balance of Convenience."
    ],
    "exceptions": [
      "Rule 3A: Application for injunction must be disposed of within 30 DAYS where ex parte injunction granted."
    ],
    "relatedTopicId": "top-cpc-13-02",
    "chapterId": "ch-cpc-13",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191?view_type=browse&sam_handle=123456789/1362",
    "examTips": "Order XXXIX Rule 2A prescribes punishment for breach of injunction (civil imprisonment up to 3 months or attachment of property for 1 year).",
    "highYield": true
  },
  {
    "id": "cpc-sec-003",
    "type": "section",
    "ref": "Section 3",
    "title": "Subordination of Courts",
    "concept": "District Court is subordinate to High Court, and every Civil Court of a grade inferior to that of a District Court and every Court of Small Causes is subordinate to the High Court and District Court.",
    "plainEnglish": "Establishes the judicial hierarchy: High Court -> District Court -> Subordinate Civil Courts and Small Cause Courts.",
    "conditions": [
      "Applies to all civil judicial administration."
    ],
    "exceptions": [
      "Subject to state civil courts acts."
    ],
    "relatedTopicId": "top-cpc-01-01",
    "chapterId": "ch-cpc-01",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Court of Small Causes is subordinate to BOTH High Court and District Court (tested in UP PCS-J 2016!).",
    "highYield": true
  },
  {
    "id": "cpc-sec-013",
    "type": "section",
    "ref": "Section 13",
    "title": "When Foreign Judgment Not Conclusive",
    "concept": "Foreign judgment is conclusive as to any matter directly adjudicated upon, EXCEPT in 6 cases: (a) not pronounced by competent court; (b) not on merits; (c) incorrect view of international law; (d) opposed to natural justice; (e) obtained by fraud; (f) sustains claim founded on breach of Indian law.",
    "plainEnglish": "A judgment of a foreign court binds Indian parties unless one of the six fatal defects under Section 13 is proved.",
    "conditions": [
      "Must be a judgment of a foreign court outside India."
    ],
    "exceptions": [
      "Cannot be enforced if obtained by fraud or without jurisdiction."
    ],
    "relatedTopicId": "top-cpc-01-03",
    "chapterId": "ch-cpc-01",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Satya v. Teja Singh; Y. Narasimha Rao v. Y. Venkata Lakshmi (marital foreign decrees).",
    "highYield": true
  },
  {
    "id": "cpc-sec-017",
    "type": "section",
    "ref": "Section 17",
    "title": "Suits for Immovable Property Situate Within Jurisdiction of Different Courts",
    "concept": "Where suit is to obtain relief respecting immovable property situate within jurisdiction of different Courts, suit may be instituted in ANY Court within the local limits of whose jurisdiction any portion of the property is situate.",
    "plainEnglish": "If a disputed property spans across two or more court boundaries, the plaintiff can file the suit in ANY of those courts, provided the claim is within that court's pecuniary value.",
    "conditions": [
      "Entire claim must be within pecuniary jurisdiction of chosen court."
    ],
    "exceptions": [
      "Does not apply if properties are independent and claims unconnected."
    ],
    "relatedTopicId": "top-cpc-02-02",
    "chapterId": "ch-cpc-02",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Entire property suit can be filed where ANY portion is situate.",
    "highYield": true
  },
  {
    "id": "cpc-sec-018",
    "type": "section",
    "ref": "Section 18",
    "title": "Place of Institution Where Local Limits of Jurisdiction Are Uncertain",
    "concept": "Where it is alleged that property is situate within uncertain local limits of two or more courts, any one of them may record a statement to that effect and proceed to entertain and dispose of suit.",
    "plainEnglish": "Resolves boundary ambiguities: any of the borderline courts can record the uncertainty and try the suit, valid as if property were wholly within its jurisdiction.",
    "conditions": [
      "Court must record statement that boundary uncertainty exists."
    ],
    "exceptions": [
      "Objection in appeal requires early objection AND consequent failure of justice."
    ],
    "relatedTopicId": "top-cpc-02-02",
    "chapterId": "ch-cpc-02",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Tested in UP PCS-J 2016! Court must record statement of uncertainty.",
    "highYield": true
  },
  {
    "id": "cpc-sec-025",
    "type": "section",
    "ref": "Section 25",
    "title": "Power of Supreme Court to Transfer Suits, Appeals or Other Proceedings",
    "concept": "On application of party and after notice, Supreme Court may transfer any suit, appeal or proceeding from a High Court or Civil Court in one State to a High Court or Civil Court in any other State.",
    "plainEnglish": "Supreme Court's exclusive pan-India transfer power to ensure fair trial and ends of justice across state borders.",
    "conditions": [
      "Application by a party supported by affidavit.",
      "Notice to parties.",
      "Expedient for ends of justice."
    ],
    "exceptions": [
      "If application dismissed as frivolous, SC may award compensation up to Rs 2,000."
    ],
    "relatedTopicId": "top-cpc-02-03",
    "chapterId": "ch-cpc-02",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Inter-state transfer power belongs exclusively to the Supreme Court under Section 25.",
    "highYield": true
  },
  {
    "id": "cpc-sec-033",
    "type": "section",
    "ref": "Section 33",
    "title": "Judgment and Decree",
    "concept": "The Court, after the case has been heard, shall pronounce judgment, and on such judgment a decree shall follow.",
    "plainEnglish": "Mandates that judgment must be pronounced first, and the formal decree must be drawn up in conformity with it.",
    "conditions": [
      "Court must have heard the case.",
      "Decree must follow judgment."
    ],
    "exceptions": [
      "Under Order XX Rule 6A, appeal can be filed on judgment if decree drawing is delayed."
    ],
    "relatedTopicId": "top-cpc-11-01",
    "chapterId": "ch-cpc-11",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Decree must agree with judgment. Date of decree is the date judgment is pronounced.",
    "highYield": true
  },
  {
    "id": "cpc-sec-038",
    "type": "section",
    "ref": "Section 38",
    "title": "Court by Which Decree May Be Executed",
    "concept": "A decree may be executed either by the Court which passed it, or by the Court to which it is sent for execution.",
    "plainEnglish": "Execution can only be initiated either in the court of first instance that passed the decree or in the transferee court.",
    "conditions": [
      "Decree sent for execution under Section 39."
    ],
    "exceptions": [
      "Executing court cannot go behind the decree; must execute it as it stands."
    ],
    "relatedTopicId": "top-cpc-12-01",
    "chapterId": "ch-cpc-12",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Executing court cannot question validity or correctness of decree except when passed without inherent jurisdiction.",
    "highYield": true
  },
  {
    "id": "cpc-sec-046",
    "type": "section",
    "ref": "Section 46",
    "title": "Precepts",
    "concept": "Court which passed decree may, on application of decree-holder, issue a precept to any other court competent to execute decree to attach property of judgment-debtor.",
    "plainEnglish": "An urgent interim attachment order issued to another court to freeze debtor assets before they can be hidden. Valid for 2 months.",
    "conditions": [
      "Issued by court which passed decree to transferee court."
    ],
    "exceptions": [
      "Attachment under precept cannot exceed 2 MONTHS unless extended by court which passed decree."
    ],
    "relatedTopicId": "top-cpc-12-03",
    "chapterId": "ch-cpc-12",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Precept attachment duration is strictly 2 MONTHS unless extended.",
    "highYield": true
  },
  {
    "id": "cpc-sec-047",
    "type": "section",
    "ref": "Section 47",
    "title": "Questions to Be Determined by the Court Executing Decree",
    "concept": "All questions arising between parties to suit or representatives relating to execution, discharge or satisfaction of decree shall be determined by Court executing decree and not by a separate suit.",
    "plainEnglish": "Comprehensive bar on fresh suits for execution disputes: All issues of satisfaction, discharge, or execution must be resolved by the execution court itself.",
    "conditions": [
      "Questions relating to execution, discharge, or satisfaction.",
      "Arising between parties to suit or their representatives."
    ],
    "exceptions": [
      "Separate suit is expressly barred under Section 47(1)."
    ],
    "relatedTopicId": "top-cpc-12-01",
    "chapterId": "ch-cpc-12",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Determination under Section 47 is NO LONGER a decree (1976 amendment deleted S. 47 from S. 2(2)).",
    "highYield": true
  },
  {
    "id": "cpc-sec-058",
    "type": "section",
    "ref": "Section 58",
    "title": "Detention and Release in Civil Prison",
    "concept": "Every person detained in civil prison in execution of decree shall be so detained: (a) where decree exceeding Rs 5,000, up to 3 MONTHS; (b) where decree between Rs 2,000 and Rs 5,000, up to 6 WEEKS; (c) where decree does not exceed Rs 2,000, NO ARREST allowed.",
    "plainEnglish": "Maximum civil jail terms: over Rs 5,000 -> 3 months; Rs 2,000 to Rs 5,000 -> 6 weeks; up to Rs 2,000 -> complete immunity from detention.",
    "conditions": [
      "Subsistence allowance must be paid in advance by decree-holder."
    ],
    "exceptions": [
      "Release on ground of serious illness (Section 59). Release does not discharge debt."
    ],
    "relatedTopicId": "top-cpc-12-02",
    "chapterId": "ch-cpc-12",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Jolly George Varghese v. Bank of Cochin (1980): No detention without mala fides or means to pay (Art. 21).",
    "highYield": true
  },
  {
    "id": "cpc-sec-064",
    "type": "section",
    "ref": "Section 64",
    "title": "Private Alienation of Property After Attachment to Be Void",
    "concept": "Where an attachment has been made, any private transfer or delivery of property attached contrary to such attachment shall be void as against all claims enforceable under attachment.",
    "plainEnglish": "Once court attaches debtor property, any private sale, gift, or mortgage by the debtor is null and void against the decree-holder.",
    "conditions": [
      "Attachment must have been legally effected and notified."
    ],
    "exceptions": [
      "Sub-section (2) (added 2002): Does not apply to transfer made pursuant to registered contract entered into before attachment (tested in UP PCS-J 2023!)."
    ],
    "relatedTopicId": "top-cpc-12-03",
    "chapterId": "ch-cpc-12",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Section 64(2) protects prior registered agreements for sale entered before attachment.",
    "highYield": true
  },
  {
    "id": "cpc-sec-075",
    "type": "section",
    "ref": "Section 75",
    "title": "Power of Court to Issue Commissions",
    "concept": "Court may issue commission for 7 purposes: (a) to examine any person; (b) to make local investigation; (c) to examine or adjust accounts; (d) to make a partition; (e) to hold scientific investigation; (f) to conduct sale of property; (g) to perform ministerial act.",
    "plainEnglish": "Empowers court to appoint an independent commissioner to perform tasks requiring outside inspection, examination, or expertise.",
    "conditions": [
      "Discretion of court exercised under Order XXVI."
    ],
    "exceptions": [
      "Commission report is evidence in the suit (Order XXVI Rule 10(2))."
    ],
    "relatedTopicId": "top-cpc-18-02",
    "chapterId": "ch-cpc-18",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Tested in UP PCS-J 2023! Seven statutory purposes under Section 75.",
    "highYield": true
  },
  {
    "id": "cpc-sec-088",
    "type": "section",
    "ref": "Section 88",
    "title": "Where Interpleader-Suit May Be Instituted",
    "concept": "Where two or more persons claim adversely to one another the same debts, sum of money or other property from another person, who claims no interest therein other than for charges or costs and is ready to deliver it to rightful claimant, such person may institute an interpleader suit.",
    "plainEnglish": "A neutral stakeholder holding property caught between rival claimants files suit asking them to fight each other so he can deliver it safely.",
    "conditions": [
      "Plaintiff must claim no interest other than charges or costs.",
      "No suit pending where rights can be properly decided."
    ],
    "exceptions": [
      "Order XXXV Rule 5: Agents cannot sue principals, nor tenants sue landlords in interpleader."
    ],
    "relatedTopicId": "top-cpc-15-04",
    "chapterId": "ch-cpc-15",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Plaintiff in interpleader must claim NO INTEREST in subject-matter except costs.",
    "highYield": true
  },
  {
    "id": "cpc-sec-095",
    "type": "section",
    "ref": "Section 95",
    "title": "Compensation for Obtaining Arrest, Attachment or Injunction on Insufficient Grounds",
    "concept": "Where arrest, attachment or injunction was applied for on insufficient grounds or suit fails without reasonable ground, Court may award compensation up to Rs 50,000 to defendant.",
    "plainEnglish": "Summary penalty against plaintiff who abuses temporary injunction or attachment before judgment to harass defendant.",
    "conditions": [
      "Insufficient grounds or no reasonable probable cause.",
      "Applied on defendant's application before judgment."
    ],
    "exceptions": [
      "Statutory ceiling raised to Rs 50,000 (from Rs 1,000) by 1976 amendment."
    ],
    "relatedTopicId": "top-cpc-13-01",
    "chapterId": "ch-cpc-13",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Section 95 compensation ceiling is Rs. 50,000. An order under S. 95 is appealable under S. 104.",
    "highYield": true
  },
  {
    "id": "cpc-sec-100A",
    "type": "section",
    "ref": "Section 100A",
    "title": "No Further Appeal in Certain Cases",
    "concept": "Where any appeal from an original or appellate decree or order is heard and decided by a Single Judge of a High Court, no further appeal shall lie from the judgment and decree of such Single Judge (bars Letters Patent Appeal).",
    "plainEnglish": "Abolishes Letters Patent intra-court appeal to a Division Bench from a Single Judge's appellate decision.",
    "conditions": [
      "Decision rendered by Single Judge of High Court in an appeal."
    ],
    "exceptions": [
      "Substituted in 2002 to speed up finality. Does not bar Special Leave Petition to Supreme Court."
    ],
    "relatedTopicId": "top-cpc-16-02",
    "chapterId": "ch-cpc-16",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Section 100A completely bars Letters Patent Appeal from Single Judge in appeals.",
    "highYield": true
  },
  {
    "id": "cpc-sec-102",
    "type": "section",
    "ref": "Section 102",
    "title": "No Second Appeal in Certain Suits",
    "concept": "No second appeal shall lie from any decree, when the subject-matter of the original suit is for recovery of money not exceeding twenty-five thousand rupees.",
    "plainEnglish": "Monetary bar on second appeals: No second appeal in money suits valuing Rs 25,000 or less.",
    "conditions": [
      "Suit for recovery of money.",
      "Subject-matter does not exceed Rs 25,000."
    ],
    "exceptions": [
      "Substituted in 2002 (raised from Rs 3,000 to Rs 25,000)."
    ],
    "relatedTopicId": "top-cpc-16-02",
    "chapterId": "ch-cpc-16",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Section 102 monetary bar is exactly Rs. 25,000.",
    "highYield": true
  },
  {
    "id": "cpc-sec-104",
    "type": "section",
    "ref": "Section 104",
    "title": "Orders from Which Appeal Lies",
    "concept": "Appeal lies from specified orders (compensatory costs under S. 35A, refusal of arrest under S. 91/92, compensation under S. 95, fines, and orders under rules as expressly appealable under O. XLIII R. 1). No second appeal from orders (S. 104(2)).",
    "plainEnglish": "Exhaustive list of orders that can be appealed. No second appeal from orders is ever permitted.",
    "conditions": [
      "Order must fall within Section 104 or Order XLIII Rule 1."
    ],
    "exceptions": [
      "Section 104(2): NO appeal shall lie from any order passed in appeal under this section."
    ],
    "relatedTopicId": "top-cpc-16-03",
    "chapterId": "ch-cpc-16",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Section 104(2) bars second appeals against orders. An order passed in appeal under S. 104 cannot be appealed again.",
    "highYield": true
  },
  {
    "id": "cpc-sec-132",
    "type": "section",
    "ref": "Section 132",
    "title": "Exemption of Certain Women from Personal Appearance",
    "concept": "Women who, according to the customs and manners of the country, ought not to be compelled to appear in public shall be exempt from personal appearance in Court.",
    "plainEnglish": "Pardanashin women are exempt from personal physical court appearances; their evidence can be recorded by commission at home.",
    "conditions": [
      "Customary pardanashin status according to social manners of community."
    ],
    "exceptions": [
      "Exemption does not exempt from arrest in execution of civil process (except as provided in Section 56 for money)."
    ],
    "relatedTopicId": "top-cpc-10-02",
    "chapterId": "ch-cpc-10",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Pardanashin women exemption under Section 132.",
    "highYield": true
  },
  {
    "id": "cpc-sec-148",
    "type": "section",
    "ref": "Section 148",
    "title": "Enlargement of Time",
    "concept": "Where any period is fixed or granted by Court for doing any act, Court may in its discretion enlarge such period not exceeding thirty days in total, even though period originally fixed has expired.",
    "plainEnglish": "Court can extend time for procedural compliance up to a total of 30 days, even after the deadline passed.",
    "conditions": [
      "Period was fixed or granted by court (not fixed by statute/Limitation Act)."
    ],
    "exceptions": [
      "Total enlargement cannot exceed 30 days in total (added 2002). Salem Advocate Bar Association held court can exceed 30 days under S. 151 in rare exceptional cases."
    ],
    "relatedTopicId": "top-cpc-13-04",
    "chapterId": "ch-cpc-13",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Statutory limit under Section 148 is 30 days in total.",
    "highYield": true
  },
  {
    "id": "cpc-sec-152",
    "type": "section",
    "ref": "Section 152",
    "title": "Amendment of Judgments, Decrees or Orders",
    "concept": "Clerical or arithmetical mistakes in judgments, decrees or orders or errors arising therein from any accidental slip or omission may at any time be corrected by the Court either of its own motion or on application of any party.",
    "plainEnglish": "Enables courts to correct mathematical errors or typographical slips at any time without requiring formal review or appeal.",
    "conditions": [
      "Error must be clerical, arithmetical, or an accidental slip/omission."
    ],
    "exceptions": [
      "Cannot be used to modify substantive findings or alter merits of judgment."
    ],
    "relatedTopicId": "top-cpc-13-04",
    "chapterId": "ch-cpc-13",
    "sourceLabel": "Central CPC",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Correction can be made AT ANY TIME, even after years, and suo motu.",
    "highYield": true
  },
  {
    "id": "cpc-ord-04-r01",
    "type": "rule",
    "ref": "Order IV Rule 1",
    "title": "Suit to Be Commenced by Plaint",
    "concept": "Every suit shall be instituted by presenting a plaint in duplicate to the Court or such officer as it appoints. Plaint shall comply with rules of Orders VI and VII. Suit not duly instituted if not in duplicate.",
    "plainEnglish": "Every suit must be filed in duplicate (two copies); filing only one copy makes the suit invalid under Rule 1(3).",
    "conditions": [
      "Plaint must be in duplicate.",
      "Must comply with verification and affidavit rules."
    ],
    "exceptions": [
      "Sub-rule (3) added in 2002: Plaint shall not be deemed duly instituted unless in duplicate."
    ],
    "relatedTopicId": "top-cpc-04-01",
    "chapterId": "ch-cpc-04",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Mandatory requirement of filing plaint in DUPLICATE.",
    "highYield": true
  },
  {
    "id": "cpc-ord-06-r02",
    "type": "rule",
    "ref": "Order VI Rule 2",
    "title": "Pleading to State Material Facts and Not Evidence",
    "concept": "Every pleading shall contain, and contain only, a statement in a concise form of the material facts on which party relies, but not the evidence by which they are to be proved.",
    "plainEnglish": "Cardinal rule of pleadings: State facta probanda (facts to be proved), NOT facta probantia (evidence).",
    "conditions": [
      "Concise form.",
      "Divided into paragraphs numbered consecutively.",
      "Dates, sums and numbers expressed in figures as well as in words."
    ],
    "exceptions": [
      "Particulars of fraud, misrepresentation, breach of trust must be specifically stated (Rule 4)."
    ],
    "relatedTopicId": "top-cpc-06-01",
    "chapterId": "ch-cpc-06",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Fundamental rule of pleadings: State facts, not law, and not evidence.",
    "highYield": true
  },
  {
    "id": "cpc-ord-08-r06",
    "type": "rule",
    "ref": "Order VIII Rule 6",
    "title": "Particulars of Set-Off to Be Given in Written Statement",
    "concept": "In suit for recovery of money, defendant may claim set-off of any ascertained sum of money legally recoverable by him from plaintiff, not exceeding pecuniary limits, where both parties fill same character.",
    "plainEnglish": "Legal set-off: Defendant adjusts an ascertained, legally enforceable debt against plaintiff's claim in a money suit.",
    "conditions": [
      "Suit must be for recovery of money.",
      "Sum must be an ASCERTAINED sum.",
      "Must be LEGALLY RECOVERABLE (not barred by limitation).",
      "Both parties fill same character."
    ],
    "exceptions": [
      "Equitable set-off applies to unascertained sums arising out of same transaction."
    ],
    "relatedTopicId": "top-cpc-07-03",
    "chapterId": "ch-cpc-07",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Legal set-off requires an ASCERTAINED sum and must be within limitation on date of filing suit.",
    "highYield": true
  },
  {
    "id": "cpc-ord-09-r08",
    "type": "rule",
    "ref": "Order IX Rule 8",
    "title": "Procedure Where Defendant Only Appears",
    "concept": "Where defendant appears and plaintiff does not appear when suit called for hearing, Court shall make an order that suit be dismissed, unless defendant admits claim.",
    "plainEnglish": "If plaintiff is absent but defendant attends, the suit is dismissed for default.",
    "conditions": [
      "Plaintiff absent; defendant present."
    ],
    "exceptions": [
      "If defendant admits claim wholly or in part, court shall pass decree upon such admission."
    ],
    "relatedTopicId": "top-cpc-08-02",
    "chapterId": "ch-cpc-08",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Rule 9 bars fresh suit on same cause of action; plaintiff must apply for RESTORATION under Rule 9.",
    "highYield": true
  },
  {
    "id": "cpc-ord-12-r06",
    "type": "rule",
    "ref": "Order XII Rule 6",
    "title": "Judgment on Admissions",
    "concept": "Where admissions of fact have been made either in pleading or otherwise, whether orally or in writing, Court may at any stage of suit make such order or give such judgment as it may think fit.",
    "plainEnglish": "Empowers court to pass judgment immediately without waiting for trial on any part of the claim that is clearly admitted by the opposite party.",
    "conditions": [
      "Admission must be clear, unambiguous, and unconditional.",
      "Can be made in pleadings or otherwise, orally or in writing."
    ],
    "exceptions": [
      "Court has judicial discretion; not bound to pass judgment if admission ambiguous."
    ],
    "relatedTopicId": "top-cpc-09-02",
    "chapterId": "ch-cpc-09",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Judgment on admission under Order XII Rule 6 can be passed AT ANY STAGE of suit.",
    "highYield": true
  },
  {
    "id": "cpc-ord-14-r01",
    "type": "rule",
    "ref": "Order XIV Rule 1",
    "title": "Framing of Issues",
    "concept": "Issues arise when a material proposition of fact or law is affirmed by one party and denied by the other. Issues are of two kinds: (a) issues of fact; (b) issues of law.",
    "plainEnglish": "Court identifies the exact points of conflict between parties by comparing plaint allegations with written statement denials.",
    "conditions": [
      "Framed at first hearing after reading pleadings and examining parties."
    ],
    "exceptions": [
      "Rule 2: Where issues of both law and fact arise and court thinks case can be disposed of on issue of law only regarding jurisdiction or bar of law, it may try that issue first."
    ],
    "relatedTopicId": "top-cpc-10-01",
    "chapterId": "ch-cpc-10",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Preliminary issues under Order XIV Rule 2 are confined to (a) jurisdiction of court; (b) statutory bar to suit.",
    "highYield": true
  },
  {
    "id": "cpc-ord-17-r01",
    "type": "rule",
    "ref": "Order XVII Rule 1",
    "title": "Court May Grant Time and Adjourn Hearing",
    "concept": "Court may grant time and adjourn hearing of suit for reasons recorded. Provided that no such adjournment shall be granted more than THREE TIMES to a party during hearing of suit.",
    "plainEnglish": "Restricts dilatory tactics: maximum of 3 adjournments allowed to a party during suit hearing.",
    "conditions": [
      "Sufficient cause shown in writing.",
      "Costs of adjournment must be paid."
    ],
    "exceptions": [
      "Salem Advocate Bar Association held that 3-adjournment rule is directory in extreme, unforeseen emergencies beyond party's control."
    ],
    "relatedTopicId": "top-cpc-10-02",
    "chapterId": "ch-cpc-10",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Statutory limit is THREE adjournments to a party during hearing of suit.",
    "highYield": true
  },
  {
    "id": "cpc-ord-20-r01",
    "type": "rule",
    "ref": "Order XX Rule 1",
    "title": "Judgment When Pronounced",
    "concept": "Court after hearing shall pronounce judgment in open Court, either at once or within 30 days. If not practicable within 30 days for exceptional reasons, within 60 days.",
    "plainEnglish": "Strict timeline for judgment delivery: immediately or within 30 days, maximum 60 days in extraordinary cases.",
    "conditions": [
      "Pronounced in open court.",
      "Future date fixed with notice to parties."
    ],
    "exceptions": [
      "Anil Rai v. State of Bihar (guidelines on delayed judgments)."
    ],
    "relatedTopicId": "top-cpc-11-01",
    "chapterId": "ch-cpc-11",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Judgment delivery timeline: 30 days, extendable up to 60 days maximum.",
    "highYield": true
  },
  {
    "id": "cpc-ord-21-r22",
    "type": "rule",
    "ref": "Order XXI Rule 22",
    "title": "Notice to Show Cause Against Execution in Certain Cases",
    "concept": "Notice to show cause must be issued where execution applied for more than TWO YEARS after date of decree, or against legal representative of judgment-debtor.",
    "plainEnglish": "Protective notice: If execution is filed more than 2 years after decree, court must issue notice to debtor before issuing warrant.",
    "conditions": [
      "Application made more than 2 years after decree date, or against legal representative."
    ],
    "exceptions": [
      "Omission to issue notice when required goes to jurisdiction of executing court."
    ],
    "relatedTopicId": "top-cpc-12-01",
    "chapterId": "ch-cpc-12",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Notice is mandatory after TWO YEARS (amended from 1 year in 1976).",
    "highYield": true
  },
  {
    "id": "cpc-ord-21-r89",
    "type": "rule",
    "ref": "Order XXI Rule 89",
    "title": "Application to Set Aside Sale on Deposit",
    "concept": "Any person claiming interest in property sold in execution may apply to set aside sale on depositing: (a) 5% of purchase money for payment to purchaser; and (b) sum specified in proclamation for payment to decree-holder. Must be deposited within 60 days.",
    "plainEnglish": "Allows debtor/owner to save sold property by depositing the decree debt plus a 5% bonus to the auction buyer within 60 days.",
    "conditions": [
      "Deposit 5% penalty for auction purchaser.",
      "Deposit entire decree amount.",
      "Must be made within 60 days under Article 127 Limitation Act."
    ],
    "exceptions": [
      "Cannot apply under Rule 89 if application under Rule 90 is pending unless withdrawn."
    ],
    "relatedTopicId": "top-cpc-12-04",
    "chapterId": "ch-cpc-12",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Penalty payable to purchaser under Rule 89 is exactly 5% of purchase money.",
    "highYield": true
  },
  {
    "id": "cpc-ord-23-r03",
    "type": "rule",
    "ref": "Order XXIII Rule 3",
    "title": "Compromise of Suit",
    "concept": "Where suit has been adjusted wholly or in part by lawful agreement or compromise in writing and signed by parties, Court shall order compromise recorded and pass decree in accordance therewith.",
    "plainEnglish": "Compromise decree: Must be in writing, signed by both parties, and lawful. Rule 3A bars fresh suit to set aside compromise decree on ground that it was not lawful.",
    "conditions": [
      "Lawful agreement or compromise.",
      "In writing and signed by parties."
    ],
    "exceptions": [
      "Rule 3A: No suit shall lie to set aside a decree on the ground that the compromise on which the decree is based was not lawful."
    ],
    "relatedTopicId": "top-cpc-14-02",
    "chapterId": "ch-cpc-14",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Pushpa Devi Bhagat v. Rajinder Singh (2006): Order XXIII Rule 3A bars separate suit against compromise decree.",
    "highYield": true
  },
  {
    "id": "cpc-ord-32-r03",
    "type": "rule",
    "ref": "Order XXXII Rule 3",
    "title": "Guardian for the Suit to Be Appointed by Court for Minor Defendant",
    "concept": "Where defendant is a minor, Court on application shall appoint a proper person to be guardian for the suit (guardian ad litem). Minor cannot be sued without guardian.",
    "plainEnglish": "A minor defendant must be defended by a court-appointed guardian ad litem; decree against unrepresented minor is a nullity.",
    "conditions": [
      "Application supported by affidavit.",
      "Notice to minor and natural guardian."
    ],
    "exceptions": [
      "Rule 3A: Decree against minor not set aside merely because guardian had interest adverse unless prejudice caused."
    ],
    "relatedTopicId": "top-cpc-15-02",
    "chapterId": "ch-cpc-15",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Next friend represents minor PLAINTIFF; Guardian ad litem represents minor DEFENDANT.",
    "highYield": true
  },
  {
    "id": "cpc-ord-33-r01",
    "type": "rule",
    "ref": "Order XXXIII Rule 1",
    "title": "Suits by Indigent Persons",
    "concept": "Suit may be instituted by an indigent person (pauper) without payment of court fees. A person is indigent if not possessed of sufficient means (other than exempt property) to pay fee, or where no fee prescribed, not entitled to property worth Rs 1,000.",
    "plainEnglish": "Provides access to justice for poor litigants unable to afford court fees.",
    "conditions": [
      "Possesses insufficient means to pay court fees."
    ],
    "exceptions": [
      "Property exempt under Section 60 excluded in assessing indigency. If indigent succeeds, court fee is recovered from subject-matter (Rule 10)."
    ],
    "relatedTopicId": "top-cpc-15-03",
    "chapterId": "ch-cpc-15",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Indigent person can sue without court fee. Exempt assets under Section 60 are NOT counted.",
    "highYield": true
  },
  {
    "id": "cpc-ord-37-r02",
    "type": "rule",
    "ref": "Order XXXVII Rule 2 & 3",
    "title": "Summary Procedure on Negotiable Instruments & Debt Claims",
    "concept": "Fast-track procedure for promissory notes, bills of exchange, cheques, or written contracts for debt. Defendant cannot defend as of right; must enter appearance within 10 days and apply for leave to defend.",
    "plainEnglish": "Express debt recovery: defendant must enter appearance in 10 days and prove a genuine triable issue to get leave to defend, otherwise plaintiff gets immediate decree.",
    "conditions": [
      "Applies to High Courts, City Civil Courts, Courts of Small Causes, and notified courts.",
      "Defendant must enter appearance within 10 DAYS of summons."
    ],
    "exceptions": [
      "IDBI Trusteeship Services v. Hubtown Ltd (2017): Principles governing grant of leave to defend (unconditional, conditional, or refusal)."
    ],
    "relatedTopicId": "top-cpc-15-04",
    "chapterId": "ch-cpc-15",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Defendant must enter appearance within 10 DAYS under Order XXXVII Rule 3.",
    "highYield": true
  },
  {
    "id": "cpc-ord-38-r05",
    "type": "rule",
    "ref": "Order XXXVIII Rule 5",
    "title": "Attachment Before Judgment",
    "concept": "Where Court is satisfied defendant with intent to obstruct or delay execution is about to dispose of or remove property from local limits of court, Court may direct defendant to furnish security or attach property.",
    "plainEnglish": "Drastic pre-trial remedy to stop dishonest defendants from liquidating or hiding assets before judgment.",
    "conditions": [
      "Intent to obstruct or delay execution of decree.",
      "About to dispose of or remove property from court limits."
    ],
    "exceptions": [
      "Rule 5(4): If attachment made without complying with Rule 5(1), attachment shall be VOID."
    ],
    "relatedTopicId": "top-cpc-13-01",
    "chapterId": "ch-cpc-13",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Raman Tech v. Bharat Tractors (2008): Order XXXVIII Rule 5 is an extraordinary power, not to be used mechanically.",
    "highYield": true
  },
  {
    "id": "cpc-ord-39-r02A",
    "type": "rule",
    "ref": "Order XXXIX Rule 2A",
    "title": "Consequence of Disobedience or Breach of Injunction",
    "concept": "In case of disobedience of injunction or breach of terms, Court may order property of guilty person to be attached and order such person to be detained in civil prison for not exceeding THREE MONTHS.",
    "plainEnglish": "Penal sanction for violating injunction orders: property attached for up to 1 year or civil jail up to 3 months.",
    "conditions": [
      "Willful disobedience of injunction order."
    ],
    "exceptions": [
      "Attachment shall not remain in force for more than 1 YEAR; property may be sold to award compensation."
    ],
    "relatedTopicId": "top-cpc-13-02",
    "chapterId": "ch-cpc-13",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Maximum detention for breach of injunction is THREE MONTHS (tested in UP PCS-J 2015!).",
    "highYield": true
  },
  {
    "id": "cpc-ord-40-r01",
    "type": "rule",
    "ref": "Order XL Rule 1",
    "title": "Appointment of Receivers",
    "concept": "Where it appears to Court to be just and convenient, Court may by order appoint a receiver of any property, whether before or after decree.",
    "plainEnglish": "An officer of the court appointed to take charge of and manage disputed property to protect it from waste or plunder.",
    "conditions": [
      "Court must find it 'just and convenient'."
    ],
    "exceptions": [
      "Does not authorize court to dispossess non-party entitled to possession."
    ],
    "relatedTopicId": "top-cpc-13-03",
    "chapterId": "ch-cpc-13",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Five principles governing receiver appointment established in Krishnaswamy v. Thangavelu (1955).",
    "highYield": true
  },
  {
    "id": "cpc-ord-41-r27",
    "type": "rule",
    "ref": "Order XLI Rule 27",
    "title": "Production of Additional Evidence in Appellate Court",
    "concept": "Parties to appeal not entitled to produce additional evidence in Appellate Court EXCEPT: (a) lower court improperly refused evidence; (aa) party could not produce despite due diligence; or (b) Appellate Court requires document to pronounce judgment.",
    "plainEnglish": "Appellate courts decide on original trial records; fresh evidence in appeal is permitted only under the 3 strict exceptions of Rule 27.",
    "conditions": [
      "Strict compliance with clauses (a), (aa), or (b).",
      "Appellate Court must record reasons."
    ],
    "exceptions": [
      "Additional evidence cannot be admitted to fill lacunae or gaps in party's case."
    ],
    "relatedTopicId": "top-cpc-16-01",
    "chapterId": "ch-cpc-16",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Clause (b): 'To enable it to pronounce judgment' is the court's requirement, not party's right.",
    "highYield": true
  },
  {
    "id": "cpc-ord-43-r01",
    "type": "rule",
    "ref": "Order XLIII Rule 1",
    "title": "Appeals from Orders (List of Appealable Orders)",
    "concept": "Specifies orders from which an appeal lies under Section 104: e.g. returning plaint (O. VII R. 10), rejecting application to set aside ex parte decree (O. IX R. 13), refusal to grant injunction (O. XXXIX R. 1/2), breach of injunction (O. XXXIX R. 2A).",
    "plainEnglish": "The definitive master catalogue of non-decree interlocutory and final orders that can be appealed.",
    "conditions": [
      "Order must be explicitly enumerated in Rule 1 clauses (a) to (w)."
    ],
    "exceptions": [
      "No appeal lies from an order rejecting application under Order IX Rule 9 unless listed. Section 104(2) bars second appeal."
    ],
    "relatedTopicId": "top-cpc-16-03",
    "chapterId": "ch-cpc-16",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Frequent UP PCS-J question: Match orders with appealability under Order XLIII Rule 1.",
    "highYield": true
  },
  {
    "id": "cpc-ord-47-r01",
    "type": "rule",
    "ref": "Order XLVII Rule 1",
    "title": "Application for Review of Judgment",
    "concept": "Prescribes procedure and grounds for review under Section 114: discovery of new evidence, mistake or error apparent on face of record, or any other sufficient reason.",
    "plainEnglish": "Procedural mechanics of review: Must be made to the same court; 'error apparent' must be patent and manifest without elaborate argument.",
    "conditions": [
      "Patent error on face of record (not a point requiring detailed reasoning).",
      "No appeal pending."
    ],
    "exceptions": [
      "Rule 7: Order rejecting review is NOT appealable; order granting review is appealable under Rule 7."
    ],
    "relatedTopicId": "top-cpc-17-02",
    "chapterId": "ch-cpc-17",
    "sourceLabel": "First Schedule Order/Rule",
    "indiaCodeUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
    "examTips": "Order REJECTING review application is NOT appealable (Order XLVII Rule 7).",
    "highYield": true
  }
];

  if (typeof module !== "undefined" && module.exports) {
    module.exports = DATA;
  }
  if (typeof window !== "undefined") {
    global.CPC_SECTIONS_ORDERS_RULES = DATA;
  }
})(typeof window !== "undefined" ? window : global);
