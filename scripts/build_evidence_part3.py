"""
Builder for Evidence Concepts Part 3 (Chapters 8 to 10: 9 Topics)
Output: assets/learning/data/evidence/evidence-concepts-part3.js
"""

import json

CONCEPTS = {
    # -------------------------------------------------------------------------
    # CHAPTER 8: EXCLUSION OF ORAL BY DOCUMENTARY EVIDENCE
    # -------------------------------------------------------------------------
    "top-evi-08-01": {
        "topicId": "top-evi-08-01",
        "chapterId": "ch-evi-08",
        "subjectId": "law-evidence",
        "title": "Exclusion of Oral by Documentary Evidence (Best Evidence Rule S. 91)",
        "subtitle": "BSA Section 94 vs IEA Section 91 & The Sanctity of Written Documents",
        "learningObjective": "Master the Best Evidence Rule under Section 94 BSA / Section 91 IEA excluding oral evidence to prove the terms of contracts, grants, and other dispositions of property reduced to the form of a document, its two statutory exceptions, and its explanations.",
        "introduction": "When transaction terms are committed to writing, the writing becomes the exclusive repository of the intention of the parties. Section 91 IEA (now Section 94 BSA) enacts the classic Best Evidence Rule: no oral testimony is permitted to prove what was written down in contracts, grants, dispositions of property, or matters required by law to be in writing.",
        "detailedExplanation": """
<h3>1. The Core Rule: Section 94 BSA / Section 91 IEA</h3>
<p>When the terms of a <strong>contract, or of a grant, or of any other disposition of property</strong>, have been reduced to the form of a document, and in all cases in which any matter is <strong>required by law to be reduced to the form of a document</strong>, no evidence shall be given in proof of the terms of such contract, grant, or other disposition of property, or of such matter, <strong>EXCEPT the document itself, or secondary evidence of its contents</strong> in cases in which secondary evidence is admissible.</p>

<h3>2. The Two Statutory Exceptions to Section 91</h3>
<ol>
  <li><strong>Appointment of a Public Officer:</strong> When a public officer is required by law to be appointed in writing, and who has acted as such officer, the writing by which they were appointed need not be proved (their acting in that capacity is sufficient proof of appointment).</li>
  <li><strong>Wills Admitted to Probate:</strong> Wills admitted to probate in India may be proved by the probate itself (without producing the original will).</li>
</ol>

<h3>3. Explanations to Section 91</h3>
<ul>
  <li><strong>Explanation 1:</strong> This section applies equally to cases in which the contracts, grants, or dispositions of property referred to are contained in <strong>one document</strong>, and to cases in which they are contained in <strong>more documents than one</strong> (e.g. series of correspondence).</li>
  <li><strong>Explanation 2:</strong> Where there are <strong>more originals than one</strong>, one original only need be proved.</li>
  <li><strong>Explanation 3:</strong> The statement, in any document whatever, of a fact other than the terms of a contract, grant, or disposition of property, does NOT preclude the admission of oral evidence as to that fact (e.g. a written receipt acknowledging payment does not exclude oral testimony that money was paid).</li>
</ul>
""",
        "keyProvisions": [
            {"section": "Section 94, BSA 2023 (S. 91 IEA)", "title": "Evidence of terms of contracts, grants and dispositions of property", "content": "Best Evidence Rule; excludes oral evidence of terms of written contracts/grants."},
            {"section": "Section 94 Exception 1, BSA 2023 (S. 91 Ex. 1 IEA)", "title": "Public officer appointment exception", "content": "Acting as public officer dispenses with producing written appointment letter."}
        ],
        "landmarkCases": [
            {"caseName": "Taburi Sahai v. Jhunjhunwala", "citation": "AIR 1967 SC 106", "bench": "Supreme Court of India", "principle": "Section 91 forbids proving the contents of a writing otherwise than by writing itself; oral evidence of terms of written transaction is inadmissible."},
            {"caseName": "Roop Kumar v. Mohan Thedani", "citation": "(2003) 6 SCC 595", "bench": "Supreme Court of India", "principle": "Section 91 relates to evidence of terms of contract, while Section 92 relates to evidence contradicting or varying those terms; both together preserve the sanctity of written documents."}
        ],
        "comparativeTable": [
            {
                "title": "Section 91 vs Section 92 Interplay",
                "headers": ["Aspect", "Section 91 IEA / Section 94 BSA", "Section 92 IEA / Section 95 BSA"],
                "rows": [
                    ["Operation", "Excludes oral evidence to PROVE terms", "Excludes oral evidence to CONTRADICT/VARY terms"],
                    ["Prerequisite", "Applies whether S. 92 invoked or not", "Invoked ONLY AFTER terms are proved under S. 91"],
                    ["Parties Covered", "Applies to parties and third persons", "Applies ONLY between parties to the document"],
                    ["Exceptions", "Two statutory exceptions", "Six statutory provisos"]
                ]
            }
        ],
        "diagramId": "diag-evi-electronic-evidence-cert",
        "diagramExplanation": "Shows Best Evidence Rule: document is exclusive proof of its terms; oral evidence excluded under Section 91.",
        "prelimTraps": [
            {
                "trap": "Believing a written receipt for Rs 10,000 prevents a party from proving payment by oral evidence under Section 91.",
                "reality": "Under Explanation 3 to Section 91 IEA / Section 94 BSA, a receipt is merely evidence of payment, not a contract or disposition of property. Payment can be proved by oral testimony independently of the receipt.",
                "rule": "Fact of payment can be proved orally notwithstanding a written receipt."
            }
        ],
        "flashcards": [
            {
                "id": "fc-evi-08-01",
                "front": "What is the classic evidentiary doctrine codified in Section 94 BSA / Section 91 IEA?",
                "back": "The Best Evidence Rule (exclusion of oral evidence to prove the terms of a written document).",
                "category": "Best Evidence Rule"
            },
            {
                "id": "fc-evi-08-02",
                "front": "What are the two statutory exceptions to Section 91 IEA / Section 94 BSA?",
                "back": "1. Appointment of a public officer who has acted as such; 2. Wills admitted to probate.",
                "category": "Section 91 Exceptions"
            }
        ],
        "sourceReferences": [{"title": "Section 94, Bharatiya Sakshya Adhiniyam, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-evi-08-02": {
        "topicId": "top-evi-08-02",
        "chapterId": "ch-evi-08",
        "subjectId": "law-evidence",
        "title": "Exclusion of Evidence of Oral Agreement & The Six Provisos (S. 92)",
        "subtitle": "BSA Section 95 vs IEA Section 92 & The Six Statutory Gateways Permitting Parol Proof",
        "learningObjective": "Master the Parol Evidence Rule under Section 95 BSA / Section 92 IEA (excluding oral evidence to contradict, vary, add to, or subtract from written terms), its strict application between parties, and the Six Statutory Provisos permitting oral evidence.",
        "introduction": "Once a transaction is proved by producing the document under Section 91, Section 92 IEA (now Section 95 BSA) protects its finality by barring parties from asserting that they orally agreed to something different (Parol Evidence Rule). However, to prevent fraud, unconscionability, and injustice, the legislature enacted Six famous Provisos.",
        "detailedExplanation": """
<h3>1. The Parol Evidence Rule: Section 95 BSA / Section 92 IEA</h3>
<p>When the terms of any such contract, grant, or other disposition of property have been proved according to Section 91, <strong>NO evidence of any oral agreement or statement shall be admitted, as between the parties to any such instrument or their representatives in interest, for the purpose of contradicting, varying, adding to, or subtracting from, its terms</strong>.</p>
<p><strong>Strict Restriction:</strong> Section 92 applies ONLY <strong>between parties to the document</strong>. A third party can lead oral evidence to contradict the document under Section 99 IEA / Section 102 BSA!</p>

<h3>2. The Six Famous Statutory Provisos to Section 92</h3>
<ol>
  <li><strong>Proviso 1 (Vitiating Factors):</strong> Any fact may be proved which would invalidate any document, or which would entitle any person to any decree or order relating thereto; such as <strong>fraud, intimidation, illegality, want of due execution, want of capacity, want or failure of consideration, or mistake in fact or law</strong>.</li>
  <li><strong>Proviso 2 (Separate Oral Agreement on Silent Matter):</strong> The existence of any separate oral agreement as to any matter on which a document is <strong>silent, and which is not inconsistent with its terms</strong>, may be proved. (Court considers formality of document).</li>
  <li><strong>Proviso 3 (Condition Precedent):</strong> The existence of any separate oral agreement, constituting a <strong>condition precedent to the attaching of any obligation</strong> under any such contract, grant, or disposition of property, may be proved (e.g. agreement that deed shall not take effect until a third party consents).</li>
  <li><strong>Proviso 4 (Subsequent Oral Rescission or Modification):</strong> The existence of any distinct subsequent oral agreement to <strong>rescind or modify</strong> any such contract, may be proved; EXCEPT where such contract is by law <strong>required to be in writing, OR has been registered</strong>!</li>
  <li><strong>Proviso 5 (Usage or Custom):</strong> Any usage or custom by which incidents not expressly mentioned in any contract are usually annexed to contracts of that description, may be proved, provided not repugnant to express terms.</li>
  <li><strong>Proviso 6 (Extrinsic Context):</strong> Any fact may be proved which shows in what manner the language of a document is related to existing facts (latent ambiguity proof).</li>
</ol>
""",
        "keyProvisions": [
            {"section": "Section 95, BSA 2023 (S. 92 IEA)", "title": "Exclusion of evidence of oral agreement", "content": "Bars oral evidence to contradict, vary, add to or subtract from written terms between parties."},
            {"section": "Section 95 Provisos 1–6, BSA 2023 (S. 92 Prov. 1–6 IEA)", "title": "The Six Statutory Provisos", "content": "Exceptions for fraud/mistake, silent collateral terms, condition precedent, subsequent rescission, custom, context."}
        ],
        "landmarkCases": [
            {"caseName": "Roop Kumar v. Mohan Thedani", "citation": "(2003) 6 SCC 595", "bench": "Supreme Court of India (Pasayat J.)", "principle": "Section 92 forbids admission of parol evidence to contradict or vary written terms; the rule is founded on the principle that writing is more reliable than human memory."},
            {"caseName": "Vipin Shantilal Shah v. State of Maharashtra", "citation": "(2001) 6 SCC 249", "bench": "Supreme Court of India", "principle": "Proviso 1 allows proof of oral agreement showing that the document was a sham or executed under fraud, misrepresentation, or mutual mistake."}
        ],
        "comparativeTable": [
            {
                "title": "The Six Provisos of Section 92 / Section 95 Summary",
                "headers": ["Proviso Number", "Ground Permitting Oral Evidence", "Key Legal Restriction / Condition"],
                "rows": [
                    ["Proviso 1", "Fraud, illegality, failure of consideration, mistake", "Vitiates document or invalidates consent"],
                    ["Proviso 2", "Separate oral agreement where document silent", "Must NOT be inconsistent with written terms"],
                    ["Proviso 3", "Condition precedent to obligation attaching", "Proves agreement never became operative"],
                    ["Proviso 4", "Subsequent oral rescission or modification", "BARRED if document required by law to be in writing or registered"],
                    ["Proviso 5", "Usage or customary commercial incident", "Must not be repugnant to express written terms"],
                    ["Proviso 6", "Surrounding factual context / translation", "Explains relation of words to existing facts"]
                ]
            }
        ],
        "diagramId": "diag-evi-electronic-evidence-cert",
        "diagramExplanation": "Shows Section 92 general bar on contradictory oral evidence and the six statutory provisos permitting oral proof.",
        "prelimTraps": [
            {
                "trap": "Believing a subsequent oral agreement can modify a registered mortgage deed under Proviso 4 to Section 92.",
                "reality": "Proviso 4 explicitly bars subsequent oral modification where the transaction is by law required to be in writing OR HAS BEEN REGISTERED. A registered mortgage cannot be orally modified.",
                "rule": "Registered documents cannot be rescinded or modified by subsequent oral agreement."
            }
        ],
        "flashcards": [
            {
                "id": "fc-evi-08-03",
                "front": "Does Section 92 IEA / Section 95 BSA apply to disputes between a party to a document and a third person stranger?",
                "back": "No; Section 92 applies ONLY between parties to the instrument or their privies. Strangers can give oral evidence under Section 99 IEA / S. 102 BSA.",
                "category": "Parol Evidence Scope"
            },
            {
                "id": "fc-evi-08-04",
                "front": "Under which Proviso to Section 92 / 95 can a party prove that an agreement was not to take effect until a condition precedent was fulfilled?",
                "back": "Proviso 3 to Section 92 IEA / Section 95 BSA.",
                "category": "Section 92 Provisos"
            }
        ],
        "sourceReferences": [{"title": "Section 95, Bharatiya Sakshya Adhiniyam, 2023", "url": "https://www.mha.gov.in"}]
    },

    # -------------------------------------------------------------------------
    # CHAPTER 9: BURDEN OF PROOF & PRESUMPTIONS
    # -------------------------------------------------------------------------
    "top-evi-09-01": {
        "topicId": "top-evi-09-01",
        "chapterId": "ch-evi-09",
        "subjectId": "law-evidence",
        "title": "Burden of Proof vs Evidential Onus & Special Knowledge (S. 106 IEA)",
        "subtitle": "BSA Sections 104–109 vs IEA Sections 101–106 & The Shambhu Nath Mehra Doctrine",
        "learningObjective": "Master the fundamental divide between Burden of Proof (Section 104 BSA / S. 101 IEA, legal burden that never shifts) and Onus of Proof (Section 105 BSA / S. 102 IEA, evidential burden that shifts), and the special knowledge rule under Section 109 BSA / Section 106 IEA.",
        "introduction": "Ei incumbit probatio qui dicit, non qui negat (the burden of proof lies upon him who affirms, not upon him who denies). The law of evidence distinguishes between the permanent legal burden of establishing a case, which remains immutable throughout trial, and the evidential burden (onus of proof) which oscillates between parties as evidence is led.",
        "detailedExplanation": """
<h3>1. Burden of Proof (Section 104 BSA / Section 101 IEA)</h3>
<p>Whoever desires any Court to give judgment as to any legal right or liability dependent on the existence of facts which they assert, <strong>must prove that those facts exist</strong>. When a person is bound to prove the existence of any fact, it is said that the burden of proof lies on that person.</p>
<p><strong>Golden Thread:</strong> In criminal cases, the legal burden of proving the guilt of the accused beyond reasonable doubt <strong>rests throughout upon the prosecution and NEVER shifts</strong> to the accused.</p>

<h3>2. Onus of Proof: The Oscillating Evidential Burden (Section 105 BSA / S. 102 IEA)</h3>
<p>The burden of proof in a suit or proceeding lies on that person who would fail if <strong>no evidence at all were given on either side</strong>.</p>
<table class="table-compact">
  <thead>
    <tr><th>Feature</th><th>Burden of Proof (S. 101 / 104)</th><th>Onus of Proof (S. 102 / 105)</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Nature</strong></td><td>Legal burden of establishing the case</td><td>Evidential burden of adducing evidence</td></tr>
    <tr><td><strong>Shifting</strong></td><td><strong>NEVER shifts</strong> throughout the trial</td><td><strong>Constantly shifts</strong> like a pendulum as evidence is led</td></tr>
    <tr><td><strong>Pleadings</strong></td><td>Determined by the affirmative pleadings/charge</td><td>Determined by the state of evidence at each stage</td></tr>
  </tbody>
</table>

<h3>3. Fact Especially Within Knowledge (Section 109 BSA / Section 106 IEA)</h3>
<p>When any fact is <strong>especially within the knowledge of any person</strong>, the burden of proving that fact is upon him. (e.g. A is charged with travelling on a railway without a ticket; the burden of proving that he had a ticket is on him).</p>

<h3>4. The Shambhu Nath Mehra Doctrine: Section 106 is NOT a Substitute for Prosecution Proof</h3>
<p>In <em>Shambhu Nath Mehra v. State of Ajmer</em> (1956), the Supreme Court held: Section 106 does NOT relieve the prosecution of its fundamental duty to prove guilt beyond reasonable doubt. It applies ONLY to facts which from their very nature are <strong>peculiarly and exclusively within the personal knowledge of the accused</strong>, and cannot be invoked until the prosecution has first established a foundational prima facie case.</p>
""",
        "keyProvisions": [
            {"section": "Section 104, BSA 2023 (S. 101 IEA)", "title": "Burden of proof", "content": "Party asserting legal right/liability must prove facts; legal burden never shifts."},
            {"section": "Section 105, BSA 2023 (S. 102 IEA)", "title": "On whom burden of proof lies", "content": "Test of failure if no evidence led; evidential onus shifts continuously."},
            {"section": "Section 109, BSA 2023 (S. 106 IEA)", "title": "Burden of proving fact especially within knowledge", "content": "Special knowledge rule; applies once prosecution establishes foundational facts."}
        ],
        "landmarkCases": [
            {"caseName": "Shambhu Nath Mehra v. State of Ajmer", "citation": "AIR 1956 SC 404", "bench": "Supreme Court of India (Vivian Bose J.)", "principle": "Section 106 cannot be used to undermine the cardinal rule of criminal law that prosecution must prove guilt; it applies only where fact is especially within accused's knowledge."},
            {"caseName": "Addagada Raghavamma v. Addagada Chenchamma", "citation": "AIR 1964 SC 136", "bench": "Constitution Bench (Subba Rao J.)", "principle": "Authoritative distinction between legal burden of proof under Section 101 (which never shifts) and evidential burden under Section 102 (which shifts as trial proceeds)."}
        ],
        "comparativeTable": [
            {
                "title": "Burden of Proof Allocation Across Scenarios",
                "headers": ["Factual Scenario", "Governing Section (BSA / IEA)", "Party Bearing Burden"],
                "rows": [
                    ["Guilt of criminal accused", "Section 104 / Section 101", "Prosecution (beyond reasonable doubt)"],
                    ["Affirmative claim in civil suit", "Section 104 / Section 101", "Plaintiff (preponderance of probability)"],
                    ["General Exceptions in BNS / IPC", "Section 108 / Section 105", "Accused (rebuttable presumption of sanity)"],
                    ["Railway ticket possession", "Section 109 / Section 106", "Passenger / Accused (special knowledge)"],
                    ["Plea of Alibi", "Section 106 / Section 103", "Accused asserting absence"]
                ]
            }
        ],
        "diagramId": "diag-evi-burden-of-proof-spectrum",
        "diagramExplanation": "Shows legal burden (immutable) vs evidential onus (shifting) and Section 106 special knowledge threshold.",
        "prelimTraps": [
            {
                "trap": "Believing Section 106 IEA / Section 109 BSA shifts the entire burden of proving innocence onto the accused in a custodial death or murder case.",
                "reality": "In Shambhu Nath Mehra and Sucha Singh, the Supreme Court held Section 106 does NOT relieve the prosecution of proving the corpus delicti and foundational facts. Section 106 operates ONLY AFTER a prima facie case is established.",
                "rule": "Section 106 never relieves prosecution of proving foundational facts."
            }
        ],
        "flashcards": [
            {
                "id": "fc-evi-09-01",
                "front": "Does the legal burden of proof under Section 104 BSA / Section 101 IEA ever shift during a criminal trial?",
                "back": "NO; the legal burden of proof never shifts. Only the evidential onus under Section 105 BSA / S. 102 IEA shifts.",
                "category": "Burden of Proof"
            },
            {
                "id": "fc-evi-09-02",
                "front": "What classic Supreme Court judgment authored by Vivian Bose J. established the scope of Section 106 IEA?",
                "back": "Shambhu Nath Mehra v. State of Ajmer (1956).",
                "category": "Special Knowledge"
            }
        ],
        "sourceReferences": [{"title": "Sections 104–109, Bharatiya Sakshya Adhiniyam, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-evi-09-02": {
        "topicId": "top-evi-09-02",
        "chapterId": "ch-evi-09",
        "subjectId": "law-evidence",
        "title": "Presumption of Death, Legitimacy (S. 112 IEA) & Dowry Death",
        "subtitle": "BSA Sections 110–118 vs IEA Sections 107–113B & The Conclusive Proof of Legitimacy",
        "learningObjective": "Master statutory presumptions: continuance of life (S. 107 IEA) vs presumption of death after 7 years (S. 108 IEA), Conclusive Proof of Legitimacy (Section 112 IEA / S. 116 BSA), and mandatory statutory presumption of Dowry Death under Section 113B IEA / Section 118 BSA.",
        "introduction": "To protect matrimonial stability, children, and victims of domestic brutality, the Code creates powerful legal presumptions. The presumption of legitimacy under Section 112 IEA (now Section 116 BSA) is a celebrated 'conclusive proof' rule that can only be rebutted by proving non-access. Concurrently, Section 113B IEA (Section 118 BSA) reverses the burden in dowry deaths occurring within 7 years of marriage.",
        "detailedExplanation": """
<h3>1. Presumption of Life vs Presumption of Death (Sections 110 & 111 BSA / Sections 107 & 108 IEA)</h3>
<ul>
  <li><strong>Continuance of Life (S. 110 BSA / S. 107 IEA):</strong> When the question is whether a man is alive or dead, and it is shown that he was <strong>alive within thirty (30) years</strong>, the burden of proving that he is dead is on the person who affirms it.</li>
  <li><strong>Presumption of Death (S. 111 BSA / S. 108 IEA):</strong> Provided that when it is proved that he has <strong>not been heard of for seven (7) years</strong> by those who would naturally have heard of him if he had been alive, the burden of proving that he is alive is shifted to the person who affirms it. (Note: Presumption is of the <em>fact of death</em>, NOT of the <em>exact date or time of death</em>!).</li>
</ul>

<h3>2. Conclusive Proof of Legitimacy: Section 116 BSA / Section 112 IEA</h3>
<p>The fact that any person was born:</p>
<ol>
  <li>During the continuance of a <strong>valid marriage</strong> between his mother and any man; OR</li>
  <li>Within <strong>two hundred and eighty (280) days</strong> after its dissolution, the mother remaining unmarried;</li>
</ol>
<p>shall be <strong>CONCLUSIVE PROOF</strong> that he is the legitimate child of that man, <strong>UNLESS it can be shown that the parties to the marriage had NO ACCESS to each other at any time when he could have been begotten</strong>.</p>
<p><strong>DNA Test Standard (Gautam Kundu & Kanti Devi):</strong> DNA tests cannot be routinely ordered to rebut the presumption under Section 112. The husband must establish a strong prima facie case of non-access before a court can direct DNA profiling.</p>

<h3>3. Presumption as to Dowry Death: Section 118 BSA / Section 113B IEA</h3>
<p>When the question is whether a person has committed the dowry death of a woman (Section 80 BNS / Section 304B IPC), and it is shown that <strong>soon before her death such woman had been subjected by such person to cruelty or harassment for, or in connection with, any demand for dowry</strong>, the Court <strong>SHALL PRESUME</strong> that such person had caused the dowry death!</p>
""",
        "keyProvisions": [
            {"section": "Section 111, BSA 2023 (S. 108 IEA)", "title": "Burden of proving that person is alive who has not been heard of for 7 years", "content": "Statutory presumption of death after 7 years of absence."},
            {"section": "Section 116, BSA 2023 (S. 112 IEA)", "title": "Birth during marriage conclusive proof of legitimacy", "content": "Conclusive proof of paternity; rebutted solely by proving non-access."},
            {"section": "Section 118, BSA 2023 (S. 113B IEA)", "title": "Presumption as to dowry death", "content": "Mandatory 'shall presume' once dowry harassment soon before death is established."}
        ],
        "landmarkCases": [
            {"caseName": "Gautam Kundu v. State of West Bengal", "citation": "(1993) 3 SCC 418", "bench": "Supreme Court of India", "principle": "Section 112 requires conclusive proof of legitimacy; courts will not lightly order DNA tests to satisfy the husband's suspicion; non-access must be established."},
            {"caseName": "Major Singh v. State of Punjab", "citation": "(2015) 5 SCC 201", "bench": "Supreme Court of India", "principle": "For Section 113B presumption of dowry death to operate, prosecution must establish that cruelty or harassment occurred 'soon before death' and was connected with dowry demand."}
        ],
        "comparativeTable": [
            {
                "title": "Presumptions: Paternity, Death & Dowry Death",
                "headers": ["Presumption", "Statutory Provision (BSA / IEA)", "Nature of Presumption", "Rebuttal Requirement"],
                "rows": [
                    ["Presumption of Death", "Section 111 / Section 108", "Shall Presume (rebuttable)", "Proof that person is alive"],
                    ["Paternity / Legitimacy", "Section 116 / Section 112", "Conclusive Proof (Irrebuttable save exception)", "Proof of NO ACCESS when child begotten"],
                    ["Abetment of Suicide of Wife", "Section 117 / Section 113A", "May Presume (discretionary)", "Harassment within 7 years of marriage"],
                    ["Dowry Death Presumption", "Section 118 / Section 113B", "Shall Presume (mandatory)", "Harassment soon before death in 7-year span"]
                ]
            }
        ],
        "diagramId": "diag-evi-burden-of-proof-spectrum",
        "diagramExplanation": "Shows legitimacy conclusive proof (S. 112/116), 7-year death presumption (S. 108/111), and mandatory dowry death presumption (S. 113B/118).",
        "prelimTraps": [
            {
                "trap": "Believing Section 108 IEA / Section 111 BSA presumes the exact date or time when the missing person died.",
                "reality": "Section 108 presumes ONLY the FACT of death, NOT the date or time of death. If any party claims death occurred on a specific date, that party must prove it independently.",
                "rule": "Section 108 presumes fact of death, never the time of death."
            }
        ],
        "flashcards": [
            {
                "id": "fc-evi-09-03",
                "front": "What is the sole statutory method to rebut the conclusive presumption of legitimacy under Section 116 BSA / S. 112 IEA?",
                "back": "By showing that the parties to the marriage had NO ACCESS to each other at any time when the child could have been begotten.",
                "category": "Legitimacy Presumption"
            },
            {
                "id": "fc-evi-09-04",
                "front": "What type of presumption is enacted under Section 118 BSA / Section 113B IEA for Dowry Death?",
                "back": "Mandatory presumption ('Shall Presume').",
                "category": "Dowry Death Presumption"
            }
        ],
        "sourceReferences": [{"title": "Sections 110–118, Bharatiya Sakshya Adhiniyam, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-evi-09-03": {
        "topicId": "top-evi-09-03",
        "chapterId": "ch-evi-09",
        "subjectId": "law-evidence",
        "title": "Court Presumptions: S. 114 IEA / S. 117 BSA & Absence of Consent",
        "subtitle": "BSA Sections 117 & 119 vs IEA Sections 114 & 114A & The Common Course of Natural Events",
        "learningObjective": "Master the discretionary common sense presumptions under Section 117 BSA / Section 114 IEA (stolen goods, accomplice credibility, official acts regularity, withheld evidence), and the mandatory statutory presumption of absence of consent in rape prosecutions under Section 119 BSA / Section 114A IEA.",
        "introduction": "Judicial reasoning draws upon human experience. Section 114 IEA (now Section 117 BSA) permits the court to presume the existence of any fact which it thinks likely to have happened, regard being had to the common course of natural events, human conduct, and public and private business. Concurrently, Section 114A IEA (Section 119 BSA) creates a protective presumption of absence of consent in rape trials.",
        "detailedExplanation": """
<h3>1. Discretionary Presumptions: Section 117 BSA / Section 114 IEA</h3>
<p>The Court <strong>MAY PRESUME</strong> the existence of any fact which it thinks likely to have happened, regard being had to the common course of natural events, human conduct, and public and private business, in their relation to the facts of the particular case.</p>
<p><strong>The Most Frequently Tested Illustrations:</strong></p>
<ul>
  <li><strong>Illustration (a): Stolen Goods:</strong> That a man who is in possession of <strong>stolen goods soon after the theft</strong> is either the thief or has received the goods knowing them to be stolen, unless he can account for his possession.</li>
  <li><strong>Illustration (b): Accomplice Evidence:</strong> That an <strong>accomplice is unworthy of credit, unless he is corroborated in material particulars</strong> (Read with Section 133 IEA / Section 138 BSA!).</li>
  <li><strong>Illustration (c): Negotiable Instruments:</strong> That a bill of exchange, accepted or endorsed, was accepted or endorsed for good consideration.</li>
  <li><strong>Illustration (e): Official Acts:</strong> That <strong>judicial and official acts have been regularly performed</strong> (Omnia praesumuntur rite esse acta).</li>
  <li><strong>Illustration (g): Withheld Evidence:</strong> That evidence which could be and is not produced would, if produced, be <strong>unfavourable to the person who withholds it</strong> (Adverse Inference).</li>
</ul>

<h3>2. The Accomplice Conundrum: Section 133 vs Section 114 Illustration (b)</h3>
<table class="table-compact">
  <thead>
    <tr><th>Section</th><th>Statutory Text</th><th>Legal Character</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Section 133 IEA / S. 138 BSA</strong></td><td>Accomplice is a competent witness; conviction is <strong>not illegal merely because based on uncorroborated testimony</strong></td><td>Strict rule of <strong>LAW</strong></td></tr>
    <tr><td><strong>Section 114 Illus. (b) / S. 117 Illus. (b)</strong></td><td>Accomplice is <strong>unworthy of credit unless corroborated in material particulars</strong></td><td>Cardinal rule of <strong>PRUDENCE</strong></td></tr>
  </tbody>
</table>
<p><strong>Harmonious Synthesis:</strong> In law, an accomplice conviction is not illegal without corroboration (S. 133); but in practice, courts virtually NEVER convict on uncorroborated accomplice testimony (S. 114(b) rule of prudence, <em>Bhuboni Sahu v. The King</em>).</p>

<h3>3. Presumption of Absence of Consent in Rape: S. 119 BSA / S. 114A IEA</h3>
<p>In a prosecution for rape under Section 64 BNS / Section 376 IPC (including custodial rape, gang rape, rape of pregnant woman), where sexual intercourse by the accused is proved and the question is whether it was without consent of the woman, and the woman states in her evidence before the court that she <strong>did not consent</strong>, the Court <strong>SHALL PRESUME</strong> that she did not consent!</p>
""",
        "keyProvisions": [
            {"section": "Section 117, BSA 2023 (S. 114 IEA)", "title": "Court may presume existence of certain facts", "content": "Discretionary presumptions based on human conduct and natural events (Illustrations a to i)."},
            {"section": "Section 119, BSA 2023 (S. 114A IEA)", "title": "Presumption as to absence of consent in certain prosecutions for rape", "content": "Mandatory presumption of non-consent once intercourse proved and victim deposes lack of consent."}
        ],
        "landmarkCases": [
            {"caseName": "Bhuboni Sahu v. The King", "citation": "AIR 1949 PC 257", "bench": "Privy Council (Sir John Beaumont)", "principle": "Accomplice evidence is tainted; while Section 133 declares uncorroborated conviction legal, Section 114(b) rule of prudence is so universal that it deserves the reverence of law."},
            {"caseName": "Tulsiram v. State of M.P.", "citation": "(1984) 4 SCC 487", "bench": "Supreme Court of India", "principle": "Presumption under Section 114(a) regarding stolen goods requires two conditions: property must be stolen, and possession must be 'soon after' the theft."}
        ],
        "comparativeTable": [
            {
                "title": "Section 114 Presumptions Breakdown",
                "headers": ["Illustration", "Factual Presumption", "Statutory Nature", "Practical Application"],
                "rows": [
                    ["Illustration (a)", "Recent possession of stolen goods", "May Presume (rebuttable)", "Theft or receiver charges"],
                    ["Illustration (b)", "Accomplice unworthy of credit", "Rule of Prudence", "Demand material corroboration"],
                    ["Illustration (e)", "Judicial & official regularity", "May Presume", "Official notices, summons service"],
                    ["Illustration (g)", "Adverse inference on withholding", "May Presume", "Failure to produce best witness/document"],
                    ["Section 114A / 119", "Absence of consent in rape", "Shall Presume (Mandatory)", "Shifts burden to accused to prove consent"]
                ]
            }
        ],
        "diagramId": "diag-evi-burden-of-proof-spectrum",
        "diagramExplanation": "Shows common sense presumptions under Section 114 (a-i) and mandatory non-consent presumption under Section 114A.",
        "prelimTraps": [
            {
                "trap": "Believing a conviction based on uncorroborated accomplice testimony is legally void and illegal.",
                "reality": "Under Section 133 IEA / Section 138 BSA, an accomplice is a competent witness, and a conviction is NOT ILLEGAL merely because it proceeds upon uncorroborated testimony. Corroboration is a rule of PRUDENCE (S. 114(b)), not of strict legality.",
                "rule": "Uncorroborated accomplice conviction is legal under S. 133, but imprudent under S. 114(b)."
            }
        ],
        "flashcards": [
            {
                "id": "fc-evi-09-05",
                "front": "What does Section 114 Illustration (b) IEA / Section 117 Illustration (b) BSA presume about an accomplice?",
                "back": "That an accomplice is unworthy of credit, unless he is corroborated in material particulars.",
                "category": "Accomplice Presumption"
            },
            {
                "id": "fc-evi-09-06",
                "front": "Under what condition does the presumption of absence of consent arise under S. 119 BSA / S. 114A IEA?",
                "back": "When sexual intercourse is proved and the woman deposes in her evidence before the court that she did not consent.",
                "category": "Absence of Consent"
            }
        ],
        "sourceReferences": [{"title": "Sections 117 & 119, Bharatiya Sakshya Adhiniyam, 2023", "url": "https://www.mha.gov.in"}]
    },

    # -------------------------------------------------------------------------
    # CHAPTER 10: ESTOPPEL, WITNESSES & TRIAL EXAMINATION
    # -------------------------------------------------------------------------
    "top-evi-10-01": {
        "topicId": "top-evi-10-01",
        "chapterId": "ch-evi-10",
        "subjectId": "law-evidence",
        "title": "Doctrine of Estoppel: Rules, Promissory & Tenant Estoppel",
        "subtitle": "BSA Sections 121–123 vs IEA Sections 115–117 & The Rule of Civil Conclusiveness",
        "learningObjective": "Master the Doctrine of Estoppel under Section 121 BSA / Section 115 IEA, its essential elements (representation, belief, altered position), rule of evidence vs substantive right, no estoppel against statute, Promissory Estoppel, and Tenant/Bailee estoppel under Sections 122 & 123 BSA / Sections 116 & 117 IEA.",
        "introduction": "Allegans contraria non est audiendus (he who alleges contrary things is not to be heard). Estoppel is an equitable principle preventing a person who has by representation intentionally led another to believe a thing to be true and act upon it, from subsequently denying the truth of that representation in litigation. It is a rule of evidence, shut out as a defence, not a cause of action.",
        "detailedExplanation": """
<h3>1. Statutory Codification: Section 121 BSA / Section 115 IEA</h3>
<p>When one person has, by their declaration, act, or omission, <strong>intentionally caused or permitted another person to believe a thing to be true and to act upon such belief</strong>, neither they nor their representative shall be allowed, in any suit or proceeding between themselves and such person or their representative, to <strong>deny the truth of that thing</strong>.</p>
<p><strong>Three Essential Ingredients (Pickard v. Sears / Sarat Chunder Dey):</strong></p>
<ol>
  <li>A representation made by one person to another;</li>
  <li>The representation was made with the intention that the other party should act upon it;</li>
  <li>The other party believed the representation and <strong>altered their position</strong> to their detriment based upon it.</li>
</ol>

<h3>2. Fundamental Limitations: No Estoppel Against Statute</h3>
<ul>
  <li><strong>Rule of Evidence, Not Cause of Action:</strong> Estoppel is a <strong>shield, not a sword</strong>; it cannot be made the foundation of a suit;</li>
  <li><strong>No Estoppel Against Statute:</strong> There can be no estoppel against a statute or public policy (e.g. an agreement entered into by a minor is void under S. 11 Contract Act; a minor cannot be estopped from pleading minority: <em>Mohori Bibee</em>);</li>
  <li><strong>No Estoppel Against Constitution:</strong> There can be no estoppel against fundamental rights (<em>Olga Tellis</em>).</li>
</ul>

<h3>3. Promissory Estoppel (Equitable Doctrine)</h3>
<p>Where one party has, by words or conduct, made to the other a clear and unequivocal promise which was intended to create legal relations and the other party has acted on it, the promisor cannot go back on the promise (<em>Motilal Padampat Sugar Mills v. State of U.P.</em>).</p>

<h3>4. Tenant & Licensee Estoppel: Section 122 BSA / Section 116 IEA</h3>
<p>No tenant of immovable property, or person claiming through such tenant, shall, <strong>during the continuance of the tenancy</strong>, be permitted to deny that the landlord of such tenant had, at the beginning of the tenancy, a <strong>title to such immovable property</strong>; and no person who came upon any immovable property by the licence of the person in possession thereof shall be permitted to deny that such person had title to such possession at the time when such licence was given.</p>
""",
        "keyProvisions": [
            {"section": "Section 121, BSA 2023 (S. 115 IEA)", "title": "Estoppel", "content": "Representation inducing altered position; bar on denying truth."},
            {"section": "Section 122, BSA 2023 (S. 116 IEA)", "title": "Estoppel of tenant and of licensee of person in possession", "content": "Bar on tenant denying landlord's title at commencement of tenancy."}
        ],
        "landmarkCases": [
            {"caseName": "Sarat Chunder Dey v. Gopal Chunder Laha", "citation": "(1892) 19 IA 203 (PC)", "bench": "Privy Council (Lord Shand)", "principle": "The main question in estoppel is not the state of mind of the person making the representation, but the effect of the representation on the mind of the person to whom it was made."},
            {"caseName": "Motilal Padampat Sugar Mills v. State of U.P.", "citation": "(1979) 2 SCC 409", "bench": "Supreme Court of India (Bhagwati J.)", "principle": "Promissory estoppel is an equitable principle enforceable against the Government where citizens alter their position acting upon governmental promises or tax exemptions."},
            {"caseName": "Bansraj Laltaprasad Mishra v. Stanley Parker Jones", "citation": "(2006) 3 SCC 91", "bench": "Supreme Court of India", "principle": "Section 116 estops the tenant from denying the landlord's title as long as the tenant remains in possession; to challenge title, the tenant must first surrender possession."}
        ],
        "comparativeTable": [
            {
                "title": "Doctrine of Estoppel Variants",
                "headers": ["Type of Estoppel", "Statutory Source (BSA / IEA)", "Key Threshold", "Rebuttal / Limitation"],
                "rows": [
                    ["Estoppel in Pais (Representation)", "Section 121 / Section 115", "Representation + Altered Position", "No estoppel against statute or minor"],
                    ["Tenant Estoppel", "Section 122 / Section 116", "Tenant in possession of land", "Operates during tenancy; must surrender first"],
                    ["Promissory Estoppel", "Equitable Common Law", "Unequivocal promise by state/party", "Overridden by overriding public interest"],
                    ["Bailee / Acceptor Estoppel", "Section 123 / Section 117", "Accepting bill / receiving goods", "Can show subsequent title delivery"]
                ]
            }
        ],
        "diagramId": "diag-evi-estoppel-types",
        "diagramExplanation": "Shows estoppel branches: Section 115 representation, Section 116 tenant estoppel, and promissory estoppel limits.",
        "prelimTraps": [
            {
                "trap": "Believing a minor who misrepresented his age to enter into a contract is estopped from pleading minority.",
                "reality": "Under Mohori Bibee and the principle 'No Estoppel Against Statute', a minor is NEVER estopped from pleading minority, because a contract with a minor is void ab initio under Section 11 Contract Act.",
                "rule": "There is no estoppel against a minor or against a statute."
            }
        ],
        "flashcards": [
            {
                "id": "fc-evi-10-01",
                "front": "What does Section 122 BSA / Section 116 IEA prohibit a tenant from doing during the continuance of tenancy?",
                "back": "Denying that the landlord had title to the immovable property at the beginning of the tenancy.",
                "category": "Tenant Estoppel"
            },
            {
                "id": "fc-evi-10-02",
                "front": "Can the doctrine of estoppel be invoked against the provisions of a mandatory statute?",
                "back": "No; it is an established rule of law that there can be NO ESTOPPEL AGAINST A STATUTE.",
                "category": "Estoppel Limitations"
            }
        ],
        "sourceReferences": [{"title": "Sections 121–123, Bharatiya Sakshya Adhiniyam, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-evi-10-02": {
        "topicId": "top-evi-10-02",
        "chapterId": "ch-evi-10",
        "subjectId": "law-evidence",
        "title": "Competency of Witnesses, Child/Dumb Witnesses & Privileged Comms",
        "subtitle": "BSA Sections 124–136 vs IEA Sections 118–134 & The Vadivelu Thevar Principle",
        "learningObjective": "Master witness competency (Section 124 BSA / S. 118 IEA), child witnesses, dumb witnesses communicating in writing/signs (Section 125 BSA / S. 119 IEA), privileged communications (marital S. 126, state affairs S. 127, attorney-client S. 132), and the Vadivelu Thevar principle: evidence is weighed, not counted (Section 136 BSA / S. 134 IEA).",
        "introduction": "Courts seek the truth from all who can perceive it. Section 118 IEA (now Section 124 BSA) establishes the universal capacity of all persons to testify unless prevented by extreme youth or infirmity. To protect sensitive societal institutions, the Code confers strict evidentiary privileges on matrimonial and legal professional communications, while emphasizing that evidence must be weighed, not counted.",
        "detailedExplanation": """
<h3>1. Who May Testify (Section 124 BSA / Section 118 IEA)</h3>
<p>All persons shall be <strong>competent to testify</strong> UNLESS the Court considers that they are <strong>prevented from understanding the questions</strong> put to them, or from giving <strong>rational answers</strong> to those questions, by tender years, extreme old age, disease, whether of body or mind, or any other cause of the same kind.</p>
<ul>
  <li><strong>Child Witness:</strong> A child of tender years is competent if they have intellectual capacity to understand questions and give rational answers (voir dire test);</li>
  <li><strong>Lunatic:</strong> A lunatic is not incompetent unless prevented by their lunacy from understanding questions.</li>
</ul>

<h3>2. Witness Unable to Communicate Verbally / Dumb Witness (Section 125 BSA / S. 119 IEA)</h3>
<p>A witness who is unable to speak may give their evidence in any other manner in which they can make it intelligible, as by <strong>writing or by signs</strong>; but such writing must be written and the signs made <strong>in open Court</strong>. Evidence so given <strong>shall be deemed to be ORAL EVIDENCE</strong>.</p>

<h3>3. Privileged Communications Architecture</h3>
<ol>
  <li><strong>Matrimonial Privilege (S. 126 BSA / S. 122 IEA):</strong> No person who is or has been married shall be compelled to disclose any communication made to them <strong>during marriage</strong> by their spouse; nor permitted to disclose it without consent of spouse, EXCEPT in suits between married persons or prosecutions for crimes against each other. (Privilege survives divorce or death of spouse!).</li>
  <li><strong>State Affairs (S. 127 BSA / S. 123 IEA):</strong> No one shall be permitted to give evidence derived from unpublished official records relating to any affairs of State without permission of head of department.</li>
  <li><strong>Professional Attorney-Client Privilege (S. 132 BSA / S. 126 IEA):</strong> No advocate shall at any time be permitted to disclose any communication made to them in the course and for the purpose of their employment, EXCEPT with client's express consent, or where made in furtherance of an <strong>illegal purpose</strong>.</li>
</ol>

<h3>4. Number of Witnesses & Vadivelu Thevar Principle (Section 136 BSA / Section 134 IEA)</h3>
<p><strong>'No particular number of witnesses shall in any case be required for the proof of any fact.'</strong></p>
<p>In <em>Vadivelu Thevar v. State of Madras</em> (1957), the Supreme Court laid down the immortal principle: <strong>'Evidence has to be WEIGHED and not COUNTED.'</strong> A conviction can be recorded on the sole testimony of a single reliable eyewitness without any corroboration.</p>
""",
        "keyProvisions": [
            {"section": "Section 124, BSA 2023 (S. 118 IEA)", "title": "Who may testify", "content": "Universal witness competency test: capacity to understand and give rational answers."},
            {"section": "Section 125, BSA 2023 (S. 119 IEA)", "title": "Witness unable to communicate verbally", "content": "Dumb witness signs/writing in open court deemed oral evidence."},
            {"section": "Section 126, BSA 2023 (S. 122 IEA)", "title": "Communications during marriage", "content": "Matrimonial privilege; survives divorce and death of spouse."},
            {"section": "Section 136, BSA 2023 (S. 134 IEA)", "title": "Number of witnesses", "content": "No particular number required; evidence is weighed, not counted."}
        ],
        "landmarkCases": [
            {"caseName": "Vadivelu Thevar v. State of Madras", "citation": "AIR 1957 SC 614", "bench": "Supreme Court of India (Sinha J.)", "principle": "Classified witnesses into 3 categories: wholly reliable, wholly unreliable, neither wholly reliable nor wholly unreliable; held conviction can rest on sole testimony of a wholly reliable witness."},
            {"caseName": "M.C. Verghese v. T.J. Poonnan", "citation": "(1969) 1 SCC 37", "bench": "Supreme Court of India (Shah J.)", "principle": "Matrimonial privilege under Section 122 applies to all communications made during the subsistence of marriage; the privilege continues even after the marriage is dissolved by divorce or death."}
        ],
        "comparativeTable": [
            {
                "title": "Privileged Communications Comparison",
                "headers": ["Type of Privilege", "Governing Section (BSA / IEA)", "Protected Relationship", "Duration of Shield"],
                "rows": [
                    ["Matrimonial Privilege", "Section 126 / Section 122", "Husband and Wife", "Survives divorce and death of spouse"],
                    ["State Affairs Privilege", "Section 127 / Section 123", "State Secrets / Public Interest", "Permanent (subject to judicial review)"],
                    ["Professional Legal Privilege", "Section 132 / Section 126", "Advocate and Client", "Permanent (even after retainer ends)"],
                    ["Information as to Crime", "Section 129 / Section 125", "Magistrate / Police Informant", "Absolute protection to source of info"]
                ]
            }
        ],
        "diagramId": "diag-evi-witness-examination-stages",
        "diagramExplanation": "Shows competency thresholds, open court sign language for dumb witnesses, and privileged communication shields.",
        "prelimTraps": [
            {
                "trap": "Believing matrimonial privilege under Section 122 IEA / Section 126 BSA expires once the husband and wife are divorced.",
                "reality": "In M.C. Verghese v. Poonnan, the Supreme Court held that the privilege for communications made DURING marriage SURVIVES divorce or death of the spouse.",
                "rule": "Matrimonial privilege survives divorce and death."
            }
        ],
        "flashcards": [
            {
                "id": "fc-evi-10-03",
                "front": "What does Section 136 BSA / Section 134 IEA declare regarding the number of witnesses required to prove a fact?",
                "back": "No particular number of witnesses shall in any case be required for the proof of any fact (evidence is weighed, not counted).",
                "category": "Number of Witnesses"
            },
            {
                "id": "fc-evi-10-04",
                "front": "How is evidence given by signs or writing in open court by a dumb witness treated under S. 125 BSA / S. 119 IEA?",
                "back": "It shall be deemed to be ORAL EVIDENCE.",
                "category": "Dumb Witnesses"
            }
        ],
        "sourceReferences": [{"title": "Sections 124–126, 136, Bharatiya Sakshya Adhiniyam, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-evi-10-03": {
        "topicId": "top-evi-10-03",
        "chapterId": "ch-evi-10",
        "subjectId": "law-evidence",
        "title": "Order of Examination: Chief, Cross, Re-Exam & Leading Questions",
        "subtitle": "BSA Sections 141–153 vs IEA Sections 135–153 & The Tactical Weapon of Cross-Examination",
        "learningObjective": "Master the three sequential stages of witness examination (Examination-in-Chief, Cross-Examination, Re-Examination under Section 142 BSA / S. 137 IEA), the definition of Leading Questions (Section 146 BSA / S. 141 IEA), when leading questions must not be asked, and when they may be asked as of right in cross-examination.",
        "introduction": "Trial is an adversarial truth-seeking journey. Chapter X regulates the orderly examination of witnesses in three stages. Cross-examination is hailed as the greatest legal engine ever invented for the discovery of truth. The Code strictly controls leading questions to prevent parties from putting words into the mouths of their own witnesses while granting free reign in cross-examination.",
        "detailedExplanation": """
<h3>1. The Three Sequential Stages of Examination (Section 142 BSA / Section 137 & 138 IEA)</h3>
<ol>
  <li><strong>Examination-in-Chief:</strong> The examination of a witness by the party who calls them. Purpose: to elicit the witness's version of facts supporting the calling party.</li>
  <li><strong>Cross-Examination:</strong> The examination of a witness by the <strong>adverse party</strong>. Must relate to relevant facts, but need NOT be confined to the facts to which the witness testified on examination-in-chief! Purpose: to test veracity, discover who they are, and shake credit.</li>
  <li><strong>Re-Examination:</strong> The examination of the witness, subsequent to cross-examination, by the party who called them. <strong>Direction of Re-Exam:</strong> Shall be directed to the <strong>explanation of matters referred to in cross-examination</strong>; and if new matter is introduced with court permission, adverse party may further cross-examine upon that matter.</li>
</ol>

<h3>2. Leading Questions Defined (Section 146 BSA / Section 141 IEA)</h3>
<p>Any question <strong>suggesting the answer which the person putting it wishes or expects to receive</strong>, is called a <strong>Leading Question</strong>. (e.g. 'Did you see A running with a bloody knife at 10 PM?' instead of 'What did you see?').</p>

<h3>3. When Leading Questions Must NOT Be Asked (Section 147 BSA / Section 142 IEA)</h3>
<p>Leading questions <strong>MUST NOT, if objected to by the adverse party, be asked in an Examination-in-Chief, or in a Re-Examination</strong>, except with the permission of the Court.</p>
<p><strong>Court's Discretion to Permit:</strong> The Court shall permit leading questions in chief/re-exam as to matters which are <strong>introductory or undisputed</strong>, or which have, in its opinion, been already sufficiently proved.</p>

<h3>4. Leading Questions in Cross-Examination: Absolute Right (Section 148 BSA / S. 143 IEA)</h3>
<p><strong>Leading questions MAY be asked in Cross-Examination.</strong> The adverse party has an unfettered statutory right to put leading questions to test the witness's answers and dismantle their narrative.</p>

<h3>5. Cross-Examination as to Previous Statements (Section 148 BSA / Section 145 IEA)</h3>
<p>A witness may be cross-examined as to <strong>previous statements made by them in writing or reduced into writing</strong>, without such writing being shown to them or being proved. BUT if it is intended to <strong>CONTRADICT</strong> them by the writing, their attention must, before the writing can be proved, be <strong>called to those parts of it which are to be used for the purpose of contradicting them</strong> (Tahsildar Singh rule).</p>
""",
        "keyProvisions": [
            {"section": "Section 142, BSA 2023 (S. 137 & 138 IEA)", "title": "Order of examinations", "content": "Chief, Cross, Re-Examination sequential order and statutory scope."},
            {"section": "Section 146, BSA 2023 (S. 141 IEA)", "title": "Leading questions defined", "content": "Question suggesting the desired answer."},
            {"section": "Section 147 & 148, BSA 2023 (S. 142 & 143 IEA)", "title": "When leading questions may and must not be asked", "content": "Barred in Chief/Re-Exam (save introductory); permitted as of right in Cross-Exam."}
        ],
        "landmarkCases": [
            {"caseName": "Tahsildar Singh v. State of U.P.", "citation": "AIR 1959 SC 1012", "bench": "Six-Judge Constitution Bench", "principle": "To contradict a witness under Section 145, their attention must first be drawn specifically to the contradictory passage in their previous police statement to afford them an opportunity to explain."},
            {"caseName": "V.K. Sasikala v. State", "citation": "(2012) 9 SCC 771", "bench": "Supreme Court of India", "principle": "Cross-examination is an essential pillar of a fair trial under Article 21; denial of opportunity to cross-examine prosecution witnesses vitiates trial."}
        ],
        "comparativeTable": [
            {
                "title": "Stages of Witness Examination Comparison",
                "headers": ["Stage", "Conducted By", "Scope of Questioning", "Leading Questions Permitted?"],
                "rows": [
                    ["Examination-in-Chief", "Calling party", "Relevant facts supporting case", "NO (save introductory/undisputed)"],
                    ["Cross-Examination", "Adverse party", "All relevant facts + credibility", "YES (Absolute statutory right)"],
                    ["Re-Examination", "Calling party", "Explanation of cross-exam points", "NO (save with court leave)"]
                ]
            }
        ],
        "diagramId": "diag-evi-witness-examination-stages",
        "diagramExplanation": "Shows trial sequence: Examination-in-Chief (no leading), Cross-Examination (leading allowed), and Re-Examination (clarification only).",
        "prelimTraps": [
            {
                "trap": "Believing cross-examination is strictly confined to the facts testified to by the witness during examination-in-chief.",
                "reality": "Section 138 IEA / Section 142(2) BSA explicitly provides that cross-examination NEED NOT BE CONFINED to the facts to which the witness testified in their examination-in-chief.",
                "rule": "Cross-examination can cover any relevant fact, not just matters in chief."
            }
        ],
        "flashcards": [
            {
                "id": "fc-evi-10-05",
                "front": "Can leading questions be asked in Cross-Examination under Section 148 BSA / Section 143 IEA?",
                "back": "YES; leading questions may be asked in Cross-Examination as of right.",
                "category": "Leading Questions"
            },
            {
                "id": "fc-evi-10-06",
                "front": "What must be done under Section 145 IEA / Section 148 BSA before a witness can be contradicted by their previous writing?",
                "back": "Their attention must be called to those parts of the writing which are to be used for contradicting them.",
                "category": "Witness Contradiction"
            }
        ],
        "sourceReferences": [{"title": "Sections 141–153, Bharatiya Sakshya Adhiniyam, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-evi-10-04": {
        "topicId": "top-evi-10-04",
        "chapterId": "ch-evi-10",
        "subjectId": "law-evidence",
        "title": "Impeaching Credit, Hostile Witnesses & Refreshing Memory",
        "subtitle": "BSA Sections 154–165 vs IEA Sections 154–165 & The Sat Paul Evidentiary Doctrine",
        "learningObjective": "Master hostile witnesses under Section 157 BSA / Section 154 IEA, the landmark Sat Paul doctrine (evidence of hostile witness not wiped off record), impeaching witness credit (Section 158 BSA / S. 155 IEA), refreshing memory (Section 162 BSA / S. 159 IEA), and the Judge's extraordinary power to question under Section 168 BSA / Section 165 IEA.",
        "introduction": "When a witness turns against the party that called them, justice must not be derailed. Section 154 IEA (now Section 157 BSA) permits a party to cross-examine their own witness with court permission. Indian law rejects the English doctrine that a hostile witness's testimony is completely discredited; rather, the evidence remains on record and can be relied upon to the extent it supports the truth.",
        "detailedExplanation": """
<h3>1. Hostile Witness: Questions by Party to Own Witness (Section 157 BSA / Section 154 IEA)</h3>
<p>The Court may, in its discretion, permit the person who calls a witness to <strong>put any questions to him which might be put in cross-examination by the adverse party</strong> (i.e. leading questions and questions shaking credit).</p>
<p><strong>Section 154(2) IEA / Section 157(2) BSA (2006 Amendment):</strong> Nothing in this section shall disentitle the person so permitted from relying on any part of the evidence of such witness.</p>

<h3>2. The Sat Paul Doctrine: Evidentiary Value of Hostile Witness</h3>
<p>In <em>Sat Paul v. Delhi Administration</em> (1976), the Supreme Court held:</p>
<ul>
  <li>The evidence of a hostile witness <strong>does not become completely effaced from the record</strong>;</li>
  <li>It is not rejected in toto;</li>
  <li>That part of the evidence of a hostile witness which is <strong>found to be trustworthy and corroborated by other evidence can be relied upon by either the prosecution or the defence</strong>!</li>
</ul>

<h3>3. Impeaching Credit of Witness (Section 158 BSA / Section 155 IEA)</h3>
<p>The credit of a witness may be impeached by the adverse party, or by the party who calls them (with court leave):</p>
<ol>
  <li>By testimony of persons who say they believe the witness to be <strong>unworthy of credit on oath</strong>;</li>
  <li>By proof that the witness has been <strong>bribed</strong>, or has accepted the offer of a bribe;</li>
  <li>By proof of <strong>former statements inconsistent</strong> with any part of their evidence which is liable to be contradicted.</li>
</ol>

<h3>4. Refreshing Memory (Section 162 BSA / Section 159 IEA)</h3>
<p>A witness may, while under examination, refresh their memory by referring to <strong>any writing made by himself at the time of the transaction</strong>, or so soon afterwards that the transaction was at that time fresh in his memory. A witness may also refer to a writing made by any other person and read by the witness within such time if they knew it to be correct.</p>

<h3>5. Judge's Extraordinary Power to Question: Section 168 BSA / Section 165 IEA</h3>
<p>The Judge may, in order to discover or obtain proper proof of relevant facts, <strong>ask any question he pleases, in any form, at any time, of any witness, or of the parties about any fact relevant or irrelevant</strong>, and may order production of any document or thing. <strong>Limitations:</strong> Judgment must be based upon facts declared relevant by the Act and duly proved; Judge cannot compel answers to privileged questions.</p>
""",
        "keyProvisions": [
            {"section": "Section 157, BSA 2023 (S. 154 IEA)", "title": "Question by party to his own witness", "content": "Hostile witness; court permission to cross-examine own witness and rely on credible parts."},
            {"section": "Section 158, BSA 2023 (S. 155 IEA)", "title": "Impeaching credit of witness", "content": "Three statutory modes of impeaching credit: unworthiness on oath, bribe, inconsistent statements."},
            {"section": "Section 162, BSA 2023 (S. 159 IEA)", "title": "Refreshing memory", "content": "Witness permitted to refresh memory from contemporaneous writing."},
            {"section": "Section 168, BSA 2023 (S. 165 IEA)", "title": "Judge's power to put questions or order production", "content": "Extraordinary judicial power to question on any relevant or irrelevant fact to discover truth."}
        ],
        "landmarkCases": [
            {"caseName": "Sat Paul v. Delhi Administration", "citation": "(1976) 1 SCC 727", "bench": "Supreme Court of India (Sarkaria J.)", "principle": "The testimony of a hostile witness does not wash off the record; courts can accept and act upon those parts of the statement which are found consistent with truth."},
            {"caseName": "State of Rajasthan v. Teja Ram", "citation": "(1999) 3 SCC 507", "bench": "Supreme Court of India", "principle": "Section 165 IEA invests the trial judge with immense powers to actively participate in the trial to search for truth; judges are not mere passive umpires."}
        ],
        "comparativeTable": [
            {
                "title": "Hostile Witness & Impeachment Matrix",
                "headers": ["Aspect", "IEA 1872 Provision", "BSA 2023 Provision", "Legal Effect"],
                "rows": [
                    ["Cross-Examining Own Witness", "Section 154(1)", "Section 157(1)", "Court leave required; treats as hostile"],
                    ["Relying on Hostile Testimony", "Section 154(2) (2006)", "Section 157(2)", "Calling party may rely on favorable parts"],
                    ["Impeaching Credit", "Section 155", "Section 158", "Attacking unworthiness on oath or bribes"],
                    ["Refreshing Memory", "Section 159", "Section 162", "Allowed from contemporaneous writings"],
                    ["Judge's Questioning Powers", "Section 165", "Section 168", "Unlimited questions to discover truth"]
                ]
            }
        ],
        "diagramId": "diag-evi-witness-examination-stages",
        "diagramExplanation": "Shows hostile witness procedure under Section 154, Sat Paul partial reliance doctrine, and Section 165 judge's questioning powers.",
        "prelimTraps": [
            {
                "trap": "Believing the testimony of a hostile witness must be rejected in its entirety by the court.",
                "reality": "Under the Sat Paul doctrine and Section 154(2) IEA / Section 157(2) BSA, the evidence of a hostile witness is NOT wiped off the record. It can be relied upon by either party to the extent found trustworthy and corroborated.",
                "rule": "Hostile witness testimony is not rejected in toto; trustworthy parts remain admissible."
            }
        ],
        "flashcards": [
            {
                "id": "fc-evi-10-07",
                "front": "What landmark Supreme Court judgment settled that the testimony of a hostile witness is not wiped off the record?",
                "back": "Sat Paul v. Delhi Administration (1976) [Sarkaria J.].",
                "category": "Hostile Witnesses"
            },
            {
                "id": "fc-evi-10-08",
                "front": "What section of the Evidence Act / BSA empowers the Judge to ask any question he pleases, relevant or irrelevant, to discover truth?",
                "back": "Section 168 BSA 2023 / Section 165 Indian Evidence Act, 1872.",
                "category": "Judge's Powers"
            }
        ],
        "sourceReferences": [{"title": "Sections 154–168, Bharatiya Sakshya Adhiniyam, 2023", "url": "https://www.mha.gov.in"}]
    }
}

# Write complete Part 3
content = f"""/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Law of Evidence Module — Authored Concepts (Part 3: Ch 8 to 10)
 * Topics: top-evi-08-01 to top-evi-10-04 (9 Comprehensive Topics)
 */

(function (global) {{
  'use strict';

  const DATA = {json.dumps(CONCEPTS, indent=2)};

  global.EVIDENCE_CONCEPTS_PART3 = DATA;
  if (typeof module !== 'undefined' && module.exports) {{
    module.exports = DATA;
  }}
}})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
"""

with open("assets/learning/data/evidence/evidence-concepts-part3.js", "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully generated assets/learning/data/evidence/evidence-concepts-part3.js ({len(CONCEPTS)} topics)")
