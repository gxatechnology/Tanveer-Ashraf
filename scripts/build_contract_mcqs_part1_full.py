# Complete Contract MCQs Part 1 Builder (Chapters 1 to 4: 112 MCQs)
import json

def make_mcq(q_id, ch_id, top_id, q_text, options, ans_idx, ans_letter, explanation, breakdown, diff, provision, objective):
    return {
        "id": q_id,
        "subjectId": "law-contract",
        "chapterId": ch_id,
        "topicId": top_id,
        "question": q_text,
        "options": options,
        "answer": ans_idx,
        "answerLetter": ans_letter,
        "explanation": explanation,
        "optionBreakdown": breakdown,
        "difficulty": diff,
        "provision": provision,
        "sourceUrl": "https://legislative.gov.in",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": objective,
        "eligible": True,
        "status": "active"
    }

mcqs = []

# ==========================================
# CHAPTER 1: FORMATION OF CONTRACT (32 MCQs)
# ==========================================
# top-cnt-01-01: Agreement and Contract (Section 2(h) & Section 10 Essentials) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-01-001", "ch-cnt-01", "top-cnt-01-01",
    "Under Section 2(h) of the Indian Contract Act, 1872, a contract is defined as:",
    ["An agreement between two competent parties", "An agreement enforceable by law", "A promise supported by consideration", "An accepted proposal"],
    1, "B",
    "Section 2(h) provides that 'an agreement enforceable by law is a contract'.",
    {"A": "Enforceability by law is the crucial defining element in Section 2(h).", "B": "Correct. Section 2(h) defines contract as an agreement enforceable by law.", "C": "This describes consideration under Section 2(d).", "D": "This describes an agreement under Section 2(e)."},
    "Easy", "Indian Contract Act, 1872, Section 2(h)", "Master statutory definition of contract."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-002", "ch-cnt-01", "top-cnt-01-01",
    "According to Section 10 of the Indian Contract Act, all agreements are contracts if they are made by:",
    ["Free consent of parties competent to contract, for lawful consideration and lawful object, and not expressly declared void", "Parties of sound mind with written execution before a notary", "Mutual assent and registered with a sub-registrar", "Two parties having identical nationality"],
    0, "A",
    "Section 10 lists essentials: free consent of parties competent to contract, lawful consideration, lawful object, and not expressly declared void.",
    {"A": "Correct. Section 10 sets out the core statutory ingredients of valid contracts.", "B": "Notarization is not a universal requirement under Section 10.", "C": "Registration is only required for specific contracts under special statutes.", "D": "Nationality is irrelevant to competency under Section 10."},
    "Easy", "Indian Contract Act, 1872, Section 10", "Identify core statutory essentials under Section 10."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-003", "ch-cnt-01", "top-cnt-01-01",
    "Which of the following statements correctly represents the relationship between an agreement and a contract?",
    ["Every contract is an agreement, but every agreement is not necessarily a contract", "Every agreement is a contract, but every contract is not an agreement", "Agreement and contract are synonymous terms under Indian law", "An agreement is always enforceable in a court of law"],
    0, "A",
    "Agreement is the genus (Section 2(e)) while contract is the species (Section 2(h)). Only agreements enforceable by law become contracts.",
    {"A": "Correct. All contracts are agreements, but only legally enforceable agreements are contracts.", "B": "Reversed statement; legally incorrect.", "C": "Distinct statutory concepts under Sections 2(e) and 2(h).", "D": "Agreements such as social, domestic, or void agreements are unenforceable."},
    "Medium", "Indian Contract Act, 1872, Sections 2(e), 2(h)", "Distinguish legal scope of agreement and contract."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-004", "ch-cnt-01", "top-cnt-01-01",
    "Under Section 2(e) of the Indian Contract Act, every promise and every set of promises, forming the consideration for each other, is an:",
    ["Offer", "Agreement", "Acceptance", "Executed contract"],
    1, "B",
    "Section 2(e) defines agreement as 'every promise and every set of promises, forming the consideration for each other'.",
    {"A": "Offer is defined under Section 2(a).", "B": "Correct. Section 2(e) explicitly defines an agreement.", "C": "Acceptance is defined under Section 2(b).", "D": "An executed contract requires completed performance and enforceability."},
    "Easy", "Indian Contract Act, 1872, Section 2(e)", "Recall statutory definition of agreement."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-005", "ch-cnt-01", "top-cnt-01-01",
    "An agreement not enforceable by law is said to be:",
    ["Voidable", "Void", "Illegal", "Unenforceable but valid"],
    1, "B",
    "Section 2(g) of the Indian Contract Act states: 'An agreement not enforceable by law is said to be void'.",
    {"A": "Voidable agreements are enforceable at option of one party under Section 2(i).", "B": "Correct. Section 2(g) defines void agreements as those unenforceable by law.", "C": "Illegal agreements involve statutory prohibitions or criminal elements.", "D": "Unenforceable due to technical defects is distinct from void ab initio."},
    "Easy", "Indian Contract Act, 1872, Section 2(g)", "Identify void agreements under Section 2(g)."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-006", "ch-cnt-01", "top-cnt-01-01",
    "An agreement enforceable by law at the option of one or more of the parties thereto, but not at the option of the other or others, is a:",
    ["Void agreement", "Voidable contract", "Contingent contract", "Quasi-contract"],
    1, "B",
    "Section 2(i) defines voidable contract as an agreement enforceable by law at option of one or more parties, but not at option of other(s).",
    {"A": "Void agreements are unenforceable by either party (Section 2(g)).", "B": "Correct. Section 2(i) defines a voidable contract.", "C": "Contingent contracts depend on happening of uncertain collateral events (Section 31).", "D": "Quasi-contracts are obligations created by law without agreement (Sections 68-72)."},
    "Easy", "Indian Contract Act, 1872, Section 2(i)", "Distinguish voidable contract under Section 2(i)."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-007", "ch-cnt-01", "top-cnt-01-01",
    "A contract which ceases to be enforceable by law becomes void when it:",
    ["Is formed without writing", "Ceases to be enforceable", "Is entered into by a minor", "Is registered under the Registration Act"],
    1, "B",
    "Section 2(j) provides: 'A contract which ceases to be enforceable by law becomes void when it ceases to be enforceable'.",
    {"A": "Oral contracts can be completely valid under Section 10.", "B": "Correct. Section 2(j) governs contracts that become void subsequent to formation.", "C": "A minor's agreement is void ab initio, never becoming a valid contract first.", "D": "Registration does not render a contract void."},
    "Medium", "Indian Contract Act, 1872, Section 2(j)", "Apply Section 2(j) on contracts becoming void."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-008", "ch-cnt-01", "top-cnt-01-01",
    "Which of the following is NOT an essential element of a valid contract under Section 10 of the Indian Contract Act?",
    ["Free consent of parties", "Adequacy of consideration", "Competency of parties", "Lawful object and consideration"],
    1, "B",
    "Explanation 2 to Section 25 clearly establishes that consideration need not be adequate; an agreement is not void merely because consideration is inadequate.",
    {"A": "Free consent is an essential element under Section 10 and Section 14.", "B": "Correct. Adequacy of consideration is not required; it only needs to have legal value.", "C": "Competency is an essential element under Section 10 and Section 11.", "D": "Lawful object and consideration are essential under Section 10 and Section 23."},
    "Medium", "Indian Contract Act, 1872, Sections 10, 25", "Evaluate consideration adequacy requirement."
))

# top-cnt-01-02: Offer / Proposal: Essentials & Offer vs Invitation to Treat (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-01-009", "ch-cnt-01", "top-cnt-01-02",
    "Under Section 2(a) of the Indian Contract Act, a proposal is made when a person signifies to another:",
    ["A desire to enter negotiations", "His willingness to do or to abstain from doing anything, with a view to obtaining the assent of that other", "An invitation to receive tenders", "A conditional statement of price"],
    1, "B",
    "Section 2(a) defines proposal: when one person signifies to another willingness to do/abstain with a view to obtaining assent of the other.",
    {"A": "Negotiations precede a proposal and lack final assent-seeking intention.", "B": "Correct. Statutory definition under Section 2(a).", "C": "Invitation to tender is an invitation to offer, not a proposal.", "D": "Quotation of price without assent-seeking intent is an invitation to treat."},
    "Easy", "Indian Contract Act, 1872, Section 2(a)", "Analyze definition of proposal under Section 2(a)."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-010", "ch-cnt-01", "top-cnt-01-02",
    "In the landmark Privy Council decision Harvey v. Facey (1893), telegraphing the lowest cash price of 'Bumper Hall Pen' was held to be:",
    ["An unconditional offer to sell", "A mere statement of lowest price (invitation to treat), not an offer", "An implied acceptance of plaintiff's offer", "A counter-proposal binding on the sender"],
    1, "B",
    "In Harvey v. Facey, the Privy Council held that quoting the lowest price was merely supplying information/invitation to treat, not an offer to sell.",
    {"A": "The court expressly rejected that quoting price constituted an offer to sell.", "B": "Correct. A quotation of minimum price is an invitation to treat.", "C": "Acceptance requires unequivocal assent, which was absent.", "D": "It was not a counter-proposal because no offer had been made."},
    "Medium", "Privy Council: Harvey v. Facey (1893) AC 552", "Distinguish offer from quotation of price in Harvey v Facey."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-011", "ch-cnt-01", "top-cnt-01-02",
    "In Pharmaceutical Society of Great Britain v. Boots Cash Chemists (1953), display of goods with price tags on a self-service shelf was held to be:",
    ["A binding standing offer to the public", "An invitation to treat", "A completed sale upon picking up the item", "A unilateral contract"],
    1, "B",
    "The English Court of Appeal held that display of goods in a shop is an invitation to treat; the customer makes the offer at the cash register.",
    {"A": "Goods display is not a binding offer to the public.", "B": "Correct. Shelf display with prices is an invitation to treat.", "C": "Sale is completed only when cashier accepts the customer's offer at the till.", "D": "Unilateral contracts require full performance of stipulated conditions."},
    "Medium", "Pharmaceutical Society of Great Britain v. Boots Cash Chemists (1953) 1 QB 401", "Identify legal nature of shelf display in shops."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-012", "ch-cnt-01", "top-cnt-01-02",
    "In Carlill v. Carbolic Smoke Ball Co. (1893), the advertisement offering £100 reward to anyone contracting influenza after using the smoke ball was held to be:",
    ["An invitation to treat", "A general offer made to the whole world, accepted by performance of conditions", "A void wagering agreement", "A void agreement due to uncertainty"],
    1, "B",
    "In Carlill v. Carbolic Smoke Ball Co., the court held that an offer can be made to the whole world, and notification of acceptance is dispensed with upon performance.",
    {"A": "The deposit of £1,000 in Alliance Bank showed clear intention to be bound, making it an offer.", "B": "Correct. It was a valid general offer accepted by performing the prescribed conditions.", "C": "It was not a wager because plaintiff had an interest in using the product.", "D": "The terms were sufficiently certain to form a binding contract."},
    "Medium", "Carlill v. Carbolic Smoke Ball Co. (1893) 1 QB 256", "Apply general offer doctrine in Carlill case."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-013", "ch-cnt-01", "top-cnt-01-02",
    "Under Section 8 of the Indian Contract Act, performance of the conditions of a proposal is an:",
    ["Invitation to make a counter-offer", "Acceptance of the proposal", "Impossibility of performance", "Revocation of the proposal"],
    1, "B",
    "Section 8 provides: 'Performance of the conditions of a proposal, or the acceptance of any consideration for a reciprocal promise... is an acceptance of the proposal'.",
    {"A": "Performance indicates acceptance, not counter-proposal.", "B": "Correct. Section 8 codifies acceptance by performing conditions.", "C": "Performance is the opposite of impossibility.", "D": "Performance solidifies contract formation rather than revocation."},
    "Easy", "Indian Contract Act, 1872, Section 8", "Understand acceptance by performance under Section 8."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-014", "ch-cnt-01", "top-cnt-01-02",
    "In Lalman Shukla v. Gauri Dutt (1913), the servant who traced the missing nephew without knowledge of the announced reward was held:",
    ["Entitled to the reward because he performed the condition", "Not entitled to the reward because an offer cannot be accepted without knowledge of its existence", "Entitled to half the reward on quantum meruit", "Entitled to damages for breach of trust"],
    1, "B",
    "The Allahabad High Court held that an offer cannot be accepted in ignorance of its existence; assent requires mutual communication and awareness.",
    {"A": "Performance without knowledge of offer does not constitute valid acceptance.", "B": "Correct. Lalman Shukla established that knowledge of the offer is essential for acceptance.", "C": "Quantum meruit is inapplicable where no contractual relationship exists.", "D": "No trust relationship was created regarding the reward."},
    "Hard", "Lalman Shukla v. Gauri Dutt (1913) 11 ALJ 489", "Recall rule on knowledge of offer in Lalman Shukla."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-015", "ch-cnt-01", "top-cnt-01-02",
    "Which of the following is generally considered an 'invitation to offer' rather than a valid proposal?",
    ["A catalogue of books listing titles and prices", "An announcement of auction sale", "A tender notice inviting quotations", "All of the above"],
    3, "D",
    "Catalogues, auction notices, and tender notices are all invitations to treat/invitations to make offers, not definitive offers.",
    {"A": "A price catalogue is an invitation to treat.", "B": "An auction notice is an invitation to prospective bidders to attend and make bids.", "C": "A tender notice invites contractors to submit offers.", "D": "Correct. All listed items constitute invitations to treat."},
    "Medium", "Indian Contract Act, 1872, Section 2(a)", "Distinguish invitations to offer from proposals."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-016", "ch-cnt-01", "top-cnt-01-02",
    "A counter-offer made in response to an original proposal has the legal effect of:",
    ["Suspending the original offer until further notice", "Rejecting and terminating the original offer", "Accepting the original offer conditionally", "Binding the original offeror unconditionally"],
    1, "B",
    "Under Hyde v. Wrench (1840), a counter-offer amounts to a rejection of the original offer, extinguishing it so it cannot subsequently be accepted.",
    {"A": "A counter-offer does not suspend; it destroys the original offer.", "B": "Correct. Under Hyde v. Wrench, a counter-offer terminates the original proposal.", "C": "Conditional acceptance is itself a counter-offer, not an acceptance.", "D": "An offeror is never bound by an unaccepted or counter-offered proposal."},
    "Medium", "Hyde v. Wrench (1840) 3 Beav 334", "Analyze legal effect of a counter-offer."
))

