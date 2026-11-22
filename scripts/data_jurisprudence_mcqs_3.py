"""
Jurisprudence MCQs - Chapters 8 to 11 (88 MCQs)
Topics: top-jur-08-01 to top-jur-11-03
8 MCQs per topic
"""

MCQS_PART3 = []

def add_mcq(mid, cid, tid, q, opts, ans_idx, exp, ob, diff, prov, lo):
    letters = ["A", "B", "C", "D"]
    MCQS_PART3.append({
        "id": mid,
        "subjectId": "law-jurisprudence",
        "chapterId": cid,
        "topicId": tid,
        "question": q,
        "options": opts,
        "answer": ans_idx,
        "answerLetter": letters[ans_idx],
        "explanation": exp,
        "optionBreakdown": ob,
        "difficulty": diff,
        "provision": prov,
        "sourceUrl": "https://archive.org",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": lo,
        "eligible": True,
        "status": "active"
    })

# -------------------------------------------------------------
# CHAPTER 8: LEGAL RIGHTS AND DUTIES
# -------------------------------------------------------------

# top-jur-08-01: Concept of Legal Rights and Duties: Salmond's Formula
add_mcq(
    "mcq-jur-08-001", "ch-jur-08", "top-jur-08-01",
    "According to Sir John Salmond, a Legal Right involves how many essential characteristics or constituents?",
    ["Three", "Four", "Five", "Seven"],
    2,
    "Salmond famously dissected a legal right into Five constituents: (1) Person of Inherence, (2) Person of Incidence, (3) Content (Act/Forbearance), (4) Object of the Right (Res), and (5) Title.",
    {"A": "Three is Austin's elements of law.", "B": "Hohfeld's four conceptions.", "C": "Correct. Salmond's 5 characteristics of a legal right.", "D": "Seven is Finnis's goods."},
    "Easy", "Salmond on Jurisprudence, 12th Ed.", "Recall Salmond's 5 elements of a legal right."
)

add_mcq(
    "mcq-jur-08-002", "ch-jur-08", "top-jur-08-01",
    "In Salmond's formula of a legal right, who is the 'Person of Inherence'?",
    ["The person bound by the duty", "The person in whom the right is vested (the subject/owner of the right)", "The judge who decides the dispute", "The sovereign state"],
    1,
    "The 'Person of Inherence' (or person of interest) is the person who is entitled to the right — the owner or beneficiary of the legal claim.",
    {"A": "That is the Person of Incidence.", "B": "Correct. Person of Inherence = the person entitled to the right.", "C": "Adjudicator.", "D": "Political entity."},
    "Medium", "Salmond on Jurisprudence", "Define Person of Inherence."
)

add_mcq(
    "mcq-jur-08-003", "ch-jur-08", "top-jur-08-01",
    "Who propounded the 'Interest Theory' of legal rights, defining a right as a 'legally protected interest'?",
    ["Savigny", "Rudolf von Ihering", "John Austin", "Holland"],
    1,
    "Rudolf von Ihering formulated the Interest Theory: rights are not mere assertions of the human will, but are substantial economic, physical, or personal interests protected and guaranteed by law.",
    {"A": "Savigny championed the Will Theory.", "B": "Correct. Ihering propounded the Interest Theory.", "C": "Austin supported the Will Theory.", "D": "Holland supported the Will Theory."},
    "Easy", "Ihering, Geist des römischen Rechts", "Identify Ihering's Interest Theory."
)

add_mcq(
    "mcq-jur-08-004", "ch-jur-08", "top-jur-08-01",
    "What is the primary criticism leveled against the 'Will Theory' of legal rights (championed by Savigny, Austin, and Holland)?",
    ["It requires too many judges", "It cannot explain the legal rights possessed by infants, lunatics, comatose patients, or unborn persons who lack conscious legal will", "It gives too much power to corporations", "It applies only in international law"],
    1,
    "The fatal flaw of the Will Theory is that if a right is defined as the exercise of autonomous personal will, infants, mentally disabled persons, and the unborn (who lack conscious will) would possess zero legal rights, which is contrary to modern law.",
    {"A": "Administrative irrelevance.", "B": "Correct. Inability to explain rights of infants and incapacitated persons.", "C": "Corporate personality issue.", "D": "Municipal law issue."},
    "Medium", "Paton's Jurisprudence", "Identify the fatal flaw of the Will Theory."
)

add_mcq(
    "mcq-jur-08-005", "ch-jur-08", "top-jur-08-01",
    "Which jurist asserted that there can be 'Absolute Duties' that exist without any corresponding correlative legal rights?",
    ["Sir John Salmond", "John Austin", "Thomas Erskine Holland", "Roscoe Pound"],
    1,
    "Austin contended that certain legal duties are 'Absolute Duties' having no corresponding rights: duties to the sovereign, duties to the public at large, duties to self, and duties to non-human entities (animals).",
    {"A": "Salmond rejected absolute duties; rights and duties are correlative.", "B": "Correct. Austin propounded the doctrine of Absolute Duties.", "C": "Holland agreed with Salmond on strict correlation.", "D": "Pound focused on social interests."},
    "Medium", "Austin, Lectures on Jurisprudence", "Identify Austin's Absolute Duties."
)

add_mcq(
    "mcq-jur-08-006", "ch-jur-08", "top-jur-08-01",
    "How did Salmond respond to Austin's concept of 'Absolute Duties'?",
    ["Salmond agreed with Austin completely", "Salmond rejected absolute duties, arguing that a duty without a corresponding right in someone is a conceptual impossibility", "Salmond argued duties exist only in criminal law", "Salmond argued rights exist only in property"],
    1,
    "Salmond maintained that right and duty are correlative terms like parent and child; every legal duty is owed to someone (even if owed collectively to the state representing the public), so absolute duties do not exist.",
    {"A": "Salmond strongly disagreed.", "B": "Correct. Salmond insisted every duty must have a corresponding right.", "C": "Duties exist across civil and criminal law.", "D": "Rights exist in personal status too."},
    "Medium", "Salmond on Jurisprudence", "Contrast Salmond and Austin on absolute duties."
)

add_mcq(
    "mcq-jur-08-007", "ch-jur-08", "top-jur-08-01",
    "What landmark 1703 judgment affirmed the foundational principle 'Ubi jus ibi remedium' (Where there is a right, there is a remedy) when an eligible voter was wrongfully prevented from voting?",
    ["Rylands v. Fletcher", "Ashby v. White", "Donoghue v. Stevenson", "Hadley v. Baxendale"],
    1,
    "In Ashby v. White (1703), Chief Justice Holt laid down that if a man has a legal right, he must have a means to vindicate it, and a remedy if he is injured in the enjoyment of it (Injuria sine damno).",
    {"A": "Strict liability precedent.", "B": "Correct. Ashby v. White (1703) 2 Ld. Raym. 938.", "C": "Negligence neighbor principle.", "D": "Contract damages rule."},
    "Easy", "Ashby v. White (1703) 2 Ld. Raym. 938", "Recall Ashby v. White and Ubi jus ibi remedium."
)

add_mcq(
    "mcq-jur-08-008", "ch-jur-08", "top-jur-08-01",
    "What is the 'Title' of a legal right according to Salmond's five elements?",
    ["The official name of the owner", "The vestitive fact or legal event by which the right was created or acquired", "The registered document number", "The headline of the statute"],
    1,
    "Salmond defined Title as the vestitive fact — the legal event, transaction, grant, or circumstance by which the right became vested in the owner (e.g. sale deed, contract, gift, inheritance, prescription).",
    {"A": "Personal name.", "B": "Correct. Title = The vestitive fact or event creating the right.", "C": "Registry number.", "D": "Statutory title."},
    "Medium", "Salmond on Jurisprudence", "Define Title in Salmond's formula."
)

# top-jur-08-02: Hohfeld's Analysis
add_mcq(
    "mcq-jur-08-009", "ch-jur-08", "top-jur-08-02",
    "Wesley Newcomb Hohfeld published his celebrated analysis of 'Fundamental Legal Conceptions' in which year?",
    ["1897", "1913", "1932", "1948"],
    1,
    "W.N. Hohfeld published 'Some Fundamental Legal Conceptions as Applied in Judicial Reasoning' in the Yale Law Journal in 1913, revolutionizing analytical jurisprudence.",
    {"A": "Holmes's Path of the Law.", "B": "Correct. 1913.", "C": "Donoghue v. Stevenson.", "D": "Universal Declaration of Human Rights."},
    "Easy", "Hohfeld, 23 Yale L.J. 16 (1913)", "Identify the year of Hohfeld's landmark paper."
)

add_mcq(
    "mcq-jur-08-010", "ch-jur-08", "top-jur-08-02",
    "In Hohfeld's table of Jural Correlatives, what is the exact correlative of a 'Right' (Claim)?",
    ["No-Right", "Duty", "Privilege", "Immunity"],
    1,
    "In Hohfeld's vertical table of Jural Correlatives: Right is strictly correlative to Duty (If A has a claim against B, B has a correlative duty to A).",
    {"A": "No-Right is the jural opposite of Right.", "B": "Correct. Duty is the jural correlative of Right.", "C": "Privilege is the jural opposite of Duty.", "D": "Immunity is the correlative of Disability."},
    "Easy", "Hohfeld's Table of Jural Correlatives", "Recall the correlative of Right."
)

add_mcq(
    "mcq-jur-08-011", "ch-jur-08", "top-jur-08-02",
    "In Hohfeld's table of Jural Correlatives, what is the correlative of 'Privilege' (Liberty)?",
    ["Duty", "No-Right", "Liability", "Disability"],
    1,
    "Privilege (Liberty) has as its jural correlative 'No-Right' (If A has the privilege/liberty to enter his own land, B has a No-Right that A shall not enter).",
    {"A": "Duty is the opposite of Privilege.", "B": "Correct. No-Right is the correlative of Privilege.", "C": "Liability is the correlative of Power.", "D": "Disability is the correlative of Immunity."},
    "Easy", "Hohfeld's Table of Jural Correlatives", "Recall the correlative of Privilege."
)

