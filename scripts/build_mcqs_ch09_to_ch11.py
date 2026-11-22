"""
Builds MCQs for Chapters 9, 10, and 11 (100 MCQs) as Python dictionaries.
Ch 9: 35 MCQs | Ch 10: 35 MCQs | Ch 11: 30 MCQs
"""

def create_mcq(m_id, ch_id, top_id, q_text, opts, ans_idx, expl, breakdowns, diff, prov, obj):
    letters = ["A", "B", "C", "D"]
    return {
        "id": m_id,
        "subjectId": "law-constitution",
        "chapterId": ch_id,
        "topicId": top_id,
        "question": q_text,
        "options": opts,
        "answer": ans_idx,
        "answerLetter": letters[ans_idx],
        "explanation": expl,
        "optionBreakdown": breakdowns,
        "difficulty": diff,
        "provision": prov,
        "sourceUrl": "https://legislative.gov.in",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": obj,
        "eligible": True,
        "status": "active"
    }

from build_mcqs_ch09 import MCQS_CH09
MCQS_CH09_11 = list(MCQS_CH09)
print(f"Loaded {len(MCQS_CH09_11)} MCQs from Chapter 9.")
print("Building MCQs for Chapters 10 and 11...")

# ==============================================================================
# CHAPTER 10: THE UNION PARLIAMENT (35 MCQs)
# ==============================================================================
# 10-01 to 10-12: Composition, Sessions, Presiding Officers
MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-001", "ch-10", "top-const-10-01",
    "Under Article 79 of the Constitution, the Parliament of the Union consists of:",
    ["The Lok Sabha and the Rajya Sabha only", "The President and the two Houses (Council of States and House of the People)", "The Prime Minister, the Lok Sabha, and the Rajya Sabha", "The Supreme Court and the two Houses"],
    1,
    "Article 79 explicitly defines the composition of Parliament: 'There shall be a Parliament for the Union which shall consist of the President and two Houses to be known respectively as the Council of States and the House of the People'. The President is an integral component of Parliament.",
    {"A": "Excludes the President, which is false under Art. 79.", "B": "Correct. President + Council of States + House of the People.", "C": "Prime Minister is not an independent organ in Art. 79.", "D": "Judiciary is separate under separation of powers."},
    "Easy", "Article 79", "Recall constitutional composition of Parliament."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-002", "ch-10", "top-const-10-01",
    "Under Article 80(1)(a), how many members are nominated to the Council of States (Rajya Sabha) by the President?",
    ["Two members", "Ten members", "Twelve members", "Fourteen members"],
    2,
    "Article 80(1)(a) provides that the Council of States shall consist of twelve (12) members nominated by the President having special knowledge or practical experience in Literature, Science, Art, and Social Service.",
    {"A": "Two was formerly Anglo-Indians in Lok Sabha (omitted by 104th CAA).", "B": "Ten is incorrect.", "C": "Correct. Twelve members nominated by President.", "D": "Fourteen is incorrect."},
    "Easy", "Article 80(1)(a)", "Recall number of nominated members in Rajya Sabha."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-003", "ch-10", "top-const-10-01",
    "Which four fields of excellence qualify individuals for presidential nomination to the Rajya Sabha under Article 80(3)?",
    ["Literature, Science, Art, and Social Service", "Literature, Science, Sports, and Law", "Art, Journalism, Economics, and Social Work", "Science, Technology, Administration, and Education"],
    0,
    "Article 80(3) specifies exactly four categories: (1) Literature; (2) Science; (3) Art; and (4) Social Service (mnemonic: LSAS). Sports is not a separate category, though sports personalities like Sachin Tendulkar have been nominated under 'Art/Special pursuit'.",
    {"A": "Correct. Literature, Science, Art, and Social Service (LSAS).", "B": "Sports and Law are not listed in Art. 80(3).", "C": "Journalism/Economics are not distinct categories.", "D": "Administration is not listed."},
    "Medium", "Article 80(3)", "Identify four nomination fields under Article 80(3)."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-004", "ch-10", "top-const-10-01",
    "What is the maximum permissible gap between two sessions of Parliament under Article 85(1)?",
    ["Three months", "Four months", "Six months", "One year"],
    2,
    "Article 85(1) mandates that the President shall summon each House to meet such that 'six months shall not intervene between its last sitting in one session and the date appointed for its first sitting in the next session'.",
    {"A": "Three months is incorrect.", "B": "Four months is incorrect.", "C": "Correct. Six months maximum gap.", "D": "One year is incorrect."},
    "Easy", "Article 85(1)", "Recall maximum inter-session gap under Article 85."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-005", "ch-10", "top-const-10-01",
    "What is the constitutional Quorum required to constitute a meeting of either House of Parliament under Article 100(3)?",
    ["One-fifth of the total number of members", "One-tenth of the total number of members of the House", "One-third of members present and voting", "Fifty members in Lok Sabha and twenty in Rajya Sabha"],
    1,
    "Article 100(3) provides: 'Until Parliament by law otherwise provides, the quorum to constitute a meeting of either House of Parliament shall be one-tenth of the total number of members of the House'.",
    {"A": "One-fifth is incorrect.", "B": "Correct. One-tenth (10%) of total membership.", "C": "One-third is incorrect.", "D": "Fixed counts are not the constitutional rule."},
    "Easy", "Article 100(3)", "Recall constitutional quorum of Parliament."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-006", "ch-10", "top-const-10-01",
    "When does the Speaker of the Lok Sabha exercise a vote in parliamentary proceedings under Article 100(1)?",
    ["In the first instance on every government bill", "Only in the case of an equality of votes (Casting Vote)", "Whenever a constitutional amendment is voted upon", "Never under any circumstances"],
    1,
    "Article 100(1) explicitly provides that the Speaker or person acting as such 'shall not vote in the first instance, but shall have and exercise a casting vote in the case of an equality of votes'.",
    {"A": "Speaker does not vote in first instance.", "B": "Correct. Exercises casting vote only in case of a tie.", "C": "No first instance vote on amendments.", "D": "Has casting vote."},
    "Easy", "Article 100(1)", "Recall Speaker's casting vote rule."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-007", "ch-10", "top-const-10-01",
    "When the Lok Sabha is dissolved, what happens to the office of the Speaker under Article 94?",
    ["The Speaker vacates office immediately upon dissolution", "The Speaker does not vacate his office until immediately before the first meeting of the House of the People after dissolution", "The Deputy Speaker takes over as Acting Speaker", "The President assumes the powers of Speaker"],
    1,
    "The second proviso to Article 94 explicitly states: 'Provided further that, whenever the House of the People is dissolved, the Speaker shall not vacate his office until immediately before the first meeting of the House of the People after the dissolution'.",
    {"A": "Speaker continues despite dissolution.", "B": "Correct. Continues until immediately before first meeting of new Lok Sabha.", "C": "Deputy Speaker does not automatically replace.", "D": "President does not assume Speaker powers."},
    "Medium", "Article 94, Second Proviso", "Master tenure of Speaker upon dissolution."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-008", "ch-10", "top-const-10-01",
    "Who decides whether a Member of Parliament has become subject to any disqualification under Article 102(1)?",
    ["The Speaker or Chairman of the House in his sole discretion", "The President of India, acting in accordance with the opinion of the Election Commission of India", "The Supreme Court of India", "A Parliamentary Privileges Committee"],
    1,
    "Under Article 103, if any question arises whether an MP has become disqualified under Article 102(1), the question is referred to the President whose decision is final; and the President SHALL obtain the opinion of the Election Commission and act according to such opinion.",
    {"A": "Speaker decides 10th Schedule defection, not Art. 102 disqualification.", "B": "Correct. President acts on binding opinion of Election Commission.", "C": "Supreme Court does not decide initially.", "D": "Committee has no statutory decision power."},
    "Medium", "Article 103", "Distinguish Article 103 disqualification from Tenth Schedule."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-009", "ch-10", "top-const-10-01",
    "The nomination of two Anglo-Indian members to the Lok Sabha by the President under Article 331 was discontinued by which Constitutional Amendment?",
    ["101st Amendment Act, 2016", "102nd Amendment Act, 2018", "103rd Amendment Act, 2019", "104th Amendment Act, 2019"],
    3,
    "The 104th Constitutional Amendment Act, 2019 extended reservation for SCs and STs in Lok Sabha and State Assemblies for another 10 years (until 2030), but chose NOT to extend the reservation/nomination of Anglo-Indians under Articles 331 and 333, effectively bringing it to an end.",
    {"A": "101st was GST.", "B": "102nd was NCBC.", "C": "103rd was EWS.", "D": "Correct. 104th Amendment Act, 2019 discontinued Anglo-Indian nomination."},
    "Easy", "104th Constitutional Amendment Act, 2019", "Recall abolition of Anglo-Indian nominations."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-010", "ch-10", "top-const-10-01",
    "Under Article 83(2), what is the normal duration of the House of the People (Lok Sabha), and how can it be extended during a National Emergency?",
    ["4 years; cannot be extended", "5 years; can be extended by Parliament by law for a period not exceeding one year at a time and not extending beyond 6 months after emergency ceases", "6 years; can be extended by 2 years", "Permanent body not subject to dissolution"],
    1,
    "Article 83(2) sets Lok Sabha duration at five years from the date of its first meeting. During a Proclamation of Emergency, Parliament may by law extend this period for not exceeding one year at a time, and not extending in any case beyond six months after the Proclamation has ceased to operate.",
    {"A": "4 years is US presidential cycle.", "B": "Correct. 5 years; extendable by 1 year at a time during emergency.", "C": "6 years is Rajya Sabha term.", "D": "Permanent body is Rajya Sabha."},
    "Medium", "Article 83(2) Proviso", "Recall extension of Lok Sabha term during emergency."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-011", "ch-10", "top-const-10-01",
    "What is the minimum age qualification for a citizen to be chosen as a member of the Council of States (Rajya Sabha) and House of the People (Lok Sabha) respectively under Article 84?",
    ["25 years for Rajya Sabha and 21 years for Lok Sabha", "30 years for Rajya Sabha and 25 years for Lok Sabha", "35 years for Rajya Sabha and 30 years for Lok Sabha", "21 years for both Houses"],
    1,
    "Under Article 84(b), the minimum age qualification is not less than thirty (30) years in the case of the Council of States (Rajya Sabha) and not less than twenty-five (25) years in the case of the House of the People (Lok Sabha).",
    {"A": "Incorrect age mix.", "B": "Correct. 30 years for Rajya Sabha; 25 years for Lok Sabha.", "C": "35 years is for President/VP.", "D": "21 years is for Panchayats."},
    "Easy", "Article 84(b)", "Recall age qualifications for Parliament."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-012", "ch-10", "top-const-10-01",
    "In Lily Thomas v. Union of India (2013), the Supreme Court struck down Section 8(4) of the Representation of the People Act, 1951, resulting in:",
    ["Automatic and immediate disqualification of any sitting MP or MLA upon conviction for an offence carrying a sentence of two years or more", "Extension of protection for 3 months to convicted legislators", "A requirement that only the Speaker can disqualify a convicted MP", "Immunity from arrest inside Parliament"],
    0,
    "In Lily Thomas (2013), the Supreme Court struck down Section 8(4) of RPA 1951 (which had shielded sitting MPs/MLAs from immediate disqualification pending appeal for 3 months), holding that under Article 102(1)(e), disqualification is instantaneous and automatic upon conviction.",
    {"A": "Correct. Automatic immediate disqualification upon 2+ years conviction.", "B": "3-month protection was struck down as unconstitutional.", "C": "Disqualification operates automatically by law.", "D": "Arrest immunity applies to civil cases only."},
    "Medium", "Lily Thomas v. Union of India (2013) 7 SCC 653", "Master Lily Thomas immediate disqualification ratio."
))