# top-cnt-01-03: Acceptance, Postal Rule & Revocation (Sections 3–9) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-01-017", "ch-cnt-01", "top-cnt-01-03",
    "Under Section 2(b) of the Indian Contract Act, when the person to whom the proposal is made signifies his assent thereto, the proposal is said to be accepted. A proposal, when accepted, becomes a:",
    ["Contract", "Promise", "Warranty", "Condition precedent"],
    1, "B",
    "Section 2(b) explicitly provides: 'A proposal, when accepted, becomes a promise'.",
    {"A": "An accepted proposal becomes a promise; it becomes a contract only when supported by consideration and enforceable.", "B": "Correct. Under Section 2(b), an accepted proposal becomes a promise.", "C": "Warranty is a collateral stipulation in Sale of Goods.", "D": "Condition precedent is a preliminary prerequisite for obligation."},
    "Easy", "Indian Contract Act, 1872, Section 2(b)", "Identify statutory result of accepted proposal."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-018", "ch-cnt-01", "top-cnt-01-03",
    "Under Section 7 of the Indian Contract Act, in order to convert a proposal into a promise, the acceptance must be:",
    ["Absolute and unqualified", "Expressed in some usual and reasonable manner, unless the proposal prescribes the manner", "Both A and B", "Neither A nor B"],
    2, "C",
    "Section 7 requires acceptance to be absolute and unqualified, and expressed in some usual and reasonable manner unless prescribed.",
    {"A": "Section 7(1) requires absolute and unqualified acceptance.", "B": "Section 7(2) requires usual and reasonable manner unless prescribed.", "C": "Correct. Both clauses (1) and (2) of Section 7 are statutory requirements.", "D": "Incorrect as both A and B are mandatory statutory requirements."},
    "Easy", "Indian Contract Act, 1872, Section 7", "Master requirements of acceptance under Section 7."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-019", "ch-cnt-01", "top-cnt-01-03",
    "Under Section 4 of the Indian Contract Act, the communication of an acceptance is complete as against the proposer when:",
    ["It comes to the actual knowledge of the proposer", "It is put in a course of transmission to him, so as to be out of the power of the acceptor", "It is written and signed by the acceptor", "The acceptor posts a registered receipt"],
    1, "B",
    "Section 4 paragraph 2: Communication of acceptance is complete against the proposer when put in course of transmission out of the power of acceptor.",
    {"A": "Actual knowledge completes acceptance as against the acceptor, not the proposer.", "B": "Correct. As against proposer, acceptance is complete upon posting (course of transmission).", "C": "Signing without transmission is not communication.", "D": "Receipt is not required; putting in transmission suffices."},
    "Hard", "Indian Contract Act, 1872, Section 4", "Distinguish communication completion points under Section 4."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-020", "ch-cnt-01", "top-cnt-01-03",
    "Under Section 4 of the Indian Contract Act, the communication of an acceptance is complete as against the acceptor when:",
    ["It is put into the post office", "It comes to the knowledge of the proposer", "The proposer replies with an acknowledgment", "The contract is registered"],
    1, "B",
    "Section 4 states that communication of acceptance is complete as against the acceptor when it comes to the knowledge of the proposer.",
    {"A": "Posting completes acceptance against proposer, not against acceptor.", "B": "Correct. As against acceptor, communication is complete when it reaches proposer's knowledge.", "C": "Proposer's reply is unnecessary for contract completion.", "D": "Registration is irrelevant to Section 4 postal rules."},
    "Medium", "Indian Contract Act, 1872, Section 4", "Analyze when acceptance binds the acceptor."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-021", "ch-cnt-01", "top-cnt-01-03",
    "In Bhagwandas Goverdhandas Kedia v. Girdharilal Parshottamdas & Co. (AIR 1966 SC 543), the Supreme Court held that in contracts negotiated by telephone or telex:",
    ["The postal rule under Section 4 applies and contract is formed where acceptance is spoken", "The contract is complete only when acceptance is heard and received by the offeror, at the offeror's place", "No contract is formed unless confirmed in writing within 24 hours", "The contract is formed halfway between the two parties"],
    1, "B",
    "The Supreme Court held that instantaneous communications (phone/telex) fall outside the postal rule; contract is complete where acceptance is heard by offeror (Entores rule).",
    {"A": "The postal rule applies only to non-instantaneous post, not telephone.", "B": "Correct. For instantaneous communication, contract is made where acceptance is received.", "C": "Written confirmation is not a legal prerequisite.", "D": "Fictional concept rejected in law."},
    "Hard", "Supreme Court: Bhagwandas v. Girdharilal (AIR 1966 SC 543)", "Apply instantaneous communication rule in Bhagwandas case."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-022", "ch-cnt-01", "top-cnt-01-03",
    "In Felthouse v. Bindley (1862), the uncle wrote offering to buy his nephew's horse, stating 'If I hear no more about him, I consider the horse mine'. The court held:",
    ["Silence constituted valid acceptance because the nephew intended to sell", "Mental acceptance or silence cannot be imposed as a mode of acceptance without communication", "A valid contract was formed upon the nephew telling the auctioneer not to sell", "The auctioneer became personally liable to the uncle"],
    1, "B",
    "Felthouse v. Bindley established that an offeror cannot impose silence as acceptance; acceptance must be positively communicated to the offeror.",
    {"A": "Subjective intent without communication does not form a binding contract.", "B": "Correct. Silence cannot amount to valid acceptance.", "C": "Internal instructions to auctioneer did not constitute communication to the uncle.", "D": "The auctioneer was held not liable to uncle because no property had passed."},
    "Medium", "Felthouse v. Bindley (1862) 11 CB (NS) 869", "Recall rule on silence and acceptance in Felthouse v Bindley."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-023", "ch-cnt-01", "top-cnt-01-03",
    "Under Section 5 of the Indian Contract Act, a proposal may be revoked at any time:",
    ["Before the communication of its acceptance is complete as against the proposer, but not afterwards", "Before the communication of its acceptance is complete as against the acceptor", "Within 30 days of making the proposal", "Until consideration is actually paid"],
    0, "A",
    "Section 5 paragraph 1: 'A proposal may be revoked at any time before the communication of its acceptance is complete as against the proposer, but not afterwards'.",
    {"A": "Correct. Proposer can revoke anytime before acceptance is posted/transmitted.", "B": "Against acceptor is the deadline for acceptor's revocation, not proposer's.", "C": "No arbitrary 30-day statutory time limit exists.", "D": "Payment of consideration is not the benchmark for revocation."},
    "Medium", "Indian Contract Act, 1872, Section 5", "Identify time limit for revocation of proposal."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-024", "ch-cnt-01", "top-cnt-01-03",
    "Under Section 5 of the Indian Contract Act, an acceptance may be revoked at any time:",
    ["Before or at the moment when the letter of acceptance is posted", "Before or at the moment when the communication of acceptance is complete as against the acceptor, but not afterwards", "Even after the proposer reads the acceptance letter", "Only with the written permission of a civil court"],
    1, "B",
    "Section 5 paragraph 2: 'An acceptance may be revoked at any time before or at the moment when the communication of the acceptance is complete as against the acceptor, but not afterwards'.",
    {"A": "Posting binds proposer, but acceptor can revoke until proposer receives it.", "B": "Correct. Acceptor can revoke before or when acceptance reaches proposer's knowledge.", "C": "Once proposer knows of acceptance, contract is irrevocable by acceptor.", "D": "Judicial intervention is not required to revoke an acceptance."},
    "Medium", "Indian Contract Act, 1872, Section 5", "Identify time limit for revocation of acceptance."
))

# top-cnt-01-04: Intention to Create Legal Relations (Balfour v Balfour Rule) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-01-025", "ch-cnt-01", "top-cnt-01-04",
    "In Balfour v. Balfour (1919), Lord Atkin held that agreements between husband and wife living in amity:",
    ["Are presumed to be legally binding contracts", "Are presumed not to result in legally enforceable contracts because parties do not intend legal consequences", "Are void ab initio under public policy", "Must be executed on judicial stamp paper"],
    1, "B",
    "In Balfour v. Balfour, Lord Atkin held that domestic agreements between spouses are presumed to lack intention to create legal relations.",
    {"A": "Commercial presumption is the opposite of domestic presumption.", "B": "Correct. Domestic agreements carry a presumption against intention to create legal relations.", "C": "They are not illegal or void ab initio, merely lacking legal intent.", "D": "Stamp paper is not a criterion for legal intention."},
    "Easy", "Court of Appeal: Balfour v. Balfour (1919) 2 KB 571", "Master Balfour v Balfour domestic presumption doctrine."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-026", "ch-cnt-01", "top-cnt-01-04",
    "In Merritt v. Merritt (1970), where husband and wife were separated and negotiated arrangements regarding their matrimonial home, the court held:",
    ["The presumption against intention to create legal relations applied as they were still married", "The domestic presumption was rebutted because separated spouses bargain at arm's length intending legal relations", "The agreement was void for want of consideration", "The agreement was voidable at option of the husband"],
    1, "B",
    "In Merritt v. Merritt, Lord Denning held that when spouses are separated or about to separate, the Balfour presumption does not apply.",
    {"A": "Separation rebuts the domestic harmony presumption.", "B": "Correct. Separated spouses negotiating their affairs intend to create binding legal relations.", "C": "Paying off mortgage constituted valid consideration.", "D": "The contract was fully valid and binding, not voidable."},
    "Medium", "Merritt v. Merritt (1970) 1 WLR 1211", "Distinguish Merritt v Merritt from Balfour v Balfour."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-027", "ch-cnt-01", "top-cnt-01-04",
    "In commercial agreements, the legal presumption regarding intention to create legal relations is:",
    ["Parties intend to create legal relations, but this presumption can be rebutted by express words like 'honour pledge'", "Parties never intend legal relations unless registered", "Intention must be proven by oral testimony in every single case", "Agreements are void unless executed before a magistrate"],
    0, "A",
    "In commercial transactions, there is a strong presumption of legal relations, rebuttable only by clear express exclusion (e.g. Rose & Frank v. JR Crompton).",
    {"A": "Correct. Commercial dealings presume legal enforceability unless explicitly excluded.", "B": "Registration is not required to establish legal intent.", "C": "The law presumes intention without requiring separate proof.", "D": "Magisterial execution is not a contract requirement."},
    "Medium", "Rose & Frank Co. v. J.R. Crompton & Bros (1925) AC 445", "Understand commercial presumption of legal relations."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-028", "ch-cnt-01", "top-cnt-01-04",
    "In Rose & Frank Co. v. J.R. Crompton & Bros (1925), an 'honourable pledge clause' explicitly declaring that the arrangement was not a formal or legal agreement was held:",
    ["Illegal and contrary to public policy", "Valid to rebut the presumption of legal relations, leaving the agreement unenforceable in court", "A void condition under Section 28", "To confer exclusive jurisdiction on arbitration"],
    1, "B",
    "The House of Lords held that parties to a business arrangement may expressly declare their intention that it shall not be attended by legal consequences.",
    {"A": "Parties are free to decide whether to enter legal relations.", "B": "Correct. An express clause excluding legal intent makes the arrangement an honour agreement.", "C": "Section 28 applies to contracts, whereas this never became a contract.", "D": "It excluded court and arbitral jurisdiction entirely."},
    "Hard", "House of Lords: Rose & Frank v. Crompton (1925) AC 445", "Analyze honour pledge clauses excluding legal relations."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-029", "ch-cnt-01", "top-cnt-01-04",
    "In Jones v. Padavatton (1969), a mother promised to pay monthly allowance to her daughter if she studied for the Bar in London. The agreement was held:",
    ["A binding commercial service contract", "A domestic family arrangement lacking intention to create legal relations", "A contract of guarantee under Section 126", "A void wagering contract"],
    1, "B",
    "The Court of Appeal held that the arrangement between mother and daughter was a family arrangement without intent to create legal relations.",
    {"A": "It was purely domestic, lacking commercial character.", "B": "Correct. Family arrangements are presumed to lack intention to create legal relations.", "C": "No third-party debt guarantee was involved.", "D": "No wager was involved."},
    "Medium", "Jones v. Padavatton (1969) 2 All ER 616", "Apply domestic presumption to parent-child agreements."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-030", "ch-cnt-01", "top-cnt-01-04",
    "Under Indian law, although 'intention to create legal relations' is not expressly mentioned in Section 10, the Supreme Court has recognized it as an essential element in:",
    ["CWT v. Abdul Hussain (1979)", "Satyabrata Ghose v. Mugneeram Bangur (1954)", "Hadley v. Baxendale (1854)", "Mohori Bibee v. Dharmodas Ghose (1903)"],
    0, "A",
    "In CWT v. Abdul Hussain (1979), the Supreme Court affirmed that intention to create legal relations is an essential requirement under Indian contract law.",
    {"A": "Correct. CWT v. Abdul Hussain recognized the requirement under Indian law.", "B": "Satyabrata Ghose is the leading case on frustration (Section 56).", "C": "Hadley v. Baxendale is the leading English case on damages.", "D": "Mohori Bibee is the leading Privy Council case on minor's agreement."},
    "Hard", "Supreme Court: CWT v. Abdul Hussain (AIR 1979 SC 1832)", "Trace Indian Supreme Court adoption of legal relations test."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-031", "ch-cnt-01", "top-cnt-01-04",
    "A invites B to dinner at a restaurant, and B accepts the invitation. A incurs expenditure booking a table, but B fails to turn up. A sues B for damages. Can A recover?",
    ["Yes, because there was a valid offer, acceptance, and expenditure incurred", "No, because social invitations lack intention to create legal relations", "Yes, on the principle of promissory estoppel", "Yes, under quasi-contract Section 70"],
    1, "B",
    "Social agreements and dinner invitations are presumed to lack intention to enter into legal obligations; no legal action lies.",
    {"A": "Social agreements are non-justiciable for want of legal intent.", "B": "Correct. Purely social invitations do not create legal obligations.", "C": "Promissory estoppel cannot turn a social dinner into an actionable contract.", "D": "Section 70 requires lawful non-gratuitous acts done for another's benefit."},
    "Easy", "Common Law & Indian Jurisprudence", "Apply legal relations rule to social invitations."
))
mcqs.append(make_mcq(
    "mcq-cnt-01-032", "ch-cnt-01", "top-cnt-01-04",
    "Which of the following tests is applied by courts to determine whether parties intended to create legal relations?",
    ["Subjective test of what the offeror privately thought", "Objective test of what a reasonable person would infer from the conduct and words of the parties", "Psychological evaluation of the parties", "Affidavit submitted by the plaintiff"],
    1, "B",
    "The test of intention to create legal relations is strictly objective: whether reasonable people considering the words and circumstances would conclude that a contract was intended.",
    {"A": "Subjective uncommunicated mental reservations are irrelevant.", "B": "Correct. An objective reasonable bystander test is applied.", "C": "Courts do not conduct psychological evaluations for contract intention.", "D": "Ex post facto self-serving affidavits cannot override objective conduct."},
    "Medium", "Smith v. Hughes (1871) LR 6 QB 597", "Identify objective test of intention."
))

