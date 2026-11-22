# Generator for Contract Law MCQs Part 1 (Chapters 1 to 4, 112 MCQs)
import json

raw_items = [
    # CH-01: Formation of Contract
    # top-cnt-01-01: Agreement and Contract (Section 2(h) & Section 10 Essentials) - 8 MCQs
    (
        "mcq-cnt-01-001", "ch-cnt-01", "top-cnt-01-01",
        "Under Section 2(h) of the Indian Contract Act, 1872, a contract is defined as:",
        ["An agreement between two competent parties", "An agreement enforceable by law", "A promise supported by consideration", "An accepted proposal"],
        1, "B",
        "Section 2(h) provides that 'an agreement enforceable by law is a contract'.",
        {"A": "Enforceability by law is the crucial defining element in Section 2(h).", "B": "Correct. Section 2(h) defines contract as an agreement enforceable by law.", "C": "This describes consideration under Section 2(d).", "D": "This describes an agreement under Section 2(e)."},
        "Easy", "Indian Contract Act, 1872, Section 2(h)", "Master statutory definition of contract."
    ),
    (
        "mcq-cnt-01-002", "ch-cnt-01", "top-cnt-01-01",
        "According to Section 10 of the Indian Contract Act, all agreements are contracts if they are made by:",
        ["Free consent of parties competent to contract, for lawful consideration and lawful object, and not expressly declared void", "Parties of sound mind with written execution before a notary", "Mutual assent and registered with a sub-registrar", "Two parties having identical nationality"],
        0, "A",
        "Section 10 lists essentials: free consent of parties competent to contract, lawful consideration, lawful object, and not expressly declared void.",
        {"A": "Correct. Section 10 sets out the core statutory ingredients of valid contracts.", "B": "Notarization is not a universal requirement under Section 10.", "C": "Registration is only required for specific contracts under special statutes.", "D": "Nationality is irrelevant to competency under Section 10."},
        "Easy", "Indian Contract Act, 1872, Section 10", "Identify core statutory essentials under Section 10."
    ),
    (
        "mcq-cnt-01-003", "ch-cnt-01", "top-cnt-01-01",
        "Which of the following statements correctly represents the relationship between an agreement and a contract?",
        ["Every contract is an agreement, but every agreement is not necessarily a contract", "Every agreement is a contract, but every contract is not an agreement", "Agreement and contract are synonymous terms under Indian law", "An agreement is always enforceable in a court of law"],
        0, "A",
        "Agreement is the genus (Section 2(e)) while contract is the species (Section 2(h)). Only agreements enforceable by law become contracts.",
        {"A": "Correct. All contracts are agreements, but only legally enforceable agreements are contracts.", "B": "Reversed statement; legally incorrect.", "C": "Distinct statutory concepts under Sections 2(e) and 2(h).", "D": "Agreements such as social, domestic, or void agreements are unenforceable."},
        "Medium", "Indian Contract Act, 1872, Sections 2(e), 2(h)", "Distinguish legal scope of agreement and contract."
    ),
    (
        "mcq-cnt-01-004", "ch-cnt-01", "top-cnt-01-01",
        "Under Section 2(e) of the Indian Contract Act, every promise and every set of promises, forming the consideration for each other, is an:",
        ["Offer", "Agreement", "Acceptance", "Executed contract"],
        1, "B",
        "Section 2(e) defines agreement as 'every promise and every set of promises, forming the consideration for each other'.",
        {"A": "Offer is defined under Section 2(a).", "B": "Correct. Section 2(e) explicitly defines an agreement.", "C": "Acceptance is defined under Section 2(b).", "D": "An executed contract requires completed performance and enforceability."},
        "Easy", "Indian Contract Act, 1872, Section 2(e)", "Recall statutory definition of agreement."
    ),
    (
        "mcq-cnt-01-005", "ch-cnt-01", "top-cnt-01-01",
        "An agreement not enforceable by law is said to be:",
        ["Voidable", "Void", "Illegal", "Unenforceable but valid"],
        1, "B",
        "Section 2(g) of the Indian Contract Act states: 'An agreement not enforceable by law is said to be void'.",
        {"A": "Voidable agreements are enforceable at option of one party under Section 2(i).", "B": "Correct. Section 2(g) defines void agreements as those unenforceable by law.", "C": "Illegal agreements involve statutory prohibitions or criminal elements.", "D": "Unenforceable due to technical defects is distinct from void ab initio."},
        "Easy", "Indian Contract Act, 1872, Section 2(g)", "Identify void agreements under Section 2(g)."
    ),
    (
        "mcq-cnt-01-006", "ch-cnt-01", "top-cnt-01-01",
        "An agreement enforceable by law at the option of one or more of the parties thereto, but not at the option of the other or others, is a:",
        ["Void agreement", "Voidable contract", "Contingent contract", "Quasi-contract"],
        1, "B",
        "Section 2(i) defines voidable contract as an agreement enforceable by law at option of one or more parties, but not at option of other(s).",
        {"A": "Void agreements are unenforceable by either party (Section 2(g)).", "B": "Correct. Section 2(i) defines a voidable contract.", "C": "Contingent contracts depend on happening of uncertain collateral events (Section 31).", "D": "Quasi-contracts are obligations created by law without agreement (Sections 68-72)."},
        "Easy", "Indian Contract Act, 1872, Section 2(i)", "Distinguish voidable contract under Section 2(i)."
    ),
    (
        "mcq-cnt-01-007", "ch-cnt-01", "top-cnt-01-01",
        "A contract which ceases to be enforceable by law becomes void when it:",
        ["Is formed without writing", "Ceases to be enforceable", "Is entered into by a minor", "Is registered under the Registration Act"],
        1, "B",
        "Section 2(j) provides: 'A contract which ceases to be enforceable by law becomes void when it ceases to be enforceable'.",
        {"A": "Oral contracts can be completely valid under Section 10.", "B": "Correct. Section 2(j) governs contracts that become void subsequent to formation.", "C": "A minor's agreement is void ab initio, never becoming a valid contract first.", "D": "Registration does not render a contract void."},
        "Medium", "Indian Contract Act, 1872, Section 2(j)", "Apply Section 2(j) on contracts becoming void."
    ),
    (
        "mcq-cnt-01-008", "ch-cnt-01", "top-cnt-01-01",
        "Which of the following is NOT an essential element of a valid contract under Section 10 of the Indian Contract Act?",
        ["Free consent of parties", "Adequacy of consideration", "Competency of parties", "Lawful object and consideration"],
        1, "B",
        "Explanation 2 to Section 25 clearly establishes that consideration need not be adequate; an agreement is not void merely because consideration is inadequate.",
        {"A": "Free consent is an essential element under Section 10 and Section 14.", "B": "Correct. Adequacy of consideration is not required; it only needs to have legal value.", "C": "Competency is an essential element under Section 10 and Section 11.", "D": "Lawful object and consideration are essential under Section 10 and Section 23."},
        "Medium", "Indian Contract Act, 1872, Sections 10, 25", "Evaluate consideration adequacy requirement."
    ),

    # top-cnt-01-02: Offer / Proposal: Essentials & Offer vs Invitation to Treat - 8 MCQs
    (
        "mcq-cnt-01-009", "ch-cnt-01", "top-cnt-01-02",
        "Under Section 2(a) of the Indian Contract Act, a proposal is made when a person signifies to another:",
        ["A desire to enter negotiations", "His willingness to do or to abstain from doing anything, with a view to obtaining the assent of that other", "An invitation to receive tenders", "A conditional statement of price"],
        1, "B",
        "Section 2(a) defines proposal: when one person signifies to another willingness to do/abstain with a view to obtaining assent of the other.",
        {"A": "Negotiations precede a proposal and lack final assent-seeking intention.", "B": "Correct. Statutory definition under Section 2(a).", "C": "Invitation to tender is an invitation to offer, not a proposal.", "D": "Quotation of price without assent-seeking intent is an invitation to treat."},
        "Easy", "Indian Contract Act, 1872, Section 2(a)", "Analyze definition of proposal under Section 2(a)."
    ),
    (
        "mcq-cnt-01-010", "ch-cnt-01", "top-cnt-01-02",
        "In the landmark Privy Council decision Harvey v. Facey (1893), telegraphing the lowest cash price of 'Bumper Hall Pen' was held to be:",
        ["An unconditional offer to sell", "A mere statement of lowest price (invitation to treat), not an offer", "An implied acceptance of plaintiff's offer", "A counter-proposal binding on the sender"],
        1, "B",
        "In Harvey v. Facey, the Privy Council held that quoting the lowest price was merely supplying information/invitation to treat, not an offer to sell.",
        {"A": "The court expressly rejected that quoting price constituted an offer to sell.", "B": "Correct. A quotation of minimum price is an invitation to treat.", "C": "Acceptance requires unequivocal assent, which was absent.", "D": "It was not a counter-proposal because no offer had been made."},
        "Medium", "Privy Council: Harvey v. Facey (1893) AC 552", "Distinguish offer from quotation of price in Harvey v Facey."
    ),
    (
        "mcq-cnt-01-011", "ch-cnt-01", "top-cnt-01-02",
        "In Pharmaceutical Society of Great Britain v. Boots Cash Chemists (1953), display of goods with price tags on a self-service shelf was held to be:",
        ["A binding standing offer to the public", "An invitation to treat", "A completed sale upon picking up the item", "A unilateral contract"],
        1, "B",
        "The English Court of Appeal held that display of goods in a shop is an invitation to treat; the customer makes the offer at the cash register.",
        {"A": "Goods display is not a binding offer to the public.", "B": "Correct. Shelf display with prices is an invitation to treat.", "C": "Sale is completed only when cashier accepts the customer's offer at the till.", "D": "Unilateral contracts require full performance of stipulated conditions."},
        "Medium", "Pharmaceutical Society of Great Britain v. Boots Cash Chemists (1953) 1 QB 401", "Identify legal nature of shelf display in shops."
    ),
    (
        "mcq-cnt-01-012", "ch-cnt-01", "top-cnt-01-02",
        "In Carlill v. Carbolic Smoke Ball Co. (1893), the advertisement offering £100 reward to anyone contracting influenza after using the smoke ball was held to be:",
        ["An invitation to treat", "A general offer made to the whole world, accepted by performance of conditions", "A void wagering agreement", "A void agreement due to uncertainty"],
        1, "B",
        "In Carlill v. Carbolic Smoke Ball Co., the court held that an offer can be made to the whole world, and notification of acceptance is dispensed with upon performance.",
        {"A": "The deposit of £1,000 in Alliance Bank showed clear intention to be bound, making it an offer.", "B": "Correct. It was a valid general offer accepted by performing the prescribed conditions.", "C": "It was not a wager because plaintiff had an interest in using the product.", "D": "The terms were sufficiently certain to form a binding contract."},
        "Medium", "Carlill v. Carbolic Smoke Ball Co. (1893) 1 QB 256", "Apply general offer doctrine in Carlill case."
    ),
    (
        "mcq-cnt-01-013", "ch-cnt-01", "top-cnt-01-02",
        "Under Section 8 of the Indian Contract Act, performance of the conditions of a proposal is an:",
        ["Invitation to make a counter-offer", "Acceptance of the proposal", "Impossibility of performance", "Revocation of the proposal"],
        1, "B",
        "Section 8 provides: 'Performance of the conditions of a proposal, or the acceptance of any consideration for a reciprocal promise... is an acceptance of the proposal'.",
        {"A": "Performance indicates acceptance, not counter-proposal.", "B": "Correct. Section 8 codifies acceptance by performing conditions.", "C": "Performance is the opposite of impossibility.", "D": "Performance solidifies contract formation rather than revocation."},
        "Easy", "Indian Contract Act, 1872, Section 8", "Understand acceptance by performance under Section 8."
    ),
    (
        "mcq-cnt-01-014", "ch-cnt-01", "top-cnt-01-02",
        "In Lalman Shukla v. Gauri Dutt (1913), the servant who traced the missing nephew without knowledge of the announced reward was held:",
        ["Entitled to the reward because he performed the condition", "Not entitled to the reward because an offer cannot be accepted without knowledge of its existence", "Entitled to half the reward on quantum meruit", "Entitled to damages for breach of trust"],
        1, "B",
        "The Allahabad High Court held that an offer cannot be accepted in ignorance of its existence; assent requires mutual communication and awareness.",
        {"A": "Performance without knowledge of offer does not constitute valid acceptance.", "B": "Correct. Lalman Shukla established that knowledge of the offer is essential for acceptance.", "C": "Quantum meruit is inapplicable where no contractual relationship exists.", "D": "No trust relationship was created regarding the reward."},
        "Hard", "Lalman Shukla v. Gauri Dutt (1913) 11 ALJ 489", "Recall rule on knowledge of offer in Lalman Shukla."
    ),
    (
        "mcq-cnt-01-015", "ch-cnt-01", "top-cnt-01-02",
        "Which of the following is generally considered an 'invitation to offer' rather than a valid proposal?",
        ["A catalogue of books listing titles and prices", "An announcement of auction sale", "A tender notice inviting quotations", "All of the above"],
        3, "D",
        "Catalogues, auction notices, and tender notices are all invitations to treat/invitations to make offers, not definitive offers.",
        {"A": "A price catalogue is an invitation to treat.", "B": "An auction notice is an invitation to prospective bidders to attend and make bids.", "C": "A tender notice invites contractors to submit offers.", "D": "Correct. All listed items constitute invitations to treat."},
        "Medium", "Indian Contract Act, 1872, Section 2(a)", "Distinguish invitations to offer from proposals."
    ),
    (
        "mcq-cnt-01-016", "ch-cnt-01", "top-cnt-01-02",
        "A counter-offer made in response to an original proposal has the legal effect of:",
        ["Suspending the original offer until further notice", "Rejecting and terminating the original offer", "Accepting the original offer conditionally", "Binding the original offeror unconditionally"],
        1, "B",
        "Under Hyde v. Wrench (1840), a counter-offer amounts to a rejection of the original offer, extinguishing it so it cannot subsequently be accepted.",
        {"A": "A counter-offer does not suspend; it destroys the original offer.", "B": "Correct. Under Hyde v. Wrench, a counter-offer terminates the original proposal.", "C": "Conditional acceptance is itself a counter-offer, not an acceptance.", "D": "An offeror is never bound by an unaccepted or counter-offered proposal."},
        "Medium", "Hyde v. Wrench (1840) 3 Beav 334", "Analyze legal effect of a counter-offer."
    ),

    # top-cnt-01-03: Acceptance, Postal Rule & Revocation (Sections 3–9) - 8 MCQs
    (
        "mcq-cnt-01-017", "ch-cnt-01", "top-cnt-01-03",
        "Under Section 2(b) of the Indian Contract Act, when the person to whom the proposal is made signifies his assent thereto, the proposal is said to be accepted. A proposal, when accepted, becomes a:",
        ["Contract", "Promise", "Warranty", "Condition precedent"],
        1, "B",
        "Section 2(b) explicitly provides: 'A proposal, when accepted, becomes a promise'.",
        {"A": "An accepted proposal becomes a promise; it becomes a contract only when supported by consideration and enforceable.", "B": "Correct. Under Section 2(b), an accepted proposal becomes a promise.", "C": "Warranty is a collateral stipulation in Sale of Goods.", "D": "Condition precedent is a preliminary prerequisite for obligation."},
        "Easy", "Indian Contract Act, 1872, Section 2(b)", "Identify statutory result of accepted proposal."
    ),
    (
        "mcq-cnt-01-018", "ch-cnt-01", "top-cnt-01-03",
        "Under Section 7 of the Indian Contract Act, in order to convert a proposal into a promise, the acceptance must be:",
        ["Absolute and unqualified", "Expressed in some usual and reasonable manner, unless the proposal prescribes the manner", "Both A and B", "Neither A nor B"],
        2, "C",
        "Section 7 requires acceptance to be absolute and unqualified, and expressed in some usual and reasonable manner unless prescribed.",
        {"A": "Section 7(1) requires absolute and unqualified acceptance.", "B": "Section 7(2) requires usual and reasonable manner unless prescribed.", "C": "Correct. Both clauses (1) and (2) of Section 7 are statutory requirements.", "D": "Incorrect as both A and B are mandatory statutory requirements."},
        "Easy", "Indian Contract Act, 1872, Section 7", "Master requirements of acceptance under Section 7."
    ),
    (
        "mcq-cnt-01-019", "ch-cnt-01", "top-cnt-01-03",
        "Under Section 4 of the Indian Contract Act, the communication of an acceptance is complete as against the proposer when:",
        ["It comes to the actual knowledge of the proposer", "It is put in a course of transmission to him, so as to be out of the power of the acceptor", "It is written and signed by the acceptor", "The acceptor posts a registered receipt"],
        1, "B",
        "Section 4 paragraph 2: Communication of acceptance is complete against the proposer when put in course of transmission out of the power of acceptor.",
        {"A": "Actual knowledge completes acceptance as against the acceptor, not the proposer.", "B": "Correct. As against proposer, acceptance is complete upon posting (course of transmission).", "C": "Signing without transmission is not communication.", "D": "Receipt is not required; putting in transmission suffices."},
        "Hard", "Indian Contract Act, 1872, Section 4", "Distinguish communication completion points under Section 4."
    ),
    (
        "mcq-cnt-01-020", "ch-cnt-01", "top-cnt-01-03",
        "Under Section 4 of the Indian Contract Act, the communication of an acceptance is complete as against the acceptor when:",
        ["It is put into the post office", "It comes to the knowledge of the proposer", "The proposer replies with an acknowledgment", "The contract is registered"],
        1, "B",
        "Section 4 states that communication of acceptance is complete as against the acceptor when it comes to the knowledge of the proposer.",
        {"A": "Posting completes acceptance against proposer, not against acceptor.", "B": "Correct. As against acceptor, communication is complete when it reaches proposer's knowledge.", "C": "Proposer's reply is unnecessary for contract completion.", "D": "Registration is irrelevant to Section 4 postal rules."},
        "Medium", "Indian Contract Act, 1872, Section 4", "Analyze when acceptance binds the acceptor."
    ),
    (
        "mcq-cnt-01-021", "ch-cnt-01", "top-cnt-01-03",
        "In Bhagwandas Goverdhandas Kedia v. Girdharilal Parshottamdas & Co. (AIR 1966 SC 543), the Supreme Court held that in contracts negotiated by telephone or telex:",
        ["The postal rule under Section 4 applies and contract is formed where acceptance is spoken", "The contract is complete only when acceptance is heard and received by the offeror, at the offeror's place", "No contract is formed unless confirmed in writing within 24 hours", "The contract is formed halfway between the two parties"],
        1, "B",
        "The Supreme Court held that instantaneous communications (phone/telex) fall outside the postal rule; contract is complete where acceptance is heard by offeror (Entores rule).",
        {"A": "The postal rule applies only to non-instantaneous post, not telephone.", "B": "Correct. For instantaneous communication, contract is made where acceptance is received.", "C": "Written confirmation is not a legal prerequisite.", "D": "Fictional concept rejected in law."},
        "Hard", "Supreme Court: Bhagwandas v. Girdharilal (AIR 1966 SC 543)", "Apply instantaneous communication rule in Bhagwandas case."
    ),
    (
        "mcq-cnt-01-022", "ch-cnt-01", "top-cnt-01-03",
        "In Felthouse v. Bindley (1862), the uncle wrote offering to buy his nephew's horse, stating 'If I hear no more about him, I consider the horse mine'. The court held:",
        ["Silence constituted valid acceptance because the nephew intended to sell", "Mental acceptance or silence cannot be imposed as a mode of acceptance without communication", "A valid contract was formed upon the nephew telling the auctioneer not to sell", "The auctioneer became personally liable to the uncle"],
        1, "B",
        "Felthouse v. Bindley established that an offeror cannot impose silence as acceptance; acceptance must be positively communicated to the offeror.",
        {"A": "Subjective intent without communication does not form a binding contract.", "B": "Correct. Silence cannot amount to valid acceptance.", "C": "Internal instructions to auctioneer did not constitute communication to the uncle.", "D": "The auctioneer was held not liable to uncle because no property had passed."},
        "Medium", "Felthouse v. Bindley (1862) 11 CB (NS) 869", "Recall rule on silence and acceptance in Felthouse v Bindley."
    ),
    (
        "mcq-cnt-01-023", "ch-cnt-01", "top-cnt-01-03",
        "Under Section 5 of the Indian Contract Act, a proposal may be revoked at any time:",
        ["Before the communication of its acceptance is complete as against the proposer, but not afterwards", "Before the communication of its acceptance is complete as against the acceptor", "Within 30 days of making the proposal", "Until consideration is actually paid"],
        0, "A",
        "Section 5 paragraph 1: 'A proposal may be revoked at any time before the communication of its acceptance is complete as against the proposer, but not afterwards'.",
        {"A": "Correct. Proposer can revoke anytime before acceptance is posted/transmitted.", "B": "Against acceptor is the deadline for acceptor's revocation, not proposer's.", "C": "No arbitrary 30-day statutory time limit exists.", "D": "Payment of consideration is not the benchmark for revocation."},
        "Medium", "Indian Contract Act, 1872, Section 5", "Identify time limit for revocation of proposal."
    ),
    (
        "mcq-cnt-01-024", "ch-cnt-01", "top-cnt-01-03",
        "Under Section 5 of the Indian Contract Act, an acceptance may be revoked at any time:",
        ["Before or at the moment when the letter of acceptance is posted", "Before or at the moment when the communication of acceptance is complete as against the acceptor, but not afterwards", "Even after the proposer reads the acceptance letter", "Only with the written permission of a civil court"],
        1, "B",
        "Section 5 paragraph 2: 'An acceptance may be revoked at any time before or at the moment when the communication of the acceptance is complete as against the acceptor, but not afterwards'.",
        {"A": "Posting binds proposer, but acceptor can revoke until proposer receives it.", "B": "Correct. Acceptor can revoke before or when acceptance reaches proposer's knowledge.", "C": "Once proposer knows of acceptance, contract is irrevocable by acceptor.", "D": "Judicial intervention is not required to revoke an acceptance."},
        "Medium", "Indian Contract Act, 1872, Section 5", "Identify time limit for revocation of acceptance."
    ),

    # top-cnt-01-04: Intention to Create Legal Relations (Balfour v Balfour Rule) - 8 MCQs
    (
        "mcq-cnt-01-025", "ch-cnt-01", "top-cnt-01-04",
        "In Balfour v. Balfour (1919), Lord Atkin held that agreements between husband and wife living in amity:",
        ["Are presumed to be legally binding contracts", "Are presumed not to result in legally enforceable contracts because parties do not intend legal consequences", "Are void ab initio under public policy", "Must be executed on judicial stamp paper"],
        1, "B",
        "In Balfour v. Balfour, Lord Atkin held that domestic agreements between spouses are presumed to lack intention to create legal relations.",
        {"A": "Commercial presumption is the opposite of domestic presumption.", "B": "Correct. Domestic agreements carry a presumption against intention to create legal relations.", "C": "They are not illegal or void ab initio, merely lacking legal intent.", "D": "Stamp paper is not a criterion for legal intention."},
        "Easy", "Court of Appeal: Balfour v. Balfour (1919) 2 KB 571", "Master Balfour v Balfour domestic presumption doctrine."
    ),
    (
        "mcq-cnt-01-026", "ch-cnt-01", "top-cnt-01-04",
        "In Merritt v. Merritt (1970), where husband and wife were separated and negotiated arrangements regarding their matrimonial home, the court held:",
        ["The presumption against intention to create legal relations applied as they were still married", "The domestic presumption was rebutted because separated spouses bargain at arm's length intending legal relations", "The agreement was void for want of consideration", "The agreement was voidable at option of the husband"],
        1, "B",
        "In Merritt v. Merritt, Lord Denning held that when spouses are separated or about to separate, the Balfour presumption does not apply.",
        {"A": "Separation rebuts the domestic harmony presumption.", "B": "Correct. Separated spouses negotiating their affairs intend to create binding legal relations.", "C": "Paying off mortgage constituted valid consideration.", "D": "The contract was fully valid and binding, not voidable."},
        "Medium", "Merritt v. Merritt (1970) 1 WLR 1211", "Distinguish Merritt v Merritt from Balfour v Balfour."
    ),
    (
        "mcq-cnt-01-027", "ch-cnt-01", "top-cnt-01-04",
        "In commercial agreements, the legal presumption regarding intention to create legal relations is:",
        ["Parties intend to create legal relations, but this presumption can be rebutted by express words like 'honour pledge'", "Parties never intend legal relations unless registered", "Intention must be proven by oral testimony in every single case", "Agreements are void unless executed before a magistrate"],
        0, "A",
        "In commercial transactions, there is a strong presumption of legal relations, rebuttable only by clear express exclusion (e.g. Rose & Frank v. JR Crompton).",
        {"A": "Correct. Commercial dealings presume legal enforceability unless explicitly excluded.", "B": "Registration is not required to establish legal intent.", "C": "The law presumes intention without requiring separate proof.", "D": "Magisterial execution is not a contract requirement."},
        "Medium", "Rose & Frank Co. v. J.R. Crompton & Bros (1925) AC 445", "Understand commercial presumption of legal relations."
    ),
    (
        "mcq-cnt-01-028", "ch-cnt-01", "top-cnt-01-04",
        "In Rose & Frank Co. v. J.R. Crompton & Bros (1925), an 'honourable pledge clause' explicitly declaring that the arrangement was not a formal or legal agreement was held:",
        ["Illegal and contrary to public policy", "Valid to rebut the presumption of legal relations, leaving the agreement unenforceable in court", "A void condition under Section 28", "To confer exclusive jurisdiction on arbitration"],
        1, "B",
        "The House of Lords held that parties to a business arrangement may expressly declare their intention that it shall not be attended by legal consequences.",
        {"A": "Parties are free to decide whether to enter legal relations.", "B": "Correct. An express clause excluding legal intent makes the arrangement an honour agreement.", "C": "Section 28 applies to contracts, whereas this never became a contract.", "D": "It excluded court and arbitral jurisdiction entirely."},
        "Hard", "House of Lords: Rose & Frank v. Crompton (1925) AC 445", "Analyze honour pledge clauses excluding legal relations."
    ),
    (
        "mcq-cnt-01-029", "ch-cnt-01", "top-cnt-01-04",
        "In Jones v. Padavatton (1969), a mother promised to pay monthly allowance to her daughter if she studied for the Bar in London. The agreement was held:",
        ["A binding commercial service contract", "A domestic family arrangement lacking intention to create legal relations", "A contract of guarantee under Section 126", "A void wagering contract"],
        1, "B",
        "The Court of Appeal held that the arrangement between mother and daughter was a family arrangement without intent to create legal relations.",
        {"A": "It was purely domestic, lacking commercial character.", "B": "Correct. Family arrangements are presumed to lack intention to create legal relations.", "C": "No third-party debt guarantee was involved.", "D": "No wager was involved."},
        "Medium", "Jones v. Padavatton (1969) 2 All ER 616", "Apply domestic presumption to parent-child agreements."
    ),
    (
        "mcq-cnt-01-030", "ch-cnt-01", "top-cnt-01-04",
        "Under Indian law, although 'intention to create legal relations' is not expressly mentioned in Section 10, the Supreme Court has recognized it as an essential element in:",
        ["CWT v. Abdul Hussain (1979)", "Satyabrata Ghose v. Mugneeram Bangur (1954)", "Hadley v. Baxendale (1854)", "Mohori Bibee v. Dharmodas Ghose (1903)"],
        0, "A",
        "In CWT v. Abdul Hussain (1979), the Supreme Court affirmed that intention to create legal relations is an essential requirement under Indian contract law.",
        {"A": "Correct. CWT v. Abdul Hussain recognized the requirement under Indian law.", "B": "Satyabrata Ghose is the leading case on frustration (Section 56).", "C": "Hadley v. Baxendale is the leading English case on damages.", "D": "Mohori Bibee is the leading Privy Council case on minor's agreement."},
        "Hard", "Supreme Court: CWT v. Abdul Hussain (AIR 1979 SC 1832)", "Trace Indian Supreme Court adoption of legal relations test."
    ),
    (
        "mcq-cnt-01-031", "ch-cnt-01", "top-cnt-01-04",
        "A invites B to dinner at a restaurant, and B accepts the invitation. A incurs expenditure booking a table, but B fails to turn up. A sues B for damages. Can A recover?",
        ["Yes, because there was a valid offer, acceptance, and expenditure incurred", "No, because social invitations lack intention to create legal relations", "Yes, on the principle of promissory estoppel", "Yes, under quasi-contract Section 70"],
        1, "B",
        "Social agreements and dinner invitations are presumed to lack intention to enter into legal obligations; no legal action lies.",
        {"A": "Social agreements are non-justiciable for want of legal intent.", "B": "Correct. Purely social invitations do not create legal obligations.", "C": "Promissory estoppel cannot turn a social dinner into an actionable contract.", "D": "Section 70 requires lawful non-gratuitous acts done for another's benefit."},
        "Easy", "Common Law & Indian Jurisprudence", "Apply legal relations rule to social invitations."
    ),
    (
        "mcq-cnt-01-032", "ch-cnt-01", "top-cnt-01-04",
        "Which of the following tests is applied by courts to determine whether parties intended to create legal relations?",
        ["Subjective test of what the offeror privately thought", "Objective test of what a reasonable person would infer from the conduct and words of the parties", "Psychological evaluation of the parties", "Affidavit submitted by the plaintiff"],
        1, "B",
        "The test of intention to create legal relations is strictly objective: whether reasonable people considering the words and circumstances would conclude that a contract was intended.",
        {"A": "Subjective uncommunicated mental reservations are irrelevant.", "B": "Correct. An objective reasonable bystander test is applied.", "C": "Courts do not conduct psychological evaluations for contract intention.", "D": "Ex post facto self-serving affidavits cannot override objective conduct."},
        "Medium", "Smith v. Hughes (1871) LR 6 QB 597", "Identify objective test of intention."
    ),

    # CH-02: Consideration
    # top-cnt-02-01: Consideration Essentials, Types & Quid Pro Quo (Section 2(d)) - 8 MCQs
    (
        "mcq-cnt-02-001", "ch-cnt-02", "top-cnt-02-01",
        "Under Section 2(d) of the Indian Contract Act, consideration is defined as when, at the desire of the promisor, the promisee or any other person:",
        ["Has done or abstained from doing, or does or abstains from doing, or promises to do or to abstain from doing, something", "Suffers physical injury or loss", "Enters into a registered bond", "Pays money to a third party"],
        0, "A",
        "Section 2(d) defines consideration covering past, present, and future acts or abstinences done at the desire of the promisor.",
        {"A": "Correct. Verbatim definition under Section 2(d).", "B": "Detriment must be requested by promisor, not accidental physical injury.", "C": "Registration is not part of Section 2(d).", "D": "Payment to a third party is only consideration if desired by promisor."},
        "Easy", "Indian Contract Act, 1872, Section 2(d)", "Identify statutory definition of consideration."
    ),
    (
        "mcq-cnt-02-002", "ch-cnt-02", "top-cnt-02-01",
        "In Durga Prasad v. Baldeo (1880), the plaintiff built market shops at the desire of the District Collector. The shopkeeper defendants promised to pay commission on sales. The court held:",
        ["The promise was valid because plaintiff incurred expenditure", "The promise was void for want of consideration because the act was done at the Collector's desire, not at the desire of the promisors", "The promise was an enforceable quasi-contract", "The Collector became liable to pay the commission"],
        1, "B",
        "In Durga Prasad v. Baldeo, the Allahabad High Court held that an act done at the desire of a third party (Collector) is no consideration under Section 2(d).",
        {"A": "Expenditure not requested by promisor does not satisfy Section 2(d).", "B": "Correct. Consideration must move at the desire of the promisor.", "C": "No quasi-contractual claim lies against shopkeepers who did not request construction.", "D": "The Collector was acting in administrative capacity, incurring no liability."},
        "Medium", "Allahabad High Court: Durga Prasad v. Baldeo (1880) ILR 3 All 221", "Master 'desire of promisor' rule in Durga Prasad v Baldeo."
    ),
    (
        "mcq-cnt-02-003", "ch-cnt-02", "top-cnt-02-01",
        "In Kedarnath Bhattacharji v. Gorie Mahomed (1886), a subscriber promised to pay Rs 100 towards building a town hall, and the town commissioner entered into contracts with builders on the faith of the subscription. The Calcutta High Court held:",
        ["The subscriber was not liable as charitable subscriptions are gratuitous", "The subscriber was liable because entering into liabilities at the promisor's request constituted valid consideration", "The agreement was void under Section 25", "Only the government could enforce the subscription"],
        1, "B",
        "The Calcutta High Court held that incurring a liability or entering into building contracts on the faith of the promised subscription constitutes valid consideration.",
        {"A": "Pure promises to donate are unenforceable, but incurring liability changes the legal status.", "B": "Correct. Incurring liabilities on the faith of the promise made it enforceable.", "C": "Section 25 was overcome because consideration existed in the form of detriment.", "D": "The plaintiff town commissioner had locus standi to sue."},
        "Hard", "Calcutta High Court: Kedarnath v. Gorie Mahomed (1886) ILR 14 Cal 64", "Recall rule on subscription consideration in Kedarnath."
    ),
    (
        "mcq-cnt-02-004", "ch-cnt-02", "top-cnt-02-01",
        "In Abdul Aziz v. Masum Ali (1914), the defendant promised to subscribe Rs 500 for rebuilding a mosque, but no expenditure or liability was incurred on the faith of the promise before he backed out. The court held:",
        ["The defendant was liable to pay the subscription", "The agreement was a nudum pactum and unenforceable as no consideration moved from the promisee", "The committee was entitled to damages under Section 73", "The defendant was estopped from denying liability"],
        1, "B",
        "The Allahabad High Court held that a bare promise to subscribe to a charity without any detriment or liability incurred is nudum pactum and void.",
        {"A": "No liability attaches to a bare gratuitous promise.", "B": "Correct. In the absence of any act or liability incurred, the promise is nudum pactum.", "C": "No damages can be awarded for breach of an unenforceable promise.", "D": "Promissory estoppel cannot enforce a gratuitous promise where no reliance detriment occurred."},
        "Medium", "Allahabad High Court: Abdul Aziz v. Masum Ali (1914) ILR 36 All 268", "Distinguish Abdul Aziz from Kedarnath regarding consideration."
    ),
    (
        "mcq-cnt-02-005", "ch-cnt-02", "top-cnt-02-01",
        "Under Section 2(d) of the Indian Contract Act, which of the following forms of consideration is recognized in India?",
        ["Past consideration only", "Present (executed) consideration only", "Future (executory) consideration only", "Past, present, and future consideration"],
        3, "D",
        "The words 'has done or abstained' (past), 'does or abstains' (present), and 'promises to do or abstain' (future) in Section 2(d) recognize all three forms.",
        {"A": "Indian law recognizes more than just past consideration.", "B": "English common law rejects past consideration, but Indian law recognizes all three.", "C": "Executory consideration is only one of the recognized types.", "D": "Correct. Section 2(d) explicitly accommodates past, present, and future consideration."},
        "Easy", "Indian Contract Act, 1872, Section 2(d)", "Identify types of consideration under Section 2(d)."
    ),
    (
        "mcq-cnt-02-006", "ch-cnt-02", "top-cnt-02-01",
        "Under English law, past consideration is generally no consideration. Under Indian law, past consideration is:",
        ["Also no consideration whatsoever", "Valid consideration because Section 2(d) expressly includes 'has done or abstained from doing'", "Valid only if given by a minor", "Void as opposed to public policy"],
        1, "B",
        "Unlike English law, Section 2(d) of the Indian Contract Act expressly includes past acts done at the promisor's desire ('has done or abstained from doing').",
        {"A": "Incorrect; Indian law differs fundamentally from English law on this point.", "B": "Correct. Section 2(d) recognizes past acts done at the promisor's request as valid consideration.", "C": "Minors cannot provide valid consideration for a contract.", "D": "Past consideration is completely lawful in India."},
        "Medium", "Indian Contract Act, 1872, Section 2(d)", "Contrast Indian and English law on past consideration."
    ),
    (
        "mcq-cnt-02-007", "ch-cnt-02", "top-cnt-02-01",
        "Performance of an existing legal or public duty already imposed by law is:",
        ["Sufficient consideration to support a promise", "No consideration in the eyes of law", "Consideration only if done by a police officer", "Illegal consideration under Section 23"],
        1, "B",
        "Doing what one is already legally bound to do (public duty) is no consideration, as it offers no new legal benefit or detriment (Collins v. Godefroy).",
        {"A": "Pre-existing legal duty does not constitute good consideration.", "B": "Correct. Under Collins v. Godefroy, performance of an existing public duty is no consideration.", "C": "Police officers performing duty cannot claim private consideration.", "D": "It is not illegal per se, but it lacks consideration value."},
        "Medium", "Collins v. Godefroy (1831) 1 B & Ad 950", "Evaluate existing public duty as consideration."
    ),
    (
        "mcq-cnt-02-008", "ch-cnt-02", "top-cnt-02-01",
        "Under Explanation 2 to Section 25 of the Indian Contract Act, the inadequacy of consideration:",
        ["Renders the agreement void per se", "May be taken into account by the court in determining whether consent was freely given", "Is irrelevant even if fraud is alleged", "Converts the agreement into a criminal offence"],
        1, "B",
        "Explanation 2 to Section 25: An agreement is not void merely because consideration is inadequate, but inadequacy may be considered in determining free consent.",
        {"A": "Consideration need not be adequate to form a valid contract.", "B": "Correct. Inadequacy is evidentiary material for testing free consent.", "C": "Courts will examine inadequacy where fraud or undue influence is raised.", "D": "Inadequacy has no criminal consequences."},
        "Medium", "Indian Contract Act, 1872, Section 25 Explanation 2", "Apply Explanation 2 to Section 25 on inadequacy."
    ),

    # top-cnt-02-02: Privity of Contract vs Privity of Consideration & Exceptions - 8 MCQs
    (
        "mcq-cnt-02-009", "ch-cnt-02", "top-cnt-02-02",
        "Under Section 2(d) of the Indian Contract Act, consideration may move from:",
        ["The promisee only", "The promisee or any other person", "The promisor only", "A court of competent jurisdiction"],
        1, "B",
        "Section 2(d) uses the phrase 'the promisee or any other person', establishing that consideration need not move from the promisee alone.",
        {"A": "This represents the strict English common law rule, not Indian law.", "B": "Correct. In India, consideration may move from the promisee or any other person.", "C": "Consideration is given to the promisor, not moving from the promisor.", "D": "Courts do not supply consideration."},
        "Easy", "Indian Contract Act, 1872, Section 2(d)", "Identify from whom consideration may move under Indian law."
    ),
    (
        "mcq-cnt-02-010", "ch-cnt-02", "top-cnt-02-02",
        "In the landmark decision Chinnaya v. Ramayya (1882), an old lady gifted property to her daughter directing her to pay an annuity to the maternal uncle. When the daughter refused, the Madras High Court held:",
        ["The uncle could not sue because he was a stranger to the consideration", "The uncle could sue because under Section 2(d) consideration may move from 'any other person' (the mother)", "The agreement was void under Section 25", "The gift was revoked by operation of law"],
        1, "B",
        "In Chinnaya v. Ramayya, the Madras High Court held that a stranger to consideration can sue under Indian law because consideration moved from the mother.",
        {"A": "Stranger to consideration can enforce a contract in India, unlike in England.", "B": "Correct. Section 2(d) allows consideration to move from 'any other person'.", "C": "The agreement was fully supported by consideration moving from the donor.", "D": "The gift deed remained valid and binding."},
        "Medium", "Madras High Court: Chinnaya v. Ramayya (1882) ILR 4 Mad 137", "Master Chinnaya v Ramayya on stranger to consideration."
    ),
    (
        "mcq-cnt-02-011", "ch-cnt-02", "top-cnt-02-02",
        "In English law, under Tweddle v. Atkinson (1861) and Dunlop Pneumatic Tyre Co. v. Selfridge & Co. (1915):",
        ["Consideration must move from the promisee, and a stranger to contract cannot sue", "A stranger to consideration can always sue", "Privity of contract does not exist", "Third-party beneficiaries have absolute rights of suit"],
        0, "A",
        "English law strictly adheres to both rules: consideration must move from the promisee, and only a party to the contract can sue on it.",
        {"A": "Correct. English common law requires consideration to move from promisee and enforces strict privity.", "B": "English law rejects suits by strangers to consideration.", "C": "Privity of contract is a cornerstone of English common law.", "D": "Third parties had no rights at common law prior to the 1999 statute."},
        "Medium", "Tweddle v. Atkinson (1861); Dunlop v. Selfridge (1915) AC 847", "Contrast Indian and English rules on privity of consideration."
    ),
    (
        "mcq-cnt-02-012", "ch-cnt-02", "top-cnt-02-02",
        "In MC Chacko v. State Bank of Travancore (AIR 1970 SC 2059), the Supreme Court affirmed that under Indian law:",
        ["A person who is not a party to a contract cannot, subject to certain well-recognized exceptions, enforce the contract", "Anyone for whose benefit a contract is made can sue, without any exceptions", "Privity of contract does not apply in India at all", "Only banks can sue third parties"],
        0, "A",
        "The Supreme Court held in MC Chacko that the doctrine of privity of contract applies in India: a stranger to a contract cannot sue, subject to recognized exceptions.",
        {"A": "Correct. Privity of contract applies in India, distinguishing it from privity of consideration.", "B": "Third-party beneficiaries cannot sue unless falling within recognized exceptions.", "C": "Privity of contract does apply in India.", "D": "No special statutory exemption for banks existed on this principle."},
        "Hard", "Supreme Court: MC Chacko v. State Bank of Travancore (AIR 1970 SC 2059)", "Affirm privity of contract in India under MC Chacko."
    ),
    (
        "mcq-cnt-02-013", "ch-cnt-02", "top-cnt-02-02",
        "Which of the following is a recognized exception to the doctrine of privity of contract in India?",
        ["Beneficiaries under a trust or charge created in their favor", "Family or marriage settlements providing maintenance or expenses", "Estoppel, acknowledgment, or agency", "All of the above"],
        3, "D",
        "Recognized exceptions include trusts/charges (Khwaja Muhammad v. Husaini Begam), marriage/family settlements (Daropti v. Jaspat Rai), and acknowledgment/estoppel.",
        {"A": "Trust beneficiaries can enforce obligations created for their benefit.", "B": "Family/marriage settlements are well-settled exceptions.", "C": "Acknowledgment or estoppel creates direct liability to third party.", "D": "Correct. All of the listed situations are recognized exceptions to privity of contract."},
        "Medium", "Indian Contract Jurisprudence", "Identify recognized exceptions to privity of contract."
    ),
    (
        "mcq-cnt-02-014", "ch-cnt-02", "top-cnt-02-02",
        "In Khwaja Muhammad Khan v. Husaini Begam (1910), a father-in-law agreed with the bride's father to pay her 'Kharch-i-pandan' (betel-box expenses) charged on specific immovable property. The Privy Council held:",
        ["The bride could not sue as she was not a party to the agreement", "The bride was entitled to enforce the agreement as a charge/trust was created in her favor", "The agreement was void as a marriage brokage contract", "Only the bride's father could claim damages"],
        1, "B",
        "The Privy Council held that although the bride was not a party to the contract, an express charge had been created on property for her benefit, entitling her to sue.",
        {"A": "The Privy Council specifically rejected the application of English privity to Indian conditions here.", "B": "Correct. She was entitled to sue as beneficiary of a specific property charge.", "C": "Kharch-i-pandan is a customary pin-money allowance, not marriage brokage.", "D": "The bride herself was granted decree to enforce the payment."},
        "Hard", "Privy Council: Khwaja Muhammad Khan v. Husaini Begam (1910) 37 IA 152", "Analyze Khwaja Muhammad Khan trust/charge exception."
    ),
    (
        "mcq-cnt-02-015", "ch-cnt-02", "top-cnt-02-02",
        "What is the fundamental difference between 'privity of contract' and 'privity of consideration' under Indian law?",
        ["India accepts privity of consideration but rejects privity of contract", "India rejects privity of consideration (stranger to consideration can sue) but accepts privity of contract (stranger to contract generally cannot sue)", "Both privities are completely rejected in India", "Both privities are strictly enforced without exceptions"],
        1, "B",
        "Under Section 2(d), consideration may move from any other person (no privity of consideration), but only parties to the contract can enforce it (privity of contract applies).",
        {"A": "Reversed; legally inaccurate.", "B": "Correct. Stranger to consideration can sue, but stranger to contract generally cannot.", "C": "Privity of contract is firmly applied by the Supreme Court.", "D": "Both doctrines have distinct treatments and exceptions in Indian law."},
        "Hard", "Indian Contract Act, 1872, Section 2(d) & MC Chacko", "Synthesize distinction between privity of contract and consideration."
    ),
    (
        "mcq-cnt-02-016", "ch-cnt-02", "top-cnt-02-02",
        "Where A acknowledges to C that he holds money received from B for the use of C, A is liable to C on the ground of:",
        ["Promissory estoppel / Acknowledgment", "Subrogation", "Novation of contract", "Vicarious liability"],
        0, "A",
        "Where a promisor acknowledges to a third party or conducts himself as an agent for that third party, privity is overcome by estoppel/acknowledgment.",
        {"A": "Correct. Acknowledgment creates an obligation through estoppel.", "B": "Subrogation is substitution of one creditor for another in insurance/suretyship.", "C": "Novation requires agreement between all three parties to replace the contract.", "D": "Vicarious liability applies to torts of servants, not contractual acknowledgment."},
        "Medium", "Common Law & Indian Contract Principles", "Understand acknowledgment/estoppel exception to privity."
    ),

    # top-cnt-02-03: Agreements Without Consideration & Section 25 Exceptions - 8 MCQs
    (
        "mcq-cnt-02-017", "ch-cnt-02", "top-cnt-02-03",
        "Under Section 25 of the Indian Contract Act, the general rule is that an agreement made without consideration is:",
        ["Voidable", "Void", "Valid", "Illegal"],
        1, "B",
        "Section 25 opens with the general rule: 'An agreement made without consideration is void, unless...'. This is the Latin maxim ex nudo pacto non oritur actio.",
        {"A": "Voidable contracts are enforceable at one party's option; lack of consideration makes it void.", "B": "Correct. Section 25 declares agreements without consideration void.", "C": "Valid only if falling under the three statutory exceptions.", "D": "Lack of consideration is not a crime or illegal act under Section 23."},
        "Easy", "Indian Contract Act, 1872, Section 25", "Recall general rule of Section 25 on consideration."
    ),
    (
        "mcq-cnt-02-018", "ch-cnt-02", "top-cnt-02-03",
        "Under Section 25(1) of the Indian Contract Act, an agreement without consideration is valid if it is:",
        ["Expressed in writing, registered under law, made on account of natural love and affection, between parties standing in near relation to each other", "Made orally before village elders on account of natural love and affection", "Expressed in writing and attested by two witnesses", "Entered into between business partners"],
        0, "A",
        "Section 25(1) requires four cumulative conditions: (1) writing, (2) registered, (3) natural love and affection, and (4) near relation.",
        {"A": "Correct. All four statutory requirements under Section 25(1) must be fulfilled.", "B": "Oral agreements do not qualify under Section 25(1); writing and registration are mandatory.", "C": "Attestation is not enough; registration under the law is compulsory.", "D": "Business partners do not typically satisfy natural love and affection between near relations."},
        "Easy", "Indian Contract Act, 1872, Section 25(1)", "Identify essentials of Section 25(1) exception."
    ),
    (
        "mcq-cnt-02-019", "ch-cnt-02", "top-cnt-02-03",
        "In Rajlukhy Dabee v. Bhootnath Mookerjee (1900), a husband executed a registered agreement to pay maintenance to his wife after near relations quarreled. The Calcutta High Court held:",
        ["The agreement was enforceable under Section 25(1)", "The agreement was void because it was executed due to quarrels and discord, not out of natural love and affection", "The agreement was a valid family settlement", "The wife was entitled to half the husband's property"],
        1, "B",
        "The court held that although in writing, registered, and between near relations, the agreement was born of quarrels, so natural love and affection was absent.",
        {"A": "The court dismissed the wife's claim under Section 25(1).", "B": "Correct. Near relation alone is insufficient; natural love and affection must actually exist.", "C": "No family settlement exception was established.", "D": "No property partition decree was passed."},
        "Medium", "Calcutta High Court: Rajlukhy Dabee v. Bhootnath Mookerjee (1900) 4 CWN 488", "Analyze natural love and affection requirement in Rajlukhy Dabee."
    ),
    (
        "mcq-cnt-02-020", "ch-cnt-02", "top-cnt-02-03",
        "Under Section 25(2) of the Indian Contract Act, an agreement without consideration is valid if it is a promise to compensate:",
        ["A person who has already voluntarily done something for the promisor, or something which the promisor was legally compellable to do", "A person who promises to do future work without pay", "A stranger for entering into an illegal trade", "A public officer for performing his statutory duty"],
        0, "A",
        "Section 25(2) validates a promise to compensate wholly or in part a person who has already voluntarily done something for the promisor.",
        {"A": "Correct. Section 25(2) covers compensation for past voluntary services.", "B": "Future gratuitous work does not fall under Section 25(2).", "C": "Illegal transactions cannot be saved by Section 25(2).", "D": "Public officers cannot take private compensation for statutory duties."},
        "Medium", "Indian Contract Act, 1872, Section 25(2)", "Identify scope of past voluntary service under Section 25(2)."
    ),
    (
        "mcq-cnt-02-021", "ch-cnt-02", "top-cnt-02-03",
        "Under Section 25(3) of the Indian Contract Act, a promise to pay a time-barred debt is valid if:",
        ["It is made orally before two respectable witnesses", "It is made in writing and signed by the person to be charged therewith, or by his authorized agent", "The debtor deposits 10% in court", "The debt is not older than 12 years"],
        1, "B",
        "Section 25(3) requires that the promise to pay a debt barred by limitation must be made in writing and signed by the debtor or his authorized agent.",
        {"A": "Oral promises cannot revive a time-barred debt under Section 25(3).", "B": "Correct. Writing and signature are mandatory statutory requirements under Section 25(3).", "C": "Court deposit is not a statutory prerequisite.", "D": "Section 25(3) does not impose a 12-year restriction on reviving barred debts."},
        "Easy", "Indian Contract Act, 1872, Section 25(3)", "Master requirements of time-barred debt revival."
    ),
    (
        "mcq-cnt-02-022", "ch-cnt-02", "top-cnt-02-03",
        "Under Explanation 1 to Section 25 of the Indian Contract Act, nothing in Section 25 shall affect the validity of:",
        ["Any gift actually made between donor and donee", "Any agreement in restraint of trade", "Any wagering contract", "Any marriage brokage agreement"],
        0, "A",
        "Explanation 1 to Section 25 states: 'Nothing in this section shall affect the validity, as between the donor and donee, of any gift actually made'.",
        {"A": "Correct. Completed gifts need no consideration under Explanation 1.", "B": "Agreements in restraint of trade are void under Section 27.", "C": "Wagers are void under Section 30.", "D": "Marriage brokage is void as against public policy under Section 23."},
        "Easy", "Indian Contract Act, 1872, Section 25 Explanation 1", "Recall exception for completed gifts under Section 25."
    ),
    (
        "mcq-cnt-02-023", "ch-cnt-02", "top-cnt-02-03",
        "A finds B's purse on the road and gives it to him. B, in gratitude, promises to give A Rs 500. This agreement is:",
        ["Void for want of consideration", "Valid and enforceable under Section 25(2)", "Voidable at the option of B", "Illegal"],
        1, "B",
        "Under Section 25(2) and Illustration (c) to Section 25, A did something voluntarily for B, and B's subsequent promise to compensate him is a valid contract.",
        {"A": "Section 25(2) creates an express statutory exception for past voluntary service.", "B": "Correct. Exactly matches Illustration (c) to Section 25 of the Act.", "C": "It is not voidable; it is a valid binding contract.", "D": "Returning a lost purse is completely lawful and commendable."},
        "Medium", "Indian Contract Act, 1872, Section 25 Illustration (c)", "Apply Section 25(2) to finder of lost goods scenario."
    ),
    (
        "mcq-cnt-02-024", "ch-cnt-02", "top-cnt-02-03",
        "A owes B Rs 1,000, but the debt is barred by the Limitation Act. A signs a written promise to pay B Rs 500 on account of the debt. Under Section 25(3), this is:",
        ["A void agreement because the whole debt is not promised", "A valid contract to pay Rs 500", "An unenforceable moral obligation", "Voidable at the option of A"],
        1, "B",
        "Under Illustration (e) to Section 25, a signed written promise to pay the whole or any part of a time-barred debt is a valid contract.",
        {"A": "A promise to pay 'wholly or in part' is expressly authorized under Section 25(3).", "B": "Correct. Section 25(3) and Illustration (e) explicitly validate paying part of a barred debt.", "C": "The written signed promise converts the moral debt into a legal contract.", "D": "It is fully binding, not voidable."},
        "Medium", "Indian Contract Act, 1872, Section 25 Illustration (e)", "Apply Section 25(3) to part-payment of barred debt."
    )
]

print(f"Total raw MCQs in part 1: {len(raw_items)}")
