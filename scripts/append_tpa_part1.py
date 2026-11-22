# Append Chapter 2 & Chapter 3 to data_tpa_mcqs_1.py (60 MCQs)
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

# Read existing 30 questions
with open('scripts/data_tpa_mcqs_1.py', 'r', encoding='utf-8') as f:
    txt = f.read()
start = txt.find('[')
end = txt.rfind(']')
data = json.loads(txt[start:end+1])

# --- CH-02 TOPIC 01: Section 10 ---
data.append(q("mcq-tpa-02-001", "ch-tpa-02", "top-tpa-02-01",
    "Under Section 10 of the Transfer of Property Act, where property is transferred subject to a condition or limitation absolutely restraining the transferee or any person claiming under him from parting with or disposing of his interest in the property, the condition or limitation is:",
    ["Void", "Voidable at the option of transferor", "Valid if agreed in writing", "Enforceable for 20 years"],
    0, "A",
    "Section 10 states that a condition absolutely restraining alienation is void. The transfer itself remains valid, while the restrictive condition is severed and void.",
    {"A": "Correct. Condition is void; transfer remains valid.", "B": "Not voidable.", "C": "Agreement in writing cannot validate absolute restraint.", "D": "No 20-year validity window."},
    "Easy", "Transfer of Property Act, 1882, Section 10", "Recall rule on absolute restraint on alienation under Section 10."))

data.append(q("mcq-tpa-02-002", "ch-tpa-02", "top-tpa-02-01",
    "Under Section 10, what are the two statutory exceptions where a condition restraining alienation is valid?",
    ["(1) In the case of a lease where condition is for benefit of lessor, and (2) transfer to or for benefit of a woman not being a Hindu, Muhammadan or Buddhist, that she shall not have power to alienate", "Transfers to government bodies and charitable trusts", "Agricultural leases exceeding 99 years", "Family partitions between brothers"],
    0, "A",
    "Section 10 contains two express exceptions: lease conditions for lessor's benefit, and married women's property restraint (non-Hindu, Muslim, Buddhist).",
    {"A": "Correct. The two statutory exceptions to Section 10.", "B": "Not general statutory exceptions under Section 10.", "C": "Leases are covered by exception 1, not 99-year rule.", "D": "Partitions are not transfers under Section 5."},
    "Medium", "Transfer of Property Act, 1882, Section 10 Exceptions", "Identify statutory exceptions to Section 10."))

data.append(q("mcq-tpa-02-003", "ch-tpa-02", "top-tpa-02-01",
    "In Rosher v. Rosher (1884), a testator devised land to his son with a condition that if the son wished to sell during the life of his mother, she should have option to buy at one-fifth market value. The court held:",
    ["The condition was valid as a partial restraint", "The condition amounted to an absolute restraint on alienation and was void", "The mother became co-owner", "The transfer was void ab initio"],
    1, "B",
    "Forcing sale at one-fifth market value effectively prevented alienation at fair market price, amounting to absolute restraint, and was held void.",
    {"A": "Extreme undervaluation turns partial restriction into absolute restraint.", "B": "Correct. Compelling sale at deep discount is in effect absolute restraint.", "C": "Mother acquired no co-ownership.", "D": "Devise remained valid; condition was void."},
    "Hard", "Rosher v. Rosher (1884) 26 Ch D 801", "Distinguish absolute from partial restraint in Rosher case."))

data.append(q("mcq-tpa-02-004", "ch-tpa-02", "top-tpa-02-01",
    "In Muhammad Raza v. Abbas Bandi Bibi (1932), the Privy Council held that a condition restricting alienation outside the family or to strangers was:",
    ["A valid partial restraint, not prohibited by Section 10", "An absolute restraint and void under Section 10", "An illegal restraint under Section 23 Contract Act", "A void wagering agreement"],
    0, "A",
    "The Privy Council held that a restriction prohibiting transfer to strangers outside family members is a partial restraint and therefore valid.",
    {"A": "Correct. Partial restraint (restricting alienation to family) is valid.", "B": "Not an absolute restraint.", "C": "Not illegal under Section 23.", "D": "No wager is involved."},
    "Medium", "Privy Council: Muhammad Raza v. Abbas Bandi Bibi (AIR 1932 PC 158)", "Master partial restraint validity in Muhammad Raza."))

