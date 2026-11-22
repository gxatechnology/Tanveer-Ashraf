import json
from concept_helpers import create_concept_file

data = {}

# -------------------------------------------------------------
# CHAPTER 1: PRELIMINARY & GENERAL PRINCIPLES OF TRANSFER
# -------------------------------------------------------------
data["top-tpa-01-01"] = {
    "topicId": "top-tpa-01-01",
    "chapterId": "ch-tpa-01",
    "subjectId": "law-tpa",
    "title": "Meaning and Scope of Transfer (Sections 1–5: Act Inter Vivos)",
    "subtitle": "Voluntary Conveyance Between Living Persons and Excluded Transactions",
    "bareActRef": "Transfer of Property Act, 1882 — Sections 1–5",
    "learningObjective": "Master the Section 5 statutory definition of 'transfer of property', the requirement of living persons (inter vivos), and identify transactions that do not amount to transfer (partition, surrender, family arrangement).",
    "detailedExplanation": """
<h3>1. Scope and Preamble of the Act</h3>
<p>The Transfer of Property Act, 1882 was enacted to define and amend certain parts of the law relating to the transfer of property by <strong>act of parties</strong> (inter vivos). It does NOT govern testamentary succession (wills) or transfers by operation of law (insolvency, court execution, intestate succession).</p>

<h3>2. Section 5: 'Transfer of Property' Defined</h3>
<p>'Transfer of property' means an act by which a <strong>living person</strong> conveys property, in present or in future, to one or more other living persons, or to himself and one or more other living persons; and 'to transfer property' is to perform such act.</p>
<ul>
  <li><strong>Living Person (Inter Vivos):</strong> Includes a human being, company or association or body of individuals, whether incorporated or not.</li>
  <li><strong>In Present or in Future:</strong> The conveyance may be immediate or deferred, but the property itself must be in existence at the date of transfer.</li>
</ul>

<h3>3. Transactions NOT Amounting to Transfer of Property</h3>
<p>Courts have settled that the following transactions are not transfers of property under Section 5:</p>
<ol>
  <li><strong>Partition of Joint Hindu Family Property:</strong> Partition merely converts joint enjoyment into separate exclusive enjoyment of pre-existing titles; no new title is conveyed (<em>Commissioner of Income Tax v. Keshavlal Lallubhai Patel, 1965 SC</em>).</li>
  <li><strong>Family Arrangement / Settlement:</strong> Merely acknowledges, clarifies, and settles antecedent title; does not create a new conveyance (<em>Kale v. Deputy Director of Consolidation, 1976 SC</em>).</li>
  <li><strong>Surrender by a Life Estate Holder:</strong> Merely an effacement of the prior interest accelerating the remainder; not an alienation.</li>
  <li><strong>Relinquishment / Release:</strong> Extinguishment of a co-owner's right in favor of other co-owners without conveying title to a stranger.</li>
  <li><strong>Charge under Section 100:</strong> Creates a security interest but does not transfer an interest in property.</li>
</ol>
""",
    "quickRevisionPoints": [
      "TPA governs transfers by act of parties (inter vivos), not wills or court auctions.",
      "Section 5: Living person conveys property in present or in future.",
      "'Living person' includes corporations and unincorporated associations.",
      "Partition is NOT a transfer of property (CIT v. Keshavlal Lallubhai, 1965 SC).",
      "Family settlement is NOT a transfer (Kale v. DDC, 1976 SC).",
      "Surrender and Charge are not transfers under Section 5."
    ],
    "provisions": [
      {
        "provision": "Section 5, TPA 1882",
        "title": "'Transfer of Property' Defined",
        "description": "An act by which a living person conveys property, in present or in future, to one or more other living persons, or to himself and others."
      }
    ],
    "definitions": [
      {
        "term": "Inter Vivos",
        "definition": "Between living persons; transfers taking effect during the lifetimes of the parties, distinguished from testamentary devolution."
      }
    ],
    "ingredients": [
      "Act of a living person.",
      "Conveyance of an existing property.",
      "Transfer in present or future.",
      "Recipient is one or more living persons."
    ],
    "exceptions": [
      "Testamentary dispositions (wills) and transfers by operation of law are excluded from TPA."
    ],
    "examples": [
      {
        "scenario": "Three brothers partition their joint ancestral property by executing a registered partition deed.",
        "application": "Under CIT v. Keshavlal Lallubhai, the partition is an adjustment of pre-existing co-ownership shares and not a 'transfer of property' under Section 5."
      }
    ],
    "landmarkCases": [
      {
        "case": "Commissioner of Income Tax v. Keshavlal Lallubhai Patel",
        "citation": "(1965) 2 SCR 100",
        "year": "1965",
        "bench": "Supreme Court of India (Shah J)",
        "ratio": "A partition of joint family property is not a transfer in the strict sense; it is merely an arrangement whereby a joint enjoyment is converted into an enjoyment in severalty. It does not amount to a transfer of property.",
        "impact": "Decisive Indian Supreme Court authority on the legal nature of partition."
      },
      {
        "case": "Kale v. Deputy Director of Consolidation",
        "citation": "(1976) 3 SCC 119",
        "year": "1976",
        "bench": "Supreme Court of India (Fazal Ali J)",
        "ratio": "A family arrangement is not a transfer of property. It simply recognizes and records pre-existing rights and titles of family members to avoid future disputes and buy peace in the family.",
        "impact": "Bedrock precedent establishing that bona fide family settlements do not constitute transfers of property."
      }
    ],
    "comparisonTables": [
      {
        "title": "Transfer of Property vs Non-Transfer Transactions",
        "headers": ["Transaction", "Is it a Transfer under s. 5?", "Reasoning"],
        "rows": [
          ["Sale (Section 54)", "YES", "Transfers absolute ownership for price"],
          ["Gift (Section 122)", "YES", "Transfers ownership gratuitously inter vivos"],
          ["Partition of HUF", "NO", "Reorganization of pre-existing titles, no new conveyance"],
          ["Family Settlement", "NO", "Bona fide settlement of antecedent claims"],
          ["Surrender of Lease", "NO", "Merely extinguishes leasehold; merges into reversion"]
        ]
      }
    ],
    "diagramId": "diag-tpa-transferability-s6",
    "diagramExplanation": "Custom vector schematic displaying the boundaries of Section 5 transfers and excluded non-transfer transactions.",
    "misconceptions": [
      {
        "myth": "A will is governed by the Transfer of Property Act 1882.",
        "reality": "Wills take effect upon death and are testamentary transfers governed exclusively by the Indian Succession Act 1925; TPA governs only inter vivos transfers."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing a living person cannot transfer property to himself.",
        "reality": "Under Section 5 (as amended in 1929), a person CAN transfer property 'to himself and one or more other living persons' (e.g. creating a trust where grantor is a co-trustee).",
        "rule": "Transfer to himself + others is valid."
      }
    ],
    "flashcards": [
      {
        "id": "fc-tpa-01-01",
        "front": "What does 'Inter Vivos' mean in Section 5 of the Transfer of Property Act?",
        "back": "Between living persons.",
        "category": "Section 5"
      },
      {
        "id": "fc-tpa-01-02",
        "front": "Is partition of joint family property a 'transfer of property' under Section 5?",
        "back": "No, partition is an adjustment of pre-existing shares, not a conveyance of new title (CIT v. Keshavlal).",
        "category": "Partition"
      },
      {
        "id": "fc-tpa-01-03",
        "front": "What did the Supreme Court hold in Kale v. DDC (1976) regarding family settlements?",
        "back": "A family settlement is not a transfer of property; it acknowledges antecedent titles to maintain family peace.",
        "category": "Family Settlement"
      },
      {
        "id": "fc-tpa-01-04",
        "front": "Can property be transferred under TPA to a living entity that is an incorporated company?",
        "back": "Yes, Section 5 expressly defines 'living person' to include a company, association, or body of individuals.",
        "category": "Living Persons"
      }
    ],
    "sourceReferences": [
      {"title": "Mulla: The Transfer of Property Act — 13th Ed.", "url": "https://archive.org"},
      {"title": "Transfer of Property Act, 1882", "url": "https://indiacode.nic.in"}
    ]
}

