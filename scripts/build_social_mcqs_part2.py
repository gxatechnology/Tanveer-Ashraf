"""
Build Social MCQs Part 2: Acts 4-6
- Act 4: Protection of Women from Domestic Violence Act, 2005 (50 MCQs: mcq-dv-01-001 to mcq-dv-01-050)
- Act 5: Sexual Harassment of Women at Workplace Act, 2013 (50 MCQs: mcq-posh-01-001 to mcq-posh-01-050)
- Act 6: Pre-Conception and Pre-Natal Diagnostic Techniques Act, 1994 (50 MCQs: mcq-pcpndt-01-001 to mcq-pcpndt-01-050)
Total: 150 MCQs
"""

import json
import os

mcqs = []

def make_q(qid, sid, cid, tid, stem, opts, ans_idx, exp, breakdown, diff, prov, obj):
    letters = ["A", "B", "C", "D"]
    return {
        "id": qid,
        "subjectId": sid,
        "chapterId": cid,
        "topicId": tid,
        "question": stem,
        "options": opts,
        "answer": ans_idx,
        "answerLetter": letters[ans_idx],
        "explanation": exp,
        "optionBreakdown": breakdown,
        "difficulty": diff,
        "provision": prov,
        "sourceUrl": "https://www.indiacode.nic.in",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": obj,
        "eligible": True,
        "status": "active"
    }

# ==============================================================================
# ACT 4: Protection of Women from Domestic Violence Act, 2005 (soc-domestic-violence)
# 50 MCQs: mcq-dv-01-001 to mcq-dv-01-050
# ==============================================================================

# Topic top-dv-01-01 (6 MCQs)
mcqs.append(make_q(
    "mcq-dv-01-001", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-01",
    "On which date did the Protection of Women from Domestic Violence Act, 2005 come into force throughout India?",
    ["13 September 2005", "26 October 2006", "1 January 2006", "15 August 2007"],
    1,
    "The PWDVA was enacted in September 2005 and officially brought into force on 26 October 2006 by Central Government notification.",
    {
        "A": "Incorrect; 13 September 2005 was the date of Presidential assent.",
        "B": "Correct; The Act came into force on 26 October 2006.",
        "C": "Incorrect; 1 January 2006 is not the statutory commencement date.",
        "D": "Incorrect; 15 August 2007 is irrelevant."
    },
    "Foundational", "PWDVA S. 1(3)", "Identify commencement date of PWDVA 2005."
))

mcqs.append(make_q(
    "mcq-dv-01-002", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-01",
    "What is the core legislative objective of the Protection of Women from Domestic Violence Act, 2005?",
    [
        "To provide a civil law remedy of protection and relief for female victims of domestic violence without criminalising ordinary family life per se",
        "To establish criminal sentencing guidelines for matrimonial disputes",
        "To replace the Hindu Marriage Act in matrimonial property distribution",
        "To grant police officers summary power to dissolve marriages"
    ],
    0,
    "PWDVA is essentially a civil remedial statute designed to provide emergency protection, residence, and monetary relief to women facing domestic violence, retaining criminal penalties only for breach of protection orders.",
    {
        "A": "Correct; PWDVA creates civil rights and emergency reliefs with penal backup for non-compliance.",
        "B": "Incorrect; Section 498A IPC deals with criminal cruelty, whereas PWDVA focuses on civil remedies.",
        "C": "Incorrect; It does not repeal or replace the Hindu Marriage Act.",
        "D": "Incorrect; Police cannot dissolve marriages under any law."
    },
    "Foundational", "PWDVA Preamble", "Understand civil remedial nature of PWDVA."
))

mcqs.append(make_q(
    "mcq-dv-01-003", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-01",
    "Which constitutional provisions directly underpin the enactment of the Protection of Women from Domestic Violence Act, 2005?",
    [
        "Articles 14, 15(3) and 21 of the Constitution",
        "Articles 25 and 26 of the Constitution",
        "Articles 311 and 312 of the Constitution",
        "Articles 352 and 356 of the Constitution"
    ],
    0,
    "The Act is an affirmative statutory measure anchored in Article 15(3) (special provisions for women) read with Article 14 (equality) and Article 21 (right to live with dignity free from violence).",
    {
        "A": "Correct; Articles 14, 15(3), and 21 provide the constitutional foundation for PWDVA.",
        "B": "Incorrect; Articles 25-26 deal with religious freedoms.",
        "C": "Incorrect; Articles 311-312 govern civil services.",
        "D": "Incorrect; Articles 352-356 relate to emergency powers."
    },
    "Standard", "Constitution Arts. 14, 15(3), 21 & PWDVA Preamble", "Identify constitutional basis of PWDVA."
))

