# Complete Contract MCQs Part 2 Builder (Chapters 5 to 7: 60 MCQs)
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

# ==================================================
# CHAPTER 5: MISREPRESENTATION & MISTAKE (24 MCQs)
# ==================================================
# top-cnt-05-01: Misrepresentation: Types, Remedies & Exceptions (Sections 18, 19) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-05-001", "ch-cnt-05", "top-cnt-05-01",
    "Under Section 18 of the Indian Contract Act, 'misrepresentation' means and includes:",
    ["Positive assertion, in a manner not warranted by information, of that which is not true, though believed to be true", "Any breach of duty which, without an intent to deceive, gains an advantage to the person committing it", "Causing, however innocently, a party to an agreement to make a mistake as to the substance of the thing", "All of the above"],
    3, "D",
    "Section 18 defines misrepresentation in three clauses: unwarranted positive assertion, breach of duty without intent to deceive gaining advantage, and innocent mistake as to substance.",
    {"A": "Unwarranted assertion is clause (1) of Section 18.", "B": "Breach of duty gaining advantage is clause (2) of Section 18.", "C": "Innocent inducement of mistake as to substance is clause (3) of Section 18.", "D": "Correct. All three clauses are statutory definitions under Section 18."},
    "Easy", "Indian Contract Act, 1872, Section 18", "Identify statutory clauses of misrepresentation under Section 18."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-002", "ch-cnt-05", "top-cnt-05-01",
    "In Derry v. Peek (1889), where tramway directors stated in a prospectus that they had statutory authority to use steam power, honestly believing the Board of Trade would grant consent as a matter of course:",
    ["The directors were guilty of fraud", "The directors were guilty of innocent misrepresentation, not fraud, because they honestly believed in their statement", "The contract was void ab initio", "The directors were sentenced to prison"],
    1, "B",
    "The House of Lords held that honesty of belief negates fraud. Because the directors honestly believed consent would be given, they were not guilty of fraud, though it was misrepresentation.",
    {"A": "Fraud was rejected by the House of Lords for lack of dishonesty.", "B": "Correct. Honest belief defeats fraud and amounts to innocent misrepresentation.", "C": "Misrepresentation makes contract voidable, not void ab initio.", "D": "No criminal sanctions were imposed."},
    "Medium", "House of Lords: Derry v. Peek (1889) 14 App Cas 337", "Distinguish honest belief in misrepresentation from fraud."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-003", "ch-cnt-05", "top-cnt-05-01",
    "Under Section 19 of the Indian Contract Act, what remedies are available to a party whose consent was caused by misrepresentation?",
    ["Rescind the contract, or insist that the contract be performed putting him in the position as if the representation were true", "Claim exemplary damages in tort for deceit", "Have the other party arrested under a warrant", "File an appeal directly to the Supreme Court"],
    0, "A",
    "Section 19 gives the aggrieved party the option to rescind (avoid) the contract, or to affirm and insist on being put in the position as if representation was true.",
    {"A": "Correct. Avoidance or affirmation with restoration under Section 19.", "B": "Damages for deceit in tort lie only for fraud, not innocent misrepresentation.", "C": "Civil misrepresentation does not allow arrest warrants.", "D": "Appeals follow regular civil procedural hierarchy."},
    "Medium", "Indian Contract Act, 1872, Section 19", "Recall remedies for misrepresentation under Section 19."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-004", "ch-cnt-05", "top-cnt-05-01",
    "Under the Exception to Section 19, if consent was caused by misrepresentation, the contract is NOT voidable if the party whose consent was so caused:",
    ["Had the means of discovering the truth with ordinary diligence", "Consulted a lawyer before signing", "Was an illiterate person", "Paid consideration in cash"],
    0, "A",
    "Exception to Section 19 expressly bars rescission where the aggrieved party had the means of discovering the truth with ordinary diligence.",
    {"A": "Correct. The Exception to Section 19 protects transactions where ordinary diligence would reveal the truth.", "B": "Consulting a lawyer is not the statutory phrasing.", "C": "Illiteracy is not an exception protecting the representation.", "D": "Payment mode is irrelevant."},
    "Easy", "Indian Contract Act, 1872, Section 19 Exception", "Master ordinary diligence exception under Section 19."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-005", "ch-cnt-05", "top-cnt-05-01",
    "A sells a horse to B, stating that the horse is sound. A honestly believes the horse is sound from its appearance, though his veterinary doctor has not examined it. In fact, the horse has an internal defect. This is:",
    ["Fraud under Section 17", "Misrepresentation under Section 18(1)", "Mistake of law under Section 21", "A wagering contract"],
    1, "B",
    "Section 18(1): A positive assertion not warranted by information, of that which is not true, though believed to be true, is misrepresentation.",
    {"A": "Fraud requires absence of honest belief.", "B": "Correct. Unwarranted positive assertion without intent to deceive is misrepresentation.", "C": "Soundness of a horse is a matter of fact, not law.", "D": "No wager is involved."},
    "Medium", "Indian Contract Act, 1872, Section 18(1)", "Apply Section 18(1) unwarranted assertion."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-006", "ch-cnt-05", "top-cnt-05-01",
    "Does the Exception to Section 19 (means of discovering the truth with ordinary diligence) apply to cases of active fraud under Section 17?",
    ["Yes, it applies to all forms of fraud and misrepresentation equally", "No, it applies only to misrepresentation and to fraudulent silence, not to active positive fraud", "Yes, but only in commercial sale of goods", "Only where the fraud is committed by a bank"],
    1, "B",
    "In Kamaldas v. R.M.K.R.M. Firm and leading commentaries, the Exception to Section 19 applies to misrepresentation and fraudulent silence, not to active fraud or fraudulent misstatements.",
    {"A": "Active fraud cannot be excused by saying the victim was gullible or could have discovered it.", "B": "Correct. Active fraud is not barred by the ordinary diligence exception.", "C": "Commercial contracts enjoy no special exception for active fraud.", "D": "Bank fraud is governed by identical general principles."},
    "Hard", "Indian Contract Act, 1872, Section 19 Exception", "Analyze limits of ordinary diligence exception in active fraud."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-007", "ch-cnt-05", "top-cnt-05-01",
    "Under Section 18(2), what type of conduct constitutes misrepresentation?",
    ["Any breach of duty which, without intent to deceive, gains an advantage to the person committing it by misleading another to his prejudice", "An intentional forgery of a promissory note", "Criminal breach of trust under BNS", "Bribery of an arbitrator"],
    0, "A",
    "Section 18(2) covers constructive fraud/innocent breach of duty: breach of duty without intent to deceive gaining an advantage to the person committing it.",
    {"A": "Correct. Section 18(2) textually defines breach of duty without deceit.", "B": "Forgery is criminal and fraudulent.", "C": "Criminal breach of trust is a crime, not innocent misrepresentation.", "D": "Bribery is illegal under Section 23."},
    "Medium", "Indian Contract Act, 1872, Section 18(2)", "Identify constructive misrepresentation under Section 18(2)."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-008", "ch-cnt-05", "top-cnt-05-01",
    "Under Section 19 Explanation, a fraud or misrepresentation which did NOT cause the consent to a contract of the party on whom such fraud was practiced:",
    ["Does not render a contract voidable", "Renders the contract void ab initio", "Entitles the party to triple damages", "Makes the contract illegal under Section 23"],
    0, "A",
    "Explanation to Section 19: 'A fraud or misrepresentation which did not cause the consent to a contract of the party on whom such fraud was practised, or to whom such misrepresentation was made, does not render a contract voidable'.",
    {"A": "Correct. The fraud or misrepresentation must have actually induced/caused the consent.", "B": "It does not render the contract void ab initio.", "C": "No damages lie for deceit that did not induce action.", "D": "It does not make the agreement illegal."},
    "Medium", "Indian Contract Act, 1872, Section 19 Explanation", "Understand inducement requirement under Section 19."
))