add_mcq(
    "mcq-jur-08-012", "ch-jur-08", "top-jur-08-02",
    "In Hohfeld's system, what is the Jural Correlative of 'Power'?",
    ["Disability", "Liability", "Immunity", "Duty"],
    1,
    "Power is correlative to Liability (If A has the legal power to alter B's legal rights, B is under a correlative liability to have his legal status altered).",
    {"A": "Disability is the opposite of Power.", "B": "Correct. Liability is the correlative of Power.", "C": "Immunity is the opposite of Liability.", "D": "Duty is the correlative of Right."},
    "Easy", "Hohfeld's Table of Jural Correlatives", "Recall the correlative of Power."
)

add_mcq(
    "mcq-jur-08-013", "ch-jur-08", "top-jur-08-02",
    "In Hohfeld's system, what is the Jural Correlative of 'Immunity'?",
    ["Liability", "Disability", "No-Right", "Power"],
    1,
    "Immunity has as its jural correlative 'Disability' (If A has an immunity against having his land expropriated without statute, the state official has a legal disability/lack of power to touch it).",
    {"A": "Liability is the opposite of Immunity.", "B": "Correct. Disability is the correlative of Immunity.", "C": "No-Right is correlative of Privilege.", "D": "Power is the opposite of Disability."},
    "Easy", "Hohfeld's Table of Jural Correlatives", "Recall the correlative of Immunity."
)

add_mcq(
    "mcq-jur-08-014", "ch-jur-08", "top-jur-08-02",
    "In Hohfeld's table of Jural Opposites (contradictory legal states in the same person), what is the opposite of 'Right' (Claim)?",
    ["Duty", "No-Right", "Privilege", "Disability"],
    1,
    "In Hohfeld's diagonal table of Jural Opposites: Right and No-Right are opposites (A person cannot simultaneously have a Right and a No-Right regarding the same act).",
    {"A": "Duty is the correlative of Right.", "B": "Correct. No-Right is the opposite of Right.", "C": "Privilege is the opposite of Duty.", "D": "Disability is the opposite of Power."},
    "Easy", "Hohfeld's Table of Jural Opposites", "Identify the Jural Opposite of Right."
)

add_mcq(
    "mcq-jur-08-015", "ch-jur-08", "top-jur-08-02",
    "In Hohfeld's system, what is the Jural Opposite of 'Immunity'?",
    ["Liability", "Power", "Duty", "No-Right"],
    0,
    "Immunity is the opposite of Liability (If A enjoys an immunity, A is free from liability; one cannot be immune and liable in the same respect).",
    {"A": "Correct. Liability is the opposite of Immunity.", "B": "Power is the opposite of Disability.", "C": "Duty is the opposite of Privilege.", "D": "No-Right is opposite of Right."},
    "Easy", "Hohfeld's Table of Jural Opposites", "Identify the Jural Opposite of Immunity."
)

add_mcq(
    "mcq-jur-08-016", "ch-jur-08", "top-jur-08-02",
    "Which Indian Constitution Bench judgment extensively analyzed Hohfeld's jural relations to interpret the scope of 'legal right' under Article 131?",
    ["State of Rajasthan v. Union of India (1977)", "Kesavananda Bharati v. State of Kerala (1973)", "Minerva Mills v. Union of India (1980)", "Maneka Gandhi v. Union of India (1978)"],
    0,
    "In State of Rajasthan v. Union of India (1977 3 SCC 592), Chief Justice Beg analyzed Hohfeldian claims, powers, and immunities to decide whether a State Government has a 'legal right' under Article 131 to challenge dissolution under Article 356.",
    {"A": "Correct. State of Rajasthan v. UOI (1977).", "B": "Basic structure case.", "C": "Judicial review case.", "D": "Article 21 procedure case."},
    "Hard", "State of Rajasthan v. UOI, (1977) 3 SCC 592", "Link Hohfeldian analysis to Indian Article 131 jurisprudence."
)

# top-jur-08-03: Classification of Legal Rights
add_mcq(
    "mcq-jur-08-017", "ch-jur-08", "top-jur-08-03",
    "What is a 'Right in Rem' (Real Right)?",
    ["A right available exclusively against a single individual", "A right available against the world at large (contra mundum)", "A right that cannot be transferred", "A right created only by royal charter"],
    1,
    "A Right in Rem is a real right available against the whole world at large (contra mundum), imposing a general negative duty on all persons not to interfere (e.g. ownership of land, reputation).",
    {"A": "That is a Right in Personam.", "B": "Correct. Right in Rem is enforceable contra mundum.", "C": "Inalienable rights.", "D": "Crown prerogative."},
    "Easy", "Salmond on Jurisprudence", "Define Right in Rem."
)

add_mcq(
    "mcq-jur-08-018", "ch-jur-08", "top-jur-08-03",
    "What is a 'Right in Personam' (Personal Right)?",
    ["A right available against the entire universe", "A right available only against a determinate person or group of persons", "A right to bodily liberty only", "A right that dies with the person"],
    1,
    "A Right in Personam is a personal right available only against a specific, determinate individual or group (e.g. right of a creditor against a borrower for repayment of a debt).",
    {"A": "Right in Rem.", "B": "Correct. Right in Personam binds determinate individuals.", "C": "Personal bodily right.", "D": "Actio personalis."},
    "Easy", "Salmond on Jurisprudence", "Define Right in Personam."
)

add_mcq(
    "mcq-jur-08-019", "ch-jur-08", "top-jur-08-03",
    "How does Salmond distinguish 'Proprietary Rights' from 'Personal Rights'?",
    ["Proprietary rights pertain to immovable land; personal rights to movable goods", "Proprietary rights constitute a person's estate/wealth and have economic value; personal rights pertain to status, bodily safety, and liberty without commercial value", "Proprietary rights are criminal; personal rights are civil", "Proprietary rights exist only in corporations"],
    1,
    "Proprietary rights constitute an individual's assets and wealth (transferable and possessing economic value). Personal rights pertain to status, life, reputation, and liberty, and are inalienable without commercial price.",
    {"A": "Both land and goods are proprietary.", "B": "Correct. Proprietary = Economic wealth/estate; Personal = Status and bodily liberty.", "C": "Both are civil.", "D": "Natural persons hold proprietary rights."},
    "Medium", "Salmond on Jurisprudence", "Distinguish Proprietary from Personal Rights."
)

add_mcq(
    "mcq-jur-08-020", "ch-jur-08", "top-jur-08-03",
    "What is an 'Imperfect Right' in jurisprudence?",
    ["A right that has been struck down by a court", "A right recognized by law for certain defensive purposes (like retention or lien), but lacking a direct judicial action for enforcement", "A right that has no owner", "A right possessed by a minor"],
    1,
    "An Imperfect Right is recognized by the legal system, but is not directly enforceable by a court suit (e.g. a time-barred debt, which cannot be sued upon, but if paid voluntarily or retained through lien, the payment is lawful).",
    {"A": "A void right.", "B": "Correct. Recognized by law for defense/retention but lacking direct suit.", "C": "Ownerless right.", "D": "Incapacity issue."},
    "Medium", "Salmond on Jurisprudence", "Define an Imperfect Right."
)

add_mcq(
    "mcq-jur-08-021", "ch-jur-08", "top-jur-08-03",
    "What is meant by 'Jus in Re Aliena' (Encumbrance)?",
    ["Absolute ownership of property", "A limited right over the property of another person which derogates from the owner's full title", "A right that cannot be sold", "A right granted to a foreign citizen"],
    1,
    "'Jus in Re Aliena' (an encumbrance) is a right carved out of another's ownership, limiting the owner's title (e.g. an easement, mortgage, or lease). Full ownership over one's own property is 'Jus in Re Propria'.",
    {"A": "Jus in Re Propria.", "B": "Correct. Jus in Re Aliena = Encumbrance over another's property.", "C": "Inalienable right.", "D": "Alien rights."},
    "Medium", "Salmond on Jurisprudence", "Define Jus in Re Aliena."
)

add_mcq(
    "mcq-jur-08-022", "ch-jur-08", "top-jur-08-03",
    "Which of the following is the best example of a 'Right in Rem'?",
    ["The right of a creditor to receive repayment from a borrower", "The right of an owner of a house that no one shall commit trespass upon it", "The right of an employer to receive personal service from an employee", "The right of a buyer to receive delivery under a contract of sale"],
    1,
    "Ownership of a house creates a negative right against every member of the public not to commit trespass, making it a classic Right in Rem. The others are contractual Rights in Personam.",
    {"A": "Right in Personam (contract).", "B": "Correct. Ownership creates a Right in Rem against trespass.", "C": "Right in Personam (employment).", "D": "Right in Personam (contract)."},
    "Easy", "Salmond on Jurisprudence", "Identify an example of a Right in Rem."
)

add_mcq(
    "mcq-jur-08-023", "ch-jur-08", "top-jur-08-03",
    "What is the difference between a 'Principal Right' and an 'Accessory Right'?",
    ["Principal rights exist only in criminal law", "A principal right exists independently on its own merit; an accessory right is dependent upon and parasitic on a principal right", "Accessory rights are always worth more money", "Principal rights are unwritten"],
    1,
    "A principal right exists autonomously (e.g. a principal debt). An accessory right exists only to secure, assist, or accompany the principal right (e.g. a mortgage, pledge, or personal guarantee securing the debt).",
    {"A": "Both exist across law.", "B": "Correct. Principal right is autonomous; accessory right is dependent.", "C": "Economic value varies.", "D": "Both can be written."},
    "Easy", "Salmond on Jurisprudence", "Distinguish Principal from Accessory Rights."
)