mcqs.append(make_q(
    "mcq-dv-01-004", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-01",
    "How does the nature of relief under PWDVA 2005 differ fundamentally from Section 498A of the IPC / Section 85-86 of the BNS?",
    [
        "Section 498A IPC / 85 BNS is purely penal focusing on punishment, whereas PWDVA provides progressive civil reliefs including protection, residence, custody, and compensation",
        "There is no difference; both are identical criminal trial codes",
        "PWDVA is strictly a criminal trial conducted by Sessions Judges",
        "Section 498A provides monetary maintenance, while PWDVA sentences accused to prison"
    ],
    0,
    "While Section 498A IPC is a criminal offence punishing cruelty with imprisonment, PWDVA 2005 provides multifaceted civil and restorative reliefs to secure immediate safety, shelter, and financial stability.",
    {
        "A": "Correct; PWDVA provides affirmative civil remedies, while 498A IPC is retributive criminal law.",
        "B": "Incorrect; The two statutes serve distinct legal purposes.",
        "C": "Incorrect; PWDVA proceedings are initiated before Judicial Magistrates under summary civil-hybrid procedure.",
        "D": "Incorrect; Section 498A does not award maintenance."
    },
    "Standard", "PWDVA Scheme & IPC S. 498A", "Distinguish civil remedies of PWDVA from criminal cruelty."
))

mcqs.append(make_q(
    "mcq-dv-01-005", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-01",
    "Under Section 2(a) of PWDVA 2005, who is an 'aggrieved person'?",
    [
        "Any woman who is, or has been, in a domestic relationship with the respondent and who alleges to have been subjected to any act of domestic violence",
        "Only a legally wedded wife living in her matrimonial home",
        "Any male or female relative residing in a joint family",
        "Any person who witnessed domestic abuse in their neighbourhood"
    ],
    0,
    "Section 2(a) defines 'aggrieved person' as any woman who is, or has been, in a domestic relationship with the respondent and who alleges to have been subjected to any act of domestic violence.",
    {
        "A": "Correct; Verbatim statutory definition under Section 2(a).",
        "B": "Incorrect; Mothers, sisters, daughters, and women in relationships in the nature of marriage are also included.",
        "C": "Incorrect; The aggrieved person under PWDVA must be a woman.",
        "D": "Incorrect; Bystanders/witnesses cannot be aggrieved persons."
    },
    "Foundational", "PWDVA S. 2(a)", "Know definition of aggrieved person under Section 2(a)."
))

mcqs.append(make_q(
    "mcq-dv-01-006", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-01",
    "In Hiral P. Harsora v. Kusum Narottamdas Harsora (2016), what vital statutory phrase in Section 2(q) of PWDVA was struck down by the Supreme Court?",
    [
        "The words 'adult male' in the definition of respondent",
        "The words 'in a domestic relationship'",
        "The words 'shared household'",
        "The words 'protection officer'"
    ],
    0,
    "In Hiral P. Harsora (2016) 10 SCC 165, the Supreme Court struck down the words 'adult male' from Section 2(q), permitting an aggrieved woman to file complaints against female relatives as well (e.g., mother-in-law, sister-in-law).",
    {
        "A": "Correct; Striking down 'adult male' allows women to be named as respondents in domestic violence proceedings.",
        "B": "Incorrect; 'Domestic relationship' remains a core statutory requirement.",
        "C": "Incorrect; 'Shared household' remains intact.",
        "D": "Incorrect; Protection officers are central to the statutory architecture."
    },
    "Advanced", "PWDVA S. 2(q) & Hiral P. Harsora (2016)", "Identify landmark ruling on gender neutrality of respondent."
))

# Topic top-dv-01-02 (6 MCQs)
mcqs.append(make_q(
    "mcq-dv-01-007", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-02",
    "Under Section 2(f) of PWDVA 2005, a 'domestic relationship' means a relationship between two persons who live or have, at any point of time, lived together in a shared household, when they are related by:",
    [
        "Consanguinity, marriage, or through a relationship in the nature of marriage, adoption or are family members living together as a joint family",
        "Commercial employment contract or tenancy lease",
        "Common business partnership only",
        "Residing in the same apartment building complex"
    ],
    0,
    "Section 2(f) sets out five categories: consanguinity (blood), marriage, relationship in the nature of marriage, adoption, or joint family membership.",
    {
        "A": "Correct; Complete statutory list of connections recognized in Section 2(f).",
        "B": "Incorrect; Employment and tenancy are contractual, not domestic.",
        "C": "Incorrect; Business partnerships do not create domestic relationships.",
        "D": "Incorrect; Neighbourhood co-residence is not a domestic relationship."
    },
    "Foundational", "PWDVA S. 2(f)", "Know definition of domestic relationship under Section 2(f)."
))

