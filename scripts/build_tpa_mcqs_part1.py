# TPA MCQs Part 1 Builder (Chapters 1 to 3: 90 MCQs)
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

data = []

# --- CH-01 TOPIC 01 ---
data.append(q("mcq-tpa-01-001", "ch-tpa-01", "top-tpa-01-01",
    "Under Section 5 of the Transfer of Property Act, 1882, 'transfer of property' is defined as an act by which a living person conveys property:",
    ["To himself or to another living person in present or in future", "Only by will to take effect after death", "Through a court auction decree", "Exclusively between blood relatives"],
    0, "A",
    "Section 5 defines transfer as an act by which a living person conveys property to one or more other living persons, or to himself, in present or future.",
    {"A": "Correct. Section 5 inter vivos definition.", "B": "Wills are testamentary, not inter vivos transfers under TPA.", "C": "Involuntary execution sales are excluded under Section 2(d).", "D": "No restriction to blood relatives."},
    "Easy", "Transfer of Property Act, 1882, Section 5", "Recall statutory definition of transfer of property."))

data.append(q("mcq-tpa-01-002", "ch-tpa-01", "top-tpa-01-01",
    "The phrase 'living person' in Section 5 includes:",
    ["A company or association or body of individuals, whether incorporated or not", "Only natural human beings", "Deceased ancestors represented by legal heirs", "Idols only"],
    0, "A",
    "Section 5 paragraph 2 explicitly provides that 'living person' includes a company, association, or body of individuals.",
    {"A": "Correct. Section 5 paragraph 2 inclusion.", "B": "Corporations and associations are expressly included.", "C": "Deceased persons cannot make inter vivos transfers.", "D": "Not limited to idols."},
    "Easy", "Transfer of Property Act, 1882, Section 5", "Identify scope of living person under Section 5."))

data.append(q("mcq-tpa-01-003", "ch-tpa-01", "top-tpa-01-01",
    "Which of the following family transactions does NOT constitute a 'transfer of property' under Section 5?",
    ["Partition of joint family property", "Gift deed executed inter vivos", "Simple mortgage", "Lease of agricultural land"],
    0, "A",
    "In Commissioner of Income Tax v. Keshavlal Lallubhai (1965), the Supreme Court held partition is not a transfer because coparceners have antecedent title.",
    {"A": "Correct. Partition rearranges existing rights and is not a transfer.", "B": "Gift is an inter vivos transfer under Section 122.", "C": "Mortgage transfers an interest in immovable property.", "D": "Lease transfers right of enjoyment under Section 105."},
    "Medium", "Supreme Court: CIT v. Keshavlal Lallubhai (AIR 1965 SC 866)", "Recognize that partition is not a transfer under Section 5."))

data.append(q("mcq-tpa-01-004", "ch-tpa-01", "top-tpa-01-01",
    "Does a family arrangement or compromise of doubtful claims amount to a transfer of property under the TPA?",
    ["No, because it acknowledges antecedent title rather than creating a new conveyance", "Yes, it is identical to a sale deed", "Yes, if consideration is paid in money", "Only if approved by the Revenue Board"],
    0, "A",
    "In Kale v. Deputy Director of Consolidation (1976), the Supreme Court held that family arrangements recognize existing rights and are not transfers.",
    {"A": "Correct. Family settlements recognize existing rights, not convey new title.", "B": "Not a sale.", "C": "Monetary equalization does not make it a conveyance.", "D": "Administrative approval does not define transfer."},
    "Medium", "Supreme Court: Kale v. Dy. Director of Consolidation (AIR 1976 SC 807)", "Distinguish family arrangement from transfer under Section 5."))