# top-cnt-05-02: Mistake of Fact: Bilateral vs Unilateral Mistake (Sections 20, 22) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-05-009", "ch-cnt-05", "top-cnt-05-02",
    "Under Section 20 of the Indian Contract Act, where both the parties to an agreement are under a mistake as to a matter of fact essential to the agreement, the agreement is:",
    ["Voidable at the option of either party", "Void", "Valid and binding", "Unenforceable for 3 years"],
    1, "B",
    "Section 20 explicitly provides: 'Where both the parties to an agreement are under a mistake as to a matter of fact essential to the agreement, the agreement is void'.",
    {"A": "Bilateral mistake makes the agreement void, not merely voidable.", "B": "Correct. Section 20 declares bilateral mistake of essential fact void.", "C": "It is completely invalid for want of consensus.", "D": "No 3-year suspension rule exists."},
    "Easy", "Indian Contract Act, 1872, Section 20", "Recall legal effect of bilateral mistake under Section 20."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-010", "ch-cnt-05", "top-cnt-05-02",
    "Under the Explanation to Section 20 of the Indian Contract Act, an erroneous opinion as to the value of the thing which forms the subject-matter of the agreement is:",
    ["A bilateral mistake making the contract void", "NOT to be deemed a mistake as to a matter of fact essential to the agreement", "A fraud by the seller", "A ground for claiming treble damages"],
    1, "B",
    "Explanation to Section 20: 'An erroneous opinion as to the value of the thing which forms the subject-matter of the agreement, is not to be deemed a mistake as to a matter of fact'.",
    {"A": "Mistake as to value does not avoid a contract under Section 20.", "B": "Correct. Explanation to Section 20 expressly excludes mistake as to value.", "C": "Erroneous valuation is not fraud.", "D": "No damages can be claimed for bad valuation opinions."},
    "Medium", "Indian Contract Act, 1872, Section 20 Explanation", "Master mistake of value exception under Section 20."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-011", "ch-cnt-05", "top-cnt-05-02",
    "In Couturier v. Hastie (1856), a contract was made for the sale of a cargo of Indian corn believed to be on a voyage from Salonica to London. Unknown to both parties, the cargo had fermented and was sold at Tunis before the contract was made. The court held:",
    ["The buyer was liable to pay the price because he took the risk", "The contract was void ab initio for common mistake as to the existence of the subject matter (res extincta)", "The seller was liable in damages for non-delivery", "The captain of the ship was personally liable"],
    1, "B",
    "Under the doctrine of res extincta (Section 20 and Illustration (a)), if the subject matter has ceased to exist at the time of contract without knowledge of either party, the agreement is void.",
    {"A": "The buyer cannot be forced to pay for non-existent goods.", "B": "Correct. Contract is void for bilateral mistake as to existence of subject matter (res extincta).", "C": "No damages lie where both parties were innocently mistaken.", "D": "The captain was not a party to the sale contract."},
    "Medium", "House of Lords: Couturier v. Hastie (1856) 5 HLC 673", "Apply doctrine of res extincta in Couturier v Hastie."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-012", "ch-cnt-05", "top-cnt-05-02",
    "In Cooper v. Phibbs (1867), A agreed to take a lease of a fishery from B. Unknown to both parties, the fishery already belonged to A as tenant in tail. The House of Lords held:",
    ["The lease was valid and A must pay rent to B", "The agreement was void for common mistake as to title (res sua)", "B was guilty of fraud and liable to imprisonment", "A had forfeited his title by signing the lease"],
    1, "B",
    "Under the doctrine of res sua (Illustration to Section 20), an agreement to buy or lease property which already belongs to the purchaser/lessee is void for mutual mistake.",
    {"A": "One cannot lease or buy one's own property.", "B": "Correct. Contract is void for common mistake of title (res sua).", "C": "B acted in good faith; no fraud was committed.", "D": "Signing a mistaken lease does not forfeit existing lawful title."},
    "Hard", "House of Lords: Cooper v. Phibbs (1867) LR 2 HL 149", "Apply doctrine of res sua in Cooper v Phibbs."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-013", "ch-cnt-05", "top-cnt-05-02",
    "Under Section 22 of the Indian Contract Act, a contract is NOT voidable merely because it was caused by one of the parties to it being under a mistake as to a matter of fact. This is the rule of:",
    ["Bilateral mistake", "Unilateral mistake", "Common mistake", "Mutual cross-purpose mistake"],
    1, "B",
    "Section 22 provides that unilateral mistake (mistake of one party alone) does not render a contract void or voidable, subject to narrow exceptions like mistake as to identity.",
    {"A": "Bilateral mistake makes contract void under Section 20.", "B": "Correct. Section 22 governs unilateral mistake, leaving the contract valid.", "C": "Common mistake is bilateral under Section 20.", "D": "Mutual cross-purpose mistake prevents consensus under Section 13."},
    "Easy", "Indian Contract Act, 1872, Section 22", "Recall statutory rule on unilateral mistake under Section 22."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-014", "ch-cnt-05", "top-cnt-05-02",
    "In Cundy v. Lindsay (1878), a rogue named Blenkarn ordered goods from Lindsay by imitating the signature of a reputable firm 'Blenkiron & Co.'. Blenkarn sold the goods to innocent purchaser Cundy. The House of Lords held:",
    ["Lindsay intended to contract with Blenkiron; there was no contract with Blenkarn, so property never passed and Cundy was liable for conversion", "Cundy acquired good title as an innocent purchaser for value", "The contract was voidable and Cundy was protected", "Lindsay was estopped by his own negligence"],
    0, "A",
    "In Cundy v. Lindsay, the mistake was as to the identity of the contracting party (written contract). The contract was void ab initio, and even a bona fide purchaser got no title.",
    {"A": "Correct. Mistake as to identity in written dealings makes contract void ab initio.", "B": "Nemo dat quod non habet: a rogue with no title can convey no title to Cundy.", "C": "It was void, not voidable.", "D": "Lindsay was held not negligent so as to create estoppel."},
    "Hard", "House of Lords: Cundy v. Lindsay (1878) 3 App Cas 459", "Master mistake of identity in Cundy v Lindsay."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-015", "ch-cnt-05", "top-cnt-05-02",
    "In Phillips v. Brooks (1919) and Lewis v. Averay (1972), where parties contract face-to-face (inter praesentes), and a rogue misrepresents his identity/creditworthiness:",
    ["The contract is void ab initio in all cases", "The contract is presumed voidable for fraud, not void for mistake of identity, so a bona fide third-party purchaser acquires good title before rescission", "No property passes to anyone", "The transaction is an illegal bailment"],
    1, "B",
    "In face-to-face transactions, the law presumes an intention to deal with the person physically present. The contract is voidable for fraud, not void for mistake, protecting bona fide buyers.",
    {"A": "Face-to-face contracts are presumed voidable, not void ab initio.", "B": "Correct. Inter praesentes dealings create a voidable contract protecting third-party buyers.", "C": "Property passes to rogue subject to right of avoidance.", "D": "It is a contract of sale, not bailment."},
    "Hard", "Lewis v. Averay (1972) 1 QB 198; Phillips v. Brooks (1919) 2 KB 243", "Distinguish face-to-face mistake of identity from written dealings."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-016", "ch-cnt-05", "top-cnt-05-02",
    "Under Section 65 of the Indian Contract Act, when an agreement is discovered to be void (such as on grounds of bilateral mistake under Section 20):",
    ["Any person who has received any advantage under such agreement is bound to restore it, or to make compensation for it, to the person from whom he received it", "The party in possession may keep all benefits without compensation", "Both parties are punished with civil imprisonment", "The property reverts to the village panchayat"],
    0, "A",
    "Section 65 codifies the doctrine of restitution: when an agreement is discovered to be void, any person who received advantage is bound to restore it or make compensation.",
    {"A": "Correct. Section 65 requires restitution of advantages upon discovery of voidness.", "B": "Unjust retention of advantages is forbidden by Section 65.", "C": "No civil imprisonment is awarded under Section 65.", "D": "Restitution is to the person from whom advantage was received, not panchayat."},
    "Medium", "Indian Contract Act, 1872, Section 65", "Apply Section 65 restitution to agreements discovered void."
))

