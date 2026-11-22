# -*- coding: utf-8 -*-
"""
Generator script for scripts/cpc_mcq_part_d.py
Chapters 16 to 20 (100 MCQs):
- Ch 16: First & Second Appeals, Order Appeals (20 MCQs)
- Ch 17: Reference, Review & Revision (20 MCQs)
- Ch 18: ADR, Commissions & Restitution (20 MCQs)
- Ch 19: UP State Amendments & High Court Practice (20 MCQs)
- Ch 20: Comprehensive Review, Traps & Precedents (20 MCQs)
"""
import json

questions_ch16 = [
    {
        "id": "mcq-cpc-16-001",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-16",
        "topicId": "top-cpc-16-01",
        "question": "Under Section 96(1) of the CPC, an appeal lies from every decree passed by any court exercising original jurisdiction, except:",
        "options": [
            "Where an appeal is expressly barred by the Code or by any other law for the time being in force",
            "Where the value of the suit exceeds rupees ten lakhs",
            "Where the decree is an ex parte decree",
            "Where the decree is passed by a Senior Civil Judge"
        ],
        "answer": 0,
        "answerLetter": "A",
        "explanation": "Section 96(1) provides that an appeal shall lie from every decree passed by any court exercising original jurisdiction to the court authorized to hear appeals from the decisions of such court, save where otherwise expressly provided in the body of this Code or by any other law.",
        "optionBreakdown": {
            "A": "Correct; statutory exception in Section 96(1) excludes decrees where an appeal is expressly barred by law.",
            "B": "Incorrect; high valuation does not bar appeal; it merely determines the appellate forum.",
            "C": "Incorrect; Section 96(2) explicitly provides that an appeal lies from an original decree passed ex parte.",
            "D": "Incorrect; decrees of Senior Civil Judges are appealable to the District Court or High Court."
        },
        "difficulty": "Standard",
        "provision": "Section 96(1) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Understand the general right of first appeal and statutory exceptions under Section 96(1)."
    },
    {
        "id": "mcq-cpc-16-002",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-16",
        "topicId": "top-cpc-16-01",
        "question": "According to Section 96(3) of the CPC, no appeal shall lie from a decree passed by the court:",
        "options": [
            "With the consent of parties (consent decree)",
            "In an ex parte proceeding",
            "In a suit for partition",
            "Under summary procedure of Order XXXVII"
        ],
        "answer": 0,
        "answerLetter": "A",
        "explanation": "Section 96(3) CPC explicitly enacts: 'No appeal shall lie from a decree passed by the Court with the consent of parties.' Such decrees can only be challenged on grounds like fraud or lack of compromise recording under Order XXIII Rule 3A.",
        "optionBreakdown": {
            "A": "Correct; Section 96(3) bars an appeal against a consent decree.",
            "B": "Incorrect; Section 96(2) expressly permits appeals against ex parte decrees.",
            "C": "Incorrect; partition decrees are regular decrees appealable under Section 96(1).",
            "D": "Incorrect; summary decrees under Order XXXVII are appealable regular decrees."
        },
        "difficulty": "Standard",
        "provision": "Section 96(3) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Identify the absolute statutory bar against appeals from consent decrees under Section 96(3)."
    },
    {
        "id": "mcq-cpc-16-003",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-16",
        "topicId": "top-cpc-16-01",
        "question": "Under Section 96(4) of the CPC (inserted by the 1976 Amendment), no appeal lies from a decree in any suit cognizable by Courts of Small Causes, except on a question of law, when the value of the subject-matter does not exceed:",
        "options": [
            "Rs. 1,000",
            "Rs. 5,000",
            "Rs. 10,000",
            "Rs. 25,000"
        ],
        "answer": 2,
        "answerLetter": "C",
        "explanation": "Section 96(4) CPC states that no appeal shall lie, except on a question of law, from a decree in any suit of the nature cognizable by Courts of Small Causes, when the amount or value of the subject-matter of the original suit does not exceed ten thousand rupees.",
        "optionBreakdown": {
            "A": "Incorrect; Rs. 1,000 was the pre-1976 or obsolete threshold.",
            "B": "Incorrect; Rs. 5,000 is not the Section 96(4) limit.",
            "C": "Correct; Section 96(4) fixes the monetary ceiling at Rs. 10,000 for Small Cause nature suits.",
            "D": "Incorrect; Rs. 25,000 is the limit for bar of second appeals under Section 102."
        },
        "difficulty": "Important",
        "provision": "Section 96(4) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Recall the monetary ceiling of Rs. 10,000 for Small Cause nature suits under Section 96(4)."
    },
    {
        "id": "mcq-cpc-16-004",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-16",
        "topicId": "top-cpc-16-01",
        "question": "What is the legal effect of Section 99 of the CPC regarding reversals or modifications of decrees by an appellate court?",
        "options": [
            "A decree can be reversed for any typographical error in the plaint",
            "No decree shall be reversed or substantially varied on account of any misjoinder or non-joinder of parties or causes of action, or error not affecting the merits or jurisdiction",
            "Every procedural irregularity mandatorily requires remand for de novo trial",
            "Appellate court has no jurisdiction to look into procedural errors even if jurisdiction is affected"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 99 CPC enacts that no decree shall be reversed or substantially varied, nor shall any case be remanded, on account of any misjoinder or non-joinder of parties or causes of action or any error, defect or irregularity in proceedings not affecting the merits of the case or the jurisdiction of the Court. Provided that nothing applies to non-joinder of a necessary party.",
        "optionBreakdown": {
            "A": "Incorrect; Section 99 prohibits reversals on minor or technical errors not affecting merits.",
            "B": "Correct; Section 99 protects decrees from technical reversals where merits and jurisdiction are untouched.",
            "C": "Incorrect; remand is prohibited for harmless technical defects.",
            "D": "Incorrect; errors affecting jurisdiction are expressly not cured by Section 99."
        },
        "difficulty": "Important",
        "provision": "Section 99 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Master the protective doctrine of Section 99 regarding harmless procedural irregularities."
    },
    {
        "id": "mcq-cpc-16-005",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-16",
        "topicId": "top-cpc-16-01",
        "question": "Under Order XLI Rule 22 of the CPC, within what period from the date of service of notice of day fixed for hearing appeal may a respondent file cross-objections?",
        "options": [
            "Within fifteen days",
            "Within one month",
            "Within sixty days",
            "Within ninety days"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Order XLI Rule 22(1) prescribes that cross-objections must be filed within one month from the date of service of notice on the respondent or his pleader of the day fixed for hearing the appeal, or within such further time as the Appellate Court may see fit to allow.",
        "optionBreakdown": {
            "A": "Incorrect; 15 days is too short.",
            "B": "Correct; Order XLI Rule 22(1) specifies 'within one month' from service of notice.",
            "C": "Incorrect; 60 days is not the statutory period.",
            "D": "Incorrect; 90 days is the standard limitation for second appeals, not cross-objections."
        },
        "difficulty": "Important",
        "provision": "Order XLI Rule 22(1) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Know the limitation period of one month for filing cross-objections under Order XLI Rule 22."
    },
    {
        "id": "mcq-cpc-16-006",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-16",
        "topicId": "top-cpc-16-01",
        "question": "If an original appeal is withdrawn or dismissed for default, what is the fate of cross-objections filed by the respondent under Order XLI Rule 22(4)?",
        "options": [
            "They automatically lapse and stand dismissed",
            "They shall nevertheless be heard and determined after such notice to other parties as the court thinks fit",
            "They are converted into a fresh original suit",
            "They can only be heard if the appellant deposits costs"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Order XLI Rule 22(4) explicitly provides that where in any case the original appeal is withdrawn or is dismissed for default, the cross-objection may nevertheless be heard and determined after such notice to the other parties as the Court thinks fit.",
        "optionBreakdown": {
            "A": "Incorrect; cross-objections possess substantive independent vitality under sub-rule (4).",
            "B": "Correct; Order XLI Rule 22(4) mandates that cross-objections survive withdrawal or default dismissal of the main appeal.",
            "C": "Incorrect; cross-objections remain within the appellate proceedings.",
            "D": "Incorrect; hearing does not depend on appellant depositing costs."
        },
        "difficulty": "Important",
        "provision": "Order XLI Rule 22(4) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Understand that cross-objections survive the withdrawal or dismissal for default of the main appeal."
    },
    {
        "id": "mcq-cpc-16-007",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-16",
        "topicId": "top-cpc-16-01",
        "question": "Under Order XLI Rule 27 of the CPC, additional evidence can be produced in the Appellate Court in which of the following circumstances?",
        "options": [
            "As a matter of absolute right whenever an appellant feels their case was weak",
            "When the trial court improperly refused to admit evidence, or party establishes due diligence, or the Appellate Court requires it to pronounce judgment",
            "Only if both parties execute a joint affidavit agreeing to introduce fresh evidence",
            "Whenever new case laws are published during the pendency of the appeal"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Order XLI Rule 27 permits additional evidence only if: (a) trial court refused to admit evidence which ought to have been admitted; (aa) party establishes that despite due diligence such evidence was not within knowledge or could not be produced; or (b) Appellate Court requires any document or witness to enable it to pronounce judgment or for any other substantial cause.",
        "optionBreakdown": {
            "A": "Incorrect; parties have no right to produce additional evidence to fill lacunae.",
            "B": "Correct; Order XLI Rule 27 strictly circumscribes additional evidence to these three exceptional conditions.",
            "C": "Incorrect; consent of parties cannot confer jurisdiction if statutory grounds are absent.",
            "D": "Incorrect; citations of case law are legal arguments, not additional evidentiary facts."
        },
        "difficulty": "Important",
        "provision": "Order XLI Rule 27 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Master the strict conditions for production of additional evidence under Order XLI Rule 27."
    },
    {
        "id": "mcq-cpc-16-008",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-16",
        "topicId": "top-cpc-16-02",
        "question": "Under Section 100(1) of the CPC, a second appeal lies to the High Court from every decree passed in appeal by any subordinate court, if the High Court is satisfied that the case involves:",
        "options": [
            "Any erroneous finding of fact",
            "A substantial question of law",
            "A dispute of valuation exceeding rupees fifty thousand",
            "Improper exercise of judicial discretion on adjournment"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 100(1) CPC provides that an appeal shall lie to the High Court from every decree passed in appeal by any Court subordinate to the High Court, if the High Court is satisfied that the case involves a substantial question of law.",
        "optionBreakdown": {
            "A": "Incorrect; findings of fact are final with the first appellate court unless perverse.",
            "B": "Correct; Section 100(1) mandates the existence of a 'substantial question of law'.",
            "C": "Incorrect; valuation does not create a second appeal; in fact Section 102 bars it if valuation <= Rs. 25,000.",
            "D": "Incorrect; discretionary adjournment orders do not constitute a substantial question of law."
        },
        "difficulty": "Standard",
        "provision": "Section 100(1) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Identify 'substantial question of law' as the sole jurisdictional foundation for a second appeal."
    },
    {
        "id": "mcq-cpc-16-009",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-16",
        "topicId": "top-cpc-16-02",
        "question": "According to the Supreme Court's landmark judgment in Chunilal V. Mehta & Sons Ltd. v. Century Spg. & Mfg. Co. Ltd. (AIR 1962 SC 1314), what constitutes a 'substantial question of law'?",
        "options": [
            "Any question of law on which the trial judge wrote a lengthy dissenting note",
            "A question directly affecting rights of parties which is open to debate, not covered by precedent or where divergent views exist",
            "Any legal argument advanced by Senior Advocates before the High Court",
            "Any matter where the High Court disagrees with the monetary calculation of damages"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "The Constitution Bench in Chunilal Mehta held that the proper test is whether the question directly and substantially affects rights of parties, is an open question not finally settled by the Supreme Court or Privy Council, or is not free from difficulty or calls for discussion of alternative views.",
        "optionBreakdown": {
            "A": "Incorrect; length of judgment or dissent does not make a question substantial.",
            "B": "Correct; Chunilal Mehta laid down that an unsettled, debatable question affecting rights of parties is substantial.",
            "C": "Incorrect; stature of counsel is irrelevant to the objective legal test.",
            "D": "Incorrect; monetary calculation of damages is a question of fact or assessment."
        },
        "difficulty": "Advanced",
        "provision": "Section 100 CPC Precedent",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Analyze the authoritative test of 'substantial question of law' under Chunilal Mehta."
    },
    {
        "id": "mcq-cpc-16-010",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-16",
        "topicId": "top-cpc-16-02",
        "question": "What is the procedure mandated by Section 100(4) of the CPC when the High Court is satisfied that a substantial question of law is involved in a second appeal?",
        "options": [
            "The High Court must dismiss the appeal and refer it to arbitration",
            "The High Court shall formulate that question and the appeal shall be heard on the question so formulated",
            "The High Court must immediately frame issues and summon oral witnesses",
            "The High Court must transfer the case to the District Judge for fresh trial"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 100(4) CPC mandates: 'Where the High Court is satisfied that a substantial question of law is involved in any case, it shall formulate that question.' Section 100(5) provides that the appeal shall be heard on the question so formulated.",
        "optionBreakdown": {
            "A": "Incorrect; High Court cannot dismiss and refer without hearing.",
            "B": "Correct; Section 100(4) requires mandatory formulation of the substantial question of law.",
            "C": "Incorrect; second appeals do not involve trial of witnesses.",
            "D": "Incorrect; transfer for retrial is not the standard procedure on admission."
        },
        "difficulty": "Important",
        "provision": "Section 100(4) & (5) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Understand the mandatory formulation of substantial questions of law under Section 100(4)."
    },
    {
        "id": "mcq-cpc-16-011",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-16",
        "topicId": "top-cpc-16-02",
        "question": "Under Section 100A of the CPC (inserted by the 2002 Amendment), where any appeal from an original or appellate decree or order is heard and decided by a Single Judge of a High Court:",
        "options": [
            "A Letters Patent Appeal or intra-court appeal lies as of right to a Division Bench",
            "No further appeal shall lie to a Division Bench of the High Court, notwithstanding any Letters Patent or law",
            "An appeal lies directly to the District Judge",
            "A further appeal lies only if the Single Judge grants a certificate of fitness"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 100A bars intra-court Letters Patent Appeals from the judgment of a Single Judge: 'Notwithstanding anything contained in any Letters Patent for any High Court or in any instrument having the force of law or in any other law... no further appeal shall lie from the judgment and decree of such Single Judge.'",
        "optionBreakdown": {
            "A": "Incorrect; Section 100A specifically abolished LPAs against Single Judge appellate decisions.",
            "B": "Correct; Section 100A creates a non-obstante bar against intra-court appeals from Single Judge appellate decisions.",
            "C": "Incorrect; District Judge is subordinate to the High Court.",
            "D": "Incorrect; Section 100A bar is absolute; Single Judge cannot grant certificate to Division Bench."
        },
        "difficulty": "Important",
        "provision": "Section 100A CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Know the abolition of Letters Patent intra-court appeals under Section 100A."
    },
    {
        "id": "mcq-cpc-16-012",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-16",
        "topicId": "top-cpc-16-02",
        "question": "Under Section 102 of the CPC, as substituted by the 2002 Amendment, no second appeal shall lie from any decree, when the subject matter of the original suit is for recovery of money not exceeding:",
        "options": [
            "Rs. 10,000",
            "Rs. 25,000",
            "Rs. 50,000",
            "Rs. 1,00,000"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 102 CPC explicitly enacts: 'No second appeal shall lie from any decree, when the subject matter of the original suit is for recovery of money not exceeding twenty-five thousand rupees.'",
        "optionBreakdown": {
            "A": "Incorrect; Rs. 10,000 is the limit for first appeal bar under Section 96(4).",
            "B": "Correct; Section 102 fixes the ceiling at Rs. 25,000 for suits for recovery of money.",
            "C": "Incorrect; Rs. 50,000 is not the statutory limit.",
            "D": "Incorrect; Rs. 1,00,000 is not the Section 102 limit."
        },
        "difficulty": "Standard",
        "provision": "Section 102 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Recall the Rs. 25,000 monetary threshold barring second appeals under Section 102."
    },
    {
        "id": "mcq-cpc-16-013",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-16",
        "topicId": "top-cpc-16-02",
        "question": "Under Section 103 of the CPC, in what circumstances may the High Court determine an issue of fact in a second appeal?",
        "options": [
            "In every case where the High Court feels the evidence was misappreciated",
            "Where evidence on record is sufficient, and the issue has not been determined by the lower appellate court or has been determined wrongly by reason of a decision on a question of law",
            "Only if both parties consent in writing to waive trial court findings",
            "Never; High Court has zero jurisdiction to touch facts under any circumstances"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 103 provides that High Court may, if evidence on record is sufficient, determine any issue necessary for disposal of appeal: (a) which has not been determined by lower Appellate Court or trial court; or (b) which has been wrongly determined by reason of any decision on such question of law.",
        "optionBreakdown": {
            "A": "Incorrect; mere difference of opinion does not empower High Court to re-appreciate facts.",
            "B": "Correct; Section 103 empowers determination of facts where evidence is sufficient and conditions (a) or (b) are met.",
            "C": "Incorrect; consent is not the statutory criterion.",
            "D": "Incorrect; Section 103 expressly provides the statutory exception."
        },
        "difficulty": "Important",
        "provision": "Section 103 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Examine the High Court's limited power to determine issues of fact under Section 103."
    },
    {
        "id": "mcq-cpc-16-014",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-16",
        "topicId": "top-cpc-16-02",
        "question": "Can a second appeal lie from an appellate decree passed ex parte under Section 100(2) of the CPC?",
        "options": [
            "No, second appeals can only lie from contested decrees",
            "Yes, an appeal may lie under Section 100 from an appellate decree passed ex parte",
            "Only if an application under Order XLI Rule 21 was rejected first",
            "Only with prior leave of the Supreme Court"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 100(2) explicitly provides: 'An appeal may lie under this section from an appellate decree passed ex parte.' The respondent can choose to file an application under Order XLI Rule 21 to re-hear the appeal or file a second appeal under Section 100(2).",
        "optionBreakdown": {
            "A": "Incorrect; Section 100(2) expressly allows second appeals against ex parte appellate decrees.",
            "B": "Correct; Section 100(2) explicitly provides for second appeal from an ex parte appellate decree.",
            "C": "Incorrect; rejection of O. XLI R. 21 is not a mandatory prerequisite.",
            "D": "Incorrect; Supreme Court leave is not required under Section 100."
        },
        "difficulty": "Standard",
        "provision": "Section 100(2) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Understand the maintainability of second appeals against ex parte appellate decrees under Section 100(2)."
    },
    {
        "id": "mcq-cpc-16-015",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-16",
        "topicId": "top-cpc-16-03",
        "question": "Which section of the CPC enumerates the orders from which an appeal lies, and states that no appeal shall lie from any other order save as provided by the Code or law?",
        "options": [
            "Section 96",
            "Section 100",
            "Section 104",
            "Section 115"
        ],
        "answer": 2,
        "answerLetter": "C",
        "explanation": "Section 104(1) CPC provides for 'Orders from which appeal lies' and explicitly provides that no appeal shall lie from any other orders save as otherwise expressly provided in the body of this Code or by any law. Order XLIII Rule 1 gives the detailed list.",
        "optionBreakdown": {
            "A": "Incorrect; Section 96 deals with appeals from original decrees.",
            "B": "Incorrect; Section 100 deals with second appeals from decrees.",
            "C": "Correct; Section 104 governs appeals from orders.",
            "D": "Incorrect; Section 115 governs revision, not appeals."
        },
        "difficulty": "Standard",
        "provision": "Section 104 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Identify Section 104 as the governing provision for appealable orders."
    },
    {
        "id": "mcq-cpc-16-016",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-16",
        "topicId": "top-cpc-16-03",
        "question": "What is the rule regarding a second appeal from an order passed in appeal under Section 104(2) of the CPC?",
        "options": [
            "A second appeal lies to the High Court if a substantial question of law arises",
            "No appeal shall lie from any order passed in appeal under Section 104",
            "A second appeal lies with the permission of the District Judge",
            "A second appeal lies if the valuation exceeds Rs. 1,00,000"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 104(2) CPC enacts an absolute statutory bar: 'No appeal shall lie from any order passed in appeal under this section.' Thus, there is no second appeal against an appellate order.",
        "optionBreakdown": {
            "A": "Incorrect; Section 104(2) bars second appeals even if a question of law arises.",
            "B": "Correct; Section 104(2) categorically bars any second appeal against an order passed in appeal.",
            "C": "Incorrect; permission cannot override Section 104(2).",
            "D": "Incorrect; valuation is irrelevant under Section 104(2)."
        },
        "difficulty": "Standard",
        "provision": "Section 104(2) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Recognize the absolute bar against second appeals from appellate orders under Section 104(2)."
    },
    {
        "id": "mcq-cpc-16-017",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-16",
        "topicId": "top-cpc-16-03",
        "question": "Which of the following orders is NOT appealable under Order XLIII Rule 1 of the CPC?",
        "options": [
            "An order under Order VII Rule 10 returning a plaint to be presented to the proper court",
            "An order under Order IX Rule 9 rejecting an application to set aside dismissal of a suit",
            "An order under Order XIV Rule 5 framing or refusing to frame an additional issue",
            "An order under Order XXXIX Rule 1 granting a temporary injunction"
        ],
        "answer": 2,
        "answerLetter": "C",
        "explanation": "Framing or refusing to frame issues under Order XIV Rule 5 is not an appealable order under Order XLIII Rule 1. An order returning plaint (O. VII R. 10), rejecting O. IX R. 9, and temporary injunction (O. XXXIX R. 1/2) are all appealable under Order XLIII Rule 1(a), (c), and (r) respectively.",
        "optionBreakdown": {
            "A": "Incorrect; appealable under Order XLIII Rule 1(a).",
            "B": "Incorrect; appealable under Order XLIII Rule 1(c).",
            "C": "Correct; order framing or refusing to frame issues is interlocutory and NOT appealable under Order XLIII Rule 1.",
            "D": "Incorrect; appealable under Order XLIII Rule 1(r)."
        },
        "difficulty": "Important",
        "provision": "Order XLIII Rule 1 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Distinguish appealable orders under Order XLIII Rule 1 from non-appealable interlocutory orders."
    },
    {
        "id": "mcq-cpc-16-018",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-16",
        "topicId": "top-cpc-16-03",
        "question": "Under Section 105(1) of the CPC, if an interlocutory order is not appealable, how can its correctness be challenged by an aggrieved party?",
        "options": [
            "It can never be challenged anywhere and attains permanent finality",
            "It may be set forth as a ground of objection in the memorandum of appeal against the final decree",
            "The party must immediately file a contempt petition",
            "The party must seek reference to the full bench of the High Court"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 105(1) CPC provides that save as otherwise expressly provided, no appeal shall lie from any order; but where a decree is appealed from, any error, defect or irregularity in any order affecting the decision of the case may be set forth as a ground of objection in the memorandum of appeal.",
        "optionBreakdown": {
            "A": "Incorrect; non-appealable orders are not immune from challenge in the final appeal.",
            "B": "Correct; Section 105(1) allows challenging non-appealable orders in the appeal against the final decree.",
            "C": "Incorrect; contempt has no relevance to procedural errors.",
            "D": "Incorrect; reference to full bench is not the mechanism."
        },
        "difficulty": "Important",
        "provision": "Section 105(1) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Understand the mechanism of challenging non-appealable orders in decree appeals under Section 105(1)."
    },
    {
        "id": "mcq-cpc-16-019",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-16",
        "topicId": "top-cpc-16-03",
        "question": "What is the crucial exception enacted by Section 105(2) of the CPC regarding an order of remand from which an appeal lies?",
        "options": [
            "If a party aggrieved by an appealable order of remand does not appeal from it, they are precluded from disputing its correctness thereafter",
            "Order of remand can never be appealed under any provision of the Code",
            "An unappealed remand order automatically voids the entire suit",
            "The trial court can refuse to accept the remand order"
        ],
        "answer": 0,
        "answerLetter": "A",
        "explanation": "Section 105(2) CPC provides: 'Notwithstanding anything contained in sub-section (1), where any party aggrieved by an order of remand from which an appeal lies does not appeal therefrom, he shall thereafter be precluded from disputing its correctness.'",
        "optionBreakdown": {
            "A": "Correct; Section 105(2) creates statutory preclusion: failure to appeal an appealable remand order bars subsequent challenge.",
            "B": "Incorrect; order of remand under Order XLI Rule 23 is appealable under Order XLIII Rule 1(u).",
            "C": "Incorrect; remand directs re-hearing, not voiding of suit.",
            "D": "Incorrect; subordinate trial court is bound by appellate remand."
        },
        "difficulty": "Advanced",
        "provision": "Section 105(2) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Master the rule of preclusion against challenging unappealed remand orders under Section 105(2)."
    },
    {
        "id": "mcq-cpc-16-020",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-16",
        "topicId": "top-cpc-16-03",
        "question": "Under Section 109 of the CPC (read with Article 133 of the Constitution), an appeal lies to the Supreme Court from any judgment, decree or final order in a civil proceeding of a High Court, if the High Court certifies:",
        "options": [
            "That the valuation exceeds fifty lakh rupees",
            "That the case involves a substantial question of law of general importance and in the opinion of the High Court needs to be decided by the Supreme Court",
            "That the Single Judge gave a dissenting opinion",
            "That the matter relates to family partition"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 109 CPC (harmonized with Article 133(1)) provides that an appeal lies to the Supreme Court if the High Court certifies: (i) that the case involves a substantial question of law of general importance; and (ii) that in the opinion of the High Court the said question needs to be decided by the Supreme Court.",
        "optionBreakdown": {
            "A": "Incorrect; monetary valuation test was deleted by the 30th Constitutional Amendment (1972).",
            "B": "Correct; Section 109 requires a certificate of a substantial question of law of general importance requiring SC determination.",
            "C": "Incorrect; dissent does not automatically grant a certificate.",
            "D": "Incorrect; nature of property is irrelevant to constitutional certification."
        },
        "difficulty": "Important",
        "provision": "Section 109 CPC & Art 133",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Know the certification requirements for civil appeals to the Supreme Court under Section 109."
    }
]

questions_ch17 = [
    {
        "id": "mcq-cpc-17-001",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-17",
        "topicId": "top-cpc-17-01",
        "question": "Under Section 113 of the CPC, which court may state a case and refer the same for the opinion of the High Court?",
        "options": [
            "Only the District Judge",
            "Subject to conditions, any court subordinate to the High Court",
            "Only a Court of Small Causes",
            "Only an administrative tribunal"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 113 CPC provides that subject to such conditions and limitations as may be prescribed, any Court may state a case and refer the same for the opinion of the High Court, and the High Court may make such order thereon as it thinks fit.",
        "optionBreakdown": {
            "A": "Incorrect; any subordinate court (including Civil Judge Junior/Senior Division) can refer.",
            "B": "Correct; Section 113 empowers any court to state a case subject to prescribed conditions.",
            "C": "Incorrect; Small Cause Courts have specific reference powers under Order XLVI Rule 1, but S. 113 applies to all courts.",
            "D": "Incorrect; CPC governs civil courts, not general administrative tribunals."
        },
        "difficulty": "Standard",
        "provision": "Section 113 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Understand the general scope of Reference under Section 113 of the CPC."
    },
    {
        "id": "mcq-cpc-17-002",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-17",
        "topicId": "top-cpc-17-01",
        "question": "Under the Proviso to Section 113 of the CPC, reference to the High Court is MANDATORY when a case pending before a court involves a question as to the validity of:",
        "options": [
            "Any custom or usage having the force of law",
            "Any Act, Ordinance or Regulation or of any provision thereof, which the court considers invalid or inoperative, but has not been so declared by that High Court or the Supreme Court",
            "Any decree passed by a foreign court",
            "Any compromise recorded under Order XXIII Rule 3"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "The Proviso to Section 113 makes reference mandatory where the case involves a question as to validity of any Act, Ordinance or Regulation (or provision), determination of which is necessary, and the court is of opinion that it is invalid or inoperative, but it has not been declared so by that High Court or the Supreme Court.",
        "optionBreakdown": {
            "A": "Incorrect; validity of custom is not governed by the mandatory proviso to Section 113.",
            "B": "Correct; Proviso to Section 113 mandates reference on the constitutionality/validity of an Act, Ordinance, or Regulation.",
            "C": "Incorrect; foreign decrees are governed by Section 13 and 44A.",
            "D": "Incorrect; compromise decrees are challenged under Order XXIII Rule 3A."
        },
        "difficulty": "Important",
        "provision": "Proviso to Section 113 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Master the mandatory reference rule concerning legislative validity under the Proviso to Section 113."
    },
    {
        "id": "mcq-cpc-17-003",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-17",
        "topicId": "top-cpc-17-01",
        "question": "Can a reference under Order XLVI Rule 1 of the CPC be made on a question of fact?",
        "options": [
            "Yes, whenever the subordinate court is unable to weigh evidence",
            "No, reference under Order XLVI Rule 1 can only be made on a question of law or usage having the force of law",
            "Yes, but only with the consent of both litigating parties",
            "Yes, if the valuation of the suit exceeds rupees ten lakhs"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Order XLVI Rule 1 specifies that a reference can be made only where there arises 'any question of law or usage having the force of law' on which the court entertains reasonable doubt. Questions of fact can never be referred.",
        "optionBreakdown": {
            "A": "Incorrect; weighing evidence is exclusively within the trial/appellate court's jurisdiction.",
            "B": "Correct; Order XLVI Rule 1 strictly restricts reference to questions of law or usage having the force of law.",
            "C": "Incorrect; consent cannot expand reference to factual disputes.",
            "D": "Incorrect; valuation is irrelevant."
        },
        "difficulty": "Standard",
        "provision": "Order XLVI Rule 1 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Understand that reference lies only on questions of law or usage, never on questions of fact."
    },
    {
        "id": "mcq-cpc-17-004",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-17",
        "topicId": "top-cpc-17-01",
        "question": "Under Order XLVI Rule 1 of the CPC, reference can be made only in a suit or execution proceeding in which:",
        "options": [
            "The decree is appealable to the High Court",
            "The decree is not subject to appeal, or in the execution of any decree from which no appeal lies",
            "A revision has already been dismissed by the High Court",
            "The plaintiff is an indigent person"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Order XLVI Rule 1 provides that a reference lies before hearing or at any time before judgment in a suit or appeal in which the decree is not subject to appeal, or where no appeal lies in execution of such decree.",
        "optionBreakdown": {
            "A": "Incorrect; where an appeal lies, the remedy is appeal, not reference.",
            "B": "Correct; Order XLVI Rule 1 requires that the decree or order must not be subject to an appeal.",
            "C": "Incorrect; dismissal of revision has nothing to do with reference prerequisites.",
            "D": "Incorrect; indigency is governed by Order XXXIII."
        },
        "difficulty": "Important",
        "provision": "Order XLVI Rule 1 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Recognize that non-appealability is a fundamental condition for reference under Order XLVI Rule 1."
    },
    {
        "id": "mcq-cpc-17-005",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-17",
        "topicId": "top-cpc-17-01",
        "question": "Can a private party directly apply to the High Court for a Reference under Section 113 of the CPC?",
        "options": [
            "Yes, any citizen has an absolute fundamental right to seek a reference",
            "No, reference is a power of the subordinate court to seek the High Court's opinion; a party cannot move the High Court directly for reference",
            "Yes, by filing an interlocutory application in the High Court Registry",
            "Yes, if the subordinate judge refuses to grant an adjournment"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Reference is a consultative proceeding between the subordinate court and the High Court. A party may invite the subordinate court to make a reference, but cannot move the High Court directly for a reference under Section 113.",
        "optionBreakdown": {
            "A": "Incorrect; there is no direct right for private parties to refer matters to High Court under S. 113.",
            "B": "Correct; reference is consultative and can only be made by the subordinate court to the High Court.",
            "C": "Incorrect; High Court Registry cannot entertain a direct reference petition from a litigant.",
            "D": "Incorrect; refusal of adjournment is not a ground for reference."
        },
        "difficulty": "Important",
        "provision": "Section 113 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Distinguish between consultative reference by courts and remedies invoked by private parties."
    },
    {
        "id": "mcq-cpc-17-006",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-17",
        "topicId": "top-cpc-17-01",
        "question": "Under Order XLVI Rule 2 of the CPC, what may the subordinate court do pending the decision of the High Court on a reference?",
        "options": [
            "Mandatorily dismiss the suit immediately",
            "Either stay the proceedings or pass a decree or order contingent upon the decision of the High Court on the point referred",
            "Transfer the suit to another State",
            "Issue non-bailable warrants against the defendant"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Order XLVI Rule 2 provides that the Court may either stay the proceedings or pass a decree or make an order contingent upon the decision of the High Court on the point referred; but no decree or order shall be executed until receipt of a copy of the judgment of the High Court.",
        "optionBreakdown": {
            "A": "Incorrect; dismissing the suit would defeat the purpose of the reference.",
            "B": "Correct; Order XLVI Rule 2 allows either staying proceedings or passing a contingent decree/order.",
            "C": "Incorrect; transfer to another State is within Supreme Court powers under Section 25.",
            "D": "Incorrect; warrants have no connection with reference."
        },
        "difficulty": "Standard",
        "provision": "Order XLVI Rule 2 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Know the procedural options of stay or contingent decree pending reference under Order XLVI Rule 2."
    },
    {
        "id": "mcq-cpc-17-007",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-17",
        "topicId": "top-cpc-17-01",
        "question": "What is the binding nature of the High Court's decision on a reference under Order XLVI Rule 3 of the CPC?",
        "options": [
            "It is merely an academic advisory opinion which the subordinate court can disregard",
            "The High Court decides the question and transmits a copy of its judgment, and the subordinate court shall dispose of the case in conformity with the decision of the High Court",
            "The subordinate judge can refer the same question again to the Supreme Court if dissatisfied",
            "It only binds the parties if they execute a bond"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Order XLVI Rule 3 states that the High Court, after hearing the parties if they appear, shall decide the point and transmit a copy of its judgment, and the Court shall dispose of the case in conformity with the decision of the High Court.",
        "optionBreakdown": {
            "A": "Incorrect; the decision on reference is binding on the subordinate court.",
            "B": "Correct; Order XLVI Rule 3 mandates disposal of the case in strict conformity with the High Court decision.",
            "C": "Incorrect; subordinate judge cannot refer matters to Supreme Court.",
            "D": "Incorrect; binding effect is statutory, not contractual."
        },
        "difficulty": "Standard",
        "provision": "Order XLVI Rule 3 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Understand the binding and authoritative effect of the High Court's opinion under Order XLVI Rule 3."
    },
    {
        "id": "mcq-cpc-17-008",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-17",
        "topicId": "top-cpc-17-02",
        "question": "Under Section 114 and Order XLVII Rule 1 of the CPC, which court has jurisdiction to review a decree or order?",
        "options": [
            "Only the High Court",
            "The very court which passed the decree or made the order",
            "The immediate appellate court",
            "The District Court exclusively"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Review is a reconsideration of the judgment by the same court and by the same judge (or successor) which pronounced the decree or made the order. Section 114 provides that an aggrieved person may apply for review to the Court which passed the decree or made the order.",
        "optionBreakdown": {
            "A": "Incorrect; review is not restricted to the High Court; any court can review its own decision.",
            "B": "Correct; review lies to the court which passed the decree or made the order.",
            "C": "Incorrect; reconsideration by a superior appellate court is an appeal or revision, not a review.",
            "D": "Incorrect; subordinate courts can review their own decrees."
        },
        "difficulty": "Standard",
        "provision": "Section 114 & Order XLVII Rule 1 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Recognize that review is exercised by the court that passed the decree or order."
    },
    {
        "id": "mcq-cpc-17-009",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-17",
        "topicId": "top-cpc-17-02",
        "question": "Which of the following is NOT a permissible ground for review under Order XLVII Rule 1 of the CPC?",
        "options": [
            "Discovery of new and important matter or evidence which, after exercise of due diligence, was not within the applicant's knowledge",
            "Mistake or error apparent on the face of the record",
            "Desire to re-argue the case on merits because the previous advocate did not argue effectively",
            "Any other sufficient reason (analogous to the other grounds)"
        ],
        "answer": 2,
        "answerLetter": "C",
        "explanation": "Review is not an appeal in disguise. A party cannot seek review merely to re-argue the case or because the advocate failed to present certain arguments. As held in Parsion Devi v. Sumitri Devi, an error apparent on the face of record must be striking and self-evident, not requiring an elaborate process of reasoning.",
        "optionBreakdown": {
            "A": "Incorrect; statutory ground under Order XLVII Rule 1(1).",
            "B": "Incorrect; statutory ground under Order XLVII Rule 1(1).",
            "C": "Correct; re-arguing on merits is strictly impermissible in a review petition.",
            "D": "Incorrect; 'any other sufficient reason' is a recognized statutory ground, interpreted as ejusdem generis."
        },
        "difficulty": "Important",
        "provision": "Order XLVII Rule 1 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Distinguish between legitimate grounds of review and an impermissible 'appeal in disguise'."
    },
    {
        "id": "mcq-cpc-17-010",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-17",
        "topicId": "top-cpc-17-02",
        "question": "According to the Explanation to Order XLVII Rule 1 of the CPC (inserted by 1976 Amendment), the fact that the decision on a question of law on which the judgment of the court is based has been reversed or modified by the subsequent decision of a superior court:",
        "options": [
            "Is a mandatory ground for reviewing the earlier judgment",
            "Shall not be a ground for the review of such judgment",
            "Automatically annuls the earlier decree",
            "Requires payment of double court fees for review"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "The Explanation to Order XLVII Rule 1 explicitly states: 'The fact that the decision on a question of law on which the judgment of the Court is based has been reversed or modified by the subsequent decision of a superior Court shall not be a ground for the review of such judgment.'",
        "optionBreakdown": {
            "A": "Incorrect; the Explanation expressly prohibits this as a ground.",
            "B": "Correct; subsequent reversal of law by a superior court is NOT a valid ground for review under the Explanation.",
            "C": "Incorrect; past final judgments between parties remain res judicata.",
            "D": "Incorrect; fee structure has nothing to do with maintainability."
        },
        "difficulty": "Advanced",
        "provision": "Explanation to Order XLVII Rule 1 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Master the Explanation to Order XLVII Rule 1 barring review on subsequent reversal of legal precedent."
    },
    {
        "id": "mcq-cpc-17-011",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-17",
        "topicId": "top-cpc-17-02",
        "question": "Can an application for review be entertained if an appeal has already been preferred against the decree or order and is pending?",
        "options": [
            "Yes, review and appeal can proceed simultaneously in different courts",
            "No, under Section 114 and Order XLVII Rule 1, review lies from a decree or order from which an appeal is allowed, but from which 'no appeal has been preferred'",
            "Yes, if the appellant deposits half the decretal amount",
            "Yes, with the permission of the Supreme Court"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Order XLVII Rule 1(1)(a) provides that an application for review lies from a decree or order from which an appeal is allowed by the Code, but 'from which no appeal has been preferred'. Once an appeal is preferred and pending, review is barred.",
        "optionBreakdown": {
            "A": "Incorrect; simultaneous appeal and review by the same party is impermissible.",
            "B": "Correct; Order XLVII Rule 1 bars review if an appeal has already been preferred by the applicant.",
            "C": "Incorrect; monetary deposit cannot confer jurisdiction barred by statute.",
            "D": "Incorrect; Supreme Court permission is not contemplated under O. XLVII."
        },
        "difficulty": "Important",
        "provision": "Order XLVII Rule 1(1)(a) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Understand the statutory bar on review when an appeal has already been preferred."
    },
    {
        "id": "mcq-cpc-17-012",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-17",
        "topicId": "top-cpc-17-02",
        "question": "Under Order XLVII Rule 7 of the CPC, what is the remedy against an order REJECTING an application for review?",
        "options": [
            "An appeal lies as of right under Order XLIII Rule 1",
            "No appeal lies against an order rejecting an application for review",
            "A second review application lies automatically",
            "A reference lies to the High Court"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Order XLVII Rule 7(1) explicitly provides: 'An order of the Court rejecting the application shall not be appealable.' However, an order granting an application may be objected to under Order XLVII Rule 7(1)(a)-(c).",
        "optionBreakdown": {
            "A": "Incorrect; Order XLVII Rule 7(1) explicitly bars an appeal against an order of rejection.",
            "B": "Correct; an order rejecting a review petition is completely non-appealable.",
            "C": "Incorrect; Order XLVII Rule 9 expressly bars a second review application.",
            "D": "Incorrect; reference does not lie against rejection of review."
        },
        "difficulty": "Standard",
        "provision": "Order XLVII Rule 7(1) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Know that an order rejecting a review application is non-appealable under Order XLVII Rule 7."
    },
    {
        "id": "mcq-cpc-17-013",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-17",
        "topicId": "top-cpc-17-02",
        "question": "Can a second application for review of an order passed on a review be made under Order XLVII Rule 9 of the CPC?",
        "options": [
            "Yes, if fresh grounds are discovered",
            "No, Order XLVII Rule 9 categorically bars any application to review an order made on an application for a review",
            "Yes, with the prior sanction of the Advocate General",
            "Yes, if the Single Judge has retired"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Order XLVII Rule 9 CPC enacts an absolute prohibition: 'No application to review an order made on an application for a review or a decree or order passed, or made on a review, shall be entertained.'",
        "optionBreakdown": {
            "A": "Incorrect; Order XLVII Rule 9 contains no exception for fresh grounds.",
            "B": "Correct; Order XLVII Rule 9 creates an absolute bar against a review of a review.",
            "C": "Incorrect; Advocate General has no sanctioning power here.",
            "D": "Incorrect; retirement of a judge does not permit second review."
        },
        "difficulty": "Standard",
        "provision": "Order XLVII Rule 9 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Recall the absolute bar against a second review application under Order XLVII Rule 9."
    },
    {
        "id": "mcq-cpc-17-014",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-17",
        "topicId": "top-cpc-17-02",
        "question": "What is meant by an 'error apparent on the face of the record' for the purposes of review?",
        "options": [
            "An error which can be established by a lengthy and complicated process of reasoning on points where there may conceivably be two opinions",
            "A self-evident error that is manifest and strikes one on mere looking at the record, without requiring elaborate arguments",
            "Any disagreement with the judge's assessment of oral witness demeanor",
            "An error relating exclusively to grammatical syntax in the decree"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "As repeatedly held by the Supreme Court (e.g. Hari Vishnu Kamath, Parsion Devi), an error apparent on the face of the record is one which is patent, manifest and self-evident. An error which has to be established by an elaborate process of reasoning cannot be said to be an error apparent on the face of the record.",
        "optionBreakdown": {
            "A": "Incorrect; if elaborate reasoning is needed, it falls outside review jurisdiction.",
            "B": "Correct; an error apparent is manifest, striking, and does not require complex reasoning.",
            "C": "Incorrect; witness demeanor appreciation is an appellate question, not reviewable.",
            "D": "Incorrect; clerical/grammatical errors are corrected under Section 152, not via review."
        },
        "difficulty": "Important",
        "provision": "Order XLVII Rule 1 CPC Precedent",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Define the judicial test of 'error apparent on the face of the record'."
    },
    {
        "id": "mcq-cpc-17-015",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-17",
        "topicId": "top-cpc-17-03",
        "question": "Under Section 115(1) of the CPC, the High Court may call for the record of any case which has been decided by any court subordinate to it, in which:",
        "options": [
            "An appeal lies to the High Court",
            "No appeal lies thereto",
            "An appeal has been dismissed as time-barred",
            "The suit was valued below Rs. 500"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 115(1) CPC provides: 'The High Court may call for the record of any case which has been decided by any Court subordinate to such High Court and in which no appeal lies thereto...'",
        "optionBreakdown": {
            "A": "Incorrect; if an appeal lies to the High Court, revision under Section 115 is strictly barred.",
            "B": "Correct; Section 115 explicitly requires that 'no appeal lies thereto'.",
            "C": "Incorrect; dismissal of appeal does not convert it into a revision prerequisite.",
            "D": "Incorrect; valuation below Rs. 500 is not the statutory condition."
        },
        "difficulty": "Standard",
        "provision": "Section 115(1) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Identify non-appealability as an essential prerequisite for revisional jurisdiction under Section 115."
    },
    {
        "id": "mcq-cpc-17-016",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-17",
        "topicId": "top-cpc-17-03",
        "question": "Which of the following jurisdictional grounds is enumerated under clauses (a), (b), and (c) of Section 115(1) of the CPC?",
        "options": [
            "Subordinate court has exercised a jurisdiction not vested in it by law",
            "Subordinate court has failed to exercise a jurisdiction so vested",
            "Subordinate court has acted in the exercise of its jurisdiction illegally or with material irregularity",
            "All of the above"
        ],
        "answer": 3,
        "answerLetter": "D",
        "explanation": "Section 115(1) provides three specific jurisdictional grounds: (a) exercised a jurisdiction not vested in it by law; (b) failed to exercise a jurisdiction so vested; or (c) acted in the exercise of its jurisdiction illegally or with material irregularity.",
        "optionBreakdown": {
            "A": "Partially correct; clause (a) contains this ground.",
            "B": "Partially correct; clause (b) contains this ground.",
            "C": "Partially correct; clause (c) contains this ground.",
            "D": "Correct; all three grounds (a), (b), and (c) are the complete statutory criteria of Section 115(1)."
        },
        "difficulty": "Standard",
        "provision": "Section 115(1)(a)-(c) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Recall the three jurisdictional grounds for revision under Section 115(1)."
    },
    {
        "id": "mcq-cpc-17-017",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-17",
        "topicId": "top-cpc-17-03",
        "question": "Under the Proviso to Section 115(1) of the CPC (as substituted by the 1999/2002 Amendment), the High Court shall NOT vary or reverse any order made, or any order deciding an issue, in the course of a suit or other proceeding, EXCEPT where:",
        "options": [
            "The applicant is willing to pay costs of both sides",
            "The order, if it had been made in favour of the party applying for revision, would have finally disposed of the suit or other proceedings",
            "The order causes mental distress to the plaintiff",
            "The suit has been pending for more than five years"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "The Proviso to Section 115(1) restricts revision against interlocutory orders: 'Provided that the High Court shall not, under this section, vary or reverse any order made... except where the order, if it had been made in favour of the party applying for revision, would have finally disposed of the suit or other proceedings.' (Shiv Shakti Coop. Housing Society v. Swaraj Developers).",
        "optionBreakdown": {
            "A": "Incorrect; costs cannot satisfy the statutory test of final disposal.",
            "B": "Correct; the Proviso permits revision only if reversal would have finally disposed of the suit/proceedings.",
            "C": "Incorrect; subjective distress is irrelevant.",
            "D": "Incorrect; pendency duration does not confer revisional jurisdiction."
        },
        "difficulty": "Important",
        "provision": "Proviso to Section 115(1) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Master the restrictive test for revision against interlocutory orders under the Proviso to Section 115(1)."
    },
    {
        "id": "mcq-cpc-17-018",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-17",
        "topicId": "top-cpc-17-03",
        "question": "Under Section 115(2) of the CPC, what is the effect of an order or decree being appealable to the High Court or to any subordinate court?",
        "options": [
            "The High Court can still convert the revision into an appeal",
            "The High Court shall not, under this section, vary or reverse any decree or order against which an appeal lies either to the High Court or to any court subordinate thereto",
            "The High Court must stay the revision indefinitely",
            "The High Court can award exemplary damages against the respondent"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 115(2) CPC provides: 'The High Court shall not, under this section, vary or reverse any decree or order against which an appeal lies either to the High Court or to any Court subordinate thereto.' This establishes that revision is completely barred if an appeal lies to ANY court.",
        "optionBreakdown": {
            "A": "Incorrect; Section 115(2) creates a direct statutory prohibition.",
            "B": "Correct; Section 115(2) bars revision where an appeal lies either to the High Court or to any subordinate court.",
            "C": "Incorrect; stay is not the remedy; dismissal is required.",
            "D": "Incorrect; damages are not part of Section 115(2)."
        },
        "difficulty": "Important",
        "provision": "Section 115(2) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Understand the comprehensive bar on revision where an appeal lies to any court under Section 115(2)."
    },
    {
        "id": "mcq-cpc-17-019",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-17",
        "topicId": "top-cpc-17-03",
        "question": "Under Section 115(3) of the CPC, does the mere filing of a revision operate as a stay of suit or other proceeding before the subordinate court?",
        "options": [
            "Yes, filing of revision creates an automatic statutory stay of all proceedings",
            "A revision shall not operate as a stay of suit or other proceeding before the Court except where such suit or other proceeding is stayed by the High Court",
            "It operates as a stay only for a period of thirty days",
            "It operates as a stay only if the applicant is the defendant"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 115(3) CPC explicitly provides: 'A revision shall not operate as a stay of suit or other proceeding before the Court except where such suit or other proceeding is stayed by the High Court.'",
        "optionBreakdown": {
            "A": "Incorrect; there is no automatic stay upon filing a revision.",
            "B": "Correct; Section 115(3) mandates that revision does not operate as a stay unless expressly granted by the High Court.",
            "C": "Incorrect; no automatic 30-day stay exists.",
            "D": "Incorrect; status of applicant does not create an automatic stay."
        },
        "difficulty": "Standard",
        "provision": "Section 115(3) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Know that revision does not operate as an automatic stay under Section 115(3)."
    },
    {
        "id": "mcq-cpc-17-020",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-17",
        "topicId": "top-cpc-17-03",
        "question": "How does supervisory jurisdiction under Article 227 of the Constitution differ from revisional jurisdiction under Section 115 of the CPC, as clarified in Surya Dev Rai v. Ram Chander Rai (2003)?",
        "options": [
            "Article 227 can be used as a routine second appeal on facts",
            "Revisional power under Section 115 is subject to statutory limitations and amendments of the CPC, whereas supervisory jurisdiction under Article 227 is a constitutional power that cannot be curtailed by CPC amendments, though exercised sparingly to keep courts within bounds of authority",
            "Section 115 applies to High Courts, while Article 227 applies only to District Judges",
            "There is no difference between Article 227 and Section 115"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "In Surya Dev Rai, the Supreme Court held that the curtailment of Section 115 CPC by the 1999 Amendment does not take away or whittle down the constitutional supervisory jurisdiction of High Courts under Article 227. However, Article 227 is exercised sparingly to rectify grave errors of jurisdiction or gross failure of justice, not as an appellate court.",
        "optionBreakdown": {
            "A": "Incorrect; Article 227 is never a routine appeal on facts.",
            "B": "Correct; Surya Dev Rai clarified the constitutional primacy of Article 227 vis-a-vis statutory restrictions of Section 115.",
            "C": "Incorrect; Article 227 is the High Court's superintendence over all subordinate courts and tribunals.",
            "D": "Incorrect; they stem from distinct constitutional and statutory foundations."
        },
        "difficulty": "Advanced",
        "provision": "Section 115 CPC & Art 227 Precedent",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Analyze the interplay between Section 115 CPC revision and Article 227 supervisory jurisdiction."
    }
]

questions_ch18 = [
    {
        "id": "mcq-cpc-18-001",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-18",
        "topicId": "top-cpc-18-01",
        "question": "Under Section 89(1) of the CPC, which of the following is NOT one of the four statutory Alternative Dispute Resolution (ADR) modes to which a court may refer a dispute?",
        "options": [
            "Arbitration or Conciliation",
            "Lok Adalat",
            "Mediation",
            "Police Investigation"
        ],
        "answer": 3,
        "answerLetter": "D",
        "explanation": "Section 89(1) lists four ADR processes: (a) arbitration, (b) conciliation, (c) judicial settlement including settlement through Lok Adalat, and (d) mediation. Police investigation is a criminal procedural step, not a civil ADR mechanism.",
        "optionBreakdown": {
            "A": "Incorrect; arbitration and conciliation are statutory modes under S. 89(1)(a) & (b).",
            "B": "Incorrect; Lok Adalat is a statutory mode under S. 89(1)(c).",
            "C": "Incorrect; mediation is a statutory mode under S. 89(1)(d).",
            "D": "Correct; police investigation is not an ADR mode under Section 89."
        },
        "difficulty": "Standard",
        "provision": "Section 89(1) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Identify the four recognized ADR modes under Section 89(1) of the CPC."
    },
    {
        "id": "mcq-cpc-18-002",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-18",
        "topicId": "top-cpc-18-01",
        "question": "In the landmark judgment Afcons Infrastructure Ltd. v. Cherian Varkey Construction Co. (P) Ltd. (2010), what did the Supreme Court hold regarding reference to arbitration under Section 89?",
        "options": [
            "The court can compulsorily force parties into arbitration without their mutual consent",
            "Reference to arbitration under Section 89 can only be made with the mutual consent of all litigating parties",
            "Arbitration can only be ordered if the dispute exceeds Rs. 10 crores",
            "Arbitration is prohibited in all civil suits"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "In Afcons, the Supreme Court clarified drafting anomalies in Section 89 and held that for arbitration or conciliation, mutual consent of all parties is mandatory. However, for mediation, Lok Adalat, or judicial settlement, the court can refer parties even without consent if elements of settlement exist.",
        "optionBreakdown": {
            "A": "Incorrect; Afcons explicitly prohibited forcing parties into binding arbitration without consent.",
            "B": "Correct; Afcons established that reference to arbitration under S. 89 requires mutual consent of all parties.",
            "C": "Incorrect; monetary limit was not prescribed.",
            "D": "Incorrect; arbitration is permitted when agreed upon."
        },
        "difficulty": "Important",
        "provision": "Section 89 CPC Precedent",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Master the consent requirement for arbitration under Section 89 as established in Afcons."
    },
    {
        "id": "mcq-cpc-18-003",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-18",
        "topicId": "top-cpc-18-01",
        "question": "Which category of civil suits was held by the Supreme Court in Afcons to be normally UNFIT for ADR reference under Section 89?",
        "options": [
            "Commercial disputes and partnership dissolutions",
            "Representative suits under Order I Rule 8, suits involving public interest, or allegations of serious fraud and forgery",
            "Matrimonial disputes and maintenance claims",
            "Partition suits between family members"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "In Afcons, the Supreme Court listed categories of suits unsuitable for ADR: representative suits under Order I Rule 8 involving public interest, disputes involving serious fraud, fabrication of documents, forgery, constitutional interpretations, and prosecution for criminal offences.",
        "optionBreakdown": {
            "A": "Incorrect; commercial disputes are prime candidates for ADR.",
            "B": "Correct; representative suits, fraud, and public interest matters are unsuitable for ADR.",
            "C": "Incorrect; matrimonial disputes are ideal for mediation.",
            "D": "Incorrect; family partitions are encouraged to be resolved via ADR."
        },
        "difficulty": "Important",
        "provision": "Section 89 CPC Precedent",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Distinguish between suits suitable and unsuitable for ADR under the Afcons guidelines."
    },
    {
        "id": "mcq-cpc-18-004",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-18",
        "topicId": "top-cpc-18-01",
        "question": "Under Order X Rule 1A of the CPC, at what stage of the suit is the court required to direct parties to opt for any of the ADR modes specified in Section 89(1)?",
        "options": [
            "Before the summons is issued to the defendant",
            "At the first hearing of the suit, after recording admissions and denials under Rule 1",
            "Only after the entire evidence of both parties is concluded",
            "In execution proceedings only"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Order X Rule 1A provides that at the first hearing of the suit, the Court shall ascertain whether the parties admit or deny allegations of fact, and thereafter the Court shall direct the parties to the suit to opt for either mode of settlement specified under Section 89(1).",
        "optionBreakdown": {
            "A": "Incorrect; summons must be served and parties present before Rule 1A operates.",
            "B": "Correct; Order X Rule 1A mandates ADR direction at the first hearing after admissions/denials.",
            "C": "Incorrect; ADR is intended to avoid lengthy trial, not wait until evidence concludes.",
            "D": "Incorrect; Order X operates during trial/first hearing."
        },
        "difficulty": "Standard",
        "provision": "Order X Rule 1A CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Know the precise procedural stage for ADR direction under Order X Rule 1A."
    },
    {
        "id": "mcq-cpc-18-005",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-18",
        "topicId": "top-cpc-18-01",
        "question": "What is the consequence if the conciliation or mediation process referred under Section 89 fails to arrive at a settlement, pursuant to Order X Rule 1C?",
        "options": [
            "The suit is dismissed for non-prosecution",
            "The presiding officer of the ADR forum imposes a fine on the resisting party",
            "The suit shall proceed from the stage at which it was referred, before the court which referred it",
            "The parties are debarred from leading oral evidence"
        ],
        "answer": 2,
        "answerLetter": "C",
        "explanation": "Order X Rule 1C provides that where a suit is referred under Rule 1A and the presiding officer of the conciliation/mediation forum certifies that it is not in the interest of justice to proceed, the suit shall proceed before the Court which referred it from the stage it was referred.",
        "optionBreakdown": {
            "A": "Incorrect; failure of ADR does not result in dismissal of the suit.",
            "B": "Incorrect; ADR conciliators/mediators have no penal powers to fine parties for failure to settle.",
            "C": "Correct; under Order X Rule 1C, the suit returns to the referring court and proceeds on merits.",
            "D": "Incorrect; trial rights remain fully intact."
        },
        "difficulty": "Standard",
        "provision": "Order X Rule 1C CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Understand the procedural restoration of the suit upon failure of ADR under Order X Rule 1C."
    },
    {
        "id": "mcq-cpc-18-006",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-18",
        "topicId": "top-cpc-18-01",
        "question": "When a civil suit is settled through any ADR mechanism under Section 89 of the CPC, what relief is available to the plaintiff regarding court fees under Section 16 of the Court Fees Act, 1870?",
        "options": [
            "No refund is permissible under any circumstances",
            "The plaintiff is entitled to receive a certificate from the court authorizing full refund of court fees paid on the plaint",
            "Only 10% of court fees can be refunded",
            "Refund is granted only if the defendant pays an equivalent sum"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 16 of the Court Fees Act, 1870 (inserted by 1999 CPC Amendment Act) mandates that where the Court refers the parties under Section 89, the plaintiff shall be entitled to receive from the Court a certificate authorizing him to receive back from the Collector the full amount of fee paid in respect of such plaint.",
        "optionBreakdown": {
            "A": "Incorrect; Section 16 expressly mandates refund.",
            "B": "Correct; full refund of court fees is statutory under Section 16 of the Court Fees Act.",
            "C": "Incorrect; 10% is not the statutory refund amount.",
            "D": "Incorrect; refund is paid by the State exchequer, not by the defendant."
        },
        "difficulty": "Important",
        "provision": "Section 89 CPC & S. 16 Court Fees Act",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Recognize the statutory entitlement to full refund of court fees upon settlement under Section 89."
    },
    {
        "id": "mcq-cpc-18-007",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-18",
        "topicId": "top-cpc-18-01",
        "question": "Under Section 89(2)(d) of the CPC, where a dispute is referred to mediation, which rules govern the procedure?",
        "options": [
            "Arbitration and Conciliation Act, 1996 exclusively",
            "The court shall effect a compromise between the parties and follow such procedure as may be prescribed (High Court Mediation Rules)",
            "The Code of Criminal Procedure",
            "The Indian Evidence Act strictly"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 89(2)(d) provides that where a dispute is referred to mediation, the Court shall effect a compromise between the parties and shall follow such procedure as may be prescribed under the Civil Procedure ADR and Mediation Rules framed by the respective High Court.",
        "optionBreakdown": {
            "A": "Incorrect; Arbitration Act applies to arbitration and conciliation under clauses (a) and (b), not mediation.",
            "B": "Correct; mediation is governed by Section 89(2)(d) and High Court Mediation Rules.",
            "C": "Incorrect; CrPC has no application to civil mediation.",
            "D": "Incorrect; Evidence Act does not strictly bind informal mediation proceedings."
        },
        "difficulty": "Important",
        "provision": "Section 89(2)(d) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Identify the procedural framework governing court-referred mediation under Section 89(2)(d)."
    },
    {
        "id": "mcq-cpc-18-008",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-18",
        "topicId": "top-cpc-18-02",
        "question": "Under Section 75 of the CPC, for which of the following purposes may a civil court issue a commission?",
        "options": [
            "To examine any person, to make a local investigation, or to examine or adjust accounts",
            "To make a partition, to hold a scientific, technical or expert investigation",
            "To conduct sale of property or perform ministerial acts",
            "All of the above"
        ],
        "answer": 3,
        "answerLetter": "D",
        "explanation": "Section 75 CPC empowers courts to issue commissions for: (a) examining any person; (b) local investigation; (c) examining or adjusting accounts; (d) making a partition; (e) scientific/technical/expert investigation; (f) conduct of sale of movable property; and (g) performing ministerial acts.",
        "optionBreakdown": {
            "A": "Partially correct; covered under clauses (a), (b), (c).",
            "B": "Partially correct; covered under clauses (d) and (e).",
            "C": "Partially correct; covered under clauses (f) and (g).",
            "D": "Correct; all these purposes are comprehensively covered under Section 75(a) to (g)."
        },
        "difficulty": "Standard",
        "provision": "Section 75 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Enumerate the statutory purposes for which a commission can be issued under Section 75."
    },
    {
        "id": "mcq-cpc-18-009",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-18",
        "topicId": "top-cpc-18-02",
        "question": "Can a commission for local investigation under Order XXVI Rule 9 of the CPC be issued to collect evidence or determine which party is in actual possession of disputed property?",
        "options": [
            "Yes, collecting evidence is the primary purpose of a local commission",
            "No, the court cannot appoint a commissioner to collect evidence for a party or to investigate who is in physical possession, which must be proved by parties through independent evidence",
            "Yes, if the plaintiff pays double commissioner fees",
            "Yes, but only in suits valued over Rs. 50,000"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "It is settled law that a commission under Order XXVI Rule 9 cannot be issued to collect evidence for a party or to fish out evidence, nor can a commissioner be appointed to ascertain actual physical possession of a party. The purpose of local investigation is to elucidate any matter in dispute or ascertain market value, damages, etc.",
        "optionBreakdown": {
            "A": "Incorrect; appointing a commissioner to collect evidence is an abuse of process.",
            "B": "Correct; Order XXVI Rule 9 cannot be utilized to delegate the court's judicial function or collect evidence of possession.",
            "C": "Incorrect; fee payment cannot cure jurisdictional illegality.",
            "D": "Incorrect; valuation does not alter this fundamental principle."
        },
        "difficulty": "Important",
        "provision": "Order XXVI Rule 9 CPC Precedent",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Master the prohibition against appointing a commissioner to collect evidence or determine possession."
    },
    {
        "id": "mcq-cpc-18-010",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-18",
        "topicId": "top-cpc-18-02",
        "question": "What is the evidentiary status of the report of a Commissioner and evidence taken by him under Order XXVI Rule 10(2) of the CPC?",
        "options": [
            "It is conclusive proof and cannot be questioned by either party",
            "The report and evidence shall be evidence in the suit and form part of the record, but with permission of the court the commissioner may be examined personally",
            "It is completely inadmissible unless the Commissioner is first examined as an ordinary witness",
            "It has the status of an unverified hearsay affidavit"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Order XXVI Rule 10(2) CPC provides: 'The report of the Commissioner and the evidence taken by him (but not the evidence without the report) shall be evidence in the suit and shall form part of the record; but the Court or, with the permission of the Court, any of the parties to the suit may examine the Commissioner personally...'",
        "optionBreakdown": {
            "A": "Incorrect; commissioner's report is never conclusive proof.",
            "B": "Correct; Order XXVI Rule 10(2) makes the report evidence forming part of the record, subject to examination of commissioner.",
            "C": "Incorrect; formal proof by calling the commissioner is not mandatory unless challenged or directed by court.",
            "D": "Incorrect; it forms part of judicial record by statutory force."
        },
        "difficulty": "Important",
        "provision": "Order XXVI Rule 10(2) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Understand the evidentiary value and procedural status of a commissioner's report under Order XXVI Rule 10(2)."
    },
    {
        "id": "mcq-cpc-18-011",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-18",
        "topicId": "top-cpc-18-02",
        "question": "Under Order XXVI Rule 1 of the CPC, a court may issue a commission for the examination of any person on interrogatories or otherwise, if that person:",
        "options": [
            "Resides within the local limits of the court's jurisdiction and is completely healthy",
            "Resides beyond local limits of court's jurisdiction, or is about to leave jurisdiction, or is from sickness or infirmity unable to attend court",
            "Is the advocate representing the plaintiff",
            "Refuses to sign the summons"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Order XXVI Rule 1 enables courts to issue commissions for examination of any person resident within local limits who is from sickness or infirmity unable to attend court. Order XXVI Rule 4 provides for persons residing beyond local limits or about to leave.",
        "optionBreakdown": {
            "A": "Incorrect; healthy persons residing locally must attend court unless exempted.",
            "B": "Correct; sickness, infirmity, or residence beyond limits justify examination on commission under Order XXVI Rules 1 and 4.",
            "C": "Incorrect; advocates cannot be examined on commission as parties' witnesses regarding privileged matters.",
            "D": "Incorrect; refusal of summons leads to substituted service or default, not commission."
        },
        "difficulty": "Standard",
        "provision": "Order XXVI Rules 1 & 4 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Know the grounds for issuing a commission to examine witnesses under Order XXVI Rules 1 and 4."
    },
    {
        "id": "mcq-cpc-18-012",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-18",
        "topicId": "top-cpc-18-02",
        "question": "Under Order XXVI Rule 13 of the CPC, in a suit for partition of immovable property where a preliminary decree has been passed, the court may issue a commission to:",
        "options": [
            "Sell the property by public auction immediately without dividing it",
            "Such person as it thinks fit to make the partition or separation according to the rights declared in such decree",
            "The District Magistrate to seize the property",
            "Arbitrators without consent of parties"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Order XXVI Rule 13 provides that where a preliminary decree for partition has been passed, the Court may issue a commission to such person as it thinks fit to make the partition or separation according to the rights declared in such decree.",
        "optionBreakdown": {
            "A": "Incorrect; physical partition by metes and bounds is the first objective under Rule 13.",
            "B": "Correct; Order XXVI Rule 13 provides for appointment of a commissioner to make partition pursuant to the preliminary decree.",
            "C": "Incorrect; District Magistrate has role under S. 54 for revenue-paying lands, not under Rule 13.",
            "D": "Incorrect; court appoints a commissioner, not forced arbitration."
        },
        "difficulty": "Standard",
        "provision": "Order XXVI Rule 13 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Recall the procedure of issuing a commission for partition under Order XXVI Rule 13."
    },
    {
        "id": "mcq-cpc-18-013",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-18",
        "topicId": "top-cpc-18-02",
        "question": "Under Section 77 of the CPC, in lieu of issuing a commission, what instrument may the court issue to examine a witness residing at any place not within India?",
        "options": [
            "A Letter of Request",
            "A Red Corner Notice",
            "A Writ of Quo Warranto",
            "A Precept under Section 46"
        ],
        "answer": 0,
        "answerLetter": "A",
        "explanation": "Section 77 CPC explicitly provides: 'In lieu of issuing a commission, the Court may issue a letter of request to examine a witness at any place not within India.'",
        "optionBreakdown": {
            "A": "Correct; Section 77 provides for the issuance of a 'letter of request' for overseas witnesses.",
            "B": "Incorrect; Red Corner Notices are Interpol criminal instruments.",
            "C": "Incorrect; Quo Warranto is a constitutional writ under Article 32/226.",
            "D": "Incorrect; Precept under Section 46 attaches property across domestic courts."
        },
        "difficulty": "Standard",
        "provision": "Section 77 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Identify 'Letter of Request' as the statutory instrument under Section 77 for foreign witnesses."
    },
    {
        "id": "mcq-cpc-18-014",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-18",
        "topicId": "top-cpc-18-02",
        "question": "Under Order XXVI Rule 10A of the CPC (inserted by the 1976 Amendment), a commission may be issued for:",
        "options": [
            "Scientific investigation",
            "Arresting a defaulting judgment-debtor",
            "Conducting local elections",
            "Determining personal religious beliefs"
        ],
        "answer": 0,
        "answerLetter": "A",
        "explanation": "Order XXVI Rule 10A specifically provides for commissions for 'scientific investigation' where any question arising in a suit involves any scientific investigation which cannot, in the opinion of the Court, be conveniently conducted before the Court.",
        "optionBreakdown": {
            "A": "Correct; Order XXVI Rule 10A provides for commissions for scientific investigation.",
            "B": "Incorrect; arrest is executed by court officers/police, not scientific commissioners.",
            "C": "Incorrect; local elections are outside civil suit jurisdiction.",
            "D": "Incorrect; personal beliefs are not subject to scientific commissions."
        },
        "difficulty": "Standard",
        "provision": "Order XXVI Rule 10A CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Know the provision for scientific investigation commissions under Order XXVI Rule 10A."
    },
    {
        "id": "mcq-cpc-18-015",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-18",
        "topicId": "top-cpc-18-03",
        "question": "What is the foundational Latin maxim that underlies the Doctrine of Restitution embodied in Section 144 of the CPC?",
        "options": [
            "Actus curiae neminem gravabit (an act of the court shall prejudice no man)",
            "Ignorantia juris non excusat (ignorance of law is no excuse)",
            "Res judicata pro veritate accipitur (a matter adjudged is accepted as true)",
            "Ubi jus ibi remedium (where there is a right, there is a remedy)"
        ],
        "answer": 0,
        "answerLetter": "A",
        "explanation": "The doctrine of restitution under Section 144 is founded on the equitable maxim 'Actus curiae neminem gravabit'—an act of the court shall prejudice no man. The court has a duty to restore the party to the position they would have occupied but for the erroneous decree or order.",
        "optionBreakdown": {
            "A": "Correct; Actus curiae neminem gravabit is the cardinal maxim underpinning Section 144.",
            "B": "Incorrect; relates to legal ignorance, not restitution.",
            "C": "Incorrect; relates to finality of judgments under Section 11.",
            "D": "Incorrect; relates to general availability of remedies."
        },
        "difficulty": "Standard",
        "provision": "Section 144 CPC Maxim",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Associate the doctrine of restitution with the maxim 'Actus curiae neminem gravabit'."
    },
    {
        "id": "mcq-cpc-18-016",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-18",
        "topicId": "top-cpc-18-03",
        "question": "Under Section 144(1) of the CPC, which court has jurisdiction to grant restitution when a decree or order is varied or reversed?",
        "options": [
            "Only the Supreme Court of India",
            "The Court of first instance (trial court)",
            "The High Court exclusively in its revisional jurisdiction",
            "The District Magistrate"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 144(1) expressly enacts: '...the Court of first instance shall, on the application of any party entitled to any benefit by way of restitution or otherwise, cause such restitution to be made as will, so far as may be, place the parties in the position which they would have occupied but for such decree or order...'",
        "optionBreakdown": {
            "A": "Incorrect; Supreme Court is an appellate forum; application goes to trial court.",
            "B": "Correct; Section 144(1) explicitly vests restitution jurisdiction in the 'Court of first instance'.",
            "C": "Incorrect; revisional court reverses decrees, but restitution is carried out by the court of first instance.",
            "D": "Incorrect; revenue authorities have no civil restitution powers."
        },
        "difficulty": "Standard",
        "provision": "Section 144(1) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Recognize that restitution applications lie to the Court of first instance under Section 144(1)."
    },
    {
        "id": "mcq-cpc-18-017",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-18",
        "topicId": "top-cpc-18-03",
        "question": "What is the effect of Section 144(2) of the CPC on the institution of a separate suit for obtaining restitution?",
        "options": [
            "A separate suit is the mandatory regular remedy",
            "No suit shall be instituted for the purpose of obtaining any restitution or other relief which could be obtained by application under Section 144(1)",
            "A separate suit is optional and can be filed concurrently with the application",
            "A separate suit can be filed only if court fees are paid on ad valorem basis"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 144(2) CPC enacts an express statutory bar: 'No suit shall be instituted for the purpose of obtaining any restitution or other relief which could be obtained by application under sub-section (1).' The remedy is exclusively by application.",
        "optionBreakdown": {
            "A": "Incorrect; separate suit is prohibited, not mandatory.",
            "B": "Correct; Section 144(2) bars a separate suit for relief obtainable by application under Section 144(1).",
            "C": "Incorrect; concurrent suits are completely barred.",
            "D": "Incorrect; payment of fees cannot bypass the express statutory bar."
        },
        "difficulty": "Important",
        "provision": "Section 144(2) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Master the absolute bar against filing a separate suit for restitution under Section 144(2)."
    },
    {
        "id": "mcq-cpc-18-018",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-18",
        "topicId": "top-cpc-18-03",
        "question": "Does the determination of an application under Section 144 of the CPC constitute a 'decree' for the purposes of appeal?",
        "options": [
            "No, it is merely an interlocutory order from which no appeal lies",
            "Yes, by virtue of Section 2(2) of the CPC, the determination of any question within Section 144 is expressly included in the definition of a 'decree'",
            "It is a decree only if granted in favour of the plaintiff",
            "It is an appealable order under Order XLIII Rule 1, not a decree"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 2(2) CPC explicitly defines a decree to 'include... the determination of any question within section 144'. Therefore, an order deciding a Section 144 application is a deemed decree and is subject to a regular first appeal under Section 96 and second appeal under Section 100.",
        "optionBreakdown": {
            "A": "Incorrect; it is not an interlocutory order; Section 2(2) makes it a decree.",
            "B": "Correct; Section 2(2) explicitly includes determination of questions under Section 144 within the definition of a decree.",
            "C": "Incorrect; determination against either party constitutes a decree.",
            "D": "Incorrect; it is a full deemed decree, not an Order XLIII order."
        },
        "difficulty": "Important",
        "provision": "Section 2(2) & Section 144 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Understand that determination under Section 144 is a deemed decree under Section 2(2)."
    },
    {
        "id": "mcq-cpc-18-019",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-18",
        "topicId": "top-cpc-18-03",
        "question": "Can the court order payment of interest, damages, compensation, or mesne profits under Section 144(1) of the CPC?",
        "options": [
            "No, restitution is restricted strictly to physical redelivery of property without any financial adjustment",
            "Yes, Section 144(1) explicitly empowers the court to make orders for refund of costs and payment of interest, damages, compensation and mesne profits",
            "Only if interest was specifically claimed in the original plaint",
            "Only with the approval of the Reserve Bank of India"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 144(1) provides that the Court may make any orders, 'including orders for the refund of costs and for the payment of interest, damages, compensation and mesne profits, which are properly consequential on such variation, reversal, setting aside or modification of the decree or order.'",
        "optionBreakdown": {
            "A": "Incorrect; restitution includes complete financial restoration of benefits.",
            "B": "Correct; Section 144(1) explicitly empowers orders for costs, interest, damages, and mesne profits.",
            "C": "Incorrect; restitution flows from reversal, not from the original plaint prayer.",
            "D": "Incorrect; RBI has no role in judicial restitution."
        },
        "difficulty": "Standard",
        "provision": "Section 144(1) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Know the comprehensive scope of consequential financial reliefs under Section 144(1)."
    },
    {
        "id": "mcq-cpc-18-020",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-18",
        "topicId": "top-cpc-18-03",
        "question": "Can the court grant restitution in the exercise of its inherent powers under Section 151 where a case does not strictly fall within the four corners of Section 144?",
        "options": [
            "No, inherent powers can never be used for restitution because Section 144 is exhaustive",
            "Yes, Section 144 is not exhaustive; the court has inherent power under Section 151 to order restitution ex debito justitiae to prevent abuse of its process",
            "Only if the State Government issues a notification",
            "Only in suits where the subject matter is agricultural land"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "It is well settled (e.g. Kavita Trehan v. Balsara Hygiene Products Ltd., AIR 1995 SC 441) that Section 144 is not exhaustive of the court's power of restitution. The jurisdiction to make restitution is inherent in every court and can be exercised under Section 151 ex debito justitiae whenever justice demands.",
        "optionBreakdown": {
            "A": "Incorrect; Section 144 is not exhaustive of the power of restitution.",
            "B": "Correct; courts possess inherent power under Section 151 to grant restitution ex debito justitiae.",
            "C": "Incorrect; executive notifications are irrelevant to inherent judicial power.",
            "D": "Incorrect; applies to all civil property and subject matters."
        },
        "difficulty": "Important",
        "provision": "Sections 144 & 151 CPC Precedent",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Master the application of inherent powers under Section 151 for restitution beyond Section 144."
    }
]

questions_ch19 = [
    {
        "id": "mcq-cpc-19-001",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-19",
        "topicId": "top-cpc-19-01",
        "question": "Under the Uttar Pradesh State Amendment to Section 115 of the CPC, revisional jurisdiction is bifurcated between which two judicial forums based on valuation?",
        "options": [
            "High Court and Supreme Court",
            "High Court and District Court",
            "District Court and Tehsildar Court",
            "High Court and Revenue Board"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "The UP State Legislature amended Section 115 CPC to bifurcate revisional jurisdiction between the High Court and the District Court depending on the valuation of the suit, thereby decentralizing revision to District Judges.",
        "optionBreakdown": {
            "A": "Incorrect; Supreme Court has no Section 115 revision jurisdiction.",
            "B": "Correct; UP Amendment to Section 115 distributes revisional power between High Court and District Court.",
            "C": "Incorrect; Tehsildars are revenue officers under UP Revenue Code.",
            "D": "Incorrect; Board of Revenue governs revenue suits, not civil CPC revisions."
        },
        "difficulty": "Standard",
        "provision": "Section 115 UP State Amendment",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Know the bifurcation of revisional jurisdiction between High Court and District Court under UP Section 115."
    },
    {
        "id": "mcq-cpc-19-002",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-19",
        "topicId": "top-cpc-19-01",
        "question": "Under the UP State Amendment to Section 115 of the CPC, does a second revision lie to the High Court against an order passed by the District Court in revision?",
        "options": [
            "Yes, a second revision lies as of right to the High Court",
            "No, a second revision is expressly barred under the UP Amendment to Section 115",
            "Yes, if the valuation of the suit exceeds rupees ten lakhs",
            "Yes, if the District Judge certifies that the case involves a substantial question of law"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "The UP State Amendment to Section 115 categorically bars a second revision. Once an order is passed by the District Court in exercise of its revisional jurisdiction, no further revision lies to the High Court against that revisional order.",
        "optionBreakdown": {
            "A": "Incorrect; second revision is prohibited by statute.",
            "B": "Correct; the UP Amendment expressly bars a second revision against an order of the District Judge in revision.",
            "C": "Incorrect; valuation cannot overcome the statutory bar.",
            "D": "Incorrect; District Judges cannot certify second revisions."
        },
        "difficulty": "Important",
        "provision": "Section 115 UP State Amendment",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Recognize the absolute bar against second revisions under the UP Amendment to Section 115."
    },
    {
        "id": "mcq-cpc-19-003",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-19",
        "topicId": "top-cpc-19-01",
        "question": "Can a party invoke the writ jurisdiction of the High Court under Article 227 of the Constitution against a revisional order passed by the District Court under the UP Amendment to Section 115?",
        "options": [
            "Never; because the UP Amendment completely bars any further challenge in any court whatsoever",
            "Yes, supervisory jurisdiction under Article 227 cannot be curtailed by State Amendments to the CPC, though it is exercised sparingly for grave jurisdictional errors",
            "Only with the prior permission of the Governor of Uttar Pradesh",
            "Only if the order relates to an agricultural ceiling dispute"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "As held by the Supreme Court and Allahabad High Court Full Bench (e.g. Ganga Saran v. Civil Judge, Hapur), while a statutory second revision is barred by the UP Amendment to Section 115, the constitutional remedy under Article 227 remains available to correct grave errors of jurisdiction or gross miscarriage of justice.",
        "optionBreakdown": {
            "A": "Incorrect; statutory amendments cannot take away constitutional powers under Article 227.",
            "B": "Correct; Article 227 remains available as a constitutional safety valve, though exercised sparingly.",
            "C": "Incorrect; Governor has no role in judicial supervisory jurisdiction.",
            "D": "Incorrect; applies across all civil proceedings."
        },
        "difficulty": "Important",
        "provision": "UP S. 115 CPC & Art 227 Precedent",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Understand the availability of Article 227 despite the bar on second revision in Uttar Pradesh."
    },
    {
        "id": "mcq-cpc-19-004",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-19",
        "topicId": "top-cpc-19-01",
        "question": "Under the UP Amendment to Section 115, what was the primary legislative objective behind empowering the District Court to hear revisions?",
        "options": [
            "To increase court fees revenue for the State treasury",
            "To provide speedy and inexpensive local justice and reduce the heavy backlog of revisions in the Allahabad High Court",
            "To abolish the High Court's original jurisdiction",
            "To replace advocates with executive magistrates"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "The UP Amendment was enacted to decentralize judicial administration, enable litigants in distant districts to access revisional justice locally before the District Judge, and prevent congestion of the Allahabad High Court docket.",
        "optionBreakdown": {
            "A": "Incorrect; revenue generation was not the objective.",
            "B": "Correct; decentralization, affordable local remedies, and docket relief for the High Court were the key objectives.",
            "C": "Incorrect; Allahabad High Court had no ordinary original civil jurisdiction.",
            "D": "Incorrect; judicial independence was strictly maintained."
        },
        "difficulty": "Standard",
        "provision": "UP S. 115 Legislative Objective",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Know the policy and legislative rationale behind the UP revisional bifurcation."
    },
    {
        "id": "mcq-cpc-19-005",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-19",
        "topicId": "top-cpc-19-01",
        "question": "In a civil suit where the valuation is within the District Court's revisional jurisdiction in UP, can the revision be filed directly in the High Court bypassing the District Court?",
        "options": [
            "Yes, High Court has concurrent jurisdiction and can entertain any revision directly as a matter of first instance",
            "No, where the revisional jurisdiction is vested in the District Court, the revision must be presented to the District Court, and cannot be entertained directly by the High Court",
            "Yes, if the plaintiff is an advocate of the High Court",
            "Yes, during summer vacation only"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Under the UP statutory scheme, the forums are mutually exclusive based on valuation. Where jurisdiction lies with the District Court, a revision cannot be filed directly before the High Court, as that would defeat the statutory bifurcation.",
        "optionBreakdown": {
            "A": "Incorrect; bifurcation is jurisdictional, not optional.",
            "B": "Correct; the revision must be presented before the competent forum specified by valuation.",
            "C": "Incorrect; advocate litigants have no special forum privileges.",
            "D": "Incorrect; vacation benches cannot usurp statutory jurisdictional ceilings."
        },
        "difficulty": "Important",
        "provision": "Section 115 UP State Amendment",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Understand the mandatory forum adherence under the UP revisional scheme."
    },
    {
        "id": "mcq-cpc-19-006",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-19",
        "topicId": "top-cpc-19-01",
        "question": "What is the limitation period for filing a revision under Section 115 in Uttar Pradesh, governed by Article 131 of the Limitation Act, 1963?",
        "options": [
            "Thirty days (30 days)",
            "Sixty days (60 days)",
            "Ninety days (90 days)",
            "One hundred and twenty days (120 days)"
        ],
        "answer": 2,
        "answerLetter": "C",
        "explanation": "Article 131 of the Schedule to the Limitation Act, 1963 prescribes a period of 90 days for filing an application to any court for the exercise of its powers of revision under the CPC or CrPC, starting from the date of the decree or order or sentence sought to be revised.",
        "optionBreakdown": {
            "A": "Incorrect; 30 days is limitation for first appeals to District Court or High Court orders in some cases.",
            "B": "Incorrect; 60 days is not the Section 115 limitation.",
            "C": "Correct; Article 131 of the Limitation Act prescribes 90 days for revisions.",
            "D": "Incorrect; 120 days is not standard limitation."
        },
        "difficulty": "Standard",
        "provision": "Article 131 Limitation Act, 1963",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Recall the 90-day limitation period for revisions under Article 131 of the Limitation Act."
    },
    {
        "id": "mcq-cpc-19-007",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-19",
        "topicId": "top-cpc-19-01",
        "question": "Can the District Court in UP, while exercising revisional jurisdiction under Section 115, reverse a finding of pure fact recorded by the trial court?",
        "options": [
            "Yes, District Court has full appellate power over facts in revision",
            "No, revisional jurisdiction is strictly limited to jurisdictional errors, illegality or material irregularity; it cannot reappreciate pure evidence or substitute findings of fact",
            "Yes, if the suit relates to recovery of rent arrears",
            "Yes, if the oral evidence was not recorded by video"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Revisional jurisdiction, whether exercised by the High Court or the District Court under the UP Amendment, is fundamentally supervisory and jurisdictional. A revisional court cannot act as an appellate court to reappreciate evidence or disturb pure findings of fact unless perverse or without jurisdiction.",
        "optionBreakdown": {
            "A": "Incorrect; revision is not an appeal on facts.",
            "B": "Correct; revisional power is strictly confined to jurisdictional defects under clauses (a), (b), and (c).",
            "C": "Incorrect; subject matter does not convert revision into factual appeal.",
            "D": "Incorrect; recording method does not alter scope of revision."
        },
        "difficulty": "Important",
        "provision": "Section 115 UP Scope",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Know the strict boundary prohibiting revisional courts from reassessing findings of pure fact."
    },
    {
        "id": "mcq-cpc-19-008",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-19",
        "topicId": "top-cpc-19-02",
        "question": "Under Order XV Rule 5 of the CPC, as inserted by the Uttar Pradesh State Amendment, what must the defendant deposit in any suit for eviction or recovery of rent?",
        "options": [
            "The entire market value of the suit property",
            "The entire amount of rent arrears admitted by him to be due, together with 9% per annum interest, on or before the first hearing of the suit",
            "Half of the monthly damages without any interest",
            "Security bond of two sureties without cash deposit"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "UP Order XV Rule 5(1) mandates that in any suit for eviction of a tenant or for recovery of rent/compensation, the defendant shall deposit the entire amount admitted by him to be due together with interest thereon at nine per cent per annum at or before the first hearing of the suit.",
        "optionBreakdown": {
            "A": "Incorrect; deposit is of admitted rent arrears and monthly dues, not property value.",
            "B": "Correct; UP Order XV Rule 5(1) requires deposit of admitted arrears + 9% interest at/before first hearing.",
            "C": "Incorrect; statutory interest rate is 9% per annum.",
            "D": "Incorrect; cash deposit in court is required, not surety bonds."
        },
        "difficulty": "Important",
        "provision": "Order XV Rule 5(1) UP Amendment",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Master the initial deposit requirement under UP Order XV Rule 5(1) including the 9% interest mandate."
    },
    {
        "id": "mcq-cpc-19-009",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-19",
        "topicId": "top-cpc-19-02",
        "question": "Under UP Order XV Rule 5(1), in addition to the initial deposit, what ongoing monthly obligation is cast upon the defendant-tenant throughout the continuation of the suit?",
        "options": [
            "Deposit the monthly amount due within one week from the expiration of each successive month",
            "Deposit rent once every six months",
            "Deposit rent only when directed by a fresh notice from the plaintiff",
            "Deposit double rent if the suit is adjourned"
        ],
        "answer": 0,
        "answerLetter": "A",
        "explanation": "UP Order XV Rule 5(1) stipulates: '...and until the suit is determined, continue to deposit monthly amount due within one week from the expiration of each successive month.'",
        "optionBreakdown": {
            "A": "Correct; the monthly rent must be deposited regularly within one week of expiration of each month.",
            "B": "Incorrect; six-monthly deposit is not permitted.",
            "C": "Incorrect; the obligation is self-operating without requiring fresh notice from plaintiff.",
            "D": "Incorrect; adjournment does not double the rent obligation."
        },
        "difficulty": "Important",
        "provision": "Order XV Rule 5(1) UP Amendment",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Recall the ongoing monthly deposit timeline within one week of month expiration under UP Order XV Rule 5."
    },
    {
        "id": "mcq-cpc-19-010",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-19",
        "topicId": "top-cpc-19-02",
        "question": "What is the penalty prescribed under UP Order XV Rule 5(1) if the defendant fails to deposit the admitted arrears or ongoing monthly rent?",
        "options": [
            "The court may strike off his defence",
            "The defendant is immediately arrested and sent to civil prison",
            "The defendant's bank accounts are permanently frozen",
            "The suit is decreed for double damages"
        ],
        "answer": 0,
        "answerLetter": "A",
        "explanation": "UP Order XV Rule 5(1) provides that in the event of default in making the deposit, 'the court may, subject to the provisions of sub-rule (2), strike off his defence.'",
        "optionBreakdown": {
            "A": "Correct; striking off the defendant's defence is the specific statutory penalty.",
            "B": "Incorrect; arrest in civil prison is an execution remedy under Section 51, not the Order XV Rule 5 penalty.",
            "C": "Incorrect; account freezing is not provided under Order XV Rule 5.",
            "D": "Incorrect; double damages are not prescribed."
        },
        "difficulty": "Standard",
        "provision": "Order XV Rule 5(1) UP Amendment",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Identify the penalty of striking off defence under UP Order XV Rule 5(1)."
    },
    {
        "id": "mcq-cpc-19-011",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-19",
        "topicId": "top-cpc-19-02",
        "question": "In the landmark judgment Bimal Chand Jain v. Sri Gopal Agarwal (AIR 1981 SC 1657), what did the Supreme Court hold regarding the court's power to strike off defence under UP Order XV Rule 5?",
        "options": [
            "The power is mandatory and automatic, leaving the court no discretion whatsoever",
            "The power is discretionary and not mandatory; striking off defence is a severe penalty to be invoked only for contumacious or deliberate default, after considering defendant's representation",
            "The power can only be exercised by the High Court",
            "The power is unconstitutional and void"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "In Bimal Chand Jain, the Supreme Court held that the word 'may' in UP Order XV Rule 5 confers judicial discretion. Striking off defence is not automatic or mandatory; it is an extreme penalty to be used when default is willful, contumacious, or unexplained.",
        "optionBreakdown": {
            "A": "Incorrect; Supreme Court rejected the argument that striking off is automatic or mandatory.",
            "B": "Correct; Bimal Chand Jain established that the power is discretionary and requires contumacious default.",
            "C": "Incorrect; trial courts hearing eviction suits exercise this power.",
            "D": "Incorrect; the provision was upheld as valid and constitutional."
        },
        "difficulty": "Important",
        "provision": "UP Order XV Rule 5 Precedent",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Master the discretionary doctrine in Bimal Chand Jain concerning UP Order XV Rule 5."
    },
    {
        "id": "mcq-cpc-19-012",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-19",
        "topicId": "top-cpc-19-02",
        "question": "Under UP Order XV Rule 5(2), within what period from the date of default can the defendant make a representation explaining reasons for default to seek condonation?",
        "options": [
            "Within seven days",
            "Within ten days",
            "Within thirty days",
            "Within sixty days"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "UP Order XV Rule 5(2) provides that before making an order striking off the defence, the Court may consider any representation made by the defendant within ten days of such default, showing sufficient cause for not making the deposit.",
        "optionBreakdown": {
            "A": "Incorrect; 7 days is the monthly payment deadline, not representation deadline.",
            "B": "Correct; UP Order XV Rule 5(2) prescribes 10 days from default for making a representation.",
            "C": "Incorrect; 30 days is not the statutory period under sub-rule (2).",
            "D": "Incorrect; 60 days is too long."
        },
        "difficulty": "Important",
        "provision": "Order XV Rule 5(2) UP Amendment",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Know the 10-day limitation period for making representations under UP Order XV Rule 5(2)."
    },
    {
        "id": "mcq-cpc-19-013",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-19",
        "topicId": "top-cpc-19-02",
        "question": "If the defendant completely denies the existence of landlord-tenant relationship, is he still required to deposit admitted rent arrears under UP Order XV Rule 5?",
        "options": [
            "He must deposit whatever the plaintiff claims even if he is an absolute stranger",
            "Where the defendant bona fide denies the relationship of landlord and tenant, and admits no rent to be due to the plaintiff, his defence cannot be struck off for non-deposit of admitted arrears",
            "He must surrender the property to the police first",
            "He must deposit 50% of the market value of the property"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "As established by judicial precedents (e.g. Manik Lal v. Prescribed Authority), the obligation under UP Order XV Rule 5 applies to 'the entire amount admitted by him to be due'. Where the tenant-landlord relationship is bona fide denied and no rent is admitted due to the plaintiff, the defence cannot be struck off for non-deposit of admitted arrears, although the court will examine bona fides.",
        "optionBreakdown": {
            "A": "Incorrect; deposit is tied to 'admitted' dues, not unilateral plaint claims.",
            "B": "Correct; bona fide denial of relationship means there is no 'admitted' rent due to the plaintiff.",
            "C": "Incorrect; surrender to police has no place in civil tenancy jurisprudence.",
            "D": "Incorrect; property valuation deposit is alien to Order XV Rule 5."
        },
        "difficulty": "Advanced",
        "provision": "UP Order XV Rule 5 Interpretation",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Analyze the legal consequence of denying landlord-tenant relationship under UP Order XV Rule 5."
    },
    {
        "id": "mcq-cpc-19-014",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-19",
        "topicId": "top-cpc-19-02",
        "question": "Can the plaintiff landlord unconditionally withdraw the rent deposited by the defendant under UP Order XV Rule 5 without prejudice to his eviction suit?",
        "options": [
            "No, withdrawing rent waives the notice to quit and dismisses the eviction suit automatically",
            "Yes, the amount deposited may at any time be withdrawn by the plaintiff without prejudice to his suit or to the rights of the parties",
            "Only with the written consent of the Chief Judicial Magistrate",
            "Only after the final decree is passed in the suit"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "UP Order XV Rule 5 explicitly provides that the amount deposited may at any time be withdrawn by the plaintiff, and such withdrawal shall not be deemed to prejudice his rights or constitute waiver of any notice or forfeiture.",
        "optionBreakdown": {
            "A": "Incorrect; withdrawal under statutory mandate does not waive eviction grounds.",
            "B": "Correct; UP Order XV Rule 5 expressly protects landlord's right to withdraw without prejudice to the suit.",
            "C": "Incorrect; CJM has no role in civil rent suits.",
            "D": "Incorrect; withdrawal is permitted during the pendency of the suit."
        },
        "difficulty": "Standard",
        "provision": "Order XV Rule 5 UP Amendment",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Understand the non-prejudicial withdrawal of rent deposits by the landlord under UP Order XV Rule 5."
    },
    {
        "id": "mcq-cpc-19-015",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-19",
        "topicId": "top-cpc-19-03",
        "question": "What is the primary role of the 'Munsarim' in the subordinate civil courts of Uttar Pradesh under the General Rules (Civil), 1957?",
        "options": [
            "To act as a judge and deliver judgments in small suits",
            "To examine plaints, appeals and applications for proper court fees, limitation, jurisdiction, and formal compliance before registration",
            "To serve summons personally on all defendants in the district",
            "To conduct public auctions of attached agricultural lands"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Under Rule 24 and Chapter III of the General Rules (Civil), 1957 applicable to UP subordinate courts, the Munsarim is the chief ministerial officer of the civil court tasked with scrutinizing plaints, appeals and applications for defects, valuation, court fees, and limitation prior to registration.",
        "optionBreakdown": {
            "A": "Incorrect; Munsarim is a ministerial officer, not a judicial officer.",
            "B": "Correct; Munsarim's report is the mandatory administrative scrutiny for court fees, limitation, and defects.",
            "C": "Incorrect; summons are served by process servers (Nazarat), not the Munsarim.",
            "D": "Incorrect; auctions are conducted by court amin or revenue authorities."
        },
        "difficulty": "Important",
        "provision": "Rule 24 General Rules (Civil) 1957 (UP)",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Know the administrative and scrutiny responsibilities of the Munsarim under UP General Rules (Civil)."
    },
    {
        "id": "mcq-cpc-19-016",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-19",
        "topicId": "top-cpc-19-03",
        "question": "Under the General Rules (Civil), 1957 (UP), what is the 'Order Sheet' and what is its legal significance?",
        "options": [
            "A private diary kept by the plaintiff's advocate",
            "A formal, continuous, chronological record of every judicial and ministerial step, appearance, order, and adjournment taken in a case",
            "An invoice of fees paid to government pleaders",
            "A list of retired judicial officers in Uttar Pradesh"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Under the General Rules (Civil), 1957, the Order Sheet is an official, contemporaneous, continuous record maintained in each case recording every proceeding, order, appearance of parties, and date fixed. It is signed by the presiding judge and carries highest evidentiary credibility.",
        "optionBreakdown": {
            "A": "Incorrect; order sheet is an official court document, not an advocate's diary.",
            "B": "Correct; Order Sheet is the official chronological judicial record of all proceedings in the case.",
            "C": "Incorrect; fee invoices are separate administrative vouchers.",
            "D": "Incorrect; list of retired judges has no relation to a case file."
        },
        "difficulty": "Standard",
        "provision": "General Rules (Civil) 1957 (UP)",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Understand the role and evidentiary significance of the Order Sheet in UP civil practice."
    },
    {
        "id": "mcq-cpc-19-017",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-19",
        "topicId": "top-cpc-19-03",
        "question": "Under Rule 39 of the General Rules (Civil), 1957 (UP), what is the mandatory requirement for an advocate filing a Vakalatnama on behalf of a client?",
        "options": [
            "The advocate must pay cash security of Rs. 5,000",
            "The Vakalatnama must be accepted in writing by the advocate, and must bear his registration number, address, and proper welfare stamps",
            "The advocate must produce two gazetted officer recommendations",
            "The Vakalatnama must be signed by the District Judge"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "General Rules (Civil) Rule 39 mandates that every Vakalatnama must contain the advocate's written acceptance, enrollment/registration number, chamber/office address, and requisite court fee and advocate welfare fund stamps.",
        "optionBreakdown": {
            "A": "Incorrect; no cash security is required from advocates.",
            "B": "Correct; written acceptance, enrollment number, address, and stamps are statutory requisites.",
            "C": "Incorrect; gazetted officer certificates are not required.",
            "D": "Incorrect; District Judge does not sign private vakalatnamas."
        },
        "difficulty": "Standard",
        "provision": "Rule 39 General Rules (Civil) 1957 (UP)",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Recall the formalities of Vakalatnama execution under UP General Rules (Civil)."
    },
    {
        "id": "mcq-cpc-19-018",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-19",
        "topicId": "top-cpc-19-03",
        "question": "What is the procedure prescribed under General Rules (Civil), 1957 for filing and proving original documents in civil courts of UP?",
        "options": [
            "Documents can be handed over orally to the judge during arguments without any list",
            "Original documents must be submitted with a formal list in prescribed Form (List of Documents) with acknowledgment receipt, and endorsed with exhibit marks when admitted in evidence",
            "Documents can only be accepted if certified by a Notary Public from New Delhi",
            "All documents must be photocopied in colour and laminated"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "General Rules (Civil) require that every document produced by a party must be accompanied by a List of Documents (Dakhila) in prescribed form. When admitted in evidence, the presiding officer marks it with an exhibit mark (Ex. 1, Ex. A, etc.) pursuant to Order XIII Rule 4.",
        "optionBreakdown": {
            "A": "Incorrect; oral handovers without list are prohibited by rules of practice.",
            "B": "Correct; formal list (Dakhila), acknowledgment receipt, and judicial exhibit marking are strictly required.",
            "C": "Incorrect; notary certification from Delhi is not required.",
            "D": "Incorrect; laminating documents is not required and often discouraged."
        },
        "difficulty": "Standard",
        "provision": "General Rules (Civil) 1957 & O. XIII R. 4",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Know the procedure for filing, listing, and exhibit marking of documentary evidence in UP."
    },
    {
        "id": "mcq-cpc-19-019",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-19",
        "topicId": "top-cpc-19-03",
        "question": "What is 'Caveat' under Section 148A of the CPC and what is its operational duration?",
        "options": [
            "A notice claiming damages, valid for one year",
            "A caveat lodged by a person claiming a right to appear on an application, remaining in force for ninety days (90 days) from the date on which it was lodged",
            "An injunction order valid for thirty days",
            "A proclamation of insolvency valid for sixty days"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 148A(1) CPC allows any person claiming a right to appear before the court on the hearing of an application to lodge a caveat. Section 148A(5) enacts: 'Where a caveat has been lodged... it shall not remain in force for more than ninety days from the date on which it was lodged, unless the application... has been made before the expiry of the said period.'",
        "optionBreakdown": {
            "A": "Incorrect; caveat is not a damage claim and does not last one year.",
            "B": "Correct; Section 148A(5) fixes the operational lifespan of a caveat at 90 days.",
            "C": "Incorrect; caveat is a protective caveat notice, not an injunction.",
            "D": "Incorrect; insolvency proclamation is governed by Insolvency Acts."
        },
        "difficulty": "Standard",
        "provision": "Section 148A(5) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Master the provisions of Section 148A and the 90-day operational validity of a caveat."
    },
    {
        "id": "mcq-cpc-19-020",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-19",
        "topicId": "top-cpc-19-03",
        "question": "What is the consequence under Section 148A(3) of the CPC if an applicant files an interlocutory application for interim relief without serving notice on the caveator?",
        "options": [
            "The applicant is imprisoned for thirty days",
            "The applicant is mandated to serve a copy of the application and supporting documents on the caveator, and an ex parte interim order obtained suppressing caveat is liable to be recalled",
            "The main suit stands automatically dismissed",
            "The court can double the court fee"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 148A(3) mandates that after a caveat has been lodged, the applicant shall forthwith furnish the caveator with a copy of the application and all documents. An order passed in breach of Section 148A without notice to the caveator suffers from procedural illegality and is liable to be recalled upon application.",
        "optionBreakdown": {
            "A": "Incorrect; imprisonment is not a penalty for procedural omission.",
            "B": "Correct; service on caveator is mandatory under S. 148A(3); ex parte orders obtained without notice can be recalled.",
            "C": "Incorrect; suit is not dismissed.",
            "D": "Incorrect; court fee doubling is not prescribed."
        },
        "difficulty": "Important",
        "provision": "Section 148A(3) CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Understand the applicant's statutory duty to serve the caveator under Section 148A(3)."
    }
]

questions_ch20 = [
    {
        "id": "mcq-cpc-20-001",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-20",
        "topicId": "top-cpc-20-01",
        "question": "Under Section 148 of the CPC, what is the maximum total period by which a court may enlarge any period fixed or granted by it for the doing of any act?",
        "options": [
            "Not exceeding fifteen days",
            "Not exceeding thirty days in total",
            "Not exceeding sixty days",
            "Not exceeding ninety days"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 148 CPC (as amended in 1999) provides that where any period is fixed or granted by the Court, the Court may in its discretion enlarge such period 'not exceeding thirty days in the total', even though the period originally fixed or granted may have expired.",
        "optionBreakdown": {
            "A": "Incorrect; 15 days is not the statutory ceiling under Section 148.",
            "B": "Correct; Section 148 prescribes that enlargement shall not exceed thirty days in the total.",
            "C": "Incorrect; 60 days exceeds the statutory ceiling.",
            "D": "Incorrect; 90 days is not the Section 148 limit."
        },
        "difficulty": "Important",
        "provision": "Section 148 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Know the 30-day statutory ceiling for enlargement of time under Section 148."
    },
    {
        "id": "mcq-cpc-20-002",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-20",
        "topicId": "top-cpc-20-01",
        "question": "Can the 30-day limit in Section 148 of the CPC fetter the inherent powers of the court under Section 151 in exceptional cases of hardship, as held in Salem Advocate Bar Association (II)?",
        "options": [
            "No, Section 151 can never be used to extend time beyond 30 days under any circumstances",
            "Yes, the procedural cap of 30 days in Section 148 is directory and does not extinguish the court's inherent power under Section 151 to extend time in rare, exceptional circumstances to prevent injustice",
            "Only if the President of India grants an exemption",
            "Only in suits where the Government is the plaintiff"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "In Salem Advocate Bar Association (II) v. Union of India (AIR 2005 SC 3353), the Supreme Court held that the 30-day cap in Section 148 is not an absolute limitation on the court's inherent power under Section 151 to extend time in rare, exceptional cases beyond the control of parties to advance substantial justice.",
        "optionBreakdown": {
            "A": "Incorrect; Salem Bar Association held that Section 151 remains available in rare cases.",
            "B": "Correct; the 30-day limit is directory and does not bar exercise of Section 151 in exceptional circumstances.",
            "C": "Incorrect; executive exemptions are completely irrelevant.",
            "D": "Incorrect; rule applies to all litigants equally."
        },
        "difficulty": "Advanced",
        "provision": "Sections 148 & 151 CPC Precedent",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Analyze the interplay between Section 148 time caps and Section 151 inherent powers under Salem Bar Association."
    },
    {
        "id": "mcq-cpc-20-003",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-20",
        "topicId": "top-cpc-20-01",
        "question": "What is the maximum number of adjournments that may be granted to a party during the hearing of a suit under Order XVII Rule 1(1) Proviso of the CPC?",
        "options": [
            "One adjournment only",
            "Not more than three times to a party during the hearing of the suit",
            "Five adjournments per year",
            "Unlimited adjournments upon payment of costs"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "The Proviso to Order XVII Rule 1(1) (inserted by 1999 Amendment) provides: 'Provided that no such adjournment shall be granted more than three times to a party during the hearing of the suit.' In Salem Bar Association, this was held to be directory in exceptional circumstances beyond a party's control.",
        "optionBreakdown": {
            "A": "Incorrect; statute allows up to three adjournments.",
            "B": "Correct; Order XVII Rule 1(1) Proviso fixes the ceiling at not more than three times.",
            "C": "Incorrect; five per year is not the statutory rule.",
            "D": "Incorrect; costs cannot buy unlimited adjournments."
        },
        "difficulty": "Standard",
        "provision": "Order XVII Rule 1(1) Proviso CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Recall the three-adjournment statutory rule under Order XVII Rule 1."
    },
    {
        "id": "mcq-cpc-20-004",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-20",
        "topicId": "top-cpc-20-01",
        "question": "Under Order VIII Rule 1 of the CPC, what is the outer time limit for filing a Written Statement from the date of service of summons?",
        "options": [
            "Thirty days (ordinarily), extendable up to ninety days for reasons recorded in writing",
            "Thirty days strictly without any extension",
            "Sixty days extendable up to one hundred and twenty days",
            "One hundred and eighty days"
        ],
        "answer": 0,
        "answerLetter": "A",
        "explanation": "Order VIII Rule 1 provides that the defendant shall file WS within 30 days of service of summons; if failed, the court may allow it to be filed on such other day for reasons recorded in writing, but 'which shall not be later than ninety days from the date of service of summons.'",
        "optionBreakdown": {
            "A": "Correct; 30 days ordinary period extendable up to 90 days under Order VIII Rule 1.",
            "B": "Incorrect; extension up to 90 days is explicitly permitted.",
            "C": "Incorrect; 120 days applies to Commercial Courts under the Commercial Courts Act, 2015, not standard CPC.",
            "D": "Incorrect; 180 days is not provided under Order VIII Rule 1."
        },
        "difficulty": "Standard",
        "provision": "Order VIII Rule 1 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Master the 30-day and 90-day time limits for written statements under Order VIII Rule 1."
    },
    {
        "id": "mcq-cpc-20-005",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-20",
        "topicId": "top-cpc-20-01",
        "question": "In Kailash v. Nanhku (AIR 2005 SC 2441), how did the Supreme Court interpret the 90-day limitation period under Order VIII Rule 1 in non-commercial civil suits?",
        "options": [
            "It is mandatory and absolute, debarring courts from accepting any WS after 90 days under any circumstances",
            "It is directory and not mandatory; in exceptional cases of grave hardship and circumstances beyond the defendant's control, the court may permit filing of WS beyond 90 days on payment of costs",
            "It applies only to suits filed by banks",
            "It was declared unconstitutional and struck down"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "The Supreme Court in Kailash v. Nanhku held that the 90-day outer limit in Order VIII Rule 1 is a rule of procedure and therefore directory, not mandatory. The court retains power to accept WS beyond 90 days in exceptional situations to prevent injustice, though extension should not be granted routinely.",
        "optionBreakdown": {
            "A": "Incorrect; the mandatory interpretation applies strictly only to Commercial Courts Act, not regular civil suits.",
            "B": "Correct; Kailash v. Nanhku held that Order VIII Rule 1 is directory in regular civil suits.",
            "C": "Incorrect; applies across all general civil suits.",
            "D": "Incorrect; the provision was upheld as directory."
        },
        "difficulty": "Important",
        "provision": "Order VIII Rule 1 Precedent",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Understand the directory interpretation of the 90-day WS period under Kailash v. Nanhku."
    },
    {
        "id": "mcq-cpc-20-006",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-20",
        "topicId": "top-cpc-20-01",
        "question": "What is the limitation period for filing an application under Order IX Rule 13 of the CPC to set aside an ex parte decree, under Article 123 of the Limitation Act, 1963?",
        "options": [
            "Thirty days (30 days) from the date of the decree or where summons was not duly served, when the applicant had knowledge of the decree",
            "Sixty days (60 days) from the date of the decree",
            "Ninety days (90 days)",
            "Three years from the date of the decree"
        ],
        "answer": 0,
        "answerLetter": "A",
        "explanation": "Article 123 of the Limitation Act, 1963 provides a limitation period of 30 days to set aside a decree passed ex parte. The time begins to run from the date of the decree or, where summons was not duly served, when the applicant had knowledge of the decree.",
        "optionBreakdown": {
            "A": "Correct; Article 123 prescribes 30 days from decree or from knowledge where summons was not duly served.",
            "B": "Incorrect; 60 days is not the limitation under Article 123.",
            "C": "Incorrect; 90 days applies to second appeals and revisions.",
            "D": "Incorrect; 3 years is the residuary article, not applicable to Order IX Rule 13."
        },
        "difficulty": "Standard",
        "provision": "Article 123 Limitation Act & O. IX R. 13",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Know the 30-day limitation period under Article 123 for setting aside an ex parte decree."
    },
    {
        "id": "mcq-cpc-20-007",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-20",
        "topicId": "top-cpc-20-01",
        "question": "What is the period of limitation for execution of a decree for mandatory injunction versus a decree other than mandatory injunction under Articles 135 and 136 of the Limitation Act, 1963?",
        "options": [
            "3 years for mandatory injunction; 12 years for any other decree",
            "12 years for mandatory injunction; 3 years for other decrees",
            "30 days for mandatory injunction; 1 year for other decrees",
            "No limitation applies to any decree under CPC"
        ],
        "answer": 0,
        "answerLetter": "A",
        "explanation": "Article 135 of the Limitation Act prescribes 3 years for execution of a decree granting a mandatory injunction. Article 136 prescribes 12 years for execution of any decree (other than mandatory injunction) or order of any civil court.",
        "optionBreakdown": {
            "A": "Correct; Article 135 prescribes 3 years for mandatory injunctions; Article 136 prescribes 12 years for other decrees.",
            "B": "Incorrect; the timeframes are inverted.",
            "C": "Incorrect; 30 days and 1 year are not execution limitations.",
            "D": "Incorrect; execution of decrees is strictly subject to Articles 135 and 136."
        },
        "difficulty": "Important",
        "provision": "Articles 135 & 136 Limitation Act",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Distinguish the limitation periods of 3 years (Art 135) and 12 years (Art 136) for execution."
    },
    {
        "id": "mcq-cpc-20-008",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-20",
        "topicId": "top-cpc-20-02",
        "question": "In the Constitution Bench decision Salem Advocate Bar Association v. Union of India (2003 & 2005), what was the Supreme Court's ruling regarding the constitutional validity of the 1999 and 2002 CPC Amendments?",
        "options": [
            "The amendments were declared wholly unconstitutional and struck down",
            "The amendments were upheld as constitutionally valid, with judicial clarification harmonizing strict procedural rules to prevent injustice",
            "The amendments were held valid only for commercial disputes exceeding Rs. 1 crore",
            "The Supreme Court referred the matter to the Parliament for complete repeal"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "The Supreme Court in Salem Advocate Bar Association (I & II) upheld the constitutional validity of all provisions introduced by the 1999 and 2002 Amendment Acts, interpreting strict timelines (such as WS filing and adjournments) as directory in exceptional circumstances to serve the ends of justice.",
        "optionBreakdown": {
            "A": "Incorrect; none of the amendments were struck down.",
            "B": "Correct; the 1999 and 2002 CPC Amendments were upheld with harmonizing judicial guidelines.",
            "C": "Incorrect; the decision applied universally across all civil proceedings.",
            "D": "Incorrect; Parliament was not directed to repeal."
        },
        "difficulty": "Important",
        "provision": "CPC Amendments Landmark Precedent",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Know the constitutional status and authoritative harmonizing principles of the Salem Bar judgments."
    },
    {
        "id": "mcq-cpc-20-009",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-20",
        "topicId": "top-cpc-20-02",
        "question": "In Kiran Singh v. Chaman Paswan (AIR 1954 SC 340), what fundamental principle was laid down regarding a decree passed by a court without subject-matter jurisdiction?",
        "options": [
            "It is a minor irregularity curable under Section 99",
            "A defect of jurisdiction strikes at the very authority of the court to pass any decree, and such a decree is a nullity whose invalidity could be set up whenever and wherever it is sought to be enforced or relied upon",
            "It is valid unless challenged within thirty days by a regular appeal",
            "It can be validated if the defendant paid costs in the trial court"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "In Kiran Singh, the Supreme Court held: 'It is a fundamental principle well-established that a decree passed by a court without jurisdiction is a nullity, and that its invalidity could be set up whenever and wherever it is sought to be enforced or relied upon, even at the stage of execution and even in collateral proceedings.'",
        "optionBreakdown": {
            "A": "Incorrect; Section 99 explicitly does NOT cure lack of jurisdiction.",
            "B": "Correct; Kiran Singh established that a decree without jurisdiction is an absolute nullity challengeable anywhere.",
            "C": "Incorrect; a nullity does not gain validity by lapse of 30 days.",
            "D": "Incorrect; payment of costs cannot confer jurisdiction."
        },
        "difficulty": "Important",
        "provision": "Jurisdiction Landmark Precedent",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Master the doctrine that a decree passed without jurisdiction is a void nullity under Kiran Singh."
    },
    {
        "id": "mcq-cpc-20-010",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-20",
        "topicId": "top-cpc-20-02",
        "question": "In Morgan Stanley Mutual Fund v. Kartick Das (1994) 4 SCC 225, what principles were laid down by the Supreme Court regarding the grant of ex parte interim injunctions under Order XXXIX Rule 3?",
        "options": [
            "Ex parte injunctions should be granted as a matter of routine in every suit without notice",
            "Ex parte injunction is an extraordinary remedy; court must record reasons and satisfy whether irreparable injury would ensue, whether refusal would entail greater hardship, and whether plaintiff acted bona fide",
            "Ex parte injunction can only be granted in suits against foreign companies",
            "Courts are prohibited from ever granting ex parte injunctions"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "In Morgan Stanley, the Supreme Court laid down strict guidelines for granting ex parte injunctions: court must evaluate whether irreparable damage will ensue before notice can be served, whether refusal entails greater hardship, comparative mischief, bona fides of plaintiff, and must record cogent reasons.",
        "optionBreakdown": {
            "A": "Incorrect; routine grant of ex parte injunctions is an abuse of process.",
            "B": "Correct; Morgan Stanley formulated the mandatory guidelines for ex parte injunctions under Order XXXIX Rule 3.",
            "C": "Incorrect; guidelines apply universally across all suits.",
            "D": "Incorrect; ex parte injunctions are permitted in urgent cases with recorded reasons."
        },
        "difficulty": "Important",
        "provision": "Order XXXIX Rule 3 Precedent",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Know the landmark guidelines governing ex parte interim injunctions under Morgan Stanley."
    },
    {
        "id": "mcq-cpc-20-011",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-20",
        "topicId": "top-cpc-20-02",
        "question": "In Manohar Lal Chopra v. Rai Bahadur Rao Raja Seth Hiralal (AIR 1962 SC 527), what did the Supreme Court hold regarding the power of civil courts to grant temporary injunctions outside Order XXXIX?",
        "options": [
            "Civil courts have no power whatsoever to grant injunctions outside Order XXXIX Rules 1 and 2",
            "The provisions of Order XXXIX are not exhaustive; civil courts have inherent power under Section 151 to grant temporary injunction in cases not falling within Order XXXIX, if ends of justice so require",
            "Injunctions outside Order XXXIX can only be issued by the Governor",
            "Inherent power under Section 151 cannot be exercised in any procedural matter"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "The Supreme Court in Manohar Lal Chopra held that Order XXXIX is not exhaustive. A civil court has inherent power under Section 151 to issue temporary injunctions in circumstances not covered by Order XXXIX Rules 1 and 2, provided it does not conflict with any express prohibition in the Code.",
        "optionBreakdown": {
            "A": "Incorrect; the Supreme Court rejected the argument of exhaustiveness.",
            "B": "Correct; Manohar Lal Chopra established that courts can grant injunctions under Section 151 outside Order XXXIX.",
            "C": "Incorrect; executive has no role in judicial interim injunctions.",
            "D": "Incorrect; Section 151 explicitly inheres in civil courts."
        },
        "difficulty": "Important",
        "provision": "Order XXXIX & Section 151 Precedent",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Master the doctrine in Manohar Lal Chopra regarding inherent power to grant injunctions under Section 151."
    },
    {
        "id": "mcq-cpc-20-012",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-20",
        "topicId": "top-cpc-20-02",
        "question": "In Bhanu Kumar Jain v. Archana Kumar (2005) 1 SCC 787, what did the Supreme Court hold regarding the simultaneous remedies available to an ex parte defendant under Section 96(2) and Order IX Rule 13?",
        "options": [
            "Filing an appeal under Section 96(2) automatically extinguishes the right to file an application under Order IX Rule 13",
            "A defendant has two parallel remedies (first appeal under S. 96(2) and setting aside application under O. IX R. 13); both can be pursued, but once an appeal is dismissed on merits, the Order IX Rule 13 application becomes infructuous under Explanation to Order IX Rule 13",
            "The defendant must choose only one remedy and the election is irrevocable from day one",
            "An ex parte defendant has no remedy under CPC"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "In Bhanu Kumar Jain, the Supreme Court reconciled Section 96(2) and Order IX Rule 13. The remedies are concurrent; in an application under Order IX Rule 13 the question is 'sufficient cause for non-appearance', whereas in an appeal under Section 96(2) the merits of the suit are challenged. However, under the Explanation to Order IX Rule 13, dismissal of appeal on any ground other than withdrawal bars the Order IX Rule 13 application.",
        "optionBreakdown": {
            "A": "Incorrect; filing appeal does not immediately extinguish Order IX Rule 13 right.",
            "B": "Correct; Bhanu Kumar Jain established the distinct scope and interaction of Section 96(2) and Order IX Rule 13.",
            "C": "Incorrect; doctrine of election does not bar concurrent institution initially.",
            "D": "Incorrect; both remedies are statutorily conferred."
        },
        "difficulty": "Advanced",
        "provision": "Section 96(2) & Order IX Rule 13 Precedent",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Analyze the dual-track remedies against ex parte decrees under Bhanu Kumar Jain."
    },
    {
        "id": "mcq-cpc-20-013",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-20",
        "topicId": "top-cpc-20-02",
        "question": "In Dahiben v. Arvindbhai Kalyanji Bhanusali (2020) 7 SCC 366, what principle was reiterated regarding the rejection of a plaint under Order VII Rule 11 of the CPC?",
        "options": [
            "The court must examine the written statement and defence evidence before rejecting a plaint",
            "For the purposes of Order VII Rule 11, only the averments in the plaint and documents produced with the plaint must be scrutinized; the defence in the written statement is wholly irrelevant at that stage",
            "A plaint can be rejected only after framing of issues",
            "Rejection of plaint can only be ordered on oral request of the Advocate General"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "In Dahiben, the Supreme Court reaffirmed that while considering an application under Order VII Rule 11, the court has to look only at the averments in the plaint and documents produced therewith. The defence taken in the written statement or other materials cannot be considered at that threshold stage.",
        "optionBreakdown": {
            "A": "Incorrect; looking at defence in WS is an error of law under Order VII Rule 11.",
            "B": "Correct; Dahiben reaffirmed that only the plaint averments and attached documents are relevant under Order VII Rule 11.",
            "C": "Incorrect; plaint can be rejected at any stage before conclusion of trial.",
            "D": "Incorrect; court exercises judicial power on party application or suo motu."
        },
        "difficulty": "Important",
        "provision": "Order VII Rule 11 CPC Precedent",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Master the threshold examination rule under Order VII Rule 11 reiterated in Dahiben."
    },
    {
        "id": "mcq-cpc-20-014",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-20",
        "topicId": "top-cpc-20-02",
        "question": "In Shiv Shakti Coop. Housing Society v. Swaraj Developers (2003) 6 SCC 659, what did the Supreme Court hold regarding the maintainability of a revision under Section 115 against an interlocutory order?",
        "options": [
            "A revision lies against every interim order passed by a subordinate court",
            "Under the amended Section 115, no revision lies against an interlocutory order unless the order, if it had been made in favour of the applicant, would have finally disposed of the suit or other proceeding",
            "Interlocutory orders can only be revised by the District Magistrate",
            "Section 115 was completely abolished by the 1999 amendment"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "In Shiv Shakti, the Supreme Court held that the Proviso to Section 115(1) as amended by Act 46 of 1999 is a condition precedent. Unless the order, if made in favour of the applicant, would have brought about a final termination of the suit or proceeding, revision is not maintainable.",
        "optionBreakdown": {
            "A": "Incorrect; routine revisions against interlocutory orders are barred by the Proviso.",
            "B": "Correct; Shiv Shakti established that final disposal test is mandatory for revisional maintainability.",
            "C": "Incorrect; District Magistrate has no civil revisional jurisdiction.",
            "D": "Incorrect; Section 115 remains on the statute book in amended form."
        },
        "difficulty": "Important",
        "provision": "Section 115 CPC Precedent",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Understand the strict 'final disposal' test under Section 115 interpreted in Shiv Shakti."
    },
    {
        "id": "mcq-cpc-20-015",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-20",
        "topicId": "top-cpc-20-03",
        "question": "Scenario: Plaintiff 'P' files a suit for recovery of Rs. 20,000 based on a promissory note against 'D' in the Court of Small Causes. The suit is decreed. 'D' seeks to file a first appeal. Can 'D' file a first appeal on questions of fact under Section 96(4) of the CPC?",
        "options": [
            "Yes, first appeals lie on both facts and law unconditionally",
            "No, under Section 96(4), in suits of Small Cause nature where value does not exceed Rs. 10,000, appeal lies only on questions of law; but since here value is Rs. 20,000, Section 96(4) bar does NOT apply and appeal lies on both law and facts",
            "No, Small Cause decrees are never appealable under any circumstances",
            "Yes, but only with the sanction of the High Court Registrar"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Section 96(4) bars appeals except on a question of law in suits cognizable by Courts of Small Causes when the value 'does not exceed ten thousand rupees'. Here the valuation is Rs. 20,000, which exceeds Rs. 10,000; therefore, the statutory restriction does not apply, and a regular appeal lies on both facts and law.",
        "optionBreakdown": {
            "A": "Incorrect; Section 96(4) restricts appeals where valuation <= Rs. 10,000.",
            "B": "Correct; since valuation is Rs. 20,000 (exceeding Rs. 10,000), the Section 96(4) restriction is inapplicable.",
            "C": "Incorrect; Small Cause decrees above Rs. 10,000 are appealable under regular provisions.",
            "D": "Incorrect; Registrar's sanction is not a requirement."
        },
        "difficulty": "Important",
        "provision": "Section 96(4) CPC Application",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Apply the Rs. 10,000 threshold of Section 96(4) to practical problem scenarios."
    },
    {
        "id": "mcq-cpc-20-016",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-20",
        "topicId": "top-cpc-20-03",
        "question": "Scenario: In a suit for permanent injunction, the trial court grants a temporary injunction under Order XXXIX Rule 1 in favour of the plaintiff. Defendant 'D' is aggrieved. What is the immediate procedural remedy available to 'D' under the CPC?",
        "options": [
            "File a regular first appeal under Section 96",
            "File an appeal from order under Section 104 read with Order XLIII Rule 1(r) or apply for discharge/variation under Order XXXIX Rule 4",
            "File a second appeal to the High Court under Section 100",
            "File a criminal complaint for extortion"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "An order under Order XXXIX Rule 1 is an appealable order under Order XLIII Rule 1(r). Alternatively, the defendant may apply to the same court to discharge, vary or set aside the injunction under Order XXXIX Rule 4 if false statements were made or change of circumstances occurred.",
        "optionBreakdown": {
            "A": "Incorrect; Section 96 applies to final decrees, not interlocutory injunction orders.",
            "B": "Correct; an appeal under Order XLIII Rule 1(r) or an application under Order XXXIX Rule 4 are the appropriate remedies.",
            "C": "Incorrect; second appeals lie only to High Court from appellate decrees.",
            "D": "Incorrect; judicial orders do not constitute criminal extortion."
        },
        "difficulty": "Standard",
        "provision": "Order XLIII Rule 1(r) & O. XXXIX R. 4",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Identify remedies against temporary injunction orders under Order XLIII Rule 1(r) and Order XXXIX Rule 4."
    },
    {
        "id": "mcq-cpc-20-017",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-20",
        "topicId": "top-cpc-20-03",
        "question": "Scenario: Plaintiff 'A' files a suit for recovery of possession against 'B'. The suit is dismissed for default of appearance of both parties under Order IX Rule 3. What remedy is available to 'A'?",
        "options": [
            "A can file a fresh suit subject to limitation, or apply under Order IX Rule 4 to set aside the dismissal",
            "A is permanently debarred from bringing a fresh suit on the same cause of action",
            "A must file a revision before the Supreme Court",
            "A can only execute the dismissed plaint"
        ],
        "answer": 0,
        "answerLetter": "A",
        "explanation": "Under Order IX Rule 4 CPC, where a suit is dismissed under Rule 2 or Rule 3, the plaintiff may (subject to law of limitation) bring a fresh suit, or he may apply for an order to set the dismissal aside on showing sufficient cause.",
        "optionBreakdown": {
            "A": "Correct; Order IX Rule 4 provides dual options: bring a fresh suit or apply to set aside dismissal.",
            "B": "Incorrect; bar on fresh suit applies to dismissals under Rule 8 (via Rule 9), NOT Rule 3.",
            "C": "Incorrect; Supreme Court revision is completely inapplicable.",
            "D": "Incorrect; dismissed plaints cannot be executed."
        },
        "difficulty": "Important",
        "provision": "Order IX Rules 3 & 4 CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Distinguish consequences of dismissal under Order IX Rule 3 from dismissal under Order IX Rule 8."
    },
    {
        "id": "mcq-cpc-20-018",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-20",
        "topicId": "top-cpc-20-03",
        "question": "Scenario: Defendant 'D' intentionally violates a temporary injunction order passed against him under Order XXXIX Rule 1. What action can the court take against 'D' under Order XXXIX Rule 2A of the CPC?",
        "options": [
            "Sentence 'D' to life imprisonment",
            "Attach 'D's property and detain him in civil prison for a term not exceeding three months",
            "Order demolition of 'D's ancestral home without hearing",
            "Impose a fine of rupees ten lakhs payable to the Prime Minister's Relief Fund"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "Order XXXIX Rule 2A(1) CPC provides that for disobedience or breach of an injunction, the Court may order the property of the person guilty of such disobedience to be attached, and may also order such person to be detained in the civil prison for a term not exceeding three months.",
        "optionBreakdown": {
            "A": "Incorrect; life imprisonment is a penal sentence for murder, not civil disobedience.",
            "B": "Correct; Order XXXIX Rule 2A authorizes attachment of property and civil prison detention up to 3 months.",
            "C": "Incorrect; demolition without due process is prohibited.",
            "D": "Incorrect; statutory remedy is civil prison and attachment, not PM Fund fines."
        },
        "difficulty": "Standard",
        "provision": "Order XXXIX Rule 2A CPC",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Recall the penalties for breach of injunction under Order XXXIX Rule 2A."
    },
    {
        "id": "mcq-cpc-20-019",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-20",
        "topicId": "top-cpc-20-03",
        "question": "Scenario: An executing court is executing a decree for recovery of money. The judgment-debtor objects that the decree was obtained by fraud and that the trial court misinterpreted the contract. Can the executing court examine these objections under Section 47 of the CPC?",
        "options": [
            "Yes, executing court has full power to retry the entire suit from inception",
            "No, the executing court cannot go behind the decree; it must execute the decree as it stands, unless the decree is a complete nullity for inherent lack of jurisdiction",
            "Yes, executing court can modify the contract terms to make them fair",
            "Yes, if the judgment-debtor is a senior citizen"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "It is a cardinal principle of execution jurisprudence under Section 47 that an executing court cannot go behind the decree. It must execute the decree as it stands and cannot question its correctness or legality on merits, unless the decree on its face was passed by a court lacking inherent jurisdiction (a nullity under Kiran Singh).",
        "optionBreakdown": {
            "A": "Incorrect; retrying the suit is strictly prohibited in execution.",
            "B": "Correct; the executing court cannot go behind the decree except in cases of inherent lack of jurisdiction.",
            "C": "Incorrect; courts cannot rewrite contracts in execution.",
            "D": "Incorrect; senior citizen status does not empower going behind decrees."
        },
        "difficulty": "Important",
        "provision": "Section 47 CPC Precedent",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Apply the rule that an executing court cannot go behind the decree under Section 47."
    },
    {
        "id": "mcq-cpc-20-020",
        "subjectId": "law-cpc",
        "chapterId": "ch-cpc-20",
        "topicId": "top-cpc-20-03",
        "question": "Scenario: In a suit for specific performance, the defendant fails to file a Written Statement within 90 days. The trial court, without applying its mind to the plaint or requiring any proof, automatically pronounces judgment against the defendant under Order VIII Rule 10. Is this approach legally sustainable under Balraj Taneja v. Sunil Madan (AIR 1999 SC 3381)?",
        "options": [
            "Yes, under Order VIII Rule 10 judgment must be automatically pronounced against the defendant whenever WS is not filed",
            "No, Order VIII Rule 10 is discretionary; court must apply its judicial mind, ensure plaint averments establish a valid cause of action, and should not pass judgment blindly merely because WS was not filed",
            "Yes, because failure to file WS is deemed to be an admission of murder",
            "Yes, if the suit was filed by an advocate"
        ],
        "answer": 1,
        "answerLetter": "B",
        "explanation": "In Balraj Taneja v. Sunil Madan, the Supreme Court held that under Order VIII Rule 10, the court is not bound to pass judgment blindly just because a written statement has not been filed. The court must be cautious, verify that the plaint discloses a valid claim, and may require the plaintiff to prove his case or make such order as it thinks fit.",
        "optionBreakdown": {
            "A": "Incorrect; automatic or blind pronouncement was expressly disapproved in Balraj Taneja.",
            "B": "Correct; Balraj Taneja held that judgment under Order VIII Rule 10 requires judicial application of mind and is not automatic.",
            "C": "Incorrect; absurd proposition.",
            "D": "Incorrect; status of plaintiff is irrelevant."
        },
        "difficulty": "Advanced",
        "provision": "Order VIII Rule 10 Precedent",
        "sourceUrl": "https://www.indiacode.nic.in/handle/123456789/2191",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": "Master the judicial application of mind required under Order VIII Rule 10 as laid down in Balraj Taneja."
    }
]

all_mcqs = questions_ch16 + questions_ch17 + questions_ch18 + questions_ch19 + questions_ch20

for mcq in all_mcqs:
    mcq["eligible"] = True
    mcq["status"] = "active"

output_py = '''"""
Part D: Chapters 16 to 20 (100 Verified MCQs)
Ch 16: 20 MCQs (mcq-cpc-16-001 to 020)
Ch 17: 20 MCQs (mcq-cpc-17-001 to 020)
Ch 18: 20 MCQs (mcq-cpc-18-001 to 020)
Ch 19: 20 MCQs (mcq-cpc-19-001 to 020)
Ch 20: 20 MCQs (mcq-cpc-20-001 to 020)
"""

MCQS_PART_D = ''' + json.dumps(all_mcqs, indent=2, ensure_ascii=False) + '''
'''

with open("scripts/cpc_mcq_part_d.py", "w", encoding="utf-8") as f:
    f.write(output_py)

print(f"Generated scripts/cpc_mcq_part_d.py with {len(all_mcqs)} MCQs.")
