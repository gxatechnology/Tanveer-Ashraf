# Append Chapter 3 (Vested/Contingent, Conditional Transfers, Election) to data_tpa_mcqs_1.py (30 MCQs)
import json

def q(id_, ch, top, text, opts, ans_idx, letter, exp, bk, diff, prov, obj):
    return {
        "id": id_,
        "subjectId": "law-tpa",
        "chapterId": ch,
        "topicId": top,
        "question": text,
        "options": opts,
        "answer": ans_idx,
        "answerLetter": letter,
        "explanation": exp,
        "optionBreakdown": bk,
        "difficulty": diff,
        "provision": prov,
        "sourceUrl": "https://legislative.gov.in",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": obj,
        "eligible": True,
        "status": "active"
    }

with open('scripts/data_tpa_mcqs_1.py', 'r', encoding='utf-8') as f:
    txt = f.read()
start = txt.find('[')
end = txt.rfind(']')
data = json.loads(txt[start:end+1])

# --- CH-03 TOPIC 01: Vested vs Contingent (Sections 19, 21) ---
data.append(q("mcq-tpa-03-001", "ch-tpa-03", "top-tpa-03-01",
    "Under Section 19 of the Transfer of Property Act, an interest is 'vested' when it is created in favor of a person:",
    ["Without specifying the time when it is to take effect, or specifying that it is to take effect forthwith, or on the happening of an event which must happen", "Dependent upon an event which may or may not happen", "Subject to the sole discretion of the transferor", "Only after 50 years"],
    0, "A",
    "Section 19 defines vested interest: without specifying time, or forthwith, or on an event which must inevitably happen (e.g. death of a person).",
    {"A": "Correct. Section 19 statutory definition of vested interest.", "B": "This describes a contingent interest under Section 21.", "C": "Discretion of transferor negates vested right.", "D": "No 50-year requirement."},
    "Easy", "Transfer of Property Act, 1882, Section 19", "Recall definition of vested interest under Section 19."))

data.append(q("mcq-tpa-03-002", "ch-tpa-03", "top-tpa-03-01",
    "Under Section 19 Explanation, an interest is NOT prevented from being vested by which of the following circumstances?",
    ["A direction that its enjoyment shall be postponed, or that a prior interest in the same property is given to another person", "An accumulation of income direction", "A provision that if a specified uncertain event happens, the interest shall pass to another (vested subject to divestment)", "All of the above"],
    3, "D",
    "Explanation to Section 19 lists conditions that do not prevent vesting: postponement of enjoyment, prior estate, accumulation, or clause for divestment.",
    {"A": "Postponement of possession/prior estate does not prevent vesting.", "B": "Accumulation direction does not delay vesting of title.", "C": "Vesting subject to divestment is still a vested interest.", "D": "Correct. All of the listed conditions leave the interest vested."},
    "Medium", "Transfer of Property Act, 1882, Section 19 Explanation", "Identify factors not preventing vesting under Section 19."))

data.append(q("mcq-tpa-03-003", "ch-tpa-03", "top-tpa-03-01",
    "What is the crucial legal effect of the death of a holder of a 'vested interest' before obtaining possession?",
    ["The interest does not defeat, but passes to his legal heirs or representatives by succession", "The interest lapses completely and reverts to the grantor", "The interest is forfeited to the State", "The property must be sold at auction"],
    0, "A",
    "Under Section 19, a vested interest is heritable and alienable; the death of the transferee before possession does not defeat the interest, which devolves on his heirs.",
    {"A": "Correct. Vested interest is heritable and passes to legal heirs.", "B": "Does not lapse on death.", "C": "No state forfeiture.", "D": "No forced auction."},
    "Easy", "Transfer of Property Act, 1882, Section 19", "Recall heritability of vested interest."))

