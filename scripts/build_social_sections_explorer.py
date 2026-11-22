"""
Build Social Sections Explorer
Generates 98 high-yield statutory provisions across the 9 Social Legislation Acts
Output: assets/learning/data/social/social-sections-explorer.js
"""

import json
import os

entries = []

def add_sec(sid, act_id, act_name, ref, title, concept, plain, conds, exps, pen, top_id, ch_id, source_lbl, tips):
    entries.append({
        "id": sid,
        "actId": act_id,
        "actName": act_name,
        "type": "section",
        "ref": ref,
        "title": title,
        "concept": concept,
        "plainEnglish": plain,
        "conditions": conds,
        "exceptions": exps,
        "penalties": pen,
        "relatedTopicId": top_id,
        "chapterId": ch_id,
        "sourceLabel": source_lbl,
        "indiaCodeUrl": "https://www.indiacode.nic.in",
        "examTips": tips,
        "highYield": True
    })

# ==========================================
# ACT 1: RPwD Act 2016 (soc-disabilities) - 12 provisions
# ==========================================
add_sec("soc-sec-disab-01", "soc-disabilities", "Rights of Persons with Disabilities Act, 2016",
        "Section 2(r)", "Person with Benchmark Disability",
        "Person with not less than 40% of a specified disability where defined in measurable terms, certified by certifying authority.",
        "To get reservations and quota benefits, disability must be certified as at least 40%.",
        ["Certified by notified medical certifying authority.", "Minimum 40% threshold for measurable disabilities."],
        ["Reasonable accommodation under Section 3 does not require 40% (Vikas Kumar)."],
        "None (Definition)", "top-disab-01-02", "ch-soc-disab-01", "RPwD Act S. 2(r)",
        "Crucial UP PCS-J trap: 40% is needed for reservations, but non-discrimination and accommodation apply to ALL disabled persons.")

add_sec("soc-sec-disab-02", "soc-disabilities", "Rights of Persons with Disabilities Act, 2016",
        "Section 2(s)", "Person with Disability",
        "Person with long-term physical, mental, intellectual or sensory impairment which in interaction with barriers hinders full and effective participation.",
        "Adopts the UNCRPD social/interactive model rather than a purely medical defect model.",
        ["Long-term impairment.", "Interaction with environmental/social barriers hinders equal participation."],
        ["None."],
        "None (Definition)", "top-disab-01-02", "ch-soc-disab-01", "RPwD Act S. 2(s)",
        "Distinguish Section 2(s) (general disability) from Section 2(r) (benchmark 40%).")

add_sec("soc-sec-disab-03", "soc-disabilities", "Rights of Persons with Disabilities Act, 2016",
        "Section 2(y)", "Reasonable Accommodation",
        "Necessary and appropriate modification and adjustments, not imposing a disproportionate or undue burden, to ensure equal rights.",
        "Making required changes in workplace, exams, or premises so a disabled person can work or study equally.",
        ["Necessary and appropriate adjustments.", "Must not impose disproportionate or undue burden on establishment."],
        ["None."],
        "None (Definition)", "top-disab-01-02", "ch-soc-disab-01", "RPwD Act S. 2(y)",
        "Supreme Court in Vikas Kumar (2021) held reasonable accommodation is an intrinsic facet of Article 14 equality.")

add_sec("soc-sec-disab-04", "soc-disabilities", "Rights of Persons with Disabilities Act, 2016",
        "Section 3", "Equality and Non-Discrimination",
        "Mandates appropriate Government to ensure equality, dignity, and respect for integrity, prohibiting discrimination on ground of disability.",
        "Guarantees that no person is discriminated against due to disability, and requires reasonable accommodation.",
        ["Applies to all persons with disability across public and private spheres.", "No deprivation of personal liberty."],
        ["Disability distinction permitted only if it is a proportionate means of achieving a legitimate aim."],
        "Breach attracts Section 89 penalty", "top-disab-01-01", "ch-soc-disab-01", "RPwD Act S. 3",
        "Section 3(1) protects dignity; Section 3(3) allows differentiation only for legitimate proportionate aims.")

add_sec("soc-sec-disab-05", "soc-disabilities", "Rights of Persons with Disabilities Act, 2016",
        "Section 16", "Duty of Educational Institutions",
        "Mandates funded/recognized schools to provide inclusive education without discrimination, ensuring accessible campus and recreation.",
        "Schools cannot deny admission to disabled children and must provide equal sports and education facilities.",
        ["All government-funded or recognized schools.", "Admit without discrimination."],
        ["None."],
        "None", "top-disab-02-02", "ch-soc-disab-02", "RPwD Act S. 16",
        "Remember inclusive education is statutory; segregation into separate wings is prohibited.")

add_sec("soc-sec-disab-06", "soc-disabilities", "Rights of Persons with Disabilities Act, 2016",
        "Section 20", "Non-Discrimination in Employment",
        "Prohibits discrimination in government employment; bars denial of promotion; bars reduction in rank or termination upon acquiring disability.",
        "An employee who becomes disabled during service cannot be fired or demoted; must be protected on equivalent pay or supernumerary post.",
        ["No dismissal or rank reduction upon acquiring disability.", "Promotion cannot be denied merely on disability."],
        ["Establishment may be exempted by Government notification having regard to nature of work."],
        "Section 89 fine", "top-disab-02-01", "ch-soc-disab-02", "RPwD Act S. 20",
        "Section 20(4) supernumerary post protection is high-yield for judicial questions on service rights.")

add_sec("soc-sec-disab-07", "soc-disabilities", "Rights of Persons with Disabilities Act, 2016",
        "Section 31", "Free Education for Children with Benchmark Disability",
        "Every child with benchmark disability between 6 and 18 years has the right to free education in a neighbourhood school or special school.",
        "Expands the RTE Act 6-14 year bracket up to age 18 for children with benchmark disabilities.",
        ["Benchmark disability (40%+).", "Age between 6 and 18 years."],
        ["None."],
        "None", "top-disab-02-02", "ch-soc-disab-02", "RPwD Act S. 31",
        "Frequently tested: general RTE is 6-14 years, but RPwD Section 31 expands it to 6-18 years.")

add_sec("soc-sec-disab-08", "soc-disabilities", "Rights of Persons with Disabilities Act, 2016",
        "Section 32", "Reservation in Higher Educational Institutions",
        "All government and government-aided higher educational institutions must reserve not less than 5% seats and give 5 years upper age relaxation.",
        "At least 5% seats in colleges and universities reserved for benchmark disabled, with 5-year age relaxation.",
        ["Benchmark disability.", "Government and government-aided higher education institutions."],
        ["Private unaided institutions not covered under Section 32."],
        "None", "top-disab-02-01", "ch-soc-disab-02", "RPwD Act S. 32",
        "High-yield distinction: 5% for higher education under S. 32, but 4% for public employment under S. 34.")

add_sec("soc-sec-disab-09", "soc-disabilities", "Rights of Persons with Disabilities Act, 2016",
        "Section 34", "Reservation in Public Employment",
        "Mandates appointment of not less than 4% of total vacancies in cadre strength in government establishments for benchmark disabled.",
        "Every government office must provide at least 4% reservation across five sub-categories (1% each for blindness, deaf, locomotor, and 1% for autism/multiple).",
        ["Benchmark disability.", "Covers Groups A, B, C, D in government establishments."],
        ["Appropriate Government may exempt any establishment by notification."],
        "None", "top-disab-02-01", "ch-soc-disab-02", "RPwD Act S. 34",
        "The 1995 Act had 3%; the 2016 Act increased public employment quota to not less than 4%.")

add_sec("soc-sec-disab-10", "soc-disabilities", "Rights of Persons with Disabilities Act, 2016",
        "Section 45", "Time Limit for Accessibility of Existing Infrastructure",
        "All existing public buildings shall be made accessible within a period not exceeding five years from notification of rules.",
        "Five-year deadline for government and municipal bodies to retrofit ramps, lifts, and tactile paths in existing public buildings.",
        ["Applies to existing public buildings.", "Five-year statutory window from notification."],
        ["None."],
        "Section 89 fine", "top-disab-02-03", "ch-soc-disab-02", "RPwD Act S. 45",
        "Supreme Court in Rajive Raturi (2018) monitored implementation of this 5-year deadline.")

add_sec("soc-sec-disab-11", "soc-disabilities", "Rights of Persons with Disabilities Act, 2016",
        "Section 89", "General Penalty for Contravention",
        "Fine up to Rs 10,000 for first contravention; fine not less than Rs 50,000 extending up to Rs 5,00,000 for subsequent contraventions.",
        "General monetary fines for violating provisions or rules of the Act where no specific penalty is provided.",
        ["First offence: fine up to Rs 10,000.", "Subsequent offence: fine of Rs 50,000 to Rs 5,00,000."],
        ["None."],
        "Fine Rs 10k (first) / Rs 50k-5L (subsequent)", "top-disab-03-03", "ch-soc-disab-03", "RPwD Act S. 89",
        "Section 89 provides only fines, no imprisonment. Compare with Section 92 which carries jail terms.")

add_sec("soc-sec-disab-12", "soc-disabilities", "Rights of Persons with Disabilities Act, 2016",
        "Section 92", "Punishment for Offences of Atrocities",
        "Penalizes insulting, humiliating in public view, assaulting, sexually exploiting, or forcing non-consensual medical termination of pregnancy on disabled persons.",
        "Jail term of 6 months to 5 years plus fine for public humiliation, assault, denying food/water, or forced abortion of a disabled person.",
        ["Public view requirement for humiliation.", "Covers assault, exploitation, and non-consensual termination."],
        ["None."],
        "Imprisonment 6 months to 5 years and fine", "top-disab-03-03", "ch-soc-disab-03", "RPwD Act S. 92",
        "Section 92 is the core penal atrocity section: 6 months to 5 years imprisonment and mandatory fine.")