data.append(q("mcq-tpa-02-005", "ch-tpa-02", "top-tpa-02-01",
    "Under Section 11 of the Transfer of Property Act, where a transfer creates an absolute interest in property in favor of a person, but terms direct that such interest shall be applied or enjoyed by him in a particular manner:",
    ["He is entitled to receive and dispose of such interest as if there were no such direction", "He is bound to follow the direction strictly", "The entire transfer is void", "The transferor can re-enter at any time"],
    0, "A",
    "Section 11 codifies the rule in Saunders v. Vautier: restriction repugnant to the interest created is void; transferee takes property free from the restriction.",
    {"A": "Correct. Section 11 invalidates directions restricting enjoyment of absolute estate.", "B": "Repugnant restriction is legally unenforceable.", "C": "Transfer remains fully valid.", "D": "No right of re-entry exists."},
    "Medium", "Transfer of Property Act, 1882, Section 11", "Identify rule against repugnant conditions under Section 11."))

data.append(q("mcq-tpa-02-006", "ch-tpa-02", "top-tpa-02-01",
    "Under Section 11 paragraph 2, what is the statutory exception permitting a transferor to impose restrictions on enjoyment?",
    ["Direction made for beneficial enjoyment of another piece of transferor's adjoining property (covenants running with land / Tulk v. Moxhay)", "Direction that property must never be used for business", "Direction that property shall not be inherited by daughters", "Direction that no trees shall ever be planted"],
    0, "A",
    "Section 11(2) saves directions made for beneficial enjoyment of another piece of property belonging to transferor (affirmative/negative restrictive covenants).",
    {"A": "Correct. Section 11(2) saves restrictive covenants for benefit of adjoining land.", "B": "General business prohibition in gross is void.", "C": "Interfering with statutory succession is void.", "D": "Tree planting restriction in gross is unenforceable."},
    "Hard", "Transfer of Property Act, 1882, Section 11 Paragraph 2", "Master Tulk v Moxhay exception under Section 11(2)."))

data.append(q("mcq-tpa-02-007", "ch-tpa-02", "top-tpa-02-01",
    "What is the key difference between Section 10 and Section 11 of the Transfer of Property Act?",
    ["Section 10 applies where alienation is restrained; Section 11 applies where mode of enjoyment of an absolute estate is restricted", "Section 10 applies to leases; Section 11 applies to sales only", "Section 10 makes the transfer void; Section 11 makes it voidable", "There is no difference between them"],
    0, "A",
    "Section 10 deals with restraint on alienation (power of disposition). Section 11 deals with restraint on enjoyment of an absolute property interest.",
    {"A": "Correct. Fundamental distinction: restraint on alienation (S.10) vs restraint on enjoyment (S.11).", "B": "Both sections have broader applications.", "C": "In both sections, the transfer is valid and only condition is void.", "D": "They govern distinct operational aspects."},
    "Medium", "Transfer of Property Act, 1882, Sections 10, 11", "Distinguish Section 10 from Section 11."))

data.append(q("mcq-tpa-02-008", "ch-tpa-02", "top-tpa-02-01",
    "Under Section 12 of the Transfer of Property Act, a condition making an interest determinable on the transferee becoming insolvent or attempting to assign it is:",
    ["Void, except in the case of a lease for the benefit of the lessor", "Valid in all commercial contracts", "Voidable at the option of the Official Receiver", "Enforceable only by banks"],
    0, "A",
    "Section 12 invalidates conditions terminating property interest upon insolvency or assignment, except in a lease for the lessor's benefit.",
    {"A": "Correct. Section 12 rule and lease exception.", "B": "General insolvency termination clauses in ownership transfers are void.", "C": "Not voidable; void by statute.", "D": "Banks enjoy no special exemption."},
    "Medium", "Transfer of Property Act, 1882, Section 12", "Recall rule on insolvency condition under Section 12."))

