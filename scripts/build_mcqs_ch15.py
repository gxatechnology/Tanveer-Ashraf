"""
Builds 35 MCQs for Chapter 15: Federal Relations, Schedules & Constitutional Bodies.
Topics:
- top-const-15-01: 10 MCQs (Centre-State Relations: Arts 245-293, Lists, Doctrines, Repugnancy)
- top-const-15-02: 9 MCQs (The Twelve Schedules: 1st to 12th Schedules, 5th, 6th, 10th)
- top-const-15-03: 8 MCQs (Independent Bodies: ECI Art 324, FC Art 280, CAG Art 148)
- top-const-15-04: 8 MCQs (Public Services Art 311, UPSC/SPSC, Tribunals Art 323A/B)
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

MCQS_CH15 = []

# ==============================================================================
# TOPIC 15-01: CENTRE-STATE RELATIONS (10 MCQs)
# ==============================================================================

MCQS_CH15.append(create_mcq(
    "mcq-const-15-001", "ch-15", "top-const-15-01",
    "Under Article 245(2) of the Constitution, can an Act of Parliament be challenged or questioned on the ground that it would have extra-territorial operation?",
    ["Yes, Indian Parliament has strictly no power to make laws having extra-territorial effect", "No, Article 245(2) explicitly provides that no law made by Parliament shall be deemed to be invalid on the ground that it would have extra-territorial operation", "Yes, unless approved by the International Court of Justice", "Yes, with permission of the Supreme Court"],
    1,
    "Article 245(2) states unequivocally: 'No law made by Parliament shall be deemed to be invalid on the ground that it would have extra-territorial operation'. Parliament has sovereign constituent competence to enact extra-territorial legislation (e.g., GVK Inds v. ITO, 2011).",
    {"A": "Parliament possesses full extra-territorial legislative power.", "B": "Correct. Article 245(2) bars invalidation on ground of extra-territorial operation.", "C": "ICJ approval has no domestic constitutional relevance.", "D": "Supreme Court cannot strike down a law merely on extra-territorial grounds."},
    "Medium", "Article 245(2) & GVK Inds (2011)", "Recall constitutional protection of parliamentary extra-territorial legislation."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-002", "ch-15", "top-const-15-01",
    "Under the 'Doctrine of Territorial Nexus', a State Legislature may enact a law operating on persons, things, or acts outside its territorial boundaries provided:",
    ["The Governor grants special presidential dispensation", "There is a real and substantial nexus (connection) between the State enacting the law and the object/person sought to be taxed or regulated", "The State High Court issues a certificate of territorial relevance", "The neighbouring state consents in writing"],
    1,
    "Under the Doctrine of Territorial Nexus (State of Bombay v. R.M.D. Chamarbaugwala, 1957), a state law can have extra-territorial effect if: (1) the connection between the state and the subject matter is real and not illusory; and (2) the liability sought to be imposed is pertinent to that connection.",
    {"A": "Governor dispensation cannot create extra-territorial jurisdiction.", "B": "Correct. Real and substantial connection between the State and the subject-matter/activity.", "C": "High Court certificates do not create legislative nexus.", "D": "Neighbouring state consent is irrelevant."},
    "Medium", "Article 245(1) & R.M.D. Chamarbaugwala (1957)", "Master the Doctrine of Territorial Nexus."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-003", "ch-15", "top-const-15-01",
    "Which judicial doctrine is applied when a statute enacted by a legislature is challenged on the ground that it encroaches upon a subject matter assigned exclusively to another legislature under the Seventh Schedule?",
    ["Doctrine of Eclipse", "Doctrine of Pith and Substance", "Doctrine of Colourable Legislation", "Doctrine of Severability"],
    1,
    "Under the Doctrine of Pith and Substance (Prafulla Kumar Mukherjee v. Bank of Commerce, Khulna, 1947), courts examine the true nature and character ('pith and substance') of the legislation. If in substance the enactment falls within the competence of the legislature that made it, incidental encroachment onto a field reserved for another legislature does not render it ultra vires.",
    {"A": "Eclipse applies to pre-constitutional laws dormant against Part III.", "B": "Correct. Doctrine of Pith and Substance determines true legislative character.", "C": "Colourable legislation addresses fraud on legislative power.", "D": "Severability excises unconstitutional clauses."},
    "Easy", "Seventh Schedule & Pith and Substance", "Identify the doctrine resolving legislative encroachment."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-004", "ch-15", "top-const-15-01",
    "What is the core maxim underlying the 'Doctrine of Colourable Legislation' as applied by the Supreme Court in K.C. Gajapati Narayan Deo v. State of Orissa (1953)?",
    ["Audi alteram partem", "What the legislature cannot do directly, it cannot do indirectly", "Res ipsa loquitur", "Salus populi suprema lex"],
    1,
    "The Doctrine of Colourable Legislation is based on the legal maxim 'what cannot be done directly cannot also be done indirectly'. In K.C. Gajapati Narayan Deo (1953), Mukherjea J. held that the question is one of legislative competence: has the legislature transgressed the limits of its constitutional powers under the guise or pretence of acting within its own powers?",
    {"A": "Audi alteram partem is a rule of natural justice (hear the other side).", "B": "Correct. What cannot be done directly, cannot be done indirectly.", "C": "Res ipsa loquitur is a rule of tort evidence (the thing speaks for itself).", "D": "Salus populi relates to public welfare."},
    "Easy", "K.C. Gajapati Narayan Deo (1953)", "Recall the core principle of Colourable Legislation."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-005", "ch-15", "top-const-15-01",
    "Under Article 248 of the Constitution, in whom is the RESIDUARY POWER of legislation (power to make laws with respect to any matter not enumerated in the Concurrent List or State List) vested?",
    ["In the State Legislatures", "In the Parliament of India exclusively", "In the Inter-State Council", "Jointly in Parliament and State Assemblies"],
    1,
    "Article 248(1) vests residuary legislative power exclusively in Parliament: 'Subject to article 246A, Parliament has exclusive power to make any law with respect to any matter not enumerated in the Concurrent List or State List'. (Confirmed by Entry 97, List I). Unlike the US and Australia where residuary powers lie with States, India follows the Canadian model.",
    {"A": "State Legislatures have no residuary powers under the Indian Constitution.", "B": "Correct. In Parliament of India exclusively (Article 248 & Entry 97 List I).", "C": "Inter-State Council has no legislative power.", "D": "Residuary power is not joint."},
    "Easy", "Article 248 & Entry 97 List I", "Recall repository of residuary legislative powers."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-006", "ch-15", "top-const-15-01",
    "Under Article 249(1), Parliament can legislate with respect to a matter in the State List in the national interest, provided:",
    ["The Supreme Court approves it under advisory jurisdiction", "The Council of States (Rajya Sabha) has declared by resolution supported by NOT LESS THAN TWO-THIRDS OF THE MEMBERS PRESENT AND VOTING that it is necessary or expedient in the national interest", "The President proclaims an emergency under Article 352", "All State Governors issue a joint request"],
    1,
    "Article 249(1) empowers Parliament to make laws on State List matters if the Rajya Sabha (Council of States) passes a resolution supported by not less than two-thirds of the members present and voting declaring that it is necessary or expedient in the national interest that Parliament should make laws.",
    {"A": "Supreme Court approval is not required.", "B": "Correct. Rajya Sabha resolution by 2/3rds present and voting.", "C": "Emergency is under Art. 250, not Art. 249.", "D": "Governor request is under Art. 252 (requires 2 or more states)."},
    "Medium", "Article 249(1)", "Recall Rajya Sabha power to nationalise state legislative topics."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-007", "ch-15", "top-const-15-01",
    "Under Article 252(1), if the Legislatures of TWO OR MORE STATES pass resolutions requesting Parliament to enact laws on a State List matter:",
    ["Parliament can enact a law on that subject, which shall apply to such consenting States and to any other State by which it is adopted afterwards by resolution", "The State List is permanently amended", "Parliament can legislate for all 28 states automatically", "The law cannot be amended or repealed by anyone"],
    0,
    "Under Article 252(1), if two or more States pass resolutions desiring parliamentary legislation on a State List subject, Parliament can pass an Act which applies to consenting States and any other State adopting it. Crucially, under Art. 252(2), such an Act can be amended or repealed ONLY by Parliament, not by the State Legislatures.",
    {"A": "Correct. Applies to consenting and subsequently adopting States.", "B": "The Seventh Schedule State List itself is not amended.", "C": "Does not apply automatically to non-consenting states.", "D": "Can be amended or repealed by Parliament under Art. 252(2)."},
    "Medium", "Article 252", "Master delegation of legislative authority by States to Parliament."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-008", "ch-15", "top-const-15-01",
    "Under Article 253 of the Constitution, Parliament has the power to make any law for the whole or any part of the territory of India for implementing any treaty, agreement, or convention with any foreign country, notwithstanding:",
    ["Any fundamental right in Part III", "Anything in the Seventh Schedule (meaning Parliament can enact laws on State List subjects to implement international treaties without state consent)", "Any order of the Supreme Court", "The Basic Structure of the Constitution"],
    1,
    "Article 253 begins with a non-obstante clause: 'Notwithstanding anything in the foregoing provisions of this Chapter, Parliament has power to make any law... for implementing any treaty, agreement or convention'. This allows Parliament to legislate even on pure State List subjects (e.g., Environment Protection Act, TRIPS) without state consent.",
    {"A": "Parliament cannot breach Part III fundamental rights even under treaty implementation.", "B": "Correct. Overrides Seventh Schedule federal distribution of powers.", "C": "Does not override judicial review.", "D": "Treaty laws must comply with the Basic Structure."},
    "Medium", "Article 253", "Explain parliamentary power to implement international treaties on State subjects."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-009", "ch-15", "top-const-15-01",
    "Under Article 254(1), if a provision of a law made by the Legislature of a State is REPUGNANT to any provision of a law made by Parliament on a Concurrent List subject, which law prevails?",
    ["The State law prevails because states have local knowledge", "The law made by Parliament shall prevail, and the law made by the Legislature of the State shall, to the extent of the repugnancy, be VOID", "Both laws are struck down and a fresh law must be passed", "The Supreme Court decides which law is more beneficial"],
    1,
    "Article 254(1) lays down the rule of federal supremacy in the Concurrent field: if there is repugnancy between a State law and a Parliamentary law on a Concurrent List subject, the Parliamentary law (whether earlier or later) prevails, and the State law is void to the extent of repugnancy.",
    {"A": "State law does not prevail under clause (1).", "B": "Correct. Parliamentary law prevails and State law is void to the extent of repugnancy.", "C": "Both laws are not struck down.", "D": "Court does not choose policy preference; it applies Art. 254."},
    "Easy", "Article 254(1)", "Recall federal paramountcy in cases of statutory repugnancy."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-010", "ch-15", "top-const-15-01",
    "Under Article 254(2), how can a State law on a Concurrent List subject that is repugnant to an earlier Parliamentary law be saved and prevail in that State?",
    ["By being passed by a 3/4ths majority of the State Assembly", "If having been RESERVED FOR THE CONSIDERATION OF THE PRESIDENT, it has received the ASSENT of the President", "By an executive notification of the Governor", "By obtaining a clearance certificate from the Attorney-General"],
    1,
    "Under Article 254(2), a State law on a Concurrent subject repugnant to an earlier Parliamentary law will prevail IN THAT STATE if it has been reserved for the consideration of the President and has received his assent. However, the Proviso to Art. 254(2) clarifies that Parliament may at any time enact subsequent legislation adding to, amending, varying or repealing such State law.",
    {"A": "Assembly voting majority cannot bypass federal repugnancy.", "B": "Correct. Reserved for President's consideration and received Presidential assent.", "C": "Governor assent is insufficient under Art. 254(2); must be Presidential assent.", "D": "AG certificate has no constitutional status under Art. 254."},
    "Hard", "Article 254(2)", "Master the presidential assent exception to the doctrine of repugnancy."
))

# ==============================================================================
# TOPIC 15-02: THE TWELVE SCHEDULES (9 MCQs)
# ==============================================================================

MCQS_CH15.append(create_mcq(
    "mcq-const-15-011", "ch-15", "top-const-15-02",
    "Which Schedule of the Constitution of India deals with the allocation of seats in the Council of States (Rajya Sabha) to the States and Union Territories?",
    ["Second Schedule", "Third Schedule", "Fourth Schedule", "Fifth Schedule"],
    2,
    "The Fourth Schedule deals with the allocation of seats in the Council of States (Rajya Sabha) to each State and Union Territory (Articles 4(1) and 80(2)). Uttar Pradesh has the largest representation with 31 seats.",
    {"A": "Second Schedule contains provisions as to salaries, allowances and emoluments.", "B": "Third Schedule contains Forms of Oaths or Affirmations.", "C": "Correct. Fourth Schedule allocates Rajya Sabha seats.", "D": "Fifth Schedule relates to administration of Scheduled Areas."},
    "Easy", "Fourth Schedule", "Identify schedule allocating Rajya Sabha seats."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-012", "ch-15", "top-const-15-02",
    "Which constitutional functionary does NOT take oath according to the Forms prescribed in the THIRD SCHEDULE of the Constitution?",
    ["Judges of the Supreme Court and High Courts", "Union Ministers and Members of Parliament", "The President of India", "Comptroller and Auditor-General of India"],
    2,
    "The President of India does NOT take oath under the Third Schedule. The oath of the President is specifically prescribed in ARTICLE 60 itself. Similarly, the Vice-President's oath is in Article 69 and Governor's oath is in Article 159. The Third Schedule contains oaths for Ministers, MPs, Judges, and CAG.",
    {"A": "SC/HC Judges take oath under Forms IV and VIII of Third Schedule.", "B": "Ministers and MPs take oath under Forms I, II, III of Third Schedule.", "C": "Correct. President takes oath under Article 60, NOT Third Schedule.", "D": "CAG takes oath under Form IV of Third Schedule."},
    "Medium", "Third Schedule & Article 60 Contrast", "Identify functionaries taking oath outside the Third Schedule."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-013", "ch-15", "top-const-15-02",
    "Which four North-Eastern States are covered under the SIXTH SCHEDULE of the Constitution for the administration of tribal areas through Autonomous District Councils?",
    ["Nagaland, Manipur, Mizoram, and Arunachal Pradesh", "Assam, Meghalaya, Tripura, and Mizoram (AMTM)", "Sikkim, Assam, Nagaland, and Tripura", "Meghalaya, Manipur, Tripura, and Nagaland"],
    1,
    "The Sixth Schedule (Articles 244(2) and 275(1)) applies specifically to the tribal areas in the four North-Eastern States of ASSAM, MEGHALAYA, TRIPURA, and MIZORAM (mnemonic: AMTM). Tribal areas in other states are governed by the Fifth Schedule.",
    {"A": "Nagaland (Art. 371A), Manipur (Art. 371C), and Arunachal (Art. 371H) are under special Part XXI provisions, not 6th Schedule.", "B": "Correct. Assam, Meghalaya, Tripura, and Mizoram (AMTM).", "C": "Sikkim is under Art. 371F.", "D": "Manipur is not a Sixth Schedule state."},
    "Easy", "Sixth Schedule (AMTM)", "Recall four Sixth Schedule states."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-014", "ch-15", "top-const-15-02",
    "Under the Fifth Schedule, what is the statutory council that must be established in each State having Scheduled Areas to advise on the welfare and advancement of Scheduled Tribes?",
    ["Autonomous Territorial Council", "Tribes Advisory Council (TAC)", "Scheduled Area Development Authority", "National Commission for Scheduled Tribes"],
    1,
    "Paragraph 4 of the Fifth Schedule mandates the establishment in each State having Scheduled Areas of a 'Tribes Advisory Council' (TAC) consisting of not more than twenty members, of whom three-fourths shall be representatives of Scheduled Tribes in the Legislative Assembly of the State.",
    {"A": "Autonomous District/Territorial Councils are under the Sixth Schedule.", "B": "Correct. Tribes Advisory Council (TAC) under Fifth Schedule.", "C": "Development Authority is an executive body.", "D": "NCST is a constitutional body under Art. 338A."},
    "Medium", "Fifth Schedule Paragraph 4", "Identify statutory advisory body under Fifth Schedule."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-015", "ch-15", "top-const-15-02",
    "How many languages are currently recognized in the EIGHTH SCHEDULE of the Constitution of India?",
    ["14 languages", "18 languages", "22 languages", "24 languages"],
    2,
    "Originally, the Eighth Schedule contained 14 languages. Sindhi was added by the 21st Amendment Act, 1967. Konkani, Manipuri, and Nepali were added by the 71st Amendment Act, 1992. Bodo, Dogri, Maithili, and Santhali were added by the 92nd Amendment Act, 2003, bringing the total to exactly 22 LANGUAGES.",
    {"A": "14 was the original number at commencement.", "B": "18 was the number after the 71st Amendment (1992).", "C": "Correct. Exactly 22 languages.", "D": "24 languages is Sahitya Akademi recognition, not constitutional 8th Schedule."},
    "Easy", "Eighth Schedule", "Recall total recognized languages in the Eighth Schedule."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-016", "ch-15", "top-const-15-02",
    "Which Constitutional Amendment Act added the NINTH SCHEDULE to the Constitution of India along with Article 31B to protect land reform laws?",
    ["First Constitutional Amendment Act, 1951", "Seventh Constitutional Amendment Act, 1956", "Twenty-Fourth Constitutional Amendment Act, 1971", "Forty-Fourth Constitutional Amendment Act, 1978"],
    0,
    "The Ninth Schedule was added by the First Constitutional Amendment Act, 1951, enacted by the provisional Parliament, along with Article 31B, to insulate land reform and zamindari abolition enactments from judicial review on fundamental rights grounds.",
    {"A": "Correct. First Constitutional Amendment Act, 1951.", "B": "7th Amendment reorganized states on linguistic basis.", "C": "24th Amendment amended Art. 13 and 368.", "D": "44th Amendment omitted right to property from Part III."},
    "Easy", "Ninth Schedule & First Amendment 1951", "Identify enactment introducing the Ninth Schedule."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-017", "ch-15", "top-const-15-02",
    "Which Constitutional Amendment Act inserted the TENTH SCHEDULE (Anti-Defection Law) into the Constitution?",
    ["42nd Amendment Act, 1976", "44th Amendment Act, 1978", "52nd Constitutional Amendment Act, 1985", "91st Amendment Act, 2003"],
    2,
    "The 52nd Constitutional Amendment Act, 1985 added the Tenth Schedule, introducing grounds of disqualification for defection by Members of Parliament and State Legislatures (popularly called the Anti-Defection Law).",
    {"A": "42nd Amendment is mini-constitution.", "B": "44th Amendment restored democratic safeguards.", "C": "Correct. 52nd Constitutional Amendment Act, 1985.", "D": "91st Amendment amended Tenth Schedule to delete the 1/3rd split defense."},
    "Easy", "Tenth Schedule & 52nd Amendment", "Identify amendment introducing Anti-Defection Law."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-018", "ch-15", "top-const-15-02",
    "Which Constitutional Amendment Act deleted Paragraph 3 of the Tenth Schedule, thereby abolishing the defense of a 'one-third split' in a political party against defection?",
    ["61st Amendment Act, 1988", "86th Amendment Act, 2002", "91st Constitutional Amendment Act, 2003", "99th Amendment Act, 2014"],
    2,
    "The 91st Constitutional Amendment Act, 2003 omitted Paragraph 3 of the Tenth Schedule. Previously, a split of at least one-third of the legislature party was protected from disqualification. Following the 91st Amendment, splits are no longer recognized as a defense; only a merger under Paragraph 4 (agreed by at least 2/3rds members) protects against defection.",
    {"A": "61st Amendment lowered voting age to 18.", "B": "86th Amendment inserted Right to Education.", "C": "Correct. 91st Amendment Act, 2003 omitted paragraph 3 (1/3rd split defense).", "D": "99th Amendment created NJAC."},
    "Medium", "Tenth Schedule Para 3 & 91st Amendment", "Recall abolition of the split defense in Anti-Defection law."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-019", "ch-15", "top-const-15-02",
    "In Kihoto Hollohan v. Zachillhu (1992), what was held by the Supreme Court regarding Paragraph 7 of the Tenth Schedule which barred judicial review over the Speaker's disqualification decisions?",
    ["The entire Tenth Schedule is unconstitutional", "Paragraph 7 was unconstitutional for lack of ratification by State Legislatures under Article 368(2) proviso, and the Speaker/Chairman acts as a TRIBUNAL whose decision is subject to judicial review under Articles 136, 226, and 227", "The Speaker's decision is completely final and courts can never interfere", "The Governor must decide all defection cases"],
    1,
    "In Kihoto Hollohan (1992), the Constitution Bench held: (1) Paragraph 7 (excluding judicial review) was unconstitutional because it curtailed HC/SC powers without requisite 50% state ratification; (2) Severing Paragraph 7, the rest of Tenth Schedule was valid; (3) The Speaker/Chairman deciding defection questions acts as a statutory 'tribunal', and their orders are subject to judicial review on grounds of mala fides, perversity, or violation of natural justice.",
    {"A": "The rest of Tenth Schedule was upheld as valid.", "B": "Correct. Paragraph 7 invalid for lack of state ratification; Speaker acts as reviewable tribunal.", "C": "Absolute immunity was struck down.", "D": "Governor decides ordinary disqualifications under Art. 192, not defection under 10th Schedule."},
    "Hard", "Kihoto Hollohan v. Zachillhu (1992)", "Master the landmark ruling on the Tenth Schedule."
))

# ==============================================================================
# TOPIC 15-03: INDEPENDENT CONSTITUTIONAL BODIES (8 MCQs)
# ==============================================================================

MCQS_CH15.append(create_mcq(
    "mcq-const-15-020", "ch-15", "top-const-15-03",
    "Under Article 324(1) of the Constitution, the superintendence, direction and control of the preparation of electoral rolls and conduct of elections is vested in the Election Commission for elections to:",
    ["Parliament, State Legislatures, and the offices of President and Vice-President", "Parliament and State Legislatures only", "Panchayats and Municipalities only", "All local, state, and central elections"],
    0,
    "Article 324(1) specifies that the Election Commission of India conducts elections to: (1) Parliament; (2) State Legislatures; (3) the office of the President; and (4) the office of the Vice-President. Elections to Panchayats and Municipalities are conducted by the STATE ELECTION COMMISSION under Articles 243K and 243ZA.",
    {"A": "Correct. Parliament, State Legislatures, President, and Vice-President.", "B": "Excludes President and Vice-President, which is incomplete.", "C": "Panchayats/Municipalities fall under State Election Commissions, not ECI.", "D": "ECI does not conduct local body polls."},
    "Easy", "Article 324(1)", "Recall jurisdictional scope of the Election Commission of India."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-021", "ch-15", "top-const-15-03",
    "Under Article 324(5) proviso, on what ground and manner can the Chief Election Commissioner (CEC) be removed from office?",
    ["By an executive order of the Prime Minister", "In like manner and on the like grounds as a Judge of the Supreme Court (by presidential address following special majority in both Houses of Parliament on proved misbehaviour or incapacity)", "By a resolution passed by a simple majority in Lok Sabha", "Upon completion of 5 years or age of 60"],
    1,
    "The Proviso to Article 324(5) guarantees constitutional tenure: 'the Chief Election Commissioner shall not be removed from his office except in like manner and on the like grounds as a Judge of the Supreme Court and the conditions of service of the Chief Election Commissioner shall not be varied to his disadvantage after his appointment'.",
    {"A": "PM cannot remove the CEC by executive fiat.", "B": "Correct. Removed in like manner and grounds as a Supreme Court Judge.", "C": "Simple majority resolution is inadequate.", "D": "Age/tenure expiration is retirement, not removal."},
    "Medium", "Article 324(5) Proviso", "Recall constitutional security of tenure for the CEC."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-022", "ch-15", "top-const-15-03",
    "In T.N. Seshan v. Union of India (1995), what was held by the Supreme Court regarding the status of Election Commissioners relative to the Chief Election Commissioner?",
    ["The Chief Election Commissioner is superior to other Election Commissioners and can overrule them", "The Chief Election Commissioner and other Election Commissioners are EQUAL in power and decision-making; all decisions must be taken unanimously or by majority vote", "Election Commissioners have advisory status only", "Only the CEC has voting power"],
    1,
    "In T.N. Seshan (1995), a unanimous 5-judge bench held that the Chief Election Commissioner is merely 'primus inter pares' (first among equals) and does not enjoy superior status or veto over the Election Commissioners. Section 10 of the CEC Act mandates that decisions are taken unanimously, or in case of difference of opinion, by majority.",
    {"A": "Superiority and veto were definitively rejected.", "B": "Correct. CEC and ECs are equal; decisions by unanimity or majority vote.", "C": "Election Commissioners have substantive voting powers.", "D": "All Commissioners have equal votes."},
    "Hard", "T.N. Seshan v. UOI (1995)", "Explain institutional equality within the multi-member Election Commission."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-023", "ch-15", "top-const-15-03",
    "In Anoop Baranwal v. Union of India (2023), what interim selection panel for appointing the Chief Election Commissioner and Election Commissioners was directed by the Constitution Bench?",
    ["Chief Justice of India, Prime Minister, and Leader of Opposition in Lok Sabha", "Union Cabinet alone", "Speaker of Lok Sabha, Vice-President, and CJI", "All Chief Justices of High Courts"],
    0,
    "In Anoop Baranwal (2023), a 5-judge bench led by Justice K.M. Joseph directed that until Parliament made a law under Art. 324(2), the CEC and ECs shall be appointed on the recommendation of a Committee consisting of the Prime Minister, Leader of Opposition in Lok Sabha, and the Chief Justice of India.",
    {"A": "Correct. Prime Minister, Leader of Opposition, and Chief Justice of India.", "B": "Executive monopoly was held to erode election integrity.", "C": "Speaker and Vice-President panel was not ordered.", "D": "High Court judges were not included."},
    "Medium", "Anoop Baranwal v. UOI (2023)", "Recall landmark selection panel judgment for election commissioners."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-024", "ch-15", "top-const-15-03",
    "Under Article 280(1), who constitutes the Finance Commission, and at what interval?",
    ["The Parliament of India every 10 years", "The President of India, at the expiration of every FIFTH YEAR or at such earlier time as the President considers necessary", "The Union Finance Minister every year", "The NITI Aayog every 3 years"],
    1,
    "Article 280(1) mandates: 'The President shall, within two years from the commencement of this Constitution and thereafter at the expiration of every fifth year or at such earlier time as the President considers necessary, by order constitute a Finance Commission'.",
    {"A": "10 years is census interval, not Finance Commission.", "B": "Correct. President constitutes every 5th year or earlier as needed.", "C": "Finance Minister does not constitute the constitutional Commission.", "D": "NITI Aayog is a non-statutory executive think tank."},
    "Easy", "Article 280(1)", "Recall appointing authority and periodicity of Finance Commission."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-025", "ch-15", "top-const-15-03",
    "Under Article 280(3), what is the primary constitutional duty of the Finance Commission?",
    ["To prepare the Union Annual Financial Statement (Budget)", "To make recommendations to the President regarding the distribution between the Union and the States of the net proceeds of taxes, and the principles governing grants-in-aid to States out of the Consolidated Fund of India", "To audit government bank accounts", "To fix income tax rates annually"],
    1,
    "Article 280(3) outlines the core functions: (a) distribution between Union and States of the net proceeds of taxes (vertical devolution) and allocation between States (horizontal devolution); (b) principles governing grants-in-aid under Art. 275; (c) measures to augment Consolidated Fund of a State to supplement Panchayat and Municipal resources.",
    {"A": "Budget preparation belongs to Ministry of Finance (Art. 112).", "B": "Correct. Tax proceeds distribution and grants-in-aid principles under Art. 280(3).", "C": "Auditing belongs to CAG under Art. 148–151.", "D": "Tax rates are fixed by Parliament via Finance Acts."},
    "Medium", "Article 280(3)", "Define constitutional duties of the Finance Commission."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-026", "ch-15", "top-const-15-03",
    "Under Article 148(1) of the Constitution, the Comptroller and Auditor-General (CAG) of India is appointed by the President and can be removed from office ONLY:",
    ["By an order of the Union Finance Minister", "In like manner and on the like grounds as a Judge of the Supreme Court", "By a simple majority vote of the Rajya Sabha", "Upon the change of the ruling party at the Centre"],
    1,
    "Article 148(1) gives the CAG identical tenure protection to Supreme Court judges: 'he shall only be removed from office in like manner and on the like grounds as a Judge of the Supreme Court'. Dr. B.R. Ambedkar called the CAG 'the most important officer under the Constitution of India'.",
    {"A": "Finance Minister has no removal power over CAG.", "B": "Correct. Removed only in like manner and grounds as a Judge of the Supreme Court.", "C": "Simple majority cannot remove the CAG.", "D": "Tenure is independent of political changes."},
    "Easy", "Article 148(1)", "Recall removal standard and tenure security for the CAG."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-027", "ch-15", "top-const-15-04",
    "Under Article 148(4), what post-retirement disability is imposed on a person who has held office as Comptroller and Auditor-General of India?",
    ["Shall not contest parliamentary elections", "Shall not be eligible for further office either under the Government of India or under the Government of any State", "Shall not practice as a chartered accountant", "Shall not hold any property in Delhi"],
    1,
    "Article 148(4) provides a strict conflict-of-interest bar: 'The Comptroller and Auditor-General shall not be eligible for further office either under the Government of India or under the Government of any State after he has ceased to hold his office'.",
    {"A": "Election contest is not barred under Art. 148(4).", "B": "Correct. Ineligible for further office under Central or State Government.", "C": "Private CA practice is not the constitutional text.", "D": "Property holding is not restricted."},
    "Medium", "Article 148(4)", "Recall post-retirement disability of the CAG."
))

# ==============================================================================
# TOPIC 15-04: PUBLIC SERVICES & TRIBUNALS (8 MCQs)
# ==============================================================================

MCQS_CH15.append(create_mcq(
    "mcq-const-15-028", "ch-15", "top-const-15-04",
    "Under Article 310(1) of the Constitution, public servants hold office during the 'Pleasure of the President' or 'Pleasure of the Governor'. Which constitutional article acts as the primary SUBSTANTIVE SAFEGUARD limiting this Doctrine of Pleasure?",
    ["Article 308", "Article 309", "Article 311", "Article 312"],
    2,
    "Article 311 acts as a powerful constitutional fetter and limitation upon the Doctrine of Pleasure embodied in Article 310. It guarantees that no civil servant shall be dismissed/removed by an authority subordinate to the appointing authority, and provides a mandatory reasonable opportunity of being heard.",
    {"A": "Article 308 defines 'State' for Part XIV.", "B": "Article 309 provides for recruitment rules.", "C": "Correct. Article 311 provides constitutional safeguards to civil servants.", "D": "Article 312 relates to All-India Services."},
    "Easy", "Article 310 & 311 Interplay", "Identify the constitutional shield limiting the Doctrine of Pleasure."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-029", "ch-15", "top-const-15-04",
    "Under Article 311(1), which of the following is an absolute constitutional protection guaranteed to civil servants?",
    ["Shall not be transferred to another district", "Shall not be dismissed or removed by an authority SUBORDINATE to that by which he was appointed", "Shall not be suspended pending inquiry", "Shall receive guaranteed promotion every five years"],
    1,
    "Article 311(1) guarantees: 'No person who is a member of a civil service of the Union or an all-India service or a civil service of a State... shall be dismissed or removed by an authority SUBORDINATE to that by which he was appointed'.",
    {"A": "Transfers are an ordinary condition of service.", "B": "Correct. Cannot be dismissed or removed by an authority subordinate to appointing authority.", "C": "Suspension is not dismissal or removal.", "D": "Promotions depend on merit and seniority rules."},
    "Medium", "Article 311(1)", "Recall first major constitutional protection under Article 311."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-030", "ch-15", "top-const-15-04",
    "Which of the following is NOT one of the three exceptions under the Second Proviso to Article 311(2) where a departmental inquiry may be dispensed with before dismissing a civil servant?",
    ["Where a person is dismissed or removed or reduced in rank on the ground of conduct which has led to his conviction on a criminal charge", "Where the authority empowered to dismiss is satisfied that for reasons recorded in writing, it is not reasonably practicable to hold such inquiry", "Where the President or Governor is satisfied that in the interest of the SECURITY OF THE STATE, it is not expedient to hold such inquiry", "Where the civil servant has completed twenty years of government service"],
    3,
    "The three express exceptions in the Second Proviso to Article 311(2) are: (a) conviction on a criminal charge; (b) where authority records in writing that inquiry is not reasonably practicable; and (c) security of the State in the opinion of President/Governor. Completion of 20 years service is NOT an exception to inquiry.",
    {"A": "Criminal conviction is clause (a) exception.", "B": "Not reasonably practicable is clause (b) exception.", "C": "Security of the State is clause (c) exception.", "D": "Correct. 20 years of service is NOT a constitutional ground to dispense with inquiry."},
    "Hard", "Article 311(2) Second Proviso", "Identify exceptions dispensing with disciplinary inquiries under Art. 311."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-031", "ch-15", "top-const-15-04",
    "Under Article 312(1), how can Parliament create a new All-India Service (such as an Indian Judicial Service)?",
    ["By an executive circular of the Prime Minister", "If the Council of States (Rajya Sabha) has declared by resolution supported by NOT LESS THAN TWO-THIRDS OF THE MEMBERS PRESENT AND VOTING that it is necessary or expedient in the national interest to do so", "By an order of the Chief Justice of India", "With the consent of all State Governors"],
    1,
    "Article 312(1) prescribes: 'if the Council of States has declared by resolution supported by not less than two-thirds of the members present and voting that it is necessary or expedient in the national interest so to do, Parliament may by law provide for the creation of one or more all-India services (including an all-India judicial service)'.",
    {"A": "Executive circular cannot create an All-India Service.", "B": "Correct. Rajya Sabha resolution supported by 2/3rds present and voting.", "C": "CJI cannot create services under Art. 312.", "D": "Governor consent is not the constitutional mechanism."},
    "Medium", "Article 312(1)", "Recall procedure for creating new All-India Services."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-032", "ch-15", "top-const-15-04",
    "Under Article 312(3), what rank of judicial post must an All-India Judicial Service (AIJS) NOT include?",
    ["Any post of District Judge", "Any post INFERIOR to that of a District Judge", "Any post of High Court Judge", "Any post of Sessions Judge"],
    1,
    "Article 312(3) explicitly provides: 'The all-India judicial service referred to in clause (1) shall not include any post inferior to that of a district judge as defined in article 236'. Thus, AIJS can only recruit at or above the District Judge level.",
    {"A": "District Judge posts are the target level of AIJS.", "B": "Correct. Shall not include any post inferior to that of a District Judge.", "C": "High Court judges are constitutional appointments under Art. 217, not AIJS.", "D": "Sessions Judge is equivalent to District Judge."},
    "Hard", "Article 312(3)", "Recall statutory rank restriction on All-India Judicial Service."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-033", "ch-15", "top-const-15-04",
    "Under Article 316(2), what is the term of office and retirement age for members of the Union Public Service Commission (UPSC) vs State Public Service Commissions (SPSC)?",
    ["Both retire at age 60 after a 5-year term", "UPSC members hold office for 6 years or until age 65; SPSC members hold office for 6 years or until age 62", "UPSC members retire at 70; SPSC members at 65", "Both hold office during the pleasure of the President with no fixed age"],
    1,
    "Under Article 316(2), a member of UPSC holds office for a term of SIX YEARS or until he attains the age of SIXTY-FIVE (65) YEARS. A member of SPSC holds office for a term of SIX YEARS or until he attains the age of SIXTY-TWO (62) YEARS (raised from 60 to 62 by 41st Amendment Act 1976).",
    {"A": "5-year term and age 60 are incorrect.", "B": "Correct. UPSC: 6 years or age 65; SPSC: 6 years or age 62.", "C": "Age 70 does not exist for PSC members.", "D": "PSC members have fixed constitutional tenure, not pleasure doctrine."},
    "Medium", "Article 316(2) & 41st Amendment", "Distinguish retirement ages of UPSC vs SPSC members."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-034", "ch-15", "top-const-15-04",
    "Which Constitutional Amendment Act inserted Part XIV-A (Articles 323A and 323B) providing for Administrative Tribunals into the Constitution?",
    ["42nd Constitutional Amendment Act, 1976", "44th Constitutional Amendment Act, 1978", "73rd Constitutional Amendment Act, 1992", "97th Constitutional Amendment Act, 2011"],
    0,
    "The 42nd Constitutional Amendment Act, 1976 inserted Part XIV-A containing Article 323A (Administrative Tribunals for public service matters) and Article 323B (Tribunals for other matters such as taxation, foreign exchange, labor, land reforms).",
    {"A": "Correct. 42nd Constitutional Amendment Act, 1976.", "B": "44th Amendment repealed other parts, but retained Part XIV-A.", "C": "73rd Amendment introduced Part IX (Panchayats).", "D": "97th Amendment introduced Part IX-B (Co-operatives)."},
    "Easy", "Part XIV-A & 42nd Amendment", "Identify amendment introducing Administrative Tribunals."
))

MCQS_CH15.append(create_mcq(
    "mcq-const-15-035", "ch-15", "top-const-15-04",
    "In the landmark seven-judge Constitution Bench judgment in L. Chandra Kumar v. Union of India (1997), what did the Supreme Court rule regarding the exclusion of High Court judicial review under Article 323A(2)(d) and Article 323B(3)(d)?",
    ["The exclusion of High Court and Supreme Court jurisdiction was valid and total", "The power of judicial review of the High Courts under Articles 226/227 and the Supreme Court under Article 32 is an inviolable BASIC FEATURE of the Constitution; statutory clauses excluding judicial review are unconstitutional, and all decisions of Tribunals are subject to scrutiny before a Division Bench of the High Court", "Administrative tribunals are abolished permanently", "Tribunals can only be presided over by serving Supreme Court judges"],
    1,
    "In L. Chandra Kumar (1997), the 7-judge bench unanimously held that judicial review under Articles 226/227 and Article 32 is part of the Basic Structure. Therefore, provisions excluding judicial review of High Courts in Articles 323A(2)(d) and 323B(3)(d) were struck down as unconstitutional. Tribunals act as courts of first instance, but their decisions are appealable before a Division Bench of the High Court under Article 226/227.",
    {"A": "Exclusion of constitutional courts was struck down.", "B": "Correct. Judicial review is basic structure; tribunal decisions are subject to High Court division bench review.", "C": "Tribunals were retained as supplementary forums.", "D": "Tribunal benches include judicial and administrative members."},
    "Hard", "Article 323A, 323B & L. Chandra Kumar (1997)", "Master landmark ruling on judicial review over Administrative Tribunals."
))

if __name__ == "__main__":
    print(f"Generated {len(MCQS_CH15)} MCQs for Chapter 15.")
