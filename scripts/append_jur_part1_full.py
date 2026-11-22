import json
import os
from concept_helpers import create_concept_file

# We load existing top-jur-01-01 to 01-03
from build_jur_part1 import data as full_data

# Ch 2: Sources
full_data["top-jur-02-01"] = {
    "topicId": "top-jur-02-01",
    "chapterId": "ch-jur-02",
    "subjectId": "law-jurisprudence",
    "title": "Custom as a Source of Law: Essentials & Theories",
    "subtitle": "Immemorial Antiquity, Continuity, Reasonableness & Opinio Juris",
    "juristRef": "Savigny, Austin, Salmond, Allen, Blackstone",
    "learningObjective": "Analyze the conditions necessary for a custom to attain the force of law, comparing Historical and Analytical views on customary legal authority.",
    "introduction": "Custom is the earliest and most natural source of law. It comprises unwritten usages, habits, and practices observed by a community over long generations. In primitive societies before formal legislatures or courts, customary observances formed the primary social and legal order.",
    "detailedExplanation": """
<h3>1. Requisites of a Valid Legal Custom</h3>
<p>In English common law and Indian jurisprudence, a custom must fulfill strict criteria to be legally binding:</p>
<ul>
  <li><strong>Immemorial Antiquity:</strong> Under English law, antiquity is fixed to the year 1189 AD (accession of Richard I). In Indian law, antiquity does not require 1189 AD, but must be demonstrated to be 'ancient and from time whereof the memory of man runneth not to the contrary' (Gokul Chand v. Parvin Kumari).</li>
  <li><strong>Continuity:</strong> The usage must have been practiced without interruption from its inception. An interruption in the right to observe the custom destroys it.</li>
  <li><strong>Peaceable &amp; Open Enjoyment (Nec vi, nec clam, nec precario):</strong> It must be enjoyed openly, peacefully, and without contest or permission.</li>
  <li><strong>Reasonableness:</strong> Must not be opposed to justice, public policy, or common sense. A wicked, malicious, or oppressive practice cannot be a valid custom.</li>
  <li><strong>Conformity with Statute Law:</strong> A custom cannot override or contradict an explicit parliamentary statute unless expressly preserved by statute.</li>
  <li><strong>Opinio Juris Sive Necessitatis:</strong> The conviction by the people that observance is legally obligatory, not merely a voluntary social courtesy.</li>
</ul>

<h3>2. Analytical vs Historical Theories of Custom</h3>
<ul>
  <li><strong>Analytical Theory (Austin &amp; Holland):</strong> Custom is not law until it receives formal recognition from the sovereign legislature or judicial decree. Prior to judicial adoption, custom is merely 'positive morality'. Austin: <em>'A custom becomes law when it is adopted as such by the courts and enforced with state sanction.'</em></li>
  <li><strong>Historical Theory (Savigny &amp; Puchta):</strong> Custom is law per se. It embodies the true inner consciousness (Volksgeist) of the people. Courts do not create its legal validity; judicial recognition merely declares and formalizes the pre-existing living law.</li>
</ul>
""",
    "quickRevisionPoints": [
      "Custom is the oldest source of law; reflects long-standing societal practice.",
      "Requisites: Immemorial antiquity, continuous observance, reasonableness, peaceable enjoyment, conformity with statute, opinio juris.",
      "English law antiquity threshold: 1189 AD (Richard I accession); Indian law: ancient & continuous living memory.",
      "Austin (Analytical): Custom is not law until recognized by court or statute (Positive Morality).",
      "Savigny (Historical): Custom is law per se as the direct expression of the Volksgeist."
    ],
    "provisions": [
      {
        "provision": "Custom Validity Test",
        "title": "Blackstone's Criteria",
        "description": "Antiquity, continuity, peaceable enjoyment, certainty, consistency, and reasonableness."
      }
    ],
    "definitions": [
      {
        "term": "Opinio Juris Sive Necessitatis",
        "definition": "The psychological belief of participants that their customary practice is an obligatory legal duty, not a mere social habit."
      }
    ],
    "ingredients": [
      "Antiquity: ancient lineage proven by historical memory.",
      "Continuity: uninterrupted compliance over generations.",
      "Reasonableness: compatibility with contemporary public welfare and morality.",
      "Certainty: definite and unambiguous in scope and application."
    ],
    "exceptions": [
      "No custom can prevail against the clear, express words of an enacted legislative statute.",
      "Customs contrary to public policy or constitutional morality are void (e.g. Sati, Devadasi system)."
    ],
    "examples": [
      {
        "scenario": "A community claims a customary right to marry within prohibited degrees of sapinda relationship under Hindu Marriage Act.",
        "application": "Under Section 5(iv) of the Hindu Marriage Act 1955, the custom is valid only if proven ancient, continuous, reasonable, and not opposed to public policy."
      }
    ],
    "landmarkCases": [
      {
        "case": "Gokul Chand v. Parvin Kumari",
        "citation": "AIR 1952 SC 231",
        "year": "1952",
        "bench": "Supreme Court of India (Mehr Chand Mahajan J)",
        "ratio": "A custom must be proved to be ancient, continuous, and certain by clear and unambiguous evidence before it can be allowed to override general statutory or personal law.",
        "impact": "Leading Indian precedent establishing the rigorous evidentiary burden required to establish customary exceptions."
      }
    ],
    "comparisonTables": [
      {
        "title": "Analytical vs Historical View of Custom",
        "headers": ["Juridical Aspect", "Analytical View (Austin)", "Historical View (Savigny)"],
        "rows": [
          ["Status Before Court Ruling", "Mere positive morality; not law", "Already genuine living law"],
          ["Role of Judicial Decision", "Creative: Court makes it law", "Declaratory: Court merely recognizes pre-existing law"],
          ["Source of Binding Force", "Coercive sanction of the sovereign state", "Inner conviction and consciousness of the people (Volksgeist)"]
        ]
      }
    ],
    "diagramId": "diag-jur-sources-of-law",
    "diagramExplanation": "Diagram maps the legal transformation of social habits into binding legal customs via judicial and statutory recognition.",
    "misconceptions": [
      {
        "myth": "Any usage followed for 20 years automatically becomes a legal custom.",
        "reality": "20 years may create an easement by prescription, but a customary law requires immemorial antiquity and continuous community acceptance."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing English 1189 AD cut-off strictly applies in Indian courts.",
        "reality": "In India, 1189 AD is not the test; the custom must simply be proved ancient, certain, and continuous beyond living memory.",
        "rule": "1189 AD = English Common Law; Ancient & Continuous = Indian Law."
      }
    ],
    "flashcards": [
      {
        "id": "fc-jur-02-01",
        "front": "What year is fixed by English law as the beginning of 'legal memory' for immemorial custom?",
        "back": "1189 AD (1st year of the reign of King Richard I).",
        "category": "Custom Requisites"
      },
      {
        "id": "fc-jur-02-02",
        "front": "What does the Latin maxim 'Opinio juris sive necessitatis' signify?",
        "back": "Opinion as to law or necessity — the belief that an action was carried out as a legal obligation.",
        "category": "Customary Law"
      },
      {
        "id": "fc-jur-02-03",
        "front": "Who stated that custom is not law until adopted by courts and enforced with state sanction?",
        "back": "John Austin (Analytical School).",
        "category": "Juristic Theories"
      },
      {
        "id": "fc-jur-02-04",
        "front": "Can a custom validly contradict an express legislative statute in India?",
        "back": "No, an express statute prevails over custom unless the statute expressly saves the custom.",
        "category": "Hierarchy of Sources"
      }
    ],
    "sourceReferences": [
      {"title": "Law in the Making — Sir Carleton Kemp Allen", "url": "https://global.oup.com"},
      {"title": "Blackstone's Commentaries on the Laws of England", "url": "https://avalon.law.yale.edu"}
    ]
}

