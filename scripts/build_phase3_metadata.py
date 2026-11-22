"""
Builder script to generate Chapter and Topic metadata for Phase 3:
- Criminal Law (BNS & IPC): 12 Chapters, 32 Topics
- Criminal Procedure (BNSS & CrPC): 12 Chapters, 32 Topics
- Law of Evidence (BSA & IEA): 10 Chapters, 26 Topics
Total: 34 Chapters, 90 Topics
"""

import json

# ==============================================================================
# 1. CRIMINAL LAW (12 Chapters, 32 Topics)
# ==============================================================================
CRIM_CHAPTERS = [
    {
        "id": "ch-crim-01",
        "subjectId": "law-criminal",
        "number": 1,
        "title": "Introduction, Territorial Application & General Explanations",
        "scope": "Title, commencement (1 July 2024), territorial jurisdiction, extra-territorial offences, and cardinal statutory definitions under BNS & IPC",
        "topicsCount": 3,
        "mcqsCount": 30,
        "pyqsCount": 6,
        "estimatedMinutes": 60,
        "weightage": "High"
    },
    {
        "id": "ch-crim-02",
        "subjectId": "law-criminal",
        "number": 2,
        "title": "Punishments & Sentencing Framework",
        "scope": "Theories of punishment, death penalty, life imprisonment, solitary confinement, community service under BNS, commutation, and remission",
        "topicsCount": 2,
        "mcqsCount": 20,
        "pyqsCount": 4,
        "estimatedMinutes": 45,
        "weightage": "Medium"
    },
    {
        "id": "ch-crim-03",
        "subjectId": "law-criminal",
        "number": 3,
        "title": "General Exceptions: Excusable & Justifiable Acts",
        "scope": "Mistake of fact, judicial acts, infancy (doli incapax), insanity (M'Naghten rules), intoxication, consent, communication in good faith, and trivial acts",
        "topicsCount": 4,
        "mcqsCount": 40,
        "pyqsCount": 10,
        "estimatedMinutes": 80,
        "weightage": "Very High"
    },
    {
        "id": "ch-crim-04",
        "subjectId": "law-criminal",
        "number": 4,
        "title": "Right of Private Defence of Body & Property",
        "scope": "Nature and limits of private defence, commencement and continuance, when defence extends to causing death of body and property",
        "topicsCount": 3,
        "mcqsCount": 30,
        "pyqsCount": 7,
        "estimatedMinutes": 60,
        "weightage": "Very High"
    },
    {
        "id": "ch-crim-05",
        "subjectId": "law-criminal",
        "number": 5,
        "title": "Inchoate Crimes: Joint Liability, Abetment, Conspiracy & Attempt",
        "scope": "Joint liability (S. 3(5) BNS vs S. 34 IPC), Common object (S. 190 BNS vs S. 149 IPC), Abetment, Criminal Conspiracy, and Attempt to commit offences",
        "topicsCount": 4,
        "mcqsCount": 40,
        "pyqsCount": 9,
        "estimatedMinutes": 75,
        "weightage": "Very High"
    },
    {
        "id": "ch-crim-06",
        "subjectId": "law-criminal",
        "number": 6,
        "title": "Offences Against Human Body: Homicide, Murder & Fatal Injuries",
        "scope": "Culpable homicide vs Murder (S. 100/101 BNS vs S. 299/300 IPC), 5 Exceptions, Rarest of rare doctrine, Rash/negligent death (S. 106 caveat), Dowry death, and Mob lynching",
        "topicsCount": 4,
        "mcqsCount": 50,
        "pyqsCount": 14,
        "estimatedMinutes": 90,
        "weightage": "Very High"
    },
    {
        "id": "ch-crim-07",
        "subjectId": "law-criminal",
        "number": 7,
        "title": "Offences Against Human Body: Hurt, Restraint & Kidnapping",
        "scope": "Hurt and Grievous hurt (8 clauses), Acid attack, Wrongful restraint & confinement, Kidnapping vs Abduction, and Human trafficking",
        "topicsCount": 3,
        "mcqsCount": 30,
        "pyqsCount": 6,
        "estimatedMinutes": 60,
        "weightage": "High"
    },
    {
        "id": "ch-crim-08",
        "subjectId": "law-criminal",
        "number": 8,
        "title": "Offences Against Women & Children",
        "scope": "Rape (S. 63 BNS vs S. 375 IPC), Consent & Age thresholds, Assault/criminal force to woman, Voyeurism, Stalking, Cruelty by husband (S. 84 BNS vs S. 498A IPC)",
        "topicsCount": 3,
        "mcqsCount": 40,
        "pyqsCount": 8,
        "estimatedMinutes": 75,
        "weightage": "Very High"
    },
    {
        "id": "ch-crim-09",
        "subjectId": "law-criminal",
        "number": 9,
        "title": "Offences Against Property: Theft, Extortion, Robbery & Dacoity",
        "scope": "Theft, Extortion, Robbery, Dacoity, Criminal misappropriation, Criminal breach of trust, Cheating, Mischief, and Criminal trespass",
        "topicsCount": 3,
        "mcqsCount": 40,
        "pyqsCount": 8,
        "estimatedMinutes": 75,
        "weightage": "Very High"
    },
    {
        "id": "ch-crim-10",
        "subjectId": "law-criminal",
        "number": 10,
        "title": "Offences Against State & Public Tranquility",
        "scope": "Endangering sovereignty, unity & integrity of India (S. 152 BNS), Terrorism (S. 113 BNS), Organised crime (S. 111 BNS), Unlawful assembly, Rioting, and Affray",
        "topicsCount": 3,
        "mcqsCount": 30,
        "pyqsCount": 4,
        "estimatedMinutes": 60,
        "weightage": "High"
    },
    {
        "id": "ch-crim-11",
        "subjectId": "law-criminal",
        "number": 11,
        "title": "Offences Against Public Justice & False Evidence",
        "scope": "Giving and fabricating false evidence (Perjury), Offences against public justice, Contempt of lawful authority of public servants, and Harboring offenders",
        "topicsCount": 2,
        "mcqsCount": 20,
        "pyqsCount": 3,
        "estimatedMinutes": 45,
        "weightage": "Medium"
    },
    {
        "id": "ch-crim-12",
        "subjectId": "law-criminal",
        "number": 12,
        "title": "Offences Affecting Reputation, Documents & Criminal Intimidation",
        "scope": "Forgery, Making false document/electronic records, Criminal intimidation, Insult, Annoyance, Defamation and Community service sanctions",
        "topicsCount": 2,
        "mcqsCount": 20,
        "pyqsCount": 3,
        "estimatedMinutes": 45,
        "weightage": "Medium"
    }
]