data.append(q("mcq-tpa-02-009", "ch-tpa-02", "top-tpa-02-01",
    "A sells a house to B with a condition: 'B shall not sell the house to anyone except C, and that too for Rs 10,000 only' (market value being Rs 10 lakhs). This condition is:",
    ["Void under Section 10 as an absolute restraint disguised as partial restraint", "A valid pre-emption agreement", "Valid partial restraint", "Voidable at the option of C"],
    0, "A",
    "Restricting sale to one named person at a tiny fraction of market value constitutes absolute restraint on alienation and is void under Section 10.",
    {"A": "Correct. Gross undervaluation and single-person restriction is void under Section 10.", "B": "Pre-emption must be at market or agreed fair valuation.", "C": "It is not a valid partial restraint.", "D": "It is void, not voidable."},
    "Easy", "Transfer of Property Act, 1882, Section 10", "Apply Section 10 to disguised absolute restraint."))

data.append(q("mcq-tpa-02-010", "ch-tpa-02", "top-tpa-02-01",
    "Where a condition restraining alienation is declared void under Section 10, what is the legal status of the conveyance itself?",
    ["The conveyance remains completely valid and the transferee takes the property free from the restraint", "The conveyance becomes void ab initio", "The property reverts to the transferor", "The property is forfeited to the State"],
    0, "A",
    "Under Section 10, the transfer itself is operative and valid; only the restraining condition is void and severed.",
    {"A": "Correct. Transfer is valid; condition is severed and void.", "B": "Transfer does not become void.", "C": "No reverter to transferor.", "D": "No state forfeiture."},
    "Easy", "Transfer of Property Act, 1882, Section 10", "Clarify effect of void condition on main transfer under Section 10."))

# --- CH-02 TOPIC 02: Section 13 ---
data.append(q("mcq-tpa-02-011", "ch-tpa-02", "top-tpa-02-02",
    "Under Section 13 of the Transfer of Property Act, can a transfer of property be made directly to an unborn person without an intermediate life estate?",
    ["No, an unborn person has no legal existence; transfer must be preceded by a prior interest created by the same transfer", "Yes, property can be transferred directly to unborn grandchildren", "Yes, if registered with a magistrate", "Only in urban commercial cities"],
    0, "A",
    "Section 13 requires that transfer for an unborn person must be preceded by a prior life estate created by the same transfer, because property cannot be in abeyance.",
    {"A": "Correct. Prior life estate is mandatory under Section 13.", "B": "Direct transfer to an unborn person is void ab initio.", "C": "Magisterial registration cannot cure absence of life estate.", "D": "Applies uniformly across India."},
    "Easy", "Transfer of Property Act, 1882, Section 13", "Recall mandatory prior interest requirement under Section 13."))

data.append(q("mcq-tpa-02-012", "ch-tpa-02", "top-tpa-02-02",
    "Under Section 13 of the Transfer of Property Act, what quantum of interest must be transferred to the unborn person?",
    ["The entire remaining interest of the transferor in the property (absolute interest)", "A life estate only", "A 10-year leasehold interest", "A contingent right of pre-emption"],
    0, "A",
    "Section 13 explicitly requires that the interest created for the unborn person must be the entire remaining interest of the transferor (no life estate to unborn person).",
    {"A": "Correct. Section 13 requires the entire remaining interest.", "B": "A life estate cannot be given to an unborn person (Tagore v. Tagore).", "C": "Leasehold does not satisfy Section 13.", "D": "Pre-emption is not the full remaining interest."},
    "Medium", "Transfer of Property Act, 1882, Section 13", "Master requirement of entire remaining interest under Section 13."))

data.append(q("mcq-tpa-02-013", "ch-tpa-02", "top-tpa-02-02",
    "In the landmark Privy Council decision Tagore v. Tagore (1872), the rule established regarding transfers to unborn persons was:",
    ["A person cannot create a life estate in favor of an unborn person; a gift to an unborn person must comprise the absolute estate", "Unborn persons can hold successive life estates indefinitely", "Hindu law permits direct gifts to unborn persons without life estate", "Gifts to unborn persons are completely prohibited under all circumstances"],
    0, "A",
    "Tagore v. Tagore established that successive life estates cannot be given to unborn persons; Section 13 codifies this by requiring transfer of the whole remaining interest.",
    {"A": "Correct. Life estate cannot be given to unborn person; must be absolute.", "B": "Successive life estates to unborn persons violate perpetuities.", "C": "Hindu law strictly prohibited gifts to unborn persons until statutory modification.", "D": "Permitted subject to strict Section 13 conditions."},
    "Hard", "Privy Council: Tagore v. Tagore (1872) 9 Beng LR 377", "Master Tagore v Tagore principle codified in Section 13."))