# ==========================================
# ACT 2: Senior Citizens Act 2007 (soc-parents) - 12 provisions
# ==========================================
add_sec("soc-sec-parent-01", "soc-parents", "Maintenance and Welfare of Parents and Senior Citizens Act, 2007",
        "Section 2(a)", "Children",
        "Includes son, daughter, grandson and grand-daughter, but does not include a minor.",
        "Biological and adopted sons, daughters, and grandchildren are liable; minors are strictly excluded.",
        ["Must have attained majority (18+ years).", "Includes married daughters."],
        ["Minors are explicitly excluded from being sued."],
        "None (Definition)", "top-parent-01-02", "ch-soc-parent-01", "Senior Citizens Act S. 2(a)",
        "Crucial trap: 'Children' does NOT include minors. Married daughters are covered.")

add_sec("soc-sec-parent-02", "soc-parents", "Maintenance and Welfare of Parents and Senior Citizens Act, 2007",
        "Section 2(d)", "Parent",
        "Father or mother whether biological, adoptive or step-father or step-mother, whether or not a senior citizen.",
        "Parents can claim maintenance from adult children even if the parents have not yet reached 60 years of age.",
        ["Biological, adoptive, or step-father/mother."],
        ["Parent DOES NOT need to be sixty years old."],
        "None (Definition)", "top-parent-01-02", "ch-soc-parent-01", "Senior Citizens Act S. 2(d)",
        "High-yield UP PCS-J trap: Senior citizen must be 60+, but a PARENT need NOT be 60.")

add_sec("soc-sec-parent-03", "soc-parents", "Maintenance and Welfare of Parents and Senior Citizens Act, 2007",
        "Section 2(h)", "Senior Citizen",
        "Any person being a citizen of India, who has attained the age of sixty years or above.",
        "Must be an Indian citizen and at least 60 years old.",
        ["Indian citizenship.", "Age 60 years or above."],
        ["Non-citizens cannot claim senior citizen benefits."],
        "None (Definition)", "top-parent-01-02", "ch-soc-parent-01", "Senior Citizens Act S. 2(h)",
        "Age threshold is strictly 60 years.")

add_sec("soc-sec-parent-04", "soc-parents", "Maintenance and Welfare of Parents and Senior Citizens Act, 2007",
        "Section 4", "Maintenance of Parents and Senior Citizens",
        "Obligation of children or relatives to maintain senior citizens/parents who are unable to maintain themselves from own earnings or property.",
        "Children must provide basic needs so parent can lead a normal life; childless senior citizens can claim against prospective inheriting relatives.",
        ["Inability to maintain self from earnings or property.", "Relative liability proportional to prospective inheritance share."],
        ["None."],
        "Recovery warrant / Imprisonment under S. 11", "top-parent-01-03", "ch-soc-parent-01", "Senior Citizens Act S. 4",
        "Standard of maintenance is 'so that the parent may lead a normal life' (Section 4(3)).")

add_sec("soc-sec-parent-05", "soc-parents", "Maintenance and Welfare of Parents and Senior Citizens Act, 2007",
        "Section 5", "Application for Maintenance & Disposal Timeline",
        "Application filed by senior citizen/parent, authorized NGO, or suo motu by Tribunal; target disposal within 90 days (extendable by 30 days).",
        "Simple application process; Tribunal can award interim maintenance and must decide within 90 days.",
        ["Service of notice.", "Ordinarily decided in 90 days; one-time extension of max 30 days for written reasons."],
        ["None."],
        "Interim maintenance under S. 5(2)", "top-parent-02-01", "ch-soc-parent-02", "Senior Citizens Act S. 5",
        "Remember timeline: 90 days target disposal, max 30-day extension once.")

add_sec("soc-sec-parent-06", "soc-parents", "Maintenance and Welfare of Parents and Senior Citizens Act, 2007",
        "Section 7", "Constitution of Maintenance Tribunal",
        "State Government constitutes Tribunal for each sub-division, presided over by an officer not below the rank of Sub-Divisional Officer (SDO/SDM).",
        "SDM presides over the Maintenance Tribunal at the sub-divisional level.",
        ["Sub-divisional level jurisdiction.", "Presided by SDM / SDO."],
        ["Not presided by a judicial magistrate."],
        "None", "top-parent-02-02", "ch-soc-parent-02", "Senior Citizens Act S. 7",
        "Maintenance Tribunal is an executive/administrative body headed by SDM, not a regular civil court.")

add_sec("soc-sec-parent-07", "soc-parents", "Maintenance and Welfare of Parents and Senior Citizens Act, 2007",
        "Section 9(2)", "Statutory Ceiling on Maintenance Allowance",
        "Maximum maintenance allowance ordered by Tribunal shall not exceed ten thousand rupees per month (Rs 10,000/-).",
        "Statutory cap of Rs 10,000 per month in the parent Act.",
        ["Prescribed by State Govt, subject to maximum ceiling of Rs 10,000/month."],
        ["None in enacted text."],
        "None", "top-parent-02-02", "ch-soc-parent-02", "Senior Citizens Act S. 9(2)",
        "The statutory ceiling under Section 9(2) is strictly Rs 10,000 per month.")

add_sec("soc-sec-parent-08", "soc-parents", "Maintenance and Welfare of Parents and Senior Citizens Act, 2007",
        "Section 15 & 16", "Appellate Tribunal & Limitation",
        "Appellate Tribunal for each district presided by District Magistrate (DM); appeal by senior citizen/parent within 60 days.",
        "DM hears appeals against SDM tribunal orders within 60 days of the order.",
        ["District level.", "Presided by District Magistrate.", "Appeal limitation is 60 days."],
        ["Literal text of Section 16(1) only mentions appeal by senior citizen/parent, not children."],
        "None", "top-parent-02-03", "ch-soc-parent-02", "Senior Citizens Act S. 15, 16",
        "Appellate Tribunal is presided by DM; appeal period is 60 days.")

add_sec("soc-sec-parent-09", "soc-parents", "Maintenance and Welfare of Parents and Senior Citizens Act, 2007",
        "Section 17", "Bar on Legal Practitioners",
        "Notwithstanding anything contained in any law, no party to a proceeding before Tribunal or Appellate Tribunal shall be represented by a legal practitioner.",
        "Advocates are completely barred from representing parties before Maintenance and Appellate Tribunals.",
        ["Non-obstante clause overriding Advocates Act and CrPC."],
        ["None in statutory text."],
        "None", "top-parent-02-02", "ch-soc-parent-02", "Senior Citizens Act S. 17",
        "Frequently tested: Section 17 enacts an absolute statutory bar on legal practitioners.")

add_sec("soc-sec-parent-10", "soc-parents", "Maintenance and Welfare of Parents and Senior Citizens Act, 2007",
        "Section 23", "Transfer of Property Void in Certain Circumstances",
        "Property transfer by gift/otherwise post-commencement subject to condition of basic amenities may be declared void if transferee fails to provide them.",
        "If a senior citizen gifted property on condition of care and the child stops taking care, Tribunal can cancel the transfer and evict the child.",
        ["Transfer made after commencement of Act.", "Subject to condition of providing basic amenities/physical needs.", "Failure or refusal to provide them."],
        ["Unconditional transfers made prior to commencement not covered (Sudesh Chhikara)."],
        "Deemed transfer by fraud/coercion/undue influence", "top-parent-03-01", "ch-soc-parent-03", "Senior Citizens Act S. 23",
        "Section 23 creates a legal fiction of fraud/coercion; widely used for cancelling gift deeds and eviction.")

add_sec("soc-sec-parent-11", "soc-parents", "Maintenance and Welfare of Parents and Senior Citizens Act, 2007",
        "Section 24", "Penalty for Abandonment of Senior Citizen",
        "Whoever, having care or protection of a senior citizen, leaves them in any place with intention of wholly abandoning them is punished.",
        "Jail up to 3 months, or fine up to Rs 5,000, or both, for abandoning an elderly parent or senior citizen.",
        ["Must have care or custody.", "Intent to wholly abandon."],
        ["None."],
        "Imprisonment up to 3 months or fine up to Rs 5,000 or both", "top-parent-03-03", "ch-soc-parent-03", "Senior Citizens Act S. 24",
        "Only substantive penal offence in the Act: max 3 months imprisonment or Rs 5,000 fine or both.")

add_sec("soc-sec-parent-12", "soc-parents", "Maintenance and Welfare of Parents and Senior Citizens Act, 2007",
        "Section 25", "Cognizance and Trial of Offences",
        "Every offence under this Act shall be cognizable and bailable, and tried summarily by a Judicial Magistrate of the First Class.",
        "Abandonment under Section 24 is cognizable, bailable, and tried summarily by a JMFC.",
        ["Cognizable and bailable.", "Summary trial by JMFC or Metropolitan Magistrate."],
        ["None."],
        "None", "top-parent-03-03", "ch-soc-parent-03", "Senior Citizens Act S. 25",
        "Note classification: cognizable AND bailable under Section 25(1).")

# ==========================================
# ACT 3: Dowry Prohibition Act 1961 (soc-dowry) - 10 provisions
# ==========================================
add_sec("soc-sec-dowry-01", "soc-dowry", "Dowry Prohibition Act, 1961",
        "Section 2", "Definition of Dowry",
        "Any property or valuable security given or agreed to be given at, before, or anytime after marriage in connection with the marriage.",
        "Covers property demanded or given before, at, or after wedding in connection with marriage; excludes Muslim mahr.",
        ["At, before, or anytime after marriage.", "In connection with marriage."],
        ["Excludes dower or mahr under Muslim Personal Law."],
        "Penalty under S. 3 and 4", "top-dowry-01-02", "ch-soc-dowry-01", "Dowry Prohibition Act S. 2",
        "1986 amendment replaced 'as consideration for the marriage' with 'in connection with the marriage'.")