data.append(q("mcq-tpa-03-004", "ch-tpa-03", "top-tpa-03-01",
    "Under Section 21 of the Transfer of Property Act, an interest is 'contingent' when it is created in favor of a person to take effect only:",
    ["On the happening of a specified uncertain event, or if a specified uncertain event shall not happen", "Forthwith upon execution of the deed", "On the death of the transferor (an event which must happen)", "Whenever the transferee attains 18 years, having already been born"],
    0, "A",
    "Section 21 defines contingent interest: takes effect only on the happening or non-happening of a specified uncertain event (condition precedent).",
    {"A": "Correct. Section 21 definition of contingent interest.", "B": "Forthwith creates an immediately vested interest.", "C": "Death is certain; so life estate creates vested remainder.", "D": "Attaining age is contingent until age is reached, but Section 21 Exception saves certain maintenance cases."},
    "Easy", "Transfer of Property Act, 1882, Section 21", "Recall statutory definition of contingent interest under Section 21."))

data.append(q("mcq-tpa-03-005", "ch-tpa-03", "top-tpa-03-01",
    "What is the legal effect if the person having a 'contingent interest' dies before the happening of the uncertain event?",
    ["The contingent interest fails and does not pass to his heirs", "The interest vests automatically in his legal heirs", "The grantor's estate is held liable in damages", "The property is transferred to the court"],
    0, "A",
    "A contingent interest depends on personal fulfillment of the condition precedent; if the contingent grantee dies before the event happens, the interest fails.",
    {"A": "Correct. Contingent interest fails on death before fulfillment of condition.", "B": "Heirs cannot inherit an interest that never vested.", "C": "No damages against grantor.", "D": "Court takes no title."},
    "Medium", "Transfer of Property Act, 1882, Section 21", "Explain consequence of death of contingent interest holder."))

data.append(q("mcq-tpa-03-006", "ch-tpa-03", "top-tpa-03-01",
    "Under the Exception to Section 21 of the TPA, where a person becomes entitled to an interest upon attaining a specified age, and the transferor also gives him absolutely the income to arise from such interest before he reaches that age:",
    ["Such interest is NOT contingent, but vested", "Such interest is void for uncertainty", "Such interest remains contingent until age is reached", "The income is forfeited to the donor"],
    0, "A",
    "Exception to Section 21: Gift of intermediate income for maintenance or benefit converts what would otherwise be a contingent interest into an immediately vested interest.",
    {"A": "Correct. Gift of intermediate income creates a vested interest under Section 21 Exception.", "B": "It is completely valid.", "C": "It is converted from contingent to vested.", "D": "Beneficiary receives the income."},
    "Hard", "Transfer of Property Act, 1882, Section 21 Exception", "Master Exception to Section 21 on intermediate income."))

data.append(q("mcq-tpa-03-007", "ch-tpa-03", "top-tpa-03-01",
    "A transfers property to B for life, and after B's death to C. What is the nature of C's interest during B's lifetime?",
    ["Vested remainder", "Contingent interest", "Spes successionis", "A mere licence"],
    0, "A",
    "Because B's death is an event that must inevitably happen, C's interest is a vested remainder taking effect in possession upon B's death.",
    {"A": "Correct. B's death is certain; C holds a vested remainder.", "B": "Not contingent because death is certain to occur.", "C": "Not spes successionis; C has a present property right.", "D": "It is a proprietary estate, not a personal licence."},
    "Easy", "Transfer of Property Act, 1882, Section 19", "Identify vested remainder after life estate."))

data.append(q("mcq-tpa-03-008", "ch-tpa-03", "top-tpa-03-01",
    "A transfers property to B if B marries C. What is the nature of B's interest before marriage?",
    ["Contingent interest", "Vested interest", "Absolute fee simple", "Easementary right"],
    0, "A",
    "Marrying C is an uncertain future event that may or may not happen; therefore, B's interest is contingent under Section 21.",
    {"A": "Correct. Contingent on uncertain future event of marriage.", "B": "Not vested until marriage takes place.", "C": "No present absolute estate.", "D": "Not an easement."},
    "Easy", "Transfer of Property Act, 1882, Section 21", "Classify conditional marriage transfer under Section 21."))