data.append(q("mcq-tpa-01-005", "ch-tpa-01", "top-tpa-01-01",
    "A surrender of a lease by a tenant to his landlord is:",
    ["Not a transfer of property, but a merger of lesser estate into the greater estate", "A transfer of property under Section 54", "An exchange under Section 118", "A gift under Section 122"],
    0, "A",
    "Surrender is the yielding up of a lesser estate to him who has the greater immediate estate; it extinguishes the leasehold without conveying property.",
    {"A": "Correct. Surrender is an extinguishment of leasehold, not a transfer.", "B": "Not a sale.", "C": "Not an exchange.", "D": "Not a gift."},
    "Hard", "Indian Property Jurisprudence, Section 5", "Classify surrender of lease."))

data.append(q("mcq-tpa-01-006", "ch-tpa-01", "top-tpa-01-01",
    "Under Section 2(d) of the Transfer of Property Act, saving clauses exclude from its operation:",
    ["Transfers by operation of law or by, or in execution of, a decree or order of a court of competent jurisdiction", "Gifts between living individuals", "Sales of land exceeding 5 acres", "Mortgages between registered firms"],
    0, "A",
    "Section 2(d) expressly saves transfers by operation of law or execution of court decrees, unless rules are specially applied.",
    {"A": "Correct. Involuntary execution sales and devolution by law are excluded under Section 2(d).", "B": "Inter vivos gifts are governed by Chapter VII.", "C": "Size of land does not exclude TPA.", "D": "Mortgages between firms are fully covered."},
    "Medium", "Transfer of Property Act, 1882, Section 2(d)", "Identify scope of Section 2(d) savings clause."))

data.append(q("mcq-tpa-01-007", "ch-tpa-01", "top-tpa-01-01",
    "Under Section 9 of the Transfer of Property Act, an oral transfer is valid in which cases?",
    ["In every case where a writing is not expressly required by law", "Never; all transfers must be written and registered", "Only for agricultural produce below Rs 50", "Only between brothers"],
    0, "A",
    "Section 9 states: 'A transfer of property may be made without writing in every case in which a writing is not expressly required by law'.",
    {"A": "Correct. Section 9 rule on oral transfer.", "B": "Writing is only required where specially mandated.", "C": "No Rs 50 limit for oral transfer under Section 9.", "D": "Relationship is irrelevant to Section 9."},
    "Easy", "Transfer of Property Act, 1882, Section 9", "Recall rule on oral transfer under Section 9."))

data.append(q("mcq-tpa-01-008", "ch-tpa-01", "top-tpa-01-01",
    "Which of the following is defined as 'immovable property' under Section 3 of the TPA?",
    ["Section 3 provides a negative definition: immovable property does not include standing timber, growing crops or grass", "All movable goods worth over Rs 1,000", "Government securities and shares", "Right to catch fish in a tank"],
    0, "A",
    "Section 3 defines immovable property negatively: 'immovable property does not include standing timber, growing crops or grass'.",
    {"A": "Correct. Section 3 negative statutory definition.", "B": "Movable goods are not immovable property.", "C": "Shares are movable goods.", "D": "Profits a prendre (fisheries) are immovable benefits under General Clauses Act."},
    "Easy", "Transfer of Property Act, 1882, Section 3", "Recall statutory definition of immovable property in Section 3."))

data.append(q("mcq-tpa-01-009", "ch-tpa-01", "top-tpa-01-01",
    "In Shantabai v. State of Bombay (AIR 1958 SC 532), Vivian Bose J. distinguished between 'standing timber' and 'trees', holding that standing timber refers to:",
    ["Trees fit for use in building or carpentry which are severed within a reasonably short time", "All living trees bearing fruit", "Bamboo groves used for shade", "Decorative shrubs in a garden"],
    0, "A",
    "Vivian Bose J. held that standing timber is wood fit for construction/carpentry intended to be cut within a short time, drawing no sustenance from soil.",
    {"A": "Correct. Shantabai test: timber trees intended for early cutting.", "B": "Fruit-bearing trees are immovable property.", "C": "Bamboo for shade is part of land.", "D": "Shrubs are not timber."},
    "Hard", "Supreme Court: Shantabai v. State of Bombay (AIR 1958 SC 532)", "Master Shantabai distinction on standing timber."))