# 10-13 to 10-24: Legislative Procedures, Money Bills & Joint Sittings (Arts 107–117)
MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-013", "ch-10", "top-const-10-02",
    "Under Article 108, which of the following is a condition precedent for the President to notify his intention to summon a Joint Sitting of Parliament?",
    ["A Bill passed by one House is rejected by the other House", "The Houses have finally disagreed as to the amendments to be made in the Bill", "More than six months elapse from the date of the reception of the Bill by the other House without the Bill being passed", "Any of the above three deadlock conditions"],
    3,
    "Article 108(1) authorizes the President to notify a Joint Sitting if after an Ordinary Bill has been passed by one House and transmitted: (a) the other House rejects it; or (b) Houses have finally disagreed on amendments; or (c) more than 6 months elapse without it being passed.",
    {"A": "True under Art. 108(1)(a).", "B": "True under Art. 108(1)(b).", "C": "True under Art. 108(1)(c).", "D": "Correct. Any of the above three deadlock conditions."},
    "Easy", "Article 108(1)", "Recall triggers for Joint Sitting."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-014", "ch-10", "top-const-10-02",
    "Who presides over a Joint Sitting of both Houses of Parliament summoned under Article 108?",
    ["The President of India", "The Chairman of the Rajya Sabha (Vice-President)", "The Speaker of the Lok Sabha (or in his absence, Deputy Speaker, or Deputy Chairman of Rajya Sabha)", "The Prime Minister"],
    2,
    "Under Article 118(4), the Speaker of the House of the People presides over a Joint Sitting. In the Speaker's absence, the Deputy Speaker presides; in his absence, the Deputy Chairman of Rajya Sabha presides. The Chairman of Rajya Sabha (Vice-President) NEVER presides because he is not a member of Parliament.",
    {"A": "President summons joint sitting, but does not preside.", "B": "Chairman of Rajya Sabha NEVER presides.", "C": "Correct. Speaker of Lok Sabha presides.", "D": "Prime Minister is member of cabinet."},
    "Easy", "Article 118(4)", "Recall presiding officer of Joint Sitting."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-015", "ch-10", "top-const-10-02",
    "For which categories of Bills is the provision of a Joint Sitting under Article 108 completely UNAVAILABLE?",
    ["Ordinary Bills and Financial Bills", "Money Bills (Article 109) and Constitution Amendment Bills (Article 368)", "Bills creating new States under Article 3", "Bills repealing colonial statutes"],
    1,
    "A Joint Sitting CANNOT be summoned for: (1) Money Bills (under Article 109, Rajya Sabha has no veto and Lok Sabha overrides after 14 days); and (2) Constitution Amendment Bills (under Article 368, each House must pass the bill separately with special majority).",
    {"A": "Ordinary and Financial bills can have joint sittings.", "B": "Correct. Money Bills and Constitution Amendment Bills.", "C": "Article 3 bills can have joint sittings as ordinary bills.", "D": "Repealing bills can have joint sittings."},
    "Easy", "Articles 108, 109, 368", "Identify bills excluded from Joint Sittings."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-016", "ch-10", "top-const-10-02",
    "How many times has a Joint Sitting of both Houses of Parliament been convened in Indian constitutional history so far?",
    ["Never", "Once", "Three times", "Seven times"],
    2,
    "A Joint Sitting has been convened exactly THREE times in history to resolve legislative deadlocks: (1) Dowry Prohibition Bill, 1960 (held in 1961); (2) Banking Service Commission (Repeal) Bill, 1977 (held in 1978); and (3) Prevention of Terrorism Bill, 2002 (POTA, held in 2002).",
    {"A": "It has been convened.", "B": "More than once.", "C": "Correct. Exactly three times (1961, 1978, 2002).", "D": "Seven is incorrect."},
    "Medium", "Joint Sitting Historical Precedents", "Recall number of Joint Sittings held in India."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-017", "ch-10", "top-const-10-02",
    "Under Article 109, where can a Money Bill be introduced?",
    ["In either House of Parliament", "Only in the Council of States (Rajya Sabha)", "Only in the House of the People (Lok Sabha) on the prior recommendation of the President", "Only in a Joint Sitting"],
    2,
    "Article 109(1) provides: 'A Money Bill shall not be introduced in the Council of States'. Under Article 117(1), it can only be introduced in the Lok Sabha on the recommendation of the President.",
    {"A": "Cannot originate in Rajya Sabha.", "B": "Directly contradicted by Art. 109(1).", "C": "Correct. Only in Lok Sabha on President's recommendation.", "D": "Bills cannot originate in joint sittings."},
    "Easy", "Article 109(1)", "Recall rule of origin for Money Bills."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-018", "ch-10", "top-const-10-02",
    "Within what period must the Rajya Sabha return a Money Bill to the Lok Sabha under Article 109(2)?",
    ["Seven days", "Fourteen days", "One month", "Six weeks"],
    1,
    "Article 109(2) mandates that Rajya Sabha must return the Money Bill to the Lok Sabha with its recommendations within a period of FOURTEEN (14) DAYS from the date of its receipt.",
    {"A": "Seven days is incorrect.", "B": "Correct. Fourteen (14) days.", "C": "One month applies to Art. 352 emergency.", "D": "Six weeks applies to ordinances."},
    "Easy", "Article 109(2)", "Recall 14-day rule for Money Bills in Rajya Sabha."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-019", "ch-10", "top-const-10-02",
    "If the Rajya Sabha does not return a Money Bill within 14 days, what is the constitutional consequence?",
    ["The Bill lapses automatically", "It is deemed to have been passed by both Houses at the expiration of 14 days in the form in which it was passed by the Lok Sabha", "The President must summon a Joint Sitting", "The Prime Minister must resubmit it"],
    1,
    "Under Article 109(5), if a Money Bill is not returned to the Lok Sabha within 14 days, it shall be deemed to have been passed by both Houses at the expiration of that period in the form in which it was passed by the Lok Sabha.",
    {"A": "Money bills never lapse in this manner.", "B": "Correct. Deemed passed by both Houses in Lok Sabha's form.", "C": "No joint sitting for Money Bills.", "D": "No resubmission required."},
    "Easy", "Article 109(5)", "Master deemed passage of Money Bills."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-020", "ch-10", "top-const-10-02",
    "Under Article 110(3), whose decision is final on the question whether a Bill is or is not a Money Bill?",
    ["The President of India", "The Speaker of the House of the People (Lok Sabha)", "The Chairman of the Council of States", "The Finance Minister"],
    1,
    "Article 110(3) provides: 'If any question arises whether a Bill is a Money Bill or not, the decision of the Speaker of the House of the People thereon shall be final'. The Speaker signs a certificate to that effect.",
    {"A": "President recommends, but Speaker certifies.", "B": "Correct. Speaker of the House of the People.", "C": "Chairman of RS has no certification power.", "D": "Finance Minister introduces, but does not certify."},
    "Easy", "Article 110(3)", "Recall Speaker's finality on Money Bill certificate."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-021", "ch-10", "top-const-10-02",
    "In K.S. Puttaswamy (Aadhaar-5J.) v. Union of India (2018), the Supreme Court ruled regarding the Speaker's certificate under Article 110(3) that:",
    ["The Speaker's decision is absolute and totally immune from judicial review under Article 122", "The Speaker's certification is subject to judicial review if it amounts to a colourable exercise of power or substantive constitutional infraction", "The certificate must be countersigned by the Chief Justice of India", "Money Bills cannot be enacted without state ratification"],
    1,
    "In the Aadhaar Case (2018), the 5-Judge Constitution Bench held that the finality attached to the Speaker's certificate under Article 110(3) does not oust judicial review; while procedural irregularities are protected by Art. 122, substantive constitutional violations are reviewable by the Court.",
    {"A": "Absolute immunity was rejected.", "B": "Correct. Subject to judicial review for substantive constitutional infractions.", "C": "CJI countersignature is non-existent.", "D": "State ratification does not apply."},
    "Hard", "Aadhaar Judgment (2019) 1 SCC 1", "Master judicial review of Speaker's Money Bill certificate."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-022", "ch-10", "top-const-10-02",
    "Which of the following matters is EXPLICITLY excluded from the definition of a Money Bill under Article 110(2)?",
    ["Imposition, abolition, remission, alteration or regulation of any tax", "The borrowing of money by the Government of India", "The imposition of fines, penalties, license fees, or local taxes levied by local authorities for local purposes", "The custody of the Consolidated Fund of India"],
    2,
    "Article 110(2) explicitly provides that a Bill shall NOT be deemed a Money Bill by reason only that it provides for the imposition of fines or other pecuniary penalties, or for the demand or payment of fees for licences or services, or for the imposition/alteration of any tax by any local authority or body for local purposes.",
    {"A": "Taxation is core Money Bill matter under Art. 110(1)(a).", "B": "Borrowing is Money Bill matter under Art. 110(1)(b).", "C": "Correct. Fines, licence fees, and local taxes are explicitly excluded under Art. 110(2).", "D": "Consolidated Fund custody is core Money Bill matter under Art. 110(1)(c)."},
    "Medium", "Article 110(2)", "Identify matters excluded from Money Bill definition."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-023", "ch-10", "top-const-10-02",
    "What action can the President take when an Ordinary Bill is presented to him under Article 111?",
    ["Assent to the Bill", "Declare that he withholds assent to the Bill", "Return the Bill with a message requesting reconsideration, provided that if passed again by both Houses with or without amendment, he MUST give assent", "Any of the above three actions"],
    3,
    "Under Article 111, the President has three options: (1) declare assent; (2) withhold assent; or (3) return the bill (if not a Money Bill) for reconsideration. If the Houses pass the bill again with or without amendment, the President 'shall not withhold assent therefrom'.",
    {"A": "Option under Art. 111.", "B": "Option under Art. 111.", "C": "Option under Art. 111 proviso (suspensive veto).", "D": "Correct. Any of the above three actions."},
    "Easy", "Article 111", "Recall Presidential options on presentation of Ordinary Bills."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-024", "ch-10", "top-const-10-02",
    "Can the President return a Money Bill for the reconsideration of Parliament under Article 111?",
    ["Yes, once", "No, the President cannot return a Money Bill; he must either give assent or withhold assent", "Yes, with the consent of the Speaker", "Only if the Rajya Sabha recommends it"],
    1,
    "Article 111 explicitly excludes Money Bills from the return power: 'Provided that the President may, as soon as possible after the presentation to him of a Bill for assent, IF IT IS NOT A MONEY BILL, return the Bill...'. Since Money Bills are introduced on prior presidential recommendation, returning them is barred.",
    {"A": "Cannot return Money Bills.", "B": "Correct. Cannot return a Money Bill; must either assent or withhold.", "C": "Speaker consent does not change Art. 111.", "D": "RS recommendation is immaterial."},
    "Medium", "Article 111 Proviso", "Recall prohibition on returning Money Bills."
))