# ==========================================
# CHAPTER 2: CONSIDERATION (24 MCQs)
# ==========================================
# top-cnt-02-01: Consideration Essentials, Types & Quid Pro Quo (Section 2(d)) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-02-001", "ch-cnt-02", "top-cnt-02-01",
    "Under Section 2(d) of the Indian Contract Act, consideration is defined as when, at the desire of the promisor, the promisee or any other person:",
    ["Has done or abstained from doing, or does or abstains from doing, or promises to do or to abstain from doing, something", "Suffers physical injury or loss", "Enters into a registered bond", "Pays money to a third party"],
    0, "A",
    "Section 2(d) defines consideration covering past, present, and future acts or abstinences done at the desire of the promisor.",
    {"A": "Correct. Verbatim definition under Section 2(d).", "B": "Detriment must be requested by promisor, not accidental physical injury.", "C": "Registration is not part of Section 2(d).", "D": "Payment to a third party is only consideration if desired by promisor."},
    "Easy", "Indian Contract Act, 1872, Section 2(d)", "Identify statutory definition of consideration."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-002", "ch-cnt-02", "top-cnt-02-01",
    "In Durga Prasad v. Baldeo (1880), the plaintiff built market shops at the desire of the District Collector. The shopkeeper defendants promised to pay commission on sales. The court held:",
    ["The promise was valid because plaintiff incurred expenditure", "The promise was void for want of consideration because the act was done at the Collector's desire, not at the desire of the promisors", "The promise was an enforceable quasi-contract", "The Collector became liable to pay the commission"],
    1, "B",
    "In Durga Prasad v. Baldeo, the Allahabad High Court held that an act done at the desire of a third party (Collector) is no consideration under Section 2(d).",
    {"A": "Expenditure not requested by promisor does not satisfy Section 2(d).", "B": "Correct. Consideration must move at the desire of the promisor.", "C": "No quasi-contractual claim lies against shopkeepers who did not request construction.", "D": "The Collector was acting in administrative capacity, incurring no liability."},
    "Medium", "Allahabad High Court: Durga Prasad v. Baldeo (1880) ILR 3 All 221", "Master 'desire of promisor' rule in Durga Prasad v Baldeo."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-003", "ch-cnt-02", "top-cnt-02-01",
    "In Kedarnath Bhattacharji v. Gorie Mahomed (1886), a subscriber promised to pay Rs 100 towards building a town hall, and the town commissioner entered into contracts with builders on the faith of the subscription. The Calcutta High Court held:",
    ["The subscriber was not liable as charitable subscriptions are gratuitous", "The subscriber was liable because entering into liabilities at the promisor's request constituted valid consideration", "The agreement was void under Section 25", "Only the government could enforce the subscription"],
    1, "B",
    "The Calcutta High Court held that incurring a liability or entering into building contracts on the faith of the promised subscription constitutes valid consideration.",
    {"A": "Pure promises to donate are unenforceable, but incurring liability changes the legal status.", "B": "Correct. Incurring liabilities on the faith of the promise made it enforceable.", "C": "Section 25 was overcome because consideration existed in the form of detriment.", "D": "The plaintiff town commissioner had locus standi to sue."},
    "Hard", "Calcutta High Court: Kedarnath v. Gorie Mahomed (1886) ILR 14 Cal 64", "Recall rule on subscription consideration in Kedarnath."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-004", "ch-cnt-02", "top-cnt-02-01",
    "In Abdul Aziz v. Masum Ali (1914), the defendant promised to subscribe Rs 500 for rebuilding a mosque, but no expenditure or liability was incurred on the faith of the promise before he backed out. The court held:",
    ["The defendant was liable to pay the subscription", "The agreement was a nudum pactum and unenforceable as no consideration moved from the promisee", "The committee was entitled to damages under Section 73", "The defendant was estopped from denying liability"],
    1, "B",
    "The Allahabad High Court held that a bare promise to subscribe to a charity without any detriment or liability incurred is nudum pactum and void.",
    {"A": "No liability attaches to a bare gratuitous promise.", "B": "Correct. In the absence of any act or liability incurred, the promise is nudum pactum.", "C": "No damages can be awarded for breach of an unenforceable promise.", "D": "Promissory estoppel cannot enforce a gratuitous promise where no reliance detriment occurred."},
    "Medium", "Allahabad High Court: Abdul Aziz v. Masum Ali (1914) ILR 36 All 268", "Distinguish Abdul Aziz from Kedarnath regarding consideration."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-005", "ch-cnt-02", "top-cnt-02-01",
    "Under Section 2(d) of the Indian Contract Act, which of the following forms of consideration is recognized in India?",
    ["Past consideration only", "Present (executed) consideration only", "Future (executory) consideration only", "Past, present, and future consideration"],
    3, "D",
    "The words 'has done or abstained' (past), 'does or abstains' (present), and 'promises to do or abstain' (future) in Section 2(d) recognize all three forms.",
    {"A": "Indian law recognizes more than just past consideration.", "B": "English common law rejects past consideration, but Indian law recognizes all three.", "C": "Executory consideration is only one of the recognized types.", "D": "Correct. Section 2(d) explicitly accommodates past, present, and future consideration."},
    "Easy", "Indian Contract Act, 1872, Section 2(d)", "Identify types of consideration under Section 2(d)."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-006", "ch-cnt-02", "top-cnt-02-01",
    "Under English law, past consideration is generally no consideration. Under Indian law, past consideration is:",
    ["Also no consideration whatsoever", "Valid consideration because Section 2(d) expressly includes 'has done or abstained from doing'", "Valid only if given by a minor", "Void as opposed to public policy"],
    1, "B",
    "Unlike English law, Section 2(d) of the Indian Contract Act expressly includes past acts done at the promisor's desire ('has done or abstained from doing').",
    {"A": "Incorrect; Indian law differs fundamentally from English law on this point.", "B": "Correct. Section 2(d) recognizes past acts done at the promisor's request as valid consideration.", "C": "Minors cannot provide valid consideration for a contract.", "D": "Past consideration is completely lawful in India."},
    "Medium", "Indian Contract Act, 1872, Section 2(d)", "Contrast Indian and English law on past consideration."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-007", "ch-cnt-02", "top-cnt-02-01",
    "Performance of an existing legal or public duty already imposed by law is:",
    ["Sufficient consideration to support a promise", "No consideration in the eyes of law", "Consideration only if done by a police officer", "Illegal consideration under Section 23"],
    1, "B",
    "Doing what one is already legally bound to do (public duty) is no consideration, as it offers no new legal benefit or detriment (Collins v. Godefroy).",
    {"A": "Pre-existing legal duty does not constitute good consideration.", "B": "Correct. Under Collins v. Godefroy, performance of an existing public duty is no consideration.", "C": "Police officers performing duty cannot claim private consideration.", "D": "It is not illegal per se, but it lacks consideration value."},
    "Medium", "Collins v. Godefroy (1831) 1 B & Ad 950", "Evaluate existing public duty as consideration."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-008", "ch-cnt-02", "top-cnt-02-01",
    "Under Explanation 2 to Section 25 of the Indian Contract Act, the inadequacy of consideration:",
    ["Renders the agreement void per se", "May be taken into account by the court in determining whether consent was freely given", "Is irrelevant even if fraud is alleged", "Converts the agreement into a criminal offence"],
    1, "B",
    "Explanation 2 to Section 25: An agreement is not void merely because consideration is inadequate, but inadequacy may be considered in determining free consent.",
    {"A": "Consideration need not be adequate to form a valid contract.", "B": "Correct. Inadequacy is evidentiary material for testing free consent.", "C": "Courts will examine inadequacy where fraud or undue influence is raised.", "D": "Inadequacy has no criminal consequences."},
    "Medium", "Indian Contract Act, 1872, Section 25 Explanation 2", "Apply Explanation 2 to Section 25 on inadequacy."
))

