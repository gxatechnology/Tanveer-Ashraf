import json
from concept_helpers import create_concept_file

# Load current Part 2
with open('assets/learning/data/jurisprudence/jurisprudence-concepts-part2.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('const DATA = ') + len('const DATA = ')
end_idx = text.rfind(';\n\n  global.')
data = json.loads(text[idx:end_idx])

# -------------------------------------------------------------
# CHAPTER 6: SOCIOLOGICAL SCHOOL
# -------------------------------------------------------------
data["top-jur-06-01"] = {
    "topicId": "top-jur-06-01",
    "chapterId": "ch-jur-06",
    "subjectId": "law-jurisprudence",
    "title": "Foundations: Ihering, Ehrlich's Living Law & Duguit's Solidarity",
    "subtitle": "Law as a Means to an End, Social Fact, and Interdependence",
    "juristRef": "Rudolf von Ihering, Eugen Ehrlich, Léon Duguit",
    "learningObjective": "Master the European origins of sociological jurisprudence, comparing Ihering's purpose in law, Ehrlich's 'Living Law', and Duguit's doctrine of 'Social Solidarity'.",
    "introduction": "The Sociological School shifted legal focus from abstract conceptual logic and state commands to the living functioning of law within human society. It treats law not as a closed formal system, but as a dynamic social institution shaped by social needs, economic pressures, and collective interdependence.",
    "detailedExplanation": """
<h3>1. Rudolf von Ihering (1818–1892): 'Law as a Means to an End'</h3>
<p>Known as the 'Father of Modern Sociological Jurisprudence', Ihering revolted against Savigny's passive historical determinism. In his masterpiece <em>'Law as a Means to an End' (Der Zweck im Recht)</em>, Ihering established that <strong>'Purpose is the creator of the entire law'</strong>. There is no legal rule which does not owe its origin to a practical purpose (Zweck) — to realize a condition of social life. In <em>The Struggle for Law (Der Kampf ums Recht)</em>, he maintained that law is not achieved through effortless organic growth, but through continuous human struggle against injustice.</p>

<h3>2. Eugen Ehrlich (1862–1922): The 'Living Law'</h3>
<p>In <em>Fundamental Principles of the Sociology of Law (1913)</em>, Austrian jurist Eugen Ehrlich propounded that <em>'the center of gravity of legal development lies not in legislation, nor in juristic science, nor in judicial decisions, but in society itself.'</em> Ehrlich distinguished between:</p>
<ul>
  <li><strong>Formal Law of the State:</strong> The statutory codes and court judgments.</li>
  <li><strong>The Living Law (Lebendes Recht):</strong> The actual social norms and customs that people voluntarily observe in their daily interactions (e.g. business contracts, family customs, commercial usages), even if completely unwritten and unrecognized by state courts. State law that defies the living law remains ineffective.</li>
</ul>

<h3>3. Léon Duguit (1859–1928): The Doctrine of 'Social Solidarity'</h3>
<p>French jurist Léon Duguit rejected traditional notions of sovereignty, natural rights, and state personality as metaphysical myths. His single foundational axiom was <strong>'Social Solidarity'</strong> (<em>La Solidarité Sociale</em>) — the inescapable fact that modern humans cannot live in isolation; they depend completely on one another through division of labor and mutual exchange of services. Law is an objective social fact: any rule that promotes social solidarity is valid; any rule that harms social solidarity is invalid. Duguit replaced individual subjective rights with 'social functions' and legal duties.</p>
""",
    "quickRevisionPoints": [
      "Ihering: 'Purpose is the creator of all law' (Law as a Means to an End); 'The Struggle for Law'.",
      "Ehrlich: 'Center of gravity of legal development lies in society itself' — The Living Law.",
      "Living Law = Actual norms observed in social life vs formal statutory court rules.",
      "Duguit: Replaced Sovereignty and Rights with 'Social Solidarity' and mutual interdependence.",
      "Duguit: No individual rights exist; individuals have only social duties to perform."
    ],
    "provisions": [
      {
        "provision": "Ihering's Axiom",
        "title": "Purpose in Law",
        "description": "Law is the sum of the conditions of social life in the widest sense of the term, as secured by the power of the State through external compulsion."
      }
    ],
    "definitions": [
      {
        "term": "Living Law (Ehrlich)",
        "definition": "The inner order of human associations and social relations actually dominating life, independent of state court enforcement."
      },
      {
        "term": "Social Solidarity (Duguit)",
        "definition": "The objective fact of human interdependence resulting from shared common needs and mutual division of labor."
      }
    ],
    "ingredients": [
      "Primacy of social purpose over formalistic statutory logic.",
      "Observation of extra-legal societal practices dominating community life.",
      "Evaluation of legal validity based on functional contribution to social cohesion."
    ],
    "exceptions": [
      "Duguit's complete elimination of individual rights leaves citizens vulnerable to state totalitarianism under the pretext of collective social solidarity."
    ],
    "examples": [
      {
        "scenario": "A state passes a statute prohibiting dowry. In a rural district, families continue customary gift exchanges as normal social practice.",
        "application": "Under Ehrlich's theory, the custom represents the 'Living Law' actually dominating conduct, while the state statute remains an ineffective formal norm."
      }
    ],
    "landmarkCases": [
      {
        "case": "National Textile Workers' Union v. P.R. Ramakrishnan",
        "citation": "(1983) 1 SCC 228",
        "year": "1983",
        "bench": "5-Judge Constitution Bench (Bhagwati J)",
        "ratio": "The Supreme Court applied sociological jurisprudence and Duguit's social solidarity doctrine, holding that in company winding-up petitions, workers have a direct legal interest and right to be heard, because a company is not merely a profit vehicle for shareholders, but a social enterprise based on labor-capital interdependence.",
        "impact": "Classic Indian judicial adoption of sociological jurisprudence to recognize labor rights in corporate law."
      }
    ],
    "comparisonTables": [
      {
        "title": "Ihering vs Ehrlich vs Duguit",
        "headers": ["Jurist", "Pivotal Concept", "Apex Legal Principle", "Attitude to State Power"],
        "rows": [
          ["Rudolf von Ihering", "Purpose in Law (Der Zweck)", "Law is a weapon in the conscious struggle for social purpose", "State compulsion is necessary to guarantee conditions of life"],
          ["Eugen Ehrlich", "The Living Law (Lebendes Recht)", "True law lives in spontaneous social associations, not statutes", "State law is secondary and often ignored by living law"],
          ["Léon Duguit", "Social Solidarity (Solidarité Sociale)", "Law is an objective social fact promoting human interdependence", "Denies sovereignty; state is merely a servant of social solidarity"]
        ]
      }
    ],
    "diagramId": "diag-jur-schools-comparison",
    "diagramExplanation": "Diagram maps the sociological transition from Ihering's purpose to Ehrlich's living law and Duguit's solidarity.",
    "misconceptions": [
      {
        "myth": "Ehrlich argued that judges should completely abandon statutory codes.",
        "reality": "Ehrlich explained that judges must understand the Living Law to interpret and bridge the gap between static statutory words and dynamic commercial realities."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Attributing 'Living Law' to Roscoe Pound.",
        "reality": "Eugen Ehrlich originated 'Living Law'; Roscoe Pound originated 'Social Engineering' and 'Law in Books vs Law in Action'.",
        "rule": "Living Law = Ehrlich; Social Engineering = Roscoe Pound."
      }
    ],
    "flashcards": [
      {
        "id": "fc-jur-06-01",
        "front": "Who wrote 'The Struggle for Law' and 'Law as a Means to an End'?",
        "back": "Rudolf von Ihering.",
        "category": "Sociological School"
      },
      {
        "id": "fc-jur-06-02",
        "front": "Who coined the jurisprudential concept of 'The Living Law'?",
        "back": "Eugen Ehrlich.",
        "category": "Ehrlich's Concepts"
      },
      {
        "id": "fc-jur-06-03",
        "front": "What doctrine was propounded by French jurist Léon Duguit to replace state sovereignty?",
        "back": "Social Solidarity (Solidarité Sociale).",
        "category": "Duguit's Theory"
      },
      {
        "id": "fc-jur-06-04",
        "front": "Who stated that 'the center of gravity of legal development lies not in legislation... but in society itself'?",
        "back": "Eugen Ehrlich.",
        "category": "Sociological Maxims"
      }
    ],
    "sourceReferences": [
      {"title": "Fundamental Principles of the Sociology of Law — Eugen Ehrlich", "url": "https://www.hup.harvard.edu"},
      {"title": "Law as a Means to an End — Rudolf von Ihering", "url": "https://archive.org"}
    ]
}

data["top-jur-06-02"] = {
    "topicId": "top-jur-06-02",
    "chapterId": "ch-jur-06",
    "subjectId": "law-jurisprudence",
    "title": "Roscoe Pound: Theory of Social Engineering & Jural Postulates",
    "subtitle": "Balancing Competing Interests, Jural Postulates, and Law in Action",
    "juristRef": "Roscoe Pound",
    "learningObjective": "Master Roscoe Pound's Theory of Social Engineering, his three-fold classification of interests (Individual, Public, Social), the Jural Postulates, and the distinction between Law in Books and Law in Action.",
    "introduction": "Roscoe Pound (1870–1964), Dean of Harvard Law School, was the undisputed leader of American Sociological Jurisprudence. Pound treated law as an applied functional science, coining the famous metaphor of **'Social Engineering'** to describe the judicial task of balancing competing societal claims.",
    "detailedExplanation": """
<h3>1. The Theory of 'Social Engineering'</h3>
<p>Pound compared the jurist to an engineer: just as an engineer designs bridges to eliminate friction, waste, and structural failure, so the legal system must structure rules to satisfy maximum human wants with the minimum friction and waste of social resources: <em>'Law is the specialized form of social control, exerting pressure to satisfy the maximum of human claims and desires with the least sacrifice.'</em></p>

<h3>2. Pound's Three-Fold Classification of Interests</h3>
<p>Pound categorized all conflicting legal claims and desires into three planes:</p>
<ul>
  <li><strong>1. Individual Interests:</strong> Demands directly involving individual life:
    <ul>
      <li>Interests of Personality (physical integrity, honor, privacy, freedom of belief).</li>
      <li>Domestic Relations (marriage, parents and children).</li>
      <li>Interests of Substance (property, freedom of contract, freedom of trade).</li>
    </ul>
  </li>
  <li><strong>2. Public Interests:</strong> Claims asserted by the state as a juristic political entity:
    <ul>
      <li>Interests of the state as a juristic person (personality of the state, maintenance of territory).</li>
      <li>Interests of the state as the guardian of social interests.</li>
    </ul>
  </li>
  <li><strong>3. Social Interests:</strong> The generalized claims essential to social life:
    <ul>
      <li>Social interest in general security (peace, order, public health, security of transactions).</li>
      <li>Social interest in security of social institutions (marriage, religious institutions, political bodies).</li>
      <li>Social interest in general morals (prohibiting obscenity, corruption, gambling).</li>
      <li>Social interest in conservation of social resources (natural resources, protection of dependents).</li>
      <li>Social interest in general progress (economic, political, and cultural advancement).</li>
      <li>Social interest in individual life (ensuring every human being can live a human life worthy of dignity).</li>
    </ul>
  </li>
</ul>

<h3>3. The Jural Postulates</h3>
<p>To evaluate and weigh these interests, Pound formulated <strong>Five Jural Postulates</strong> of a civilized society (presuppositions that civilized men are entitled to assume):</p>
<ol>
  <li>Others will commit no intentional aggressions upon them.</li>
  <li>They may control for beneficial purposes what they have discovered, created, or acquired.</li>
  <li>Others with whom they contract will make good their promises in good faith.</li>
  <li>Others will act with due care not to cast an unreasonable risk of injury upon them.</li>
  <li>Others who maintain things likely to escape and do damage will keep them within safe bounds (Rylands v Fletcher principle).</li>
</ol>

<h3>4. Law in Books vs Law in Action</h3>
<p>In a seminal 1910 paper, Pound distinguished between <strong>'Law in Books'</strong> (the black-letter statutory provisions and doctrines recorded in volumes) and <strong>'Law in Action'</strong> (how the law actually operates in police stations, courts, and administrative enforcement).</p>
""",
    "quickRevisionPoints": [
      "Roscoe Pound: Leader of American Sociological School; Dean of Harvard Law School.",
      "Social Engineering: Satisfying maximum human wants with minimum friction and waste.",
      "Three-fold Interests: Individual, Public, and Social Interests.",
      "Balancing Rule: Interests must be weighed on the SAME plane (preferably transferred to social plane).",
      "Five Jural Postulates: Baseline civilizational expectations (non-aggression, property, contract, care, containment).",
      "Law in Books vs Law in Action: Doctrinal rules vs empirical judicial execution."
    ],
    "provisions": [
      {
        "provision": "Pound's Balancing Principle",
        "title": "Weighing on Same Level",
        "description": "Never balance an individual interest directly against a social interest; translate both onto the social plane before balancing."
      }
    ],
    "definitions": [
      {
        "term": "Social Engineering",
        "definition": "The systematic ordering of human relations through the politically organized society to maximize satisfaction of desires and claims with least waste."
      },
      {
        "term": "Jural Postulates",
        "definition": "The reasonable expectations and practical assumptions of civilized society upon which legal rights and duties are constructed."
      }
    ],
    "ingredients": [
      "Fact-finding: Investigation of actual social effects of legal doctrines.",
      "Sociological study of judicial method and administrative execution.",
      "Continuous pragmatic revision of legal standards to meet emergent industrial realities."
    ],
    "exceptions": [
      "Pound conceded that interests are never static; he formulated new jural postulates in the 20th century regarding employment security and collective social insurance."
    ],
    "examples": [
      {
        "scenario": "A factory pollutes a river, asserting the owner's individual interest in freedom of trade against the community's demand for clean drinking water.",
        "application": "Under Pound's balancing framework, the claim is weighed on the social plane: the social interest in economic progress vs the paramount social interest in public health and conservation of resources."
      }
    ],
    "landmarkCases": [
      {
        "case": "M.C. Mehta v. Union of India (Oleum Gas Leak Case)",
        "citation": "(1987) 1 SCC 395",
        "year": "1987",
        "bench": "5-Judge Constitution Bench (P.N. Bhagwati CJ)",
        "ratio": "The Supreme Court applied Roscoe Pound's social engineering principle to create the new doctrine of Absolute Liability, holding that an enterprise engaged in a hazardous industrial activity owes an absolute, non-delegable duty to the community that cannot be evaded through common law exceptions.",
        "impact": "Monumental Indian constitutional application of social engineering to balance industrial enterprise against community survival."
      }
    ],
    "comparisonTables": [
      {
        "title": "Roscoe Pound's Three-Fold Classification of Interests",
        "headers": ["Category of Interest", "Sub-Types", "Primary Examples"],
        "rows": [
          ["Individual Interests", "Personality, Domestic Relations, Substance", "Reputation, freedom of speech, marriage, private contract, ownership"],
          ["Public Interests", "State as Juristic Person, State as Guardian", "Defense of borders, preservation of revenue, public land administration"],
          ["Social Interests", "Security, Morals, Conservation, Progress, Individual Life", "Public health, anti-corruption, forest preservation, basic human dignity"]
        ]
      }
    ],
    "diagramId": "diag-jur-jurists-theories",
    "diagramExplanation": "Pound's functional scale balancing Individual, Public, and Social Interests through Jural Postulates.",
    "misconceptions": [
      {
        "myth": "Pound believed an individual interest should be directly weighed against a social interest.",
        "reality": "Pound strictly warned against this, noting that weighing an individual claim against a social interest automatically biases the scale in favor of the collective. Both must be generalized to the same level."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing Jural Postulates are immutable natural law principles.",
        "reality": "Pound explained that Jural Postulates are empirical assumptions of a specific civilized society at a given historical time and place, not eternal dogmas.",
        "rule": "Jural Postulates = Historical and civilizational assumptions, not eternal natural law."
      }
    ],
    "flashcards": [
      {
        "id": "fc-jur-06-05",
        "front": "Who defined law as 'Social Engineering' to satisfy maximum wants with minimum friction?",
        "back": "Roscoe Pound.",
        "category": "Roscoe Pound"
      },
      {
        "id": "fc-jur-06-06",
        "front": "What are the three classes of interests formulated by Roscoe Pound?",
        "back": "Individual Interests, Public Interests, and Social Interests.",
        "category": "Pound's Taxonomy"
      },
      {
        "id": "fc-jur-06-07",
        "front": "How many Jural Postulates did Pound initially formulate for civilized society?",
        "back": "Five Jural Postulates.",
        "category": "Jural Postulates"
      },
      {
        "id": "fc-jur-06-08",
        "front": "What famous distinction did Pound introduce in 1910 regarding legal reality?",
        "back": "'Law in Books' versus 'Law in Action'.",
        "category": "Sociological Concepts"
      }
    ],
    "sourceReferences": [
      {"title": "An Introduction to the Philosophy of Law — Roscoe Pound", "url": "https://yalebooks.yale.edu"},
      {"title": "Jurisprudence (Vols 1–5) — Roscoe Pound", "url": "https://www.westacademic.com"}
    ]
}

# -------------------------------------------------------------
# CHAPTER 7: REALIST SCHOOL & MODERN TRENDS
# -------------------------------------------------------------
data["top-jur-07-01"] = {
    "topicId": "top-jur-07-01",
    "chapterId": "ch-jur-07",
    "subjectId": "law-jurisprudence",
    "title": "American Realism: Oliver Wendell Holmes Jr. & Jerome Frank",
    "subtitle": "The Bad Man Theory, Rule-Skepticism, and Fact-Skepticism",
    "juristRef": "Oliver Wendell Holmes Jr., Karl Llewellyn, Jerome Frank",
    "learningObjective": "Master American Legal Realism, Holmes's 'Bad Man Theory' and experience dictum, Karl Llewellyn's rule-skepticism, and Jerome Frank's fact-skepticism.",
    "introduction": "American Legal Realism emerged in the 1920s and 1930s as a radical revolt against legal formalism, mechanical jurisprudence, and the illusion of certainty in appellate precedent. Realists argued that law is not an abstract system of pure logic, but what human judges and officials actually decide in concrete courtrooms.",
    "detailedExplanation": """
<h3>1. Oliver Wendell Holmes Jr.: The Grandfather of Realism</h3>
<p>In <em>The Common Law (1881)</em>, Justice Holmes delivered the defining aphorism of realist jurisprudence: <strong>'The life of the law has not been logic: it has been experience.'</strong> Law reflects the felt necessities of the time, prevalent moral and political theories, intuitions of public policy, and even judges' personal prejudices, far more than syllogistic deduction.</p>
<p>In <em>The Path of the Law (1897)</em>, Holmes introduced the <strong>'Bad Man Theory'</strong>: If you want to know what the law really is and nothing else, you must look at it as a bad man, who cares only for the material consequences which such knowledge enables him to predict, not as a good man finding his reasons for conduct in vague moral conscience. Law is nothing more than: <strong>'The prophecies of what the courts will do in fact, and nothing more pretentious, are what I mean by the law.'</strong></p>

<h3>2. Karl Llewellyn: Rule-Skepticism</h3>
<p>Karl Llewellyn (1893–1962) outlined the core realist tenets: law is in flux; law is a means to social ends; society moves faster than law; and temporary divorce of 'Is' from 'Ought' during factual study is essential. Llewellyn was a <strong>'Rule-Skeptic'</strong>: he distrusted conventional paper rules (black-letter statutes) because judges often reach a decision based on intuitive sense of fairness ('the hunch') and then hunt for statutory rules to rationalize it ex-post.</p>

<h3>3. Jerome Frank: Fact-Skepticism</h3>
<p>In <em>Law and the Modern Mind (1930)</em>, Jerome Frank argued that the search for absolute legal certainty is an infantile neurosis (comparing it to a child's search for an infallible father figure). Frank was a <strong>'Fact-Skeptic'</strong>: even if legal rules were 100% certain, trial outcomes remain utterly unpredictable because of the complete unreliability of trial court fact-finding — witnesses lie, forget, or misperceive; documents are lost; and judges/jurors harbor subconscious human biases (conditioned by what the judge had for breakfast, his background, race, or demeanor).</p>
""",
    "quickRevisionPoints": [
      "American Realism: Revolt against mechanical jurisprudence; law is what judges do in fact.",
      "Holmes: 'The life of the law has not been logic: it has been experience' (1881).",
      "Holmes's Bad Man Theory: Law is the prediction of what courts will do in fact.",
      "Llewellyn (Rule-Skeptic): Paper rules do not dictate decisions; judges decide by intuition.",
      "Jerome Frank (Fact-Skeptic): Trial facts are elusive, unpredictable, and biased (Law and the Modern Mind).",
      "Basic Equation of Realism: Decision = Personality of the Judge × Stimuli of the Facts."
    ],
    "provisions": [
      {
        "provision": "Holmes's Prediction Formula",
        "title": "Prophecy Theory of Law",
        "description": "The prophecies of what the courts will do in fact, and nothing more pretentious, are what I mean by the law."
      }
    ],
    "definitions": [
      {
        "term": "Rule-Skepticism (Llewellyn)",
        "definition": "Skepticism toward formal paper rules as the true explanatory basis for appellate court judicial decisions."
      },
      {
        "term": "Fact-Skepticism (Frank)",
        "definition": "The conviction that trial court decisions are unpredictable because the ascertainment of past facts through fallible human testimony is inherently uncertain."
      }
    ],
    "ingredients": [
      "Pragmatic empirical investigation of trial court processes.",
      "Rejection of mechanical deduction from statutory premises.",
      "Psychological and behavioral analysis of judicial decision-making."
    ],
    "exceptions": [
      "Realism was criticized for ignoring that judges are guided and constrained by legal rules when taking the judicial oath, and for reducing law to subjective caprice."
    ],
    "examples": [
      {
        "scenario": "Two identical criminal trials for cheque bounce produce opposite outcomes because Judge A believes the complainant's witness while Judge B finds the complainant evasive.",
        "application": "Jerome Frank's fact-skepticism explains this divergence: the variable was not the statutory rule of Negotiable Instruments Act, but the subjective human fact-finding of the trial judges."
      }
    ],
    "landmarkCases": [
      {
        "case": "Rameshwar Prasad v. Union of India",
        "citation": "(2006) 2 SCC 1",
        "year": "2006",
        "bench": "5-Judge Constitution Bench (Y.K. Sabharwal CJ)",
        "ratio": "The Supreme Court examined subjective satisfaction in the dissolution of the Bihar Legislative Assembly, emphasizing that judicial review assesses real constitutional motives rather than formal recitals, exemplifying realist scrutiny of executive pretexts.",
        "impact": "Exemplified the realist judicial technique of piercing formal legal veneers to inspect political reality."
      }
    ],
    "comparisonTables": [
      {
        "title": "Rule-Skepticism vs Fact-Skepticism",
        "headers": ["Comparison Metric", "Rule-Skepticism (Llewellyn)", "Fact-Skepticism (Jerome Frank)"],
        "rows": [
          ["Chief Focus", "Appellate Court decisions and written opinions", "Trial Court proceedings and fact-finding"],
          ["Source of Unpredictability", "Multiplicity of competing legal rules and rationales", "Subjective witness unreliability and judicial perceptual bias"],
          ["Solution Proposed", "Better empirical study of real commercial practices", "Reform of trial procedures, judicial psychology, and bench education"]
        ]
      }
    ],
    "diagramId": "diag-jur-schools-comparison",
    "diagramExplanation": "Diagram contrasting Mechanical Jurisprudence (Rules -> Decision) with Legal Realism (Facts + Judicial Psychology -> Decision -> Ex-post Rationalization).",
    "misconceptions": [
      {
        "myth": "Legal Realists argue that rules do not matter at all and judges can decide whatever they like.",
        "reality": "Realists argue that formal rules are not the *sole* cause of decisions; rules act as limiting horizons, but non-rule factors drive outcomes."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Confusing Rule-Skeptics with Fact-Skeptics.",
        "reality": "Llewellyn was a Rule-Skeptic; Jerome Frank was a Fact-Skeptic.",
        "rule": "Llewellyn = Rule-Skeptic; Jerome Frank = Fact-Skeptic."
      }
    ],
    "flashcards": [
      {
        "id": "fc-jur-07-01",
        "front": "Who famously declared: 'The life of the law has not been logic: it has been experience'?",
        "back": "Oliver Wendell Holmes Jr. in 'The Common Law' (1881).",
        "category": "American Realism"
      },
      {
        "id": "fc-jur-07-02",
        "front": "What is Justice Holmes's 'Bad Man Theory'?",
        "back": "To know the law, look through the eyes of a bad man who cares only about predicting material penalties.",
        "category": "Holmes's Concepts"
      },
      {
        "id": "fc-jur-07-03",
        "front": "Who authored 'Law and the Modern Mind' (1930) and championed Fact-Skepticism?",
        "back": "Jerome Frank.",
        "category": "Fact-Skepticism"
      },
      {
        "id": "fc-jur-07-04",
        "front": "Which American realist jurist drafted the Uniform Commercial Code (UCC)?",
        "back": "Karl Llewellyn.",
        "category": "Rule-Skepticism"
      }
    ],
    "sourceReferences": [
      {"title": "The Path of the Law — Oliver Wendell Holmes Jr. (1897)", "url": "https://www.jstor.org"},
      {"title": "Law and the Modern Mind — Jerome Frank", "url": "https://archive.org"}
    ]
}

data["top-jur-07-02"] = {
    "topicId": "top-jur-07-02",
    "chapterId": "ch-jur-07",
    "subjectId": "law-jurisprudence",
    "title": "Scandinavian Realism & Comparative Jurisprudential Synthesis",
    "subtitle": "Hägerström, Olivecrona, Alf Ross, and the Synthesis of Legal Schools",
    "juristRef": "Axel Hägerström, Karl Olivecrona, Alf Ross, A.V. Lundstedt",
    "learningObjective": "Compare Scandinavian Realism with American Realism, evaluate Hägerström's anti-metaphysical philosophy, Olivecrona's 'Independent Imperatives', and Alf Ross's psychological prediction theory.",
    "introduction": "While American Realism focused on the practical behavior of trial judges and courtroom psychology, Scandinavian Realism (the Uppsala School) adopted a rigorous philosophical assault on metaphysics. Scandinavian realists dismantled mystical legal concepts like 'rights', 'duties', and 'sovereignty', treating them as psychological illusions and linguistic magic.",
    "detailedExplanation": """
<h3>1. Axel Hägerström (1868–1939): The Spiritual Father</h3>
<p>Hägerström asserted that metaphysics must be destroyed: <em>'Praeterea censeo metaphysicam esse delendam'</em>. He proved through Roman law that ancient legal concepts like <em>Mancipatio</em> were based on verbal magic (incantations believed to magically transfer mystical power). Modern notions of 'legal right' are merely secularized magical superstitions possessing no physical reality in the empirical world.</p>

<h3>2. Karl Olivecrona: Law as Fact &amp; 'Independent Imperatives'</h3>
<p>In <em>Law as Fact (1939)</em>, Olivecrona analyzed the psychological machinery of law. He rejected Austin's idea that law is a command of an identifiable sovereign person. Instead, legal rules are <strong>'Independent Imperatives'</strong> — imperative messages addressed to the general public by impersonal state organs, acting directly upon human psychology through ceremonies, uniforms, and solemn language to induce automatic habits of obedience.</p>

<h3>3. Alf Ross: Directives and Valid Law</h3>
<p>In <em>On Law and Justice (1958)</em>, Danish jurist Alf Ross synthesized positivism and realism. He defined legal norms as <strong>'Directives'</strong> designed to guide judges. Valid law (Gældende Ret) is not an abstract metaphysical idea, but the body of directives which judges actually feel emotionally bound by and apply in their judgments. Law is a predictive science combining external compliance with the internal psychological feeling of obligation.</p>

<h3>4. Comparative Synthesis of the Five Major Schools</h3>
<table class="academic-table">
  <thead>
    <tr>
      <th>School of Jurisprudence</th>
      <th>Ultimate Source of Law</th>
      <th>Key Focus</th>
      <th>Leading Jurist</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Natural Law</strong></td>
      <td>Reason, Nature, Divine Will</td>
      <td>Moral Justice &amp; Ethics</td>
      <td>Aquinas, Fuller, Finnis</td>
    </tr>
    <tr>
      <td><strong>Analytical Positivism</strong></td>
      <td>State Sovereign Enactment</td>
      <td>Law as it Is; Positive Norms</td>
      <td>Austin, Hart, Kelsen</td>
    </tr>
    <tr>
      <td><strong>Historical School</strong></td>
      <td>Custom &amp; National Consciousness</td>
      <td>Organic Evolutionary Tradition</td>
      <td>Savigny, Maine</td>
    </tr>
    <tr>
      <td><strong>Sociological School</strong></td>
      <td>Societal Needs &amp; Institutions</td>
      <td>Functional Social Engineering</td>
      <td>Ihering, Ehrlich, Pound</td>
    </tr>
    <tr>
      <td><strong>Realist School</strong></td>
      <td>Judicial Action &amp; Psychology</td>
      <td>Empirical Courtroom Outcomes</td>
      <td>Holmes, Frank, Ross</td>
    </tr>
  </tbody>
</table>
""",
    "quickRevisionPoints": [
      "Scandinavian Realism (Uppsala School): Philosophical, anti-metaphysical critique of legal concepts.",
      "Hägerström: Legal rights and duties are secularized magical superstitions (Roman mancipatio).",
      "Olivecrona: Law as Fact; legal rules are 'Independent Imperatives' functioning as psychological machinery.",
      "Alf Ross: Legal norms are directives; valid law is what judges feel bound by and apply.",
      "American Realism is court-centered and empirical; Scandinavian Realism is language-centered and anti-metaphysical."
    ],
    "provisions": [
      {
        "provision": "Olivecrona's Law as Fact",
        "title": "Independent Imperatives",
        "description": "Rules operating as psychological signposts without an individual commanding sovereign."
      }
    ],
    "definitions": [
      {
        "term": "Independent Imperatives (Olivecrona)",
        "definition": "Impersonal commands of law acting directly upon human consciousness without a personal commanding will."
      }
    ],
    "ingredients": [
      "Rejection of metaphysical entities (rights, corporate souls, natural justice).",
      "Treatment of legal phenomena as observable psychological and sociological facts.",
      "Linguistic demystification of legal ceremonies and terminology."
    ],
    "exceptions": [
      "Scandinavian realism was criticized for excessive nihilism, reducing centuries of moral jurisprudence to mere word-magic."
    ],
    "examples": [
      {
        "scenario": "A borrower says 'I have a legal right to the return of my collateral.'",
        "application": "Scandinavian realists explain that no tangible physical thing called 'right' exists in space; the borrower merely experiences a psychological feeling of security because society conditions the lender to return it."
      }
    ],
    "landmarkCases": [
      {
        "case": "Synthetics & Chemicals Ltd. v. State of U.P.",
        "citation": "(1990) 1 SCC 109",
        "year": "1990",
        "bench": "7-Judge Constitution Bench (Sabyasachi Mukharji CJ)",
        "ratio": "The Supreme Court synthesized sociological and realist jurisprudence to examine whether industrial alcohol falls under state excise jurisdiction, asserting that words of a constitutional statute are living organisms reflecting real industrial economic facts rather than rigid abstract concepts.",
        "impact": "Exemplified the comparative synthesis of realism and sociological interpretation in Indian federal taxation."
      }
    ],
    "comparisonTables": [
      {
        "title": "American Realism vs Scandinavian Realism",
        "headers": ["Comparison Feature", "American Realism", "Scandinavian Realism"],
        "rows": [
          ["Geographical Origin", "United States (Holmes, Frank, Llewellyn)", "Scandinavia / Sweden & Denmark (Hägerström, Olivecrona, Ross)"],
          ["Primary Methodology", "Empirical study of court litigation and judicial behavior", "Philosophical and psychological critique of metaphysics"],
          ["View of Rules", "Rule-skepticism and fact-skepticism in trials", "Independent imperatives acting as psychological machinery"],
          ["Core Focus", "What judges do in fact in courtrooms", "How law operates as a psychological fact on the human mind"]
        ]
      }
    ],
    "diagramId": "diag-jur-schools-comparison",
    "diagramExplanation": "Grand comparative synthesis table showing the 5 major schools of jurisprudence and their core answers to 'What is Law?'.",
    "misconceptions": [
      {
        "myth": "Scandinavian Realists and American Realists belong to the same exact intellectual society.",
        "reality": "They developed independently: American Realism was practical and courtroom-oriented, while Scandinavian Realism was deeply philosophical and anti-metaphysical."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Confusing Olivecrona with Alf Ross.",
        "reality": "Olivecrona formulated 'Independent Imperatives'; Alf Ross formulated 'Directives' and emotional bindingness.",
        "rule": "Independent Imperatives = Olivecrona; Directives & Predictive validity = Alf Ross."
      }
    ],
    "flashcards": [
      {
        "id": "fc-jur-07-05",
        "front": "Who is recognized as the spiritual founder of the Scandinavian Realist School?",
        "back": "Axel Hägerström.",
        "category": "Scandinavian Realism"
      },
      {
        "id": "fc-jur-07-06",
        "front": "Who authored the famous realist text 'Law as Fact' (1939)?",
        "back": "Karl Olivecrona.",
        "category": "Olivecrona's Work"
      },
      {
        "id": "fc-jur-07-07",
        "front": "What term did Karl Olivecrona use to describe legal rules?",
        "back": "'Independent Imperatives'.",
        "category": "Olivecrona's Concepts"
      },
      {
        "id": "fc-jur-07-08",
        "front": "Which Danish jurist authored 'On Law and Justice' (1958)?",
        "back": "Alf Ross.",
        "category": "Alf Ross"
      }
    ],
    "sourceReferences": [
      {"title": "Law as Fact (2nd Ed.) — Karl Olivecrona", "url": "https://www.stevensandson.co.uk"},
      {"title": "On Law and Justice — Alf Ross (Oxford University Press)", "url": "https://global.oup.com"}
    ]
}

create_concept_file('assets/learning/data/jurisprudence/jurisprudence-concepts-part2.js', 'JURISPRUDENCE_CONCEPTS_PART2', data)
print(f"Jurisprudence Part 2 completely authored: {len(data)} topics!")
