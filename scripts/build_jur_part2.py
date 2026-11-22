import json
from concept_helpers import create_concept_file

data = {}

# -------------------------------------------------------------
# CHAPTER 5: HISTORICAL SCHOOL (Savigny & Maine)
# -------------------------------------------------------------
data["top-jur-05-01"] = {
    "topicId": "top-jur-05-01",
    "chapterId": "ch-jur-05",
    "subjectId": "law-jurisprudence",
    "title": "Friedrich Carl von Savigny & the Doctrine of Volksgeist",
    "subtitle": "Law as the Organic Reflection of the National Spirit",
    "juristRef": "Friedrich Carl von Savigny, Georg Friedrich Puchta, Thibaut",
    "learningObjective": "Master Savigny's Volksgeist doctrine, his famous opposition to Thibaut's codification proposal, the evolutionary stages of law, and the criticisms of the Historical School.",
    "introduction": "Friedrich Carl von Savigny (1779–1861) is the founder of the Historical School of Jurisprudence. Founded in Germany as a reaction against 18th-century rationalism, the French Napoleonic Code, and abstract natural law, Savigny posited that law is not made by sovereign decree, but grows organically out of the common consciousness of the people.",
    "detailedExplanation": """
<h3>1. The Thibaut-Savigny Codification Controversy (1814)</h3>
<p>Following the defeat of Napoleon, Professor A.F.J. Thibaut published a pamphlet proposing the immediate drafting of a unified Civil Code for all German states, modeled on the French Code Civil. Savigny fiercely opposed this in his celebrated tract <em>'On the Vocation of Our Age for Legislation and Jurisprudence' (Vom Beruf unserer Zeit für Gesetzgebung und Rechtswissenschaft)</em> (1814). Savigny argued that law is not an artificial construct that can be imported or drafted overnight; Germany was not yet legally or linguistically ready for codification, and premature codification would freeze and deform the organic growth of national law.</p>

<h3>2. The Concept of 'Volksgeist' (National Spirit)</h3>
<p>Savigny's central thesis is that law is an integral element of a nation's soul. Key tenets include:</p>
<ul>
  <li><strong>Organic Growth:</strong> Law develops organically like language, manners, and constitution. It possesses a national character shaped by historical traditions.</li>
  <li><strong>Law is Found, Not Made:</strong> The legislator does not invent law; he merely discovers and records that which already exists in the popular consciousness: <em>'Das Recht wird nicht gemacht, es ist und wird mit dem Volke'</em> (Law is not made; it grows with the people).</li>
  <li><strong>Three Stages of Legal Evolution:</strong>
    <ol>
      <li><strong>Early Stage:</strong> Law lives in the common consciousness of the people as unwritten custom and religious observance.</li>
      <li><strong>Mature Stage:</strong> As society grows complex, the popular consciousness is represented by a specialized class — the <strong>Jurists</strong> (lawyers and legal scholars). Jurists systematize the technical scientific principles of customary law.</li>
      <li><strong>Final Stage (Legislation):</strong> Legislation is only the final, formal recording of mature customary law, not an autonomous source of new rules.</li>
    </ol>
  </li>
</ul>

<h3>3. Critical Evaluation of Savigny</h3>
<p>Savigny's doctrine was criticized for: (a) Over-romanticizing custom and national spirit, (b) Paralyzing legislative reform by opposing deliberate social change, (c) Failing to explain how Roman Law (foreign to Germany) was widely received across Germany, and (d) Inapplicability to modern pluralistic multi-ethnic societies.</p>
""",
    "quickRevisionPoints": [
      "Savigny is the Father of the Historical School; reacted against French rationalism and natural law.",
      "Thibaut-Savigny Controversy (1814): Savigny successfully opposed premature codification of German law.",
      "Volksgeist: Law is the product of the common consciousness / national spirit of the people.",
      "Law is found, not made; develops organically like language and manners.",
      "Three stages: Popular custom -> Juristic science -> Formal legislation.",
      "Puchta: Disciple of Savigny who formalized the concept of Volksgeist."
    ],
    "provisions": [
      {
        "provision": "Volksgeist Doctrine",
        "title": "Organic Development",
        "description": "Law grows with the growth, strengthens with the strength of the people, and finally dies away as the nation loses its nationality."
      }
    ],
    "definitions": [
      {
        "term": "Volksgeist",
        "definition": "The collective consciousness, unique spirit, customs, and ethos of a particular national community."
      }
    ],
    "ingredients": [
      "Historical lineage rooted in customary community observance.",
      "Organic continuity without violent artificial legislative interruption.",
      "Recognition of jurists as the intellectual custodians of national law."
    ],
    "exceptions": [
      "Savigny could not account for the extensive 'Reception of Roman Law' in Germany, which was an alien imported system rather than native Germanic Volksgeist."
    ],
    "examples": [
      {
        "scenario": "A colonial government passes a statute completely outlawing traditional indigenous joint-family succession.",
        "application": "According to Savigny, such an alien decree will remain a dead letter because it lacks organic roots in the native Volksgeist and fails to command internal moral obedience."
      }
    ],
    "landmarkCases": [
      {
        "case": "Byram Pestonji Gariwala v. Union Bank of India",
        "citation": "(1992) 1 SCC 31",
        "year": "1992",
        "bench": "Supreme Court of India (K. Ramaswamy J)",
        "ratio": "The Supreme Court cited Savigny's Historical Jurisprudence, holding that Indian procedural law must be construed in harmony with the historical evolution of the legal profession and traditional practices of advocates settling compromises on behalf of clients.",
        "impact": "Prominent Indian Supreme Court application of Savigny's historical methodology to statutory interpretation."
      }
    ],
    "comparisonTables": [
      {
        "title": "Analytical School (Austin) vs Historical School (Savigny)",
        "headers": ["Foundational Question", "Analytical School (Austin)", "Historical School (Savigny)"],
        "rows": [
          ["Nature of Law", "Command of the political sovereign", "Found in the national spirit (Volksgeist)"],
          ["Creation of Law", "Law is consciously 'made' by legislature", "Law is organically 'found' in custom"],
          ["Primary Source", "Legislation and state sanction", "Custom and historical tradition"],
          ["Role of Custom", "Mere positive morality until court enforces", "True living law prior to any court intervention"],
          ["Attitude to Codification", "Demands immediate statutory codification", "Opposes premature codification"]
        ]
      }
    ],
    "diagramId": "diag-jur-jurists-theories",
    "diagramExplanation": "Diagram shows Savigny's three-stage evolution of law from popular custom to juristic science to codification.",
    "misconceptions": [
      {
        "myth": "Savigny completely opposed all forms of written statutes.",
        "reality": "Savigny did not oppose all legislation, but insisted that legislation must only formalize mature customary development, rather than invent novel artificial rules."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Confusing Puchta with Thibaut.",
        "reality": "Thibaut was Savigny's opponent who advocated codification; Puchta was Savigny's disciple who supported Volksgeist.",
        "rule": "Thibaut = Pro-Codification opponent; Puchta = Pro-Savigny disciple."
      }
    ],
    "flashcards": [
      {
        "id": "fc-jur-05-01",
        "front": "Who is revered as the Father of the Historical School of Jurisprudence?",
        "back": "Friedrich Carl von Savigny.",
        "category": "Historical School"
      },
      {
        "id": "fc-jur-05-02",
        "front": "What does the German concept 'Volksgeist' signify?",
        "back": "The unique spirit, consciousness, and living character of the people.",
        "category": "Savigny's Concepts"
      },
      {
        "id": "fc-jur-05-03",
        "front": "What famous 1814 publication marked Savigny's opposition to Thibaut's codification proposal?",
        "back": "On the Vocation of Our Age for Legislation and Jurisprudence (Vom Beruf).",
        "category": "Legal History"
      },
      {
        "id": "fc-jur-05-04",
        "front": "According to Savigny, what represents the second mature stage of legal evolution?",
        "back": "The jurists (legal scholars and lawyers who systematize customary principles).",
        "category": "Savigny's Stages"
      }
    ],
    "sourceReferences": [
      {"title": "On the Vocation of Our Age for Legislation and Jurisprudence — F.C. von Savigny", "url": "https://archive.org"},
      {"title": "Historical Jurisprudence — Sir Paul Vinogradoff", "url": "https://www.oxfordlawtrove.com"}
    ]
}