data.append(q("mcq-tpa-03-009", "ch-tpa-03", "top-tpa-03-01",
    "Can a 'vested interest' be attached and sold in execution of a money decree under Section 60 of the Code of Civil Procedure?",
    ["Yes, a vested interest is attachable and saleable in execution", "No, only tangible cash can be attached", "Only with permission of the High Court", "Only after the death of the life tenant"],
    0, "A",
    "Under Section 60 CPC and Section 19 TPA, a vested interest is an existing present property right and is fully liable to attachment and sale in execution of a decree.",
    {"A": "Correct. Vested interests are attachable under Section 60 CPC.", "B": "Property interests of all kinds are attachable.", "C": "No High Court permission required.", "D": "Can be attached during life tenancy."},
    "Medium", "Code of Civil Procedure, 1908, Section 60 & TPA Section 19", "Assess attachability of vested interest."))

data.append(q("mcq-tpa-03-010", "ch-tpa-03", "top-tpa-03-01",
    "Can a 'contingent interest' be attached and sold in execution of a decree under Section 60 CPC?",
    ["No, Section 60(1)(m) CPC specifically exempts a contingent interest from attachment and sale", "Yes, all contingent rights can be auctioned", "Only in suits between banks and borrowers", "Only if the decree exceeds Rs 10 lakhs"],
    0, "A",
    "Section 60(1)(m) of the Code of Civil Procedure expressly exempts a contingent interest from attachment and sale in execution.",
    {"A": "Correct. Contingent interest is expressly exempt from attachment under Section 60(1)(m) CPC.", "B": "Cannot be auctioned in execution.", "C": "Applies uniformly.", "D": "No monetary threshold."},
    "Hard", "Code of Civil Procedure, 1908, Section 60(1)(m)", "Identify statutory bar on attachment of contingent interest."))

# --- CH-03 TOPIC 02: Conditional Transfers (Sections 25–34) ---
data.append(q("mcq-tpa-03-011", "ch-tpa-03", "top-tpa-03-02",
    "Under Section 25 of the Transfer of Property Act, an interest created on a condition precedent fails if the condition is:",
    ["Impossible, forbidden by law, defeats provisions of law, fraudulent, involves injury to person/property, or is immoral/opposed to public policy", "Difficult to perform", "Expressed in a foreign language", "Not approved by the district magistrate"],
    0, "A",
    "Section 25 mirrors Section 23 of the Contract Act: an interest created on a condition precedent fails if the condition is impossible, unlawful, fraudulent, or immoral.",
    {"A": "Correct. Section 25 statutory grounds of invalid condition precedent.", "B": "Mere difficulty does not invalidate a condition.", "C": "Language is irrelevant.", "D": "Magistrate approval is not required."},
    "Easy", "Transfer of Property Act, 1882, Section 25", "Recall invalid conditions precedent under Section 25."))

data.append(q("mcq-tpa-03-012", "ch-tpa-03", "top-tpa-03-02",
    "Under Section 25, Illustration (b): A transfers Rs 500 to B on condition that he shall murder C. What is the legal effect?",
    ["The transfer is void because the condition precedent is unlawful", "B gets Rs 500 without committing murder", "B is entitled to Rs 250 as an advance", "The transfer is voidable at B's option"],
    0, "A",
    "Illustration (b) to Section 25: A condition precedent to commit murder is unlawful (forbidden by law); the transfer fails and is void.",
    {"A": "Correct. Transfer fails under Section 25 and Illustration (b).", "B": "B gets nothing because condition precedent failed.", "C": "No advance payment.", "D": "Void, not voidable."},
    "Easy", "Transfer of Property Act, 1882, Section 25 Illustration (b)", "Apply Section 25 unlawful condition illustration."))

data.append(q("mcq-tpa-03-013", "ch-tpa-03", "top-tpa-03-02",
    "Under Section 26 of the Transfer of Property Act, what standard of compliance is required for a 'condition precedent'?",
    ["Substantial compliance: where the condition precedent is substantially complied with, it is deemed to have been fulfilled", "Strict literal 100% compliance without any variation", "Compliance to the personal satisfaction of the transferor", "Compliance approved by a civil court"],
    0, "A",
    "Section 26 embodies the doctrine of cy-pres for conditions precedent: substantial compliance is sufficient (e.g. consent of majority of trustees where one died).",
    {"A": "Correct. Section 26 requires substantial compliance for condition precedent.", "B": "Strict literal compliance is rejected under Section 26.", "C": "Objective substantial fulfillment suffices.", "D": "No court pre-approval required."},
    "Medium", "Transfer of Property Act, 1882, Section 26", "Recall substantial compliance rule for condition precedent under Section 26."))

