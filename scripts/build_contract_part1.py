import json
from concept_helpers import create_concept_file

data = {}

# -------------------------------------------------------------
# CHAPTER 1: FORMATION OF CONTRACT
# -------------------------------------------------------------
data["top-cnt-01-01"] = {
    "topicId": "top-cnt-01-01",
    "chapterId": "ch-cnt-01",
    "subjectId": "law-contract",
    "title": "Agreement and Contract (Section 2(h) & Section 10 Essentials)",
    "subtitle": "The Genesis of Contractual Obligation: Every Contract is an Agreement, but Not Every Agreement is a Contract",
    "bareActRef": "Indian Contract Act, 1872 — Sections 2(e), 2(h), 10",
    "learningObjective": "Master the statutory definition of contract under Section 2(h), analyze the essential ingredients of a valid contract under Section 10, and distinguish void, voidable, and illegal agreements.",
    "introduction": "The Indian Contract Act, 1872 defines a contract under Section 2(h) as 'an agreement enforceable by law'. A contract is born when an agreement satisfies the rigorous requirements of legal enforceability codified in Section 10.",
    "detailedExplanation": """
<h3>1. The Statutory Equation: Agreement + Legal Enforceability = Contract</h3>
<ul>
  <li><strong>Section 2(e) — Agreement:</strong> 'Every promise and every set of promises, forming the consideration for each other, is an agreement.'</li>
  <li><strong>Section 2(h) — Contract:</strong> 'An agreement enforceable by law is a contract.'</li>
  <li><strong>The Axiom:</strong> 'All contracts are agreements, but all agreements are not contracts.' An agreement of a purely social, domestic, moral, or religious nature lacks the intention to create legal relations and hence is not enforceable as a contract.</li>
</ul>

<h3>2. The Pillar of Enforceability: Section 10 Essentials</h3>
<p>Section 10 lays down that all agreements are contracts if they are made:</p>
<ol>
  <li><strong>By the Free Consent of Parties:</strong> Not caused by coercion, undue influence, fraud, misrepresentation, or bilateral mistake (Sections 13–22).</li>
  <li><strong>Competent to Contract:</strong> Parties must be of the age of majority, of sound mind, and not disqualified by law (Sections 11–12).</li>
  <li><strong>For a Lawful Consideration:</strong> Quid pro quo that is not unlawful under Section 23.</li>
  <li><strong>With a Lawful Object:</strong> The purpose must not be forbidden by law, defeat the provisions of any law, fraudulent, injurious to person/property, or immoral/opposed to public policy (Section 23).</li>
  <li><strong>Not Expressly Declared to be Void:</strong> Must not fall within the specific prohibitions of Sections 24–30 (e.g., restraint of marriage, trade, legal proceedings, or wagering).</li>
  <li><strong>Compliance with Legal Formalities:</strong> Written or registered where required by specific statutory provisions (e.g., Section 25(1) natural love and affection, or Section 17 Registration Act 1908).</li>
</ol>
""",
    "quickRevisionPoints": [
      "Section 2(h): An agreement enforceable by law is a contract.",
      "Section 2(e): Every promise forming consideration for each other is an agreement.",
      "Section 10: Free consent, competent parties, lawful consideration, lawful object, not expressly declared void.",
      "Void Agreement (s. 2(g)): Void ab initio; creates zero legal rights (quod ab initio non valet in tractu temporis non convalescit).",
      "Voidable Contract (s. 2(i)): Enforceable at the option of one party, not at the option of the other.",
      "All contracts are agreements, but all agreements are not contracts."
    ],
    "provisions": [
      {
        "provision": "Section 10, Indian Contract Act 1872",
        "title": "What Agreements are Contracts",
        "description": "All agreements are contracts if they are made by the free consent of parties competent to contract, for a lawful consideration and with a lawful object, and are not hereby expressly declared to be void."
      }
    ],
    "definitions": [
      {
        "term": "Void Agreement (Section 2(g))",
        "definition": "An agreement not enforceable by law is said to be void (void ab initio)."
      },
      {
        "term": "Voidable Contract (Section 2(i))",
        "definition": "An agreement which is enforceable by law at the option of one or more of the parties thereto, but not at the option of the other or others."
      }
    ],
    "ingredients": [
      "Plurality of parties (promisor and promisee).",
      "Consensus ad idem (meeting of minds).",
      "Free consent under Section 14.",
      "Capacity under Section 11.",
      "Lawful consideration and object under Section 23.",
      "Absence of statutory voidness under Sections 24–30."
    ],
    "exceptions": [
      "Social and domestic agreements are presumed to lack intention to enter into legal relations (Balfour v. Balfour)."
    ],
    "examples": [
      {
        "scenario": "A invites B to dinner at his house. B accepts the invitation, but A fails to serve dinner.",
        "application": "B cannot sue A because social domestic agreements lack intention to create legal relations; it is an agreement but not a contract."
      }
    ],
    "landmarkCases": [
      {
        "case": "Balfour v. Balfour",
        "citation": "(1919) 2 KB 571",
        "year": "1919",
        "bench": "Court of Appeal (Atkin LJ)",
        "ratio": "Agreements between husband and wife for living allowances are ordinary domestic arrangements and not contracts because parties did not intend that they should be attended by legal consequences.",
        "impact": "Established the universal common law requirement of intention to create legal relations."
      }
    ],
    "comparisonTables": [
      {
        "title": "Void Agreement vs Voidable Contract",
        "headers": ["Aspect", "Void Agreement (s. 2(g))", "Voidable Contract (s. 2(i))"],
        "rows": [
          ["Enforceability", "Enforceable by neither party from the inception (void ab initio)", "Enforceable at the option of the aggrieved party"],
          ["Cause", "Lack of capacity, illegal object, restraint of trade/marriage", "Vitiated consent (coercion, undue influence, fraud, misrepresentation)"],
          ["Restitution", "Section 65 applies if discovered void; no restoration for illegal", "Section 64 applies: benefits received must be restored on rescission"],
          ["Effect of Delay", "Cannot be validated by lapse of time or ratification", "Becomes binding if not avoided within reasonable time"]
        ]
      }
    ],
    "diagramId": "diag-cnt-agreement-vs-contract",
    "diagramExplanation": "Custom vector schematic illustrating the transformation of an offer and acceptance into an agreement, and the addition of Section 10 tests to create a binding contract.",
    "misconceptions": [
      {
        "myth": "A void contract and a void agreement mean the exact same thing.",
        "reality": "A void agreement (s. 2(g)) was never a contract at all (void ab initio). A void contract (s. 2(j)) was initially valid, but subsequently ceased to be enforceable due to supervening impossibility or law."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing Section 10 requires writing and registration for all contracts.",
        "reality": "Section 10 requires writing/registration ONLY when expressly required by any other specific statute in force in India.",
        "rule": "Oral contracts are completely valid unless a specific statute prescribes writing."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-01-01",
        "front": "Which section of the Indian Contract Act defines 'Contract'?",
        "back": "Section 2(h) — 'An agreement enforceable by law is a contract.'",
        "category": "Statutory Definitions"
      },
      {
        "id": "fc-cnt-01-02",
        "front": "What are the core essentials of a contract specified in Section 10?",
        "back": "Free consent, competency of parties, lawful consideration, lawful object, and not expressly declared void.",
        "category": "Section 10"
      },
      {
        "id": "fc-cnt-01-03",
        "front": "What is the definition of a 'Voidable Contract' under Section 2(i)?",
        "back": "An agreement enforceable by law at the option of one or more parties, but not at the option of the other or others.",
        "category": "Statutory Definitions"
      },
      {
        "id": "fc-cnt-01-04",
        "front": "What Latin maxim expresses that what is void from the beginning cannot become valid through time?",
        "back": "'Quod ab initio non valet in tractu temporis non convalescit'.",
        "category": "Legal Maxims"
      }
    ],
    "sourceReferences": [
      {"title": "Pollock & Mulla: The Indian Contract Act — 16th Ed.", "url": "https://archive.org"},
      {"title": "Law of Contract — Dr. R.K. Bangia", "url": "https://archive.org"}
    ]
}

