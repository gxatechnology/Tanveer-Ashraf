# Complete Contract MCQs Part 3 Builder (Chapters 8 to 11: 88 MCQs)
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

# =========================================================================
# CHAPTER 8: DISCHARGE OF CONTRACT & DOCTRINE OF FRUSTRATION (24 MCQs)
# =========================================================================
# top-cnt-08-01: Performance of Contracts & Reciprocal Promises (Sections 37–55) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-08-001", "ch-cnt-08", "top-cnt-08-01",
    "Under Section 37 of the Indian Contract Act, the parties to a contract must either perform, or offer to perform, their respective promises, unless:",
    ["Such performance is dispensed with or excused under the provisions of this Act, or of any other law", "The promisor finds it financially inconvenient", "The promisor leaves the jurisdiction", "The contract is more than 6 months old"],
    0, "A",
    "Section 37 paragraph 1 imposes the fundamental obligation to perform or offer to perform, unless performance is legally dispensed with or excused.",
    {"A": "Correct. Section 37 statutory rule: performance must be made unless legally excused.", "B": "Financial difficulty does not excuse performance under Section 37.", "C": "Absence from jurisdiction does not extinguish obligations.", "D": "No 6-month obsolescence rule exists."},
    "Easy", "Indian Contract Act, 1872, Section 37", "Recall core obligation of performance under Section 37."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-002", "ch-cnt-08", "top-cnt-08-01",
    "Under Section 37 paragraph 2, promises bind the representatives of the promisors in case of the death of such promisors before performance, unless:",
    ["The debt exceeds Rs 1 lakh", "A contrary intention appears from the contract (e.g. contracts involving personal skill or qualification)", "The representatives refuse to inherit the property", "The promisee fails to register a death notice within 30 days"],
    1, "B",
    "Section 37 paragraph 2 binds legal representatives up to the value of estate inherited, unless the contract involves personal skill, artistry, or contrary intention.",
    {"A": "Monetary value does not displace the general rule.", "B": "Correct. Contracts involving personal skill (painting, singing) terminate on death.", "C": "Representatives are bound to the extent of inherited assets regardless of personal refusal.", "D": "No 30-day statutory notice is required."},
    "Medium", "Indian Contract Act, 1872, Section 37 Paragraph 2", "Apply rule of devolution of contractual liability on death."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-003", "ch-cnt-08", "top-cnt-08-01",
    "Under Section 38 of the Indian Contract Act, where a promisor has made an offer of performance (tender) to the promisee, and the offer has not been accepted:",
    ["The promisor is not responsible for non-performance, nor does he thereby lose his rights under the contract", "The promisor is liable to be sued for breach", "The contract is automatically renewed for 1 year", "The promisor must pay damages to the promisee"],
    0, "A",
    "Section 38: A valid tender of performance discharges the promisor from responsibility for non-performance and preserves all his contractual rights.",
    {"A": "Correct. Section 38 provides that a valid unaccepted tender discharges liability for non-performance.", "B": "Promisor who tenders performance is not in breach.", "C": "No automatic renewal occurs.", "D": "Promisor does not owe damages; rather promisee is in default."},
    "Easy", "Indian Contract Act, 1872, Section 38", "Identify effect of refusal to accept tender of performance."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-004", "ch-cnt-08", "top-cnt-08-01",
    "Under Section 38 paragraph 2, which of the following is an essential condition of a valid offer of performance (tender)?",
    ["It must be unconditional", "It must be made at a proper time and place, and under such circumstances that the promisee has a reasonable opportunity of ascertaining that the promisor can perform", "If it is an offer to deliver anything, the promisee must have a reasonable opportunity of seeing that the thing offered is what was promised", "All of the above"],
    3, "D",
    "Section 38 clauses (1), (2), and (3) prescribe that tender must be unconditional, at proper time/place, with opportunity to inspect and verify ability to perform.",
    {"A": "Tender must be unconditional (Section 38(1)).", "B": "Proper time and place with opportunity to ascertain (Section 38(2)).", "C": "Opportunity to inspect goods (Section 38(3)).", "D": "Correct. All three conditions are mandatory for a valid tender."},
    "Medium", "Indian Contract Act, 1872, Section 38", "Master essentials of valid tender under Section 38."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-005", "ch-cnt-08", "top-cnt-08-01",
    "Under Section 40 of the Indian Contract Act, if it appears from the nature of the case that it was the intention of the parties that any promise should be performed by the promisor himself:",
    ["Such promise must be performed by the promisor himself; in other cases, the promisor or his representatives may employ a competent person to perform it", "The contract is void for uncertainty", "The promisee can demand execution by a third party", "The promisor can assign the duty to an independent contractor without consent"],
    0, "A",
    "Section 40 distinguishes personal contracts (which must be performed personally by promisor) from non-personal contracts (which may be performed by agents/representatives).",
    {"A": "Correct. Section 40 textually mandates personal performance where intended.", "B": "Personal contracts are completely valid.", "C": "Promisee cannot compel third-party performance where personal skill is contracted.", "D": "Personal duties cannot be unilaterally assigned."},
    "Easy", "Indian Contract Act, 1872, Section 40", "Distinguish personal performance contracts under Section 40."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-006", "ch-cnt-08", "top-cnt-08-01",
    "Under Section 43 of the Indian Contract Act, when two or more persons make a joint promise, the promisee may, in the absence of express agreement to the contrary:",
    ["Compel all joint promisors together, but never any one individually", "Compel any one or more of such joint promisors to perform the whole of the promise", "Sue only the eldest promisor", "Only recover a proportionate fraction from each"],
    1, "B",
    "Section 43 makes joint liability joint and several at the option of the promisee: promisee may compel any one or more joint promisors to perform the entire promise.",
    {"A": "Promisee is not bound to sue all joint promisors together in India.", "B": "Correct. Section 43 allows the promisee to compel any one joint promisor to perform the whole.", "C": "Age of promisors is legally irrelevant.", "D": "Proportionate division is an internal matter of contribution between promisors, not binding promisee."},
    "Medium", "Indian Contract Act, 1872, Section 43", "Master joint and several liability under Section 43."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-007", "ch-cnt-08", "top-cnt-08-01",
    "Under Section 43 paragraph 2, each of two or more joint promisors may compel every other joint promisor to contribute:",
    ["Equally with himself to the performance of the promise, unless a contrary intention appears from the contract", "According to their physical weight", "Only if decreed by an arbitrator", "Nothing, as the paying promisor has no remedy"],
    0, "A",
    "Section 43 paragraph 2 gives the performing joint promisor the right of equal contribution against all other joint promisors (and sharing of losses under paragraph 3).",
    {"A": "Correct. Section 43(2) mandates equal contribution between joint promisors.", "B": "Physical attributes have no legal relevance.", "C": "Right of contribution arises by operation of statute, needing no prior arbitration.", "D": "Right to contribution is an established statutory right."},
    "Easy", "Indian Contract Act, 1872, Section 43 Paragraph 2", "Identify right of contribution among joint promisors."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-008", "ch-cnt-08", "top-cnt-08-01",
    "Under Section 55 of the Indian Contract Act, when a party to a contract promises to do a certain thing at or before a specified time, and fails to do so at or before the specified time:",
    ["The contract becomes voidable at the option of the promisee, if the intention of the parties was that time should be of the essence of the contract", "The contract is always void ab initio", "The promisor is criminally liable for fraud", "The contract automatically extends for 30 days"],
    0, "A",
    "Section 55 paragraph 1: If time is of the essence, failure to perform within time makes the contract voidable at the option of the promisee.",
    {"A": "Correct. Section 55(1) makes contract voidable if time is of the essence.", "B": "It is voidable, not void ab initio.", "C": "Delay in performance is not a criminal offense.", "D": "No automatic statutory extension exists."},
    "Medium", "Indian Contract Act, 1872, Section 55", "Master time as essence of contract under Section 55."
))

