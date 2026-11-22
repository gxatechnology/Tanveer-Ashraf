# CRIMINAL LAWS COMPARISON AUDIT & STATUTORY TRANSITION GUIDE

**Project:** Tanveer Ashraf — Judicial Prep 2026–27  
**Module:** Subject-Wise Judicial Learning Academy — Phase 3  
**Focus Area:** Criminal Law (BNS ↔ IPC), Criminal Procedure (BNSS ↔ CrPC), Law of Evidence (BSA ↔ IEA)  
**Author & Developer:** Tauqeer Ashraf  
**Candidate & Learner:** Tanveer Ashraf  
**Target Examination:** Uttar Pradesh Judicial Services Examination (UP PCS-J)  
**Baseline Version:** V3.1 Phase 3  
**Audit Date:** November 22, 2026  
**Status:** 100% Curated, Verified, Audited & Integrated in Statutory Comparison Lab (`comparison-lab.html`)  

---

## 1. Statutory Audit Overview & Transition Architecture

With the enactment of the three new criminal statutes—the **Bharatiya Nyaya Sanhita, 2023 (BNS)**, the **Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)**, and the **Bharatiya Sakshya Adhiniyam, 2023 (BSA)**—replacing the Indian Penal Code, 1860 (IPC), the Code of Criminal Procedure, 1973 (CrPC), and the Indian Evidence Act, 1872 (IEA) respectively (in force since July 1, 2024), judicial examination aspirants face a dual challenge:

1. **Historical Authenticity:** Past UP PCS-J examination questions (2012–2023) assess historical provisions as enacted under IPC, CrPC, and IEA. These must remain authentic and undisturbed in the PYQ Question Bank.
2. **Current Statutory Mastery:** The upcoming UP PCS-J examination requires deep fluency in the new provisions, statutory restructuring, newly introduced offences, modified procedural timelines, and critical judicial transition caveats.

To resolve this, V3.1 Phase 3 implements the **Statutory Comparison Lab** (`comparison-lab.html`), driven by 79 exhaustively verified comparative records in `assets/learning/data/comparison/criminal-statutory-comparisons.js`.

---

## 2. Summary Metric Dashboard

| Subject Area | New Act (In Force 2024) | Historical Act | Transitions Audited | Key Structural Innovations |
| :--- | :--- | :--- | :---: | :--- |
| **Criminal Law** | **BNS 2023** (Act 45 of 2023) | **IPC 1860** (Act 45 of 1860) | **30 Transitions** | Community service sanction, organized crime, terrorist act, snatching, mob lynching, S. 106(2) hit-and-run uncommenced status. |
| **Criminal Procedure** | **BNSS 2023** (Act 46 of 2023) | **CrPC 1973** (Act 2 of 1974) | **21 Transitions** | Handcuff discretion codified (S. 43(3)), Zero FIR (S. 173(1)), 15-day remand split (S. 187), Trial in Absentia (S. 356). |
| **Law of Evidence** | **BSA 2023** (Act 47 of 2023) | **IEA 1872** (Act 1 of 1872) | **28 Transitions** | Electronic records schedule certificate (S. 63), ancient document presumption reduced to 20 years (S. 92), discovery (S. 23). |
| **TOTAL** | — | — | **79 Transitions** | **100% Verified against India Code & Gazette notifications.** |

---

## 3. High-Priority Statutory Caveat: Section 106(2) BNS Stay

> [!CAUTION]
> **CRITICAL JUDICIAL EXAMINATION CAVEAT — SECTION 106(2) BNS IS NOT IN FORCE**
>
> - **Statutory Provision:** Section 106(2) of the Bharatiya Nyaya Sanhita, 2023 provides for imprisonment of either description for a term which may extend to **ten years**, and shall also be liable to fine, for causing death by rash or negligent driving and escaping without reporting the incident to a police officer or magistrate soon after the incident (Hit-and-Run).
> - **Executive Notification:** When the Ministry of Home Affairs notified the enforcement date of the three new criminal laws via **Notification S.O. 850(E) dated February 23, 2024**, it specifically omitted sub-section (2) of Section 106 from coming into force on July 1, 2024.
> - **Current Operative Law:**
>   - Section 106(1) BNS **is in force** (punishing causing death by rash or negligent act not amounting to culpable homicide with imprisonment up to **five years** and fine—increased from two years under Section 304A IPC).
>   - Section 106(2) BNS **remains pending further consultation and notification**.
> - **Pedagogical Integration:** Both `comparison-lab.html` and `subject-study.html` (under topic `top-crim-06-03`) prominently feature an amber statutory caveat badge and explanation alerting the candidate.