# 10-25 to 10-35: Financial Procedures, Privileges & Committees (Arts 105, 112–116)
MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-025", "ch-10", "top-const-10-03",
    "What is the official constitutional term for the 'Budget' under Article 112?",
    ["Union Financial Plan", "Annual Financial Statement", "Consolidated Revenue Estimate", "National Appropriation Statement"],
    1,
    "The Constitution nowhere uses the word 'Budget'. Article 112 refers to it officially as the 'Annual Financial Statement', which is caused to be laid before both Houses of Parliament by the President in respect of every financial year.",
    {"A": "Colloquial term.", "B": "Correct. Annual Financial Statement.", "C": "Fictional term.", "D": "Fictional term."},
    "Easy", "Article 112(1)", "Recall official constitutional term for Budget."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-026", "ch-10", "top-const-10-03",
    "Under Article 113, what is the constitutional difference between 'Expenditure Charged' on the Consolidated Fund and 'Other Expenditure'?",
    ["Charged expenditure is not discussed in Parliament", "Charged expenditure can be discussed in both Houses but is NOT submitted to the vote of Parliament; other expenditure is voted upon by Lok Sabha in the form of Demands for Grants", "Charged expenditure must be voted by Rajya Sabha", "Charged expenditure is audited by the Prime Minister"],
    1,
    "Under Article 113(1), expenditure charged upon the Consolidated Fund of India can be discussed in either House of Parliament, but is NOT submitted to the vote of Parliament. Other expenditure is submitted in the form of Demands for Grants to the Lok Sabha only.",
    {"A": "Charged expenditure CAN be discussed.", "B": "Correct. Discussed in both Houses, but not voted upon.", "C": "Rajya Sabha never votes on demands for grants.", "D": "Audited by CAG."},
    "Medium", "Article 113(1) & (2)", "Distinguish charged expenditure from voted expenditure."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-027", "ch-10", "top-const-10-03",
    "Which of the following is CHARGED upon the Consolidated Fund of India under Article 112(3)?",
    ["Salaries and allowances of Supreme Court Judges and CAG", "Pensions of High Court Judges", "Emoluments and allowances of the President and debt charges of the Government of India", "All of the above expenditures"],
    3,
    "Article 112(3) lists charged expenditures: President's emoluments, Chairman/Deputy Chairman RS and Speaker/Deputy Speaker LS salaries, debt charges, Supreme Court judges' salaries/pensions, CAG's salary/pension, High Court judges' PENSIONS (salaries are on State funds), and any sum required to satisfy any court decree.",
    {"A": "True under Art. 112(3)(d) & (e).", "B": "True under Art. 112(3)(d)(iii).", "C": "True under Art. 112(3)(a) & (c).", "D": "Correct. All of the above expenditures are charged on CFI."},
    "Medium", "Article 112(3)", "Recall charged expenditures under Article 112(3)."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-028", "ch-10", "top-const-10-03",
    "Where are the SALARIES and PENSIONS of High Court Judges charged respectively?",
    ["Both on the Consolidated Fund of India", "Both on the Consolidated Fund of the State", "Salaries are charged on the Consolidated Fund of the STATE, while Pensions are charged on the Consolidated Fund of INDIA", "Salaries on Union, Pensions on State"],
    2,
    "Under Article 202(3)(d), the salaries and allowances of High Court judges are charged on the Consolidated Fund of the concerned STATE; but under Article 112(3)(d)(iii), the PENSIONS payable to High Court judges are charged on the Consolidated Fund of INDIA.",
    {"A": "Incorrect distribution.", "B": "Incorrect (pensions are on India).", "C": "Correct. Salaries on State Fund; Pensions on India Fund.", "D": "Reversed distribution."},
    "Hard", "Articles 112(3)(d)(iii) & 202(3)(d)", "Prelims Trap: HC Judges Salaries vs Pensions."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-029", "ch-10", "top-const-10-03",
    "No money can be withdrawn from the Consolidated Fund of India except under appropriation made by law under which Article?",
    ["Article 112", "Article 113", "Article 114 (Appropriation Act)", "Article 115"],
    2,
    "Article 114(3) provides: 'Subject to the provisions of articles 115 and 116, no money shall be withdrawn from the Consolidated Fund of India except under appropriation made by law passed in accordance with the provisions of this article'.",
    {"A": "Article 112 is annual statement estimates.", "B": "Article 113 is voting of demands.", "C": "Correct. Article 114 Appropriation Act.", "D": "Article 115 is supplementary grants."},
    "Easy", "Article 114(3)", "Recall Article 114 Appropriation Act."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-030", "ch-10", "top-const-10-03",
    "What is a 'Vote on Account' under Article 116(1)(a)?",
    ["A vote of no confidence against the government", "A grant in advance made by the Lok Sabha to meet estimated expenditure for a part of the financial year pending the completion of the budgetary process and passage of the Appropriation Bill", "A loan taken from the Reserve Bank of India", "An extraordinary grant for war"],
    1,
    "Article 116(1)(a) empowers the House of the People to make a grant in advance in respect of the estimated expenditure for a part of any financial year pending the voting of demands and the passing of the Appropriation Act. It is normally granted for two months for an amount equivalent to one-sixth of total estimates.",
    {"A": "Vote of no-confidence is under Rule 198.", "B": "Correct. Advance grant pending budget completion.", "C": "Ways and means advances are RBI loans.", "D": "Vote of credit is for war (Art. 116(1)(b))."},
    "Medium", "Article 116(1)(a)", "Define Vote on Account under Article 116."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-031", "ch-10", "top-const-10-03",
    "Under Article 105(2), what immunity is conferred upon a Member of Parliament?",
    ["Immunity from civil and criminal arrest for life", "No MP is liable to any proceedings in any court in respect of anything said or any vote given by him in Parliament or any committee thereof", "Immunity from income tax on parliamentary salary", "Immunity from traffic laws in New Delhi"],
    1,
    "Article 105(2) provides: 'No member of Parliament shall be liable to any proceedings in any court in respect of anything said or any vote given by him in Parliament or any committee thereof, and no person shall be so liable in respect of the publication by or under the authority of either House of Parliament of any report, paper, votes or proceedings'.",
    {"A": "Arrest immunity applies only to civil arrest 40 days before/after sessions (s. 135A CPC).", "B": "Correct. Complete speech and voting immunity in courts.", "C": "Taxation applies normally.", "D": "Traffic laws apply normally."},
    "Easy", "Article 105(2)", "Recall Article 105(2) parliamentary speech immunity."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-032", "ch-10", "top-const-10-03",
    "In Sita Soren v. Union of India (2024), a 7-Judge Constitution Bench unanimously overruled P.V. Narasimha Rao (1998) and held that:",
    ["Legislators taking bribes to vote or make speeches in the House enjoy absolute constitutional immunity under Articles 105(2) and 194(2)", "Articles 105(2) and 194(2) do NOT protect legislators who accept bribes for making a speech or casting a vote from criminal prosecution under the Prevention of Corruption Act", "Bribery can only be penalized by the Speaker", "Immunity applies if the vote was actually cast as promised"],
    1,
    "In Sita Soren (March 2024), a unanimous 7-Judge Bench headed by CJI D.Y. Chandrachud held that parliamentary privilege under Article 105(2)/194(2) is aimed at protecting fearless democratic deliberation, not shielding corruption. The offence of bribery is complete the moment the bribe is accepted, irrespective of whether the vote or speech is delivered.",
    {"A": "Overruled 1998 majority ruling.", "B": "Correct. Overruled P.V. Narasimha Rao; no immunity for bribery.", "C": "Criminal courts have jurisdiction.", "D": "Performance of corrupt bargain is irrelevant."},
    "Hard", "Sita Soren v. Union of India (2024) 5 SCC 625", "Master 2024 Sita Soren parliamentary bribery judgment."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-033", "ch-10", "top-const-10-03",
    "What is the total membership and composition of the Public Accounts Committee (PAC)?",
    ["15 members, all from Lok Sabha", "22 members (15 from Lok Sabha and 7 from Rajya Sabha)", "30 members, all from Lok Sabha", "25 members (20 Lok Sabha and 5 Rajya Sabha)"],
    1,
    "The Public Accounts Committee consists of 22 members: 15 elected by Lok Sabha and 7 elected by Rajya Sabha from amongst their members according to the principle of proportional representation by single transferable vote. A Minister cannot be elected to the Committee.",
    {"A": "15 members was pre-1954 count before Rajya Sabha was associated.", "B": "Correct. 22 members (15 Lok Sabha + 7 Rajya Sabha).", "C": "30 members is the Estimates Committee.", "D": "25 members is incorrect."},
    "Easy", "Public Accounts Committee Composition", "Recall PAC composition and strength."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-034", "ch-10", "top-const-10-03",
    "Which is the LARGEST parliamentary committee of the Indian Parliament, and from which House are all its members drawn?",
    ["Public Accounts Committee (22 members)", "Estimates Committee (30 members, drawn EXCLUSIVELY from the Lok Sabha)", "Committee on Public Undertakings (22 members)", "Departmentally Related Standing Committees (31 members)"],
    1,
    "The Estimates Committee is the largest committee of Parliament, consisting of 30 members. All 30 members are elected exclusively from the Lok Sabha; the Rajya Sabha has NO representation in the Estimates Committee.",
    {"A": "PAC has 22 members.", "B": "Correct. Estimates Committee (30 members, exclusively from Lok Sabha).", "C": "COPU has 22 members.", "D": "DRSCs have 31 members each, but split between LS and RS."},
    "Medium", "Estimates Committee Composition", "Identify largest committee and its exclusive Lok Sabha character."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-10-035", "ch-10", "top-const-10-03",
    "By established parliamentary convention since 1967, who is appointed as the Chairman of the Public Accounts Committee (PAC)?",
    ["The Prime Minister", "The Minister of Finance", "A prominent member of the Opposition party appointed by the Speaker", "The senior-most member of the Rajya Sabha"],
    2,
    "The Chairman of the PAC is appointed by the Speaker of the Lok Sabha from amongst its members. Since 1967, an unbroken convention has developed whereby the Chairman of the PAC is invariably selected from the Opposition, ensuring non-partisan scrutiny of executive expenditure.",
    {"A": "Ministers are barred from being members.", "B": "Finance Minister cannot be a member.", "C": "Correct. Opposition member appointed by the Speaker.", "D": "Chairman must be a Lok Sabha member."},
    "Medium", "PAC Convention", "Recall Opposition Chairman convention in PAC."
))

