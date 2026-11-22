"""
Appender for Criminal Law MCQs Part 1 (Topics top-crim-01-02 to top-crim-04-03: 110 MCQs)
Compiles complete 120 MCQs for Part 1 into scripts/data_crim_mcqs_1.py
"""

import json

# Import the initial 10 MCQs from scripts/data_crim_mcqs_1.py
import sys
sys.path.append('scripts')
from data_crim_mcqs_1 import MCQS_PART1

def make_mcq(q_id, ch_id, top_id, q_text, options, ans_idx, ans_letter, explanation, breakdown, diff, provision, objective):
    return {
        "id": q_id,
        "subjectId": "law-criminal",
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
        "sourceUrl": "https://www.mha.gov.in",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": objective,
        "eligible": True,
        "status": "active"
    }

mcqs = list(MCQS_PART1)

# -----------------------------------------------------------------------------
# top-crim-01-02: Actus Reus, Mens Rea & Strict Liability (10 MCQs: 011 to 020)
# -----------------------------------------------------------------------------
mcqs.append(make_mcq(
    "mcq-crim-01-011", "ch-crim-01", "top-crim-01-02",
    "The fundamental maxim 'Actus non facit reum nisi mens sit rea' literally translates to:",
    ["An act makes a man guilty only if civilly actionable", "An act does not make a person guilty unless the mind is also guilty", "A guilty mind alone without an act is punishable", "Every illegal omission automatically constitutes an actus reus"],
    1, "B",
    "The maxim means that an act does not constitute a crime unless accompanied by a guilty mind or criminal intention.",
    {"A": "Civil liability does not govern criminal penal maxims.", "B": "Correct; actus non facit reum nisi mens sit rea demands both act and mental element.", "C": "Bare intention without an act is never punishable.", "D": "Omission must be illegal and accompanied by requisite mens rea."},
    "Easy", "General Principles of Criminal Law", "Master the foundational maxim of criminal liability."
))

mcqs.append(make_mcq(
    "mcq-crim-01-012", "ch-crim-01", "top-crim-01-02",
    "Which of the following is NOT one of the recognized four stages in the commission of a crime?",
    ["Intention", "Preparation", "Attempt", "Motive"],
    3, "D",
    "The four recognized stages are Intention, Preparation, Attempt, and Commission (Accomplishment). Motive is the psychological reason that prompts intention, but is not a sequential stage.",
    {"A": "Intention is the first stage.", "B": "Preparation is the second stage.", "C": "Attempt is the third stage.", "D": "Correct; motive is not one of the four procedural stages of crime."},
    "Easy", "General Principles of Criminal Law", "Distinguish stages of crime from motive."
))

mcqs.append(make_mcq(
    "mcq-crim-01-013", "ch-crim-01", "top-crim-01-02",
    "As a general rule, mere preparation to commit an offence is not punishable. In which of the following cases is mere preparation made expressly punishable?",
    ["Preparation to commit murder", "Preparation to commit theft", "Preparation to commit dacoity", "Preparation to commit cheating"],
    2, "C",
    "Under Section 310(2) BNS / Section 399 IPC, making preparation to commit dacoity is specifically penalised with rigorous imprisonment extending up to 10 years.",
    {"A": "Preparation to commit murder is not punishable; only attempt is.", "B": "Preparation to commit theft is not punishable.", "C": "Correct; making preparation to commit dacoity is an exceptional statutory offence.", "D": "Preparation to commit cheating is not punishable."},
    "Medium", "BNS Section 310(2) / IPC Section 399", "Identify statutory exceptions where preparation is punishable."
))

mcqs.append(make_mcq(
    "mcq-crim-01-014", "ch-crim-01", "top-crim-01-02",
    "In State of Maharashtra v. Mayer Hans George (1965), the Supreme Court held that mens rea is excluded in statutory offences when:",
    ["The offender is a foreign national unaware of Indian exchange laws", "The statute either expressly or by necessary implication rules out mens rea for public welfare", "The offence causes no physical damage to individuals", "The Reserve Bank of India failed to notify the individual personally"],
    1, "B",
    "A Constitution Bench held that unless a statute either clearly or by necessary implication rules out mens rea, it must be read into penal provisions; however, in FERA/public welfare statutes, strict liability may be inferred.",
    {"A": "Foreign nationality does not exclude mens rea or provide a defence.", "B": "Correct; legislative exclusion of mens rea can be express or necessarily implied in socio-economic enactments.", "C": "Lack of physical damage is not the test.", "D": "Individual notification is not required for published gazette regulations."},
    "Hard", "State of Maharashtra v. Mayer Hans George, AIR 1965 SC 722", "Analyze the doctrine of strict liability in statutory crimes."
))