data["top-cnt-01-02"] = {
    "topicId": "top-cnt-01-02",
    "chapterId": "ch-cnt-01",
    "subjectId": "law-contract",
    "title": "Offer / Proposal: Essentials & Offer vs Invitation to Treat",
    "subtitle": "The First Step in Contract Formation: Definite Intention vs Invitation to Bargain",
    "bareActRef": "Indian Contract Act, 1872 — Sections 2(a), 8",
    "learningObjective": "Master the statutory definition of proposal under Section 2(a), distinguish an offer from an invitation to offer/treat, and analyze general vs specific offers.",
    "detailedExplanation": """
<h3>1. Statutory Definition: Section 2(a)</h3>
<p>'When one person signifies to another his willingness to do or to abstain from doing anything, with a view to obtaining the assent of that other to such act or abstinence, he is said to make a proposal.'</p>
<ul>
  <li><strong>Signification:</strong> The offer must be communicated; an unexpressed thought is not an offer.</li>
  <li><strong>Willingness to do or abstain:</strong> Can be positive or negative.</li>
  <li><strong>With a view to obtaining assent:</strong> Made with the purpose of binding oneself upon the other's acceptance.</li>
</ul>

<h3>2. Offer vs. Invitation to Treat (Invitation to Offer)</h3>
<p>An offer is the final expression of willingness to be bound by contract upon acceptance. An <strong>Invitation to Treat</strong> is merely an invitation to negotiate or solicit offers from others. The person issuing the invitation does not intend to be bound immediately upon acceptance.</p>
<ul>
  <li><strong>Display of Goods in a Shop or Supermarket:</strong> Mere invitation to treat. When the customer picks goods and brings them to the cash counter, the customer makes the offer; the cashier accepts (<em>Pharmaceutical Society of Great Britain v. Boots Cash Chemists</em>).</li>
  <li><strong>Catalogues, Price Lists, Quotations:</strong> Merely invitations to treat (<em>Harvey v. Facey</em>).</li>
  <li><strong>Advertisements for Tender or Auction:</strong> Mere invitation to receive bids or offers.</li>
</ul>

<h3>3. General Offer vs. Specific Offer</h3>
<ul>
  <li><strong>Specific Offer:</strong> Made to a definite person or group; can be accepted only by that specific person (<em>Boulton v. Jones</em>).</li>
  <li><strong>General Offer:</strong> Made to the world at large (<em>contra mundum</em>). Can be accepted by anyone who performs the conditions specified in the advertisement without prior notice of acceptance (Section 8, ICA; <em>Carlill v. Carbolic Smoke Ball Co.</em>).</li>
</ul>

<h3>4. Communication of Offer is Essential</h3>
<p>An offer cannot be accepted in ignorance of its existence. In <em>Lalman Shukla v. Gauri Datt (1913)</em>, a servant traced his master's missing nephew without knowing of an advertised reward. Held: No contract existed, because there can be no acceptance without knowledge of the offer.</p>
""",
    "quickRevisionPoints": [
      "Section 2(a): Proposal is signifying willingness to do/abstain with a view to obtaining assent.",
      "Invitation to Treat = Inviting others to make an offer (catalogues, shop displays, tenders, price quotes).",
      "Harvey v. Facey (1893): Stating lowest cash price for Bumper Hall Pen was an invitation to treat, not an offer.",
      "General Offer: Made to world at large; accepted by performing condition (s. 8; Carlill v. Carbolic Smoke Ball Co.).",
      "Specific Offer: Made to a definite person; can be accepted only by that person (Boulton v. Jones).",
      "Lalman Shukla v. Gauri Datt (1913): Acceptance in ignorance of offer is void; no contract."
    ],
    "provisions": [
      {
        "provision": "Section 2(a), Indian Contract Act 1872",
        "title": "Definition of Proposal",
        "description": "When one person signifies to another his willingness to do or to abstain from doing anything, with a view to obtaining the assent of that other to such act or abstinence, he is said to make a proposal."
      },
      {
        "provision": "Section 8, Indian Contract Act 1872",
        "title": "Acceptance by Performing Conditions",
        "description": "Performance of the conditions of a proposal, or the acceptance of any consideration for a reciprocal promise which may be offered with a proposal, is an acceptance of the proposal."
      }
    ],
    "definitions": [
      {
        "term": "General Offer",
        "definition": "An offer addressed to the public at large which matures into a contract with any person who performs the stipulated conditions with knowledge of the offer."
      }
    ],
    "ingredients": [
      "Communication of intention to obtain assent.",
      "Definite and certain terms.",
      "Distinction from casual statements of intention or preliminary negotiations."
    ],
    "exceptions": [
      "Cross-offers made in ignorance of each other do not constitute a contract (Tinn v. Hoffmann)."
    ],
    "examples": [
      {
        "scenario": "A company advertises that anyone who uses their medical ball as directed and contracts influenza will receive £100 reward, depositing £1000 in a bank to show sincerity.",
        "application": "Under Carlill v. Carbolic Smoke Ball Co., this is a binding general offer. Mrs. Carlill used the ball, caught influenza, and was entitled to recover £100."
      }
    ],
    "landmarkCases": [
      {
        "case": "Carlill v. Carbolic Smoke Ball Co.",
        "citation": "(1893) 1 QB 256",
        "year": "1893",
        "bench": "Court of Appeal (Lindley, Bowen, and A.L. Smith LJJ)",
        "ratio": "A general offer made to the public at large can be accepted by performance of its conditions under Section 8 without formal notification of acceptance, and the deposit of money in bank proved serious intention to create legal relations.",
        "impact": "Classic authority on general offers, performance as acceptance, and advertisement contracts."
      },
      {
        "case": "Lalman Shukla v. Gauri Datt",
        "citation": "(1913) 11 ALJ 489",
        "year": "1913",
        "bench": "Allahabad High Court (Banerji J)",
        "ratio": "A servant who searched for and found his master's missing nephew in ignorance of an advertised reward was not entitled to the reward, because an offer cannot be accepted without prior knowledge and assent.",
        "impact": "Bedrock Indian precedent establishing that knowledge of proposal is indispensable for valid acceptance."
      },
      {
        "case": "Harvey v. Facey",
        "citation": "(1893) AC 552",
        "year": "1893",
        "bench": "Privy Council (Lord Morris)",
        "ratio": "Telegram asking 'Will you sell Bumper Hall Pen? Telegraph lowest cash price' received reply 'Lowest cash price £900'. Buyer telegraphed 'We agree to buy for £900'. Held: Mere quotation of price was an invitation to treat, not an offer to sell.",
        "impact": "Authoritative ruling distinguishing an offer from a statement of lowest minimum price."
      }
    ],
    "comparisonTables": [
      {
        "title": "Offer vs Invitation to Treat",
        "headers": ["Criterion", "Offer / Proposal", "Invitation to Treat"],
        "rows": [
          ["Nature", "Final willingness to enter contract upon acceptance", "Invitation to others to negotiate or make offers"],
          ["Effect of Assent", "Immediately forms a binding contract", "Results in an offer which may be accepted or rejected"],
          ["Intention", "Intention to be legally bound immediately", "Intention to solicit preliminary bids or quotations"],
          ["Examples", "Specific offer to sell car for Rs. 5 lakhs", "Price list, shop display, newspaper auction notice"]
        ]
      }
    ],
    "diagramId": "diag-cnt-agreement-vs-contract",
    "diagramExplanation": "Custom vector schematic illustrating the difference between an invitation to treat and a true offer leading to acceptance.",
    "misconceptions": [
      {
        "myth": "When a shop displays a coat in a shop window with a price tag, the shopkeeper is making an offer and must sell it to anyone who enters.",
        "reality": "Under Fisher v. Bell and Boots Cash Chemists, display in a shop window is an invitation to treat. The customer makes the offer, which the shopkeeper is free to accept or reject."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing cross-offers create a contract.",
        "reality": "When two parties make identical offers to each other in ignorance, they are 'cross-offers' and do NOT create a contract (Tinn v. Hoffmann).",
        "rule": "Cross-offers != Acceptance. There must be an acceptance of one offer."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-01-05",
        "front": "Which section of the Contract Act provides that performance of the conditions of a proposal constitutes acceptance?",
        "back": "Section 8.",
        "category": "Offer & Acceptance"
      },
      {
        "id": "fc-cnt-01-06",
        "front": "What did the Allahabad High Court hold in Lalman Shukla v. Gauri Datt (1913)?",
        "back": "An offer cannot be accepted without knowledge; a person finding a lost boy in ignorance of a reward cannot claim it.",
        "category": "Landmark Precedents"
      },
      {
        "id": "fc-cnt-01-07",
        "front": "Is a display of goods with price tags in a self-service store an offer or an invitation to treat?",
        "back": "It is an invitation to treat (Boots Cash Chemists case).",
        "category": "Invitation to Treat"
      },
      {
        "id": "fc-cnt-01-08",
        "front": "What was the ruling in Harvey v. Facey regarding quoting the lowest cash price of 'Bumper Hall Pen'?",
        "back": "Quoting lowest price is merely an invitation to treat, not an offer to sell.",
        "category": "Landmark Precedents"
      }
    ],
    "sourceReferences": [
      {"title": "Pollock & Mulla: Indian Contract Act", "url": "https://archive.org"},
      {"title": "Anson's Law of Contract — 31st Ed.", "url": "https://archive.org"}
    ]
}