data.append(q("mcq-tpa-03-014", "ch-tpa-03", "top-tpa-03-02",
    "Under Section 28 of the Transfer of Property Act, a 'conditional limitation' (gift over) is a disposition where:",
    ["An interest is created to accrue to any person with the condition that it shall cease to exist in case a specified uncertain event happens or does not happen, and pass to another person", "An interest is leased for 99 years", "A mortgage is converted into a sale", "A donee is made a trustee"],
    0, "A",
    "Section 28 governs conditional limitation (executory limitation): an interest divests upon a condition subsequent and shifts over to another person.",
    {"A": "Correct. Section 28 definition of conditional limitation / gift over.", "B": "Lease is not a conditional limitation.", "C": "Mortgage conversion is not gift over.", "D": "Trust creation is governed by Trusts Act."},
    "Medium", "Transfer of Property Act, 1882, Section 28", "Identify conditional limitation under Section 28."))

data.append(q("mcq-tpa-03-015", "ch-tpa-03", "top-tpa-03-02",
    "Under Section 29 of the Transfer of Property Act, what standard of compliance is required for a 'condition subsequent' to divest an already vested estate?",
    ["Strict compliance: an ulterior disposition cannot take effect unless the condition is strictly fulfilled", "Substantial compliance only", "Partial compliance of 50%", "Symbolic compliance"],
    0, "A",
    "Section 29: An ulterior disposition divesting a prior vested estate cannot take effect unless the condition is strictly fulfilled (law leans against divestment).",
    {"A": "Correct. Section 29 mandates strict fulfillment for condition subsequent.", "B": "Substantial compliance applies to condition precedent (S.26), not condition subsequent (S.29).", "C": "Partial compliance is insufficient to divest.", "D": "Symbolic compliance cannot divest vested estate."},
    "Hard", "Transfer of Property Act, 1882, Section 29", "Contrast Section 26 (substantial) with Section 29 (strict compliance)."))

data.append(q("mcq-tpa-03-016", "ch-tpa-03", "top-tpa-03-02",
    "What is the fundamental difference between a 'condition precedent' and a 'condition subsequent'?",
    ["A condition precedent must be fulfilled before the estate can vest; a condition subsequent operates after the estate has vested, divesting or extinguishing it", "Condition precedent is void; condition subsequent is valid", "Condition precedent applies only to wills", "There is no difference in property law"],
    0, "A",
    "Condition precedent delays vesting until fulfilled. Condition subsequent defeats or terminates an estate that has already vested.",
    {"A": "Correct. Precedent enables vesting; subsequent terminates existing vested estate.", "B": "Both types of conditions can be valid.", "C": "Both apply to inter vivos transfers under TPA.", "D": "They have opposite operational mechanics."},
    "Easy", "Indian Property Jurisprudence, Sections 25–34", "Distinguish condition precedent from condition subsequent."))

data.append(q("mcq-tpa-03-017", "ch-tpa-03", "top-tpa-03-02",
    "Under Section 30 of the Transfer of Property Act, if an ulterior disposition is not valid (e.g. violates perpetuities):",
    ["The prior disposition is not affected by it, and remains valid and absolute", "The prior disposition also fails and becomes void", "The entire transfer is canceled", "The property goes to the municipality"],
    0, "A",
    "Section 30: 'A prior disposition is not affected by the invalidity of the ulterior disposition'. (Prior vested estate becomes indefeasible).",
    {"A": "Correct. Section 30 rule: invalidity of gift over leaves prior estate absolute.", "B": "Prior disposition is protected.", "C": "Transfer is not canceled.", "D": "No municipal escheat."},
    "Medium", "Transfer of Property Act, 1882, Section 30", "Recall rule on invalidity of ulterior disposition under Section 30."))

