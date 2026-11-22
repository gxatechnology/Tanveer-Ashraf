"""
Appends Ch 6 (55 MCQs), Ch 7 (30 MCQs), and Ch 8 (25 MCQs) to scripts/build_mcqs_ch06_to_ch08.py
"""

with open('scripts/build_mcqs_ch06_to_ch08.py', 'a', encoding='utf-8') as f:
    f.write('''
# ==============================================================================
# CHAPTER 6: FUNDAMENTAL RIGHTS (55 MCQs)
# ==============================================================================
# 06-01 to 06-10: Art 12 State & Art 13 Judicial Review
MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-001", "ch-06", "top-const-06-01",
    "Which of the following is NOT included in the definition of 'State' under Article 12?",
    ["Government and Parliament of India", "Government and Legislature of each of the States", "All local or other authorities within the territory of India", "Private unaided educational institutions acting in non-public capacity"],
    3,
    "Article 12 defines 'the State' to include: (1) Government and Parliament of India; (2) Government and Legislature of each of the States; (3) All local authorities; and (4) Other authorities within the territory of India or under the control of the Government of India. Private bodies with no public function are not 'State'.",
    {"A": "Expressly included in Art. 12.", "B": "Expressly included in Art. 12.", "C": "Expressly included in Art. 12.", "D": "Correct. Private unaided bodies not exercising public functions fall outside Art. 12."},
    "Easy", "Article 12", "Define scope of 'State' under Article 12."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-002", "ch-06", "top-const-06-01",
    "In Ajay Hasia v. Khalid Mujib (1981), the Supreme Court laid down how many cumulative tests to determine whether an entity is an 'instrumentality or agency of the State'?",
    ["Three tests", "Four tests", "Six tests", "Eight tests"],
    2,
    "In Ajay Hasia (1981), Justice P.N. Bhagwati formulated SIX criteria: (1) entire share capital held by government; (2) financial assistance meeting almost entire expenditure; (3) monopoly status conferred or protected by State; (4) deep and pervasive State control; (5) functions of public importance closely related to governmental functions; (6) transfer of a government department to a corporation.",
    {"A": "Three is incorrect.", "B": "Four is incorrect.", "C": "Correct. Six cumulative tests formulated by Bhagwati J.", "D": "Eight is incorrect."},
    "Medium", "Ajay Hasia v. Khalid Mujib (1981) 1 SCC 722", "Identify Ajay Hasia tests for Article 12."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-003", "ch-06", "top-const-06-01",
    "In Pradeep Kumar Biswas v. Indian Institute of Chemical Biology (2002), the 7-Judge Bench held that for an entity to be 'State' under Article 12, the government control must be:",
    ["Merely regulatory under statutory rules", "Deep and pervasive, not merely regulatory", "Based solely on financial loans", "Determined by the Prime Minister"],
    1,
    "In Pradeep Kumar Biswas (2002), a 7-Judge Bench overruled Sabhajit Tewary and held that the Council of Scientific and Industrial Research (CSIR) is 'State' because government control over its management, finances, and governing body is 'deep and pervasive', not merely regulatory.",
    {"A": "Regulatory control is insufficient (Zee Telefilms).", "B": "Correct. Control must be deep and pervasive.", "C": "Financial loan alone is insufficient.", "D": "Executive fiat is irrelevant."},
    "Hard", "Pradeep Kumar Biswas (2002) 5 SCC 111", "Master deep and pervasive control test."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-004", "ch-06", "top-const-06-01",
    "Is the 'Judiciary' considered 'State' under Article 12 when exercising its judicial functions?",
    ["Yes, always in all capacities", "No, when performing judicial functions, the courts are not 'State'; but when performing administrative functions, they fall under Article 12", "Never under any circumstances", "Only District Courts are State"],
    1,
    "In Naresh Shridhar Mirajkar v. State of Maharashtra (1966) and Rupa Ashok Hurra, the Supreme Court held that the judiciary while acting in its judicial capacity is not 'State' (a judicial order cannot violate fundamental rights so as to be challenged under Art. 32); however, in its administrative capacity (e.g. staff appointments under Art. 146/229), it is 'State'.",
    {"A": "Judicial adjudications are not State under Art. 12.", "B": "Correct. Not State judicially, but State administratively.", "C": "Administrative acts are subject to Art. 12.", "D": "No distinction between levels."},
    "Hard", "Naresh Mirajkar (1966) 3 SCR 744", "Differentiate judicial from administrative functions of judiciary."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-005", "ch-06", "top-const-06-01",
    "The 'Doctrine of Eclipse' applies primarily to:",
    ["Post-constitutional laws under Article 13(2)", "Pre-constitutional laws under Article 13(1)", "Constitutional amendments under Article 368", "Ordinances under Article 123"],
    1,
    "In Bhikaji Narain Dhakras v. State of M.P. (1955), the Supreme Court established the Doctrine of Eclipse: a pre-constitutional law inconsistent with fundamental rights is not dead ab initio; it remains in a dormant or moribund condition ('eclipsed') and becomes active again once the constitutional shadow is removed by an amendment.",
    {"A": "Post-constitutional laws violating FRs are void ab initio (Deep Chand, Mahendra Lal Jain).", "B": "Correct. Pre-constitutional laws under Article 13(1).", "C": "Does not apply to Art. 368.", "D": "Ordinances are post-constitutional laws."},
    "Medium", "Bhikaji Narain Dhakras (1955) 2 SCR 589", "Master Doctrine of Eclipse."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-006", "ch-06", "top-const-06-01",
    "Under the 'Doctrine of Severability' (Article 13), if an unconstitutional provision can be cleanly separated from the valid parts of a statute:",
    ["The entire statute is declared void", "Only the offending provision is void, while the valid remainder survives", "The President must re-enact the statute", "The High Court must draft an amendment"],
    1,
    "In A.K. Gopalan v. State of Madras (1950) and R.M.D.C. v. Union of India (1957), the Supreme Court held that under the Doctrine of Severability, only the invalid part is void if the valid and invalid portions are distinct and what remains is an independent, workable legislative scheme.",
    {"A": "Entire statute falls only if provisions are inextricably interwoven.", "B": "Correct. Only the unconstitutional part is struck down.", "C": "President does not re-enact.", "D": "Courts cannot draft statutes."},
    "Easy", "Article 13(1) & (2)", "Explain Doctrine of Severability."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-007", "ch-06", "top-const-06-01",
    "Can an Indian citizen 'waive' his Fundamental Rights under the Constitution?",
    ["Yes, any citizen can waive any right by a written contract", "No, in Basheshar Nath v. CIT (1959), the Supreme Court held that Fundamental Rights cannot be waived", "Yes, but only rights under Article 19", "Yes, with the permission of the Attorney-General"],
    1,
    "In Basheshar Nath v. Commissioner of Income Tax (1959), a 5-Judge Constitution Bench held that the American Doctrine of Waiver does not apply in India. Fundamental Rights are enacted as matters of public policy and national interest; no citizen can bargain away or waive constitutional protections.",
    {"A": "Waiver of FRs is void.", "B": "Correct. Basheshar Nath established that FRs cannot be waived.", "C": "Article 19 cannot be waived (Nar Singh Pal).", "D": "Attorney-General has no dispensing power."},
    "Medium", "Basheshar Nath v. CIT, AIR 1959 SC 149", "Recall bar on waiver of Fundamental Rights."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-008", "ch-06", "top-const-06-01",
    "Does the definition of 'law' under Article 13(3)(a) include custom or usage having the force of law?",
    ["No, only statutes passed by Parliament", "Yes, Article 13(3)(a) explicitly includes ordinance, order, bye-law, rule, regulation, notification, custom or usage", "Custom is excluded from constitutional review", "Only customs in tribal areas are included"],
    1,
    "Article 13(3)(a) defines 'law' comprehensively to include: 'any Ordinance, order, bye-law, rule, regulation, notification, custom or usage having in the territory of India the force of law'.",
    {"A": "Statutes are only one part.", "B": "Correct. Explicitly includes customs and usages having the force of law.", "C": "Customs violating FRs are void (Madhu Kishwar).", "D": "Applies throughout India."},
    "Easy", "Article 13(3)(a)", "Identify components of 'law' under Article 13."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-009", "ch-06", "top-const-06-01",
    "Which Constitutional Amendment inserted clause (4) in Article 13 declaring that 'Nothing in this article shall apply to any amendment of this Constitution made under article 368'?",
    ["24th Amendment Act, 1971", "25th Amendment Act, 1971", "42nd Amendment Act, 1976", "44th Amendment Act, 1978"],
    0,
    "The 24th Constitutional Amendment Act, 1971 inserted Article 13(4) and Article 368(3) to nullify the 11-Judge Bench ruling in Golaknath (1967), explicitly excluding Article 368 amendments from Article 13 review (upheld in Kesavananda subject to Basic Structure).",
    {"A": "Correct. 24th Amendment Act, 1971.", "B": "25th Amendment dealt with property compensation Art. 31C.", "C": "42nd Amendment was 1976 mini-constitution.", "D": "44th Amendment restored civil liberties in 1978."},
    "Medium", "24th Constitutional Amendment Act, 1971", "Identify 24th Amendment addition of Article 13(4)."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-010", "ch-06", "top-const-06-01",
    "Is the Board of Control for Cricket in India (BCCI) a 'State' under Article 12 according to Zee Telefilms Ltd. v. Union of India (2005)?",
    ["Yes, because it selects the Indian national cricket team", "No, because it is not financially, functionally, or administratively dominated by the government, though amenable to Article 226 for public duties", "Yes, under Ajay Hasia monopoly test", "Yes, under CSIR doctrine"],
    1,
    "In Zee Telefilms (2005), the 5-Judge Bench held that BCCI is NOT 'State' under Article 12 as government control is not deep and pervasive; however, because it performs a public function (selecting national team), it is amenable to High Court writ jurisdiction under Article 226.",
    {"A": "Selecting national team makes it amenable to Art. 226, not Art. 12 State.", "B": "Correct. Not Art. 12 State, but amenable to Art. 226.", "C": "Monopoly is de facto, not State-conferred.", "D": "CSIR had pervasive government control."},
    "Hard", "Zee Telefilms Ltd. v. Union of India (2005) 4 SCC 649", "Analyze BCCI status under Article 12 and 226."
))

# 06-11 to 06-20: Right to Equality (Arts 14–18)
MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-011", "ch-06", "top-const-06-02",
    "The two concepts in Article 14—'Equality before the law' and 'Equal protection of the laws'—are borrowed respectively from:",
    ["British common law and the American Constitution (14th Amendment)", "American Constitution and Irish Constitution", "French Declaration and Russian Constitution", "German Weimar law and Canadian charter"],
    0,
    "'Equality before the law' is a negative concept of British origin (Dicey's Rule of Law: no person above the law). 'Equal protection of the laws' is a positive concept borrowed from Section 1 of the 14th Amendment of the US Constitution (equal treatment under equal circumstances).",
    {"A": "Correct. British common law (Dicey) and American 14th Amendment.", "B": "Ireland provided DPSP.", "C": "French gave liberty, equality, fraternity.", "D": "Weimar gave emergency."},
    "Easy", "Article 14 Genesis", "Trace dual origins of Article 14 concepts."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-012", "ch-06", "top-const-06-02",
    "Under the traditional doctrine of classification (State of West Bengal v. Anwar Ali Sarkar, 1952), a valid classification under Article 14 must satisfy which two conditions?",
    ["(1) Intelligible differentia, and (2) Rational nexus to the statutory object sought to be achieved", "(1) Executive discretion, and (2) Financial viability", "(1) Approval by Governor, and (2) Public consultation", "(1) Majority vote, and (2) Natural justice"],
    0,
    "The twin tests of reasonable classification are: (1) The classification must be founded on an 'intelligible differentia' distinguishing grouped persons/things from others; and (2) That differentia must have a 'rational nexus' to the object sought to be achieved by the statute.",
    {"A": "Correct. Intelligible differentia and rational nexus.", "B": "Discretion does not validate classification.", "C": "Governor approval is legislative step, not classification test.", "D": "Majority vote is procedural."},
    "Easy", "Anwar Ali Sarkar, AIR 1952 SC 75", "Master twin tests of reasonable classification."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-013", "ch-06", "top-const-06-02",
    "In E.P. Royappa v. State of Tamil Nadu (1974), Justice P.N. Bhagwati propounded the 'New Doctrine of Equality', declaring that:",
    ["Equality is a dynamic concept; Equality and Arbitrariness are sworn enemies", "Equality is confined to formal mathematical parity", "Article 14 is limited to classification", "Executive orders are immune from Article 14"],
    0,
    "In Royappa (1974), Bhagwati J revolutionized Article 14: 'Equality is a dynamic concept with many aspects and dimensions and it cannot be "cribbed, cabined and confined" within traditional limits. From a positivistic point of view, equality is antithetic to arbitrariness. In fact equality and arbitrariness are sworn enemies.'",
    {"A": "Correct. Equality and Arbitrariness are sworn enemies.", "B": "Mathematical parity was rejected.", "C": "Classification is merely an aid, not the exhausted content of Art. 14.", "D": "Executive orders are fully reviewable."},
    "Medium", "E.P. Royappa (1974) 4 SCC 3", "Identify New Doctrine of Arbitrariness."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-014", "ch-06", "top-const-06-02",
    "Which five specific grounds of discrimination are prohibited by Article 15(1)?",
    ["Religion, race, caste, sex, place of birth", "Religion, race, language, residence, property", "Caste, creed, colour, domicile, wealth", "Sex, descent, residence, language, occupation"],
    0,
    "Article 15(1) provides: 'The State shall not discriminate against any citizen on grounds ONLY of religion, race, caste, sex, place of birth or any of them'.",
    {"A": "Correct. Religion, race, caste, sex, place of birth (RRCSP).", "B": "Residence is in Art. 16, not Art. 15(1).", "C": "Creed/colour/wealth are not constitutional terms here.", "D": "Descent and residence are Art. 16 grounds."},
    "Easy", "Article 15(1)", "Recall the five grounds of Article 15(1)."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-015", "ch-06", "top-const-06-02",
    "Which Constitutional Amendment inserted Article 15(4) empowering the State to make special provisions for the advancement of SEBCs and SCs/STs, overriding Champakam Dorairajan?",
    ["1st Constitutional Amendment Act, 1951", "7th Constitutional Amendment Act, 1956", "24th Constitutional Amendment Act, 1971", "42nd Constitutional Amendment Act, 1976"],
    0,
    "The 1st Constitutional Amendment Act, 1951 added Article 15(4) to overcome the Supreme Court's decision in State of Madras v. Champakam Dorairajan (1951), which had struck down communal seat reservations in medical colleges.",
    {"A": "Correct. 1st Amendment Act, 1951 added Article 15(4).", "B": "7th Amendment was 1956 states reorganisation.", "C": "24th Amendment was 1971 constituent power.", "D": "42nd Amendment was 1976."},
    "Medium", "Article 15(4) & 1st Amendment", "Trace legislative nullification of Champakam Dorairajan."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-016", "ch-06", "top-const-06-02",
    "In Indra Sawhney v. Union of India (Mandal Case, 1992), the 9-Judge Constitution Bench ruled that:",
    ["Reservations cannot exceed 50% in ordinary circumstances, and the 'Creamy Layer' must be excluded from OBCs", "Reservations can extend up to 80% based on population", "Creamy layer exclusion applies to Scheduled Castes", "Reservations can be granted in promotions indefinitely"],
    0,
    "In Indra Sawhney (1992), the 9-Judge Bench: (1) upheld 27% OBC reservation; (2) ruled that backward classes cannot be identified solely by economic criteria; (3) mandated exclusion of the 'Creamy Layer'; (4) held total reservation should not exceed 50% except in extraordinary remote situations; and (5) held reservations apply only to initial appointments, not promotions.",
    {"A": "Correct. 50% ceiling and Creamy Layer exclusion.", "B": "80% quota is unconstitutional.", "C": "Creamy layer did not originally apply to SC/ST (until Jarnail Singh 2018).", "D": "Promotions reservation was banned (prompting 77th Amendment)."},
    "Medium", "Indra Sawhney (1992) Supp (3) SCC 217", "Master core holdings of Mandal Case."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-017", "ch-06", "top-const-06-02",
    "Which Constitutional Amendment introduced the 10% reservation for Economically Weaker Sections (EWS) under Articles 15(6) and 16(6)?",
    ["101st Amendment Act, 2016", "102nd Amendment Act, 2018", "103rd Amendment Act, 2019", "104th Amendment Act, 2019"],
    2,
    "The 103rd Constitutional Amendment Act, 2019 inserted Articles 15(6) and 16(6) providing up to 10% reservation in admissions and appointments for Economically Weaker Sections (EWS) of citizens other than SC, ST, and SEBCs (upheld in Janhit Abhiyan v. UOI 2022).",
    {"A": "101st Amendment was GST.", "B": "102nd Amendment gave constitutional status to NCBC.", "C": "Correct. 103rd Amendment Act, 2019 introduced EWS quota.", "D": "104th Amendment extended SC/ST assembly quotas and omitted Anglo-Indians."},
    "Easy", "103rd Constitutional Amendment Act, 2019", "Recall EWS amendment number."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-018", "ch-06", "top-const-06-02",
    "In Janhit Abhiyan v. Union of India (2022), a 5-Judge Constitution Bench upheld the 103rd Amendment (EWS Quota) by a 3:2 majority on the ground that:",
    ["Economic criteria can be an independent basis for affirmative action, and the 50% ceiling rule applies only to non-EWS backward classes under Arts. 15(4) and 16(4)", "The Constitution does not protect equality", "Private educational institutions have no rights", "States have no role in reservations"],
    0,
    "In Janhit Abhiyan (2022), the 3:2 majority (Maheshwari, Trivedi, Pardiwala JJ; Lalit CJ & Bhat J dissenting) held that reservation solely based on economic criteria is permissible and does not violate the Basic Structure, and that the 50% ceiling rule of Indra Sawhney is not inflexible and applies only to social reservations under Arts. 15(4) and 16(4).",
    {"A": "Correct. Economic criteria valid; 50% ceiling does not bar EWS.", "B": "Equality is preserved.", "C": "Private rights were balanced.", "D": "States have concurrent power."},
    "Hard", "Janhit Abhiyan v. Union of India (2022) 10 SCC 1", "Analyze EWS judgment ratio."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-019", "ch-06", "top-const-06-02",
    "Article 17 of the Constitution abolishes 'Untouchability'. Which of the following is TRUE regarding Article 17?",
    ["It is an absolute right with no exceptions, enforceable against both the State and private individuals", "It allows reasonable restrictions in private temples", "The term 'Untouchability' is defined in Article 366 of the Constitution", "It applies only to public employment"],
    0,
    "Article 17 is an absolute, unqualified fundamental right with zero exceptions. It is enforceable against both the State and private citizens. The term 'Untouchability' is NOT defined anywhere in the Constitution or the Protection of Civil Rights Act, 1955.",
    {"A": "Correct. Absolute right enforceable against State and private individuals.", "B": "No exceptions in private temples (civil rights violations).", "C": "Untouchability is NOT defined in Constitution.", "D": "Applies across all social spheres."},
    "Medium", "Article 17", "Analyze absolute nature of Article 17."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-020", "ch-06", "top-const-06-02",
    "In Balaji Raghavan v. Union of India (1996), the Supreme Court upheld the validity of National Awards (Bharat Ratna, Padma Vibhushan) under Article 18 on the condition that:",
    ["They are awarded only to military officers", "They are mere decorations and cannot be used as prefixes or suffixes to the recipient's name", "Recipients pay a state honorarium", "They are approved by the Leader of Opposition"],
    1,
    "In Balaji Raghavan (1996), a 5-Judge Bench held that National Awards do not amount to 'titles' within the prohibition of Article 18(1); however, they are mere decorations and if any recipient uses them as a prefix or suffix to his name, the award is liable to be forfeited.",
    {"A": "Civilians are routinely awarded.", "B": "Correct. Cannot be used as prefix or suffix.", "C": "No honorarium is paid.", "D": "Committee advises Prime Minister."},
    "Medium", "Balaji Raghavan v. UOI (1996) 1 SCC 361", "Recall condition on National Awards under Article 18."
))

# 06-21 to 06-30: Freedoms & Protections in Conviction (Arts 19–20)
MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-021", "ch-06", "top-const-06-03",
    "How many fundamental democratic freedoms are guaranteed to citizens under Article 19(1) today?",
    ["Seven freedoms", "Six freedoms", "Five freedoms", "Eight freedoms"],
    1,
    "Originally, Article 19(1) guaranteed SEVEN freedoms. The 44th Constitutional Amendment Act, 1978 deleted the 'Right to acquire, hold and dispose of property' (Article 19(1)(f)), leaving SIX democratic freedoms: speech, assembly, association, movement, residence, and profession.",
    {"A": "Seven was the original 1950 count.", "B": "Correct. Six freedoms remain today.", "C": "Five is incorrect.", "D": "Eight is incorrect."},
    "Easy", "Article 19(1)", "Recall number of democratic freedoms under Article 19."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-022", "ch-06", "top-const-06-03",
    "The right to form 'Co-operative Societies' was inserted into Article 19(1)(c) by which Constitutional Amendment?",
    ["42nd Amendment Act, 1976", "44th Amendment Act, 1978", "97th Amendment Act, 2011", "103rd Amendment Act, 2019"],
    2,
    "The 97th Constitutional Amendment Act, 2011 amended Article 19(1)(c) to include 'co-operative societies' alongside associations and unions (this specific part of the 97th Amendment was upheld in Rajkot District Coop. Bank 2021).",
    {"A": "42nd Amendment added socialist/secular.", "B": "44th Amendment deleted property.", "C": "Correct. 97th Amendment Act, 2011.", "D": "103rd Amendment was EWS."},
    "Medium", "Article 19(1)(c) & 97th Amendment", "Recall cooperative societies amendment in Article 19."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-023", "ch-06", "top-const-06-02",
    "In Shreya Singhal v. Union of India (2015), the Supreme Court struck down Section 66A of the Information Technology Act, 2000 because:",
    ["It was excessively vague, overbroad, and chilled free speech, not falling under any permissible ground of Article 19(2)", "Parliament lacked legislative competence over cyber laws", "Only the President can regulate internet posts", "It violated Article 25 freedom of conscience"],
    0,
    "In Shreya Singhal (2015), the Supreme Court struck down Section 66A of the IT Act, holding that it created an unconstitutionally vague criminal offence that swept within its net innocent speech, chilling free speech under Article 19(1)(a) without satisfying the reasonable restriction test under Article 19(2).",
    {"A": "Correct. Struck down for vagueness, overbreadth, and chilling effect.", "B": "Parliament has full cyber competence under residuary powers.", "C": "President does not regulate cyber crimes.", "D": "Article 25 was not the ground."},
    "Medium", "Shreya Singhal v. Union of India (2015) 5 SCC 1", "Recall Section 66A strike-down ratio."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-024", "ch-06", "top-const-06-03",
    "Which of the following is NOT a permissible ground of restriction on Freedom of Speech under Article 19(2)?",
    ["Sovereignty and integrity of India", "Friendly relations with foreign States", "Public order, decency or morality", "Public interest or general administrative convenience"],
    3,
    "The 8 exhaustive grounds under Article 19(2) are: (1) sovereignty and integrity of India; (2) security of the State; (3) friendly relations with foreign States; (4) public order; (5) decency or morality; (6) contempt of court; (7) defamation; (8) incitement to an offence. 'Public interest' is a ground in Art. 19(6) for trade, but NOT in Art. 19(2) for speech.",
    {"A": "Explicit ground under Art. 19(2) (added by 16th Amendment).", "B": "Explicit ground under Art. 19(2) (added by 1st Amendment).", "C": "Explicit ground under Art. 19(2).", "D": "Correct. 'Public interest' is NOT a ground under Article 19(2)."},
    "Hard", "Article 19(2)", "Identify non-permissible grounds under Article 19(2)."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-025", "ch-06", "top-const-06-03",
    "The protection against 'Ex-post facto laws' under Article 20(1) applies to:",
    ["Only criminal laws and penal liabilities", "Both criminal and civil tax laws", "Only retrospective civil property acquisitions", "Preventive detention orders"],
    0,
    "In Kedar Nath v. State of West Bengal (1953) and Hathisingh Mfg. Co., the Supreme Court settled that Article 20(1) prohibits retrospective criminal enactments and heavier penalties; it has NO application to civil liabilities, retrospective tax laws, or preventive detention.",
    {"A": "Correct. Applies strictly to criminal laws and penal liability.", "B": "Tax laws can be enacted retrospectively.", "C": "Civil laws are excluded.", "D": "Preventive detention is not a prosecution."},
    "Medium", "Article 20(1)", "Differentiate criminal from civil applicability in Article 20(1)."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-026", "ch-06", "top-const-06-03",
    "Under Article 20(2), the protection against 'Double Jeopardy' requires that:",
    ["A person was previously prosecuted before an administrative department", "A person must have been both prosecuted AND punished for the same offence before a court of law or judicial tribunal", "A person was merely acquitted by a magistrate", "A person was detained under a preventive detention order"],
    1,
    "In Maqbool Hussain v. State of Bombay (1953), the Supreme Court held that Article 20(2) incorporates the maxim 'nemo debet bis vexari pro una et eadem causa' with a narrower scope than American law: it requires that the person must have been both PROSECUTED AND PUNISHED for the same offence before a court of law or judicial tribunal.",
    {"A": "Departmental/customs confiscation is not prosecution before a court (Maqbool Hussain).", "B": "Correct. Requires both prosecution AND punishment before a court.", "C": "Acquittal alone does not satisfy Art. 20(2) (though protected under s. 300 CrPC).", "D": "Preventive detention is not prosecution."},
    "Hard", "Maqbool Hussain, AIR 1953 SC 325", "Master Article 20(2) Double Jeopardy requirements."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-027", "ch-06", "top-const-06-03",
    "In Selvi v. State of Karnataka (2010), the 3-Judge Bench held that involuntary Narco-analysis, Polygraph tests, and Brain Electrical Activation Profile (BEAP) violate:",
    ["Article 14 and Article 19", "Article 20(3) (Privilege against Self-Incrimination) and Article 21 (Personal Liberty and Privacy)", "Article 22 safeguards", "Article 25 religious freedom"],
    1,
    "In Selvi (2010), Chief Justice K.G. Balakrishnan held that compulsory administration of narco-analysis, lie detector, and brain mapping constitutes cruel, inhuman, and degrading treatment violating Article 21 (mental privacy) and constitutes testimonial compulsion violating Article 20(3).",
    {"A": "Not decided primarily on Arts 14/19.", "B": "Correct. Violates Article 20(3) and Article 21.", "C": "Not grounded on preventive detention.", "D": "No religious dimension."},
    "Medium", "Selvi v. State of Karnataka (2010) 7 SCC 263", "Master Selvi narco-analysis judgment."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-028", "ch-06", "top-const-06-03",
    "In State of Bombay v. Kathi Kalu Oghad (1961), an 11-Judge Constitution Bench held that taking which of the following from an accused does NOT violate Article 20(3)?",
    ["Compelled oral confession", "Specimen handwriting, fingerprints, and physical measurements", "Narco-analysis statements", "Privileged letters between accused and attorney"],
    1,
    "In Kathi Kalu Oghad (1961), the 11-Judge Bench held that 'to be a witness' in Article 20(3) means imparting personal knowledge of relevant facts by oral or written testimony. Giving specimen signatures, handwriting, fingerprints, or showing body parts does not amount to being a witness against oneself.",
    {"A": "Oral confession is testimonial.", "B": "Correct. Specimen handwriting, fingerprints, and measurements do not violate Art. 20(3).", "C": "Narco-analysis is testimonial.", "D": "Privileged communications are protected."},
    "Hard", "Kathi Kalu Oghad, AIR 1961 SC 1808", "Distinguish physical evidence from testimonial compulsion."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-029", "ch-06", "top-const-06-03",
    "Does Article 20(3) protect an accused person during police investigation before formal court proceedings begin?",
    ["No, it applies only during court trial", "Yes, in Nandini Satpathy v. P.L. Dani (1978), the Supreme Court held that the right extends to police interrogations and custodial questioning", "Only when the accused is represented by a Senior Advocate", "Only after charges are framed"],
    1,
    "In Nandini Satpathy v. P.L. Dani (1978), Justice V.R. Krishna Iyer ruled that the protective umbrella of Article 20(3) extends beyond the courtroom to police interrogations: an accused or suspect has the right to remain silent when questions have a tendency to expose him to a criminal charge.",
    {"A": "Strictly rejected in Nandini Satpathy.", "B": "Correct. Right extends to police questioning and custodial interrogation.", "C": "Advocate status is irrelevant.", "D": "Applies prior to framing of charges."},
    "Medium", "Nandini Satpathy (1978) 2 SCC 424", "Examine scope of Article 20(3) during police interrogation."
))

MCQS_CH06_08.append(create_mcq(
    "mcq-const-06-030", "ch-06", "top-const-06-03",
    "In Anuradha Bhasin v. Union of India (2020), the Supreme Court held that freedom of speech and trade over the medium of the Internet is constitutionally protected under:",
    ["Article 14 and Article 21 only", "Article 19(1)(a) and Article 19(1)(g)", "Article 21A", "Article 300A"],
    1,
    "In Anuradha Bhasin (2020), the Supreme Court held that freedom of speech and expression and the freedom to practice any profession or carry on trade over the internet are constitutionally protected under Article 19(1)(a) and Article 19(1)(g), and any suspension must satisfy the test of proportionality and cannot be indefinite.",
    {"A": "Grounded in Article 19.", "B": "Correct. Article 19(1)(a) and 19(1)(g).", "C": "Article 21A is school education.", "D": "Article 300A is property."},
    "Medium", "Anuradha Bhasin (2020) 3 SCC 637", "Recall internet suspension judgment."
))

print(f"Ch 6 Part A complete ({len(MCQS_CH06_08)} total).")
''')

print("Ch 6 Part A appended.")