add_sec("soc-sec-dowry-02", "soc-dowry", "Dowry Prohibition Act, 1961",
        "Section 3", "Penalty for Giving or Taking Dowry",
        "Mandatory imprisonment of not less than five years, and fine not less than Rs 15,000 or value of dowry, whichever is more.",
        "Both giving and taking dowry are punishable with minimum 5 years imprisonment and heavy fine.",
        ["Giving, taking, or abetting giving/taking."],
        ["Presents given to bride without demand entered in statutory list under 1985 Rules are exempt."],
        "Min 5 years imprisonment and fine min Rs 15,000 or value of dowry", "top-dowry-02-01", "ch-soc-dowry-02", "Dowry Prohibition Act S. 3",
        "Mandatory minimum is 5 years; court can award less only for adequate and special reasons in judgment.")

add_sec("soc-sec-dowry-03", "soc-dowry", "Dowry Prohibition Act, 1961",
        "Section 4", "Penalty for Demanding Dowry",
        "Demanding dowry directly or indirectly from parents or guardians is punishable with imprisonment of 6 months to 2 years and fine up to Rs 10,000.",
        "Mere demand of dowry during negotiations or after marriage is an offence even if no money is actually paid.",
        ["Bare demand directly or indirectly.", "No actual transfer needed."],
        ["Court may award less than 6 months for adequate and special reasons."],
        "Imprisonment 6 months to 2 years and fine up to Rs 10,000", "top-dowry-02-01", "ch-soc-dowry-02", "Dowry Prohibition Act S. 4",
        "Differentiate S. 3 (giving/taking: 5 yrs) from S. 4 (mere demand: 6m-2y). S. Gopal Reddy ruling applies.")

add_sec("soc-sec-dowry-04", "soc-dowry", "Dowry Prohibition Act, 1961",
        "Section 4A", "Ban on Dowry Advertisements",
        "Prohibits printing, publishing, or circulating advertisements offering share in property/money as consideration for marriage.",
        "Bans matrimonial ads offering cash, cars, or property; advertiser and publisher both liable to 6m-5y jail or fine up to Rs 15,000.",
        ["Printing, publishing, or circulating in any media."],
        ["Court may award less than 6 months for adequate and special reasons."],
        "Imprisonment 6 months to 5 years or fine up to Rs 15,000", "top-dowry-02-02", "ch-soc-dowry-02", "Dowry Prohibition Act S. 4A",
        "Inserted by 1986 amendment; punishes both advertiser and publisher.")

add_sec("soc-sec-dowry-05", "soc-dowry", "Dowry Prohibition Act, 1961",
        "Section 5", "Agreement for Giving or Taking Dowry to be Void",
        "Any agreement for the giving or taking of dowry shall be void ab initio.",
        "Dowry contracts are illegal and void; cannot be enforced in civil courts under Contract Act Section 23.",
        ["Any agreement for dowry."],
        ["None."],
        "Void ab initio", "top-dowry-02-02", "ch-soc-dowry-02", "Dowry Prohibition Act S. 5",
        "Connect Section 5 DP Act with Section 23 Indian Contract Act (unlawful consideration).")

add_sec("soc-sec-dowry-06", "soc-dowry", "Dowry Prohibition Act, 1961",
        "Section 6", "Dowry for Benefit of Wife & Trust Obligation",
        "Dowry received by any other person must be transferred to the woman within 3 months; held in trust pending transfer.",
        "In-laws who receive dowry hold it as trustees and must transfer it to the woman within 3 months; failure carries 6m-2y jail.",
        ["Must transfer within 3 months of marriage (if received before) or receipt (if received at/after)."],
        ["If woman dies unnaturally within 7 years, transfers to her parents/children, not husband."],
        "Imprisonment 6 months to 2 years or fine Rs 5,000 to Rs 10,000 or both", "top-dowry-02-03", "ch-soc-dowry-02", "Dowry Prohibition Act S. 6",
        "Section 6(3): if woman dies unnaturally within 7 years without children, property reverts to her parents.")

add_sec("soc-sec-dowry-07", "soc-dowry", "Dowry Prohibition Act, 1961",
        "Section 7", "Cognizance of Offences",
        "No court inferior to Metropolitan Magistrate or JMFC shall try offences; cognizance on own knowledge, police report, or aggrieved/NGO complaint.",
        "Trial by JMFC; complaints can be filed by victim, parents, or recognized welfare NGOs; CrPC limitation excluded.",
        ["JMFC or Metropolitan Magistrate.", "Chapter XXXVI CrPC limitation completely excluded under S. 7(2)."],
        ["None."],
        "None", "top-dowry-03-01", "ch-soc-dowry-03", "Dowry Prohibition Act S. 7",
        "Section 7(2) specifically excludes CrPC limitation; Section 7(3) grants victim immunity from prosecution for giving.")

add_sec("soc-sec-dowry-08", "soc-dowry", "Dowry Prohibition Act, 1961",
        "Section 8", "Offences Cognizable, Non-Bailable & Non-Compoundable",
        "Offences are cognizable for investigation/arrest, non-bailable, and non-compoundable.",
        "Police can investigate and arrest without warrant; offences cannot be bailed as of right or settled in trial court.",
        ["Cognizable, non-bailable, non-compoundable."],
        ["None."],
        "None", "top-dowry-03-01", "ch-soc-dowry-03", "Dowry Prohibition Act S. 8",
        "Remember all three parameters: cognizable, non-bailable, non-compoundable.")

add_sec("soc-sec-dowry-09", "soc-dowry", "Dowry Prohibition Act, 1961",
        "Section 8A", "Burden of Proof in Certain Cases",
        "Burden of proving that he had not committed the offence under Section 3 or Section 4 lies on the accused person.",
        "Statutory reverse burden: once prosecution shows dowry demand/taking, accused must prove innocence on balance of probabilities.",
        ["Prosecutions under Section 3 (taking) or Section 4 (demanding)."],
        ["Standard on accused is preponderance of probabilities, not beyond reasonable doubt."],
        "None", "top-dowry-03-02", "ch-soc-dowry-03", "Dowry Prohibition Act S. 8A",
        "Compare Section 8A DP Act with Section 113B Evidence Act / Section 118 BSA (dowry death presumption).")

add_sec("soc-sec-dowry-10", "soc-dowry", "Dowry Prohibition Act, 1961",
        "Section 8B", "Dowry Prohibition Officers",
        "State Government appoints Dowry Prohibition Officers with police powers to prevent dowry and collect evidence; assisted by Advisory Board (max 5, min 2 women).",
        "DPOs oversee enforcement, prevent dowry, and collect evidence; supported by a 5-member advisory board with at least 2 women.",
        ["State Government appointment.", "Advisory board: not more than 5 members, at least 2 women."],
        ["None."],
        "None", "top-dowry-03-03", "ch-soc-dowry-03", "Dowry Prohibition Act S. 8B",
        "High-yield: Section 8B(4) advisory board composition: max 5 social workers, min 2 women.")

# ==========================================
# ACT 4: PWDVA 2005 (soc-domestic-violence) - 11 provisions
# ==========================================
add_sec("soc-sec-dv-01", "soc-domestic-violence", "Protection of Women from Domestic Violence Act, 2005",
        "Section 2(a)", "Aggrieved Person",
        "Any woman who is, or has been, in a domestic relationship with the respondent and who alleges to have been subjected to domestic violence.",
        "Covers any woman living or who has lived in a domestic relationship (wives, mothers, sisters, live-in partners, divorcees).",
        ["Woman.", "In domestic relationship currently or in the past."],
        ["Men cannot be aggrieved persons under PWDVA."],
        "None (Definition)", "top-dv-01-01", "ch-soc-dv-01", "PWDVA S. 2(a)",
        "The past tense 'has been' protects divorced women for past violence (Prabha Tyagi).")

add_sec("soc-sec-dv-02", "soc-domestic-violence", "Protection of Women from Domestic Violence Act, 2005",
        "Section 2(f)", "Domestic Relationship",
        "Relationship between two persons who live or have lived together in a shared household through consanguinity, marriage, adoption, or joint family.",
        "Recognizes relationships by blood, marriage, live-in arrangements in the nature of marriage, adoption, or joint family.",
        ["Cohabitation in shared household at any point of time."],
        ["Commercial relationships (tenants, employees) excluded."],
        "None (Definition)", "top-dv-01-02", "ch-soc-dv-01", "PWDVA S. 2(f)",
        "D. Velusamy (2010) established criteria for live-in relationships to qualify under Section 2(f).")

add_sec("soc-sec-dv-03", "soc-domestic-violence", "Protection of Women from Domestic Violence Act, 2005",
        "Section 2(s)", "Shared Household",
        "Household where aggrieved person lives or lived in a domestic relationship; includes joint family property or house of in-laws.",
        "Premises where the woman lived with the family, even if owned exclusively by the father-in-law (overruling S.R. Batra).",
        ["Lived in domestic relationship at any point of time."],
        ["Transitory vacation rentals without domestic nexus excluded."],
        "None (Definition)", "top-dv-01-02", "ch-soc-dv-01", "PWDVA S. 2(s)",
        "Satish Chander Ahuja (2020) landmark ruling: shared household covers in-laws' self-acquired property.")

add_sec("soc-sec-dv-04", "soc-domestic-violence", "Protection of Women from Domestic Violence Act, 2005",
        "Section 3", "Definition of Domestic Violence",
        "Covers physical abuse, sexual abuse, verbal and emotional abuse (insulting for no male child), and economic abuse (depriving of Stridhan/needs).",
        "Four statutory categories: physical, sexual, verbal/emotional, and economic abuse, plus dowry harassment.",
        ["Harm, injury, endangerment to health, safety, life, limb, or well-being."],
        ["None."],
        "Civil reliefs under S. 18-22", "top-dv-01-03", "ch-soc-dv-01", "PWDVA S. 3",
        "Section 3 Explanation I defines all four types; economic abuse includes alienating Stridhan.")