# top-cnt-02-02: Privity of Contract vs Privity of Consideration & Exceptions (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-02-009", "ch-cnt-02", "top-cnt-02-02",
    "Under Section 2(d) of the Indian Contract Act, consideration may move from:",
    ["The promisee only", "The promisee or any other person", "The promisor only", "A court of competent jurisdiction"],
    1, "B",
    "Section 2(d) uses the phrase 'the promisee or any other person', establishing that consideration need not move from the promisee alone.",
    {"A": "This represents the strict English common law rule, not Indian law.", "B": "Correct. In India, consideration may move from the promisee or any other person.", "C": "Consideration is given to the promisor, not moving from the promisor.", "D": "Courts do not supply consideration."},
    "Easy", "Indian Contract Act, 1872, Section 2(d)", "Identify from whom consideration may move under Indian law."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-010", "ch-cnt-02", "top-cnt-02-02",
    "In the landmark decision Chinnaya v. Ramayya (1882), an old lady gifted property to her daughter directing her to pay an annuity to the maternal uncle. When the daughter refused, the Madras High Court held:",
    ["The uncle could not sue because he was a stranger to the consideration", "The uncle could sue because under Section 2(d) consideration may move from 'any other person' (the mother)", "The agreement was void under Section 25", "The gift was revoked by operation of law"],
    1, "B",
    "In Chinnaya v. Ramayya, the Madras High Court held that a stranger to consideration can sue under Indian law because consideration moved from the mother.",
    {"A": "Stranger to consideration can enforce a contract in India, unlike in England.", "B": "Correct. Section 2(d) allows consideration to move from 'any other person'.", "C": "The agreement was fully supported by consideration moving from the donor.", "D": "The gift deed remained valid and binding."},
    "Medium", "Madras High Court: Chinnaya v. Ramayya (1882) ILR 4 Mad 137", "Master Chinnaya v Ramayya on stranger to consideration."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-011", "ch-cnt-02", "top-cnt-02-02",
    "In English law, under Tweddle v. Atkinson (1861) and Dunlop Pneumatic Tyre Co. v. Selfridge & Co. (1915):",
    ["Consideration must move from the promisee, and a stranger to contract cannot sue", "A stranger to consideration can always sue", "Privity of contract does not exist", "Third-party beneficiaries have absolute rights of suit"],
    0, "A",
    "English law strictly adheres to both rules: consideration must move from the promisee, and only a party to the contract can sue on it.",
    {"A": "Correct. English common law requires consideration to move from promisee and enforces strict privity.", "B": "English law rejects suits by strangers to consideration.", "C": "Privity of contract is a cornerstone of English common law.", "D": "Third parties had no rights at common law prior to the 1999 statute."},
    "Medium", "Tweddle v. Atkinson (1861); Dunlop v. Selfridge (1915) AC 847", "Contrast Indian and English rules on privity of consideration."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-012", "ch-cnt-02", "top-cnt-02-02",
    "In MC Chacko v. State Bank of Travancore (AIR 1970 SC 2059), the Supreme Court affirmed that under Indian law:",
    ["A person who is not a party to a contract cannot, subject to certain well-recognized exceptions, enforce the contract", "Anyone for whose benefit a contract is made can sue, without any exceptions", "Privity of contract does not apply in India at all", "Only banks can sue third parties"],
    0, "A",
    "The Supreme Court held in MC Chacko that the doctrine of privity of contract applies in India: a stranger to a contract cannot sue, subject to recognized exceptions.",
    {"A": "Correct. Privity of contract applies in India, distinguishing it from privity of consideration.", "B": "Third-party beneficiaries cannot sue unless falling within recognized exceptions.", "C": "Privity of contract does apply in India.", "D": "No special statutory exemption for banks existed on this principle."},
    "Hard", "Supreme Court: MC Chacko v. State Bank of Travancore (AIR 1970 SC 2059)", "Affirm privity of contract in India under MC Chacko."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-013", "ch-cnt-02", "top-cnt-02-02",
    "Which of the following is a recognized exception to the doctrine of privity of contract in India?",
    ["Beneficiaries under a trust or charge created in their favor", "Family or marriage settlements providing maintenance or expenses", "Estoppel, acknowledgment, or agency", "All of the above"],
    3, "D",
    "Recognized exceptions include trusts/charges (Khwaja Muhammad v. Husaini Begam), marriage/family settlements (Daropti v. Jaspat Rai), and acknowledgment/estoppel.",
    {"A": "Trust beneficiaries can enforce obligations created for their benefit.", "B": "Family/marriage settlements are well-settled exceptions.", "C": "Acknowledgment or estoppel creates direct liability to third party.", "D": "Correct. All of the listed situations are recognized exceptions to privity of contract."},
    "Medium", "Indian Contract Jurisprudence", "Identify recognized exceptions to privity of contract."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-014", "ch-cnt-02", "top-cnt-02-02",
    "In Khwaja Muhammad Khan v. Husaini Begam (1910), a father-in-law agreed with the bride's father to pay her 'Kharch-i-pandan' (betel-box expenses) charged on specific immovable property. The Privy Council held:",
    ["The bride could not sue as she was not a party to the agreement", "The bride was entitled to enforce the agreement as a charge/trust was created in her favor", "The agreement was void as a marriage brokage contract", "Only the bride's father could claim damages"],
    1, "B",
    "The Privy Council held that although the bride was not a party to the contract, an express charge had been created on property for her benefit, entitling her to sue.",
    {"A": "The Privy Council specifically rejected the application of English privity to Indian conditions here.", "B": "Correct. She was entitled to sue as beneficiary of a specific property charge.", "C": "Kharch-i-pandan is a customary pin-money allowance, not marriage brokage.", "D": "The bride herself was granted decree to enforce the payment."},
    "Hard", "Privy Council: Khwaja Muhammad Khan v. Husaini Begam (1910) 37 IA 152", "Analyze Khwaja Muhammad Khan trust/charge exception."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-015", "ch-cnt-02", "top-cnt-02-02",
    "What is the fundamental difference between 'privity of contract' and 'privity of consideration' under Indian law?",
    ["India accepts privity of consideration but rejects privity of contract", "India rejects privity of consideration (stranger to consideration can sue) but accepts privity of contract (stranger to contract generally cannot sue)", "Both privities are completely rejected in India", "Both privities are strictly enforced without exceptions"],
    1, "B",
    "Under Section 2(d), consideration may move from any other person (no privity of consideration), but only parties to the contract can enforce it (privity of contract applies).",
    {"A": "Reversed; legally inaccurate.", "B": "Correct. Stranger to consideration can sue, but stranger to contract generally cannot.", "C": "Privity of contract is firmly applied by the Supreme Court.", "D": "Both doctrines have distinct treatments and exceptions in Indian law."},
    "Hard", "Indian Contract Act, 1872, Section 2(d) & MC Chacko", "Synthesize distinction between privity of contract and consideration."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-016", "ch-cnt-02", "top-cnt-02-02",
    "Where A acknowledges to C that he holds money received from B for the use of C, A is liable to C on the ground of:",
    ["Promissory estoppel / Acknowledgment", "Subrogation", "Novation of contract", "Vicarious liability"],
    0, "A",
    "Where a promisor acknowledges to a third party or conducts himself as an agent for that third party, privity is overcome by estoppel/acknowledgment.",
    {"A": "Correct. Acknowledgment creates an obligation through estoppel.", "B": "Subrogation is substitution of one creditor for another in insurance/suretyship.", "C": "Novation requires agreement between all three parties to replace the contract.", "D": "Vicarious liability applies to torts of servants, not contractual acknowledgment."},
    "Medium", "Common Law & Indian Contract Principles", "Understand acknowledgment/estoppel exception to privity."
))

# top-cnt-02-03: Agreements Without Consideration & Section 25 Exceptions (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-02-017", "ch-cnt-02", "top-cnt-02-03",
    "Under Section 25 of the Indian Contract Act, the general rule is that an agreement made without consideration is:",
    ["Voidable", "Void", "Valid", "Illegal"],
    1, "B",
    "Section 25 opens with the general rule: 'An agreement made without consideration is void, unless...'. This is the Latin maxim ex nudo pacto non oritur actio.",
    {"A": "Voidable contracts are enforceable at one party's option; lack of consideration makes it void.", "B": "Correct. Section 25 declares agreements without consideration void.", "C": "Valid only if falling under the three statutory exceptions.", "D": "Lack of consideration is not a crime or illegal act under Section 23."},
    "Easy", "Indian Contract Act, 1872, Section 25", "Recall general rule of Section 25 on consideration."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-018", "ch-cnt-02", "top-cnt-02-03",
    "Under Section 25(1) of the Indian Contract Act, an agreement without consideration is valid if it is:",
    ["Expressed in writing, registered under law, made on account of natural love and affection, between parties standing in near relation to each other", "Made orally before village elders on account of natural love and affection", "Expressed in writing and attested by two witnesses", "Entered into between business partners"],
    0, "A",
    "Section 25(1) requires four cumulative conditions: (1) writing, (2) registered, (3) natural love and affection, and (4) near relation.",
    {"A": "Correct. All four statutory requirements under Section 25(1) must be fulfilled.", "B": "Oral agreements do not qualify under Section 25(1); writing and registration are mandatory.", "C": "Attestation is not enough; registration under the law is compulsory.", "D": "Business partners do not typically satisfy natural love and affection between near relations."},
    "Easy", "Indian Contract Act, 1872, Section 25(1)", "Identify essentials of Section 25(1) exception."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-019", "ch-cnt-02", "top-cnt-02-03",
    "In Rajlukhy Dabee v. Bhootnath Mookerjee (1900), a husband executed a registered agreement to pay maintenance to his wife after near relations quarreled. The Calcutta High Court held:",
    ["The agreement was enforceable under Section 25(1)", "The agreement was void because it was executed due to quarrels and discord, not out of natural love and affection", "The agreement was a valid family settlement", "The wife was entitled to half the husband's property"],
    1, "B",
    "The court held that although in writing, registered, and between near relations, the agreement was born of quarrels, so natural love and affection was absent.",
    {"A": "The court dismissed the wife's claim under Section 25(1).", "B": "Correct. Near relation alone is insufficient; natural love and affection must actually exist.", "C": "No family settlement exception was established.", "D": "No property partition decree was passed."},
    "Medium", "Calcutta High Court: Rajlukhy Dabee v. Bhootnath Mookerjee (1900) 4 CWN 488", "Analyze natural love and affection requirement in Rajlukhy Dabee."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-020", "ch-cnt-02", "top-cnt-02-03",
    "Under Section 25(2) of the Indian Contract Act, an agreement without consideration is valid if it is a promise to compensate:",
    ["A person who has already voluntarily done something for the promisor, or something which the promisor was legally compellable to do", "A person who promises to do future work without pay", "A stranger for entering into an illegal trade", "A public officer for performing his statutory duty"],
    0, "A",
    "Section 25(2) validates a promise to compensate wholly or in part a person who has already voluntarily done something for the promisor.",
    {"A": "Correct. Section 25(2) covers compensation for past voluntary services.", "B": "Future gratuitous work does not fall under Section 25(2).", "C": "Illegal transactions cannot be saved by Section 25(2).", "D": "Public officers cannot take private compensation for statutory duties."},
    "Medium", "Indian Contract Act, 1872, Section 25(2)", "Identify scope of past voluntary service under Section 25(2)."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-021", "ch-cnt-02", "top-cnt-02-03",
    "Under Section 25(3) of the Indian Contract Act, a promise to pay a time-barred debt is valid if:",
    ["It is made orally before two respectable witnesses", "It is made in writing and signed by the person to be charged therewith, or by his authorized agent", "The debtor deposits 10% in court", "The debt is not older than 12 years"],
    1, "B",
    "Section 25(3) requires that the promise to pay a debt barred by limitation must be made in writing and signed by the debtor or his authorized agent.",
    {"A": "Oral promises cannot revive a time-barred debt under Section 25(3).", "B": "Correct. Writing and signature are mandatory statutory requirements under Section 25(3).", "C": "Court deposit is not a statutory prerequisite.", "D": "Section 25(3) does not impose a 12-year restriction on reviving barred debts."},
    "Easy", "Indian Contract Act, 1872, Section 25(3)", "Master requirements of time-barred debt revival."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-022", "ch-cnt-02", "top-cnt-02-03",
    "Under Explanation 1 to Section 25 of the Indian Contract Act, nothing in Section 25 shall affect the validity of:",
    ["Any gift actually made between donor and donee", "Any agreement in restraint of trade", "Any wagering contract", "Any marriage brokage agreement"],
    0, "A",
    "Explanation 1 to Section 25 states: 'Nothing in this section shall affect the validity, as between the donor and donee, of any gift actually made'.",
    {"A": "Correct. Completed gifts need no consideration under Explanation 1.", "B": "Agreements in restraint of trade are void under Section 27.", "C": "Wagers are void under Section 30.", "D": "Marriage brokage is void as against public policy under Section 23."},
    "Easy", "Indian Contract Act, 1872, Section 25 Explanation 1", "Recall exception for completed gifts under Section 25."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-023", "ch-cnt-02", "top-cnt-02-03",
    "A finds B's purse on the road and gives it to him. B, in gratitude, promises to give A Rs 500. This agreement is:",
    ["Void for want of consideration", "Valid and enforceable under Section 25(2)", "Voidable at the option of B", "Illegal"],
    1, "B",
    "Under Section 25(2) and Illustration (c) to Section 25, A did something voluntarily for B, and B's subsequent promise to compensate him is a valid contract.",
    {"A": "Section 25(2) creates an express statutory exception for past voluntary service.", "B": "Correct. Exactly matches Illustration (c) to Section 25 of the Act.", "C": "It is not voidable; it is a valid binding contract.", "D": "Returning a lost purse is completely lawful and commendable."},
    "Medium", "Indian Contract Act, 1872, Section 25 Illustration (c)", "Apply Section 25(2) to finder of lost goods scenario."
))
mcqs.append(make_mcq(
    "mcq-cnt-02-024", "ch-cnt-02", "top-cnt-02-03",
    "A owes B Rs 1,000, but the debt is barred by the Limitation Act. A signs a written promise to pay B Rs 500 on account of the debt. Under Section 25(3), this is:",
    ["A void agreement because the whole debt is not promised", "A valid contract to pay Rs 500", "An unenforceable moral obligation", "Voidable at the option of A"],
    1, "B",
    "Under Illustration (e) to Section 25, a signed written promise to pay the whole or any part of a time-barred debt is a valid contract.",
    {"A": "A promise to pay 'wholly or in part' is expressly authorized under Section 25(3).", "B": "Correct. Section 25(3) and Illustration (e) explicitly validate paying part of a barred debt.", "C": "The written signed promise converts the moral debt into a legal contract.", "D": "It is fully binding, not voidable."},
    "Medium", "Indian Contract Act, 1872, Section 25 Illustration (e)", "Apply Section 25(3) to part-payment of barred debt."
))

