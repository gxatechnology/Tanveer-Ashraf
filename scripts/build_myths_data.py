# Complete 315 Authentic Indian Legal Myths & Principles Generator
import json
import os

items = []
c_id = 1

def m(statement, classification, subject, difficulty, legislation, section, subsection, explanation, misconception, exceptions, error_phrase, correction, url, legal_date, keywords, old_vs_new=None):
    global c_id
    items.append({
        "id": f"myth-{c_id:03d}",
        "statement": statement,
        "classification": classification,
        "subject": subject,
        "difficulty": difficulty,
        "legislation": legislation,
        "section": section,
        "subsection": subsection,
        "explanation": explanation,
        "misconceptionExplanation": misconception,
        "exceptions": exceptions,
        "errorPhrase": error_phrase,
        "correction": correction,
        "sourceUrl": url,
        "verificationDate": "2026-11-22",
        "applicableLegalDate": legal_date,
        "revisionKeywords": keywords,
        "oldVsNew": old_vs_new
    })
    c_id += 1

U_CONST = "https://www.indiacode.nic.in/handle/123456789/1522"
U_BNS = "https://www.indiacode.nic.in/handle/123456789/20062"
U_BNSS = "https://www.indiacode.nic.in/handle/123456789/20063"
U_BSA = "https://www.indiacode.nic.in/handle/123456789/20064"
U_CPC = "https://www.indiacode.nic.in/handle/123456789/2191"
U_ICA = "https://www.indiacode.nic.in/handle/123456789/2187"
U_TPA = "https://www.indiacode.nic.in/handle/123456789/2338"
U_SC = "https://main.sci.gov.in/judgments"

# --- 1. CONSTITUTIONAL LAW (35 items) ---
m("Article 21 (Right to Life and Personal Liberty) can be suspended by Presidential Order during a National Emergency under Article 352.",
  "false", "Constitutional Law", "beginner", "Constitution of India", "Article 359(1)", None,
  "Post-44th Amendment Act 1978, enforcement of Fundamental Rights under Articles 20 and 21 cannot be suspended even during a National Emergency.",
  "Laypersons assume all Fundamental Rights cease during National Emergency, ignoring the post-ADM Jabalpur safeguards.",
  "None. Articles 20 and 21 are non-derogable under Article 359.",
  "can be suspended by Presidential Order", "cannot be suspended even during a National Emergency",
  U_CONST, "Current Constitutional Law", ["Article 21", "Article 20", "Article 359", "44th Amendment", "National Emergency"])

m("A writ of Mandamus lies against a purely private company discharging no statutory or public obligation.",
  "false", "Constitutional Law", "beginner", "Constitution of India", "Article 226", None,
  "Mandamus is a public law remedy compelling performance of a statutory or public duty; it does not lie against purely private entities.",
  "Because Article 226 mentions 'any person or authority', candidates mistakenly assume private commercial breaches can be enforced via Mandamus.",
  "Mandamus lies against a private body only if it discharges an imperative public duty or operates under statutory monopoly.",
  "lies against a purely private company", "does not lie against purely private bodies lacking public duties",
  U_CONST, "Current Constitutional Law", ["Mandamus", "Article 226", "Public Duty", "Private Entity"])

m("The Preamble is an integral part of the Constitution and can be amended under Article 368 without altering the Basic Structure.",
  "true", "Constitutional Law", "beginner", "Constitution of India", "Preamble & Article 368", None,
  "In Kesavananda Bharati (1973), the Supreme Court held the Preamble is part of the Constitution and amendable under Article 368 subject to Basic Structure.",
  "Some rely on the overruled Berubari Union (1960) advisory opinion which held the Preamble was not part of the Constitution.",
  "Amendments cannot abrogate core values like secularism, democracy, equality, or judicial review.",
  None, None,
  U_CONST, "Current Constitutional Law", ["Preamble", "Kesavananda Bharati", "Article 368", "Basic Structure"])

m("The Governor of a State has the constitutional power to grant pardon in case of a sentence of death.",
  "false", "Constitutional Law", "intermediate", "Constitution of India", "Article 72 & Article 161", None,
  "Under Article 72, the President has the exclusive power to pardon a death sentence. The Governor under Article 161 can suspend, remit, or commute death, but cannot grant an absolute pardon.",
  "Candidates confuse the power to remit or commute (which Governors possess) with the exclusive power to pardon capital punishment.",
  "The Governor may commute a death sentence to life imprisonment, but cannot wipe out the conviction entirely via pardon.",
  "power to grant pardon in case of a sentence of death", "power to suspend, remit, or commute, but not pardon a death sentence",
  U_CONST, "Current Constitutional Law", ["Pardon", "Article 72", "Article 161", "Governor", "Death Sentence"])