add_sec("soc-sec-dv-05", "soc-domestic-violence", "Protection of Women from Domestic Violence Act, 2005",
        "Section 12", "Application to Magistrate & Timelines",
        "Aggrieved person, Protection Officer, or other person can apply to Magistrate; hearing within 3 days; disposal target within 60 days.",
        "Magistrate fixes first hearing ordinarily within 3 days and endeavors to dispose of petition in 60 days.",
        ["Notice to respondent within 2 days (S. 13).", "60-day disposal target."],
        ["None."],
        "None", "top-dv-02-03", "ch-soc-dv-02", "PWDVA S. 12",
        "Prabha Tyagi (2022) held that an aggrieved woman can apply directly to Magistrate without prior DIR.")

add_sec("soc-sec-dv-06", "soc-domestic-violence", "Protection of Women from Domestic Violence Act, 2005",
        "Section 17", "Right to Reside in a Shared Household",
        "Every woman in a domestic relationship has the right to reside in the shared household, regardless of title; cannot be evicted save by law.",
        "Guarantees woman's roof over her head; husband or in-laws cannot throw her out without a legal court order.",
        ["Domestic relationship.", "Shared household."],
        ["Eviction permitted strictly by due procedure established by law."],
        "Residence order under S. 19", "top-dv-02-02", "ch-soc-dv-02", "PWDVA S. 17",
        "Section 17(1) non-obstante clause overrides property ownership: residence right is independent of title.")

add_sec("soc-sec-dv-07", "soc-domestic-violence", "Protection of Women from Domestic Violence Act, 2005",
        "Section 18", "Protection Orders",
        "Magistrate can restrain respondent from committing domestic violence, entering workplace, communicating, alienating assets, or causing violence.",
        "Restraining orders preventing violence, contact, phone calls, or disposing of assets.",
        ["Prima facie satisfaction that domestic violence has occurred or is likely to occur."],
        ["None."],
        "Breach is penal offence under S. 31", "top-dv-03-01", "ch-soc-dv-03", "PWDVA S. 18",
        "Crucial: Only breach of Section 18 Protection Orders attracts Section 31 jail term.")

add_sec("soc-sec-dv-08", "soc-domestic-violence", "Protection of Women from Domestic Violence Act, 2005",
        "Section 19", "Residence Orders",
        "Restraining dispossession, directing respondent to remove himself from shared household, or providing alternate accommodation.",
        "Court can order respondent to leave the home, or secure alternative rental accommodation of equal standard for the woman.",
        ["Proviso: No order directing any woman to remove herself can be passed."],
        ["Alternative accommodation must be of the same level as enjoyed in shared household."],
        "Contempt / Execution", "top-dv-03-01", "ch-soc-dv-03", "PWDVA S. 19",
        "High-yield: Proviso to Section 19(1) bars ordering female respondents (e.g. mother-in-law) to remove themselves.")

add_sec("soc-sec-dv-09", "soc-domestic-violence", "Protection of Women from Domestic Violence Act, 2005",
        "Section 20", "Monetary Reliefs & Maintenance",
        "Magistrate can direct respondent to pay expenses incurred, loss of earnings, medical expenses, loss of property, and maintenance.",
        "Covers medical bills, property loss, and monthly maintenance for the woman and her children.",
        ["Adequate, fair, and reasonable standard of living consistent with respondent's lifestyle."],
        ["None."],
        "Enforced as criminal fine under S. 421 CrPC / 461 BNSS", "top-dv-03-01", "ch-soc-dv-03", "PWDVA S. 20",
        "Rajnesh v. Neha (2020) mandates asset affidavits and set-off across overlapping maintenance claims.")

add_sec("soc-sec-dv-10", "soc-domestic-violence", "Protection of Women from Domestic Violence Act, 2005",
        "Section 23", "Power to Grant Interim & Ex-Parte Orders",
        "Magistrate may pass interim orders and ex-parte orders on affidavit in prescribed Form III showing prima facie case.",
        "Allows court to issue urgent emergency protection or maintenance orders on day one without waiting for respondent.",
        ["Prima facie satisfaction on affidavit."],
        ["None."],
        "Breach attracts S. 31", "top-dv-02-03", "ch-soc-dv-02", "PWDVA S. 23",
        "Appeals under Section 29 lie against Section 23 interim/ex-parte orders.")

add_sec("soc-sec-dv-11", "soc-domestic-violence", "Protection of Women from Domestic Violence Act, 2005",
        "Section 31", "Penalty for Breach of Protection Order",
        "Breach of protection order or interim protection order is punishable with imprisonment up to one year, or fine up to Rs 20,000, or both.",
        "Violating a court protection order turns a civil PWDVA proceeding into a cognizable, non-bailable criminal crime.",
        ["Breach of Section 18 protection order.", "Offence is cognizable and non-bailable under Section 32."],
        ["Does not apply to default in monetary maintenance payment under Section 20."],
        "Imprisonment up to 1 year or fine up to Rs 20,000 or both", "top-dv-03-03", "ch-soc-dv-03", "PWDVA S. 31",
        "Section 31 is cognizable and non-bailable; tried by the same Magistrate who passed the order.")

# ==========================================
# ACT 5: POSH Act 2013 (soc-posh) - 11 provisions
# ==========================================
add_sec("soc-sec-posh-01", "soc-posh", "Sexual Harassment of Women at Workplace Act, 2013",
        "Section 2(a)", "Aggrieved Woman",
        "A woman of any age, whether employed or not, who alleges to have been subjected to any act of sexual harassment by the respondent.",
        "Covers any woman at a workplace—employees, interns, trainees, clients, visitors, or domestic workers.",
        ["Woman of any age.", "Whether employed or not."],
        ["Men cannot be aggrieved persons under statutory POSH Act."],
        "None (Definition)", "top-posh-01-02", "ch-soc-posh-01", "POSH Act S. 2(a)",
        "Crucial: Woman need NOT be an employee; clients and visitors are protected.")

add_sec("soc-sec-posh-02", "soc-posh", "Sexual Harassment of Women at Workplace Act, 2013",
        "Section 2(n)", "Sexual Harassment",
        "Includes physical contact, demands for sexual favours, sexually coloured remarks, showing pornography, or unwelcome physical/verbal/non-verbal conduct.",
        "Unwelcome sexual conduct in any form—physical, verbal, or visual.",
        ["Unwelcome nature of conduct is decisive."],
        ["Subjective innocent intention is no defense."],
        "Disciplinary action under S. 13", "top-posh-01-03", "ch-soc-posh-01", "POSH Act S. 2(n)",
        "Overlaps with Section 354A IPC / Section 75 BNS.")

add_sec("soc-sec-posh-03", "soc-posh", "Sexual Harassment of Women at Workplace Act, 2013",
        "Section 2(o)", "Workplace & Extended Workplace",
        "Covers government/private offices, hospitals, sports institutes, transport provided by employer, and any place visited arising out of employment.",
        "Workplace includes company cabs, outstation business trips, client sites, and virtual Zoom/WhatsApp meetings.",
        ["Arising out of or during course of employment."],
        ["Includes dwelling places for domestic workers under S. 2(o)(vi)."],
        "None (Definition)", "top-posh-01-02", "ch-soc-posh-01", "POSH Act S. 2(o)",
        "Notional extension of workplace covers remote work, virtual calls, and employer cabs.")

add_sec("soc-sec-posh-04", "soc-posh", "Sexual Harassment of Women at Workplace Act, 2013",
        "Section 3(2)", "Quid Pro Quo & Hostile Work Environment",
        "Promises of preferential treatment or threats of detrimental treatment, or creating an intimidating, offensive or hostile environment amounts to sexual harassment.",
        "Job-for-sex demands or creating a toxic, hostile workplace linked to sexual harassment.",
        ["Connected with act of sexual harassment under S. 2(n)."],
        ["None."],
        "Inquiry under S. 11", "top-posh-01-03", "ch-soc-posh-01", "POSH Act S. 3(2)",
        "Codifies both classic forms: quid pro quo and hostile work environment.")

add_sec("soc-sec-posh-05", "soc-posh", "Sexual Harassment of Women at Workplace Act, 2013",
        "Section 4", "Constitution of Internal Committee (IC)",
        "Mandatory constitution of IC at all workplaces employing 10 or more workers: Presiding Officer (senior woman), min 50% women, external NGO member.",
        "Establishments with 10+ employees must set up an IC headed by a senior woman, with 50% female members and an outside expert.",
        ["10 or more workers.", "Presiding officer must be senior female employee.", "At least 50% women members.", "External member from NGO."],
        ["Workplaces with less than 10 workers go to Local Committee."],
        "Penalty of Rs 50,000 under S. 26", "top-posh-02-01", "ch-soc-posh-02", "POSH Act S. 4",
        "Aureliano Fernandes (2023) issued nationwide directions on strict IC constitution.")

add_sec("soc-sec-posh-06", "soc-posh", "Sexual Harassment of Women at Workplace Act, 2013",
        "Section 6", "Local Committee (LC) at District Level",
        "District Officer constitutes Local Committee in every district to receive complaints from establishments with less than 10 workers or against employers.",
        "District-level committee for small offices, domestic workers, or complaints where the boss himself is the harasser.",
        ["Less than 10 workers or complaint against employer.", "Chairperson must be eminent woman in social work."],
        ["None."],
        "None", "top-posh-02-02", "ch-soc-posh-02", "POSH Act S. 6",
        "District Officer (DM/Collector) constitutes LC and appoints taluka Nodal Officers under S. 6(2).")