add_mcq(
    "mcq-jur-08-024", "ch-jur-08", "top-jur-08-03",
    "What is a 'Vested Right' as distinguished from a 'Contingent Right'?",
    ["A vested right is immediate and unconditional or dependent on an event that must happen; a contingent right depends on an uncertain future event", "A vested right can never be inherited", "A contingent right is immediately enforceable in court", "A vested right exists only in international treaties"],
    0,
    "A vested right creates an immediate, fixed proprietary interest (certain to take effect); a contingent right depends upon an uncertain future contingency that may or may not occur.",
    {"A": "Correct. Vested is certain/immediate; contingent is conditional upon uncertainty.", "B": "Vested rights are fully heritable.", "C": "Contingent rights cannot be enforced until contingency happens.", "D": "Vested rights are fundamental in municipal property law."},
    "Easy", "Salmond on Jurisprudence", "Distinguish Vested from Contingent Rights."
)

# -------------------------------------------------------------
# CHAPTER 9: LEGAL PERSONALITY
# -------------------------------------------------------------

# top-jur-09-01: Natural Persons, Unborn, Dead & Animals
add_mcq(
    "mcq-jur-09-001", "ch-jur-09", "top-jur-09-01",
    "How does Jurisprudence define a 'Legal Person'?",
    ["Any biological human being who is alive", "Any being or entity whom the law regards as capable of bearing rights and duties", "Only citizens who possess the right to vote", "Only adult men of sound mind"],
    1,
    "In legal theory, a 'Person' is any entity recognized by the law as capable of holding legal rights and bearing legal duties, whether a biological human being, a corporation, or a religious idol.",
    {"A": "Biological humanity is neither necessary nor sufficient (slaves were humans but not persons; corporations are persons).", "B": "Correct. Capability of bearing rights and duties.", "C": "Minors and corporations are persons without voting rights.", "D": "Discriminatory and historically false."},
    "Easy", "Salmond on Jurisprudence", "Define Legal Personality."
)

add_mcq(
    "mcq-jur-09-002", "ch-jur-09", "top-jur-09-01",
    "What does the Latin legal fiction 'Nasciturus pro iam nato habetur' mean regarding an unborn child?",
    ["An unborn child has no rights whatsoever", "An unborn child is deemed to be already born whenever it is for its legal benefit", "An unborn child must pay taxes", "An unborn child is an adult in law"],
    1,
    "The civil law maxim 'Nasciturus pro iam nato habetur, quotiens de commodis eius agitur' means that a child in the mother's womb is deemed to be already born whenever its legal benefit or inheritance is concerned.",
    {"A": "Directly contradicts the doctrine.", "B": "Correct. Unborn child deemed born for its legal benefit.", "C": "No fiscal duties attach in utero.", "D": "Attains majority at 18."},
    "Easy", "Digest of Justinian / Salmond", "Recall the Nasciturus doctrine."
)

add_mcq(
    "mcq-jur-09-003", "ch-jur-09", "top-jur-09-01",
    "Can property be transferred for the benefit of an unborn person under Section 13 of the Transfer of Property Act 1882?",
    ["No, transfers to unborn persons are permanently prohibited", "Yes, provided it is preceded by a prior life estate in a living person and conveys the whole remaining interest", "Yes, directly without any prior interest", "Yes, but only for a period of 5 years"],
    1,
    "Section 13 TPA allows transfers for the benefit of an unborn person, provided a prior life interest is created in a living person by the same deed and the transfer conveys the entire absolute remaining interest.",
    {"A": "Section 13 expressly permits it.", "B": "Correct. Prior life estate + whole remaining interest.", "C": "Direct transfer violates Section 5.", "D": "Time limit is governed by Section 14."},
    "Medium", "Transfer of Property Act, Section 13", "Link personality of unborn child to Section 13 TPA."
)

add_mcq(
    "mcq-jur-09-004", "ch-jur-09", "top-jur-09-01",
    "What is the legal status of a deceased human being in jurisprudence?",
    ["A dead person remains a legal person until his will is probated", "A dead person is NOT a legal person; personality is extinguished upon biological death", "A dead person can be sued for contract breach", "A dead person can hold title to newly acquired property"],
    1,
    "Death terminates legal personality: 'Actio personalis moritur cum persona'. A deceased person has no rights and no duties. Posthumous protections (reputation, corpse, will) are enforced for the benefit of living relatives and public policy.",
    {"A": "Will is executed by living executors.", "B": "Correct. Personality is extinguished at death.", "C": "Suit lies against legal representatives, not the deceased.", "D": "Dead person cannot acquire property."},
    "Medium", "Salmond on Jurisprudence", "State legal status of deceased persons."
)

add_mcq(
    "mcq-jur-09-005", "ch-jur-09", "top-jur-09-01",
    "What does the maxim 'Actio personalis moritur cum persona' signify?",
    ["A personal right of action dies with the person", "The King never dies", "An act of court harms no one", "No one can transfer what he does not own"],
    0,
    "'Actio personalis moritur cum persona' means that a personal right of action (such as tortious defamation, assault, or personal injury) dies with the deceased and cannot be maintained post-death.",
    {"A": "Correct. Personal right of action dies with the person.", "B": "Rex nunquam moritur.", "C": "Actus curiae neminem gravabit.", "D": "Nemo dat quod non habet."},
    "Easy", "Legal Maxims — Broom", "Define Actio personalis moritur cum persona."
)

add_mcq(
    "mcq-jur-09-006", "ch-jur-09", "top-jur-09-01",
    "Are animals recognized as 'Legal Persons' under classical jurisprudence and modern positive law?",
    ["Yes, animals have constitutional rights under Article 14", "No, animals are objects of legal rights and duties, not legal subjects/persons", "Yes, domestic pets can execute wills", "Yes, horses can be sued for trespass in civil courts"],
    1,
    "In positive law, animals lack legal personality; they have no legal duties and cannot hold legal rights. Welfare laws protecting animals impose duties on humans owed to the state, not directly to the animal.",
    {"A": "Article 14 applies to persons.", "B": "Correct. Animals are objects of rights, not legal subjects.", "C": "Pets cannot execute instruments.", "D": "The owner is liable for animal trespass."},
    "Easy", "Salmond on Jurisprudence", "State legal status of animals."
)

add_mcq(
    "mcq-jur-09-007", "ch-jur-09", "top-jur-09-01",
    "In Hindu Law, what is the legal status of a consecrated Hindu Idol (Deity) according to the Privy Council and Supreme Court of India?",
    ["It is mere stone and has no legal status", "It is a recognized Juristic Person capable of holding property and suing/being sued through its Shebait or next friend", "It is an unincorporated association", "It is a government agency"],
    1,
    "In Pramatha Nath Mullick v. Pradyumna Kumar Mullick (1925 PC) and the Ayodhya Verdict (2019 SC), it is settled law that a consecrated Hindu Idol is a juristic person holding property and capable of suing through a Shebait or next friend.",
    {"A": "Religious idols are juristic entities once consecrated.", "B": "Correct. Consecrated Hindu Idol is a juristic person.", "C": "It is not an association.", "D": "It is not a government body."},
    "Medium", "Pramatha Nath Mullick v. Pradyumna Kumar Mullick, (1925) 52 IA 245", "Identify juristic personality of Hindu Idol."
)

add_mcq(
    "mcq-jur-09-008", "ch-jur-09", "top-jur-09-01",
    "Did the Privy Council recognize a 'Mosque' as a juristic person in Masjid Shahid Ganj v. Shiromani Gurdwara Parbandhak Committee (1940)?",
    ["Yes, a mosque is a juristic person identical to a Hindu idol", "No, a mosque is not a juristic person capable of holding property in its own name", "Yes, but only if built before 1857", "Yes, under the Waqf Act"],
    1,
    "In Masjid Shahid Ganj (1940 PC), the Privy Council held that while a Hindu idol is a juristic person, a mosque is a consecrated building dedicated to the Almighty and is NOT a separate juristic person capable of suing or holding property.",
    {"A": "Privy Council expressly rejected this analogy.", "B": "Correct. Mosque is not a juristic person.", "C": "Date of construction is irrelevant.", "D": "Waqf properties vest in the Almighty, managed by Mutawallis."},
    "Hard", "Masjid Shahid Ganj v. SGPC, AIR 1940 PC 116", "Recall Masjid Shahid Ganj ruling on mosques."
)

# top-jur-09-02: Corporate Personality & Theories
add_mcq(
    "mcq-jur-09-009", "ch-jur-09", "top-jur-09-02",
    "Which landmark 1897 House of Lords judgment established the bedrock doctrine of the independent legal personality of an incorporated company?",
    ["Salomon v. Salomon & Co. Ltd.", "Daimler Co. v. Continental Tyre Co.", "Lee v. Lee's Air Farming Ltd.", "Foss v. Harbottle"],
    0,
    "Salomon v. Salomon & Co. Ltd. (1897 AC 22) established that upon statutory incorporation, a company is a legal person entirely separate and distinct from its shareholders, directors, and incorporators.",
    {"A": "Correct. Salomon v. Salomon & Co. Ltd. (1897).", "B": "Piercing the veil for enemy character.", "C": "Director as employee of one-man company.", "D": "Majority rule and minority rights."},
    "Easy", "Salomon v. Salomon & Co. Ltd. (1897) AC 22", "Identify Salomon v. Salomon."
)

add_mcq(
    "mcq-jur-09-010", "ch-jur-09", "top-jur-09-02",
    "Who is the principal philosophical champion of the 'Realist Theory' (Organic Theory) of corporate personality?",
    ["Friedrich Carl von Savigny", "Otto von Gierke", "John Salmond", "Rudolf von Ihering"],
    1,
    "German jurist Otto von Gierke (supported in England by F.W. Maitland) championed the Realist Theory: a corporation is not a fictitious creation of the state, but a real, living, organic group-person (Gesamtperson) with its own real will and mind.",
    {"A": "Savigny championed the Fiction Theory.", "B": "Correct. Otto von Gierke propounded the Realist Theory.", "C": "Salmond supported the Fiction Theory.", "D": "Ihering propounded the Bracket Theory."},
    "Easy", "Otto von Gierke, Genossenschaftsrecht", "Identify Gierke and the Realist Theory."
)

