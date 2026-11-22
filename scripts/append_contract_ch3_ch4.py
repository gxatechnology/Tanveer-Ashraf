import json
from concept_helpers import create_concept_file

with open('assets/learning/data/contract/contract-concepts-part1.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('const DATA = ') + len('const DATA = ')
end_idx = text.rfind(';\n\n  global.')
data = json.loads(text[idx:end_idx])

# CHAPTER 3: CAPACITY TO CONTRACT
data["top-cnt-03-01"] = {
    "topicId": "top-cnt-03-01",
    "chapterId": "ch-cnt-03",
    "subjectId": "law-contract",
    "title": "Competency to Contract & Minor's Agreements (Mohori Bibee)",
    "subtitle": "Statutory Incapacity and the Rule of Absolute Voidness",
    "bareActRef": "Indian Contract Act, 1872 — Sections 10, 11",
    "learningObjective": "Understand minor contractual incapacity, the doctrine of void ab initio, absence of estoppel, and restitution rules.",
    "detailedExplanation": """
<h3>1. Statutory Capacity: Section 11</h3>
<p>Under Section 11, every person is competent to contract who is of the age of majority according to the law to which he is subject, who is of sound mind, and is not disqualified from contracting by any law.</p>

<h3>2. The Rule of Mohori Bibee v. Dharmodas Ghose (1903)</h3>
<p>The Privy Council settled that a minor's agreement is absolutely void (void ab initio), and not merely voidable. A mortgage executed by a minor cannot be enforced, nor can money advanced be recovered under Section 64 or 65 because no contract ever came into legal existence.</p>

<h3>3. Key Legal Principles Affecting Minors</h3>
<ul>
  <li><strong>No Estoppel:</strong> The rule of estoppel under Section 115 Evidence Act does not apply against a minor. A minor who misrepresents his age can still plead infancy (Leslie v. Sheill).</li>
  <li><strong>Doctrine of Restitution:</strong> Under equitable principles and Section 33 of the Specific Relief Act 1963, if a minor obtained property by falsely stating age, the court may compel restoration of the traceable asset, or in appropriate cases, monetary compensation if justice requires (Khan Gul v. Lakha Singh).</li>
  <li><strong>No Ratification:</strong> An agreement void ab initio cannot be ratified upon attaining majority, because consideration given during minority is non-existent in law.</li>
  <li><strong>Minor as Beneficiary:</strong> A minor can be a promisee or beneficiary under a contract (e.g., purchase or promissory note in minor's favor).</li>
</ul>
""",
    "quickRevisionPoints": [
      "Section 11: Majority age, sound mind, not disqualified.",
      "Mohori Bibee (1903 PC): Minor agreement is void ab initio, not voidable.",
      "No estoppel applies against a minor pleading infancy (Leslie v. Sheill).",
      "No ratification upon attaining majority.",
      "A minor can be a lawful beneficiary or promisee.",
      "Section 33 Specific Relief Act: Court may order restitution of benefits."
    ],
    "provisions": [
      {
        "provision": "Section 11, ICA 1872",
        "title": "Who are Competent to Contract",
        "description": "Every person is competent to contract who is of the age of majority according to the law to which he is subject, and who is of sound mind and is not disqualified from contracting by any law."
      }
    ],
    "definitions": [
      {
        "term": "Void Ab Initio",
        "definition": "Having no legal effect from the very inception of the transaction."
      }
    ],
    "ingredients": [
      "Age of majority under Indian Majority Act 1875 (18 years).",
      "Sound mental capacity under Section 12.",
      "Absence of statutory disqualification."
    ],
    "exceptions": [
      "Agreements for the benefit of a minor are enforceable by the minor."
    ],
    "examples": [
      {
        "scenario": "A, aged 17, executes a promissory note for Rs. 50,000 for a personal loan.",
        "application": "The lender cannot recover the amount because the note is void ab initio."
      }
    ],
    "landmarkCases": [
      {
        "case": "Mohori Bibee v. Dharmodas Ghose",
        "citation": "(1903) 30 IA 114",
        "year": "1903",
        "bench": "Privy Council (Lord Hobhouse)",
        "ratio": "Contracts with minors are not merely voidable at the minor's option, but void ab initio. Sections 64 and 65 do not apply to agreements void at inception.",
        "impact": "The leading foundation on minor incapacity in Indian contract jurisprudence."
      },
      {
        "case": "Khan Gul v. Lakha Singh",
        "citation": "AIR 1928 Lah 609",
        "year": "1928",
        "bench": "Lahore High Court (Shadi Lal CJ)",
        "ratio": "A minor fraudulently representing age must restore the consideration received under equitable discretion, now codified in Section 33 Specific Relief Act 1963.",
        "impact": "Established the modern equitable doctrine of restitution against fraudulent minors."
      }
    ],
    "comparisonTables": [
      {
        "title": "Minor Position: Indian Law vs English Law",
        "headers": ["Aspect", "Indian Law", "English Law (Infants Relief Act 1874)"],
        "rows": [
          ["Status of Contract", "Void ab initio (Mohori Bibee)", "Void, voidable, or valid (necessaries/beneficial service)"],
          ["Ratification", "Strictly barred", "Barred under Infants Relief Act 1874"],
          ["Enforceability as Beneficiary", "Fully permitted", "Permitted for necessary services and goods"]
        ]
      }
    ],
    "diagramId": "diag-cnt-validity-consent",
    "diagramExplanation": "Schematic charting contractual capacity and the consequences of minor status.",
    "misconceptions": [
      {
        "myth": "A contract with a minor is voidable at the option of the minor.",
        "reality": "It is void ab initio under Indian law, not voidable."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Assuming fresh consideration after majority validates a minor debt.",
        "reality": "A fresh promise after majority to pay for a loan taken during minority lacks consideration and is void.",
        "rule": "Minor debt cannot serve as consideration for subsequent promise."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-03-01",
        "front": "What did the Privy Council hold in Mohori Bibee v. Dharmodas Ghose (1903)?",
        "back": "A minor's contract is absolutely void ab initio.",
        "category": "Minor Capacity"
      },
      {
        "id": "fc-cnt-03-02",
        "front": "Can the doctrine of estoppel be applied against a minor who lies about his age?",
        "back": "No, estoppel does not apply against a statute that declares a minor incapable of contracting.",
        "category": "Estoppel Rules"
      },
      {
        "id": "fc-cnt-03-03",
        "front": "Which section of the Specific Relief Act 1963 codifies discretionary restitution against a minor?",
        "back": "Section 33.",
        "category": "Restitution"
      },
      {
        "id": "fc-cnt-03-04",
        "front": "Can a minor enforce a contract entered into for his sole benefit?",
        "back": "Yes, a minor can be a promisee or beneficiary.",
        "category": "Minor Rights"
      }
    ],
    "sourceReferences": [
      {"title": "Indian Contract Act, 1872", "url": "https://indiacode.nic.in"}
    ]
}

data["top-cnt-03-02"] = {
    "topicId": "top-cnt-03-02",
    "chapterId": "ch-cnt-03",
    "subjectId": "law-contract",
    "title": "Persons of Unsound Mind & Disqualified Persons (Section 12)",
    "subtitle": "The Cognitive Test of Contractual Capacity and Statutory Disqualifications",
    "bareActRef": "Indian Contract Act, 1872 — Section 12",
    "learningObjective": "Master the two-fold statutory test of sound mind under Section 12, lucid intervals, and statutory disqualifications.",
    "detailedExplanation": """
<h3>1. The Statutory Test of Sound Mind: Section 12</h3>
<p>A person is said to be of sound mind for the purpose of making a contract if, at the time when he makes it, he is capable of:</p>
<ol>
  <li>Understanding it, and</li>
  <li>Forming a rational judgment as to its effect upon his interests.</li>
</ol>
<p>Both conditions must co-exist at the exact moment of contract execution.</p>

<h3>2. Fluctuating Mental Capacity</h3>
<ul>
  <li><strong>Usually of Unsound Mind, Occasionally Sound:</strong> May contract during intervals of soundness (<em>Lucid Interval</em>) (Section 12, Para 2).</li>
  <li><strong>Usually of Sound Mind, Occasionally Unsound:</strong> May NOT contract during bouts of unsoundness (e.g., severe delirium or intoxication) (Section 12, Para 3).</li>
</ul>

<h3>3. Disqualified Persons</h3>
<p>Persons disqualified by specific legal statutes include: Alien enemies during war, foreign sovereigns/ambassadors (cannot be sued without central government consent under Section 86 CPC), undischarged insolvents, and convicts serving prison terms.</p>
""",
    "quickRevisionPoints": [
      "Section 12 test: Understanding the agreement + forming rational judgment on interests.",
      "Soundness is tested at the exact time of making the contract.",
      "Contracts made during a lucid interval are valid and binding.",
      "Drunkenness or delirium renders a person temporarily incapable under Section 12.",
      "Alien enemies, undischarged insolvents, and convicts are disqualified by law."
    ],
    "provisions": [
      {
        "provision": "Section 12, ICA 1872",
        "title": "What is a Sound Mind for the Purposes of Contracting",
        "description": "A person is of sound mind for the purpose of contracting if he is capable of understanding it and forming a rational judgment as to its effect upon his interests at the time of making."
      }
    ],
    "definitions": [
      {
        "term": "Lucid Interval",
        "definition": "A temporary period of rational sanity during which a person normally of unsound mind is fully capable of contracting."
      }
    ],
    "ingredients": [
      "Capability of understanding contractual terms.",
      "Capability of assessing rational impact on own interests.",
      "Relevant mental state at the time of execution."
    ],
    "exceptions": [
      "Necessaries supplied to persons of unsound mind are reimbursable from property under Section 68."
    ],
    "examples": [
      {
        "scenario": "A patient in a psychiatric hospital who has periods of complete lucidity enters into a property sale during a certified lucid interval.",
        "application": "The sale is valid and binding under Section 12 paragraph 2."
      }
    ],
    "landmarkCases": [
      {
        "case": "Inder Singh v. Parmeshwardhari Singh",
        "citation": "AIR 1957 Pat 491",
        "year": "1957",
        "bench": "Patna High Court",
        "ratio": "A property sale executed by an intellectually disabled youth for nominal consideration was held void because he lacked capacity to form a rational judgment on his financial interest.",
        "impact": "Confirmed the dual requirement of understanding and rational assessment under Section 12."
      }
    ],
    "comparisonTables": [
      {
        "title": "Mental Capacity Scenarios under Section 12",
        "headers": ["General Mental State", "State at Time of Contract", "Contractual Validity"],
        "rows": [
          ["Usually Unsound", "During Lucid Interval", "Valid and enforceable"],
          ["Usually Sound", "During Delirium / Intoxication", "Void for incapacity"],
          ["Permanent Unsoundness", "Unsound", "Void ab initio"]
        ]
      }
    ],
    "diagramId": "diag-cnt-validity-consent",
    "diagramExplanation": "Flowchart representing capacity evaluation at the moment of agreement.",
    "misconceptions": [
      {
        "myth": "A person declared of unsound mind can never enter into a valid contract.",
        "reality": "If they experience a genuine lucid interval, they may validly contract during that period."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Treating mere eccentricity as unsoundness of mind.",
        "reality": "Eccentric behavior does not invalidate a contract unless it impairs rational understanding of the transaction.",
        "rule": "Understanding + rational assessment = sound mind."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-03-05",
        "front": "What are the two components of a sound mind under Section 12?",
        "back": "Capability of understanding the contract, and capability of forming a rational judgment as to its effect on one's interests.",
        "category": "Capacity to Contract"
      },
      {
        "id": "fc-cnt-03-06",
        "front": "Can a person usually of unsound mind contract during a lucid interval?",
        "back": "Yes, under Section 12 paragraph 2.",
        "category": "Lucid Intervals"
      },
      {
        "id": "fc-cnt-03-07",
        "front": "At what point in time is the soundness of mind evaluated?",
        "back": "At the exact time when the contract is made.",
        "category": "Section 12"
      },
      {
        "id": "fc-cnt-03-08",
        "front": "What is the status of an agreement entered into by a person during severe drunken stupor?",
        "back": "Void for want of contractual capacity under Section 12 paragraph 3.",
        "category": "Incapacity"
      }
    ],
    "sourceReferences": [
      {"title": "Indian Contract Act, 1872", "url": "https://indiacode.nic.in"}
    ]
}

data["top-cnt-03-03"] = {
    "topicId": "top-cnt-03-03",
    "chapterId": "ch-cnt-03",
    "subjectId": "law-contract",
    "title": "Necessaries Supplied to Incompetent Persons (Section 68)",
    "subtitle": "Quasi-Contractual Reimbursement for Essential Goods and Services",
    "bareActRef": "Indian Contract Act, 1872 — Section 68",
    "learningObjective": "Master Section 68 claims for necessaries supplied to minors or persons of unsound mind, property-only liability, and the rule in Nash v Inman.",
    "detailedExplanation": """
<h3>1. Statutory Provision: Section 68</h3>
<p>'If a person, incapable of entering into a contract, or any one whom he is legally bound to support, is supplied by another person with necessaries suited to his condition in life, the person who has furnished such supplies is entitled to be reimbursed from the property of such incapable person.'</p>

<h3>2. Essential Ingredients of Section 68</h3>
<ol>
  <li><strong>Supplied to Incompetent or Dependents:</strong> Goods or services supplied to a minor, person of unsound mind, or someone they are legally bound to support (e.g., minor's wife or child).</li>
  <li><strong>Suited to Condition in Life:</strong> 'Necessaries' are not limited to bare physical subsistence (food, shelter, clothing). They include education, medical care, and legal defense, judged according to the social status and station of the person.</li>
  <li><strong>Actual Need at Time of Delivery:</strong> The goods must be necessary both at the time of order and at the time of delivery. If the minor is already adequately provided, the goods are not necessaries (<em>Nash v. Inman</em>).</li>
</ol>

<h3>3. Nature of Liability: Property Only, No Personal Liability</h3>
<p>The incompetent person is <strong>never personally liable</strong>. The supplier can seek reimbursement exclusively from the property or estate of the incompetent person. If the minor owns no property, the supplier recovers nothing.</p>
""",
    "quickRevisionPoints": [
      "Section 68 is quasi-contractual; no agreement is required.",
      "Covers necessaries suited to the recipient's station in life.",
      "Extends to dependents whom the incapable person is bound to support.",
      "Nash v. Inman (1908): 11 fancy waistcoats supplied to a minor already well-supplied were not necessaries.",
      "Liability is proprietary only (against estate); minor is never personally liable."
    ],
    "provisions": [
      {
        "provision": "Section 68, ICA 1872",
        "title": "Claim for Necessaries Supplied to Incapable Person",
        "description": "A person furnishing supplies of necessaries suited to the condition in life of an incapable person or dependent is entitled to reimbursement from the property of such incapable person."
      }
    ],
    "definitions": [
      {
        "term": "Necessaries",
        "definition": "Articles and services essential to maintain a person according to their degree, status, and condition in life, excluding luxuries."
      }
    ],
    "ingredients": [
      "Incapable recipient or dependent.",
      "Goods/services qualify as necessaries.",
      "Actual deficiency in supply at delivery.",
      "Existence of property from which to reimburse."
    ],
    "exceptions": [
      "Articles of pure luxury or ornamental expenditure do not qualify."
    ],
    "examples": [
      {
        "scenario": "A doctor provides essential medical treatment and medicines to the ailing infant child of a wealthy minor.",
        "application": "The doctor is entitled to be reimbursed from the minor's property under Section 68."
      }
    ],
    "landmarkCases": [
      {
        "case": "Nash v. Inman",
        "citation": "(1908) 2 KB 1",
        "year": "1908",
        "bench": "Court of Appeal (Fletcher Moulton LJ)",
        "ratio": "A tailor who supplied 11 fancy waistcoats to an undergraduate minor could not recover the price because the student's father proved he was already adequately supplied with suitable clothes.",
        "impact": "Leading authority establishing that plaintiff must prove both suitability to station and actual lack of supply."
      }
    ],
    "comparisonTables": [
      {
        "title": "Contractual Debt vs Section 68 Claim",
        "headers": ["Feature", "Contractual Debt", "Section 68 Claim"],
        "rows": [
          ["Basis", "Express agreement between competent parties", "Quasi-contract (unjust enrichment/necessity)"],
          ["Personal Liability", "Debtor can be arrested/personally liable", "No personal liability; against estate only"],
          ["Minor Competence", "Void ab initio if entered by minor", "Reimbursement valid from minor's property"]
        ]
      }
    ],
    "diagramId": "diag-cnt-validity-consent",
    "diagramExplanation": "Diagram showing the flow of reimbursement from the minor's estate under Section 68.",
    "misconceptions": [
      {
        "myth": "A minor can be sued personally and sent to prison for unpaid bills for food.",
        "reality": "Under Section 68, liability attaches solely to property; no personal decree or arrest can be made."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing necessaries mean only basic bread, water, and clothing.",
        "reality": "Necessaries depend on station in life and include professional education, medical care, and funeral expenses.",
        "rule": "Necessaries = Suited to condition in life + actually needed."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-03-09",
        "front": "Which section of the Contract Act provides for supply of necessaries to minors?",
        "back": "Section 68.",
        "category": "Necessaries"
      },
      {
        "id": "fc-cnt-03-10",
        "front": "Can a minor be held personally liable under Section 68?",
        "back": "No, reimbursement is strictly limited to the minor's property/estate.",
        "category": "Liability Scope"
      },
      {
        "id": "fc-cnt-03-11",
        "front": "What was held in the classic case Nash v. Inman (1908)?",
        "back": "Goods are not necessaries if the minor is already adequately supplied with them.",
        "category": "Case Law"
      },
      {
        "id": "fc-cnt-03-12",
        "front": "Does Section 68 cover necessaries supplied to a minor's lawful dependents?",
        "back": "Yes, it covers anyone whom the incapable person is legally bound to support.",
        "category": "Dependents"
      }
    ],
    "sourceReferences": [
      {"title": "Indian Contract Act, 1872", "url": "https://indiacode.nic.in"}
    ]
}

# CHAPTER 4: FREE CONSENT
data["top-cnt-04-01"] = {
    "topicId": "top-cnt-04-01",
    "chapterId": "ch-cnt-04",
    "subjectId": "law-contract",
    "title": "Concept of Free Consent & Consensus ad Idem (Sections 13, 14)",
    "subtitle": "The Subjective Meeting of Minds and Vitiating Elements",
    "bareActRef": "Indian Contract Act, 1872 — Sections 13, 14",
    "learningObjective": "Understand consensus ad idem under Section 13, the five vitiating factors under Section 14, and the distinction between absence of consent vs vitiated consent.",
    "detailedExplanation": """
<h3>1. Consensus Ad Idem: Section 13</h3>
<p>'Two or more persons are said to consent when they agree upon the same thing in the same sense.' (Consensus ad idem). If there is no identity of subject matter or sense, there is no consent at all, and no agreement is ever formed (<em>Raffles v. Wichelhaus</em> — Peerless ship arriving in October vs December).</p>

<h3>2. Free Consent Defined: Section 14</h3>
<p>Consent is said to be free when it is not caused by:</p>
<ol>
  <li><strong>Coercion:</strong> As defined in Section 15.</li>
  <li><strong>Undue Influence:</strong> As defined in Section 16.</li>
  <li><strong>Fraud:</strong> As defined in Section 17.</li>
  <li><strong>Misrepresentation:</strong> As defined in Section 18.</li>
  <li><strong>Mistake:</strong> Subject to the provisions of Sections 20, 21, and 22.</li>
</ol>

<h3>3. Legal Consequence of Vitiated Consent</h3>
<ul>
  <li>Consent caused by Coercion, Fraud, or Misrepresentation -> <strong>Voidable</strong> under Section 19 at option of aggrieved party.</li>
  <li>Consent caused by Undue Influence -> <strong>Voidable</strong> under Section 19A.</li>
  <li>Consent caused by Bilateral Mistake of essential fact -> <strong>Void</strong> under Section 20.</li>
</ul>
""",
    "quickRevisionPoints": [
      "Section 13: Consent = Agreeing upon the same thing in the same sense (consensus ad idem).",
      "Section 14: 5 vitiating factors: Coercion, Undue Influence, Fraud, Misrepresentation, Mistake.",
      "No consensus = No agreement at all (Raffles v. Wichelhaus).",
      "Coercion, Fraud, Misrepresentation make contract voidable under Section 19.",
      "Undue Influence makes contract voidable under Section 19A.",
      "Bilateral mistake on essential fact makes agreement void under Section 20."
    ],
    "provisions": [
      {
        "provision": "Section 13, ICA 1872",
        "title": "Consent Defined",
        "description": "Two or more persons are said to consent when they agree upon the same thing in the same sense."
      },
      {
        "provision": "Section 14, ICA 1872",
        "title": "Free Consent Defined",
        "description": "Consent is said to be free when it is not caused by coercion, undue influence, fraud, misrepresentation, or mistake."
      }
    ],
    "definitions": [
      {
        "term": "Consensus Ad Idem",
        "definition": "Mutual agreement between parties upon the same subject-matter in the exact same sense."
      }
    ],
    "ingredients": [
      "Agreement on identity of subject-matter.",
      "Agreement in the same sense.",
      "Absence of Section 14 vitiating elements."
    ],
    "exceptions": [
      "If consent was not caused by the vitiating factor (e.g. party was unaware of misrepresentation), contract remains binding."
    ],
    "examples": [
      {
        "scenario": "A agrees to sell cotton to B to arrive ex Peerless from Bombay. Two ships named Peerless sail from Bombay, one in October and one in December. A intended December; B intended October.",
        "application": "There was no consensus ad idem; no contract was formed (Raffles v. Wichelhaus)."
      }
    ],
    "landmarkCases": [
      {
        "case": "Raffles v. Wichelhaus",
        "citation": "(1864) 2 H&C 906",
        "year": "1864",
        "bench": "Court of Exchequer",
        "ratio": "Where parties contracted for cargo from a ship named 'Peerless', unaware that two different ships of that name existed sailing in different months, there was no consensus ad idem and no binding contract.",
        "impact": "Classic authority on mutual misunderstanding destroying consensus ad idem."
      }
    ],
    "comparisonTables": [
      {
        "title": "Absence of Consent vs Vitiated Consent",
        "headers": ["Feature", "Absence of Consent (s. 13)", "Vitiated Consent (s. 14)"],
        "rows": [
          ["Meeting of Minds", "Zero consensus ad idem", "Consensus exists but procured improperly"],
          ["Legal Effect", "Void ab initio; agreement never formed", "Voidable at option of aggrieved party (or void for mistake)"],
          ["Example", "Contracting for two different ships", "Signing contract under threat of physical harm"]
        ]
      }
    ],
    "diagramId": "diag-cnt-validity-consent",
    "diagramExplanation": "Diagram showing the branches of vitiated consent leading to voidable or void status.",
    "misconceptions": [
      {
        "myth": "All contracts where consent is not free are void ab initio.",
        "reality": "Most are voidable at the option of the aggrieved party (ss. 19, 19A). Only bilateral mistake of essential fact makes the agreement void (s. 20)."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Confusing Section 19 with Section 19A.",
        "reality": "Section 19 governs Coercion, Fraud, and Misrepresentation. Section 19A specifically governs Undue Influence.",
        "rule": "19 = Coercion/Fraud/Misrep; 19A = Undue Influence."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-04-01",
        "front": "What does Section 13 of the Indian Contract Act define?",
        "back": "Consent — two or more persons agree upon the same thing in the same sense.",
        "category": "Consent"
      },
      {
        "id": "fc-cnt-04-02",
        "front": "What are the 5 factors that negate free consent under Section 14?",
        "back": "Coercion (s.15), Undue Influence (s.16), Fraud (s.17), Misrepresentation (s.18), and Mistake (ss.20-22).",
        "category": "Free Consent"
      },
      {
        "id": "fc-cnt-04-03",
        "front": "What is the legal consequence when there is no consensus ad idem between parties?",
        "back": "The agreement is void ab initio; no contract ever comes into existence.",
        "category": "Consensus"
      },
      {
        "id": "fc-cnt-04-04",
        "front": "Which section governs the voidability of contracts caused by Undue Influence?",
        "back": "Section 19A.",
        "category": "Voidability"
      }
    ],
    "sourceReferences": [
      {"title": "Indian Contract Act, 1872", "url": "https://indiacode.nic.in"}
    ]
}

data["top-cnt-04-02"] = {
    "topicId": "top-cnt-04-02",
    "chapterId": "ch-cnt-04",
    "subjectId": "law-contract",
    "title": "Coercion: Statutory Definition & Legal Impact (Section 15)",
    "subtitle": "Physical Duress, Threats to Penal Law, and Unlawful Detention of Property",
    "bareActRef": "Indian Contract Act, 1872 — Sections 15, 19, 72",
    "learningObjective": "Master Section 15 coercion, compare with English duress, understand Chikham Amiraju, and identify remedies under Sections 19 and 72.",
    "detailedExplanation": """
<h3>1. Statutory Definition: Section 15</h3>
<p>'Coercion' is committing, or threatening to commit, any act forbidden by the Indian Penal Code (or Bharatiya Nyaya Sanhita), or the unlawful detaining, or threatening to detain, any property, to the prejudice of any person whatever, with the intention of causing any person to enter into an agreement.</p>
<p><strong>Explanation:</strong> It is immaterial whether the penal law is or is not in force in the place where the coercion is employed (e.g., coercion committed on high seas).</p>

<h3>2. The Scope of Coercion</h3>
<ul>
  <li><strong>Acts Forbidden by Penal Code:</strong> Threat to murder, assault, or falsely prosecute. In <em>Chikham Amiraju v. Chikham Seshamma (1917)</em>, a Hindu man threatened to commit suicide unless his wife and son executed a release deed of family property. Held: Suicide is an act forbidden by the penal code; the threat constituted coercion.</li>
  <li><strong>Unlawful Detaining of Property:</strong> Refusing to surrender books of account or seized goods until an agreement or payment is extracted (<em>Astley v. Reynolds</em>).</li>
  <li><strong>Prejudice of Any Person Whatever:</strong> The threat need not be directed at the contracting party; threatening a party's child or parent is coercion.</li>
</ul>

<h3>3. Coercion vs. English Common Law Duress</h3>
<p>English duress historically applied only to physical threats against life or liberty. Indian Section 15 is much wider: it covers threats to property and any act forbidden by penal law.</p>

<h3>4. Legal Effects: Sections 19 and 72</h3>
<p>The contract is voidable at the option of the party whose consent was coerced (Section 19). Under Section 72, any money paid or thing delivered under coercion must be repaid or returned.</p>
""",
    "quickRevisionPoints": [
      "Section 15: Committing/threatening act forbidden by Penal Code, or unlawful detaining of property.",
      "Intention must be to cause someone to enter into an agreement.",
      "Chikham Amiraju (1917 Mad): Threat to commit suicide is coercion under Section 15.",
      "Threat to property constitutes coercion under Indian law (unlike classical English duress).",
      "Remedy: Voidable under Section 19; restitution under Section 72."
    ],
    "provisions": [
      {
        "provision": "Section 15, ICA 1872",
        "title": "Coercion Defined",
        "description": "Coercion is the committing, or threatening to commit, any act forbidden by the Penal Code, or the unlawful detaining or threatening to detain any property, with the intention of causing any person to enter into an agreement."
      }
    ],
    "definitions": [
      {
        "term": "Duress",
        "definition": "The English common law concept of coercion, historically limited to threats of bodily injury, death, or unlawful imprisonment."
      }
    ],
    "ingredients": [
      "Act forbidden by penal statute, or unlawful detention of property.",
      "Intention to compel entry into agreement.",
      "Direction to prejudice of any person."
    ],
    "exceptions": [
      "Threat to bring a lawful civil suit is not coercion."
    ],
    "examples": [
      {
        "scenario": "A landlord unlawfully locks a tenant's trade machinery and refuses to release it unless the tenant signs a promissory note for double rent.",
        "application": "The promissory note is voidable for coercion under Section 15 (unlawful detention of property)."
      }
    ],
    "landmarkCases": [
      {
        "case": "Chikham Amiraju v. Chikham Seshamma",
        "citation": "(1917) ILR 41 Mad 33",
        "year": "1917",
        "bench": "Madras High Court (Wallis CJ and Seshagiri Ayyar J)",
        "ratio": "A threat by a husband to commit suicide unless his wife and son executed a deed transferring property to his brother amounted to coercion under Section 15, because suicide is an act forbidden by the penal code.",
        "impact": "Leading Indian precedent establishing that threat to commit suicide constitutes coercion."
      }
    ],
    "comparisonTables": [
      {
        "title": "Coercion (Indian Law) vs Duress (English Law)",
        "headers": ["Aspect", "Coercion (s. 15 ICA)", "English Duress"],
        "rows": [
          ["Threat to Property", "Expressly included (unlawful detention)", "Historically excluded (now recognized as economic duress)"],
          ["Target of Threat", "Can be directed against any third party", "Must be directed against party or near relative"],
          ["Scope of Acts", "Any act forbidden by penal law", "Violence, imprisonment, or unlawful pressure"]
        ]
      }
    ],
    "diagramId": "diag-cnt-coercion-undue-influence",
    "diagramExplanation": "Schematic comparing physical/penal coercion with psychological undue influence.",
    "misconceptions": [
      {
        "myth": "A threat to file a regular civil suit for recovery of money constitutes coercion.",
        "reality": "Exercising or threatening a lawful legal remedy is not an act forbidden by penal law and is not coercion."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing suicide is punishable and therefore forbidden.",
        "reality": "Attempt to commit suicide is punishable, and suicide itself is forbidden by penal law; hence the threat is coercion.",
        "rule": "Threat to commit suicide = Coercion (Chikham Amiraju)."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-04-05",
        "front": "Which section defines Coercion in the Indian Contract Act?",
        "back": "Section 15.",
        "category": "Coercion"
      },
      {
        "id": "fc-cnt-04-06",
        "front": "What did the Madras High Court decide in Chikham Amiraju v. Seshamma?",
        "back": "A threat to commit suicide constitutes coercion under Section 15.",
        "category": "Landmark Precedents"
      },
      {
        "id": "fc-cnt-04-07",
        "front": "Does unlawful detention of property amount to coercion under Indian law?",
        "back": "Yes, Section 15 explicitly includes unlawful detaining or threatening to detain property.",
        "category": "Property Coercion"
      },
      {
        "id": "fc-cnt-04-08",
        "front": "Under which section can money paid under coercion be recovered?",
        "back": "Section 72.",
        "category": "Restitution"
      }
    ],
    "sourceReferences": [
      {"title": "Indian Contract Act, 1872", "url": "https://indiacode.nic.in"}
    ]
}

data["top-cnt-04-03"] = {
    "topicId": "top-cnt-04-03",
    "chapterId": "ch-cnt-04",
    "subjectId": "law-contract",
    "title": "Undue Influence, Fiduciary Position & Unconscionability (Section 16)",
    "subtitle": "Moral Coercion, Dominating the Will, and the Burden of Proof",
    "bareActRef": "Indian Contract Act, 1872 — Sections 16, 19A",
    "learningObjective": "Master Section 16 undue influence, fiduciary relations, unconscionable transactions, pardanashin ladies, and Section 19A remedies.",
    "detailedExplanation": """
<h3>1. Statutory Definition: Section 16(1)</h3>
<p>'A contract is said to be induced by undue influence where the relations subsisting between the parties are such that one of the parties is in a position to dominate the will of the other and uses that position to obtain an unfair advantage over the other.'</p>

<h3>2. When a Person is Deemed in a Position to Dominate: Section 16(2)</h3>
<p>A person is deemed to dominate the will of another in three situations:</p>
<ol>
  <li><strong>Real or Apparent Authority:</strong> E.g., police officer and accused, tax officer and assessee, employer and subordinate.</li>
  <li><strong>Fiduciary Relationship:</strong> A relation of mutual trust and confidence (parent and child, trustee and beneficiary, advocate and client, doctor and patient, spiritual guru and devotee).</li>
  <li><strong>Mental Distress:</strong> Contracting with a person whose mental capacity is temporarily or permanently affected by reason of age, illness, or bodily distress.</li>
</ol>

<h3>3. Burden of Proof in Unconscionable Transactions: Section 16(3)</h3>
<p>Where a person in a dominating position enters into a contract which appears on the face of it, or on the evidence, to be <strong>unconscionable</strong> (grossly one-sided), the burden of proving that the contract was made with free consent lies upon the dominating party!</p>

<h3>4. Protection of Pardanashin Ladies</h3>
<p>A pardanashin lady (observing complete seclusion from outside society) receives special legal protection. The law presumes undue influence; the party claiming under a contract with a pardanashin lady must prove that the deed was read and explained to her and she had independent legal advice.</p>

<h3>5. Relief under Section 19A</h3>
<p>A contract induced by undue influence is voidable at the option of the aggrieved party. The court has discretion to set it aside absolutely, or upon such terms and conditions as to the court may seem just.</p>
""",
    "quickRevisionPoints": [
      "Section 16: Position to dominate will + using that position to obtain unfair advantage.",
      "Dominating positions: Real authority, fiduciary relationship, mental distress.",
      "Section 16(3): In unconscionable bargains, burden of proof shifts to the dominating party.",
      "Pardanashin ladies receive special protection against undue influence.",
      "Section 19A: Voidable; court may set aside absolutely or upon terms."
    ],
    "provisions": [
      {
        "provision": "Section 16, ICA 1872",
        "title": "Undue Influence Defined",
        "description": "Where relations are such that one party is in a position to dominate the will of the other and uses that position to obtain an unfair advantage."
      },
      {
        "provision": "Section 19A, ICA 1872",
        "title": "Power to Set Aside Contract Induced by Undue Influence",
        "description": "Any contract induced by undue influence may be set aside absolutely or upon terms."
      }
    ],
    "definitions": [
      {
        "term": "Unconscionable Bargain",
        "definition": "A transaction so grossly unfair and one-sided that it shocks the conscience of the court."
      }
    ],
    "ingredients": [
      "Sub-existing relation with power to dominate.",
      "Exercise of domination.",
      "Securing of unfair advantage."
    ],
    "exceptions": [
      "Ordinary commercial transactions between business equals do not attract undue influence."
    ],
    "examples": [
      {
        "scenario": "A guru induces his wealthy disciple to gift all his ancestral property to the guru's ashram for the salvation of the disciple's soul.",
        "application": "The gift is voidable for undue influence under Section 16(2) (spiritual influence/fiduciary relation)."
      }
    ],
    "landmarkCases": [
      {
        "case": "Subhas Chandra Das Mushib v. Ganga Prasad Das Mushib",
        "citation": "(1967) 1 SCR 331",
        "year": "1967",
        "bench": "Supreme Court of India (Mitter J)",
        "ratio": "The court laid down three stages for examining undue influence: (1) whether the relations show one dominating the other, (2) whether the contract is unconscionable on its face, and (3) if so, whether the dominating party has discharged the burden of proving fair play.",
        "impact": "Authoritative guide on the structured inquiry into Section 16 undue influence."
      },
      {
        "case": "Mannu Singh v. Umadat Pande",
        "citation": "(1890) ILR 12 All 523",
        "year": "1890",
        "bench": "Allahabad High Court",
        "ratio": "A devotee gifted all his property to his spiritual guru. Held: Spiritual advisor is in a fiduciary position of domination; the burden of proving free consent lay on the guru, failing which the gift was set aside.",
        "impact": "Leading precedent on spiritual undue influence."
      }
    ],
    "comparisonTables": [
      {
        "title": "Coercion vs Undue Influence",
        "headers": ["Aspect", "Coercion (Section 15)", "Undue Influence (Section 16)"],
        "rows": [
          ["Nature of Pressure", "Physical force or threat of crime", "Moral pressure or mental dominance"],
          ["Pre-existing Relationship", "Not required; can be by stranger", "Essential; parties must stand in special relation"],
          ["Governing Remedy Section", "Section 19", "Section 19A (court can set aside on terms)"]
        ]
      }
    ],
    "diagramId": "diag-cnt-coercion-undue-influence",
    "diagramExplanation": "Custom vector schematic illustrating the elements and shifting burden under Section 16.",
    "misconceptions": [
      {
        "myth": "High interest rate alone automatically proves undue influence.",
        "reality": "Urgent financial distress of a borrower in the open money market does not establish that the lender dominated his will."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Assuming husband and wife is automatically a fiduciary relation under Section 16.",
        "reality": "Spousal relation is not presumed to be fiduciary; dominance must be proved on facts (unlike parent-child or lawyer-client).",
        "rule": "Parent-child = Presumed fiduciary; Husband-wife = Not presumed."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-04-09",
        "front": "What are the two core elements of Undue Influence under Section 16(1)?",
        "back": "Position to dominate the will of another, and using that position to obtain an unfair advantage.",
        "category": "Undue Influence"
      },
      {
        "id": "fc-cnt-04-10",
        "front": "When does the burden of proof shift to the defendant under Section 16(3)?",
        "back": "When a person in a dominating position enters into a transaction that appears unconscionable on its face.",
        "category": "Burden of Proof"
      },
      {
        "id": "fc-cnt-04-11",
        "front": "Which section allows the court to set aside a contract induced by undue influence upon terms?",
        "back": "Section 19A.",
        "category": "Relief"
      },
      {
        "id": "fc-cnt-04-12",
        "front": "What was held in Mannu Singh v. Umadat Pande (1890)?",
        "back": "Gift by a devotee to his spiritual guru was set aside for undue influence because guru failed to prove free consent.",
        "category": "Case Law"
      }
    ],
    "sourceReferences": [
      {"title": "Indian Contract Act, 1872", "url": "https://indiacode.nic.in"}
    ]
}

data["top-cnt-04-04"] = {
    "topicId": "top-cnt-04-04",
    "chapterId": "ch-cnt-04",
    "subjectId": "law-contract",
    "title": "Fraud: Active Concealment & When Silence is Fraud (Section 17)",
    "subtitle": "Intentional Deception and the Boundary Between Caveat Emptor and Fraud",
    "bareActRef": "Indian Contract Act, 1872 — Sections 17, 19",
    "learningObjective": "Master Section 17 fraud, active concealment, when silence amounts to fraud, and the Derry v Peek mens rea rule.",
    "detailedExplanation": """
<h3>1. Statutory Definition: Section 17</h3>
<p>'Fraud' means and includes any of the following acts committed by a party to a contract, or with his connivance, or by his agent, with intent to deceive another party or to induce him to enter into the contract:</p>
<ol>
  <li><strong>False Suggestion (Suggestio Falsi):</strong> Suggestion as a fact of that which is not true, by one who does not believe it to be true.</li>
  <li><strong>Active Concealment (Suppressio Veri):</strong> The active concealment of a fact by one having knowledge or belief of the fact.</li>
  <li><strong>Promise Without Intention:</strong> A promise made without any intention of performing it.</li>
  <li><strong>Any Other Deceptive Act:</strong> Any other act fitted to deceive.</li>
  <li><strong>Statutory Fraud:</strong> Any such act or omission as the law specially declares to be fraudulent.</li>
</ol>

<h3>2. Mere Silence is NOT Fraud: The Explanation to Section 17</h3>
<p>'Mere silence as to facts likely to affect the willingness of a person to enter into a contract is not fraud.' This reflects the general rule of <strong>Caveat Emptor</strong> (Let the buyer beware). A seller is not bound to disclose all defects.</p>
<p><strong>Two Crucial Exceptions where Silence IS Fraud:</strong></p>
<ul>
  <li><strong>Duty to Speak:</strong> Where circumstances create a legal duty for the person keeping silence to speak (e.g., contracts <em>uberrimae fidei</em> like insurance, fiduciary relationships, family settlements).</li>
  <li><strong>Silence Equivalent to Speech:</strong> Where silence is, in itself, equivalent to speech (e.g., buyer says 'If you do not deny it, I shall assume the horse is sound', and seller remains silent).</li>
</ul>

<h3>3. Remedies for Fraud: Section 19</h3>
<p>A contract induced by fraud is <strong>voidable</strong> at the option of the defrauded party. In addition, the victim can:</p>
<ul>
  <li>Rescind the contract and claim restitution under Section 64.</li>
  <li>Affirm the contract and insist that he be put in the position in which he would have been if the representation was true.</li>
  <li>Sue for damages in the independent tort of deceit (<em>Derry v. Peek</em>).</li>
</ul>
""",
    "quickRevisionPoints": [
      "Section 17: Intentional deception (false statement, active concealment, empty promise).",
      "Suggestio falsi (false suggestion) & Suppressio veri (active concealment).",
      "Mere silence is NOT fraud (Caveat Emptor).",
      "Silence IS fraud when there is a duty to speak (uberrimae fidei) or silence equals speech.",
      "Remedy: Voidable under Section 19 + tortious damages for deceit."
    ],
    "provisions": [
      {
        "provision": "Section 17, ICA 1872",
        "title": "Fraud Defined",
        "description": "Fraud includes false suggestions made without belief in truth, active concealment of facts, promises without intention to perform, and acts fitted to deceive."
      }
    ],
    "definitions": [
      {
        "term": "Contracts Uberrimae Fidei",
        "definition": "Contracts of utmost good faith (such as insurance) where parties are under an absolute legal duty to disclose all material facts."
      }
    ],
    "ingredients": [
      "Intent to deceive or induce contract.",
      "Commission of one of the 5 acts in Section 17.",
      "Actual reliance and deception by the other party."
    ],
    "exceptions": [
      "If the party had means of discovering truth with ordinary diligence in cases of silence/misrepresentation (Section 19 Exception)."
    ],
    "examples": [
      {
        "scenario": "A sells a horse to B knowing it has an unsound hoof, and deliberately uses wax to fill and conceal the crack so B cannot see it.",
        "application": "This is active concealment (suppressio veri) under Section 17(2), constituting fraud."
      }
    ],
    "landmarkCases": [
      {
        "case": "Derry v. Peek",
        "citation": "(1889) 14 App Cas 337",
        "year": "1889",
        "bench": "House of Lords (Lord Herschell)",
        "ratio": "Fraud is proved when a false representation has been made: (1) knowingly, (2) without belief in its truth, or (3) recklessly, careless whether it be true or false. Honest belief in truth excludes fraud.",
        "impact": "Classic common law authority establishing the requisite mental element for fraud."
      },
      {
        "case": "Shri Krishan v. Kurukshetra University",
        "citation": "(1976) 1 SCC 311",
        "year": "1976",
        "bench": "Supreme Court of India (Beg J)",
        "ratio": "A student who did not mention his short attendance in his examination form did not commit fraud because mere silence is not fraud; it was the duty of university authorities to scrutinize attendance records.",
        "impact": "Affirmed the rule that mere silence is not fraud under Section 17 where no duty to speak exists."
      }
    ],
    "comparisonTables": [
      {
        "title": "Fraud (Section 17) vs Misrepresentation (Section 18)",
        "headers": ["Aspect", "Fraud", "Misrepresentation"],
        "rows": [
          ["Intent to Deceive", "Present (Mens rea required)", "Absent (Innocent or negligent belief)"],
          ["Belief in Truth", "Maker does not believe statement to be true", "Maker honestly believes statement to be true"],
          ["Damages in Tort", "Yes, damages for deceit can be claimed", "No tort damages (rescission/restitution only)"]
        ]
      }
    ],
    "diagramId": "diag-cnt-fraud-misrep",
    "diagramExplanation": "Custom vector schematic contrasting active fraud with innocent misrepresentation.",
    "misconceptions": [
      {
        "myth": "A seller of land who does not disclose hidden defects in title never commits fraud.",
        "reality": "If the seller actively conceals defects, or fails to disclose material latent title defects required by Section 55(1)(a) TPA, it amounts to fraud."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Assuming Derry v. Peek allowed damages for innocent misrepresentation.",
        "reality": "Derry v. Peek held that without dishonesty, there is NO fraud, even if the statement was made carelessly without reasonable ground.",
        "rule": "Fraud requires absence of honest belief."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-04-13",
        "front": "What does Section 17 of the Contract Act define?",
        "back": "Fraud — intentional deception inducing entry into an agreement.",
        "category": "Fraud"
      },
      {
        "id": "fc-cnt-04-14",
        "front": "Is mere silence as to material facts fraud under Section 17?",
        "back": "No, mere silence is not fraud unless there is a duty to speak or silence is equivalent to speech.",
        "category": "Silence as Fraud"
      },
      {
        "id": "fc-cnt-04-15",
        "front": "What did Derry v. Peek (1889) establish regarding fraud?",
        "back": "Fraud requires proof that a false statement was made knowingly, without belief in truth, or recklessly.",
        "category": "Case Law"
      },
      {
        "id": "fc-cnt-04-16",
        "front": "What are contracts 'Uberrimae Fidei'?",
        "back": "Contracts of utmost good faith (e.g. insurance) where full disclosure of all material facts is legally mandatory.",
        "category": "Disclosure"
      }
    ],
    "sourceReferences": [
      {"title": "Indian Contract Act, 1872", "url": "https://indiacode.nic.in"}
    ]
}

create_concept_file('assets/learning/data/contract/contract-concepts-part1.js', 'CONTRACT_CONCEPTS_PART1', data)
print(f"Contract Part 1 complete with {len(data)} topics!")