# ==========================================
# CHAPTER 3: CAPACITY TO CONTRACT (24 MCQs)
# ==========================================
# top-cnt-03-01: Competency to Contract & Minor's Agreements (Mohori Bibee) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-03-001", "ch-cnt-03", "top-cnt-03-01",
    "Under Section 11 of the Indian Contract Act, every person is competent to contract who is of the age of majority according to the law to which he is subject, and who is:",
    ["Of sound mind, and is not disqualified from contracting by any law to which he is subject", "Possessed of immovable property", "A citizen of India by birth", "Educated and capable of signing documents"],
    0, "A",
    "Section 11 defines competency: age of majority, sound mind, and not disqualified by any law.",
    {"A": "Correct. These are the three statutory conditions of competency under Section 11.", "B": "Property ownership is not a criterion for capacity.", "C": "Foreigners and non-citizens also possess capacity subject to legal restrictions.", "D": "Formal education is not a legal test of capacity."},
    "Easy", "Indian Contract Act, 1872, Section 11", "Identify statutory requirements of competency."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-002", "ch-cnt-03", "top-cnt-03-01",
    "In the landmark Privy Council decision Mohori Bibee v. Dharmodas Ghose (1903), it was held that a minor's agreement is:",
    ["Voidable at the option of the minor", "Voidable at the option of the adult party", "Void ab initio (absolutely void)", "Valid until repudiated by guardian"],
    2, "C",
    "The Privy Council conclusively ruled that a minor's contract is not merely voidable, but absolutely void ab initio under Sections 10 and 11.",
    {"A": "English infant relief acts made certain contracts voidable, but Indian law makes them void ab initio.", "B": "Adult party cannot enforce nor avoid on minor's disability.", "C": "Correct. Mohori Bibee settled that minor's agreement is void ab initio.", "D": "Guardian's repudiation is irrelevant as no contract ever existed."},
    "Easy", "Privy Council: Mohori Bibee v. Dharmodas Ghose (1903) 30 IA 114", "Master Mohori Bibee ruling on minor's agreement."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-003", "ch-cnt-03", "top-cnt-03-01",
    "Does the doctrine of estoppel under Section 115 of the Indian Evidence Act apply against a minor who fraudulently misrepresents his age?",
    ["Yes, estoppel applies equally to minors and adults", "No, there can be no estoppel against a statute declaring minor's agreement void", "Yes, but only in criminal prosecutions", "Yes, if the minor is older than 16 years"],
    1, "B",
    "Sadiq Ali Khan v. Jai Kishori (1928) and Leslie v. Sheill (1914): A minor is not estopped from pleading infancy, because estoppel cannot defeat a statute.",
    {"A": "Estoppel would indirectly enforce a void contract, which the law prohibits.", "B": "Correct. Well-settled rule: no estoppel against a statute or against a minor pleading infancy.", "C": "Estoppel is a civil rule of evidence.", "D": "No age gradation exists within minority under Section 11."},
    "Medium", "Privy Council: Sadiq Ali Khan v. Jai Kishori (AIR 1928 PC 152)", "Evaluate estoppel against a minor."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-004", "ch-cnt-03", "top-cnt-03-01",
    "Can a person, upon attaining the age of majority, ratify an agreement entered into during his minority?",
    ["Yes, by executing a written confirmation", "No, an agreement void ab initio cannot be validated by subsequent ratification", "Yes, provided fresh consideration is paid", "Yes, with permission of the District Judge"],
    1, "B",
    "An agreement void ab initio is a legal nullity from the beginning. A dead transaction cannot be revived or ratified after majority (Nazir Ahmad v. Jiwan Das).",
    {"A": "Written confirmation cannot breathe life into a nullity.", "B": "Correct. Void ab initio agreements cannot be ratified upon attaining majority.", "C": "Fresh consideration requires a fresh contract, not ratification of the old void one.", "D": "Judicial permission cannot cure lack of initial capacity."},
    "Medium", "Nazir Ahmad v. Jiwan Das (AIR 1938 Lah 159)", "Assess ratification of minor's agreement upon majority."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-005", "ch-cnt-03", "top-cnt-03-01",
    "Under the equitable doctrine of restitution (Leslie v. Sheill, 1914, and Khan Gul v. Lakha Singh, 1928), if a minor obtains property by misrepresenting his age:",
    ["The minor can be compelled to restore the specific property if traceable in his possession", "The minor must repay the cash spent on luxuries", "The minor must pay general damages for deceit", "The property is forfeited to the State"],
    0, "A",
    "Equity compels restoration of specific property traceable in minor's hands (restitution stops where repayment begins, Leslie v. Sheill; expanded in Khan Gul).",
    {"A": "Correct. Traceable property can be restored under equitable restitution.", "B": "Personal decree for repayment of spent money cannot be passed against minor.", "C": "Tort cannot be used to indirectly enforce an invalid contract.", "D": "No escheat to the State occurs."},
    "Hard", "Leslie v. Sheill (1914) 3 KB 607; Khan Gul v. Lakha Singh (AIR 1928 Lah 609)", "Analyze doctrine of restitution against minor."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-006", "ch-cnt-03", "top-cnt-03-01",
    "Can a minor be a promisee or a beneficiary under a contract (e.g. purchaser of property or payee of a promissory note)?",
    ["No, a minor can never enter into any transaction whatsoever", "Yes, law does not disable a minor from becoming a beneficiary or enforcing a promise made in his favor", "Only if the contract is signed by the President of India", "Only in contracts exceeding Rs 10 lakhs"],
    1, "B",
    "A minor cannot be a promisor/obligor, but nothing in the Contract Act prevents a minor from being a promisee/beneficiary who has fully performed his part (Raghava Chariar v. Srinivasa).",
    {"A": "Incapacity protects minors from liability; it does not disable them from receiving benefits.", "B": "Correct. Minor can be a beneficiary or enforce a promise in his favor.", "C": "Presidential signature is unrelated to minor contracts.", "D": "No monetary threshold exists."},
    "Medium", "Madras High Court: Raghava Chariar v. Srinivasa (1916) 40 Mad 308", "Distinguish minor as obligor versus minor as beneficiary."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-007", "ch-cnt-03", "top-cnt-03-01",
    "Under Section 33 of the Specific Relief Act, 1963, where a minor institutes a suit for cancellation of an instrument, the court may:",
    ["Require the minor to restore benefits or make compensation to the other party to the extent the minor's estate has benefited", "Imprison the minor for fraudulent representation", "Enforce the mortgage against the minor", "Dismiss the suit with exemplary costs"],
    0, "A",
    "Section 33(2)(b) of the Specific Relief Act, 1963 empowers the court to grant equitable restitution against a minor to the extent his estate has benefited.",
    {"A": "Correct. Section 33 incorporates statutory restitution against a minor.", "B": "Civil courts cannot imprison minors for civil contracts.", "C": "The mortgage remains void and cannot be enforced.", "D": "The minor is entitled to sue for cancellation of void documents."},
    "Hard", "Specific Relief Act, 1963, Section 33", "Apply Section 33 SRA restitution against minor."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-008", "ch-cnt-03", "top-cnt-03-01",
    "Under the Indian Majority Act, 1875 (as amended), a person attains majority upon completing:",
    ["18 years in all cases", "21 years if a guardian of his person or property is appointed under the Guardians and Wards Act, 1890", "16 years for personal contracts", "25 years for commercial contracts"],
    0, "A",
    "By the Indian Majority (Amendment) Act, 1999, the uniform age of majority is 18 years for all individuals in India, deleting the former 21-year exception.",
    {"A": "Correct. Following 1999 amendment, 18 years is the uniform age of majority.", "B": "The 21-year exception for ward of court was omitted by 1999 amendment.", "C": "16 years is not the age of majority.", "D": "25 years is not a majority threshold."},
    "Medium", "Indian Majority Act, 1875, Section 3 (as amended in 1999)", "Identify statutory age of majority under Indian law."
))

# top-cnt-03-02: Persons of Unsound Mind & Disqualified Persons (Section 12) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-03-009", "ch-cnt-03", "top-cnt-03-02",
    "Under Section 12 of the Indian Contract Act, a person is of sound mind for the purpose of contracting if, at the time of making it:",
    ["He has a medical certificate from a government doctor", "He is capable of understanding the contract and of forming a rational judgment as to its effect upon his interests", "He has never suffered from any mental illness in his lifetime", "He can read and write English fluently"],
    1, "B",
    "Section 12 provides a two-fold test: capacity to understand the terms and capacity to form a rational judgment as to its effect upon one's interests.",
    {"A": "Medical certificate is not a statutory prerequisite under Section 12.", "B": "Correct. Section 12 test: understanding the contract + rational judgment of effects.", "C": "Past mental illness does not disable a person during lucid intervals.", "D": "Language literacy is irrelevant to mental soundness."},
    "Easy", "Indian Contract Act, 1872, Section 12", "Recall statutory test of sound mind under Section 12."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-010", "ch-cnt-03", "top-cnt-03-02",
    "Under Section 12 paragraph 2, a person who is usually of unsound mind, but occasionally of sound mind:",
    ["May never make a contract under any circumstances", "May make a contract when he is of sound mind", "May make a contract only with the consent of his legal heirs", "May contract only through the Public Trustee"],
    1, "B",
    "Section 12 paragraph 2: 'A person who is usually of unsound mind, but occasionally of sound mind, may make a contract when he is of sound mind' (lucid interval).",
    {"A": "The law permits contracts during lucid intervals.", "B": "Correct. Section 12 expressly validates contracts made during lucid intervals.", "C": "Consent of heirs is not a requirement.", "D": "Public Trustee involvement is not mandated for lucid contracts."},
    "Medium", "Indian Contract Act, 1872, Section 12 Paragraph 2", "Apply lucid interval rule under Section 12."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-011", "ch-cnt-03", "top-cnt-03-02",
    "Under Section 12 paragraph 3, a person who is usually of sound mind, but occasionally of unsound mind:",
    ["May make a contract at any time because sound mind is presumed", "May not make a contract when he is of unsound mind", "May make a voidable contract at his option", "Must obtain a court decree before contracting"],
    1, "B",
    "Section 12 paragraph 3: 'A person who is usually of sound mind, but occasionally of unsound mind, may not make a contract when he is of unsound mind' (e.g. delirious from fever or drunk).",
    {"A": "Temporary incapacity prevents contract formation during that period.", "B": "Correct. Cannot make a contract during periods of unsound mind.", "C": "An agreement made by a person of unsound mind is void ab initio in India.", "D": "No court decree is required to establish temporary disability."},
    "Medium", "Indian Contract Act, 1872, Section 12 Paragraph 3", "Apply temporary unsoundness rule under Section 12."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-012", "ch-cnt-03", "top-cnt-03-02",
    "Under Indian law, an agreement entered into by a person of unsound mind is:",
    ["Voidable at his option", "Void ab initio", "Valid unless set aside within 3 years", "Enforceable with leave of the High Court"],
    1, "B",
    "Unlike English common law where it is voidable, in Indian law under Sections 10, 11, and 12, an agreement by an unsound person is void ab initio.",
    {"A": "Voidable is the English common law rule (Imperial Loan Co v. Stone), not Indian law.", "B": "Correct. Under Indian law, capacity is fundamental; lack of it renders agreement void ab initio.", "C": "No limitation period can validate a void ab initio agreement.", "D": "High Court leave cannot cure total initial incapacity."},
    "Hard", "Indian Contract Act, 1872, Sections 10, 11, 12", "Distinguish Indian vs English position on lunatic contracts."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-013", "ch-cnt-03", "top-cnt-03-02",
    "Under Section 83 of the Code of Civil Procedure, 1908, an alien enemy residing in India without permission of the Central Government:",
    ["Can sue in any court as an ordinary plaintiff", "Cannot sue in any court in India", "Can sue only with permission of the High Court", "Can enter into valid contracts of trade"],
    1, "B",
    "Under Section 83 CPC, alien enemies residing in India without license of the Central Government cannot sue in Indian courts, and trading with an alien enemy is void.",
    {"A": "Alien enemies without license are barred from suing.", "B": "Correct. Section 83 CPC bars suits by unlicensed alien enemies.", "C": "Permission must come from Central Government, not High Court.", "D": "Trading with the enemy is illegal and void under Section 23."},
    "Medium", "Code of Civil Procedure, 1908, Section 83", "Identify contractual disability of alien enemy."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-014", "ch-cnt-03", "top-cnt-03-02",
    "Can a convict undergoing sentence of imprisonment in jail enter into a contract in India?",
    ["No, a convict suffers total civil death and can never contract", "Yes, Indian law does not declare a convict incompetent to contract, though practical disability may exist", "Only with written sanction of the prison superintendent", "Only for transfer of ancestral property"],
    1, "B",
    "Unlike old English common law of attainder/civil death, Indian law does not disqualify convicts from contracting, except where specifically barred by statute.",
    {"A": "Civil death does not apply in modern Indian jurisprudence.", "B": "Correct. Indian law recognizes no general contractual disqualification for convicts.", "C": "Superintendent sanction is an administrative matter, not substantive contract law.", "D": "No restriction limited to ancestral property exists."},
    "Hard", "Indian Contract Act, 1872, Section 11", "Assess contractual capacity of convicts under Indian law."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-015", "ch-cnt-03", "top-cnt-03-02",
    "An undischarged insolvent who enters into a contract for sale of property:",
    ["Has full power to transfer property vested in the Official Receiver/Assignee", "Is disqualified from dealing with property vested in the Official Assignee under insolvency law", "Can transfer property with 50% discount", "Is immune from all civil liability"],
    1, "B",
    "Upon adjudication, all property of an insolvent vests in the Official Assignee/Receiver; the insolvent is disqualified from dealing with such property.",
    {"A": "Insolvent is stripped of ownership and power of disposition over vested property.", "B": "Correct. Statutory disqualification under Provincial/Presidency Towns Insolvency Acts.", "C": "Discount does not cure lack of title or statutory disability.", "D": "Insolvency gives no immunity from unlawful acts."},
    "Medium", "Insolvency Law & Section 11 Contract Act", "Identify disability of undischarged insolvent."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-016", "ch-cnt-03", "top-cnt-03-02",
    "Under Section 86 of the Code of Civil Procedure, a foreign Sovereign or Ambassador:",
    ["Cannot enter into contracts in India", "Can enter into contracts but cannot be sued in an Indian court without consent of the Central Government", "Is criminally liable for contractual breach", "Must submit to arbitration in all disputes"],
    1, "B",
    "Foreign sovereigns and diplomats possess full capacity to contract, but enjoy sovereign immunity: no suit can be filed against them without Central Government consent (Section 86 CPC).",
    {"A": "They have full capacity to enter contracts.", "B": "Correct. Capacity exists, but procedural immunity bars suits without Central Government consent.", "C": "Breach of contract is never a criminal offence per se.", "D": "Arbitration is optional, not statutorily mandatory."},
    "Medium", "Code of Civil Procedure, 1908, Section 86", "Explain procedural capacity and immunity of foreign sovereigns."
))