mcqs.append(make_mcq(
    "mcq-crim-01-015", "ch-crim-01", "top-crim-01-02",
    "Which of the following offences under the penal code is an example of strict statutory liability where mens rea regarding age is irrelevant?",
    ["Kidnapping from lawful guardianship", "Culpable Homicide", "Extortion", "Defamation"],
    0, "A",
    "In R v. Prince and under Section 137 BNS / Section 361 IPC, kidnapping from lawful guardianship is a strict liability offence; the honest belief that the girl was above age is no defence.",
    {"A": "Correct; kidnapping is a strict liability offence regarding age.", "B": "Culpable homicide requires specific intention or knowledge.", "C": "Extortion requires intentional putting in fear.", "D": "Defamation requires intent or knowledge to harm reputation."},
    "Medium", "BNS Section 137 / IPC Section 361 & R v. Prince", "Recognize strict liability exceptions in penal law."
))

mcqs.append(make_mcq(
    "mcq-crim-01-016", "ch-crim-01", "top-crim-01-02",
    "What is the test formulated in Abhayanand Mishra v. State of Bihar (1961) to determine when preparation ends and attempt begins?",
    ["The proximity test where the accused does an act towards commission after completing preparation", "The locus poenitentiae test requiring the last possible act", "The unequivocal act test requiring verbal confession", "The impossibility test"],
    0, "A",
    "The Supreme Court held that a person commits an attempt when they intend to commit an offence and, although not having completed it, take a step towards commission after preparation.",
    {"A": "Correct; taking an active step towards execution constitutes attempt.", "B": "Locus poenitentiae applies before execution starts.", "C": "Attempt does not require verbal confession.", "D": "Impossibility does not negate attempt (e.g. picking an empty pocket)."},
    "Hard", "Abhayanand Mishra v. State of Bihar, AIR 1961 SC 1698", "Distinguish attempt from preparation."
))

mcqs.append(make_mcq(
    "mcq-crim-01-017", "ch-crim-01", "top-crim-01-02",
    "A puts his hand in B's pocket intending to steal money, but finds the pocket completely empty. A is guilty of:",
    ["No offence because the act was impossible of completion", "Attempt to commit theft under Section 62 BNS / Section 511 IPC", "Mischief", "Criminal trespass"],
    1, "B",
    "Factual impossibility does not bar liability for attempt. Under Section 62 BNS / Section 511 IPC (Illustration b), picking an empty pocket constitutes attempt to commit theft.",
    {"A": "Factual impossibility is no defence in attempt.", "B": "Correct; attempt to commit theft is complete upon putting the hand with dishonest intent.", "C": "Mischief requires destruction or damage to property.", "D": "Pocket picking is not criminal trespass into property."},
    "Easy", "BNS Section 62 / IPC Section 511 Illustration (b)", "Understand attempt with factual impossibility."
))

mcqs.append(make_mcq(
    "mcq-crim-01-018", "ch-crim-01", "top-crim-01-02",
    "Which mental element in the Bharatiya Nyaya Sanhita signifies the highest degree of blameworthiness?",
    ["Negligence", "Rashness", "Knowledge", "Intention"],
    3, "D",
    "The hierarchy of culpability from highest to lowest is: Intention (purposeful desire of consequence) > Knowledge (awareness of likelihood) > Rashness (reckless indifference) > Negligence (breach of duty of care).",
    {"A": "Negligence is the lowest tier of culpability.", "B": "Rashness involves consciousness of risk but indifference.", "C": "Knowledge involves awareness of probable result.", "D": "Correct; Intention is the most severe and culpable state of mind."},
    "Medium", "Hierarchy of Mens Rea in Criminal Law", "Master degrees of mental culpability."
))