full_data["top-jur-02-02"] = {
    "topicId": "top-jur-02-02",
    "chapterId": "ch-jur-02",
    "subjectId": "law-jurisprudence",
    "title": "Judicial Precedent, Stare Decisis & Ratio Decidendi",
    "subtitle": "Binding Precedent, Obiter Dicta, and the Mechanics of Judicial Lawmaking",
    "juristRef": "Salmond, Goodhart, Wambaugh, Cross, Austin",
    "learningObjective": "Distinguish between Ratio Decidendi and Obiter Dicta, master Wambaugh's Inversion Test and Goodhart's Material Facts Test, and examine Article 141 of the Indian Constitution.",
    "introduction": "A judicial precedent is a judgment of a superior court cited as an authority for deciding a similar legal question in subsequent cases. The doctrine of precedent is founded on the principle of Stare Decisis (stare decisis et non quieta movere — to stand by decisions and not disturb settled points), ensuring certainty, predictability, and uniform justice.",
    "detailedExplanation": """
<h3>1. Structure of a Judicial Precedent</h3>
<p>Every judicial judgment contains three distinct components:</p>
<ul>
  <li><strong>Ratio Decidendi:</strong> The underlying legal principle or reason essential for the decision. It is the binding portion of the precedent. Salmond defined it as <em>'the legal principle which formulates the essential ground of the judicial decision'</em>.</li>
  <li><strong>Obiter Dicta:</strong> Things said by the way — observations, analogies, or statements of law not strictly necessary for resolving the dispute between the parties. They carry persuasive authority but are not legally binding.</li>
  <li><strong>Operative Order:</strong> The specific decree or order binding only upon the actual litigants in that proceeding (inter partes).</li>
</ul>

<h3>2. Tests for Determining Ratio Decidendi</h3>
<ul>
  <li><strong>Wambaugh's Inversion Test (1894):</strong> Invert or reverse the proposition of law formulated by the court. If the court would have reached the exact same final decision despite the inversion, the proposition is mere obiter dictum. If inverting it forces a different outcome, it is genuine ratio decidendi.</li>
  <li><strong>Goodhart's Material Facts Test (1930):</strong> Arthur Goodhart argued that the ratio is not found in the judge's formal reasons, but in the judge's determination of the <em>material facts</em> of the case plus the decision based on those facts. Non-material facts are discarded.</li>
</ul>

<h3>3. Constitutional Stare Decisis in India (Article 141)</h3>
<p>Under Article 141 of the Constitution of India, the law declared by the Supreme Court is binding on all courts within the territory of India. The Supreme Court itself is not bound by its own prior judgments, but will not lightly overrule established precedents unless convinced they are erroneous and cause public mischief (Bengal Immunity Co. v. State of Bihar).</p>
""",
    "quickRevisionPoints": [
      "Stare Decisis: Stand by settled decisions; ensures predictability and judicial stability.",
      "Ratio Decidendi is the binding legal principle; Obiter Dicta is persuasive observation.",
      "Wambaugh's Inversion Test: Invert the legal rule; if outcome changes, rule is ratio.",
      "Goodhart's Test: Ratio = Material facts determined by judge + decision based thereon.",
      "Article 141: Law declared by Supreme Court binds all courts in India (SC not bound by own rulings)."
    ],
    "provisions": [
      {
        "provision": "Constitution of India, Art. 141",
        "title": "Law Declared by Supreme Court",
        "description": "The law declared by the Supreme Court shall be binding on all courts within the territory of India."
      }
    ],
    "definitions": [
      {
        "term": "Ratio Decidendi",
        "definition": "The rule of law upon which the judgment is based and which is necessary for the court's final decision."
      },
      {
        "term": "Obiter Dictum",
        "definition": "A statement of law in a judicial opinion that was not necessary for the decision of the case."
      }
    ],
    "ingredients": [
      "Existence of a hierarchical court structure with appellate jurisdiction.",
      "Competent determination of a contested question of law on material facts.",
      "Clear articulation of the legal ratio governing the factual dispute."
    ],
    "exceptions": [
      "Decisions rendered Per Incuriam (through carelessness/ignorance of a binding statute or higher bench precedent) have no binding value.",
      "Sub Silentio: A proposition of law passed without argument or conscious consideration does not create a binding precedent."
    ],
    "examples": [
      {
        "scenario": "A 2-judge bench of the Supreme Court decides a bail case contrary to an earlier 3-judge bench ruling without mentioning it.",
        "application": "The 2-judge bench ruling is per incuriam and the earlier 3-judge bench decision remains the binding authority under Article 141."
      }
    ],
    "landmarkCases": [
      {
        "case": "Bengal Immunity Co. v. State of Bihar",
        "citation": "AIR 1955 SC 661",
        "year": "1955",
        "bench": "7-Judge Bench (Das, Bhagwati, Venkatarama Ayyar, Sinha, Jafer Imam JJ)",
        "ratio": "The Supreme Court of India is not bound by its own previous decisions under Article 141, and has inherent power to reconsider and overrule its past rulings if convinced they are palpably erroneous or harm the public interest.",
        "impact": "Overruled the previous ruling in State of Bombay v. United Motors, establishing Indian stare decisis flexibility."
      }
    ],
    "comparisonTables": [
      {
        "title": "Ratio Decidendi vs Obiter Dictum",
        "headers": ["Attribute", "Ratio Decidendi", "Obiter Dictum"],
        "rows": [
          ["Binding Nature", "Strictly binding on subordinate courts", "Persuasive authority only"],
          ["Necessity to Dispute", "Essential for resolving the controversy", "Incidental statement 'by the way'"],
          ["Identification Method", "Wambaugh's Inversion or Goodhart's Test", "Passage can be excised without altering outcome"]
        ]
      }
    ],
    "diagramId": "diag-jur-sources-of-law",
    "diagramExplanation": "Flowchart showing the hierarchy of judicial precedent from Supreme Court under Art. 141 down to High Courts and District Courts.",
    "misconceptions": [
      {
        "myth": "Every statement made by the Supreme Court in a judgment is binding law under Article 141.",
        "reality": "Only the 'law declared' (Ratio Decidendi) is binding under Art. 141; casual obiter observations are not binding."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Confusing Per Incuriam with Sub Silentio.",
        "reality": "Per Incuriam means decided in ignorance of binding statute/ruling; Sub Silentio means decided without argument on the point.",
        "rule": "Ignorance of law = Per Incuriam; Lack of argument = Sub Silentio."
      }
    ],
    "flashcards": [
      {
        "id": "fc-jur-02-05",
        "front": "What test did Wambaugh formulate to ascertain the Ratio Decidendi?",
        "back": "The Inversion Test (reverse the proposition; if outcome changes, it is ratio).",
        "category": "Precedent Analysis"
      },
      {
        "id": "fc-jur-02-06",
        "front": "What is Arthur Goodhart's test for identifying the ratio of a case?",
        "back": "The Material Facts Test (Ratio = Material facts as seen by the judge + Decision on those facts).",
        "category": "Precedent Analysis"
      },
      {
        "id": "fc-jur-02-07",
        "front": "What is the legal effect of a judgment rendered 'Per Incuriam'?",
        "back": "It has no binding precedential force because it was rendered in ignorance of binding law.",
        "category": "Judicial Precedent"
      },
      {
        "id": "fc-jur-02-08",
        "front": "Is the Supreme Court of India bound by its own prior decisions under Article 141?",
        "back": "No, established in Bengal Immunity Co. v. State of Bihar (1955).",
        "category": "Indian Precedent"
      }
    ],
    "sourceReferences": [
      {"title": "Precedent in English Law — Rupert Cross", "url": "https://global.oup.com"},
      {"title": "The Ratio Decidendi of a Case — Arthur L. Goodhart (1930)", "url": "https://www.jstor.org"}
    ]
}