data.append(q("mcq-tpa-03-018", "ch-tpa-03", "top-tpa-03-02",
    "Under Section 31 of the Transfer of Property Act, a transferor may create an interest subject to a condition that it shall cease to exist:",
    ["In case a specified uncertain event happens, or in case a specified uncertain event does not happen", "Whenever the transferor changes his mind", "Upon the transferee joining a political party", "Only with approval of the Collector"],
    0, "A",
    "Section 31 allows an interest to be made determinable upon the happening or non-happening of a specified uncertain event (condition of defeasance).",
    {"A": "Correct. Section 31 statutory rule on condition of defeasance.", "B": "Arbitrary unilateral revocation is barred under Section 10/126.", "C": "Political freedom conditions violate public policy.", "D": "Collector approval is not required."},
    "Medium", "Transfer of Property Act, 1882, Section 31", "Identify condition of defeasance under Section 31."))

data.append(q("mcq-tpa-03-019", "ch-tpa-03", "top-tpa-03-02",
    "Under Section 32 of the Transfer of Property Act, in order that a condition that an interest shall cease to exist may be valid:",
    ["It is necessary that the event to which it relates be one which could legally constitute the condition of the creation of an interest (must be lawful under Section 25)", "The condition can be completely illegal", "The condition must involve physical violence", "The condition must be unwritten"],
    0, "A",
    "Section 32: A condition of defeasance must itself be lawful; an invalid/immoral condition cannot defeat an existing vested interest.",
    {"A": "Correct. Section 32 mandates that defeasance condition must be lawful.", "B": "Illegal conditions cannot divest property.", "C": "Physical violence is unlawful.", "D": "Must be part of the transfer instrument."},
    "Medium", "Transfer of Property Act, 1882, Section 32", "Recall legality requirement for condition of defeasance under Section 32."))

data.append(q("mcq-tpa-03-020", "ch-tpa-03", "top-tpa-03-02",
    "A transfers an estate to B for life, and after B's death to C; with a proviso that if C should ever marry D, C's estate shall terminate and pass to E. C marries D. What is the result under Section 28 and 29?",
    ["C's estate is divested and passes to E, because the condition subsequent was strictly fulfilled", "C retains the estate because conditions in restraint of marriage are void", "E receives nothing", "B's life estate is revived"],
    0, "A",
    "Restraining marriage to a particular named person (D) is a partial restraint and valid; strictly fulfilled, it divests C's interest and vests in E.",
    {"A": "Correct. Valid partial restraint strictly fulfilled divests estate under Section 28/29.", "B": "Restraint of marriage to a specific person is valid.", "C": "E takes the gift over.", "D": "B is deceased; life estate cannot revive."},
    "Hard", "Transfer of Property Act, 1882, Sections 28, 29", "Apply strict fulfillment of condition subsequent."))

# --- CH-03 TOPIC 03: Doctrine of Election (Section 35) ---
data.append(q("mcq-tpa-03-021", "ch-tpa-03", "top-tpa-03-03",
    "Under Section 35 of the Transfer of Property Act, the 'Doctrine of Election' is founded on the equitable principle that:",
    ["A person who accepts a benefit under an instrument must also adopt the whole of it, conforming to all its provisions and renouncing every right inconsistent with it (allegans contraria non est audiendus)", "A person can accept beneficial parts and reject onerous parts", "Every citizen must vote in civic elections", "Election applies only between direct descendants"],
    0, "A",
    "The doctrine of election embodies the equitable maxim 'he who accepts a benefit must bear the burden' (qui approbat non reprobat): you cannot blow hot and cold.",
    {"A": "Correct. Foundational equitable principle of doctrine of election under Section 35.", "B": "Cannot pick and choose (approbate and reprobate).", "C": "Civic voting is unrelated.", "D": "Applies across all property owners."},
    "Easy", "Transfer of Property Act, 1882, Section 35", "Recall foundation of doctrine of election under Section 35."))