# top-cnt-05-03: Mistake of Law: Indian Law vs Foreign Law (Section 21) (8 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-05-017", "ch-cnt-05", "top-cnt-05-03",
    "Under Section 21 paragraph 1 of the Indian Contract Act, a contract is NOT voidable because it was caused by a mistake as to any law in force in India. This is based on the maxim:",
    ["Ignorantia juris non excusat (Ignorance of law is no excuse)", "Caveat emptor (Buyer beware)", "Res ipsa loquitur (Thing speaks for itself)", "Nemo bis punitur pro eodem delicto"],
    0, "A",
    "Section 21: A mistake of Indian law does not avoid a contract. Everyone is presumed to know the law of the land (ignorantia juris non excusat).",
    {"A": "Correct. Ignorantia juris non excusat is the foundation of Section 21 paragraph 1.", "B": "Caveat emptor applies to sale of goods.", "C": "Res ipsa loquitur is a rule of evidence in tort.", "D": "Nemo bis punitur is double jeopardy in criminal law."},
    "Easy", "Indian Contract Act, 1872, Section 21", "Recall maxim underlying Section 21 on mistake of law."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-018", "ch-cnt-05", "top-cnt-05-03",
    "Under Section 21 paragraph 2 of the Indian Contract Act, a mistake as to a law NOT in force in India (i.e. foreign law) has the same effect as a:",
    ["Mistake of Indian criminal law", "Mistake of fact", "Ground for contempt of court", "Voidable transaction under Section 19"],
    1, "B",
    "Section 21 paragraph 2: 'A mistake as to a law not in force in India has the same effect as a mistake of fact' (and may render agreement void under Section 20 if bilateral).",
    {"A": "Foreign law is treated as fact, not Indian criminal law.", "B": "Correct. Foreign law is treated as a matter of fact under Section 21.", "C": "Foreign law mistake carries no contempt consequences.", "D": "It is governed by Section 20 (void if bilateral) rather than Section 19."},
    "Medium", "Indian Contract Act, 1872, Section 21 Paragraph 2", "Identify legal status of foreign law mistake under Section 21."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-019", "ch-cnt-05", "top-cnt-05-03",
    "In Shiba Prasad Singh v. Maharaja Srish Chandra Nandi (AIR 1949 PC 297), the Privy Council held that under Section 72 of the Indian Contract Act, money paid under a mistake of law:",
    ["Can never be recovered under any circumstance", "Can be recovered back, because Section 72 uses the word 'mistake' without qualification", "Can only be recovered if the payee is a bank", "Is forfeited to the provincial government"],
    1, "B",
    "The Privy Council held that Section 72 ('money paid... by mistake') applies to mistake of law as well as mistake of fact; money paid under mistake of law is recoverable.",
    {"A": "The old English rule barring recovery of money paid under mistake of law does not apply under Section 72.", "B": "Correct. Shiba Prasad Singh settled that money paid under mistake of law is recoverable under Section 72.", "C": "Payee identity does not restrict Section 72.", "D": "No forfeiture to government applies."},
    "Hard", "Privy Council: Shiba Prasad Singh v. Srish Chandra Nandi (AIR 1949 PC 297)", "Master Shiba Prasad Singh on recovery of money paid under mistake of law."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-020", "ch-cnt-05", "top-cnt-05-03",
    "In Sales Tax Officer, Banaras v. Kanhaiya Lal Saraf (AIR 1959 SC 135), the Constitution Bench of the Supreme Court held that sales tax paid under a provision subsequently declared unconstitutional:",
    ["Cannot be refunded because the citizen is presumed to know the law", "Must be refunded by the State under Section 72 as money paid under mistake of law", "Can only be adjusted against future liabilities across 20 years", "Is a valid voluntary contribution to the treasury"],
    1, "B",
    "The Supreme Court affirmed Shiba Prasad Singh and held that taxes paid under an ultra vires statute are money paid under mistake of law recoverable under Section 72.",
    {"A": "The Supreme Court rejected the State's defense of ignorantia juris.", "B": "Correct. Kanhaiya Lal Saraf established State's obligation to refund tax paid under mistake of law.", "C": "No 20-year adjustment rule was ordered.", "D": "Taxes paid under unconstitutional statutes cannot be treated as voluntary donations."},
    "Hard", "Supreme Court: STO Banaras v. Kanhaiya Lal Saraf (AIR 1959 SC 135)", "Apply Kanhaiya Lal Saraf to tax paid under mistake of law."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-021", "ch-cnt-05", "top-cnt-05-03",
    "Under Section 21, Illustration: A and B make a contract grounded on the erroneous belief that a particular debt is barred by the Indian Law of Limitation. The contract is:",
    ["Void ab initio", "Not voidable", "Voidable at the option of the debtor", "Illegal under Section 23"],
    1, "B",
    "Illustration to Section 21 explicitly states: 'A and B make a contract grounded on the erroneous belief that a particular debt is barred by the Indian Law of Limitation: the contract is not voidable'.",
    {"A": "Mistake of Indian law does not make contract void.", "B": "Correct. Exactly matches the Illustration to Section 21: contract is not voidable.", "C": "Debtor cannot avoid on ground of ignorance of limitation law.", "D": "It is completely legal and binding."},
    "Medium", "Indian Contract Act, 1872, Section 21 Illustration", "Apply Section 21 Illustration on limitation law mistake."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-022", "ch-cnt-05", "top-cnt-05-03",
    "What is the harmonized relationship between Section 21 (contract not voidable for mistake of Indian law) and Section 72 (money paid under mistake recoverable)?",
    ["Section 72 is invalid and subordinated to Section 21", "Section 21 applies to enforceability of executory contracts; Section 72 applies to restitution of payments already made without legal liability", "Both sections mean identical things and contradict each other", "Section 21 applies only to criminal cases"],
    1, "B",
    "As explained in Kanhaiya Lal Saraf, Section 21 prevents avoidance of contracts, whereas Section 72 deals with quasi-contractual restitution of money paid where no contract or obligation existed.",
    {"A": "Neither section is invalid; both are statutory provisions.", "B": "Correct. Section 21 governs contract avoidance; Section 72 governs restitution of unjust retention.", "C": "No statutory contradiction; they govern distinct operational spheres.", "D": "Both are civil contract law provisions."},
    "Hard", "Supreme Court: Kanhaiya Lal Saraf & Section 72 Jurisprudence", "Harmonize Section 21 and Section 72."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-023", "ch-cnt-05", "top-cnt-05-03",
    "A mistake as to a private right of ownership or property, though involving legal principles, is treated in contract law as a:",
    ["Mistake of general Indian public law under Section 21", "Mistake of fact under Section 20", "Statutory fraud", "Waiver of fundamental right"],
    1, "B",
    "Under Cooper v. Phibbs (Lord Westbury), private right of ownership is a matter of fact, although arising from rules of law; mistake as to private title is treated as mistake of fact.",
    {"A": "General public law is distinguished from private property rights.", "B": "Correct. Mistake as to private title is treated as a mistake of fact under Section 20.", "C": "Ignorance of private title is not fraud.", "D": "Fundamental rights cannot be waived, but private title mistake is a civil matter."},
    "Hard", "House of Lords: Cooper v. Phibbs (1867) LR 2 HL 149", "Classify mistake of private right of ownership."
))
mcqs.append(make_mcq(
    "mcq-cnt-05-024", "ch-cnt-05", "top-cnt-05-03",
    "If an Indian merchant and an American company enter into an agreement in Mumbai under a mutual mistaken belief regarding US import tariff laws, the agreement is:",
    ["Valid and not voidable under Section 21 paragraph 1", "Void under Section 20, because mistake of foreign law is treated as a mistake of fact", "Voidable at the option of the US company alone", "Illegal under the Foreign Exchange Management Act"],
    1, "B",
    "Under Section 21 paragraph 2, a mistake of foreign law is treated as a mistake of fact. Because both parties were under this essential mistake, the agreement is void under Section 20.",
    {"A": "Section 21 paragraph 1 applies only to law in force in India.", "B": "Correct. Foreign law = fact; mutual mistake of essential fact = void under Section 20.", "C": "Bilateral mistake makes agreement void, not voidable.", "D": "Tariff misunderstanding is not an automatic FEMA violation."},
    "Hard", "Indian Contract Act, 1872, Sections 20, 21 Paragraph 2", "Synthesize Section 20 and Section 21(2) on foreign law."
))