add_sec("soc-sec-posh-07", "soc-posh", "Sexual Harassment of Women at Workplace Act, 2013",
        "Section 9", "Complaint of Sexual Harassment & Limitation",
        "Written complaint to IC/LC within three months of incident (or last incident in a series); extendable by max three months for recorded reasons.",
        "Must file complaint within 3 months; IC can extend by another 3 months for written reasons.",
        ["Written complaint.", "3-month limitation.", "Max 3-month extension."],
        ["Where woman cannot make complaint due to physical/mental incapacity, legal heir or co-worker can file."],
        "None", "top-posh-02-03", "ch-soc-posh-02", "POSH Act S. 9",
        "Limitation: 3 months + 3 months max extension.")

add_sec("soc-sec-posh-08", "soc-posh", "Sexual Harassment of Women at Workplace Act, 2013",
        "Section 10", "Conciliation & Ban on Monetary Settlements",
        "IC/LC may facilitate conciliation at request of aggrieved woman before inquiry, but NO monetary settlement shall be made as basis of conciliation.",
        "Mediation allowed only on woman's request, but paying money to settle sexual harassment is strictly illegal.",
        ["Only at request of aggrieved woman.", "Before initiating inquiry."],
        ["No monetary settlement permitted under any circumstance."],
        "Inquiry proceeds if conciliation terms breached", "top-posh-02-03", "ch-soc-posh-02", "POSH Act S. 10",
        "High-yield: Proviso to Section 10(1) expressly prohibits monetary settlements in conciliation.")

add_sec("soc-sec-posh-09", "soc-posh", "Sexual Harassment of Women at Workplace Act, 2013",
        "Section 11", "Inquiry into Complaint & CPC Powers",
        "Inquiry conducted as per service rules; IC/LC has CPC civil court powers for summoning, oaths, and document discovery; target 90 days.",
        "IC functions like a civil court to summon witnesses and documents; must finish inquiry within 90 days; no advocates allowed.",
        ["CPC civil court powers for inquiry.", "Inquiry target is 90 days.", "Rule 7(6) bars legal practitioners."],
        ["None."],
        "Report under S. 13", "top-posh-02-03", "ch-soc-posh-02", "POSH Act S. 11",
        "Section 11(3) confers CPC powers; Rule 7(6) strictly bars advocates.")

add_sec("soc-sec-posh-10", "soc-posh", "Sexual Harassment of Women at Workplace Act, 2013",
        "Section 16", "Prohibition of Publication of Content & RTI Bar",
        "Non-obstante clause overriding RTI Act 2005: strictly prohibits disclosing identity, addresses, or inquiry proceedings to public or media.",
        "Absolute confidentiality: names and details of complainant, respondent, and witnesses cannot be leaked or disclosed under RTI.",
        ["Non-obstante bar overriding Right to Information Act, 2005."],
        ["Section 17 allows disseminating justice outcome without revealing identities."],
        "Penalty under service rules or Rs 5,000 fine under S. 17", "top-posh-03-02", "ch-soc-posh-03", "POSH Act S. 16",
        "Section 16 explicitly overrides the RTI Act 2005; breach carries Rs 5,000 fine under Section 17.")

add_sec("soc-sec-posh-11", "soc-posh", "Sexual Harassment of Women at Workplace Act, 2013",
        "Section 26", "Penalties for Non-Compliance by Employer",
        "Fine up to Rs 50,000 for failing to constitute IC; second conviction attracts twice the penalty and cancellation/revocation of business license.",
        "Companies that fail to set up an IC face a 50k fine, and repeat offenders lose their business/operating license.",
        ["First offence: fine up to Rs 50,000.", "Second/subsequent offence: double fine and cancellation of license/registration."],
        ["None."],
        "Fine Rs 50,000 / Cancellation of business license", "top-posh-03-03", "ch-soc-posh-03", "POSH Act S. 26",
        "Section 26(2) allows cancellation of commercial licenses for repeat defaulters.")

# ==========================================
# ACT 6: PCPNDT Act 1994 (soc-pcpndt) - 11 provisions
# ==========================================
add_sec("soc-sec-pcpndt-01", "soc-pcpndt", "Pre-Conception and Pre-Natal Diagnostic Techniques Act, 1994",
        "Section 2(o)", "Sex Selection",
        "Any procedure, technique, test or administration for purpose of ensuring or increasing probability that embryo will be of a particular sex.",
        "Includes pre-conception sperm sorting, IVF sex selection, or any medical procedure to choose the baby's sex.",
        ["Applies at pre-conception stage as well as post-conception."],
        ["None."],
        "Offence under S. 23", "top-pcpndt-01-02", "ch-soc-pcpndt-01", "PCPNDT Act S. 2(o)",
        "Added by 2002 amendment to cover pre-conception technologies.")

add_sec("soc-sec-pcpndt-02", "soc-pcpndt", "Pre-Conception and Pre-Natal Diagnostic Techniques Act, 1994",
        "Section 4", "Regulation of Pre-Natal Diagnostic Techniques",
        "Techniques permitted strictly for detecting chromosomal abnormalities, genetic diseases, or congenital anomalies; strictly prohibited for sex determination.",
        "Prenatal testing allowed only to detect severe genetic diseases, never to determine the sex of the fetus.",
        ["Maternal age above 35, or history of 2+ miscarriages, or genetic disease exposure.", "Written consent under S. 4(3)."],
        ["Section 4(5) absolute prohibition on sex determination."],
        "Imprisonment up to 3 years under S. 23", "top-pcpndt-01-03", "ch-soc-pcpndt-01", "PCPNDT Act S. 4",
        "Section 4(2) lists qualifying medical indications; Section 4(5) enacts total ban on sex determination.")

add_sec("soc-sec-pcpndt-03", "soc-pcpndt", "Pre-Conception and Pre-Natal Diagnostic Techniques Act, 1994",
        "Section 5(2)", "Prohibition on Communicating Sex of Fetus",
        "No person shall communicate in any manner the sex of the foetus to pregnant woman or relatives by words, signs or in any other manner.",
        "Absolute ban on telling parents or relatives the baby's sex through words, hints, gestures, or coded symbols.",
        ["Absolute prohibition across all medical and non-medical persons."],
        ["None."],
        "Imprisonment up to 3 years and fine under S. 23", "top-pcpndt-02-01", "ch-soc-pcpndt-02", "PCPNDT Act S. 5(2)",
        "Crucial: 'by words, signs or in any other manner' covers all coded hints and gestures.")

add_sec("soc-sec-pcpndt-04", "soc-pcpndt", "Pre-Conception and Pre-Natal Diagnostic Techniques Act, 1994",
        "Section 6", "Absolute Prohibition of Sex Selection",
        "No clinic, laboratory, or person shall conduct or cause to be conducted sex selection on a human being including pre-conception.",
        "Total ban on sex selection before or after conception; aiding and abetting is also a crime.",
        ["Applies universally across all clinics and facilities."],
        ["None."],
        "Imprisonment under S. 23", "top-pcpndt-02-01", "ch-soc-pcpndt-02", "PCPNDT Act S. 6",
        "Section 6(a) bans pre-conception sex selection; Section 6(b) bans aiding and abetting.")

add_sec("soc-sec-pcpndt-05", "soc-pcpndt", "Pre-Conception and Pre-Natal Diagnostic Techniques Act, 1994",
        "Section 17", "Appropriate Authority & Multi-Member Body",
        "State Government appoints Appropriate Authority; multi-member body at State level (senior health officer, woman social worker, legal officer).",
        "Regulatory enforcement body that grants/cancels registrations and conducts raids and searches.",
        ["3-member body at State level under S. 17(3).", "District Appropriate Authority is usually Chief Medical Officer."],
        ["None."],
        "None", "top-pcpndt-03-01", "ch-soc-pcpndt-03", "PCPNDT Act S. 17",
        "Multi-member body under Section 17(3) prevents unilateral arbitrary decisions.")

add_sec("soc-sec-pcpndt-06", "soc-pcpndt", "Pre-Conception and Pre-Natal Diagnostic Techniques Act, 1994",
        "Section 18", "Mandatory Registration of Clinics",
        "No ultrasound clinic, genetic counselling centre, or genetic clinic can operate without prior registration; certificate valid for 5 years.",
        "Every ultrasound machine and scan centre must be registered; certificate must be displayed publicly; valid for 5 years.",
        ["Prior registration mandatory before commencing operations.", "Valid for 5 years under S. 19(4)."],
        ["None."],
        "Seizure of machine under S. 30 / Punishment under S. 23", "top-pcpndt-02-02", "ch-soc-pcpndt-02", "PCPNDT Act S. 18",
        "Operating an unregistered ultrasound machine is a serious criminal offence.")

add_sec("soc-sec-pcpndt-07", "soc-pcpndt", "Pre-Conception and Pre-Natal Diagnostic Techniques Act, 1994",
        "Section 20", "Suspension & Cancellation of Registration",
        "Appropriate Authority can suspend or cancel registration after show cause notice; can suspend immediately without notice in public interest under S. 20(3).",
        "Authority can revoke clinic license for violations after notice, or suspend immediately in public interest.",
        ["Show cause notice and hearing under S. 20(1)-(2).", "Emergency suspension without notice under S. 20(3) for written reasons."],
        ["None."],
        "Closure of clinic", "top-pcpndt-02-02", "ch-soc-pcpndt-02", "PCPNDT Act S. 20",
        "Section 20(3) emergency suspension power is frequently tested.")

add_sec("soc-sec-pcpndt-08", "soc-pcpndt", "Pre-Conception and Pre-Natal Diagnostic Techniques Act, 1994",
        "Section 22", "Prohibition on Advertisements",
        "Bans advertising sex selection or sex determination in any form (print, electronic, internet); punishable with up to 3 years jail and Rs 10,000 fine.",
        "Total ban on advertising sex determination; Supreme Court in Sabu Mathew George ordered search engines to auto-block keyword ads.",
        ["All media formats covered."],
        ["None."],
        "Imprisonment up to 3 years and fine up to Rs 10,000", "top-pcpndt-02-01", "ch-soc-pcpndt-02", "PCPNDT Act S. 22",
        "Sabu Mathew George (2017) auto-block doctrine applies to Section 22.")

