# Part 1: Constitutional Law (35), BNS 2023 (40), IPC vs BNS (30) = 105 items

U_CONST = "https://www.indiacode.nic.in/handle/123456789/1522"
U_BNS = "https://www.indiacode.nic.in/handle/123456789/20062"
U_SC = "https://main.sci.gov.in/judgments"

def get_part1_items(m):
    # ---------------------------------------------------------
    # 1. CONSTITUTIONAL LAW (35 items)
    # ---------------------------------------------------------
    m("Article 21 (Right to Life and Personal Liberty) can be suspended by Presidential Order during a National Emergency proclaimed under Article 352.",
      "false", "Constitutional Law", "beginner", "Constitution of India", "Article 359(1)", None,
      "Post-44th Amendment Act 1978, enforcement of Fundamental Rights under Articles 20 and 21 cannot be suspended even during a National Emergency.",
      "Laypersons assume all Fundamental Rights cease during National Emergency, ignoring the post-ADM Jabalpur safeguards.",
      "None. Articles 20 and 21 are non-derogable under Article 359.",
      "can be suspended by Presidential Order", "cannot be suspended even during a National Emergency",
      U_CONST, "Current Constitutional Law", ["Article 21", "Article 20", "Article 359", "44th Amendment", "National Emergency"])

    m("A writ of Mandamus lies against a purely private company discharging no statutory or public duty.",
      "false", "Constitutional Law", "beginner", "Constitution of India", "Article 226", None,
      "Mandamus is a public law remedy that compels the performance of a public or statutory duty. It does not lie against a purely private entity discharging private obligations (Federal Bank v. Sagar Thomas).",
      "Students often assume high courts can issue prerogative writs against any registered corporate body.",
      "Mandamus may lie against a private body if it is discharging a public function or statutory obligation (Zee Telefilms / Binny Ltd).",
      "lies against a purely private company discharging no statutory or public duty", "does not lie against a private company unless it performs a public or statutory duty",
      U_CONST, "Current Constitutional Law", ["Mandamus", "Article 226", "Public Duty", "Judicial Review", "Private Entity"])

    m("The power of Judicial Review over constitutional amendments is an indestructible feature of the Basic Structure.",
      "true", "Constitutional Law", "beginner", "Constitution of India", "Articles 13 & 368", None,
      "In Minerva Mills (1980) and L. Chandra Kumar (1997), the Supreme Court confirmed that Judicial Review is part of the Basic Structure and cannot be abrogated even by constitutional amendment.",
      "Some believe Article 368(4) and (5) successfully excluded judicial review until struck down.",
      "Clauses (4) and (5) of Article 368 attempting to bar judicial review were struck down as unconstitutional.",
      None, None,
      U_CONST, "Current Constitutional Law", ["Judicial Review", "Basic Structure", "Minerva Mills", "L. Chandra Kumar", "Article 368"])

    m("Reasonable restrictions under Article 19(2) can be imposed on the freedom of speech by mere executive order without statutory backing.",
      "false", "Constitutional Law", "intermediate", "Constitution of India", "Article 19(2)", None,
      "Article 19(2) requires restrictions to be imposed by 'law' enacted by a competent legislature. An executive circular or departmental instruction is not a 'law' for abridging Article 19(1)(a) (Bijoe Emmanuel / Kharak Singh).",
      "Many believe executive orders can restrict speech during law-and-order concerns.",
      "Executive action authorized by a valid statutory enactment can regulate time, place, and manner.",
      "can be imposed on the freedom of speech by mere executive order", "must be authorized by an enacted statutory law",
      U_CONST, "Current Constitutional Law", ["Freedom of Speech", "Article 19(2)", "Reasonable Restrictions", "Executive Order", "Statutory Law"])

    m("The doctrine of eclipse applies to post-constitutional laws that violate Fundamental Rights.",
      "false", "Constitutional Law", "advanced", "Constitution of India", "Article 13(2)", None,
      "In Deep Chand v. State of U.P. and Mahendra Lal Jaini, the Supreme Court held that a post-constitutional law violating Part III is stillborn and dead at inception (void ab initio), and cannot be revived by the doctrine of eclipse.",
      "Eclipse is wrongly assumed to revive all unconstitutional laws upon subsequent constitutional amendments.",
      "Doctrine of eclipse applies to pre-constitutional laws under Article 13(1) (Bhikaji Narain Dhakras v. State of M.P.).",
      "applies to post-constitutional laws that violate Fundamental Rights", "applies strictly to pre-constitutional laws under Article 13(1)",
      U_CONST, "Current Constitutional Law", ["Doctrine of Eclipse", "Article 13(1)", "Article 13(2)", "Deep Chand", "Bhikaji Narain"])

    m("A person can be appointed as Attorney General for India only if they are qualified to be appointed as a Judge of the Supreme Court.",
      "true", "Constitutional Law", "beginner", "Constitution of India", "Article 76(1)", None,
      "Article 76(1) mandates that the President shall appoint a person who is qualified to be appointed a Judge of the Supreme Court to be Attorney General for India.",
      "Laypersons confuse statutory law officers with constitutional eligibility benchmarks.",
      "None. Supreme Court judge qualification is mandatory.",
      None, None,
      U_CONST, "Current Constitutional Law", ["Attorney General", "Article 76", "Supreme Court Judge", "Qualification"])

    m("The Speaker of the Lok Sabha cannot vote in the first instance, but exercises a casting vote in case of an equality of votes.",
      "true", "Constitutional Law", "beginner", "Constitution of India", "Article 100(1)", None,
      "Under Article 100(1), the Speaker or person acting as such does not vote in the first instance, but has and must exercise a casting vote in the case of an equality of votes.",
      "Some assume the Speaker votes like any other Member of Parliament on every bill.",
      "The Speaker may vote in the first instance when a resolution for their removal from office is under consideration (Article 96(2)).",
      None, None,
      U_CONST, "Current Constitutional Law", ["Speaker", "Article 100", "Casting Vote", "Lok Sabha", "Parliamentary Procedure"])

    m("The right to a clean environment is an expressly enumerated Fundamental Right in the original text of Part III.",
      "false", "Constitutional Law", "beginner", "Constitution of India", "Articles 21 & 48A", None,
      "The right to a clean and healthy environment is an unenumerated right recognized through expansive judicial interpretation of Article 21 (Subhash Kumar v. State of Bihar & M.C. Mehta).",
      "Candidates frequently confuse judicial interpretation with textual enumeration.",
      "Article 48A is a DPSP in Part IV, not an enumerated Fundamental Right in Part III.",
      "is an expressly enumerated Fundamental Right in the original text", "is an unenumerated right established through judicial interpretation of Article 21",
      U_CONST, "Current Constitutional Law", ["Right to Environment", "Article 21", "Article 48A", "M.C. Mehta", "Subhash Kumar"])

    m("A Money Bill can be introduced in either House of Parliament provided the President recommends it.",
      "false", "Constitutional Law", "beginner", "Constitution of India", "Article 109(1)", None,
      "Under Article 109(1), a Money Bill shall not be introduced in the Council of States (Rajya Sabha); it can only be introduced in the House of the People (Lok Sabha).",
      "Aspirants confuse Money Bills with ordinary bills which can be initiated in either House.",
      "None. Rajya Sabha only receives the bill for recommendations, which Lok Sabha may accept or reject.",
      "can be introduced in either House of Parliament", "can only be introduced in the Lok Sabha",
      U_CONST, "Current Constitutional Law", ["Money Bill", "Article 109", "Article 110", "Lok Sabha", "Rajya Sabha"])

    m("The Preamble to the Constitution of India can be amended under Article 368.",
      "true", "Constitutional Law", "beginner", "Constitution of India", "Preamble & Article 368", None,
      "In Kesavananda Bharati (1973), the Supreme Court held that the Preamble is an integral part of the Constitution and can be amended under Article 368, provided the Basic Structure is not destroyed.",
      "Many mistakenly believe the Preamble is unamendable due to the Berubari Union (1960) ruling.",
      "The 42nd Constitutional Amendment Act, 1976 amended the Preamble to insert 'Socialist', 'Secular', and 'Integrity'.",
      None, None,
      U_CONST, "Current Constitutional Law", ["Preamble", "Article 368", "Kesavananda Bharati", "42nd Amendment", "Basic Structure"])

    m("An Ordinance promulgated by the President under Article 123 has the same force and effect as an Act of Parliament.",
      "true", "Constitutional Law", "beginner", "Constitution of India", "Article 123(2)", None,
      "Article 123(2) expressly provides that an Ordinance promulgated under this article shall have the same force and effect as an Act of Parliament.",
      "Some assume ordinances are inferior subordinate legislation.",
      "An Ordinance ceases to operate at the expiration of 6 weeks from the reassembly of Parliament or upon disapproval resolutions.",
      None, None,
      U_CONST, "Current Constitutional Law", ["Ordinance", "Article 123", "Presidential Power", "Parliament", "Legislative Power"])

    m("The Supreme Court is bound to give its advisory opinion whenever the President makes a reference under Article 143.",
      "depends", "Constitutional Law", "intermediate", "Constitution of India", "Article 143", None,
      "Under Article 143(1) (question of law/fact of public importance), the Supreme Court 'may' report its opinion, retaining discretion to refuse (e.g. Special Reference No. 1 of 1993 - Ayodhya Reference). Under Article 143(2) (pre-constitutional treaties/agreements), the Court is obligated ('shall') to report.",
      "Candidates often state advisory opinion is entirely voluntary or entirely mandatory without distinguishing clauses (1) and (2).",
      "Discretionary under 143(1), mandatory under 143(2).",
      None, None,
      U_CONST, "Current Constitutional Law", ["Advisory Jurisdiction", "Article 143", "Presidential Reference", "Supreme Court", "Discretion"])

    m("The protection against Double Jeopardy under Article 20(2) bars disciplinary departmental proceedings following a criminal acquittal.",
      "false", "Constitutional Law", "intermediate", "Constitution of India", "Article 20(2)", None,
      "Article 20(2) protects against being prosecuted and punished for the same offence more than once before a court of law. Departmental inquiries are administrative, not judicial prosecutions (Venkataraman v. Union of India).",
      "Candidates confuse administrative disciplinary action with judicial prosecution.",
      "A departmental inquiry may be stayed if based on identical grave criminal charges involving complex questions of law.",
      "bars disciplinary departmental proceedings following a criminal acquittal", "does not bar departmental proceedings as they are not judicial prosecutions",
      U_CONST, "Current Constitutional Law", ["Double Jeopardy", "Article 20(2)", "Departmental Inquiry", "Prosecution", "Venkataraman"])

    m("The right against self-incrimination under Article 20(3) protects witnesses appearing in purely civil or revenue proceedings.",
      "false", "Constitutional Law", "intermediate", "Constitution of India", "Article 20(3)", None,
      "Article 20(3) states that no person 'accused of any offence' shall be compelled to be a witness against himself. It is strictly limited to criminal proceedings where formal accusation exists (M.P. Sharma v. Satish Chandra / Nandini Satpathy).",
      "Many believe Article 20(3) can be invoked in any legal hearing or tax inquiry.",
      "If answers in a civil/revenue inquiry tend to expose the person to criminal prosecution, protection can be claimed at that threshold.",
      "protects witnesses appearing in purely civil or revenue proceedings", "applies strictly to a person accused of a criminal offence",
      U_CONST, "Current Constitutional Law", ["Self Incrimination", "Article 20(3)", "Accused", "Civil Proceedings", "Nandini Satpathy"])

    m("The Right to Property remains a Fundamental Right enforceable through writ petitions under Article 32.",
      "false", "Constitutional Law", "beginner", "Constitution of India", "Article 300A", None,
      "The 44th Constitutional Amendment Act, 1978 repealed Article 19(1)(f) and Article 31, transforming the Right to Property into a constitutional legal right under Article 300A, enforceable under Article 226, not Article 32.",
      "Outdated textbooks or non-legal general knowledge questions sometimes treat property as a Fundamental Right.",
      "Article 300A still guarantees that no person shall be deprived of their property save by authority of law.",
      "remains a Fundamental Right enforceable through writ petitions under Article 32", "is a constitutional legal right under Article 300A, not a Fundamental Right",
      U_CONST, "Current Constitutional Law", ["Right to Property", "Article 300A", "Article 31", "44th Amendment", "Article 32"])

    m("The Curative Petition mechanism was created by the Supreme Court to prevent miscarriage of justice after dismissal of a review petition.",
      "true", "Constitutional Law", "intermediate", "Constitution of India", "Articles 137 & 142", None,
      "In Rupa Ashok Hurra v. Ashok Hurra (2002), a Constitution Bench recognized curative petitions under inherent powers (Articles 137 and 142) on grounds of violation of natural justice or apprehension of bias.",
      "Some assume judicial remedies conclude irreversibly with the dismissal of a review petition.",
      "Curative petitions require certification by a Senior Advocate and circulation before the 3 senior-most judges plus the bench that passed the order.",
      None, None,
      U_CONST, "Current Constitutional Law", ["Curative Petition", "Rupa Ashok Hurra", "Article 137", "Article 142", "Natural Justice"])

    m("The Governor has the power under Article 161 to completely pardon a sentence of death.",
      "false", "Constitutional Law", "intermediate", "Constitution of India", "Articles 72 & 161", None,
      "Under Article 72, the President alone possesses the power to grant a complete pardon in all cases where the sentence is one of death. Under Article 161, the Governor may suspend, remit, or commute a death sentence, but cannot pardon it.",
      "Candidates confuse commutation/remission with full pardon of capital punishment.",
      "The Governor may remit or commute death sentences to imprisonment for life under state laws.",
      "has the power under Article 161 to completely pardon a sentence of death", "cannot pardon a death sentence as that power belongs exclusively to the President under Article 72",
      U_CONST, "Current Constitutional Law", ["Pardoning Power", "Article 72", "Article 161", "Death Sentence", "Governor"])

    m("A Proclamation of President's Rule under Article 356 is immune from judicial review.",
      "false", "Constitutional Law", "beginner", "Constitution of India", "Article 356", None,
      "In the landmark 9-judge bench decision in S.R. Bommai v. Union of India (1994), the Supreme Court ruled that a proclamation under Article 356 is subject to judicial review on grounds of mala fides or irrelevant considerations.",
      "Prior to Bommai and during the 38th Amendment era, it was thought executive satisfaction was unchallengeable.",
      "The Court does not substitute its own wisdom for the President's, but assesses material relevancy.",
      "is immune from judicial review", "is subject to judicial review on grounds of mala fides or irrationality",
      U_CONST, "Current Constitutional Law", ["President's Rule", "Article 356", "S.R. Bommai", "Judicial Review", "Proclamation"])

    m("The writ jurisdiction of High Courts under Article 226 is wider in scope than that of the Supreme Court under Article 32.",
      "true", "Constitutional Law", "beginner", "Constitution of India", "Articles 32 & 226", None,
      "The Supreme Court under Article 32 can issue writs solely for the enforcement of Fundamental Rights (Part III), whereas High Courts under Article 226 can issue writs for Fundamental Rights 'and for any other purpose' (legal rights).",
      "Laypersons assume the apex court must have broader jurisdiction in every parameter.",
      "Article 32 is itself a Fundamental Right, whereas Article 226 is a constitutional power.",
      None, None,
      U_CONST, "Current Constitutional Law", ["Article 226", "Article 32", "Writ Jurisdiction", "High Court", "Supreme Court"])

    m("Directive Principles of State Policy (Part IV) are justiciable and enforceable by courts in the same manner as Fundamental Rights.",
      "false", "Constitutional Law", "beginner", "Constitution of India", "Article 37", None,
      "Article 37 explicitly declares that the provisions contained in Part IV 'shall not be enforceable by any court', though they are fundamental in the governance of the country.",
      "Citizens often believe DPSPs can be enforced via mandamus.",
      "Courts frequently use DPSPs as interpretive tools to expand the scope of Fundamental Rights (e.g. Article 21).",
      "are justiciable and enforceable by courts in the same manner", "are non-justiciable and cannot be directly enforced by courts under Article 37",
      U_CONST, "Current Constitutional Law", ["DPSP", "Part IV", "Article 37", "Non-justiciable", "Fundamental Rights"])

    m("The guarantee of equality before the law under Article 14 prohibits all legislative classification.",
      "false", "Constitutional Law", "intermediate", "Constitution of India", "Article 14", None,
      "Article 14 forbids class legislation but permits reasonable classification, provided it is founded on an intelligible differentia and has a rational nexus to the statutory objective (State of W.B. v. Anwar Ali Sarkar).",
      "Aspirants confuse universal identical treatment with constitutional non-discrimination.",
      "Arbitrary classification without rational nexus violates Article 14 (E.P. Royappa doctrine).",
      "prohibits all legislative classification", "permits reasonable classification based on intelligible differentia with a rational nexus",
      U_CONST, "Current Constitutional Law", ["Article 14", "Reasonable Classification", "Intelligible Differentia", "Rational Nexus", "Equality"])

    m("The freedom of conscience and religion under Article 25 is absolute and immune from state regulation.",
      "false", "Constitutional Law", "beginner", "Constitution of India", "Article 25(1)", None,
      "Article 25(1) specifically makes the freedom of religion subject to 'public order, morality, and health' as well as the other provisions of Part III.",
      "Religious adherents often believe their freedom of faith cannot be curtailed by secular laws.",
      "Essential religious practices are protected, but secular activities associated with religion can be regulated by law (Article 25(2)).",
      "is absolute and immune from state regulation", "is expressly subject to public order, morality, health, and other Fundamental Rights",
      U_CONST, "Current Constitutional Law", ["Article 25", "Freedom of Religion", "Public Order", "Morality", "Essential Religious Practice"])

    m("Article 31C shields a law giving effect to Directive Principles in Article 39(b) and (c) from challenge under Articles 14 and 19.",
      "true", "Constitutional Law", "advanced", "Constitution of India", "Article 31C", None,
      "The first part of Article 31C was upheld in Kesavananda Bharati (1973), shielding legislation distributing material resources (39(b)) or preventing concentration of wealth (39(c)) from challenge under Articles 14 and 19.",
      "Minerva Mills struck down the 42nd Amendment expansion of 31C to all DPSPs, leading some to assume the entire article was struck down.",
      "The second part ('no law containing a declaration... shall be called in question') was struck down.",
      None, None,
      U_CONST, "Current Constitutional Law", ["Article 31C", "Article 39(b)", "Article 39(c)", "Kesavananda Bharati", "Minerva Mills"])

    m("The Supreme Court has the power to transfer a case or appeal from one High Court to another High Court.",
      "true", "Constitutional Law", "intermediate", "Constitution of India", "Article 139A(2)", None,
      "Under Article 139A(2), the Supreme Court may, if it deems expedient for the ends of justice, transfer any case, appeal, or other proceeding pending before any High Court to any other High Court.",
      "Some assume high courts are sovereign within their territories and immune to apex transfer orders.",
      "Application must be made by the Attorney General for India or by an interested party.",
      None, None,
      U_CONST, "Current Constitutional Law", ["Article 139A", "Transfer of Cases", "Supreme Court", "High Court", "Jurisdiction"])

    m("A person detained under preventive detention can be kept in detention indefinitely without reference to an Advisory Board.",
      "false", "Constitutional Law", "intermediate", "Constitution of India", "Article 22(4)", None,
      "Article 22(4) mandates that no law providing for preventive detention shall authorize the detention of a person for a period longer than 3 months unless an Advisory Board finds sufficient cause.",
      "Preventive detention is mistakenly viewed as unchecked executive imprisonment.",
      "Parliament may prescribe maximum detention periods and procedures by law.",
      "can be kept in detention indefinitely without reference to an Advisory Board", "cannot be detained for more than 3 months without an Advisory Board's approval",
      U_CONST, "Current Constitutional Law", ["Preventive Detention", "Article 22", "Advisory Board", "Three Months", "Liberty"])

    m("Fundamental Duties under Article 51A were part of the original Constitution drafted in 1949.",
      "false", "Constitutional Law", "beginner", "Constitution of India", "Part IVA & Article 51A", None,
      "Fundamental Duties were incorporated into Part IVA by the 42nd Constitutional Amendment Act, 1976 upon the recommendation of the Swaran Singh Committee. The 11th duty was added by the 86th Amendment in 2002.",
      "Aspirants frequently confuse original provisions with 42nd Amendment additions.",
      "None. They were completely absent in the 1949 text.",
      "were part of the original Constitution drafted in 1949", "were added by the 42nd Constitutional Amendment Act, 1976",
      U_CONST, "Current Constitutional Law", ["Fundamental Duties", "Article 51A", "42nd Amendment", "Swaran Singh Committee", "Part IVA"])

    m("Under the Doctrine of Severability, if an invalid provision of a statute cannot be separated from the valid part, the entire statute falls.",
      "true", "Constitutional Law", "intermediate", "Constitution of India", "Article 13(1)", None,
      "In R.M.D. Chamarbaugwalla v. Union of India (1957), the Supreme Court laid down that if the valid and invalid provisions are so inextricably bound that the legislature would not have enacted the valid part alone, the whole statute is void.",
      "Candidates mistakenly think courts always preserve the surviving clauses regardless of legislative intent.",
      "If the valid portion is independent and self-sustaining, only the unconstitutional section is struck down.",
      None, None,
      U_CONST, "Current Constitutional Law", ["Doctrine of Severability", "Article 13", "R.M.D. Chamarbaugwalla", "Constitutionality", "Void Statutes"])

    m("Residuary legislative powers in the Indian federation vest in the State Legislatures.",
      "false", "Constitutional Law", "beginner", "Constitution of India", "Article 248 & List I Entry 97", None,
      "Unlike the United States or Australia, residuary legislative powers in India are vested exclusively in Parliament under Article 248 and Entry 97 of the Union List (Seventh Schedule).",
      "Candidates confuse Indian federalism with the classical American model where residuary powers belong to the states.",
      "None in India; Parliament has sole competence.",
      "vest in the State Legislatures", "vest exclusively in the Union Parliament under Article 248",
      U_CONST, "Current Constitutional Law", ["Residuary Powers", "Article 248", "Parliament", "Union List", "Federalism"])

    m("Adjudication of disputes relating to waters of inter-state rivers is barred from the jurisdiction of the Supreme Court if Parliament so enacts under Article 262.",
      "true", "Constitutional Law", "intermediate", "Constitution of India", "Article 262(2)", None,
      "Article 262(2) empowers Parliament by law to provide that neither the Supreme Court nor any other court shall exercise jurisdiction in respect of inter-state water disputes, enacted via the Inter-State River Water Disputes Act, 1956.",
      "Many believe Article 131 original jurisdiction can never be excluded by statute.",
      "The Supreme Court can still review tribunal orders under Article 136 special leave on constitutional grounds.",
      None, None,
      U_CONST, "Current Constitutional Law", ["Article 262", "Inter-State Water Disputes", "Supreme Court Jurisdiction", "Tribunals", "Federal Disputes"])

    m("All disputes arising out of the election of the President or Vice-President can only be decided by the Supreme Court.",
      "true", "Constitutional Law", "beginner", "Constitution of India", "Article 71(1)", None,
      "Article 71(1) mandates that all doubts and disputes arising out of or in connection with the election of a President or Vice-President shall be inquired into and decided exclusively by the Supreme Court, whose decision shall be final.",
      "Some assume election petitions for the President are filed in the Delhi High Court or Election Commission.",
      "Election cannot be challenged on the ground of any vacancy in the electoral college (Article 71(4)).",
      None, None,
      U_CONST, "Current Constitutional Law", ["Article 71", "Presidential Election", "Supreme Court", "Electoral Disputes", "Vice-President"])

    m("Minority educational institutions under Article 30(1) enjoy complete immunity from state regulations concerning academic standards and teacher welfare.",
      "false", "Constitutional Law", "advanced", "Constitution of India", "Article 30(1)", None,
      "In T.M.A. Pai Foundation and P.A. Inamdar, the Supreme Court established that the right under Article 30(1) is to administer, not to maladminister; regulatory measures for academic excellence, syllabus, sanitation, and labour welfare apply equally.",
      "Aspirants believe minority status confers uninhibited autonomy from all statutory regulations.",
      "Regulations must not destroy or obliterate the minority character of the institution.",
      "enjoy complete immunity from state regulations concerning academic standards", "are subject to reasonable state regulations ensuring academic excellence and teacher welfare",
      U_CONST, "Current Constitutional Law", ["Article 30", "Minority Institutions", "T.M.A. Pai", "P.A. Inamdar", "Educational Standards"])

    m("The President is bound to act in accordance with the advice tendered by the Council of Ministers in all circumstances without any exception.",
      "false", "Constitutional Law", "intermediate", "Constitution of India", "Article 74(1)", None,
      "Under the proviso to Article 74(1) (added by 44th Amendment), the President may require the Council of Ministers to reconsider such advice once. Furthermore, situational discretions exist (e.g. appointment of PM when no majority exists, dismissing a ministry that lost confidence).",
      "People assume the President is an absolute rubber stamp with zero discretionary pause.",
      "After one reconsideration, the President is bound by the reconsidered advice.",
      "without any exception", "subject to the power to seek reconsideration once under the proviso to Article 74(1)",
      U_CONST, "Current Constitutional Law", ["Article 74", "President", "Council of Ministers", "Reconsideration", "Aid and Advice"])

    m("The law declared by the Supreme Court is binding on all courts within the territory of India, including the Supreme Court itself.",
      "false", "Constitutional Law", "intermediate", "Constitution of India", "Article 141", None,
      "Article 141 makes the law declared by the Supreme Court binding on 'all courts within the territory of India', but the Supreme Court itself is not bound by its own earlier decisions and can overrule them (Bengal Immunity / Kesavananda Bharati).",
      "Many believe stare decisis binds the Supreme Court irrevocably to its own precedents.",
      "A bench of coordinate strength is bound by an earlier coordinate bench, requiring reference to a larger bench for reconsideration.",
      "including the Supreme Court itself", "excluding the Supreme Court itself which has the power to overrule its own precedents",
      U_CONST, "Current Constitutional Law", ["Article 141", "Precedent", "Stare Decisis", "Supreme Court", "Bengal Immunity"])

    m("The Right to Privacy was declared a Fundamental Right protected under Article 21 by a 9-judge Constitution Bench in K.S. Puttaswamy.",
      "true", "Constitutional Law", "beginner", "Constitution of India", "Article 21", None,
      "In Justice K.S. Puttaswamy (Retd.) v. Union of India (2017), a unanimous 9-judge bench explicitly declared the Right to Privacy an intrinsic part of the Right to Life and Personal Liberty under Article 21.",
      "Before Puttaswamy, earlier 8-judge bench in M.P. Sharma (1954) and 6-judge bench in Kharak Singh (1962) caused ambiguity.",
      "Privacy is not an absolute right and can be restricted meeting the three-fold test of legality, legitimate aim, and proportionality.",
      None, None,
      U_CONST, "Current Constitutional Law", ["Right to Privacy", "Article 21", "Puttaswamy", "Proportionality", "Fundamental Rights"])

    m("The Right to Education under Article 21A guarantees free and compulsory education to all children until the age of 18 years.",
      "false", "Constitutional Law", "beginner", "Constitution of India", "Article 21A", None,
      "Article 21A guarantees free and compulsory education specifically to all children of the age of six to fourteen years (6-14 years), not up to 18 years.",
      "Candidates confuse juvenile age under POCSO/JJ Act (18 years) with the Article 21A age bracket (6 to 14 years).",
      "Early childhood care below 6 years is covered under Article 45 (DPSP).",
      "until the age of 18 years", "between the ages of six and fourteen years",
      U_CONST, "Current Constitutional Law", ["Article 21A", "Right to Education", "86th Amendment", "Age Limit", "Compulsory Education"])

    # ---------------------------------------------------------
    # 2. BHARATIYA NYAYA SANHITA (BNS) 2023 (40 items)
    # ---------------------------------------------------------
    m("Community service has been introduced as an enumerated form of statutory punishment under Section 4(f) of the BNS, 2023.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 4(f)", None,
      "Section 4(f) of the BNS, 2023 adds 'Community Service' as an official statutory punishment for small offences such as defamation, public servant unlawfully engaging in trade, and non-serious theft.",
      "Many assume community service was only an informal judicial innovation without express statutory status.",
      "Applicable only to specified minor offences under the Sanhita.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Community Service", "Section 4", "Punishment", "BNS 2023", "Penal Reform"])

    m("Murder is defined in Section 101 and punished under Section 103 of the Bharatiya Nyaya Sanhita, 2023.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Sections 101 & 103", None,
      "Under BNS 2023, Section 101 defines murder (corresponding to old IPC 300) and Section 103 prescribes punishment for murder (corresponding to old IPC 302).",
      "Lawyers accustomed to IPC 300/302 often confuse the new chapter and section numbering.",
      "Section 103(2) creates a distinct aggravated clause for mob lynching.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Murder", "Section 101", "Section 103", "Punishment", "BNS 2023"])

    m("The historic offence of Sedition has been retained under the exact same name in the Bharatiya Nyaya Sanhita, 2023.",
      "false", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 152", None,
      "The colonial offence of 'Sedition' (old Section 124A IPC) has been formally repealed. Section 152 BNS now penalizes 'Acts endangering sovereignty, unity and integrity of India' without using the word sedition.",
      "News media often erroneously reported that sedition was kept unchanged under BNS.",
      "Section 152 requires exciting secession, armed rebellion, or subversive activities, with explanatory safeguards for lawful criticism.",
      "has been retained under the exact same name", "has been repealed and replaced by Section 152 (Acts endangering sovereignty and integrity of India)",
      U_BNS, "Current Law (in force from July 1, 2024)", ["Sedition", "Section 152", "Sovereignty", "IPC 124A", "BNS 2023"],
      {"oldAct": "IPC 1860", "oldSection": "124A", "newAct": "BNS 2023", "newSection": "152", "substantiveChange": "Term 'sedition' repealed; replaced by acts endangering sovereignty, unity, and integrity."})

    m("Section 103(2) of the BNS introduces a specific statutory punishment for murder committed by a mob of five or more persons on grounds of race, caste, or community.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 103(2)", None,
      "Section 103(2) BNS specifically penalizes mob lynching where a group of 5 or more persons acting in concert commits murder on grounds of race, caste, community, sex, place of birth, language, or personal belief.",
      "Under IPC, mob lynching had to be prosecuted using general common intention (IPC 34) or unlawful assembly (IPC 149).",
      "Punishment under 103(2) is death or imprisonment for life, and fine.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Mob Lynching", "Section 103(2)", "Murder", "Group Violence", "BNS 2023"])

    m("Snatching is recognized as a specific standalone offence under Section 304 of the Bharatiya Nyaya Sanhita, 2023.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 304", None,
      "Section 304 BNS defines snatching as sudden, quickly seizing, securing or grabbing movable property from a person, filling a long-standing gap in central penal legislation.",
      "Under the old IPC, snatching had to be prosecuted under ordinary theft (IPC 379) or state amendments.",
      "Punished with imprisonment up to 3 years and fine.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Snatching", "Section 304", "Theft", "Property Offence", "BNS 2023"])

    m("Organized crime is penalized under Section 111 of the Bharatiya Nyaya Sanhita, 2023 as a distinct statutory offence.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "intermediate", "Bharatiya Nyaya Sanhita, 2023", "Section 111", None,
      "Section 111 BNS introduces a comprehensive definition of organized crime syndicate activities, including kidnapping, robbery, extortion, land grabbing, and cybercrimes.",
      "Previously, organized crime was only tackled under state enactments like MCOCA or UP Gangsters Act.",
      "Requires continuing unlawful activity by a member of a crime syndicate.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Organized Crime", "Section 111", "Syndicate", "Severe Penalties", "BNS 2023"])

    m("The Bharatiya Nyaya Sanhita, 2023 incorporates 'Terrorist Act' as a penal offence within the general penal code under Section 113.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "intermediate", "Bharatiya Nyaya Sanhita, 2023", "Section 113", None,
      "Section 113 BNS imports the definition of a terrorist act into the general criminal code, parallel to the provisions of UAPA, 1967.",
      "Historically, IPC did not contain a dedicated section on terrorist acts.",
      "An officer not below the rank of Superintendent of Police decides whether to register under BNS or UAPA.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Terrorist Act", "Section 113", "BNS 2023", "UAPA", "National Security"])

    m("Petty organized crime is defined and punished under Section 112 of the Bharatiya Nyaya Sanhita, 2023.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "intermediate", "Bharatiya Nyaya Sanhita, 2023", "Section 112", None,
      "Section 112 BNS penalizes petty organized crime such as theft, snatching, cheating, ticket unauthorized selling, betting, or card skimming committed by organized groups.",
      "Helps curb recurring street gangs that operated beneath severe special gang statutes.",
      "Punished with imprisonment from 1 to 7 years, and fine.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Petty Organized Crime", "Section 112", "Street Gangs", "Theft", "BNS 2023"])

    m("Sexual intercourse by employing deceitful means or making a false promise to marry is explicitly penalized under Section 69 of the BNS, 2023.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 69", None,
      "Section 69 BNS penalizes sexual intercourse by deceitful means (including false promise of employment, promotion, or marriage without intent to fulfill), distinct from rape under Section 63.",
      "Under IPC, this had to be prosecuted under IPC 375 (consent vitiated by misconception of fact under IPC 90).",
      "Punishable with imprisonment up to 10 years and fine.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Section 69", "Deceitful Means", "False Promise of Marriage", "BNS 2023", "Sexual Offences"])

    m("An attempt to commit suicide is punishable under all circumstances under the Bharatiya Nyaya Sanhita, 2023.",
      "false", "Bharatiya Nyaya Sanhita, 2023", "intermediate", "Bharatiya Nyaya Sanhita, 2023", "Section 226", None,
      "Ordinary attempt to commit suicide (old IPC 309) is omitted. Section 226 BNS only punishes attempting suicide with the specific intent to compel or restrain a public servant from discharging official duties.",
      "Many believe BNS restored the old blanket criminalization of suicide attempt.",
      "General suicide attempts are treated under Section 115 of the Mental Healthcare Act, 2017.",
      "under all circumstances under the Bharatiya Nyaya Sanhita, 2023", "only when committed with intent to compel or restrain a public servant under Section 226",
      U_BNS, "Current Law (in force from July 1, 2024)", ["Suicide Attempt", "Section 226", "Public Servant", "IPC 309", "Mental Healthcare Act"],
      {"oldAct": "IPC 1860", "oldSection": "309", "newAct": "BNS 2023", "newSection": "226", "substantiveChange": "General suicide attempt decriminalized; only attempts intended to compel public servants are penalized."})

    m("Under Section 41 of the BNS, the right of private defence of property extends to causing death in the case of robbery.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 41", None,
      "Section 41 BNS (corresponding to old IPC 103) enumerates offences where private defence of property extends to causing death: robbery, house-breaking by night, mischief by fire, and theft/mischief/house-trespass causing apprehension of death or grievous hurt.",
      "Some assume private defence of property never allows causing death under any circumstances.",
      "Harm inflicted must not exceed what is strictly necessary for defence.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Private Defence", "Section 41", "Robbery", "Property Defence", "BNS 2023"])

    m("An act done by a child under seven years of age is an offence under the Bharatiya Nyaya Sanhita, 2023.",
      "false", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 20", None,
      "Section 20 BNS (corresponding to old IPC 82) retains the absolute defence of infancy (doli incapax): 'Nothing is an offence which is done by a child under seven years of age.'",
      "Some assume the lower age limit for criminal liability was raised to 12 years in BNS.",
      "Between 7 and 12 years, liability depends on maturity of understanding under Section 21 BNS.",
      "is an offence under the Bharatiya Nyaya Sanhita, 2023", "is not an offence under the absolute immunity of Section 20 (doli incapax)",
      U_BNS, "Current Law (in force from July 1, 2024)", ["Doli Incapax", "Section 20", "Child Under 7", "Infancy Defence", "BNS 2023"])

    m("Unsoundness of mind at the time of committing an act provides an absolute general exception under Section 22 of the BNS, 2023.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 22", None,
      "Section 22 BNS (corresponding to old IPC 84) embodies the M'Naghten rule: nothing is an offence done by a person who, by reason of unsoundness of mind, is incapable of knowing the nature of the act or that it is wrong.",
      "Laypersons confuse medical insanity with legal insanity.",
      "Legal insanity at the exact moment of the act must be proven by the defence.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Unsoundness of Mind", "Section 22", "Legal Insanity", "M'Naghten", "BNS 2023"])

    m("Involuntary intoxication administered without knowledge or against one's will is a complete defence under Section 23 of the BNS, 2023.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 23", None,
      "Section 23 BNS (old IPC 85) provides that nothing is an offence done by a person incapable of knowing the nature of the act by reason of intoxication administered without his knowledge or against his will.",
      "Voluntary intoxication is excluded from Section 23 protection and governed by Section 24.",
      "Requires that the state of intoxication was non-consensual.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Involuntary Intoxication", "Section 23", "General Exceptions", "BNS 2023", "Criminal Law"])

    m("A consent given by a child under twelve years of age is valid in law to excuse causing hurt under the BNS.",
      "false", "Bharatiya Nyaya Sanhita, 2023", "intermediate", "Bharatiya Nyaya Sanhita, 2023", "Section 27", None,
      "Section 27 BNS (corresponding to old IPC 90) expressly provides that a consent is not a valid consent if it is given by a person who is under twelve years of age.",
      "Candidates confuse 12 years (consent threshold) with 7 years (doli incapax) and 18 years (majority).",
      "Consent given by parent/guardian for benefit of child under 12 is protected under Section 29 BNS.",
      "is valid in law to excuse causing hurt under the BNS", "is invalid under Section 27 which bars consent given by a child under twelve years",
      U_BNS, "Current Law (in force from July 1, 2024)", ["Consent", "Section 27", "Child under 12", "General Exceptions", "BNS 2023"])

    m("Causing death by rash or negligent act is penalized under Section 106(1) of the Bharatiya Nyaya Sanhita, 2023.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 106(1)", None,
      "Section 106(1) BNS (corresponding to old IPC 304A) penalizes causing death by any rash or negligent act not amounting to culpable homicide with imprisonment up to 5 years.",
      "Under old IPC 304A, the maximum term was 2 years; BNS 106(1) increased it to 5 years (and registered medical practitioners up to 2 years).",
      "Subsection (2) governs hit-and-run incidents.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Section 106", "Negligence", "Death by Negligence", "BNS 2023", "IPC 304A"])

    m("Under Section 106(2) of the BNS, fleeing the scene of a rash driving accident without reporting to police carries up to ten years imprisonment.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 106(2)", None,
      "Section 106(2) BNS provides that whoever escapes without reporting to a police officer or magistrate soon after causing death by rash and negligent driving shall be punished with imprisonment up to 10 years and fine.",
      "This is a major enhancement from the old law to address hit-and-run fatalities.",
      "Operation of Section 106(2) was placed under administrative consultation regarding commercial drivers.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Hit and Run", "Section 106(2)", "Rash Driving", "Ten Years Imprisonment", "BNS 2023"])

    m("Abetment is defined under Section 45 of the Bharatiya Nyaya Sanhita, 2023.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 45", None,
      "Section 45 BNS (corresponding to old IPC 107) defines abetment of a thing through instigation, engagement in conspiracy, or intentional aiding.",
      "Moved from Chapter V of IPC (Sec 107) to Chapter IV of BNS (Sec 45).",
      "Abetment in India of offences outside India is covered under Section 49 BNS.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Abetment", "Section 45", "Instigation", "Conspiracy", "BNS 2023"])

    m("Criminal conspiracy is defined under Section 61(1) and punished under Section 61(2) of the Bharatiya Nyaya Sanhita, 2023.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 61", None,
      "Section 61 BNS consolidates criminal conspiracy (old IPC 120A and 120B) into a single streamlined section.",
      "An agreement between two or more persons to do an illegal act or an act by illegal means constitutes conspiracy.",
      "For acts not offences, an overt act in pursuance is necessary.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Criminal Conspiracy", "Section 61", "Agreement", "BNS 2023", "IPC 120B"])

    m("An assembly of three persons with a common illegal object constitutes an Unlawful Assembly under the BNS, 2023.",
      "false", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 189", None,
      "Section 189(1) BNS (corresponding to old IPC 141) strictly requires an assembly of five or more persons to constitute an unlawful assembly.",
      "Candidates sometimes confuse the minimum membership of conspiracy (2), affray (2), and unlawful assembly (5).",
      "If the number drops below 5 bona fide members, unlawful assembly cannot be sustained.",
      "An assembly of three persons with a common illegal object", "An assembly requires five or more persons under Section 189",
      U_BNS, "Current Law (in force from July 1, 2024)", ["Unlawful Assembly", "Section 189", "Five or More", "BNS 2023", "IPC 141"])

    m("Rioting is defined under Section 191 of the Bharatiya Nyaya Sanhita, 2023.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 191", None,
      "Section 191(1) BNS (old IPC 146) provides that whenever force or violence is used by an unlawful assembly or any member thereof in prosecution of common object, every member is guilty of rioting.",
      "Force or violence is the essential ingredient distinguishing rioting from an unlawful assembly.",
      "Armed with deadly weapon is punished under Section 191(3) BNS.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Rioting", "Section 191", "Force and Violence", "Unlawful Assembly", "BNS 2023"])

    m("The offence of Affray under Section 194 of the BNS can be committed in a private residence as well as in public.",
      "false", "Bharatiya Nyaya Sanhita, 2023", "intermediate", "Bharatiya Nyaya Sanhita, 2023", "Section 194", None,
      "Section 194 BNS (old IPC 159) strictly requires that two or more persons fight in a public place and disturb the public peace. Fighting inside a private residence does not constitute affray.",
      "Laypersons think any mutual physical altercation amounts to affray.",
      "Private fighting may constitute assault or hurt, but not affray.",
      "can be committed in a private residence as well as in public", "must strictly take place in a public place disturbing public peace",
      U_BNS, "Current Law (in force from July 1, 2024)", ["Affray", "Section 194", "Public Place", "Breach of Peace", "BNS 2023"])

    m("Giving false evidence (perjury) and fabricating false evidence are defined under Sections 227 and 228 of the BNS, 2023.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "intermediate", "Bharatiya Nyaya Sanhita, 2023", "Sections 227 & 228", None,
      "Section 227 defines giving false evidence (old IPC 191) and Section 228 defines fabricating false evidence (old IPC 192). Section 229 penalizes them (old IPC 193).",
      "Essential for judicial integrity and UP PCS-J Paper II.",
      "Giving false evidence in capital trials carries up to life imprisonment under Section 230 BNS.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Perjury", "Section 227", "Section 228", "False Evidence", "BNS 2023"])

    m("Public nuisance is defined and penalized under Section 270 of the Bharatiya Nyaya Sanhita, 2023.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 270", None,
      "Section 270 BNS (corresponding to old IPC 268) defines a person guilty of a public nuisance who does any act causing common injury, danger or annoyance to the public.",
      "A common nuisance cannot be excused on the ground that it causes some convenience or advantage.",
      "Private nuisance gives rise only to civil remedies, whereas public nuisance is a penal offence.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Public Nuisance", "Section 270", "Common Injury", "Annoyance", "BNS 2023"])

    m("Rash driving or riding on a public way is punishable under Section 281 of the Bharatiya Nyaya Sanhita, 2023.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 281", None,
      "Section 281 BNS (corresponding to old IPC 279) penalizes driving any vehicle rashly or negligently on a public way so as to endanger human life or cause hurt, with imprisonment up to 6 months or fine up to 1,000 rupees, or both.",
      "Moved from Section 279 IPC to Section 281 BNS.",
      "Applicable to driving on any public way.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Rash Driving", "Section 281", "Public Way", "IPC 279", "BNS 2023"])

    m("Culpable homicide not amounting to murder is defined under Section 100 of the Bharatiya Nyaya Sanhita, 2023.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 100", None,
      "Section 100 BNS (corresponding to old IPC 299) defines culpable homicide: causing death by doing an act with the intention of causing death, or causing bodily injury likely to cause death, or with knowledge that the act is likely to cause death.",
      "Section 105 BNS prescribes the punishment for culpable homicide not amounting to murder (old IPC 304).",
      "Distinction between intention and knowledge governs Parts I and II of Section 105.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Culpable Homicide", "Section 100", "Section 105", "IPC 299", "BNS 2023"])

    m("Under Section 137(2) of the BNS, the age limit for kidnapping from lawful guardianship remains 16 for males and 18 for females.",
      "false", "Bharatiya Nyaya Sanhita, 2023", "intermediate", "Bharatiya Nyaya Sanhita, 2023", "Section 137(2)", None,
      "Section 137(2) BNS eliminated the gender differential of the old IPC 361, establishing a uniform age of under eighteen years for both male and female minors.",
      "Under old IPC 361, the ages were 16 for males and 18 for females.",
      "Applies equally to all minors under eighteen years.",
      "remains 16 for males and 18 for females", "has been made uniform at under eighteen years of age for both genders",
      U_BNS, "Current Law (in force from July 1, 2024)", ["Kidnapping", "Section 137", "Minor Age", "Uniform Age 18", "BNS 2023"],
      {"oldAct": "IPC 1860", "oldSection": "361", "newAct": "BNS 2023", "newSection": "137(2)", "substantiveChange": "Age limit unified to under 18 years for both males and females (previously 16 for males)."})

    m("Trafficking of persons is penalized under Section 143 of the Bharatiya Nyaya Sanhita, 2023.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 143", None,
      "Section 143 BNS (corresponding to old IPC 370) penalizes recruitment, transportation, harbouring, transferring or receiving persons for exploitation by threats, force, abduction or fraud.",
      "Enhanced punishments apply for trafficking minors or multiple persons.",
      "Consent of the victim is immaterial where trafficking means are employed.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Trafficking", "Section 143", "Exploitation", "IPC 370", "BNS 2023"])

    m("Rape is defined under Section 63 and punished under Section 64 of the Bharatiya Nyaya Sanhita, 2023.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Sections 63 & 64", None,
      "Section 63 BNS defines rape (old IPC 375) across four enumerated physical acts without consent, and Section 64 prescribes rigorous imprisonment for not less than 10 years extending to life (old IPC 376).",
      "Moved from Section 375/376 IPC to Sections 63/64 BNS.",
      "Exception 2 retains the marital rape exemption for wives not under 18 years.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Rape Definition", "Section 63", "Section 64", "Punishment", "BNS 2023"])

    m("Gang rape of a woman under Section 70(1) of the BNS is punishable with rigorous imprisonment for a term of not less than twenty years, which may extend to life.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 70(1)", None,
      "Section 70(1) BNS (old IPC 376D) penalizes gang rape where one or more persons acting in furtherance of common intention commit rape, with minimum 20 years extending to life imprisonment.",
      "Section 70(2) punishes gang rape of a woman under eighteen years with life imprisonment or death.",
      "Each member is deemed guilty of gang rape.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Gang Rape", "Section 70", "Twenty Years Minimum", "IPC 376D", "BNS 2023"])

    m("Dowry death under Section 79 of the BNS requires that the death of a woman occur within ten years of her marriage.",
      "false", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 79", None,
      "Section 79 BNS (old IPC 304B) requires that the death occur within seven years of marriage under abnormal circumstances, with proof of cruelty or harassment in connection with demands for dowry soon before death.",
      "Candidates confuse 7 years (dowry death threshold) with 10 years (long-term matrimonial limitation).",
      "Section 85/86 covers ongoing cruelty beyond 7 years.",
      "occur within ten years of her marriage", "occur within seven years of her marriage",
      U_BNS, "Current Law (in force from July 1, 2024)", ["Dowry Death", "Section 79", "Seven Years", "Cruelty", "BNS 2023"],
      {"oldAct": "IPC 1860", "oldSection": "304B", "newAct": "BNS 2023", "newSection": "79", "substantiveChange": "Moved from IPC 304B to BNS 79; 7-year statutory period strictly maintained."})

    m("Cruelty by husband or relatives of husband is penalized under Section 85 of the Bharatiya Nyaya Sanhita, 2023.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 85", None,
      "Section 85 BNS (old IPC 498A) penalizes the husband or relative of the husband who subjects a woman to cruelty with imprisonment up to 3 years and fine.",
      "Section 86 BNS defines cruelty in detail, including physical injury and dowry harassment.",
      "Cruelty includes both mental and physical conduct driving the woman to suicide.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Cruelty", "Section 85", "Section 86", "IPC 498A", "BNS 2023"])

    m("Theft under Section 303(1) of the BNS requires moving movable property out of the possession of any person without that person's consent.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 303(1)", None,
      "Section 303(1) BNS (old IPC 378) defines theft: intending to take dishonestly any movable property out of the possession of any person without consent, and moving that property in order to such taking.",
      "Immovable property cannot be the subject of theft until severed from the earth.",
      "First-time offenders stealing property below 5,000 rupees can receive community service under Section 303(2) proviso.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Theft", "Section 303", "Movable Property", "Dishonest Taking", "BNS 2023"])

    m("Extortion under Section 308 of the BNS involves intentionally putting any person in fear of any injury and thereby dishonestly inducing delivery of property.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 308", None,
      "Section 308(1) BNS (old IPC 383) defines extortion. Unlike theft, extortion can apply to movable or immovable property, or valuable security.",
      "In extortion, delivery of property is obtained by coercion, whereas in theft it is taken without consent.",
      "Carries imprisonment up to 7 years depending on aggravation.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Extortion", "Section 308", "Fear of Injury", "Delivery of Property", "BNS 2023"])

    m("Robbery under Section 309 of the BNS is an aggravated form of either theft or extortion.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 309", None,
      "Section 309(1) BNS (old IPC 390) provides that in all robbery there is either theft or extortion, where the offender causes or attempts to cause death, hurt, or wrongful restraint.",
      "Every robbery is an aggravated theft or extortion.",
      "Robbery committed on a highway between sunset and sunrise carries up to 14 years imprisonment under Section 309(4).",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Robbery", "Section 309", "Aggravated Theft", "Highway Robbery", "BNS 2023"])

    m("The minimum number of persons required to commit Dacoity under Section 310 of the BNS is four.",
      "false", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 310", None,
      "Section 310(1) BNS (old IPC 391) mandates that when five or more persons conjointly commit or attempt to commit a robbery, every person so committing is guilty of dacoity. The minimum number is five, not four.",
      "If the group consists of 4 persons, it remains robbery under Section 309, not dacoity.",
      "All persons present and aiding are counted toward the threshold of five.",
      "The minimum number of persons required to commit Dacoity under Section 310 of the BNS is four", "Dacoity strictly requires five or more persons under Section 310",
      U_BNS, "Current Law (in force from July 1, 2024)", ["Dacoity", "Section 310", "Five Persons Minimum", "Robbery", "BNS 2023"])

    m("Criminal breach of trust under Section 316 of the BNS requires entrustment with property or dominion over property.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 316", None,
      "Section 316(1) BNS (old IPC 405) defines criminal breach of trust: whoever, being in any manner entrusted with property or dominion over property, dishonestly misappropriates or converts it to his own use.",
      "Entrustment is the sine qua non of criminal breach of trust, distinguishing it from simple criminal misappropriation (Sec 314).",
      "Enhanced punishments apply to carriers, clerks, servants, and public servants (Sections 316(3)-(5)).",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Criminal Breach of Trust", "Section 316", "Entrustment", "Misappropriation", "BNS 2023"])

    m("Cheating under Section 318 of the BNS requires fraudulent or dishonest inducement at the inception of the transaction.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 318", None,
      "Section 318(1) BNS (old IPC 415) defines cheating. For criminal liability under Section 318(4) (old IPC 420), dishonest intention must exist at the time of making the initial promise, not merely subsequent breach of contract (Hridaya Ranjan Pd. Verma).",
      "Mere civil breach of contract does not amount to cheating unless fraudulent inception is proven.",
      "Punishable under Section 318(4) with imprisonment up to 7 years and fine.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Cheating", "Section 318", "Dishonest Inducement", "IPC 420", "BNS 2023"])

    m("Forgery is defined under Section 336 of the Bharatiya Nyaya Sanhita, 2023.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 336", None,
      "Section 336 BNS (old IPC 463) defines forgery as the making of any false document or false electronic record with intent to cause damage or injury to the public or any person, or support any claim or title.",
      "Making a false document is defined in Section 335 BNS (old IPC 464).",
      "Punished under Section 336(2) with imprisonment up to 2 years or fine, or both.",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Forgery", "Section 336", "False Document", "Electronic Record", "BNS 2023"])

    m("Defamation under Section 356 of the BNS includes an option for community service as a statutory punishment.",
      "true", "Bharatiya Nyaya Sanhita, 2023", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 356(2)", None,
      "Section 356(2) BNS (old IPC 500) provides that whoever defames another may be punished with simple imprisonment up to 2 years, or with fine, or with both, or with community service.",
      "Under old IPC 500, community service was not a recognized statutory sentence.",
      "All ten classic exceptions to defamation are preserved in Section 356(1).",
      None, None,
      U_BNS, "Current Law (in force from July 1, 2024)", ["Defamation", "Section 356", "Community Service", "IPC 500", "BNS 2023"])

    # ---------------------------------------------------------
    # 3. HISTORICAL IPC VS BNS TRANSITIONS (30 items)
    # ---------------------------------------------------------
    m("The offence of murder, previously punished under Section 302 of the IPC, is now punished under Section 103 of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 103", None,
      "Old IPC Section 302 corresponds directly to Section 103 of the BNS, 2023.",
      "Lawyers commonly cite 302 out of habit; new FIRs register under Section 103 BNS.",
      "Section 103(1) governs ordinary murder; 103(2) governs mob lynching.",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 302", "BNS 103", "Murder", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "302", "newAct": "BNS 2023", "newSection": "103", "substantiveChange": "Punishment for murder relocated from IPC 302 to BNS 103."})

    m("Attempt to murder, historically governed by Section 307 of the IPC, is now governed by Section 109 of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 109", None,
      "Old IPC Section 307 corresponds directly to Section 109 of the BNS, 2023.",
      "Essential conversion for UP PCS-J candidates reading recent criminal appeals.",
      "Carries imprisonment up to 10 years, and if hurt is caused, up to life imprisonment.",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 307", "BNS 109", "Attempt to Murder", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "307", "newAct": "BNS 2023", "newSection": "109", "substantiveChange": "Attempt to murder relocated from IPC 307 to BNS 109."})

    m("The principal offence of rape, previously punished under Section 376 of the IPC, is now punished under Section 64 of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 64", None,
      "Section 376 IPC is now Section 64 of the BNS, 2023.",
      "Rape provisions are consolidated in Chapter V of BNS ('Offences Against Women and Children').",
      "Aggravated forms of rape are governed by Section 65 to 71 BNS.",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 376", "BNS 64", "Rape Punishment", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "376", "newAct": "BNS 2023", "newSection": "64", "substantiveChange": "Punishment for rape relocated from IPC 376 to BNS 64."})

    m("The offence of cheating and dishonestly inducing delivery of property (popularly known as '420') is now codified under Section 318(4) of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 318(4)", None,
      "Old IPC Section 420 is now Section 318(4) of the BNS, 2023.",
      "The colloquial cultural term 'char sau bees' ceases to correspond to the statutory section number.",
      "Carries imprisonment up to 7 years and fine.",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 420", "BNS 318(4)", "Cheating", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "420", "newAct": "BNS 2023", "newSection": "318(4)", "substantiveChange": "Cheating with delivery of property relocated from IPC 420 to BNS 318(4)."})

    m("Section 377 of the IPC (Unnatural Offences) has been reenacted with identical wording in the Bharatiya Nyaya Sanhita, 2023.",
      "false", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Omitted in BNS", None,
      "Section 377 IPC has been completely omitted from the BNS, 2023. Consensual adult same-sex relations were decriminalized in Navtej Johar (2018), and non-consensual acts on adults are dealt under relevant sexual assault provisions.",
      "Some assume the legislature preserved Section 377 for bestiality or male victims.",
      "Bestiality is not specifically codified in BNS.",
      "has been reenacted with identical wording in the Bharatiya Nyaya Sanhita, 2023", "has been completely omitted from the BNS, 2023",
      U_BNS, "Transition (July 1, 2024)", ["IPC 377", "Navtej Johar", "Omission", "Decriminalization", "BNS 2023"],
      {"oldAct": "IPC 1860", "oldSection": "377", "newAct": "BNS 2023", "newSection": "Omitted", "substantiveChange": "IPC Section 377 was omitted entirely from the BNS."})

    m("Common intention, previously found in Section 34 of the IPC, is now located in Section 3(5) of the Bharatiya Nyaya Sanhita, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 3(5)", None,
      "Old IPC Section 34 has been relocated to Section 3(5) of the BNS, 2023: 'When a criminal act is done by several persons in furtherance of the common intention of all, each of such persons is liable for that act in the same manner as if it were done by him alone.'",
      "Previously a separate standalone section; now a sub-clause in Section 3 BNS (General Explanations).",
      "Requires prior meeting of minds and active participation.",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 34", "BNS 3(5)", "Common Intention", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "34", "newAct": "BNS 2023", "newSection": "3(5)", "substantiveChange": "Joint liability for common intention relocated from IPC 34 to BNS 3(5)."})

    m("Every member of an unlawful assembly guilty of an offence committed in prosecution of common object, formerly IPC Section 149, is now governed by Section 190 of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 190", None,
      "Old IPC Section 149 corresponds directly to Section 190 of the BNS, 2023.",
      "Essential for framing charges in group violence trials.",
      "Creates vicarious criminal liability for all members of the unlawful assembly.",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 149", "BNS 190", "Common Object", "Unlawful Assembly", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "149", "newAct": "BNS 2023", "newSection": "190", "substantiveChange": "Constructive liability of unlawful assembly relocated from IPC 149 to BNS 190."})

    m("Voluntarily causing hurt, historically punished under Section 323 of the IPC, is now punished under Section 115(2) of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 115(2)", None,
      "Old IPC Section 323 corresponds directly to Section 115(2) of the BNS, 2023.",
      "Simple hurt is defined in Section 114 BNS (old IPC 319).",
      "Punishable with imprisonment up to 1 year or fine up to 1,000 rupees, or both.",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 323", "BNS 115(2)", "Simple Hurt", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "323", "newAct": "BNS 2023", "newSection": "115(2)", "substantiveChange": "Punishment for causing hurt relocated from IPC 323 to BNS 115(2)."})

    m("Voluntarily causing grievous hurt, formerly punished under Section 325 of the IPC, is now punished under Section 117(2) of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 117(2)", None,
      "Old IPC Section 325 is now Section 117(2) of the BNS, 2023. Grievous hurt definition (old IPC 320) is in Section 116 BNS.",
      "Grievous hurt retains the 8 classic statutory clauses.",
      "Punishable with imprisonment up to 7 years and fine.",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 325", "BNS 117(2)", "Grievous Hurt", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "325", "newAct": "BNS 2023", "newSection": "117(2)", "substantiveChange": "Punishment for grievous hurt relocated from IPC 325 to BNS 117(2)."})

    m("Assault or criminal force to a woman with intent to outrage her modesty, previously IPC Section 354, is now Section 74 of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 74", None,
      "Old IPC Section 354 corresponds directly to Section 74 of the BNS, 2023.",
      "Consolidated within Chapter V for crimes against women.",
      "Punishable with imprisonment of 1 to 5 years and fine.",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 354", "BNS 74", "Outraging Modesty", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "354", "newAct": "BNS 2023", "newSection": "74", "substantiveChange": "Outraging modesty of woman relocated from IPC 354 to BNS 74."})

    m("The offence of kidnapping, previously punished under Section 363 of the IPC, is now punished under Section 137(2) of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 137(2)", None,
      "Old IPC Section 363 corresponds to Section 137(2) of the BNS, 2023.",
      "Kidnapping from India is defined in Section 137(1)(a) and from lawful guardianship in 137(1)(b).",
      "Punished with imprisonment up to 7 years and fine.",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 363", "BNS 137(2)", "Kidnapping", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "363", "newAct": "BNS 2023", "newSection": "137(2)", "substantiveChange": "Punishment for kidnapping relocated from IPC 363 to BNS 137(2)."})

    m("The basic punishment for theft, previously under Section 379 of the IPC, is now provided under Section 303(2) of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 303(2)", None,
      "Old IPC Section 379 corresponds directly to Section 303(2) of the BNS, 2023.",
      "BNS 303(2) introduces a proviso allowing community service for first-time offenders where stolen value is under 5,000 rupees.",
      "General theft carries imprisonment up to 3 years, or fine, or both.",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 379", "BNS 303(2)", "Theft Punishment", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "379", "newAct": "BNS 2023", "newSection": "303(2)", "substantiveChange": "Theft punishment relocated from IPC 379 to BNS 303(2), adding community service option for petty theft."})

    m("Punishment for robbery, previously under Section 392 of the IPC, is now codified under Section 309(4) of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 309(4)", None,
      "Old IPC Section 392 corresponds directly to Section 309(4) of the BNS, 2023.",
      "Ordinary robbery carries rigorous imprisonment up to 10 years and fine; highway robbery at night up to 14 years.",
      "Attempt to commit robbery is in Section 309(5) BNS (old IPC 393).",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 392", "BNS 309(4)", "Robbery Punishment", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "392", "newAct": "BNS 2023", "newSection": "309(4)", "substantiveChange": "Robbery punishment relocated from IPC 392 to BNS 309(4)."})

    m("Punishment for dacoity, historically under Section 395 of the IPC, is now governed by Section 310(2) of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 310(2)", None,
      "Old IPC Section 395 corresponds directly to Section 310(2) of the BNS, 2023.",
      "Punishable with imprisonment for life or rigorous imprisonment up to 10 years, and fine.",
      "Dacoity with murder is governed by Section 310(3) BNS (old IPC 396).",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 395", "BNS 310(2)", "Dacoity Punishment", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "395", "newAct": "BNS 2023", "newSection": "310(2)", "substantiveChange": "Dacoity punishment relocated from IPC 395 to BNS 310(2)."})

    m("Punishment for criminal breach of trust, previously under Section 406 of the IPC, is now found in Section 316(2) of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 316(2)", None,
      "Old IPC Section 406 corresponds directly to Section 316(2) of the BNS, 2023.",
      "Carries imprisonment up to 5 years (raised from 3 years in IPC 406) or fine, or both.",
      "Aggravated forms follow in subsections (3)-(5).",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 406", "BNS 316(2)", "Criminal Breach of Trust", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "406", "newAct": "BNS 2023", "newSection": "316(2)", "substantiveChange": "Criminal breach of trust relocated from IPC 406 to BNS 316(2), increasing punishment to up to 5 years."})

    m("Dishonestly receiving stolen property, formerly Section 411 of the IPC, is now codified under Section 317(2) of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 317(2)", None,
      "Old IPC Section 411 corresponds directly to Section 317(2) of the BNS, 2023.",
      "Carries imprisonment up to 3 years, or fine, or both.",
      "Habitually dealing in stolen property is Section 317(4) BNS (old IPC 413).",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 411", "BNS 317(2)", "Stolen Property", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "411", "newAct": "BNS 2023", "newSection": "317(2)", "substantiveChange": "Receiving stolen property relocated from IPC 411 to BNS 317(2)."})

    m("Punishment for forgery, previously under Section 465 of the IPC, is now provided under Section 336(2) of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 336(2)", None,
      "Old IPC Section 465 corresponds directly to Section 336(2) of the BNS, 2023.",
      "Punishable with imprisonment up to 2 years, or fine, or both.",
      "Forgery of valuable security is governed by Section 338 BNS (old IPC 467).",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 465", "BNS 336(2)", "Forgery Punishment", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "465", "newAct": "BNS 2023", "newSection": "336(2)", "substantiveChange": "Forgery punishment relocated from IPC 465 to BNS 336(2)."})

    m("Criminal intimidation, formerly penalized under Section 506 of the IPC, is now governed by Section 351 of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 351", None,
      "Old IPC Section 506 is now Section 351(2) and 351(3) of the BNS, 2023.",
      "Definition and punishments are consolidated under Section 351.",
      "Threat to cause death or grievous hurt carries up to 7 years imprisonment.",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 506", "BNS 351", "Criminal Intimidation", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "506", "newAct": "BNS 2023", "newSection": "351", "substantiveChange": "Criminal intimidation relocated from IPC 506 to BNS 351."})

    m("Word, gesture or act intended to insult the modesty of a woman, previously IPC Section 509, is now Section 79 of the BNS, 2023.",
      "false", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 79 vs Section 75", None,
      "Section 79 BNS is Dowry Death (old IPC 304B). Word, gesture, or act insulting the modesty of a woman (old IPC 509) is codified under Section 75 of the BNS, 2023.",
      "A common pitfall because the number 79 was assigned to dowry death in BNS.",
      "Section 75 punishes insulting modesty with imprisonment up to 3 years and fine.",
      "is now Section 79 of the BNS, 2023", "is now codified under Section 75 of the BNS, 2023 (Section 79 governs dowry death)",
      U_BNS, "Transition (July 1, 2024)", ["IPC 509", "BNS 75", "BNS 79", "Insulting Modesty", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "509", "newAct": "BNS 2023", "newSection": "75", "substantiveChange": "Insulting modesty of woman moved from IPC 509 to BNS 75 (not Section 79)."})

    m("The general provision for punishing attempts to commit offences, previously Section 511 of the IPC, is now Section 62 of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 62", None,
      "Old IPC Section 511 corresponds directly to Section 62 of the BNS, 2023.",
      "Provides punishment of one-half of the longest term provided for the offence where no express attempt provision exists.",
      "Applicable to offences punishable with imprisonment.",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 511", "BNS 62", "Attempt to Commit Offence", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "511", "newAct": "BNS 2023", "newSection": "62", "substantiveChange": "General attempt provision relocated from IPC 511 to BNS 62."})

    m("The offence of Adultery, struck down by the Supreme Court in Joseph Shine (2018), has been re-introduced as a gender-neutral crime in the BNS, 2023.",
      "false", "Historical IPC vs BNS Transitions", "intermediate", "Bharatiya Nyaya Sanhita, 2023", "Omitted in BNS", None,
      "The legislature did not re-introduce the offence of adultery in the Bharatiya Nyaya Sanhita, 2023. It remains strictly a civil ground for divorce under matrimonial statutes.",
      "Parliamentary committees discussed reintroducing it, leading some to assume it was enacted.",
      "Remains a valid ground for divorce under the Hindu Marriage Act and Special Marriage Act.",
      "has been re-introduced as a gender-neutral crime in the BNS, 2023", "was omitted entirely from the BNS, 2023 in line with Joseph Shine",
      U_BNS, "Transition (July 1, 2024)", ["Adultery", "Joseph Shine", "Omission", "Decriminalization", "BNS 2023"],
      {"oldAct": "IPC 1860", "oldSection": "497", "newAct": "BNS 2023", "newSection": "Omitted", "substantiveChange": "Adultery was omitted entirely from the BNS following its unconstitutionality in Joseph Shine."})

    m("The archaic colonial offence of being a 'Thug' (old Section 310 IPC) has been retained in the Bharatiya Nyaya Sanhita, 2023.",
      "false", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Omitted in BNS", None,
      "Section 310 of the IPC (Thug) was an obsolete 19th-century colonial category and was completely omitted from the BNS, 2023.",
      "Some assume all IPC offences were retained with higher numbers.",
      "Organized gang robberies are now covered under Sections 111, 112, and 310 BNS.",
      "has been retained in the Bharatiya Nyaya Sanhita, 2023", "was completely omitted as obsolete colonial legislation from the BNS, 2023",
      U_BNS, "Transition (July 1, 2024)", ["Thug", "IPC 310", "Obsolete Law", "Omission", "BNS 2023"],
      {"oldAct": "IPC 1860", "oldSection": "310", "newAct": "BNS 2023", "newSection": "Omitted", "substantiveChange": "Colonial category of 'Thug' was omitted from the BNS."})

    m("Solitary confinement has been completely abolished as a form of sentence under the Bharatiya Nyaya Sanhita, 2023.",
      "false", "Historical IPC vs BNS Transitions", "intermediate", "Bharatiya Nyaya Sanhita, 2023", "Sections 11 & 12", None,
      "Sections 11 and 12 of the BNS, 2023 explicitly retain solitary confinement (corresponding to old IPC 73 and 74), subject to strict limits not exceeding 3 months in total and 14 days at a time.",
      "Many reformers advocated for its removal, leading aspirants to assume it was abolished.",
      "Strictly regulated under Section 12 BNS with intervals between confinement periods.",
      "has been completely abolished as a form of sentence under the Bharatiya Nyaya Sanhita, 2023", "is retained under Sections 11 and 12 of the BNS with strict statutory duration caps",
      U_BNS, "Transition (July 1, 2024)", ["Solitary Confinement", "Section 11", "Section 12", "IPC 73", "BNS 2023"],
      {"oldAct": "IPC 1860", "oldSection": "73", "newAct": "BNS 2023", "newSection": "11", "substantiveChange": "Solitary confinement was retained with identical statutory limitations."})

    m("The offence of buying or disposing of any person as a slave, previously IPC Section 370, has been replaced by comprehensive trafficking provisions in Section 143 BNS.",
      "true", "Historical IPC vs BNS Transitions", "intermediate", "Bharatiya Nyaya Sanhita, 2023", "Section 143", None,
      "Old IPC Section 370 (human trafficking) and 371 (habitual slave dealing) are comprehensively consolidated under Section 143 of the BNS, 2023.",
      "Reflects modern international anti-trafficking standards.",
      "Punishment extends to rigorous imprisonment for life.",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["Trafficking", "IPC 370", "BNS 143", "Slavery", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "370", "newAct": "BNS 2023", "newSection": "143", "substantiveChange": "Comprehensive trafficking provisions relocated from IPC 370 to BNS 143."})

    m("Dishonest misappropriation of property, formerly Section 403 of the IPC, is now governed by Section 314 of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 314", None,
      "Old IPC Section 403 corresponds directly to Section 314 of the BNS, 2023.",
      "Carries imprisonment up to 2 years, or fine, or both.",
      "Distinguished from theft because initial possession was lawful or innocent.",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 403", "BNS 314", "Misappropriation", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "403", "newAct": "BNS 2023", "newSection": "314", "substantiveChange": "Dishonest misappropriation relocated from IPC 403 to BNS 314."})

    m("Mischief, historically defined in Section 425 and punished in Section 426 of the IPC, is now defined in Section 324(1) and punished in Section 324(2) of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 324", None,
      "Old IPC Sections 425/426 correspond directly to Section 324 of the BNS, 2023.",
      "Mischief causing damage to public property carries enhanced penalties under subsections (3)-(5).",
      "Basic mischief carries imprisonment up to 6 months, or fine, or both.",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 425", "BNS 324", "Mischief", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "425", "newAct": "BNS 2023", "newSection": "324", "substantiveChange": "Mischief definition and punishment consolidated in BNS 324."})

    m("Criminal trespass and House-trespass, formerly Sections 441 and 442 of the IPC, are now codified under Section 329 of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 329", None,
      "Old IPC Sections 441/442 are now consolidated in Section 329 of the BNS, 2023.",
      "Consolidates entry into property in possession of another with intent to commit an offence.",
      "Lurking house-trespass and house-breaking follow in Section 331 BNS.",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 441", "BNS 329", "Criminal Trespass", "House Trespass", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "441", "newAct": "BNS 2023", "newSection": "329", "substantiveChange": "Criminal trespass and house trespass consolidated in BNS 329."})

    m("Fabricating false evidence, previously Section 192 of the IPC, is now Section 228 of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "intermediate", "Bharatiya Nyaya Sanhita, 2023", "Section 228", None,
      "Old IPC Section 192 corresponds directly to Section 228 of the BNS, 2023.",
      "Causing any circumstance to exist or making false entry in any book or record.",
      "Punished under Section 229 BNS.",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 192", "BNS 228", "Fabricating Evidence", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "192", "newAct": "BNS 2023", "newSection": "228", "substantiveChange": "Fabricating false evidence relocated from IPC 192 to BNS 228."})

    m("The offence of Defamation, formerly Section 499 of the IPC, is now codified under Section 356 of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 356", None,
      "Old IPC Section 499/500 corresponds to Section 356 of the BNS, 2023.",
      "Adds community service as an alternative punishment under Section 356(2).",
      "Retains all 10 statutory exceptions protecting public truth, criticism, and privilege.",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 499", "BNS 356", "Defamation", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "499", "newAct": "BNS 2023", "newSection": "356", "substantiveChange": "Defamation relocated from IPC 499 to BNS 356, adding community service."})

    m("Act of a person of unsound mind, historically IPC Section 84, is now located in Section 22 of the BNS, 2023.",
      "true", "Historical IPC vs BNS Transitions", "beginner", "Bharatiya Nyaya Sanhita, 2023", "Section 22", None,
      "Old IPC Section 84 corresponds directly to Section 22 of the BNS, 2023.",
      "Retains the core legal insanity test without textual deviation.",
      "General exception shielding from all criminal culpability.",
      None, None,
      U_BNS, "Transition (July 1, 2024)", ["IPC 84", "BNS 22", "Unsound Mind", "Statutory Transition"],
      {"oldAct": "IPC 1860", "oldSection": "84", "newAct": "BNS 2023", "newSection": "22", "substantiveChange": "Defence of unsound mind relocated from IPC 84 to BNS 22."})

    print("Part 1: 105 items registered.")