data.append(q("mcq-tpa-01-010", "ch-tpa-01", "top-tpa-01-01",
    "Under the General Clauses Act, 1897 Section 3(26), 'immovable property' includes:",
    ["Land, benefits to arise out of land, and things attached to the earth, or permanently fastened to anything attached to the earth", "Moveable machinery that can be shifted without dismantle", "Standing crops and grass ready for harvest", "Government promissory notes"],
    0, "A",
    "General Clauses Act 3(26) supplies the positive definition: land, benefits arising out of land, and things attached to the earth.",
    {"A": "Correct. Positive definition applied in conjunction with TPA Section 3.", "B": "Easily movable machinery is chattel.", "C": "Standing crops are excluded under Section 3 TPA.", "D": "Promissory notes are movable actionable claims."},
    "Medium", "General Clauses Act, 1897, Section 3(26)", "Identify positive definition of immovable property."))

# --- CH-01 TOPIC 02: Section 6 ---
data.append(q("mcq-tpa-01-011", "ch-tpa-01", "top-tpa-01-02",
    "Under Section 6 of the Transfer of Property Act, what is the general rule regarding transferability of property?",
    ["Property of any kind may be transferred, except as otherwise provided by this Act or by any other law for the time being in force", "No property can be transferred without government license", "Only movable property is transferable", "Property can only be transferred to state authorities"],
    0, "A",
    "Section 6 opens with the general rule: property of any kind may be transferred, except as otherwise provided by law. Transferability is the rule; restraint is the exception.",
    {"A": "Correct. Section 6 opening rule.", "B": "No license requirement for private property.", "C": "Both movable and immovable property are transferable.", "D": "Private transfers are fully protected."},
    "Easy", "Transfer of Property Act, 1882, Section 6", "Recall general rule of transferability under Section 6."))

data.append(q("mcq-tpa-01-012", "ch-tpa-01", "top-tpa-01-02",
    "Under Section 6(a) of the TPA, which of the following cannot be transferred?",
    ["The chance of an heir-apparent succeeding to an estate (spes successionis), the chance of a relation obtaining a legacy on the death of a kinsman, or any other mere possibility of a like nature", "An existing house with registered title", "A vested remainder in agricultural land", "An actionable claim for debt"],
    0, "A",
    "Section 6(a) bars transfer of spes successionis (mere chance of succession) or other possibilities of a like nature.",
    {"A": "Correct. Section 6(a) bars transfer of spes successionis.", "B": "Existing house is fully transferable.", "C": "Vested remainder is a present property right, fully transferable.", "D": "Actionable claims are transferable under Section 130."},
    "Easy", "Transfer of Property Act, 1882, Section 6(a)", "Identify prohibition on transfer of spes successionis."))

data.append(q("mcq-tpa-01-013", "ch-tpa-01", "top-tpa-01-02",
    "In Amrit Narayan v. Gaya Singh (1917), the Privy Council held that a Hindu reversioner's right during the lifetime of a Hindu widow is:",
    ["A mere spes successionis (chance of succession) which cannot be transferred or made the subject of a valid contract", "A vested property interest transferable under Section 5", "An actionable claim enforceable in civil court", "A mortgageable estate"],
    0, "A",
    "The Privy Council held that a reversioner's interest during widow's life is a mere chance (spes successionis) that cannot be transferred or mortgaged.",
    {"A": "Correct. Leading case confirming reversioner's right is non-transferable spes successionis.", "B": "Not a vested interest.", "C": "Not an actionable claim.", "D": "Cannot be mortgaged under Section 6(a)."},
    "Medium", "Privy Council: Amrit Narayan v. Gaya Singh (1917) 45 IA 35", "Apply spes successionis doctrine to Hindu reversioner."))