# top-cnt-08-02: Doctrine of Frustration & Supervening Impossibility (Section 56) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-08-009", "ch-cnt-08", "top-cnt-08-02",
    "Under Section 56 paragraph 1 of the Indian Contract Act, an agreement to do an act impossible in itself is:",
    ["Voidable", "Void", "Valid until discovered", "Enforceable with 50% discount"],
    1, "B",
    "Section 56 paragraph 1 codifies initial impossibility (impossibilium nulla obligatio est): an agreement to do an act impossible in itself is void ab initio.",
    {"A": "Initial impossibility makes agreement void, not voidable.", "B": "Correct. Section 56(1) explicitly states agreement to do impossible act is void.", "C": "It is void from inception, not merely upon discovery.", "D": "No discount can enforce an impossible agreement."},
    "Easy", "Indian Contract Act, 1872, Section 56 Paragraph 1", "Recall rule on initial impossibility under Section 56(1)."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-010", "ch-cnt-08", "top-cnt-08-02",
    "Under Section 56 paragraph 2 of the Indian Contract Act, a contract to do an act which, after the contract is made, becomes impossible, or, by reason of some event which the promisor could not prevent, unlawful, becomes:",
    ["Void when the act becomes impossible or unlawful", "Voidable at the option of the promisee", "Valid and promisor must pay damages", "Suspended for 7 years"],
    0, "A",
    "Section 56 paragraph 2 codifies supervening impossibility (doctrine of frustration): the contract becomes void when the act becomes impossible or unlawful.",
    {"A": "Correct. Section 56(2) provides that contract becomes void upon supervening impossibility.", "B": "Frustration terminates contract automatically by operation of law, not at option of party.", "C": "Promisor is discharged from performance and damages.", "D": "No 7-year suspension rule exists."},
    "Easy", "Indian Contract Act, 1872, Section 56 Paragraph 2", "Identify effect of supervening impossibility under Section 56(2)."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-011", "ch-cnt-08", "top-cnt-08-02",
    "In the foundational English decision Taylor v. Caldwell (1863), a music hall was accidentally destroyed by fire before the scheduled concert without fault of either party. Blackburn J. held:",
    ["The music hall owner was liable in damages for failing to provide the hall", "Both parties were discharged because an implied condition existed that the hall would continue to exist", "The singer was entitled to full fee on quantum meruit", "The insurance company was substituted as promisor"],
    1, "B",
    "Taylor v. Caldwell established the common law doctrine of frustration: where performance depends on the continued existence of a person or thing, destruction excuses performance.",
    {"A": "Owner was not liable in damages as fire was without fault.", "B": "Correct. Leading case establishing discharge by destruction of subject matter.", "C": "No performance took place, so quantum meruit did not arise.", "D": "Insurance companies are not substituted in contract suits."},
    "Medium", "Taylor v. Caldwell (1863) 3 B & S 826", "Master Taylor v Caldwell on destruction of subject matter."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-012", "ch-cnt-08", "top-cnt-08-02",
    "In Krell v. Henry (1903) (Coronation Case), rooms were hired on Pall Mall to view the coronation procession of King Edward VII, which was postponed due to the King's illness. The court held:",
    ["The hirer was liable to pay the balance rent because the room still physically existed", "The contract was frustrated because the procession was the foundational purpose and foundation of the contract", "The owner was entitled to 50% cancellation fee", "The contract was void ab initio under Section 20"],
    1, "B",
    "The Court of Appeal held that frustration applies where the fundamental purpose/foundation of the contract has ceased to exist, even if physical subject matter remains.",
    {"A": "Hirer was excused from paying balance rent.", "B": "Correct. Frustration of non-occurrence of foundational event (frustration of purpose).", "C": "No cancellation fee was awarded.", "D": "Contract was valid when made and frustrated subsequently."},
    "Medium", "Krell v. Henry (1903) 2 KB 740", "Apply coronation cases doctrine on frustration of purpose."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-013", "ch-cnt-08", "top-cnt-08-02",
    "In the landmark Supreme Court decision Satyabrata Ghose v. Mugneeram Bangur & Co. (AIR 1954 SC 44), Mukherjea J. established that under Indian law:",
    ["Section 56 is an exhaustive code on frustration; courts need not resort to English theories of implied term, and frustration applies when performance becomes practically impossible or foundation disappears", "Frustration does not apply to land development contracts under any circumstances", "Frustration is governed exclusively by English common law", "Parties can never invoke frustration without government gazette notification"],
    0, "A",
    "Mukherjea J. ruled that Section 56 is exhaustive on frustration in India, embodying practical and commercial impossibility, dispensing with English common law fictions.",
    {"A": "Correct. Landmark ruling establishing exhaustive nature of Section 56 and practical impossibility test.", "B": "Frustration can apply to land contracts, though temporary requisition in this case did not frustrate it.", "C": "Section 56 displaces English implied term theories.", "D": "No gazette notification is required to invoke Section 56."},
    "Hard", "Supreme Court: Satyabrata Ghose v. Mugneeram Bangur (AIR 1954 SC 44)", "Master Satyabrata Ghose doctrine on Section 56."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-014", "ch-cnt-08", "top-cnt-08-02",
    "Does commercial hardship, economic unprofitability, or abnormal rise in freight/prices amount to frustration under Section 56 of the Indian Contract Act?",
    ["Yes, any 20% loss automatically frustrates a contract", "No, commercial difficulty, strikes, or onerousness of performance does not frustrate a contract (Energy Watchdog v. CERC, 2017)", "Only if the contract is with a foreign supplier", "Yes, under the doctrine of rebus sic stantibus"],
    1, "B",
    "In Energy Watchdog v. CERC (2017) and Tsakiroglou v. Noblee Thorl (1962), courts held that mere commercial hardship or increased cost of performance does not amount to frustration.",
    {"A": "Economic loss or price rise does not frustrate a contract.", "B": "Correct. Energy Watchdog established that commercial hardship or price escalation is not frustration.", "C": "Applies uniformly to domestic and international commercial contracts.", "D": "Rebus sic stantibus is an international treaty doctrine, not Indian contract law."},
    "Hard", "Supreme Court: Energy Watchdog v. CERC (2017) 14 SCC 80", "Differentiate commercial hardship from statutory frustration."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-015", "ch-cnt-08", "top-cnt-08-02",
    "Self-induced frustration (where the impossibility is caused by the deliberate act or default of one of the contracting parties):",
    ["Operates as a valid discharge under Section 56", "Does NOT operate as frustration, but amounts to a breach of contract by the defaulting party", "Makes the contract void ab initio", "Entitles the defaulting party to claim quantum meruit"],
    1, "B",
    "Under Maritime National Fish Ltd. v. Ocean Trawlers (1935), frustration must occur without fault of either party; self-induced impossibility constitutes breach.",
    {"A": "Frustration cannot be relied upon by a party whose own act caused it.", "B": "Correct. Self-induced frustration is in law a breach of contract.", "C": "It is not void ab initio.", "D": "A breaching party cannot claim quantum meruit for self-created default."},
    "Medium", "Privy Council: Maritime National Fish v. Ocean Trawlers (1935) AC 524", "Identify legal effect of self-induced frustration."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-016", "ch-cnt-08", "top-cnt-08-02",
    "Under Section 65 of the Indian Contract Act, when a contract becomes void by reason of supervening impossibility under Section 56:",
    ["Any person who has received any advantage under such agreement or contract is bound to restore it, or to make compensation for it, to the person from whom he received it", "Advance payments can be forfeited by the receiver as liquidated damages", "The loss lies where it falls as under English common law before 1943", "The promisor must pay double the consideration"],
    0, "A",
    "Unlike the harsh old English common law rule in Fibrosa, Section 65 has always applied in India to restore benefits received under contracts that become void by frustration.",
    {"A": "Correct. Section 65 mandates restitution of advantages received under frustrated contracts.", "B": "Advance payments cannot be retained without lawful counter-performance.", "C": "The English rule of Chandler v. Webster never applied in India due to Section 65.", "D": "No double damages penalty applies under Section 65."},
    "Hard", "Indian Contract Act, 1872, Section 65", "Apply Section 65 restitution upon contract frustration."
))

# top-cnt-08-03: Discharge by Novation, Rescission & Alteration (Sections 62–67) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-08-017", "ch-cnt-08", "top-cnt-08-03",
    "Under Section 62 of the Indian Contract Act, if the parties to a contract agree to substitute a new contract for it, or to rescind or alter it:",
    ["The original contract must still be performed in part", "The original contract need not be performed", "The new contract is voidable at option of promisor", "Leave of the civil court is mandatory"],
    1, "B",
    "Section 62 states: 'If the parties to a contract agree to substitute a new contract for it, or to rescind or alter it, the original contract need not be performed'.",
    {"A": "Original contract is completely extinguished.", "B": "Correct. Section 62 explicitly provides that original contract need not be performed.", "C": "The new substituted contract is fully valid and binding.", "D": "Civil court leave is not required for novation."},
    "Easy", "Indian Contract Act, 1872, Section 62", "Recall statutory rule of novation under Section 62."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-018", "ch-cnt-08", "top-cnt-08-03",
    "What is the essential prerequisite for a valid 'novation' under Section 62 of the Indian Contract Act?",
    ["Mutual consent of all contracting parties (including the new party, if parties are changed)", "Registration with the Registrar of Companies", "Payment of full consideration in advance", "Execution before a judicial magistrate"],
    0, "A",
    "Novation requires tripartite mutual consent if a new party is substituted, or bilateral mutual consent if terms are altered. A party cannot unilaterally novate a contract.",
    {"A": "Correct. Mutual consent of all concerned parties is indispensable for novation.", "B": "Company registration is not a general contract prerequisite.", "C": "Advance payment is not essential.", "D": "Magisterial execution is not required."},
    "Medium", "Lata Construction v. Rameshchandra Ramniklal Shah (AIR 2000 SC 380)", "Identify essential prerequisite of novation under Section 62."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-019", "ch-cnt-08", "top-cnt-08-03",
    "What is the fundamental difference between 'novation' and 'alteration' under Section 62?",
    ["In novation, parties may change or the core obligation is substituted; in alteration, terms are modified between the same parties without changing the parties", "Novation is oral, alteration must be in writing", "Novation requires court order, alteration does not", "Alteration always makes the contract void"],
    0, "A",
    "Novation may involve change of parties or complete substitution of new contract. Alteration involves change in terms between the original parties without substituting new parties.",
    {"A": "Correct. Novation can change parties; alteration modifies terms between identical parties.", "B": "Both can be oral or written depending on subject matter.", "C": "Neither requires a court order.", "D": "Consensual alteration is completely valid."},
    "Medium", "Indian Contract Jurisprudence, Section 62", "Distinguish novation from alteration."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-020", "ch-cnt-08", "top-cnt-08-03",
    "In Pigot's Case (1614), what is the legal effect of a material alteration made in a written contract by a party without the consent of the other party?",
    ["The contract is valid in its original form", "The altered contract becomes void and unenforceable by the party who made the alteration", "The altering party is entitled to 50% damages", "The alteration is automatically validated after 30 days"],
    1, "B",
    "Under the rule in Pigot's Case and Indian law, an unauthorized material alteration of a written deed/contract by a party destroys the document, making it void against that party.",
    {"A": "Unauthorized alteration prevents enforcement even in original terms.", "B": "Correct. Unilateral material alteration renders the contract void.", "C": "A wrongdoer cannot claim damages.", "D": "Time does not validate unauthorized alterations."},
    "Hard", "Pigot's Case (1614) 11 Co Rep 26b; Nathu Lal v. Gomti Kuar (AIR 1940 PC 160)", "Apply rule on unauthorized material alteration."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-021", "ch-cnt-08", "top-cnt-08-03",
    "Under Section 63 of the Indian Contract Act, every promisee may:",
    ["Dispense with or remit, wholly or in part, the performance of the promise made to him, or extend the time for performance, or accept any satisfaction instead of it", "Compel the promisor to pay triple interest", "Transfer the obligation to an unwilling third party", "Unilaterally imprison the promisor"],
    0, "A",
    "Section 63 codifies remission, dispensation, extension of time, and accord and satisfaction. It dispenses with consideration for remission, departing from English Pinnel's Case.",
    {"A": "Correct. Section 63 grants promisee power to dispense with, remit, extend time, or accept satisfaction.", "B": "Promisee cannot impose punitive triple interest unilaterally.", "C": "Obligations cannot be assigned to unwilling third parties.", "D": "Private imprisonment is illegal."},
    "Easy", "Indian Contract Act, 1872, Section 63", "Recall promisee's powers of remission under Section 63."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-022", "ch-cnt-08", "top-cnt-08-03",
    "Under English common law (Pinnel's Case, 1602, and Foakes v. Beer, 1884), payment of a lesser sum in satisfaction of a larger debt is no discharge for lack of consideration. Under Indian law (Section 63):",
    ["The English rule applies and payment of a lesser sum is void for want of consideration", "Payment of a lesser sum accepted by the promisee in full discharge validly discharges the whole debt without fresh consideration", "Part-payment is illegal under Section 23", "Part-payment requires approval of the High Court"],
    1, "B",
    "Section 63 Illustration (b) expressly provides that a creditor may accept a smaller sum in full satisfaction, completely discharging the debt without new consideration.",
    {"A": "The rule in Pinnel's Case and Foakes v. Beer does NOT apply in India.", "B": "Correct. Section 63 explicitly departs from English law: lesser sum accepted discharges the debt.", "C": "Part-payment is fully legal.", "D": "Judicial approval is not required."},
    "Hard", "Indian Contract Act, 1872, Section 63 Illustration (b)", "Contrast Section 63 remission with Pinnel's Case and Foakes v Beer."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-023", "ch-cnt-08", "top-cnt-08-03",
    "Under Section 64 of the Indian Contract Act, when a person at whose option a contract is voidable rescinds it, the party rescinding must:",
    ["Pay a fine of Rs 500 to the court", "If he has received any benefit thereunder from another party to such contract, restore such benefit, so far as may be, to the person from whom it was received", "Perform half the contract", "Forfeit all his ancestral property"],
    1, "B",
    "Section 64: The party rescinding a voidable contract must restore any benefit received thereunder to the person from whom it was received (restitutio in integrum).",
    {"A": "No court fine is imposed for exercising a lawful right of rescission.", "B": "Correct. Section 64 requires restoration of benefits received under rescinded voidable contracts.", "C": "Rescission extinguishes performance duties; cannot compel half performance.", "D": "Ancestral property is not forfeited."},
    "Easy", "Indian Contract Act, 1872, Section 64", "Identify duty of restoring benefit under Section 64."
))
mcqs.append(make_mcq(
    "mcq-cnt-08-024", "ch-cnt-08", "top-cnt-08-03",
    "Under Section 67 of the Indian Contract Act, if any promisee neglects or refuses to afford the promisor reasonable facilities for the performance of his promise:",
    ["The promisor is excused by such neglect or refusal as to any non-performance caused thereby", "The promisor must perform despite lack of facilities", "The contract is void ab initio", "The promisee can sue for breach"],
    0, "A",
    "Section 67: If the promisee fails to afford reasonable facilities for performance (e.g. refusing to let a builder enter the house to repair), the promisor is excused from non-performance.",
    {"A": "Correct. Section 67 excuses promisor where promisee fails to afford reasonable facilities.", "B": "Promisor is not bound to perform when obstructed by promisee.", "C": "Contract was validly formed, not void ab initio.", "D": "Promisee cannot sue for breach caused by his own obstruction."},
    "Medium", "Indian Contract Act, 1872, Section 67", "Recall effect of promisee's refusal of facilities under Section 67."
))