print(f"Chapter 10 complete ({len(MCQS_CH09_11)} total).")

# ==============================================================================
# CHAPTER 11: STATE GOVERNMENT & LOCAL GOVERNANCE (30 MCQs)
# ==============================================================================
# 11-01 to 11-08: The Governor
MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-001", "ch-11", "top-const-11-01",
    "Under Article 153 proviso (inserted by 7th Amendment, 1956), can the same person be appointed Governor of two or more States?",
    ["No, each State must have a separate Governor", "Yes, nothing in Article 153 prevents the appointment of the same person as Governor for two or more States", "Only during an emergency", "Only with the approval of both State Assemblies"],
    1,
    "The proviso to Article 153 explicitly provides: 'Provided that nothing in this article shall prevent the appointment of the same person as Governor for two or more States'.",
    {"A": "Initial 1950 rule, modified in 1956.", "B": "Correct. Permitted by 7th Amendment proviso.", "C": "Not limited to emergency.", "D": "State Assemblies do not vote on appointment."},
    "Easy", "Article 153 Proviso", "Recall Article 153 dual governorship proviso."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-002", "ch-11", "top-const-11-01",
    "Under Article 156(1), the Governor of a State holds office during:",
    ["A fixed immutable tenure of 5 years", "The pleasure of the Chief Minister", "The pleasure of the President", "Good behaviour certified by the High Court"],
    2,
    "Article 156(1) provides: 'The Governor shall hold office during the pleasure of the President'. Under Article 156(3), subject to the pleasure of the President, the term is five years.",
    {"A": "Subject to pleasure of President.", "B": "Chief Minister has no removal power.", "C": "Correct. Holds office during the pleasure of the President.", "D": "High Court has no removal role."},
    "Easy", "Article 156(1)", "Recall tenure of Governor."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-003", "ch-11", "top-const-11-01",
    "In B.P. Singhal v. Union of India (2010), a 5-Judge Constitution Bench ruled on the removal of Governors under Article 156(1) that:",
    ["The President has unlimited discretion to dismiss a Governor without any reason or restraint", "The President can remove a Governor without assigning reasons, but the power cannot be exercised arbitrarily, capriciously, or on the ground of change of political party in power at the Centre", "Governors can only be impeached by the State Assembly", "Governors have fixed 5-year tenure that cannot be terminated prematurely"],
    1,
    "In B.P. Singhal (2010), the Supreme Court settled that while the President need not assign reasons in the removal order, the 'pleasure doctrine' under Article 156(1) is not unfettered; removal cannot be arbitrary, whimsical, or based on political difference with the Centre, and is subject to judicial review.",
    {"A": "Arbitrary power rejected.", "B": "Correct. Cannot be removed arbitrarily or on political party change.", "C": "Assembly cannot impeach Governor.", "D": "No absolute security of tenure."},
    "Medium", "B.P. Singhal v. Union of India (2010) 6 SCC 331", "Master B.P. Singhal Governor removal doctrine."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-004", "ch-11", "top-const-11-01",
    "In State of Punjab v. Principal Secretary to Governor (2023), the Supreme Court ruled regarding the Governor's powers under Article 200 that:",
    ["The Governor has an absolute pocket veto and can sit on state bills indefinitely", "If the Governor decides to withhold assent to an ordinary bill, he MUST return the bill forthwith to the State Legislature with a message for reconsideration", "The Governor must send all bills to the Supreme Court", "The Governor can unilaterally amend state bills"],
    1,
    "In State of Punjab (November 2023), Chief Justice D.Y. Chandrachud held that the Governor cannot kill legislation by indefinitely withholding assent; withholding assent under Article 200 is inextricably coupled with returning the bill to the Legislature for reconsideration forthwith. If passed again, the Governor has no choice but to assent.",
    {"A": "Pocket veto was declared unconstitutional.", "B": "Correct. Withholding assent mandates returning the bill forthwith.", "C": "Cannot refer to SC directly.", "D": "Governor cannot amend bills."},
    "Hard", "State of Punjab v. Principal Secretary (2023) SCC OnLine SC 1471", "Master 2023 Governor assent judgment."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-005", "ch-11", "top-const-11-01",
    "Under Article 200, when is the Governor constitutionally OBLIGATED to reserve a State bill for the consideration of the President?",
    ["Whenever the Chief Minister is from an opposition party", "When the bill in the Governor's opinion so derogates from the powers of the High Court as to endanger the position which that court is designed to fill", "Whenever the bill levies a state tax", "Whenever the bill deals with local panchayats"],
    1,
    "The second proviso to Article 200 makes reservation mandatory in one specific case: 'Provided further that the Governor shall not assent to, but shall reserve for the consideration of the President, any Bill which in the opinion of the Governor would, if it became law, so derogate from the powers of the High Court as to endanger the position which that Court is by this Constitution designed to fill'.",
    {"A": "Political grounds are unconstitutional.", "B": "Correct. Mandatory if bill endangers constitutional position of High Court.", "C": "State taxation is within State List.", "D": "Panchayat bills do not require reservation."},
    "Medium", "Article 200, Second Proviso", "Identify mandatory bill reservation under Article 200."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-006", "ch-11", "top-const-11-01",
    "In Nabam Rebia v. Deputy Speaker, Arunachal Pradesh (2016), a 5-Judge Constitution Bench held regarding the Governor's discretionary powers under Article 163 that:",
    ["The Governor has unfettered discretion to summon or prorogue the Assembly contrary to cabinet advice", "The Governor's discretionary powers under Article 163 are strictly limited to constitutional mandates; the Governor cannot summon or prepone assembly sessions without the aid and advice of the Chief Minister and Cabinet", "The Governor is the supreme ruler of the State", "The Governor's discretion cannot be reviewed by courts"],
    1,
    "In Nabam Rebia (2016), the Supreme Court ruled that Article 163 does not give the Governor a general dispensing power; the Governor must act on cabinet advice in summoning or proroguing the House unless the government has demonstrably lost its majority on the floor of the House.",
    {"A": "Unfettered discretion rejected.", "B": "Correct. Must summon/prorogue on cabinet advice; discretion is strictly bounded.", "C": "Constitutional head, not supreme ruler.", "D": "Discretion is fully reviewable."},
    "Medium", "Nabam Rebia (2016) 8 SCC 1", "Master Nabam Rebia gubernatorial discretion limits."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-007", "ch-11", "top-const-11-01",
    "Under Article 213, an Ordinance promulgated by the Governor ceases to operate at the expiration of what period from the reassembly of the State Legislature?",
    ["Two weeks", "Four weeks", "Six weeks", "Three months"],
    2,
    "Article 213(2)(a) provides that an Ordinance promulgated by the Governor shall cease to operate at the expiration of SIX WEEKS from the reassembly of the Legislature of the State, or earlier if disapproved by resolutions of the Legislature.",
    {"A": "Two weeks is incorrect.", "B": "Four weeks is incorrect.", "C": "Correct. Six weeks from reassembly.", "D": "Three months is incorrect."},
    "Easy", "Article 213(2)(a)", "Recall 6-week expiry rule for State Ordinances."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-008", "ch-11", "top-const-11-01",
    "Under the proviso to Article 213(1), when does the Governor require prior instructions from the President before promulgating an Ordinance?",
    ["If a Bill containing the same provisions would have required previous presidential sanction under the Constitution", "If he would have deemed it necessary to reserve a Bill containing the same provisions for the President", "If an Act of the State Legislature containing the same provisions would have been invalid without presidential assent", "In all of the above three circumstances"],
    3,
    "Article 213(1) proviso mandates prior Presidential instructions in three cases: (a) if bill would have required prior sanction; (b) if bill would have been reserved for President; or (c) if an Act would have been void without presidential assent (e.g. repugnancy under Art. 254(2)).",
    {"A": "True under Art. 213(1)(a).", "B": "True under Art. 213(1)(b).", "C": "True under Art. 213(1)(c).", "D": "Correct. In all of the above three circumstances."},
    "Medium", "Article 213(1) Proviso", "Recall presidential instruction triggers for State Ordinances."
))