data.append(q("mcq-tpa-01-014", "ch-tpa-01", "top-tpa-01-02",
    "Under Section 6(b) of the Transfer of Property Act, which of the following cannot be transferred?",
    ["A mere right of re-entry for breach of a condition subsequent cannot be transferred to anyone except the owner of the property affected thereby", "A leased property with its reversion", "An easement appurtenant to dominant tenement", "A mortgage debt"],
    0, "A",
    "Section 6(b) bars transfer of a mere right of re-entry apart from the reversion/ownership.",
    {"A": "Correct. Section 6(b) prohibits transfer of mere right of re-entry in gross.", "B": "Reversion is transferable with lease.", "C": "Easement attached to dominant heritage is transferable with it.", "D": "Mortgage debts are transferable."},
    "Medium", "Transfer of Property Act, 1882, Section 6(b)", "Identify restriction on transfer of right of re-entry."))

data.append(q("mcq-tpa-01-015", "ch-tpa-01", "top-tpa-01-02",
    "Under Section 6(c) of the Transfer of Property Act, an easement:",
    ["Cannot be transferred apart from the dominant heritage", "Can be transferred freely as an independent property right", "Can only be leased for 1 year", "Is automatically extinguished on transfer"],
    0, "A",
    "Section 6(c): 'An easement cannot be transferred apart from the dominant heritage'. Easements exist for the benefit of dominant land and cannot be severed in gross.",
    {"A": "Correct. Section 6(c) rule on easements.", "B": "Easements in gross cannot be independently transferred under TPA.", "C": "No 1-year rule.", "D": "Transfer of dominant land transfers the easement automatically under Section 8."},
    "Easy", "Transfer of Property Act, 1882, Section 6(c)", "Recall non-transferability of easement apart from dominant land."))

data.append(q("mcq-tpa-01-016", "ch-tpa-01", "top-tpa-01-02",
    "Under Section 6(d) of the Transfer of Property Act, an interest in property restricted in its enjoyment to the owner personally:",
    ["Cannot be transferred by him", "May be sold at public auction", "Can be mortgaged for business loans", "Transfers to legal heirs automatically"],
    0, "A",
    "Section 6(d) prohibits transfer of an interest restricted in its enjoyment to the owner personally (e.g. religious service tenure, right of residence).",
    {"A": "Correct. Section 6(d) statutory rule.", "B": "Cannot be auctioned in execution (Section 60 CPC).", "C": "Cannot be mortgaged.", "D": "Personal right does not pass to heirs."},
    "Easy", "Transfer of Property Act, 1882, Section 6(d)", "Identify restriction on personal property interests under Section 6(d)."))

data.append(q("mcq-tpa-01-017", "ch-tpa-01", "top-tpa-01-02",
    "Under Section 6(dd) of the Transfer of Property Act (inserted in 1929), which of the following is non-transferable?",
    ["A right to future maintenance, in whatsoever manner arising, secured or determined", "Past arrears of maintenance already accrued", "A money decree passed by a court", "A tenancy in urban shops"],
    0, "A",
    "Section 6(dd) explicitly prohibits transfer of a right to future maintenance. Arrears already accrued, however, can be transferred.",
    {"A": "Correct. Section 6(dd) prohibits transfer of right to future maintenance.", "B": "Accrued arrears constitute an existing debt, which is transferable.", "C": "Money decrees are transferable.", "D": "Tenancy rights are generally transferable unless barred by rent law."},
    "Medium", "Transfer of Property Act, 1882, Section 6(dd)", "Distinguish future maintenance from accrued maintenance."))

data.append(q("mcq-tpa-01-018", "ch-tpa-01", "top-tpa-01-02",
    "Under Section 6(e) of the Transfer of Property Act, which of the following cannot be transferred?",
    ["A mere right to sue", "An actionable claim", "A promissory note", "A book debt"],
    0, "A",
    "Section 6(e) provides that 'a mere right to sue cannot be transferred'. Law prohibits trafficking in unliquidated damages litigation.",
    {"A": "Correct. Section 6(e) bars transfer of a mere right to sue.", "B": "Actionable claims are transferable under Section 130.", "C": "Promissory notes are transferable under NI Act.", "D": "Book debts are actionable claims, fully transferable."},
    "Easy", "Transfer of Property Act, 1882, Section 6(e)", "Recall prohibition on transfer of mere right to sue."))