data.append(q("mcq-tpa-02-014", "ch-tpa-02", "top-tpa-02-02",
    "A transfers property to B for life, and after B's death to B's eldest son (yet unborn) for life, and after his death to C absolutely. What is the legal validity of the transfer to B's unborn son?",
    ["The transfer to B's unborn son is void because it conveys only a life estate, not the entire remaining interest", "It is valid for 21 years", "It is valid because C gets the ultimate estate", "It is valid if B gives written consent"],
    0, "A",
    "Under Section 13, the interest created for the unborn person must be the whole remaining interest. Creating a life estate for an unborn person is void ab initio.",
    {"A": "Correct. Transfer of life estate to unborn person is void under Section 13.", "B": "No 21-year saving rule for life estate to unborn.", "C": "Ultimate gift to C also fails under Section 16.", "D": "Consent of prior holder cannot cure Section 13 defect."},
    "Medium", "Transfer of Property Act, 1882, Section 13", "Apply Section 13 to life estate created for unborn person."))

data.append(q("mcq-tpa-02-015", "ch-tpa-02", "top-tpa-02-02",
    "Under Section 13, at what exact moment must the unborn beneficiary come into existence?",
    ["Before or at the moment when the prior life estate terminates", "Within 12 years after the life tenant's death", "At the date of execution of the deed", "When he completes 18 years of age"],
    0, "A",
    "The unborn person must come into existence (at least conceived in womb) before or at the expiry of the prior life estate; otherwise property reverts to transferor.",
    {"A": "Correct. Unborn person must exist before or at termination of prior estate.", "B": "Property cannot remain in abeyance for 12 years.", "C": "He is unborn at deed execution; that is the very premise.", "D": "Conception/birth, not age 18, is the existence test."},
    "Hard", "Transfer of Property Act, 1882, Section 13", "Determine exact timing of existence for unborn beneficiary."))

data.append(q("mcq-tpa-02-016", "ch-tpa-02", "top-tpa-02-02",
    "In Girjesh Dutt v. Data Din (AIR 1934 Oudh 35), a donor gifted property to his nephew's daughter for life, and then to her male descendants absolutely; and in default of male descendants, to her female descendants for life. The court held:",
    ["The gift to female descendants was void under Section 13 as it created a life estate for unborn persons, and subsequent gifts failed under Section 16", "The entire gift was valid in all respects", "Female descendants took absolute ownership", "The property escheated to the Crown"],
    0, "A",
    "The court held that gift of life interest to unborn female descendants was void under Section 13, and gift over in default failed under Section 16.",
    {"A": "Correct. Landmark Indian case illustrating failure under Section 13 and Section 16.", "B": "Gift to unborn life estate is void.", "C": "Court cannot convert a life estate into absolute estate.", "D": "Property reverted to donor's heirs."},
    "Hard", "Girjesh Dutt v. Data Din (AIR 1934 Oudh 35)", "Master Girjesh Dutt ruling on Section 13 and Section 16."))

data.append(q("mcq-tpa-02-017", "ch-tpa-02", "top-tpa-02-02",
    "Under Section 16 of the Transfer of Property Act, where by reason of any rules in Section 13 and 14 an interest fails, any interest created in the same transaction and intended to take effect after or upon failure of such prior interest:",
    ["Also fails", "Takes effect immediately as a vested estate", "Is preserved for 21 years", "Is transferred to the state government"],
    0, "A",
    "Section 16: Where a prior interest fails under Section 13 or 14, any subsequent interest intended to take effect upon or after such prior interest also fails.",
    {"A": "Correct. Section 16 rule: subsequent interest dependent on void prior interest fails.", "B": "Cannot accelerate if dependent on invalid prior disposition.", "C": "No 21-year preservation rule.", "D": "Reverts to transferor, not government."},
    "Medium", "Transfer of Property Act, 1882, Section 16", "Recall effect of prior failure on subsequent interest under Section 16."))

