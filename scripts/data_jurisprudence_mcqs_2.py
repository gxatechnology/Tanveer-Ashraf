"""
Jurisprudence MCQs - Chapters 6 to 11 (112 MCQs)
Topics: top-jur-06-01 to top-jur-11-03
8 MCQs per topic
"""

MCQS_PART2 = []

def add_mcq(mid, cid, tid, q, opts, ans_idx, exp, ob, diff, prov, lo):
    letters = ["A", "B", "C", "D"]
    MCQS_PART2.append({
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
# CHAPTER 6: SOCIOLOGICAL SCHOOL OF JURISPRUDENCE
# -------------------------------------------------------------

# top-jur-06-01: Ihering, Ehrlich, Duguit
add_mcq(
    "mcq-jur-06-001", "ch-jur-06", "top-jur-06-01",
    "Who is universally celebrated as the 'Father of Modern Sociological Jurisprudence'?",
    ["Rudolf von Ihering", "Eugen Ehrlich", "Léon Duguit", "Roscoe Pound"],
    0,
    "Rudolf von Ihering (1818–1892) is regarded as the father of modern sociological jurisprudence because he shifted focus from conceptual abstractions to practical purpose in law.",
    {"A": "Correct. Ihering is the father of modern sociological jurisprudence.", "B": "Ehrlich founded sociology of living law.", "C": "Duguit propounded social solidarity.", "D": "Pound developed American sociological jurisprudence."},
    "Easy", "Ihering, Law as a Means to an End", "Identify the father of modern sociological jurisprudence."
)

add_mcq(
    "mcq-jur-06-002", "ch-jur-06", "top-jur-06-01",
    "What famous dictum did Rudolf von Ihering formulate in 'Der Zweck im Recht' (Law as a Means to an End)?",
    ["Law is the command of the sovereign", "Purpose is the creator of the entire law", "Law is found, not made", "Law is a prediction of what courts will do"],
    1,
    "Ihering established that 'Purpose is the creator of the entire law' (Der Zweck ist der Schöpfer des ganzen Rechts). There is no legal rule which does not owe its origin to a practical social purpose.",
    {"A": "Austin's command dictum.", "B": "Correct. 'Purpose is the creator of all law'.", "C": "Savigny's historical dictum.", "D": "Holmes's realist dictum."},
    "Easy", "Ihering, Der Zweck im Recht (1877)", "Recall Ihering's purpose dictum."
)

add_mcq(
    "mcq-jur-06-003", "ch-jur-06", "top-jur-06-01",
    "In 'The Struggle for Law' (Der Kampf ums Recht), what did Ihering argue regarding the achievement of legal rights?",
    ["Law develops effortlessly and organically like language", "Law is not an effortless organic growth, but a continuous human struggle against injustice", "Law is created solely by divine intervention", "Law should be abandoned in favor of passive meditation"],
    1,
    "Ihering revolted against Savigny's passive organic model, asserting that all law in the world has been obtained by struggle; every legal principle had to be wrung from those who resisted it.",
    {"A": "Savigny's romantic view attacked by Ihering.", "B": "Correct. Law is achieved through conscious human struggle against injustice.", "C": "Theological view.", "D": "Passive fatalism."},
    "Medium", "Ihering, The Struggle for Law (1872)", "Recall Ihering's struggle for law thesis."
)

add_mcq(
    "mcq-jur-06-004", "ch-jur-06", "top-jur-06-01",
    "Austrian jurist Eugen Ehrlich propounded that the center of gravity of legal development lies in:",
    ["Legislation passed by Parliament", "Judicial decisions of supreme courts", "Juristic science and scholarly commentaries", "Society itself (The Living Law)"],
    3,
    "Ehrlich opened 'Fundamental Principles of the Sociology of Law' (1913) with the celebrated proposition: 'At the present as well as at any other time, the center of gravity of legal development lies not in legislation, nor in juristic science, nor in judicial decisions, but in society itself.'",
    {"A": "Bentham/Austin positivist view.", "B": "Realist court-centric view.", "C": "Savigny's mature juristic stage.", "D": "Correct. Ehrlich's center of gravity is society itself."},
    "Easy", "Eugen Ehrlich, Fundamental Principles of the Sociology of Law", "Recall Ehrlich's center of gravity dictum."
)

add_mcq(
    "mcq-jur-06-005", "ch-jur-06", "top-jur-06-01",
    "What did Eugen Ehrlich term 'The Living Law' (Lebendes Recht)?",
    ["Statutes enacted by living parliamentarians", "The actual norms and inner orders that dominate daily social relations and associations, whether recognized by state courts or not", "The natural law written in the human heart", "The unwritten constitution of Great Britain"],
    1,
    "Ehrlich defined 'Living Law' as the actual rules of conduct observed by people in their commercial, family, and social associations, which dominates life even if never enacted into statute or enforced by courts.",
    {"A": "Positive statutory law.", "B": "Correct. The living social norms governing human associations.", "C": "Theological natural law.", "D": "British constitutional convention."},
    "Medium", "Ehrlich, Sociology of Law", "Define Ehrlich's Living Law."
)

add_mcq(
    "mcq-jur-06-006", "ch-jur-06", "top-jur-06-01",
    "French jurist Léon Duguit replaced the traditional legal concepts of Sovereignty and Individual Rights with which single foundational doctrine?",
    ["The Categorical Imperative", "Social Solidarity (Solidarité Sociale)", "The Dictatorship of the Proletariat", "The Living Law"],
    1,
    "Léon Duguit rejected state sovereignty and subjective rights as metaphysical myths, founding his entire jurisprudence on 'Social Solidarity' — the inescapable mutual interdependence of humans in modern society.",
    {"A": "Kant's moral principle.", "B": "Correct. Duguit's Social Solidarity.", "C": "Marxist political doctrine.", "D": "Ehrlich's concept."},
    "Easy", "Léon Duguit, Law in the Modern State (1913)", "Identify Duguit's Social Solidarity."
)

add_mcq(
    "mcq-jur-06-007", "ch-jur-06", "top-jur-06-01",
    "What was Léon Duguit's radical view regarding 'Individual Legal Rights'?",
    ["Individual rights are absolute and sacred natural rights", "No individual possesses any rights; an individual possesses only social duties and functions to serve social solidarity", "Rights are created solely by the police", "Rights exist only for property owners"],
    1,
    "Duguit eliminated subjective rights: 'The only right which any man can possess is the right always to do his duty' — individuals have only social functions and obligations to maintain social solidarity.",
    {"A": "Locke's natural rights theory.", "B": "Correct. Duguit denied individual rights, recognizing only social duties.", "C": "Authoritarian force.", "D": "Feudal concept."},
    "Medium", "Duguit, Traité de Droit Constitutionnel", "Recall Duguit's denial of subjective rights."
)

add_mcq(
    "mcq-jur-06-008", "ch-jur-06", "top-jur-06-01",
    "In which landmark case did the Supreme Court of India adopt Duguit's Social Solidarity doctrine to recognize the right of workers to be heard in company winding-up petitions?",
    ["National Textile Workers' Union v. P.R. Ramakrishnan", "Salomon v. Salomon", "Bengal Immunity v. State of Bihar", "Bachan Singh v. State of Punjab"],
    0,
    "In National Textile Workers' Union (1983), Bhagwati J applied sociological jurisprudence and social solidarity, holding that a company is not just capital, but a social partnership between labor and capital; workers must be heard before winding up.",
    {"A": "Correct. National Textile Workers' Union, (1983) 1 SCC 228.", "B": "English corporate personality landmark.", "C": "Constitutional precedent on Article 141.", "D": "Death penalty sentencing landmark."},
    "Hard", "National Textile Workers' Union, (1983) 1 SCC 228", "Link Duguit to Indian corporate labor jurisprudence."
)

# top-jur-06-02: Roscoe Pound
add_mcq(
    "mcq-jur-06-009", "ch-jur-06", "top-jur-06-02",
    "Dean Roscoe Pound famously characterized the primary function of Law as:",
    ["The command of sovereign backed by coercion", "Social Engineering", "The preservation of the status quo", "The manifestation of Volksgeist"],
    1,
    "Roscoe Pound defined law as 'Social Engineering' — the balancing and harmonizing of competing human interests with the least friction and waste of social resources.",
    {"A": "Austin's command theory.", "B": "Correct. Pound's Social Engineering.", "C": "Conservative positivism.", "D": "Savigny's historical theory."},
    "Easy", "Roscoe Pound, Social Control Through Law (1942)", "Recall Pound's metaphor of Social Engineering."
)

add_mcq(
    "mcq-jur-06-010", "ch-jur-06", "top-jur-06-02",
    "Into what three broad categories did Roscoe Pound classify the human 'Interests' that the legal system must balance?",
    ["Natural, Moral, and Legal Interests", "Individual Interests, Public Interests, and Social Interests", "Substantive, Procedural, and Remedial Interests", "Civil, Criminal, and Constitutional Interests"],
    1,
    "Pound classified interests into: (1) Individual Interests (personality, domestic relations, substance/property), (2) Public Interests (interests of the state as a political person), and (3) Social Interests (general security, morals, conservation).",
    {"A": "Philosophical categories.", "B": "Correct. Individual, Public, and Social Interests.", "C": "Procedural classification.", "D": "Subject branches."},
    "Easy", "Roscoe Pound, A Survey of Social Interests (1943)", "Recall Pound's 3 classes of interests."
)

add_mcq(
    "mcq-jur-06-011", "ch-jur-06", "top-jur-06-02",
    "What crucial methodological rule did Roscoe Pound lay down when balancing competing interests?",
    ["Public interests must always extinguish individual interests", "Interests must always be compared on the same plane or level (preferably sub specie societatis as social interests)", "Individual property rights always override public welfare", "Judges should flip a coin to balance interests"],
    1,
    "Pound warned against comparing an individual interest against a social interest, which inevitably biases the result. Competing claims must be transferred to the same plane — evaluated as competing social interests.",
    {"A": "Totalitarian bias rejected by Pound.", "B": "Correct. Balancing must occur on the same plane (sub specie societatis).", "C": "Laissez-faire bias.", "D": "Arbitrary procedure."},
    "Medium", "Pound, Jurisprudence, Vol. III", "Explain Pound's rule on balancing on the same plane."
)

add_mcq(
    "mcq-jur-06-012", "ch-jur-06", "top-jur-06-02",
    "What are 'Jural Postulates' in Roscoe Pound's sociological jurisprudence?",
    ["Statutory sections passed by Parliament", "General assumptions and expectations of civilized society which law in that era seeks to guarantee and protect", "Judicial decrees delivered by appellate courts", "Religious dogmas in scripture"],
    1,
    "Pound's Jural Postulates are the reasonable generalized expectations of civilized society in a given time and place (e.g. expectation that others will commit no intentional aggression, that men will honor promises, etc.).",
    {"A": "Statutory codes.", "B": "Correct. General presuppositions and expectations of civilized society.", "C": "Judicial decrees.", "D": "Religious scripture."},
    "Medium", "Pound, Introduction to the Philosophy of Law (1922)", "Define Pound's Jural Postulates."
)

add_mcq(
    "mcq-jur-06-013", "ch-jur-06", "top-jur-06-02",
    "How many basic Jural Postulates of civilized society did Roscoe Pound initially formulate in 1919?",
    ["Three", "Five", "Eight", "Twelve"],
    1,
    "Pound initially formulated Five Jural Postulates: (1) Protection against intentional aggression, (2) Control over property one has created, (3) Good faith in promises/transactions, (4) Protection against negligent harm, and (5) Restraint of dangerous things.",
    {"A": "Three interests.", "B": "Correct. Five Jural Postulates.", "C": "Fuller's 8 desiderata.", "D": "Twelve tables."},
    "Medium", "Pound, Outlines of Lectures on Jurisprudence", "Recall the number of Pound's Jural Postulates."
)

add_mcq(
    "mcq-jur-06-014", "ch-jur-06", "top-jur-06-02",
    "Roscoe Pound strongly criticized what he termed 'Mechanical Jurisprudence'. What did he mean by that term?",
    ["The use of computers in court registry", "Rigid, blind deduction of conclusions from abstract legal concepts without considering practical social effects", "The law of automobile traffic accidents", "The use of machinery in industrial factories"],
    1,
    "In 'Mechanical Jurisprudence' (1908), Pound criticized judges who treat law as a closed mechanical game of abstract deduction, ignoring whether the ruling produces practical justice in living society.",
    {"A": "Court technology.", "B": "Correct. Rigid deduction from abstract concepts ignoring social consequences.", "C": "Motor vehicle law.", "D": "Industrial mechanization."},
    "Easy", "Roscoe Pound, Mechanical Jurisprudence (1908)", "Define Mechanical Jurisprudence."
)

add_mcq(
    "mcq-jur-06-015", "ch-jur-06", "top-jur-06-02",
    "In Indian constitutional jurisprudence, which part of the Constitution embodies Roscoe Pound's social engineering goals of balancing private rights with public welfare?",
    ["The Preamble and Directive Principles of State Policy (Part IV)", "Article 368 only", "Schedule VIII only", "The Union List in Schedule VII"],
    0,
    "The Preamble and the Directive Principles of State Policy (Part IV, Articles 36–51) represent the Indian constitutional blueprint for social engineering, aiming to create a welfare state.",
    {"A": "Correct. Preamble and Directive Principles embody social engineering.", "B": "Article 368 is amendment power.", "C": "Schedule VIII lists official languages.", "D": "Union List divides legislative subjects."},
    "Easy", "Kesavananda Bharati v. State of Kerala, (1973) 4 SCC 225", "Link Directive Principles to social engineering."
)

add_mcq(
    "mcq-jur-06-016", "ch-jur-06", "top-jur-06-02",
    "Which jurist famously critiqued Pound's metaphor of 'Social Engineering' by pointing out that human beings in society are living organisms, not dead mechanical parts like steel and bolts?",
    ["Julius Stone", "C.K. Allen", "Hans Kelsen", "Lon Fuller"],
    0,
    "Julius Stone criticized the engineering analogy as dangerously mechanical, observing that society consists of conscious, willful living beings, not inert building materials that can be mechanically shaped.",
    {"A": "Correct. Julius Stone criticized the engineering metaphor.", "B": "Allen analyzed custom and precedent.", "C": "Kelsen focused on pure norms.", "D": "Fuller focused on internal morality."},
    "Hard", "Julius Stone, Province and Function of Law", "Recall critique of Pound's engineering metaphor."
)

# -------------------------------------------------------------
# CHAPTER 7: REALIST SCHOOL OF JURISPRUDENCE
# -------------------------------------------------------------

# top-jur-07-01: American Realism
add_mcq(
    "mcq-jur-07-017", "ch-jur-07", "top-jur-07-01",
    "Who is revered as the spiritual godfather of American Legal Realism through his famous 1881 dictum 'The life of the law has not been logic; it has been experience'?",
    ["Jerome Frank", "Karl Llewellyn", "Oliver Wendell Holmes Jr.", "Benjamin Cardozo"],
    2,
    "Justice Oliver Wendell Holmes Jr. opened 'The Common Law' (1881) with his celebrated dictum: 'The life of the law has not been logic; it has been experience', laying the intellectual groundwork for American Realism.",
    {"A": "Frank founded Fact-Skepticism.", "B": "Llewellyn drafted Realist manifestos.", "C": "Correct. O.W. Holmes Jr. coined this celebrated opening dictum.", "D": "Cardozo analyzed the judicial process."},
    "Easy", "O.W. Holmes Jr., The Common Law (1881)", "Recall Holmes's famous opening sentence."
)

add_mcq(
    "mcq-jur-07-018", "ch-jur-07", "top-jur-07-01",
    "In 'The Path of the Law' (1897), how did Oliver Wendell Holmes Jr. define Law?",
    ["The command of the sovereign", "The prophecies of what the courts will do in fact, and nothing more pretentious", "The pure norm descending from Grundnorm", "The reflection of Volksgeist"],
    1,
    "Holmes famously defined law: 'The prophecies of what the courts will do in fact, and nothing more pretentious, are what I mean by the law.'",
    {"A": "Austin's command definition.", "B": "Correct. Prophecies of what courts will do in fact.", "C": "Kelsen's normative definition.", "D": "Savigny's historical definition."},
    "Easy", "Holmes, The Path of the Law (1897)", "Recall Holmes's prediction theory of law."
)

add_mcq(
    "mcq-jur-07-019", "ch-jur-07", "top-jur-07-01",
    "In 'Law and the Modern Mind' (1930), Jerome Frank categorized legal realists into two groups. What were they?",
    ["Rule-Skeptics and Fact-Skeptics", "Analytical Realists and Historical Realists", "Normative Realists and Positivist Realists", "Marxist Realists and Capitalist Realists"],
    0,
    "Jerome Frank divided Realists into: (1) Rule-Skeptics (like Karl Llewellyn, who doubt that formal paper rules determine appellate decisions), and (2) Fact-Skeptics (like Frank himself, who doubt that trial courts can ever ascertain objective facts due to witness bias, perjury, and human frailty).",
    {"A": "Correct. Rule-Skeptics and Fact-Skeptics.", "B": "School classifications.", "C": "Methodological terms.", "D": "Ideological terms."},
    "Medium", "Jerome Frank, Law and the Modern Mind (1930)", "Distinguish Rule-Skeptics from Fact-Skeptics."
)

add_mcq(
    "mcq-jur-07-020", "ch-jur-07", "top-jur-07-01",
    "What psychological concept did Jerome Frank use to explain the public's irrational craving for absolute certainty in law?",
    ["Oedipus Complex", "The Basic Legal Myth / Father-Complex", "Inferiority Complex", "Cognitive Dissonance"],
    1,
    "Frank utilized Freudian psychoanalysis, arguing that humanity's craving for an infallible, perfectly certain legal system is a childish 'Father-Complex' (The Basic Legal Myth) seeking an omnipotent father figure in judges and formal rules.",
    {"A": "Freudian sexual complex.", "B": "Correct. The Father-Complex and Basic Legal Myth.", "C": "Adlerian psychological complex.", "D": "Social psychology phenomenon."},
    "Hard", "Jerome Frank, Law and the Modern Mind", "Recall Frank's Father-Complex critique of legal certainty."
)

add_mcq(
    "mcq-jur-07-021", "ch-jur-07", "top-jur-07-01",
    "Which American Realist jurist, principal draftsman of the Uniform Commercial Code (UCC), formulated the concept of 'Law-Jobs'?",
    ["Karl Llewellyn", "Jerome Frank", "Felix Cohen", "William Douglas"],
    0,
    "Karl Llewellyn formulated the functional theory of 'Law-Jobs' in 'The Bramble Bush' (1930) and 'The Cheyenne Way', analyzing the universal tasks law performs to keep a group coordinated and survive.",
    {"A": "Correct. Karl Llewellyn propounded 'Law-Jobs'.", "B": "Frank was a fact-skeptic.", "C": "Felix Cohen analyzed functional jurisprudence.", "D": "Douglas was a Supreme Court judge."},
    "Medium", "Karl Llewellyn, The Bramble Bush (1930)", "Identify Llewellyn's Law-Jobs theory."
)

add_mcq(
    "mcq-jur-07-022", "ch-jur-07", "top-jur-07-01",
    "What distinction did Karl Llewellyn draw between 'Paper Rules' and 'Real Rules'?",
    ["Paper rules are written statutes; real rules are unwritten customs", "Paper rules are the accepted formal legal rules in books; real rules are what courts and officials actually do in practice", "Paper rules apply only to contracts; real rules apply to crimes", "Paper rules are draft bills before Parliament"],
    1,
    "Llewellyn distinguished between 'Paper Rules' (the formal doctrines found in law-books and judgments) and 'Real Rules' (the descriptive practices and actual behavior of judges, police, and officials in reality).",
    {"A": "Statute vs custom distinction.", "B": "Correct. Paper rules in books vs Real rules in actual practice.", "C": "Incorrect subject division.", "D": "Legislative procedure."},
    "Easy", "Llewellyn, A Realistic Jurisprudence (1930)", "Distinguish Paper Rules from Real Rules."
)

add_mcq(
    "mcq-jur-07-023", "ch-jur-07", "top-jur-07-01",
    "In 'The Nature of the Judicial Process' (1921), Justice Benjamin N. Cardozo analyzed how appellate judges actually decide cases. Which four methods did Cardozo identify?",
    ["Philosophy (Logic), History, Custom, and Sociology (Social Welfare)", "Command, Sanction, Duty, and Sovereign", "Text, Context, Preamble, and Schedule", "Grammar, Logic, Rhetoric, and Politics"],
    0,
    "Cardozo identified four directing forces in judicial decision-making: (1) The method of Philosophy (analogy/logic), (2) The method of History (evolution), (3) The method of Custom (tradition), and (4) The method of Sociology (justice, morals, and social welfare).",
    {"A": "Correct. Cardozo's four methods: Philosophy, History, Custom, Sociology.", "B": "Austin's imperative categories.", "C": "Statutory interpretation aids.", "D": "Medieval liberal arts."},
    "Medium", "Cardozo, The Nature of the Judicial Process (1921)", "Recall Cardozo's 4 methods of judicial process."
)

add_mcq(
    "mcq-jur-07-024", "ch-jur-07", "top-jur-07-01",
    "What is the famous caricature of Jerome Frank's fact-skepticism often referred to by critics as 'Gastronomical Jurisprudence'?",
    ["That judges should dine together to reach consensus", "The assertion that a judicial decision may depend on what the judge ate for breakfast", "The legal regulation of restaurant food safety", "That law is digested by lawyers like food"],
    1,
    "Critics mocked Frank's psychological fact-skepticism by calling it 'Gastronomical Jurisprudence' — the cynical notion that a judicial decision is determined by a judge's digestion or personal prejudices rather than legal rules.",
    {"A": "Judicial bench dining.", "B": "Correct. Gastronomical jurisprudence: Decisions depend on what judge had for breakfast.", "C": "Pure food laws.", "D": "Incorrect metaphor."},
    "Easy", "Jerome Frank, Courts on Trial (1949)", "Explain Gastronomical Jurisprudence."
)

# top-jur-07-02: Scandinavian Realism
add_mcq(
    "mcq-jur-07-025", "ch-jur-07", "top-jur-07-02",
    "How does Scandinavian Realism fundamentally differ from American Legal Realism?",
    ["American Realism focuses on the trial process and judicial behavior; Scandinavian Realism is a philosophical critique exposing legal concepts (rights, duties) as metaphysical illusions", "Scandinavian Realism believes in natural law", "Scandinavian Realism rejects psychology", "There is no difference between them"],
    0,
    "American Realists are empirically minded lawyers focused on courts and judges; Scandinavian Realists (the Uppsala School) are radical philosophical positivists who analyze legal concepts as psychological magic and metaphysical myths.",
    {"A": "Correct. American = court behavior; Scandinavian = philosophical attack on metaphysical illusions.", "B": "Scandinavians fiercely attacked natural law.", "C": "Scandinavians rely heavily on psychological explanations.", "D": "They belong to different traditions."},
    "Hard", "Olivecrona, Law as Fact", "Distinguish Scandinavian from American Realism."
)

add_mcq(
    "mcq-jur-07-026", "ch-jur-07", "top-jur-07-02",
    "Who is regarded as the spiritual founder of the Uppsala School of Scandinavian Realism with his battle cry 'Metaphysics must be destroyed' (Praeterea censeo metaphysicam esse delendam)?",
    ["Axel Hägerström", "Karl Olivecrona", "Alf Ross", "Vilhelm Lundstedt"],
    0,
    "Swedish philosopher Axel Hägerström (1868–1939) founded the Scandinavian Realist school, insisting that objective values, rights, and duties do not exist in the physical world and are emotional metaphysical delusions.",
    {"A": "Correct. Axel Hägerström founded the Uppsala School.", "B": "Olivecrona was Hägerström's student.", "C": "Ross was a Danish realist.", "D": "Lundstedt was a Swedish disciple."},
    "Medium", "Hägerström, Inquiries into the Nature of Law and Morals", "Identify Axel Hägerström."
)

add_mcq(
    "mcq-jur-07-027", "ch-jur-07", "top-jur-07-02",
    "In 'Law as Fact' (1939), how did Karl Olivecrona characterize legal rules?",
    ["Commands of a personal sovereign", "Independent Imperatives (non-personal commands addressed to the mind without a personal commander)", "Divine moral duties", "Statutory fictions"],
    1,
    "Olivecrona rejected Austin's personal command theory; statutes are not commands from one man to another, but 'Independent Imperatives' — impersonal linguistic formulas that exert psychological pressure on human minds.",
    {"A": "Austin's personal command model.", "B": "Correct. Olivecrona's Independent Imperatives.", "C": "Natural law view.", "D": "Maine's fictions."},
    "Medium", "Karl Olivecrona, Law as Fact (1939)", "Define Olivecrona's Independent Imperatives."
)

add_mcq(
    "mcq-jur-07-028", "ch-jur-07", "top-jur-07-02",
    "Which Danish Scandinavian Realist authored 'On Law and Justice' (1958) and used the fictional concept of 'Tû-Tû' to prove that legal rights have no semantic reference to reality?",
    ["Alf Ross", "Axel Hägerström", "Karl Olivecrona", "Vilhelm Lundstedt"],
    0,
    "Alf Ross compared legal terms like 'Ownership' and 'Right' to the meaningless magic word 'Tû-Tû' used by a primitive Polynesian tribe: it has no physical reality, but serves as a convenient technical shorthand linking facts to legal consequences.",
    {"A": "Correct. Alf Ross created the famous Tû-Tû illustration.", "B": "Hägerström founded the school.", "C": "Olivecrona authored Law as Fact.", "D": "Lundstedt rejected legal rights."},
    "Medium", "Alf Ross, Tû-Tû (1957) / On Law and Justice (1958)", "Identify Alf Ross and Tû-Tû."
)

add_mcq(
    "mcq-jur-07-029", "ch-jur-07", "top-jur-07-02",
    "According to Vilhelm Lundstedt, why should the concept of 'Justice' be expelled from legal science?",
    ["Because judges are corrupt", "Because 'Justice' is a purely emotional and subjective fantasy which cannot be verified scientifically, and law must be judged solely on social welfare", "Because justice belongs only to the military", "Because Parliament has banned the word justice"],
    1,
    "Lundstedt held that 'Justice' is an emotional delusion of the human mind without objective existence; legal science must replace talk of justice and natural rights with the objective study of social welfare.",
    {"A": "Lundstedt did not attack judicial integrity.", "B": "Correct. Justice is an unverifiable subjective emotional fantasy.", "C": "Incorrect proposition.", "D": "Incorrect proposition."},
    "Hard", "Lundstedt, Superstition or Rationality in Action for Peace", "Recall Lundstedt's critique of justice."
)

add_mcq(
    "mcq-jur-07-030", "ch-jur-07", "top-jur-07-02",
    "How do Scandinavian Realists explain the historical psychological origin of the binding force of law?",
    ["From the physical fear of God", "From ancient magical rituals, solemn oaths, and verbal formulas that conditioned human minds into automatic feelings of obligation", "From modern democratic voting", "From written contracts signed by ancestors"],
    1,
    "Hägerström and Olivecrona traced the binding power of law back to ancient Roman magical incantations, religious rites, and verbal oaths (e.g. mancipatio), which created deep-seated psychological conditioning in human brains.",
    {"A": "Theological explanation.", "B": "Correct. Origin in ancient magical formulas and psychological conditioning.", "C": "Democratic theory.", "D": "Locke's social contract."},
    "Medium", "Olivecrona, Law as Fact", "Explain Scandinavian Realist view of legal magic."
)

add_mcq(
    "mcq-jur-07-031", "ch-jur-07", "top-jur-07-02",
    "In Alf Ross's jurisprudence, how is a valid legal rule verified scientifically?",
    ["By measuring its moral goodness", "By observing whether the rule is actually applied by judges in courts because they feel an internal psychological obligation to obey it", "By checking whether it matches natural law", "By asking the Prime Minister"],
    1,
    "Alf Ross synthesized realism and positivism: a rule of law is valid if it can serve as a scheme of interpretation for a coherent system of actions, verified by the fact that judges actually follow it because they feel emotionally/normatively bound by it.",
    {"A": "Natural law test.", "B": "Correct. Verifiable by judicial adherence motivated by internal normative feeling.", "C": "Natural law.", "D": "Political executive."},
    "Hard", "Alf Ross, On Law and Justice", "Explain Ross's verification of valid law."
)

add_mcq(
    "mcq-jur-07-032", "ch-jur-07", "top-jur-07-02",
    "What common foundational belief unites both American and Scandinavian Realists?",
    ["Both believe natural law is the supreme law", "Both reject mechanical conceptual formalism and demand that law be studied as an empirical, practical human phenomenon", "Both believe statutes should be abolished", "Both believe judges should rule by intuition alone"],
    1,
    "Both realist schools share a relentless hostility towards mechanical jurisprudence and abstract conceptualism, demanding that legal rules be analyzed in their actual operation and psychological reality.",
    {"A": "Both are fiercely anti-natural law.", "B": "Correct. Rejection of mechanical conceptualism in favor of empirical reality.", "C": "Neither seeks abolition of statutes.", "D": "Neither promotes arbitrary rule."},
    "Easy", "Dias on Jurisprudence", "Identify common denominator of legal realism."
)