# top-cnt-03-03: Necessaries Supplied to Incompetent Persons (Section 68) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-03-017", "ch-cnt-03", "top-cnt-03-03",
    "Under Section 68 of the Indian Contract Act, if a person incapable of entering into a contract is supplied by another with necessaries suited to his condition in life:",
    ["The incompetent person is personally liable to be imprisoned for debt", "The person who has furnished such supplies is entitled to be reimbursed from the property of such incapable person", "The supplier has no remedy whatsoever", "The guardian is personally liable in all cases"],
    1, "B",
    "Section 68 provides that the supplier is entitled to reimbursement from the property/estate of the incapable person, not through personal liability.",
    {"A": "Minors and lunatics are never personally liable under Section 68.", "B": "Correct. Liability attaches strictly to the property/estate of the incapable person.", "C": "Supplier is entitled to statutory reimbursement under quasi-contract.", "D": "Guardian is not personally liable unless he undertook personal guarantee."},
    "Easy", "Indian Contract Act, 1872, Section 68", "Recall statutory rule of reimbursement under Section 68."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-018", "ch-cnt-03", "top-cnt-03-03",
    "Under Section 68, the liability for necessaries supplied to a minor or lunatic is:",
    ["Personal liability of the minor", "Quasi-contractual liability attached to the minor's estate/property", "Tortious liability for wrongful conversion", "Criminal liability for fraud"],
    1, "B",
    "Liability under Section 68 is quasi-contractual (restitutionary) and attaches only in rem against the minor's estate, not in personam.",
    {"A": "Personal decree can never be passed against a minor.", "B": "Correct. It is a quasi-contractual reimbursement out of the minor's property.", "C": "No tortious cause of action is involved.", "D": "Receiving necessaries is lawful, not criminal."},
    "Medium", "Indian Contract Act, 1872, Section 68", "Characterize nature of liability under Section 68."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-019", "ch-cnt-03", "top-cnt-03-03",
    "In Peters v. Fleming (1840) and Chapple v. Cooper (1844), 'necessaries' suited to the condition in life of a minor include:",
    ["Things without which an individual cannot reasonably exist: food, clothing, shelter, education, and medical attendance suited to social status", "Expensive ornamental jewels and racehorses", "Any luxury item the minor demands", "Gambling debts"],
    0, "A",
    "Necessaries are not confined to bare physical survival, but include articles and services suitable to the station and degree in life of the infant (Chapple v. Cooper).",
    {"A": "Correct. Food, clothing, lodging, medical care, and education suited to status.", "B": "Mere luxuries and ornamental articles are not necessaries.", "C": "Minor's subjective desires cannot expand legal necessaries.", "D": "Gambling is illegal/void and cannot be a necessary."},
    "Medium", "Chapple v. Cooper (1844) 13 M & W 252", "Define scope of 'necessaries' in contract law."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-020", "ch-cnt-03", "top-cnt-03-03",
    "In Nash v. Inman (1908), a Cambridge undergraduate minor was supplied with eleven fancy waistcoats by a tailor. The minor was already amply supplied with clothes. The court held:",
    ["The tailor could recover the price because waistcoats are clothing", "The tailor could not recover because goods are not necessaries if the minor is already adequately supplied", "The minor was liable to be imprisoned", "The father was personally liable to pay the tailor"],
    1, "B",
    "In Nash v. Inman, the Court of Appeal held that plaintiff must prove not only that goods were suitable to the minor's station, but that he was not already adequately supplied.",
    {"A": "Clothing ceases to be a necessary if already sufficiently possessed.", "B": "Correct. Nash v. Inman established that plaintiff must prove actual lack of supply.", "C": "Minors cannot be imprisoned for price of goods.", "D": "Father had given no guarantee and was not liable."},
    "Hard", "Court of Appeal: Nash v. Inman (1908) 2 KB 1", "Master burden of proof in Nash v Inman."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-021", "ch-cnt-03", "top-cnt-03-03",
    "Does Section 68 cover necessaries supplied to the dependent family members whom the incapable person is legally bound to support?",
    ["No, Section 68 covers supplies to the incapable person alone", "Yes, Section 68 expressly includes supplies to 'any one whom he is legally bound to support'", "Only if authorized by a Family Court order", "Only if the dependent is an adult"],
    1, "B",
    "Section 68 explicitly states: 'supplied by another with necessaries... or any one whom he is legally bound to support, the person who has furnished... is entitled to be reimbursed'.",
    {"A": "Statutory wording covers legally dependent family members.", "B": "Correct. Section 68 covers the incapable person and anyone he is legally bound to support.", "C": "No preliminary family court order is required.", "D": "Dependents can be of any age, including minor children or wife."},
    "Medium", "Indian Contract Act, 1872, Section 68", "Apply Section 68 to dependent family members."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-022", "ch-cnt-03", "top-cnt-03-03",
    "A supplies B, a lunatic, with necessaries suitable to his condition in life. B has no property or estate whatsoever. What is A's legal remedy?",
    ["A can obtain personal decree against B and attach B's future earnings", "A has no remedy because liability under Section 68 is confined to the property of the incapable person", "A can arrest B's nearest relative", "A can sue the State Government for reimbursement"],
    1, "B",
    "Under Section 68, reimbursement is strictly from property. If the incapable person has no property, the supplier cannot recover anything, as there is no personal liability.",
    {"A": "Personal decree cannot be passed against an incapable person.", "B": "Correct. If there is no property, there can be no recovery under Section 68.", "C": "Relatives are not vicariously liable for an adult lunatic's necessaries.", "D": "State bears no general civil contractual liability for destitute individuals."},
    "Hard", "Indian Contract Act, 1872, Section 68", "Analyze case of incapable person without property under Section 68."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-023", "ch-cnt-03", "top-cnt-03-03",
    "Money lent to a minor to save his property from sale in execution of a decree is:",
    ["A void loan that cannot be recovered under any circumstance", "Recoverable under Section 68 as a necessary for preservation of the minor's estate", "A criminal violation of the Moneylenders Act", "Convertible into a mortgage without registration"],
    1, "B",
    "In Kedarnath v. Ajudhia (1883), money advanced to save a minor's property from execution sale was held to be a necessary recoverable from the minor's property under Section 68.",
    {"A": "Loans advanced for essential preservation of minor's property are treated as necessaries.", "B": "Correct. Preserving minor's estate from execution is a recognized necessary.", "C": "Advancing emergency funds is lawful.", "D": "Mortgages always require registered execution under TPA."},
    "Hard", "Kedarnath v. Ajudhia (1883) ILR 5 All 392", "Apply Section 68 to money lent for saving minor's estate."
))
mcqs.append(make_mcq(
    "mcq-cnt-03-024", "ch-cnt-03", "top-cnt-03-03",
    "Under Section 68 of the Indian Contract Act, what price is the supplier of necessaries entitled to recover?",
    ["The agreed contractual price, no matter how exorbitant", "A reasonable price for the goods/services supplied", "Double the wholesale cost", "Only the bare manufacturing cost"],
    1, "B",
    "Because the liability is quasi-contractual and restitutionary, the supplier is entitled only to a fair and reasonable price, not an inflated contractual charge.",
    {"A": "Contractual price is inapplicable because there is no valid contract.", "B": "Correct. Reimbursement is limited to a reasonable value for the necessaries.", "C": "Penal multipliers do not apply.", "D": "Fair market price, not bare manufacturing cost, is reimbursable."},
    "Medium", "Common Law & Section 68 Principles", "Determine quantum of reimbursement under Section 68."
))

# ==========================================
# CHAPTER 4: FREE CONSENT (32 MCQs)
# ==========================================
# top-cnt-04-01: Concept of Free Consent & Consensus ad Idem (Sections 13, 14) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-04-001", "ch-cnt-04", "top-cnt-04-01",
    "Under Section 13 of the Indian Contract Act, two or more persons are said to consent when they:",
    ["Sign the same written agreement", "Agree upon the same thing in the same sense (consensus ad idem)", "Receive identical consideration", "Appear before the same sub-registrar"],
    1, "B",
    "Section 13 defines consent: 'Two or more persons are said to consent when they agree upon the same thing in the same sense'. This is consensus ad idem.",
    {"A": "Signing without mental identity of subject matter is not consent.", "B": "Correct. Section 13 codifies the doctrine of consensus ad idem.", "C": "Identical consideration is not required.", "D": "Registration does not define mutual consent."},
    "Easy", "Indian Contract Act, 1872, Section 13", "Recall statutory definition of consent under Section 13."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-002", "ch-cnt-04", "top-cnt-04-01",
    "In Raffles v. Wichelhaus (1864) (The Peerless Case), where two ships named 'Peerless' sailed from Bombay at different times, and buyer and seller meant different ships:",
    ["A valid contract was formed for the first ship", "No contract was formed because there was no consensus ad idem (meeting of the minds)", "The contract was voidable at the buyer's option", "The seller was liable in damages for non-delivery"],
    1, "B",
    "The Court of Exchequer held that there was no consensus ad idem; each party meant a different ship, so no binding contract ever came into existence.",
    {"A": "No agreement was formed on either ship.", "B": "Correct. Total absence of consensus ad idem renders the agreement void ab initio.", "C": "It was completely void, not voidable.", "D": "No damages could be awarded on a non-existent contract."},
    "Medium", "Court of Exchequer: Raffles v. Wichelhaus (1864) 2 H & C 906", "Master Raffles v Wichelhaus consensus ad idem doctrine."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-003", "ch-cnt-04", "top-cnt-04-01",
    "Under Section 14 of the Indian Contract Act, consent is said to be free when it is not caused by:",
    ["Coercion, undue influence, fraud, misrepresentation, or mistake", "Lack of money or insolvency", "Parental disapproval", "Incompetence of legal counsel"],
    0, "A",
    "Section 14 enumerates five vitiating factors: (1) coercion (S.15), (2) undue influence (S.16), (3) fraud (S.17), (4) misrepresentation (S.18), (5) mistake (S.20-22).",
    {"A": "Correct. These are the five statutory vitiating factors under Section 14.", "B": "Insolvency is a matter of capacity or breach, not free consent.", "C": "Parental feelings do not vitiate legal consent unless amounting to undue influence.", "D": "Counsel errors do not vitiate free consent under Section 14."},
    "Easy", "Indian Contract Act, 1872, Section 14", "Identify five vitiating factors under Section 14."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-004", "ch-cnt-04", "top-cnt-04-01",
    "Under Section 19 of the Indian Contract Act, when consent to an agreement is caused by coercion, fraud, or misrepresentation, the agreement is a contract:",
    ["Void ab initio", "Voidable at the option of the party whose consent was so caused", "Illegal and unconstitutional", "Valid and enforceable unconditionally"],
    1, "B",
    "Section 19: When consent is caused by coercion, fraud, or misrepresentation, the contract is voidable at the option of the aggrieved party.",
    {"A": "Mistake can cause voidness, but coercion/fraud/misrep makes it voidable.", "B": "Correct. Section 19 declares such contracts voidable at option of aggrieved party.", "C": "It is not illegal or unconstitutional.", "D": "It is not unconditionally valid against the victim."},
    "Easy", "Indian Contract Act, 1872, Section 19", "Recall legal effect of vitiated consent under Section 19."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-005", "ch-cnt-04", "top-cnt-04-01",
    "Under Section 19A of the Indian Contract Act, when consent to an agreement is caused by undue influence, the agreement is a contract:",
    ["Voidable at the option of the party whose consent was so caused", "Void ab initio under all circumstances", "Binding without any judicial review", "Enforceable only by criminal court"],
    0, "A",
    "Section 19A explicitly states: 'When consent to an agreement is caused by undue influence, the agreement is a contract voidable at the option of the party whose consent was so caused'.",
    {"A": "Correct. Section 19A provides voidability for contracts tainted by undue influence.", "B": "Undue influence makes a contract voidable, not void ab initio.", "C": "Courts possess wide discretion under Section 19A to set it aside absolutely or on terms.", "D": "Civil courts exercise jurisdiction under Section 19A."},
    "Easy", "Indian Contract Act, 1872, Section 19A", "Identify remedy for undue influence under Section 19A."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-006", "ch-cnt-04", "top-cnt-04-01",
    "What is the fundamental distinction between 'absence of consent' (Section 13) and 'vitiated consent' (Section 14)?",
    ["Absence of consent makes agreement void ab initio; vitiated consent generally makes the contract voidable", "Absence of consent makes contract voidable; vitiated consent makes it void ab initio", "Both lead to identical legal consequences in every respect", "Absence of consent is punishable with rigorous imprisonment"],
    0, "A",
    "If there is no consensus ad idem (Section 13), there is no agreement at all (void ab initio). If consent exists but is not free (Section 14), a contract is formed but is voidable.",
    {"A": "Correct. No consent = void ab initio; tainted consent = voidable (except bilateral mistake).", "B": "Reversed; legally inaccurate.", "C": "Their legal statuses and remedies are fundamentally different.", "D": "Absence of consent is a civil nullity, not a crime."},
    "Hard", "Indian Contract Act, 1872, Sections 13, 14", "Differentiate lack of consensus from vitiated consent."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-007", "ch-cnt-04", "top-cnt-04-01",
    "In Foster v. Mackinnon (1869), an old man was induced to endorse a bill of exchange on the false representation that it was a guarantee. The court held:",
    ["He was liable because he signed the bill", "The endorsement was void ab initio because his mind did not accompany his signature (plea of non est factum)", "The bill was valid in the hands of all third parties", "He was liable in tort for negligence"],
    1, "B",
    "Under the doctrine of non est factum (it is not his deed), if a person signs a document radically different from what he intended without negligence, the contract is void ab initio.",
    {"A": "The court held that signing under fundamental deceit as to nature is void.", "B": "Correct. Non est factum applies: mind did not accompany signature.", "C": "Even a holder in due course cannot enforce a forged or void non est factum document.", "D": "The jury found he was not negligent in signing."},
    "Hard", "Foster v. Mackinnon (1869) LR 4 CP 704", "Master non est factum doctrine in Foster v Mackinnon."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-008", "ch-cnt-04", "top-cnt-04-01",
    "Under Section 19, if a party whose consent was caused by fraud or misrepresentation chooses to affirm the contract, he may insist that:",
    ["The contract shall be performed, and that he shall be put in the position in which he would have been if the representations made had been true", "The other party shall be sentenced to 3 years imprisonment", "The consideration shall be tripled", "The contract shall be rewritten by a magistrate"],
    0, "A",
    "Section 19 paragraph 2: The aggrieved party may insist that the contract be performed and that he be put in the position in which he would have been if representation had been true.",
    {"A": "Correct. Section 19 paragraph 2 affirms this statutory right of restitution/affirmation.", "B": "Civil affirmation has no criminal penal sanctions.", "C": "No arbitrary tripling of consideration is authorized.", "D": "Magistrates do not rewrite commercial contracts."},
    "Medium", "Indian Contract Act, 1872, Section 19 Paragraph 2", "Identify affirmation right under Section 19."
))