# =========================================================================
# CHAPTER 9: BREACH OF CONTRACT & REMEDIES (DAMAGES) (24 MCQs)
# =========================================================================
# top-cnt-09-01: Anticipatory Breach vs Actual Breach of Contract (Section 39) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-09-001", "ch-cnt-09", "top-cnt-09-01",
    "Under Section 39 of the Indian Contract Act, when a party to a contract has refused to perform, or disabled himself from performing, his promise in its entirety:",
    ["The promisee may put an end to the contract, unless he has signified, by words or conduct, his acquiescence in its continuance", "The contract is automatically renewed", "The promisee must perform his part first before complaining", "The promisor is granted an automatic 6-month extension"],
    0, "A",
    "Section 39 codifies anticipatory breach and repudiation: promisee may terminate the contract unless he has signified acquiescence in its continuance.",
    {"A": "Correct. Section 39 textually empowers the promisee to put an end to the contract upon refusal.", "B": "No automatic renewal occurs.", "C": "Promisee is relieved from performing upon promisor's total repudiation.", "D": "No statutory extension applies."},
    "Easy", "Indian Contract Act, 1872, Section 39", "Recall statutory rule of anticipatory breach under Section 39."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-002", "ch-cnt-09", "top-cnt-09-01",
    "In the landmark English decision Hochster v. De La Tour (1853), the defendant engaged the plaintiff as a courier for a European tour starting on June 1. On May 11, the defendant wrote refusing to employ him. The plaintiff sued on May 22. The court held:",
    ["The suit was premature and plaintiff must wait until June 1 before suing", "The plaintiff was entitled to treat the renunciation as an immediate breach and sue for damages at once without waiting for the due date", "The contract was void for uncertainty", "The courier was bound to seek specific performance"],
    1, "B",
    "Hochster v. De La Tour established the doctrine of anticipatory breach: an explicit repudiation before the due date entitles the promisee to sue immediately for damages.",
    {"A": "Waiting until due date is not mandatory upon unequivocal repudiation.", "B": "Correct. Leading case establishing right to sue immediately on anticipatory breach.", "C": "Contract was certain and binding.", "D": "Specific performance is not required for personal service contracts."},
    "Medium", "Hochster v. De La Tour (1853) 2 E & B 678", "Master Hochster v De La Tour on anticipatory breach."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-003", "ch-cnt-09", "top-cnt-09-01",
    "In Frost v. Knight (1872), the defendant promised to marry the plaintiff upon the death of his father. While the father was still alive, the defendant broke off the engagement. The court held:",
    ["Plaintiff could not sue because the contingency (father's death) had not happened", "Plaintiff was entitled to sue immediately for anticipatory breach of promise", "The agreement was void under Section 26 as restraint of marriage", "The suit was barred by limitation"],
    1, "B",
    "Cockburn C.J. held that repudiating a conditional or future promise enables the promisee to treat the contract as broken immediately and recover damages.",
    {"A": "Repudiation dispenses with waiting for the condition.", "B": "Correct. Leading case confirming anticipatory breach of contingent/future promise.", "C": "Agreement to marry is not a restraint of marriage.", "D": "Limitation runs from the repudiation/termination."},
    "Medium", "Frost v. Knight (1872) LR 7 Ex 111", "Apply anticipatory breach doctrine in Frost v Knight."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-004", "ch-cnt-09", "top-cnt-09-01",
    "When an anticipatory breach occurs, what two options are available to the promisee?",
    ["(1) Treat the contract as rescinded and sue immediately for damages, or (2) keep the contract alive until the due date of performance", "Only to sue after waiting 3 years", "Only to report to the police", "None, promisee must accept the cancellation without remedy"],
    0, "A",
    "The promisee has an election: (1) accept the repudiation, terminate the contract, and sue immediately; or (2) refuse repudiation, keep contract alive for benefit of both parties until due date.",
    {"A": "Correct. The two well-settled legal options available to the aggrieved promisee.", "B": "No mandatory 3-year waiting rule exists.", "C": "Contract breach is a civil matter, not police report.", "D": "Aggrieved party has full statutory remedies."},
    "Medium", "Indian Contract Act, 1872, Section 39", "Identify dual options available upon anticipatory breach."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-005", "ch-cnt-09", "top-cnt-09-01",
    "In Avery v. Bowden (1855), the charterer told the ship captain at Odessa before loading days expired that he had no cargo and advised him to leave. The captain refused to accept repudiation and remained. Before loading days expired, the Crimean War broke out, making performance illegal. The court held:",
    ["The charterer was liable for anticipatory breach", "The captain, by keeping the contract alive, took the risk of intervening events; the contract was discharged by frustration without liability on either side", "The ship was confiscated by the Admiralty", "The charterer had to pay full demurrage"],
    1, "B",
    "Avery v. Bowden established that if the promisee keeps the contract alive, it remains alive for the benefit of both parties; a supervening frustrating event discharges both parties without liability.",
    {"A": "The captain lost his right to sue for prior repudiation by refusing it.", "B": "Correct. Keeping the contract alive exposes promisee to subsequent frustration discharging promisor.", "C": "Ship was not confiscated.", "D": "No demurrage was payable on frustrated contract."},
    "Hard", "Avery v. Bowden (1855) 5 E & B 714", "Master Avery v Bowden on consequences of keeping contract alive."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-006", "ch-cnt-09", "top-cnt-09-01",
    "In White & Carter (Councils) Ltd. v. McGregor (1962), the advertiser repudiated an advertising contract the same day it was signed. The advertising company refused the repudiation, displayed the ads for 3 years, and sued for the full contract price. The House of Lords held:",
    ["The advertising company had a duty to mitigate and could only claim nominal damages", "The innocent party had an unfettered right to complete performance and recover the contract debt, provided it did not require the repudiating party's cooperation and had a legitimate interest", "The contract was void ab initio", "The repudiator was liable to imprisonment"],
    1, "B",
    "The House of Lords held by majority that an innocent party is not bound to accept repudiation and can perform unilaterally to claim the contract price, subject to legitimate interest.",
    {"A": "Mitigation duty applies to damage claims, not actions for contract debt.", "B": "Correct. Landmark ruling on right to affirm contract and complete performance.", "C": "Contract was valid and binding.", "D": "No criminal penalties in civil repudiation."},
    "Hard", "House of Lords: White & Carter v. McGregor (1962) AC 413", "Analyze White & Carter doctrine on affirmation after repudiation."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-007", "ch-cnt-09", "top-cnt-09-01",
    "Under Section 39, Illustration (a): A, a singer, contracts with B, a theatre manager, to sing at his theatre two nights every week for the next two months, B engaging to pay Rs 100 for each night. On the sixth night, A willfully absents herself. What is B's right?",
    ["B must continue the contract and pay A for remaining nights", "B is at liberty to put an end to the contract", "B must file a writ petition in the High Court", "B is liable to A in damages"],
    1, "B",
    "Illustration (a) to Section 39: B is at liberty to put an end to the contract because A refused to perform her promise in its entirety.",
    {"A": "B is not bound to continue with a defaulting performer.", "B": "Correct. Exactly matches Illustration (a) to Section 39: B is at liberty to put an end to contract.", "C": "Writ petitions do not lie against private contracts.", "D": "A is the breaching party, not B."},
    "Easy", "Indian Contract Act, 1872, Section 39 Illustration (a)", "Apply Section 39 Illustration (a) on singer's absence."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-008", "ch-cnt-09", "top-cnt-09-01",
    "Under Section 39, Illustration (b): A, the singer, willfully absents herself on the sixth night, but with B's assent sings on the seventh night. What is the legal effect?",
    ["B has signified his acquiescence in the continuance of the contract, and cannot put an end to it, but is entitled to compensation for damages sustained on the sixth night", "The contract is completely novated and B loses all claims for past breach", "The contract becomes void ab initio", "A is entitled to double payment for the seventh night"],
    0, "A",
    "Illustration (b) to Section 39: By permitting her to sing on the 7th night, B acquiesced in the contract's continuance; he cannot terminate it, but retains right to damages for the 6th night.",
    {"A": "Correct. Matches Illustration (b) to Section 39 verbatim: acquiescence bars termination but preserves damages.", "B": "Acquiescence does not waive damages for past breach.", "C": "It does not become void.", "D": "Regular agreed contractual rate applies."},
    "Medium", "Indian Contract Act, 1872, Section 39 Illustration (b)", "Apply Section 39 Illustration (b) on acquiescence and damages."
))