full_data["top-jur-02-03"] = {
    "topicId": "top-jur-02-03",
    "chapterId": "ch-jur-02",
    "subjectId": "law-jurisprudence",
    "title": "Legislation, Codification & Principles of Interpretation",
    "subtitle": "Supreme vs Subordinate Legislation and Canons of Statutory Construction",
    "juristRef": "Salmond, Bentham, Austin, Maxwell",
    "learningObjective": "Compare legislation with judicial precedent and custom, understand delegated legislation, and master the Literal, Golden, and Mischief rules of statutory interpretation.",
    "introduction": "Legislation is the formal declaration of legal rules by a competent sovereign organ. Derived from Latin 'legis' (law) and 'latio' (making), it is the most prolific, direct, and powerful modern source of law, capable of creating, amending, or abolishing legal rules instantaneously.",
    "detailedExplanation": """
<h3>1. Classification of Legislation</h3>
<ul>
  <li><strong>Supreme Legislation:</strong> Enacted by the sovereign legislative power of the state (e.g. Parliament under Indian Constitution). Cannot be annulled by any other internal authority except through constitutional judicial review.</li>
  <li><strong>Subordinate (Delegated) Legislation:</strong> Emanates from subordinate authorities acting under delegated legislative power conferred by an enabling parent statute (Rules, Regulations, Bye-laws, Notifications, Orders). Subordinate legislation must not be ultra vires the parent Act or the Constitution.</li>
</ul>

<h3>2. Codification of Law</h3>
<p>Jeremy Bentham was the pioneering advocate of universal codification, coining the term 'codification'. He argued that judge-made common law was retrospective, unpredictable 'dog-law'. A systematic statutory code ensures certainty, clarity, accessibility, and public knowledge of law.</p>

<h3>3. Three Primary Rules of Statutory Interpretation</h3>
<ul>
  <li><strong>Literal Rule:</strong> Words must be given their plain, ordinary, and grammatical meaning if the language is clear and unambiguous. <em>Litera scripta manet</em>. (Absoluta sententia expositore non indiget).</li>
  <li><strong>Golden Rule:</strong> If the literal interpretation leads to an absurdity, inconsistency, or injustice, the court may modify the grammatical meaning to avert the absurdity, but no further (Lord Wensleydale in Grey v. Pearson).</li>
  <li><strong>Mischief Rule (Rule in Heydon's Case, 1584):</strong> The court examines: (1) What was the common law before the Act? (2) What was the mischief for which the prior law did not provide? (3) What remedy did Parliament resolve? (4) The true reason of the remedy. The court must suppress the mischief and advance the remedy.</li>
</ul>
""",
    "quickRevisionPoints": [
      "Legislation is direct, prospective, and authoritative lawmaking by sovereign organs.",
      "Supreme legislation comes from Parliament; Subordinate comes from delegated executive bodies.",
      "Bentham coined 'Codification' and fiercely attacked common law as uncodified 'dog-law'.",
      "Literal Rule: Words interpreted in plain, ordinary grammatical sense.",
      "Golden Rule: Modify literal words only to prevent clear absurdity (Grey v. Pearson).",
      "Mischief Rule (Heydon's Case): Discover the mischief and advance the statutory remedy."
    ],
    "provisions": [
      {
        "provision": "Rule in Heydon's Case (1584)",
        "title": "Mischief Rule Four Inquiries",
        "description": "Previous common law, the mischief unaddressed, parliamentary remedy, and true reason of the remedy."
      }
    ],
    "definitions": [
      {
        "term": "Delegated Legislation",
        "definition": "Rules, regulations, orders, or bye-laws made by an executive body under statutory powers conferred by Parliament."
      }
    ],
    "ingredients": [
      "Authority: Enacted by a body possessing constitutional or delegated legislative competence.",
      "Form: Reduced to formal written statutory text.",
      "Operation: Primarily prospective, creating universal norms."
    ],
    "exceptions": [
      "Delegated legislation is invalid if it suffers from excessive delegation (delegation of essential legislative policy) or violates Fundamental Rights."
    ],
    "examples": [
      {
        "scenario": "A statute prohibits 'any vehicle' from entering a park. An ambulance enters to rescue an injured child.",
        "application": "Under the Literal Rule, the ambulance is excluded. Under the Golden/Mischief Rule, the purposive object of park peace and safety does not intend to bar emergency lifesaving vehicles, preventing absurdity."
      }
    ],
    "landmarkCases": [
      {
        "case": "Bengal Immunity Co. v. State of Bihar",
        "citation": "AIR 1955 SC 661",
        "year": "1955",
        "bench": "7-Judge Bench",
        "ratio": "The Supreme Court applied the Mischief Rule of Heydon's Case to interpret Article 286 of the Constitution, examining the pre-existing tax chaos under the Government of India Act 1935 to ascertain the true remedy intended by the framers.",
        "impact": "Classic Indian constitutional authority adopting the Mischief Rule of statutory construction."
      }
    ],
    "comparisonTables": [
      {
        "title": "Legislation vs Precedent as Sources of Law",
        "headers": ["Comparison Metric", "Legislation", "Judicial Precedent"],
        "rows": [
          ["Time of Creation", "Prospective rule for future conduct", "Decides past dispute retrospectively"],
          ["Form", "Codified statutory text (litera scripta)", "Extracted from ratio decidendi of reasoning"],
          ["Abrogation Power", "Can repeal judicial precedents and customs", "Cannot directly repeal statutes (can only strike down if unconstitutional)"]
        ]
      }
    ],
    "diagramId": "diag-jur-sources-of-law",
    "diagramExplanation": "Diagram illustrating the hierarchy between primary legislation, delegated legislation, and statutory canons of interpretation.",
    "misconceptions": [
      {
        "myth": "Courts can use the Mischief Rule whenever they disagree with the policy of an Act.",
        "reality": "If the statutory language is plain, clear, and unambiguous, the Literal Rule must be applied, and courts cannot rewrite policy."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing Salmond coined the term 'Codification'.",
        "reality": "Jeremy Bentham coined the term 'Codification'.",
        "rule": "Bentham = Coined 'Codification' and 'International Law'."
      }
    ],
    "flashcards": [
      {
        "id": "fc-jur-02-09",
        "front": "Who coined the word 'Codification'?",
        "back": "Jeremy Bentham.",
        "category": "Legislation"
      },
      {
        "id": "fc-jur-02-10",
        "front": "In which 1584 landmark English case was the Mischief Rule laid down?",
        "back": "Heydon's Case (1584) 3 Co Rep 7a.",
        "category": "Statutory Interpretation"
      },
      {
        "id": "fc-jur-02-11",
        "front": "What is the core formulation of the 'Golden Rule' of interpretation?",
        "back": "Adhere to the grammatical meaning unless it leads to absurdity, then modify only to remove the absurdity (Grey v Pearson).",
        "category": "Interpretation Rules"
      },
      {
        "id": "fc-jur-02-12",
        "front": "What does 'Ultra Vires' mean in the context of delegated legislation?",
        "back": "Beyond the powers conferred by the parent enabling statute.",
        "category": "Subordinate Legislation"
      }
    ],
    "sourceReferences": [
      {"title": "Maxwell on the Interpretation of Statutes — Sweet & Maxwell", "url": "https://www.sweetandmaxwell.co.uk"},
      {"title": "Principles of Statutory Interpretation — Justice G.P. Singh", "url": "https://www.lexisnexis.in"}
    ]
}

create_concept_file('assets/learning/data/jurisprudence/jurisprudence-concepts-part1.js', 'JURISPRUDENCE_CONCEPTS_PART1', full_data)
print("Updated jurisprudence-concepts-part1.js with 6 topics!")
