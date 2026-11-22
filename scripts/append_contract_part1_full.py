import json
from concept_helpers import create_concept_file

# Load current Part 1
with open('assets/learning/data/contract/contract-concepts-part1.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('const DATA = ') + len('const DATA = ')
end_idx = text.rfind(';\n\n  global.')
data = json.loads(text[idx:end_idx])

# -------------------------------------------------------------
# CHAPTER 2: CONSIDERATION
# -------------------------------------------------------------
data["top-cnt-02-01"] = {
    "topicId": "top-cnt-02-01",
    "chapterId": "ch-cnt-02",
    "subjectId": "law-contract",
    "title": "Consideration Essentials, Types & Quid Pro Quo (Section 2(d))",
    "subtitle": "The Price for Which the Promise of the Other is Bought",
    "bareActRef": "Indian Contract Act, 1872 — Section 2(d)",
    "learningObjective": "Master the definition of consideration under Section 2(d), distinguish past, present (executed), and future (executory) consideration, and understand adequacy vs sufficiency.",
    "detailedExplanation": """
<h3>1. Statutory Definition: Section 2(d)</h3>
<p>'When, at the desire of the promisor, the promisee or any other person has done or abstained from doing, or does or abstains from doing, or promises to do or to abstain from doing, something, such act or abstinence or promise is called a consideration for the promise.'</p>

<h3>2. The Three Cardinal Essentials of Consideration</h3>
<ol>
  <li><strong>At the Desire of the Promisor:</strong> The act or abstinence must be done at the request or desire of the promisor. Voluntary acts done without the promisor's request do not constitute consideration (<em>Durga Prasad v. Baldeo, 1880</em> — market stalls constructed at Collector's request, not promisor's desire; held: no consideration).</li>
  <li><strong>By the Promisee or Any Other Person:</strong> In India, consideration may move from the promisee OR from any third person (<em>Chinnaya v. Ramayya</em>). This differs fundamentally from English law, where consideration must move only from the promisee.</li>
  <li><strong>Nature of the Act (Past, Present, or Future):</strong>
    <ul>
      <li><strong>Past Consideration:</strong> 'has done or abstained from doing' (Valid in India; invalid at English common law except under Lampleigh v. Brathwait doctrine).</li>
      <li><strong>Present / Executed Consideration:</strong> 'does or abstains from doing' (e.g., cash sale).</li>
      <li><strong>Future / Executory Consideration:</strong> 'promises to do or abstain' (e.g., mutual promises to deliver goods and pay next month).</li>
    </ul>
  </li>
</ol>

<h3>3. Consideration Must Have Value, but Need Not Be Adequate</h3>
<p>Explanation 2 to Section 25 provides: <em>'An agreement to which the consent of the promisor is freely given is not void merely because the consideration is inadequate.'</em> The law does not measure economic equality; even a peppercorn or Rs. 1 is sufficient consideration for a mansion if consent was freely given. Inadequacy of consideration is merely evidence to determine whether consent was caused by undue influence or fraud.</p>
""",
    "quickRevisionPoints": [
      "Section 2(d): Act or abstinence at desire of promisor, moving from promisee or any other person.",
      "Durga Prasad v. Baldeo (1880): Act must be at desire of promisor; Collector's order is not promisor's request.",
      "Past, present, and future consideration are all recognized in India.",
      "Consideration must be real, not illusory; need not be adequate (Explanation 2, s. 25).",
      "Performance of an existing public or legal duty is no consideration (Collins v. Godefroy)."
    ],
    "provisions": [
      {
        "provision": "Section 2(d), Indian Contract Act 1872",
        "title": "Definition of Consideration",
        "description": "When, at the desire of the promisor, the promisee or any other person has done or abstained from doing, or does or abstains from doing, or promises to do or to abstain from doing, something, such act or abstinence or promise is called a consideration for the promise."
      }
    ],
    "definitions": [
      {
        "term": "Quid Pro Quo",
        "definition": "Something for something; the mutual exchange of value which converts a gratuitous promise into a legally binding contract."
      }
    ],
    "ingredients": [
      "Act done at desire of promisor.",
      "Move from promisee or third party.",
      "Past, executed, or executory nature.",
      "Lawful and real in the eyes of law."
    ],
    "exceptions": [
      "Agreements enforceable without consideration under Section 25 (natural love/affection, past voluntary services, time-barred debts)."
    ],
    "examples": [
      {
        "scenario": "A builds market stalls at the request of the District Magistrate. Shopkeepers promise A to pay commission on sales.",
        "application": "Under Durga Prasad v. Baldeo, the construction was not at the shopkeepers' desire; the promise was nudum pactum and unenforceable."
      }
    ],
    "landmarkCases": [
      {
        "case": "Durga Prasad v. Baldeo",
        "citation": "(1880) ILR 3 All 221",
        "year": "1880",
        "bench": "Allahabad High Court",
        "ratio": "The plaintiff constructed a market at the request of the District Collector. The defendant shopkeepers promised to pay commission to plaintiff on sales. Held: Consideration did not move at the desire of the promisors (defendants); the agreement was void for lack of consideration.",
        "impact": "Leading Indian authority establishing that act must be at promisor's desire under Section 2(d)."
      },
      {
        "case": "Currie v. Misa",
        "citation": "(1875) LR 10 Ex 153",
        "year": "1875",
        "bench": "Exchequer Chamber (Lush J)",
        "ratio": "A valuable consideration, in the sense of the law, may consist either in some right, interest, profit, or benefit accruing to the one party, or some forbearance, detriment, loss, or responsibility, given, suffered, or undertaken by the other.",
        "impact": "Classic definition of valuable consideration in Anglo-Indian contract jurisprudence."
      }
    ],
    "comparisonTables": [
      {
        "title": "Indian Law vs English Law on Consideration",
        "headers": ["Aspect", "Indian Law (Section 2(d))", "English Common Law"],
        "rows": [
          ["Source of Consideration", "Promisee or any other person (stranger to consideration valid)", "Must move exclusively from the promisee"],
          ["Past Consideration", "Valid ('has done or abstained')", "Generally invalid (Past consideration is no consideration)"],
          ["Adequacy", "Need not be adequate if consent free (Exp 2 s. 25)", "Must be sufficient, need not be adequate"]
        ]
      }
    ],
    "diagramId": "diag-cnt-agreement-vs-contract",
    "diagramExplanation": "Custom vector schematic showing the flow of consideration at the desire of the promisor.",
    "misconceptions": [
      {
        "myth": "In India, past consideration is void like in England.",
        "reality": "Under Section 2(d), the words 'has done or abstained from doing' expressly recognize past consideration as valid consideration."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Confusing an act done voluntarily with an act done at promisor's desire.",
        "reality": "An act done without request does NOT satisfy Section 2(d); it can only be enforced under Section 25(2) if done voluntarily for the promisor.",
        "rule": "Section 2(d) = At desire; Section 25(2) = Voluntary."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-02-01",
        "front": "Which section of the Indian Contract Act defines Consideration?",
        "back": "Section 2(d).",
        "category": "Consideration"
      },
      {
        "id": "fc-cnt-02-02",
        "front": "What did the Allahabad High Court hold in Durga Prasad v. Baldeo (1880)?",
        "back": "Consideration must move at the desire of the promisor; market construction at Collector's request was not valid consideration.",
        "category": "Landmark Precedents"
      },
      {
        "id": "fc-cnt-02-03",
        "front": "Is past consideration valid under Indian contract law?",
        "back": "Yes, Section 2(d) expressly includes past consideration ('has done or abstained from doing').",
        "category": "Consideration Types"
      },
      {
        "id": "fc-cnt-02-04",
        "front": "Does inadequacy of consideration render an agreement void under Section 25?",
        "back": "No, Explanation 2 to Section 25 states agreement is not void merely because consideration is inadequate.",
        "category": "Adequacy of Consideration"
      }
    ],
    "sourceReferences": [
      {"title": "Pollock & Mulla: Indian Contract Act", "url": "https://archive.org"},
      {"title": "Law of Contract — Avtar Singh", "url": "https://archive.org"}
    ]
}

data["top-cnt-02-02"] = {
    "topicId": "top-cnt-02-02",
    "chapterId": "ch-cnt-02",
    "subjectId": "law-contract",
    "title": "Privity of Contract vs Privity of Consideration & Exceptions",
    "subtitle": "Stranger to Consideration vs Stranger to Contract: The Indian Distinction",
    "bareActRef": "Indian Contract Act, 1872 — Section 2(d) & Common Law Doctrine",
    "learningObjective": "Differentiate between Privity of Contract and Privity of Consideration, analyze Chinnaya v Ramayya, and master the recognized exceptions where a third party can sue.",
    "detailedExplanation": """
<h3>1. Privity of Consideration vs. Privity of Contract</h3>
<ul>
  <li><strong>Privity of Consideration:</strong> The rule that consideration must proceed from the promisee himself. In India, <em>there is NO rule of privity of consideration</em>. Under Section 2(d), consideration may move from 'the promisee or any other person'. A stranger to consideration can maintain an action (<em>Chinnaya v. Ramayya, 1882</em>).</li>
  <li><strong>Privity of Contract:</strong> The rule that only parties to a contract can sue or be sued upon it. A stranger to the contract cannot enforce it even if it was made for his benefit (<em>Tweddle v. Atkinson, 1861</em>; <em>Dunlop Pneumatic Tyre Co. v. Selfridge & Co., 1915</em>; affirmed in India in <em>MC Chacko v. State Bank of Travancore, 1970 SC</em>).</li>
</ul>

<h3>2. Chinnaya v. Ramayya (1882): Stranger to Consideration Can Sue</h3>
<p>An old lady gifted landed property to her daughter (defendant) on the condition that the daughter should pay an annual annuity to the lady's sister (plaintiff). On the same day, the daughter executed an agreement with the sister promising to pay the annuity. Later, the daughter refused to pay, arguing that no consideration moved from the sister. The Madras High Court held: Consideration moved from the mother (gift of property), which was sufficient under Section 2(d) ('or any other person'). The sister could enforce the promise!</p>

<h3>3. Exceptions to Privity of Contract (Where Third Party Can Sue)</h3>
<ol>
  <li><strong>Trust or Charge (Beneficiaries):</strong> Where a trust or specific charge on immovable property is created in favor of a third party, the beneficiary can sue to enforce it (<em>Khwaja Muhammad Khan v. Husaini Begam, 1910 PC</em>).</li>
  <li><strong>Marriage Settlements and Family Arrangements:</strong> Female or minor relatives can enforce provisions made for their maintenance or marriage in family partitions (<em>Daropti v. Jaspat Rai</em>).</li>
  <li><strong>Acknowledgment or Estoppel:</strong> Where a promisor acknowledges to a third party that he holds money for him or pays part of it, he is estopped from denying privity (<em>Devaraja Urs v. Ram Krishniah</em>).</li>
  <li><strong>Covenants Running with Land:</strong> A purchaser of land with notice of restrictive covenants is bound by them (<em>Tulk v. Moxhay</em>).</li>
  <li><strong>Assignee of an Actionable Claim:</strong> Under Transfer of Property Act, an assignee can sue in his own name.</li>
</ol>
""",
    "quickRevisionPoints": [
      "In India, stranger to consideration CAN sue (s. 2(d); Chinnaya v. Ramayya).",
      "Stranger to contract CANNOT sue (Privity of contract: Tweddle v. Atkinson; MC Chacko v. SBT).",
      "Exceptions to privity: Beneficiaries of trust/charge (Khwaja Muhammad Khan), marriage/family settlements, estoppel/acknowledgment, covenants on land.",
      "Khwaja Muhammad Khan v. Husaini Begam (1910 PC): Kharch-i-pandan allowance enforced by bride as beneficiary of charge on property.",
      "MC Chacko v. State Bank of Travancore (1970 SC): Confirmed privity of contract strictly applies in India."
    ],
    "provisions": [
      {
        "provision": "Section 2(d) Words",
        "title": "Stranger to Consideration",
        "description": "When at the desire of the promisor, the promisee or ANY OTHER PERSON has done..."
      }
    ],
    "definitions": [
      {
        "term": "Privity of Contract",
        "definition": "The legal relationship existing between the specific contracting parties which prevents a non-party from suing or being burdened by the agreement."
      }
    ],
    "ingredients": [
      "Presence of valid contractual nexus.",
      "Distinction between payer of consideration and named parties.",
      "Establishment of equitable trust or family partition exception."
    ],
    "exceptions": [
      "Trusts, family settlements, estoppel, and agency."
    ],
    "examples": [
      {
        "scenario": "A father agrees with B's father to pay an allowance (Kharch-i-pandan) to B on her marriage to his son, creating a charge on his estate.",
        "application": "Under Khwaja Muhammad Khan v. Husaini Begam, B, though not a signatory, is the beneficiary of a charge and can sue to recover the allowance."
      }
    ],
    "landmarkCases": [
      {
        "case": "Chinnaya v. Ramayya",
        "citation": "(1882) ILR 4 Mad 137",
        "year": "1882",
        "bench": "Madras High Court (Innes and Kindersley JJ)",
        "ratio": "Consideration under Section 2(d) need not proceed from the promisee; it may move from a third person. A promise by a daughter to pay annuity to her maternal aunt in consideration of a gift from her mother is fully enforceable.",
        "impact": "Monumental Indian precedent establishing that a stranger to consideration can sue."
      },
      {
        "case": "Khwaja Muhammad Khan v. Husaini Begam",
        "citation": "(1910) 37 IA 152",
        "year": "1910",
        "bench": "Privy Council (Rt. Hon. Ameer Ali)",
        "ratio": "The rule in Tweddle v. Atkinson has no application to Indian society where contracts are entered into for the benefit of minors and brides. An agreement creating a charge on property for pin-money (Kharch-i-pandan) of a bride is enforceable by the bride as a beneficiary.",
        "impact": "Leading Privy Council authority creating the trust/beneficiary exception to privity of contract in India."
      },
      {
        "case": "M.C. Chacko v. State Bank of Travancore",
        "citation": "(1970) 1 SCC 858",
        "year": "1970",
        "bench": "Supreme Court of India (Shah J)",
        "ratio": "The Supreme Court held that a person not a party to a contract cannot, subject to certain well-recognized exceptions, enforce the terms of the contract. The doctrine of privity of contract firmly applies in India unless a trust or charge is clearly created.",
        "impact": "Decisive Indian Supreme Court ruling affirming the doctrine of privity of contract."
      }
    ],
    "comparisonTables": [
      {
        "title": "Privity of Contract vs Privity of Consideration",
        "headers": ["Aspect", "Privity of Consideration", "Privity of Contract"],
        "rows": [
          ["Applies in India?", "NO (Stranger to consideration CAN sue)", "YES (Stranger to contract CANNOT sue)"],
          ["Governing Authority", "Section 2(d) ICA; Chinnaya v. Ramayya (1882)", "MC Chacko v. State Bank of Travancore (1970 SC)"],
          ["Meaning", "The person paying consideration must be the promisee", "Only persons who are parties to contract can sue upon it"]
        ]
      }
    ],
    "diagramId": "diag-cnt-agreement-vs-contract",
    "diagramExplanation": "Custom vector schematic contrasting the flow of consideration from a third party vs privity barriers.",
    "misconceptions": [
      {
        "myth": "Because a stranger to consideration can sue, any beneficiary can sue on a contract.",
        "reality": "A stranger to the CONTRACT cannot sue unless he fits into an established exception (trust, family settlement, acknowledgment). Privity of contract still bars strangers."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Citing Tweddle v. Atkinson for the proposition that a stranger to consideration cannot sue in India.",
        "reality": "Tweddle v. Atkinson is English law. In India, Section 2(d) expressly allows consideration to move from 'any other person' (Chinnaya v. Ramayya).",
        "rule": "India: Stranger to consideration CAN sue; Stranger to contract CANNOT."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-02-05",
        "front": "Can a stranger to consideration sue under Indian Contract Law?",
        "back": "Yes, under Section 2(d) and Chinnaya v. Ramayya (1882).",
        "category": "Privity of Consideration"
      },
      {
        "id": "fc-cnt-02-06",
        "front": "What did the Privy Council hold in Khwaja Muhammad Khan v. Husaini Begam (1910)?",
        "back": "A bride, as beneficiary of a charge on property for Kharch-i-pandan, can sue to enforce the agreement even though she was not a party.",
        "category": "Privity Exceptions"
      },
      {
        "id": "fc-cnt-02-07",
        "front": "Which Indian Supreme Court case confirmed that the doctrine of Privity of Contract applies in India?",
        "back": "M.C. Chacko v. State Bank of Travancore (1970).",
        "category": "Privity of Contract"
      },
      {
        "id": "fc-cnt-02-08",
        "front": "What English case established the classical doctrine of Privity of Contract?",
        "back": "Tweddle v. Atkinson (1861) and Dunlop Pneumatic Tyre Co. v. Selfridge (1915).",
        "category": "English Precedents"
      }
    ],
    "sourceReferences": [
      {"title": "Pollock & Mulla: Indian Contract Act", "url": "https://archive.org"}
    ]
}

data["top-cnt-02-03"] = {
    "topicId": "top-cnt-02-03",
    "chapterId": "ch-cnt-02",
    "subjectId": "law-contract",
    "title": "Agreements Without Consideration & Section 25 Exceptions",
    "subtitle": "Ex Nudo Pacto Non Oritur Actio and the Three Statutory Safe Harbors",
    "bareActRef": "Indian Contract Act, 1872 — Section 25",
    "learningObjective": "Master the general rule 'No Consideration, No Contract' (Ex nudo pacto non oritur actio) and the 3 statutory exceptions under Section 25, plus gift and agency.",
    "detailedExplanation": """
<h3>1. The General Rule: Section 25</h3>
<p>'An agreement made without consideration is void.' This codifies the ancient maxim: <strong>Ex nudo pacto non oritur actio</strong> (Out of a bare pact no cause of action arises). A gratuitous promise cannot be legally enforced.</p>

<h3>2. The Three Statutory Exceptions under Section 25</h3>
<p>An agreement without consideration is nevertheless valid and binding if it falls into one of the following three categories:</p>
<ol>
  <li><strong>Section 25(1) — Natural Love and Affection:</strong>
    <ul>
      <li>Must be expressed in <strong>writing</strong>.</li>
      <li>Must be <strong>registered</strong> under the law for registration of documents.</li>
      <li>Must be made on account of <strong>natural love and affection</strong>.</li>
      <li>Must be between parties standing in a <strong>near relation</strong> to each other.</li>
      <li><em>Key Judicial Distinction:</em> Near relationship does not necessarily imply natural love and affection. In <em>Rajlukhy Dabee v. Bhootnath Mookerjee (1900)</em>, a registered written agreement between husband and wife executed after constant quarrels and separation was held void because it was prompted by discord, not love and affection! Contrast with <em>Bhiwa v. Shivaram</em> where reconciliation between brothers made the gift valid.</li>
    </ul>
  </li>
  <li><strong>Section 25(2) — Compensation for Past Voluntary Services:</strong>
    <ul>
      <li>A promise to compensate, wholly or in part, a person who has already <strong>voluntarily done something</strong> for the promisor, or something which the promisor was legally compellable to do (e.g., paying infant's maintenance).</li>
    </ul>
  </li>
  <li><strong>Section 25(3) — Promise to Pay a Time-Barred Debt:</strong>
    <ul>
      <li>A promise to pay, wholly or in part, a debt of which the creditor might have enforced payment but for the law of limitation.</li>
      <li>Must be made in <strong>writing</strong>.</li>
      <li>Must be <strong>signed</strong> by the debtor or his authorized agent.</li>
    </ul>
  </li>
</ol>

<h3>3. Other Statutory Exceptions</h3>
<ul>
  <li><strong>Completed Gifts (Explanation 1, Section 25):</strong> Nothing in Section 25 affects the validity, as between the donor and donee, of any gift actually made (completed transfer).</li>
  <li><strong>Contract of Agency (Section 185):</strong> No consideration is necessary to create an agency.</li>
  <li><strong>Remission / Satisfaction (Section 63):</strong> A promisee may dispense with or remit performance without fresh consideration.</li>
</ul>
""",
    "quickRevisionPoints": [
      "Maxim: Ex nudo pacto non oritur actio — agreement without consideration is void (s. 25).",
      "Section 25(1): Natural love & affection -> Writing + Registered + Near relation + Real love.",
      "Rajlukhy Dabee v. Bhootnath (1900): Registered deed between quarreling spouses void for lack of love & affection.",
      "Section 25(2): Promise to compensate for past voluntary services.",
      "Section 25(3): Promise to pay time-barred debt -> Writing + Signed by debtor/agent.",
      "Other exceptions: Completed gifts (Exp 1), Agency (s. 185), Remission of performance (s. 63)."
    ],
    "provisions": [
      {
        "provision": "Section 25, Indian Contract Act 1872",
        "title": "Agreement Without Consideration Void, Unless...",
        "description": "An agreement made without consideration is void, unless: (1) it is expressed in writing and registered, made on account of natural love and affection between near relations; or (2) is a promise to compensate for past voluntary services; or (3) is a promise in writing signed to pay a debt barred by limitation."
      }
    ],
    "definitions": [
      {
        "term": "Nudum Pactum",
        "definition": "A bare agreement entered into without valuable consideration, creating no legal obligation."
      }
    ],
    "ingredients": [
      "Presence of writing and registration for Section 25(1).",
      "Near relation coupled with genuine affection.",
      "Past services rendered voluntarily for the promisor.",
      "Written signature on time-barred debt promise."
    ],
    "exceptions": [
      "Sections 25(1), 25(2), 25(3), Explanation 1 (gifts), and Section 185 (agency)."
    ],
    "examples": [
      {
        "scenario": "A owes B Rs. 10,000, but the debt is barred by the Limitation Act. A signs a written promise to pay B Rs. 5,000 on account of the debt.",
        "application": "Under Section 25(3), this is an enforceable contract; B can recover Rs. 5,000."
      }
    ],
    "landmarkCases": [
      {
        "case": "Rajlukhy Dabee v. Bhootnath Mookerjee",
        "citation": "(1900) 4 CWN 488",
        "year": "1900",
        "bench": "Calcutta High Court",
        "ratio": "A husband executed a registered written agreement to pay separate residence and maintenance to his wife after constant quarrels. Held: Even though in writing, registered, and between near relations, the agreement was caused by discord, not natural love and affection, and was void for lack of consideration under Section 25(1).",
        "impact": "Classic authority that near relationship does not automatically prove natural love and affection."
      }
    ],
    "comparisonTables": [
      {
        "title": "The Three Section 25 Exceptions Compared",
        "headers": ["Exception", "Writing Required?", "Registration Required?", "Essential Condition"],
        "rows": [
          ["Section 25(1)", "YES (Mandatory)", "YES (Mandatory)", "Natural love and affection between near relations"],
          ["Section 25(2)", "NO (Can be oral)", "NO", "Past services rendered voluntarily for promisor"],
          ["Section 25(3)", "YES (Mandatory)", "NO (Writing & signature only)", "Debt must be time-barred, signed by debtor/agent"]
        ]
      }
    ],
    "diagramId": "diag-cnt-agreement-vs-contract",
    "diagramExplanation": "Custom vector schematic displaying Section 25 general voidness and the 3 statutory safe harbors.",
    "misconceptions": [
      {
        "myth": "A promise to pay a time-barred debt must be registered to be valid.",
        "reality": "Section 25(3) requires ONLY writing and signature; registration is NOT required for a time-barred debt promise (registration is required only under Section 25(1))."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing Section 25(2) applies if services were rendered at the request of the promisor.",
        "reality": "If services were rendered at promisor's request, it falls under Section 2(d) (past consideration)! Section 25(2) is reserved for services rendered VOLUNTARILY.",
        "rule": "At request = Section 2(d); Voluntary = Section 25(2)."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-02-09",
        "front": "What are the four essentials of Section 25(1) (natural love and affection)?",
        "back": "Expressed in writing, registered under law, made on account of natural love and affection, and between near relations.",
        "category": "Section 25"
      },
      {
        "id": "fc-cnt-02-10",
        "front": "What did the Calcutta High Court decide in Rajlukhy Dabee v. Bhootnath Mookerjee?",
        "back": "A registered agreement between quarreling spouses was void under s. 25(1) because it was prompted by discord, not natural love and affection.",
        "category": "Landmark Precedents"
      },
      {
        "id": "fc-cnt-02-11",
        "front": "Does a promise to pay a time-barred debt under Section 25(3) require registration?",
        "back": "No, it requires writing and signature by debtor or his agent, but not registration.",
        "category": "Time-Barred Debts"
      },
      {
        "id": "fc-cnt-02-12",
        "front": "Does creation of an agency require consideration under the Contract Act?",
        "back": "No, Section 185 states that no consideration is necessary to create an agency.",
        "category": "Agency Consideration"
      }
    ],
    "sourceReferences": [
      {"title": "Pollock & Mulla: Indian Contract Act", "url": "https://archive.org"}
    ]
}

create_concept_file('assets/learning/data/contract/contract-concepts-part1.js', 'CONTRACT_CONCEPTS_PART1', data)
print(f"Contract Part 1 updated with Chapter 2: {len(data)} topics!")