# 11-09 to 11-16: State Legislature & Advocate-General
MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-009", "ch-11", "top-const-11-02",
    "Under Article 169, how can a Legislative Council (Vidhan Parishad) in a State be created or abolished?",
    ["By an order of the Governor", "By an Act of Parliament, if the State Legislative Assembly passes a resolution by special majority (majority of total membership + 2/3rd present and voting)", "By a constitutional amendment requiring 50% state ratification", "By a presidential ordinance"],
    1,
    "Article 169(1) provides that Parliament may by law create or abolish a Legislative Council if the Legislative Assembly of that State passes a resolution to that effect by a special majority (majority of total membership and 2/3rd present and voting). Such an Act is NOT an Article 368 amendment (Art. 169(3)).",
    {"A": "Governor cannot create councils.", "B": "Correct. Parliament enacts law following State Assembly special majority resolution.", "C": "Article 169(3) excludes Art. 368.", "D": "Cannot be done by ordinance alone."},
    "Medium", "Article 169", "Recall creation and abolition of Legislative Councils."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-010", "ch-11", "top-const-11-02",
    "What is the maximum strength of a State Legislative Council under Article 171(1)?",
    ["Equal to the Legislative Assembly", "Not more than one-third of the total number of members in the Legislative Assembly of that State (and not less than 40)", "Fixed at 100 members in all States", "Half of the Legislative Assembly"],
    1,
    "Article 171(1) provides that the total number of members in the Legislative Council shall NOT exceed one-third of the total membership of the Legislative Assembly, provided that the total number shall in no case be less than forty (40).",
    {"A": "Cannot equal Assembly.", "B": "Correct. Not more than 1/3rd of Assembly, and not less than 40.", "C": "Fixed count is incorrect.", "D": "Half is incorrect."},
    "Easy", "Article 171(1)", "Recall size limits of Legislative Council."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-011", "ch-11", "top-const-11-02",
    "Which category is explicitly included in gubernatorial nominations to the Legislative Council under Article 171(5), but is ABSENT from presidential nominations to the Rajya Sabha under Article 80(3)?",
    ["Science", "Art", "Social Service", "Co-operative Movement"],
    3,
    "Article 171(5) lists five categories for Council nominations: Literature, Science, Art, the CO-OPERATIVE MOVEMENT, and Social Service. In contrast, Article 80(3) lists only four categories, completely omitting 'Co-operative Movement'.",
    {"A": "Science is in both.", "B": "Art is in both.", "C": "Social Service is in both.", "D": "Correct. 'Co-operative Movement' is present in Council (Art. 171) but absent from RS (Art. 80)."},
    "Hard", "Article 171(5) vs 80(3)", "Prelims Trap: Co-operative movement in Council nomination."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-012", "ch-11", "top-const-11-02",
    "What is the maximum duration for which a State Legislative Council can delay an Ordinary Bill passed by the Legislative Assembly in total?",
    ["One month", "Three months", "Four months (3 months in first instance + 1 month in second instance)", "Six months"],
    2,
    "Under Article 197, the Legislative Council has only dilatory power: it can delay an ordinary bill for at most three months in the first instance, and for at most one month in the second instance (total four months), after which the bill is deemed passed by both Houses in the form passed by the Assembly.",
    {"A": "One month applies to second instance only.", "B": "Three months applies to first instance only.", "C": "Correct. Four months in total (3 months + 1 month).", "D": "Six months applies to Rajya Sabha deadlock."},
    "Medium", "Article 197", "Recall maximum dilatory period of Legislative Council."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-013", "ch-11", "top-const-11-02",
    "Is there any provision for a 'Joint Sitting' of the two Houses of a State Legislature to resolve a legislative deadlock?",
    ["Yes, convened by the Governor under Article 208", "No, the Indian Constitution does NOT provide for a Joint Sitting in State Legislatures; the Legislative Assembly has ultimate legislative supremacy", "Yes, presided over by the Advocate-General", "Yes, upon an order of the High Court"],
    1,
    "Unlike Parliament (Article 108), there is NO constitutional provision for a Joint Sitting in State Legislatures. If a deadlock arises on an ordinary bill, the Legislative Assembly simply passes the bill a second time, and the Council cannot prevent its enactment.",
    {"A": "No joint sitting in States.", "B": "Correct. No Joint Sitting in State Legislatures; Assembly is supreme.", "C": "Advocate-General cannot convene joint sessions.", "D": "High Court has no legislative role."},
    "Easy", "Article 197 & State Deadlock", "Affirm absence of Joint Sitting in States."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-014", "ch-11", "top-const-11-02",
    "Under Article 165, what qualification is required for appointment as the Advocate-General for the State?",
    ["Must be qualified to be appointed a Judge of a High Court", "Must be a retired District Judge", "Must have 20 years practice in the Supreme Court", "Must be an elected member of the Vidhan Sabha"],
    0,
    "Article 165(1) provides: 'The Governor of each State shall appoint a person who is qualified to be appointed a Judge of a High Court to be Advocate-General for the State'.",
    {"A": "Correct. Qualified to be appointed a Judge of a High Court.", "B": "District judge status alone is insufficient unless meeting HC judge criteria.", "C": "Supreme Court practice not mandatory.", "D": "Advocate-General is not an MLA."},
    "Easy", "Article 165(1)", "Recall qualifications for Advocate-General."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-015", "ch-11", "top-const-11-02",
    "What is the tenure and remuneration of the Advocate-General for the State under Article 165(3)?",
    ["Five years; salary equal to Chief Justice of High Court", "Holds office during the pleasure of the Governor; remuneration determined by the Governor", "Holds office until 62 years of age", "Tenure determined by the State Legislative Assembly"],
    1,
    "Article 165(3) provides: 'The Advocate-General shall hold office during the pleasure of the Governor, and shall receive such remuneration as the Governor may determine'.",
    {"A": "No fixed 5-year tenure.", "B": "Correct. Holds office during the pleasure of the Governor.", "C": "62 years applies to HC judges, not Advocate-General.", "D": "Assembly does not set tenure."},
    "Easy", "Article 165(3)", "Recall tenure of Advocate-General."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-016", "ch-11", "top-const-11-02",
    "Under Article 177, the Advocate-General for the State has the right to speak and take part in the proceedings of the State Legislature, but does NOT have the right to:",
    ["Address legislative committees", "Vote on any bill or motion", "Appear before the Bar of the House", "Answer questions asked by MLAs"],
    1,
    "Article 177 confers upon the Advocate-General the right to speak and take part in proceedings of the Legislature or any committee thereof, but 'shall not by virtue of this article be entitled to vote'.",
    {"A": "Can address committees.", "B": "Correct. Has NO right to vote in the State Legislature.", "C": "Can appear before the House.", "D": "Can participate in debates."},
    "Easy", "Article 177", "Recall Article 177 voting bar on Advocate-General."
))

