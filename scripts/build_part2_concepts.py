# -*- coding: utf-8 -*-
"""
Generates assets/learning/data/constitution/constitution-concepts-part2.js
Covers Chapter 6 (Fundamental Rights), Chapter 7 (DPSP), Chapter 8 (Fundamental Duties) - 11 topics.
"""
import json
import os

out_path = r"C:\Users\tauqe\Documents\Tanveer_Ashraf_Judicial\assets\learning\data\constitution\constitution-concepts-part2.js"

data = {}

# ----------------------------------------------------
# CHAPTER 6: FUNDAMENTAL RIGHTS
# ----------------------------------------------------

# TOPIC 1: Articles 12 & 13
data['top-const-06-01'] = {
    'topicId': 'top-const-06-01',
    'chapterId': 'ch-06',
    'title': 'Concept of Fundamental Rights, Definition of "State" & Judicial Review',
    'subtitle': 'Articles 12 & 13: The Shield of Part III, Severability & Doctrine of Eclipse',
    'articleRef': 'Articles 12 and 13',
    'learningObjective': 'Analyze the scope of "State" under Article 12 and master the foundational doctrines of constitutional review under Article 13.',
    'detailedExplanation': """
<h3>1. The Framework of Part III</h3>
<p>Part III of the Constitution (Articles 12 to 35) is rightfully described as the <strong>Magna Carta of India</strong>. Fundamental Rights operate as limitations on state power, securing civil liberties and political democracy. They are justifiable and directly enforceable against the "State" under Article 32.</p>

<h3>2. Article 12: Definition of "State"</h3>
<p>For the purpose of Part III, unless the context otherwise requires, the "State" includes:</p>
<ol>
  <li>The Government and Parliament of India (Central executive and legislature).</li>
  <li>The Government and the Legislature of each of the States.</li>
  <li>All local authorities within the territory of India or under the control of the Government of India (Municipalities, Panchayats, District Boards, Improvement Trusts).</li>
  <li><strong>"Other authorities":</strong> The critical expanding frontier of Article 12.</li>
</ol>
<h4>Evolution of "Other Authorities":</h4>
<ul>
  <li><em>Early restrictive test:</em> In <em>University of Madras v. Santa Bai (1954)</em>, applied ejusdem generis (only bodies performing governmental/sovereign functions). Rejected in <em>Ujjammabai (1962)</em>.</li>
  <li><em>The Instrumentality Test:</em> In <strong>R.D. Shetty v. International Airport Authority (1979)</strong> and <strong>Ajay Hasia v. Khalid Mujib (1981)</strong>, Justice P.N. Bhagwati formulated the 6-factor test:
    <ol>
      <li>Entire share capital held by the Government.</li>
      <li>Deep and pervasive State control.</li>
      <li>Monopoly status conferred or protected by the State.</li>
      <li>Extensive financial assistance meeting almost entire expenditure.</li>
      <li>Functions of the corporation of public importance closely related to governmental functions.</li>
      <li>Department of Government transferred to a corporation.</li>
    </ol>
  </li>
  <li><em>Refinement:</em> In <strong>Pradeep Kumar Biswas v. Indian Institute of Chemical Biology (2002 5 SCC 111)</strong>, a 7-Judge bench held that the body must be financially, functionally, and administratively dominated by or under the pervasive control of the Government. CSIR was held to be State.</li>
  <li><em>BCCI:</em> In <em>Zee Telefilms v. UOI (2005)</em>, BCCI was held NOT to be "State" under Art. 12, though amenable to writ jurisdiction under Art. 226 for public duties.</li>
  <li><em>Is Judiciary a "State"?</em> While performing administrative functions (appointments, rule-making), the judiciary IS State; while performing adjudicatory judicial functions, a judicial order cannot be challenged under Art. 32 as violating Fundamental Rights (<em>Naresh Shridhar Mirajkar v. State of Maharashtra, 1967</em>).</li>
</ul>

<h3>3. Article 13: Laws Inconsistent with Fundamental Rights</h3>
<p>Article 13 provides the constitutional teeth for <strong>Judicial Review</strong>:</p>
<ul>
  <li><strong>Article 13(1) [Pre-Constitutional Laws]:</strong> Laws in force before Jan 26, 1950, to the extent of inconsistency with FRs, become void from the date of commencement of the Constitution (void ab initio not applied; operates prospectively).
    <ul>
      <li><strong>Doctrine of Eclipse:</strong> A pre-constitutional law violating an FR is not dead; it remains dormant or shadowed by the FR. If a constitutional amendment removes the inconsistency, the law becomes active and enforceable again without re-enactment (<em>Bhikaji Narain Dhakras v. State of M.P., 1955</em>).</li>
    </ul>
  </li>
  <li><strong>Article 13(2) [Post-Constitutional Laws]:</strong> The State shall not make any law which takes away or abridges the rights conferred by Part III; any law made in contravention shall, to the extent of contravention, be <strong>void ab initio</strong> (a still-born law, <em>Deep Chand v. State of U.P., 1959</em>).
    <ul>
      <li><strong>Doctrine of Severability:</strong> If an unconstitutional provision can be cleanly severed from the valid portions without altering the fundamental intent of the legislature, only the invalid part is struck down; the rest remains valid (<em>A.K. Gopalan, 1950</em>; <em>R.M.D.C. v. UOI, 1957</em>).</li>
    </ul>
  </li>
  <li><strong>Doctrine of Waiver:</strong> In <em>Basheshar Nath v. CIT (AIR 1959 SC 149)</em>, the Supreme Court held that an Indian citizen <strong>CANNOT waive</strong> any Fundamental Right, because FRs are enacted not merely for individual benefit but as public policy for the welfare of the entire community.</li>
  <li><strong>Article 13(3):</strong> Defines "Law" broadly to include Ordinance, order, bye-law, rule, regulation, notification, custom, or usage having the force of law.</li>
  <li><strong>Article 13(4):</strong> Inserted by the 24th Amendment, 1971: <em>Nothing in this article shall apply to any amendment of this Constitution made under article 368.</em> (Upheld in Kesavananda Bharati, subject to the Basic Structure doctrine).</li>
</ul>
""",
    'quickRevisionPoints': [
        'Part III is the Magna Carta of India (Articles 12 to 35).',
        'Article 12: "State" includes Union, States, local authorities, and "other authorities".',
        'Ajay Hasia & Pradeep Kumar Biswas established the test of deep and pervasive state control for "other authorities".',
        'Judiciary in its judicial capacity is NOT State for Art. 32 petitions (Naresh Mirajkar).',
        'Article 13 provides the bedrock for Judicial Review.',
        'Doctrine of Eclipse applies to pre-constitutional laws (Bhikaji Narain).',
        'Doctrine of Severability: only unconstitutional sections are void if severable (RMDC case).',
        'Doctrine of Waiver does NOT apply in India; citizens cannot waive Fundamental Rights (Basheshar Nath).'
    ],
    'provisions': [
        {'provision': 'Article 12', 'title': 'Definition of State', 'description': 'Delimits entities against which Fundamental Rights are enforceable.'},
        {'provision': 'Article 13(1)', 'title': 'Pre-Constitutional Laws', 'description': 'Inconsistent pre-1950 laws are void to the extent of inconsistency.'},
        {'provision': 'Article 13(2)', 'title': 'Post-Constitutional Laws', 'description': 'Prohibits State from enacting laws abridging Fundamental Rights.'},
        {'provision': 'Article 13(4)', 'title': 'Constitutional Amendments', 'description': 'Exempts Article 368 amendments from Article 13 scrutiny (subject to Basic Structure).'}
    ],
    'definitions': [
        {'term': 'Doctrine of Eclipse', 'definition': 'The legal principle that pre-constitutional laws violating Fundamental Rights remain dormant/overshadowed, and revive automatically if the constitutional obstacle is removed.'},
        {'term': 'Doctrine of Severability', 'definition': 'The rule that if an invalid provision can be excised from a statute without defeating the legislative intent, only the invalid clause is declared void while the remainder survives.'},
        {'term': 'Doctrine of Waiver', 'definition': 'The intentional relinquishment of a known legal right, which the Supreme Court ruled is inapplicable to Fundamental Rights in India.'}
    ],
    'ingredients': [
        'Entity satisfies the deep and pervasive control test under Article 12.',
        'Impugned enactment falls within the expansive definition of "law" under Article 13(3).',
        'Violation of a specific guarantee enshrined in Part III.'
    ],
    'exceptions': [
        'A purely private body without government funding or statutory duty is not "State" under Article 12.',
        'Article 13 does not apply to personal laws (State of Bombay v. Narasu Appa Mali).'
    ],
    'examples': [
        {'scenario': 'A nationalised bank terminates an employee without an inquiry in violation of natural justice.', 'application': 'Maintainable under Article 32/226, because nationalised banks fulfill the Ajay Hasia criteria and constitute "State" under Article 12.'},
        {'scenario': 'A citizen signs an agreement with the tax department agreeing to waive his Article 14 rights in exchange for settling an audit.', 'application': 'The agreement is void ab initio under the Basheshar Nath doctrine, because Fundamental Rights cannot be waived by private contract.'}
    ],
    'landmarkCases': [
        {'case': 'Ajay Hasia v. Khalid Mujib', 'citation': '(1981) 1 SCC 722', 'year': '1981', 'bench': '5-Judge Bench (Bhagwati J)', 'ratio': 'Formulated the authoritative 6-factor test to determine whether a corporation or society is an instrumentality of State under Article 12.', 'impact': 'Expanded the reach of fundamental rights to public corporations.'},
        {'case': 'Pradeep Kumar Biswas v. Indian Institute of Chemical Biology', 'citation': '(2002) 5 SCC 111', 'year': '2002', 'bench': '7-Judge Bench (Ruma Pal J)', 'ratio': 'Overruled Sabhajit Tewary (1975). Held that CSIR is "State" under Art. 12 because it is financially, functionally, and administratively dominated by the Government.', 'impact': 'Settled the definitive contemporary test of Article 12.'},
        {'case': 'Basheshar Nath v. CIT', 'citation': 'AIR 1959 SC 149', 'year': '1959', 'bench': '5-Judge Bench', 'ratio': 'Held that the doctrine of waiver does not apply to Fundamental Rights in India.', 'impact': 'Shielded citizens from coercive waivers of constitutional protections.'},
        {'case': 'Bhikaji Narain Dhakras v. State of M.P.', 'citation': 'AIR 1955 SC 781', 'year': '1955', 'bench': 'Constitution Bench (Das CJ)', 'ratio': 'Laid down the Doctrine of Eclipse regarding pre-constitutional motor transport legislation.', 'impact': 'Established the revival mechanism for eclipsed laws.'}
    ],
    'comparisonTables': [
        {
            'title': 'Pre-Constitutional vs Post-Constitutional Invalidation (Art. 13)',
            'headers': ['Aspect', 'Article 13(1) Pre-Constitutional', 'Article 13(2) Post-Constitutional'],
            'rows': [
                ['Enactment Date', 'Before 26 January 1950', 'On or after 26 January 1950'],
                ['Legal Status', 'Valid when enacted; becomes dormant', 'Void ab initio (still-born)'],
                ['Applicable Doctrine', 'Doctrine of Eclipse applies', 'Eclipse does not apply (Deep Chand)'],
                ['Effect of Amendment', 'Revives automatically without re-enactment', 'Must be freshly re-enacted by legislature']
            ]
        }
    ],
    'diagramId': 'diag-article12-tree',
    'diagramExplanation': 'The hierarchy charts the four branches of Article 12, culminating in the 6-factor Ajay Hasia test for other authorities.',
    'misconceptions': [
        {'myth': 'The Board of Control for Cricket in India (BCCI) is "State" under Article 12.', 'reality': 'The Supreme Court in Zee Telefilms (2005) held BCCI is NOT "State" under Article 12 because it receives no state finance or state monopoly.'},
        {'myth': 'Judicial decrees of a court can be challenged as violating Fundamental Rights under Article 32.', 'reality': 'In Naresh Mirajkar (1967), the Supreme Court ruled that judicial decisions of superior courts cannot be challenged under Article 32.'}
    ],
    'prelimTraps': [
        {'trap': 'Can an Indian citizen waive his Fundamental Right to Equality under Article 14?', 'reality': 'NO. In Basheshar Nath (1959), the Supreme Court ruled that NO Fundamental Right can be waived by any person in India.', 'rule': 'No waiver of FRs in India.'},
        {'trap': 'Does the Doctrine of Eclipse apply to post-constitutional laws?', 'reality': 'Generally NO. The Supreme Court in Deep Chand (1959) and Mahendra Lal Jain (1963) held that post-constitutional laws violating Part III are dead from birth and cannot be eclipsed.', 'rule': 'Eclipse = Pre-constitutional laws.'}
    ],
    'flashcards': [
        {'id': 'fc-06-01', 'front': 'Which article defines "State" for the purposes of Part III?', 'back': 'Article 12.', 'category': 'Constitutional Articles'},
        {'id': 'fc-06-02', 'front': 'What is the Doctrine of Eclipse?', 'back': 'A pre-constitutional law violating an FR remains dormant and revives if the constitutional hurdle is removed (Bhikaji Narain).', 'category': 'Judicial Doctrines'},
        {'id': 'fc-06-03', 'front': 'Which landmark case held that citizens cannot waive their Fundamental Rights?', 'back': 'Basheshar Nath v. CIT (AIR 1959 SC 149).', 'category': 'Landmark Precedents'},
        {'id': 'fc-06-04', 'front': 'Are personal laws included within the definition of "law" under Article 13?', 'back': 'Held NO in State of Bombay v. Narasu Appa Mali (AIR 1952 Bom 84).', 'category': 'Legal Scope'}
    ],
    'sourceReferences': [
        {'title': 'Ajay Hasia v. Khalid Mujib (1981) 1 SCC 722', 'url': 'https://main.sci.gov.in'},
        {'title': 'Pradeep Kumar Biswas v. IICB (2002) 5 SCC 111', 'url': 'https://main.sci.gov.in'}
    ]
}

