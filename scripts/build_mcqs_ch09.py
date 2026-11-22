"""
Builds 35 MCQs for Chapter 9 (The Union & State Executive).
top-const-09-01: 15 MCQs (President & Vice-President)
top-const-09-02: 10 MCQs (Executive Powers, Ordinance & Pardons)
top-const-09-03: 10 MCQs (Prime Minister, CoM & Attorney-General)
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

MCQS_CH09 = []

# ==============================================================================
# TOPIC 09-01: THE PRESIDENT & VICE-PRESIDENT (15 MCQs)
# ==============================================================================

MCQS_CH09.append(create_mcq(
    "mcq-const-09-001", "ch-09", "top-const-09-01",
    "Under Article 54 of the Constitution, the Electoral College for the election of the President of India consists of:",
    ["All members of both Houses of Parliament and all members of State Legislative Assemblies", "Elected members of both Houses of Parliament and elected members of Legislative Assemblies of the States (including Delhi and Puducherry)", "Elected members of Lok Sabha only", "Members of Parliament, State Assemblies, and State Legislative Councils"],
    1,
    "Article 54 provides that the President is elected by an Electoral College consisting of: (a) the elected members of both Houses of Parliament; and (b) the elected members of the Legislative Assemblies of the States (including NCT of Delhi and UT of Puducherry added via 70th Amendment). Nominated members and Legislative Council members do not vote.",
    {"A": "Incorrect because nominated members are excluded.", "B": "Correct. Elected members of Parliament and elected members of State/UT Legislative Assemblies.", "C": "Incorrect because Rajya Sabha and State Assemblies participate.", "D": "Incorrect because Legislative Council members are excluded."},
    "Medium", "Article 54", "Recall the composition of the Presidential Electoral College."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-002", "ch-09", "top-const-09-01",
    "Which Constitutional Amendment Act included the elected members of the Legislative Assemblies of the National Capital Territory of Delhi and the Union Territory of Puducherry in the Electoral College for the election of the President?",
    ["61st Amendment Act, 1988", "69th Amendment Act, 1991", "70th Amendment Act, 1992", "73rd Amendment Act, 1992"],
    2,
    "The 70th Constitutional Amendment Act, 1992 inserted the Explanation to Article 54 clarifying that 'State' includes the National Capital Territory of Delhi and the Union Territory of Puducherry for the Presidential Electoral College.",
    {"A": "61st Amendment lowered voting age from 21 to 18.", "B": "69th Amendment created NCT of Delhi with Legislative Assembly.", "C": "Correct. 70th Amendment included Delhi and Puducherry in Presidential Electoral College.", "D": "73rd Amendment relates to Panchayati Raj."},
    "Medium", "Article 54 Explanation & 70th Amendment", "Identify amendment expanding Presidential Electoral College."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-003", "ch-09", "top-const-09-01",
    "Under Article 55(3), the election of the President is held in accordance with the system of:",
    ["First-past-the-post system with simple majority", "Proportional representation by means of the single transferable vote and voting by secret ballot", "List system with open ballot", "Preferential cumulative voting"],
    1,
    "Article 55(3) mandates: 'The election of the President shall be held in accordance with the system of proportional representation by means of the single transferable vote and the voting at such election shall be by secret ballot'.",
    {"A": "First-past-the-post applies to Lok Sabha and Assembly general elections.", "B": "Correct. Proportional representation by single transferable vote with secret ballot.", "C": "List system is not adopted in India.", "D": "Cumulative voting is not used for Presidential elections."},
    "Easy", "Article 55(3)", "Recall voting method for Presidential election."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-004", "ch-09", "top-const-09-01",
    "What is the formula to calculate the value of the vote of an elected Member of the Legislative Assembly (MLA) of a State under Article 55(2)(a)?",
    ["Total population of State / (Total elected members of Assembly × 1,000)", "Total registered voters / Total MLAs", "Total population of State / Total elected MPs", "State Budget / Total elected members"],
    0,
    "Article 55(2)(a) prescribes: Value of vote of an MLA = (Total population of the State as per 1971 census) / (Total number of elected members of the Legislative Assembly × 1,000).",
    {"A": "Correct. Population divided by (elected MLAs × 1000).", "B": "Voters count is not used; census population is used.", "C": "Elected MPs formula calculates MP vote value, not MLA.", "D": "Budget has no relevance to vote value."},
    "Medium", "Article 55(2)(a)", "Recall mathematical formula for MLA vote value."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-005", "ch-09", "top-const-09-01",
    "Which census population data is currently frozen until the year 2026 for calculating the value of votes in Presidential elections under the 84th Amendment Act, 2001?",
    ["1951 Census", "1971 Census", "1991 Census", "2011 Census"],
    1,
    "By the 42nd Amendment Act 1976 and further extended by the 84th Amendment Act 2001, the population of States for the Presidential election under Article 55 is frozen to the 1971 Census until relevant figures for the first census after 2026 are published.",
    {"A": "1951 census is not the benchmark.", "B": "Correct. 1971 Census figures remain frozen until post-2026.", "C": "1991 census was not adopted for Presidential vote weights.", "D": "2011 census is not used for Presidential electoral quotas."},
    "Medium", "Article 55 Explanation & 84th Amendment", "Recall census year freeze for Presidential election."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-006", "ch-09", "top-const-09-01",
    "Under Article 58, which of the following is NOT an essential qualification for election as President of India?",
    ["Must be a citizen of India", "Must have completed the age of thirty-five (35) years", "Must be qualified for election as a member of the Rajya Sabha", "Must be qualified for election as a member of the House of the People (Lok Sabha)"],
    2,
    "Under Article 58(1)(c), a person must be qualified for election as a member of the House of the People (Lok Sabha). Qualification for the Council of States (Rajya Sabha) is a requirement for the Vice-President (Art. 66(3)(c)), NOT the President.",
    {"A": "Citizen of India is required under Art. 58(1)(a).", "B": "Age of 35 years is required under Art. 58(1)(b).", "C": "Correct. Rajya Sabha qualification applies to Vice-President, not President.", "D": "Lok Sabha qualification is explicitly required for President under Art. 58(1)(c)."},
    "Medium", "Article 58 & 66", "Distinguish qualification differences between President and Vice-President."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-007", "ch-09", "top-const-09-01",
    "Under Article 61, on what sole constitutional ground can the President of India be impeached?",
    ["Proved misbehaviour or incapacity", "Violation of the Constitution", "Corruption and moral turpitude", "Gross administrative failure"],
    1,
    "Article 61(1) states: 'When a President is to be impeached for VIOLATION OF THE CONSTITUTION, the charge shall be preferred by either House of Parliament'. No other ground is recognized.",
    {"A": "Proved misbehaviour or incapacity is the ground for removal of Supreme Court and High Court Judges (Art. 124(4)).", "B": "Correct. 'Violation of the Constitution' is the sole ground.", "C": "Corruption is not an express text ground under Art. 61.", "D": "Administrative failure is not a constitutional ground for impeachment."},
    "Easy", "Article 61(1)", "Identify the constitutional ground for Presidential impeachment."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-008", "ch-09", "top-const-09-01",
    "Under Article 61(2), what are the formal procedural requirements to prefer a charge of impeachment against the President?",
    ["Notice signed by at least 1/10th members and passed by simple majority", "14 days' written notice signed by at least 1/4th of total members of the House, and passed by a majority of not less than 2/3rds of the TOTAL MEMBERSHIP of that House", "Resolution moved by the Prime Minister with 7 days notice", "Passed by 2/3rds of members present and voting"],
    1,
    "Article 61(2) mandates: (a) at least 14 days' written notice signed by not less than one-fourth (1/4th) of the total number of members of the House; and (b) the resolution must be passed by a majority of NOT LESS THAN TWO-THIRDS OF THE TOTAL MEMBERSHIP of the House.",
    {"A": "1/10th notice and simple majority are incorrect.", "B": "Correct. 14 days notice, 1/4th signatories, and 2/3rd total membership majority.", "C": "PM cannot unilaterally move impeachment.", "D": "Present and voting is insufficient; 2/3rds of total membership is required."},
    "Hard", "Article 61(2)", "Master the procedural rigours of Article 61."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-009", "ch-09", "top-const-09-01",
    "Do nominated members of Parliament and elected members of State Legislative Assemblies participate in the impeachment of the President under Article 61?",
    ["Nominated MPs do NOT participate, but State MLAs do participate", "Both nominated MPs and State MLAs participate equally", "Nominated members of Parliament DO participate, but members of State Legislative Assemblies do NOT participate", "Only the Supreme Court conducts impeachment; MPs have no voting role"],
    2,
    "In the impeachment under Article 61, ALL members of Parliament (both elected and nominated) participate. However, members of State Legislative Assemblies DO NOT participate, even though elected MLAs vote in Presidential elections.",
    {"A": "Incorrect; reverse of the constitutional rule.", "B": "Incorrect; MLAs have zero role in impeachment.", "C": "Correct. Nominated MPs participate in impeachment; State MLAs do not.", "D": "Parliament conducts impeachment; Supreme Court only investigates disputes under Art. 71."},
    "Hard", "Article 61 & 54 Contrast", "Recognize asymmetry between Presidential election and impeachment electorates."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-010", "ch-09", "top-const-09-01",
    "Under Article 71(1), all doubts and disputes arising out of or in connection with the election of a President or Vice-President shall be inquired into and decided by:",
    ["The Election Commission of India", "A Joint Committee of Parliament", "The Supreme Court of India whose decision shall be final", "A special Constitution Bench appointed by the President"],
    2,
    "Article 71(1) states: 'All doubts and disputes arising out of or in connection with the election of a President or Vice-President shall be inquired into and decided by the Supreme Court whose decision shall be final'.",
    {"A": "ECI conducts the election, but disputes are adjudicated solely by Supreme Court.", "B": "Parliament has no judicial dispute-adjudication power over Presidential polls.", "C": "Correct. Supreme Court of India exclusively under Art. 71.", "D": "President cannot appoint benches to decide his own election."},
    "Easy", "Article 71(1)", "Recall exclusive dispute authority for Presidential election."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-011", "ch-09", "top-const-09-01",
    "Under Article 71(4), can the election of a person as President or Vice-President be called in question on the ground of the existence of any vacancy in the Electoral College?",
    ["Yes, if more than 10% seats are vacant", "Yes, if an entire State Assembly is dissolved", "No, the election cannot be called in question on the ground of the existence of any vacancy in the Electoral College", "Yes, with special leave of the Supreme Court"],
    2,
    "Article 71(4) (inserted by the 11th Amendment Act 1961) specifically mandates: 'The election of a person as President or Vice-President shall not be called in question on the ground of the existence of any vacancy for whatever reason among the members of the electoral college electing him'. Confirmed in In re Presidential Election, 1974.",
    {"A": "Percentage of vacancy is irrelevant.", "B": "Dissolution of Gujarat Assembly did not halt Presidential poll in 1974 reference.", "C": "Correct. Vacancies in Electoral College cannot invalidate election.", "D": "Article 71(4) provides an absolute bar."},
    "Medium", "Article 71(4) & In re Presidential Election 1974", "Recall bar on challenging Presidential election due to vacancies."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-012", "ch-09", "top-const-09-01",
    "Under Article 64 and Article 89(1), who is the ex-officio Chairman of the Council of States (Rajya Sabha)?",
    ["The Prime Minister", "The Vice-President of India", "The Chief Justice of India", "A member elected by the Council of States"],
    1,
    "Article 64 states: 'The Vice-President shall be ex officio Chairman of the Council of the States and shall not hold any other office of profit'.",
    {"A": "Prime Minister is Leader of the House or Minister.", "B": "Correct. Vice-President is ex-officio Chairman of Rajya Sabha.", "C": "Chief Justice has judicial functions.", "D": "Deputy Chairman is elected by the Council, but Chairman is ex-officio Vice-President."},
    "Easy", "Article 64 & 89(1)", "Identify ex-officio role of Vice-President."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-013", "ch-09", "top-const-09-01",
    "How is the Vice-President of India elected under Article 66(1)?",
    ["By elected members of both Houses of Parliament only", "By members of an electoral college consisting of the members of both Houses of Parliament (both elected and nominated) in accordance with proportional representation", "By members of Parliament and State Assemblies", "By the Rajya Sabha alone"],
    1,
    "Article 66(1) provides: 'The Vice-President shall be elected by the members of an electoral college consisting of the members of both Houses of Parliament in accordance with the system of proportional representation by means of the single transferable vote'. Both elected and nominated MPs vote; State MLAs do not.",
    {"A": "Nominated MPs also vote in Vice-President election.", "B": "Correct. Both elected and nominated members of both Houses of Parliament.", "C": "State Assemblies do not vote in Vice-Presidential elections.", "D": "Lok Sabha also votes, not Rajya Sabha alone."},
    "Medium", "Article 66(1)", "Recall composition of Vice-Presidential Electoral College."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-014", "ch-09", "top-const-09-01",
    "Under Article 67(b), what is the procedure for the removal of the Vice-President of India?",
    ["Impeachment under Article 61 by 2/3rds total membership in each House", "Resolution of the Council of States passed by a majority of all the then members of the Council and agreed to by the House of the People", "An order of the Supreme Court of India", "Resolution moved by the President of India"],
    1,
    "Under Article 67(b), the Vice-President may be removed from office by a resolution of the Council of States passed by a majority of all the then members of the Council (effective majority) and agreed to by the House of the People (simple majority). 14 days' notice is required.",
    {"A": "Impeachment under Art. 61 applies only to the President.", "B": "Correct. Resolution by Council of States (effective majority) agreed by House of People.", "C": "Supreme Court adjudicates election disputes, not removal.", "D": "President cannot remove Vice-President on executive order."},
    "Medium", "Article 67(b)", "Master removal procedure of the Vice-President."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-015", "ch-09", "top-const-09-01",
    "Under the President (Discharge of Functions) Act, 1969, who discharges the functions of the President when both the President and the Vice-President offices fall vacant?",
    ["The Prime Minister of India", "The Speaker of the Lok Sabha", "The Chief Justice of India, or in his absence, the senior-most Judge of the Supreme Court available", "The Attorney-General for India"],
    2,
    "Under the President (Discharge of Functions) Act, 1969 (enacted under Art. 70), if both President and Vice-President offices fall vacant, the Chief Justice of India (and in his absence, the senior-most Judge of the Supreme Court) discharges the functions of President. Justice M. Hidayatullah acted as President under this provision in 1969.",
    {"A": "Prime Minister cannot assume executive headship directly.", "B": "Speaker does not succeed before CJI under Indian statutory hierarchy.", "C": "Correct. Chief Justice of India, then senior-most Supreme Court Judge.", "D": "Attorney-General is a legal advisor, not constitutional successor."},
    "Easy", "Article 70 & Act of 1969", "Identify succession hierarchy under President Discharge of Functions Act."
))

# ==============================================================================
# TOPIC 09-02: EXECUTIVE POWERS, ORDINANCE & PARDONS (10 MCQs)
# ==============================================================================

MCQS_CH09.append(create_mcq(
    "mcq-const-09-016", "ch-09", "top-const-09-02",
    "Under Article 72 of the Constitution, the President has the power to grant pardons, reprieves, respites or remissions of punishment in all of the following cases EXCEPT:",
    ["In all cases where the punishment or sentence is by a Court Martial", "In all cases where the punishment is for an offence against any law relating to a matter to which the executive power of the Union extends", "In all cases where the sentence is a sentence of death", "In civil suits where damages are awarded by a civil court"],
    3,
    "Article 72 applies exclusively to criminal punishments and sentences (Court Martial, Union executive matters, and death sentences). The pardoning power does not extend to civil suits or civil damages awards.",
    {"A": "Court Martial pardoning is specifically vested in President under Art. 72(1)(a).", "B": "Offences under Union executive power fall under Art. 72(1)(b).", "C": "Death sentences fall under Art. 72(1)(c).", "D": "Correct. Pardoning power under Art. 72 does not apply to civil tort/contract damages."},
    "Medium", "Article 72", "Define scope and limits of Presidential clemency."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-017", "ch-09", "top-const-09-02",
    "In which landmark case did the Supreme Court hold that the President's pardoning power under Article 72 is subject to judicial review on grounds of arbitrariness, mala fides, or extraneous considerations?",
    ["A.K. Gopalan v. State of Madras (1950)", "Kehar Singh v. Union of India (1989) & Epuru Sudhakar v. Govt. of A.P. (2006)", "A.D.M. Jabalpur v. Shivkant Shukla (1976)", "Minerva Mills v. Union of India (1980)"],
    1,
    "In Kehar Singh (1989) and further solidified in Epuru Sudhakar (2006), the Supreme Court ruled that while the President/Governor exercises constitutional clemency power, orders under Articles 72/161 are subject to limited judicial review if passed without application of mind, based on extraneous or malafide considerations, or contaminated by arbitrariness.",
    {"A": "Gopalan was early preventive detention case under Art. 21.", "B": "Correct. Kehar Singh & Epuru Sudhakar established judicial review of clemency.", "C": "ADM Jabalpur dealt with habeas corpus suspension during emergency.", "D": "Minerva Mills dealt with basic structure and Art. 368/31C."},
    "Medium", "Article 72 & Epuru Sudhakar (2006)", "Recall landmark cases on judicial review of clemency power."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-018", "ch-09", "top-const-09-02",
    "Can the Governor of a State grant a pardon in case of a sentence of death under Article 161 of the Constitution?",
    ["Yes, the Governor has identical powers as the President regarding death sentences", "No, the power to grant a complete PARDON for a death sentence is vested exclusively in the President under Article 72; the Governor cannot pardon death, though he can suspend, remit, or commute it", "Yes, but only with prior sanction of the President", "No, neither President nor Governor can pardon death sentences"],
    1,
    "Under Article 72(1)(c), the power to PARDON a death sentence belongs exclusively to the President. Under Article 161, a Governor cannot completely pardon a death sentence, though the Governor can suspend, remit or commute a death sentence under state law competence.",
    {"A": "Incorrect; Governor cannot grant full pardon in death penalty cases.", "B": "Correct. Sole prerogative of complete pardon for death lies with President (Art. 72).", "C": "Presidential sanction mechanism does not convert Art. 161 into death pardon.", "D": "President explicitly possesses death sentence pardon power."},
    "Hard", "Article 72 & 161 Comparison", "Distinguish pardoning powers of President vs Governor in capital offences."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-019", "ch-09", "top-const-09-02",
    "What is the maximum life of an Ordinance promulgated by the President under Article 123 in the absence of parliamentary approval?",
    ["Six weeks from the date of promulgation", "Six months from the date of promulgation", "Six weeks from the reassembly of Parliament (maximum theoretical duration being 6 months + 6 weeks)", "One year"],
    2,
    "Under Article 123(2)(a), an Ordinance shall cease to operate at the expiration of SIX WEEKS from the reassembly of Parliament (or earlier if disapproved by resolutions). Since the maximum interval between parliamentary sessions is six months (Art. 85), the maximum theoretical life is 6 months and 6 weeks.",
    {"A": "Six weeks runs from reassembly of Parliament, not date of promulgation.", "B": "Six months is interval between sessions, not expiration rule.", "C": "Correct. Six weeks from reassembly of Parliament (maximum 6 months + 6 weeks).", "D": "One year is unconstitutional."},
    "Medium", "Article 123(2)(a)", "Calculate duration and expiration of Presidential ordinances."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-020", "ch-09", "top-const-09-02",
    "In D.C. Wadhwa v. State of Bihar (1987), what constitutional principle regarding the ordinance-making power was laid down by the Supreme Court?",
    ["Ordinances can amend the Constitution directly", "Repeated re-promulgation of ordinances without placing them before the legislature is a fraud on the Constitution and subverts democratic legislative process", "Governor can issue ordinances even when the Assembly is in active session", "Ordinances have higher legal status than parliamentary statutes"],
    1,
    "In D.C. Wadhwa (1987), the Constitution Bench held that executive re-promulgation of ordinances year after year without placing them before the legislature is a 'fraud on the Constitution'. An ordinance is an emergency power to meet extraordinary situations, not a substitute for the legislature. Reaffirmed in Krishna Kumar Singh v. State of Bihar (2017).",
    {"A": "Ordinances cannot amend the Constitution.", "B": "Correct. Re-promulgation without legislative scrutiny is a fraud on the Constitution.", "C": "Assembly must be prorogued or adjourned; cannot promulgate during active session.", "D": "Ordinances have equal, not superior, force to statutes."},
    "Hard", "Article 123, 213 & D.C. Wadhwa (1987)", "Recall ruling on fraudulent re-promulgation of ordinances."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-021", "ch-09", "top-const-09-02",
    "Under Article 123(1), what is a mandatory condition precedent for the President to promulgate an Ordinance?",
    ["Both Houses of Parliament must be in active session", "At least one House of Parliament must NOT be in session", "The Supreme Court must issue an advisory opinion under Article 143", "A National Emergency under Article 352 must be in force"],
    1,
    "Article 123(1) states: 'If at any time, except when both Houses of Parliament are in session, the President is satisfied that circumstances exist...'. Thus, an Ordinance can only be promulgated when either both Houses or at least one House is not in session.",
    {"A": "If both Houses are in session, no Ordinance can be promulgated.", "B": "Correct. At least one House of Parliament must not be in session.", "C": "Advisory opinion is not a condition precedent.", "D": "Ordinance power is independent of emergency declarations."},
    "Medium", "Article 123(1)", "Identify jurisdictional condition for promulgating an ordinance."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-022", "ch-09", "top-const-09-02",
    "Under Article 77(1) of the Constitution, all executive action of the Government of India shall be expressed to be taken in the name of:",
    ["The Prime Minister of India", "The President of India", "The Parliament of India", "The Cabinet Secretariat"],
    1,
    "Article 77(1) explicitly provides: 'All executive action of the Government of India shall be expressed to be taken in the name of the President'.",
    {"A": "Prime Minister is head of government, but executive action is in President's name.", "B": "Correct. In the name of the President.", "C": "Parliament is the legislature, not executive titular.", "D": "Cabinet Secretariat coordinates, but does not own executive expression."},
    "Easy", "Article 77(1)", "Recall constitutional form for expressing Union executive actions."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-023", "ch-09", "top-const-09-02",
    "Who allocates business of the Government of India among Ministers under Article 77(3)?",
    ["The Speaker of Lok Sabha", "The Prime Minister directly by administrative circular", "The President, by making rules for the more convenient transaction of business (Allocation of Business Rules)", "The Union Law Minister"],
    2,
    "Article 77(3) mandates: 'The President shall make rules for the more convenient transaction of the business of the Government of India, and for the allocation among Ministers of the said business'.",
    {"A": "Speaker manages legislative business in Lok Sabha, not government ministries.", "B": "PM advises, but formal rules are made by President under Art. 77(3).", "C": "Correct. The President makes Allocation of Business Rules.", "D": "Law Minister does not allocate portfolios."},
    "Medium", "Article 77(3)", "Recall authority enacting Government Allocation of Business Rules."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-024", "ch-09", "top-const-09-02",
    "What is the meaning of 'Respite' under Article 72 and Article 161 in the context of Presidential/Gubernatorial clemency?",
    ["Substituting a lighter form of punishment for a heavier one", "Reducing the amount of sentence without changing its character", "Awarding a lesser sentence in place of one originally awarded, on special grounds such as pregnancy or mental illness", "Temporary suspension of the execution of a sentence"],
    2,
    "'Respite' means awarding a lesser sentence in place of one originally awarded, on some special factual ground, such as the pregnancy of a female offender or advanced infirmity. In contrast: Commutation = substitution of lighter form; Remission = reducing quantum without changing character; Reprieve = temporary stay.",
    {"A": "Substitution of a lighter form is 'Commutation'.", "B": "Reducing amount without changing character is 'Remission'.", "C": "Correct. Awarding a lesser punishment due to special grounds (respite).", "D": "Temporary suspension of execution is 'Reprieve'."
    },
    "Hard", "Article 72 Technical Terms", "Distinguish clemency terms: Pardon, Commutation, Remission, Respite, Reprieve."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-025", "ch-09", "top-const-09-02",
    "Can the President of India grant an oral hearing to a convict seeking clemency under Article 72 as a matter of constitutional right?",
    ["Yes, natural justice mandates an oral personal hearing before rejecting a mercy petition", "No, in Kehar Singh v. Union of India (1989), the Supreme Court ruled that there is no fundamental or constitutional right to an oral hearing under Article 72", "Yes, if requested in writing by the convict's senior advocate", "Yes, in all capital punishment cases"],
    1,
    "In Kehar Singh v. Union of India (1989), Chief Justice R.S. Pathak speaking for the Constitution Bench settled that a petitioner for clemency under Article 72 has no right to an oral hearing before the President. The proceeding is purely executive and does not partake of judicial trial procedure.",
    {"A": "Natural justice in Art. 72 does not mandate oral hearing.", "B": "Correct. Kehar Singh held there is no constitutional right to an oral hearing under Art. 72.", "C": "Advocate request cannot compel personal audience with President.", "D": "Death row convicts have no automatic right to personal audience."},
    "Hard", "Article 72 & Kehar Singh (1989)", "Recall rule regarding oral hearing in clemency petitions."
))

# ==============================================================================
# TOPIC 09-03: PRIME MINISTER, COUNCIL OF MINISTERS & AG (10 MCQs)
# ==============================================================================

MCQS_CH09.append(create_mcq(
    "mcq-const-09-026", "ch-09", "top-const-09-03",
    "Following the 42nd and 44th Constitutional Amendment Acts, what is the exact legal nature of the President's duty to act on the aid and advice of the Council of Ministers under Article 74(1)?",
    ["Advice is purely discretionary and recommendatory", "President MUST act in accordance with such advice, but can require the Council of Ministers to RECONSIDER such advice once; thereafter, the President shall act in accordance with the advice tendered after reconsideration", "President can reject the advice permanently with concurrence of Chief Justice of India", "President acts independently in all defense and foreign affairs matters"],
    1,
    "The 42nd Amendment made advice strictly binding. The 44th Amendment Act, 1978 inserted the Proviso to Article 74(1): 'Provided that the President may require the Council of Ministers to reconsider such advice, either generally or otherwise, and the President shall act in accordance with the advice tendered after such reconsideration'.",
    {"A": "Discretionary advice was replaced by binding obligation.", "B": "Correct. Binding, with power to remit once for reconsideration under 44th Amendment proviso.", "C": "Chief Justice has no advisory veto over executive cabinet advice.", "D": "Union executive is aid-advised across all subjects, including defense."},
    "Medium", "Article 74(1) & 44th Amendment", "Master the binding nature and reconsideration proviso of Cabinet advice."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-027", "ch-09", "top-const-09-03",
    "Under Article 74(2), can any court inquire into the question whether any, and if so what, advice was tendered by Ministers to the President?",
    ["Yes, under Article 226 and Article 32 judicial review", "No, Article 74(2) bars courts from inquiring into the question whether any, and if so what, advice was tendered by Ministers to the President", "Yes, upon an application under the Right to Information Act", "Yes, if approved by a 5-judge bench of the Supreme Court"],
    1,
    "Article 74(2) states unequivocally: 'The question whether any, and if so what, advice was tendered by Ministers to the President shall not be inquired into in any court'. In S.R. Bommai (1994), the SC clarified that while Ministerial advice is shielded, the background material on which advice is based is not protected under Art. 74(2).",
    {"A": "Writ courts cannot inquire into Ministerial advice itself.", "B": "Correct. Absolute constitutional bar under Article 74(2).", "C": "RTI does not override Article 74(2) constitutional bar.", "D": "No bench can breach express text of Art. 74(2)."},
    "Medium", "Article 74(2) & S.R. Bommai (1994)", "Recall constitutional bar on judicial inquiry into ministerial advice."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-028", "ch-09", "top-const-09-03",
    "Under Article 75(3) of the Constitution, the Council of Ministers is collectively responsible to:",
    ["The President of India", "The House of the People (Lok Sabha)", "Both Houses of Parliament jointly", "The Prime Minister"],
    1,
    "Article 75(3) states: 'The Council of Ministers shall be collectively responsible to the House of the People'. Collective responsibility is to the popular chamber (Lok Sabha), not Parliament as a whole or the President.",
    {"A": "Ministers hold office during pleasure of President individually (Art. 75(2)), not collectively.", "B": "Correct. Collectively responsible to the House of the People (Lok Sabha).", "C": "Rajya Sabha cannot pass a motion of no-confidence.", "D": "Cabinet is headed by PM, but responsible to Lok Sabha."},
    "Easy", "Article 75(3)", "Recall core organ of collective responsibility."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-029", "ch-09", "top-const-09-03",
    "What ceiling was placed on the total number of Ministers, including the Prime Minister, in the Union Council of Ministers by the 91st Constitutional Amendment Act, 2003?",
    ["Shall not exceed 10% of the total number of members of the Lok Sabha", "Shall not exceed 15% of the total number of members of the House of the People", "Shall not exceed 50 members in total", "Shall not exceed 20% of the total membership of Parliament"],
    1,
    "Article 75(1A), inserted by the 91st Constitutional Amendment Act 2003, mandates: 'The total number of Ministers, including the Prime Minister, in the Council of Ministers shall not exceed fifteen per cent (15%) of the total number of members of the House of the People'.",
    {"A": "10% applies to Delhi Assembly (Art. 239AA).", "B": "Correct. Shall not exceed 15% of total members of House of the People.", "C": "Fixed count of 50 is incorrect.", "D": "Percentage is calculated against Lok Sabha only, not both Houses."},
    "Medium", "Article 75(1A) & 91st Amendment", "Recall ministerial size cap under 91st Amendment."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-030", "ch-09", "top-const-09-03",
    "Under Article 75(5), a Minister who for any period of six consecutive months is not a member of either House of Parliament shall:",
    ["Be disqualified from contesting elections for 6 years", "At the expiration of that period cease to be a Minister", "Be automatically nominated to the Rajya Sabha by the President", "Require a vote of confidence from the Lok Sabha"],
    1,
    "Article 75(5) explicitly states: 'A Minister who for any period of six consecutive months is not a member of either House of Parliament shall at the expiration of that period cease to be a Minister'. Reaffirmed in S.R. Chaudhuri v. State of Punjab (2001).",
    {"A": "No electoral disqualification penalty is imposed.", "B": "Correct. Ceases to be a Minister at the end of 6 consecutive months.", "C": "Nomination is not automatic.", "D": "Confidence vote cannot cure failure to become an MP within 6 months."},
    "Easy", "Article 75(5)", "Recall six-month rule for non-legislator ministers."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-031", "ch-09", "top-const-09-03",
    "Under Article 78 of the Constitution, what is the constitutional duty of the Prime Minister in relation to the President?",
    ["To submit weekly intelligence reports to the Supreme Court", "To communicate to the President all decisions of the Council of Ministers relating to administration and legislation, and furnish such information as the President may call for", "To preside over joint sittings of Parliament", "To countersign all orders of the Supreme Court"],
    1,
    "Article 78 delineates the duties of the Prime Minister: (a) communicate to President all decisions of Council of Ministers relating to administration and proposals for legislation; (b) furnish information called for; and (c) submit for Council consideration any matter decided by a Minister without Council consideration.",
    {"A": "Intelligence reports are not submitted to Supreme Court.", "B": "Correct. Duty to communicate Cabinet decisions and furnish requested information.", "C": "Speaker presides over joint sittings under Art. 118(4).", "D": "PM does not countersign Supreme Court orders."},
    "Medium", "Article 78", "Recall duties of Prime Minister towards President."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-032", "ch-09", "top-const-09-03",
    "Under Article 76(1), what qualifications are required for appointment as the Attorney-General for India?",
    ["Must have practiced as an advocate in the Supreme Court for at least 20 years", "Must be a person qualified to be appointed a Judge of the Supreme Court", "Must be an elected member of the Lok Sabha with a law degree", "Must have served as a Union Law Minister"],
    1,
    "Article 76(1) provides: 'The President shall appoint a person who is QUALIFIED TO BE APPOINTED A JUDGE OF THE SUPREME COURT to be Attorney-General for India'.",
    {"A": "Specific 20-year SC practice is not the constitutional text.", "B": "Correct. Qualified to be appointed a Judge of the Supreme Court.", "C": "Attorney-General is a non-political law officer, not an MP.", "D": "Political ministerial tenure is irrelevant."},
    "Easy", "Article 76(1)", "Recall qualifications for Attorney-General for India."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-033", "ch-09", "top-const-09-03",
    "Under Article 76(4), the Attorney-General for India holds office during the pleasure of:",
    ["The Chief Justice of India", "The Prime Minister of India", "The President of India", "The Parliament of India"],
    2,
    "Article 76(4) states: 'The Attorney-General shall hold office during the pleasure of the President, and shall receive such remuneration as the President may determine'.",
    {"A": "CJI does not control AG appointment or tenure.", "B": "PM advises President, but constitutional pleasure is of the President.", "C": "Correct. Holds office during the pleasure of the President.", "D": "Parliament has no impeachment or removal power over the AG."},
    "Easy", "Article 76(4)", "Identify appointing and tenure authority for Attorney-General."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-034", "ch-09", "top-const-09-03",
    "Under Article 88, which special parliamentary rights are granted to the Attorney-General for India?",
    ["The right to speak in, and take part in proceedings of, either House, any joint sitting, and any Parliamentary Committee of which he is named a member, but WITHOUT the right to vote", "Full voting rights in both Lok Sabha and Rajya Sabha", "The right to veto money bills passed by the Lok Sabha", "The right to preside over the Rajya Sabha in absence of the Chairman"],
    0,
    "Article 88 confers upon every Minister and the Attorney-General the right to speak and take part in the proceedings of either House, joint sittings, and parliamentary committees, 'but shall not by virtue of this article be entitled to vote'.",
    {"A": "Correct. Right to speak and participate in Parliament, but strictly without right to vote.", "B": "AG has no parliamentary vote.", "C": "AG has no legislative veto.", "D": "Presiding officer is Deputy Chairman, not AG."},
    "Medium", "Article 88", "Master parliamentary privileges and voting disability of Attorney-General."
))

MCQS_CH09.append(create_mcq(
    "mcq-const-09-035", "ch-09", "top-const-09-03",
    "In Shamsher Singh v. State of Punjab (1974), what core principle of constitutional executive authority was reaffirmed by the seven-judge Constitution Bench?",
    ["The President and Governors possess personal autocratic powers overriding their Cabinets", "Under the Westminster cabinet system of government, the President and Governor act on the aid and advice of the Council of Ministers, and the executive satisfaction is not personal satisfaction but constitutional satisfaction of the Council", "The Governor is an employee/agent of the Central Government with no independent status", "Ministers are personally answerable to the Supreme Court for every administrative file"],
    1,
    "In Shamsher Singh v. State of Punjab (1974), the 7-judge Constitution Bench led by Chief Justice A.N. Ray (with concurring judgment by Justice V.R. Krishna Iyer) held that the President and Governor are constitutional heads. The satisfaction required by the Constitution is not their personal satisfaction, but the satisfaction of the Council of Ministers on whose aid and advice they act.",
    {"A": "Autocratic personal powers were rejected as incompatible with parliamentary democracy.", "B": "Correct. Constitutional satisfaction of Council of Ministers, not personal satisfaction of President/Governor.", "C": "In Hargovind Pant (1979), SC held Governor is not an employee of Centre.", "D": "Ministers are collectively responsible to the legislature, not courts on routine policy."},
    "Hard", "Article 74, 163 & Shamsher Singh (1974)", "Explain constitutional satisfaction vs personal satisfaction of constitutional heads."
))

if __name__ == "__main__":
    print(f"Generated {len(MCQS_CH09)} MCQs for Chapter 9.")