# 11-17 to 11-23: Rural Local Governance (Panchayats - Part IX)
MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-017", "ch-11", "top-const-11-03",
    "The 73rd Constitutional Amendment Act, 1992 added which Part and Schedule to the Constitution of India?",
    ["Part VIII and Tenth Schedule", "Part IX and Eleventh Schedule", "Part IXA and Twelfth Schedule", "Part X and Ninth Schedule"],
    1,
    "The 73rd Amendment Act, 1992 added Part IX (titled 'The Panchayats', Articles 243 to 243-O) and the Eleventh Schedule (containing 29 functional subjects) to the Constitution.",
    {"A": "Part VIII is Union Territories.", "B": "Correct. Part IX and Eleventh Schedule.", "C": "Part IXA and 12th Schedule is 74th Amendment (Municipalities).", "D": "Part X is Scheduled/Tribal areas."},
    "Easy", "73rd Constitutional Amendment Act, 1992", "Identify Part and Schedule added by 73rd Amendment."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-018", "ch-11", "top-const-11-03",
    "What is a 'Gram Sabha' defined as under Article 243(b) and Article 243A?",
    ["An elected council of village elders", "A body consisting of all persons registered in the electoral rolls relating to a village comprised within the area of the Panchayat", "A meeting called by the district collector", "A committee of landholders in the village"],
    1,
    "Article 243(b) defines Gram Sabha as a body consisting of persons registered in the electoral rolls relating to a village comprised within the area of Panchayat at the village level. It is the grassroots foundation of direct democracy.",
    {"A": "Elected council is Gram Panchayat, not Gram Sabha.", "B": "Correct. Body of all registered voters in the village.", "C": "Collector does not define membership.", "D": "All adult registered electors are members."},
    "Easy", "Article 243(b) & 243A", "Define Gram Sabha."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-019", "ch-11", "top-const-11-03",
    "Under Article 243D(3), what minimum proportion of total seats in every Panchayat must be reserved for women?",
    ["Not less than one-tenth", "Not less than one-fifth", "Not less than one-third (including seats reserved for SC/ST women)", "Not less than one-half"],
    2,
    "Article 243D(3) provides: 'Not less than one-third (including the number of seats reserved for women belonging to the Scheduled Castes and the Scheduled Tribes) of the total number of seats to be filled by direct election in every Panchayat shall be reserved for women'.",
    {"A": "One-tenth is quorum.", "B": "One-fifth is incorrect.", "C": "Correct. Not less than one-third (33.33%).", "D": "One-half (50%) is voluntary adoption by some States (e.g. Bihar, MP, UP), but constitutional minimum is 1/3rd."},
    "Easy", "Article 243D(3)", "Recall constitutional minimum women reservation in Panchayats."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-020", "ch-11", "top-const-11-03",
    "Under Article 243E, if a Panchayat is dissolved before the expiration of its 5-year duration, what is the term of office of the newly elected Panchayat?",
    ["A fresh full period of five years", "Only for the remainder of the period for which the dissolved Panchayat would have continued", "One year only", "Until the next general election to the State Assembly"],
    1,
    "Article 243E(4) explicitly provides: 'A Panchayat constituted upon the dissolution of a Panchayat before the expiration of its duration shall continue only for the remainder of the period for which the dissolved Panchayat would have continued under clause (1) had it not been so dissolved'.",
    {"A": "Fresh 5-year term is false.", "B": "Correct. Continues ONLY for the remainder of the unexpired term.", "C": "One year is incorrect.", "D": "Assembly elections are independent."},
    "Medium", "Article 243E(4)", "Master remainder of term rule upon early Panchayat dissolution."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-021", "ch-11", "top-const-11-03",
    "Under Article 243K, who conducts, superintends, and directs all elections to the Panchayats?",
    ["The Election Commission of India (Article 324)", "The State Election Commission headed by a State Election Commissioner", "The District Magistrate / Collector", "The State Panchayati Raj Department"],
    1,
    "Article 243K(1) vests the superintendence, direction, and control of the preparation of electoral rolls for, and the conduct of, all elections to the Panchayats in a State Election Commission consisting of a State Election Commissioner appointed by the Governor.",
    {"A": "ECI conducts Union and State legislative polls, not local polls.", "B": "Correct. State Election Commission under Article 243K.", "C": "District Magistrate acts as returning officer under SEC.", "D": "Department is executive ministry."},
    "Easy", "Article 243K(1)", "Identify election authority for Panchayats."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-022", "ch-11", "top-const-11-03",
    "How can the State Election Commissioner be removed from office under Article 243K(2)?",
    ["By an order of the Governor in his discretion", "Only in like manner and on the like grounds as a Judge of a High Court", "By an order of the Chief Minister", "By a resolution of the Zilla Parishad"],
    1,
    "Article 243K(2) proviso provides: 'Provided that the State Election Commissioner shall not be removed from his office except in like manner and on the like grounds as a Judge of a High Court and the conditions of service of the State Election Commissioner shall not be varied to his disadvantage after his appointment'.",
    {"A": "Governor cannot remove unilaterally.", "B": "Correct. Removed only in like manner and grounds as a High Court Judge.", "C": "Chief Minister has no removal power.", "D": "Zilla Parishad has no power."},
    "Medium", "Article 243K(2) Proviso", "Recall tenure protection of State Election Commissioner."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-023", "ch-11", "top-const-11-03",
    "In which States is the constitution of an Intermediate Panchayat (Panchayat Samiti) NOT mandatory under Article 243B(2)?",
    ["States having a population not exceeding 10 lakhs", "States having a population not exceeding 20 lakhs", "States having an area of less than 10,000 sq km", "States with less than 5 districts"],
    1,
    "Article 243B(2) provides: 'Notwithstanding anything in clause (1), Panchayats at the intermediate level may not be constituted in a State having a population not exceeding twenty lakhs'.",
    {"A": "10 lakhs is incorrect.", "B": "Correct. Population not exceeding twenty lakhs (20 lakhs).", "C": "Area is not the criterion.", "D": "District count is not the criterion."},
    "Medium", "Article 243B(2)", "Recall 20-lakh population exemption for intermediate Panchayats."
))