# TOPIC 2: Articles 14–18 (Right to Equality)
data['top-const-06-02'] = {
    'topicId': 'top-const-06-02',
    'chapterId': 'ch-06',
    'title': 'Right to Equality (Articles 14–18)',
    'subtitle': 'Equality Before Law, Non-Discrimination, Affirmative Action & Abolition of Untouchability',
    'articleRef': 'Articles 14, 15, 16, 17, 18',
    'learningObjective': 'Master the dual concepts in Article 14, the classical vs new doctrine of equality, affirmative action jurisprudence in Articles 15 and 16, and the abolition of untouchability and titles.',
    'detailedExplanation': """
<h3>1. Article 14: The General Principle of Equality</h3>
<p>Article 14 declares: <em>"The State shall not deny to any person equality before the law or the equal protection of the laws within the territory of India."</em></p>
<ul>
  <li>Applicable to <strong>all persons</strong> (citizens as well as non-citizens, natural persons as well as legal persons such as statutory corporations and companies).</li>
  <li><strong>Equality Before the Law (Negative Concept, UK origin):</strong> Absence of special privilege; all persons subject to ordinary law administered by ordinary courts; no person is above the law.</li>
  <li><strong>Equal Protection of the Laws (Positive Concept, 14th Amendment USA origin):</strong> Equality of treatment under equal circumstances; like should be treated alike, not that unlike should be treated alike.</li>
  <li><strong>The Old Test: Reasonable Classification:</strong> Formulated in <em>State of West Bengal v. Anwar Ali Sarkar (1952)</em>. Article 14 forbids class legislation, but permits reasonable classification, provided two conditions are satisfied:
    <ol>
      <li>Classification must be founded on an <strong>intelligible differentia</strong> which distinguishes persons grouped together from others left out.</li>
      <li>The differentia must have a <strong>rational nexus</strong> to the object sought to be achieved by the statute.</li>
    </ol>
  </li>
  <li><strong>The New Dynamic Concept: Arbitrariness Doctrine:</strong> In <em>E.P. Royappa v. State of Tamil Nadu (1974 4 SCC 3)</em>, Justice P.N. Bhagwati propounded: <em>"Equality is a dynamic concept with many aspects and dimensions and it cannot be 'cribbed, cabined and confined' within traditional and doctrinaire limits. Equality and arbitrariness are sworn enemies; one belongs to the rule of law in a republic while the other, to the whim and caprice of an absolute monarch. Where an act is arbitrary, it is implicit in it that it is unequal both according to political logic and constitutional law and therefore violative of Art. 14."</em> Reaffirmed in <em>Maneka Gandhi (1978)</em> and <em>Shayara Bano (2017)</em> (striking down Triple Talaq for manifest arbitrariness).</li>
</ul>

<h3>2. Article 15: Prohibition of Discrimination</h3>
<ul>
  <li><strong>Article 15(1):</strong> State shall not discriminate against any <strong>citizen</strong> on grounds <strong>ONLY of religion, race, caste, sex, place of birth or any of them</strong>.</li>
  <li><strong>Article 15(2):</strong> Horizontal application: No citizen shall, on grounds only of religion, race, caste, sex, place of birth, be subject to disability regarding access to shops, restaurants, public wells, tanks, roads.</li>
  <li><strong>Exceptions (Protective Discrimination):</strong>
    <ul>
      <li><em>15(3):</em> Special provisions for <strong>women and children</strong> (maternity leaves, free education).</li>
      <li><em>15(4) [1st Amendment 1951, post-Champakam Dorairajan]:</em> Special provisions for advancement of <strong>Socially and Educationally Backward Classes (SEBCs) or SCs and STs</strong>.</li>
      <li><em>15(5) [93rd Amendment 2005]:</em> Reservations in educational institutions (aided or unaided, private or public), except minority educational institutions.</li>
      <li><em>15(6) [103rd Amendment 2019]:</em> Up to 10% reservation for <strong>Economically Weaker Sections (EWS)</strong> of citizens other than SC/ST/OBC (upheld in <em>Janhit Abhiyan v. UOI, 2022</em>).</li>
    </ul>
  </li>
</ul>

<h3>3. Article 16: Equality of Opportunity in Public Employment</h3>
<ul>
  <li><strong>16(1) & (2):</strong> Equality of opportunity for all citizens; no discrimination on grounds <strong>only of religion, race, caste, sex, descent, place of birth, residence or any of them</strong> (note: "descent" and "residence" are additional grounds absent in Art. 15).</li>
  <li><strong>16(3):</strong> Parliament may prescribe <strong>residence requirements</strong> within a State for certain employment (State legislatures cannot do so).</li>
  <li><strong>16(4):</strong> Reservation for any backward class of citizens which, in the opinion of the State, is <strong>not adequately represented</strong> in the services under the State.</li>
  <li><strong>The Landmark: Indra Sawhney v. Union of India (1992 Supp 3 SCC 217) [Mandal Case]:</strong>
    <ol>
      <li>Upheld 27% quota for OBCs.</li>
      <li>Backward classes can be identified primarily on the basis of caste.</li>
      <li><strong>Creamy Layer</strong> must be excluded from backward classes.</li>
      <li>Reservation is confined to initial appointments only, NOT in promotions.</li>
      <li>Total reservations should not exceed <strong>50%</strong> of available seats, except in extraordinary situations.</li>
      <li>"Carry forward rule" is valid provided it does not breach the 50% ceiling in any year.</li>
    </ol>
  </li>
  <li><strong>Constitutional Amendments Post-Indra Sawhney:</strong>
    <ul>
      <li><em>77th Amendment 1995:</em> Added Art. 16(4A) allowing reservation in promotion for SCs and STs.</li>
      <li><em>81st Amendment 2000:</em> Added Art. 16(4B) creating an exception to the 50% ceiling for unfilled backlog vacancies.</li>
      <li><em>85th Amendment 2001:</em> Consequential seniority for SC/ST promotions. (Upheld in <em>M. Nagaraj v. UOI, 2006</em> and modified in <em>Jarnail Singh v. Lachhmi Narain Gupta, 2018</em>).</li>
      <li><em>103rd Amendment 2019:</em> Added Art. 16(6) providing up to 10% reservation for EWS in civil posts.</li>
    </ul>
  </li>
</ul>

<h3>4. Articles 17 and 18: Social Emancipation</h3>
<ul>
  <li><strong>Article 17 (Abolition of Untouchability):</strong> Absolute right enforceable against the world at large (State and private individuals). Untouchability is abolished and its practice in any form is forbidden. Enforced through the <em>Protection of Civil Rights Act, 1955</em>.</li>
  <li><strong>Article 18 (Abolition of Titles):</strong> Prohibits State from conferring titles, except military or academic distinctions. Prohibits citizens from accepting foreign titles without Presidential consent. In <em>Balaji Raghavan v. UOI (1996 1 SCC 361)</em>, National Awards (Bharat Ratna, Padma awards) were held valid as decorational honours, but cannot be used as prefixes or suffixes to names.</li>
</ul>
""",
    'quickRevisionPoints': [
        'Article 14 guarantees Equality before law (UK) and Equal protection of laws (USA) to ALL persons.',
        'Reasonable classification requires intelligible differentia and rational nexus (Anwar Ali Sarkar).',
        'Royappa & Maneka Gandhi propounded that non-arbitrariness is the core essence of Article 14.',
        'Article 15 prohibits discrimination against CITIZENS on grounds ONLY of religion, race, caste, sex, place of birth.',
        'Article 16 guarantees equality in public employment; adds "descent" and "residence" to prohibited grounds.',
        'Indra Sawhney (1992): 50% cap on reservations, creamy layer exclusion, no reservation in promotions under 16(4).',
        'Article 17 is an absolute right abolishing untouchability; enforceable against private individuals.',
        'Article 18 abolishes titles; National Awards (Bharat Ratna) are valid but cannot be used as titles (Balaji Raghavan).'
    ],
    'provisions': [
        {'provision': 'Article 14', 'title': 'Equality Before Law', 'description': 'Equal protection and non-arbitrariness for all persons.'},
        {'provision': 'Article 15(4) & (5)', 'title': 'Educational Affirmative Action', 'description': 'Special provisions for SEBCs, SCs, STs in state institutions and admissions.'},
        {'provision': 'Article 16(4)', 'title': 'Public Service Reservations', 'description': 'Representation of inadequately represented backward classes in state services.'},
        {'provision': 'Article 17', 'title': 'Abolition of Untouchability', 'description': 'Absolute constitutional abolition and penalization of untouchability.'}
    ],
    'definitions': [
        {'term': 'Intelligible Differentia', 'definition': 'A distinct and comprehensible characteristic that clearly differentiates persons or objects grouped together from those excluded.'},
        {'term': 'Creamy Layer', 'definition': 'The socially, economically, and educationally advanced stratum of backward classes disqualified from claiming reservation benefits (Indra Sawhney).'},
        {'term': 'Manifest Arbitrariness', 'definition': 'A statutory enactment or executive measure passed capriciously, irrationally, or without adequate determining principle, violative of Article 14 (Shayara Bano).' }
    ],
    'ingredients': [
        'Classification based on clear intelligible differentiating criteria.',
        'Direct rational nexus between the classification and legislative object.',
        'Absence of manifest arbitrariness and hostile discrimination.'
    ],
    'exceptions': [
        'Articles 15(3), 15(4), 15(5), 15(6) and 16(4), 16(4A), 16(6) operate as constitutionally permitted affirmative action exceptions to formal equality.',
        'Foreign diplomats and rulers enjoy judicial immunity under international law, functioning as an exception to Article 14.'
    ],
    'examples': [
        {'scenario': 'A state government provides special free coaching programs exclusively for girl students in public schools.', 'application': 'Completely valid under Article 15(3), which expressly empowers the State to make special provisions for women and children.'},
        {'scenario': 'A recipient of the Padma Shri uses the title "Padma Shri" as a prefix on his legal letterhead.', 'application': 'Violates the undertaking required pursuant to Balaji Raghavan (1996); the awards are not titles under Article 18 and cannot be used as prefixes or suffixes.'}
    ],
    'landmarkCases': [
        {'case': 'Indra Sawhney v. Union of India', 'citation': '(1992) Supp 3 SCC 217', 'year': '1992', 'bench': '9-Judge Bench', 'ratio': 'Authoritative ruling on reservations: 50% cap, exclusion of creamy layer, backwardness identified by caste, no reservation in promotions under Art. 16(4).', 'impact': 'Settled the constitutional framework of affirmative action in India.'},
        {'case': 'E.P. Royappa v. State of Tamil Nadu', 'citation': '(1974) 4 SCC 3', 'year': '1974', 'bench': '5-Judge Bench (Bhagwati J)', 'ratio': 'Laid down the "new doctrine of equality": equality is antithetical to arbitrariness.', 'impact': 'Radically expanded the protective umbrella of Article 14.'},
        {'case': 'Janhit Abhiyan v. Union of India', 'citation': '(2023) 5 SCC 1', 'year': '2022', 'bench': '5-Judge Bench (3:2 majority)', 'ratio': 'Upheld the constitutional validity of the 103rd Amendment Act, 2019 providing 10% reservation to Economically Weaker Sections (EWS).', 'impact': 'Recognized economic status as an independent criterion for affirmative action.'},
        {'case': 'Shayara Bano v. Union of India', 'citation': '(2017) 9 SCC 1', 'year': '2017', 'bench': '5-Judge Bench', 'ratio': 'Set aside the practice of Talaq-e-Biddat (Triple Talaq) as manifestly arbitrary and violative of Article 14.', 'impact': 'Elevated manifest arbitrariness as a ground to strike down primary legislation.'}
    ],
    'comparisonTables': [
        {
            'title': 'Prohibited Grounds of Discrimination: Art. 15 vs Art. 16',
            'headers': ['Ground', 'Article 15 (5 Grounds)', 'Article 16 (7 Grounds)'],
            'rows': [
                ['Religion', 'Prohibited', 'Prohibited'],
                ['Race', 'Prohibited', 'Prohibited'],
                ['Caste', 'Prohibited', 'Prohibited'],
                ['Sex', 'Prohibited', 'Prohibited'],
                ['Place of Birth', 'Prohibited', 'Prohibited'],
                ['Descent', 'NOT explicitly mentioned', 'Prohibited'],
                ['Residence', 'NOT explicitly mentioned', 'Prohibited (subject to Parliament law under 16(3))']
            ]
        }
    ],
    'diagramId': 'diag-equality-matrix',
    'diagramExplanation': 'The matrix contrasts the general equality code under Article 14 with the specific non-discrimination and affirmative action provisions in Articles 15 to 18.',
    'misconceptions': [
        {'myth': 'Article 14 prohibits the State from classifying people for legislative purposes.', 'reality': 'Article 14 prohibits class legislation, but permits reasonable classification based on intelligible differentia with a rational nexus.'},
        {'myth': 'State Legislatures can pass a law requiring that state government jobs be reserved for state residents.', 'reality': 'Under Article 16(3), ONLY Parliament has the power to prescribe residence qualifications for public employment; State Legislatures cannot do so.'}
    ],
    'prelimTraps': [
        {'trap': 'To whom is Article 14 available: citizens only or any person?', 'reality': 'Article 14 applies to "any person" (citizens and non-citizens alike). Articles 15, 16, and 19 apply ONLY to citizens.', 'rule': '14, 20, 21, 21A, 22, 23, 24, 25, 26, 27, 28 = Any person. 15, 16, 19, 29, 30 = Citizens only.'},
        {'trap': 'Additional grounds in Article 16 absent in Article 15.', 'reality': 'Descent and Residence.', 'rule': 'Article 16 has 7 grounds; Article 15 has 5 grounds.'}
    ],
    'flashcards': [
        {'id': 'fc-06-05', 'front': 'Which case established the "New Doctrine of Equality" based on non-arbitrariness?', 'back': 'E.P. Royappa v. State of Tamil Nadu (1974).', 'category': 'Judicial Doctrines'},
        {'id': 'fc-06-06', 'front': 'What was the ceiling on total reservations fixed in Indra Sawhney (1992)?', 'back': '50%, barring extraordinary situations in far-flung remote areas.', 'category': 'Reservation Quotas'},
        {'id': 'fc-06-07', 'front': 'Which article of the Constitution completely abolishes untouchability?', 'back': 'Article 17 (absolute right).', 'category': 'Constitutional Articles'},
        {'id': 'fc-06-08', 'front': 'Can Bharat Ratna or Padma Vibhushan be used as titles prefixed to names?', 'back': 'No, held unconstitutional in Balaji Raghavan v. UOI (1996).', 'category': 'Titles & Awards'}
    ],
    'sourceReferences': [
        {'title': 'Indra Sawhney v. Union of India, 1992 Supp 3 SCC 217', 'url': 'https://main.sci.gov.in'},
        {'title': 'E.P. Royappa v. State of Tamil Nadu (1974) 4 SCC 3', 'url': 'https://main.sci.gov.in'}
    ]
}

print("Part 2 Topics 1 & 2 complete.")