add_mcq(
    "mcq-jur-09-011", "ch-jur-09", "top-jur-09-02",
    "According to the 'Fiction Theory' (Savigny, Salmond, Holland), what is the nature of corporate personality?",
    ["It is a real living organism like a human being", "It is an artificial creation of the sovereign state existing only in legal fiction", "It is a mathematical bracket", "It is an ownerless purpose"],
    1,
    "The Fiction Theory maintains that only natural human beings possess a real will and personality; a corporation has no real will, and its personality is an imaginary fiction created by the sovereign state.",
    {"A": "Realist Theory.", "B": "Correct. Fictitious creation of sovereign state.", "C": "Bracket Theory.", "D": "Purpose Theory (Brinz)."},
    "Medium", "Savigny, System of Modern Roman Law", "Define the Fiction Theory."
)

add_mcq(
    "mcq-jur-09-012", "ch-jur-09", "top-jur-09-02",
    "Who propounded the 'Bracket Theory' (Symbolist Theory) of corporate personality?",
    ["Rudolf von Ihering", "Hans Kelsen", "Alois von Brinz", "Otto von Gierke"],
    0,
    "Rudolf von Ihering propounded the Bracket Theory: corporate personality is merely a convenient algebraic bracket placed over a group of living human members to treat them as a unit; the bracket can be removed to see the real persons underneath.",
    {"A": "Correct. Rudolf von Ihering propounded the Bracket Theory.", "B": "Kelsen reduced personality to a bundle of norms.", "C": "Brinz propounded the Purpose Theory.", "D": "Gierke propounded the Realist Theory."},
    "Medium", "Ihering, Geist des römischen Rechts", "Identify Ihering's Bracket Theory."
)

add_mcq(
    "mcq-jur-09-013", "ch-jur-09", "top-jur-09-02",
    "The 'Purpose Theory' (Zweckvermögen) of corporate personality, propounded by Alois von Brinz, asserts that:",
    ["Corporations have a soul", "Corporations are not persons at all, but 'ownerless properties' dedicated to a specific socio-economic purpose", "Corporations are sovereign entities", "Corporations cannot hold property"],
    1,
    "Brinz's Purpose Theory posits that legal personality is unnecessary; property can exist without a human owner if it is dedicated as 'ownerless property' (Zweckvermögen) to a specific charitable or economic purpose.",
    {"A": "Metaphysical fantasy.", "B": "Correct. Ownerless property dedicated to a specific purpose.", "C": "Incorrect proposition.", "D": "Corporations hold dedicated property."},
    "Hard", "Alois von Brinz, Lehrbuch der Pandekten", "Explain Brinz's Purpose Theory."
)

add_mcq(
    "mcq-jur-09-014", "ch-jur-09", "top-jur-09-02",
    "What is an example of a 'Corporation Sole' in Anglo-Indian jurisprudence?",
    ["Tata Motors Limited", "The President of India or the Public Trustee", "The Bar Council of India", "A partnership firm"],
    1,
    "A Corporation Sole is an incorporated series of successive persons occupying a single official station (e.g. the President of India, Comptroller and Auditor General, Crown, Public Trustee). Corporation Aggregate consists of co-existing persons.",
    {"A": "Corporation aggregate (registered company).", "B": "Correct. President of India / Public Trustee is a Corporation Sole.", "C": "Statutory corporation aggregate.", "D": "Unincorporated association."},
    "Easy", "Salmond on Jurisprudence", "Identify Corporation Sole."
)

add_mcq(
    "mcq-jur-09-015", "ch-jur-09", "top-jur-09-02",
    "In which famous English wartime case did the court pierce the corporate veil to determine whether an English-registered company had acquired 'Enemy Character' because its shares were held by Germans?",
    ["Salomon v. Salomon", "Daimler Co. Ltd. v. Continental Tyre & Rubber Co. (Great Britain) Ltd.", "Gilford Motor Co. v. Horne", "Lee v. Lee's Air Farming"],
    1,
    "In Daimler Co. (1916 2 AC 307), the House of Lords pierced the corporate veil during World War I, holding that an English-incorporated company whose shares and control were in the hands of German enemy aliens possessed enemy character.",
    {"A": "Salomon established separate personality.", "B": "Correct. Daimler Co. pierced the veil for enemy character.", "C": "Gilford Motor pierced the veil for fraud/sham.", "D": "Lee upheld director's employee status."},
    "Medium", "Daimler Co. v. Continental Tyre Co., (1916) 2 AC 307", "Recall Daimler Co. and enemy character veil piercing."
)

add_mcq(
    "mcq-jur-09-016", "ch-jur-09", "top-jur-09-02",
    "Under what circumstances will Indian courts 'pierce or lift the corporate veil'?",
    ["In every case where a company suffers losses", "Where the corporate personality is used as a sham or cloak for fraud, tax evasion, or circumventing statutory duties", "Whenever a shareholder files a civil suit", "Only when the company is nationalized"],
    1,
    "In State of UP v. Renusagar Power Co. and Tata Engineering, the Supreme Court confirmed that courts will lift the corporate veil when the corporate facade is abused as a device for tax evasion, fraud, illegal conduct, or public interest.",
    {"A": "Commercial losses do not justify lifting the veil.", "B": "Correct. Fraud, tax evasion, sham, and public interest justify piercing the veil.", "C": "Shareholder suits are governed by company law.", "D": "Nationalization is unrelated."},
    "Easy", "State of U.P. v. Renusagar Power Co., (1988) 4 SCC 59", "State grounds for piercing the corporate veil."
)

# -------------------------------------------------------------
# CHAPTER 10: OWNERSHIP AND POSSESSION
# -------------------------------------------------------------

# top-jur-10-01: Possession: Corpus and Animus
add_mcq(
    "mcq-jur-09-017", "ch-jur-10", "top-jur-10-01",
    "In classical Roman law and analytical jurisprudence, what are the two indispensable constituents of legal Possession?",
    ["Title and Registration", "Corpus Possessionis (Physical Control) and Animus Possidendi (Mental Intention)", "Right and Remedy", "Command and Sanction"],
    1,
    "Possession requires two elements: (1) Corpus Possessionis (the objective physical power of control), and (2) Animus Possidendi (the subjective mental intention to exclude others).",
    {"A": "Title is for ownership.", "B": "Correct. Corpus and Animus.", "C": "Substantive elements of action.", "D": "Austin's elements of law."},
    "Easy", "Salmond on Jurisprudence", "Identify Corpus and Animus."
)

add_mcq(
    "mcq-jur-09-018", "ch-jur-10", "top-jur-10-01",
    "What specific mental element did Friedrich Carl von Savigny require to convert mere physical custody (detentio) into legal possession (possessio)?",
    ["Animus Revertendi", "Animus Domini (The intention to hold as absolute owner)", "Animus Possidendi (Mere intent to exclude)", "Animus Furandi"],
    1,
    "Savigny insisted on 'Animus Domini' — the mental intention to hold the property as absolute owner. Under Savigny's theory, bailees, pledgees, and tenants had mere custody (detentio) because they recognized another's ownership.",
    {"A": "Intention to return.", "B": "Correct. Savigny required Animus Domini (intent to hold as owner).", "C": "Salmond's modern replacement.", "D": "Intention to steal in theft."},
    "Medium", "Savigny, Das Recht des Besitzes (Treatise on Possession)", "Recall Savigny's Animus Domini requirement."
)

add_mcq(
    "mcq-jur-09-019", "ch-jur-10", "top-jur-09-01",
    "How did Rudolf von Ihering's 'Objective Theory' of possession critique Savigny's subjective theory?",
    ["Ihering argued that whenever observable corpus (physical control) exists, law presumes possession unless statute explicitly denies it for policy reasons", "Ihering argued possession requires no physical control", "Ihering argued animals possess land", "Ihering denied the existence of possession"],
    0,
    "Ihering rejected Savigny's animus domini as an artificial Roman illusion, arguing that corpus implies the normal animus; whenever external physical relationship exists, law protects possession unless denied by statute.",
    {"A": "Correct. Ihering's Objective Theory of possession.", "B": "Corpus is central to Ihering.", "C": "Animals lack legal capacity.", "D": "Ihering wrote extensively on possession."},
    "Medium", "Ihering, Der Besitzwille", "Explain Ihering's Objective Theory of possession."
)

add_mcq(
    "mcq-jur-09-020", "ch-jur-10", "top-jur-09-01",
    "What landmark 1722 common law decision established that a finder of a lost chattel acquires possessory title good against all the world except the true owner?",
    ["Armory v. Delamirie", "Bridges v. Hawkesworth", "South Staffordshire Water Co. v. Sharman", "Elwes v. Brigg Gas Co."],
    0,
    "In Armory v. Delamirie (1722 1 Stra 505), a chimney sweeper's boy found a jewel and gave it to a goldsmith for valuation. The court held the finder had possessory title against all the world except the rightful owner.",
    {"A": "Correct. Armory v. Delamirie (1722).", "B": "Notes dropped in public shop.", "C": "Rings found in mud at bottom of pool.", "D": "Prehistoric boat buried in land."},
    "Easy", "Armory v. Delamirie (1722) 1 Stra 505", "Recall Armory v. Delamirie."
)

