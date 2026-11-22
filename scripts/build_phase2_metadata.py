import json
import os

# -------------------------------------------------------------
# 1. JURISPRUDENCE CHAPTERS & TOPICS
# -------------------------------------------------------------
JUR_CHAPTERS = [
    {
        "id": "ch-jur-01",
        "subjectId": "law-jurisprudence",
        "number": 1,
        "title": "Nature, Scope & Classification of Jurisprudence",
        "scope": "Meaning, definitions, grammar of law, law and morality, classifications of law",
        "topicsCount": 3,
        "mcqsCount": 24,
        "pyqsCount": 6,
        "estimatedMinutes": 55,
        "weightage": "High"
    },
    {
        "id": "ch-jur-02",
        "subjectId": "law-jurisprudence",
        "number": 2,
        "title": "Sources of Law: Custom, Precedent & Legislation",
        "scope": "Custom essentials, stare decisis, ratio decidendi, obiter dicta, statutory codification",
        "topicsCount": 3,
        "mcqsCount": 24,
        "pyqsCount": 5,
        "estimatedMinutes": 60,
        "weightage": "High"
    },
    {
        "id": "ch-jur-03",
        "subjectId": "law-jurisprudence",
        "number": 3,
        "title": "Natural Law School & Philosophical Foundations",
        "scope": "Classical Greek/Roman, Medieval Aquinas, Social Contract, 20th century revival (Fuller, Finnis)",
        "topicsCount": 3,
        "mcqsCount": 24,
        "pyqsCount": 4,
        "estimatedMinutes": 65,
        "weightage": "Very High"
    },
    {
        "id": "ch-jur-04",
        "subjectId": "law-jurisprudence",
        "number": 4,
        "title": "Analytical & Positivist School: Austin, Hart & Kelsen",
        "scope": "Bentham's Utilitarianism, Austin's Command Theory, Hart's Rules, Kelsen's Pure Theory & Grundnorm",
        "topicsCount": 4,
        "mcqsCount": 30,
        "pyqsCount": 8,
        "estimatedMinutes": 75,
        "weightage": "Very High"
    },
    {
        "id": "ch-jur-05",
        "subjectId": "law-jurisprudence",
        "number": 5,
        "title": "Historical School of Jurisprudence: Savigny & Maine",
        "scope": "Savigny's Volksgeist, opposition to codification, Maine's Status to Contract, Ancient Law",
        "topicsCount": 2,
        "mcqsCount": 18,
        "pyqsCount": 4,
        "estimatedMinutes": 45,
        "weightage": "High"
    },
    {
        "id": "ch-jur-06",
        "subjectId": "law-jurisprudence",
        "number": 6,
        "title": "Sociological School: Ihering, Ehrlich, Duguit & Pound",
        "scope": "Ihering's purpose, Ehrlich's living law, Duguit's social solidarity, Pound's social engineering & jural postulates",
        "topicsCount": 2,
        "mcqsCount": 18,
        "pyqsCount": 4,
        "estimatedMinutes": 50,
        "weightage": "Very High"
    },
    {
        "id": "ch-jur-07",
        "subjectId": "law-jurisprudence",
        "number": 7,
        "title": "Realist School & Modern Critical Jurisprudence",
        "scope": "American Realism (Holmes, Frank, Llewellyn), Scandinavian Realism (Olivecrona, Ross), Comparative schools",
        "topicsCount": 2,
        "mcqsCount": 16,
        "pyqsCount": 3,
        "estimatedMinutes": 45,
        "weightage": "Medium"
    },
    {
        "id": "ch-jur-08",
        "subjectId": "law-jurisprudence",
        "number": 8,
        "title": "Legal Rights and Duties: Salmond & Hohfeldian Analysis",
        "scope": "Essentials of legal rights, correlation with duties, Hohfeld's tables of jural correlatives & opposites, classification of rights",
        "topicsCount": 3,
        "mcqsCount": 24,
        "pyqsCount": 4,
        "estimatedMinutes": 60,
        "weightage": "Very High"
    },
    {
        "id": "ch-jur-09",
        "subjectId": "law-jurisprudence",
        "number": 9,
        "title": "Legal Personality: Natural & Juristic Persons",
        "scope": "Status of unborn, dead, animals, idols; Corporate personality theories (Fiction, Realist, Bracket, Purpose), veil lifting",
        "topicsCount": 2,
        "mcqsCount": 18,
        "pyqsCount": 3,
        "estimatedMinutes": 45,
        "weightage": "High"
    },
    {
        "id": "ch-jur-10",
        "subjectId": "law-jurisprudence",
        "number": 10,
        "title": "Concepts of Ownership and Possession",
        "scope": "Corpus & animus, Savigny vs Salmond, possession in fact and law, ownership bundle of rights, possessory remedies",
        "topicsCount": 3,
        "mcqsCount": 24,
        "pyqsCount": 3,
        "estimatedMinutes": 60,
        "weightage": "High"
    },
    {
        "id": "ch-jur-11",
        "subjectId": "law-jurisprudence",
        "number": 11,
        "title": "Liability, Obligations & Administration of Justice",
        "scope": "Civil and criminal liability, remedial and penal, strict & absolute liability, theories of punishment",
        "topicsCount": 3,
        "mcqsCount": 20,
        "pyqsCount": 1,
        "estimatedMinutes": 50,
        "weightage": "Medium"
    }
]

