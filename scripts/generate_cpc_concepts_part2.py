"""
Generates assets/learning/data/cpc/cpc-concepts-part2.js
Topics: top-cpc-08-01 to top-cpc-14-02 (19 Topics, Chapters 8 to 14)
"""

import json

TOPICS_PART2 = {
  "top-cpc-08-01": {
    "topicId": "top-cpc-08-01",
    "chapterId": "ch-cpc-08",
    "subjectId": "law-cpc",
    "title": "Summons to Defendant: Modes of Service & Substituted Service (Order V)",
    "subtitle": "Order V Rules 1–30, Personal Service, Courier/Email (R. 9) & Substituted Service (R. 20)",
    "learningObjective": "Master the statutory methods of serving summons on defendants under Order V, distinguishing direct service, postal/electronic courier, refusal endorsements, and substituted service under Rule 20.",
    "introduction": "Audi alteram partem requires that no defendant be condemned unheard. Once a suit is instituted, summons must be issued under Section 27 and Order V to afford the defendant notice of the claim and opportunity to defend.",
    "detailedExplanation": """
<h3>1. Issue of Summons [Section 27 & Order V Rule 1]</h3>
<p>When a suit has been duly instituted, a summons may be issued to the defendant to appear and answer the claim on a day specified therein. The summons must be issued within <strong>thirty days</strong> from the date of institution of the suit (inserted by 1999 amendment).</p>

<h3>2. Modes of Service [Order V Rule 9]</h3>
<p>Summons can be served through:</p>
<ol>
  <li><strong>Proper Officer of Court:</strong> Personal delivery to defendant or his authorized agent (Rule 12).</li>
  <li><strong>Adult Family Member (Rule 15):</strong> Where defendant is absent from residence and has no agent, service may be made on any <strong>adult member of the family (male or female)</strong> residing with him. <em>Explanation:</em> A servant is NOT a member of the family!</li>
  <li><strong>Registered Post, Speed Post, Courier & Electronic Transmission [Rule 9(3)]:</strong> Service by registered post acknowledgment due, approved courier services, or electronic mail.</li>
</ol>

<h3>3. Service by Affixture on Refusal or Inability to Find [Order V Rule 17]</h3>
<p>Where the defendant or his agent refuses to sign the acknowledgment, or where the serving officer, after using all due and reasonable diligence, cannot find the defendant and there is no adult family member, the serving officer shall <strong>affix a copy of the summons on the outer door</strong> or some other conspicuous part of the house in which the defendant ordinarily resides or carries on business.</p>

<h3>4. Substituted Service [Order V Rule 20]</h3>
<p>Where the Court is satisfied that there is reason to believe that the defendant is <strong>keeping out of the way for the purpose of avoiding service</strong>, or that for any other reason the summons cannot be served in the ordinary way, the Court shall order the summons to be served by:</p>
<ul>
  <li>Affixing a copy in some conspicuous place in the court-house, and upon some conspicuous part of the house in which defendant last resided; OR</li>
  <li>By an advertisement in a <strong>daily newspaper circulating in the locality</strong> in which defendant last resided (Rule 20(1A)).</li>
</ul>
<p><strong>Legal Effect (Rule 20(2)):</strong> Service substituted by order of the Court shall be <strong>as effectual as if it had been made on the defendant personally</strong>.</p>
""",
    "keyProvisions": [
      {"section": "Section 27", "title": "Summons to Defendants", "description": "Summons issued on such day not beyond thirty days from institution."},
      {"section": "Order V Rule 9", "title": "Delivery of Summons by Court", "description": "Delivery by court officer, registered post, speed post, courier, email."},
      {"section": "Order V Rule 15", "title": "Service on Adult Member of Defendant's Family", "description": "Service on adult male or female member; servant is expressly not family."},
      {"section": "Order V Rule 17", "title": "Procedure when Defendant Refuses Service or Cannot be Found", "description": "Affixture on outer door with witness report."},
      {"section": "Order V Rule 20", "title": "Substituted Service", "description": "Court ordered affixture or newspaper advertisement when defendant avoids service; deemed as effectual as personal service."}
    ],
    "landmarkCases": [
      {"caseName": "Salem Advocate Bar Association v. Union of India", "year": "2005", "citation": "(2005) 6 SCC 344", "court": "Supreme Court of India", "principle": "Approved service through courier and modern electronic means (fax, email) under Order V Rule 9, directing High Courts to frame rules governing approved courier agencies."},
      {"caseName": "Sushil Kumar Sabharwal v. Gurpreet Singh", "year": "2002", "citation": "(2002) 5 SCC 377", "court": "Supreme Court of India", "principle": "Service of summons is a solemn matter. Substituted service under Rule 20 cannot be ordered mechanically without recorded satisfaction that defendant is actively evading service."}
    ],
    "comparativeTable": {
      "title": "Modes of Service of Summons",
      "headers": ["Mode", "Governing Rule", "Preconditions / Key Features"],
      "rows": [
        ["Personal Service", "Order V Rule 12", "Delivered directly to defendant or his empowered agent"],
        ["Family Member", "Order V Rule 15", "Adult male/female residing with defendant; SERVANT EXCLUDED"],
        ["Affixture on Refusal", "Order V Rule 17", "Refusal to sign or cannot be found after due diligence"],
        ["Substituted Service", "Order V Rule 20", "Requires judicial satisfaction that defendant is avoiding service"]
      ]
    },
    "diagramId": "diag-cpc-civil-suit-journey",
    "diagramExplanation": "Shows Stage 5: Summons in the Civil Suit Journey.",
    "prelimTraps": [
      {"trap": "Thinking service on a domestic servant living in the household constitutes valid service.", "reality": "Explanation to Order V Rule 15 explicitly states: 'a servant is not a member of the family within the meaning of this rule.'", "tip": "Servant is NEVER a family member under Order V Rule 15!"},
      {"trap": "Assuming substituted service has a lesser evidentiary value than personal service.", "reality": "Order V Rule 20(2) explicitly provides that substituted service is AS EFFECTUAL as personal service.", "tip": "Rule 20(2): Substituted service = Personal service in law."}
    ],
    "flashcards": [
      {"front": "Can summons be served on a female adult family member under Order V Rule 15?", "back": "Yes. The 1976 amendment removed the word 'male', permitting service on any adult family member (male or female).", "category": "Summons"},
      {"front": "Is service on a household servant valid service under Order V Rule 15?", "back": "No. The Explanation to Order V Rule 15 expressly excludes a servant.", "category": "Summons"}
    ],
    "sourceReferences": [
      {"title": "Order V, Code of Civil Procedure, 1908", "url": "https://www.indiacode.nic.in/handle/123456789/2191"}
    ]
  },

  "top-cpc-08-02": {
    "topicId": "top-cpc-08-02",
    "chapterId": "ch-cpc-08",
    "subjectId": "law-cpc",
    "title": "Appearance & Non-Appearance: Dismissal for Default & Remedies (Order IX)",
    "subtitle": "Order IX Rules 2, 3, 4, 8, 9: Neither Party Appears vs Defendant Appears & Plaintiff Defaults",
    "learningObjective": "Master the consequence of non-appearance of parties under Order IX, distinguishing between dismissal when neither party appears (Rule 3) and dismissal when only defendant appears (Rule 8), along with their distinct remedies.",
    "introduction": "Order IX governs consequences of appearance and non-appearance of parties when the suit is called on for hearing. The Code draws a sharp distinction between mutual default and default solely attributable to the plaintiff.",
    "detailedExplanation": """
<h3>1. Dismissal for Non-Service Due to Plaintiff's Default [Order IX Rule 2]</h3>
<p>Where on the day fixed it is found that summons was not served on the defendant because plaintiff failed to pay court-fee, postal charges, or copies of plaint, the Court may make an order that the suit be dismissed.</p>
<p><strong>Remedy (Rule 4):</strong> Plaintiff may either bring a <strong>fresh suit</strong> (subject to limitation) OR apply for an order to <strong>set the dismissal aside</strong> on showing sufficient cause.</p>

<h3>2. Dismissal when Neither Party Appears [Order IX Rule 3]</h3>
<p>Where neither party appears when the suit is called on for hearing, the Court may make an order that the <strong>suit be dismissed</strong>.</p>
<p><strong>Remedy (Order IX Rule 4):</strong> Where a suit is dismissed under Rule 2 or Rule 3, the plaintiff has two alternative remedies:</p>
<ol>
  <li>He may bring a <strong>fresh suit</strong> (subject to the law of limitation); OR</li>
  <li>He may apply for an order to <strong>set the dismissal aside</strong> on satisfying the court of sufficient cause.</li>
</ol>

<h3>3. Procedure when Only Defendant Appears [Order IX Rule 8]</h3>
<p>Where the defendant appears and the plaintiff does not appear when the suit is called on for hearing, the Court <strong>shall make an order that the suit be dismissed</strong>, UNLESS the defendant admits the claim or part thereof, in which case the Court shall pass a decree against the defendant upon such admission.</p>

<h3>4. Bar on Fresh Suit when Dismissed under Rule 8 [Order IX Rule 9]</h3>
<p><strong>THE CRITICAL BAR:</strong> Where a suit is dismissed wholly or partly under Rule 8, the plaintiff shall be <strong>PRECLUDED from bringing a fresh suit</strong> in respect of the same cause of action!</p>
<p><strong>Sole Remedy:</strong> The plaintiff's exclusive remedy is to apply under Order IX Rule 9 for an order to <strong>set the dismissal aside</strong>. If he satisfies the Court that there was <strong>sufficient cause</strong> for non-appearance, the Court shall set aside the dismissal upon terms as to costs.</p>
<p><em>Notice Requirement (Rule 9(2)):</em> No order shall be made under this rule unless notice of the application has been served on the opposite party.</p>
""",
    "keyProvisions": [
      {"section": "Order IX Rule 2", "title": "Dismissal where Summons not Served for Plaintiff's Failure", "description": "Failure to pay process fees/copies allows dismissal."},
      {"section": "Order IX Rule 3", "title": "Where Neither Party Appears, Suit to be Dismissed", "description": "Mutual absence allows dismissal."},
      {"section": "Order IX Rule 4", "title": "Plaintiff may bring Fresh Suit or Apply for Restoration", "description": "Dual remedy (fresh suit OR restoration) for dismissal under Rule 2 or Rule 3."},
      {"section": "Order IX Rule 8", "title": "Procedure where Defendant only Appears", "description": "Mandatory dismissal of suit unless defendant admits claim."},
      {"section": "Order IX Rule 9", "title": "Decree against Plaintiff by Default Bars Fresh Suit", "description": "Fresh suit completely barred; only restoration application on sufficient cause lies."}
    ],
    "landmarkCases": [
      {"caseName": "Sangram Singh v. Election Tribunal, Kotah", "year": "1955", "citation": "AIR 1955 SC 425", "court": "Supreme Court of India", "principle": "Order IX is designed to ensure orderly justice. Dismissal for default does not extinguish rights permanently if sufficient cause is shown. Procedural rules are handmaids of justice."},
      {"caseName": "Suraj Rattan Thirani v. Azamabad Tea Co. Ltd.", "year": "1965", "citation": "AIR 1965 SC 295", "court": "Supreme Court of India", "principle": "Order IX Rule 9 creates an absolute bar against instituting a fresh suit on the same cause of action if earlier suit was dismissed under Rule 8."}
    ],
    "comparativeTable": {
      "title": "Dismissal under Rule 3 vs Dismissal under Rule 8",
      "headers": ["Feature", "Neither Party Appears (Rule 3)", "Only Defendant Appears (Rule 8)"],
      "rows": [
        ["Attendance", "Both plaintiff and defendant absent", "Defendant present, plaintiff absent"],
        ["Fresh Suit Bar", "NO BAR; Plaintiff CAN file a fresh suit (Rule 4)", "ABSOLUTE BAR; Fresh suit is completely prohibited (Rule 9)"],
        ["Restoration Remedy", "Application under Order IX Rule 4", "Application under Order IX Rule 9"],
        ["Notice to Defendant", "No notice required for restoration under Rule 4", "Mandatory notice to defendant required under Rule 9(2)"],
        ["Appealability", "Order rejecting Rule 4 is not appealable", "Order rejecting Rule 9 is appealable under O. 43 R. 1(c)"]
      ]
    },
    "diagramId": "diag-cpc-exparte-default-remedies.svg",
    "diagramExplanation": "Visualizes default dismissal pathways under Order IX Rules 2, 3, 4 vs Rule 8 & 9.",
    "prelimTraps": [
      {"trap": "Assuming a fresh suit is barred when a suit is dismissed because neither party appeared under Rule 3.", "reality": "Order IX Rule 4 expressly allows the plaintiff to file a FRESH SUIT when dismissed under Rule 3. The bar operates ONLY when dismissed under Rule 8.", "tip": "Dismissal under R. 3 = Fresh suit allowed (R. 4). Dismissal under R. 8 = Fresh suit BARRED (R. 9)!"},
      {"trap": "Believing an order rejecting an application under Order IX Rule 4 is appealable.", "reality": "Order rejecting Rule 4 is NOT appealable under Order XLIII Rule 1. Only an order rejecting Rule 9 (Rule 8 dismissal) is appealable under Order XLIII Rule 1(c).", "tip": "Rejecting Rule 9 = Appealable under O. 43 R. 1(c)."}
    ],
    "flashcards": [
      {"front": "Can a plaintiff file a fresh suit if his suit was dismissed under Order IX Rule 8?", "back": "No. Order IX Rule 9 strictly bars a fresh suit on the same cause of action.", "category": "Default Dismissal"},
      {"front": "Under which provision is an order rejecting an application to set aside dismissal under Order IX Rule 9 appealable?", "back": "Order XLIII Rule 1(c) of the CPC.", "category": "Appeals"}
    ],
    "sourceReferences": [
      {"title": "Order IX, Code of Civil Procedure, 1908", "url": "https://www.indiacode.nic.in/handle/123456789/2191"}
    ]
  },

  "top-cpc-08-03": {
    "topicId": "top-cpc-08-03",
    "chapterId": "ch-cpc-08",
    "subjectId": "law-cpc",
    "title": "Ex Parte Decrees: Remedies & Setting Aside under Order IX Rule 13",
    "subtitle": "Order IX Rules 6, 13, 14: Fourfold Remedies, Sufficient Cause & Second Proviso on Irregular Summons",
    "learningObjective": "Master the remedies available against an ex parte decree, focusing on Order IX Rule 13 grounds (summons not duly served vs prevented by sufficient cause), and the crucial Second Proviso protecting decrees from technical irregularities.",
    "introduction": "When the defendant fails to appear despite due service of summons, the court may proceed ex parte under Order IX Rule 6(1)(a) and pass an ex parte decree. The aggrieved defendant has four concurrent statutory remedies, chief among them being an application under Order IX Rule 13.",
    "detailedExplanation": """
<h3>1. Four Concurrent Remedies Against an Ex Parte Decree</h3>
<p>An aggrieved defendant against whom an ex parte decree has been passed has four distinct legal avenues:</p>
<ol>
  <li><strong>Application to Set Aside [Order IX Rule 13]:</strong> Filed in the court that passed the decree within 30 days (Article 123, Limitation Act).</li>
  <li><strong>Regular First Appeal [Section 96(2)]:</strong> An appeal lies from an original decree passed ex parte.</li>
  <li><strong>Application for Review [Section 114 & Order XLVII Rule 1]:</strong> Where grounds for review exist.</li>
  <li><strong>Substantive Suit on Ground of Fraud:</strong> An independent civil suit to set aside the decree on the ground that it was obtained by extrinsic fraud or fraudulent suppression of summons (not merely on lack of service).</li>
</ol>

<h3>2. Grounds for Setting Aside under Order IX Rule 13</h3>
<p>Under Order IX Rule 13, the court shall set aside the ex parte decree if the defendant satisfies the court of either of two grounds:</p>
<ol>
  <li>That the <strong>summons was not duly served</strong>; OR</li>
  <li>That he was <strong>prevented by any sufficient cause</strong> from appearing when the suit was called on for hearing.</li>
</ol>

<h3>3. The Crucial Second Proviso to Rule 13 (Added in 1976)</h3>
<p><em>'Provided further that no Court shall set aside a decree passed ex parte merely on the ground that there has been an irregularity in the service of summons, IF it is satisfied that the defendant had NOTICE of the date of hearing and had sufficient time to appear and answer the plaintiff's claim.'</em></p>
<p>This proviso prevents hyper-technical challenges: if defendant actually knew of the hearing date and had time to appear, mere procedural irregularity in service will NOT invalidate the decree!</p>

<h3>4. Effect of Explanation to Rule 13 (Bar when Appeal Dismissed)</h3>
<p>The Explanation provides that where an appeal has been preferred against an ex parte decree and the appeal has been <strong>dismissed on any ground other than withdrawal</strong>, no application under Order IX Rule 13 shall lie.</p>
""",
    "keyProvisions": [
      {"section": "Order IX Rule 6", "title": "Procedure when only Plaintiff Appears", "description": "Court may proceed ex parte if summons duly served."},
      {"section": "Order IX Rule 13", "title": "Setting Aside Decree Ex Parte Against Defendant", "description": "Court sets aside decree if summons not duly served or sufficient cause shown."},
      {"section": "Second Proviso to R. 13", "title": "Irregularity in Service Not Ground if Notice Existed", "description": "Merely irregular service cannot set aside decree if defendant had actual notice and sufficient time."},
      {"section": "Order IX Rule 14", "title": "No Decree to be Set Aside Without Notice to Opposite Party", "description": "Mandatory notice to plaintiff before setting aside ex parte decree."}
    ],
    "landmarkCases": [
      {"caseName": "Bhanu Kumar Jain v. Archana Kumar", "year": "2005", "citation": "(2005) 1 SCC 787", "court": "Supreme Court of India", "principle": "Defendant can avail both remedies—O. 9 R. 13 application and S. 96(2) first appeal—simultaneously. However, if first appeal is dismissed on merits, O. 9 R. 13 application cannot be proceeded with due to doctrine of merger."},
      {"caseName": "Parimal v. Veena", "year": "2011", "citation": "(2011) 3 SCC 545", "court": "Supreme Court of India", "principle": "'Sufficient cause' in Order IX Rule 13 means an elastic expression covering circumstances beyond the control of the party. The court must not adopt an over-technical approach, but intentional non-appearance cannot be condoned."}
    ],
    "comparativeTable": {
      "title": "Application under O. 9 R. 13 vs First Appeal under S. 96(2)",
      "headers": ["Attribute", "Order IX Rule 13 Application", "First Appeal under Section 96(2)"],
      "rows": [
        ["Forum", "Same trial court which passed the ex parte decree", "Superior appellate court (District Court or High Court)"],
        ["Ground of Attack", "Confined to non-service of summons or sufficient cause", "Merits of the case, appreciation of evidence, legal validity"],
        ["Appellate Remedy", "Appeal lies under Order XLIII Rule 1(d) if rejected", "Second appeal lies to HC on substantial question of law (S. 100)"],
        ["Limitation", "30 days under Article 123 of Limitation Act", "30 or 90 days depending on appellate forum"]
      ]
    },
    "diagramId": "diag-cpc-exparte-default-remedies.svg",
    "diagramExplanation": "Shows the fourfold remedial paths against an ex parte decree and the operation of Order IX Rule 13.",
    "prelimTraps": [
      {"trap": "Believing ANY defect in service of summons entitles the defendant to have an ex parte decree set aside.", "reality": "The Second Proviso to Order IX Rule 13 explicitly states that mere irregularity in service is NO GROUND if the defendant had actual notice and sufficient time to appear.", "tip": "Actual notice cures mere procedural irregularity in summons!"},
      {"trap": "Assuming an order rejecting an application under Order IX Rule 13 cannot be appealed.", "reality": "An order rejecting an Order IX Rule 13 application is an APPEALABLE ORDER under Order XLIII Rule 1(d).", "tip": "Rejection of O. 9 R. 13 = Appealable under O. 43 R. 1(d)."}
    ],
    "flashcards": [
      {"front": "What are the two statutory grounds for setting aside an ex parte decree under Order IX Rule 13?", "back": "1. Summons was not duly served; OR\n2. Prevented by sufficient cause from appearing.", "category": "Ex Parte Decrees"},
      {"front": "Under which provision is an order rejecting an application to set aside an ex parte decree appealable?", "back": "Order XLIII Rule 1(d) of the CPC.", "category": "Appeals"}
    ],
    "sourceReferences": [
      {"title": "Order IX Rules 13 & 14, Code of Civil Procedure, 1908", "url": "https://www.indiacode.nic.in/handle/123456789/2191"}
    ]
  },

  "top-cpc-09-01": {
    "topicId": "top-cpc-09-01",
    "chapterId": "ch-cpc-09",
    "subjectId": "law-cpc",
    "title": "Examination of Parties (Order X) & Discovery and Interrogatories (Order XI)",
    "subtitle": "Order X Rules 1–4, Order XI Rules 1–23: Interrogatories, Answering Timeline (R. 8) & Penalties (R. 21)",
    "learningObjective": "Master the pre-trial discovery mechanisms: oral examination under Order X (including ADR referral), discovery by interrogatories under Order XI, timeline to answer, and the severe penalty of striking out defence under Rule 21.",
    "introduction": "Before trial begins, the court must ascertain the real contest and narrow down issues. Order X empowers the court to examine parties orally at the first hearing, while Order XI enables discovery by interrogatories and inspection of documents.",
    "detailedExplanation": """
<h3>1. Examination of Parties by the Court [Order X]</h3>
<ul>
  <li><strong>Order X Rule 1:</strong> Ascertainment whether allegations in pleadings are admitted or denied.</li>
  <li><strong>Order X Rule 1A (ADR Direction):</strong> Inserted in 1999/2002; after recording admissions and denials, the court <strong>shall direct the parties to opt for one of the modes of alternative dispute resolution</strong> specified in Section 89 (Arbitration, Conciliation, Judicial Settlement, Lok Adalat, or Mediation).</li>
  <li><strong>Order X Rule 2:</strong> Oral examination of party or companion to elucidate matters in controversy.</li>
</ul>

<h3>2. Discovery by Interrogatories [Order XI Rules 1 to 11]</h3>
<p>Interrogatories are formal written questions administered by one party to the other with leave of the Court, which must be answered by <strong>affidavit</strong>.</p>
<ul>
  <li><strong>Object:</strong> To discover facts within the knowledge of the opponent, obtain admissions, and narrow down issues.</li>
  <li><strong>Limitation:</strong> Interrogatories can only be administered regarding <strong>facts in issue</strong>. Interrogatories seeking evidence (<em>facta probantia</em>) or of a fishing/roving nature are not permitted.</li>
  <li><strong>Time to Answer (Order XI Rule 8):</strong> Interrogatories shall be answered by affidavit to be filed within <strong>ten days</strong>, or within such other time as the Court may allow.</li>
</ul>

<h3>3. Non-Compliance Penalty [Order XI Rule 21]</h3>
<p>Where any party fails to comply with any order to answer interrogatories, or for discovery or inspection of documents:</p>
<ol>
  <li>If a <strong>plaintiff</strong>, he shall be liable to have his <strong>suit dismissed for want of prosecution</strong>.</li>
  <li>If a <strong>defendant</strong>, he shall be liable to have his <strong>defence, if any, struck out</strong>, and to be placed in the same position as if he had not defended.</li>
</ol>
<p>In <em>Babbar Sewing Machine Co. v. Tirlok Nath Mahajan (1978) 4 SCC 188</em>, the Supreme Court held that Rule 21 is a drastic penalty of last resort, to be exercised only upon willful, obstinate disobedience.</p>
""",
    "keyProvisions": [
      {"section": "Order X Rule 1A", "title": "Direction of the Court to Opt for ADR", "description": "Mandatory direction to opt for Section 89 ADR mechanisms at first hearing."},
      {"section": "Order XI Rule 1", "title": "Discovery by Interrogatories", "description": "Delivering written interrogatories with court leave."},
      {"section": "Order XI Rule 8", "title": "Affidavit in Answer, Filing", "description": "Affidavit answering interrogatories within 10 days."},
      {"section": "Order XI Rule 21", "title": "Non-compliance with Order for Discovery", "description": "Dismissal of suit for plaintiff; striking out defence for defendant."}
    ],
    "landmarkCases": [
      {"caseName": "Babbar Sewing Machine Co. v. Tirlok Nath Mahajan", "year": "1978", "citation": "(1978) 4 SCC 188", "court": "Supreme Court of India", "principle": "Striking out defence under Order XI Rule 21 is a penal provision of last resort. It should not be applied lightly for mere delay unless there is contumacious or obstinate disregard of court orders."},
      {"caseName": "Afcons Infrastructure Ltd. v. Cherian Varkey Construction Co.", "year": "2010", "citation": "(2010) 8 SCC 24", "court": "Supreme Court of India", "principle": "Clarified procedure under Order X Rule 1A for referring parties to ADR mechanisms under Section 89 after pleadings are complete."}
    ],
    "comparativeTable": {
      "title": "Interrogatories vs Cross-Examination",
      "headers": ["Feature", "Interrogatories (Order XI)", "Cross-Examination (Trial Stage)"],
      "rows": [
        ["Timing", "Pre-trial discovery stage before issues", "During trial after examination-in-chief"],
        ["Form", "Written questions approved by court and answered on affidavit", "Oral questions put to witness in open court"],
        ["Scope", "Confined strictly to material facts; no fishing questions", "Broad scope; can test veracity, memory, and credibility"],
        ["Time to Answer", "Within 10 days by sworn affidavit (Rule 8)", "Immediate oral answer under oath"]
      ]
    },
    "diagramId": "diag-cpc-civil-trial-sequence",
    "diagramExplanation": "Shows Stage 8: Discovery & Admissions in the Civil Trial Sequence.",
    "prelimTraps": [
      {"trap": "Thinking an affidavit in answer to interrogatories must be filed within 30 days.", "reality": "Order XI Rule 8 strictly prescribes TEN DAYS (not 30 days) for filing the affidavit in answer.", "tip": "Answering interrogatories = 10 DAYS (O. 11 R. 8)!"},
      {"trap": "Believing an order striking out defence under Order XI Rule 21 is not appealable.", "reality": "An order under Order XI Rule 21 is an APPEALABLE ORDER under Order XLIII Rule 1(f).", "tip": "Rule 21 order = Appealable under O. 43 R. 1(f)."}
    ],
    "flashcards": [
      {"front": "Within how many days must an affidavit in answer to interrogatories be filed under Order XI Rule 8?", "back": "Within ten (10) days, or within such other time as the Court may allow.", "category": "Discovery"},
      {"front": "What is the consequence under Order XI Rule 21 if a defendant fails to comply with an order for discovery?", "back": "His defence may be struck out, placing him in the same position as if he had not defended.", "category": "Discovery"}
    ],
    "sourceReferences": [
      {"title": "Order X & Order XI, Code of Civil Procedure, 1908", "url": "https://www.indiacode.nic.in/handle/123456789/2191"}
    ]
  },

  "top-cpc-09-02": {
    "topicId": "top-cpc-09-02",
    "chapterId": "ch-cpc-09",
    "subjectId": "law-cpc",
    "title": "Admissions (Order XII) & Production and Return of Documents (Order XIII)",
    "subtitle": "Order XII Rules 1–9, Judgment on Admissions (R. 6) & Production/Impounding (Order XIII)",
    "learningObjective": "Master the statutory procedure for admissions under Order XII, the extraordinary power to pronounce Judgment on Admissions under Rule 6, and rules on production, admission, and impounding of documents under Order XIII.",
    "introduction": "Admissions dispense with the need for formal proof. Order XII facilitates obtaining admissions of cases, documents, and facts, while Order XII Rule 6 empowers the court to grant immediate judgment on clear admissions without waiting for trial.",
    "detailedExplanation": """
<h3>1. Notice to Admit Documents & Facts [Order XII Rules 2 & 4]</h3>
<ul>
  <li><strong>Notice to Admit Documents (Rule 2):</strong> Either party may call upon the other to admit any document. If not admitted within <strong>seven days</strong> of notice, costs of proving the document shall be paid by the refusing party regardless of outcome.</li>
  <li><strong>Notice to Admit Facts (Rule 4):</strong> Any party may give notice to admit specific facts. Must be given not later than <strong>nine days before the day fixed for hearing</strong>, and admission must be made within <strong>six days</strong> after service.</li>
</ul>

<h3>2. Judgment on Admissions [Order XII Rule 6]</h3>
<p>Where admissions of fact have been made either in the pleading or otherwise, whether <strong>orally or in writing</strong>, the Court may at <strong>any stage of the suit</strong>, either on the application of any party or of its own motion (<strong>suo motu</strong>), and without waiting for the determination of any other question between the parties, make such order or give such <strong>judgment as it may think fit</strong>, having regard to such admissions.</p>
<p>In <em>Uttam Singh Dugal & Co. v. Union Bank of India (2000) 7 SCC 120</em>, the Supreme Court emphasized that Order XII Rule 6 is designed to expedite litigation. The admission must be <strong>clear, unambiguous, and unconditional</strong>. Once so established, judgment must follow.</p>

<h3>3. Production and Impounding of Documents [Order XIII]</h3>
<ul>
  <li><strong>Order XIII Rule 1:</strong> Original documents must be produced on or before the settlement of issues.</li>
  <li><strong>Rejection of Irrelevant/Inadmissible Documents (Rule 3):</strong> Court may reject inadmissible documents recording grounds.</li>
  <li><strong>Endorsements on Admitted Documents (Rule 4):</strong> Number, title, name of person producing, date, signed by Judge.</li>
  <li><strong>Impounding Documents (Rule 8):</strong> Court may, if it sees sufficient cause, direct any document or book produced before it to be <strong>impounded and kept in custody</strong> of an officer of the Court.</li>
  <li><strong>Return of Admitted Documents (Rule 9):</strong> Documents can be returned when suit is finally disposed of or appeal period expires, upon substituted certified copy.</li>
</ul>
""",
    "keyProvisions": [
      {"section": "Order XII Rule 2", "title": "Notice to Admit Documents", "description": "Notice to admit within 7 days; refusal attracts cost penalty."},
      {"section": "Order XII Rule 4", "title": "Notice to Admit Facts", "description": "Notice at least 9 days before hearing; admission within 6 days."},
      {"section": "Order XII Rule 6", "title": "Judgment on Admissions", "description": "Plenary power to grant judgment on clear oral or written admissions at any stage without trial."},
      {"section": "Order XIII Rule 1", "title": "Original Documents to be Produced", "description": "Production at or before settlement of issues."},
      {"section": "Order XIII Rule 8", "title": "Power to Impound Document", "description": "Court power to impound any document produced before it."}
    ],
    "landmarkCases": [
      {"caseName": "Uttam Singh Dugal & Co. Ltd. v. Union Bank of India", "year": "2000", "citation": "(2000) 7 SCC 120", "court": "Supreme Court of India", "principle": "The object of Order XII Rule 6 is to enable a party to obtain speedy judgment on admitted facts. The admission can be in pleadings or outside, provided it is clear, unambiguous, and unconditional."},
      {"caseName": "Karam Kapahi v. Lal Chand Public Charitable Trust", "year": "2010", "citation": "(2010) 4 SCC 753", "court": "Supreme Court of India", "principle": "Order XII Rule 6 is couched in wide terms—'in the pleading or otherwise', whether 'orally or in writing'. It can be invoked at any stage of the suit."}
    ],
    "comparativeTable": {
      "title": "Notice to Admit Documents vs Notice to Admit Facts",
      "headers": ["Parameter", "Notice to Admit Documents (O. 12 R. 2)", "Notice to Admit Facts (O. 12 R. 4)"],
      "rows": [
        ["Timing of Notice", "At any time, not later than specified by court", "At least 9 days before the day fixed for hearing"],
        ["Time Allowed to Admit", "Within 7 days of service of notice", "Within 6 days after service of notice"],
        ["Consequence of Refusal", "Must pay cost of proving document unless court orders otherwise", "Costs of proving facts unless court orders otherwise"],
        ["Scope of Admission", "Genuineness of document only (not truth of contents)", "Truth of specific material facts stated in notice"]
      ]
    },
    "diagramId": "diag-cpc-civil-trial-sequence",
    "diagramExplanation": "Shows Stage 8: Discovery & Admissions in the Civil Trial Sequence.",
    "prelimTraps": [
      {"trap": "Thinking Order XII Rule 6 applies only to written admissions made inside the formal pleadings.", "reality": "Rule 6 explicitly covers admissions made 'in the pleading or otherwise, whether orally or in writing'.", "tip": "Rule 6 = Pleadings or otherwise, oral or written!"},
      {"trap": "Believing a judgment under Order XII Rule 6 can be passed only upon an application by a party.", "reality": "Rule 6 empowers the court to act 'of its own motion' (suo motu) without any party application.", "tip": "Order XII Rule 6 judgment can be passed suo motu."}
    ],
    "flashcards": [
      {"front": "Under which provision can a court pass Judgment on Admissions at any stage without trial?", "back": "Order XII Rule 6 of the CPC.", "category": "Admissions"},
      {"front": "What are the essential requirements for an admission under Order XII Rule 6?", "back": "It must be clear, unambiguous, and unconditional (Uttam Singh Dugal v. UBI).", "category": "Admissions"}
    ],
    "sourceReferences": [
      {"title": "Order XII & Order XIII, Code of Civil Procedure, 1908", "url": "https://www.indiacode.nic.in/handle/123456789/2191"}
    ]
  },

  "top-cpc-10-01": {
    "topicId": "top-cpc-10-01",
    "chapterId": "ch-cpc-10",
    "subjectId": "law-cpc",
    "title": "Settlement of Issues (Order XIV) & Disposal at First Hearing (Order XV)",
    "subtitle": "Order XIV Rules 1–7: Issues of Fact vs Law (R. 2), First Hearing Disposal (O. XV) & UP O. XV R. 5",
    "learningObjective": "Master the framing of issues under Order XIV, trial of preliminary issues of law under Rule 2, disposal of suits at the first hearing under Order XV, and the vital Uttar Pradesh local amendment Order XV Rule 5.",
    "introduction": "Issues are the core focal points of civil litigation. Order XIV governs the framing and settlement of issues, while Order XV allows summary disposal at the first hearing when parties are not at issue on questions of law or fact.",
    "detailedExplanation": """
<h3>1. Framing of Issues [Order XIV Rule 1]</h3>
<p>Issues arise when a material proposition of fact or law is affirmed by the one party and denied by the other. Material propositions are those propositions of law or fact which a plaintiff must allege in order to show a right to sue or a defendant must allege in order to constitute his defence.</p>
<p><strong>Kinds of Issues [Rule 1(4)]:</strong></p>
<ol>
  <li>Issues of <strong>fact</strong>; and</li>
  <li>Issues of <strong>law</strong>.</li>
</ol>
<p><strong>Materials for Framing Issues (Rule 3):</strong> Allegations made on oath by parties, allegations in pleadings, and contents of documents produced.</p>

<h3>2. Preliminary Issues [Order XIV Rule 2]</h3>
<p><strong>General Rule (Rule 2(1)):</strong> Notwithstanding that a case may be decided on a preliminary issue, the Court <strong>shall pronounce judgment on all issues</strong> (to prevent piecemeal remands on appeal).</p>
<p><strong>Exception (Rule 2(2)):</strong> The court may try an issue as a preliminary issue ONLY where it is an <strong>issue of law only</strong>, relating to:</p>
<ul>
  <li>The <strong>jurisdiction of the Court</strong>; OR</li>
  <li>A <strong>bar to the suit created by any law</strong> for the time being in force (e.g., limitation, res judicata).</li>
</ul>
<p>If an issue of jurisdiction or limitation involves mixed questions of law and fact requiring evidence, it CANNOT be tried as a preliminary issue!</p>

<h3>3. Disposal of Suit at the First Hearing [Order XV]</h3>
<ul>
  <li><strong>Order XV Rule 1 (Parties not at issue):</strong> Where at first hearing it appears parties are not at issue on any question of law or fact, Court may at once pronounce judgment.</li>
  <li><strong>Order XV Rule 2 (One of several defendants not at issue):</strong> Court may pronounce judgment at once for or against him.</li>
  <li><strong>Order XV Rule 3 (Parties at issue):</strong> Where issues are framed and no further evidence than what is immediately producible is needed, court may determine issues at once.</li>
</ul>

<h3>4. UTTAR PRADESH STATE AMENDMENT: Order XV Rule 5</h3>
<p><strong>Striking Off Defence for Failure to Deposit Admitted Rent:</strong> In UP, Order XV Rule 5 was inserted (by UP Act 37 of 1972 and amended by UP Act 57 of 1976) in suits by a lessor for eviction of a lessee after determination of lease:</p>
<ol>
  <li>The defendant-tenant is <strong>mandatorily required to deposit the entire admitted rent</strong> due at or before the first hearing of the suit; AND</li>
  <li>Must continue to deposit monthly rent throughout the continuation of the suit.</li>
  <li><strong>Consequence:</strong> In case of default, the Court may <strong>strike off his defence</strong>! (The court retains judicial discretion to condone bona fide delay upon representation made within 10 days).</li>
</ol>
""",
    "keyProvisions": [
      {"section": "Order XIV Rule 1", "title": "Framing of Issues", "description": "Material proposition affirmed by one and denied by other; issues of fact and law."},
      {"section": "Order XIV Rule 2", "title": "Court to Pronounce Judgment on all Issues", "description": "Mandatory judgment on all issues; preliminary issue only on pure law relating to jurisdiction or statutory bar."},
      {"section": "Order XV Rule 1", "title": "Parties not at Issue", "description": "Immediate judgment at first hearing if no contest."},
      {"section": "UP Order XV Rule 5", "title": "Striking Off Defence for Non-Deposit of Rent", "description": "UP state amendment requiring eviction tenants to deposit admitted arrears and current rent; failure allows striking off defence."}
    ],
    "landmarkCases": [
      {"caseName": "Ramesh B. Desai v. Bipin Vadilal Mehta", "year": "2006", "citation": "(2006) 5 SCC 638", "court": "Supreme Court of India", "principle": "A plea of limitation or jurisdiction is generally a mixed question of law and fact. It cannot be tried as a preliminary issue under Order XIV Rule 2(2) unless it can be decided purely on the averments without recording evidence."},
      {"caseName": "Bimal Chand Jain v. Gopal Agarwal", "year": "1981", "citation": "(1981) 3 SCC 486", "court": "Supreme Court of India", "principle": "Order XV Rule 5 of UP is a discretionary power. Striking off defence is not automatic upon default; the court must apply judicial discretion and consider whether tenant had sufficient cause for delay."}
    ],
    "comparativeTable": {
      "title": "General Issues vs Preliminary Issues (Order XIV Rule 2)",
      "headers": ["Attribute", "General Issues (Rule 2(1))", "Preliminary Issues (Rule 2(2))"],
      "rows": [
        ["Scope", "All issues of fact and law", "Pure issues of law ONLY"],
        ["Subject Matter", "Merits, damages, title, breach", "Jurisdiction of Court OR statutory bar (limitation/res judicata)"],
        ["Requirement of Evidence", "Requires full trial and witness evidence", "Decidable purely on admitted facts/pleadings without trial"],
        ["Judgment Requirement", "Court must pronounce judgment on ALL issues", "If preliminary issue succeeds, suit dismissed without trying rest"]
      ]
    },
    "diagramId": "diag-cpc-civil-trial-sequence",
    "diagramExplanation": "Shows Stage 9: Framing of Issues in the Civil Trial Sequence.",
    "prelimTraps": [
      {"trap": "Thinking an issue of fact can be tried as a preliminary issue under Order XIV Rule 2.", "reality": "Order XIV Rule 2(2) permits preliminary trial ONLY for pure 'issues of law' relating to jurisdiction or statutory bars.", "tip": "Preliminary issue = Pure issue of law ONLY!"},
      {"trap": "Assuming UP Order XV Rule 5 requires automatic striking off of defence upon non-deposit of rent.", "reality": "Supreme Court in Bimal Chand Jain held that striking off under UP O. 15 R. 5 is discretionary, not mandatory.", "tip": "UP O. 15 R. 5 striking off is discretionary!"}
    ],
    "flashcards": [
      {"front": "What two matters can be tried as a preliminary issue under Order XIV Rule 2(2)?", "back": "Pure issues of law relating to: (1) The jurisdiction of the Court, or (2) A statutory bar to the suit (e.g., limitation or res judicata).", "category": "Framing of Issues"},
      {"front": "What is the subject matter of UP State Amendment Order XV Rule 5?", "back": "Striking off defence of a tenant in an eviction suit for failure to deposit admitted rent arrears and monthly rent.", "category": "UP State Amendments"}
    ],
    "sourceReferences": [
      {"title": "Order XIV & XV, Code of Civil Procedure, 1908", "url": "https://www.indiacode.nic.in/handle/123456789/2191"}
    ]
  },

  "top-cpc-10-02": {
    "topicId": "top-cpc-10-02",
    "chapterId": "ch-cpc-10",
    "subjectId": "law-cpc",
    "title": "Witness Attendance (Order XVI), Adjournments (Order XVII) & Trial (Order XVIII)",
    "subtitle": "Order XVI Rules 1–21, Order XVII Rules 1–3 (Three Adjournments Cap) & Order XVIII Rules 1–19",
    "learningObjective": "Master the trial procedure: summoning witnesses under Order XVI, the statutory three-adjournments rule in Order XVII Rule 1, and the sequence of trial, examination on affidavit (R. 4), and court inspection (R. 18) under Order XVIII.",
    "introduction": "The trial stage is the evidentiary climax of a civil suit. Orders XVI, XVII, and XVIII govern witness attendance, adjournment restrictions, and the conduct of the hearing.",
    "detailedExplanation": """
<h3>1. Summoning and Attendance of Witnesses [Order XVI]</h3>
<ul>
  <li><strong>List of Witnesses (Rule 1):</strong> Parties shall, on or before such date as the Court may appoint, and not later than <strong>fifteen days after issues are settled</strong>, present a list of witnesses whom they propose to call.</li>
  <li><strong>Witnesses Not in List (Rule 1A):</strong> A party may bring any witness to give evidence without applying for summons under Rule 1, subject to court permission.</li>
  <li><strong>Expenses of Witnesses (Rule 2):</strong> Party applying for summons must pay into Court a sum sufficient to cover travelling and subsistence allowance (diet money) within period fixed.</li>
</ul>

<h3>2. Adjournments & The 'Three Adjournments' Rule [Order XVII Rule 1]</h3>
<p>The Court may, if sufficient cause is shown, at any stage of the suit grant time and adjourn the hearing.</p>
<p><strong>THE STATUTORY CAP (Inserted in 1999):</strong> <em>'Provided that no such adjournment shall be granted more than three times to a party during hearing of the suit.'</em></p>
<p>In <em>Salem Advocate Bar Association (2005) 6 SCC 344</em>, the Supreme Court held that the cap of three adjournments is <strong>directory</strong> in extreme circumstances beyond the party's control (e.g., sudden illness, strike of transport), but cannot be bypassed routinely.</p>

<h3>3. Procedure on Default under Order XVII</h3>
<ul>
  <li><strong>Order XVII Rule 2:</strong> Where parties fail to appear on adjourned date, Court may proceed under Order IX (dismissal or ex parte).</li>
  <li><strong>Order XVII Rule 3:</strong> Where party to whom time was granted fails to produce evidence or cause attendance of witnesses, the Court may, <strong>notwithstanding such default, proceed to decide the suit forthwith</strong> on merits.</li>
</ul>

<h3>4. Hearing of Suit & Examination of Witnesses [Order XVIII]</h3>
<ul>
  <li><strong>Right to Begin (Rules 1 & 2):</strong> Plaintiff has right to begin, unless defendant admits facts and contends plaintiff is not entitled to relief, in which case defendant has right to begin.</li>
  <li><strong>Party Appearing as Witness First (Rule 3A):</strong> Where a party wishes to appear as a witness, he <strong>shall appear before any other witness</strong> on his behalf has been examined, unless the Court permits him to appear later.</li>
  <li><strong>Evidence on Affidavit (Rule 4):</strong> Examination-in-chief of all witnesses shall be on <strong>affidavit</strong>. Cross-examination and re-examination may be taken either by the Court or by a <strong>Commissioner</strong> appointed by the Court.</li>
  <li><strong>Court Inspection (Rule 18):</strong> The Court may at any stage of a suit inspect any property or thing concerning which any question may arise.</li>
</ul>
""",
    "keyProvisions": [
      {"section": "Order XVI Rule 1", "title": "List of Witnesses", "description": "Witness list within 15 days of settlement of issues."},
      {"section": "Order XVII Rule 1", "title": "Court May Grant Time and Adjourn Hearing", "description": "Adjournments restricted to maximum 3 times per party during hearing."},
      {"section": "Order XVII Rule 3", "title": "Court May Proceed Notwithstanding Party Fails to Produce Evidence", "description": "Power to decide suit forthwith on merits on evidence present."},
      {"section": "Order XVIII Rule 3A", "title": "Party to Appear before other Witnesses", "description": "Party must testify before other witnesses unless court permits."},
      {"section": "Order XVIII Rule 4", "title": "Recording of Evidence", "description": "Examination-in-chief by affidavit; cross-examination by court or commissioner."}
    ],
    "landmarkCases": [
      {"caseName": "Salem Advocate Bar Association v. Union of India", "year": "2005", "citation": "(2005) 6 SCC 344", "court": "Supreme Court of India", "principle": "The proviso to Order XVII Rule 1 capping adjournments at three times is directory. In extreme cases beyond a party's control, court can grant adjournment on exemplary costs. Order XVIII Rule 4 appointment of commissioners for recording cross-examination upheld."},
      {"caseName": "Prakash Chander v. Janki Manchanda", "year": "1986", "citation": "AIR 1987 SC 42", "court": "Supreme Court of India", "principle": "Order XVII Rule 3 applies only where party is present and fails to produce evidence; if party is absent, Order XVII Rule 2 (Order IX procedure) applies."}
    ],
    "comparativeTable": {
      "title": "Order XVII Rule 2 vs Order XVII Rule 3",
      "headers": ["Factor", "Order XVII Rule 2", "Order XVII Rule 3"],
      "rows": [
        ["Presence of Party", "Party fails to appear on the adjourned date", "Party is present, but fails to produce evidence or witnesses"],
        ["Disposal Nature", "Disposal under Order IX (dismissal for default / ex parte)", "Disposal on merits 'forthwith' on existing record"],
        ["Remedy", "Order IX Rule 9 or Rule 13 restoration application", "Regular Appeal under Section 96 (Decree on merits)"]
      ]
    },
    "diagramId": "diag-cpc-civil-trial-sequence",
    "diagramExplanation": "Shows Stage 10: Trial & Evidence in the Civil Trial Sequence.",
    "prelimTraps": [
      {"trap": "Believing a party can examine himself as a witness after all his other witnesses have testified without permission.", "reality": "Order XVIII Rule 3A explicitly requires the party to appear BEFORE other witnesses, unless court permits otherwise.", "tip": "Party must testify FIRST (Order XVIII Rule 3A)!"},
      {"trap": "Thinking cross-examination must always be conducted inside the courtroom before the Judge.", "reality": "Under Order XVIII Rule 4(2), cross-examination can be recorded by a Court Commissioner outside the courtroom.", "tip": "Cross-examination can be recorded by a Commissioner."}
    ],
    "flashcards": [
      {"front": "How many adjournments can be granted to a party during hearing under Order XVII Rule 1 proviso?", "back": "Not more than three (3) times, though directory in extreme circumstances (Salem Bar Case).", "category": "Adjournments"},
      {"front": "How is examination-in-chief recorded under Order XVIII Rule 4?", "back": "By way of affidavit.", "category": "Trial Procedure"}
    ],
    "sourceReferences": [
      {"title": "Orders XVI, XVII & XVIII, Code of Civil Procedure, 1908", "url": "https://www.indiacode.nic.in/handle/123456789/2191"}
    ]
  },

  "top-cpc-11-01": {
    "topicId": "top-cpc-11-01",
    "chapterId": "ch-cpc-11",
    "subjectId": "law-cpc",
    "title": "Judgment and Decree under Section 33 & Order XX: Distinction & Timelines",
    "subtitle": "Section 33, Order XX Rules 1–7: Pronouncement Timelines (30–60 Days) & Decree Drawing (R. 6A)",
    "learningObjective": "Master the statutory sequence of Judgment and Decree under Section 33 and Order XX, understanding pronouncement timelines (30 to 60 days), contents of judgment, and drawing up of decrees under Rule 6A.",
    "introduction": "Once trial concludes and arguments are heard, the court proceeds to adjudication. Section 33 directs that the Court, after the case has been heard, shall pronounce judgment, and on such judgment a decree shall follow. Order XX regulates this formal transition.",
    "detailedExplanation": """
<h3>1. Statutory Timelines for Pronouncing Judgment [Order XX Rule 1]</h3>
<p>The Court, after the case has been heard, shall pronounce judgment in an open Court, either at once, or as soon thereafter as may be practicable:</p>
<ul>
  <li><strong>Standard Period:</strong> Within <strong>thirty days</strong> from the date on which the hearing of the case was concluded.</li>
  <li><strong>Exceptional Extension:</strong> Where not practicable due to exceptional and extraordinary circumstances, it may be fixed on a future day, but which <strong>shall not ordinarily be beyond sixty days</strong> from conclusion of hearing.</li>
</ul>
<p>In <em>Anil Rai v. State of Bihar (2001) 7 SCC 318</em>, the Supreme Court laid down comprehensive guidelines emphasizing that inordinate delay in pronouncing judgments violates the rule of law.</p>

<h3>2. Contents of Judgment [Order XX Rule 4]</h3>
<ul>
  <li><strong>Small Cause Courts [Rule 4(1)]:</strong> Judgments of Courts of Small Causes need not contain more than the <em>points for determination</em> and the <em>decision thereon</em>.</li>
  <li><strong>Other Courts [Rule 4(2)]:</strong> Judgments of all other Courts shall contain:
    <ol>
      <li>A concise statement of the case;</li>
      <li>The points for determination;</li>
      <li>The decision thereon; and</li>
      <li>The reasons for such decision.</li>
    </ol>
  </li>
  <li><strong>Court to Decide Each Issue (Rule 5):</strong> In suits in which issues have been framed, the Court shall state its finding or decision, with reasons, upon each separate issue.</li>
</ul>

<h3>3. Preparation of Decree [Order XX Rule 6 & 6A]</h3>
<ul>
  <li><strong>Rule 6 (Contents):</strong> Decree shall agree with the judgment, contain number of suit, names of parties, relief granted, and amount of costs.</li>
  <li><strong>Rule 6A (Preparation Timeline):</strong> Every endeavor shall be made to ensure that the decree is drawn up as expeditiously as possible and, in any case, <strong>within fifteen days</strong> from the date on which the judgment is pronounced.</li>
  <li><strong>Right to Appeal Without Decree Copy:</strong> If decree is not drawn up within 15 days, the last paragraph of the judgment shall be deemed to be the decree for the purpose of preferring an appeal!</li>
  <li><strong>Date of Decree (Rule 7):</strong> The decree shall bear the <strong>date on which the judgment was pronounced</strong> (not the date on which it was signed).</li>
</ul>
""",
    "keyProvisions": [
      {"section": "Section 33", "title": "Judgment and Decree", "description": "Court pronounces judgment; decree follows judgment."},
      {"section": "Order XX Rule 1", "title": "Judgment when Pronounced", "description": "Within 30 days, extendable up to 60 days in extraordinary cases."},
      {"section": "Order XX Rule 4", "title": "Judgments of Courts", "description": "Concise statement, points for determination, decision, and reasons."},
      {"section": "Order XX Rule 6A", "title": "Preparation of Decree", "description": "Decree drawn up within 15 days; appeal can be filed on judgment if delayed."},
      {"section": "Order XX Rule 7", "title": "Date of Decree", "description": "Decree bears date of pronouncement of judgment."}
    ],
    "landmarkCases": [
      {"caseName": "Anil Rai v. State of Bihar", "year": "2001", "citation": "(2001) 7 SCC 318", "court": "Supreme Court of India", "principle": "Laid down authoritative guidelines regarding timelines for pronouncement of judgments to prevent justice from becoming a casualty of delayed adjudication."},
      {"caseName": "Kanhaiyalal v. Anupkumar", "year": "2003", "citation": "(2003) 1 SCC 430", "court": "Supreme Court of India", "principle": "Clarified that under Order XX Rule 6A, a party can prefer an appeal against the judgment even if the formal decree has not been drawn up within 15 days."}
    ],
    "comparativeTable": {
      "title": "Judgment vs Decree",
      "headers": ["Characteristic", "Judgment [S. 2(9) & O. XX R. 4]", "Decree [S. 2(2) & O. XX R. 6]"],
      "rows": [
        ["Definition", "Statement of grounds given by Judge", "Formal expression of conclusive adjudication"],
        ["Sequence", "Pronounced first in open court", "Drawn up within 15 days following judgment"],
        ["Contents", "Statement of facts, issues, points, reasoning", "Operative outcome, reliefs granted, costs breakdown"],
        ["Execution", "Cannot be executed directly", "Decree is the executable instrument (O. XXI)"],
        ["Date of Bearing", "Date of oral pronouncement", "Bears date of pronouncement of judgment (R. 7)"]
      ]
    },
    "diagramId": "diag-cpc-civil-trial-sequence",
    "diagramExplanation": "Shows Stage 12 (Judgment) & Stage 13 (Decree) in the Civil Trial Sequence.",
    "prelimTraps": [
      {"trap": "Thinking a decree bears the date on which the Judge actually signs it.", "reality": "Order XX Rule 7 explicitly mandates that the decree shall bear the date on which the JUDGMENT WAS PRONOUNCED.", "tip": "Date of decree = Date of judgment pronouncement (O. 20 R. 7)!"},
      {"trap": "Assuming an appeal cannot be filed until the formal decree is drawn up.", "reality": "Under Order XX Rule 6A, if decree is not drawn up within 15 days, appeal can be filed on the operative portion of the judgment.", "tip": "Rule 6A allows appeal without waiting for decree."}
    ],
    "flashcards": [
      {"front": "What is the standard time limit for pronouncing judgment after hearing concludes under Order XX Rule 1?", "back": "Within 30 days, extendable up to 60 days under extraordinary circumstances.", "category": "Judgment & Decree"},
      {"front": "What date does a decree bear under Order XX Rule 7?", "back": "The date on which the judgment was pronounced.", "category": "Judgment & Decree"}
    ],
    "sourceReferences": [
      {"title": "Section 33 & Order XX, Code of Civil Procedure, 1908", "url": "https://www.indiacode.nic.in/handle/123456789/2191"}
    ]
  },

  "top-cpc-11-02": {
    "topicId": "top-cpc-11-02",
    "chapterId": "ch-cpc-11",
    "subjectId": "law-cpc",
    "title": "Statutory Interest under Section 34: Commercial, Pendente Lite & Future Interest",
    "subtitle": "Section 34 Threefold Stages of Interest, Statutory 6% Cap & Commercial Transaction Provisos",
    "learningObjective": "Master the award of statutory interest under Section 34, distinguishing pre-suit interest, pendente lite interest, and future interest, including the 6% statutory ceiling and commercial transaction exception.",
    "introduction": "In money recovery suits, compensation for delay in payment is awarded as interest. Section 34 divides interest into three distinct temporal periods, giving the court wide discretion subject to statutory caps.",
    "detailedExplanation": """
<h3>1. The Three Stages of Interest under Section 34</h3>
<p>Section 34 bifurcates interest into three distinct temporal periods:</p>
<ol>
  <li><strong>Pre-Suit Interest (Past Interest):</strong> From the date the cause of action accrued until the date of institution of the suit. This is a matter of substantive law, not Section 34 discretion (e.g., contractual rate, statutory provision, or trade usage under Interest Act, 1978).</li>
  <li><strong>Pendente Lite Interest:</strong> From the date of institution of the suit to the date of the decree. Purely within the <strong>judicial discretion</strong> of the Court.</li>
  <li><strong>Future Interest (Post-Decree Interest):</strong> From the date of decree to the date of actual payment or realization.</li>
</ol>

<h3>2. The Statutory Ceiling on Future Interest (Section 34 Main Body)</h3>
<p>The Court may order future interest at such rate not exceeding <strong>six per cent per annum (6% p.a.)</strong>, as the Court deems reasonable on such principal sum.</p>

<h3>3. The Commercial Transaction Exception (Proviso to Section 34)</h3>
<p>Where the liability in relation to the sum so adjudged had arisen out of a <strong>commercial transaction</strong>, the rate of such further interest may <strong>exceed six per cent per annum</strong>, but shall not exceed:</p>
<ul>
  <li>The <strong>contractual rate of interest</strong>; OR</li>
  <li>Where there is no contractual rate, the rate at which moneys are lent or advanced by <strong>nationalised banks</strong> in relation to commercial transactions.</li>
</ul>
<p><em>Explanation I:</em> A transaction is a commercial transaction if it is connected with the industry, trade or business of the party incurring the liability.</p>

<h3>4. Consequence of Silence in Decree [Section 34(2)]</h3>
<p>Where a decree is <strong>silent with respect to the payment of further interest</strong> on such principal sum from the date of the decree to date of payment, the Court shall be deemed to have <strong>refused such interest</strong>, and a separate suit therefor shall NOT lie!</p>
""",
    "keyProvisions": [
      {"section": "Section 34(1)", "title": "Interest", "description": "Discretionary interest pendente lite; future interest capped at 6% p.a. (contractual/banking rate for commercial transactions)."},
      {"section": "Proviso to S. 34(1)", "title": "Commercial Transactions Rate", "description": "May exceed 6% up to contractual or nationalised bank commercial lending rate."},
      {"section": "Section 34(2)", "title": "Deemed Refusal if Decree Silent", "description": "Silence in decree regarding future interest deemed refusal; fresh suit barred."}
    ],
    "landmarkCases": [
      {"caseName": "Central Bank of India v. Ravindra", "year": "2002", "citation": "(2002) 1 SCC 367", "court": "Supreme Court of India (Constitution Bench)", "principle": "Authoritative interpretation of Section 34: 'Principal sum adjudged' includes capitalized interest up to date of suit in banking transactions, upon which pendente lite and future interest runs."},
      {"caseName": "State Bank of India v. Sarathi Textiles", "year": "2009", "citation": "(2009) 12 SCC 728", "court": "Supreme Court of India", "principle": "Award of future interest is discretionary; court is not bound to award contractual rate in every case, though commercial rate is permissible."}
    ],
    "comparativeTable": {
      "title": "Three Stages of Interest under Section 34",
      "headers": ["Stage", "Period", "Governing Principle / Rate"],
      "rows": [
        ["Pre-Suit Interest", "Cause of action to date of suit", "Substantive law / Contract / Interest Act, 1978"],
        ["Pendente Lite Interest", "Date of suit to date of decree", "Discretionary with Court (reasonable rate)"],
        ["Future Interest (Standard)", "Date of decree to payment", "Discretionary, CAPPED at maximum 6% p.a."],
        ["Future Interest (Commercial)", "Date of decree to payment", "Can exceed 6% up to contractual/bank commercial rate"]
      ]
    },
    "diagramId": "diag-cpc-civil-trial-sequence",
    "diagramExplanation": "Shows how Section 34 interest integrates into final decree adjudication.",
    "prelimTraps": [
      {"trap": "Believing future interest in ordinary non-commercial suits can be awarded at 18% per annum.", "reality": "Section 34(1) strictly caps future interest at 6% per annum for non-commercial transactions.", "tip": "Ordinary future interest cap = 6% p.a.!"},
      {"trap": "Assuming silence of decree on future interest allows party to file a separate suit for interest.", "reality": "Section 34(2) explicitly provides that silence is deemed refusal, and a separate suit is strictly BARRED.", "tip": "Silence = Deemed Refusal (S. 34(2)); no fresh suit lies."}
    ],
    "flashcards": [
      {"front": "What is the statutory ceiling on future interest under Section 34(1) for non-commercial suits?", "back": "Six per cent per annum (6% p.a.).", "category": "Interest"},
      {"front": "What is the legal consequence under Section 34(2) if a decree is silent regarding future interest?", "back": "It is deemed to have been refused, and a separate suit for interest is barred.", "category": "Interest"}
    ],
    "sourceReferences": [
      {"title": "Section 34, Code of Civil Procedure, 1908", "url": "https://www.indiacode.nic.in/handle/123456789/2191"}
    ]
  },

  "top-cpc-11-03": {
    "topicId": "top-cpc-11-03",
    "chapterId": "ch-cpc-11",
    "subjectId": "law-cpc",
    "title": "Costs: General (S. 35), Compensatory (S. 35A), Delay Costs (S. 35B) & Order XXA",
    "subtitle": "Section 35 Costs Follow Event, S. 35A Rs. 3,000 Ceiling & S. 35B Condition Precedent",
    "learningObjective": "Master the law of civil costs: general costs under Section 35 ('costs follow the event'), compensatory costs for false or vexatious claims under Section 35A (Rs. 3,000 limit), and delay costs under Section 35B.",
    "introduction": "To reimburse successful litigants and discourage vexatious or dilatory tactics, the CPC contains a sophisticated costs regime across Sections 35, 35A, 35B, and Order XXA.",
    "detailedExplanation": """
<h3>1. General Costs [Section 35]</h3>
<p>Costs of and incident to all suits are in the discretion of the Court. However, sub-section (2) enacts the fundamental rule: <strong>'Costs follow the event'</strong>—the successful party is normally entitled to recover his costs from the unsuccessful party. If the court directs that costs shall NOT follow the event, it <strong>shall state its reasons in writing</strong>.</p>

<h3>2. Compensatory Costs for False or Vexatious Claims [Section 35A]</h3>
<p>Awarded where any party objects that a claim or defence is <strong>false or vexatious to the knowledge of the party</strong> by whom it has been put forward, and such objection is subsequently allowed.</p>
<ul>
  <li><strong>Ceiling Limit:</strong> No Court shall make any order for compensatory costs exceeding <strong>three thousand rupees (Rs. 3,000)</strong> or exceeding the limits of its pecuniary jurisdiction, whichever amount is less.</li>
  <li><strong>Criminal Immunity:</strong> No person against whom an order under this section has been made shall, by reason thereof, be exempted from any criminal liability (e.g., prosecution for false claim under IPC).</li>
  <li><strong>Credit in Subsequent Damages Suit:</strong> Amount awarded under Section 35A shall be taken into account in any subsequent suit for damages for false claim.</li>
  <li><strong>Appealability:</strong> An order under Section 35A is an appealable order under <strong>Section 104(1)(ff)</strong>!</li>
</ul>

<h3>3. Costs for Causing Delay [Section 35B]</h3>
<p>Inserted by 1976 Amendment; where on any date fixed for hearing of a suit or taking any step, a party fails to take that step or applies for adjournment, the Court may make an order requiring such party to pay to the other party such <strong>costs as would be reasonably sufficient to reimburse him</strong>.</p>
<p><strong>Condition Precedent:</strong> The payment of such cost shall be a <strong>condition precedent</strong> to the further prosecution of the suit (if plaintiff defaults) or defence (if defendant defaults).</p>

<h3>4. Order XXA (Special Costs)</h3>
<p>Added in 1976, empowering the court to award specific costs incurred on notice, typing, travel of witnesses, and inspection of records.</p>
""",
    "keyProvisions": [
      {"section": "Section 35", "title": "Costs", "description": "General costs follow the event; reasons required if departed from."},
      {"section": "Section 35A", "title": "Compensatory Costs in Respect of False or Vexatious Claims", "description": "Maximum ceiling Rs. 3,000; appealable under Section 104(1)(ff)."},
      {"section": "Section 35B", "title": "Costs for Causing Delay", "description": "Reimbursement costs; payment is condition precedent to further prosecution/defence."},
      {"section": "Order XXA", "title": "Special Costs", "description": "Specific litigation expenses including notices and witness travel."}
    ],
    "landmarkCases": [
      {"caseName": "Salem Advocate Bar Association v. Union of India", "year": "2005", "citation": "(2005) 6 SCC 344", "court": "Supreme Court of India", "principle": "Noted that Rs. 3,000 limit in Section 35A has become unrealistic due to inflation, urging realistic actual costs under Section 35 and Order XXA to deter frivolous litigation."},
      {"caseName": "Ashok Kumar Mittal v. Ram Kumar Gupta", "year": "2009", "citation": "(2009) 2 SCC 656", "court": "Supreme Court of India", "principle": "Compensatory costs under Section 35A cannot exceed statutory ceiling of Rs. 3,000. Imposing exemplary costs of Rs. 1,00,000 under Section 35A held contrary to statute."}
    ],
    "comparativeTable": {
      "title": "General Costs (S. 35) vs Compensatory Costs (S. 35A) vs Delay Costs (S. 35B)",
      "headers": ["Feature", "General Costs (S. 35)", "Compensatory Costs (S. 35A)", "Delay Costs (S. 35B)"],
      "rows": [
        ["Object", "Indemnify successful party for litigation expenses", "Penalize false, frivolous, or vexatious pleadings", "Reimburse party for delay caused on hearing date"],
        ["Maximum Ceiling", "No statutory ceiling (reasonable expenses)", "Strict cap: Rs. 3,000 or pecuniary limit", "Actual reasonable costs incurred"],
        ["Appealability", "Only in appeal against decree", "Directly appealable under S. 104(1)(ff)", "Not appealable as an order"],
        ["Condition Precedent", "Enforced via execution of decree", "Enforced in decree execution", "Payment is condition precedent to proceed"]
      ]
    },
    "diagramId": "diag-cpc-civil-trial-sequence",
    "diagramExplanation": "Shows costs allocation at the decree preparation stage.",
    "prelimTraps": [
      {"trap": "Believing a court can award Rs. 50,000 under Section 35A for a false claim.", "reality": "Section 35A(2) strictly caps compensatory costs at Rs. 3,000.", "tip": "Section 35A maximum ceiling is Rs. 3,000 ONLY!"},
      {"trap": "Thinking an order awarding compensatory costs under Section 35A cannot be appealed.", "reality": "Section 104(1)(ff) expressly provides an appeal from an order under Section 35A.", "tip": "Section 35A order is appealable under S. 104(1)(ff)!"}
    ],
    "flashcards": [
      {"front": "What is the maximum monetary ceiling on compensatory costs under Section 35A?", "back": "Three thousand rupees (Rs. 3,000) or the pecuniary limit of the Court, whichever is less.", "category": "Costs"},
      {"front": "What is the consequence if a party fails to pay delay costs ordered under Section 35B?", "back": "Payment is a condition precedent to further prosecution of the suit (plaintiff) or defence (defendant).", "category": "Costs"}
    ],
    "sourceReferences": [
      {"title": "Sections 35, 35A, 35B, Code of Civil Procedure, 1908", "url": "https://www.indiacode.nic.in/handle/123456789/2191"}
    ]
  },

  "top-cpc-12-01": {
    "topicId": "top-cpc-12-01",
    "chapterId": "ch-cpc-12",
    "subjectId": "law-cpc",
    "title": "Executing Court Powers, Jurisdiction & Transfer of Decrees (Sections 36–46)",
    "subtitle": "Executing Court Cannot Go Behind Decree, Section 38–39 Transfer, Precepts (S. 46) & S. 47 Scope",
    "learningObjective": "Master the law of execution: competence of executing court, the cardinal rule that executing court cannot go behind the decree, transfer of decrees under Section 39, precepts under Section 46, and determination of execution questions under Section 47.",
    "introduction": "Execution is the enforcement of a decree. As the Privy Council remarked, the difficulties of a litigant in India begin when he has obtained a decree. Part II (Sections 36–74) and Order XXI (106 Rules) provide the exhaustive execution machinery.",
    "detailedExplanation": """
<h3>1. Court by which Decree May be Executed [Section 38]</h3>
<p>A decree may be executed either by the <strong>Court which passed it</strong>, or by the <strong>Court to which it is sent for execution</strong>.</p>
<p><em>Court Passing Decree Defined (Section 37):</em> Includes the court of first instance where the decree was passed in appeal, or where the original court has ceased to exist or lost jurisdiction.</p>

<h3>2. The Cardinal Rule: Executing Court Cannot Go Behind Decree</h3>
<p>An executing court must execute the decree as it stands. It has <strong>no jurisdiction to examine the correctness, legality, or merits</strong> of the decree. It cannot modify, vary, or add to its terms.</p>
<p><strong>Sole Exception: Total Nullity:</strong> Where the decree is passed by a court suffering from <strong>inherent lack of subject-matter jurisdiction</strong> (coram non judice), the decree is a complete nullity, and the executing court can refuse to execute it (<em>Kiran Singh v. Chaman Paswan</em>).</p>

<h3>3. Transfer of Decree [Section 39]</h3>
<p>The court passing a decree may send it for execution to another competent court:</p>
<ol>
  <li>If the judgment-debtor resides or works within the jurisdiction of that other court;</li>
  <li>If the judgment-debtor has property within such jurisdiction sufficient to satisfy the decree;</li>
  <li>If the decree directs sale/delivery of immovable property outside its jurisdiction.</li>
</ol>
<p><strong>Section 39(4) (Bar on Executing Court - Added in 2002):</strong> The court which passed the decree is <strong>expressly prohibited from executing</strong> such decree against any person or property outside the local limits of its jurisdiction.</p>

<h3>4. Questions to be Determined by Executing Court [Section 47]</h3>
<p>All questions arising between the parties to the suit or their representatives, and relating to the <strong>execution, discharge or satisfaction of the decree</strong>, shall be determined by the Court executing the decree and <strong>NOT by a separate suit</strong>.</p>
<p><em>Bar on Separate Suit:</em> Section 47 completely bars substantive independent suits on execution questions. (Note: Determinations under Section 47 are no longer decrees since 1976 amendment).</p>

<h3>5. Precepts [Section 46]</h3>
<p>Upon the application of the decree-holder, the Court which passed the decree may issue a <strong>precept</strong> to any other Court competent to execute such decree to attach any property belonging to the judgment-debtor.</p>
<p><strong>Limitation:</strong> Attachment under a precept shall not continue for more than <strong>two months</strong>, unless the period is extended by the court passing the decree or the decree is transferred in the meantime.</p>
""",
    "keyProvisions": [
      {"section": "Section 38", "title": "Court by Which Decree May be Executed", "description": "Executed either by court passing it or court to which sent."},
      {"section": "Section 39(4)", "title": "Territorial Bar on Execution", "description": "Court cannot execute against property/person outside its territorial limits."},
      {"section": "Section 46", "title": "Precepts", "description": "Interim attachment order to another court; valid for maximum 2 months unless extended."},
      {"section": "Section 47", "title": "Questions to be Determined by Executing Court", "description": "Execution, discharge, or satisfaction determined by executing court; separate suit barred."}
    ],
    "landmarkCases": [
      {"caseName": "Vasudev Dhanjibhai Modi v. Rajabhai Abdul Rehman", "year": "1970", "citation": "(1970) 1 SCC 670", "court": "Supreme Court of India", "principle": "Executing court cannot go behind the decree. It must take the decree as it stands. Only when a decree on its face is without jurisdiction and a nullity can executing court entertain an objection."},
      {"caseName": "Dhurandhar Prasad Singh v. Jai Prakash University", "year": "2001", "citation": "(2001) 6 SCC 534", "court": "Supreme Court of India", "principle": "Distinguished between void decrees (nullity, challengeable in execution under Section 47) and voidable/illegal decrees (valid until set aside in appeal/review, cannot be challenged in execution)."}
    ],
    "comparativeTable": {
      "title": "Transfer of Decree (S. 39) vs Precept (S. 46)",
      "headers": ["Feature", "Transfer of Decree (Section 39)", "Precept (Section 46)"],
      "rows": [
        ["Nature", "Permanent transmission of decree for complete execution", "Temporary interim attachment order to prevent alienation"],
        ["Duration", "Continues until execution is completed or returned", "Limited strictly to TWO MONTHS unless extended"],
        ["Powers of Recipient Court", "Full execution powers under Section 42", "Power only to attach; cannot sell property under precept alone"]
      ]
    },
    "diagramId": "diag-cpc-execution-framework.svg",
    "diagramExplanation": "Visualizes the execution framework under Sections 36–74 and Order XXI, showing decree transfer, Section 47 jurisdiction, and modes of enforcement.",
    "prelimTraps": [
      {"trap": "Thinking a determination under Section 47 is an appealable decree.", "reality": "Prior to 1976, Section 47 orders were deemed decrees. The 1976 Amendment Act removed Section 47 from Section 2(2); hence it is NOT a decree.", "tip": "Section 47 orders are NO LONGER decrees!"},
      {"trap": "Believing an attachment under a Precept under Section 46 continues indefinitely.", "reality": "Section 46 proviso caps attachment under a precept at TWO MONTHS, unless extended or decree transferred.", "tip": "Precept attachment = Maximum 2 months (S. 46)."}
    ],
    "flashcards": [
      {"front": "Can an executing court go behind the decree to question its correctness?", "back": "No. The executing court must execute the decree as it stands, unless it is a total nullity for inherent lack of jurisdiction.", "category": "Execution"},
      {"front": "How long does an attachment under a Precept under Section 46 remain in force?", "back": "For not more than two months, unless extended or decree transferred.", "category": "Execution"}
    ],
    "sourceReferences": [
      {"title": "Sections 38–47, Code of Civil Procedure, 1908", "url": "https://www.indiacode.nic.in/handle/123456789/2191"}
    ]
  },

  "top-cpc-12-02": {
    "topicId": "top-cpc-12-02",
    "chapterId": "ch-cpc-12",
    "subjectId": "law-cpc",
    "title": "Modes of Execution: Arrest & Detention (S. 51, 55, 58 & S. 56 Bar on Women)",
    "subtitle": "Civil Imprisonment Periods (S. 58), Exemption of Women (S. 56) & Jolly George Varghese Principles",
    "learningObjective": "Master the statutory rules governing arrest and detention in civil prison under Sections 51, 55, 56, and 58, the complete statutory immunity of women under Section 56, and human rights constraints.",
    "introduction": "Execution against the person of the judgment-debtor is a severe measure. The CPC hedges civil imprisonment with rigorous statutory safeguards, monetary thresholds, and an absolute gender exemption.",
    "detailedExplanation": """
<h3>1. Modes of Execution under Section 51</h3>
<p>Subject to conditions, execution may be ordered by:</p>
<ol type="a">
  <li>Delivery of any property specifically decreed;</li>
  <li>Attachment and sale, or sale without attachment;</li>
  <li><strong>Arrest and detention in prison</strong>;</li>
  <li>Appointing a receiver; or</li>
  <li>In such other manner as nature of relief requires.</li>
</ol>
<p><strong>Proviso to Section 51 (Requirement of Means):</strong> Where execution is by detention, the court MUST give opportunity to show cause and be satisfied that the debtor has <em>means to pay and refuses/neglects to pay</em>, or is absconding/dishonestly transferring property.</p>

<h3>2. ABSOLUTE STATUTORY BAR ON WOMEN [Section 56]</h3>
<p><strong>Section 56:</strong> <em>'Notwithstanding anything in this Part, the Court shall NOT order the arrest or detention in the civil prison of a <strong>woman</strong> in execution of a decree for the payment of money.'</em></p>
<p>This is an absolute, non-derogable prohibition. A woman cannot be sent to civil prison in execution of a money decree under any circumstance.</p>

<h3>3. Period of Detention in Civil Prison [Section 58]</h3>
<p>The duration of civil imprisonment depends strictly on the sum decreed:</p>
<ol>
  <li><strong>Where sum exceeds Rs. 5,000:</strong> Maximum period not exceeding <strong>three months</strong>.</li>
  <li><strong>Where sum exceeds Rs. 2,000 but does not exceed Rs. 5,000:</strong> Maximum period not exceeding <strong>six weeks</strong>.</li>
  <li><strong>Where sum DOES NOT exceed Rs. 2,000:</strong> <strong>NO ORDER FOR DETENTION</strong> shall be made at all!</li>
</ol>

<h3>4. Release and Prohibition on Re-Arrest [Section 58(2)]</h3>
<p>A judgment-debtor released from detention on payment of decree or expiry of period shall <strong>not be liable to be re-arrested</strong> under the decree in execution of which he was detained in the civil prison. However, release does NOT discharge the debt!</p>

<h3>5. Jolly George Varghese Doctrine</h3>
<p>In <em>Jolly George Varghese v. Bank of Cochin (1980) 2 SCC 360</em>, the Supreme Court held that mere poverty or inability to pay a civil debt is not a ground for imprisonment under Article 21 and ICCPR Article 11. There must be an element of bad faith, willful refusal, or fraudulent evasion.</p>
""",
    "keyProvisions": [
      {"section": "Section 51 Proviso", "title": "Show Cause for Detention", "description": "Mandatory satisfaction regarding means to pay and willful refusal before civil imprisonment."},
      {"section": "Section 56", "title": "Prohibition of Arrest or Detention of Women", "description": "Absolute bar on arrest or civil detention of women in execution of money decrees."},
      {"section": "Section 58", "title": "Duration of Detention & Release", "description": "Up to 3 months for >Rs. 5,000; up to 6 weeks for Rs. 2,000–5,000; nil for under Rs. 2,000."},
      {"section": "Section 58(2)", "title": "Prohibition on Re-Arrest", "description": "No re-arrest under same decree once released."}
    ],
    "landmarkCases": [
      {"caseName": "Jolly George Varghese v. Bank of Cochin", "year": "1980", "citation": "(1980) 2 SCC 360", "court": "Supreme Court of India", "principle": "To cast a person in prison because of his sheer inability to pay due to poverty violates Article 21 and international human rights. There must be proof of contumacious refusal or dishonest transfer of property under Section 51 proviso."}
    ],
    "comparativeTable": {
      "title": "Period of Civil Detention under Section 58",
      "headers": ["Decree Amount Adjudged", "Maximum Civil Imprisonment Period"],
      "rows": [
        ["Exceeding Rs. 5,000", "Maximum THREE MONTHS"],
        ["Exceeding Rs. 2,000 up to Rs. 5,000", "Maximum SIX WEEKS"],
        ["Not exceeding Rs. 2,000", "NO DETENTION PERMITTED (Total Immunity)"],
        ["Woman debtor (Money Decree)", "NO DETENTION PERMITTED (Absolute Bar under Section 56)"]
      ]
    },
    "diagramId": "diag-cpc-execution-framework.svg",
    "diagramExplanation": "Shows execution modes and the detention thresholds under Section 58.",
    "prelimTraps": [
      {"trap": "Thinking a woman can be arrested in execution of a money decree if she willfully refuses to pay.", "reality": "Section 56 is an absolute bar; no woman can be arrested or detained in civil prison in execution of a money decree.", "tip": "Section 56: Absolute immunity for women in money decrees!"},
      {"trap": "Believing a person can be detained in civil prison for a debt of Rs. 1,500.", "reality": "Section 58(1A) completely prohibits detention where the amount does not exceed Rs. 2,000.", "tip": "Below Rs. 2,000 = ZERO civil detention (S. 58(1A))."}
    ],
    "flashcards": [
      {"front": "What is the maximum period of civil detention under Section 58 for a decree exceeding Rs. 5,000?", "back": "Three months.", "category": "Execution"},
      {"front": "Can a woman be arrested in execution of a money decree under CPC?", "back": "No. Section 56 completely prohibits the arrest or detention of a woman in civil prison for a money decree.", "category": "Execution"}
    ],
    "sourceReferences": [
      {"title": "Sections 51, 56, 58, Code of Civil Procedure, 1908", "url": "https://www.indiacode.nic.in/handle/123456789/2191"}
    ]
  },

  "top-cpc-12-03": {
    "topicId": "top-cpc-12-03",
    "chapterId": "ch-cpc-12",
    "subjectId": "law-cpc",
    "title": "Attachment of Property: Section 60 Exemptions & Garnishee Orders (O. XXI)",
    "subtitle": "Section 60 Non-Attachable Properties, Salary Exemption Formula & Garnishee Rules (O. 21 R. 46A–46I)",
    "learningObjective": "Master the property attachment regime: the comprehensive list of non-attachable properties under Section 60 proviso, the salary attachment formula, and Garnishee proceedings under Order XXI Rules 46A to 46I.",
    "introduction": "Section 60 declares what property is liable to attachment and sale in execution of a decree, followed by an extensive humanitarian proviso shielding essential subsistence assets from creditor seizure. Order XXI Rules 46A–46I regulate Garnishee proceedings against third-party debtors.",
    "detailedExplanation": """
<h3>1. Properties Liable to Attachment [Section 60(1) Main Body]</h3>
<p>Lands, houses, goods, money, bank-notes, cheques, bills of exchange, promissory notes, government securities, bonds, debts, and all other saleable property belonging to judgment-debtor over which he has a disposing power.</p>

<h3>2. Properties EXEMPT from Attachment [Proviso to Section 60(1)]</h3>
<p>The following cannot be attached or sold (high-yield exam items):</p>
<ul>
  <li><strong>Clause (a):</strong> Necessary wearing-apparel, cooking vessels, beds and bedding of debtor and family, and personal ornaments of a religious nature (e.g., mangalsutra).</li>
  <li><strong>Clause (b):</strong> Tools of artisans; where debtor is an agriculturist, his implements of husbandry and cattle necessary for farming, and seed-grain.</li>
  <li><strong>Clause (c):</strong> Houses and buildings belonging to and occupied by an <strong>agriculturist, agricultural labourer, or domestic servant</strong>.</li>
  <li><strong>Clause (g):</strong> Stipends and gratuities allowed to pensioners, and political pensions.</li>
  <li><strong>Clause (h):</strong> Wages of labourers and domestic servants, whether payable in money or in kind.</li>
  <li><strong>Clause (m):</strong> An expectancy of succession by survivorship (<em>spes successionis</em>) or other merely contingent or possible right.</li>
  <li><strong>Clause (n):</strong> A right to future maintenance.</li>
</ul>

<h3>3. Statutory Salary Exemption Formula [Section 60(1) Clauses (i) & (ia)]</h3>
<ul>
  <li><strong>In Execution of Maintenance Decrees [Clause (ia)]:</strong>
    <br>One-third (1/3rd) of the salary is exempt; <strong>two-thirds (2/3rds) can be attached</strong>.</li>
  <li><strong>In Execution of ANY OTHER Decrees (Money Decrees) [Clause (i)]:</strong>
    <br>The first <strong>one thousand rupees (Rs. 1,000)</strong> PLUS <strong>two-thirds (2/3rds) of the remainder</strong> is exempt.
    <br><em>Attachment Formula:</em> Attachable amount = <code>[Total Salary - Rs. 1,000] / 3</code>.
    <br><em>24-Month Ceiling:</em> Where salary has been attached continuously for <strong>twenty-four months</strong>, it shall be exempt from further attachment for a period of <strong>twelve months</strong>.</li>
</ul>

<h3>4. Garnishee Orders [Order XXI Rules 46A to 46I]</h3>
<p>A 'Garnishee' is a third person who owes a debt to the judgment-debtor. Inserted in 1976, Rules 46A–46I empower the court to issue a notice to the Garnishee calling upon him either to pay the debt into Court or show cause why he should not do so. If the Garnishee fails to comply, the Court may order execution against him as if it were a decree against him!</p>
""",
    "keyProvisions": [
      {"section": "Section 60", "title": "Property Liable to Attachment and Sale", "description": "Authorizes attachment of debtor's assets, subject to extensive humanitarian exemption proviso."},
      {"section": "Section 60(1)(i)", "title": "Salary Exemption in Money Decrees", "description": "First Rs. 1,000 plus 2/3rd of remainder exempt; max 24 months attachment."},
      {"section": "Section 60(1)(ia)", "title": "Salary Exemption in Maintenance", "description": "1/3rd exempt; 2/3rd attachable."},
      {"section": "Order XXI Rule 46A", "title": "Notice to Garnishee", "description": "Notice to third party owing debt to judgment-debtor to pay into court."}
    ],
    "landmarkCases": [
      {"caseName": "Union of India v. Jyoti Chit Fund & Finance", "year": "1976", "citation": "(1976) 3 SCC 607", "court": "Supreme Court of India", "principle": "Provisions of Section 60 protecting provident fund, pensions, and minimum wages are grounded in public policy to protect subsistence. Parties cannot contract out of Section 60 exemptions."},
      {"caseName": "Appasaheb v. Bhalchandra", "year": "1961", "citation": "AIR 1961 SC 589", "court": "Supreme Court of India", "principle": "An agriculturist under Section 60(1)(b)/(c) means a person who cultivates land personally, not a large-scale absentee landlord."}
    ],
    "comparativeTable": {
      "title": "Salary Attachment: Money Decree vs Maintenance Decree",
      "headers": ["Decree Category", "Exempt Portion", "Attachable Portion", "24-Month Limitation"],
      "rows": [
        ["Ordinary Money Decree [S. 60(1)(i)]", "First Rs. 1,000 + 2/3rd of remainder", "1/3rd of balance above Rs. 1,000", "YES (24 months continuous cap)"],
        ["Maintenance Decree [S. 60(1)(ia)]", "One-third (1/3rd) of salary", "Two-thirds (2/3rds) of salary", "NO (Can continue indefinitely)"]
      ]
    },
    "diagramId": "diag-cpc-execution-framework.svg",
    "diagramExplanation": "Shows attachment mechanics and Section 60 exemptions.",
    "prelimTraps": [
      {"trap": "Confusing salary attachment in maintenance decrees with ordinary money decrees.", "reality": "In maintenance, 2/3rd is ATTACHABLE (only 1/3rd exempt). In money decrees, first Rs. 1,000 + 2/3rd is EXEMPT.", "tip": "Maintenance = 2/3rd ATTACHABLE! Money = 2/3rd EXEMPT!"},
      {"trap": "Thinking a right to future maintenance can be attached by a creditor.", "reality": "Clause (n) of Section 60(1) proviso explicitly exempts a right to future maintenance from attachment.", "tip": "Right to future maintenance CANNOT be attached (S. 60(1)(n))."}
    ],
    "flashcards": [
      {"front": "How much salary can be attached in execution of a maintenance decree under Section 60(1)(ia)?", "back": "Two-thirds (2/3rds) of the salary (1/3rd is exempt).", "category": "Attachment"},
      {"front": "What is a 'Garnishee' under Order XXI Rule 46A?", "back": "A third person who owes a debt to the judgment-debtor, whom the court directs to pay into court.", "category": "Execution"}
    ],
    "sourceReferences": [
      {"title": "Section 60 & Order XXI Rules 46A–46I, Code of Civil Procedure, 1908", "url": "https://www.indiacode.nic.in/handle/123456789/2191"}
    ]
  },

  "top-cpc-12-04": {
    "topicId": "top-cpc-12-04",
    "chapterId": "ch-cpc-12",
    "subjectId": "law-cpc",
    "title": "Objections to Execution (O. XXI R. 58) & Resistance to Delivery (O. XXI R. 97–106)",
    "subtitle": "Order XXI Rule 58 Adjudication (Treated as Suit), R. 97 Resistance & R. 101 All Questions Decided",
    "learningObjective": "Master the adjudication of third-party claims in execution: claim petitions under Order XXI Rule 58 (adjudicated as suits, appealable as decrees) and resistance/dispossession proceedings under Order XXI Rules 97 to 106.",
    "introduction": "When property is attached or delivered, third parties often assert rights. The 1976 amendment radically overhauled Order XXI Rules 58 and 97–106 to eliminate separate suits, requiring the executing court itself to conclusively adjudicate all third-party title disputes.",
    "detailedExplanation": """
<h3>1. Adjudication of Claims to Attached Property [Order XXI Rule 58]</h3>
<p>Where any claim is preferred to, or any objection is made to the attachment of, any property on the ground that such property is not liable to attachment, the Court <strong>shall proceed to adjudicate upon the claim or objection</strong>.</p>
<ul>
  <li><strong>All Questions Determined (Rule 58(2)):</strong> All questions (including questions relating to right, title or interest in property) shall be determined by the executing court and <strong>NOT by a separate suit</strong>.</li>
  <li><strong>Decree Status & Appeal (Rule 58(4)):</strong> Any order made under Rule 58 shall have the <strong>same force and be subject to the same conditions as to appeal as if it were a decree</strong>!</li>
  <li><strong>Refusal to Entertain (Rule 58(1) Proviso):</strong> Court shall NOT entertain claim if property is already sold, or claim is designedly or unnecessarily delayed. (If refused, party can file separate suit under Rule 58(5)).</li>
</ul>

<h3>2. Resistance or Obstruction to Possession [Order XXI Rule 97]</h3>
<p>Where the decree-holder for possession of immovable property or purchaser of sold property is <strong>resisted or obstructed by any person</strong> in obtaining possession, he may make an application to the Court complaining of such resistance.</p>

<h3>3. Complete Determination under Rule 101</h3>
<p>Order XXI Rule 101 is the crown jewel of execution efficiency: <em>'All questions (including questions relating to right, title or interest in the property) arising between the parties to a proceeding on an application under Rule 97 or Rule 99 shall be determined by the Court dealing with the application and <strong>NOT by a separate suit</strong>.'</em></p>

<h3>4. Orders Treated as Decrees [Order XXI Rule 103]</h3>
<p>Every order made under Rule 98 or Rule 100 adjudicating rights of third parties or directing delivery/restoration shall have the <strong>same force and be subject to the same conditions as to appeal as if it were a decree</strong>.</p>
""",
    "keyProvisions": [
      {"section": "Order XXI Rule 58", "title": "Adjudication of Claims to Attached Property", "description": "Complete determination of title; separate suit barred; appealable as decree."},
      {"section": "Order XXI Rule 97", "title": "Resistance or Obstruction to Possession", "description": "Decree-holder/purchaser application complaining of resistance by any person."},
      {"section": "Order XXI Rule 101", "title": "Question to be Determined", "description": "Executing court determines all title/possession questions; separate suit prohibited."},
      {"section": "Order XXI Rule 103", "title": "Orders to be Treated as Decrees", "description": "Orders under Rule 98/100 appealable as regular decrees."}
    ],
    "landmarkCases": [
      {"caseName": "Shreenath v. Rajesh", "year": "1998", "citation": "(1998) 4 SCC 543", "court": "Supreme Court of India", "principle": "Order XXI Rule 97 covers resistance not only by judgment-debtor but by ANY third-party stranger claiming an independent right. Third party need not wait for physical dispossession before moving application."},
      {"caseName": "Brahmdeo Chaudhary v. Rishikesh Prasad Jaiswal", "year": "1997", "citation": "(1997) 3 SCC 694", "court": "Supreme Court of India", "principle": "A third-party stranger in bona fide possession can resist execution at the threshold, and executing court must adjudicate his right under Order XXI Rule 97/101 before using police force to dispossess him."}
    ],
    "comparativeTable": {
      "title": "Claim under Rule 58 vs Resistance under Rule 97",
      "headers": ["Feature", "Claim Petition (Order XXI Rule 58)", "Resistance Application (Order XXI Rule 97)"],
      "rows": [
        ["Stage", "During attachment stage before sale", "During delivery of possession of immovable property"],
        ["Applicant", "Third-party claimant objecting to attachment", "Decree-holder or auction-purchaser complaining of obstruction"],
        ["Separate Suit", "Barred (Rule 58(2))", "Barred (Rule 101)"],
        ["Appellate Status", "Treated as a Decree (Rule 58(4))", "Treated as a Decree (Rule 103)"]
      ]
    },
    "diagramId": "diag-cpc-execution-framework.svg",
    "diagramExplanation": "Shows how Order XXI Rules 58 and 97–106 convert execution objections into deemed trials appealable as decrees.",
    "prelimTraps": [
      {"trap": "Believing a third party dispossessed in execution must file an independent civil suit to recover property.", "reality": "Under Order XXI Rule 99 and 101, third party must apply to executing court; a separate suit is strictly BARRED.", "tip": "Rule 101 bars separate suits; all title decided in execution!"},
      {"trap": "Assuming an order under Order XXI Rule 58 or Rule 103 is an appealable order under Order XLIII.", "reality": "Orders under Rule 58(4) and Rule 103 have the force of a DECREE and are appealable as regular First Appeals under Section 96.", "tip": "O. 21 R. 58 & R. 103 orders = Regular Decrees for appeal!"}
    ],
    "flashcards": [
      {"front": "What is the legal status for appeal of an order passed under Order XXI Rule 58?", "back": "It has the same force and is subject to the same conditions as to appeal as if it were a decree (Rule 58(4)).", "category": "Execution"},
      {"front": "Does a separate suit lie to determine title raised in resistance to possession under Order XXI Rule 97?", "back": "No. Order XXI Rule 101 strictly bars a separate suit; the executing court itself must determine all title questions.", "category": "Execution"}
    ],
    "sourceReferences": [
      {"title": "Order XXI Rules 58 & 97–106, Code of Civil Procedure, 1908", "url": "https://www.indiacode.nic.in/handle/123456789/2191"}
    ]
  },

  "top-cpc-13-01": {
    "topicId": "top-cpc-13-01",
    "chapterId": "ch-cpc-13",
    "subjectId": "law-cpc",
    "title": "Arrest & Attachment Before Judgment under Order XXXVIII (Rules 1–13)",
    "subtitle": "Order XXXVIII Rules 1–4 (Arrest Before Judgment) & Rules 5–13 (Attachment Before Judgment)",
    "learningObjective": "Master the exceptional pre-judgment security mechanisms under Order XXXVIII: arrest before judgment (Rules 1–4) and attachment before judgment (Rules 5–13), conditions, security furnish, and agricultural immunity.",
    "introduction": "To prevent a dishonest defendant from frustrating an anticipated decree by absconding or dissipating his assets during trial, Order XXXVIII empowers the court to order arrest before judgment or attachment before judgment.",
    "detailedExplanation": """
<h3>1. Arrest Before Judgment [Order XXXVIII Rules 1 to 4]</h3>
<p>Where at any stage of a suit (other than suits for immovable property under Section 16), the Court is satisfied by affidavit or otherwise that the defendant:</p>
<ol>
  <li>Has <strong>absconded or left the local limits</strong> of court's jurisdiction; or</li>
  <li>Is about to abscond or leave local limits; or</li>
  <li>Has <strong>disposed of or removed from local limits his property</strong> or any part thereof with intent to delay or obstruct execution; or</li>
  <li>Is about to leave India under circumstances affording reasonable probability of obstructing execution,</li>
</ol>
<p>The Court may issue a warrant to arrest the defendant and bring him before the Court to <strong>show cause why he should not furnish security for his appearance</strong>.</p>
<p><em>Failure to furnish security (Rule 4):</em> Defendant may be committed to civil prison until suit is decided or decree satisfied (maximum 6 months; or 6 weeks if suit value under Rs. 50).</p>

<h3>2. Attachment Before Judgment [Order XXXVIII Rules 5 to 13]</h3>
<p>Where at any stage of a suit the Court is satisfied that defendant, with intent to obstruct or delay execution:</p>
<ol>
  <li>Is about to <strong>dispose of the whole or any part of his property</strong>; or</li>
  <li>Is about to <strong>remove the whole or any part of his property</strong> from the local limits of the Court's jurisdiction,</li>
</ol>
<p>The Court may direct defendant to furnish security in a sum specified, or to produce and place at disposal of Court said property, or to show cause why he should not furnish security (Rule 5(1)).</p>
<p><strong>Attachment of Specific Property (Rule 5(1)):</strong> The court may also in the order direct the <strong>conditional attachment</strong> of the whole or any portion of the property.</p>
<p><strong>VOID ATTACHMENT [Rule 5(4) - Inserted in 1976]:</strong> <em>'If an order of attachment is made without complying with the provisions of sub-rule (1), such attachment shall be VOID.'</em></p>

<h3>3. Key Statutory Protections in Attachment</h3>
<ul>
  <li><strong>Agricultural Produce Immune (Rule 12):</strong> Nothing in this Order shall be deemed to authorize the plaintiff to apply for attachment, or the Court to order the attachment, of any <strong>agricultural produce</strong> in the possession of an agriculturist!</li>
  <li><strong>No Re-attachment Needed (Rule 11):</strong> Where property is under attachment before judgment and a decree is subsequently passed, it is <strong>not necessary to apply for re-attachment</strong> in execution.</li>
  <li><strong>Rights of Strangers Protected (Rule 10):</strong> Attachment before judgment shall not affect the rights of persons not parties to the suit.</li>
</ul>
""",
    "keyProvisions": [
      {"section": "Order XXXVIII Rule 1", "title": "Where Defendant May be Called Upon to Furnish Security for Appearance", "description": "Warrant of arrest before judgment where defendant is absconding or leaving jurisdiction."},
      {"section": "Order XXXVIII Rule 5", "title": "Where Defendant May be Called Upon to Furnish Security for Production of Property", "description": "Attachment before judgment; mandatory compliance under sub-rule (1) otherwise attachment void (sub-rule 4)."},
      {"section": "Order XXXVIII Rule 11", "title": "Property Attached Before Judgment Not to be Re-attached", "description": "No re-attachment required when executing subsequently passed decree."},
      {"section": "Order XXXVIII Rule 12", "title": "Agricultural Produce Not Attachable", "description": "Absolute statutory immunity for agricultural produce in agriculturist's possession."}
    ],
    "landmarkCases": [
      {"caseName": "Raman Tech. & Process Engg. Co. v. Solanki Traders", "year": "2008", "citation": "(2008) 2 SCC 302", "court": "Supreme Court of India", "principle": "Power of attachment before judgment under Order XXXVIII Rule 5 is a drastic and extraordinary power. It must not be exercised mechanically merely because plaintiff has a bona fide case. There must be clear proof that defendant is actively attempting to defeat decree."}
    ],
    "comparativeTable": {
      "title": "Arrest Before Judgment (Rule 1) vs Attachment Before Judgment (Rule 5)",
      "headers": ["Feature", "Arrest Before Judgment (Rule 1)", "Attachment Before Judgment (Rule 5)"],
      "rows": [
        ["Target", "Person of the defendant (Personal appearance)", "Property of the defendant (Securing satisfaction)"],
        ["Excluded Suits", "Cannot be granted in Section 16 immovable property suits", "Can be granted in any suit where property is at risk"],
        ["Primary Object", "To ensure defendant's attendance during proceedings", "To prevent disposal/alienation of assets prior to decree"],
        ["Appealability", "Order under Rule 2, 3 or 6 appealable under O. 43 R. 1(q)", "Order under Rule 2, 3 or 6 appealable under O. 43 R. 1(q)"]
      ]
    },
    "diagramId": "diag-cpc-interim-relief-injunctions.svg",
    "diagramExplanation": "Shows pre-judgment security remedies under Order XXXVIII.",
    "prelimTraps": [
      {"trap": "Thinking agricultural produce can be attached before judgment under Order XXXVIII.", "reality": "Order XXXVIII Rule 12 explicitly prohibits attachment of agricultural produce in possession of an agriculturist.", "tip": "Rule 12: Agricultural produce CANNOT be attached before judgment!"},
      {"trap": "Assuming failure to follow Rule 5(1) procedure is a mere procedural irregularity.", "reality": "Under Order XXXVIII Rule 5(4), attachment made without complying with sub-rule (1) is VOID ab initio.", "tip": "Non-compliance with Rule 5(1) renders attachment VOID!"}
    ],
    "flashcards": [
      {"front": "What is the legal effect of an attachment order passed in violation of Order XXXVIII Rule 5(1)?", "back": "It is completely VOID under Order XXXVIII Rule 5(4).", "category": "Attachment Before Judgment"},
      {"front": "Can agricultural produce of an agriculturist be attached before judgment under Order XXXVIII Rule 12?", "back": "No. Order XXXVIII Rule 12 strictly bars attachment of agricultural produce before judgment.", "category": "Attachment Before Judgment"}
    ],
    "sourceReferences": [
      {"title": "Order XXXVIII, Code of Civil Procedure, 1908", "url": "https://www.indiacode.nic.in/handle/123456789/2191"}
    ]
  },

  "top-cpc-13-02": {
    "topicId": "top-cpc-13-02",
    "chapterId": "ch-cpc-13",
    "subjectId": "law-cpc",
    "title": "Temporary Injunctions under Order XXXIX Rules 1–5: The Triple Test",
    "subtitle": "Order XXXIX Rules 1–5, The Triple Test, 30-Day Rule (R. 3A), Disobedience Penalties (R. 2A)",
    "learningObjective": "Master the law of temporary injunctions under Order XXXIX: grounds under Rule 1, the classic Triple Test, ex parte injunction procedure under Rule 3, the 30-day mandate under Rule 3A, and civil prison penalties for disobedience under Rule 2A.",
    "introduction": "An injunction is a preventive judicial remedy. While perpetual injunctions are governed by the Specific Relief Act, 1963, temporary injunctions are regulated by Order XXXIX of the CPC to maintain the status quo during litigation.",
    "detailedExplanation": """
<h3>1. Cases in which Temporary Injunction May be Granted [Order XXXIX Rule 1]</h3>
<p>Temporary injunction may be granted where it is proved by affidavit or otherwise:</p>
<ol type="a">
  <li>That any property in dispute is in danger of being <strong>wasted, damaged, or alienated</strong> by any party, or wrongfully sold in execution of a decree; or</li>
  <li>That the defendant threatens or intends to <strong>remove or dispose of his property</strong> with a view to defrauding his creditors; or</li>
  <li>That the defendant threatens to <strong>dispossess the plaintiff</strong>, or otherwise cause injury to the plaintiff in relation to any property in dispute.</li>
</ol>

<h3>2. The Inviolable 'Triple Test' for Injunction</h3>
<p>In <em>Dalpat Kumar v. Prahlad Singh (1992) 1 SCC 719</em>, the Supreme Court established that the grant of temporary injunction requires the concurrent existence of three pillars:</p>
<ol>
  <li><strong>Prima Facie Case:</strong> A substantial question raised requiring investigation; plaintiff must show a serious bona fide contention with reasonable prospect of success. (Does not mean proving case conclusively on merits).</li>
  <li><strong>Balance of Convenience:</strong> The comparative mischief or inconvenience likely to arise from withholding the injunction will be greater than that which is likely to arise from granting it.</li>
  <li><strong>Irreparable Injury:</strong> Non-grant would result in an injury that cannot be adequately compensated by monetary damages.</li>
</ol>

<h3>3. Ex Parte Injunctions & Notice Requirement [Order XXXIX Rule 3]</h3>
<p>The Court shall in all cases, before granting an injunction, direct notice of application to opposite party.</p>
<p><strong>Proviso (Ex Parte Injunction):</strong> Where it appears that object of granting injunction would be defeated by delay, Court may grant ex parte injunction, but MUST record reasons and require applicant to:</p>
<ul>
  <li>Deliver or send by registered post copies of application, plaint, affidavit, and documents to defendant <strong>on the day of injunction or immediately next day</strong>; AND</li>
  <li>File an affidavit on the day of injunction or next day stating such delivery/posting was done.</li>
</ul>

<h3>4. Disposal within Thirty Days [Order XXXIX Rule 3A]</h3>
<p>Where an ex parte injunction has been granted without notice, the Court <strong>shall make an endeavor to finally dispose of the application within thirty days</strong> from date of grant.</p>

<h3>5. Disobedience or Breach of Injunction [Order XXXIX Rule 2A]</h3>
<p>In case of disobedience of any injunction or breach of any terms:</p>
<ul>
  <li>The Court may order the property of guilty person to be <strong>attached</strong> (valid for up to one year, after which property may be sold); AND</li>
  <li>May also order such person to be detained in <strong>civil prison for a term not exceeding three months</strong>, unless in the meantime the Court directs his release.</li>
</ul>
""",
    "keyProvisions": [
      {"section": "Order XXXIX Rule 1", "title": "Cases in which Temporary Injunction May be Granted", "description": "Property wasted/damaged/alienated, fraudulent disposal, threat of dispossession."},
      {"section": "Order XXXIX Rule 2A", "title": "Consequence of Disobedience of Injunction", "description": "Attachment of property (up to 1 year) and detention in civil prison up to 3 months."},
      {"section": "Order XXXIX Rule 3", "title": "Notice to Opposite Party", "description": "Ex parte injunction requires recorded reasons, same-day delivery of documents, and affidavit of compliance."},
      {"section": "Order XXXIX Rule 3A", "title": "Court to Dispose of Application within Thirty Days", "description": "Mandatory endeavor to decide ex parte injunction within 30 days."},
      {"section": "Order XXXIX Rule 4", "title": "Order for Injunction may be Discharged, Varied or Set Aside", "description": "Discharge upon false statement, change in circumstances, or undue hardship."}
    ],
    "landmarkCases": [
      {"caseName": "Dalpat Kumar v. Prahlad Singh", "year": "1992", "citation": "(1992) 1 SCC 719", "court": "Supreme Court of India", "principle": "Authoritative articulation of the Triple Test: Prima facie case, balance of convenience, and irreparable injury. Prima facie case alone is not sufficient; irreparable loss must be shown."},
      {"caseName": "Morgan Stanley Mutual Fund v. Kartick Das", "year": "1994", "citation": "(1994) 4 SCC 225", "court": "Supreme Court of India", "principle": "Laid down strict principles governing ex parte injunctions: exceptional urgency, clean hands, full disclosure, and recording of reasons."},
      {"caseName": "Samee Khan v. Bindu Khan", "year": "1998", "citation": "(1998) 7 SCC 59", "court": "Supreme Court of India", "principle": "Under Order XXXIX Rule 2A, the court can simultaneously order attachment of property AND detention in civil prison. Attachment is not a condition precedent for civil imprisonment."}
    ],
    "comparativeTable": {
      "title": "Temporary Injunction (CPC) vs Perpetual Injunction (Specific Relief Act)",
      "headers": ["Feature", "Temporary Injunction (Order XXXIX)", "Perpetual Injunction (SRA 1963 S. 38)"],
      "rows": [
        ["Governing Statute", "Code of Civil Procedure, 1908 (Order XXXIX)", "Specific Relief Act, 1963 (Sections 37 & 38)"],
        ["Stage", "Interlocutory stage at any point during suit", "Only at final disposal by a decree on merits"],
        ["Duration", "Specific time or until further orders of court", "Perpetual; permanently restrains infringement"],
        ["Test", "Triple Test (Prima facie, Balance, Irreparable)", "Established legal right and actual/threatened violation"]
      ]
    },
    "diagramId": "diag-cpc-interim-relief-injunctions.svg",
    "diagramExplanation": "Visualizes the Triple Test, Order XXXIX Rule 3 notice procedure, and Rule 2A disobedience penalties.",
    "prelimTraps": [
      {"trap": "Thinking attachment of property MUST precede civil prison under Order XXXIX Rule 2A.", "reality": "Supreme Court in Samee Khan held that the court can order civil imprisonment directly or alongside attachment.", "tip": "Rule 2A: Civil prison up to 3 months can be ordered directly!"},
      {"trap": "Believing an order rejecting or granting an injunction cannot be appealed.", "reality": "Orders under Order XXXIX Rules 1, 2, 2A, and 4 are APPEALABLE ORDERS under Order XLIII Rule 1(r).", "tip": "Order XXXIX orders are appealable under O. 43 R. 1(r)."}
    ],
    "flashcards": [
      {"front": "What is the maximum period of civil detention for breach of injunction under Order XXXIX Rule 2A?", "back": "A term not exceeding three months.", "category": "Injunctions"},
      {"front": "Within how many days should an ex parte injunction application be disposed of under Order XXXIX Rule 3A?", "back": "Within thirty (30) days from the date on which the injunction was granted.", "category": "Injunctions"}
    ],
    "sourceReferences": [
      {"title": "Order XXXIX Rules 1–5, Code of Civil Procedure, 1908", "url": "https://www.indiacode.nic.in/handle/123456789/2191"}
    ]
  },

  "top-cpc-13-03": {
    "topicId": "top-cpc-13-03",
    "chapterId": "ch-cpc-13",
    "subjectId": "law-cpc",
    "title": "Interlocutory Orders, Receivers (Order XL) & Caveat Petitions (Section 148A)",
    "subtitle": "Order XL Rules 1–5 (Receiver as Court Hand) & Section 148A Caveat (90-Day Validity & Notice)",
    "learningObjective": "Master the law governing Court Receivers under Order XL (appointment on 'just and convenient' standard, powers, duties, immunity) and Caveat Petitions under Section 148A (right to lodge, mandatory notice, 90-day expiry).",
    "introduction": "Order XL and Section 148A provide critical interim protections: appointment of a Receiver as an officer of the court to preserve property pendente lite, and lodging of a Caveat to ensure no ex parte adverse order is passed without hearing.",
    "detailedExplanation": """
<h3>1. Appointment of Receivers [Order XL Rule 1]</h3>
<p>Where it appears to the Court to be <strong>just and convenient</strong>, the Court may by order:</p>
<ol type="a">
  <li>Appoint a receiver of any property, whether before or after decree;</li>
  <li>Remove any person from the possession or custody of the property;</li>
  <li>Commit the same to the custody, possession or management of the receiver; and</li>
  <li>Confer upon the receiver all such powers as to bringing and defending suits, realization and management of property.</li>
</ol>
<p><strong>Limitation (Rule 1(2)):</strong> The Court cannot remove from the possession of property any person whom any party to the suit has <strong>not a present right so to remove</strong>.</p>

<h3>2. Legal Status of a Receiver</h3>
<ul>
  <li>A receiver is an <strong>officer of the Court</strong> and acts as the extended arm (hand) of the court.</li>
  <li>Property in receiver's hands is in <em>custodia legis</em> (custody of the law).</li>
  <li>No suit can be instituted against a receiver without prior <strong>leave of the Court</strong> which appointed him.</li>
  <li>Receiver is personally liable for wilful default or gross negligence causing loss (Rule 3).</li>
</ul>

<h3>3. Caveat Petitions [Section 148A]</h3>
<p>Inserted by 1976 Amendment; where an application is expected to be made, or has been made, in a suit or proceeding instituted, or about to be instituted, in a Court, any person claiming a right to appear before the Court on hearing of such application may <strong>lodge a caveat</strong> in respect thereof.</p>
<ul>
  <li><strong>Duties on Caveat:</strong>
    <ol>
      <li><strong>Caveator's Duty (Sub-sec 2):</strong> Shall serve a copy of the caveat by registered post on the person by whom application has been or is expected to be made.</li>
      <li><strong>Court's Duty (Sub-sec 3):</strong> The Court <strong>shall serve a notice of the application</strong> on the caveator before passing any order.</li>
      <li><strong>Applicant's Duty (Sub-sec 4):</strong> Applicant shall furnish caveator immediately with a copy of the application and all documents.</li>
    </ol>
  </li>
  <li><strong>Duration of Caveat (Sub-sec 5):</strong> A caveat shall <strong>not remain in force after the expiry of ninety days (90 days)</strong> from the date on which it was lodged.</li>
</ul>
""",
    "keyProvisions": [
      {"section": "Order XL Rule 1", "title": "Appointment of Receivers", "description": "Appointment on 'just and convenient' standard; property in custodia legis."},
      {"section": "Section 148A", "title": "Right to Lodge a Caveat", "description": "Lodging caveat against expected application; mandatory notice; expires after 90 days."}
    ],
    "landmarkCases": [
      {"caseName": "Maharwal Khewaji Trust v. Baldev Dass", "year": "2004", "citation": "(2004) 8 SCC 488", "court": "Supreme Court of India", "principle": "Preservation of property in statu quo is the primary duty of the court during pendency of litigation. Receiver or injunction must be granted where waste or alienation is threatened."},
      {"caseName": "C.G.C. Construction Ltd. v. State of West Bengal", "year": "1998", "citation": "AIR 1999 Cal 73", "court": "Calcutta High Court", "principle": "Order passed without issuing notice to caveator when caveat is on file is an infringement of natural justice and is liable to be set aside."}
    ],
    "comparativeTable": {
      "title": "Receiver (Order XL) vs Temporary Injunction (Order XXXIX)",
      "headers": ["Attribute", "Receiver (Order XL)", "Temporary Injunction (Order XXXIX)"],
      "rows": [
        ["Nature of Remedy", "Dispossesses parties; property taken into custodia legis", "Restrains parties from acting; parties retain possession"],
        ["Standard", "'Just and convenient' (Very high threshold)", "Triple Test (Prima facie, Balance, Irreparable loss)"],
        ["Management", "Court officer manages and accounts for income", "Parties manage subject to court negative restraints"],
        ["Appealability", "Appeal lies under Order XLIII Rule 1(s)", "Appeal lies under Order XLIII Rule 1(r)"]
      ]
    },
    "diagramId": "diag-cpc-interim-relief-injunctions.svg",
    "diagramExplanation": "Shows interim remedies including Receiver appointments and Section 148A Caveats.",
    "prelimTraps": [
      {"trap": "Believing a Caveat under Section 148A remains valid until the suit is decided.", "reality": "Section 148A(5) explicitly provides that a caveat expires automatically after NINETY (90) DAYS.", "tip": "Caveat life = 90 DAYS ONLY (S. 148A(5))!"},
      {"trap": "Thinking a suit can be instituted against a Court Receiver without permission.", "reality": "Leave of the appointing Court is a condition precedent for suing a Receiver; suit without leave is liable to be dismissed.", "tip": "Suing a Receiver requires prior court leave."}
    ],
    "flashcards": [
      {"front": "How long does a caveat lodged under Section 148A remain in force?", "back": "Ninety (90) days from the date on which it was lodged.", "category": "Caveat"},
      {"front": "What is the statutory standard for appointing a Receiver under Order XL Rule 1?", "back": "Where it appears to the Court to be 'just and convenient'.", "category": "Receivers"}
    ],
    "sourceReferences": [
      {"title": "Section 148A & Order XL, Code of Civil Procedure, 1908", "url": "https://www.indiacode.nic.in/handle/123456789/2191"}
    ]
  },

  "top-cpc-13-04": {
    "topicId": "top-cpc-13-04",
    "chapterId": "ch-cpc-13",
    "subjectId": "law-cpc",
    "title": "Inherent Powers of Court (Section 151) & Amendments of Decrees (Sections 152–153)",
    "subtitle": "Section 151 Scope, Ends of Justice vs Express Bars & Clerical Corrections (S. 152–153)",
    "learningObjective": "Master the inherent powers of civil courts under Section 151 (ends of justice and abuse of process), the limitations where express provisions exist, and rectification of clerical/arithmetical mistakes under Sections 152 and 153.",
    "introduction": "No code of procedure can foresee every possible contingency. Section 151 saves the inherent powers of civil courts to do substantial justice and prevent abuse of process, while Sections 152 and 153 provide for rectification of accidental slips and clerical errors.",
    "detailedExplanation": """
<h3>1. Inherent Powers Saved, Not Conferred [Section 151]</h3>
<p><em>'Nothing in this Code shall be deemed to limit or otherwise affect the inherent power of the Court to make such orders as may be necessary for the <strong>ends of justice</strong> or to <strong>prevent abuse of the process</strong> of the Court.'</em></p>
<p><strong>Fundamental Jurisprudential Principles:</strong></p>
<ol>
  <li>Section 151 does NOT confer any new power; it merely <strong>saves and recognizes the inherent jurisdiction</strong> that every civil court possesses by virtue of its existence as a court of justice.</li>
  <li><strong>Subordinate to Express Provisions:</strong> Inherent power CANNOT be exercised in conflict with or to override express provisions of the CPC. If the Code prohibits a thing, Section 151 cannot be invoked to permit it.</li>
  <li><strong>Not a Substitute for Appeal/Revision:</strong> Inherent powers cannot be used as an alternative route where a specific statutory remedy (like appeal or review) is available or has been allowed to lapse.</li>
</ol>

<h3>2. The Landmark Manohar Lal Chopra Principles</h3>
<p>In <em>Manohar Lal Chopra v. Rai Bahadur Rao Raja Seth Hiralal (AIR 1962 SC 527)</em>, a four-judge bench settled that civil courts have inherent power to grant temporary injunctions in circumstances not covered by Order XXXIX Rules 1 and 2, provided it does not conflict with any express prohibition.</p>

<h3>3. Correction of Clerical or Arithmetical Errors [Section 152]</h3>
<p>Clerical or arithmetical mistakes in judgments, decrees or orders, or <strong>errors arising therein from any accidental slip or omission</strong> may at any time be corrected by the Court either of its own motion (<strong>suo motu</strong>) or on the application of any of the parties.</p>
<ul>
  <li>Covers ministerial slips, typographic errors, wrong survey numbers or calculation errors.</li>
  <li>Cannot be used to change the substantive decision or reconsider rights of parties on merits.</li>
  <li>Can be done <strong>at any time</strong> (no period of limitation).</li>
</ul>

<h3>4. General Power to Amend [Section 153]</h3>
<p>The Court may at any time, and on such terms as to costs, amend any defect or error in any proceeding in a suit for determining the real question or issue raised.</p>
""",
    "keyProvisions": [
      {"section": "Section 151", "title": "Saving of Inherent Powers of Court", "description": "Saves inherent power for ends of justice or to prevent abuse of process."},
      {"section": "Section 152", "title": "Amendment of Judgments, Decrees or Orders", "description": "Correction of clerical or arithmetical errors arising from accidental slip at any time."},
      {"section": "Section 153", "title": "General Power to Amend", "description": "Plenary power to amend defects in any proceeding to determine real issue."}
    ],
    "landmarkCases": [
      {"caseName": "Manohar Lal Chopra v. Rai Bahadur Rao Raja Seth Hiralal", "year": "1962", "citation": "AIR 1962 SC 527", "court": "Supreme Court of India (Four-Judge Bench)", "principle": "Civil courts have inherent power under Section 151 to grant temporary injunction even outside Order XXXIX, as the Code is not exhaustive. Inherent powers cannot override express statutory prohibitions."},
      {"caseName": "Jayalakshmi Coelho v. Oswald Joseph Coelho", "year": "2001", "citation": "(2001) 4 SCC 181", "court": "Supreme Court of India", "principle": "Section 152 is based on the maxim 'actus curiae neminem gravabit' (an act of the court shall prejudice no man). It is strictly confined to clerical/arithmetical errors or accidental omissions, and cannot be used to modify substantive adjudication."}
    ],
    "comparativeTable": {
      "title": "Section 151 (Inherent Power) vs Section 152 (Rectification)",
      "headers": ["Attribute", "Section 151 (Inherent Powers)", "Section 152 (Clerical Rectification)"],
      "rows": [
        ["Scope", "Broad residual power for ends of justice / abuse of process", "Narrow power restricted to clerical, arithmetical slips"],
        ["Limitation", "Cannot override express provisions of the Code", "Can be exercised 'at any time' without limitation"],
        ["Nature of Power", "Substantive procedural justice", "Ministerial correction of accidental errors"],
        ["Suo Motu Power", "Yes, can be exercised suo motu", "Yes, can be exercised suo motu"]
      ]
    },
    "diagramId": "diag-cpc-civil-trial-sequence",
    "diagramExplanation": "Shows inherent powers and correction mechanisms operating across the judicial lifecycle.",
    "prelimTraps": [
      {"trap": "Believing Section 151 CONFERRED new powers on civil courts for the first time in 1908.", "reality": "Section 151 did NOT confer powers; it merely SAVED inherent powers already inherent in courts of justice.", "tip": "Section 151 SAVES inherent powers, does not confer them!"},
      {"trap": "Assuming an application under Section 152 for correcting a clerical error is subject to a 3-year limitation period.", "reality": "Section 152 explicitly states that clerical corrections may be made 'at any time' without limitation.", "tip": "Section 152: Correction can be done AT ANY TIME!"}
    ],
    "flashcards": [
      {"front": "Does Section 151 confer inherent powers or merely save them?", "back": "It merely saves the pre-existing inherent powers of civil courts; it does not confer new jurisdiction.", "category": "Inherent Powers"},
      {"front": "Under which provision can clerical or arithmetical mistakes in a decree be corrected at any time?", "back": "Section 152 of the CPC.", "category": "Rectification"}
    ],
    "sourceReferences": [
      {"title": "Sections 151–153, Code of Civil Procedure, 1908", "url": "https://www.indiacode.nic.in/handle/123456789/2191"}
    ]
  },

  "top-cpc-14-01": {
    "topicId": "top-cpc-14-01",
    "chapterId": "ch-cpc-14",
    "subjectId": "law-cpc",
    "title": "Death, Marriage & Insolvency of Parties: Abatement & Substitution (Order XXII)",
    "subtitle": "Order XXII Rules 1–12: Survival of Right to Sue, 90-Day Substitution, Abatement & R. 9 Setting Aside",
    "learningObjective": "Master the law of abatement and substitution under Order XXII: survival of right to sue (Rule 1), timelines to bring legal representatives on record (90 days under Article 120), automatic abatement, and setting aside abatement under Rule 9.",
    "introduction": "When a party dies during litigation, the suit does not automatically end. Order XXII regulates the survival of the right to sue, substitution of legal representatives, and the procedural consequences of abatement.",
    "detailedExplanation": """
<h3>1. Survival of Right to Sue [Order XXII Rule 1]</h3>
<p>The death of a plaintiff or defendant shall not cause the suit to abate if the <strong>right to sue survives</strong>. If the right to sue does not survive (e.g., personal actions under the maxim <em>actio personalis moritur cum persona</em>, such as defamation, assault, or divorce), the suit abates immediately.</p>

<h3>2. Substitution of Legal Representatives (Rules 3 & 4)</h3>
<ul>
  <li><strong>Death of Plaintiff (Rule 3):</strong> Where one of two or more plaintiffs dies and right to sue does not survive to surviving plaintiffs alone, or sole plaintiff dies and right survives, the Court, on application made in that behalf, shall cause the <strong>legal representative of the deceased plaintiff to be made a party</strong>.
    <br><em>Time Limit:</em> <strong>Ninety (90) days</strong> from the date of death under Article 120 of the Limitation Act, 1963.
    <br><em>Consequence of Failure:</em> The suit shall <strong>abate so far as the deceased plaintiff is concerned</strong>.</li>
  <li><strong>Death of Defendant (Rule 4):</strong> Legal representatives of deceased defendant must be substituted within 90 days. If no application is made within time, the suit shall <strong>abate as against the deceased defendant</strong>.</li>
</ul>

<h3>3. No Abatement After Conclusion of Hearing [Order XXII Rule 6]</h3>
<p><em>'Notwithstanding anything contained in the foregoing rules, whether the cause of action survives or not, there shall be <strong>no abatement by reason of the death of either party between the conclusion of the hearing and the pronouncing of the judgment</strong>, but judgment may in such case be pronounced notwithstanding the death and shall have the same force and effect as if it had been pronounced before the death took place.'</em></p>

<h3>4. Setting Aside Abatement [Order XXII Rule 9]</h3>
<p>Where a suit abates, <strong>no fresh suit shall be brought</strong> on the same cause of action. The plaintiff or his legal representatives must apply under Rule 9 to <strong>set aside the abatement</strong> within <strong>sixty (60) days</strong> from date of abatement (Article 121, Limitation Act), showing sufficient cause for delay (Section 5 Limitation Act applies).</p>

<h3>5. Exemption: Execution Proceedings [Order XXII Rule 12]</h3>
<p>Order XXII Rule 12 explicitly provides: <em>'Nothing in rules 3, 4 and 8 shall apply to proceedings in <strong>execution of a decree or order</strong>.'</em> Therefore, an execution petition NEVER abates on the death of a decree-holder or judgment-debtor!</p>
""",
    "keyProvisions": [
      {"section": "Order XXII Rule 1", "title": "No Abatement by Party's Death if Right to Sue Survives", "description": "Suit continues if right to sue survives."},
      {"section": "Order XXII Rule 3 & 4", "title": "Procedure in Case of Death of Plaintiff / Defendant", "description": "Substitution of LRs within 90 days; failure causes abatement."},
      {"section": "Order XXII Rule 6", "title": "No Abatement by Reason of Death after Hearing", "description": "Death between conclusion of hearing and judgment does not abate suit."},
      {"section": "Order XXII Rule 9", "title": "Effect of Abatement or Dismissal", "description": "Fresh suit barred; application to set aside abatement on sufficient cause."},
      {"section": "Order XXII Rule 12", "title": "Application of Order to Execution Proceedings", "description": "Rules 3, 4 and 8 do not apply to execution proceedings."}
    ],
    "landmarkCases": [
      {"caseName": "Perumon Bhagvathy Devaswom v. Bhargavi Amma", "year": "2008", "citation": "(2008) 8 SCC 321", "court": "Supreme Court of India", "principle": "Laid down principles for condoning delay and setting aside abatement under Order XXII Rule 9. Abatement is automatic on expiry of 90 days, but courts should adopt a liberal approach to advance substantial justice."},
      {"caseName": "Sardar Amarjit Singh Kalra v. Pramod Gupta", "year": "2003", "citation": "(2003) 3 SCC 272", "court": "Supreme Court of India (Constitution Bench)", "principle": "In land acquisition or joint claims, death of one claimant does not abate the entire appeal if interests are distinct and separate."}
    ],
    "comparativeTable": {
      "title": "Timelines Governing Abatement (Order XXII & Limitation Act)",
      "headers": ["Stage", "Governing Provision", "Limitation Period", "Starting Point"],
      "rows": [
        ["Substitution of LRs", "O. XXII R. 3/4 & Art. 120", "Ninety (90) Days", "Date of death of plaintiff/defendant"],
        ["Automatic Abatement", "O. XXII R. 3(2)/4(3)", "Occurs on 91st day", "Automatic operation of law"],
        ["Setting Aside Abatement", "O. XXII R. 9 & Art. 121", "Sixty (60) Days", "From date of abatement (91st day after death)"],
        ["Condonation of Delay", "Section 5 Limitation Act", "Discretionary on cause", "After expiry of 60 days"]
      ]
    },
    "diagramId": "diag-cpc-civil-trial-sequence",
    "diagramExplanation": "Shows how Order XXII intervenes when party death occurs during trial.",
    "prelimTraps": [
      {"trap": "Thinking execution proceedings abate if judgment-debtor dies and LRs are not brought on record within 90 days.", "reality": "Order XXII Rule 12 explicitly provides that Rules 3 and 4 do NOT apply to execution proceedings. Execution never abates!", "tip": "Rule 12: Execution proceedings NEVER abate!"},
      {"trap": "Believing a suit abates if a party dies two days after arguments are concluded but before judgment.", "reality": "Under Order XXII Rule 6, there is NO ABATEMENT if death occurs between conclusion of hearing and pronouncement of judgment.", "tip": "Death after hearing concludes = No abatement (O. 22 R. 6)!"}
    ],
    "flashcards": [
      {"front": "Within how many days must an application to bring legal representatives on record be filed?", "back": "Within ninety (90) days from the date of death (Article 120, Limitation Act).", "category": "Abatement"},
      {"front": "Do the abatement rules in Order XXII apply to execution proceedings?", "back": "No. Order XXII Rule 12 expressly exempts execution proceedings from Rules 3, 4, and 8.", "category": "Abatement"}
    ],
    "sourceReferences": [
      {"title": "Order XXII, Code of Civil Procedure, 1908", "url": "https://www.indiacode.nic.in/handle/123456789/2191"}
    ]
  },

  "top-cpc-14-02": {
    "topicId": "top-cpc-14-02",
    "chapterId": "ch-cpc-14",
    "subjectId": "law-cpc",
    "title": "Withdrawal of Suits (Order XXIII Rule 1) & Lawful Compromise (O. XXIII R. 3)",
    "subtitle": "Order XXIII Rule 1 (Absolute vs Qualified Withdrawal), Rule 3 Lawful Compromise & Rule 3A Bar",
    "learningObjective": "Master the rules on withdrawal of suits under Order XXIII Rule 1 (distinguishing unconditional abandonment from withdrawal with leave for formal defects) and compromise of suits under Rule 3, including the bar on fresh suits under Rule 3A.",
    "introduction": "Litigation may terminate without a full trial if the plaintiff withdraws the suit or parties reach a settlement. Order XXIII regulates withdrawal and adjustment of suits, guarding against abuse and ensuring compromises are lawful.",
    "detailedExplanation": """
<h3>1. Withdrawal of Suit or Abandonment of Claim [Order XXIII Rule 1]</h3>
<ul>
  <li><strong>Absolute Withdrawal [Rule 1(1) & 1(4)]:</strong> The plaintiff may at any stage of a suit abandon his suit or abandon a part of his claim without leave of court.
    <br><em>Consequence (Rule 1(4)):</em> The plaintiff shall be liable for costs and shall be <strong>PRECLUDED from instituting any fresh suit</strong> in respect of such subject-matter or such part of the claim!</li>
  <li><strong>Qualified Withdrawal with Leave to Sue Freshly [Rule 1(3)]:</strong> Where the Court is satisfied:
    <ol type="a">
      <li>That a suit must fail by reason of some <strong>formal defect</strong> (e.g., misjoinder, failure to issue statutory notice under S. 80, deficit court-fee); or</li>
      <li>That there are <strong>sufficient grounds</strong> for allowing plaintiff to institute a fresh suit,</li>
    </ol>
    The Court may grant the plaintiff permission to withdraw with <strong>liberty to institute a fresh suit</strong> in respect of the same subject-matter.</li>
  <li><strong>Limitation Not Extended (Rule 2):</strong> Any fresh suit instituted on permission shall be governed by the law of limitation in the same manner as if the first suit had not been instituted!</li>
</ul>

<h3>2. Compromise of Suit [Order XXIII Rule 3]</h3>
<p>Where it is proved to the satisfaction of the Court that a suit has been adjusted wholly or in part by any <strong>lawful agreement or compromise in writing and signed by the parties</strong>, the Court shall order such agreement, compromise or satisfaction to be recorded, and shall pass a <strong>compromise decree</strong> in accordance therewith so far as it relates to the parties to the suit.</p>
<p><em>Explanation:</em> An agreement or compromise which is void or voidable under the Indian Contract Act, 1872 (e.g., fraud, coercion, unlawful object) shall NOT be deemed to be lawful.</p>

<h3>3. No Appeal from Consent Decree & Bar on Fresh Suit</h3>
<ul>
  <li><strong>Section 96(3):</strong> <em>'No appeal shall lie from a decree passed by the Court with the consent of parties.'</em></li>
  <li><strong>Bar on Fresh Suit [Order XXIII Rule 3A]:</strong> <em>'No suit shall lie to set aside a decree on the ground that the compromise on which the decree is based was not lawful.'</em></li>
  <li><strong>Remedy:</strong> The sole remedy of a party alleging the compromise was unlawful or fraudulent is to apply to the <strong>same court which passed the compromise decree</strong> to recall it (<em>Banwari Lal v. Chando Devi</em>).</li>
</ul>
""",
    "keyProvisions": [
      {"section": "Order XXIII Rule 1(1)", "title": "Withdrawal of Suit or Abandonment of Part of Claim", "description": "Absolute withdrawal bars fresh suit on same subject matter (Rule 1(4))."},
      {"section": "Order XXIII Rule 1(3)", "title": "Permission to Withdraw with Liberty for Fresh Suit", "description": "Leave granted only for formal defect or other sufficient grounds."},
      {"section": "Order XXIII Rule 3", "title": "Compromise of Suit", "description": "Lawful compromise in writing and signed by parties; compromise decree passed."},
      {"section": "Order XXIII Rule 3A", "title": "Bar to Suit to Set Aside Compromise Decree", "description": "No separate suit lies to set aside compromise decree on ground that it was not lawful."},
      {"section": "Section 96(3)", "title": "No Appeal from Consent Decree", "description": "Consent decrees cannot be appealed."}
    ],
    "landmarkCases": [
      {"caseName": "Banwari Lal v. Chando Devi", "year": "1993", "citation": "(1993) 1 SCC 581", "court": "Supreme Court of India", "principle": "A party challenging a compromise decree on the ground of fraud or illegality cannot file a separate suit due to Order XXIII Rule 3A. He must approach the very court which recorded the compromise under Section 151."},
      {"caseName": "K.S. Bhoopathy v. Kokila", "year": "2000", "citation": "(2000) 5 SCC 458", "court": "Supreme Court of India", "principle": "Court cannot grant leave to withdraw with liberty to sue freshly under Rule 1(3) merely to enable a plaintiff to defeat a valuable right accrued to defendant or to cure defects on merits. 'Formal defect' means technical defects not affecting merits."}
    ],
    "comparativeTable": {
      "title": "Withdrawal under Rule 1(1) vs Withdrawal under Rule 1(3)",
      "headers": ["Feature", "Unconditional Withdrawal (Rule 1(1))", "Withdrawal with Liberty (Rule 1(3))"],
      "rows": [
        ["Leave of Court", "No leave required; unilateral right of plaintiff", "Court permission and judicial satisfaction mandatory"],
        ["Grounds", "Any reason; plaintiff simply abandons claim", "Strictly formal defect or analogous sufficient ground"],
        ["Right to Sue Freshly", "ABSOLUTELY BARRED (Rule 1(4))", "PRESERVED; plaintiff can file fresh suit"],
        ["Costs", "Plaintiff normally ordered to pay defendant's costs", "Subject to terms as to costs imposed by court"]
      ]
    },
    "diagramId": "diag-cpc-civil-trial-sequence",
    "diagramExplanation": "Shows alternative pre-trial exits via withdrawal or compromise under Order XXIII.",
    "prelimTraps": [
      {"trap": "Assuming an independent civil suit can be filed to set aside a fraudulent compromise decree.", "reality": "Order XXIII Rule 3A strictly BARS a separate suit to set aside a compromise decree.", "tip": "Rule 3A bars independent suit; apply to SAME court to recall decree!"},
      {"trap": "Thinking an oral compromise stated before the Judge is sufficient under Order XXIII Rule 3.", "reality": "Order XXIII Rule 3 strictly requires the compromise to be 'IN WRITING AND SIGNED BY THE PARTIES'.", "tip": "Compromise must be in writing and signed (O. 23 R. 3)!"}
    ],
    "flashcards": [
      {"front": "Can an independent suit be filed to set aside a compromise decree on ground of fraud under Order XXIII Rule 3A?", "back": "No. Order XXIII Rule 3A expressly bars a separate suit; the party must apply to the court that passed the decree.", "category": "Compromise"},
      {"front": "Does Section 96(3) permit an appeal against a consent decree passed under Order XXIII Rule 3?", "back": "No. Section 96(3) strictly bars any appeal from a consent decree.", "category": "Appeals"}
    ],
    "sourceReferences": [
      {"title": "Order XXIII & Section 96(3), Code of Civil Procedure, 1908", "url": "https://www.indiacode.nic.in/handle/123456789/2191"}
    ]
  }
}

def generate_file():
    code = '''/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Civil Procedure Code Module — Authored Concepts (Part 2: Ch 8 to 14)
 * Topics: top-cpc-08-01 to top-cpc-14-02 (19 Comprehensive Authoritative Topics)
 */

(function (global) {
  'use strict';

  const DATA = ''' + json.dumps(TOPICS_PART2, indent=2) + ''';

  global.CPC_CONCEPTS_PART2 = DATA;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = DATA;
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
'''
    with open('assets/learning/data/cpc/cpc-concepts-part2.js', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Wrote assets/learning/data/cpc/cpc-concepts-part2.js with 19 topics.")

if __name__ == '__main__':
    generate_file()