mcqs.append(make_q(
    "mcq-dv-01-008", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-02",
    "In D. Velusamy v. D. Patchaiammal (2010), what criteria did the Supreme Court establish for a relationship to qualify as a 'relationship in the nature of marriage' under PWDVA?",
    [
        "Couple must hold themselves out to society as spouses, be of legal age to marry, qualified to marry, and cohabited voluntarily for a significant period",
        "Couple must merely have had casual weekend sexual relations",
        "Couple must have executed a formal friendship contract",
        "One partner must be financially dependent on the other for at least one month"
    ],
    0,
    "In D. Velusamy (2010) 10 SCC 469, Markandey Katju, J., established four tests: holding out to society as spouses, legal age to marry, legal qualification to marry, and pooling resources/living together for a significant period.",
    {
        "A": "Correct; Four essential criteria laid down in D. Velusamy (2010).",
        "B": "Incorrect; Mere casual/fleeting relations do not qualify.",
        "C": "Incorrect; Friendship contracts cannot create marital relationships.",
        "D": "Incorrect; Financial dependency alone is insufficient."
    },
    "Advanced", "PWDVA S. 2(f) & D. Velusamy (2010)", "Understand judicial criteria for live-in relationships under PWDVA."
))

mcqs.append(make_q(
    "mcq-dv-01-009", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-02",
    "In Indra Sarma v. V.K.V. Sarma (2013), did the Supreme Court extend PWDVA protection to a woman who entered a live-in relationship knowing the man was already married with children?",
    [
        "Yes, all women are protected without exception",
        "No, knowing involvement with a married man is not a relationship in the nature of marriage and amounts to an adulterous relationship outside PWDVA protection",
        "Yes, but only for claiming gold jewellery",
        "Only if the first wife gave written consent to the live-in relationship"
    ],
    0 if False else 1,
    "In Indra Sarma (2013) 15 SCC 755, the Court held that entering a relationship knowing that the partner is legally married does not satisfy the criteria of a 'relationship in the nature of marriage'.",
    {
        "A": "Incorrect; The Court set boundaries against enabling bigamy.",
        "B": "Correct; An adulterous liaison with knowledge of subsisting marriage is excluded from Section 2(f).",
        "C": "Incorrect; Jewellery recovery cannot confer statutory marital status.",
        "D": "Incorrect; First wife's consent does not legalise bigamous live-in status."
    },
    "Advanced", "PWDVA S. 2(f) & Indra Sarma (2013)", "Distinguish bona fide live-in relations from bigamous liaisons."
))

mcqs.append(make_q(
    "mcq-dv-01-010", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-02",
    "In Satish Chander Ahuja v. Sneha Ahuja (2020), what major clarification did the Supreme Court provide regarding the definition of 'shared household' under Section 2(s)?",
    [
        "Overruled S.R. Batra v. Taruna Batra (2007) and held that shared household is not restricted to property owned by the husband, but includes a house belonging to joint family/in-laws where the woman has lived in a domestic relationship",
        "Held that a daughter-in-law has an absolute ownership share in her father-in-law's self-acquired property",
        "Held that a shared household right expires exactly one year after marriage",
        "Held that shared households only exist in rural agricultural villages"
    ],
    0,
    "In Satish Chander Ahuja (2020) 10 SCC 786, a 3-judge bench overruled S.R. Batra (2007) and held that a shared household includes premises where the aggrieved person lived with the respondent in a domestic relationship, even if owned by the father-in-law.",
    {
        "A": "Correct; Overruled S.R. Batra; shared household encompasses residence in joint family property.",
        "B": "Incorrect; It confers a right of residence/occupation, not proprietary ownership.",
        "C": "Incorrect; No one-year limitation applies.",
        "D": "Incorrect; Applies universally across urban and rural properties."
    },
    "Advanced", "PWDVA S. 2(s) & Satish Chander Ahuja (2020)", "Master landmark precedent expanding shared household definition."
))