# top-cnt-09-02: Damages for Breach: Rule in Hadley v Baxendale (Section 73) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-09-009", "ch-cnt-09", "top-cnt-09-02",
    "Under Section 73 paragraph 1 of the Indian Contract Act, when a contract has been broken, the party who suffers by such breach is entitled to receive compensation for any loss or damage caused to him thereby, which:",
    ["Naturally arose in the usual course of things from such breach, or which the parties knew, when they made the contract, to be likely to result from the breach", "Is the most remote and indirect consequence imaginable", "Exceeds 10 times the contract value", "Is assessed by a religious body"],
    0, "A",
    "Section 73 paragraph 1 codifies the two limbs of Hadley v. Baxendale: (1) general damages naturally arising in the usual course, and (2) special damages within contemplation of parties.",
    {"A": "Correct. Section 73 textually incorporates the two limbs of Hadley v. Baxendale.", "B": "Section 73 paragraph 3 expressly bars compensation for remote and indirect loss.", "C": "Damages are compensatory, not arbitrary tenfold multipliers.", "D": "Damages are determined by courts of law."},
    "Easy", "Indian Contract Act, 1872, Section 73", "Recall statutory rule of damages under Section 73."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-010", "ch-cnt-09", "top-cnt-09-02",
    "Under Section 73 paragraph 3 of the Indian Contract Act, compensation is NOT to be given for any:",
    ["Direct loss", "Remote and indirect loss or damage sustained by reason of the breach", "Loss of ordinary market profits", "Expenses incurred in performance"],
    1, "B",
    "Section 73 paragraph 3 explicitly states: 'Such compensation is not to be given for any remote and indirect loss or damage sustained by reason of the breach'.",
    {"A": "Direct loss is recoverable under limb 1.", "B": "Correct. Remote and indirect loss is expressly excluded by Section 73 paragraph 3.", "C": "Loss of usual profit is recoverable under limb 1.", "D": "Wasted expenses are recoverable as reliance loss."},
    "Easy", "Indian Contract Act, 1872, Section 73 Paragraph 3", "Identify exclusion of remote damages under Section 73."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-011", "ch-cnt-09", "top-cnt-09-02",
    "In the landmark English decision Hadley v. Baxendale (1854), a broken crankshaft of a flour mill was sent via carrier for replacement. Due to carrier delay, the mill remained idle. The court held:",
    ["The carrier was liable for lost profits of the mill", "The carrier was not liable for lost mill profits because millers usually keep spare shafts, and special circumstances were not communicated to the carrier", "The carrier had to replace the mill at its own cost", "The contract was void for frustration"],
    1, "B",
    "Alderson B. laid down the two branches of damages: lost profits were not natural consequences, nor was the special circumstance of having no spare shaft communicated to the carrier.",
    {"A": "Carrier was held not liable for remote lost profits.", "B": "Correct. Foundational case establishing general vs special damages and notice requirement.", "C": "Carrier only paid ordinary delay damages, not new mill.", "D": "No frustration occurred; it was a simple breach."},
    "Medium", "Hadley v. Baxendale (1854) 9 Ex 341", "Master Hadley v Baxendale two limbs of damages."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-012", "ch-cnt-09", "top-cnt-09-02",
    "In Victoria Laundry (Windsor) Ltd. v. Newman Industries Ltd. (1949), a boiler was delivered 20 weeks late. The laundry sued for normal business loss and loss of a highly lucrative special dyeing contract. The court held:",
    ["The laundry could recover normal business loss, but could not recover the exceptional profits from the special government contract because defendants had no notice of it", "The laundry could recover both normal and special lucrative profits", "The laundry could recover nothing because delivery took place", "The manufacturers were sentenced to pay punitive damages"],
    0, "A",
    "Asquith L.J. held that defendants were liable for ordinary loss of profits that a reasonable person would foresee, but not for extraordinary profits on lucrative contracts without special notice.",
    {"A": "Correct. Recovered ordinary business loss under limb 1, but denied extraordinary special profits under limb 2.", "B": "Special contract profits were too remote without specific notice.", "C": "Late delivery is an actionable breach entitling to damages.", "D": "Punitive damages are not awarded in contract breaches."},
    "Hard", "Victoria Laundry v. Newman Industries (1949) 2 KB 528", "Apply Victoria Laundry distinction on ordinary vs lucrative profits."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-013", "ch-cnt-09", "top-cnt-09-02",
    "In The Heron II (Koufos v. C. Czarnikow Ltd., 1969), the House of Lords clarified the test of remoteness in contract law, holding that the loss must be:",
    ["A slight possibility", "Not unlikely, or having a real danger or serious possibility of occurring", "Absolutely certain to happen in 100% of cases", "Identical to the test of foreseeability in tort of negligence"],
    1, "B",
    "The House of Lords established that the contract test is stricter than tort: the loss must be within reasonable contemplation as 'not unlikely' or a 'serious possibility'.",
    {"A": "Slight possibility satisfies tort negligence (Wagon Mound No 2), but not contract.", "B": "Correct. House of Lords test: 'not unlikely' or 'serious possibility' within contemplation.", "C": "Absolute certainty is not required in civil law.", "D": "The contract test is distinct and narrower than tort foreseeability."},
    "Hard", "House of Lords: The Heron II (1969) 1 AC 350", "Differentiate contract remoteness from tort foreseeability."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-014", "ch-cnt-09", "top-cnt-09-02",
    "Under the Explanation to Section 73 of the Indian Contract Act, in estimating the loss or damage arising from a breach of contract, the means which existed of remedying the inconvenience must be taken into account. This codifies:",
    ["The doctrine of promissory estoppel", "The legal duty to mitigate damages", "The doctrine of exemplary damages", "The rule against double jeopardy"],
    1, "B",
    "Explanation to Section 73: 'In estimating the loss or damage... the means which existed of remedying the inconvenience caused by the non-performance of the contract must be taken into account'.",
    {"A": "Promissory estoppel is not an assessment rule for damages.", "B": "Correct. Explanation to Section 73 statutorily codifies the duty to mitigate damages.", "C": "Exemplary damages are generally not recognized in contract law.", "D": "Double jeopardy is a criminal constitutional protection under Article 20(2)."},
    "Medium", "Indian Contract Act, 1872, Section 73 Explanation", "Master statutory duty to mitigate damages under Section 73."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-015", "ch-cnt-09", "top-cnt-09-02",
    "What is the ordinary measure of damages for breach of a contract for the sale of goods under Section 73?",
    ["The total purchase price of the goods", "The difference between the contract price and the market price on the date of breach", "The profit the buyer hoped to make 5 years later", "A flat 10% penalty on the seller"],
    1, "B",
    "Settled measure under Section 73: Damages = Contract Price minus Market Price at the date and place of breach (Jamal v. Moolla Dawood Sons & Co., 1916).",
    {"A": "Total purchase price is not damages unless goods are undelivered and price prepaid.", "B": "Correct. Contract price versus market price on breach date is the settled measure.", "C": "Long-term speculative profits are too remote.", "D": "Contract law does not impose arbitrary flat percentage penalties."},
    "Easy", "Privy Council: Jamal v. Moolla Dawood Sons & Co. (1916) 43 IA 6", "Identify measure of damages for sale of goods breach."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-016", "ch-cnt-09", "top-cnt-09-02",
    "In Ghaziabad Development Authority v. Union of India (AIR 2000 SC 2003), the Supreme Court held that in ordinary cases of breach of contract:",
    ["Damages for mental anguish, frustration, or vexation are generally not recoverable, except in exceptional contracts having peace of mind as their object (e.g. holiday contracts)", "Damages for mental pain and suffering are awarded in every commercial breach", "Only criminal compensation can be claimed", "No interest can ever be awarded"],
    0, "A",
    "The Supreme Court affirmed that mental agony damages are not granted in commercial contracts, but may be granted where the very object of contract is pleasure/relaxation (Jarvis v. Swans Tours).",
    {"A": "Correct. Mental anguish is excluded in commercial breaches, except contracts for enjoyment/holiday.", "B": "Commercial breaches do not attract damages for wounded feelings.", "C": "Civil damages are the primary remedy.", "D": "Interest is regularly awarded as compensation for detention of money."},
    "Hard", "Supreme Court: Ghaziabad Development Authority v. Union of India (AIR 2000 SC 2003)", "Analyze damages for mental distress in contract."
))

# top-cnt-09-03: Liquidated Damages vs Penalty: Indian Law Position (Section 74) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-09-017", "ch-cnt-09", "top-cnt-09-03",
    "Under Section 74 of the Indian Contract Act, when a contract has been broken, if a sum is named in the contract as the amount to be paid in case of such breach, or if the contract contains any other stipulation by way of penalty:",
    ["The plaintiff is automatically entitled to receive the entire named sum regardless of actual loss", "The party complaining of the breach is entitled to receive reasonable compensation not exceeding the amount so named or the penalty stipulated, whether or not actual damage or loss is proved", "The stipulation is void and plaintiff gets nothing", "The named sum is forfeited to the state government"],
    1, "B",
    "Section 74 provides that the court will award reasonable compensation not exceeding the named amount, whether or not actual damage is proved, eliminating English common law distinction.",
    {"A": "Plaintiff is not automatically entitled to the named sum; it represents the statutory ceiling.", "B": "Correct. Section 74 entitles party to reasonable compensation not exceeding the named ceiling.", "C": "The clause is valid as a ceiling, not void.", "D": "No forfeiture to state government occurs."},
    "Easy", "Indian Contract Act, 1872, Section 74", "Recall statutory rule under Section 74."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-018", "ch-cnt-09", "top-cnt-09-03",
    "In English common law (Dunlop Pneumatic Tyre Co. v. New Garage & Motor Co., 1915), the law draws a sharp distinction between 'liquidated damages' and 'penalty'. In Indian law (Section 74):",
    ["The English distinction is strictly preserved; liquidated damages are awarded in full and penalties are struck down", "The Indian Contract Act has eliminated the elaborate English distinction; whether named sum is liquidated damages or penalty, the court awards only reasonable compensation not exceeding the named sum", "All liquidated damages clauses are declared illegal under Section 23", "Penalties are enforced with criminal imprisonment"],
    1, "B",
    "In Fateh Chand v. Balkishan Dass (1963) and Maula Bux (1969), the Supreme Court established that Section 74 cuts through the English distinction, treating the named sum as an upper limit.",
    {"A": "The English distinction has been statutorily eliminated in India.", "B": "Correct. Section 74 awards reasonable compensation up to the stipulated maximum in all cases.", "C": "Stipulated sums are lawful under Section 74.", "D": "Civil contract penalties do not carry criminal imprisonment."},
    "Hard", "Supreme Court: Fateh Chand v. Balkishan Dass (AIR 1963 SC 1405)", "Contrast Indian Section 74 with English penalty distinction."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-019", "ch-cnt-09", "top-cnt-09-03",
    "In the landmark Constitution Bench decision Fateh Chand v. Balkishan Dass (AIR 1963 SC 1405), the Supreme Court held that the phrase 'whether or not actual damage or loss is proved to have been caused thereby' in Section 74:",
    ["Dispenses with proof of loss completely in every case, entitling plaintiff to the entire named sum", "Dispenses with proof of actual loss only where loss cannot be assessed; but where loss is capable of assessment, party must prove actual loss suffered to get reasonable compensation", "Is unconstitutional under Article 14", "Applies only to government contracts"],
    1, "B",
    "The Constitution Bench held that where actual loss is capable of proof, it must be proved; the phrase applies where compensation cannot be mathematically calculated.",
    {"A": "The Supreme Court expressly rejected automatic entitlement to named sum.", "B": "Correct. Proof of loss is required where assessable; phrase applies where loss is difficult to quantify.", "C": "Section 74 is fully constitutional.", "D": "Applies uniformly to private and public contracts."},
    "Hard", "Supreme Court: Fateh Chand v. Balkishan Dass (AIR 1963 SC 1405)", "Master Fateh Chand ruling on Section 74 proof of loss."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-020", "ch-cnt-09", "top-cnt-09-03",
    "In Maula Bux v. Union of India (AIR 1970 SC 1955), the government forfeited earnest money deposits and security deposits for non-supply of potatoes. The Supreme Court held:",
    ["Forfeiture of security deposit is governed by Section 74; government could not forfeit the whole deposit without proving reasonable compensation for loss suffered", "The government has sovereign immunity to forfeit all deposits unconditionally", "Security deposits are gifts to the treasury", "Section 74 does not apply to security deposits"],
    0, "A",
    "The Supreme Court held that forfeiture of guarantee/security deposit for breach of contract is in the nature of a penalty governed by Section 74; reasonable compensation alone is retainable.",
    {"A": "Correct. Maula Bux established that deposit forfeiture is governed by Section 74 reasonable compensation.", "B": "Government contracts enjoy no sovereign immunity from Section 74.", "C": "Deposits are not gifts.", "D": "Section 74 explicitly applies to stipulations by way of penalty/forfeiture."},
    "Hard", "Supreme Court: Maula Bux v. Union of India (AIR 1970 SC 1955)", "Apply Maula Bux on forfeiture of security deposits."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-021", "ch-cnt-09", "top-cnt-09-03",
    "In ONGC Ltd. v. Saw Pipes Ltd. (AIR 2003 SC 2629), the Supreme Court held that where the parties have made a genuine pre-estimate of loss and loss is difficult or impossible to prove:",
    ["The court cannot award anything without strict proof of each rupee lost", "The court or arbitrator can award the agreed liquidated amount as reasonable compensation without requiring strict evidence of actual loss", "The liquidated damages clause is struck down as a penalty", "The parties must refer the dispute to a chartered accountant"],
    1, "B",
    "The Supreme Court held that where loss cannot easily be calculated and parties made a genuine pre-estimate, the stipulated liquidated damages can be awarded as reasonable compensation.",
    {"A": "Strict mathematical proof is dispensed with where loss is impossible to quantify.", "B": "Correct. Saw Pipes validated award of agreed genuine pre-estimate where loss is hard to assess.", "C": "Genuine pre-estimate is not a penalty.", "D": "Arbitrators/courts have direct jurisdiction to award it."},
    "Hard", "Supreme Court: ONGC v. Saw Pipes Ltd. (AIR 2003 SC 2629)", "Master ONGC v Saw Pipes on genuine pre-estimate."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-022", "ch-cnt-09", "top-cnt-09-03",
    "In Kailash Nath Associates v. Delhi Development Authority (2015) 4 SCC 136), R.F. Nariman J. reconciled Section 74 jurisprudence and affirmed that:",
    ["Compensation can only be awarded for damage or loss actually suffered; if there is no loss suffered at all, nothing can be awarded under Section 74", "A party can always pocket the named sum even if it made a huge profit from breach", "Section 74 does not apply to DDA tenders", "Fateh Chand has been overruled"],
    0, "A",
    "Nariman J. reaffirmed that damage or loss is the sine qua non for compensation under Section 74; where DDA resold the plot at three times the price and suffered zero loss, it could not forfeit earnest money.",
    {"A": "Correct. Kailash Nath reaffirmed: no loss = no compensation under Section 74.", "B": "Unjust windfall retention is prohibited by Section 74.", "C": "DDA contracts are strictly bound by Section 74.", "D": "Fateh Chand was explicitly approved and reaffirmed."},
    "Hard", "Supreme Court: Kailash Nath Associates v. DDA (2015) 4 SCC 136", "Analyze Kailash Nath Associates ruling on loss as sine qua non."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-023", "ch-cnt-09", "top-cnt-09-03",
    "Under the Exception to Section 74, when any person enters into any bail-bond, recognizance, or other instrument of the same nature, or under the provisions of any law, gives any bond for performance of any public duty:",
    ["He is entitled to have the penalty reduced to Rs 100", "He shall be liable, upon breach of the condition of any such instrument, to pay the whole sum mentioned therein", "The bond is void under Section 23", "He is exempted from all civil liability"],
    1, "B",
    "Exception to Section 74: A person giving a bail-bond, recognizance, or public duty bond is liable, upon breach, to pay the whole sum mentioned therein (full forfeiture).",
    {"A": "Courts cannot reduce public duty bonds under the general rule of Section 74.", "B": "Correct. Exception to Section 74 mandates payment of the whole sum mentioned in public duty bonds.", "C": "Public bonds are fully lawful.", "D": "No civil exemption exists."},
    "Medium", "Indian Contract Act, 1872, Section 74 Exception", "Recall Exception to Section 74 regarding public bonds."
))
mcqs.append(make_mcq(
    "mcq-cnt-09-024", "ch-cnt-09", "top-cnt-09-03",
    "What is the legal effect of a stipulation for an increased rate of interest from the date of default in a loan agreement?",
    ["It is always completely valid and cannot be questioned", "It is a stipulation by way of penalty under Section 74, and the court can grant relief by awarding reasonable interest", "It is an illegal agreement making the loan unrecoverable", "It makes the lender liable to criminal prosecution under BNS"],
    1, "B",
    "Explanation to Section 74 and settled case law: A stipulation for increased interest from default (especially with retroactive effect) is a penalty, entitling court to grant relief.",
    {"A": "Courts have statutory jurisdiction to relieve against penal interest.", "B": "Correct. Increased interest from default is a penalty under Section 74 Explanation.", "C": "The loan remains valid; only the penal rate is relieved against.", "D": "Charging penal interest is not a criminal offense under BNS."},
    "Medium", "Indian Contract Act, 1872, Section 74 Explanation", "Apply penalty rule to increased interest on default."
))