data.append(q("mcq-tpa-02-018", "ch-tpa-02", "top-tpa-02-02",
    "Can more than one successive life estate be created in favor of LIVING persons before property vests in an unborn person?",
    ["Yes, any number of successive life estates may be created in favor of living persons", "No, only one single life estate is permissible", "Only two life estates can ever be created", "Only if the living persons are married to each other"],
    0, "A",
    "Section 13 does not restrict the number of prior life estates created in favor of living persons (e.g. to A for life, then to B for life, then to C for life, then to C's unborn son absolutely).",
    {"A": "Correct. Multiple successive life estates to living persons are valid.", "B": "Not limited to one life estate.", "C": "No numerical restriction of two.", "D": "Marital status is irrelevant."},
    "Medium", "Transfer of Property Act, 1882, Section 13", "Understand multiple life estates to living persons under Section 13."))

data.append(q("mcq-tpa-02-019", "ch-tpa-02", "top-tpa-02-02",
    "Under Section 13, if the unborn person is conceived in the mother's womb before the termination of the prior life estate:",
    ["He is deemed to be in existence in the eyes of law (en ventre sa mere)", "He is not considered in existence until actual physical birth", "The transfer is suspended for 9 years", "The property reverts to the donor permanently"],
    0, "A",
    "A child in the mother's womb (en ventre sa mere) is treated as already in existence in law from the date of conception, satisfying Section 13.",
    {"A": "Correct. En ventre sa mere rule applies to Section 13.", "B": "Conception in womb counts as existence in law.", "C": "No 9-year suspension.", "D": "No reverter if child is conceived before life estate ends."},
    "Medium", "Indian Property Jurisprudence, Section 13", "Apply en ventre sa mere rule to Section 13."))

data.append(q("mcq-tpa-02-020", "ch-tpa-02", "top-tpa-02-02",
    "What happens to the property if the unborn person in whose favor absolute interest was created under Section 13 is never born?",
    ["The property reverts back to the transferor or his legal heirs (resulting trust)", "The property belongs to the life tenant absolutely", "The property escheats to the municipality", "The property is auctioned by the court"],
    0, "A",
    "If the ultimate gift fails because the unborn person is never born, the remaining reversionary interest reverts to the transferor or his legal representatives.",
    {"A": "Correct. Reversion vests back in transferor/heirs upon failure of unborn gift.", "B": "Life tenant holds only a life estate; cannot usurp fee simple.", "C": "No escheat to municipality.", "D": "No court auction."},
    "Easy", "Transfer of Property Act, 1882, Section 13", "Explain reversion upon non-birth of unborn beneficiary."))

# --- CH-02 TOPIC 03: Sections 14, 17 ---
data.append(q("mcq-tpa-02-021", "ch-tpa-02", "top-tpa-02-03",
    "Under Section 14 of the Transfer of Property Act, the 'Rule Against Perpetuity' provides that no transfer of property can operate to create an interest which is to take effect after the lifetime of one or more persons living at the date of such transfer, and:",
    ["The minority of some person who shall be in existence at the expiration of that period, and to whom the interest created is to belong", "A gross period of 21 years in all cases", "The lifetime of all grandchildren", "99 years from execution"],
    0, "A",
    "Section 14: Maximum perpetuity period in India = Life of living persons + minority (18 years) of unborn beneficiary in existence. (Unlike English law, no gross period of 21 years in gross).",
    {"A": "Correct. Indian perpetuity period: life of living persons + actual minority of beneficiary.", "B": "English common law allows 21 years in gross, but Indian law strictly requires actual minority.", "C": "Unborn grandchildren cannot extend life period.", "D": "No 99-year rule under Section 14."},
    "Medium", "Transfer of Property Act, 1882, Section 14", "Master formula for perpetuity period under Section 14."))

data.append(q("mcq-tpa-02-022", "ch-tpa-02", "top-tpa-02-03",
    "What is the maximum period of postponement of vesting permitted under Section 14 of the Transfer of Property Act in India?",
    ["Life or lives in being + period of gestation + minority (18 years) of the ultimate beneficiary", "Life in being + 21 years in gross", "100 years absolute", "Life of the transferor only"],
    0, "A",
    "Under Section 14, the maximum perpetuity period = Life of living persons + period of gestation (if gestation actually exists) + minority (18 years).",
    {"A": "Correct. Statutory maximum period under Section 14.", "B": "21 years in gross is English law, not Indian Section 14.", "C": "No 100-year rule.", "D": "Can extend across lives in being plus minority."},
    "Medium", "Transfer of Property Act, 1882, Section 14", "Identify exact components of perpetuity period under Indian law."))