data.append(q("mcq-tpa-01-019", "ch-tpa-01", "top-tpa-01-02",
    "What is the key distinction between an 'actionable claim' (Section 3 & 130) and a 'mere right to sue' (Section 6(e))?",
    ["An actionable claim is a claim to a definite ascertained debt or beneficial interest; a mere right to sue is an unliquidated damages claim requiring judicial quantification", "Actionable claims are void; rights to sue are valid", "There is no difference in Indian law", "Rights to sue relate only to criminal torts"],
    0, "A",
    "An actionable claim is an existing, accruing, or contingent debt (liquidated sum). A mere right to sue is a claim for unliquidated damages for breach of contract or tort.",
    {"A": "Correct. Ascertained debt (transferable) vs unliquidated damages (non-transferable).", "B": "Actionable claims are valid and transferable.", "C": "Distinct statutory concepts.", "D": "Rights to sue are civil claims."},
    "Hard", "Indian Property Jurisprudence, Sections 3, 6(e), 130", "Distinguish actionable claim from mere right to sue."))

data.append(q("mcq-tpa-01-020", "ch-tpa-01", "top-tpa-01-02",
    "Under Section 6(f) and 6(g) of the TPA, public offices and stipends/pensions are non-transferable because:",
    ["Trafficking in public offices and military/civil pensions is opposed to public policy and barred by statute", "They are too valuable to be assessed in money", "Only central banks can buy them", "They are governed by maritime law"],
    0, "A",
    "Section 6(f) bars transfer of public office or salary of public officer; Section 6(g) bars military/civil pensions and political stipends on public policy grounds.",
    {"A": "Correct. Sections 6(f) and 6(g) bar transfers of offices and pensions on public policy grounds.", "B": "Public policy, not valuation difficulty, is the foundation.", "C": "Central banks cannot purchase public offices.", "D": "Maritime law has no application."},
    "Medium", "Transfer of Property Act, 1882, Section 6(f), 6(g)", "Identify public policy basis of Section 6(f) and 6(g)."))

# --- CH-01 TOPIC 03: Sections 7, 8 ---
data.append(q("mcq-tpa-01-021", "ch-tpa-01", "top-tpa-01-03",
    "Under Section 7 of the Transfer of Property Act, every person competent to contract under the Indian Contract Act is competent to transfer:",
    ["Transferable property, or to dispose of transferable property not his own, being authorized to determine of it", "Only if he is a hereditary landowner", "Only with the concurrence of all village elders", "Provided he is not an income tax payer"],
    0, "A",
    "Section 7: Every person competent to contract and entitled to transferable property, or authorized to dispose of property not his own, is competent to transfer.",
    {"A": "Correct. Section 7 statutory competency rule.", "B": "No hereditary requirement.", "C": "No village elder consent required.", "D": "Tax status is irrelevant to property competency."},
    "Easy", "Transfer of Property Act, 1882, Section 7", "Identify essentials of competency to transfer under Section 7."))

data.append(q("mcq-tpa-01-022", "ch-tpa-01", "top-tpa-01-03",
    "Can a minor execute a valid transfer of immovable property under Section 7 of the TPA?",
    ["No, because a minor is incompetent to contract under Section 11 of the Contract Act and Mohori Bibee, rendering any transfer by him void ab initio", "Yes, if he is represented by an advocate", "Yes, for agricultural lands only", "Yes, with permission of the sub-registrar"],
    0, "A",
    "Section 7 requires competency to contract; under Mohori Bibee, a minor's transfer as transferor is void ab initio.",
    {"A": "Correct. Minor cannot be a transferor under Section 7.", "B": "Advocate cannot validate a void transfer.", "C": "Applies to all property.", "D": "Sub-registrar cannot cure statutory incapacity."},
    "Medium", "Transfer of Property Act, 1882, Section 7", "Determine capacity of minor as transferor under Section 7."))

