"""
Build Social Legislation Metadata: Chapters & Topics
Outputs:
- assets/learning/data/social/social-chapters.js
- assets/learning/data/social/social-topics.js
"""

import json
import os

CHAPTERS = [
    # Act 1: Rights of Persons with Disabilities Act, 2016 (soc-disabilities)
    {
        "id": "ch-soc-disab-01",
        "subjectId": "soc-disabilities",
        "number": 1,
        "title": "Legislative Background, Guiding Principles & Key Definitions",
        "scope": "UN Convention on the Rights of Persons with Disabilities (UNCRPD), constitutional basis (Articles 14, 15, 21, 41), definitions of disability, person with benchmark disability (40% threshold), high support need, discrimination, reasonable accommodation, and the 21 specified disabilities under the Schedule.",
        "topicsCount": 3,
        "mcqsCount": 17,
        "pyqsCount": 2,
        "estimatedMinutes": 55,
        "weightage": "Very High"
    },
    {
        "id": "ch-soc-disab-02",
        "subjectId": "soc-disabilities",
        "number": 2,
        "title": "Substantive Rights, Education, Employment & Accessibility",
        "scope": "Rights to equality and non-discrimination (Section 3), community life, protection from cruelty and violence, inclusive education mandates (Sections 16-17), 4% employment reservation (Section 34), equal opportunity policies, and mandatory accessibility standards for built environment, transport, and ICT (Sections 40-46).",
        "topicsCount": 3,
        "mcqsCount": 17,
        "pyqsCount": 1,
        "estimatedMinutes": 60,
        "weightage": "Very High"
    },
    {
        "id": "ch-soc-disab-03",
        "subjectId": "soc-disabilities",
        "number": 3,
        "title": "Institutional Machinery, Special Courts & Penalties",
        "scope": "Central and State Advisory Boards (Sections 60-73), Chief Commissioner and State Commissioners for Persons with Disabilities (powers and inquiry functions under Sections 74-83), designation of Special Courts and Special Public Prosecutors (Sections 84-85), and penal provisions for offences and atrocities (Sections 89-95).",
        "topicsCount": 3,
        "mcqsCount": 16,
        "pyqsCount": 1,
        "estimatedMinutes": 50,
        "weightage": "High"
    },

    # Act 2: Maintenance and Welfare of Parents and Senior Citizens Act, 2007 (soc-parents)
    {
        "id": "ch-soc-parent-01",
        "subjectId": "soc-parents",
        "number": 1,
        "title": "Enactment, Scope, Objectives & Key Definitions",
        "scope": "Social context, Article 41 directive, Statement of Objects and Reasons, Act No. 56 of 2007, definitions of senior citizen (60 years), parent, children, relative, property, maintenance, and welfare under Section 2, and the statutory duty of children and relatives to maintain senior citizens (Section 4).",
        "topicsCount": 3,
        "mcqsCount": 17,
        "pyqsCount": 0,
        "estimatedMinutes": 50,
        "weightage": "High"
    },
    {
        "id": "ch-soc-parent-02",
        "subjectId": "soc-parents",
        "number": 2,
        "title": "Maintenance Proceedings & Adjudicative Tribunals",
        "scope": "Application for maintenance under Section 5, interim maintenance and expenses, conciliation proceedings (Section 6), constitution and jurisdiction of Maintenance Tribunal presided by Sub-Divisional Officer (Section 7), summary procedure (Section 8), determination of maintenance order (Section 9), Appellate Tribunal headed by District Magistrate (Sections 15-16), and statutory bar on legal representation (Section 17).",
        "topicsCount": 3,
        "mcqsCount": 17,
        "pyqsCount": 1,
        "estimatedMinutes": 60,
        "weightage": "Very High"
    },
    {
        "id": "ch-soc-parent-03",
        "subjectId": "soc-parents",
        "number": 3,
        "title": "Protection of Property, Medical Care & Offences",
        "scope": "Section 23 statutory deemed fraud and invalidation of conditional property transfers, judicial interpretation (Sudesh Chhikara v. Ramti Devi), establishment of old age homes (Section 19), medical support mandates (Section 20), offence of exposure and abandonment under Section 24, and cognizance and summary trial powers (Section 25).",
        "topicsCount": 3,
        "mcqsCount": 16,
        "pyqsCount": 0,
        "estimatedMinutes": 55,
        "weightage": "Very High"
    },

    # Act 3: Dowry Prohibition Act, 1961 (soc-dowry)
    {
        "id": "ch-soc-dowry-01",
        "subjectId": "soc-dowry",
        "number": 1,
        "title": "Origin, Policy, Definition & Statutory Scope",
        "scope": "Legislative history, 1984 and 1986 amendments, definition of 'dowry' under Section 2, property or valuable security in connection with marriage, distinction from customary presents and stridhan, Section 3 penalty for giving or taking dowry (minimum 5 years imprisonment and 15,000 rupees or value of dowry), and statutory exception for voluntary presents without demand under Section 3(2).",
        "topicsCount": 3,
        "mcqsCount": 17,
        "pyqsCount": 2,
        "estimatedMinutes": 55,
        "weightage": "Very High"
    },
    {
        "id": "ch-soc-dowry-02",
        "subjectId": "soc-dowry",
        "number": 2,
        "title": "Offences, Statutory Agreements & Stridhan Protection",
        "scope": "Penalty for demanding dowry under Section 4 (minimum 6 months up to 2 years), ban on advertisements offering share of property or money under Section 4A, agreements for giving or taking dowry declared void under Section 5, dowry to be held in trust for the benefit of wife or her heirs under Section 6, transfer timelines (3 months), and criminal breach of trust liability for failure to transfer.",
        "topicsCount": 3,
        "mcqsCount": 17,
        "pyqsCount": 1,
        "estimatedMinutes": 60,
        "weightage": "Very High"
    },
    {
        "id": "ch-soc-dowry-03",
        "subjectId": "soc-dowry",
        "number": 3,
        "title": "Cognizance, Evidentiary Burden & Enforcement Machinery",
        "scope": "Cognizance of offences by Metropolitan Magistrate or Judicial Magistrate First Class under Section 7, non-applicability of limitation under CrPC Section 468, offence classification as cognizable, non-bailable and non-compoundable under Section 8, statutory reverse burden of proof under Section 8A, appointment, powers and functions of Dowry Prohibition Officers under Section 8B, and interface with BNS Sections 80/85 (IPC 304B/498A).",
        "topicsCount": 3,
        "mcqsCount": 16,
        "pyqsCount": 2,
        "estimatedMinutes": 55,
        "weightage": "Very High"
    },

    # Act 4: Protection of Women from Domestic Violence Act, 2005 (soc-domestic-violence)
    {
        "id": "ch-soc-dv-01",
        "subjectId": "soc-domestic-violence",
        "number": 1,
        "title": "Purpose, Constitutional Roots & Key Definitions",
        "scope": "Enactment background, CEDAW and Vienna Accord foundations, civil law remedy structure, Section 2 definitions of aggrieved person, respondent (including female relatives post-Hiralal Mallick), domestic relationship, shared household, domestic incident report (DIR), and the comprehensive multi-dimensional definition of domestic violence under Section 3 (physical, sexual, verbal, emotional, and economic abuse).",
        "topicsCount": 3,
        "mcqsCount": 17,
        "pyqsCount": 1,
        "estimatedMinutes": 60,
        "weightage": "Very High"
    },
    {
        "id": "ch-soc-dv-02",
        "subjectId": "soc-domestic-violence",
        "number": 2,
        "title": "Enforcement Machinery & Shared Household Rights",
        "scope": "Section 17 statutory right to reside in shared household, evolution of judicial doctrine from S.R. Batra v. Taruna Batra to Satish Chander Ahuja v. Sneha Ahuja and Prabha Tyagi v. Kamlesh Devi, appointment, qualifications and duties of Protection Officers (Sections 8-9), registration and functions of Service Providers (Section 10), duties of shelter homes and medical facilities (Sections 6-7), and Section 12 application procedure and 60-day disposal norm.",
        "topicsCount": 3,
        "mcqsCount": 17,
        "pyqsCount": 1,
        "estimatedMinutes": 65,
        "weightage": "Very High"
    },
    {
        "id": "ch-soc-dv-03",
        "subjectId": "soc-domestic-violence",
        "number": 3,
        "title": "Statutory Reliefs, Enforcement & Breach Penalties",
        "scope": "Protection orders under Section 18, residence orders restraining dispossession or directing alternate accommodation under Section 19, monetary reliefs and maintenance under Section 20, temporary custody orders under Section 21, compensation orders under Section 22, ex-parte and interim orders under Section 23, criminal penalty for breach of protection order under Section 31 (cognizable and non-bailable), and appeal to Court of Session within 30 days under Section 29.",
        "topicsCount": 3,
        "mcqsCount": 16,
        "pyqsCount": 0,
        "estimatedMinutes": 55,
        "weightage": "Very High"
    },

    # Act 5: Sexual Harassment of Women at Workplace Act, 2013 (soc-posh)
    {
        "id": "ch-soc-posh-01",
        "subjectId": "soc-posh",
        "number": 1,
        "title": "Vishaka Foundations, Scope & Key Concepts",
        "scope": "Judicial origins in Vishaka v. State of Rajasthan (1997), constitutional roots in Articles 14, 19(1)(g) and 21, Act No. 14 of 2013, definitions of aggrieved woman (any woman regardless of employment status), employee (regular, temporary, ad-hoc, daily wage, probationer, intern), workplace including transportation provided by employer (extended workplace doctrine), and Section 3 sexual harassment forms (quid pro quo vs hostile work environment).",
        "topicsCount": 3,
        "mcqsCount": 17,
        "pyqsCount": 0,
        "estimatedMinutes": 55,
        "weightage": "Very High"
    },
    {
        "id": "ch-soc-posh-02",
        "subjectId": "soc-posh",
        "number": 2,
        "title": "Institutional Committees & Inquiry Procedures",
        "scope": "Mandatory constitution of Internal Committee (IC) by employers with 10 or more workers (Section 4), composition: Presiding Officer woman, 2 employee members, 1 external NGO member (50% women requirement), Local Committee (LC) constituted by District Officer for establishments with fewer than 10 workers or complaints against employer (Sections 6-7), complaint submission within 3 months (Section 9), conciliation without monetary settlement (Section 10), and inquiry under service rules with CPC civil court powers (Section 11).",
        "topicsCount": 3,
        "mcqsCount": 17,
        "pyqsCount": 1,
        "estimatedMinutes": 65,
        "weightage": "Very High"
    },
    {
        "id": "ch-soc-posh-03",
        "subjectId": "soc-posh",
        "number": 3,
        "title": "Inquiry Reports, Employer Duties & Penalties",
        "scope": "Interim relief during pendency (transfer, leave up to 3 months under Section 12), completion of inquiry within 90 days and report within 10 days (Section 13), determination of compensation based on mental trauma, loss of career opportunities and respondent's financial capacity (Section 15), strict ban on publication of identity and inquiry contents under Section 16, penalty for non-compliance by employer (50,000 rupees fine, cancellation of license under Section 26), and appeal within 90 days under Section 18.",
        "topicsCount": 3,
        "mcqsCount": 16,
        "pyqsCount": 0,
        "estimatedMinutes": 55,
        "weightage": "Very High"
    },

    # Act 6: PCPNDT Act, 1994 (soc-pcpndt)
    {
        "id": "ch-soc-pcpndt-01",
        "subjectId": "soc-pcpndt",
        "number": 1,
        "title": "Social Context, Preamble & Regulatory Scheme",
        "scope": "Socio-demographic crisis of skewed child sex ratio, 1994 enactment and comprehensive 2003 amendment bringing pre-conception sex selection within the statutory net, definitions of genetic counselling centre, genetic laboratory, genetic clinic, pre-natal diagnostic procedures, sex selection, and strict statutory conditions under Section 4 permitting diagnostic tests only for detecting genetic abnormalities and strictly excluding sex determination.",
        "topicsCount": 3,
        "mcqsCount": 17,
        "pyqsCount": 1,
        "estimatedMinutes": 55,
        "weightage": "Very High"
    },
    {
        "id": "ch-soc-pcpndt-02",
        "subjectId": "soc-pcpndt",
        "number": 2,
        "title": "Absolute Prohibitions, Registration & Record Maintenance",
        "scope": "Absolute prohibition of communicating sex of foetus under Section 5(2), total ban on pre-conception and pre-natal sex selection under Section 6, mandatory registration of ultrasound machines, imaging centres and clinics under Section 18, strict maintenance of records including statutory Form F under Section 29, minimum 2-year record preservation mandate, and search and seizure consequences for non-maintenance of records (Voluntary Health Association of India v. UOI).",
        "topicsCount": 3,
        "mcqsCount": 17,
        "pyqsCount": 0,
        "estimatedMinutes": 60,
        "weightage": "Very High"
    },
    {
        "id": "ch-soc-pcpndt-03",
        "subjectId": "soc-pcpndt",
        "number": 3,
        "title": "Enforcement Authorities, Search & Seizure & Penalties",
        "scope": "Central and State Supervisory Boards (Sections 7-16A), Appointment, powers, and duties of Appropriate Authorities and Advisory Committees (Sections 17-17A), extraordinary search, seizure and seal powers under Section 30, offences and graded penalties for medical professionals and commercial operators under Section 23 (up to 3 years imprisonment on first conviction, 5 years on subsequent), removal of name from State Medical Register, statutory presumption of guilt under Section 24, and cognizance exclusively on complaint by Appropriate Authority under Section 28.",
        "topicsCount": 3,
        "mcqsCount": 16,
        "pyqsCount": 1,
        "estimatedMinutes": 55,
        "weightage": "Very High"
    },

    # Act 7: Medical Termination of Pregnancy Act, 1971 (soc-mtp)
    {
        "id": "ch-soc-mtp-01",
        "subjectId": "soc-mtp",
        "number": 1,
        "title": "History, Legislative Intent & Key Definitions",
        "scope": "Shantilal Shah Committee recommendations (1966), Act No. 34 of 1971, exceptions to criminal provisions in BNS Sections 90-92 (IPC 312-314), definitions of registered medical practitioner (RMP), guardian, mentally ill person, and the transformative 2021 Amendment replacing 'married woman and her husband' with 'woman and her partner' to secure reproductive autonomy and dignity (X v. Principal Secretary, Health and Family Welfare Dept., Delhi, 2022).",
        "topicsCount": 3,
        "mcqsCount": 17,
        "pyqsCount": 1,
        "estimatedMinutes": 55,
        "weightage": "Very High"
    },
    {
        "id": "ch-soc-mtp-02",
        "subjectId": "soc-mtp",
        "number": 2,
        "title": "Gestational Framework & Permissible Grounds",
        "scope": "The statutory three-tier gestational ceiling post-2021: up to 20 weeks on opinion of one RMP; 20 to 24 weeks on opinion of two RMPs for prescribed categories of vulnerable women (survivors of sexual assault/rape/incest, minors, change of marital status during pregnancy, women with physical/mental disabilities, disaster/humanitarian emergencies); and termination beyond 24 weeks without gestational ceiling for substantial foetal abnormalities approved by State Medical Board under Section 3(2B). Section 5 emergency life-saving exception.",
        "topicsCount": 3,
        "mcqsCount": 17,
        "pyqsCount": 1,
        "estimatedMinutes": 65,
        "weightage": "Very High"
    },
    {
        "id": "ch-soc-mtp-03",
        "subjectId": "soc-mtp",
        "number": 3,
        "title": "Consent, Confidentiality, Approval & Penalties",
        "scope": "Consent regime under Section 3(4): sole consent of pregnant adult woman mandatory; spousal or parental consent not required; guardian consent required only where woman is minor (under 18) or mentally ill; place of termination approved by Government (Section 4); maintenance of confidential admission register; privacy safeguards and punishment for disclosure of woman's identity under Section 5A (up to 1 year imprisonment); and penal consequences for unlawful terminations by unqualified persons under Section 5.",
        "topicsCount": 3,
        "mcqsCount": 16,
        "pyqsCount": 1,
        "estimatedMinutes": 55,
        "weightage": "Very High"
    },

    # Act 8: Indecent Representation of Women (Prohibition) Act, 1986 (soc-indecent-rep)
    {
        "id": "ch-soc-irwa-01",
        "subjectId": "soc-indecent-rep",
        "number": 1,
        "title": "Origin, Policy, Scope & Core Prohibition",
        "scope": "Legislative genesis, Act No. 60 of 1986, constitutional mandate of gender dignity under Article 51A(e), definitions of 'indecent representation of women' (depiction derogatory, denigrating, or corrupting public morality), advertisement, distribution, book, pamphlet, slide, film, writing, and Section 3 absolute prohibition on publishing or causing to be published advertisements containing indecent representation of women.",
        "topicsCount": 3,
        "mcqsCount": 15,
        "pyqsCount": 1,
        "estimatedMinutes": 50,
        "weightage": "High"
    },
    {
        "id": "ch-soc-irwa-02",
        "subjectId": "soc-indecent-rep",
        "number": 2,
        "title": "Distribution Prohibitions & Statutory Exceptions",
        "scope": "Section 4 prohibition on production, sale, hire, distribution, circulation or sending by post of books, pamphlets, papers, slides, films or drawings containing indecent representation; statutory exceptions under Section 4 proviso: publications justified in public good in the interest of science, literature, art or learning, bona fide religious purposes, ancient monuments, sculptures in temples, and films certified under Cinematograph Act, 1952; and application to modern digital media alongside Information Technology Act, 2000 (Section 67).",
        "topicsCount": 3,
        "mcqsCount": 15,
        "pyqsCount": 1,
        "estimatedMinutes": 55,
        "weightage": "Very High"
    },
    {
        "id": "ch-soc-irwa-03",
        "subjectId": "soc-indecent-rep",
        "number": 3,
        "title": "Enforcement Powers, Corporate Liability & Penalties",
        "scope": "Section 5 powers of authorized Gazetted Officers to enter, search, seize and inspect premises, vehicles, and packages, requirement of warrant for private dwellings, seizure procedures and intimation to nearest Magistrate, Section 6 graded penalties: first conviction up to 2 years imprisonment and 2,000 rupees fine; second or subsequent conviction minimum 6 months up to 5 years imprisonment and 10,000 to 1,00,000 rupees fine; offences by companies under Section 7; and cognizable and bailable nature of offences under Section 8.",
        "topicsCount": 3,
        "mcqsCount": 15,
        "pyqsCount": 1,
        "estimatedMinutes": 50,
        "weightage": "High"
    },

    # Act 9: Protection of Children from Sexual Offences Act, 2012 (soc-pocso)
    {
        "id": "ch-soc-pocso-01",
        "subjectId": "soc-pocso",
        "number": 1,
        "title": "International Roots, Preamble & Key Definitions",
        "scope": "UN Convention on the Rights of the Child (CRC 1989), Article 15(3) constitutional backing, Act No. 32 of 2012, definition of 'child' under Section 2(1)(d) strictly meaning any person below 18 years of age, gender-neutral protection for male, female and transgender children, and primacy of child's best interests as the guiding interpretive touchstone across all proceedings.",
        "topicsCount": 3,
        "mcqsCount": 15,
        "pyqsCount": 1,
        "estimatedMinutes": 55,
        "weightage": "Very High"
    },
    {
        "id": "ch-soc-pocso-02",
        "subjectId": "soc-pocso",
        "number": 2,
        "title": "Substantive Offences & Graded Punishments",
        "scope": "Penetrative sexual assault under Section 3 and punishment under Section 4 (minimum 10 years up to life imprisonment); aggravated penetrative sexual assault under Section 5 (committed by police, armed forces, public servants, teachers, hospital staff, family members, or on child under 12/16) and punishment under Section 6 (minimum 20 years up to life imprisonment or death post-2019 amendment); sexual assault under Section 7-8; aggravated sexual assault under Section 9-10; sexual harassment under Section 11-12; and child pornography and storage under Sections 13-15.",
        "topicsCount": 3,
        "mcqsCount": 15,
        "pyqsCount": 0,
        "estimatedMinutes": 65,
        "weightage": "Very High"
    },
    {
        "id": "ch-soc-pocso-03",
        "subjectId": "soc-pocso",
        "number": 3,
        "title": "Mandatory Reporting, Investigation & Medical Care",
        "scope": "Mandatory reporting obligation under Section 19 on any person having apprehension or knowledge of offence, immunity for reporting in good faith (Section 19(7)), criminal penalty for failure to report under Section 21 (up to 6 months imprisonment or fine; 1 year for in-charge of institution), investigation procedures under Section 24: Special Juvenile Police Unit (SJPU) or child welfare police officer, recording statement at child's residence, no uniform, no detention of child in police station at night, and medical examination within 24 hours under Section 27.",
        "topicsCount": 3,
        "mcqsCount": 15,
        "pyqsCount": 0,
        "estimatedMinutes": 60,
        "weightage": "Very High"
    },
    {
        "id": "ch-soc-pocso-04",
        "subjectId": "soc-pocso",
        "number": 4,
        "title": "Special Courts, Child-Friendly Trial & Statutory Presumptions",
        "scope": "Designation of Court of Session as Special Court under Section 28, recording of child's evidence within 30 days of cognizance and completion of trial within 1 year (Section 35), child-friendly trial safeguards: in-camera trial (Section 37), frequent breaks, no aggressive questioning, non-confrontation with accused via video-link or single-way mirrors (Section 36), legal aid and support persons (Section 39-40), statutory presumptions of culpable mental state and guilt under Sections 29 and 30, and Section 42A overriding effect over inconsistent laws.",
        "topicsCount": 3,
        "mcqsCount": 15,
        "pyqsCount": 1,
        "estimatedMinutes": 65,
        "weightage": "Very High"
    }
]