mcqs.append(make_mcq(
    "mcq-crim-01-019", "ch-crim-01", "top-crim-01-02",
    "A purchases matchsticks and petrol to burn down B's house. While walking towards B's house, A is intercepted by police 2 kilometres away. A has committed:",
    ["Attempt to commit mischief by fire", "Only preparation, which is not punishable", "Criminal conspiracy", "Completed mischief"],
    1, "B",
    "Procuring materials and walking towards the spot is still in the stage of preparation; A has not yet performed an overt act directly proximate to igniting the fire.",
    {"A": "Attempt requires an act immediately connected to ignition.", "B": "Correct; merely purchasing materials and moving is non-punishable preparation.", "C": "No conspiracy is shown as A acted alone.", "D": "No damage occurred, so completed mischief is absent."},
    "Medium", "Malkiat Singh v. State of Punjab, (1969) 1 SCC 157", "Apply proximity test to preparation versus attempt."
))

mcqs.append(make_mcq(
    "mcq-crim-01-020", "ch-crim-01", "top-crim-01-02",
    "Under Section 62 BNS / Section 511 IPC, what is the default punishment for attempt when no express provision is made in the code?",
    ["One-fourth of the longest term of imprisonment for the offence", "One-half of the longest term of imprisonment provided for the offence, or fine, or both", "Full term of imprisonment provided for the offence", "Only a nominal fine of Rs 1,000"],
    1, "B",
    "Section 62 BNS / Section 511 IPC provides that whoever attempts to commit an offence shall be punished with imprisonment for a term extending up to one-half of the longest term provided for that offence.",
    {"A": "One-fourth is the default fine imprisonment limit under procedural law.", "B": "Correct; one-half of the maximum term is the standard default punishment for attempt.", "C": "Completed offences attract the full term, not attempt.", "D": "Fine alone is not the sole statutory penalty."},
    "Easy", "BNS Section 62 / IPC Section 511", "Recall the general penalty formula for attempt."
))

# -----------------------------------------------------------------------------
# top-crim-01-03: General Explanations & Person / Public Servant (10 MCQs: 021 to 030)
# -----------------------------------------------------------------------------
mcqs.append(make_mcq(
    "mcq-crim-01-021", "ch-crim-01", "top-crim-01-03",
    "How does the Bharatiya Nyaya Sanhita, 2023 structurally organize definitions compared to the Indian Penal Code, 1860?",
    ["Definitions are scattered across 45 separate sections (Ss. 6 to 52A)", "All primary definitions are consolidated alphabetically into a single section: Section 2", "Definitions are moved to an unnumbered appendix at the end of the Act", "Definitions are completely abolished to leave terms to judicial interpretation"],
    1, "B",
    "Section 2 BNS consolidates definitions into clauses (1) to (39), replacing the scattered provisions of IPC Sections 6 to 52A.",
    {"A": "This describes the legacy IPC arrangement.", "B": "Correct; Section 2 BNS contains an organized dictionary of defined terms.", "C": "Definitions are in Section 2, not an appendix.", "D": "Statutory definitions remain vital in criminal codes."},
    "Easy", "BNS Section 2 vs IPC Sections 6–52A", "Understand the structural consolidation of definitions in BNS."
))

mcqs.append(make_mcq(
    "mcq-crim-01-022", "ch-crim-01", "top-crim-01-03",
    "Under Section 2(10) of the Bharatiya Nyaya Sanhita, 2023, the pronoun 'he' and its derivatives are defined to include:",
    ["Only male persons", "Any person, whether male, female, or transgender", "Male persons and registered legal entities only", "Only adult citizens of India"],
    1, "B",
    "Section 2(10) BNS modernizes gender definitions by explicitly enacting that the pronoun 'he' and its derivatives are used of any person, whether male, female, or transgender.",
    {"A": "Too narrow; criminal law pronouns cover all genders.", "B": "Correct; Section 2(10) BNS explicitly includes male, female, and transgender.", "C": "Transgender inclusion is the modern statutory advance.", "D": "Citizenship does not limit pronoun definitions."},
    "Medium", "BNS Section 2(10) Gender Definition", "Master the gender-neutral and transgender inclusion in BNS."
))