mcqs.append(make_q(
    "mcq-dv-01-011", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-02",
    "Does a divorced woman have the right to file an application under PWDVA 2005 for acts of domestic violence committed during the subsistence of marriage?",
    [
        "No, divorce permanently extinguishes all rights under PWDVA",
        "Yes, as affirmed in Juveria Abdul Majid Patni (2014) and Prabha Tyagi (2022), past domestic violence during a subsisting relationship remains actionable even after divorce",
        "Only if the divorce was granted by mutual consent",
        "Only if she has not claimed any maintenance under Section 125 CrPC"
    ],
    1,
    "In Juveria Abdul Majid Patni (2014) and Prabha Tyagi v. Kamlesh Devi (2022), the Supreme Court clarified that the phrase 'has been in a domestic relationship' protects women even after marriage has ended.",
    {
        "A": "Incorrect; The statutory past tense 'has been' explicitly preserves claims.",
        "B": "Correct; Right to seek relief for past domestic abuse survives dissolution of marriage.",
        "C": "Incorrect; The ground of divorce does not bar relief.",
        "D": "Incorrect; Section 125 claims do not bar PWDVA applications."
    },
    "Advanced", "PWDVA S. 2(a), 2(f) & Prabha Tyagi (2022)", "Know survival of PWDVA claims post-divorce."
))

mcqs.append(make_q(
    "mcq-dv-01-012", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-02",
    "Under Section 2(q) of PWDVA 2005 as interpreted following Hiral Harsora, who can be named as a respondent?",
    [
        "Any person who is, or has been, in a domestic relationship with the aggrieved person and against whom relief is sought",
        "Only male relatives aged 21 years or older",
        "Only the husband personally",
        "Only neighbours living within 100 metres"
    ],
    0,
    "Following Hiral Harsora (2016), any person (male or female) who is or has been in a domestic relationship with the aggrieved person can be a respondent.",
    {
        "A": "Correct; Post-Harsora interpretation covers any person in a domestic relationship.",
        "B": "Incorrect; Gender and 21-year restrictions were struck down.",
        "C": "Incorrect; In-laws and relatives can also be respondents.",
        "D": "Incorrect; Neighbours lack domestic relationship."
    },
    "Standard", "PWDVA S. 2(q) & Hiral Harsora (2016)", "Identify proper respondents in PWDVA proceedings."
))

# Topic top-dv-01-03 (6 MCQs)
mcqs.append(make_q(
    "mcq-dv-01-013", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-03",
    "Under Section 3 of PWDVA 2005, which of the following is NOT recognized as a form of domestic violence?",
    [
        "Physical abuse and sexual abuse",
        "Verbal and emotional abuse",
        "Economic abuse",
        "A husband's decision to change his employment"
    ],
    3,
    "Section 3 defines domestic violence broadly into four categories: physical abuse, sexual abuse, verbal/emotional abuse, and economic abuse. Changing employment is a personal career decision, not domestic violence.",
    {
        "A": "Incorrect; Physical and sexual abuse are core statutory categories.",
        "B": "Incorrect; Verbal and emotional abuse are explicitly defined in Section 3.",
        "C": "Incorrect; Economic abuse is explicitly recognized in Section 3.",
        "D": "Correct; Routine career changes do not constitute domestic abuse."
    },
    "Foundational", "PWDVA S. 3", "Identify four statutory categories of domestic violence."
))

mcqs.append(make_q(
    "mcq-dv-01-014", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-03",
    "Under Section 3(a) of PWDVA 2005, 'verbal and emotional abuse' explicitly includes:",
    [
        "Insults, ridicule, humiliation, name calling, and insults specially regarding not having a child or a male child",
        "Polite disagreement over household grocery selections",
        "Requesting quiet during study hours",
        "Purchasing gifts on festivals"
    ],
    0,
    "Section 3, Explanation I, Clause (iii) specifically defines verbal and emotional abuse to include insults, ridicule, humiliation, name-calling, and insults specially with regard to not having a child or not having a male child.",
    {
        "A": "Correct; Verbatim statutory inclusion under Section 3 Explanation I.",
        "B": "Incorrect; Minor domestic disagreements are not abuse.",
        "C": "Incorrect; Reasonable household requests do not constitute abuse.",
        "D": "Incorrect; Voluntary gift-giving is not abuse."
    },
    "Foundational", "PWDVA S. 3 Expl. I", "Recognize statutory elements of verbal and emotional abuse."
))

