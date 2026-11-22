import json
from concept_helpers import create_concept_file

# Load current data from assets/learning/data/jurisprudence/jurisprudence-concepts-part1.js
with open('assets/learning/data/jurisprudence/jurisprudence-concepts-part1.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract json inside const DATA = ...;
idx = text.find('const DATA = ') + len('const DATA = ')
end_idx = text.rfind(';\n\n  global.')
data = json.loads(text[idx:end_idx])

# -------------------------------------------------------------
# CHAPTER 3: NATURAL LAW SCHOOL
# -------------------------------------------------------------
data["top-jur-03-01"] = {
    "topicId": "top-jur-03-01",
    "chapterId": "ch-jur-03",
    "subjectId": "law-jurisprudence",
    "title": "Classical & Medieval Natural Law (Aquinas & Stoics)",
    "subtitle": "Jus Naturale, Eternal Law, and the Maxim 'Lex Injusta Non Est Lex'",
    "juristRef": "Heraclitus, Socrates, Aristotle, Cicero, St. Thomas Aquinas",
    "learningObjective": "Trace the Greek, Roman, and Christian origins of natural law, master Aquinas's four-fold classification of laws, and evaluate the maxim that an unjust law is not law.",
    "introduction": "Natural Law (Jus Naturale) is the philosophy that there exists an objective, universal, immutable moral order derived from nature, human reason, or divine will. Positive human enactments derive their moral validity from conformity with this higher transcendent law.",
    "detailedExplanation": """
<h3>1. Greek Philosophy & Stoic Cosmopolitanism</h3>
<ul>
  <li><strong>Heraclitus &amp; Socrates:</strong> Discovered the notion of a cosmic order governed by universal reason (Logos). Socrates argued that virtue is knowledge and that an appeal can be made to human insight beyond human decrees.</li>
  <li><strong>Aristotle:</strong> Distinguished between <em>Natural Justice</em> (which everywhere has the same force and does not exist by people's thinking this or that) and <em>Conventional Justice</em> (matters indifferent until determined by law).</li>
  <li><strong>The Stoics:</strong> Founded by Zeno, the Stoics held that the universe is governed by Reason (Logos). Human beings, possessing a spark of divine reason, are members of a universal world community (Cosmopolis).</li>
</ul>

<h3>2. Roman Law & Cicero</h3>
<p>Cicero in <em>De Re Publica</em> articulated the classic pagan formulation of natural law: <em>'True law is right reason in agreement with nature; it is of universal application, unchanging and everlasting... It is a sin to try to alter this law, nor is it allowable to attempt to repeal any part of it, and it is impossible to abolish it entirely... God is the author of this law.'</em> Roman jurists divided law into: (a) <strong>Jus Civile</strong> (law applicable to Roman citizens), (b) <strong>Jus Gentium</strong> (law common to all civilized nations), and (c) <strong>Jus Naturale</strong> (natural law discovered by human reason).</p>

<h3>3. St. Thomas Aquinas & Medieval Scholasticism</h3>
<p>In <em>Summa Theologiae</em> (Treatise on Law), Aquinas integrated Aristotelian philosophy with Catholic Christian theology, formulating his celebrated four-fold taxonomy of law:</p>
<ol>
  <li><strong>Lex Aeterna (Eternal Law):</strong> Divine reason directing the entire cosmos, known fully only to God.</li>
  <li><strong>Lex Divina (Divine Law):</strong> God's revelation through sacred scriptures (Bible, Ten Commandments).</li>
  <li><strong>Lex Naturalis (Natural Law):</strong> The participation of rational creatures in the Eternal Law, discovered through natural human reason (e.g. good is to be done, evil avoided).</li>
  <li><strong>Lex Humana (Human / Positive Law):</strong> Particular statutory determinations made by human sovereigns for the common good. If human law contradicts natural law, it is not law but a corruption of law (<em>Lex injusta non est lex</em>).</li>
</ol>
""",
    "quickRevisionPoints": [
      "Natural Law is universal, eternal, immutable, and discovered through human reason.",
      "Aristotle bifurcated justice into Natural Justice (universal) and Conventional Justice (statutory).",
      "Cicero: 'True law is right reason in agreement with nature; unchanging and everlasting.'",
      "Aquinas's Four Laws: Lex Aeterna (Eternal), Lex Divina (Divine), Lex Naturalis (Natural), Lex Humana (Human).",
      "Foundational Maxim: 'Lex injusta non est lex' — an unjust law is not law."
    ],
    "provisions": [
      {
        "provision": "Lex Injusta Non Est Lex",
        "title": "Substantive Invalidation",
        "description": "An unjust law lacking moral reason does not bind conscience and loses legal authenticity."
      }
    ],
    "definitions": [
      {
        "term": "Natural Law",
        "definition": "A system of universal, immutable principles of justice and human rights discoverable by natural human reason independent of state enactment."
      }
    ],
    "ingredients": [
      "Universality: valid across all geographical boundaries and historical eras.",
      "Immutability: cannot be amended or abolished by human parliaments.",
      "Rational discovery: derived through human intellect and moral reflection."
    ],
    "exceptions": [
      "Aquinas conceded that an unjust human law may occasionally be obeyed to prevent public scandal, chaos, or violent rebellion."
    ],
    "examples": [
      {
        "scenario": "A totalitarian dictator decrees that all infants of a minority group must be exterminated.",
        "application": "Under Aquinas and Cicero, this decree lacks the essential quality of law (Lex Humana) because it flagrantly violates Lex Naturalis; it represents raw tyranny without moral obligation."
      }
    ],
    "landmarkCases": [
      {
        "case": "Maneka Gandhi v. Union of India",
        "citation": "(1978) 1 SCC 248",
        "year": "1978",
        "bench": "7-Judge Constitution Bench (Beg CJ, Chandrachud, Bhagwati, Krishnaiyer, Untwalia, Murtaza Fazal Ali, Kailasam JJ)",
        "ratio": "The Supreme Court read natural law principles of 'just, fair and reasonable' procedure into Article 21, holding that statutory procedure established by law must conform to natural justice and fair play.",
        "impact": "Decisive resurgence of substantive natural law in Indian constitutional jurisprudence, overruling A.K. Gopalan."
      }
    ],
    "comparisonTables": [
      {
        "title": "Aquinas's Four-Fold Classification of Law",
        "headers": ["Classification", "Source", "Mode of Discovery", "Operational Scope"],
        "rows": [
          ["Lex Aeterna (Eternal Law)", "Divine Wisdom of God", "Inaccessible fully to mortal mind", "Governs the whole universe"],
          ["Lex Divina (Divine Law)", "Scriptural Revelation", "Read in Holy Scriptures", "Directs soul towards salvation"],
          ["Lex Naturalis (Natural Law)", "Human Reason participating in Divine Reason", "Natural intellect ('Do good, avoid evil')", "Guides moral human choices"],
          ["Lex Humana (Human Law)", "Sovereign State Legislature", "Enactment and promulgation", "Regulates civic social order"]
        ]
      }
    ],
    "diagramId": "diag-jur-schools-comparison",
    "diagramExplanation": "Diagram shows the moral hierarchy descending from Eternal Law to Human Positive Law.",
    "misconceptions": [
      {
        "myth": "Natural law requires belief in a Christian or religious God.",
        "reality": "Secular natural law (Hugo Grotius) established that natural law would exist even if God did not exist ('Etiamsi daremus non esse Deum')."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Attributing 'Lex injusta non est lex' exclusively to John Austin.",
        "reality": "Austin fiercely rejected this maxim. The maxim originates in St. Augustine and St. Thomas Aquinas.",
        "rule": "Lex injusta non est lex = Augustine / Aquinas (Natural Law)."
      }
    ],
    "flashcards": [
      {
        "id": "fc-jur-03-01",
        "front": "Who formulated the four-fold classification: Lex Aeterna, Lex Divina, Lex Naturalis, and Lex Humana?",
        "back": "St. Thomas Aquinas (Summa Theologiae).",
        "category": "Medieval Natural Law"
      },
      {
        "id": "fc-jur-03-02",
        "front": "What does the Latin phrase 'Lex injusta non est lex' mean?",
        "back": "An unjust law is not a law.",
        "category": "Natural Law Maxims"
      },
      {
        "id": "fc-jur-03-03",
        "front": "How did Aristotle classify justice in the Nicomachean Ethics?",
        "back": "Natural Justice (universal force) and Conventional Justice (statutory/positive law).",
        "category": "Greek Jurisprudence"
      },
      {
        "id": "fc-jur-03-04",
        "front": "Which Roman orator famously defined true law as 'right reason in agreement with nature'?",
        "back": "Marcus Tullius Cicero.",
        "category": "Roman Natural Law"
      }
    ],
    "sourceReferences": [
      {"title": "Summa Theologiae — St. Thomas Aquinas (Treatise on Law)", "url": "https://www.newadvent.org"},
      {"title": "De Re Publica — Cicero", "url": "https://www.thelatinlibrary.com"}
    ]
}

data["top-jur-03-02"] = {
    "topicId": "top-jur-03-02",
    "chapterId": "ch-jur-03",
    "subjectId": "law-jurisprudence",
    "title": "Social Contract Theory (Hobbes, Locke & Rousseau)",
    "subtitle": "State of Nature, Inalienable Rights, and General Will",
    "juristRef": "Thomas Hobbes, John Locke, Jean-Jacques Rousseau, Hugo Grotius",
    "learningObjective": "Compare the social contract paradigms of Hobbes, Locke, and Rousseau, evaluating their concepts of human nature, sovereign power, and inalienable rights.",
    "introduction": "The Social Contract Theory secularized natural law during the Enlightenment. It posited that political authority and positive legal obligations are derived from a hypothetical mutual covenant entered into by free individuals living in a pre-political 'State of Nature'.",
    "detailedExplanation": """
<h3>1. Thomas Hobbes (1588–1679): The Absolutist Sovereign</h3>
<p>In <em>Leviathan (1651)</em>, Hobbes described the State of Nature as a condition of war of all against all (<em>Bellum omnium contra omnes</em>), where human life was <em>'solitary, poor, nasty, brutish, and short'</em>. Driven by fear of violent death, men entered a social contract surrendering all their natural liberties to an absolute sovereign (the Leviathan). The sovereign was not a party to the contract, so his commands were absolute, unconditional, and irrevocable, subject only to the subject's right of self-preservation.</p>

<h3>2. John Locke (1632–1704): Limited Government & Inalienable Rights</h3>
<p>In <em>Two Treatises of Government (1689)</em>, Locke painted the State of Nature as a state of peace, goodwill, and mutual preservation governed by Reason. However, it lacked three conveniences: (a) an established, settled law, (b) a known, indifferent judge, and (c) an execution power to enforce decisions. Individuals formed a contract surrendering only their executive power to protect their inalienable natural rights to <strong>Life, Liberty, and Property (Estate)</strong>. The government holds power as a fiduciary trust; if the sovereign breaches the trust, citizens possess the right to revolt.</p>

<h3>3. Jean-Jacques Rousseau (1712–1778): Popular Sovereignty & General Will</h3>
<p>In <em>The Social Contract (1762)</em>, Rousseau proclaimed: <em>'Man is born free, and everywhere he is in chains.'</em> In his State of Nature, man was a 'noble savage' living innocent and happy, until private property introduced inequality and strife. Through the social contract, each citizen completely alienates his person and powers to the community, creating the <strong>'General Will' (Volonté Générale)</strong>. Sovereignty belongs to the community as a whole (Popular Sovereignty), and whoever refuses to obey the general will shall be 'forced to be free'.</p>
""",
    "quickRevisionPoints": [
      "Hobbes (Leviathan): State of Nature is brutish, war of all against all; creates Absolute Sovereign.",
      "Locke (Two Treatises): State of Nature is peaceful; contract preserves inalienable rights to Life, Liberty, and Property.",
      "Locke's fiduciary trust: Government can be overthrown if it violates natural rights.",
      "Rousseau (Social Contract): 'Man is born free, but everywhere in chains'; creates the General Will.",
      "Grotius: Father of modern international law; secularized natural law."
    ],
    "provisions": [
      {
        "provision": "Lockean Inalienable Rights",
        "title": "Natural Rights Triad",
        "description": "Life, Liberty, and Property — the bedrock of modern constitutional bills of rights."
      }
    ],
    "definitions": [
      {
        "term": "General Will (Rousseau)",
        "definition": "The collective sovereign will of the political body aiming constantly at the common public good."
      }
    ],
    "ingredients": [
      "State of nature: condition of humanity prior to political society.",
      "Pact: agreement by individuals to form civil society and establish government.",
      "Sovereignty allocation: absolute (Hobbes), limited fiduciary (Locke), or popular direct (Rousseau)."
    ],
    "exceptions": [
      "Hobbes recognized one inalienable exception: a subject can resist the sovereign if commanded to kill himself or cannot be protected from death."
    ],
    "examples": [
      {
        "scenario": "A parliament enacts a law expropriating all private homes without compensation or hearing.",
        "application": "Under Locke's philosophy, this constitutes a tyrannical breach of the fiduciary trust to preserve property, morally legitimizing civil disobedience and judicial nullification."
      }
    ],
    "landmarkCases": [
      {
        "case": "K.S. Puttaswamy v. Union of India",
        "citation": "(2017) 10 SCC 1",
        "year": "2017",
        "bench": "9-Judge Constitution Bench",
        "ratio": "The Supreme Court recognized privacy as an inalienable natural right inherent to human dignity, rejecting the positivist argument that human rights are mere statutory bounties conferred by the state, explicitly invoking Lockean natural rights theory.",
        "impact": "Monumental affirmation of inalienable natural rights under Part III of the Constitution."
      }
    ],
    "comparisonTables": [
      {
        "title": "Comparative Matrix of Social Contract Theorists",
        "headers": ["Philosopher", "State of Nature", "Character of Contract", "Sovereign Power"],
        "rows": [
          ["Thomas Hobbes", "War of all against all; brutish, short", "Surrender of all rights for security", "Absolute & Indivisible (Leviathan)"],
          ["John Locke", "State of peace; inconvenient enforcement", "Surrender only of executive judicial power", "Limited Fiduciary Trust (Life, Liberty, Property)"],
          ["J.J. Rousseau", "Noble savage corrupted by property", "Total surrender to collective community", "Popular Sovereignty & The General Will"]
        ]
      }
    ],
    "diagramId": "diag-jur-schools-comparison",
    "diagramExplanation": "Comparative architecture of the transition from the State of Nature to Civil Society across Hobbes, Locke, and Rousseau.",
    "misconceptions": [
      {
        "myth": "Hobbes, Locke, and Rousseau believed the Social Contract was a real historical event that occurred on a specific date.",
        "reality": "All three utilized the Social Contract as a philosophical, heuristic device to deduce the moral legitimacy and limits of state authority."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing Hobbes advocated the separation of powers.",
        "reality": "Hobbes vehemently opposed separation of powers, demanding indivisible absolute sovereignty. Locke and Montesquieu advocated separation of powers.",
        "rule": "Indivisible absolute power = Hobbes; Fiduciary separation of powers = Locke."
      }
    ],
    "flashcards": [
      {
        "id": "fc-jur-03-05",
        "front": "Who described the state of nature as 'solitary, poor, nasty, brutish, and short'?",
        "back": "Thomas Hobbes in 'Leviathan' (1651).",
        "category": "Social Contract"
      },
      {
        "id": "fc-jur-03-06",
        "front": "Which three inalienable natural rights were identified by John Locke?",
        "back": "Life, Liberty, and Property (Estate).",
        "category": "Lockean Theory"
      },
      {
        "id": "fc-jur-03-07",
        "front": "Who coined the concept of the 'General Will' (Volonté Générale)?",
        "back": "Jean-Jacques Rousseau in 'The Social Contract' (1762).",
        "category": "Popular Sovereignty"
      },
      {
        "id": "fc-jur-03-08",
        "front": "Who is revered as the 'Father of Modern International Law' for secularizing natural law?",
        "back": "Hugo Grotius (De Jure Belli Ac Pacis, 1625).",
        "category": "Natural Law Jurists"
      }
    ],
    "sourceReferences": [
      {"title": "Leviathan — Thomas Hobbes (Cambridge Texts in History of Political Thought)", "url": "https://www.cambridge.org"},
      {"title": "Two Treatises of Government — John Locke", "url": "https://www.yorku.ca"}
    ]
}

data["top-jur-03-03"] = {
    "topicId": "top-jur-03-03",
    "chapterId": "ch-jur-03",
    "subjectId": "law-jurisprudence",
    "title": "Revival of Natural Law in the 20th Century (Fuller, Stammler & Finnis)",
    "subtitle": "Natural Law with Variable Content, Procedural Morality, and Basic Human Goods",
    "juristRef": "Rudolf Stammler, Giorgio Del Vecchio, Lon L. Fuller, John Finnis, Gustav Radbruch",
    "learningObjective": "Master the 20th-century resurgence of natural law following totalitarianism, analyzing Stammler's variable content, Fuller's inner procedural morality, and Finnis's 7 basic human goods.",
    "introduction": "The 19th century witnessed the decline of classical natural law under the assault of analytical positivism and historical empiricism. However, the horrors of Nazi Germany and fascist totalitarianism in WWII proved that raw statutory legality divorced from morality leads to barbarism, sparking a dramatic revival of natural law.",
    "detailedExplanation": """
<h3>1. Rudolf Stammler: 'Natural Law with a Variable Content'</h3>
<p>Stammler rejected immutable metaphysical dogmas. He introduced the celebrated concept of <strong>'Natural Law with a Variable Content'</strong> (<em>Naturrecht mit wechselndem Inhalte</em>). The fundamental ideal of justice remains constant (formal principle), but its substantive application changes and adapts to varying social, historical, and economic realities of time and place. Stammler formulated four 'Principles of Just Law' based on mutual respect and participation.</p>

<h3>2. Gustav Radbruch's Formula (1946)</h3>
<p>A former German positivist who renounced positivism after WWII, Radbruch formulated his famous <strong>Radbruch Formula</strong>: Where statutory law conflicts with justice in an intolerable degree (<em>unerträglich</em>), or where equality (the core of justice) is deliberately denied, the statute lacks the nature of law and must yield to justice. Extreme injustice is no law (<em>Gesetzliches Unrecht und übergesetzliches Recht</em>).</p>

<h3>3. Lon L. Fuller: The Internal Morality of Law</h3>
<p>In <em>The Morality of Law (1964)</em>, Lon Fuller presented a secular, procedural natural law theory. He identified 8 procedural desiderata that make legal ordering possible (the allegory of King Rex). A system that systematically fails in these 8 canons is not a defective legal system — it is not a legal system at all.</p>

<h3>4. John Finnis: Restatement of Natural Law (1980)</h3>
<p>In <em>Natural Law and Natural Rights</em>, John Finnis offered a modern analytical defense of natural law based on <strong>Seven Basic Human Goods</strong> that are self-evidently valuable for human flourishing: (1) Life, (2) Knowledge, (3) Play, (4) Aesthetic Experience, (5) Sociability / Friendship, (6) Practical Reasonableness, and (7) Religion (harmony with cosmic order). These goods are incommensurable and intrinsic.</p>
""",
    "quickRevisionPoints": [
      "20th-century revival was triggered by the legal atrocities of Nazi totalitarianism.",
      "Stammler: 'Natural Law with a Variable Content' — immutable ideal, changing substance.",
      "Radbruch Formula: Extreme injustice is not law; intolerable contradiction destroys statute.",
      "Fuller's 8 Desiderata: Procedural natural law based on the craft of lawmaking.",
      "John Finnis: 7 Basic Human Goods (Life, Knowledge, Play, Aesthetics, Friendship, Practical Reason, Religion)."
    ],
    "provisions": [
      {
        "provision": "Radbruch Formula",
        "title": "Extreme Injustice Rule",
        "description": "Flawed statutes lose legal validity when the contradiction with justice becomes unbearable."
      }
    ],
    "definitions": [
      {
        "term": "Natural Law with Variable Content",
        "definition": "Stammler's concept that while the ideal of justice is universal, its practical content varies with time, place, and culture."
      }
    ],
    "ingredients": [
      "Rejection of Austinian sovereign command without moral limits.",
      "Integration of procedural fairness with substantive justice.",
      "Recognition of foundational human rights that constrain state legislatures."
    ],
    "exceptions": [
      "Modern natural law does not claim to deduce every fine municipal regulation (like speed limits) from universal reason."
    ],
    "examples": [
      {
        "scenario": "A Nazi statute stripped German Jews of citizenship and authorized seizure of their property without cause.",
        "application": "Under the Radbruch Formula, this law is nullified as 'extreme statutory injustice' possessing zero legal validity."
      }
    ],
    "landmarkCases": [
      {
        "case": "A.K. Roy v. Union of India",
        "citation": "(1982) 1 SCC 271",
        "year": "1982",
        "bench": "5-Judge Constitution Bench (Chandrachud CJ, Bhagwati, Gupta, Tulzapurkar, A.N. Sen JJ)",
        "ratio": "The Supreme Court recognized that preventive detention laws must pass the test of procedural fairness, clarity, and non-arbitrariness, adopting modern procedural natural law principles.",
        "impact": "Incorporated Fullerian procedural canons into Indian administrative and preventive detention review."
      }
    ],
    "comparisonTables": [
      {
        "title": "Modern Natural Law Thinkers Comparison",
        "headers": ["Jurist", "Seminal Concept", "Core Philosophical Contribution"],
        "rows": [
          ["Rudolf Stammler", "Natural Law with a Variable Content", "Formal ideal of justice applied to changing historical conditions"],
          ["Gustav Radbruch", "Radbruch Formula", "Extreme statutory injustice loses the character of law"],
          ["Lon L. Fuller", "Inner Morality of Law", "8 procedural requirements essential for a genuine legal system"],
          ["John Finnis", "7 Basic Human Goods", "Self-evident values foundational for rational human flourishing"]
        ]
      }
    ],
    "diagramId": "diag-jur-schools-comparison",
    "diagramExplanation": "Timeline showing the collapse of 19th century positivism and the rise of 20th century neo-naturalism.",
    "misconceptions": [
      {
        "myth": "John Finnis claims that human goods are derived from biological evolution.",
        "reality": "Finnis insists that the 7 basic goods are self-evident (per se nota) to practical reason, not deduced from empirical biology."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing Stammler was an analytical positivist.",
        "reality": "Stammler was a neo-Kantian Natural Law philosopher who coined 'Natural Law with a Variable Content'.",
        "rule": "Stammler = Natural Law with Variable Content."
      }
    ],
    "flashcards": [
      {
        "id": "fc-jur-03-09",
        "front": "Who originated the concept of 'Natural Law with a Variable Content'?",
        "back": "Rudolf Stammler.",
        "category": "Neo-Kantian Jurisprudence"
      },
      {
        "id": "fc-jur-03-10",
        "front": "What does the Radbruch Formula dictate regarding unjust laws?",
        "back": "An intensely unjust statute loses its legal character and must yield to justice ('Extreme injustice is no law').",
        "category": "Radbruch's Philosophy"
      },
      {
        "id": "fc-jur-03-11",
        "front": "How many 'Basic Human Goods' are identified by John Finnis?",
        "back": "Seven (Life, Knowledge, Play, Aesthetic Experience, Sociability/Friendship, Practical Reasonableness, Religion).",
        "category": "Finnis Natural Law"
      },
      {
        "id": "fc-jur-03-12",
        "front": "In which book did Lon Fuller present the allegory of the inept King Rex?",
        "back": "The Morality of Law (1964).",
        "category": "Procedural Natural Law"
      }
    ],
    "sourceReferences": [
      {"title": "Natural Law and Natural Rights — John Finnis", "url": "https://global.oup.com"},
      {"title": "The Theory of Justice — Rudolf Stammler", "url": "https://archive.org"}
    ]
}

# -------------------------------------------------------------
# CHAPTER 4: ANALYTICAL & POSITIVIST SCHOOL
# -------------------------------------------------------------
data["top-jur-04-01"] = {
    "topicId": "top-jur-04-01",
    "chapterId": "ch-jur-04",
    "subjectId": "law-jurisprudence",
    "title": "Jeremy Bentham: Utilitarianism & Censorial Jurisprudence",
    "subtitle": "The Father of Positivism, Felicific Calculus, and Codification",
    "juristRef": "Jeremy Bentham",
    "learningObjective": "Master Bentham's Utilitarian principle, Felicific calculus, distinction between Expository and Censorial jurisprudence, and his pioneering theory of legislation.",
    "introduction": "Jeremy Bentham (1748–1832) is the true founder of modern analytical legal positivism. Though John Austin popularized the school, Bentham authored the foundational texts, establishing that law must be analyzed empirically as a sovereign mandate separated from moral speculation.",
    "detailedExplanation": """
<h3>1. Utilitarianism: The Greatest Happiness Principle</h3>
<p>Bentham opened his masterpiece, <em>An Introduction to the Principles of Morals and Legislation (1789)</em>, with his famous declaration: <em>'Nature has placed mankind under the governance of two sovereign masters, pain and pleasure. It is for them alone to point out what we ought to do, as well as to determine what we shall do.'</em> The standard of right and wrong is the <strong>Principle of Utility</strong> — that which approves or disapproves of every action according to its tendency to augment or diminish the happiness of the party whose interest is in question. For the legislator, the goal is <strong>'the greatest happiness of the greatest number'</strong>.</p>

<h3>2. The Felicific / Hedonistic Calculus</h3>
<p>Bentham proposed that pain and pleasure could be scientifically measured using seven dimensions: (1) Intensity, (2) Duration, (3) Certainty or uncertainty, (4) Propinquity or remoteness, (5) Fecundity (chance of being followed by sensations of same kind), (6) Purity (chance of not being followed by sensations of opposite kind), and (7) Extent (number of persons affected).</p>

<h3>3. Expository vs Censorial Jurisprudence</h3>
<p>Bentham established the vital epistemological demarcation:</p>
<ul>
  <li><strong>Expository Jurisprudence (Law as it is):</strong> Explains what the law actually is in a given society. Deals with positive facts.</li>
  <li><strong>Censorial Jurisprudence (Law as it ought to be):</strong> Articulates what the law ought to be using utility as the critical measuring rod; also called the <strong>Science of Legislation</strong>.</li>
</ul>

<h3>4. Critique of Judge-Made Law & Common Law</h3>
<p>Bentham was a ferocious critic of the English common law and Sir William Blackstone. He condemned common law as <em>'Judge-made law'</em> and <em>'Dog-law'</em>: just as a man trains his dog by waiting until it does something wrong and then beating it, so judges wait until a citizen acts, and then retrospectively declare his act unlawful. To cure this, Bentham demanded comprehensive, universal statutory <strong>Codification</strong>.</p>
""",
    "quickRevisionPoints": [
      "Jeremy Bentham: True founder of Analytical Positivism (earlier than Austin).",
      "Two sovereign masters: Pain and Pleasure.",
      "Principle of Utility: 'The greatest happiness of the greatest number'.",
      "Felicific Calculus measures pleasure across 7 dimensions (Intensity, Duration, Extent, etc.).",
      "Expository Jurisprudence (Law as it is) vs Censorial Jurisprudence (Law as it ought to be).",
      "Attacked common law as retrospective 'dog-law'; demanded universal codification."
    ],
    "provisions": [
      {
        "provision": "Principle of Utility",
        "title": "Greatest Happiness Principle",
        "description": "Legislation must maximize net societal pleasure and minimize net collective pain."
      }
    ],
    "definitions": [
      {
        "term": "Expository Jurisprudence",
        "definition": "The branch of legal study that ascertains and expounds what the positive law actually is."
      },
      {
        "term": "Censorial Jurisprudence",
        "definition": "The critical art and science of evaluating and reforming law based on the principle of utility (law as it ought to be)."
      }
    ],
    "ingredients": [
      "Empirical legal analysis stripped of theological or natural law dogmas.",
      "Sovereign power as the source of enforceable positive commands.",
      "Hedonistic metric: utility as the exclusive measure of legislative reform."
    ],
    "exceptions": [
      "Bentham rejected inalienable natural rights, famously dismissing the French Declaration of the Rights of Man as 'nonsense upon stilts'."
    ],
    "examples": [
      {
        "scenario": "A parliament considers legalizing medical euthanasia for terminally ill patients in intractable pain.",
        "application": "Applying Bentham's felicific calculus, if prolonging life causes immense net pain and zero pleasure to patient and family, utility approves the reform."
      }
    ],
    "landmarkCases": [
      {
        "case": "State of Tamil Nadu v. K. Balu",
        "citation": "(2017) 2 SCC 281",
        "year": "2017",
        "bench": "Supreme Court of India (T.S. Thakur CJ, Chandrachud, Rao JJ)",
        "ratio": "The Supreme Court applied utilitarian principles of public health and safety to prohibit liquor vends within 500 meters of national and state highways, balancing individual commercial freedoms against the greater public happiness and reduction of road accident fatalities.",
        "impact": "Classic judicial application of utilitarian public welfare calculus in Indian road safety regulation."
      }
    ],
    "comparisonTables": [
      {
        "title": "Expository vs Censorial Jurisprudence",
        "headers": ["Dimension", "Expository Jurisprudence", "Censorial Jurisprudence"],
        "rows": [
          ["Core Subject", "Law as it IS (De Lege Lata)", "Law as it OUGHT to be (De Lege Ferenda)"],
          ["Primary Actor", "The Expositor (Lawyer / Judge)", "The Censor (Legislator / Reformer)"],
          ["Guiding Metric", "Statutory validity and state sanction", "Principle of Utility (Greatest Happiness)"],
          ["Nature of Discipline", "Descriptive science of positive rules", "Normative science of legislation"]
        ]
      }
    ],
    "diagramId": "diag-jur-jurists-theories",
    "diagramExplanation": "Diagram shows Bentham's bifurcation of jurisprudence into Expository and Censorial branches.",
    "misconceptions": [
      {
        "myth": "John Austin wrote his works before Jeremy Bentham.",
        "reality": "Bentham was Austin's mentor. Bentham's work 'Of Laws in General' was completed in 1782, but remained unpublished in full until 1945."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing Bentham defended natural rights.",
        "reality": "Bentham called natural rights 'simple nonsense: natural and imprescriptible rights, rhetorical nonsense, nonsense upon stilts'.",
        "rule": "Natural Rights = 'Nonsense upon stilts' (Bentham)."
      }
    ],
    "flashcards": [
      {
        "id": "fc-jur-04-01",
        "front": "Who declared that natural rights are 'nonsense upon stilts'?",
        "back": "Jeremy Bentham.",
        "category": "Utilitarianism"
      },
      {
        "id": "fc-jur-04-02",
        "front": "What are the two sovereign masters identified by Bentham?",
        "back": "Pain and Pleasure.",
        "category": "Bentham's Axioms"
      },
      {
        "id": "fc-jur-04-03",
        "front": "How did Bentham divide the science of jurisprudence?",
        "back": "Expository Jurisprudence (law as it is) and Censorial Jurisprudence (law as it ought to be).",
        "category": "Bentham's Taxonomy"
      },
      {
        "id": "fc-jur-04-04",
        "front": "What derogatory term did Bentham use to describe common law / judge-made law?",
        "back": "'Dog-law'.",
        "category": "Critique of Common Law"
      }
    ],
    "sourceReferences": [
      {"title": "An Introduction to the Principles of Morals and Legislation — Jeremy Bentham", "url": "https://www.earlymoderntexts.com"},
      {"title": "Of Laws in General — Jeremy Bentham (Ed. H.L.A. Hart)", "url": "https://global.oup.com"}
    ]
}

data["top-jur-04-02"] = {
    "topicId": "top-jur-04-02",
    "chapterId": "ch-jur-04",
    "subjectId": "law-jurisprudence",
    "title": "John Austin & the Command Theory of Sovereign Law",
    "subtitle": "Imperative Theory, Sanction, Habitual Obedience, and the Triad of Command",
    "juristRef": "John Austin",
    "learningObjective": "Critically analyze John Austin's Imperative Theory of Law (Command, Sovereign, Sanction, Duty), evaluate the core criticisms leveled by Maine, Bryce, and Hart, and assess its contemporary relevance.",
    "introduction": "John Austin (1790–1859), holder of the first Chair of Jurisprudence at University College London, gave analytical jurisprudence its rigorous form. In 'The Province of Jurisprudence Determined' (1832), Austin sought to demarcate the exact boundary of law properly so-called from other social rules.",
    "detailedExplanation": """
<h3>1. The Triad of Law: Command, Duty, Sanction</h3>
<p>Austin defined positive law with mathematical economy: <strong>'Law is the command of a sovereign, backed by the threat of sanction, imposing a duty of obedience upon subjects.'</strong> Law contains four interconnected elements:</p>
<ul>
  <li><strong>Command:</strong> An intimation or expression of a wish by a superior to an inferior, accompanied by the intention and physical power to inflict an evil (sanction) in case of non-compliance.</li>
  <li><strong>Duty:</strong> The obligation imposed on the inferior by the command; duty and command are correlative terms.</li>
  <li><strong>Sanction:</strong> The evil threatened by the sovereign to enforce compliance. For Austin, sanction is the sole motivator for legal obedience.</li>
  <li><strong>Sovereign:</strong> The determinate political superior who issues the commands.</li>
</ul>

<h3>2. Austin's Characteristics of the Sovereign</h3>
<p>Austin laid down strict conditions for sovereignty:</p>
<ol>
  <li><strong>Determinate Person or Body:</strong> The sovereign must be identifiable (e.g. King in Parliament), not an amorphous crowd or vague public opinion.</li>
  <li><strong>Habitual Obedience from the Bulk of Society:</strong> The bulk of the political society must be in the habit of obedience to this superior.</li>
  <li><strong>No Habit of Obedience to Any Other Superior:</strong> The sovereign himself must not be in the habit of obedience to any higher human political authority.</li>
  <li><strong>Illimitable and Indivisible:</strong> The sovereign cannot be legally limited (sovereign cannot command himself) and sovereignty cannot be divided.</li>
</ol>

<h3>3. Major Criticisms of Austin's Imperative Theory</h3>
<ul>
  <li><strong>Sir Henry Maine (Historical Critique):</strong> Austin ignored customary law. In early societies (such as Maharaja Ranjit Singh's Punjab), the ruler possessed absolute military power but never issued positive statutory commands; society was governed by sacred customs that the ruler dared not breach.</li>
  <li><strong>H.L.A. Hart (Gunman Situation):</strong> Austin reduced law to the order of a gunman in a bank: 'Hand over your money or I will shoot.' A gunman obliges someone to act, but does not impose a genuine legal obligation. Law commands authority because of an accepted internal rule, not mere terror of sanction.</li>
  <li><strong>Constitutional Law &amp; International Law:</strong> Austin was forced to exclude Constitutional Law (calling it positive morality because the sovereign cannot bind himself) and International Law (lacking a world sovereign and sanction).</li>
</ul>
""",
    "quickRevisionPoints": [
      "Austin's Formula: Law = Command of the Sovereign + Duty + Sanction.",
      "Sovereign: Determinate, habitually obeyed by bulk, obeys no superior, legally illimitable.",
      "Austin called International Law 'Positive International Morality'.",
      "Maine's critique: Custom preceded sovereign command (Ranjit Singh example).",
      "Hart's critique: Gunman situation ('being obliged' vs 'having an obligation').",
      "Austin is regarded as the Father of English Jurisprudence."
    ],
    "provisions": [
      {
        "provision": "Austin's Sovereign Test",
        "title": "Habitual Obedience Condition",
        "description": "Bulk of society habitually obeys superior, who in turn obeys no human superior."
      }
    ],
    "definitions": [
      {
        "term": "Command (Austin)",
        "definition": "An expression of a wish by a political superior coupled with the power to inflict an evil (sanction) in the event of disobedience."
      },
      {
        "term": "Sanction (Austin)",
        "definition": "The conditional evil threatened by the sovereign to guarantee compliance with a command."
      }
    ],
    "ingredients": [
      "Determinate political superior (sovereign).",
      "Communicated command expressing a wish.",
      "Correlative legal duty binding the inferior.",
      "Physical coercive sanction backing the command."
    ],
    "exceptions": [
      "Austin recognized three exceptions that are laws though not commands: (1) Declaratory laws, (2) Laws to repeal laws (rescinding laws), and (3) Laws of imperfect obligation (laws lacking a sanction, e.g. time-barred debts)."
    ],
    "examples": [
      {
        "scenario": "A military junta takes power by coup and issues decrees backed by execution squads.",
        "application": "Under Austin's strict criteria, if the bulk of the population obeys out of fear and the junta obeys no superior, its decrees constitute positive law regardless of their tyranny."
      }
    ],
    "landmarkCases": [
      {
        "case": "Madzimbamuto v. Lardner-Burke",
        "citation": "[1969] 1 AC 645",
        "year": "1969",
        "bench": "Privy Council (Lord Reid)",
        "ratio": "The Privy Council examined whether the unilateral declaration of independence by Ian Smith's Rhodesian regime constituted a valid sovereign government, adopting Austinian and Kelsenian tests of effective habitual obedience versus lawful constitutional authority.",
        "impact": "Leading Commonwealth decision on revolutionary sovereignty and habitual obedience."
      }
    ],
    "comparisonTables": [
      {
        "title": "Bentham vs Austin on Positivism",
        "headers": ["Point of Comparison", "Jeremy Bentham", "John Austin"],
        "rows": [
          ["Concept of Sovereign", "Can be legally limited by treaties or internal checks", "Sovereign is strictly legally illimitable and indivisible"],
          ["Concept of Sanction", "Includes both punishment (pain) and rewards (pleasure)", "Restricted exclusively to punitive sanction (infliction of evil)"],
          ["Scope of Work", "Broad social reform via Censorial Jurisprudence", "Strictly formal exposition of existing positive law"]
        ]
      }
    ],
    "diagramId": "diag-jur-jurists-theories",
    "diagramExplanation": "Schematic of Austin's Command Theory illustrating the vertical relationship between the sovereign, command, duty, and sanction.",
    "misconceptions": [
      {
        "myth": "Austin believed judges should not make law.",
        "reality": "Austin defended judge-made law, calling it 'tacit command of the sovereign' (what the sovereign permits, he commands)."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Assuming Austin included 'Rewards' as sanctions.",
        "reality": "Bentham included rewards; Austin strictly excluded rewards, insisting sanctions are always evils/penalties.",
        "rule": "Sanction = Evil only (Austin); Sanction = Pain or Pleasure (Bentham)."
      }
    ],
    "flashcards": [
      {
        "id": "fc-jur-04-05",
        "front": "What four elements constitute positive law according to John Austin?",
        "back": "Command, Duty, Sanction, and Sovereign.",
        "category": "Austinian Theory"
      },
      {
        "id": "fc-jur-04-06",
        "front": "Which three categories of rules did Austin admit as law even though not commands?",
        "back": "Declaratory laws, Repealing laws, and Laws of imperfect obligation.",
        "category": "Austinian Exceptions"
      },
      {
        "id": "fc-jur-04-07",
        "front": "How did H.L.A. Hart describe Austin's command theory?",
        "back": "As the 'Gunman Situation writ large' (failing to distinguish 'being obliged' from 'having an obligation').",
        "category": "Hart's Critique"
      },
      {
        "id": "fc-jur-04-08",
        "front": "Which historical example did Sir Henry Maine cite to refute Austin's command theory?",
        "back": "Maharaja Ranjit Singh of Punjab (ruled by customary religious norms, not statutory commands).",
        "category": "Historical Critique"
      }
    ],
    "sourceReferences": [
      {"title": "The Province of Jurisprudence Determined — John Austin", "url": "https://www.cambridge.org"},
      {"title": "Early History of Institutions — Sir Henry Maine", "url": "https://archive.org"}
    ]
}

data["top-jur-04-03"] = {
    "topicId": "top-jur-04-03",
    "chapterId": "ch-jur-04",
    "subjectId": "law-jurisprudence",
    "title": "H.L.A. Hart: Concept of Law, Primary & Secondary Rules",
    "subtitle": "The Rule of Recognition, Internal Point of View, and Minimum Content of Natural Law",
    "juristRef": "H.L.A. Hart",
    "learningObjective": "Master H.L.A. Hart's critique of Austin, the union of primary and secondary rules, the Rule of Recognition, the internal point of view, and the minimum content of natural law.",
    "introduction": "Herbert Lionel Adolphus Hart (1907–1992) revolutionized analytical jurisprudence with 'The Concept of Law' (1961). Hart rejected Austin's coercive command model, replacing it with an analytical framework centered on social rules, linguistic analysis, and the institutional union of primary and secondary rules.",
    "detailedExplanation": """
<h3>1. The Internal and External Point of View</h3>
<p>Hart demonstrated that Austin's observer sees only the <strong>External Point of View</strong> — predicting that disobedience will lead to punishment (like observing traffic stop when light is red merely to avoid a ticket). However, a legal system functions because officials and citizens adopt the <strong>Internal Point of View</strong> — accepting the rule as a common standard of critical evaluation, feeling that they <em>ought</em> to obey, and using it to justify demands and criticism.</p>

<h3>2. The Union of Primary and Secondary Rules</h3>
<p>Hart defined a mature legal system as the <strong>'Union of Primary and Secondary Rules'</strong>:</p>
<ul>
  <li><strong>Primary Rules of Obligation:</strong> Rules that require human beings to do or abstain from certain actions (e.g. criminal law rules against murder or theft). They impose duties directly on individuals. A primitive society with only primary rules suffers from three fatal defects:
    <ol>
      <li><strong>Uncertainty:</strong> No authoritative method to verify what the rules are.</li>
      <li><strong>Static Quality:</strong> No mechanism to deliberately change, repeal, or adapt rules to new circumstances.</li>
      <li><strong>Inefficiency:</strong> No specialized organ to adjudicate disputes and authoritatively enforce penalties.</li>
    </ol>
  </li>
  <li><strong>Secondary Rules:</strong> Rules that confer power to create, identify, extinguish, and enforce primary rules. They provide the cure for the three defects:
    <ol>
      <li><strong>Rule of Recognition (Cure for Uncertainty):</strong> The apex criteria providing authoritative identification of valid rules in the system (e.g. 'What Queen in Parliament enacts is law' or Indian Constitution Arts. 245, 246).</li>
      <li><strong>Rules of Change (Cure for Static Quality):</strong> Empower legislatures and individuals to introduce new rules and revoke old ones (e.g. Art. 368 amending power, power to make contracts/wills).</li>
      <li><strong>Rules of Adjudication (Cure for Inefficiency):</strong> Empower judicial officials to determine whether a primary rule has been broken and prescribe procedure (e.g. Art. 32, 226, 136).</li>
    </ol>
  </li>
</ul>

<h3>3. The Minimum Content of Natural Law</h3>
<p>While remaining a positivist, Hart admitted that owing to five basic human truisms: (1) Human vulnerability, (2) Approximate equality, (3) Limited altruism, (4) Limited resources, and (5) Limited understanding and strength of will, every viable legal system must contain a <strong>'Minimum Content of Natural Law'</strong> (rules restricting violence, theft, and fraud) to ensure human survival.</p>
""",
    "quickRevisionPoints": [
      "Hart's Core Formulation: Law is the Union of Primary and Secondary Rules.",
      "Primary Rules impose duties (do/abstain); Secondary Rules confer public and private powers.",
      "Three Defects of Primitive Law: Uncertainty, Static nature, Inefficiency.",
      "Three Secondary Cures: Rule of Recognition, Rules of Change, Rules of Adjudication.",
      "Rule of Recognition is the ultimate criterion of legal validity in a municipal system.",
      "Internal Point of View: Acceptance of rules as critical reflective standards of conduct.",
      "Minimum Content of Natural Law: Necessary rules based on 5 human truisms."
    ],
    "provisions": [
      {
        "provision": "Rule of Recognition",
        "title": "Apex Validity Test",
        "description": "The ultimate social practice rule accepted by officials to identify all valid municipal laws."
      }
    ],
    "definitions": [
      {
        "term": "Rule of Recognition",
        "definition": "The secondary rule that provides the criteria by which the validity of other rules of the system is assessed."
      },
      {
        "term": "Internal Aspect of Rules",
        "definition": "The critical, reflective attitude of participants who accept a pattern of behavior as a common guide and standard of criticism."
      }
    ],
    "ingredients": [
      "Official acceptance: Judges and officials must accept secondary rules from an internal point of view.",
      "Citizen obedience: General obedience to primary rules of obligation by the general public.",
      "Systemic coherence: Coordination between primary duties and secondary power-conferring rules."
    ],
    "exceptions": [
      "Core of certainty vs Penumbra of doubt: When statutory rules meet borderline factual situations (open texture of law), judicial discretion must operate."
    ],
    "examples": [
      {
        "scenario": "A parliament enacts a valid amendment following Article 368 procedures.",
        "application": "Its legal validity is confirmed by the secondary 'Rule of Recognition' and enacted via the 'Rule of Change'."
      }
    ],
    "landmarkCases": [
      {
        "case": "Indira Nehru Gandhi v. Raj Narain",
        "citation": "1975 Supp SCC 1",
        "year": "1975",
        "bench": "5-Judge Constitution Bench (Ray CJ, Khanna, Mathew, Beg, Chandrachud JJ)",
        "ratio": "Justice K.K. Mathew explicitly cited H.L.A. Hart's Rule of Recognition, holding that the Constitution itself serves as the ultimate Rule of Recognition in India, and an amendment that seeks to decide an election dispute by raw legislative decree violates the basic judicial functions of adjudication.",
        "impact": "Direct judicial adoption of Hart's secondary rules and Rule of Recognition in Indian constitutional law."
      }
    ],
    "comparisonTables": [
      {
        "title": "Hart's Primary vs Secondary Rules Matrix",
        "headers": ["Type of Rule", "Function & Operation", "Defect Remedied", "Prime Example"],
        "rows": [
          ["Primary Rules", "Impose duties directly on human conduct", "None (Baseline rules of conduct)", "Section 103 BNS (Murder prohibition)"],
          ["Rule of Recognition", "Provides authoritative criteria for legal validity", "Cures Uncertainty", "Constitution of India / Enactment clause"],
          ["Rules of Change", "Empowers creation, amendment, and repeal of rules", "Cures Static Quality", "Article 368 Amendment Procedure"],
          ["Rules of Adjudication", "Empowers courts to identify breaches and enforce", "Cures Inefficiency", "Judicial Powers under Art. 32, 226, CPC"]
        ]
      }
    ],
    "diagramId": "diag-jur-jurists-theories",
    "diagramExplanation": "Diagram showing the interaction between Primary Rules of Obligation and the Triad of Secondary Rules (Recognition, Change, Adjudication).",
    "misconceptions": [
      {
        "myth": "The Rule of Recognition is a written constitutional document.",
        "reality": "Hart explained that the Rule of Recognition is an unwritten customary social practice among officials who recognize and apply the written constitution as authoritative."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing Hart rejected Natural Law completely.",
        "reality": "Hart advocated the 'Minimum Content of Natural Law' based on five universal facts of human nature.",
        "rule": "Hart = Soft/Inclusive Positivism with Minimum Content of Natural Law."
      }
    ],
    "flashcards": [
      {
        "id": "fc-jur-04-09",
        "front": "What constitutes the core definition of law in H.L.A. Hart's 'Concept of Law'?",
        "back": "The Union of Primary and Secondary Rules.",
        "category": "Hart's Jurisprudence"
      },
      {
        "id": "fc-jur-04-10",
        "front": "What are Hart's three secondary rules and which defects do they cure?",
        "back": "Rule of Recognition (Uncertainty), Rule of Change (Static quality), Rule of Adjudication (Inefficiency).",
        "category": "Secondary Rules"
      },
      {
        "id": "fc-jur-04-11",
        "front": "What is the distinction between Hart's 'Internal' and 'External' points of view?",
        "back": "External = Observer predicting punishment; Internal = Participant accepting rules as valid standards of critical behavior.",
        "category": "Internal Point of View"
      },
      {
        "id": "fc-jur-04-12",
        "front": "Which Supreme Court judge extensively cited Hart's Rule of Recognition in the 1975 Election Case?",
        "back": "Justice K.K. Mathew (Indira Nehru Gandhi v. Raj Narain).",
        "category": "Indian Precedent"
      }
    ],
    "sourceReferences": [
      {"title": "The Concept of Law (3rd Ed.) — H.L.A. Hart", "url": "https://global.oup.com"},
      {"title": "Hart's Postscript — Oxford University Press", "url": "https://academic.oup.com"}
    ]
}

data["top-jur-04-04"] = {
    "topicId": "top-jur-04-04",
    "chapterId": "ch-jur-04",
    "subjectId": "law-jurisprudence",
    "title": "Hans Kelsen: Pure Theory of Law & the Grundnorm Hierarchy",
    "subtitle": "Normative Science, Stufenbau Hierarchy, and the Grundnorm Efficacy Test",
    "juristRef": "Hans Kelsen, Adolf Merkl",
    "learningObjective": "Master Hans Kelsen's Pure Theory of Law, the Sein vs Sollen distinction, the Stufenbau hierarchy of norms, the nature of the Grundnorm, and its application in revolutionary situations.",
    "introduction": "Hans Kelsen (1881–1973), an Austrian jurist and principal architect of the Austrian Federal Constitution of 1920, developed the 'Pure Theory of Law' (Reine Rechtslehre). Kelsen sought to liberate jurisprudence from all non-legal elements such as sociology, psychology, ethics, and political ideology, creating a pure structural science of legal norms.",
    "detailedExplanation": """
<h3>1. The 'Purity' of the Pure Theory</h3>
<p>Kelsen insisted that jurisprudence must be purified of alien disciplines. Ethics deals with moral justice, sociology deals with factual behavior, and politics deals with state power. Jurisprudence is concerned exclusively with <strong>Norms</strong> — specific prescriptive standards stating what <em>ought to happen</em> under certain conditions.</p>

<h3>2. The 'Is' (Sein) versus 'Ought' (Sollen) Demarcation</h3>
<ul>
  <li><strong>Natural Science (Sein / What Is):</strong> Governed by the Principle of Causality (Cause and Effect). E.g., if metal is heated, it expands.</li>
  <li><strong>Legal Science (Sollen / What Ought to Be):</strong> Governed by the Principle of <strong>Imputation (Zurechnung)</strong>. E.g., if a person commits theft, an organ of the state <em>ought</em> to inflict punishment. A legal rule is an 'ought-proposition'.</li>
</ul>

<h3>3. Stufenbau: The Pyramid Hierarchy of Norms</h3>
<p>Developed with Adolf Merkl, Kelsen structured law as a dynamic hierarchical pyramid (<em>Stufenbau</em>):</p>
<ul>
  <li>Each lower norm derives its validity from a superior norm authorizing its creation.</li>
  <li>An administrative order derives validity from a statute; a statute derives validity from the constitution; the historical constitution derives its validity from an ultimate presupposed apex norm: the <strong>Grundnorm (Basic Norm)</strong>.</li>
</ul>

<h3>4. The Grundnorm (Basic Norm)</h3>
<p>The Grundnorm is the hypothetical apex presupposition that gives validity to the entire constitutional order. It is not created by positive enactment, but is <em>presupposed</em> to be valid by legal science. The validity of the Grundnorm depends on <strong>Minimum Effectiveness</strong> (efficacy). If a successful revolution or coup d'état overthrows the old constitutional order and establishes an effective government commanding general obedience, the Grundnorm changes (Revolutionary Grundnorm).</p>
""",
    "quickRevisionPoints": [
      "Kelsen's Pure Theory: Law is purified of sociology, ethics, psychology, and politics.",
      "Sein (Is / Causality in natural science) vs Sollen (Ought / Imputation in legal science).",
      "Stufenbau: Pyramidal hierarchy of norms where lower norms derive validity from higher norms.",
      "Grundnorm: The apex, presupposed basic norm from which the entire legal order derives validity.",
      "Efficacy Condition: Grundnorm is valid only as long as the legal order is by and large effective.",
      "Revolutionary Grundnorm: A successful revolution changes the basic norm."
    ],
    "provisions": [
      {
        "provision": "Kelsen's Imputation Principle",
        "title": "Zurechnung Formulation",
        "description": "If condition X occurs, sanction Y ought to be inflicted by the authorized state organ."
      }
    ],
    "definitions": [
      {
        "term": "Grundnorm",
        "definition": "The ultimate presupposed postulate which serves as the supreme source of validity for all legal norms in a legal order."
      },
      {
        "term": "Principle of Imputation",
        "definition": "The connection between condition and consequence in normative law (ought), contrasting with causality (is) in natural science."
      }
    ],
    "ingredients": [
      "Normativity: Rules expressed as conditional sanctions and ought-prescriptions.",
      "Hierarchical derivation: Validated step-by-step from base to apex.",
      "Presupposition: Acceptance of an ultimate foundational basic norm.",
      "Societal efficacy: By-and-large compliance by the population."
    ],
    "exceptions": [
      "If the legal order loses minimum general effectiveness, the Grundnorm collapses and ceases to validate norms."
    ],
    "examples": [
      {
        "scenario": "A police officer issues a traffic penalty ticket under a state regulation.",
        "application": "The ticket is valid because authorized by the regulation; the regulation is valid because authorized by the Motor Vehicles Act; the Act is valid under Article 246 of the Constitution; the Constitution is valid because the Grundnorm mandates obedience to the Constituent Assembly."
      }
    ],
    "landmarkCases": [
      {
        "case": "State v. Dosso",
        "citation": "PLD 1958 SC 533",
        "year": "1958",
        "bench": "Supreme Court of Pakistan (Muhammad Munir CJ)",
        "ratio": "The Supreme Court of Pakistan adopted Kelsen's Pure Theory of Law, holding that a successful military coup d'état destroys the old Grundnorm, and an effective revolutionary regime becomes a new law-creating organ whose commands are valid law.",
        "impact": "Internationally celebrated precedent applying Kelsen's Grundnorm to revolutionary regimes (subsequently qualified in Asma Jilani)."
      }
    ],
    "comparisonTables": [
      {
        "title": "Austin's Sovereign vs Kelsen's Grundnorm",
        "headers": ["Philosophical Dimension", "John Austin (Command)", "Hans Kelsen (Pure Theory)"],
        "rows": [
          ["Apex Authority", "Factual human political sovereign (King/Parliament)", "Hypothetical, presupposed legal norm (Grundnorm)"],
          ["Nature of Law", "Command backed by physical sanction", "Normative ought-proposition based on imputation"],
          ["Role of Sociology", "Relies heavily on habitual factual obedience", "Purified strictly of all sociological and empirical elements"],
          ["Hierarchy Structure", "Simple two-tier: Sovereign above, Subject below", "Multi-layered pyramid of norms (Stufenbau)"]
        ]
      }
    ],
    "diagramId": "diag-jur-jurists-theories",
    "diagramExplanation": "The Stufenbau pyramid illustrating the hierarchical descent of normative validity from the Grundnorm down to individual administrative orders.",
    "misconceptions": [
      {
        "myth": "The Grundnorm is the text of the Constitution of India itself.",
        "reality": "The written Constitution is a positive norm. The Grundnorm is the presupposition that the framers of the Constitution had authority to bind the nation."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Confusing Causality with Imputation.",
        "reality": "Causality governs physical science ('Is'); Imputation governs normative law ('Ought').",
        "rule": "Causality = Natural Science (Sein); Imputation = Legal Norms (Sollen)."
      }
    ],
    "flashcards": [
      {
        "id": "fc-jur-04-13",
        "front": "What does Kelsen mean by 'Pure Theory of Law'?",
        "back": "A theory purified of all extraneous sociological, ethical, psychological, and political ideologies.",
        "category": "Kelsen's Philosophy"
      },
      {
        "id": "fc-jur-04-14",
        "front": "What is the German term for the pyramid hierarchy of norms developed by Kelsen and Merkl?",
        "back": "Stufenbau (Hierarchy of Norms).",
        "category": "Stufenbau Theory"
      },
      {
        "id": "fc-jur-04-15",
        "front": "What is the difference between 'Causality' and 'Imputation' in Kelsen's jurisprudence?",
        "back": "Causality connects natural cause and effect ('Is'); Imputation connects legal condition to sanction ('Ought').",
        "category": "Kelsen's Concepts"
      },
      {
        "id": "fc-jur-04-16",
        "front": "Which celebrated 1958 foreign court decision applied Kelsen's Grundnorm to validate a military coup?",
        "back": "State v. Dosso (Supreme Court of Pakistan).",
        "category": "Comparative Precedent"
      }
    ],
    "sourceReferences": [
      {"title": "Pure Theory of Law — Hans Kelsen (Trans. Max Knight)", "url": "https://www.ucpress.edu"},
      {"title": "General Theory of Law and State — Hans Kelsen", "url": "https://www.hup.harvard.edu"}
    ]
}

create_concept_file('assets/learning/data/jurisprudence/jurisprudence-concepts-part1.js', 'JURISPRUDENCE_CONCEPTS_PART1', data)
print(f"Jurisprudence Part 1 completely authored: {len(data)} topics!")