# TOPIC 3: Articles 19 & 20
data['top-const-06-03'] = {
    'topicId': 'top-const-06-03',
    'chapterId': 'ch-06',
    'title': 'Right to Freedom & Protection in Respect of Conviction (Articles 19–20)',
    'subtitle': 'The Six Democratic Freedoms, Reasonable Restrictions & Triple Protections of Art. 20',
    'articleRef': 'Articles 19 and 20',
    'learningObjective': 'Master the six fundamental freedoms under Article 19(1), their exhaustive reasonable restrictions, and the triple constitutional protections against ex-post facto laws, double jeopardy, and self-incrimination under Article 20.',
    'detailedExplanation': """
<h3>1. Article 19: The Six Democratic Freedoms</h3>
<p>Article 19(1) guarantees to all <strong>citizens</strong> (not non-citizens or corporations) six basic democratic freedoms:</p>
<ol type="a">
  <li>Freedom of speech and expression;</li>
  <li>Freedom to assemble peaceably and without arms;</li>
  <li>Freedom to form associations or unions or co-operative societies (co-operatives added by 97th Amendment 2011);</li>
  <li>Freedom to move freely throughout the territory of India;</li>
  <li>Freedom to reside and settle in any part of the territory of India;</li>
  <li><em>[Omitted]:</em> Right to acquire, hold and dispose of property was repealed by the <strong>44th Constitutional Amendment Act, 1978</strong> and relocated as a constitutional right under Article 300A;</li>
  <li>Freedom to practise any profession, or to carry on any occupation, trade or business.</li>
</ol>

<h3>2. The Test of "Reasonable Restrictions" under Clauses (2) to (6)</h3>
<p>The freedoms under Article 19 are not absolute. They can be restricted ONLY on grounds specifically enumerated in clauses (2) to (6):</p>
<ul>
  <li><strong>Article 19(2) Grounds [Speech & Expression]:</strong> Sovereignty and integrity of India, security of the State, friendly relations with foreign States, public order, decency or morality, contempt of court, defamation, or incitement to an offence. ("Public order" and "incitement to an offence" added by 1st Amendment 1951; "sovereignty and integrity" added by 16th Amendment 1963).</li>
  <li><strong>Doctrine of Proportionality (Modern Test):</strong> Formulated in <em>Modern Dental College (2016)</em> and <em>K.S. Puttaswamy (2017)</em>: The restriction must pursue a legitimate state aim, have a rational nexus to the goal, be the least restrictive means, and balance the societal benefit against the right infringed.</li>
  <li><strong>Freedom of Press:</strong> Not explicitly mentioned, but held to be implicitly included within the freedom of speech and expression (<em>Romesh Thappar v. State of Madras, 1950</em>; <em>Indian Express Newspapers v. UOI, 1985</em>).</li>
  <li><strong>Right to Strike:</strong> There is NO fundamental right to strike or call a bandh under Article 19(1)(c) (<em>TK Rangarajan v. Govt of T.N., 2003</em>).</li>
</ul>

<h3>3. Article 20: Protection in Respect of Conviction for Offences</h3>
<p>Article 20 provides three absolute procedural safeguards available to <strong>all persons</strong> (citizens and foreigners):</p>
<ol>
  <li><strong>Protection Against Ex-Post Facto Laws (Article 20(1)):</strong>
    <ul>
      <li>No person shall be convicted of any offence except for violation of a law in force at the time of the commission of the act.</li>
      <li>No person shall be subjected to a penalty greater than that which might have been inflicted under the law in force at the time of the commission of the act (<em>Kedar Nath v. State of West Bengal, 1953</em>).</li>
      <li><em>Rule:</em> Applies only to <strong>criminal laws</strong>, not to civil liability or tax laws. Beneficial retroactive amendments (reduction of punishment) can be extended to an accused (<em>Rattan Lal v. State of Punjab, 1965</em>).</li>
    </ul>
  </li>
  <li><strong>Protection Against Double Jeopardy (Article 20(2)):</strong>
    <ul>
      <li><em>"No person shall be prosecuted and punished for the same offence more than once."</em> (Based on the maxim <em>nemo debet bis vexari</em>).</li>
      <li>Requires BOTH <strong>prosecution AND punishment</strong> before a court of law or judicial tribunal. Departmental proceedings or administrative disciplinary actions followed by criminal prosecution do NOT violate Article 20(2) (<em>Maqbool Hussain v. State of Bombay, 1953</em>; <em>S.A. Venkataraman v. UOI, 1954</em>).</li>
    </ul>
  </li>
  <li><strong>Protection Against Self-Incrimination (Article 20(3)):</strong>
    <ul>
      <li><em>"No person accused of any offence shall be compelled to be a witness against himself."</em> (Based on <em>nemo tenetur seipsum accusare</em>).</li>
      <li>Requires: (1) Person accused of an offence; (2) Compulsion; (3) To give testimony against oneself.</li>
      <li>In <strong>State of Bombay v. Kathi Kalu Oghad (1961)</strong>, an 11-Judge bench held that giving thumb impressions, specimen handwriting, or physical measurements does not violate Art. 20(3), as it does not convey personal knowledge.</li>
      <li>In <strong>Selvi v. State of Karnataka (2010 7 SCC 263)</strong>, the Supreme Court held that involuntary administration of <strong>narco-analysis, polygraph tests, and brain-mapping</strong> violates Article 20(3) and Article 21.</li>
    </ul>
  </li>
</ol>
""",
    'quickRevisionPoints': [
        'Article 19 guarantees 6 freedoms to CITIZENS only (Right to property was omitted by 44th Amendment 1978).',
        'Freedoms can be restricted ONLY on grounds exhaustively listed in clauses (2) to (6).',
        'Freedom of Press is implicit in Article 19(1)(a) (Romesh Thappar).',
        'Article 20(1): Protection against retrospective criminal laws (ex-post facto).',
        'Article 20(2): Double jeopardy requires both prosecution and punishment before a judicial court (Maqbool Hussain).',
        'Article 20(3): Self-incrimination; involuntary narco-analysis and lie-detector tests are unconstitutional (Selvi).',
        'Articles 20 and 21 can NEVER be suspended, even during a National Emergency under Article 352 (44th Amendment).'
    ],
    'provisions': [
        {'provision': 'Article 19(1)(a)', 'title': 'Speech & Expression', 'description': 'Freedom of speech, press, and information.'},
        {'provision': 'Article 20(1)', 'title': 'Ex-Post Facto Law', 'description': 'Prohibition on retroactive penal sanctions.'},
        {'provision': 'Article 20(2)', 'title': 'Double Jeopardy', 'description': 'Bar on successive prosecution and punishment for the same offence.'},
        {'provision': 'Article 20(3)', 'title': 'Self-Incrimination', 'description': 'Protection against compelled testimony.'}
    ],
    'definitions': [
        {'term': 'Ex-Post Facto Law', 'definition': 'A law that retrospectively criminalizes an act that was innocent when performed or enhances the penalty for a past act.'},
        {'term': 'Double Jeopardy', 'definition': 'Constitutional protection ensuring a person is not put in legal peril of life or liberty more than once for the same offence.'}
    ],
    'ingredients': [
        'Citizen status for Article 19 claims.',
        'Reasonable restriction anchored strictly in the permissible grounds of clauses (2) to (6).',
        'Criminal accusation and element of compulsion for Article 20(3) protection.'
    ],
    'exceptions': [
        'Article 20(1) does not bar retrospective civil or tax liabilities (only penal laws).',
        'Departmental or administrative inquiries do not bar subsequent criminal trials under Article 20(2).'
    ],
    'examples': [
        {'scenario': 'A civil servant is dismissed from service by a departmental tribunal for bribery, and subsequently prosecuted in a criminal court for corruption under the Prevention of Corruption Act.', 'application': 'Lawful. Departmental punishment is not a judicial punishment; hence prosecution in court does not constitute double jeopardy under Article 20(2) (S.A. Venkataraman v. UOI).'},
        {'scenario': 'Police forcibly administer sodium pentothal (narco-analysis) to an accused to extract a confession.', 'application': 'Unconstitutional. Involuntary narco-analysis violates the right against self-incrimination under Article 20(3) and right to privacy under Article 21 (Selvi v. State of Karnataka).'}
    ],
    'landmarkCases': [
        {'case': 'Selvi v. State of Karnataka', 'citation': '(2010) 7 SCC 263', 'year': '2010', 'bench': '3-Judge Bench (Balakrishnan CJ)', 'ratio': 'Held that involuntary administration of narco-analysis, polygraph test, and BEAP (brain electrical activation profile) violates Article 20(3) and Article 21.', 'impact': 'Landmark shield for cognitive privacy and bodily integrity.'},
        {'case': 'State of Bombay v. Kathi Kalu Oghad', 'citation': 'AIR 1961 SC 1808', 'year': '1961', 'bench': '11-Judge Bench', 'ratio': 'Distinguished giving personal testimony from providing physical evidence. Held that taking fingerprints, signature, or handwriting specimens does not violate Article 20(3).', 'impact': 'Core precedent on forensic evidence.'},
        {'case': 'Shreya Singhal v. Union of India', 'citation': '(2015) 5 SCC 1', 'year': '2015', 'bench': '2-Judge Bench (Nariman J)', 'ratio': 'Struck down Section 66A of the Information Technology Act, 2000 as an unconstitutionally vague and overbroad restriction on free speech under Article 19(1)(a).', 'impact': 'Landmark ruling on digital free speech.'}
    ],
    'comparisonTables': [
        {
            'title': 'The Triple Protections of Article 20',
            'headers': ['Clause', 'Doctrine', 'Applicable Field', 'Key Landmark Ruling'],
            'rows': [
                ['Art. 20(1)', 'No Ex-Post Facto Law', 'Criminal laws only (not civil/tax)', 'Kedar Nath v. State of W.B. (1953)'],
                ['Art. 20(2)', 'No Double Jeopardy', 'Judicial trials (not departmental)', 'Maqbool Hussain v. State of Bombay (1953)'],
                ['Art. 20(3)', 'No Self-Incrimination', 'Accused persons against compulsion', 'Selvi v. State of Karnataka (2010)']
            ]
        }
    ],
    'diagramId': 'diag-article20-protections',
    'diagramExplanation': 'The schematic breaks down Article 20 into its three constitutional bastions: retrospective penal shield, double jeopardy barrier, and self-incrimination shield.',
    'misconceptions': [
        {'myth': 'Article 19(1)(a) explicitly mentions freedom of the press.', 'reality': 'Freedom of the press is NOT explicitly mentioned; it is implied within freedom of speech and expression (Romesh Thappar).'},
        {'myth': 'Article 20 can be suspended during a National Emergency.', 'reality': 'Articles 20 and 21 can NEVER be suspended under any circumstances, even during a National Emergency (44th Amendment Act, 1978).'}
    ],
    'prelimTraps': [
        {'trap': 'Does double jeopardy apply if an accused is acquitted in the first trial and prosecuted again?', 'reality': 'Article 20(2) requires that the person was "prosecuted AND punished". However, Section 300 of the CrPC/BNSS protects against second trials after acquittal as well.', 'rule': 'Constitutional protection Art. 20(2) requires both prosecution and punishment.'},
        {'trap': 'Can retrospective civil taxation be challenged under Article 20(1)?', 'reality': 'NO. Article 20(1) applies exclusively to criminal/penal offences, not to civil taxation or contract laws.', 'rule': 'Art. 20(1) = Criminal only.'}
    ],
    'flashcards': [
        {'id': 'fc-06-09', 'front': 'Which amendment omitted the Right to Property from Article 19(1)(f)?', 'back': 'The 44th Constitutional Amendment Act, 1978 (relocated to Article 300A).', 'category': 'Amendments'},
        {'id': 'fc-06-10', 'front': 'Which two Fundamental Rights cannot be suspended even during a National Emergency?', 'back': 'Articles 20 and 21 (guaranteed by the 44th Amendment Act, 1978).', 'category': 'Emergency Provisions'},
        {'id': 'fc-06-11', 'front': 'Which landmark case held that involuntary narco-analysis violates Article 20(3)?', 'back': 'Selvi v. State of Karnataka (2010).', 'category': 'Landmark Precedents'},
        {'id': 'fc-06-12', 'front': 'Does departmental disciplinary punishment bar criminal prosecution under Article 20(2)?', 'back': 'No, departmental inquiry is not a judicial trial before a court (S.A. Venkataraman case).', 'category': 'Double Jeopardy'}
    ],
    'sourceReferences': [
        {'title': 'Selvi v. State of Karnataka (2010) 7 SCC 263', 'url': 'https://main.sci.gov.in'},
        {'title': 'Shreya Singhal v. Union of India (2015) 5 SCC 1', 'url': 'https://main.sci.gov.in'}
    ]
}