data["top-jur-05-02"] = {
    "topicId": "top-jur-05-02",
    "chapterId": "ch-jur-05",
    "subjectId": "law-jurisprudence",
    "title": "Sir Henry Maine: Status to Contract & Anthropological Law",
    "subtitle": "Comparative Jurisprudence, Static vs Progressive Societies, and the Movement of Law",
    "juristRef": "Sir Henry Maine",
    "learningObjective": "Master Sir Henry Maine's comparative historical methodology, the distinction between Static and Progressive societies, and his celebrated aphorism on Status to Contract.",
    "introduction": "Sir Henry Maine (1822–1888) was the pioneer of the English Historical School and Comparative Jurisprudence. Serving as Law Member in the Council of the Governor-General of India (1862–1869), Maine avoided Savigny's romantic nationalism by employing rigorous historical and anthropological comparison between Roman, English, and ancient Indian legal institutions.",
    "detailedExplanation": """
<h3>1. Stages of Legal Development in Ancient Societies</h3>
<p>In his landmark work <em>Ancient Law (1861)</em>, Maine identified four sequential developmental stages in early law:</p>
<ol>
  <li><strong>Themistes (Divine Judgments):</strong> Kings ruled by divine right; disputes were resolved by inspired ad-hoc judicial awards ('Themistes' dictated by goddess Themis). Law was personal and patriarchal.</li>
  <li><strong>Customary Law (Oligarchy of Aristocrats):</strong> Royal authority weakened; an oligarchy of priests or patricians gained a monopoly over customary unwritten traditions.</li>
  <li><strong>Era of Codification (The Codes):</strong> The invention of writing and demand for democratic transparency led to the reduction of customary rules into written Codes (e.g. Twelve Tables of Rome, Code of Manu, Laws of Solon).</li>
</ol>

<h3>2. Static vs Progressive Societies</h3>
<p>After the era of Codes, societies split into two paths:</p>
<ul>
  <li><strong>Static (Stationary) Societies:</strong> Societies that stopped developing after their ancient codes. Their legal evolution remained frozen in customary religious texts (e.g. ancient Eastern civilizations).</li>
  <li><strong>Progressive Societies:</strong> Rare, dynamic societies (Western European) that continued to modify and adapt their laws to changing social needs using three sequential instruments:
    <ol>
      <li><strong>Legal Fictions:</strong> Masking legal change by pretending the old law remains unaltered while its substance is altered (e.g. Roman praetor formulas, English ejectment action).</li>
      <li><strong>Equity:</strong> A distinct body of rules existing alongside civil law, grounded in natural justice and fairness to mitigate statutory rigor (e.g. English Court of Chancery, Roman Jus Gentium).</li>
      <li><strong>Legislation:</strong> Direct, open, and authoritative statutory enactment by sovereign bodies — the most advanced instrument of progressive law.</li>
    </ol>
  </li>
</ul>

<h3>3. The Celebrated Status to Contract Aphorism</h3>
<p>Maine formulated his most famous thesis summarizing the movement of progressive societies: <strong>'The movement of the progressive societies has hitherto been a movement from Status to Contract.'</strong></p>
<p>In early society, an individual's rights, duties, and social position were rigidly fixed at birth by membership in a patriarchal family, caste, or feudal estate (Status) — such as slave, son under patria potestas, woman under coverture. In progressive societies, family dependency dissolves, and individual freedom emerges: a person's rights and liabilities are determined by free, voluntary consensual agreements (Contract).</p>
""",
    "quickRevisionPoints": [
      "Sir Henry Maine: English Historical and Comparative Jurisprudence; author of 'Ancient Law' (1861).",
      "Stages of ancient law: Themistes (Divine commands) -> Custom (Oligarchy) -> Written Codes (12 Tables).",
      "Progressive societies adapt law via three sequential tools: Legal Fictions -> Equity -> Legislation.",
      "Most famous quote: 'The movement of the progressive societies has hitherto been a movement from Status to Contract.'",
      "Modern qualification: Rise of social welfare legislation has created a reverse trend from Contract back to Status (minimum wage, consumer protection, labor laws)."
    ],
    "provisions": [
      {
        "provision": "Maine's Historical Law",
        "title": "Movement of Progressive Societies",
        "description": "Progressive societies move from ascribed family status to voluntary individual contractual freedom."
      }
    ],
    "definitions": [
      {
        "term": "Status",
        "definition": "A legal condition where an individual's rights, duties, and capacities are fixed by law and birth, independent of his personal will."
      },
      {
        "term": "Legal Fiction",
        "definition": "Any assumption which conceals, or affects to conceal, the fact that a rule of law has undergone alteration, its letter remaining unchanged, its operation being modified."
      }
    ],
    "ingredients": [
      "Anthropological and comparative comparison of Roman, English, and Indian legal history.",
      "Identification of patriarchal kinship (Patria Potestas) as the primordial unit of early law.",
      "Evolutionary progression from collective family liability to individual autonomous responsibility."
    ],
    "exceptions": [
      "In the 20th century, the expansion of labor laws, standard form contracts, and statutory tenancy has partially reversed the trend: terms are imposed by status (employee, tenant, consumer) rather than free bargaining."
    ],
    "examples": [
      {
        "scenario": "Under ancient Roman law, a son remained under his father's patria potestas throughout the father's life, unable to own separate property or contract independently.",
        "application": "In modern progressive society, upon attaining majority (18 years), the individual gains autonomous contractual capacity, illustrating the transition from Status to Contract."
      }
    ],
    "landmarkCases": [
      {
        "case": "Central Inland Water Transport Corp. v. Brojo Nath Ganguly",
        "citation": "(1986) 3 SCC 156",
        "year": "1986",
        "bench": "Supreme Court of India (Madon J)",
        "ratio": "The Supreme Court struck down a service rule permitting termination of permanent employees on 3 months' notice, noting that the modern welfare state cannot tolerate unconscionable standard contracts where unequal bargaining power forces citizens into subordinate status, referencing modern shifts in contract jurisprudence.",
        "impact": "Classic Indian authority demonstrating the protective re-emergence of status to protect weaker parties from unconscionable contracts."
      }
    ],
    "comparisonTables": [
      {
        "title": "Maine's Three Instruments of Legal Adaptation",
        "headers": ["Instrument", "Chronological Order", "Mechanism", "Historical Example"],
        "rows": [
          ["Legal Fictions", "1st Instrument", "Pretending the law has not changed while changing its application", "Roman Praetorian Edicts, English John Doe actions"],
          ["Equity", "2nd Instrument", "Parallel body of fairness rules overriding rigid formal law", "Court of Chancery, Injunctions, Specific Performance"],
          ["Legislation", "3rd Instrument", "Direct, deliberate statutory enactment by state organs", "Acts of Parliament, Indian Contract Act 1872"]
        ]
      }
    ],
    "diagramId": "diag-jur-jurists-theories",
    "diagramExplanation": "Diagram tracing Maine's evolutionary pathway: Themistes -> Customs -> Codes -> Legal Fictions -> Equity -> Legislation -> Status to Contract.",
    "misconceptions": [
      {
        "myth": "Maine asserted that all societies throughout world history move from status to contract.",
        "reality": "Maine explicitly restricted this movement to 'progressive societies' (Western Europe), noting that the vast majority of human societies remained static."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Confusing the order of Maine's three agencies of legal development.",
        "reality": "The strict chronological order is: (1) Legal Fictions, (2) Equity, (3) Legislation.",
        "rule": "Fictions -> Equity -> Legislation."
      }
    ],
    "flashcards": [
      {
        "id": "fc-jur-05-05",
        "front": "Who authored the monumental 1861 jurisprudential treatise 'Ancient Law'?",
        "back": "Sir Henry Maine.",
        "category": "Historical Jurisprudence"
      },
      {
        "id": "fc-jur-05-06",
        "front": "What famous dictum did Sir Henry Maine formulate regarding progressive societies?",
        "back": "'The movement of the progressive societies has hitherto been a movement from Status to Contract.'",
        "category": "Maine's Dictum"
      },
      {
        "id": "fc-jur-05-07",
        "front": "What are the three agencies by which progressive societies adapt law according to Maine?",
        "back": "Legal Fictions, Equity, and Legislation (in that chronological order).",
        "category": "Legal Adaptation"
      },
      {
        "id": "fc-jur-05-08",
        "front": "What were 'Themistes' in ancient Greek legal evolution?",
        "back": "Divinely inspired judicial awards delivered by kings as patriarchal arbiters.",
        "category": "Early Law"
      }
    ],
    "sourceReferences": [
      {"title": "Ancient Law: Its Connection with the Early History of Society — Sir Henry Maine", "url": "https://www.gutenberg.org"},
      {"title": "Lectures on the Early History of Institutions — Sir Henry Maine", "url": "https://archive.org"}
    ]
}

create_concept_file('assets/learning/data/jurisprudence/jurisprudence-concepts-part2.js', 'JURISPRUDENCE_CONCEPTS_PART2', data)
print(f"Jurisprudence Part 2 authored with {len(data)} topics!")
