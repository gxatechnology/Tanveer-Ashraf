import json
import os

items = []
current_id = 1

def item(stmt, classification, subject, diff, leg, sec, subsec, expl, mis_expl, exc, err_phrase, corr, url, legal_date, keywords, old_vs_new=None):
    global current_id
    items.append({
        "id": f"myth-{current_id:03d}",
        "statement": stmt,
        "classification": classification,
        "subject": subject,
        "difficulty": diff,
        "legislation": leg,
        "section": sec,
        "subsection": subsec,
        "explanation": expl,
        "misconceptionExplanation": mis_expl,
        "exceptions": exc,
        "errorPhrase": err_phrase,
        "correction": corr,
        "sourceUrl": url,
        "verificationDate": "2026-11-22",
        "applicableLegalDate": legal_date,
        "revisionKeywords": keywords,
        "oldVsNew": old_vs_new
    })
    current_id += 1

# =========================================================================
# 1. CONSTITUTIONAL LAW (35 statements)
# =========================================================================
item(
    stmt="Article 21 (Right to Life and Personal Liberty) can be suspended by Presidential Order during a National Emergency proclaimed under Article 352.",
    classification="false",
    subject="Constitutional Law",
    diff="beginner",
    leg="Constitution of India",
    sec="Article 359(1)",
    subsec=None,
    expl="Following the 44th Constitutional Amendment Act, 1978, the enforcement of Fundamental Rights under Articles 20 and 21 cannot be suspended even during a National Emergency.",
    mis_expl="Lay candidates often assume that all Fundamental Rights are suspended during a National Emergency under Article 352, forgetting the post-ADM Jabalpur constitutional safeguards introduced by the 44th Amendment.",
    exc="None. Articles 20 and 21 are non-derogable under Article 359.",
    err_phrase="can be suspended by Presidential Order",
    corr="cannot be suspended even during a National Emergency",
    url="https://www.indiacode.nic.in/handle/123456789/1522",
    legal_date="Current Constitutional Law",
    keywords=["Article 21", "Article 20", "Article 359", "44th Amendment", "National Emergency"]
)

item(
    stmt="A writ of Mandamus lies against a purely private company discharging no statutory or public duty.",
    classification="false",
    subject="Constitutional Law",
    diff="beginner",
    leg="Constitution of India",
    sec="Article 226",
    subsec=None,
    expl="Mandamus is a public law remedy that compels the performance of a public or statutory duty. It does not lie against a private entity unless it is discharging a public function or statutory obligation.",
    mis_expl="Because High Courts have wide jurisdiction under Article 226 against 'any person or authority', aspirants sometimes mistakenly believe private contractual disputes can be enforced via Mandamus.",
    exc="Mandamus may lie against a private body if it performs an imperative public duty or operates under statutory command (Federal Bank v. Sagar Thomas).",
    err_phrase="lies against a purely private company",
    corr="does not lie against purely private bodies with no public duties",
    url="https://www.indiacode.nic.in/handle/123456789/1522",
    legal_date="Current Constitutional Law",
    keywords=["Mandamus", "Article 226", "Article 32", "Public Duty", "Private Body"]
)

item(
    stmt="The Preamble is an integral part of the Constitution and can be amended under Article 368 without altering the Basic Structure.",
    classification="true",
    subject="Constitutional Law",
    diff="beginner",
    leg="Constitution of India",
    sec="Preamble & Article 368",
    subsec=None,
    expl="In Kesavananda Bharati v. State of Kerala (1973), the Supreme Court held that the Preamble is part of the Constitution and can be amended under Article 368, provided the Basic Structure is not destroyed. It was amended once by the 42nd Amendment Act, 1976.",
    mis_expl="Some rely on the earlier Berubari Union (1960) advisory opinion which held that the Preamble was not part of the Constitution.",
    exc="Amendments cannot destroy basic features such as secularism, democracy, or judicial review.",
    err_phrase=None,
    corr=None,
    url="https://www.indiacode.nic.in/handle/123456789/1522",
    legal_date="Current Constitutional Law",
    keywords=["Preamble", "Kesavananda Bharati", "Article 368", "Basic Structure", "42nd Amendment"]
)