# TOPIC 4: Articles 21, 21A & 22
data['top-const-06-04'] = {
    'topicId': 'top-const-06-04',
    'chapterId': 'ch-06',
    'title': 'Right to Life, Personal Liberty & Education (Articles 21, 21A & 22)',
    'subtitle': 'Evolution from A.K. Gopalan to Maneka Gandhi, Right to Privacy & Preventive Detention',
    'articleRef': 'Articles 21, 21A, 22',
    'learningObjective': 'Trace the revolutionary expansion of Article 21 from formalistic procedure to substantive due process, the Golden Triangle doctrine, and analyze preventive detention safeguards.',
    'detailedExplanation': """
<h3>1. The Evolution of Article 21: From Gopalan to Maneka Gandhi</h3>
<p>Article 21 declares: <em>"No person shall be deprived of his life or personal liberty except according to procedure established by law."</em></p>
<ul>
  <li><strong>The Narrow Era: A.K. Gopalan v. State of Madras (AIR 1950 SC 27):</strong> The Supreme Court gave a formalistic, pedantic reading. Held that "procedure established by law" meant any law enacted by the legislature, even if unjust or harsh; courts could not examine its substantive fairness. Held that Articles 19, 21, and 22 were watertight, mutually exclusive compartments (the "silo" approach).</li>
  <li><strong>The Watershed Overruling: Maneka Gandhi v. Union of India ((1978) 1 SCC 248):</strong>
    <ul>
      <li>Overruled A.K. Gopalan completely.</li>
      <li>Held that the procedure depriving a person of life or personal liberty must be <strong>"just, fair and reasonable"</strong>, not arbitrary, fanciful, or oppressive. This effectively imported the American doctrine of <strong>Substantive Due Process</strong> into Indian jurisprudence.</li>
      <li><strong>The Golden Triangle:</strong> Articles 14, 19, and 21 are not mutually exclusive; they form a trinity or golden triangle. A law depriving personal liberty under Art. 21 must also satisfy the non-arbitrariness test of Art. 14 and the reasonable restrictions test of Art. 19.</li>
    </ul>
  </li>
</ul>

<h3>2. The Expansive Horizon: Implied Rights under Article 21</h3>
<p>Through dynamic judicial activism, the Supreme Court has interpreted "Life" as meaning something more than mere animal existence; it encompasses life with human dignity (<em>Francis Coralie Mullin, 1981</em>):</p>
<ul>
  <li><strong>Right to Privacy:</strong> Declared a fundamental right protected intrinsically under Article 21 by a unanimous 9-Judge bench in <em>K.S. Puttaswamy v. Union of India (2017 10 SCC 1)</em>, overruling <em>M.P. Sharma (1954)</em> and <em>Kharak Singh (1962)</em>.</li>
  <li><strong>Right to Clean Environment:</strong> Subhash Kumar v. State of Bihar (1991), M.C. Mehta cases.</li>
  <li><strong>Right to Livelihood:</strong> Olga Tellis v. Bombay Municipal Corporation (1985).</li>
  <li><strong>Right to Speedy Trial:</strong> Hussainara Khatoon v. Home Secretary, State of Bihar (1979).</li>
  <li><strong>Right to Free Legal Aid:</strong> M.H. Hoskot v. State of Maharashtra (1978).</li>
  <li><strong>Right to Die with Dignity (Passive Euthanasia):</strong> Common Cause v. UOI (2018) recognized Living Wills.</li>
  <li><strong>Decriminalization of Consensual Adult Homosexuality:</strong> Navtej Singh Johar v. UOI (2018).</li>
</ul>

<h3>3. Article 21A: Right to Education</h3>
<p>Inserted by the <strong>86th Constitutional Amendment Act, 2002</strong>:</p>
<ul>
  <li>The State shall provide <strong>free and compulsory education to all children of the age of 6 to 14 years</strong> in such manner as the State may determine.</li>
  <li>Enforced through the <em>Right of Children to Free and Compulsory Education (RTE) Act, 2009</em> (effective from April 1, 2010).</li>
  <li>Precursor: <em>Mohini Jain (1992)</em> and <em>Unni Krishnan v. State of A.P. (1993)</em> which held that the right to education flowed directly from Article 21.</li>
</ul>

<h3>4. Article 22: Safeguards in Punitive and Preventive Detention</h3>
<p>Article 22 operates in two distinct parts:</p>
<h4>A. Punitive Detention (Ordinary Arrests - Clauses 1 & 2):</h4>
<ol>
  <li>Right to be informed of the grounds of arrest as soon as may be.</li>
  <li>Right to consult and be defended by a legal practitioner of one's choice.</li>
  <li>Right to be produced before the nearest magistrate within <strong>24 hours of arrest</strong> (excluding travel time).</li>
  <li>Right not to be detained beyond 24 hours without the authority of a magistrate.</li>
  <li><em>Exceptions:</em> These safeguards do NOT apply to enemy aliens or persons arrested under preventive detention laws.</li>
</ol>
<h4>B. Preventive Detention (Detention without Trial - Clauses 3 to 7):</h4>
<ul>
  <li>Detention intended to prevent a person from committing an offence in the future.</li>
  <li>Maximum detention without review: <strong>3 months</strong> (the 44th Amendment 1978 reduced this to 2 months, but that specific clause has not yet been brought into administrative force by notification).</li>
  <li>Advisory Board comprising persons qualified to be High Court judges must report whether there is sufficient cause for detention beyond 3 months.</li>
  <li>Detenu must be informed of the grounds of detention as soon as possible, except facts which the authority considers against public interest to disclose.</li>
  <li>Detenu must be afforded the earliest opportunity of making a representation against the detention order.</li>
</ul>
""",
    'quickRevisionPoints': [
        'A.K. Gopalan (1950) adopted a narrow literal view of "procedure established by law".',
        'Maneka Gandhi (1978) established that procedure must be "just, fair, and reasonable" (substantive due process).',
        'Golden Triangle: Articles 14, 19, and 21 are mutually reinforcing.',
        'Right to Privacy declared a fundamental right under Art. 21 in K.S. Puttaswamy (2017) (9-Judge Bench).',
        'Article 21A: Free and compulsory education for children aged 6 to 14 (86th Amendment, 2002).',
        'Article 22(2): Mandatory production of arrested person before magistrate within 24 hours.',
        'Article 22(4): Maximum preventive detention period without Advisory Board confirmation is 3 months.'
    ],
    'provisions': [
        {'provision': 'Article 21', 'title': 'Right to Life & Liberty', 'description': 'No deprivation except according to just, fair, and reasonable procedure.'},
        {'provision': 'Article 21A', 'title': 'Right to Education', 'description': 'Free and compulsory education for children between 6 and 14 years.'},
        {'provision': 'Article 22(2)', 'title': 'Magistrate Production', 'description': '24-hour mandatory production safeguard.'},
        {'provision': 'Article 22(4)', 'title': 'Advisory Board Review', 'description': 'Limits preventive detention without Advisory Board review.'}
    ],
    'definitions': [
        {'term': 'Procedure Established by Law', 'definition': 'The constitutional phrase in Article 21, interpreted post-Maneka Gandhi to require procedural fairness, natural justice, and non-arbitrariness.'},
        {'term': 'Preventive Detention', 'definition': 'Detention of a person without trial and without conviction by a court, undertaken preemptively to prevent anticipated prejudicial acts affecting state security or public order.'}
    ],
    'ingredients': [
        'Deprivation of life or personal liberty.',
        'Existence of an enacted valid statutory law.',
        'Fair, just, and reasonable procedural mechanism conforming to natural justice.'
    ],
    'exceptions': [
        'The 24-hour production rule under Article 22(2) does not apply to enemy aliens or persons detained under preventive detention laws.'
    ],
    'examples': [
        {'scenario': 'Police arrest a suspect on Friday evening and do not produce him before a magistrate until Tuesday afternoon.', 'application': 'Gross violation of Article 22(2) and Section 57 CrPC/BNSS; detention beyond 24 hours without judicial warrant is illegal.'},
        {'scenario': 'A state passes a statute providing that undertrials can be chained during transit without judicial permission.', 'application': 'Unconstitutional under Article 21, as routine handcuffing without judicial permission violates human dignity (Prem Shankar Shukla v. Delhi Administration, 1980).'}
    ],
    'landmarkCases': [
        {'case': 'Maneka Gandhi v. Union of India', 'citation': '(1978) 1 SCC 248', 'year': '1978', 'bench': '7-Judge Bench (Beg CJ)', 'ratio': 'Procedure depriving liberty must be right, just, and fair. Established the Golden Triangle connecting Articles 14, 19, and 21.', 'impact': 'Transformational foundation of modern Indian human rights jurisprudence.'},
        {'case': 'K.S. Puttaswamy v. Union of India', 'citation': '(2017) 10 SCC 1', 'year': '2017', 'bench': '9-Judge Bench (Khehar CJ)', 'ratio': 'Unanimously declared that the Right to Privacy is an intrinsic part of the right to life and personal liberty under Article 21.', 'impact': 'Overruled M.P. Sharma (1954) and Kharak Singh (1962).'},
        {'case': 'Hussainara Khatoon v. Home Secretary, State of Bihar', 'citation': '(1980) 1 SCC 81', 'year': '1979', 'bench': 'Bhagwati J', 'ratio': 'Held that the right to a speedy trial is an inalienable component of fundamental rights under Article 21.', 'impact': 'Led to the release of thousands of undertrial prisoners.'}
    ],
    'comparisonTables': [
        {
            'title': 'A.K. Gopalan (1950) vs Maneka Gandhi (1978)',
            'headers': ['Dimension', 'A.K. Gopalan (1950)', 'Maneka Gandhi (1978)'],
            'rows': [
                ['Concept of Law', 'Strict positive legislative enactment', 'Just, fair, and reasonable procedure'],
                ['Substantive Due Process', 'Rejected (literal procedure established)', 'Effectively incorporated into Art. 21'],
                ['Relationship of FRs', 'Mutually exclusive watertight silos', 'Golden Triangle (Arts. 14, 19, 21 interwoven)'],
                ['Personal Liberty', 'Narrow bodily freedom from restraint', 'Wide umbrella covering human dignity']
            ]
        }
    ],
    'diagramId': 'diag-golden-triangle',
    'diagramExplanation': 'The visual illuminates the Golden Triangle: an equilateral linkage between Article 14 (Equality), Article 19 (Freedom), and Article 21 (Life and Liberty).',
    'misconceptions': [
        {'myth': 'The Right to Privacy was introduced into the Constitution through an amendment.', 'reality': 'Privacy was not added by amendment; it was recognized by judicial interpretation of Article 21 by a 9-Judge bench in Puttaswamy (2017).'},
        {'myth': 'Preventive detention is permitted only during wars or emergencies.', 'reality': 'India is one of the few democracies where preventive detention is sanctioned by the Constitution during normal peacetime under Article 22.'}
    ],
    'prelimTraps': [
        {'trap': 'Age bracket under Article 21A for free and compulsory education.', 'reality': '6 to 14 years (NOT 0 to 6 years, which is covered under DPSP Article 45).', 'rule': 'Art. 21A = 6 to 14 years; Art. 45 = early childhood care below 6 years.'},
        {'trap': 'Maximum period for which a person can be detained under preventive detention without Advisory Board approval.', 'reality': '3 months (as currently notified in force under Article 22(4)).', 'rule': 'Preventive detention = 3 months.'}
    ],
    'flashcards': [
        {'id': 'fc-06-13', 'front': 'Which case propounded the "Golden Triangle" doctrine of Articles 14, 19, and 21?', 'back': 'Maneka Gandhi v. Union of India (1978).', 'category': 'Constitutional Doctrines'},
        {'id': 'fc-06-14', 'front': 'Which amendment inserted Article 21A (Right to Education)?', 'back': 'The 86th Constitutional Amendment Act, 2002.', 'category': 'Amendments'},
        {'id': 'fc-06-15', 'front': 'Which landmark 9-judge bench declared Right to Privacy as a fundamental right?', 'back': 'Justice K.S. Puttaswamy (Retd.) v. Union of India (2017).', 'category': 'Landmark Rulings'},
        {'id': 'fc-06-16', 'front': 'Within how many hours must an arrested person be produced before a magistrate?', 'back': '24 hours, excluding travel time (Article 22(2)).', 'category': 'Procedural Safeguards'}
    ],
    'sourceReferences': [
        {'title': 'Maneka Gandhi v. Union of India (1978) 1 SCC 248', 'url': 'https://main.sci.gov.in'},
        {'title': 'K.S. Puttaswamy v. Union of India (2017) 10 SCC 1', 'url': 'https://main.sci.gov.in'}
    ]
}

# TOPIC 5: Articles 23–28
data['top-const-06-05'] = {
    'topicId': 'top-const-06-05',
    'chapterId': 'ch-06',
    'title': 'Right Against Exploitation & Freedom of Religion (Articles 23–28)',
    'subtitle': 'Prohibition of Human Trafficking, Begar, Child Labour & Secular Religious Freedoms',
    'articleRef': 'Articles 23, 24, 25, 26, 27, 28',
    'learningObjective': 'Master the absolute prohibitions on exploitation under Articles 23–24 and the secular balance between individual religious freedom (Art. 25) and denomination rights (Art. 26).',
    'detailedExplanation': """
<h3>1. Right Against Exploitation (Articles 23 & 24)</h3>
<ul>
  <li><strong>Article 23: Prohibition of Traffic in Human Beings and Forced Labour:</strong>
    <ul>
      <li>Prohibits traffic in human beings, <em>begar</em> (labor without remuneration), and other similar forms of forced labor.</li>
      <li>Available against both the State and private individuals.</li>
      <li>In <em>People’s Union for Democratic Rights (PUDR) v. Union of India (Asiad Workers Case, 1982)</em>, the Supreme Court held that paying less than the statutory minimum wage constitutes "forced labor" violative of Article 23, because poverty and hunger compel the worker to submit to unconscionable terms.</li>
      <li><em>Exception (Art. 23(2)):</em> State can impose <strong>compulsory public service</strong> for public purposes (military conscription, disaster relief) without discrimination on religion, race, caste, or class.</li>
    </ul>
  </li>
  <li><strong>Article 24: Prohibition of Child Labour:</strong>
    <ul>
      <li>No child below the age of <strong>fourteen years</strong> shall be employed to work in any factory or mine or engaged in any other hazardous employment.</li>
      <li>Enforced via the <em>Child and Adolescent Labour (Prohibition and Regulation) Act, 1986</em> (amended in 2016). In <em>M.C. Mehta v. State of Tamil Nadu (Sivakasi Fireworks Case, 1996)</em>, the Court ordered creation of a Child Labour Rehabilitation Welfare Fund.</li>
    </ul>
  </li>
</ul>

<h3>2. Freedom of Religion (Articles 25–28)</h3>
<ul>
  <li><strong>Article 25: Freedom of Conscience and Profession, Practice, Propagation:</strong>
    <ul>
      <li>Guaranteed to <strong>all persons</strong> (not just citizens).</li>
      <li>Subject to: <strong>Public order, morality, and health</strong>, and to the other provisions of Part III.</li>
      <li><em>Right to propagate</em> does not include the right to forcibly convert another person (<em>Rev. Stainislaus v. State of M.P., 1977</em>).</li>
      <li><em>Article 25(2):</em> State is permitted to regulate economic, financial, or secular activities associated with religious practice, and to provide for social welfare and reform by opening Hindu religious institutions of a public character to all classes and sections of Hindus. (Explanation II clarifies that "Hindus" includes Sikhs, Jains, and Buddhists; wearing and carrying of <em>kirpans</em> is deemed included in the profession of the Sikh religion).</li>
      <li><strong>Essential Religious Practices Doctrine:</strong> First formulated in the <em>Shirur Mutt Case (1954)</em>. Courts protect only practices that are foundational and integral to the religion. Applied in <em>Shayara Bano (2017)</em> and <em>Indian Young Lawyers Association (Sabarimala Case, 2018)</em>.</li>
    </ul>
  </li>
  <li><strong>Article 26: Freedom to Manage Religious Affairs:</strong>
    <ul>
      <li>Guaranteed to every <strong>religious denomination</strong> or section thereof:
        <ol type="a">
          <li>Establish and maintain institutions for religious and charitable purposes;</li>
          <li>Manage its own affairs in matters of religion;</li>
          <li>Own and acquire movable and immovable property;</li>
          <li>Administer such property in accordance with law.</li>
        </ol>
      </li>
      <li>Subject ONLY to <strong>public order, morality, and health</strong> (it is NOT subject to the other provisions of Part III, unlike Article 25).</li>
    </ul>
  </li>
  <li><strong>Article 27: Freedom from Taxes for Promotion of any Religion:</strong>
    <ul>
      <li>No person shall be compelled to pay any taxes whose proceeds are specifically appropriated for the promotion or maintenance of any particular religion.</li>
      <li>Prohibits <strong>taxes</strong>, but does NOT prohibit a <strong>fee</strong> levied to regulate secular administration or provide safety services to pilgrims.</li>
    </ul>
  </li>
  <li><strong>Article 28: Freedom as to Attendance at Religious Instruction:</strong>
    <ul>
      <li>Four types of educational institutions:
        <ol>
          <li><em>Wholly maintained by the State:</em> Religious instruction completely prohibited.</li>
          <li><em>Administered by the State but established under endowment/trust:</em> Religious instruction permitted.</li>
          <li><em>Recognised by the State:</em> Religious instruction voluntary (requires consent).</li>
          <li><em>Receiving aid out of State funds:</em> Religious instruction voluntary.</li>
        </ol>
      </li>
    </ul>
  </li>
</ul>
""",
    'quickRevisionPoints': [
        'Article 23 prohibits trafficking, begar, and forced labor (paying below minimum wage is forced labor under PUDR case).',
        'Article 24 prohibits employment of children below 14 in factories, mines, or hazardous work.',
        'Article 25 guarantees freedom of conscience, profession, practice, and propagation to ALL persons.',
        'Article 25 is subject to Public Order, Morality, Health, AND other Fundamental Rights.',
        'Essential Religious Practices test formulated in Shirur Mutt case (1954).',
        'Article 26 protects rights of religious denominations (subject only to public order, morality, and health).',
        'Article 27 prohibits taxes for promotion of religion (fees for regulation are permitted).',
        'Article 28 completely bans religious instruction in state-maintained educational institutions.'
    ],
    'provisions': [
        {'provision': 'Article 23', 'title': 'Traffic in Human Beings', 'description': 'Bans trafficking and begar; enforceable against private parties.'},
        {'provision': 'Article 24', 'title': 'Child Labour', 'description': 'Bars employment of children under 14 in hazardous industries.'},
        {'provision': 'Article 25', 'title': 'Religious Freedom', 'description': 'Individual right to conscience, practice, and propagation.'},
        {'provision': 'Article 26', 'title': 'Denominational Rights', 'description': 'Collective autonomy to manage religious affairs and property.'}
    ],
    'definitions': [
        {'term': 'Begar', 'definition': 'Compulsory labor extracted from a person without payment of wages or with grossly inadequate consideration.'},
        {'term': 'Religious Denomination', 'definition': 'A collection of individuals having a common faith, a common organization, and designated by a distinctive name (Shirur Mutt test).'}
    ],
    'ingredients': [
        'Protection against physical and socio-economic coercion.',
        'Individual liberty of conscience balanced against public order, morality, and health.',
        'Non-involvement of public tax revenues in religious proselytization.'
    ],
    'exceptions': [
        'Under Article 23(2), the State can impose compulsory national or military service.',
        'Article 25 does not protect practices that are commercial, financial, or secular adjuncts to religion.'
    ],
    'examples': [
        {'scenario': 'A municipality imposes a ₹50 entry fee on pilgrims visiting a shrine to maintain sanitation facilities and security barricades.', 'application': 'Completely valid under Article 27; the levy is a fee for service, not a tax for promoting religion.'},
        {'scenario': 'An organization attempts to convert indigent villagers by paying them cash incentives.', 'application': 'Unlawful; the right to propagate under Article 25 does not include the right to convert by fraud, force, or financial allurement (Rev. Stainislaus v. State of M.P.).'}
    ],
    'landmarkCases': [
        {'case': 'PUDR v. Union of India (Asiad Workers Case)', 'citation': '(1982) 3 SCC 235', 'year': '1982', 'bench': 'Bhagwati J', 'ratio': 'Held that non-payment of minimum wages violates Article 23; any labor performed under economic compulsion for less than the statutory wage is forced labor.', 'impact': 'Revolutionized labor jurisprudence in India.'},
        {'case': 'Commissioner, Hindu Religious Endowments, Madras v. Sri Lakshmindra Thirtha Swamiar (Shirur Mutt Case)', 'citation': 'AIR 1954 SC 282', 'year': '1954', 'bench': '7-Judge Bench (Mukherjea J)', 'ratio': 'Established the "Essential Religious Practices" doctrine and defined what constitutes a religious denomination under Article 26.', 'impact': 'Core precedent for all freedom of religion litigation.'},
        {'case': 'Indian Young Lawyers Association v. State of Kerala (Sabarimala Case)', 'citation': '(2019) 11 SCC 1', 'year': '2018', 'bench': '5-Judge Bench (4:1 majority)', 'ratio': 'Held that the exclusion of women aged 10–50 from entering Sabarimala Temple violated their right to worship under Article 25 and freedom from discrimination under Article 15.', 'impact': 'Asserted primacy of individual gender equality over traditional religious exclusions.'}
    ],
    'comparisonTables': [
        {
            'title': 'Article 25 vs Article 26',
            'headers': ['Aspect', 'Article 25', 'Article 26'],
            'rows': [
                ['Nature of Right', 'Individual right of every person', 'Collective right of a religious denomination'],
                ['Beneficiary', 'All natural persons (citizens & foreigners)', 'Religious groups or sections having a common faith'],
                ['Restrictions', 'Public order, morality, health, AND other FRs', 'ONLY Public order, morality, and health'],
                ['Property Management', 'Does not deal with property', 'Explicitly guarantees right to own and administer property']
            ]
        }
    ],
    'diagramId': 'diag-religious-freedoms',
    'diagramExplanation': 'The architecture depicts the balance between individual conscience (Art. 25), group autonomy (Art. 26), financial neutrality (Art. 27), and secular education (Art. 28).',
    'misconceptions': [
        {'myth': 'Article 25 gives a citizen an absolute right to convert others to their religion.', 'reality': 'The Supreme Court in Rev. Stainislaus (1977) held that Article 25 gives the right to propagate one’s faith, but NOT a right to convert others.'},
        {'myth': 'Article 27 prohibits the government from collecting fees at religious shrines.', 'reality': 'Article 27 prohibits taxes (for promoting religion); it does not prohibit regulatory fees to manage hygiene, crowd safety, and services.'}
    ],
    'prelimTraps': [
        {'trap': 'Is Article 26 subject to "other provisions of Part III"?', 'reality': 'NO! Article 25 is subject to "other provisions of Part III", but Article 26 is subject ONLY to "public order, morality and health".', 'rule': 'Art. 25 has 4 restrictions; Art. 26 has only 3 restrictions.'},
        {'trap': 'Are Sikhs, Jains, and Buddhists treated as Hindus in Article 25?', 'reality': 'YES. Explanation II to Article 25(2)(b) explicitly states that the reference to Hindus shall be construed as including Sikhs, Jains, and Buddhists.', 'rule': 'Explanation II = Sikhs, Jains, Buddhists included.'}
    ],
    'flashcards': [
        {'id': 'fc-06-17', 'front': 'Which case held that paying less than minimum wages constitutes "forced labour" under Article 23?', 'back': 'PUDR v. Union of India (Asiad Workers Case, 1982).', 'category': 'Exploitation Jurisprudence'},
        {'id': 'fc-06-18', 'front': 'In which case was the "Essential Religious Practices" doctrine first propounded?', 'back': 'The Shirur Mutt Case (AIR 1954 SC 282).', 'category': 'Religious Doctrines'},
        {'id': 'fc-06-19', 'front': 'Which constitutional explanation protects the wearing and carrying of kirpans by Sikhs?', 'back': 'Explanation I to Article 25.', 'category': 'Constitutional Text'},
        {'id': 'fc-06-20', 'front': 'Does Article 27 prohibit the levy of fees on pilgrims at religious places?', 'back': 'No, it prohibits taxes; fees for secular maintenance and crowd safety are valid.', 'category': 'Taxation vs Fees'}
    ],
    'sourceReferences': [
        {'title': 'PUDR v. Union of India (1982) 3 SCC 235', 'url': 'https://main.sci.gov.in'},
        {'title': 'Indian Young Lawyers Association v. State of Kerala (2019) 11 SCC 1', 'url': 'https://main.sci.gov.in'}
    ]
}

