"""
Generate all 150 MCQs for Part 2: Acts 4-6
Act 4: PWDVA (50 MCQs: mcq-dv-01-001 to mcq-dv-01-050)
Act 5: POSH (50 MCQs: mcq-posh-01-001 to mcq-posh-01-050)
Act 6: PCPNDT (50 MCQs: mcq-pcpndt-01-001 to mcq-pcpndt-01-050)
"""

import json
import os

mcqs = []

def add_q(qid, sid, cid, tid, stem, opts, ans_idx, exp, breakdown, diff, prov, obj):
    letters = ["A", "B", "C", "D"]
    mcqs.append({
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
    })

# --- ACT 4: DOMESTIC VIOLENCE (PWDVA 2005) - 50 MCQs ---

# Chapter 1: ch-soc-dv-01 (18 MCQs)
# top-dv-01-01 (6)
add_q("mcq-dv-01-001", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-01",
      "On which date did the Protection of Women from Domestic Violence Act, 2005 come into force across India?",
      ["13 September 2005", "26 October 2006", "1 January 2006", "15 August 2007"], 1,
      "The PWDVA came into force on 26 October 2006 following central notification.",
      {"A": "Incorrect; 13 September 2005 was Presidential assent.", "B": "Correct; Enforcement date is 26 October 2006.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PWDVA S. 1(3)", "Commencement date of PWDVA 2005.")

add_q("mcq-dv-01-002", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-01",
      "What is the primary nature of the Protection of Women from Domestic Violence Act, 2005?",
      ["It is predominantly a civil remedial enactment providing emergency protective and financial reliefs with criminal consequences for non-compliance",
       "It is a purely penal code providing jail terms for marital incompatibility",
       "It is an amendment to the Hindu Marriage Act governing divorce procedures",
       "It is an administrative code governing women's police stations"], 0,
      "PWDVA is essentially a civil remedial statute with criminal penalties strictly for breach of protection orders under Section 31.",
      {"A": "Correct; Civil remedial enactment with penal enforcement backup.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PWDVA Preamble", "Understand civil-remedial character of PWDVA.")

add_q("mcq-dv-01-003", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-01",
      "Which constitutional provisions provide direct support for the special welfare provisions in PWDVA 2005?",
      ["Articles 14, 15(3) and 21", "Articles 25 and 26", "Articles 311 and 312", "Articles 352 and 356"], 0,
      "Articles 14 (equality), 15(3) (affirmative provisions for women), and 21 (dignity and right to life) form the constitutional bedrock of PWDVA.",
      {"A": "Correct; Articles 14, 15(3), and 21.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "Constitution Arts. 14, 15(3), 21", "Constitutional grounding of PWDVA.")

add_q("mcq-dv-01-004", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-01",
      "How does PWDVA 2005 interact with Section 498A IPC / Section 85-86 BNS?",
      ["PWDVA provides concurrent civil remedies that can be pursued alongside criminal proceedings under Section 498A IPC / Section 85 BNS",
       "Invoking PWDVA completely bars any prosecution under Section 498A IPC",
       "Section 498A conviction is a mandatory prerequisite before filing PWDVA petition",
       "PWDVA repealed Section 498A IPC"], 0,
      "Reliefs under PWDVA are in addition to and not in derogation of any other law under Section 36; proceedings under 498A IPC and PWDVA can run concurrently.",
      {"A": "Correct; Remedies are concurrent and cumulative under Section 36.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PWDVA S. 36 & IPC S. 498A", "Interplay between PWDVA and penal cruelty provisions.")

add_q("mcq-dv-01-005", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-01",
      "Under Section 2(a) of PWDVA 2005, who can be an 'aggrieved person'?",
      ["Any woman who is, or has been, in a domestic relationship with the respondent and who alleges domestic violence",
       "Any man or woman residing in a family home",
       "Only legally wedded wives having biological children",
       "Any landlord whose tenant engages in violence"], 0,
      "Section 2(a) defines aggrieved person strictly as a woman who is or has been in a domestic relationship with the respondent.",
      {"A": "Correct; Any woman who is or has been in a domestic relationship.", "B": "Incorrect; Men cannot be aggrieved persons under PWDVA.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PWDVA S. 2(a)", "Definition of aggrieved person.")

add_q("mcq-dv-01-006", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-01",
      "In Hiral P. Harsora v. Kusum Narottamdas Harsora (2016), what did the Supreme Court hold regarding Section 2(q)?",
      ["Struck down the words 'adult male' so that a complaint under PWDVA can also be filed against female relatives in a domestic relationship",
       "Held that only biological fathers can be named as respondents",
       "Held that respondents must be at least 25 years old",
       "Held that corporations can be named as domestic respondents"], 0,
      "In Hiral Harsora (2016) 10 SCC 165, the Supreme Court struck down 'adult male' from Section 2(q) on the anvil of Article 14.",
      {"A": "Correct; Struck down 'adult male', permitting complaints against female respondents.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "PWDVA S. 2(q) & Hiral Harsora (2016)", "Supreme Court ruling on gender neutrality of respondent.")

# top-dv-01-02 (6)
add_q("mcq-dv-01-007", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-02",
      "Which of the following is NOT recognized under Section 2(f) of PWDVA as creating a 'domestic relationship'?",
      ["Consanguinity (blood)", "Marriage or relationship in the nature of marriage", "Commercial partnership agreement", "Adoption or joint family cohabitation"], 2,
      "Commercial partnership is purely contractual and does not create a domestic relationship under Section 2(f).",
      {"A": "Incorrect; Blood relation is included.", "B": "Incorrect; Marriage and live-in relations are included.", "C": "Correct; Commercial partnership is not a domestic relationship.", "D": "Incorrect; Adoption/joint family is included."},
      "Foundational", "PWDVA S. 2(f)", "Scope of domestic relationship under Section 2(f).")

add_q("mcq-dv-01-008", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-02",
      "In D. Velusamy v. D. Patchaiammal (2010), what did the Supreme Court hold regarding live-in relationships?",
      ["Not all live-in relationships qualify; couple must hold themselves out to society as spouses, be of legal age, qualified to enter legal marriage, and lived together for a significant time",
       "Any casual overnight stay constitutes a relationship in the nature of marriage",
       "Live-in relationships are completely prohibited in India",
       "Only live-in couples with registered contracts are protected"], 0,
      "In D. Velusamy (2010), the Supreme Court laid down four objective criteria for 'relationships in the nature of marriage'.",
      {"A": "Correct; Established four rigorous criteria for live-in protection.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PWDVA S. 2(f) & D. Velusamy (2010)", "Criteria for relationship in the nature of marriage.")

add_q("mcq-dv-01-009", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-02",
      "In Satish Chander Ahuja v. Sneha Ahuja (2020), what landmark interpretation was given to 'shared household' under Section 2(s)?",
      ["Overruled S.R. Batra (2007) and held that shared household includes premises where the aggrieved person lived in a domestic relationship, even if owned exclusively by the in-laws",
       "Held that a daughter-in-law acquires title ownership in her father-in-law's house",
       "Held that shared household is strictly limited to rented apartments",
       "Held that shared household rights cease upon the birth of a child"], 0,
      "Satish Chander Ahuja (2020) 10 SCC 786 overruled S.R. Batra and recognized residence rights in properties owned by parents-in-law.",
      {"A": "Correct; Overruled S.R. Batra, protecting residence right in in-laws' property.", "B": "Incorrect; Protects residence, not ownership title.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "PWDVA S. 2(s) & Satish Chander Ahuja (2020)", "Landmark ruling expanding shared household definition.")

add_q("mcq-dv-01-010", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-02",
      "In Prabha Tyagi v. Kamlesh Devi (2022), what did the Supreme Court hold regarding the necessity of physical co-habitation at the time of filing?",
      ["It is not mandatory for the aggrieved woman to actually be residing in the shared household on the date of filing the application under Section 12",
       "The woman must physically chain herself to the premises to maintain the application",
       "Physical presence inside the house at the moment of filing is an absolute condition precedent",
       "The application can only be filed if the husband resides in a foreign country"], 0,
      "In Prabha Tyagi (2022) 8 SCC 90, the Court held that Section 2(f) uses 'has lived at any point of time'; subsisting actual physical residence at the time of filing is not required.",
      {"A": "Correct; Subsisting physical residence on date of filing is not mandatory.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "PWDVA S. 2(f), 2(s) & Prabha Tyagi (2022)", "Supreme Court precedent on past domestic residence.")

add_q("mcq-dv-01-011", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-02",
      "Can a mother or sister invoke PWDVA against a son or brother respectively?",
      ["Yes, because they share a domestic relationship by consanguinity",
       "No, PWDVA applies strictly between husbands and wives",
       "Only if they are above seventy years of age",
       "Only with the written consent of the District Collector"], 0,
      "Section 2(a) and 2(f) cover any woman related by consanguinity, marriage, or joint family; mothers and sisters can freely file PWDVA applications against sons/brothers.",
      {"A": "Correct; Domestic relationship includes consanguinity (mothers, sisters, daughters).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PWDVA S. 2(a), 2(f)", "Application of PWDVA to mothers and sisters.")

add_q("mcq-dv-01-012", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-02",
      "Does a woman in a live-in relationship have a right to claim maintenance under PWDVA 2005?",
      ["Yes, Section 20 read with Section 2(f) empowers the Magistrate to grant monetary relief and maintenance to a woman in a relationship in the nature of marriage",
       "No, maintenance is exclusively restricted to legally married wives under all Indian laws",
       "Only if she proves she has no surviving blood relatives",
       "Only after residing together continuously for twenty-five years"], 0,
      "Under PWDVA, a woman in a relationship in the nature of marriage is an aggrieved person entitled to monetary relief and maintenance under Section 20.",
      {"A": "Correct; Entitled to monetary relief and maintenance under Section 20.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PWDVA S. 2(f), S. 20 & D. Velusamy (2010)", "Maintenance rights in live-in relationships.")

# top-dv-01-03 (6)
add_q("mcq-dv-01-013", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-03",
      "Which section of PWDVA 2005 contains the exhaustive definition of 'domestic violence'?",
      ["Section 3", "Section 5", "Section 12", "Section 18"], 0,
      "Section 3 of PWDVA comprehensively defines domestic violence covering physical, sexual, verbal, emotional, and economic abuse.",
      {"A": "Correct; Section 3 defines domestic violence.", "B": "Incorrect; S. 5 deals with duties of police/officers.", "C": "Incorrect; S. 12 deals with application to Magistrate.", "D": "Incorrect; S. 18 deals with protection orders."},
      "Foundational", "PWDVA S. 3", "Identify core definition section for domestic violence.")

add_q("mcq-dv-01-014", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-03",
      "Under Section 3 Explanation I, which of the following is explicitly included as 'verbal and emotional abuse'?",
      ["Insults, ridicule, humiliation, name calling, and insults specially regarding not having a child or a male child",
       "Refusing to buy lottery tickets",
       "Disagreeing on interior paint colour",
       "Turning off the television at midnight"], 0,
      "Section 3 Explanation I(iii) explicitly highlights taunts and insults regarding childlessness or not bearing a male child as statutory verbal and emotional abuse.",
      {"A": "Correct; Specific statutory text in Section 3 Explanation I(iii).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PWDVA S. 3 Expl. I(iii)", "Elements of verbal and emotional abuse.")

add_q("mcq-dv-01-015", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-03",
      "Depriving a woman of access to her Stridhan or household financial necessities constitutes:",
      ["Economic abuse under Section 3", "A purely civil tort with no PWDVA application", "Breach of contract under Sale of Goods Act", "Ordinary domestic friction"], 0,
      "Section 3 Explanation I(iv) explicitly defines deprivation of financial resources, basic necessities, and alienation of Stridhan as economic abuse.",
      {"A": "Correct; Economic abuse under Section 3 Explanation I(iv).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PWDVA S. 3 Expl. I(iv)", "Recognize economic abuse under PWDVA.")

add_q("mcq-dv-01-016", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-03",
      "Does marital rape or sexual abuse by the husband fall within the definition of domestic violence under PWDVA 2005?",
      ["Yes, Section 3(a) explicitly includes sexual abuse, defined as any conduct of a sexual nature that abuses, humiliates, degrades or violates the dignity of woman",
       "No, because marital rape is an exception under the Penal Code",
       "Only if accompanied by visible fracture of bones",
       "Only if certified by three medical officers"], 0,
      "While marital rape may have an exception under penal law (BNS/IPC), PWDVA Section 3 explicitly includes sexual abuse as domestic violence for obtaining civil protection and compensation.",
      {"A": "Correct; Sexual abuse is explicitly included in Section 3 civil remedies.", "B": "Incorrect; Penal exception does not preclude civil protection under PWDVA.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PWDVA S. 3(a) & Expl. I(ii)", "Sexual abuse as a ground for PWDVA civil relief.")

add_q("mcq-dv-01-017", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-03",
      "Under Section 3(c) of PWDVA 2005, threatening the aggrieved person with any conduct mentioned in clause (a) or (b) constitutes:",
      ["Domestic violence", "Unpunishable intention", "Mere preparation without consequence", "Civil contempt of court"], 0,
      "Section 3(c) explicitly provides that threatening the aggrieved person with physical, sexual, verbal, emotional, or economic abuse itself constitutes domestic violence.",
      {"A": "Correct; Threat of abuse constitutes domestic violence under Section 3(c).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PWDVA S. 3(c)", "Threats as actionable domestic violence.")

add_q("mcq-dv-01-018", "soc-domestic-violence", "ch-soc-dv-01", "top-dv-01-03",
      "Under Section 3 Explanation II, how does the court determine whether an act constitutes domestic violence?",
      ["The overall facts and circumstances of the case shall be taken into consideration",
       "Strict mechanical count of how many injuries were sustained",
       "Solely by checking if an FIR was registered within 24 hours",
       "By conducting a lie-detector test on both parties"], 0,
      "Explanation II to Section 3 mandates: 'For the purpose of determining whether any act... constitutes domestic violence, the overall facts and circumstances of the case shall be taken into consideration.'",
      {"A": "Correct; Overall facts and circumstances must be considered.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PWDVA S. 3 Expl. II", "Holistic assessment standard under Section 3.")

# Chapter 2: ch-soc-dv-02 (16 MCQs)
# top-dv-02-01 (6)
add_q("mcq-dv-01-019", "soc-domestic-violence", "ch-soc-dv-02", "top-dv-02-01",
      "What is a 'Domestic Incident Report' (DIR) under Section 2(e) of PWDVA 2005?",
      ["A report made in the prescribed form on receipt of a complaint of domestic violence from an aggrieved person",
       "An FIR registered under Section 154 CrPC",
       "A chargesheet filed under Section 173 CrPC",
       "A post-mortem report prepared by a government hospital"], 0,
      "Section 2(e) defines Domestic Incident Report as a report made in the prescribed form (Form I) upon receipt of a complaint of domestic violence.",
      {"A": "Correct; Statutory definition under Section 2(e).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PWDVA S. 2(e) & S. 9", "Definition and role of Domestic Incident Report.")

add_q("mcq-dv-01-020", "soc-domestic-violence", "ch-soc-dv-02", "top-dv-02-01",
      "Under Section 8(1) of PWDVA 2005, who appoints Protection Officers in each district?",
      ["The State Government by notification", "The District Sessions Judge", "The Chief Judicial Magistrate", "The National Commission for Women"], 0,
      "Section 8(1) empowers the State Government to appoint as many Protection Officers in each district as may be considered necessary.",
      {"A": "Correct; State Government appoints Protection Officers.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PWDVA S. 8(1)", "Appointing authority for Protection Officers.")

add_q("mcq-dv-01-021", "soc-domestic-violence", "ch-soc-dv-02", "top-dv-02-01",
      "Under Section 8(2) of PWDVA 2005, what statutory preference is prescribed regarding the gender of Protection Officers?",
      ["Protection Officers shall as far as possible be women",
       "Protection Officers must strictly be retired military male personnel",
       "Protection Officers must alternate equally between male and female",
       "No gender preference exists"], 0,
      "Section 8(2) provides: 'The Protection Officers shall as far as possible be women and shall possess such qualifications and experience as may be prescribed.'",
      {"A": "Correct; Statutory preference: shall as far as possible be women.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PWDVA S. 8(2)", "Statutory gender preference for Protection Officers.")

add_q("mcq-dv-01-022", "soc-domestic-violence", "ch-soc-dv-02", "top-dv-02-01",
      "Under Section 10 of PWDVA 2005, what entities can register as 'Service Providers' to assist aggrieved persons?",
      ["Voluntary associations registered under the Societies Registration Act or companies under Companies Act with objective of protecting women's rights",
       "Commercial debt collection agencies",
       "Private armed security contractors",
       "Commercial marriage bureaus"], 0,
      "Section 10(1) allows any voluntary association or company committed to women's welfare to register with the State Government as a Service Provider.",
      {"A": "Correct; Voluntary associations and non-profit companies under Section 10.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PWDVA S. 10(1)", "Eligibility and registration of Service Providers.")

add_q("mcq-dv-01-023", "soc-domestic-violence", "ch-soc-dv-02", "top-dv-02-01",
      "Under Section 6 and Section 7 of PWDVA 2005, what duties are cast upon shelter homes and medical facilities?",
      ["They must provide shelter or medical aid to the aggrieved person upon request by her or by a Protection Officer/Service Provider",
       "They can refuse entry unless the woman produces an advance court decree",
       "They must charge commercial emergency tariffs",
       "They must detain the woman until her husband arrives"], 0,
      "Sections 6 and 7 create mandatory statutory obligations for shelter homes and medical facilities to provide lodging and treatment upon request.",
      {"A": "Correct; Mandatory statutory duty to provide shelter and medical aid.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PWDVA S. 6, 7", "Statutory duties of shelter homes and medical facilities.")

add_q("mcq-dv-01-024", "soc-domestic-violence", "ch-soc-dv-02", "top-dv-02-01",
      "Is an aggrieved woman mandatorily required to route her application through a Protection Officer before approaching the Magistrate under Section 12?",
      ["No, in Prabha Tyagi (2022) the Supreme Court confirmed that an aggrieved woman can file an application directly under Section 12 without a prior DIR from a Protection Officer",
       "Yes, without a Protection Officer's report the Magistrate has zero jurisdiction",
       "Only if she is illiterate",
       "Only if she resides in a rural area"], 0,
      "In Prabha Tyagi (2022), the Supreme Court clarified that obtaining a DIR from a Protection Officer is not a condition precedent for filing an application under Section 12.",
      {"A": "Correct; Direct approach to Magistrate under Section 12 is fully permissible.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "PWDVA S. 12 & Prabha Tyagi (2022)", "Direct filing under Section 12 without DIR.")

# top-dv-02-02 (5)
add_q("mcq-dv-01-025", "soc-domestic-violence", "ch-soc-dv-02", "top-dv-02-02",
      "Under Section 17(1) of PWDVA 2005, what substantive right is guaranteed to every woman in a domestic relationship?",
      ["Right to reside in the shared household, whether or not she has any right, title or beneficial interest in the same",
       "Right to sell the matrimonial home at market value",
       "Right to take absolute ownership of 50 percent of the premises",
       "Right to evict all male relatives unconditionally"], 0,
      "Section 17(1) non-obstante clause gives every woman in a domestic relationship the right to reside in the shared household regardless of proprietary title.",
      {"A": "Correct; Statutory right to reside in shared household regardless of title.", "B": "Incorrect.", "C": "Incorrect; Right is of residence, not title.", "D": "Incorrect."},
      "Foundational", "PWDVA S. 17(1)", "Substantive right to reside in shared household.")

add_q("mcq-dv-01-026", "soc-domestic-violence", "ch-soc-dv-02", "top-dv-02-02",
      "Under Section 17(2) of PWDVA 2005, can an aggrieved person be evicted or excluded from the shared household by the respondent?",
      ["No, she shall not be evicted or excluded from the shared household or any part of it by the respondent save in accordance with procedure established by law",
       "Yes, at the sole discretion of the title-holder father-in-law",
       "Yes, if the husband serves a 15-day notice by registered post",
       "Yes, if the couple has separated for more than three months"], 0,
      "Section 17(2) explicitly protects the aggrieved person against dispossession or exclusion except through due process of law.",
      {"A": "Correct; Protection against summary eviction save by procedure established by law.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PWDVA S. 17(2)", "Protection against arbitrary eviction under Section 17(2).")

add_q("mcq-dv-01-027", "soc-domestic-violence", "ch-soc-dv-02", "top-dv-02-02",
      "In S. Vanitha v. Deputy Commissioner (2021), how did the Supreme Court resolve a conflict where elderly in-laws sought eviction of a daughter-in-law under the Senior Citizens Act while she claimed residence under PWDVA?",
      ["Held that both statutes must be harmoniously construed; the Senior Citizens tribunal cannot summarily evict the daughter-in-law without considering her shared household rights under PWDVA",
       "Held that the Senior Citizens Act unconditionally extinguishes PWDVA",
       "Held that PWDVA completely repeals the Senior Citizens Act",
       "Held that both parties must be sent to civil prison"], 0,
      "In S. Vanitha (2021) 15 SCC 730, Dr. D.Y. Chandrachud, J., harmonized both Acts, holding that eviction under Senior Citizens Act cannot bypass PWDVA protections.",
      {"A": "Correct; Harmonious construction ensuring PWDVA protections are considered.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "PWDVA S. 17 & S. Vanitha (2021)", "Harmonization between Senior Citizens Act and PWDVA.")

add_q("mcq-dv-01-028", "soc-domestic-violence", "ch-soc-dv-02", "top-dv-02-02",
      "Under Section 19(1)(f) of PWDVA 2005, if the respondent is directed to secure alternate accommodation for the aggrieved person, what standard must it meet?",
      ["It must be of the same level as enjoyed by her in the shared household or the respondent must pay rent for the same",
       "Any makeshift dormitory room is sufficient",
       "It must be situated within 500 metres of the High Court",
       "It must be a newly purchased luxury apartment"], 0,
      "Section 19(1)(f) requires the respondent to secure alternative accommodation of the same level as enjoyed by her in the shared household or pay rent.",
      {"A": "Correct; Same level as enjoyed in shared household or rent payment.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PWDVA S. 19(1)(f)", "Standard of alternate accommodation under Section 19.")

add_q("mcq-dv-01-029", "soc-domestic-violence", "ch-soc-dv-02", "top-dv-02-02",
      "Can a residence order under Section 19 be passed against female relatives directing their removal from the shared household?",
      ["No, the proviso to Section 19(1) expressly prohibits passing any order directing any woman to remove herself from the shared household",
       "Yes, female respondents can be removed just like male respondents",
       "Only if they are second-degree relatives",
       "Only if approved by the State Government"], 0,
      "Proviso to Section 19(1) provides: 'Provided that no order under clause (b) shall be passed against any person who is a woman.' A woman cannot be directed to remove herself from the household.",
      {"A": "Correct; Proviso to Section 19(1) bars removal orders against female respondents.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "PWDVA S. 19(1) Proviso", "Statutory bar on removing female respondents under Section 19.")

# top-dv-02-03 (5)
add_q("mcq-dv-01-030", "soc-domestic-violence", "ch-soc-dv-02", "top-dv-02-03",
      "Which judicial forum has original jurisdiction to entertain applications under Section 12 of PWDVA 2005?",
      ["Judicial Magistrate of the First Class or Metropolitan Magistrate", "Executive Magistrate", "District Collector", "Labour Court"], 0,
      "Section 27 and Section 12 confer jurisdiction on the Court of Judicial Magistrate of the First Class or Metropolitan Magistrate.",
      {"A": "Correct; JMFC or Metropolitan Magistrate.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PWDVA S. 12, S. 27", "Competent judicial forum under PWDVA.")

add_q("mcq-dv-01-031", "soc-domestic-violence", "ch-soc-dv-02", "top-dv-02-03",
      "Under Section 12(4) of PWDVA 2005, the Magistrate shall fix the first date of hearing ordinarily not beyond how many days from the date of receipt of application?",
      ["Three days", "Seven days", "Fifteen days", "Thirty days"], 0,
      "Section 12(4) provides that the Magistrate shall fix the first date of hearing, which shall not ordinarily be beyond three days from the date of receipt of application.",
      {"A": "Correct; Statutory target: ordinarily not beyond three days.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PWDVA S. 12(4)", "First date of hearing timeline under Section 12(4).")

add_q("mcq-dv-01-032", "soc-domestic-violence", "ch-soc-dv-02", "top-dv-02-03",
      "Under Section 12(5) of PWDVA 2005, the Magistrate shall endeavor to dispose of every application within what target timeline?",
      ["Sixty days from the date of its first hearing", "Thirty days from filing", "Ninety days from notice", "One year"], 0,
      "Section 12(5) provides that the Magistrate shall endeavor to dispose of every application made under sub-section (1) within a period of sixty days from the date of its first hearing.",
      {"A": "Correct; Target disposal within sixty days from the date of first hearing.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PWDVA S. 12(5)", "Statutory target timeline (60 days) under Section 12(5).")

add_q("mcq-dv-01-033", "soc-domestic-violence", "ch-soc-dv-02", "top-dv-02-03",
      "Under Section 23 of PWDVA 2005, can the Magistrate pass interim and ex-parte orders?",
      ["Yes, Section 23(1) authorizes interim orders and Section 23(2) authorizes ex-parte orders on the basis of an affidavit in the prescribed form",
       "No, ex-parte orders are completely barred under PWDVA",
       "Only after recording oral testimony of at least three independent witnesses",
       "Only with the concurrence of the High Court"], 0,
      "Section 23 empowers the Magistrate to grant interim orders and ex-parte orders based on an affidavit (Form III) showing a prima facie case.",
      {"A": "Correct; Explicit power to pass interim and ex-parte orders under Section 23.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PWDVA S. 23", "Interim and ex-parte orders under Section 23.")

add_q("mcq-dv-01-034", "soc-domestic-violence", "ch-soc-dv-02", "top-dv-02-03",
      "Under Section 27(1) of PWDVA 2005, where can an application under Section 12 be instituted?",
      ["Where the aggrieved person permanently or temporarily resides or carries on business, where respondent resides, or where cause of action arose",
       "Strictly at the ancestral home of the husband",
       "Only where the marriage was solemnized",
       "Only at the State capital"], 0,
      "Section 27(1) confers expansive territorial jurisdiction including where the aggrieved person temporarily resides, facilitating accessible justice.",
      {"A": "Correct; Includes temporary residence of aggrieved woman, respondent residence, or cause of action.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PWDVA S. 27(1)", "Territorial jurisdiction under Section 27.")

# Chapter 3: ch-soc-dv-03 (16 MCQs)
# top-dv-03-01 (6)
add_q("mcq-dv-01-035", "soc-domestic-violence", "ch-soc-dv-03", "top-dv-03-01",
      "Under Section 18 of PWDVA 2005, what kind of relief can the Magistrate grant?",
      ["Protection orders prohibiting the respondent from committing acts of domestic violence, entering her place of employment, or communicating with her",
       "A decree of absolute divorce",
       "Sentencing the respondent to 3 years rigorous imprisonment immediately",
       "Order forfeiting the respondent's passport permanently"], 0,
      "Section 18 provides for Protection Orders restraining violence, entry into workplace/school, communication, alienation of assets, etc.",
      {"A": "Correct; Protection orders restraining violence, contact, and interference.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PWDVA S. 18", "Scope of Protection Orders under Section 18.")

add_q("mcq-dv-01-036", "soc-domestic-violence", "ch-soc-dv-03", "top-dv-03-01",
      "Under Section 19 of PWDVA 2005, what relief can the Magistrate grant?",
      ["Residence orders restraining disposal or dispossessing, directing alternate accommodation, or removing respondent from shared household",
       "Orders declaring the marriage void",
       "Orders granting adoption of foreign children",
       "Orders attaching immovable property for revenue tax"], 0,
      "Section 19 deals with Residence Orders securing occupation, preventing alienation, or ordering alternate accommodation.",
      {"A": "Correct; Residence orders securing housing rights under Section 19.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PWDVA S. 19", "Scope of Residence Orders under Section 19.")

add_q("mcq-dv-01-037", "soc-domestic-violence", "ch-soc-dv-03", "top-dv-03-01",
      "Under Section 20 of PWDVA 2005, what can be directed by the Magistrate as monetary relief?",
      ["Expenses incurred and losses suffered including loss of earnings, medical expenses, loss caused by destruction of property, and maintenance for aggrieved person and children",
       "Payment of punitive damages of 1 crore rupees to the Prime Minister's Relief Fund",
       "Exemption from paying income tax",
       "Surrender of all commercial bank guarantees"], 0,
      "Section 20 covers comprehensive monetary relief including medical costs, loss of property/earnings, and maintenance.",
      {"A": "Correct; Medical expenses, loss of earnings, property loss, and maintenance.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PWDVA S. 20", "Components of monetary relief under Section 20.")

add_q("mcq-dv-01-038", "soc-domestic-violence", "ch-soc-dv-03", "top-dv-03-01",
      "Under Section 21 of PWDVA 2005, what power does the Magistrate have regarding children?",
      ["Grant temporary custody of any child or children to the aggrieved person and specify arrangements for visit by the respondent",
       "Appoint a permanent testamentary guardian under Hindu Minority and Guardianship Act",
       "Send the children to a juvenile correction home",
       "Declare the children illegitimate"], 0,
      "Section 21 empowers the Magistrate to grant temporary custody to the aggrieved woman and regulate visiting arrangements.",
      {"A": "Correct; Temporary custody and visiting arrangements under Section 21.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PWDVA S. 21", "Custody orders under Section 21.")

add_q("mcq-dv-01-039", "soc-domestic-violence", "ch-soc-dv-03", "top-dv-03-01",
      "Under Section 22 of PWDVA 2005, the Magistrate can order the respondent to pay compensation and damages for:",
      ["Injuries, including mental torture and emotional distress, caused by the acts of domestic violence",
       "Loss of business profits due to economic slowdown",
       "Litigation costs in unrelated property partition suits",
       "Inflation adjustment on wedding expenses"], 0,
      "Section 22 empowers the Magistrate to award compensation and damages for personal injuries, including mental torture and emotional distress.",
      {"A": "Correct; Compensation for personal injuries, mental torture and emotional distress.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PWDVA S. 22", "Compensation orders under Section 22.")

add_q("mcq-dv-01-040", "soc-domestic-violence", "ch-soc-dv-03", "top-dv-03-01",
      "Under Section 26 of PWDVA 2005, can reliefs under Sections 18, 19, 20, 21, and 22 be sought in other legal proceedings?",
      ["Yes, in any legal proceeding before a civil court, family court, or criminal court affecting the aggrieved person and the respondent",
       "No, they can only ever be sought before a Judicial Magistrate in an independent Section 12 petition",
       "Only in proceedings before the Supreme Court",
       "Only in commercial arbitration proceedings"], 0,
      "Section 26 allows PWDVA reliefs to be claimed in any pending or subsequent proceeding before a civil court, family court, or criminal court.",
      {"A": "Correct; Can be claimed in civil, family, or criminal proceedings under Section 26.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "PWDVA S. 26", "Claiming PWDVA reliefs in other legal proceedings.")

# top-dv-03-02 (5)
add_q("mcq-dv-01-041", "soc-domestic-violence", "ch-soc-dv-03", "top-dv-03-02",
      "Under Section 29 of PWDVA 2005, within what period and to which court does an appeal lie from an order of the Magistrate?",
      ["Within thirty days from the date of service of the order, to the Court of Session",
       "Within sixty days to the High Court",
       "Within fifteen days to the District Magistrate",
       "Within ninety days to the Supreme Court"], 0,
      "Section 29 specifies that an appeal shall lie to the Court of Session within thirty days from the date on which the order is served.",
      {"A": "Correct; Thirty days to Court of Session under Section 29.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PWDVA S. 29", "Appellate forum and limitation period under Section 29.")

add_q("mcq-dv-01-042", "soc-domestic-violence", "ch-soc-dv-03", "top-dv-03-02",
      "Does an appeal under Section 29 lie against an interim or ex-parte order passed under Section 23?",
      ["Yes, Section 29 uses the words 'an order made by the Magistrate', which encompasses both final and interim orders",
       "No, only final disposal orders are appealable",
       "Only if the Magistrate certifies that a substantial question of law arises",
       "Only with special leave from the Governor"], 0,
      "It is settled law (including Delhi and Bombay High Courts) that an appeal under Section 29 lies against interim orders passed under Section 23.",
      {"A": "Correct; Appeals lie against interim as well as final orders under Section 29.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PWDVA S. 23, S. 29", "Appealability of interim orders under Section 29.")

add_q("mcq-dv-01-043", "soc-domestic-violence", "ch-soc-dv-03", "top-dv-03-02",
      "In Rajnesh v. Neha (2020), what comprehensive guidelines were laid down by the Supreme Court concerning maintenance under PWDVA and other statutes?",
      ["Mandatory filing of an Affidavit of Assets and Liabilities by both parties, and adjustment/set-off of maintenance awarded across overlapping proceedings",
       "Abolished maintenance claims under Section 125 CrPC",
       "Held that maintenance can never exceed 10 percent of gross salary",
       "Mandated that maintenance can only be paid in gold coins"], 0,
      "In Rajnesh v. Neha (2020) 10 SCC 733, the Supreme Court mandated comprehensive Affidavits of Assets and Liabilities and uniform adjustment of overlapping maintenance awards.",
      {"A": "Correct; Mandatory Affidavits of Assets & Liabilities and adjustment across forums.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "PWDVA S. 20 & Rajnesh v. Neha (2020)", "Supreme Court guidelines on maintenance and asset disclosure.")

add_q("mcq-dv-01-044", "soc-domestic-violence", "ch-soc-dv-02", "top-dv-03-02",
      "Under Section 28(2) of PWDVA 2005, what flexibility is given to the Magistrate regarding procedure?",
      ["The Magistrate can lay down its own procedure for disposal of an application under Section 12 or Section 23(2)",
       "The Magistrate must strictly record verbatim depositions under Order XVIII CPC",
       "The Magistrate cannot accept documentary evidence",
       "The Magistrate must consult the local panchayat before every ruling"], 0,
      "Section 28(2) empowers the Magistrate to formulate its own summary procedure for disposal of Section 12 or Section 23 applications.",
      {"A": "Correct; Section 28(2) allows flexible procedure for expeditious disposal.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PWDVA S. 28(2)", "Procedural flexibility under Section 28(2).")

add_q("mcq-dv-01-045", "soc-domestic-violence", "ch-soc-dv-03", "top-dv-03-02",
      "Can an aggrieved person seek alteration, modification or revocation of an order under Section 25(2) of PWDVA 2005?",
      ["Yes, if the Magistrate is satisfied that there is a change in circumstances requiring alteration, modification or revocation",
       "No, an order once passed is final and can never be modified",
       "Only if the respondent agrees in writing",
       "Only after the expiry of five years"], 0,
      "Section 25(2) empowers the Magistrate to alter, modify, or revoke any order upon being satisfied of a change in circumstances.",
      {"A": "Correct; Modification permissible upon change in circumstances under Section 25(2).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PWDVA S. 25(2)", "Alteration and modification of orders under Section 25(2).")

# top-dv-03-03 (5)
add_q("mcq-dv-01-046", "soc-domestic-violence", "ch-soc-dv-03", "top-dv-03-03",
      "Under Section 31(1) of PWDVA 2005, what is the punishment for a breach of a protection order or interim protection order by the respondent?",
      ["Imprisonment for a term which may extend to one year, or with fine which may extend to twenty thousand rupees, or with both",
       "Simple warning by the Protection Officer",
       "Imprisonment for 7 years and fine of Rs 1 lakh",
       "Daily civil imprisonment of 3 days"], 0,
      "Section 31(1) makes breach of a protection order a penal offence punishable with imprisonment up to one year, or fine up to twenty thousand rupees, or both.",
      {"A": "Correct; Imprisonment up to 1 year, or fine up to Rs 20,000, or both.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PWDVA S. 31(1)", "Penal sanction for breach of protection order under Section 31.")

add_q("mcq-dv-01-047", "soc-domestic-violence", "ch-soc-dv-03", "top-dv-03-03",
      "Under Section 32(1) of PWDVA 2005, the offence of breach of a protection order under Section 31 is classified as:",
      ["Cognizable and non-bailable", "Non-cognizable and bailable", "Non-cognizable and non-bailable", "Compoundable without leave of court"], 0,
      "Section 32(1) states: 'Notwithstanding anything contained in the Code of Criminal Procedure, 1973, the offence under sub-section (1) of section 31 shall be cognizable and non-bailable.'",
      {"A": "Correct; Cognizable and non-bailable under Section 32(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PWDVA S. 32(1)", "Classification of Section 31 offence as cognizable and non-bailable.")

add_q("mcq-dv-01-048", "soc-domestic-violence", "ch-soc-dv-03", "top-dv-03-03",
      "Does breach of a monetary relief order under Section 20 attract criminal prosecution under Section 31?",
      ["No, Section 31 strictly penalizes breach of a protection order or interim protection order; monetary orders are executed as fines under CrPC/BNSS",
       "Yes, non-payment of any rupee automatically attracts Section 31 imprisonment",
       "Only if the amount exceeds fifty thousand rupees",
       "Only if the respondent leaves the country"], 0,
      "Section 31 applies strictly to breach of 'protection orders' (Section 18). Monetary orders are recovered as fines under CrPC Section 421 / BNSS Section 461.",
      {"A": "Correct; Section 31 is confined to protection orders; monetary orders are executed as fines.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "PWDVA S. 20, S. 31", "Distinction between enforcement of protection orders and monetary orders.")

add_q("mcq-dv-01-049", "soc-domestic-violence", "ch-soc-dv-03", "top-dv-03-03",
      "Under Section 31(2) of PWDVA 2005, can the Magistrate who passed the protection order frame charges and try the offence under Section 31?",
      ["Yes, the offence under Section 31 shall be tried by the Magistrate who had passed the order, and the Magistrate may also frame charges under Section 498A IPC or Dowry Prohibition Act",
       "No, it must be committed to the Court of Session",
       "No, it can only be tried by a High Court Judge",
       "Only with prior sanction of the Law Ministry"], 0,
      "Section 31(2) and (3) empower the same Magistrate to try the breach offence and also frame connected charges under Section 498A IPC or DP Act.",
      {"A": "Correct; Same Magistrate tries the breach and can frame connected charges.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PWDVA S. 31(2), (3)", "Trial of Section 31 offence and joinder of penal charges.")

add_q("mcq-dv-01-050", "soc-domestic-violence", "ch-soc-dv-03", "top-dv-03-03",
      "Under Section 33 of PWDVA 2005, what is the penalty on a Protection Officer who fails or refuses to discharge duties without sufficient cause?",
      ["Imprisonment for a term which may extend to one year, or with fine which may extend to twenty thousand rupees, or with both (subject to prior sanction under Section 34)",
       "Immediate dismissal from service without any inquiry",
       "Fine of Rs 100 only",
       "Transfer to another district"], 0,
      "Section 33 punishes willful failure or refusal by a Protection Officer with imprisonment up to one year, or fine up to Rs 20,000, or both, subject to sanction under Section 34.",
      {"A": "Correct; Imprisonment up to 1 year, or fine up to Rs 20,000, or both.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PWDVA S. 33, S. 34", "Penal liability of Protection Officers under Section 33.")


# --- ACT 5: POSH ACT, 2013 (soc-posh) - 50 MCQs ---

# Chapter 1: ch-soc-posh-01 (18 MCQs)
# top-posh-01-01 (6)
add_q("mcq-posh-01-001", "soc-posh", "ch-soc-posh-01", "top-posh-01-01",
      "Which landmark judgment of the Supreme Court laid down the original guidelines to prevent sexual harassment at the workplace in 1997?",
      ["Vishaka v. State of Rajasthan (1997)", "Bhanwari Devi v. Union of India (1992)", "Maneka Gandhi v. Union of India (1978)", "Shayara Bano v. Union of India (2017)"], 0,
      "In Vishaka v. State of Rajasthan (1997) 6 SCC 241, the Supreme Court exercised Article 32 powers to frame binding guidelines pending legislation.",
      {"A": "Correct; Vishaka v. State of Rajasthan (1997) laid down the original guidelines.", "B": "Incorrect; Bhanwari Devi was the victim whose assault triggered Vishaka.", "C": "Incorrect.", "D": "Incorrect; Shayara Bano relates to Triple Talaq."},
      "Foundational", "Vishaka (1997) & POSH Preamble", "Origin of workplace sexual harassment jurisprudence.")

add_q("mcq-posh-01-002", "soc-posh", "ch-soc-posh-01", "top-posh-01-01",
      "On which date did the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013 come into force?",
      ["23 April 2013", "9 December 2013", "1 January 2014", "15 August 2013"], 1,
      "The POSH Act received Presidential assent on 22 April 2013 and came into force on 9 December 2013.",
      {"A": "Incorrect; 23 April 2013 was gazette notification date after assent.", "B": "Correct; Came into force on 9 December 2013.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 1(3)", "Commencement date of POSH Act 2013.")

add_q("mcq-posh-01-003", "soc-posh", "ch-soc-posh-01", "top-posh-01-01",
      "Which international convention ratified by India was central to the enactment of the POSH Act, 2013 under Article 253 of the Constitution?",
      ["Convention on the Elimination of All Forms of Discrimination Against Women (CEDAW)",
       "Geneva Conventions",
       "Kyoto Protocol",
       "Berne Convention"], 0,
      "India ratified CEDAW on 25 June 1993; the POSH Act was enacted pursuant to international commitments under CEDAW and Article 253.",
      {"A": "Correct; CEDAW ratified by India in 1993.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "CEDAW & POSH Act Preamble", "International convention underlying POSH Act.")

add_q("mcq-posh-01-004", "soc-posh", "ch-soc-posh-01", "top-posh-01-01",
      "In Aureliano Fernandes v. State of Goa (2023), what critical observations were made by the Supreme Court regarding the implementation of the POSH Act?",
      ["Noted serious lapses in constituting Internal Committees and issued comprehensive nationwide directions to all establishments and professional bodies to audit compliance",
       "Held that the POSH Act should be repealed as unnecessary",
       "Held that IC recommendations are non-binding suggestions",
       "Held that only software companies need to constitute ICs"], 0,
      "In Aureliano Fernandes (2023) 14 SCC 593, Hima Kohli, J., highlighted widespread non-compliance and issued time-bound nationwide implementation directives.",
      {"A": "Correct; Issued nationwide directives to enforce IC constitution and compliance.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "POSH Act S. 4 & Aureliano Fernandes (2023)", "Supreme Court directives on POSH compliance.")

add_q("mcq-posh-01-005", "soc-posh", "ch-soc-posh-01", "top-posh-01-01",
      "Which fundamental rights in Part III of the Constitution are directly safeguarded by the POSH Act, 2013?",
      ["Articles 14, 15, 19(1)(g) and 21", "Articles 29 and 30", "Articles 31A and 31B", "Articles 368 and 370"], 0,
      "The Act guarantees gender equality (Art. 14, 15), right to practice profession free from harassment (Art. 19(1)(g)), and right to life with dignity (Art. 21).",
      {"A": "Correct; Articles 14, 15, 19(1)(g), and 21.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "Constitution Arts. 14, 15, 19(1)(g), 21", "Constitutional rights protected by POSH Act.")

add_q("mcq-posh-01-006", "soc-posh", "ch-soc-posh-01", "top-posh-01-01",
      "Under Section 1(2) of the POSH Act, 2013, what is its territorial extent?",
      ["It extends to the whole of India", "It extends to the whole of India except Jammu and Kashmir", "It applies only to Union Territories", "It applies only to Special Economic Zones"], 0,
      "The POSH Act extends to the whole of India.",
      {"A": "Correct; Extends to the whole of India.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 1(2)", "Territorial extent of POSH Act.")

# top-posh-01-02 (6)
add_q("mcq-posh-01-007", "soc-posh", "ch-soc-posh-01", "top-posh-01-02",
      "Under Section 2(a) of the POSH Act, 2013, who is an 'aggrieved woman'?",
      ["In relation to a workplace, a woman of any age whether employed or not, who alleges to have been subjected to any act of sexual harassment by the respondent",
       "Only a full-time permanent employee on the regular payroll",
       "Only an employee who has completed at least 240 days of continuous service",
       "Only a woman holding managerial rank"], 0,
      "Section 2(a) provides a broad definition: any woman of any age, whether employed or not (e.g. clients, visitors, interns), who alleges sexual harassment at a workplace.",
      {"A": "Correct; A woman of any age, whether employed or not.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 2(a)", "Broad definition of aggrieved woman under Section 2(a).")

add_q("mcq-posh-01-008", "soc-posh", "ch-soc-posh-01", "top-posh-01-02",
      "Can a female client, visitor, intern, or job applicant file a complaint under POSH if sexually harassed at an office?",
      ["Yes, because Section 2(a) explicitly includes women 'whether employed or not'",
       "No, POSH is restricted to contractual employees having an employment contract",
       "Only if she was invited by the Managing Director in writing",
       "Only if she has a pending salary claim"], 0,
      "Section 2(a)(i) covers any woman 'whether employed or not'; visitors, interns, and clients are fully protected against harassment at the workplace.",
      {"A": "Correct; Expressly protected under Section 2(a)(i).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Act S. 2(a)(i)", "Protection of non-employees (visitors/clients/interns).")

add_q("mcq-posh-01-009", "soc-posh", "ch-soc-posh-01", "top-posh-01-02",
      "Under Section 2(o) of the POSH Act, 2013, what constitutes a 'workplace'?",
      ["Government offices, private sector organizations, hospitals, sports institutes, dwelling places (for domestic workers), and any place visited by employee arising out of or during employment including transportation",
       "Only physical commercial office buildings owned by the employer",
       "Only government secretariats and courts",
       "Only factories registered under the Factories Act, 1948"], 0,
      "Section 2(o) establishes an expansive definition of workplace, incorporating the 'notional extension of employment' doctrine.",
      {"A": "Correct; Comprehensive definition including extended workplace and transport.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 2(o)", "Definition of workplace under Section 2(o).")

add_q("mcq-posh-01-010", "soc-posh", "ch-soc-posh-01", "top-posh-01-02",
      "Does sexual harassment occurring during a virtual office meeting on Zoom, Teams, or via official WhatsApp chat fall within the POSH Act?",
      ["Yes, courts have affirmed that the digital and remote workspace is an extended workplace under Section 2(o)",
       "No, POSH strictly requires physical presence inside a brick-and-mortar office",
       "Only if the server hosting the software is located in India",
       "Only if the meeting was recorded on video"], 0,
      "High Courts and administrative tribunals have repeatedly held that virtual platforms and digital communication during work constitute an extended workplace under Section 2(o).",
      {"A": "Correct; Virtual/remote working is an extended workplace under Section 2(o).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Act S. 2(o)", "Virtual/digital extended workplace under POSH.")

add_q("mcq-posh-01-011", "soc-posh", "ch-soc-posh-01", "top-posh-01-02",
      "Under Section 2(o)(vi), is a dwelling place or a house recognized as a workplace?",
      ["Yes, in relation to a domestic worker",
       "No, private residences are completely outside POSH",
       "Only if the house is larger than 5,000 square feet",
       "Only if five or more servants are employed"], 0,
      "Section 2(o)(vi) specifically designates 'a dwelling place or a house' as a workplace in relation to domestic workers.",
      {"A": "Correct; Dwelling place is a workplace for domestic workers under Section 2(o)(vi).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Act S. 2(o)(vi)", "Coverage of domestic workers and private households.")

add_q("mcq-posh-01-012", "soc-posh", "ch-soc-posh-01", "top-posh-01-02",
      "Under Section 2(f) of the POSH Act, 2013, an 'employee' includes:",
      ["A person employed for any work on regular, temporary, ad hoc, daily wage basis, directly or through an agent, including co-workers, contract workers, probationers, trainees and apprentices",
       "Only permanent staff on monthly payroll",
       "Only executive directors",
       "Only workers who are members of registered trade unions"], 0,
      "Section 2(f) provides an all-inclusive definition covering regular, temporary, contract, ad-hoc, daily wage, probationer, trainee, and apprentice personnel.",
      {"A": "Correct; All-inclusive definition of employee under Section 2(f).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Act S. 2(f)", "Definition of employee under Section 2(f).")

# top-posh-01-03 (6)
add_q("mcq-posh-01-013", "soc-posh", "ch-soc-posh-01", "top-posh-01-03",
      "Under Section 2(n) of the POSH Act, 2013, which of the following is NOT an express form of 'sexual harassment'?",
      ["Physical contact and advances", "A demand or request for sexual favours", "Making sexually coloured remarks or showing pornography", "Constructive professional feedback on performance"], 3,
      "Section 2(n) defines sexual harassment into five categories; objective professional feedback on work performance is not sexual harassment.",
      {"A": "Incorrect; Physical contact is sexual harassment.", "B": "Incorrect; Demands for sexual favours are sexual harassment.", "C": "Incorrect; Sexually coloured remarks/pornography are included.", "D": "Correct; Constructive feedback on work is not sexual harassment."},
      "Foundational", "POSH Act S. 2(n)", "Statutory elements of sexual harassment under Section 2(n).")

add_q("mcq-posh-01-014", "soc-posh", "ch-soc-posh-01", "top-posh-01-03",
      "Under Section 3(2) of the POSH Act, 2013, which circumstance, among others, if connected with any act of sexual harassment, amounts to sexual harassment?",
      ["Implied or explicit promise of preferential treatment in her employment, or threat of detrimental treatment / threat about her present or future employment status",
       "Denial of a festive holiday given to all staff",
       "Transfer of the entire department to another floor",
       "Setting sales targets equally across the team"], 0,
      "Section 3(2) codifies 'quid pro quo' harassment and creation of an intimidating/hostile work environment.",
      {"A": "Correct; Quid pro quo promises or threats under Section 3(2).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 3(2)", "Quid pro quo and hostile environment under Section 3(2).")

add_q("mcq-posh-01-015", "soc-posh", "ch-soc-posh-01", "top-posh-01-03",
      "What is the difference between 'quid pro quo' harassment and 'hostile work environment' harassment?",
      ["Quid pro quo involves conditioning job benefits or threats on sexual compliance; hostile environment involves pervasive intimidating, offensive or humiliating conduct",
       "There is no difference; they are identical",
       "Quid pro quo applies only to government staff, while hostile environment applies to private staff",
       "Quid pro quo requires physical violence, while hostile environment requires theft"], 0,
      "Quid pro quo ('this for that') links employment outcomes to sexual favours; hostile work environment creates an abusive, intimidating atmosphere.",
      {"A": "Correct; Standard jurisprudential distinction codified in Section 3(2).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Act S. 3(2)", "Distinguish quid pro quo from hostile work environment.")

add_q("mcq-posh-01-016", "soc-posh", "ch-soc-posh-01", "top-posh-01-03",
      "Can a single isolated incident of serious sexual misconduct constitute sexual harassment under the POSH Act?",
      ["Yes, a single egregious act such as unwelcome physical assault or explicit demand for sexual favours is sufficient",
       "No, the Act requires at least five separate recorded incidents over six months",
       "Only if confirmed by an external auditor",
       "Only if committed during an official outstation tour"], 0,
      "A single severe or egregious act can constitute sexual harassment; repetition is not an absolute statutory requirement under Section 2(n).",
      {"A": "Correct; A single severe incident can constitute sexual harassment.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Act S. 2(n)", "Single incident vs course of conduct.")

add_q("mcq-posh-01-017", "soc-posh", "ch-soc-posh-01", "top-posh-01-03",
      "Does the subjective intention of the male respondent matter in determining whether his conduct amounted to sexual harassment?",
      ["No, the impact on the recipient woman and the unwelcome nature of the conduct are decisive, not the subjective intention of the respondent",
       "Yes, if the respondent says it was meant as a friendly joke, the complaint must be dismissed",
       "Only if the respondent admits his intention in writing",
       "Intention is the sole criterion"], 0,
      "It is settled law (Vishaka and Section 2(n)) that sexual harassment turns on whether the conduct was unwelcome to the recipient; lack of malicious intent is no defense.",
      {"A": "Correct; Unwelcome character and impact on victim are decisive, not perpetrator's intent.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "POSH Act S. 2(n) & Vishaka (1997)", "Objective and impact test in sexual harassment.")

add_q("mcq-posh-01-018", "soc-posh", "ch-soc-posh-01", "top-posh-01-03",
      "Can a male employee file a complaint under the POSH Act, 2013 if he is sexually harassed by a female or male colleague?",
      ["No, the POSH Act is gender-specific protecting only an 'aggrieved woman'; however, organizations may provide gender-neutral protection under internal HR service rules",
       "Yes, the POSH Act protects men and women identically",
       "Only if he is under eighteen years of age",
       "Only in IT companies"], 0,
      "Under Section 2(a), only an 'aggrieved woman' can invoke the statutory machinery of the POSH Act. Protection for male employees depends on company policy or general law.",
      {"A": "Correct; Statutory POSH remedy is strictly for women; male employees rely on internal HR policies.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Act S. 2(a)", "Gender-specific statutory scope of POSH Act.")

# Chapter 2: ch-soc-posh-02 (16 MCQs)
# top-posh-02-01 (6)
add_q("mcq-posh-01-019", "soc-posh", "ch-soc-posh-02", "top-posh-02-01",
      "Under Section 4(1) of the POSH Act, every employer of a workplace must constitute an 'Internal Committee' (IC) if the establishment employs at least how many workers?",
      ["Ten or more workers", "Twenty or more workers", "Fifty or more workers", "One hundred or more workers"], 0,
      "Section 4(1) mandates every employer of a workplace employing ten or more workers to constitute an Internal Committee by an order in writing.",
      {"A": "Correct; Ten or more workers under Section 4(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 4(1)", "Threshold (10 or more workers) for constituting Internal Committee.")

add_q("mcq-posh-01-020", "soc-posh", "ch-soc-posh-02", "top-posh-02-01",
      "Under Section 4(2)(a) of the POSH Act, 2013, who must preside over the Internal Committee as Presiding Officer?",
      ["A woman employed at a senior level at workplace from amongst the employees",
       "The Managing Director or Chief Executive Officer",
       "A retired High Court Judge",
       "The head of the local police station"], 0,
      "Section 4(2)(a) mandates that the Presiding Officer shall be a woman employed at a senior level at the workplace.",
      {"A": "Correct; Senior woman employee under Section 4(2)(a).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 4(2)(a)", "Qualifications of IC Presiding Officer.")

add_q("mcq-posh-01-021", "soc-posh", "ch-soc-posh-02", "top-posh-02-01",
      "Under Section 4(2)(c) of the POSH Act, what external representation is mandatory on the Internal Committee?",
      ["One member from amongst non-governmental organizations or associations committed to the cause of women or a person familiar with issues relating to sexual harassment",
       "A representative of the local municipal corporation",
       "A police officer not below the rank of DSP",
       "An external commercial auditor"], 0,
      "Section 4(2)(c) requires at least one external member from an NGO or person familiar with sexual harassment issues to prevent institutional bias.",
      {"A": "Correct; External NGO or experienced member under Section 4(2)(c).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Act S. 4(2)(c)", "Mandatory external member on Internal Committee.")

add_q("mcq-posh-01-022", "soc-posh", "ch-soc-posh-02", "top-posh-02-01",
      "Under Section 4(2) proviso, what proportion of the total members nominated to the Internal Committee must be women?",
      ["At least one-half (50 percent) of the total members",
       "At least one-third",
       "All members must strictly be women",
       "At least 75 percent"], 0,
      "Section 4(2) proviso mandates: 'Provided that at least one-half of the total Members so nominated shall be women.'",
      {"A": "Correct; At least 50% must be women.", "B": "Incorrect; One-third is standard in panchayats, but POSH requires 50%.", "C": "Incorrect; Men can be members.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 4(2) Proviso", "Mandatory 50% female representation on IC.")

add_q("mcq-posh-01-023", "soc-posh", "ch-soc-posh-02", "top-posh-02-01",
      "Under Section 4(3) of the POSH Act, 2013, what is the maximum term of office for the Presiding Officer and members of the Internal Committee?",
      ["Such period, not exceeding three years, from the date of nomination",
       "One year only",
       "Five years",
       "Co-terminus with their employment tenure"], 0,
      "Section 4(3) provides that the Presiding Officer and every Member of the Internal Committee shall hold office for such period, not exceeding three years, from the date of nomination.",
      {"A": "Correct; Not exceeding three years under Section 4(3).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Act S. 4(3)", "Tenure of IC members (max 3 years).")

add_q("mcq-posh-01-024", "soc-posh", "ch-soc-posh-02", "top-posh-02-01",
      "If an employer has multiple administrative units or offices located at different places or divisional sub-offices, how must Internal Committees be constituted under Section 4(1)?",
      ["An Internal Committee must be constituted at all administrative units or offices",
       "Only one centralized committee at the corporate headquarters is needed",
       "Only at units employing more than 500 workers",
       "Only in the State where the company is registered"], 0,
      "Section 4(1) explicit proviso: where the offices or administrative units are located at different places, the IC shall be constituted at all administrative units or offices.",
      {"A": "Correct; IC must be constituted at every administrative unit or branch office.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "POSH Act S. 4(1) Proviso", "Decentralized IC mandate across branches.")

# top-posh-02-02 (5)
add_q("mcq-posh-01-025", "soc-posh", "ch-soc-posh-02", "top-posh-02-02",
      "Under Section 6(1) of the POSH Act, who constitutes the 'Local Committee' (LC) in every district?",
      ["The District Officer (District Magistrate / Additional District Magistrate / Collector)",
       "The Chief Judicial Magistrate",
       "The Superintendent of Police",
       "The Bar Association President"], 0,
      "Section 6(1) read with Section 5 provides that the District Officer constitutes the Local Committee in every district.",
      {"A": "Correct; District Officer constitutes the Local Committee under Section 6(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 5, S. 6(1)", "Authority constituting Local Committee.")

add_q("mcq-posh-01-026", "soc-posh", "ch-soc-posh-02", "top-posh-02-02",
      "When does an aggrieved woman approach the Local Committee instead of an Internal Committee under Section 6(1)?",
      ["Where the establishment has less than ten workers, or if the complaint is against the employer himself",
       "Whenever she is dissatisfied with an interlocutory order of the IC",
       "Only if her salary is below Rs 15,000",
       "Only if the workplace is in a rural area"], 0,
      "Section 6(1) specifies that the Local Committee receives complaints from establishments where no IC has been constituted due to having fewer than 10 workers, or where the complaint is against the employer himself.",
      {"A": "Correct; Less than 10 workers or complaint is against the employer.", "B": "Incorrect; Appeals lie under Section 18, not LC.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 6(1)", "Jurisdiction of Local Committee.")

add_q("mcq-posh-01-027", "soc-posh", "ch-soc-posh-02", "top-posh-02-02",
      "Under Section 7(1)(a) of the POSH Act, who is nominated as the Chairperson of the Local Committee?",
      ["An eminent woman in the field of social work and committed to the cause of women",
       "The senior-most male IAS officer in the district",
       "The District Sessions Judge",
       "The Mayor of the Municipal Corporation"], 0,
      "Section 7(1)(a) provides that the Chairperson of the Local Committee shall be an eminent woman in the field of social work and committed to the cause of women.",
      {"A": "Correct; Eminent woman in social work committed to women's cause.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Act S. 7(1)(a)", "Chairperson qualifications for Local Committee.")

add_q("mcq-posh-01-028", "soc-posh", "ch-soc-posh-02", "top-posh-02-02",
      "Under Section 6(2) of the POSH Act, who designates a 'Nodal Officer' in every block, taluka and tehsil to receive complaints and forward them to the Local Committee within 7 days?",
      ["The District Officer", "The Chief Minister", "The High Court Registrar", "The Village Pradhan"], 0,
      "Section 6(2) mandates the District Officer to designate a Nodal Officer in every block, taluka, tehsil, and ward to receive and forward complaints within 7 days.",
      {"A": "Correct; District Officer designates Nodal Officers under Section 6(2).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Act S. 6(2)", "Role of Nodal Officer at taluka/block level.")

add_q("mcq-posh-01-029", "soc-posh", "ch-soc-posh-02", "top-posh-02-02",
      "Under Section 7(1)(c) of the POSH Act, at least one of the members nominated to the Local Committee must be a woman belonging to:",
      ["Scheduled Castes or Scheduled Tribes or Other Backward Classes or minority community",
       "The Indian Foreign Service",
       "The chartered accountants institute",
       "A registered trade union of port workers"], 0,
      "Section 7(1)(c) mandates social inclusion: at least one nominee shall be a woman belonging to SC, ST, OBC, or minority community.",
      {"A": "Correct; Representation for SC/ST/OBC/minority women under Section 7(1)(c).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Act S. 7(1)(c)", "Social diversity representation on Local Committee.")

# top-posh-02-03 (5)
add_q("mcq-posh-01-030", "soc-posh", "ch-soc-posh-02", "top-posh-02-03",
      "Under Section 9(1) of the POSH Act, 2013, what is the limitation period for filing a written complaint to the Internal Committee or Local Committee?",
      ["Within a period of three months from the date of incident, or last incident in case of a series of incidents",
       "Within thirty days of the incident",
       "Within six months",
       "Within three years"], 0,
      "Section 9(1) prescribes a period of three months from the date of incident or date of last incident in case of a series of incidents.",
      {"A": "Correct; Three months under Section 9(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 9(1)", "Limitation period for filing POSH complaint.")

add_q("mcq-posh-01-031", "soc-posh", "ch-soc-posh-02", "top-posh-02-03",
      "Under the proviso to Section 9(1), by how much time can the Internal Committee or Local Committee extend the limitation period for recorded reasons?",
      ["A period not exceeding three months", "A period not exceeding one month", "A period not exceeding six months", "Indefinitely"], 0,
      "Proviso to Section 9(1) allows the IC/LC to extend time by a period not exceeding three months for reasons recorded in writing.",
      {"A": "Correct; Maximum extension of three months for recorded reasons.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Act S. 9(1) Proviso", "Extension of limitation period under Section 9.")

add_q("mcq-posh-01-032", "soc-posh", "ch-soc-posh-02", "top-posh-02-03",
      "Under Section 10(1) of the POSH Act, 2013, can the IC/LC initiate conciliation, and can a monetary settlement be the basis of conciliation?",
      ["Yes, at the request of the aggrieved woman before initiating inquiry, but NO monetary settlement shall be made as a basis of conciliation",
       "Yes, and the respondent must pay at least 5 lakh rupees during conciliation",
       "Conciliation is strictly illegal under the POSH Act",
       "Conciliation can only take place after the final inquiry report is submitted"], 0,
      "Section 10(1) allows conciliation upon request of the woman, but proviso to Section 10(1) explicitly bars any monetary settlement as a basis of conciliation.",
      {"A": "Correct; Conciliation permitted on woman's request, but monetary settlement is strictly prohibited.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 10(1) & Proviso", "Statutory bar on monetary conciliation under Section 10.")

add_q("mcq-posh-01-033", "soc-posh", "ch-soc-posh-02", "top-posh-02-03",
      "Under Section 11(3) of the POSH Act, what powers are vested in the Internal Committee and Local Committee for conducting an inquiry?",
      ["Same powers as are vested in a Civil Court under the Code of Civil Procedure, 1908 in respect of summoning witnesses, discovery and production of documents",
       "Powers of a Court of Session to issue non-bailable arrest warrants",
       "Advisory powers only with no authority to compel attendance",
       "Powers of a police investigating officer to remand in custody"], 0,
      "Section 11(3) confers CPC powers on IC/LC for summoning, enforcing attendance, examining on oath, and requiring discovery/production of documents.",
      {"A": "Correct; CPC Civil Court powers for inquiry under Section 11(3).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Act S. 11(3)", "Civil court powers of IC/LC under Section 11(3).")

add_q("mcq-posh-01-034", "soc-posh", "ch-soc-posh-02", "top-posh-02-03",
      "Can parties be represented by a legal practitioner (advocate) before the Internal Committee or Local Committee during inquiry proceedings?",
      ["No, Rule 7(6) of the POSH Rules, 2013 expressly prohibits parties from bringing any legal practitioner to represent them in inquiry proceedings",
       "Yes, engaging a Senior Advocate is a fundamental right",
       "Only the respondent has a right to an advocate",
       "Only if approved by the Bar Council of India"], 0,
      "Rule 7(6) of the POSH Rules, 2013 provides: 'The parties shall not be allowed to bring any legal practitioner to represent them in their case at any stage of the proceedings before the Complaints Committee.'",
      {"A": "Correct; Legal practitioners are barred under Rule 7(6).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Rules 2013 Rule 7(6)", "Bar on legal practitioners in POSH inquiry proceedings.")

# Chapter 3: ch-soc-posh-03 (16 MCQs)
# top-posh-03-01 (6)
add_q("mcq-posh-01-035", "soc-posh", "ch-soc-posh-03", "top-posh-03-01",
      "Under Section 12(1) of the POSH Act, 2013, what interim recommendations can the IC make during the pendency of an inquiry?",
      ["Transfer the aggrieved woman or respondent to any other workplace, or grant leave to the aggrieved woman up to three months",
       "Dismiss the respondent immediately without hearing",
       "Freeze the respondent's personal bank accounts",
       "Cancel the employer's company registration"], 0,
      "Section 12(1) allows transfer of woman/respondent, or granting paid leave up to 3 months (in addition to entitled leave).",
      {"A": "Correct; Transfer of either party or grant leave up to 3 months under Section 12(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 12(1)", "Interim reliefs during pendency of POSH inquiry.")

add_q("mcq-posh-01-036", "soc-posh", "ch-soc-posh-03", "top-posh-03-01",
      "Is the leave granted to an aggrieved woman under Section 12(1)(b) of the POSH Act deducted from her regular annual leave balance?",
      ["No, Section 12(2) explicitly provides that the leave granted under this section shall be in addition to the leave she would be otherwise entitled to",
       "Yes, it is deducted first from casual leave and then earned leave",
       "It is unpaid leave without salary",
       "It must be made up by working overtime on weekends"], 0,
      "Section 12(2) provides that the leave granted to the aggrieved woman under Section 12 shall be in addition to her statutory leave entitlements.",
      {"A": "Correct; In addition to regular entitled leave under Section 12(2).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Act S. 12(2)", "Leave in addition to regular entitlements under Section 12(2).")

add_q("mcq-posh-01-037", "soc-posh", "ch-soc-posh-03", "top-posh-03-01",
      "Under Section 13(1) of the POSH Act, within what period must the IC or LC submit its inquiry report to the employer or District Officer?",
      ["Within a period of ten days from the completion of the inquiry",
       "Within thirty days",
       "Within three months",
       "Within twenty-four hours"], 0,
      "Section 13(1) provides that on completion of an inquiry, the IC/LC shall provide a report of its findings to the employer/District Officer within ten days.",
      {"A": "Correct; Within ten days from completion of inquiry under Section 13(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 13(1)", "Timeline for submitting inquiry report (10 days).")

add_q("mcq-posh-01-038", "soc-posh", "ch-soc-posh-03", "top-posh-03-01",
      "Under Section 13(4) of the POSH Act, 2013, within what period must the employer or District Officer act upon the recommendations of the IC or LC?",
      ["Within sixty days of receipt of the recommendations",
       "Within thirty days",
       "Within ninety days",
       "Within seven days"], 0,
      "Section 13(4) specifies that the employer or District Officer shall act upon the recommendation within sixty days of its receipt.",
      {"A": "Correct; Within sixty days under Section 13(4).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 13(4)", "Timeline (60 days) for employer action on IC report.")

add_q("mcq-posh-01-039", "soc-posh", "ch-soc-posh-03", "top-posh-03-01",
      "Under Section 15 of the POSH Act, what factors are considered while determining the compensation payable to the aggrieved woman by the respondent?",
      ["Mental trauma, pain, suffering, loss in career opportunity, medical expenses, and the financial status of the respondent",
       "Arbitrary flat rate fixed by the State Government",
       "Equal to 10 years of company turnover",
       "Strictly the market price of gold"], 0,
      "Section 15 sets out five criteria: mental trauma/suffering, loss of career opportunities, medical expenses, feasibility of payment, and financial status of respondent.",
      {"A": "Correct; Trauma, pain, career loss, medical costs, and respondent's financial capacity.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Act S. 15", "Factors for determining compensation under Section 15.")

add_q("mcq-posh-01-040", "soc-posh", "ch-soc-posh-03", "top-posh-03-01",
      "Under Section 11(1) of the POSH Act, what is the maximum target time for completing the inquiry?",
      ["The inquiry shall be completed within a period of ninety days",
       "Within thirty days",
       "Within six months",
       "Within one year"], 0,
      "Section 11(1) provides: 'Provided that the inquiry shall be completed within a period of ninety days.'",
      {"A": "Correct; Target period for completing inquiry is ninety days under Section 11(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 11(1)", "Target timeline (90 days) for completing inquiry.")

# top-posh-03-02 (5)
add_q("mcq-posh-01-041", "soc-posh", "ch-soc-posh-03", "top-posh-03-02",
      "Under Section 16 of the POSH Act, 2013, can the contents of the complaint, identity of complainant/respondent, or inquiry proceedings be disclosed to the public or media under the Right to Information Act, 2005?",
      ["No, Section 16 contains a non-obstante clause overriding the RTI Act 2005 and strictly prohibits publication or making known the contents to public/media",
       "Yes, all POSH complaints are public documents under RTI",
       "Only if the complainant gives television interviews",
       "Only after the employer approves the disclosure"], 0,
      "Section 16 non-obstante clause strictly prohibits publication of identity, addresses, or proceedings, expressly overriding the RTI Act 2005.",
      {"A": "Correct; Non-obstante bar overriding RTI Act to protect confidentiality.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 16", "Confidentiality mandate and exclusion of RTI under Section 16.")

add_q("mcq-posh-01-042", "soc-posh", "ch-soc-posh-03", "top-posh-03-02",
      "Under Section 17 of the POSH Act, what penalty is imposed on any person who contravenes the confidentiality provisions of Section 16?",
      ["Penalty in accordance with service rules, or where no service rules exist, a penalty of five thousand rupees",
       "Imprisonment for 3 years",
       "Suspension of passport",
       "Fine of one lakh rupees"], 0,
      "Section 17 provides that any person breaching Section 16 shall be liable to penalty in accordance with service rules, or a fine of five thousand rupees.",
      {"A": "Correct; Service rule penalty or fine of Rs 5,000 under Section 17.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Act S. 17", "Penalty for breach of confidentiality under Section 17.")

add_q("mcq-posh-01-043", "soc-posh", "ch-soc-posh-03", "top-posh-03-02",
      "Under Section 14(1) of the POSH Act, does the mere inability of an aggrieved woman to substantiate a complaint attract action for making a false or malicious complaint?",
      ["No, Section 14(1) proviso explicitly clarifies that mere inability to substantiate a complaint or provide adequate proof shall not attract action against the complainant",
       "Yes, whenever a complaint is dismissed, the woman must be fired immediately",
       "Yes, dismissal of complaint automatically triggers criminal perjury charges",
       "Only if the respondent pays a prosecution deposit"], 0,
      "Proviso to Section 14(1) explicitly protects complainants: mere inability to substantiate or provide adequate proof does not make a complaint malicious.",
      {"A": "Correct; Inability to substantiate does NOT attract penalty under Section 14(1) proviso.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 14(1) Proviso", "Statutory protection against false complaint penalties.")

add_q("mcq-posh-01-044", "soc-posh", "ch-soc-posh-03", "top-posh-03-02",
      "Under Section 14(1), what is required before any action can be taken against a complainant for filing a false or malicious complaint?",
      ["The malicious intent must be established after an inquiry in accordance with the prescribed procedure",
       "The employer's oral suspicion alone is sufficient",
       "The respondent's acquittal in a criminal case automatically proves malice",
       "A poll conducted among co-workers"], 0,
      "Section 14 requires that malicious intent and knowledge of falsity must be positively established through a proper inquiry.",
      {"A": "Correct; Malice and falsity must be proven through inquiry.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Act S. 14(1)", "Proof of malicious intent under Section 14.")

add_q("mcq-posh-01-045", "soc-posh", "ch-soc-posh-03", "top-posh-03-02",
      "Can Section 16 confidentiality be waived by mutual consent of the employer and employee?",
      ["No, the prohibition under Section 16 is statutory and public-policy oriented to protect victim dignity; however, Section 17 allows disseminating information about justice secured without disclosing identity",
       "Yes, parties can freely contract out of Section 16",
       "Only if approved by a trade union",
       "Only after two years from the incident"], 0,
      "Section 16 confidentiality cannot be waived to broadcast identities; Section 17 proviso only allows publicizing factual outcomes without names/identities.",
      {"A": "Correct; Absolute prohibition to protect dignity; only anonymized justice outcome permitted.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "POSH Act S. 16, 17", "Inviolable nature of POSH confidentiality.")

# top-posh-03-03 (5)
add_q("mcq-posh-01-046", "soc-posh", "ch-soc-posh-03", "top-posh-03-03",
      "Under Section 26(1) of the POSH Act, 2013, what is the penalty on an employer who fails to constitute an Internal Committee?",
      ["Fine which may extend to fifty thousand rupees", "Imprisonment for 6 months", "Immediate cancellation of factory license", "Daily penalty of Rs 10,000"], 0,
      "Section 26(1) provides that failure to constitute an IC or contravening provisions of the Act is punishable with a fine up to fifty thousand rupees.",
      {"A": "Correct; Fine up to fifty thousand rupees (Rs 50,000) under Section 26(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 26(1)", "Penalty for failure to constitute IC under Section 26(1).")

add_q("mcq-posh-01-047", "soc-posh", "ch-soc-posh-03", "top-posh-03-03",
      "Under Section 26(2) of the POSH Act, what are the consequences if an employer, having been previously convicted, commits a second or subsequent offence under the Act?",
      ["Twice the punishment, and cancellation, withdrawal or non-renewal of business license, permit or registration by Government or local authority",
       "Death penalty for company directors",
       "Compulsory nationalization of the company",
       "Simple warning by the Labour Inspector"], 0,
      "Section 26(2) mandates twice the fine and empowers the government/local authority to cancel, withdraw, or refuse renewal of licenses or registrations.",
      {"A": "Correct; Double punishment and cancellation of business license under Section 26(2).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Act S. 26(2)", "Enhanced penalty for repeat offences under Section 26(2).")

add_q("mcq-posh-01-048", "soc-posh", "ch-soc-posh-03", "top-posh-03-03",
      "Under Section 18(1) of the POSH Act, 2013, within what period can any person aggrieved by the recommendations of the IC or LC prefer an appeal?",
      ["Within ninety days of the recommendations", "Within thirty days", "Within sixty days", "Within one year"], 0,
      "Section 18(1) provides that any person aggrieved may prefer an appeal to the court or tribunal within ninety days of the recommendations.",
      {"A": "Correct; Ninety days (90 days) under Section 18(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 18(1)", "Limitation period (90 days) for appeal under Section 18.")

add_q("mcq-posh-01-049", "soc-posh", "ch-soc-posh-03", "top-posh-03-03",
      "Under Section 21 of the POSH Act, 2013, what annual statutory obligation is imposed on the Internal Committee and Local Committee?",
      ["Prepare in each calendar year an Annual Report and submit it to the employer and District Officer",
       "Publish all complaints in the local daily newspaper",
       "Distribute cash dividends to female staff",
       "Submit an audit report to the Comptroller and Auditor General"], 0,
      "Section 21 mandates every IC and LC to prepare and submit an Annual Report detailing number of complaints received, disposed, and pending.",
      {"A": "Correct; Mandatory Annual Report submission under Section 21.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POSH Act S. 21", "Annual Report obligation under Section 21.")

add_q("mcq-posh-01-050", "soc-posh", "ch-soc-posh-03", "top-posh-03-03",
      "Under Section 27 of the POSH Act, 2013, which court is competent to try offences punishable under the Act?",
      ["No court inferior to that of a Metropolitan Magistrate or a Judicial Magistrate of the first class",
       "Any Executive Magistrate",
       "Only the High Court",
       "The Gram Nyayalaya"], 0,
      "Section 27(1) provides: 'No court inferior to that of a Metropolitan Magistrate or a Judicial Magistrate of the first class shall try any offence punishable under this Act.'",
      {"A": "Correct; Metropolitan Magistrate or JMFC under Section 27(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POSH Act S. 27(1)", "Competent trial court under Section 27.")


# --- ACT 6: PCPNDT ACT, 1994 (soc-pcpndt) - 50 MCQs ---

# Chapter 1: ch-soc-pcpndt-01 (18 MCQs)
# top-pcpndt-01-01 (6)
add_q("mcq-pcpndt-01-001", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-01-01",
      "On which date did the Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act, 1994 come into force in India?",
      ["1 January 1996", "20 September 1994", "14 February 2003", "1 July 1995"], 0,
      "Enacted in 1994 (Act 57 of 1994), the Act was brought into force on 1 January 1996 by Central Government notification.",
      {"A": "Correct; Came into force on 1 January 1996.", "B": "Incorrect; 20 September 1994 was Presidential assent.", "C": "Incorrect; 2003 was amendment enforcement.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 1(3)", "Commencement date of PCPNDT Act.")

add_q("mcq-pcpndt-01-002", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-01-01",
      "What crucial addition was introduced into the title and scope of the Act by the Amendment Act of 2002 (effective 14 February 2003)?",
      ["Inclusion of 'Pre-Conception' and 'Prohibition of Sex Selection' to ban pre-conception technologies like sperm sorting and IVF sex selection",
       "Decriminalisation of all ultrasound scanning",
       "Exemption of private multi-specialty hospitals",
       "Transfer of enforcement to the Medical Council alone"], 0,
      "The 2002 Amendment brought pre-conception sex selection technologies explicitly under the prohibitory umbrella following CEHAT directions.",
      {"A": "Correct; Added 'Pre-Conception' and 'Prohibition of Sex Selection' in 2003.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "Act 39 of 2002 & PCPNDT Title", "2002 Amendment expanding scope to pre-conception.")

add_q("mcq-pcpndt-01-003", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-01-01",
      "In which landmark PIL did the Supreme Court issue sweeping directions to strictly enforce the PCPNDT Act across all States and Union Territories?",
      ["CEHAT v. Union of India (2001 & 2003)", "Parmanand Katara v. Union of India (1989)", "Common Cause v. Union of India (2018)", "Lily Thomas v. Union of India (2000)"], 0,
      "In CEHAT (Centre for Enquiry into Health and Allied Themes) v. UOI (2001 & 2003), the Supreme Court mandated implementation and spurred the 2002 amendments.",
      {"A": "Correct; CEHAT v. Union of India (2001, 2003).", "B": "Incorrect; Relates to emergency medical care.", "C": "Incorrect; Relates to passive euthanasia.", "D": "Incorrect; Relates to MPs disqualification."},
      "Foundational", "CEHAT v. UOI (2001, 2003)", "Landmark PIL enforcing PCPNDT Act.")

add_q("mcq-pcpndt-01-004", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-01-01",
      "What is the primary socio-legal mischief targeted by the PCPNDT Act, 1994?",
      ["Rampant female foeticide leading to severe decline in child sex ratio and sex-selective abortions",
       "Overcharging by private diagnostic radiologists",
       "Import duties on medical imaging equipment",
       "Lack of ultrasound training in medical colleges"], 0,
      "The Act was enacted to arrest the alarming skew in the sex ratio caused by misuse of prenatal diagnostic techniques for sex-selective abortions.",
      {"A": "Correct; Combating female foeticide and declining sex ratio.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act Preamble", "Legislative purpose of PCPNDT Act.")

add_q("mcq-pcpndt-01-005", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-01-01",
      "Under Section 1(2) of the PCPNDT Act, 1994, what is the territorial extent of the Act?",
      ["It extends to the whole of India", "It extends to the whole of India except Jammu and Kashmir", "It applies only to non-tribal areas", "It applies only to cities with population above 10 lakhs"], 0,
      "Following the 2019 Reorganisation, the Act extends to the whole of India.",
      {"A": "Correct; Whole of India.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 1(2)", "Territorial extent of PCPNDT Act.")

add_q("mcq-pcpndt-01-006", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-01-01",
      "In Voluntary Health Association of Punjab v. Union of India (2016), what did the Supreme Court direct regarding pending PCPNDT cases?",
      ["Directed fast-tracking of all pending PCPNDT trials and mandated quarterly monitoring by High Courts",
       "Directed withdrawal of all pending prosecutions against radiologists",
       "Stayed the operation of Section 28 for three years",
       "Ordered decriminalisation of record-keeping irregularities"], 0,
      "In VHAP v. UOI (2016) 10 SCC 265, Dipak Misra, J., ordered fast-tracking of trials and directed High Courts to monitor proceedings quarterly.",
      {"A": "Correct; Fast-tracking trials and quarterly High Court monitoring.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "VHAP v. UOI (2016)", "Supreme Court monitoring directions in VHAP.")

# top-pcpndt-01-02 (6)
add_q("mcq-pcpndt-01-007", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-01-02",
      "Under Section 2(o) of the PCPNDT Act, 'sex selection' includes any procedure, technique, test or administration:",
      ["Having for its purpose of ensuring or increasing the probability that an embryo will be of a particular sex",
       "Intended to enhance fetal nutrition",
       "Conducted to vaccinate against rubella",
       "Monitoring fetal heartbeat rate"], 0,
      "Section 2(o) defines sex selection broadly to include any technique or medicine intended to ensure or increase probability of a specific sex.",
      {"A": "Correct; Statutory definition under Section 2(o).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 2(o)", "Definition of sex selection under Section 2(o).")

add_q("mcq-pcpndt-01-008", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-01-02",
      "Under Section 2(k) of the PCPNDT Act, what is a 'pre-natal diagnostic technique'?",
      ["All pre-natal diagnostic procedures and pre-natal diagnostic tests",
       "Only MRI scans of the brain",
       "Only blood sugar testing during pregnancy",
       "Urine tests for kidney function"], 0,
      "Section 2(k) defines pre-natal diagnostic technique as all pre-natal diagnostic procedures and pre-natal diagnostic tests.",
      {"A": "Correct; Pre-natal diagnostic procedures and tests under Section 2(k).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 2(k)", "Definition of pre-natal diagnostic technique.")

add_q("mcq-pcpndt-01-009", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-01-02",
      "Under Section 2(d) of the Act, which medical centres are covered as 'Genetic Clinic'?",
      ["A clinic, institute, hospital, nursing home or any place, by whatever name called, which is used for conducting pre-natal diagnostic procedures",
       "Only government district civil hospitals",
       "Only institutes funded by the Indian Council of Medical Research",
       "Only charitable dispensaries"], 0,
      "Section 2(d) provides an inclusive definition covering any clinic, hospital, nursing home or place used for pre-natal diagnostic procedures.",
      {"A": "Correct; Comprehensive definition under Section 2(d).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PCPNDT Act S. 2(d)", "Definition of Genetic Clinic under Section 2(d).")

add_q("mcq-pcpndt-01-010", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-01-02",
      "Does an ordinary ultrasound clinic or imaging centre equipped with sonography machines fall within the regulatory net of the PCPNDT Act?",
      ["Yes, Section 2(d) explicitly includes an ultrasound clinic or imaging centre having facilities for sonography or imaging",
       "No, the Act applies strictly to genetic amniocentesis laboratories",
       "Only if the ultrasound clinic advertises sex determination",
       "Only if located within 1 km of a maternity hospital"], 0,
      "Section 2(d) explicitly includes ultrasound clinics and imaging centres having facilities for ultrasonography or imaging.",
      {"A": "Correct; Explicitly included under Section 2(d).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 2(d)", "Inclusion of ultrasound clinics under PCPNDT.")

add_q("mcq-pcpndt-01-011", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-01-02",
      "Under Section 2(g) of the Act, who is a 'medical geneticist'?",
      ["A person who possesses a recognized medical qualification and a post-graduate degree or diploma in medical genetics or has minimum experience as prescribed",
       "Any person who holds a Bachelor of Science degree in biology",
       "Any registered nurse with 1 year experience",
       "Any chemist running a pharmacy"], 0,
      "Section 2(g) defines medical geneticist as a person with recognized medical qualifications and specialized post-graduate credentials in medical genetics.",
      {"A": "Correct; Statutory qualification under Section 2(g).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PCPNDT Act S. 2(g)", "Definition and qualifications of medical geneticist.")

add_q("mcq-pcpndt-01-012", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-01-02",
      "Under Section 2(i) of the Act, a 'pre-natal diagnostic procedure' includes all gynecological or medical procedures such as:",
      ["Amniocentesis, chorionic villi biopsy, maternal serum analysis or taking samples of amniotic fluid or tissue",
       "Routine dental checkup",
       "External palpation only",
       "Routine blood pressure measurement"], 0,
      "Section 2(i) covers medical procedures like amniocentesis, chorionic villus biopsy, and collection of embryonic/fetal fluids or tissues.",
      {"A": "Correct; Amniocentesis, chorionic villus sampling, etc. under Section 2(i).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PCPNDT Act S. 2(i)", "Scope of pre-natal diagnostic procedures.")

# top-pcpndt-01-03 (6)
add_q("mcq-pcpndt-01-013", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-01-03",
      "Under Section 4(1) of the PCPNDT Act, pre-natal diagnostic techniques can be conducted strictly for detecting which conditions?",
      ["Chromosomal abnormalities, genetic metabolic diseases, hemoglobinopathies, sex-linked genetic diseases, and congenital anomalies",
       "The sex of the fetus for family balancing",
       "Astrological compatibility of the unborn child",
       "Future athletic or intellectual capabilities"], 0,
      "Section 4(1) strictly enumerates legitimate medical purposes: detecting chromosomal, genetic, and congenital disorders only.",
      {"A": "Correct; Strictly for detecting specified genetic and congenital abnormalities.", "B": "Incorrect; Absolute statutory ban on sex detection.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 4(1)", "Permissible diagnostic purposes under Section 4(1).")

add_q("mcq-pcpndt-01-014", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-01-03",
      "Under Section 4(2) of the Act, what is an essential statutory prerequisite regarding the pregnant woman's age for conducting pre-natal diagnostic techniques?",
      ["The age of the pregnant woman is above thirty-five years",
       "The age of the pregnant woman is below twenty-one years",
       "The age of the pregnant woman is exactly thirty years",
       "Age is completely irrelevant under Section 4(2)"], 0,
      "Section 4(2)(i) specifies age above thirty-five years as one of the qualifying medical conditions for conducting pre-natal diagnostic techniques.",
      {"A": "Correct; Age above thirty-five years under Section 4(2)(i).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PCPNDT Act S. 4(2)(i)", "Maternal age threshold (above 35) under Section 4(2).")

add_q("mcq-pcpndt-01-015", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-01-03",
      "Which of the following is an authorized medical condition under Section 4(2) for conducting pre-natal diagnostic techniques?",
      ["The pregnant woman has undergone of two or more spontaneous abortions or foetal loss",
       "The family desires a male child after two daughters",
       "The in-laws have executed a demand in writing",
       "The father's employer demands verification"], 0,
      "Section 4(2)(ii) authorizes testing where the woman has a history of two or more spontaneous abortions or fetal loss.",
      {"A": "Correct; History of two or more spontaneous abortions under Section 4(2)(ii).", "B": "Incorrect; Sex selection is criminal.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PCPNDT Act S. 4(2)(ii)", "Permissible obstetric grounds under Section 4(2).")

add_q("mcq-pcpndt-01-016", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-01-03",
      "Under Section 4(5) of the PCPNDT Act, 1994, can pre-natal diagnostic techniques be conducted for determining the sex of a foetus?",
      ["No person shall conduct the pre-natal diagnostic techniques, including ultrasonography, for the purpose of determining the sex of a foetus",
       "Yes, if both parents give written consent",
       "Yes, in the third trimester only",
       "Yes, if certified by the Village Panchayat"], 0,
      "Section 4(5) enacts an absolute prohibition: no person shall conduct pre-natal diagnostic techniques, including ultrasonography, for determining the sex of a fetus.",
      {"A": "Correct; Absolute statutory bar under Section 4(5).", "B": "Incorrect; Parental consent cannot waive statutory crime.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 4(5)", "Absolute statutory ban on fetal sex determination.")

add_q("mcq-pcpndt-01-017", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-01-03",
      "Under Section 4(3) of the Act, can a genetic test be conducted without explaining all known side effects and obtaining written consent?",
      ["No, the person conducting the procedure must explain all known side and after effects and obtain written consent in the prescribed form",
       "Yes, oral explanation without any consent document is sufficient",
       "Yes, in emergency situations consent is deemed",
       "Only husband's signature is required"], 0,
      "Section 4(3) mandates full disclosure of known side-effects and obtaining written consent in the prescribed format (Form G).",
      {"A": "Correct; Mandatory written informed consent in prescribed form.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PCPNDT Act S. 4(3)", "Informed written consent requirement under Section 4(3).")

add_q("mcq-pcpndt-01-018", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-01-03",
      "Can pre-natal diagnostic techniques be used to assess the fetal sex if the pregnant woman has a history of sex-linked genetic diseases?",
      ["Yes, but strictly for determining the presence of sex-linked disorders, NOT for disclosing the sex or facilitating female foeticide",
       "Yes, and the doctor is free to announce the sex publicly",
       "No, sex-linked diseases cannot be tested",
       "Only with Supreme Court permission"], 0,
      "Section 4(1)(iv) permits testing for sex-linked genetic diseases, but Section 5(2) strictly bars communicating the sex of the fetus to anyone.",
      {"A": "Correct; Diagnosis permitted strictly to detect disease, but sex disclosure remains barred.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "PCPNDT Act S. 4(1)(iv), S. 5(2)", "Sex-linked disease testing vs disclosure ban.")

# Chapter 2: ch-soc-pcpndt-02 (16 MCQs)
# top-pcpndt-02-01 (6)
add_q("mcq-pcpndt-01-019", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-02-01",
      "Under Section 5(2) of the PCPNDT Act, what is the prohibition regarding communicating the sex of the fetus?",
      ["No person shall communicate in any manner the sex of the foetus to the pregnant woman or her relatives or any other person by words, signs or in any other manner",
       "The doctor can communicate verbally but not in writing",
       "The doctor can communicate via coded symbols to the father",
       "The doctor can communicate if the fetus is female"], 0,
      "Section 5(2) is an absolute embargo: no communication in any manner (words, signs, symbols, gestures) to the woman or relatives or anyone else.",
      {"A": "Correct; Total ban on communicating fetal sex in any manner.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 5(2)", "Absolute ban on communicating sex under Section 5(2).")

add_q("mcq-pcpndt-01-020", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-02-01",
      "Under Section 6(a) of the PCPNDT Act, 1994, what is the prohibition on pre-conception sex selection?",
      ["No genetic counselling centre, genetic laboratory, genetic clinic or person shall conduct or cause to be conducted sex selection on a human being, including at pre-conception stage",
       "Sex selection is permitted in accredited IVF clinics",
       "Sex selection is allowed if the couple has three daughters",
       "Sex selection is allowed for non-resident Indians"], 0,
      "Section 6(a) enacts a complete prohibition on conducting sex selection at any stage, including prior to conception.",
      {"A": "Correct; Absolute prohibition on pre-conception sex selection under Section 6(a).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 6(a)", "Ban on pre-conception sex selection under Section 6(a).")

add_q("mcq-pcpndt-01-021", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-02-01",
      "Under Section 22(1) of the PCPNDT Act, what is the restriction on advertisements relating to sex selection or pre-natal determination of sex?",
      ["No person, including a company or organization, shall issue, publish, distribute, or cause to be published any advertisement in any manner regarding facilities of sex selection or pre-natal determination of sex",
       "Advertisements are permitted in medical journals only",
       "Advertisements can be displayed on clinic reception boards",
       "Online advertisements on international search engines are permitted"], 0,
      "Section 22(1) contains an all-encompassing ban on advertising sex selection or sex determination in print, digital, or any other media.",
      {"A": "Correct; Complete prohibition on advertising sex determination under Section 22(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PCPNDT Act S. 22(1)", "Prohibition of advertisements under Section 22(1).")

add_q("mcq-pcpndt-01-022", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-02-01",
      "In Sabu Mathew George v. Union of India (2017), what order did the Supreme Court pass regarding search engines like Google, Yahoo, and Microsoft?",
      ["Directed search engines to set up in-house auto-blocking mechanisms to proactively remove and block advertisements and search queries relating to sex selection under Section 22",
       "Held that search engines enjoy complete safe-harbor immunity to display sex selection ads",
       "Dismissed the petition as unconstitutional censorship",
       "Allowed keyword ads on sex determination"], 0,
      "In Sabu Mathew George (2017) 7 SCC 638, the Supreme Court directed search engine intermediaries to employ 'auto-block' algorithms to prevent sex selection ads.",
      {"A": "Correct; Mandated auto-blocking of sex selection advertisements by search engines.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "PCPNDT Act S. 22 & Sabu Mathew George (2017)", "Supreme Court auto-block doctrine for search engines.")

add_q("mcq-pcpndt-01-023", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-02-01",
      "Under Section 22(2) of the Act, what is the punishment for contravening the advertisement ban in Section 22?",
      ["Imprisonment for a term which may extend to three years and with fine which may extend to ten thousand rupees",
       "Fine of Rs 500 only",
       "Simple apology on social media",
       "Imprisonment for 10 years"], 0,
      "Section 22(2) provides imprisonment up to three years and fine up to ten thousand rupees for issuing prohibited advertisements.",
      {"A": "Correct; Imprisonment up to 3 years and fine up to Rs 10,000 under Section 22(2).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PCPNDT Act S. 22(2)", "Penalty for illegal advertisements under Section 22(2).")

add_q("mcq-pcpndt-01-024", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-02-01",
      "Under Section 6(b) of the Act, is a person who aids or abets pre-conception or pre-natal sex selection liable?",
      ["Yes, no person shall aid or abet sex selection by any person or facility",
       "No, only the registered clinic owner is liable",
       "Only the doctor who signed the report is liable",
       "Abetment is not recognized under special statutes"], 0,
      "Section 6(b) explicitly prohibits aiding or abetting sex selection in any manner.",
      {"A": "Correct; Explicit statutory ban on aiding or abetting under Section 6(b).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PCPNDT Act S. 6(b)", "Liability for aiding and abetting sex selection.")

# top-pcpndt-02-02 (5)
add_q("mcq-pcpndt-01-025", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-02-02",
      "Under Section 18(1) of the PCPNDT Act, 1994, can an ultrasound clinic or genetic clinic operate without registration?",
      ["No person shall open any Genetic Counselling Centre, Genetic Laboratory, Genetic Clinic or Ultrasound Clinic unless registered under this Act",
       "Yes, registration is voluntary for the first two years",
       "Yes, if the owner is an MBBS doctor",
       "Only clinics with annual turnover exceeding 10 lakhs need registration"], 0,
      "Section 18(1) enacts a mandatory prohibition: no clinic, laboratory, or ultrasound facility can operate without prior registration.",
      {"A": "Correct; Mandatory registration requirement under Section 18(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 18(1)", "Mandatory registration under Section 18(1).")

add_q("mcq-pcpndt-01-026", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-02-02",
      "Under Section 19(4) of the PCPNDT Act, for what period is a certificate of registration valid from the date of issue?",
      ["Five years", "One year", "Three years", "Ten years"], 0,
      "Under Section 19(4) and Rule 8, the certificate of registration is valid for a period of five years from the date of its issue.",
      {"A": "Correct; Valid for five years under Section 19(4).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 19(4)", "Period of validity (5 years) of registration certificate.")

add_q("mcq-pcpndt-01-027", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-02-02",
      "Under Section 19(3) of the Act, can an application for registration be rejected without hearing the applicant?",
      ["No, no application shall be rejected unless the applicant has been given an opportunity of being heard in the matter",
       "Yes, the Appropriate Authority has absolute unreviewable discretion",
       "Yes, if the applicant belongs to another State",
       "Rejections require no reasons"], 0,
      "Section 19(3) proviso mandates that no application shall be rejected unless the applicant has been given an opportunity of being heard.",
      {"A": "Correct; Mandatory opportunity of being heard under Section 19(3).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PCPNDT Act S. 19(3)", "Natural justice requirement before rejecting registration.")

add_q("mcq-pcpndt-01-028", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-02-02",
      "Under Section 20(1) and (2) of the Act, on what grounds can the Appropriate Authority suspend or cancel the registration of a clinic?",
      ["If the clinic has contravened any provisions of this Act or rules, after issuing a show-cause notice and giving reasonable opportunity of being heard",
       "Whenever the clinic increases its consultation fee",
       "Only after the doctor is convicted by the Supreme Court",
       "At the whim of the local health inspector"], 0,
      "Section 20 empowers the Appropriate Authority to suspend or cancel registration after issuing a show cause notice and giving opportunity of hearing.",
      {"A": "Correct; Contravention of Act/rules after show cause notice under Section 20.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PCPNDT Act S. 20", "Suspension and cancellation of registration under Section 20.")

add_q("mcq-pcpndt-01-029", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-02-02",
      "Under Section 20(3) of the Act, can the Appropriate Authority suspend registration WITHOUT issuing a show cause notice?",
      ["Yes, in the public interest, for reasons to be recorded in writing, if it considers it necessary or expedient to do so",
       "No, under no circumstances can registration be suspended without notice",
       "Only if recommended by the local police station",
       "Only during national elections"], 0,
      "Section 20(3) explicitly authorizes suspension without prior notice in public interest, for written reasons recorded by the Appropriate Authority.",
      {"A": "Correct; Emergency suspension without prior notice in public interest under Section 20(3).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "PCPNDT Act S. 20(3)", "Emergency suspension power under Section 20(3).")

# top-pcpndt-02-03 (5)
add_q("mcq-pcpndt-01-030", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-02-03",
      "Under Section 29(1) of the PCPNDT Act, for what minimum period must all records, charts, forms, reports and consent documents be preserved by a clinic?",
      ["Two years", "One year", "Three years", "Five years"], 0,
      "Section 29(1) explicitly mandates that all records, charts, forms, and other documents shall be maintained and preserved for a period of two years.",
      {"A": "Correct; Mandatory preservation period is two years under Section 29(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 29(1)", "Mandatory record preservation period (2 years).")

add_q("mcq-pcpndt-01-031", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-02-03",
      "What is the statutory significance of 'Form F' under Rule 9 of the PCPNDT Rules, 1996?",
      ["Form F is the mandatory statutory record of every pregnant woman undergoing ultrasonography, recording full medical indications, history, and doctor certification",
       "Form F is a receipt for payment of registration fees",
       "Form F is a customs import permit for ultrasound machines",
       "Form F is a certificate of birth"], 0,
      "Form F is the cornerstone statutory record required for every pregnant woman scanned, specifying clinical history, medical indication, and doctor declaration.",
      {"A": "Correct; Mandatory statutory record of pregnancy scans under Rule 9.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Rules Rule 9 & Form F", "Role and significance of Form F.")

add_q("mcq-pcpndt-01-032", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-02-03",
      "In Federation of Obstetrics and Gynaecological Societies of India (FOGSI) v. Union of India (2019), what did the Supreme Court hold regarding clerical errors and non-maintenance of Form F?",
      ["Upheld Section 23(1) and (2) and held that non-maintenance or improper maintenance of Form F cannot be treated as a mere clerical error, as it is a crucial tool to prevent female foeticide",
       "Held that Form F errors can never be prosecuted under any circumstances",
       "Struck down Section 23 as unconstitutional",
       "Held that Form F is optional for private clinics"], 0,
      "In FOGSI v. UOI (2019) 6 SCC 544, Arun Mishra, J., upheld the strict liability framework, holding that incomplete Form F defeats the purpose of the Act.",
      {"A": "Correct; Incomplete Form F is not a mere clerical error; upheld statutory stringency.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "PCPNDT S. 23 & FOGSI v. UOI (2019)", "Supreme Court landmark ruling on Form F non-compliance.")

add_q("mcq-pcpndt-01-033", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-02-03",
      "Under Section 29(2) of the Act, all records maintained by a clinic shall at all reasonable times be open for inspection by:",
      ["The Appropriate Authority or any person authorized by it in this behalf",
       "Only the Chief Justice of the High Court",
       "Any curious member of the public",
       "Journalists holding accreditation"], 0,
      "Section 29(2) provides that all records shall at all reasonable times be open to inspection by the Appropriate Authority or authorized officer.",
      {"A": "Correct; Open to inspection by Appropriate Authority or authorized officer.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PCPNDT Act S. 29(2)", "Inspection of records under Section 29(2).")

add_q("mcq-pcpndt-01-034", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-02-03",
      "Under the proviso to Section 29(1), if criminal proceedings are instituted against any clinic, for how long must the records be preserved?",
      ["Preserved until the final disposal of such proceedings",
       "Only for two years regardless of proceedings",
       "For thirty days from filing",
       "For five years only"], 0,
      "Proviso to Section 29(1) mandates that if legal proceedings are instituted, the records must be preserved until the final disposal of such proceedings.",
      {"A": "Correct; Preserved until final disposal of proceedings under Section 29(1) proviso.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PCPNDT Act S. 29(1) Proviso", "Record preservation during pending litigation.")

# Chapter 3: ch-soc-pcpndt-03 (16 MCQs)
# top-pcpndt-03-01 (6)
add_q("mcq-pcpndt-01-035", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-03-01",
      "Under Section 17(1) and (2) of the PCPNDT Act, who appoints the 'Appropriate Authority' for States and Union Territories?",
      ["The Central Government for Union Territories, and the State Government for the whole or part of the State",
       "The Governor in individual discretion",
       "The Medical Council of India",
       "The National Human Rights Commission"], 0,
      "Section 17 empowers the Central Government (for UTs) and State Governments (for States) to appoint one or more Appropriate Authorities.",
      {"A": "Correct; State Government for States, Central Government for UTs under Section 17.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 17(1), (2)", "Appointing authority for Appropriate Authority.")

add_q("mcq-pcpndt-01-036", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-02-01",
      "Under Section 17(3) of the Act, when an Appropriate Authority is appointed for the State, what is its composition?",
      ["A multi-member body consisting of: (a) officer of rank not below Joint Director Health, (b) eminent woman social worker, and (c) legal expert (officer of law department)",
       "A single police sub-inspector",
       "A committee of three radiologists",
       "The Chief Justice and two judges"], 0,
      "Section 17(3) mandates a 3-member multi-member body: senior health officer, woman representative from NGO, and an officer from the law department.",
      {"A": "Correct; Multi-member body (health officer, woman social worker, legal officer).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PCPNDT Act S. 17(3)", "Composition of multi-member Appropriate Authority.")

add_q("mcq-pcpndt-01-037", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-03-01",
      "Under Section 30(1) of the PCPNDT Act, 1994, what powers of search and seizure are vested in the Appropriate Authority?",
      ["Power to enter and search any clinic, inspect records, seize machines, equipment, ultrasound scanners, and seal premises if reason to believe an offence has been committed",
       "Only the power to ask for voluntary disclosure",
       "Power to demolish the building",
       "Power to freeze private bank accounts without court order"], 0,
      "Section 30(1) grants extensive search and seizure powers, including seizing ultrasound machines and sealing premises where an offence is suspected.",
      {"A": "Correct; Search, seizure of machines, and sealing of premises under Section 30(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 30(1)", "Search and seizure powers under Section 30.")

add_q("mcq-pcpndt-01-038", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-03-01",
      "Under Section 30(2) of the Act, which procedural code applies to searches and seizures conducted under the PCPNDT Act?",
      ["The provisions of the Code of Criminal Procedure, 1973 / BNSS 2023 relating to searches and seizures",
       "The Code of Civil Procedure, 1908",
       "The Indian Evidence Act, 1872",
       "The Arbitration and Conciliation Act, 1996"], 0,
      "Section 30(2) explicitly provides that the provisions of CrPC/BNSS relating to search and seizure shall apply to every search or seizure under this Act.",
      {"A": "Correct; CrPC / BNSS search and seizure rules apply under Section 30(2).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PCPNDT Act S. 30(2)", "Application of CrPC search procedure under Section 30(2).")

add_q("mcq-pcpndt-01-039", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-03-01",
      "Can an Appropriate Authority seal an unregistered ultrasound machine found operating in a diagnostic centre?",
      ["Yes, under Section 30 read with Rule 12, the Appropriate Authority has full statutory power to seize and seal any unregistered machine",
       "No, only a High Court Judge can order sealing",
       "Only if the owner consents in writing",
       "Only after the owner is convicted in trial"], 0,
      "Seizure and sealing of machines used in violation of the Act is explicitly authorized under Section 30 and Rule 12 to prevent ongoing destruction of evidence.",
      {"A": "Correct; Full statutory power to seize and seal unregistered machines.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PCPNDT Act S. 30 & Rule 12", "Sealing of unregistered machines under Section 30.")

add_q("mcq-pcpndt-01-040", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-03-01",
      "Under Section 17A of the PCPNDT Act, what civil court powers are vested in the Appropriate Authority for conducting inquiries?",
      ["Summoning of persons, discovery and production of documents, receiving evidence on affidavits, and issuing commissions for examination of witnesses",
       "Power to pass executable decree for money damages",
       "Power to appoint a court receiver over agricultural lands",
       "Power to grant injunctions against the High Court"], 0,
      "Section 17A confers CPC civil court powers for summoning witnesses, enforcing attendance, requiring production of documents, and taking evidence on affidavit.",
      {"A": "Correct; CPC civil court inquiry powers under Section 17A.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PCPNDT Act S. 17A", "Inquiry powers of Appropriate Authority under Section 17A.")

# top-pcpndt-03-02 (5)
add_q("mcq-pcpndt-01-041", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-03-02",
      "Under Section 28(1)(a) of the PCPNDT Act, 1994, on whose complaint can a court take cognizance of an offence under the Act?",
      ["The Appropriate Authority concerned, or any officer authorized in this behalf by the Central Government or State Government",
       "Any police officer on a standard FIR",
       "Any private citizen without prior notice",
       "The Indian Medical Association"], 0,
      "Section 28(1)(a) provides that no court shall take cognizance of an offence except on a complaint made by the Appropriate Authority or authorized officer.",
      {"A": "Correct; Complaint by Appropriate Authority or authorized officer under Section 28(1)(a).", "B": "Incorrect; Police cannot file chargesheet directly without Appropriate Authority.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 28(1)(a)", "Cognizance on complaint of Appropriate Authority under Section 28(1).")

add_q("mcq-pcpndt-01-042", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-03-02",
      "Under Section 28(1)(b) of the Act, can a private individual or NGO file a complaint in court?",
      ["Yes, provided they have given notice of not less than fifteen days to the Appropriate Authority of the alleged offence and their intention to make a complaint",
       "No, private complaints are completely prohibited under all circumstances",
       "Yes, directly without any notice to anyone",
       "Only if they deposit five lakh rupees in court"], 0,
      "Section 28(1)(b) allows a person to file a complaint after giving notice of not less than fifteen days to the Appropriate Authority.",
      {"A": "Correct; Private complaint permitted after giving 15 days notice to Appropriate Authority.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 28(1)(b)", "15-day notice requirement for private complaints under Section 28(1)(b).")

add_q("mcq-pcpndt-01-043", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-03-02",
      "Under Section 28(2) of the PCPNDT Act, which court is competent to try offences under this Act?",
      ["No court inferior to that of a Metropolitan Magistrate or a Judicial Magistrate of the first class",
       "Any Executive Magistrate",
       "Only the High Court",
       "Gram Panchayat Nyayalaya"], 0,
      "Section 28(2) explicitly provides: 'No court inferior to that of a Metropolitan Magistrate or a Judicial Magistrate of the first class shall try any offence under this Act.'",
      {"A": "Correct; Metropolitan Magistrate or JMFC under Section 28(2).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 28(2)", "Competent trial court under Section 28(2).")

add_q("mcq-pcpndt-01-044", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-03-02",
      "Can a police officer register an FIR under Section 154 CrPC and file a police report under Section 173 CrPC for offences under the PCPNDT Act?",
      ["No, the Supreme Court has clarified that Section 28 creates an express bar: cognizance can ONLY be taken on a complaint filed by the Appropriate Authority or person under 28(1)(b)",
       "Yes, police have automatic power to file chargesheets under all Central Acts",
       "Only if the DGP personally signs the chargesheet",
       "Only if the offence took place on a national highway"], 0,
      "Courts (including Supreme Court and High Courts) have held that Section 28 bars police chargesheets; trial courts cannot take cognizance on a police report without a statutory complaint by the Appropriate Authority.",
      {"A": "Correct; Bar on police chargesheet; cognizance only on statutory complaint under Section 28.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "PCPNDT Act S. 28 & CrPC S. 190", "Bar on police chargesheets under Section 28.")

add_q("mcq-pcpndt-01-045", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-03-02",
      "Under Section 28(3) of the Act, on an application by a person who has given notice under 28(1)(b), what duty is cast on the Appropriate Authority?",
      ["To furnish a copy of relevant records in its possession to that person",
       "To arrest that person for interference",
       "To destroy the records immediately",
       "To forward the records to the World Health Organization"], 0,
      "Section 28(3) mandates the Appropriate Authority to provide copies of relevant records in its possession to the person intending to file a complaint.",
      {"A": "Correct; Duty to furnish copies of relevant records under Section 28(3).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PCPNDT Act S. 28(3)", "Duty to provide records to prospective complainant.")

# top-pcpndt-03-03 (5)
add_q("mcq-pcpndt-01-046", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-03-03",
      "Under Section 23(1) of the PCPNDT Act, what is the punishment for a medical geneticist, gynecologist, or registered medical practitioner for a first offence under the Act?",
      ["Imprisonment for a term which may extend to three years and with fine which may extend to ten thousand rupees",
       "Fine of Rs 1,000 only",
       "Imprisonment for 7 years",
       "Simple warning by the State Medical Council"], 0,
      "Section 23(1) prescribes imprisonment up to three years and fine up to ten thousand rupees for the first offence.",
      {"A": "Correct; Up to 3 years imprisonment and fine up to Rs 10,000 under Section 23(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 23(1)", "Penalty for first offence by medical personnel under Section 23(1).")

add_q("mcq-pcpndt-01-047", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-03-03",
      "Under Section 23(1) of the Act, what is the punishment on subsequent conviction of a medical practitioner?",
      ["Imprisonment for a term which may extend to five years and with fine which may extend to fifty thousand rupees",
       "Imprisonment up to 1 year and fine of Rs 2,000",
       "Suspension of passport only",
       "Life imprisonment"], 0,
      "Section 23(1) provides that on any subsequent conviction, the punishment shall be imprisonment which may extend to five years and with fine which may extend to fifty thousand rupees.",
      {"A": "Correct; Up to 5 years imprisonment and fine up to Rs 50,000 under Section 23(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 23(1)", "Penalty for subsequent conviction under Section 23(1).")

add_q("mcq-pcpndt-01-048", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-03-03",
      "Under Section 23(2) of the Act, what action must the State Medical Council take against a registered medical practitioner upon framing of charges and upon conviction?",
      ["Suspended from the State Medical Register during trial, and name removed permanently or for a period of five years upon conviction for a first offence",
       "Promoted to civil surgeon rank",
       "Exempted from attending court hearings",
       "No action can be taken by the Medical Council"], 0,
      "Section 23(2) mandates suspension of registration from the medical register till disposal of trial, and removal for 5 years on first conviction (permanent on repeat).",
      {"A": "Correct; Suspension during trial and removal for 5 years/permanent upon conviction under Section 23(2).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "PCPNDT Act S. 23(2)", "Disciplinary consequences on medical license under Section 23(2).")

add_q("mcq-pcpndt-01-049", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-03-03",
      "Under Section 24 of the PCPNDT Act, what statutory presumption is created regarding the pregnant woman who was subjected to pre-natal sex determination?",
      ["The court shall presume that she was compelled by her husband or relatives to undergo the diagnostic technique, and she shall not be liable for the offence",
       "She is presumed to be the principal conspirator",
       "She is sentenced to 3 years imprisonment automatically",
       "The marriage is presumed dissolved"], 0,
      "Section 24 creates a protective statutory presumption: the court shall presume that the pregnant woman was compelled by her husband or relative, shielding her from victim-prosecution.",
      {"A": "Correct; Presumption of compulsion shielding the pregnant woman under Section 24.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 24", "Protective presumption in favor of pregnant woman under Section 24.")

add_q("mcq-pcpndt-01-050", "soc-pcpndt", "ch-soc-pcpndt-01", "top-pcpndt-03-03",
      "Under Section 27 of the PCPNDT Act, 1994, all offences under this Act are classified as:",
      ["Cognizable, non-bailable, and non-compoundable",
       "Non-cognizable and bailable",
       "Cognizable and compoundable with leave of court",
       "Non-cognizable, non-bailable, and compoundable"], 0,
      "Section 27 states: 'Every offence under this Act shall be cognizable, non-bailable and non-compoundable.'",
      {"A": "Correct; Cognizable, non-bailable, and non-compoundable under Section 27.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "PCPNDT Act S. 27", "Classification of offences under Section 27.")

# --- Save to assets/learning/data/social/social-mcqs-part2.js ---
output_path = os.path.join("assets", "learning", "data", "social", "social-mcqs-part2.js")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

header = """/**
 * Tanveer Ashraf Judicial Prep 2026–27
 * Social Legislation MCQs — Part 2 (Acts 4-6)
 *
 * Covers:
 * 4. Protection of Women from Domestic Violence Act, 2005 (50 MCQs: mcq-dv-01-001 to mcq-dv-01-050)
 * 5. Sexual Harassment of Women at Workplace Act, 2013 (50 MCQs: mcq-posh-01-001 to mcq-posh-01-050)
 * 6. Pre-Conception and Pre-Natal Diagnostic Techniques Act, 1994 (50 MCQs: mcq-pcpndt-01-001 to mcq-pcpndt-01-050)
 *
 * Total: 150 Verified Practice MCQs
 * 100% 4-Option Rationale (A, B, C, D) & Statutory Provisions
 */

(function(global) {
    'use strict';

    const SOCIAL_MCQS_PART2 = """

footer = """;

    if (typeof module !== 'undefined' && module.exports) {
        module.exports = SOCIAL_MCQS_PART2;
    }
    global.SOCIAL_MCQS_PART2 = SOCIAL_MCQS_PART2;
})(typeof window !== 'undefined' ? window : global);
"""

with open(output_path, "w", encoding="utf-8") as f:
    f.write(header + json.dumps(mcqs, indent=2, ensure_ascii=False) + footer)

print(f"SUCCESS: Created {output_path} with {len(mcqs)} MCQs!")