data["top-tpa-01-02"] = {
    "topicId": "top-tpa-01-02",
    "chapterId": "ch-tpa-01",
    "subjectId": "law-tpa",
    "title": "What May Be Transferred & Non-Transferable Properties (Section 6)",
    "subtitle": "The Universal Rule of Transferability and the 10 Inalienable Exceptions",
    "bareActRef": "Transfer of Property Act, 1882 — Section 6",
    "learningObjective": "Master the general principle 'Property of any kind may be transferred' and the 10 statutory clauses of Section 6 (clauses a to i) prohibiting transfer.",
    "detailedExplanation": """
<h3>1. General Rule: Everything is Transferable</h3>
<p>Section 6 opens with the cardinal principle of property law: <em>'Property of any kind may be transferred, except as otherwise provided by this Act or by any other law for the time being in force.'</em> Alienability is the essential badge of property. Non-transferability is an exception.</p>

<h3>2. The Ten Non-Transferable Properties: Section 6 Clauses</h3>
<ol>
  <li><strong>Clause (a) — Spes Successionis:</strong> The chance of an heir-apparent succeeding to an estate, the chance of a relation obtaining a legacy on the death of a kinsman, or any other mere possibility cannot be transferred. (A mere hope of future inheritance is not a present property right).</li>
  <li><strong>Clause (b) — Mere Right of Re-entry:</strong> A mere right of re-entry for breach of a condition subsequent cannot be transferred to anyone except the owner of the property affected thereby.</li>
  <li><strong>Clause (c) — Easement Apart from Dominant Heritage:</strong> An easement cannot be transferred apart from the dominant heritage. (An easement is parasitic on the dominant tenement).</li>
  <li><strong>Clause (d) — Restricted Personal Enjoyment:</strong> An interest in property restricted in its enjoyment to the owner personally cannot be transferred (e.g., religious office, shebaiti right, occupancy rights).</li>
  <li><strong>Clause (dd) — Future Maintenance:</strong> A right to future maintenance, in whatsoever manner arising, secured or determined, cannot be transferred. (Designed to protect widows and dependents from starvation).</li>
  <li><strong>Clause (e) — Mere Right to Sue:</strong> A mere right to sue cannot be transferred. (Distinguished from an actionable claim; you cannot sell a right to sue for unliquidated damages in tort or contract).</li>
  <li><strong>Clause (f) — Public Office & Salary:</strong> A public office cannot be transferred, nor can the salary of a public officer, whether before or after it has become payable.</li>
  <li><strong>Clause (g) — Stipends and Pensions:</strong> Military, naval, air-force, and civil pensions and political pensions cannot be transferred.</li>
  <li><strong>Clause (h) — Nature of Interest / Unlawful Object:</strong> No transfer can be made (1) opposed to nature of interest (e.g. res communes like air/sea), (2) for unlawful object/consideration under Section 23 Contract Act, or (3) to a person legally disqualified.</li>
  <li><strong>Clause (i) — Untransferable Tenancies:</strong> Untransferable rights of occupancy (tenancy) under local tenancy laws.</li>
</ol>
""",
    "quickRevisionPoints": [
      "General rule: Property of any kind may be transferred.",
      "Clause (a): Spes successionis (chance of heir-apparent) is strictly non-transferable.",
      "Clause (b): Mere right of re-entry cannot be transferred separately from property.",
      "Clause (c): Easement cannot be transferred without dominant heritage.",
      "Clause (dd): Right to future maintenance cannot be transferred.",
      "Clause (e): A mere right to sue cannot be transferred (distinguished from actionable claim).",
      "Clause (f) & (g): Public offices, salaries, and pensions cannot be transferred."
    ],
    "provisions": [
      {
        "provision": "Section 6(a), TPA 1882",
        "title": "Spes Successionis Non-Transferable",
        "description": "The chance of an heir-apparent succeeding to an estate, the chance of a relation obtaining a legacy on the death of a kinsman, or any other mere possibility of a like nature, cannot be transferred."
      },
      {
        "provision": "Section 6(e), TPA 1882",
        "title": "Mere Right to Sue Non-Transferable",
        "description": "A mere right to sue cannot be transferred."
      }
    ],
    "definitions": [
      {
        "term": "Spes Successionis",
        "definition": "A bare hope or expectancy of succeeding to property upon the death of a living person."
      }
    ],
    "ingredients": [
      "Rule of universal transferability.",
      "Strict construction of Section 6 exceptions.",
      "Protection of public policy and dependents."
    ],
    "exceptions": [
      "Actionable claims under Section 130 are transferable; mere rights to sue for unliquidated damages under 6(e) are not."
    ],
    "examples": [
      {
        "scenario": "A expects to inherit his father's house upon his father's death. During the father's lifetime, A executes a sale deed of the house to B.",
        "application": "The transfer is void ab initio under Section 6(a) as a transfer of spes successionis; B acquires zero title."
      }
    ],
    "landmarkCases": [
      {
        "case": "Amrit Narayan v. Gaya Singh",
        "citation": "(1918) 45 IA 35",
        "year": "1918",
        "bench": "Privy Council (Rt. Hon. Ameer Ali)",
        "ratio": "A Hindu reversioner has no right or interest in praesenti in the property which the female owner holds for life. Until her death, he has nothing more than a spes successionis, which is incapable of being transferred or renounced.",
        "impact": "Classic authority on the absolute inalienability of spes successionis under Section 6(a)."
      }
    ],
    "comparisonTables": [
      {
        "title": "Actionable Claim vs Mere Right to Sue",
        "headers": ["Aspect", "Actionable Claim (Section 130)", "Mere Right to Sue (Section 6(e))"],
        "rows": [
          ["Transferability", "Fully TRANSFERABLE by written instrument", "Strictly NON-TRANSFERABLE and void"],
          ["Nature of Claim", "Claim to a liquidated, ascertained debt or beneficial interest", "Claim for unliquidated damages for breach of contract or tort"],
          ["Example", "Arrears of rent, fixed loan debt", "Right to claim damages for assault or defamation"]
        ]
      }
    ],
    "diagramId": "diag-tpa-transferability-s6",
    "diagramExplanation": "Custom vector schematic illustrating the 10 statutory heads of Section 6 non-transferable properties.",
    "misconceptions": [
      {
        "myth": "Arrears of maintenance already accrued can never be transferred.",
        "reality": "Section 6(dd) prohibits transfer of FUTURE maintenance. Arrears of maintenance already accrued and quantified are a debt and CAN be transferred."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Confusing an actionable claim with a right to sue.",
        "reality": "An actionable claim for an existing debt is transferable (Section 130); a claim for unliquidated damages is a 'mere right to sue' and cannot be transferred (Section 6(e)).",
        "rule": "Debt = Transferable; Unliquidated damages = Non-transferable."
      }
    ],
    "flashcards": [
      {
        "id": "fc-tpa-01-05",
        "front": "What does Section 6(a) of the Transfer of Property Act prohibit from being transferred?",
        "back": "Spes successionis — the chance of an heir-apparent succeeding to an estate or obtaining a legacy.",
        "category": "Section 6"
      },
      {
        "id": "fc-tpa-01-06",
        "front": "Can an easement be transferred separately from the dominant heritage under Section 6(c)?",
        "back": "No, an easement cannot be transferred apart from the dominant heritage.",
        "category": "Easements"
      },
      {
        "id": "fc-tpa-01-07",
        "front": "Can a right to future maintenance be transferred under Section 6(dd)?",
        "back": "No, a right to future maintenance, howsoever secured or determined, cannot be transferred.",
        "category": "Maintenance"
      },
      {
        "id": "fc-tpa-01-08",
        "front": "What was the Privy Council's ruling in Amrit Narayan v. Gaya Singh (1918)?",
        "back": "The interest of a Hindu reversioner during the life of a female heir is a mere spes successionis and non-transferable.",
        "category": "Case Law"
      }
    ],
    "sourceReferences": [
      {"title": "Mulla: The Transfer of Property Act", "url": "https://archive.org"}
    ]
}