data["top-cnt-01-03"] = {
    "topicId": "top-cnt-01-03",
    "chapterId": "ch-cnt-01",
    "subjectId": "law-contract",
    "title": "Acceptance, Postal Rule & Revocation (Sections 3–9)",
    "subtitle": "The Mirror Image Rule, The English Postal Exception, and Revocation Timelines",
    "bareActRef": "Indian Contract Act, 1872 — Sections 2(b), 3, 4, 5, 6, 7, 9",
    "learningObjective": "Master Section 2(b) acceptance, Section 7 absolute acceptance, Section 4 completion of communication by post, and Section 5 revocation rules.",
    "detailedExplanation": """
<h3>1. Section 2(b): The Nature of Acceptance</h3>
<p>'When the person to whom the proposal is made signifies his assent thereto, the proposal is said to be accepted. A proposal, when accepted, becomes a promise.'</p>
<p>Anson's celebrated metaphor: <em>'Acceptance is to a proposal what a lighted match is to a train of gunpowder. It produces something which cannot be undone.'</em></p>

<h3>2. Essentials of Valid Acceptance: Section 7</h3>
<p>To convert a proposal into a promise, the acceptance must be:</p>
<ol>
  <li><strong>Absolute and Unqualified:</strong> Must correspond exactly to the terms of the offer (the <em>Mirror Image Rule</em>). A conditional or qualified acceptance is a <strong>Counter-Offer</strong>, which destroys the original offer (<em>Hyde v. Wrench</em>).</li>
  <li><strong>Expressed in Some Usual and Reasonable Manner:</strong> Unless the proposal prescribes a particular mode. If a mode is prescribed and the offeree deviates, the proposer must insist on the prescribed mode within a reasonable time, failing which he is deemed to have accepted the deviation (Section 7(2)).</li>
</ol>

<h3>3. Communication of Acceptance by Post: Section 4</h3>
<p>The Indian rule on postal communication diverges uniquely into two separate completion points:</p>
<ul>
  <li><strong>As Against the Proposer:</strong> Communication of acceptance is complete <em>the moment the letter of acceptance is posted</em> (put in course of transmission so as to be out of the power of the acceptor). The proposer is immediately bound!</li>
  <li><strong>As Against the Acceptor:</strong> Communication of acceptance is complete only <em>when the letter of acceptance comes to the knowledge of the proposer</em>.</li>
</ul>

<h3>4. Revocation of Proposal and Acceptance: Section 5</h3>
<ul>
  <li><strong>Revocation of Proposal:</strong> A proposal may be revoked at any time <em>before the communication of its acceptance is complete as against the proposer</em> (i.e., before the letter of acceptance is posted).</li>
  <li><strong>Revocation of Acceptance:</strong> An acceptance may be revoked at any time <em>before the communication of the acceptance is complete as against the acceptor</em> (i.e., before the letter reaches the proposer).</li>
  <li><strong>Instantaneous Communication (Telephone, Telex, Email):</strong> Section 4 postal rule does NOT apply to instantaneous communication. The contract is formed only when the acceptance is actually heard or received by the offeror at his place of business (<em>Bhagwandas Goverdhandas Kedia v. Girdharilal Parshottamdas & Co., 1966 SC</em>).</li>
</ul>
""",
    "quickRevisionPoints": [
      "Section 2(b): Acceptance converts proposal into a promise; like a lighted match to gunpowder.",
      "Section 7: Acceptance must be absolute, unqualified, and in the usual/prescribed manner.",
      "Counter-offer destroys original offer (Hyde v. Wrench: counter-offer of £950 killed £1000 offer).",
      "Section 4 Postal Rule: As against proposer, complete upon POSTING; as against acceptor, complete upon RECEIPT.",
      "Section 5 Revocation: Offer can be revoked before acceptance letter is posted; acceptance can be revoked before letter is received.",
      "Bhagwandas v. Girdharilal (1966 SC): Phone/telex contracts are complete where acceptance is HEARD by offeror."
    ],
    "provisions": [
      {
        "provision": "Section 4, Indian Contract Act 1872",
        "title": "Communication When Complete",
        "description": "The communication of an acceptance is complete: as against the proposer, when it is put in a course of transmission to him, so as to be out of the power of the acceptor; as against the acceptor, when it comes to the knowledge of the proposer."
      },
      {
        "provision": "Section 5, Indian Contract Act 1872",
        "title": "Revocation of Proposals and Acceptances",
        "description": "A proposal may be revoked at any time before the communication of its acceptance is complete as against the proposer, but not afterwards. An acceptance may be revoked at any time before the communication of the acceptance is complete as against the acceptor, but not afterwards."
      }
    ],
    "definitions": [
      {
        "term": "Counter-Offer",
        "definition": "A conditional or varied reply to an offer which constitutes a rejection of the original offer and puts forward a new proposal."
      }
    ],
    "ingredients": [
      "Assent to all terms of proposal without variation.",
      "Communication in prescribed or reasonable mode.",
      "Compliance with Section 4 completion timeline."
    ],
    "exceptions": [
      "Silence does not constitute acceptance; an offeror cannot unilaterally declare that silence means assent (Felthouse v. Bindley)."
    ],
    "examples": [
      {
        "scenario": "A offers by letter to sell his house to B for Rs. 20 lakhs. B posts a letter of acceptance on 5th May. The letter reaches A on 8th May.",
        "application": "As against A, the contract is formed on 5th May (A cannot revoke after 5th May). As against B, the contract binds on 8th May (B can revoke his acceptance by telegram/email reaching before 8th May)."
      }
    ],
    "landmarkCases": [
      {
        "case": "Bhagwandas Goverdhandas Kedia v. Girdharilal Parshottamdas & Co.",
        "citation": "AIR 1966 SC 543",
        "year": "1966",
        "bench": "Supreme Court of India (Shah, Wanchoo, and Hidayatullah JJ)",
        "ratio": "In contracts made by telephone or instantaneous communication, Section 4 postal rule does not apply; the contract is complete only when the acceptance is received and heard by the offeror, and the cause of action arises where acceptance is heard.",
        "impact": "Primary Indian constitutional bench authority on instantaneous communication and jurisdiction."
      },
      {
        "case": "Hyde v. Wrench",
        "citation": "(1840) 3 Beav 334",
        "year": "1840",
        "bench": "Rolls Court (Lord Langdale MR)",
        "ratio": "A made an offer to sell an estate for £1,000. B offered £950, which A rejected. B then wrote agreeing to pay £1,000. Held: The counter-offer of £950 terminated the original offer of £1,000; no contract existed.",
        "impact": "Classic authority on the mirror image rule and counter-offer terminating the original proposal."
      },
      {
        "case": "Felthouse v. Bindley",
        "citation": "(1862) 11 CB (NS) 869",
        "year": "1862",
        "bench": "Court of Common Pleas (Willes J)",
        "ratio": "An uncle wrote to his nephew: 'If I hear no more about him, I consider the horse mine at £30 15s.' The nephew did not reply. Held: Acceptance cannot be imposed by silence; mental assent without communication does not create a contract.",
        "impact": "Foundational precedent establishing that silence does not amount to acceptance."
      }
    ],
    "comparisonTables": [
      {
        "title": "Postal Rule vs Instantaneous Communication",
        "headers": ["Aspect", "Postal Communication (s. 4 ICA)", "Instantaneous (Phone / Telex / Email)"],
        "rows": [
          ["When Complete against Offeror", "Moment letter is posted (put in transit)", "Moment acceptance is received / heard"],
          ["Place of Contract Formation", "Place where letter is posted", "Place where acceptance is heard / received"],
          ["Risk of Loss in Transit", "Borne by offeror", "Borne by acceptor (must ensure line was open)"],
          ["Governing Authority", "Section 4 ICA; Adams v. Lindsell", "Bhagwandas v. Girdharilal (1966 SC); Entores"]
        ]
      }
    ],
    "diagramId": "diag-cnt-agreement-vs-contract",
    "diagramExplanation": "Custom vector schematic illustrating Section 4 timelines for postal contracts and revocation limits under Section 5.",
    "misconceptions": [
      {
        "myth": "In India, both parties are bound simultaneously the moment the acceptance letter is dropped in the letterbox.",
        "reality": "Only the proposer is bound upon posting. The acceptor is not bound until the letter reaches the proposer; the acceptor can revoke before receipt."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Applying the postal rule to contracts concluded over telephone.",
        "reality": "Telephone contracts are governed by the instantaneous communication rule (Bhagwandas Kedia): contract is made where acceptance is HEARD.",
        "rule": "Postal = Place of Posting; Phone/Email = Place of Receipt."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-01-09",
        "front": "When is communication of acceptance complete as against the PROPOSER under Section 4?",
        "back": "When it is put in course of transmission to him so as to be out of the power of the acceptor (moment of posting).",
        "category": "Section 4"
      },
      {
        "id": "fc-cnt-01-10",
        "front": "What did the Supreme Court hold in Bhagwandas v. Girdharilal regarding telephone contracts?",
        "back": "The postal rule does not apply; the contract is complete where the acceptance is heard by the offeror.",
        "category": "Landmark Precedents"
      },
      {
        "id": "fc-cnt-01-11",
        "front": "What is the legal effect of a Counter-Offer on the original offer?",
        "back": "It terminates and destroys the original offer (Hyde v. Wrench).",
        "category": "Counter-Offers"
      },
      {
        "id": "fc-cnt-01-12",
        "front": "Does mental assent or silence amount to a valid acceptance?",
        "back": "No, silence cannot be prescribed as a mode of acceptance (Felthouse v. Bindley).",
        "category": "Acceptance Rules"
      }
    ],
    "sourceReferences": [
      {"title": "Pollock & Mulla: Indian Contract Act", "url": "https://archive.org"},
      {"title": "Anson's Law of Contract", "url": "https://archive.org"}
    ]
}