# =========================================================================================
# CHAPTER 10: SPECIAL CONTRACTS: INDEMNITY, GUARANTEE, BAILMENT & PLEDGE (24 MCQs)
# =========================================================================================
# top-cnt-10-01: Contracts of Indemnity & Guarantee: Rights & Surety Liability (Sections 124–147) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-10-001", "ch-cnt-10", "top-cnt-10-01",
    "Under Section 124 of the Indian Contract Act, a 'contract of indemnity' is defined as a contract by which one party promises to save the other from loss caused to him by:",
    ["The conduct of the promisor himself, or by the conduct of any other person", "Accidental fires and sea perils only", "Acts of God and sovereign acts", "Any event whatsoever"],
    0, "A",
    "Section 124 defines indemnity strictly: loss caused by conduct of promisor himself or of any other person (human conduct, excluding natural accidents/insurance).",
    {"A": "Correct. Section 124 statutory definition: loss caused by conduct of promisor or other person.", "B": "Accidental fire/sea peril is insurance, which common law includes in indemnity but Section 124 textually narrows.", "C": "Acts of God are not human conduct under Section 124.", "D": "Not any event; restricted to conduct of human agencies."},
    "Easy", "Indian Contract Act, 1872, Section 124", "Recall statutory definition of contract of indemnity."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-002", "ch-cnt-10", "top-cnt-10-01",
    "In Gajanan Moreshwar Parelkar v. Moreshwar Madan Mantri (AIR 1942 Bom 302), Chagla J. established regarding when an indemnity holder can enforce indemnity:",
    ["The indemnity holder can only sue after he has actually paid out of pocket (English common law rule)", "Equitable principles apply: the indemnity holder can compel the indemnifier to pay off liability before actual loss or out-of-pocket payment, once liability becomes absolute", "The indemnity holder must wait until his property is sold in execution", "Indemnity contracts cannot be enforced in High Courts"],
    1, "B",
    "Chagla J. held that Indian courts apply equity: indemnity is not given by leaving the person to be ruined and then paying; indemnifier can be compelled to pay once liability is absolute.",
    {"A": "The old common law 'damnification first' rule was rejected in equity.", "B": "Correct. Landmark ruling establishing indemnity can be enforced before actual out-of-pocket payment.", "C": "Waiting for execution sale defeats the purpose of indemnity.", "D": "High Courts have full equitable jurisdiction."},
    "Hard", "Bombay High Court: Gajanan Moreshwar v. Moreshwar Madan (AIR 1942 Bom 302)", "Master Gajanan Moreshwar doctrine on indemnity enforcement."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-003", "ch-cnt-10", "top-cnt-10-01",
    "Under Section 126 of the Indian Contract Act, a 'contract of guarantee' is a contract to:",
    ["Save another from loss caused by fire", "Perform the promise, or discharge the liability, of a third person in case of his default", "Pledge movable goods for a debt", "Deliver goods on lease"],
    1, "B",
    "Section 126: A contract of guarantee is a contract to perform the promise, or discharge the liability, of a third person in case of his default. It involves 3 parties: creditor, principal debtor, surety.",
    {"A": "This describes fire insurance/indemnity.", "B": "Correct. Section 126 statutory definition of contract of guarantee.", "C": "This describes a pledge under Section 172.", "D": "This describes a bailment/lease under Section 148."},
    "Easy", "Indian Contract Act, 1872, Section 126", "Identify statutory definition and parties to guarantee."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-004", "ch-cnt-10", "top-cnt-10-01",
    "Under Section 128 of the Indian Contract Act, the liability of the surety is:",
    ["Subordinate to the principal debtor, and creditor must exhaust remedies against debtor first", "Co-extensive with that of the principal debtor, unless it is otherwise provided by the contract", "Limited to 50% of the principal debt", "Enforceable only after the principal debtor is declared insolvent"],
    1, "B",
    "Section 128: The liability of the surety is co-extensive with that of the principal debtor. Creditor can sue surety directly without suing principal debtor first (Bank of Bihar v. Damodar Prasad).",
    {"A": "Creditor is not bound to exhaust remedies against principal debtor first.", "B": "Correct. Section 128 explicitly establishes co-extensive liability.", "C": "Surety is liable for the whole debt unless contract restricts it.", "D": "Insolvency of debtor is not a prerequisite to sue surety."},
    "Medium", "Indian Contract Act, 1872, Section 128", "Master co-extensive liability of surety under Section 128."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-005", "ch-cnt-10", "top-cnt-10-01",
    "Under Section 130 of the Indian Contract Act, a continuing guarantee may at any time be revoked by the surety, as to future transactions, by:",
    ["Notice to the creditor", "Filing an application before a civil judge", "Publishing an advertisement in a newspaper", "Obtaining consent of the principal debtor"],
    0, "A",
    "Section 130: 'A continuing guarantee may at any time be revoked by the surety, as to future transactions, by notice to the creditor'. Past accrued transactions remain binding.",
    {"A": "Correct. Section 130 allows revocation as to future transactions by notice to creditor.", "B": "Civil judge application is unnecessary.", "C": "Newspaper notice is not sufficient unless creditor receives actual notice.", "D": "Principal debtor's consent is not required."},
    "Easy", "Indian Contract Act, 1872, Section 130", "Recall revocation of continuing guarantee by notice."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-006", "ch-cnt-10", "top-cnt-10-01",
    "Under Section 133 of the Indian Contract Act, any variance, made without the surety's consent, in the terms of the contract between the principal debtor and the creditor:",
    ["Discharges the surety as to transactions subsequent to the variance", "Has no effect on the surety's liability", "Makes the contract void ab initio", "Doubles the surety's liability"],
    0, "A",
    "Section 133: Any unauthorized variance in the contract between principal debtor and creditor discharges the surety as to transactions subsequent to the variance.",
    {"A": "Correct. Section 133 discharges surety upon unauthorized variance in contract terms.", "B": "Surety is discharged because his risk has been altered without consent.", "C": "The main contract between debtor and creditor remains valid.", "D": "Surety liability cannot be increased without consent."},
    "Medium", "Indian Contract Act, 1872, Section 133", "Identify discharge of surety by variance under Section 133."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-007", "ch-cnt-10", "top-cnt-10-01",
    "Under Section 135 of the Indian Contract Act, a contract between the creditor and the principal debtor, by which the creditor makes a composition with, or promises to give time to, or not to sue, the principal debtor:",
    ["Discharges the surety, unless the surety assents to such contract", "Does not affect the surety in any manner", "Increases the limitation period against the surety", "Makes the principal debtor immune from civil suit"],
    0, "A",
    "Section 135: Giving time, composition, or agreement not to sue the principal debtor without surety's assent discharges the surety.",
    {"A": "Correct. Section 135 discharges the surety if creditor gives time or makes composition without surety's assent.", "B": "Surety is discharged as his right to immediate payment and subrogation is compromised.", "C": "Limitation is not statutorily increased.", "D": "Debtor remains liable under the composition agreement."},
    "Medium", "Indian Contract Act, 1872, Section 135", "Master discharge of surety by giving time under Section 135."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-008", "ch-cnt-10", "top-cnt-10-01",
    "Under Section 141 of the Indian Contract Act, a surety is entitled to the benefit of every security which the creditor has against the principal debtor at the time when the contract of suretyship is entered into; and if the creditor loses or parts with such security without surety's consent:",
    ["The surety is discharged to the extent of the value of the security", "The surety is completely discharged even if security was worth Re 1", "The creditor is guilty of criminal breach of trust", "The principal debtor is discharged from debt"],
    0, "A",
    "Section 141 codifies the surety's right to securities: if creditor loses or parts with security without surety's consent, surety is discharged to the extent of the value of the security.",
    {"A": "Correct. Section 141 discharges the surety pro tanto (to the extent of the value of security).", "B": "Discharge is pro tanto, not necessarily total unless security equaled the whole debt.", "C": "No criminal breach of trust is committed.", "D": "Principal debtor remains liable for his debt."},
    "Hard", "Indian Contract Act, 1872, Section 141", "Apply pro tanto discharge under Section 141."
))