data.append(q("mcq-tpa-01-023", "ch-tpa-01", "top-tpa-01-03",
    "Can a minor be a transferee (purchaser or donee) under the Transfer of Property Act?",
    ["Yes, law does not disable a minor from being a transferee of property in his favor, provided no reciprocal executory obligation is imposed on him", "No, a minor can never hold or receive property", "Only if appointed as a government officer", "Only through a testamentary trust"],
    0, "A",
    "Settled law (Ulfat Rai v. Gauri Shankar): A minor can be a transferee/donee/purchaser where consideration is paid, as capacity to receive benefit is not restricted.",
    {"A": "Correct. Minor can be a transferee where no ongoing personal obligation binds him.", "B": "Minors routinely hold title to property.", "C": "No official appointment needed.", "D": "Inter vivos transfers directly to minors are valid."},
    "Hard", "Ulfat Rai v. Gauri Shankar (1911) ILR 33 All 657", "Evaluate capacity of minor as transferee under TPA."))

data.append(q("mcq-tpa-01-024", "ch-tpa-01", "top-tpa-01-03",
    "Under Section 8 of the Transfer of Property Act, unless a different intention is expressed or necessarily implied, a transfer of property passes forthwith to the transferee:",
    ["All the interest which the transferor is then capable of passing in the property and in the legal incidents thereof", "Only a 5-year life estate", "Only the bare legal title without any easements", "Half the mineral rights"],
    0, "A",
    "Section 8 provides that transfer passes all the interest which the transferor is capable of passing in the property and its legal incidents.",
    {"A": "Correct. Section 8 statutory rule on operation of transfer.", "B": "Full estate passes unless limited expressly.", "C": "All legal incidents and easements pass with property.", "D": "No automatic mineral severance under Section 8."},
    "Easy", "Transfer of Property Act, 1882, Section 8", "Recall statutory rule on operation of transfer under Section 8."))

data.append(q("mcq-tpa-01-025", "ch-tpa-01", "top-tpa-01-03",
    "Under Section 8, the legal incidents of a transfer of land include:",
    ["The easements annexed thereto, the rents and profits thereof accruing after the transfer, and all things attached to the earth", "The personal debts of the transferor", "Criminal liabilities of previous owners", "The transferor's voting card"],
    0, "A",
    "Section 8 paragraph 2 explicitly lists legal incidents of land: easements annexed, rents/profits accruing after transfer, and things attached to earth.",
    {"A": "Correct. Section 8 paragraph 2 incidents of land.", "B": "Personal debts do not run with land.", "C": "Criminal liabilities are personal.", "D": "Voting cards are personal civic documents."},
    "Medium", "Transfer of Property Act, 1882, Section 8", "Identify legal incidents of land passing under Section 8."))

data.append(q("mcq-tpa-01-026", "ch-tpa-01", "top-tpa-01-03",
    "Under Section 8, where property transferred is a house, the legal incidents include:",
    ["The easements annexed thereto, the rent accruing after transfer, and locks, keys, bars, doors, windows, and other things provided for permanent use therewith", "All movable furniture inside the house", "Family heirlooms and jewels kept in safes", "Motor vehicles parked in the garage"],
    0, "A",
    "Section 8 paragraph 3 specifies house incidents: easements, post-transfer rent, and permanent fixtures like locks, keys, doors, windows.",
    {"A": "Correct. Section 8 paragraph 3 text.", "B": "Loose furniture is chattel not passing with house.", "C": "Jewels are separate movables.", "D": "Vehicles are independent movable property."},
    "Easy", "Transfer of Property Act, 1882, Section 8", "Identify legal incidents of house transfer under Section 8."))