data["top-cnt-01-04"] = {
    "topicId": "top-cnt-01-04",
    "chapterId": "ch-cnt-01",
    "subjectId": "law-contract",
    "title": "Intention to Create Legal Relations (Balfour v Balfour Rule)",
    "subtitle": "The Essential Mental Element Distinguishing Enforceable Contracts from Social Promises",
    "bareActRef": "Indian Contract Act, 1872 — Judicial Doctrine (Section 10)",
    "learningObjective": "Analyze the common law doctrine of intention to create legal relations, its status under Indian law, and the rebuttable presumptions in domestic vs commercial arrangements.",
    "detailedExplanation": """
<h3>1. The Doctrine of Intention to Create Legal Relations</h3>
<p>To constitute a binding contract, there must be a common intention of the parties to enter into legal obligations and be subject to the sanctions of law. If parties do not intend their agreement to result in legal rights and duties, no contract arises.</p>

<h3>2. The Two Classical Presumptions</h3>
<ol>
  <li><strong>Domestic and Social Agreements (Presumption of No Legal Intention):</strong> Agreements between family members, spouses, or friends are presumed <em>not</em> to be intended as legally binding contracts (<em>Balfour v. Balfour</em>).
    <ul>
      <li><em>Rebuttal:</em> The presumption is rebutted where spouses are already separated or contemplating divorce when executing written property/maintenance agreements (<em>Merritt v. Merritt, 1970</em>), or where substantial financial expenditure was incurred in reliance on the promise (<em>Parker v. Clark</em>).</li>
    </ul>
  </li>
  <li><strong>Commercial and Business Agreements (Presumption of Legal Intention):</strong> In commercial transactions, there is a strong presumption that parties intend to create legal relations.
    <ul>
      <li><em>Rebuttal:</em> The presumption can be rebutted only by an express, unequivocal clause in the agreement declaring that it shall not be attended by legal consequences, such as an 'Honour Pledge Clause' (<em>Rose and Frank Co. v. J.R. Crompton & Bros.</em>).</li>
    </ul>
  </li>
</ol>

<h3>3. Position Under Indian Law</h3>
<p>Although 'intention to create legal relations' is not expressly listed in the text of Section 10 of the Indian Contract Act 1872, the Supreme Court of India in <em>CWT v. Abdul Hussain (1977)</em> and <em>Banwari Lal v. Sukhdarshan Dayal (1973)</em> recognized it as a necessary ingredient of a valid contract under Indian law, derived from the requirement of consensus and Section 2(a) ('with a view to obtaining the assent').</p>
""",
    "quickRevisionPoints": [
      "Intention to create legal relations is an essential test of contractual enforceability.",
      "Domestic/Social agreements: Presumed NOT to intend legal consequences (Balfour v. Balfour).",
      "Rebuttal in domestic agreements: Merritt v. Merritt (spouses separated; written agreement enforceable).",
      "Commercial agreements: Presumed to intend legal relations.",
      "Honour Pledge Clause: Rebuts legal intention in business contracts (Rose and Frank Co. v. Crompton).",
      "Indian position: SC recognized it as an essential ingredient in CWT v. Abdul Hussain (1977)."
    ],
    "provisions": [
      {
        "provision": "Judicial Requisite",
        "title": "Animus Contrahendi",
        "description": "The common intention of the parties to enter into legal obligations enforceable by the courts."
      }
    ],
    "definitions": [
      {
        "term": "Honour Pledge Clause",
        "definition": "An explicit contractual clause stating that the arrangement is not entered into as a formal legal agreement, and shall not be subject to legal jurisdiction in law courts."
      }
    ],
    "ingredients": [
      "Objective intention inferred from language and circumstances.",
      "Application of domestic vs commercial presumptions.",
      "Evidence sufficient to rebut the baseline presumption."
    ],
    "exceptions": [
      "Agreements expressly designated as binding in honour only."
    ],
    "examples": [
      {
        "scenario": "A husband agrees to pay £30 a month to his wife for maintenance while he lives abroad for his job.",
        "application": "Under Balfour v. Balfour, this is an ordinary domestic arrangement with no intention to create legal relations; wife cannot sue for arrears."
      }
    ],
    "landmarkCases": [
      {
        "case": "Balfour v. Balfour",
        "citation": "(1919) 2 KB 571",
        "year": "1919",
        "bench": "Court of Appeal (Warrington, Duke, and Atkin LJJ)",
        "ratio": "Spouses entering into domestic living arrangements do not intend that they should be attended by legal consequences. The law of contract does not regulate domestic marital promises.",
        "impact": "The foundational ruling on intention to create legal relations."
      },
      {
        "case": "Merritt v. Merritt",
        "citation": "(1970) 1 WLR 1211",
        "year": "1970",
        "bench": "Court of Appeal (Lord Denning MR)",
        "ratio": "Where a husband and wife had separated and the husband signed an agreement to pay £40 a month and transfer the house upon completion of mortgage payments, held: the domestic presumption did not apply; the parties were bargaining at arm's length and intended legal relations.",
        "impact": "Classic authority demonstrating the rebuttal of the Balfour domestic presumption upon marital separation."
      },
      {
        "case": "Rose and Frank Co. v. J.R. Crompton & Bros.",
        "citation": "(1925) AC 445",
        "year": "1925",
        "bench": "House of Lords",
        "ratio": "A commercial agency contract containing an express 'Honourable Pledge Clause' explicitly excluding the jurisdiction of courts was held not to be an enforceable legal contract.",
        "impact": "Authoritative precedent on rebutting the commercial presumption of legal intention."
      }
    ],
    "comparisonTables": [
      {
        "title": "Domestic vs Commercial Presumptions",
        "headers": ["Type of Agreement", "Presumption", "Standard of Rebuttal", "Leading Authority"],
        "rows": [
          ["Domestic / Social", "NO intention to create legal relations", "Evidence of separation, written deed, substantial reliance", "Balfour v. Balfour (1919); Merritt (1970)"],
          ["Commercial / Business", "YES, intention to create legal relations", "Express and unequivocal exclusion clause (Honour clause)", "Rose & Frank Co. v. Crompton (1925)"]
        ]
      }
    ],
    "diagramId": "diag-cnt-agreement-vs-contract",
    "diagramExplanation": "Custom vector schematic illustrating how intention filters agreements into contracts.",
    "misconceptions": [
      {
        "myth": "Because Section 10 does not mention 'intention to create legal relations', Indian courts enforce all domestic agreements.",
        "reality": "Indian courts consistently require intention to create legal relations, interpreting Section 2(a) and Section 10 as encompassing animus contrahendi."
      }
    ],
    "prelimTraps": [
      {
        "trap": "Believing Merritt v. Merritt followed Balfour v. Balfour.",
        "reality": "Merritt v. Merritt DISTINGUISHED Balfour because the spouses were living separately and negotiating at arm's length.",
        "rule": "Balfour = Amicable spouses (Not binding); Merritt = Separated spouses (Binding)."
      }
    ],
    "flashcards": [
      {
        "id": "fc-cnt-01-13",
        "front": "What did the Court of Appeal hold in Balfour v. Balfour (1919)?",
        "back": "Domestic agreements between spouses living in harmony lack intention to create legal relations and are not contracts.",
        "category": "Intention"
      },
      {
        "id": "fc-cnt-01-14",
        "front": "Under what circumstance was the domestic presumption rebutted in Merritt v. Merritt?",
        "back": "The husband and wife had separated and entered into a written agreement regarding the matrimonial house.",
        "category": "Rebutting Presumptions"
      },
      {
        "id": "fc-cnt-01-15",
        "front": "What is an 'Honourable Pledge Clause' in commercial contracts?",
        "back": "A clause explicitly stating that the agreement is an honorable commitment and not a legal contract enforceable in courts.",
        "category": "Commercial Contracts"
      },
      {
        "id": "fc-cnt-01-16",
        "front": "What Latin phrase signifies the intention to contract?",
        "back": "'Animus Contrahendi'.",
        "category": "Legal Terms"
      }
    ],
    "sourceReferences": [
      {"title": "Anson's Law of Contract", "url": "https://archive.org"},
      {"title": "Pollock & Mulla: Indian Contract Act", "url": "https://archive.org"}
    ]
}

create_concept_file('assets/learning/data/contract/contract-concepts-part1.js', 'CONTRACT_CONCEPTS_PART1', data)
print(f"Contract Part 1 initial authoring: {len(data)} topics!")