# =========================================================================================
# CHAPTER 6: LEGALITY OF OBJECT AND CONSIDERATION & VOID AGREEMENTS (18 MCQs)
# =========================================================================================
# top-cnt-06-01: Unlawful Consideration & Public Policy Doctrine (Section 23) (9 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-06-001", "ch-cnt-06", "top-cnt-06-01",
    "Under Section 23 of the Indian Contract Act, the consideration or object of an agreement is lawful, unless:",
    ["It is forbidden by law, or is of such a nature that, if permitted, it would defeat the provisions of any law", "It is fraudulent, or involves or implies injury to the person or property of another", "The court regards it as immoral, or opposed to public policy", "All of the above"],
    3, "D",
    "Section 23 sets out five distinct grounds of unlawfulness: forbidden by law, defeating provisions of law, fraudulent, injury to person/property, or immoral/opposed to public policy.",
    {"A": "Forbidden by law or defeating provisions is clause 1 & 2.", "B": "Fraudulent or injury to person/property is clause 3 & 4.", "C": "Immoral or opposed to public policy is clause 5.", "D": "Correct. All of the listed grounds render consideration or object unlawful under Section 23."},
    "Easy", "Indian Contract Act, 1872, Section 23", "Identify five heads of unlawful consideration under Section 23."
))
mcqs.append(make_mcq(
    "mcq-cnt-06-002", "ch-cnt-06", "top-cnt-06-01",
    "Under Section 23, an agreement whose consideration or object is unlawful is:",
    ["Voidable at the option of the innocent party", "Void", "Valid until challenged by the government", "Punishable with death penalty"],
    1, "B",
    "Section 23 explicitly concludes: 'Every agreement of which the object or consideration is unlawful is void'.",
    {"A": "Unlawful agreements are void ab initio, not merely voidable.", "B": "Correct. Section 23 explicitly declares unlawful agreements void.", "C": "It is a nullity from inception, needing no government challenge.", "D": "Contract law does not impose death penalties."},
    "Easy", "Indian Contract Act, 1872, Section 23", "Recall legal effect of unlawful consideration."
))
mcqs.append(make_mcq(
    "mcq-cnt-06-003", "ch-cnt-06", "top-cnt-06-01",
    "In Central Inland Water Transport Corporation v. Brojo Nath Ganguly (AIR 1986 SC 1571), a service rule empowering the employer to terminate permanent employees with 3 months' notice without assigning reasons was held:",
    ["Valid under freedom of contract", "Opposed to public policy and void under Section 23 as unconscionable, unfair, and unreasonable", "A valid liquidated damages clause under Section 74", "Enforceable only against managerial staff"],
    1, "B",
    "The Supreme Court held that unconscionable and grossly unequal bargaining terms are opposed to public policy under Section 23 and Article 14.",
    {"A": "Freedom of contract does not protect unconscionable standard contracts.", "B": "Correct. Landmark ruling holding unfair/unconscionable contracts void under Section 23 public policy.", "C": "It was an arbitrary termination clause, not liquidated damages.", "D": "It was struck down across the board for all permanent staff."},
    "Hard", "Supreme Court: Central Inland Water Transport Corp v. Brojo Nath Ganguly (AIR 1986 SC 1571)", "Master Brojo Nath Ganguly public policy doctrine."
))
mcqs.append(make_mcq(
    "mcq-cnt-06-004", "ch-cnt-06", "top-cnt-06-01",
    "Agreements stifling criminal prosecution (promising money to drop prosecution for a non-compoundable criminal offence) are:",
    ["Valid compromises encouraged by law", "Void as opposed to public policy under Section 23", "Enforceable with leave of the police inspector", "Valid quasi-contracts under Section 70"],
    1, "B",
    "Administration of justice requires criminals to be prosecuted. Dropping non-compoundable criminal charges for money is stifling prosecution and void under Section 23.",
    {"A": "Only legally compoundable offences under Section 320 CrPC can be compromised.", "B": "Correct. Stifling criminal prosecution is opposed to public policy and void.", "C": "Police officers cannot validate unlawful agreements.", "D": "Section 70 cannot enforce illegal or public policy violations."},
    "Medium", "Kamini Kumar Deb v. Birendra Nath Chuckerbutty (AIR 1930 PC 100)", "Analyze agreements stifling criminal prosecution."
))
mcqs.append(make_mcq(
    "mcq-cnt-06-005", "ch-cnt-06", "top-cnt-06-01",
    "In English law, 'maintenance' is assisting a party in litigation without lawful justification, and 'champerty' is assisting litigation in return for a share of proceeds. Under Indian law:",
    ["Maintenance and champerty are criminal offences in all cases", "Agreements to finance litigation for a share of proceeds are not per se void or illegal, unless extortionate, unconscionable, or motivated by improper gambling in litigation", "Champerty is completely prohibited by Section 23", "Litigation financing can only be done by banks"],
    1, "B",
    "In Ram Coomar Coondoo v. Chunder Canto Mookerjee (1876), the Privy Council established that English laws of maintenance and champerty do not apply in India; financing is valid unless extortionate.",
    {"A": "They were never criminal offences in India.", "B": "Correct. Valid in India unless unconscionable, extortionate, or for improper gambling in litigation.", "C": "Champerty is not per se void in Indian law.", "D": "Private individuals can advance litigation funds."},
    "Hard", "Privy Council: Ram Coomar Coondoo v. Chunder Canto Mookerjee (1876) 2 App Cas 186", "Distinguish Indian champerty rule from English law."
))
mcqs.append(make_mcq(
    "mcq-cnt-06-006", "ch-cnt-06", "top-cnt-06-01",
    "An agreement to pay money to a public servant to induce him to retire and secure a government job or public title for the promisor is:",
    ["A valid commercial transaction", "Void as opposed to public policy under Section 23 (trafficking in public offices)", "Enforceable under Section 25(2)", "A valid contingent contract"],
    1, "B",
    "Trafficking in public offices, appointments, or titles corrupts public administration and is strictly void under Section 23 as opposed to public policy.",
    {"A": "Public offices cannot be bought or sold.", "B": "Correct. Trafficking in public offices is void as opposed to public policy.", "C": "Section 25(2) cannot validate unlawful consideration.", "D": "Contingent contract requires lawful subject matter."},
    "Medium", "Indian Contract Act, 1872, Section 23", "Identify trafficking in public offices under Section 23."
))
mcqs.append(make_mcq(
    "mcq-cnt-06-007", "ch-cnt-06", "top-cnt-06-01",
    "Under Section 24 of the Indian Contract Act, if any part of a single consideration for one or more objects, or any one or any part of any one of several considerations for a single object, is unlawful:",
    ["The whole agreement is void", "Only the unlawful part is void, and lawful part is enforced", "The agreement is voidable", "The court will substitute fresh consideration"],
    0, "A",
    "Section 24: Where consideration is indivisible and partly unlawful, the whole agreement is void (if lawful and unlawful parts cannot be severed).",
    {"A": "Correct. Section 24 declares the agreement void where consideration is partly unlawful and inseparable.", "B": "Severability applies under Section 57/58, not under Section 24 inseparable consideration.", "C": "It is completely void, not voidable.", "D": "Courts cannot invent or rewrite consideration for parties."},
    "Medium", "Indian Contract Act, 1872, Section 24", "Master indivisible unlawful consideration under Section 24."
))
mcqs.append(make_mcq(
    "mcq-cnt-06-008", "ch-cnt-06", "top-cnt-06-01",
    "Under the maxim 'In pari delicto potior est conditio defendentis' (where both parties are equally at fault, the defendant is in the stronger position):",
    ["The court will assist the plaintiff to recover money paid under an executed illegal contract", "The court will refuse to assist either party and leave them where they stand", "The defendant is automatically convicted of a misdemeanor", "The plaintiff receives 50% refund from the state"],
    1, "B",
    "Where both parties are in equal guilt under an illegal contract, the court refuses its assistance to the plaintiff, leaving the property in the hands of the possessor/defendant.",
    {"A": "Courts do not enforce or aid executed illegal agreements.", "B": "Correct. The court declines assistance and maintains the status quo.", "C": "Civil maxim does not imply automatic criminal conviction.", "D": "No state refund mechanism exists."},
    "Hard", "Kedar Nath Motani v. Prahlad Rai (AIR 1960 SC 213)", "Explain in pari delicto maxim."
))
mcqs.append(make_mcq(
    "mcq-cnt-06-009", "ch-cnt-06", "top-cnt-06-01",
    "An agreement to let a house to a woman for the purpose of running a brothel is:",
    ["Valid if the rent is paid in advance", "Void as its object is immoral under Section 23", "Voidable at the landlord's discretion", "Enforceable under the Rent Control Act"],
    1, "B",
    "Under Section 23 and settled case law (e.g. Pearce v. Brooks, Chundun v. Soshila), letting premises for prostitution is immoral and void ab initio.",
    {"A": "Advance payment cannot legalize an immoral object.", "B": "Correct. Void for immoral object under Section 23.", "C": "It is completely void, not voidable.", "D": "Rent control acts do not protect immoral contracts."},
    "Easy", "Indian Contract Act, 1872, Section 23", "Apply immorality clause under Section 23."
))