data.append(q("mcq-tpa-02-023", "ch-tpa-02", "top-tpa-02-03",
    "Under Indian law, what is the age of minority for the purpose of the Rule Against Perpetuity in Section 14?",
    ["18 years under the Indian Majority Act", "21 years under English common law", "25 years under Roman law", "16 years under juvenile statutes"],
    0, "A",
    "Minority in India is governed by the Indian Majority Act, 1875, which fixes the age of majority at 18 years (Saundara Rajan v. Natarajan, 1925).",
    {"A": "Correct. 18 years is the age of majority in India.", "B": "21 years is English common law rule, rejected for India in Saundara Rajan.", "C": "Roman law is inapplicable.", "D": "Juvenile statutes do not govern property vesting."},
    "Easy", "Privy Council: Saundara Rajan v. Natarajan (AIR 1925 PC 244)", "Recall age of minority under Section 14."))

data.append(q("mcq-tpa-02-024", "ch-tpa-02", "top-tpa-02-03",
    "In Saundara Rajan v. Natarajan (AIR 1925 PC 244), the Privy Council held that where vesting in unborn children was postponed until they attained the age of 21 years:",
    ["The bequest was void under Section 14 because in India minority terminates at 18 years, making postponement to 21 years violate the rule against perpetuity", "The bequest was automatically modified to 18 years", "The bequest was completely valid under English law", "The property was forfeited"],
    0, "A",
    "The Privy Council held that postponing vesting beyond 18 years violates Section 14, rendering the disposition void; courts cannot rewrite 21 years to 18 years.",
    {"A": "Correct. Postponing vesting to 21 years violates Section 14 in India.", "B": "Cy-pres modification does not rewrite invalid private property transfers.", "C": "English law does not override Indian statute.", "D": "No forfeiture; property reverted to estate."},
    "Hard", "Privy Council: Saundara Rajan v. Natarajan (AIR 1925 PC 244)", "Apply Saundara Rajan on 21-year vesting violation."))

data.append(q("mcq-tpa-02-025", "ch-tpa-02", "top-tpa-02-03",
    "Does the Rule Against Perpetuity apply to transfers for the benefit of the public under Section 18 of the TPA?",
    ["No, Section 18 expressly exempts transfers for advancement of religion, knowledge, commerce, health, safety, or other objects beneficial to mankind", "Yes, public trusts must vest within 18 years", "Only if approved by the Charity Commissioner", "Only for medical hospitals"],
    0, "A",
    "Section 18 creates an express statutory exception to Sections 14, 16, and 17 for transfers for the benefit of the public (charitable, religious, educational trusts).",
    {"A": "Correct. Section 18 exempts public/charitable transfers from perpetuity rules.", "B": "Charitable gifts may be in perpetuity.", "C": "Exemption flows directly from Section 18.", "D": "Covers religion, knowledge, commerce, health, safety, and all public benefits."},
    "Easy", "Transfer of Property Act, 1882, Section 18", "Identify Section 18 charitable exemption from perpetuities."))

data.append(q("mcq-tpa-02-026", "ch-tpa-02", "top-tpa-02-03",
    "Does the Rule Against Perpetuity apply to personal covenants or contracts (e.g. covenant for pre-emption or option to purchase)?",
    ["No, Section 14 applies only to creation of an interest in property, not to mere personal contracts (Ram Baran Prasad v. Ram Mohit Hazra, 1967)", "Yes, all contracts expire after 18 years", "Only if the contract is registered", "Only between landlord and tenant"],
    0, "A",
    "In Ram Baran Prasad v. Ram Mohit Hazra (1967), the Supreme Court affirmed that Section 14 applies to property interests, not personal contracts like pre-emption.",
    {"A": "Correct. Section 14 does not bind personal contracts or pre-emption covenants.", "B": "Contracts are not bound by property perpetuities.", "C": "Registration does not change contract into property interest.", "D": "Applies across all pre-emption covenants."},
    "Hard", "Supreme Court: Ram Baran Prasad v. Ram Mohit Hazra (AIR 1967 SC 744)", "Master Ram Baran Prasad ruling on pre-emption and perpetuity."))