CRIM_TOPICS = [
    # Ch 1
    {"id": "top-crim-01-01", "chapterId": "ch-crim-01", "subjectId": "law-criminal", "title": "Title, Territorial Scope & Commencement (1 July 2024)", "order": 1, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    {"id": "top-crim-01-02", "chapterId": "ch-crim-01", "subjectId": "law-criminal", "title": "Statutory Definitions & Interpretations in BNS & IPC", "order": 2, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    {"id": "top-crim-01-03", "chapterId": "ch-crim-01", "subjectId": "law-criminal", "title": "Actus Reus, Mens Rea & Strict Liability in Penal Law", "order": 3, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    # Ch 2
    {"id": "top-crim-02-01", "chapterId": "ch-crim-02", "subjectId": "law-criminal", "title": "Sentencing Framework & Community Service under BNS", "order": 1, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 22},
    {"id": "top-crim-02-02", "chapterId": "ch-crim-02", "subjectId": "law-criminal", "title": "Solitary Confinement, Commutation & Limit of Punishments", "order": 2, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 23},
    # Ch 3
    {"id": "top-crim-03-01", "chapterId": "ch-crim-03", "subjectId": "law-criminal", "title": "Mistake of Fact vs Mistake of Law & Judicial Acts", "order": 1, "mcqsCount": 10, "pyqsCount": 3, "estimatedMinutes": 20},
    {"id": "top-crim-03-02", "chapterId": "ch-crim-03", "subjectId": "law-criminal", "title": "Infancy (Doli Incapax) & Insanity: M'Naghten Rules", "order": 2, "mcqsCount": 10, "pyqsCount": 3, "estimatedMinutes": 20},
    {"id": "top-crim-03-03", "chapterId": "ch-crim-03", "subjectId": "law-criminal", "title": "Involuntary vs Voluntary Intoxication (Basdev Doctrine)", "order": 3, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    {"id": "top-crim-03-04", "chapterId": "ch-crim-03", "subjectId": "law-criminal", "title": "Consent, Good Faith Medical Acts & Trivial Acts (De Minimis)", "order": 4, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    # Ch 4
    {"id": "top-crim-04-01", "chapterId": "ch-crim-04", "subjectId": "law-criminal", "title": "Nature, Scope and Statutory Limits of Private Defence", "order": 1, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    {"id": "top-crim-04-02", "chapterId": "ch-crim-04", "subjectId": "law-criminal", "title": "Private Defence of Body: When Extends to Causing Death", "order": 2, "mcqsCount": 10, "pyqsCount": 3, "estimatedMinutes": 20},
    {"id": "top-crim-04-03", "chapterId": "ch-crim-04", "subjectId": "law-criminal", "title": "Private Defence of Property: Extent and Causing Death", "order": 3, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    # Ch 5
    {"id": "top-crim-05-01", "chapterId": "ch-crim-05", "subjectId": "law-criminal", "title": "Common Intention vs Common Object: Joint Criminal Liability", "order": 1, "mcqsCount": 10, "pyqsCount": 3, "estimatedMinutes": 20},
    {"id": "top-crim-05-02", "chapterId": "ch-crim-05", "subjectId": "law-criminal", "title": "Abetment: Instigation, Conspiracy & Intentional Aiding", "order": 2, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    {"id": "top-crim-05-03", "chapterId": "ch-crim-05", "subjectId": "law-criminal", "title": "Criminal Conspiracy: Agreement, Mens Rea & Evidence", "order": 3, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    {"id": "top-crim-05-04", "chapterId": "ch-crim-05", "subjectId": "law-criminal", "title": "Criminal Attempt: Preparation vs Attempt & Proximity Test", "order": 4, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 15},
    # Ch 6
    {"id": "top-crim-06-01", "chapterId": "ch-crim-06", "subjectId": "law-criminal", "title": "Culpable Homicide vs Murder: S. 100/101 BNS & S. 299/300 IPC", "order": 1, "mcqsCount": 15, "pyqsCount": 5, "estimatedMinutes": 25},
    {"id": "top-crim-06-02", "chapterId": "ch-crim-06", "subjectId": "law-criminal", "title": "The Five Exceptions to Murder & Provocation Doctrine", "order": 2, "mcqsCount": 15, "pyqsCount": 4, "estimatedMinutes": 25},
    {"id": "top-crim-06-03", "chapterId": "ch-crim-06", "subjectId": "law-criminal", "title": "Rash & Negligent Death: S. 106(1) & S. 106(2) BNS Caveat", "order": 3, "mcqsCount": 10, "pyqsCount": 3, "estimatedMinutes": 20},
    {"id": "top-crim-06-04", "chapterId": "ch-crim-06", "subjectId": "law-criminal", "title": "Dowry Death, Abetment of Suicide & Mob Lynching Provisions", "order": 4, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    # Ch 7
    {"id": "top-crim-07-01", "chapterId": "ch-crim-07", "subjectId": "law-criminal", "title": "Hurt and Grievous Hurt: Eight Statutory Clauses & Acid Attack", "order": 1, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    {"id": "top-crim-07-02", "chapterId": "ch-crim-07", "subjectId": "law-criminal", "title": "Wrongful Restraint & Wrongful Confinement", "order": 2, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    {"id": "top-crim-07-03", "chapterId": "ch-crim-07", "subjectId": "law-criminal", "title": "Kidnapping vs Abduction & Human Trafficking Framework", "order": 3, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    # Ch 8
    {"id": "top-crim-08-01", "chapterId": "ch-crim-08", "subjectId": "law-criminal", "title": "Rape: Definition, Consent, Age Thresholds & Aggravated Offences", "order": 1, "mcqsCount": 15, "pyqsCount": 3, "estimatedMinutes": 25},
    {"id": "top-crim-08-02", "chapterId": "ch-crim-08", "subjectId": "law-criminal", "title": "Outraging Modesty, Sexual Harassment, Voyeurism & Stalking", "order": 2, "mcqsCount": 15, "pyqsCount": 3, "estimatedMinutes": 25},
    {"id": "top-crim-08-03", "chapterId": "ch-crim-08", "subjectId": "law-criminal", "title": "Cruelty by Husband/Relatives & Deceitful Marriage Offences", "order": 3, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 25},
    # Ch 9
    {"id": "top-crim-09-01", "chapterId": "ch-crim-09", "subjectId": "law-criminal", "title": "Theft, Extortion, Robbery & Dacoity: The Gradation Spectrum", "order": 1, "mcqsCount": 15, "pyqsCount": 3, "estimatedMinutes": 25},
    {"id": "top-crim-09-02", "chapterId": "ch-crim-09", "subjectId": "law-criminal", "title": "Criminal Misappropriation & Criminal Breach of Trust", "order": 2, "mcqsCount": 15, "pyqsCount": 3, "estimatedMinutes": 25},
    {"id": "top-crim-09-03", "chapterId": "ch-crim-09", "subjectId": "law-criminal", "title": "Cheating, Mischief, Criminal Trespass & House-breaking", "order": 3, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 25},
    # Ch 10
    {"id": "top-crim-10-01", "chapterId": "ch-crim-10", "subjectId": "law-criminal", "title": "Acts Endangering Sovereignty & Integrity of India (S. 152 BNS)", "order": 1, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-crim-10-02", "chapterId": "ch-crim-10", "subjectId": "law-criminal", "title": "Terrorism & Organised Crime in BNS (S. 111, 112, 113)", "order": 2, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-crim-10-03", "chapterId": "ch-crim-10", "subjectId": "law-criminal", "title": "Unlawful Assembly, Rioting & Affray", "order": 3, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    # Ch 11
    {"id": "top-crim-11-01", "chapterId": "ch-crim-11", "subjectId": "law-criminal", "title": "Giving and Fabricating False Evidence: Perjury & Sanctions", "order": 1, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 22},
    {"id": "top-crim-11-02", "chapterId": "ch-crim-11", "subjectId": "law-criminal", "title": "Contempt of Lawful Authority of Public Servants", "order": 2, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 23},
    # Ch 12
    {"id": "top-crim-12-01", "chapterId": "ch-crim-12", "subjectId": "law-criminal", "title": "Forgery, False Documents & Electronic Records (BNS S. 336)", "order": 1, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 22},
    {"id": "top-crim-12-02", "chapterId": "ch-crim-12", "subjectId": "law-criminal", "title": "Criminal Intimidation, Insult, Annoyance & Defamation", "order": 2, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 23}
]

# ==============================================================================
# 2. CRIMINAL PROCEDURE (12 Chapters, 32 Topics)
# ==============================================================================
CRPC_CHAPTERS = [
    {
        "id": "ch-crpc-01",
        "subjectId": "law-crpc",
        "number": 1,
        "title": "Constitution & Hierarchy of Criminal Courts & Prosecutors",
        "scope": "Classes of criminal courts, territorial divisions, powers to pass sentences, separation of judiciary, and Directorate of Prosecution under BNSS & CrPC",
        "topicsCount": 3,
        "mcqsCount": 30,
        "pyqsCount": 5,
        "estimatedMinutes": 60,
        "weightage": "High"
    },
    {
        "id": "ch-crpc-02",
        "subjectId": "law-crpc",
        "number": 2,
        "title": "Powers of Police & Arrest of Persons",
        "scope": "Arrest without warrant, notice of appearance (S. 35 BNSS / S. 41A CrPC), handcuff regulation, search of arrestee, and rights of arrested persons (24-hour rule)",
        "topicsCount": 3,
        "mcqsCount": 35,
        "pyqsCount": 6,
        "estimatedMinutes": 65,
        "weightage": "Very High"
    },
    {
        "id": "ch-crpc-03",
        "subjectId": "law-crpc",
        "number": 3,
        "title": "Processes to Compel Appearance & Production of Things",
        "scope": "Summons, warrant of arrest, proclamation and attachment of property (S. 84 BNSS / S. 82 CrPC), search warrants, and impounding documents",
        "topicsCount": 3,
        "mcqsCount": 30,
        "pyqsCount": 4,
        "estimatedMinutes": 60,
        "weightage": "High"
    },
    {
        "id": "ch-crpc-04",
        "subjectId": "law-crpc",
        "number": 4,
        "title": "Security Proceedings, Public Order & Urgent Injunctions",
        "scope": "Security for keeping peace and good behaviour, unlawful assemblies, urgent orders in nuisance/danger (S. 163 BNSS / S. 144 CrPC), and immovable property disputes",
        "topicsCount": 3,
        "mcqsCount": 30,
        "pyqsCount": 4,
        "estimatedMinutes": 60,
        "weightage": "High"
    },
    {
        "id": "ch-crpc-05",
        "subjectId": "law-crpc",
        "number": 5,
        "title": "Maintenance of Wives, Children & Parents",
        "scope": "Statutory maintenance under S. 144 BNSS / S. 125 CrPC, neglected dependants, interim maintenance, alteration, enforcement, and landmark precedents",
        "topicsCount": 2,
        "mcqsCount": 25,
        "pyqsCount": 5,
        "estimatedMinutes": 50,
        "weightage": "Very High"
    },
    {
        "id": "ch-crpc-06",
        "subjectId": "law-crpc",
        "number": 6,
        "title": "Information to Police, FIR & Powers of Investigation",
        "scope": "FIR (S. 173 BNSS / S. 154 CrPC), Zero FIR, E-FIR, preliminary inquiry, investigation powers, witness examination (S. 180 BNSS / S. 161 CrPC), and confessions (S. 183 BNSS / S. 164 CrPC)",
        "topicsCount": 3,
        "mcqsCount": 40,
        "pyqsCount": 6,
        "estimatedMinutes": 75,
        "weightage": "Very High"
    },
    {
        "id": "ch-crpc-07",
        "subjectId": "law-crpc",
        "number": 7,
        "title": "Remand, Police Custody & Final Police Report",
        "scope": "Remand under S. 187 BNSS / S. 167 CrPC (15-day custody in 40/60 days), default bail, medical inquest, and police closure/charge-sheet (S. 193 BNSS / S. 173 CrPC)",
        "topicsCount": 2,
        "mcqsCount": 30,
        "pyqsCount": 4,
        "estimatedMinutes": 55,
        "weightage": "Very High"
    },
    {
        "id": "ch-crpc-08",
        "subjectId": "law-crpc",
        "number": 8,
        "title": "Jurisdiction & Cognizance of Offences by Criminal Courts",
        "scope": "Ordinary place of inquiry/trial, special territorial rules, cognizance by Magistrates (S. 210 BNSS / S. 190 CrPC), sanction for prosecution, and complaint procedure",
        "topicsCount": 3,
        "mcqsCount": 30,
        "pyqsCount": 4,
        "estimatedMinutes": 60,
        "weightage": "High"
    },
    {
        "id": "ch-crpc-09",
        "subjectId": "law-crpc",
        "number": 9,
        "title": "The Charge & Joinder of Charges",
        "scope": "Contents of charge, particulars of time/place/person, effect of errors, alteration of charge, separate trials rule, and statutory exceptions to separate trials",
        "topicsCount": 2,
        "mcqsCount": 25,
        "pyqsCount": 3,
        "estimatedMinutes": 50,
        "weightage": "High"
    },
    {
        "id": "ch-crpc-10",
        "subjectId": "law-crpc",
        "number": 10,
        "title": "Trial Procedures: Sessions, Warrant, Summons & Summary Trials",
        "scope": "Sessions trial, Warrant trial (police case vs complaint), Summons trial, Summary trial, Plea bargaining, and Trial in absentia of proclaimed offenders (S. 356 BNSS)",
        "topicsCount": 4,
        "mcqsCount": 45,
        "pyqsCount": 4,
        "estimatedMinutes": 80,
        "weightage": "Very High"
    },
    {
        "id": "ch-crpc-11",
        "subjectId": "law-crpc",
        "number": 11,
        "title": "General Provisions as to Inquiries, Trials & Inherent Powers",
        "scope": "Double jeopardy (Autrefois acquit/convict), right to legal aid, examination of accused (S. 351 BNSS / S. 313 CrPC), tender of pardon, S. 319 CrPC / S. 358 BNSS, and S. 528 BNSS / S. 482 CrPC",
        "topicsCount": 3,
        "mcqsCount": 35,
        "pyqsCount": 4,
        "estimatedMinutes": 65,
        "weightage": "Very High"
    },
    {
        "id": "ch-crpc-12",
        "subjectId": "law-crpc",
        "number": 12,
        "title": "Bail Jurisprudence, Appeals, Reference & Revision",
        "scope": "Bailable vs Non-bailable bail, undertrial release (S. 479 BNSS vs S. 436A CrPC), anticipatory bail (S. 482 BNSS / S. 438 CrPC), judgments, appeals, reference, and revision",
        "topicsCount": 4,
        "mcqsCount": 45,
        "pyqsCount": 4,
        "estimatedMinutes": 80,
        "weightage": "Very High"
    }
]

CRPC_TOPICS = [
    # Ch 1
    {"id": "top-crpc-01-01", "chapterId": "ch-crpc-01", "subjectId": "law-crpc", "title": "Hierarchy & Classes of Criminal Courts in BNSS & CrPC", "order": 1, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    {"id": "top-crpc-01-02", "chapterId": "ch-crpc-01", "subjectId": "law-crpc", "title": "Sentencing Jurisdiction of Sessions & Magistrates", "order": 2, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    {"id": "top-crpc-01-03", "chapterId": "ch-crpc-01", "subjectId": "law-crpc", "title": "Directorate of Prosecution & Public Prosecutors", "order": 3, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 20},
    # Ch 2
    {"id": "top-crpc-02-01", "chapterId": "ch-crpc-02", "subjectId": "law-crpc", "title": "Arrest Without Warrant & Notice of Appearance (Arnesh Kumar)", "order": 1, "mcqsCount": 12, "pyqsCount": 2, "estimatedMinutes": 22},
    {"id": "top-crpc-02-02", "chapterId": "ch-crpc-02", "subjectId": "law-crpc", "title": "Procedure of Arrest, Handcuff Rules & Search of Arrestee", "order": 2, "mcqsCount": 11, "pyqsCount": 2, "estimatedMinutes": 21},
    {"id": "top-crpc-02-03", "chapterId": "ch-crpc-02", "subjectId": "law-crpc", "title": "Rights of Arrested Persons & The 24-Hour Rule (D.K. Basu)", "order": 3, "mcqsCount": 12, "pyqsCount": 2, "estimatedMinutes": 22},
    # Ch 3
    {"id": "top-crpc-03-01", "chapterId": "ch-crpc-03", "subjectId": "law-crpc", "title": "Summons & Warrants of Arrest: Form, Service & Execution", "order": 1, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-crpc-03-02", "chapterId": "ch-crpc-03", "subjectId": "law-crpc", "title": "Proclamation & Attachment of Property for Absconders", "order": 2, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    {"id": "top-crpc-03-03", "chapterId": "ch-crpc-03", "subjectId": "law-crpc", "title": "Search Warrants, Summons to Produce & Impounding", "order": 3, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 20},
    # Ch 4
    {"id": "top-crpc-04-01", "chapterId": "ch-crpc-04", "subjectId": "law-crpc", "title": "Security for Keeping Peace & Good Behaviour Proceedings", "order": 1, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-crpc-04-02", "chapterId": "ch-crpc-04", "subjectId": "law-crpc", "title": "Maintenance of Public Order & Urgent Injunctions (S. 144 CrPC)", "order": 2, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    {"id": "top-crpc-04-03", "chapterId": "ch-crpc-04", "subjectId": "law-crpc", "title": "Disputes as to Immovable Property: Possession Inquiries", "order": 3, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 20},
    # Ch 5
    {"id": "top-crpc-05-01", "chapterId": "ch-crpc-05", "subjectId": "law-crpc", "title": "Maintenance of Wives, Children & Parents: S. 125 CrPC / S. 144 BNSS", "order": 1, "mcqsCount": 13, "pyqsCount": 3, "estimatedMinutes": 25},
    {"id": "top-crpc-05-02", "chapterId": "ch-crpc-05", "subjectId": "law-crpc", "title": "Procedure, Alteration & Enforcement of Maintenance Orders", "order": 2, "mcqsCount": 12, "pyqsCount": 2, "estimatedMinutes": 25},
    # Ch 6
    {"id": "top-crpc-06-01", "chapterId": "ch-crpc-06", "subjectId": "law-crpc", "title": "First Information Report: S. 173 BNSS / S. 154 CrPC & Zero FIR", "order": 1, "mcqsCount": 14, "pyqsCount": 2, "estimatedMinutes": 25},
    {"id": "top-crpc-06-02", "chapterId": "ch-crpc-06", "subjectId": "law-crpc", "title": "Police Investigation Powers & Examination of Witnesses (S. 161 CrPC)", "order": 2, "mcqsCount": 13, "pyqsCount": 2, "estimatedMinutes": 25},
    {"id": "top-crpc-06-03", "chapterId": "ch-crpc-06", "subjectId": "law-crpc", "title": "Recording Confessions & Statements by Magistrate (S. 164 CrPC)", "order": 3, "mcqsCount": 13, "pyqsCount": 2, "estimatedMinutes": 25},
    # Ch 7
    {"id": "top-crpc-07-01", "chapterId": "ch-crpc-07", "subjectId": "law-crpc", "title": "Remand & Police Custody: S. 187 BNSS vs S. 167 CrPC & Default Bail", "order": 1, "mcqsCount": 15, "pyqsCount": 2, "estimatedMinutes": 28},
    {"id": "top-crpc-07-02", "chapterId": "ch-crpc-07", "subjectId": "law-crpc", "title": "Inquest Inquiries & Final Police Report (Charge-Sheet S. 173 CrPC)", "order": 2, "mcqsCount": 15, "pyqsCount": 2, "estimatedMinutes": 27},
    # Ch 8
    {"id": "top-crpc-08-01", "chapterId": "ch-crpc-08", "subjectId": "law-crpc", "title": "Territorial Jurisdiction of Criminal Courts for Inquiries & Trials", "order": 1, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-crpc-08-02", "chapterId": "ch-crpc-08", "subjectId": "law-crpc", "title": "Cognizance of Offences by Magistrates & Statutory Sanctions", "order": 2, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    {"id": "top-crpc-08-03", "chapterId": "ch-crpc-08", "subjectId": "law-crpc", "title": "Complaints to Magistrates & Issue of Process (S. 200–204 CrPC)", "order": 3, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 20},
    # Ch 9
    {"id": "top-crpc-09-01", "chapterId": "ch-crpc-09", "subjectId": "law-crpc", "title": "Form, Contents & Alteration of Charge", "order": 1, "mcqsCount": 12, "pyqsCount": 1, "estimatedMinutes": 25},
    {"id": "top-crpc-09-02", "chapterId": "ch-crpc-09", "subjectId": "law-crpc", "title": "Joinder of Charges & Statutory Exceptions to Separate Trials", "order": 2, "mcqsCount": 13, "pyqsCount": 2, "estimatedMinutes": 25},
    # Ch 10
    {"id": "top-crpc-10-01", "chapterId": "ch-crpc-10", "subjectId": "law-crpc", "title": "Trial Before Court of Session: Discharge, Opening & Verdict", "order": 1, "mcqsCount": 12, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-crpc-10-02", "chapterId": "ch-crpc-10", "subjectId": "law-crpc", "title": "Trial of Warrant Cases by Magistrates (Police vs Complaint)", "order": 2, "mcqsCount": 11, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-crpc-10-03", "chapterId": "ch-crpc-10", "subjectId": "law-crpc", "title": "Summons Trials & Summary Trials: Distinction & Procedure", "order": 3, "mcqsCount": 11, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-crpc-10-04", "chapterId": "ch-crpc-10", "subjectId": "law-crpc", "title": "Plea Bargaining & Trial in Absentia of Proclaimed Offenders", "order": 4, "mcqsCount": 11, "pyqsCount": 1, "estimatedMinutes": 20},
    # Ch 11
    {"id": "top-crpc-11-01", "chapterId": "ch-crpc-11", "subjectId": "law-crpc", "title": "Autrefois Acquit & Autrefois Convict: Double Jeopardy in Procedure", "order": 1, "mcqsCount": 12, "pyqsCount": 1, "estimatedMinutes": 22},
    {"id": "top-crpc-11-02", "chapterId": "ch-crpc-11", "subjectId": "law-crpc", "title": "Examination of Accused (S. 313 CrPC) & Tender of Pardon", "order": 2, "mcqsCount": 11, "pyqsCount": 1, "estimatedMinutes": 21},
    {"id": "top-crpc-11-03", "chapterId": "ch-crpc-11", "subjectId": "law-crpc", "title": "Inherent Powers (S. 482 CrPC / S. 528 BNSS) & Summoning (S. 319)", "order": 3, "mcqsCount": 12, "pyqsCount": 2, "estimatedMinutes": 22},
    # Ch 12
    {"id": "top-crpc-12-01", "chapterId": "ch-crpc-12", "subjectId": "law-crpc", "title": "Bailable vs Non-Bailable Offences & General Bail Principles", "order": 1, "mcqsCount": 12, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-crpc-12-02", "chapterId": "ch-crpc-12", "subjectId": "law-crpc", "title": "Undertrial Bail Rights: S. 479 BNSS vs S. 436A CrPC", "order": 2, "mcqsCount": 11, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-crpc-12-03", "chapterId": "ch-crpc-12", "subjectId": "law-crpc", "title": "Anticipatory Bail & Special Powers of High Court / Sessions", "order": 3, "mcqsCount": 11, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-crpc-12-04", "chapterId": "ch-crpc-12", "subjectId": "law-crpc", "title": "Judgments, Appeals, Reference & Revision Jurisdiction", "order": 4, "mcqsCount": 11, "pyqsCount": 1, "estimatedMinutes": 20}
]

# ==============================================================================
# 3. LAW OF EVIDENCE (10 Chapters, 26 Topics)
# ==============================================================================
EVI_CHAPTERS = [
    {
        "id": "ch-evi-01",
        "subjectId": "law-evidence",
        "number": 1,
        "title": "Introduction, Cardinal Definitions & Standards of Proof",
        "scope": "Commencement (1 July 2024), Court, Fact, Fact in issue, Relevant fact, Document, Electronic record, Proved, Disproved, Not proved, and Presumptions",
        "topicsCount": 3,
        "mcqsCount": 30,
        "pyqsCount": 8,
        "estimatedMinutes": 60,
        "weightage": "Very High"
    },
    {
        "id": "ch-evi-02",
        "subjectId": "law-evidence",
        "number": 2,
        "title": "Relevancy of Facts: Res Gestae, Conduct, Conspiracy & Alibi",
        "scope": "Res Gestae (S. 4 BSA / S. 6 IEA), Occasion/cause/effect, Motive, preparation, conduct, TIP, Things said/done in conspiracy, and Plea of Alibi",
        "topicsCount": 4,
        "mcqsCount": 45,
        "pyqsCount": 11,
        "estimatedMinutes": 80,
        "weightage": "Very High"
    },
    {
        "id": "ch-evi-03",
        "subjectId": "law-evidence",
        "number": 3,
        "title": "Admissions & Confessions",
        "scope": "Definition of admission, Confession under inducement/threat, Confession to police officer (S. 23(1) BSA / S. 25 IEA), Discovery statements (S. 23(2) BSA / S. 27 IEA), and Co-accused confession",
        "topicsCount": 4,
        "mcqsCount": 45,
        "pyqsCount": 13,
        "estimatedMinutes": 80,
        "weightage": "Very High"
    },
    {
        "id": "ch-evi-04",
        "subjectId": "law-evidence",
        "number": 4,
        "title": "Statements by Persons Who Cannot Be Called: Dying Declarations",
        "scope": "Dying declarations (S. 26(a) BSA / S. 32(1) IEA), Statements against interest, Statements in ordinary course of business, and Evidence in prior judicial proceedings",
        "topicsCount": 2,
        "mcqsCount": 25,
        "pyqsCount": 8,
        "estimatedMinutes": 55,
        "weightage": "Very High"
    },
    {
        "id": "ch-evi-05",
        "subjectId": "law-evidence",
        "number": 5,
        "title": "Relevancy of Judgments, Expert Opinions & Character Evidence",
        "scope": "Judgments in rem vs in personam, Fraud in judgments, Expert opinions (Science, Art, Handwriting, Digital records), and Character evidence in civil vs criminal matters",
        "topicsCount": 3,
        "mcqsCount": 30,
        "pyqsCount": 7,
        "estimatedMinutes": 60,
        "weightage": "High"
    },
    {
        "id": "ch-evi-06",
        "subjectId": "law-evidence",
        "number": 6,
        "title": "Facts Which Need Not Be Proved & Oral Evidence",
        "scope": "Judicial notice (S. 52 BSA / S. 57 IEA), Facts admitted, Oral evidence must be direct (S. 55 BSA / S. 60 IEA), and Exclusion of hearsay rule",
        "topicsCount": 2,
        "mcqsCount": 20,
        "pyqsCount": 5,
        "estimatedMinutes": 45,
        "weightage": "Medium"
    },
    {
        "id": "ch-evi-07",
        "subjectId": "law-evidence",
        "number": 7,
        "title": "Documentary Evidence & Electronic Records Admissibility",
        "scope": "Primary vs Secondary evidence, When secondary is admissible, Electronic records certification (S. 63 BSA vs S. 65B IEA), Public documents, and 30-year presumption",
        "topicsCount": 3,
        "mcqsCount": 35,
        "pyqsCount": 7,
        "estimatedMinutes": 70,
        "weightage": "Very High"
    },
    {
        "id": "ch-evi-08",
        "subjectId": "law-evidence",
        "number": 8,
        "title": "Exclusion of Oral by Documentary Evidence: The Best Evidence Rule",
        "scope": "Exclusion of oral evidence of terms of contracts/grants (S. 94 BSA / S. 91 IEA), Exclusion of evidence of oral agreement (S. 95 BSA / S. 92 IEA & 6 Provisos), and Ambiguities",
        "topicsCount": 2,
        "mcqsCount": 20,
        "pyqsCount": 4,
        "estimatedMinutes": 50,
        "weightage": "High"
    },
    {
        "id": "ch-evi-09",
        "subjectId": "law-evidence",
        "number": 9,
        "title": "Burden of Proof & Statutory Presumptions",
        "scope": "Burden of proof vs Onus of proof, Facts especially within knowledge (S. 109 BSA / S. 106 IEA), Presumption of death, Legitimacy (S. 116 BSA / S. 112 IEA), Dowry death presumption",
        "topicsCount": 3,
        "mcqsCount": 35,
        "pyqsCount": 6,
        "estimatedMinutes": 65,
        "weightage": "Very High"
    },
    {
        "id": "ch-evi-10",
        "subjectId": "law-evidence",
        "number": 10,
        "title": "Estoppel, Competency of Witnesses & Witness Examination",
        "scope": "Doctrine of Estoppel (S. 121 BSA / S. 115 IEA), Competency of witnesses, Privileged communications, Examination stages, Leading questions, and Hostile witnesses",
        "topicsCount": 4,
        "mcqsCount": 40,
        "pyqsCount": 4,
        "estimatedMinutes": 75,
        "weightage": "Very High"
    }
]

EVI_TOPICS = [
    # Ch 1
    {"id": "top-evi-01-01", "chapterId": "ch-evi-01", "subjectId": "law-evidence", "title": "Scope, Commencement (1 July 2024), Court, Fact & Fact in Issue", "order": 1, "mcqsCount": 10, "pyqsCount": 3, "estimatedMinutes": 20},
    {"id": "top-evi-01-02", "chapterId": "ch-evi-01", "subjectId": "law-evidence", "title": "Relevant Fact, Document & Electronic Record Definitions", "order": 2, "mcqsCount": 10, "pyqsCount": 3, "estimatedMinutes": 20},
    {"id": "top-evi-01-03", "chapterId": "ch-evi-01", "subjectId": "law-evidence", "title": "Proved, Disproved, Not Proved & Presumption Standards", "order": 3, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    # Ch 2
    {"id": "top-evi-02-01", "chapterId": "ch-evi-02", "subjectId": "law-evidence", "title": "Doctrine of Res Gestae: Facts Forming Part of Same Transaction", "order": 1, "mcqsCount": 12, "pyqsCount": 4, "estimatedMinutes": 20},
    {"id": "top-evi-02-02", "chapterId": "ch-evi-02", "subjectId": "law-evidence", "title": "Occasion, Cause, Effect, Opportunity & Motive/Conduct", "order": 2, "mcqsCount": 11, "pyqsCount": 3, "estimatedMinutes": 20},
    {"id": "top-evi-02-03", "chapterId": "ch-evi-02", "subjectId": "law-evidence", "title": "Test Identification Parade (TIP) & Explanatory Facts", "order": 3, "mcqsCount": 11, "pyqsCount": 2, "estimatedMinutes": 20},
    {"id": "top-evi-02-04", "chapterId": "ch-evi-02", "subjectId": "law-evidence", "title": "Conspiracy Proof (S. 8 BSA / S. 10 IEA) & Plea of Alibi", "order": 4, "mcqsCount": 11, "pyqsCount": 2, "estimatedMinutes": 20},
    # Ch 3
    {"id": "top-evi-03-01", "chapterId": "ch-evi-03", "subjectId": "law-evidence", "title": "Admissions Defined & Persons Qualified to Make Admissions", "order": 1, "mcqsCount": 11, "pyqsCount": 3, "estimatedMinutes": 20},
    {"id": "top-evi-03-02", "chapterId": "ch-evi-03", "subjectId": "law-evidence", "title": "Confessions Under Inducement, Threat or Promise (S. 22 BSA / S. 24 IEA)", "order": 2, "mcqsCount": 11, "pyqsCount": 3, "estimatedMinutes": 20},
    {"id": "top-evi-03-03", "chapterId": "ch-evi-03", "subjectId": "law-evidence", "title": "Confession to Police Officers & In Police Custody", "order": 3, "mcqsCount": 11, "pyqsCount": 3, "estimatedMinutes": 20},
    {"id": "top-evi-03-04", "chapterId": "ch-evi-03", "subjectId": "law-evidence", "title": "Discovery Statements: S. 23(2) BSA / S. 27 IEA (Pulukuri Kottaya)", "order": 4, "mcqsCount": 12, "pyqsCount": 4, "estimatedMinutes": 20},
    # Ch 4
    {"id": "top-evi-04-01", "chapterId": "ch-evi-04", "subjectId": "law-evidence", "title": "Dying Declarations: S. 26(a) BSA / S. 32(1) IEA (Pakala Narayana Swami)", "order": 1, "mcqsCount": 13, "pyqsCount": 5, "estimatedMinutes": 28},
    {"id": "top-evi-04-02", "chapterId": "ch-evi-04", "subjectId": "law-evidence", "title": "Statements Against Interest, Course of Business & Prior Evidence", "order": 2, "mcqsCount": 12, "pyqsCount": 3, "estimatedMinutes": 27},
    # Ch 5
    {"id": "top-evi-05-01", "chapterId": "ch-evi-05", "subjectId": "law-evidence", "title": "Relevancy of Judgments: Res Judicata, In Rem & In Personam", "order": 1, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    {"id": "top-evi-05-02", "chapterId": "ch-evi-05", "subjectId": "law-evidence", "title": "Expert Opinions: Science, Art, Fingerprints & Digital Evidence", "order": 2, "mcqsCount": 10, "pyqsCount": 3, "estimatedMinutes": 20},
    {"id": "top-evi-05-03", "chapterId": "ch-evi-05", "subjectId": "law-evidence", "title": "Character Evidence in Civil & Criminal Proceedings", "order": 3, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    # Ch 6
    {"id": "top-evi-06-01", "chapterId": "ch-evi-06", "subjectId": "law-evidence", "title": "Facts Judicially Noticeable & Facts Admitted", "order": 1, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 22},
    {"id": "top-evi-06-02", "chapterId": "ch-evi-06", "subjectId": "law-evidence", "title": "Oral Evidence Must Be Direct & Exceptions to Hearsay", "order": 2, "mcqsCount": 10, "pyqsCount": 3, "estimatedMinutes": 23},
    # Ch 7
    {"id": "top-evi-07-01", "chapterId": "ch-evi-07", "subjectId": "law-evidence", "title": "Primary vs Secondary Evidence & Admissibility Criteria", "order": 1, "mcqsCount": 12, "pyqsCount": 3, "estimatedMinutes": 24},
    {"id": "top-evi-07-02", "chapterId": "ch-evi-07", "subjectId": "law-evidence", "title": "Electronic Records Admissibility: BSA S. 63 vs IEA S. 65B Certificate", "order": 2, "mcqsCount": 12, "pyqsCount": 2, "estimatedMinutes": 24},
    {"id": "top-evi-07-03", "chapterId": "ch-evi-07", "subjectId": "law-evidence", "title": "Public Documents, Certified Copies & Presumptions as to Documents", "order": 3, "mcqsCount": 11, "pyqsCount": 2, "estimatedMinutes": 22},
    # Ch 8
    {"id": "top-evi-08-01", "chapterId": "ch-evi-08", "subjectId": "law-evidence", "title": "Exclusion of Oral by Documentary Evidence (Best Evidence Rule S. 91)", "order": 1, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 25},
    {"id": "top-evi-08-02", "chapterId": "ch-evi-08", "subjectId": "law-evidence", "title": "Exclusion of Evidence of Oral Agreement & The Six Provisos (S. 92)", "order": 2, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 25},
    # Ch 9
    {"id": "top-evi-09-01", "chapterId": "ch-evi-09", "subjectId": "law-evidence", "title": "Burden of Proof vs Evidential Onus & Special Knowledge (S. 106 IEA)", "order": 1, "mcqsCount": 12, "pyqsCount": 2, "estimatedMinutes": 22},
    {"id": "top-evi-09-02", "chapterId": "ch-evi-09", "subjectId": "law-evidence", "title": "Presumption of Death, Legitimacy (S. 112 IEA) & Dowry Death", "order": 2, "mcqsCount": 12, "pyqsCount": 2, "estimatedMinutes": 22},
    {"id": "top-evi-09-03", "chapterId": "ch-evi-09", "subjectId": "law-evidence", "title": "Court Presumptions: S. 114 IEA / S. 117 BSA & Absence of Consent", "order": 3, "mcqsCount": 11, "pyqsCount": 2, "estimatedMinutes": 21},
    # Ch 10
    {"id": "top-evi-10-01", "chapterId": "ch-evi-10", "subjectId": "law-evidence", "title": "Doctrine of Estoppel: Rules, Promissory & Tenant Estoppel", "order": 1, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-evi-10-02", "chapterId": "ch-evi-10", "subjectId": "law-evidence", "title": "Competency of Witnesses, Child/Dumb Witnesses & Privileged Comms", "order": 2, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-evi-10-03", "chapterId": "ch-evi-10", "subjectId": "law-evidence", "title": "Order of Examination: Chief, Cross, Re-Exam & Leading Questions", "order": 3, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-evi-10-04", "chapterId": "ch-evi-10", "subjectId": "law-evidence", "title": "Impeaching Credit, Hostile Witnesses & Refreshing Memory", "order": 4, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 15}
]

def write_module(filepath, var_name, data):
    content = f"""/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Judicial Learning Academy Data Module
 */
(function(global) {{
  'use strict';

  const DATA = {json.dumps(data, indent=2)};

  global.{var_name} = DATA;
  if (typeof module !== 'undefined' && module.exports) {{
    module.exports = DATA;
  }}
}})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {filepath} ({len(data)} items)")

# Write files
write_module("assets/learning/data/criminal/criminal-chapters.js", "CRIMINAL_CHAPTERS", CRIM_CHAPTERS)
write_module("assets/learning/data/criminal/criminal-topics.js", "CRIMINAL_TOPICS", CRIM_TOPICS)

write_module("assets/learning/data/crpc/crpc-chapters.js", "CRPC_CHAPTERS", CRPC_CHAPTERS)
write_module("assets/learning/data/crpc/crpc-topics.js", "CRPC_TOPICS", CRPC_TOPICS)

write_module("assets/learning/data/evidence/evidence-chapters.js", "EVIDENCE_CHAPTERS", EVI_CHAPTERS)
write_module("assets/learning/data/evidence/evidence-topics.js", "EVIDENCE_TOPICS", EVI_TOPICS)

print("All 6 metadata files successfully built.")
