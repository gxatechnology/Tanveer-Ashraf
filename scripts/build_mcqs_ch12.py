"""
Builds 45 MCQs for Chapter 12: The Union & State Judiciary.
Topics:
- top-const-12-01: 12 MCQs (Structure of SC & Appointments, Collegium)
- top-const-12-02: 12 MCQs (Jurisdictions: Original, Appellate, SLP, Advisory)
- top-const-12-03: 10 MCQs (Court of Record, Precedent, Art 142, Contempt)
- top-const-12-04: 11 MCQs (High Courts, Writs, Subordinate Courts)
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

MCQS_CH12 = []

# ==============================================================================
# TOPIC 12-01: STRUCTURE & APPOINTMENTS (12 MCQs)
# ==============================================================================

MCQS_CH12.append(create_mcq(
    "mcq-const-12-001", "ch-12", "top-const-12-01",
    "Under Article 124(1), who has the power to increase the number of Judges of the Supreme Court of India?",
    ["The President of India by executive notification", "The Parliament of India by law", "The Chief Justice of India with approval of the Full Court", "The Law Commission of India"],
    1,
    "Article 124(1) states: 'There shall be a Supreme Court of India consisting of a Chief Justice of India and, until Parliament by law prescribes a larger number, of not more than seven other Judges'. Parliament alone has the authority to increase judge strength by ordinary law.",
    {"A": "President cannot unilaterally increase judge strength without parliamentary statute.", "B": "Correct. Parliament by law (Supreme Court Number of Judges Acts).", "C": "CJI cannot alter statutory strength.", "D": "Law Commission is recommendatory."},
    "Easy", "Article 124(1)", "Recall authority empowered to alter Supreme Court judge strength."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-002", "ch-12", "top-const-12-01",
    "What is the current sanctioned strength of the Supreme Court of India (including the Chief Justice of India) following the Supreme Court (Number of Judges) Amendment Act, 2019?",
    ["31 Judges", "34 Judges (33 + 1 CJI)", "35 Judges", "38 Judges"],
    1,
    "The Supreme Court (Number of Judges) Amendment Act, 2019 increased the maximum number of judges from 30 to 33, excluding the Chief Justice of India, bringing total sanctioned strength to exactly 34 (33 Puisne Judges + 1 CJI).",
    {"A": "31 was the strength under the 2008 Act.", "B": "Correct. 34 Judges (33 Puisne Judges + Chief Justice of India).", "C": "35 is incorrect.", "D": "38 is incorrect."},
    "Easy", "Article 124(1) & Act of 2019", "Recall current sanctioned strength of the Supreme Court."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-003", "ch-12", "top-const-12-01",
    "Under Article 124(3), which of the following is NOT a prescribed qualification for appointment as a Judge of the Supreme Court?",
    ["Has been for at least 5 years a Judge of a High Court", "Has been for at least 10 years an advocate of a High Court", "Is, in the opinion of the President, a distinguished jurist", "Has served as a District Judge for at least 7 years"],
    3,
    "Under Article 124(3), the three alternative qualifications are: (a) 5 years as High Court Judge; (b) 10 years as High Court advocate; or (c) in President's opinion, a distinguished jurist. Direct appointment from Subordinate Judiciary (District Judge) without serving as HC Judge or 10-year HC advocate is not a constitutional qualification.",
    {"A": "5 years as HC judge is valid under Art. 124(3)(a).", "B": "10 years as HC advocate is valid under Art. 124(3)(b).", "C": "Distinguished jurist is valid under Art. 124(3)(c).", "D": "Correct. 7 years as District Judge is qualification for High Court (Art. 217(2)(a)), not Supreme Court."},
    "Medium", "Article 124(3) & 217(2)", "Distinguish qualifications for Supreme Court vs High Court."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-004", "ch-12", "top-const-12-01",
    "In the Second Judges Case (Supreme Court Advocates-on-Record Association v. Union of India, 1993), what meaning was assigned to the word 'consultation' in Article 124(2)?",
    ["Consultation means mere exchange of informal views without binding effect", "Consultation means 'concurrence', and the opinion of the Chief Justice of India formed with the two senior-most colleagues has primacy", "Executive has ultimate veto over judicial appointments", "Consultation requires approval by a parliamentary select committee"],
    1,
    "Overruling S.P. Gupta (First Judges Case, 1981), the 9-judge bench in the Second Judges Case (1993) held that 'consultation' under Article 124(2) means 'concurrence'. The Chief Justice of India's opinion, arrived at in consultation with his two senior-most colleagues, enjoys constitutional primacy.",
    {"A": "Mere exchange of views was the overruled holding of S.P. Gupta (1981).", "B": "Correct. Consultation means concurrence, establishing primacy of CJI-led collegium.", "C": "Executive primacy was rejected.", "D": "Parliamentary committee has no constitutional role."},
    "Medium", "Article 124(2) & Second Judges Case (1993)", "Master the evolution of the Collegium System."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-005", "ch-12", "top-const-12-01",
    "In the Third Judges Case (Special Reference No. 1 of 1998), the Supreme Court expanded the Collegium for appointment of Supreme Court Judges to include:",
    ["The CJI and two senior-most judges", "The CJI and four senior-most puisne judges of the Supreme Court", "The CJI, Union Law Minister, and Leader of Opposition", "All sitting judges of the Supreme Court"],
    1,
    "Under the Presidential Reference under Article 143 (Third Judges Case, 1998), the Supreme Court held that for appointment of Supreme Court judges, the CJI must consult a collegium of the FOUR SENIOR-MOST puisne judges of the Supreme Court. For High Court appointments, the collegium consists of CJI and two senior-most judges.",
    {"A": "CJI + 2 senior-most judges applies to High Court appointments.", "B": "Correct. CJI + 4 senior-most judges for Supreme Court appointments.", "C": "NJAC structure was struck down in 2015.", "D": "Full court does not constitute the collegium."},
    "Medium", "Article 143 & Third Judges Case (1998)", "Identify composition of the 5-member Supreme Court Collegium."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-006", "ch-12", "top-const-12-01",
    "In Supreme Court Advocates-on-Record Association v. Union of India (2015) (Fourth Judges Case), the Supreme Court struck down the 99th Constitutional Amendment Act and the NJAC Act on the ground that:",
    ["Judicial appointments can only be made by the Union Public Service Commission", "The National Judicial Appointments Commission (NJAC) violated the independence of judiciary, which is a Basic Feature of the Constitution", "The law was passed without requisite state ratifications", "The Law Minister cannot be an advocate"],
    1,
    "By a 4:1 majority, the Constitution Bench struck down the 99th Amendment Act, 2014 and the NJAC Act, 2014 holding that the inclusion of the Union Law Minister and two eminent persons infringed upon the independence of the judiciary, which is an inviolable basic feature of the Constitution.",
    {"A": "UPSC has no role in higher judicial appointments.", "B": "Correct. NJAC breached judicial independence as part of the Basic Structure.", "C": "State ratifications had been obtained; invalidation was on substantive Basic Structure grounds.", "D": "Ministerial status was not the ground."},
    "Hard", "Article 124A & Fourth Judges Case (2015)", "Explain constitutional invalidation of the NJAC Act."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-007", "ch-12", "top-const-12-01",
    "Under Article 124(4), what is the majority required in Parliament to pass an address for the removal of a Supreme Court Judge?",
    ["Simple majority of members present and voting in both Houses", "A majority of the total membership of each House AND a majority of not less than two-thirds of the members of that House present and voting", "Absolute majority of the Lok Sabha alone", "Two-thirds of total membership of Rajya Sabha alone"],
    1,
    "Article 124(4) mandates a rigorous dual-tier special majority: 'supported by a majority of the total membership of that House and by a majority of not less than two-thirds of the members of that House present and voting'.",
    {"A": "Simple majority is inadequate for judicial removal.", "B": "Correct. Majority of total membership AND 2/3rds present and voting in each House.", "C": "Both Houses must pass the address in the same session.", "D": "Rajya Sabha alone cannot remove a judge."},
    "Medium", "Article 124(4)", "Recall special majority required for judicial removal."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-008", "ch-12", "top-const-12-01",
    "Under the Judges (Inquiry) Act, 1968, what is the composition of the Inquiry Committee appointed by the Speaker/Chairman to investigate charges against a Supreme Court or High Court judge?",
    ["Three members: One SC Judge, one Chief Justice of a High Court, and one distinguished jurist", "Five members of Parliament from ruling and opposition parties", "The Chief Justice of India and two Union Ministers", "Three retired Supreme Court Judges"],
    0,
    "Section 3(2) of the Judges (Inquiry) Act, 1968 mandates a 3-member committee: (a) one chosen from among the Supreme Court judges; (b) one chosen from among the Chief Justices of the High Courts; and (c) one distinguished jurist.",
    {"A": "Correct. One SC judge + one HC Chief Justice + one distinguished jurist.", "B": "MPs do not form the judicial inquiry committee.", "C": "Union Ministers cannot sit on the inquiry committee.", "D": "Must include a sitting HC Chief Justice and a distinguished jurist."},
    "Hard", "Judges (Inquiry) Act, 1968 Section 3", "Recall composition of statutory judicial inquiry committee."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-009", "ch-12", "top-const-12-01",
    "To whom does a Judge of the Supreme Court address his resignation in writing under Article 124(2) proviso (a)?",
    ["The Chief Justice of India", "The President of India", "The Prime Minister of India", "The Speaker of the Lok Sabha"],
    1,
    "Article 124(2) proviso (a) provides: 'a Judge may, by writing under his hand addressed to the President, resign his office'.",
    {"A": "Resignation is not addressed to the CJI.", "B": "Correct. Addressed to the President of India.", "C": "Prime Minister is not the appointing authority.", "D": "Speaker has no role in receiving judicial resignations."},
    "Easy", "Article 124(2) proviso (a)", "Recall recipient of Supreme Court Judge resignation."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-010", "ch-12", "top-const-12-01",
    "Under Article 124(7), what post-retirement restriction is placed on a person who has held office as a Judge of the Supreme Court?",
    ["Shall not contest any election for 5 years", "Shall not plead or act in any court or before any authority within the territory of India", "Shall not write legal commentaries or textbooks", "Shall not accept any commission of inquiry"],
    1,
    "Article 124(7) imposes a total constitutional bar: 'No person who has held office as a Judge of the Supreme Court shall plead or act in any court or before any authority within the territory of India'.",
    {"A": "No 5-year election ban is imposed by Art. 124(7).", "B": "Correct. Absolute bar from pleading or acting before any court or authority in India.", "C": "Academic writing is permitted.", "D": "Inquiry commissions are administrative appointments, not pleading/acting."},
    "Medium", "Article 124(7)", "Recall constitutional bar on post-retirement practice for SC judges."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-011", "ch-12", "top-const-12-01",
    "Under Article 127, who can appoint an ad hoc Judge of the Supreme Court if there is a lack of quorum of judges to hold or continue any session?",
    ["The President of India unilaterally", "The Chief Justice of India, with previous consent of the President and after consultation with the Chief Justice of the High Court concerned", "The Parliament by special resolution", "The Union Law Ministry"],
    1,
    "Article 127(1) provides: The Chief Justice of India may, with the previous consent of the President and after consultation with the Chief Justice of the High Court concerned, request in writing a High Court Judge duly qualified to attend sittings of the Supreme Court as an ad hoc Judge.",
    {"A": "President cannot appoint ad hoc judge unilaterally.", "B": "Correct. CJI with previous consent of President and consultation with HC Chief Justice.", "C": "Parliament does not appoint ad hoc judges.", "D": "Law Ministry has no appointing authority under Art. 127."},
    "Hard", "Article 127", "Master procedure for appointing ad hoc Supreme Court judges."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-012", "ch-12", "top-const-12-01",
    "Under Article 128, the Chief Justice of India may request a retired Judge of the Supreme Court or Federal Court to sit and act as a Judge of the Supreme Court, subject to:",
    ["Approval by 2/3rds majority of Parliament", "Previous consent of the President and consent of the retired person requested", "An order of the Union Cabinet", "Passing a fresh fitness examination"],
    1,
    "Article 128 states that the CJI may, with the previous consent of the President, request any retired Supreme Court or Federal Court judge to sit and act as a Judge of the Supreme Court. Proviso mandates that no such person shall be required to sit and act unless he consents.",
    {"A": "Parliamentary approval is not required.", "B": "Correct. Previous consent of President AND consent of the retired judge.", "C": "Cabinet order is irrelevant.", "D": "No examination exists for constitutional judges."},
    "Medium", "Article 128", "Recall procedure for attendance of retired judges at Supreme Court sittings."
))

# ==============================================================================
# TOPIC 12-02: JURISDICTIONS OF THE SUPREME COURT (12 MCQs)
# ==============================================================================

MCQS_CH12.append(create_mcq(
    "mcq-const-12-013", "ch-12", "top-const-12-02",
    "Under Article 131, which of the following disputes falls within the EXCLUSIVE ORIGINAL JURISDICTION of the Supreme Court of India?",
    ["A dispute between a citizen and the Government of India", "A dispute between two private corporate entities", "A dispute between the Government of India and one or more States, or between two or more States, involving any question of legal right", "A dispute regarding sharing of inter-state river waters"],
    2,
    "Article 131 vests exclusive original jurisdiction in disputes: (a) between GoI and one or more States; (b) between GoI and any State(s) on one side and other State(s) on the other; or (c) between two or more States, if the dispute involves any question on which existence/extent of a legal right depends.",
    {"A": "Disputes involving private citizens/companies do not fall under Art. 131 (State of Bihar v. Union of India).", "B": "Private corporate disputes go to ordinary civil courts.", "C": "Correct. Inter-governmental disputes involving legal rights.", "D": "Inter-state river water disputes are excluded under Art. 262 and Inter-State River Water Disputes Act 1956."},
    "Medium", "Article 131", "Define parameters of Supreme Court's exclusive original jurisdiction."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-014", "ch-12", "top-const-12-02",
    "Can a private individual or corporation be a party to an original suit filed in the Supreme Court under Article 131?",
    ["Yes, if their fundamental rights are violated", "No, in State of Bihar v. Union of India (1970), the Supreme Court held that Article 131 applies strictly to inter-governmental disputes between constituent units of the federation", "Yes, if they are co-plaintiffs with a State Government", "Yes, in public interest litigation"],
    1,
    "In State of Bihar v. Union of India (1970), the Supreme Court ruled that Article 131 is exclusively designed for federal disputes between constituent units (Union and States). A private entity or citizen cannot join an Article 131 suit as plaintiff or co-plaintiff.",
    {"A": "Fundamental rights are enforced under Art. 32, not Art. 131.", "B": "Correct. Private parties cannot be parties to Article 131 suits.", "C": "Co-plaintiff status is barred for private parties under Art. 131.", "D": "PIL is under Art. 32, not Art. 131 original suits."},
    "Hard", "Article 131 & State of Bihar v. UOI (1970)", "Recall rule regarding private litigants in Article 131."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-015", "ch-12", "top-const-12-02",
    "Which of the following matters is explicitly EXCLUDED from the original jurisdiction of the Supreme Court under the Proviso to Article 131?",
    ["Disputes arising out of any pre-Constitution treaty, agreement, covenant, or engagement", "Boundary disputes between two adjoining States", "Disputes regarding GST compensation cess", "Disputes regarding central police deployment in a State"],
    0,
    "The Proviso to Article 131 explicitly excludes disputes arising out of any treaty, agreement, covenant, engagement, sanad or other similar instrument entered into or executed before the commencement of the Constitution.",
    {"A": "Correct. Pre-Constitution treaties, covenants, and engagements are barred under Art. 131 proviso.", "B": "Inter-state boundary disputes are covered under Art. 131.", "C": "Tax/cess disputes between Union and States involve legal rights under Art. 131.", "D": "Police deployment disputes can be contested under Art. 131."},
    "Medium", "Article 131 Proviso", "Identify constitutional exclusion from Article 131 jurisdiction."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-016", "ch-12", "top-const-12-02",
    "Under Article 132(1), an appeal lies to the Supreme Court from any judgment, decree or final order of a High Court (whether civil, criminal or other proceeding) if the High Court certifies under Article 134A that:",
    ["The value of the subject matter exceeds rupees ten lakhs", "The case involves a substantial question of law as to the INTERPRETATION OF THIS CONSTITUTION", "The accused has been awarded life imprisonment", "A Central Minister is a respondent in the proceedings"],
    1,
    "Article 132(1) confers constitutional appellate jurisdiction where the High Court certifies under Article 134A that the case involves a substantial question of law as to the interpretation of this Constitution.",
    {"A": "Valuation threshold was abolished by 30th Amendment Act 1972.", "B": "Correct. Substantial question of law as to the interpretation of the Constitution.", "C": "Life imprisonment falls under criminal appeals (Art. 134), not constitutional interpretation.", "D": "Minister status does not grant appellate right."},
    "Easy", "Article 132(1)", "Recall threshold test for constitutional appellate jurisdiction."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-017", "ch-12", "top-const-12-02",
    "Under Article 133(1), what certificate must the High Court grant under Article 134A for a civil appeal to lie to the Supreme Court?",
    ["That the subject matter exceeds Rs. 1 crore", "That the case involves a substantial question of law of general importance, and that in the opinion of the High Court the said question needs to be decided by the Supreme Court", "That the plaintiff is a registered charitable trust", "That both parties have consented to Supreme Court appeal"],
    1,
    "Following the 30th Amendment Act, 1972, Article 133(1) requires the High Court to certify: (a) that the case involves a substantial question of law of general importance; and (b) that in the opinion of the High Court the said question needs to be decided by the Supreme Court.",
    {"A": "Pecuniary valuation test was removed in 1972.", "B": "Correct. Substantial question of law of general importance needing SC decision.", "C": "Charitable status is irrelevant.", "D": "Consent of parties cannot confer appellate jurisdiction."},
    "Medium", "Article 133(1) & 30th Amendment", "Master requirements for civil appeals under Article 133."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-018", "ch-12", "top-const-12-02",
    "Under Article 134(1)(a) and (b), in which criminal cases does an appeal lie to the Supreme Court AS OF RIGHT (without needing a High Court certificate of fitness)?",
    ["Where the High Court has on appeal reversed an order of acquittal of an accused person and sentenced him to death", "Where the High Court has sentenced the accused to 3 years imprisonment", "Where the trial court has acquitted the accused and High Court upheld acquittal", "Where bail has been rejected by the High Court"],
    0,
    "Under Article 134(1)(a), an appeal lies as of right if the High Court has on appeal reversed an acquittal order and sentenced the accused to death; or under (b) withdrawn a trial to itself and sentenced the accused to death.",
    {"A": "Correct. Reversed acquittal and sentenced to death gives automatic appeal as of right.", "B": "3-year sentence requires certificate under Art. 134(1)(c) or SLP.", "C": "Upheld acquittal gives no automatic appeal as of right.", "D": "Bail rejections do not qualify under Art. 134(1)(a)."},
    "Medium", "Article 134(1)", "Identify cases where criminal appeal lies as of right."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-019", "ch-12", "top-const-12-02",
    "Under Article 136(1), the Supreme Court may grant Special Leave to Appeal (SLP) from:",
    ["Final orders of High Courts in civil matters only", "Any judgment, decree, determination, sentence or order in any cause or matter passed or made by ANY COURT OR TRIBUNAL in India", "Supreme Court judgments only", "District Court orders directly bypassing High Courts in all instances"],
    1,
    "Article 136(1) is an extraordinary plenary power: 'the Supreme Court may, in its discretion, grant special leave to appeal from any judgment, decree, determination, sentence or order in any cause or matter passed or made by any court or tribunal in the territory of India'.",
    {"A": "Not restricted to High Courts or civil matters; covers all causes.", "B": "Correct. Any court or tribunal in any cause or matter in India.", "C": "Review is under Art. 137, not SLP.", "D": "While SLP can theoretically bypass HC, plenary text covers any court/tribunal."},
    "Easy", "Article 136(1)", "Recall broad scope of Special Leave Petition jurisdiction."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-020", "ch-12", "top-const-12-02",
    "Under Article 136(2), which specific category of courts or tribunals is EXEMPT from the Special Leave jurisdiction of the Supreme Court?",
    ["National Green Tribunal", "Central Administrative Tribunal", "Any court or tribunal constituted by or under any law relating to the ARMED FORCES (Court Martial)", "Consumer Disputes Redressal Commissions"],
    2,
    "Article 136(2) provides: 'Nothing in clause (1) shall apply to any judgment, determination, sentence or order passed or made by any court or tribunal constituted by or under any law relating to the Armed Forces'.",
    {"A": "NGT appeals lie to Supreme Court.", "B": "CAT orders are amenable to judicial review.", "C": "Correct. Armed Forces courts/tribunals (Court Martial) are excluded under Art. 136(2).", "D": "Consumer commissions fall within tribunal scope."},
    "Medium", "Article 136(2)", "Identify constitutional exemption from Article 136."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-021", "ch-12", "top-const-12-02",
    "Under Article 143(1), on what matters may the President refer a question of law or fact to the Supreme Court for advisory opinion?",
    ["Only on proposed constitutional amendments", "If it appears to the President that a question of law or fact has arisen, or is likely to arise, which is of such a nature and of such public importance that it is expedient to obtain the opinion of the Supreme Court", "Only on tax treaties", "Only when requested by the Leader of the Opposition"],
    1,
    "Article 143(1) provides: 'If at any time it appears to the President that a question of law or fact has arisen, or is likely to arise, which is of such a nature and of such public importance that it is expedient to obtain the opinion of the Supreme Court upon it, he may refer the question to that Court for consideration'.",
    {"A": "Not limited to constitutional amendments.", "B": "Correct. Question of law or fact of public importance arisen or likely to arise.", "C": "Not restricted to tax treaties.", "D": "Opposition leader request is not a constitutional requirement."},
    "Easy", "Article 143(1)", "Recall grounds for Presidential advisory reference."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-022", "ch-12", "top-const-12-02",
    "Is the Supreme Court bound to deliver an advisory opinion on every reference made by the President under Article 143(1)?",
    ["Yes, the Supreme Court is constitutionally compelled to answer all references under Art. 143(1)", "No, under Article 143(1), the Supreme Court has discretion and may, for good and cogent reasons, refuse to answer a reference (as done in the Ayodhya Reference / Ismail Faruqui Case, 1994)", "Yes, unless the reference is returned by the Prime Minister", "No, but it must obtain sanction from Parliament before refusing"],
    1,
    "In In re Special Courts Bill (1978) and M. Ismail Faruqui v. Union of India (Ayodhya Reference, 1994), the Supreme Court settled that under Article 143(1), the Court is NOT bound to answer every reference; it may decline for valid reasons. However, under Article 143(2) (pre-Constitution treaties), the Court is bound to give its opinion.",
    {"A": "Supreme Court is not compelled under Art. 143(1).", "B": "Correct. Court may decline to answer under Art. 143(1) for good reasons (e.g., Ismail Faruqui).", "C": "Executive cannot recall without court's concurrence.", "D": "Parliament has no sanctioning role in Art. 143."},
    "Hard", "Article 143(1) & Ismail Faruqui (1994)", "Distinguish discretionary Art. 143(1) vs mandatory Art. 143(2) references."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-023", "ch-12", "top-const-12-02",
    "What is the binding nature of an advisory opinion delivered by the Supreme Court under Article 143?",
    ["It has the binding force of a decree under Article 141 on all courts in India", "It is purely advisory and NOT binding on the President, nor does it strictly constitute 'law declared' under Article 141, though it carries highest persuasive authority", "It binds the President but does not bind state governments", "It becomes an act of Parliament automatically"],
    1,
    "An opinion rendered under Article 143 is not a judicial pronouncement in an adversarial dispute. It is not binding on the President, and technically does not attract Article 141 (law declared), though because it emanates from the apex court, all subordinate courts treat it with utmost respect and high persuasive value.",
    {"A": "It is not a judgment or decree under Art. 141.", "B": "Correct. Purely advisory, not binding on President, high persuasive value.", "C": "Does not bind President or States as an operative decree.", "D": "Does not become an act of Parliament."},
    "Medium", "Article 143 & In re Special Courts Bill 1978", "Explain legal effect and binding nature of Article 143 opinions."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-024", "ch-12", "top-const-12-02",
    "Under Article 145(3), what is the minimum number of Judges who are to sit for the purpose of deciding any case involving a substantial question of law as to the interpretation of the Constitution, or for hearing a reference under Article 143?",
    ["Three (3) Judges", "Five (5) Judges (Constitution Bench)", "Seven (7) Judges", "Nine (9) Judges"],
    1,
    "Article 145(3) mandates: 'The minimum number of Judges who are to sit for the purpose of deciding any case involving a substantial question of law as to the interpretation of this Constitution or for the purpose of hearing any reference under article 143 shall be FIVE'.",
    {"A": "Three judges constitute a Division Bench.", "B": "Correct. Exactly five (5) judges constitute a Constitution Bench.", "C": "Seven judges is a larger bench.", "D": "Nine judges heard the Second Judges case and Puttaswamy."},
    "Easy", "Article 145(3)", "Recall statutory minimum quorum for a Constitution Bench."
))

# ==============================================================================
# TOPIC 12-03: COURT OF RECORD, PRECEDENT, ART 142 & CONTEMPT (10 MCQs)
# ==============================================================================

MCQS_CH12.append(create_mcq(
    "mcq-const-12-025", "ch-12", "top-const-12-03",
    "Under Article 129 of the Constitution, the Supreme Court is designated as a 'Court of Record', which means that:",
    ["Its records are destroyed after ten years", "Its proceedings and acts are enrolled for perpetual memory and testimony, and it has the inherent power to punish for contempt of itself", "It must maintain an audio recording of all hearings", "It can only hear cases recorded in writing"],
    1,
    "Article 129 declares: 'The Supreme Court shall be a court of record and shall have all the powers of such a court including the power to punish for contempt of itself'. A court of record's acts/proceedings are conclusive evidence and cannot be questioned in any collateral proceeding.",
    {"A": "Records are preserved perpetually, not destroyed.", "B": "Correct. Proceedings enrolled for perpetual testimony + inherent contempt power.", "C": "Audio recording is an administrative measure, not constitutional definition.", "D": "Court of record refers to evidentiary value and contempt power, not mode of hearing."},
    "Easy", "Article 129", "Define constitutional meaning of 'Court of Record'."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-026", "ch-12", "top-const-12-03",
    "Under Article 141 of the Constitution, the law declared by the Supreme Court shall be binding on:",
    ["The Supreme Court itself in all subsequent cases", "All courts within the territory of India", "High Courts only, but not district courts", "The President of India and Council of Ministers only"],
    1,
    "Article 141 states succinctly: 'The law declared by the Supreme Court shall be binding on all courts within the territory of India'. However, the Supreme Court is not bound by its own previous decisions and may overrule them (Bengal Immunity Co. v. State of Bihar, 1955).",
    {"A": "Supreme Court is not rigidly bound by its own decisions (Bengal Immunity).", "B": "Correct. Binding on all courts within the territory of India.", "C": "Binds both High Courts and subordinate courts.", "D": "Applies to 'all courts', not merely executive organs."},
    "Easy", "Article 141 & Bengal Immunity (1955)", "Recall territorial scope of Article 141 doctrine of precedent."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-027", "ch-12", "top-const-12-03",
    "Under Article 142(1), what extraordinary power is conferred on the Supreme Court in the exercise of its jurisdiction?",
    ["Power to pass an order declaring martial law", "Power to pass such decree or make such order as is necessary for doing COMPLETE JUSTICE in any cause or matter pending before it", "Power to dissolve Parliament if it fails to pass bills", "Power to appoint Chief Ministers directly"],
    1,
    "Article 142(1) confers plenary equity jurisdiction: 'The Supreme Court in the exercise of its jurisdiction may pass such decree or make such order as is necessary for DOING COMPLETE JUSTICE in any cause or matter pending before it'.",
    {"A": "Supreme Court cannot declare martial law.", "B": "Correct. Power to do complete justice in any cause or matter.", "C": "Supreme Court cannot dissolve Parliament.", "D": "Appointment of Chief Ministers is executive function."},
    "Easy", "Article 142(1)", "Recall purpose and language of Article 142 plenary equity power."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-028", "ch-12", "top-const-12-03",
    "In Supreme Court Bar Association v. Union of India (1998), what limitation on the power under Article 142 was articulated by the Constitution Bench?",
    ["Article 142 can be used to supersede any express statutory provision", "Article 142 is a supplementary power that cannot be used to supplant substantive statutory law or punish an advocate by suspending their license (which falls exclusively under the Advocates Act, 1961)", "Article 142 cannot be exercised in environmental matters", "Article 142 only applies to tax disputes"],
    1,
    "In SCBA v. UOI (1998), overruling Vinay Chandra Mishra (1995), the Supreme Court ruled that Article 142 is curative and cannot be used to override substantive statutory provisions or usurp the disciplinary jurisdiction of the Bar Council under the Advocates Act, 1961.",
    {"A": "Incorrect; cannot override substantive statutory law.", "B": "Correct. Supplementary power that cannot supplant statutory law or usurp Bar Council's role.", "C": "Article 142 is frequently used in environmental matters.", "D": "Article 142 applies to any cause or matter."},
    "Hard", "Article 142 & SCBA v. UOI (1998)", "Master constitutional limits of Article 142 complete justice power."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-029", "ch-12", "top-const-12-03",
    "Under Article 144, all authorities, civil and judicial, in the territory of India shall:",
    ["Report their financial accounts to the Supreme Court", "Act in aid of the Supreme Court", "Seek permission of the Supreme Court before passing any administrative orders", "Be subordinate to the Attorney-General"],
    1,
    "Article 144 provides: 'All authorities, civil and judicial, in the territory of India shall act in aid of the Supreme Court'.",
    {"A": "Financial accounts go to CAG.", "B": "Correct. Act in aid of the Supreme Court.", "C": "Administrative bodies do not require prior permission for everyday work.", "D": "Subordination to AG is unconstitutional."},
    "Easy", "Article 144", "Recall duty of civil and judicial authorities under Article 144."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-030", "ch-12", "top-const-12-03",
    "Under Article 137, what is the power of the Supreme Court to review its own judgments or orders?",
    ["The Supreme Court has no power to review its own judgments once signed", "The Supreme Court shall have power to review any judgment pronounced or order made by it, subject to the provisions of any law made by Parliament or rules under Article 145", "Judgments can be reviewed only by the President of India", "Review can only be sought by the Attorney-General"],
    1,
    "Article 137 provides: 'Subject to the provisions of any law made by Parliament or any rules made under article 145, the Supreme Court shall have power to review any judgment pronounced or order made by it'. Under Supreme Court Rules, review is filed within 30 days.",
    {"A": "Article 137 expressly provides for review.", "B": "Correct. Supreme Court has power to review its judgments subject to law/rules.", "C": "President has no review jurisdiction over judicial judgments.", "D": "Any aggrieved party can seek review."},
    "Medium", "Article 137", "Recall review jurisdiction of the Supreme Court."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-031", "ch-12", "top-const-12-03",
    "In Rupa Ashok Hurra v. Ashok Hurra (2002), what revolutionary remedy was created by the 5-judge Constitution Bench to prevent miscarriage of justice after a review petition has been dismissed?",
    ["Writ of Quo Warranto", "Curative Petition", "Public Interest Litigation", "Inter-Court Reference"],
    1,
    "In Rupa Ashok Hurra (2002), the Supreme Court evolved the concept of the 'Curative Petition' under inherent powers and Article 142 to cure gross miscarriage of justice or violation of natural justice, even after the dismissal of a review petition under Article 137.",
    {"A": "Quo warranto challenges unauthorized public office holding.", "B": "Correct. Curative Petition created in Rupa Ashok Hurra (2002).", "C": "PIL was developed in late 1970s / 1980s.", "D": "Inter-court reference is not the post-review remedy."},
    "Medium", "Article 137, 142 & Rupa Ashok Hurra (2002)", "Identify origin and purpose of Curative Petitions."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-032", "ch-12", "top-const-12-03",
    "What are the two grounds on which a Curative Petition can be entertained as laid down in Rupa Ashok Hurra v. Ashok Hurra (2002)?",
    ["High value of claim and delay in disposal", "Violation of principles of natural justice AND where a judge failed to disclose bias/interest", "Novelty of arguments and political sensitivity", "Change in government policy"],
    1,
    "A Curative Petition is entertained only on rare grounds: (1) violation of principles of natural justice (e.g., party was not served or heard); or (2) where a judge failed to disclose a personal/financial interest or bias. It must be certified by a Senior Advocate and circulated to the 3 senior-most judges.",
    {"A": "Value of claim is irrelevant.", "B": "Correct. Violation of natural justice and undisclosed judicial bias.", "C": "Novelty of argument is not a ground.", "D": "Policy change does not justify curative remedy."},
    "Hard", "Rupa Ashok Hurra v. Ashok Hurra (2002)", "Recall specific grounds for filing a Curative Petition."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-033", "ch-12", "top-const-12-03",
    "What is the difference between 'Civil Contempt' and 'Criminal Contempt' under Section 2 of the Contempt of Courts Act, 1971?",
    ["Civil contempt is committed by citizens; criminal contempt is committed by government servants", "Civil contempt means wilful disobedience to any judgment, decree, direction, or order of a court; Criminal contempt means publication of any matter or doing any act that scandalises the court, prejudices judicial proceedings, or obstructs administration of justice", "Civil contempt is punishable with death; criminal contempt with fine", "Civil contempt relates to money suits; criminal contempt to murder cases"],
    1,
    "Under Section 2(b), Civil Contempt is wilful disobedience to any judgment, decree, direction, order, writ, or wilful breach of an undertaking given to a court. Under Section 2(c), Criminal Contempt involves scandalising or tending to scandalise the court, prejudicing judicial proceedings, or obstructing justice in any manner.",
    {"A": "Classification is based on nature of act, not identity of offender.", "B": "Correct. Wilful disobedience (Civil) vs scandalising/obstructing justice (Criminal).", "C": "Neither is punishable with death; max imprisonment is 6 months under Sec. 12.", "D": "Contempt classification does not mirror underlying suit classification."},
    "Medium", "Contempt of Courts Act 1971 Sec. 2 & Art. 129", "Distinguish civil contempt from criminal contempt."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-034", "ch-12", "top-const-12-03",
    "Under the Contempt of Courts (Amendment) Act, 2006, which of the following was introduced as a valid defense in contempt proceedings under Section 13(b)?",
    ["Ignorance of law", "Truth, if it is in the public interest and the request for invoking the defense is bona fide", "Superior executive orders", "Apology tendered after conviction"],
    1,
    "The Contempt of Courts (Amendment) Act, 2006 inserted Section 13(b), which provides that the court may permit defense of TRUTH if it is satisfied that it is in public interest and the request for invoking the defense is bona fide.",
    {"A": "Ignorance of law is never a valid defense.", "B": "Correct. Truth in public interest and bona fide is a recognized statutory defense.", "C": "Superior orders cannot justify contempt of court.", "D": "Apology must be bona fide and tendered at earliest stage."},
    "Hard", "Contempt of Courts Act Sec. 13(b) & 2006 Amendment", "Recall defense of truth in contempt proceedings."
))

# ==============================================================================
# TOPIC 12-04: HIGH COURTS & SUBORDINATE COURTS (11 MCQs)
# ==============================================================================

MCQS_CH12.append(create_mcq(
    "mcq-const-12-035", "ch-12", "top-const-12-04",
    "Under Article 214 and Article 216, what is the constitutional provision regarding the maximum number of Judges in a High Court?",
    ["Every High Court shall have exactly 50 judges", "The Constitution does not fix a maximum strength; the High Court consists of a Chief Justice and such other Judges as the President may from time to time deem it necessary to appoint", "The maximum strength is determined by the State Legislature", "No High Court can have more than 100 judges"],
    1,
    "Article 216 provides: 'Every High Court shall consist of a Chief Justice and such other Judges as the President may from time to time deem it necessary to appoint'. Unlike the Supreme Court where Parliament fixes judge strength, High Court strength is determined by the President.",
    {"A": "Strength varies widely across High Courts (e.g., Allahabad has sanctioned 160).", "B": "Correct. President determines High Court judge strength from time to time.", "C": "State Legislature has no power to fix High Court strength.", "D": "Allahabad HC has over 150 sanctioned judges."},
    "Medium", "Article 216", "Explain determination of High Court judge strength."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-036", "ch-12", "top-const-12-04",
    "Under Article 217(1), up to what age does a Judge of a High Court hold office?",
    ["60 years", "62 years", "65 years", "68 years"],
    1,
    "Under Article 217(1) (as amended by 15th Amendment Act 1963), a Judge of a High Court holds office until he attains the age of SIXTY-TWO (62) YEARS. (Supreme Court Judges hold office until age 65).",
    {"A": "60 years was original retirement age before 15th Amendment.", "B": "Correct. 62 years for High Court Judges.", "C": "65 years applies to Supreme Court Judges (Art. 124(2)).", "D": "68 years is not adopted in India."},
    "Easy", "Article 217(1)", "Recall retirement age of High Court Judges."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-037", "ch-12", "top-const-12-04",
    "Under Article 226, the writ jurisdiction of a High Court is WIDER than the writ jurisdiction of the Supreme Court under Article 32 because:",
    ["The High Court can issue writs against foreign nations", "The High Court can issue writs not only for the enforcement of Fundamental Rights, but also 'for any other purpose' (such as enforcement of ordinary legal rights)", "High Court orders cannot be appealed to the Supreme Court", "High Court judges have higher constitutional seniority"],
    1,
    "Under Article 32, the Supreme Court can issue writs ONLY for the enforcement of Fundamental Rights in Part III. Under Article 226, High Courts can issue writs for the enforcement of Fundamental Rights AND 'for any other purpose' (ordinary statutory/legal rights).",
    {"A": "No court can issue writs against foreign sovereign states.", "B": "Correct. 'For any other purpose' allows enforcement of ordinary legal rights.", "C": "High Court orders are appealable to Supreme Court.", "D": "Supreme Court is the apex constitutional court."},
    "Easy", "Article 226 vs Article 32", "Contrast writ jurisdiction of High Court and Supreme Court."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-038", "ch-12", "top-const-12-04",
    "Under Article 226(2), can a High Court issue a writ to a person, authority, or Government located outside its territorial boundaries?",
    ["No, a High Court's writ can never cross state territorial borders", "Yes, if the cause of action arises, wholly or in part, within the territories in relation to which that High Court exercises jurisdiction", "Yes, but only with prior permission of the Governor", "No, unless directed by the Central Government"],
    1,
    "Article 226(2) (inserted by 15th Amendment Act 1963) empowers a High Court to issue directions, orders or writs to any Government, authority or person outside its territorial limits if the cause of action arises, WHOLLY OR IN PART, within its territorial jurisdiction.",
    {"A": "Pre-1963 position (Election Commission v. Saka Venkata Rao) was modified by 15th Amendment.", "B": "Correct. If cause of action arises wholly or in part within its territory.", "C": "Governor permission is not required.", "D": "Executive direction has no role in writ jurisdiction."},
    "Medium", "Article 226(2) & 15th Amendment", "Master extraterritorial writ jurisdiction of High Courts."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-039", "ch-12", "top-const-12-04",
    "Under Article 227 of the Constitution, what power does every High Court possess over all courts and tribunals throughout its territories?",
    ["Power of criminal investigation", "Power of Superintendence over all courts and tribunals (both administrative and judicial superintendence)", "Power of financial auditing", "Power to pass legislative statutes"],
    1,
    "Article 227(1) provides: 'Every High Court shall have superintendence over all courts and tribunals throughout the territories in relation to which it exercises jurisdiction'. This includes both administrative and judicial superintendence (Waryam Singh v. Amarnath, 1954).",
    {"A": "Criminal investigation is an executive police function.", "B": "Correct. Power of Superintendence over all courts and tribunals.", "C": "Financial auditing belongs to CAG.", "D": "Legislation belongs to State Legislature."},
    "Easy", "Article 227", "Define High Court power of superintendence."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-040", "ch-12", "top-const-12-04",
    "Does the High Court's power of superintendence under Article 227 extend to courts or tribunals constituted by or under any law relating to the Armed Forces?",
    ["Yes, all military tribunals are subject to Article 227", "No, Article 227(4) explicitly provides that nothing in Article 227 shall be construed as giving to a High Court any jurisdiction over any court or tribunal constituted by or under any law relating to the Armed Forces", "Yes, if fundamental rights of soldiers are violated", "Yes, upon reference by the Chief of Army Staff"],
    1,
    "Article 227(4) states explicitly: 'Nothing in this article shall be construed as giving to a High Court any jurisdiction to question any judgment of any inferior court which is not otherwise subject to appeal or revision; and nothing in this article shall be construed as giving to a High Court any jurisdiction over any court or tribunal constituted by or under any law relating to the Armed Forces'.",
    {"A": "Armed forces tribunals are excluded.", "B": "Correct. Article 227(4) bars superintendence over Armed Forces courts/tribunals.", "C": "Direct Art. 227 superintendence is barred, though Art. 226 judicial review remains in exceptional cases.", "D": "Army Chief reference cannot bypass Art. 227(4)."},
    "Medium", "Article 227(4)", "Identify constitutional exemption from High Court superintendence."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-041", "ch-12", "top-const-12-04",
    "Under Article 222(1), who has the power to transfer a Judge from one High Court to any other High Court?",
    ["The Chief Justice of India alone without consulting anyone", "The President of India, after consultation with the Chief Justice of India", "The Governor of the transferring State", "The Union Law Minister"],
    1,
    "Article 222(1) provides: 'The President may, after consultation with the Chief Justice of India, transfer a Judge from one High Court to any other High Court'. In the Third Judges Case (1998), it was settled that transfer collegium consists of CJI + 4 senior-most SC judges + Chief Justices of both High Courts.",
    {"A": "CJI advises, but formal order is by President under Art. 222.", "B": "Correct. President, after consultation with the Chief Justice of India.", "C": "Governor has no power to transfer judges.", "D": "Law Minister cannot order judicial transfers."},
    "Medium", "Article 222(1)", "Recall authority and process for High Court judge transfers."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-042", "ch-12", "top-const-12-04",
    "Under Article 233(1), appointment of persons to be, and the posting and promotion of, District Judges in any State shall be made by:",
    ["The Chief Justice of the High Court alone", "The Governor of the State in consultation with the High Court exercising jurisdiction in relation to such State", "The State Public Service Commission alone", "The Chief Minister of the State"],
    1,
    "Article 233(1) states: 'Appointments of persons to be, and the posting and promotion of, district judges in any State shall be made by the Governor of the State in consultation with the High Court exercising jurisdiction in relation to such State'.",
    {"A": "Governor issues the appointment order, not Chief Justice alone.", "B": "Correct. Governor in consultation with the High Court.", "C": "SPSC does not appoint District Judges.", "D": "Chief Minister cannot make appointments without HC consultation."},
    "Medium", "Article 233(1)", "Recall appointing authority for District Judges."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-043", "ch-12", "top-const-12-04",
    "Under Article 233(2), what is the minimum practice requirement as an advocate or pleader for direct recruitment as a District Judge?",
    ["3 years", "5 years", "7 years", "10 years"],
    1,
    "Article 233(2) mandates: 'A person not already in the service of the Union or of the State shall only be eligible to be appointed a district judge if he has been for not less than SEVEN YEARS an advocate or a pleader and is recommended by the High Court for appointment'. (Reaffirmed in Dheeraj Mor v. Hon'ble High Court of Delhi, 2020).",
    {"A": "3 years is not sufficient for District Judge.", "B": "5 years is for High Court judge qualification from subordinate bench.", "C": "Correct. Not less than seven (7) years practice.", "D": "10 years is for High Court judge under Art. 217(2)(b)."},
    "Easy", "Article 233(2)", "Recall minimum standing as advocate for direct District Judge recruitment."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-044", "ch-12", "top-const-12-04",
    "Under Article 235 of the Constitution, in whom is the 'control' over subordinate courts (including posting, promotion, and grant of leave) vested?",
    ["The State Law Ministry", "The Governor of the State", "The High Court", "The State Public Service Commission"],
    2,
    "Article 235 mandates: 'The control over district courts and courts subordinate thereto including the posting and promotion of, and the grant of leave to, persons belonging to the judicial service of a State and holding any post inferior to the post of district judge shall be vested in the HIGH COURT'.",
    {"A": "Law Ministry has zero disciplinary control over judges.", "B": "Governor makes initial formal orders, but operational 'control' is vested in HC.", "C": "Correct. Vested in the High Court to maintain judicial independence.", "D": "SPSC conducts initial exams; has no control over serving officers."},
    "Medium", "Article 235 & State of West Bengal v. Nripendra Nath Bagchi (1966)", "Explain scope of High Court control over subordinate judiciary."
))

MCQS_CH12.append(create_mcq(
    "mcq-const-12-045", "ch-12", "top-const-12-04",
    "Under Article 231(1), who is empowered to establish a common High Court for two or more States, or for two or more States and a Union Territory?",
    ["The President by executive order", "The Parliament by law", "The Chief Justice of India with approval of Governors concerned", "The Inter-State Council"],
    1,
    "Article 231(1) states: 'Notwithstanding anything contained in the preceding provisions of this Chapter, Parliament may by law establish a common High Court for two or more States or for two or more States and a Union territory'. Examples: Punjab and Haryana High Court, Gauhati High Court, Bombay High Court.",
    {"A": "President cannot establish a common High Court without parliamentary statute.", "B": "Correct. Parliament by law.", "C": "CJI cannot alter High Court territorial jurisdictions.", "D": "Inter-State Council is a deliberative body under Art. 263."},
    "Easy", "Article 231(1)", "Recall authority empowered to establish common High Courts."
))

if __name__ == "__main__":
    print(f"Generated {len(MCQS_CH12)} MCQs for Chapter 12.")