data.append(q("mcq-tpa-02-027", "ch-tpa-02", "top-tpa-02-03",
    "Under Section 17 of the Transfer of Property Act, what is the maximum period for which accumulation of income may be directed?",
    ["The life of the transferor, OR a period of 18 years from the date of the transfer (whichever is longer)", "21 years from transferor's death", "In perpetuity for 100 years", "Only 5 years"],
    0, "A",
    "Section 17 provides that direction for accumulation is valid only for: (a) life of transferor, OR (b) a period of 18 years from date of transfer; beyond that, direction is void.",
    {"A": "Correct. Section 17 maximum accumulation period.", "B": "21 years is English Thellusson Act period, not Indian Section 17.", "C": "Perpetual accumulation is prohibited.", "D": "Not limited to 5 years."},
    "Medium", "Transfer of Property Act, 1882, Section 17", "Recall statutory limits on accumulation under Section 17."))

data.append(q("mcq-tpa-02-028", "ch-tpa-02", "top-tpa-02-03",
    "Under Section 17 paragraph 2, which of the following directions for accumulation is exempted from the 18-year restriction?",
    ["Payment of debts of transferor or any other person, provision for portions for children, or preservation/maintenance of property", "Accumulation for speculative stock trading", "Accumulation to build a private family museum", "Accumulation to pay gambling debts"],
    0, "A",
    "Section 17(2) exempts: (1) payment of debts, (2) provision for portions for children/descendants, and (3) preservation and repair of property.",
    {"A": "Correct. The three statutory exceptions under Section 17(2).", "B": "Commercial speculation is not exempted.", "C": "Private museums are not statutory exceptions.", "D": "Gambling debts are illegal."},
    "Medium", "Transfer of Property Act, 1882, Section 17 Paragraph 2", "Identify exceptions to Section 17 accumulation limits."))

data.append(q("mcq-tpa-02-029", "ch-tpa-02", "top-tpa-02-03",
    "In the landmark English decision Thellusson v. Woodford (1799), which led to the statutory restriction on accumulation:",
    ["A testator directed accumulation of his huge estate during the lives of all his descendants living at his death, which would have tied up wealth for over a century", "A testator directed daily burning of currency", "A testator gave property to a foreign emperor", "A testator tried to create a commercial bank"],
    0, "A",
    "Thellusson's will directed accumulation for lives of all sons, grandsons, and great-grandsons, tying up millions for over a century, prompting the Thellusson Act (codified in Section 17).",
    {"A": "Correct. Historical foundation of the rule against accumulation.", "B": "Destruction of property was not involved.", "C": "Not given to an emperor.", "D": "Not a bank incorporation."},
    "Hard", "Thellusson v. Woodford (1799) 4 Ves 227", "Explain historical origin of accumulation rule."))

data.append(q("mcq-tpa-02-030", "ch-tpa-02", "top-tpa-02-03",
    "Under Section 14, in testing whether a disposition violates the Rule Against Perpetuity, the court looks at:",
    ["Possible events at the date of transfer, not what actually happens subsequently (remoteness of vesting test)", "Actual events after 50 years have passed", "The health condition of the beneficiaries", "The wishes of the executors"],
    0, "A",
    "Perpetuity is tested at the date of transfer (or testator's death for wills): if vesting could possibly be postponed beyond the legal limit under any hypothetical scenario, it is void.",
    {"A": "Correct. Test of possibility, not hindsight, governs perpetuity.", "B": "Hindsight / actual subsequent events cannot save a disposition.", "C": "Health status is irrelevant.", "D": "Executors cannot rewrite terms."},
    "Hard", "Indian Property Jurisprudence, Section 14", "Apply rule of possibility in testing perpetuity."))

# Save back to file
with open('scripts/data_tpa_mcqs_1.py', 'w', encoding='utf-8') as f:
    f.write("# TPA MCQs Part 1 (Chapters 1 & 2: 60 MCQs)\n")
    f.write("MCQS_PART1 = " + json.dumps(data, indent=2) + "\n")

print(f"Updated scripts/data_tpa_mcqs_1.py: Total {len(data)} MCQs")
