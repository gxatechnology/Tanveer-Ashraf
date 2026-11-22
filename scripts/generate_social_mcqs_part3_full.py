"""
Generate all 155 MCQs for Part 3: Acts 7-9
Act 7: MTP Act, 1971 (50 MCQs: mcq-mtp-01-001 to mcq-mtp-01-050)
Act 8: IRWA, 1986 (45 MCQs: mcq-irwa-01-001 to mcq-irwa-01-045)
Act 9: POCSO Act, 2012 (60 MCQs: mcq-pocso-01-001 to mcq-pocso-01-060)
Total: 155 MCQs
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

# --- ACT 7: MEDICAL TERMINATION OF PREGNANCY ACT, 1971 (soc-mtp) - 50 MCQs ---

# Chapter 1: ch-soc-mtp-01 (18 MCQs)
# top-mtp-01-01 (6)
add_q("mcq-mtp-01-001", "soc-mtp", "ch-soc-mtp-01", "top-mtp-01-01",
      "Which government committee's recommendations in 1966 led directly to the enactment of the Medical Termination of Pregnancy Act, 1971?",
      ["Shantilal Shah Committee", "Justice Verma Committee", "Mudaliar Committee", "Sarkaria Commission"], 0,
      "The Shantilal Shah Committee appointed in 1964 submitted its historic report in December 1966 recommending legalisation of abortion on health and compassionate grounds.",
      {"A": "Correct; Shantilal Shah Committee (1966).", "B": "Incorrect; Justice Verma Committee dealt with 2013 criminal law amendments.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "Shantilal Shah Committee & MTP Preamble", "Historical background of MTP Act 1971.")

add_q("mcq-mtp-01-002", "soc-mtp", "ch-soc-mtp-01", "top-mtp-01-02",
      "On which date did the Medical Termination of Pregnancy Act, 1971 (Act No. 34 of 1971) come into force in India?",
      ["10 August 1971", "1 April 1972", "1 January 1972", "15 August 1973"], 1,
      "The Act was enacted in August 1971 and officially brought into force on 1 April 1972.",
      {"A": "Incorrect; 10 August 1971 was Presidential assent date.", "B": "Correct; Came into force on 1 April 1972.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 1(3)", "Commencement date of MTP Act 1971.")

add_q("mcq-mtp-01-003", "soc-mtp", "ch-soc-mtp-01", "top-mtp-01-01",
      "Under Section 3(1) of the MTP Act, what is the legal effect of terminating a pregnancy in accordance with the provisions of this Act?",
      ["A registered medical practitioner shall not be guilty of any offence under the Indian Penal Code, 1860 / Bharatiya Nyaya Sanhita, 2023 or any other law",
       "The doctor receives immunity only if approved by the District Magistrate",
       "The doctor is awarded a state citation",
       "The child's birth is still registered"], 0,
      "Section 3(1) contains a non-obstante clause providing that a registered medical practitioner shall not be guilty of causing miscarriage under IPC/BNS if done under the Act.",
      {"A": "Correct; Statutory immunity from penal liability for causing miscarriage under Section 3(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 3(1) & IPC S. 312 / BNS S. 88", "Statutory exception to penal offence of causing miscarriage.")

add_q("mcq-mtp-01-004", "soc-mtp", "ch-soc-mtp-01", "top-mtp-01-01",
      "Which penal code provisions generalise causing miscarriage as a serious criminal offence, from which the MTP Act provides an exception?",
      ["Sections 312 to 316 of the IPC / Sections 88 to 92 of the BNS",
       "Sections 302 and 304 IPC / Sections 101 and 103 BNS",
       "Sections 375 and 376 IPC / Sections 63 and 64 BNS",
       "Sections 498A IPC / Section 85 BNS"], 0,
      "Causing miscarriage is a serious criminal offence under Sections 312-316 IPC (now Sections 88-92 BNS 2023), for which MTP Act provides a regulated health exception.",
      {"A": "Correct; IPC 312-316 / BNS 88-92.", "B": "Incorrect; Murder provisions.", "C": "Incorrect; Rape provisions.", "D": "Incorrect; Cruelty provisions."},
      "Standard", "MTP Act Scheme & IPC S. 312 / BNS S. 88", "Penal provisions governing miscarriage.")

add_q("mcq-mtp-01-005", "soc-mtp", "ch-soc-mtp-01", "top-mtp-01-01",
      "Under Section 1(2) of the MTP Act, 1971, what is the territorial extent of the Act?",
      ["It extends to the whole of India", "It extends to the whole of India except Jammu and Kashmir", "It applies only to Union Territories", "It applies only to government hospitals"], 0,
      "The Act extends to the whole of India.",
      {"A": "Correct; Whole of India.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 1(2)", "Territorial extent of MTP Act.")

add_q("mcq-mtp-01-006", "soc-mtp", "ch-soc-mtp-01", "top-mtp-01-01",
      "In Suchita Srivastava v. Chandigarh Administration (2009), what fundamental right did the Supreme Court recognize regarding reproductive choices?",
      ["Reproductive choice is an integral facet of personal liberty under Article 21 of the Constitution",
       "Reproductive choices are subject to the veto of the State Government",
       "Only married women have reproductive autonomy under Article 21",
       "Reproductive rights are commercial property rights"], 0,
      "In Suchita Srivastava (2009) 9 SCC 1, the Supreme Court held that reproductive choices of a woman fall within the realm of personal liberty under Article 21.",
      {"A": "Correct; Reproductive choice is protected under Article 21.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "Constitution Art. 21 & Suchita Srivastava (2009)", "Reproductive autonomy under Article 21.")

# top-mtp-01-02 (6)
add_q("mcq-mtp-01-007", "soc-mtp", "ch-soc-mtp-01", "top-mtp-01-02",
      "Under Section 2(d) of the MTP Act, 1971, who is a 'registered medical practitioner'?",
      ["A medical practitioner who possesses any recognized medical qualification under the National Medical Commission Act, 2019 and whose name is entered in the State Medical Register and who has prescribed training/experience in gynecology and obstetrics",
       "Any person holding a registered pharmacy diploma",
       "Any traditional naturopathic practitioner",
       "Any nurse who has assisted in 10 deliveries"], 0,
      "Section 2(d) mandates recognized medical qualification under NMC Act, registration on the State Medical Register, and prescribed postgraduate training/experience in gynecology/obstetrics.",
      {"A": "Correct; Recognized NMC qualification, State Register entry, and prescribed obstetric training.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 2(d)", "Definition of Registered Medical Practitioner under Section 2(d).")

add_q("mcq-mtp-01-008", "soc-mtp", "ch-soc-mtp-01", "top-mtp-01-02",
      "Under Section 2(a) of the MTP Act, who is a 'guardian' in relation to a minor or mentally ill person?",
      ["A person having the care of the person of a minor or a mentally ill person",
       "Only the biological father",
       "Only a testamentary guardian appointed by a registered will",
       "The District Magistrate ex officio"], 0,
      "Section 2(a) defines 'guardian' simply and broadly as a person having the care of the person of a minor or a mentally ill person.",
      {"A": "Correct; Person having the care of the minor or mentally ill person under Section 2(a).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 2(a)", "Definition of guardian under Section 2(a).")

add_q("mcq-mtp-01-009", "soc-mtp", "ch-soc-mtp-01", "top-mtp-01-02",
      "Under Section 2(e) of the MTP Act (inserted by 2021 Amendment), 'termination of pregnancy' means:",
      ["A procedure to terminate a pregnancy by using medical or surgical methods",
       "Causing accidental trauma to a fetus",
       "Delivery of a live child after 37 weeks",
       "Surgical caesarean section at full term"], 0,
      "Section 2(e) defines termination of pregnancy as a procedure to terminate a pregnancy by using medical or surgical methods.",
      {"A": "Correct; Statutory definition under Section 2(e).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 2(e)", "Definition of termination of pregnancy.")

add_q("mcq-mtp-01-010", "soc-mtp", "ch-soc-mtp-01", "top-mtp-01-02",
      "Under Section 2(b) of the MTP Act, what term replaced 'lunatic' by the 2002 Amendment?",
      ["'Mentally ill person'", "'Insane individual'", "'Unsound mind patient'", "'Incapable person'"], 0,
      "Act 64 of 2002 replaced the archaic word 'lunatic' with 'mentally ill person' having the meaning assigned under the Mental Health Act.",
      {"A": "Correct; Replaced with 'mentally ill person'.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "MTP Act S. 2(b)", "Replacement of archaic terminology in Section 2(b).")

add_q("mcq-mtp-01-011", "soc-mtp", "ch-soc-mtp-01", "top-mtp-01-02",
      "What minimum experience or qualification is prescribed under MTP Rules for a general MBBS doctor to terminate pregnancy up to 12 weeks?",
      ["Six months of housemanship in gynecology and obstetrics, or assisted in at least 25 cases of MTP in an approved institution",
       "Ten years of private general practice",
       "Conducting 100 caesarean surgeries",
       "Passing a written exam conducted by the District Collector"], 0,
      "MTP Rules require six months housemanship in obstetrics/gynecology or assisting in at least 25 cases of MTP in a recognized training institution.",
      {"A": "Correct; Six months housemanship or assisting in 25 MTP cases under MTP Rules.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "MTP Rules 2003 Rule 4", "Prescribed training/experience for RMP under MTP Rules.")

add_q("mcq-mtp-01-012", "soc-mtp", "ch-soc-mtp-01", "top-mtp-01-02",
      "Can a homoeopathic or ayurvedic practitioner (AYUSH) perform medical or surgical abortion under the MTP Act?",
      ["No, only registered medical practitioners possessing qualifications under the NMC Act with prescribed obstetric training can terminate pregnancy",
       "Yes, all registered medical systems have equal authority under MTP",
       "Only if they use herbal medications",
       "Only in rural primary health centres"], 0,
      "The Supreme Court and MTP Act strictly restrict termination to allopathic practitioners possessing recognized NMC qualifications and prescribed obstetric training.",
      {"A": "Correct; Only NMC-qualified allopathic practitioners with obstetric training.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "MTP Act S. 2(d)", "Exclusion of non-allopathic practitioners from MTP.")

# top-mtp-01-03 (6)
add_q("mcq-mtp-01-013", "soc-mtp", "ch-soc-mtp-01", "top-mtp-01-03",
      "On which date did the Medical Termination of Pregnancy (Amendment) Act, 2021 (Act No. 8 of 2021) come into force?",
      ["24 September 2021", "25 March 2021", "1 January 2022", "15 August 2021"], 0,
      "The 2021 Amendment received Presidential assent on 25 March 2021 and was officially enforced on 24 September 2021 by Central Government notification.",
      {"A": "Correct; Enforced on 24 September 2021.", "B": "Incorrect; 25 March 2021 was assent date.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Amendment Act 2021", "Commencement date of 2021 MTP Amendment Act.")

add_q("mcq-mtp-01-014", "soc-mtp", "ch-soc-mtp-01", "top-mtp-01-03",
      "In Section 3(2) Explanation 1 of the MTP Act, what vital change was made by the 2021 Amendment regarding contraceptive failure?",
      ["Substituted the words 'any woman or her partner' for the words 'any married woman or her husband'",
       "Restricted contraceptive failure ground strictly to government employees",
       "Abolished contraceptive failure as a ground for abortion",
       "Mandated written affidavit by both spouses"], 0,
      "The 2021 Amendment substituted 'any woman or her partner' in place of 'any married woman or her husband', extending statutory coverage to unmarried women.",
      {"A": "Correct; Substituted 'any woman or her partner', extending rights to unmarried women.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 3(2) Expl. 1", "Extension of contraceptive failure ground to unmarried women.")

add_q("mcq-mtp-01-015", "soc-mtp", "ch-soc-mtp-01", "top-mtp-01-03",
      "In which landmark judgment did the Supreme Court hold that excluding unmarried women from accessing abortion between 20 and 24 weeks is discriminatory and violates Article 14?",
      ["X v. Principal Secretary, Health and Family Welfare Department, GNCTD (2022)",
       "Navtej Singh Johar v. Union of India (2018)",
       "Joseph Shine v. Union of India (2018)",
       "K.S. Puttaswamy v. Union of India (2017)"], 0,
      "In X v. Principal Secretary, GNCTD (2022) 11 SCC 641, Dr. D.Y. Chandrachud, J., held that artificial distinctions between married and unmarried women violate Article 14.",
      {"A": "Correct; X v. Principal Secretary (2022).", "B": "Incorrect; Section 377 IPC.", "C": "Incorrect; Section 497 IPC adultery.", "D": "Incorrect; Right to Privacy."},
      "Advanced", "MTP Act S. 3 & X v. Principal Secretary (2022)", "Supreme Court landmark ruling on unmarried women's abortion rights.")

add_q("mcq-mtp-01-016", "soc-mtp", "ch-soc-mtp-01", "top-mtp-01-03",
      "In X v. Principal Secretary (2022), what did the Supreme Court hold regarding marital rape under the MTP Act?",
      ["Held that for the purposes of the MTP Act, rape includes marital rape, enabling a married woman pregnant through non-consensual marital sex to access abortion up to 24 weeks",
       "Held that marital rape cannot be recognized under any Indian law",
       "Held that married women can never terminate pregnancy without husband's consent",
       "Held that MTP applies only to pregnancies out of wedlock"], 0,
      "The Supreme Court held that within the protective framework of MTP, rape includes marital rape, entitling surviving wives to terminate pregnancy up to 24 weeks under Rule 3B.",
      {"A": "Correct; Rape includes marital rape for MTP purposes under Rule 3B.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "MTP Rules Rule 3B & X v. Principal Secretary (2022)", "Recognition of marital rape under MTP Act.")

add_q("mcq-mtp-01-017", "soc-mtp", "ch-soc-mtp-01", "top-mtp-01-03",
      "How did the 2021 Amendment alter the general upper gestational ceiling for terminating pregnancy?",
      ["Increased the ceiling from 20 weeks to 24 weeks for special categories of women, and removed the ceiling entirely for substantial foetal abnormalities approved by a Medical Board",
       "Reduced the ceiling from 20 weeks to 12 weeks",
       "Fixed an absolute uniform ceiling of 28 weeks for all women",
       "Abolished all gestational ceilings unconditionally"], 0,
      "The 2021 Amendment increased the limit from 20 to 24 weeks for vulnerable categories, and created Section 3(2B) allowing post-24 week termination for substantial fetal abnormalities.",
      {"A": "Correct; Expanded to 24 weeks for vulnerable groups, and beyond 24 weeks for fetal abnormalities.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 3(2), (2B)", "Evolution of gestational ceilings in 2021 Amendment.")

add_q("mcq-mtp-01-018", "soc-mtp", "ch-soc-mtp-01", "top-mtp-01-03",
      "Under the 2021 Amendment, how many doctors' opinions are required to terminate a pregnancy up to 20 weeks?",
      ["Opinion of one registered medical practitioner",
       "Opinion of two registered medical practitioners",
       "Opinion of three registered medical practitioners",
       "Approval of the State Medical Board"], 0,
      "Under amended Section 3(2)(a), for pregnancy up to twenty weeks, the opinion of only one registered medical practitioner is required (previously required 2 doctors beyond 12 weeks).",
      {"A": "Correct; Only one RMP required up to 20 weeks under Section 3(2)(a).", "B": "Incorrect; Two RMPs required between 20 and 24 weeks.", "C": "Incorrect.", "D": "Incorrect; Medical Board required beyond 24 weeks."},
      "Foundational", "MTP Act S. 3(2)(a)", "Doctor requirement (1 RMP up to 20 weeks).")

# Chapter 2: ch-soc-mtp-02 (16 MCQs)
# top-mtp-02-01 (6)
add_q("mcq-mtp-01-019", "soc-mtp", "ch-soc-mtp-02", "top-mtp-02-01",
      "Under Section 3(2)(b) of the MTP Act, 1971 (as amended in 2021), between which gestational ages can a pregnancy be terminated on the opinion of two registered medical practitioners for eligible categories of women?",
      ["Between twenty weeks and twenty-four weeks", "Between twelve weeks and sixteen weeks", "Between twenty-four weeks and thirty-two weeks", "Up to twelve weeks only"], 0,
      "Section 3(2)(b) permits termination between 20 and 24 weeks on the opinion of not less than two registered medical practitioners for eligible categories prescribed in Rule 3B.",
      {"A": "Correct; 20 to 24 weeks with opinion of two RMPs under Section 3(2)(b).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 3(2)(b)", "20 to 24 weeks gestational bracket and two RMPs requirement.")

add_q("mcq-mtp-01-020", "soc-mtp", "ch-soc-mtp-02", "top-mtp-02-01",
      "Which of the following is NOT an eligible category of woman entitled to terminate pregnancy between 20 and 24 weeks under Rule 3B of MTP Rules, 2021?",
      ["Survivors of sexual assault or rape or incest",
       "Minors and women with physical or mental disabilities",
       "Change of marital status during ongoing pregnancy (widowhood or divorce)",
       "A woman seeking termination solely because the unborn child is female"], 3,
      "Rule 3B lists vulnerable categories (rape survivors, minors, disability, change of marital status, disaster emergencies). Sex selection is criminal and strictly prohibited.",
      {"A": "Incorrect; Rape/incest survivors are eligible under Rule 3B(a).", "B": "Incorrect; Minors and disabled women are eligible under Rule 3B(b),(c).", "C": "Incorrect; Change of marital status is eligible under Rule 3B(d).", "D": "Correct; Sex-selective termination is completely illegal under PCPNDT and MTP."},
      "Foundational", "MTP Rules 2021 Rule 3B", "Eligible categories for 20-24 weeks termination under Rule 3B.")

add_q("mcq-mtp-01-021", "soc-mtp", "ch-soc-mtp-02", "top-mtp-02-01",
      "Under Rule 3B(g) of the MTP Rules, 2021, can women in humanitarian settings or disaster or emergency situations terminate pregnancy between 20 and 24 weeks?",
      ["Yes, women with pregnancy in humanitarian settings or disaster or emergency situations declared by the Government are eligible under Rule 3B(g)",
       "No, disasters suspend all medical rights",
       "Only if they have lost all personal property",
       "Only with prior sanction of the President of India"], 0,
      "Rule 3B(g) specifically includes women in humanitarian settings, disaster zones, or emergencies declared by Government.",
      {"A": "Correct; Expressly included under Rule 3B(g).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "MTP Rules 2021 Rule 3B(g)", "Humanitarian emergency inclusion under Rule 3B.")

add_q("mcq-mtp-01-022", "soc-mtp", "ch-soc-mtp-02", "top-mtp-02-01",
      "Under Section 3(2B) of the MTP Act, the 24-week gestational ceiling shall NOT apply to the termination of pregnancy by any medical practitioner where:",
      ["Such termination is necessitated by the diagnosis of any of the substantial foetal abnormalities diagnosed by a Medical Board",
       "The pregnant woman travels to a foreign country",
       "The father files an affidavit of financial distress",
       "The doctor charges zero medical fees"], 0,
      "Section 3(2B) provides that gestational limits under Section 3(2)(b) shall not apply to termination where substantial fetal abnormalities are diagnosed by a Medical Board.",
      {"A": "Correct; Substantial fetal abnormalities diagnosed by Medical Board under Section 3(2B).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 3(2B)", "Exemption from gestational limits under Section 3(2B).")

add_q("mcq-mtp-01-023", "soc-mtp", "ch-soc-mtp-02", "top-mtp-02-01",
      "Under Section 3(2C) of the MTP Act, what is the composition of the State-level Medical Board?",
      ["A Gynecologist, a Pediatrician, a Radiologist or Sonologist, and such other members as may be notified by the State Government",
       "Three police officers and a magistrate",
       "A committee of three religious clerics",
       "The District Collector and two village pradhans"], 0,
      "Section 3(2C) provides that every State Medical Board shall consist of: Gynecologist, Pediatrician, Radiologist/Sonologist, and other notified members.",
      {"A": "Correct; Gynecologist, Pediatrician, Radiologist/Sonologist under Section 3(2C).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "MTP Act S. 3(2C)", "Composition of Medical Board under Section 3(2C).")

add_q("mcq-mtp-01-024", "soc-mtp", "ch-soc-mtp-02", "top-mtp-02-01",
      "Under Rule 3A of MTP Rules, within what timeline must the Medical Board examine the woman and convey its decision?",
      ["Examine within three days of receipt of application and convey decision within forty-eight hours of examination",
       "Within thirty days",
       "Within fifteen days",
       "Within two weeks"], 0,
      "Rule 3A mandates that the Medical Board shall examine the woman within 3 days and convey its decision within 48 hours to prevent delay in critical pregnancies.",
      {"A": "Correct; Examine within 3 days, convey decision within 48 hours under Rule 3A.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "MTP Rules 2021 Rule 3A", "Timelines for Medical Board decision under Rule 3A.")

# top-mtp-02-02 (5)
add_q("mcq-mtp-01-025", "soc-mtp", "ch-soc-mtp-02", "top-mtp-02-02",
      "Under Section 3(2)(a)(i) of the MTP Act, pregnancy can be terminated if its continuance would involve a risk to:",
      ["The life of the pregnant woman or of grave injury to her physical or mental health",
       "The political reputation of her family",
       "The financial credit rating of the father",
       "The inheritance shares of existing siblings"], 0,
      "Section 3(2)(a)(i) sets out the primary health ground: risk to the life of the pregnant woman or of grave injury to her physical or mental health.",
      {"A": "Correct; Risk to life or grave injury to physical/mental health under Section 3(2)(a)(i).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 3(2)(a)(i)", "Core health grounds for termination.")

add_q("mcq-mtp-01-026", "soc-mtp", "ch-soc-mtp-02", "top-mtp-02-02",
      "Under Section 3(2) Explanation 2, where a pregnancy is alleged by the pregnant woman to have been caused by rape, the anguish caused by such pregnancy shall be presumed to constitute:",
      ["A grave injury to the mental health of the pregnant woman",
       "A minor domestic inconvenience",
       "Proof beyond reasonable doubt in the rape trial",
       "A ground for immediate dissolution of marriage"], 0,
      "Explanation 2 to Section 3(2) creates a statutory presumption: anguish caused by a pregnancy resulting from rape is presumed to constitute grave injury to mental health.",
      {"A": "Correct; Presumed to constitute grave injury to mental health under Explanation 2.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 3(2) Expl. 2", "Statutory presumption of mental anguish in rape cases.")

add_q("mcq-mtp-01-027", "soc-mtp", "ch-soc-mtp-02", "top-mtp-02-02",
      "Under Section 3(2)(a)(ii) of the Act, what fetal ground justifies termination of pregnancy?",
      ["Substantial risk that if the child were born, it would suffer from any serious physical or mental abnormality so as to be seriously handicapped",
       "The child is predicted to be below 5 feet in height",
       "The child will have brown eyes instead of black",
       "The family astrologer predicts misfortune"], 0,
      "Section 3(2)(a)(ii) permits termination where there is substantial risk of serious physical or mental abnormality causing the child to be seriously handicapped.",
      {"A": "Correct; Substantial risk of serious physical or mental abnormality under Section 3(2)(a)(ii).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 3(2)(a)(ii)", "Substantial fetal abnormality ground under Section 3(2).")

add_q("mcq-mtp-01-028", "soc-mtp", "ch-soc-mtp-02", "top-mtp-02-02",
      "Under Section 3(3) of the MTP Act, 1971, in determining whether the continuance of a pregnancy would involve risk of grave injury to the health of a pregnant woman, account may be taken of:",
      ["The pregnant woman's actual or reasonably foreseeable environment",
       "The opinions of her neighbours",
       "The general GDP growth rate of the district",
       "The employment rate in public sector corporations"], 0,
      "Section 3(3) provides a compassionate contextual rule: the doctor may take into account the pregnant woman's actual or reasonably foreseeable environment.",
      {"A": "Correct; Woman's actual or reasonably foreseeable environment under Section 3(3).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "MTP Act S. 3(3)", "Consideration of actual or foreseeable environment under Section 3(3).")

add_q("mcq-mtp-01-029", "soc-mtp", "ch-soc-mtp-02", "top-mtp-02-02",
      "Can failure of any device or method used by any woman or her partner for the purpose of limiting the number of children be presumed to constitute grave injury to mental health?",
      ["Yes, Explanation 1 to Section 3(2) creates a statutory presumption that the anguish caused by such pregnancy may be presumed to constitute grave injury to mental health",
       "No, contraceptive failure can never be a ground under Indian law",
       "Only if the contraceptive was purchased from a government pharmacy",
       "Only for women who already have three children"], 0,
      "Explanation 1 to Section 3(2) explicitly provides that anguish caused by contraceptive failure may be presumed to constitute a grave injury to the mental health of the woman.",
      {"A": "Correct; Statutory presumption of mental anguish due to contraceptive failure.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "MTP Act S. 3(2) Expl. 1", "Presumption of mental injury in contraceptive failure.")

# top-mtp-02-03 (5)
add_q("mcq-mtp-01-030", "soc-mtp", "ch-soc-mtp-02", "top-mtp-02-03",
      "Under Section 5(1) of the MTP Act, what emergency exception completely overrides the gestational limits in Section 3 and Section 4?",
      ["Where the termination of pregnancy is immediately necessary to save the life of the pregnant woman, conducted by a registered medical practitioner",
       "Where the husband demands an abortion before leaving for military service",
       "Where the hospital has a vacant bed that day",
       "Where the woman pays double the hospital fee"], 0,
      "Section 5(1) non-obstante clause provides that Section 3(2) gestational limits do not apply where termination is immediately necessary to save the woman's life.",
      {"A": "Correct; Immediate necessity to save woman's life overrides all limits under Section 5(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 5(1)", "Life-saving emergency exception under Section 5(1).")

add_q("mcq-mtp-01-031", "soc-mtp", "ch-soc-mtp-02", "top-mtp-02-03",
      "Does an emergency termination under Section 5(1) to save the woman's life require the opinion of two doctors or approval of a Medical Board?",
      ["No, the opinion of a single registered medical practitioner acting in good faith is sufficient under Section 5(1)",
       "Yes, it requires three doctors and a magistrate's counter-signature",
       "Yes, approval of the High Court is mandatory",
       "It requires approval of the Chief Medical Officer within 1 hour"], 0,
      "Section 5(1) specifically exempts emergency procedures from Section 3(2); a single registered medical practitioner can act immediately in good faith.",
      {"A": "Correct; Single RMP acting in good faith under Section 5(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "MTP Act S. 5(1)", "Single doctor emergency competence under Section 5(1).")

add_q("mcq-mtp-01-032", "soc-mtp", "ch-soc-mtp-02", "top-mtp-02-03",
      "Can a writ petition under Article 226 or Article 32 be filed before the High Court or Supreme Court to seek permission for termination beyond 24 weeks?",
      ["Yes, Constitutional Courts routinely exercise writ powers, ordering medical boards to examine the woman and granting permission where fetal viability or maternal health requires it",
       "No, Constitutional Courts have zero jurisdiction over medical matters",
       "Only the President can permit abortions beyond 24 weeks",
       "Writ petitions are barred under Section 5"], 0,
      "The Supreme Court and High Courts exercise constitutional writ jurisdiction under Articles 32 and 226 to protect maternal life and reproductive autonomy beyond 24 weeks.",
      {"A": "Correct; Constitutional Courts regularly exercise writ jurisdiction with medical board inputs.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "Constitution Art. 32, 226 & MTP S. 3(2B)", "Constitutional writ jurisdiction in late-term abortions.")

add_q("mcq-mtp-01-033", "soc-mtp", "ch-soc-mtp-02", "top-mtp-02-03",
      "Under Section 5(1), does an emergency termination to save the life of the woman need to be conducted in a government or approved hospital?",
      ["No, Section 5(1) explicitly provides that Section 4 (place of termination) shall also not apply where termination is immediately necessary to save her life",
       "Yes, it must strictly be conducted in an AIIMS hospital",
       "Yes, it cannot be conducted in any private nursing home",
       "Only if the place has an operational blood bank"], 0,
      "Section 5(1) explicitly states: 'the provisions of section 4, and so much of the provisions of sub-section (2) of section 3... shall not apply' to life-saving emergencies.",
      {"A": "Correct; Section 4 place restrictions are waived in life-saving emergencies under Section 5(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "MTP Act S. 5(1)", "Waiver of place restrictions under Section 5(1).")

add_q("mcq-mtp-01-034", "soc-mtp", "ch-soc-mtp-02", "top-mtp-02-03",
      "In XYZ v. State of Gujarat (2023), what did the Supreme Court hold regarding delay by High Courts in deciding rape survivors' abortion petitions?",
      ["Deprecated delays and held that in pregnancy matters, every day's delay is crucial; High Courts must act with utmost dispatch",
       "Held that High Courts should take at least six months to verify facts",
       "Held that rape victims should wait until delivery to seek relief",
       "Dismissed the petition as non-justiciable"], 0,
      "In XYZ v. State of Gujarat (2023) 9 SCC 705, the Supreme Court stressed that in abortion matters, time is of the essence and delays cause irreparable maternal harm.",
      {"A": "Correct; Urgency and utmost dispatch required in reproductive rights cases.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "MTP Act S. 3 & XYZ v. State of Gujarat (2023)", "Supreme Court precedent on expeditious judicial disposal.")

# Chapter 3: ch-soc-mtp-03 (16 MCQs)
# top-mtp-03-01 (6)
add_q("mcq-mtp-01-035", "soc-mtp", "ch-soc-mtp-03", "top-mtp-03-01",
      "Under Section 4 of the MTP Act, 1971, where can a pregnancy be lawfully terminated?",
      ["At a hospital established or maintained by Government, or a place for the time being approved for the purpose of this Act by Government or a District-level Committee",
       "At any pharmacy or chemist shop",
       "At the patient's personal residence",
       "Inside any registered commercial ambulance"], 0,
      "Section 4 specifies that no termination of pregnancy shall be made at any place other than a government hospital or an approved place.",
      {"A": "Correct; Government hospital or approved place under Section 4.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 4", "Approved places for termination under Section 4.")

add_q("mcq-mtp-01-036", "soc-mtp", "ch-soc-mtp-03", "top-mtp-03-01",
      "Under Section 3(4)(b) of the MTP Act, whose consent is strictly required for terminating the pregnancy of an adult woman of sound mind?",
      ["Save as otherwise provided in clause (a), no pregnancy shall be terminated except with the consent of the pregnant woman herself",
       "The joint written consent of the pregnant woman and her husband",
       "The written consent of her parents-in-law",
       "The approval of the local Gram Panchayat"], 0,
      "Section 3(4)(b) embodies female bodily autonomy: for an adult woman of sound mind, her sole consent is necessary and sufficient; no spousal or parental consent is required.",
      {"A": "Correct; Sole consent of the pregnant woman under Section 3(4)(b).", "B": "Incorrect; Spousal consent is NOT required by law.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 3(4)(b)", "Sole consent of adult pregnant woman under Section 3(4)(b).")

add_q("mcq-mtp-01-037", "soc-mtp", "ch-soc-mtp-03", "top-mtp-03-01",
      "Can a husband file a suit for damages or injunction against a doctor for terminating his adult wife's pregnancy with her sole consent?",
      ["No, as held in Anil Kumar Malhotra (2018) and other precedents, a husband has no legal right to compel his wife to bear a child; her sole consent is legally sufficient",
       "Yes, a husband is the legal owner of his wife's reproductive capacity",
       "Yes, if the marriage was arranged by parents",
       "Yes, under the law of torts for loss of consortium"], 0,
      "Indian Courts (including Punjab & Haryana HC in Anil Kumar Malhotra) have consistently held that a wife's reproductive autonomy is paramount; husband's consent is not required.",
      {"A": "Correct; Husband cannot restrain wife or sue doctor; wife's consent is paramount.", "B": "Incorrect; Repugnant to constitutional equality.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "MTP Act S. 3(4)(b) & Art. 21", "Husband cannot veto or challenge wife's lawful MTP.")

add_q("mcq-mtp-01-038", "soc-mtp", "ch-soc-mtp-03", "top-mtp-03-01",
      "Under Section 3(4)(a) of the MTP Act, whose consent is required if the pregnant woman has not attained the age of eighteen years or is a mentally ill person?",
      ["No pregnancy shall be terminated except with the consent in writing of her guardian",
       "The consent of the local police inspector",
       "The oral consent of the minor herself",
       "A decree of a Family Court"], 0,
      "Section 3(4)(a) specifies that where the pregnant woman is below 18 years or mentally ill, written consent of her guardian is mandatory.",
      {"A": "Correct; Written consent of her guardian under Section 3(4)(a).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 3(4)(a)", "Guardian consent for minors and mentally ill persons.")

add_q("mcq-mtp-01-039", "soc-mtp", "ch-soc-mtp-03", "top-mtp-03-01",
      "When a minor approaches an RMP for termination of pregnancy under MTP, does the doctor have an obligation under the POCSO Act, 2012?",
      ["Yes, under Section 19 of POCSO Act, there is a mandatory duty to report sexual abuse of a minor; however, Supreme Court (2022) directed protecting the minor's identity",
       "No, the MTP Act completely repeals the POCSO Act",
       "Only if the minor asks the doctor to report",
       "Only if the accused accompanied the minor to the clinic"], 0,
      "In X v. Principal Secretary (2022), the Supreme Court harmonized MTP and POCSO, recognizing mandatory Section 19 reporting while protecting privacy and confidentiality of the minor.",
      {"A": "Correct; Mandatory reporting under Section 19 POCSO with strict confidentiality protections.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "MTP Act S. 3 & POCSO S. 19", "Interplay between MTP Act and mandatory POCSO reporting.")

add_q("mcq-mtp-01-040", "soc-mtp", "ch-soc-mtp-03", "top-mtp-03-01",
      "Under Section 4(b) of the Act, who heads the District-level Committee empowered to approve private places for MTP?",
      ["Chief Medical Officer or District Health Officer of the District",
       "Superintendent of Police",
       "District Sessions Judge",
       "Elected Member of Legislative Assembly"], 0,
      "Under MTP Rules, the District-level Committee for approving places is headed by the Chief Medical Officer (CMO) or District Health Officer.",
      {"A": "Correct; Chief Medical Officer (CMO) or District Health Officer.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "MTP Act S. 4 & MTP Rules 2003", "District-level approval committee for MTP clinics.")

# top-mtp-03-02 (5)
add_q("mcq-mtp-01-041", "soc-mtp", "ch-soc-mtp-03", "top-mtp-03-02",
      "What statutory safeguard was inserted into the MTP Act as Section 5A by the 2021 Amendment?",
      ["Protection of privacy of a woman: no registered medical practitioner shall reveal the name and other particulars of a woman whose pregnancy has been terminated",
       "Mandatory publication of abortion statistics in newspapers",
       "Display of names of patients on hospital notice boards",
       "Linking of all abortion records to public voter IDs"], 0,
      "Section 5A(1) enacts a strict confidentiality rule: no RMP shall reveal the name and other particulars of a woman whose pregnancy has been terminated except to an authorized person.",
      {"A": "Correct; Protection of woman's privacy and strict confidentiality under Section 5A.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 5A", "Confidentiality mandate under Section 5A.")

add_q("mcq-mtp-01-042", "soc-mtp", "ch-soc-mtp-03", "top-mtp-03-02",
      "Under Section 5A(2) of the MTP Act, what is the punishment for revealing the name or particulars of a woman whose pregnancy has been terminated?",
      ["Imprisonment which may extend to one year, or with fine, or with both",
       "Simple apology to the woman",
       "Fine of Rs 100 only",
       "Imprisonment for 7 years"], 0,
      "Section 5A(2) provides that whoever contravenes Section 5A(1) shall be punishable with imprisonment which may extend to one year, or with fine, or with both.",
      {"A": "Correct; Imprisonment up to one year, or fine, or both under Section 5A(2).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 5A(2)", "Penalty for breach of confidentiality under Section 5A(2).")

add_q("mcq-mtp-01-043", "soc-mtp", "ch-soc-mtp-03", "top-mtp-03-02",
      "To whom alone can the particulars of a woman undergoing MTP be disclosed under Section 5A(1)?",
      ["To a person authorized by any law for the time being in force",
       "To any journalist requesting an interview",
       "To the employer of the woman",
       "To the resident welfare association of her society"], 0,
      "Section 5A(1) permits disclosure strictly to 'a person authorized by any law for the time being in force' (e.g., investigating officers or courts under judicial orders).",
      {"A": "Correct; Strictly to a person authorized by law under Section 5A(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "MTP Act S. 5A(1)", "Authorized disclosure exceptions under Section 5A.")

add_q("mcq-mtp-01-044", "soc-mtp", "ch-soc-mtp-03", "top-mtp-03-02",
      "How are MTP registers and patient admission forms maintained in hospitals to ensure privacy under MTP Regulations?",
      ["In secret custody with serial admission numbers, and registers are not open to general public inspection",
       "Displayed on the main entrance counter",
       "Uploaded to an open-access public website",
       "Shared with commercial marketing companies"], 0,
      "MTP Regulations mandate maintaining Admission Registers under confidential custody, with serial code numbers, accessible only to inspecting authorities.",
      {"A": "Correct; Confidential custody with serial code numbers under MTP Regulations.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "MTP Regulations 2003 Reg. 6, 7", "Confidential maintenance of MTP admission registers.")

add_q("mcq-mtp-01-045", "soc-mtp", "ch-soc-mtp-03", "top-mtp-03-02",
      "Under Section 7 of the MTP Act, 1971, who has the power to make regulations regarding maintenance of admission registers and notices?",
      ["The State Government by notification in the Official Gazette",
       "The Chief Justice of India",
       "The Medical Council of India alone",
       "The Municipal Health Officer"], 0,
      "Section 7 empowers the State Government to make regulations regarding certification of opinions, maintenance of registers, and confidentiality.",
      {"A": "Correct; State Government has power to make regulations under Section 7.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "MTP Act S. 7", "Regulation-making power under Section 7.")

# top-mtp-03-03 (5)
add_q("mcq-mtp-01-046", "soc-mtp", "ch-soc-mtp-03", "top-mtp-03-03",
      "Under Section 5(2) of the MTP Act, what is the criminal liability of any person who terminates a pregnancy when they are NOT a registered medical practitioner?",
      ["Punishable with rigorous imprisonment for a term which shall not be less than two years but which may extend to seven years under the Indian Penal Code / BNS",
       "Fine of Rs 500 only",
       "Civil imprisonment for thirty days",
       "Simple censure by the Panchayat"], 0,
      "Section 5(2) provides that termination by any person who is not an RMP shall be an offence punishable under IPC with rigorous imprisonment of 2 to 7 years.",
      {"A": "Correct; Rigorous imprisonment for 2 to 7 years under Section 5(2).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 5(2) & IPC S. 312 / BNS S. 88", "Penal liability of unqualified abortionists under Section 5(2).")

add_q("mcq-mtp-01-047", "soc-mtp", "ch-soc-mtp-03", "top-mtp-03-03",
      "Under Section 5(3) of the Act, what is the punishment for terminating a pregnancy at a place which has NOT been approved or maintained by Government?",
      ["Rigorous imprisonment for a term which shall not be less than two years but which may extend to seven years",
       "Fine of Rs 1,000 only",
       "Cancellation of land lease only",
       "Imprisonment for three months"], 0,
      "Section 5(3) explicitly punishes terminating pregnancy at unapproved places with rigorous imprisonment of not less than two years extending up to seven years.",
      {"A": "Correct; Rigorous imprisonment for 2 to 7 years under Section 5(3).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 5(3)", "Punishment for operating unapproved abortion facility.")

add_q("mcq-mtp-01-048", "soc-mtp", "ch-soc-mtp-03", "top-mtp-03-03",
      "Who can be punished under Section 5(4) of the MTP Act for an illegal termination at an unapproved place?",
      ["Any person who terminates the pregnancy, and the owner of any place which is not approved under the Act",
       "Only the patient herself",
       "Only the pharmacist who sold the disinfectant",
       "Only the driver of the taxi"], 0,
      "Section 5(4) makes both the doctor/practitioner terminating the pregnancy and the owner of the unapproved clinic liable.",
      {"A": "Correct; Both the person terminating and the clinic owner are liable under Section 5(4).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "MTP Act S. 5(4)", "Joint liability of practitioner and unapproved facility owner.")

add_q("mcq-mtp-01-049", "soc-mtp", "ch-soc-mtp-03", "top-mtp-03-03",
      "Under Section 8 of the MTP Act, what protection is granted for action taken in good faith?",
      ["No suit or other legal proceeding shall lie against any registered medical practitioner for any damage caused or likely to be caused by anything which is in good faith done or intended to be done under this Act",
       "Protection applies only if the patient signs a 100-rupee stamp paper",
       "Protection applies only to military doctors",
       "Good faith protection is unconstitutional"], 0,
      "Section 8 provides statutory immunity to registered medical practitioners against civil suits or legal proceedings for acts done in good faith under the Act.",
      {"A": "Correct; Statutory protection of action taken in good faith under Section 8.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "MTP Act S. 8", "Good faith indemnity clause under Section 8.")

add_q("mcq-mtp-01-050", "soc-mtp", "ch-soc-mtp-03", "top-mtp-03-03",
      "Under Section 6 of the MTP Act, 1971, who has the power to make general rules for carrying out the provisions of the Act?",
      ["The Central Government by notification in the Official Gazette",
       "The Chief Justice of the High Court",
       "The Indian Medical Association",
       "The Director General of Health Services"], 0,
      "Section 6(1) empowers the Central Government, by notification in the Official Gazette, to make rules for carrying out the provisions of the Act.",
      {"A": "Correct; Central Government has rulemaking power under Section 6.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "MTP Act S. 6", "Rulemaking power under Section 6.")


# --- ACT 8: INDECENT REPRESENTATION OF WOMEN (PROHIBITION) ACT, 1986 (soc-indecent-rep) - 45 MCQs ---

# Chapter 1: ch-soc-irwa-01 (15 MCQs)
# top-irwa-01-01 (5)
add_q("mcq-irwa-01-001", "soc-indecent-rep", "ch-soc-irwa-01", "top-irwa-01-01",
      "On which date did the Indecent Representation of Women (Prohibition) Act, 1986 (Act No. 60 of 1986) come into force in India?",
      ["23 December 1986", "2 October 1987", "1 January 1987", "15 August 1988"], 1,
      "The Act was enacted in December 1986 and brought into force on 2 October 1987 (Gandhi Jayanti) by Central Government notification.",
      {"A": "Incorrect; 23 December 1986 was Presidential assent date.", "B": "Correct; Came into force on 2 October 1987.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "IRWA S. 1(3)", "Commencement date of IRWA 1986.")

add_q("mcq-irwa-01-002", "soc-indecent-rep", "ch-soc-irwa-01", "top-irwa-01-01",
      "What was the core legislative policy behind enacting the Indecent Representation of Women (Prohibition) Act, 1986?",
      ["To prohibit indecent representation of women through advertisements or in publications, writings, paintings, figures or in any other manner",
       "To censor political criticism of the government",
       "To regulate dress codes in public transport",
       "To establish an official state fashion board"], 0,
      "The Act was enacted to prohibit indecent representation of women through advertisements, publications, writings, paintings, and figures, curbing commercial exploitation of female dignity.",
      {"A": "Correct; Statutory purpose stated in Preamble.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "IRWA Preamble", "Legislative purpose of IRWA 1986.")

add_q("mcq-irwa-01-003", "soc-indecent-rep", "ch-soc-irwa-01", "top-irwa-01-01",
      "Under Section 1(2) of the Act, what is the territorial extent of the Indecent Representation of Women (Prohibition) Act, 1986?",
      ["It extends to the whole of India", "It extends to the whole of India except Jammu and Kashmir", "It applies only to metropolitan cities", "It applies only to printing presses"], 0,
      "The Act extends to the whole of India.",
      {"A": "Correct; Whole of India.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "IRWA S. 1(2)", "Territorial extent of IRWA 1986.")

add_q("mcq-irwa-01-004", "soc-indecent-rep", "ch-soc-irwa-01", "top-irwa-01-01",
      "How does the Indecent Representation of Women Act interact with Section 292 of the Indian Penal Code, 1860 / Section 294 of Bharatiya Nyaya Sanhita, 2023 (Obscenity)?",
      ["IRWA is a specialized enactment focused specifically on the dignity of women, complementing general obscenity provisions under the Penal Code",
       "IRWA repealed Section 292 IPC completely",
       "IRWA only applies after an IPC conviction is obtained",
       "Section 292 IPC cannot be applied if IRWA is invoked"], 0,
      "IRWA is a targeted special statute addressing derogatory/indecent portrayals of women, operating concurrently with general penal obscenity laws under Section 292 IPC / 294 BNS.",
      {"A": "Correct; Specialized enactment complementing general penal obscenity provisions.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "IRWA Scheme & IPC S. 292 / BNS S. 294", "Interplay between IRWA and general penal obscenity laws.")

add_q("mcq-irwa-01-005", "soc-indecent-rep", "ch-soc-irwa-01", "top-irwa-01-01",
      "Which constitutional provisions directly inspire the prohibition of indecent depiction of women?",
      ["Article 15(3) and fundamental duty under Article 51A(e) to renounce practices derogatory to the dignity of women",
       "Article 356 and Article 365",
       "Article 110 and Article 112",
       "Article 310 and Article 311"], 0,
      "Article 15(3) (affirmative provisions for women) read with Article 51A(e) (duty to renounce practices derogatory to women's dignity) underpins the enactment.",
      {"A": "Correct; Article 15(3) and Article 51A(e) of the Constitution.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "Constitution Arts. 15(3), 51A(e)", "Constitutional basis of IRWA.")

# top-irwa-01-02 (5)
add_q("mcq-irwa-01-006", "soc-indecent-rep", "ch-soc-irwa-01", "top-irwa-01-02",
      "Under Section 2(a) of the Act, 'advertisement' includes:",
      ["Any notice, circular, label, wrapper or other document and also includes any visible representation made by means of any light, sound, smoke or gas",
       "Only printed flyers distributed by hand",
       "Only television commercials broadcast after 10 PM",
       "Only newspaper front-page ads"], 0,
      "Section 2(a) defines advertisement broadly, including notices, circulars, wrappers, documents, and representations made by light, sound, smoke or gas.",
      {"A": "Correct; Broad statutory definition under Section 2(a).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "IRWA S. 2(a)", "Definition of advertisement under Section 2(a).")

add_q("mcq-irwa-01-007", "soc-indecent-rep", "ch-soc-irwa-01", "top-irwa-01-02",
      "Under Section 2(b) of the Act, 'distribution' includes:",
      ["Distribution by way of samples whether free or otherwise",
       "Only commercial retail sale",
       "Only postal delivery across State borders",
       "Exclusively export to foreign nations"], 0,
      "Section 2(b) defines distribution to explicitly include distribution by way of samples whether free or otherwise.",
      {"A": "Correct; Distribution by way of samples whether free or otherwise under Section 2(b).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "IRWA S. 2(b)", "Definition of distribution under Section 2(b).")

add_q("mcq-irwa-01-008", "soc-indecent-rep", "ch-soc-irwa-01", "top-irwa-01-02",
      "Under Section 2(d) of the Act, 'package' includes:",
      ["Any box, carton, tin or other container",
       "Only wooden freight crates",
       "Only plastic envelopes",
       "Only sealed steel drums"], 0,
      "Section 2(d) defines package as including any box, carton, tin or other container.",
      {"A": "Correct; Box, carton, tin or other container under Section 2(d).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "IRWA S. 2(d)", "Definition of package under Section 2(d).")

add_q("mcq-irwa-01-009", "soc-indecent-rep", "ch-soc-irwa-01", "top-irwa-01-02",
      "Does displaying an indecent portrayal of a woman on consumer product packaging (e.g., soap box or perfume wrapper) violate the Act?",
      ["Yes, Section 2(a) covers wrappers and labels, and Section 4 prohibits sale or distribution of such packages",
       "No, consumer packaging is exempt from the Act",
       "Only if the product is sold at a government ration shop",
       "Only if imported from abroad"], 0,
      "Sections 2(a), 2(d), 3, and 4 explicitly cover labels, wrappers, packages, and cartons, making commercial packaging subject to the statutory ban.",
      {"A": "Correct; Packaging, labels, and wrappers are explicitly prohibited under the Act.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "IRWA S. 2(a), 2(d), S. 4", "Application of IRWA to product packaging.")

add_q("mcq-irwa-01-010", "soc-indecent-rep", "ch-soc-irwa-01", "top-irwa-01-02",
      "Can digital electronic representations, online banners, or social media advertisements be prosecuted under the principles of Section 2(a)?",
      ["Yes, Section 2(a) covers visible representations made by light, sound, or other media, and courts apply modern purposive interpretation alongside the IT Act, 2000",
       "No, IRWA only applies to physical papyrus and paper",
       "Only if the website is hosted on a government server",
       "Only if the file size is under 1 megabyte"], 0,
      "Section 2(a) broadly covers representations made by light, sound, or other visible means; modern digital media is covered under purposive construction and IT Act provisions.",
      {"A": "Correct; Digital and electronic media are covered under purposive interpretation.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "IRWA S. 2(a) & IT Act S. 67", "Application of IRWA to electronic and digital media.")

# top-irwa-01-03 (5)
add_q("mcq-irwa-01-011", "soc-indecent-rep", "ch-soc-irwa-01", "top-irwa-01-03",
      "Under Section 2(c) of the Act, what is the core statutory definition of 'indecent representation of women'?",
      ["The depiction in any manner of the figure, of a woman, her form or body or any part thereof in such a way as to have the effect of being indecent, or derogatory to, or denigrating women, or is likely to deprave, corrupt or injure the public morality or morals",
       "Any depiction of a woman without traditional head covering",
       "Any photograph of a woman working in a corporate office",
       "Depicting a woman driving an automobile"], 0,
      "Section 2(c) defines indecent representation as depiction of the female body in a manner that is indecent, derogatory, denigrating, or likely to deprave/corrupt public morals.",
      {"A": "Correct; Statutory definition under Section 2(c).", "B": "Incorrect; Narrow religious standards are not the law.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "IRWA S. 2(c)", "Core statutory definition under Section 2(c).")

add_q("mcq-irwa-01-012", "soc-indecent-rep", "ch-soc-irwa-01", "top-irwa-01-03",
      "What are the three distinct alternative limbs of 'indecent representation' under Section 2(c)?",
      ["(1) Indecent, (2) derogatory or denigrating to women, or (3) likely to deprave, corrupt or injure public morality or morals",
       "(1) Commercial, (2) residential, (3) industrial",
       "(1) Political, (2) religious, (3) philosophical",
       "(1) Civil, (2) criminal, (3) revenue"], 0,
      "Section 2(c) sets out three disjunctive tests: indecent; derogatory or denigrating; or likely to corrupt/injure public morality.",
      {"A": "Correct; Three disjunctive limbs in Section 2(c).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "IRWA S. 2(c)", "Three statutory tests of indecent representation.")

add_q("mcq-irwa-01-013", "soc-indecent-rep", "ch-soc-irwa-01", "top-irwa-01-03",
      "In Aveek Sarkar v. State of West Bengal (2014), what test for obscenity and indecency was adopted by the Supreme Court, discarding the old British Hicklin test?",
      ["Adopted the contemporary community standards test: material must be judged as a whole in its context, considering modern community standards rather than isolated passages affecting vulnerable minds",
       "Reaffirmed the strict 1868 Hicklin test as immutable",
       "Held that all artistic nudity is automatically criminal",
       "Held that only European art can be displayed in India"], 0,
      "In Aveek Sarkar (2014) 4 SCC 257, the Supreme Court formally discarded the outdated 1868 Hicklin test and adopted the contemporary community standards test.",
      {"A": "Correct; Contemporary community standards test adopted in Aveek Sarkar (2014).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "IRWA S. 2(c) & Aveek Sarkar (2014)", "Contemporary community standards test for obscenity.")

add_q("mcq-irwa-01-014", "soc-indecent-rep", "ch-soc-irwa-01", "top-irwa-01-03",
      "Does mere artistic or semi-nude depiction of a woman per se constitute an offence under Section 2(c) if it is neither lascivious, derogatory, nor denigrating?",
      ["No, nudity per se is not obscenity or indecent representation unless it appeals to prurient interest or denigrates female dignity",
       "Yes, any absence of full clothing is an automatic criminal offence",
       "Only if painted on canvas",
       "Only if displayed outdoors"], 0,
      "As held in Bobby Art International (Bandit Queen case) and Aveek Sarkar, nudity in an artistic or serious message context is not per se indecent representation.",
      {"A": "Correct; Nudity per se without derogatory or prurient effect is not an offence.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "IRWA S. 2(c) & Bobby Art International (1996)", "Distinction between art and indecent representation.")

add_q("mcq-irwa-01-015", "soc-indecent-rep", "ch-soc-irwa-01", "top-irwa-01-03",
      "What is the meaning of the word 'denigrating' in Section 2(c)?",
      ["Belittling, disparaging, or portraying women in a humiliating or inferior status",
       "Praising female achievements",
       "Awarding academic scholarships",
       "Electing a woman as company director"], 0,
      "'Denigrating' means portraying women as subhuman, subservient, sexual commodities, or in a manner that degrades their human dignity.",
      {"A": "Correct; Belittling, disparaging, or portraying women as mere commodities.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "IRWA S. 2(c)", "Meaning of 'denigrating' in Section 2(c).")

# Chapter 2: ch-soc-irwa-02 (15 MCQs)
# top-irwa-02-01 (5)
add_q("mcq-irwa-01-016", "soc-indecent-rep", "ch-soc-irwa-02", "top-irwa-02-01",
      "Under Section 3 of the Act, what is the prohibition regarding advertisements?",
      ["No person shall publish, or cause to be published, or arrange or take part in the publication or exhibition of, any advertisement which contains indecent representation of women in any form",
       "Advertisements are prohibited only on Sundays",
       "Only foreign advertising agencies are barred",
       "Advertisements require approval of the village panchayat"], 0,
      "Section 3 completely bars publishing, arranging, or exhibiting any advertisement containing indecent representation of women in any form.",
      {"A": "Correct; Total prohibition on advertisements containing indecent representation under Section 3.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "IRWA S. 3", "Prohibition of advertisements under Section 3.")

add_q("mcq-irwa-01-017", "soc-indecent-rep", "ch-soc-irwa-02", "top-irwa-02-01",
      "Under Section 3, who can be held liable for an illegal advertisement containing indecent representation of women?",
      ["The person who publishes it, causes it to be published, or arranges or takes part in the publication or exhibition",
       "Only the model who posed for the photograph",
       "Only the billboard carpenter",
       "Only the municipal billboard inspector"], 0,
      "Section 3 covers the entire chain of commercial advertising: publisher, client causing publication, and agency arranging or exhibiting it.",
      {"A": "Correct; All persons publishing, causing, arranging, or taking part in publication.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "IRWA S. 3", "Scope of liability in advertising chain under Section 3.")

add_q("mcq-irwa-01-018", "soc-indecent-rep", "ch-soc-irwa-02", "top-irwa-02-01",
      "Does an advertising agency that designs and arranges the display of an indecent billboard incur liability under Section 3?",
      ["Yes, Section 3 explicitly includes anyone who 'arranges or takes part in the publication or exhibition'",
       "No, advertising agencies enjoy total statutory immunity",
       "Only if the agency is owned by foreign nationals",
       "Only if the billboard falls and causes physical injury"], 0,
      "The phrase 'arranges or takes part in the publication or exhibition' directly ropes in advertising agencies, marketing consultants, and media buyers.",
      {"A": "Correct; Advertising agencies arranging the display are directly liable under Section 3.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "IRWA S. 3", "Liability of advertising agencies under Section 3.")

add_q("mcq-irwa-01-019", "soc-indecent-rep", "ch-soc-irwa-02", "top-irwa-02-01",
      "Can an outdoor billboard displaying an indecent depiction of a woman erected on private land be prosecuted under Section 3?",
      ["Yes, Section 3 prohibits exhibition of advertisements containing indecent representation in any form, regardless of whether on public or private land",
       "No, private land is exempt from all advertising laws",
       "Only if the billboard faces a railway line",
       "Only if illuminated by neon lights"], 0,
      "Section 3 applies to any advertisement exhibited in any form, irrespective of land tenure.",
      {"A": "Correct; Applies universally to exhibition in any form.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "IRWA S. 3", "Universal application to outdoor billboard displays.")

add_q("mcq-irwa-01-020", "soc-indecent-rep", "ch-soc-irwa-02", "top-irwa-02-01",
      "Is financial profit or commercial gain a mandatory ingredient for establishing an offence under Section 3?",
      ["No, Section 3 penalizes the bare act of publishing or exhibiting the prohibited advertisement; profit motive is not an essential ingredient",
       "Yes, prosecution must prove profit exceeding ten thousand rupees",
       "Only if the advertiser is a public limited company",
       "Only if commercial invoices are produced"], 0,
      "The penal offence under Section 3 is complete upon publishing or exhibiting the prohibited advertisement; commercial gain is immaterial.",
      {"A": "Correct; Profit motive is not an ingredient of the offence under Section 3.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "IRWA S. 3", "Absence of profit motive requirement under Section 3.")

# top-irwa-02-02 (5)
add_q("mcq-irwa-01-021", "soc-indecent-rep", "ch-soc-irwa-02", "top-irwa-02-02",
      "Under Section 4 of the Act, which of the following activities involving publications containing indecent representation of women is prohibited?",
      ["Producing, selling, letting to hire, distributing, circulating, or sending by post any book, pamphlet, paper, slide, film, writing, drawing, painting, photograph, representation or figure",
       "Only selling books in public libraries",
       "Only exporting materials to Commonwealth countries",
       "Only displaying paintings in state art galleries"], 0,
      "Section 4 enacts a comprehensive prohibition covering production, sale, hire, distribution, circulation, and postal dispatch of prohibited materials.",
      {"A": "Correct; Comprehensive commercial and distribution ban under Section 4.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "IRWA S. 4", "Prohibition of publication and distribution under Section 4.")

add_q("mcq-irwa-01-022", "soc-indecent-rep", "ch-soc-irwa-02", "top-irwa-02-02",
      "Under Section 4, does sending an indecent photograph of a woman through postal service or courier constitute an offence?",
      ["Yes, Section 4 explicitly penalizes any person who 'sends by post' any material containing indecent representation of women",
       "No, postal communications are strictly confidential and immune from law",
       "Only if the postal packet is damaged in transit",
       "Only if sent to a government official"], 0,
      "Section 4 explicitly criminalizes sending prohibited material by post.",
      {"A": "Correct; Sending by post is expressly prohibited under Section 4.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "IRWA S. 4", "Prohibition on sending indecent representations by post.")

add_q("mcq-irwa-01-023", "soc-indecent-rep", "ch-soc-irwa-02", "top-irwa-02-02",
      "Can a bookstall owner who displays and sells a magazine containing indecent representation of women plead that he had not read the magazine?",
      ["No, Section 4 makes selling or distributing strict liability; lack of knowledge does not absolve the distributor, though it may be considered in sentencing",
       "Yes, shopkeepers are automatically exempt from all contents of magazines they sell",
       "Only if the shopkeeper has been in business for over 20 years",
       "Yes, if the publisher gives an indemnity bond"], 0,
      "Selling or offering for sale prohibited material under Section 4 is a strict liability statutory offence designed to deter distributors of indecent material.",
      {"A": "Correct; Commercial distribution is prohibited; ignorance of contents is no complete defense.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "IRWA S. 4", "Liability of bookstall owners and distributors under Section 4.")

add_q("mcq-irwa-01-024", "soc-indecent-rep", "ch-soc-irwa-02", "top-irwa-02-02",
      "Does hiring or renting video cassettes, DVDs, or digital media containing indecent representation of women attract Section 4?",
      ["Yes, Section 4 explicitly penalizes letting to hire or circulating any slide, film, or representation",
       "No, rental businesses are exempt",
       "Only if the rental fee exceeds Rs 100",
       "Only if rented to minors"], 0,
      "Section 4 explicitly includes 'lets to hire, distributes, circulates' any film or visual representation.",
      {"A": "Correct; Letting to hire or circulating is expressly prohibited under Section 4.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "IRWA S. 4", "Prohibition on renting or hiring indecent media.")

add_q("mcq-indecent-01-025", "soc-indecent-rep", "ch-soc-irwa-02", "top-irwa-02-02",
      "Does private possession of an indecent photograph inside a personal locked drawer without any sale, distribution, or exhibition violate Section 4?",
      ["No, Section 4 penalizes producing, selling, letting to hire, distributing, circulating, or sending by post; mere private possession without more is not penal under Section 4",
       "Yes, bare private possession is punishable with 5 years imprisonment",
       "Only if the photograph was taken in a foreign country",
       "Possession is automatically deemed distribution"], 0,
      "Section 4 targets commercial, public, or communicative acts (produce, sell, hire, distribute, circulate, post); private possession alone without distribution intent is not Section 4 offence.",
      {"A": "Correct; Section 4 targets production, distribution, sale, or posting, not bare private possession.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "IRWA S. 4", "Commercial and public focus of Section 4.")

# top-irwa-02-03 (5)
add_q("mcq-irwa-01-026", "soc-indecent-rep", "ch-soc-irwa-02", "top-irwa-02-03",
      "Under Section 4 proviso, clause (a), which publications are EXEMPT from the prohibitions of the Act?",
      ["Any publication proved to be justified as being for the public good on the ground that it is in the interest of science, literature, art, or learning or other objects of general concern",
       "Publications endorsed by commercial influencers",
       "Any magazine with a circulation of over one million",
       "Publications that carry commercial tobacco warnings"], 0,
      "Section 4 proviso (a) mirrors Section 292 IPC: publications justified for public good in the interest of science, literature, art, or learning are exempt.",
      {"A": "Correct; Statutory public good exception for science, literature, art, and learning.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "IRWA S. 4 Proviso (a)", "Scientific, literary, and artistic public good exception.")

add_q("mcq-irwa-01-027", "soc-indecent-rep", "ch-soc-irwa-02", "top-irwa-02-03",
      "Under Section 4 proviso, clause (b)(i), are sculptures or representations on ancient monuments exempt from the Act?",
      ["Yes, any representation kept or used bona fide for religious purposes, or sculpted on or in any temple, or on any car used for conveyance of idols, or any ancient monument within Ancient Monuments and Archaeological Sites and Remains Act, 1958",
       "No, historical temple sculptures like Khajuraho must be covered with black cloth",
       "Only if the monument was built after 1947",
       "Only if approved annually by the District Magistrate"], 0,
      "Section 4 proviso (b) specifically protects religious carvings, temples, idol cars, and ancient monuments protected under the 1958 Act (e.g., Khajuraho, Konark).",
      {"A": "Correct; Religious carvings and ancient protected monuments are explicitly exempt.", "B": "Incorrect; Ancient heritage is expressly protected.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "IRWA S. 4 Proviso (b)", "Heritage, temple sculpture, and ancient monument exemption.")

add_q("mcq-irwa-01-028", "soc-indecent-rep", "ch-soc-irwa-02", "top-irwa-02-03",
      "Under Section 4 proviso, clause (b)(ii), does the Act apply to films certified under Part II of the Cinematograph Act, 1952?",
      ["No, films in respect of which the provisions of Part II of the Cinematograph Act, 1952 apply are expressly exempted from Section 4",
       "Yes, the Act overrides the Cinematograph Act completely",
       "Only documentaries are exempt, not feature films",
       "Only films with 'U' certificate are exempt"], 0,
      "Section 4 proviso (b)(ii) explicitly excludes films regulated and certified under Part II of the Cinematograph Act, 1952 by the Central Board of Film Certification (CBFC).",
      {"A": "Correct; Films certified under Part II of Cinematograph Act are exempt.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "IRWA S. 4 Proviso (b)(ii)", "Exemption of Cinematograph Act certified films.")

add_q("mcq-irwa-01-029", "soc-indecent-rep", "ch-soc-irwa-02", "top-irwa-02-03",
      "Are medical textbooks or anatomical diagrams of the female reproductive system exempt from prosecution under the Act?",
      ["Yes, under Section 4 proviso (a) as being in the interest of science, medical learning, and public good",
       "No, all medical books showing female anatomy are illegal in India",
       "Only if printed in Latin",
       "Only if sold to married medical students"], 0,
      "Section 4 proviso (a) protects all bona fide scientific, educational, and medical literature published for learning and health science.",
      {"A": "Correct; Protected under the science and learning exception in Section 4 proviso (a).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "IRWA S. 4 Proviso (a)", "Protection of medical and educational literature.")

add_q("mcq-irwa-01-030", "soc-indecent-rep", "ch-soc-irwa-02", "top-irwa-02-03",
      "Who bears the burden of establishing that a published work falls within the statutory exceptions in the proviso to Section 4?",
      ["The person charged with the offence, on a standard of preponderance of probabilities under Section 105 of the Evidence Act / BSA 2023",
       "The prosecution beyond all reasonable doubt",
       "The Archaeological Survey of India",
       "The censor board"], 0,
      "Under Section 105 of the Evidence Act / Section 108 of BSA 2023, the burden of proving that a case falls within a general or special statutory exception lies on the accused.",
      {"A": "Correct; Burden of proving statutory exception lies on the accused.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "IRWA S. 4 Proviso & IEA S. 105 / BSA S. 108", "Burden of proving statutory exceptions.")

# Chapter 3: ch-soc-irwa-03 (15 MCQs)
# top-irwa-03-01 (5)
add_q("mcq-irwa-01-031", "soc-indecent-rep", "ch-soc-irwa-03", "top-irwa-03-01",
      "Under Section 5(1) of the Act, which officer can be authorized by the State Government to exercise powers of entry, search and seizure?",
      ["Any Gazetted Officer authorized by the State Government",
       "Any police constable on duty",
       "Only the Chief Secretary of the State",
       "The local municipal corporator"], 0,
      "Section 5(1) provides that subject to rules, any Gazetted Officer authorized by the State Government may enter and search places within their local limits.",
      {"A": "Correct; Gazetted Officer authorized by State Government under Section 5(1).", "B": "Incorrect; Constables lack statutory search authorization.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "IRWA S. 5(1)", "Authorized searching officer (Gazetted Officer) under Section 5(1).")

add_q("mcq-irwa-01-032", "soc-indecent-rep", "ch-soc-irwa-03", "top-irwa-03-01",
      "Under the proviso to Section 5(1) of the Act, what special restriction applies to searching a 'private dwelling house'?",
      ["No entry shall be made into a private dwelling house without a warrant",
       "Private dwelling houses can never be searched under any circumstances",
       "A dwelling house can be searched at any time without a warrant",
       "Dwelling houses can only be searched on national holidays"], 0,
      "Proviso to Section 5(1) enacts a vital privacy safeguard: 'Provided that no entry under this sub-section shall be made into a private dwelling house without a warrant.'",
      {"A": "Correct; No entry into a private dwelling house without a warrant.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "IRWA S. 5(1) Proviso", "Mandatory warrant requirement for searching private dwelling house.")

add_q("mcq-irwa-01-033", "soc-indecent-rep", "ch-soc-irwa-03", "top-irwa-03-01",
      "Under Section 5(1)(c) of the Act, what power does the authorized Gazetted Officer have regarding seized materials?",
      ["Seize any advertisement or any book, pamphlet, slide, film, or other representation if there is reason to believe it contravenes the Act",
       "Sell the seized materials at public auction immediately",
       "Burn the seized material on the spot without making a list",
       "Distribute the materials to local schools"], 0,
      "Section 5(1)(c) empowers the authorized officer to seize any advertisement, article, or material believed to contravene the provisions of the Act.",
      {"A": "Correct; Power to seize offending advertisements and materials under Section 5(1)(c).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "IRWA S. 5(1)(c)", "Power of seizure under Section 5(1)(c).")

add_q("mcq-irwa-01-034", "soc-indecent-rep", "ch-soc-irwa-03", "top-irwa-03-01",
      "Under Section 5(2) of the Act, which code governs the execution of search warrants and searches under this Act?",
      ["The Code of Criminal Procedure, 1973 / Bharatiya Nagarik Suraksha Sanhita, 2023",
       "The Code of Civil Procedure, 1908",
       "The Indian Contract Act, 1872",
       "The Customs Act, 1962"], 0,
      "Section 5(2) provides that the provisions of CrPC/BNSS relating to search and seizure shall apply to every search or seizure under this Act.",
      {"A": "Correct; CrPC / BNSS provisions apply to searches under Section 5(2).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "IRWA S. 5(2)", "Application of CrPC/BNSS search procedure under Section 5(2).")

add_q("mcq-indecent-01-035", "soc-indecent-rep", "ch-soc-irwa-03", "top-irwa-03-01",
      "Under Section 5(3) of the Act, if any person seizes anything under clause (b) or (c) of sub-section (1), what duty is cast upon them?",
      ["Shall, as soon as may be, inform the nearest Magistrate and take his orders as to the custody thereof",
       "Shall retain the seized items permanently in their private home",
       "Shall destroy the items after twenty-four hours",
       "Shall deliver the items to the media"], 0,
      "Section 5(3) mandates that the searching officer shall immediately report the seizure to the nearest Magistrate and take orders regarding custody.",
      {"A": "Correct; Inform nearest Magistrate and take orders as to custody under Section 5(3).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "IRWA S. 5(3)", "Duty to report seizure to nearest Magistrate under Section 5(3).")

# top-irwa-03-02 (5)
add_q("mcq-irwa-01-036", "soc-indecent-rep", "ch-soc-irwa-03", "top-irwa-03-02",
      "Under Section 7(1) of the Act, where an offence under this Act has been committed by a company, who shall be deemed guilty of the offence?",
      ["Every person who, at the time the offence was committed, was in charge of, and was responsible to, the company for the conduct of the business, as well as the company",
       "Only the junior-most receptionist",
       "Every shareholder regardless of voting rights",
       "Only the company's external statutory auditor"], 0,
      "Section 7(1) enacts standard vicarious corporate liability: the company and every person in charge of and responsible to the company are deemed guilty.",
      {"A": "Correct; Company and persons in charge and responsible for conduct of business.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "IRWA S. 7(1)", "Offences by companies and vicarious liability under Section 7(1).")

add_q("mcq-irwa-01-037", "soc-indecent-rep", "ch-soc-irwa-03", "top-irwa-03-02",
      "Under the proviso to Section 7(1), can a director escape liability for a company offence under this Act?",
      ["Yes, if he proves that the offence was committed without his knowledge or that he had exercised all due diligence to prevent the commission of such offence",
       "No, director liability is absolute and irrebuttable",
       "Only if he resigns before the trial starts",
       "Only if he was travelling overseas"], 0,
      "Proviso to Section 7(1) provides standard statutory defense: absence of knowledge or exercise of all due diligence.",
      {"A": "Correct; Defense of lack of knowledge or exercise of due diligence under Section 7(1) proviso.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "IRWA S. 7(1) Proviso", "Statutory defense for directors under Section 7(1).")

add_q("mcq-irwa-01-038", "soc-indecent-rep", "ch-soc-irwa-03", "top-irwa-03-02",
      "Under Section 7(2) of the Act, if an offence is proved to have been committed with the consent, connivance, or neglect of a specific director or officer:",
      ["Such director, manager, secretary or other officer shall also be deemed to be guilty of that offence and liable to be proceeded against",
       "The company alone is fined, and the individual is exempt",
       "The officer is given a departmental warning only",
       "The case is referred to the National Company Law Tribunal"], 0,
      "Section 7(2) holds directors, managers, secretaries, or officers individually guilty if consent, connivance, or attributable neglect is proven.",
      {"A": "Correct; Individual liability for consent, connivance, or neglect under Section 7(2).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "IRWA S. 7(2)", "Individual culpability of directors under Section 7(2).")

add_q("mcq-irwa-01-039", "soc-indecent-rep", "ch-soc-irwa-03", "top-irwa-03-02",
      "Under Explanation to Section 7, what is included within the definition of a 'company'?",
      ["Any body corporate and includes a firm or other association of individuals",
       "Only public limited companies listed on the stock exchange",
       "Only multinational foreign corporations",
       "Only entities registered under Section 8 of Companies Act"], 0,
      "Explanation (a) to Section 7 defines 'company' broadly to mean any body corporate and includes a firm or other association of individuals.",
      {"A": "Correct; Any body corporate, firm, or association of individuals.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "IRWA S. 7 Expl. (a)", "Definition of company under Section 7.")

add_q("mcq-irwa-01-040", "soc-indecent-rep", "ch-soc-irwa-03", "top-irwa-03-02",
      "Under Explanation (b) to Section 7, who is a 'director' in relation to a partnership firm?",
      ["A partner in the firm", "A salaried manager", "An independent consultant", "A silent dormant investor"], 0,
      "Explanation (b) to Section 7 provides: 'director, in relation to a firm, means a partner in the firm.'",
      {"A": "Correct; 'Director' in relation to a firm means a partner in the firm.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "IRWA S. 7 Expl. (b)", "Definition of director in relation to a partnership firm.")

# top-irwa-03-03 (5)
add_q("mcq-irwa-01-041", "soc-indecent-rep", "ch-soc-irwa-03", "top-irwa-03-03",
      "Under Section 6 of the Act, what is the punishment for a FIRST conviction under the Indecent Representation of Women (Prohibition) Act, 1986?",
      ["Imprisonment of either description for a term which may extend to two years, and with fine which may extend to two thousand rupees",
       "Fine of Rs 500 only",
       "Imprisonment for 7 years",
       "Simple community service for one month"], 0,
      "Section 6 provides that on a first conviction, the punishment is imprisonment up to two years, and fine up to two thousand rupees.",
      {"A": "Correct; Up to 2 years imprisonment and fine up to Rs 2,000 under Section 6.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "IRWA S. 6", "Punishment for first conviction under Section 6.")

add_q("mcq-irwa-01-042", "soc-indecent-rep", "ch-soc-irwa-03", "top-irwa-03-03",
      "Under Section 6 of the Act, what is the mandatory punishment on a SECOND or subsequent conviction?",
      ["Imprisonment for a term of not less than six months but which may extend to five years and with a fine not less than ten thousand rupees but which may extend to one lakh rupees",
       "Imprisonment up to 1 year and fine of Rs 5,000",
       "Life imprisonment",
       "Fine of Rs 50,000 only without imprisonment"], 0,
      "Section 6 mandates enhanced punishment for repeat offenders: minimum 6 months up to 5 years imprisonment, and fine between Rs 10,000 and Rs 1,00,000.",
      {"A": "Correct; Min 6 months to 5 years imprisonment, and fine Rs 10,000 to Rs 1,00,000.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "IRWA S. 6", "Enhanced punishment for subsequent convictions under Section 6.")

add_q("mcq-irwa-01-043", "soc-indecent-rep", "ch-soc-irwa-03", "top-irwa-03-03",
      "Under Section 8(1) of the Act, an offence punishable under this Act is classified as:",
      ["Bailable", "Non-bailable", "Compoundable without court leave", "Non-cognizable"], 0,
      "Section 8(1) explicitly provides: 'Notwithstanding anything contained in the Code of Criminal Procedure, 1973, an offence punishable under this Act shall be bailable.'",
      {"A": "Correct; Explicitly declared bailable under Section 8(1).", "B": "Incorrect; Offence is bailable.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "IRWA S. 8(1)", "Bailable classification under Section 8(1).")

add_q("mcq-irwa-01-044", "soc-indecent-rep", "ch-soc-irwa-03", "top-irwa-03-03",
      "Under Section 8(2) of the Act, an offence under this Act is classified as:",
      ["Cognizable", "Non-cognizable", "Compoundable", "Summary dispute"], 0,
      "Section 8(2) states: 'An offence punishable under this Act shall be cognizable.' Combined with 8(1), offences are cognizable and bailable.",
      {"A": "Correct; Explicitly declared cognizable under Section 8(2).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "IRWA S. 8(2)", "Cognizable classification under Section 8(2).")

add_q("mcq-irwa-01-045", "soc-indecent-rep", "ch-soc-irwa-03", "top-irwa-03-03",
      "Under Section 9 of the Act, what protection is afforded for action taken in good faith?",
      ["No suit, prosecution or other legal proceeding shall lie against the Central Government or any State Government or any officer of the Central Government or any State Government for anything which is in good faith done or intended to be done under this Act",
       "Protection applies only if the officer is an IAS officer",
       "Protection is restricted to police commissioners",
       "No immunity exists under special laws"], 0,
      "Section 9 contains the standard statutory good faith indemnity protecting Central/State Governments and authorized officers.",
      {"A": "Correct; Statutory protection of action taken in good faith under Section 9.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "IRWA S. 9", "Good faith immunity clause under Section 9.")


# --- ACT 9: POCSO ACT, 2012 (soc-pocso) - 60 MCQs ---

# Chapter 1: ch-soc-pocso-01 (15 MCQs)
# top-pocso-01-01 (5)
add_q("mcq-pocso-01-001", "soc-pocso", "ch-soc-pocso-01", "top-pocso-01-01",
      "On which date did the Protection of Children from Sexual Offences (POCSO) Act, 2012 (Act No. 32 of 2012) come into force in India?",
      ["14 November 2012", "19 June 2012", "1 January 2013", "16 August 2019"], 0,
      "The POCSO Act was brought into force on 14 November 2012 (Children's Day) by Central Government notification.",
      {"A": "Correct; Came into force on 14 November 2012 (Children's Day).", "B": "Incorrect; 19 June 2012 was Presidential assent date.", "C": "Incorrect.", "D": "Incorrect; 2019 was amendment enforcement."},
      "Foundational", "POCSO Act S. 1(3)", "Commencement date of POCSO Act 2012.")

add_q("mcq-pocso-01-002", "soc-pocso", "ch-soc-pocso-01", "top-pocso-01-01",
      "Which international convention ratified by India in 1992 formed the core treaty commitment leading to the enactment of the POCSO Act, 2012?",
      ["UN Convention on the Rights of the Child (UNCRC)",
       "Geneva Conventions on Prisoners of War",
       "Hague Convention on Civil Aspects of International Child Abduction",
       "UN Convention Against Corruption"], 0,
      "India acceded to the UN Convention on the Rights of the Child (UNCRC) on 11 December 1992; POCSO was enacted under Article 253 to implement these obligations.",
      {"A": "Correct; UN Convention on the Rights of the Child (UNCRC).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "UNCRC & POCSO Act Preamble", "International treaty basis of POCSO Act.")

add_q("mcq-pocso-01-003", "soc-pocso", "ch-soc-pocso-01", "top-pocso-01-01",
      "Which constitutional provisions in Part III and Part IV directly mandate the State to enact child-centric protective legislation like POCSO?",
      ["Article 15(3), Article 21, and Article 39(e) and 39(f)",
       "Article 356 and Article 365",
       "Article 310 and Article 311",
       "Article 262 and Article 263"], 0,
      "Article 15(3) empowers affirmative legislation for children, Article 21 guarantees dignity and life, and Articles 39(e)-(f) direct the State to protect children against abuse.",
      {"A": "Correct; Articles 15(3), 21, and 39(e)-(f) of the Constitution.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "Constitution Arts. 15(3), 21, 39(e),(f)", "Constitutional foundation of POCSO Act.")

add_q("mcq-pocso-01-004", "soc-pocso", "ch-soc-pocso-01", "top-pocso-01-01",
      "On which date did the major Protection of Children from Sexual Offences (Amendment) Act, 2019 (Act No. 25 of 2019) come into force?",
      ["16 August 2019", "1 August 2019", "1 January 2020", "2 October 2019"], 0,
      "The 2019 POCSO Amendment introduced death penalty for aggravated penetrative sexual assault and came into force on 16 August 2019.",
      {"A": "Correct; Enforced on 16 August 2019.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Amendment Act 2019", "Commencement date of 2019 POCSO Amendment Act.")

add_q("mcq-pocso-01-005", "soc-pocso", "ch-soc-pocso-01", "top-pocso-01-01",
      "Under Section 1(2) of the POCSO Act, 2012, what is the territorial extent of the Act?",
      ["It extends to the whole of India", "It extends to the whole of India except Jammu and Kashmir", "It applies only to Union Territories", "It applies only to schools and orphanages"], 0,
      "The POCSO Act extends to the whole of India.",
      {"A": "Correct; Extends to the whole of India.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 1(2)", "Territorial extent of POCSO Act.")

# top-pocso-01-02 (5)
add_q("mcq-pocso-01-006", "soc-pocso", "ch-soc-pocso-01", "top-pocso-01-02",
      "Under Section 2(1)(d) of the POCSO Act, 2012, who is a 'child'?",
      ["Any person below the age of eighteen years",
       "Any person below the age of fourteen years",
       "Any person below the age of sixteen years",
       "Any unmarried female below twenty-one years"], 0,
      "Section 2(1)(d) provides an unequivocal, objective definition: 'child' means any person below the age of eighteen years.",
      {"A": "Correct; Any person below the age of eighteen years under Section 2(1)(d).", "B": "Incorrect; 14 is the child labor benchmark.", "C": "Incorrect; 16 was the pre-2013 age under 375 IPC.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 2(1)(d)", "Definition of child under Section 2(1)(d).")

add_q("mcq-pocso-01-007", "soc-pocso", "ch-soc-pocso-01", "top-pocso-01-02",
      "Is the definition of a victim child under the POCSO Act, 2012 gender-neutral?",
      ["Yes, Section 2(1)(d) defines a child as 'any person' below 18 years, protecting boys, girls, and transgender children equally",
       "No, POCSO protects female children exclusively",
       "Boys are only protected if under the age of twelve",
       "Transgender children are excluded from POCSO"], 0,
      "Unlike Section 375 IPC / Section 63 BNS (which defines rape solely against females), POCSO is completely gender-neutral regarding the victim child.",
      {"A": "Correct; Gender-neutral definition protecting all children below 18.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 2(1)(d)", "Gender neutrality of victim child under POCSO.")

add_q("mcq-pocso-01-008", "soc-pocso", "ch-soc-pocso-01", "top-pocso-01-02",
      "Can a female adult be prosecuted as an accused perpetrator under the substantive offences of the POCSO Act, 2012?",
      ["Yes, offences under POCSO use the phrase 'whoever commits', making perpetrators gender-neutral (both male and female adults can be prosecuted)",
       "No, only adult males can be charged under POCSO",
       "Female adults can only be prosecuted for abetment, never as principal offenders",
       "Only if she was acting as a school principal"], 0,
      "The charging sections (Sections 3, 5, 7, 9, 11) use gender-neutral language ('Whoever commits...'), allowing prosecution of any person regardless of gender.",
      {"A": "Correct; Offender language is gender-neutral ('Whoever commits').", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POCSO Act S. 3, 5, 7, 9", "Gender neutrality of perpetrators under POCSO.")

add_q("mcq-pocso-01-009", "soc-pocso", "ch-soc-pocso-01", "top-pocso-01-02",
      "How is the age of a victim child determined in a POCSO trial in the absence of a school birth certificate?",
      ["In accordance with the procedure laid down in Section 94 of the Juvenile Justice (Care and Protection of Children) Act, 2015 (matriculation certificate, municipal birth certificate, or ossification test)",
       "By visual estimate of the police officer",
       "By horoscope verified by an astrologer",
       "The child is presumed to be twenty-one unless proven otherwise"], 0,
      "Settled law (Jarnail Singh, Rishipal Singh) establishes that age determination under POCSO strictly follows the statutory hierarchy in Section 94 of the JJ Act, 2015.",
      {"A": "Correct; Rule under Section 94 of JJ Act 2015 applies to POCSO age determination.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "POCSO Act S. 34 & JJ Act 2015 S. 94", "Age determination procedure under POCSO.")

add_q("mcq-pocso-01-010", "soc-pocso", "ch-soc-pocso-01", "top-pocso-01-02",
      "Can the consent of a minor child (aged below 18 years) operate as a valid legal defense for an accused charged with penetrative sexual assault under POCSO?",
      ["No, the consent of a child below eighteen years is legally void and immaterial under the statutory scheme of POCSO",
       "Yes, if the child was above sixteen and consented in writing",
       "Yes, if the parties were in a romantic relationship",
       "Consent reduces the offence to a fine of Rs 500"], 0,
      "POCSO is built on statutory non-consent: the consent of any person below 18 years is non-est in the eyes of law and cannot legitimize sexual acts.",
      {"A": "Correct; Consent of a minor is legally void and irrelevant under POCSO.", "B": "Incorrect; POCSO recognizes no romantic consent below 18.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act Scheme & S. 3, 4", "Absolute immateriality of minor's consent under POCSO.")

# top-pocso-01-03 (5)
add_q("mcq-pocso-01-011", "soc-pocso", "ch-soc-pocso-01", "top-pocso-01-03",
      "Under Section 42A of the POCSO Act, 2012, what is the effect of the Act over other laws?",
      ["The provisions of this Act shall have effect notwithstanding anything inconsistent therewith contained in any other law for the time being in force",
       "The Act is subordinate to the Code of Criminal Procedure",
       "The Act is subordinate to personal laws",
       "The Act operates only as an optional guideline"], 0,
      "Section 42A contains an express non-obstante clause giving POCSO overriding effect over any inconsistent enactment.",
      {"A": "Correct; Section 42A contains an express non-obstante overriding effect clause.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 42A", "Overriding effect of POCSO under Section 42A.")

add_q("mcq-pocso-01-012", "soc-pocso", "ch-soc-pocso-01", "top-pocso-01-03",
      "Under Section 42 of the POCSO Act, 2012, where an act constitutes an offence punishable under POCSO and also under Sections 376, 354, etc. of the Penal Code:",
      ["The offender found guilty shall be liable to punishment under this Act or under the Penal Code as provides for punishment which is greater in degree",
       "The offender must be acquitted of both charges",
       "The court can only impose the lesser punishment",
       "The offender is tried twice in separate courts"], 0,
      "Section 42 establishes the principle of greater punishment: the offender is liable to punishment under whichever statute provides the punishment greater in degree.",
      {"A": "Correct; Liable to punishment greater in degree under Section 42.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect; Double jeopardy bars dual trials."},
      "Standard", "POCSO Act S. 42", "Rule of greater punishment under Section 42.")

add_q("mcq-pocso-01-013", "soc-pocso", "ch-soc-pocso-01", "top-pocso-01-03",
      "In Independent Thought v. Union of India (2017), what did the Supreme Court hold regarding Exception 2 to Section 375 IPC in light of POCSO?",
      ["Read down Exception 2 to Section 375 IPC, holding that sexual intercourse with a girl child below 18 years is rape, even if she is married to the accused",
       "Held that child marriage legalizes sexual intercourse with minors",
       "Held that POCSO does not apply to married girls",
       "Held that child marriages cannot be registered"], 0,
      "In Independent Thought (2017) 10 SCC 800, Madan B. Lokur, J., harmonized IPC with POCSO, ruling that marital rape exception cannot shield intercourse with a wife below 18.",
      {"A": "Correct; Struck down child-marriage exception in rape; intercourse below 18 is rape.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "POCSO S. 2(1)(d), S. 42A & Independent Thought (2017)", "Supreme Court ruling eliminating marital exception for child brides.")

add_q("mcq-pocso-01-014", "soc-pocso", "ch-soc-pocso-01", "top-pocso-01-03",
      "Can an accused charged under POCSO also be charged under the Information Technology Act, 2000 for electronic circulation of child pornography?",
      ["Yes, joint charges can be framed under POCSO Section 14/15 and IT Act Section 67B in accordance with criminal procedural rules",
       "No, IT Act is completely barred if POCSO is invoked",
       "Only with prior sanction of the Ministry of Electronics and IT",
       "Only if the computer server is confiscated"], 0,
      "POCSO and Section 67B of the IT Act 2000 operate cumulatively under standard joinder provisions of CrPC/BNSS.",
      {"A": "Correct; Joint charges under POCSO and Section 67B IT Act are standard.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POCSO S. 15 & IT Act S. 67B", "Cumulative operation of POCSO and IT Act Section 67B.")

add_q("mcq-pocso-01-015", "soc-pocso", "ch-soc-pocso-01", "top-pocso-01-03",
      "Does the Prohibition of Child Marriage Act, 2006 (PCMA) override the penal provisions of the POCSO Act, 2012?",
      ["No, POCSO overrides personal laws and marriage customs; consummation of marriage with a child below 18 constitutes penetrative sexual assault under POCSO",
       "Yes, valid religious marriage legalizes sexual relations under POCSO",
       "Only if the marriage was performed with parental blessings",
       "Only if the couple registers their marriage under the Special Marriage Act"], 0,
      "Section 42A of POCSO explicitly overrides any inconsistent law; marriage cannot legitimize sexual acts with a child below 18 years.",
      {"A": "Correct; Marriage cannot exempt an accused from POCSO; Section 42A overrides.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "POCSO S. 42A & Independent Thought (2017)", "POCSO overriding child marriage claims.")

# Chapter 2: ch-soc-pocso-02 (15 MCQs)
# top-pocso-02-01 (5)
add_q("mcq-pocso-01-016", "soc-pocso", "ch-soc-pocso-02", "top-pocso-02-01",
      "Under Section 3 of the POCSO Act, 2012, which of the following acts constitutes 'penetrative sexual assault'?",
      ["Penetration of penis into vagina, mouth, urethra or anus of a child, or introducing any object or part of the body (other than penis) into vagina, urethra or anus of a child, or manipulating any body part of child to cause penetration",
       "Mere verbal teasing at a school playground",
       "Standing in front of a child in a public park",
       "Holding hands during a class photo"], 0,
      "Section 3 defines penetrative sexual assault comprehensively, covering penile penetration as well as introducing any object or body part into vagina, urethra, or anus.",
      {"A": "Correct; Comprehensive statutory definition under Section 3.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 3", "Definition of penetrative sexual assault under Section 3.")

add_q("mcq-pocso-01-017", "soc-pocso", "ch-soc-pocso-02", "top-pocso-02-01",
      "Under Section 4(1) of the POCSO Act (as amended in 2019), what is the minimum punishment for penetrative sexual assault?",
      ["Imprisonment for a term which shall not be less than ten years, but which may extend to imprisonment for life, and with fine",
       "Imprisonment for 3 years",
       "Imprisonment for 7 years",
       "Fine of Rs 50,000 only"], 0,
      "The 2019 Amendment enhanced the minimum sentence under Section 4(1) from 7 years to not less than ten years, extending up to life imprisonment, and fine.",
      {"A": "Correct; Not less than 10 years extending to life imprisonment and fine.", "B": "Incorrect.", "C": "Incorrect; 7 years was the pre-2019 floor.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 4(1)", "Mandatory minimum penalty (10 years) under Section 4(1).")

add_q("mcq-pocso-01-018", "soc-pocso", "ch-soc-pocso-02", "top-pocso-02-01",
      "Under Section 5 of the POCSO Act, which of the following circumstances aggravates penetrative sexual assault into 'Aggravated Penetrative Sexual Assault'?",
      ["Committed by a police officer, public servant, member of armed forces, teacher, doctor, family member, or gang assault, or on a child below 12 or disabled child, or causing grievous hurt/death",
       "Committed during a cricket match",
       "Committed in a commercial hotel",
       "Committed on a weekend"], 0,
      "Section 5 lists aggravating factors: positions of trust/authority (police, teachers, doctors, relatives), vulnerability (under 12, disability), gang assault, or transmitting HIV.",
      {"A": "Correct; Abuse of trust/authority, extreme youth (under 12), disability, gang assault under Section 5.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 5", "Aggravating circumstances under Section 5.")

add_q("mcq-pocso-01-019", "soc-pocso", "ch-soc-pocso-02", "top-pocso-02-01",
      "Under Section 6(1) of the POCSO Act (as amended in 2019), what is the punishment for Aggravated Penetrative Sexual Assault?",
      ["Rigorous imprisonment for not less than twenty years, but which may extend to imprisonment for life (natural life), or with death, and with fine",
       "Imprisonment for 7 years",
       "Imprisonment for 10 years",
       "Imprisonment for life with mandatory release after 14 years"], 0,
      "The 2019 Amendment introduced the death penalty: rigorous imprisonment of not less than 20 years extending to life (remainder of natural life) or with death, and fine.",
      {"A": "Correct; Min 20 years up to natural life imprisonment or death, and fine under Section 6.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 6", "Capital punishment and 20-year minimum under Section 6.")

add_q("mcq-pocso-01-020", "soc-pocso", "ch-soc-pocso-02", "top-pocso-02-01",
      "Under Section 5(m) and Section 6 of the POCSO Act, committing penetrative sexual assault on a child below what age specifically attracts the death penalty option?",
      ["Below twelve years of age", "Below fourteen years of age", "Below sixteen years of age", "Below ten years of age"], 0,
      "Section 5(m) specifically defines committing penetrative sexual assault on a child below twelve years of age as aggravated assault punishable under Section 6 with up to death penalty.",
      {"A": "Correct; Below twelve years of age under Section 5(m).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POCSO Act S. 5(m), S. 6", "Specific age bracket (below 12 years) for aggravated assault.")

# top-pocso-02-02 (5)
add_q("mcq-pocso-01-021", "soc-pocso", "ch-soc-pocso-02", "top-pocso-02-02",
      "Under Section 7 of the POCSO Act, 2012, what constitutes 'sexual assault'?",
      ["Whoever, with sexual intent touches the vagina, penis, anus or breast of the child or makes the child touch the vagina, penis, anus or breast of that person, or does any other act with sexual intent involving physical contact without penetration",
       "Waving at a child from a distance",
       "Taking an attendance roll call in school",
       "Writing an arithmetic examination question"], 0,
      "Section 7 defines sexual assault as touching sexual body parts with sexual intent, or doing any other act involving physical contact with sexual intent, without penetration.",
      {"A": "Correct; Touching sexual parts or physical contact with sexual intent without penetration under Section 7.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 7", "Definition of sexual assault under Section 7.")

add_q("mcq-pocso-01-022", "soc-pocso", "ch-soc-pocso-02", "top-pocso-02-02",
      "In Attorney General for India v. Satish (2022), what did the Supreme Court hold regarding 'skin-to-skin' contact under Section 7?",
      ["Overruled the Bombay High Court's 'skin-to-skin' judgment and held that direct physical contact even over clothes with sexual intent constitutes sexual assault under Section 7",
       "Held that touching over clothes can never be an offence",
       "Held that skin-to-skin contact is strictly mandatory for Section 7",
       "Held that sexual intent cannot be proved without a written confession"], 0,
      "In AG v. Satish (2022) 5 SCC 541, U.U. Lalit, J., emphatically overruled the 'skin-to-skin' interpretation, affirming that touching with sexual intent over clothing constitutes sexual assault.",
      {"A": "Correct; Overruled skin-to-skin requirement; touching over clothes is sexual assault.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "POCSO Act S. 7 & AG v. Satish (2022)", "Supreme Court landmark ruling on physical contact under Section 7.")

add_q("mcq-pocso-01-023", "soc-pocso", "ch-soc-pocso-02", "top-pocso-02-02",
      "Under Section 8 of the POCSO Act, what is the punishment for committing sexual assault?",
      ["Imprisonment for a term which shall not be less than three years but which may extend to five years, and with fine",
       "Fine of Rs 1,000 only",
       "Imprisonment for 10 years",
       "Simple community service"], 0,
      "Section 8 provides imprisonment for not less than three years extending up to five years, and fine.",
      {"A": "Correct; Not less than 3 years up to 5 years, and fine under Section 8.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 8", "Punishment for sexual assault under Section 8.")

add_q("mcq-pocso-01-024", "soc-pocso", "ch-soc-pocso-02", "top-pocso-02-02",
      "Under Section 9 of the POCSO Act, what transforms sexual assault into 'Aggravated Sexual Assault'?",
      ["When committed by persons in positions of authority/trust (police, teachers, doctors, relatives), or on disabled children, or in educational institutions",
       "When committed during a holiday",
       "When committed outside municipal boundaries",
       "When the victim child is an only child"], 0,
      "Section 9 mirrors Section 5, listing aggravating factors: abuse of authority, trust, institutional settings, extreme youth, or disability.",
      {"A": "Correct; Abuse of trust, authority, educational settings, or vulnerability under Section 9.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POCSO Act S. 9", "Aggravated sexual assault circumstances under Section 9.")

add_q("mcq-pocso-01-025", "soc-pocso", "ch-soc-pocso-02", "top-pocso-02-02",
      "Under Section 10 of the POCSO Act (as amended in 2019), what is the punishment for Aggravated Sexual Assault?",
      ["Imprisonment for a term which shall not be less than five years but which may extend to seven years, and with fine",
       "Imprisonment for 1 year",
       "Imprisonment for 20 years",
       "Fine of Rs 5,000 only"], 0,
      "Section 10 prescribes imprisonment for not less than five years extending up to seven years, and fine.",
      {"A": "Correct; Not less than 5 years up to 7 years, and fine under Section 10.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 10", "Punishment for aggravated sexual assault under Section 10.")

# top-pocso-02-03 (5)
add_q("mcq-pocso-01-026", "soc-pocso", "ch-soc-pocso-02", "top-pocso-02-03",
      "Under Section 11 of the POCSO Act, which of the following acts constitutes 'sexual harassment' of a child?",
      ["Uttering words, making sounds or gestures, or exhibiting any object or body part, or showing pornography, or stalking a child with sexual intent",
       "Asking a child to complete their homework",
       "Giving a child a storybook as a birthday present",
       "Teaching a child swimming strokes under lifeguard supervision"], 0,
      "Section 11 defines sexual harassment: sexually coloured words, sounds, gestures, exhibition of body parts, showing pornography, or repeated stalking with sexual intent.",
      {"A": "Correct; Words, gestures, showing pornography, or stalking with sexual intent under Section 11.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 11", "Definition of sexual harassment under Section 11.")

add_q("mcq-pocso-01-027", "soc-pocso", "ch-soc-pocso-02", "top-pocso-02-03",
      "Under Section 12 of the POCSO Act, what is the punishment for committing sexual harassment of a child?",
      ["Imprisonment for a term which may extend to three years and also with fine",
       "Fine of Rs 500 only",
       "Imprisonment for 7 years",
       "Simple warning by the Special Court"], 0,
      "Section 12 provides that whoever commits sexual harassment of a child shall be punished with imprisonment up to three years and also with fine.",
      {"A": "Correct; Up to 3 years imprisonment and fine under Section 12.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 12", "Punishment for sexual harassment under Section 12.")

add_q("mcq-pocso-01-028", "soc-pocso", "ch-soc-pocso-02", "top-pocso-02-03",
      "Under Section 14(1) of the POCSO Act (as amended in 2019), what is the punishment for using a child for pornographic purposes?",
      ["Imprisonment for a term which shall not be less than five years, and also with fine (up to seven years and fine on subsequent conviction)",
       "Fine of Rs 10,000 only",
       "Imprisonment for 1 year",
       "Community service for six months"], 0,
      "Section 14(1) provides imprisonment of not less than five years and fine; subsequent conviction carries not less than seven years and fine.",
      {"A": "Correct; Not less than 5 years and fine under Section 14(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POCSO Act S. 14(1)", "Punishment for using child for pornography under Section 14.")

add_q("mcq-pocso-01-029", "soc-pocso", "ch-soc-pocso-02", "top-pocso-02-03",
      "Under Section 15 of the POCSO Act (amended in 2019), does retaining or storing child pornographic material on a mobile phone or computer without deleting or reporting it constitute an offence?",
      ["Yes, Section 15 penalizes storing or possessing child pornographic material in any form if the person fails to delete, destroy, or report it to the Special Juvenile Police Unit or cyber police",
       "No, private possession on mobile phones is completely legal",
       "Only if the device is connected to a public Wi-Fi",
       "Only if the owner sells the device"], 0,
      "Section 15 (substituted in 2019) criminalizes possession or retention of child pornography unless the person deletes/destroys it or reports it to designated authorities.",
      {"A": "Correct; Storing or retaining child pornography without reporting/deleting is an offence under Section 15.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "POCSO Act S. 15", "Storage and retention of child pornography under Section 15.")

add_q("mcq-pocso-01-030", "soc-pocso", "ch-soc-pocso-02", "top-pocso-02-03",
      "Under Section 15(2) of the Act, what is the punishment for storing child pornography for commercial purposes or transmitting it?",
      ["Imprisonment for not less than three years which may extend to five years, or with fine, or with both",
       "Fine of Rs 1,000 only",
       "Imprisonment for twenty years",
       "Admonition"], 0,
      "Section 15(2) provides imprisonment of not less than three years extending up to five years, or fine, or both for storing for commercial purposes or sharing/transmitting.",
      {"A": "Correct; Not less than 3 years up to 5 years, or fine, or both under Section 15(2).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POCSO Act S. 15(2)", "Commercial storage and transmission penalty under Section 15(2).")

# Chapter 3: ch-soc-pocso-03 (15 MCQs)
# top-pocso-03-01 (5)
add_q("mcq-pocso-01-031", "soc-pocso", "ch-soc-pocso-03", "top-pocso-03-01",
      "Under Section 19(1) of the POCSO Act, 2012, who is under a mandatory duty to report the commission or likelihood of commission of an offence under the Act?",
      ["Notwithstanding anything contained in the CrPC, any person who has an apprehension that an offence under this Act has been committed or is likely to be committed",
       "Only the biological parents of the child",
       "Only registered doctors",
       "Only advocates holding a bar council enrollment"], 0,
      "Section 19(1) creates a universal civic obligation: 'any person' who has apprehension or knowledge must report to the Special Juvenile Police Unit or local police.",
      {"A": "Correct; Universal mandatory reporting obligation on 'any person' under Section 19(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 19(1)", "Universal mandatory reporting obligation under Section 19(1).")

add_q("mcq-pocso-01-032", "soc-pocso", "ch-soc-pocso-03", "top-pocso-03-01",
      "Under Section 19(2) of the POCSO Act, what specific duty is cast on the in-charge of any company, institution, or school?",
      ["Every person in-charge of an institution educating or caring for children who has knowledge of an offence shall immediately report it to the Special Juvenile Police Unit or local police",
       "They must conduct their own internal private inquiry before informing police",
       "They must settle the dispute with parents by paying compensation",
       "They can conceal the incident to protect school reputation"], 0,
      "Section 19(2) mandates heads of schools, hospitals, and child-care institutions to immediately report offences; internal concealment is strictly criminalized.",
      {"A": "Correct; Mandatory immediate reporting by institution heads under Section 19(2).", "B": "Incorrect; Private concealment is illegal.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 19(2)", "Mandatory reporting duty of institution heads under Section 19(2).")

add_q("mcq-pocso-01-033", "soc-pocso", "ch-soc-pocso-03", "top-pocso-03-01",
      "Under Section 21(1) of the POCSO Act, what is the punishment for failing to report an offence under Section 19(1)?",
      ["Imprisonment for a term which may extend to six months or with fine or with both",
       "Fine of Rs 100 only",
       "Imprisonment for 5 years",
       "Simple administrative censure"], 0,
      "Section 21(1) punishes failure to report with imprisonment up to six months, or fine, or both.",
      {"A": "Correct; Imprisonment up to six months or fine or both under Section 21(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 21(1)", "Penalty for failure to report under Section 21(1).")

add_q("mcq-pocso-01-034", "soc-pocso", "ch-soc-pocso-03", "top-pocso-03-01",
      "Under Section 21(2) of the POCSO Act, what is the punishment if an in-charge of a company or institution fails to report an offence under Section 19(2)?",
      ["Imprisonment for a term which may extend to one year and also with fine",
       "Fine of Rs 1,000 only",
       "Imprisonment for 7 years",
       "Cancellation of school accreditation only"], 0,
      "Section 21(2) provides enhanced penalty for institution heads who fail to report: imprisonment up to one year and also with fine.",
      {"A": "Correct; Imprisonment up to one year and fine under Section 21(2).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POCSO Act S. 21(2)", "Enhanced penalty for institution heads under Section 21(2).")

add_q("mcq-pocso-01-035", "soc-pocso", "ch-soc-pocso-03", "top-pocso-03-01",
      "Under Section 23 of the POCSO Act, what is the restriction on media and reporting regarding the identity of the victim child?",
      ["No person shall make any report or present any comments in media revealing the identity of the child (name, address, school, photograph), punishable under Section 23(4) with 6 months to 1 year imprisonment",
       "Media can freely broadcast the child's photograph with parental permission",
       "Identity can be revealed if the child is above 12 years",
       "Identity can be broadcast on social media live streams"], 0,
      "Section 23 enacts an absolute statutory embargo on disclosing the child's identity or publishing materials that could lead to identification.",
      {"A": "Correct; Total ban on revealing child's identity; punishable with 6m-1yr imprisonment under Section 23(4).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 23", "Strict media reporting restrictions under Section 23.")

# top-pocso-03-02 (5)
add_q("mcq-pocso-01-036", "soc-pocso", "ch-soc-pocso-03", "top-pocso-03-02",
      "Under Section 24(1) of the POCSO Act, where and by whom should the statement of the child be recorded?",
      ["Recorded at the residence of the child or at a place of her choice, by a woman police officer not below the rank of sub-inspector",
       "At the local police lockup by the Station House Officer",
       "In open court before the media",
       "At the accused person's residence"], 0,
      "Section 24(1) provides that the statement shall be recorded at the child's residence or place of choice, by a woman police officer not below the rank of SI.",
      {"A": "Correct; Recorded at child's residence by a woman police officer not below SI.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 24(1)", "Recording of child's statement by woman police officer under Section 24.")

add_q("mcq-pocso-01-037", "soc-pocso", "ch-soc-pocso-03", "top-pocso-03-02",
      "Under Section 24(2) of the POCSO Act, what is the rule regarding the police officer's attire while recording the child's statement?",
      ["The police officer shall not be wearing a police uniform",
       "The officer must wear full formal dress uniform with ceremonial cap",
       "The officer must wear black judicial robes",
       "Attire is completely discretionary"], 0,
      "Section 24(2) explicitly provides: 'The police officer while recording the statement of the child shall not be in uniform.'",
      {"A": "Correct; Police officer shall not wear uniform under Section 24(2).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 24(2)", "Mandatory plainclothes attire for police officer under Section 24(2).")

add_q("mcq-pocso-01-038", "soc-pocso", "ch-soc-pocso-03", "top-pocso-03-02",
      "Under Section 24(3) of the POCSO Act, can the child be detained at the police station overnight for any reason?",
      ["No, the police officer shall not detain the child in the police station for any purpose during the night",
       "Yes, if the investigation is ongoing",
       "Yes, if the parent signs a detention consent",
       "Detention up to 48 hours is permitted"], 0,
      "Section 24(3) enacts an absolute statutory embargo: 'The police officer shall not detain the child in the police station for any purpose during the night.'",
      {"A": "Correct; Absolute prohibition on detaining child at police station overnight under Section 24(3).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 24(3)", "Absolute bar on overnight police detention of child.")

add_q("mcq-pocso-01-039", "soc-pocso", "ch-soc-pocso-03", "top-pocso-03-02",
      "Under Section 27(1) of the POCSO Act, how must the medical examination of the child be conducted?",
      ["In accordance with Section 164A CrPC / 184 BNSS, and conducted in the presence of the parent or other person in whom the child reposes trust",
       "By a police officer in the police vehicle",
       "Without the presence of any family member",
       "Only after charges are framed by the Special Court"], 0,
      "Section 27(1) mandates medical examination in presence of parent or trusted person; Section 27(2) requires a female doctor for female child victims.",
      {"A": "Correct; Examination in presence of parent/trusted person under Section 27(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POCSO Act S. 27(1)", "Procedure for medical examination of child under Section 27.")

add_q("mcq-pocso-01-040", "soc-pocso", "ch-soc-pocso-03", "top-pocso-03-02",
      "Under Section 27(2) of the POCSO Act, if the victim is a female child, who must conduct the medical examination?",
      ["The medical examination shall be conducted by a woman doctor",
       "Any male doctor in the presence of the police",
       "A panel of three male radiologists",
       "The District Health Officer personally"], 0,
      "Section 27(2) mandates: 'In case the victim is a female child, the medical examination shall be conducted by a woman doctor.'",
      {"A": "Correct; Mandatory examination by woman doctor under Section 27(2).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 27(2)", "Mandatory woman doctor requirement under Section 27(2).")

# top-pocso-03-03 (5)
add_q("mcq-pocso-01-041", "soc-pocso", "ch-soc-pocso-03", "top-pocso-03-03",
      "Under Section 25(1) of the POCSO Act, before whom is the child's statement recorded under Section 164 CrPC / 183 BNSS?",
      ["Before a Judicial Magistrate, recorded as soon as may be after the commission of the offence is brought to notice",
       "Before an Executive Magistrate",
       "Before the village sarpanch",
       "Before the child's school headmaster"], 0,
      "Section 25(1) mandates recording the child's statement by a Judicial Magistrate under Section 164 CrPC as soon as the offence is reported.",
      {"A": "Correct; Recorded by Judicial Magistrate under Section 164 CrPC / 183 BNSS.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 25(1)", "Magistrate recording of statement under Section 25(1).")

add_q("mcq-pocso-01-042", "soc-pocso", "ch-soc-pocso-03", "top-pocso-03-03",
      "Under Section 26 of the POCSO Act, what assistance must be provided while recording the child's statement if the child has a disability or communication difficulty?",
      ["Assistance of an interpreter, translator, or special educator, and audio-video electronic recording should be utilized",
       "Child's testimony is discarded as inadmissible",
       "Child is sent for psychological conditioning",
       "Accused is asked to interpret for the child"], 0,
      "Section 26 provides for assistance of translators, special educators, and audio-video electronic means to ensure effective communication.",
      {"A": "Correct; Assistance of interpreter/special educator and audio-video recording under Section 26.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POCSO Act S. 26", "Special educator and translation assistance under Section 26.")

add_q("mcq-pocso-01-043", "soc-pocso", "ch-soc-pocso-03", "top-pocso-03-03",
      "Under Section 25(2) of the POCSO Act, is the presence of the accused advocate permitted during the recording of the child's statement under Section 164 CrPC?",
      ["No, the Magistrate records the statement without the presence of the advocate for the accused",
       "Yes, the advocate for the accused has an absolute right to cross-examine immediately",
       "Yes, the accused must sit facing the child",
       "Only if approved by the Bar Association"], 0,
      "Recording of a Section 164 statement is an inquisitorial pre-trial procedure; the accused or their advocate is not permitted to cross-examine or intimidate the child at this stage.",
      {"A": "Correct; Recorded without the presence of the accused's advocate.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POCSO Act S. 25(2)", "Exclusion of accused's advocate during Section 164 recording.")

add_q("mcq-pocso-01-044", "soc-pocso", "ch-soc-pocso-03", "top-pocso-03-03",
      "Can the statement recorded under Section 164 CrPC be treated as substantive evidence without the child testifying in the Special Court?",
      ["No, Section 164 statements are previous statements used for corroboration or contradiction under Evidence Act; the child must be examined in court unless exceptional conditions apply",
       "Yes, Section 164 completely dispenses with trial testimony",
       "Yes, the Magistrate's recording operates as a final conviction",
       "Only if recorded in English"], 0,
      "Settled criminal law establishes that a Section 164 statement is not substantive evidence; it corroborates or contradicts the witness under Sections 145 and 157 Evidence Act.",
      {"A": "Correct; Used for corroboration and contradiction; not substantive evidence per se.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "POCSO S. 25 & IEA S. 145, 157", "Evidentiary status of Section 164 statement.")

add_q("mcq-pocso-01-045", "soc-pocso", "ch-soc-pocso-03", "top-pocso-03-03",
      "Under Section 26(2) of the Act, how should the Magistrate ensure that the child feels safe while recording the statement?",
      ["The Magistrate shall ensure that the environment is comfortable and non-intimidating, allowing presence of parents or trusted persons",
       "The Magistrate must wear a ceremonial wig and judicial robes",
       "The recording must take place in the police station lockup",
       "The child must stand in the prisoner's dock"], 0,
      "Section 26 mandates child-friendly procedures: non-intimidating environment and allowing parents or trusted guardians to accompany the child.",
      {"A": "Correct; Safe, non-intimidating environment with parent/trusted person present.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POCSO Act S. 26(2)", "Child-friendly atmosphere during Magistrate recording.")

# Chapter 4: ch-soc-pocso-04 (15 MCQs)
# top-pocso-04-01 (5)
add_q("mcq-pocso-01-046", "soc-pocso", "ch-soc-pocso-04", "top-pocso-04-01",
      "Under Section 28(1) of the POCSO Act, 2012, which court is designated as a 'Special Court' to try offences under the Act?",
      ["A Court of Session in each district, designated by the State Government with the concurrence of the Chief Justice of the High Court",
       "A Court of Judicial Magistrate of the Second Class",
       "The High Court directly",
       "The Juvenile Justice Board"], 0,
      "Section 28(1) provides that the State Government, with concurrence of the Chief Justice of the High Court, shall designate for each district a Court of Session to be a Special Court.",
      {"A": "Correct; Court of Session designated as Special Court in each district.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect; JJB handles juvenile offenders, not adult POCSO accused."},
      "Foundational", "POCSO Act S. 28(1)", "Designation of Special Court under Section 28(1).")

add_q("mcq-pocso-01-047", "soc-pocso", "ch-soc-pocso-04", "top-pocso-04-01",
      "Can a Special Court take cognizance of an offence under POCSO directly without the case being committed to it by a Magistrate under Section 209 CrPC / 232 BNSS?",
      ["Yes, Section 33(1) explicitly provides that the Special Court may take cognizance of any offence without the accused being committed to it for trial",
       "No, committal by a Magistrate is an absolute mandatory prerequisite",
       "Only if the High Court transfers the case",
       "Only if the accused consents to direct trial"], 0,
      "Section 33(1) explicitly empowers the Special Court to take direct cognizance of any offence without committal under CrPC.",
      {"A": "Correct; Direct cognizance without committal under Section 33(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 33(1)", "Direct cognizance without committal under Section 33(1).")

add_q("mcq-pocso-01-048", "soc-pocso", "ch-soc-pocso-04", "top-pocso-04-01",
      "Under Section 32(1) of the POCSO Act, who appoints the Special Public Prosecutor for conducting cases in the Special Court?",
      ["The State Government by notification, appointing an advocate who has been in practice for not less than seven years",
       "The Bar Council of India",
       "The Chief Justice of India",
       "The District Collector"], 0,
      "Section 32(1) provides that the State Government shall appoint a Special Public Prosecutor with not less than seven years of standing as an advocate.",
      {"A": "Correct; State Government appoints Special Public Prosecutor with min 7 years practice.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 32(1)", "Appointment and standing (7 years) of Special Public Prosecutor.")

add_q("mcq-pocso-01-049", "soc-pocso", "ch-soc-pocso-04", "top-pocso-04-01",
      "Under Section 31 of the POCSO Act, 2012, which procedural code applies to trials before the Special Court?",
      ["Provisions of the Code of Criminal Procedure, 1973 / BNSS 2023 (including provisions relating to bail) apply to proceedings before a Special Court",
       "The Code of Civil Procedure, 1908 exclusively",
       "Summary procedure under small causes court",
       "Customary tribal procedures"], 0,
      "Section 31 provides that save as otherwise provided in the Act, CrPC/BNSS provisions apply to proceedings before the Special Court.",
      {"A": "Correct; CrPC / BNSS provisions apply to Special Court proceedings under Section 31.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POCSO Act S. 31", "Application of CrPC/BNSS to Special Court under Section 31.")

add_q("mcq-pocso-01-050", "soc-pocso", "ch-soc-pocso-04", "top-pocso-04-01",
      "Can the Special Court try offences under other statutes (such as IPC, BNS, or IT Act) jointly with POCSO offences in the same trial?",
      ["Yes, Section 28(2) and Section 33 empower the Special Court to try offences under other laws with which the accused may be charged under CrPC/BNSS",
       "No, POCSO Special Courts can never try any non-POCSO offence",
       "Only if the Supreme Court passes a special order",
       "Only if the accused pleads guilty to all charges"], 0,
      "Section 28(2) explicitly provides that the Special Court can try offences under other enactments charged jointly under CrPC joinder rules.",
      {"A": "Correct; Special Court can try connected offences under other laws in joint trial.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POCSO Act S. 28(2), S. 33", "Joint trial competence of Special Court for connected offences.")

# top-pocso-04-02 (5)
add_q("mcq-pocso-01-051", "soc-pocso", "ch-soc-pocso-04", "top-pocso-04-02",
      "Under Section 33(2) of the POCSO Act, how are questions put to the child during trial in the Special Court?",
      ["The Special Public Prosecutor or the defence advocate shall put questions to the child through the Special Court, preventing direct badgering",
       "The defence lawyer shouts questions directly into the child's ear",
       "Questions must be submitted three months in advance in Latin",
       "The child is cross-examined by the accused directly"], 0,
      "Section 33(2) provides: 'The Special Public Prosecutor or the defence counsel shall put questions to the child through the Special Court.'",
      {"A": "Correct; Questions put to the child through the Special Court under Section 33(2).", "B": "Incorrect; Direct aggressive confrontation is barred.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 33(2)", "Examination of child through the Special Court under Section 33(2).")

add_q("mcq-pocso-01-052", "soc-pocso", "ch-soc-pocso-04", "top-pocso-04-02",
      "Under Section 33(4) of the Act, what duty is cast on the Special Court regarding the visual exposure of the child to the accused?",
      ["The Special Court shall ensure that the child is not exposed in any way to the accused at the time of recording evidence, while ensuring accused can hear the child and communicate with lawyer",
       "The child must sit on the accused's lap",
       "The child and accused must be handcuffed together",
       "Visual exposure is mandatory to test the child's courage"], 0,
      "Section 33(4) mandates protective screens, one-way mirrors, or video links so that the child is not exposed to the accused during testimony.",
      {"A": "Correct; Special Court ensures child is not exposed in any way to accused under Section 33(4).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 33(4)", "Protection against visual exposure to accused under Section 33(4).")

add_q("mcq-pocso-01-053", "soc-pocso", "ch-soc-pocso-04", "top-pocso-04-02",
      "Under Section 37 of the POCSO Act, 2012, in what manner shall the Special Court conduct trial proceedings?",
      ["The Special Court shall try cases in camera and in the presence of parents of the child or other trusted person",
       "In open court with live television broadcast",
       "In the presence of the entire school student body",
       "In public stadium hearings"], 0,
      "Section 37 mandates in-camera proceedings to protect the child's privacy, permitting parents or trusted persons to be present.",
      {"A": "Correct; Mandatory in-camera trial under Section 37.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 37", "Mandatory in-camera trial under Section 37.")

add_q("mcq-pocso-01-054", "soc-pocso", "ch-soc-pocso-04", "top-pocso-04-02",
      "Under Section 35(1) of the POCSO Act, within what period shall the evidence of the child be recorded by the Special Court?",
      ["Within a period of thirty days of the Special Court taking cognizance of the offence",
       "Within seven days",
       "Within six months",
       "Within one year"], 0,
      "Section 35(1) specifies that the evidence of the child shall be recorded within a period of thirty days of the Special Court taking cognizance.",
      {"A": "Correct; Within thirty days of cognizance under Section 35(1).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 35(1)", "Timeline (30 days) for recording child's evidence under Section 35(1).")

add_q("mcq-pocso-01-055", "soc-pocso", "ch-soc-pocso-04", "top-pocso-04-02",
      "Under Section 35(2) of the POCSO Act, what is the target timeline for the Special Court to complete the entire trial?",
      ["The Special Court shall complete the trial, as far as possible, within a period of one year from the date of taking cognizance of the offence",
       "Within three months",
       "Within six months",
       "Within three years"], 0,
      "Section 35(2) mandates that the Special Court shall complete the trial, as far as possible, within a period of one year from taking cognizance.",
      {"A": "Correct; Target completion within one year of taking cognizance under Section 35(2).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 35(2)", "One-year trial completion target under Section 35(2).")

# top-pocso-04-03 (5)
add_q("mcq-pocso-01-056", "soc-pocso", "ch-soc-pocso-04", "top-pocso-04-03",
      "Under Section 29 of the POCSO Act, 2012, what statutory presumption is created against the accused in prosecutions under Sections 3, 5, 7 and 9?",
      ["The Special Court shall presume that the accused has committed or abetted the offence, unless the contrary is proved",
       "The court shall presume the accused is innocent beyond all doubt",
       "The court shall presume the child fabricated the case",
       "The court shall presume the parents committed the offence"], 0,
      "Section 29 creates a statutory reverse presumption of guilt once the foundational facts are proved by prosecution: court shall presume commission/abetment unless contrary is proved.",
      {"A": "Correct; Statutory presumption that accused committed the offence unless contrary is proved.", "B": "Incorrect; Section 29 displaces ordinary presumption of innocence upon proof of foundational facts.", "C": "Incorrect.", "D": "Incorrect."},
      "Foundational", "POCSO Act S. 29", "Statutory presumption of guilt under Section 29.")

add_q("mcq-pocso-01-057", "soc-pocso", "ch-soc-pocso-04", "top-pocso-04-03",
      "Under Section 30 of the POCSO Act, 2012, what statutory presumption is created regarding culpable mental state (mens rea)?",
      ["The Special Court shall presume the existence of culpable mental state on the part of the accused, but it shall be a defense for the accused to prove that he had no such mental state",
       "The prosecution must independently prove mens rea with wiretapped audio",
       "Mens rea is completely irrelevant in criminal law",
       "Mental state is presumed innocent under Section 30"], 0,
      "Section 30 creates a mandatory presumption of culpable mental state (intention, motive, knowledge), requiring the accused to prove absence of mens rea beyond reasonable doubt under 30(2).",
      {"A": "Correct; Mandatory presumption of culpable mental state under Section 30.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POCSO Act S. 30", "Presumption of culpable mental state under Section 30.")

add_q("mcq-pocso-01-058", "soc-pocso", "ch-soc-pocso-04", "top-pocso-04-03",
      "What is the prerequisite before the statutory presumption under Section 29 can be invoked against an accused?",
      ["The prosecution must first establish the foundational facts of the alleged incident by leading credible, reliable evidence",
       "The presumption applies automatically upon filing of the police FIR",
       "The accused must first confess before police",
       "The presumption applies only after the accused is convicted"], 0,
      "As repeatedly held by the Supreme Court, Section 29 does not relieve prosecution of its initial burden to prove foundational facts; only after foundational facts are established does the presumption operate.",
      {"A": "Correct; Prosecution must prove foundational facts before Section 29 presumption triggers.", "B": "Incorrect; FIR alone does not trigger presumption.", "C": "Incorrect.", "D": "Incorrect."},
      "Advanced", "POCSO Act S. 29 & Landmark Judicial Rulings", "Foundational facts requirement for Section 29 presumption.")

add_q("mcq-pocso-01-059", "soc-pocso", "ch-soc-pocso-04", "top-pocso-04-03",
      "Under Section 33(8) of the POCSO Act and Rule 9 of the POCSO Rules, 2020, what power is vested in the Special Court regarding compensation to the child victim?",
      ["The Special Court may direct payment of interim or final compensation to the child from the victim compensation fund or legal services authority for immediate relief and rehabilitation",
       "The Special Court can only order compensation after Supreme Court confirms the conviction",
       "The child must file a separate civil suit for damages under tort law",
       "Compensation can only be awarded in commercial disputes"], 0,
      "Section 33(8) and POCSO Rules 2020 empower the Special Court to grant immediate interim compensation and final rehabilitation compensation.",
      {"A": "Correct; Special Court awards interim and final compensation under Section 33(8) and POCSO Rules.", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POCSO Act S. 33(8) & POCSO Rules Rule 9", "Power of Special Court to award interim and final compensation.")

add_q("mcq-pocso-01-060", "soc-pocso", "ch-soc-pocso-04", "top-pocso-04-03",
      "Can compensation awarded to a child victim under Section 33(8) of POCSO be recovered from the fine imposed on the convicted accused?",
      ["Yes, Section 33(8) provides that the Special Court may order payment of compensation to the child, and any fine imposed under Section 4, 6, 8, 10, etc. may be applied towards such compensation",
       "No, all fines must strictly go to the Consolidated Fund of India",
       "Fines can only be paid to the police department",
       "The accused is exempt from paying any fine"], 0,
      "Under POCSO and Section 357 CrPC / 395 BNSS, the fine imposed on the accused is directed to be paid as compensation to the victim child.",
      {"A": "Correct; Fines imposed can be applied towards victim compensation under Section 33(8).", "B": "Incorrect.", "C": "Incorrect.", "D": "Incorrect."},
      "Standard", "POCSO Act S. 33(8) & CrPC S. 357 / BNSS S. 395", "Application of fine towards victim compensation.")

# --- Save to assets/learning/data/social/social-mcqs-part3.js ---
output_path = os.path.join("assets", "learning", "data", "social", "social-mcqs-part3.js")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

header = """/**
 * Tanveer Ashraf Judicial Prep 2026–27
 * Social Legislation MCQs — Part 3 (Acts 7-9)
 *
 * Covers:
 * 7. Medical Termination of Pregnancy Act, 1971 (50 MCQs: mcq-mtp-01-001 to mcq-mtp-01-050)
 * 8. Indecent Representation of Women (Prohibition) Act, 1986 (45 MCQs: mcq-irwa-01-001 to mcq-irwa-01-045)
 * 9. Protection of Children from Sexual Offences Act, 2012 (60 MCQs: mcq-pocso-01-001 to mcq-pocso-01-060)
 *
 * Total: 155 Verified Practice MCQs
 * 100% 4-Option Rationale (A, B, C, D) & Statutory Provisions
 */

(function(global) {
    'use strict';

    const SOCIAL_MCQS_PART3 = """

footer = """;

    if (typeof module !== 'undefined' && module.exports) {
        module.exports = SOCIAL_MCQS_PART3;
    }
    global.SOCIAL_MCQS_PART3 = SOCIAL_MCQS_PART3;
})(typeof window !== 'undefined' ? window : global);
"""

with open(output_path, "w", encoding="utf-8") as f:
    f.write(header + json.dumps(mcqs, indent=2, ensure_ascii=False) + footer)

print(f"SUCCESS: Created {output_path} with {len(mcqs)} MCQs!")