# top-cnt-10-02: Bailment: Duties of Bailor & Bailee, Bailee's Lien (Sections 148–171) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-10-009", "ch-cnt-10", "top-cnt-10-01",
    "Under Section 148 of the Indian Contract Act, a 'bailment' is the delivery of goods by one person to another for some purpose, upon a contract that they shall:",
    ["Become the permanent property of the bailee", "When the purpose is accomplished, be returned or otherwise disposed of according to the directions of the person delivering them", "Be sold at an auction after 7 days", "Be destroyed after inspection"],
    1, "B",
    "Section 148: Bailment is delivery of movable goods upon a contract that, when the purpose is accomplished, they shall be returned or disposed of according to bailor's directions.",
    {"A": "Ownership does not pass in bailment; only possession is transferred.", "B": "Correct. Section 148 statutory definition of bailment.", "C": "Bailee has no general right to auction goods.", "D": "Goods must be returned or disposed of as directed, not destroyed."},
    "Easy", "Indian Contract Act, 1872, Section 148", "Recall statutory definition of bailment under Section 148."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-010", "ch-cnt-10", "top-cnt-10-02",
    "In Ultzen v. Nicolls (1894), a customer went into a restaurant and an attendant took his coat and hung it on a hook behind the customer. The coat was stolen. The court held:",
    ["There was no bailment because the customer was inside the restaurant", "There was a valid bailment because the waiter took possession, and the restaurant was liable for negligence", "The customer was solely responsible under caveat emptor", "The thief alone could be sued"],
    1, "B",
    "The court held that taking possession of the customer's coat by the attendant created a bailment, and the restaurant proprietor was liable for failing to exercise proper care.",
    {"A": "Physical assumption of control by waiter created delivery of possession.", "B": "Correct. Leading case establishing bailment upon taking possession of garment.", "C": "Caveat emptor applies to sale of goods, not bailment.", "D": "Bailee is liable for breach of duty of care."},
    "Medium", "Ultzen v. Nicolls (1894) 1 QB 92", "Apply delivery of possession test in bailment."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-011", "ch-cnt-10", "top-cnt-10-02",
    "In Kaliaperumal Pillai v. Visalakshmi Achi (AIR 1938 Mad 32), a lady gave gold to a goldsmith to melt and make jewels. Every evening she took the half-made jewels, placed them in a box, locked it, kept the key with herself, and left the box in the goldsmith's premises. The jewels were stolen at night. The court held:",
    ["The goldsmith was liable as a bailee", "There was no bailment at night because possession was retained by the lady who locked the box and kept the key; the goldsmith was not liable", "The goldsmith was liable for conversion", "The lady was liable to pay the goldsmith double wages"],
    1, "B",
    "The Madras High Court held that bailment requires transfer of exclusive possession. Since the lady kept the key and locked the box, possession was not with the goldsmith at night.",
    {"A": "Bailment was absent at night due to lack of possession.", "B": "Correct. Leading Indian authority: without transfer of exclusive control, there is no bailment.", "C": "No conversion occurred as goldsmith did not take or misuse goods.", "D": "No double wages award exists in law."},
    "Hard", "Madras High Court: Kaliaperumal Pillai v. Visalakshmi Achi (AIR 1938 Mad 32)", "Master Kaliaperumal rule on exclusive possession in bailment."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-012", "ch-cnt-10", "top-cnt-10-02",
    "Under Section 151 of the Indian Contract Act, in all cases of bailment, what standard of care is required of the bailee?",
    ["The highest imaginable standard of care under strict liability", "To take as much care of the goods bailed to him as a man of ordinary prudence would, under similar circumstances, take of his own goods of the same bulk, quality and value", "Only minimal care; bailee is liable only for gross fraud", "Bailee is an absolute insurer against all perils"],
    1, "B",
    "Section 151 sets a uniform standard of care: that of a man of ordinary prudence taking care of his own goods of similar quality and value. (Section 152 exempts bailee if this care is taken).",
    {"A": "Bailee is not an absolute insurer under strict liability.", "B": "Correct. Section 151 statutory standard of ordinary prudence.", "C": "Bailee is liable for ordinary negligence, not merely gross fraud.", "D": "Bailee is not an insurer under Section 151."},
    "Easy", "Indian Contract Act, 1872, Section 151", "Identify bailee's standard of care under Section 151."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-013", "ch-cnt-10", "top-cnt-10-02",
    "Under Section 150 of the Indian Contract Act, what is the duty of a bailor regarding faults in goods bailed?",
    ["A gratuitous bailor is bound to disclose faults known to him; a bailor for reward is responsible for damages whether he was aware of the faults or not", "No bailor is ever responsible for any defect", "All bailors are strictly liable for unknown defects in gratuitous bailments", "Bailor is only liable if he is a manufacturer"],
    0, "A",
    "Section 150 distinguishes gratuitous bailor (liable only for known faults not disclosed) from bailor for hire/reward (liable for faults whether aware of them or not).",
    {"A": "Correct. Section 150 statutory distinction between gratuitous bailor and bailor for hire.", "B": "Bailors have statutory disclosure duties under Section 150.", "C": "Gratuitous bailor is not liable for unknown defects.", "D": "Duty applies to all bailors, not just manufacturers."},
    "Medium", "Indian Contract Act, 1872, Section 150", "Distinguish gratuitous vs reward bailor liability under Section 150."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-014", "ch-cnt-10", "top-cnt-10-02",
    "Under Section 154 of the Indian Contract Act, if the bailee makes any use of the goods bailed which is not according to the conditions of the bailment:",
    ["He is liable to make compensation to the bailor for any damage arising to the goods from or during such use of them", "The contract is converted into a sale", "The bailor forfeits the goods", "The bailee acquires absolute title"],
    0, "A",
    "Section 154: Bailee using goods unauthorizedly is strictly liable for any damage arising during such use, even if damage occurs by inevitable accident.",
    {"A": "Correct. Section 154 imposes strict liability for unauthorized use of bailed goods.", "B": "Unauthorized use does not convert bailment into sale.", "C": "Bailor does not forfeit ownership.", "D": "Bailee can never acquire title by wrongful use."},
    "Medium", "Indian Contract Act, 1872, Section 154", "Recall bailee liability for unauthorized use under Section 154."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-015", "ch-cnt-10", "top-cnt-10-02",
    "Under Section 170 of the Indian Contract Act, a 'particular lien' is available to a bailee where:",
    ["He has rendered any service involving the exercise of labor or skill in respect of the goods bailed", "He has lent money on mortgage to the bailor", "The bailor is an undischarged insolvent", "The bailee is a police officer"],
    0, "A",
    "Section 170 gives the bailee a particular lien to retain goods until remuneration is paid, where he has rendered service involving labor or skill improving the goods (e.g. tailor, mechanic).",
    {"A": "Correct. Section 170 defines bailee's particular lien for labor/skill expended.", "B": "Lending on mortgage is not the basis of bailee's particular lien.", "C": "Insolvency does not create particular lien.", "D": "Police officers do not hold commercial bailee liens."},
    "Easy", "Indian Contract Act, 1872, Section 170", "Recall bailee particular lien under Section 170."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-016", "ch-cnt-10", "top-cnt-10-02",
    "Under Section 171 of the Indian Contract Act, who among the following entitled parties possess a statutory 'general lien' to retain any goods bailed to them as a security for a general balance of account?",
    ["Bankers, factors, wharfingers, advocates of High Court, and policy-brokers", "Tailors, carpenters, and jewelers", "Railway passengers", "Landlords over tenants' furniture"],
    0, "A",
    "Section 171 restricts general lien to five named classes: bankers, factors, wharfingers, attorneys of a High Court, and policy-brokers, unless excluded by contract.",
    {"A": "Correct. Section 171 specifies these five classes entitled to general lien.", "B": "Tailors and artisans have only a particular lien under Section 170.", "C": "Passengers have no general lien.", "D": "Landlords have distress remedies under special tenancy acts, not Section 171 general lien."},
    "Medium", "Indian Contract Act, 1872, Section 171", "Identify five classes possessing general lien under Section 171."
))