# TOPIC 6: Cultural Rights & Writs (Articles 29–32)
data['top-const-06-06'] = {
    'topicId': 'top-const-06-06',
    'chapterId': 'ch-06',
    'title': 'Cultural & Educational Rights & Constitutional Remedies / Writs (Articles 29–32)',
    'subtitle': 'Minority Rights & The Heart and Soul of the Constitution: The 5 High Prerogative Writs',
    'articleRef': 'Articles 29, 30, 32',
    'learningObjective': 'Master the minority rights under Articles 29 and 30, understand Article 32 as the guarantor of Fundamental Rights, and analyze the scope and grounds of the five high prerogative writs.',
    'detailedExplanation': """
<h3>1. Cultural and Educational Rights (Articles 29 & 30)</h3>
<ul>
  <li><strong>Article 29: Protection of Interests of Minorities:</strong>
    <ul>
      <li><em>29(1):</em> Any section of citizens residing in India having a distinct <strong>language, script or culture of its own</strong> has the right to conserve the same. (Available to both minorities and majorities).</li>
      <li><em>29(2):</em> No citizen shall be denied admission into any educational institution maintained by the State or receiving aid out of State funds on grounds <strong>only of religion, race, caste, language or any of them</strong>.</li>
    </ul>
  </li>
  <li><strong>Article 30: Right of Minorities to Establish and Administer Educational Institutions:</strong>
    <ul>
      <li><em>30(1):</em> All minorities, whether based on <strong>religion or language</strong>, shall have the right to establish and administer educational institutions of their choice.</li>
      <li>Note: The Constitution recognises ONLY two types of minorities: <strong>Religious and Linguistic minorities</strong> (determined state-wise, as held in <em>T.M.A. Pai Foundation v. State of Karnataka, 2002</em>).</li>
      <li><em>30(2):</em> State shall not discriminate in granting aid to educational institutions on the ground that it is under minority management.</li>
      <li>In <em>P.A. Inamdar v. State of Maharashtra (2005 6 SCC 537)</em>, the Supreme Court held that the State cannot impose reservation quotas on unaided private minority educational institutions.</li>
    </ul>
  </li>
</ul>

<h3>2. Article 32: Right to Constitutional Remedies</h3>
<p>Dr. B.R. Ambedkar famously observed in the Constituent Assembly: <em>"If I was asked to name any particular article in this Constitution as the most important—an article without which this Constitution would be a nullity—I could not refer to any other article except this one. It is the very soul of the Constitution and the very heart of it."</em></p>
<ul>
  <li>Article 32 is itself a <strong>Fundamental Right</strong>; the Supreme Court cannot refuse to hear a petition under Article 32 alleging violation of a Fundamental Right (<em>Romesh Thappar, 1950</em>).</li>
  <li>Article 32 is part of the <strong>Basic Structure</strong> of the Constitution (<em>Fertilizer Corporation Kamgar Union, 1981</em>).</li>
  <li>Can be invoked ONLY for the enforcement of <strong>Fundamental Rights</strong>, not ordinary legal rights or non-fundamental constitutional rights.</li>
</ul>

<h3>3. The Five High Prerogative Writs</h3>
<ol>
  <li><strong>Habeas Corpus ("To have the body of"):</strong>
    <ul>
      <li>An order directed to a person who detains another, commanding him to produce the body of the prisoner before the court to determine the legality of detention.</li>
      <li>If detention is unlawful, the court orders immediate release.</li>
      <li>Can be filed by the detenu or by any friend/relative on their behalf (exception to strict locus standi). Lies against both public authorities and private individuals. (<em>Sunil Batra v. Delhi Administration, 1980</em>).</li>
    </ul>
  </li>
  <li><strong>Mandamus ("We Command"):</strong>
    <ul>
      <li>A judicial order commanding a public authority, corporation, inferior court, or tribunal to perform a mandatory statutory or public duty that it has refused to perform.</li>
      <li><em>Conditions:</em> Petitioner must have a legal right to compel performance; duty must be mandatory, not discretionary.</li>
      <li><em>Cannot be issued against:</em> The President of India or State Governors (Art. 361), private individuals or private contracts, or to enforce non-statutory departmental manuals.</li>
    </ul>
  </li>
  <li><strong>Prohibition:</strong>
    <ul>
      <li>Issued by a superior court to an inferior judicial or quasi-judicial body to prevent it from usurping jurisdiction which it does not legally possess (preventive in nature: <em>"prevention is better than cure"</em>).</li>
      <li>Lies only against judicial and quasi-judicial authorities, not against legislative or administrative bodies.</li>
    </ul>
  </li>
  <li><strong>Certiorari ("To be certified"):</strong>
    <ul>
      <li>Issued by a superior court to an inferior court or tribunal to quash an order already passed in excess of jurisdiction, lack of jurisdiction, or in violation of natural justice, or where there is an error of law apparent on the face of the record.</li>
      <li>Both preventive and curative. (In <em>Surya Dev Rai v. Ram Chander Rai, 2003</em> and <em>Radhey Shyam, 2015</em>, clarified regarding civil courts).</li>
    </ul>
  </li>
  <li><strong>Quo-Warranto ("By what authority?"):</strong>
    <ul>
      <li>Issued to inquire into the legality of the claim which a person asserts to a public office of a substantive character, and to oust him from its enjoyment if his claim is unlawful.</li>
      <li>Prevents illegal usurpation of public offices.</li>
      <li>Can be sought by <strong>any citizen</strong> even if their personal rights are not infringed (no strict locus standi required).</li>
    </ul>
  </li>
</ol>
""",
    'quickRevisionPoints': [
        'Article 29 protects language, script, and culture; Article 30 protects religious and linguistic minorities.',
        'Minority status is determined at the state level (T.M.A. Pai Foundation, 2002).',
        'Article 32 is Dr. Ambedkar’s "Heart and Soul of the Constitution" and part of the Basic Structure.',
        'Article 32 can be invoked ONLY for Fundamental Rights; Article 226 can be invoked for FRs AND other legal rights.',
        'Habeas Corpus: Against illegal detention; lies against public and private parties.',
        'Mandamus: To compel performance of a public/statutory duty; does not lie against President/Governor.',
        'Prohibition: Preventive writ to stop inferior judicial/tribunal bodies from exceeding jurisdiction.',
        'Certiorari: Curative writ to quash orders passed without jurisdiction or violating natural justice.',
        'Quo-Warranto: Challenges illegal usurpation of substantive public offices; no locus standi required.'
    ],
    'provisions': [
        {'provision': 'Article 29', 'title': 'Protection of Minorities', 'description': 'Right to conserve distinct language, script, or culture.'},
        {'provision': 'Article 30', 'title': 'Minority Educational Rights', 'description': 'Right to establish and administer educational institutions.'},
        {'provision': 'Article 32', 'title': 'Remedies for Enforcement', 'description': 'Constitutional right to move Supreme Court by appropriate writ proceedings.'}
    ],
    'definitions': [
        {'term': 'Locus Standi', 'definition': 'The legal capacity of a person to invoke the court’s jurisdiction based on personal injury or direct legal interest.'},
        {'term': 'Public Interest Litigation (PIL)', 'definition': 'Relaxation of traditional locus standi developed under Article 32 allowing public-spirited citizens to petition courts on behalf of marginalized groups.'}
    ],
    'ingredients': [
        'Violation of a guaranteed right under Part III.',
        'Absence of lawful jurisdiction or violation of natural justice in lower tribunals.',
        'Substantive public character of office in quo-warranto.'
    ],
    'exceptions': [
        'Article 32 cannot be invoked to challenge valid judicial orders of the Supreme Court itself.',
        'Mandamus cannot be issued against the President or Governor for acts in performance of official duties (Article 361).'
    ],
    'examples': [
        {'scenario': 'A person without the statutory qualifications is appointed as the Vice-Chancellor of a State University.', 'application': 'Any citizen can file a writ of Quo-Warranto to challenge the appointment and oust the usurper, as the office is a public office of substantive character.'},
        {'scenario': 'A magistrate detains an accused without passing a remand order after the 24-hour statutory period.', 'application': 'A writ of Habeas Corpus will lie immediately commanding the production and release of the detenu.'}
    ],
    'landmarkCases': [
        {'case': 'T.M.A. Pai Foundation v. State of Karnataka', 'citation': '(2002) 8 SCC 481', 'year': '2002', 'bench': '11-Judge Bench (Kirpal CJ)', 'ratio': 'Determined that for the purposes of Article 30, a minority (religious or linguistic) must be determined with reference to the population of the State, not all of India.', 'impact': 'Settled the territorial basis of minority definitions.'},
        {'case': 'Sunil Batra v. Delhi Administration', 'citation': '(1980) 3 SCC 488', 'year': '1980', 'bench': 'Krishna Iyer J', 'ratio': 'Expanded Habeas Corpus from mere physical liberation to protecting prisoners from torture, solitary confinement, and cruel treatment inside jail.', 'impact': 'Humanized Indian prison conditions via epistolary jurisdiction.'},
        {'case': 'Bandhua Mukti Morcha v. Union of India', 'citation': '(1984) 3 SCC 161', 'year': '1984', 'bench': 'Bhagwati J', 'ratio': 'Established that the procedural requirements of Article 32 are flexible; court can appoint commissioners to inspect bonded labor sites.', 'impact': 'Institutionalized Public Interest Litigation (PIL).'}
    ],
    'comparisonTables': [
        {
            'title': 'Article 32 vs Article 226',
            'headers': ['Aspect', 'Article 32 (Supreme Court)', 'Article 226 (High Courts)'],
            'rows': [
                ['Status', 'Fundamental Right itself (Part III)', 'Constitutional Right (Part VI)'],
                ['Subject Matter', 'ONLY for Fundamental Rights', 'For Fundamental Rights AND "any other purpose" (ordinary legal rights)'],
                ['Discretion', 'Cannot be refused; mandatory remedy', 'Discretionary remedy'],
                ['Territorial Scope', 'Throughout the entire territory of India', 'Within the State or cause of action arising in the State']
            ]
        }
    ],
    'diagramId': 'diag-five-writs',
    'diagramExplanation': 'The visual delineates the 5 high prerogative writs categorized into personal liberty (Habeas Corpus), performance of duty (Mandamus), jurisdictional supervision (Prohibition & Certiorari), and public office legality (Quo-Warranto).',
    'misconceptions': [
        {'myth': 'Article 32 has a wider jurisdiction than Article 226.', 'reality': 'Article 226 is WIDER in scope than Article 32 because High Courts can issue writs for Fundamental Rights AS WELL AS ordinary legal rights ("for any other purpose").'},
        {'myth': 'A writ of Mandamus can be issued to direct the legislature to enact a statute.', 'reality': 'Courts cannot issue a mandamus to Parliament or State Legislatures to pass a law; lawmaking is discretionary sovereign power.'}
    ],
    'prelimTraps': [
        {'trap': 'Unit for determining linguistic or religious minorities under Article 30.', 'reality': 'The STATE, not India as a whole (T.M.A. Pai Foundation, 2002).', 'rule': 'Minority unit = State population.'},
        {'trap': 'Which writ can be sought by any person without showing personal locus standi?', 'reality': 'Quo-Warranto (and Habeas Corpus filed on behalf of a detained person).', 'rule': 'Quo-Warranto = Any citizen can file.'}
    ],
    'flashcards': [
        {'id': 'fc-06-21', 'front': 'Which article was called the "Heart and Soul of the Constitution" by Dr. B.R. Ambedkar?', 'back': 'Article 32 (Right to Constitutional Remedies).', 'category': 'Constitutional Sayings'},
        {'id': 'fc-06-22', 'front': 'Which writ literally translates to "To have the body of"?', 'back': 'Habeas Corpus.', 'category': 'Prerogative Writs'},
        {'id': 'fc-06-23', 'front': 'Can a writ of Mandamus be issued against the President of India or a State Governor?', 'back': 'No, protected by constitutional immunity under Article 361.', 'category': 'Writ Jurisprudence'},
        {'id': 'fc-06-24', 'front': 'Which landmark case held that minority status under Article 30 must be determined state-wise?', 'back': 'T.M.A. Pai Foundation v. State of Karnataka (2002).', 'category': 'Minority Rights'}
    ],
    'sourceReferences': [
        {'title': 'T.M.A. Pai Foundation v. State of Karnataka (2002) 8 SCC 481', 'url': 'https://main.sci.gov.in'},
        {'title': 'Sunil Batra v. Delhi Administration (1980) 3 SCC 488', 'url': 'https://main.sci.gov.in'}
    ]
}