# top-cnt-04-02: Coercion: Statutory Definition & Legal Impact (Section 15) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-04-009", "ch-cnt-04", "top-cnt-04-02",
    "Under Section 15 of the Indian Contract Act, 'coercion' is defined as committing or threatening to commit any act forbidden by:",
    ["The Indian Penal Code (or Bharatiya Nyaya Sanhita)", "The Code of Criminal Procedure", "International Law", "Any local customary council"],
    0, "A",
    "Section 15 defines coercion as committing or threatening to commit any act forbidden by the Indian Penal Code (now BNS), or unlawful detaining of property.",
    {"A": "Correct. Section 15 expressly references acts forbidden by the Indian Penal Code.", "B": "CrPC is procedural, not the code defining forbidden acts.", "C": "International law is not the statutory reference in Section 15.", "D": "Customary councils cannot define forbidden acts for Section 15."},
    "Easy", "Indian Contract Act, 1872, Section 15", "Recall statutory definition of coercion under Section 15."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-010", "ch-cnt-04", "top-cnt-04-02",
    "Under Section 15, does coercion require that the Indian Penal Code (BNS) must be in force at the place where the coercion is employed?",
    ["Yes, coercion can only occur within Indian territorial waters", "No, Explanation to Section 15 expressly provides that it is immaterial whether the IPC is or is not in force at the place where coercion is employed", "Only if both parties are Indian citizens", "Only on high seas under admiralty jurisdiction"],
    1, "B",
    "Explanation to Section 15: 'It is immaterial whether the Indian Penal Code is or is not in force at the place where the coercion is employed' (e.g. threat on high seas on English ship).",
    {"A": "Territorial presence of IPC is expressly dispensed with.", "B": "Correct. The Explanation explicitly makes territorial application of IPC immaterial.", "C": "Citizenship is irrelevant to Section 15.", "D": "Not restricted to admiralty jurisdiction."},
    "Medium", "Indian Contract Act, 1872, Section 15 Explanation", "Apply Explanation to Section 15 on territoriality."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-011", "ch-cnt-04", "top-cnt-04-02",
    "In Chikkam Ammiraju v. Chikkam Seshamma (1917), a husband threatened to commit suicide unless his wife and son executed a release deed of property. The Madras High Court held:",
    ["Threat to commit suicide is an act forbidden by the IPC and therefore amounts to coercion under Section 15", "Threat to commit suicide is not coercion because suicide cannot be punished under the IPC", "The release deed was valid and irrevocable", "Suicide is an act of God"],
    0, "A",
    "The Madras High Court held that suicide is an act forbidden by the IPC (attempt being punishable under Section 309 IPC), so a threat to commit suicide constitutes coercion.",
    {"A": "Correct. Chikkam Ammiraju is the leading case holding threat of suicide constitutes coercion.", "B": "Attempt to commit suicide is penalised; the completed act is forbidden by law.", "C": "The release deed was set aside as voidable.", "D": "Suicide is a human act, not an act of God."},
    "Hard", "Madras High Court: Chikkam Ammiraju v. Seshamma (1917) ILR 41 Mad 33", "Master Chikkam Ammiraju ruling on threat to commit suicide."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-012", "ch-cnt-04", "top-cnt-04-02",
    "Does a threat to file a criminal prosecution or civil suit on a true or bona fide claim constitute coercion under Section 15?",
    ["Yes, any threat of litigation constitutes criminal coercion", "No, threatening to take lawful legal proceedings on a bona fide claim does not amount to coercion", "Only if the lawyer charges excessive fees", "Yes, under Section 19"],
    1, "B",
    "A threat to bring a legitimate legal action or enforce statutory rights is not an act forbidden by IPC and does not amount to coercion (Askari Mirza v. Bibi Jai Kishori).",
    {"A": "Lawful recourse to justice cannot be treated as coercion.", "B": "Correct. Lawful threat of litigation on a bona fide claim is not coercion.", "C": "Advocate fees are completely irrelevant to coercion.", "D": "Section 19 provides remedies for actual coercion, not lawful claims."},
    "Medium", "Askari Mirza v. Bibi Jai Kishori (1912) 16 IC 344", "Distinguish lawful threat of litigation from coercion."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-013", "ch-cnt-04", "top-cnt-04-02",
    "Under Section 15 of the Indian Contract Act, coercion may proceed from:",
    ["The promisor only", "Any person, and may be directed against any person", "A police officer only", "A magistrate of the first class"],
    1, "B",
    "Section 15 does not require coercion to move from a party to the contract, nor must it be directed against a contracting party (e.g. threat by stranger against promisor's child).",
    {"A": "Coercion need not proceed from a party to the contract.", "B": "Correct. Coercion may proceed from any person and be directed against any person.", "C": "Coercion is not confined to public officials.", "D": "Magistrates are judicial officers, not statutory agents of coercion."},
    "Hard", "Indian Contract Act, 1872, Section 15", "Analyze who may exercise coercion and against whom."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-014", "ch-cnt-04", "top-cnt-04-02",
    "Under Section 72 of the Indian Contract Act, a person to whom money has been paid, or anything delivered, by mistake or under coercion:",
    ["May retain the money as an involuntary gift", "Must repay or return it", "Is liable only for interest", "Is immune from civil suit"],
    1, "B",
    "Section 72 creates a quasi-contractual obligation: 'A person to whom money has been paid, or anything delivered, by mistake or under coercion, must repay or return it'.",
    {"A": "No gift is created under coercion.", "B": "Correct. Section 72 mandates restitution of money or property paid under coercion.", "C": "Principal amount must be returned, not merely interest.", "D": "No civil immunity exists for unjust retention."},
    "Medium", "Indian Contract Act, 1872, Section 72", "Apply Section 72 restitution for money paid under coercion."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-015", "ch-cnt-04", "top-cnt-04-02",
    "In English law, the concept corresponding to coercion is 'duress'. Duress at English common law differs from coercion under Section 15 because English common law duress:",
    ["Includes unlawful detention of property", "Was strictly confined to actual or threatened violence to the person (loss of life or liberty)", "Can proceed from any third party stranger", "Is defined in the English Criminal Code"],
    1, "B",
    "At English common law, duress was narrow, limited to violence or threat of violence to the person. Section 15 is much wider, covering unlawful detention of property and acts forbidden by IPC.",
    {"A": "Common law duress did not include duress of goods (expanded only later in equity).", "B": "Correct. Common law duress was strictly confined to threats against bodily safety/liberty.", "C": "Common law duress had to move from a party to the contract.", "D": "English common law has no unified criminal code like IPC."},
    "Hard", "Comparative Contract Law: Common Law Duress vs Section 15", "Contrast English duress with Indian statutory coercion."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-016", "ch-cnt-04", "top-cnt-04-02",
    "An agent refused to hand over business account books to a newly appointed agent unless the principal executed a release deed discharging him from all liabilities. This was held to be:",
    ["Valid exercise of lien under Section 171", "Coercion by unlawful detention of property under Section 15", "Legitimate negotiation", "Novation of agency"],
    1, "B",
    "In Muthiah Chettiar v. Karuppan Chetti (1927), detaining account books unlawfully to extort a release deed was held to be coercion under Section 15.",
    {"A": "An agent has no general lien to unlawfully withhold account books.", "B": "Correct. Unlawful detaining of property to extract consent is coercion under Section 15.", "C": "Extortionate detention is not legitimate negotiation.", "D": "No novation occurs where consent is extracted by pressure."},
    "Hard", "Madras High Court: Muthiah Chettiar v. Karuppan Chetti (1927) 53 MLJ 422", "Apply unlawful detaining of property test under Section 15."
))