data.append(q("mcq-tpa-03-022", "ch-tpa-03", "top-tpa-03-03",
    "In the landmark English decision Cooper v. Cooper (1874), the House of Lords established regarding election that:",
    ["He who accepts a benefit under a deed or will must confirm the whole, giving full effect to its provisions and renouncing inconsistent rights", "Election applies only to leasehold lands", "No compensation is payable upon dissenting", "The doctrine was abolished by statute"],
    0, "A",
    "Lord Hatherley in Cooper v. Cooper held that the rule of election requires a beneficiary taking under an instrument to give full effect to that instrument.",
    {"A": "Correct. Foundational ruling establishing classical doctrine of election.", "B": "Applies to all property dispositions.", "C": "Equity requires compensation if property is retained.", "D": "Never abolished; codified in Section 35 TPA and Section 180 Succession Act."},
    "Medium", "House of Lords: Cooper v. Cooper (1874) LR 7 HL 53", "Master Cooper v Cooper doctrine of election."))

data.append(q("mcq-tpa-03-023", "ch-tpa-03", "top-tpa-03-03",
    "Under Section 35, when a person professes to transfer property which he has no right to transfer, and as part of the same transaction confers any benefit on the owner of the property:",
    ["Such owner must elect either to confirm such transfer, or to dissent from it", "The transfer is automatically void ab initio", "The owner is imprisoned for contempt", "The transferor becomes absolute owner"],
    0, "A",
    "Section 35: The owner of the property is put to election: he must either confirm the transfer or dissent from it.",
    {"A": "Correct. Section 35 statutory election obligation.", "B": "Transfer is not void ab initio; it depends on owner's election.", "C": "No contempt arises.", "D": "Transferor has no title."},
    "Easy", "Transfer of Property Act, 1882, Section 35", "Identify core statutory requirement of Section 35."))

data.append(q("mcq-tpa-03-024", "ch-tpa-03", "top-tpa-03-03",
    "Under Section 35, if the owner elects to DISSENT from the transfer:",
    ["He must relinquish the benefit conferred on him, which reverts to the transferor or his representative as if it had not been disposed of", "He can still retain the benefit conferred", "He forfeits his own property", "He must pay 50% penalty to the court"],
    0, "A",
    "Section 35: If the owner dissents, he relinquishes the benefit, which reverts to the transferor or his representative.",
    {"A": "Correct. Benefit is relinquished upon dissenting from transfer.", "B": "Cannot keep both his own property and the conferred benefit.", "C": "He retains his own property.", "D": "No court penalty."},
    "Easy", "Transfer of Property Act, 1882, Section 35", "Recall consequence of dissenting under Section 35."))

data.append(q("mcq-tpa-03-025", "ch-tpa-03", "top-tpa-03-03",
    "Under Section 35 paragraph 2, what duty is owed to a disappointed transferee when the owner dissents from the transfer?",
    ["The transferor or his representative is bound to make compensation to the disappointed transferee: in all cases where transfer is for consideration, and in gratuitous transfers if transferor died or became incapable before election", "No compensation is ever payable to disappointed transferee", "The state pays compensation", "The disappointed transferee has only criminal remedies"],
    0, "A",
    "Section 35(2): Transferee is compensated out of relinquished benefit: in all transfers for consideration, and in gifts if transferor dies/becomes incapable before election.",
    {"A": "Correct. Section 35(2) compensation rules for disappointed transferee.", "B": "Compensation is mandatory under Section 35(2).", "C": "State does not pay.", "D": "Civil restitutionary compensation."},
    "Hard", "Transfer of Property Act, 1882, Section 35 Paragraph 2", "Master compensation rules for disappointed transferee under Section 35."))

data.append(q("mcq-tpa-03-026", "ch-tpa-03", "top-tpa-03-03",
    "Under Section 35, what is the measure of compensation payable to the disappointed transferee?",
    ["The amount or value of the property attempted to be transferred to him", "Treble damages in tort", "A flat nominal sum of Rs 100", "The market value of the entire ancestral estate"],
    0, "A",
    "Section 35 paragraph 2: Compensation is limited to 'the amount or value of the property attempted to be transferred to him' (capped at the value of relinquished benefit).",
    {"A": "Correct. Value of the property attempted to be transferred.", "B": "No treble damages in equity.", "C": "Not a flat Rs 100.", "D": "Ancestral estate is unaffected."},
    "Medium", "Transfer of Property Act, 1882, Section 35", "Determine measure of compensation under Section 35."))