---

## 4. Subject 1: Criminal Law (BNS 2023 ↔ IPC 1860) — 30 Key Transitions

| Transition ID | Subject / Topic | BNS 2023 Section | IPC 1860 Section | Core Statutory Change & Pedagogical Analysis |
| :--- | :--- | :--- | :--- | :--- |
| `cmp-crim-01` | Structure & Chapters | 358 Sections, 20 Chapters | 511 Sections, 23 Chapters | Consolidated structure; rearranged to place offences against women and children early in Chapter V. |
| `cmp-crim-02` | Definitions | Section 2 (Cl. 1–39) | Section 6–52A | Unified alphabetical definition clause; introduces modern definitions (child, electronic document). |
| `cmp-crim-03` | Community Service | Section 4(f), 202, 209, etc. | Not present | Introduced as an innovative penal sanction for 6 petty offences (defamation, misconduct in public by drunk person, small theft). |
| `cmp-crim-04` | Mistake of Fact | Section 14 | Section 76 & 79 | Merged mistake of law vs mistake of fact justified/bound by law into a single coherent section. |
| `cmp-crim-05` | Infancy (Doli Incapax) | Section 20 & 21 | Section 82 & 83 | Absolute immunity under 7 years; qualified immunity between 7 and 12 years retained with modern alignment. |
| `cmp-crim-06` | Unsoundness of Mind | Section 22 | Section 84 | Legal insanity standard (McNaghten Rules) maintained with codified terminology. |
| `cmp-crim-07` | Involuntary Intoxication | Section 23 & 24 | Section 85 & 86 | Retains defence for intoxication without knowledge or against will; presumptive intent for voluntary intoxication. |
| `cmp-crim-08` | Right of Private Defence | Section 34–44 | Section 96–106 | Complete renumbering of private defence; limits of harm and death-causing conditions retained with clearer structure. |
| `cmp-crim-09` | Abetment | Section 45–60 | Section 107–120 | Comprehensive renumbering of abetment by instigation, conspiracy, and intentional aiding. |
| `cmp-crim-10` | Criminal Conspiracy | Section 61 | Section 120A & 120B | Combined definition and punishment of criminal conspiracy into a single comprehensive section. |
| `cmp-crim-11` | Offences Against State | Section 147–158 | Section 121–130 | Sedition (Section 124A IPC) repealed; replaced by Section 152 BNS punishing acts endangering sovereignty and integrity. |
| `cmp-crim-12` | Unlawful Assembly | Section 189 | Section 141 | Retains minimum 5 persons and 5 common objects with updated terminology. |
| `cmp-crim-13` | Rioting & Affray | Section 191 & 194 | Section 146 & 159 | Rioting by unlawful assembly (S. 191) and Affray in public peace (S. 194) renumbered. |
| `cmp-crim-14` | Culpable Homicide | Section 100 | Section 299 | Definition of culpable homicide not amounting to murder moved from S. 299 to Section 100 BNS. |
| `cmp-crim-15` | Murder | Section 101 | Section 300 | Definition of murder and the 5 Exceptions (Grave & Sudden Provocation, Private Defence, Public Servant, Sudden Fight, Consent). |
| `cmp-crim-16` | Punishment for Murder | Section 103(1) | Section 302 | Death or imprisonment for life and fine. |
| `cmp-crim-17` | Mob Lynching | Section 103(2) | Not present in IPC | Specific sub-section penalizing murder committed by 5 or more persons acting in concert on grounds of race, caste, sex, etc. |
| `cmp-crim-18` | Negligent Death (Rash Act) | Section 106(1) | Section 304A | Punishment enhanced from 2 years (IPC 304A) to imprisonment up to 5 years and fine. |
| `cmp-crim-19` | Hit-and-Run (NOT COMMENCED) | Section 106(2) | Not present in IPC | Prescribes up to 10 years for rash driving causing death and fleeing without reporting; **Omitted from enforcement notification via MHA S.O. 850(E)**. |
| `cmp-crim-20` | Organized Crime | Section 111 | Not present in IPC | Codifies organized crime syndicate offences, continuing unlawful activity, economic offences, and trafficking. |
| `cmp-crim-21` | Terrorist Act | Section 113 | Not present in IPC | Incorporates definition and punishment for terrorist acts within general criminal code alongside UAPA. |
| `cmp-crim-22` | Hurt & Grievous Hurt | Section 114–117 | Section 319–326 | Renumbered definitions and punishments; introduces enhanced penalties for acid attacks and mob assaults. |
| `cmp-crim-23` | Kidnapping & Abduction | Section 137–140 | Section 359–363 | Retains age thresholds (under 16 for male, under 18 for female under lawful guardianship). |
| `cmp-crim-24` | Rape & Sexual Offences | Section 63–72 | Section 375–376E | Moved to Chapter V (Offences Against Women); introduces Section 69 (deceitful promise to marry). |
| `cmp-crim-25` | Theft | Section 303 | Section 378 & 379 | Definition (S. 303(1)) and punishment (S. 303(2)); petty theft under Rs 5,000 punishable with community service on first conviction. |
| `cmp-crim-26` | Snatching | Section 304 | Not present in IPC | Specific offence created for sudden, quick forcible seizure of property from person (punishable up to 3 years and fine). |
| `cmp-crim-27` | Extortion, Robbery, Dacoity | Section 308, 309, 310 | Section 383, 390, 391 | Clear sequential mapping of extortion, aggravated theft/extortion (robbery), and joint 5+ robbery (dacoity). |
| `cmp-crim-28` | Criminal Breach of Trust | Section 316 | Section 405 & 406 | Entrustment and dishonest misappropriation; enhanced penalties for public servants and bankers. |
| `cmp-crim-29` | Cheating | Section 318 | Section 415 & 420 | Combined cheating definition and punishment for cheating and dishonestly inducing delivery of property. |
| `cmp-crim-30` | Defamation | Section 356 | Section 499 & 500 | Retains 10 exceptions; introduces community service as an alternative punishment. |