add_sec("soc-sec-pcpndt-09", "soc-pcpndt", "Pre-Conception and Pre-Natal Diagnostic Techniques Act, 1994",
        "Section 23", "Penalties for Medical Personnel & Owners",
        "First offence: up to 3 years imprisonment and fine up to Rs 10,000; subsequent offence: up to 5 years and fine up to Rs 50,000; license suspended/removed.",
        "Doctors face up to 3 years jail on first conviction (5 years on repeat), plus medical license suspension during trial and cancellation upon conviction.",
        ["Applies to medical geneticists, gynecologists, radiologists, and clinic owners."],
        ["None."],
        "Imprisonment 3y/5y, fine Rs 10k/50k, removal of medical license", "top-pcpndt-03-03", "ch-soc-pcpndt-03", "PCPNDT Act S. 23",
        "FOGSI (2019) upheld strict liability under Section 23; incomplete Form F attracts Section 23.")

add_sec("soc-sec-pcpndt-10", "soc-pcpndt", "Pre-Conception and Pre-Natal Diagnostic Techniques Act, 1994",
        "Section 24", "Presumption of Compulsion on Pregnant Woman",
        "Court shall presume that the pregnant woman was compelled by her husband or relatives to undergo sex determination; shields her from liability.",
        "Law presumes the pregnant mother was forced by family; husband and relatives are prosecuted while woman is protected as victim.",
        ["Applies in prosecutions for undergoing sex determination."],
        ["Presumption is in favor of the woman, against husband/relatives."],
        "Husband/relatives prosecuted under S. 23(3)", "top-pcpndt-03-03", "ch-soc-pcpndt-03", "PCPNDT Act S. 24",
        "Section 24 creates a protective presumption shielding the pregnant woman.")

add_sec("soc-sec-pcpndt-11", "soc-pcpndt", "Pre-Conception and Pre-Natal Diagnostic Techniques Act, 1994",
        "Section 28", "Cognizance on Complaint Only",
        "Court can take cognizance ONLY on complaint by Appropriate Authority or person who gave 15 days notice; police cannot file chargesheet directly.",
        "Trial court can only act on a complaint by the health authority or citizen giving 15 days notice; direct police FIR chargesheets are barred.",
        ["Complaint by Appropriate Authority or authorized officer.", "Private complaint requires 15-day prior notice under S. 28(1)(b)."],
        ["No court inferior to Metropolitan Magistrate or JMFC."],
        "None", "top-pcpndt-03-02", "ch-soc-pcpndt-03", "PCPNDT Act S. 28",
        "High-yield: Police cannot file a direct chargesheet under CrPC 173; Section 28 requires statutory complaint.")

# ==========================================
# ACT 7: MTP Act 1971 (soc-mtp) - 10 provisions
# ==========================================
add_sec("soc-sec-mtp-01", "soc-mtp", "Medical Termination of Pregnancy Act, 1971",
        "Section 2(d)", "Registered Medical Practitioner",
        "Medical practitioner possessing recognized medical qualification under NMC Act, registered in State Medical Register, with prescribed obstetric training/experience.",
        "Only allopathic doctors with NMC credentials and gynecological/obstetric training can lawfully terminate pregnancy.",
        ["NMC qualification.", "State Medical Register entry.", "Prescribed obstetric experience under Rule 4."],
        ["AYUSH / non-allopathic practitioners strictly excluded."],
        "Unqualified termination is penal under S. 5(2)", "top-mtp-01-02", "ch-soc-mtp-01", "MTP Act S. 2(d)",
        "Termination by non-RMP is punishable with 2 to 7 years rigorous imprisonment under Section 5(2).")

add_sec("soc-sec-mtp-02", "soc-mtp", "Medical Termination of Pregnancy Act, 1971",
        "Section 3(2)(a)", "Termination Up to 20 Weeks",
        "Pregnancy may be terminated up to twenty weeks on the opinion of ONE registered medical practitioner formed in good faith.",
        "Abortion up to 20 weeks requires the opinion of just one qualified doctor.",
        ["Gestational age up to 20 weeks.", "Opinion of one RMP formed in good faith.", "Maternal health risk or contraceptive failure."],
        ["None."],
        "None", "top-mtp-02-01", "ch-soc-mtp-02", "MTP Act S. 3(2)(a)",
        "2021 amendment simplified up to 20 weeks to a single doctor's opinion (previously 2 doctors for 12-20 weeks).")

add_sec("soc-sec-mtp-03", "soc-mtp", "Medical Termination of Pregnancy Act, 1971",
        "Section 3(2)(b)", "Termination Between 20 and 24 Weeks",
        "Pregnancy between 20 and 24 weeks may be terminated on opinion of TWO registered medical practitioners for eligible categories under Rule 3B.",
        "Abortion between 20-24 weeks requires 2 doctors' opinions and woman must belong to an eligible vulnerable group (rape, minors, disability, etc.).",
        ["Gestational age between 20 and 24 weeks.", "Opinion of not less than two RMPs.", "Woman falls under Rule 3B categories."],
        ["Unmarried women are fully eligible (X v. Principal Secretary 2022)."],
        "None", "top-mtp-02-01", "ch-soc-mtp-02", "MTP Act S. 3(2)(b)",
        "Rule 3B categories: rape survivors, incest, minors, disabled women, change of marital status, disaster survivors.")

add_sec("soc-sec-mtp-04", "soc-mtp", "Medical Termination of Pregnancy Act, 1971",
        "Section 3(2) Expl. 1", "Contraceptive Failure Ground (Any Woman or Partner)",
        "Pregnancy caused by failure of device/method used by ANY WOMAN OR HER PARTNER to limit children is presumed to cause grave mental injury.",
        "Unintended pregnancy due to contraceptive failure is legal ground for abortion for married as well as unmarried women.",
        ["Failure of contraceptive device or method.", "Applies to 'any woman or her partner'."],
        ["None."],
        "None", "top-mtp-01-03", "ch-soc-mtp-01", "MTP Act S. 3(2) Expl. 1",
        "2021 amendment replaced 'married woman or her husband' with 'woman or her partner'. X v. Principal Secretary affirmed equality.")

add_sec("soc-sec-mtp-05", "soc-mtp", "Medical Termination of Pregnancy Act, 1971",
        "Section 3(2B)", "Termination Beyond 24 Weeks for Substantial Fetal Abnormalities",
        "The 24-week gestational ceiling shall NOT apply where termination is necessitated by substantial foetal abnormalities diagnosed by a Medical Board.",
        "No gestational time limit applies if a State Medical Board certifies substantial fetal abnormalities.",
        ["Diagnosis of substantial fetal abnormality by 4-member State Medical Board."],
        ["Does not require court approval."],
        "None", "top-mtp-02-03", "ch-soc-mtp-02", "MTP Act S. 3(2B)",
        "Section 3(2B) completely removes the 24-week cap for severe fetal abnormalities.")

add_sec("soc-sec-mtp-06", "soc-mtp", "Medical Termination of Pregnancy Act, 1971",
        "Section 3(4)", "Consent of Pregnant Woman",
        "Sole consent of adult woman of sound mind required; written consent of guardian required only for minors (under 18) or mentally ill persons.",
        "An adult woman makes her own decision; NO spousal, husband, or in-law consent is needed or allowed to veto her choice.",
        ["Adult woman: sole consent.", "Minor (below 18) or mentally ill: guardian's written consent."],
        ["Husband's consent is completely irrelevant under Indian law."],
        "Termination without woman's consent is penal offence under IPC 313 / BNS 89", "top-mtp-03-01", "ch-soc-mtp-03", "MTP Act S. 3(4)",
        "Frequently tested: husband's consent is NOT required. Sole consent of adult woman governs.")

add_sec("soc-sec-mtp-07", "soc-mtp", "Medical Termination of Pregnancy Act, 1971",
        "Section 4", "Approved Places for Termination",
        "Termination permitted only in government hospitals or private places approved by Government or District-level Committee.",
        "Abortion can only be performed in government hospitals or clinics approved by the CMO-led committee.",
        ["Government hospital or approved clinic.", "Approved place must have resuscitation, suction, and emergency equipment."],
        ["Section 5(1) emergency exception waives place requirement to save life."],
        "Imprisonment 2 to 7 years under S. 5(3)", "top-mtp-03-01", "ch-soc-mtp-03", "MTP Act S. 4",
        "Conducting MTP at unapproved places carries 2 to 7 years rigorous imprisonment under Section 5(3).")

add_sec("soc-sec-mtp-08", "soc-mtp", "Medical Termination of Pregnancy Act, 1971",
        "Section 5(1)", "Emergency Exception to Save Pregnant Woman's Life",
        "Sections 3(2) gestational limits and Section 4 place restrictions do NOT apply where termination is immediately necessary to save the woman's life.",
        "In a life-threatening emergency, any single doctor can terminate pregnancy at any place and at any gestational stage.",
        ["Immediate necessity to save the life of the pregnant woman.", "Single RMP acting in good faith."],
        ["Overrides all gestational limits and place restrictions."],
        "None", "top-mtp-02-03", "ch-soc-mtp-02", "MTP Act S. 5(1)",
        "Section 5(1) is the ultimate life-saving emergency exception overriding Sections 3 and 4.")

add_sec("soc-sec-mtp-09", "soc-mtp", "Medical Termination of Pregnancy Act, 1971",
        "Section 5A", "Protection of Privacy & Confidentiality",
        "Prohibits revealing name and particulars of a woman whose pregnancy has been terminated, except to a person authorized by law.",
        "Strict confidentiality: doctor or clinic revealing a patient's abortion details faces up to 1 year jail or fine or both.",
        ["Strict statutory confidentiality.", "Disclosure permitted only to authorized persons under law."],
        ["None."],
        "Imprisonment up to 1 year or fine or both", "top-mtp-03-02", "ch-soc-mtp-03", "MTP Act S. 5A",
        "Inserted by 2021 amendment: breach of privacy is punishable with up to 1 year imprisonment under S. 5A(2).")

