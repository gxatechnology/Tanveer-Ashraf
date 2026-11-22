"""
Builder for Criminal Law Concepts Part 3 (Chapters 9 to 12: 10 Topics)
- Chapter 9: top-crim-09-01, top-crim-09-02, top-crim-09-03
- Chapter 10: top-crim-10-01, top-crim-10-02, top-crim-10-03
- Chapter 11: top-crim-11-01, top-crim-11-02
- Chapter 12: top-crim-12-01, top-crim-12-02
Output: assets/learning/data/criminal/criminal-concepts-part3.js
"""

import json

CONCEPTS = {
    # -------------------------------------------------------------------------
    # CHAPTER 9: OFFENCES AGAINST PROPERTY
    # -------------------------------------------------------------------------
    "top-crim-09-01": {
        "topicId": "top-crim-09-01",
        "chapterId": "ch-crim-09",
        "subjectId": "law-criminal",
        "title": "Theft, Extortion, Robbery & Dacoity: The Gradation Spectrum",
        "subtitle": "BNS Sections 303–313 vs IPC Sections 378–402 & The Escalation of Violence",
        "learningObjective": "Master the escalating continuum of property offences from Theft (Section 303 BNS) to Extortion (Section 308), Robbery (Section 309), and Dacoity (Section 310), and the community service proviso.",
        "introduction": "Offences against property operate on a graduated spectrum of violence and coercion. Theft involves dishonest taking of movable property without consent. Extortion adds the element of fear inducing delivery. Robbery is an aggravated form where either theft or extortion is accompanied by imminent violence. Dacoity is a robbery conjointly committed or attempted by five or more persons.",
        "detailedExplanation": """
<h3>1. Theft: Section 303 BNS / Section 378 IPC</h3>
<p>Whoever, intending to take dishonestly any movable property out of the possession of any person without that person's consent, moves that property in order to such taking, is said to commit theft.</p>
<p><strong>Five Essential Ingredients:</strong></p>
<ol>
  <li>Dishonest intention to take property (animus furandi);</li>
  <li>Property must be <strong>movable property</strong>;</li>
  <li>Must be taken <strong>out of the possession</strong> of another person (ownership not required; lawful possession suffices);</li>
  <li>Taken <strong>without that person's consent</strong>;</li>
  <li>There must be some <strong>moving</strong> of the property in order to such taking.</li>
</ol>
<p><strong>NEW BNS REFORM (Section 303(2) Proviso):</strong> Where the value of the stolen property is less than <strong>five thousand rupees (Rs 5,000)</strong>, and the offender is a first-time offender and returns or restores the property, the Court may award a sentence of <strong>Community Service</strong>.</p>

<h3>2. Extortion: Section 308 BNS / Section 383 IPC</h3>
<p>Whoever intentionally puts any person in fear of any injury to that person, or to any other, and thereby dishonestly induces the person so put in fear to deliver to any person any property, or valuable security, or anything signed or sealed which may be converted into a valuable security, commits extortion.</p>
<p>Extortion differs from theft because: (a) It applies to immovable property as well as movable; (b) Property is <em>delivered</em> by the victim under fear, not taken away secretly.</p>

<h3>3. Robbery: Section 309 BNS / Section 390 IPC</h3>
<p>In all robbery there is either theft or extortion:</p>
<ul>
  <li><strong>When Theft is Robbery:</strong> If, in order to the committing of the theft, or in committing the theft, or in carrying away or attempting to carry away property obtained by the theft, the offender, for that end, voluntarily causes or attempts to cause to any person death or hurt or wrongful restraint, or fear of instant death/hurt/wrongful restraint.</li>
  <li><strong>When Extortion is Robbery:</strong> If the offender, at the time of committing the extortion, is in the presence of the person put in fear, and commits the extortion by putting that person in fear of instant death, of instant hurt, or of instant wrongful restraint.</li>
</ul>

<h3>4. Dacoity: Section 310 BNS / Section 391 IPC</h3>
<p>When <strong>five or more persons</strong> conjointly commit or attempt to commit a robbery, or where the whole number of persons conjointly committing or attempting to commit a robbery, and persons present and aiding such commission or attempt, amount to five or more, every person so committing, attempting or aiding, is said to commit 'dacoity'.</p>
<p>Punishment for Dacoity (Section 310(2) BNS / Section 395 IPC): Imprisonment for life, or rigorous imprisonment up to 10 years, and fine.</p>
""",
        "quickRevisionPoints": [
            "Theft = Section 303 BNS (S. 378 IPC): 5 elements (Dishonest + Movable + Out of possession + No consent + Moving).",
            "Community service available for theft < Rs 5,000 for first-time offender returning property (S. 303(2) Proviso).",
            "Extortion = Section 308 BNS (S. 383 IPC): Inducing delivery under fear of injury (movable or immovable).",
            "Robbery = Section 309 BNS (S. 390 IPC): Theft or extortion + instant violence/fear.",
            "Dacoity = Section 310 BNS (S. 391 IPC): Conjoint robbery by FIVE OR MORE PERSONS."
        ],
        "provisions": [
            {
                "article": "Section 303 BNS",
                "title": "Theft",
                "text": "Whoever, intending to take dishonestly any movable property out of the possession of any person without that person's consent, moves that property... (2) imprisoned up to three years or fine... Proviso: Community service if value under Rs 5,000.",
                "breakdown": "Corresponds to Section 378 & 379 IPC with new community service reform."
            },
            {
                "article": "Section 310 BNS",
                "title": "Dacoity",
                "text": "When five or more persons conjointly commit or attempt to commit a robbery... punishment: imprisonment for life or rigorous imprisonment up to ten years...",
                "breakdown": "Corresponds to Section 391 & 395 IPC. Retains the 5-person threshold."
            }
        ],
        "definitions": [
            {"term": "Theft", "definition": "Dishonest moving of movable property out of another's possession without consent."},
            {"term": "Dacoity", "definition": "Robbery conjointly committed or attempted by five or more persons."}
        ],
        "ingredients": ["Theft: Movable property + possession + moving + dishonest intention.", "Dacoity: Exactly five or more persons + robbery elements."],
        "exceptions": ["Taking under a bona fide claim of right (even if erroneous) is not theft because dishonest intention is absent."],
        "examples": [
            {"scenario": "Four armed persons hold up a bank cashier and loot cash.", "application": "Robbery under Section 309 BNS / Section 390 IPC; cannot be charged with Dacoity because the number of persons is four, not five."}
        ],
        "landmarkCases": [
            {
                "case": "K.N. Mehra v. State of Rajasthan",
                "citation": "AIR 1957 SC 369",
                "year": "1957",
                "bench": "Jagannadhadas J",
                "ratio": "Temporary deprivation of property with dishonest intention constitutes theft. Taking an Indian Air Force aircraft without authorization on an unpermitted flight to Pakistan, even if intended to be returned, constituted theft under Section 378 IPC.",
                "impact": "Established that intention to permanently deprive is NOT an essential ingredient of theft under Indian law."
            },
            {
                "case": "State of Maharashtra v. Joseph Mingel Koli",
                "citation": "1997 Cri LJ 362",
                "year": "1997",
                "bench": "Bombay High Court",
                "ratio": "If the number of accused participating in robbery falls below five due to acquittal of unidentified co-accused and there is no finding that five or more participated, conviction must be altered from dacoity to robbery.",
                "impact": "Reiterates the indispensable numerical threshold of five persons for dacoity."
            }
        ],
        "comparisonTables": [
            {
                "title": "Theft vs Extortion vs Robbery vs Dacoity",
                "headers": ["Feature", "Theft (S. 303 BNS)", "Extortion (S. 308 BNS)", "Robbery (S. 309 BNS)", "Dacoity (S. 310 BNS)"],
                "rows": [
                    ["Property Type", "Movable property only", "Movable or Immovable", "Movable (if theft) / Either (if extortion)", "Either"],
                    ["Consent", "Taken WITHOUT consent", "Obtained by FEAR (vitiated consent)", "Overpowered by instant violence", "Overpowered by group violence"],
                    ["Delivery", "Taken away by offender", "Delivered by victim", "Taken or delivered on spot", "Taken or delivered conjointly"],
                    ["Persons", "One or more", "One or more", "One to four", "FIVE OR MORE strictly"]
                ]
            }
        ],
        "diagramId": "diag-crim-property-offences-gradation",
        "diagramExplanation": "Diagram charts the escalation ladder from theft to extortion, robbery, and dacoity.",
        "prelimTraps": [
            {
                "trap": "Believing dacoity can be committed by four persons.",
                "reality": "Section 310 BNS / Section 391 IPC explicitly mandates FIVE OR MORE PERSONS. Four persons commit robbery, not dacoity.",
                "rule": "Dacoity strictly requires 5 or more persons."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crim-09-01",
                "front": "What is the minimum number of persons required to constitute the offence of Dacoity?",
                "back": "Five (5) or more persons acting conjointly (Section 310 BNS / Section 391 IPC).",
                "category": "Property Offences"
            },
            {
                "id": "fc-crim-09-02",
                "front": "Does theft under Indian law require an intention to permanently deprive the owner?",
                "back": "No, temporary dishonest taking out of possession constitutes theft (K.N. Mehra v. State of Rajasthan).",
                "category": "Theft"
            }
        ],
        "sourceReferences": [{"title": "Sections 303, 308, 309, 310, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-crim-09-02": {
        "topicId": "top-crim-09-02",
        "chapterId": "ch-crim-09",
        "subjectId": "law-criminal",
        "title": "Criminal Misappropriation & Criminal Breach of Trust",
        "subtitle": "BNS Sections 314–317 vs IPC Sections 403–409 & The Entrustment Nexus",
        "learningObjective": "Master the distinction between Dishonest Misappropriation of Property (Section 314 BNS / S. 403 IPC) and Criminal Breach of Trust (Section 316 BNS / S. 405 IPC), focusing on initial innocent possession vs fiduciary entrustment.",
        "introduction": "While theft involves taking property unlawfully from another's possession, Misappropriation and Breach of Trust involve property that came into the offender's possession lawfully or innocently in the first instance. Section 314 BNS penalizes converting property innocently acquired, while Section 316 BNS penalizes breaching a fiduciary relationship of entrustment.",
        "detailedExplanation": """
<h3>1. Criminal Misappropriation: Section 314 BNS / Section 403 IPC</h3>
<p>Whoever dishonestly misappropriates or converts to his own use any movable property, shall be punished with imprisonment of either description for a term which may extend to <strong>two years</strong>, or with fine, or with both.</p>
<ul>
  <li>Initial possession is <strong>innocent or lawful</strong> (e.g. finder of lost property).</li>
  <li>The dishonest mental state (mens rea) arises <em>subsequently</em>, when the finder decides to retain or convert the property instead of returning it after knowing or having means of finding the owner.</li>
  <li><strong>Explanation 2 (Finder of Goods):</strong> A person finding property not in possession of any other person, and taking such property for the purpose of protecting it for, or of restoring it to, the owner, does not take it dishonestly. But if he appropriates it when he knows who the owner is or without using reasonable means to discover the owner, he is guilty.</li>
</ul>

<h3>2. Criminal Breach of Trust: Section 316 BNS / Section 405 IPC</h3>
<p>Whoever, being in any manner <strong>entrusted with property</strong>, or with any dominion over property, dishonestly misappropriates or converts to his own use that property, or dishonestly uses or disposes of that property in violation of any direction of law or legal contract, commits criminal breach of trust.</p>
<p><strong>Essential Ingredients:</strong></p>
<ol>
  <li>Entrustment of property or dominion over property (creates a fiduciary relationship);</li>
  <li>Dishonest misappropriation, conversion, or disposal in violation of legal direction or contract.</li>
</ol>
<p><strong>Aggravated Forms:</strong> Carrier, wharfinger (S. 316(3) BNS / S. 407 IPC); Clerk or servant (S. 316(4) BNS / S. 408 IPC); Public servant, banker, merchant, factor, broker, attorney, or agent (S. 316(5) BNS / S. 409 IPC — up to Life Imprisonment or 10 years).</p>
""",
        "quickRevisionPoints": [
            "Criminal Misappropriation = Section 314 BNS (S. 403 IPC); initial possession is innocent; dishonest conversion happens later.",
            "Finder of lost goods who converts without reasonable search for owner commits misappropriation (S. 314 Expl. 2).",
            "Criminal Breach of Trust = Section 316 BNS (S. 405 IPC); requires FIDUCIARY ENTRUSTMENT of property or dominion.",
            "Public servant or banker committing breach of trust: Section 316(5) BNS (S. 409 IPC); carries up to LIFE IMPRISONMENT.",
            "Jaswantrai Manilal Akhaney (1956): Entrustment creates a trust/fiduciary duty over property."
        ],
        "provisions": [
            {
                "article": "Section 314 BNS",
                "title": "Dishonest misappropriation of property",
                "text": "Whoever dishonestly misappropriates or converts to his own use any movable property, shall be punished with imprisonment... which may extend to two years, or with fine, or with both.",
                "breakdown": "Corresponds to Section 403 IPC."
            },
            {
                "article": "Section 316 BNS",
                "title": "Criminal breach of trust",
                "text": "Whoever, being in any manner entrusted with property, or with any dominion over property, dishonestly misappropriates or converts... (2) up to five years... (5) public servant/banker: life or ten years.",
                "breakdown": "Corresponds to Sections 405 to 409 IPC."
            }
        ],
        "definitions": [
            {"term": "Entrustment", "definition": "Handing over property to a person holding it in fiduciary confidence for a designated purpose or on behalf of the owner."},
            {"term": "Dominion over Property", "definition": "Legal or physical control over property without ownership."}
        ],
        "ingredients": ["Initial lawful custody or possession.", "Subsequent dishonest conversion or violation of trust."],
        "exceptions": ["Retaining property under a genuine disputed debt or set-off without dishonest intention."],
        "examples": [
            {"scenario": "A banker receives Rs 10 lakhs from a customer for purchasing government securities, but uses the funds to pay his personal debts.", "application": "Guilty of Criminal Breach of Trust by Banker under Section 316(5) BNS / Section 409 IPC; carries imprisonment up to life."}
        ],
        "landmarkCases": [
            {
                "case": "Jaswantrai Manilal Akhaney v. State of Bombay",
                "citation": "AIR 1956 SC 575",
                "year": "1956",
                "bench": "Sinha J",
                "ratio": "Entrustment contemplates the creation of a fiduciary relationship whereby the owner transfers legal possession or dominion over property, retaining beneficial interest in himself. Pledging securities entrusted for safe custody constitutes criminal breach of trust.",
                "impact": "Classic authority on the meaning of 'entrustment' under Section 405 IPC / Section 316 BNS."
            }
        ],
        "comparisonTables": [
            {
                "title": "Theft vs Misappropriation vs Criminal Breach of Trust",
                "headers": ["Feature", "Theft (S. 303 BNS)", "Misappropriation (S. 314 BNS)", "Breach of Trust (S. 316 BNS)"],
                "rows": [
                    ["Initial Possession", "Unlawful (taken out of possession)", "Lawful / Innocent (e.g. found)", "Lawful by ENTRUSTMENT (fiduciary)"],
                    ["Property Scope", "Movable property only", "Movable property only", "Movable or Immovable property"],
                    ["Contractual Relationship", "No relationship exists", "No prior relationship", "Fiduciary / contractual trust exists"],
                    ["Max Basic Punishment", "3 Years (S. 303 BNS)", "2 Years (S. 314 BNS)", "5 Years (S. 316 BNS); Life for Banker"]
                ]
            }
        ],
        "diagramId": "diag-crim-property-offences-gradation",
        "diagramExplanation": "Diagram contrasts possession-based theft with custody-based misappropriation and trust-based breach.",
        "prelimTraps": [
            {
                "trap": "Confusing theft with criminal misappropriation when goods are found on a public road.",
                "reality": "If property is not in anyone's possession when found, taking it is NOT theft. Retaining it dishonestly without search for owner is Criminal Misappropriation.",
                "rule": "Finder of lost goods = Section 314 BNS (Misappropriation), never Theft."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crim-09-03",
                "front": "What is the defining element separating Criminal Breach of Trust from Criminal Misappropriation?",
                "back": "FIDUCIARY ENTRUSTMENT: Breach of trust requires property to be entrusted; misappropriation starts with accidental/innocent possession.",
                "category": "Property Offences"
            },
            {
                "id": "fc-crim-09-04",
                "front": "What is the maximum punishment for Criminal Breach of Trust by a Public Servant or Banker under Section 316(5) BNS / Section 409 IPC?",
                "back": "Imprisonment for life, or imprisonment up to ten years, and fine.",
                "category": "Sentencing Scales"
            }
        ],
        "sourceReferences": [{"title": "Sections 314, 316, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-crim-09-03": {
        "topicId": "top-crim-09-03",
        "chapterId": "ch-crim-09",
        "subjectId": "law-criminal",
        "title": "Cheating, Mischief, Criminal Trespass & House-breaking",
        "subtitle": "BNS Sections 318–334 vs IPC Sections 415–462 & The Fraudulent Inducement Continuum",
        "learningObjective": "Master Cheating under Section 318 BNS (consolidating IPC S. 415 & 420), Mischief under Section 324 BNS, Criminal Trespass (Section 329 BNS), and the six ways of House-breaking.",
        "introduction": "Property can be compromised through mental deception (Cheating), physical destruction (Mischief), or spatial invasion (Trespass). The Bharatiya Nyaya Sanhita consolidates historical Sections 415 and 420 IPC into Section 318 BNS, while maintaining the classic definitions of mischief and the six specific statutory modes of house-breaking.",
        "detailedExplanation": """
<h3>1. Cheating: Section 318 BNS / Sections 415 & 420 IPC</h3>
<p>Whoever, by deceiving any person, fraudulently or dishonestly induces the person so deceived to deliver any property to any person, or to consent that any person shall retain any property, or intentionally induces the person so deceived to do or omit to do anything which he would not do or omit if he were not so deceived, and which act or omission causes or is likely to cause damage or harm to that person in body, mind, reputation or property, is said to 'cheat'.</p>
<ul>
  <li><strong>Consolidation in BNS:</strong> Section 318(1) defines cheating (formerly S. 415 IPC); Section 318(2) punishes simple cheating with up to <strong>three years</strong>; Section 318(4) punishes cheating and dishonestly inducing delivery of property (formerly the famous Section 420 IPC) with imprisonment up to <strong>seven years</strong> and fine.</li>
  <li><strong>Crucial Distinction: Breach of Contract vs Cheating:</strong> Mere failure to keep a promise does not constitute cheating. The prosecution must prove that the accused had a <strong>fraudulent or dishonest intention from the very beginning</strong> (at the inception of the transaction) (<em>Hridaya Ranjan Prasad Verma v. State of Bihar</em>, 2000).</li>
</ul>

<h3>2. Mischief: Section 324 BNS / Section 425 IPC</h3>
<p>Whoever with intent to cause, or knowing that he is likely to cause, wrongful loss or damage to the public or to any person, causes the destruction of any property, or any such change in any property or in the situation thereof as destroys or diminishes its value or utility, or affects it injuriously, commits 'mischief'.</p>

<h3>3. Criminal Trespass & House-Breaking: Sections 329–331 BNS / Sections 441–446 IPC</h3>
<ul>
  <li><strong>Criminal Trespass (Section 329(1) BNS / S. 441 IPC):</strong> Entering into or upon property in possession of another with intent to commit an offence, or to intimidate, insult, or annoy.</li>
  <li><strong>House-Trespass (Section 329(2) BNS / S. 442 IPC):</strong> Criminal trespass by entering or remaining in any building, tent, or vessel used as human dwelling or place of worship/property custody.</li>
  <li><strong>House-Breaking (Section 329(3) BNS / S. 445 IPC):</strong> House-trespass effected through any of the <strong>six statutory ways</strong>:
    <ol>
      <li>Through an opening made or enlarged by the trespasser;</li>
      <li>Through any passage not intended for human entrance (e.g. scaling a wall/roof);</li>
      <li>Through any passage opened by picking locks or keys;</li>
      <li>By opening any lock;</li>
      <li>By using criminal force or threat of force;</li>
      <li>By entering/leaving through any passage fastened against entrance.</li>
    </ol>
  </li>
  <li><strong>House-Breaking by Night:</strong> House-breaking committed after sunset and before sunrise.</li>
</ul>
""",
        "quickRevisionPoints": [
            "Former Section 420 IPC is now Section 318(4) BNS (Cheating & inducing delivery of property, up to 7 yrs).",
            "Cheating requires dishonest intention at the VERY INCEPTION of transaction (Hridaya Ranjan Prasad Verma).",
            "Mischief is Section 324 BNS (S. 425 IPC): Destroying or diminishing value/utility of property.",
            "Criminal Trespass requires intent to commit an offence, intimidate, insult, or annoy (S. 329(1) BNS).",
            "House-breaking specifies exactly SIX STATUTORY WAYS (S. 329(3) BNS / S. 445 IPC)."
        ],
        "provisions": [
            {
                "article": "Section 318 BNS",
                "title": "Cheating",
                "text": "Whoever, by deceiving any person, fraudulently or dishonestly induces... (2) up to three years... (4) cheating and dishonestly inducing delivery of property: up to seven years and fine.",
                "breakdown": "Consolidates Section 415 (definition) and Section 420 (aggravated delivery) IPC."
            },
            {
                "article": "Section 329 BNS",
                "title": "Criminal Trespass, House-Trespass & House-Breaking",
                "text": "Consolidates definitions of criminal trespass, house-trespass, lurking house-trespass, and the six ways of house-breaking.",
                "breakdown": "Corresponds to Sections 441 to 446 IPC."
            }
        ],
        "definitions": [
            {"term": "Cheating", "definition": "Deceiving a person and thereby fraudulently inducing delivery of property or performance of an act causing harm in body, mind, reputation, or property."},
            {"term": "Mischief", "definition": "Causing destruction or diminution in value or utility of property with intent to cause wrongful loss."}
        ],
        "ingredients": ["Cheating: Deception + fraudulent inducement + delivery of property or injurious act.", "Trespass: Unlawful entry + intent to commit offence or intimidate/annoy."],
        "exceptions": ["Breach of contract arising from subsequent commercial failure without initial dishonest intention."],
        "examples": [
            {"scenario": "A enters B's house at midnight by climbing over the roof and dropping through a skylight.", "application": "Guilty of House-Breaking by Night under Section 329(3) BNS (Clause 2: passage not intended for human entrance); punishable under Section 331 BNS."}
        ],
        "landmarkCases": [
            {
                "case": "Hridaya Ranjan Prasad Verma v. State of Bihar",
                "citation": "(2000) 4 SCC 168",
                "year": "2000",
                "bench": "D.P. Mohapatra J",
                "ratio": "The distinction between mere breach of contract and cheating depends upon the intention of the accused at the time of the inducement. If dishonest intention existed from the very beginning, it is cheating; if intention was bona fide at inception, failure to perform later is mere breach of contract.",
                "impact": "Authoritative constitutional ruling distinguishing civil breach from criminal cheating under Section 420 IPC / Section 318 BNS."
            }
        ],
        "comparisonTables": [
            {
                "title": "Breach of Contract versus Cheating",
                "headers": ["Point of Distinction", "Breach of Contract (Civil)", "Cheating (S. 318 BNS / S. 415 IPC)"],
                "rows": [
                    ["Inception Intention", "Honest and bona fide intention to perform at start", "Dishonest and fraudulent intention from the VERY BEGINNING"],
                    ["Nature of Remedy", "Civil suit for damages or specific performance", "Criminal prosecution and imprisonment"],
                    ["Mens Rea", "No criminal mens rea required", "Dishonest/fraudulent inducement essential"],
                    ["Key Authority", "Section 73 Indian Contract Act, 1872", "Hridaya Ranjan Prasad Verma v. State of Bihar"]
                ]
            }
        ],
        "diagramId": "diag-crim-property-offences-gradation",
        "diagramExplanation": "Diagram charts cheating, mischief, and the six ways of house-breaking.",
        "prelimTraps": [
            {
                "trap": "Believing entering through an open door left unlocked by the owner constitutes house-breaking.",
                "reality": "Walking through an ordinary unlocked open door is simple house-trespass, NOT house-breaking, because none of the six statutory modes occurred.",
                "rule": "House-breaking strictly requires one of the six specific modes under Section 329(3) BNS."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crim-09-05",
                "front": "Where is the famous offence of Section 420 IPC (Cheating and dishonestly inducing delivery) codified in BNS 2023?",
                "back": "Section 318, sub-section (4) of BNS 2023 (imprisonment up to 7 years and fine).",
                "category": "Cheating"
            },
            {
                "id": "fc-crim-09-06",
                "front": "How many statutory ways of committing House-Breaking are specified in Section 329(3) BNS / Section 445 IPC?",
                "back": "Six (6) statutory ways.",
                "category": "House-Breaking"
            }
        ],
        "sourceReferences": [{"title": "Sections 318, 324, 329, 331, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    # -------------------------------------------------------------------------
    # CHAPTER 10: OFFENCES AGAINST THE STATE & PUBLIC TRANQUILITY
    # -------------------------------------------------------------------------
    "top-crim-10-01": {
    "topicId": "top-crim-10-01",
    "chapterId": "ch-crim-10",
    "subjectId": "law-criminal",
    "title": "Acts Endangering Sovereignty & Integrity of India (S. 152 BNS)",
    "subtitle": "BNS Section 152 vs Historical Sedition (IPC Section 124A) & Kedarnath Doctrine",
    "learningObjective": "Master the abolition of colonial 'Sedition' (Section 124A IPC) and the enactment of Section 152 BNS penalizing acts endangering the sovereignty, unity, and integrity of India.",
    "introduction": "One of the most consequential structural reforms in the Bharatiya Nyaya Sanhita, 2023 is the deletion of colonial 'Sedition' (Rajdroh under Section 124A IPC) and its replacement with a targeted provision protecting national integrity: Section 152 BNS (Act endangering sovereignty, unity and integrity of India). Section 152 shifts focus from criticizing the government to protecting the constitutional existence of the nation.",
    "detailedExplanation": """
<h3>1. The Omission of Sedition (Section 124A IPC)</h3>
<p>Section 124A IPC penalized exciting 'disaffection towards the Government established by law'. In <em>S.G. Vombatkere v. Union of India</em> (2022), the Supreme Court directed that Section 124A IPC be kept in abeyance pending re-examination. BNS formally omitted the colonial offence of sedition entirely.</p>

<h3>2. Section 152 BNS: Act Endangering Sovereignty, Unity and Integrity of India</h3>
<p>Whoever, purposely or knowingly, by words, either spoken or written, or by signs, or by visible representation, or by electronic communication or by use of financial mean, or otherwise:</p>
<ol>
  <li>Excites or attempts to excite <strong>secession or armed rebellion or subversive activities</strong>; OR</li>
  <li>Encourages feelings of <strong>separatist activities</strong>; OR</li>
  <li>Endangers <strong>sovereignty or unity and integrity of India</strong>,</li>
</ol>
<p>shall be punished with <strong>imprisonment for life</strong> or with imprisonment which may extend to <strong>seven years</strong>, and shall also be liable to fine.</p>

<h3>3. Explanation to Section 152 BNS: Protection of Free Speech</h3>
<p>Comments expressing disapprobation of the measures, or administrative or other action of the Government with a view to obtain their alteration by lawful means without exciting or attempting to excite the activities aforesaid, do not constitute an offence under this section.</p>
<p>This codifies the classic constitutional safeguard in <em>Kedar Nath Singh v. State of Bihar</em> (AIR 1962 SC 955): Robust criticism of governmental policies is a constitutional right under Article 19(1)(a); only calls to armed rebellion, secession, or subversive violence are penalized.</p>
""",
        "quickRevisionPoints": [
            "Colonial 'Sedition' (Section 124A IPC) is OMITTED from Indian penal law.",
            "Section 152 BNS replaces it: Penalizes acts exciting secession, armed rebellion, or endangering sovereignty.",
            "Punishment under S. 152 BNS: Life Imprisonment or up to 7 YEARS and fine.",
            "Electronic communication and financial means are explicitly included in S. 152 BNS.",
            "Criticism of government policies for lawful alteration is protected by the Explanation (Kedar Nath Singh)."
        ],
        "provisions": [
            {
                "article": "Section 152 BNS",
                "title": "Act endangering sovereignty, unity and integrity of India",
                "text": "Whoever purposely or knowingly excites secession, armed rebellion, subversive activities, or encourages separatist activities... punished with imprisonment for life or up to seven years and fine.",
                "breakdown": "Replaces Section 124A IPC. Focuses on armed rebellion and territorial sovereignty."
            }
        ],
        "definitions": [
            {"term": "Secession", "definition": "The formal withdrawal or attempt to separate a state or territory from the Union of India."},
            {"term": "Subversive Activities", "definition": "Actions intended to overthrow, disrupt, or undermine the constitutional order through non-democratic or violent means."}
        ],
        "ingredients": ["Purposely or knowingly exciting secession, armed rebellion, or subversive acts.", "Endangering sovereignty, unity, and integrity of India."],
        "exceptions": ["Lawful political criticism, protests, and democratic dissent seeking change through constitutional means."],
        "examples": [
            {"scenario": "A speaker publishes an online manifesto calling on citizens to take up arms, declare an independent republic, and attack military installations.", "application": "Liable under Section 152 BNS (Act endangering sovereignty); faces life imprisonment."}
        ],
        "landmarkCases": [
            {
                "case": "Kedar Nath Singh v. State of Bihar",
                "citation": "AIR 1962 SC 955",
                "year": "1962",
                "bench": "5-Judge Constitution Bench (Sinha CJ)",
                "ratio": "Criticism of public measures or comments on government actions, however strongly worded, are within reasonable speech limits unless accompanied by incitement to violence or public disorder.",
                "impact": "Constitutional benchmark codified in the Explanation to Section 152 BNS."
            },
            {
                "case": "S.G. Vombatkere v. Union of India",
                "citation": "(2022) 7 SCC 633",
                "year": "2022",
                "bench": "N.V. Ramana CJ",
                "ratio": "The Supreme Court directed that all pending trials, appeals, and proceedings with respect to the charge framed under Section 124A IPC be kept in abeyance.",
                "impact": "Directly prompted Parliament to repeal Section 124A IPC and enact Section 152 BNS."
            }
        ],
        "comparisonTables": [
            {
                "title": "Section 124A IPC (Sedition) versus Section 152 BNS",
                "headers": ["Feature", "Section 124A IPC (Colonial Sedition)", "Section 152 BNS (Sovereignty Protection)"],
                "rows": [
                    ["Core Target", "Disaffection towards 'Government established by law'", "Secession, armed rebellion, subversive activities"],
                    ["Protected Interest", "Colonial regime authority", "Sovereignty, unity, and territorial integrity of India"],
                    ["Punishment", "Life or up to 3 years and fine", "Life or up to 7 years and fine"],
                    ["Modern Mediums", "Silent on modern cyber tools", "Explicitly includes electronic communication & financial means"],
                    ["Status", "Omitted / Repealed", "Active statutory law in force"]
                ]
            }
        ],
        "diagramId": "diag-crim-culpable-homicide-murder",
        "diagramExplanation": "Diagram charts offences against the state, showing Section 152 BNS protecting sovereignty.",
        "prelimTraps": [
            {
                "trap": "Believing Section 152 BNS is called 'Sedition'.",
                "reality": "The word 'Sedition' (Rajdroh) does NOT appear anywhere in the Bharatiya Nyaya Sanhita. Section 152 is titled 'Act endangering sovereignty, unity and integrity of India'.",
                "rule": "BNS has abolished the title and colonial concept of 'Sedition'."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crim-10-01",
                "front": "What section of BNS replaced the historical offence of Sedition (Section 124A IPC)?",
                "back": "Section 152 BNS (Act endangering sovereignty, unity and integrity of India).",
                "category": "Offences Against State"
            },
            {
                "id": "fc-crim-10-02",
                "front": "What is the maximum term of imprisonment under Section 152 BNS if life imprisonment is not awarded?",
                "back": "Imprisonment extending up to seven (7) years and fine (increased from 3 years in IPC 124A).",
                "category": "Offences Against State"
            }
        ],
        "sourceReferences": [{"title": "Section 152, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-crim-10-02": {
        "topicId": "top-crim-10-02",
        "chapterId": "ch-crim-10",
        "subjectId": "law-criminal",
        "title": "Terrorism & Organised Crime in BNS (S. 111, 112, 113)",
        "subtitle": "The Integration of Special Penal Offenses into General Criminal Law",
        "learningObjective": "Master the groundbreaking incorporation of Organised Crime (Section 111 BNS), Petty Organised Crime (Section 112 BNS), and Terrorist Acts (Section 113 BNS) directly into the general penal code.",
        "introduction": "Historically, terrorism and organised crime were governed exclusively by special enactments (UAPA 1967, MCOCA 1999). The Bharatiya Nyaya Sanhita, 2023 achieves a historic codification by introducing dedicated substantive provisions for Organised Crime (Section 111), Petty Organised Crime (Section 112), and Terrorist Acts (Section 113) directly into the general penal statute.",
        "detailedExplanation": """
<h3>1. Organised Crime: Section 111 BNS (NEW)</h3>
<p>Any continuing unlawful activity including kidnapping, robbery, extortion, land grabbing, contract killing, economic offences, cyber-crimes having severe consequences, trafficking in persons or drugs, or running gang syndicates, committed by any person or group using violence, intimidation, or coercion to obtain direct or indirect material or financial benefit.</p>
<ul>
  <li><strong>Continuing Unlawful Activity:</strong> An activity prohibited by law which is a cognizable offence punishable with imprisonment of 3+ years, where more than one charge-sheet has been filed before a competent court within the preceding <strong>ten years</strong>, and that court has taken cognizance.</li>
  <li><strong>Punishment:</strong> If death of any person results: <strong>Death or Life Imprisonment</strong>, and fine not less than Rs 10 lakhs (S. 111(2)(a)). If no death: Imprisonment not less than <strong>five years</strong> extending to life, and fine not less than Rs 5 lakhs (S. 111(2)(b)).</li>
</ul>

<h3>2. Petty Organised Crime: Section 112 BNS (NEW)</h3>
<p>Whoever, being a member of a group or gang, commits theft, snatching, cheating, unauthorized selling of tickets, betting or gambling, or selling public exam question papers, commits petty organised crime. Punished with imprisonment for not less than <strong>one year</strong> extending to <strong>seven years</strong>, and fine.</p>

<h3>3. Terrorist Act: Section 113 BNS (NEW)</h3>
<p>Whoever does any act with intent to threaten or likely to threaten the unity, integrity, sovereignty, or security of India, or to strike terror in the people, by using bombs, dynamite, firearms, lethal weapons, poisonous gases, or cyber attacks: Punished with <strong>Death or Life Imprisonment</strong> if death results; otherwise imprisonment for not less than <strong>five years</strong> extending to life imprisonment.</p>
""",
        "quickRevisionPoints": [
            "BNS integrates Organised Crime (S. 111) and Terrorism (S. 113) into the general penal code.",
            "Organised Crime requires continuing unlawful activity: 2+ charge-sheets in preceding 10 years taken cognizance.",
            "Organised Crime causing death carries Death or Life Imprisonment and min fine Rs 10 lakhs.",
            "Petty organised crime (S. 112 BNS): Snatching, exam paper leaks, ticket touting by gang (1 to 7 yrs).",
            "Terrorist act (S. 113 BNS): Death or Life Imprisonment if death results."
        ],
        "provisions": [
            {
                "article": "Section 111 BNS",
                "title": "Organised Crime",
                "text": "Any continuing unlawful activity including kidnapping, robbery, extortion, land grabbing... punishment: death or life imprisonment if death results...",
                "breakdown": "Brand-new provision adapting MCOCA principles into national penal law."
            },
            {
                "article": "Section 113 BNS",
                "title": "Terrorist Act",
                "text": "Whoever does any act with intent to threaten the unity, integrity, sovereignty or security of India... punishment: death or imprisonment for life...",
                "breakdown": "Brand-new provision incorporating general anti-terror definitions into BNS."
            }
        ],
        "definitions": [
            {"term": "Continuing Unlawful Activity", "definition": "An activity punishable with 3+ years where 2+ charge-sheets have been filed in the preceding 10 years and cognizance taken."},
            {"term": "Petty Organised Crime", "definition": "Organized gang activities including street snatching, exam paper leaks, ticket black-marketing, and betting."}
        ],
        "ingredients": ["Membership of organized crime syndicate or gang.", "Economic or material benefit motive.", "Requisite number of prior charge-sheets for S. 111."],
        "exceptions": ["Isolated individual crimes without gang/syndicate nexus do not fall under Section 111 or 112."],
        "examples": [
            {"scenario": "A criminal syndicate leader running an extortion gang with three prior charge-sheets in the last 6 years orders the contract killing of a builder.", "application": "Liable under Section 111(2)(a) BNS (Organised Crime causing death); faces death penalty or life imprisonment and fine of at least Rs 10 lakhs."}
        ],
        "landmarkCases": [
            {
                "case": "State of Maharashtra v. Bharat Shanti Lal Shah",
                "citation": "(2008) 13 SCC 5",
                "year": "2008",
                "bench": "Altamas Kabir J",
                "ratio": "The definition of continuing unlawful activity requiring two or more charge-sheets within the preceding 10 years is constitutionally valid and does not violate Article 14 or 21.",
                "impact": "Direct constitutional precedent validating the framework adopted in Section 111 BNS."
            }
        ],
        "comparisonTables": [
            {
                "title": "BNS 2023 Organized Crime Framework",
                "headers": ["Offence", "BNS Section", "Applicable Conduct", "Minimum Punishment"],
                "rows": [
                    ["Organised Crime (Death)", "Section 111(2)(a)", "Syndicate crimes resulting in death", "Death or Life Imprisonment (Min Rs 10L fine)"],
                    ["Organised Crime (General)", "Section 111(2)(b)", "Syndicate extortion, trafficking, land-grab", "5 Years to Life (Min Rs 5L fine)"],
                    ["Petty Organised Crime", "Section 112", "Snatching, paper leaks, touting by gang", "1 Year to 7 Years and fine"],
                    ["Terrorist Act", "Section 113", "Attacks threatening security/integrity", "5 Years to Life / Death if death results"]
                ]
            }
        ],
        "diagramId": "diag-crim-culpable-homicide-murder",
        "diagramExplanation": "Diagram charts the new statutory offences of organized crime and terrorism in BNS.",
        "prelimTraps": [
            {
                "trap": "Believing a person can be charged under Section 111 BNS for a first-time individual extortion.",
                "reality": "Section 111 requires a 'continuing unlawful activity' which mandates more than one charge-sheet filed within the preceding 10 years.",
                "rule": "Section 111 BNS strictly requires 2+ charge-sheets in preceding 10 years."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crim-10-03",
                "front": "What is the prior charge-sheet threshold to establish 'continuing unlawful activity' under Section 111 BNS?",
                "back": "More than one charge-sheet (at least 2) filed before a competent court within the preceding ten years.",
                "category": "Organised Crime"
            },
            {
                "id": "fc-crim-10-04",
                "front": "Which section of BNS 2023 penalizes Petty Organised Crime such as snatching and exam paper leaks?",
                "back": "Section 112 BNS 2023 (imprisonment from 1 to 7 years and fine).",
                "category": "BNS Innovations"
            }
        ],
        "sourceReferences": [{"title": "Sections 111, 112, 113, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-crim-10-03": {
        "topicId": "top-crim-10-03",
        "chapterId": "ch-crim-10",
        "subjectId": "law-criminal",
        "title": "Unlawful Assembly, Rioting & Affray",
        "subtitle": "BNS Sections 189, 191, 194 vs IPC Sections 141, 146, 159 & Public Tranquility",
        "learningObjective": "Master the five heads of Unlawful Assembly (Section 189 BNS / S. 141 IPC), Rioting (Section 191 BNS / S. 146 IPC), and Affray (Section 194 BNS / S. 159 IPC).",
        "introduction": "Public peace and order are the bedrock of civil society. The Bharatiya Nyaya Sanhita punishes collective threats to peace through a three-tiered classification: Unlawful Assembly (the gathering with common illegal object), Rioting (the application of force by such assembly), and Affray (public fighting disturbing public peace).",
        "detailedExplanation": """
<h3>1. Unlawful Assembly: Section 189 BNS / Section 141 IPC</h3>
<p>An assembly of <strong>five or more persons</strong> is designated an 'unlawful assembly', if the common object of the persons composing that assembly is:</p>
<ol>
  <li><strong>First:</strong> To overawe by criminal force, or show of criminal force, the Central or State Government, or Parliament, or Legislature, or any public servant in exercise of lawful power;</li>
  <li><strong>Secondly:</strong> To resist the execution of any law, or of any legal process;</li>
  <li><strong>Thirdly:</strong> To commit any mischief or criminal trespass, or other offence;</li>
  <li><strong>Fourthly:</strong> By means of criminal force, or show of criminal force, to any person, to take or obtain possession of any property, or to deprive any person of the enjoyment of a right of way, or of the use of water or other incorporeal right, or to enforce any right or supposed right;</li>
  <li><strong>Fifthly:</strong> By means of criminal force, or show of criminal force, to compel any person to do what he is not legally bound to do, or to omit to do what he is legally entitled to do.</li>
</ol>
<p>An assembly which was not unlawful when it assembled, may subsequently become an unlawful assembly (Explanation to S. 189).</p>

<h3>2. Rioting: Section 191 BNS / Section 146 IPC</h3>
<p>Whenever <strong>force or violence</strong> is used by an unlawful assembly, or by any member thereof, in prosecution of the common object of such assembly, every member of such assembly is guilty of the offence of rioting.</p>
<ul>
  <li>Rioting is simply an unlawful assembly in active violent operation.</li>
  <li>Punishment: Imprisonment up to <strong>two years</strong>, or fine, or both (S. 191(2) BNS / S. 147 IPC).</li>
  <li>Rioting armed with deadly weapon: Imprisonment up to <strong>five years</strong>, or fine, or both (S. 191(3) BNS / S. 148 IPC).</li>
</ul>

<h3>3. Affray: Section 194 BNS / Section 159 IPC</h3>
<p>When <strong>two or more persons</strong>, by fighting in a <strong>public place</strong>, disturb the public peace, they are said to 'commit an affray'.</p>
<ul>
  <li>Requires at least <strong>two persons</strong>;</li>
  <li>Must be in a <strong>public place</strong> (a private room is NOT an affray);</li>
  <li>Must cause actual disturbance of the public peace.</li>
  <li>Punishment: Imprisonment up to <strong>one month</strong>, or fine up to Rs 1,000, or both (S. 194 BNS / S. 160 IPC).</li>
</ul>
""",
        "quickRevisionPoints": [
            "Unlawful Assembly = Section 189 BNS (S. 141 IPC): Exactly 5+ persons with common object under 5 heads.",
            "An assembly lawful at inception may subsequently become unlawful (S. 189 Explanation).",
            "Rioting = Section 191 BNS (S. 146 IPC): Unlawful assembly + Force or violence used.",
            "Affray = Section 194 BNS (S. 159 IPC): Min 2 persons fighting in PUBLIC PLACE disturbing public peace.",
            "Rioting requires 5+ persons; Affray requires min 2 persons."
        ],
        "provisions": [
            {
                "article": "Section 189 BNS",
                "title": "Unlawful Assembly",
                "text": "An assembly of five or more persons is designated an unlawful assembly if the common object is... five heads...",
                "breakdown": "Corresponds to Section 141 IPC with the five classical heads preserved."
            },
            {
                "article": "Section 194 BNS",
                "title": "Affray",
                "text": "When two or more persons, by fighting in a public place, disturb the public peace, they are said to commit an affray.",
                "breakdown": "Corresponds to Section 159 IPC."
            }
        ],
        "definitions": [
            {"term": "Unlawful Assembly", "definition": "A group of five or more persons united by a common illegal object specified in Section 189 BNS."},
            {"term": "Affray", "definition": "A bilateral fight between two or more persons in a public venue resulting in disturbance of the public peace."}
        ],
        "ingredients": ["Unlawful assembly: 5+ persons + common object under one of five statutory heads.", "Affray: 2+ persons + public place + actual fight + disturbance of public peace."],
        "exceptions": ["An assembly defending property against an unlawful raid is not an unlawful assembly because enforcing a lawful defence is not an illegal object."],
        "examples": [
            {"scenario": "Two passengers get into a fist fight on a platform at Hazratganj railway station, causing panic among commuters.", "application": "Guilty of Affray under Section 194 BNS / Section 159 IPC; committed in a public place disturbing public peace."}
        ],
        "landmarkCases": [
            {
                "case": "Moti Das v. State of Bihar",
                "citation": "AIR 1954 SC 657",
                "year": "1954",
                "bench": "Das J",
                "ratio": "An assembly which was lawful when assembled may become an unlawful assembly subsequently if it develops a common unlawful object to use criminal force.",
                "impact": "Classic authority on the transformation of a lawful assembly into an unlawful assembly."
            }
        ],
        "comparisonTables": [
            {
                "title": "Rioting (S. 191 BNS) vs Affray (S. 194 BNS)",
                "headers": ["Point of Distinction", "Rioting (S. 191 BNS / S. 146 IPC)", "Affray (S. 194 BNS / S. 159 IPC)"],
                "rows": [
                    ["Minimum Persons", "Five (5) persons", "Two (2) persons"],
                    ["Locus / Place", "Any place (public or private)", "Must strictly be in a PUBLIC PLACE"],
                    ["Common Object", "Common object essential (S. 189)", "Common object is NOT required (mere fight)"],
                    ["Max Punishment", "Up to 2 years (5 years if armed)", "Up to 1 month or fine Rs 1,000"]
                ]
            }
        ],
        "diagramId": "diag-crim-culpable-homicide-murder",
        "diagramExplanation": "Diagram details the continuum of public order offences from unlawful assembly to rioting and affray.",
        "prelimTraps": [
            {
                "trap": "Believing two people fighting inside a private bedroom can be convicted of affray.",
                "reality": "Affray strictly requires fighting in a PUBLIC PLACE. A fight inside a private house is assault, not affray.",
                "rule": "Affray strictly requires a PUBLIC PLACE."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crim-10-05",
                "front": "What are the minimum number of persons required for Unlawful Assembly and Affray respectively?",
                "back": "Unlawful Assembly = Minimum 5 persons; Affray = Minimum 2 persons.",
                "category": "Public Tranquility"
            },
            {
                "id": "fc-crim-10-06",
                "front": "What converts an Unlawful Assembly into the offence of Rioting?",
                "back": "The use of FORCE or VIOLENCE by the assembly or any member in prosecution of the common object (Section 191 BNS).",
                "category": "Rioting"
            }
        ],
        "sourceReferences": [{"title": "Sections 189, 191, 194, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    # -------------------------------------------------------------------------
    # CHAPTER 11: OFFENCES AGAINST PUBLIC JUSTICE
    # -------------------------------------------------------------------------
    "top-crim-11-01": {
    "topicId": "top-crim-11-01",
    "chapterId": "ch-crim-11",
    "subjectId": "law-criminal",
    "title": "Giving and Fabricating False Evidence: Perjury & Sanctions",
    "subtitle": "BNS Sections 227–233 vs IPC Sections 191–195 & The Integrity of Judicial Proceedings",
    "learningObjective": "Master the offences of Giving False Evidence (Section 227 BNS / S. 191 IPC) and Fabricating False Evidence (Section 228 BNS / S. 192 IPC), perjury in judicial proceedings, and procedural safeguards under Section 215 BNSS / S. 195 CrPC.",
    "introduction": "The administration of justice depends upon the truthfulness of testimony and records. The Bharatiya Nyaya Sanhita protects the stream of justice from pollution through Sections 227 to 233. Giving false evidence (oral perjury) and fabricating false evidence (documentary/circumstantial deception) are severely penalized, especially when committed in judicial proceedings.",
    "detailedExplanation": """
<h3>1. Giving False Evidence: Section 227 BNS / Section 191 IPC</h3>
<p>Whoever, being legally bound by an oath or by an express provision of law to state the truth, or being bound by law to make a declaration upon any subject, makes any statement which is <strong>false, and which he either knows or believes to be false or does not believe to be true</strong>, is said to give false evidence.</p>
<ul>
  <li>Statement may be verbal or in writing (affidavit).</li>
  <li>Can be an assertion of fact, or an assertion of belief or opinion.</li>
</ul>

<h3>2. Fabricating False Evidence: Section 228 BNS / Section 192 IPC</h3>
<p>Whoever causes any circumstance to exist or makes any false entry in any book or record, or electronic record, or makes any document containing a false statement, intending that such circumstance or false entry may appear in evidence in a judicial proceeding, and may cause any person who in such proceeding is to form an opinion upon the evidence, to entertain an <strong>erroneous opinion</strong> touching any point material to the result, is said 'to fabricate false evidence'.</p>

<h3>3. Punishment for Perjury: Section 229 BNS / Section 193 IPC</h3>
<ul>
  <li>In any stage of a <strong>judicial proceeding</strong>: Imprisonment of either description for a term which may extend to <strong>seven years</strong>, and fine.</li>
  <li>In any other case (e.g. before an administrative inquiry): Imprisonment up to <strong>three years</strong>, and fine.</li>
</ul>

<h3>4. Procedural Bar: Section 215 BNSS / Section 195 CrPC</h3>
<p>No court shall take cognizance of any offence of perjury or fabricating false evidence committed in or in relation to any proceeding in any Court, EXCEPT on the <strong>complaint in writing of that Court</strong> or by such officer of the Court as that Court may authorize. Private complaints of perjury are barred.</p>
""",
        "quickRevisionPoints": [
            "Giving false evidence = Section 227 BNS (S. 191 IPC); requires oath/legal duty + false statement.",
            "Fabricating false evidence = Section 228 BNS (S. 192 IPC); creating circumstances/false entries to deceive court.",
            "Punishment: In judicial proceedings = up to 7 YEARS and fine; other cases = up to 3 years (S. 229 BNS).",
            "Procedural Bar: Section 215 BNSS (S. 195 CrPC) requires written complaint of the Court.",
            "Bishir Ahmad (1970): Intention to cause judge to form erroneous opinion on material point is essential."
        ],
        "provisions": [
            {
                "article": "Section 227 BNS",
                "title": "Giving false evidence",
                "text": "Whoever, being legally bound by an oath or express provision of law to state the truth... makes statement false and known/believed to be false...",
                "breakdown": "Corresponds to Section 191 IPC."
            },
            {
                "article": "Section 229 BNS",
                "title": "Punishment for false evidence",
                "text": "Whoever intentionally gives false evidence in judicial proceeding... imprisoned up to seven years and fine; in other case up to three years.",
                "breakdown": "Corresponds to Section 193 IPC."
            }
        ],
        "definitions": [
            {"term": "Perjury", "definition": "Making a false statement under legal oath or duty knowing or believing it to be false in a judicial proceeding."},
            {"term": "Fabricating False Evidence", "definition": "Creating false records or circumstances with intent to cause a judge to form an erroneous opinion on a material point."}
        ],
        "ingredients": ["Legally bound by oath or express law to state the truth.", "Statement made false and known/believed to be false."],
        "exceptions": ["An honest statement of belief, even if mistaken, does not constitute perjury."],
        "examples": [
            {"scenario": "A puts jewels into a box belonging to Z, with the intention that they may be found in that box, and that this circumstance may cause Z to be convicted of theft.", "application": "A has fabricated false evidence under Section 228 BNS / Section 192 IPC (Illustration (a))."}
        ],
        "landmarkCases": [
            {
                "case": "Iqbal Singh Marwah v. Meenakshi Marwah",
                "citation": "(2005) 4 SCC 370",
                "year": "2005",
                "bench": "5-Judge Constitution Bench (Lahoti CJ)",
                "ratio": "The bar under Section 195(1)(b)(ii) CrPC / Section 215 BNSS applies only to offences committed in respect of a document after it has been produced or given in evidence in court, and not to documents forged prior to production.",
                "impact": "Crucial landmark on the jurisdictional scope of perjury complaints by courts."
            }
        ],
        "comparisonTables": [
            {
                "title": "Giving False Evidence vs Fabricating False Evidence",
                "headers": ["Point of Distinction", "Giving False Evidence (S. 227 BNS / S. 191 IPC)", "Fabricating False Evidence (S. 228 BNS / S. 192 IPC)"],
                "rows": [
                    ["Medium", "Verbal testimony or written sworn statements (affidavits)", "Physical circumstances, false book entries, electronic records"],
                    ["Legal Duty", "Must be legally bound by oath or express provision of law", "No prior oath or legal duty required; act of creation suffices"],
                    ["Nexus", "Directly made by the witness in proceedings", "Created with intent that it may appear in evidence"],
                    ["Punishment", "Both punished identically under Section 229 BNS", "Up to 7 years in judicial proceedings"]
                ]
            }
        ],
        "diagramId": "diag-crim-culpable-homicide-murder",
        "diagramExplanation": "Diagram charts offences against public justice and perjury sanctions.",
        "prelimTraps": [
            {
                "trap": "Believing a private citizen can file a police FIR for perjury committed by a witness in a civil suit.",
                "reality": "Under Section 215 BNSS / S. 195 CrPC, only the presiding Court itself can file a written complaint for perjury.",
                "rule": "Perjury in court = Only the Court can complain (S. 215 BNSS)."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crim-11-01",
                "front": "What is the maximum punishment for giving false evidence in a judicial proceeding under Section 229 BNS / Section 193 IPC?",
                "back": "Imprisonment of either description for a term extending up to seven (7) years, and fine.",
                "category": "Perjury"
            },
            {
                "id": "fc-crim-11-02",
                "front": "Who alone is competent to file a complaint for perjury committed in relation to a court proceeding?",
                "back": "The Court itself or its authorized officer in writing (Section 215 BNSS / Section 195 CrPC).",
                "category": "Procedural Bars"
            }
        ],
        "sourceReferences": [{"title": "Sections 227, 228, 229, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-crim-11-02": {
        "topicId": "top-crim-11-02",
        "chapterId": "ch-crim-11",
        "subjectId": "law-criminal",
        "title": "Contempt of Lawful Authority of Public Servants",
        "subtitle": "BNS Sections 206–226 vs IPC Sections 172–190 & Enforcement of Lawful Mandates",
        "learningObjective": "Master the offences protecting lawful administrative governance: absconding to avoid service of summons (S. 206 BNS), non-attendance (S. 209), refusing oath (S. 213), and obstructing public servants (S. 221 BNS).",
        "introduction": "To function effectively, state administrative machinery must have coercive power to enforce attendance, demand information, and execute warrants. Chapter XI of the Bharatiya Nyaya Sanhita (Sections 206 to 226) penalizes defiance of lawful public orders, non-appearance on proclamation, refusal to answer questions, and obstruction of public servants.",
        "detailedExplanation": """
<h3>1. Absconding to Avoid Service of Summons: Section 206 BNS / Section 172 IPC</h3>
<p>Whoever absconds in order to avoid being served with a summons, notice or order proceeding from any public servant legally competent to issue it: Simple imprisonment up to <strong>one month</strong> or fine; if summons is from a Court of Justice: up to <strong>six months</strong> or fine.</p>

<h3>2. Failure to Attend in Obedience to Order: Section 209 BNS / Section 174 IPC</h3>
<p>Whoever, being legally bound to attend in person or by agent at a certain place and time in obedience to a summons, notice, order or proclamation from a public servant, intentionally omits to attend: Simple imprisonment up to 1 month or fine; if from Court: up to 6 months.</p>
<p><strong>Section 209(2) BNS (Proclamation Absconders):</strong> Failure to appear pursuant to a proclamation issued under Section 84 BNSS (proclaimed offender): Imprisonment up to <strong>three years</strong>, or fine, or both; or <strong>Community Service</strong>.</p>

<h3>3. Obstructing Public Servant in Discharge of Duty: Section 221 BNS / Section 186 IPC</h3>
<p>Whoever voluntarily obstructs any public servant in the discharge of his public functions, shall be punished with imprisonment of either description for a term which may extend to <strong>three months</strong>, or with fine up to Rs 2,500, or with both.</p>

<h3>4. Disobedience to Order Promulgated by Public Servant: Section 223 BNS / Section 188 IPC</h3>
<p>Whoever, knowing that, by an order promulgated by a public servant lawfully empowered to promulgate such order, he is directed to abstain from a certain act: Simple imprisonment up to <strong>six months</strong>, or fine up to Rs 2,500, or both.</p>
""",
        "quickRevisionPoints": [
            "Section 206 BNS (S. 172 IPC): Absconding to avoid summons.",
            "Section 209(2) BNS: Failure to appear on proclamation carries up to 3 years OR Community Service.",
            "Section 221 BNS (S. 186 IPC): Obstructing public servant in discharge of functions (up to 3 months).",
            "Section 223 BNS (S. 188 IPC): Disobedience to lawful administrative orders (e.g. curfew/S. 144 CrPC).",
            "Section 215 BNSS (S. 195 CrPC) requires written complaint of the concerned public servant."
        ],
        "provisions": [
            {
                "article": "Section 209 BNS",
                "title": "Non-attendance in obedience to an order from public servant",
                "text": "Whoever intentionally omits to attend... (2) where proclamation issued under S. 84 BNSS: imprisoned up to three years or fine or community service.",
                "breakdown": "Introduces Community Service option for proclamation failure."
            },
            {
                "article": "Section 223 BNS",
                "title": "Disobedience to order duly promulgated by public servant",
                "text": "Whoever knowing that an order is promulgated directs to abstain from certain act... imprisoned up to six months...",
                "breakdown": "Corresponds to Section 188 IPC."
            }
        ],
        "definitions": [
            {"term": "Absconding", "definition": "Hiding or concealing oneself to prevent service of lawful court processes."}
        ],
        "ingredients": ["Public servant lawfully empowered to issue order.", "Knowledge of the order by the accused.", "Intentional disobedience or obstruction."],
        "exceptions": ["Where the public servant's order is ultra vires or without jurisdiction."],
        "examples": [
            {"scenario": "A citizen violates a prohibitory night curfew order promulgated by the District Magistrate under Section 163 BNSS (S. 144 CrPC).", "application": "Guilty of disobedience under Section 223 BNS / Section 188 IPC; punishable with up to six months imprisonment."}
        ],
        "landmarkCases": [
            {
                "case": "State of UP v. Mata Bhikh",
                "citation": "(1994) 4 SCC 95",
                "year": "1994",
                "bench": "Kuldip Singh J",
                "ratio": "The provisions of Section 195 CrPC / Section 215 BNSS are mandatory and a court cannot take cognizance of an offence under Section 188 IPC / Section 223 BNS without a written complaint of the public servant concerned.",
                "impact": "Strictly enforces administrative complaint prerequisites for prosecution."
            }
        ],
        "comparisonTables": [
            {
                "title": "Public Servant Defiance Offences",
                "headers": ["Offence", "BNS Section", "IPC Equivalent", "Maximum Punishment"],
                "rows": [
                    ["Absconding to Avoid Summons", "Section 206", "Section 172", "1 Month (6 Months if Court summons)"],
                    ["Non-Attendance on Summons", "Section 209(1)", "Section 174", "1 Month (6 Months if Court order)"],
                    ["Non-Appearance on Proclamation", "Section 209(2)", "Section 174A", "3 Years or Fine or Community Service"],
                    ["Obstructing Public Servant", "Section 221", "Section 186", "3 Months or Fine up to Rs 2,500"],
                    ["Disobedience to Lawful Order", "Section 223", "Section 188", "6 Months or Fine up to Rs 2,500"]
                ]
            }
        ],
        "diagramId": "diag-crim-culpable-homicide-murder",
        "diagramExplanation": "Diagram charts offences defying lawful public administrative authority.",
        "prelimTraps": [
            {
                "trap": "Believing police can register an FIR on their own for violation of Section 223 BNS (S. 188 IPC).",
                "reality": "Prosecution requires a written complaint by the public servant whose order was disobeyed under Section 215 BNSS.",
                "rule": "Section 223 BNS requires public servant's written complaint."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crim-11-03",
                "front": "What punishment can be awarded under Section 209(2) BNS for failing to appear pursuant to an absconder proclamation?",
                "back": "Imprisonment up to three years, or fine, or both; or Community Service.",
                "category": "Contempt of Authority"
            },
            {
                "id": "fc-crim-11-04",
                "front": "Where is the historical offence of Section 188 IPC (Disobedience to order of public servant) codified in BNS?",
                "back": "Section 223 of BNS 2023.",
                "category": "BNS Renumbering"
            }
        ],
        "sourceReferences": [{"title": "Sections 206, 209, 221, 223, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    # -------------------------------------------------------------------------
    # CHAPTER 12: OFFENCES AFFECTING REPUTATION, DOCUMENTS & INTIMIDATION
    # -------------------------------------------------------------------------
    "top-crim-12-01": {
    "topicId": "top-crim-12-01",
    "chapterId": "ch-crim-12",
    "subjectId": "law-criminal",
    "title": "Forgery, False Documents & Electronic Records (BNS S. 336)",
    "subtitle": "BNS Sections 336–345 vs IPC Sections 463–477A & Digital Document Integrity",
    "learningObjective": "Master the definition of Forgery under Section 336 BNS (Section 463 IPC), making a false document/electronic record under Section 337 BNS (Section 464 IPC), and using forged documents under Section 340 BNS.",
    "introduction": "Documents and electronic records form the bedrock of civil and commercial transactions. Section 336 of the Bharatiya Nyaya Sanhita, 2023 penalizes Forgery—the creation of false documents or electronic records with intent to cause damage, commit fraud, or support claims. Section 337 details the three specific statutory methods by which a person 'makes a false document'.",
    "detailedExplanation": """
<h3>1. Forgery: Section 336 BNS / Section 463 IPC</h3>
<p>Whoever makes any false document or false electronic record or part of a document or electronic record, with intent to:</p>
<ol>
  <li>Cause damage or injury to the public or to any person; OR</li>
  <li>Support any claim or title; OR</li>
  <li>Cause any person to part with property; OR</li>
  <li>Enter into any express or implied contract; OR</li>
  <li>With intent to commit fraud or that fraud may be committed,</li>
</ol>
<p>commits forgery. Basic punishment under Section 338 BNS / Section 465 IPC: Imprisonment up to <strong>two years</strong>, or fine, or both.</p>

<h3>2. Making a False Document: Section 337 BNS / Section 464 IPC</h3>
<p>A person is said to make a false document or electronic record in three specific ways:</p>
<ul>
  <li><strong>First:</strong> Dishonestly or fraudulently makes, signs, seals, executes, or transmits any document or electronic record, with intention of causing it to be believed that it was made by or by authority of a person by whom he knows it was not made (Impersonation / False Attestation).</li>
  <li><strong>Secondly:</strong> Without lawful authority, dishonestly or fraudulently, by cancellation or otherwise, <strong>alters a document or electronic record</strong> in any material part after it has been executed.</li>
  <li><strong>Thirdly:</strong> Dishonestly or fraudulently causes any person to sign, seal, execute, or alter a document, knowing that such person by reason of unsoundness of mind or intoxication cannot, or by reason of deception does not, know the contents.</li>
</ul>

<h3>3. Using as Genuine a Forged Document: Section 340 BNS / Section 471 IPC</h3>
<p>Whoever fraudulently or dishonestly uses as genuine any document or electronic record which he knows or has reason to believe to be a forged document, shall be punished in the same manner as if he had forged such document.</p>
""",
        "quickRevisionPoints": [
            "Forgery = Section 336 BNS (S. 463 IPC); Making false document = Section 337 BNS (S. 464 IPC).",
            "Punishment for Forgery = Section 338 BNS (S. 465 IPC): up to 2 years or fine or both.",
            "Using forged document as genuine = Section 340 BNS (S. 471 IPC): punished same as forger.",
            "Three modes of making false document: (1) False signing/execution; (2) Material alteration; (3) Inducing signature by deception/insanity.",
            "Electronic records are explicitly integrated throughout Sections 336 to 345 BNS."
        ],
        "provisions": [
            {
                "article": "Section 336 BNS",
                "title": "Forgery",
                "text": "Whoever makes any false document or false electronic record with intent to cause damage, support title, commit fraud...",
                "breakdown": "Corresponds to Section 463 IPC."
            },
            {
                "article": "Section 337 BNS",
                "title": "Making a false document or electronic record",
                "text": "A person is said to make a false document: (a) dishonestly/fraudulently signing; (b) altering materially; (c) procuring signature of incapacitated person...",
                "breakdown": "Corresponds to Section 464 IPC."
            }
        ],
        "definitions": [
            {"term": "Forgery", "definition": "Making a false document or electronic record with fraudulent or injurious intent."},
            {"term": "Material Alteration", "definition": "Changing a vital term (date, sum, party name, property boundary) of an executed document without authority."}
        ],
        "ingredients": ["Making a false document as defined in Section 337.", "Intent to cause damage, commit fraud, or support a claim."],
        "exceptions": ["Making an altered document under honest bona fide claim of authority without dishonest intent."],
        "examples": [
            {"scenario": "A has a letter of credit for Rs 10,000 written by B. A adds a zero to make it Rs 1,00,000 intending to defraud the bank.", "application": "A has materially altered the document under Section 337 (Clause Secondly) and is guilty of forgery of valuable security under Section 339 BNS / Section 467 IPC."}
        ],
        "landmarkCases": [
            {
                "case": "Sheila Sebastian v. R. Jawaharaj",
                "citation": "(2018) 7 SCC 581",
                "year": "2018",
                "bench": "N.V. Ramana J",
                "ratio": "A charge of forgery cannot be sustained against a person unless it is proved that he himself made or was part of making the false document under Section 464 IPC. Creating a document by an authorized person, even if containing false statements, is not making a false document.",
                "impact": "Crucial distinction between making a false document and making a document containing false recitals."
            }
        ],
        "comparisonTables": [
            {
                "title": "Making False Document: The Three Statutory Modes",
                "headers": ["Mode", "Section 337 Clause", "Operational Mechanism"],
                "rows": [
                    ["False Execution", "Clause (a)", "Signing or transmitting pretending to be another person"],
                    ["Material Alteration", "Clause (b)", "Altering sums, dates, or terms after execution without authority"],
                    ["Deceptive Procurement", "Clause (c)", "Inducing an illiterate, drunk, or insane person to sign unaware of contents"]
                ]
            }
        ],
        "diagramId": "diag-crim-culpable-homicide-murder",
        "diagramExplanation": "Diagram charts forgery and making false documents under Chapter XVII BNS.",
        "prelimTraps": [
            {
                "trap": "Believing writing a letter containing false statements constitutes 'forgery'.",
                "reality": "Writing a letter containing lies signed in your own real name is NOT forgery. Forgery requires pretending the document was made by someone else or altering it (Sheila Sebastian).",
                "rule": "A document containing false recitals is NOT a false document if signed by the real author."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crim-12-01",
                "front": "Where is the definition of Forgery codified in BNS 2023?",
                "back": "Section 336 of BNS 2023 (formerly Section 463 IPC).",
                "category": "Forgery"
            },
            {
                "id": "fc-crim-12-02",
                "front": "How many statutory methods exist for 'making a false document' under Section 337 BNS / Section 464 IPC?",
                "back": "Three (3) methods: False execution, Material alteration, and Deceptive procurement.",
                "category": "False Documents"
            }
        ],
        "sourceReferences": [{"title": "Sections 336, 337, 338, 340, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-crim-12-02": {
        "topicId": "top-crim-12-02",
        "chapterId": "ch-crim-12",
        "subjectId": "law-criminal",
        "title": "Criminal Intimidation, Insult, Annoyance & Defamation",
        "subtitle": "BNS Sections 351–356 vs IPC Sections 499–510 & The 10 Defamation Exceptions",
        "learningObjective": "Master Criminal Intimidation under Section 351 BNS (Section 503 IPC), and Defamation under Section 356 BNS (Sections 499–500 IPC), analyzing the 10 statutory exceptions and the new Community Service sanction.",
        "introduction": "Reputation and psychological security are protected under the final chapter of penal law. Section 351 BNS penalizes Criminal Intimidation (threatening injury to body, property, or reputation). Section 356 BNS consolidates the substantive definition of Defamation, its ten classical exceptions, and introduces an innovative punishment option: Community Service.",
        "detailedExplanation": """
<h3>1. Criminal Intimidation: Section 351 BNS / Section 503 IPC</h3>
<p>Whoever threatens another with any injury to his person, reputation or property, or to the person or property of any one in whom that person is interested, with intent to cause alarm to that person, or to cause that person to do any act which he is not legally bound to do, or to omit to do any act which that person is legally entitled to do, as the means of avoiding the execution of such threat, commits criminal intimidation.</p>
<ul>
  <li>Punishment (Section 351(2) BNS / Section 506 IPC): Imprisonment up to <strong>two years</strong>, or fine, or both.</li>
  <li>If threat be to cause death or grievous hurt, or destruction of property by fire: Imprisonment up to <strong>seven years</strong>, or fine, or both (Section 351(3) BNS).</li>
</ul>

<h3>2. Defamation: Section 356 BNS / Section 499 IPC</h3>
<p>Whoever, by words either spoken or intended to be read, or by signs or by visible representations, makes or publishes any imputation concerning any person intending to harm, or knowing or having reason to believe that such imputation will harm, the reputation of such person, is said to defame that person.</p>
<p><strong>The Ten Statutory Exceptions to Defamation:</strong></p>
<ol>
  <li><strong>First:</strong> Imputation of truth which public good requires to be made or published;</li>
  <li><strong>Secondly:</strong> Public conduct of public servants;</li>
  <li><strong>Thirdly:</strong> Conduct of any person touching any public question;</li>
  <li><strong>Fourthly:</strong> Publication of reports of proceedings of courts;</li>
  <li><strong>Fifthly:</strong> Merits of case decided in court or conduct of witnesses and others;</li>
  <li><strong>Sixthly:</strong> Merits of public performance (books, films, art);</li>
  <li><strong>Seventhly:</strong> Censure passed in good faith by person having lawful authority over another;</li>
  <li><strong>Eighthly:</strong> Accusation preferred in good faith to authorized person;</li>
  <li><strong>Ninthly:</strong> Imputation made in good faith by person for protection of his or other's interests;</li>
  <li><strong>Tenthly:</strong> Caution intended for good of person to whom conveyed or for public good.</li>
</ol>

<h3>3. Punishment for Defamation: Section 356(2) BNS / Section 500 IPC</h3>
<p>Whoever defames another shall be punished with simple imprisonment for a term which may extend to <strong>two years</strong>, or with fine, or with both, <strong>OR WITH COMMUNITY SERVICE</strong>.</p>
<p>The addition of Community Service in Section 356(2) provides judges with an effective restorative alternative to prison for civil reputation disputes.</p>
""",
        "quickRevisionPoints": [
            "Criminal Intimidation is Section 351 BNS (formerly Section 503 IPC); threat of injury to induce action/omission.",
            "Defamation is Section 356 BNS (formerly Sections 499 & 500 IPC).",
            "Ten statutory exceptions to defamation preserved in Section 356(1) BNS.",
            "First Exception requires TWO things: TRUTH + PUBLIC GOOD (truth alone is not enough).",
            "Punishment for Defamation: Simple imprisonment up to 2 years, or fine, OR COMMUNITY SERVICE (S. 356(2) BNS)."
        ],
        "provisions": [
            {
                "article": "Section 351 BNS",
                "title": "Criminal Intimidation",
                "text": "Whoever threatens another with injury to person, reputation or property with intent to cause alarm... (2) up to two years... (3) threat of death/grievous hurt: up to seven years.",
                "breakdown": "Corresponds to Sections 503 and 506 IPC."
            },
            {
                "article": "Section 356 BNS",
                "title": "Defamation",
                "text": "Whoever makes or publishes any imputation... intending to harm reputation... ten exceptions... (2) simple imprisonment up to two years, or fine, or community service.",
                "breakdown": "Consolidates Section 499 and 500 IPC with new Community Service sanction."
            }
        ],
        "definitions": [
            {"term": "Defamation", "definition": "Publishing an imputation intending or knowing it will harm the reputation of a living or deceased person."},
            {"term": "Criminal Intimidation", "definition": "Communicating a threat of injury to body, property, or reputation with intent to cause alarm or coerce action."}
        ],
        "ingredients": ["Making or publishing an imputation.", "Imputation refers to complainant.", "Intention or knowledge of harming reputation."],
        "exceptions": ["The ten statutory exceptions under Section 356(1) BNS."],
        "examples": [
            {"scenario": "A publishes in a newspaper that B is a convicted thief. It is true, and published for the public good to warn citizens.", "application": "Protected under the First Exception to Section 356 BNS / Section 499 IPC (Truth published for public good)."}
        ],
        "landmarkCases": [
            {
                "case": "Subramanian Swamy v. Union of India",
                "citation": "(2016) 7 SCC 221",
                "year": "2016",
                "bench": "Dipak Misra & P.C. Pant JJ",
                "ratio": "Sections 499 and 500 IPC penalizing criminal defamation do not violate Article 19(1)(a) of the Constitution. Reputation is an integral part of the right to life under Article 21, and criminal defamation constitutes a reasonable restriction under Article 19(2).",
                "impact": "Upheld the constitutional validity of criminal defamation in Indian law."
            }
        ],
        "comparisonTables": [
            {
                "title": "Criminal Intimidation vs Extortion",
                "headers": ["Point of Distinction", "Criminal Intimidation (S. 351 BNS / S. 503 IPC)", "Extortion (S. 308 BNS / S. 383 IPC)"],
                "rows": [
                    ["Object / Purpose", "To cause ALARM or coerce an act/omission", "To obtain DELIVERY OF PROPERTY or valuable security"],
                    ["Property Transfer", "Not necessarily aimed at acquiring property", "Directly aimed at obtaining property delivery"],
                    ["Offence Category", "Offence affecting peace & security (Chapter XIX)", "Offence against property (Chapter XVII)"],
                    ["Punishment", "Up to 2 years (7 years if death threat)", "Up to 7 years (or more if threat of death)"]
                ]
            }
        ],
        "diagramId": "diag-crim-punishments-bns",
        "diagramExplanation": "Diagram charts reputation and intimidation offences, highlighting the new community service option.",
        "prelimTraps": [
            {
                "trap": "Believing truth alone is a complete defence to criminal defamation under Indian law.",
                "reality": "Unlike English civil law, the First Exception to Section 356 BNS / Section 499 IPC requires BOTH: TRUTH AND PUBLIC GOOD.",
                "rule": "Defamation Exception 1 = Truth + PUBLIC GOOD."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crim-12-03",
                "front": "What two elements must be proved for the First Exception to Defamation to succeed?",
                "back": "1. The imputation must be TRUE; AND 2. It must be published for the PUBLIC GOOD.",
                "category": "Defamation"
            },
            {
                "id": "fc-crim-12-04",
                "front": "What new alternative punishment is available for Defamation under Section 356(2) BNS 2023?",
                "back": "Community Service (in addition to simple imprisonment up to 2 years or fine).",
                "category": "BNS Innovations"
            }
        ],
        "sourceReferences": [{"title": "Sections 351, 356, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    }
}

# Write complete Part 3
content = f"""/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Criminal Law Module — Authored Concepts (Part 3: Ch 9 to 12)
 * Topics: top-crim-09-01 to top-crim-12-02 (10 Comprehensive Topics)
 */

(function (global) {{
  'use strict';

  const DATA = {json.dumps(CONCEPTS, indent=2)};

  global.CRIMINAL_CONCEPTS_PART3 = DATA;
  if (typeof module !== 'undefined' && module.exports) {{
    module.exports = DATA;
  }}
}})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
"""

with open("assets/learning/data/criminal/criminal-concepts-part3.js", "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully generated assets/learning/data/criminal/criminal-concepts-part3.js ({len(CONCEPTS)} topics)")