# top-cnt-04-03: Undue Influence, Fiduciary Position & Unconscionability (Section 16) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-04-017", "ch-cnt-04", "top-cnt-04-03",
    "Under Section 16(1) of the Indian Contract Act, a contract is said to be induced by 'undue influence' where the relations subsisting between the parties are such that:",
    ["One of the parties is in a position to dominate the will of the other and uses that position to obtain an unfair advantage over the other", "One of the parties physically assaults the other", "Both parties belong to the same trade union", "One party has an advanced university degree"],
    0, "A",
    "Section 16(1) defines undue influence: one party is in a position to dominate the will of the other and uses that position to obtain an unfair advantage.",
    {"A": "Correct. Domination of will + use to obtain unfair advantage are the twin essentials.", "B": "Physical assault constitutes coercion (Section 15), not undue influence.", "C": "Trade union membership does not imply will domination.", "D": "Educational degree does not establish legal domination."},
    "Easy", "Indian Contract Act, 1872, Section 16(1)", "Recall statutory definition of undue influence under Section 16(1)."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-018", "ch-cnt-04", "top-cnt-04-03",
    "Under Section 16(2) of the Indian Contract Act, a person is deemed to be in a position to dominate the will of another where he:",
    ["Holds a real or apparent authority over the other, or stands in a fiduciary relation to the other", "Makes a contract with a person whose mental capacity is temporarily or permanently affected by reason of age, illness, or mental or bodily distress", "Both A and B", "Neither A nor B"],
    2, "C",
    "Section 16(2) clauses (a) and (b) provide statutory presumptions of domination: real/apparent authority, fiduciary relations, and mental distress.",
    {"A": "Clause (a) covers real/apparent authority and fiduciary relations.", "B": "Clause (b) covers mental distress, illness, and old age.", "C": "Correct. Both clauses (a) and (b) are codified statutory presumptions under Section 16(2).", "D": "Incorrect as both A and B are explicit statutory clauses."},
    "Easy", "Indian Contract Act, 1872, Section 16(2)", "Identify statutory presumptions of domination under Section 16(2)."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-019", "ch-cnt-04", "top-cnt-04-03",
    "Which of the following relationships is recognized in law as a fiduciary relationship raising a presumption of undue influence?",
    ["Advocate and client", "Doctor and patient", "Parent and child / Spiritual adviser and devotee", "All of the above"],
    3, "D",
    "Fiduciary relationships include parent-child, trustee-beneficiary, advocate-client, doctor-patient, and spiritual guru-disciple.",
    {"A": "Advocate-client is a classic fiduciary relationship.", "B": "Doctor-patient is a recognized fiduciary relationship.", "C": "Parent-child and guru-disciple are settled fiduciary relationships.", "D": "Correct. All of the listed relationships are fiduciary in character."},
    "Easy", "Indian Contract Jurisprudence, Section 16", "Identify fiduciary relationships under Section 16."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-020", "ch-cnt-04", "top-cnt-04-03",
    "In Mannu Singh v. Umadat Pande (1890), a Hindu devotee gifted all his property to his spiritual guru. When the disciple sued to cancel the gift, the court held:",
    ["The gift was valid because it was a pious religious donation", "The guru was in a fiduciary relation and dominated the disciple's will; the burden was on the guru to prove bona fides, which he failed to discharge", "The disciple was estopped by his own deed", "Only the religious endowment board could challenge the deed"],
    1, "B",
    "The Allahabad High Court held that a spiritual adviser stands in a fiduciary relation; under Section 16(3), the burden was on the guru to prove absence of undue influence.",
    {"A": "Pious motive cannot override the statutory presumption of undue influence.", "B": "Correct. Leading case holding spiritual adviser in fiduciary position with reversed burden of proof.", "C": "No estoppel lies against undue influence under Section 19A.", "D": "The donor himself has direct right of suit to cancel."},
    "Hard", "Allahabad High Court: Mannu Singh v. Umadat Pande (1890) ILR 12 All 523", "Analyze spiritual adviser undue influence in Mannu Singh."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-021", "ch-cnt-04", "top-cnt-04-03",
    "Under Section 16(3) of the Indian Contract Act, where a transaction appears on the face of it or on evidence to be unconscionable, the burden of proving that the contract was not induced by undue influence lies upon:",
    ["The person who challenges the contract", "The person in a position to dominate the will of the other", "The state prosecutor", "Both parties equally"],
    1, "B",
    "Section 16(3) reverses the burden of proof: where a dominant party enters an unconscionable contract, the dominant party must prove that it was not induced by undue influence.",
    {"A": "General burden is on challenger, but Section 16(3) reverses this burden.", "B": "Correct. Section 16(3) places the burden on the dominant party.", "C": "Prosecutors do not participate in civil contract litigation.", "D": "The burden is explicitly placed on the dominant person."},
    "Medium", "Indian Contract Act, 1872, Section 16(3)", "Master reverse burden of proof under Section 16(3)."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-022", "ch-cnt-04", "top-cnt-04-03",
    "In Subhash Chandra Das Mushib v. Ganga Prasad Das Mushib (AIR 1967 SC 878), the Supreme Court laid down that to establish undue influence, the court must consider:",
    ["Only whether the parties were related by blood", "Whether relations subsisted between parties where one dominated the will of the other, and whether that position was used to obtain an unfair advantage", "Only the market value of the property transferred", "Whether the deed was signed in blue ink"],
    1, "B",
    "The Supreme Court held that undue influence requires proof of two distinct elements: (1) position to dominate will, and (2) actual use of that position to obtain an unfair advantage.",
    {"A": "Mere blood relationship is not enough to prove undue influence.", "B": "Correct. Dominating position + actual use to gain unfair advantage must both be established.", "C": "Inadequacy of price alone does not prove undue influence without dominant relation.", "D": "Ink color is irrelevant to validity."},
    "Hard", "Supreme Court: Subhash Chandra v. Ganga Prasad (AIR 1967 SC 878)", "Apply two-stage test in Subhash Chandra case."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-023", "ch-cnt-04", "top-cnt-04-03",
    "A contract entered into with a 'pardanashin lady' carries a special rule of law in India, under which:",
    ["The contract is void ab initio", "The burden of proving that the deed was explained to and understood by her, and that she had independent advice, lies heavily on the person founding on the deed", "She can never hold or convey immovable property", "Her husband must be a co-signatory in all cases"],
    1, "B",
    "Under Privy Council rulings (e.g. Kali Bakhsh v. Ram Gopal), courts extend special protection to pardanashin ladies; the grantee must prove independent advice and full understanding.",
    {"A": "Pardanashin ladies are fully competent to contract.", "B": "Correct. Law places a heavy burden of proof on the party claiming under the deed.", "C": "She has full constitutional and statutory right to own and dispose of property.", "D": "Husband's co-signature is not a legal requirement."},
    "Medium", "Privy Council: Kali Bakhsh Singh v. Ram Gopal Singh (1913) 41 IA 23", "Understand protective doctrine for pardanashin ladies."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-024", "ch-cnt-04", "top-cnt-04-03",
    "Under Section 19A of the Indian Contract Act, when a court sets aside a contract induced by undue influence, it may do so:",
    ["Only with the consent of the defendant", "Either absolutely or, if the party entitled to avoid has received any benefit, upon such terms and conditions as to the court may seem just", "Only by imposing a fine on the plaintiff", "Without hearing the parties"],
    1, "B",
    "Section 19A paragraph 2: 'Any such contract may be set aside either absolutely or, if the party who was entitled to avoid it has received any benefit thereunder, upon such terms and conditions as to the Court may seem just'.",
    {"A": "Court does not require wrongdoer's consent to grant equitable relief.", "B": "Correct. Section 19A empowers courts to set aside absolutely or on just terms.", "C": "Civil courts setting aside contracts do not impose criminal fines on plaintiffs.", "D": "Due process requires full hearing."},
    "Medium", "Indian Contract Act, 1872, Section 19A Paragraph 2", "Apply court's equitable discretion under Section 19A."
))

# top-cnt-04-04: Fraud: Active Concealment & When Silence is Fraud (Section 17) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-04-025", "ch-cnt-04", "top-cnt-04-04",
    "Under Section 17 of the Indian Contract Act, 'fraud' means and includes which of the following acts committed by a party with intent to deceive:",
    ["Suggestion as a fact of that which is not true by one who does not believe it to be true", "Active concealment of a fact by one having knowledge or belief of the fact", "A promise made without any intention of performing it", "All of the above"],
    3, "D",
    "Section 17 defines fraud comprehensively across five clauses: false suggestion (suggestio falsi), active concealment (suppressio veri), empty promise, any other act fitted to deceive, and acts declared fraudulent by law.",
    {"A": "Suggestio falsi is covered under Section 17(1).", "B": "Active concealment is covered under Section 17(2).", "C": "Promise without intention is covered under Section 17(3).", "D": "Correct. All of the listed acts constitute statutory fraud under Section 17."},
    "Easy", "Indian Contract Act, 1872, Section 17", "Identify ingredients of fraud under Section 17."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-026", "ch-cnt-04", "top-cnt-04-04",
    "In the landmark English House of Lords decision Derry v. Peek (1889), Lord Herschell established that fraud is proved when a false representation has been made:",
    ["Knowingly, or without belief in its truth, or recklessly, careless whether it be true or false", "Negligently without consulting an expert", "In good faith but relying on an outdated map", "By an infant below the age of 12"],
    0, "A",
    "In Derry v. Peek, Lord Herschell held that fraudulent intent requires absence of honest belief: knowingly, without belief in its truth, or recklessly careless of truth.",
    {"A": "Correct. Derry v. Peek defined common law fraud (knowingly, without belief, or recklessly).", "B": "Negligence without dishonesty is misrepresentation, not fraud.", "C": "Honest belief, even if mistaken, negates fraud.", "D": "Infancy is an issue of capacity, not the definition of deceit."},
    "Medium", "House of Lords: Derry v. Peek (1889) 14 App Cas 337", "Master Derry v Peek definition of deceit and fraud."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-027", "ch-cnt-04", "top-cnt-04-04",
    "Under Explanation to Section 17 of the Indian Contract Act, does mere silence as to facts likely to affect the willingness of a person to enter into a contract amount to fraud?",
    ["Yes, silence is always fraud in every commercial contract", "No, mere silence is not fraud, unless it is the duty of the person keeping silence to speak, or unless his silence is, in itself, equivalent to speech", "Yes, if the price exceeds Rs 5,000", "No, silence is completely protected without any exceptions"],
    1, "B",
    "Explanation to Section 17 lays down the rule of caveat emptor: mere silence is not fraud, except where (1) there is a duty to speak, or (2) silence is equivalent to speech.",
    {"A": "Commercial bargaining does not impose a general duty of disclosure.", "B": "Correct. Mere silence is not fraud unless duty to speak exists or silence equals speech.", "C": "Monetary value does not alter the definition of fraud.", "D": "There are well-settled statutory exceptions where silence constitutes fraud."},
    "Medium", "Indian Contract Act, 1872, Section 17 Explanation", "Apply rule on silence as fraud under Section 17."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-028", "ch-cnt-04", "top-cnt-04-04",
    "Contracts 'uberrimae fidei' (contracts of utmost good faith) are transactions where full disclosure of all material facts is legally required. Which of the following is a contract uberrimae fides?",
    ["Contract of marine, fire, or life insurance", "Family settlement agreements", "Allotment of company shares via prospectus", "All of the above"],
    3, "D",
    "Contracts uberrimae fidei include contracts of insurance (duty of utmost good faith), family settlements, and company prospectuses.",
    {"A": "Insurance is the foremost example of contract uberrimae fidei.", "B": "Family settlements require full disclosure among family members.", "C": "Company prospectuses require full truth of material disclosures.", "D": "Correct. All of the listed classes of contracts require utmost good faith."},
    "Medium", "Indian Contract Jurisprudence, Section 17", "Identify contracts uberrimae fidei."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-029", "ch-cnt-04", "top-cnt-04-04",
    "In Shri Krishan v. Kurukshetra University (AIR 1976 SC 376), a student did not disclose in his examination admission form that he was short of attendance. The Supreme Court held:",
    ["The student committed fraud under Section 17", "Mere silence was not fraud; it was the duty of the university to scrutinize the candidate's eligibility before issuing the admit card", "The student was liable to criminal conviction for cheating", "The university could withdraw his degree at any time"],
    1, "B",
    "The Supreme Court held that the student committed no fraud; mere silence where there is no statutory duty to speak is not fraud, and the university failed to perform its own checking.",
    {"A": "The Supreme Court expressly rejected the finding of fraud.", "B": "Correct. Shri Krishan settled that mere silence is not fraud where authorities had duty to verify.", "C": "No cheating prosecution was maintainable.", "D": "The university was restrained from canceling his examination results."},
    "Hard", "Supreme Court: Shri Krishan v. Kurukshetra University (AIR 1976 SC 376)", "Apply Shri Krishan ruling on silence and fraud."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-030", "ch-cnt-04", "top-cnt-04-04",
    "Under Section 17, when a seller of a horse which is unsound remains silent, but the buyer says to the seller: 'If you do not deny it, I shall assume that the horse is sound', and the seller says nothing:",
    ["The seller is completely protected by caveat emptor", "The seller's silence is equivalent to speech and amounts to fraud", "The contract is void for illegality", "The buyer is liable for contempt"],
    1, "B",
    "Illustration (c) to Section 17 explicitly states that where silence is in itself equivalent to speech, remaining silent constitutes statutory fraud.",
    {"A": "Caveat emptor does not apply when silence equals speech.", "B": "Correct. Matches Illustration (c) to Section 17: silence is equivalent to speech.", "C": "It is not illegal; it makes the contract voidable for fraud.", "D": "No judicial contempt is involved."},
    "Medium", "Indian Contract Act, 1872, Section 17 Illustration (c)", "Apply silence equivalent to speech illustration."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-031", "ch-cnt-04", "top-cnt-04-04",
    "What is the crucial element that distinguishes 'fraud' (Section 17) from 'innocent misrepresentation' (Section 18)?",
    ["The value of consideration involved in the contract", "The presence of an intention to deceive (mens rea) in fraud, which is absent in innocent misrepresentation", "Fraud is only committed in writing, whereas misrepresentation is always oral", "Fraud can only be committed by a corporation"],
    1, "B",
    "Intent to deceive is the essential hallmark of fraud under Section 17. Misrepresentation under Section 18 occurs without intention to deceive.",
    {"A": "Monetary value does not distinguish fraud from misrepresentation.", "B": "Correct. Intent to deceive distinguishes fraud from misrepresentation.", "C": "Both can be committed orally or in writing.", "D": "Individuals commit fraud equally."},
    "Easy", "Indian Contract Act, 1872, Sections 17, 18", "Distinguish fraud from misrepresentation based on intention."
))
mcqs.append(make_mcq(
    "mcq-cnt-04-032", "ch-cnt-04", "top-cnt-04-04",
    "Under the Exception to Section 19, if consent was caused by misrepresentation or by silence fraudulent within the meaning of Section 17, the contract is NOT voidable if:",
    ["The plaintiff has a law degree", "The party whose consent was so caused had the means of discovering the truth with ordinary diligence", "The consideration was paid by cheque", "The contract was signed on a Sunday"],
    1, "B",
    "Exception to Section 19: If consent was caused by misrepresentation or fraudulent silence, the contract is not voidable if the party had means of discovering the truth with ordinary diligence.",
    {"A": "Educational qualifications do not invoke the Section 19 Exception.", "B": "Correct. Exception to Section 19 bars avoidance if truth could be discovered by ordinary diligence.", "C": "Payment mode is irrelevant.", "D": "Signing day does not affect contractual validity."},
    "Hard", "Indian Contract Act, 1872, Section 19 Exception", "Master Section 19 Exception on ordinary diligence."
))

print(f"Total MCQs generated for Part 1: {len(mcqs)}")

with open('scripts/data_contract_mcqs_1.py', 'w', encoding='utf-8') as f:
    f.write("# Contract Law MCQs Part 1 (Chapters 1 to 4: 112 MCQs)\n")
    f.write("MCQS_PART1 = " + json.dumps(mcqs, indent=2) + "\n")

print("Successfully written scripts/data_contract_mcqs_1.py")
