# Part 3: Contract Law (25), TPA 1882 (20), Torts (20), Jurisprudence (15), Maxims & Precedents (25) = 105 items

U_ICA = "https://www.indiacode.nic.in/handle/123456789/2187"
U_TPA = "https://www.indiacode.nic.in/handle/123456789/2338"
U_SC = "https://main.sci.gov.in/judgments"

def get_part3_items(m):
    # ---------------------------------------------------------
    # 8. INDIAN CONTRACT ACT, 1872 (25 items)
    # ---------------------------------------------------------
    m("An agreement entered into with a minor is voidable at the option of the minor in Indian law.",
      "false", "Law of Contract", "beginner", "Indian Contract Act, 1872", "Section 11", None,
      "In Mohori Bibee v. Dharmodas Ghose (1903), the Privy Council established that a contract with a minor is void ab initio, not merely voidable.",
      "Students often confuse English common law rules with the strict Indian rule of void ab initio.",
      "Section 68 permits reimbursement for necessaries supplied to a minor from their estate.",
      "is voidable at the option of the minor", "is void ab initio and cannot be enforced or ratified",
      U_ICA, "Current Contract Law", ["Minor Agreement", "Section 11", "Mohori Bibee", "Void Ab Initio", "Contract Capacity"])

    m("Past consideration is recognized as valid consideration under Section 2(d) of the Indian Contract Act, 1872.",
      "true", "Law of Contract", "beginner", "Indian Contract Act, 1872", "Section 2(d)", None,
      "Section 2(d) uses the words 'has done or abstained from doing', confirming that past consideration is good consideration in India.",
      "Under English law, past consideration is generally no consideration.",
      "The act must have been done at the desire of the promisor.",
      None, None,
      U_ICA, "Current Contract Law", ["Past Consideration", "Section 2(d)", "Promisor Desire", "Contract Act", "Consideration"])

    m("Under Indian law, consideration must strictly move from the promisee and cannot move from a third person.",
      "false", "Law of Contract", "beginner", "Indian Contract Act, 1872", "Section 2(d)", None,
      "Section 2(d) states 'when at the desire of the promisor, the promisee or any other person has done...', allowing consideration to move from a stranger (Chinnaya v. Ramayya).",
      "Candidates confuse stranger to consideration (permitted) with stranger to contract (doctrine of privity).",
      "Stranger to consideration can sue if party to contract, but stranger to contract generally cannot.",
      "must strictly move from the promisee and cannot move from a third person", "may move from the promisee or any other person under Section 2(d)",
      U_ICA, "Current Contract Law", ["Consideration", "Section 2(d)", "Chinnaya v. Ramayya", "Privity", "Contract Act"])

    m("An acceptance of an offer must be absolute and unqualified under Section 7 of the Indian Contract Act, 1872.",
      "true", "Law of Contract", "beginner", "Indian Contract Act, 1872", "Section 7", None,
      "Section 7 mandates that acceptance must be absolute and unqualified; a conditional acceptance operates as a counter-offer destroying the original proposal.",
      "A counter-proposal terminates the original offer (Hyde v. Wrench).",
      "Must be expressed in some usual and reasonable manner unless prescribed.",
      None, None,
      U_ICA, "Current Contract Law", ["Acceptance", "Section 7", "Absolute and Unqualified", "Counter Offer", "Contract Formation"])

    m("A proposal can be revoked at any time before the communication of its acceptance is complete as against the proposer.",
      "true", "Law of Contract", "intermediate", "Indian Contract Act, 1872", "Section 5", None,
      "Section 5 provides that a proposal may be revoked at any time before acceptance is complete as against the proposer, but not afterwards.",
      "Revocation of offer must reach the offeree before acceptance is dispatched.",
      "Governed by the postal communication rules under Section 4.",
      None, None,
      U_ICA, "Current Contract Law", ["Revocation", "Section 5", "Proposal", "Communication", "Contract Formation"])

    m("Under Section 4 of the Indian Contract Act, communication of acceptance is complete against the proposer as soon as it is put in the course of transmission.",
      "true", "Law of Contract", "intermediate", "Indian Contract Act, 1872", "Section 4", None,
      "Section 4 establishes the postal rule: acceptance is complete against the proposer the moment the letter of acceptance is posted beyond offeree control.",
      "Acceptance is complete against the acceptor only when it comes to the knowledge of the proposer.",
      "In instantaneous communication (phone/email), contract is made where acceptance is received (Bhagwandas v. Girdharilal).",
      None, None,
      U_ICA, "Current Contract Law", ["Section 4", "Postal Rule", "Acceptance Complete", "Transmission", "Contract Act"])

    m("An agreement made without consideration is void under all circumstances in Indian law.",
      "false", "Law of Contract", "beginner", "Indian Contract Act, 1872", "Section 25", None,
      "Section 25 enumerates three exceptions where an agreement without consideration is valid: (1) registered natural love and affection between near relations, (2) promise to compensate for past voluntary service, and (3) written promise to pay a time-barred debt.",
      "Many remember 'ex nudo pacto non oritur actio' without noting statutory exceptions.",
      "Gift actually made is also protected under Section 25 Explanation 1.",
      "is void under all circumstances in Indian law", "is valid if falling within the three statutory exceptions of Section 25",
      U_ICA, "Current Contract Law", ["Section 25", "Consideration Exceptions", "Love and Affection", "Time-barred Debt", "Voluntary Service"])

    m("Coercion under Section 15 of the Contract Act requires committing or threatening to commit any act forbidden by the Indian Penal Code or BNS.",
      "true", "Law of Contract", "intermediate", "Indian Contract Act, 1872", "Section 15", None,
      "Section 15 defines coercion as committing or threatening to commit any act forbidden by penal law, or unlawful detaining of property to the prejudice of any person with intent to cause agreement.",
      "Threat to commit suicide amounts to coercion as suicide attempt is forbidden (Chikkam Ammiraju v. Chikkam Seshamma).",
      "It is immaterial whether the penal code is or is not in force in the place where coercion is employed.",
      None, None,
      U_ICA, "Current Contract Law", ["Coercion", "Section 15", "Forbidden Act", "Chikkam Ammiraju", "Vitiated Consent"])

    m("Undue influence under Section 16 is presumed to exist where one party holds a real or apparent authority or stands in a fiduciary relation.",
      "true", "Law of Contract", "intermediate", "Indian Contract Act, 1872", "Section 16(2)", None,
      "Section 16(2) creates a presumption of dominant position where authority is held, fiduciary relation exists, or a person's mental capacity is affected by age, illness, or bodily distress.",
      "Burden of proving contract was fair shifts to the dominant party under Section 16(3).",
      "Applicable to parent-child, doctor-patient, and spiritual advisor-disciple relationships.",
      None, None,
      U_ICA, "Current Contract Law", ["Undue Influence", "Section 16", "Fiduciary Relation", "Dominant Position", "Burden of Proof"])

    m("Mere silence as to facts likely to affect the willingness of a person to enter into a contract is always fraud.",
      "false", "Law of Contract", "beginner", "Indian Contract Act, 1872", "Section 17 Explanation", None,
      "The Explanation to Section 17 explicitly states that mere silence is not fraud, unless there is a duty to speak (uberrimae fidei) or unless silence is in itself equivalent to speech.",
      "Laypersons think non-disclosure of known facts automatically constitutes fraud.",
      "Caveat emptor applies in ordinary commercial transactions.",
      "is always fraud", "is not fraud unless there is a duty to speak or silence is equivalent to speech",
      U_ICA, "Current Contract Law", ["Fraud", "Section 17", "Mere Silence", "Duty to Speak", "Uberrimae Fidei"])

    m("Misrepresentation under Section 18 of the Contract Act renders the resulting agreement void ab initio.",
      "false", "Law of Contract", "beginner", "Indian Contract Act, 1872", "Section 19", None,
      "Under Section 19, when consent to an agreement is caused by coercion, fraud, or misrepresentation, the agreement is a contract voidable at the option of the party whose consent was so caused, not void ab initio.",
      "Candidates confuse voidable contracts with void agreements.",
      "Party may also insist contract be performed and put in position if representations were true.",
      "renders the resulting agreement void ab initio", "renders the contract voidable at the option of the aggrieved party under Section 19",
      U_ICA, "Current Contract Law", ["Misrepresentation", "Section 18", "Section 19", "Voidable Contract", "Consent Vitiated"])

    m("Where both parties to an agreement are under a mistake as to a matter of fact essential to the agreement, the agreement is void under Section 20.",
      "true", "Law of Contract", "beginner", "Indian Contract Act, 1872", "Section 20", None,
      "Section 20 provides that where both parties are under a mistake as to a matter of fact essential to the agreement, the agreement is void (bilateral mistake).",
      "An erroneous opinion as to value of thing is not deemed a mistake as to a matter of fact (Explanation).",
      "Unilateral mistake under Section 22 does not make contract voidable.",
      None, None,
      U_ICA, "Current Contract Law", ["Bilateral Mistake", "Section 20", "Essential Fact", "Void Agreement", "Contract Act"])

    m("A contract is voidable under Section 21 of the Contract Act if it was caused by a mistake as to any law in force in India.",
      "false", "Law of Contract", "beginner", "Indian Contract Act, 1872", "Section 21", None,
      "Section 21 explicitly declares: 'A contract is not voidable because it was caused by a mistake as to any law in force in India.' Ignorantia juris non excusat applies.",
      "Candidates assume mistake of law is treated identically to mistake of fact.",
      "A mistake as to a law not in force in India (foreign law) is treated as a mistake of fact.",
      "is voidable under Section 21 of the Contract Act if it was caused by a mistake as to any law in force in India", "is not voidable for mistake of Indian law under Section 21",
      U_ICA, "Current Contract Law", ["Section 21", "Mistake of Law", "Ignorantia Juris", "Indian Law", "Foreign Law"])

    m("An agreement in restraint of trade is completely valid in Indian law if the restriction is reasonable between the parties.",
      "false", "Law of Contract", "intermediate", "Indian Contract Act, 1872", "Section 27", None,
      "Section 27 enacts a strict rule: every agreement by which anyone is restrained from exercising a lawful profession, trade or business is to that extent void. The common law test of 'reasonableness' does not apply, with the sole statutory exception being sale of goodwill (Madhub Chunder / Superintendence Co.).",
      "English law enforces reasonable restraints; Indian statute bars all restraints outside goodwill.",
      "Negative covenants during subsistence of employment are valid, but post-termination restraints are void.",
      "is completely valid in Indian law if the restriction is reasonable between the parties", "is void under Section 27 regardless of reasonableness, except for sale of goodwill",
      U_ICA, "Current Contract Law", ["Restraint of Trade", "Section 27", "Sale of Goodwill", "Void Agreements", "Madhub Chunder"])

    m("Every agreement by which any party is restricted absolutely from enforcing their rights under a contract in ordinary tribunals is void under Section 28.",
      "true", "Law of Contract", "beginner", "Indian Contract Act, 1872", "Section 28", None,
      "Section 28 invalidates agreements that restrict enforcement of rights or extinguish rights upon expiry of a specified period.",
      "Arbitration clauses are explicitly protected under Exception 1 and Exception 2 to Section 28.",
      "Clauses restricting jurisdiction to one of two competent courts are valid (Hakam Singh).",
      None, None,
      U_ICA, "Current Contract Law", ["Section 28", "Restraint of Legal Proceedings", "Arbitration Exception", "Jurisdiction Clauses", "Contract Act"])

    m("Agreements by way of wager are void under Section 30 of the Indian Contract Act, 1872.",
      "true", "Law of Contract", "beginner", "Indian Contract Act, 1872", "Section 30", None,
      "Section 30 provides that agreements by way of wager are void, and no suit shall be brought for recovering anything alleged to be won on any wager.",
      "Horse-racing prizes exceeding 500 rupees are statutorily exempted.",
      "Collateral transactions to wagering agreements are not illegal under general contract law, except in Gujarat and Maharashtra.",
      None, None,
      U_ICA, "Current Contract Law", ["Wager", "Section 30", "Void Agreement", "Speculation", "Horse Racing Exception"])

    m("A contingent contract to do or not to do anything if an impossible event happens is void under Section 36.",
      "true", "Law of Contract", "beginner", "Indian Contract Act, 1872", "Section 36", None,
      "Section 36 provides that contingent agreements to do or not to do anything if an impossible event happens are void, whether the impossibility of the event is known or not to the parties.",
      "Example: agreement to pay Rs. 1000 if two straight lines enclose a space.",
      "Governed under Chapter III (Contingent Contracts).",
      None, None,
      U_ICA, "Current Contract Law", ["Contingent Contract", "Section 36", "Impossible Event", "Void Agreement", "Contract Act"])

    m("The Doctrine of Frustration of contract is codified in Section 56 of the Indian Contract Act, 1872.",
      "true", "Law of Contract", "beginner", "Indian Contract Act, 1872", "Section 56", None,
      "Section 56 para 2 codifies frustration: a contract to do an act which, after the contract is made, becomes impossible or unlawful, becomes void when the act becomes impossible or unlawful (Satyabrata Ghose v. Mugneeram Bangur).",
      "Indian law leaves no room for common law implied term theories; frustration is positive statutory law.",
      "Commercial hardship or difficulty does not amount to frustration (Energy Watchdog).",
      None, None,
      U_ICA, "Current Contract Law", ["Frustration", "Section 56", "Satyabrata Ghose", "Impossibility", "Energy Watchdog"])

    m("Novation of a contract under Section 62 of the Contract Act can be effected by one party unilaterally without the consent of the other.",
      "false", "Law of Contract", "intermediate", "Indian Contract Act, 1872", "Section 62", None,
      "Section 62 requires mutual agreement of all parties: 'If the parties to a contract agree to substitute a new contract for it, or to rescind or alter it, the original contract need not be performed.' Unilateral substitution is a breach, not novation.",
      "Novation requires tripartite or multipartite consensus.",
      "The original contract is extinguished upon valid novation.",
      "can be effected by one party unilaterally without the consent of the other", "requires the mutual agreement of all parties to substitute the contract",
      U_ICA, "Current Contract Law", ["Novation", "Section 62", "Mutual Consent", "Substitution", "Discharge of Contract"])

    m("Under Section 74 of the Contract Act, the Court must award the entire liquidated damages named in the contract without assessing reasonable compensation.",
      "false", "Law of Contract", "intermediate", "Indian Contract Act, 1872", "Section 74", None,
      "Section 74 abolished the English distinction between liquidated damages and penalties: the party complaining is entitled to receive 'reasonable compensation not exceeding the amount so named', whether actual damage is proved or not (Fateh Chand / Kailash Nath Associates).",
      "Litigants think naming a penalty amount in the agreement guarantees automatic full recovery.",
      "Where loss can be assessed, actual loss must be proved.",
      "must award the entire liquidated damages named in the contract without assessing reasonable compensation", "awards only reasonable compensation not exceeding the named amount under Section 74",
      U_ICA, "Current Contract Law", ["Section 74", "Liquidated Damages", "Penalty", "Reasonable Compensation", "Kailash Nath"])

    m("Anticipatory breach of contract under Section 39 allows the promisee to put an end to the contract unless they have signified acquiescence in its continuance.",
      "true", "Law of Contract", "beginner", "Indian Contract Act, 1872", "Section 39", None,
      "Section 39 provides that when a party has refused to perform or disabled himself from performing his promise, the promisee may put an end to the contract, unless he has signified continuance by words or conduct.",
      "Promisee can either accept breach immediately and sue for damages, or keep contract alive until due date (Hochster v. De La Tour).",
      "If kept alive, contract remains open for benefit of both parties.",
      None, None,
      U_ICA, "Current Contract Law", ["Anticipatory Breach", "Section 39", "Repudiation", "Hochster v. De La Tour", "Contract Act"])

    m("Quasi-contracts or relations resembling those created by contract are codified under Sections 68 to 72 of the Indian Contract Act, 1872.",
      "true", "Law of Contract", "beginner", "Indian Contract Act, 1872", "Sections 68-72", None,
      "Chapter V codifies obligations based on unjust enrichment: necessaries to incapable persons (68), reimbursement of interested payer (69), non-gratuitous acts (70), finder of goods (71), and payment under mistake or coercion (72).",
      "Not based on consent, but imposed by law to prevent unjust enrichment.",
      "Lord Mansfield's doctrine of restitution codified.",
      None, None,
      U_ICA, "Current Contract Law", ["Quasi Contract", "Unjust Enrichment", "Section 68", "Section 70", "Section 72"])

    m("Under Section 71 of the Contract Act, a finder of goods is subject to the same responsibility as a bailee.",
      "true", "Law of Contract", "beginner", "Indian Contract Act, 1872", "Section 71", None,
      "Section 71 provides that a person who finds goods belonging to another and takes them into custody is subject to the same responsibility as a bailee under Section 151 (duty of reasonable care).",
      "Finder has a right of lien for expenses incurred under Section 168.",
      "Finder has right to sell goods if owner cannot be found or goods are perishing under Section 169.",
      None, None,
      U_ICA, "Current Contract Law", ["Finder of Goods", "Section 71", "Bailee Responsibility", "Reasonable Care", "Contract Act"])

    m("A contract of guarantee under Section 126 of the Contract Act is a bipartite contract between the creditor and the surety alone.",
      "false", "Law of Contract", "intermediate", "Indian Contract Act, 1872", "Section 126", None,
      "Section 126 defines a contract of guarantee as a tripartite contract involving three distinct parties: the principal debtor, the creditor, and the surety, with three collateral contracts.",
      "Candidates miss the tripartite nature, thinking the principal debtor is extraneous.",
      "Liability of surety is co-extensive with principal debtor under Section 128 unless contract provides otherwise.",
      "is a bipartite contract between the creditor and the surety alone", "is a tripartite contract involving principal debtor, creditor, and surety",
      U_ICA, "Current Contract Law", ["Contract of Guarantee", "Section 126", "Tripartite Contract", "Surety", "Principal Debtor"])

    m("A continuing guarantee can be revoked by the surety at any time as to future transactions by notice to the creditor under Section 130.",
      "true", "Law of Contract", "beginner", "Indian Contract Act, 1872", "Section 130", None,
      "Section 130 provides that a continuing guarantee may at any time be revoked by the surety, as to future transactions, by notice to the creditor.",
      "Surety remains liable for transactions entered into prior to the notice of revocation.",
      "Death of surety operates as revocation as to future transactions under Section 131 unless contract provides contrary.",
      None, None,
      U_ICA, "Current Contract Law", ["Continuing Guarantee", "Section 130", "Revocation Notice", "Future Transactions", "Contract Act"])

    # ---------------------------------------------------------
    # 9. TRANSFER OF PROPERTY ACT, 1882 (20 items)
    # ---------------------------------------------------------
    m("Transfer of property under Section 5 of the Transfer of Property Act, 1882 applies to testamentary transfers made by Will.",
      "false", "Transfer of Property Act, 1882", "beginner", "Transfer of Property Act, 1882", "Section 5", None,
      "Section 5 strictly defines transfer of property as an act inter vivos (between living persons). Testamentary transfers by Will take effect on death and are governed by the Indian Succession Act, 1925, not the TPA.",
      "Many assume all conveyances of property are governed by the TPA.",
      "Will is not a transfer of property under Section 5.",
      "applies to testamentary transfers made by Will", "applies strictly to transfers inter vivos between living persons",
      U_TPA, "Current Property Law", ["Inter Vivos", "Section 5", "Testamentary Transfer", "Will Excluded", "TPA 1882"])

    m("Spes successionis (the chance of an heir-apparent succeeding to an estate) cannot be transferred under Section 6(a) of the TPA.",
      "true", "Transfer of Property Act, 1882", "beginner", "Transfer of Property Act, 1882", "Section 6(a)", None,
      "Section 6(a) explicitly provides that the chance of an heir-apparent succeeding to an estate, the chance of a relation obtaining a legacy on the death of a kinsman, or any other mere possibility cannot be transferred.",
      "Transfer of a bare expectancy is void ab initio.",
      "Doctrine of feeding the grant by estoppel (Section 43) applies if a person fraudulently represents title.",
      None, None,
      U_TPA, "Current Property Law", ["Spes Successionis", "Section 6(a)", "Transferability", "Expectancy", "TPA 1882"])

    m("A condition restraining a transferee absolutely from parting with or disposing of their interest in the property is void under Section 10 of the TPA.",
      "true", "Transfer of Property Act, 1882", "beginner", "Transfer of Property Act, 1882", "Section 10", None,
      "Section 10 invalidates conditions imposing absolute restraint on alienation as repugnant to ownership.",
      "Exceptions exist for leases for the benefit of the lessor and married women not being Hindu, Muslim or Buddhist.",
      "Partial restraints (e.g. pre-emption to family at market value) may be valid.",
      None, None,
      U_TPA, "Current Property Law", ["Restraint on Alienation", "Section 10", "Absolute Restraint Void", "Property Ownership", "TPA 1882"])

    m("The Rule Against Perpetuity under Section 14 of the TPA allows vesting of property to be delayed for an unlimited number of years.",
      "false", "Transfer of Property Act, 1882", "intermediate", "Transfer of Property Act, 1882", "Section 14", None,
      "Section 14 mandates that vesting can only be delayed during the lifetime of one or more persons living at the date of transfer, and the minority of some person who shall be in existence at the expiration of that period (perpetuity period = lives in being + minority of 18 years).",
      "Perpetuity period in India is minority (18 years), unlike English common law (which allows gross term of 21 years).",
      "Transfers violating Section 14 are wholly void.",
      "allows vesting of property to be delayed for an unlimited number of years", "limits vesting delay to the lifetime of living persons plus the minority of unborn person under Section 14",
      U_TPA, "Current Property Law", ["Rule Against Perpetuity", "Section 14", "Lives in Being", "Minority Period", "TPA 1882"])

    m("A transfer directly to an unborn person without creating a prior life interest is valid under Section 13 of the TPA.",
      "false", "Transfer of Property Act, 1882", "intermediate", "Transfer of Property Act, 1882", "Section 13", None,
      "Section 13 requires that where an interest is created for the benefit of an unborn person, it must be preceded by a prior life estate created by the same transfer, and the interest to the unborn person must be the whole of the remaining interest.",
      "A transfer cannot be made directly to an unborn child as there must be a living recipient to hold legal title.",
      "The entire residual interest must be conveyed to the unborn person without diminution.",
      "directly to an unborn person without creating a prior life interest is valid", "requires a prior life interest and transfer of the whole remaining interest under Section 13",
      U_TPA, "Current Property Law", ["Unborn Person", "Section 13", "Prior Life Interest", "Absolute Remainder", "TPA 1882"])

    m("A vested interest under Section 19 of the TPA is defeated by the death of the transferee before obtaining possession.",
      "false", "Transfer of Property Act, 1882", "intermediate", "Transfer of Property Act, 1882", "Section 19 Explanation", None,
      "Section 19 expressly provides that a vested interest is not defeated by the death of the transferee before obtaining possession; it passes to their legal heirs as a heritable and transferable proprietary interest.",
      "Candidates confuse vested interest (immediate proprietary right, delayed enjoyment) with contingent interest (ownership depends on uncertain event).",
      "Contingent interest under Section 21 fails if the contingency becomes impossible before vesting.",
      "is defeated by the death of the transferee before obtaining possession", "is not defeated by the death of the transferee and passes to their legal heirs under Section 19",
      U_TPA, "Current Property Law", ["Vested Interest", "Section 19", "Heritable Property", "Contingent Interest", "TPA 1882"])

    m("The Doctrine of Election under Section 35 of the TPA requires that a person who takes a benefit under an instrument must also accept its burdens.",
      "true", "Transfer of Property Act, 1882", "beginner", "Transfer of Property Act, 1882", "Section 35", None,
      "Section 35 codifies the equitable principle: 'allegans contraria non est audiendus' (a person cannot blow hot and cold / approbate and reprobate). If owner disposes of another's property and confers benefit on real owner, real owner must elect to confirm transfer or dissent.",
      "If owner dissents, they relinquish the benefit conferred.",
      "Applies to all kinds of property, movable and immovable.",
      None, None,
      U_TPA, "Current Property Law", ["Doctrine of Election", "Section 35", "Approbate Reprobate", "Equitable Transfer", "TPA 1882"])

    m("A transfer by an ostensible owner with consent of the real owner is protected under Section 41 of the TPA if the purchaser acted in good faith after reasonable inquiry.",
      "true", "Transfer of Property Act, 1882", "intermediate", "Transfer of Property Act, 1882", "Section 41", None,
      "Section 41 enacts the statutory exception to 'nemo dat quod non habet': where an ostensible owner transfers immovable property for consideration, transfer is not voidable on ground that transferor was not authorized, if transferee took reasonable care.",
      "Transferee must conduct title search and search registry records (Ramcoomar Koondoo v. Macqueen).",
      "Real owner is estopped by having permitted the ostensible holding.",
      None, None,
      U_TPA, "Current Property Law", ["Ostensible Owner", "Section 41", "Bona Fide Purchaser", "Ramcoomar Koondoo", "Benami"])

    m("The Doctrine of Lis Pendens under Section 52 of the TPA renders any transfer made during the pendency of a suit void ab initio.",
      "false", "Transfer of Property Act, 1882", "beginner", "Transfer of Property Act, 1882", "Section 52", None,
      "Section 52 does not make transfers during litigation void ab initio; it merely makes the transfer subservient to the rights of the parties under the final decree (pendente lite transfer is valid between transferor and transferee, but binds transferee to decree: Kedar Nath v. Sheo Narain).",
      "Candidates mistakenly state lis pendens invalidates the deed of sale altogether.",
      "Decree binds the transferee as if they were a party to the suit.",
      "renders any transfer made during the pendency of a suit void ab initio", "makes the transfer subservient to the rights of the parties under the final decree, not void ab initio",
      U_TPA, "Current Property Law", ["Lis Pendens", "Section 52", "Pendente Lite", "Decree Binding", "Kedar Nath"])

    m("A fraudulent transfer intended to defeat or delay creditors is voidable at the option of any creditor so defeated or delayed under Section 53.",
      "true", "Transfer of Property Act, 1882", "beginner", "Transfer of Property Act, 1882", "Section 53(1)", None,
      "Section 53(1) provides that every transfer of immovable property made with intent to defeat or delay creditors shall be voidable at the option of any creditor so defeated or delayed.",
      "Does not impair the rights of a transferee in good faith and for consideration.",
      "Suit by creditor must be instituted on behalf of all creditors (representative capacity).",
      None, None,
      U_TPA, "Current Property Law", ["Fraudulent Transfer", "Section 53", "Creditor Protection", "Voidable Transfer", "TPA 1882"])

    m("The Doctrine of Part Performance under Section 53A of the TPA can be used as an active sword to file a suit for ejectment.",
      "false", "Transfer of Property Act, 1882", "intermediate", "Transfer of Property Act, 1882", "Section 53A", None,
      "In India, Section 53A acts strictly as a shield (defence to protect existing possession), not as a sword (cause of action to enforce title or eject others: Prabodh Kumar Das / Delhi Motor Co.).",
      "English equity allows part performance as a sword; Indian statute limits it to defending possession.",
      "Transferee must have taken possession in part performance and performed their contractual obligation.",
      "can be used as an active sword to file a suit for ejectment", "acts strictly as a shield to defend possession and cannot be used as an active sword to claim title",
      U_TPA, "Current Property Law", ["Part Performance", "Section 53A", "Shield Not Sword", "Possession Defence", "TPA 1882"])

    m("A sale of tangible immovable property of the value of one hundred rupees and upwards can be made by oral delivery of possession without registration.",
      "false", "Transfer of Property Act, 1882", "beginner", "Transfer of Property Act, 1882", "Section 54", None,
      "Section 54 mandates that transfer of tangible immovable property of the value of one hundred rupees and upwards can be made only by a registered instrument.",
      "Oral delivery is permissible only for tangible immovable property of value less than one hundred rupees.",
      "A contract for sale does not of itself create any interest in or charge on property.",
      "can be made by oral delivery of possession without registration", "can be made only by a registered instrument under Section 54",
      U_TPA, "Current Property Law", ["Sale of Property", "Section 54", "Mandatory Registration", "One Hundred Rupees", "TPA 1882"])

    m("Under Section 58(c) of the TPA, a mortgage by conditional sale must have the condition embodied in the very document which effects or purports to effect the sale.",
      "true", "Transfer of Property Act, 1882", "intermediate", "Transfer of Property Act, 1882", "Section 58(c) proviso", None,
      "The proviso to Section 58(c), added in 1929, explicitly requires that no transaction shall be deemed a mortgage by conditional sale unless the condition is embodied in the document which effects or purports to effect the sale.",
      "A separate contemporaneous agreement to reconvey cannot convert an absolute sale into a mortgage (Pandit Chunchun Jha v. Sheikh Ebadat Ali).",
      "Crucial distinction between mortgage by conditional sale and absolute sale with condition of repurchase.",
      None, None,
      U_TPA, "Current Property Law", ["Mortgage by Conditional Sale", "Section 58(c)", "Single Document", "Chunchun Jha", "TPA 1882"])

    m("In a Usufructuary Mortgage under Section 58(d) of the TPA, the mortgagor delivers possession of the mortgaged property to the mortgagee.",
      "true", "Transfer of Property Act, 1882", "beginner", "Transfer of Property Act, 1882", "Section 58(d)", None,
      "Section 58(d) defines usufructuary mortgage: mortgagor delivers possession and authorizes mortgagee to retain possession until payment of mortgage-money, and to receive rents and profits in lieu of interest or principal.",
      "No personal liability of mortgagor exists unless contracted.",
      "Mortgagee has no right of foreclosure or sale under Section 67.",
      None, None,
      U_TPA, "Current Property Law", ["Usufructuary Mortgage", "Section 58(d)", "Possession", "Rents and Profits", "No Foreclosure"])

    m("The right of redemption under Section 60 of the TPA is an absolute statutory right embodied in the maxim 'once a mortgage, always a mortgage'.",
      "true", "Transfer of Property Act, 1882", "beginner", "Transfer of Property Act, 1882", "Section 60", None,
      "Section 60 provides the mortgagor's right of redemption upon payment of mortgage-money. Clogs on redemption are void (Vernon v. Bethell / Murarilal v. Devkaran).",
      "Any stipulation preventing mortgagor from redeeming property upon discharging debt is invalid.",
      "Right can only be extinguished by act of parties or decree of court.",
      None, None,
      U_TPA, "Current Property Law", ["Right of Redemption", "Section 60", "Clog on Redemption", "Once a Mortgage", "Equity of Redemption"])

    m("The Doctrine of Subrogation under Section 92 of the TPA allows a person redeeming a mortgage to step into the shoes and exercise the rights of the mortgagee.",
      "true", "Transfer of Property Act, 1882", "intermediate", "Transfer of Property Act, 1882", "Section 92", None,
      "Section 92 provides that any co-mortgagor or third party who redeems property subject to mortgage acquires the rights of the mortgagee as to redemption, foreclosure or sale (subrogation).",
      "Legal subrogation arises by operation of law for co-mortgagors, subsequent mortgagees, or sureties.",
      "Conventional subrogation requires a registered written agreement.",
      None, None,
      U_TPA, "Current Property Law", ["Subrogation", "Section 92", "Step into Shoes", "Co-mortgagor", "TPA 1882"])

    m("A lease of immovable property from year to year or for any term exceeding one year can be made by oral agreement.",
      "false", "Transfer of Property Act, 1882", "beginner", "Transfer of Property Act, 1882", "Section 107", None,
      "Section 107 provides that a lease of immovable property from year to year, or for any term exceeding one year, or reserving a yearly rent, can be made only by a registered instrument.",
      "All other leases of immovable property may be made either by registered instrument or oral agreement with delivery of possession.",
      "Unregistered long-term lease creates only a month-to-month tenancy terminable by 15 days notice.",
      "can be made by oral agreement", "can be made only by a registered instrument under Section 107",
      U_TPA, "Current Property Law", ["Lease Registration", "Section 107", "Year to Year", "Registered Instrument", "TPA 1882"])

    m("A gift of immovable property under Section 123 of the TPA requires a registered instrument signed by the donor and attested by at least two witnesses.",
      "true", "Transfer of Property Act, 1882", "beginner", "Transfer of Property Act, 1882", "Section 123", None,
      "Section 123 mandates that for the purpose of making a gift of immovable property, transfer must be effected by a registered instrument signed by donor and attested by at least two witnesses.",
      "Gift of movable property may be completed by registered deed or delivery of possession.",
      "Acceptance must be made during lifetime of donor while still capable of giving (Section 122).",
      None, None,
      U_TPA, "Current Property Law", ["Gift of Property", "Section 123", "Two Witnesses", "Mandatory Registration", "TPA 1882"])

    m("An actionable claim under Section 130 of the TPA can be transferred by oral assignment without any written instrument.",
      "false", "Transfer of Property Act, 1882", "beginner", "Transfer of Property Act, 1882", "Section 130", None,
      "Section 130 mandates that the transfer of an actionable claim shall be effected only by the execution of an instrument in writing signed by the transferor or his duly authorized agent.",
      "Oral transfer of actionable claim is completely void.",
      "Notice to debtor is not essential to complete transfer between assignor and assignee, but debtor is protected until notice.",
      "can be transferred by oral assignment without any written instrument", "can be transferred only by an instrument in writing under Section 130",
      U_TPA, "Current Property Law", ["Actionable Claim", "Section 130", "Written Instrument", "Assignment", "TPA 1882"])

    m("A universal donee under Section 128 of the TPA is personally liable for all the debts and liabilities of the donor without any monetary limit.",
      "false", "Transfer of Property Act, 1882", "intermediate", "Transfer of Property Act, 1882", "Section 128", None,
      "Section 128 provides that a universal donee (who receives donor's entire property) is liable for all debts and liabilities of donor, but 'only to the extent of the property comprised in the gift.'",
      "Donee is not personally liable out of their own private assets beyond the value received.",
      "Protects creditors from fraudulent divestment by donor.",
      "without any monetary limit", "only to the extent of the value of the property comprised in the gift",
      U_TPA, "Current Property Law", ["Universal Donee", "Section 128", "Limited Liability", "Donor Debts", "TPA 1882"])

    # ---------------------------------------------------------
    # 10. LAW OF TORTS (20 items)
    # ---------------------------------------------------------
    m("Tortious liability arises from the breach of a duty primarily fixed by the law, towards persons generally, redressible by an action for unliquidated damages.",
      "true", "Law of Torts", "beginner", "Law of Torts", "Winfield Definition", None,
      "Winfield's celebrated definition of tortious liability captures its four core elements: duty fixed by law, duty towards persons generally, breach of duty, and unliquidated damages.",
      "Distinguished from contract where duties are fixed by agreement, and crime where state prosecutes for punishment.",
      "Remains the benchmark academic definition in Indian tort jurisprudence.",
      None, None,
      U_SC, "Judicial Precedents & Common Law", ["Tort Definition", "Winfield", "Unliquidated Damages", "Duty Fixed by Law", "Torts"])

    m("Damnum sine injuria (damage without legal injury) gives rise to a valid cause of action for damages in tort.",
      "false", "Law of Torts", "beginner", "Law of Torts", "Gloucester Grammar School Case", None,
      "Damnum sine injuria means damage suffered without infringement of a legal right; it is not actionable in law (Gloucester Grammar School case / Chasemore v. Richards).",
      "Laypersons assume any financial harm or economic loss can be sued for.",
      "Competition causing loss of profits is lawful damnum sine injuria.",
      "gives rise to a valid cause of action for damages in tort", "gives rise to no cause of action as legal injury is absent",
      U_SC, "Judicial Precedents & Common Law", ["Damnum Sine Injuria", "Gloucester Grammar School", "Legal Right", "No Cause of Action", "Torts"])

    m("Injuria sine damno (violation of a legal right without actual monetary loss) is actionable per se in tort.",
      "true", "Law of Torts", "beginner", "Law of Torts", "Ashby v. White", None,
      "Injuria sine damno means infringement of an absolute legal right without actual physical or financial damage, and is actionable per se (Ashby v. White - qualified voter wrongfully denied vote).",
      "Chief Justice Holt laid down that every injury imports a damage though it costs not a penny.",
      "Applies to trespass, false imprisonment, and voting rights.",
      None, None,
      U_SC, "Judicial Precedents & Common Law", ["Injuria Sine Damno", "Ashby v. White", "Actionable Per Se", "Ubi Jus Ibi Remedium", "Torts"])

    m("Under the defence of Volenti non fit injuria, a plaintiff who voluntarily undertakes a risk with full knowledge cannot claim damages.",
      "true", "Law of Torts", "beginner", "Law of Torts", "Hall v. Brooklands", None,
      "Volenti non fit injuria provides a complete defence where plaintiff consented to the harm or risk freely with full knowledge of nature and extent of risk (scienti et volenti).",
      "Mere knowledge of risk does not imply consent (scienter non est volenti - Smith v. Baker).",
      "Does not apply to rescue cases (Haynes v. Harwood).",
      None, None,
      U_SC, "Judicial Precedents & Common Law", ["Volenti Non Fit Injuria", "Consent Defence", "Smith v. Baker", "Rescue Cases", "Torts"])

    m("The rule of Strict Liability in Rylands v. Fletcher applies even in the absence of an escape of the dangerous thing from the defendant's land.",
      "false", "Law of Torts", "intermediate", "Law of Torts", "Rylands v. Fletcher", None,
      "In Rylands v. Fletcher (1868), Blackburn J. laid down that escape of the substance from the defendant's land to a place outside is an indispensable condition of strict liability (Read v. Lyons).",
      "Candidates miss the escape requirement, assuming hazardous condition on land alone suffices.",
      "Subject to exceptions: Act of God, plaintiff's default, consent, statutory authority.",
      "applies even in the absence of an escape of the dangerous thing from the defendant's land", "strictly requires the escape of the dangerous thing from the defendant's land",
      U_SC, "Judicial Precedents & Common Law", ["Strict Liability", "Rylands v. Fletcher", "Escape Requirement", "Read v. Lyons", "Torts"])

    m("The rule of Absolute Liability formulated in M.C. Mehta v. Union of India allows the defences of Act of God and plaintiff's default.",
      "false", "Law of Torts", "beginner", "Law of Torts", "M.C. Mehta v. Union of India (1987)", None,
      "In the Oleum Gas Leak case (M.C. Mehta v. UOI, 1987), the Supreme Court held that an enterprise engaged in a hazardous or inherently dangerous industry owes an absolute and non-delegable duty, with zero exceptions (Rylands v. Fletcher exceptions do not apply).",
      "Aspirants frequently confuse strict liability (which has 5 exceptions) with Indian absolute liability (which has zero exceptions).",
      "Quantum of damages is proportional to the capacity and wealth of the enterprise.",
      "allows the defences of Act of God and plaintiff's default", "admits of zero exceptions and holds hazardous enterprises strictly liable without defence",
      U_SC, "Judicial Precedents & Common Law", ["Absolute Liability", "M.C. Mehta", "Oleum Gas Leak", "No Exceptions", "Enterprise Liability"])

    m("Under vicarious liability, an employer is liable for the tortious acts committed by their employee during the course of employment.",
      "true", "Law of Torts", "beginner", "Law of Torts", "Respondeat Superior", None,
      "Based on the maxims 'respondeat superior' (let the principal answer) and 'qui facit per alium facit per se' (he who acts through another acts himself), an employer is liable for torts committed in the course of employment.",
      "Employer is not liable for independent contractor torts, unless duty is non-delegable.",
      "Acts outside course of employment ('frolic of his own') do not bind employer.",
      None, None,
      U_SC, "Judicial Precedents & Common Law", ["Vicarious Liability", "Respondeat Superior", "Course of Employment", "Master Servant", "Torts"])

    m("The defence of sovereign immunity protects the State against paying compensation for violation of Fundamental Rights under Article 21.",
      "false", "Law of Torts", "intermediate", "Law of Torts", "Nilabati Behera / Rudul Sah", None,
      "In Rudul Sah, Nilabati Behera, and D.K. Basu, the Supreme Court ruled that sovereign immunity has no application in public law remedies for violation of Fundamental Rights under Articles 32 and 226.",
      "Kasturi Lal v. State of U.P. (1965) allowed sovereign immunity in private law torts, but is inapplicable to constitutional torts.",
      "State must pay monetary compensation for custodial violence and illegal detention.",
      "protects the State against paying compensation for violation of Fundamental Rights under Article 21", "is completely inapplicable to constitutional tort violations under Article 21",
      U_SC, "Judicial Precedents & Common Law", ["Constitutional Tort", "Sovereign Immunity", "Rudul Sah", "Nilabati Behera", "Article 21"])

    m("Res ipsa loquitur (the thing speaks for itself) is a rule of evidence that shifts the burden of proof to the defendant in negligence actions.",
      "true", "Law of Torts", "beginner", "Law of Torts", "Byrne v. Boadle", None,
      "Res ipsa loquitur applies where the instrumentality causing harm was under exclusive control of defendant and the accident is such as does not happen without negligence, creating a prima facie inference of negligence (Byrne v. Boadle).",
      "Defendant must offer a plausible explanation consistent with due care.",
      "Reduces hardship for plaintiffs who cannot prove exact mechanics of negligence.",
      None, None,
      U_SC, "Judicial Precedents & Common Law", ["Res Ipsa Loquitur", "Negligence", "Byrne v. Boadle", "Burden of Proof", "Torts"])

    m("Under modern tort law, contributory negligence of the plaintiff completely bars all recovery of damages.",
      "false", "Law of Torts", "beginner", "Law of Torts", "Apportionment of Damages", None,
      "Under modern law of apportionment of damages, contributory negligence is no longer a complete defence; it merely reduces the plaintiff's damages in proportion to their degree of fault.",
      "Old common law complete bar (Butterfield v. Forrester) was abrogated.",
      "Governed by principles of comparative fault.",
      "completely bars all recovery of damages", "results in proportional reduction of damages based on comparative fault",
      U_SC, "Judicial Precedents & Common Law", ["Contributory Negligence", "Apportionment", "Comparative Fault", "Damages Reduction", "Torts"])

    m("Publication of a defamatory statement to at least one person other than the plaintiff is an essential element of the tort of Defamation.",
      "true", "Law of Torts", "beginner", "Law of Torts", "Defamation Tort", None,
      "In civil defamation, communication of the defamatory matter to a third party (someone other than the person defamed) is mandatory; communication solely to plaintiff causes no loss of reputation.",
      "If a letter is sent to plaintiff in language they cannot read and another reads it, sender is liable if they knew or ought to have known it would be read.",
      "Truth, fair comment, and privilege are complete defences.",
      None, None,
      U_SC, "Judicial Precedents & Common Law", ["Defamation", "Publication", "Reputation", "Civil Tort", "Third Party"])

    m("Innuendo refers to words that are prima facie innocent on their face but bear a defamatory meaning due to special extrinsic facts known to recipients.",
      "true", "Law of Torts", "intermediate", "Law of Torts", "Cassidy v. Daily Mirror", None,
      "An innuendo arises where plaintiff pleads and proves special extrinsic facts known to readers that make innocent words defamatory of plaintiff (Cassidy v. Daily Mirror / Tolley v. Fry).",
      "Plaintiff must specifically allege the innuendo in pleadings.",
      "Intention of defendant to defame is irrelevant in civil law.",
      None, None,
      U_SC, "Judicial Precedents & Common Law", ["Innuendo", "Defamation", "Cassidy v. Daily Mirror", "Extrinsic Facts", "Torts"])

    m("Private nuisance requires proof of substantial and unreasonable interference with the plaintiff's use and enjoyment of land.",
      "true", "Law of Torts", "beginner", "Law of Torts", "St. Helen's Smelting Co.", None,
      "Private nuisance is unreasonable interference with use and enjoyment of land, balancing rights through the standard of a reasonable neighbour ('give and take': St. Helen's Smelting Co. v. Tipping).",
      "Physical structural damage is always actionable; sensory discomfort requires substantial inconvenience.",
      "Plaintiff must have proprietary interest in the affected land (Hunter v. Canary Wharf).",
      None, None,
      U_SC, "Judicial Precedents & Common Law", ["Private Nuisance", "Use and Enjoyment", "Unreasonable Interference", "St. Helens Smelting", "Torts"])

    m("Trespass to land is actionable only upon proof of actual tangible physical damage to the property.",
      "false", "Law of Torts", "beginner", "Law of Torts", "Trespass Quare Clausum Fregit", None,
      "Trespass to land is actionable per se without proof of any damage; the mere entry upon another's land without lawful justification is a tort.",
      "Laypersons think entering garden or walking across field is not trespass unless crops are broken.",
      "Even stepping an inch over the boundary constitutes actionable trespass.",
      "is actionable only upon proof of actual tangible physical damage", "is actionable per se without proof of any actual damage",
      U_SC, "Judicial Precedents & Common Law", ["Trespass to Land", "Actionable Per Se", "Strict Possession", "Direct Interference", "Torts"])

    m("False imprisonment requires complete deprivation of the plaintiff's liberty in all directions without lawful justification.",
      "true", "Law of Torts", "intermediate", "Law of Torts", "Bird v. Jones", None,
      "In Bird v. Jones (1845), it was held that false imprisonment requires total restraint of liberty; partial obstruction where a person is free to go in another direction is not false imprisonment.",
      "Restraint can be physical or psychological (submission to apprehended authority).",
      "Plaintiff need not be aware of detention at the time (Meering v. Grahame-White Aviation).",
      None, None,
      U_SC, "Judicial Precedents & Common Law", ["False Imprisonment", "Bird v. Jones", "Total Restraint", "Deprivation of Liberty", "Torts"])

    m("In an action for Malicious Prosecution, the plaintiff must prove that the previous criminal prosecution terminated in their favor.",
      "true", "Law of Torts", "beginner", "Law of Torts", "Abrath v. North Eastern Railway", None,
      "Essential ingredients: (1) prosecution by defendant, (2) termination of prosecution in plaintiff's favor, (3) absence of reasonable and probable cause, (4) malice, and (5) damage.",
      "Pending criminal proceedings bar suit for malicious prosecution.",
      "Acquittal or discharge satisfies the favorable termination requirement.",
      None, None,
      U_SC, "Judicial Precedents & Common Law", ["Malicious Prosecution", "Favorable Termination", "Absence of Probable Cause", "Malice", "Torts"])

    m("The tort of Deceit requires proof that the defendant made a false representation knowing it to be false, without belief in its truth, or recklessly.",
      "true", "Law of Torts", "intermediate", "Law of Torts", "Derry v. Peek", None,
      "In Derry v. Peek (1889), the House of Lords established that fraud/deceit is proved when a false representation is made knowingly, without belief in its truth, or recklessly careless whether true or false.",
      "An honest belief in the truth of a statement negates deceit, even if carelessly formed.",
      "Negligent misstatement is a separate tort under Hedley Byrne v. Heller.",
      None, None,
      U_SC, "Judicial Precedents & Common Law", ["Deceit", "Derry v. Peek", "Fraud Tort", "Reckless Representation", "Torts"])

    m("Conversion is an intentional dealing with goods inconsistent with the true owner's right of possession.",
      "true", "Law of Torts", "intermediate", "Law of Torts", "Hollins v. Fowler", None,
      "Conversion is dealing with chattel in a manner inconsistent with owner's right of dominion, intending to assert a right inconsistent with owner (Hollins v. Fowler).",
      "Good faith purchase of stolen goods is still conversion against true owner.",
      "Remedy is market value of goods at time of conversion.",
      None, None,
      U_SC, "Judicial Precedents & Common Law", ["Conversion", "Chattel", "Right of Possession", "Hollins v. Fowler", "Torts"])

    m("The tort of Negligence requires proof of three elements: legal duty of care, breach of that duty, and consequential legal damage.",
      "true", "Law of Torts", "beginner", "Law of Torts", "Donoghue v. Stevenson", None,
      "Donoghue v. Stevenson (1932) established the modern tort of negligence based on Lord Atkin's neighbour principle: taking reasonable care to avoid acts or omissions foreseeably likely to injure your neighbour.",
      "Standard of care is that of an ordinary reasonable prudent person (Blyth v. Birmingham Waterworks).",
      "Damage must not be too remote (Wagon Mound No. 1 - reasonable foreseeability test).",
      None, None,
      U_SC, "Judicial Precedents & Common Law", ["Negligence", "Donoghue v. Stevenson", "Duty of Care", "Neighbour Principle", "Wagon Mound"])

    m("The 'Eggshell Skull Rule' allows a tortfeasor to escape liability if the victim had a pre-existing medical vulnerability causing unusual damage.",
      "false", "Law of Torts", "intermediate", "Law of Torts", "Dulieu v. White / Smith v. Leech Brain", None,
      "The eggshell skull rule establishes that a tortfeasor must take their victim as they find them (talem qualem); pre-existing physical or psychological vulnerability does not reduce liability (Smith v. Leech Brain).",
      "Defendants argue unusual fragility makes severe consequence unforeseeable.",
      "Applies once initial type of physical harm was reasonably foreseeable.",
      "allows a tortfeasor to escape liability if the victim had a pre-existing medical vulnerability", "mandates that a tortfeasor takes the victim as they find them regardless of vulnerability",
      U_SC, "Judicial Precedents & Common Law", ["Eggshell Skull Rule", "Smith v. Leech Brain", "Vulnerability", "Remoteness of Damage", "Torts"])

    # ---------------------------------------------------------
    # 11. JURISPRUDENCE (15 items)
    # ---------------------------------------------------------
    m("Analytical Positivist John Austin defined law as the command of a sovereign backed by the threat of sanction.",
      "true", "Jurisprudence", "beginner", "Jurisprudence", "Austin Imperative Theory", None,
      "John Austin's imperative theory posits law as: (1) command, (2) issued by political sovereign, (3) imposing duty, and (4) backed by sanction.",
      "Criticized by H.L.A. Hart for failing to distinguish being obliged from having an obligation.",
      "Central foundation of 19th-century English analytical jurisprudence.",
      None, None,
      U_SC, "Jurisprudence & Legal Theory", ["John Austin", "Imperative Theory", "Command of Sovereign", "Sanction", "Positivism"])

    m("Hans Kelsen's Pure Theory of Law views the legal system as a hierarchy of norms deriving validity from an ultimate Grundnorm.",
      "true", "Jurisprudence", "beginner", "Jurisprudence", "Kelsen Pure Theory", None,
      "Kelsen's Reine Rechtslehre seeks a science of law free from political, sociological or moral elements, structured as a pyramidal hierarchy of norms culminating in the Grundnorm (basic norm).",
      "In India, the Constitution functions as the Grundnorm.",
      "Validity of lower norms depends on compliance with higher empowering norms.",
      None, None,
      U_SC, "Jurisprudence & Legal Theory", ["Hans Kelsen", "Pure Theory of Law", "Grundnorm", "Hierarchy of Norms", "Jurisprudence"])

    m("H.L.A. Hart defined law as the union of primary rules of obligation and secondary rules of recognition, change, and adjudication.",
      "true", "Jurisprudence", "intermediate", "Jurisprudence", "The Concept of Law", None,
      "In 'The Concept of Law' (1961), Hart refuted Austin's gunman model by demonstrating that law consists of primary duty-imposing rules combined with secondary power-conferring rules.",
      "Rule of Recognition resolves uncertainty about what counts as valid law.",
      "Emphasizes the internal point of view of participants accepting legal rules.",
      None, None,
      U_SC, "Jurisprudence & Legal Theory", ["H.L.A. Hart", "Primary Rules", "Secondary Rules", "Rule of Recognition", "Jurisprudence"])

    m("Friedrich Carl von Savigny, leader of the Historical School, propounded that law originates in the Volksgeist (spirit of the people).",
      "true", "Jurisprudence", "beginner", "Jurisprudence", "Historical School", None,
      "Savigny maintained that law is not made deliberately by legislators, but develops organically like language, growing with the nation and resting in common popular consciousness (Volksgeist).",
      "Opposed premature statutory codification in Germany in 1814.",
      "Stressed custom and historical continuity over abstract universal codes.",
      None, None,
      U_SC, "Jurisprudence & Legal Theory", ["Savigny", "Volksgeist", "Historical School", "Custom", "Jurisprudence"])

    m("Roscoe Pound of the Sociological School propounded the theory of 'Social Engineering' to balance competing human interests in society.",
      "true", "Jurisprudence", "beginner", "Jurisprudence", "Sociological Jurisprudence", None,
      "Roscoe Pound defined law as social engineering: ordering human relations through elimination of friction and waste, balancing individual interests, public interests, and social interests (jural postulates).",
      "Focuses on law in action rather than abstract doctrine in books.",
      "Heavily influenced Indian constitutional jurisprudence on social welfare.",
      None, None,
      U_SC, "Jurisprudence & Legal Theory", ["Roscoe Pound", "Social Engineering", "Sociological School", "Jural Postulates", "Jurisprudence"])

    m("The American Legal Realist movement emphasized that law is found primarily in paper statutes rather than in actual judicial behaviour.",
      "false", "Jurisprudence", "intermediate", "Jurisprudence", "Legal Realism", None,
      "Legal Realism (Holmes, Llewellyn, Frank) rejected mechanical jurisprudence and argued that law is what courts do in fact ('the prophecies of what the courts will do in fact, and nothing more pretentious, are what I mean by the law' - O.W. Holmes).",
      "Aspirants confuse positivist formalism with realist empirical pragmatism.",
      "Distinguishes real rules from paper rules.",
      "found primarily in paper statutes rather than in actual judicial behaviour", "determined by what courts actually do in practice (law in action)",
      U_SC, "Jurisprudence & Legal Theory", ["Legal Realism", "O.W. Holmes", "Karl Llewellyn", "Law in Action", "Jurisprudence"])

    m("The Natural Law School posits that an unjust human law contrary to moral reason lacks the character of true law (lex iniusta non est lex).",
      "true", "Jurisprudence", "beginner", "Jurisprudence", "Natural Law", None,
      "From Cicero and St. Thomas Aquinas to John Finnis and Lon Fuller, Natural Law asserts that human laws derive validity from higher universal moral principles.",
      "Revived after WWII in the Nuremberg Trials to punish Nazi atrocities enacted under valid positive statutes.",
      "Foundation for universal human rights and constitutional morality.",
      None, None,
      U_SC, "Jurisprudence & Legal Theory", ["Natural Law", "Lex Iniusta Non Est Lex", "Aquinas", "Lon Fuller", "Morality"])

    m("John Salmond defined Jurisprudence as the science of the first principles of the civil law.",
      "true", "Jurisprudence", "beginner", "Jurisprudence", "Salmond Definition", None,
      "Salmond's classic definition: 'Jurisprudence may be defined as the science of the first principles of the civil law', meaning the law of the state administered by judicial tribunals.",
      "Distinguished civil law from natural law, international law, and conventional law.",
      "Core standard text for UP PCS-J Paper II Jurisprudence.",
      None, None,
      U_SC, "Jurisprudence & Legal Theory", ["Salmond", "First Principles", "Civil Law", "Jurisprudence Definition", "Legal Theory"])

    m("In Wesley Newcomb Hohfeld's analysis of jural relations, a Right correlates with a Duty, and a Liberty correlates with a No-Right.",
      "true", "Jurisprudence", "intermediate", "Jurisprudence", "Hohfeldian Analysis", None,
      "Hohfeld resolved conceptual ambiguity with jural correlatives (Right-Duty, Liberty-No Right, Power-Liability, Immunity-Disability) and jural opposites.",
      "Strict distinction between claim-rights (enforceable duties) and liberties (absence of duty).",
      "Standard framework for analytical jurisprudence.",
      None, None,
      U_SC, "Jurisprudence & Legal Theory", ["Hohfeld", "Jural Correlatives", "Right and Duty", "Liberty", "Analytical Jurisprudence"])

    m("Ownership is legally analyzed as a bundle of rights including the right to possess, use, manage, consume, and alienate.",
      "true", "Jurisprudence", "beginner", "Jurisprudence", "Ownership Concept", None,
      "As analyzed by Salmond and Honoré, ownership is not a single tangible physical thing, but a bundle of legal incidents: right to possess, use, manage, capital, security, and transmissibility.",
      "Distinguished from possession (factual control).",
      "Ownership can be corporeal or incorporeal, sole or co-ownership, legal or equitable.",
      None, None,
      U_SC, "Jurisprudence & Legal Theory", ["Ownership", "Bundle of Rights", "Honoré", "Salmond", "Property Concept"])

    m("Legal possession requires only the physical control over an object (corpus possessionis) without any mental element.",
      "false", "Jurisprudence", "intermediate", "Jurisprudence", "Possession Theory", None,
      "Under classical jurisprudence (Savigny, Salmond, Holmes), possession requires both elements: physical power/control (corpus possessionis) AND the mental intention to hold the object as one's own (animus possidendi).",
      "Holding an object for another without animus (custody/detention) is not possession.",
      "Both corpus and animus must concur to establish legal possession.",
      "requires only the physical control over an object (corpus possessionis) without any mental element", "requires both physical control (corpus) and mental intent to exclude others (animus)",
      U_SC, "Jurisprudence & Legal Theory", ["Possession", "Corpus Possessionis", "Animus Possidendi", "Savigny", "Salmond"])

    m("A corporation is an artificial legal person possessing an identity entirely separate and distinct from its individual shareholders.",
      "true", "Jurisprudence", "beginner", "Jurisprudence", "Salomon v. Salomon", None,
      "Salomon v. Salomon & Co. Ltd. (1897) affirmed the principle of separate legal personality: a company is in law a distinct person, neither agent nor trustee of its shareholders.",
      "Company can own property, sue and be sued in its own name, and has perpetual succession.",
      "Corporate veil can be pierced in cases of fraud or tax evasion.",
      None, None,
      U_SC, "Jurisprudence & Legal Theory", ["Corporate Personality", "Salomon v. Salomon", "Separate Entity", "Corporate Veil", "Legal Person"])

    m("The Ratio Decidendi of a judicial decision is the binding legal principle upon which the court decided the material facts of the case.",
      "true", "Jurisprudence", "beginner", "Jurisprudence", "Precedent Theory", None,
      "The ratio decidendi is the rule of law on which the judgment is founded and which forms the binding precedent under Article 141 (Goodhart's material facts test / Wambaugh's inversion test).",
      "Distinguished from obiter dicta which are passing judicial remarks.",
      "Lower courts are bound strictly by the ratio.",
      None, None,
      U_SC, "Jurisprudence & Legal Theory", ["Ratio Decidendi", "Binding Precedent", "Goodhart Test", "Wambaugh", "Article 141"])

    m("Obiter Dicta uttered by judges in judgments carry binding statutory authority equal to enacted legislation.",
      "false", "Jurisprudence", "beginner", "Jurisprudence", "Precedent Theory", None,
      "Obiter dicta (things said by the way) are judicial observations not strictly necessary for the decision. They possess persuasive value but lack binding authority as precedents (State of Orissa v. Sudhansu Sekhar Misra).",
      "Candidates mistakenly treat every line in a Supreme Court judgment as binding law under Article 141.",
      "Supreme Court obiter dicta are entitled to high respect but are not binding enactments.",
      "carry binding statutory authority equal to enacted legislation", "possess persuasive value but lack binding authoritative effect as precedent",
      U_SC, "Jurisprudence & Legal Theory", ["Obiter Dicta", "Persuasive Value", "Precedent", "Ratio Decidendi", "Jurisprudence"])

    m("A custom to have the force of law in India must be ancient, continuous, certain, reasonable, and not opposed to statutory law or public policy.",
      "true", "Jurisprudence", "beginner", "Jurisprudence", "Sources of Law", None,
      "To be recognized as a valid source of law, a custom must fulfill all judicial tests: antiquity (immemorial), continuity, certainty, reasonableness, peaceful enjoyment, and conformity with statute and public policy.",
      "Custom overriding statutory enactment is void in modern positive law.",
      "Burden of proving a custom lies on the party asserting it.",
      None, None,
      U_SC, "Jurisprudence & Legal Theory", ["Custom", "Source of Law", "Antiquity", "Certainty", "Public Policy"])

    # ---------------------------------------------------------
    # 12. LEGAL MAXIMS & LANDMARK PRECEDENTS (25 items)
    # ---------------------------------------------------------
    m("The maxim 'Actus non facit reum nisi mens sit rea' means that an act does not make a person guilty unless the mind is also guilty.",
      "true", "Legal Maxims & Landmark Cases", "beginner", "Legal Maxims", "Mens Rea Principle", None,
      "This fundamental maxim of criminal jurisprudence requires the concurrence of an unlawful act (actus reus) and a blameworthy mental state (mens rea) to establish criminal culpability (Fowler v. Padget).",
      "Subject to statutory strict liability offences (e.g. food adulteration, traffic violations).",
      "Reflected in BNS general exceptions (Sections 14-44).",
      None, None,
      U_SC, "Judicial Precedents & Legal Maxims", ["Mens Rea", "Actus Reus", "Criminal Liability", "Legal Maxim", "General Exceptions"])

    m("The maxim 'Ignorantia facti excusat, ignorantia juris non excusat' means that ignorance of law excuses but ignorance of fact does not.",
      "false", "Legal Maxims & Landmark Cases", "beginner", "Legal Maxims", "Ignorance Principle", None,
      "The maxim means exactly the opposite: ignorance of fact excuses (Section 14 BNS / Section 79 IPC / Section 20 ICA), but ignorance of law does not excuse (Section 21 ICA / State of Maharashtra v. Mayer Hans George).",
      "A frequent inversion trap in objective examinations.",
      "Every person subject to the law is presumed to know the law of the land.",
      "ignorance of law excuses but ignorance of fact does not", "ignorance of fact excuses, whereas ignorance of law does not excuse",
      U_SC, "Judicial Precedents & Legal Maxims", ["Ignorantia Facti", "Ignorantia Juris", "Mistake of Fact", "Mistake of Law", "Legal Maxim"])

    m("The maxim 'Ubi jus ibi remedium' means that where there is a right, the law provides a remedy.",
      "true", "Legal Maxims & Landmark Cases", "beginner", "Legal Maxims", "Ashby v. White", None,
      "Laid down in Ashby v. White (1703): if a person has a recognized legal right, they must have a means to vindicate and maintain it, and a remedy if injured in the enjoyment.",
      "Core rationale behind writ petitions under Article 32 and Article 226.",
      "Without remedy, a legal right is an empty illusion.",
      None, None,
      U_SC, "Judicial Precedents & Legal Maxims", ["Ubi Jus Ibi Remedium", "Ashby v. White", "Remedy", "Legal Right", "Legal Maxim"])

    m("The maxim 'Audi alteram partem' embodies the rule of natural justice that no person should be condemned unheard.",
      "true", "Legal Maxims & Landmark Cases", "beginner", "Legal Maxims", "Natural Justice", None,
      "Audi alteram partem requires that before an adverse administrative or judicial order is passed, the affected person must be given fair notice of charges and reasonable opportunity to be heard (Maneka Gandhi).",
      "Includes right to cross-examine adverse witnesses in disciplinary inquiries.",
      "Excluded in extreme emergencies or where statute expressly or impliedly excludes it.",
      None, None,
      U_SC, "Judicial Precedents & Legal Maxims", ["Audi Alteram Partem", "Natural Justice", "Right to Hearing", "Maneka Gandhi", "Administrative Law"])

    m("The maxim 'Nemo judex in causa sua' provides that no person shall be a judge in their own cause, prohibiting all forms of bias.",
      "true", "Legal Maxims & Landmark Cases", "beginner", "Legal Maxims", "Rule Against Bias", None,
      "This pillar of natural justice prohibits pecuniary bias, personal bias, subject-matter bias, or official bias (A.K. Kraipak v. Union of India / Dimes v. Grand Junction Canal).",
      "Pecuniary bias, however small, disqualifies a judge automatically.",
      "Real likelihood of bias is the standard test.",
      None, None,
      U_SC, "Judicial Precedents & Legal Maxims", ["Nemo Judex In Causa Sua", "Rule Against Bias", "A.K. Kraipak", "Natural Justice", "Judicial Impartiality"])

    m("The maxim 'Delegatus non potest delegare' means that a delegate can sub-delegate their statutory powers freely without legislative authorization.",
      "false", "Legal Maxims & Landmark Cases", "beginner", "Legal Maxims", "Sub-delegation Principle", None,
      "The maxim strictly means that a delegate cannot further delegate their power unless the parent statute expressly or by necessary implication authorizes sub-delegation (Barium Chemicals Ltd. v. Company Law Board).",
      "Administrative bodies often unlawfully sub-delegate executive tasks.",
      "Only purely ministerial acts can be performed through subordinates.",
      "can sub-delegate their statutory powers freely without legislative authorization", "cannot further delegate their statutory power unless authorized by statute",
      U_SC, "Judicial Precedents & Legal Maxims", ["Delegatus Non Potest Delegare", "Sub-delegation", "Administrative Law", "Barium Chemicals", "Legal Maxim"])

    m("The maxim 'Expressio unius est exclusio alterius' means that the express mention of one thing excludes all others.",
      "true", "Legal Maxims & Landmark Cases", "intermediate", "Legal Maxims", "Statutory Interpretation", None,
      "Used in statutory construction: where a statute explicitly mentions specific items or persons, it implies the intentional exclusion of items or persons of the same class not mentioned.",
      "Must be applied with caution as it is a tool of construction, not an absolute rule of law.",
      "Subordinate to legislative intent.",
      None, None,
      U_SC, "Judicial Precedents & Legal Maxims", ["Expressio Unius", "Exclusion", "Statutory Interpretation", "Legislative Intent", "Legal Maxim"])

    m("The maxim 'Noscitur a sociis' means that the meaning of an unclear word in a statute is judged and derived from the company of associated words.",
      "true", "Legal Maxims & Landmark Cases", "intermediate", "Legal Maxims", "Statutory Interpretation", None,
      "Noscitur a sociis instructs that dubious words may be understood by reference to associated words in the same statutory sentence (State of Assam v. Ranga Muhammad).",
      "Associated words color and restrict ambiguous terminology.",
      "Broader principle under which ejusdem generis is a specific application.",
      None, None,
      U_SC, "Judicial Precedents & Legal Maxims", ["Noscitur A Sociis", "Associated Words", "Interpretation of Statutes", "Contextual Meaning", "Legal Maxim"])

    m("The rule of 'Ejusdem Generis' applies when specific words belonging to a distinct category are followed by general words, confining general words to the same class.",
      "true", "Legal Maxims & Landmark Cases", "intermediate", "Legal Maxims", "Statutory Interpretation", None,
      "Ejusdem generis (of the same kind) requires: (1) enumeration of specific words, (2) forming a distinct genus or category, (3) followed by general words (Kavalappara Kochuni v. State of Madras).",
      "If specific words do not form a distinct genus, the rule does not apply.",
      "Prevents general words from being given unlimited scope contrary to context.",
      None, None,
      U_SC, "Judicial Precedents & Legal Maxims", ["Ejusdem Generis", "Statutory Interpretation", "Distinct Genus", "General Words", "Legal Maxim"])

    m("The maxim 'Generalia specialibus non derogant' means that general statutory provisions automatically override special statutory provisions.",
      "false", "Legal Maxims & Landmark Cases", "intermediate", "Legal Maxims", "Statutory Conflict", None,
      "The maxim means the exact opposite: general provisions do NOT derogate from special provisions; a special statute overrides a general statute on the specific subject matter (LIC v. D.J. Bahadur / St. Stephen's College).",
      "Frequent examination trap confusing generalia with specialia.",
      "Special enactments prevail unless legislature clearly intended to repeal the special law.",
      "general statutory provisions automatically override special statutory provisions", "special statutory provisions prevail over general provisions and are not derogated by them",
      U_SC, "Judicial Precedents & Legal Maxims", ["Generalia Specialibus", "Special Law Overrides General", "Statutory Interpretation", "Conflict of Laws", "Legal Maxim"])

    m("The maxim 'Salus populi suprema lex esto' establishes that the welfare of the people is the supreme law.",
      "true", "Legal Maxims & Landmark Cases", "beginner", "Legal Maxims", "Public Welfare", None,
      "Cicero's maxim asserts that public interest and welfare of the community transcend private individual conveniences, underpinning state emergency powers, police power, and public health regulations.",
      "Forms the constitutional basis for eminent domain and public welfare restrictions.",
      "Must still comply with basic rule of law and constitutional proportionality.",
      None, None,
      U_SC, "Judicial Precedents & Legal Maxims", ["Salus Populi", "Supreme Law", "Public Welfare", "Eminent Domain", "Legal Maxim"])

    m("The maxim 'Pacta sunt servanda' is a foundational principle of international and contract law meaning that agreements must be kept.",
      "true", "Legal Maxims & Landmark Cases", "beginner", "Legal Maxims", "Sanctity of Contracts", None,
      "Pacta sunt servanda affirms that contracts and treaties entered into freely are binding on the parties and must be executed in good faith.",
      "Codified in Article 26 of the Vienna Convention on the Law of Treaties.",
      "Subject to exceptional doctrines like frustration (rebus sic stantibus / Section 56 ICA).",
      None, None,
      U_SC, "Judicial Precedents & Legal Maxims", ["Pacta Sunt Servanda", "Good Faith", "Treaty Binding", "Contract Sanctity", "International Law"])

    m("Kesavananda Bharati v. State of Kerala (1973) established by a 7:6 majority that Parliament has unlimited power to abrogate the Basic Structure of the Constitution.",
      "false", "Legal Maxims & Landmark Cases", "beginner", "Landmark Precedents", "Kesavananda Bharati (1973)", None,
      "The historic 13-judge bench held that while Parliament has wide power to amend under Article 368, it cannot alter the Basic Structure or framework of the Constitution.",
      "A frequent false statement in competitive exams.",
      "Basic features include supremacy of the Constitution, republican democracy, secularism, separation of powers, and judicial review.",
      "Parliament has unlimited power to abrogate the Basic Structure", "Parliament's amending power cannot damage or destroy the Basic Structure of the Constitution",
      U_SC, "Judicial Precedents & Landmark Cases", ["Kesavananda Bharati", "Basic Structure", "Article 368", "13-judge Bench", "Constitutional Limits"])

    m("Maneka Gandhi v. Union of India (1978) established that the procedure depriving a person of liberty under Article 21 must be just, fair, and reasonable.",
      "true", "Legal Maxims & Landmark Cases", "beginner", "Landmark Precedents", "Maneka Gandhi (1978)", None,
      "Overruled the formalistic interpretation in A.K. Gopalan (1950), reading the American substantive due process concept into Article 21 by requiring procedure established by law to be just, fair, and reasonable, tested against Articles 14 and 19 (the Golden Triangle).",
      "Passports cannot be impounded arbitrarily without hearing.",
      "Expanded Article 21 into the reservoir of fundamental human rights.",
      None, None,
      U_SC, "Judicial Precedents & Landmark Cases", ["Maneka Gandhi", "Article 21", "Just Fair Reasonable", "Golden Triangle", "Due Process"])

    m("Vishaka v. State of Rajasthan (1997) laid down binding guidelines to prevent sexual harassment of women at workplaces pending statutory enactment.",
      "true", "Legal Maxims & Landmark Cases", "beginner", "Landmark Precedents", "Vishaka Guidelines", None,
      "Invoking Articles 14, 19, 21, and the CEDAW Convention under Article 141 and 51(c), the Supreme Court laid down comprehensive guidelines that governed India until the POSH Act, 2013 was enacted.",
      "Exemplified judicial law-making to fill legislative vacuums under Article 141.",
      "Mandated Internal Complaints Committees in every establishment.",
      None, None,
      U_SC, "Judicial Precedents & Landmark Cases", ["Vishaka", "Workplace Harassment", "Article 141", "CEDAW", "POSH Act"])

    m("D.K. Basu v. State of West Bengal (1997) mandated eleven binding guidelines for police officers during arrest and detention to prevent custodial violence.",
      "true", "Legal Maxims & Landmark Cases", "beginner", "Landmark Precedents", "D.K. Basu (1997)", None,
      "The Supreme Court laid down 11 mandatory requirements including identification tags for police, memo of arrest, right of arrestee to inform a friend/relative, and medical examination every 48 hours.",
      "Failure of police to comply constitutes contempt of court and departmental action.",
      "Substantially incorporated into BNSS Sections 37, 47, 48, and 51.",
      None, None,
      U_SC, "Judicial Precedents & Landmark Cases", ["D.K. Basu", "Arrest Guidelines", "Custodial Violence", "Arrest Memo", "Police Accountability"])

    m("Navtej Singh Johar v. Union of India (2018) decriminalized consensual adult same-sex relations by reading down Section 377 of the IPC.",
      "true", "Legal Maxims & Landmark Cases", "beginner", "Landmark Precedents", "Navtej Johar (2018)", None,
      "A 5-judge Constitution Bench held that criminalizing consensual sexual acts between adults violates Articles 14, 15, 19, and 21, overruling Suresh Kumar Koushal (2014).",
      "Affirmed constitutional morality over public morality.",
      "Non-consensual sexual acts and acts on children remain criminal offences.",
      None, None,
      U_SC, "Judicial Precedents & Landmark Cases", ["Navtej Johar", "Section 377", "LGBTQ Rights", "Constitutional Morality", "Article 21"])

    m("Joseph Shine v. Union of India (2018) struck down Section 497 of the IPC (Adultery) as unconstitutional for treating a woman as property of her husband.",
      "true", "Legal Maxims & Landmark Cases", "beginner", "Landmark Precedents", "Joseph Shine (2018)", None,
      "The Supreme Court held Section 497 IPC violated Articles 14, 15, and 21 by treating a married woman as chattel of her husband and denying her sexual autonomy.",
      "Adultery remains a valid civil ground for divorce under matrimonial statutes.",
      "Not reenacted in the Bharatiya Nyaya Sanhita, 2023.",
      None, None,
      U_SC, "Judicial Precedents & Landmark Cases", ["Joseph Shine", "Section 497", "Adultery Unconstitutional", "Gender Equality", "Matrimonial Law"])

    m("Shayara Bano v. Union of India (2017) declared the practice of Talaq-e-biddat (instant triple talaq) unconstitutional and void by a 3:2 majority.",
      "true", "Legal Maxims & Landmark Cases", "beginner", "Landmark Precedents", "Shayara Bano (2017)", None,
      "The Supreme Court ruled that Talaq-e-biddat is manifest arbitrariness violating Article 14 and is not an essential religious practice under Article 25.",
      "Led to the enactment of the Muslim Women (Protection of Rights on Marriage) Act, 2019.",
      "Recognized that statutory personal laws are subject to constitutional scrutiny.",
      None, None,
      U_SC, "Judicial Precedents & Landmark Cases", ["Shayara Bano", "Triple Talaq", "Article 14", "Manifest Arbitrariness", "Essential Religious Practice"])

    m("Common Cause v. Union of India (2018) recognized the right to die with dignity, legalizing passive euthanasia and Advance Medical Directives (living wills).",
      "true", "Legal Maxims & Landmark Cases", "beginner", "Landmark Precedents", "Common Cause (2018)", None,
      "A 5-judge Constitution Bench held that the right to die with dignity is an intrinsic part of the Right to Life under Article 21, permitting withdrawal of life support for terminally ill patients in permanent vegetative state.",
      "Active euthanasia remains strictly illegal in India.",
      "Guidelines for living wills were streamlined in 2023.",
      None, None,
      U_SC, "Judicial Precedents & Landmark Cases", ["Common Cause", "Passive Euthanasia", "Living Will", "Die with Dignity", "Article 21"])

    m("In Indra Sawhney v. Union of India (1992), the 9-judge bench ruled that the total reservation under Article 16(4) should ordinarily not exceed fifty percent.",
      "true", "Legal Maxims & Landmark Cases", "beginner", "Landmark Precedents", "Mandal Case (1992)", None,
      "The landmark Mandal judgment upheld 27% OBC reservations, mandated exclusion of the creamy layer, and established the 50% cap on total reservations.",
      "Reservation in promotions was initially barred (subsequently modified by 77th and 81st amendments).",
      "The 50% rule was reaffirmed in M. Nagaraj and Jarnail Singh.",
      None, None,
      U_SC, "Judicial Precedents & Landmark Cases", ["Indra Sawhney", "Reservation Cap", "Fifty Percent", "Creamy Layer", "Article 16(4)"])

    m("S.R. Bommai v. Union of India (1994) held that secularism is a basic feature of the Constitution and state governments pursuing unsecular policies can be dismissed under Article 356.",
      "true", "Legal Maxims & Landmark Cases", "beginner", "Landmark Precedents", "S.R. Bommai (1994)", None,
      "A 9-judge bench held that secularism is part of the Basic Structure; any state government acting against secularism can be subjected to President's Rule under Article 356.",
      "Proclamation under Article 356 is subject to judicial review.",
      "Legislative Assembly cannot be dissolved until Parliament approves the proclamation.",
      None, None,
      U_SC, "Judicial Precedents & Landmark Cases", ["S.R. Bommai", "Secularism", "Article 356", "Basic Structure", "Federalism"])

    m("M.C. Mehta v. Kamal Nath (1997) held that the Doctrine of Public Trust is part of the law of the land in India.",
      "true", "Legal Maxims & Landmark Cases", "beginner", "Landmark Precedents", "Public Trust Doctrine", None,
      "The Supreme Court ruled that certain natural resources (rivers, forests, seashores) are held by the State in trust for the general public and cannot be converted into private commercial ownership (Span Motel case).",
      "Based on Roman law and ancient common law doctrine.",
      "Derived from Article 21 right to life and healthy environment.",
      None, None,
      U_SC, "Judicial Precedents & Landmark Cases", ["Public Trust Doctrine", "Kamal Nath", "Environmental Law", "Span Motel", "Article 21"])

    m("A.K. Kraipak v. Union of India (1969) established that the rules of Natural Justice apply to administrative inquiries as well as quasi-judicial proceedings.",
      "true", "Legal Maxims & Landmark Cases", "beginner", "Landmark Precedents", "A.K. Kraipak (1969)", None,
      "Hegde J. held that the dividing line between an administrative power and a quasi-judicial power is quite thin and being gradually obliterated; the aim of both is to arrive at a just decision, so natural justice applies to both.",
      "An acting candidate participating in selection board vitiated the selection on ground of personal bias.",
      "Cornerstone of modern Indian administrative law.",
      None, None,
      U_SC, "Judicial Precedents & Landmark Cases", ["A.K. Kraipak", "Natural Justice", "Administrative Inquiries", "Rule Against Bias", "Administrative Law"])

    m("Lalita Kumari v. Government of Uttar Pradesh (2014) held that registration of an FIR under Section 154 of the CrPC is mandatory if information discloses a cognizable offence.",
      "true", "Legal Maxims & Landmark Cases", "beginner", "Landmark Precedents", "Lalita Kumari (2014)", None,
      "A 5-judge Constitution Bench held that Section 154 CrPC uses the mandatory word 'shall': police cannot conduct a preliminary inquiry when information discloses a cognizable offence.",
      "Preliminary inquiry permitted only in narrow categories like matrimonial disputes, medical negligence, corruption, or 3-month unexplained delays.",
      "Incorporated with 14-day statutory cap in BNSS Section 173(3).",
      None, None,
      U_SC, "Judicial Precedents & Landmark Cases", ["Lalita Kumari", "Mandatory FIR", "Section 154", "Cognizable Offence", "BNSS 173"])

    print("Part 3: 105 items registered.")