# top-cnt-10-03: Pledge: Rights of Pawnee & Pledge by Non-Owners (Sections 172–181) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-10-017", "ch-cnt-10", "top-cnt-10-03",
    "Under Section 172 of the Indian Contract Act, a 'pledge' is defined as:",
    ["The bailment of goods as security for payment of a debt or performance of a promise", "The sale of goods with a buy-back clause", "The mortgage of immovable land", "The gratuitous loan of a motor car"],
    0, "A",
    "Section 172 defines pledge (pawn): bailment of goods as security for payment of a debt or performance of a promise. The bailor is the 'pawnor' and the bailee is the 'pawnee'.",
    {"A": "Correct. Section 172 statutory definition of pledge.", "B": "Sale with buyback is a conditional sale, not a pledge.", "C": "Mortgage of land is governed by TPA Section 58.", "D": "Gratuitous loan is simple commodatum/bailment, not pledge."},
    "Easy", "Indian Contract Act, 1872, Section 172", "Identify statutory definition of pledge under Section 172."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-018", "ch-cnt-10", "top-cnt-10-03",
    "What are the rights of a pawnee under Section 176 of the Indian Contract Act if the pawnor makes default in payment of the debt at the stipulated time?",
    ["The pawnee may bring a suit against the pawnor upon the debt, and retain the goods as a collateral security; or he may sell the thing pledged, on giving the pawnor reasonable notice of the sale", "The pawnee automatically becomes the absolute owner without notice", "The pawnee must destroy the goods", "The pawnee must file a criminal case under BNS"],
    0, "A",
    "Section 176 gives pawnee two remedies: (1) sue on debt and retain goods as collateral; or (2) sell the pledged goods after giving reasonable notice of sale to the pawnor.",
    {"A": "Correct. Section 176 remedies: suit with retention of goods, or sale on reasonable notice.", "B": "Pledgee never becomes absolute owner automatically; foreclosure is not available.", "C": "Destroying goods is illegal conversion.", "D": "Default in debt payment is a civil matter."},
    "Medium", "Indian Contract Act, 1872, Section 176", "Master pawnee rights upon default under Section 176."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-019", "ch-cnt-10", "top-cnt-10-03",
    "Under Section 176, if the proceeds of the sale of pledged goods are less than the amount due, and if greater than the amount due:",
    ["The pawnor is still liable to pay the balance; and the pawnee shall pay over the surplus to the pawnor", "The loss lies on the pawnee, and pawnee keeps surplus", "The state government takes the surplus", "The pawnor is imprisoned for the balance"],
    0, "A",
    "Section 176 explicitly provides: if proceeds are less, pawnor is liable for balance; if proceeds are greater, pawnee must pay over the surplus to the pawnor.",
    {"A": "Correct. Section 176 statutory rule on shortfall and surplus.", "B": "Pawnee cannot retain surplus nor absorb deficit.", "C": "Surplus belongs to pawnor, not state.", "D": "No civil imprisonment for honest shortfall."},
    "Easy", "Indian Contract Act, 1872, Section 176", "Recall shortfall and surplus rules under Section 176."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-020", "ch-cnt-10", "top-cnt-10-03",
    "Is reasonable notice of sale to the pawnor under Section 176 mandatory before the pawnee sells the pledged goods?",
    ["Yes, reasonable notice is mandatory and cannot be waived even by express contract (The Bank of Chittoor v. P. Narasimbulu)", "No, notice is optional and can be dispensed with at pawnee's discretion", "Only if the goods are perishable", "Only for debts exceeding Rs 50 lakhs"],
    0, "A",
    "Reasonable notice under Section 176 is statutory and mandatory. Any clause in a contract waiving notice of sale is void as contrary to Section 176.",
    {"A": "Correct. Settled law: notice of sale under Section 176 is mandatory and cannot be contracted out.", "B": "Notice is not optional.", "C": "Even for perishable goods, reasonable notice is required under Section 176.", "D": "No monetary threshold exists."},
    "Hard", "Bank of Chittoor v. Narasimbulu (AIR 1966 AP 163)", "Analyze mandatory nature of notice under Section 176."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-021", "ch-cnt-10", "top-cnt-10-03",
    "Under Section 177 of the Indian Contract Act, what is the 'right to redeem' of a defaulting pawnor?",
    ["He can redeem the goods at any subsequent time before the actual sale of them, on paying the debt and any expenses caused by his default", "His right of redemption is extinguished immediately upon the default date", "He can redeem only within 24 hours of default", "He can redeem only with permission of the High Court"],
    0, "A",
    "Section 177: If a time is stipulated for payment and pawnor defaults, he may redeem the goods at any subsequent time before the actual sale, paying expenses caused by default.",
    {"A": "Correct. Section 177 preserves redemption right until actual sale takes place.", "B": "Default date does not extinguish right of redemption.", "C": "No 24-hour limit applies.", "D": "High Court permission is not needed."},
    "Medium", "Indian Contract Act, 1872, Section 177", "Identify right to redeem before sale under Section 177."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-022", "ch-cnt-10", "top-cnt-10-03",
    "Under Section 178 of the Indian Contract Act, a pledge made by a 'mercantile agent' who is in possession of goods or documents of title with the consent of the owner is:",
    ["Valid, provided the pawnee acts in good faith and without notice of lack of authority, and the agent acts in ordinary course of business", "Void ab initio under the nemo dat rule", "Voidable at the option of the principal under all circumstances", "A criminal conspiracy under BNS"],
    0, "A",
    "Section 178 creates a statutory exception to nemo dat: pledge by mercantile agent in possession with owner's consent is valid if pawnee acts in good faith without notice.",
    {"A": "Correct. Section 178 validates pledge by mercantile agent in good faith.", "B": "Section 178 is an express exception overriding nemo dat.", "C": "It is valid and binding, not voidable.", "D": "It is a lawful commercial dealing."},
    "Medium", "Indian Contract Act, 1872, Section 178", "Master pledge by mercantile agent under Section 178."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-023", "ch-cnt-10", "top-cnt-10-03",
    "Under Section 178A of the Indian Contract Act, where goods are pledged by a person who obtained possession under a contract voidable under Section 19 or Section 19A:",
    ["The pledge is valid if the contract had not been rescinded at the time of the pledge and the pawnee acted in good faith and without notice", "The pledge is void ab initio in all cases", "The original owner can recover the goods without paying the debt", "The pawnee must deliver the goods to the police"],
    0, "A",
    "Section 178A: Pledge by person in possession under voidable contract (e.g. obtained by fraud/coercion) is valid if pledged before rescission to a bona fide pawnee without notice.",
    {"A": "Correct. Section 178A protects bona fide pawnees before contract rescission.", "B": "It is not void ab initio; title is voidable, passing good security before avoidance.", "C": "Owner must redeem by satisfying pawnee's debt.", "D": "No police seizure is authorized against bona fide pledgee."},
    "Hard", "Indian Contract Act, 1872, Section 178A", "Apply Section 178A on pledge under voidable contract."
))
mcqs.append(make_mcq(
    "mcq-cnt-10-024", "ch-cnt-10", "top-cnt-10-03",
    "Under Section 179 of the Indian Contract Act, where a person pledges goods in which he has only a limited interest (e.g. a finder or a person with a lien):",
    ["The pledge is completely void", "The pledge is valid to the extent of that limited interest", "The pledge transfers absolute ownership to the pawnee", "The pawnee is guilty of criminal misappropriation"],
    1, "B",
    "Section 179: 'Where a person pledges goods in which he has only a limited interest, the pledge is valid to the extent of that interest'.",
    {"A": "Pledge is not completely void; it is valid to the extent of pledgor's interest.", "B": "Correct. Section 179 validates pledge to the extent of limited interest.", "C": "Pawnee cannot get greater interest than the pledgor possessed.", "D": "Pledging one's limited interest is not criminal misappropriation."},
    "Medium", "Indian Contract Act, 1872, Section 179", "Recall rule on pledge by person with limited interest under Section 179."
))

# =========================================================================
# CHAPTER 11: SPECIAL CONTRACTS: LAW OF AGENCY (16 MCQs)
# =========================================================================
# top-cnt-11-01: Contract of Agency: Creation, Authority & Sub-Agent (Sections 182–210) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-11-001", "ch-cnt-11", "top-cnt-11-01",
    "Under Section 182 of the Indian Contract Act, an 'agent' is defined as a person employed to:",
    ["Do any act for another, or to represent another in dealings with third persons", "Perform manual labor in a factory", "Act as an independent contractor without control", "Supervise government examinations"],
    0, "A",
    "Section 182 defines agent: 'a person employed to do any act for another, or to represent another in dealings with third persons'. The person for whom act is done is the 'principal'.",
    {"A": "Correct. Section 182 statutory definition of agent and principal.", "B": "Manual labor without representational capacity is servant/workman, not agent.", "C": "Independent contractors act on their own account, not representing principals.", "D": "Exam supervisors are public servants, not contractual commercial agents."},
    "Easy", "Indian Contract Act, 1872, Section 182", "Recall statutory definition of agent under Section 182."
))
mcqs.append(make_mcq(
    "mcq-cnt-11-002", "ch-cnt-11", "top-cnt-11-01",
    "Under Section 185 of the Indian Contract Act, what consideration is necessary to create an agency?",
    ["Valuable consideration in money", "No consideration is necessary to create an agency", "Mutual promises under registered deed", "A minimum retainer fee of Rs 1,000"],
    1, "B",
    "Section 185 explicitly states: 'No consideration is necessary to create an agency'. Detriment suffered by principal in entrusting affairs to agent suffices.",
    {"A": "Consideration is not required.", "B": "Correct. Section 185 explicitly dispenses with consideration in creating agency.", "C": "Registration is not required.", "D": "Retainer fees are not legally necessary to create valid agency."},
    "Easy", "Indian Contract Act, 1872, Section 185", "Recall rule on consideration in agency under Section 185."
))
mcqs.append(make_mcq(
    "mcq-cnt-11-003", "ch-cnt-11", "top-cnt-11-01",
    "Under Section 184 of the Indian Contract Act, as between the principal and third persons, who may become an agent?",
    ["Only an adult of sound mind", "Any person may become an agent, including a minor or person of unsound mind, but an incompetent agent is not responsible to his principal", "Only an advocate registered with the Bar Council", "Only a corporate entity"],
    1, "B",
    "Section 184: Anyone can be an agent as between principal and third parties (qui facit per alium facit per se), but a minor agent incurs no personal liability to his principal.",
    {"A": "Adult status is required to be a principal (Section 183), but not to be an agent.", "B": "Correct. Section 184 allows any person to be an agent, qualifying liability to principal.", "C": "Advocate status is not required for commercial agency.", "D": "Natural persons are standard agents."},
    "Medium", "Indian Contract Act, 1872, Section 184", "Identify who may be an agent under Section 184."
))
mcqs.append(make_mcq(
    "mcq-cnt-11-004", "ch-cnt-11", "top-cnt-11-01",
    "Under Section 189 of the Indian Contract Act, what is the extent of an agent's authority in an emergency?",
    ["The agent has authority to do all such acts for the purpose of protecting his principal from loss as would be done by a person of ordinary prudence in his own case", "The agent's authority is completely suspended until principal replies", "The agent can sell all principal's assets to himself", "The agent must file an urgent writ petition"],
    0, "A",
    "Section 189 (Agent's authority in an emergency): Agent has authority to do all acts of an ordinary prudent man to protect the principal from imminent loss.",
    {"A": "Correct. Section 189 emergency authority: acts of ordinary prudence to protect principal.", "B": "Emergency expands authority, rather than suspending it.", "C": "Self-dealing is forbidden.", "D": "Writ petitions are irrelevant to commercial agency emergencies."},
    "Medium", "Indian Contract Act, 1872, Section 189", "Recall agent's emergency authority under Section 189."
))
mcqs.append(make_mcq(
    "mcq-cnt-11-005", "ch-cnt-11", "top-cnt-11-01",
    "Under Section 190 of the Indian Contract Act, what is the general rule regarding delegation of authority by an agent (Delegatus non potest delegare)?",
    ["An agent can freely delegate all his powers to anyone", "An agent cannot lawfully employ another to perform acts which he has expressly or impliedly undertaken to perform personally, unless by ordinary custom of trade or from nature of agency a sub-agent may be employed", "Sub-agents are prohibited by criminal law", "Delegation is allowed only with approval of the High Court"],
    1, "B",
    "Section 190 codifies the maxim delegatus non potest delegare: an agent cannot delegate personal duties unless trade custom or nature of business permits.",
    {"A": "Unchecked delegation is forbidden.", "B": "Correct. Section 190 codifies delegatus non potest delegare with trade custom exceptions.", "C": "Delegation is not a crime.", "D": "Judicial approval is not required."},
    "Easy", "Indian Contract Act, 1872, Section 190", "Master delegatus non potest delegare under Section 190."
))
mcqs.append(make_mcq(
    "mcq-cnt-11-006", "ch-cnt-11", "top-cnt-11-01",
    "Under Section 192 of the Indian Contract Act, where a sub-agent is PROPERLY appointed by an agent:",
    ["The principal is represented by the sub-agent and bound by his acts; the agent is responsible to the principal for the acts of the sub-agent; and the sub-agent is responsible for his acts to the agent, but not to the principal (except in case of fraud or willful wrong)", "The sub-agent is directly responsible to the principal in all cases", "The original agent is discharged from all liability", "The sub-agent has no authority whatsoever"],
    0, "A",
    "Section 192 establishes the triangular relationship of a properly appointed sub-agent: principal is bound; agent is liable to principal; sub-agent is liable only to agent (privity of agency), except for fraud.",
    {"A": "Correct. Section 192 governs properly appointed sub-agent relationships.", "B": "There is no privity between principal and sub-agent, except in fraud/willful wrong.", "C": "The agent remains responsible to principal for sub-agent's acts.", "D": "Sub-agent represents principal as regards third parties."},
    "Hard", "Indian Contract Act, 1872, Section 192", "Master legal relationship of properly appointed sub-agent under Section 192."
))
mcqs.append(make_mcq(
    "mcq-cnt-11-007", "ch-cnt-11", "top-cnt-11-01",
    "Under Section 193 of the Indian Contract Act, where an agent, without having authority to do so, appoints a person to act as a sub-agent (IMPROPER appointment):",
    ["The principal is bound by the acts of such sub-agent", "The agent is responsible for the acts of the sub-agent both to the principal and to third persons; the principal is not represented by nor responsible for the acts of the person so employed", "The sub-agent becomes an employee of the state", "The contract of agency is void ab initio"],
    1, "B",
    "Section 193: Where sub-agent is appointed without authority, principal is not bound nor represented; the agent is personally responsible for all sub-agent acts to both principal and third parties.",
    {"A": "Principal is not represented nor bound by unauthorized sub-agent.", "B": "Correct. Section 193 makes agent solely responsible for improperly appointed sub-agent.", "C": "Sub-agent does not become a state employee.", "D": "Agency is not void ab initio, but agent is in breach."},
    "Medium", "Indian Contract Act, 1872, Section 193", "Identify liability for improperly appointed sub-agent under Section 193."
))
mcqs.append(make_mcq(
    "mcq-cnt-11-008", "ch-cnt-11", "top-cnt-11-01",
    "What is the difference between a 'sub-agent' (Section 191) and a 'substituted agent' (Section 194)?",
    ["A sub-agent acts under the control of the agent; a substituted agent is named by the agent on the principal's authority and enters into direct privity of contract with the principal", "A substituted agent is illegal, while a sub-agent is legal", "Sub-agent is appointed by court, substituted agent by police", "There is no legal difference between them"],
    0, "A",
    "Under Sections 194 and 195, a substituted agent is a person named by the agent to act for the principal in business of agency; he becomes a direct agent of the principal (privity created).",
    {"A": "Correct. Substituted agent enters into direct contractual relation with principal; sub-agent acts under agent.", "B": "Both are recognized statutory concepts under the Contract Act.", "C": "Neither is appointed by court or police.", "D": "They are fundamentally distinct in liability and privity."},
    "Hard", "Indian Contract Act, 1872, Sections 191, 194, 195", "Distinguish sub-agent from substituted agent."
))