# top-cnt-06-02: Specific Void Agreements: Restraint of Trade, Marriage & Wagering (Sections 26–30) (9 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-06-010", "ch-cnt-06", "top-cnt-06-02",
    "Under Section 26 of the Indian Contract Act, every agreement in restraint of the marriage of any person, other than a minor, is:",
    ["Voidable at the option of the bride", "Void", "Valid if reasonable", "Illegal under criminal law"],
    1, "B",
    "Section 26 explicitly provides: 'Every agreement in restraint of the marriage of any person, other than a minor, is void'.",
    {"A": "It is not voidable; it is void.", "B": "Correct. Section 26 declares restraint of marriage of any non-minor void.", "C": "Reasonableness test does not apply to Section 26; restraint is absolute.", "D": "It is a void civil agreement, not a criminal offence per se."},
    "Easy", "Indian Contract Act, 1872, Section 26", "Recall Section 26 rule on restraint of marriage."
))
mcqs.append(make_mcq(
    "mcq-cnt-06-011", "ch-cnt-06", "top-cnt-06-02",
    "Under Section 27 of the Indian Contract Act, every agreement by which anyone is restrained from exercising a lawful profession, trade, or business of any kind, is:",
    ["To that extent void", "Completely valid if the restraint is reasonable", "Voidable at the option of the employee", "Valid if approved by the Ministry of Commerce"],
    0, "A",
    "Section 27 states: 'Every agreement by which any one is restrained from exercising a lawful profession, trade or business of any kind, is to that extent void'.",
    {"A": "Correct. Section 27 invalidates restraints 'to that extent void'.", "B": "Under Indian law, unlike English law (Nordenfelt), general reasonableness cannot validate restraint of trade.", "C": "It is void, not voidable.", "D": "Ministry approval cannot override Section 27."},
    "Easy", "Indian Contract Act, 1872, Section 27", "Identify statutory rule on restraint of trade under Section 27."
))
mcqs.append(make_mcq(
    "mcq-cnt-06-012", "ch-cnt-06", "top-cnt-06-02",
    "What is the sole statutory Exception recognized in Section 27 of the Indian Contract Act?",
    ["Restraint on employees after termination of employment", "Sale of goodwill of a business (reasonable local limits)", "Partnership agreements in perpetuity", "Exclusive dealing agreements for 20 years"],
    1, "B",
    "The sole statutory Exception to Section 27 validates an agreement not to carry on a similar business within specified local limits upon sale of goodwill, provided the limits appear reasonable.",
    {"A": "Post-employment restraints are void under Indian law (Niranjan Shankar Golikari).", "B": "Correct. Sale of goodwill is the only statutory Exception to Section 27.", "C": "Partnership restraints are governed by Partnership Act Sections 11, 36, 54.", "D": "Exclusive dealing is not an express statutory Exception under Section 27."},
    "Medium", "Indian Contract Act, 1872, Section 27 Exception", "Identify sole statutory exception to Section 27."
))
mcqs.append(make_mcq(
    "mcq-cnt-06-013", "ch-cnt-06", "top-cnt-06-02",
    "In Niranjan Shankar Golikari v. Century Spinning & Mfg. Co. (AIR 1967 SC 1098), the Supreme Court held that a negative covenant restraining an employee during the period of employment:",
    ["Is void under Section 27 as a restraint of trade", "Is valid and does not attract Section 27, because it operates during the term of employment to ensure exclusive service", "Is an offence under the Trade Unions Act", "Is enforceable only against foreign technicians"],
    1, "B",
    "The Supreme Court held that negative covenants operating during the subsistence of an employment contract are valid, whereas post-termination restraints are void under Section 27.",
    {"A": "Restraint during employment is not hit by Section 27.", "B": "Correct. Negative covenant during service is valid; post-employment restraint is void.", "C": "It is not a trade union offence.", "D": "Applies uniformly to all employees."},
    "Hard", "Supreme Court: Niranjan Shankar Golikari v. Century Spinning (AIR 1967 SC 1098)", "Master Golikari doctrine on negative covenants during employment."
))
mcqs.append(make_mcq(
    "mcq-cnt-06-014", "ch-cnt-06", "top-cnt-06-02",
    "In Superintendence Company of India v. Krishan Murgai (AIR 1980 SC 1717), a post-service covenant prohibiting an employee from serving a competitor for 2 years after leaving service was held:",
    ["Valid because 2 years is a reasonable duration", "Void under Section 27, because the doctrine of reasonableness does not apply to post-service restraints under Section 27", "A valid trade secret covenant", "Enforceable with 50% salary compensation"],
    1, "B",
    "The Supreme Court ruled that under Section 27, all post-termination restraints of trade are void ab initio; English common law reasonableness test (Nordenfelt) has no application in India.",
    {"A": "Reasonableness cannot save a post-employment restraint under Indian law.", "B": "Correct. Krishan Murgai settled that all post-service employee restraints are void under Section 27.", "C": "Trade secret protection cannot justify general employment prohibition.", "D": "Paying compensation does not validate a void restraint."},
    "Hard", "Supreme Court: Superintendence Co v. Krishan Murgai (AIR 1980 SC 1717)", "Apply Krishan Murgai ruling on post-employment restraint."
))
mcqs.append(make_mcq(
    "mcq-cnt-06-015", "ch-cnt-06", "top-cnt-06-02",
    "Under Section 28 of the Indian Contract Act (as amended in 1997), which of the following agreements is void?",
    ["Every agreement by which any party is restricted absolutely from enforcing his rights under or in respect of any contract by usual legal proceedings", "Every agreement which extinguishes the rights of any party or discharges any party from liability on the expiry of a specified period so as to restrict the period of limitation", "Both A and B", "Neither A nor B"],
    2, "C",
    "Section 28 invalidates agreements restricting legal proceedings (clause a) and agreements curtailing limitation periods or extinguishing rights on expiry of specified periods (clause b).",
    {"A": "Clause (a) invalidates absolute restrictions on court access.", "B": "Clause (b) (added in 1997) invalidates contractual curtailment of limitation.", "C": "Correct. Both clauses (a) and (b) are statutory grounds of voidness under Section 28.", "D": "Incorrect as both are explicit statutory clauses."},
    "Medium", "Indian Contract Act, 1872, Section 28", "Identify scope of Section 28 on legal proceedings."
))
mcqs.append(make_mcq(
    "mcq-cnt-06-016", "ch-cnt-06", "top-cnt-06-02",
    "Does an arbitration clause referring future disputes to arbitration violate Section 28 of the Indian Contract Act?",
    ["Yes, all arbitration agreements are void under Section 28", "No, Exception 1 to Section 28 expressly saves contracts to refer to arbitration disputes that may arise", "Only if the arbitrator is a sitting High Court Judge", "Only in international commercial contracts"],
    1, "B",
    "Exception 1 to Section 28 expressly provides that contracts referring existing or future disputes to arbitration are not rendered illegal or void.",
    {"A": "Arbitration is expressly protected by statute.", "B": "Correct. Exception 1 to Section 28 expressly saves arbitration agreements.", "C": "Arbitrators can be any competent individuals.", "D": "Applies to both domestic and international arbitration."},
    "Easy", "Indian Contract Act, 1872, Section 28 Exception 1", "Recall arbitration exception under Section 28."
))
mcqs.append(make_mcq(
    "mcq-cnt-06-017", "ch-cnt-06", "top-cnt-06-02",
    "Under Section 29 of the Indian Contract Act, agreements, the meaning of which is not certain, or capable of being made certain, are:",
    ["Voidable", "Void", "Valid if registered", "Enforceable by an arbitrator"],
    1, "B",
    "Section 29 states: 'Agreements, the meaning of which is not certain, or capable of being made certain, are void'. (Certum est quod certum reddi potest).",
    {"A": "Uncertainty makes an agreement void, not voidable.", "B": "Correct. Section 29 declares uncertain agreements void.", "C": "Registration cannot supply certainty to meaningless terms.", "D": "Arbitrators cannot make an uncertain contract certain if basic intent is missing."},
    "Easy", "Indian Contract Act, 1872, Section 29", "Identify void agreements for uncertainty under Section 29."
))
mcqs.append(make_mcq(
    "mcq-cnt-06-018", "ch-cnt-06", "top-cnt-06-02",
    "Under Section 30 of the Indian Contract Act, agreements by way of wager are void. In Gherulal Parakh v. Mahadeodas Maiya (AIR 1959 SC 781), the Supreme Court held that in India (outside Maharashtra/Gujarat):",
    ["Wagering agreements are illegal and transactions collateral to a wager are also void", "Wagering agreements are void but NOT illegal, so a collateral agreement to a wager is valid and enforceable", "Wagering agreements are valid commercial options", "A partnership in wagering contracts is punishable under BNS"],
    1, "B",
    "The Supreme Court held in Gherulal Parakh that wagers are void under Section 30, but not forbidden by law/illegal under Section 23; therefore, transactions collateral to a wager are enforceable.",
    {"A": "Collateral transactions to wagers are void in England and Maharashtra/Gujarat by local statute, but not under general Indian law.", "B": "Correct. Wagers are void, not illegal; collateral agreements remain enforceable.", "C": "Wagers are void under Section 30.", "D": "No general BNS criminalization outside gambling enactments."},
    "Hard", "Supreme Court: Gherulal Parakh v. Mahadeodas Maiya (AIR 1959 SC 781)", "Master Gherulal Parakh on collateral agreements to wagers."
))

