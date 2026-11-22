/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Social Legislation Chapters Metadata Module (Paper I — General Knowledge)
 * Covers 9 Prescribed Social Acts across 28 Chapters.
 */
(function(global) {
  "use strict";

  const DATA = [
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
];

  if (typeof module !== "undefined" && module.exports) {
    module.exports = DATA;
  }
  const root = typeof window !== "undefined" ? window : global;
  root.SOCIAL_CHAPTERS = DATA;
})(typeof window !== "undefined" ? window : global);
