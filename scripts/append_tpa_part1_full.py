import json
from concept_helpers import create_concept_file

with open('assets/learning/data/tpa/tpa-concepts-part1.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('const DATA = ') + len('const DATA = ')
end_idx = text.rfind(';\n\n  global.')
data = json.loads(text[idx:end_idx])

# -------------------------------------------------------------
# CHAPTER 2: SPECIFIC RULES OF TRANSFER
# -------------------------------------------------------------
data["top-tpa-02-01"] = {
    "topicId": "top-tpa-02-01",
    "chapterId": "ch-tpa-02",
    "subjectId": "law-tpa",
    "title": "Conditions Restraining Alienation: Absolute vs Partial (Section 10)",
    "subtitle": "The Doctrine of Free Alienation and the Distinction Between Void and Valid Restraints",
    "bareActRef": "Transfer of Property Act, 1882 — Sections 10, 11, 12",
    "learningObjective": "Master Section 10 rule on conditions restraining alienation, absolute vs partial restraints, Section 11 repugnant conditions, and Section 12 insolvency restraints.",
    "detailedExplanation": """
<h3>1. Section 10: Rule Against Absolute Restraint on Alienation</h3>
<p>'Where property is transferred subject to a condition or limitation absolutely restraining the transferee or any person claiming under him from parting with or disposing of his interest in the property, the condition or limitation is <strong>void</strong>.'</p>
<ul>
  <li><strong>The Transfer Remains Valid:</strong> Only the restraining condition is void; the transferee takes the property as an absolute, unencumbered owner!</li>
  <li><strong>Absolute vs. Partial Restraint:</strong>
    <ul>
      <li><strong>Absolute Restraint (Void):</strong> Completely deprives the transferee of the power of alienation (e.g., 'You shall never sell to anyone in the world').</li>
      <li><strong>Partial Restraint (Valid):</strong> Substantially leaves the power of alienation intact, imposing only limited, reasonable restrictions (e.g., a pre-emption clause giving first refusal to family members at fair market value; <em>Muhammad Raza v. Abbas Bandi Bibi, 1932 PC</em>).</li>
    </ul>
  </li>
  <li><strong>Two Statutory Exceptions to Section 10:</strong>
    <ol>
      <li><strong>Lease:</strong> A condition in a lease that the lessee shall not sub-let or assign without lessor's consent is valid and enforceable.</li>
      <li><strong>Married Women:</strong> A condition that property transferred to or for the benefit of a married woman (not being a Hindu, Muhammadan, or Buddhist) shall not be alienated during her coverture.</li>
    </ol>
  </li>
</ul>

<h3>2. Section 11: Restriction Repugnant to Interest Created</h3>
<p>Where, on a transfer of property, an absolute interest is created, but the terms of the transfer direct that such interest shall be applied or enjoyed by the transferee in a particular manner, the transferee is entitled to receive and dispose of such interest as if there were no such direction (the condition is void for repugnancy). Exception: Negative covenants for the beneficial enjoyment of adjacent land of the transferor (doctrine of <em>Tulk v. Moxhay</em>).</p>
""",
    "quickRevisionPoints": [
      "Section 10: Absolute restraint on alienation is VOID; the transfer itself remains VALID.",
      "Partial restraint is valid if reasonable (e.g. pre-emption at market rate; Muhammad Raza v. Abbas Bandi).",
      "Two exceptions to Section 10: Lease conditions against sub-letting, and married non-Hindu/Muslim women.",
      "Section 11: Conditions restricting mode of enjoyment of an absolute estate are void for repugnancy.",
      "Section 12: Condition terminating interest on insolvency or attempted alienation is void.",
      "Tulk v. Moxhay: Restrictive covenants for beneficial enjoyment of adjoining land are valid exception to Section 11."
    ],
    "provisions": [
      {
        "provision": "Section 10, TPA 1882",
        "title": "Condition Restraining Alienation",
        "description": "Where property is transferred subject to a condition absolutely restraining the transferee from parting with or disposing of his interest, the condition is void, except in leases and married women settlements."
      },
      {
        "provision": "Section 11, TPA 1882",
        "title": "Restriction Repugnant to Interest Created",
        "description": "Where an absolute interest is created, any direction that it shall be applied or enjoyed in a particular manner is void, unless made for the beneficial enjoyment of adjoining property."
      }
    ],
    "definitions": [
      {
        "term": "Repugnant Condition",
        "definition": "A condition in a deed which is completely contradictory and hostile to the nature of the absolute estate granted."
      }
    ],
    "ingredients": [
      "Conveyance of an interest in property.",
      "Imposition of restraining condition.",
      "Assessment of absolute vs partial character of restraint."
    ],
    "exceptions": [
      "Leases (covenants against sub-letting) and settlements on married women."
    ],
    "examples": [
      {
        "scenario": "A sells a house to B with a clause: 'B shall never sell this house to anyone outside A's caste'.",
        "application": "Under Section 10, this is an absolute restraint on alienation; the restriction is void, and B can sell to anyone."
      }
    ],
    "landmarkCases": [
      {
        "case": "Muhammad Raza v. Abbas Bandi Bibi",
        "citation": "(1932) 59 IA 236",
        "year": "1932",
        "bench": "Privy Council (Sir George Lowndes)",
        "ratio": "A condition in a compromise restricting alienation to members of the family was held to be a partial restraint, not absolute, and was therefore valid and enforceable under Section 10.",
        "impact": "Classic authority on the validity of partial restraints under Section 10."
      },
      {
        "case": "Bhavani Amma Kanakadevi v. CSI Dakshina Kerala Maha Idavaka",
        "citation": "AIR 2008 Ker 38",
        "year": "2008",
        "bench": "Kerala High Court",
        "ratio": "A clause in a sale deed prohibiting the buyer from alienating the land for any purpose other than construction of a church was held void under Section 10 as an absolute restraint on alienation.",
        "impact": "Affirmed the strict nullity of absolute restraints on alienation in modern Indian conveyancing."
      }
    ],
    "comparisonTables": [
      {
        "title": "Section 10 vs Section 11",
        "headers": ["Aspect", "Section 10 (Restraint on Alienation)", "Section 11 (Restriction on Enjoyment)"],
        "rows": [
          ["Target of Restraint", "Power to sell, gift, mortgage, or transfer", "Manner of personal user or enjoyment of property"],
          ["Interest Involved", "Applies to ANY interest (limited or absolute)", "Applies strictly to ABSOLUTE interests"],
          ["Exceptions", "Leases & married women", "Negative covenants for adjoining land (Tulk v. Moxhay)"]
        ]
      }
    ],
    "diagramId": "diag-tpa-transferability-s6",
    "diagramExplanation": "Custom vector schematic displaying the boundary between void absolute restraints and valid partial restraints.",
    "misconceptions": [
      {
        "myth": "If a deed contains an absolute restraint on alienation, the entire deed and sale become void.",
        "reality": "Only the condition is void; the transfer itself stands, and the buyer takes the property absolutely free from the condition."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing a lessor cannot prohibit a tenant from sub-letting.",
        "reality": "Leases are expressly exempted from Section 10. A clause in a lease prohibiting assignment or sub-letting is completely valid.",
        "rule": "Lease sub-letting ban = Valid under Section 10 Exception."
      }
    ],
    "flashcards": [
      {
        "id": "fc-tpa-02-01",
        "front": "What is the legal effect of an absolute restraint on alienation under Section 10?",
        "back": "The condition is VOID, but the transfer remains completely VALID.",
        "category": "Section 10"
      },
      {
        "id": "fc-tpa-02-02",
        "front": "What are the two statutory exceptions to Section 10?",
        "back": "1. Leases (conditions against sub-letting); 2. Property settled on married women.",
        "category": "Section 10 Exceptions"
      },
      {
        "id": "fc-tpa-02-03",
        "front": "What did the Privy Council hold in Muhammad Raza v. Abbas Bandi Bibi (1932)?",
        "back": "A condition restricting alienation to members of a specific family is a partial restraint and is valid.",
        "category": "Partial Restraints"
      },
      {
        "id": "fc-tpa-02-04",
        "front": "What does Section 11 of the Transfer of Property Act govern?",
        "back": "Restrictions repugnant to the interest created (invalidating conditions that dictate how an absolute owner must enjoy property).",
        "category": "Section 11"
      }
    ],
    "sourceReferences": [
      {"title": "Mulla: The Transfer of Property Act", "url": "https://archive.org"}
    ]
}

data["top-tpa-02-02"] = {
    "topicId": "top-tpa-02-02",
    "chapterId": "ch-tpa-02",
    "subjectId": "law-tpa",
    "title": "Transfer for Benefit of Unborn Persons & Prior Life Estate (Section 13)",
    "subtitle": "The Double Mechanism: Creation of Prior Interest and Absolute Remainder",
    "bareActRef": "Transfer of Property Act, 1882 — Section 13",
    "learningObjective": "Master Section 13 rules for transferring property for the benefit of an unborn person, the mandatory creation of a prior life interest, and the requirement of absolute interest.",
    "detailedExplanation": """
<h3>1. The Problem: Direct Transfer to Unborn Person is Impossible</h3>
<p>Under Section 5, a transfer of property can be made only between <strong>living persons</strong> (inter vivos). An unborn person is not a living person; therefore, property cannot be transferred directly to an unborn child. Section 13 creates the only legal mechanism to benefit an unborn person.</p>

<h3>2. Section 13: The Statutory Mechanism</h3>
<p>'Where, on a transfer of property, an interest therein is created for the benefit of a person not in existence at the date of the transfer, subject to a <strong>prior interest</strong> created by the same transfer, the interest created for the benefit of such person shall not take effect, unless it extends to the <strong>whole of the remaining interest</strong> of the transferor in the property.'</p>

<h3>3. The Three Cardinal Essentials of Section 13</h3>
<ol>
  <li><strong>No Direct Transfer:</strong> Property must be transferred first to a living person (the life estate holder) to sustain the estate until the unborn person is born.</li>
  <li><strong>Prior Life Interest:</strong> A prior interest must be created by the <em>same transaction</em> in favor of a living person. There can be successive life estates to living persons, but the unborn person must come into existence before the termination of the last prior life estate.</li>
  <li><strong>Whole of Remaining Interest (Absolute Estate):</strong> The transfer to the unborn person MUST be of the <strong>entire absolute interest</strong> of the transferor. A life interest cannot be given to an unborn person! A life estate to an unborn person followed by another remainder is void ab initio.</li>
</ol>

<h3>4. English Law Comparison: Doctrine of Double Possibilities</h3>
<p>In England, the old rule in <em>Whitby v. Mitchell</em> prohibited a life estate to an unborn person followed by an estate to the child of that unborn person (double possibility). Section 13 in India goes further: it prohibits ANY life interest to an unborn person; the unborn must get the absolute estate.</p>
""",
    "quickRevisionPoints": [
      "Property cannot be transferred directly to an unborn person under Section 5.",
      "Section 13 requires two things: (1) Prior interest to a living person, (2) Whole remaining interest (absolute estate) to the unborn.",
      "A life interest can NEVER be given to an unborn person.",
      "The unborn child must come into existence before the expiration of the prior life estate.",
      "If the transfer to the unborn fails under Section 13, any subsequent interest also fails under Section 16."
    ],
    "provisions": [
      {
        "provision": "Section 13, TPA 1882",
        "title": "Transfer for Benefit of Unborn Person",
        "description": "Where an interest is created for the benefit of an unborn person, subject to a prior interest created by the same transfer, it shall not take effect unless it extends to the whole of the remaining interest of the transferor."
      }
    ],
    "definitions": [
      {
        "term": "Prior Interest",
        "definition": "An intervening estate (usually a life interest) conferred upon a living person to hold the legal title until the unborn beneficiary comes into existence."
      }
    ],
    "ingredients": [
      "Creation of prior life estate in living person.",
      "Conferment of ultimate interest on unborn child.",
      "Conferment of absolute, whole remaining interest.",
      "Birth of unborn before termination of prior estate."
    ],
    "exceptions": [
      "If the child is in the mother's womb at the expiration of the life estate, it is treated as born alive under the nasciturus fiction."
    ],
    "examples": [
      {
        "scenario": "A transfers Blackacre to B for life, and after B's death to B's unborn eldest son for life, and after his death to C absolutely.",
        "application": "Under Section 13, the transfer to B's unborn son is void because it gives him only a life interest instead of the whole remaining interest; C's interest also fails under Section 16."
      }
    ],
    "landmarkCases": [
      {
        "case": "Girish Dutt v. Data Din",
        "citation": "AIR 1934 Oudh 35",
        "year": "1934",
        "bench": "Oudh Chief Court",
        "ratio": "A gift of property to a female for life, and after her death to her unborn son for life, and then to others was held completely void under Section 13, because the transfer to the unborn person was not of the whole remaining interest.",
        "impact": "Classic authority on the invalidity of creating a life estate in favor of an unborn person."
      }
    ],
    "comparisonTables": [
      {
        "title": "Valid vs Void Transfers to Unborn Persons",
        "headers": ["Transfer Terms", "Validity", "Reason under Section 13"],
        "rows": [
          ["To A for life, remainder to A's unborn son absolutely", "VALID", "Prior life estate in living person + whole remaining interest to unborn"],
          ["Directly to A's unborn son without prior life estate", "VOID", "Violates Section 5 (no living person to take immediately)"],
          ["To A for life, remainder to A's unborn son for life, then to C", "VOID", "Violates Section 13 (unborn given only life interest, not whole interest)"]
        ]
      }
    ],
    "diagramId": "diag-tpa-perpetuity-s14",
    "diagramExplanation": "Custom vector schematic illustrating the two-stage structure of Section 13 and the perpetuity boundary.",
    "misconceptions": [
      {
        "myth": "A transfer can be made directly to an unborn child if a trustee is appointed.",
        "reality": "Even through a trust, the property must vest in the living trustee as a prior interest; Section 13 principles must be strictly satisfied."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Assuming an unborn person can be given a life interest if someone else gets the absolute estate later.",
        "reality": "Section 13 strictly prohibits giving a limited or life interest to an unborn person. The unborn MUST receive the entire absolute estate.",
        "rule": "Unborn must get whole remaining interest."
      }
    ],
    "flashcards": [
      {
        "id": "fc-tpa-02-05",
        "front": "What two statutory requirements must be fulfilled under Section 13 to transfer property to an unborn person?",
        "back": "1. Creation of a prior interest in a living person; 2. Transfer of the whole remaining interest (absolute estate) to the unborn person.",
        "category": "Section 13"
      },
      {
        "id": "fc-tpa-02-06",
        "front": "Can a life interest be created in favor of an unborn person under Indian law?",
        "back": "No, a life interest to an unborn person is completely void under Section 13.",
        "category": "Unborn Persons"
      },
      {
        "id": "fc-tpa-02-07",
        "front": "What was held in Girish Dutt v. Data Din (1934)?",
        "back": "A transfer giving a life estate to an unborn child followed by a gift over was void under Section 13.",
        "category": "Landmark Precedents"
      },
      {
        "id": "fc-tpa-02-08",
        "front": "By when must the unborn person come into existence?",
        "back": "Before the termination of the prior life estate.",
        "category": "Timing of Birth"
      }
    ],
    "sourceReferences": [
      {"title": "Mulla: The Transfer of Property Act", "url": "https://archive.org"}
    ]
}

data["top-tpa-02-03"] = {
    "topicId": "top-tpa-02-03",
    "chapterId": "ch-tpa-02",
    "subjectId": "law-tpa",
    "title": "Rule Against Perpetuity & Accumulation of Income (Sections 14, 17)",
    "subtitle": "The Maximum Time-Limit for Tying Up Property: Life in Being + Minority",
    "bareActRef": "Transfer of Property Act, 1882 — Sections 14, 15, 16, 17, 18",
    "learningObjective": "Master the Rule Against Perpetuity under Section 14, calculate the perpetuity period, and understand the Section 17 rules on accumulation of income.",
    "detailedExplanation": """
<h3>1. The Rule Against Perpetuity: Section 14</h3>
<p>'No transfer of property can operate to create an interest which is to take effect after the lifetime of one or more persons living at the date of such transfer, and the minority of some person who shall be in existence at the expiration of that period, to whom, if he attains full age, the interest created is to belong.'</p>
<p><strong>The Maximum Statutory Period of Perpetuity in India:</strong></p>
<p><code>Maximum Period = Life (or Lives) in Being + Period of Gestation (Actual) + Minority of Beneficiary (18 Years)</code></p>
<ul>
  <li><strong>Life in Being:</strong> The person or persons must be alive at the date of the transfer.</li>
  <li><strong>Minority:</strong> In India, minority is strictly <strong>18 years</strong> (under Indian Majority Act 1875). It is NOT a gross period of 21 years (as in English law). In India, the 18-year period must be tied to the <em>actual minority</em> of the unborn beneficiary; a gross term of years in the air is void!</li>
  <li><strong>Gestation Period:</strong> The actual period of pregnancy (usually 9 months) during which the beneficiary is in the womb.</li>
</ul>

<h3>2. Failure of Prior Interest: Section 16</h3>
<p>Where, by reason of any of the rules contained in Sections 13 and 14, an interest created for the benefit of a person fails, any interest created in the same transaction and intended to take effect after or upon failure of such prior interest also <strong>fails completely</strong>.</p>

<h3>3. Direction for Accumulation of Income: Section 17</h3>
<p>A direction that the income arising from property shall be accumulated is void, <strong>except</strong> for a maximum period of:</p>
<ol>
  <li>The life of the transferor, OR</li>
  <li>A period of <strong>eighteen years</strong> from the date of the transfer.</li>
</ol>
<p><strong>Three Exceptions where Accumulation Beyond 18 Years is Valid:</strong></p>
<ul>
  <li>Payment of the debts of the transferor or any other person.</li>
  <li>Provision for portions for children or remoter issue of transferor.</li>
  <li>Preservation or maintenance of the property transferred.</li>
</ul>

<h3>4. Exemption for Public Charities: Section 18</h3>
<p>Sections 14, 16, and 17 do NOT apply to transfers of property for the benefit of the public in the advancement of religion, knowledge, commerce, health, safety, or any other object beneficial to mankind.</p>
""",
    "quickRevisionPoints": [
      "Section 14 Formula: Life in being + gestation period + minority (18 years) of unborn person.",
      "India allows minority of 18 years tied to a person, NOT a gross period of 21 years in gross (unlike England).",
      "Section 16: Failure of prior interest under ss. 13/14 causes subsequent remainder to fail automatically.",
      "Section 17: Accumulation of income allowed only for life of transferor OR 18 years.",
      "Three exceptions to accumulation: Payment of debts, portions for children, preservation of property.",
      "Section 18: Public charity, religion, and education are completely exempt from the rule against perpetuity."
    ],
    "provisions": [
      {
        "provision": "Section 14, TPA 1882",
        "title": "Rule Against Perpetuity",
        "description": "No transfer can create an interest taking effect after the lifetime of one or more persons living at the date of transfer and the minority of some person in existence at the expiration of that period."
      },
      {
        "provision": "Section 17, TPA 1882",
        "title": "Direction for Accumulation",
        "description": "Direction to accumulate income is void except for the life of the transferor or 18 years from transfer, with exceptions for debts, portions, and preservation."
      }
    ],
    "definitions": [
      {
        "term": "Perpetuity",
        "definition": "An inalienable tying up of property which prevents it from being freely circulated in commerce beyond the legal period permitted by law."
      }
    ],
    "ingredients": [
      "Life in being at date of transfer.",
      "Actual period of gestation.",
      "Minority of 18 years of the unborn beneficiary.",
      "Vesting within the statutory time envelope."
    ],
    "exceptions": [
      "Public charities, religious endowments, and personal covenants under Section 18."
    ],
    "examples": [
      {
        "scenario": "A transfers property to B for life, remainder to B's unborn son when he attains the age of 25 years.",
        "application": "Under Section 14, vesting is postponed beyond the age of minority (18 years) to 25 years. The transfer to the unborn son violates the rule against perpetuity and is void."
      }
    ],
    "landmarkCases": [
      {
        "case": "R.K. Kempraj v. M/s. Burton Son & Co.",
        "citation": "(1969) 2 SCC 594",
        "year": "1969",
        "bench": "Supreme Court of India (Grover J)",
        "ratio": "The rule against perpetuity applies to transfers of proprietary interests in property; it does not apply to personal contracts or covenants for renewal of leases.",
        "impact": "Classic authority that personal covenants and renewal clauses do not attract Section 14."
      }
    ],
    "comparisonTables": [
      {
        "title": "Perpetuity Period: Indian Law vs English Law",
        "headers": ["Aspect", "Indian Law (Section 14)", "English Common Law"],
        "rows": [
          ["Life in Being", "Lives of persons living at date of transfer", "Lives in being at creation of interest"],
          ["Subsequent Period", "Actual minority of beneficiary (18 years)", "Gross period of 21 years (whether a minor exists or not)"],
          ["Gestation Period", "Actual period of gestation (if any)", "Actual period of gestation"]
        ]
      }
    ],
    "diagramId": "diag-tpa-perpetuity-s14",
    "diagramExplanation": "Custom vector schematic displaying the timeline envelope of Life in Being + Gestation + Minority under Section 14.",
    "misconceptions": [
      {
        "myth": "In India, property can be tied up for a flat period of 21 years after lives in being.",
        "reality": "The 21-year gross period is English law. In India, Section 14 strictly limits the period to 18 years (minority) tied to an existing person."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing a direction to accumulate income for payment of debts is limited to 18 years.",
        "reality": "Payment of debts is an express exception under Section 17(2)(i); accumulation for debt payment can exceed 18 years.",
        "rule": "Debt accumulation can exceed 18 years."
      }
    ],
    "flashcards": [
      {
        "id": "fc-tpa-02-09",
        "front": "What is the maximum period permitted by the Rule Against Perpetuity under Section 14 in India?",
        "back": "Life in being + actual period of gestation + minority (18 years) of the unborn beneficiary.",
        "category": "Perpetuity Formula"
      },
      {
        "id": "fc-tpa-02-10",
        "front": "What is the maximum permissible period for accumulation of income under Section 17?",
        "back": "Life of the transferor OR a period of 18 years from the date of transfer.",
        "category": "Accumulation"
      },
      {
        "id": "fc-tpa-02-11",
        "front": "Are religious and charitable transfers subject to the Rule Against Perpetuity?",
        "back": "No, Section 18 completely exempts transfers for the benefit of the public in religion, knowledge, or charity.",
        "category": "Section 18"
      },
      {
        "id": "fc-tpa-02-12",
        "front": "Does Section 14 apply to an agreement to renew a lease?",
        "back": "No, R.K. Kempraj (1969 SC) held that Section 14 applies to property interests, not personal covenants.",
        "category": "Case Law"
      }
    ],
    "sourceReferences": [
      {"title": "Mulla: The Transfer of Property Act", "url": "https://archive.org"}
    ]
}

# -------------------------------------------------------------
# CHAPTER 3: VESTED AND CONTINGENT INTERESTS
# -------------------------------------------------------------
data["top-tpa-03-01"] = {
    "topicId": "top-tpa-03-01",
    "chapterId": "ch-tpa-03",
    "subjectId": "law-tpa",
    "title": "Vested Interest vs Contingent Interest (Sections 19, 21)",
    "subtitle": "Immediate Proprietary Ownership vs Uncertain Conditional Expectancy",
    "bareActRef": "Transfer of Property Act, 1882 — Sections 19, 20, 21",
    "learningObjective": "Master Section 19 vested interest, Section 21 contingent interest, heritability, transferability, and attachment rules.",
    "detailedExplanation": """
<h3>1. Vested Interest Defined: Section 19</h3>
<p>'Where, on a transfer of property, an interest therein is created in favour of a person without specifying the time when it is to take effect, or in terms specifying that it is to take effect forthwith or on the happening of an event which <strong>must happen</strong>, such interest is <strong>vested</strong>, unless a contrary intention appears.'</p>
<ul>
  <li><strong>Present Fixed Right:</strong> An immediate right to present or future enjoyment.</li>
  <li><strong>Certainty of Event:</strong> Even if enjoyment is postponed to a future date, if the event is bound to happen (e.g., death of a life-tenant), the interest is vested!</li>
  <li><strong>Heritable and Alienable:</strong> A vested interest is not defeated by the death of the transferee before obtaining possession; it passes to his legal heirs (Section 19). It can be attached and sold in execution of a decree.</li>
</ul>

<h3>2. Contingent Interest Defined: Section 21</h3>
<p>'Where, on a transfer of property, an interest therein is created in favour of a person to take effect only on the happening of a specified <strong>uncertain event</strong>, or if a specified uncertain event shall not happen, such person acquires thereby a <strong>contingent interest</strong> in the property.'</p>
<ul>
  <li><strong>Mere Expectancy:</strong> Dependent on an event which may or may not happen (e.g., attaining age 21, marrying a particular person).</li>
  <li><strong>Effect of Death:</strong> If the transferee dies before the contingency happens, the interest lapses and fails; nothing passes to his heirs (unless the condition is merely collateral).</li>
  <li><strong>Transferable but Speculative:</strong> Can be transferred, but transferee takes subject to the same contingency.</li>
</ul>

<h3>3. Statutory Presumption in Favor of Vesting</h3>
<p>The law favors vesting. Under Explanation to Section 19, an interest is not contingent merely because:</p>
<ol>
  <li>Enjoyment of property is postponed.</li>
  <li>A prior interest in the same property is given to another person.</li>
  <li>Income is directed to be accumulated until the time of enjoyment.</li>
  <li>A conditional provision for divesting is attached.</li>
</ol>
""",
    "quickRevisionPoints": [
      "Section 19: Vested interest = takes effect forthwith or on event that MUST happen (e.g. death).",
      "Vested interest is HERITABLE (passes to heirs on death before possession) and ATTACHABLE.",
      "Section 21: Contingent interest = depends on an UNCERTAIN future event (e.g. attaining age 25).",
      "Contingent interest is NOT heritable if transferee dies before contingency occurs.",
      "Law favors vesting; postponement of enjoyment does not make an interest contingent (Explanation s. 19).",
      "Upon happening of the contingency, a contingent interest matures into a vested interest."
    ],
    "provisions": [
      {
        "provision": "Section 19, TPA 1882",
        "title": "Vested Interest Defined",
        "description": "An interest created without specifying time, or specifying it to take effect forthwith, or on an event which must happen, is a vested interest."
      },
      {
        "provision": "Section 21, TPA 1882",
        "title": "Contingent Interest Defined",
        "description": "An interest created to take effect only on the happening of a specified uncertain event, or if a specified uncertain event shall not happen, is a contingent interest."
      }
    ],
    "definitions": [
      {
        "term": "Vested in Interest vs Vested in Possession",
        "definition": "Vested in interest means present fixed title; vested in possession means present actual physical enjoyment."
      }
    ],
    "ingredients": [
      "Determination of event certainty (inevitable vs uncertain).",
      "Presumption in favor of early vesting.",
      "Heritability analysis upon premature death."
    ],
    "exceptions": [
      "A condition of attaining a certain age makes the interest contingent until that age is reached (Section 21)."
    ],
    "examples": [
      {
        "scenario": "A transfers an estate to B for life, and after B's death to C. C dies during B's lifetime.",
        "application": "C had a Vested Interest (B's death is an event that must happen). Upon C's death, the estate passes to C's legal heirs, who will take possession when B dies."
      }
    ],
    "landmarkCases": [
      {
        "case": "Rajes Kanta Roy v. Shanti Debi",
        "citation": "AIR 1957 SC 255",
        "year": "1957",
        "bench": "Supreme Court of India (Jagannadhadas J)",
        "ratio": "The Supreme Court laid down the classic test: if the event on which performance depends is certain to happen, the interest is vested; if uncertain, contingent. A provision for payment of monthly maintenance out of estate was held to be a vested interest.",
        "impact": "Leading Indian authority on distinguishing vested from contingent interests."
      }
    ],
    "comparisonTables": [
      {
        "title": "Vested Interest vs Contingent Interest",
        "headers": ["Aspect", "Vested Interest (Section 19)", "Contingent Interest (Section 21)"],
        "rows": [
          ["Condition of Vesting", "Forthwith or on an event that MUST happen (Certain)", "Only on an event that may or may not happen (Uncertain)"],
          ["Heritability", "Fully HERITABLE; passes to heirs on death", "Generally NOT heritable if transferee dies before event"],
          ["Attachment in Execution", "Can be attached and sold in execution of decree", "Cannot be attached in execution (mere expectancy; s. 60 CPC)"],
          ["Nature of Right", "Present proprietary right", "Mere prospective chance of acquiring property"]
        ]
      }
    ],
    "diagramId": "diag-tpa-vested-contingent",
    "diagramExplanation": "Custom vector schematic illustrating the branching paths of vested certainty vs contingent expectancy.",
    "misconceptions": [
      {
        "myth": "Because a person cannot immediately enjoy physical possession, his interest must be contingent.",
        "reality": "Explanation to Section 19 clarifies that mere postponement of possession does not prevent an interest from being vested."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Classifying a transfer to take effect on the death of a living person as contingent.",
        "reality": "Death is an event that MUST happen. Therefore, an interest to take effect on someone's death is a VESTED interest.",
        "rule": "Death = Event that must happen -> Vested Interest."
      }
    ],
    "flashcards": [
      {
        "id": "fc-tpa-03-01",
        "front": "What defines a Vested Interest under Section 19?",
        "back": "An interest taking effect forthwith, or on the happening of an event which MUST happen.",
        "category": "Vested Interest"
      },
      {
        "id": "fc-tpa-03-02",
        "front": "Is a vested interest defeated if the transferee dies before obtaining possession?",
        "back": "No, it is heritable and passes to the transferee's legal heirs.",
        "category": "Heritability"
      },
      {
        "id": "fc-tpa-03-03",
        "front": "What defines a Contingent Interest under Section 21?",
        "back": "An interest taking effect only on the happening or non-happening of a specified UNCERTAIN event.",
        "category": "Contingent Interest"
      },
      {
        "id": "fc-tpa-03-04",
        "front": "What did the Supreme Court hold in Rajes Kanta Roy v. Shanti Debi (1957)?",
        "back": "If the event must happen, the interest is vested; if the event is uncertain, it is contingent.",
        "category": "Landmark Precedents"
      }
    ],
    "sourceReferences": [
      {"title": "Mulla: The Transfer of Property Act", "url": "https://archive.org"}
    ]
}

data["top-tpa-03-02"] = {
    "topicId": "top-tpa-03-02",
    "chapterId": "ch-tpa-03",
    "subjectId": "law-tpa",
    "title": "Conditional Transfers: Condition Precedent vs Subsequent (Sections 25–34)",
    "subtitle": "Acquisition and Divesting of Estates: Substantial vs Strict Compliance",
    "bareActRef": "Transfer of Property Act, 1882 — Sections 25, 26, 27, 28, 29, 31",
    "learningObjective": "Master Section 25 void conditions, compare Condition Precedent (s. 26: substantial compliance) with Condition Subsequent (s. 29: strict compliance), and understand conditional limitations (s. 28).",
    "detailedExplanation": """
<h3>1. Void Conditions: Section 25</h3>
<p>An interest created on a transfer of property dependent upon a condition fails if the fulfillment of the condition is:</p>
<ul>
  <li>Impossible (e.g., walking 100 miles in an hour).</li>
  <li>Forbidden by law.</li>
  <li>Defeats the provisions of any law.</li>
  <li>Fraudulent, or involves injury to person or property.</li>
  <li>Immoral or opposed to public policy (e.g., condition requiring a woman to desert her husband).</li>
</ul>

<h3>2. Condition Precedent vs. Condition Subsequent</h3>
<ol>
  <li><strong>Condition Precedent (Section 26):</strong> A condition which must be fulfilled <em>before</em> the estate can vest in the transferee.
    <ul>
      <li><strong>Doctrine of Substantial Compliance (Section 26):</strong> Where the condition precedent is satisfied <strong>substantially</strong>, it is deemed to have been fulfilled! (e.g., transfer on condition of marrying with consent of parents; father dies; consent of mother obtained; held: substantially fulfilled).</li>
    </ul>
  </li>
  <li><strong>Condition Subsequent (Sections 28, 29, 31):</strong> A condition by which an already vested estate is defeated, divested, or extinguished upon the happening or non-happening of a future event.
    <ul>
      <li><strong>Strict Compliance Required (Section 29):</strong> A condition subsequent is strictly construed because the law abhors forfeiture. It must be fulfilled <strong>strictly</strong> according to its terms, otherwise the estate is not divested!</li>
    </ul>
  </li>
</ol>

<h3>3. Conditional Limitation: Section 28</h3>
<p>On a transfer of property, an interest may be created to accrue to any person with the condition superadded that in case a specified uncertain event shall happen, such interest shall pass to another person (an estate shifted from B to C on a contingency).</p>
""",
    "quickRevisionPoints": [
      "Section 25: Condition is void if impossible, unlawful, fraudulent, injurious, or immoral.",
      "Condition Precedent: Must be fulfilled before estate vests; SUBSTANTIAL compliance suffices (s. 26).",
      "Condition Subsequent: Divests an already vested estate; STRICT compliance required (s. 29).",
      "Law favors vesting and abhors forfeiture; therefore condition precedent is liberal, condition subsequent strict.",
      "Section 28: Conditional limitation shifts estate to another person upon happening of event.",
      "Section 31: Condition that estate shall cease on specified event."
    ],
    "provisions": [
      {
        "provision": "Section 26, TPA 1882",
        "title": "Fulfillment of Condition Precedent",
        "description": "Where the terms of a transfer of property impose a condition to be fulfilled before a person can take an interest in the property, the condition shall be deemed to have been fulfilled if it has been substantially complied with."
      },
      {
        "provision": "Section 29, TPA 1882",
        "title": "Fulfillment of Condition Subsequent",
        "description": "An ulterior disposition of the kind contemplated by the last preceding section cannot take effect unless the condition is strictly fulfilled."
      }
    ],
    "definitions": [
      {
        "term": "Condition Precedent",
        "definition": "A prerequisite condition that must precede the inception and vesting of an estate."
      },
      {
        "term": "Condition Subsequent",
        "definition": "A condition following vesting that terminates or divests the established estate."
      }
    ],
    "ingredients": [
      "Validity of condition under Section 25.",
      "Temporal placement (precedent vs subsequent).",
      "Application of substantial vs strict compliance standard."
    ],
    "exceptions": [
      "If a condition precedent is illegal, the entire transfer fails; if a condition subsequent is illegal, the condition fails and the transfer remains absolute."
    ],
    "examples": [
      {
        "scenario": "A transfers Rs. 50,000 to B on condition that B marries with the consent of C, D, and E. E dies. B marries with the consent of C and D.",
        "application": "Under Section 26, the condition precedent has been substantially complied with, and B takes the interest."
      }
    ],
    "landmarkCases": [
      {
        "case": "Wilkinson v. Wilkinson",
        "citation": "(1871) LR 12 Eq 604",
        "year": "1871",
        "bench": "Court of Chancery",
        "ratio": "A condition requiring a married woman to live apart from her husband to receive property was struck down as contrary to public policy and void.",
        "impact": "Classic authority on void immoral conditions under Section 25."
      }
    ],
    "comparisonTables": [
      {
        "title": "Condition Precedent vs Condition Subsequent",
        "headers": ["Aspect", "Condition Precedent (s. 26)", "Condition Subsequent (s. 29)"],
        "rows": [
          ["Time of Fulfillment", "Precedes the vesting of property", "Follows vesting (divests property)"],
          ["Standard of Compliance", "SUBSTANTIAL compliance is sufficient", "STRICT compliance is mandatory"],
          ["Effect of Invalidity", "Transfer FAILS completely", "Condition is ignored; estate becomes ABSOLUTE"]
        ]
      }
    ],
    "diagramId": "diag-tpa-vested-contingent",
    "diagramExplanation": "Custom vector schematic illustrating condition precedent vs condition subsequent pathways.",
    "misconceptions": [
      {
        "myth": "If a condition subsequent is unlawful or impossible, the transferee loses his property.",
        "reality": "If a condition subsequent is invalid, the condition is wiped out, and the transferee's estate becomes completely absolute."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Applying strict compliance to Condition Precedent.",
        "reality": "Section 26 specifically prescribes SUBSTANTIAL compliance for Condition Precedent. Strict compliance applies to Condition Subsequent (Section 29).",
        "rule": "Precedent = Substantial; Subsequent = Strict."
      }
    ],
    "flashcards": [
      {
        "id": "fc-tpa-03-05",
        "front": "What standard of compliance applies to a Condition Precedent under Section 26?",
        "back": "Substantial compliance.",
        "category": "Condition Precedent"
      },
      {
        "id": "fc-tpa-03-06",
        "front": "What standard of compliance applies to a Condition Subsequent under Section 29?",
        "back": "Strict compliance.",
        "category": "Condition Subsequent"
      },
      {
        "id": "fc-tpa-03-07",
        "front": "What happens if a condition subsequent is impossible or illegal from the inception?",
        "back": "The condition is void, and the transferee's estate becomes absolute.",
        "category": "Invalid Conditions"
      },
      {
        "id": "fc-tpa-03-08",
        "front": "Under Section 25, what makes a conditional transfer void?",
        "back": "If the condition is impossible, forbidden by law, fraudulent, injurious, or immoral/opposed to public policy.",
        "category": "Section 25"
      }
    ],
    "sourceReferences": [
      {"title": "Mulla: The Transfer of Property Act", "url": "https://archive.org"}
    ]
}

data["top-tpa-03-03"] = {
    "topicId": "top-tpa-03-03",
    "chapterId": "ch-tpa-03",
    "subjectId": "law-tpa",
    "title": "Doctrine of Election: Foundation & Operation (Section 35)",
    "subtitle": "Allegans Contraria Non Est Audiendus: He Who Accepts the Benefit Must Bear the Burden",
    "bareActRef": "Transfer of Property Act, 1882 — Section 35",
    "learningObjective": "Master the equitable Doctrine of Election codified in Section 35, the Latin maxim Allegans contraria non est audiendus, indirect benefits, and compensation to disappointed transferees.",
    "detailedExplanation": """
<h3>1. The Equitable Foundation: Section 35</h3>
<p>'Where a person professes to transfer property which he has no right to transfer, and as part of the same transaction confers any benefit on the owner of the property, such owner must <strong>elect</strong> either to confirm such transfer or to dissent from it; and in the latter case he shall relinquish the benefit so conferred.'</p>
<p><strong>The Core Maxims:</strong></p>
<ul>
  <li><strong>Allegans contraria non est audiendus:</strong> A person making contradictory statements will not be heard.</li>
  <li><strong>Qui approbat non reprobat:</strong> He who approbates cannot reprobate (one cannot blow hot and cold, accepting the beneficial part of an instrument while repudiating its burden).</li>
</ul>

<h3>2. The Mechanism of Election</h3>
<ol>
  <li><strong>If the Owner Confirms the Transfer:</strong> He retains the conferred benefit, and the third party gets the property.</li>
  <li><strong>If the Owner Dissents (Rejects the Transfer):</strong>
    <ul>
      <li>He retains his own property.</li>
      <li>He must <strong>relinquish the benefit</strong> conferred upon him.</li>
      <li>The relinquished benefit reverts to the transferor or his representative.</li>
      <li>From the reverted benefit, the transferor must <strong>compensate the disappointed transferee</strong> (the measure of compensation is the value of the property attempted to be transferred).</li>
    </ul>
  </li>
</ol>

<h3>3. Essential Conditions for Election to Arise</h3>
<ul>
  <li>The transfer of another's property and the conferment of benefit on the owner must form <strong>part of the same transaction</strong>.</li>
  <li>The benefit must be conferred on the owner directly. Section 35: <em>'A person taking no benefit directly under a transaction, but deriving a benefit under it indirectly, need not elect.'</em></li>
  <li>Taking benefit in one capacity (e.g., individual) does not necessitate election when dissenting in another capacity (e.g., as guardian or trustee).</li>
</ul>

<h3>4. Mode of Election: Express or Implied</h3>
<p>Election may be express or implied by conduct (e.g., enjoying the benefit for <strong>two years</strong> without doing any act of dissent creates an implied presumption of election to confirm).</p>
""",
    "quickRevisionPoints": [
      "Section 35 codifies the equitable Doctrine of Election.",
      "Maxims: Qui approbat non reprobat (cannot approbate and reprobate) & Allegans contraria non est audiendus.",
      "Applies when transferor professes to transfer property not his own and confers benefit on true owner in same transaction.",
      "If owner dissents: Relinquishes benefit; disappointed transferee is compensated from reverted benefit.",
      "Transfer and benefit MUST form part of the SAME transaction.",
      "Enjoying benefit for 2 years without dissent raises presumption of election to confirm."
    ],
    "provisions": [
      {
        "provision": "Section 35, TPA 1882",
        "title": "Election: When Necessary",
        "description": "Where a person professes to transfer property which he has no right to transfer, and confers benefit on the owner in the same transaction, the owner must elect to confirm or dissent, relinquishing benefit if dissents."
      }
    ],
    "definitions": [
      {
        "term": "Doctrine of Election",
        "definition": "The equitable obligation requiring an owner who is given a benefit under an instrument to choose between accepting the instrument in its entirety or rejecting it."
      }
    ],
    "ingredients": [
      "Unauthorized conveyance of another's property.",
      "Conferment of benefit on true owner.",
      "Both acts contained in the same transaction.",
      "Obligation to elect between property and benefit."
    ],
    "exceptions": [
      "Indirect benefits do not put a person to election."
    ],
    "examples": [
      {
        "scenario": "A professes to sell C's farm (worth Rs. 8 lakhs) to B, and in the same deed gives Rs. 10 lakhs cash to C. C elects to retain his farm and dissents.",
        "application": "Under Section 35, C forfeits the Rs. 10 lakhs cash. The Rs. 10 lakhs reverts to A, who must compensate disappointed buyer B with Rs. 8 lakhs (value of the farm), keeping the remaining Rs. 2 lakhs."
      }
    ],
    "landmarkCases": [
      {
        "case": "Cooper v. Cooper",
        "citation": "(1874) LR 7 HL 53",
        "year": "1874",
        "bench": "House of Lords (Lord Hatherley)",
        "ratio": "The doctrine of election rests upon the principle that a person who takes a benefit under an instrument must adopt the whole of it, conforming to all its provisions and renouncing every right inconsistent with it.",
        "impact": "Classic common law exposition of the foundation of the doctrine of election."
      },
      {
        "case": "C. Beepathuma v. Velasari Shankaranarayana Kadambolithaya",
        "citation": "(1964) 5 SCR 836",
        "year": "1964",
        "bench": "Supreme Court of India (Sikri J)",
        "ratio": "The Supreme Court applied the doctrine of election and the rule of approbate and reprobate under Section 35, holding that parties who accepted benefits under a family partition will cannot challenge the disposition of their property contained in the same will.",
        "impact": "Leading Indian constitutional authority on Section 35 election."
      }
    ],
    "comparisonTables": [
      {
        "title": "Election Outcomes",
        "headers": ["Choice of Owner", "Owner's Fate", "Transferee's Fate", "Transferor's Role"],
        "rows": [
          ["Confirms Transfer", "Keeps conferred benefit; loses property", "Gets owner's property as contemplated", "Transaction complete; no further duty"],
          ["Dissents from Transfer", "Keeps own property; forfeits benefit", "Compensated from the forfeited benefit", "Receives reverted benefit; must pay compensation"]
        ]
      }
    ],
    "diagramId": "diag-tpa-vested-contingent",
    "diagramExplanation": "Custom vector schematic displaying the two branches of election under Section 35.",
    "misconceptions": [
      {
        "myth": "If the owner dissents, the disappointed transferee gets nothing.",
        "reality": "Under Section 35, the disappointed transferee is entitled to be compensated out of the benefit relinquished by the dissenting owner."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Applying election when the benefit and transfer are in two separate documents.",
        "reality": "Section 35 strictly requires that the transfer and the benefit must form 'part of the same transaction'.",
        "rule": "Must be part of the SAME transaction."
      }
    ],
    "flashcards": [
      {
        "id": "fc-tpa-03-09",
        "front": "Which section of the Transfer of Property Act codifies the Doctrine of Election?",
        "back": "Section 35.",
        "category": "Doctrine of Election"
      },
      {
        "id": "fc-tpa-03-10",
        "front": "What does the Latin maxim 'Qui approbat non reprobat' mean?",
        "back": "He who approbates cannot reprobate (one cannot accept the benefit and reject the burden).",
        "category": "Legal Maxims"
      },
      {
        "id": "fc-tpa-03-11",
        "front": "What happens if the owner dissents from the transfer under Section 35?",
        "back": "He keeps his property, relinquishes the benefit, and the disappointed transferee is compensated from the relinquished benefit.",
        "category": "Section 35 Mechanics"
      },
      {
        "id": "fc-tpa-03-12",
        "front": "How long must an owner enjoy a conferred benefit without dissenting to raise an implied presumption of election under Section 35?",
        "back": "Two years.",
        "category": "Implied Election"
      }
    ],
    "sourceReferences": [
      {"title": "Mulla: The Transfer of Property Act", "url": "https://archive.org"}
    ]
}

create_concept_file('assets/learning/data/tpa/tpa-concepts-part1.js', 'TPA_CONCEPTS_PART1', data)
print(f"TPA Part 1 complete with {len(data)} topics!")
