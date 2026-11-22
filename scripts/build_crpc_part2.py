"""
Builder for CrPC Concepts Part 2 (Chapters 5 to 8: 10 Topics)
Output: assets/learning/data/crpc/crpc-concepts-part2.js
"""

import json

CONCEPTS = {
    # -------------------------------------------------------------------------
    # CHAPTER 5: MAINTENANCE OF WIVES, CHILDREN & PARENTS
    # -------------------------------------------------------------------------
    "top-crpc-05-01": {
        "topicId": "top-crpc-05-01",
        "chapterId": "ch-crpc-05",
        "subjectId": "law-crpc",
        "title": "Maintenance of Wives, Children & Parents: S. 125 CrPC / S. 144 BNSS",
        "subtitle": "Section 144 BNSS vs Section 125 CrPC & 60-Day Interim Maintenance Mandate",
        "learningObjective": "Master the secular statutory remedy of maintenance under Section 144 BNSS / Section 125 CrPC, eligible claimants, neglect or refusal standard, and the mandatory 60-day disposal of interim maintenance applications.",
        "introduction": "Section 125 CrPC (now Section 144 BNSS) is a social justice measure designed to prevent vagrancy and destitution. It is completely secular, applying across all religious communities irrespective of personal laws. BNSS 2023 sharpens this protection by imposing a strict 60-day disposal deadline for interim maintenance applications.",
        "detailedExplanation": """
<h3>1. Persons Entitled to Claim Maintenance (Section 144(1) BNSS / Section 125(1) CrPC)</h3>
<p>If any person having sufficient means neglects or refuses to maintain:</p>
<ol>
  <li><strong>Wife:</strong> Unable to maintain herself. 'Wife' includes a woman who has been <strong>divorced by, or has obtained a divorce from, her husband and has not remarried</strong>.</li>
  <li><strong>Children:</strong> Legitimate or illegitimate minor child, whether married or not, unable to maintain itself (if married minor daughter, father must maintain until she attains majority if husband has insufficient means).</li>
  <li><strong>Disabled Adult Children:</strong> Legitimate or illegitimate child (not being a married daughter) who has attained majority, where such child is by reason of physical or mental abnormality or injury unable to maintain itself.</li>
  <li><strong>Parents:</strong> Father or mother, unable to maintain himself or herself.</li>
</ol>

<h3>2. Essential Ingredients for Award of Maintenance</h3>
<ul>
  <li>Respondent must have <strong>sufficient means</strong> (earning capacity or property);</li>
  <li>Respondent must have <strong>neglected or refused</strong> to maintain the claimant;</li>
  <li>Claimant must be <strong>unable to maintain herself / himself</strong>.</li>
</ul>

<h3>3. Interim Maintenance & 60-Day Disposal Proviso (BNSS S. 144(2) Proviso)</h3>
<p>During the pendency of the proceeding, the Magistrate may order monthly interim maintenance and expenses of proceeding. BNSS 2023 expressly mandates: an application for interim maintenance and expenses <strong>shall, as far as possible, be disposed of within sixty (60) days</strong> from the date of the service of notice of the application to such person.</p>

<h3>4. Disqualifications for Wife (Section 144(4) BNSS / Section 125(4) CrPC)</h3>
<p>No wife shall be entitled to receive maintenance if:</p>
<ol>
  <li>She is <strong>living in adultery</strong>; OR</li>
  <li>Without any sufficient reason, she <strong>refuses to live with her husband</strong>; OR</li>
  <li>The parties are <strong>living separately by mutual consent</strong>.</li>
</ol>
""",
        "keyProvisions": [
            {"section": "Section 144, BNSS 2023 (S. 125 CrPC)", "title": "Order for maintenance of wives, children and parents", "content": "Secular maintenance order; includes divorced wife; 60-day interim maintenance timeline."},
            {"section": "Section 144(4), BNSS 2023 (S. 125(4) CrPC)", "title": "Grounds disentitling wife from maintenance", "content": "Living in adultery, refusing to cohabit without sufficient reason, or living separately by mutual consent."}
        ],
        "landmarkCases": [
            {"caseName": "Mohd. Ahmed Khan v. Shah Bano Begum", "citation": "(1985) 2 SCC 556", "bench": "Five-Judge Constitution Bench (Chandrachud C.J.)", "principle": "Section 125 CrPC is a secular provision that cuts across the barriers of religion and personal law; a divorced Muslim wife is entitled to maintenance until remarriage."},
            {"caseName": "Rajnesh v. Neha", "citation": "(2021) 2 SCC 324", "bench": "Supreme Court of India (Indu Malhotra J.)", "principle": "Laid down comprehensive guidelines for payment of maintenance across all statutes, mandatory filing of Assets and Liabilities Affidavits, and payment from the date of filing of application."}
        ],
        "comparativeTable": [
            {
                "title": "Maintenance Law: CrPC 1973 vs BNSS 2023",
                "headers": ["Aspect", "CrPC 1973 Section 125", "BNSS 2023 Section 144"],
                "rows": [
                    ["Section Number", "Section 125 CrPC", "Section 144 BNSS"],
                    ["Pecuniary Cap", "No cap (removed in 2001)", "No cap (Magistrate's reasonable discretion)"],
                    ["Interim Maintenance Disposal", "As far as possible in 60 days (2001 amendment)", "Expressly reaffirmed within 60 days from notice service"],
                    ["Divorced Wife Protection", "Included until remarriage", "Included until remarriage (Unaltered)"]
                ]
            }
        ],
        "diagramId": "diag-crpc-maintenance-s144",
        "diagramExplanation": "Shows claimant categories, essential ingredients, 60-day interim timeline, and statutory disqualifications.",
        "prelimTraps": [
            {
                "trap": "Believing a father is not liable to maintain an illegitimate minor child under Section 144 BNSS / Section 125 CrPC.",
                "reality": "Section 144(1)(b) BNSS / S. 125(1)(b) CrPC explicitly covers 'legitimate or ILLEGITIMATE minor child'. Paternity, not matrimonial legitimacy, governs maintenance.",
                "rule": "Father is legally bound to maintain illegitimate minor children."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crpc-05-01",
                "front": "Within how many days should an interim maintenance application be disposed of under Section 144(2) BNSS / S. 125 CrPC?",
                "back": "Within sixty (60) days from the date of the service of notice of the application.",
                "category": "Maintenance Timelines"
            },
            {
                "id": "fc-crpc-05-02",
                "front": "Does 'wife' under Section 144 BNSS / Section 125 CrPC include a divorced wife?",
                "back": "Yes, provided she has not remarried (Section 144(1) Explanation (b)).",
                "category": "Maintenance Scope"
            }
        ],
        "sourceReferences": [{"title": "Sections 144–147, Bharatiya Nagarik Suraksha Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-crpc-05-02": {
        "topicId": "top-crpc-05-02",
        "chapterId": "ch-crpc-05",
        "subjectId": "law-crpc",
        "title": "Procedure, Alteration & Enforcement of Maintenance Orders",
        "subtitle": "BNSS Sections 145–147 vs CrPC Sections 126–128 & Limitation for Arrears Enforcement",
        "learningObjective": "Master territorial jurisdiction under Section 145 BNSS / S. 126 CrPC, ex-parte procedures, alteration of allowance on change in circumstances (Section 146 BNSS / S. 127 CrPC), and the 1-year limitation for recovery warrants.",
        "introduction": "An order of maintenance is worthless without effective enforcement machinery. The Code establishes flexible territorial jurisdiction to protect claimants, provides summary recovery through warrants as for levying fines, and sets a strict 1-year limitation period for recovering accumulated arrears.",
        "detailedExplanation": """
<h3>1. Venue & Procedure (Section 145 BNSS / Section 126 CrPC)</h3>
<p>Proceedings under Section 144 BNSS may be taken against any person in any district where:</p>
<ol>
  <li>He is residing; OR</li>
  <li>He or his wife resides; OR</li>
  <li>He last resided with his wife, or as the case may be, with the mother of the illegitimate child.</li>
</ol>
<p><strong>Ex-Parte Order:</strong> If the Magistrate is satisfied that the person is willfully avoiding service or willfully neglecting to attend, the Magistrate may proceed to hear and determine the case ex parte. Such order may be set aside on good cause shown within <strong>three (3) months</strong> from the date thereof.</p>

<h3>2. Alteration in Allowance (Section 146 BNSS / Section 127 CrPC)</h3>
<p>On proof of a <strong>change in the circumstances</strong> of the person receiving or paying the monthly allowance, the Magistrate may make such alteration in the allowance as thought fit. The Magistrate shall cancel or vary the order if:</p>
<ul>
  <li>The woman has remarried (order cancelled from date of remarriage);</li>
  <li>The woman has received the whole sum due under customary or personal law upon divorce;</li>
  <li>The woman has voluntarily surrendered her rights after divorce.</li>
</ul>

<h3>3. Enforcement & 1-Year Limitation (Section 147 BNSS / Section 128 CrPC & S. 144(3))</h3>
<p>If any person so ordered fails without sufficient cause to comply with the order, the Magistrate may, for every breach, issue a warrant for levying the amount due in the manner provided for levying fines, and may sentence such person to <strong>imprisonment for a term which may extend to one month</strong> or until payment if sooner made.</p>
<p><strong>Crucial Limitation Bar:</strong> No warrant shall be issued for the recovery of any amount due unless application be made to the Court to levy such amount within a period of <strong>one (1) year</strong> from the date on which it became due!</p>
""",
        "keyProvisions": [
            {"section": "Section 145, BNSS 2023 (S. 126 CrPC)", "title": "Procedure", "content": "Jurisdiction where husband/wife resides; ex-parte set-aside within 3 months."},
            {"section": "Section 146, BNSS 2023 (S. 127 CrPC)", "title": "Alteration in allowance", "content": "Variation on change in circumstances, remarriage, or customary divorce settlement."},
            {"section": "Section 144(3), BNSS 2023 (S. 125(3) CrPC)", "title": "Enforcement of order and limitation", "content": "Warrant as fine; imprisonment up to 1 month per default; 1-year limitation for arrears."}
        ],
        "landmarkCases": [
            {"caseName": "Shantha v. B.G. Shivananjappa", "citation": "(2005) 4 SCC 468", "bench": "Supreme Court of India", "principle": "The liability to pay maintenance is a continuing one; the magistrate has power to impose imprisonment for each month's default."},
            {"caseName": "Poongodi v. Thangavel", "citation": "(2013) 10 SCC 618", "bench": "Supreme Court of India", "principle": "The proviso to Section 125(3) restricting recovery to one year does not extinguish the claimant's entitlement to arrears; subsequent applications can be made for distinct default periods."}
        ],
        "comparativeTable": [
            {
                "title": "Maintenance Enforcement Timeframes",
                "headers": ["Procedural Action", "Statutory Time Limit", "Section in BNSS", "Section in CrPC"],
                "rows": [
                    ["Setting aside ex-parte order", "Within 3 months of order date", "Section 145(2) Proviso", "Section 126(2) Proviso"],
                    ["Filing application for arrears warrant", "Within 1 year from due date", "Section 144(3) Proviso", "Section 125(3) Proviso"],
                    ["Default imprisonment term", "Up to 1 month for each breach", "Section 144(3)", "Section 125(3)"],
                    ["Cancellation on remarriage", "Effective from remarriage date", "Section 146(3)", "Section 127(3)"]
                ]
            }
        ],
        "diagramId": "diag-crpc-maintenance-s144",
        "diagramExplanation": "Shows maintenance enforcement routes, warrant mechanisms, and statutory limitation bars.",
        "prelimTraps": [
            {
                "trap": "Believing a wife can file an application to recover 5 years of accumulated maintenance arrears at once.",
                "reality": "Under Section 144(3) BNSS / Section 125(3) CrPC proviso, no warrant can be issued for any amount unless application is made within ONE YEAR from the date it became due.",
                "rule": "1-year limitation strictly bars recovery warrants for older arrears."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crpc-05-03",
                "front": "What is the maximum term of imprisonment a Magistrate can impose for each default of maintenance under S. 144(3) BNSS / S. 125(3) CrPC?",
                "back": "Imprisonment extending up to one (1) month, or until payment if sooner made.",
                "category": "Maintenance Enforcement"
            },
            {
                "id": "fc-crpc-05-04",
                "front": "Within what period must an application for recovery of maintenance arrears be made?",
                "back": "Within one (1) year from the date on which the amount became due.",
                "category": "Maintenance Limitation"
            }
        ],
        "sourceReferences": [{"title": "Sections 144(3), 145–147, Bharatiya Nagarik Suraksha Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    # -------------------------------------------------------------------------
    # CHAPTER 6: INFORMATION TO POLICE & POWERS TO INVESTIGATE
    # -------------------------------------------------------------------------
    "top-crpc-06-01": {
        "topicId": "top-crpc-06-01",
        "chapterId": "ch-crpc-06",
        "subjectId": "law-crpc",
        "title": "First Information Report: S. 173 BNSS / S. 154 CrPC & Zero FIR",
        "subtitle": "Section 173 BNSS vs Section 154 CrPC, Statutory Zero FIR & Preliminary Inquiry Rules",
        "learningObjective": "Master the mandatory registration of FIR under Section 173 BNSS / Section 154 CrPC (Lalita Kumari), the groundbreaking statutory codification of 'Zero FIR', e-FIR formalities, and the 14-day preliminary inquiry window under BNSS Section 173(3).",
        "introduction": "The First Information Report (FIR) triggers the state's criminal justice machinery. While Section 154 CrPC required judicial interpretation to mandate registration and recognize Zero FIR, BNSS 2023 directly codifies Zero FIR into the text of Section 173 and introduces structured preliminary inquiries for medium-gravity offences.",
        "detailedExplanation": """
<h3>1. Statutory Codification of Zero FIR (Section 173(1) BNSS / Section 154 CrPC)</h3>
<p>Every information relating to the commission of a cognizable offence, if given orally to an officer in charge of a police station, shall be reduced to writing. Section 173(1) BNSS explicitly codifies <strong>Zero FIR</strong>: information must be registered <strong>'irrespective of the area where the offence was committed'</strong>. The police station must register the Zero FIR and immediately transfer it to the police station having territorial jurisdiction.</p>

<h3>2. Electronic FIR (e-FIR) under BNSS Section 173(1)(ii)</h3>
<p>BNSS 2023 permits information to be given through <strong>electronic communication</strong>. Safeguard requirement: the information given electronically shall be taken on record by the police officer only after it is <strong>signed by the person giving it within three (3) days</strong>.</p>

<h3>3. Mandatory Preliminary Inquiry for 3–7 Year Offences (Section 173(3) BNSS)</h3>
<p>For offences punishable with imprisonment of <strong>not less than three years and less than seven years</strong>, the officer in charge of a police station may, with prior permission of an officer not below the rank of <strong>Deputy Superintendent of Police (DSP)</strong>, considering the nature and gravity of the offence:</p>
<ol>
  <li>Proceed to conduct a <strong>preliminary inquiry within fourteen (14) days</strong> to ascertain whether a prima facie case exists; OR</li>
  <li>Proceed with investigation if a prima facie case exists.</li>
</ol>

<h3>4. Lalita Kumari Mandatory Registration Doctrine</h3>
<p>In <em>Lalita Kumari v. Govt. of U.P.</em> (2014), a Constitution Bench held that registration of FIR is <strong>mandatory under Section 154 CrPC</strong> if the information discloses commission of a cognizable offence. Preliminary inquiry was permitted only in 5 exceptional categories (matrimonial, commercial, medical negligence, corruption, cases with abnormal delay).</p>
""",
        "keyProvisions": [
            {"section": "Section 173, BNSS 2023 (S. 154 CrPC)", "title": "Information in cognizable cases", "content": "Mandatory FIR, statutory Zero FIR, electronic FIR with 3-day signature rule, and 14-day preliminary inquiry."},
            {"section": "Section 173(4), BNSS 2023 (S. 154(3) CrPC)", "title": "Remedy on police refusal to register FIR", "content": "Aggrieved person may send substance of information by post to Superintendent of Police (SP)."}
        ],
        "landmarkCases": [
            {"caseName": "Lalita Kumari v. Govt. of U.P.", "citation": "(2014) 2 SCC 1", "bench": "Five-Judge Constitution Bench", "principle": "Registration of FIR is mandatory under Section 154 if information discloses a cognizable offence; police have no discretion to embark on inquiry before registering FIR."},
            {"caseName": "State of Haryana v. Bhajan Lal", "citation": "1992 Supp (1) SCC 335", "bench": "Supreme Court of India", "principle": "Laid down the definitive 7-point test for quashing FIR under Section 482 CrPC / Article 226 when allegations do not disclose any cognizable offence."}
        ],
        "comparativeTable": [
            {
                "title": "FIR Architecture: CrPC 1973 vs BNSS 2023",
                "headers": ["Feature", "CrPC 1973 Section 154", "BNSS 2023 Section 173"],
                "rows": [
                    ["Zero FIR", "Judicial doctrine; not in text", "Statutorily codified in Section 173(1)"],
                    ["Electronic FIR", "Ad-hoc state police portals", "Statutory code: must be signed within 3 days"],
                    ["Preliminary Inquiry", "Judge-made exception (Lalita Kumari)", "Statutory 14-day window for 3–7 yr offences (S. 173(3))"],
                    ["Copy to Informant", "Forthwith, free of cost (S. 154(2))", "Forthwith, free of cost (S. 173(2)) [Unaltered]"]
                ]
            }
        ],
        "diagramId": "diag-crpc-investigation-flowchart",
        "diagramExplanation": "Shows FIR pathways: physical, Zero FIR, e-FIR with 3-day validation, 14-day preliminary inquiry, and full investigation.",
        "prelimTraps": [
            {
                "trap": "Believing an e-FIR becomes operative immediately without any physical signature requirement.",
                "reality": "Under Section 173(1)(ii) BNSS, information given electronically must be signed by the informant within THREE (3) DAYS before it is officially taken on record as an FIR.",
                "rule": "e-FIR requires signature within 3 days to become formal FIR."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crpc-06-01",
                "front": "What is the maximum time for completing a preliminary inquiry under Section 173(3) BNSS 2023?",
                "back": "Fourteen (14) days.",
                "category": "Preliminary Inquiry"
            },
            {
                "id": "fc-crpc-06-02",
                "front": "Within how many days must an electronic information (e-FIR) be signed by the informant under Section 173(1) BNSS?",
                "back": "Within three (3) days.",
                "category": "e-FIR Rules"
            }
        ],
        "sourceReferences": [{"title": "Section 173, Bharatiya Nagarik Suraksha Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-crpc-06-02": {
        "topicId": "top-crpc-06-02",
        "chapterId": "ch-crpc-06",
        "subjectId": "law-crpc",
        "title": "Police Investigation Powers & Examination of Witnesses (S. 161 CrPC)",
        "subtitle": "BNSS Sections 175–182 vs CrPC Sections 156–163 & Witness Attendance Protections",
        "learningObjective": "Master police powers of investigation without magistrate order, magisterial investigation directions under Section 156(3) CrPC / S. 175(3) BNSS, witness examination under Section 161 CrPC / S. 180 BNSS, and the bar on signing statements under Section 162 CrPC / S. 182 BNSS.",
        "introduction": "Police investigation is the statutory collection of evidence through spot inspection, witness interrogation, and seizure. The Code places vital constraints on this power to protect witnesses from harassment and to prevent coerced testimony from polluting the record of trial.",
        "detailedExplanation": """
<h3>1. Power to Investigate Cognizable Offence (Section 175 BNSS / Section 156 CrPC)</h3>
<p>Any officer in charge of a police station may, without the order of a Magistrate, investigate any cognizable case which a court having jurisdiction over the local area would have power to inquire into or try. Under Section 175(3) BNSS / Section 156(3) CrPC, any Magistrate empowered under Section 190 CrPC / S. 210 BNSS may <strong>order such an investigation</strong>.</p>

<h3>2. Witness Attendance & Protected Classes (Section 179 BNSS / Section 160 CrPC)</h3>
<p>A police officer making an investigation may by written order require the attendance of any person appearing to be acquainted with the facts. <strong>Protected Classes Proviso:</strong> No male person under <strong>fifteen (15) years</strong> or above <strong>sixty (60) years</strong> [CrPC said 65 years], no woman, and no mentally or physically disabled person shall be required to attend at any place <strong>other than the place in which such person resides</strong>!</p>

<h3>3. Examination of Witnesses (Section 180 BNSS / Section 161 CrPC)</h3>
<ul>
  <li>Police officer may examine orally any person supposed to be acquainted with facts;</li>
  <li>Such person is bound to answer truly all questions, <strong>other than questions the answers to which would have a tendency to expose him to a criminal charge or to a penalty or forfeiture</strong> (statutory reflection of Article 20(3));</li>
  <li>Police may reduce statements into writing; BNSS Section 180(3) explicitly permits recording by <strong>audio-video electronic means</strong>.</li>
</ul>

<h3>4. Bar on Signing Statements & Limited Use (Section 182 BNSS / Section 162 CrPC)</h3>
<p>No statement made by any person to a police officer in the course of an investigation <strong>shall be signed</strong> by the person making it. Nor shall any such statement be used for any purpose at any inquiry or trial, EXCEPT by the accused (and with court permission by the prosecution) to <strong>contradict such witness</strong> in the manner provided by Section 148 BSA / Section 145 IEA.</p>
""",
        "keyProvisions": [
            {"section": "Section 175, BNSS 2023 (S. 156 CrPC)", "title": "Police officer's power to investigate cognizable case", "content": "Independent investigation power; Magistrate direction under S. 175(3) / 156(3)."},
            {"section": "Section 179, BNSS 2023 (S. 160 CrPC)", "title": "Order for attendance of witnesses", "content": "Exemption from station attendance: male <15 or >=60, women, disabled persons."},
            {"section": "Section 182, BNSS 2023 (S. 162 CrPC)", "title": "Statements to police not to be signed; use in evidence", "content": "Strict bar on signing statements; use restricted to contradiction under Section 145 IEA."}
        ],
        "landmarkCases": [
            {"caseName": "Nandini Satpathy v. P.L. Dani", "citation": "(1978) 2 SCC 424", "bench": "Three-Judge Bench (Krishna Iyer J.)", "principle": "The right against self-incrimination under Article 20(3) and Section 161(2) CrPC applies at the stage of police interrogation; an accused has the right to remain silent to questions that incriminate him."},
            {"caseName": "Tahsildar Singh v. State of U.P.", "citation": "AIR 1959 SC 1012", "bench": "Six-Judge Constitution Bench", "principle": "Section 162 CrPC creates a total ban on the use of police statements except for the strictly limited purpose of contradicting the prosecution witness under Section 145 Evidence Act."}
        ],
        "comparativeTable": [
            {
                "title": "Witness Protection & Statements: CrPC 1973 vs BNSS 2023",
                "headers": ["Rule / Safeguard", "CrPC 1973 Section", "BNSS 2023 Section"],
                "rows": [
                    ["Senior Citizen Age Exemption", "Male above 65 years (S. 160(1))", "Male above 60 years (S. 179(1)) [Expanded]"],
                    ["Audio-Video Recording of S. 161", "Added by 2008 proviso", "Integral to Section 180(3) BNSS"],
                    ["Signing Police Statements", "Strictly prohibited (S. 162(1))", "Strictly prohibited (S. 182(1)) [Unaltered]"],
                    ["Evidentiary Use of Statements", "Only for contradiction (S. 162)", "Only for contradiction (S. 182) [Unaltered]"]
                ]
            }
        ],
        "diagramId": "diag-crpc-investigation-flowchart",
        "diagramExplanation": "Shows witness interrogation process, home examination exemptions, and Section 162 contradiction bar.",
        "prelimTraps": [
            {
                "trap": "Believing a statement given to the police during investigation can be used as substantive evidence to corroborate a witness at trial.",
                "reality": "Under Section 182 BNSS / Section 162 CrPC, police statements CANNOT be used for corroboration; they can ONLY be used to CONTRADICT the witness.",
                "rule": "Police statements under Section 161 / 180 can NEVER be used for corroboration."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crpc-06-03",
                "front": "What age threshold for senior males qualifies for examination at residence under Section 179 BNSS?",
                "back": "Sixty (60) years of age (lowered from 65 years under CrPC).",
                "category": "Witness Protections"
            },
            {
                "id": "fc-crpc-06-04",
                "front": "For what sole purpose can a Section 161 CrPC / Section 180 BNSS statement be used during trial under S. 162 CrPC / S. 182 BNSS?",
                "back": "ONLY to contradict the witness in the manner provided by the Evidence Act; never for corroboration.",
                "category": "Police Statements"
            }
        ],
        "sourceReferences": [{"title": "Sections 175–182, Bharatiya Nagarik Suraksha Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-crpc-06-03": {
        "topicId": "top-crpc-06-03",
        "chapterId": "ch-crpc-06",
        "subjectId": "law-crpc",
        "title": "Recording Confessions & Statements by Magistrate (S. 164 CrPC)",
        "subtitle": "BNSS Section 183 vs CrPC Section 164 & Mandatory Audio-Video Recording",
        "learningObjective": "Master the judicial recording of confessions and witness statements under Section 183 BNSS / Section 164 CrPC, mandatory statutory warnings, reflection time, audio-video electronic recording, and recording of statements in sexual offences.",
        "introduction": "Because confessions made to police officers are inadmissible under evidence law, the Code provides a judicial forum for recording voluntary confessions and witness statements under Section 164 CrPC (now Section 183 BNSS). Strict statutory compliance is required; failure to warn the maker invalidates the confession.",
        "detailedExplanation": """
<h3>1. Competent Magistrate (Section 183(1) BNSS / Section 164(1) CrPC)</h3>
<p>Any <strong>Judicial Magistrate of the First Class or Metropolitan Magistrate</strong> (whether or not they have jurisdiction in the case) may record any confession or statement made to them in the course of an investigation. Executive Magistrates and police officers are strictly barred.</p>

<h3>2. Mandatory Warnings & Reflection Time (Section 183(2) BNSS / Section 164(2) CrPC)</h3>
<p>Before recording a confession, the Magistrate <strong>SHALL explain</strong> to the person making it:</p>
<ol>
  <li>That they are <strong>not bound to make a confession</strong>; AND</li>
  <li>That if they do so, it may be <strong>used as evidence against them</strong>.</li>
</ol>
<p>The Magistrate shall not record any confession unless, upon questioning, they have <strong>reason to believe that it is being made voluntarily</strong>. If the person expresses unwillingness to confess, the Magistrate shall not authorize the detention of such person in <strong>police custody</strong>.</p>

<h3>3. Mandatory Audio-Video Recording: Section 183(1) Proviso</h3>
<p>BNSS 2023 mandates that any confession or statement recorded under Section 183(1) <strong>may also be recorded by audio-video electronic means</strong> in the presence of the advocate of the person accused of an offence.</p>

<h3>4. Statements in Sexual Offences (Section 183(6) BNSS / Section 164(5A) CrPC)</h3>
<p>In cases punishable under sexual offence provisions (Sections 64–71 BNS / Sections 376–376E IPC), the Judicial Magistrate <strong>shall record the statement of the victim as soon as the commission of the offence is brought to the notice of the police</strong>. If the victim is temporarily or permanently mentally or physically disabled, recording shall be assisted by an interpreter or special educator and videographed.</p>
""",
        "keyProvisions": [
            {"section": "Section 183, BNSS 2023 (S. 164 CrPC)", "title": "Recording of confessions and statements", "content": "Magistrate warning of voluntary nature; audio-video recording option; bar on police remand if unwilling."},
            {"section": "Section 183(6), BNSS 2023 (S. 164(5A) CrPC)", "title": "Mandatory recording of victim statement in sexual offences", "content": "Recorded as soon as brought to notice; female magistrate; videography for disabled victims."}
        ],
        "landmarkCases": [
            {"caseName": "Sarwan Singh v. State of Punjab", "citation": "AIR 1957 SC 637", "bench": "Supreme Court of India", "principle": "Magistrate must grant sufficient time for reflection (ordinarily 24 hours) after removing accused from police influence before recording confession."},
            {"caseName": "Shivappa v. State of Karnataka", "citation": "(1995) 2 SCC 76", "bench": "Supreme Court of India", "principle": "Failure to administer the statutory warnings under Section 164(2) goes to the root of the matter and renders the confession completely inadmissible."}
        ],
        "comparativeTable": [
            {
                "title": "Confessions under Section 164 CrPC vs Section 183 BNSS",
                "headers": ["Aspect", "CrPC 1973 Section 164", "BNSS 2023 Section 183"],
                "rows": [
                    ["Section Number", "Section 164 CrPC", "Section 183 BNSS"],
                    ["Audio-Video Recording", "Permitted (2008 amendment)", "Expressly emphasized with advocate presence"],
                    ["Statutory Warnings", "Mandatory before recording", "Mandatory before recording (Unaltered)"],
                    ["Unwilling Accused Remand", "No police custody permitted", "No police custody permitted (Unaltered)"]
                ]
            }
        ],
        "diagramId": "diag-crpc-investigation-flowchart",
        "diagramExplanation": "Shows judicial confession procedure: isolation from police, statutory warning, reflection time, voluntary certification.",
        "prelimTraps": [
            {
                "trap": "Believing an Executive Magistrate can record a judicial confession under Section 183 BNSS / Section 164 CrPC.",
                "reality": "Only a Judicial Magistrate (or in CrPC, Metropolitan Magistrate) can record confessions under Section 164 / 183. Executive Magistrates are completely incompetent.",
                "rule": "Only Judicial Magistrates can record Section 164 / 183 confessions."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crpc-06-05",
                "front": "What must the Magistrate do if an accused produced under Section 183 BNSS / S. 164 CrPC states he is unwilling to confess?",
                "back": "The Magistrate SHALL NOT authorize detention of such person in police custody (must remand to judicial custody).",
                "category": "Confession Safeguards"
            },
            {
                "id": "fc-crpc-06-06",
                "front": "What minimum reflection time is ordinarily recommended by the Supreme Court in Sarwan Singh before recording a confession?",
                "back": "Ordinarily at least twenty-four (24) hours of reflection away from police influence.",
                "category": "Judicial Confessions"
            }
        ],
        "sourceReferences": [{"title": "Section 183, Bharatiya Nagarik Suraksha Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    # -------------------------------------------------------------------------
    # CHAPTER 7: REMAND, POLICE CUSTODY & INVESTIGATION COMPLETION
    # -------------------------------------------------------------------------
    "top-crpc-07-01": {
        "topicId": "top-crpc-07-01",
        "chapterId": "ch-crpc-07",
        "subjectId": "law-crpc",
        "title": "Remand & Police Custody: S. 187 BNSS vs S. 167 CrPC & Default Bail",
        "subtitle": "Section 187 BNSS Groundbreaking Reform: Police Custody in Parts Across 40/60 Days",
        "learningObjective": "Master the monumental reform in Section 187 BNSS permitting 15 days of police custody to be taken in parts across the initial 40 or 60 days, default bail timelines (60/90 days), and the indefeasible right to statutory bail.",
        "introduction": "Section 167 CrPC (now Section 187 BNSS) governs detention when investigation cannot be completed within 24 hours. The Supreme Court in Anupam J. Kulkarni (1992) held that 15 days of police remand could ONLY be taken during the first 15 days of detention. BNSS 2023 executes a historic legislative reversal: police custody can now be granted in parts throughout the initial 40 or 60 days.",
        "detailedExplanation": """
<h3>1. The Historic Shift in Police Custody (Section 187(2) & 187(3) BNSS)</h3>
<ul>
  <li><strong>CrPC 1973 Position (Anupam J. Kulkarni):</strong> Police custody could not exceed 15 days in the whole, and could ONLY be granted during the <strong>first fifteen days</strong> after initial arrest. Subsequent detention could only be judicial custody.</li>
  <li><strong>BNSS 2023 Groundbreaking Reform:</strong> The Magistrate may authorize detention in police custody for a term <strong>not exceeding fifteen (15) days in the whole, or in parts</strong>, at any time during the initial <strong>forty (40) days</strong> (in 60-day cases) or initial <strong>sixty (60) days</strong> (in 90-day cases) of the detention period!</li>
  <li><strong>Significance:</strong> Police can now seek police remand after weeks of judicial custody if new evidence or forensic reports emerge, expressly overriding the strict rigidity of the Kulkarni doctrine.</li>
</ul>

<h3>2. Maximum Total Detention & Default Bail (Section 187(3) BNSS / Section 167(2) CrPC)</h3>
<p>The Magistrate may authorize detention beyond 15 days in <strong>judicial custody</strong>, but the total detention period cannot exceed:</p>
<ol>
  <li><strong>Ninety (90) Days:</strong> Where the investigation relates to an offence punishable with <strong>death, imprisonment for life, or imprisonment for a term of not less than ten (10) years</strong>;</li>
  <li><strong>Sixty (60) Days:</strong> Where the investigation relates to <strong>any other offence</strong>.</li>
</ol>

<h3>3. The Indefeasible Right to Default Bail</h3>
<p>On the expiry of the said period of 90 days or 60 days, if the charge-sheet is not filed, the accused person <strong>SHALL be released on bail</strong> if prepared to and does furnish bail. In <em>Bikramjit Singh</em> and <em>M. Ravindran</em>, the Supreme Court held that default bail is an <strong>indefeasible fundamental right</strong> under Article 21 which cannot be defeated by subsequent filing of a charge-sheet while the application is pending.</p>
""",
        "keyProvisions": [
            {"section": "Section 187, BNSS 2023 (S. 167 CrPC)", "title": "Procedure when investigation cannot be completed in 24 hours", "content": "15 days police custody in parts during initial 40/60 days; 60/90 days default bail limits."},
            {"section": "Section 187(3), BNSS 2023 (S. 167(2) CrPC)", "title": "Default Bail Mandate", "content": "Accused must be released on bail if charge-sheet not filed within 60 or 90 days."}
        ],
        "landmarkCases": [
            {"caseName": "CBI v. Anupam J. Kulkarni", "citation": "(1992) 3 SCC 141", "bench": "Supreme Court of India", "principle": "Held that police custody can be granted only during the first 15 days; overruled by the express legislative text of Section 187 BNSS 2023."},
            {"caseName": "M. Ravindran v. Directorate of Revenue Intelligence", "citation": "(2021) 2 SCC 485", "bench": "Three-Judge Bench", "principle": "Default bail under Section 167(2) is not a mere statutory right but an integral part of the fundamental right to personal liberty under Article 21."}
        ],
        "comparativeTable": [
            {
                "title": "Police Custody & Default Bail: CrPC vs BNSS",
                "headers": ["Feature", "CrPC 1973 Section 167", "BNSS 2023 Section 187"],
                "rows": [
                    ["15-Day Police Custody", "Only during the first 15 days (Kulkarni rule)", "Can be taken in parts during first 40 or 60 days"],
                    ["90-Day Default Bail", "Death, life, or >= 10 yrs imprisonment", "Death, life, or >= 10 yrs imprisonment (Unaltered)"],
                    ["60-Day Default Bail", "All other offences", "All other offences (Unaltered)"],
                    ["Nature of Right", "Indefeasible right under Art 21", "Indefeasible right under Art 21 (Reaffirmed)"]
                ]
            }
        ],
        "diagramId": "diag-crpc-remand-custody-timeline",
        "diagramExplanation": "Shows the 15-day police custody spread across 40/60 days and the 60/90 days default bail deadlines.",
        "prelimTraps": [
            {
                "trap": "Believing Section 187 BNSS allows police custody beyond a total of 15 days.",
                "reality": "The TOTAL aggregate police custody remains capped at 15 DAYS. What changed is that those 15 days can now be taken IN PARTS during the first 40 or 60 days, rather than strictly in the first 15 days.",
                "rule": "Total police custody = max 15 days; can now be split in parts."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crpc-07-01",
                "front": "What revolutionary reform did Section 187 BNSS make regarding 15 days of police custody?",
                "back": "Police custody of up to 15 days can now be taken in parts across the first 40 days (for 60-day cases) or first 60 days (for 90-day cases).",
                "category": "BNSS Remand Reforms"
            },
            {
                "id": "fc-crpc-07-02",
                "front": "What are the two statutory default bail periods under Section 187 BNSS / S. 167 CrPC?",
                "back": "Ninety (90) days for offences punishable with death, life, or 10+ yrs; sixty (60) days for all other offences.",
                "category": "Default Bail"
            }
        ],
        "sourceReferences": [{"title": "Section 187, Bharatiya Nagarik Suraksha Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-crpc-07-02": {
        "topicId": "top-crpc-07-02",
        "chapterId": "ch-crpc-07",
        "subjectId": "law-crpc",
        "title": "Inquest Inquiries & Final Police Report (Charge-Sheet S. 173 CrPC)",
        "subtitle": "BNSS Sections 193–196 vs CrPC Sections 173–176 & 90-Day Victim Reporting",
        "learningObjective": "Master police and magisterial inquests (Sections 174–176 CrPC / Sections 194–196 BNSS), the completion of investigation through the Police Report / Charge-Sheet (Section 173 CrPC / Section 193 BNSS), and the mandatory 90-day progress report to the victim.",
        "introduction": "An investigation culminates in a final police report under Section 173 CrPC (now Section 193 BNSS), presenting either a charge-sheet or a closure report. For unnatural deaths, preliminary inquest proceedings establish the apparent cause of death before or alongside substantive investigation.",
        "detailedExplanation": """
<h3>1. Inquest by Police (Section 194 BNSS / Section 174 CrPC)</h3>
<p>When an officer in charge of a police station receives information that a person has committed suicide, or has been killed by another, or has died under suspicious circumstances, the officer shall immediately report to the nearest <strong>Executive Magistrate</strong> and proceed to the place where the body is. Scope: Inquest is confined strictly to ascertaining the <strong>apparent cause of death</strong>, wounds, fractures, and weapon used. It is NOT for ascertaining who committed the crime!</p>

<h3>2. Magisterial Inquest (Section 196 BNSS / Section 176 CrPC)</h3>
<p>An inquest <strong>shall be held by a Judicial Magistrate or Metropolitan Magistrate</strong> in cases of:</p>
<ul>
  <li>Death or disappearance of any person in <strong>custody of the police</strong> or in any other custody;</li>
  <li>Rape alleged to have been committed on any woman while in custody.</li>
  <li>Executive Magistrate conducts inquest in cases involving death of a woman within <strong>seven (7) years of marriage</strong> (dowry death inquiries under S. 196(1) BNSS / S. 176(1) CrPC).</li>
</ul>

<h3>3. Final Police Report / Charge-Sheet (Section 193 BNSS / Section 173 CrPC)</h3>
<p>Every investigation shall be completed without unnecessary delay. In child rape cases, investigation must be completed within <strong>two (2) months</strong> from the date information was recorded.</p>
<p><strong>BNSS 90-Day Victim Update Mandate (Section 193(3)(ii) BNSS):</strong> The police officer shall inform the progress of investigation, including by electronic means, to the <strong>informant or the victim within ninety (90) days</strong>.</p>

<h3>4. Further Investigation (Section 193(9) BNSS / Section 173(8) CrPC)</h3>
<p>Nothing in this section precludes <strong>further investigation</strong> in respect of an offence after a report has been forwarded to the Magistrate. Police may obtain further evidence and forward a supplementary police report (Charge-Sheet). However, fresh investigation or re-investigation de novo without court permission is prohibited.</p>
""",
        "keyProvisions": [
            {"section": "Section 193, BNSS 2023 (S. 173 CrPC)", "title": "Report of police officer on completion of investigation", "content": "Charge-sheet/final report; 2-month limit for child sexual offences; 90-day victim progress reporting."},
            {"section": "Section 194, BNSS 2023 (S. 174 CrPC)", "title": "Police to inquire and report on suicide, etc.", "content": "Inquest into apparent cause of death."},
            {"section": "Section 196, BNSS 2023 (S. 176 CrPC)", "title": "Inquiry by Magistrate into cause of death", "content": "Judicial Magistrate inquest mandatory for custodial deaths and custodial rape."}
        ],
        "landmarkCases": [
            {"caseName": "Pedda Narayana v. State of A.P.", "citation": "(1975) 4 SCC 153", "bench": "Supreme Court of India", "principle": "The scope of an inquest report under Section 174 is very limited; it is not necessary to mention names of eyewitnesses or accused in the inquest report."},
            {"caseName": "Vinay Tyagi v. Irshad Ali", "citation": "(2013) 5 SCC 762", "bench": "Supreme Court of India", "principle": "Differentiated between 'further investigation' under Section 173(8), which police can conduct, and 're-investigation / fresh investigation', which only superior courts can direct."}
        ],
        "comparativeTable": [
            {
                "title": "Inquest & Final Report: CrPC 1973 vs BNSS 2023",
                "headers": ["Aspect", "CrPC 1973 Framework", "BNSS 2023 Framework"],
                "rows": [
                    ["Inquest in Custodial Death", "Judicial Magistrate mandatory (S. 176(1A))", "Judicial Magistrate mandatory (S. 196(2))"],
                    ["Child Sexual Offence Deadline", "2 months for investigation (S. 173(1A))", "2 months for investigation (S. 193(1))"],
                    ["Victim Progress Reporting", "No explicit timeline", "Mandatory progress report within 90 days (S. 193(3)(ii))"],
                    ["Electronic Charge-Sheet", "Varying state practices", "Statutorily authorized under BNSS"]
                ]
            }
        ],
        "diagramId": "diag-crpc-investigation-flowchart",
        "diagramExplanation": "Shows progress from inquest to final police report, closure, or charge-sheet forwarding to the Magistrate.",
        "prelimTraps": [
            {
                "trap": "Believing an Executive Magistrate conducts inquests in custodial death cases under Section 176 CrPC / Section 196 BNSS.",
                "reality": "Custodial deaths and custodial rapes MANDATE an inquest by a Judicial Magistrate (or Metropolitan Magistrate under CrPC). Executive Magistrates are competent for dowry deaths or general unnatural deaths.",
                "rule": "Custodial death = Judicial Magistrate inquest mandatory."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crpc-07-03",
                "front": "Who is statutorily mandated to conduct an inquiry into a custodial death under S. 196(2) BNSS / S. 176(1A) CrPC?",
                "back": "A Judicial Magistrate (not an Executive Magistrate).",
                "category": "Inquests"
            },
            {
                "id": "fc-crpc-07-04",
                "front": "Within what period must police update the victim or informant on investigation progress under S. 193(3)(ii) BNSS?",
                "back": "Within ninety (90) days.",
                "category": "BNSS Investigation Reforms"
            }
        ],
        "sourceReferences": [{"title": "Sections 193–196, Bharatiya Nagarik Suraksha Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    # -------------------------------------------------------------------------
    # CHAPTER 8: JURISDICTION, COGNIZANCE & COMPLAINTS
    # -------------------------------------------------------------------------
    "top-crpc-08-01": {
        "topicId": "top-crpc-08-01",
        "chapterId": "ch-crpc-08",
        "subjectId": "law-crpc",
        "title": "Territorial Jurisdiction of Criminal Courts for Inquiries & Trials",
        "subtitle": "BNSS Sections 197–209 vs CrPC Sections 177–189 & The Forum of Justice",
        "learningObjective": "Master territorial jurisdiction rules: ordinary place of trial (Section 177 CrPC / S. 197 BNSS), consequences ensuing (Section 179 CrPC / S. 199 BNSS), continuing offences, offences in transit, and offences outside India.",
        "introduction": "Territorial jurisdiction ensures that criminal trials occur in a convenient forum where witnesses and evidence are located. Chapter XIII of CrPC (Chapter XIV of BNSS) establishes rules governing the venue of inquiries and trials, resolving multi-jurisdictional complexities.",
        "detailedExplanation": """
<h3>1. Ordinary Place of Inquiry & Trial (Section 197 BNSS / Section 177 CrPC)</h3>
<p>Every offence shall ordinarily be inquired into and tried by a Court within whose local jurisdiction it was <strong>committed</strong>. This embodies the forum delicti commissi doctrine.</p>

<h3>2. Special Territorial Rules (Sections 198–205 BNSS / Sections 178–185 CrPC)</h3>
<ul>
  <li><strong>Uncertainty / Multi-Localities (S. 198 BNSS / S. 178 CrPC):</strong> Where it is uncertain in which of several local areas an offence was committed, or where an offence is committed partly in one local area and partly in another, or where an offence is a <strong>continuing one</strong>, it may be inquired into or tried by a court having jurisdiction over any of such local areas.</li>
  <li><strong>Offence Triable Where Act Done or Consequence Ensues (S. 199 BNSS / S. 179 CrPC):</strong> Where an act is an offence by reason of anything which has been done and of any consequence which has ensued, the offence may be tried where the act was done <strong>OR where consequence ensued</strong> (e.g. fatal blow struck in Varanasi, death occurs in Lucknow; trial valid in either).</li>
  <li><strong>Offences on Journey or Voyage (S. 203 BNSS / S. 183 CrPC):</strong> An offence committed while the offender or victim is in the course of performing a journey or voyage may be tried by any court through or into whose local jurisdiction the offender or victim passed in the course of that journey.</li>
</ul>

<h3>3. Offences Committed Outside India (Section 208 BNSS / Section 188 CrPC)</h3>
<p>When an offence is committed outside India by a <strong>citizen of India</strong>, or by a non-citizen on any ship or aircraft registered in India, they may be dealt with as if it had been committed at any place within India at which they may be found. <strong>Proviso:</strong> Previous sanction of the <strong>Central Government</strong> is mandatory before commencement of trial.</p>
""",
        "keyProvisions": [
            {"section": "Section 197, BNSS 2023 (S. 177 CrPC)", "title": "Ordinary place of inquiry and trial", "content": "Court within whose local jurisdiction the offence was committed."},
            {"section": "Section 199, BNSS 2023 (S. 179 CrPC)", "title": "Offence triable where act is done or consequence ensues", "content": "Concurrent jurisdiction at place of act or place of consequence."},
            {"section": "Section 208, BNSS 2023 (S. 188 CrPC)", "title": "Offence committed outside India", "content": "Jurisdiction where offender is found; Central Government sanction prerequisite for trial."}
        ],
        "landmarkCases": [
            {"caseName": "Mobarik Ali Ahmed v. State of Bombay", "citation": "AIR 1957 SC 857", "bench": "Constitution Bench", "principle": "A foreigner residing outside India who through letters and telephone induces a person in Bombay to part with money can be tried in Bombay where the consequence of cheating occurred."},
            {"caseName": "Thota Venkateswarlu v. State of A.P.", "citation": "(2011) 9 SCC 527", "bench": "Supreme Court of India", "principle": "Prior sanction of the Central Government under Section 188 CrPC is not required at the stage of investigation or cognizance; it is mandatory only before trial commences."}
        ],
        "comparativeTable": [
            {
                "title": "Territorial Jurisdiction Scenarios",
                "headers": ["Scenario", "Competent Court", "Section in BNSS", "Section in CrPC"],
                "rows": [
                    ["Offence committed in one place", "Court where committed", "Section 197", "Section 177"],
                    ["Act in City A, Death in City B", "Either City A or City B", "Section 199", "Section 179"],
                    ["Theft in Train / Voyage", "Any station train passed through", "Section 203", "Section 183"],
                    ["Citizen commits crime abroad", "Place in India where found", "Section 208", "Section 188"]
                ]
            }
        ],
        "diagramId": "diag-crpc-investigation-flowchart",
        "diagramExplanation": "Shows jurisdictional nexus: act locality, consequence locality, journey transit, and extraterritorial jurisdiction.",
        "prelimTraps": [
            {
                "trap": "Believing a court cannot take cognizance of an offence committed abroad by an Indian citizen without prior Central Government sanction.",
                "reality": "Under the Thota Venkateswarlu doctrine, cognizance and investigation do NOT require prior sanction under S. 188 CrPC / S. 208 BNSS. Sanction is required only before the actual TRIAL commences.",
                "rule": "Section 188 sanction is required before trial, not before cognizance."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crpc-08-01",
                "front": "Where an injury is inflicted in Kanpur but the victim dies in Prayagraj, which court has jurisdiction to try murder?",
                "back": "Both Kanpur and Prayagraj courts have concurrent jurisdiction under Section 199 BNSS / Section 179 CrPC.",
                "category": "Territorial Jurisdiction"
            },
            {
                "id": "fc-crpc-08-02",
                "front": "Whose prior sanction is required to try an offence committed outside India under Section 208 BNSS / S. 188 CrPC?",
                "back": "The Central Government.",
                "category": "Extraterritorial Jurisdiction"
            }
        ],
        "sourceReferences": [{"title": "Sections 197–209, Bharatiya Nagarik Suraksha Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-crpc-08-02": {
        "topicId": "top-crpc-08-02",
        "chapterId": "ch-crpc-08",
        "subjectId": "law-crpc",
        "title": "Cognizance of Offences by Magistrates & Statutory Sanctions",
        "subtitle": "BNSS Sections 210–222 vs CrPC Sections 190–199 & The 120-Day Deemed Sanction Rule",
        "learningObjective": "Master taking cognizance under Section 210 BNSS / Section 190 CrPC, the three statutory modes, prosecution for contempt/perjury (S. 195 CrPC), prosecution of public servants (S. 197 CrPC), and BNSS Section 218 introducing a 120-day deemed sanction rule.",
        "introduction": "Taking cognizance is the judicial application of mind to suspected offences to initiate criminal proceedings. Cognizance is taken of the OFFENCE, not of the offender. Because public servants need protection from vexatious litigation, the Code requires statutory sanction, which BNSS 2023 modernizes with a 120-day time-bound deemed sanction mechanism.",
        "detailedExplanation": """
<h3>1. Modes of Taking Cognizance (Section 210 BNSS / Section 190 CrPC)</h3>
<p>Any Magistrate of the First Class (and any Magistrate of the Second Class specially empowered) may take cognizance of any offence upon:</p>
<ol>
  <li><strong>Clause (a):</strong> Receiving a <strong>complaint of facts</strong> which constitute such offence;</li>
  <li><strong>Clause (b):</strong> A <strong>police report</strong> of such facts (charge-sheet under S. 173 / S. 193);</li>
  <li><strong>Clause (c):</strong> Information received from any person other than a police officer, or <strong>upon his own knowledge</strong> (suo motu).</li>
</ol>
<p>If cognizance is taken under Clause (c), the accused has a statutory right under Section 211 BNSS / S. 191 CrPC to have the case transferred to another Magistrate.</p>

<h3>2. Prosecution for Contempt & Perjury: Section 215 BNSS / S. 195 CrPC</h3>
<p>No court shall take cognizance of contempt of lawful authority of public servants (Section 195(1)(a)) or offences against public justice (perjury/forgery in relation to court documents under S. 195(1)(b)) <strong>EXCEPT on the complaint in writing of that public servant or court</strong>.</p>

<h3>3. Prosecution of Judges & Public Servants (Section 218 BNSS / S. 197 CrPC)</h3>
<p>When any person who is or was a Judge or Magistrate or a public servant not removable from office save by or with the sanction of the Government is accused of any offence alleged to have been committed by them <strong>while acting or purporting to act in the discharge of their official duty</strong>, no Court shall take cognizance without previous sanction of the Central or State Government.</p>

<h3>4. BNSS 120-Day Deemed Sanction Rule (Section 218(1) Proviso)</h3>
<p>BNSS 2023 solves chronic delays in prosecutorial sanctions by introducing an unprecedented statutory deadline: the Government <strong>shall take a decision within one hundred and twenty (120) days</strong> from the date of receipt of the request. If the Government fails to decide within 120 days, <strong>sanction shall be deemed to have been accorded</strong>!</p>
""",
        "keyProvisions": [
            {"section": "Section 210, BNSS 2023 (S. 190 CrPC)", "title": "Cognizance of offences by Magistrates", "content": "Three modes: complaint, police report, or suo motu/information."},
            {"section": "Section 215, BNSS 2023 (S. 195 CrPC)", "title": "Prosecution for contempt and offences against public justice", "content": "Mandatory written complaint of public servant or court concerned."},
            {"section": "Section 218, BNSS 2023 (S. 197 CrPC)", "title": "Prosecution of Judges and public servants", "content": "Official duty test; 120-day decision deadline with deemed sanction provision."}
        ],
        "landmarkCases": [
            {"caseName": "R.R. Chari v. State of U.P.", "citation": "AIR 1951 SC 207", "bench": "Supreme Court of India", "principle": "Taking cognizance does not involve any formal action; it occurs the moment a Magistrate applies his mind to the suspected commission of an offence for the purpose of proceeding under the Code."},
            {"caseName": "State of Orissa v. Ganesh Chandra Jew", "citation": "(2004) 8 SCC 40", "bench": "Supreme Court of India", "principle": "The official duty test under Section 197 requires a reasonable connection between the act complained of and the discharge of official duty; it cannot be an indiscriminate shield for criminal acts."}
        ],
        "comparativeTable": [
            {
                "title": "Sanction to Prosecute: CrPC 1973 vs BNSS 2023",
                "headers": ["Aspect", "CrPC 1973 Section 197", "BNSS 2023 Section 218"],
                "rows": [
                    ["Scope of Protection", "Acting in discharge of official duty", "Acting in discharge of official duty"],
                    ["Time Limit for Decision", "No statutory time limit (judicial guidelines)", "Mandatory 120 days for Government decision"],
                    ["Consequence of Inaction", "Accused remained in legal limbo", "Deemed sanction upon expiry of 120 days"],
                    ["Retired Public Servants", "Protected for past official acts", "Protected for past official acts (Unaltered)"]
                ]
            }
        ],
        "diagramId": "diag-crpc-courts-hierarchy",
        "diagramExplanation": "Shows the three streams of cognizance under Section 210 BNSS / S. 190 CrPC and the 120-day sanction filter.",
        "prelimTraps": [
            {
                "trap": "Believing a private citizen can file a police complaint for perjury committed in court.",
                "reality": "Under Section 215 BNSS / Section 195 CrPC, private complaints for perjury or fabricating false evidence are strictly barred. The complaint must be made in writing by the presiding judge of the COURT itself.",
                "rule": "Perjury complaints can ONLY be filed by the court concerned."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crpc-08-03",
                "front": "What revolutionary deemed sanction rule was introduced by Section 218 BNSS 2023 for public servant prosecution?",
                "back": "If the Government fails to decide on a sanction request within one hundred and twenty (120) days, sanction is deemed granted.",
                "category": "BNSS Sanction Reforms"
            },
            {
                "id": "fc-crpc-08-04",
                "front": "Does a Magistrate take cognizance of the offender or of the offence?",
                "back": "Cognizance is always taken of the OFFENCE, not of the offender (R.R. Chari doctrine).",
                "category": "Cognizance Principles"
            }
        ],
        "sourceReferences": [{"title": "Sections 210–222, Bharatiya Nagarik Suraksha Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    },

    "top-crpc-08-03": {
        "topicId": "top-crpc-08-03",
        "chapterId": "ch-crpc-08",
        "subjectId": "law-crpc",
        "title": "Complaints to Magistrates & Issue of Process (S. 200–204 CrPC)",
        "subtitle": "BNSS Sections 223–227 vs CrPC Sections 200–204 & Accused Opportunity of Hearing",
        "learningObjective": "Master private complaint procedure under Sections 200–203 CrPC / Sections 223–226 BNSS, inquiry under Section 202, dismissal of complaint, and the revolutionary Section 223(1) proviso granting the accused an opportunity of being heard before cognizance.",
        "introduction": "When citizens file private criminal complaints directly before Magistrates, the Code establishes a preliminary screening process to weed out false, frivolous, or malicious allegations before summoning the accused. BNSS 2023 fundamentally reforms this stage by introducing an opportunity of hearing for the proposed accused.",
        "detailedExplanation": """
<h3>1. Examination of Complainant (Section 223 BNSS / Section 200 CrPC)</h3>
<p>A Magistrate taking cognizance of an offence on complaint shall examine upon oath the complainant and the witnesses present, and the substance of each examination shall be reduced to writing and signed by the complainant and witnesses, and also by the Magistrate.</p>
<p><strong>Exemption from Examination:</strong> Examination is NOT required if the complaint is made in writing by a <strong>public servant acting in discharge of official duties</strong> or a <strong>Court</strong>.</p>

<h3>2. BNSS Innovation: Hearing Accused Before Cognizance (Section 223(1) Proviso)</h3>
<p>In a historic departure from CrPC jurisprudence (which held the accused has no locus standi prior to issue of process), BNSS Section 223(1) proviso enacts: <strong>No cognizance of an offence shall be taken by the Magistrate without giving the accused an opportunity of being heard!</strong></p>

<h3>3. Postponement of Issue of Process (Section 225 BNSS / Section 202 CrPC)</h3>
<p>Any Magistrate may postpone the issue of process and either:</p>
<ol>
  <li>Inquire into the case himself; OR</li>
  <li>Direct an investigation to be made by a police officer or other person.</li>
</ol>
<p><strong>Mandatory Inquest / Inquiry for Outsiders:</strong> Under Section 202(1) CrPC / Section 225(1) BNSS, if the accused resides at a place <strong>beyond the area in which the Magistrate exercises jurisdiction</strong>, holding an inquiry or directing investigation is <strong>MANDATORY</strong> before issuing process.</p>

<h3>4. Dismissal of Complaint vs Issue of Process (Sections 203 & 204 CrPC / S. 226 & 227 BNSS)</h3>
<ul>
  <li><strong>Dismissal (S. 226 BNSS / S. 203 CrPC):</strong> If after considering statements and inquiry results, the Magistrate is of opinion that there is <strong>no sufficient ground for proceeding</strong>, they shall dismiss the complaint, briefly recording reasons.</li>
  <li><strong>Issue of Process (S. 227 BNSS / S. 204 CrPC):</strong> If in the opinion of the Magistrate there is <strong>sufficient ground for proceeding</strong>, they shall issue a Summons (in a summons-case) or a Warrant / Summons (in a warrant-case).</li>
</ul>
""",
        "keyProvisions": [
            {"section": "Section 223, BNSS 2023 (S. 200 CrPC)", "title": "Examination of complainant", "content": "Oath examination; hearing to accused before taking cognizance under BNSS proviso."},
            {"section": "Section 225, BNSS 2023 (S. 202 CrPC)", "title": "Postponement of issue of process", "content": "Mandatory inquiry/investigation when accused resides outside territorial jurisdiction."},
            {"section": "Section 226 & 227, BNSS 2023 (S. 203 & 204 CrPC)", "title": "Dismissal of complaint & Issue of Process", "content": "Dismissal on lack of sufficient ground; process issued on prima facie satisfaction."}
        ],
        "landmarkCases": [
            {"caseName": "Chandra Deo Singh v. Prokash Chandra Bose", "citation": "AIR 1963 SC 1430", "bench": "Four-Judge Bench", "principle": "At the stage of Section 202/203, the Magistrate is only to see whether there is 'sufficient ground for proceeding', not whether there is sufficient ground for conviction."},
            {"caseName": "National Bank of Oman v. Barakara Abdul Aziz", "citation": "(2013) 2 SCC 488", "bench": "Supreme Court of India", "principle": "When the accused resides outside the territorial jurisdiction of the Magistrate, inquiry or investigation under Section 202 is mandatory to prevent harassment."}
        ],
        "comparativeTable": [
            {
                "title": "Private Complaint Procedure: CrPC vs BNSS",
                "headers": ["Stage", "CrPC 1973 Practice", "BNSS 2023 Framework"],
                "rows": [
                    ["Examination on Oath", "Mandatory under S. 200", "Mandatory under S. 223"],
                    ["Accused Right to be Heard", "No locus standi at pre-process stage", "Opportunity of hearing mandatory before cognizance (S. 223(1) Proviso)"],
                    ["Accused Outside Jurisdiction", "Mandatory S. 202 inquiry", "Mandatory S. 225 inquiry (Unaltered)"],
                    ["Dismissal of Complaint", "Recorded reasons under S. 203", "Recorded reasons under S. 226 (Unaltered)"]
                ]
            }
        ],
        "diagramId": "diag-crpc-investigation-flowchart",
        "diagramExplanation": "Shows private complaint path: filing, S. 200 oath, S. 202 inquiry for non-residents, and S. 203 dismissal or S. 204 process.",
        "prelimTraps": [
            {
                "trap": "Believing a Magistrate can issue summons directly to an accused residing in another state without any Section 202 inquiry.",
                "reality": "Under Section 202(1) CrPC / Section 225(1) BNSS, if the accused resides beyond the area of local jurisdiction, postponing process and conducting an inquiry/investigation is MANDATORY.",
                "rule": "Accused outside jurisdiction = mandatory S. 202 inquiry before summons."
            }
        ],
        "flashcards": [
            {
                "id": "fc-crpc-08-05",
                "front": "What new right does Section 223(1) proviso BNSS grant to an accused in a private complaint before cognizance?",
                "back": "An opportunity of being heard before the Magistrate takes cognizance of the offence.",
                "category": "BNSS Complaint Reforms"
            },
            {
                "id": "fc-crpc-08-06",
                "front": "When is an inquiry or investigation under Section 202 CrPC / Section 225 BNSS mandatory before issuing process?",
                "back": "When the accused resides at a place beyond the area in which the Magistrate exercises jurisdiction.",
                "category": "Postponement of Process"
            }
        ],
        "sourceReferences": [{"title": "Sections 223–227, Bharatiya Nagarik Suraksha Sanhita, 2023", "url": "https://www.mha.gov.in"}]
    }
}

# Write complete Part 2
content = f"""/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Criminal Procedure Module — Authored Concepts (Part 2: Ch 5 to 8)
 * Topics: top-crpc-05-01 to top-crpc-08-03 (10 Comprehensive Topics)
 */

(function (global) {{
  'use strict';

  const DATA = {json.dumps(CONCEPTS, indent=2)};

  global.CRPC_CONCEPTS_PART2 = DATA;
  if (typeof module !== 'undefined' && module.exports) {{
    module.exports = DATA;
  }}
}})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
"""

with open("assets/learning/data/crpc/crpc-concepts-part2.js", "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully generated assets/learning/data/crpc/crpc-concepts-part2.js ({len(CONCEPTS)} topics)")
