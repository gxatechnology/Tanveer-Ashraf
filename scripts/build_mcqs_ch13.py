"""
Builds 25 MCQs for Chapter 13: Emergency Provisions (Articles 352–360).
Topics:
- top-const-13-01: 13 MCQs (National Emergency, Art 352, 358, 359, 44th Amendment)
- top-const-13-02: 12 MCQs (President's Rule Art 356, Bommai, Financial Emergency Art 360)
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

MCQS_CH13 = []

# ==============================================================================
# TOPIC 13-01: NATIONAL EMERGENCY (13 MCQs)
# ==============================================================================

MCQS_CH13.append(create_mcq(
    "mcq-const-13-001", "ch-13", "top-const-13-01",
    "Under Article 352(1), on which three grounds can the President declare a Proclamation of National Emergency?",
    ["War, External Aggression, or Internal Disturbance", "War, External Aggression, or Armed Rebellion", "Financial Instability, War, or Communal Riot", "Breakdown of Law and Order, War, or Insurgency"],
    1,
    "Article 352(1) (as amended by 44th Amendment Act 1978) specifies three grounds: 'War, External Aggression, or Armed Rebellion'. The phrase 'Internal Disturbance' was deleted because of its vague and subjective misuse during the 1975 emergency.",
    {"A": "'Internal Disturbance' was substituted by 'Armed Rebellion' via the 44th Amendment.", "B": "Correct. War, External Aggression, or Armed Rebellion.", "C": "Financial instability triggers Art. 360, not Art. 352.", "D": "Breakdown of law and order is not a ground under Art. 352."},
    "Easy", "Article 352(1) & 44th Amendment", "Recall the three constitutional grounds for National Emergency."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-002", "ch-13", "top-const-13-01",
    "Which Constitutional Amendment Act substituted the phrase 'Internal Disturbance' with 'Armed Rebellion' in Article 352?",
    ["42nd Amendment Act, 1976", "44th Amendment Act, 1978", "52nd Amendment Act, 1985", "86th Amendment Act, 2002"],
    1,
    "The 44th Constitutional Amendment Act, 1978 replaced 'internal disturbance' with 'armed rebellion' in Article 352(1) to prevent subjective political misuse of emergency powers.",
    {"A": "42nd Amendment added 'internal disturbance' provisions and made proclamation non-justiciable.", "B": "Correct. 44th Amendment Act, 1978 substituted 'armed rebellion'.", "C": "52nd Amendment introduced the Anti-Defection law.", "D": "86th Amendment inserted Article 21A (Right to Education)."},
    "Easy", "Article 352 & 44th Amendment", "Identify the amendment substituting 'internal disturbance'."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-003", "ch-13", "top-const-13-01",
    "Under Article 352(3) inserted by the 44th Amendment Act, 1978, the President shall not issue a Proclamation of Emergency unless:",
    ["The Prime Minister verbally instructs the President", "The decision of the Union Cabinet (consisting of the Prime Minister and other Ministers of Cabinet rank) that such a Proclamation may be issued has been communicated to him in WRITING", "The Chief Justice of India gives a written certificate of emergency", "Both Houses of Parliament pass a joint resolution beforehand"],
    1,
    "Article 352(3) mandates: 'The President shall not issue a Proclamation under clause (1) or a Proclamation varying such Proclamation unless the decision of the Union Cabinet (that is to say, the Council consisting of the Prime Minister and other Ministers of Cabinet rank appointed under article 75) that such a Proclamation may be issued has been communicated to him in WRITING'.",
    {"A": "Verbal PM instruction was the flaw of the 1975 emergency corrected by 44th Amendment.", "B": "Correct. Written communication of decision of the Union Cabinet.", "C": "CJI has no role in declaring emergency.", "D": "Parliamentary approval comes after proclamation, within one month."},
    "Medium", "Article 352(3)", "Master safeguards introduced by 44th Amendment regarding Cabinet written advice."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-004", "ch-13", "top-const-13-01",
    "What is the time period within which a Proclamation of National Emergency under Article 352 must be approved by both Houses of Parliament?",
    ["Within fourteen days", "Within ONE MONTH from the date of its issue", "Within two months from the date of its issue", "Within six months"],
    1,
    "Under Article 352(4) (amended by 44th Amendment from earlier 2 months to 1 month), every Proclamation shall cease to operate at the expiration of ONE MONTH unless before the expiration of that period it has been approved by resolutions of both Houses of Parliament.",
    {"A": "Fourteen days is notice period for impeachment or Speaker removal.", "B": "Correct. Exactly one month (reduced from two months by 44th Amendment).", "C": "Two months applies to Article 356 (President's Rule) and Article 360 (Financial Emergency).", "D": "Six months is duration after approval."},
    "Medium", "Article 352(4)", "Recall approval timeframe for National Emergency."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-005", "ch-13", "top-const-13-01",
    "What majority is required in each House of Parliament to approve or extend a Proclamation of National Emergency under Article 352(6)?",
    ["Simple majority of members present and voting", "A majority of the total membership of that House AND a majority of not less than two-thirds of the members of that House present and voting", "Three-fourths majority of total membership", "Absolute majority of Lok Sabha alone"],
    1,
    "Article 352(6) mandates a special majority: 'a majority of the total membership of that House and by a majority of not less than two-thirds of the members of that House present and voting'. (Introduced by the 44th Amendment; previously simple majority was sufficient).",
    {"A": "Simple majority was abolished for Art. 352 by 44th Amendment (still applies to Art. 356 and 360).", "B": "Correct. Majority of total membership AND 2/3rds present and voting.", "C": "Three-fourths is not prescribed anywhere in the Constitution.", "D": "Both Houses must approve."},
    "Medium", "Article 352(6)", "Distinguish parliamentary majority for Art. 352 vs Art. 356."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-006", "ch-13", "top-const-13-01",
    "Once approved by Parliament, for how long does a Proclamation of National Emergency remain in force under Article 352(5)?",
    ["One month", "Three months", "SIX MONTHS (and can be extended indefinitely every six months with parliamentary approval)", "One year"],
    2,
    "Under Article 352(5), an approved emergency remains in force for SIX MONTHS unless revoked earlier. It can be extended repeatedly for six months at a time with fresh parliamentary approval. There is no constitutional upper limit on total duration for Art. 352.",
    {"A": "One month is the initial pre-approval lifespan.", "B": "Three months is not the statutory duration.", "C": "Correct. Six months at a time, with indefinite extension potential.", "D": "One year is maximum life under Art. 356 without EC certificate."},
    "Medium", "Article 352(5)", "Recall duration and renewal rules of National Emergency."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-007", "ch-13", "top-const-13-01",
    "Under Article 352(7) and (8), how can the Lok Sabha compel the disapproval or revocation of a National Emergency?",
    ["By passing a motion of no-confidence against the Speaker", "If not less than 1/10th of the total members of Lok Sabha give written notice, a special sitting must be held within 14 days, and the President MUST revoke the emergency if Lok Sabha passes a resolution disapproving it by simple majority", "By filing a writ in the High Court", "Lok Sabha cannot revoke; revocation is sole prerogative of the President"],
    1,
    "Under Article 352(7) & (8) (added by 44th Amendment), if not less than 1/10th members of Lok Sabha give notice in writing to the Speaker (or President if House not in session), a special sitting shall be held within 14 days. If Lok Sabha passes a disapproval resolution by simple majority, the President must revoke the proclamation.",
    {"A": "Speaker motion is separate under Art. 94.", "B": "Correct. 1/10th notice, special sitting within 14 days, disapproval by simple majority.", "C": "Judicial review is parallel, but parliamentary disapproval is legislative check.", "D": "44th Amendment removed President's sole monopoly on revocation."},
    "Hard", "Article 352(7) & (8)", "Master Lok Sabha disapproval mechanism for National Emergency."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-008", "ch-13", "top-const-13-01",
    "Under Article 358(1), which Fundamental Right is automatically suspended during a National Emergency declared on the grounds of WAR or EXTERNAL AGGRESSION?",
    ["Article 14 (Right to Equality)", "Article 19 (Six Democratic Freedoms)", "Article 21 (Right to Life and Personal Liberty)", "Article 25 (Freedom of Religion)"],
    1,
    "Article 358(1) provides for the automatic suspension of Article 19 freedoms while a proclamation of emergency is in operation. Following the 44th Amendment, Article 358 operates ONLY when emergency is declared on grounds of 'war or external aggression', NOT on 'armed rebellion'.",
    {"A": "Article 14 is suspended only under Art. 359 by presidential order, not automatically under Art. 358.", "B": "Correct. Article 19 is automatically suspended under Article 358.", "C": "Article 21 can NEVER be suspended (44th Amendment).", "D": "Article 25 is not automatically suspended."},
    "Easy", "Article 358(1)", "Recall automatic suspension of Article 19 under Article 358."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-009", "ch-13", "top-const-13-01",
    "Does Article 358 automatically suspend the freedoms guaranteed under Article 19 when a National Emergency is declared on the ground of ARMED REBELLION?",
    ["Yes, Article 19 is suspended in all forms of emergency", "No, by virtue of the 44th Amendment Act, 1978, Article 19 is suspended under Article 358 ONLY when emergency is declared on grounds of WAR or EXTERNAL AGGRESSION (External Emergency)", "Yes, if approved by a 2/3rds majority of Parliament", "Yes, in the border states only"],
    1,
    "The 44th Amendment Act, 1978 amended Article 358 to restrict automatic suspension of Article 19 strictly to emergencies proclaimed on grounds of 'war or external aggression'. If declared on 'armed rebellion' (internal emergency), Article 19 remains fully operative and cannot be automatically suspended.",
    {"A": "Incorrect; 44th Amendment created explicit carve-out.", "B": "Correct. Art. 19 is suspended ONLY for War/External Aggression, NOT Armed Rebellion.", "C": "Parliamentary majority does not alter the text of Art. 358.", "D": "Border state restriction is not part of Art. 358."},
    "Hard", "Article 358 & 44th Amendment", "Distinguish external vs internal emergency impacts on Article 19."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-010", "ch-13", "top-const-13-01",
    "Under Article 359(1) (as amended by the 44th Amendment Act, 1978), the President can suspend the right to move any court for the enforcement of Fundamental Rights EXCEPT:",
    ["Articles 14 and 19", "Articles 20 and 21", "Articles 25 and 26", "Articles 32 and 226"],
    1,
    "Article 359(1) provides that the President may by order suspend the right to move any court for enforcement of specified Fundamental Rights, 'EXCEPT ARTICLES 20 AND 21'. Following the 44th Amendment (overruling the infamous ADM Jabalpur ruling), the right to protection against retrospective criminal laws, double jeopardy, self-incrimination (Art. 20) and the right to life and liberty (Art. 21) can NEVER be suspended.",
    {"A": "Articles 14 and 19 can be suspended by Presidential order under Art. 359.", "B": "Correct. Articles 20 and 21 are absolute and immune from suspension under Article 359.", "C": "Religious freedoms can be suspended if specified in order.", "D": "Writ remedies for non-excepted rights can be suspended."},
    "Easy", "Article 359(1) & 44th Amendment", "Recall absolute immunity of Articles 20 & 21 during Emergency."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-011", "ch-13", "top-const-13-01",
    "In which infamous decision did the Supreme Court hold by 4:1 majority that during a Presidential Order under Article 359, no person had locus standi to move a High Court for habeas corpus to challenge detention, which was later universally condemned and formally overruled in K.S. Puttaswamy (2017)?",
    ["A.K. Gopalan v. State of Madras (1950)", "A.D.M. Jabalpur v. Shivkant Shukla (1976)", "Minerva Mills v. Union of India (1980)", "Maneka Gandhi v. Union of India (1978)"],
    1,
    "In A.D.M. Jabalpur v. Shivkant Shukla (1976) (Habeas Corpus Case), the majority held that Art. 21 was the sole repository of right to life and liberty, and once suspended under Art. 359, no writ lay even against illegal detentions. Justice H.R. Khanna famously dissented. The ruling was nullified by the 44th Amendment and formally overruled in K.S. Puttaswamy (2017).",
    {"A": "Gopalan was early Art. 21 case on procedure established by law.", "B": "Correct. ADM Jabalpur (1976) — the Habeas Corpus case.", "C": "Minerva Mills dealt with basic structure and Art. 368.", "D": "Maneka Gandhi expanded Art. 21 substantive due process."},
    "Medium", "Article 359 & ADM Jabalpur (1976)", "Recall landmark habeas corpus case and Justice H.R. Khanna's dissent."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-012", "ch-13", "top-const-13-01",
    "What is the effect of a Proclamation of National Emergency on the life of the Lok Sabha under the Proviso to Article 83(2)?",
    ["Lok Sabha is dissolved immediately", "The life of the Lok Sabha may be extended by Parliament by law for a period NOT EXCEEDING ONE YEAR AT A TIME, and not extending beyond six months after the proclamation has ceased to operate", "Lok Sabha continues automatically without any law for 5 years", "All elections are cancelled permanently"],
    1,
    "Under the Proviso to Article 83(2), while a Proclamation of Emergency is in operation, the normal 5-year duration of the Lok Sabha may be extended by Parliament by law for a period not exceeding one year at a time, and not extending beyond six months after the Proclamation has ceased to operate. (During 1975-77, the 5th Lok Sabha was extended twice).",
    {"A": "Lok Sabha is not automatically dissolved.", "B": "Correct. Extended by law up to 1 year at a time, max 6 months post-emergency.", "C": "Requires specific parliamentary legislation.", "D": "Elections cannot be cancelled permanently."},
    "Medium", "Article 83(2) Proviso", "Recall rule on extending parliamentary life during National Emergency."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-013", "ch-13", "top-const-13-01",
    "Under Article 353(a), what is the executive effect of a Proclamation of National Emergency on State Governments?",
    ["State Governments are dismissed automatically", "The executive power of the Union extends to the giving of directions to any State as to the manner in which the executive power thereof is to be exercised (State Governments continue, but under complete Union executive control)", "State Governors assume independent sovereign powers", "Supreme Court administers the States directly"],
    1,
    "Under Article 353(a), during a National Emergency, State Governments are NOT dismissed (unlike under Art. 356). Instead, the Union executive acquires power to issue binding directions to any State on any matter whatsoever, effectively transforming the federal system into a unitary one.",
    {"A": "State Governments are dismissed under Art. 356, NOT under Art. 352.", "B": "Correct. Union acquires power to issue directions on any executive matter.", "C": "Governors do not become independent sovereigns.", "D": "Supreme Court does not administer states."},
    "Hard", "Article 353(a)", "Distinguish executive impact of Art. 352 vs Art. 356."
))

# ==============================================================================
# TOPIC 13-02: PRESIDENT'S RULE & FINANCIAL EMERGENCY (12 MCQs)
# ==============================================================================

MCQS_CH13.append(create_mcq(
    "mcq-const-13-014", "ch-13", "top-const-13-02",
    "Under Article 356(1), on what ground can the President issue a Proclamation imposing President's Rule in a State?",
    ["If the State Government fails to repay central loans", "If the President, on receipt of a report from the Governor of a State or otherwise, is satisfied that a situation has arisen in which the government of the State cannot be carried on in accordance with the provisions of this Constitution", "If communal violence breaks out in two districts", "If the ruling party loses an election in another state"],
    1,
    "Article 356(1) states: 'If the President, on receipt of a report from the Governor of a State or otherwise, is satisfied that a situation has arisen in which the government of the State cannot be carried on in accordance with the provisions of this Constitution', he may assume state executive powers.",
    {"A": "Financial default triggers Art. 360, not Art. 356.", "B": "Correct. Government cannot be carried on in accordance with the Constitution.", "C": "Routine law and order breakdown is insufficient (S.R. Bommai).", "D": "Electoral loss elsewhere is political and unconstitutional ground."},
    "Easy", "Article 356(1)", "Recall ground for imposition of President's Rule."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-015", "ch-13", "top-const-13-02",
    "Under Article 365 of the Constitution, what is the consequence if a State fails to comply with, or give effect to, any directions given in the exercise of the executive power of the Union?",
    ["The Union can cut off water supply to the State", "It shall be lawful for the President to hold that a situation has arisen in which the government of the State cannot be carried on in accordance with the provisions of this Constitution (triggering Article 356)", "The State High Court is dissolved", "The Governor is dismissed by the Chief Justice of India"],
    1,
    "Article 365 provides that where any State fails to comply with or give effect to any directions given by the Union, it shall be lawful for the President to hold that a situation has arisen in which the government of the State cannot be carried on in accordance with the provisions of the Constitution, enabling invocation of Article 356.",
    {"A": "Cutting off basic utilities is unconstitutional.", "B": "Correct. State non-compliance triggers presumption of constitutional breakdown under Art. 365.", "C": "High Courts cannot be dissolved under emergency powers.", "D": "Governor is appointed/removed by President, not CJI."},
    "Medium", "Article 365 & 356 Linkage", "Understand Article 365 as a trigger for Article 356."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-016", "ch-13", "top-const-13-02",
    "What is the time period within which a Proclamation under Article 356 must be approved by both Houses of Parliament?",
    ["Within one month", "Within TWO MONTHS from the date of its issue", "Within three months", "Within six months"],
    1,
    "Under Article 356(3), every Proclamation shall cease to operate at the expiration of TWO MONTHS unless before the expiration of that period it has been approved by resolutions of both Houses of Parliament. (Note: Article 352 is 1 month; Article 356 is 2 months).",
    {"A": "One month applies to Article 352 (National Emergency).", "B": "Correct. Exactly two months for Article 356.", "C": "Three months is incorrect.", "D": "Six months is the duration after approval."},
    "Medium", "Article 356(3)", "Contrast approval windows: Art. 352 (1 month) vs Art. 356 (2 months)."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-017", "ch-13", "top-const-13-02",
    "What parliamentary majority is required to approve a Proclamation under Article 356?",
    ["Simple majority of members present and voting in each House", "Special majority (2/3rds present and voting + absolute majority)", "Joint sitting passed by 3/4ths majority", "Ratification by half of the States"],
    0,
    "A Proclamation under Article 356 (President's Rule) requires approval by a SIMPLE MAJORITY of members present and voting in each House of Parliament (unlike Article 352 which requires a dual-tier special majority under Art. 352(6)).",
    {"A": "Correct. Simple majority of members present and voting.", "B": "Special majority is required for Article 352 and 368, NOT Article 356.", "C": "No provision for joint sitting exists under Art. 356.", "D": "State ratifications are not required."},
    "Medium", "Article 356 Parliamentary Approval", "Identify majority required to pass President's Rule resolution."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-018", "ch-13", "top-const-13-02",
    "What is the NORMAL maximum duration for which President's Rule under Article 356 can remain in force?",
    ["One year", "THREE YEARS (extended every 6 months with parliamentary approval)", "Five years", "Indefinitely without limit"],
    1,
    "Under Article 356(4) first proviso, the maximum period for which Article 356 can remain in force in a State is THREE YEARS. (Beyond 1 year, the stringent conditions of clause (5) must be satisfied).",
    {"A": "One year is the threshold before clause (5) conditions apply.", "B": "Correct. Three years is the outer constitutional limit under Article 356.", "C": "Five years was applied exceptionally only in Punjab via 67th and 68th Amendments.", "D": "Indefinite extension applies to Article 352, not Article 356."},
    "Medium", "Article 356(4)", "Recall outer time limit for President's Rule."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-019", "ch-13", "top-const-13-02",
    "Under Article 356(5) (inserted by the 44th Amendment Act, 1978), what two mandatory conditions must exist to extend President's Rule BEYOND ONE YEAR?",
    ["Unemployment above 10% OR Governor's special petition", "A Proclamation of Emergency is in operation (in the whole of India or in that State) AND the Election Commission certifies that continuation is necessary due to difficulties in holding general elections", "Approval by the Supreme Court AND consent of the ousted Chief Minister", "Armed rebellion in two neighbouring States"],
    1,
    "Article 356(5) mandates that beyond one year, a resolution can only be passed if: (a) a Proclamation of Emergency under Art. 352 is in operation; AND (b) the Election Commission certifies that holding general elections to the Legislative Assembly of the State is difficult.",
    {"A": "Unemployment is not a constitutional ground.", "B": "Correct. National Emergency in operation + Election Commission certificate.", "C": "Supreme Court approval is not a legislative prerequisite.", "D": "Neighbouring state conditions do not satisfy clause (5)."},
    "Hard", "Article 356(5) & 44th Amendment", "Master conditions precedent for extending President's Rule beyond one year."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-020", "ch-13", "top-const-13-02",
    "In the landmark nine-judge bench judgment in S.R. Bommai v. Union of India (1994), what major constitutional restriction was placed on the dissolution of a State Legislative Assembly under Article 356?",
    ["The Legislative Assembly can never be dissolved under Article 356", "The Legislative Assembly CANNOT be dissolved until the Proclamation is approved by BOTH HOUSES of Parliament; until then, the Assembly can only be kept under SUSPENDED ANIMATION", "The Governor can dissolve the Assembly immediately upon submitting his report", "The Assembly can be dissolved only if 50% MLAs resign"],
    1,
    "In S.R. Bommai (1994), the 9-judge bench held that the Legislative Assembly cannot be dissolved merely upon the issuance of the Proclamation under Art. 356. It can only be kept in 'suspended animation'. Dissolution can take place ONLY AFTER both Houses of Parliament have approved the Proclamation. If Parliament disapproves, the dismissed ministry and suspended assembly revive.",
    {"A": "Assembly can be dissolved after parliamentary approval.", "B": "Correct. Suspended animation only until Parliament approves; dissolution only post-approval.", "C": "Immediate dissolution was held unconstitutional in Bommai.", "D": "MLA resignations do not dictate Art. 356 rules."},
    "Hard", "Article 356 & S.R. Bommai (1994)", "Explain assembly dissolution restrictions laid down in S.R. Bommai."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-021", "ch-13", "top-const-13-02",
    "What power does the Supreme Court possess if a Proclamation under Article 356 is struck down as malafide and unconstitutional as laid down in S.R. Bommai v. Union of India (1994)?",
    ["The Supreme Court can only order financial compensation to the dismissed ministers", "The Supreme Court has the power to RESTORE the dismissed State Government and REVIVE the dissolved Legislative Assembly (status quo ante)", "The Supreme Court must order fresh parliamentary elections", "The Supreme Court cannot reverse the dissolution once published in the Gazette"],
    1,
    "In S.R. Bommai (1994), the Supreme Court established that Article 356 is subject to judicial review. If the proclamation is found invalid, the Court has the power to restore the dismissed ministry and revive the dissolved State Legislative Assembly to status quo ante (as famously applied in Arunachal Pradesh / Nabam Rebia in 2016).",
    {"A": "Compensation is not the constitutional remedy.", "B": "Correct. Power to restore dismissed Ministry and revive dissolved Assembly (status quo ante).", "C": "Parliamentary elections are unaffected.", "D": "Gazette publication does not insulate unconstitutional action from judicial review."},
    "Hard", "Article 356 & S.R. Bommai (1994)", "Recall Supreme Court's power to restore state governments."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-022", "ch-13", "top-const-13-02",
    "Under Article 356(1)(b), upon the issuance of President's Rule, what happens to the legislative powers of the State Legislature?",
    ["They are transferred to the High Court of the State", "The President may declare that the powers of the Legislature of the State shall be exercisable by or under the authority of PARLIAMENT", "They are exercised by the State Chief Secretary", "They remain suspended and no laws can be passed for the State"],
    1,
    "Article 356(1)(b) states that the President may 'declare that the powers of the Legislature of the State shall be exercisable by or under the authority of Parliament'. Under Art. 357, Parliament may also delegate this power to the President.",
    {"A": "High Courts do not exercise legislative functions.", "B": "Correct. Powers exercisable by or under the authority of Parliament.", "C": "Chief Secretary is an administrative civil servant.", "D": "Laws continue to be enacted via Parliament or President under Art. 357."},
    "Medium", "Article 356(1)(b) & 357", "Recall transfer of state legislative powers during President's Rule."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-023", "ch-13", "top-const-13-02",
    "Can the President assume the powers of the State High Court under Article 356 of the Constitution?",
    ["Yes, all state organs including the High Court come under the President", "No, Article 356(1) PROVISO explicitly bars the President from assuming any of the powers vested in or exercisable by a High Court, or suspending any constitutional provision relating to High Courts", "Yes, with the concurrence of the Chief Justice of India", "Yes, during external war"],
    1,
    "The Proviso to Article 356(1) is an absolute constitutional carve-out: 'Provided that nothing in this clause shall authorise the President to assume to himself any of the powers vested in or exercisable by a High Court, or to suspend in whole or in part the operation of any provision of this Constitution relating to High Courts'.",
    {"A": "Incorrect; High Court powers are strictly protected.", "B": "Correct. Proviso explicitly bars assumption or suspension of High Court powers.", "C": "CJI concurrence cannot override express constitutional bar.", "D": "External war does not alter the Proviso to Art. 356(1)."},
    "Medium", "Article 356(1) Proviso", "Identify constitutional protection of High Courts during President's Rule."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-024", "ch-13", "top-const-13-02",
    "Under Article 360(1), on what ground can the President declare a Financial Emergency?",
    ["If the national debt exceeds 50% of GDP", "If the President is satisfied that a situation has arisen whereby the FINANCIAL STABILITY or CREDIT of India or of any part of the territory thereof is THREATENED", "If the annual budget is defeated in the Lok Sabha", "If the Reserve Bank of India reports negative reserves"],
    1,
    "Article 360(1) states: 'If the President is satisfied that a situation has arisen whereby the financial stability or credit of India or of any part of the territory thereof is threatened, he may by a Proclamation make a declaration to that effect'.",
    {"A": "Debt percentage is an economic indicator, not constitutional test.", "B": "Correct. Threat to financial stability or credit of India or any part thereof.", "C": "Budget defeat leads to ministry resignation, not financial emergency.", "D": "RBI reserve level is not the constitutional wording."},
    "Easy", "Article 360(1)", "Recall constitutional ground for Financial Emergency."
))

MCQS_CH13.append(create_mcq(
    "mcq-const-13-025", "ch-13", "top-const-13-02",
    "Which of the following extraordinary executive directions can be issued during a Financial Emergency under Article 360(4)(b)?",
    ["Dissolution of all commercial banks", "A direction requiring the REDUCTION OF SALARIES AND ALLOWANCES of all or any class of persons serving in connection with the affairs of the Union, INCLUDING THE JUDGES OF THE SUPREME COURT AND THE HIGH COURTS", "Confiscation of gold jewellery of citizens", "Printing of unlimited paper currency without backing"],
    1,
    "Under Article 360(4)(b), the President can issue directions for the reduction of salaries and allowances of all or any class of persons serving in connection with the affairs of the Union, including the Judges of the Supreme Court and the High Courts. (India has NEVER declared a Financial Emergency to date).",
    {"A": "Bank dissolution is not authorized under Art. 360.", "B": "Correct. Reduction of salaries of Union employees including Supreme Court and High Court Judges.", "C": "Gold confiscation is unconstitutional.", "D": "Unlimited currency printing is not an Art. 360 power."},
    "Medium", "Article 360(4)(b)", "Identify executive powers regarding salary reductions during Financial Emergency."
))

if __name__ == "__main__":
    print(f"Generated {len(MCQS_CH13)} MCQs for Chapter 13.")
