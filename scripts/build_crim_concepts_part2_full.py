"""
Builder for Criminal Law Concepts Part 2 (Chapters 5 to 8: 14 Topics)
- Chapter 5: top-crim-05-01, top-crim-05-02, top-crim-05-03, top-crim-05-04
- Chapter 6: top-crim-06-01, top-crim-06-02, top-crim-06-03, top-crim-06-04
- Chapter 7: top-crim-07-01, top-crim-07-02, top-crim-07-03
- Chapter 8: top-crim-08-01, top-crim-08-02, top-crim-08-03
Output: assets/learning/data/criminal/criminal-concepts-part2.js
"""

import json

CONCEPTS = {
    # -------------------------------------------------------------------------
    # CHAPTER 5: INCHOATE CRIMES & JOINT LIABILITY
    # -------------------------------------------------------------------------
    "top-crim-05-01": {
        "topicId": "top-crim-05-01",
        "chapterId": "ch-crim-05",
        "subjectId": "law-criminal",
        "title": "Common Intention vs Common Object: Joint Criminal Liability",
        "subtitle": "BNS Section 3(5) (Section 34 IPC) versus BNS Section 190 (Section 149 IPC)",
        "learningObjective": "Master the cardinal distinctions between joint liability based on common intention under Section 3(5) BNS / Section 34 IPC and constructive liability based on common object under Section 190 BNS / Section 149 IPC.",
        "introduction": "Joint criminal liability creates vicarious responsibility for crimes committed by groups. Section 3(5) of the Bharatiya Nyaya Sanhita, 2023 (formerly Section 34 IPC) embodies the principle of common intention, holding each co-actor liable as if the act was done by him alone. Section 190 BNS (formerly Section 149 IPC) imposes constructive liability on every member of an unlawful assembly for acts done in prosecution of the common object.",
        "detailedExplanation": """
<h3>1. Common Intention: Section 3(5) BNS / Section 34 IPC</h3>
<p>When a criminal act is done by several persons in furtherance of the common intention of all, each of such persons is liable for that act in the same manner as if it were done by him alone.</p>
<p><strong>Essential Ingredients:</strong></p>
<ol>
  <li>Criminal act done by several persons (minimum two persons);</li>
  <li>Done in <em>furtherance of the common intention</em> of all;</li>
  <li>Participation of each accused in some manner in the act (physical presence or active participation per <em>Barendra Kumar Ghosh</em>).</li>
</ol>
<p><strong>Common Intention vs Same Intention:</strong> In <em>Mahbub Shah v. Emperor</em> (AIR 1945 PC 118), the Privy Council established that common intention implies a pre-arranged plan and prior concert—a meeting of minds. Several persons may simultaneously entertain the same intention to attack a victim, but without a prior concert or meeting of minds, Section 3(5) BNS / Section 34 IPC cannot be invoked.</p>

<h3>2. Common Object: Section 190 BNS / Section 149 IPC</h3>
<p>If an offence is committed by any member of an unlawful assembly in prosecution of the common object of that assembly, or such as the members of that assembly knew to be likely to be committed in prosecution of that object, every person who, at the time of the committing of that offence, is a member of the same assembly, is guilty of that offence.</p>
<p><strong>Essential Ingredients:</strong></p>
<ol>
  <li>Unlawful assembly of <strong>five or more persons</strong> (defined in Section 189 BNS / Section 141 IPC);</li>
  <li>Commission of an offence by any member of the assembly;</li>
  <li>Offence committed in prosecution of common object, OR an offence which members knew was likely to be committed.</li>
</ol>
""",
        "quickRevisionPoints": [
            "Former Section 34 IPC is now Section 3(5) BNS (Common Intention).",
            "Former Section 149 IPC is now Section 190 BNS (Common Object).",
            "Common Intention: Min 2 persons; pre-arranged plan/prior meeting of minds; active participation; creates rule of evidence.",
            "Common Object: Min 5 persons; membership of unlawful assembly suffices; creates a distinct substantive offence.",
            "Same intention is NOT common intention (Mahbub Shah v. Emperor)."
        ],
        "provisions": [
            {
                "article": "Section 3(5) BNS",
                "title": "Joint Liability: Common Intention",
                "text": "When a criminal act is done by several persons in furtherance of the common intention of all, each of such persons is liable for that act in the same manner as if it were done by him alone.",
                "breakdown": "Relocates historical Section 34 IPC verbatim into Chapter I of BNS."
            },
            {
                "article": "Section 190 BNS",
                "title": "Every member of unlawful assembly guilty of offence committed in prosecution of common object",
                "text": "If an offence is committed by any member of an unlawful assembly in prosecution of the common object... every person who at that time is a member is guilty.",
                "breakdown": "Corresponds to Section 149 IPC. Imposes constructive substantive penal liability."
            }
        ],
        "definitions": [
            {"term": "Common Intention", "definition": "A pre-oriented meeting of minds and shared purpose prior to or at the time of committing the criminal act."},
            {"term": "Common Object", "definition": "A shared unlawful purpose falling within the five statutory categories of Section 189 BNS / Section 141 IPC."}
        ],
        "ingredients": ["Active participation in physical execution for S. 3(5) BNS.", "Membership of assembly of 5+ persons with common object for S. 190 BNS."],
        "exceptions": ["Mere presence at the scene without sharing the common intention or common object does not attract joint liability."],
        "examples": [
            {"scenario": "A and B stand outside a post office guarding the door while C shoots the postmaster inside during a robbery.", "application": "A and B are equally guilty of murder under Section 103 read with Section 3(5) BNS / S. 34 IPC (Barendra Kumar Ghosh v. Emperor)."}
        ],
        "landmarkCases": [
            {
                "case": "Barendra Kumar Ghosh v. Emperor",
                "citation": "AIR 1925 PC 1",
                "year": "1925",
                "bench": "Lord Sumner",
                "ratio": "'They also serve who only stand and wait.' Participation in action with a shared common intention suffices; physical firing of the fatal shot by the individual accused is not required.",
                "impact": "Foundational precedent establishing vicarious joint liability under Section 34 IPC / Section 3(5) BNS."
            },
            {
                "case": "Mahbub Shah v. Emperor",
                "citation": "AIR 1945 PC 118",
                "year": "1945",
                "bench": "Sir Madhavan Nair",
                "ratio": "Care must be taken not to confuse the same or similar intention with common intention. Common intention requires a pre-arranged plan and meeting of minds; same intention does not attract joint liability under Section 34.",
                "impact": "Established the indispensable requirement of prior concert."
            }
        ],
        "comparisonTables": [
            {
                "title": "Common Intention (S. 3(5) BNS) vs Common Object (S. 190 BNS)",
                "headers": ["Point of Distinction", "Common Intention (S. 3(5) BNS / S. 34 IPC)", "Common Object (S. 190 BNS / S. 149 IPC)"],
                "rows": [
                    ["Minimum Persons", "Two (2) persons", "Five (5) persons"],
                    ["Nature of Provision", "Rule of evidence / liability; creates no separate offence", "Creates a specific, independent substantive offence"],
                    ["Mental Nexus", "Pre-arranged plan / prior meeting of minds", "Shared common object under S. 189 BNS"],
                    ["Participation", "Active participation in execution is essential", "Active participation not required; membership suffices"],
                    ["IPC Equivalent", "Section 34 IPC", "Section 149 IPC"]
                ]
            }
        ],
        "diagramId": "diag-crim-joint-liability-common-intention",
        "diagramExplanation": "Diagram compares the bilateral structure of Common Intention vs the collective framework of Common Object.",
        "prelimTraps": [
            {
                "trap": "Believing a person can be convicted under Section 34 IPC / Section 3(5) BNS alone without any substantive section.",
                "reality": "Section 3(5) BNS / Section 34 IPC does not create a substantive offence; it is always read with a substantive offence (e.g. S. 103 read with S. 3(5)).",
                "rule": "Section 3(5) BNS is a rule of joint liability, not an independent crime."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crim-05-01",
                "front": "Where is the principle of Common Intention (formerly Section 34 IPC) codified in BNS 2023?",
                "back": "Section 3, sub-section (5) of BNS 2023.",
                "category": "Joint Liability"
            },
            {
                "id": "fc-crim-05-02",
                "front": "What is the minimum number of persons required for Common Intention and Common Object respectively?",
                "back": "Common Intention = Minimum 2 persons; Common Object = Minimum 5 persons.",
                "category": "Joint Liability"
            }
        ],
        "sourceReferences": [{"title": "Sections 3(5), 189, 190, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-crim-05-02": {
        "topicId": "top-crim-05-02",
        "chapterId": "ch-crim-05",
        "subjectId": "law-criminal",
        "title": "Abetment: Instigation, Conspiracy & Intentional Aiding",
        "subtitle": "BNS Sections 45–60 vs IPC Sections 107–120 & The Three Forms of Abetment",
        "learningObjective": "Master the three statutory modes of abetment under Section 45 BNS (Section 107 IPC): Instigation, Conspiracy, and Intentional Aiding, and penal consequences where the act abetted is or is not committed.",
        "introduction": "He who acts through another acts himself (<em>Qui facit per alium facit per se</em>). Section 45 of the Bharatiya Nyaya Sanhita, 2023 (formerly Section 107 IPC) penalizes persons who promote, facilitate, or incite the commission of an offence through instigation, conspiracy, or intentional aiding. The abettor is distinct from the principal perpetrator but bears full criminal liability.",
        "detailedExplanation": """
<h3>1. The Three Modes of Abetment (Section 45 BNS / Section 107 IPC)</h3>
<p>A person abets the doing of a thing who:</p>
<ol>
  <li><strong>First (Instigation):</strong> Instigates any person to do that thing (provoking, inciting, urging, or encouraging).</li>
  <li><strong>Secondly (Conspiracy):</strong> Engages with one or more other person or persons in any conspiracy for the doing of that thing, if an act or illegal omission takes place in pursuance of that conspiracy.</li>
  <li><strong>Thirdly (Intentional Aiding):</strong> Intentionally aids, by any act or illegal omission, the doing of that thing.</li>
</ol>
<p><strong>Explanation 1 (Wilful Misrepresentation):</strong> A person who by wilful misrepresentation, or by wilful concealment of a material fact which he is bound to disclose, voluntarily causes or procures a thing to be done, is said to instigate.</p>
<p><strong>Explanation 2 (Prior or Simultaneous Aiding):</strong> Doing an act prior to or at the time of commission to facilitate the crime constitutes intentional aiding.</p>

<h3>2. The Abettor (Section 46 BNS / Section 108 IPC)</h3>
<p>A person abets an offence who abets either the commission of an offence, or the commission of an act which would be an offence if committed by a person capable by law of committing an offence with the same intention or knowledge as that of the abettor.</p>
<ul>
  <li>It is NOT necessary that the act abetted should be committed (Explanation 2).</li>
  <li>It is NOT necessary that the person abetted should be capable by law of committing an offence (e.g. A instigates a child under 7 or a lunatic to kill Z; A is guilty of abetment of murder, though the child/lunatic is immune).</li>
  <li>Abetment of an abetment is an offence (Explanation 4).</li>
</ul>
""",
        "quickRevisionPoints": [
            "Section 45 BNS (S. 107 IPC) specifies 3 modes of abetment: Instigation, Conspiracy, Intentional Aiding.",
            "Abettor defined in Section 46 BNS (S. 108 IPC).",
            "Act abetted need NOT be committed for abetment offence to be complete (S. 46 Expl. 2).",
            "Abetment of child/lunatic: Abettor is liable even if agent is immune (S. 46 Expl. 3).",
            "Abetment of an abetment is an offence (S. 46 Expl. 4)."
        ],
        "provisions": [
            {
                "article": "Section 45 BNS",
                "title": "Abetment of a thing",
                "text": "A person abets the doing of a thing, who: (a) instigates any person to do that thing; or (b) engages in conspiracy...; or (c) intentionally aids by any act or illegal omission...",
                "breakdown": "Corresponds to Section 107 IPC with tripartite classification."
            }
        ],
        "definitions": [
            {"term": "Instigation", "definition": "Actively prompting, encouraging, soliciting, or urging a person to commit an offence."},
            {"term": "Intentional Aiding", "definition": "Facilitating the commission of a crime by prior or contemporaneous physical act or illegal omission."}
        ],
        "ingredients": ["Mental element of intention to facilitate crime.", "Performance of act of instigation, conspiracy, or aiding."],
        "exceptions": ["Mere passive presence or knowledge without active encouragement is not abetment."],
        "examples": [
            {"scenario": "A tells a 6-year-old child to place poison into B's drink; the child does so and B dies.", "application": "The child is immune under Section 20 BNS / S. 82 IPC (doli incapax), but A is guilty of abetment of murder under Section 46 Explanation 3 BNS / Section 108 Explanation 3 IPC."}
        ],
        "landmarkCases": [
            {
                "case": "Queen v. Mohit",
                "citation": "(1871) 3 NWP 316",
                "year": "1871",
                "bench": "Allahabad High Court",
                "ratio": "Persons who followed a woman to the pyre shouting 'Sati Sati' were held guilty of abetment of suicide by instigation, as their continuous cheering actively encouraged the fatal act.",
                "impact": "Classic authority on instigation through verbal active encouragement."
            }
        ],
        "comparisonTables": [
            {
                "title": "The Three Modes of Abetment",
                "headers": ["Mode", "Section 45 Clause", "Essential Requirement"],
                "rows": [
                    ["Instigation", "Clause (a)", "Active incitement, urging, or misrepresentation"],
                    ["Conspiracy", "Clause (b)", "Agreement + Act/illegal omission in pursuance"],
                    ["Intentional Aiding", "Clause (c)", "Facilitation prior to or at time of commission"]
                ]
            }
        ],
        "diagramId": "diag-crim-mens-rea-liability",
        "diagramExplanation": "Diagram charts abetment as an inchoate offence complete upon encouragement.",
        "prelimTraps": [
            {
                "trap": "Believing an abettor cannot be convicted if the person abetted refuses to commit the crime.",
                "reality": "Under Section 46 Explanation 2 BNS / Section 108 IPC, the offence of abetment is complete the moment instigation takes place.",
                "rule": "Abetment does NOT require commission of the abetted act."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crim-05-03",
                "front": "What are the three statutory modes of abetment in Section 45 BNS / Section 107 IPC?",
                "back": "1. Instigation; 2. Conspiracy; 3. Intentional Aiding.",
                "category": "Abetment"
            },
            {
                "id": "fc-crim-05-04",
                "front": "Is abetment of an abetment punishable under penal law?",
                "back": "Yes, Section 46 Explanation 4 BNS / Section 108 Explanation 4 IPC explicitly makes abetment of an abetment an offence.",
                "category": "Abetment"
            }
        ],
        "sourceReferences": [{"title": "Sections 45, 46, 47, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-crim-05-03": {
        "topicId": "top-crim-05-03",
        "chapterId": "ch-crim-05",
        "subjectId": "law-criminal",
        "title": "Criminal Conspiracy: Agreement, Mens Rea & Evidence",
        "subtitle": "BNS Section 61 vs IPC Sections 120A & 120B & The Agreement as Actus Reus",
        "learningObjective": "Master the substantive offence of Criminal Conspiracy under Section 61 BNS (formerly Sections 120A & 120B IPC), focusing on the agreement itself constituting the actus reus.",
        "introduction": "Criminal conspiracy is a partnership in crime. While abetment by conspiracy under Section 45 requires an overt act done in pursuance of the agreement, the substantive offence of Criminal Conspiracy under Section 61 BNS (formerly Sections 120A & 120B IPC) treats the mere agreement to commit an offence as the complete actus reus, without requiring any overt act whatsoever.",
        "detailedExplanation": """
<h3>1. Statutory Definition: Section 61(1) BNS / Section 120A IPC</h3>
<p>When two or more persons agree to do, or cause to be done:</p>
<ol>
  <li>An <strong>illegal act</strong>; OR</li>
  <li>An act which is not illegal by <strong>illegal means</strong>,</li>
</ol>
<p>such an agreement is designated a criminal conspiracy.</p>
<p><strong>The Crucial Proviso:</strong> Provided that no agreement except an agreement to commit an <strong>offence</strong> shall amount to a criminal conspiracy unless some act besides the agreement is done by one or more parties to such agreement in pursuance thereof.</p>
<ul>
  <li>If agreement is to commit an <strong>offence</strong>: The mere agreement constitutes the completed crime (no overt act needed).</li>
  <li>If agreement is to do an <strong>illegal act not amounting to an offence</strong> (e.g. civil tort): An overt act in pursuance of the agreement is mandatory.</li>
</ul>

<h3>2. Punishment: Section 61(2) BNS / Section 120B IPC</h3>
<ul>
  <li>Conspiracy to commit offence punishable with death, life imprisonment, or rigorous imprisonment for 2+ years: Punished in the same manner as if the accused had abetted the offence.</li>
  <li>Conspiracy to commit other offences: Imprisonment up to <strong>six months</strong>, or fine, or both.</li>
</ul>

<h3>3. Evidentiary Rule: Section 8 BSA / Section 10 IEA</h3>
<p>Because conspiracies are hatched in secret, direct evidence is rarely available. Under Section 8 BSA (formerly S. 10 IEA), once reasonable ground exists to believe two persons have conspired, anything said, done, or written by any one of them in reference to their common intention is admissible against all conspirators.</p>
""",
        "quickRevisionPoints": [
            "Criminal conspiracy is consolidated into Section 61 BNS (formerly Sections 120A & 120B IPC).",
            "Minimum 2 persons required for conspiracy.",
            "Agreement to commit an OFFENCE requires NO overt act; agreement itself is the crime.",
            "Agreement for non-offence illegal act REQUIRES an overt act in pursuance.",
            "Punishment: Same as abetment if offence carries death/life/2+ yrs RI; otherwise max 6 months."
        ],
        "provisions": [
            {
                "article": "Section 61 BNS",
                "title": "Criminal Conspiracy",
                "text": "When two or more persons agree to do, or cause to be done: (a) an illegal act; or (b) an act which is not illegal by illegal means, such an agreement is designated a criminal conspiracy... (2) punishment scale.",
                "breakdown": "Consolidates Section 120A (definition) and Section 120B (punishment) IPC into a single section."
            }
        ],
        "definitions": [{"term": "Criminal Conspiracy", "definition": "An agreement between two or more persons to commit an illegal act or a legal act by illegal means."}],
        "ingredients": ["Agreement between two or more persons.", "Shared unlawful purpose or unlawful means."],
        "exceptions": ["Husband and wife alone under traditional English common law could not conspire; under Indian law, husband and wife CAN commit criminal conspiracy."],
        "examples": [
            {"scenario": "A and B agree in a coffee shop to burgle a jewellery store tomorrow night; before they take any further step, police arrest them upon wiretap evidence.", "application": "Both are guilty of criminal conspiracy under Section 61 BNS / S. 120B IPC; the agreement to commit an offence constitutes the completed crime."}
        ],
        "landmarkCases": [
            {
                "case": "State (NCT of Delhi) v. Navjot Sandhu (Parliament Attack Case)",
                "citation": "(2005) 11 SCC 600",
                "year": "2005",
                "bench": "P.V. Reddi J",
                "ratio": "The essence of criminal conspiracy is the unlawful agreement. It is not necessary that every conspirator must know every detail of the conspiracy, or participate in every stage. Conspirators may enter the conspiracy at different times and join in various ways.",
                "impact": "Authoritative modern precedent on proof of conspiracy through circumstantial evidence."
            }
        ],
        "comparisonTables": [
            {
                "title": "Abetment by Conspiracy (S. 45) vs Substantive Conspiracy (S. 61)",
                "headers": ["Metric", "Abetment by Conspiracy (S. 45 BNS / S. 107 IPC)", "Criminal Conspiracy (S. 61 BNS / S. 120A IPC)"],
                "rows": [
                    ["Overt Act Requirement", "MANDATORY: Act or illegal omission must take place", "NOT required if agreement is to commit an offence"],
                    ["Nature", "A mode of abetting another crime", "An independent substantive offence in itself"],
                    ["Placement", "Chapter IV (General Abetment)", "Chapter IV (Section 61)"],
                    ["IPC Equivalent", "Section 107 (Clause Secondly) IPC", "Sections 120A & 120B IPC (Added in 1913)"]
                ]
            }
        ],
        "diagramId": "diag-crim-mens-rea-liability",
        "diagramExplanation": "Diagram charts the agreement as the completed actus reus in criminal conspiracy.",
        "prelimTraps": [
            {
                "trap": "Believing an overt act is always required for criminal conspiracy under Indian law.",
                "reality": "Under Section 61 Proviso BNS / Section 120A Proviso IPC, an agreement to commit an OFFENCE requires NO overt act.",
                "rule": "Conspiracy to commit an offence = Agreement ALONE is punishable."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crim-05-05",
                "front": "Where is the substantive offence of Criminal Conspiracy codified in BNS 2023?",
                "back": "Section 61 BNS 2023 (formerly Sections 120A and 120B IPC).",
                "category": "Criminal Conspiracy"
            },
            {
                "id": "fc-crim-05-06",
                "front": "When is an overt act required to constitute criminal conspiracy?",
                "back": "Only when the agreement is to do an illegal act NOT amounting to an offence (Section 61 Proviso BNS).",
                "category": "Criminal Conspiracy"
            }
        ],
        "sourceReferences": [{"title": "Section 61, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-crim-05-04": {
        "topicId": "top-crim-05-04",
        "chapterId": "ch-crim-05",
        "subjectId": "law-criminal",
        "title": "Criminal Attempt: Preparation vs Attempt & Proximity Test",
        "subtitle": "BNS Section 62 vs IPC Section 511 & The Impossible Attempt Doctrine",
        "learningObjective": "Master the general attempt provision under Section 62 BNS (formerly Section 511 IPC), exploring the boundary between preparation and attempt, the proximity test, and impossibility in attempts.",
        "introduction": "An attempt is an intentional preparatory act that has progressed so close to the completed crime that it would have succeeded but for some unexpected intervention or failure. Section 62 of the Bharatiya Nyaya Sanhita, 2023 (formerly Section 511 IPC, which was the final section of the IPC) provides the general residual punishment for attempting to commit offences.",
        "detailedExplanation": """
<h3>1. Statutory Provision: Section 62 BNS / Section 511 IPC</h3>
<p>Whoever attempts to commit an offence punishable by this Sanhita with imprisonment for life or imprisonment, or to cause such an offence to be committed, and in such attempt does any act towards the commission of the offence, shall, where no express provision is made by this Sanhita for the punishment of such attempt, be punished with <strong>imprisonment of any description provided for the offence, for a term which may extend to one-half (1/2) of the imprisonment for life or, as the case may be, one-half of the longest term of imprisonment provided for that offence</strong>, or with such fine, or with both.</p>

<h3>2. The Three Categories of Attempts in Penal Law</h3>
<ol>
  <li><strong>Offences where commission and attempt are punished in the same section with the same penalty:</strong> Waging war (S. 147 BNS / S. 121 IPC), Sedition against sovereignty (S. 152 BNS).</li>
  <li><strong>Offences where attempt is punished in a separate specific section:</strong> Attempt to murder (S. 109 BNS / S. 307 IPC), Attempt to commit culpable homicide (S. 110 BNS / S. 308 IPC), Attempt to commit robbery (S. 309 BNS / S. 393 IPC).</li>
  <li><strong>Residual attempts governed by Section 62 BNS / Section 511 IPC:</strong> All other offences where no specific attempt section exists (e.g. attempt to commit theft, kidnapping, cheating). Punished with half of maximum term.</li>
</ol>

<h3>3. Attempt to Commit Impossible Crimes</h3>
<p>An attempt to commit an offence does not cease to be an attempt merely because the completion was factually impossible:</p>
<ul>
  <li>A puts his hand into Z's pocket with intent to steal Z's purse. The pocket is empty. A is guilty of attempt to commit theft under Section 62 read with Section 303 BNS (Section 511 Illustration (b) IPC).</li>
  <li>A shoots at a bolster in Z's bed believing it to be Z, but Z is absent. Guilty of attempt to murder.</li>
</ul>
""",
        "quickRevisionPoints": [
            "Former Section 511 IPC (the last section of IPC) is relocated to Section 62 BNS.",
            "Section 62 is a residual attempt provision; applies where no express attempt section exists.",
            "Punishment under S. 62 BNS = Up to ONE-HALF of the longest term of imprisonment provided for offence.",
            "Factually impossible attempt is PUNISHABLE (e.g. empty pocket theft per S. 511 Illustration (b)).",
            "Attempt requires: Intention + Overt act towards commission + Failure by outside intervention."
        ],
        "provisions": [
            {
                "article": "Section 62 BNS",
                "title": "Punishment for attempting to commit offences",
                "text": "Whoever attempts to commit an offence punishable... and in such attempt does any act towards the commission of the offence... shall be punished with imprisonment for a term which may extend to one-half of the imprisonment for life or one-half of the longest term...",
                "breakdown": "Relocates historical Section 511 IPC into Chapter IV of BNS."
            }
        ],
        "definitions": [{"term": "Criminal Attempt", "definition": "A direct step taken towards the commission of an offence following preparation, which would have resulted in completion but for extraneous interruption."}],
        "ingredients": ["Intention to commit a specific offence.", "Performance of an overt act towards its execution.", "Failure to accomplish the intended harm."],
        "exceptions": ["Attempt to commit an offence punishable with fine only is NOT punishable under Section 62 BNS."],
        "examples": [
            {"scenario": "A breaks open a box with intent to steal jewels, but finds no jewels inside.", "application": "Guilty of attempt to commit theft under Section 62 read with Section 303 BNS / Section 511 IPC (Illustration (a))."}
        ],
        "landmarkCases": [
            {
                "case": "Abhayanand Mishra v. State of Bihar",
                "citation": "AIR 1961 SC 1698",
                "year": "1961",
                "bench": "Raghubar Dayal J",
                "ratio": "A candidate applied for MA examination submitting forged certificates and admission fee. The university issued an admit card, but discovered the fraud before exams commenced. Held: Accused had progressed beyond preparation and was guilty of attempt to cheat under Section 511 IPC.",
                "impact": "Classic authority defining the commencement of attempt upon dispatching fraudulent applications."
            }
        ],
        "comparisonTables": [
            {
                "title": "Attempt Classifications in Penal Law",
                "headers": ["Category", "Example Offence", "Statutory Provision"],
                "rows": [
                    ["Same Section Same Penalty", "Waging War", "Section 147 BNS / Section 121 IPC"],
                    ["Specific Attempt Section", "Attempt to Murder", "Section 109 BNS / Section 307 IPC"],
                    ["Specific Attempt Section", "Attempted Culpable Homicide", "Section 110 BNS / Section 308 IPC"],
                    ["General Residual Provision", "Attempt to commit theft / kidnap", "Section 62 BNS / Section 511 IPC (Half penalty)"]
                ]
            }
        ],
        "diagramId": "diag-crim-mens-rea-liability",
        "diagramExplanation": "Diagram charts the transition from non-punishable preparation to punishable attempt.",
        "prelimTraps": [
            {
                "trap": "Believing Section 62 BNS / S. 511 IPC applies to an attempt to murder.",
                "reality": "Attempt to murder has a specific section: Section 109 BNS / Section 307 IPC. Section 62 is strictly RESIDUAL.",
                "rule": "Specific attempt sections override Section 62 BNS."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crim-05-07",
                "front": "Where was Section 511 IPC relocated in the Bharatiya Nyaya Sanhita, 2023?",
                "back": "Section 62 of BNS 2023.",
                "category": "Attempt"
            },
            {
                "id": "fc-crim-05-08",
                "front": "What is the maximum term of imprisonment under Section 62 BNS for an attempt?",
                "back": "One-half (1/2) of the longest term of imprisonment provided for the offence.",
                "category": "Attempt"
            }
        ],
        "sourceReferences": [{"title": "Section 62, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    }
}

content = f"""/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Criminal Law Module — Authored Concepts (Part 2: Ch 5 to 8)
 * Topics: top-crim-05-01 to top-crim-08-03
 */

(function (global) {{
  'use strict';

  const DATA = {json.dumps(CONCEPTS, indent=2)};

  global.CRIMINAL_CONCEPTS_PART2 = DATA;
  if (typeof module !== 'undefined' && module.exports) {{
    module.exports = DATA;
  }}
}})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
"""

with open("assets/learning/data/criminal/criminal-concepts-part2.js", "w", encoding="utf-8") as f:
    f.write(content)

print("Written criminal-concepts-part2.js batch")