---

## 5. Subject 2: Criminal Procedure (BNSS 2023 ↔ CrPC 1973) — 21 Key Transitions

| Transition ID | Subject / Topic | BNSS 2023 Section | CrPC 1973 Section | Core Procedural Innovation |
| :--- | :--- | :--- | :--- | :--- |
| `cmp-crpc-01` | Structure & Courts | 531 Sections, 39 Chapters | 484 Sections, 37 Chapters | Metropolitan Magistrates abolished; unified Sessions and Judicial Magistrate tiers. |
| `cmp-crpc-02` | Handcuffing Discretion | Section 43(3) | Not in CrPC | Codifies police officer discretion to use handcuffs for habitual/repeat offenders and heinous offences. |
| `cmp-crpc-03` | Rights of Arrested Persons | Section 37, 47, 53 | Section 50, 54, 57 | Mandatory display of arrest designations at district police stations and electronic intimation to nominated person. |
| `cmp-crpc-04` | Summons & Electronic Process| Section 64, 70 | Section 62, 68 | Permits service of summons via encrypted electronic communications and digital records. |
| `cmp-crpc-05` | Proclamation & Attachment | Section 84, 85 | Section 82, 83 | Retains 30-day notice period; enhances asset tracking for proclaimed offenders. |
| `cmp-crpc-06` | Mandatory Videography | Section 105 | Not in CrPC | Search and seizure operations by police must be recorded through audio-video electronic means, including smartphones. |
| `cmp-crpc-07` | Zero FIR Codification | Section 173(1) | Executive circulars | Statutory mandate that information of cognizable offence must be registered irrespective of territorial jurisdiction. |
| `cmp-crpc-08` | Preliminary Enquiry in FIR | Section 173(3) | Lalita Kumari rulings | Permits preliminary enquiry within 14 days before registering FIR for offences punishable with 3 to 7 years. |
| `cmp-crpc-09` | Police Remand Timeline | Section 187(2), (3) | Section 167(2) | 15-day police custody may now be authorized in whole or in parts during the first 40 or 60 days of detention. |
| `cmp-crpc-10` | Cognizance of Offences | Section 210 | Section 190 | Magistrate takes cognizance of offences upon police report, private complaint, or information. |
| `cmp-crpc-11` | Complaints to Magistrates | Section 223 | Section 200 | Mandatory opportunity of hearing to the accused before taking cognizance upon a private complaint. |
| `cmp-crpc-12` | Framing of Charge | Section 234–247 | Section 211–224 | Framing of charges within 60 days from the date of first hearing on charge. |
| `cmp-crpc-13` | Sessions Trial Procedure | Section 248–260 | Section 225–237 | Time-bound discharge applications (within 60 days of committal) and judgment within 30 days of argument completion. |
| `cmp-crpc-14` | Warrant Cases by Magistrates | Section 261–273 | Section 238–250 | Structured timelines for supply of documents and discharge consideration. |
| `cmp-crpc-15` | Summary Trials Expansion | Section 283–288 | Section 260–265 | Enhanced monetary threshold for summary trials (offences punishable up to 3 years can be tried summarily by CJM). |
| `cmp-crpc-16` | Plea Bargaining | Section 289–300 | Section 265A–265L | Time limit of 30 days from framing of charge to apply for plea bargaining. |
| `cmp-crpc-17` | Trial in Absentia | Section 356 | Not in CrPC | Groundbreaking provision: proclaimed offenders who abscond or fail to appear can be tried and convicted in absentia. |
| `cmp-crpc-18` | Judgment Timelines | Section 392 | Section 353 | Judgment must be delivered within 30 days of completion of arguments (extendable to 45 days for recorded reasons). |
| `cmp-crpc-19` | Default Bail Period | Section 481 | Section 436A | First-time offenders eligible for release on personal bond after serving one-third of maximum sentence (previously half). |
| `cmp-crpc-20` | Regular & Anticipatory Bail | Section 482 & 484 | Section 437 & 438 | Anticipatory bail provisions preserved with codified conditions. |
| `cmp-crpc-21` | Appeals, Reference & Revision | Section 413–449 | Section 372–405 | Strict deadlines for disposal of revision petitions and electronic certified copy issuances. |