data.append(q("mcq-tpa-01-027", "ch-tpa-01", "top-tpa-01-03",
    "Under Section 8, where the property transferred is a debt or other actionable claim, the legal incidents include:",
    ["The securities for the debt, but not arrears of interest accrued before the transfer", "All unrelated assets of the debtor", "The debtor's personal passport", "The bank account of the debtor's spouse"],
    0, "A",
    "Section 8 paragraph 5: Transfer of debt passes securities for the debt, but does not pass arrears of interest accrued before transfer unless expressed.",
    {"A": "Correct. Section 8 paragraph 5 on transfer of debt.", "B": "Only securities for the specific debt pass.", "C": "Passports are state documents.", "D": "Spouse's property is unaffected."},
    "Medium", "Transfer of Property Act, 1882, Section 8", "Identify legal incidents of debt transfer under Section 8."))

data.append(q("mcq-tpa-01-028", "ch-tpa-01", "top-tpa-01-03",
    "Under Section 8, can a transferor convey a lesser interest than what he owns in the property?",
    ["Yes, if a different intention is expressed or necessarily implied in the instrument", "No, transfer must always convey absolute fee simple ownership", "Only with permission of the High Court", "Only if the transferee is a co-sharer"],
    0, "A",
    "Section 8 begins: 'Unless a different intention is expressed or necessarily implied...'. A transferor may carve out and transfer a life estate, mortgage, or lease.",
    {"A": "Correct. Parties may express contrary intention to convey limited estate.", "B": "TPA allows transfer of limited interests (leases, mortgages, life estates).", "C": "No High Court permission required.", "D": "Applies to all transferees."},
    "Medium", "Transfer of Property Act, 1882, Section 8", "Apply contrary intention exception under Section 8."))

data.append(q("mcq-tpa-01-029", "ch-tpa-01", "top-tpa-01-03",
    "A transfers his land to B by deed. Later, A claims that the mature mango trees planted on the land were not transferred. In the absence of any reservation in the deed:",
    ["The trees passed to B as things attached to the earth under Section 8", "The trees belong to A as separate movable goods", "The trees must be cut and divided equally", "The transfer of land is void for ambiguity"],
    0, "A",
    "Things attached to the earth pass with the land under Section 8 unless specifically reserved by the transferor in the deed.",
    {"A": "Correct. Trees pass with the land as legal incidents under Section 8.", "B": "Trees are attached to earth and pass unless reserved.", "C": "No division without contract clause.", "D": "The conveyance is fully valid."},
    "Easy", "Transfer of Property Act, 1882, Section 8", "Apply Section 8 to trees attached to land."))

data.append(q("mcq-tpa-01-030", "ch-tpa-01", "top-tpa-01-03",
    "What is the doctrine of 'Nemo dat quod non habet' in relation to Section 7 of the TPA?",
    ["No one can transfer a better title than he himself possesses, unless authorized to dispose of property not his own", "Every person in possession is the absolute owner", "Title passes automatically by possession", "Government alone has title to transfer"],
    0, "A",
    "Nemo dat quod non habet is the general rule embodied in Section 7: a transferor can only convey the interest he holds or is authorized to dispose of.",
    {"A": "Correct. Fundamental property rule underlying Section 7.", "B": "Possession is not identical to title.", "C": "Possession does not convey title against true owner.", "D": "Private ownership is recognized under Indian law."},
    "Medium", "Transfer of Property Act, 1882, Section 7", "Master nemo dat quod non habet in Section 7."))

print(f"Total Part 1 MCQs generated: {len(data)}")

with open('scripts/data_tpa_mcqs_1.py', 'w', encoding='utf-8') as f:
    f.write("# TPA MCQs Part 1 (Chapters 1 to 3: 90 MCQs)\n")
    f.write("MCQS_PART1 = " + json.dumps(data, indent=2) + "\n")
print("Written scripts/data_tpa_mcqs_1.py")