add_sec("soc-sec-mtp-10", "soc-mtp", "Medical Termination of Pregnancy Act, 1971",
        "Section 5(2) & 5(3)", "Penalties for Unqualified Persons & Unapproved Places",
        "Termination by non-RMP is punishable with 2 to 7 years RI under IPC/BNS; termination at unapproved place carries 2 to 7 years RI.",
        "Quacks performing abortions or approved doctors operating in unapproved clinics face mandatory 2 to 7 years in prison.",
        ["Rigorous imprisonment of 2 to 7 years."],
        ["None."],
        "Rigorous imprisonment 2 to 7 years", "top-mtp-03-03", "ch-soc-mtp-03", "MTP Act S. 5(2), (3)",
        "Both offences carry mandatory 2 to 7 years rigorous imprisonment.")

# ==========================================
# ACT 8: IRWA 1986 (soc-indecent-rep) - 9 provisions
# ==========================================
add_sec("soc-sec-irwa-01", "soc-indecent-rep", "Indecent Representation of Women (Prohibition) Act, 1986",
        "Section 2(c)", "Indecent Representation of Women",
        "Depicting a woman's form or body in such a way as to be indecent, derogatory, denigrating, or corrupting public morality.",
        "Portraying women in an indecent, vulgar, or degrading manner that depraves morals or insults female dignity.",
        ["Three tests: (1) indecent, (2) derogatory/denigrating, or (3) depraving/corrupting public morals."],
        ["Scientific, literary, or ancient heritage art exempt under Section 4 proviso."],
        "Section 6 penalties", "top-irwa-01-03", "ch-soc-irwa-01", "IRWA S. 2(c)",
        "Aveek Sarkar (2014) established contemporary community standards test.")

add_sec("soc-sec-irwa-02", "soc-indecent-rep", "Indecent Representation of Women (Prohibition) Act, 1986",
        "Section 3", "Prohibition of Indecent Advertisements",
        "No person shall publish, cause to be published, arrange, or exhibit any advertisement containing indecent representation of women.",
        "Total ban on indecent ads in newspapers, billboards, posters, or digital media; advertisers, agencies, and publishers all liable.",
        ["Publishing, arranging, or exhibiting in any form."],
        ["None."],
        "Section 6 penalties", "top-irwa-02-01", "ch-soc-irwa-02", "IRWA S. 3",
        "Holds the entire advertising chain liable including media agencies arranging display.")

add_sec("soc-sec-irwa-03", "soc-indecent-rep", "Indecent Representation of Women (Prohibition) Act, 1986",
        "Section 4", "Prohibition of Publications & Distribution",
        "Prohibits producing, selling, hiring, distributing, circulating, or sending by post any book, paper, slide, film, drawing, or painting containing indecent depiction.",
        "Commercial sale, distribution, hire, or mailing of indecent books, magazines, posters, or photos is criminalized.",
        ["Production, sale, letting to hire, distribution, circulation, posting."],
        ["Statutory exceptions under Section 4 proviso."],
        "Section 6 penalties", "top-irwa-02-02", "ch-soc-irwa-02", "IRWA S. 4",
        "Targets commercial distribution, sale, hire, and postal circulation.")

add_sec("soc-sec-irwa-04", "soc-indecent-rep", "Indecent Representation of Women (Prohibition) Act, 1986",
        "Section 4 Proviso (a)", "Public Good & Science/Art Exception",
        "Exempts publications justified for public good in the interest of science, literature, art, learning, or objects of general concern.",
        "Medical textbooks, serious literature, and bona fide art galleries are protected from prosecution.",
        ["Public good justification.", "Science, literature, art, or learning."],
        ["None."],
        "Exempt from prosecution", "top-irwa-02-03", "ch-soc-irwa-02", "IRWA S. 4 Proviso (a)",
        "Mirrors Section 292 IPC exception for science, literature, and art.")

add_sec("soc-sec-irwa-05", "soc-indecent-rep", "Indecent Representation of Women (Prohibition) Act, 1986",
        "Section 4 Proviso (b)", "Religious Sculptures & Ancient Monuments Exception",
        "Exempts representations kept/used for religious purposes, temple carvings, idol conveyances, and ancient monuments (1958 Act), plus certified films.",
        "Protects ancient temple carvings (Khajuraho, Konark), religious idols, and movies certified by CBFC censor board.",
        ["Temple sculptures, religious idol cars, ancient monuments under 1958 Act.", "Films certified under Cinematograph Act 1952."],
        ["None."],
        "Exempt from prosecution", "top-irwa-02-03", "ch-soc-irwa-02", "IRWA S. 4 Proviso (b)",
        "Crucial: Films certified under Cinematograph Act 1952 are expressly exempt.")

add_sec("soc-sec-irwa-06", "soc-indecent-rep", "Indecent Representation of Women (Prohibition) Act, 1986",
        "Section 5", "Powers of Entry, Search & Seizure",
        "Authorized Gazetted Officer may enter and search places, seize offending materials; search of private dwelling house strictly requires a warrant.",
        "Gazetted officer can raid and seize offending posters or publications, but CANNOT enter a private residence without a magistrate's search warrant.",
        ["Gazetted Officer authorized by State Government.", "Private dwelling house requires search warrant under S. 5(1) proviso.", "CrPC search rules apply."],
        ["None."],
        "None", "top-irwa-03-01", "ch-soc-irwa-03", "IRWA S. 5",
        "High-yield: Proviso to Section 5(1) strictly requires a warrant for entering private dwelling houses.")

add_sec("soc-sec-irwa-07", "soc-indecent-rep", "Indecent Representation of Women (Prohibition) Act, 1986",
        "Section 6", "Penalties for Offences",
        "First conviction: up to 2 years imprisonment and fine up to Rs 2,000; second/subsequent: not less than 6 months up to 5 years and fine Rs 10,000 to Rs 1,00,000.",
        "First offence carries up to 2 years jail and Rs 2,000 fine; repeat offence carries minimum 6 months to 5 years jail and Rs 10k-1L fine.",
        ["First offence: up to 2 years, fine up to Rs 2,000.", "Subsequent: min 6 months to 5 years, fine Rs 10,000 to Rs 1,00,000."],
        ["None."],
        "Jail 2y/5y, fine Rs 2k / Rs 10k-1L", "top-irwa-03-03", "ch-soc-irwa-03", "IRWA S. 6",
        "Memorize tiers: 2y/2k (first) vs 6m-5y/10k-1L (repeat).")

add_sec("soc-sec-irwa-08", "soc-indecent-rep", "Indecent Representation of Women (Prohibition) Act, 1986",
        "Section 7", "Offences by Companies",
        "Company and persons in charge and responsible for conduct of business are deemed guilty; individual officers liable for consent or connivance.",
        "Corporate liability: directors and managers in charge are prosecuted alongside the publishing company.",
        ["Company and persons in charge.", "Defense: lack of knowledge or due diligence under S. 7(1) proviso."],
        ["Partnership firm partners are directors under Explanation."],
        "Section 6 penalties", "top-irwa-03-02", "ch-soc-irwa-03", "IRWA S. 7",
        "Standard vicarious corporate liability clause with due diligence defense.")

add_sec("soc-sec-irwa-09", "soc-indecent-rep", "Indecent Representation of Women (Prohibition) Act, 1986",
        "Section 8", "Classification of Offences (Cognizable & Bailable)",
        "Offences punishable under this Act are explicitly declared BAILABLE under Section 8(1) and COGNIZABLE under Section 8(2).",
        "Police can investigate and arrest without warrant (cognizable), but accused is entitled to bail as a matter of right (bailable).",
        ["Cognizable under S. 8(2).", "Bailable under S. 8(1)."],
        ["None."],
        "None", "top-irwa-03-03", "ch-soc-irwa-03", "IRWA S. 8",
        "Frequently tested UP PCS-J trap: IRWA offences are COGNIZABLE and BAILABLE.")

# ==========================================
# ACT 9: POCSO Act 2012 (soc-pocso) - 12 provisions
# ==========================================
add_sec("soc-sec-pocso-01", "soc-pocso", "Protection of Children from Sexual Offences Act, 2012",
        "Section 2(1)(d)", "Definition of Child",
        "Any person below the age of eighteen years; gender-neutral definition protecting all boys, girls, and transgender children.",
        "Anyone under 18 is legally a child; their consent to sexual acts is legally void and immaterial.",
        ["Below 18 years of age.", "Gender-neutral."],
        ["None."],
        "None (Definition)", "top-pocso-01-02", "ch-soc-pocso-01", "POCSO Act S. 2(1)(d)",
        "Gender-neutral victim status; consent below 18 is completely void.")

add_sec("soc-sec-pocso-02", "soc-pocso", "Protection of Children from Sexual Offences Act, 2012",
        "Section 3 & 4", "Penetrative Sexual Assault & Punishment",
        "Penetration of penis, object, or body part into vagina, mouth, urethra, or anus; punished with not less than 10 years up to life imprisonment and fine.",
        "Penetrative sexual assault carries a mandatory minimum 10-year prison sentence, extending up to life imprisonment.",
        ["Penetration of sexual orifices with body part or object.", "Mandatory minimum 10 years imprisonment post-2019."],
        ["None."],
        "Rigorous imprisonment not less than 10 years up to life, and fine", "top-pocso-02-01", "ch-soc-pocso-02", "POCSO Act S. 3, 4",
        "2019 amendment raised minimum punishment from 7 years to 10 years.")