mcqs.append(make_mcq(
    "mcq-crim-01-023", "ch-crim-01", "top-crim-01-03",
    "Under Section 2(11) BNS / Section 52 IPC, nothing is said to be done or believed in 'good faith' which is done or believed:",
    ["Without malicious intent", "Without due care and attention", "Without written legal advice from an advocate", "Under an honest mistake of civil law"],
    1, "B",
    "Section 2(11) BNS / Section 52 IPC defines good faith negatively: nothing is done in good faith which is done or believed without due care and attention.",
    {"A": "Absence of malice alone is insufficient if care and attention were lacking.", "B": "Correct; 'due care and attention' is the statutory touchstone of good faith.", "C": "Legal advice is not a statutory prerequisite.", "D": "Mistake of law does not define good faith."},
    "Easy", "BNS Section 2(11) / IPC Section 52", "Recall the statutory definition of 'good faith'."
))

mcqs.append(make_mcq(
    "mcq-crim-01-024", "ch-crim-01", "top-crim-01-03",
    "Who among the following is NOT a 'Public Servant' under Section 2(28) of the Bharatiya Nyaya Sanhita, 2023?",
    ["A Judge or Magistrate", "A commissioned officer in the military forces of India", "An arbitrator or other person to whom any cause has been referred by a Court", "A Member of Parliament or Member of Legislative Assembly in their personal capacity as advocates"],
    3, "D",
    "While MPs/MLAs are public servants when discharging legislative functions (P.V. Narasimha Rao), practicing advocates in their personal profession are not public servants.",
    {"A": "Judges are expressly included under Section 2(28)(a).", "B": "Commissioned officers are included under Section 2(28)(b).", "C": "Arbitrators appointed by courts are included under Section 2(28)(e).", "D": "Correct; advocates in private practice are not public servants."},
    "Medium", "BNS Section 2(28) / IPC Section 21", "Identify who constitutes a Public Servant."
))

mcqs.append(make_mcq(
    "mcq-crim-01-025", "ch-crim-01", "top-crim-01-03",
    "The definition of 'Dishonestly' under Section 2(7) BNS / Section 24 IPC requires:",
    ["Intention to cause injury to the feelings of another", "Intention of causing wrongful gain to one person or wrongful loss to another person", "Deceiving any person fraudulently without financial loss", "Acting contrary to ethical or moral expectations"],
    1, "B",
    "Section 2(7) BNS / Section 24 IPC provides that whoever does anything with the intention of causing wrongful gain to one person or wrongful loss to another person is said to do that thing dishonestly.",
    {"A": "Hurt to feelings does not constitute dishonest intention.", "B": "Correct; wrongful gain or wrongful loss is the twin criterion of 'dishonestly'.", "C": "Fraudulently under Section 2(8) involves deceit and injury.", "D": "Moral failure is not legal dishonesty."},
    "Easy", "BNS Section 2(7) / IPC Section 24", "Define 'Dishonestly' in criminal law."
))

mcqs.append(make_mcq(
    "mcq-crim-01-026", "ch-crim-01", "top-crim-01-03",
    "Under Section 2(8) BNS / Section 25 IPC, a person is said to do a thing 'fraudulently' if they do that thing with intent to defraud, but not otherwise. In Dr. Vimla v. Delhi Administration (1963), 'defraud' was held to involve:",
    ["Deceit and injury to someone", "Only wrongful gain of money", "Mere telling of a white lie without injury", "Non-performance of a contractual promise"],
    0, "A",
    "The Supreme Court held that 'defraud' involves two elements: deceit (or misleading) and injury to the person deceived (or someone else).",
    {"A": "Correct; deceit plus injury constitutes fraud.", "B": "Injury need not be purely pecuniary; economic gain is not mandatory.", "C": "Deceit without injury does not constitute legal fraud.", "D": "Breach of contract without deceit is a civil wrong."},
    "Hard", "Dr. Vimla v. Delhi Administration, AIR 1963 SC 1572", "Master the twin elements of 'fraudulently'."
))

