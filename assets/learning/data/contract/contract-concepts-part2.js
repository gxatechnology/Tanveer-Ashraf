/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Judicial Learning Academy Data Module
 */
(function(global) {
  'use strict';

  const DATA = {
  "top-cnt-05-01": {
    "topicId": "top-cnt-05-01",
    "chapterId": "ch-cnt-05",
    "subjectId": "law-contract",
    "title": "Misrepresentation: Types, Remedies & Exceptions (Sections 18, 19)",
    "subtitle": "Innocent Falsehood, Duty of Care, and Ordinary Diligence",
    "bareActRef": "Indian Contract Act, 1872 — Sections 18, 19",
    "learningObjective": "Analyze the three heads of misrepresentation under Section 18, the exception of ordinary diligence under Section 19, and rescission remedies.",
    "detailedExplanation": "\n<h3>1. Statutory Definition: Section 18</h3>\n<p>'Misrepresentation' means and includes:</p>\n<ol>\n  <li><strong>Unwarranted Positive Assertion:</strong> The positive assertion, in a manner not warranted by the information of the person making it, of that which is not true, though he believes it to be true (Section 18(1)).</li>\n  <li><strong>Breach of Duty Without Intent to Deceive:</strong> Any breach of duty which, without an intent to deceive, gains an advantage to the person committing it, by misleading another to his prejudice (Section 18(2) — Constructive Fraud).</li>\n  <li><strong>Innocent Mistake as to Substance:</strong> Causing, however innocently, a party to an agreement to make a mistake as to the substance of the thing which is the subject of the agreement (Section 18(3)).</li>\n</ol>\n\n<h3>2. The Crucial Exception to Section 19: Ordinary Diligence</h3>\n<p>Section 19 provides that misrepresentation renders a contract voidable. However, the <strong>Exception to Section 19</strong> states: <em>'If such consent was caused by misrepresentation or by silence fraudulent within the meaning of section 17, the contract, nevertheless, is not voidable, if the party whose consent was so caused had the means of discovering the truth with ordinary diligence.'</em></p>\n<p>If a buyer of a factory is handed falsified books, but his own accountants verify the figures independently and fail to spot errors, or if he is given the means and fails to look, he cannot later rescind for innocent misrepresentation (<em>Kamal Kant v. Prakash Devi</em>).</p>\n",
    "quickRevisionPoints": [
      "Section 18: Unwarranted positive assertion, constructive breach of duty, or causing innocent mistake as to substance.",
      "Misrepresentation lacks fraudulent intent (mens rea).",
      "Section 19 Exception: If the party had means of discovering truth with ordinary diligence, contract is NOT voidable.",
      "Remedies: Rescission under Section 19, or insisting on performance as represented.",
      "No damages in tort for innocent misrepresentation (distinguished from fraud)."
    ],
    "provisions": [
      {
        "provision": "Section 18, ICA 1872",
        "title": "Misrepresentation Defined",
        "description": "Positive assertions not warranted by information, breach of duty gaining advantage without intent to deceive, or innocently causing mistake as to substance."
      },
      {
        "provision": "Section 19 Exception, ICA 1872",
        "title": "Ordinary Diligence Bar",
        "description": "Contract is not voidable if the party whose consent was caused by misrepresentation had means of discovering the truth with ordinary diligence."
      }
    ],
    "definitions": [
      {
        "term": "Constructive Fraud",
        "definition": "A breach of duty that gains an unfair advantage without an actual dishonest intent to deceive."
      }
    ],
    "ingredients": [
      "False statement of fact.",
      "Absence of dishonest motive.",
      "Inducement of the other party into contract."
    ],
    "exceptions": [
      "Ordinary diligence bar under Section 19 Exception."
    ],
    "examples": [
      {
        "scenario": "A tells B that his sheep farm produces 2,000 pounds of wool annually, based on what his manager told him. It actually produces only 1,200 pounds.",
        "application": "A had no intent to deceive, but the statement was an unwarranted positive assertion under Section 18(1), entitling B to rescind."
      }
    ],
    "landmarkCases": [
      {
        "case": "Derry v. Peek",
        "citation": "(1889) 14 App Cas 337",
        "year": "1889",
        "bench": "House of Lords",
        "ratio": "An honest belief in the truth of a statement prevents it from being fraudulent, relegating the claim to innocent misrepresentation where no tort damages lie.",
        "impact": "Classic dividing line between fraud and misrepresentation."
      }
    ],
    "comparisonTables": [
      {
        "title": "Fraud vs Misrepresentation Exception",
        "headers": [
          "Factor",
          "Fraud (Active)",
          "Misrepresentation (s. 18)"
        ],
        "rows": [
          [
            "Ordinary Diligence Defense",
            "NOT available to fraudulent party",
            "Available under Section 19 Exception"
          ],
          [
            "Intent",
            "Deliberate deceit",
            "Innocent or negligent belief"
          ],
          [
            "Damages Claim",
            "Yes, tort of deceit",
            "No general tort damages"
          ]
        ]
      }
    ],
    "diagramId": "diag-cnt-fraud-misrep",
    "diagramExplanation": "Custom vector schematic displaying the three categories of misrepresentation and the ordinary diligence test.",
    "misconceptions": [
      {
        "myth": "The 'ordinary diligence' exception applies to active fraudulent assertions.",
        "reality": "The exception applies only to misrepresentation and silence fraud. It does NOT protect a party guilty of positive active fraud."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing damages are automatically available for misrepresentation under Indian Contract Act.",
        "reality": "Indian Contract Act gives only rescission or rectification; tort damages require proof of fraud.",
        "rule": "Misrepresentation = Rescission; Fraud = Rescission + Damages."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-05-01",
        "front": "What are the three forms of Misrepresentation defined in Section 18?",
        "back": "Unwarranted positive assertion, breach of duty without intent to deceive, and causing innocent mistake as to substance.",
        "category": "Misrepresentation"
      },
      {
        "id": "fc-cnt-05-02",
        "front": "What does the Exception to Section 19 lay down regarding ordinary diligence?",
        "back": "A contract is not voidable for misrepresentation if the aggrieved party had the means of discovering the truth with ordinary diligence.",
        "category": "Ordinary Diligence"
      },
      {
        "id": "fc-cnt-05-03",
        "front": "Does the ordinary diligence defense protect a person who makes an active fraudulent misstatement?",
        "back": "No, it does not apply to active, positive fraud.",
        "category": "Exceptions to Diligence"
      },
      {
        "id": "fc-cnt-05-04",
        "front": "What remedy is available to a party induced by misrepresentation under Section 19?",
        "back": "Rescission of contract or insisting that the contract be performed on the basis that the representation was true.",
        "category": "Remedies"
      }
    ],
    "sourceReferences": [
      {
        "title": "Indian Contract Act, 1872",
        "url": "https://indiacode.nic.in"
      }
    ]
  },
  "top-cnt-05-02": {
    "topicId": "top-cnt-05-02",
    "chapterId": "ch-cnt-05",
    "subjectId": "law-contract",
    "title": "Mistake of Fact: Bilateral vs Unilateral Mistake (Sections 20, 22)",
    "subtitle": "Nullity of Consensus and the Protective Limits of Unilateral Error",
    "bareActRef": "Indian Contract Act, 1872 — Sections 20, 22",
    "learningObjective": "Distinguish between Bilateral Mistake under Section 20 (agreement void) and Unilateral Mistake under Section 22 (contract not voidable), and exceptions.",
    "detailedExplanation": "\n<h3>1. Bilateral Mistake of Essential Fact: Section 20</h3>\n<p>'Where both the parties to an agreement are under a mistake as to a matter of fact essential to the agreement, the agreement is void.'</p>\n<ul>\n  <li><strong>Both Parties Mistaken:</strong> The error must be mutual/bilateral.</li>\n  <li><strong>Matter of Fact:</strong> Not an error of law or mere opinion of value (Explanation to Section 20: an erroneous opinion as to value is not a mistake of fact).</li>\n  <li><strong>Essential to the Agreement:</strong> Going to the root of the contract (e.g., identity or existence of subject-matter: <em>Couturier v. Hastie</em> — corn sold had already fermented and been discarded at sea; agreement void).</li>\n</ul>\n\n<h3>2. Unilateral Mistake: Section 22</h3>\n<p>'A contract is not voidable merely because it was caused by one of the parties to it being under a mistake as to a matter of fact.'</p>\n<p>General rule: One party's personal misunderstanding does not relieve him of contractual obligations (<em>Caveat Emptor</em>).</p>\n<p><strong>Two Recognized Exceptions where Unilateral Mistake Renders Contract Void:</strong></p>\n<ol>\n  <li><strong>Mistake as to Identity of the Contracting Person:</strong> Where identity is material and induced by fraud (<em>Cundy v. Lindsay</em>; <em>Ingram v. Little</em>).</li>\n  <li><strong>Mistake as to Nature of the Document (Non Est Factum):</strong> Where a person signs a document fundamentally different in character from what he intended, without negligence (<em>Foster v. Mackinnon</em>).</li>\n</ol>\n",
    "quickRevisionPoints": [
      "Section 20: Bilateral mistake as to essential matter of fact renders agreement void ab initio.",
      "Explanation to Section 20: Erroneous opinion as to value is NOT a mistake of fact.",
      "Section 22: Unilateral mistake does NOT render contract voidable (contract remains valid).",
      "Exceptions to unilateral mistake: Mistake as to personal identity (Cundy v. Lindsay) and Non est factum (Foster v. Mackinnon).",
      "Couturier v. Hastie: Cargo perished before contract; agreement void for bilateral mistake."
    ],
    "provisions": [
      {
        "provision": "Section 20, ICA 1872",
        "title": "Agreement Void Where Both Parties Under Mistake of Fact",
        "description": "Where both parties to an agreement are under a mistake as to a matter of fact essential to the agreement, the agreement is void."
      },
      {
        "provision": "Section 22, ICA 1872",
        "title": "Contract Caused by Mistake of One Party as to Matter of Fact",
        "description": "A contract is not voidable merely because it was caused by one of the parties to it being under a mistake as to a matter of fact."
      }
    ],
    "definitions": [
      {
        "term": "Non Est Factum",
        "definition": "It is not my deed; an equitable defense allowing a signer to repudiate a document if fundamentally different in nature from what was represented."
      }
    ],
    "ingredients": [
      "Mutuality of error for Section 20.",
      "Subject-matter essentiality.",
      "Absence of mere valuation error."
    ],
    "exceptions": [
      "Identity fraud and non est factum under unilateral mistake."
    ],
    "examples": [
      {
        "scenario": "A agrees to buy a horse from B. Unbeknownst to both parties, the horse had died an hour before the agreement was made.",
        "application": "The agreement is void under Section 20 due to bilateral mistake regarding the existence of the subject matter."
      }
    ],
    "landmarkCases": [
      {
        "case": "Couturier v. Hastie",
        "citation": "(1856) 5 HLC 673",
        "year": "1856",
        "bench": "House of Lords",
        "ratio": "A contract for the sale of a cargo of corn supposed to be on transit at sea was void because, unknown to both parties, the cargo had fermented and been sold before the contract was entered into.",
        "impact": "Bedrock authority on bilateral mistake as to existence of subject matter."
      },
      {
        "case": "Foster v. Mackinnon",
        "citation": "(1869) LR 4 CP 704",
        "year": "1869",
        "bench": "Court of Common Pleas (Byles J)",
        "ratio": "An elderly gentleman was induced to sign a bill of exchange on the fraudulent representation that it was a guarantee. Held: The mind of the signer did not accompany the signature; defense of non est factum succeeded.",
        "impact": "Classic authority on unilateral mistake regarding nature of document."
      }
    ],
    "comparisonTables": [
      {
        "title": "Bilateral Mistake vs Unilateral Mistake",
        "headers": [
          "Aspect",
          "Bilateral Mistake (s. 20)",
          "Unilateral Mistake (s. 22)"
        ],
        "rows": [
          [
            "Parties Mistaken",
            "Both parties",
            "Only one party"
          ],
          [
            "Legal Result",
            "Agreement is VOID ab initio",
            "Contract remains VALID and enforceable"
          ],
          [
            "Exceptions",
            "Erroneous opinion of value is not mistake",
            "Void if mistake as to identity or non est factum"
          ]
        ]
      }
    ],
    "diagramId": "diag-cnt-validity-consent",
    "diagramExplanation": "Custom vector schematic illustrating the diverging results of bilateral vs unilateral mistake.",
    "misconceptions": [
      {
        "myth": "If one party miscalculated market prices, he can avoid the contract for mistake.",
        "reality": "Under Section 22 and Explanation to Section 20, unilateral price or valuation errors do not affect contractual validity."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Labeling a contract under Section 20 as 'voidable'.",
        "reality": "Section 20 explicitly says the agreement is VOID, not voidable.",
        "rule": "Bilateral mistake = VOID."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-05-05",
        "front": "What is the legal effect of a bilateral mistake of fact essential to an agreement under Section 20?",
        "back": "The agreement is VOID ab initio.",
        "category": "Mistake of Fact"
      },
      {
        "id": "fc-cnt-05-06",
        "front": "Does a unilateral mistake of fact make a contract voidable under Section 22?",
        "back": "No, a contract is not voidable merely because one party was mistaken as to a matter of fact.",
        "category": "Unilateral Mistake"
      },
      {
        "id": "fc-cnt-05-07",
        "front": "Is an erroneous opinion as to the value of the subject-matter a mistake of fact?",
        "back": "No, Explanation to Section 20 explicitly excludes erroneous opinions as to value.",
        "category": "Valuation"
      },
      {
        "id": "fc-cnt-05-08",
        "front": "What does the plea 'Non Est Factum' mean in contract law?",
        "back": "'It is not my deed' — mistake as to the character and nature of the document signed.",
        "category": "Legal Maxims"
      }
    ],
    "sourceReferences": [
      {
        "title": "Indian Contract Act, 1872",
        "url": "https://indiacode.nic.in"
      }
    ]
  },
  "top-cnt-05-03": {
    "topicId": "top-cnt-05-03",
    "chapterId": "ch-cnt-05",
    "subjectId": "law-contract",
    "title": "Mistake of Law: Indian Law vs Foreign Law (Section 21)",
    "subtitle": "Ignorantia Juris Non Excusat and the Special Status of Foreign Law",
    "bareActRef": "Indian Contract Act, 1872 — Section 21",
    "learningObjective": "Master the rule of Section 21 on mistake of Indian law vs mistake of foreign law, and the maxim Ignorantia juris non excusat.",
    "detailedExplanation": "\n<h3>1. Mistake as to Law in Force in India: Section 21</h3>\n<p>'A contract is not voidable because it was caused by a mistake as to any law in force in India.' This codifies the universal legal maxim: <strong>Ignorantia juris non excusat</strong> (Ignorance of the law is no excuse). Every citizen is presumed to know the law of the land; parties cannot escape contractual liabilities by claiming they misunderstood an Indian statutory provision or tax regulation.</p>\n\n<h3>2. Mistake as to Foreign Law</h3>\n<p>The second paragraph of Section 21 creates a vital rule: <em>'A mistake as to a law not in force in India has the same effect as a mistake of fact.'</em></p>\n<p>Under Indian Evidence Act, foreign law is not judicially noticed; it is a question of fact that must be pleaded and proved by expert evidence. Therefore:</p>\n<ul>\n  <li>A bilateral mistake regarding foreign law is treated as a <strong>mistake of fact under Section 20</strong>, rendering the agreement <strong>void</strong>!</li>\n  <li>A unilateral mistake regarding foreign law is governed by Section 22.</li>\n</ul>\n\n<h3>3. Mistake as to Private Rights</h3>\n<p>In English law (<em>Cooper v. Phibbs</em>), a mistake as to a private right of ownership was treated as a mistake of fact. In India, courts generally follow this equitable approach where parties contract in mutual ignorance of an existing private proprietary right.</p>\n",
    "quickRevisionPoints": [
      "Maxim: Ignorantia juris non excusat — ignorance of law is no excuse.",
      "Mistake of Indian law: Contract is NOT voidable; remains valid and enforceable.",
      "Mistake of Foreign law: Treated as a mistake of FACT.",
      "Bilateral mistake of foreign law renders agreement VOID under Section 20.",
      "Cooper v. Phibbs: Mistake as to private title treated as mistake of fact."
    ],
    "provisions": [
      {
        "provision": "Section 21, ICA 1872",
        "title": "Effect of Mistakes as to Law",
        "description": "A contract is not voidable because it was caused by a mistake as to any law in force in India; but a mistake as to a law not in force in India has the same effect as a mistake of fact."
      }
    ],
    "definitions": [
      {
        "term": "Ignorantia Juris Non Excusat",
        "definition": "Ignorance of the law excuses not; a conclusive presumption that everyone knows the legal rules of their jurisdiction."
      }
    ],
    "ingredients": [
      "Distinction between domestic legal provisions and foreign laws.",
      "Treatment of foreign law as an evidentiary fact.",
      "Application of Section 20 to bilateral foreign legal error."
    ],
    "exceptions": [
      "Misrepresentation of law by a party in a fiduciary position may be relieved as constructive fraud."
    ],
    "examples": [
      {
        "scenario": "A and B enter into a contract in Bombay believing that French law permits export of certain wines, whereas French law strictly prohibits it.",
        "application": "Because French law is foreign law, their bilateral mistake is treated as a mistake of fact, rendering the agreement void under Section 20."
      }
    ],
    "landmarkCases": [
      {
        "case": "Cooper v. Phibbs",
        "citation": "(1867) LR 2 HL 149",
        "year": "1867",
        "bench": "House of Lords (Lord Westbury)",
        "ratio": "A nephew agreed to lease a fishery from his uncle's daughters, unaware that under a family settlement the fishery already belonged to him. Held: A mistake as to private ownership, though involving law, is treated as a mistake of fact; the lease was void.",
        "impact": "Classic authority on mistake of private rights."
      }
    ],
    "comparisonTables": [
      {
        "title": "Mistake of Indian Law vs Foreign Law",
        "headers": [
          "Aspect",
          "Mistake of Indian Law",
          "Mistake of Foreign Law"
        ],
        "rows": [
          [
            "Presumption of Knowledge",
            "Conclusive presumption that parties know the law",
            "No presumption; treated as question of fact"
          ],
          [
            "Legal Effect on Contract",
            "Contract remains valid (Not voidable)",
            "Treated as mistake of fact (Void if bilateral)"
          ],
          [
            "Governing Rule",
            "Section 21, Para 1",
            "Section 21, Para 2 read with Section 20"
          ]
        ]
      }
    ],
    "diagramId": "diag-cnt-validity-consent",
    "diagramExplanation": "Custom vector schematic showing the divergent paths of domestic vs foreign legal mistake.",
    "misconceptions": [
      {
        "myth": "A contract entered under a mistake of foreign law is always valid in India.",
        "reality": "Foreign law is treated as fact; if both parties were mistaken about foreign law, the contract is void under Section 20."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing mistake of Indian law makes a contract voidable.",
        "reality": "Section 21 explicitly says: 'A contract is NOT voidable because it was caused by a mistake as to any law in force in India.'",
        "rule": "Mistake of Indian Law = Contract Valid."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-05-09",
        "front": "What is the legal effect of a mistake as to any law in force in India under Section 21?",
        "back": "The contract is NOT voidable (remains valid).",
        "category": "Mistake of Law"
      },
      {
        "id": "fc-cnt-05-10",
        "front": "How is a mistake as to a law not in force in India treated under Section 21?",
        "back": "It has the same effect as a mistake of fact.",
        "category": "Foreign Law"
      },
      {
        "id": "fc-cnt-05-11",
        "front": "Translate the legal maxim: 'Ignorantia juris non excusat'.",
        "back": "Ignorance of the law is no excuse.",
        "category": "Legal Maxims"
      },
      {
        "id": "fc-cnt-05-12",
        "front": "What did Lord Westbury hold in Cooper v. Phibbs regarding mistake of private rights?",
        "back": "A mistake as to private title is treated as a mistake of fact, entitling relief.",
        "category": "Private Rights"
      }
    ],
    "sourceReferences": [
      {
        "title": "Indian Contract Act, 1872",
        "url": "https://indiacode.nic.in"
      }
    ]
  },
  "top-cnt-06-01": {
    "topicId": "top-cnt-06-01",
    "chapterId": "ch-cnt-06",
    "subjectId": "law-contract",
    "title": "Unlawful Consideration & Public Policy Doctrine (Section 23)",
    "subtitle": "The Five Heads of Illegality and the Unruly Horse of Public Policy",
    "bareActRef": "Indian Contract Act, 1872 — Section 23",
    "learningObjective": "Master the 5 statutory heads of unlawful consideration/object under Section 23 and the judicial doctrine of public policy.",
    "detailedExplanation": "\n<h3>1. The Five Heads of Section 23</h3>\n<p>The consideration or object of an agreement is unlawful if:</p>\n<ol>\n  <li><strong>Forbidden by Law:</strong> Prohibited by an express penal statute or legislative enactment (e.g., sale of smuggled goods or narcotics).</li>\n  <li><strong>Defeats the Provisions of Any Law:</strong> Though not directly forbidden, it would indirectly circumvent and defeat the legislative policy of any statute (e.g., agreeing not to plead limitation, or evading tenancy ceiling laws).</li>\n  <li><strong>Is Fraudulent:</strong> Intended to cheat or defraud third parties or the public revenue.</li>\n  <li><strong>Involves or Implies Injury to Person or Property:</strong> E.g., an agreement to publish a criminal libel, commit an assault, or bond an individual into perpetual slavery.</li>\n  <li><strong>Opposed to Public Policy or Immoral:</strong> Violates the fundamental moral consensus or public interest of society.</li>\n</ol>\n\n<h3>2. The Doctrine of Public Policy: 'The Unruly Horse'</h3>\n<p>Burrough J famously declared in <em>Richardson v. Mellish (1824)</em> that public policy is <em>'a very unruly horse, and when once you get astride it you never know where it will carry you.'</em></p>\n<p>Recognized Heads of Public Policy in Indian Law:</p>\n<ul>\n  <li><strong>Trading with Alien Enemy:</strong> Commercial intercourse during wartime is void.</li>\n  <li><strong>Stifling Criminal Prosecution:</strong> Compounding non-compoundable public offenses for monetary gain.</li>\n  <li><strong>Maintenance and Champerty:</strong> In India, financing another's litigation for a share of proceeds (champerty) is NOT per se illegal unless it is extortionate, unconscionable, or prompted by improper gambling motives (<em>Ram Coomar Coondoo v. Chunder Canto Mookerjee, 1876 PC</em>).</li>\n  <li><strong>Trafficking in Public Offices:</strong> Buying or selling public appointments or judicial honours.</li>\n  <li><strong>Agreements Creating Monopolies or Restricting Parentage.</strong></li>\n</ul>\n",
    "quickRevisionPoints": [
      "Section 23: 5 heads — Forbidden by law, defeats law, fraudulent, injury to person/property, immoral/opposed to public policy.",
      "Every agreement of which the object or consideration is unlawful is void.",
      "Public policy is 'an unruly horse' (Richardson v. Mellish).",
      "Stifling prosecution of non-compoundable offenses is void.",
      "Champerty is NOT per se illegal in India unless extortionate (Ram Coomar Coondoo).",
      "Sale of public offices or titles is contrary to public policy."
    ],
    "provisions": [
      {
        "provision": "Section 23, ICA 1872",
        "title": "What Considerations and Objects are Lawful, and What Not",
        "description": "The consideration or object of an agreement is lawful, unless: it is forbidden by law; defeats provisions of law; fraudulent; involves injury to person or property; or is immoral or opposed to public policy."
      }
    ],
    "definitions": [
      {
        "term": "Champerty",
        "definition": "An agreement whereby a stranger assists a litigant in a suit in exchange for a share of the proceeds of litigation."
      }
    ],
    "ingredients": [
      "Unlawful character of either consideration or ultimate object.",
      "Direct violation of statutory prohibition or policy.",
      "Direct voidness under Section 23."
    ],
    "exceptions": [
      "Severable lawful parts of a contract may survive if separable from illegal parts (Section 24)."
    ],
    "examples": [
      {
        "scenario": "A promises to pay B Rs. 1 lakh if B secures him a government gazetted post using political connections.",
        "application": "The agreement is void under Section 23 as trafficking in public offices, which is opposed to public policy."
      }
    ],
    "landmarkCases": [
      {
        "case": "Ram Coomar Coondoo v. Chunder Canto Mookerjee",
        "citation": "(1876) LR 4 IA 23",
        "year": "1876",
        "bench": "Privy Council (Sir Montague Smith)",
        "ratio": "The English common law doctrines of maintenance and champerty do not apply in full rigour to India. An agreement to supply funds to carry on litigation in consideration of having a share of property is not void unless it is extortionate or unconscionable.",
        "impact": "Leading authority settling the legality of litigation funding and champerty in India."
      },
      {
        "case": "Central Inland Water Transport Corp. v. Brojo Nath Ganguly",
        "citation": "(1986) 3 SCC 156",
        "year": "1986",
        "bench": "Supreme Court of India (Madon J)",
        "ratio": "An unconscionable clause in an employment contract allowing termination on 3 months' notice without inquiry was struck down as opposed to public policy under Section 23, affirming the expanding modern scope of public policy in protecting weaker parties.",
        "impact": "Monumental Indian constitutional precedent applying Section 23 to standard form contracts."
      }
    ],
    "comparisonTables": [
      {
        "title": "Forbidden by Law vs Defeats Provisions of Law",
        "headers": [
          "Head",
          "Nature of Prohibition",
          "Example"
        ],
        "rows": [
          [
            "Forbidden by Law",
            "Direct express legislative ban with penalties",
            "Contract to smuggle gold; contract to pay bribe"
          ],
          [
            "Defeats Provisions of Law",
            "Indirect circumvention of statutory policy",
            "Agreement to waive statutory limitation period"
          ]
        ]
      }
    ],
    "diagramId": "diag-cnt-void-agreements",
    "diagramExplanation": "Custom vector schematic showing the 5 heads of illegality under Section 23.",
    "misconceptions": [
      {
        "myth": "All litigation funding agreements (champerty) are illegal in India.",
        "reality": "Unlike English common law, champerty is valid in India unless it is extortionate, fraudulent, or against public policy."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Confusing compoundable criminal offenses with non-compoundable offenses.",
        "reality": "Settling compoundable offenses (like simple hurt) is lawful; settling non-compoundable offenses (like robbery) is void for stifling prosecution.",
        "rule": "Stifling non-compoundable crime = Void."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-06-01",
        "front": "What are the 5 heads under Section 23 that make consideration or object unlawful?",
        "back": "Forbidden by law, defeats provisions of law, fraudulent, involves injury to person/property, and immoral or opposed to public policy.",
        "category": "Section 23"
      },
      {
        "id": "fc-cnt-06-02",
        "front": "Is Champerty per se illegal in India?",
        "back": "No, the Privy Council held in Ram Coomar Coondoo (1876) that champerty is valid unless extortionate or unconscionable.",
        "category": "Champerty"
      },
      {
        "id": "fc-cnt-06-03",
        "front": "What judge famously called public policy 'an unruly horse'?",
        "back": "Burrough J in Richardson v. Mellish (1824).",
        "category": "Judicial Quotes"
      },
      {
        "id": "fc-cnt-06-04",
        "front": "What did the Supreme Court hold in Brojo Nath Ganguly (1986) under Section 23?",
        "back": "Grossly unequal and unconscionable standard contract terms are void as opposed to public policy.",
        "category": "Landmark Precedents"
      }
    ],
    "sourceReferences": [
      {
        "title": "Indian Contract Act, 1872",
        "url": "https://indiacode.nic.in"
      }
    ]
  },
  "top-cnt-06-02": {
    "topicId": "top-cnt-06-02",
    "chapterId": "ch-cnt-06",
    "subjectId": "law-contract",
    "title": "Specific Void Agreements: Restraint of Trade, Marriage & Wagering (Sections 26–30)",
    "subtitle": "Statutory Prohibitions on Restraints and Speculative Wagers",
    "bareActRef": "Indian Contract Act, 1872 — Sections 26, 27, 28, 29, 30",
    "learningObjective": "Master the specific void agreements: Restraint of Marriage (s. 26), Restraint of Trade (s. 27), Restraint of Legal Proceedings (s. 28), Uncertainty (s. 29), and Wagering (s. 30).",
    "detailedExplanation": "\n<h3>1. Restraint of Marriage: Section 26</h3>\n<p>'Every agreement in restraint of the marriage of any person, other than a minor, is void.' Restraints may be total or partial; all are void (except regarding minors).</p>\n\n<h3>2. Restraint of Trade: Section 27</h3>\n<p>'Every agreement by which any one is restrained from exercising a lawful profession, trade or business of any kind, is to that extent void.'</p>\n<ul>\n  <li>Unlike English law (which allows 'reasonable' restraints under Nordenfelt), <strong>Indian law makes ALL restraints of trade void</strong>, whether total or partial, reasonable or unreasonable (<em>Madhub Chunder v. Rajcoomar Dass, 1874</em>).</li>\n  <li><strong>Single Statutory Exception:</strong> Sale of Goodwill of a business. A seller may agree with the buyer to refrain from carrying on a similar business within specified local limits, provided the limits appear reasonable to the court.</li>\n  <li><strong>Employment Contracts:</strong> Negative covenants operating <em>during</em> the term of employment are valid (e.g., employee will not work for a rival while employed) (<em>Niranjan Shankar Golikari v. Century Spg & Mfg Co.</em>). But post-employment negative covenants are strictly void (<em>Superintendence Co. of India v. Krishan Murgai</em>).</li>\n</ul>\n\n<h3>3. Restraint of Legal Proceedings: Section 28</h3>\n<p>Every agreement restricting a party absolutely from enforcing rights in court, or limiting the time within which he may enforce rights, is void.</p>\n<ul>\n  <li><strong>Exceptions:</strong> Arbitration agreements (submitting present or future disputes to arbitration) are fully valid (Exceptions 1 and 2).</li>\n</ul>\n\n<h3>4. Wagering Agreements: Section 30</h3>\n<p>An agreement by way of wager is void, and no suit can be brought to recover anything alleged to be won upon any wager. A wager is a promise to pay money upon the determination of an uncertain event where neither party has any interest other than the stake (<em>Carlill</em>).</p>\n<ul>\n  <li><strong>Exception:</strong> Horse racing prizes of value of Rs. 500 or upwards.</li>\n  <li><strong>Collateral Transactions:</strong> In India (outside Maharashtra and Gujarat), collateral transactions to a wagering agreement are NOT void, because wagering is void, not illegal. In Maharashtra and Gujarat, wagering is declared illegal by local amendment, tainting collaterals.</li>\n</ul>\n",
    "quickRevisionPoints": [
      "Section 26: Restraint of marriage of any person (other than minor) is void.",
      "Section 27: All restraints of trade are void, reasonable or not (Madhub Chunder).",
      "Section 27 Exception: Sale of goodwill (reasonable geographic limits allowed).",
      "Post-employment negative covenants are strictly void (Krishan Murgai).",
      "Section 28: Restraint of legal proceedings is void; arbitration is a valid exception.",
      "Section 30: Wagering agreements are void; collateral transactions remain valid (outside MH/GJ)."
    ],
    "provisions": [
      {
        "provision": "Section 27, ICA 1872",
        "title": "Agreement in Restraint of Trade Void",
        "description": "Every agreement by which any one is restrained from exercising a lawful profession, trade or business of any kind, is to that extent void."
      },
      {
        "provision": "Section 30, ICA 1872",
        "title": "Agreements by Way of Wager Void",
        "description": "Agreements by way of wager are void; and no suit shall be brought for recovering anything alleged to be won on any wager."
      }
    ],
    "definitions": [
      {
        "term": "Wager",
        "definition": "A promise to give money upon the determination of an uncertain future event, where neither party has any interest except the winning or losing of the stake."
      }
    ],
    "ingredients": [
      "Statutory prohibition under Sections 26–30.",
      "Severability of the restraining clause.",
      "Distinction between void vs illegal status."
    ],
    "exceptions": [
      "Goodwill sale under Section 27; Arbitration under Section 28; Horse race prizes under Section 30."
    ],
    "examples": [
      {
        "scenario": "A sells the goodwill of his bakery to B for Rs. 5 lakhs, agreeing not to open a competing bakery within a 3-mile radius for 3 years.",
        "application": "The restraint is valid under the statutory exception to Section 27 as reasonable protection of goodwill."
      }
    ],
    "landmarkCases": [
      {
        "case": "Madhub Chunder v. Rajcoomar Dass",
        "citation": "(1874) 14 Beng LR 76",
        "year": "1874",
        "bench": "Calcutta High Court (Sir Richard Couch CJ)",
        "ratio": "Section 27 does not recognize the English test of reasonableness; any agreement restraining a person from exercising a lawful trade, even partial or reasonable, is void.",
        "impact": "Landmark ruling establishing the absolute prohibition on restraints of trade in India."
      },
      {
        "case": "Niranjan Shankar Golikari v. Century Spg. & Mfg. Co.",
        "citation": "AIR 1967 SC 1098",
        "year": "1967",
        "bench": "Supreme Court of India (Shelat J)",
        "ratio": "A negative covenant operating during the period of employment prohibiting an employee from serving elsewhere is not in restraint of trade under Section 27.",
        "impact": "Classic authority upholding exclusivity clauses during active employment."
      }
    ],
    "comparisonTables": [
      {
        "title": "Restraint of Trade: Indian Law vs English Law",
        "headers": [
          "Aspect",
          "Indian Law (Section 27)",
          "English Law (Nordenfelt Rule)"
        ],
        "rows": [
          [
            "General Rule",
            "All restraints are void ab initio",
            "Restraints are prima facie void unless reasonable"
          ],
          [
            "Test of Reasonableness",
            "Inapplicable (except for sale of goodwill)",
            "Universal test: reasonable between parties & public interest"
          ],
          [
            "Statutory Exceptions",
            "Only sale of goodwill (and partnership law)",
            "Common law public interest test"
          ]
        ]
      }
    ],
    "diagramId": "diag-cnt-void-agreements",
    "diagramExplanation": "Custom vector schematic showing Sections 26 to 30 void categories and their statutory exceptions.",
    "misconceptions": [
      {
        "myth": "An insurance contract is a wagering agreement because payment depends on an uncertain future fire or death.",
        "reality": "Insurance requires 'insurable interest' in property or life; wager has zero interest other than the stake."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing collateral transactions to a wager are void in all of India.",
        "reality": "In India (except Maharashtra and Gujarat), wagering is void, NOT illegal; therefore, collateral transactions (e.g. loans to pay wager) are enforceable.",
        "rule": "Wager collateral = Enforceable (General India); Void (MH/GJ)."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-06-05",
        "front": "What does Section 27 of the Indian Contract Act lay down regarding restraint of trade?",
        "back": "Every agreement restraining someone from exercising a lawful profession, trade, or business is void to that extent.",
        "category": "Restraint of Trade"
      },
      {
        "id": "fc-cnt-06-06",
        "front": "What is the only statutory exception to Section 27 (restraint of trade)?",
        "back": "Sale of the goodwill of a business (subject to reasonable local limits).",
        "category": "Goodwill Exception"
      },
      {
        "id": "fc-cnt-06-07",
        "front": "What did the Supreme Court hold in Niranjan Shankar Golikari regarding employment covenants?",
        "back": "Negative covenants operating DURING the period of employment are valid and not in restraint of trade.",
        "category": "Employment Covenants"
      },
      {
        "id": "fc-cnt-06-08",
        "front": "Are agreements by way of wager void or illegal under Section 30?",
        "back": "They are VOID under Section 30; collateral contracts remain valid (except in Maharashtra/Gujarat).",
        "category": "Wagering Agreements"
      }
    ],
    "sourceReferences": [
      {
        "title": "Indian Contract Act, 1872",
        "url": "https://indiacode.nic.in"
      }
    ]
  },
  "top-cnt-07-01": {
    "topicId": "top-cnt-07-01",
    "chapterId": "ch-cnt-07",
    "subjectId": "law-contract",
    "title": "Contingent Contracts: Meaning, Rules & Enforcement (Sections 31–36)",
    "subtitle": "Contracts Conditional on Uncertain Collateral Future Events",
    "bareActRef": "Indian Contract Act, 1872 — Sections 31, 32, 33, 34, 35, 36",
    "learningObjective": "Master Section 31 contingent contracts, compare with wagering agreements, and memorize enforcement rules under Sections 32 to 36.",
    "detailedExplanation": "\n<h3>1. Statutory Definition: Section 31</h3>\n<p>'A contingent contract is a contract to do or not to do something, if some event, collateral to such contract, does or does not happen.'</p>\n<ul>\n  <li><strong>Performance Depends on Future Event:</strong> The event must be uncertain.</li>\n  <li><strong>Collateral to Contract:</strong> The event must be independent of the promise itself (e.g., arrival of a ship, destruction by fire, marriage of a person).</li>\n  <li><strong>Contract of Insurance:</strong> Classic example of a contingent contract (e.g., insurer promises to pay if house burns down).</li>\n</ul>\n\n<h3>2. The Rules of Enforcement (Sections 32–36)</h3>\n<ol>\n  <li><strong>Happening of Uncertain Event (Section 32):</strong> Enforceable only when the event happens. If the event becomes impossible, the contract becomes <strong>void</strong>.</li>\n  <li><strong>Non-Happening of Uncertain Event (Section 33):</strong> Enforceable when the happening becomes impossible, and not before.</li>\n  <li><strong>Event Deemed Impossible by Conduct of Living Person (Section 34):</strong> If the event is how a person will act at an unspecified time, it is deemed impossible when that person does something which renders it impossible within any definite period (e.g., A agrees to pay B if B marries C; C marries D; event is deemed impossible).</li>\n  <li><strong>Contingent on Event Happening Within Fixed Time (Section 35):</strong> Becomes void if event does not happen within fixed time, or becomes impossible before time expires.</li>\n  <li><strong>Contingent on Impossible Events (Section 36):</strong> Agreements contingent on impossible events are <strong>void ab initio</strong>, whether the impossibility was known to parties or not (e.g., A agrees to pay B if two straight lines enclose a space).</li>\n</ol>\n",
    "quickRevisionPoints": [
      "Section 31: Contract to do/not do something if a collateral event happens or does not happen.",
      "Insurance contracts are valid contingent contracts.",
      "Section 32: Contingent on happening -> Enforceable when happens; void if impossible.",
      "Section 33: Contingent on non-happening -> Enforceable when happening becomes impossible.",
      "Section 34: Conduct of living person making event impossible.",
      "Section 36: Contingent on impossible events is VOID ab initio."
    ],
    "provisions": [
      {
        "provision": "Section 31, ICA 1872",
        "title": "Contingent Contract Defined",
        "description": "A contingent contract is a contract to do or not to do something, if some event, collateral to such contract, does or does not happen."
      },
      {
        "provision": "Section 36, ICA 1872",
        "title": "Agreements Contingent on Impossible Events Void",
        "description": "Agreements contingent upon the happening of an impossible event are void, whether the impossibility of the event was known or not to the parties to the agreement at the time when it was made."
      }
    ],
    "definitions": [
      {
        "term": "Collateral Event",
        "definition": "An independent, incidental future occurrence that is neither the performance nor the consideration of the contract."
      }
    ],
    "ingredients": [
      "Valid underlying agreement.",
      "Conditionality on collateral event.",
      "Uncertainty of future occurrence."
    ],
    "exceptions": [
      "Agreements contingent on impossible events are void ab initio (Section 36)."
    ],
    "examples": [
      {
        "scenario": "A contracts to pay B Rs. 10,000 if B's ship does not return. The ship is sunk in a storm.",
        "application": "Under Section 33, when the return becomes impossible, the contract can be enforced by B."
      }
    ],
    "landmarkCases": [
      {
        "case": "Chandulal Harjivandas v. CIT",
        "citation": "AIR 1967 SC 1262",
        "year": "1967",
        "bench": "Supreme Court of India",
        "ratio": "A life insurance contract was analyzed as a classic contingent contract where liability to pay matures upon the happening of death or maturity.",
        "impact": "Affirmed the character of insurance policies as contingent contracts under Section 31."
      }
    ],
    "comparisonTables": [
      {
        "title": "Contingent Contract vs Wagering Agreement",
        "headers": [
          "Aspect",
          "Contingent Contract (s. 31)",
          "Wagering Agreement (s. 30)"
        ],
        "rows": [
          [
            "Validity",
            "Completely VALID and enforceable",
            "VOID by statute"
          ],
          [
            "Interest in Event",
            "Parties have substantive insurable/commercial interest",
            "Parties have NO interest except winning the stake"
          ],
          [
            "Role of Event",
            "Collateral to main contract",
            "Sole determining factor and core of wager"
          ]
        ]
      }
    ],
    "diagramId": "diag-cnt-validity-consent",
    "diagramExplanation": "Custom vector schematic illustrating Section 32 to 36 enforcement pathways.",
    "misconceptions": [
      {
        "myth": "A contract contingent on an impossible event is voidable if the promisor was ignorant of the impossibility.",
        "reality": "Under Section 36, it is void ab initio, whether the impossibility was known or unknown."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Confusing Section 32 (happening) with Section 33 (non-happening).",
        "reality": "Section 32 becomes enforceable when event HAPPENS; Section 33 becomes enforceable when event BECOMES IMPOSSIBLE.",
        "rule": "Happening = 32; Non-happening = 33."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-07-01",
        "front": "Which section of the Contract Act defines a 'Contingent Contract'?",
        "back": "Section 31.",
        "category": "Contingent Contracts"
      },
      {
        "id": "fc-cnt-07-02",
        "front": "When does a contract contingent on the HAPPENING of an event become void under Section 32?",
        "back": "When the happening of the event becomes impossible.",
        "category": "Section 32"
      },
      {
        "id": "fc-cnt-07-03",
        "front": "What is the status of an agreement contingent on an impossible event under Section 36?",
        "back": "Void ab initio, whether the impossibility was known to the parties or not.",
        "category": "Section 36"
      },
      {
        "id": "fc-cnt-07-04",
        "front": "What is the key distinction between a contingent contract and a wagering agreement?",
        "back": "In a contingent contract, parties have a real collateral interest (valid); in a wager, there is no interest except the stake (void).",
        "category": "Contingent vs Wager"
      }
    ],
    "sourceReferences": [
      {
        "title": "Indian Contract Act, 1872",
        "url": "https://indiacode.nic.in"
      }
    ]
  },
  "top-cnt-07-02": {
    "topicId": "top-cnt-07-02",
    "chapterId": "ch-cnt-07",
    "subjectId": "law-contract",
    "title": "Quasi-Contracts & Doctrine of Unjust Enrichment (Sections 68–72)",
    "subtitle": "Certain Relations Resembling Those Created by Contract",
    "bareActRef": "Indian Contract Act, 1872 — Sections 68, 69, 70, 71, 72",
    "learningObjective": "Master Chapter V of ICA on Quasi-Contracts: Sections 68 (necessaries), 69 (payment by interested person), 70 (non-gratuitous acts), 71 (finder of goods), and 72 (mistake/coercion).",
    "detailedExplanation": "\n<h3>1. Nature of Quasi-Contracts: Chapter V ICA</h3>\n<p>Chapter V is titled <em>'Of Certain Relations Resembling Those Created by Contract'</em>. Quasi-contracts are not actual contracts; there is no offer, acceptance, or consensus. They are obligations created by law based on Lord Mansfield's equitable principle in <em>Moses v. Macferlan (1760)</em>: <strong>Nemo debet locupletari ex aliena jactura</strong> (No one should be unjustly enriched at another's expense).</p>\n\n<h3>2. The Five Statutory Heads of Quasi-Contract</h3>\n<ol>\n  <li><strong>Section 68 — Necessaries Supplied to Incapable Persons:</strong> Reimbursement from the property of a minor or lunatic for necessaries suited to his condition in life.</li>\n  <li><strong>Section 69 — Reimbursement of Person Paying Money Due by Another:</strong> A person who is interested in the payment of money which another is bound by law to pay, and who therefore pays it, is entitled to be reimbursed by the other (e.g., sub-tenant pays municipal taxes to prevent auction of property).</li>\n  <li><strong>Section 70 — Obligation of Person Enjoying Benefit of Non-Gratuitous Act:</strong> Where a person lawfully does anything for another, or delivers anything to him, not intending to do so gratuitously, and such other person enjoys the benefit thereof, the latter is bound to make compensation (e.g., government receives goods under informal order and consumes them; <em>State of West Bengal v. B.K. Mondal & Sons</em>).</li>\n  <li><strong>Section 71 — Responsibility of Finder of Goods:</strong> A person who finds goods belonging to another and takes them into custody is subject to the same responsibility as a <strong>Bailee</strong> (must take reasonable care under Section 151 and return to owner).</li>\n  <li><strong>Section 72 — Money Paid by Mistake or Under Coercion:</strong> A person to whom money has been paid, or anything delivered, by mistake or under coercion, must repay or return it (<em>Sales Tax Officer, Banaras v. Kanhaiya Lal Saraf</em>).</li>\n</ol>\n",
    "quickRevisionPoints": [
      "Quasi-contracts rest on unjust enrichment (Nemo debet locupletari ex aliena jactura; Moses v. Macferlan).",
      "Section 68: Necessaries to minors -> against property only.",
      "Section 69: Interested person pays debt bound by law -> entitled to reimbursement.",
      "Section 70: Non-gratuitous lawful act -> benefit enjoyed -> bound to compensate (B.K. Mondal).",
      "Section 71: Finder of goods has the duties and liability of a BAILEE.",
      "Section 72: Money paid under mistake (fact or law) or coercion must be returned (Kanhaiya Lal Saraf)."
    ],
    "provisions": [
      {
        "provision": "Section 69, ICA 1872",
        "title": "Reimbursement of Person Paying Money Due by Another",
        "description": "A person who is interested in the payment of money which another is bound by law to pay, and who therefore pays it, is entitled to be reimbursed by the other."
      },
      {
        "provision": "Section 70, ICA 1872",
        "title": "Obligation of Person Enjoying Benefit of Non-Gratuitous Act",
        "description": "Where a person lawfully does anything for another person, not intending to do so gratuitously, and such other person enjoys the benefit thereof, the latter is bound to make compensation."
      }
    ],
    "definitions": [
      {
        "term": "Unjust Enrichment",
        "definition": "The retention of a benefit or money conferred by another which in justice and equity belongs to that other person."
      }
    ],
    "ingredients": [
      "Absence of express contract.",
      "Conferment of lawful non-gratuitous benefit.",
      "Enjoyment of benefit by defendant."
    ],
    "exceptions": [
      "Gratuitous acts or intermeddling by officious volunteers creates no claim under Section 70."
    ],
    "examples": [
      {
        "scenario": "A tradesman leaves goods at B's house by mistake. B treats the goods as his own and consumes them.",
        "application": "Under Section 70, B is bound to pay A for the goods because he enjoyed the benefit of a non-gratuitous delivery."
      }
    ],
    "landmarkCases": [
      {
        "case": "State of West Bengal v. B.K. Mondal & Sons",
        "citation": "AIR 1962 SC 779",
        "year": "1962",
        "bench": "5-Judge Constitution Bench (Gajendragadkar J)",
        "ratio": "Where a contractor constructed buildings for the state without complying with formal government contract requirements under Article 299 of the Constitution, but the State enjoyed the benefit of the buildings, held: Section 70 applied and the State was bound to pay compensation.",
        "impact": "Monumental ruling applying Section 70 quasi-contract against the State."
      },
      {
        "case": "Sales Tax Officer, Banaras v. Kanhaiya Lal Saraf",
        "citation": "AIR 1959 SC 135",
        "year": "1959",
        "bench": "Supreme Court of India (Bhagwati J)",
        "ratio": "Money paid under mistake of law (tax paid under an unconstitutional sales tax assessment) is recoverable under Section 72, which covers both mistakes of fact and mistakes of law.",
        "impact": "Landmark authority establishing that tax paid under mistake of law is refundable under Section 72."
      }
    ],
    "comparisonTables": [
      {
        "title": "The 5 Quasi-Contract Sections Compared",
        "headers": [
          "Section",
          "Core Subject",
          "Legal Test",
          "Recipient Liability"
        ],
        "rows": [
          [
            "Section 68",
            "Incompetent person necessaries",
            "Suited to station in life",
            "From property only"
          ],
          [
            "Section 69",
            "Interested person payment",
            "Bound by law to pay",
            "Reimbursement of exact sum"
          ],
          [
            "Section 70",
            "Non-gratuitous lawful acts",
            "Lawful + non-gratuitous + benefit enjoyed",
            "Fair compensation or return"
          ],
          [
            "Section 71",
            "Finder of lost goods",
            "Takes goods into custody",
            "Bailee duties (reasonable care)"
          ],
          [
            "Section 72",
            "Mistake or coercion",
            "Payment made under mistake/coercion",
            "Full restitution / refund"
          ]
        ]
      }
    ],
    "diagramId": "diag-cnt-validity-consent",
    "diagramExplanation": "Custom vector schematic displaying Chapter V quasi-contractual remedies.",
    "misconceptions": [
      {
        "myth": "A finder of lost goods becomes the absolute owner immediately upon finding.",
        "reality": "Under Section 71, the finder is subject to the duties of a bailee and must make reasonable efforts to trace the true owner."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing Section 72 applies only to mistakes of fact.",
        "reality": "The Supreme Court in Kanhaiya Lal Saraf settled that Section 72 applies equally to mistakes of FACT and mistakes of LAW.",
        "rule": "Section 72 covers mistake of law and fact."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-07-05",
        "front": "What equitable doctrine forms the foundation of Chapter V Quasi-Contracts?",
        "back": "Doctrine of Unjust Enrichment (Nemo debet locupletari ex aliena jactura).",
        "category": "Quasi-Contracts"
      },
      {
        "id": "fc-cnt-07-06",
        "front": "What are the three essentials to claim compensation under Section 70?",
        "back": "Act done lawfully, not intended to be done gratuitously, and the other person enjoyed the benefit.",
        "category": "Section 70"
      },
      {
        "id": "fc-cnt-07-07",
        "front": "What is the legal status and responsibility of a finder of goods under Section 71?",
        "back": "He is subject to the same responsibility as a Bailee.",
        "category": "Section 71"
      },
      {
        "id": "fc-cnt-07-08",
        "front": "What was held in Sales Tax Officer v. Kanhaiya Lal Saraf (1959) regarding Section 72?",
        "back": "Money paid under mistake of law is recoverable under Section 72.",
        "category": "Section 72 Precedents"
      }
    ],
    "sourceReferences": [
      {
        "title": "Indian Contract Act, 1872",
        "url": "https://indiacode.nic.in"
      }
    ]
  }
};

  global.CONTRACT_CONCEPTS_PART2 = DATA;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = DATA;
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