# ----------------------------------------------------
# CHAPTER 7: DIRECTIVE PRINCIPLES OF STATE POLICY
# ----------------------------------------------------

# TOPIC 7: Articles 36 & 37
data['top-const-07-01'] = {
    'topicId': 'top-const-07-01',
    'chapterId': 'ch-07',
    'title': 'Genesis, Nature & Justiciability of DPSP (Articles 36–37)',
    'subtitle': 'Fundamental in the Governance of the Country',
    'articleRef': 'Articles 36 and 37',
    'learningObjective': 'Analyze the Irish origin of the Directive Principles, their non-justiciable character, and their status as fundamental canons of governance under Article 37.',
    'detailedExplanation': """
<h3>1. Genesis of Part IV</h3>
<p>The Directive Principles of State Policy (Part IV, Articles 36 to 51) were borrowed from the <strong>Constitution of Ireland, 1937</strong> (which in turn borrowed them from the Spanish Constitution). Dr. B.R. Ambedkar characterized them as the <strong>"Novel Features"</strong> of the Indian Constitution, designed to establish a <em>Welfare State</em> and realize socio-economic democracy.</p>

<h3>2. Article 36: Definition of State</h3>
<p>Article 36 provides that unless the context otherwise requires, <em>"the State"</em> has the same meaning as in Part III (Article 12). Thus, Directive Principles are addressed to the Central Government, Parliament, State Governments, State Legislatures, and all local and other statutory authorities.</p>

<h3>3. Article 37: Nature and Constitutional Significance</h3>
<p>Article 37 contains two foundational declarations:</p>
<ol>
  <li><strong>Non-Justiciability:</strong> The provisions contained in Part IV <em>"shall not be enforceable by any court"</em>. No court can issue a writ of mandamus compelling the government to implement a Directive Principle.</li>
  <li><strong>Fundamental in Governance:</strong> <em>"Nevertheless, the principles therein laid down are fundamental in the governance of the country and it shall be the duty of the State to apply these principles in making laws."</em></li>
</ol>
<p>Sir B.N. Rau, Constitutional Advisor, classified rights into two categories: justiciable rights (which became Part III) and non-justiciable rights (which became Part IV). Lack of adequate financial resources in 1949 prevented the framers from making socio-economic rights immediately enforceable.</p>
""",
    'quickRevisionPoints': [
        'DPSP contained in Part IV (Articles 36 to 51), borrowed from Ireland.',
        'Dr. Ambedkar called DPSP the "Novel Features" of the Indian Constitution.',
        'Aims to establish economic democracy and a Welfare State.',
        'Article 36 adopts the definition of "State" from Article 12.',
        'Article 37: DPSP are non-enforceable by courts, but "fundamental in the governance of the country".'
    ],
    'provisions': [
        {'provision': 'Article 36', 'title': 'Definition of State', 'description': 'Applies Article 12 definition to Directive Principles.'},
        {'provision': 'Article 37', 'title': 'Application of Principles', 'description': 'Non-justiciable character balanced with duty of State in lawmaking.'}
    ],
    'definitions': [
        {'term': 'Welfare State', 'definition': 'A state committed to securing socio-economic justice, social security, and equitable wealth distribution rather than being merely a police state.'},
        {'term': 'Instrument of Instructions', 'definition': 'The characterization of DPSP by Dr. Ambedkar as instructions to the executive and legislature analogous to those issued to the Governor-General under the GoI Act 1935.'}
    ],
    'ingredients': [
        'Ethical and constitutional directives guiding legislative and executive policy.',
        'Non-coercive, non-justiciable character.',
        'Focus on substantive socio-economic transformation.'
    ],
    'exceptions': [
        'Courts cannot strike down an otherwise valid statute merely because it does not implement a DPSP.'
    ],
    'examples': [
        {'scenario': 'A citizen approaches the High Court seeking a writ of mandamus directing the State Government to enact a law guaranteeing the Right to Work under Article 41.', 'application': 'The petition must be dismissed as barred by Article 37; courts cannot enforce DPSP through judicial writs.'}
    ],
    'landmarkCases': [
        {'case': 'State of Madras v. Champakam Dorairajan', 'citation': 'AIR 1951 SC 226', 'year': '1951', 'bench': '7-Judge Bench', 'ratio': 'Held that Directive Principles have to conform to and run as subsidiary to the Chapter of Fundamental Rights.', 'impact': 'Prompted the 1st Constitutional Amendment Act, 1951.'}
    ],
    'comparisonTables': [
        {
            'title': 'Fundamental Rights (Part III) vs Directive Principles (Part IV)',
            'headers': ['Feature', 'Fundamental Rights (Part III)', 'Directive Principles (Part IV)'],
            'rows': [
                ['Nature', 'Negative injunctions (prohibitions on State)', 'Positive instructions (affirmative duties on State)'],
                ['Justiciability', 'Justiciable (enforceable via Art. 32/226)', 'Non-justiciable (unenforceable in court)'],
                ['Objective', 'Establish political democracy', 'Establish socio-economic welfare democracy'],
                ['Legal Sanction', 'Enforced by judicial writs', 'Enforced by political sanction (electoral public opinion)']
            ]
        }
    ],
    'diagramId': 'diag-dpsp-foundations',
    'diagramExplanation': 'The visual contrasts the negative judicial shield of Part III with the positive promotional banner of Part IV.',
    'misconceptions': [
        {'myth': 'Because DPSP are non-justiciable, they are legally useless.', 'reality': 'The Supreme Court uses DPSP to interpret Fundamental Rights and determine the reasonableness of restrictions under Article 19.'}
    ],
    'prelimTraps': [
        {'trap': 'Who described DPSP as a "cheque on a bank, payable only when the resources of the bank permit"?', 'reality': 'Prof. K.T. Shah in the Constituent Assembly.', 'rule': 'Cheque on bank = K.T. Shah.'}
    ],
    'flashcards': [
        {'id': 'fc-07-01', 'front': 'From which country’s constitution were Directive Principles borrowed?', 'back': 'Constitution of Ireland (1937).', 'category': 'Foreign Sources'},
        {'id': 'fc-07-02', 'front': 'Which article declares that DPSP are "fundamental in the governance of the country"?', 'back': 'Article 37.', 'category': 'Constitutional Articles'},
        {'id': 'fc-07-03', 'front': 'Who described Directive Principles as the "Novel Features" of the Indian Constitution?', 'back': 'Dr. B.R. Ambedkar.', 'category': 'Constitutional Sayings'}
    ],
    'sourceReferences': [
        {'title': 'Constituent Assembly Debates, Vol. VII', 'url': 'https://www.constitutionofindia.net'},
        {'title': 'State of Madras v. Champakam Dorairajan, AIR 1951 SC 226', 'url': 'https://main.sci.gov.in'}
    ]
}

# TOPIC 8: Articles 38–51
data['top-const-07-02'] = {
    'topicId': 'top-const-07-02',
    'chapterId': 'ch-07',
    'title': 'Substantive Classification of Directives (Articles 38–51)',
    'subtitle': 'Socialistic, Gandhian & Liberal-Intellectual Principles, Uniform Civil Code (Art. 44)',
    'articleRef': 'Articles 38–51',
    'learningObjective': 'Master the tripartite ideological classification of Directive Principles, analyze Article 44 Uniform Civil Code, and examine amendments.',
    'detailedExplanation': """
<h3>1. The Tripartite Ideological Classification</h3>
<p>Although the text of the Constitution does not formally categorize them, scholars and courts divide Part IV into three ideological streams:</p>

<h4>A. Socialistic Principles (Reflecting welfare ideology):</h4>
<ul>
  <li><strong>Article 38:</strong> State to secure a social order for the promotion of the welfare of the people; minimize inequalities in income, status, and facilities (clause (2) added by 44th Amendment 1978).</li>
  <li><strong>Article 39:</strong> Specific policies to be followed by the State:
    <ul>
      <li>(a) Adequate means of livelihood for all citizens.</li>
      <li>(b) Ownership and control of material resources of community distributed to subserve the common good.</li>
      <li>(c) Operation of economic system does not result in the concentration of wealth.</li>
      <li>(d) Equal pay for equal work for both men and women.</li>
      <li>(e) Health and strength of workers and children protected against abuse.</li>
      <li>(f) Opportunities for healthy development of children (amended by 42nd Amendment 1976).</li>
    </ul>
  </li>
  <li><strong>Article 39A [42nd Amendment 1976]:</strong> Equal justice and <strong>free legal aid</strong> for the poor.</li>
  <li><strong>Article 41:</strong> Right to work, to education, and to public assistance in cases of unemployment, old age, sickness, and disablement.</li>
  <li><strong>Article 42:</strong> Just and humane conditions of work and <strong>maternity relief</strong>.</li>
  <li><strong>Article 43:</strong> Living wage, decent standard of life, and social and cultural opportunities for workers.</li>
  <li><strong>Article 43A [42nd Amendment 1976]:</strong> Participation of workers in management of industries.</li>
</ul>

<h4>B. Gandhian Principles (Reflecting Mahatma Gandhi’s rural reconstruction vision):</h4>
<ul>
  <li><strong>Article 40:</strong> Organization of <strong>Village Panchayats</strong> as units of self-government (fulfilled by 73rd Amendment).</li>
  <li><strong>Article 43:</strong> Promotion of cottage industries on an individual or co-operative basis in rural areas.</li>
  <li><strong>Article 43B [97th Amendment 2011]:</strong> Promotion of voluntary formation and autonomous functioning of <strong>co-operative societies</strong>.</li>
  <li><strong>Article 46:</strong> Promotion of educational and economic interests of SCs, STs, and other weaker sections.</li>
  <li><strong>Article 47:</strong> Prohibition of the consumption of intoxicating drinks and drugs injurious to health.</li>
  <li><strong>Article 48:</strong> Prohibition of the slaughter of cows, calves, and other milch and draught cattle.</li>
</ul>

<h4>C. Liberal-Intellectual Principles (Reflecting modern liberal democracy):</h4>
<ul>
  <li><strong>Article 44:</strong> State shall endeavour to secure for the citizens a <strong>Uniform Civil Code (UCC)</strong> throughout the territory of India. (Judicially emphasized in <em>Shah Bano, 1985</em>; <em>Sarla Mudgal, 1995</em>; <em>John Vallamattom, 2003</em>).</li>
  <li><strong>Article 45 [Substituted by 86th Amendment 2002]:</strong> Early childhood care and education for all children until they complete the age of <strong>six years</strong>.</li>
  <li><strong>Article 48A [42nd Amendment 1976]:</strong> Protection and improvement of environment and safeguarding of forests and wild life.</li>
  <li><strong>Article 49:</strong> Protection of monuments, places and objects of national historic or artistic importance.</li>
  <li><strong>Article 50:</strong> <strong>Separation of the Judiciary from the Executive</strong> in the public services of the State.</li>
  <li><strong>Article 51:</strong> Promotion of international peace and security, maintaining just relations between nations, respect for international law, and settlement of disputes by arbitration.</li>
</ul>
""",
    'quickRevisionPoints': [
        'Article 38: Social order promoting welfare; minimize income inequalities (44th Amendment).',
        'Article 39(b) & 39(c): Distribution of material resources and prevention of wealth concentration.',
        'Article 39A: Equal justice and free legal aid (added by 42nd Amendment 1976).',
        'Article 40: Organization of Village Panchayats (Gandhian principle).',
        'Article 43B: Promotion of co-operative societies (added by 97th Amendment 2011).',
        'Article 44: Uniform Civil Code for all citizens.',
        'Article 45: Early childhood care below 6 years (substituted by 86th Amendment 2002).',
        'Article 48A: Protection of environment, forests, wildlife (added by 42nd Amendment 1976).',
        'Article 50: Separation of Judiciary from Executive.',
        'Article 51: Promotion of international peace and security.'
    ],
    'provisions': [
        {'provision': 'Article 39A', 'title': 'Free Legal Aid', 'description': 'Mandate to provide free legal services to indigent citizens.'},
        {'provision': 'Article 40', 'title': 'Village Panchayats', 'description': 'Constitutional foundation for local self-government.'},
        {'provision': 'Article 44', 'title': 'Uniform Civil Code', 'description': 'Directive to secure common civil laws across all communities.'},
        {'provision': 'Article 50', 'title': 'Judicial Separation', 'description': 'Mandate separating magistrates and judicial officers from executive control.'}
    ],
    'definitions': [
        {'term': 'Uniform Civil Code (Article 44)', 'definition': 'A common set of civil personal laws governing marriage, divorce, succession, adoption, and maintenance applicable uniformly to all citizens irrespective of religion.'},
        {'term': 'Living Wage (Article 43)', 'definition': 'A level of wage sufficient not only to provide bare sustenance, but also education for children, healthcare, insurance, and cultural comfort.'}
    ],
    'ingredients': [
        'Progressive socio-economic state policy formulation.',
        'Preservation of environmental and national cultural heritage.',
        'Structural insulation of the judiciary from administrative interference.'
    ],
    'exceptions': [
        'State policies implementing DPSP must not violate the Basic Structure or abrogated fundamental rights except within Article 31C.'
    ],
    'examples': [
        {'scenario': 'A state government enacts a total ban on the sale and consumption of alcohol.', 'application': 'Completely constitutional under Article 47, which imposes a duty on the State to prohibit consumption of intoxicating drinks.'},
        {'scenario': 'Parliament enacts the Legal Services Authorities Act, 1987 establishing Lok Adalats and legal aid cells.', 'application': 'Enacted to give statutory effect to Article 39A of the Constitution.'}
    ],
    'landmarkCases': [
        {'case': 'Mohd. Ahmed Khan v. Shah Bano Begum', 'citation': '(1985) 2 SCC 556', 'year': '1985', 'bench': '5-Judge Bench (Chandrachud CJ)', 'ratio': 'Expressed regret that Article 44 on Uniform Civil Code had remained a dead letter, and held that Section 125 CrPC on maintenance applies uniformly to all women.', 'impact': 'Landmark catalyst in personal law and gender equality debates.'},
        {'case': 'Sarla Mudgal v. Union of India', 'citation': '(1995) 3 SCC 635', 'year': '1995', 'bench': 'Kuldip Singh J', 'ratio': 'Held that a Hindu husband cannot convert to Islam solely to contract a second marriage without dissolving his first marriage under Hindu law; reiterated the necessity of a Uniform Civil Code under Article 44.', 'impact': 'Check on fraudulent conversions to evade bigamy laws.'}
    ],
    'comparisonTables': [
        {
            'title': 'The Three Ideological Categories of DPSP',
            'headers': ['Category', 'Key Articles', 'Core Philosophy'],
            'rows': [
                ['Socialistic Directives', 'Arts. 38, 39, 39A, 41, 42, 43, 43A', 'Egalitarian distribution of wealth and labor welfare'],
                ['Gandhian Directives', 'Arts. 40, 43, 43B, 46, 47, 48', 'Rural cottage economy, panchayats, cow protection'],
                ['Liberal-Intellectual', 'Arts. 44, 45, 48A, 49, 50, 51', 'Rule of law, UCC, secular judicial separation, environment']
            ]
        }
    ],
    'diagramId': 'diag-dpsp-classification',
    'diagramExplanation': 'The 3-column architectural diagram classifies all Articles from 38 to 51 into Socialistic, Gandhian, and Liberal streams.',
    'misconceptions': [
        {'myth': 'Article 45 guarantees free and compulsory education for children up to 14 years.', 'reality': 'Article 45 originally did; but the 86th Amendment Act 2002 transferred 6-14 education to Fundamental Right Article 21A, and substituted Article 45 with early childhood care below 6 years.'}
    ],
    'prelimTraps': [
        {'trap': 'Which article directs the Separation of Judiciary from Executive?', 'reality': 'Article 50 (NOT Article 51, which deals with International Peace).', 'rule': 'Art. 50 = Separation of Judiciary; Art. 51 = International Peace.'},
        {'trap': 'Articles inserted by the 42nd Amendment Act 1976 in Part IV.', 'reality': 'Articles 39A, 43A, and 48A (and amendment to 39(f)).', 'rule': '39A, 43A, 48A = 42nd Amendment.'}
    ],
    'flashcards': [
        {'id': 'fc-07-04', 'front': 'Which article provides for a Uniform Civil Code?', 'back': 'Article 44.', 'category': 'Constitutional Articles'},
        {'id': 'fc-07-05', 'front': 'Which article directs the separation of Judiciary from Executive?', 'back': 'Article 50.', 'category': 'Constitutional Articles'},
        {'id': 'fc-07-06', 'front': 'Which article directs the promotion of Village Panchayats?', 'back': 'Article 40 (Gandhian principle).', 'category': 'Constitutional Articles'},
        {'id': 'fc-07-07', 'front': 'Which article added by the 42nd Amendment provides for Free Legal Aid?', 'back': 'Article 39A.', 'category': 'Legal Welfare'}
    ],
    'sourceReferences': [
        {'title': 'Sarla Mudgal v. Union of India (1995) 3 SCC 635', 'url': 'https://main.sci.gov.in'},
        {'title': 'Legal Services Authorities Act, 1987 (implementing Art. 39A)', 'url': 'https://nalsa.gov.in'}
    ]
}

