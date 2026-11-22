"""
Complete generator for Criminal Law Concepts Part 1 (12 Topics)
Output: assets/learning/data/criminal/criminal-concepts-part1.js
"""

import json

# Load existing 3 topics
from build_crim_concepts_part1 import CONCEPTS

# Add Chapter 2
CONCEPTS["top-crim-02-01"] = {
    "topicId": "top-crim-02-01",
    "chapterId": "ch-crim-02",
    "subjectId": "law-criminal",
    "title": "Sentencing Framework & Community Service under BNS",
    "subtitle": "The Six Punishments of Section 4 BNS and the New Restorative Sanction",
    "learningObjective": "Master the six statutory punishments under Section 4 BNS (formerly Section 53 IPC), focusing on death penalty standards, life imprisonment, and the revolutionary introduction of community service.",
    "introduction": "Punishment is the coercive sanction imposed by the state upon an offender. Section 4 of the Bharatiya Nyaya Sanhita, 2023 prescribes six distinct classes of punishments: Death, Imprisonment for life, Imprisonment (Rigorous or Simple), Forfeiture of property, Fine, and Community Service. The addition of Community Service represents a major shift towards restorative justice for minor infractions.",
    "detailedExplanation": """
<h3>1. The Six Classes of Punishment (Section 4 BNS / Section 53 IPC)</h3>
<ol>
  <li><strong>Death Penalty:</strong> The ultimate sentence. Preserved under BNS for heinous offences (murder, terrorism, treason, aggravated rape of child under 18). Governed by the constitutional 'rarest of rare' doctrine (<em>Bachan Singh v. State of Punjab</em>).</li>
  <li><strong>Imprisonment for Life:</strong> Means imprisonment for the remainder of the convict's natural life, not a fixed term of 14 or 20 years (<em>Gopal Vinayak Godse v. State of Maharashtra</em>). Executive remission requires compliance with Section 473 BNSS (formerly S. 433A CrPC).</li>
  <li><strong>Imprisonment:</strong> (a) Rigorous (hard labor), or (b) Simple (confinement without hard labor).</li>
  <li><strong>Forfeiture of Property:</strong> Abolished for general offences; reserved for offences against the state.</li>
  <li><strong>Fine:</strong> Monetary sanction, unlimited where no sum expressed, but must not be excessive (S. 8 BNS / S. 63 IPC).</li>
  <li><strong>Community Service (Section 4(f) BNS):</strong> A newly introduced form of punishment. Non-remunerative work for public benefit ordered by court for specified petty offences.</li>
</ol>

<h3>2. The Scope of Community Service in BNS</h3>
<p>Community service may be awarded in specific statutory instances under BNS:</p>
<ul>
  <li>Small theft where value of stolen property is less than Rs 5,000 and offender is first-time offender who restores property (S. 303(2) Proviso);</li>
  <li>Defamation (S. 356(2));</li>
  <li>Misconduct in public by a drunken person (S. 355);</li>
  <li>Public servant unlawfully engaging in trade (S. 202);</li>
  <li>Non-appearance in response to a proclamation (S. 209);</li>
  <li>Attempt to commit suicide to compel public servant to discharge duty (S. 226).</li>
</ul>
""",
    "quickRevisionPoints": [
        "Section 4 BNS prescribes 6 punishments: Death, Life Imprisonment, Imprisonment, Forfeiture, Fine, Community Service.",
        "Community Service is the brand-new 6th punishment introduced in Section 4(f) BNS.",
        "Life imprisonment = Remainder of natural life (Gopal Vinayak Godse).",
        "Community service applies to: theft < Rs 5,000, defamation, public drunkenness, non-appearance on proclamation.",
        "Death penalty governed by 'rarest of rare cases' doctrine (Bachan Singh)."
    ],
    "provisions": [
        {
            "article": "Section 4 BNS",
            "title": "Punishments",
            "text": "The punishments to which offenders are liable under the provisions of this Sanhita are: (a) Death; (b) Imprisonment for life; (c) Imprisonment (rigorous/simple); (d) Forfeiture of property; (e) Fine; (f) Community service.",
            "breakdown": "Expands historical Section 53 IPC by introducing Community Service as a statutory alternative to incarceration."
        }
    ],
    "definitions": [
        {"term": "Community Service", "definition": "Work which the Court may order a convict, or a person who has committed a minor offence, to perform for the benefit of the community without receiving any remuneration."}
    ],
    "ingredients": ["Judicial discretion in sentencing based on aggravating and mitigating circumstances.", "Mandatory statutory limits on fines and imprisonment terms."],
    "exceptions": ["Death penalty cannot be executed on pregnant women (postponed or commuted to life under BNSS S. 416)."],
    "examples": [
        {"scenario": "A first-time offender steals a bicycle valued at Rs 3,500 from a railway platform and promptly returns it during inquiry.", "application": "Under Section 303(2) Proviso BNS, the court may sentence him to perform community service instead of prison."}
    ],
    "landmarkCases": [
        {
            "case": "Bachan Singh v. State of Punjab",
            "citation": "(1980) 2 SCC 684",
            "year": "1980",
            "bench": "5-Judge Constitution Bench (Sarkaria J)",
            "ratio": "The death penalty does not violate Articles 14, 19, or 21 of the Constitution. It must be awarded only in the 'rarest of rare cases' when the alternative option of life imprisonment is unquestionably foreclosed.",
            "impact": "Establishes the foundational balancing of aggravating and mitigating circumstances for capital sentencing."
        },
        {
            "case": "Gopal Vinayak Godse v. State of Maharashtra",
            "citation": "AIR 1961 SC 600",
            "year": "1961",
            "bench": "Subba Rao J",
            "ratio": "A sentence of imprisonment for life is not equivalent to imprisonment for 20 years or 14 years. It means imprisonment for the remaining natural life of the prisoner unless lawfully commuted by the Government.",
            "impact": "Eliminated the popular misconception that life imprisonment expires after 14 or 20 years."
        }
    ],
    "comparisonTables": [
        {
            "title": "Comparison: Punishments under BNS 2023 vs IPC 1860",
            "headers": ["Classification", "BNS Section 4", "IPC Section 53"],
            "rows": [
                ["Number of Punishments", "Six (6) statutory punishments", "Five (5) statutory punishments (Penal Servitude omitted in 1949)"],
                ["Community Service", "Explicitly recognized under Section 4(f)", "Not recognized in general penal code"],
                ["Life Imprisonment", "Defined as remainder of natural life", "Interpreted via case law (Godse)"],
                ["Petty Property Theft", "Community service available if < Rs 5,000", "Mandatory imprisonment or fine"]
            ]
        }
    ],
    "diagramId": "diag-crim-punishments-bns",
    "diagramExplanation": "Diagram illustrates the six classes of statutory punishments with special emphasis on the new community service sanction.",
    "prelimTraps": [
        {
            "trap": "Believing life imprisonment automatically means 14 years or 20 years in jail.",
            "reality": "Life imprisonment means imprisonment for the full remainder of the convict's natural life.",
            "rule": "14 years is only the minimum threshold before which government cannot commute under CrPC S. 433A / BNSS S. 473."
        }
    ],
    "flashcards": [
        {
            "id": "fc-crim-02-01",
            "front": "What is the newly introduced sixth class of punishment in Section 4(f) BNS 2023?",
            "back": "Community Service.",
            "category": "Punishments"
        },
        {
            "id": "fc-crim-02-02",
            "front": "What is the property value ceiling for awarding community service in theft under BNS Section 303(2)?",
            "back": "Value less than five thousand rupees (Rs 5,000), for a first-time offender upon return of property.",
            "category": "Community Service"
        }
    ],
    "sourceReferences": [{"title": "Section 4, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
}

CONCEPTS["top-crim-02-02"] = {
    "topicId": "top-crim-02-02",
    "chapterId": "ch-crim-02",
    "subjectId": "law-criminal",
    "title": "Solitary Confinement, Commutation & Limit of Punishments",
    "subtitle": "Statutory Ceilings under BNS Sections 5–11 vs IPC Sections 54–75",
    "learningObjective": "Master the strict statutory caps on solitary confinement (Section 11 BNS / Sections 73–74 IPC), rules of commutation, and default imprisonment for non-payment of fines.",
    "introduction": "Because penal sanctions infringe upon individual liberty, the law imposes stringent mathematical limits on sentencing. Solitary confinement is subject to absolute caps of 3 months maximum, with periods broken into intervals of not more than 14 days, and 7 days where the sentence exceeds three months. Understanding these limits is high-yield for UP PCS-J preliminary examinations.",
    "detailedExplanation": """
<h3>1. Solitary Confinement (Section 11 BNS / Sections 73 & 74 IPC)</h3>
<p>Whenever any person is convicted of an offence for which the Court has power to sentence him to rigorous imprisonment, the Court may order solitary confinement according to the following mathematical scale:</p>
<ul>
  <li>If term of imprisonment ≤ 6 months: Solitary confinement not exceeding <strong>one month</strong>.</li>
  <li>If term > 6 months and ≤ 1 year: Solitary confinement not exceeding <strong>two months</strong>.</li>
  <li>If term > 1 year: Solitary confinement not exceeding <strong>three months</strong> (absolute ceiling).</li>
</ul>
<p><strong>Limit of Solitary Confinement (Section 11(2) BNS / Section 74 IPC):</strong> Solitary confinement shall in no case exceed <strong>14 days at a time</strong>, with intervals between periods of not less than such periods. When the imprisonment awarded exceeds three months, solitary confinement shall not exceed <strong>7 days in any one month</strong>, with intervals of equal duration.</p>

<h3>2. Limit of Punishment of Offence Made Up of Several Offences (Section 9 BNS / Section 71 IPC)</h3>
<p>Where anything which is an offence is made up of parts, the offender shall not be punished with the punishment of more than one of such his offences unless expressly provided. (e.g. A gives Z 50 strokes with a stick; A can be punished only for one beating, not 50 separate hurts).</p>

<h3>3. Default Imprisonment for Non-Payment of Fine (Section 8 BNS / Sections 64–70 IPC)</h3>
<ul>
  <li>If offence punishable with imprisonment and fine: Term of default imprisonment shall not exceed <strong>one-fourth (1/4th)</strong> of the maximum term fixed for the offence (S. 8(3) BNS / S. 65 IPC).</li>
  <li>If offence punishable with fine only:
    <ul>
      <li>Fine ≤ Rs 5,000 (formerly Rs 50): Simple imprisonment up to <strong>2 months</strong>.</li>
      <li>Fine ≤ Rs 10,000 (formerly Rs 100): Simple imprisonment up to <strong>4 months</strong>.</li>
      <li>In any other case: Simple imprisonment up to <strong>6 months</strong>.</li>
    </ul>
  </li>
  <li>Default imprisonment for fine-only offences must ALWAYS be <strong>simple imprisonment</strong>.</li>
</ul>
""",
    "quickRevisionPoints": [
        "Maximum solitary confinement allowed by law is THREE MONTHS (S. 11 BNS / S. 73 IPC).",
        "Scale: ≤ 6 months imprisonment = 1 month solitary; 6-12 months = 2 months solitary; > 1 year = 3 months solitary.",
        "Intervals: Max 14 days at a time; if sentence > 3 months, max 7 days in any one month.",
        "Default imprisonment for fine where offence punishable with imprisonment = max 1/4th of maximum term.",
        "Fine-only default imprisonment is ALWAYS simple imprisonment (2, 4, or 6 months scale)."
    ],
    "provisions": [
        {
            "article": "Section 11 BNS",
            "title": "Solitary Confinement",
            "text": "Whenever any person is convicted of an offence for which the Court has power to sentence him to rigorous imprisonment, the Court may order solitary confinement not exceeding three months...",
            "breakdown": "Preserves the historical 73/74 IPC scale for solitary confinement with strict humanitarian intervals."
        }
    ],
    "definitions": [{"term": "Solitary Confinement", "definition": "Confinement of a prisoner separate from other inmates without opportunity of social intercourse, allowed only within strict statutory ceilings."}],
    "ingredients": ["Can only be awarded where the main offence is punishable with rigorous imprisonment.", "Subject to strict mathematical limits: 1, 2, or 3 months maximum.", "Strict interval rules between periods."],
    "exceptions": ["Cannot be awarded in offences punishable with simple imprisonment only."],
    "examples": [
        {"scenario": "A court sentences a thief to 9 months rigorous imprisonment and 3 months solitary confinement.", "application": "The sentence is illegal. Under Section 11 BNS / Section 73 IPC, for a term between 6 and 12 months, solitary confinement cannot exceed TWO MONTHS."}
    ],
    "landmarkCases": [
        {
            "case": "Sunil Batra v. Delhi Administration",
            "citation": "(1978) 4 SCC 494",
            "year": "1978",
            "bench": "5-Judge Bench (Krishna Iyer J)",
            "ratio": "Section 30(2) of the Prisons Act does not authorize keeping a prisoner in solitary confinement prior to confirmation of death sentence. Solitary confinement inflicts deep psychological torture and can be imposed only as a punitive judicial sentence within strict statutory limits.",
            "impact": "Constitutionalized prisoners' rights and strictly circumscribed prison authorities' power to isolate convicts."
        }
    ],
    "comparisonTables": [
        {
            "title": "Default Imprisonment Scale for Fine-Only Offences",
            "headers": ["Fine Amount (BNS S. 8(4))", "Historical IPC Scale (S. 67)", "Maximum Default Imprisonment", "Nature of Imprisonment"],
            "rows": [
                ["Not exceeding Rs 5,000", "Not exceeding Rs 50", "Up to 2 Months", "Simple Imprisonment Only"],
                ["Not exceeding Rs 10,000", "Not exceeding Rs 100", "Up to 4 Months", "Simple Imprisonment Only"],
                ["Exceeding Rs 10,000", "Exceeding Rs 100", "Up to 6 Months", "Simple Imprisonment Only"]
            ]
        }
    ],
    "diagramId": "diag-crim-punishments-bns",
    "diagramExplanation": "Diagram summarizes sentencing ceilings, default imprisonment formulas, and solitary confinement scales.",
    "prelimTraps": [
        {
            "trap": "Believing default imprisonment for a fine-only offence can be rigorous imprisonment.",
            "reality": "Under Section 8(4) BNS / Section 67 IPC, default imprisonment for an offence punishable with fine only MUST be simple imprisonment.",
            "rule": "Fine-only default = Always SIMPLE imprisonment."
        }
    ],
    "flashcards": [
        {
            "id": "fc-crim-02-03",
            "front": "What is the absolute maximum period of solitary confinement that can be awarded in any case?",
            "back": "Three (3) months.",
            "category": "Solitary Confinement"
        },
        {
            "id": "fc-crim-02-04",
            "front": "When a prison term exceeds three months, what is the maximum solitary confinement permitted in any single month?",
            "back": "Seven (7) days in any one month, with intervals of equal duration.",
            "category": "Solitary Confinement"
        }
    ],
    "sourceReferences": [{"title": "Sections 8, 9, 11, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
}

# Add Chapter 3
CONCEPTS["top-crim-03-01"] = {
    "topicId": "top-crim-03-01",
    "chapterId": "ch-crim-03",
    "subjectId": "law-criminal",
    "title": "Mistake of Fact vs Mistake of Law & Judicial Acts",
    "subtitle": "BNS Sections 14–17 vs IPC Sections 76–79 & The Bound by Law vs Justified by Law Axiom",
    "learningObjective": "Master the classical general exceptions of Mistake of Fact (Ignorantia facti excusat) versus Mistake of Law (Ignorantia juris non excusat), judicial acts, and lawful executive execution.",
    "introduction": "Chapter III of the Bharatiya Nyaya Sanhita, 2023 codifies General Exceptions (Sections 14 to 44). Sections 14 and 17 embody the ancient common law maxim: <em>Ignorantia facti excusat, ignorantia juris non excusat</em> — ignorance of fact excuses, ignorance of law does not. An act done under a bona fide mistake of fact in good faith is immune from criminal liability, provided the person believed himself to be bound by law (S. 14 BNS / S. 76 IPC) or justified by law (S. 17 BNS / S. 79 IPC).",
    "detailedExplanation": """
<h3>1. Bound by Law: Section 14 BNS / Section 76 IPC</h3>
<p>Nothing is an offence which is done by a person who is, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be, bound by law to do it.</p>
<ul>
  <li><strong>Illustration (a):</strong> A, a soldier, fires on a mob by the order of his superior officer, in conformity with the commands of the law. A has committed no offence.</li>
  <li><strong>Illustration (b):</strong> A, an officer of a Court of Justice, being ordered by that Court to arrest Y, and after due enquiry, believing Z to be Y, arrests Z. A has committed no offence.</li>
</ul>

<h3>2. Justified by Law: Section 17 BNS / Section 79 IPC</h3>
<p>Nothing is an offence which is done by any person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith, believes himself to be justified by law, in doing it.</p>
<ul>
  <li><strong>Illustration:</strong> A sees Z commit what appears to A to be a murder. A, in the exercise, to the best of his judgment exerted in good faith, of the power which the law gives to all persons of apprehending murderers in the act, seizes Z, in order to bring Z before the proper authorities. A has committed no offence, though it may turn out that Z was acting in self-defence.</li>
</ul>

<h3>3. Distinction Between Section 14 and Section 17</h3>
<p>In Section 14, the actor acts under a legal <em>compulsion</em> or duty (bound by law); in Section 17, the actor acts under a legal <em>justification</em> or authorization (justified by law).</p>

<h3>4. Judicial Immunity & Execution of Orders (Sections 15 & 16 BNS / Sections 77 & 78 IPC)</h3>
<ul>
  <li><strong>Section 15 BNS (Section 77 IPC):</strong> Act of Judge when acting judicially in the exercise of any power which is, or which in good faith he believes to be, given to him by law. Complete absolute immunity.</li>
  <li><strong>Section 16 BNS (Section 78 IPC):</strong> Act done pursuant to the judgment or order of a Court of Justice (e.g. hangman executing death warrant). Protected even if the court had no jurisdiction, provided the officer in good faith believes the court possessed jurisdiction.</li>
</ul>
""",
    "quickRevisionPoints": [
        "Maxim: Ignorantia facti excusat (mistake of fact excuses); Ignorantia juris non excusat (mistake of law does not).",
        "Section 14 BNS (S. 76 IPC) = Person bound by law, or believing in good faith by mistake of fact to be bound.",
        "Section 17 BNS (S. 79 IPC) = Person justified by law, or believing in good faith by mistake of fact to be justified.",
        "Section 15 BNS (S. 77 IPC) = Judicial immunity of judges acting judicially.",
        "Section 16 BNS (S. 78 IPC) = Ministerial officers executing court orders (Hangman's protection)."
    ],
    "provisions": [
        {
            "article": "Section 14 BNS",
            "title": "Act done by a person bound, or by mistake of fact believing himself bound, by law",
            "text": "Nothing is an offence which is done by a person who is, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be, bound by law to do it.",
            "breakdown": "Corresponds to Section 76 IPC. Requires mistake of fact + good faith (due care and attention) + belief of being bound by law."
        },
        {
            "article": "Section 17 BNS",
            "title": "Act done by a person justified, or by mistake of fact believing himself justified, by law",
            "text": "Nothing is an offence which is done by any person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith, believes himself to be justified by law, in doing it.",
            "breakdown": "Corresponds to Section 79 IPC. Protection where act is legally justified or mistakenly believed to be justified."
        }
    ],
    "definitions": [
        {"term": "Mistake of Fact", "definition": "An unconscious ignorance or forgetfulness of a fact, past or present, or a belief in the present existence of a thing which does not exist, or in the past existence of a thing which has not existed."},
        {"term": "Mistake of Law", "definition": "Ignorance or erroneous conception of the legal effect of certain facts, which never constitutes a valid defence in criminal law."}
    ],
    "ingredients": ["Mistake must be one of fact, NEVER of law.", "Mistake must be entertaining in good faith (with due care and attention).", "The state of facts believed must have justified or mandated the act if true."],
    "exceptions": ["Mistake of foreign law is treated as a mistake of fact in civil matters, but NOT in criminal prosecutions."],
    "examples": [
        {"scenario": "A police constable is ordered by a sub-inspector to fire upon an orderly, peaceful demonstration without any magistrate order.", "application": "The constable is NOT protected under Section 14 BNS / S. 76 IPC because an order manifestly illegal cannot be obeyed under the cloak of superior orders (State of West Bengal v. Shew Mangal Singh)."}
    ],
    "landmarkCases": [
        {
            "case": "State of West Bengal v. Shew Mangal Singh",
            "citation": "AIR 1981 SC 1917",
            "year": "1981",
            "bench": "Chandrachud CJ",
            "ratio": "A subordinate police officer is bound to obey lawful orders only. An order to fire upon an innocent person is manifestly illegal, and obedience to such an order affords no protection under Section 76 IPC.",
            "impact": "Establishes that the defence of superior orders is unavailable where the order is patently unlawful."
        },
        {
            "case": "Chirangi v. State of MP",
            "citation": "1952 Cri LJ 1212",
            "year": "1952",
            "bench": "Nagpur High Court",
            "ratio": "An adivasi father, suffering from delirium and visual illusion, struck his son with an axe believing him to be a tiger. Held protected under Section 79 IPC as an act done under a bona fide mistake of fact.",
            "impact": "Classic illustration of mistake of fact negativing mens rea."
        }
    ],
    "comparisonTables": [
        {
            "title": "Section 14 BNS (S. 76 IPC) versus Section 17 BNS (S. 79 IPC)",
            "headers": ["Feature", "Section 14 BNS / S. 76 IPC", "Section 17 BNS / S. 79 IPC"],
            "rows": [
                ["Nature of Belief", "Belief of being BOUND by law (Legal Duty)", "Belief of being JUSTIFIED by law (Legal Right/Power)"],
                ["Obligation", "Compulsion under statutory or superior mandate", "Discretionary authority or private citizen power"],
                ["Illustrations", "Soldier firing on lawful command; Bailiff arresting wrong person", "Citizen arresting apparent murderer in self-defence"],
                ["Latin Maxim", "Respondiat superior (qualified)", "Justificatio factualis"]
            ]
        }
    ],
    "diagramId": "diag-crim-mens-rea-liability",
    "diagramExplanation": "Diagram maps mistake of fact as an absolute negation of mens rea under General Exceptions.",
    "prelimTraps": [
        {
            "trap": "Believing a person can claim defence of mistake of law if the statute was newly enacted.",
            "reality": "Ignorantia juris non excusat applies universally. No one can plead ignorance of law (Mayer Hans George).",
            "rule": "Mistake of Fact = Defence; Mistake of Law = NO Defence."
        }
    ],
    "flashcards": [
        {
            "id": "fc-crim-03-01",
            "front": "What is the key difference between Section 14 BNS (S. 76 IPC) and Section 17 BNS (S. 79 IPC)?",
            "back": "Section 14 applies to acts done under belief of being BOUND by law; Section 17 applies to acts done under belief of being JUSTIFIED by law.",
            "category": "General Exceptions"
        },
        {
            "id": "fc-crim-03-02",
            "front": "Which section protects an executioner (hangman) carrying out a death warrant issued by a court?",
            "back": "Section 16 BNS (formerly Section 78 IPC) — acts done pursuant to judgment or order of court.",
            "category": "General Exceptions"
        }
    ],
    "sourceReferences": [{"title": "Sections 14, 15, 16, 17, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
}

CONCEPTS["top-crim-03-02"] = {
    "topicId": "top-crim-03-02",
    "chapterId": "ch-crim-03",
    "subjectId": "law-criminal",
    "title": "Infancy (Doli Incapax) & Insanity: M'Naghten Rules",
    "subtitle": "BNS Sections 20–22 vs IPC Sections 82–84 & Legal vs Medical Insanity",
    "learningObjective": "Master the absolute immunity of children under 7, qualified immunity between 7 and 12 (Doli Incapax), and the M'Naghten rules of legal insanity under Section 22 BNS and Section 84 IPC.",
    "introduction": "Criminal responsibility presupposes the cognitive capacity to understand the nature and quality of one's actions. The law grants absolute immunity to children under 7 years (<em>doli incapax</em>), qualified immunity to children between 7 and 12 years based on maturity of understanding, and full defence to persons suffering from legal insanity under the M'Naghten rules (Section 22 BNS / Section 84 IPC).",
    "detailedExplanation": """
<h3>1. Infancy: Sections 20 & 21 BNS / Sections 82 & 83 IPC</h3>
<ul>
  <li><strong>Absolute Immunity (Section 20 BNS / Section 82 IPC):</strong> Nothing is an offence which is done by a child under <strong>seven years of age</strong>. This is a conclusive presumption of law (<em>juris et de jure</em>) that a child under 7 is <em>doli incapax</em> (incapable of committing crime). No evidence can be led to prove malicious intent.</li>
  <li><strong>Qualified Immunity (Section 21 BNS / Section 83 IPC):</strong> Nothing is an offence which is done by a child above 7 years of age and under <strong>twelve years</strong>, who has not attained sufficient maturity of understanding to judge the nature and consequences of his conduct on that occasion. In <em>Ulla Mahapatra</em> (1950), an 11-year-old who threatened revenge and murdered the deceased with a knife was held to possess sufficient maturity and convicted.</li>
</ul>

<h3>2. Insanity: Section 22 BNS / Section 84 IPC (M'Naghten Rules)</h3>
<p>Nothing is an offence which is done by a person who, at the time of doing it, by reason of unsoundness of mind, is incapable of knowing:</p>
<ol>
  <li>The nature of the act; OR</li>
  <li>That he is doing what is either wrong; OR</li>
  <li>Contrary to law.</li>
</ol>
<p><strong>Crucial Distinction: Legal Insanity versus Medical Insanity:</strong> Medical insanity comprises every mental derangement, delusion, or psychosis recognized by psychiatrists. Legal insanity is strictly confined to cognitive incapacity at the <em>exact moment</em> of the crime as defined in Section 22 BNS. Every medically insane person is NOT legally insane. (<em>Bhikari v. State of UP</em>, AIR 1966 SC 1).</p>
<p><strong>Burden of Proof:</strong> Under Section 108 BSA (formerly S. 105 IEA), the burden of proving legal insanity lies squarely on the accused, though he needs only establish it by a preponderance of probabilities (<em>Dahyabhai Chhaganbhai Thakkar v. State of Gujarat</em>, 1964).</p>
""",
    "quickRevisionPoints": [
        "Child under 7 years = Conclusive immunity (Doli Incapax, S. 20 BNS / S. 82 IPC).",
        "Child 7 to 12 years = Qualified immunity based on maturity of understanding (S. 21 BNS / S. 83 IPC).",
        "Section 22 BNS (S. 84 IPC) codifies the English M'Naghten Rules (1843).",
        "Test of Insanity is COGNITIVE incapacity: incapable of knowing nature of act or that it is wrong/contrary to law.",
        "Medical insanity is NOT legal insanity; burden of proof on accused on preponderance of probabilities."
    ],
    "provisions": [
        {
            "article": "Section 20 BNS",
            "title": "Act of a child under seven years of age",
            "text": "Nothing is an offence which is done by a child under seven years of age.",
            "breakdown": "Absolute irrebuttable presumption of incapacity to form mens rea."
        },
        {
            "article": "Section 22 BNS",
            "title": "Act of a person of unsound mind",
            "text": "Nothing is an offence which is done by a person who, at the time of doing it, by reason of unsoundness of mind, is incapable of knowing the nature of the act, or that he is doing what is either wrong or contrary to law.",
            "breakdown": "Corresponds to Section 84 IPC. Cognitive impairment test at the precise time of act."
        }
    ],
    "definitions": [
        {"term": "Doli Incapax", "definition": "Incapable of doing a criminal wrong; a conclusive presumption applied to children under 7 years."},
        {"term": "Legal Insanity", "definition": "A degree of mental disease destroying cognitive capacity to know the nature of the act or that it is wrong or illegal at the time of commission."}
    ],
    "ingredients": ["Mental impairment existing at the exact time of commission of the act.", "Total cognitive incapacity to comprehend nature of act OR that act was wrong OR contrary to law."],
    "exceptions": ["Moral insanity, emotional frenzy, or uncontrollable impulse is NO defence under Indian law."],
    "examples": [
        {"scenario": "A mother sacrifices her 5-year-old child to please an idol, believing she is obeying divine command, but knows that killing human beings is prohibited by law.", "application": "She is NOT protected under Section 22 BNS / S. 84 IPC because she knew her act was contrary to law (Queen Empress v. Lakshman Dagdu)."}
    ],
    "landmarkCases": [
        {
            "case": "M'Naghten's Case",
            "citation": "(1843) 10 Cl & Fin 200",
            "year": "1843",
            "bench": "House of Lords (Tindal CJ)",
            "ratio": "To establish a defence on the ground of insanity, it must be clearly proved that at the time of committing the act, the party accused was labouring under such a defect of reason from disease of the mind as not to know the nature and quality of the act he was doing, or if he did know it, that he did not know he was doing what was wrong.",
            "impact": "The universal global foundation of criminal insanity codification in Section 84 IPC and Section 22 BNS."
        },
        {
            "case": "Dahyabhai Chhaganbhai Thakkar v. State of Gujarat",
            "citation": "AIR 1964 SC 1563",
            "year": "1964",
            "bench": "Subba Rao J",
            "ratio": "The doctrine of burden of proof in insanity: The prosecution must prove guilt beyond reasonable doubt. The accused can rebut by establishing insanity on preponderance of probabilities. If evidence raises a reasonable doubt as to mens rea, accused is entitled to acquittal.",
            "impact": "Definitive authority on evidentiary standards in Section 84 IPC / Section 22 BNS defences."
        }
    ],
    "comparisonTables": [
        {
            "title": "Medical Insanity versus Legal Insanity",
            "headers": ["Point of Distinction", "Medical Insanity", "Legal Insanity (S. 22 BNS / S. 84 IPC)"],
            "rows": [
                ["Focus", "Medical disease, neurosis, psychosis, behavioral disorder", "Cognitive incapacity to know nature/illegality of act"],
                ["Timing", "Continuous or periodic clinical condition", "Must exist at the precise moment of crime"],
                ["Scope", "Broad clinical spectrum", "Strictly confined to M'Naghten statutory criteria"],
                ["Effect in Court", "Mitigating factor for sentencing", "Complete exculpation / acquittal"]
            ]
        }
    ],
    "diagramId": "diag-crim-mens-rea-liability",
    "diagramExplanation": "Diagram charts infancy and insanity as statutory bars extinguishing criminal capacity.",
    "prelimTraps": [
        {
            "trap": "Believing a child of 8 years is always immune from criminal prosecution.",
            "reality": "Under S. 21 BNS / S. 83 IPC, between 7 and 12 years immunity is qualified; if the child has attained sufficient maturity, he is liable.",
            "rule": "Under 7 = Absolute immunity; 7 to 12 = Qualified immunity based on understanding."
        }
    ],
    "flashcards": [
        {
            "id": "fc-crim-03-03",
            "front": "What age threshold provides absolute immunity (Doli Incapax) under Section 20 BNS / Section 82 IPC?",
            "back": "Under seven (7) years of age.",
            "category": "Infancy"
        },
        {
            "id": "fc-crim-03-04",
            "front": "Which landmark 1843 English case formulated the rules on legal insanity codified in Section 84 IPC / Section 22 BNS?",
            "back": "M'Naghten's Case (1843).",
            "category": "Insanity"
        }
    ],
    "sourceReferences": [{"title": "Sections 20, 21, 22, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
}

CONCEPTS["top-crim-03-03"] = {
    "topicId": "top-crim-03-03",
    "chapterId": "ch-crim-03",
    "subjectId": "law-criminal",
    "title": "Involuntary vs Voluntary Intoxication (Basdev Doctrine)",
    "subtitle": "BNS Sections 23–24 vs IPC Sections 85–86 & The Knowledge vs Intention Dichotomy",
    "learningObjective": "Master the exculpatory defence of involuntary intoxication under Section 23 BNS and the presumption of knowledge in voluntary intoxication under Section 24 BNS (Basdev doctrine).",
    "introduction": "Intoxication impairs judgment and self-control. The law treats involuntary intoxication (administered against will or without knowledge) as a complete defence identical to temporary insanity (Section 23 BNS / Section 85 IPC). Conversely, voluntary drunkenness is no excuse, but Section 24 BNS / Section 86 IPC creates a critical judicial distinction: knowledge is imputed, but intention is NOT automatically presumed.",
    "detailedExplanation": """
<h3>1. Involuntary Intoxication: Section 23 BNS / Section 85 IPC</h3>
<p>Nothing is an offence which is done by a person who, at the time of doing it, is, by reason of intoxication, incapable of knowing the nature of the act, or that he is doing what is either wrong or contrary to law; provided that the thing which intoxicated him was <strong>administered to him without his knowledge or against his will</strong>.</p>
<p>Involuntary intoxication operates on the principle that the actor was blameless in ingesting the intoxicant, and his resulting cognitive incapacity negates criminal responsibility.</p>

<h3>2. Voluntary Intoxication: Section 24 BNS / Section 86 IPC</h3>
<p>Where an act done is not an offence unless done with a particular knowledge or criminal intent, a person who does the act in a state of intoxication shall be liable to be dealt with <strong>as if he had the same knowledge as he would have had if he had not been intoxicated</strong>, unless the thing which intoxicated him was administered without his knowledge or against his will.</p>

<h3>3. The Basdev Doctrine (Knowledge vs Intention)</h3>
<p>In <em>Basdev v. State of Pepsu</em> (AIR 1956 SC 488), the Supreme Court laid down the authoritative law on voluntary drunkenness:</p>
<ul>
  <li>Section 86 IPC / Section 24 BNS attributes to the intoxicated person the same <strong>KNOWLEDGE</strong> as a sober man.</li>
  <li>It does NOT attribute the same <strong>INTENTION</strong>.</li>
  <li>However, intention must be gathered from the totality of circumstances, and drunkenness may be considered to decide whether the accused had formed the requisite specific intent.</li>
  <li>Mere drunkenness is not sufficient; there must be such a degree of intoxication as to render the mind incapable of forming the specific intent required for the crime.</li>
</ul>
<p>In <em>Basdev</em>, a retired military officer attended a wedding, got drunk, asked a young boy to step aside, and when the boy refused, took out a pistol and shot him in the abdomen. Held: Although drunk, his speech and actions showed he was not so incapacitated as to be unable to form the intention to cause bodily injury sufficient to cause death. Convicted of murder under Section 302 IPC.</p>
""",
    "quickRevisionPoints": [
        "Involuntary intoxication (administered without knowledge/against will) = COMPLETE DEFENCE (S. 23 BNS / S. 85 IPC).",
        "Voluntary intoxication = NO complete defence (S. 24 BNS / S. 86 IPC).",
        "Section 24 BNS imputes KNOWLEDGE, but does NOT automatically impute INTENTION (Basdev v. State of Pepsu).",
        "Degree of drunkenness must incapacitate mind from forming specific intent to reduce charge.",
        "D.P.P. v. Beard (1920) is the leading English precedent on drunkenness."
    ],
    "provisions": [
        {
            "article": "Section 23 BNS",
            "title": "Act of a person incapable of judgment by reason of intoxication caused against his will",
            "text": "Nothing is an offence which is done by a person who, at the time of doing it, by reason of intoxication, is incapable of knowing the nature of the act... administered to him without his knowledge or against his will.",
            "breakdown": "Involuntary intoxication provides absolute defence matching Section 85 IPC."
        },
        {
            "article": "Section 24 BNS",
            "title": "Offence requiring a particular intent or knowledge committed by one who is intoxicated",
            "text": "...liable to be dealt with as if he had the same knowledge as he would have had if he had not been intoxicated...",
            "breakdown": "Voluntary drunkenness creates a statutory fiction of knowledge matching Section 86 IPC."
        }
    ],
    "definitions": [
        {"term": "Involuntary Intoxication", "definition": "Intoxication induced by fraud, stratagem, force, or medical accident without the actor's knowledge or consent."},
        {"term": "Basdev Doctrine", "definition": "Rule establishing that Section 86 IPC / S. 24 BNS imputes knowledge to a voluntarily drunk person, while specific intention must be deduced from facts."}
    ],
    "ingredients": ["For S. 23: Administration without knowledge or against will + cognitive incapacity.", "For S. 24: Voluntary ingestion + statutory imputation of knowledge."],
    "exceptions": ["Voluntary drunkenness undertaken deliberately to gather courage to commit a crime (Dutch courage) is an aggravating factor."],
    "examples": [
        {"scenario": "A spikes B's soft drink with heavy liquor without B's knowledge. B hallucinates and smashes a shop window.", "application": "B is protected under Section 23 BNS / S. 85 IPC because intoxication was administered without his knowledge."}
    ],
    "landmarkCases": [
        {
            "case": "Basdev v. State of Pepsu",
            "citation": "AIR 1956 SC 488",
            "year": "1956",
            "bench": "Chandrasekhara Aiyar J",
            "ratio": "Under Section 86 IPC, the law attributes to the intoxicated accused the same knowledge as if he had not been intoxicated. Intention cannot be mechanically presumed, but where the degree of intoxication has not totally incapacitated the mind, intention is inferred from surrounding conduct.",
            "impact": "Authoritative constitutional ruling distinguishing knowledge and intention in voluntary drunkenness."
        },
        {
            "case": "Director of Public Prosecutions v. Beard",
            "citation": "(1920) AC 479",
            "year": "1920",
            "bench": "House of Lords (Lord Birkenhead LC)",
            "ratio": "Evidence of drunkenness falling short of proved incapacity in the accused to form the intent necessary to constitute the crime, and merely establishing that his mind was affected by drink so that he more readily gave way to some violent passion, does not rebut the presumption that a man intends the natural consequences of his acts.",
            "impact": "Foundational common law precedent adopted in Indian jurisprudence."
        }
    ],
    "comparisonTables": [
        {
            "title": "Involuntary Intoxication (S. 23) vs Voluntary Intoxication (S. 24)",
            "headers": ["Metric", "Section 23 BNS (S. 85 IPC)", "Section 24 BNS (S. 86 IPC)"],
            "rows": [
                ["Mode of Ingestion", "Administered without knowledge or against will", "Self-administered voluntarily"],
                ["Legal Status", "Complete General Exception / Exculpatory", "No defence; statutory imputation of knowledge"],
                ["Cognitive Threshold", "Incapable of knowing nature or illegality", "Same knowledge as a sober person imputed"],
                ["Intention Requirement", "Negatives all mens rea completely", "Intention determined from facts (Basdev doctrine)"]
            ]
        }
    ],
    "diagramId": "diag-crim-mens-rea-liability",
    "diagramExplanation": "Diagram charts the bifurcated pathways of involuntary versus voluntary intoxication.",
    "prelimTraps": [
        {
            "trap": "Believing Section 24 BNS (S. 86 IPC) presumes both knowledge and intention.",
            "reality": "The statute explicitly mentions KNOWLEDGE; it does NOT mention intention (Basdev v. State of Pepsu).",
            "rule": "Section 24 BNS presumes KNOWLEDGE, not intention."
        }
    ],
    "flashcards": [
        {
            "id": "fc-crim-03-05",
            "front": "What does Section 24 BNS / Section 86 IPC impute to a voluntarily intoxicated offender?",
            "back": "KNOWLEDGE (as if he were sober); it does NOT automatically impute intention.",
            "category": "Intoxication"
        },
        {
            "id": "fc-crim-03-06",
            "front": "Which leading Supreme Court case established the doctrine of intoxication in Basdev v. State of Pepsu?",
            "back": "Basdev v. State of Pepsu (AIR 1956 SC 488).",
            "category": "Landmark Cases"
        }
    ],
    "sourceReferences": [{"title": "Sections 23, 24, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
}

CONCEPTS["top-crim-03-04"] = {
    "topicId": "top-crim-03-04",
    "chapterId": "ch-crim-03",
    "subjectId": "law-criminal",
    "title": "Consent, Good Faith Medical Acts & Trivial Acts (De Minimis)",
    "subtitle": "BNS Sections 25–33 vs IPC Sections 87–95 & The Maxim De Minimis Non Curat Lex",
    "learningObjective": "Master the principles of consent, medical immunity for surgeries in good faith (Section 26 BNS / Section 88 IPC), consent of guardians, and the doctrine of trivial harm (Section 33 BNS / Section 95 IPC).",
    "introduction": "The law recognizes that certain acts causing harm are justified by social necessity, consent, or their negligible nature. Sections 25 to 33 BNS (formerly Sections 87 to 95 IPC) codify these justifications. The maxim <em>Volenti non fit injuria</em> (to him who consents, no injury is done) protects lawful sports and consensual acts not intended to cause death, while <em>De minimis non curat lex</em> (the law does not notice trifles) immunizes trivial everyday frictions.",
    "detailedExplanation": """
<h3>1. Consensual Acts & Sports (Section 25 BNS / Section 87 IPC)</h3>
<p>Act not intended to cause death or grievous hurt, done by consent in good faith, is not an offence (e.g. fencing, cricket, boxing within rules). Consent must be given by a person above <strong>eighteen years of age</strong> (under BNS / IPC).</p>

<h3>2. Medical Acts Done in Good Faith (Section 26 & 30 BNS / Sections 88 & 92 IPC)</h3>
<ul>
  <li><strong>Section 26 BNS (Section 88 IPC):</strong> Act not intended to cause death, done by consent in good faith for person's benefit (e.g. surgeon operating on a patient for painful calculous with patient's consent; patient dies under surgery; surgeon not guilty).</li>
  <li><strong>Section 30 BNS (Section 92 IPC):</strong> Act done in good faith for benefit of a person <em>without consent</em> where it is impossible for the person to signify consent (e.g. emergency surgery on unconscious road accident victim). Proviso: Cannot extend to intentional causing of death.</li>
</ul>

<h3>3. Vitiated Consent (Section 28 BNS / Section 90 IPC)</h3>
<p>Consent is NOT valid consent if given:</p>
<ol>
  <li>Under fear of injury, or misconception of fact;</li>
  <li>By a person who, from unsoundness of mind or intoxication, is unable to understand the nature of the act;</li>
  <li>By a child under twelve years of age.</li>
</ol>

<h3>4. Trivial Acts / De Minimis (Section 33 BNS / Section 95 IPC)</h3>
<p>Nothing is an offence by reason that it causes, or that it is intended to cause, or that it is known to be likely to cause, any harm, if that harm is so slight that <strong>no person of ordinary sense and temper would complain of such harm</strong>.</p>
<p>Maxim: <em>De minimis non curat lex</em>. In <em>Veeda Menezes v. Yusuf Khan</em> (AIR 1966 SC 1773), throwing a file at a tenant which caused a slight scratch was held trivial and excused under Section 95 IPC.</p>
""",
    "quickRevisionPoints": [
        "Volenti non fit injuria codified in S. 25 BNS (S. 87 IPC); consent age is 18+.",
        "Medical surgery with consent in good faith protected under S. 26 BNS (S. 88 IPC).",
        "Emergency medical surgery without consent protected under S. 30 BNS (S. 92 IPC).",
        "Consent under fear, misconception of fact, insanity, or under 12 years is VOID (S. 28 BNS / S. 90 IPC).",
        "Trivial harm: De minimis non curat lex codified in S. 33 BNS (S. 95 IPC) (Veeda Menezes)."
    ],
    "provisions": [
        {
            "article": "Section 26 BNS",
            "title": "Act not intended to cause death, done by consent in good faith for person's benefit",
            "text": "Nothing which is not intended to cause death, is an offence by reason of any harm which it may cause... to any person for whose benefit it is done in good faith...",
            "breakdown": "Protects bona fide medical practitioners performing risky surgeries with patient consent."
        },
        {
            "article": "Section 33 BNS",
            "title": "Act causing slight harm (De Minimis)",
            "text": "Nothing is an offence by reason that it causes... any harm, if that harm is so slight that no person of ordinary sense and temper would complain of such harm.",
            "breakdown": "Corresponds to Section 95 IPC. Shields everyday negligible frictions from penal prosecution."
        }
    ],
    "definitions": [
        {"term": "Volenti Non Fit Injuria", "definition": "To one who consents, no legal injury is done."},
        {"term": "De Minimis Non Curat Lex", "definition": "The law does not concern itself with trifles or negligible trivialities."}
    ],
    "ingredients": ["Bona fide pursuit of patient/victim's benefit.", "Good faith (due care and attention).", "Absence of intention to cause death."],
    "exceptions": ["Consent cannot excuse an act which is an offence independently of any harm caused to the person (e.g. miscarriage S. 27 BNS / S. 91 IPC)."],
    "examples": [
        {"scenario": "A passenger accidentally steps on another passenger's toes in a crowded Lucknow metro train.", "application": "Protected under Section 33 BNS / Section 95 IPC; the harm is so slight that no person of ordinary sense and temper would complain."}
    ],
    "landmarkCases": [
        {
            "case": "Veeda Menezes v. Yusuf Khan",
            "citation": "AIR 1966 SC 1773",
            "year": "1966",
            "bench": "Shah J",
            "ratio": "Section 95 IPC is intended to prevent penalization of trivialities. Whether an act is trivial depends on the nature of the harm, the intention of the actor, and the social milieu.",
            "impact": "Authoritative precedent on the scope of De Minimis non curat lex."
        }
    ],
    "comparisonTables": [
        {
            "title": "Medical Defence: With Consent (S. 26) vs Without Consent (S. 30)",
            "headers": ["Feature", "Section 26 BNS (S. 88 IPC)", "Section 30 BNS (S. 92 IPC)"],
            "rows": [
                ["Consent Status", "Express or implied consent given by patient", "No consent (impossible to signify or no guardian present)"],
                ["Situation", "Scheduled or elective medical procedures", "Emergency trauma cases (unconscious accident victim)"],
                ["Intent", "Not intended to cause death; done for benefit", "Done in good faith for benefit; cannot extend to causing death"],
                ["IPC Equivalent", "Section 88 IPC", "Section 92 IPC"]
            ]
        }
    ],
    "diagramId": "diag-crim-mens-rea-liability",
    "diagramExplanation": "Diagram maps consent and medical good faith as statutory exculpatory exceptions.",
    "prelimTraps": [
        {
            "trap": "Believing consent of a 14-year-old child to medical surgery is valid on his own.",
            "reality": "Under Section 27 BNS / Section 89 IPC, for a child under 12, consent must be given by the guardian.",
            "rule": "For S. 87 IPC / S. 25 BNS (sports/consent), age is 18; for S. 89 IPC / S. 27 BNS (child guardian consent), age is under 12."
        }
    ],
    "flashcards": [
        {
            "id": "fc-crim-03-07",
            "front": "Which section of BNS codifies the maxim 'De minimis non curat lex' (law does not notice trifles)?",
            "back": "Section 33 BNS (formerly Section 95 IPC).",
            "category": "General Exceptions"
        },
        {
            "id": "fc-crim-03-08",
            "front": "Can consent excuse an act which is an offence independently of any harm caused to the consenting person?",
            "back": "No, per Section 27 BNS / Section 91 IPC (e.g., causing miscarriage).",
            "category": "Consent Exceptions"
        }
    ],
    "sourceReferences": [{"title": "Sections 25, 26, 28, 30, 33, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
}

# Add Chapter 4
CONCEPTS["top-crim-04-01"] = {
    "topicId": "top-crim-04-01",
    "chapterId": "ch-crim-04",
    "subjectId": "law-criminal",
    "title": "Nature, Scope and Statutory Limits of Private Defence",
    "subtitle": "BNS Sections 34–37 vs IPC Sections 96–99 & The Proportionality Principle",
    "learningObjective": "Master the fundamental doctrines of the Right of Private Defence under BNS Sections 34–37 (IPC Sections 96–99), its protective rather than punitive character, and absolute statutory limits under Section 37 BNS.",
    "introduction": "Self-preservation is the first law of nature. The state cannot place a police constable at every citizen's elbow; therefore, the law concedes to every person the right to defend his own body and property, as well as the body and property of any other person, against unlawful aggression (Section 34 & 35 BNS / Section 96 & 97 IPC). However, private defence is a defensive weapon, not a retaliatory shield.",
    "detailedExplanation": """
<h3>1. Foundational Axioms of Private Defence</h3>
<ul>
  <li><strong>Section 34 BNS (Section 96 IPC):</strong> Nothing is an offence which is done in the exercise of the right of private defence.</li>
  <li><strong>Section 35 BNS (Section 97 IPC):</strong> Every person has a right to defend:
    <ol>
      <li>His own body, and the body of <em>any other person</em>, against any offence affecting the human body;</li>
      <li>The property, movable or immovable, of himself or of <em>any other person</em>, against theft, robbery, mischief, or criminal trespass.</li>
    </ol>
  </li>
</ul>
<p>Note that the right extends to defending <strong>strangers</strong>; family or master-servant relationship is not required.</p>

<h3>2. The Proportionality Rule</h3>
<p>In <em>Darshan Singh v. State of Punjab</em> (2010), the Supreme Court reiterated that a person defending himself cannot be expected to weigh his blows in golden scales in the heat of the moment. However, the force used must not be out of all proportion to the aggression. Force must cease the moment apprehension of danger ceases.</p>

<h3>3. Statutory Limits of Private Defence (Section 37 BNS / Section 99 IPC)</h3>
<p>The right of private defence is subject to four absolute limitations:</p>
<ol>
  <li><strong>No right against Public Servants:</strong> No right against an act done, or attempted to be done, by a public servant acting in good faith under color of his office, though that act may not be strictly justifiable by law, provided it does not cause reasonable apprehension of death or grievous hurt.</li>
  <li><strong>No right against Direction of Public Servants:</strong> Same protection applies to persons acting under the direction of a public servant.</li>
  <li><strong>Time to Have Recourse to Public Authorities:</strong> There is no right of private defence in cases in which there is time to have recourse to the protection of the public authorities.</li>
  <li><strong>No Excess Harm:</strong> The right in no case extends to the inflicting of <strong>more harm than it is necessary to inflict</strong> for the purpose of defence.</li>
</ol>
""",
    "quickRevisionPoints": [
        "Private defence is a defensive right, NOT a retributive or punitive right.",
        "Right extends to defending own body/property AND body/property of ANY other person (including strangers).",
        "Section 37 BNS (S. 99 IPC) sets 4 limits: public servant, time for police recourse, no excess harm.",
        "Golden scales doctrine: Defender in heat of moment not expected to weigh blows in golden scales (Darshan Singh).",
        "Right ceases the moment reasonable apprehension of danger terminates."
    ],
    "provisions": [
        {
            "article": "Section 34 BNS",
            "title": "Things done in private defence",
            "text": "Nothing is an offence which is done in the exercise of the right of private defence.",
            "breakdown": "Absolute exculpatory provision matching Section 96 IPC."
        },
        {
            "article": "Section 37 BNS",
            "title": "Acts against which there is no right of private defence",
            "text": "There is no right of private defence against an act which does not reasonably cause the apprehension of death or of grievous hurt... no right where time to have recourse to public authorities... in no case extends to inflicting more harm than necessary.",
            "breakdown": "Corresponds to Section 99 IPC. Lays down the four core statutory boundaries."
        }
    ],
    "definitions": [
        {"term": "Right of Private Defence", "definition": "A statutory preventive right granted to citizens to protect body and property against unlawful criminal aggression where state protection is unavailable."}
    ],
    "ingredients": ["Existence of imminent unlawful aggression.", "Absence of reasonable opportunity to seek police assistance.", "Proportionality between harm threatened and defensive force employed."],
    "exceptions": ["No private defence against free fight where both parties enter into conflict with premeditation.", "No right of private defence against private defence."],
    "examples": [
        {"scenario": "A thief steals a purse and runs away; after he is 500 meters away and unarmed, the owner shoots him in the back.", "application": "Owner is guilty of culpable homicide/murder; the right of private defence ceased once the immediate apprehension of danger ended, and shooting an unarmed fleeing thief inflicts disproportionate harm under Section 37 BNS / S. 99 IPC."}
    ],
    "landmarkCases": [
        {
            "case": "Darshan Singh v. State of Punjab",
            "citation": "(2010) 2 SCC 333",
            "year": "2010",
            "bench": "Dalveer Bhandari J",
            "ratio": "The Supreme Court synthesized ten cardinal principles of private defence: the right is defensive, not punitive; a person cannot be expected to weigh his blows in golden scales; the right commences as soon as a reasonable apprehension of danger arises and continues until the apprehension lasts.",
            "impact": "Authoritative modern compendium on the law of private defence in India."
        }
    ],
    "comparisonTables": [
        {
            "title": "Private Defence of Body vs Private Defence of Property",
            "headers": ["Metric", "Defence of Body (S. 38–40 BNS)", "Defence of Property (S. 41–44 BNS)"],
            "rows": [
                ["Trigger", "Offences affecting human body (murder, hurt, assault)", "Theft, robbery, mischief, criminal trespass"],
                ["Death Caused", "7 specific aggravated apprehension clauses (S. 38)", "4 specific property categories (S. 41)"],
                ["Commencement", "As soon as reasonable apprehension of danger to body arises", "As soon as reasonable apprehension of danger to property arises"],
                ["Continuance", "Continues as long as apprehension to body continues", "Continues till recovery or assistance obtained"]
            ]
        }
    ],
    "diagramId": "diag-crim-private-defence-spectrum",
    "diagramExplanation": "Diagram charts the spectrum of private defence and its four absolute statutory limits under Section 37 BNS.",
    "prelimTraps": [
        {
            "trap": "Assuming private defence is available against a police officer executing an irregular search warrant.",
            "reality": "Under Section 37 BNS / Section 99 IPC, no right of private defence exists against a public servant acting in good faith under color of office, unless there is apprehension of death or grievous hurt.",
            "rule": "Public servant acting in good faith under color of office is protected under S. 37 BNS."
        }
    ],
    "flashcards": [
        {
            "id": "fc-crim-04-01",
            "front": "Does the right of private defence extend to protecting the body and property of a total stranger?",
            "back": "Yes, Section 35 BNS / Section 97 IPC explicitly says 'of himself or of any other person'.",
            "category": "Private Defence"
        },
        {
            "id": "fc-crim-04-02",
            "front": "Which section of BNS lays down the four absolute limitations on the right of private defence?",
            "back": "Section 37 BNS (formerly Section 99 IPC).",
            "category": "Statutory Limits"
        }
    ],
    "sourceReferences": [{"title": "Sections 34, 35, 36, 37, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
}

CONCEPTS["top-crim-04-02"] = {
    "topicId": "top-crim-04-02",
    "chapterId": "ch-crim-04",
    "subjectId": "law-criminal",
    "title": "Private Defence of Body: When Extends to Causing Death",
    "subtitle": "BNS Section 38 vs IPC Section 100 & The Seven Aggravated Threat Categories",
    "learningObjective": "Master the seven statutory categories where the right of private defence of the body extends to the voluntary causing of death under Section 38 BNS and Section 100 IPC, including acid attacks.",
    "introduction": "Causing the death of another human being is the most extreme exercise of private defence. The law restricts this extreme privilege to seven grave situations where the defender reasonably apprehends fatal injury, grievous hurt, rape, unnatural lust, kidnapping, wrongful confinement, or acid attack. In these seven situations under Section 38 BNS (formerly Section 100 IPC), killing the assailant is justified.",
    "detailedExplanation": """
<h3>1. The Seven Clauses of Section 38 BNS / Section 100 IPC</h3>
<p>The right of private defence of the body extends, under the restrictions mentioned in Section 37, to the voluntary causing of death or of any other harm to the assailant, if the offence which occasions the exercise of the right be of any of the following descriptions:</p>
<ol>
  <li><strong>First:</strong> An assault as may reasonably cause the apprehension that death will otherwise be the consequence of such assault.</li>
  <li><strong>Secondly:</strong> An assault as may reasonably cause the apprehension that grievous hurt will otherwise be the consequence of such assault.</li>
  <li><strong>Thirdly:</strong> An assault with the intention of committing <strong>rape</strong>.</li>
  <li><strong>Fourthly:</strong> An assault with the intention of gratifying <strong>unnatural lust</strong>.</li>
  <li><strong>Fifthly:</strong> An assault with the intention of <strong>kidnapping or abducting</strong>.</li>
  <li><strong>Sixthly:</strong> An assault with the intention of wrongfully confining a person, under circumstances which may reasonably cause him to apprehend that he will be unable to have recourse to the public authorities for his release.</li>
  <li><strong>Seventhly:</strong> An act of throwing or administering acid or an attempt to throw or administer acid which may reasonably cause the apprehension that grievous hurt will otherwise be the consequence of such act (Added by 2013 Criminal Law Amendment).</li>
</ol>

<h3>2. Section 39 BNS / Section 101 IPC (When Defence Extends to Harm Other Than Death)</h3>
<p>If the offence be not of any of the descriptions enumerated in Section 38, the right of private defence of the body does NOT extend to the voluntary causing of death to the assailant, but extends to the voluntary causing of any harm other than death.</p>

<h3>3. Section 40 BNS / Section 102 IPC (Commencement and Continuance)</h3>
<p>The right of private defence of the body commences as soon as a <strong>reasonable apprehension of danger to the body arises</strong> from an attempt or threat to commit the offence, though the offence may not have been committed; and it continues as long as such apprehension of danger to the body continues. The defender need not wait until an actual blow is struck.</p>
""",
    "quickRevisionPoints": [
        "Section 38 BNS (S. 100 IPC) prescribes 7 categories where defence of body extends to causing death.",
        "Seven categories: Death, Grievous Hurt, Rape, Unnatural Lust, Kidnapping/Abduction, Wrongful Confinement, Acid Attack.",
        "Acid attack was added as the 7th clause by the 2013 Criminal Law Amendment.",
        "If threat does not fall in the 7 clauses, defender CANNOT cause death (S. 39 BNS / S. 101 IPC).",
        "Commencement: Starts with reasonable apprehension of danger; defender need not wait for blow (S. 40 BNS / S. 102 IPC)."
    ],
    "provisions": [
        {
            "article": "Section 38 BNS",
            "title": "When the right of private defence of the body extends to causing death",
            "text": "The right of private defence of the body extends, under the restrictions mentioned in section 37, to the voluntary causing of death... (1) death apprehension, (2) grievous hurt, (3) rape, (4) unnatural lust, (5) kidnapping/abduction, (6) wrongful confinement, (7) acid attack.",
            "breakdown": "Corresponds to Section 100 IPC with all seven clauses preserved."
        }
    ],
    "definitions": [{"term": "Reasonable Apprehension", "definition": "A well-grounded, bona fide fear of imminent harm evaluated from the standpoint of an ordinary person placed in the defender's specific situation."}],
    "ingredients": ["Aggression falling within one of the seven statutory clauses.", "Existence of reasonable apprehension of consequence.", "Defensive act performed within limits of Section 37 BNS."],
    "exceptions": ["Cannot cause death if aggression is mere simple hurt or simple assault."],
    "examples": [
        {"scenario": "A man attempts to rape a woman in an isolated field; the woman grabs a stone and smashes his skull, killing him.", "application": "The woman is completely exonerated under Section 38(3) BNS / Section 100(3) IPC; defence of body against rape extends to voluntary causing of death."}
    ],
    "landmarkCases": [
        {
            "case": "Amjad Khan v. State",
            "citation": "AIR 1952 SC 165",
            "year": "1952",
            "bench": "Bose J",
            "ratio": "A defender faced with an armed mob attempting to break into his shop is not expected to modulate his defensive shots precisely. A reasonable apprehension of death or grievous hurt justifies firing upon the mob under Section 100 IPC.",
            "impact": "Classic authority on reasonable apprehension of death justifying firearms usage."
        }
    ],
    "comparisonTables": [
        {
            "title": "Section 38 BNS (Causing Death) vs Section 39 BNS (Harm Other Than Death)",
            "headers": ["Attribute", "Section 38 BNS (S. 100 IPC)", "Section 39 BNS (S. 101 IPC)"],
            "rows": [
                ["Level of Threat", "Grave threat (Death, Grievous Hurt, Rape, Acid)", "Lesser threat (Simple hurt, simple assault, battery)"],
                ["Maximum Force Permitted", "Voluntary causing of DEATH", "Any harm OTHER THAN death"],
                ["Statutory Clauses", "Seven specific exhaustive categories", "Residual clause covering all other bodily offences"],
                ["Excess Force Consequence", "Exoneration if within limits", "If death caused, culpable homicide under Exception 2 to S. 101 BNS"]
            ]
        }
    ],
    "diagramId": "diag-crim-private-defence-spectrum",
    "diagramExplanation": "Diagram details the seven specific statutory clauses authorizing the taking of life in bodily defence.",
    "prelimTraps": [
        {
            "trap": "Believing an assault to commit theft allows killing the assailant in defence of body.",
            "reality": "Theft is a property offence; defence of body against simple theft does NOT allow causing death unless accompanied by apprehension of death/grievous hurt.",
            "rule": "Only the 7 specific bodily clauses under Section 38 BNS allow causing death."
        }
    ],
    "flashcards": [
        {
            "id": "fc-crim-04-03",
            "front": "How many statutory categories under Section 38 BNS / Section 100 IPC allow causing death in defence of body?",
            "back": "Seven (7) categories.",
            "category": "Private Defence of Body"
        },
        {
            "id": "fc-crim-04-04",
            "front": "Which category was added to Section 100 IPC / Section 38 BNS by the Criminal Law (Amendment) Act, 2013?",
            "back": "Clause Seventhly: Act of throwing or administering acid or an attempt to throw/administer acid.",
            "category": "Amendments"
        }
    ],
    "sourceReferences": [{"title": "Sections 38, 39, 40, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
}

CONCEPTS["top-crim-04-03"] = {
    "topicId": "top-crim-04-03",
    "chapterId": "ch-crim-04",
    "subjectId": "law-criminal",
    "title": "Private Defence of Property: Extent and Causing Death",
    "subtitle": "BNS Sections 41–44 vs IPC Sections 103–105 & Night House-Breaking Rules",
    "learningObjective": "Master the four statutory situations where private defence of property extends to causing death under Section 41 BNS (Section 103 IPC), and rules of commencement and continuance under Section 44 BNS.",
    "introduction": "While human life takes precedence over property, the law permits the voluntary causing of death in defence of property against four severe property crimes: Robbery, House-breaking by night, Mischief by fire or explosive substance to human dwellings/vessels, and Theft/mischief/house-trespass creating apprehension of death or grievous hurt (Section 41 BNS / Section 103 IPC).",
    "detailedExplanation": """
<h3>1. When Defence of Property Extends to Causing Death (Section 41 BNS / Section 103 IPC)</h3>
<p>The right of private defence of property extends, under the restrictions mentioned in Section 37, to the voluntary causing of death or of any other harm to the wrong-doer, if the offence, the committing of which, or the attempting to commit which, occasions the exercise of the right, be an offence of any of the descriptions following:</p>
<ol>
  <li><strong>First:</strong> <strong>Robbery</strong> (all forms of robbery under S. 309 BNS / S. 390 IPC);</li>
  <li><strong>Secondly:</strong> <strong>House-breaking by night</strong> (after sunset and before sunrise);</li>
  <li><strong>Thirdly:</strong> <strong>Mischief by fire or any explosive substance</strong> committed on any building, tent or vessel, which building, tent or vessel is used as a human dwelling, or as a place for the custody of property;</li>
  <li><strong>Fourthly:</strong> <strong>Theft, mischief, or house-trespass</strong>, under such circumstances as may reasonably cause apprehension that death or grievous hurt will be the consequence, if such right of private defence is not exercised.</li>
</ol>

<h3>2. Section 42 BNS / Section 104 IPC (Harm Other Than Death)</h3>
<p>If the offence be theft, mischief, or criminal trespass not of any of the descriptions in Section 41, the right extends only to voluntary causing of harm <em>other than death</em>.</p>

<h3>3. Commencement & Continuance of Defence of Property (Section 44 BNS / Section 105 IPC)</h3>
<ul>
  <li>Commences when a reasonable apprehension of danger to property commences.</li>
  <li><strong>Against Theft:</strong> Continues till the offender has effected his retreat with the property, or either the assistance of the public authorities is obtained, or the property has been recovered.</li>
  <li><strong>Against Robbery:</strong> Continues as long as the offender causes or attempts to cause to any person death or hurt or wrongful restraint or as long as the fear of instant death/hurt/restraint continues.</li>
  <li><strong>Against Criminal Trespass / Mischief:</strong> Continues as long as the offender continues in the commission of criminal trespass or mischief.</li>
  <li><strong>Against House-breaking by night:</strong> Continues as long as the house-trespass which has been begun by such house-breaking continues.</li>
</ul>
""",
    "quickRevisionPoints": [
        "Section 41 BNS (S. 103 IPC) specifies 4 property offences where causing death is justified.",
        "Four offences: Robbery, House-breaking by night, Mischief by fire/explosive to dwelling/storage, Theft/trespass with fear of death/grievous hurt.",
        "Day house-breaking does NOT allow causing death unless accompanied by apprehension of death/grievous hurt.",
        "Theft defence continues until offender retreats with property, or assistance obtained, or property recovered.",
        "Mischief by fire to an open field does NOT allow causing death (must be building/tent/vessel used for dwelling/storage)."
    ],
    "provisions": [
        {
            "article": "Section 41 BNS",
            "title": "When right of private defence of property extends to causing death",
            "text": "The right of private defence of property extends... to the voluntary causing of death: (a) Robbery; (b) House-breaking after sunset and before sunrise; (c) Mischief by fire/explosives on building/tent/vessel; (d) Theft/mischief/trespass causing fear of death/grievous hurt.",
            "breakdown": "Corresponds to Section 103 IPC. Strictly defines the four property offences justifying homicide."
        }
    ],
    "definitions": [{"term": "House-Breaking by Night", "definition": "House-breaking committed after sunset and before sunrise (S. 329 BNS / S. 446 IPC)."}],
    "ingredients": ["Commission or attempt of one of the four statutory property offences.", "Proportionality and necessity of defensive force under Section 37 BNS.", "No time to seek assistance of public authorities."],
    "exceptions": ["Simple theft or daytime house-trespass without threat to life does not allow causing death."],
    "examples": [
        {"scenario": "A homeowner discovers an intruder climbing through a broken window at 2:00 AM holding an iron rod; the owner strikes the intruder with a bat, causing his death.", "application": "Protected under Section 41(b) BNS / Section 103(b) IPC (House-breaking by night); causing death is legally justified."}
    ],
    "landmarkCases": [
        {
            "case": "State of UP v. Ram Swarup",
            "citation": "AIR 1974 SC 1570",
            "year": "1974",
            "bench": "Chandrachud J",
            "ratio": "The right of private defence of property commences as soon as a reasonable apprehension of danger to the property commences. The defender is not entitled to use more force than necessary, but once the four categories of Section 103 IPC are met, taking of life is permissible.",
            "impact": "Clarified that peaceful possession is essential before claiming private defence of property."
        }
    ],
    "comparisonTables": [
        {
            "title": "Causing Death in Defence of Property: The Four Clauses",
            "headers": ["Clause", "Offence Description", "Essential Condition"],
            "rows": [
                ["First", "Robbery", "Any robbery (instant violence or fear)"],
                ["Second", "House-breaking by night", "Must be between sunset and sunrise"],
                ["Third", "Mischief by fire/explosives", "On building, tent, or vessel used as dwelling/custody of property"],
                ["Fourth", "Theft, mischief, or house-trespass", "Circumstances reasonably causing apprehension of death or grievous hurt"]
            ]
        }
    ],
    "diagramId": "diag-crim-private-defence-spectrum",
    "diagramExplanation": "Diagram charts the four specific property offences authorizing the voluntary causing of death.",
    "prelimTraps": [
        {
            "trap": "Believing mischief by fire to agricultural crops allows killing the offender under Section 41 BNS.",
            "reality": "Mischief by fire under S. 41(c) BNS / S. 103(c) IPC must be to a building, tent, or vessel used as a human dwelling or for property custody.",
            "rule": "Mischief by fire to crops = Section 42 BNS (Harm other than death)."
        }
    ],
    "flashcards": [
        {
            "id": "fc-crim-04-05",
            "front": "What are the four property offences where the right of private defence extends to causing death?",
            "back": "1. Robbery; 2. House-breaking by night; 3. Mischief by fire/explosives to dwelling/store; 4. Theft/trespass with fear of death/grievous hurt.",
            "category": "Private Defence of Property"
        },
        {
            "id": "fc-crim-04-06",
            "front": "Until when does the right of private defence of property against theft continue?",
            "back": "Until offender retreats with property, or assistance of public authorities obtained, or property recovered.",
            "category": "Continuance of Defence"
        }
    ],
    "sourceReferences": [{"title": "Sections 41, 42, 43, 44, Bharatiya Nyaya Sanhita, 2023", "url": "https://www.mha.gov.in"}]
}

# Write complete Part 1
content = f"""/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Criminal Law Module — Authored Concepts (Part 1: Ch 1 to 4)
 * Topics: top-crim-01-01 to top-crim-04-03 (12 Comprehensive Topics)
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

print(f"Successfully generated assets/learning/data/criminal/criminal-concepts-part1.js ({len(CONCEPTS)} topics)")
