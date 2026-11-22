"""
Builds Criminal Law Concepts Part 1 (Chapters 1 to 4: 12 Topics)
- Chapter 1: top-crim-01-01, top-crim-01-02, top-crim-01-03
- Chapter 2: top-crim-02-01, top-crim-02-02
- Chapter 3: top-crim-03-01, top-crim-03-02, top-crim-03-03, top-crim-03-04
- Chapter 4: top-crim-04-01, top-crim-04-02, top-crim-04-03
"""

import json

CONCEPTS = {
    "top-crim-01-01": {
        "topicId": "top-crim-01-01",
        "chapterId": "ch-crim-01",
        "subjectId": "law-criminal",
        "title": "Title, Territorial Scope & Commencement (1 July 2024)",
        "subtitle": "Territorial and Extra-Territorial Jurisdiction under BNS & IPC",
        "learningObjective": "Master the territorial boundaries, maritime jurisdiction, extraterritorial applicability, and the 1 July 2024 commencement framework under BNS Section 1 and IPC Sections 1 to 4.",
        "introduction": "Substantive criminal law defines offences and prescribes punishments. The Bharatiya Nyaya Sanhita, 2023 (BNS) was enacted by Parliament as Act No. 45 of 2023, coming into force on 1 July 2024. Under Article 20(1) of the Constitution of India, criminal statutes operate prospectively; hence offences committed prior to 1 July 2024 remain governed by the Indian Penal Code, 1860 (IPC), while offences committed on or after 1 July 2024 are charged exclusively under the BNS.",
        "detailedExplanation": """
<h3>1. Enactment, Title and Commencement</h3>
<p>Section 1 of the Bharatiya Nyaya Sanhita, 2023 establishes that the Act may be called the Bharatiya Nyaya Sanhita, 2023 and came into force on <strong>1 July 2024</strong> across the whole of India. Unlike the historical IPC which originally excepted Jammu & Kashmir prior to the 2019 Reorganisation Act, the BNS applies uniformly to all territories from day one.</p>

<h3>2. Intra-Territorial Jurisdiction (Section 1(2) BNS / Section 2 IPC)</h3>
<p>Every person—regardless of nationality, citizenship, rank, or status—is liable to punishment under the Sanhita for every act or omission contrary to its provisions of which he is guilty within India. Foreign nationals committing an offence on Indian soil cannot plead ignorance of Indian law (<em>State of Maharashtra v. Mayer Hans George</em>, AIR 1965 SC 722).</p>
<p>Territory of India includes:</p>
<ul>
  <li>The land mass within international borders of India;</li>
  <li>Maritime territory up to <strong>12 nautical miles</strong> (Territorial Waters, Continental Shelf, EEZ and other Maritime Zones Act, 1976);</li>
  <li>Airspace superjacent to Indian land and territorial waters;</li>
  <li>Indian flag vessels and aircraft wherever they may be situated.</li>
</ul>

<h3>3. Extra-Territorial Jurisdiction (Section 1(3) & 1(4) BNS / Sections 3 & 4 IPC)</h3>
<p>The Sanhita applies to any offence committed beyond India by:</p>
<ol>
  <li>Any citizen of India in any place without and beyond India;</li>
  <li>Any person on any ship or aircraft registered in India wherever it may be;</li>
  <li>Any person in any place without and beyond India committing an offence targeting a computer resource located in India (cyber jurisdiction).</li>
</ol>
<p>In <em>Mobarik Ali Ahmed v. State of Bombay</em> (AIR 1957 SC 857), the Supreme Court held that where a Pakistani national induced a Mumbai merchant through letters and telegrams from Karachi to part with money, the offence of cheating was completed in Mumbai, and the accused was amenable to Indian penal jurisdiction upon arrest in India.</p>
""",
        "quickRevisionPoints": [
            "BNS came into force on 1 July 2024 (Act 45 of 2023); historical offences remain under IPC 1860.",
            "BNS S. 1 consolidates title, extent, commencement, and extra-territorial jurisdiction (formerly IPC S. 1-4).",
            "Intra-territorial jurisdiction applies to ALL persons (citizens & foreigners) within India and 12 nautical miles maritime belt.",
            "Extra-territorial jurisdiction covers Indian citizens anywhere, Indian flag vessels/aircraft, and attacks targeting Indian computer resources.",
            "Mobarik Ali Ahmed (1957): Foreigner acting from abroad is liable where the offence is completed in India."
        ],
        "provisions": [
            {
                "article": "Section 1 BNS",
                "title": "Short title, commencement and application",
                "text": "This Act may be called the Bharatiya Nyaya Sanhita, 2023. It shall come into force on such date as the Central Government may appoint... applies to whole of India and extra-territorial acts.",
                "breakdown": "Consolidates title, territorial application within 12 nautical miles, and extra-territorial reach over citizens, vessels, and computer systems.",
                "exceptions": "President and Governors enjoy immunity during term of office under Article 361; foreign sovereigns and diplomatic envoys under Vienna Convention."
            },
            {
                "article": "Section 1 to 4 IPC",
                "title": "Historical Title, Extent and Extra-Territorial Jurisdiction",
                "text": "Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof...",
                "breakdown": "Historical framework dividing intra-territorial (S. 2) and extra-territorial jurisdiction (S. 3, 4)."
            }
        ],
        "definitions": [
            {"term": "Intra-Territorial Jurisdiction", "definition": "Jurisdiction exercisable over all offences committed within the physical land boundaries, airspace, and 12-nautical-mile territorial waters of India."},
            {"term": "Extra-Territorial Jurisdiction", "definition": "Statutory power to try and punish offences committed beyond the territory of India by Indian citizens, on Indian registered vessels, or targeting Indian cyber infrastructure."}
        ],
        "ingredients": [
            "Commission of an act or omission prohibited by the Sanhita.",
            "Locus of offence within Indian territory, or personal/protective nexus (Indian citizen, registered vessel, Indian computer resource).",
            "Absence of constitutional or diplomatic immunity."
        ],
        "exceptions": [
            "Foreign diplomatic envoys and ambassadors accredited to India enjoy full criminal immunity under Vienna Convention on Diplomatic Relations.",
            "Foreign sovereigns visiting India in official capacity.",
            "Foreign warships in Indian territorial waters (extraterritorial status)."
        ],
        "examples": [
            {
                "scenario": "An Indian citizen commits murder in Paris and flees to Lucknow. Can he be tried in Lucknow under Indian penal law?",
                "application": "Yes. Under Section 1(3)(a) BNS (formerly S. 4(1) IPC), an Indian citizen who commits an offence anywhere beyond India can be dealt with in India as if the offence had been committed at the place where he is found, subject to sanction under S. 208 BNSS (formerly S. 188 CrPC)."
            }
        ],
        "landmarkCases": [
            {
                "case": "State of Maharashtra v. Mayer Hans George",
                "citation": "AIR 1965 SC 722",
                "year": "1965",
                "bench": "3-Judge Bench (Subba Rao, Dayal, Mudholkar JJ)",
                "ratio": "Ignorance of Indian statutory notifications is no defence for a foreign national passing through Indian airspace. Publication in the Official Gazette constitutes sufficient legal notice.",
                "impact": "Establishes that foreign nationals entering Indian jurisdiction are bound strictly by Indian penal enactments without separate personal notice."
            },
            {
                "case": "Mobarik Ali Ahmed v. State of Bombay",
                "citation": "AIR 1957 SC 857",
                "year": "1957",
                "bench": "Jagannadhadas J",
                "ratio": "Physical presence of the offender in India at the time of committing the crime is not essential for intra-territorial jurisdiction under Section 2 IPC if the acts take effect and complete the crime within India.",
                "impact": "Foundational precedent for cross-border and cyber jurisdiction under Section 1(4) BNS."
            }
        ],
        "comparisonTables": [
            {
                "title": "Comparison: BNS Section 1 vs IPC Sections 1–4",
                "headers": ["Metric", "BNS 2023 (Section 1)", "IPC 1860 (Sections 1–4)"],
                "rows": [
                    ["Structure", "Consolidated single section (S. 1)", "Four separate sections (S. 1, 2, 3, 4)"],
                    ["Commencement", "1 July 2024 (prospective operation)", "1 January 1862"],
                    ["Geographical Extent", "Whole of India uniformly from day one", "Originally excluded J&K until 2019 Reorganisation Act"],
                    ["Cyber Infrastructure", "Expressly covers targeting computer resources in India (S. 1(4))", "Added via IT Act 2000 amendment to Section 4(3)"]
                ]
            }
        ],
        "diagramId": "diag-crim-mens-rea-liability",
        "diagramExplanation": "Diagram maps the foundational architecture of criminal liability, starting from territorial jurisdiction to actus reus, mens rea, and strict liability.",
        "prelimTraps": [
            {
                "trap": "Believing an offence committed in June 2024 can be charged under BNS 2023.",
                "reality": "Article 20(1) bars retrospective penal law. Offences committed before 1 July 2024 MUST be charged under IPC 1860.",
                "rule": "Offence date governs substantive law: before 1 July 2024 = IPC; on/after 1 July 2024 = BNS."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crim-01-01",
                "front": "What is the exact date of commencement of the Bharatiya Nyaya Sanhita, 2023?",
                "back": "1 July 2024 (Ministry of Home Affairs Gazette Notification S.O. 850(E)).",
                "category": "Commencement & Enactment"
            },
            {
                "id": "fc-crim-01-02",
                "front": "What maritime distance constitutes Indian territorial waters for penal jurisdiction?",
                "back": "12 nautical miles from the appropriate baseline into the sea.",
                "category": "Territorial Jurisdiction"
            },
            {
                "id": "fc-crim-01-03",
                "front": "Which section of BNS codifies extraterritorial jurisdiction over Indian citizens and cyber attacks?",
                "back": "Section 1, sub-sections (3) and (4) BNS (formerly Sections 3 & 4 IPC).",
                "category": "Extraterritorial Jurisdiction"
            }
        ],
        "sourceReferences": [
            {"title": "Bharatiya Nyaya Sanhita, 2023 (Bare Act No. 45 of 2023)", "url": "https://www.mha.gov.in"},
            {"title": "Constitution of India, Article 20(1) (Protection against Ex-Post Facto Laws)", "url": "https://legislative.gov.in"}
        ]
    },

    "top-crim-01-02": {
        "topicId": "top-crim-01-02",
        "chapterId": "ch-crim-01",
        "subjectId": "law-criminal",
        "title": "Statutory Definitions & Interpretations in BNS & IPC",
        "subtitle": "The Consolidated Lexicon of Criminal Law: Section 2 BNS vs IPC Sections 6–52A",
        "learningObjective": "Master the cardinal statutory definitions in Section 2 BNS, analyzing modern modifications including gender neutrality in definitions, transgender recognition, electronic records, and mental illness.",
        "introduction": "While the Indian Penal Code scattered definitions across Chapters I and II (Sections 6 to 52A), the Bharatiya Nyaya Sanhita, 2023 consolidates all interpretive clauses into a single alphabetical definitions section—Section 2, clauses (1) to (39). Understanding these statutory definitions is indispensable for judicial examinations because they govern the substantive scope of offences throughout the code.",
        "detailedExplanation": """
<h3>1. Structural Consolidation in Section 2 BNS</h3>
<p>Section 2 BNS arranges definitions alphabetically from clause (1) 'act' to clause (39) 'wrongful gain / wrongful loss'. This modern legislative drafting technique replaces the disjointed arrangement in IPC where terms like 'dishonestly' were in S. 24, 'fraudulently' in S. 25, 'document' in S. 29, and 'good faith' in S. 52.</p>

<h3>2. Key Modified & Modernized Definitions</h3>
<ul>
  <li><strong>Child (Section 2(3) BNS):</strong> Explicitly defined as any person below the age of eighteen years, harmonizing penal law with the POCSO Act, 2012 and Juvenile Justice Act, 2015.</li>
  <li><strong>Gender (Section 2(10) BNS):</strong> The pronoun 'he' and its derivatives are used for any person, whether male, female, or <em>transgender</em>. This explicitly codifies the Supreme Court's mandate in <em>NALSA v. Union of India</em> (2014).</li>
  <li><strong>Electronic Record & Document (Section 2(6) & 2(8) BNS):</strong> 'Document' explicitly includes any electronic and digital record. Section 2(6) adopts the definition of electronic record from the Information Technology Act, 2000.</li>
  <li><strong>Mental Illness (Section 2(20) BNS):</strong> Replaces the antiquated phrase 'unsoundness of mind' in contemporary interpretative terminology, aligning with the Mental Healthcare Act, 2017.</li>
</ul>

<h3>3. Cardinal Unchanged Definitions</h3>
<ul>
  <li><strong>Dishonestly (Section 2(7) BNS / Section 24 IPC):</strong> Doing anything with the intention of causing wrongful gain to one person or wrongful loss to another.</li>
  <li><strong>Fraudulently (Section 2(9) BNS / Section 25 IPC):</strong> Doing a thing with intent to defraud, but not otherwise (requires deceit + injury/risk of injury, per <em>Dr. Vimla v. Delhi Administration</em>).</li>
  <li><strong>Good Faith (Section 2(11) BNS / Section 52 IPC):</strong> Nothing is said to be done or believed in 'good faith' which is done or believed without due care and attention. Honest belief without due diligence is NOT good faith.</li>
  <li><strong>Public Servant (Section 2(28) BNS / Section 21 IPC):</strong> Defines 12 categories of public servants including commissioned officers, judges, court officers, arbitrators, and every person in service or pay of government.</li>
</ul>
""",
        "quickRevisionPoints": [
            "Section 2 BNS consolidates over 45 definitions into 39 alphabetical clauses.",
            "Child = Person below 18 years (S. 2(3) BNS).",
            "Gender = 'He' includes male, female, and transgender (S. 2(10) BNS).",
            "Dishonestly = Intent to cause wrongful gain or wrongful loss (S. 2(7) BNS).",
            "Fraudulently = Intent to defraud (Deceit + Injury) (Dr. Vimla v. Delhi Admn).",
            "Good Faith = Requires due care and attention (S. 2(11) BNS); subjective honesty alone is insufficient."
        ],
        "provisions": [
            {
                "article": "Section 2 BNS",
                "title": "Definitions Clause",
                "text": "In this Sanhita, unless the context otherwise requires... (1) 'act', (3) 'child', (7) 'dishonestly', (8) 'document', (9) 'fraudulently', (10) 'gender', (11) 'good faith', (28) 'public servant'...",
                "breakdown": "Consolidated single interpretive section applying throughout the entire Sanhita."
            }
        ],
        "definitions": [
            {"term": "Dishonestly", "definition": "Doing anything with the intention of causing wrongful gain to one person or wrongful loss to another person."},
            {"term": "Fraudulently", "definition": "Doing a thing with intent to defraud, which requires deceit combined with injury or economic/non-economic loss."}
        ],
        "ingredients": [
            "Statutory interpretation according to definitions unless context indicates contrary intent.",
            "Good faith requires positive demonstration of due care and caution.",
            "Distinction between wrongful economic gain (dishonest) and deceitful deprivation (fraudulent)."
        ],
        "exceptions": [
            "Definitions do not apply where the contextual subject matter specifically overrides the general definition."
        ],
        "examples": [
            {
                "scenario": "A doctor uses an unsterilized scalpel believing honestly that it is clean, resulting in infection.",
                "application": "Cannot claim 'good faith' under Section 2(11) BNS / Section 52 IPC because he acted without due care and attention, even though he harbored no malicious motive."
            }
        ],
        "landmarkCases": [
            {
                "case": "Dr. Vimla v. Delhi Administration",
                "citation": "AIR 1963 SC 1572",
                "year": "1963",
                "bench": "Subba Rao J",
                "ratio": "The word 'defraud' involves two elements: deceit and injury to the person deceived. Deceit without injury or risk of injury does not constitute fraud.",
                "impact": "Definitive authority distinguishing 'fraudulently' from 'dishonestly'."
            }
        ],
        "comparisonTables": [
            {
                "title": "Distinction: 'Dishonestly' versus 'Fraudulently'",
                "headers": ["Point of Distinction", "Dishonestly (S. 2(7) BNS)", "Fraudulently (S. 2(9) BNS)"],
                "rows": [
                    ["Core Ingredient", "Wrongful gain or wrongful loss of property", "Deceit accompanied by injury or risk of injury"],
                    ["Nature of Injury", "Exclusively economic/pecuniary", "May be non-economic (reputation, body, property)"],
                    ["Deceit Requirement", "Deceit is NOT an essential ingredient", "Deceit is an INDISPENSABLE ingredient"],
                    ["IPC Reference", "Section 24 IPC", "Section 25 IPC"]
                ]
            }
        ],
        "diagramId": "diag-crim-mens-rea-liability",
        "diagramExplanation": "Diagram clarifies the mental elements: how dishonesty and fraudulence provide the mens rea for property and document offences.",
        "prelimTraps": [
            {
                "trap": "Assuming good faith in penal law means 'acting with honest intention'.",
                "reality": "In criminal law (S. 2(11) BNS / S. 52 IPC), honesty is immaterial; 'due care and attention' is mandatory.",
                "rule": "Good Faith in Penal Law = Due care and attention (unlike Contract Act where honesty without negligence is good faith)."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crim-01-04",
                "front": "How is 'Good Faith' defined in Section 2(11) BNS / Section 52 IPC?",
                "back": "Negatively: Nothing is said to be done or believed in good faith which is done or believed without due care and attention.",
                "category": "Statutory Definitions"
            },
            {
                "id": "fc-crim-01-05",
                "front": "What two elements must co-exist to prove 'fraudulently' per Dr. Vimla's case?",
                "back": "Deceit and Injury (or risk of injury) to the person deceived.",
                "category": "Statutory Definitions"
            }
        ],
        "sourceReferences": [
            {"title": "Section 2, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}
        ]
    },

    "top-crim-01-03": {
        "topicId": "top-crim-01-03",
        "chapterId": "ch-crim-01",
        "subjectId": "law-criminal",
        "title": "Actus Reus, Mens Rea & Strict Liability in Penal Law",
        "subtitle": "The Foundational Maxim: Actus Non Facit Reum Nisi Mens Sit Rea",
        "learningObjective": "Master the interaction between the physical actus reus and the mental mens rea, exploring the four stages of crime and statutory strict liability exceptions.",
        "introduction": "The cardinal axiom of criminal jurisprudence is expressed in the Latin maxim: <em>Actus non facit reum nisi mens sit rea</em> — the physical act itself does not constitute guilt unless the mind is also guilty. Every crime generally requires the concurrence of an unlawful physical act (actus reus) and a blameworthy mental state (mens rea), subject to statutory exceptions of strict liability.",
        "detailedExplanation": """
<h3>1. Elements of Crime</h3>
<p>To establish criminal liability, four foundational elements must converge:</p>
<ol>
  <li><strong>Human Being:</strong> The act must be committed by a person under legal obligation to obey the law and capable of punishment.</li>
  <li><strong>Mens Rea (Guilty Mind):</strong> The mental element required for the specific offence (intention, knowledge, recklessness, or negligence). The IPC and BNS do not use the term 'mens rea' in the abstract; instead, specific mental states are codified in definitions (e.g. 'dishonestly', 'voluntarily', 'knowingly', 'malignantly', 'rashly').</li>
  <li><strong>Actus Reus (Unlawful Physical Act/Omission):</strong> A physical result of human conduct which the law prohibits, including illegal omissions (S. 3(1) BNS / S. 32 IPC).</li>
  <li><strong>Injury (Harm):</strong> Illegal harm caused to any person in body, mind, reputation, or property (S. 2(14) BNS / S. 44 IPC).</li>
</ol>

<h3>2. The Four Stages of Crime</h3>
<ol>
  <li><strong>Intention:</strong> Purely internal mental contemplation. Never punishable in itself because law cannot read minds and thoughts are free.</li>
  <li><strong>Preparation:</strong> Devising or arranging the means. Generally not punishable because locus poenitentiae (opportunity to repent) remains. <em>Exceptions where preparation is punishable:</em> Waging war (S. 148 BNS / S. 122 IPC), and Making preparation for dacoity (S. 312 BNS / S. 399 IPC).</li>
  <li><strong>Attempt:</strong> Direct movement towards commission of crime after preparation. Always punishable (S. 62 BNS / S. 511 IPC).</li>
  <li><strong>Commission (Consummation):</strong> Successful completion of the offence.</li>
</ol>

<h3>3. Strict Liability Offences (Exclusion of Mens Rea)</h3>
<p>In statutory crimes, Parliament may exclude mens rea to protect public welfare. As laid down in <em>State of Maharashtra v. Mayer Hans George</em> (AIR 1965 SC 722) and <em>Suresh Kumar v. State</em>, mens rea is presumed unless the statute expressly or by necessary implication rules it out. Examples in penal law: Kidnapping from lawful guardianship (S. 137 BNS / S. 361 IPC), Waging war, and Public nuisance.</p>
""",
        "quickRevisionPoints": [
            "Maxim: Actus non facit reum nisi mens sit rea (Act does not make guilty without guilty mind).",
            "Four elements: Human being + Mens rea + Actus reus + Injury (S. 2(14) BNS).",
            "Four stages: Intention (not punishable) -> Preparation (generally not punishable) -> Attempt (always punishable) -> Commission.",
            "Only 2 Preparations punishable in general penal law: Waging war (S. 148 BNS) and Dacoity preparation (S. 312 BNS).",
            "Strict Liability: Kidnapping from guardianship has no mens rea requirement regarding minor's age (R v. Prince)."
        ],
        "provisions": [
            {
                "article": "Section 3(1) BNS",
                "title": "General Principles & Words referring to acts include illegal omissions",
                "text": "In every part of this Sanhita, except where a contrary intention appears from the context, words which refer to acts done extend also to illegal omissions.",
                "breakdown": "Actus reus includes both positive commission of unlawful acts and illegal omissions where a legal duty exists."
            }
        ],
        "definitions": [
            {"term": "Actus Reus", "definition": "The external, physical element of a crime consisting of voluntary human conduct (act or illegal omission) prohibited by law."},
            {"term": "Mens Rea", "definition": "The blameworthy mental state (intention, knowledge, recklessness) accompanying the forbidden physical act."}
        ],
        "ingredients": [
            "Concurrence of physical actus reus and mental mens rea at the time of the offence.",
            "Causal link between the conduct and the prohibited harm.",
            "Rebuttable presumption of mens rea in every statutory penal offence."
        ],
        "exceptions": [
            "Offences of strict and absolute liability where legislative intent excludes mens rea for public welfare.",
            "Kidnapping from lawful guardianship where honest belief as to age is no defence."
        ],
        "examples": [
            {
                "scenario": "A buys poison with intent to kill B, places it on his desk, but before administering it, feels remorse and throws it away.",
                "application": "A is not guilty of attempt because his conduct was still in the stage of preparation; locus poenitentiae existed and no direct step towards administration was taken."
            }
        ],
        "landmarkCases": [
            {
                "case": "R. v. Prince",
                "citation": "(1875) LR 2 CCR 154",
                "year": "1875",
                "bench": "Blackburn J, Bramwell B",
                "ratio": "Prince took an unmarried girl under sixteen out of possession of her father, honestly and reasonably believing her to be eighteen based on her appearance. Held guilty; mens rea as to age was excluded by the legislature in kidnapping.",
                "impact": "Classic common law cornerstone for strict liability in offences protecting minors."
            },
            {
                "case": "State of Maharashtra v. Mayer Hans George",
                "citation": "AIR 1965 SC 722",
                "year": "1965",
                "bench": "Subba Rao, Dayal JJ",
                "ratio": "Unless a statute either clearly or by necessary implication rules out mens rea as a constituent part of a crime, a defendant cannot be found guilty without a guilty mind.",
                "impact": "Established the standard test for strict liability statutes in India."
            }
        ],
        "comparisonTables": [
            {
                "title": "Preparation versus Attempt: Legal Tests",
                "headers": ["Test", "Legal Principle", "Key Precedent"],
                "rows": [
                    ["Proximity Test", "The act must be proximate to the intended result and not remote", "Commonwealth v. Peaslee"],
                    ["Locus Poenitentiae", "If accused still has time to repent and abandon without intervention, it is preparation", "Malkiat Singh v. State of Punjab"],
                    ["Equivocality Test", "An act is an attempt if it unequivocally indicates the end goal", "Barker's Principle"],
                    ["On the Job Test", "Attempt begins when the execution of the crime actually commences", "Abhayanand Mishra v. State of Bihar"]
                ]
            }
        ],
        "diagramId": "diag-crim-mens-rea-liability",
        "diagramExplanation": "Diagram maps the four sequential stages of crime from mental intention to physical commission.",
        "prelimTraps": [
            {
                "trap": "Believing that preparation is never punishable under Indian penal law.",
                "reality": "Preparation is punishable in two specific instances: Waging War and Preparation for Dacoity.",
                "rule": "Preparation is punishable for Waging War (S. 148 BNS / S. 122 IPC) and Preparation for Dacoity (S. 312 BNS / S. 399 IPC)."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crim-01-06",
                "front": "What does the maxim 'Actus non facit reum nisi mens sit rea' mean?",
                "back": "An act does not make a person legally guilty unless the mind is also guilty.",
                "category": "Criminal Maxims"
            },
            {
                "id": "fc-crim-01-07",
                "front": "Name the two offences where preparation alone is made punishable by statute.",
                "back": "1. Waging war against the Government (S. 148 BNS / S. 122 IPC); 2. Preparation for Dacoity (S. 312 BNS / S. 399 IPC).",
                "category": "Stages of Crime"
            }
        ],
        "sourceReferences": [
            {"title": "Glanville Williams: Criminal Law (The General Part)", "url": "https://www.sweetandmaxwell.co.uk"},
            {"title": "Section 62, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}
        ]
    }
}

# Write Part 1
content = f"""/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Criminal Law Module — Authored Concepts (Part 1: Ch 1 to 4)
 * Topics: top-crim-01-01 to top-crim-04-03
 */

(function (global) {{
  'use strict';

  const DATA = {json.dumps(CONCEPTS, indent=2)};

  global.CRIMINAL_CONCEPTS_PART1 = DATA;
  if (typeof module !== 'undefined' && module.exports) {{
    module.exports = DATA;
  }}
}})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
"""

with open("assets/learning/data/criminal/criminal-concepts-part1.js", "w", encoding="utf-8") as f:
    f.write(content)

print("Written criminal-concepts-part1.js initial batch")