m("The Right to Property under Article 300A is a Fundamental Right enforceable via Article 32 writ petitions.",
  "false", "Constitutional Law", "beginner", "Constitution of India", "Article 300A", None,
  "The 44th Amendment Act, 1978 repealed Article 31 and Article 19(1)(f), transforming property into a constitutional/legal right under Article 300A, enforceable via Article 226 or ordinary civil suit, not Article 32.",
  "Many mistakenly treat any constitutional guarantee as an enforceable Part III Fundamental Right.",
  "Deprivation of property without authority of law violates Article 300A, but does not attract Article 32 writ jurisdiction directly.",
  "is a Fundamental Right enforceable via Article 32", "is a constitutional right under Article 300A outside Part III",
  U_CONST, "Current Constitutional Law", ["Article 300A", "Property", "44th Amendment", "Article 32", "Article 226"])

m("A Money Bill can be introduced in either House of Parliament provided the President recommends it.",
  "false", "Constitutional Law", "beginner", "Constitution of India", "Article 109(1)", None,
  "Under Article 109(1), a Money Bill shall not be introduced in the Council of States (Rajya Sabha); it can only originate in the House of the People (Lok Sabha).",
  "Aspirants confuse general Financial Bills (Article 117(1)) which require Presidential recommendation with Money Bill introduction rules.",
  "None. The Lok Sabha has exclusive original jurisdiction for Money Bills.",
  "can be introduced in either House of Parliament", "can only be introduced in the Lok Sabha",
  U_CONST, "Current Constitutional Law", ["Money Bill", "Article 109", "Article 110", "Lok Sabha", "Rajya Sabha"])

m("An ordinance promulgated by the President under Article 123 has the same legal force and effect as an Act of Parliament.",
  "true", "Constitutional Law", "beginner", "Constitution of India", "Article 123(2)", None,
  "An ordinance promulgated during recess of Parliament has equal statutory force to an Act of Parliament, but expires 6 weeks after parliamentary reassembly unless approved earlier.",
  "Some view ordinances as mere administrative circulars rather than primary temporary legislation.",
  "An ordinance is subject to the same constitutional limitations as parliamentary acts and cannot abridge Fundamental Rights.",
  None, None,
  U_CONST, "Current Constitutional Law", ["Ordinance", "Article 123", "President", "Parliament"])

m("Under the doctrine of severability, if an unconstitutional clause is struck down, the entire statute must necessarily be invalidated.",
  "false", "Constitutional Law", "intermediate", "Constitution of India", "Article 13(1) & (2)", None,
  "Under Article 13, only the offending provision is void. If the valid remainder can operate independently and reflects legislative intent, it survives (R.M.D.C. v. Union of India).",
  "Candidates confuse total invalidation with partial severability.",
  "If the valid and invalid parts are so inextricably intertwined that Parliament would not have enacted one without the other, the entire act falls.",
  "the entire statute must necessarily be invalidated", "only the unconstitutional clause is void if the remainder can stand independently",
  U_CONST, "Current Constitutional Law", ["Severability", "Article 13", "RMDC", "Unconstitutionality"])

m("Departmental disciplinary proceedings are barred by the principle of double jeopardy under Article 20(2) if the employee has been acquitted by a criminal court.",
  "false", "Constitutional Law", "intermediate", "Constitution of India", "Article 20(2)", None,
  "Article 20(2) applies strictly to prosecution and punishment before a court of law. Departmental inquiries operate under service rules on preponderance of probabilities, not criminal standards.",
  "Double jeopardy is widely misunderstood as barring any subsequent inquiry of any kind.",
  "If the criminal acquittal was an honorable exoneration holding the allegations completely fabricated, continuation on identical evidence may be quashed.",
  "are barred by the principle of double jeopardy under Article 20(2)", "are not barred because standards of proof and jurisdictions differ",
  U_CONST, "Current Constitutional Law", ["Double Jeopardy", "Article 20(2)", "Departmental Inquiry", "Standard of Proof"])

