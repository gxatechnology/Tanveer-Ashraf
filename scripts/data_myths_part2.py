# Part 2: BSA 2023 (35), IEA vs BSA (20), BNSS 2023 (30), CPC 1908 (35) = 120 items

U_BSA = "https://www.indiacode.nic.in/handle/123456789/20064"
U_BNSS = "https://www.indiacode.nic.in/handle/123456789/20063"
U_CPC = "https://www.indiacode.nic.in/handle/123456789/2191"
U_SC = "https://main.sci.gov.in/judgments"

def get_part2_items(m):
    # ---------------------------------------------------------
    # 4. BHARATIYA SAKSHYA ADHINIYAM (BSA) 2023 (35 items)
    # ---------------------------------------------------------
    m("Electronic and digital records are treated on par with traditional paper documents as primary evidence under Section 57 of the BSA, 2023.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Sections 57 & 61", None,
      "Section 57 Explanation 5 to 7 and Section 61 BSA explicitly establish that electronic or digital records produced from computers or devices shall have the same legal effect as paper documents and can constitute primary evidence when stored/transmitted simultaneously.",
      "Under old IEA 65B, electronic records were strictly secondary evidence requiring complex certificate hurdles.",
      "Section 63 outlines admissibility conditions and the new certificate requirement.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Electronic Evidence", "Section 57", "Section 61", "BSA 2023", "Primary Evidence"])

    m("The mandatory certificate for proving electronic records in court is now governed by Section 63 of the BSA, 2023.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 63", None,
      "Section 63 BSA replaces Section 65B of the Indian Evidence Act, 1872 for the admissibility of electronic records.",
      "A statutory certificate in the form set out in the Schedule to BSA is required at the time of presenting evidence.",
      "Certificate can be signed by the person in charge of the computer device or an expert.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Section 63", "Certificate", "Electronic Records", "IEA 65B", "BSA 2023"])

    m("Under Section 24 of the BSA, a confession made by a co-accused who is absconding can be considered against other co-accused facing joint trial.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "intermediate", "Bharatiya Sakshya Adhiniyam, 2023", "Section 24", None,
      "Section 24 Explanation II of the BSA, 2023 explicitly provides that where a person facing joint trial has absconded or fails to comply with a proclamation under BNSS 84, the joint trial proceeds and their confession may be taken into consideration.",
      "Under old IEA Section 30, an absconding accused was not being 'jointly tried', preventing use of their confession.",
      "It remains weak evidence requiring independent corroboration.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Section 24", "Co-accused Confession", "Absconding", "Joint Trial", "BSA 2023"],
      {"oldAct": "IEA 1872", "oldSection": "30", "newAct": "BSA 2023", "newSection": "24", "substantiveChange": "Explanation II added allowing consideration of confession even if co-accused has absconded."})

    m("An accomplice is an incompetent witness against an accused person under the Bharatiya Sakshya Adhiniyam, 2023.",
      "false", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 138", None,
      "Section 138 BSA (old IEA 133) explicitly provides that an accomplice shall be a competent witness against an accused person, and a conviction is not illegal merely because it proceeds upon uncorroborated testimony.",
      "Laypersons assume criminals or accomplices cannot testify in court as witnesses.",
      "Section 119 illustration (b) BSA (old 114(b)) cautions that an accomplice is unworthy of credit unless corroborated in material particulars.",
      "is an incompetent witness against an accused person", "is a competent witness against an accused person under Section 138",
      U_BSA, "Current Law (in force from July 1, 2024)", ["Accomplice", "Section 138", "Competent Witness", "Corroboration", "BSA 2023"])

    m("The law of evidence requires a minimum of two eyewitnesses to prove any criminal charge in court.",
      "false", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 139", None,
      "Section 139 BSA (old IEA 134) establishes the golden rule: 'No particular number of witnesses shall in any case be required for the proof of any fact.' Evidence is weighed, not counted (Vadivelu Thevar v. State of Madras).",
      "Citizens and young candidates frequently assume multi-witness corroboration is legally mandatory.",
      "Testimony of a single wholly reliable eyewitness is sufficient for conviction even in capital cases.",
      "requires a minimum of two eyewitnesses to prove any criminal charge", "requires no particular number of witnesses under Section 139",
      U_BSA, "Current Law (in force from July 1, 2024)", ["Number of Witnesses", "Section 139", "Vadivelu Thevar", "Sole Witness", "BSA 2023"])

    m("A dying declaration is admissible in evidence without administration of oath or cross-examination under Section 26(a) of the BSA.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 26(a)", None,
      "Section 26(a) BSA (old IEA 32(1)) creates a statutory exception to the hearsay rule for statements made by a person as to cause of death or circumstances of transaction resulting in death.",
      "Based on the maxim 'nemo moriturus praesumitur mentiri' (a man will not meet his maker with a lie in his mouth).",
      "Can form the sole basis of conviction if found truthful, voluntary, and unprompted (Laxman v. State of Maharashtra).",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Dying Declaration", "Section 26(a)", "Hearsay Exception", "Laxman", "BSA 2023"])

    m("The opinion of an expert upon a point of foreign law, science, art, or finger impressions is relevant under Section 39 of the BSA, 2023.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 39", None,
      "Section 39 BSA (old IEA 45) makes opinions of specially skilled persons relevant on questions of foreign law, science, art, identity of handwriting, or finger impressions.",
      "Expert opinion is advisory in nature and does not bind the court automatically.",
      "Court must independently evaluate the underlying scientific data.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Expert Opinion", "Section 39", "Scientific Evidence", "IEA 45", "BSA 2023"])

    m("Leading questions may be asked freely in examination-in-chief without permission of the Court.",
      "false", "Bharatiya Sakshya Adhiniyam, 2023", "intermediate", "Bharatiya Sakshya Adhiniyam, 2023", "Section 146", None,
      "Under Section 146(1) BSA (old IEA 142), leading questions must not, if objected to by the adverse party, be asked in examination-in-chief or in re-examination, except with permission of the Court.",
      "Court permits leading questions in examination-in-chief only as to introductory matters or undisputed facts.",
      "Leading questions may be asked as of right in cross-examination (Section 146(2) BSA).",
      "may be asked freely in examination-in-chief without permission of the Court", "must not be asked in examination-in-chief if objected to, except with court permission",
      U_BSA, "Current Law (in force from July 1, 2024)", ["Leading Questions", "Section 146", "Examination in Chief", "Cross-examination", "BSA 2023"])

    m("Leading questions may be asked by the adverse party as of right in cross-examination under Section 146(2) of the BSA.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 146(2)", None,
      "Section 146(2) BSA (old IEA 143) provides that leading questions may be asked in cross-examination.",
      "Cross-examination aims to test veracity and impeach credibility, making leading questions essential.",
      "The court can restrain questions that are indecent, scandalous, or intended to insult (Section 151/152 BSA).",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Leading Questions", "Section 146(2)", "Cross-examination", "Evidence", "BSA 2023"])

    m("Under Section 157 of the BSA, the party calling a witness may be permitted by the Court to put any questions which might be put in cross-examination.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "intermediate", "Bharatiya Sakshya Adhiniyam, 2023", "Section 157", None,
      "Section 157 BSA (old IEA 154) governs hostile witnesses, empowering the court in its discretion to permit the caller to cross-examine their own witness.",
      "Hostile witness testimony is not automatically discarded in toto; portions supporting either prosecution or defence can be relied upon (Sat Paul v. Delhi Administration).",
      "Discretion must be exercised judiciously.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Hostile Witness", "Section 157", "Cross-examination", "IEA 154", "BSA 2023"])

    m("Communications between an advocate and their client made in the course of professional employment are privileged under Section 132 of the BSA.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "intermediate", "Bharatiya Sakshya Adhiniyam, 2023", "Section 132", None,
      "Section 132 BSA (old IEA 126) provides professional privilege protecting communications between legal advisers and clients from disclosure without express consent.",
      "Privilege does not protect communications made in furtherance of any illegal purpose or observing crimes/frauds committed during employment.",
      "Privilege continues even after employment has ceased.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Professional Privilege", "Section 132", "Advocate Client", "IEA 126", "BSA 2023"])

    m("A Trial Judge has the power under Section 168 of the BSA to ask any question at any time to any witness about any fact.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 168", None,
      "Section 168 BSA (old IEA 165) gives the judge expansive powers to discover or obtain proper proof of relevant facts, asking questions in any form, at any time, about any fact relevant or irrelevant.",
      "A trial judge in India is not a passive spectator or mere umpire.",
      "Judgment must be based only on facts declared relevant and duly proved.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Judge Power", "Section 168", "Questioning Witness", "IEA 165", "BSA 2023"])

    m("Under Section 118 of the BSA, where a woman dies of dowry death within 7 years of marriage, the Court has discretion whether or not to presume the husband caused it.",
      "false", "Bharatiya Sakshya Adhiniyam, 2023", "intermediate", "Bharatiya Sakshya Adhiniyam, 2023", "Section 118", None,
      "Section 118 BSA (old IEA 113B) uses the mandatory phrase 'the Court shall presume', making it a mandatory presumption of law upon proof of cruelty soon before death.",
      "Candidates confuse discretionary presumptions ('may presume') with mandatory presumptions ('shall presume').",
      "Rebuttable by the defence by establishing contrary evidence.",
      "the Court has discretion whether or not to presume", "the Court is statutorily mandated to presume ('shall presume')",
      U_BSA, "Current Law (in force from July 1, 2024)", ["Dowry Death Presumption", "Section 118", "Shall Presume", "IEA 113B", "BSA 2023"])

    m("Under Section 117 of the BSA, the Court may presume abetment of suicide by a married woman if she committed suicide within seven years of marriage.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "intermediate", "Bharatiya Sakshya Adhiniyam, 2023", "Section 117", None,
      "Section 117 BSA (old IEA 113A) provides that the court 'may presume' abetment of suicide where a woman commits suicide within 7 years of marriage and cruelty is shown.",
      "Distinguished from Section 118 (dowry death) which uses 'shall presume'.",
      "Court retains discretion having regard to all circumstances.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Suicide Presumption", "Section 117", "May Presume", "Seven Years", "BSA 2023"])

    m("Under Section 109 of the BSA, when any fact is especially within the knowledge of any person, the burden of proving that fact is upon that person.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 109", None,
      "Section 109 BSA (old IEA 106) embodies the special knowledge rule (e.g., ticket in train travel, events inside matrimonial bedroom at night).",
      "Section 109 does not relieve the prosecution of proving its prima facie case beyond reasonable doubt.",
      "Applies only to facts especially within the private knowledge of the accused.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Burden of Proof", "Section 109", "Special Knowledge", "IEA 106", "BSA 2023"])

    m("Facts which, though not in issue, are so connected with a fact in issue as to form part of the same transaction, are relevant under Section 4 of the BSA.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 4", None,
      "Section 4 BSA (old IEA 6) codifies the common law doctrine of Res Gestae: facts forming part of the same transaction are relevant whether they occurred at the same time and place or at different times and places.",
      "Spontaneous statements uttered contemporaneously with the event are admissible as res gestae.",
      "Fabricated or narrative afterthoughts are excluded.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Res Gestae", "Section 4", "Same Transaction", "IEA 6", "BSA 2023"])

    m("Evidence of motive, preparation, and previous or subsequent conduct is relevant under Section 6 of the BSA, 2023.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 6", None,
      "Section 6 BSA (old IEA 8) makes any fact relevant which shows or constitutes a motive or preparation for any fact in issue, or relevant conduct of parties or agents.",
      "Conduct must be directly influenced by facts in issue.",
      "Statements accompanying and explaining conduct are relevant.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Motive", "Preparation", "Conduct", "Section 6", "BSA 2023"])

    m("Test Identification Parade (TIP) facts necessary to establish the identity of any person or thing are relevant under Section 7 of the BSA, 2023.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 7", None,
      "Section 7 BSA (old IEA 9) makes facts necessary to explain or introduce relevant facts, or support/rebut inferences, or establish identity, relevant.",
      "Substantive evidence is identification in court; TIP in investigation is corroborative.",
      "Unexplained delay in holding TIP weakens its evidentiary value.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Identification Parade", "Section 7", "Identity", "IEA 9", "BSA 2023"])

    m("An admission can always be proved by or on behalf of the person who made it as a general rule.",
      "false", "Bharatiya Sakshya Adhiniyam, 2023", "intermediate", "Bharatiya Sakshya Adhiniyam, 2023", "Section 19", None,
      "Under Section 19 BSA (old IEA 21), admissions are relevant and may be proved against the person who makes them, but cannot be proved by or on behalf of the person who made them, subject to 3 narrow exceptions.",
      "Self-serving statements are inadmissible; only self-harming admissions are admissible.",
      "Exceptions include dying declarations, statements of bodily feeling in good faith, or if relevant otherwise than as admission.",
      "can always be proved by or on behalf of the person who made it", "can only be proved against the person who made it, not on their own behalf",
      U_BSA, "Current Law (in force from July 1, 2024)", ["Admissions", "Section 19", "Self-harming", "IEA 21", "BSA 2023"])

    m("A confession made to a police officer of any rank is completely admissible in evidence without any recovery.",
      "false", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 23(1)", None,
      "Section 23(1) BSA (old IEA 25) strictly mandates that no confession made to a police officer shall be proved as against a person accused of any offence.",
      "An absolute bar enacted to eliminate third-degree torture in police custody.",
      "Only so much as relates distinctly to a fact discovered thereby is admissible under Section 23(2) proviso (old IEA 27).",
      "is completely admissible in evidence without any recovery", "is strictly inadmissible under Section 23(1) to protect against custodial coercion",
      U_BSA, "Current Law (in force from July 1, 2024)", ["Police Confession", "Section 23", "Inadmissible", "Custodial Torture", "BSA 2023"])

    m("Under Section 23(2) of the BSA, so much of information received from an accused in police custody as relates distinctly to the fact thereby discovered may be proved.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 23(2)", None,
      "Section 23(2) BSA proviso (old IEA 27 / Pulukuri Kottaya doctrine) confirms that when any fact is discovered in consequence of information received from an accused in custody, that distinct portion is admissible.",
      "Recovery of the physical object confirms the truth of that specific part of the confession.",
      "Inculpatory confessions of past guilt remain excluded.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Recovery Statement", "Section 23(2)", "Fact Discovered", "Pulukuri Kottaya", "BSA 2023"])

    m("The doctrine of Estoppel can be pleaded against a mandatory statutory enactment.",
      "false", "Bharatiya Sakshya Adhiniyam, 2023", "intermediate", "Bharatiya Sakshya Adhiniyam, 2023", "Section 121", None,
      "It is a well-settled principle of Indian law that there can be no estoppel against a statute or against the legislature exercising sovereign legislative power (M.P. Sugar Mills / Olga Tellis).",
      "Litigants often argue government promises override statutory mandates.",
      "Promissory estoppel binds the executive on administrative assurances where no statutory violation occurs.",
      "can be pleaded against a mandatory statutory enactment", "cannot be pleaded against a statute as law overrides private representations",
      U_BSA, "Current Law (in force from July 1, 2024)", ["Estoppel", "Section 121", "No Estoppel Against Statute", "Public Policy", "BSA 2023"])

    m("Courts in India are bound to take Judicial Notice of all laws in force in India under Section 52 of the BSA, 2023.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 52(1)", None,
      "Section 52(1)(a) BSA (old IEA 57) mandates that the Court shall take judicial notice of all laws in force in the territory of India, meaning domestic statutes need not be proved by evidence.",
      "Customs and foreign laws must be proved as facts by evidence.",
      "Section 51 BSA provides that facts of which the court takes judicial notice need not be proved.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Judicial Notice", "Section 52", "Domestic Law", "Section 51", "BSA 2023"])

    m("Under Section 53 of the BSA, facts admitted by parties or their agents need not be proved at the hearing.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 53", None,
      "Section 53 BSA (old IEA 58) provides that no fact need be proved in any proceeding which the parties or their agents agree to admit at the hearing.",
      "The court may in its discretion require admitted facts to be proved otherwise than by such admissions.",
      "Judicial admissions in pleadings dispense with formal proof.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Admitted Facts", "Section 53", "Pleadings", "Proof Dispensed", "BSA 2023"])

    m("Secondary evidence is admissible when the original document is shown to be lost or destroyed under Section 60 of the BSA.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 60", None,
      "Section 60 BSA (old IEA 65) enumerates cases in which secondary evidence may be given: when the original is in possession of adversary, lost or destroyed, or a public document.",
      "Loss of original must be proved before secondary evidence is led.",
      "Certified copies are admissible for public documents.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Secondary Evidence", "Section 60", "Lost Document", "IEA 65", "BSA 2023"])

    m("Oral evidence must in all cases whatever be direct under Section 55 of the BSA, 2023.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 55", None,
      "Section 55 BSA (old IEA 60) establishes the fundamental exclusionary rule against hearsay: if oral evidence refers to a fact which could be seen, it must be the evidence of a witness who says he saw it.",
      "Excludes second-hand hearsay reports.",
      "Subject to statutory exceptions like dying declarations and res gestae.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Direct Evidence", "Section 55", "Hearsay Exclusion", "IEA 60", "BSA 2023"])

    m("Hearsay evidence is generally admissible in Indian courts without any statutory exceptions.",
      "false", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 55", None,
      "Hearsay evidence is strictly inadmissible as a general rule because it is not on oath, not subject to cross-examination, and lacks personal responsibility (Kalyan Kumar Gogoi v. Ashutosh Agnihotri).",
      "Laypersons think rumors and third-party reports can be recounted in court.",
      "Only specific statutory exceptions like Section 4 (res gestae) and Section 26 (dying declaration) permit hearsay.",
      "is generally admissible in Indian courts without any statutory exceptions", "is strictly excluded under Section 55 subject to narrow statutory exceptions",
      U_BSA, "Current Law (in force from July 1, 2024)", ["Hearsay Inadmissible", "Section 55", "Rule of Evidence", "Kalyan Kumar Gogoi", "BSA 2023"])

    m("When the terms of a contract have been reduced to the form of a document, oral evidence is excluded under Section 94 of the BSA.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "intermediate", "Bharatiya Sakshya Adhiniyam, 2023", "Section 94", None,
      "Section 94 BSA (old IEA 91) embodies the best evidence rule: no evidence shall be given in proof of the terms of a written contract except the document itself or secondary evidence where admissible.",
      "Section 95 BSA (old IEA 92) further excludes oral agreement to contradict, vary, add to or subtract from its terms.",
      "Exceptions exist for fraud, illegality, failure of consideration, and subsequent oral rescission.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Best Evidence Rule", "Section 94", "Section 95", "Written Contract", "BSA 2023"])

    m("Oral evidence is admissible to clear a latent ambiguity in a document under Section 98 of the BSA, 2023.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "intermediate", "Bharatiya Sakshya Adhiniyam, 2023", "Section 98", None,
      "Section 98 BSA (old IEA 95/97) permits extrinsic oral evidence to explain language that is unmeaning in reference to existing facts or where language applies partly to one set of facts and partly to another (latent ambiguity).",
      "Distinguished from patent ambiguity on the face of the document.",
      "Helps establish the true application of clear language to ambiguous facts.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Latent Ambiguity", "Section 98", "Extrinsic Evidence", "IEA 95", "BSA 2023"])

    m("Oral evidence is admissible to cure a patent ambiguity apparent on the face of a document under Section 96 of the BSA.",
      "false", "Bharatiya Sakshya Adhiniyam, 2023", "intermediate", "Bharatiya Sakshya Adhiniyam, 2023", "Section 96", None,
      "Section 96 BSA (old IEA 93) strictly provides that when the language used in a document is on its face ambiguous or defective (patent ambiguity), evidence may not be given of facts which would show its meaning.",
      "Litigants think any document drafting defect can be remedied by witness testimony.",
      "Court cannot rewrite an incomprehensible or blank document for the parties.",
      "is admissible to cure a patent ambiguity apparent on the face of a document", "is strictly inadmissible to cure patent ambiguity on the face of the document",
      U_BSA, "Current Law (in force from July 1, 2024)", ["Patent Ambiguity", "Section 96", "Defective Language", "IEA 93", "BSA 2023"])

    m("Birth during marriage is conclusive proof of legitimacy under Section 116 of the BSA, 2023 unless non-access is established.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "intermediate", "Bharatiya Sakshya Adhiniyam, 2023", "Section 116", None,
      "Section 116 BSA (old IEA 112) provides that the fact that any person was born during the continuance of a valid marriage between his mother and any man is conclusive proof that he is legitimate, unless non-access is proved.",
      "DNA testing can rebut the presumption only when non-access or strong scientific doubt is established under judicial directions (Nandlal Wasudeo Badwaik).",
      "Conclusive proof cannot be rebutted by ordinary balance of probabilities.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Legitimacy Presumption", "Section 116", "Conclusive Proof", "Non-access", "BSA 2023"])

    m("A witness may refresh their memory by referring to any writing made by themselves at the time of the transaction under Section 162 of the BSA.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 162", None,
      "Section 162 BSA (old IEA 159) allows a witness under examination to refresh his memory by referring to any writing made by himself at the time of the transaction or soon afterwards.",
      "Adverse party has the right to inspect the document and cross-examine the witness on it (Section 164 BSA).",
      "Expert witnesses may refresh memory by scientific treatises.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Refreshing Memory", "Section 162", "Contemporaneous Writing", "IEA 159", "BSA 2023"])

    m("The credit of a witness can be impeached by the adverse party under Section 158 of the BSA, 2023.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 158", None,
      "Section 158 BSA (old IEA 155) enumerates methods of impeaching credit: testimony of persons who believe the witness unworthy of credit, proof of corrupt inducement, or proof of former inconsistent statements.",
      "Essential cross-examination tool in criminal trials.",
      "Rape prosecutrix general immoral character cannot be questioned (Section 149(4) BSA).",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Impeaching Credit", "Section 158", "Inconsistent Statements", "IEA 155", "BSA 2023"])

    m("In order to corroborate the testimony of a witness, any former statement made by such witness relating to the same fact is admissible under Section 160 of the BSA.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "intermediate", "Bharatiya Sakshya Adhiniyam, 2023", "Section 160", None,
      "Section 160 BSA (old IEA 157) permits any former statement made by a witness relating to the same fact at or about the time when the fact took place to be proved to corroborate testimony in court.",
      "FIR can be used to corroborate or contradict the informant who lodged it.",
      "Former statement is not substantive evidence on its own.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Corroboration", "Section 160", "Former Statement", "FIR", "BSA 2023"])

    m("An admission made in civil cases under an express condition that evidence of it is not to be given is inadmissible under Section 21 of the BSA.",
      "true", "Bharatiya Sakshya Adhiniyam, 2023", "intermediate", "Bharatiya Sakshya Adhiniyam, 2023", "Section 21", None,
      "Section 21 BSA (old IEA 23) embodies the 'without prejudice' communication privilege in civil cases, ensuring settlements can be explored without fear of admissions being used in trial.",
      "Does not exempt any advocate from giving evidence of matter under Section 132.",
      "Applies only to civil proceedings.",
      None, None,
      U_BSA, "Current Law (in force from July 1, 2024)", ["Without Prejudice", "Section 21", "Civil Admissions", "Settlement", "BSA 2023"])

    # ---------------------------------------------------------
    # 5. HISTORICAL IEA VS BSA TRANSITIONS (20 items)
    # ---------------------------------------------------------
    m("Section 65B of the Indian Evidence Act, 1872 regarding electronic evidence certification has been relocated to Section 63 of the BSA, 2023.",
      "true", "Historical IEA vs BSA Transitions", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 63", None,
      "Old IEA Section 65B corresponds to Section 63 of the BSA, 2023.",
      "Anjum v. State and Arjun Panditrao precedents on electronic certificates are now applied under Section 63 BSA.",
      "Certificate format is officially scheduled in the Adhiniyam.",
      None, None,
      U_BSA, "Transition (July 1, 2024)", ["IEA 65B", "BSA 63", "Electronic Certificate", "Statutory Transition"],
      {"oldAct": "IEA 1872", "oldSection": "65B", "newAct": "BSA 2023", "newSection": "63", "substantiveChange": "Electronic certificate requirement relocated from IEA 65B to BSA 63."})

    m("Section 27 of the Indian Evidence Act (Information received from accused) is now incorporated as the proviso to Section 23(2) of the BSA, 2023.",
      "true", "Historical IEA vs BSA Transitions", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 23(2)", None,
      "Old IEA Section 27 has been incorporated into the proviso to Section 23(2) of the BSA, 2023.",
      "Allows discovery of facts in consequence of information received from accused in police custody.",
      "Maintains the classic Pulukuri Kottaya doctrine.",
      None, None,
      U_BSA, "Transition (July 1, 2024)", ["IEA 27", "BSA 23(2)", "Discovery of Fact", "Statutory Transition"],
      {"oldAct": "IEA 1872", "oldSection": "27", "newAct": "BSA 2023", "newSection": "23(2)", "substantiveChange": "Section 27 IEA integrated as proviso to Section 23(2) BSA."})

    m("The dying declaration provision, historically Section 32(1) of the IEA, is now codified in Section 26(a) of the BSA, 2023.",
      "true", "Historical IEA vs BSA Transitions", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 26(a)", None,
      "Old IEA Section 32(1) corresponds directly to Section 26(a) of the BSA, 2023.",
      "Statements by persons who cannot be called as witnesses are in Section 26 BSA.",
      "Dying declaration remains primary hearsay exception.",
      None, None,
      U_BSA, "Transition (July 1, 2024)", ["IEA 32(1)", "BSA 26(a)", "Dying Declaration", "Statutory Transition"],
      {"oldAct": "IEA 1872", "oldSection": "32(1)", "newAct": "BSA 2023", "newSection": "26(a)", "substantiveChange": "Dying declaration relocated from IEA 32(1) to BSA 26(a)."})

    m("Presumption as to absence of consent in certain prosecutions for rape, formerly Section 114A of the IEA, is now Section 119 of the BSA, 2023.",
      "true", "Historical IEA vs BSA Transitions", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 119", None,
      "Old IEA Section 114A corresponds directly to Section 119 of the BSA, 2023.",
      "Where sexual intercourse is proved and woman states in court she did not consent, court shall presume absence of consent.",
      "Mandatory statutory presumption.",
      None, None,
      U_BSA, "Transition (July 1, 2024)", ["IEA 114A", "BSA 119", "Consent Presumption", "Statutory Transition"],
      {"oldAct": "IEA 1872", "oldSection": "114A", "newAct": "BSA 2023", "newSection": "119", "substantiveChange": "Presumption of absence of consent in rape relocated from IEA 114A to BSA 119."})

    m("The presumption as to dowry death, formerly Section 113B of the IEA, is now found in Section 118 of the BSA, 2023.",
      "true", "Historical IEA vs BSA Transitions", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 118", None,
      "Old IEA Section 113B corresponds directly to Section 118 of the BSA, 2023.",
      "Mandatory 'shall presume' applies upon showing cruelty soon before death within 7 years of marriage.",
      "Linked to BNS Section 79.",
      None, None,
      U_BSA, "Transition (July 1, 2024)", ["IEA 113B", "BSA 118", "Dowry Death Presumption", "Statutory Transition"],
      {"oldAct": "IEA 1872", "oldSection": "113B", "newAct": "BSA 2023", "newSection": "118", "substantiveChange": "Dowry death presumption relocated from IEA 113B to BSA 118."})

    m("The conclusive presumption of legitimacy of a child born during wedlock, previously Section 112 of the IEA, is now Section 116 of the BSA, 2023.",
      "true", "Historical IEA vs BSA Transitions", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 116", None,
      "Old IEA Section 112 corresponds directly to Section 116 of the BSA, 2023.",
      "Rebuttable only by proof of non-access.",
      "Protects child from stigma of illegitimacy.",
      None, None,
      U_BSA, "Transition (July 1, 2024)", ["IEA 112", "BSA 116", "Legitimacy", "Statutory Transition"],
      {"oldAct": "IEA 1872", "oldSection": "112", "newAct": "BSA 2023", "newSection": "116", "substantiveChange": "Legitimacy presumption relocated from IEA 112 to BSA 116."})

    m("The rule of Estoppel, previously codified under Section 115 of the IEA, is now codified under Section 121 of the BSA, 2023.",
      "true", "Historical IEA vs BSA Transitions", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 121", None,
      "Old IEA Section 115 corresponds directly to Section 121 of the BSA, 2023.",
      "Precludes a person who intentionally caused another to believe a thing from denying its truth.",
      "Sections 122 and 123 govern tenant and bailee estoppels.",
      None, None,
      U_BSA, "Transition (July 1, 2024)", ["IEA 115", "BSA 121", "Estoppel", "Statutory Transition"],
      {"oldAct": "IEA 1872", "oldSection": "115", "newAct": "BSA 2023", "newSection": "121", "substantiveChange": "Doctrine of estoppel relocated from IEA 115 to BSA 121."})

    m("Competency of an accomplice as a witness, previously Section 133 of the IEA, is now Section 138 of the BSA, 2023.",
      "true", "Historical IEA vs BSA Transitions", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 138", None,
      "Old IEA Section 133 corresponds directly to Section 138 of the BSA, 2023.",
      "Accomplice is competent witness against co-accused.",
      "Corroboration rule in Section 119(b) BSA.",
      None, None,
      U_BSA, "Transition (July 1, 2024)", ["IEA 133", "BSA 138", "Accomplice Competence", "Statutory Transition"],
      {"oldAct": "IEA 1872", "oldSection": "133", "newAct": "BSA 2023", "newSection": "138", "substantiveChange": "Accomplice witness competency relocated from IEA 133 to BSA 138."})

    m("The principle that no particular number of witnesses is required, previously Section 134 of the IEA, is now Section 139 of the BSA, 2023.",
      "true", "Historical IEA vs BSA Transitions", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 139", None,
      "Old IEA Section 134 corresponds directly to Section 139 of the BSA, 2023.",
      "Quality of evidence over quantity.",
      "Sole credible witness principle upheld.",
      None, None,
      U_BSA, "Transition (July 1, 2024)", ["IEA 134", "BSA 139", "Number of Witnesses", "Statutory Transition"],
      {"oldAct": "IEA 1872", "oldSection": "134", "newAct": "BSA 2023", "newSection": "139", "substantiveChange": "No particular number of witnesses rule relocated from IEA 134 to BSA 139."})

    m("Cross-examination as to previous statements in writing, previously Section 145 of the IEA, is now Section 148 of the BSA, 2023.",
      "true", "Historical IEA vs BSA Transitions", "intermediate", "Bharatiya Sakshya Adhiniyam, 2023", "Section 148", None,
      "Old IEA Section 145 corresponds directly to Section 148 of the BSA, 2023.",
      "Contradicting a witness by their previous statement in writing requires drawing attention to parts to contradict.",
      "Crucial for using police statements under BNSS 180 (old CrPC 161).",
      None, None,
      U_BSA, "Transition (July 1, 2024)", ["IEA 145", "BSA 148", "Previous Statements", "Contradiction", "Statutory Transition"],
      {"oldAct": "IEA 1872", "oldSection": "145", "newAct": "BSA 2023", "newSection": "148", "substantiveChange": "Cross-examination on previous statements relocated from IEA 145 to BSA 148."})

    m("The provision regarding hostile witnesses, previously Section 154 of the IEA, is now Section 157 of the BSA, 2023.",
      "true", "Historical IEA vs BSA Transitions", "intermediate", "Bharatiya Sakshya Adhiniyam, 2023", "Section 157", None,
      "Old IEA Section 154 corresponds directly to Section 157 of the BSA, 2023.",
      "Permits party calling witness to put cross-examination questions.",
      "Preserves the 2006 amendment regarding relying on favorable parts.",
      None, None,
      U_BSA, "Transition (July 1, 2024)", ["IEA 154", "BSA 157", "Hostile Witness", "Statutory Transition"],
      {"oldAct": "IEA 1872", "oldSection": "154", "newAct": "BSA 2023", "newSection": "157", "substantiveChange": "Hostile witness cross-examination relocated from IEA 154 to BSA 157."})

    m("The Judge's power to put questions and order production, previously Section 165 of the IEA, is now Section 168 of the BSA, 2023.",
      "true", "Historical IEA vs BSA Transitions", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 168", None,
      "Old IEA Section 165 corresponds directly to Section 168 of the BSA, 2023.",
      "Affords broad judicial inquiry powers to discover truth.",
      "Judgments must still be based on legally relevant facts.",
      None, None,
      U_BSA, "Transition (July 1, 2024)", ["IEA 165", "BSA 168", "Judge Power", "Statutory Transition"],
      {"oldAct": "IEA 1872", "oldSection": "165", "newAct": "BSA 2023", "newSection": "168", "substantiveChange": "Judge's power to put questions relocated from IEA 165 to BSA 168."})

    m("The definition of 'Document' in Section 2(1)(d) of the BSA expressly includes electronic and digital records, emails, server logs, and messages.",
      "true", "Historical IEA vs BSA Transitions", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 2(1)(d)", None,
      "Section 2(1)(d) BSA modernized the definition of 'document' (old IEA 3) to expressly encompass electronic records, server logs, emails, text messages, location details, voice mails, and digital files.",
      "Eliminates interpretative ambiguities regarding modern technological data.",
      "Fundamental to paperless criminal and civil litigation.",
      None, None,
      U_BSA, "Transition (July 1, 2024)", ["Document Definition", "Section 2(1)(d)", "Electronic Records", "IEA 3", "BSA 2023"],
      {"oldAct": "IEA 1872", "oldSection": "3", "newAct": "BSA 2023", "newSection": "2(1)(d)", "substantiveChange": "Definition of document expressly widened to modern digital and electronic records."})

    m("Relevancy of expert opinions, historically governed by Section 45 of the IEA, is now governed by Section 39 of the BSA, 2023.",
      "true", "Historical IEA vs BSA Transitions", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 39", None,
      "Old IEA Section 45 corresponds directly to Section 39 of the BSA, 2023.",
      "Includes foreign law, science, art, handwriting, and finger impressions.",
      "Digital forensics experts are also covered.",
      None, None,
      U_BSA, "Transition (July 1, 2024)", ["IEA 45", "BSA 39", "Expert Opinion", "Statutory Transition"],
      {"oldAct": "IEA 1872", "oldSection": "45", "newAct": "BSA 2023", "newSection": "39", "substantiveChange": "Expert opinion relevancy relocated from IEA 45 to BSA 39."})

    m("Burden of proving a fact especially within knowledge, formerly Section 106 of the IEA, is now Section 109 of the BSA, 2023.",
      "true", "Historical IEA vs BSA Transitions", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 109", None,
      "Old IEA Section 106 corresponds directly to Section 109 of the BSA, 2023.",
      "Applies when fact is especially within knowledge of a party.",
      "Frequently tested in UP PCS-J Paper II.",
      None, None,
      U_BSA, "Transition (July 1, 2024)", ["IEA 106", "BSA 109", "Special Knowledge", "Statutory Transition"],
      {"oldAct": "IEA 1872", "oldSection": "106", "newAct": "BSA 2023", "newSection": "109", "substantiveChange": "Burden of proof of special knowledge relocated from IEA 106 to BSA 109."})

    m("The general burden of proof in a case, formerly Section 101 of the IEA, is now located in Section 104 of the BSA, 2023.",
      "true", "Historical IEA vs BSA Transitions", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 104", None,
      "Old IEA Section 101 corresponds directly to Section 104 of the BSA, 2023: whoever desires any court to give judgment as to any legal right dependent on facts he asserts, must prove those facts exist.",
      "The burden of establishing guilt beyond reasonable doubt never shifts.",
      "Onus of proof shifts during trial as evidence is produced (Section 105 BSA / old IEA 102).",
      None, None,
      U_BSA, "Transition (July 1, 2024)", ["IEA 101", "BSA 104", "Burden of Proof", "Statutory Transition"],
      {"oldAct": "IEA 1872", "oldSection": "101", "newAct": "BSA 2023", "newSection": "104", "substantiveChange": "General burden of proof relocated from IEA 101 to BSA 104."})

    m("The shifting of onus of proof, formerly Section 102 of the IEA, is now codified in Section 105 of the BSA, 2023.",
      "true", "Historical IEA vs BSA Transitions", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 105", None,
      "Old IEA Section 102 corresponds directly to Section 105 of the BSA, 2023: burden of proof lies on that person who would fail if no evidence at all were given on either side.",
      "Distinguishes static legal burden from dynamic evidential onus.",
      "Shifts back and forth during the trial proceedings.",
      None, None,
      U_BSA, "Transition (July 1, 2024)", ["IEA 102", "BSA 105", "Onus of Proof", "Statutory Transition"],
      {"oldAct": "IEA 1872", "oldSection": "102", "newAct": "BSA 2023", "newSection": "105", "substantiveChange": "Evidential onus test relocated from IEA 102 to BSA 105."})

    m("Exclusion of oral evidence by documentary evidence, formerly Sections 91 and 92 of the IEA, is now Sections 94 and 95 of the BSA, 2023.",
      "true", "Historical IEA vs BSA Transitions", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Sections 94 & 95", None,
      "Old IEA Sections 91/92 correspond directly to Sections 94/95 of the BSA, 2023.",
      "Documents speak for themselves and oral evidence cannot vary terms.",
      "Preserves all classic proviso exceptions.",
      None, None,
      U_BSA, "Transition (July 1, 2024)", ["IEA 91", "IEA 92", "BSA 94", "BSA 95", "Statutory Transition"],
      {"oldAct": "IEA 1872", "oldSection": "91", "newAct": "BSA 2023", "newSection": "94", "substantiveChange": "Best evidence rule relocated from IEA 91/92 to BSA 94/95."})

    m("The doctrine of Res Gestae, historically Section 6 of the IEA, is now located in Section 4 of the BSA, 2023.",
      "true", "Historical IEA vs BSA Transitions", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 4", None,
      "Old IEA Section 6 corresponds directly to Section 4 of the BSA, 2023.",
      "Facts forming part of the same transaction.",
      "Essential foundation of criminal law evidence.",
      None, None,
      U_BSA, "Transition (July 1, 2024)", ["IEA 6", "BSA 4", "Res Gestae", "Statutory Transition"],
      {"oldAct": "IEA 1872", "oldSection": "6", "newAct": "BSA 2023", "newSection": "4", "substantiveChange": "Res Gestae relocated from IEA 6 to BSA 4."})

    m("Relevancy of facts showing motive, preparation, and conduct, formerly Section 8 of the IEA, is now Section 6 of the BSA, 2023.",
      "true", "Historical IEA vs BSA Transitions", "beginner", "Bharatiya Sakshya Adhiniyam, 2023", "Section 6", None,
      "Old IEA Section 8 corresponds directly to Section 6 of the BSA, 2023.",
      "Conduct includes both previous and subsequent conduct.",
      "Motive is highly relevant in cases dependent on circumstantial evidence.",
      None, None,
      U_BSA, "Transition (July 1, 2024)", ["IEA 8", "BSA 6", "Motive Conduct", "Statutory Transition"],
      {"oldAct": "IEA 1872", "oldSection": "8", "newAct": "BSA 2023", "newSection": "6", "substantiveChange": "Motive, preparation and conduct relocated from IEA 8 to BSA 6."})

    # ---------------------------------------------------------
    # 6. BHARATIYA NAGARIK SURAKSHA SANHITA (BNSS) 2023 (30 items)
    # ---------------------------------------------------------
    m("A preliminary enquiry is permissible before registering an FIR for offences punishable between three and seven years under Section 173(3) of the BNSS.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "beginner", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 173(3)", None,
      "Section 173(3) BNSS explicitly codifies the preliminary enquiry mechanism: for offences punishable with imprisonment of 3 to 7 years, police may conduct a preliminary enquiry within 14 days with prior permission of an officer not below Deputy Superintendent of Police.",
      "Under Lalita Kumari (2013), preliminary inquiry was judicially created for limited categories like corruption or medical negligence.",
      "Mandatory FIR immediately if prima facie cognizable case is apparent.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Preliminary Enquiry", "Section 173(3)", "FIR Registration", "Lalita Kumari", "BNSS 2023"])

    m("Zero FIR has been granted express statutory recognition under Section 173(1) of the BNSS, 2023.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "beginner", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 173(1)", None,
      "Section 173(1) BNSS mandates that information relating to a cognizable offence shall be recorded by the officer in charge of a police station 'irrespective of the area where the offence was committed' (Zero FIR).",
      "Previously, Zero FIR existed solely through executive guidelines and Supreme Court directions.",
      "Station must register it, transfer to jurisdictional police, and initiate urgent steps.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Zero FIR", "Section 173(1)", "Jurisdiction", "Police Station", "BNSS 2023"])

    m("Electronic FIR (e-FIR) is recognized under Section 173(1) of the BNSS, provided the informant signs it within three days.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "beginner", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 173(1)", None,
      "Section 173(1) proviso BNSS provides that information given through electronic communication shall be taken on record by police, provided it is signed within three days by the person giving it before it is entered in the book.",
      "Provides formal statutory validity to online crime reporting across India.",
      "Action cannot proceed to formal investigation until signature is obtained.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["e-FIR", "Section 173(1)", "Three Days Signature", "Electronic Communication", "BNSS 2023"])

    m("Handcuffing is permissible under Section 43(3) of the BNSS for persons accused of heinous offences including murder, rape, or terror acts.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "intermediate", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 43(3)", None,
      "Section 43(3) BNSS statutory authorizes police officers to use handcuffs during arrest or court production for habitual, repeat offenders or those accused of serious offences like terror acts, murder, rape, or acid attack.",
      "Prem Shankar Shukla v. Delhi Administration (1980) had strictly curbed routine handcuffing without judicial permission.",
      "Intended to prevent escape of dangerous offenders.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Handcuffing", "Section 43(3)", "Prem Shankar Shukla", "Heinous Offences", "BNSS 2023"])

    m("Police custody under Section 187 of the BNSS must strictly be completed within the first fifteen days of arrest and cannot be sought thereafter.",
      "false", "Bharatiya Nagarik Suraksha Sanhita, 2023", "intermediate", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 187(2) & (3)", None,
      "Section 187(3) BNSS permits police custody of up to 15 days in whole or in parts at any time during the initial 40 or 60 days of the total detention period.",
      "Under old CrPC Section 167(2) (CBI v. Anupam Kulkarni), police custody could strictly only be taken during the first 15 days.",
      "Total duration of police custody cannot exceed 15 days in aggregate.",
      "must strictly be completed within the first fifteen days of arrest and cannot be sought thereafter", "can be taken in parts during the initial 40 or 60 days under Section 187(3)",
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Police Custody", "Section 187", "Anupam Kulkarni", "Remand", "BNSS 2023"],
      {"oldAct": "CrPC 1973", "oldSection": "167", "newAct": "BNSS 2023", "newSection": "187", "substantiveChange": "Police custody of up to 15 days can now be sought in parts across initial 40/60 days."})

    m("Audio-video electronic recording of search and seizure operations is mandatory under Section 105 of the BNSS, 2023.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "beginner", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 105", None,
      "Section 105 BNSS mandates that search and seizure processes, including the preparation of the list of seized items, must be recorded through audio-video electronic means (preferably mobile phone) and forwarded to the Magistrate without delay.",
      "Addresses pervasive allegations of planted evidence and fabricated seizure memos.",
      "Seizure list must be signed by witnesses.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Search and Seizure", "Section 105", "Audio Video Recording", "Forensic Integrity", "BNSS 2023"])

    m("Forensic investigation is made mandatory under Section 176(3) of the BNSS for all offences punishable with imprisonment of seven years or more.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "beginner", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 176(3)", None,
      "Section 176(3) BNSS provides that on information of an offence punishable with 7 years or more, the officer in charge shall cause a forensic expert to visit the crime scene, collect evidence, and videograph the process.",
      "Where forensic facility is unavailable, state shall utilize facilities of other states.",
      "A transitional period of 5 years was granted for states to establish forensic infrastructure.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Forensic Investigation", "Section 176(3)", "Seven Years Offence", "Crime Scene", "BNSS 2023"])

    m("Under Section 479 of the BNSS, a first-time offender who has undergone one-third of the maximum sentence is eligible for mandatory release on bail.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "beginner", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 479(1)", None,
      "Section 479(1) proviso BNSS introduces a beneficial reform: a first-time offender who has never been previously convicted of any offence shall be released on bail on undergoing one-third of the maximum imprisonment.",
      "Under old CrPC 436A, the period was one-half for all undertrials without exception.",
      "Does not apply to offences punishable with death or life imprisonment.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Undertrial Bail", "Section 479", "One-third Sentence", "First-time Offender", "BNSS 2023"],
      {"oldAct": "CrPC 1973", "oldSection": "436A", "newAct": "BNSS 2023", "newSection": "479", "substantiveChange": "Bail eligibility reduced to one-third of maximum sentence for first-time offenders."})

    m("Trial in absentia of a proclaimed offender who has absconded is recognized under Section 356 of the BNSS, 2023.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "intermediate", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 356", None,
      "Section 356 BNSS allows the Court to proceed with the inquiry or trial in the absence of a proclaimed offender who has absconded to evade trial, and pronounce judgment.",
      "Under old CrPC, trials could not culminate in conviction in absentia (only evidence recording under 299).",
      "Notice must be published in newspapers and 90 days must elapse before proceeding.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Trial in Absentia", "Section 356", "Proclaimed Offender", "Absconding", "BNSS 2023"])

    m("The maximum fine limit in summary trials by Magistrates has been raised to twenty thousand rupees under Section 283 of the BNSS.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "intermediate", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 283", None,
      "Section 283 BNSS (old CrPC 260) expands summary trial powers and increases the maximum fine in summary trials from 2,000 rupees to 20,000 rupees.",
      "Section 283(2) permits summary trial for petty theft up to 20,000 rupees.",
      "Imprisonment in summary trial cannot exceed 3 months.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Summary Trial", "Section 283", "Twenty Thousand Rupees", "Fine Limit", "BNSS 2023"])

    m("Plea bargaining under Chapter XXI of the BNSS is available for offences punishable with death or imprisonment for life.",
      "false", "Bharatiya Nagarik Suraksha Sanhita, 2023", "beginner", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 290", None,
      "Section 290 BNSS (old CrPC 265A) explicitly bars plea bargaining for offences punishable with death, imprisonment for life, imprisonment exceeding 7 years, offences affecting socio-economic condition of the country, or crimes against women or children below 14 years.",
      "Candidates mistakenly think any criminal case can be settled via plea bargaining.",
      "Application must be filed voluntarily by the accused within 30 days from framing of charge.",
      "is available for offences punishable with death or imprisonment for life", "is strictly barred for offences punishable with death, life imprisonment, or exceeding 7 years",
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Plea Bargaining", "Section 290", "Barred Offences", "CrPC 265A", "BNSS 2023"])

    m("Every State Government is mandated under Section 398 of the BNSS to prepare and notify a Witness Protection Scheme.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "beginner", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 398", None,
      "Section 398 BNSS gives statutory backing to the Supreme Court's Mahender Chawla (2019) directives, mandating that every State Government shall prepare and notify a Witness Protection Scheme.",
      "Previously, witness protection was non-statutory and haphazard across states.",
      "Ensures witnesses can testify freely without threats or intimidation.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Witness Protection", "Section 398", "State Scheme", "Mahender Chawla", "BNSS 2023"])

    m("Under Section 472 of the BNSS, a mercy petition against a death sentence must be filed within thirty days from dismissal of appeal.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "intermediate", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 472", None,
      "Section 472 BNSS introduces strict statutory timelines: a convict on death row may submit a mercy petition to the Governor within 30 days, and if rejected, to the President within 30 days.",
      "Previously, mercy petitions had no statutory limitation period, leading to years of delay.",
      "Orders of the President on mercy petitions cannot be challenged on merits.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Mercy Petition", "Section 472", "Thirty Days", "Death Sentence", "BNSS 2023"])

    m("Under Section 258 and 392 of the BNSS, criminal courts must pronounce judgment within forty-five days after the conclusion of arguments.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "beginner", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Sections 258 & 392", None,
      "Sections 258 and 392 BNSS mandate that judgment shall be pronounced within 30 days of trial conclusion, extendable up to 45 days for recorded reasons.",
      "Under CrPC, no fixed outer limitation existed, causing prolonged judgment reserves.",
      "Ensures speedy trial under Article 21.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Judgment Timeline", "Section 258", "Section 392", "Forty-five Days", "BNSS 2023"])

    m("Notice of appearance before a police officer in offences punishable up to seven years is governed by Section 35(3) of the BNSS.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "beginner", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 35(3)", None,
      "Section 35(3) BNSS corresponds to old CrPC Section 41A (Arnesh Kumar guidelines): where arrest is not required for offences punishable with up to 7 years, police must issue a notice of appearance.",
      "Arrest without notice requires recording reasons in writing.",
      "Failure to comply with notice authorizes arrest.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Notice of Appearance", "Section 35(3)", "Arnesh Kumar", "CrPC 41A", "BNSS 2023"])

    m("Medical examination of an arrested person by a registered medical practitioner is governed by Section 51 of the BNSS, 2023.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "beginner", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 51", None,
      "Section 51 BNSS (old CrPC 54) provides for mandatory medical examination of an arrested person immediately after arrest.",
      "A copy of the medical report must be furnished to the arrested person or nominated relative.",
      "Protects against custodial torture.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Medical Examination", "Section 51", "Arrestee Rights", "CrPC 54", "BNSS 2023"])

    m("The statutory provision for maintenance of wives, children, and parents, formerly Section 125 of the CrPC, is now Section 144 of the BNSS.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "beginner", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 144", None,
      "Old CrPC Section 125 is now Section 144 of the BNSS, 2023.",
      "Secular remedy for maintenance of destitute wife, minor children, and parents.",
      "Application for interim maintenance must be disposed of within 60 days.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Maintenance", "Section 144", "CrPC 125", "Interim Maintenance", "BNSS 2023"],
      {"oldAct": "CrPC 1973", "oldSection": "125", "newAct": "BNSS 2023", "newSection": "144", "substantiveChange": "Maintenance of wives, children and parents relocated from CrPC 125 to BNSS 144."})

    m("Urgent orders in cases of nuisance or apprehended danger (popularly known as Section 144) are now governed by Section 163 of the BNSS.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "beginner", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 163", None,
      "Old CrPC Section 144 is now Section 163 of the BNSS, 2023.",
      "District Magistrate, SDM or Executive Magistrate can issue urgent prohibitory orders to prevent obstruction, annoyance, or riot.",
      "Cannot remain in force for more than 2 months unless extended by State Government up to 6 months.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Section 163", "Curfew Order", "CrPC 144", "Public Order", "BNSS 2023"],
      {"oldAct": "CrPC 1973", "oldSection": "144", "newAct": "BNSS 2023", "newSection": "163", "substantiveChange": "Urgent prohibitory orders relocated from CrPC 144 to BNSS 163."})

    m("Inquest reports into unnatural deaths by police officers, formerly Section 174 of the CrPC, are now governed by Section 194 of the BNSS.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "beginner", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 194", None,
      "Old CrPC Section 174 is now Section 194 of the BNSS, 2023.",
      "Police officer investigates apparent cause of death in cases of suicide, animal killing, accident, or suspicious death.",
      "Magisterial inquest under Section 196 BNSS applies to custodial death or death of married woman within 7 years.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Inquest Report", "Section 194", "CrPC 174", "Unnatural Death", "BNSS 2023"],
      {"oldAct": "CrPC 1973", "oldSection": "174", "newAct": "BNSS 2023", "newSection": "194", "substantiveChange": "Police inquest on unnatural death relocated from CrPC 174 to BNSS 194."})

    m("Cognizance of offences by Magistrates, historically governed by Section 190 of the CrPC, is now governed by Section 210 of the BNSS.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "beginner", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 210", None,
      "Old CrPC Section 190 corresponds directly to Section 210 of the BNSS, 2023.",
      "Magistrate takes cognizance upon receiving a complaint, police report, or information received from any other person.",
      "Taking cognizance means applying judicial mind to suspected commission of offence.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Cognizance", "Section 210", "Magistrate", "CrPC 190", "BNSS 2023"],
      {"oldAct": "CrPC 1973", "oldSection": "190", "newAct": "BNSS 2023", "newSection": "210", "substantiveChange": "Magisterial cognizance relocated from CrPC 190 to BNSS 210."})

    m("Discharge of the accused in a warrant case instituted on a police report is governed by Section 262 of the BNSS, 2023.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "intermediate", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 262", None,
      "Old CrPC Section 239 corresponds directly to Section 262 of the BNSS, 2023: if Magistrate considers the charge groundless, he shall discharge the accused and record reasons.",
      "If charge is not groundless, Magistrate frames charges under Section 263 BNSS (old CrPC 240).",
      "Essential pre-trial stage in warrant cases.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Discharge", "Section 262", "Groundless Charge", "CrPC 239", "BNSS 2023"])

    m("Compounding of criminal offences, historically Section 320 of the CrPC, is now codified under Section 359 of the BNSS, 2023.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "beginner", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 359", None,
      "Old CrPC Section 320 corresponds directly to Section 359 of the BNSS, 2023.",
      "Table I lists offences compoundable without court permission; Table II lists offences compoundable only with court permission.",
      "Compounding has the effect of an acquittal of the accused.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Compounding", "Section 359", "Acquittal Effect", "CrPC 320", "BNSS 2023"],
      {"oldAct": "CrPC 1973", "oldSection": "320", "newAct": "BNSS 2023", "newSection": "359", "substantiveChange": "Compounding of offences relocated from CrPC 320 to BNSS 359."})

    m("Committal of a case to the Court of Session when an offence is triable exclusively by it is governed by Section 232 of the BNSS.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "intermediate", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 232", None,
      "Old CrPC Section 209 corresponds directly to Section 232 of the BNSS, 2023.",
      "Magistrate commits the case, remands accused to custody, and sends records and weapons to the Court of Session.",
      "Applies to offences like murder, rape, and dacoity.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Committal", "Section 232", "Court of Session", "CrPC 209", "BNSS 2023"])

    m("Anticipatory bail can be granted by any Judicial Magistrate under Section 482 of the BNSS, 2023.",
      "false", "Bharatiya Nagarik Suraksha Sanhita, 2023", "beginner", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 482", None,
      "Section 482 BNSS (old CrPC 438) confers power to grant direction for bail to a person apprehending arrest exclusively on the High Court and the Court of Session. A Magistrate has zero jurisdiction to grant anticipatory bail.",
      "Laypersons assume any bail can be moved before the local trial magistrate.",
      "Regular bail can be granted by Magistrates under Section 480 BNSS (old CrPC 437).",
      "can be granted by any Judicial Magistrate under Section 482", "can only be granted by the High Court or Court of Session under Section 482",
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Anticipatory Bail", "Section 482", "High Court", "Court of Session", "BNSS 2023"],
      {"oldAct": "CrPC 1973", "oldSection": "438", "newAct": "BNSS 2023", "newSection": "482", "substantiveChange": "Anticipatory bail relocated from CrPC 438 to BNSS 482; jurisdiction restricted to HC and Sessions."})

    m("A police officer is empowered to arrest without warrant any person who commits any non-cognizable offence in their presence.",
      "false", "Bharatiya Nagarik Suraksha Sanhita, 2023", "intermediate", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 35 & Section 39", None,
      "Police cannot arrest without warrant for non-cognizable offences as a general rule (Section 35 BNSS / old CrPC 41). Under Section 39 BNSS (old CrPC 42), arrest is permitted only if the person refuses to give their name and residence or gives false details.",
      "Candidates mistakenly think commission in police presence converts a non-cognizable offence into cognizable arrest power.",
      "Magisterial warrant is required for non-cognizable arrests once identity is ascertained.",
      "any person who commits any non-cognizable offence in their presence", "only if such person refuses to disclose their name and residence under Section 39",
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Arrest Power", "Section 35", "Section 39", "Non-cognizable", "BNSS 2023"])

    m("In a bailable offence, bail is an absolute right of the accused and police or court is bound to release them upon furnishing bail under Section 478 BNSS.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "beginner", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 478", None,
      "Section 478 BNSS (old CrPC 436) mandates that a person accused of a bailable offence 'shall be released on bail' if prepared to give bail.",
      "Court or police officer has no discretion to refuse bail in bailable offences (Rasiklal v. Kishore Khanchand Wadhwani).",
      "Indigent persons can be discharged on their personal bond without sureties.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Bailable Offence", "Section 478", "Right to Bail", "Rasiklal", "BNSS 2023"])

    m("Under Section 175 of the BNSS, police officers can require the attendance of witnesses, but women and children under fifteen cannot be compelled to attend at any place other than their residence.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "intermediate", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 175(1)", None,
      "Section 175(1) proviso BNSS (old CrPC 160) safeguards that no male person under 15 or above 60 years, or woman, or mentally/physically disabled person, shall be required to attend at any place other than their place of residence.",
      "Essential protection against police harassment.",
      "Statement of woman can be recorded at her residence or by woman police officer.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Witness Attendance", "Section 175", "Women Protection", "CrPC 160", "BNSS 2023"])

    m("Inherent powers to make such orders as may be necessary to prevent abuse of the process of any court belong to both the High Court and Sessions Court under Section 528 BNSS.",
      "false", "Bharatiya Nagarik Suraksha Sanhita, 2023", "beginner", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 528", None,
      "Section 528 BNSS (old CrPC 482) preserves the inherent powers exclusively for the High Court: 'Nothing in this Sanhita shall be deemed to limit or affect the inherent powers of the High Court.' The Court of Session possesses no inherent powers.",
      "Candidates mistakenly attribute inherent criminal powers to Sessions Judges.",
      "Sessions Court has revisional powers under Section 438 BNSS, not inherent powers.",
      "belong to both the High Court and Sessions Court under Section 528", "belong exclusively to the High Court under Section 528",
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Inherent Powers", "Section 528", "High Court Exclusive", "CrPC 482", "BNSS 2023"],
      {"oldAct": "CrPC 1973", "oldSection": "482", "newAct": "BNSS 2023", "newSection": "528", "substantiveChange": "Inherent criminal powers relocated from CrPC 482 to BNSS 528; remains HC exclusive."})

    m("A private person has the statutory power to arrest any person who in their presence commits a non-bailable and cognizable offence under Section 40 of the BNSS.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "beginner", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 40", None,
      "Section 40 BNSS (old CrPC 43) empowers any private person to arrest or cause to be arrested any person who in his presence commits a non-bailable and cognizable offence, or any proclaimed offender.",
      "Arrested person must be handed over to a police officer or police station without unnecessary delay.",
      "Citizen arrest is recognized in Indian law.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["Citizen Arrest", "Section 40", "Private Person", "CrPC 43", "BNSS 2023"])

    m("No appeal shall lie from a conviction by a High Court where the High Court passes a sentence of imprisonment not exceeding six months under Section 417 BNSS.",
      "true", "Bharatiya Nagarik Suraksha Sanhita, 2023", "intermediate", "Bharatiya Nagarik Suraksha Sanhita, 2023", "Section 417", None,
      "Section 417 BNSS (old CrPC 376) bars appeals in petty cases, including where High Court imposes imprisonment up to 6 months or fine up to 1,000 rupees, or Court of Session imposes imprisonment up to 3 months.",
      "Special Leave under Article 136 is not an ordinary appeal.",
      "Prevents petty criminal convictions from overburdening appellate benches.",
      None, None,
      U_BNSS, "Current Law (in force from July 1, 2024)", ["No Appeal Petty Cases", "Section 417", "CrPC 376", "Appellate Bar", "BNSS 2023"])

    # ---------------------------------------------------------
    # 7. CODE OF CIVIL PROCEDURE (CPC) 1908 (35 items)
    # ---------------------------------------------------------
    m("The doctrine of Res Judicata under Section 11 of the CPC applies to execution proceedings as well as suits.",
      "true", "Code of Civil Procedure, 1908", "intermediate", "Code of Civil Procedure, 1908", "Section 11 Explanation VII", None,
      "Explanation VII to Section 11 CPC, inserted by the 1976 Amendment, explicitly provides that the provisions of Section 11 shall apply to a proceeding for the execution of a decree.",
      "Some assume res judicata applies solely to the main trial of original civil suits.",
      "Issues decided at one stage of execution cannot be reagitated at subsequent stages.",
      None, None,
      U_CPC, "Current Civil Procedure", ["Res Judicata", "Section 11", "Explanation VII", "Execution Proceedings", "CPC 1908"])

    m("Section 10 of the CPC (Res Sub Judice) bars the institution of a subsequent suit on the same cause of action.",
      "false", "Code of Civil Procedure, 1908", "beginner", "Code of Civil Procedure, 1908", "Section 10", None,
      "Section 10 CPC does not bar the institution of the subsequent suit; it merely bars the trial of that suit. The plaint is received and registered, but proceedings are stayed pending decision of previous suit (National Institute of Mental Health v. C. Parameshwara).",
      "Candidates frequently state that Section 10 bars the filing or institution of the plaint.",
      "Interim relief like injunctions or receiver appointment can still be granted during stay of trial.",
      "bars the institution of a subsequent suit on the same cause of action", "bars only the trial of the subsequent suit, not its institution",
      U_CPC, "Current Civil Procedure", ["Res Sub Judice", "Section 10", "Stay of Suit", "Institution Permitted", "CPC 1908"])

    m("The inherent powers of a civil court under Section 151 of the CPC create new substantive rights for litigants.",
      "false", "Code of Civil Procedure, 1908", "intermediate", "Code of Civil Procedure, 1908", "Section 151", None,
      "Section 151 CPC does not confer any substantive power or right; it merely saves the inherent procedural power of the court to make orders necessary for ends of justice or to prevent abuse of process where no express provision exists (Manohar Lal Chopra v. Seth Hiralal).",
      "Aspirants believe Section 151 can override statutory prohibitions or create new causes of action.",
      "Inherent power cannot be exercised in conflict with what is expressly provided by the Code.",
      "create new substantive rights for litigants", "merely save procedural powers to prevent abuse of process without creating substantive rights",
      U_CPC, "Current Civil Procedure", ["Section 151", "Inherent Powers", "Manohar Lal Chopra", "Procedural Law", "CPC 1908"])

    m("A Caveat lodged under Section 148A of the CPC remains in force for a period of ninety days from the date it was lodged.",
      "true", "Code of Civil Procedure, 1908", "beginner", "Code of Civil Procedure, 1908", "Section 148A(5)", None,
      "Section 148A(5) CPC expressly provides that a caveat shall not remain in force after the expiry of 90 days from the date on which it was lodged, unless the application has been made before the expiry.",
      "A fresh caveat must be filed if protection is needed beyond 90 days.",
      "Ensures the caveator receives notice before any ex parte order is passed.",
      None, None,
      U_CPC, "Current Civil Procedure", ["Caveat", "Section 148A", "Ninety Days", "Ex Parte Order", "CPC 1908"])

    m("A foreign judgment is conclusive as to any matter directly adjudicated upon between the same parties under Section 13 of the CPC.",
      "true", "Code of Civil Procedure, 1908", "intermediate", "Code of Civil Procedure, 1908", "Section 13", None,
      "Section 13 CPC declares foreign judgments conclusive, subject to 6 enumerated exceptions (not pronounced by competent court, not on merits, against international law, violation of natural justice, obtained by fraud, or sustaining claim founded on breach of Indian law).",
      "Can be enforced in India by a suit upon the judgment or execution under Section 44A for reciprocating territories.",
      "Foreign judgment cannot be challenged on mere factual errors.",
      None, None,
      U_CPC, "Current Civil Procedure", ["Foreign Judgment", "Section 13", "Conclusiveness", "Execution", "CPC 1908"])

    m("A suit for the recovery of immovable property must be instituted in the court within the local limits of whose jurisdiction the property is situate under Section 16.",
      "true", "Code of Civil Procedure, 1908", "beginner", "Code of Civil Procedure, 1908", "Section 16(a)", None,
      "Section 16(a) CPC mandates that suits for recovery of immovable property shall be instituted in the court within the local limits of whose jurisdiction the property is situate (forum rei sitae).",
      "Where property is situated across jurisdictions of different courts, suit may be filed in any of those courts under Section 17 CPC.",
      "Personal obedience proviso permits suits where relief can be obtained entirely through personal arrest/attachment.",
      None, None,
      U_CPC, "Current Civil Procedure", ["Territorial Jurisdiction", "Section 16", "Immovable Property", "Forum Rei Sitae", "CPC 1908"])

    m("Pecuniary jurisdiction of a court can be waived by consent of parties, rendering a decree passed without pecuniary jurisdiction completely valid.",
      "false", "Code of Civil Procedure, 1908", "intermediate", "Code of Civil Procedure, 1908", "Section 6 & Section 21(2)", None,
      "Pecuniary jurisdiction is statutory under Section 6 CPC. While Section 21(2) requires objection to be taken at the earliest opportunity, consent cannot confer jurisdiction where court inherently lacks pecuniary power (Kiran Singh v. Chaman Paswan).",
      "Parties assume jurisdiction can be created by contract or joint compromise.",
      "A decree without subject-matter jurisdiction is a total nullity.",
      "can be waived by consent of parties, rendering a decree passed without pecuniary jurisdiction completely valid", "cannot be conferred by consent of parties as statutory limits govern under Section 6",
      U_CPC, "Current Civil Procedure", ["Pecuniary Jurisdiction", "Section 6", "Section 21", "Kiran Singh", "Nullity Decree"])

    m("A temporary injunction under Order XXXIX Rules 1 and 2 of the CPC can be granted without the applicant proving a prima facie case.",
      "false", "Code of Civil Procedure, 1908", "beginner", "Code of Civil Procedure, 1908", "Order XXXIX Rules 1 & 2", None,
      "To obtain a temporary injunction, the applicant must establish all three classical pillars: (1) prima facie case, (2) balance of convenience in their favor, and (3) irreparable injury that cannot be compensated in damages (Dalpat Kumar v. Prahlad Singh).",
      "Laypersons think alleging urgency or hardship alone suffices for injunctions.",
      "Absence of any one of the three pillars is fatal to the injunction application.",
      "can be granted without the applicant proving a prima facie case", "strictly requires proving a prima facie case, balance of convenience, and irreparable injury",
      U_CPC, "Current Civil Procedure", ["Temporary Injunction", "Order XXXIX", "Prima Facie Case", "Dalpat Kumar", "CPC 1908"])

    m("Rejection of a plaint under Order VII Rule 11 of the CPC precludes the plaintiff from presenting a fresh plaint on the same cause of action.",
      "false", "Code of Civil Procedure, 1908", "beginner", "Code of Civil Procedure, 1908", "Order VII Rule 13", None,
      "Order VII Rule 13 CPC explicitly declares that the rejection of the plaint on any of the grounds mentioned in Rule 11 shall not of its own force preclude the plaintiff from presenting a fresh plaint in respect of the same cause of action.",
      "Candidates confuse rejection of plaint (Order VII Rule 11) with dismissal of suit (which operates as res judicata).",
      "Plaintiff can rectify valuation, court-fees, or cause of action defects and refile.",
      "precludes the plaintiff from presenting a fresh plaint on the same cause of action", "does not preclude the plaintiff from presenting a fresh plaint under Order VII Rule 13",
      U_CPC, "Current Civil Procedure", ["Rejection of Plaint", "Order VII Rule 11", "Order VII Rule 13", "Fresh Plaint", "CPC 1908"])

    m("A defendant must ordinarily file their Written Statement within thirty days from the date of service of summons under Order VIII Rule 1 of the CPC.",
      "true", "Code of Civil Procedure, 1908", "beginner", "Code of Civil Procedure, 1908", "Order VIII Rule 1", None,
      "Order VIII Rule 1 CPC stipulates that written statement shall be presented within 30 days, extendable up to 90 days for recorded reasons (Salem Advocate Bar Association). In commercial suits, outer cap is 120 days.",
      "In non-commercial suits, the 90-day provision is directory, though exceptional reasons are needed.",
      "In commercial suits, the 120-day cap is mandatory and forfeiture occurs thereafter.",
      None, None,
      U_CPC, "Current Civil Procedure", ["Written Statement", "Order VIII Rule 1", "Thirty Days", "Salem Advocate", "Commercial Courts"])

    m("A counter-claim under Order VIII Rule 6A of the CPC can only be filed against the plaintiff and cannot include any relief against co-defendants alone.",
      "true", "Code of Civil Procedure, 1908", "intermediate", "Code of Civil Procedure, 1908", "Order VIII Rule 6A", None,
      "A counter-claim must be directed against the plaintiff, although the defendant may join a co-defendant along with the plaintiff if claim against plaintiff exists (Rohit Shekhar v. Narayan Dutt Tiwari). A counter-claim exclusively against a co-defendant is not maintainable.",
      "Litigants try to settle intra-defendant disputes via counter-claim without involving the plaintiff.",
      "Counter-claim has the same effect as a cross-suit.",
      None, None,
      U_CPC, "Current Civil Procedure", ["Counter-claim", "Order VIII Rule 6A", "Plaintiff", "Cross-suit", "CPC 1908"])

    m("Legal set-off under Order VIII Rule 6 of the CPC can be claimed for an unascertained sum of damages.",
      "false", "Code of Civil Procedure, 1908", "intermediate", "Code of Civil Procedure, 1908", "Order VIII Rule 6", None,
      "Order VIII Rule 6 CPC strictly requires that legal set-off must be an 'ascertained sum of money' legally recoverable by defendant from plaintiff. Unascertained damages can only be claimed as equitable set-off in narrow circumstances arising from the same transaction.",
      "Candidates confuse legal set-off (ascertained sum) with equitable set-off (same transaction).",
      "Pecuniary jurisdiction must also not be exceeded.",
      "can be claimed for an unascertained sum of damages", "strictly requires an ascertained sum of money under Order VIII Rule 6",
      U_CPC, "Current Civil Procedure", ["Set-off", "Order VIII Rule 6", "Ascertained Sum", "Equitable Set-off", "CPC 1908"])

    m("Where a suit is wholly or partly dismissed under Order IX Rule 8 of the CPC for plaintiff's default, the plaintiff is precluded from bringing a fresh suit on the same cause of action.",
      "true", "Code of Civil Procedure, 1908", "intermediate", "Code of Civil Procedure, 1908", "Order IX Rule 9", None,
      "Order IX Rule 9 CPC expressly bars the plaintiff from bringing a fresh suit on the same cause of action where suit is dismissed under Rule 8 (defendant appears, plaintiff absent). The remedy is an application to set aside dismissal.",
      "Differs from dismissal under Order IX Rule 2 or 3, where fresh suit is permitted under Rule 4.",
      "Plaintiff must demonstrate sufficient cause for non-appearance.",
      None, None,
      U_CPC, "Current Civil Procedure", ["Order IX Rule 8", "Order IX Rule 9", "Dismissal for Default", "Bar on Fresh Suit", "CPC 1908"])

    m("An ex parte decree passed against a defendant can be set aside under Order IX Rule 13 of the CPC if sufficient cause is shown.",
      "true", "Code of Civil Procedure, 1908", "beginner", "Code of Civil Procedure, 1908", "Order IX Rule 13", None,
      "Order IX Rule 13 CPC empowers the court to set aside an ex parte decree if defendant satisfies the court that summons was not duly served or that they were prevented by sufficient cause from appearing.",
      "Defendant can also file an appeal under Section 96(2) against the ex parte decree.",
      "Second proviso prevents setting aside on mere irregularity of summons if defendant had notice of date.",
      None, None,
      U_CPC, "Current Civil Procedure", ["Ex Parte Decree", "Order IX Rule 13", "Sufficient Cause", "Setting Aside", "CPC 1908"])

    m("Under Order VI Rule 17 of the CPC, an amendment of pleadings must be allowed at any stage even after trial has commenced without proving due diligence.",
      "false", "Code of Civil Procedure, 1908", "intermediate", "Code of Civil Procedure, 1908", "Order VI Rule 17 proviso", None,
      "The proviso to Order VI Rule 17 CPC (inserted in 2002) mandates that no application for amendment shall be allowed after the trial has commenced, unless the court concludes that in spite of due diligence, the party could not have raised the matter before.",
      "Many believe amendments can be sought routinely at any stage of litigation without threshold diligence.",
      "Pre-trial amendments are liberally granted to determine real controversy.",
      "must be allowed at any stage even after trial has commenced without proving due diligence", "is barred after trial commences unless due diligence is established under the proviso",
      U_CPC, "Current Civil Procedure", ["Amendment of Pleadings", "Order VI Rule 17", "Due Diligence", "Trial Commencement", "CPC 1908"])

    m("A representative suit under Order I Rule 8 of the CPC requires prior permission of the Court and notice to all interested parties.",
      "true", "Code of Civil Procedure, 1908", "beginner", "Code of Civil Procedure, 1908", "Order I Rule 8", None,
      "Order I Rule 8 CPC allows one person to sue or be sued on behalf of numerous persons having the same interest, but mandates court permission and notice to all interested parties by personal service or public advertisement.",
      "Decree passed in a representative suit binds all persons represented under Section 11 Explanation VI.",
      "No compromise can be entered into without court leave and notice.",
      None, None,
      U_CPC, "Current Civil Procedure", ["Representative Suit", "Order I Rule 8", "Public Notice", "Explanation VI", "CPC 1908"])

    m("If a sole plaintiff dies and the right to sue survives, but no application for substitution of legal representatives is made within the limitation period, the suit abates.",
      "true", "Code of Civil Procedure, 1908", "beginner", "Code of Civil Procedure, 1908", "Order XXII Rule 3", None,
      "Under Order XXII Rule 3(2) CPC, where within the time limited by law (90 days under Article 120 Limitation Act) no application is made to substitute legal representatives, the suit abates as against the deceased plaintiff.",
      "Abatement can be set aside under Order XXII Rule 9 upon showing sufficient cause (within 60 days under Art 121).",
      "Right to sue must survive; personal actions die with person (actio personalis moritur cum persona).",
      None, None,
      U_CPC, "Current Civil Procedure", ["Abatement of Suit", "Order XXII Rule 3", "Legal Representatives", "Limitation", "CPC 1908"])

    m("Appointment of a Receiver under Order XL Rule 1 of the CPC is an exceptional discretionary remedy known as one of the hardest measures in civil law.",
      "true", "Code of Civil Procedure, 1908", "intermediate", "Code of Civil Procedure, 1908", "Order XL Rule 1", None,
      "Order XL Rule 1 CPC permits appointment of a receiver where it appears 'just and convenient'. Because it dispossesses a party before final adjudication, courts apply strict principles requiring proof of danger or waste (T. Krishnaswamy Chetty).",
      "It is not granted merely because an applicant feels aggrieved or files an application.",
      "Receiver is an officer of the court and property is in custodia legis.",
      None, None,
      U_CPC, "Current Civil Procedure", ["Receiver", "Order XL Rule 1", "Custodia Legis", "Just and Convenient", "CPC 1908"])

    m("A second appeal under Section 100 of the CPC lies to the High Court on any question of fact or appreciation of evidence.",
      "false", "Code of Civil Procedure, 1908", "beginner", "Code of Civil Procedure, 1908", "Section 100(1)", None,
      "Section 100(1) CPC strictly provides that an appeal shall lie to the High Court from every decree passed in appeal by any subordinate court only 'if the High Court is satisfied that the case involves a substantial question of law.'",
      "Appellants frequently seek reappreciation of evidence in second appeal, which is barred.",
      "The High Court must formulate the substantial question of law at admission.",
      "lies to the High Court on any question of fact or appreciation of evidence", "lies strictly on a substantial question of law under Section 100(1)",
      U_CPC, "Current Civil Procedure", ["Second Appeal", "Section 100", "Substantial Question of Law", "High Court", "CPC 1908"])

    m("Under Section 100A of the CPC, no further appeal lies to a Division Bench from a decree passed by a single Judge of a High Court in an appeal.",
      "true", "Code of Civil Procedure, 1908", "intermediate", "Code of Civil Procedure, 1908", "Section 100A", None,
      "Section 100A CPC (inserted in 2002) bars Letters Patent Appeals: where any appeal from an original or appellate decree is heard and decided by a single Judge of a High Court, no further appeal shall lie to a Division Bench.",
      "Abolished internal intra-court appeals to curb delay in finality of civil litigation.",
      "Applies notwithstanding anything contained in Letters Patent of High Courts.",
      None, None,
      U_CPC, "Current Civil Procedure", ["Section 100A", "Letters Patent Appeal", "Single Judge", "Division Bench", "CPC 1908"])

    m("Review of a judgment under Section 114 and Order XLVII of the CPC is an appeal in disguise allowing complete rehearing of the case.",
      "false", "Code of Civil Procedure, 1908", "beginner", "Code of Civil Procedure, 1908", "Order XLVII Rule 1", None,
      "A review is not an appeal in disguise (Parsion Devi v. Sumitri Devi). It is strictly limited to: (1) discovery of new important evidence not available despite due diligence, (2) mistake or error apparent on the face of the record, or (3) any other sufficient reason analogous thereto.",
      "Litigants often apply for review to reargue propositions rejected by the court.",
      "An erroneous decision cannot be corrected in review; that is the domain of appeal.",
      "is an appeal in disguise allowing complete rehearing of the case", "is not an appeal and is strictly limited to error apparent on the face of the record",
      U_CPC, "Current Civil Procedure", ["Review", "Section 114", "Order XLVII", "Error Apparent", "Parsion Devi"])

    m("Revision under Section 115 of the CPC lies to the High Court in cases where an appeal lies to the High Court or subordinate court.",
      "false", "Code of Civil Procedure, 1908", "beginner", "Code of Civil Procedure, 1908", "Section 115(1)", None,
      "Section 115(1) CPC expressly restricts revisional jurisdiction: the High Court may call for the record of any case decided by subordinate court 'in which no appeal lies thereto.' Availability of an appeal totally bars revision.",
      "Lawyers sometimes file revision petitions even where a statutory appeal is provided.",
      "Revision is restricted to jurisdictional errors (exceeded, failed to exercise, or illegal exercise).",
      "lies to the High Court in cases where an appeal lies", "lies strictly in cases where no appeal lies to the High Court or subordinate court",
      U_CPC, "Current Civil Procedure", ["Revision", "Section 115", "Jurisdictional Error", "Bar on Revision", "CPC 1908"])

    m("Restitution under Section 144 of the CPC places parties in the position they would have occupied but for an erroneous decree that was varied or reversed.",
      "true", "Code of Civil Procedure, 1908", "intermediate", "Code of Civil Procedure, 1908", "Section 144", None,
      "Section 144 CPC codifies the equitable principle of restitution: where a decree is varied or reversed in appeal or revision, the court shall cause restitution to be made to place parties in the position they would have occupied.",
      "Based on the maxim 'actus curiae neminem gravabit' (act of court shall prejudice no one).",
      "Separate suit for restitution is barred under Section 144(2) CPC.",
      None, None,
      U_CPC, "Current Civil Procedure", ["Restitution", "Section 144", "Actus Curiae", "Reversal of Decree", "CPC 1908"])

    m("A Precept issued by a decree-holding court under Section 46 of the CPC remains in force for more than two months without an extension.",
      "false", "Code of Civil Procedure, 1908", "intermediate", "Code of Civil Procedure, 1908", "Section 46 proviso", None,
      "The proviso to Section 46 CPC expressly provides that no attachment under a precept shall continue for more than two months, unless the period is extended by the court which passed the decree or decree has been transferred.",
      "Precept is a temporary protective attachment issued to another court pending formal transfer.",
      "Ceases to have effect automatically after 2 months unless extended.",
      "remains in force for more than two months without an extension", "cannot continue for more than two months unless expressly extended under Section 46 proviso",
      U_CPC, "Current Civil Procedure", ["Precept", "Section 46", "Two Months Limitation", "Attachment", "CPC 1908"])

    m("A Garnishee Order under Order XXI Rule 46A of the CPC is an order directing the debtor of the judgment-debtor to pay the debt directly to court.",
      "true", "Code of Civil Procedure, 1908", "intermediate", "Code of Civil Procedure, 1908", "Order XXI Rule 46A", None,
      "Order XXI Rule 46A CPC provides for garnishee proceedings where a third party owing money to the judgment-debtor is ordered not to pay the judgment-debtor and to appear and show cause why they should not pay into court.",
      "Direct execution against debts due to the judgment-debtor.",
      "Garnishee can dispute liability, which court then tries as an issue.",
      None, None,
      U_CPC, "Current Civil Procedure", ["Garnishee Order", "Order XXI Rule 46A", "Execution", "Debtor of Judgment Debtor", "CPC 1908"])

    m("Resistance or obstruction to possession of immovable property in execution of a decree is adjudicated under Order XXI Rule 97 of the CPC.",
      "true", "Code of Civil Procedure, 1908", "intermediate", "Code of Civil Procedure, 1908", "Order XXI Rule 97", None,
      "Order XXI Rule 97 CPC provides that where decree-holder or purchaser is resisted or obstructed by any person in obtaining possession, they may apply to court. Under Rule 101, all questions including right, title, and interest are determined by executing court, not by a separate suit.",
      "Separate civil suit by third-party resister is barred; all issues must be determined under Rule 101.",
      "Decree passed under Rule 98/100 has the force of a regular appealable decree under Rule 103.",
      None, None,
      U_CPC, "Current Civil Procedure", ["Order XXI Rule 97", "Obstruction to Possession", "Rule 101", "Execution", "CPC 1908"])

    m("Mesne profits under Section 2(12) of the CPC include profits due to improvements made by the person in wrongful possession.",
      "false", "Code of Civil Procedure, 1908", "beginner", "Code of Civil Procedure, 1908", "Section 2(12)", None,
      "Section 2(12) CPC explicitly excludes profits due to improvements: mesne profits means profits which the person in wrongful possession actually received or might have received, 'together with interest on such profits, but shall not include profits due to improvements made by the person in wrongful possession.'",
      "A classic statutory trick question in UP PCS-J.",
      "Wrongful possessor is not penalized for value added by their own capital improvements.",
      "include profits due to improvements made by the person in wrongful possession", "strictly exclude profits due to improvements made by the person in wrongful possession",
      U_CPC, "Current Civil Procedure", ["Mesne Profits", "Section 2(12)", "Improvements Excluded", "Wrongful Possession", "CPC 1908"])

    m("A 'Legal Representative' under Section 2(11) of the CPC includes any person who intermeddles with the estate of the deceased.",
      "true", "Code of Civil Procedure, 1908", "beginner", "Code of Civil Procedure, 1908", "Section 2(11)", None,
      "Section 2(11) CPC defines legal representative as a person who in law represents the estate of a deceased person, 'and includes any person who intermeddles with the estate of the deceased.'",
      "Intermeddlers (executors de son tort) can be joined in execution to the extent of deceased assets in their hands.",
      "Protects decree-holders against clandestine dissipation of deceased assets.",
      None, None,
      U_CPC, "Current Civil Procedure", ["Legal Representative", "Section 2(11)", "Intermeddler", "Estate", "CPC 1908"])

    m("Under Section 56 of the CPC, the Court has discretion to order the arrest and civil prison detention of a woman in execution of a money decree.",
      "false", "Code of Civil Procedure, 1908", "beginner", "Code of Civil Procedure, 1908", "Section 56", None,
      "Section 56 CPC contains an absolute statutory prohibition: 'Notwithstanding anything in this Part, the Court shall not order the arrest or detention in the civil prison of a woman in execution of a decree for the payment of money.'",
      "Candidates assume civil arrest applies equally regardless of sex.",
      "Women can still have their property attached and sold in execution.",
      "has discretion to order the arrest and civil prison detention of a woman in execution of a money decree", "is strictly prohibited from arresting or detaining a woman in execution of a money decree",
      U_CPC, "Current Civil Procedure", ["Section 56", "Woman Arrest Prohibition", "Money Decree", "Civil Prison", "CPC 1908"])

    m("Property exempt from attachment and sale in execution under Section 60 of the CPC includes necessary wearing apparel, cooking vessels, and tools of artisans.",
      "true", "Code of Civil Procedure, 1908", "beginner", "Code of Civil Procedure, 1908", "Section 60(1) proviso", None,
      "Section 60(1) proviso CPC lists exempt properties: necessary wearing apparel, cooking vessels, beds, tools of artisans, implements of husbandry, books of account, and stipends/pensions.",
      "Humanitarian safeguard ensuring judgment-debtors and families are not reduced to absolute destitution.",
      "Salary is exempt up to first 1,000 rupees and two-thirds of remainder in non-maintenance decrees.",
      None, None,
      U_CPC, "Current Civil Procedure", ["Section 60", "Exempt Property", "Attachment", "Execution", "Humanitarian Safeguard"])

    m("An order granting or refusing an adjournment under Order XVII Rule 1 of the CPC can include an award of costs occasioned by the adjournment.",
      "true", "Code of Civil Procedure, 1908", "beginner", "Code of Civil Procedure, 1908", "Order XVII Rule 1(2)", None,
      "Order XVII Rule 1(2) CPC provides that the Court may grant time and adjourn the hearing, and 'shall make such order as to costs occasioned by the adjournment or higher costs as may be considered appropriate.'",
      "Designed to prevent frivolous dilatory tactics in civil courts.",
      "Rule 1(1) proviso stipulates no adjournment shall be granted more than three times to a party.",
      None, None,
      U_CPC, "Current Civil Procedure", ["Adjournment Costs", "Order XVII Rule 1", "Three Adjournments Cap", "Delay Prevention", "CPC 1908"])

    m("The summary procedure under Order XXXVII of the CPC applies to suits based upon bills of exchange, hundis, and promissory notes.",
      "true", "Code of Civil Procedure, 1908", "beginner", "Code of Civil Procedure, 1908", "Order XXXVII Rule 1", None,
      "Order XXXVII CPC provides a fast-track summary procedure for negotiable instruments and written contracts where defendant must obtain leave to defend within 10 days from service of summons.",
      "Defendant cannot defend suit as of right without showing bona fide defence.",
      "Failure to obtain leave entitles plaintiff to immediate judgment.",
      None, None,
      U_CPC, "Current Civil Procedure", ["Order XXXVII", "Summary Procedure", "Leave to Defend", "Negotiable Instruments", "Fast Track"])

    m("An order refusing to set aside the abatement or dismissal of a suit under Order XXII Rule 9 is appealable under Order XLIII Rule 1(k) of the CPC.",
      "true", "Code of Civil Procedure, 1908", "intermediate", "Code of Civil Procedure, 1908", "Order XLIII Rule 1(k)", None,
      "Order XLIII Rule 1(k) CPC provides that an appeal shall lie from an order under Rule 9 of Order XXII refusing to set aside the abatement or dismissal of a suit.",
      "Appeal from orders (Miscellaneous Appeals) lie only against orders enumerated in Section 104 and Order XLIII Rule 1.",
      "Non-appealable orders can only be challenged under Section 115 revision or Article 227.",
      None, None,
      U_CPC, "Current Civil Procedure", ["Appeal from Orders", "Order XLIII Rule 1", "Abatement Refusal", "Order XXII Rule 9", "CPC 1908"])

    m("A decree becomes executable immediately upon being signed, and filing an appeal automatically operates as an unconditional stay of execution.",
      "false", "Code of Civil Procedure, 1908", "beginner", "Code of Civil Procedure, 1908", "Order XLI Rule 5(1)", None,
      "Order XLI Rule 5(1) CPC explicitly declares: 'An appeal shall not operate as a stay of proceedings under a decree or order appealed from except so far as the Appellate Court may order.' Stay must be specifically applied for and ordered.",
      "Litigants wrongly assume the mere filing of an appeal halts execution automatically.",
      "Executing court may proceed with execution unless stay is formally communicated.",
      "and filing an appeal automatically operates as an unconditional stay of execution", "and filing an appeal does not operate as a stay of execution unless stay is expressly ordered under Order XLI Rule 5",
      U_CPC, "Current Civil Procedure", ["Stay of Execution", "Order XLI Rule 5", "Appellate Court", "No Automatic Stay", "CPC 1908"])

    m("Under Section 34 of the CPC, the court can award interest from the date of the suit to the date of decree at any arbitrary usurious rate chosen by the plaintiff.",
      "false", "Code of Civil Procedure, 1908", "beginner", "Code of Civil Procedure, 1908", "Section 34", None,
      "Section 34 CPC regulates interest: reasonable interest for pendente lite period, and post-decree interest not exceeding 6% per annum, except that in commercial transactions it may extend to the agreed contractual rate or nationalized bank lending rate.",
      "Usurious, exorbitant penalty rates are checked by statutory judicial limits.",
      "Post-decree interest is capped at 6% for non-commercial debts.",
      "at any arbitrary usurious rate chosen by the plaintiff", "subject to reasonable rates and statutory caps under Section 34",
      U_CPC, "Current Civil Procedure", ["Interest", "Section 34", "Pendente Lite", "Six Percent Cap", "Commercial Exception"])

    print("Part 2: 120 items registered.")