# TOPIC 9: FR vs DPSP
data['top-const-07-03'] = {
    'topicId': 'top-const-07-03',
    'chapterId': 'ch-07',
    'title': 'Harmonious Construction: Fundamental Rights vs DPSP',
    'subtitle': 'From Champakam Dorairajan to Minerva Mills: The Two Wheels of the Chariot',
    'articleRef': 'Inter-relationship Jurisprudence',
    'learningObjective': 'Trace the historical constitutional tug-of-war between Part III and Part IV, analyzing Article 31C and the doctrine of harmonious balance.',
    'detailedExplanation': """
<h3>1. The Evolution of the Conflict</h3>
<p>The relationship between Fundamental Rights (Part III) and Directive Principles (Part IV) represents one of the most intellectually profound constitutional dialogues in Indian jurisprudence:</p>

<h3>2. Phase 1: Primacy of Fundamental Rights (1951)</h3>
<ul>
  <li>In <strong>State of Madras v. Champakam Dorairajan (AIR 1951 SC 226)</strong>, a 7-Judge bench held:
    <ul>
      <li>Fundamental Rights are sacrosanct and enforceable; Directive Principles are non-justiciable.</li>
      <li><em>"The Directive Principles have to conform to and run as subsidiary to the Chapter on Fundamental Rights."</em> In case of conflict, Fundamental Rights prevail.</li>
    </ul>
  </li>
</ul>

<h3>3. Phase 2: Doctrine of Harmonious Construction (1958)</h3>
<ul>
  <li>In <strong>In Re Kerala Education Bill (AIR 1958 SC 956)</strong>, Chief Justice S.R. Das softened the Champakam stance by introducing the <strong>Doctrine of Harmonious Construction</strong>:
    <ul>
      <li>Courts should not read Part III and Part IV in conflict. They should attempt to harmonize them, giving effect to both as far as possible.</li>
      <li>However, if harmonious construction is impossible, Fundamental Rights still enjoyed formal legal primacy.</li>
    </ul>
  </li>
</ul>

<h3>4. Phase 3: The 25th Amendment and Article 31C (1971)</h3>
<ul>
  <li>Parliament enacted the <strong>25th Constitutional Amendment Act, 1971</strong>, inserting <strong>Article 31C</strong>:
    <ul>
      <li><em>First Part:</em> No law giving effect to the policy of the State towards securing the principles in <strong>Article 39(b) or Article 39(c)</strong> shall be deemed to be void on the ground that it is inconsistent with Article 14 or Article 19.</li>
      <li><em>Second Part:</em> "No law containing a declaration that it is for giving effect to such policy shall be called in question in any court on the ground that it does not give effect to such policy." (Ousting judicial review).</li>
    </ul>
  </li>
  <li>In <strong>Kesavananda Bharati (1973)</strong>, the Supreme Court:
    <ul>
      <li>UPHELD the first part of Article 31C (subordinating Articles 14 and 19 to Articles 39(b) and 39(c)).</li>
      <li>STRUCK DOWN the second part of Article 31C because judicial review is part of the Basic Structure and cannot be barred.</li>
    </ul>
  </li>
</ul>

<h3>5. Phase 4: Overreach and the Minerva Mills Bedrock (1980)</h3>
<ul>
  <li>The <strong>42nd Constitutional Amendment Act, 1976</strong> expanded Article 31C to give primacy to <strong>ALL Directive Principles</strong> over Articles 14 and 19.</li>
  <li>In <strong>Minerva Mills v. Union of India ((1980) 3 SCC 625)</strong>, the Supreme Court struck down this expansion as unconstitutional:
    <ul>
      <li>To give absolute primacy to Directive Principles over Fundamental Rights destroys the core balance of the Constitution.</li>
      <li>Justice Y.V. Chandrachud CJ famously observed: <em>"The Indian Constitution is founded on the bedrock of the balance between Parts III and IV. To give absolute primacy to one over the other is to disturb the harmony of the Constitution. Part III and Part IV together constitute the core of commitment to social revolution. They are like two wheels of a chariot, one no less important than the other."</em></li>
    </ul>
  </li>
  <li>In <strong>Unni Krishnan (1993)</strong>, the Court declared that Fundamental Rights and Directive Principles are supplementary and complementary to each other.</li>
</ul>
""",
    'quickRevisionPoints': [
        'Champakam Dorairajan (1951): DPSP are subsidiary to Fundamental Rights.',
        'Kerala Education Bill (1958): Introduced Doctrine of Harmonious Construction.',
        '25th Amendment 1971 inserted Article 31C: Laws implementing Art. 39(b) or 39(c) cannot be challenged under Art. 14 or 19.',
        'Kesavananda Bharati (1973) upheld the first part of Art. 31C; struck down the second part ousting judicial review.',
        'Minerva Mills (1980): The balance between Part III and Part IV is part of the Basic Structure ("two wheels of a chariot").',
        'Present position: Only Articles 39(b) and 39(c) enjoy constitutional primacy over Articles 14 and 19.'
    ],
    'provisions': [
        {'provision': 'Article 31C', 'title': 'Saving of Certain Laws', 'description': 'Protects statutes implementing Articles 39(b) and 39(c) from invalidation under Articles 14 and 19.'}
    ],
    'definitions': [
        {'term': 'Harmonious Construction', 'definition': 'A cannon of constitutional interpretation that seeks to read competing provisions together so as to give maximum operational effect to each without rendering either redundant.'},
        {'term': 'Bedrock of the Balance', 'definition': 'The classic Minerva Mills principle declaring that the equilibrium between individual liberties (Part III) and social justice (Part IV) is an inviolable basic feature.'}
    ],
    'ingredients': [
        'Statutory nexus with equitable distribution of community resources under Article 39(b) or prevention of wealth concentration under Article 39(c).',
        'Preservation of judicial review over the genuine existence of the nexus.',
        'Maintenance of the core equilibrium between civil liberties and state welfare.'
    ],
    'exceptions': [
        'Only Articles 39(b) and 39(c) enjoy constitutional immunity under Article 31C. Other Directive Principles do not override Articles 14 and 19.'
    ],
    'examples': [
        {'scenario': 'A state passes an agrarian land ceiling statute redistributing surplus land under Article 39(b), which an owner challenges under Article 14.', 'application': 'Protected under Article 31C; the statute cannot be struck down for violating Article 14 if it genuinely implements Article 39(b) (Sanjeev Coke Mfg. Co., 1983).'}
    ],
    'landmarkCases': [
        {'case': 'Minerva Mills v. Union of India', 'citation': '(1980) 3 SCC 625', 'year': '1980', 'bench': '5-Judge Bench (Chandrachud CJ)', 'ratio': 'Struck down Section 4 of 42nd Amendment expanding Art. 31C. Held that the balance between Part III and Part IV is basic structure; they are like the two wheels of a chariot.', 'impact': 'Settled the eternal balance between liberties and welfare.'},
        {'case': 'Kesavananda Bharati v. State of Kerala', 'citation': '(1973) 4 SCC 225', 'year': '1973', 'bench': '13-Judge Bench', 'ratio': 'Upheld first half of Article 31C; struck down the second half barring judicial review.', 'impact': 'Established judicial scrutiny over DPSP nexus.'}
    ],
    'comparisonTables': [
        {
            'title': 'Evolution of the Primacy Contest',
            'headers': ['Period / Ruling', 'Dominant Principle', 'Status of Conflict'],
            'rows': [
                ['Champakam Dorairajan (1951)', 'Fundamental Rights supreme', 'DPSP must conform as subsidiary'],
                ['Kerala Education Bill (1958)', 'Harmonious Construction', 'Attempt to reconcile; FRs prevail if deadlock'],
                ['25th Amendment / Kesavananda (1973)', 'Limited Primacy of 39(b) & (c)', 'Art. 31C shields laws implementing 39(b)/(c) from Arts. 14 & 19'],
                ['Minerva Mills (1980)', 'Equilibrium / Bedrock Balance', 'Balance is Basic Structure; both parts equal']
            ]
        }
    ],
    'diagramId': 'diag-two-wheels-chariot',
    'diagramExplanation': 'The metaphor of the two wheels of a chariot represents the twin indispensability of Fundamental Rights (liberty) and Directive Principles (equality and social justice).',
    'misconceptions': [
        {'myth': 'All Directive Principles have primacy over Fundamental Rights under the 42nd Amendment.', 'reality': 'The 42nd Amendment attempted to give all DPSP primacy, but the Supreme Court struck down that expansion in Minerva Mills (1980). Only 39(b) and (c) have primacy.'}
    ],
    'prelimTraps': [
        {'trap': 'Which Directive Principles override Articles 14 and 19 under Article 31C?', 'reality': 'ONLY Article 39(b) and Article 39(c). No other Directive Principle enjoys this immunity.', 'rule': 'Art. 31C = Only 39(b) and 39(c).'},
        {'trap': 'Who described Fundamental Rights and DPSP as "two wheels of a chariot"?', 'reality': 'Chief Justice Y.V. Chandrachud in Minerva Mills v. Union of India (1980).', 'rule': 'Two wheels = Y.V. Chandrachud (Minerva Mills).'}
    ],
    'flashcards': [
        {'id': 'fc-07-08', 'front': 'Which case compared Fundamental Rights and DPSP to the "two wheels of a chariot"?', 'back': 'Minerva Mills v. Union of India (1980).', 'category': 'Landmark Precedents'},
        {'id': 'fc-07-09', 'front': 'Which article was inserted by the 25th Amendment to protect laws implementing Art. 39(b) & (c)?', 'back': 'Article 31C.', 'category': 'Constitutional Articles'},
        {'id': 'fc-07-10', 'front': 'Which case first introduced the Doctrine of Harmonious Construction between Part III and IV?', 'back': 'In Re Kerala Education Bill (1958).', 'category': 'Doctrinal Evolution'}
    ],
    'sourceReferences': [
        {'title': 'Minerva Mills v. Union of India (1980) 3 SCC 625', 'url': 'https://main.sci.gov.in'},
        {'title': 'In Re Kerala Education Bill, AIR 1958 SC 956', 'url': 'https://main.sci.gov.in'}
    ]
}

# ----------------------------------------------------
# CHAPTER 8: FUNDAMENTAL DUTIES
# ----------------------------------------------------