item(
    stmt="The President of India can grant pardon in cases of death sentence, whereas the Governor of a State has no power whatsoever regarding capital punishment.",
    classification="false",
    subject="Constitutional Law",
    diff="intermediate",
    leg="Constitution of India",
    sec="Article 72 & Article 161",
    subsec=None,
    expl="While only the President can pardon a death sentence under Article 72, the Governor under Article 161 has the constitutional power to suspend, remit, or commute a sentence of death in respect of matters extending to the executive power of the State.",
    mis_expl="Many confuse the exclusive power to pardon (complete forgiveness) with the powers of remission, commutation, or suspension of death sentences, which the Governor does possess.",
    exc="The Governor cannot grant an absolute pardon in death penalty cases, but can commute the death sentence to life imprisonment.",
    err_phrase="has no power whatsoever regarding capital punishment",
    corr="has the power to suspend, remit, or commute a sentence of death",
    url="https://www.indiacode.nic.in/handle/123456789/1522",
    legal_date="Current Constitutional Law",
    keywords=["Pardon", "Article 72", "Article 161", "Governor", "Commutation", "Death Sentence"]
)

item(
    stmt="The Fundamental Right to Property under Article 31 remains enforceable as a Fundamental Right under Part III of the Constitution.",
    classification="false",
    subject="Constitutional Law",
    diff="beginner",
    leg="Constitution of India",
    sec="Article 300A",
    subsec=None,
    expl="The 44th Constitutional Amendment Act, 1978 repealed Article 19(1)(f) and Article 31, transforming the right to property into a constitutional/legal right under Article 300A in Part XII.",
    mis_expl="Candidates sometimes confuse a constitutional right under Article 300A with an enforceable Fundamental Right under Part III.",
    exc="Property rights cannot be deprived save by authority of law, but do not enjoy direct Article 32 writ protection.",
    err_phrase="remains enforceable as a Fundamental Right under Part III",
    corr="is a constitutional right under Article 300A outside Part III",
    url="https://www.indiacode.nic.in/handle/123456789/1522",
    legal_date="Current Constitutional Law",
    keywords=["Property", "Article 300A", "44th Amendment", "Fundamental Rights", "Part III"]
)

item(
    stmt="A Money Bill can only be introduced in the Lok Sabha and cannot be rejected or amended by the Rajya Sabha.",
    classification="true",
    subject="Constitutional Law",
    diff="beginner",
    leg="Constitution of India",
    sec="Article 109 & Article 110",
    subsec=None,
    expl="Under Article 109, a Money Bill cannot be introduced in the Council of States. The Rajya Sabha has only 14 days to return it with recommendations, which the Lok Sabha may accept or reject.",
    mis_expl="Some believe the Rajya Sabha has equal veto powers over all financial legislation.",
    exc="The Speaker's decision certifying a bill as a Money Bill under Article 110(3) is final, subject to limited judicial review.",
    err_phrase=None,
    corr=None,
    url="https://www.indiacode.nic.in/handle/123456789/1522",
    legal_date="Current Constitutional Law",
    keywords=["Money Bill", "Article 109", "Article 110", "Lok Sabha", "Rajya Sabha"]
)

item(
    stmt="An ordinance promulgated by the President under Article 123 has the same force and effect as an Act of Parliament.",
    classification="true",
    subject="Constitutional Law",
    diff="beginner",
    leg="Constitution of India",
    sec="Article 123",
    subsec="2",
    expl="Under Article 123(2), an ordinance promulgated during parliamentary recess has the same force and effect as an Act of Parliament, but must be laid before both Houses and ceases to operate after 6 weeks from reassembly.",
    mis_expl="Ordinance power is often mistakenly viewed as inferior subordinate legislation rather than primary legislation of temporary duration.",
    exc="An ordinance cannot abridge Fundamental Rights and is subject to the same constitutional limitations as an Act of Parliament (D.C. Wadhwa v. State of Bihar).",
    err_phrase=None,
    corr=None,
    url="https://www.indiacode.nic.in/handle/123456789/1522",
    legal_date="Current Constitutional Law",
    keywords=["Ordinance", "Article 123", "President", "Parliament", "D.C. Wadhwa"]
)

