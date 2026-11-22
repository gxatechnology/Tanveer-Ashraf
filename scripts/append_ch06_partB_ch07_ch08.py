"""
Appends Ch 6 Part B (25 MCQs), Ch 7 (30 MCQs), and Ch 8 (25 MCQs)
to scripts/build_mcqs_ch06_to_ch08.py
"""

with open('scripts/build_mcqs_ch06_to_ch08.py', 'a', encoding='utf-8') as f:
    f.write('''
# 06-31 to 06-40: Life, Liberty & Education (Arts 21, 21A, 22)
MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-031", "ch-06", "top-const-06-04",
    "In Maneka Gandhi v. Union of India (1978), the Supreme Court fundamentally reinterpreted Article 21 by holding that 'procedure established by law' must be:",
    ["Strictly literal and formal", "Just, fair, and reasonable, incorporating substantive due process principles", "Prescribed by an executive circular", "Approved by the Law Commission"],
    1,
    "In Maneka Gandhi (1978), a 7-Judge Bench overruled the narrow literalist doctrine of A.K. Gopalan (1950) and ruled that the procedure depriving a person of life or personal liberty under Article 21 must not be arbitrary, fanciful, or oppressive; it must be 'right and just and fair', importing the American concept of Substantive Due Process into Indian constitutional law.",
    {"A": "A.K. Gopalan literalism was overruled.", "B": "Correct. Procedure must be just, fair, and reasonable (substantive due process).", "C": "Executive circular cannot deprive liberty.", "D": "Law Commission has no statutory power."},
    "Easy", "Maneka Gandhi (1978) 1 SCC 248", "Master Maneka Gandhi Article 21 reinterpretation."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-032", "ch-06", "top-const-06-04",
    "Which three Articles constitute the famous 'Golden Triangle' of the Indian Constitution as established in Maneka Gandhi and Minerva Mills?",
    ["Articles 14, 19, and 21", "Articles 19, 20, and 21", "Articles 14, 15, and 16", "Articles 32, 226, and 136"],
    0,
    "Articles 14, 19, and 21 form the 'Golden Triangle' or holy trinity of the Indian Constitution. A law depriving personal liberty must simultaneously satisfy the equality test of Article 14, the reasonable restriction test of Article 19, and the fair procedure test of Article 21.",
    {"A": "Correct. Articles 14, 19, and 21.", "B": "Article 20 is not part of the triad name.", "C": "Articles 15 and 16 are species of Art. 14.", "D": "These are jurisdictional remedies."},
    "Easy", "Golden Triangle Doctrine", "Identify the three Golden Triangle articles."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-033", "ch-06", "top-const-06-04",
    "In K.S. Puttaswamy v. Union of India (2017), a unanimous 9-Judge Constitution Bench declared the 'Right to Privacy' to be:",
    ["A statutory right under the IT Act", "A Fundamental Right guaranteed under Article 21 and Part III of the Constitution", "A common law tort remedy only", "A directive principle under Part IV"],
    1,
    "In K.S. Puttaswamy (2017), the 9-Judge Bench unanimously held that the Right to Privacy is an intrinsic and inalienable part of the Right to Life and Personal Liberty under Article 21 and an overarching facet of the freedoms guaranteed in Part III, expressly overruling M.P. Sharma (1954) and Kharak Singh (1962).",
    {"A": "Privacy is fundamental, not merely statutory.", "B": "Correct. Fundamental Right under Article 21 and Part III.", "C": "Transcends tort law.", "D": "Enforceable fundamental right, not directive."},
    "Easy", "K.S. Puttaswamy (2017) 10 SCC 1", "Recall Puttaswamy Right to Privacy judgment."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-034", "ch-06", "top-const-06-04",
    "The Right to Free and Compulsory Education for all children aged 6 to 14 years was inserted as Article 21A by which Constitutional Amendment?",
    ["42nd Amendment Act, 1976", "44th Amendment Act, 1978", "86th Amendment Act, 2002", "93rd Amendment Act, 2005"],
    2,
    "The 86th Constitutional Amendment Act, 2002 inserted Article 21A, creating a Fundamental Right to free and compulsory education for all children between the ages of 6 and 14 years (giving effect to the landmark rulings in Mohini Jain 1992 and Unni Krishnan 1993).",
    {"A": "42nd Amendment transferred education to Concurrent List.", "B": "44th Amendment dealt with emergency and property.", "C": "Correct. 86th Amendment Act, 2002 inserted Article 21A.", "D": "93rd Amendment inserted Art. 15(5) reservations."},
    "Easy", "Article 21A & 86th Amendment", "Recall 86th Amendment Article 21A."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-035", "ch-06", "top-const-06-04",
    "In Common Cause v. Union of India (2018), the Supreme Court recognized which aspect of personal liberty under Article 21?",
    ["Right to unrestricted active euthanasia", "Right to die with dignity, including the validity of passive euthanasia and Living Wills (Advance Medical Directives)", "Right to commit suicide under Section 309 IPC", "Right to decline state vaccination"],
    1,
    "In Common Cause (2018), a 5-Judge Constitution Bench held that the right to die with dignity is an inseparable facet of the Right to Life under Article 21; the Court legalized passive euthanasia and gave legal sanction to Advance Medical Directives ('Living Wills').",
    {"A": "Active euthanasia remains illegal.", "B": "Correct. Passive euthanasia and Living Wills recognized.", "C": "Suicide is not a constitutional right (Gian Kaur 1996).", "D": "Compulsory vaccination is a valid public health measure."},
    "Medium", "Common Cause v. UOI (2018) 5 SCC 1", "Identify euthanasia doctrine under Article 21."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-036", "ch-06", "top-const-06-04",
    "Under Article 22(2), every person arrested and detained in custody must be produced before the nearest magistrate within what time period?",
    ["12 hours", "24 hours excluding the time necessary for the journey", "48 hours", "7 days"],
    1,
    "Article 22(2) provides: 'Every person who is arrested and detained in custody shall be produced before the nearest magistrate within a period of twenty-four hours of such arrest excluding the time necessary for the journey from the place of arrest to the court of the magistrate'.",
    {"A": "12 hours is incorrect.", "B": "Correct. 24 hours excluding journey time.", "C": "48 hours is incorrect.", "D": "7 days is incorrect."},
    "Easy", "Article 22(2)", "Recall 24-hour production rule before magistrate."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-037", "ch-06", "top-const-06-04",
    "Which of the following protections of Article 22(1) and (2) does NOT apply to an enemy alien or a person detained under preventive detention?",
    ["Right to be informed of grounds of arrest as soon as may be", "Right to consult and be defended by a legal practitioner", "Right to be produced before magistrate within 24 hours", "All of the above protections"],
    3,
    "Article 22(3) explicitly states that clauses (1) and (2) (right to be informed of grounds, right to counsel, and production before magistrate within 24 hours) do NOT apply to: (a) any person who for the time being is an enemy alien; or (b) any person who is arrested or detained under any law providing for preventive detention.",
    {"A": "Clause (1) protection denied by 22(3).", "B": "Clause (1) protection denied by 22(3).", "C": "Clause (2) protection denied by 22(3).", "D": "Correct. All of the above protections are excluded under Article 22(3)."},
    "Medium", "Article 22(3)", "Examine exclusions under Article 22(3)."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-038", "ch-06", "top-const-06-04",
    "In D.K. Basu v. State of West Bengal (1997), the Supreme Court laid down mandatory guidelines regarding:",
    ["Arrest, detention, and prevention of custodial violence", "Medical college admissions", "Air pollution in Delhi", "Appointment of judges"],
    0,
    "In D.K. Basu (1997), the Supreme Court laid down 11 mandatory procedural requirements to be followed by police authorities during arrest and detention to eliminate custodial deaths, torture, and third-degree methods.",
    {"A": "Correct. Mandatory arrest and custodial violence guidelines.", "B": "T.M.A. Pai dealt with admissions.", "C": "M.C. Mehta dealt with pollution.", "D": "Second Judges case dealt with judges."},
    "Easy", "D.K. Basu (1997) 1 SCC 416", "Recall D.K. Basu arrest guidelines."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-039", "ch-06", "top-const-06-04",
    "Under Article 22(4), what is the maximum period for which a person can normally be detained under preventive detention without obtaining the opinion of an Advisory Board?",
    ["One month", "Two months", "Three months", "Six months"],
    2,
    "Under Article 22(4) as it currently stands in practice, no preventive detention law can authorize detention for longer than THREE MONTHS unless an Advisory Board consisting of persons qualified to be High Court judges reports sufficient cause before the expiration of that period.",
    {"A": "One month is incorrect.", "B": "Two months was proposed by 44th Amendment s. 3, but never brought into force by notification.", "C": "Correct. Three months is the applicable constitutional duration.", "D": "Six months is incorrect."},
    "Medium", "Article 22(4)", "Recall 3-month maximum preventive detention window."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-040", "ch-06", "top-const-06-04",
    "In Hussainara Khatoon v. Home Secretary, State of Bihar (1979), the Supreme Court derived which fundamental right under Article 21 for undertrial prisoners?",
    ["Right to Free Legal Aid and Speedy Trial", "Right to choose judges", "Right to private air-conditioned cells", "Right to parole every month"],
    0,
    "In the landmark Hussainara Khatoon series (1979), Justice P.N. Bhagwati read the 'Right to a Speedy Trial' and 'Right to Free Legal Aid' as implicit fundamental rights under Article 21, ordering the release of tens of thousands of undertrial prisoners who had been incarcerated longer than the maximum sentence for their alleged offences.",
    {"A": "Correct. Right to Free Legal Aid and Speedy Trial.", "B": "Bench selection is CJI master of roster power.", "C": "Frivolous option.", "D": "Parole is statutory discretion."},
    "Medium", "Hussainara Khatoon (1980) 1 SCC 81", "Identify speedy trial and legal aid under Art. 21."
))

# 06-41 to 06-50: Exploitation & Religion (Arts 23–28)
MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-041", "ch-06", "top-const-06-05",
    "In People's Union for Democratic Rights (PUDR) v. Union of India (Asiad Workers Case, 1982), the Supreme Court held that paying less than the statutory minimum wage constitutes:",
    ["Breach of contract only", "'Forced Labour' (Begar) violating Article 23", "Unfair trade practice", "Mere moral delinquency"],
    1,
    "In PUDR (Asiad Workers Case 1982), Justice Bhagwati ruled that 'force' in Article 23 is not restricted to physical compulsion; paying less than the minimum wage to workers who have no choice due to economic necessity constitutes 'forced labour' within the prohibition of Article 23.",
    {"A": "Transcends contract law to constitutional violation.", "B": "Correct. Constitutes 'forced labour' violating Article 23.", "C": "Not merely trade practice.", "D": "Constitutional offence."},
    "Medium", "PUDR v. Union of India (1982) 3 SCC 235", "Master Article 23 forced labour definition in PUDR."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-042", "ch-06", "top-const-06-05",
    "Article 24 of the Constitution prohibits the employment of children below what age in any factory, mine, or hazardous occupation?",
    ["Below 12 years", "Below 14 years", "Below 16 years", "Below 18 years"],
    1,
    "Article 24 provides: 'No child below the age of fourteen years shall be employed to work in any factory or mine or engaged in any other hazardous employment'.",
    {"A": "12 years is incorrect.", "B": "Correct. Below fourteen (14) years.", "C": "16 years is incorrect.", "D": "18 years is definition of child in POCSO/JJ Act, but Art. 24 specifies 14 years."},
    "Easy", "Article 24", "Recall Article 24 age threshold."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-043", "ch-06", "top-const-06-05",
    "Under Article 25(1), the Freedom of Conscience and the Right to profess, practise, and propagate religion is subject to:",
    ["Public order, morality and health, and other provisions of Part III", "Security of the State only", "Absolute executive discretion", "International covenants"],
    0,
    "Article 25(1) begins with express limitations: 'Subject to public order, morality and health and to the other provisions of this Part, all persons are equally entitled to freedom of conscience and the right freely to profess, practise and propagate religion'.",
    {"A": "Correct. Public order, morality, health, and other Part III rights.", "B": "Security of State is Art. 19(2), not Art. 25(1).", "C": "Discretion is bounded by law.", "D": "Constitution is primary."},
    "Easy", "Article 25(1)", "Recall the limitations on Article 25(1)."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-044", "ch-06", "top-const-06-05",
    "In Rev. Stanislaus v. State of Madhya Pradesh (1977), a 5-Judge Constitution Bench held that the right to 'propagate' religion under Article 25:",
    ["Includes a fundamental right to convert another person to one's own religion", "Does NOT include the right to convert another person, but only to transmit or spread one's religion by exposition of its tenets", "Permits conversion by economic inducement", "Is restricted only to minority religions"],
    1,
    "In Rev. Stanislaus (1977), Chief Justice A.N. Ray held that what Article 25 grants is not the right to convert another person, but the right to propagate one's religion by expounding its doctrines. If a person converts another by force or fraud, it impinges on the 'freedom of conscience' of the convert.",
    {"A": "Right to convert was explicitly rejected.", "B": "Correct. Does NOT include right to convert; only right to spread tenets.", "C": "Inducement is prohibited by anti-conversion laws.", "D": "Applies to all persons."},
    "Hard", "Rev. Stanislaus, AIR 1977 SC 908", "Master Stanislaus conversion doctrine."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-045", "ch-06", "top-const-06-05",
    "Under the 'Essential Religious Practices Test' formulated in the Shirur Mutt Case (1954), who decides whether a practice is an essential religious practice?",
    ["The political party in power", "The courts, with reference to the doctrines and scriptures of that religion", "The local district collector", "The United Nations Human Rights Council"],
    1,
    "In Commr., Hindu Religious Endowments v. Sri Lakshmindra Thirtha Swamiar (Shirur Mutt Case 1954), the 7-Judge Bench held that what constitutes the essential part of a religion is primarily to be ascertained with reference to the doctrines of that religion itself by the courts.",
    {"A": "Executive cannot decide religion.", "B": "Correct. Courts decide with reference to doctrines of the religion.", "C": "District collector has no ecclesiastical power.", "D": "UN has no internal role."},
    "Medium", "Shirur Mutt Case, AIR 1954 SC 282", "Explain Essential Religious Practices test."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-046", "ch-06", "top-const-06-05",
    "In Indian Young Lawyers Association v. State of Kerala (Sabarimala Case, 2018), the Supreme Court struck down the exclusion of women aged 10 to 50 from entering Sabarimala Temple because:",
    ["It violated Articles 14, 15, and 21, and did not constitute an essential religious practice under Article 25", "The temple was built on government land", "Women paid higher taxes", "The deity had no legal personality"],
    0,
    "In the Sabarimala Case (2018), the 4:1 majority held that biological factors (menstruation) cannot be a basis for discrimination under Articles 14 and 15; patriarchal notions of purity violate women's dignity under Article 21 and the practice is not an essential religious practice.",
    {"A": "Correct. Violated equality, dignity, and not an essential religious practice.", "B": "Land ownership was not the ground.", "C": "Taxation is irrelevant.", "D": "Deities do have juristic personality in Hindu law."},
    "Medium", "Sabarimala Case (2019) 11 SCC 1", "Recall Sabarimala judgment reasoning."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-047", "ch-06", "top-const-06-05",
    "Under Article 26, every religious denomination or any section thereof has the right to:",
    ["Establish and maintain institutions for religious and charitable purposes, and manage its own affairs in matters of religion", "Wage holy war against other groups", "Refuse to pay municipal property taxes", "Enforce religious dogma in state courts"],
    0,
    "Article 26 guarantees to every religious denomination the corporate right to: (a) establish and maintain religious/charitable institutions; (b) manage its own affairs in matters of religion; (c) own and acquire movable and immovable property; and (d) administer such property in accordance with law.",
    {"A": "Correct. Four denominational rights under Article 26.", "B": "Strictly illegal.", "C": "Property must be administered according to law.", "D": "Courts enforce secular law."},
    "Easy", "Article 26", "Recall collective religious rights under Article 26."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-048", "ch-06", "top-const-06-05",
    "Article 27 of the Constitution prohibits:",
    ["The levy of any fee for maintenance of temples", "The compulsion to pay any taxes the proceeds of which are specifically appropriated in payment of expenses for the promotion of any particular religion", "Donations to religious charitable trusts", "Religious pilgrimage subsidies"],
    1,
    "Article 27 prohibits the State from compelling any citizen to pay TAXES where proceeds are specifically earmarked for promoting or maintaining any particular religion or religious denomination. It prohibits 'taxes', not 'fees' for secular services (Shirur Mutt Case).",
    {"A": "Fees for regulation/secular services are valid.", "B": "Correct. Prohibits taxes earmarked for promoting a particular religion.", "C": "Voluntary donations are valid.", "D": "General non-discriminatory subsidies are valid (Prafull Goradia)."},
    "Medium", "Article 27", "Distinguish tax prohibition from fees in Article 27."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-049", "ch-06", "top-const-06-05",
    "Under Article 28, in which category of educational institutions is religious instruction completely prohibited?",
    ["Institutions wholly maintained out of State funds", "Institutions administered by State under a trust requiring religious instruction", "Institutions recognized by the State", "Institutions receiving aid out of State funds"],
    0,
    "Article 28(1) provides: 'No religious instruction shall be provided in any educational institution wholly maintained out of State funds'. In trust institutions administered by State (Art. 28(2)), it is permitted; in aided/recognized schools (Art. 28(3)), it requires consent.",
    {"A": "Correct. Wholly maintained out of State funds = Total prohibition.", "B": "Trust schools are exempt under Art. 28(2).", "C": "Recognized schools require voluntary consent under Art. 28(3).", "D": "Aided schools require voluntary consent under Art. 28(3)."},
    "Hard", "Article 28(1)", "Master classification of institutions under Article 28."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-050", "ch-06", "top-const-06-05",
    "Wearing and carrying of 'Kirpans' is deemed to be included in the profession of the Sikh religion under which constitutional provision?",
    ["Explanation I to Article 25", "Explanation II to Article 25", "Article 26(b)", "Article 19(1)(b)"],
    0,
    "Explanation I to Article 25 explicitly provides: 'The wearing and carrying of kirpans shall be deemed to be included in the profession of the Sikh religion'. Explanation II states that reference to Hindus includes Sikhs, Jains, and Buddhists.",
    {"A": "Correct. Explanation I to Article 25.", "B": "Explanation II deals with Hindu definition.", "C": "Article 26(b) is managing religious affairs.", "D": "Article 19(1)(b) is peaceful assembly without arms."},
    "Easy", "Article 25, Explanation I", "Recall Explanation I to Article 25."
))

# 06-51 to 06-55: Cultural & Remedies (Arts 29–32)
MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-051", "ch-06", "top-const-06-06",
    "Under Article 30(1), which categories of minorities have the fundamental right to establish and administer educational institutions of their choice?",
    ["Linguistic and Religious minorities only", "Racial and Ethnic minorities", "Economic and Political minorities", "Caste and Class minorities"],
    0,
    "Article 30(1) states: 'All minorities, whether based on religion or language, shall have the right to establish and administer educational institutions of their choice'. The Indian Constitution recognizes ONLY two types of minorities: Religious and Linguistic.",
    {"A": "Correct. Religious and Linguistic minorities only.", "B": "Ethnic/racial minorities not recognized under Art. 30.", "C": "Economic minorities not recognized under Art. 30.", "D": "Caste is covered under Art. 15/16, not Art. 30."},
    "Easy", "Article 30(1)", "Recall the two types of minorities recognized in Article 30."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-052", "ch-06", "top-const-06-06",
    "In T.M.A. Pai Foundation v. State of Karnataka (2002), an 11-Judge Constitution Bench settled that the unit for determining religious or linguistic minority status is:",
    ["The entire nation of India", "The concerned State", "The concerned district or taluk", "The municipal ward"],
    1,
    "In T.M.A. Pai (2002), the 11-Judge Bench held that since reorganization of States in India was conducted on linguistic lines, the unit for determining whether a community is a linguistic or religious minority under Article 30 is the STATE, and not the whole of India.",
    {"A": "National level rejected in T.M.A. Pai.", "B": "Correct. The State is the unit for minority determination.", "C": "District level rejected.", "D": "Municipal level rejected."},
    "Medium", "T.M.A. Pai Foundation (2002) 8 SCC 481", "Master T.M.A. Pai minority determination unit."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-053", "ch-06", "top-const-06-06",
    "Why did Dr. B.R. Ambedkar describe Article 32 as the 'Heart and Soul' of the Constitution?",
    ["Because it confers voting rights", "Because an article without which the Constitution would be a nullity is Article 32, guaranteeing direct judicial remedy to the Supreme Court for breach of Fundamental Rights", "Because it creates the post of Prime Minister", "Because it establishes the Supreme Court"],
    1,
    "Dr. Ambedkar famously declared in the Constituent Assembly: 'If I was asked to name any particular article in this Constitution as the most important—an article without which this Constitution would be a nullity—I could not refer to any other article except this one. It is the very soul of the Constitution and the very heart of it'.",
    {"A": "Voting rights are Article 326.", "B": "Correct. Direct constitutional remedy making rights enforceable.", "C": "Prime Minister is Article 74/75.", "D": "Supreme Court establishment is Article 124."},
    "Easy", "Article 32 Philosophy", "Explain Ambedkar's 'Heart and Soul' quote."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-054", "ch-06", "top-const-06-06",
    "Which prerogative writ literally means 'We Command' and is issued to compel a public official or authority to perform a mandatory statutory duty?",
    ["Habeas Corpus", "Mandamus", "Certiorari", "Quo Warranto"],
    1,
    "Mandamus (Latin for 'We Command') is a prerogative order issued by a superior court commanding a public officer, inferior court, tribunal, or government to perform a mandatory public or statutory duty which they have refused or failed to perform.",
    {"A": "Habeas Corpus means 'to have the body' (illegal detention).", "B": "Correct. Mandamus means 'We Command'.", "C": "Certiorari means 'to be certified' (quashing judicial errors).", "D": "Quo Warranto means 'by what authority' (public office usurper)."},
    "Easy", "Prerogative Writs: Mandamus", "Define writ of Mandamus."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-055", "ch-06", "top-const-06-06",
    "Which prerogative writ is issued to inquire into the legality of the claim which a person asserts to a public office and to oust him if unlawfully usurped?",
    ["Habeas Corpus", "Prohibition", "Certiorari", "Quo Warranto"],
    3,
    "Quo Warranto (literally 'By what warrant or authority') is issued against a usurper of a substantive public office of a permanent character created by statute or Constitution, challenging his legal title and ousting him if unqualified.",
    {"A": "Habeas Corpus tests physical liberty.", "B": "Prohibition stops lower court mid-trial.", "C": "Certiorari quashes concluded lower court order.", "D": "Correct. Quo Warranto tests title to public office."},
    "Easy", "Prerogative Writs: Quo Warranto", "Define writ of Quo Warranto."
))

print(f"Chapter 6 complete ({len(MCQS_CH06_08)} total).")

# ==============================================================================
# CHAPTER 7: DIRECTIVE PRINCIPLES OF STATE POLICY (30 MCQs)
# ==============================================================================
# 07-01 to 07-10: Genesis, Nature & Justiciability (Arts 36–37)
MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-001", "ch-07", "top-const-07-01",
    "Under Article 37, the Directive Principles of State Policy are:",
    ["Justiciable and enforceable by any High Court or Supreme Court", "Non-justiciable in courts of law, but fundamental in the governance of the country", "Subordinate to executive circulars", "Applicable only to Union territories"],
    1,
    "Article 37 explicitly declares: 'The provisions contained in this Part shall not be enforceable by any court, but the principles therein laid down are nevertheless fundamental in the governance of the country and it shall be the duty of the State to apply these principles in making laws'.",
    {"A": "Non-justiciability is expressly mandated by Art. 37.", "B": "Correct. Non-justiciable, but fundamental in governance.", "C": "Supersede executive circulars.", "D": "Apply throughout India."},
    "Easy", "Article 37", "Recall Article 37 foundational rule."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-002", "ch-07", "top-const-07-01",
    "The definition of 'State' for the purposes of Part IV (DPSP) under Article 36 is:",
    ["Identical to the definition in Article 12 (Part III)", "Narrower than Article 12, excluding local authorities", "Wider than Article 12, including private corporations", "Defined independently in Article 366"],
    0,
    "Article 36 provides: 'In this Part, unless the context otherwise requires, \"the State\" has the same meaning as in Part III'. Hence, the four categories of Article 12 apply identically to Directive Principles.",
    {"A": "Correct. Article 36 adopts Article 12 definition.", "B": "Local authorities are included.", "C": "Private corporations are not included.", "D": "Not in Art. 366."},
    "Easy", "Article 36", "Connect Article 36 to Article 12 definition."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-003", "ch-07", "top-const-07-01",
    "The Instrument of Instructions contained in the Government of India Act, 1935 was incorporated into the Constitution of 1950 as:",
    ["Fundamental Rights", "Directive Principles of State Policy", "Fundamental Duties", "Emergency Provisions"],
    1,
    "Dr. B.R. Ambedkar noted that the Directive Principles of State Policy are like the 'Instrument of Instructions' issued to the Governor-General and Governors by the British Government under the Government of India Act, 1935, with the difference that they are addressed to the legislature and executive of a democratic republic.",
    {"A": "FRs are negative civil rights.", "B": "Correct. DPSP embodies Instrument of Instructions.", "C": "Duties were added in 1976.", "D": "Emergency provisions are in Part XVIII."},
    "Medium", "DPSP Historical Blueprints", "Connect DPSP to 1935 Instrument of Instructions."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-004", "ch-07", "top-const-07-01",
    "Which legal philosopher's distinction between 'justiciable rights' and 'non-justiciable directives' influenced Sir B.N. Rau to bifurcate rights into Part III and Part IV?",
    ["A.V. Dicey", "Sir Ivor Jennings", "Sir B.N. Rau citing the Irish jurist Sir James Fitzjames Stephen / Irish precedent", "John Locke"],
    2,
    "The Drafting Committee, guided by Constitutional Adviser Sir B.N. Rau, drew inspiration from the Irish Constitution of 1937 which bifurcated rights into justiciable fundamental rights and non-justiciable directive principles of social policy.",
    {"A": "Dicey focused on Rule of Law.", "B": "Jennings criticized length.", "C": "Correct. Irish precedent of bifurcating rights into enforceable and non-enforceable.", "D": "Locke focused on natural rights."},
    "Medium", "Constituent Assembly Historical Drafting", "Recall reason for bifurcating Part III and Part IV."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-005", "ch-07", "top-const-07-01",
    "Can a court issue a writ of Mandamus compelling the State to enact a law to implement a Directive Principle?",
    ["Yes, under Article 32", "No, in State of Himachal Pradesh v. A Parent of a Student (1985), the Supreme Court held that courts cannot issue a mandamus to legislate on DPSP", "Yes, under Article 226", "Yes, upon a public interest litigation"],
    1,
    "In State of H.P. v. A Parent of a Student (1985) and Asif Hameed v. State of J&K (1989), the Supreme Court settled that courts cannot issue a writ of mandamus to the legislature or executive to enact or initiate legislation to implement Directive Principles under Part IV.",
    {"A": "Article 32 cannot enforce Part IV.", "B": "Correct. Courts cannot compel the legislature to enact DPSP laws.", "C": "Article 226 cannot issue mandamus to legislate.", "D": "PIL cannot override Art. 37."},
    "Medium", "State of H.P. (1985) 3 SCC 169", "Affirm rule against mandamus to legislate DPSP."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-006", "ch-07", "top-const-07-01",
    "Can a law be declared unconstitutional solely on the ground that it fails to implement or violates a Directive Principle of State Policy?",
    ["Yes, because DPSP are fundamental in governance", "No, because DPSP are non-justiciable under Article 37", "Yes, if challenged by a registered trade union", "Yes, by a 7-Judge Bench only"],
    1,
    "In Deep Chand v. State of U.P. (1959), the Supreme Court ruled that a law cannot be struck down merely because it is contrary to or fails to give effect to a Directive Principle, since DPSP are non-enforceable under Article 37.",
    {"A": "Fundamental in governance does not mean enforceable in court.", "B": "Correct. Non-justiciability bars striking down laws on DPSP breach alone.", "C": "Trade unions cannot enforce DPSP.", "D": "Bench size does not alter Article 37."},
    "Medium", "Article 37 Enforceability Limits", "Differentiate fundamental in governance from justiciability."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-007", "ch-07", "top-const-07-01",
    "What is the primary judicial role of Directive Principles in constitutional adjudication?",
    ["They serve as an interpretive tool to determine the 'reasonableness' of restrictions under Article 19 and public purpose under Article 14", "They automatically override Fundamental Rights", "They allow the President to suspend statutes", "They permit the Governor to issue decrees"],
    0,
    "In State of Bombay v. F.N. Balsara (1951) and Kasturi Lal v. State of J&K (1980), the Supreme Court established that Directive Principles serve as an authoritative benchmark for determining whether a restriction on fundamental rights under Article 19 is 'reasonable' and whether state action is in the 'public interest'.",
    {"A": "Correct. Benchmark for testing 'reasonableness' of restrictions under Art. 19.", "B": "Cannot automatically override FRs.", "C": "President has no statutory suspension power.", "D": "Governor cannot issue decrees."},
    "Medium", "Interpretive Role of DPSP", "Master role of DPSP in interpreting reasonableness."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-008", "ch-07", "top-const-07-01",
    "Who called the Directive Principles of State Policy a 'Cheque on a bank, payable only when the resources of the bank permit'?",
    ["Prof. K.T. Shah", "Dr. B.R. Ambedkar", "K.M. Munshi", "T.T. Krishnamachari"],
    0,
    "Prof. K.T. Shah famously criticized the non-justiciable character of DPSP in the Constituent Assembly by remarking: 'It is like a cheque on a bank, payable only when the resources of the bank permit'.",
    {"A": "Correct. Prof. K.T. Shah.", "B": "Ambedkar defended them as economic democracy.", "C": "Munshi called Preamble political horoscope.", "D": "Krishnamachari called DPSP a dustbin of sentiments."},
    "Easy", "Constituent Assembly Quotes on DPSP", "Recall Prof. K.T. Shah's famous cheque critique."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-009", "ch-07", "top-const-07-01",
    "Who described the Directive Principles of State Policy as a 'Veritable dustbin of sentiments'?",
    ["T.T. Krishnamachari", "Sir Ivor Jennings", "K.C. Wheare", "Granville Austin"],
    0,
    "T.T. Krishnamachari, a member of the Drafting Committee, skeptically referred to the Directive Principles as a 'veritable dustbin of sentiments' during the assembly debates.",
    {"A": "Correct. T.T. Krishnamachari.", "B": "Sir Ivor Jennings criticized them as pious aspirations.", "C": "Wheare focused on quasi-federalism.", "D": "Austin called them conscience of the constitution."},
    "Medium", "Constituent Assembly Debates on DPSP", "Recall T.T. Krishnamachari's critique."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-010", "ch-07", "top-const-07-01",
    "The ultimate sanction behind the Directive Principles of State Policy, as identified by Dr. B.R. Ambedkar, is:",
    ["Contempt of court", "Political sanction and public opinion through regular elections", "Presidential dismissal", "Financial audit by CAG"],
    1,
    "Dr. Ambedkar declared that the real sanction behind the Directive Principles is political, not judicial: 'A government which rests on popular votes can hardly ignore the Directive Principles while shaping its policy. If any government ignores them, it will certainly have to answer for them before the electorate at the election time'.",
    {"A": "Contempt is judicial sanction, not applicable to DPSP.", "B": "Correct. Political sanction of the electorate at elections.", "C": "President does not dismiss governments on DPSP grounds.", "D": "CAG audits finances."},
    "Easy", "Dr. Ambedkar's Speech on DPSP", "Identify political sanction behind DPSP."
))

# 07-11 to 07-20: Substantive Classification (Arts 38–51)
MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-011", "ch-07", "top-const-07-02",
    "Article 39A providing for 'Equal justice and free legal aid' was inserted by which Constitutional Amendment?",
    ["25th Amendment Act, 1971", "42nd Amendment Act, 1976", "44th Amendment Act, 1978", "86th Amendment Act, 2002"],
    1,
    "Article 39A was added by the 42nd Constitutional Amendment Act, 1976, directing the State to ensure equal justice and provide free legal aid by suitable legislation, which led to the enactment of the Legal Services Authorities Act, 1987.",
    {"A": "25th Amendment inserted Article 31C.", "B": "Correct. 42nd Amendment Act, 1976 added Article 39A.", "C": "44th Amendment inserted Art. 38(2).", "D": "86th Amendment amended Art. 45."},
    "Easy", "Article 39A & 42nd Amendment", "Identify 42nd Amendment origin of Article 39A."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-012", "ch-07", "top-const-07-02",
    "Which Article of the Constitution directs the State to take steps to organise 'Village Panchayats' as units of self-government?",
    ["Article 39", "Article 40", "Article 43", "Article 48"],
    1,
    "Article 40 of the Constitution (a Gandhian principle) provides: 'The State shall take steps to organise village panchayats and endow them with such powers and authority as may be necessary to enable them to function as units of self-government'.",
    {"A": "Article 39 is principles of policy.", "B": "Correct. Article 40 directs organisation of Village Panchayats.", "C": "Article 43 is living wage.", "D": "Article 48 is agriculture and animal husbandry."},
    "Easy", "Article 40", "Recall Article 40 Village Panchayats."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-013", "ch-07", "top-const-07-02",
    "Article 44 of the Constitution contains the directive regarding:",
    ["Uniform Civil Code for the citizens throughout the territory of India", "Separation of judiciary from the executive", "Promotion of international peace and security", "Protection of monuments of national importance"],
    0,
    "Article 44 provides: 'The State shall endeavour to secure for the citizens a Uniform Civil Code throughout the territory of India'.",
    {"A": "Correct. Article 44 directs securing a Uniform Civil Code.", "B": "Separation of judiciary is Article 50.", "C": "International peace is Article 51.", "D": "Monuments protection is Article 49."},
    "Easy", "Article 44", "Recall Article 44 Uniform Civil Code."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-014", "ch-07", "top-const-07-02",
    "Which landmark judgment emphasized the urgent necessity of enacting a Uniform Civil Code under Article 44 to remove gender disparities in maintenance?",
    ["Mohd. Ahmed Khan v. Shah Bano Begum (1985)", "Sarla Mudgal v. Union of India (1995)", "Shayara Bano v. Union of India (2017)", "All of the above landmark judgments"],
    3,
    "In Shah Bano (1985), Sarla Mudgal (1995), John Vallamattom (2003), and Shayara Bano (2017), the Supreme Court repeatedly called upon the legislature to give effect to Article 44 to protect women against discriminatory personal laws.",
    {"A": "Shah Bano urged UCC enactment.", "B": "Sarla Mudgal urged UCC on fraudulent conversions.", "C": "Shayara Bano struck down triple talaq.", "D": "Correct. All of the above judgments urged Article 44 implementation."},
    "Medium", "Article 44 Jurisprudence", "Connect UCC to landmark Supreme Court cases."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-015", "ch-07", "top-const-07-02",
    "Article 50 of the Constitution directs the State to:",
    ["Separate the Judiciary from the Executive in the public services of the State", "Separate the military from civil administration", "Abolish the death penalty", "Separate religion from state politics"],
    0,
    "Article 50 states: 'The State shall take steps to separate the judiciary from the executive in the public services of the State', ensuring that judicial magistrates are completely detached from executive control.",
    {"A": "Correct. Separate Judiciary from Executive.", "B": "Military separation is an inherent civil control.", "C": "Death penalty is not abolished.", "D": "Secularism is spread across Part III."},
    "Easy", "Article 50", "Recall Article 50 Separation of Judiciary."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-016", "ch-07", "top-const-07-02",
    "Article 48A directing the State to 'protect and improve the environment and to safeguard the forests and wild life' was inserted by:",
    ["1st Amendment Act, 1951", "24th Amendment Act, 1971", "42nd Amendment Act, 1976", "44th Amendment Act, 1978"],
    2,
    "Article 48A was added by the 42nd Constitutional Amendment Act, 1976 (along with fundamental duty Article 51A(g)), providing the constitutional foundation for modern environmental jurisprudence in India.",
    {"A": "1st Amendment added 15(4) and 9th Schedule.", "B": "24th Amendment dealt with constituent power.", "C": "Correct. 42nd Amendment Act, 1976 inserted Article 48A.", "D": "44th Amendment restored liberties."},
    "Easy", "Article 48A & 42nd Amendment", "Identify 42nd Amendment insertion of Article 48A."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-017", "ch-07", "top-const-07-02",
    "Which Article of the Constitution embodies the directive for the 'Promotion of international peace and security'?",
    ["Article 49", "Article 50", "Article 51", "Article 52"],
    2,
    "Article 51 directs the State to: (a) promote international peace and security; (b) maintain just and honourable relations between nations; (c) foster respect for international law and treaty obligations; and (d) encourage settlement of international disputes by arbitration.",
    {"A": "Article 49 is protection of monuments.", "B": "Article 50 is separation of judiciary.", "C": "Correct. Article 51 is international peace and security.", "D": "Article 52 begins Part V (President of India)."},
    "Easy", "Article 51", "Recall Article 51 International Peace."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-018", "ch-07", "top-const-07-02",
    "Participation of workers in the management of industries is provided under which Article?",
    ["Article 41", "Article 42", "Article 43A", "Article 47"],
    2,
    "Article 43A was inserted by the 42nd Constitutional Amendment Act, 1976: 'The State shall take steps, by suitable legislation or in any other way, to secure the participation of workers in the management of undertakings, establishments or other organisations engaged in any industry'.",
    {"A": "Article 41 is right to work, education, public assistance.", "B": "Article 42 is just and humane conditions and maternity relief.", "C": "Correct. Article 43A provides workers' participation in management.", "D": "Article 47 is nutrition, standard of living, and prohibition of intoxicating drinks."},
    "Medium", "Article 43A", "Recall Article 43A workers' participation."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-019", "ch-07", "top-const-07-02",
    "Which Article directs the State to bring about the 'Prohibition of the consumption of intoxicating drinks and of drugs which are injurious to health'?",
    ["Article 45", "Article 46", "Article 47", "Article 48"],
    2,
    "Article 47 directs the State to raise the level of nutrition and the standard of living of its people and the improvement of public health, and in particular to bring about prohibition of intoxicating drinks and drugs except for medicinal purposes.",
    {"A": "Article 45 is early childhood care.", "B": "Article 46 is promotion of educational/economic interests of SC/ST.", "C": "Correct. Article 47 directs prohibition of liquor/drugs.", "D": "Article 48 is agriculture/cow slaughter."},
    "Easy", "Article 47", "Recall Article 47 Prohibition."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-020", "ch-07", "top-const-07-02",
    "Under the 86th Amendment Act, 2002, the subject matter of Article 45 was amended to provide for:",
    ["Compulsory military training", "Early childhood care and education for all children until they complete the age of six years", "Free laptops for college students", "Vocational education in all villages"],
    1,
    "Consequent to inserting Article 21A for ages 6–14, the 86th Amendment substituted Article 45 to state: 'The State shall endeavour to provide early childhood care and education for all children until they complete the age of six years'.",
    {"A": "Military training is not in DPSP.", "B": "Correct. Early childhood care and education until age of six years.", "C": "Laptops not in DPSP.", "D": "Vocational education is covered generally under Art. 41."},
    "Medium", "Article 45 & 86th Amendment", "Trace 86th Amendment substitution of Article 45."
))

# 07-21 to 07-30: Harmonious Construction (FR vs DPSP)
MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-021", "ch-07", "top-const-07-03",
    "In State of Madras v. Champakam Dorairajan (1951), what was the Supreme Court's ruling on the relationship between Fundamental Rights and DPSP?",
    ["DPSP override Fundamental Rights in case of conflict", "Fundamental Rights are sacrosanct and DPSP must run as subsidiary to Fundamental Rights", "Both have identical legal status", "High Courts can choose which one to apply"],
    1,
    "In Champakam Dorairajan (1951), the 7-Judge Bench ruled that Fundamental Rights are sacrosanct and cannot be abridged by any legislative or executive act; the Directive Principles must conform to and run as subsidiary to the Chapter on Fundamental Rights.",
    {"A": "Overruled in later jurisprudence.", "B": "Correct. FRs sacrosanct; DPSP run as subsidiary.", "C": "Identical status rejected.", "D": "Discretionary application rejected."},
    "Easy", "Champakam Dorairajan, AIR 1951 SC 226", "Master initial judicial subordinate view of DPSP."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-022", "ch-07", "top-const-07-03",
    "The 'Doctrine of Harmonious Construction' between Fundamental Rights and Directive Principles was first propounded in:",
    ["A.K. Gopalan v. State of Madras (1950)", "In re Kerala Education Bill (1958)", "Golaknath v. State of Punjab (1967)", "Kesavananda Bharati v. State of Kerala (1973)"],
    1,
    "In In re Kerala Education Bill (1958), Chief Justice S.R. Das modified the rigid Champakam doctrine, introducing the 'Doctrine of Harmonious Construction': courts should not see an inherent conflict between Parts III and IV, but must attempt to give effect to both so far as possible.",
    {"A": "A.K. Gopalan dealt with Art. 21 and preventive detention.", "B": "Correct. In re Kerala Education Bill (1958) introduced Harmonious Construction.", "C": "Golaknath banned amending FRs.", "D": "Kesavananda established Basic Structure."},
    "Medium", "In re Kerala Education Bill, AIR 1958 SC 956", "Recall origin of Harmonious Construction between FR and DPSP."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-023", "ch-07", "top-const-07-03",
    "Which Constitutional Amendment inserted Article 31C granting immunity to laws implementing Article 39(b) and 39(c) from challenge under Articles 14 and 19?",
    ["24th Amendment Act, 1971", "25th Amendment Act, 1971", "42nd Amendment Act, 1976", "44th Amendment Act, 1978"],
    1,
    "The 25th Constitutional Amendment Act, 1971 inserted Article 31C, which provided that no law giving effect to the policy of securing the principles in Article 39(b) (material resources distribution) or 39(c) (prevention of wealth concentration) shall be void on the ground of inconsistency with Articles 14, 19, or 31.",
    {"A": "24th Amendment dealt with Art. 368.", "B": "Correct. 25th Amendment Act, 1971 inserted Article 31C.", "C": "42nd Amendment expanded 31C to all DPSPs.", "D": "44th Amendment deleted Art. 31."},
    "Medium", "Article 31C & 25th Amendment", "Identify 25th Amendment origin of Article 31C."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-024", "ch-07", "top-const-07-03",
    "In Kesavananda Bharati (1973), which portion of Article 31C was struck down as unconstitutional for violating the Basic Structure?",
    ["The entire Article 31C", "The first part protecting laws implementing Articles 39(b) and 39(c)", "The second part: 'and no law containing a declaration that it is to give effect to such policy shall be called in question in any court on the ground that it does not give effect to such policy'", "The reference to Article 14"],
    2,
    "In Kesavananda Bharati (1973), the 13-Judge Bench upheld the first part of Article 31C granting immunity to laws implementing Art. 39(b) and (c), but struck down the second part ('and no law containing a declaration... shall be called in question in any court') because it ousted Judicial Review, an essential basic feature.",
    {"A": "First part was upheld.", "B": "Immunity for 39(b)/(c) was upheld.", "C": "Correct. Struck down the ouster of judicial review clause.", "D": "Article 14 reference was upheld in part 1."},
    "Hard", "Kesavananda Bharati (1973) 4 SCC 225", "Master Article 31C split validity in Kesavananda."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-025", "ch-07", "top-const-07-03",
    "What famous metaphor did Chief Justice Y.V. Chandrachud use in Minerva Mills v. Union of India (1980) to describe the relationship between Fundamental Rights and DPSP?",
    ["'Two sides of the same sovereign coin'", "'Two wheels of a chariot, one no less important than the other'", "'The sword and the shield of democracy'", "'The warp and the weft of a tapestry'"],
    1,
    "In Minerva Mills (1980), Chandrachud CJ famously observed: 'The Indian Constitution is founded on the bedrock of the balance between Parts III and IV. To give absolute primacy to one over the other is to disturb the harmony of the Constitution... They are like the two wheels of a chariot, one no less important than the other'.",
    {"A": "Metaphor not used.", "B": "Correct. 'Two wheels of a chariot, one no less important than the other'.", "C": "Metaphor not used.", "D": "Metaphor not used."},
    "Easy", "Minerva Mills (1980) 3 SCC 625", "Recall 'Two wheels of a chariot' quote."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-026", "ch-07", "top-const-07-03",
    "In Minerva Mills (1980), the Supreme Court struck down Section 4 of the 42nd Amendment Act, 1976 because it sought to:",
    ["Abolish all Directive Principles", "Subordinate Fundamental Rights (Articles 14 and 19) to ALL Directive Principles, destroying the essential balance between Parts III and IV", "Make DPSP directly enforceable in High Courts", "Delete Article 39(b) and 39(c)"],
    1,
    "Section 4 of the 42nd Amendment had amended Article 31C to extend blanket immunity to laws implementing ANY and ALL Directive Principles. The Court struck it down, holding that destroying the harmony and balance between Fundamental Rights and Directive Principles destroys the Basic Structure.",
    {"A": "It sought to elevate DPSP, not abolish them.", "B": "Correct. Subordinating FRs to ALL DPSPs destroys the Basic Structure.", "C": "Did not make DPSP enforceable in court.", "D": "Preserved 39(b) and (c)."},
    "Hard", "Minerva Mills (1980) 3 SCC 625", "Analyze strike-down of 42nd Amendment Article 31C expansion."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-027", "ch-07", "top-const-07-03",
    "What is the current constitutional status of Article 31C today?",
    ["Completely deleted by the 44th Amendment", "It remains in force in its pre-1976 form, protecting ONLY laws implementing Article 39(b) and Article 39(c) from challenge under Articles 14 and 19", "It protects laws implementing all DPSPs", "It is suspended by presidential order"],
    1,
    "Following Kesavananda Bharati (1973), Minerva Mills (1980), and Sanjeev Coke (1983), Article 31C survives only in its original limited scope: protecting laws enacted to secure the principles in Article 39(b) or 39(c) against challenge under Articles 14 and 19.",
    {"A": "44th Amendment deleted Art. 31, not Art. 31C.", "B": "Correct. Survives in limited form for Articles 39(b) and 39(c) only.", "C": "Blanket protection was struck down in Minerva Mills.", "D": "Not suspended."},
    "Hard", "Article 31C Current Status", "Master current constitutional vitality of Article 31C."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-028", "ch-07", "top-const-07-03",
    "In State of Gujarat v. Mirzapur Moti Kureshi Kassab Jamat (2005), a 7-Judge Constitution Bench held that cow slaughter bans under Article 48 are:",
    ["Unreasonable restrictions violating Article 19(1)(g)", "Inherently reasonable restrictions on trade under Article 19(6) read with Articles 48 and 51A(g)", "Applicable only to Muslim butchers", "Void for violating secularism"],
    1,
    "In Mirzapur Moti Kureshi (2005), Chief Justice R.C. Lahoti held that in testing the constitutional validity of a statute under Article 19, the Directive Principles (Art. 48) and Fundamental Duties (Art. 51A(g)) must be read together, upholding a complete ban on the slaughter of cow progeny as a reasonable restriction in public interest.",
    {"A": "Overruled earlier Hanif Quareshi test.", "B": "Correct. Reasonable restriction under Art. 19(6) read with Art. 48 and 51A(g).", "C": "Secular application to all cattle slaughter.", "D": "Upheld as constitutional."},
    "Medium", "Mirzapur Moti Kureshi (2005) 8 SCC 534", "Recall cattle slaughter jurisprudence under Art. 48."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-029", "ch-07", "top-const-07-03",
    "Which Article contains the directive that the ownership and control of the material resources of the community must be distributed to subserve the common good?",
    ["Article 38", "Article 39(b)", "Article 39(c)", "Article 43"],
    1,
    "Article 39(b) provides: 'that the ownership and control of the material resources of the community are so distributed as best to subserve the common good'.",
    {"A": "Article 38 is social order promotion.", "B": "Correct. Article 39(b) material resources distribution.", "C": "Article 39(c) is prevention of concentration of wealth.", "D": "Article 43 is living wage."},
    "Easy", "Article 39(b)", "Recall Article 39(b) material resources clause."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-07-030", "ch-07", "top-const-07-03",
    "In Property Owners Association v. State of Maharashtra (2024), a 9-Judge Constitution Bench held regarding Article 39(b) that:",
    ["Every privately owned property is automatically a 'material resource of the community'", "Not all private property is a material resource of the community; whether private property qualifies depends on factors like nature of resource, public impact, and scarcity", "Private property cannot be acquired by the State under any circumstances", "Article 39(b) applies only to agricultural land"],
    1,
    "In the landmark 9-Judge Bench ruling in Property Owners Association (November 2024), Chief Justice D.Y. Chandrachud (overruling Justice Krishna Iyer's expansive socialist view in Sanjeev Coke) held that privately owned property does not automatically qualify as a 'material resource of the community'; it depends on an inquiry into the nature, characteristics, and public impact of the property.",
    {"A": "Overruled Krishna Iyer's broad view.", "B": "Correct. Not all private property qualifies; must satisfy contextual test.", "C": "Eminent domain is recognized.", "D": "Applies beyond agriculture."},
    "Hard", "Property Owners Assn. (2024) SCC OnLine SC", "Recall 2024 9-Judge Bench ruling on Article 39(b)."
))

print(f"Chapter 7 complete ({len(MCQS_CH06_08)} total).")

# ==============================================================================
# CHAPTER 8: FUNDAMENTAL DUTIES (25 MCQs)
# ==============================================================================
# 08-01 to 08-12: Origin & Enactment (Art 51A)
MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-001", "ch-08", "top-const-08-01",
    "Part IVA containing Article 51A (Fundamental Duties) was added to the Constitution by which Constitutional Amendment?",
    ["42nd Amendment Act, 1976", "44th Amendment Act, 1978", "86th Amendment Act, 2002", "91st Amendment Act, 2003"],
    0,
    "Part IVA and Article 51A were inserted by the 42nd Constitutional Amendment Act, 1976 on the recommendation of the Sardar Swaran Singh Committee.",
    {"A": "Correct. 42nd Amendment Act, 1976.", "B": "44th Amendment restored liberties in 1978.", "C": "86th Amendment added the 11th duty in 2002.", "D": "91st Amendment limited ministry size."},
    "Easy", "Part IVA & 42nd Amendment", "Recall 42nd Amendment addition of Part IVA."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-002", "ch-08", "top-const-08-01",
    "On the recommendation of which Committee were Fundamental Duties incorporated into the Indian Constitution?",
    ["Sardar Swaran Singh Committee", "Verma Committee", "Sarkaria Commission", "Balwant Rai Mehta Committee"],
    0,
    "The Sardar Swaran Singh Committee (appointed by the Congress government in 1976) recommended the inclusion of a chapter on Fundamental Duties in the Constitution.",
    {"A": "Correct. Sardar Swaran Singh Committee (1976).", "B": "Justice J.S. Verma Committee (1999) examined legal operationalization.", "C": "Sarkaria Commission dealt with Centre-State relations.", "D": "Balwant Rai Mehta dealt with Panchayati Raj."},
    "Easy", "Swaran Singh Committee", "Identify Swaran Singh Committee on Fundamental Duties."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-003", "ch-08", "top-const-08-01",
    "How many Fundamental Duties were originally enacted by the 42nd Constitutional Amendment Act, 1976?",
    ["Eight duties", "Ten duties", "Eleven duties", "Twelve duties"],
    1,
    "The 42nd Amendment Act, 1976 originally enacted TEN Fundamental Duties under Article 51A (clauses (a) to (j)). The 11th duty (clause (k)) was added by the 86th Amendment in 2002.",
    {"A": "Swaran Singh Committee suggested 8 duties.", "B": "Correct. Exactly ten (10) duties enacted in 1976.", "C": "Eleven is current count.", "D": "Twelve is incorrect."},
    "Easy", "Article 51A Original Count", "Recall original count of Fundamental Duties."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-004", "ch-08", "top-const-08-01",
    "Which of the following recommendations of the Swaran Singh Committee was NOT accepted by Parliament while enacting the 42nd Amendment?",
    ["Imposition of penalty or punishment by Parliament for non-compliance with any duty", "Duty to pay taxes", "No law imposing a penalty for non-compliance with duties shall be called in question in any court", "All of the above recommendations were rejected"],
    3,
    "The Swaran Singh Committee had recommended: (1) Parliament may impose penalties for non-compliance with duties; (2) such penal laws should be immune from judicial review; and (3) Duty to pay taxes should be a fundamental duty. The Congress government REJECTED all three recommendations.",
    {"A": "Penal sanction clause was rejected.", "B": "Duty to pay taxes was rejected.", "C": "Bar on judicial review was rejected.", "D": "Correct. All of the above recommendations were rejected by Parliament."},
    "Hard", "Swaran Singh Committee Recommendations", "Identify rejected Swaran Singh recommendations."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-005", "ch-08", "top-const-08-01",
    "The 11th Fundamental Duty (duty of parent or guardian to provide education to his child between 6 and 14 years) was added by:",
    ["44th Amendment Act, 1978", "86th Amendment Act, 2002", "91st Amendment Act, 2003", "97th Amendment Act, 2011"],
    1,
    "The 86th Constitutional Amendment Act, 2002 added the 11th Fundamental Duty as clause (k) to Article 51A: 'who is a parent or guardian to provide opportunities for education to his child or, as the case may be, ward between the age of six and fourteen years'.",
    {"A": "44th Amendment restored liberties in 1978.", "B": "Correct. 86th Amendment Act, 2002 added the 11th duty.", "C": "91st Amendment limited ministry size.", "D": "97th Amendment dealt with co-operatives."},
    "Easy", "Article 51A(k) & 86th Amendment", "Recall 86th Amendment 11th duty."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-006", "ch-08", "top-const-08-01",
    "Are Fundamental Duties under Article 51A directly enforceable by writs of mandamus in a court of law?",
    ["Yes, under Article 32", "No, Fundamental Duties are non-justiciable per se and cannot be enforced directly without an independent parliamentary statute", "Yes, under Article 226", "Yes, by filing an FIR at a police station"],
    1,
    "Fundamental Duties are non-justiciable and non-self-executing: no citizen can be punished or coerced directly under Article 51A without an enabling statutory enactment passed by Parliament (Verma Committee Report 1999).",
    {"A": "Article 32 enforces Part III, not Part IVA.", "B": "Correct. Non-justiciable per se without enabling legislation.", "C": "Article 226 cannot enforce 51A directly.", "D": "FIR requires penal statutory offence."},
    "Medium", "Article 51A Enforceability", "Understand non-justiciability of Fundamental Duties."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-007", "ch-08", "top-const-08-01",
    "To whom are the Fundamental Duties in Article 51A addressed?",
    ["To all persons residing in India (citizens and foreigners alike)", "Exclusively to Citizens of India", "To the State and its instrumentalities", "To public officials and civil servants only"],
    1,
    "Article 51A explicitly opens with: 'It shall be the duty of every CITIZEN of India...'. Fundamental Duties apply strictly to Indian citizens and do not extend to foreigners.",
    {"A": "Foreigners are excluded.", "B": "Correct. Exclusively to Citizens of India.", "C": "State duties are in Part IV (DPSP).", "D": "Applies to all citizens, not just officials."},
    "Easy", "Article 51A Applicability", "Identify citizen-only scope of Article 51A."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-008", "ch-08", "top-const-08-01",
    "Which Committee was appointed by the Government of India in 1998 to operationalize Fundamental Duties and identify legal provisions for their enforcement?",
    ["Justice J.S. Verma Committee", "Justice Sarkaria Committee", "Justice Venkatachaliah Commission", "Justice Punchhi Commission"],
    0,
    "The Justice J.S. Verma Committee on Fundamental Duties of Citizens was appointed in 1998 (reported in 1999) and identified existing legal provisions across penal, environmental, and civil statutes that already enforce several fundamental duties.",
    {"A": "Correct. Justice J.S. Verma Committee (1999).", "B": "Sarkaria dealt with federalism.", "C": "Venkatachaliah was NCRWC (2002).", "D": "Punchhi was 2007 Centre-State commission."},
    "Medium", "Justice J.S. Verma Committee (1999)", "Recall Verma Committee on Fundamental Duties."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-009", "ch-08", "top-const-08-01",
    "Which existing penal enactment directly enforces the duty under Article 51A(a) to respect the National Flag and National Anthem?",
    ["The Unlawful Activities (Prevention) Act, 1967", "The Prevention of Insults to National Honour Act, 1971", "The Official Secrets Act, 1923", "The Representation of the People Act, 1951"],
    1,
    "The Prevention of Insults to National Honour Act, 1971 penalizes any disrespect to the National Flag, the Constitution of India, or the National Anthem, giving statutory teeth to Article 51A(a).",
    {"A": "UAPA enforces territorial integrity Art. 51A(c).", "B": "Correct. Prevention of Insults to National Honour Act, 1971.", "C": "Official Secrets Act penalizes espionage.", "D": "RPA governs corrupt electoral practices."},
    "Easy", "Statutory Enforcement of 51A(a)", "Identify statute enforcing respect for National Flag."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-010", "ch-08", "top-const-08-01",
    "In AIIMS Students' Union v. AIIMS (2002), the Supreme Court ruled regarding Fundamental Duties that:",
    ["Fundamental Duties are dead letters with zero legal significance", "Fundamental Duties are equally important as Fundamental Rights; every citizen has a duty to strive for excellence under Article 51A(j)", "Duties can be enforced by issuing an injunction against Parliament", "Duties apply only in medical institutions"],
    1,
    "In AIIMS Students' Union v. AIIMS (2002), Justice R.C. Lahoti held that Fundamental Duties are not mere pious platitudes; they must be read with Fundamental Rights, and the duty to strive towards excellence under Article 51A(j) was invoked to strike down excessive institutional reservation.",
    {"A": "Duties are legally vital.", "B": "Correct. Fundamental Duties are equally important as Fundamental Rights.", "C": "Courts cannot enjoin Parliament.", "D": "Applies throughout society."},
    "Medium", "AIIMS Students' Union (2002) 1 SCC 428", "Master AIIMS Students' Union ratio on duties."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-011", "ch-08", "top-const-08-01",
    "In Bijoe Emmanuel v. State of Kerala (National Anthem Case, 1986), Jehovah's Witnesses students stood up respectfully but did not sing the National Anthem. The Supreme Court held that:",
    ["They must be expelled under Article 51A(a)", "Standing up respectfully without singing does not constitute disrespect under the 1971 Act, and their expulsion violated Article 19(1)(a) and Article 25", "Expulsion was valid under police regulations", "National Anthem singing is compulsory for everyone without exception"],
    1,
    "In Bijoe Emmanuel (1986), Justice O. Chinnappa Reddy held that showing respect to the National Anthem by standing up in reverent silence satisfies constitutional requirements; compelling a student to sing against his genuine religious belief violates Article 19(1)(a) and Article 25.",
    {"A": "Expulsion was set aside.", "B": "Correct. Standing respectfully does not disrespect anthem; expulsion set aside.", "C": "Police regulations subordinated to Constitution.", "D": "Religious conscience protected."},
    "Medium", "Bijoe Emmanuel (1986) 3 SCC 615", "Master Bijoe Emmanuel National Anthem ruling."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-012", "ch-08", "top-const-08-01",
    "In Shyam Narayan Chouksey v. Union of India (2018), modifying its earlier 2016 interim order, the Supreme Court held that playing the National Anthem in cinema halls before movie screenings is:",
    ["Mandatory under criminal penalty", "Optional and not mandatory for cinema hall owners", "Strictly prohibited", "Mandatory only in government-owned theatres"],
    1,
    "In Shyam Narayan Chouksey (2018), a 3-Judge Bench modified its 2016 order and held that playing the National Anthem before the start of feature films in cinema halls is optional and not mandatory, leaving it to the discretion of cinema owners.",
    {"A": "2016 interim mandatory order was modified in 2018.", "B": "Correct. Playing National Anthem in cinema halls is optional.", "C": "Not prohibited.", "D": "No government-theatre distinction."},
    "Medium", "Shyam Narayan Chouksey (2018) 2 SCC 574", "Recall cinema hall National Anthem ruling."
))

# 08-13 to 08-25: Breakdown of 11 Duties (Art 51A(a) to (k))
MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-013", "ch-08", "top-const-08-02",
    "Which clause of Article 51A mandates citizens 'to develop the scientific temper, humanism and the spirit of inquiry and reform'?",
    ["Article 51A(e)", "Article 51A(f)", "Article 51A(h)", "Article 51A(j)"],
    2,
    "Article 51A(h) explicitly provides: 'to develop the scientific temper, humanism and the spirit of inquiry and reform'.",
    {"A": "51A(e) is harmony and dignity of women.", "B": "51A(f) is composite culture.", "C": "Correct. Article 51A(h) is scientific temper.", "D": "51A(j) is excellence in all spheres."},
    "Easy", "Article 51A(h)", "Recall scientific temper clause under Article 51A."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-014", "ch-08", "top-const-08-02",
    "Which clause of Article 51A obligates citizens to 'renounce practices derogatory to the dignity of women'?",
    ["Article 51A(c)", "Article 51A(d)", "Article 51A(e)", "Article 51A(g)"],
    2,
    "Article 51A(e) directs citizens: 'to promote harmony and the spirit of common brotherhood amongst all the people of India... to renounce practices derogatory to the dignity of women'.",
    {"A": "51A(c) is sovereignty, unity and integrity.", "B": "51A(d) is defend the country.", "C": "Correct. Article 51A(e) mandates renouncing practices derogatory to women.", "D": "51A(g) is environment and wildlife."},
    "Easy", "Article 51A(e)", "Identify clause on dignity of women in Article 51A."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-015", "ch-08", "top-const-08-02",
    "Under Article 51A(g), what specific natural components are citizens duty-bound to protect and improve?",
    ["Forests, lakes, rivers, and wildlife, and to have compassion for living creatures", "Mountains, oceans, and mineral deposits", "Agricultural lands and cattle farms", "National parks and zoological gardens only"],
    0,
    "Article 51A(g) specifically mentions: 'to protect and improve the natural environment including forests, lakes, rivers and wild life, and to have compassion for living creatures'.",
    {"A": "Correct. Forests, lakes, rivers, wildlife, and compassion for living creatures.", "B": "Oceans/minerals not specifically listed.", "C": "Agriculture is Art. 48.", "D": "Under-inclusive."},
    "Easy", "Article 51A(g)", "Recall natural components in Article 51A(g)."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-016", "ch-08", "top-const-08-02",
    "Which clause of Article 51A requires citizens to 'safeguard public property and to abjure violence'?",
    ["Article 51A(g)", "Article 51A(h)", "Article 51A(i)", "Article 51A(j)"],
    2,
    "Article 51A(i) provides: 'to safeguard public property and to abjure violence'.",
    {"A": "51A(g) is natural environment.", "B": "51A(h) is scientific temper.", "C": "Correct. Article 51A(i) is safeguard public property and abjure violence.", "D": "51A(j) is strive towards excellence."},
    "Easy", "Article 51A(i)", "Identify public property and abjuring violence clause."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-017", "ch-08", "top-const-08-02",
    "Which clause of Article 51A directs citizens to 'value and preserve the rich heritage of our composite culture'?",
    ["Article 51A(e)", "Article 51A(f)", "Article 51A(g)", "Article 51A(h)"],
    1,
    "Article 51A(f) provides: 'to value and preserve the rich heritage of our composite culture'.",
    {"A": "51A(e) is brotherhood and women's dignity.", "B": "Correct. Article 51A(f) is composite culture.", "C": "51A(g) is environment.", "D": "51A(h) is scientific temper."},
    "Easy", "Article 51A(f)", "Recall composite culture clause under Article 51A."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-018", "ch-08", "top-const-08-02",
    "Which clause of Article 51A obligates citizens to 'cherish and follow the noble ideals which inspired our national struggle for freedom'?",
    ["Article 51A(a)", "Article 51A(b)", "Article 51A(c)", "Article 51A(d)"],
    1,
    "Article 51A(b) provides: 'to cherish and follow the noble ideals which inspired our national struggle for freedom'.",
    {"A": "51A(a) is respect Constitution, Flag, Anthem.", "B": "Correct. Article 51A(b) is noble ideals of freedom struggle.", "C": "51A(c) is uphold sovereignty, unity, integrity.", "D": "51A(d) is defend the country."},
    "Easy", "Article 51A(b)", "Recall freedom struggle ideals clause under Article 51A."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-019", "ch-08", "top-const-08-02",
    "Which clause of Article 51A directs citizens to 'uphold and protect the sovereignty, unity and integrity of India'?",
    ["Article 51A(a)", "Article 51A(b)", "Article 51A(c)", "Article 51A(d)"],
    2,
    "Article 51A(c) provides: 'to uphold and protect the sovereignty, unity and integrity of India'.",
    {"A": "51A(a) is Flag and Anthem.", "B": "51A(b) is freedom ideals.", "C": "Correct. Article 51A(c) is sovereignty, unity, integrity.", "D": "51A(d) is national service."},
    "Easy", "Article 51A(c)", "Identify sovereignty and integrity clause in Article 51A."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-020", "ch-08", "top-const-08-02",
    "Which clause of Article 51A directs citizens to 'defend the country and render national service when called upon to do so'?",
    ["Article 51A(b)", "Article 51A(c)", "Article 51A(d)", "Article 51A(e)"],
    2,
    "Article 51A(d) provides: 'to defend the country and render national service when called upon to do so'.",
    {"A": "51A(b) is freedom struggle ideals.", "B": "51A(c) is sovereignty.", "C": "Correct. Article 51A(d) is defend country and national service.", "D": "51A(e) is brotherhood."},
    "Easy", "Article 51A(d)", "Recall national service clause under Article 51A."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-021", "ch-08", "top-const-08-02",
    "Which clause of Article 51A obligates citizens to 'strive towards excellence in all spheres of individual and collective activity'?",
    ["Article 51A(g)", "Article 51A(h)", "Article 51A(i)", "Article 51A(j)"],
    3,
    "Article 51A(j) provides: 'to strive towards excellence in all spheres of individual and collective activity so that the nation constantly rises to higher levels of endeavour and achievement'.",
    {"A": "51A(g) is environment.", "B": "51A(h) is scientific temper.", "C": "51A(i) is public property.", "D": "Correct. Article 51A(j) is strive towards excellence."},
    "Easy", "Article 51A(j)", "Identify striving for excellence clause."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-022", "ch-08", "top-const-08-02",
    "Which of the following is NOT a Fundamental Duty under Article 51A?",
    ["To abide by the Constitution and respect its ideals and institutions, the National Flag and the National Anthem", "To vote in public elections", "To safeguard public property and abjure violence", "To develop the scientific temper and humanism"],
    1,
    "'To vote in public elections' is NOT a fundamental duty under Article 51A (though recommended by the Swaran Singh Committee and NCRWC, it was not enacted into the constitutional text).",
    {"A": "True duty under Art. 51A(a).", "B": "Correct (this is NOT a constitutional duty under Art. 51A).", "C": "True duty under Art. 51A(i).", "D": "True duty under Art. 51A(h)."},
    "Medium", "Article 51A Inclusions/Exclusions", "Identify non-existent duty under Article 51A."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-023", "ch-08", "top-const-08-02",
    "In M.C. Mehta v. Union of India (1988), the Supreme Court directed the Central Government under Article 51A(g) to:",
    ["Close all leather tanneries in India", "Introduce compulsory environmental education in all educational institutions across India for at least one hour a week", "Abolish private motor vehicles", "Impose environmental taxes on all citizens"],
    1,
    "In M.C. Mehta (Kanpur Tanneries Case 1988), the Supreme Court invoked Article 51A(g) to direct the Central Government to issue instructions to all state governments and educational authorities to provide compulsory environmental lessons for at least one hour a week in all educational institutions.",
    {"A": "Only polluting non-compliant tanneries were tackled.", "B": "Correct. Introduce compulsory environmental education in schools/colleges.", "C": "Private vehicles were not banned.", "D": "Courts cannot levy taxes."},
    "Medium", "M.C. Mehta (1988) 1 SCC 471", "Recall M.C. Mehta environmental education directive."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-024", "ch-08", "top-const-08-02",
    "In Aruna Roy v. Union of India (2002), the Supreme Court upheld the National Curriculum Framework (NCF) against challenge under Article 28, holding that teaching values of all religions promotes:",
    ["Religious indoctrination", "The Fundamental Duty of promoting harmony, brotherhood, and composite culture under Article 51A(e) and (f)", "The conversion of minority students", "State control of religious trusts"],
    1,
    "In Aruna Roy (2002), a 3-Judge Bench held that education for value development based on the universal truths of all religions does not violate secularism or Article 28; it promotes the Fundamental Duties of brotherhood (Art. 51A(e)) and valuing composite culture (Art. 51A(f)).",
    {"A": "Religious study was distinguished from religious indoctrination.", "B": "Correct. Promotes brotherhood and composite culture under Art. 51A.", "C": "Conversion was not involved.", "D": "No trust control."},
    "Medium", "Aruna Roy (2002) 7 SCC 368", "Recall Aruna Roy curriculum judgment."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-08-025", "ch-08", "top-const-08-02",
    "Can a citizen be disqualified from contesting elections under the Representation of the People Act, 1951 for preaching untouchability or showing disrespect to the National Flag?",
    ["No, election rights are unrestricted", "Yes, Section 8 of the RPA 1951 disqualifies persons convicted under the Protection of Civil Rights Act 1955 or the Prevention of Insults to National Honour Act 1971, enforcing Article 51A duties", "Only if convicted of murder", "Only if disqualified by the Governor"],
    1,
    "Under Section 8(1) of the Representation of the People Act, 1951, a person convicted of offences under the Prevention of Insults to National Honour Act, 1971 or the Protection of Civil Rights Act, 1955 is disqualified from contesting elections to Parliament and State Assemblies for six years from conviction/release.",
    {"A": "RPA imposes strict moral and legal qualifications.", "B": "Correct. Disqualified under Section 8 of RPA 1951.", "C": "Applies to civil rights and flag offences.", "D": "Disqualification operates by law."},
    "Medium", "Section 8, RPA 1951", "Connect Fundamental Duties to electoral disqualifications."
))

print(f"Chapters 6 to 8 complete ({len(MCQS_CH06_08)} total).")
''')

print("Chapters 6, 7, and 8 appended successfully.")