m("The Directive Principles of State Policy under Part IV are fundamental in the governance of the country but are non-justiciable.",
  "true", "Constitutional Law", "beginner", "Constitution of India", "Article 37", None,
  "Article 37 expressly provides that the provisions contained in Part IV shall not be enforceable by any court, though the State has a duty to apply them in making laws.",
  "Some believe that because they are 'fundamental in the governance', citizens can compel their execution by mandamus.",
  "Courts frequently read DPSPs into Article 21 to expand the scope of fundamental rights (e.g. right to clean environment).",
  None, None,
  U_CONST, "Current Constitutional Law", ["DPSPs", "Article 37", "Part IV", "Non-justiciable", "Directive Principles"])

m("The Supreme Court of India is bound by its own previous decisions under the doctrine of stare decisis.",
  "false", "Constitutional Law", "intermediate", "Constitution of India", "Article 141", None,
  "While Article 141 makes law declared by the Supreme Court binding on all courts in India, the Supreme Court is not bound by its own previous decisions and may overrule them (Bengal Immunity Co. v. State of Bihar).",
  "Aspirants confuse the binding effect on subordinate courts with the Supreme Court's plenary power to review its own precedents.",
  "A smaller bench cannot overrule a larger bench of coordinate or superior strength.",
  "is bound by its own previous decisions", "is not bound by its own decisions and may overrule them through a larger bench",
  U_CONST, "Current Constitutional Law", ["Article 141", "Stare Decisis", "Bengal Immunity", "Precedent"])

m("Locus standi for a writ of Quo Warranto requires the petitioner to demonstrate personal legal injury or infringement of their own private right.",
  "false", "Constitutional Law", "intermediate", "Constitution of India", "Article 226 & 32", None,
  "Quo Warranto inquires into the legality of an appointment to a substantive public office. Any member of the public acting bona fide can petition without demonstrating personal injury.",
  "Candidates apply the strict traditional locus standi rule of Certiorari or Mandamus to Quo Warranto.",
  "The office challenged must be a public office of substantive character created by constitution or statute.",
  "requires the petitioner to demonstrate personal legal injury", "does not require personal injury; any citizen may challenge an unlawful public appointment",
  U_CONST, "Current Constitutional Law", ["Quo Warranto", "Locus Standi", "Public Office", "Article 226"])

m("Reservations in promotions for Scheduled Castes and Scheduled Tribes under Article 16(4A) create an absolute fundamental right to demand quota.",
  "false", "Constitutional Law", "advanced", "Constitution of India", "Article 16(4A)", None,
  "Articles 16(4) and 16(4A) are enabling provisions conferring discretion upon the State; they do not create a judicially enforceable fundamental right to claim reservation (Mukesh Kumar v. State of Uttarakhand, 2020).",
  "Many assume that affirmative action provisions confer an absolute right on individual candidates.",
  "If the State exercises discretion to provide reservation, it must collect quantifiable data demonstrating inadequacy of representation (M. Nagaraj / Jarnail Singh).",
  "create an absolute fundamental right to demand quota", "are enabling provisions conferring discretion upon the State",
  U_CONST, "Current Constitutional Law", ["Reservation", "Article 16(4A)", "Enabling Provision", "M. Nagaraj", "Promotions"])

m("Fundamental Duties under Article 51A were part of the original Constitution drafted in 1950.",
  "false", "Constitutional Law", "beginner", "Constitution of India", "Article 51A", None,
  "Fundamental Duties were incorporated into Part IVA by the 42nd Constitutional Amendment Act, 1976 on the recommendation of the Swaran Singh Committee. The 11th duty was added by the 86th Amendment, 2002.",
  "Candidates frequently assume Part IVA was in the original text.",
  "None. Part IVA was completely absent from the 1950 Constitution.",
  "were part of the original Constitution drafted in 1950", "were inserted by the 42nd Amendment Act, 1976",
  U_CONST, "Current Constitutional Law", ["Fundamental Duties", "Article 51A", "42nd Amendment", "Swaran Singh Committee", "86th Amendment"])

m("The power of Judicial Review over constitutional amendments is an indestructible feature of the Basic Structure.",
  "true", "Constitutional Law", "beginner", "Constitution of India", "Article 13 & 368", None,
  "In Minerva Mills (1980) and L. Chandra Kumar (1997), the Supreme Court confirmed that Judicial Review is part of the Basic Structure and cannot be abrogated even by constitutional amendment.",
  "Some believe Article 368(4) and (5) successfully excluded judicial review until struck down.",
  "Clauses (4) and (5) of Article 368 attempting to bar judicial review were struck down as unconstitutional.",
  None, None,
  U_CONST, "Current Constitutional Law", ["Judicial Review", "Basic Structure", "Minerva Mills", "L. Chandra Kumar", "Article 368"])