add_mcq(
    "mcq-jur-09-021", "ch-jur-10", "top-jur-09-01",
    "Why was the shopkeeper in Bridges v. Hawkesworth (1851) NOT entitled to bank notes dropped on the floor of his shop by a stranger?",
    ["The notes were counterfeit", "The notes were dropped in the public part of the shop where the shopkeeper had never manifested an intention (animus) to exercise exclusive control over lost chattels before discovery", "The finder was a police officer", "The shop was closed"],
    1,
    "Patteson J held that notes dropped in a public shop were not in the shopkeeper's custody before being picked up, because the shopkeeper had no animus to control lost items in public areas prior to discovery; the finder's title prevailed.",
    {"A": "Notes were genuine.", "B": "Correct. Lack of prior animus to control items in public part of shop.", "C": "Finder was a customer.", "D": "Shop was open to public."},
    "Medium", "Bridges v. Hawkesworth (1851) 21 LJ QB 75", "Explain ruling in Bridges v. Hawkesworth."
)

add_mcq(
    "mcq-jur-09-022", "ch-jur-10", "top-jur-09-01",
    "How does 'Mediate Possession' differ from 'Immediate Possession' in Salmond's classification?",
    ["Mediate possession is held through another person (e.g. landlord possessing through tenant); immediate possession is held directly by oneself", "Mediate possession is held by courts; immediate by police", "Mediate possession is illegal; immediate is legal", "Mediate possession applies only to money"],
    0,
    "Salmond classified possession into: (1) Immediate (direct physical holding by oneself), and (2) Mediate (indirect possession held through a servant, agent, bailee, or tenant).",
    {"A": "Correct. Mediate = through another; Immediate = direct personal holding.", "B": "Judicial/police administration.", "C": "Both can be legal.", "D": "Applies to all property."},
    "Easy", "Salmond on Jurisprudence", "Distinguish Mediate from Immediate Possession."
)

add_mcq(
    "mcq-jur-09-023", "ch-jur-10", "top-jur-09-01",
    "What is the legal status of a servant holding his master's silver cutlery?",
    ["The servant has full legal possession", "The servant has mere physical custody (detentio); legal possession remains in the master", "The servant is a bailee", "The servant is an ostensible owner"],
    1,
    "A servant holds goods on behalf of his master; he has mere physical custody (detentio), while constructive and legal possession remains at all times in the master.",
    {"A": "Servant lacks animus possidendi for himself.", "B": "Correct. Servant has mere custody; possession remains in master.", "C": "Bailment requires independent contractual possession.", "D": "Servant is not ostensible owner."},
    "Easy", "Salmond on Jurisprudence", "Distinguish custody from legal possession."
)

add_mcq(
    "mcq-jur-09-024", "ch-jur-09", "top-jur-09-01",
    "Which section of the Specific Relief Act, 1963 provides a summary possessory remedy allowing a dispossessed person to recover immovable property within 6 months, irrespective of title?",
    ["Section 5", "Section 6", "Section 9", "Section 34"],
    1,
    "Section 6 of the Specific Relief Act 1963 provides a summary remedy: anyone dispossessed of immovable property without consent and otherwise than in due course of law may sue within 6 months to recover possession, regardless of any other title.",
    {"A": "Section 5 is recovery based on title.", "B": "Correct. Section 6 provides summary possessory remedy.", "C": "Section 9 is defenses to contract.", "D": "Section 34 is declaratory decrees."},
    "Easy", "Specific Relief Act, 1963, Section 6", "Identify Section 6 Specific Relief Act."
)

# top-jur-10-02: Concept of Ownership
add_mcq(
    "mcq-jur-09-025", "ch-jur-10", "top-jur-10-02",
    "Who defined Ownership as 'a right over a determinate thing, indefinite in point of user, unrestricted in point of disposition, and unlimited in point of duration'?",
    ["Sir John Salmond", "John Austin", "Thomas Erskine Holland", "Markby"],
    1,
    "John Austin formulated this classic analytical definition of ownership in his 'Lectures on Jurisprudence': indefinite user, unrestricted disposition, and unlimited duration.",
    {"A": "Salmond propounded the bundle of rights theory.", "B": "Correct. John Austin's celebrated definition.", "C": "Holland defined it as plenary control.", "D": "Markby analyzed ownership components."},
    "Easy", "Austin, Lectures on Jurisprudence", "Recall Austin's definition of Ownership."
)

add_mcq(
    "mcq-jur-09-026", "ch-jur-09", "top-jur-10-02",
    "Who propounded the 'Bundle of Rights' theory of ownership in English jurisprudence?",
    ["Sir John Salmond", "Jeremy Bentham", "Hans Kelsen", "H.L.A. Hart"],
    0,
    "Sir John Salmond characterized ownership as a complex 'bundle of rights' (rights to possess, use, manage, consume, alienate, and exclude others), emphasizing its residual character.",
    {"A": "Correct. Salmond's Bundle of Rights theory.", "B": "Bentham analyzed utility of property.", "C": "Kelsen analyzed normative hierarchy.", "D": "Hart analyzed rules."},
    "Easy", "Salmond on Jurisprudence", "Identify Salmond's Bundle of Rights theory."
)

add_mcq(
    "mcq-jur-09-027", "ch-jur-10", "top-jur-10-02",
    "What is the 'Residual Character' of Ownership according to Salmond?",
    ["Ownership expires when property is abandoned", "Whenever lesser encumbrances, leases, or easements terminate, the full rights automatically expand and collapse back into the owner's title", "Ownership can never be transferred", "The state takes residual property"],
    1,
    "Salmond explained the residual nature of ownership: an owner may grant away many sticks from the bundle (e.g. lease, mortgage, easement), but when those limited interests expire, full unencumbered ownership automatically re-emerges in the owner.",
    {"A": "Abandonment is res derelicta.", "B": "Correct. Encumbrances expire and automatically revert to owner's root title.", "C": "Ownership is alienable.", "D": "Escheat occurs only without heirs."},
    "Medium", "Salmond on Jurisprudence", "Define Residual Character of Ownership."
)

add_mcq(
    "mcq-jur-09-028", "ch-jur-09", "top-jur-09-02",
    "What is 'Incorporeal Ownership' in Salmond's taxonomy?",
    ["Ownership of tangible physical land or cattle", "Ownership over intangible property or legal rights, such as patents, copyrights, trademarks, or goodwill", "Ownership by a corporation sole", "Ownership of minerals deep underground"],
    1,
    "Corporeal ownership is ownership of physical tangible objects (land, chattels). Incorporeal ownership is ownership of intangible rights and intellectual property (patents, copyrights, trademarks, actionable claims).",
    {"A": "Corporeal ownership.", "B": "Correct. Incorporeal ownership = Intangibles and intellectual property rights.", "C": "Institutional entity.", "D": "Corporeal sub-surface property."},
    "Easy", "Salmond on Jurisprudence", "Define Incorporeal Ownership."
)

add_mcq(
    "mcq-jur-09-029", "ch-jur-09", "top-jur-09-02",
    "How does English equity recognize dual ownership in a Trust?",
    ["The Trustee has Legal Ownership; the Beneficiary has Equitable/Beneficial Ownership", "The Court has legal ownership; the police have beneficial ownership", "There is no dual ownership in a trust", "The state owns trust assets"],
    0,
    "English law recognizes dual ownership: the Trustee holds the formal 'Legal Title/Ownership' (governed by common law), while the Beneficiary holds the 'Equitable or Beneficial Ownership' (protected by equity courts).",
    {"A": "Correct. Trustee = Legal Owner; Beneficiary = Equitable Owner.", "B": "Courts and police do not hold trust assets.", "C": "Dual ownership is the foundation of trusts in Anglo-American law.", "D": "State does not own private trust property."},
    "Easy", "Underhill and Hayton, Law of Trusts and Trustees", "Explain dual ownership in trusts."
)

add_mcq(
    "mcq-jur-09-030", "ch-jur-09", "top-jur-09-02",
    "What is the Latin maxim expressing the ancient principle that whoever owns the soil owns everything up to the heavens and down to the center of the earth?",
    ["Cuius est solum, eius est usque ad coelum et ad inferos", "Sic utere tuo ut alienum non laedas", "Nemo dat quod non habet", "Quicquid plantatur solo, solo cedit"],
    0,
    "'Cuius est solum, eius est usque ad coelum et ad inferos' (Whoever owns the soil owns up to the heavens and down to the depths of hell) expressed classical unlimited vertical ownership of land.",
    {"A": "Correct. Cuius est solum maxim.", "B": "Use your own property so as not to injure another.", "C": "No one can transfer what he does not own.", "D": "Whatever is affixed to the soil belongs to the soil."},
    "Easy", "Broom's Legal Maxims", "Identify Cuius est solum maxim."
)

add_mcq(
    "mcq-jur-09-031", "ch-jur-09", "top-jur-09-02",
    "Why has Austin's definition of ownership as 'indefinite in point of user' been rejected in modern welfare states?",
    ["Because land no longer exists", "Because zoning laws, environmental regulations, town planning acts, and building codes severely restrict how an owner may use his land", "Because all property is owned by the United Nations", "Because Austin was not a lawyer"],
    1,
    "Modern environmental protection laws, urban development acts, rent control, and planning regulations prevent 'indefinite user'; an owner cannot build whatever he wants or pollute the air on his land.",
    {"A": "Absurd.", "B": "Correct. Regulatory welfare state severely restricts indefinite user.", "C": "UN has no municipal land ownership.", "D": "Austin was an English barrister and professor."},
    "Medium", "Dias on Jurisprudence", "Critique Austin's indefinite user of ownership."
)

add_mcq(
    "mcq-jur-09-032", "ch-jur-09", "top-jur-09-02",
    "In State of West Bengal v. Subodh Gopal Bose (1954), how did the Supreme Court of India characterize property ownership?",
    ["As a single indivisible physical entity", "As a bundle of rights which includes the right of possession, user, disposition, and destruction", "As an absolute sovereign power above the Constitution", "As a temporary license granted by the Collector"],
    1,
    "Patanjali Sastri CJ confirmed that property in legal sense is not merely the physical thing, but a bundle of rights including user, enjoyment, possession, and disposition.",
    {"A": "Indivisible physical view rejected.", "B": "Correct. Property is a bundle of rights.", "C": "Property is subject to constitutional law.", "D": "Fee simple is not a temporary license."},
    "Medium", "State of West Bengal v. Subodh Gopal Bose, AIR 1954 SC 92", "Recall Subodh Gopal Bose on bundle of rights."
)