item(
    stmt="The doctrine of severability allows a court to strike down an entire statute if a single clause violates a Fundamental Right, regardless of whether the valid portions can stand independently.",
    classification="false",
    subject="Constitutional Law",
    diff="intermediate",
    leg="Constitution of India",
    sec="Article 13(1) & (2)",
    subsec=None,
    expl="The doctrine of severability under Article 13 provides that only the unconstitutional portion is void, provided the valid and invalid portions are separable and the valid remainder can give effect to legislative intent (R.M.D.C. v. Union of India).",
    mis_expl="Aspirants sometimes confuse total unconstitutionality with partial invalidity under severability.",
    exc="If the valid and invalid provisions are inextricably bound together such that Parliament would not have enacted the valid part alone, the entire statute falls.",
    err_phrase="strike down an entire statute if a single clause violates a Fundamental Right, regardless of whether the valid portions can stand independently",
    corr="strike down only the unconstitutional provision if the valid remainder can stand independently",
    url="https://www.indiacode.nic.in/handle/123456789/1522",
    legal_date="Current Constitutional Law",
    keywords=["Severability", "Article 13", "RMDC", "Unconstitutionality", "Fundamental Rights"]
)

item(
    stmt="A person who is acquitted in a criminal trial cannot be subjected to disciplinary departmental proceedings on the exact same charges.",
    classification="false",
    subject="Constitutional Law & Service Law",
    diff="intermediate",
    leg="Constitution of India",
    sec="Article 20(2) & Article 311",
    subsec=None,
    expl="Departmental inquiry and criminal prosecution operate in distinct fields with different standards of proof: criminal trial requires proof beyond reasonable doubt, while departmental inquiry operates on preponderance of probabilities.",
    mis_expl="Double jeopardy under Article 20(2) applies strictly to prosecution and punishment before a court of law, not to departmental disciplinary actions.",
    exc="If the criminal acquittal was honorable and based on finding the allegations utterly false, continuation of departmental inquiry on identical evidence may be quashed (Capt. M. Paul Anthony v. Bharat Gold Mines).",
    err_phrase="cannot be subjected to disciplinary departmental proceedings",
    corr="can be subjected to departmental proceedings because standards of proof differ",
    url="https://www.indiacode.nic.in/handle/123456789/1522",
    legal_date="Current Constitutional Law",
    keywords=["Double Jeopardy", "Article 20(2)", "Departmental Inquiry", "Preponderance of Probabilities", "Acquittal"]
)

item(
    stmt="The Directive Principles of State Policy under Part IV are fundamental in the governance of the country and are directly enforceable in any court of law.",
    classification="false",
    subject="Constitutional Law",
    diff="beginner",
    leg="Constitution of India",
    sec="Article 37",
    subsec=None,
    expl="Article 37 explicitly declares that Directive Principles of State Policy shall not be enforceable by any court, though they are fundamental in the governance of the country and it shall be the duty of the State to apply them in making laws.",
    mis_expl="Candidates confuse the aspirational duty of the State with legal enforceability through writ petitions.",
    exc="Courts use DPSPs to interpret Fundamental Rights expansively (e.g., Article 21 read with Article 39(e)).",
    err_phrase="are directly enforceable in any court of law",
    corr="are non-justiciable and cannot be enforced directly in any court",
    url="https://www.indiacode.nic.in/handle/123456789/1522",
    legal_date="Current Constitutional Law",
    keywords=["DPSPs", "Article 37", "Part IV", "Enforceability", "Justiciability"]
)

# Output test
print(f"Authored initial {len(items)} items. Writing full generator script...")