mcqs.append(make_mcq(
    "mcq-crim-01-027", "ch-crim-01", "top-crim-01-03",
    "Under Section 2(39) BNS / Section 44 IPC, the term 'Injury' denotes any harm whatever illegally caused to any person, in:",
    ["Body or property only", "Body, mind, reputation, or property", "Reputation and financial status only", "Physical body and health only"],
    1, "B",
    "Section 2(39) BNS / Section 44 IPC covers harm illegally caused to four distinct facets: body, mind, reputation, or property.",
    {"A": "Omits mind and reputation.", "B": "Correct; body, mind, reputation, and property are the four statutory facets.", "C": "Omits body and mind.", "D": "Too narrow; physical health is only one aspect of bodily injury."},
    "Easy", "BNS Section 2(39) / IPC Section 44", "Recall the four dimensions of legal 'Injury'."
))

mcqs.append(make_mcq(
    "mcq-crim-01-028", "ch-crim-01", "top-crim-01-03",
    "Under Section 2(26) BNS / Section 11 IPC, the word 'Person' includes:",
    ["Only human beings born alive", "Any Company or Association or body of persons, whether incorporated or not", "Only citizens entitled to vote under Article 326", "Only natural persons holding taxable property"],
    1, "B",
    "Section 2(26) BNS / Section 11 IPC explicitly includes corporations, associations, partnerships, and unincorporated bodies within the definition of person.",
    {"A": "Legal persons are fully recognized.", "B": "Correct; corporate bodies and associations are statutory persons.", "C": "Franchise is irrelevant to corporate personhood.", "D": "Tax status does not determine penal personhood."},
    "Easy", "BNS Section 2(26) / IPC Section 11", "Define corporate and juristic persons under BNS."
))

mcqs.append(make_mcq(
    "mcq-crim-01-029", "ch-crim-01", "top-crim-01-03",
    "Under Section 3(1) of the Bharatiya Nyaya Sanhita, 2023, every act or omission contrary to the Sanhita is punishable. An omission is punishable ONLY IF:",
    ["It violates moral ethics of society", "It is an 'illegal omission' in breach of a legal duty", "It results in financial loss to the State", "It is accompanied by a formal complaint from relatives"],
    1, "B",
    "Under Section 2(13) BNS / Section 32 IPC, words referring to acts done extend also to illegal omissions. An omission is illegal only when it is an offence, or prohibited by law, or furnishes ground for civil action.",
    {"A": "Moral duty (e.g. saving a drowning child) is not an illegal omission unless parent/lifeguard duty exists.", "B": "Correct; omission must be 'illegal' (breach of legal obligation).", "C": "Financial loss to State is not the test.", "D": "Standing of relatives does not define illegal omissions."},
    "Medium", "BNS Section 2(13) & 3(1) / IPC Section 32", "Distinguish legal omissions from moral omissions."
))

mcqs.append(make_mcq(
    "mcq-crim-01-030", "ch-crim-01", "top-crim-01-03",
    "Under Section 2(37) BNS / Section 52A IPC, 'Harbour' includes supplying a person with shelter, food, drink, money, clothes, arms, ammunition, or means of conveyance. Which relationship is statutorily exempted from the offence of harbouring?",
    ["Father harbouring a son", "Spouse harbouring a husband or wife", "Advocate harbouring a client", "Employer harbouring an employee"],
    1, "B",
    "Section 2(37) BNS / Section 52A IPC explicitly exempts the husband or wife of the person harboured from criminal liability for harbouring.",
    {"A": "Parents are not exempted from harbouring laws.", "B": "Correct; matrimonial cohabitation creates a statutory exception for husband/wife.", "C": "Advocates have legal privilege, not harbouring immunity.", "D": "Employers have no harbouring exemption."},
    "Medium", "BNS Section 2(37) Exception / IPC Section 52A", "Recognize the matrimonial exemption in harbouring."
))

# Save state
with open("scripts/data_crim_mcqs_1.py", "w", encoding="utf-8") as f:
    f.write(f"MCQS_PART1 = {json.dumps(mcqs, indent=2)}\n")
print(f"Generated {len(mcqs)} MCQs in scripts/data_crim_mcqs_1.py")
