"""
Appends Ch 9 (35 MCQs), Ch 10 (35 MCQs), and Ch 11 (30 MCQs)
to scripts/build_mcqs_ch09_to_ch11.py
"""

with open('scripts/build_mcqs_ch09_to_ch11.py', 'a', encoding='utf-8') as f:
    f.write('''
# ==============================================================================
# CHAPTER 9: THE UNION EXECUTIVE (35 MCQs)
# ==============================================================================
# 09-01 to 09-12: President & VP Office, Election, Impeachment
MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-001", "ch-09", "top-const-09-01",
    "Under Article 54, which of the following is NOT a member of the Electoral College for the election of the President of India?",
    ["Elected members of Rajya Sabha", "Elected members of Lok Sabha", "Elected members of State Legislative Assemblies", "Nominated members of Rajya Sabha and members of State Legislative Councils"],
    3,
    "Under Article 54, the Electoral College consists ONLY of elected members of both Houses of Parliament and elected members of State Legislative Assemblies (including Delhi and Puducherry). Nominated members of Parliament/Assemblies and all members of State Legislative Councils are strictly excluded.",
    {"A": "Elected RS members vote in presidential polls.", "B": "Elected LS members vote in presidential polls.", "C": "Elected MLAs vote in presidential polls.", "D": "Correct. Nominated MPs and all MLCs are strictly excluded."},
    "Easy", "Article 54", "Recall composition of Presidential Electoral College."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-002", "ch-09", "top-const-09-01",
    "Which Constitutional Amendment included elected members of the Legislative Assemblies of Delhi and Puducherry in the Presidential Electoral College?",
    ["61st Amendment Act, 1988", "69th Amendment Act, 1991", "70th Amendment Act, 1992", "73rd Amendment Act, 1992"],
    2,
    "The 70th Constitutional Amendment Act, 1992 added an Explanation to Article 54 specifying that 'State' includes the National Capital Territory of Delhi and the Union Territory of Puducherry for the purposes of Presidential elections.",
    {"A": "61st reduced voting age.", "B": "69th created NCT of Delhi.", "C": "Correct. 70th Amendment Act, 1992 included Delhi and Puducherry.", "D": "73rd dealt with Panchayats."},
    "Medium", "Article 54, Explanation & 70th Amendment", "Identify 70th Amendment addition to Article 54."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-003", "ch-09", "top-const-09-01",
    "What is the formula to calculate the value of the vote of an elected MLA in a Presidential election under Article 55?",
    ["Total population of State / (Total elected members of Assembly * 1000)", "Total population of State / Total registered voters", "Total state budget / Total elected members", "Equal to 100 votes for every MLA"],
    0,
    "Under Article 55(2)(a), the value of vote of an MLA is obtained by dividing the total population of the State by the total number of elected members of the State Legislative Assembly, and dividing the quotient by 1,000.",
    {"A": "Correct. Population / (Elected MLAs * 1000).", "B": "Registered voters is not the denominator.", "C": "Budget is irrelevant.", "D": "Value varies from State to State based on population."},
    "Medium", "Article 55(2)(a)", "Recall formula for MLA vote value."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-004", "ch-09", "top-const-09-01",
    "What is the sole constitutional ground on which the President of India can be impeached under Article 61?",
    ["Incapacity or physical infirmity", "Violation of the Constitution", "Corruption and moral turpitude", "Gross administrative negligence"],
    1,
    "Article 61(1) explicitly provides: 'When a President is to be impeached for VIOLATION OF THE CONSTITUTION, the charge shall be preferred by either House of Parliament'.",
    {"A": "Incapacity applies to judges under Art. 124(4), not President.", "B": "Correct. 'Violation of the Constitution' is the sole ground.", "C": "Corruption is not constitutional phrasing under Art. 61.", "D": "Negligence is not specified."},
    "Easy", "Article 61(1)", "Recall sole ground for Presidential impeachment."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-005", "ch-09", "top-const-09-01",
    "What majority is required in EACH House of Parliament to pass an impeachment resolution against the President under Article 61?",
    ["Simple majority of members present and voting", "Majority of total membership and 2/3rd present and voting", "A majority of not less than two-thirds of the TOTAL membership of the House", "Absolute majority of both Houses in a Joint Sitting"],
    2,
    "Under Article 61(2)(b) and 61(4), an impeachment resolution must be passed by a majority of not less than TWO-THIRDS OF THE TOTAL MEMBERSHIP of each House. This is the most stringent majority requirement in the Indian Constitution.",
    {"A": "Simple majority is insufficient.", "B": "This is standard Art. 368 majority, not Art. 61.", "C": "Correct. 2/3rd of the TOTAL membership of the House.", "D": "No joint sitting for impeachment."},
    "Hard", "Article 61(2)(b) & (4)", "Master Article 61 majority requirement."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-006", "ch-09", "top-const-09-01",
    "Who presides over the investigation of charges during the impeachment of the President?",
    ["The Chief Justice of India", "The other House of Parliament to which the charge was not preferred", "A special Supreme Court Tribunal", "The Attorney-General for India"],
    1,
    "Under Article 61(3), when a charge has been preferred by either House, the OTHER House investigates the charge or causes the charge to be investigated, and the President has the right to appear and be represented.",
    {"A": "CJI does not preside over impeachment investigation.", "B": "Correct. The other House investigates the charge.", "C": "No judicial tribunal is appointed.", "D": "Attorney-General does not preside."},
    "Medium", "Article 61(3)", "Explain investigating mechanism in impeachment."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-007", "ch-09", "top-const-09-01",
    "Who investigates and decides all doubts and disputes arising out of or in connection with the election of a President or Vice-President?",
    ["The Election Commission of India", "The Supreme Court of India, whose decision shall be final", "A Joint Parliamentary Committee", "The Delhi High Court"],
    1,
    "Under Article 71(1), all doubts and disputes arising out of or in connection with the election of a President or Vice-President shall be inquired into and decided by the Supreme Court whose decision shall be final.",
    {"A": "ECI conducts the election, but disputes go to SC.", "B": "Correct. Supreme Court of India exclusively under Article 71.", "C": "Parliament cannot decide election disputes.", "D": "High Court has no jurisdiction under Art. 71."},
    "Easy", "Article 71(1)", "Recall exclusive Supreme Court jurisdiction in election disputes."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-008", "ch-09", "top-const-09-01",
    "Can the election of a President be called in question on the ground of the existence of any vacancy in the Electoral College?",
    ["Yes, if a major State Assembly was dissolved", "No, Article 71(4) explicitly bars challenging the election on the ground of any vacancy in the electoral college", "Yes, on a petition by 20 electors", "Only if more than 50% seats were vacant"],
    1,
    "Article 71(4) (inserted by 11th Amendment 1961) explicitly provides: 'The election of a person as President or Vice-President shall not be called in question on the ground of the existence of any vacancy for whatever reason among the members of the electoral college electing him'.",
    {"A": "Overruled in Presidential Election 1974 reference.", "B": "Correct. Article 71(4) prohibits challenges based on vacancy.", "C": "Petitions cannot challenge vacancy.", "D": "Vacancy percentage is legally immaterial."},
    "Medium", "Article 71(4)", "Master rule on vacancies in Presidential Electoral College."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-009", "ch-09", "top-const-09-01",
    "Who elects the Vice-President of India under Article 66?",
    ["Elected members of Lok Sabha and Rajya Sabha only", "An electoral college consisting of the members of both Houses of Parliament (both elected and nominated)", "Elected MPs and elected MLAs", "All members of Lok Sabha only"],
    1,
    "Under Article 66(1), the Vice-President is elected by the members of an electoral college consisting of the members of BOTH Houses of Parliament (both elected and nominated). State Legislative Assemblies play NO role in electing the Vice-President.",
    {"A": "Nominated MPs also vote in VP election.", "B": "Correct. All members of both Houses of Parliament (elected + nominated).", "C": "MLAs do not vote for Vice-President.", "D": "Rajya Sabha participates equally."},
    "Easy", "Article 66(1)", "Recall Vice-Presidential Electoral College."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-010", "ch-09", "top-const-09-01",
    "How can the Vice-President of India be removed from office under Article 67(b)?",
    ["By impeachment identical to Article 61", "By a resolution of the Council of States passed by a majority of all the then members and agreed to by the House of the People", "By an order of the President in his discretion", "By a reference to the Supreme Court"],
    1,
    "Under Article 67(b), the Vice-President may be removed by a resolution of the Rajya Sabha passed by a majority of all the then members (effective majority) and agreed to by the Lok Sabha (simple majority), following at least 14 days notice.",
    {"A": "VP removal is not termed impeachment.", "B": "Correct. Effective majority in Rajya Sabha + Agreement of Lok Sabha.", "C": "President cannot unilaterally remove VP.", "D": "Supreme Court has no removal role."},
    "Medium", "Article 67(b)", "Explain procedure for removal of Vice-President."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-011", "ch-09", "top-const-09-01",
    "What is the minimum age qualification for election as President or Vice-President of India?",
    ["25 years", "30 years", "35 years", "40 years"],
    2,
    "Under Article 58(1)(b) (President) and Article 66(3)(b) (Vice-President), a candidate must have completed the age of thirty-five (35) years.",
    {"A": "25 years is for Lok Sabha / Vidhan Sabha.", "B": "30 years is for Rajya Sabha / Vidhan Parishad.", "C": "Correct. 35 years for President, Vice-President, and Governor.", "D": "40 years is incorrect."},
    "Easy", "Articles 58 & 66", "Recall age qualification for President and VP."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-012", "ch-09", "top-const-09-01",
    "Under the President (Discharge of Functions) Act, 1969, who acts as President when the offices of both the President and the Vice-President fall vacant simultaneously?",
    ["The Prime Minister", "The Speaker of the Lok Sabha", "The Chief Justice of India (or in his absence, the senior-most Judge of the Supreme Court)", "The Attorney-General"],
    2,
    "Under the President (Discharge of Functions) Act, 1969, if both offices are vacant, the Chief Justice of India (or the senior-most judge of the Supreme Court) discharges the functions of the President (as done by Justice M. Hidayatullah in 1969).",
    {"A": "Prime Minister cannot act as President.", "B": "Speaker is next in line in US succession, not India.", "C": "Correct. Chief Justice of India (or senior-most SC Judge).", "D": "Attorney-General is a law officer."},
    "Medium", "President (Discharge of Functions) Act, 1969", "Recall succession line in dual vacancy."
))

# 09-13 to 09-24: Executive Powers, Clemency & Ordinances (Arts 72 & 123)
MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-013", "ch-09", "top-const-09-02",
    "Under Article 72, the President of India has the power to grant pardons in which of the following cases?",
    ["In all cases where the punishment or sentence is for an offence against a Union law", "In all cases where the punishment or sentence is by a Court Martial", "In all cases where the sentence is a sentence of death", "In all of the above three categories"],
    3,
    "Article 72(1) confers pardoning power across three spheres: (a) offences against laws relating to Union executive competence; (b) sentences by Court Martial; and (c) all cases where the sentence is a sentence of death.",
    {"A": "True under Art. 72(1)(a).", "B": "True under Art. 72(1)(b).", "C": "True under Art. 72(1)(c).", "D": "Correct. In all of the above three categories."},
    "Easy", "Article 72(1)", "Recall the three jurisdictions of Article 72."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-014", "ch-09", "top-const-09-02",
    "What is the legal difference between a 'Pardon' and 'Commutation' under Article 72?",
    ["Pardon reduces sentence length; Commutation grants bail", "Pardon completely wipes out both the conviction and sentence; Commutation substitutes a lighter form of punishment for the sentence awarded", "Commutation is done by the Governor; Pardon is done by the President", "They are identical in legal effect"],
    1,
    "A Pardon completely absolves the offender from the guilt of the crime and wipes out both punishment and disqualifications, restoring him to innocence. Commutation merely substitutes a lighter form of punishment (e.g. death to life imprisonment) without erasing the conviction.",
    {"A": "Reduction of length without changing nature is Remission.", "B": "Correct. Pardon wipes out guilt; Commutation substitutes lighter penalty.", "C": "Both powers exist in Art. 72.", "D": "Distinct legal effects."},
    "Medium", "Article 72 Clemency Types", "Distinguish Pardon from Commutation."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-015", "ch-09", "top-const-09-02",
    "In Maru Ram v. Union of India (1980), the Supreme Court settled that the pardoning power of the President under Article 72:",
    ["Is a personal discretionary prerogative of the President", "Must be exercised strictly on the aid and advice of the Council of Ministers (Union Cabinet)", "Requires concurrence of the Chief Justice of India", "Cannot be exercised without parliamentary approval"],
    1,
    "In Maru Ram (1980), Justice V.R. Krishna Iyer ruled that the President does not exercise personal discretion under Article 72: the advice of the Central Government is binding on the Head of the Republic, and clemency powers cannot be exercised arbitrarily.",
    {"A": "Personal discretion was firmly rejected.", "B": "Correct. Must be exercised on the binding advice of the Council of Ministers.", "C": "CJI concurrence is not required.", "D": "Parliamentary approval is not required."},
    "Medium", "Maru Ram v. Union of India (1981) 1 SCC 107", "Affirm cabinet advice in Article 72 clemency."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-016", "ch-09", "top-const-09-02",
    "In Kehar Singh v. Union of India (1989), a 5-Judge Constitution Bench ruled that under Article 72, the President:",
    ["Is bound by the findings of fact recorded by the Supreme Court", "Can scrutinize the evidence on record afresh and come to a different conclusion from that arrived at by the judicial court", "Can only grant clemency on medical grounds", "Must hold an oral hearing of the convict"],
    1,
    "In Kehar Singh (1989), Chief Justice R.S. Pathak held that the President under Article 72 is entitled to go into the merits of the case afresh and can arrive at a conclusion different from that of the courts, though the convict has no right to insist on an oral hearing.",
    {"A": "President is not bound by judicial fact findings.", "B": "Correct. President can examine evidence afresh and differ from court.", "C": "Clemency is not limited to medical grounds.", "D": "Convict has no right to oral hearing."},
    "Hard", "Kehar Singh v. Union of India (1989) 1 SCC 204", "Master Kehar Singh Article 72 doctrine."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-017", "ch-09", "top-const-09-02",
    "In Epuru Sudhakar v. Govt. of A.P. (2006), the Supreme Court held that the exercise of pardoning power under Article 72/161 is:",
    ["Completely immune from judicial review", "Subject to limited judicial review on grounds of mala fides, extraneous considerations, or non-application of mind", "Subject to appeal before a High Court bench", "Reviewable only on grounds of financial cost"],
    1,
    "In Epuru Sudhakar (2006), the Supreme Court ruled that while courts cannot question the merits of a clemency decision, the order is open to judicial challenge if passed without application of mind, with mala fides, based on irrelevant considerations, or influenced by caste/political favoritism.",
    {"A": "Absolute immunity was rejected.", "B": "Correct. Limited judicial review for mala fides, irrelevant grounds, non-application of mind.", "C": "Not an ordinary appeal.", "D": "Financial cost is irrelevant."},
    "Medium", "Epuru Sudhakar (2006) 8 SCC 161", "Recall grounds for judicial review of clemency."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-018", "ch-09", "top-const-09-02",
    "Under Article 123, when can the President promulgate an Ordinance?",
    ["At any time when the Prime Minister requests it", "Only when both Houses of Parliament are NOT in session, or when either of the two Houses is not in session", "Only during a Proclamation of National Emergency", "Only with the prior consent of the Supreme Court"],
    1,
    "Under Article 123(1), the President can promulgate an Ordinance only when BOTH Houses of Parliament are not in session, or when EITHER of the two Houses is not in session (since a bill requires the passage of both Houses to become law).",
    {"A": "Cannot promulgate when both Houses are sitting.", "B": "Correct. When both or either of the two Houses is not in session.", "C": "Emergency is not a prerequisite.", "D": "Judicial consent is not needed."},
    "Medium", "Article 123(1)", "Identify session condition for promulgation of Ordinances."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-019", "ch-09", "top-const-09-02",
    "An Ordinance promulgated by the President under Article 123 ceases to operate at the expiration of what period from the reassembly of Parliament?",
    ["Two weeks", "Four weeks", "Six weeks", "Three months"],
    2,
    "Under Article 123(2)(a), an Ordinance shall cease to operate at the expiration of SIX WEEKS from the reassembly of Parliament, or earlier if disapproved by resolutions passed by both Houses.",
    {"A": "Two weeks is incorrect.", "B": "Four weeks is incorrect.", "C": "Correct. Six weeks from reassembly.", "D": "Three months is incorrect."},
    "Easy", "Article 123(2)(a)", "Recall 6-week expiry window of Ordinances."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-020", "ch-09", "top-const-09-02",
    "What is the maximum theoretical lifespan of an Ordinance promulgated under Article 123 if Parliament does not approve it?",
    ["6 months", "6 weeks", "7.5 months (6 months maximum recess + 6 weeks from reassembly)", "1 year"],
    2,
    "Since Article 85 mandates that six months shall not intervene between two sessions of Parliament, the maximum interval is 6 months, plus 6 weeks from reassembly before it lapses, yielding a maximum lifespan of 7.5 months.",
    {"A": "Under-inclusive (ignores 6 weeks).", "B": "Applies only post-reassembly.", "C": "Correct. 6 months gap + 6 weeks post-reassembly = 7.5 months.", "D": "1 year is incorrect."},
    "Medium", "Articles 85 & 123", "Calculate maximum lifespan of an Ordinance."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-021", "ch-09", "top-const-09-02",
    "In D.C. Wadhwa v. State of Bihar (1987) and Krishna Kumar Singh v. State of Bihar (2017), the Supreme Court held that repeated repromulgation of Ordinances without placing them before the Legislature is:",
    ["A valid exercise of emergency powers", "A fraud on the Constitution and a subversion of the democratic legislative process", "Permissible if approved by the Governor", "Reviewable only by the Election Commission"],
    1,
    "In D.C. Wadhwa (1987) and the 7-Judge Bench in Krishna Kumar Singh (2017), the Supreme Court held that repromulgating ordinances without placing them before the legislature is a fraud on the Constitution and subverts parliamentary democracy, rendering such repromulgated ordinances void.",
    {"A": "Cannot bypass legislative primacy.", "B": "Correct. A fraud on the Constitution and subversion of democracy.", "C": "Governor cannot validate unconstitutional repromulgation.", "D": "ECI has no role."},
    "Medium", "Krishna Kumar Singh (2017) 3 SCC 1", "Master repromulgation doctrine in Krishna Kumar Singh."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-022", "ch-09", "top-const-09-02",
    "Can an Ordinance promulgated under Article 123 amend the Constitution of India?",
    ["Yes, if passed during an emergency", "No, an Ordinance has the same limitations as an Act of Parliament and cannot amend the Constitution", "Yes, with the consent of 50% of the States", "Yes, by inserting a non-obstante clause"],
    1,
    "Article 123(3) provides that if an Ordinance makes any provision which Parliament would not under this Constitution be competent to enact, it shall be void. An Ordinance is an ordinary legislative power and CANNOT amend the Constitution under Article 368.",
    {"A": "Emergency does not permit ordinance amendment.", "B": "Correct. An Ordinance cannot amend the Constitution.", "C": "State consent does not apply to ordinances.", "D": "Non-obstante clause cannot override Art. 368."},
    "Easy", "Article 123(3)", "Affirm rule that Ordinance cannot amend Constitution."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-023", "ch-09", "top-const-09-02",
    "Is the 'Satisfaction of the President' to promulgate an Ordinance under Article 123 subject to judicial review?",
    ["No, it is completely non-justiciable", "Yes, in A.K. Roy v. Union of India (1982), the Supreme Court settled that presidential satisfaction is justiciable on grounds of mala fides or colourable exercise of power", "Only if challenged by the Speaker of Lok Sabha", "Only during President's Rule"],
    1,
    "The 38th Amendment (1975) had made presidential satisfaction final and non-justiciable. The 44th Amendment (1978) deleted this ouster. In A.K. Roy (1982), the Supreme Court settled that presidential satisfaction is open to judicial challenge if it is mala fide or a colourable exercise of power.",
    {"A": "44th Amendment deleted the ouster clause.", "B": "Correct. Justiciable on grounds of mala fides or colourable exercise.", "C": "Any aggrieved citizen can challenge.", "D": "Applies across all times."},
    "Hard", "A.K. Roy v. Union of India (1982) 1 SCC 271", "Examine justiciability of presidential satisfaction."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-024", "ch-09", "top-const-09-02",
    "What is the difference between the pardoning power of the Governor under Article 161 and the President under Article 72 regarding death sentences?",
    ["Governor has wider pardoning powers than President", "President can grant a complete Pardon for death sentences; Governor cannot pardon death sentences, though he can suspend, remit, or commute them", "Governor can pardon court martial sentences", "President cannot commute death sentences"],
    1,
    "Under Article 72 and 161, only the President has the sovereign power to grant a complete PARDON (wiping out conviction and sentence) in cases of death penalty. The Governor under Article 161 can only suspend, remit, or commute a death sentence, but CANNOT pardon it.",
    {"A": "President's power is wider.", "B": "Correct. Only President can pardon death sentences; Governor can only suspend/remit/commute.", "C": "Governor has zero power over court martial.", "D": "President routinely commutes death sentences."},
    "Medium", "Articles 72 & 161 Comparison", "Distinguish Presidential from Gubernatorial death clemency."
))

# 09-25 to 09-35: Prime Minister, Council of Ministers & Attorney-General
MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-025", "ch-09", "top-const-09-03",
    "Article 74(1) as amended by the 42nd and 44th Amendments provides that the President:",
    ["May disregard cabinet advice in his discretion", "Shall act in accordance with the aid and advice of the Council of Ministers, but may require them to reconsider such advice once, and is bound by the reconsidered advice", "Is bound by the advice of the Chief Justice of India", "Must refer all cabinet decisions to Parliament"],
    1,
    "The 42nd Amendment made cabinet advice explicitly binding on the President. The 44th Amendment added a proviso: the President may require the Council of Ministers to reconsider such advice once, but the President SHALL act in accordance with the advice tendered after reconsideration.",
    {"A": "Discretionary rejection was barred.", "B": "Correct. May send back once for reconsideration; bound thereafter.", "C": "CJI does not tender executive advice.", "D": "Cabinet decisions do not go to Parliament for prior approval."},
    "Easy", "Article 74(1) Proviso", "Master 44th Amendment Article 74(1) reconsideration proviso."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-026", "ch-09", "top-const-09-03",
    "Under Article 74(2), can courts inquire into the advice tendered by Ministers to the President?",
    ["Yes, courts have plenary power to inspect all cabinet minutes", "No, Article 74(2) bars inquiry into whether any, and if so what, advice was tendered by Ministers to the President", "Yes, upon an application under the RTI Act", "Only in criminal prosecutions for treason"],
    1,
    "Article 74(2) explicitly provides: 'The question whether any, and if so what, advice was tendered by Ministers to the President shall not be inquired into in any court'. However, background materials placed before cabinet are not immune (S.R. Bommai).",
    {"A": "Article 74(2) explicitly bars inquiry.", "B": "Correct. Article 74(2) bars judicial inquiry into cabinet advice.", "C": "RTI does not override Article 74(2).", "D": "No treason exception."},
    "Medium", "Article 74(2)", "Recall Article 74(2) bar on inquiring into ministerial advice."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-027", "ch-09", "top-const-09-03",
    "Under Article 75(3), the Council of Ministers is collectively responsible to:",
    ["The Parliament of India", "The House of the People (Lok Sabha)", "The Council of States (Rajya Sabha)", "The President of India"],
    1,
    "Article 75(3) unambiguously states: 'The Council of Ministers shall be collectively responsible to the House of the People'. Ministers are not responsible to the Rajya Sabha.",
    {"A": "Parliament includes Rajya Sabha, to which cabinet is not collectively responsible.", "B": "Correct. House of the People (Lok Sabha).", "C": "Rajya Sabha cannot pass a vote of no-confidence.", "D": "Individual responsibility under pleasure doctrine (Art. 75(2))."},
    "Easy", "Article 75(3)", "Identify collective responsibility to Lok Sabha."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-028", "ch-09", "top-const-09-03",
    "Under Article 75(1A), the total number of Ministers, including the Prime Minister, in the Council of Ministers shall not exceed:",
    ["10% of the total number of members of the Lok Sabha", "15% of the total number of members of the House of the People (Lok Sabha)", "20% of the total membership of Parliament", "Fifty members in total"],
    1,
    "The 91st Constitutional Amendment Act, 2003 inserted Article 75(1A), restricting the size of the Union Council of Ministers, including the Prime Minister, to not exceed 15% of the total number of members of the House of the People.",
    {"A": "10% applies to Delhi Assembly (Art. 239AA), not Union Cabinet.", "B": "Correct. 15% of the total membership of Lok Sabha.", "C": "Parliament membership is not the denominator.", "D": "Fixed number is incorrect."},
    "Easy", "Article 75(1A) & 91st Amendment", "Recall 15% ceiling on Council of Ministers."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-029", "ch-09", "top-const-09-03",
    "Under Article 75(5), for what maximum consecutive period can a person remain a Minister without being a member of either House of Parliament?",
    ["Three months", "Six months", "One year", "Two years"],
    1,
    "Article 75(5) provides: 'A Minister who for any period of six consecutive months is not a member of either House of Parliament shall at the expiration of that period cease to be a Minister'.",
    {"A": "Three months is incorrect.", "B": "Correct. Six consecutive months.", "C": "One year is incorrect.", "D": "Two years is incorrect."},
    "Easy", "Article 75(5)", "Recall 6-month non-MP ministerial window."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-030", "ch-09", "top-const-09-03",
    "In Shamsher Singh v. State of Punjab (1974), a 7-Judge Constitution Bench established that:",
    ["The President and Governors are constitutional heads who must act on cabinet advice in all cases except where discretionary action is specifically mandated", "The President can dismiss the Prime Minister at will", "Ministers are civil servants under Article 311", "Governor's discretion is unlimited"],
    0,
    "In Shamsher Singh (1974), Chief Justice A.N. Ray held that the President and Governor are constitutional heads of an executive operating on the Westminster model; executive power vested in them is exercised strictly on the advice of the Council of Ministers.",
    {"A": "Correct. Constitutional heads acting strictly on cabinet advice.", "B": "PM commanding majority cannot be dismissed.", "C": "Ministers are political executives, not Art. 311 civil servants.", "D": "Governor's discretion is strictly limited."},
    "Medium", "Shamsher Singh (1974) 2 SCC 831", "Master Shamsher Singh constitutional head doctrine."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-031", "ch-09", "top-const-09-03",
    "Under Article 76, what qualification is required for appointment as the Attorney-General for India?",
    ["Must be qualified to be appointed a Judge of the Supreme Court", "Must be a Senior Advocate of at least 15 years standing", "Must be an elected Member of Parliament", "Must have served as a High Court Chief Justice for 5 years"],
    0,
    "Article 76(1) states: 'The President shall appoint a person who is qualified to be appointed a Judge of the Supreme Court to be Attorney-General for India'.",
    {"A": "Correct. Qualified to be appointed a Judge of the Supreme Court.", "B": "Advocate standing alone is not the constitutional phrase.", "C": "AG is not a Member of Parliament.", "D": "HC Chief Justice service is not required."},
    "Easy", "Article 76(1)", "Recall qualifications for Attorney-General."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-032", "ch-09", "top-const-09-03",
    "What is the tenure of office of the Attorney-General for India under Article 76(4)?",
    ["Five years from the date of appointment", "Holds office until the age of 65 years", "Holds office during the pleasure of the President", "Holds office during the pleasure of the Chief Justice of India"],
    2,
    "Article 76(4) explicitly provides: 'The Attorney-General shall hold office during the pleasure of the President, and shall receive such remuneration as the President may determine'.",
    {"A": "No fixed 5-year tenure.", "B": "65 years applies to SC judges, not AG.", "C": "Correct. Holds office during the pleasure of the President.", "D": "CJI has no tenure control."},
    "Easy", "Article 76(4)", "Recall tenure of Attorney-General."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-033", "ch-09", "top-const-09-03",
    "Under Article 76(3), in which courts does the Attorney-General for India enjoy the 'Right of Audience'?",
    ["Only in the Supreme Court of India", "In all courts in the territory of India", "In the Supreme Court and High Courts only", "Only before Constitution Benches"],
    1,
    "Article 76(3) provides: 'In the performance of his duties the Attorney-General shall have right of audience in all courts in the territory of India'.",
    {"A": "Under-inclusive.", "B": "Correct. In all courts in the territory of India.", "C": "Under-inclusive (includes subordinate courts too).", "D": "Under-inclusive."},
    "Easy", "Article 76(3)", "Recall territorial right of audience of AG."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-034", "ch-09", "top-const-09-03",
    "Under Article 88, the Attorney-General for India has the right to speak and take part in proceedings of Parliament, BUT does NOT have the right to:",
    ["Introduce government bills", "Vote in any proceedings or joint sittings of Parliament", "Address parliamentary committees", "Attend sittings of the Lok Sabha"],
    1,
    "Article 88 confers upon the Attorney-General the right to speak and take part in proceedings of either House, any joint sitting, and any committee of Parliament of which he may be named a member, but by virtue of this article he is NOT entitled to vote.",
    {"A": "Can assist in legislative debates.", "B": "Correct. Has NO right to vote in Parliament.", "C": "Can address committees if nominated.", "D": "Can attend sittings."},
    "Easy", "Article 88", "Recall Article 88 bar on Attorney-General voting."
))

MCQS_CH09_11.append(create_mcq(
    "mcq-const-09-035", "ch-09", "top-const-09-03",
    "Under Article 78, which of the following is a constitutional duty of the Prime Minister towards the President?",
    ["To communicate all decisions of the Council of Ministers relating to administration and legislation", "To submit for the consideration of the Council of Ministers any matter on which a decision has been taken by a Minister but not considered by the Council", "To furnish such information relating to administration and legislation as the President may call for", "All of the above are constitutional duties under Article 78"],
    3,
    "Article 78 defines the PM as the vital communication channel between the Cabinet and the President, encompassing all three duties: (a) communicating cabinet decisions; (b) furnishing information called for; and (c) submitting individual minister decisions for cabinet consideration when required by President.",
    {"A": "True under Art. 78(a).", "B": "True under Art. 78(c).", "C": "True under Art. 78(b).", "D": "Correct. All of the above are duties under Article 78."},
    "Medium", "Article 78", "Recall duties of Prime Minister under Article 78."
))

print(f"Chapter 9 complete ({len(MCQS_CH09_11)} total).")
''')

print("Chapter 9 appended.")
