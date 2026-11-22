import json
import os
from concept_helpers import create_concept_file

data = {
  "top-jur-01-01": {
    "topicId": "top-jur-01-01",
    "chapterId": "ch-jur-01",
    "subjectId": "law-jurisprudence",
    "title": "Meaning, Nature and Scope of Jurisprudence",
    "subtitle": "Jurisprudence as the Science and Grammar of Law",
    "juristRef": "Ulpian, Salmond, Austin, Holland, Allen",
    "learningObjective": "Master the classical and modern definitions of jurisprudence, distinguishing between formal science, practical statecraft, and substantive legal theory for judicial examinations.",
    "introduction": "Jurisprudence is derived from the Latin term 'Jurisprudentia' (Juris = law, Prudentia = knowledge or skill). It signifies the knowledge of law and its application. Unlike substantive statutes which prescribe specific rules of conduct, jurisprudence investigates the philosophical foundations, essential nature, structural taxonomy, and underlying principles of legal systems.",
    "detailedExplanation": """
<h3>1. Etymological & Classical Roots</h3>
<p>In Ancient Rome, Ulpian defined jurisprudence broadly as <em>'Divinarum atque humanarum rerum notitia, justi atque injusti scientia'</em> — the knowledge of things divine and human, the science of the just and the unjust. While Cicero linked it to the philosophical search for true law, modern jurisprudence emerged as an independent academic discipline through the systematic work of Jeremy Bentham and John Austin.</p>

<h3>2. Leading Juristic Definitions</h3>
<ul>
  <li><strong>John Austin:</strong> Defined jurisprudence as the <em>'Philosophy of Positive Law'</em>. Law is the command of the political sovereign, and jurisprudence analyzes positive law irrespective of its goodness or badness. Austin bifurcated jurisprudence into <strong>General Jurisprudence</strong> (subjects and concepts common to all mature legal systems) and <strong>Particular Jurisprudence</strong> (science of any actual system of positive law in a specific country).</li>
  <li><strong>John Salmond:</strong> Defined jurisprudence as the <em>'Science of First Principles of the Civil Law'</em>. By 'civil law', Salmond meant the law of the state applied by judicial courts. He divided jurisprudence into: (a) Expository (contents of a legal system as it exists), (b) Historical (evolution and historical origins), and (c) Critical or Science of Legislation (law as it ought to be).</li>
  <li><strong>Sir Thomas Erskine Holland:</strong> Defined jurisprudence as the <em>'Formal Science of Positive Law'</em>. By 'formal', Holland meant that jurisprudence deals not with the substantive material rules themselves, but with the fundamental relations and structural forms which are common across legal systems, comparing it to grammar in language.</li>
  <li><strong>Julius Stone:</strong> Defined jurisprudence as <em>'The lawyer's extraversion'</em> — a lawyer examining the precepts, ideals and techniques of the law in the light of disciplines outside law, such as history, economics, and sociology.</li>
  <li><strong>Roscoe Pound:</strong> Characterized jurisprudence as the <em>'Science of Social Engineering'</em>, treating law as a dynamic instrument to balance competing interests in human society.</li>
</ul>

<h3>3. Scope, Utility and Practical Value</h3>
<p>Jurisprudence is often described as the 'eye of the law' or the 'grammar of law'. It equips the judge and advocate with conceptual tools to resolve ambiguities in statutory language, interpret constitutional doctrines, fill legislative gaps through judicial reasoning, and assess the broader social impact of judicial decisions.</p>
""",
    "quickRevisionPoints": [
      "Jurisprudence = Juris (law) + Prudentia (knowledge/skill); origins in Roman law (Ulpian).",
      "Austin: 'Philosophy of Positive Law' — split into General vs Particular Jurisprudence.",
      "Salmond: 'Science of the First Principles of the Civil Law' (the law of the courts).",
      "Holland: 'Formal Science of Positive Law' — compares jurisprudence to grammar.",
      "Julius Stone: 'The lawyer’s extraversion' — examining law through outside disciplines.",
      "Roscoe Pound: Science of Social Engineering; functional balancing of human claims."
    ],
    "provisions": [
      {
        "provision": "Jurisprudence Taxonomy",
        "title": "Science of Positive Law",
        "description": "Systematic study of the fundamental principles, doctrines, and concepts underlying legal systems."
      },
      {
        "provision": "Holland's Formulation",
        "title": "Formal Science",
        "description": "Studies the structural form, categories, and legal relations rather than detailed material rules."
      }
    ],
    "definitions": [
      {
        "term": "General Jurisprudence (Austin)",
        "definition": "The science of those principles, notions, and distinctions which are common to the various systems of mature positive law."
      },
      {
        "term": "Formal Science (Holland)",
        "definition": "A science that deals with the human relations which are governed by legal rules rather than with the material rules themselves."
      }
    ],
    "ingredients": [
      "Analysis of core legal concepts: rights, duties, personality, property, ownership, possession, and liability.",
      "Examination of the relationship between law, sovereign power, morality, and justice.",
      "Study of the sources from which legal rules originate and derive binding validity.",
      "Investigation of the operational techniques, logic, and interpretation employed by courts."
    ],
    "exceptions": [
      "Jurisprudence does not provide concrete statutory answers or codified penalties for specific offences.",
      "Austin's division between General and Particular jurisprudence was criticized by Salmond and Buckland, who argued that jurisprudence cannot be strictly partitioned because principles remain universal."
    ],
    "examples": [
      {
        "scenario": "A court must decide whether an artificial intelligence system or an ancient temple deity can own property and file a suit.",
        "application": "Substantive procedural codes define who may sue, but the fundamental question of whether non-human entities possess 'legal personality' is resolved entirely by jurisprudential theories of corporate and juristic personality."
      }
    ],
    "landmarkCases": [
      {
        "case": "Kesavananda Bharati v. State of Kerala",
        "citation": "(1973) 4 SCC 225",
        "year": "1973",
        "bench": "13-Judge Bench (Sikri CJ, Hegde, Mukherjea, Shelat, Grover, Ray, Reddy, Palekar, Khanna, Mathew, Beg, Dwivedi, Chandrachud JJ)",
        "ratio": "The Supreme Court utilized natural law principles, German constitutional jurisprudence, and Salmond's first principles to establish the Basic Structure Doctrine, demonstrating that judicial power operates on foundational jurisprudential axioms above ordinary legislative authority.",
        "impact": "Directly links jurisprudential concept of supra-constitutional limits to Indian constitutional adjudication."
      }
    ],
    "comparisonTables": [
      {
        "title": "Comparison of Classical Juristic Definitions",
        "headers": ["Jurist", "Exact Definitional Phrase", "Key Focus", "Core Metaphor"],
        "rows": [
          ["John Austin", "Philosophy of Positive Law", "Positive law (command backed by sanction)", "Sovereignty & Sanction"],
          ["John Salmond", "Science of First Principles of Civil Law", "Law applied by courts of the state", "First Principles of Justice"],
          ["T.E. Holland", "Formal Science of Positive Law", "Form and structure, not material substance", "Grammar of Law"],
          ["Julius Stone", "Lawyer's Extraversion", "Integration of law with sociology and economics", "Looking outward"],
          ["Roscoe Pound", "Science of Social Engineering", "Functional balancing of competing social claims", "Engineering and Efficiency"]
        ]
      }
    ],
    "diagramId": "diag-jur-schools-comparison",
    "diagramExplanation": "Diagram maps the evolution of jurisprudence from formal positivist science to functional social engineering.",
    "misconceptions": [
      {
        "myth": "Jurisprudence is identical to statutory interpretation.",
        "reality": "Statutory interpretation is a judicial technique for construing specific statutory language, whereas jurisprudence investigates the conceptual nature of law, authority, and rights as a whole."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Confusing Holland's 'Formal Science' with Austin's 'Philosophy of Positive Law'.",
        "reality": "Holland called it a 'Formal Science', while Austin called it 'Philosophy of Positive Law'.",
        "rule": "Holland = Formal Science; Austin = Philosophy of Positive Law; Salmond = Science of First Principles."
      }
    ],
    "flashcards": [
      {
        "id": "fc-jur-01-01",
        "front": "Who defined jurisprudence as the 'Formal Science of Positive Law'?",
        "back": "Sir Thomas Erskine Holland.",
        "category": "Juristic Definitions"
      },
      {
        "id": "fc-jur-01-02",
        "front": "What did John Austin mean by 'General Jurisprudence'?",
        "back": "The science concerned with subjects and distinctions common to all mature systems of positive law.",
        "category": "Analytical School"
      },
      {
        "id": "fc-jur-01-03",
        "front": "Who famously termed jurisprudence as 'the lawyer's extraversion'?",
        "back": "Julius Stone.",
        "category": "Modern Jurisprudence"
      },
      {
        "id": "fc-jur-01-04",
        "front": "How did Salmond categorize the study of jurisprudence?",
        "back": "Expository (law as it is), Historical (evolution of law), and Critical/Science of Legislation (law as it ought to be).",
        "category": "Salmond's Classification"
      }
    ],
    "sourceReferences": [
      {"title": "Salmond on Jurisprudence (12th Ed. by P.J. Fitzgerald)", "url": "https://www.sweetandmaxwell.co.uk"},
      {"title": "The Province of Jurisprudence Determined — John Austin", "url": "https://www.cambridge.org"}
    ]
  },

  "top-jur-01-02": {
    "topicId": "top-jur-01-02",
    "chapterId": "ch-jur-01",
    "subjectId": "law-jurisprudence",
    "title": "Law, Morality and Justice (Hart-Fuller & Hart-Devlin Debates)",
    "subtitle": "The Separation Thesis and the Limits of Legal Moralism",
    "juristRef": "H.L.A. Hart, Lon L. Fuller, Lord Devlin, John Stuart Mill",
    "learningObjective": "Analyse the conceptual tension between legal positivism and moral philosophy, evaluating the Hart-Fuller debate on Nazi law and the Hart-Devlin debate on legal enforcement of public morality.",
    "introduction": "The relationship between law and morality constitutes the central dividing line in legal philosophy. Legal positivists insist on the 'Separation Thesis' (that the legal validity of a rule does not depend upon its moral merit), whereas natural law theorists assert that unjust rules lack the authentic quality of law.",
    "detailedExplanation": """
<h3>1. The Positivist 'Separation Thesis'</h3>
<p>Legal Positivism, championing the separation thesis, asserts that <em>'the existence of law is one thing; its merit or demerit is another'</em> (Austin). A law duly enacted by competent authority is legally binding, even if profoundly immoral. Positivists do not deny that moral values influence lawmaking, but deny that moral rectitude is a necessary condition for legal validity.</p>

<h3>2. The Hart-Fuller Debate (1958)</h3>
<p>Triggered by the problem of the 'Grudge Informers' in post-WWII Nazi Germany, where citizens denounced personal enemies under Nazi statutes:</p>
<ul>
  <li><strong>H.L.A. Hart's Positivist Stance:</strong> Hart argued that Nazi laws, however abominable, were valid positive laws at the time of their enactment. To hold informers liable retrospectively by pretending Nazi statutes were never law is dishonest and undermines the rule of law. If society decides to punish them, it must pass an explicit, frank retrospective statute, openly acknowledging that it sacrifices one legal value (non-retroactivity) for another (moral retribution).</li>
  <li><strong>Lon L. Fuller's Natural Law Response:</strong> Fuller argued that law is a purposeful enterprise subjected to an <strong>'Internal Morality'</strong> of 8 procedural requirements (generality, promulgation, non-retroactivity, clarity, non-contradiction, possibility of compliance, constancy, and congruence between official action and declared rule). Total failure in these 8 principles results not in bad law, but in something that is not law at all. The Nazi legal order was a monstrous perversion lacking internal morality.</li>
</ul>

<h3>3. The Hart-Devlin Debate (1959–1965)</h3>
<p>Sparked by the UK Wolfenden Committee Report (1957) recommending decriminalization of private homosexual acts between consenting adults:</p>
<ul>
  <li><strong>Lord Devlin's Legal Moralism:</strong> Society is bound together by a shared common morality. Destruction of this moral fabric threatens societal cohesion just as treason does. Therefore, society has a prima facie right to use criminal law to preserve its moral integrity whenever an act generates genuine disgust and indignation in the reasonable man on the Clapham omnibus.</li>
  <li><strong>H.L.A. Hart's Millian Liberalism:</strong> Grounded in J.S. Mill's 'Harm Principle' — the only justification for state coercion over an individual against his will is to prevent harm to others. Mere moral distress, disgust, or divergence from public sentiment without tangible physical or economic harm cannot justify criminal sanctions.</li>
</ul>
""",
    "quickRevisionPoints": [
      "Separation Thesis: 'The existence of law is one thing; its merit or demerit is another' (Austin/Hart).",
      "Hart-Fuller Debate (1958 Harvard Law Review): Focused on retrospective punishment of Nazi grudge informers.",
      "Fuller's Internal Morality: 8 procedural desiderata; complete failure destroys legal character.",
      "Hart-Devlin Debate: Arose from Wolfenden Report on consensual adult private conduct.",
      "Devlin: Society has right to enforce moral cohesion against disintegration.",
      "Hart: Criminal law cannot enforce morality without tangible harm to others (Harm Principle)."
    ],
    "provisions": [
      {
        "provision": "Wolfenden Report 1957",
        "title": "Private Morality Doctrine",
        "description": "Criminal law must preserve public order and decency, but not intervene in private moral lives of citizens."
      },
      {
        "provision": "Fuller's 8 Desiderata",
        "title": "Inner Morality of Law",
        "description": "Procedural virtues required for a legal system to command genuine rational obedience."
      }
    ],
    "definitions": [
      {
        "term": "Separation Thesis",
        "definition": "The positivist doctrine that there is no necessary conceptual connection between law and morality."
      },
      {
        "term": "Harm Principle (J.S. Mill)",
        "definition": "The sole ground for state interference with individual liberty is self-protection to prevent harm to others."
      }
    ],
    "ingredients": [
      "Distinction between law (state-enforced, external sanction) and morality (conscience, internal sanction).",
      "Positivist recognition of formal legal validity based on authoritative enactment sources.",
      "Naturalist insistence that gross moral bankruptcy negates legal obligation."
    ],
    "exceptions": [
      "Inclusive Legal Positivism (Hart): Moral principles may become legal criteria if the legal system's Rule of Recognition incorporates them (e.g. Fundamental Rights under Indian Constitution Art. 14, 21)."
    ],
    "examples": [
      {
        "scenario": "Two consenting adults engage in private acts not harming any third party, but condemned by orthodox societal majorities.",
        "application": "Under Devlin's view, the state may prohibit it to safeguard societal moral fabric; under Hart's view and Indian Supreme Court jurisprudence (Navtej Singh Johar), private consensual morality cannot be criminalized without tangible public harm."
      }
    ],
    "landmarkCases": [
      {
        "case": "Navtej Singh Johar v. Union of India",
        "citation": "(2018) 10 SCC 1",
        "year": "2018",
        "bench": "5-Judge Constitution Bench (Dipak Misra CJ, Nariman, Khanwilkar, Chandrachud, Malhotra JJ)",
        "ratio": "Constitutional morality overrides majoritarian public morality. Criminalization of consensual adult private acts under Section 377 IPC violates fundamental rights to equality, liberty, dignity, and privacy under Articles 14, 19, and 21.",
        "impact": "Decisive Indian constitutional precedent affirming Hart's position that majoritarian moral indignation cannot dictate criminal liability."
      }
    ],
    "comparisonTables": [
      {
        "title": "Hart vs Fuller & Hart vs Devlin Comparative Matrix",
        "headers": ["Debate Dimension", "H.L.A. Hart", "Opposing Scholar", "Core Theoretical Climax"],
        "rows": [
          ["Hart-Fuller (Nazi Law)", "Law was valid positive law; use candid retrospective statute", "Lon Fuller (Inner Morality of Law)", "Nazi perversion failed 8 procedural desiderata = Non-law"],
          ["Hart-Devlin (Enforcing Morals)", "Mill's Harm Principle; no punishment for harmless private acts", "Lord Devlin (Social Cohesion)", "Society has right to enforce moral fabric against disintegration"]
        ]
      }
    ],
    "diagramId": "diag-jur-law-morality",
    "diagramExplanation": "Venn diagram showing the overlapping spheres of legal sanctions, moral obligations, and constitutional rights.",
    "misconceptions": [
      {
        "myth": "Legal positivists believe law must be immoral or that judges should disregard morality.",
        "reality": "Positivists acknowledge morality's vital role in lawmaking, but argue that identifying whether a law exists is logically distinct from judging its moral goodness."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing Fuller advocated classical divine natural law.",
        "reality": "Fuller developed a 'Procedural Natural Law' (Internal Morality) based on rational procedural requirements, not Catholic divine theology.",
        "rule": "Fuller = Procedural/Internal Morality; Aquinas = Substantive Divine Natural Law."
      }
    ],
    "flashcards": [
      {
        "id": "fc-jur-01-05",
        "front": "What was the central factual catalyst of the Hart-Fuller Debate?",
        "back": "The legal validity of Nazi statutes and the prosecution of post-war 'grudge informers'.",
        "category": "Legal Philosophy"
      },
      {
        "id": "fc-jur-01-06",
        "front": "How many procedural desiderata constitute Lon Fuller's 'Inner Morality of Law'?",
        "back": "Eight (Generality, Promulgation, Non-retroactivity, Clarity, Non-contradiction, Possibility of compliance, Constancy, and Congruence).",
        "category": "Natural Law"
      },
      {
        "id": "fc-jur-01-07",
        "front": "Which famous official report sparked the Hart-Devlin Debate?",
        "back": "The Wolfenden Committee Report on Homosexual Offences and Prostitution (1957).",
        "category": "Law & Morality"
      },
      {
        "id": "fc-jur-01-08",
        "front": "Which Supreme Court decision cemented 'Constitutional Morality' over majoritarian public morality in India?",
        "back": "Navtej Singh Johar v. Union of India (2018) 10 SCC 1.",
        "category": "Indian Jurisprudence"
      }
    ],
    "sourceReferences": [
      {"title": "The Morality of Law — Lon L. Fuller (Yale University Press)", "url": "https://yalebooks.yale.edu"},
      {"title": "The Enforcement of Morals — Patrick Devlin (Oxford University Press)", "url": "https://global.oup.com"}
    ]
  },

  "top-jur-01-03": {
    "topicId": "top-jur-01-03",
    "chapterId": "ch-jur-01",
    "subjectId": "law-jurisprudence",
    "title": "Classifications of Law & General vs Particular Jurisprudence",
    "subtitle": "Substantive, Procedural, Public, Private, Municipal & International Taxonomy",
    "juristRef": "Salmond, Austin, Holland, Bentham",
    "learningObjective": "Master the taxonomy of legal systems, distinguishing between substantive and adjective law, public and private law, and civil versus criminal law.",
    "introduction": "Law can be classified into distinct categories based on its subject matter, source, territorial application, and functional operation. A clear grasp of legal classification is vital for procedural litigation and jurisdictional analysis.",
    "detailedExplanation": """
<h3>1. Substantive Law vs Adjective (Procedural) Law</h3>
<ul>
  <li><strong>Substantive Law:</strong> Defines the nature, extent, and boundaries of legal rights, duties, liabilities, and obligations (e.g., Bharatiya Nyaya Sanhita, Indian Contract Act, Transfer of Property Act). Salmond defined it as that which relates to the ends which the administration of justice contemplates.</li>
  <li><strong>Adjective (Procedural) Law:</strong> Deals with the machinery, procedure, remedies, evidence, and enforcement of substantive rights through the courts (e.g., Bharatiya Nagarik Suraksha Sanhita, Code of Civil Procedure, Bharatiya Sakshya Adhiniyam). Substantive rights cannot be enforced without adjective avenues.</li>
</ul>

<h3>2. Public Law vs Private Law</h3>
<ul>
  <li><strong>Public Law:</strong> Regulates the structure, powers, and duties of sovereign state authorities and their relations with citizens (Constitutional Law, Administrative Law, Criminal Law). In public law disputes, the state represents the collective interest of society.</li>
  <li><strong>Private Law (Civil Law):</strong> Governs relations between private individuals or corporate entities where the state acts merely as an impartial adjudicator (Contract, Torts, Property, Family Law).</li>
</ul>

<h3>3. Municipal (Domestic) Law vs International Law</h3>
<ul>
  <li><strong>Municipal Law:</strong> The internal law of a sovereign state governing persons within its territorial jurisdiction, enforced by domestic police and courts.</li>
  <li><strong>International Law:</strong> Body of customary rules, treaties, and general principles of law governing relations between sovereign nation states and international bodies. John Austin famously denied international law the status of 'true law', calling it 'positive international morality' because it lacked an overarching sovereign command and physical sanction.</li>
</ul>
""",
    "quickRevisionPoints": [
      "Substantive law defines rights/duties (IPC, Contract, TPA); Adjective law governs procedural machinery (CrPC, CPC, BSA).",
      "Public law regulates state organs and citizen-state relations (Constitutional, Criminal, Administrative).",
      "Private law governs interpersonal rights and duties (Contracts, Torts, Property).",
      "Austin called International Law 'Positive International Morality' due to absence of sovereign command/sanction.",
      "Salmond: Law is the body of principles recognized and applied by the state in the administration of justice."
    ],
    "provisions": [
      {
        "provision": "Taxonomy of Municipal Law",
        "title": "Substantive vs Procedural",
        "description": "Substantive rules determine rights; procedural rules determine the mechanism of remedy."
      }
    ],
    "definitions": [
      {
        "term": "Substantive Law",
        "definition": "The branch of law that defines and regulates rights and duties, creating actionable legal causes."
      },
      {
        "term": "Adjective Law",
        "definition": "The branch of law that prescribes the method, procedure, and evidentiary rules for enforcing rights."
      }
    ],
    "ingredients": [
      "Identification of the subject matter regulated (rights vs remedies).",
      "Determination of party status (state vs citizen, or private citizen vs private citizen).",
      "Territorial scope (internal municipal boundary vs international domain)."
    ],
    "exceptions": [
      "Certain statutory provisions combine substantive and procedural aspects (e.g., limitation bars the remedy but does not extinguish the debt; Section 145 CrPC regulates urgent possession disputes)."
    ],
    "examples": [
      {
        "scenario": "A builder breaches an agreement to construct an apartment, and the buyer seeks specific performance.",
        "application": "The right to demand performance arises from the substantive law (Contract Act / Specific Relief Act), while the filing of the plaint, issuance of summons, and execution of the decree are governed by adjective law (CPC)."
      }
    ],
    "landmarkCases": [
      {
        "case": "Thirumalai Chemicals Ltd. v. Union of India",
        "citation": "(2011) 6 SCC 739",
        "year": "2011",
        "bench": "Supreme Court of India (K.S. Radhakrishnan J)",
        "ratio": "Substantive law creates and defines rights and obligations and is ordinarily prospective unless expressly made retrospective; procedural law is concerned with the mode of proceeding and is generally retrospective in application.",
        "impact": "Classic authority on the distinction and retrospective application of procedural vs substantive law."
      }
    ],
    "comparisonTables": [
      {
        "title": "Substantive Law vs Adjective (Procedural) Law",
        "headers": ["Comparison Parameter", "Substantive Law", "Adjective / Procedural Law"],
        "rows": [
          ["Primary Purpose", "Creates, defines, and limits rights and liabilities", "Prescribes the mechanism, procedure, and remedy"],
          ["Retrospective Effect", "Presumed to be prospective unless clear legislative intent", "Generally retrospective in operation"],
          ["Core Statutes", "BNS 2023, Contract Act 1872, TPA 1882", "BNSS 2023, CPC 1908, BSA 2023"],
          ["Salmond's Metaphor", "The end which the administration of justice contemplates", "The instrument and means to achieve that end"]
        ]
      }
    ],
    "diagramId": "diag-jur-sources-of-law",
    "diagramExplanation": "Classification diagram showing the structural division of legal systems into substantive, procedural, public, and private spheres.",
    "misconceptions": [
      {
        "myth": "Procedural law is merely secondary and has no real power over substantive rights.",
        "reality": "Procedural bars (e.g., limitation period, res judicata) can completely extinguish or render unenforceable an otherwise valid substantive right."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Assuming the Law of Limitation is substantive law.",
        "reality": "Law of limitation is adjective (procedural) law; it bars the court remedy, not the underlying right.",
        "rule": "Limitation = Procedural (lex fori); extinguishes remedy, leaves substantive right intact."
      }
    ],
    "flashcards": [
      {
        "id": "fc-jur-01-09",
        "front": "Why did John Austin classify International Law as 'Positive International Morality'?",
        "back": "Because it lacked a determinate political sovereign and an organized centralized coercive sanction.",
        "category": "Classification of Law"
      },
      {
        "id": "fc-jur-01-10",
        "front": "What is the general presumption regarding retrospective application of procedural vs substantive law?",
        "back": "Substantive law is presumed prospective; procedural law is presumed retrospective.",
        "category": "Legal Principles"
      },
      {
        "id": "fc-jur-01-11",
        "front": "Is the Indian Law of Evidence substantive or procedural law?",
        "back": "Procedural / Adjective law (Lex Fori — law of the forum).",
        "category": "Statutory Classification"
      },
      {
        "id": "fc-jur-01-12",
        "front": "Who defined civil law as 'the law of the State or of the land, the law of lawyers and the law-courts'?",
        "back": "Sir John Salmond.",
        "category": "Salmond's Theory"
      }
    ],
    "sourceReferences": [
      {"title": "Salmond on Jurisprudence — Sweet & Maxwell", "url": "https://www.sweetandmaxwell.co.uk"},
      {"title": "Holland's Elements of Jurisprudence — Oxford Clarendon Press", "url": "https://archive.org"}
    ]
  }
}

create_concept_file('assets/learning/data/jurisprudence/jurisprudence-concepts-part1.js', 'JURISPRUDENCE_CONCEPTS_PART1', data)
print("Part 1 base written successfully.")