# top-jur-10-03: Ownership vs Possession & Remedies
add_mcq(
    "mcq-jur-09-033", "ch-jur-10", "top-jur-10-03",
    "How did Sir John Salmond famously summarize the conceptual contrast between Possession and Ownership?",
    ["Possession is criminal; ownership is civil", "Possession is the de facto exercise of a claim; ownership is the de jure recognition of one", "Possession is temporary; ownership lasts only 10 years", "Possession is unwritten; ownership is always registered"],
    1,
    "Salmond observed: 'Possession is the de facto exercise of a claim; ownership is the de jure recognition of one. What possession is in the world of fact, ownership is in the world of law.'",
    {"A": "Both are private law civil concepts.", "B": "Correct. Possession is de facto; ownership is de jure.", "C": "Ownership is perpetual.", "D": "Movable property ownership is unwritten."},
    "Easy", "Salmond on Jurisprudence", "Recall Salmond's de facto vs de jure aphorism."
)

add_mcq(
    "mcq-jur-09-034", "ch-jur-10", "top-jur-10-03",
    "Which section of the Indian Evidence Act, 1872 enacts that possession is prima facie evidence of ownership, placing the burden of proof on the person who denies it?",
    ["Section 105", "Section 110", "Section 114", "Section 115"],
    1,
    "Section 110 of the Indian Evidence Act provides that when a person is shown to be in possession of anything, the burden of proving that he is not the owner is on the person who affirms that he is not the owner.",
    {"A": "Section 105 is burden of proving general exceptions in penal law.", "B": "Correct. Section 110: Presumption of ownership from possession.", "C": "Section 114 is court may presume existence of certain facts.", "D": "Section 115 is estoppel."},
    "Easy", "Indian Evidence Act, 1872, Section 110", "Identify Section 110 Evidence Act."
)

add_mcq(
    "mcq-jur-09-035", "ch-jur-10", "top-jur-10-03",
    "What are the three Latin essentials required to establish title by Adverse Possession against the true owner?",
    ["Nec vi, nec clam, nec precario", "Actus reus, mens rea, and corpus", "Uberrimae fidei, consensus, and consideration", "Pendente lite, res judicata, and stare decisis"],
    0,
    "To mature into adverse possession, the possession must be 'Nec vi, nec clam, nec precario' — adequate in continuity, in publicity, and in extent (without force, without secrecy, and without permission/license).",
    {"A": "Correct. Nec vi, nec clam, nec precario.", "B": "Criminal elements.", "C": "Contractual elements.", "D": "Procedural doctrines."},
    "Easy", "Karnataka Board of Wakf v. Bharat IT, (2004) 10 SCC 779", "Identify elements of Adverse Possession."
)

add_mcq(
    "mcq-jur-09-036", "ch-jur-10", "top-jur-10-03",
    "What is the statutory limitation period under Article 65 of the Limitation Act, 1963 to recover possession of immovable property based on title against an adverse possessor?",
    ["3 years", "6 years", "12 years", "30 years"],
    2,
    "Article 65 of the Limitation Act 1963 provides a limitation period of 12 years to recover possession of private immovable property, after which the owner's title is extinguished under Section 27.",
    {"A": "3 years is for money suits.", "B": "6 years is residuary limitation.", "C": "Correct. 12 years for adverse possession against private land.", "D": "30 years applies against the Government (Article 112)."},
    "Easy", "Limitation Act, 1963, Article 65", "Recall limitation period for adverse possession."
)

add_mcq(
    "mcq-jur-09-037", "ch-jur-10", "top-jur-10-03",
    "What is the limitation period for adverse possession when the immovable property belongs to the Central or State Government (Article 112, Limitation Act 1963)?",
    ["12 years", "20 years", "30 years", "60 years"],
    2,
    "Under Article 112 of the Limitation Act 1963, the limitation period for suits by or on behalf of the Central Government or any State Government is 30 years.",
    {"A": "12 years is against private individuals.", "B": "20 years is easement prescription.", "C": "Correct. 30 years against the Government.", "D": "Old 1908 Limitation Act was 60 years; reduced to 30 years in 1963 Act."},
    "Medium", "Limitation Act, 1963, Article 112", "Recall limitation period against government land."
)

add_mcq(
    "mcq-jur-09-038", "ch-jur-10", "top-jur-09-03",
    "What is the effect of Section 27 of the Limitation Act, 1963 upon the expiration of the limitation period for recovering property?",
    ["The remedy is barred but the right of ownership survives", "The right to such property is extinguished (extinction of title)", "The property automatically vests in the President of India", "The possessor is sent to civil prison"],
    1,
    "Unlike ordinary limitation (which bars only the procedural remedy, keeping the right alive as an imperfect right), Section 27 is substantive: at the determination of the period, the original owner's right to the property is completely extinguished.",
    {"A": "True of ordinary debts, but false for property under Section 27.", "B": "Correct. Section 27 extinguishes the property right itself.", "C": "Escheat.", "D": "No penal imprisonment."},
    "Medium", "Limitation Act, 1963, Section 27", "Explain Section 27 extinction of title."
)

add_mcq(
    "mcq-jur-09-039", "ch-jur-10", "top-jur-10-03",
    "In which landmark 3-Judge Bench judgment in 2019 did the Supreme Court overrule Gurdwara Sahib and hold that Adverse Possession can be used by a plaintiff as a 'Sword' to seek declaration of title?",
    ["Ravinder Kaur Grewal v. Manjit Kaur", "Balkrishan v. Satyaprakash", "T. Anjanappa v. Somalingappa", "P.T. Munichikkanna Reddy v. Revamma"],
    0,
    "In Ravinder Kaur Grewal (2019 8 SCC 729), the Supreme Court ruled that a person who has perfected title by adverse possession can use it not only as a defense (shield), but also as a plaintiff (sword) to obtain declaration of title and injunction.",
    {"A": "Correct. Ravinder Kaur Grewal v. Manjit Kaur (2019).", "B": "Balkrishan concerned animus.", "C": "Anjanappa concerned hostile possession.", "D": "Munichikkanna concerned mental intention."},
    "Hard", "Ravinder Kaur Grewal v. Manjit Kaur, (2019) 8 SCC 729", "Recall Ravinder Kaur Grewal adverse possession landmark."
)

add_mcq(
    "mcq-jur-09-040", "ch-jur-10", "top-jur-10-03",
    "What is the legal defense of 'Jus Tertii' in possessory litigation?",
    ["Pleading that the plaintiff owns the property", "Pleading that neither the plaintiff nor the defendant owns the property, but that title belongs to an independent third party", "Claiming diplomatic immunity", "Pleading self-defense"],
    1,
    "'Jus Tertii' is the defense raised by a wrongdoer asserting that legal title belongs to a third party (tertius). In possessory suits, the defense of jus tertii is barred: a wrongdoer who dispossesses a peaceful possessor cannot justify his wrong by setting up another's title.",
    {"A": "Admission of plaintiff's title.", "B": "Correct. Jus Tertii = Claiming title belongs to a third party.", "C": "Diplomatic immunity.", "D": "Private defense."},
    "Medium", "Salmond on the Law of Torts", "Define Jus Tertii."
)

# -------------------------------------------------------------
# CHAPTER 11: LIABILITY AND ADMINISTRATION OF JUSTICE
# -------------------------------------------------------------

# top-jur-11-01: Nature of Legal Liability: Acts, Mens Rea, Negligence
add_mcq(
    "mcq-jur-11-001", "ch-jur-11", "top-jur-11-01",
    "How did Sir John Salmond define Legal Liability (or Responsibility)?",
    ["The physical punishment inflicted by prisons", "The bond of necessity that exists between the wrongdoer and the remedy of the wrong", "The command of the sovereign", "The social solidarity of citizens"],
    1,
    "Salmond defined liability as 'the bond of necessity that exists between the wrongdoer and the remedy of the wrong'. A person is liable when his breach of duty triggers the coercive legal sanction of the state.",
    {"A": "Penal sanction.", "B": "Correct. Salmond's 'bond of necessity' definition.", "C": "Austin's command.", "D": "Duguit's solidarity."},
    "Easy", "Salmond on Jurisprudence", "Recall Salmond's definition of liability."
)

add_mcq(
    "mcq-jur-11-002", "ch-jur-11", "top-jur-11-01",
    "According to Salmond, what are the three integral components of an 'Act' in jurisprudence?",
    ["Volition (Muscular contraction), Circumstances, and Consequences", "Motive, Intention, and Malice", "Offer, Acceptance, and Consideration", "Command, Duty, and Sanction"],
    0,
    "Salmond analyzed an act into three elements: (1) Its origin in bodily volition (muscular movement), (2) The surrounding circumstances, and (3) The resulting consequences in the external world.",
    {"A": "Correct. Volition, Circumstances, and Consequences.", "B": "Mental states of liability.", "C": "Contractual formation.", "D": "Imperative elements."},
    "Medium", "Salmond on Jurisprudence", "Identify Salmond's 3 components of an act."
)

add_mcq(
    "mcq-jur-11-003", "ch-jur-11", "top-jur-11-01",
    "What fundamental maxim of penal jurisprudence governs the requirement of a blameworthy mental state for criminal liability?",
    ["Ubi jus ibi remedium", "Actus non facit reum nisi mens sit rea", "Volenti non fit injuria", "Res ipsa loquitur"],
    1,
    "'Actus non facit reum nisi mens sit rea' (An act does not make a person guilty unless his mind is also guilty) is the bedrock maxim of criminal jurisprudence.",
    {"A": "Civil right/remedy maxim.", "B": "Correct. Actus non facit reum nisi mens sit rea.", "C": "Voluntary consent defense.", "D": "Rule of evidence in tort."},
    "Easy", "Coke's Third Institute / Glanville Williams", "Identify the fundamental penal maxim on Mens Rea."
)