# =========================================================================================
# CHAPTER 7: CONTINGENT CONTRACTS & QUASI-CONTRACTS (18 MCQs)
# =========================================================================================
# top-cnt-07-01: Contingent Contracts: Meaning, Rules & Enforcement (Sections 31–36) (9 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-07-001", "ch-cnt-07", "top-cnt-07-01",
    "Under Section 31 of the Indian Contract Act, a 'contingent contract' is defined as a contract to do or not to do something, if:",
    ["Some event, collateral to such contract, does or does not happen", "Both parties agree to do illegal acts", "A third party pays double consideration", "The High Court approves the contract"],
    0, "A",
    "Section 31 defines contingent contract: 'a contract to do or not to do something, if some event, collateral to such contract, does or does not happen'.",
    {"A": "Correct. Verbatim definition under Section 31.", "B": "Contingent contract requires lawful consideration and collateral event.", "C": "Third-party payment is not the defining criterion.", "D": "High Court approval is not required."},
    "Easy", "Indian Contract Act, 1872, Section 31", "Recall statutory definition of contingent contract."
))
mcqs.append(make_mcq(
    "mcq-cnt-07-002", "ch-cnt-07", "top-cnt-07-01",
    "Which of the following is a classic example of a contingent contract under Section 31?",
    ["A contract of fire, marine, or life insurance", "A contract of guarantee", "A contract of indemnity", "All of the above"],
    3, "D",
    "Contracts of insurance, guarantee, and indemnity are all contingent contracts because performance depends upon the happening of a collateral event (loss, default, or damage).",
    {"A": "Insurance depends on fire, shipwreck, or death.", "B": "Guarantee depends on default of principal debtor.", "C": "Indemnity depends on loss caused by conduct.", "D": "Correct. All of these contracts are classic contingent contracts."},
    "Easy", "Indian Contract Act, 1872, Section 31", "Identify standard classes of contingent contracts."
))
mcqs.append(make_mcq(
    "mcq-cnt-07-003", "ch-cnt-07", "top-cnt-07-01",
    "What is the fundamental difference between a 'contingent contract' (Section 31) and a 'wagering agreement' (Section 30)?",
    ["A contingent contract is valid and parties have an insurable interest in the collateral event; a wager is void and parties have no interest other than the stake", "A wager is valid and enforceable, while a contingent contract is void", "Both are completely void in all cases", "There is no legal difference between them"],
    0, "A",
    "In a wager, the uncertain event is the sole determination of money won or lost (parties have no real interest). In a contingent contract, the event is collateral and parties have a legitimate interest.",
    {"A": "Correct. Contingent contracts are valid with real interest; wagers are void with interest only in the stake.", "B": "Reversed; legally inaccurate.", "C": "Contingent contracts are fully valid and enforceable.", "D": "They are fundamentally different legal concepts."},
    "Medium", "Indian Contract Act, 1872, Sections 30, 31", "Distinguish contingent contract from wagering agreement."
))
mcqs.append(make_mcq(
    "mcq-cnt-07-004", "ch-cnt-07", "top-cnt-07-01",
    "Under Section 32 of the Indian Contract Act, contingent contracts to do or not to do anything if an uncertain future event happens:",
    ["Can be enforced before the event happens with leave of court", "Cannot be enforced by law unless and until that event has happened; and if the event becomes impossible, such contracts become void", "Are void ab initio from inception", "Can only be performed by legal heirs"],
    1, "B",
    "Section 32: Contingent contracts dependent on an event happening cannot be enforced until it happens; if the event becomes impossible, the contract becomes void.",
    {"A": "Courts cannot enforce before the contingency occurs.", "B": "Correct. Enforceable only when event happens; becomes void if event becomes impossible.", "C": "They are valid conditional contracts, not void ab initio.", "D": "Performance is by the promisor unless personal skill is absent."},
    "Easy", "Indian Contract Act, 1872, Section 32", "Recall enforcement rule under Section 32."
))
mcqs.append(make_mcq(
    "mcq-cnt-07-005", "ch-cnt-07", "top-cnt-07-01",
    "Under Section 33 of the Indian Contract Act, contingent contracts to do or not to do anything if an uncertain future event does NOT happen can be enforced:",
    ["When the happening of that event becomes impossible, and not before", "Immediately upon execution of the deed", "Only within 14 days of execution", "Whenever the promisor pleases"],
    0, "A",
    "Section 33: Contracts contingent on an event not happening can be enforced when the happening of that event becomes impossible, and not before.",
    {"A": "Correct. Enforcement arises when the negative contingency is verified by impossibility of the event.", "B": "Cannot be enforced immediately while event might still happen.", "C": "No 14-day statutory rule exists.", "D": "Enforceability is governed by law, not promisor's whim."},
    "Medium", "Indian Contract Act, 1872, Section 33", "Identify enforcement of negative contingent contract under Section 33."
))
mcqs.append(make_mcq(
    "mcq-cnt-07-006", "ch-cnt-07", "top-cnt-07-01",
    "Under Section 34 of the Indian Contract Act, if the future event on which a contract is contingent is the way in which a person will act at an unspecified time, the event shall be considered to have become impossible when:",
    ["Such person dies or does anything which renders it impossible that he should so act within any definite time", "Such person attains 60 years of age", "Such person files for insolvency", "The promisor revokes the offer"],
    0, "A",
    "Section 34: Event is deemed impossible when the person does anything rendering it impossible to act so (e.g. A agrees to pay B if B marries C; C marries D, rendering marriage to B impossible).",
    {"A": "Correct. Matches Section 34 and its Illustration: act rendering event impossible.", "B": "Age 60 is not a statutory impossibility threshold.", "C": "Insolvency does not necessarily make marriage or personal acts impossible.", "D": "Revocation cannot occur after contract is formed."},
    "Medium", "Indian Contract Act, 1872, Section 34", "Apply Section 34 on human conduct contingency."
))
mcqs.append(make_mcq(
    "mcq-cnt-07-007", "ch-cnt-07", "top-cnt-07-01",
    "Under Section 35 of the Indian Contract Act, contingent contracts to do or not to do anything if a specified uncertain event happens within a fixed time become void if:",
    ["At the expiration of the time fixed, such event has not happened, or if, before the time fixed, such event becomes impossible", "The market price fluctuates by 5%", "The parties fail to meet monthly", "The contract is not registered"],
    0, "A",
    "Section 35: Contracts contingent on specified event within fixed time become void if time expires without happening, or if before time expires the event becomes impossible.",
    {"A": "Correct. Section 35 fixes expiration of time or prior impossibility as terminating events.", "B": "Price fluctuations do not void contingent contracts.", "C": "Monthly meetings are not statutory requirements.", "D": "Registration is not universally required."},
    "Medium", "Indian Contract Act, 1872, Section 35", "Master fixed-time contingent contracts under Section 35."
))
mcqs.append(make_mcq(
    "mcq-cnt-07-008", "ch-cnt-07", "top-cnt-07-01",
    "Under Section 36 of the Indian Contract Act, contingent agreements to do or not to do anything, if an impossible event happens, are:",
    ["Voidable at the option of the promisee", "Void, whether the impossibility of the event was known or not to the parties to the agreement at the time when it was made", "Valid if ratified by an affidavit", "Enforceable on quantum meruit"],
    1, "B",
    "Section 36: 'Contingent agreements to do or not to do anything, if an impossible event happens, are void, whether the impossibility of the event was known or not to the parties...'.",
    {"A": "Agreement is void ab initio, not voidable.", "B": "Correct. Section 36 declares agreements contingent on impossible events void ab initio.", "C": "Affidavits cannot validate an impossible agreement.", "D": "Quantum meruit does not arise on impossible void agreements."},
    "Easy", "Indian Contract Act, 1872, Section 36", "Identify agreements contingent on impossible events under Section 36."
))
mcqs.append(make_mcq(
    "mcq-cnt-07-009", "ch-cnt-07", "top-cnt-07-01",
    "A agrees to pay B Rs 1,000 if two straight lines should enclose a space. Under Section 36, the agreement is:",
    ["Void", "Valid", "Voidable", "A valid conditional gift"],
    0, "A",
    "Illustration (a) to Section 36: An agreement contingent on an impossible event (two straight lines enclosing a space) is void.",
    {"A": "Correct. Matches Illustration (a) to Section 36 verbatim: void ab initio.", "B": "Geometrical impossibility makes it completely void.", "C": "It is not voidable.", "D": "It is not a valid gift."},
    "Easy", "Indian Contract Act, 1872, Section 36 Illustration (a)", "Apply Section 36 geometrical impossibility illustration."
))

