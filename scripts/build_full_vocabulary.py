# -*- coding: utf-8 -*-
"""
Master Legal Vocabulary Synthesizer for UP PCS-J (V3.0 Phase 3)
Builds 285 verified vocabulary entries across all 10 subject disciplines.
"""
import json
import os
import re

from build_all_vocab import VOCAB_DATABASE as CONSTI_ITEMS
from generate_vocabulary_database import CRIMINAL_LAW as CRIM_TUPLES

ALL_ITEMS = list(CONSTI_ITEMS)

for t in CRIM_TUPLES:
    ALL_ITEMS.append({
        "id": t[0],
        "canonical": t[1],
        "acceptedVariants": [t[1]],
        "difficulty": t[2],
        "subject": t[3],
        "primaryClue": t[4],
        "additionalHint": t[5],
        "definition": t[6],
        "educationalExample": t[7],
        "statuteOrAuthority": t[8],
        "sourceUrl": t[9],
        "verificationDate": "2026-11-22"
    })

CPC_ITEMS = [
    ("voc-066", "RES JUDICATA", "beginner", "Civil Procedure",
     "Statutory rule barring courts from re-trying a suit or issue conclusively decided between same parties",
     "Codified under Section 11 of Code of Civil Procedure, 1908; based on public policy to end litigation",
     "A doctrine precluding parties from re-litigating a matter on which a final judgment has already been rendered.",
     "Having lost a title suit up to the High Court, a party cannot file a fresh suit on the same cause of action.",
     "Code of Civil Procedure, 1908, Section 11; Satyadhyan Ghosal v. Deorajin Debi (AIR 1960 SC 941)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-067", "RES SUB JUDICE", "intermediate", "Civil Procedure",
     "Rule mandating stay of trial of a subsequently instituted suit where matter in issue is directly pending in a prior suit",
     "Codified under Section 10 of Code of Civil Procedure, 1908; prevents conflicting judicial decrees",
     "The procedural requirement staying the trial of a later suit when an identical dispute is already pending.",
     "When a second partition suit regarding identical ancestral property was filed in another district, it was stayed under Section 10.",
     "Code of Civil Procedure, 1908, Section 10; National Institute of Mental Health v. C. Parameshwara (2005 2 SCC 256)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-068", "PLAINT", "beginner", "Civil Procedure",
     "The statement of claim in writing through which a civil suit is formally instituted by a plaintiff",
     "Governed by Order VII of CPC; must state material facts, cause of action, valuation, and relief",
     "The formal written pleading wherein a plaintiff sets forth the cause of action and prayers seeking relief.",
     "The trial court rejected the plaint under Order VII Rule 11 CPC because it failed to disclose a valid cause of action.",
     "Code of Civil Procedure, 1908, Section 26 & Order VII; Saleem Bhai v. State of Maharashtra (2003 1 SCC 557)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-069", "WRITTEN STATEMENT", "beginner", "Civil Procedure",
     "The formal statement of defense filed by a defendant responding specifically to plaintiff's plaint",
     "Governed by Order VIII of CPC; must be filed within 30 days, extendable up to 90/120 days",
     "The pleading filed by a defendant setting up defenses, denying allegations, or asserting set-off.",
     "General denials are insufficient; the defendant must specifically deal with each allegation of fact in the written statement.",
     "Code of Civil Procedure, 1908, Order VIII Rule 1; Kailash v. Nanhku (2005 4 SCC 480)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-070", "INJUNCTION", "beginner", "Civil Procedure",
     "Judicial order restraining a party from doing an act or compelling performance of a restorative act",
     "Temporary injunctions governed by Order XXXIX CPC; perpetual injunctions governed by Specific Relief Act Section 38",
     "A court decree or order commanding a party to refrain from doing or to perform a specified act.",
     "The court granted an ad-interim temporary injunction restraining the defendant from demolishing the common boundary wall.",
     "Code of Civil Procedure, 1908, Order XXXIX Rules 1 & 2; Dalpat Kumar v. Prahlad Singh (1992 1 SCC 719)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-071", "DECREE", "beginner", "Civil Procedure",
     "Formal expression of an adjudication conclusively determining the rights of parties with regard to all or any matters in controversy",
     "Defined in Section 2(2) CPC; includes preliminary and final decrees, and rejection of plaint",
     "The formal judicial declaration resolving the substantive disputes in a civil suit conclusively.",
     "In a suit for partition, the court first passes a preliminary decree defining shares before the final division decree.",
     "Code of Civil Procedure, 1908, Section 2(2); Phoolchand v. Gopal Lal (AIR 1967 SC 1470)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-072", "JUDGMENT", "beginner", "Civil Procedure",
     "The statement given by the Judge on the grounds of a decree or order",
     "Defined under Section 2(9) and Order XX of CPC; contains concise statement of case, points for determination, decision, and reasons",
     "The formal reasoned expression of the court containing legal findings upon which a decree is founded.",
     "A judgment must contain sound judicial reasoning justifying each framed issue before the formal decree can be drawn.",
     "Code of Civil Procedure, 1908, Section 2(9) & Order XX Rule 4; Balraj Taneja v. Sunil Madan (1999 8 SCC 396)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-073", "MESNE PROFITS", "intermediate", "Civil Procedure",
     "Profits which person in wrongful possession actually received or might with ordinary diligence have received, with interest",
     "Defined in Section 2(12) of CPC; does not include profits due to improvements made by wrongful possessor",
     "Damages awarded to the true owner representing compensation for unauthorized occupation of immovable property.",
     "Upon decreeing possession of the commercial showroom, the court directed an inquiry into mesne profits under Order XX Rule 12.",
     "Code of Civil Procedure, 1908, Section 2(12); Lucy Kochuwareed v. P. Mariappa Gounder (1979 3 SCC 150)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-074", "GARNISHEE", "advanced", "Civil Procedure",
     "Third party indebted to a judgment-debtor who is ordered by court to pay the debt directly to decree-holder",
     "Governed by Order XXI Rules 46A to 46-I of CPC; common execution procedure for bank deposits",
     "A person who holds money owed to a judgment-debtor and is subject to a court attachment order.",
     "The court issued a garnishee order attaching the judgment-debtor's fixed deposit lying in the nationalized bank.",
     "Code of Civil Procedure, 1908, Order XXI Rule 46A; F.G.P. Ltd. v. Saleh Hooseini Doctor (2009 10 SCC 223)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-075", "INTERPLEADER", "intermediate", "Civil Procedure",
     "Suit where plaintiff claims no interest in subject-matter other than charges and asks competing claimants to litigate between themselves",
     "Governed by Section 88 and Order XXXV of CPC; plaintiff must not collude with either defendant",
     "A proceeding enabling a neutral stakeholder to require rival claimants to resolve their competing entitlements in court.",
     "An auctioneer holding proceeds of sale claimed by both buyer and mortgagee filed an interpleader suit.",
     "Code of Civil Procedure, 1908, Section 88 & Order XXXV; Asanalli v. Mansooralli (AIR 1948 Nag 326)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-076", "SET OFF", "intermediate", "Civil Procedure",
     "Statutory cross-claim for ascertained sum of money legally recoverable by defendant from plaintiff in a money recovery suit",
     "Order VIII Rule 6 CPC; both debts must be mutual and legally recoverable at the date of suit",
     "A plea whereby a defendant seeks to extinguish or reduce plaintiff's money claim through a mutual existing debt.",
     "In a suit for Rs 50,000 for supplied goods, defendant pleaded set-off of Rs 20,000 previously loaned to plaintiff.",
     "Code of Civil Procedure, 1908, Order VIII Rule 6; Union of India v. Karam Chand Thapar (2004 3 SCC 504)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-077", "COUNTERCLAIM", "intermediate", "Civil Procedure",
     "Independent cross-action brought by defendant against plaintiff in a suit, treated as a cross-plaint",
     "Governed by Order VIII Rules 6A to 6G CPC; can exceed the pecuniary limits of the original plaint",
     "A formal claim raised by the defendant against the plaintiff that could have formed the basis of an independent suit.",
     "In an eviction suit, the defendant raised a counterclaim seeking specific performance of an oral agreement of sale.",
     "Code of Civil Procedure, 1908, Order VIII Rule 6A; Jag Mohan Chawla v. Dera Radha Swami Satsang (1996 4 SCC 699)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-078", "RESTITUTION", "intermediate", "Civil Procedure",
     "Duty of the court to place parties in the original position they would have occupied but for an erroneous decree reversed in appeal",
     "Codified under Section 144 of CPC; based on maxim 'Actus curiae neminem gravabit'",
     "The restoration of property or benefit wrongfully taken from a party pursuant to an erroneous decree subsequently set aside.",
     "When an eviction decree was reversed in second appeal, the tenant was restored to physical possession under Section 144 CPC.",
     "Code of Civil Procedure, 1908, Section 144; South Eastern Coalfields Ltd. v. State of M.P. (2003 8 SCC 648)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-079", "REVISION", "intermediate", "Civil Procedure",
     "Supervisory jurisdiction of the High Court to correct non-appealable jurisdictional errors of subordinate courts",
     "Governed by Section 115 CPC; limited to acting without jurisdiction, failing to exercise it, or material irregularity",
     "The procedural power of a superior court to examine the record of a subordinate court for jurisdictional defects.",
     "The High Court exercised civil revisional jurisdiction to overturn an order refusing to reject a time-barred plaint.",
     "Code of Civil Procedure, 1908, Section 115; Shiv Shakti Coop. Housing Society v. Swaraj Developers (2003 6 SCC 659)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-080", "REVIEW", "intermediate", "Civil Procedure",
     "Re-examination of its own decree or order by the same court on grounds of error apparent on face of record",
     "Governed by Section 114 and Order XLVII CPC; discovery of new evidence or mistake apparent on face of record",
     "The reconsideration of a judgment by the very court that pronounced it, strictly confined to patent errors.",
     "A review petition cannot be an appeal in disguise; it lies only for manifest errors apparent without detailed rehearing.",
     "Code of Civil Procedure, 1908, Section 114 & Order XLVII; Kamlesh Verma v. Mayawati (2013 8 SCC 320)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-081", "REFERENCE", "advanced", "Civil Procedure",
     "Subordinate court seeking opinion of High Court on a question of law or validity of an Act/Regulation",
     "Governed by Section 113 and Order XLVI CPC; necessary when reasonable doubt arises on a point of statutory validity",
     "The procedure whereby a subordinate trial court submits an unresolved question of legal validity to the High Court for ruling.",
     "The civil judge referred the question of constitutionality of a local tenancy regulation to the High Court under Section 113.",
     "Code of Civil Procedure, 1908, Section 113 & Order XLVI",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-082", "CAVEAT", "beginner", "Civil Procedure",
     "Formal notice filed by a party requesting court not to pass any order without prior notice to the caveator",
     "Governed by Section 148A of CPC; remains in force for 90 days from the date of filing",
     "A precautionary warning lodged in court ensuring a party is heard before any ex-parte relief is granted to an adversary.",
     "Anticipating an ex-parte stay against demolition, the municipal council lodged a caveat under Section 148A.",
     "Code of Civil Procedure, 1908, Section 148A; Deepak Khosla v. Union of India (2011 4 Comp LJ 368 Del)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-083", "EX PARTE", "beginner", "Civil Procedure",
     "Proceedings conducted or orders passed in the absence of one of the parties who failed to appear despite notice",
     "Governed by Order IX Rule 6 CPC; remedy to set aside ex parte decree lies under Order IX Rule 13",
     "A judicial act performed or decree pronounced by the court when only one party is present.",
     "Because the defendant failed to appear after registered summons service, the court passed an ex parte eviction decree.",
     "Code of Civil Procedure, 1908, Order IX Rules 6 & 13; G.P. Srivastava v. R.K. Raizada (2000 3 SCC 54)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-084", "AMICUS CURIAE", "intermediate", "Civil Procedure",
     "A neutral advocate appointed by the court as a 'friend of the court' to assist on complex questions of law",
     "Latin legal term; owes allegiance to judicial justice rather than to any litigant in the suit",
     "An impartial legal specialist invited by the court to advise on matters of public importance or novel legal complexity.",
     "In a public interest case on prison conditions, the High Court appointed a senior advocate as amicus curiae.",
     "Supreme Court Rules, 2013; Re: Ramlila Maidan Incident (2012 5 SCC 1)",
     "https://main.sci.gov.in/judgments"),

    ("voc-085", "ATTACHMENT", "intermediate", "Civil Procedure",
     "Judicial seizure or freezing of a debtor's property to hold it subject to satisfaction of a decree",
     "Attachment before judgment governed by Order XXXVIII; execution attachment governed by Order XXI CPC",
     "The legal process taking custody of a debtor's assets to secure payment of a judgment debt.",
     "Plaintiff proved defendant was secretly selling off properties to defeat the decree, securing attachment before judgment.",
     "Code of Civil Procedure, 1908, Section 60 & Order XXXVIII Rule 5; Raman Tech. v. Bharat Components (2008 8 SCC 327)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-086", "SUBPOENA", "intermediate", "Civil Procedure",
     "Court order summoning a person to testify as a witness or produce specific documents under penalty",
     "Corresponds to summons to witness under Order XVI of CPC",
     "A compulsory writ commanding an individual's appearance in court to give oral evidence or present documents.",
     "The court issued a subpoena duces tecum directing the registrar to produce the original volume of deed records.",
     "Code of Civil Procedure, 1908, Order XVI Rules 1 & 10",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-087", "INTERLOCUTORY", "intermediate", "Civil Procedure",
     "Provisional or interim order passed during the pendency of a suit that does not finally dispose of the case",
     "Governed by Order XXXIX (Injunctions) and Order XL (Receivers) CPC",
     "An order deciding an intermediate procedural matter or granting temporary relief pending trial.",
     "An order granting temporary child custody during a matrimonial trial is an interlocutory order.",
     "Code of Civil Procedure, 1908, Section 104 & Order XXXIX; Madhu Limaye v. State of Maharashtra (1977 4 SCC 551)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-088", "COMMISSION", "intermediate", "Civil Procedure",
     "Authority issued by court to a person to conduct local investigation, examine witnesses, or inspect accounts",
     "Governed by Section 75 and Order XXVI CPC; commissioner's report forms part of the record",
     "A warrant authorizing an appointed advocate or expert to perform an inspection or examine incapacitated witnesses.",
     "In a boundary encroachment suit, the judge appointed an advocate commissioner with a surveyor to measure disputed land.",
     "Code of Civil Procedure, 1908, Section 75 & Order XXVI Rule 9; Haryana Waqf Board v. Shanti Sarup (2008 8 SCC 671)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-089", "RECEIVER", "intermediate", "Civil Procedure",
     "Neutral officer appointed by court under Order XL to manage, preserve, and protect property during litigation",
     "Equitable remedy granted when property is in danger of being wasted, damaged, or alienated",
     "An impartial custodian appointed by court to manage property in dispute pending final adjudication.",
     "To prevent diversion of factory profits during a bitter partnership dissolution, the court appointed an official receiver.",
     "Code of Civil Procedure, 1908, Order XL Rule 1; T. Krishnaswamy Chetty v. C. Thangavelu Chetty (AIR 1955 Mad 430)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-090", "LIS PENDENS", "intermediate", "Civil Procedure",
     "Doctrine that property in active litigation cannot be transferred so as to affect the rights of any party under decree",
     "Codified in Section 52 of Transfer of Property Act, 1882; based on maxim 'Pendente lite nihil innovetur'",
     "The principle that the transfer of a disputed property pending a lawsuit remains subject to the court's ultimate decree.",
     "Purchasers who buy suit property during pendency of a partition appeal take title strictly subject to the final decree.",
     "Transfer of Property Act, 1882, Section 52; Jayaram Mudaliar v. Ayyaswami (1972 2 SCC 200)",
     "https://www.indiacode.nic.in/handle/123456789/2338"),

    ("voc-091", "AFFIDAVIT", "beginner", "Civil Procedure",
     "Voluntary statement of facts sworn or affirmed in writing before an authorized oath commissioner or notary",
     "Governed by Order XIX of CPC; must state facts within deponent's personal knowledge, distinguishing belief",
     "A written solemn declaration of facts made on oath or affirmation before an authorized judicial officer.",
     "The interlocutory application for temporary injunction was supported by an affidavit verifying urgent danger.",
     "Code of Civil Procedure, 1908, Order XIX Rules 1-3; A.K.K. Nambiar v. Union of India (AIR 1970 SC 652)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-092", "EXECUTION", "beginner", "Civil Procedure",
     "The formal judicial enforcement of a court decree or order through attachment, sale, or arrest",
     "Governed by Order XXI CPC; longest and most comprehensive procedural order in Indian law",
     "The final phase of a civil lawsuit wherein the successful litigant obtains the fruits of the decree.",
     "The decree-holder filed an execution application under Order XXI Rule 11 seeking warrant for delivery of possession.",
     "Code of Civil Procedure, 1908, Sections 36-74 & Order XXI; Rahul S. Shah v. Jinendra Kumar Gandhi (2021 6 SCC 418)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-093", "REPRESENTATIVE SUIT", "advanced", "Civil Procedure",
     "Suit filed by or against numerous persons having the same interest in one suit with permission of court",
     "Governed by Order I Rule 8 CPC; requires public advertisement and court sanction",
     "A lawsuit instituted by named individuals representing a broad class of persons sharing an identical community of interest.",
     "Four villagers filed a representative suit on behalf of the entire village to protect community grazing pastures.",
     "Code of Civil Procedure, 1908, Order I Rule 8; Chairman, Tamil Nadu Housing Board v. T.N. Ganapathy (1990 1 SCC 608)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-094", "ABATEMENT", "intermediate", "Civil Procedure",
     "Termination or suspension of a suit upon death of a party if the legal representatives are not brought on record in time",
     "Governed by Order XXII CPC; abatement operates automatically after 90 days if no substitution application is made",
     "The legal cessation of a lawsuit upon death of a plaintiff or defendant where the right to sue survives but is not pursued.",
     "The partition suit abated against the deceased defendant because no substitution petition was filed within 90 days.",
     "Code of Civil Procedure, 1908, Order XXII Rules 3 & 4; Mithailal Dalsangar Singh v. Kiran Devi (2003 10 SCC 691)",
     "https://www.indiacode.nic.in/handle/123456789/2191"),

    ("voc-095", "INHERENT POWERS", "advanced", "Civil Procedure",
     "Residual judicial power of the civil court under Section 151 CPC to make orders necessary for ends of justice",
     "Inherent authority codified in Section 151 CPC; cannot override express statutory prohibitions",
     "The intrinsic residual power of a court to do complete justice and prevent abuse of the process of the court.",
     "Where the procedural rules were silent, the trial court invoked inherent powers under Section 151 to stay parallel inquiry.",
     "Code of Civil Procedure, 1908, Section 151; Manohar Lal Chopra v. Rai Bahadur Rao Raja Seth Hiralal (AIR 1962 SC 527)",
     "https://www.indiacode.nic.in/handle/123456789/2191")
]

for t in CPC_ITEMS:
    ALL_ITEMS.append({
        "id": t[0],
        "canonical": t[1],
        "acceptedVariants": [t[1]],
        "difficulty": t[2],
        "subject": t[3],
        "primaryClue": t[4],
        "additionalHint": t[5],
        "definition": t[6],
        "educationalExample": t[7],
        "statuteOrAuthority": t[8],
        "sourceUrl": t[9],
        "verificationDate": "2026-11-22"
    })

print(f"Total items after CPC: {len(ALL_ITEMS)}")