# top-cnt-11-02: Rights, Duties, Revocation & Principal's Liability (Sections 211–238) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-11-009", "ch-cnt-11", "top-cnt-11-02",
    "Under Section 211 of the Indian Contract Act, what is the primary duty of an agent in conducting the business of his principal?",
    ["To conduct the business according to the directions given by the principal, or, in the absence of directions, according to the custom of the place where business is conducted", "To maximize his own personal commission at all costs", "To follow instructions of the local chamber of commerce", "To consult the sub-registrar weekly"],
    0, "A",
    "Section 211: An agent is bound to conduct business according to principal's directions; in absence of directions, according to trade custom. If he does otherwise, he must make good any loss.",
    {"A": "Correct. Section 211 statutory duty to obey directions or trade custom.", "B": "Self-dealing and secret profits violate agent's duty.", "C": "Chamber of commerce does not override principal's directions.", "D": "Weekly consultation is not required."},
    "Easy", "Indian Contract Act, 1872, Section 211", "Recall agent's primary duty under Section 211."
))
mcqs.append(make_mcq(
    "mcq-cnt-11-010", "ch-cnt-11", "top-cnt-11-02",
    "Under Section 215 and 216 of the Indian Contract Act, if an agent deals on his own account in the business of agency without the knowledge and consent of his principal:",
    ["The principal may repudiate the transaction if it is disadvantageous, and claim from the agent any benefit/secret profit resulting to the agent from the transaction", "The agent automatically acquires ownership of principal's business", "The transaction is valid and agent keeps all profits", "The agent is immune from accounting"],
    0, "A",
    "Sections 215 and 216 strictly prohibit self-dealing and secret profits: principal may repudiate the transaction and claim all profits made by the agent.",
    {"A": "Correct. Sections 215 and 216 entitle principal to repudiate and disgorge secret profits.", "B": "Agent does not acquire principal's business.", "C": "Agent cannot retain secret profits derived from breach of duty.", "D": "Agent is strictly bound to account under Section 213."},
    "Medium", "Indian Contract Act, 1872, Sections 215, 216", "Master rules against self-dealing and secret profit in agency."
))
mcqs.append(make_mcq(
    "mcq-cnt-11-011", "ch-cnt-11", "top-cnt-11-02",
    "Under Section 217 and 221 of the Indian Contract Act, what rights of retainer and lien does an agent possess?",
    ["Agent may retain moneys received on account of principal for advances, expenses, and commission; and has a particular lien on goods, papers, and property of principal for commission and disbursements", "Agent has absolute ownership over principal's property until paid", "Agent can sell principal's real estate without court decree", "Agent has no lien whatsoever"],
    0, "A",
    "Section 217 grants right of retainer out of sums received; Section 221 grants agent's lien on principal's goods, papers, and property for commission, disbursements, and services.",
    {"A": "Correct. Sections 217 and 221 grant agent right of retainer and particular lien.", "B": "Lien confers right to retain possession, not ownership.", "C": "Agent cannot sell real estate under simple possessory lien.", "D": "Statute explicitly provides retainer and lien rights."},
    "Medium", "Indian Contract Act, 1872, Sections 217, 221", "Recall agent's right of retainer and lien."
))
mcqs.append(make_mcq(
    "mcq-cnt-11-012", "ch-cnt-11", "top-cnt-11-02",
    "Under Section 201 of the Indian Contract Act, an agency is terminated by:",
    ["Revocation by principal, renunciation by agent, completion of business, death/unsoundness of principal or agent, or insolvency of principal", "Marriage of the agent", "Change of political government", "The agent taking a holiday"],
    0, "A",
    "Section 201 enumerates the modes of termination: revocation, renunciation, completion of business, death/unsoundness of mind of principal or agent, or adjudication of principal as insolvent.",
    {"A": "Correct. Section 201 statutory grounds for termination of agency.", "B": "Marriage does not terminate commercial agency.", "C": "Change of government does not terminate private contracts.", "D": "Holidays do not terminate agency."},
    "Easy", "Indian Contract Act, 1872, Section 201", "Identify statutory modes of termination of agency."
))
mcqs.append(make_mcq(
    "mcq-cnt-11-013", "ch-cnt-11", "top-cnt-11-02",
    "Under Section 202 of the Indian Contract Act, where the agent has himself an interest in the property which forms the subject-matter of the agency (agency coupled with interest):",
    ["The agency cannot, in the absence of an express contract, be terminated to the prejudice of such interest by revocation or death/unsoundness of the principal", "The principal can revoke the agency at will at any time", "The agency is void ab initio under Section 23", "The agent must pay a fine to the principal"],
    0, "A",
    "Section 202: An agency coupled with interest is irrevocable to the prejudice of that interest; it does not terminate even upon death or insanity of the principal (Smart v. Sandars).",
    {"A": "Correct. Section 202 makes agency coupled with interest irrevocable.", "B": "Principal cannot revoke agency coupled with interest to agent's prejudice.", "C": "Agency coupled with interest is completely valid.", "D": "No fine is payable."},
    "Medium", "Indian Contract Act, 1872, Section 202", "Master agency coupled with interest under Section 202."
))
mcqs.append(make_mcq(
    "mcq-cnt-11-014", "ch-cnt-11", "top-cnt-11-02",
    "Under Section 226 of the Indian Contract Act, contracts entered into through an agent, and obligations arising from acts done by an agent, may be enforced in the same manner, and will have the same legal consequences, as if:",
    ["The contracts had been entered into and the acts done by the principal in person", "The agent had acted as a judicial magistrate", "The third party were a joint promisor", "The contracts were entered into under seal"],
    0, "A",
    "Section 226 codifies the fundamental maxim qui facit per alium facit per se: acts of the agent within authority have identical legal consequences as if done by the principal personally.",
    {"A": "Correct. Section 226 codifies qui facit per alium facit per se.", "B": "Agent does not act as a magistrate.", "C": "Third party is the promisee/promisor, not joint promisor with principal.", "D": "Seals are English formalities not required in India."},
    "Easy", "Indian Contract Act, 1872, Section 226", "Recall qui facit per alium facit per se under Section 226."
))
mcqs.append(make_mcq(
    "mcq-cnt-11-015", "ch-cnt-11", "top-cnt-11-02",
    "Under Section 230 of the Indian Contract Act, in the absence of any contract to that effect, an agent cannot personally enforce contracts entered into by him on behalf of his principal, nor is he personally bound by them. In which of the following cases is a personal contract by the agent PRESUMED to exist?",
    ["Where the contract is made by an agent for the sale or purchase of goods for a merchant resident abroad", "Where the agent does not disclose the name of his principal (undisclosed principal)", "Where the principal, though disclosed, cannot be sued (e.g. foreign sovereign or minor)", "All of the above"],
    3, "D",
    "Section 230 paragraph 2 sets out the three statutory presumptions of agent's personal liability: foreign principal, undisclosed principal, and principal who cannot be sued.",
    {"A": "Foreign principal presumption under Section 230(1).", "B": "Undisclosed principal presumption under Section 230(2).", "C": "Non-suable principal presumption under Section 230(3).", "D": "Correct. All three cases raise statutory presumption of agent's personal liability under Section 230."},
    "Medium", "Indian Contract Act, 1872, Section 230", "Identify statutory presumptions of agent personal liability under Section 230."
))
mcqs.append(make_mcq(
    "mcq-cnt-11-016", "ch-cnt-11", "top-cnt-11-02",
    "Under Section 238 of the Indian Contract Act, misrepresentations made, or frauds committed, by agents acting in the course of their business for their principals, have the same effect on agreements made by such agents as if:",
    ["Such misrepresentations or frauds had been made or committed by the principals", "The contracts were automatically converted into criminal bonds", "The agent alone were liable and principal completely exempt", "The third party had committed contributory negligence"],
    0, "A",
    "Section 238: Principal is vicariously liable for frauds and misrepresentations of his agent committed in the course of the principal's business (Lloyd v. Grace, Smith & Co., 1912).",
    {"A": "Correct. Section 238 imposes vicarious contractual liability on principal for agent's fraud in course of business.", "B": "Civil agreements are not converted into criminal bonds.", "C": "Principal cannot disclaim liability for agent acting within course of employment.", "D": "Contributory negligence is not presumed against third party."},
    "Hard", "Indian Contract Act, 1872, Section 238; Lloyd v. Grace, Smith & Co. (1912) AC 716", "Master principal's liability for agent's fraud under Section 238."
))

print(f"Total MCQs generated for Part 3: {len(mcqs)}")

with open('scripts/data_contract_mcqs_3.py', 'w', encoding='utf-8') as f:
    f.write("# Contract Law MCQs Part 3 (Chapters 8 to 11: 88 MCQs)\n")
    f.write("MCQS_PART3 = " + json.dumps(mcqs, indent=2) + "\n")

print("Successfully written scripts/data_contract_mcqs_3.py")
