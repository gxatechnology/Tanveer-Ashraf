"""
Jurisprudence MCQs - Chapters 1 to 5 (128 MCQs)
Topics: top-jur-01-01 to top-jur-05-02
8 MCQs per topic
"""

MCQS_PART1 = []

def add_mcq(mid, cid, tid, q, opts, ans_idx, exp, ob, diff, prov, lo):
    letters = ["A", "B", "C", "D"]
    MCQS_PART1.append({
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
# CHAPTER 1: NATURE AND SCOPE OF JURISPRUDENCE
# -------------------------------------------------------------

# top-jur-01-01: Definitions of Jurisprudence
add_mcq(
    "mcq-jur-01-001", "ch-jur-01", "top-jur-01-01",
    "Who defined Jurisprudence as 'the observation of things divine and human, the science of the just and the unjust'?",
    ["Cicero", "Ulpian", "Justinian", "Salmond"],
    1,
    "Roman jurist Ulpian formulated the classical definition of jurisprudence in the Digest: 'Jurisprudentia est divinarum atque humanarum rerum notitia, justi atque injusti scientia'.",
    {"A": "Cicero defined law as right reason in agreement with nature.", "B": "Correct. Ulpian defined jurisprudence as knowledge of divine and human affairs.", "C": "Justinian compiled the Corpus Juris Civilis.", "D": "Salmond defined it as the science of first principles of civil law."},
    "Easy", "Ulpian, Digest 1.1.10", "Identify Ulpian's definition of jurisprudence."
)

add_mcq(
    "mcq-jur-01-002", "ch-jur-01", "top-jur-01-01",
    "According to Sir John Salmond, Jurisprudence in its specific sense is defined as:",
    ["The science of positive law", "The science of civil law", "The philosophy of positive law", "The formal science of positive law"],
    1,
    "Salmond defined jurisprudence as 'the science of civil law' (the law of the land), dividing it into theoretical and practical branches.",
    {"A": "Austin defined jurisprudence as the philosophy of positive law.", "B": "Correct. Salmond defined jurisprudence as the science of civil law.", "C": "Austin's preferred formulation.", "D": "Holland defined it as the formal science of positive law."},
    "Medium", "Salmond on Jurisprudence, 12th Ed.", "Recall Salmond's definition of jurisprudence."
)

add_mcq(
    "mcq-jur-01-003", "ch-jur-01", "top-jur-01-01",
    "Who defined Jurisprudence as 'the formal science of positive law'?",
    ["John Austin", "Sir Thomas Erskine Holland", "Hans Kelsen", "H.L.A. Hart"],
    1,
    "Sir Thomas Erskine Holland defined jurisprudence as 'the formal science of positive law', meaning it deals with the structural forms and relations of legal rules rather than their material content.",
    {"A": "Austin defined it as the philosophy of positive law.", "B": "Correct. Holland defined jurisprudence as a 'formal science'.", "C": "Kelsen propounded the Pure Theory of Law.", "D": "Hart analyzed law as the union of primary and secondary rules."},
    "Easy", "Holland's Elements of Jurisprudence", "Recognize Holland's formal science definition."
)

add_mcq(
    "mcq-jur-01-004", "ch-jur-01", "top-jur-01-01",
    "Gray defined Jurisprudence as:",
    ["The science of law, the statement and systematic arrangement of the rules followed by courts", "The knowledge of law in its historical evolution", "The study of fundamental legal conceptions", "The art of judicial interpretation"],
    0,
    "John Chipman Gray defined jurisprudence as 'the science of law, the statement and systematic arrangement of the rules followed by the courts and the principles involved in those rules'.",
    {"A": "Correct. Gray emphasized the rules followed by the courts.", "B": "Reflects the historical school approach.", "C": "Hohfeld focused on fundamental legal conceptions.", "D": "Reflects an interpretative approach."},
    "Medium", "Gray, Nature and Sources of the Law", "Recall Gray's court-centric definition."
)

add_mcq(
    "mcq-jur-01-005", "ch-jur-01", "top-jur-01-01",
    "Which jurist described Jurisprudence as the 'eye of the law'?",
    ["Laski", "Maine", "Austin", "Savigny"],
    0,
    "Harold Laski famously remarked that 'Jurisprudence is the eye of the law', emphasizing that without jurisprudential inquiry, legal rules lack direction and philosophical illumination.",
    {"A": "Correct. Laski described jurisprudence as the eye of the law.", "B": "Maine analyzed the movement from status to contract.", "C": "Austin viewed law as sovereign command.", "D": "Savigny linked law to Volksgeist."},
    "Easy", "Laski, Grammar of Politics", "Recall Laski's metaphor for jurisprudence."
)

add_mcq(
    "mcq-jur-01-006", "ch-jur-01", "top-jur-01-01",
    "Julius Stone described Jurisprudence as:",
    ["The lawyer's extraversion", "The science of justice", "The grammar of law", "The social engineering of law"],
    0,
    "Julius Stone defined jurisprudence as 'the lawyer's extraversion', meaning the lawyer's examination of legal precepts in the light of disciplines outside the law, such as history, sociology, and philosophy.",
    {"A": "Correct. Stone termed jurisprudence the lawyer's extraversion.", "B": "Salmond referred to first principles of civil justice.", "C": "Allen termed it grammar of law.", "D": "Roscoe Pound termed law social engineering."},
    "Medium", "Julius Stone, Legal System and Lawyers' Reasonings", "Identify Julius Stone's concept of jurisprudence."
)

add_mcq(
    "mcq-jur-01-007", "ch-jur-01", "top-jur-01-01",
    "According to Austin, what is the proper subject matter of Jurisprudence?",
    ["Divine Law", "Positive Morality", "Positive Law (Jus Positum)", "Natural Law"],
    2,
    "Austin declared that 'the matter of jurisprudence is positive law: law, simply and strictly so called: or law set by political superiors to political inferiors'.",
    {"A": "Austin excluded laws of God from municipal jurisprudence.", "B": "Positive morality was excluded from strict positive law.", "C": "Correct. Positive law alone is the subject of jurisprudence for Austin.", "D": "Austin rejected abstract natural law as non-positive."},
    "Easy", "Austin, Province of Jurisprudence Determined", "Identify Austin's subject matter of jurisprudence."
)

add_mcq(
    "mcq-jur-01-008", "ch-jur-01", "top-jur-01-01",
    "Who criticized Holland's definition of jurisprudence as a 'formal science', arguing that form cannot be studied in total isolation from matter?",
    ["Professor Gray", "Dr. Jenks", "Salmond", "Keeton"],
    1,
    "Dr. Edward Jenks severely criticized Holland, arguing that law is a living human institution and that treating jurisprudence as a purely 'formal' science like geometry or logic divorces it from practical reality.",
    {"A": "Gray was an American realist judge.", "B": "Correct. Dr. Jenks criticized Holland's formal science analogy.", "C": "Salmond provided an alternative definition.", "D": "Keeton defined it as principles of law."},
    "Hard", "Jenks, Law and Politics in the Middle Ages", "Recall the critique of Holland's formal science."
)

# top-jur-01-02: Nature & Scope of Jurisprudence
add_mcq(
    "mcq-jur-01-009", "ch-jur-01", "top-jur-01-02",
    "John Austin divided Jurisprudence into which two categories?",
    ["Expository and Censorial", "General and Particular", "Analytical and Historical", "Substantive and Adjective"],
    1,
    "Austin divided jurisprudence into: (1) General Jurisprudence (science of common principles found in mature systems) and (2) Particular Jurisprudence (science of any actual system of law, like English or Roman law).",
    {"A": "Bentham divided jurisprudence into Expository and Censorial.", "B": "Correct. Austin divided it into General and Particular.", "C": "School-based classification.", "D": "Classification of branches of law."},
    "Easy", "Austin's Lectures on Jurisprudence", "Distinguish Austin's division of jurisprudence."
)

add_mcq(
    "mcq-jur-01-010", "ch-jur-01", "top-jur-01-02",
    "Who introduced the division of Jurisprudence into 'Expository' (what the law is) and 'Censorial' (what the law ought to be)?",
    ["John Austin", "Jeremy Bentham", "H.L.A. Hart", "Lon Fuller"],
    1,
    "Jeremy Bentham, the father of modern English utilitarian positivism, divided jurisprudence into 'Expository' (as it is) and 'Censorial' or the art of legislation (as it ought to be).",
    {"A": "Austin adopted the is/ought separation but used general/particular.", "B": "Correct. Bentham created the Expository/Censorial dichotomy.", "C": "Hart separated primary and secondary rules.", "D": "Fuller discussed inner morality."},
    "Medium", "Bentham, Introduction to Principles of Morals and Legislation", "Recall Bentham's division of jurisprudence."
)

add_mcq(
    "mcq-jur-01-011", "ch-jur-01", "top-jur-01-02",
    "Why did Sir Thomas Erskine Holland reject Austin's classification of 'Particular Jurisprudence'?",
    ["He argued law cannot be studied empirically", "He argued jurisprudence is a science, and a science must be general by nature", "He argued particular law is purely political", "He denied the existence of national legal systems"],
    1,
    "Holland argued that science is a system of generalized knowledge; just as geology is not 'English geology' or 'French geology', jurisprudence cannot be 'particular'. Particular law is law, not jurisprudence.",
    {"A": "Holland advocated scientific method.", "B": "Correct. Holland argued science is universal, so jurisprudence cannot be particular.", "C": "Holland did not equate particular law to politics.", "D": "Holland recognized diverse national systems."},
    "Hard", "Holland's Elements of Jurisprudence", "Understand Holland's rejection of particular jurisprudence."
)

add_mcq(
    "mcq-jur-01-012", "ch-jur-01", "top-jur-01-02",
    "According to Salmond, what are the three concrete departments of Jurisprudence?",
    ["Analytical, Historical, and Ethical", "Civil, Criminal, and Constitutional", "Theoretical, Applied, and Practical", "Statutory, Customary, and Precedential"],
    0,
    "Salmond classified jurisprudence into three primary departments: (1) Analytical Jurisprudence (dogmatic analysis), (2) Historical Jurisprudence (origin and evolution), and (3) Ethical Jurisprudence (ideal purpose and justice).",
    {"A": "Correct. Analytical, Historical, and Ethical are Salmond's three departments.", "B": "These are subject branches of law.", "C": "General methodology terms.", "D": "Sources of law."},
    "Medium", "Salmond on Jurisprudence", "Identify Salmond's three departments of jurisprudence."
)

add_mcq(
    "mcq-jur-01-013", "ch-jur-01", "top-jur-01-02",
    "Which branch of jurisprudence investigates the legal history, origin, and organic growth of legal concepts across generations?",
    ["Analytical Jurisprudence", "Philosophical Jurisprudence", "Historical Jurisprudence", "Comparative Jurisprudence"],
    2,
    "Historical jurisprudence traces the origins, development, and evolution of legal concepts and principles over time.",
    {"A": "Analytical focuses on structural analysis of existing positive law.", "B": "Philosophical focuses on ideal ethical standards.", "C": "Correct. Historical jurisprudence traces historical evolution.", "D": "Comparative compares existing systems."},
    "Easy", "Dias on Jurisprudence", "Distinguish historical jurisprudence."
)

add_mcq(
    "mcq-jur-01-014", "ch-jur-01", "top-jur-01-02",
    "The phrase 'Jurisprudence is the science of first principles of civil law' is attributed to:",
    ["Keeton", "Salmond", "Paton", "Dicey"],
    1,
    "Salmond stated in the opening of his treatise that jurisprudence is 'the science of the first principles of the civil law'.",
    {"A": "Keeton defined it as study of general principles.", "B": "Correct. Salmond defined it as the first principles of civil law.", "C": "Paton viewed law as social institution.", "D": "Dicey analyzed the Rule of Law."},
    "Easy", "Salmond on Jurisprudence", "Recall Salmond's formulation of first principles."
)

add_mcq(
    "mcq-jur-01-015", "ch-jur-01", "top-jur-01-02",
    "Which jurist famously asserted that 'General Jurisprudence' is the science concerned with the exposition of principles, notions, and distinctions common to all advanced legal systems?",
    ["John Austin", "Savigny", "Pound", "Ehrlich"],
    0,
    "Austin defined General Jurisprudence as the science concerned with principles and distinctions common to mature systems of law (such as English and Roman systems).",
    {"A": "Correct. Austin defined general jurisprudence this way.", "B": "Savigny denied universal general jurisprudence, focusing on national Volksgeist.", "C": "Pound focused on social engineering.", "D": "Ehrlich focused on living law."},
    "Medium", "Austin, Lectures on Jurisprudence", "Recall Austin's view on general jurisprudence."
)

add_mcq(
    "mcq-jur-01-016", "ch-jur-01", "top-jur-01-02",
    "Why is Jurisprudence regarded as of immense practical educational value to a judicial candidate?",
    ["It contains readymade statutory rules for civil suits", "It trains the analytical mind to synthesize legal concepts and resolve ambiguities", "It replaces the study of procedural law", "It provides binding precedents under Article 141"],
    1,
    "Jurisprudence deepens analytical reasoning, clarifies basic concepts (rights, duties, possession, personality), and provides conceptual tools to interpret ambiguous statutes.",
    {"A": "Statutory rules are found in bare acts.", "B": "Correct. Jurisprudence provides cognitive clarity and structural analysis.", "C": "It does not replace procedural law.", "D": "It is academic doctrine, not judicial precedent under Article 141."},
    "Medium", "Dias on Jurisprudence", "Identify practical importance of jurisprudence."
)

# top-jur-01-03: Jurisprudence and Social Sciences
add_mcq(
    "mcq-jur-01-017", "ch-jur-01", "top-jur-01-03",
    "Which school of jurisprudence first established the deep organic connection between Jurisprudence and Sociology?",
    ["Analytical School", "Historical School", "Sociological School", "Realist School"],
    2,
    "The Sociological School (pioneered by Ihering, Ehrlich, Duguit, and Roscoe Pound) linked jurisprudence directly to sociology, studying law in action within society.",
    {"A": "Analytical school isolated law from sociology.", "B": "Historical school linked law to history and national spirit.", "C": "Correct. Sociological school linked law with social sciences.", "D": "Realist focused primarily on judicial behavior."},
    "Easy", "Pound, Jurisprudence, Vol. 1", "Identify sociological school connection."
)

add_mcq(
    "mcq-jur-01-018", "ch-jur-01", "top-jur-01-03",
    "The economic approach to jurisprudence and the concept that law is a tool of the dominant class to protect property relations is primarily associated with:",
    ["Jeremy Bentham", "Karl Marx", "Max Weber", "Adam Smith"],
    1,
    "Marxist jurisprudence posits that law is an ideological superstructure determined by the economic base of production, serving to consolidate the economic power of the ruling class.",
    {"A": "Bentham was a utilitarian philosopher.", "B": "Correct. Karl Marx developed the materialist economic theory of law.", "C": "Weber analyzed bureaucratic and legal rational authority.", "D": "Adam Smith founded classical economics."},
    "Easy", "Marx & Engels, The Communist Manifesto", "Identify economic/Marxist theory of law."
)

add_mcq(
    "mcq-jur-01-019", "ch-jur-01", "top-jur-01-03",
    "Which sociologist and legal theorist analyzed law through the concepts of 'Charismatic', 'Traditional', and 'Rational-Legal' authority?",
    ["Emile Durkheim", "Max Weber", "Karl Marx", "Talcott Parsons"],
    1,
    "Max Weber famously classified legitimate authority into three ideal types: Traditional, Charismatic, and Rational-Legal (which forms the basis of modern bureaucratic constitutional law).",
    {"A": "Durkheim studied mechanical and organic solidarity.", "B": "Correct. Weber classified the 3 types of legal authority.", "C": "Marx focused on class struggle.", "D": "Parsons focused on structural functionalism."},
    "Medium", "Max Weber, Economy and Society", "Recall Max Weber's typology of authority."
)

add_mcq(
    "mcq-jur-01-020", "ch-jur-01", "top-jur-01-03",
    "The discipline of 'Ethics' differs essentially from 'Jurisprudence' in that:",
    ["Ethics deals with the internal conscience and motives, while law regulates external human conduct backed by sanctions", "Ethics is enforced by the state courts", "Ethics is solely concerned with economic efficiency", "Ethics does not care about justice"],
    0,
    "Ethics evaluates internal motives and conscience according to moral virtue, whereas positive law regulates external conduct and is enforced by coercive state sanctions.",
    {"A": "Correct. Ethics governs internal conscience; law regulates external actions with sanctions.", "B": "Courts enforce law, not pure ethics.", "C": "Economic efficiency is the domain of economics.", "D": "Ethics is deeply concerned with justice."},
    "Medium", "Salmond on Jurisprudence", "Distinguish law from ethics."
)

add_mcq(
    "mcq-jur-01-021", "ch-jur-01", "top-jur-01-03",
    "Emile Durkheim correlated legal evolution with social solidarity, distinguishing between:",
    ["Primary and Secondary rules", "Repressive Law (Mechanical Solidarity) and Restitutive Law (Organic Solidarity)", "Command and Sanction", "Natural and Positive Law"],
    1,
    "Durkheim showed that early societies with mechanical solidarity use 'Repressive Law' (penal sanctions), while modern complex societies with division of labor use 'Restitutive Law' (civil, contract, and administrative compensation).",
    {"A": "Hart distinguished primary and secondary rules.", "B": "Correct. Durkheim analyzed repressive and restitutive law.", "C": "Austin analyzed command and sanction.", "D": "Classical legal philosophy distinction."},
    "Hard", "Durkheim, The Division of Labour in Society", "Recall Durkheim's legal sociology."
)

add_mcq(
    "mcq-jur-01-022", "ch-jur-01", "top-jur-01-03",
    "Who authored the influential modern treatise 'Economic Analysis of Law', applying microeconomic concepts of efficiency and transaction costs to legal rules?",
    ["Richard Posner", "Ronald Dworkin", "John Rawls", "Robert Nozick"],
    0,
    "Judge Richard Posner pioneered modern Law and Economics with his treatise 'Economic Analysis of Law' (1973), examining torts, contracts, and property through the lens of economic wealth maximization.",
    {"A": "Correct. Richard Posner authored Economic Analysis of Law.", "B": "Dworkin authored Taking Rights Seriously.", "C": "Rawls authored A Theory of Justice.", "D": "Nozick authored Anarchy, State, and Utopia."},
    "Medium", "Posner, Economic Analysis of Law", "Identify Posner's economic analysis of law."
)

add_mcq(
    "mcq-jur-01-023", "ch-jur-01", "top-jur-01-03",
    "The relationship between Psychology and Jurisprudence is most directly reflected in which of the following areas of law?",
    ["The doctrine of adverse possession under property law", "The determination of Mens Rea, criminal insanity (M'Naghten rules), and validity of consent", "The calculation of stamp duty on conveyance deeds", "The doctrine of territorial nexus in tax law"],
    1,
    "Psychology intersects directly with jurisprudence in determining mens rea, subjective intent, criminal responsibility, the insanity defense (M'Naghten rules), and voluntary consent.",
    {"A": "Adverse possession is an objective land doctrine.", "B": "Correct. Mens rea and insanity rely directly on psychological science.", "C": "Fiscal statutory calculation.", "D": "Constitutional jurisdictional doctrine."},
    "Easy", "Glanville Williams, Criminal Law", "Identify intersection of psychology and jurisprudence."
)

add_mcq(
    "mcq-jur-01-024", "ch-jur-01", "top-jur-01-03",
    "Which jurist remarked that 'Law without history has no root; history without law has no fruit'?",
    ["Maitland", "Stubbs", "Savigny", "Salmond"],
    0,
    "F.W. Maitland famously observed the symbiotic relationship between legal history and substantive jurisprudence.",
    {"A": "Correct. F.W. Maitland coined this famous aphorism.", "B": "Stubbs was an English constitutional historian.", "C": "Savigny founded historical school.", "D": "Salmond was an analytical jurist."},
    "Hard", "Maitland, Selected Historical Essays", "Recall Maitland's aphorism on law and history."
)

# -------------------------------------------------------------
# CHAPTER 2: NATURE AND ESSENTIALS OF LAW
# -------------------------------------------------------------

# top-jur-02-01: Meaning & Elements of Law
add_mcq(
    "mcq-jur-02-001", "ch-jur-02", "top-jur-02-01",
    "What are the three essential constituents of Law according to John Austin's Imperative Theory?",
    ["Reason, Morality, and Justice", "Command, Duty, and Sanction (backed by Sovereign)", "Primary rules, Secondary rules, and Rule of Recognition", "Grundnorm, Hierarchy, and Validity"],
    1,
    "Austin's command theory formula defines law as: Command of the Sovereign + Duty of the Subject + Sanction for Disobedience.",
    {"A": "Reflects natural law philosophy.", "B": "Correct. Command, Duty, and Sanction backed by Sovereign is Austin's formula.", "C": "Hart's formula.", "D": "Kelsen's formula."},
    "Easy", "Austin, Province of Jurisprudence Determined", "Recall Austin's 3 constituents of law."
)

add_mcq(
    "mcq-jur-02-002", "ch-jur-02", "top-jur-02-01",
    "In H.L.A. Hart's 'The Concept of Law' (1961), law is explained as the union of:",
    ["Command and Sovereign", "Primary Rules of Obligation and Secondary Rules of Recognition, Change, and Adjudication", "Norms and Sanctions", "Custom and Precedent"],
    1,
    "Hart famously replaced Austin's command model with the thesis that law is the union of primary rules (imposing duties) and secondary rules (conferring powers: recognition, change, adjudication).",
    {"A": "Austin's imperative model.", "B": "Correct. Hart's union of primary and secondary rules.", "C": "Kelsen's normative structure.", "D": "Sources of law."},
    "Easy", "H.L.A. Hart, The Concept of Law", "Recall Hart's union of primary and secondary rules."
)

add_mcq(
    "mcq-jur-02-003", "ch-jur-02", "top-jur-02-01",
    "How did Sir John Salmond define Law?",
    ["The command of a sovereign backed by threat of force", "The body of principles recognized and applied by the state in the administration of justice", "An ordinance of reason for the common good", "A prediction of what the courts will do in fact"],
    1,
    "Salmond defined law from the perspective of the courtroom: 'the body of principles recognized and applied by the state in the administration of justice'.",
    {"A": "Austin's definition.", "B": "Correct. Salmond defined law through the administration of justice.", "C": "St. Thomas Aquinas's definition.", "D": "O.W. Holmes Jr.'s realist definition."},
    "Medium", "Salmond on Jurisprudence", "Identify Salmond's definition of law."
)

add_mcq(
    "mcq-jur-02-004", "ch-jur-02", "top-jur-02-01",
    "In Kelsen's Pure Theory of Law, what imparts binding legal validity to all inferior norms in a legal system?",
    ["The sovereign's physical power", "The Grundnorm (Basic Norm)", "Moral justice", "Democratic consensus"],
    1,
    "In Hans Kelsen's hierarchy of norms (Stufenbaulehre), every legal norm derives its validity from a superior norm, ascending to the apex 'Grundnorm' (Basic Norm).",
    {"A": "Austin stressed sovereign force; Kelsen rejected physical coercion as validity test.", "B": "Correct. The Grundnorm is the apex hypothesis imparting validity.", "C": "Kelsen strictly excluded morals from the pure theory.", "D": "Democratic consensus is a sociological fact, not a pure norm."},
    "Easy", "Kelsen, General Theory of Law and State", "Identify Kelsen's Grundnorm."
)

add_mcq(
    "mcq-jur-02-005", "ch-jur-02", "top-jur-02-01",
    "What is the ultimate 'Secondary Rule' in H.L.A. Hart's legal system that provides authoritative criteria for identifying valid primary rules?",
    ["Rule of Adjudication", "Rule of Change", "Rule of Recognition", "Grundnorm"],
    2,
    "Hart's 'Rule of Recognition' is the fundamental secondary rule that provides authoritative criteria by which officials identify what counts as valid law (e.g. enacted by Queen-in-Parliament).",
    {"A": "Rules of adjudication empower judges to resolve disputes.", "B": "Rules of change govern introduction and repeal of laws.", "C": "Correct. Rule of Recognition identifies valid rules.", "D": "Grundnorm is Kelsen's term."},
    "Medium", "Hart, The Concept of Law", "Identify Hart's Rule of Recognition."
)

add_mcq(
    "mcq-jur-02-006", "ch-jur-02", "top-jur-02-01",
    "Who criticized Austin's command theory by comparing the Austinian Sovereign to a 'Gunman Writ Large'?",
    ["Lon Fuller", "H.L.A. Hart", "Roscoe Pound", "Friedmann"],
    1,
    "H.L.A. Hart famously observed that reducing law to commands backed by threats makes the legal order indistinguishable from the orders of an armed bank robber ('The Gunman Situation Writ Large').",
    {"A": "Fuller criticized positivism through the 8 desiderata.", "B": "Correct. Hart formulated the gunman situation critique.", "C": "Pound criticized mechanical jurisprudence.", "D": "Friedmann analyzed legal theory."},
    "Medium", "Hart, The Concept of Law", "Recall Hart's Gunman critique of Austin."
)

add_mcq(
    "mcq-jur-02-007", "ch-jur-02", "top-jur-02-01",
    "According to Oliver Wendell Holmes Jr., what is the 'Bad Man' theory of law?",
    ["Law is designed only to punish wicked men", "If you want to know what law is, look at it through the eyes of a bad man who cares only about material consequences/penalties", "A bad man has no legal rights", "Judges are bad men who make arbitrary rules"],
    1,
    "Holmes argued that a legal duty is not a moral duty; to understand real law, look at it from the viewpoint of a bad man who cares nothing for ethics, but only for what the courts will actually do to him.",
    {"A": "Incorrect paraphrase.", "B": "Correct. The bad man cares only about practical judicial consequences/sanctions.", "C": "The bad man possesses legal rights.", "D": "Holmes did not call judges bad men."},
    "Medium", "Holmes, The Path of the Law (1897)", "Recall Holmes's Bad Man theory."
)

add_mcq(
    "mcq-jur-02-008", "ch-jur-02", "top-jur-02-01",
    "Which element did John Austin consider an absolute impossibility in his sovereign?",
    ["Habit of obedience by the subjects", "Legal limitation or legal liability upon the sovereign", "Power to inflict sanctions", "Political superiority"],
    1,
    "Austin maintained that sovereign power is legally illimitable and indivisible: 'A sovereign is legally incapable of legal limitation', because a sovereign cannot bind himself by law.",
    {"A": "Habit of obedience is Austin's central requirement.", "B": "Correct. Austin held that the sovereign cannot be subject to legal limitations.", "C": "Sanction power is essential to sovereignty.", "D": "Political superiority is central to Austin's definition."},
    "Medium", "Austin, Lectures on Jurisprudence", "Identify Austin's view on sovereign limitations."
)

# top-jur-02-02: Law and Morality
add_mcq(
    "mcq-jur-02-009", "ch-jur-02", "top-jur-02-02",
    "The celebrated 'Hart-Devlin Debate' arose following the publication of which official British committee report in 1957?",
    ["The Simon Commission Report", "The Wolfenden Committee Report", "The Radcliffe Committee Report", "The Kilbrandon Commission Report"],
    1,
    "The Wolfenden Report (1957) recommended decriminalizing private consensual homosexual acts between adults, stating there must be a realm of private morality that is not the law's business, triggering the Hart-Devlin debate.",
    {"A": "Simon Commission examined Indian constitutional reform.", "B": "Correct. Wolfenden Report on Homosexual Offenses and Prostitution.", "C": "Radcliffe report concerned currency and boundary.", "D": "Kilbrandon concerned UK devolution."},
    "Easy", "Wolfenden Committee Report 1957", "Identify origin of Hart-Devlin debate."
)

add_mcq(
    "mcq-jur-02-010", "ch-jur-02", "top-jur-02-02",
    "What was Lord Devlin's central thesis regarding the enforcement of morals by criminal law?",
    ["Law should never enforce moral values", "Society is bound together by a shared moral fabric; loosening that fabric threatens society with disintegration, giving society the right to preserve morality by law", "Only religious authorities can enforce morality", "Individual liberty always overrides collective moral opinions"],
    1,
    "Lord Devlin propounded the 'Disintegration Thesis': society possesses an invisible moral bond; destruction of moral consensus weakens the social cohesion, justifying the legal enforcement of morals.",
    {"A": "This was Hart's liberal stance.", "B": "Correct. Devlin's shared moral fabric / disintegration thesis.", "C": "Devlin did not advocate ecclesiastical rule.", "D": "This is John Stuart Mill's Harm Principle."},
    "Medium", "Devlin, The Enforcement of Morals (1965)", "Understand Lord Devlin's position on law and morality."
)

add_mcq(
    "mcq-jur-02-011", "ch-jur-02", "top-jur-02-02",
    "H.L.A. Hart, defending the liberal tradition against Lord Devlin, relied heavily on which classic principle formulated by John Stuart Mill?",
    ["The Categorical Imperative", "The Harm Principle", "The Utilitarian Pleasure Principle", "The Golden Rule"],
    1,
    "Hart defended J.S. Mill's 'Harm Principle' from 'On Liberty' (1859): the only purpose for which power can be rightfully exercised over any member of a civilized community against his will is to prevent harm to others.",
    {"A": "Kant's moral principle.", "B": "Correct. Mill's Harm Principle.", "C": "Bentham's hedonistic principle.", "D": "Traditional theological ethics."},
    "Easy", "Hart, Law, Liberty and Morality", "Identify Mill's Harm Principle in Hart's argument."
)

add_mcq(
    "mcq-jur-02-012", "ch-jur-02", "top-jur-02-02",
    "Lon L. Fuller propounded that law possesses an 'Internal Morality'. How many procedural desiderata or requirements of legal excellence did Fuller formulate?",
    ["Five", "Seven", "Eight", "Ten"],
    2,
    "Fuller outlined the 'Eight Desiderata' (internal procedural morality of law) in 'The Morality of Law': generality, promulgation, non-retroactivity, clarity, non-contradiction, possibility of compliance, constancy through time, and congruence between official action and declared rule.",
    {"A": "Salmond's five elements.", "B": "Seven lamps of advocacy.", "C": "Correct. Fuller's Eight Desiderata.", "D": "Ten commandments."},
    "Easy", "Lon Fuller, The Morality of Law (1964)", "Recall Fuller's 8 procedural requirements."
)

add_mcq(
    "mcq-jur-02-013", "ch-jur-02", "top-jur-02-02",
    "In the fictional allegory used by Lon Fuller to illustrate the total failure of legal order, what was the name of the inept monarch?",
    ["King Solomon", "King Rex", "King Minos", "King Lycurgus"],
    1,
    "Fuller used the allegory of 'King Rex' who failed to make law eight consecutive times by violating each of the eight procedural desiderata.",
    {"A": "Biblical monarch.", "B": "Correct. King Rex in Fuller's The Morality of Law.", "C": "Mythological king of Crete.", "D": "Spartan lawgiver."},
    "Medium", "Lon Fuller, The Morality of Law", "Identify King Rex allegory."
)

add_mcq(
    "mcq-jur-02-014", "ch-jur-02", "top-jur-02-02",
    "What is the foundational premise of Legal Positivism regarding the relationship between Law and Morality?",
    ["Law is identical to moral virtue", "The Separation Thesis: The existence of law is one thing, its merit or demerit is another", "An unjust law is no law at all (Lex injusta non est lex)", "Legal validity depends on conformity with divine scripture"],
    1,
    "The hallmark of Legal Positivism is the 'Separation Thesis' (formulated by Austin and Hart): there is no necessary conceptual connection between the law that IS and the law that OUGHT to be.",
    {"A": "Classical natural law view.", "B": "Correct. Austin/Hart's Separation Thesis.", "C": "Augustine/Aquinas natural law maxim.", "D": "Theological scholasticism."},
    "Easy", "Hart, Positivism and the Separation of Law and Morals", "Define the Separation Thesis of positivism."
)

add_mcq(
    "mcq-jur-02-015", "ch-jur-02", "top-jur-02-02",
    "Which Indian constitutional judgment decriminalized adult consensual same-sex conduct, echoing the Hart-Devlin debate and Mill's harm principle?",
    ["Suresh Kumar Koushal v. Naz Foundation", "Navtej Singh Johar v. Union of India", "Justice K.S. Puttaswamy v. Union of India", "Shayara Bano v. Union of India"],
    1,
    "In Navtej Singh Johar (2018), a 5-judge Constitution Bench struck down Section 377 IPC to the extent it criminalized consensual homosexual sex, holding that constitutional morality overrides majoritarian public morality.",
    {"A": "Koushal reversed Naz Foundation; later overruled.", "B": "Correct. Navtej Singh Johar (2018) decriminalized Section 377.", "C": "Puttaswamy established fundamental right to privacy.", "D": "Shayara Bano invalidated instant Triple Talaq."},
    "Medium", "Navtej Singh Johar v. UOI, (2018) 10 SCC 1", "Link Hart-Devlin debate to Navtej Johar."
)

add_mcq(
    "mcq-jur-02-016", "ch-jur-02", "top-jur-02-02",
    "What classic Latin maxim of natural law asserts that 'an unjust law is not law'?",
    ["Ubi jus ibi remedium", "Lex injusta non est lex", "Salus populi suprema lex", "Ignorantia juris non excusat"],
    1,
    "'Lex injusta non est lex' (an unjust law is no law at all) was formulated by St. Augustine and St. Thomas Aquinas, and cited by natural lawyers to deny validity to tyrannical decrees.",
    {"A": "Where there is a right, there is a remedy.", "B": "Correct. Lex injusta non est lex.", "C": "Welfare of the people is the supreme law.", "D": "Ignorance of law is no excuse."},
    "Easy", "St. Thomas Aquinas, Summa Theologiae", "Identify the classic natural law maxim on unjust law."
)

# top-jur-02-03: Classification of Law
add_mcq(
    "mcq-jur-02-017", "ch-jur-02", "top-jur-02-03",
    "How did Salmond define 'Substantive Law' as opposed to 'Adjective Law' (Procedural Law)?",
    ["Substantive law defines legal rights and liabilities; adjective law defines the machinery and procedure for enforcing them", "Substantive law is unwritten; adjective law is statutory", "Substantive law applies only to criminal cases; adjective law to civil cases", "Substantive law is enacted by Parliament; adjective law by High Courts"],
    0,
    "Salmond explained that substantive law creates, defines, and regulates rights and duties (e.g. IPC, Contract Act), while adjective/procedural law regulates the judicial machinery for enforcing rights (e.g. CPC, CrPC/BNSS).",
    {"A": "Correct. Substantive defines rights; adjective/procedural defines machinery of enforcement.", "B": "Both can be written statutes.", "C": "Both apply to civil and criminal matters.", "D": "Both can be parliamentary statutes."},
    "Easy", "Salmond on Jurisprudence", "Distinguish substantive from adjective law."
)

add_mcq(
    "mcq-jur-02-018", "ch-jur-02", "top-jur-02-03",
    "Which branch of law regulates relations between individual private citizens where the state acts merely as an impartial arbiter?",
    ["Public Law", "Private Law (Civil Law)", "Constitutional Law", "Administrative Law"],
    1,
    "Private Law (Civil Law, Contracts, Torts, Property) governs relationships between private legal persons where the state does not participate as a party but provides the adjudicatory forum.",
    {"A": "Public law involves the state acting in its sovereign capacity.", "B": "Correct. Private law regulates relations between citizens.", "C": "Constitutional law is the apex branch of public law.", "D": "Administrative law regulates state executive action."},
    "Easy", "Holland's Elements of Jurisprudence", "Define Private Law."
)

add_mcq(
    "mcq-jur-02-019", "ch-jur-02", "top-jur-02-03",
    "Why did John Austin characterize Public International Law as 'Positive International Morality' rather than true law?",
    ["It has no moral principles", "It lacks a determinate sovereign commander with physical sanctions to compel obedience", "It is written in French and English", "It deals only with war and treaties"],
    1,
    "Austin famously denied that International Law is law strictly so-called because it lacks a determinate political sovereign and coercive sanctions; he called it 'positive international morality'.",
    {"A": "Austin recognized international customs as moral rules.", "B": "Correct. Austin denied it was true law due to lack of sovereign and sanction.", "C": "Language is irrelevant to Austin's taxonomy.", "D": "International law covers peacetime relations too."},
    "Medium", "Austin, Province of Jurisprudence Determined", "Understand Austin's classification of international law."
)

add_mcq(
    "mcq-jur-02-020", "ch-jur-02", "top-jur-02-03",
    "In modern constitutional jurisprudence, what is the 'Rule of Law' as formulated by A.V. Dicey in 1885?",
    ["Supremacy of regular law, equality before the law, and predominance of legal spirit", "Rule of the judicial bench over Parliament", "The military command of the Crown", "The prerogative power of the Prime Minister"],
    0,
    "A.V. Dicey formulated three pillars of the Rule of Law: (1) Absolute supremacy of regular law over arbitrary power, (2) Equality before the law (equal subjection to ordinary courts), and (3) The constitution as the result of ordinary judicial decisions.",
    {"A": "Correct. Dicey's three principles of the Rule of Law.", "B": "Dicey upheld Parliamentary sovereignty alongside Rule of Law.", "C": "Military rule is martial law.", "D": "Prerogative power is subject to ordinary law."},
    "Easy", "Dicey, Law of the Constitution (1885)", "Recall Dicey's three pillars of Rule of Law."
)

add_mcq(
    "mcq-jur-02-021", "ch-jur-02", "top-jur-02-03",
    "Which legal classification distinguishes 'Municipal Law' from 'International Law'?",
    ["Municipal law is local city law; international law is world law", "Municipal law is the internal national law of a sovereign state; international law governs relations between sovereign states", "Municipal law applies only to corporations", "Municipal law is unwritten common law"],
    1,
    "In jurisprudence, 'Municipal Law' refers to the national, domestic legal system of an independent sovereign state (e.g. Indian law), as distinguished from International Law.",
    {"A": "Municipal does not mean just municipal corporation bye-laws in jurisprudence.", "B": "Correct. Municipal law is the national domestic law of a sovereign state.", "C": "It applies to all natural and legal persons.", "D": "Municipal law includes statutes and codes."},
    "Easy", "Oppenheim's International Law", "Define Municipal Law."
)

add_mcq(
    "mcq-jur-02-022", "ch-jur-02", "top-jur-02-03",
    "Which article of the Indian Constitution embodies the core principle of 'Equality before the law' and 'Equal protection of the laws'?",
    ["Article 19", "Article 14", "Article 21", "Article 32"],
    1,
    "Article 14 guarantees that 'The State shall not deny to any person equality before the law or the equal protection of the laws within the territory of India', embodying Dicey's second pillar.",
    {"A": "Article 19 protects fundamental freedoms.", "B": "Correct. Article 14 guarantees equality before law.", "C": "Article 21 protects life and personal liberty.", "D": "Article 32 provides constitutional remedies."},
    "Easy", "Constitution of India, Article 14", "Link Rule of Law to Article 14."
)

add_mcq(
    "mcq-jur-02-023", "ch-jur-02", "top-jur-02-03",
    "Which of the following is the best example of 'Substantive Law'?",
    ["The Bharatiya Nagarik Suraksha Sanhita, 2023", "The Bharatiya Nyaya Sanhita, 2023", "The Bharatiya Sakshya Adhiniyam, 2023", "The Code of Civil Procedure, 1908"],
    1,
    "The Bharatiya Nyaya Sanhita (BNS) defines crimes and prescribes punishments, making it substantive criminal law. BNSS, BSA, and CPC are procedural/adjective laws.",
    {"A": "BNSS is procedural criminal law.", "B": "Correct. BNS creates and defines offenses (substantive law).", "C": "BSA is procedural/adjective law of evidence.", "D": "CPC is civil procedural law."},
    "Easy", "Salmond on Jurisprudence", "Classify BNS as substantive law."
)

add_mcq(
    "mcq-jur-02-024", "ch-jur-02", "top-jur-02-03",
    "Private International Law is also widely known as:",
    ["Public International Law", "Conflict of Laws", "Jus Cogens", "Lex Mercatoria"],
    1,
    "Private International Law is commonly termed the 'Conflict of Laws', resolving issues of applicable legal jurisdiction and foreign law when a civil dispute involves foreign elements.",
    {"A": "Public International Law governs interstate relations.", "B": "Correct. Private International Law = Conflict of Laws.", "C": "Jus cogens refers to peremptory norms of international law.", "D": "Lex mercatoria is customary law of merchants."},
    "Easy", "Dicey, Morris & Collins, The Conflict of Laws", "Identify Conflict of Laws."
)

# -------------------------------------------------------------
# CHAPTER 3: SOURCES OF LAW
# -------------------------------------------------------------

# top-jur-03-01: Custom as a Source of Law
add_mcq(
    "mcq-jur-03-001", "ch-jur-03", "top-jur-03-01",
    "Sir William Blackstone laid down seven essentials of a valid custom. Which of the following is NOT one of Blackstone's essentials?",
    ["Immemorial antiquity", "Continuous and peaceful observance", "Certainty and reasonableness", "Prior express approval by an Act of Parliament"],
    3,
    "Blackstone's essentials are: immemorial antiquity, continuity, peaceable enjoyment, certainty, reasonableness, compulsoriness, and consistency. A custom derives validity from popular practice, not prior parliamentary enactment.",
    {"A": "Antiquity is Blackstone's 1st requirement.", "B": "Continuity is essential.", "C": "Certainty and reasonableness are mandatory.", "D": "Correct. Custom does not require prior statutory enactment."},
    "Medium", "Blackstone's Commentaries on the Laws of England", "Identify Blackstone's essentials of valid custom."
)

add_mcq(
    "mcq-jur-03-002", "ch-jur-03", "top-jur-03-01",
    "Under English common law, what specific year is fixed as the threshold of 'Immemorial Antiquity' (Time immemorial)?",
    ["1066 AD (Norman Conquest)", "1189 AD (Accession of Richard I)", "1215 AD (Magna Carta)", "1688 AD (Glorious Revolution)"],
    1,
    "In English law, the Statute of Westminster I (1275) fixed the threshold of legal memory as 1189 AD (the accession of King Richard I). A custom must have existed since or before 1189 AD.",
    {"A": "1066 is the Battle of Hastings.", "B": "Correct. 1189 AD is the year of legal memory.", "C": "1215 is Magna Carta.", "D": "1688 is the Glorious Revolution."},
    "Medium", "Salmond on Jurisprudence", "Recall year of legal memory in English law."
)

add_mcq(
    "mcq-jur-03-003", "ch-jur-03", "top-jur-03-01",
    "What is the position of Indian law regarding the English rule of immemorial antiquity (1189 AD)?",
    ["The rule of 1189 AD applies strictly to all Indian customs", "Indian courts do not follow the rigid year 1189 AD; it is sufficient if the custom is proved to be ancient, certain, continuous, and reasonable", "Indian law does not recognize any custom at all", "Customs in India must be registered under the Registration Act 1908"],
    1,
    "The Privy Council held in Baba Narayan v. Maya Ram (1940) and Gokul Chand v. Parvin Kumari (1952 SC) that the English rule of 1189 AD does not apply in India; proof of ancient, continuous, and uniform observance suffices.",
    {"A": "Incorrect; English date is inapplicable in India.", "B": "Correct. Indian law requires proof of being ancient and continuous without a fixed year.", "C": "Article 13(3)(a) explicitly recognizes custom as law.", "D": "Custom is unwritten; not registrable."},
    "Medium", "Gokul Chand v. Parvin Kumari, 1952 SCR 825", "Understand Indian rule on ancient custom."
)

add_mcq(
    "mcq-jur-03-004", "ch-jur-03", "top-jur-03-01",
    "What psychological element is required in international and municipal law to convert a mere social habit into a legally binding custom?",
    ["Anima naturalis", "Opinio juris sive necessitatis", "Mens rea", "Consensus ad idem"],
    1,
    "'Opinio juris sive necessitatis' (the belief that an action is carried out as a matter of legal duty rather than mere social courtesy) is the indispensable mental element of binding custom.",
    {"A": "Irrelevant biological phrase.", "B": "Correct. Opinio juris converts habit into binding custom.", "C": "Guilty mind in criminal law.", "D": "Meeting of minds in contract law."},
    "Medium", "Brownlie's Principles of Public International Law", "Define Opinio Juris."
)

add_mcq(
    "mcq-jur-03-005", "ch-jur-03", "top-jur-03-01",
    "According to the Historical School (Savigny), what is the relationship between Custom and Legislation?",
    ["Custom is superior and anterior to legislation because it embodies the organic Volksgeist", "Legislation is the only true source of law; custom is a subordinate concession", "Custom has zero legal validity unless ratified by Parliament", "Custom and legislation are identical in origin"],
    0,
    "Savigny asserted that custom is the primary and purest source of law, reflecting the national spirit (Volksgeist); legislation is merely a secondary and formal consolidation of customary rules.",
    {"A": "Correct. Historical school exalts custom over legislation.", "B": "Austin's positivist view.", "C": "Positivist analytical view.", "D": "Historically incorrect."},
    "Easy", "Savigny, System of Modern Roman Law", "Contrast custom and legislation in Historical School."
)

add_mcq(
    "mcq-jur-03-006", "ch-jur-03", "top-jur-03-01",
    "Which article of the Indian Constitution expressly defines 'Law' to include 'custom or usage having in the territory of India the force of law'?",
    ["Article 13(3)(a)", "Article 14", "Article 19(1)", "Article 368"],
    0,
    "Article 13(3)(a) of the Constitution of India provides: ''law' includes any Ordinance, order, bye-law, rule, regulation, notification, custom or usage having in the territory of India the force of law'.",
    {"A": "Correct. Article 13(3)(a) defines law to include custom and usage.", "B": "Article 14 is equality before law.", "C": "Article 19(1) lists fundamental freedoms.", "D": "Article 368 governs constitutional amendment."},
    "Easy", "Constitution of India, Article 13(3)(a)", "Identify Article 13(3)(a) definition of custom."
)

add_mcq(
    "mcq-jur-03-007", "ch-jur-03", "top-jur-03-01",
    "Can a custom that is opposed to public policy, morality, or an express statutory provision be enforced by Indian courts?",
    ["Yes, custom always overrides statute law in India", "No, custom must yield to an express statute and must not be contrary to public policy or morality", "Yes, if the custom has existed for more than 500 years", "Yes, in all family disputes"],
    1,
    "It is a settled rule of Indian jurisprudence that an ancient custom, no matter how long observed, is void if it is immoral, contrary to public policy, or expressly abrogated by an Act of the Legislature.",
    {"A": "Statute overrides custom unless expressly saved.", "B": "Correct. Custom must be reasonable, moral, and yields to express statute.", "C": "Antiquity cannot validate immoral customs.", "D": "Family customs cannot violate statutory prohibitions."},
    "Easy", "Mulla: Hindu Law", "State limits on enforceability of custom."
)

add_mcq(
    "mcq-jur-03-008", "ch-jur-03", "top-jur-03-01",
    "In which landmark case did the Supreme Court hold that an ancient custom permitting female infanticide or discriminatory exclusion of women from inheritance is void as contrary to public policy?",
    ["Madhu Kishwar v. State of Bihar", "Gokul Chand v. Parvin Kumari", "Surjit Kaur v. Garja Singh", "Balusami v. Balakrishna"],
    0,
    "In Madhu Kishwar (1996), the Supreme Court ruled that tribal customary laws excluding female heirs from inheriting land violate Articles 14 and 21 and must be interpreted in harmony with gender justice.",
    {"A": "Correct. Madhu Kishwar v. State of Bihar, (1996) 5 SCC 125.", "B": "Gokul Chand concerned proof of custom.", "C": "Surjit Kaur concerned custom of marriage.", "D": "Balusami concerned adoption."},
    "Medium", "Madhu Kishwar v. State of Bihar, (1996) 5 SCC 125", "Recall modern judicial limits on discriminatory custom."
)

# top-jur-03-02: Judicial Precedent & Stare Decisis
add_mcq(
    "mcq-jur-03-009", "ch-jur-03", "top-jur-03-02",
    "What does the Latin maxim 'Stare decisis et non quieta movere' mean?",
    ["To stand by decisions and not disturb what is settled", "The King can do no wrong", "Ignorance of law excuses no one", "The act of court harms no one"],
    0,
    "'Stare decisis et non quieta movere' is the bedrock doctrine of precedent: to abide by decided cases and not disturb settled principles, ensuring legal certainty and stability.",
    {"A": "Correct. Stare decisis = Stand by decisions and not disturb settled points.", "B": "Rex non potest peccare.", "C": "Ignorantia juris non excusat.", "D": "Actus curiae neminem gravabit."},
    "Easy", "Salmond on Jurisprudence", "Define Stare Decisis."
)

add_mcq(
    "mcq-jur-03-010", "ch-jur-03", "top-jur-03-02",
    "Which part of a judicial decision creates binding precedent for future cases?",
    ["The factual narrative", "The Ratio Decidendi", "The Obiter Dictum", "The final formal decree"],
    1,
    "The 'Ratio Decidendi' (the underlying legal principle or reason for the decision based on material facts) forms the binding precedent. Obiter dicta are merely persuasive.",
    {"A": "Facts are unique to each case.", "B": "Correct. Ratio Decidendi is the binding legal core.", "C": "Obiter dictum is remarks made in passing (persuasive only).", "D": "Decree binds only the immediate parties."},
    "Easy", "Dias on Jurisprudence", "Identify Ratio Decidendi."
)

add_mcq(
    "mcq-jur-03-011", "ch-jur-03", "top-jur-03-02",
    "What did Professor A.L. Goodhart formulate as the test for determining the Ratio Decidendi of a case?",
    ["The ratio is found by taking the material facts of the case as found by the judge and his decision based on those facts", "The ratio is what the judge says in his headnote", "The ratio is determined by the dissenting opinion", "The ratio is found in the pleadings of the advocates"],
    0,
    "Arthur Goodhart rejected Wambaugh's inversion test, asserting that the ratio decidendi is found by taking into account the material facts of the case as identified by the judge and the decision based on those material facts.",
    {"A": "Correct. Goodhart's Material Facts Test.", "B": "Headnotes are written by publishers, not judges.", "C": "Dissent is not binding precedent.", "D": "Advocate pleadings do not constitute ratio."},
    "Medium", "Goodhart, Determining the Ratio Decidendi of a Case", "Explain Goodhart's test of ratio decidendi."
)

add_mcq(
    "mcq-jur-03-012", "ch-jur-03", "top-jur-03-02",
    "Which article of the Indian Constitution gives constitutional force to the doctrine of precedent, declaring that law declared by the Supreme Court is binding on all courts in India?",
    ["Article 136", "Article 141", "Article 142", "Article 144"],
    1,
    "Article 141 provides: 'The law declared by the Supreme Court shall be binding on all courts within the territory of India.'",
    {"A": "Article 136 is Special Leave Petition.", "B": "Correct. Article 141 embodies the binding rule of precedent.", "C": "Article 142 is complete justice power.", "D": "Article 144 mandates civil/military authorities to aid Supreme Court."},
    "Easy", "Constitution of India, Article 141", "Identify Article 141."
)

add_mcq(
    "mcq-jur-03-013", "ch-jur-03", "top-jur-03-02",
    "Is the Supreme Court of India bound by its own prior decisions under Article 141?",
    ["Yes, it is perpetually bound like the English House of Lords before 1966", "No, the Supreme Court is not bound by its own decisions and can overrule an erroneous prior precedent (Bengal Immunity Case)", "Yes, unless Parliament amends the Constitution", "Only 2-judge benches are free to overrule 5-judge benches"],
    1,
    "In Bengal Immunity Co. v. State of Bihar (1955), the Supreme Court settled that the words 'all courts within the territory of India' in Article 141 do not include the Supreme Court itself; it is free to depart from its own previous decisions to correct errors.",
    {"A": "The House of Lords Practice Statement 1966 abolished absolute self-bindingness.", "B": "Correct. Supreme Court can overrule its own prior decisions.", "C": "Overruling does not require constitutional amendment.", "D": "A smaller bench cannot overrule a larger bench."},
    "Medium", "Bengal Immunity Co. v. State of Bihar, (1955) 2 SCR 603", "Recall Bengal Immunity ruling on Article 141."
)

add_mcq(
    "mcq-jur-03-014", "ch-jur-03", "top-jur-03-02",
    "What is a precedent called when a court renders a decision 'Per Incuriam'?",
    ["A judgment delivered in open court", "A decision given in ignorance or forgetfulness of a binding statutory provision or authoritative decision of a superior court", "A decision confirmed by the full bench", "A decision based on foreign common law"],
    1,
    "A decision 'per incuriam' (literally 'through inadvertence') is one rendered in ignorance or forgetfulness of an inconsistent statutory provision or binding precedent. A per incuriam decision carries zero binding precedent value.",
    {"A": "In open court is coram publico.", "B": "Correct. Per incuriam = in ignorance of binding statute or higher authority.", "C": "Full bench is an en banc decision.", "D": "Foreign common law does not define per incuriam."},
    "Easy", "Salmond on Jurisprudence", "Define Per Incuriam."
)

add_mcq(
    "mcq-jur-03-015", "ch-jur-03", "top-jur-03-02",
    "What is the doctrine of 'Prospective Overruling', first adopted in India in I.C. Golak Nath v. State of Punjab (1967)?",
    ["The overruled law ceases to have effect only from the date of the new judgment, without invalidating past completed transactions", "The new judgment applies retrospectively to the year 1950", "The judgment takes effect only when approved by Parliament", "The judgment applies only to future generations"],
    0,
    "Subba Rao CJ adopted the American doctrine of 'Prospective Overruling' in Golak Nath: the declaration of unconstitutionality operates solely for the future, preserving the validity of past transactions done under the old law.",
    {"A": "Correct. Prospective overruling affects only future transactions.", "B": "That is retrospective overruling.", "C": "Judicial overruling does not await parliamentary consent.", "D": "Incorrect definition."},
    "Medium", "Golak Nath v. State of Punjab, AIR 1967 SC 1643", "Explain Prospective Overruling in Golak Nath."
)

add_mcq(
    "mcq-jur-03-016", "ch-jur-03", "top-jur-03-02",
    "What is an 'Obiter Dictum' in a judicial pronouncement?",
    ["A remark, illustration, or observation made by a judge in passing which is not essential to the determination of the case", "The operative decree executable against parties", "The reason for the judgment on material facts", "A preliminary objection raised by counsel"],
    0,
    "Obiter dictum ('something said by the way') is an incidental observation made by a court not necessary to the decision. While not strictly binding under English common law, considered obiter of the Supreme Court of India carries authoritative persuasive guidance.",
    {"A": "Correct. Obiter dictum is an observation made in passing.", "B": "That is the decree.", "C": "That is the ratio decidendi.", "D": "That is an argument of counsel."},
    "Easy", "Dias on Jurisprudence", "Define Obiter Dictum."
)

# top-jur-03-03: Legislation as a Source of Law
add_mcq(
    "mcq-jur-03-017", "ch-jur-03", "top-jur-03-03",
    "According to Salmond, how does Legislation differ essentially from other sources of law?",
    ["It consists in the formal declaration of legal rules by a competent sovereign authority", "It is always unwritten", "It derives its validity solely from judicial precedent", "It cannot be amended once enacted"],
    0,
    "Salmond defined legislation as 'the formal utterance of the legislative will of the state'. It differs from custom and precedent because it creates new law by deliberate positive declaration.",
    {"A": "Correct. Formal declaration of rules by competent authority.", "B": "Legislation is written enacted law (lex scripta).", "C": "Legislation is superior to precedent.", "D": "Legislation can be freely amended or repealed."},
    "Easy", "Salmond on Jurisprudence", "Define Legislation according to Salmond."
)

add_mcq(
    "mcq-jur-03-018", "ch-jur-03", "top-jur-03-03",
    "What is 'Subordinate Legislation' (Delegated Legislation)?",
    ["Legislation passed by the British Parliament for colonies", "Legislation proceeding from any authority other than the sovereign power, dependent for its validity on delegated statutory power", "Constitutional amendments under Article 368", "Ordinances issued during national emergency"],
    1,
    "Subordinate or Delegated Legislation emanates from an authority subordinate to the sovereign legislature (e.g. rules, regulations, bye-laws framed by executive departments under delegated rule-making power).",
    {"A": "Colonial legislation history.", "B": "Correct. Subordinate legislation flows from delegated authority.", "C": "Constitutional amendments are sovereign constituent acts.", "D": "Ordinances are executive legislative acts under direct constitutional power."},
    "Easy", "Salmond on Jurisprudence", "Define Subordinate/Delegated Legislation."
)

add_mcq(
    "mcq-jur-03-019", "ch-jur-03", "top-jur-03-03",
    "What did the Supreme Court lay down in the landmark In Re Delhi Laws Act, 1912 case (1951)?",
    ["Parliament can delegate its entire legislative power to the executive without limit", "Parliament cannot abdicate its essential legislative functions; it must lay down the legislative policy before delegating ancillary details", "Delegated legislation is completely unconstitutional in India", "The executive has inherent sovereign power to enact statutes"],
    1,
    "In Re Delhi Laws Act (1951 SCR 747), a 7-judge bench established that the legislature cannot abdicate its 'essential legislative function' (laying down policy); it can delegate only subsidiary administrative details.",
    {"A": "Total delegation is unconstitutional abdication.", "B": "Correct. Essential legislative function cannot be delegated.", "C": "Delegated legislation is valid within constitutional limits.", "D": "The executive has no inherent law-making power outside delegated authority or ordinances."},
    "Hard", "In Re Delhi Laws Act, 1951 SCR 747", "Recall In Re Delhi Laws Act ruling on delegated legislation."
)

add_mcq(
    "mcq-jur-03-020", "ch-jur-03", "top-jur-03-03",
    "What is 'Conditional Legislation' as distinguished from 'Delegated Legislation'?",
    ["Legislation that becomes valid only after a referendum", "Legislation complete in itself where the legislature leaves it to the executive to determine the time and manner of its application to a particular area", "Legislation conditional upon payment of taxes", "Legislation requiring presidential assent"],
    1,
    "In conditional legislation, the legislature enacts a full and complete statute, leaving only the decision of when and where to bring it into force to the executive (e.g. Section 1(3) enforcement notifications).",
    {"A": "Referendum is plebiscite.", "B": "Correct. Conditional legislation leaves determination of application time/area to executive.", "C": "Incorrect definition.", "D": "Assent is constitutional formality."},
    "Medium", "Queen v. Burah (1878) 5 IA 178", "Distinguish conditional from delegated legislation."
)

add_mcq(
    "mcq-jur-03-021", "ch-jur-03", "top-jur-03-03",
    "When a piece of delegated legislation exceeds the limits of power conferred by the parent Act, it is declared void under which doctrine?",
    ["Doctrine of Ultra Vires", "Doctrine of Severability", "Doctrine of Pith and Substance", "Doctrine of Eclipse"],
    0,
    "Subordinate legislation that exceeds the statutory authority conferred by the parent Act or violates constitutional fundamental rights is struck down as 'Ultra Vires' (beyond the powers).",
    {"A": "Correct. Ultra Vires = beyond the statutory powers.", "B": "Severability separates valid from invalid portions.", "C": "Pith and substance tests legislative competence across lists.", "D": "Eclipse applies to pre-constitutional laws violating Part III."},
    "Easy", "Administrative Law — C.K. Takwani", "Identify Doctrine of Ultra Vires."
)

add_mcq(
    "mcq-jur-03-022", "ch-jur-03", "top-jur-03-03",
    "Under what circumstances can the Governor of a State promulgate an Ordinance under Article 213 of the Constitution?",
    ["At any time the Governor wishes", "Only when the State Legislative Assembly is not in session and the Governor is satisfied that immediate action is necessary", "Only with prior consultation of the Chief Justice of the High Court", "Only during a financial emergency"],
    1,
    "Article 213 empowers the Governor to promulgate ordinances only when the state legislature is in recess and circumstances exist requiring immediate legislative action.",
    {"A": "Governor cannot bypass an active assembly.", "B": "Correct. Promulgated during legislative recess upon satisfaction of urgency.", "C": "No judicial consultation is mandated.", "D": "Financial emergency is under Article 360."},
    "Easy", "Constitution of India, Article 213", "Identify conditions for Article 213 Ordinance."
)

add_mcq(
    "mcq-jur-03-023", "ch-jur-03", "top-jur-03-03",
    "In D.C. Wadhwa v. State of Bihar (1987), the Supreme Court struck down the practice of:",
    ["Passing delegated rules without public notice", "Repromulgating ordinances repeatedly without placing them before the legislature, as a fraud on the Constitution", "Bypassing the Governor's assent", "Appointing non-legislators as ministers indefinitely"],
    1,
    "In D.C. Wadhwa, the Supreme Court struck down Bihar's practice of repromulgating hundreds of ordinances over decades without legislative debate as a 'subversion of democratic legislative process and a colorable fraud on the Constitution'.",
    {"A": "Concerning notice in rules.", "B": "Correct. Repromulgation of ordinances was declared a fraud on the Constitution.", "C": "Assent was obtained.", "D": "Dealt with in S.R. Chaudhuri v. State of Punjab."},
    "Medium", "D.C. Wadhwa v. State of Bihar, (1987) 1 SCC 378", "Recall D.C. Wadhwa ruling on ordinance re-promulgation."
)

add_mcq(
    "mcq-jur-03-024", "ch-jur-03", "top-jur-03-03",
    "Which classic canon of statutory interpretation directs courts to ascertain the intention of the legislature primarily from the literal, grammatical meaning of the words used?",
    ["The Mischief Rule (Heydon's Case)", "The Golden Rule", "The Literal Rule (Grammatical Rule)", "The Purposive Approach"],
    2,
    "The Literal Rule of interpretation holds that words in a statute must be given their ordinary, natural, grammatical meaning, unless such construction leads to absurdity or repugnancy.",
    {"A": "Mischief Rule looks at pre-existing defect and legislative remedy.", "B": "Golden Rule modifies literal meaning to prevent absurdity.", "C": "Correct. Literal rule adheres strictly to natural grammatical text.", "D": "Purposive approach looks at broader policy objectives."},
    "Easy", "Maxwell on the Interpretation of Statutes", "Define Literal Rule of statutory interpretation."
)

# -------------------------------------------------------------
# CHAPTER 4: NATURAL LAW AND SOCIAL CONTRACT
# -------------------------------------------------------------

# top-jur-04-01: Classical Natural Law (Greek & Roman)
add_mcq(
    "mcq-jur-04-001", "ch-jur-04", "top-jur-04-01",
    "Who defined Natural Law in 'De Re Publica' as 'True law is right reason in agreement with nature; it is of universal application, unchanging and everlasting'?",
    ["Aristotle", "Plato", "Marcus Tullius Cicero", "Seneca"],
    2,
    "Roman statesman and philosopher Cicero formulated the classic definition of natural law: 'Est quidem vera lex recta ratio naturae congruens, diffusa in omnes, constans, sempiterna' (True law is right reason in accord with nature).",
    {"A": "Aristotle distinguished natural from conventional justice.", "B": "Plato wrote The Republic and Laws.", "C": "Correct. Cicero formulated the classic natural law definition.", "D": "Seneca was a Stoic philosopher."},
    "Easy", "Cicero, De Re Publica, III.xxii.33", "Identify Cicero's definition of Natural Law."
)

add_mcq(
    "mcq-jur-04-002", "ch-jur-04", "top-jur-04-01",
    "Roman jurisprudence divided law into three distinct branches. What were they?",
    ["Jus Civile, Jus Gentium, and Jus Naturale", "Common Law, Equity, and Statute", "Canon Law, Feudal Law, and Maritime Law", "Constitutional Law, Criminal Law, and Civil Law"],
    0,
    "Roman jurists classified law into: (1) Jus Civile (applicable to Roman citizens), (2) Jus Gentium (universal customary law applied to foreigners), and (3) Jus Naturale (universal immutable principles dictated by natural reason).",
    {"A": "Correct. Jus Civile, Jus Gentium, and Jus Naturale.", "B": "English common law branches.", "C": "Medieval European branches.", "D": "Modern classifications."},
    "Easy", "Institutes of Justinian", "Recall Roman tripartite division of law."
)

add_mcq(
    "mcq-jur-04-003", "ch-jur-04", "top-jur-04-01",
    "Which philosophical school founded by Zeno of Citium viewed the universe as governed by universal divine reason (Logos) and urged humans to 'Live according to Nature'?",
    ["Sophists", "Stoics", "Epicureans", "Skeptics"],
    1,
    "The Stoic philosophers (Zeno, Seneca, Epictetus, Marcus Aurelius) established that nature is governed by Logos (divine universal reason) and that universal human equality stems from shared rational nature.",
    {"A": "Sophists separated nature (physis) from conventional law (nomos).", "B": "Correct. Stoics developed universal reason (Logos) and natural law.", "C": "Epicureans advocated moderate pleasure and avoidance of pain.", "D": "Skeptics doubted absolute truth."},
    "Medium", "Zeller, Stoics, Epicureans and Sceptics", "Identify Stoic school of natural law."
)

add_mcq(
    "mcq-jur-04-004", "ch-jur-04", "top-jur-04-01",
    "Aristotle distinguished between two kinds of justice in his 'Nicomachean Ethics'. What are they?",
    ["Substantive Justice and Procedural Justice", "Distributive Justice and Corrective (Remedial) Justice", "Divine Justice and Human Justice", "Civil Justice and Criminal Justice"],
    1,
    "Aristotle divided justice into: (1) Distributive Justice (fair distribution of honours, wealth, and offices according to merit), and (2) Corrective or Remedial Justice (restoring equilibrium disturbed by civil wrong or crime).",
    {"A": "Modern legal procedural distinction.", "B": "Correct. Distributive and Corrective justice.", "C": "Theological distinction.", "D": "Substantive legal branches."},
    "Medium", "Aristotle, Nicomachean Ethics, Book V", "Recall Aristotle's two types of justice."
)

add_mcq(
    "mcq-jur-04-005", "ch-jur-04", "top-jur-04-01",
    "In Sophocles' ancient Greek tragedy 'Antigone', how does Antigone justify defying King Creon's edict prohibiting the burial of her brother?",
    ["By claiming royal immunity as a princess", "By invoking the unwritten, immutable laws of the Gods that transcend mortal decrees", "By asserting an exemption under positive statute", "By claiming self-defense"],
    1,
    "Antigone defied Creon's decree, pleading that human edicts cannot override the 'unwritten and unfailing laws of the Gods, which are not of yesterday or today, but live forever'. This is the earliest literary expression of natural law over positive tyranny.",
    {"A": "Antigone claimed no personal exemption.", "B": "Correct. She appealed to eternal unwritten divine natural laws.", "C": "Creon was the supreme positive lawgiver.", "D": "Self-defense had no application."},
    "Easy", "Sophocles, Antigone, lines 450–457", "Identify literary foundation of natural law in Antigone."
)

add_mcq(
    "mcq-jur-04-006", "ch-jur-04", "top-jur-04-01",
    "Heraclitus, the pre-Socratic Greek philosopher, identified the foundation of all human laws in:",
    ["The physical decree of the tyrant", "The One Divine Law / Logos that nourishes all human laws", "The majority vote of the citizens", "Economic trade among city-states"],
    1,
    "Heraclitus declared: 'All human laws are nourished by one divine law; for it prevails as far as it wills, and suffices for all things, and overrules them all.'",
    {"A": "Tyranny is positive force.", "B": "Correct. Heraclitus linked human laws to the universal divine Logos.", "C": "Democratic voting is Athenian nomos.", "D": "Trade is commercial practice."},
    "Hard", "Heraclitus, Fragment B114", "Recall Heraclitus's concept of law and Logos."
)

add_mcq(
    "mcq-jur-04-007", "ch-jur-04", "top-jur-04-01",
    "How did the Roman 'Praetor Peregrinus' contribute to the development of universal natural law principles?",
    ["By enforcing rigid Roman ritual law on foreign merchants", "By applying equitable, fair principles of Jus Gentium drawn from common practices of Mediterranean merchants", "By abolishing all private contracts in Rome", "By creating a system of trial by ordeal"],
    1,
    "The Praetor Peregrinus (magistrate for foreigners) ignored rigid formal Roman Jus Civile and administered Jus Gentium based on equity, good faith (bona fides), and natural reason, helping universalize natural law principles.",
    {"A": "Jus Civile was restricted strictly to Roman citizens.", "B": "Correct. Praetor Peregrinus developed Jus Gentium based on commercial equity.", "C": "Contracts were expanded and enforced.", "D": "Ordeal was not a Roman legal practice."},
    "Medium", "Maine, Ancient Law, Chapter III", "Explain Praetor Peregrinus's role in Jus Gentium."
)

add_mcq(
    "mcq-jur-04-008", "ch-jur-04", "top-jur-04-01",
    "According to Cicero, what happens when a legislature enacts a statute that contradicts natural law?",
    ["It remains a valid law because Parliament is supreme", "It does not truly deserve the name of law, just as poison mixed by a robber does not deserve to be called medicine", "It can be amended only by the Pope", "Citizens must obey it blindly until repealed"],
    1,
    "Cicero famously stated in De Legibus that an unjust enactment does not deserve to be called law, just as a concoction of deadly herbs administered by an assassin cannot be termed a physician's prescription.",
    {"A": "Cicero denied legislative omnipotence against natural justice.", "B": "Correct. Unjust enactments do not possess the character of true law.", "C": "Papal authority arose in medieval times.", "D": "Blind obedience was rejected."},
    "Medium", "Cicero, De Legibus, II.v.11-13", "Recall Cicero's view on unjust legislation."
)

# top-jur-04-02: Medieval & Scholastic Natural Law
add_mcq(
    "mcq-jur-04-009", "ch-jur-04", "top-jur-04-02",
    "In his monumental 'Summa Theologiae', St. Thomas Aquinas classified Law into how many distinct tiers?",
    ["Two", "Three", "Four", "Six"],
    2,
    "Aquinas formulated the classic fourfold classification of law: (1) Lex Aeterna (Eternal Law), (2) Lex Naturalis (Natural Law), (3) Lex Divina (Divine Law), and (4) Lex Humana (Human/Positive Law).",
    {"A": "Two is dualism.", "B": "Tripartite is Roman.", "C": "Correct. Aquinas formulated four categories of law.", "D": "Six tiers is incorrect."},
    "Easy", "St. Thomas Aquinas, Summa Theologiae, I-II, qq. 90–97", "Identify Aquinas's 4 tiers of law."
)

add_mcq(
    "mcq-jur-04-010", "ch-jur-04", "top-jur-04-02",
    "How did St. Thomas Aquinas define 'Lex Naturalis' (Natural Law)?",
    ["The direct revelation in the Holy Bible", "The participation of the rational creature in the Eternal Law of God", "The statutory commands of the Pope", "The survival instinct of biological animals"],
    1,
    "Aquinas defined natural law as: 'Participatio legis aeternae in rationali creatura' (The participation of the rational creature in the eternal law of God) discoverable by human reason.",
    {"A": "That is Lex Divina (revealed scripture).", "B": "Correct. Natural law is the participation of rational creatures in eternal law.", "C": "Canon law.", "D": "Ulpian's biological concept of natural law."},
    "Medium", "Aquinas, Summa Theologiae, I-II, q. 91, a. 2", "Define Aquinas's Lex Naturalis."
)

add_mcq(
    "mcq-jur-04-011", "ch-jur-04", "top-jur-04-02",
    "What is the foundational first precept of Practical Reason according to St. Thomas Aquinas?",
    ["Might is right", "Good is to be done and pursued, and evil is to be avoided", "The greatest happiness for the greatest number", "Obey the sovereign at all costs"],
    1,
    "Aquinas laid down: 'Bonum est faciendum et prosequendum, et malum vitandum' (Good is to be done and pursued, and evil is to be avoided). All other natural precepts derive from this first principle.",
    {"A": "Thrasymachus's cynical definition.", "B": "Correct. 'Good is to be done and pursued, and evil avoided'.", "C": "Bentham's utilitarian principle.", "D": "Hobbes's sovereign absolutism."},
    "Easy", "Aquinas, Summa Theologiae, I-II, q. 94, a. 2", "Identify first precept of practical reason in Aquinas."
)

add_mcq(
    "mcq-jur-04-012", "ch-jur-04", "top-jur-04-02",
    "What did St. Thomas Aquinas rule regarding an unjust human law (Lex Injusta)?",
    ["It has the force of true law and must be worshipped", "Being contrary to reason, it is not a law, but an act of violence (magis est violentia quam lex)", "It immediately dissolves all governments", "It automatically converts into natural law"],
    1,
    "Aquinas famously wrote: 'Human law has the character of law to the extent that it accords with right reason... If it is at variance with reason, it is called an unjust law, and has not the character of law, but rather of violence.'",
    {"A": "Aquinas rejected positivist blind obedience.", "B": "Correct. Unjust law is an act of violence, not true law.", "C": "He counseled avoiding scandal and social chaos.", "D": "Illogical proposition."},
    "Medium", "Aquinas, Summa Theologiae, I-II, q. 93, a. 3", "Recall Aquinas on unjust human law."
)

add_mcq(
    "mcq-jur-04-013", "ch-jur-04", "top-jur-04-02",
    "How does Aquinas's 'Lex Divina' (Divine Law) differ from 'Lex Naturalis' (Natural Law)?",
    ["Lex Divina is discovered by natural human reason, whereas Natural Law is found in the Bible", "Lex Divina is revealed directly through sacred scriptures (Old and New Testaments), whereas Natural Law is perceived through human reason", "Lex Divina applies only to angels", "There is no difference between them in Aquinas"],
    1,
    "Lex Divina is supernatural revealed law given by God through scripture to guide humanity to eternal beatitude, whereas Lex Naturalis is accessible to all human beings through natural reason alone.",
    {"A": "Inverted definitions.", "B": "Correct. Lex Divina = Scripture; Lex Naturalis = Human reason.", "C": "Applies to mankind.", "D": "They are distinct tiers in Aquinas."},
    "Medium", "Aquinas, Summa Theologiae", "Distinguish Lex Divina from Lex Naturalis."
)

add_mcq(
    "mcq-jur-04-014", "ch-jur-04", "top-jur-04-02",
    "In medieval jurisprudence, St. Augustine of Hippo (354–430 AD) asserted that states without justice are no better than:",
    ["Monasteries", "Bands of robbers and pirates (Magna latrocinia)", "Heavenly cities", "Philosophical academies"],
    1,
    "St. Augustine famously asked in 'The City of God': 'Set justice aside, and what are kingdoms but great bands of robbers? (Remota itaque justitia, quid sunt regna nisi magna latrocinia?)'.",
    {"A": "Religious institutions.", "B": "Correct. Augustine compared unjust states to bands of robbers.", "C": "Heavenly city is Civitas Dei.", "D": "Academic academies."},
    "Easy", "St. Augustine, De Civitate Dei, IV.4", "Recall St. Augustine's quote on unjust kingdoms."
)

add_mcq(
    "mcq-jur-04-015", "ch-jur-04", "top-jur-04-02",
    "According to Aquinas, when may a citizen disobey an unjust human law?",
    ["Whenever it imposes taxes", "When the law commands an act contrary to divine law (e.g. commanding idolatry), or where disobedience does not cause greater social scandal and chaos", "Disobedience is strictly prohibited under all circumstances", "Whenever the Prime Minister belongs to another party"],
    1,
    "Aquinas held that laws contradicting divine law MUST be disobeyed; laws that are merely unjust in distributing burdens should usually be endured to avoid social scandal or riot, unless conscience dictates otherwise.",
    {"A": "Lawful taxes must be paid.", "B": "Correct. Must disobey if contrary to divine law; avoid scandal otherwise.", "C": "Totalitarianism rejected by Aquinas.", "D": "Modern party politics irrelevant."},
    "Hard", "Aquinas, Summa Theologiae, I-II, q. 96, a. 4", "Understand Aquinas's conditions for civil disobedience."
)

add_mcq(
    "mcq-jur-04-016", "ch-jur-04", "top-jur-04-02",
    "Who is regarded as the intellectual father of international law who secularized natural law in the 17th century by declaring that natural law would be valid 'even if we were to concede that God does not exist' (Etiamsi daremus non esse Deum)?",
    ["Thomas Hobbes", "Hugo Grotius", "John Locke", "Jean Bodin"],
    1,
    "Dutch jurist Hugo Grotius, in 'De Jure Belli ac Pacis' (1625), secularized natural law, stating that natural law is rooted in human social nature and reason, and would subsist even if God did not exist.",
    {"A": "Hobbes founded absolutist social contract.", "B": "Correct. Hugo Grotius secularized natural law.", "C": "Locke founded liberal property rights.", "D": "Bodin formulated sovereignty."},
    "Easy", "Grotius, De Jure Belli ac Pacis (1625), Prolegomena 11", "Identify Hugo Grotius and secularized natural law."
)

# top-jur-04-03: Social Contract Theories
add_mcq(
    "mcq-jur-04-017", "ch-jur-04", "top-jur-04-03",
    "Thomas Hobbes described human life in the primordial 'State of Nature' in 'Leviathan' (1651) as:",
    ["Peaceful, harmonious, and morally perfect", "Solitary, poor, nasty, brutish, and short", "A state of perfect freedom and equality under natural law", "A communal brotherhood sharing all property"],
    1,
    "Hobbes famously described the state of nature as a war of all against all (bellum omnium contra omnes), where life is 'solitary, poor, nasty, brutish, and short' due to the absence of a common sovereign power.",
    {"A": "Rousseau's romantic noble savage.", "B": "Correct. Hobbes's celebrated description in Chapter XIII of Leviathan.", "C": "Locke's description of state of nature.", "D": "Marx's primitive communism."},
    "Easy", "Hobbes, Leviathan, Chapter XIII", "Recall Hobbes's description of state of nature."
)

add_mcq(
    "mcq-jur-04-018", "ch-jur-04", "top-jur-04-03",
    "In Hobbes's social contract, what single inalienable right does the individual retain against the absolute Sovereign (Leviathan)?",
    ["The right to free speech", "The right to self-preservation and bodily defense of one's own life", "The right to private property", "The right to vote out the sovereign"],
    1,
    "Hobbes held that since the social contract was entered into precisely to escape violent death, no person can surrender the natural right to preserve his own life; if the sovereign commands an individual to kill himself, he has a right to resist.",
    {"A": "Free speech was suppressed under Hobbes's sovereign.", "B": "Correct. Self-preservation is the only inalienable right retained under Hobbes.", "C": "Property was subject to sovereign will.", "D": "The Leviathan cannot be voted out."},
    "Medium", "Hobbes, Leviathan, Chapter XXI", "Identify Hobbes's inalienable right to self-preservation."
)

add_mcq(
    "mcq-jur-04-019", "ch-jur-04", "top-jur-04-03",
    "According to John Locke in the 'Second Treatise of Government' (1689), what are the three fundamental Inalienable Natural Rights of individuals?",
    ["Liberty, Equality, and Fraternity", "Life, Liberty, and Estate (Property)", "Peace, Bread, and Land", "Right to Work, Rest, and Leisure"],
    1,
    "Locke established that individuals possess inherent natural rights to 'Life, Liberty, and Estate' (collectively termed Property), which exist prior to government and which governments are instituted to protect.",
    {"A": "Motto of the French Revolution.", "B": "Correct. Locke's triad of Life, Liberty, and Property.", "C": "Bolshevik slogan.", "D": "Universal Declaration socioeconomic rights."},
    "Easy", "Locke, Second Treatise of Government, Section 87", "Recall Locke's natural rights triad."
)

add_mcq(
    "mcq-jur-04-020", "ch-jur-04", "top-jur-04-03",
    "What is the consequence under John Locke's theory if the sovereign government systematically breaches its fiduciary trust and violates natural rights?",
    ["The people must submit patiently", "The people have the legitimate right of revolution to dissolve the government and establish a new legislature", "The government automatically becomes a military dictatorship", "The country reverts permanently to the state of nature"],
    1,
    "Locke argued that government holds power as a fiduciary trustee; when government betrays trust by violating life, liberty, and property, the trust is forfeited and citizens have the 'right to appeal to Heaven' (revolution).",
    {"A": "Hobbes's stance of absolute submission.", "B": "Correct. Locke's right of revolution against tyrannical rulers.", "C": "Incorrect outcome.", "D": "Locke envisioned reconstituting civil government."},
    "Medium", "Locke, Second Treatise, Chapter XIX", "Understand Locke's Right of Revolution."
)

add_mcq(
    "mcq-jur-04-021", "ch-jur-04", "top-jur-04-03",
    "Jean-Jacques Rousseau opened 'The Social Contract' (1762) with which famous maxim?",
    ["Property is theft", "Man is born free, and everywhere he is in chains", "Workers of the world unite", "God is dead"],
    1,
    "Rousseau's immortal opening line: 'Man is born free, and everywhere he is in chains' (L'homme est né libre, et partout il est dans les fers).",
    {"A": "Proudhon's socialist slogan.", "B": "Correct. Rousseau's iconic opening sentence.", "C": "Marx's closing line.", "D": "Nietzsche's statement."},
    "Easy", "Rousseau, The Social Contract, Book I, Chapter 1", "Recall Rousseau's opening dictum."
)

add_mcq(
    "mcq-jur-04-022", "ch-jur-04", "top-jur-04-03",
    "What central political concept did Rousseau invent to reconcile individual liberty with political authority?",
    ["The Rule of Law", "The General Will (Volonté Générale)", "The Separation of Powers", "The Doctrine of Basic Structure"],
    1,
    "Rousseau resolved the tension between freedom and authority through the 'General Will' (Volonté Générale) — the common collective interest aimed at the public good, to which each citizen surrenders private selfish wills.",
    {"A": "Dicey's concept.", "B": "Correct. Rousseau's General Will.", "C": "Montesquieu's doctrine.", "D": "Indian Supreme Court doctrine."},
    "Medium", "Rousseau, The Social Contract, Book II", "Define Rousseau's General Will."
)

add_mcq(
    "mcq-jur-04-023", "ch-jur-04", "top-jur-04-03",
    "Which American constitutional document directly incorporated John Locke's natural rights philosophy, modifying Locke's triad to 'Life, Liberty and the pursuit of Happiness'?",
    ["The Articles of Confederation (1777)", "The Declaration of Independence (1776)", "The Federalist Papers (1787)", "The Monroe Doctrine (1823)"],
    1,
    "Thomas Jefferson drafted the American Declaration of Independence (1776), directly adapting Locke's natural law doctrine: 'that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness'.",
    {"A": "Early US constitutional compact.", "B": "Correct. American Declaration of Independence (1776).", "C": "Essays defending the US Constitution.", "D": "Foreign policy doctrine."},
    "Easy", "US Declaration of Independence, 1776", "Link Locke to US Declaration of Independence."
)

add_mcq(
    "mcq-jur-04-024", "ch-jur-04", "top-jur-04-03",
    "How does Rousseau's 'General Will' (Volonté Générale) differ from the 'Will of All' (Volonté de tous)?",
    ["There is no difference in Rousseau's philosophy", "The General Will aims at the common collective interest of the community, while the Will of All is merely the sum of private selfish interests", "The Will of All is supreme over the General Will", "The General Will applies only during wartime"],
    1,
    "Rousseau explained: 'There is often a great deal of difference between the will of all and the general will; the latter considers only the common interest, while the former takes private interest into account, and is no more than a sum of particular wills.'",
    {"A": "Rousseau drew a profound distinction.", "B": "Correct. General Will = Common interest; Will of All = Sum of private selfish interests.", "C": "General Will is supreme.", "D": "It applies in all political life."},
    "Hard", "Rousseau, The Social Contract, Book II, Chapter 3", "Distinguish General Will from Will of All."
)

# top-jur-04-04: Revival of Natural Law in the 20th Century
add_mcq(
    "mcq-jur-04-025", "ch-jur-04", "top-jur-04-04",
    "Who is known for propounding the concept of 'Natural Law with a Variable Content' (Naturrecht mit wechselndem Inhalte)?",
    ["Rudolf Stammler", "Lon L. Fuller", "Gustav Radbruch", "John Finnis"],
    0,
    "German Neo-Kantian jurist Rudolf Stammler reconciled absolute natural justice with historical variability by formulating 'Natural Law with a Variable Content': the ideal of justice is universal, but its application changes with social conditions.",
    {"A": "Correct. Rudolf Stammler formulated natural law with a variable content.", "B": "Fuller developed internal procedural morality.", "C": "Radbruch formulated the Radbruch formula.", "D": "Finnis formulated 7 basic human goods."},
    "Medium", "Stammler, The Theory of Justice", "Identify Stammler's Natural Law with Variable Content."
)

add_mcq(
    "mcq-jur-04-026", "ch-jur-04", "top-jur-04-04",
    "What is the 'Radbruch Formula' formulated by German jurist Gustav Radbruch following the atrocities of the Nazi regime?",
    ["Laws passed by Parliament can never be questioned", "Where statutory law is so intolerably unjust that it violates fundamental equality, the statute loses its legal quality and must yield to justice (Statutory Non-Law)", "International courts have no jurisdiction over domestic laws", "Natural law is purely aesthetic"],
    1,
    "The Radbruch Formula (1946) established that extreme injustice is not law (Gesetzliches Unrecht und übergesetzliches Recht): where the contradiction between positive law and justice reaches an intolerable level, positive law ceases to be valid law.",
    {"A": "Extreme positivist view rejected by Radbruch.", "B": "Correct. The Radbruch Formula: Intolerable injustice ceases to be valid law.", "C": "Radbruch supported Nuremberg trials.", "D": "It is deeply normative."},
    "Medium", "Radbruch, Statutory Lawlessness and Supra-Statutory Law (1946)", "Define the Radbruch Formula."
)

add_mcq(
    "mcq-jur-04-027", "ch-jur-04", "top-jur-04-04",
    "In 'Natural Law and Natural Rights' (1980), Oxford legal philosopher John Finnis identified how many 'Basic Goods' of human flourishing?",
    ["Five", "Seven", "Nine", "Twelve"],
    1,
    "John Finnis revived neo-Thomistic natural law without committing the naturalistic fallacy, identifying Seven Self-Evident Basic Goods: Life, Knowledge, Play, Aesthetic Experience, Sociability/Friendship, Practical Reasonableness, and Religion.",
    {"A": "Aristotelian categories.", "B": "Correct. Finnis identified 7 Basic Goods of human flourishing.", "C": "Incorrect number.", "D": "Incorrect number."},
    "Easy", "John Finnis, Natural Law and Natural Rights (1980)", "Recall Finnis's 7 Basic Goods."
)

add_mcq(
    "mcq-jur-04-028", "ch-jur-04", "top-jur-04-04",
    "Which Indian constitutional judgment revitalized Natural Law principles by reading 'fair, just and reasonable' procedural due process into Article 21?",
    ["A.K. Gopalan v. State of Madras (1950)", "Maneka Gandhi v. Union of India (1978)", "ADM Jabalpur v. Shivkant Shukla (1976)", "Minerva Mills v. Union of India (1980)"],
    1,
    "In Maneka Gandhi (1978), the Supreme Court overruled A.K. Gopalan, holding that procedure established by law under Article 21 cannot be arbitrary or oppressive; it must be right, just, and fair, embodying principles of natural justice.",
    {"A": "Gopalan took a rigid positivist literal approach.", "B": "Correct. Maneka Gandhi revived natural justice under Article 21.", "C": "ADM Jabalpur took an extreme positivist stance during Emergency.", "D": "Minerva Mills concerned basic structure."},
    "Easy", "Maneka Gandhi v. Union of India, (1978) 1 SCC 248", "Link Maneka Gandhi to modern revival of natural law."
)

add_mcq(
    "mcq-jur-04-029", "ch-jur-04", "top-jur-04-04",
    "The Principles of Natural Justice in Indian administrative law comprise two core Latin maxims. What are they?",
    ["Nemo judex in causa sua & Audi alteram partem", "Caveat emptor & Res ipsa loquitur", "Volenti non fit injuria & Actus reus", "Damnum sine injuria & Injuria sine damno"],
    0,
    "Natural justice consists of: (1) Nemo judex in causa sua (Rule against bias — no one should be a judge in his own cause), and (2) Audi alteram partem (Right to a fair hearing — hear the other side).",
    {"A": "Correct. The two pillars of Natural Justice.", "B": "Commercial and tort doctrines.", "C": "Tort defenses and criminal components.", "D": "Tortious injury concepts."},
    "Easy", "A.K. Kraipak v. Union of India, AIR 1970 SC 150", "Identify the two maxims of natural justice."
)

add_mcq(
    "mcq-jur-04-030", "ch-jur-04", "top-jur-04-04",
    "What did the Supreme Court establish in A.K. Kraipak v. Union of India (1970) regarding the applicability of Natural Justice?",
    ["Natural justice applies only to judicial courts, not administrative bodies", "The dividing line between quasi-judicial and administrative powers is blurred; principles of natural justice apply equally to administrative proceedings", "Natural justice has been abolished by Parliament", "Natural justice applies only in criminal trials"],
    1,
    "Hegde J in A.K. Kraipak established that the aim of natural justice is to prevent miscarriage of justice; it applies to administrative proceedings as well as quasi-judicial inquiries.",
    {"A": "Old restrictive view rejected in Kraipak.", "B": "Correct. Natural justice applies to administrative actions.", "C": "Natural justice is an integral constitutional norm.", "D": "Applies across all civil/administrative domains."},
    "Medium", "A.K. Kraipak v. Union of India, (1969) 2 SCC 262", "Recall A.K. Kraipak ruling on natural justice."
)

add_mcq(
    "mcq-jur-04-031", "ch-jur-04", "top-jur-04-04",
    "Lon Fuller's famous debate with H.L.A. Hart in the Harvard Law Review (1958) centered on which wartime dilemma?",
    ["The trial of Japanese military leaders in Tokyo", "The Post-War German 'Grudge Informer' cases (spouses who reported each other under Nazi statutes)", "The Nuremberg economic sanctions", "The partition of British India"],
    1,
    "The Hart-Fuller Debate revolved around the post-war German Grudge Informer trials: whether a woman who denounced her husband under Nazi laws to get rid of him could be prosecuted, testing whether Nazi laws were valid positive law or void non-law.",
    {"A": "Tokyo war crimes tribunal.", "B": "Correct. The Grudge Informer problem tested positivism vs natural law.", "C": "Economic trials.", "D": "Indian partition."},
    "Medium", "Hart-Fuller Debate, (1958) 71 Harvard Law Review", "Identify the Grudge Informer case in Hart-Fuller debate."
)

add_mcq(
    "mcq-jur-04-032", "ch-jur-04", "top-jur-04-04",
    "Which modern philosophical theory of justice formulated by John Rawls utilizes the concepts of the 'Original Position' and the 'Veil of Ignorance'?",
    ["Utilitarianism", "Justice as Fairness", "Historical Materialism", "Libertarian Entitlement Theory"],
    1,
    "John Rawls, in 'A Theory of Justice' (1971), formulated 'Justice as Fairness', where free and rational persons behind a 'Veil of Ignorance' in the 'Original Position' agree on principles of equal basic liberty and the Difference Principle.",
    {"A": "Rawls explicitly rejected utilitarianism.", "B": "Correct. Rawls's Justice as Fairness.", "C": "Marxist theory.", "D": "Nozick's entitlement theory."},
    "Easy", "John Rawls, A Theory of Justice (1971)", "Identify John Rawls's Justice as Fairness."
)

# -------------------------------------------------------------
# CHAPTER 5: HISTORICAL SCHOOL OF JURISPRUDENCE
# -------------------------------------------------------------

# top-jur-05-01: Friedrich Carl von Savigny & Volksgeist
add_mcq(
    "mcq-jur-05-001", "ch-jur-05", "top-jur-05-01",
    "Who is universally celebrated as the 'Father of the Historical School of Jurisprudence'?",
    ["Sir Henry Maine", "Friedrich Carl von Savigny", "Georg Friedrich Puchta", "Hugo Grotius"],
    1,
    "Friedrich Carl von Savigny (1779–1861) is the founder and father of the Historical School, reacting against 18th-century rationalism and French codification.",
    {"A": "Maine is the founder of English historical/anthropological jurisprudence.", "B": "Correct. Savigny is the father of the Historical School.", "C": "Puchta was Savigny's prominent disciple.", "D": "Grotius founded modern natural law."},
    "Easy", "Dias on Jurisprudence", "Identify the father of the Historical School."
)

add_mcq(
    "mcq-jur-05-002", "ch-jur-05", "top-jur-05-01",
    "What does Savigny's central concept of 'Volksgeist' mean?",
    ["The statutory decree of the legislature", "The national spirit or common consciousness of the people", "The sovereign will of the monarch", "The divine revelation of the church"],
    1,
    "Volksgeist means the 'Spirit of the People' or national consciousness. Savigny posited that law grows organically out of the internal convictions, manners, and spirit of a nation, like language and culture.",
    {"A": "Austin's positivist concept.", "B": "Correct. Volksgeist = National spirit / common consciousness of the people.", "C": "Hobbes's sovereign will.", "D": "Theological canon law."},
    "Easy", "Savigny, Of the Vocation of Our Age for Legislation", "Define Volksgeist."
)

add_mcq(
    "mcq-jur-05-003", "ch-jur-05", "top-jur-05-01",
    "Savigny's famous 1814 pamphlet 'On the Vocation of Our Age for Legislation and Jurisprudence' was written in vehement opposition to the codification proposal of which German professor?",
    ["Professor A.F.J. Thibaut", "Professor Rudolf von Ihering", "Professor Georg Puchta", "Professor Max Weber"],
    0,
    "Professor Thibaut published a tract in 1814 urging immediate unified codification of civil law for Germany (modeled on the Code Napoléon). Savigny wrote his famous rebuttal opposing premature codification.",
    {"A": "Correct. The Thibaut-Savigny Controversy of 1814.", "B": "Ihering was a later sociological jurist.", "C": "Puchta supported Savigny.", "D": "Weber was a 20th-century sociologist."},
    "Medium", "Thibaut-Savigny Controversy 1814", "Identify Savigny's opponent in codification controversy."
)

add_mcq(
    "mcq-jur-05-004", "ch-jur-05", "top-jur-05-01",
    "Which of the following aphorisms summarizes Savigny's fundamental view on how law comes into existence?",
    ["Law is made by the command of the sovereign", "Law is found, not made; it grows with the growth and strengthens with the strength of the people", "Law is the prediction of judicial rulings", "Law is an instrument of class exploitation"],
    1,
    "Savigny famously held: 'Das Recht wird nicht gemacht, es ist und wird mit dem Volke' (Law is not made, it grows with the people, develops with their growth, and finally dies away as the nation loses its nationality).",
    {"A": "Austin's positivist axiom.", "B": "Correct. Law is found, not made; grows organically.", "C": "Holmes's realist dictum.", "D": "Marxist materialist axiom."},
    "Easy", "Savigny, Of the Vocation of Our Age", "Recall Savigny's core aphorism on law."
)

add_mcq(
    "mcq-jur-05-005", "ch-jur-05", "top-jur-05-01",
    "According to Savigny, who represents the popular consciousness (Volksgeist) in modern advanced societies as law becomes complex and technical?",
    ["The Police and Military", "The Jurists and Lawyers", "The Executive Ministers", "Foreign Arbitrators"],
    1,
    "Savigny explained that as civilization advances, law develops a technical, scientific side; the popular consciousness is represented by the Jurists (lawyers and scholars), who formulate the scientific principles of customary law.",
    {"A": "Forces of state coercion.", "B": "Correct. Jurists represent the mature popular consciousness.", "C": "Political executives.", "D": "Foreign bodies have no national Volksgeist."},
    "Medium", "Savigny, System of Modern Roman Law", "Identify the role of Jurists in Savigny's theory."
)

add_mcq(
    "mcq-jur-05-006", "ch-jur-05", "top-jur-05-01",
    "Which German jurist, a disciple of Savigny, popularized and formally coined the German term 'Volksgeist'?",
    ["Georg Friedrich Puchta", "Rudolf Stammler", "Otto von Gierke", "Karl Marx"],
    0,
    "Puchta, Savigny's most brilliant disciple, formally coined and systematized the term 'Volksgeist' into a structured jurisprudential doctrine in his 'Outlines of Jurisprudence' (1828).",
    {"A": "Correct. Puchta formally developed and named the Volksgeist doctrine.", "B": "Stammler was neo-Kantian.", "C": "Gierke championed the Realist theory.", "D": "Marx rejected historical romanticism."},
    "Medium", "Puchta, Gewohnheitsrecht (1828)", "Identify Puchta's role in Volksgeist."
)

add_mcq(
    "mcq-jur-05-007", "ch-jur-05", "top-jur-05-01",
    "What is the major historical inconsistency in Savigny's Volksgeist theory pointed out by critics?",
    ["Savigny was a French general", "While exalting German popular custom, Savigny devoted his life to championing the reception of foreign Roman Law in Germany", "Savigny completely ignored property rights", "Savigny supported violent socialist revolution"],
    1,
    "Critics (like Allen and Dias) highlighted the glaring paradox that Savigny romanticized German Volksgeist while passionately promoting the 'Reception of Roman Law' — a foreign imperial legal system alien to early Germanic custom.",
    {"A": "Savigny was a Prussian scholar.", "B": "Correct. The paradox of championing foreign Roman Law while praising German Volksgeist.", "C": "Savigny wrote extensively on possession and property.", "D": "Savigny was a deeply conservative aristocrat."},
    "Hard", "Dias on Jurisprudence", "Analyze major criticism of Savigny's theory."
)

add_mcq(
    "mcq-jur-05-008", "ch-jur-05", "top-jur-05-01",
    "How did Savigny view the role of formal Legislation by Parliament?",
    ["Legislation is the supreme creative source of all new law", "Legislation is only the final formal recording of mature customary law, not an autonomous source of deliberate social change", "Legislation is unconstitutional", "Legislation is identical to natural law"],
    1,
    "Savigny maintained that legislation cannot create new law; it merely gives formal written shape to legal rules that have already matured through national custom and juristic science.",
    {"A": "Positivist view (Bentham/Austin).", "B": "Correct. Legislation is merely the final declaratory stage of mature custom.", "C": "Savigny did not deem legislation unconstitutional.", "D": "Natural law was rejected by Savigny."},
    "Medium", "Savigny, Of the Vocation of Our Age", "Understand Savigny's view on legislation."
)

# top-jur-05-02: Sir Henry Maine
add_mcq(
    "mcq-jur-05-009", "ch-jur-05", "top-jur-05-02",
    "Sir Henry Maine authored which monumental 1861 treatise founding English historical and anthropological jurisprudence?",
    ["Ancient Law", "The Province of Jurisprudence Determined", "The Common Law", "The Law of the Constitution"],
    0,
    "Sir Henry Maine published 'Ancient Law: Its Connection with the Early History of Society and Its Relation to Modern Ideas' in 1861, pioneering comparative historical jurisprudence.",
    {"A": "Correct. Maine's Ancient Law (1861).", "B": "Austin's work (1832).", "C": "Holmes's work (1881).", "D": "Dicey's work (1885)."},
    "Easy", "Sir Henry Maine, Ancient Law (1861)", "Identify Maine's monumental treatise."
)

add_mcq(
    "mcq-jur-05-010", "ch-jur-05", "top-jur-05-02",
    "What famous evolutionary dictum did Sir Henry Maine formulate regarding the development of law in progressive societies?",
    ["Law is the command of the sovereign", "The movement of the progressive societies has hitherto been a movement from Status to Contract", "Law is social engineering", "The life of the law has not been logic; it has been experience"],
    1,
    "Maine's immortal dictum: 'The movement of the progressive societies has hitherto been a movement from Status to Contract' (Chapter V, Ancient Law), describing how individual autonomous bargaining replaced inherited feudal/family status.",
    {"A": "Austin's dictum.", "B": "Correct. Maine's Status to Contract dictum.", "C": "Roscoe Pound's dictum.", "D": "O.W. Holmes Jr.'s dictum."},
    "Easy", "Maine, Ancient Law, Chapter V", "Recall Maine's Status to Contract dictum."
)

add_mcq(
    "mcq-jur-05-011", "ch-jur-05", "top-jur-05-02",
    "According to Sir Henry Maine, what are the three agencies by which progressive societies bring law into harmony with changing social needs, in chronological order?",
    ["Custom, Precedent, and Legislation", "Legal Fictions, Equity, and Legislation", "King, Aristocracy, and Democracy", "Religion, Philosophy, and Positive Law"],
    1,
    "Maine laid down the exact historical order of legal adaptation in progressive societies: (1) Legal Fictions, (2) Equity, and (3) Legislation.",
    {"A": "General sources of law.", "B": "Correct. Maine's three agencies: Fictions -> Equity -> Legislation.", "C": "Political forms.", "D": "Philosophical stages."},
    "Medium", "Maine, Ancient Law, Chapter II", "Identify Maine's three agencies of legal adaptation."
)

add_mcq(
    "mcq-jur-05-012", "ch-jur-05", "top-jur-05-02",
    "How did Sir Henry Maine define a 'Legal Fiction'?",
    ["A fraudulent misrepresentation made to a court", "Any assumption which conceals, or affects to conceal, the fact that a rule of law has undergone alteration, its letter remaining unchanged, its operation being modified", "A fictional narrative used in literature", "A statute that has been repealed by Parliament"],
    1,
    "Maine defined legal fiction as any assumption that masks legal change: the letter of the law remains unchanged, but its practical application is altered to meet new needs (e.g. Roman Praetorian edicts, English ejectment actions).",
    {"A": "Civil fraud definition.", "B": "Correct. Maine's classical definition of legal fiction.", "C": "Literary fiction.", "D": "Repealed statute."},
    "Medium", "Maine, Ancient Law, Chapter II", "Define Legal Fiction according to Maine."
)

add_mcq(
    "mcq-jur-05-013", "ch-jur-05", "top-jur-05-02",
    "In ancient early society, what were 'Themistes' according to Sir Henry Maine?",
    ["Written parliamentary statutes", "Divinely inspired judicial awards delivered by kings or patriarchal chiefs in individual disputes", "Customs observed by merchants", "Philosophical treaties on ethics"],
    1,
    "Maine traced the earliest stage of law to 'Themistes' — divinely inspired judicial pronouncements delivered by kings as patriarchal arbiters before the existence of customary or statutory rules.",
    {"A": "Statutes are the final stage.", "B": "Correct. Themistes = Divinely inspired patriarchal judicial awards.", "C": "Customs developed later in stage two.", "D": "Philosophical writings."},
    "Medium", "Maine, Ancient Law, Chapter I", "Define Themistes in Maine's legal evolution."
)

add_mcq(
    "mcq-jur-05-014", "ch-jur-05", "top-jur-05-02",
    "According to Maine, what four distinct chronological stages mark the early development of law?",
    ["Themistes (Royal Awards) -> Customary Law -> Aristocratic Monopolies -> Codes", "Codes -> Custom -> Legislation -> Equity", "Natural Law -> Positive Law -> Realism -> Sociology", "Fictions -> Custom -> Equity -> Precedent"],
    0,
    "Maine outlined the four early stages: (1) Rulings by patriarchal kings (Themistes), (2) Customary law practiced by communities, (3) Administration of customs by aristocratic oligarchies, and (4) Era of Written Codes (e.g. Twelve Tables, Manu).",
    {"A": "Correct. Themistes -> Customs -> Aristocratic monopoly -> Era of Codes.", "B": "Inverted order.", "C": "Philosophical schools.", "D": "Incorrect sequence."},
    "Hard", "Maine, Ancient Law, Chapter I", "Identify Maine's 4 stages of early legal development."
)

add_mcq(
    "mcq-jur-05-015", "ch-jur-05", "top-jur-05-02",
    "Why did Sir Henry Maine describe the movement from status to contract as limited strictly to 'progressive societies'?",
    ["Because all societies on earth progress at the same rate", "Because stationary societies (the vast majority in history) stopped developing after the stage of the Code, whereas only a few Western societies continued developing through fictions, equity, and legislation", "Because contract law was invented only in England", "Because status was prohibited by international law"],
    1,
    "Maine emphasized that the vast majority of human societies became 'stationary' once their laws were codified into codes; only a small handful of 'progressive societies' (Western civilization) moved forward from status to contract.",
    {"A": "Maine rejected universal uniform progress.", "B": "Correct. Stationary vs Progressive societies distinction.", "C": "Contract existed in Roman law.", "D": "Status was the universal primordial unit."},
    "Medium", "Maine, Ancient Law, Chapter II", "Distinguish stationary from progressive societies."
)

add_mcq(
    "mcq-jur-05-016", "ch-jur-05", "top-jur-05-02",
    "In the 20th century, how has modern welfare legislation (labor laws, rent control, standard form contracts) affected Maine's dictum 'from Status to Contract'?",
    ["It has accelerated the movement towards absolute unrestricted individual contract", "It has created a counter-movement from 'Contract back to Status', where statutory rights and protective terms are imposed based on an individual's status (worker, tenant, consumer)", "It has abolished all contract law", "It has confirmed Maine's prediction without any deviation"],
    1,
    "Modern jurists (like Dicey and Friedmann) observed a reverse trend: modern welfare legislation attaches non-negotiable protective terms to individuals based on their status (employee, tenant, consumer), showing a shift from Contract back to Status.",
    {"A": "Individual bargaining has been restricted in welfare states.", "B": "Correct. Re-emergence of status to protect weaker parties.", "C": "Contract law remains vital.", "D": "The counter-trend modifies Maine's thesis."},
    "Medium", "Friedmann, Law in a Changing Society", "Analyze the counter-movement from Contract to Status."
)