data.append(q("mcq-tpa-03-027", "ch-tpa-03", "top-tpa-03-03",
    "Does the doctrine of election apply if the benefit is conferred on the owner under a completely DIFFERENT and independent transaction?",
    ["No, the transfer of property and the benefit conferred must form part of the same transaction", "Yes, any past benefit across 20 years triggers election", "Yes, if both parties are merchants", "Only if decreed by an arbitrator"],
    0, "A",
    "Section 35 explicitly requires that the transfer and benefit must form 'part of the same transaction'. Independent gifts create no obligation of election.",
    {"A": "Correct. Same transaction is an indispensable requirement of Section 35.", "B": "Unrelated past benefits do not trigger election.", "C": "Merchant status does not alter rule.", "D": "Arbitration decree cannot invent same transaction."},
    "Hard", "Transfer of Property Act, 1882, Section 35", "Apply 'same transaction' requirement under Section 35."))

data.append(q("mcq-tpa-03-028", "ch-tpa-03", "top-tpa-03-03",
    "Under Section 35 paragraph 4, when does an owner's acceptance of the benefit constitute an IMPLIED election to confirm the transfer?",
    ["Where he has enjoyed the benefit for two years without doing any act of dissent, or where he has done some act which renders it impossible to place the parties in the same condition as before", "After 14 days of receipt", "If he deposits the money in a savings bank", "If he sends an email thanking the donor"],
    0, "A",
    "Section 35(4) sets out two statutory presumptions of implied election: (1) enjoyment for two years without dissent, or (2) exhaustively dealing with benefit so status quo cannot be restored.",
    {"A": "Correct. Section 35(4) two-year enjoyment and impossibility of restoration rules.", "B": "14 days does not create statutory presumption.", "C": "Deposit alone is not conclusive election.", "D": "Polite email does not waive election rights."},
    "Medium", "Transfer of Property Act, 1882, Section 35 Paragraph 4", "Identify statutory presumptions of implied election under Section 35."))

data.append(q("mcq-tpa-03-029", "ch-tpa-03", "top-tpa-03-03",
    "Under Section 35 paragraph 5, if the owner does not elect within one year after the date of transfer, what procedure may the transferor adopt?",
    ["Transferor or his representatives may require him by notice to make his election; and if he fails to do so within a reasonable time, he shall be deemed to have elected to confirm the transfer", "Transferor can arrest the owner", "Transfer is automatically canceled", "The property goes to the nearest relative"],
    0, "A",
    "Section 35(5): Requisition notice after one year; if owner fails to elect within reasonable time after notice, he is deemed to have confirmed the transfer.",
    {"A": "Correct. Requisition notice and deemed confirmation under Section 35(5).", "B": "No civil arrest for election.", "C": "Transfer is not canceled; it is deemed confirmed.", "D": "No relative devolution."},
    "Medium", "Transfer of Property Act, 1882, Section 35 Paragraph 5", "Recall requisition notice procedure under Section 35(5)."))

data.append(q("mcq-tpa-03-030", "ch-tpa-03", "top-tpa-03-03",
    "Under Section 35 paragraph 6, what is the rule regarding election where the person bound to elect is a minor or of unsound mind?",
    ["The election shall be postponed until the disability ceases, or until the election is made by his legal guardian with permission of the court", "The minor is deemed to have dissented immediately", "The transfer is void ab initio", "The property is auctioned by the court"],
    0, "A",
    "Section 35(6): Election is suspended during minority or unsoundness of mind until disability ceases, unless guardian elects with court sanction.",
    {"A": "Correct. Section 35(6) suspension of election during legal disability.", "B": "No deemed dissent against minor.", "C": "Transfer is not void ab initio.", "D": "No auction."},
    "Easy", "Transfer of Property Act, 1882, Section 35 Paragraph 6", "Recall rule on election during legal disability."))

with open('scripts/data_tpa_mcqs_1.py', 'w', encoding='utf-8') as f:
    f.write("# TPA MCQs Part 1 (Chapters 1 to 3: 90 MCQs)\n")
    f.write("MCQS_PART1 = " + json.dumps(data, indent=2) + "\n")

print(f"Final data_tpa_mcqs_1.py: Total {len(data)} MCQs")