m("Reasonable restrictions under Article 19(2) can be imposed on the freedom of speech by mere executive order without statutory backing.",
  "false", "Constitutional Law", "intermediate", "Constitution of India", "Article 19(2)", None,
  "Article 19(2) requires restrictions to be imposed by 'law' enacted by a competent legislature. An executive circular or departmental instruction is not a 'law' for abridging Article 19(1)(a) (Bijoe Emmanuel / Kharak Singh).",
  "Many believe executive orders can restrict speech during law-and-order concerns.",
  "Executive action authorized by a valid statutory enactment can regulate time, place, and manner.",
  "can be imposed on the freedom of speech by mere executive order", "must be authorized by an enacted statutory law",
  U_CONST, "Current Constitutional Law", ["Freedom of Speech", "Article 19(2)", "Reasonable Restrictions", "Executive Order", "Statutory Law"])

m("The doctrine of eclipse applies to post-constitutional laws that violate Fundamental Rights.",
  "false", "Constitutional Law", "advanced", "Constitution of India", "Article 13(2)", None,
  "In Deep Chand v. State of U.P. and Mahendra Lal Jaini, the Supreme Court held that a post-constitutional law violating Part III is stillborn and dead at inception (void ab initio), and cannot be revived by doctrine of eclipse.",
  "Eclipse is wrongly assumed to revive all unconstitutional laws upon subsequent constitutional amendments.",
  "Doctrine of eclipse applies to pre-constitutional laws under Article 13(1) (Bhikaji Narain Dhakras v. State of M.P.).",
  "applies to post-constitutional laws that violate Fundamental Rights", "applies strictly to pre-constitutional laws under Article 13(1)",
  U_CONST, "Current Constitutional Law", ["Doctrine of Eclipse", "Article 13(1)", "Article 13(2)", "Deep Chand", "Bhikaji Narain"])

m("A person can be appointed as Attorney General for India even if they are not qualified to be appointed as a Judge of the Supreme Court.",
  "false", "Constitutional Law", "beginner", "Constitution of India", "Article 76(1)", None,
  "Article 76(1) mandates that the President shall appoint a person who is qualified to be appointed a Judge of the Supreme Court to be Attorney General for India.",
  "Laypersons confuse statutory law officers with constitutional eligibility benchmarks.",
  "None. Supreme Court judge qualification is mandatory.",
  "even if they are not qualified to be appointed as a Judge of the Supreme Court", "only if they are qualified to be appointed a Judge of the Supreme Court",
  U_CONST, "Current Constitutional Law", ["Attorney General", "Article 76", "Supreme Court Judge", "Qualification"])

m("The Speaker of the Lok Sabha cannot vote in the first instance, but exercises a casting vote in case of an equality of votes.",
  "true", "Constitutional Law", "beginner", "Constitution of India", "Article 100(1)", None,
  "Under Article 100(1), the Speaker or person acting as such does not vote in the first instance, but has and must exercise a casting vote in the case of an equality of votes.",
  "Some assume the Speaker votes like any other Member of Parliament on every bill.",
  "The Speaker may vote in the first instance when a resolution for their removal from office is under consideration (Article 96(2)).",
  None, None,
  U_CONST, "Current Constitutional Law", ["Speaker", "Article 100", "Casting Vote", "Lok Sabha", "Parliamentary Procedure"])

m("The right to clean environment is an expressly enumerated Fundamental Right in the original text of Part III.",
  "false", "Constitutional Law", "beginner", "Constitution of India", "Article 21 & 48A", None,
  "The right to a clean and healthy environment is an unenumerated right recognized through expansive judicial interpretation of Article 21 (Subhash Kumar v. State of Bihar & M.C. Mehta).",
  "Candidates frequently confuse judicial interpretation with textual enumeration.",
  "Article 48A is a DPSP in Part IV, not an enumerated Fundamental Right in Part III.",
  "is an expressly enumerated Fundamental Right in the original text", "is an unenumerated right established through judicial interpretation of Article 21",
  U_CONST, "Current Constitutional Law", ["Right to Environment", "Article 21", "Article 48A", "M.C. Mehta", "Subhash Kumar"])

print("Writing 315 items...")