# top-cnt-07-02: Quasi-Contracts & Doctrine of Unjust Enrichment (Sections 68–72) (9 MCQs)
mcqs.append(make_mcq(
    "mcq-cnt-07-010", "ch-cnt-07", "top-cnt-07-02",
    "Under Chapter V of the Indian Contract Act (Sections 68–72), quasi-contracts are statutorily described as:",
    ["Implied commercial partnerships", "Certain relations resembling those created by contract", "Contracts under seal", "Equitable mortgages"],
    1, "B",
    "The heading of Chapter V is: 'Of Certain Relations Resembling Those Created by Contract'. Indian law avoids the fiction of 'implied contract' and grounds liability on unjust enrichment.",
    {"A": "They are not partnerships.", "B": "Correct. Statutory chapter heading of Sections 68-72.", "C": "Contracts under seal are English deeds, not quasi-contracts.", "D": "Equitable mortgage is a property concept under TPA Section 58(f)."},
    "Easy", "Indian Contract Act, 1872, Chapter V Heading", "Recall statutory title of quasi-contracts in Chapter V."
))
mcqs.append(make_mcq(
    "mcq-cnt-07-011", "ch-cnt-07", "top-cnt-07-02",
    "In Moses v. Macferlan (1760), Lord Mansfield founded quasi-contractual obligations on the principle of:",
    ["Consensus ad idem", "Natural justice and equity to prevent unjust enrichment (nemo debet locupletari ex aliena jactura)", "Promissory estoppel", "Vicarious responsibility"],
    1, "B",
    "Lord Mansfield held that the action for money had and received lies on the ties of natural justice and equity, wherever defendant received money which ex aequo et bono belongs to plaintiff.",
    {"A": "Quasi-contracts arise precisely where consensus ad idem is absent.", "B": "Correct. Lord Mansfield founded quasi-contract on equity to prevent unjust enrichment.", "C": "Promissory estoppel arose much later in Central London Property v. High Trees.", "D": "Vicarious responsibility is a tort doctrine."},
    "Medium", "Moses v. Macferlan (1760) 2 Burr 1005", "Master Lord Mansfield unjust enrichment doctrine."
))
mcqs.append(make_mcq(
    "mcq-cnt-07-012", "ch-cnt-07", "top-cnt-07-02",
    "Under Section 69 of the Indian Contract Act, a person who is interested in the payment of money which another is bound by law to pay, and who therefore pays it:",
    ["Is entitled to be reimbursed by the other", "Cannot recover because he made a voluntary payment", "Must obtain prior written permission from the High Court", "Is guilty of champerty"],
    0, "A",
    "Section 69: A person interested in the payment of money which another is bound by law to pay, and who therefore pays it, is entitled to be reimbursed by the other.",
    {"A": "Correct. Section 69 provides statutory right of reimbursement.", "B": "Payment is not officious volunteer payment because payer was legally interested.", "C": "No prior judicial sanction is required.", "D": "Paying lawful debts to protect one's interest is not champerty."},
    "Easy", "Indian Contract Act, 1872, Section 69", "Recall Section 69 reimbursement rule."
))
mcqs.append(make_mcq(
    "mcq-cnt-07-013", "ch-cnt-07", "top-cnt-07-02",
    "In Brook's Wharf & Bull Wharf Ltd. v. Goodman Bros (1937), warehousemen paid customs duty on imported goods which the owners were legally bound to pay, to prevent seizure of goods. The court held:",
    ["The warehousemen made an officious payment and could not recover", "The warehousemen were interested in payment and entitled to reimbursement from the owners under quasi-contract", "The customs authorities had to refund the money to the warehousemen", "The contract was void for illegality"],
    1, "B",
    "The English Court of Appeal held that warehousemen were entitled to recover the customs duty from the owners on unjust enrichment principles (corresponding to Section 69).",
    {"A": "Warehousemen had lawful interest in protecting their warehouse from customs seizure.", "B": "Correct. Leading case on reimbursement of money paid by interested party.", "C": "Customs duty was lawfully due and retained by revenue.", "D": "The transaction was completely lawful."},
    "Medium", "Brook's Wharf v. Goodman Bros (1937) 1 KB 534", "Apply reimbursement rule in Brook's Wharf case."
))
mcqs.append(make_mcq(
    "mcq-cnt-07-014", "ch-cnt-07", "top-cnt-07-02",
    "Under Section 70 of the Indian Contract Act, where a person lawfully does anything for another person, or delivers anything to him, not intending to do so gratuitously, and such other person enjoys the benefit thereof:",
    ["The latter is bound to make compensation to the former in respect of, or to restore, the thing so done or delivered", "The former has no claim unless a written contract existed", "The transaction is treated as a completed gift under Section 25", "The court will order criminal attachment of property"],
    0, "A",
    "Section 70 codifies three conditions: (1) lawful act/delivery, (2) not intending to act gratuitously, (3) enjoyment of benefit by the other person. Obligation is to compensate or restore.",
    {"A": "Correct. Section 70 mandates compensation or restoration of enjoyed benefits.", "B": "Section 70 applies precisely where there is no valid express contract.", "C": "Non-gratuitous intention precludes treatment as a gift.", "D": "It is a civil quasi-contractual remedy, not criminal attachment."},
    "Easy", "Indian Contract Act, 1872, Section 70", "Identify essentials of Section 70 non-gratuitous acts."
))
mcqs.append(make_mcq(
    "mcq-cnt-07-015", "ch-cnt-07", "top-cnt-07-02",
    "In State of West Bengal v. B.K. Mondal & Sons (AIR 1962 SC 779), the contractor constructed buildings for the government under oral requests without formal compliance with Article 299 of the Constitution. The Supreme Court held:",
    ["The contractor was entitled to compensation under Section 70 because the government accepted and enjoyed the benefit of the lawful non-gratuitous work", "The contractor had no remedy because Article 299 is mandatory and overrides Section 70 completely", "The contractor's officers were liable to imprisonment", "The buildings must be demolished"],
    0, "A",
    "The Supreme Court held that while the contract was unenforceable under Article 299, the government was bound to pay compensation under Section 70 for benefits enjoyed.",
    {"A": "Correct. Landmark Constitution Bench ruling applying Section 70 to non-compliant government contracts.", "B": "Article 299 bars contract suits, but does not displace quasi-contractual restitution.", "C": "No criminal offense was committed.", "D": "Demolition was rejected; compensation was awarded."},
    "Hard", "Supreme Court: State of WB v. BK Mondal & Sons (AIR 1962 SC 779)", "Master BK Mondal ruling on Section 70 and Article 299."
))
mcqs.append(make_mcq(
    "mcq-cnt-07-016", "ch-cnt-07", "top-cnt-07-02",
    "Under Section 71 of the Indian Contract Act, a person who finds goods belonging to another, and takes them into his custody, is subject to the same responsibility as a:",
    ["Trustee in bankruptcy", "Bailee", "Pawnee", "Mortgagee in possession"],
    1, "B",
    "Section 71 provides: 'A person who finds goods belonging to another, and takes them into his custody, is subject to the same responsibility as a bailee'.",
    {"A": "Finder is not a trustee in bankruptcy.", "B": "Correct. Section 71 statutorily equates finder of goods to a bailee.", "C": "Pawnee holds goods as security for debt (Section 172).", "D": "Mortgagee in possession relates to immovable property under TPA."},
    "Easy", "Indian Contract Act, 1872, Section 71", "Identify legal status of finder of goods under Section 71."
))
mcqs.append(make_mcq(
    "mcq-cnt-07-017", "ch-cnt-07", "top-cnt-07-02",
    "Under Section 168 and 169 of the Indian Contract Act, what are the rights of a finder of goods?",
    ["The finder may sue the owner for compensation for trouble and expense, and has a right of lien", "The finder can sell the goods if the owner cannot with reasonable diligence be found, or refuses to pay lawful charges, and the thing is in danger of perishing or lawful charges amount to 2/3 of its value", "Both A and B", "The finder automatically becomes absolute owner after 24 hours"],
    1, "B",
    "Under Section 168, the finder cannot sue for trouble/expense (only for specific reward offered), but has a lien. Under Section 169, finder may sell if goods are perishing or charges equal 2/3 value.",
    {"A": "Finder cannot sue for general trouble and expense (Section 168); only has lien.", "B": "Correct. Section 169 conditions for sale: perishing goods or charges equal two-thirds of value.", "C": "A is partially incorrect as finder cannot sue for trouble/expense.", "D": "Finder never becomes absolute owner after 24 hours."},
    "Hard", "Indian Contract Act, 1872, Sections 168, 169", "Master rights and power of sale of finder of goods."
))
mcqs.append(make_mcq(
    "mcq-cnt-07-018", "ch-cnt-07", "top-cnt-07-02",
    "Under Section 72 of the Indian Contract Act, a person to whom money has been paid, or anything delivered, by mistake or under coercion, must repay or return it. In Mahabir Kishore v. State of MP (AIR 1990 SC 313), the limitation period for recovering money paid under mistake of law runs from:",
    ["The date the money was initially deposited", "The date on which the mistake is discovered or could with reasonable diligence have been discovered", "The date the recipient files his income tax return", "12 years from the date of payment"],
    1, "B",
    "Under Section 17(1)(c) of the Limitation Act, 1963 and Mahabir Kishore, limitation runs from the date of discovery of the mistake (when the judgment declaring the law was passed).",
    {"A": "Payment date is not the starting point for mistake of law.", "B": "Correct. Limitation runs from the date when the mistake is discovered.", "C": "Tax return filing is irrelevant.", "D": "Limitation for suit under Section 72 is 3 years (Article 113) from discovery, not 12 years."},
    "Hard", "Supreme Court: Mahabir Kishore v. State of MP (AIR 1990 SC 313)", "Apply limitation rule for recovery under Section 72."
))

print(f"Total MCQs generated for Part 2: {len(mcqs)}")

with open('scripts/data_contract_mcqs_2.py', 'w', encoding='utf-8') as f:
    f.write("# Contract Law MCQs Part 2 (Chapters 5 to 7: 60 MCQs)\n")
    f.write("MCQS_PART2 = " + json.dumps(mcqs, indent=2) + "\n")

print("Successfully written scripts/data_contract_mcqs_2.py")