add_mcq(
    "mcq-jur-11-004", "ch-jur-11", "top-jur-11-01",
    "What is the crucial legal distinction between 'Intention' and 'Motive' in criminal jurisprudence?",
    ["Intention is the immediate aim and purpose of the act; Motive is the ultimate ulterior desire that induced the intention", "Intention is emotional; Motive is rational", "Intention is irrelevant in criminal law; Motive alone decides guilt", "There is no legal difference between them"],
    0,
    "Intention refers to the immediate foresight and desire of the consequences of the act (means/ends). Motive is the ultimate ulterior cause or desire that moved the actor (e.g. stealing bread = intention is theft, motive is feeding starving child). Guilt depends on intention; motive is relevant to sentencing.",
    {"A": "Correct. Intention = immediate aim; Motive = ultimate ulterior purpose.", "B": "Both have rational/emotional elements.", "C": "Intention determines guilt; motive is not essential element of offense.", "D": "They are fundamentally distinct."},
    "Medium", "Salmond on Jurisprudence", "Distinguish Intention from Motive."
)

add_mcq(
    "mcq-jur-11-005", "ch-jur-11", "top-jur-11-01",
    "How did Sir John Salmond and Austin view the nature of 'Negligence' in their 'Subjective Theory'?",
    ["Negligence is an objective failure to follow statutory codes", "Negligence is a blameworthy state of mind — a culpable state of indifference, inadvertence, or carelessness", "Negligence is identical to intentional murder", "Negligence exists only in contract breach"],
    1,
    "Salmond championed the Subjective Theory of negligence: negligence is not external conduct, but a mental attitude of carelessness, inadvertence, or indifference towards the consequences of one's actions.",
    {"A": "Objective theory of Holmes/Pollock.", "B": "Correct. Salmond's Subjective Theory: Negligence is a mental state.", "C": "Negligence excludes intentional malice.", "D": "Negligence is central to tort and criminal law."},
    "Medium", "Salmond on Jurisprudence", "Explain Salmond's Subjective Theory of Negligence."
)

add_mcq(
    "mcq-jur-11-006", "ch-jur-11", "top-jur-11-01",
    "Who championed the 'Objective Theory' of negligence, defining negligence as the breach of an objective duty of care judged by the standard of the 'Reasonable Man' (Bonus paterfamilias)?",
    ["Sir John Salmond", "Oliver Wendell Holmes Jr. and Sir Frederick Pollock", "Hans Kelsen", "Jeremy Bentham"],
    1,
    "Holmes and Pollock established the Objective Theory dominating modern tort law: negligence is not a subjective state of mind, but an objective failure of conduct falling below the standard of the prudent reasonable man.",
    {"A": "Salmond championed subjective theory.", "B": "Correct. Holmes and Pollock championed the Objective Theory.", "C": "Kelsen analyzed pure norms.", "D": "Bentham analyzed utility."},
    "Easy", "Holmes, The Common Law / Pollock on Torts", "Identify proponents of Objective Theory of Negligence."
)

add_mcq(
    "mcq-jur-11-007", "ch-jur-11", "top-jur-11-01",
    "What landmark 1932 House of Lords decision established the independent tort of negligence based on Lord Atkin's 'Neighbour Principle'?",
    ["Rylands v. Fletcher", "Donoghue v. Stevenson", "Ashby v. White", "Hadley v. Baxendale"],
    1,
    "In Donoghue v. Stevenson (1932 AC 562), Lord Atkin formulated the universal 'Neighbour Principle': you must take reasonable care to avoid acts or omissions which you can reasonably foresee would be likely to injure your neighbour.",
    {"A": "Strict liability.", "B": "Correct. Donoghue v. Stevenson (1932 AC 562).", "C": "Injuria sine damno.", "D": "Contract damages."},
    "Easy", "Donoghue v. Stevenson, (1932) AC 562", "Recall Donoghue v. Stevenson."
)

add_mcq(
    "mcq-jur-11-008", "ch-jur-11", "top-jur-11-01",
    "In criminal law, what degree of mental culpability occupies the middle ground between intentional malice and simple negligence, involving conscious risk-taking?",
    ["Recklessness", "Accident", "Absolute innocence", "Strict liability"],
    0,
    "Recklessness is the conscious taking of an unjustified, unreasonable risk: the actor foresees the dangerous consequence as probable, but callously persists in the act regardless of the risk (e.g. driving at 120 mph through a crowded bazaar).",
    {"A": "Correct. Recklessness = Conscious foresight and running of unjustified risk.", "B": "Accident excludes culpability.", "C": "Innocence.", "D": "Strict liability dispenses with mens rea."},
    "Medium", "Glanville Williams, Textbook of Criminal Law", "Define Recklessness."
)

# top-jur-11-02: Strict, Absolute & Vicarious Liability
add_mcq(
    "mcq-jur-11-009", "ch-jur-11", "top-jur-11-02",
    "Which landmark 1868 English judgment established the common law rule of 'Strict Liability' for the escape of dangerous things brought onto land?",
    ["Rylands v. Fletcher", "Donoghue v. Stevenson", "M.C. Mehta v. Union of India", "Derry v. Peek"],
    0,
    "In Rylands v. Fletcher (1868 LR 3 HL 330), Blackburn J laid down that a person who brings on his land and keeps there anything likely to do mischief if it escapes, must keep it at his peril, and is strictly answerable for natural damage upon escape.",
    {"A": "Correct. Rylands v. Fletcher (1868).", "B": "Negligence neighbour principle.", "C": "Indian absolute liability landmark.", "D": "Fraud deceit rule."},
    "Easy", "Rylands v. Fletcher, (1868) LR 3 HL 330", "Recall Rylands v. Fletcher."
)

add_mcq(
    "mcq-jur-11-010", "ch-jur-11", "top-jur-11-02",
    "Which of the following is NOT one of the recognized common law defenses to the rule of Strict Liability in Rylands v. Fletcher?",
    ["Act of God (Vis Major)", "Plaintiff's own default or consent", "Act of an unknown stranger", "Exercise of reasonable care by the defendant"],
    3,
    "Because liability in Rylands v. Fletcher is STRICT (no fault), the absence of negligence or taking of 'reasonable care' is NO DEFENSE. The recognized defenses are: Act of God, Plaintiff's fault, Consent, Act of stranger, and Statutory authority.",
    {"A": "Act of God is an established defense.", "B": "Plaintiff's fault/consent is an established defense.", "C": "Act of stranger is an established defense.", "D": "Correct. Reasonable care is NOT a defense to strict liability."},
    "Medium", "Salmond on Torts", "Identify defenses to Rylands v. Fletcher."
)

add_mcq(
    "mcq-jur-11-011", "ch-jur-11", "top-jur-11-02",
    "In which historic 1987 decision did the Supreme Court of India formulate the indigenous doctrine of 'Absolute Liability', holding that hazardous industries have zero defenses?",
    ["Bhopal Gas Leak Case (Union Carbide)", "M.C. Mehta v. Union of India (Oleum Gas Leak Case)", "Vellore Citizens Welfare Forum v. UOI", "Subhash Kumar v. State of Bihar"],
    1,
    "In M.C. Mehta v. Union of India (1987 1 SCC 395), Chief Justice P.N. Bhagwati refused to follow the 19th-century English rule of Rylands v. Fletcher, creating the stricter rule of 'Absolute Liability' without any exceptions for hazardous industries.",
    {"A": "Union Carbide settlement case.", "B": "Correct. M.C. Mehta (Oleum Gas Leak Case, 1987).", "C": "Precautionary principle landmark.", "D": "Right to clean water landmark."},
    "Easy", "M.C. Mehta v. Union of India, (1987) 1 SCC 395", "Identify M.C. Mehta and Absolute Liability."
)

add_mcq(
    "mcq-jur-11-012", "ch-jur-11", "top-jur-11-02",
    "How does the Indian doctrine of 'Absolute Liability' differ essentially from English 'Strict Liability'?",
    ["Absolute liability applies only to government departments", "Absolute liability permits NO DEFENSES whatsoever (not even Act of God or act of stranger), does not require 'escape', and damages are proportional to the enterprise's financial capacity", "Absolute liability requires proof of intentional malice", "Absolute liability applies only to criminal cases"],
    1,
    "Absolute Liability differs from Rylands in three cardinal respects: (1) Zero exceptions/defenses allowed, (2) No requirement of 'escape' from premises, and (3) Measure of compensation is exemplary, scaled to the financial capacity of the enterprise.",
    {"A": "Applies to private hazardous industries.", "B": "Correct. Zero defenses, no escape needed, damages scaled to enterprise capacity.", "C": "It is liability without fault.", "D": "It is a civil tort doctrine."},
    "Medium", "M.C. Mehta v. Union of India, (1987) 1 SCC 395", "Compare Strict and Absolute Liability."
)

add_mcq(
    "mcq-jur-11-013", "ch-jur-11", "top-jur-11-02",
    "What classic Latin maxim forms the foundation of Vicarious Liability, declaring that 'he who acts through another is deemed in law to do it himself'?",
    ["Qui facit per alium facit per se", "Respondeat superior", "Volenti non fit injuria", "Ex turpi causa non oritur actio"],
    0,
    "'Qui facit per alium facit per se' (He who does an act through another does it himself) is the principal legal maxim governing the law of agency and master-servant vicarious liability.",
    {"A": "Correct. Qui facit per alium facit per se.", "B": "Respondeat superior means let the master be answerable.", "C": "Consent defense.", "D": "No cause of action from illegal transaction."},
    "Easy", "Salmond on the Law of Torts", "Identify Qui facit per alium maxim."
)