JUR_TOPICS = [
    # Ch 1
    {"id": "top-jur-01-01", "chapterId": "ch-jur-01", "subjectId": "law-jurisprudence", "title": "Meaning, Nature and Scope of Jurisprudence", "order": 1, "mcqsCount": 8, "pyqsCount": 2, "estimatedMinutes": 18},
    {"id": "top-jur-01-02", "chapterId": "ch-jur-01", "subjectId": "law-jurisprudence", "title": "Law, Morality and Justice (Hart-Fuller & Hart-Devlin Debates)", "order": 2, "mcqsCount": 8, "pyqsCount": 2, "estimatedMinutes": 20},
    {"id": "top-jur-01-03", "chapterId": "ch-jur-01", "subjectId": "law-jurisprudence", "title": "Classifications of Law & General vs Particular Jurisprudence", "order": 3, "mcqsCount": 8, "pyqsCount": 2, "estimatedMinutes": 17},
    # Ch 2
    {"id": "top-jur-02-01", "chapterId": "ch-jur-02", "subjectId": "law-jurisprudence", "title": "Custom as a Source of Law: Essentials & Theories", "order": 1, "mcqsCount": 8, "pyqsCount": 2, "estimatedMinutes": 20},
    {"id": "top-jur-02-02", "chapterId": "ch-jur-02", "subjectId": "law-jurisprudence", "title": "Judicial Precedent, Stare Decisis & Ratio Decidendi", "order": 2, "mcqsCount": 8, "pyqsCount": 2, "estimatedMinutes": 22},
    {"id": "top-jur-02-03", "chapterId": "ch-jur-02", "subjectId": "law-jurisprudence", "title": "Legislation, Codification & Principles of Interpretation", "order": 3, "mcqsCount": 8, "pyqsCount": 1, "estimatedMinutes": 18},
    # Ch 3
    {"id": "top-jur-03-01", "chapterId": "ch-jur-03", "subjectId": "law-jurisprudence", "title": "Classical & Medieval Natural Law (Aquinas & Stoics)", "order": 1, "mcqsCount": 8, "pyqsCount": 1, "estimatedMinutes": 22},
    {"id": "top-jur-03-02", "chapterId": "ch-jur-03", "subjectId": "law-jurisprudence", "title": "Social Contract Theory (Hobbes, Locke & Rousseau)", "order": 2, "mcqsCount": 8, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-jur-03-03", "chapterId": "ch-jur-03", "subjectId": "law-jurisprudence", "title": "Revival of Natural Law in the 20th Century (Fuller, Stammler & Finnis)", "order": 3, "mcqsCount": 8, "pyqsCount": 2, "estimatedMinutes": 23},
    # Ch 4
    {"id": "top-jur-04-01", "chapterId": "ch-jur-04", "subjectId": "law-jurisprudence", "title": "Jeremy Bentham: Utilitarianism & Censorial Jurisprudence", "order": 1, "mcqsCount": 7, "pyqsCount": 2, "estimatedMinutes": 18},
    {"id": "top-jur-04-02", "chapterId": "ch-jur-04", "subjectId": "law-jurisprudence", "title": "John Austin & the Command Theory of Sovereign Law", "order": 2, "mcqsCount": 8, "pyqsCount": 2, "estimatedMinutes": 20},
    {"id": "top-jur-04-03", "chapterId": "ch-jur-04", "subjectId": "law-jurisprudence", "title": "H.L.A. Hart: Concept of Law, Primary & Secondary Rules", "order": 3, "mcqsCount": 8, "pyqsCount": 2, "estimatedMinutes": 20},
    {"id": "top-jur-04-04", "chapterId": "ch-jur-04", "subjectId": "law-jurisprudence", "title": "Hans Kelsen: Pure Theory of Law & the Grundnorm Hierarchy", "order": 4, "mcqsCount": 7, "pyqsCount": 2, "estimatedMinutes": 17},
    # Ch 5
    {"id": "top-jur-05-01", "chapterId": "ch-jur-05", "subjectId": "law-jurisprudence", "title": "Friedrich Carl von Savigny & the Doctrine of Volksgeist", "order": 1, "mcqsCount": 9, "pyqsCount": 2, "estimatedMinutes": 22},
    {"id": "top-jur-05-02", "chapterId": "ch-jur-05", "subjectId": "law-jurisprudence", "title": "Sir Henry Maine: Status to Contract & Anthropological Law", "order": 2, "mcqsCount": 9, "pyqsCount": 2, "estimatedMinutes": 23},
    # Ch 6
    {"id": "top-jur-06-01", "chapterId": "ch-jur-06", "subjectId": "law-jurisprudence", "title": "Foundations: Ihering, Ehrlich's Living Law & Duguit's Solidarity", "order": 1, "mcqsCount": 9, "pyqsCount": 2, "estimatedMinutes": 25},
    {"id": "top-jur-06-02", "chapterId": "ch-jur-06", "subjectId": "law-jurisprudence", "title": "Roscoe Pound: Theory of Social Engineering & Jural Postulates", "order": 2, "mcqsCount": 9, "pyqsCount": 2, "estimatedMinutes": 25},
    # Ch 7
    {"id": "top-jur-07-01", "chapterId": "ch-jur-07", "subjectId": "law-jurisprudence", "title": "American Realism: Oliver Wendell Holmes Jr. & Jerome Frank", "order": 1, "mcqsCount": 8, "pyqsCount": 2, "estimatedMinutes": 22},
    {"id": "top-jur-07-02", "chapterId": "ch-jur-07", "subjectId": "law-jurisprudence", "title": "Scandinavian Realism & Comparative Jurisprudential Synthesis", "order": 2, "mcqsCount": 8, "pyqsCount": 1, "estimatedMinutes": 23},
    # Ch 8
    {"id": "top-jur-08-01", "chapterId": "ch-jur-08", "subjectId": "law-jurisprudence", "title": "Concept of Legal Rights and Duties: Salmond's Formula", "order": 1, "mcqsCount": 8, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-jur-08-02", "chapterId": "ch-jur-08", "subjectId": "law-jurisprudence", "title": "Hohfeld's Analysis: Jural Correlatives & Jural Opposites", "order": 2, "mcqsCount": 8, "pyqsCount": 2, "estimatedMinutes": 22},
    {"id": "top-jur-08-03", "chapterId": "ch-jur-08", "subjectId": "law-jurisprudence", "title": "Classification of Legal Rights (In Rem, In Personam, Proprietary)", "order": 3, "mcqsCount": 8, "pyqsCount": 1, "estimatedMinutes": 18},
    # Ch 9
    {"id": "top-jur-09-01", "chapterId": "ch-jur-09", "subjectId": "law-jurisprudence", "title": "Legal Personality: Natural Persons, Unborn, Dead & Animals", "order": 1, "mcqsCount": 9, "pyqsCount": 2, "estimatedMinutes": 22},
    {"id": "top-jur-09-02", "chapterId": "ch-jur-09", "subjectId": "law-jurisprudence", "title": "Corporate Personality, Theories & Piercing the Corporate Veil", "order": 2, "mcqsCount": 9, "pyqsCount": 1, "estimatedMinutes": 23},
    # Ch 10
    {"id": "top-jur-10-01", "chapterId": "ch-jur-10", "subjectId": "law-jurisprudence", "title": "Concept & Essentials of Possession: Corpus & Animus", "order": 1, "mcqsCount": 8, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-jur-10-02", "chapterId": "ch-jur-10", "subjectId": "law-jurisprudence", "title": "Concept & Characteristics of Ownership (Salmond & Austin)", "order": 2, "mcqsCount": 8, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-jur-10-03", "chapterId": "ch-jur-10", "subjectId": "law-jurisprudence", "title": "Relationship Between Ownership and Possession & Remedies", "order": 3, "mcqsCount": 8, "pyqsCount": 1, "estimatedMinutes": 20},
    # Ch 11
    {"id": "top-jur-11-01", "chapterId": "ch-jur-11", "subjectId": "law-jurisprudence", "title": "Nature of Legal Liability: Acts, Omissions, Mens Rea & Negligence", "order": 1, "mcqsCount": 7, "pyqsCount": 1, "estimatedMinutes": 17},
    {"id": "top-jur-11-02", "chapterId": "ch-jur-11", "subjectId": "law-jurisprudence", "title": "Strict, Absolute & Vicarious Liability in Jurisprudence", "order": 2, "mcqsCount": 7, "pyqsCount": 0, "estimatedMinutes": 16},
    {"id": "top-jur-11-03", "chapterId": "ch-jur-11", "subjectId": "law-jurisprudence", "title": "Administration of Justice & Modern Theories of Punishment", "order": 3, "mcqsCount": 6, "pyqsCount": 0, "estimatedMinutes": 17}
]


# -------------------------------------------------------------
# 2. LAW OF CONTRACT CHAPTERS & TOPICS
# -------------------------------------------------------------
CNT_CHAPTERS = [
    {
        "id": "ch-cnt-01",
        "subjectId": "law-contract",
        "number": 1,
        "title": "Formation of Contract: Agreement, Offer & Acceptance",
        "sectionsRange": "Sections 1–9",
        "topicsCount": 4,
        "mcqsCount": 26,
        "pyqsCount": 12,
        "estimatedMinutes": 65,
        "weightage": "Very High"
    },
    {
        "id": "ch-cnt-02",
        "subjectId": "law-contract",
        "number": 2,
        "title": "Consideration & Doctrine of Privity",
        "sectionsRange": "Sections 2(d), 25",
        "topicsCount": 3,
        "mcqsCount": 24,
        "pyqsCount": 10,
        "estimatedMinutes": 60,
        "weightage": "Very High"
    },
    {
        "id": "ch-cnt-03",
        "subjectId": "law-contract",
        "number": 3,
        "title": "Capacity to Contract & Minor's Agreements",
        "sectionsRange": "Sections 10–12, 68",
        "topicsCount": 3,
        "mcqsCount": 24,
        "pyqsCount": 9,
        "estimatedMinutes": 55,
        "weightage": "Very High"
    },
    {
        "id": "ch-cnt-04",
        "subjectId": "law-contract",
        "number": 4,
        "title": "Free Consent I: Coercion, Undue Influence & Fraud",
        "sectionsRange": "Sections 13–17, 19",
        "topicsCount": 4,
        "mcqsCount": 26,
        "pyqsCount": 11,
        "estimatedMinutes": 65,
        "weightage": "Very High"
    },
    {
        "id": "ch-cnt-05",
        "subjectId": "law-contract",
        "number": 5,
        "title": "Free Consent II: Misrepresentation & Mistake",
        "sectionsRange": "Sections 18–22",
        "topicsCount": 3,
        "mcqsCount": 22,
        "pyqsCount": 7,
        "estimatedMinutes": 50,
        "weightage": "High"
    },
    {
        "id": "ch-cnt-06",
        "subjectId": "law-contract",
        "number": 6,
        "title": "Legality of Object & Void Agreements",
        "sectionsRange": "Sections 23–30",
        "topicsCount": 2,
        "mcqsCount": 22,
        "pyqsCount": 8,
        "estimatedMinutes": 50,
        "weightage": "Very High"
    },
    {
        "id": "ch-cnt-07",
        "subjectId": "law-contract",
        "number": 7,
        "title": "Contingent Contracts & Quasi-Contracts",
        "sectionsRange": "Sections 31–36, 68–72",
        "topicsCount": 2,
        "mcqsCount": 22,
        "pyqsCount": 6,
        "estimatedMinutes": 50,
        "weightage": "High"
    },
    {
        "id": "ch-cnt-08",
        "subjectId": "law-contract",
        "number": 8,
        "title": "Performance of Contract & Frustration",
        "sectionsRange": "Sections 37–67",
        "topicsCount": 3,
        "mcqsCount": 25,
        "pyqsCount": 8,
        "estimatedMinutes": 60,
        "weightage": "Very High"
    },
    {
        "id": "ch-cnt-09",
        "subjectId": "law-contract",
        "number": 9,
        "title": "Breach of Contract & Remedies for Damages",
        "sectionsRange": "Sections 73–75",
        "topicsCount": 3,
        "mcqsCount": 25,
        "pyqsCount": 5,
        "estimatedMinutes": 55,
        "weightage": "Very High"
    },
    {
        "id": "ch-cnt-10",
        "subjectId": "law-contract",
        "number": 10,
        "title": "Special Contracts I: Indemnity, Guarantee, Bailment & Pledge",
        "sectionsRange": "Sections 124–181",
        "topicsCount": 3,
        "mcqsCount": 24,
        "pyqsCount": 4,
        "estimatedMinutes": 60,
        "weightage": "High"
    },
    {
        "id": "ch-cnt-11",
        "subjectId": "law-contract",
        "number": 11,
        "title": "Special Contracts II: Contract of Agency",
        "sectionsRange": "Sections 182–238",
        "topicsCount": 2,
        "mcqsCount": 20,
        "pyqsCount": 2,
        "estimatedMinutes": 45,
        "weightage": "Medium"
    }
]

CNT_TOPICS = [
    # Ch 1
    {"id": "top-cnt-01-01", "chapterId": "ch-cnt-01", "subjectId": "law-contract", "title": "Agreement and Contract (Section 2(h) & Section 10 Essentials)", "order": 1, "mcqsCount": 7, "pyqsCount": 3, "estimatedMinutes": 17},
    {"id": "top-cnt-01-02", "chapterId": "ch-cnt-01", "subjectId": "law-contract", "title": "Offer / Proposal: Essentials & Offer vs Invitation to Treat", "order": 2, "mcqsCount": 7, "pyqsCount": 4, "estimatedMinutes": 17},
    {"id": "top-cnt-01-03", "chapterId": "ch-cnt-01", "subjectId": "law-contract", "title": "Acceptance, Postal Rule & Revocation (Sections 3–9)", "order": 3, "mcqsCount": 6, "pyqsCount": 3, "estimatedMinutes": 16},
    {"id": "top-cnt-01-04", "chapterId": "ch-cnt-01", "subjectId": "law-contract", "title": "Intention to Create Legal Relations (Balfour v Balfour Rule)", "order": 4, "mcqsCount": 6, "pyqsCount": 2, "estimatedMinutes": 15},
    # Ch 2
    {"id": "top-cnt-02-01", "chapterId": "ch-cnt-02", "subjectId": "law-contract", "title": "Consideration Essentials, Types & Quid Pro Quo (Section 2(d))", "order": 1, "mcqsCount": 8, "pyqsCount": 4, "estimatedMinutes": 20},
    {"id": "top-cnt-02-02", "chapterId": "ch-cnt-02", "subjectId": "law-contract", "title": "Privity of Contract vs Privity of Consideration & Exceptions", "order": 2, "mcqsCount": 8, "pyqsCount": 3, "estimatedMinutes": 20},
    {"id": "top-cnt-02-03", "chapterId": "ch-cnt-02", "subjectId": "law-contract", "title": "Agreements Without Consideration & Section 25 Exceptions", "order": 3, "mcqsCount": 8, "pyqsCount": 3, "estimatedMinutes": 20},
    # Ch 3
    {"id": "top-cnt-03-01", "chapterId": "ch-cnt-03", "subjectId": "law-contract", "title": "Competency to Contract & Minor's Agreements (Mohori Bibee)", "order": 1, "mcqsCount": 8, "pyqsCount": 4, "estimatedMinutes": 20},
    {"id": "top-cnt-03-02", "chapterId": "ch-cnt-03", "subjectId": "law-contract", "title": "Persons of Unsound Mind & Disqualified Persons (Section 12)", "order": 2, "mcqsCount": 8, "pyqsCount": 2, "estimatedMinutes": 18},
    {"id": "top-cnt-03-03", "chapterId": "ch-cnt-03", "subjectId": "law-contract", "title": "Necessaries Supplied to Incompetent Persons (Section 68)", "order": 3, "mcqsCount": 8, "pyqsCount": 3, "estimatedMinutes": 17},
    # Ch 4
    {"id": "top-cnt-04-01", "chapterId": "ch-cnt-04", "subjectId": "law-contract", "title": "Concept of Free Consent & Consensus ad Idem (Sections 13, 14)", "order": 1, "mcqsCount": 6, "pyqsCount": 2, "estimatedMinutes": 15},
    {"id": "top-cnt-04-02", "chapterId": "ch-cnt-04", "subjectId": "law-contract", "title": "Coercion: Statutory Definition & Legal Impact (Section 15)", "order": 2, "mcqsCount": 7, "pyqsCount": 3, "estimatedMinutes": 17},
    {"id": "top-cnt-04-03", "chapterId": "ch-cnt-04", "subjectId": "law-contract", "title": "Undue Influence, Fiduciary Position & Unconscionability (Section 16)", "order": 3, "mcqsCount": 7, "pyqsCount": 4, "estimatedMinutes": 18},
    {"id": "top-cnt-04-04", "chapterId": "ch-cnt-04", "subjectId": "law-contract", "title": "Fraud: Active Concealment & When Silence is Fraud (Section 17)", "order": 4, "mcqsCount": 6, "pyqsCount": 2, "estimatedMinutes": 15},
    # Ch 5
    {"id": "top-cnt-05-01", "chapterId": "ch-cnt-05", "subjectId": "law-contract", "title": "Misrepresentation: Types, Remedies & Exceptions (Sections 18, 19)", "order": 1, "mcqsCount": 8, "pyqsCount": 3, "estimatedMinutes": 18},
    {"id": "top-cnt-05-02", "chapterId": "ch-cnt-05", "subjectId": "law-contract", "title": "Mistake of Fact: Bilateral vs Unilateral Mistake (Sections 20, 22)", "order": 2, "mcqsCount": 7, "pyqsCount": 2, "estimatedMinutes": 16},
    {"id": "top-cnt-05-03", "chapterId": "ch-cnt-05", "subjectId": "law-contract", "title": "Mistake of Law: Indian Law vs Foreign Law (Section 21)", "order": 3, "mcqsCount": 7, "pyqsCount": 2, "estimatedMinutes": 16},
    # Ch 6
    {"id": "top-cnt-06-01", "chapterId": "ch-cnt-06", "subjectId": "law-contract", "title": "Unlawful Consideration & Public Policy Doctrine (Section 23)", "order": 1, "mcqsCount": 11, "pyqsCount": 4, "estimatedMinutes": 25},
    {"id": "top-cnt-06-02", "chapterId": "ch-cnt-06", "subjectId": "law-contract", "title": "Specific Void Agreements: Restraint of Trade, Marriage & Wagering (Sections 26–30)", "order": 2, "mcqsCount": 11, "pyqsCount": 4, "estimatedMinutes": 25},
    # Ch 7
    {"id": "top-cnt-07-01", "chapterId": "ch-cnt-07", "subjectId": "law-contract", "title": "Contingent Contracts: Meaning, Rules & Enforcement (Sections 31–36)", "order": 1, "mcqsCount": 11, "pyqsCount": 3, "estimatedMinutes": 25},
    {"id": "top-cnt-07-02", "chapterId": "ch-cnt-07", "subjectId": "law-contract", "title": "Quasi-Contracts & Doctrine of Unjust Enrichment (Sections 68–72)", "order": 2, "mcqsCount": 11, "pyqsCount": 3, "estimatedMinutes": 25},
    # Ch 8
    {"id": "top-cnt-08-01", "chapterId": "ch-cnt-08", "subjectId": "law-contract", "title": "Performance of Contracts & Reciprocal Promises (Sections 37–55)", "order": 1, "mcqsCount": 9, "pyqsCount": 3, "estimatedMinutes": 20},
    {"id": "top-cnt-08-02", "chapterId": "ch-cnt-08", "subjectId": "law-contract", "title": "Doctrine of Frustration & Supervening Impossibility (Section 56)", "order": 2, "mcqsCount": 8, "pyqsCount": 3, "estimatedMinutes": 20},
    {"id": "top-cnt-08-03", "chapterId": "ch-cnt-08", "subjectId": "law-contract", "title": "Discharge by Novation, Rescission & Alteration (Sections 62–67)", "order": 3, "mcqsCount": 8, "pyqsCount": 2, "estimatedMinutes": 20},
    # Ch 9
    {"id": "top-cnt-09-01", "chapterId": "ch-cnt-09", "subjectId": "law-contract", "title": "Anticipatory Breach vs Actual Breach of Contract (Section 39)", "order": 1, "mcqsCount": 8, "pyqsCount": 2, "estimatedMinutes": 18},
    {"id": "top-cnt-09-02", "chapterId": "ch-cnt-09", "subjectId": "law-contract", "title": "Damages for Breach: Rule in Hadley v Baxendale (Section 73)", "order": 2, "mcqsCount": 9, "pyqsCount": 2, "estimatedMinutes": 20},
    {"id": "top-cnt-09-03", "chapterId": "ch-cnt-09", "subjectId": "law-contract", "title": "Liquidated Damages vs Penalty: Indian Law Position (Section 74)", "order": 3, "mcqsCount": 8, "pyqsCount": 1, "estimatedMinutes": 17},
    # Ch 10
    {"id": "top-cnt-10-01", "chapterId": "ch-cnt-10", "subjectId": "law-contract", "title": "Contracts of Indemnity & Guarantee: Rights & Surety Liability (Sections 124–147)", "order": 1, "mcqsCount": 8, "pyqsCount": 2, "estimatedMinutes": 22},
    {"id": "top-cnt-10-02", "chapterId": "ch-cnt-10", "subjectId": "law-contract", "title": "Bailment: Duties of Bailor & Bailee, Bailee's Lien (Sections 148–171)", "order": 2, "mcqsCount": 8, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-cnt-10-03", "chapterId": "ch-cnt-10", "subjectId": "law-contract", "title": "Pledge: Rights of Pawnee & Pledge by Non-Owners (Sections 172–181)", "order": 3, "mcqsCount": 8, "pyqsCount": 1, "estimatedMinutes": 18},
    # Ch 11
    {"id": "top-cnt-11-01", "chapterId": "ch-cnt-11", "subjectId": "law-contract", "title": "Contract of Agency: Creation, Authority & Sub-Agent (Sections 182–210)", "order": 1, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 22},
    {"id": "top-cnt-11-02", "chapterId": "ch-cnt-11", "subjectId": "law-contract", "title": "Rights, Duties, Revocation & Principal's Liability (Sections 211–238)", "order": 2, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 23}
]


# -------------------------------------------------------------
# 3. TRANSFER OF PROPERTY ACT CHAPTERS & TOPICS
# -------------------------------------------------------------
TPA_CHAPTERS = [
    {
        "id": "ch-tpa-01",
        "subjectId": "law-tpa",
        "number": 1,
        "title": "Preliminary, Meaning of Transfer & What May Be Transferred",
        "sectionsRange": "Sections 1–9",
        "topicsCount": 3,
        "mcqsCount": 30,
        "pyqsCount": 8,
        "estimatedMinutes": 60,
        "weightage": "Very High"
    },
    {
        "id": "ch-tpa-02",
        "subjectId": "law-tpa",
        "number": 2,
        "title": "Restraints on Alienation & Rule Against Perpetuity",
        "sectionsRange": "Sections 10–18",
        "topicsCount": 3,
        "mcqsCount": 30,
        "pyqsCount": 7,
        "estimatedMinutes": 65,
        "weightage": "Very High"
    },
    {
        "id": "ch-tpa-03",
        "subjectId": "law-tpa",
        "number": 3,
        "title": "Vested & Contingent Interests, Conditional Transfers & Election",
        "sectionsRange": "Sections 19–37",
        "topicsCount": 3,
        "mcqsCount": 30,
        "pyqsCount": 6,
        "estimatedMinutes": 60,
        "weightage": "Very High"
    },
    {
        "id": "ch-tpa-04",
        "subjectId": "law-tpa",
        "number": 4,
        "title": "Doctrines of Notice, Ostensible Ownership & Feeding the Grant",
        "sectionsRange": "Sections 3, 41, 43",
        "topicsCount": 3,
        "mcqsCount": 30,
        "pyqsCount": 7,
        "estimatedMinutes": 65,
        "weightage": "Very High"
    },
    {
        "id": "ch-tpa-05",
        "subjectId": "law-tpa",
        "number": 5,
        "title": "Doctrines of Lis Pendens, Fraudulent Transfer & Part Performance",
        "sectionsRange": "Sections 52, 53, 53A",
        "topicsCount": 3,
        "mcqsCount": 30,
        "pyqsCount": 7,
        "estimatedMinutes": 65,
        "weightage": "Very High"
    },
    {
        "id": "ch-tpa-06",
        "subjectId": "law-tpa",
        "number": 6,
        "title": "Sale of Immovable Property & Exchange",
        "sectionsRange": "Sections 54–57, 118–121",
        "topicsCount": 3,
        "mcqsCount": 30,
        "pyqsCount": 4,
        "estimatedMinutes": 55,
        "weightage": "High"
    },
    {
        "id": "ch-tpa-07",
        "subjectId": "law-tpa",
        "number": 7,
        "title": "Mortgages of Immovable Property & Charges",
        "sectionsRange": "Sections 58–104",
        "topicsCount": 3,
        "mcqsCount": 30,
        "pyqsCount": 5,
        "estimatedMinutes": 65,
        "weightage": "Very High"
    },
    {
        "id": "ch-tpa-08",
        "subjectId": "law-tpa",
        "number": 8,
        "title": "Leases, Gifts & Actionable Claims",
        "sectionsRange": "Sections 105–137",
        "topicsCount": 3,
        "mcqsCount": 30,
        "pyqsCount": 3,
        "estimatedMinutes": 60,
        "weightage": "High"
    }
]

TPA_TOPICS = [
    # Ch 1
    {"id": "top-tpa-01-01", "chapterId": "ch-tpa-01", "subjectId": "law-tpa", "title": "Meaning and Scope of Transfer (Sections 1–5: Act Inter Vivos)", "order": 1, "mcqsCount": 10, "pyqsCount": 3, "estimatedMinutes": 20},
    {"id": "top-tpa-01-02", "chapterId": "ch-tpa-01", "subjectId": "law-tpa", "title": "What May Be Transferred & Non-Transferable Properties (Section 6)", "order": 2, "mcqsCount": 10, "pyqsCount": 3, "estimatedMinutes": 20},
    {"id": "top-tpa-01-03", "chapterId": "ch-tpa-01", "subjectId": "law-tpa", "title": "Competency to Transfer & Operation of Transfer (Sections 7, 8)", "order": 3, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    # Ch 2
    {"id": "top-tpa-02-01", "chapterId": "ch-tpa-02", "subjectId": "law-tpa", "title": "Conditions Restraining Alienation: Absolute vs Partial (Section 10)", "order": 1, "mcqsCount": 10, "pyqsCount": 3, "estimatedMinutes": 22},
    {"id": "top-tpa-02-02", "chapterId": "ch-tpa-02", "subjectId": "law-tpa", "title": "Transfer for Benefit of Unborn Persons & Prior Life Estate (Section 13)", "order": 2, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 21},
    {"id": "top-tpa-02-03", "chapterId": "ch-tpa-02", "subjectId": "law-tpa", "title": "Rule Against Perpetuity & Accumulation of Income (Sections 14, 17)", "order": 3, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 22},
    # Ch 3
    {"id": "top-tpa-03-01", "chapterId": "ch-tpa-03", "subjectId": "law-tpa", "title": "Vested Interest vs Contingent Interest (Sections 19, 21)", "order": 1, "mcqsCount": 10, "pyqsCount": 3, "estimatedMinutes": 20},
    {"id": "top-tpa-03-02", "chapterId": "ch-tpa-03", "subjectId": "law-tpa", "title": "Conditional Transfers: Condition Precedent vs Subsequent (Sections 25–34)", "order": 2, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-tpa-03-03", "chapterId": "ch-tpa-03", "subjectId": "law-tpa", "title": "Doctrine of Election: Foundation & Operation (Section 35)", "order": 3, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 20},
    # Ch 4
    {"id": "top-tpa-04-01", "chapterId": "ch-tpa-04", "subjectId": "law-tpa", "title": "Doctrine of Notice: Actual vs Constructive Notice (Section 3)", "order": 1, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 22},
    {"id": "top-tpa-04-02", "chapterId": "ch-tpa-04", "subjectId": "law-tpa", "title": "Transfer by Ostensible Owner & Benami Transactions (Section 41)", "order": 2, "mcqsCount": 10, "pyqsCount": 3, "estimatedMinutes": 22},
    {"id": "top-tpa-04-03", "chapterId": "ch-tpa-04", "subjectId": "law-tpa", "title": "Doctrine of Feeding the Grant by Estoppel (Section 43)", "order": 3, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 21},
    # Ch 5
    {"id": "top-tpa-05-01", "chapterId": "ch-tpa-05", "subjectId": "law-tpa", "title": "Doctrine of Lis Pendens & Pendente Lite Transfers (Section 52)", "order": 1, "mcqsCount": 10, "pyqsCount": 3, "estimatedMinutes": 22},
    {"id": "top-tpa-05-02", "chapterId": "ch-tpa-05", "subjectId": "law-tpa", "title": "Fraudulent Transfer & Protection of Creditors (Section 53)", "order": 2, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 21},
    {"id": "top-tpa-05-03", "chapterId": "ch-tpa-05", "subjectId": "law-tpa", "title": "Doctrine of Part Performance: Equitable Shield (Section 53A)", "order": 3, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 22},
    # Ch 6
    {"id": "top-tpa-06-01", "chapterId": "ch-tpa-06", "subjectId": "law-tpa", "title": "Concept and Essentials of Sale (Section 54: Sale vs Contract to Sell)", "order": 1, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 18},
    {"id": "top-tpa-06-02", "chapterId": "ch-tpa-06", "subjectId": "law-tpa", "title": "Rights and Liabilities of Buyer and Seller (Section 55)", "order": 2, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 19},
    {"id": "top-tpa-06-03", "chapterId": "ch-tpa-06", "subjectId": "law-tpa", "title": "Exchange of Immovable Property (Sections 118–121)", "order": 3, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 18},
    # Ch 7
    {"id": "top-tpa-07-01", "chapterId": "ch-tpa-07", "subjectId": "law-tpa", "title": "Concept of Mortgage & 6 Statutory Forms of Mortgage (Section 58)", "order": 1, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 22},
    {"id": "top-tpa-07-02", "chapterId": "ch-tpa-07", "subjectId": "law-tpa", "title": "Right of Redemption & Clog on Equity of Redemption (Section 60)", "order": 2, "mcqsCount": 10, "pyqsCount": 2, "estimatedMinutes": 22},
    {"id": "top-tpa-07-03", "chapterId": "ch-tpa-07", "subjectId": "law-tpa", "title": "Rights of Mortgagee, Subrogation (s. 92) & Charges (Section 100)", "order": 3, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 21},
    # Ch 8
    {"id": "top-tpa-08-01", "chapterId": "ch-tpa-08", "subjectId": "law-tpa", "title": "Leases of Immovable Property & Determination of Lease (Sections 105–117)", "order": 1, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-tpa-08-02", "chapterId": "ch-tpa-08", "subjectId": "law-tpa", "title": "Gifts: Essentials, Onerous Gifts & Revocation (Sections 122–129)", "order": 2, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 20},
    {"id": "top-tpa-08-03", "chapterId": "ch-tpa-08", "subjectId": "law-tpa", "title": "Transfer of Actionable Claims: Assignment & Notice (Sections 130–137)", "order": 3, "mcqsCount": 10, "pyqsCount": 1, "estimatedMinutes": 20}
]

# -------------------------------------------------------------
# WRITE FILES FUNCTION
# -------------------------------------------------------------
def write_js_file(filepath, var_name, data):
    content = f"""/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Judicial Learning Academy Data Module
 */
(function(global) {{
  'use strict';

  const DATA = {json.dumps(data, indent=2, ensure_ascii=False)};

  global.{var_name} = DATA;
  if (typeof module !== 'undefined' && module.exports) {{
    module.exports = DATA;
  }}
}})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Wrote {filepath} ({len(data)} items)")

# Write Jurisprudence
write_js_file('assets/learning/data/jurisprudence/jurisprudence-chapters.js', 'JURISPRUDENCE_CHAPTERS', JUR_CHAPTERS)
write_js_file('assets/learning/data/jurisprudence/jurisprudence-topics.js', 'JURISPRUDENCE_TOPICS', JUR_TOPICS)

# Write Contract
write_js_file('assets/learning/data/contract/contract-chapters.js', 'CONTRACT_CHAPTERS', CNT_CHAPTERS)
write_js_file('assets/learning/data/contract/contract-topics.js', 'CONTRACT_TOPICS', CNT_TOPICS)

# Write TPA
write_js_file('assets/learning/data/tpa/tpa-chapters.js', 'TPA_CHAPTERS', TPA_CHAPTERS)
write_js_file('assets/learning/data/tpa/tpa-topics.js', 'TPA_TOPICS', TPA_TOPICS)

print("Phase 2 Metadata generation complete!")