add_sec("soc-sec-pocso-03", "soc-pocso", "Protection of Children from Sexual Offences Act, 2012",
        "Section 5 & 6", "Aggravated Penetrative Sexual Assault & Punishment",
        "Assault by police, teacher, doctor, family member, gang assault, or on child under 12; punished with 20 years to life/death penalty and fine.",
        "Assault by trusted authorities or on child under 12 carries minimum 20 years prison up to life imprisonment or the death penalty.",
        ["Positions of trust/authority, child under 12, gang assault, HIV transmission, grievous hurt."],
        ["Death penalty introduced by 2019 amendment."],
        "Rigorous imprisonment 20 years to natural life or death, and fine", "top-pocso-02-01", "ch-soc-pocso-02", "POCSO Act S. 5, 6",
        "Section 6 provides for capital punishment or minimum 20 years to remainder of natural life.")

add_sec("soc-sec-pocso-04", "soc-pocso", "Protection of Children from Sexual Offences Act, 2012",
        "Section 7 & 8", "Sexual Assault & Punishment",
        "Touching sexual organs or physical contact with sexual intent without penetration; punished with not less than 3 years up to 5 years and fine.",
        "Touching sexual parts with sexual intent (even over clothes) carries 3 to 5 years in prison.",
        ["Sexual intent.", "Physical contact without penetration.", "Skin-to-skin contact NOT required (AG v. Satish)."],
        ["None."],
        "Imprisonment not less than 3 years up to 5 years, and fine", "top-pocso-02-02", "ch-soc-pocso-02", "POCSO Act S. 7, 8",
        "Supreme Court in AG v. Satish (2022) overruled Bombay HC 'skin-to-skin' ruling; touching over clothes is sexual assault.")

add_sec("soc-sec-pocso-05", "soc-pocso", "Protection of Children from Sexual Offences Act, 2012",
        "Section 9 & 10", "Aggravated Sexual Assault & Punishment",
        "Sexual assault without penetration committed by police, teachers, doctors, relatives, or in schools/institutions; punished with 5 to 7 years and fine.",
        "Abuse of trust or authority in non-penetrative assault raises punishment to minimum 5 years up to 7 years in prison.",
        ["Aggravating factors under Section 9."],
        ["None."],
        "Imprisonment not less than 5 years up to 7 years, and fine", "top-pocso-02-02", "ch-soc-pocso-02", "POCSO Act S. 9, 10",
        "Minimum sentence is 5 years; maximum is 7 years plus fine.")

add_sec("soc-sec-pocso-06", "soc-pocso", "Protection of Children from Sexual Offences Act, 2012",
        "Section 11 & 12", "Sexual Harassment of Child & Punishment",
        "Words, gestures, sounds, showing pornography, or repeated stalking with sexual intent; punished with imprisonment up to 3 years and fine.",
        "Sexually coloured comments, gestures, flashing, or stalking a child carries up to 3 years in prison and fine.",
        ["Sexual intent.", "Verbal, gestural, or electronic stalking/harassment."],
        ["None."],
        "Imprisonment up to 3 years and fine", "top-pocso-02-03", "ch-soc-pocso-02", "POCSO Act S. 11, 12",
        "Non-contact verbal/gestural harassment is punishable with up to 3 years imprisonment.")

add_sec("soc-sec-pocso-07", "soc-pocso", "Protection of Children from Sexual Offences Act, 2012",
        "Section 15", "Storage & Retention of Child Pornography",
        "Penalizes storing or possessing child pornography unless reported or deleted; commercial storage carries 3 to 5 years and fine.",
        "Possessing child pornography on phone or PC without reporting is illegal; commercial storage carries 3 to 5 years prison.",
        ["Possession/storage.", "Duty to delete or report to SJPU/police under S. 15(1)."],
        ["Commercial storage punished under S. 15(2)."],
        "Fine Rs 1,000 (first) / Rs 5,000 (subsequent); Commercial: 3 to 5 years", "top-pocso-02-03", "ch-soc-pocso-02", "POCSO Act S. 15",
        "Substituted by 2019 amendment; penalizes retaining/transmitting child pornography.")

add_sec("soc-sec-pocso-08", "soc-pocso", "Protection of Children from Sexual Offences Act, 2012",
        "Section 19 & 21", "Mandatory Reporting & Penalties for Failure",
        "Mandatory civic duty on any person and institution head to report suspected offences; failure carries up to 6 months jail (1 year for institution head).",
        "Anyone who knows of child abuse must inform police; failure to report carries 6 months jail; school/hospital heads face 1 year jail.",
        ["Universal reporting duty under S. 19(1).", "Specific duty on institution heads under S. 19(2)."],
        ["None."],
        "Imprisonment up to 6 months or fine (general) / up to 1 year and fine (institution heads)", "top-pocso-03-01", "ch-soc-pocso-03", "POCSO Act S. 19, 21",
        "Mandatory reporting overrides doctor-patient or school-student confidentiality; Section 21 punishes failure to report.")

add_sec("soc-sec-pocso-09", "soc-pocso", "Protection of Children from Sexual Offences Act, 2012",
        "Section 24", "Recording Child's Statement by Police",
        "Recorded at child's residence by woman police officer not below SI; officer shall NOT wear uniform; child shall NOT be detained at police station overnight.",
        "Woman officer in plain clothes records child's statement at home; child cannot be kept at police station at night under any circumstance.",
        ["Woman officer not below Sub-Inspector.", "Plain clothes (no uniform).", "No overnight police station detention."],
        ["None."],
        "Departmental action / Section 21", "top-pocso-03-02", "ch-soc-pocso-03", "POCSO Act S. 24",
        "Strict procedural protections: plainclothes woman SI and absolute bar on overnight detention.")

add_sec("soc-sec-pocso-10", "soc-pocso", "Protection of Children from Sexual Offences Act, 2012",
        "Section 28 & 33", "Special Courts & Direct Cognizance",
        "Court of Session designated as Special Court in each district; direct cognizance without committal under CrPC; child not exposed to accused.",
        "Special Sessions Court tries cases directly without magistrate committal, in camera, with screen preventing child seeing the accused.",
        ["Court of Session.", "Direct cognizance under S. 33(1).", "Protective screens under S. 33(4).", "In-camera trial under S. 37."],
        ["None."],
        "None", "top-pocso-04-01", "ch-soc-pocso-04", "POCSO Act S. 28, 33",
        "Special Court takes direct cognizance without committal; questions put through the court (S. 33(2)).")

add_sec("soc-sec-pocso-11", "soc-pocso", "Protection of Children from Sexual Offences Act, 2012",
        "Section 29 & 30", "Statutory Presumptions of Guilt & Mens Rea",
        "Special Court shall presume that accused committed offence under S. 3, 5, 7, 9 once foundational facts proved; presumes culpable mental state under S. 30.",
        "Reverse burden: once prosecution proves basic incident, court presumes accused is guilty unless accused proves innocence.",
        ["Prosecution must first prove foundational facts.", "Statutory presumption of guilt under S. 29.", "Presumption of mens rea under S. 30."],
        ["Accused can rebut on preponderance of probabilities."],
        "None", "top-pocso-04-03", "ch-soc-pocso-04", "POCSO Act S. 29, 30",
        "Foundational facts must be established before Section 29 presumption triggers.")

add_sec("soc-sec-pocso-12", "soc-pocso", "Protection of Children from Sexual Offences Act, 2012",
        "Section 35", "Trial Timelines (30 Days & 1 Year)",
        "Evidence of child recorded within thirty days of cognizance; entire trial completed, as far as possible, within one year from taking cognizance.",
        "Child's testimony must be recorded within 30 days; entire trial must be completed within 1 year.",
        ["Child evidence within 30 days of cognizance.", "Trial completion target within 1 year of cognizance."],
        ["None."],
        "None", "top-pocso-04-02", "ch-soc-pocso-04", "POCSO Act S. 35",
        "High-yield statutory timelines: 30 days for recording child's evidence, 1 year for trial completion.")

# Save to assets/learning/data/social/social-sections-explorer.js
output_path = os.path.join("assets", "learning", "data", "social", "social-sections-explorer.js")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

header = """/**
 * Tanveer Ashraf Judicial Prep 2026–27
 * Social Legislation High-Yield Section-Explorer
 *
 * Curated statutory explorer covering 98 high-yield provisions across all 9 Acts:
 * 1. Rights of Persons with Disabilities Act, 2016 (12 provisions)
 * 2. Maintenance and Welfare of Parents and Senior Citizens Act, 2007 (12 provisions)
 * 3. Dowry Prohibition Act, 1961 (10 provisions)
 * 4. Protection of Women from Domestic Violence Act, 2005 (11 provisions)
 * 5. Sexual Harassment of Women at Workplace Act, 2013 (11 provisions)
 * 6. Pre-Conception and Pre-Natal Diagnostic Techniques Act, 1994 (11 provisions)
 * 7. Medical Termination of Pregnancy Act, 1971 (10 provisions)
 * 8. Indecent Representation of Women (Prohibition) Act, 1986 (9 provisions)
 * 9. Protection of Children from Sexual Offences Act, 2012 (12 provisions)
 *
 * Total: Exactly 98 Curated Statutory Entries with UP Exam Tips
 */

(function(global) {
    'use strict';

    const SOCIAL_SECTIONS_EXPLORER = """

footer = """;

    if (typeof module !== 'undefined' && module.exports) {
        module.exports = SOCIAL_SECTIONS_EXPLORER;
    }
    global.SOCIAL_SECTIONS_EXPLORER = SOCIAL_SECTIONS_EXPLORER;
})(typeof window !== 'undefined' ? window : global);
"""

with open(output_path, "w", encoding="utf-8") as f:
    f.write(header + json.dumps(entries, indent=2, ensure_ascii=False) + footer)

print(f"SUCCESS: Created {output_path} with {len(entries)} statutory entries!")
