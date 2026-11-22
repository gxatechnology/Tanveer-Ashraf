"""
Builds 30 MCQs for Chapter 14: Amendment of the Constitution & Basic Structure.
Topics:
- top-const-14-01: 15 MCQs (Article 368, Types of Amendments, Procedures)
- top-const-14-02: 15 MCQs (Shankari Prasad to Kesavananda, Minerva Mills, NJAC)
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

MCQS_CH14 = []

# ==============================================================================
# TOPIC 14-01: AMENDMENT PROCEDURE UNDER ART. 368 (15 MCQs)
# ==============================================================================

MCQS_CH14.append(create_mcq(
    "mcq-const-14-001", "ch-14", "top-const-14-01",
    "In which Part of the Constitution of India is the provision for the amendment of the Constitution contained?",
    ["Part XVIII", "Part XIX", "Part XX", "Part XXI"],
    2,
    "Article 368 is contained alone in Part XX of the Constitution, titled 'Amendment of the Constitution'. (Part XVIII is Emergency; Part XIX is Miscellaneous; Part XXI is Temporary, Transitional and Special Provisions).",
    {"A": "Part XVIII covers Emergency Provisions (Arts. 352–360).", "B": "Part XIX covers Miscellaneous provisions.", "C": "Correct. Part XX contains Article 368.", "D": "Part XXI contains temporary and special provisions."},
    "Easy", "Part XX & Article 368", "Recall the constitutional Part containing Article 368."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-002", "ch-14", "top-const-14-01",
    "Under Article 368(2), in which House of Parliament can a bill for the amendment of the Constitution be initiated?",
    ["In the Lok Sabha only", "In the Rajya Sabha only", "In EITHER HOUSE of Parliament", "In a State Legislative Assembly with Governor's approval"],
    2,
    "Article 368(2) explicitly provides: 'An amendment of this Constitution may be initiated ONLY by the introduction of a Bill for the purpose in EITHER HOUSE of Parliament'. State Legislatures have zero power to initiate constitutional amendment bills.",
    {"A": "Money bills are initiated only in Lok Sabha (Art. 109), but Amendment bills can start in either House.", "B": "Rajya Sabha does not hold an initiation monopoly.", "C": "Correct. In either House of Parliament.", "D": "State Assemblies cannot initiate constitutional amendment bills."},
    "Easy", "Article 368(2)", "Recall initiation chamber for constitutional amendment bills."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-003", "ch-14", "top-const-14-01",
    "Does a Constitutional Amendment Bill require the prior recommendation or sanction of the President of India before its introduction in Parliament?",
    ["Yes, all amendment bills require prior Presidential recommendation under Article 117", "No, prior recommendation of the President is NOT required for introducing a Constitutional Amendment Bill under Article 368", "Yes, if it alters state borders under Article 3", "Yes, if it affects fundamental rights"],
    1,
    "Unlike Money Bills (Art. 117) or bills altering state boundaries (Art. 3), a Constitutional Amendment Bill under Article 368 does NOT require the prior recommendation of the President before being introduced in either House.",
    {"A": "Article 117 applies to financial bills, not constitutional amendments.", "B": "Correct. Prior recommendation of President is not required under Article 368.", "C": "Article 3 ordinary bills require recommendation, but Art. 368 does not.", "D": "Fundamental rights amendments require no prior sanction."},
    "Medium", "Article 368(2)", "Recognize absence of prior presidential sanction requirement."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-004", "ch-14", "top-const-14-01",
    "Can a private member (an MP who is not a Minister) introduce a Constitutional Amendment Bill in Parliament?",
    ["No, only Ministers can introduce constitutional amendments", "Yes, a private member can introduce a Constitutional Amendment Bill in either House", "Yes, but only in the Rajya Sabha", "No, unless supported by 100 MPs in advance"],
    1,
    "Under parliamentary rules and Article 368, a Constitutional Amendment Bill can be introduced either by a Minister (Government Bill) or by a private member (Private Member's Bill).",
    {"A": "Incorrect; private members have full constitutional right to introduce amendment bills.", "B": "Correct. A private member can introduce a Constitutional Amendment Bill.", "C": "Can be introduced in either House.", "D": "Advance support of 100 MPs is not required for introduction."},
    "Medium", "Article 368 & Rules of Procedure", "Recall private member eligibility to introduce amendment bills."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-005", "ch-14", "top-const-14-01",
    "What specific majority is required in EACH HOUSE of Parliament to pass a Constitutional Amendment Bill under Article 368(2)?",
    ["Simple majority of members present and voting", "A majority of the TOTAL MEMBERSHIP of that House AND by a majority of not less than TWO-THIRDS of the members of that House present and voting", "Three-fourths of the total membership", "Two-thirds of total membership of Lok Sabha alone"],
    1,
    "Article 368(2) prescribes: 'passed in each House by a majority of the total membership of that House and by a majority of not less than two-thirds of the members of that House present and voting'.",
    {"A": "Simple majority does not satisfy Article 368.", "B": "Correct. Majority of total membership + 2/3rds present and voting in each House.", "C": "Three-fourths is incorrect.", "D": "Both Houses must pass it independently with the requisite majority."},
    "Medium", "Article 368(2)", "Recall the exact dual-test special majority under Article 368."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-006", "ch-14", "top-const-14-01",
    "Is there any provision for convening a JOINT SITTING of both Houses of Parliament under Article 108 in case of a deadlock over a Constitutional Amendment Bill?",
    ["Yes, the President can summon a joint sitting under Article 108", "No, each House must pass the Constitutional Amendment Bill separately; there is NO PROVISION for a joint sitting under Article 368", "Yes, if the deadlock continues for more than 6 months", "Yes, if recommended by the Chief Justice of India"],
    1,
    "There is NO provision for a joint sitting of both Houses to resolve a deadlock on a Constitutional Amendment Bill. Each House must pass the bill independently with the prescribed special majority. If either House rejects the bill, the bill lapses (e.g., 24th Amendment Bill 1970 fell in Rajya Sabha).",
    {"A": "Joint sittings under Art. 108 apply only to ordinary and financial bills, never to Art. 368.", "B": "Correct. No joint sitting is permissible; each House must pass separately.", "C": "Six-month deadlock rule in Art. 108 does not apply to Art. 368.", "D": "CJI cannot intervene in legislative procedure."},
    "Medium", "Article 368 & 108 Contrast", "Identify absence of joint sitting mechanism for constitutional amendments."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-007", "ch-14", "top-const-14-01",
    "Under the 24th Constitutional Amendment Act, 1971, what is the duty of the President when a Constitutional Amendment Bill passed by Parliament is presented for assent under Article 368(2)?",
    ["The President can exercise absolute veto", "The President can withhold assent or return the bill for reconsideration", "The President SHALL GIVE HIS ASSENT thereto (assent is mandatory; no veto power exists)", "The President must refer the bill to the Supreme Court under Article 143"],
    2,
    "The 24th Amendment Act, 1971 amended Article 368(2) by substituting the words 'it shall be presented to the President who shall give his assent thereto'. The President CANNOT withhold assent, CANNOT return the bill for reconsideration, and has NO pocket veto over a constitutional amendment.",
    {"A": "Absolute veto does not apply to Art. 368.", "B": "Suspensive veto under Art. 111 does not apply to Art. 368.", "C": "Correct. The President shall give his assent (assent is constitutionally mandatory).", "D": "Reference to SC is not mandatory."},
    "Medium", "Article 368(2) & 24th Amendment", "Master mandatory nature of Presidential assent to constitutional amendments."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-008", "ch-14", "top-const-14-01",
    "Which of the following constitutional provisions requires RATIFICATION BY THE LEGISLATURES OF NOT LESS THAN ONE-HALF OF THE STATES under the Proviso to Article 368(2)?",
    ["Abolition or creation of Legislative Councils under Article 169", "The election of the President (Articles 54 & 55), the representation of States in Parliament, and the Seventh Schedule Lists", "Citizenship provisions under Articles 5 to 11", "Official language provisions under Part XVII"],
    1,
    "Under the Proviso to Article 368(2), federal provisions require ratification by resolutions passed by not less than one-half of State Legislatures: (a) Arts. 54 & 55 (President election); (b) Arts. 73 & 162 (executive powers); (c) Arts. 124–147 & 214–231 (Judiciary); (d) Seventh Schedule Lists; (e) representation of States in Parliament; and (f) Article 368 itself.",
    {"A": "Article 169 requires ordinary parliamentary law, not Art. 368 ratification.", "B": "Correct. Arts 54/55, representation in Parliament, Seventh Schedule require state ratification.", "C": "Citizenship can be amended by ordinary law under Art. 11.", "D": "Official language does not fall under Art. 368(2) proviso."},
    "Hard", "Article 368(2) Proviso", "Identify federal provisions requiring 50% State ratification."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-009", "ch-14", "top-const-14-01",
    "What majority is required in the State Legislatures to ratify a Constitutional Amendment Bill under the Proviso to Article 368(2)?",
    ["Two-thirds of members present and voting in each State Assembly", "A resolution passed by a SIMPLE MAJORITY of members present and voting in the State Legislature", "Total membership majority in both Houses of the State Legislature", "Unanimous resolution of the State Assembly"],
    1,
    "Under the Proviso to Article 368(2), ratification by State Legislatures requires merely a resolution passed by a SIMPLE MAJORITY of the members present and voting in each ratifying State Legislature.",
    {"A": "Two-thirds majority is not required at the state level.", "B": "Correct. Simple majority of members present and voting in the State Legislature.", "C": "Total membership majority is not required in states.", "D": "Unanimity is not required."},
    "Medium", "Article 368(2) Proviso State Majority", "Recall voting majority required for State ratification."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-010", "ch-14", "top-const-14-01",
    "Is there any time limit prescribed in the Constitution within which the States must ratify an amendment bill referred to them under Article 368(2) proviso?",
    ["Within six months", "Within one year", "The Constitution prescribes NO TIME LIMIT within which States must ratify", "Before the next general election"],
    2,
    "The Constitution of India prescribes NO TIME LIMIT within which State Legislatures must pass resolutions of ratification. Once the required number (not less than half) of States ratify, the bill is presented to the President.",
    {"A": "Six months is not prescribed.", "B": "One year is not prescribed.", "C": "Correct. No time limit is prescribed in the Constitution.", "D": "General election does not cause lapse of state ratification process."},
    "Medium", "Article 368(2) Proviso Timing", "Recognize absence of state ratification deadline."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-011", "ch-14", "top-const-14-01",
    "Which of the following constitutional changes can be effected by Parliament by SIMPLE MAJORITY and is NOT deemed to be an amendment under Article 368?",
    ["Formation of new States and alteration of areas/boundaries under Article 3", "Change in the election procedure of the President under Article 55", "Amendment of the Supreme Court's jurisdiction under Chapter IV Part V", "Amendment of Article 368 itself"],
    0,
    "Article 4(2) explicitly provides that laws made under Article 2 or 3 (admission, formation of new states, boundary changes) 'shall not be deemed to be an amendment of this Constitution for the purposes of article 368'. They are passed by simple parliamentary majority.",
    {"A": "Correct. Article 4(2) states Art. 2 and 3 changes are not Art. 368 amendments.", "B": "Article 55 requires special majority + 50% state ratification.", "C": "Supreme Court Chapter requires special majority + 50% state ratification.", "D": "Article 368 itself requires special majority + 50% state ratification."},
    "Easy", "Article 4(2) & 368", "Identify constitutional changes outside Article 368 scope."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-012", "ch-14", "top-const-14-01",
    "Which of the following schedules can be amended by Parliament by simple majority without invoking Article 368?",
    ["Seventh Schedule (Union, State, Concurrent Lists)", "Fifth Schedule (Scheduled Areas) and Sixth Schedule (Tribal Areas)", "Tenth Schedule (Anti-Defection)", "Fourth Schedule (Allocation of Rajya Sabha seats)"],
    1,
    "Paragraph 7 of the Fifth Schedule and Paragraph 21 of the Sixth Schedule expressly declare that amendments to these Schedules made by Parliament by law 'shall not be deemed to be an amendment of this Constitution for the purposes of article 368'.",
    {"A": "Seventh Schedule requires Art. 368 special majority + 50% state ratification.", "B": "Correct. Fifth and Sixth Schedules can be amended by simple majority outside Art. 368.", "C": "Tenth Schedule requires Article 368 procedure (Kihoto Hollohan).", "D": "Fourth Schedule is amended under Art. 4 or ordinary reorganization laws."},
    "Hard", "Fifth & Sixth Schedule Amendment Clauses", "Identify schedules amendable outside Article 368."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-013", "ch-14", "top-const-14-01",
    "Which Constitutional Amendment Act inserted clauses (4) and (5) into Article 368 declaring that no constitutional amendment shall be called in question in any court, which were subsequently struck down by the Supreme Court?",
    ["24th Amendment Act, 1971", "39th Amendment Act, 1975", "42nd Amendment Act, 1976", "44th Amendment Act, 1978"],
    2,
    "The 42nd Amendment Act, 1976 inserted clauses (4) and (5) into Article 368 seeking to confer unlimited amending power on Parliament and totally excluding judicial review. In Minerva Mills (1980), the Supreme Court struck down clauses (4) and (5) as unconstitutional.",
    {"A": "24th Amendment inserted Art. 368(1) and Art. 13(4).", "B": "39th Amendment placed election of PM beyond judicial review (struck down in Indira Gandhi).", "C": "Correct. 42nd Amendment Act, 1976 inserted clauses (4) and (5).", "D": "44th Amendment repealed parts of 42nd Amendment."},
    "Medium", "Article 368(4), (5) & 42nd Amendment", "Identify amendment inserting non-justiciability clauses in Art. 368."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-014", "ch-14", "top-const-14-01",
    "Under Article 368(1), what is the nature of the power exercised by Parliament when amending the Constitution?",
    ["Administrative power", "Constituent power", "Delegated legislative power", "Judicial power"],
    1,
    "Article 368(1) explicitly provides: 'Parliament may in exercise of its CONSTITUENT POWER amend by way of addition, variation or repeal any provision of this Constitution in accordance with the procedure laid down in this article'. Constituent power is distinct from ordinary legislative power.",
    {"A": "Administrative power belongs to the executive.", "B": "Correct. 'Constituent power' (inserted by 24th Amendment 1971).", "C": "Delegated power is rulemaking by administrative agencies.", "D": "Judicial power belongs to courts."},
    "Easy", "Article 368(1)", "Recall nature of amending power under Article 368."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-015", "ch-14", "top-const-14-01",
    "Can a State Legislative Council be created or abolished under Article 169 through the Article 368 amendment process?",
    ["Yes, Article 169 requires a special majority under Article 368", "No, Article 169(3) explicitly declares that such a law 'shall not be deemed to be an amendment of this Constitution for the purposes of article 368' (passed by simple majority in Parliament following 2/3rds resolution in State Assembly)", "Yes, with ratification by half of the states", "Only the President can abolish a Legislative Council"],
    1,
    "Article 169(3) explicitly provides: 'No such law as aforesaid shall be deemed to be an amendment of this Constitution for the purposes of article 368'. Once the State Assembly passes a resolution by special majority (2/3rds present & voting + total membership), Parliament enacts the law by simple majority.",
    {"A": "Article 169 law is an ordinary parliamentary law.", "B": "Correct. Article 169(3) clarifies it is not an amendment for purposes of Art. 368.", "C": "State ratification under Art. 368 does not apply.", "D": "President acts on parliamentary legislation."},
    "Medium", "Article 169(3)", "Master the mechanism for abolition/creation of Legislative Councils."
))

# ==============================================================================
# TOPIC 14-02: BASIC STRUCTURE DOCTRINE & JURISPRUDENCE (15 MCQs)
# ==============================================================================

MCQS_CH14.append(create_mcq(
    "mcq-const-14-016", "ch-14", "top-const-14-02",
    "In Shankari Prasad v. Union of India (1951), what was the view taken by the Supreme Court regarding the scope of amending power under Article 368?",
    ["Fundamental Rights are sacrosanct and cannot be amended", "The word 'law' in Article 13(2) includes constitutional amendments, hence amendments cannot abridge Fundamental Rights", "The word 'law' in Article 13(2) refers to ordinary legislative enactments and does NOT include constitutional amendments made in exercise of constituent power; thus Parliament can amend Fundamental Rights", "The President has sole power to amend the Constitution"],
    2,
    "In Shankari Prasad (1951), a unanimous 5-judge bench held that 'law' in Article 13(2) applies only to ordinary legislative rules and not to constitutional amendments passed under Article 368 constituent power. Therefore, Fundamental Rights could be amended.",
    {"A": "That was the subsequent holding in Golaknath (1967).", "B": "That was Golaknath's reasoning overruling Shankari Prasad.", "C": "Correct. 'Law' in Art. 13 does not include constitutional amendments; Parliament can amend Part III.", "D": "Executive amendment was never accepted."},
    "Medium", "Shankari Prasad v. UOI (1951)", "Recall the original doctrine on amending Fundamental Rights."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-017", "ch-14", "top-const-14-02",
    "In Sajjan Singh v. State of Rajasthan (1965), which dissenting judge prophetically questioned whether Fundamental Rights could be made playthings of a majority and hinted at basic constitutional features?",
    ["Justice P.B. Gajendragadkar", "Justice J.R. Mudholkar and Justice M. Hidayatullah", "Justice K. Subba Rao", "Justice Vivian Bose"],
    1,
    "In Sajjan Singh (1965), while the majority affirmed Shankari Prasad, Justice J.R. Mudholkar and Justice M. Hidayatullah expressed serious doubts. Justice Mudholkar referred to Pakistan's Supreme Court decision in Fazlul Quader Chowdhry and questioned whether the 'basic features' of the Constitution could be changed at all.",
    {"A": "Gajendragadkar CJ delivered the majority judgment.", "B": "Correct. Justice Mudholkar and Justice Hidayatullah raised the 'basic features' query.", "C": "Subba Rao CJ authored Golaknath in 1967.", "D": "Vivian Bose was not on the Sajjan Singh bench."},
    "Hard", "Sajjan Singh v. State of Rajasthan (1965)", "Identify prophetic dissents anticipating the Basic Structure Doctrine."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-018", "ch-14", "top-const-14-02",
    "In I.C. Golak Nath v. State of Punjab (1967), what was the revolutionary holding of the eleven-judge bench by a 6:5 majority?",
    ["Article 368 contains only the procedure, not the power to amend; constitutional amendments are 'law' within Article 13(2), and Parliament has NO POWER to abridge or take away Fundamental Rights", "Fundamental Rights can be amended by a 3/4ths majority of Parliament", "Judicial review is abolished", "Preamble is not a part of the Constitution"],
    0,
    "In Golak Nath (1967), Chief Justice K. Subba Rao for the 6:5 majority held that Article 368 only laid down procedure; amending power derived from residual legislative powers (Art. 248). An amendment is 'law' under Article 13(2), so Parliament had NO power to abridge or take away any Fundamental Right. The doctrine of Prospective Overruling was applied.",
    {"A": "Correct. Amendments are 'law' under Art. 13(2); Parliament cannot abridge Part III.", "B": "3/4ths majority was not held.", "C": "Judicial review was vigorously asserted.", "D": "Preamble was not the focus in Golak Nath."},
    "Medium", "I.C. Golak Nath v. State of Punjab (1967)", "Explain the core holding in Golak Nath."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-019", "ch-14", "top-const-14-02",
    "Which doctrine was adopted from American jurisprudence by Chief Justice Subba Rao in I.C. Golak Nath (1967) to avoid invalidating all previous amendments (1st, 4th, and 17th)?",
    ["Doctrine of Eclipse", "Doctrine of Severability", "Doctrine of Prospective Overruling", "Doctrine of Pith and Substance"],
    2,
    "To prevent administrative chaos and legal vacuum that would arise from nullifying earlier land reform amendments, Chief Justice Subba Rao applied the 'Doctrine of Prospective Overruling' for the first time in Indian constitutional law, ruling that the decision would operate only on future amendments.",
    {"A": "Doctrine of Eclipse applies to pre-constitutional laws under Art. 13(1).", "B": "Severability separates valid from invalid statutory clauses.", "C": "Correct. Doctrine of Prospective Overruling.", "D": "Pith and substance resolves legislative competence under Lists."},
    "Medium", "Golak Nath & Prospective Overruling", "Identify the doctrinal innovation applied in Golak Nath."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-020", "ch-14", "top-const-14-02",
    "How did Parliament seek to neutralize the judgment in I.C. Golak Nath through the 24th Constitutional Amendment Act, 1971?",
    ["By inserting Article 13(4) and Article 368(3) declaring that Article 13 shall not apply to any amendment made under Article 368", "By abolishing the Supreme Court of India", "By reducing the retirement age of judges to 55", "By removing Part III from the Constitution entirely"],
    0,
    "The 24th Amendment Act, 1971 inserted Article 13(4) ('Nothing in this article shall apply to any amendment of this Constitution made under article 368') and Article 368(3), explicitly insulating constitutional amendments from the definition of 'law' in Article 13.",
    {"A": "Correct. Inserted Art. 13(4) and Art. 368(3) clarifying Art. 13 does not apply to Art. 368.", "B": "Supreme Court was not abolished.", "C": "Retirement age was not changed.", "D": "Part III was retained."},
    "Medium", "24th Amendment Act 1971 & Art. 13(4)", "Explain how 24th Amendment nullified Golak Nath."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-021", "ch-14", "top-const-14-02",
    "What was the size of the Constitution Bench that heard and decided Kesavananda Bharati v. State of Kerala (1973)?",
    ["9 Judges", "11 Judges", "13 Judges (the largest bench in Indian judicial history)", "15 Judges"],
    2,
    "Kesavananda Bharati v. State of Kerala (1973) was heard by a 13-judge Constitution Bench (the largest ever assembled in the Supreme Court of India) for 68 days between October 1972 and March 1973, delivering an 11-opinion judgment of over 700 pages on April 24, 1973.",
    {"A": "9 judges heard Bommai, Second Judges, and Puttaswamy.", "B": "11 judges heard Golak Nath and Bank Nationalisation.", "C": "Correct. 13 Judges (largest Constitution Bench in Indian history).", "D": "15 judges has never been assembled."},
    "Easy", "Kesavananda Bharati (1973)", "Recall bench size of Kesavananda Bharati."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-022", "ch-14", "top-const-14-02",
    "What was the voting ratio of the 13-judge bench in Kesavananda Bharati v. State of Kerala (1973) that established the Basic Structure Doctrine?",
    ["Unanimous (13:0)", "7:6 Majority", "8:5 Majority", "11:2 Majority"],
    1,
    "The Basic Structure Doctrine was established by a razor-thin 7:6 majority: Chief Justice S.M. Sikri, Justices J.M. Shelat, K.S. Hegde, A.N. Grover, P. Jaganmohan Reddy, H.R. Khanna, and B.K. Mukherjea formed the majority, with Justice H.R. Khanna delivering the pivotal controlling judgment.",
    {"A": "The decision was sharply divided, not unanimous.", "B": "Correct. 7:6 Majority.", "C": "8:5 was not the division.", "D": "11:2 was not the division."},
    "Easy", "Kesavananda Bharati Bench Division", "Recall majority-minority split in Kesavananda Bharati."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-023", "ch-14", "top-const-14-02",
    "What is the fundamental thesis of the 'Basic Structure Doctrine' laid down in Kesavananda Bharati v. State of Kerala (1973)?",
    ["Parliament cannot amend any part of the Constitution", "Parliament has wide constituent power to amend any provision of the Constitution (including Fundamental Rights), but this power does NOT extend to damaging, destroying, or altering the 'BASIC STRUCTURE' or essential framework of the Constitution", "Any amendment affecting corporate taxes is unconstitutional", "Amendments must be approved by the President alone without Parliament"],
    1,
    "In Kesavananda Bharati (1973), the Supreme Court overruled Golak Nath and upheld the validity of the 24th Amendment, affirming Parliament's power to amend any part of the Constitution including Fundamental Rights. However, it held that the word 'amend' implies that the original foundational framework must survive: Parliament cannot alter, damage or destroy the 'Basic Structure' of the Constitution.",
    {"A": "Parliament's amending power was reaffirmed, not abolished.", "B": "Correct. Power to amend is plenary, but cannot alter/damage the Basic Structure.", "C": "Taxes do not constitute the basic structure.", "D": "President cannot amend without Parliament."},
    "Medium", "Kesavananda Bharati Core Principle", "Master the essence of the Basic Structure Doctrine."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-024", "ch-14", "top-const-14-02",
    "Whose controlling opinion among the 13 judges in Kesavananda Bharati provided the decisive bridge for the 7:6 majority formulation of the Basic Structure Doctrine?",
    ["Justice A.N. Ray", "Justice H.R. Khanna", "Justice Y.V. Chandrachud", "Justice P.N. Bhagwati"],
    1,
    "Justice H.R. Khanna's judgment was the pivot: he agreed with six judges that Article 368 power was plenary, but agreed with six other judges that the power to 'amend' did not include the power to alter or abrogate the basic structure or framework of the Constitution.",
    {"A": "Justice A.N. Ray was in the 6-judge minority.", "B": "Correct. Justice H.R. Khanna delivered the controlling majority opinion.", "C": "Justice Y.V. Chandrachud was in the minority in 1973.", "D": "Justice Bhagwati was in the minority in 1973."},
    "Medium", "Justice H.R. Khanna & Kesavananda", "Identify the decisive judge behind the Basic Structure compromise."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-025", "ch-14", "top-const-14-02",
    "In Indira Nehru Gandhi v. Raj Narain (1975), which constitutional provision was struck down by the Supreme Court as violating the Basic Structure (marking the FIRST time an amendment was struck down under this doctrine)?",
    ["Article 31C", "Clause (4) of Article 329A (inserted by the 39th Amendment Act, 1975)", "Article 352(3)", "Article 368(4)"],
    1,
    "In Indira Gandhi v. Raj Narain (1975), the Supreme Court struck down Article 329A(4) (inserted by the 39th Amendment to validate Indira Gandhi's election and bar judicial review over PM/Speaker elections) on the ground that it violated the Rule of Law, Free and Fair Elections, and Separation of Powers/Judicial Review — all basic features.",
    {"A": "Article 31C's second part was struck down in Kesavananda, but Indira Gandhi was the first post-Kesavananda invalidation of a full clause.", "B": "Correct. Article 329A(4) inserted by 39th Amendment was struck down.", "C": "Article 352(3) is valid.", "D": "Article 368(4) was struck down later in Minerva Mills (1980)."},
    "Hard", "Indira Nehru Gandhi v. Raj Narain (1975)", "Recall the first case striking down an amendment using Basic Structure."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-026", "ch-14", "top-const-14-02",
    "In Minerva Mills Ltd. v. Union of India (1980), which clauses of Article 368 inserted by the 42nd Amendment Act were struck down as unconstitutional?",
    ["Clauses (1) and (2)", "Clauses (4) and (5)", "Clause (3)", "The Proviso to Article 368(2)"],
    1,
    "In Minerva Mills (1980), the Supreme Court struck down Section 55 of the 42nd Amendment which had inserted clauses (4) and (5) into Article 368. Clause (4) sought to bar judicial review of constitutional amendments, and clause (5) declared there would be no limitation on Parliament's constituent power. The Court held that a limited amending power is itself a basic feature of the Constitution.",
    {"A": "Clauses (1) and (2) are valid.", "B": "Correct. Clauses (4) and (5) of Article 368 were struck down.", "C": "Clause (3) is valid.", "D": "The Proviso to Article 368(2) is valid."},
    "Medium", "Minerva Mills v. UOI (1980) & Art. 368", "Recall which clauses of Article 368 were struck down in Minerva Mills."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-027", "ch-14", "top-const-14-02",
    "In Minerva Mills Ltd. v. Union of India (1980), Chief Justice Y.V. Chandrachud famously observed regarding the relationship between Fundamental Rights and Directive Principles that:",
    ["Directive Principles are superior to Fundamental Rights in all cases", "Fundamental Rights and Directive Principles are like the two wheels of a chariot, and the harmony and balance between them is an essential feature of the Basic Structure", "Fundamental Rights can be entirely suppressed to implement any Directive Principle", "Courts cannot look at Directive Principles"],
    1,
    "Chief Justice Chandrachud poetically held: 'The Indian Constitution is founded on the bedrock of the balance between Parts III and IV. To give absolute primacy to one over the other is to disturb the harmony of the Constitution... They are like two wheels of a chariot, none less important than the other'. This balance is part of the Basic Structure.",
    {"A": "Absolute primacy to DPSPs was explicitly rejected.", "B": "Correct. Harmony and balance between Parts III and IV is a basic feature of the Constitution.", "C": "Total suppression of rights violates basic structure.", "D": "Courts use DPSPs for interpretation."},
    "Medium", "Minerva Mills (1980) & Two Wheels Analogy", "Explain the constitutional balance between Parts III and IV as a basic feature."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-028", "ch-14", "top-const-14-02",
    "In Waman Rao v. Union of India (1981), what cut-off date was established by the Supreme Court for applying the Basic Structure Doctrine to laws placed in the Ninth Schedule?",
    ["January 26, 1950", "April 24, 1973 (the date of the Kesavananda Bharati judgment)", "June 25, 1975", "January 1, 1980"],
    1,
    "In Waman Rao (1981), Chief Justice Y.V. Chandrachud settled that laws placed in the Ninth Schedule BEFORE April 24, 1973 (date of Kesavananda Bharati judgment) receive blanket immunity. However, laws inserted into the Ninth Schedule ON OR AFTER April 24, 1973 are open to challenge if they damage or destroy the Basic Structure. Reaffirmed in I.R. Coelho (2007).",
    {"A": "1950 is commencement date.", "B": "Correct. April 24, 1973 — the date of Kesavananda Bharati.", "C": "June 25, 1975 was declaration of internal emergency.", "D": "1980 is year of Minerva Mills."},
    "Medium", "Waman Rao v. UOI (1981)", "Recall the cut-off date for Ninth Schedule basic structure immunity."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-029", "ch-14", "top-const-14-02",
    "In I.R. Coelho v. State of Tamil Nadu (2007) (9-Judge Bench), what test was laid down to determine the validity of laws inserted into the Ninth Schedule after April 24, 1973?",
    ["The laws are completely immune from judicial review", "The 'Rights Test' or 'Essence of Rights Test': if a Ninth Schedule law abrogates or damages the basic structure or the essence of Fundamental Rights in Articles 14, 19, or 21, it is unconstitutional", "Only laws affecting religion can be reviewed", "The Prime Minister must approve judicial review"],
    1,
    "In I.R. Coelho (2007), a unanimous 9-judge bench led by CJI Y.K. Sabharwal held that the Ninth Schedule cannot be used as a 'constitutional dustbin' or black hole. Any law added to the 9th Schedule after April 24, 1973 must pass the 'Essence of Rights Test' (impact on the golden triangle of Articles 14, 19, and 21 as parts of basic structure).",
    {"A": "Absolute immunity was definitively rejected.", "B": "Correct. The 'Rights Test' (essence of Articles 14, 19, 21 as basic structure).", "C": "Review extends across fundamental freedoms, not merely religion.", "D": "Executive consent for judicial review is alien to constitutional law."},
    "Hard", "I.R. Coelho v. State of T.N. (2007)", "Master the Ninth Schedule jurisprudence and the Essence of Rights test."
))

MCQS_CH14.append(create_mcq(
    "mcq-const-14-030", "ch-14", "top-const-14-02",
    "Which of the following is NOT a recognized component of the 'Basic Structure' of the Indian Constitution according to settled Supreme Court jurisprudence?",
    ["Supremacy of the Constitution and Republican/Democratic form of government", "Secularism, Federalism, and Separation of Powers", "Independence of the Judiciary and Judicial Review", "Absolute and unamendable right to private property under Article 31"],
    3,
    "The right to property was NEVER held to be part of the Basic Structure. In fact, Article 31 was omitted as a Fundamental Right by the 44th Amendment Act, 1978 and converted into a constitutional/statutory right under Article 300A. The others (Supremacy, Secularism, Federalism, Judicial Independence, Judicial Review) are established basic features.",
    {"A": "Supremacy and Democratic form were declared basic features in Kesavananda.", "B": "Secularism (S.R. Bommai) and Federalism (Bommai) are basic features.", "C": "Judicial independence (NJAC 2015) and Judicial review (L. Chandra Kumar) are basic features.", "D": "Correct. Right to property is NOT a basic feature; it was demoted to Art. 300A."},
    "Medium", "Basic Structure Components Catalogue", "Identify elements that do and do not form part of the Basic Structure."
))

if __name__ == "__main__":
    print(f"Generated {len(MCQS_CH14)} MCQs for Chapter 14.")