add_mcq(
    "mcq-jur-11-014", "ch-jur-11", "top-jur-11-02",
    "What does the maxim 'Respondeat Superior' mean in the context of employer vicarious liability?",
    ["Let the superior officer be immune", "Let the superior (master) be held responsible", "A servant has no legal rights", "Superior courts override subordinate courts"],
    1,
    "'Respondeat Superior' means 'Let the principal/master be responsible'. It is grounded in the deep pocket theory and social insurance: the master sets the hazardous enterprise in motion and profits from it, so he must bear the risk of his servant's torts.",
    {"A": "Sovereign immunity concept.", "B": "Correct. Let the master be answerable.", "C": "Servant holds legal status.", "D": "Appellate hierarchy."},
    "Easy", "Winfield and Jolowicz on Tort", "Define Respondeat Superior."
)

add_mcq(
    "mcq-jur-11-015", "ch-jur-11", "top-jur-11-02",
    "To hold an employer vicariously liable for the tort of an employee, what two conditions must be established?",
    ["The employee was poor, and the employer was rich", "A master-servant relationship existed, and the tort was committed in the 'course of employment'", "The employee had criminal intent, and the employer approved the crime", "The employer was physically present at the scene of the tort"],
    1,
    "The two universal essentials of vicarious liability are: (1) A contract of service establishing a Master-Servant relationship (distinguished from an independent contractor), and (2) The tort was committed within the 'Course of Employment'.",
    {"A": "Economic status alone does not create liability.", "B": "Correct. Master-servant relationship + course of employment.", "C": "Unauthorized modes of doing authorized acts bind master even without criminal intent.", "D": "Physical presence is not required."},
    "Easy", "Salmond on Torts", "Recall the two essentials of vicarious liability."
)

add_mcq(
    "mcq-jur-11-016", "ch-jur-11", "top-jur-11-02",
    "In State of Rajasthan v. Vidhyawati (1962), what did the Supreme Court of India hold regarding the State's vicarious liability for torts of government drivers?",
    ["The State enjoys absolute sovereign immunity and can never be sued", "The State is vicariously liable for the negligent driving of its employees engaged in non-sovereign administrative acts", "Government drivers have personal immunity", "Only the President can be sued"],
    1,
    "Sinha CJ established that the state cannot claim immunity for the tortious acts of its employees when engaged in ordinary administrative acts (such as driving a government jeep from a repair workshop), restricting the old doctrine of sovereign immunity.",
    {"A": "Kasturi Lal later revived immunity for pure sovereign functions (seized gold).", "B": "Correct. State is vicariously liable for non-sovereign negligence.", "C": "Drivers are joint tortfeasors.", "D": "State is sued under Article 300."},
    "Medium", "State of Rajasthan v. Vidhyawati, AIR 1962 SC 933", "Recall State of Rajasthan v. Vidhyawati landmark."
)

# top-jur-11-03: Administration of Justice & Theories of Punishment
add_mcq(
    "mcq-jur-11-017", "ch-jur-11", "top-jur-11-03",
    "According to Sir John Salmond, what is the primary and essential function of the State?",
    ["Religious propagation", "The Administration of Justice through the physical force of the state", "Economic banking", "Foreign military conquest"],
    1,
    "Salmond defined the administration of justice as 'the maintenance of right within a political community by means of the physical force of the state', declaring it the primary and indispensable function of political society.",
    {"A": "Theocratic state.", "B": "Correct. Administration of justice through state physical force.", "C": "Economic enterprise.", "D": "Imperialism."},
    "Easy", "Salmond on Jurisprudence", "Identify primary state function in Salmond."
)

add_mcq(
    "mcq-jur-11-018", "ch-jur-11", "top-jur-11-03",
    "Who is the leading philosophical champion of the 'Deterrent Theory' of punishment, relying on the 'hedonistic calculus' of pain and pleasure?",
    ["Immanuel Kant", "Jeremy Bentham", "Karl Marx", "G.W.F. Hegel"],
    1,
    "Jeremy Bentham championed the Deterrent Theory: punishment is an evil, but justified if it prevents greater future evils; the pain of punishment must be calculated to outweigh the anticipated pleasure of the crime.",
    {"A": "Kant championed retributive justice.", "B": "Correct. Jeremy Bentham's deterrent utilitarian calculus.", "C": "Marx viewed crime as rooted in class exploitation.", "D": "Hegel championed retributive annulment of crime."},
    "Easy", "Jeremy Bentham, Principles of Penal Law", "Identify Bentham's Deterrent Theory."
)

add_mcq(
    "mcq-jur-11-019", "ch-jur-11", "top-jur-11-03",
    "What ancient moral principle of exact retaliation (an eye for an eye, a tooth for a tooth) forms the root of the 'Retributive Theory' of punishment?",
    ["Lex Mercatoria", "Lex Talionis", "Lex Domicilii", "Lex Loci Delicti"],
    1,
    "'Lex Talionis' (the law of exact retaliation) is the ancient moral foundation of the Retributive Theory, demanding that the punishment must morally fit and correspond to the crime committed.",
    {"A": "Law merchant.", "B": "Correct. Lex Talionis (eye for an eye).", "C": "Law of domicile.", "D": "Law of place of tort."},
    "Easy", "Broom's Legal Maxims", "Identify Lex Talionis."
)

add_mcq(
    "mcq-jur-11-020", "ch-jur-11", "top-jur-11-03",
    "Which German philosopher asserted that punishment is a 'Categorical Imperative' of moral justice, declaring that even if civil society were to dissolve tomorrow, the last murderer in prison must be executed?",
    ["Immanuel Kant", "Friedrich Nietzsche", "Karl Marx", "G.W. Leibniz"],
    0,
    "Immanuel Kant, in 'The Metaphysics of Morals', gave the classic uncompromising defense of Retributive Justice: punishment is a categorical moral duty owed to cosmic justice; society cannot compromise it for utilitarian goals.",
    {"A": "Correct. Immanuel Kant's categorical imperative of retribution.", "B": "Nietzsche attacked traditional morality.", "C": "Marx was a materialist.", "D": "Leibniz was a rationalist mathematician."},
    "Medium", "Kant, The Metaphysics of Morals (1797)", "Recall Kant's Retributive Theory of punishment."
)

add_mcq(
    "mcq-jur-11-021", "ch-jur-11", "top-jur-11-03",
    "What is the core premise of the 'Reformative Theory' (Rehabilitative Theory) of punishment?",
    ["Crime is an intentional moral rebellion deserving maximum vengeance", "Crime is a disease or social/psychological maladjustment; prisons should function as hospitals or reformatory schools ('Hate the crime, not the criminal')", "Punishment must physically disable the offender permanently", "All prisoners must be sentenced to hard labor without parole"],
    1,
    "The Reformative Theory views the criminal as a patient suffering from social or psychological pathology; the object of correctional jurisprudence is rehabilitation, therapy, and education to return the offender as a useful citizen.",
    {"A": "Retributive approach.", "B": "Correct. Reformative theory: treat crime as a disease; rehabilitate the offender.", "C": "Preventive incapacitation.", "D": "Retributive deterrence."},
    "Easy", "Salmond on Jurisprudence", "Define Reformative Theory of punishment."
)

add_mcq(
    "mcq-jur-11-022", "ch-jur-11", "top-jur-11-03",
    "How does the 'Preventive Theory' of punishment achieve its objective of social defense?",
    ["By converting the offender through religious sermon", "By physically disabling or incapacitating the offender (imprisonment, forfeiture, suspension of license, or capital punishment) to prevent repeat offenses", "By making the offender pay compensation to the victim", "By ignoring the crime"],
    1,
    "The Preventive Theory (defended by Paton and Holmes) disables the offender physically so he cannot offend again during the sentence (e.g. keeping a burglar behind bars, revoking a doctor's license, or execution).",
    {"A": "Expiatory/spiritual approach.", "B": "Correct. Preventive theory = Physical incapacitation and disability.", "C": "Restitution / civil redress.", "D": "Amnesty."},
    "Medium", "Paton's Jurisprudence", "Define Preventive Theory of punishment."
)

add_mcq(
    "mcq-jur-11-023", "ch-jur-11", "top-jur-11-03",
    "What celebrated sentencing doctrine governing the award of Capital Punishment in India was established in Bachan Singh v. State of Punjab (1980)?",
    ["The Strict Liability Doctrine", "The 'Rarest of Rare Cases' Doctrine", "The Precautionary Principle", "The Golden Rule"],
    1,
    "In Bachan Singh (1980 2 SCC 684), a 5-judge Constitution Bench upheld the death penalty under Article 21, but restricted its application to the 'Rarest of Rare Cases' when the alternative option of life imprisonment is unquestionably foreclosed.",
    {"A": "Tort doctrine.", "B": "Correct. The 'Rarest of Rare Cases' doctrine.", "C": "Environmental law principle.", "D": "Statutory interpretation rule."},
    "Easy", "Bachan Singh v. State of Punjab, (1980) 2 SCC 684", "Identify Bachan Singh landmark on death penalty."
)

add_mcq(
    "mcq-jur-11-024", "ch-jur-11", "top-jur-11-03",
    "In Sunil Batra v. Delhi Administration (1978), how did Justice V.R. Krishna Iyer humanize Indian prison jurisprudence?",
    ["By declaring that all prisons in India must be demolished", "By ruling that prisoners are human beings retaining fundamental rights under Articles 14, 19, and 21, and that cruel bar fetters and solitary confinement violate human dignity", "By ordering the release of all murder convicts", "By making prison wardens personally liable for state debts"],
    1,
    "Justice Krishna Iyer ruled that prisoners do not lose all constitutional rights upon entering prison gates; inhumane solitary confinement and bar fetters violate Articles 14, 19, and 21, championing reformative penology.",
    {"A": "Prisons were reformed, not demolished.", "B": "Correct. Prisoners retain fundamental rights; reformative penology upheld.", "C": "No mass release was ordered.", "D": "Fiscal irrelevance."},
    "Medium", "Sunil Batra v. Delhi Administration, (1978) 4 SCC 494", "Recall Sunil Batra ruling on prisoner rights."
)