data["top-tpa-01-03"] = {
    "topicId": "top-tpa-01-03",
    "chapterId": "ch-tpa-01",
    "subjectId": "law-tpa",
    "title": "Competency to Transfer & Operation of Transfer (Sections 7, 8)",
    "subtitle": "Capacity to Convey and the Complete Devolution of Legal Incidents",
    "bareActRef": "Transfer of Property Act, 1882 — Sections 7, 8",
    "learningObjective": "Master Section 7 capacity to transfer and Section 8 operation of transfer passing all legal incidents to the transferee.",
    "detailedExplanation": """
<h3>1. Competency to Transfer: Section 7</h3>
<p>Every person competent to contract (under Section 11 Contract Act: age of majority, sound mind, not disqualified) and entitled to transferable property, or authorized to dispose of transferable property not his own, is competent to transfer such property.</p>
<ul>
  <li><strong>Can be Absolute or Conditional:</strong> The transfer may be total or partial, absolute or conditional.</li>
  <li><strong>Authority of Agent / Guardian:</strong> A person may transfer property belonging to another if duly authorized by law (e.g., manager of HUF for legal necessity, court receiver, or power of attorney holder).</li>
</ul>

<h3>2. Operation of Transfer: Section 8</h3>
<p>'Unless a different intention is expressed or necessarily implied, a transfer of property passes forthwith to the transferee all the interest which the transferor is then capable of passing in the property and in the legal incidents thereof.'</p>
<p><strong>Legal Incidents Transferred Automatically under Section 8:</strong></p>
<ol>
  <li><strong>Land:</strong> The easements annexed thereto, the rents and profits accruing after the transfer, and all things attached to the earth (trees, buildings, fixtures).</li>
  <li><strong>House:</strong> The easements annexed, rent accruing after transfer, and the locks, keys, bars, doors, windows, and other things provided for permanent use therewith.</li>
  <li><strong>Machinery Attached to Earth:</strong> The movable parts of the machinery.</li>
  <li><strong>Debt or Actionable Claim:</strong> The securities for the debt (e.g. mortgage, pledge) in the hands of the transferor.</li>
  <li><strong>Money / Other Property Yielding Income:</strong> The interest or income accruing after the transfer takes effect.</li>
</ol>
""",
    "quickRevisionPoints": [
      "Section 7: Competency = Competent to contract + entitled to property or authorized to dispose.",
      "Section 8: Transfer passes forthwith ALL interest the transferor is capable of passing.",
      "Land transfer automatically carries fixtures, trees, easements, and post-transfer rents.",
      "House transfer automatically includes keys, locks, doors, windows, and fixtures.",
      "Debt transfer automatically carries underlying securities to the transferee.",
      "Maxim: Quicquid plantatur solo, solo cedit (English rule modified in India by Section 8 & Section 108)."
    ],
    "provisions": [
      {
        "provision": "Section 8, TPA 1882",
        "title": "Operation of Transfer",
        "description": "Unless a different intention is expressed or implied, a transfer of property passes forthwith to the transferee all the interest which the transferor is then capable of passing and in the legal incidents thereof."
      }
    ],
    "definitions": [
      {
        "term": "Legal Incidents",
        "definition": "The rights, appurtenances, easements, and attached accessions that naturally accompany the ownership of the principal property."
      }
    ],
    "ingredients": [
      "Contractual capacity of transferor.",
      "Title or lawful authority to convey.",
      "Presumption that full title and all incidents pass unless expressly excluded."
    ],
    "exceptions": [
      "Parties may expressly reserve certain incidents (e.g. reserving easement or mineral rights)."
    ],
    "examples": [
      {
        "scenario": "A sells his agricultural land to B without mentioning the mango orchard growing on it.",
        "application": "Under Section 8, the trees attached to the earth pass automatically to B as legal incidents of the land."
      }
    ],
    "landmarkCases": [
      {
        "case": "Bishwanath Prasad Singh v. Rajendra Prasad",
        "citation": "(2006) 4 SCC 432",
        "year": "2006",
        "bench": "Supreme Court of India (S.B. Sinha J)",
        "ratio": "Section 8 provides that a transfer passes all the interest which the transferor is capable of passing. To ascertain whether a document is an absolute sale or a conditional conveyance, the intention of the parties gathered from the entire instrument is decisive.",
        "impact": "Primary modern authority on Section 8 and interpretation of deed conveyances."
      }
    ],
    "comparisonTables": [
      {
        "title": "Legal Incidents by Property Type (Section 8)",
        "headers": ["Property Type", "Incidents Automatically Passing to Transferee"],
        "rows": [
          ["Land", "Easements, post-transfer rents, trees, fixtures attached to earth"],
          ["House", "Locks, keys, doors, windows, permanent fixtures, easements"],
          ["Debt / Actionable Claim", "Securities for the debt, pledge, mortgages held by transferor"]
        ]
      }
    ],
    "diagramId": "diag-tpa-transferability-s6",
    "diagramExplanation": "Custom vector schematic illustrating how Section 8 transfers the core title alongside all attached legal incidents.",
    "misconceptions": [
      {
        "myth": "Rent that fell due BEFORE the transfer was made passes to the buyer under Section 8.",
        "reality": "Section 8 passes only rents and profits accruing AFTER the transfer. Arrears of rent accrued before transfer are an actionable claim and do not pass automatically."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing a separate deed is required to transfer the lock and keys of a house.",
        "reality": "Section 8 explicitly provides that keys, doors, and locks pass automatically as legal incidents of the house.",
        "rule": "Legal incidents pass automatically under Section 8."
      }
    ],
    "flashcards": [
      {
        "id": "fc-tpa-01-09",
        "front": "What two conditions are required for competency to transfer under Section 7?",
        "back": "Competent to contract under Section 11 Contract Act, and entitled to transferable property or authorized to dispose of it.",
        "category": "Competency"
      },
      {
        "id": "fc-tpa-01-10",
        "front": "What does Section 8 of the Transfer of Property Act govern?",
        "back": "Operation of Transfer — passing all interest and legal incidents to the transferee forthwith.",
        "category": "Section 8"
      },
      {
        "id": "fc-tpa-01-11",
        "front": "Do pre-transfer arrears of rent pass to the transferee automatically under Section 8?",
        "back": "No, only rents and profits accruing AFTER the transfer pass automatically.",
        "category": "Rents & Incidents"
      },
      {
        "id": "fc-tpa-01-12",
        "front": "Does a transfer of debt automatically pass the securities for the debt under Section 8?",
        "back": "Yes, securities for the debt pass automatically to the transferee.",
        "category": "Debt Securities"
      }
    ],
    "sourceReferences": [
      {"title": "Mulla: The Transfer of Property Act", "url": "https://archive.org"}
    ]
}

create_concept_file('assets/learning/data/tpa/tpa-concepts-part1.js', 'TPA_CONCEPTS_PART1', data)
print(f"TPA Part 1 initial authoring: {len(data)} topics!")