TOPICS = [
    # Act 1: Rights of Persons with Disabilities Act, 2016
    {
        "id": "top-disab-01-01",
        "chapterId": "ch-soc-disab-01",
        "subjectId": "soc-disabilities",
        "title": "UNCRPD Background, Salient Features & Constitutional Underpinnings",
        "order": 1,
        "mcqsCount": 6,
        "pyqsCount": 1,
        "estimatedMinutes": 18
    },
    {
        "id": "top-disab-01-02",
        "chapterId": "ch-soc-disab-01",
        "subjectId": "soc-disabilities",
        "title": "Key Definitions: Disability, Benchmark Disability (40%), High Support Need & Discrimination",
        "order": 2,
        "mcqsCount": 6,
        "pyqsCount": 1,
        "estimatedMinutes": 20
    },
    {
        "id": "top-disab-01-03",
        "chapterId": "ch-soc-disab-01",
        "subjectId": "soc-disabilities",
        "title": "The 21 Specified Disabilities in the Schedule: Physical, Intellectual & Mental",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 17
    },
    {
        "id": "top-disab-02-01",
        "chapterId": "ch-soc-disab-02",
        "subjectId": "soc-disabilities",
        "title": "Rights & Entitlements: Equality, Non-Discrimination, Community Life & Legal Capacity",
        "order": 1,
        "mcqsCount": 6,
        "pyqsCount": 0,
        "estimatedMinutes": 20
    },
    {
        "id": "top-disab-02-02",
        "chapterId": "ch-soc-disab-02",
        "subjectId": "soc-disabilities",
        "title": "Education & Employment Mandates: Inclusive Education, 4% Reservation & Equal Opportunity",
        "order": 2,
        "mcqsCount": 6,
        "pyqsCount": 1,
        "estimatedMinutes": 22
    },
    {
        "id": "top-disab-02-03",
        "chapterId": "ch-soc-disab-02",
        "subjectId": "soc-disabilities",
        "title": "Accessibility Architecture: Built Environment, Transport, ICT & Mandatory Audits",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 18
    },
    {
        "id": "top-disab-03-01",
        "chapterId": "ch-soc-disab-03",
        "subjectId": "soc-disabilities",
        "title": "Central & State Advisory Boards: Composition, Functions & Tenure",
        "order": 1,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 16
    },
    {
        "id": "top-disab-03-02",
        "chapterId": "ch-soc-disab-03",
        "subjectId": "soc-disabilities",
        "title": "Chief Commissioner & State Commissioners for PwD: Inquiries, Powers & Grievance Redressal",
        "order": 2,
        "mcqsCount": 6,
        "pyqsCount": 0,
        "estimatedMinutes": 18
    },
    {
        "id": "top-disab-03-03",
        "chapterId": "ch-soc-disab-03",
        "subjectId": "soc-disabilities",
        "title": "Special Courts, Special Public Prosecutors & Offences / Penalties (Sections 84–95)",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 1,
        "estimatedMinutes": 16
    },

    # Act 2: Maintenance and Welfare of Parents and Senior Citizens Act, 2007
    {
        "id": "top-parent-01-01",
        "chapterId": "ch-soc-parent-01",
        "subjectId": "soc-parents",
        "title": "Legislative History, Statement of Objects and Constitutional Directive (Art. 41)",
        "order": 1,
        "mcqsCount": 6,
        "pyqsCount": 0,
        "estimatedMinutes": 16
    },
    {
        "id": "top-parent-01-02",
        "chapterId": "ch-soc-parent-01",
        "subjectId": "soc-parents",
        "title": "Statutory Definitions: Senior Citizen (60+), Parent, Children, Relative & Welfare",
        "order": 2,
        "mcqsCount": 6,
        "pyqsCount": 0,
        "estimatedMinutes": 18
    },
    {
        "id": "top-parent-01-03",
        "chapterId": "ch-soc-parent-01",
        "subjectId": "soc-parents",
        "title": "Duty to Maintain: Obligation of Children & Relatives Entitled to Inherit Property",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 16
    },
    {
        "id": "top-parent-02-01",
        "chapterId": "ch-soc-parent-02",
        "subjectId": "soc-parents",
        "title": "Maintenance Application (S. 4–5): Filing, Interim Maintenance & Maximum Cap Evolution",
        "order": 1,
        "mcqsCount": 6,
        "pyqsCount": 1,
        "estimatedMinutes": 20
    },
    {
        "id": "top-parent-02-02",
        "chapterId": "ch-soc-parent-02",
        "subjectId": "soc-parents",
        "title": "Constitution and Procedure of Maintenance Tribunals (S. 7–14, SDO Adjudication)",
        "order": 2,
        "mcqsCount": 6,
        "pyqsCount": 0,
        "estimatedMinutes": 22
    },
    {
        "id": "top-parent-02-03",
        "chapterId": "ch-soc-parent-02",
        "subjectId": "soc-parents",
        "title": "Appellate Tribunal (S. 15–18, District Magistrate) & Bar on Legal Practitioners (S. 17)",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 18
    },
    {
        "id": "top-parent-03-01",
        "chapterId": "ch-soc-parent-03",
        "subjectId": "soc-parents",
        "title": "Section 23: Invalidation of Property Transfers Conditioned on Maintenance & Landmark Precedents",
        "order": 1,
        "mcqsCount": 6,
        "pyqsCount": 0,
        "estimatedMinutes": 22
    },
    {
        "id": "top-parent-03-02",
        "chapterId": "ch-soc-parent-03",
        "subjectId": "soc-parents",
        "title": "Medical Care, Old Age Homes & State Welfare Safeguards (Sections 19–20)",
        "order": 2,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 16
    },
    {
        "id": "top-parent-03-03",
        "chapterId": "ch-soc-parent-03",
        "subjectId": "soc-parents",
        "title": "Section 24: Abandonment of Senior Citizens, Penalties & Summary Trial Procedures",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 17
    },

    # Act 3: Dowry Prohibition Act, 1961
    {
        "id": "top-dowry-01-01",
        "chapterId": "ch-soc-dowry-01",
        "subjectId": "soc-dowry",
        "title": "Legislative Scheme, Objectives and 1984/1986 Amendments",
        "order": 1,
        "mcqsCount": 6,
        "pyqsCount": 1,
        "estimatedMinutes": 18
    },
    {
        "id": "top-dowry-01-02",
        "chapterId": "ch-soc-dowry-01",
        "subjectId": "soc-dowry",
        "title": "Statutory Definition of 'Dowry' under Section 2 vs Traditional Presents / Stridhan",
        "order": 2,
        "mcqsCount": 6,
        "pyqsCount": 1,
        "estimatedMinutes": 20
    },
    {
        "id": "top-dowry-01-03",
        "chapterId": "ch-soc-dowry-01",
        "subjectId": "soc-dowry",
        "title": "Section 3: Penalties for Giving or Taking Dowry & Statutory Exclusion for Customary Gifts",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 17
    },
    {
        "id": "top-dowry-02-01",
        "chapterId": "ch-soc-dowry-02",
        "subjectId": "soc-dowry",
        "title": "Section 4 & 4A: Demanding Dowry and Ban on Advertisements Offering Property",
        "order": 1,
        "mcqsCount": 6,
        "pyqsCount": 1,
        "estimatedMinutes": 20
    },
    {
        "id": "top-dowry-02-02",
        "chapterId": "ch-soc-dowry-02",
        "subjectId": "soc-dowry",
        "title": "Section 5: Agreements for Giving/Taking Dowry to be Void & Unenforceable",
        "order": 2,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 18
    },
    {
        "id": "top-dowry-02-03",
        "chapterId": "ch-soc-dowry-02",
        "subjectId": "soc-dowry",
        "title": "Section 6: Dowry to be for Benefit of Wife / Heirs & Criminal Breach of Trust Interface",
        "order": 3,
        "mcqsCount": 6,
        "pyqsCount": 0,
        "estimatedMinutes": 22
    },
    {
        "id": "top-dowry-03-01",
        "chapterId": "ch-soc-dowry-03",
        "subjectId": "soc-dowry",
        "title": "Section 7: Cognizance of Offences, Competent Magistrates & Non-applicability of CrPC S. 468",
        "order": 1,
        "mcqsCount": 5,
        "pyqsCount": 1,
        "estimatedMinutes": 18
    },
    {
        "id": "top-dowry-03-02",
        "chapterId": "ch-soc-dowry-03",
        "subjectId": "soc-dowry",
        "title": "Section 8 & 8A: Offence Classification (Cognizable/Non-Bailable) & Reverse Burden of Proof",
        "order": 2,
        "mcqsCount": 6,
        "pyqsCount": 1,
        "estimatedMinutes": 20
    },
    {
        "id": "top-dowry-03-03",
        "chapterId": "ch-soc-dowry-03",
        "subjectId": "soc-dowry",
        "title": "Section 8B: Dowry Prohibition Officers & Interplay with BNS 80/85 (IPC 304B/498A)",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 17
    },

    # Act 4: Protection of Women from Domestic Violence Act, 2005
    {
        "id": "top-dv-01-01",
        "chapterId": "ch-soc-dv-01",
        "subjectId": "soc-domestic-violence",
        "title": "Legislative Purpose, CEDAW Framework & Civil Remedy Architecture",
        "order": 1,
        "mcqsCount": 6,
        "pyqsCount": 0,
        "estimatedMinutes": 18
    },
    {
        "id": "top-dv-01-02",
        "chapterId": "ch-soc-dv-01",
        "subjectId": "soc-domestic-violence",
        "title": "Section 2 Definitions: Aggrieved Person, Respondent, Domestic Relationship & DIR",
        "order": 2,
        "mcqsCount": 6,
        "pyqsCount": 1,
        "estimatedMinutes": 22
    },
    {
        "id": "top-dv-01-03",
        "chapterId": "ch-soc-dv-01",
        "subjectId": "soc-domestic-violence",
        "title": "Section 3: Definition and Dimensions of Domestic Violence (Physical, Sexual, Emotional, Economic)",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 20
    },
    {
        "id": "top-dv-02-01",
        "chapterId": "ch-soc-dv-02",
        "subjectId": "soc-domestic-violence",
        "title": "Section 17: Right to Reside in Shared Household (Satish Chander Ahuja & Prabha Tyagi Doctrines)",
        "order": 1,
        "mcqsCount": 6,
        "pyqsCount": 1,
        "estimatedMinutes": 24
    },
    {
        "id": "top-dv-02-02",
        "chapterId": "ch-soc-dv-02",
        "subjectId": "soc-domestic-violence",
        "title": "Protection Officers, Service Providers & Shelter Homes (Sections 8–11)",
        "order": 2,
        "mcqsCount": 6,
        "pyqsCount": 0,
        "estimatedMinutes": 20
    },
    {
        "id": "top-dv-02-03",
        "chapterId": "ch-soc-dv-02",
        "subjectId": "soc-domestic-violence",
        "title": "Procedure for Applications under Section 12, Notice (S. 13) & 60-Day Disposal Mandate (S. 12(5))",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 21
    },
    {
        "id": "top-dv-03-01",
        "chapterId": "ch-soc-dv-03",
        "subjectId": "soc-domestic-violence",
        "title": "Section 18: Protection Orders & Section 19: Residence Orders (Restraining Dispossession)",
        "order": 1,
        "mcqsCount": 6,
        "pyqsCount": 0,
        "estimatedMinutes": 20
    },
    {
        "id": "top-dv-03-02",
        "chapterId": "ch-soc-dv-03",
        "subjectId": "soc-domestic-violence",
        "title": "Monetary Relief (S. 20), Custody Orders (S. 21) & Ex-Parte / Interim Reliefs (S. 23)",
        "order": 2,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 18
    },
    {
        "id": "top-dv-03-03",
        "chapterId": "ch-soc-dv-03",
        "subjectId": "soc-domestic-violence",
        "title": "Section 31: Penalty for Breach of Protection Order, Cognizance & Section 29 Appeals",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 17
    },

    # Act 5: Sexual Harassment of Women at Workplace Act, 2013 (POSH)
    {
        "id": "top-posh-01-01",
        "chapterId": "ch-soc-posh-01",
        "subjectId": "soc-posh",
        "title": "From Vishaka (1997) to POSH Act: Constitutional Foundations & International Obligations",
        "order": 1,
        "mcqsCount": 6,
        "pyqsCount": 0,
        "estimatedMinutes": 18
    },
    {
        "id": "top-posh-01-02",
        "chapterId": "ch-soc-posh-01",
        "subjectId": "soc-posh",
        "title": "Key Definitions: Aggrieved Woman, Employee, Workplace (Extended Workplace) & Employer",
        "order": 2,
        "mcqsCount": 6,
        "pyqsCount": 0,
        "estimatedMinutes": 20
    },
    {
        "id": "top-posh-01-03",
        "chapterId": "ch-soc-posh-01",
        "subjectId": "soc-posh",
        "title": "Section 3: Sexual Harassment Concepts: Quid Pro Quo vs Hostile Work Environment",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 17
    },
    {
        "id": "top-posh-02-01",
        "chapterId": "ch-soc-posh-02",
        "subjectId": "soc-posh",
        "title": "Internal Committee (IC): Constitution, Presiding Officer, External Member & 10-Worker Threshold",
        "order": 1,
        "mcqsCount": 6,
        "pyqsCount": 1,
        "estimatedMinutes": 22
    },
    {
        "id": "top-posh-02-02",
        "chapterId": "ch-soc-posh-02",
        "subjectId": "soc-posh",
        "title": "Local Committee (LC): Constitution, District Officer & Unorganized Sector Coverage (S. 6–7)",
        "order": 2,
        "mcqsCount": 6,
        "pyqsCount": 0,
        "estimatedMinutes": 21
    },
    {
        "id": "top-posh-02-03",
        "chapterId": "ch-soc-posh-02",
        "subjectId": "soc-posh",
        "title": "Complaint Mechanism (S. 9): 3-Month Limitation, Conciliation (S. 10) & Natural Justice Inquiry",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 22
    },
    {
        "id": "top-posh-03-01",
        "chapterId": "ch-soc-posh-03",
        "subjectId": "soc-posh",
        "title": "Inquiry Report, Recommendations & Interim Measures (Leave, Transfer) during Pendency (S. 12–13)",
        "order": 1,
        "mcqsCount": 6,
        "pyqsCount": 0,
        "estimatedMinutes": 20
    },
    {
        "id": "top-posh-03-02",
        "chapterId": "ch-soc-posh-03",
        "subjectId": "soc-posh",
        "title": "Section 16: Strict Prohibition of Publication of Contents of Complaint, Inquiry & Identity",
        "order": 2,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 18
    },
    {
        "id": "top-posh-03-03",
        "chapterId": "ch-soc-posh-03",
        "subjectId": "soc-posh",
        "title": "Duties of Employer (S. 19), Penalties for Non-Compliance (S. 26) & Section 18 Appeals",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 17
    },

    # Act 6: PCPNDT Act, 1994
    {
        "id": "top-pcpndt-01-01",
        "chapterId": "ch-soc-pcpndt-01",
        "subjectId": "soc-pcpndt",
        "title": "Historical Context, Declining Child Sex Ratio & 2003 Pre-Conception Amendments",
        "order": 1,
        "mcqsCount": 6,
        "pyqsCount": 1,
        "estimatedMinutes": 18
    },
    {
        "id": "top-pcpndt-01-02",
        "chapterId": "ch-soc-pcpndt-01",
        "subjectId": "soc-pcpndt",
        "title": "Key Definitions: Genetic Clinic, Laboratory, Pre-Natal Diagnostic Procedures & Sex Selection",
        "order": 2,
        "mcqsCount": 6,
        "pyqsCount": 0,
        "estimatedMinutes": 20
    },
    {
        "id": "top-pcpndt-01-03",
        "chapterId": "ch-soc-pcpndt-01",
        "subjectId": "soc-pcpndt",
        "title": "Regulation of Pre-Natal Diagnostic Techniques: Permissible Indications & Strict Exclusions (S. 4)",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 17
    },
    {
        "id": "top-pcpndt-02-01",
        "chapterId": "ch-soc-pcpndt-02",
        "subjectId": "soc-pcpndt",
        "title": "Section 5 & 6: Absolute Ban on Sex Selection & Prohibition on Communicating Foetal Sex",
        "order": 1,
        "mcqsCount": 6,
        "pyqsCount": 0,
        "estimatedMinutes": 21
    },
    {
        "id": "top-pcpndt-02-02",
        "chapterId": "ch-soc-pcpndt-02",
        "subjectId": "soc-pcpndt",
        "title": "Mandatory Registration of Genetic Clinics & Ultrasound Machines (Sections 18–21)",
        "order": 2,
        "mcqsCount": 6,
        "pyqsCount": 0,
        "estimatedMinutes": 20
    },
    {
        "id": "top-pcpndt-02-03",
        "chapterId": "ch-soc-pcpndt-02",
        "subjectId": "soc-pcpndt",
        "title": "Record Maintenance Mandates (Form F), Preservation Periods (2 Years) & Sealing Powers",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 19
    },
    {
        "id": "top-pcpndt-03-01",
        "chapterId": "ch-soc-pcpndt-03",
        "subjectId": "soc-pcpndt",
        "title": "Central & State Supervisory Boards (CSB/SSB): Composition and Policy Mandates (Sections 7–16)",
        "order": 1,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 17
    },
    {
        "id": "top-pcpndt-03-02",
        "chapterId": "ch-soc-pcpndt-03",
        "subjectId": "soc-pcpndt",
        "title": "Appropriate Authorities & Advisory Committees: Inspection, Search & Seizure (Sections 17 & 30)",
        "order": 2,
        "mcqsCount": 6,
        "pyqsCount": 1,
        "estimatedMinutes": 20
    },
    {
        "id": "top-pcpndt-03-03",
        "chapterId": "ch-soc-pcpndt-03",
        "subjectId": "soc-pcpndt",
        "title": "Offences, Penalties (S. 23), Reverse Burden of Proof (S. 24) & Cognizance Safeguards (S. 28)",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 18
    },

    # Act 7: Medical Termination of Pregnancy Act, 1971
    {
        "id": "top-mtp-01-01",
        "chapterId": "ch-soc-mtp-01",
        "subjectId": "soc-mtp",
        "title": "Legislative Scheme, Shantilal Shah Committee & Constitutional Privacy Protections",
        "order": 1,
        "mcqsCount": 6,
        "pyqsCount": 1,
        "estimatedMinutes": 18
    },
    {
        "id": "top-mtp-01-02",
        "chapterId": "ch-soc-mtp-01",
        "subjectId": "soc-mtp",
        "title": "Key Definitions: Registered Medical Practitioner (RMP), Guardian & Mentally Ill Person",
        "order": 2,
        "mcqsCount": 6,
        "pyqsCount": 0,
        "estimatedMinutes": 18
    },
    {
        "id": "top-mtp-01-03",
        "chapterId": "ch-soc-mtp-01",
        "subjectId": "soc-mtp",
        "title": "The 2021 Amendment Paradigm: Expanding Scope to Unmarried Women & Reproductive Autonomy",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 19
    },
    {
        "id": "top-mtp-02-01",
        "chapterId": "ch-soc-mtp-02",
        "subjectId": "soc-mtp",
        "title": "Gestational Tiers: Up to 20 Weeks (1 RMP) & 20–24 Weeks (2 RMPs for Vulnerable Categories)",
        "order": 1,
        "mcqsCount": 6,
        "pyqsCount": 1,
        "estimatedMinutes": 23
    },
    {
        "id": "top-mtp-02-02",
        "chapterId": "ch-soc-mtp-02",
        "subjectId": "soc-mtp",
        "title": "Termination Beyond 24 Weeks: Substantial Foetal Abnormalities & Medical Board Certification",
        "order": 2,
        "mcqsCount": 6,
        "pyqsCount": 0,
        "estimatedMinutes": 22
    },
    {
        "id": "top-mtp-02-03",
        "chapterId": "ch-soc-mtp-02",
        "subjectId": "soc-mtp",
        "title": "Section 5: Emergency Exception (Life-Saving Termination Without Gestational Limits)",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 20
    },
    {
        "id": "top-mtp-03-01",
        "chapterId": "ch-soc-mtp-03",
        "subjectId": "soc-mtp",
        "title": "Consent Regime (S. 3(4)): Woman's Sole Consent vs Guardian Consent (Minor / Mentally Ill)",
        "order": 1,
        "mcqsCount": 6,
        "pyqsCount": 1,
        "estimatedMinutes": 19
    },
    {
        "id": "top-mtp-03-02",
        "chapterId": "ch-soc-mtp-03",
        "subjectId": "soc-mtp",
        "title": "Approved Places for Termination (S. 4) & Maintenance of Confidential Admission Register",
        "order": 2,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 18
    },
    {
        "id": "top-mtp-03-03",
        "chapterId": "ch-soc-mtp-03",
        "subjectId": "soc-mtp",
        "title": "Offences and Penalties under Section 5A (Privacy Breach) & Interplay with BNS 90–92 (IPC 312–314)",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 18
    },

    # Act 8: Indecent Representation of Women (Prohibition) Act, 1986
    {
        "id": "top-irwa-01-01",
        "chapterId": "ch-soc-irwa-01",
        "subjectId": "soc-indecent-rep",
        "title": "Historical Context, Rajya Sabha Debates and Salient Features of Act No. 60 of 1986",
        "order": 1,
        "mcqsCount": 5,
        "pyqsCount": 1,
        "estimatedMinutes": 16
    },
    {
        "id": "top-irwa-01-02",
        "chapterId": "ch-soc-irwa-01",
        "subjectId": "soc-indecent-rep",
        "title": "Section 2 Definitions: Indecent Representation of Women, Advertisement, Distribution & Package",
        "order": 2,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 18
    },
    {
        "id": "top-irwa-01-03",
        "chapterId": "ch-soc-irwa-01",
        "subjectId": "soc-indecent-rep",
        "title": "Section 3: Absolute Prohibition on Advertisements Containing Indecent Representation of Women",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 16
    },
    {
        "id": "top-irwa-02-01",
        "chapterId": "ch-soc-irwa-02",
        "subjectId": "soc-indecent-rep",
        "title": "Section 4: Prohibition on Publication, Sale, Hire, Distribution or Circulation of Indecent Material",
        "order": 1,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 19
    },
    {
        "id": "top-irwa-02-02",
        "chapterId": "ch-soc-irwa-02",
        "subjectId": "soc-indecent-rep",
        "title": "Statutory Exceptions: Scientific, Art, Literature, Religious Purposes & Ancient Monuments (S. 4 Proviso)",
        "order": 2,
        "mcqsCount": 5,
        "pyqsCount": 1,
        "estimatedMinutes": 19
    },
    {
        "id": "top-irwa-02-03",
        "chapterId": "ch-soc-irwa-02",
        "subjectId": "soc-indecent-rep",
        "title": "Digital Convergence: Application of IRWA to Electronic Media & Interplay with IT Act 2000 (S. 67)",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 17
    },
    {
        "id": "top-irwa-03-01",
        "chapterId": "ch-soc-irwa-03",
        "subjectId": "soc-indecent-rep",
        "title": "Section 5: Powers of Entry, Search, Seizure & Examination of Gazetted Officers",
        "order": 1,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 17
    },
    {
        "id": "top-irwa-03-02",
        "chapterId": "ch-soc-irwa-03",
        "subjectId": "soc-indecent-rep",
        "title": "Section 6: Penalties for First & Subsequent Convictions (Imprisonment & Mandatory Fines)",
        "order": 2,
        "mcqsCount": 5,
        "pyqsCount": 1,
        "estimatedMinutes": 17
    },
    {
        "id": "top-irwa-03-03",
        "chapterId": "ch-soc-irwa-03",
        "subjectId": "soc-indecent-rep",
        "title": "Section 7 & 8: Offences by Companies, Cognizability, Bailability & Good Faith Protection",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 16
    },

    # Act 9: Protection of Children from Sexual Offences Act, 2012
    {
        "id": "top-pocso-01-01",
        "chapterId": "ch-soc-pocso-01",
        "subjectId": "soc-pocso",
        "title": "UN Convention on the Rights of the Child (CRC) & Special Protective Paradigm",
        "order": 1,
        "mcqsCount": 5,
        "pyqsCount": 1,
        "estimatedMinutes": 18
    },
    {
        "id": "top-pocso-01-02",
        "chapterId": "ch-soc-pocso-01",
        "subjectId": "soc-pocso",
        "title": "Section 2 Definitions: 'Child' (Strict Age Cutoff under 18 Years) & Gender-Neutral Architecture",
        "order": 2,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 19
    },
    {
        "id": "top-pocso-01-03",
        "chapterId": "ch-soc-pocso-01",
        "subjectId": "soc-pocso",
        "title": "Statutory Interpretation: Primacy of Child Welfare, Strict Liability & Age Determination Standards",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 18
    },
    {
        "id": "top-pocso-02-01",
        "chapterId": "ch-soc-pocso-02",
        "subjectId": "soc-pocso",
        "title": "Penetrative Sexual Assault (S. 3–4) & Aggravated Penetrative Sexual Assault (S. 5–6, 2019 Amendments)",
        "order": 1,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 23
    },
    {
        "id": "top-pocso-02-02",
        "chapterId": "ch-soc-pocso-02",
        "subjectId": "soc-pocso",
        "title": "Sexual Assault (S. 7–8) & Aggravated Sexual Assault (S. 9–10)",
        "order": 2,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 21
    },
    {
        "id": "top-pocso-02-03",
        "chapterId": "ch-soc-pocso-02",
        "subjectId": "soc-pocso",
        "title": "Sexual Harassment (S. 11–12) & Child Pornography / Digital Exploitation (Sections 13–15)",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 21
    },
    {
        "id": "top-pocso-03-01",
        "chapterId": "ch-soc-pocso-03",
        "subjectId": "soc-pocso",
        "title": "Sections 19–21: Mandatory Duty to Report Offences & Penalties for Failure to Report",
        "order": 1,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 20
    },
    {
        "id": "top-pocso-03-02",
        "chapterId": "ch-soc-pocso-03",
        "subjectId": "soc-pocso",
        "title": "Investigation Procedures: Special Juvenile Police Unit (SJPU), Women Officers & Child-Friendly Setting",
        "order": 2,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 20
    },
    {
        "id": "top-pocso-03-03",
        "chapterId": "ch-soc-pocso-03",
        "subjectId": "soc-pocso",
        "title": "Medical Examination of Child (S. 27), Emergency Medical Treatment & Immediate Compensation",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 20
    },
    {
        "id": "top-pocso-04-01",
        "chapterId": "ch-soc-pocso-04",
        "subjectId": "soc-pocso",
        "title": "Designation and Jurisdiction of Special Courts (S. 28) & Recording Evidence within 30 Days (S. 35)",
        "order": 1,
        "mcqsCount": 5,
        "pyqsCount": 1,
        "estimatedMinutes": 22
    },
    {
        "id": "top-pocso-04-02",
        "chapterId": "ch-soc-pocso-04",
        "subjectId": "soc-pocso",
        "title": "Child-Friendly Court Procedures: In-Camera Trial, Video Link & No Direct Confrontation (S. 33–38)",
        "order": 2,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 22
    },
    {
        "id": "top-pocso-04-03",
        "chapterId": "ch-soc-pocso-04",
        "subjectId": "soc-pocso",
        "title": "Statutory Presumptions (S. 29 Presumption of Guilt, S. 30 Culpable Mental State) & S. 42A Overriding Effect",
        "order": 3,
        "mcqsCount": 5,
        "pyqsCount": 0,
        "estimatedMinutes": 21
    }
]