# 11-24 to 11-30: Urban Local Bodies (Municipalities - Part IXA)
MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-024", "ch-11", "top-const-11-04",
    "The 74th Constitutional Amendment Act, 1992 added which Part and Schedule to the Constitution of India?",
    ["Part IX and Eleventh Schedule", "Part IXA and Twelfth Schedule", "Part IXB and Thirteenth Schedule", "Part X and Eighth Schedule"],
    1,
    "The 74th Constitutional Amendment Act, 1992 inserted Part IXA ('The Municipalities', Articles 243P to 243ZG) and the Twelfth Schedule (containing 18 functional matters) into the Constitution.",
    {"A": "Part IX/11th Sched is 73rd Amendment (Panchayats).", "B": "Correct. Part IXA and Twelfth Schedule.", "C": "Part IXB is Co-operatives (97th Amendment).", "D": "Part X is tribal areas."},
    "Easy", "74th Constitutional Amendment Act, 1992", "Identify Part and Schedule added by 74th Amendment."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-025", "ch-11", "top-const-11-04",
    "Article 243Q mandates the constitution of which three types of Municipalities?",
    ["Village Panchayat, Mandal Parishad, and Zilla Parishad", "Nagar Panchayat (transitional area), Municipal Council (smaller urban area), and Municipal Corporation (larger urban area)", "Cantonment Board, Port Trust, and Town Area Committee", "Urban Development Authority, Housing Board, and Improvement Trust"],
    1,
    "Article 243Q(1) specifies three forms: (a) a Nagar Panchayat for a transitional area (rural to urban); (b) a Municipal Council for a smaller urban area; and (c) a Municipal Corporation for a larger urban area.",
    {"A": "These are rural 3-tier Panchayats.", "B": "Correct. Nagar Panchayat, Municipal Council, Municipal Corporation.", "C": "These are special statutory urban entities.", "D": "These are para-statal agencies."},
    "Easy", "Article 243Q(1)", "Recall three categories of Municipalities."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-026", "ch-11", "top-const-11-04",
    "Under Article 243S, the constitution of Wards Committees is mandatory within the territorial area of a Municipality having a population of:",
    ["One lakh or more", "Two lakhs or more", "Three lakhs (3,00,000) or more", "Five lakhs or more"],
    2,
    "Article 243S(1) provides: 'There shall be constituted Wards Committees, consisting of one or more wards, within the territorial area of a Municipality having a population of three lakhs or more'.",
    {"A": "One lakh is incorrect.", "B": "Two lakhs is incorrect.", "C": "Correct. Three lakhs (3,00,000) or more.", "D": "Five lakhs is incorrect."},
    "Medium", "Article 243S(1)", "Recall population threshold for Wards Committees."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-027", "ch-11", "top-const-11-04",
    "Under Article 243ZD, what proportion of members of a District Planning Committee (DPC) must be elected from among the elected members of the Zilla Parishad and Municipalities in the district?",
    ["Not less than one-half", "Not less than two-thirds", "Not less than four-fifths (4/5ths)", "All members must be nominated bureaucrats"],
    2,
    "Article 243ZD(2)(b) provides that not less than four-fifths (4/5ths or 80%) of the total number of members of the District Planning Committee shall be elected by and from amongst the elected members of the Panchayat at the district level and of the Municipalities in the district in proportion to their population.",
    {"A": "One-half is incorrect.", "B": "Two-thirds applies to Metropolitan Planning Committee (Art. 243ZE).", "C": "Correct. Not less than four-fifths (4/5ths) in DPC.", "D": "Nominated bureaucracy violates Art. 243ZD."},
    "Hard", "Article 243ZD(2)(b)", "Master District Planning Committee composition ratio."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-028", "ch-11", "top-const-11-04",
    "Under Article 243ZE, a Metropolitan Planning Committee (MPC) is constituted for a metropolitan area having a population of:",
    ["Five lakhs or more", "Ten lakhs (1,000,000) or more", "Twenty lakhs or more", "Fifty lakhs or more"],
    1,
    "Under Article 243P(c) and Article 243ZE, a 'Metropolitan area' means an area having a population of TEN LAKHS (1 million) or more, comprised in one or more districts and consisting of two or more Municipalities or Panchayats.",
    {"A": "Five lakhs is incorrect.", "B": "Correct. Ten lakhs (1 million) or more.", "C": "Twenty lakhs is incorrect.", "D": "Fifty lakhs is incorrect."},
    "Medium", "Article 243P(c) & 243ZE", "Recall population threshold for Metropolitan Planning Committees."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-029", "ch-11", "top-const-11-04",
    "How many functional items are listed in the Twelfth Schedule within the legislative competence of Municipalities under Article 243W?",
    ["Twelve (12) items", "Eighteen (18) items", "Twenty-one (21) items", "Twenty-nine (29) items"],
    1,
    "The Twelfth Schedule contains EIGHTEEN (18) functional items devolved to Municipalities (such as urban planning, regulation of land use, water supply, public health, fire services, and slum improvement). In contrast, the Eleventh Schedule for Panchayats contains 29 items.",
    {"A": "Twelve is schedule number, not item count.", "B": "Correct. Exactly eighteen (18) items.", "C": "Twenty-one is incorrect.", "D": "Twenty-nine (29) is the Eleventh Schedule (Panchayats)."},
    "Easy", "Twelfth Schedule & Article 243W", "Recall item count in Twelfth Schedule."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-11-030", "ch-11", "top-const-11-04",
    "Under Article 243ZG, can a court interfere in municipal election matters or entertain an ordinary writ petition questioning the validity of ward delimitation?",
    ["Yes, High Courts can stay elections under Article 226 at any stage", "No, Article 243ZG explicitly bars courts from questioning the validity of any delimitation law and provides that elections can be called in question ONLY by an election petition", "Yes, upon an application by a registered political party", "Supreme Court alone has original jurisdiction"],
    1,
    "In Kishansing Tomar v. Municipal Corp. of Ahmedabad (2006), the Supreme Court reiterated that Article 243ZG imposes a strict constitutional bar: no election to any Municipality shall be called in question except by an election petition presented to such authority and in such manner as provided by State law.",
    {"A": "Courts cannot stall elections once notified.", "B": "Correct. Article 243ZG bars court interference; election petition is exclusive remedy.", "C": "Political party petition does not bypass bar.", "D": "Election tribunals hear petitions initially."},
    "Medium", "Article 243ZG", "Recall bar on judicial interference in municipal elections."
))

print(f"Chapters 9 to 11 complete ({len(MCQS_CH09_11)} total).")