mcqs.append(make_q(
    "mcq-dv-01-015", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-03",
    "Under Section 3, Explanation I, Clause (iv) of PWDVA 2005, 'economic abuse' includes:",
    [
        "Deprivation of all or any economic or financial resources to which the aggrieved person is entitled under any law or custom or which she requires out of necessity",
        "Refusal of the husband to invest in speculative stock markets",
        "Joint opening of a mutual fund portfolio",
        "Paying rent on time for the leased premises"
    ],
    0,
    "Economic abuse includes deprivation of financial resources, household necessities, alienation of assets or Stridhan, and prohibiting access to resources.",
    {
        "A": "Correct; Core statutory definition of economic abuse under Section 3.",
        "B": "Incorrect; Refusing speculative investment is financial prudence.",
        "C": "Incorrect; Joint investing is not abusive.",
        "D": "Incorrect; Paying rent fulfills a household duty."
    },
    "Standard", "PWDVA S. 3 Expl. I(iv)", "Understand scope of economic abuse under PWDVA."
))

mcqs.append(make_q(
    "mcq-dv-01-016", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-03",
    "Does disposal or alienation of the wife's Stridhan or jewellery by the husband or in-laws without her consent constitute 'economic abuse' under Section 3?",
    [
        "No, in-laws have equal customary right over household jewellery",
        "Yes, disposing of household assets or any other property in which the aggrieved person has an interest or entitlement is an express statutory form of economic abuse",
        "Only if the jewellery value exceeds five lakh rupees",
        "Only if the marriage has broken down completely"
    ],
    1,
    "Section 3 Explanation I(iv)(b) explicitly provides that disposal of household assets or any other property in which the aggrieved person has an interest or entitlement by virtue of domestic relationship constitutes economic abuse.",
    {
        "A": "Incorrect; In-laws have no legal entitlement to Stridhan.",
        "B": "Correct; Explicitly categorized as economic abuse under Section 3.",
        "C": "Incorrect; Value is immaterial; any unauthorized alienation is abuse.",
        "D": "Incorrect; Applies during subsisting cohabitation as well."
    },
    "Standard", "PWDVA S. 3 Expl. I(iv)(b)", "Identify alienation of Stridhan as economic abuse."
))

mcqs.append(make_q(
    "mcq-dv-01-017", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-03",
    "Can coercive demands for dowry constitute domestic violence under Section 3 of PWDVA 2005?",
    [
        "No, dowry demands can only be prosecuted under the Dowry Prohibition Act",
        "Yes, Section 3(b) explicitly provides that harassing, harming, or endangering the aggrieved person to coerce her or any relative to meet any unlawful demand for dowry is domestic violence",
        "Only if accompanied by visible grievous physical hurt",
        "Only if the marriage took place within the past two years"
    ],
    1,
    "Section 3(b) explicitly includes coercion to meet unlawful demands for dowry as a recognized form of domestic violence, creating immediate civil relief avenues alongside criminal prosecution.",
    {
        "A": "Incorrect; PWDVA provides concurrent civil remedies for dowry harassment.",
        "B": "Correct; Statutory mandate of Section 3(b).",
        "C": "Incorrect; Physical injury is not a mandatory prerequisite.",
        "D": "Incorrect; No two-year limit applies."
    },
    "Standard", "PWDVA S. 3(b)", "Know linkage between dowry demands and PWDVA Section 3."
))

mcqs.append(make_q(
    "mcq-dv-01-018", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-03",
    "In Kamlesh Devi v. Jaipal (2019), what did the Supreme Court hold regarding vague, unsubstantiated allegations without a shared domestic nexus?",
    [
        "Held that any distant relative can be summoned under PWDVA without showing cohabitation or domestic violence",
        "Held that in the absence of any specific act of domestic violence or proof of living together in a shared household, an application under PWDVA is not maintainable",
        "Held that all domestic disputes must be automatically converted into murder trials",
        "Held that domestic violence can be presumed without any evidence"
    ],
    1,
    "In Kamlesh Devi v. Jaipal (2019) 13 SCC 234, the Supreme Court held that where the ingredients of living together in a shared household and commission of domestic violence are missing, an application under Section 12 is an abuse of process.",
    {
        "A": "Incorrect; Vague allegations against distant relatives cannot sustain a PWDVA claim.",
        "B": "Correct; Essential ingredients of shared household and domestic violence must be pleaded.",
        "C": "Incorrect; Absurd proposition.",
        "D": "Incorrect; Domestic violence requires factual foundation."
    },
    "Advanced", "PWDVA S. 3, 12 & Kamlesh Devi (2019)", "Understand essential pleadings required under Section 12."
))

print(f"Total MCQs after Act 4 Topic 3: {len(mcqs)}")

# Output builder progress to part2 file
# Let's write the remaining MCQs for Act 4 (Topics 4-9: 32 MCQs), Act 5 (50 MCQs), Act 6 (50 MCQs)
# To manage size and ensure extreme precision, let's write a generator script that appends all questions and validates syntax!