def main():
    print("Generating social-chapters.js...")
    chapters_js = """/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Social Legislation Chapters Metadata Module (Paper I — General Knowledge)
 * Covers 9 Prescribed Social Acts across 28 Chapters.
 */
(function(global) {
  "use strict";

  const DATA = """ + json.dumps(CHAPTERS, indent=2) + """;

  if (typeof module !== "undefined" && module.exports) {
    module.exports = DATA;
  }
  const root = typeof window !== "undefined" ? window : global;
  root.SOCIAL_CHAPTERS = DATA;
})(typeof window !== "undefined" ? window : global);
"""

    with open("assets/learning/data/social/social-chapters.js", "w", encoding="utf-8") as f:
        f.write(chapters_js)
    print(f"Created social-chapters.js ({len(CHAPTERS)} chapters)")

    print("Generating social-topics.js...")
    topics_js = """/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Social Legislation Topics Metadata Module (Paper I — General Knowledge)
 * Covers 9 Prescribed Social Acts across 84 Topics.
 */
(function(global) {
  "use strict";

  const DATA = """ + json.dumps(TOPICS, indent=2) + """;

  if (typeof module !== "undefined" && module.exports) {
    module.exports = DATA;
  }
  const root = typeof window !== "undefined" ? window : global;
  root.SOCIAL_TOPICS = DATA;
})(typeof window !== "undefined" ? window : global);
"""

    with open("assets/learning/data/social/social-topics.js", "w", encoding="utf-8") as f:
        f.write(topics_js)
    print(f"Created social-topics.js ({len(TOPICS)} topics)")

    # Assert counts
    assert len(CHAPTERS) == 28, f"Expected 28 chapters, got {len(CHAPTERS)}"
    assert len(TOPICS) == 84, f"Expected 84 topics, got {len(TOPICS)}"
    
    total_mcqs = sum(t["mcqsCount"] for t in TOPICS)
    total_ch_mcqs = sum(c["mcqsCount"] for c in CHAPTERS)
    print(f"Total MCQs mapped: {total_mcqs} (Chapter sum: {total_ch_mcqs})")
    assert total_mcqs == 455, f"Expected 455 MCQs, got {total_mcqs}"
    assert total_ch_mcqs == 455, f"Expected 455 chapter MCQs, got {total_ch_mcqs}"

    total_pyqs = sum(t["pyqsCount"] for t in TOPICS)
    total_ch_pyqs = sum(c["pyqsCount"] for c in CHAPTERS)
    print(f"Total PYQs mapped: {total_pyqs} (Chapter sum: {total_ch_pyqs})")
    assert total_pyqs == 23, f"Expected 23 PYQs, got {total_pyqs}"
    assert total_ch_pyqs == 23, f"Expected 23 chapter PYQs, got {total_ch_pyqs}"
    print("SUCCESS: Chapters and Topics verified perfectly!")

if __name__ == "__main__":
    main()