# TOPIC 10: Article 51A Genesis & Enactment
data['top-const-08-01'] = {
    'topicId': 'top-const-08-01',
    'chapterId': 'ch-08',
    'title': 'Genesis, Swaran Singh Committee & Enactment (Article 51A)',
    'subtitle': '42nd Amendment Act 1976 & 86th Amendment Act 2002',
    'articleRef': 'Article 51A',
    'learningObjective': 'Trace the historical inclusion of Part IVA in 1976, analyze the Swaran Singh Committee recommendations, and examine the addition of the 11th duty in 2002.',
    'detailedExplanation': """
<h3>1. Genesis of Fundamental Duties</h3>
<p>The original Constitution of 1950 contained Fundamental Rights and Directive Principles, but did not incorporate Fundamental Duties of citizens. The framers assumed that citizens of free India would voluntarily perform their moral obligations. However, during the Internal Emergency (1975–77), the necessity of codifying citizen obligations was felt.</p>

<h3>2. The Swaran Singh Committee Recommendations (1976)</h3>
<p>In 1976, the Congress Party set up the <strong>Sardar Swaran Singh Committee</strong> to make recommendations regarding fundamental duties:</p>
<ul>
  <li>Recommended the inclusion of a separate chapter on Fundamental Duties in the Constitution.</li>
  <li>Emphasized that citizens should be conscious that along with rights, they have certain duties.</li>
  <li><em>Recommendations NOT accepted:</em>
    <ul>
      <li>Parliament to prescribe penalties or punishment for failure to fulfill duties.</li>
      <li>Such penal law not to be questioned in any court on the ground of infringement of Fundamental Rights.</li>
      <li>Duty to pay taxes as a fundamental duty.</li>
    </ul>
  </li>
</ul>

<h3>3. Enactment via the 42nd and 86th Amendments</h3>
<ul>
  <li><strong>42nd Constitutional Amendment Act, 1976:</strong>
    <ul>
      <li>Added a new Part: <strong>Part IVA</strong>.</li>
      <li>Consisted of only one article: <strong>Article 51A</strong>.</li>
      <li>Enacted <strong>10 Fundamental Duties</strong>, inspired by the Constitution of the erstwhile USSR (none of the major Western democracies, except Japan, incorporated fundamental duties).</li>
    </ul>
  </li>
  <li><strong>86th Constitutional Amendment Act, 2002:</strong>
    <ul>
      <li>Added the <strong>11th Fundamental Duty</strong> under clause (k): <em>"Who is a parent or guardian to provide opportunities for education to his child or, as the case may be, ward between the age of six and fourteen years."</em></li>
      <li>Enacted concurrently with Article 21A (Fundamental Right to Education) and substituted Article 45 (Early childhood care).</li>
    </ul>
  </li>
</ul>
""",
    'quickRevisionPoints': [
        'Fundamental Duties were NOT in the original Constitution of 1950.',
        'Recommended by the Sardar Swaran Singh Committee (1976).',
        'Inspired by the USSR Constitution.',
        'Inserted by the 42nd Amendment Act 1976 as Part IVA (Article 51A) with 10 duties.',
        '11th duty (education for children 6-14 years) added by 86th Amendment Act 2002.',
        'Duty to pay taxes was recommended by Swaran Singh Committee but REJECTED by Parliament.'
    ],
    'provisions': [
        {'provision': 'Part IVA', 'title': 'Fundamental Duties', 'description': 'Single-article constitutional part containing citizen duties.'},
        {'provision': 'Article 51A(k)', 'title': 'Duty of Education', 'description': 'Parental duty to educate children aged 6 to 14 years.'}
    ],
    'definitions': [
        {'term': 'Civic & Moral Obligations', 'definition': 'Citizen responsibilities serving as a moral compass to foster patriotism, national unity, and respect for public property and constitutional ideals.'}
    ],
    'ingredients': [
        'Applicable exclusively to Indian citizens (not to foreigners).',
        'Non-justiciable and non-enforceable per se without statutory enabling legislation.',
        'Direct relationship with democratic civic responsibility.'
    ],
    'exceptions': [
        'Failure to perform a Fundamental Duty does not attract direct constitutional penalties unless backed by specific statutory penal laws (e.g., Prevention of Insults to National Honour Act).'
    ],
    'examples': [
        {'scenario': 'A person refuses to stand up during the playing of the National Anthem in a public assembly.', 'application': 'Violates Article 51A(a); can be penalized under the statutory provisions of the Prevention of Insults to National Honour Act, 1971 (Bijoe Emmanuel v. State of Kerala, 1986).'}
    ],
    'landmarkCases': [
        {'case': 'Bijoe Emmanuel v. State of Kerala (National Anthem Case)', 'citation': '(1986) 3 SCC 615', 'year': '1986', 'bench': 'Chinnappa Reddy J', 'ratio': 'Jehovah’s Witnesses school children refused to sing the National Anthem due to religious beliefs, but stood respectfully. Held that standing respectfully showed proper respect under Article 51A(a) and expelling them violated Article 19(1)(a) and 25.', 'impact': 'Balanced Fundamental Rights against Fundamental Duties.'}
    ],
    'comparisonTables': [
        {
            'title': 'Original 10 Duties (1976) vs 11th Duty (2002)',
            'headers': ['Aspect', '42nd Amendment Act (1976)', '86th Amendment Act (2002)'],
            'rows': [
                ['Number of Duties', '10 Fundamental Duties (clauses a to j)', '11th Duty added (clause k)'],
                ['Subject Matter', 'Patriotism, environment, heritage, scientific temper', 'Parental duty to educate child (6–14 yrs)'],
                ['Committee Origin', 'Sardar Swaran Singh Committee', 'Tapas Majumdar Committee / 86th Amendment report']
            ]
        }
    ],
    'diagramId': 'diag-duties-evolution',
    'diagramExplanation': 'The timeline details the 1976 Swaran Singh genesis, the 42nd Amendment enactment, and the 2002 86th Amendment expansion.',
    'misconceptions': [
        {'myth': 'Fundamental Duties apply to all persons residing in India including foreigners.', 'reality': 'Unlike certain Fundamental Rights (Arts. 14, 21), Fundamental Duties under Article 51A apply EXCLUSIVELY to citizens of India.'},
        {'myth': 'The duty to pay taxes is a Fundamental Duty under Article 51A.', 'reality': 'The Swaran Singh Committee recommended making tax payment a duty, but Parliament did NOT accept this recommendation.'}
    ],
    'prelimTraps': [
        {'trap': 'Which country inspired the inclusion of Fundamental Duties in India?', 'reality': 'The USSR (Soviet Union).', 'rule': 'Duties = USSR.'},
        {'trap': 'How many duties were added by the 42nd Amendment in 1976?', 'reality': '10 duties. The 11th duty was added in 2002 by the 86th Amendment.', 'rule': '1976 = 10 duties; 2002 = 11th duty.'}
    ],
    'flashcards': [
        {'id': 'fc-08-01', 'front': 'Which committee recommended the inclusion of Fundamental Duties?', 'back': 'Sardar Swaran Singh Committee (1976).', 'category': 'Constitutional Committees'},
        {'id': 'fc-08-02', 'front': 'Under which Part and Article are Fundamental Duties located?', 'back': 'Part IVA, Article 51A.', 'category': 'Constitutional Text'},
        {'id': 'fc-08-03', 'front': 'Which amendment added the 11th Fundamental Duty regarding education?', 'back': 'The 86th Constitutional Amendment Act, 2002.', 'category': 'Amendments'}
    ],
    'sourceReferences': [
        {'title': 'Constitution (Forty-second Amendment) Act, 1976', 'url': 'https://legislative.gov.in'},
        {'title': 'Bijoe Emmanuel v. State of Kerala (1986) 3 SCC 615', 'url': 'https://main.sci.gov.in'}
    ]
}

# TOPIC 11: Analysis of the 11 Duties & Legal Enforcement
data['top-const-08-02'] = {
    'topicId': 'top-const-08-02',
    'chapterId': 'ch-08',
    'title': 'Analysis of the 11 Duties & Legal Enforcement',
    'subtitle': 'Verma Committee on Fundamental Duties & Judicial Application',
    'articleRef': 'Article 51A(a) to (k)',
    'learningObjective': 'Master the 11 individual duties under Article 51A, analyze the Justice Verma Committee report, and examine how courts use duties to interpret reasonableness under Article 19.',
    'detailedExplanation': """
<h3>1. The 11 Fundamental Duties (Article 51A)</h3>
<p>It shall be the duty of every citizen of India:</p>
<ol type="a">
  <li>To abide by the Constitution and respect its ideals and institutions, the <strong>National Flag and the National Anthem</strong>;</li>
  <li>To cherish and follow the <strong>noble ideals</strong> that inspired the national struggle for freedom;</li>
  <li>To uphold and protect the <strong>sovereignty, unity and integrity</strong> of India;</li>
  <li>To defend the country and render <strong>national service</strong> when called upon to do so;</li>
  <li>To promote <strong>harmony and the spirit of common brotherhood</strong> amongst all the people of India transcending religious, linguistic and regional or sectional diversities and to <strong>renounce practices derogatory to the dignity of women</strong>;</li>
  <li>To value and preserve the rich heritage of the country’s <strong>composite culture</strong>;</li>
  <li>To protect and improve the <strong>natural environment</strong> including forests, lakes, rivers and wildlife and to have compassion for living creatures;</li>
  <li>To develop <strong>scientific temper, humanism</strong> and the spirit of inquiry and reform;</li>
  <li>To safeguard <strong>public property</strong> and to abjure violence;</li>
  <li>To strive towards <strong>excellence in all spheres</strong> of individual and collective activity so that the nation constantly rises to higher levels of endeavour and achievement;</li>
  <li>Who is a parent or guardian to provide <strong>opportunities for education</strong> to his child or ward between the age of six and fourteen years (added by 86th Amendment 2002).</li>
</ol>

<h3>2. The Justice J.S. Verma Committee (1999)</h3>
<p>The Justice Verma Committee was appointed by the Government of India in 1998 to operationalize the teaching of Fundamental Duties in educational institutions. The Committee identified existing legal provisions that enforce several Fundamental Duties:</p>
<ul>
  <li><em>Prevention of Insults to National Honour Act, 1971:</em> Enforces Art. 51A(a) (insults to Flag, Constitution, Anthem).</li>
  <li><em>Unlawful Activities (Prevention) Act, 1967 (UAPA):</em> Enforces Art. 51A(c) (sovereignty and integrity).</li>
  <li><em>Indian Penal Code, 1860 / BNS, 2023:</em> Section 153A/153B (promoting enmity on religion/caste) enforces Art. 51A(e).</li>
  <li><em>Protection of Civil Rights Act, 1955:</em> Enforces equality and brotherhood.</li>
  <li><em>Wildlife (Protection) Act, 1972 & Forest (Conservation) Act, 1980:</em> Enforce Art. 51A(g).</li>
  <li><em>Prevention of Damage to Public Property Act, 1984:</em> Enforces Art. 51A(i).</li>
</ul>

<h3>3. Judicial Enforcement & Interpretation</h3>
<ul>
  <li><strong>AIIMS Students' Union v. AIIMS ((2002) 1 SCC 428):</strong> The Supreme Court held: <em>"Fundamental Duties, though not enforceable by a writ of the court, are yet not meaningless. They cannot be overlooked by the courts. When the court is called upon to determine the constitutional validity of a law or the reasonableness of a restriction under Article 19, the Directive Principles and Fundamental Duties provide valuable guidance."</em></li>
  <li><strong>State of Gujarat v. Mirzapur Moti Kureshi Kassab Jamat ((2005) 8 SCC 534):</strong> A 7-Judge bench upheld a total ban on cow slaughter, ruling that Article 51A(g) (compassion for living creatures) read with Article 48 constitutes a "reasonable restriction" on Article 19(1)(g).</li>
</ul>
""",
    'quickRevisionPoints': [
        'Article 51A contains 11 duties: Clauses (a) through (k).',
        'Clause (e) includes the duty to renounce practices derogatory to the dignity of women.',
        'Clause (g) mandates protection of natural environment and compassion for living creatures.',
        'Clause (h) mandates development of scientific temper and humanism.',
        'Justice Verma Committee (1999) documented statutory enactments enforcing Fundamental Duties.',
        'Courts use Fundamental Duties to judge the "reasonableness" of statutory restrictions under Article 19.'
    ],
    'provisions': [
        {'provision': 'Article 51A(e)', 'title': 'Dignity of Women', 'description': 'Promote brotherhood and renounce practices derogatory to women.'},
        {'provision': 'Article 51A(g)', 'title': 'Environmental Compassion', 'description': 'Protect forests, lakes, rivers, wildlife, and compassion for animals.'},
        {'provision': 'Article 51A(h)', 'title': 'Scientific Temper', 'description': 'Develop scientific inquiry, humanism, and spirit of reform.'}
    ],
    'definitions': [
        {'term': 'Scientific Temper', 'definition': 'A rational, evidence-based, inquiring attitude that questions orthodoxy, dogma, and superstition in public and private life.'},
        {'term': 'Composite Culture', 'definition': 'The multi-ethnic, multi-religious, syncretic heritage of India embodying tolerance, artistic pluralism, and mutual respect.'}
    ],
    'ingredients': [
        'Positive civic and moral commitment by citizens.',
        'Statutory criminal enforcement through targeted penal enactments.',
        'Use as an interpretive aid to support progressive social legislation.'
    ],
    'exceptions': [
        'Citizens cannot be fined or imprisoned directly under Article 51A; penal sanction requires a separate parliamentary statute.'
    ],
    'examples': [
        {'scenario': 'A person dumps toxic industrial chemicals into a sacred river, claiming a religious ritual exception.', 'application': 'Actionable under the Water Act and Environment Protection Act read in the light of Article 51A(g) (duty to protect natural environment).'}
    ],
    'landmarkCases': [
        {'case': 'State of Gujarat v. Mirzapur Moti Kureshi Kassab Jamat', 'citation': '(2005) 8 SCC 534', 'year': '2005', 'bench': '7-Judge Bench (Lahoti CJ)', 'ratio': 'Held that constitutional amendments have introduced Fundamental Duties; hence restrictions on fundamental rights enacted to implement Article 51A(g) are inherently reasonable under Article 19.', 'impact': 'Elevated Fundamental Duties as a test of constitutional reasonableness.'},
        {'case': "AIIMS Students' Union v. AIIMS", 'citation': '(2002) 1 SCC 428', 'year': '2002', 'bench': '3-Judge Bench (Lahoti J)', 'ratio': 'Held that Fundamental Duties are equally important as Fundamental Rights; every citizen has a duty to strive for excellence under Article 51A(j).', 'impact': 'Applied duty of excellence to strike down arbitrary institutional quotas.'}
    ],
    'comparisonTables': [
        {
            'title': 'Duties vs Statutory Penal Enactments',
            'headers': ['Fundamental Duty Clause', 'Direct Enforcing Statute'],
            'rows': [
                ['Art. 51A(a) [Flag & Anthem]', 'Prevention of Insults to National Honour Act, 1971'],
                ['Art. 51A(c) [Sovereignty & Integrity]', 'Unlawful Activities (Prevention) Act, 1967 (UAPA)'],
                ['Art. 51A(e) [Harmony & Brotherhood]', 'Section 153A, Indian Penal Code / BNS, 2023'],
                ['Art. 51A(g) [Forests & Wildlife]', 'Wildlife (Protection) Act, 1972 & Forest Act, 1980'],
                ['Art. 51A(i) [Public Property]', 'Prevention of Damage to Public Property Act, 1984']
            ]
        }
    ],
    'diagramId': 'diag-11-duties-grid',
    'diagramExplanation': 'The 11-panel diagram groups the duties into national symbols, patriotic ideals, social harmony, environment, and personal striving.',
    'misconceptions': [
        {'myth': 'A court can issue a writ of mandamus compelling a citizen to perform a Fundamental Duty under Article 51A.', 'reality': 'Mandamus cannot be issued directly to enforce a Fundamental Duty; enforcement requires a legislative statute passed by Parliament.'}
    ],
    'prelimTraps': [
        {'trap': 'Under which clause is "renouncing practices derogatory to the dignity of women" found?', 'reality': 'Clause (e) of Article 51A.', 'rule': 'Art. 51A(e) = Brotherhood & Dignity of Women.'},
        {'trap': 'Under which clause is "developing scientific temper" found?', 'reality': 'Clause (h) of Article 51A.', 'rule': 'Art. 51A(h) = Scientific temper.'}
    ],
    'flashcards': [
        {'id': 'fc-08-04', 'front': 'Which clause of Article 51A mandates the development of "scientific temper"?', 'back': 'Article 51A(h).', 'category': 'Constitutional Clauses'},
        {'id': 'fc-08-05', 'front': 'Which clause mandates renouncing practices derogatory to the dignity of women?', 'back': 'Article 51A(e).', 'category': 'Constitutional Clauses'},
        {'id': 'fc-08-06', 'front': 'Which committee in 1999 identified existing legal provisions enforcing Fundamental Duties?', 'back': 'Justice J.S. Verma Committee.', 'category': 'Judicial Committees'}
    ],
    'sourceReferences': [
        {'title': 'Justice J.S. Verma Committee Report on Fundamental Duties (1999)', 'url': 'https://ncert.nic.in'},
        {'title': "AIIMS Students' Union v. AIIMS (2002) 1 SCC 428", 'url': 'https://main.sci.gov.in'}
    ]
}

# Write Part 2 output
js_content = "/**\n * Constitution Concepts — Part 2 (Chapters 6 to 8)\n * 11 Comprehensive, verified topics\n */\n"
js_content += "(function() {\n  'use strict';\n  const PART2 = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n\n"
js_content += "  if (typeof window !== 'undefined') { window.CONSTITUTION_CONCEPTS_PART2 = PART2; }\n"
js_content += "  if (typeof module !== 'undefined' && module.exports) { module.exports = PART2; }\n})();\n"

with open(r"C:\Users\tauqe\Documents\Tanveer_Ashraf_Judicial\assets\learning\data\constitution\constitution-concepts-part2.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully wrote constitution-concepts-part2.js with {len(data)} topics.")