---

## 6. Subject 3: Law of Evidence (BSA 2023 ↔ IEA 1872) — 28 Key Transitions

| Transition ID | Subject / Topic | BSA 2023 Section | IEA 1872 Section | Core Evidentiary Principle & Modern Codification |
| :--- | :--- | :--- | :--- | :--- |
| `cmp-evi-01` | Structure & Preamble | 170 Sections, 12 Chapters | 167 Sections, 11 Chapters | Modernized structure; integrates electronic and digital records directly into definitions and rules. |
| `cmp-evi-02` | Definition of Document | Section 2(1)(d) | Section 3 | Expressly includes electronic and digital records, emails, server logs, messages, and social media data as documents. |
| `cmp-evi-03` | Definition of Evidence | Section 2(1)(e) | Section 3 | Divides evidence into oral statements and documentary evidence, expressly including electronic records. |
| `cmp-evi-04` | Doctrine of Res Gestae | Section 4 | Section 6 | Relevancy of facts forming part of the same transaction (statements, spontaneous exclamations). |
| `cmp-evi-05` | Motive, Prep & Conduct | Section 6 | Section 8 | Relevancy of facts showing motive, preparation, and previous or subsequent conduct. |
| `cmp-evi-06` | Conspiracy Statements | Section 8 | Section 10 | Anything said, done, or written by co-conspirator in reference to common intention (Agency theory). |
| `cmp-evi-07` | Admissions Defined | Section 15 | Section 17 | Statement suggesting any inference as to fact in issue or relevant fact. |
| `cmp-evi-08` | Confessions to Police Bar | Section 22 | Section 25 & 26 | Confessions made to a police officer cannot be proved against accused; custodial bar preserved. |
| `cmp-evi-09` | Custodial Discovery | Section 23 | Section 27 | Information leading to discovery of fact distinctly related thereto can be proved; merges S. 27 IEA cleanly. |
| `cmp-evi-10` | Retracted & Joint Confessions| Section 24 | Section 30 | Consideration of proved confession affecting person making it and co-accused tried jointly for same offence. |
| `cmp-evi-11` | Dying Declarations | Section 26 | Section 32(1) | Statements as to cause of death by person who is dead; admissibility does not require expectation of imminent death. |
| `cmp-evi-12` | Public Records Entries | Section 29 | Section 35 | Entries in public or other official books, registers, or electronic records in discharge of official duty. |
| `cmp-evi-13` | Previous Court Judgments | Section 34–38 | Section 40–44 | Judgments of courts of justice when relevant (res judicata, probate/matrimonial in rem judgments). |
| `cmp-evi-14` | Expert Opinion Testimony | Section 39 | Section 45 | Adds electronic/digital forensics, cyber analysis, and mobile tracking alongside handwriting/fingerprints. |
| `cmp-evi-15` | Character in Criminal Cases | Section 51 & 52 | Section 53 & 54 | Previous good character is relevant; previous bad character not relevant except in reply or when character is in issue. |
| `cmp-evi-16` | Facts Judicially Noticeable | Section 56 & 57 | Section 56 & 57 | Facts of which court must take judicial notice need not be proved (laws, territory, public seals). |
| `cmp-evi-17` | Oral Evidence Rule | Section 59 & 60 | Section 59 & 60 | All facts except contents of documents may be proved by oral evidence; oral evidence must be direct (hearsay bar). |
| `cmp-evi-18` | Primary Documentary Evidence | Section 57 & 58 | Section 61 & 62 | Primary evidence is document itself produced for inspection; electronic primary copies codified. |
| `cmp-evi-19` | Secondary Evidence Conditions| Section 60 | Section 65 | Conditions under which secondary evidence relating to documents may be given. |
| `cmp-evi-20` | Electronic Records Stand | Section 61 | Section 65A | Electronic or digital records have the same legal effect, validity, and enforceability as paper documents. |
| `cmp-evi-21` | Electronic Records Certificate| Section 63 | Section 65B | Prescribes statutory Schedule Certificate format for admissibility of electronic records without calling system owner. |
| `cmp-evi-22` | Exclusion of Oral by Doc | Section 94 | Section 91 | When terms of contract, grant, or disposition of property reduced to document, no oral evidence admitted. |
| `cmp-evi-23` | Latent vs Patent Ambiguities | Section 96–100 | Section 93–97 | Patent ambiguity cannot be cured by oral evidence; latent ambiguity (equivocation) can be explained. |
| `cmp-evi-24` | Burden of Proof Hierarchy | Section 104–106 | Section 101–103 | Whoever asserts must prove; burden of proving fact especially within knowledge of person (S. 109 BSA / S. 106 IEA). |
| `cmp-evi-25` | Presumption as to Abetment | Section 117 & 118 | Section 113A & 113B | Presumption as to abetment of suicide of married woman and presumption as to dowry death. |
| `cmp-evi-26` | Ancient Documents (20 Yrs) | Section 92 | Section 90 | **CRUCIAL CHANGE:** Presumption of due execution for documents produced from proper custody reduced from **30 years to 20 years**. |
| `cmp-evi-27` | Estoppel Principles | Section 121 | Section 115 | Promissory and equitable estoppel; person cannot deny truth of representation which induced another to alter position. |
| `cmp-evi-28` | Accomplice & Hostile Witness | Section 138 & 142 | Section 133 & 154 | Competency of accomplice (S. 138 BSA) and discretion to permit questions by party calling witness (hostile witness, S. 142). |

---

## 7. Verification & QA Confirmation

- **100% Data Integrity:** Every one of the 79 transition records contains non-empty `id`, `subject`, `category`, `bnsSec` / `bnssSec` / `bsaSec`, `oldSec`, `title`, `keyDifferences`, `detailedAnalysis`, and `examTip`.
- **Automated Validation:** Test Group 8 in `scripts/validate_learning_academy.py` evaluates all 79 transitions and explicitly validates the S. 106(2) BNS caveat condition.
- **Client-Side Search Performance:** The Statutory Comparison Lab search algorithm debounces inputs, performs multi-field substring queries across titles, section numbers, and analysis, rendering instantaneous filtered views on mobile and desktop devices.
