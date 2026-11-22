# -*- coding: utf-8 -*-
"""
Appends Chapters 3, 4, 5 and writes assets/learning/data/constitution/constitution-concepts-part1.js
"""
import sys

code = '''
# ----------------------------------------------------
# CHAPTER 3: THE PREAMBLE
# ----------------------------------------------------

# TOPIC 7: Text, Ideals & Expressions of Preamble
data['top-const-03-01'] = {
    'topicId': 'top-const-03-01',
    'chapterId': 'ch-03',
    'title': 'Text, Ideals & Grand Expressions of the Preamble',
    'subtitle': 'Sovereign, Socialist, Secular, Democratic, Republic, Justice, Liberty, Equality, Fraternity',
    'articleRef': 'Preamble',
    'learningObjective': 'Analyze the philosophical foundations of the Constitution, examine each key term in the Preamble, and study the 42nd Amendment changes.',
    'detailedExplanation': """
<h3>1. The Text and Opening Phrase</h3>
<p>The Preamble to the Constitution of India is based on the <em>"Objectives Resolution"</em> drafted and moved by Pandit Jawaharlal Nehru on December 13, 1946, and adopted on January 22, 1947.</p>
<p><strong>Opening Words:</strong> <em>"WE, THE PEOPLE OF INDIA..."</em> emphasizes popular sovereignty—that ultimate political and legal authority resides with the citizens of India, not a monarch, foreign parliament, or divine right.</p>

<h3>2. The Nature of the Indian State (Five Pillars)</h3>
<ul>
  <li><strong>SOVEREIGN:</strong> Complete external and internal independence. India is not a dominion or dependency of any foreign power and is free to conduct its own internal affairs and foreign policy. Membership of the Commonwealth or United Nations does not curtail this constitutional sovereignty.</li>
  <li><strong>SOCIALIST:</strong> Added by the <strong>42nd Constitutional Amendment Act, 1976</strong>. India adheres to <em>Democratic Socialism</em> (a mixed economy where public and private sectors co-exist), not Communist/Marxist State socialism. In <em>Excel Wear v. Union of India (1978)</em> and <em>D.S. Nakara v. Union of India (1983)</em>, the Supreme Court held that democratic socialism aims to end poverty, ignorance, disease, and inequality of opportunity.</li>
  <li><strong>SECULAR:</strong> Added by the <strong>42nd Amendment Act, 1976</strong>. India practices positive secularism—giving equal respect and protection to all religions, without recognizing any state religion (Articles 25–28). In <em>S.R. Bommai (1994)</em>, secularism was held to be an unalterable part of the Basic Structure.</li>
  <li><strong>DEMOCRATIC:</strong> Political democracy based on universal adult suffrage (Art. 326), periodic free and fair elections, rule of law, independence of judiciary, and freedom from arbitrary executive governance. Includes social and economic democracy (Dr. B.R. Ambedkar: "Political democracy cannot last unless there lies at the base of it social democracy").</li>
  <li><strong>REPUBLIC:</strong> Signifies that the head of the State (the President of India) is elected by the people indirectly for a fixed term (5 years), not hereditary like the British Crown. It also signifies the absence of any privileged class; public offices are open to every citizen without discrimination.</li>
</ul>

<h3>3. The Four Great Objectives of the Constitution</h3>
<ul>
  <li><strong>JUSTICE:</strong> Social, Economic, and Political (borrowed from the 1917 Russian Revolution). Social justice means equal treatment without caste, color, or gender bias; Economic justice means elimination of glaring wealth inequalities; Political justice means equal access to political offices and equal voice.</li>
  <li><strong>LIBERTY:</strong> Of thought, expression, belief, faith, and worship (secured via Fundamental Rights, Arts. 19 & 25–28). Liberty is not absolute license; it is regulated by constitutional restrictions.</li>
  <li><strong>EQUALITY:</strong> Of status and of opportunity (secured via Articles 14–18), ensuring the abolition of special privileges and adequate opportunities for all.</li>
  <li><strong>FRATERNITY:</strong> Assuring the dignity of the individual and the <strong>unity and integrity of the Nation</strong> (the words <em>"and integrity"</em> were added by the 42nd Amendment, 1976). Promotes common brotherhood transcending linguistic, regional, and religious diversities.</li>
</ul>
""",
    'quickRevisionPoints': [
        'Preamble is based on Nehru’s Objective Resolution (moved Dec 13, 1946; adopted Jan 22, 1947).',
        'Amended only ONCE so far: 42nd Constitutional Amendment Act, 1976.',
        '42nd Amendment added THREE words: "SOCIALIST", "SECULAR", and "and INTEGRITY".',
        'Five descriptors of State: Sovereign, Socialist, Secular, Democratic, Republic.',
        'Four objectives: Justice (Social, Economic, Political), Liberty, Equality, Fraternity.',
        'Source of power: "We, the People of India" (popular sovereignty).',
        'Adoption date mentioned in Preamble: 26th day of November, 1949.'
    ],
    'provisions': [
        {'provision': 'Preamble', 'title': 'Solemn Declaration', 'description': 'Declares the character of the Republic and resolves to secure Justice, Liberty, Equality, Fraternity.'},
        {'provision': 'Constitution (42nd Amendment) Act, 1976, s. 2', 'title': 'Preamble Amendment', 'description': 'Inserted Socialist, Secular, and Unity and Integrity.'}
    ],
    'definitions': [
        {'term': 'Democratic Socialism', 'definition': 'A socio-economic philosophy combining democratic parliamentary institutions with welfare state policies to eliminate poverty and inequality in a mixed economy.'},
        {'term': 'Positive Secularism', 'definition': 'The Indian constitutional doctrine treating all religious faiths with equal benevolence, respect, and non-preferential state protection.'}
    ],
    'ingredients': [
        'Source of authority: Derives legitimacy directly from the People of India.',
        'Nature of Indian polity: Sovereign, Socialist, Secular, Democratic, Republic.',
        'Objectives to be achieved: Justice, Liberty, Equality, Fraternity.',
        'Date of adoption: November 26, 1949.'
    ],
    'exceptions': [
        'The Preamble is neither a direct source of legislative power nor a limitation upon legislative powers.',
        'The Preamble is non-justiciable (its provisions are not directly enforceable in courts of law on their own).'
    ],
    'examples': [
        {'scenario': 'A citizen files a writ petition seeking to enforce the term "Economic Justice" to claim a free housing grant directly from the State.', 'application': 'Dismissed as not maintainable, because the Preamble is non-justiciable and cannot create enforceable legal causes of action independent of specific statutory or constitutional provisions.'}
    ],
    'landmarkCases': [
        {'case': 'D.S. Nakara v. Union of India', 'citation': '(1983) 1 SCC 305', 'year': '1983', 'bench': '5-Judge Bench (Desai J)', 'ratio': 'Held that the socialist framework of the Preamble provides a guide to the courts to interpret welfare statutes generously in favor of disadvantaged pensioners.', 'impact': 'Interpreted "Socialist" as meaning social security and protection for weaker sections.'},
        {'case': 'Excel Wear v. Union of India', 'citation': '(1978) 4 SCC 224', 'year': '1978', 'bench': '5-Judge Bench (Untwalia J)', 'ratio': 'Held that the addition of the word "Socialist" does not permit the State to completely ignore the fundamental right of employers to close down an unviable private business.', 'impact': 'Affirmed that Indian socialism is democratic and does not abrogate private enterprise rights.'}
    ],
    'comparisonTables': [
        {
            'title': 'Original Preamble (1949) vs Amended Preamble (Post-1976)',
            'headers': ['Feature', 'Original 1949 Preamble', 'Post-42nd Amendment 1976'],
            'rows': [
                ['Polity Description', 'Sovereign Democratic Republic', 'Sovereign Socialist Secular Democratic Republic'],
                ['Fraternity Clause', 'Unity of the Nation', 'Unity and Integrity of the Nation'],
                ['Socialism Type', 'Implicit in DPSP (Arts. 38, 39)', 'Explicitly incorporated in Preamble text'],
                ['Secularism Status', 'Implicit in Arts. 25–28', 'Explicitly incorporated in Preamble text']
            ]
        }
    ],
    'diagramId': 'diag-preamble-pillars',
    'diagramExplanation': 'The visual schematic presents the Preamble as a constitutional temple supported by the five pillars of State nature and capped by the four fundamental objectives.',
    'misconceptions': [
        {'myth': 'The Preamble was amended twice.', 'reality': 'The Preamble has been amended only ONCE in Indian constitutional history, by the 42nd Amendment Act of 1976.'},
        {'myth': 'Secularism and Socialism were absent from the original Constitution.', 'reality': 'Both ideals were already deeply embedded implicitly in the Directive Principles (Arts. 38, 39) and Fundamental Rights (Arts. 25–28); the 42nd Amendment made them explicit.'}
    ],
    'prelimTraps': [
        {'trap': 'Order of words in the Preamble.', 'reality': 'SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC, REPUBLIC (Mnemonic: S-S-S-D-R).', 'rule': 'Sovereign -> Socialist -> Secular -> Democratic -> Republic.'},
        {'trap': 'Order of the types of Justice mentioned.', 'reality': 'Social, Economic, and Political (Justice comes first among the four objectives).', 'rule': 'Justice -> Liberty -> Equality -> Fraternity.'}
    ],
    'flashcards': [
        {'id': 'fc-03-01', 'front': 'Which constitutional amendment inserted the words "Socialist", "Secular", and "Integrity" into the Preamble?', 'back': 'The 42nd Constitutional Amendment Act, 1976.', 'category': 'Preamble Amendments'},
        {'id': 'fc-03-02', 'front': 'On which resolution was the Preamble originally based?', 'back': 'The Objective Resolution moved by Jawaharlal Nehru on Dec 13, 1946.', 'category': 'Historical Genesis'},
        {'id': 'fc-03-03', 'front': 'From which country’s revolution was the ideal of "Justice (Social, Economic, Political)" borrowed?', 'back': 'Russian Revolution (1917).', 'category': 'Foreign Influences'},
        {'id': 'fc-03-04', 'front': 'From which country were "Liberty, Equality, Fraternity" borrowed?', 'back': 'French Revolution (1789).', 'category': 'Foreign Influences'}
    ],
    'sourceReferences': [
        {'title': 'Constituent Assembly Debates, Vol. X (Adoption of Preamble)', 'url': 'https://www.constitutionofindia.net'},
        {'title': 'Kesavananda Bharati v. State of Kerala (1973) 4 SCC 225', 'url': 'https://main.sci.gov.in'}
    ]
}

# TOPIC 8: Legal Status & Amendability of Preamble
data['top-const-03-02'] = {
    'topicId': 'top-const-03-02',
    'chapterId': 'ch-03',
    'title': 'Legal Status, Enforceability & Amendability of the Preamble',
    'subtitle': 'Berubari Union (1960), Kesavananda Bharati (1973) & LIC of India (1995)',
    'articleRef': 'Preamble Jurisprudence',
    'learningObjective': 'Master the landmark judicial evolution regarding whether the Preamble is part of the Constitution and the limits of its amendability under Article 368.',
    'detailedExplanation': """
<h3>1. The Historic Judicial Debate</h3>
<p>The legal status of the Preamble has witnessed one of the most dramatic jurisprudential evolutions in Indian constitutional history, spanning three pivotal Supreme Court decisions:</p>

<h3>2. The Berubari Union Case (1960): Not a Part of the Constitution</h3>
<ul>
  <li>In <em>In Re Berubari Union and Exchange of Enclaves (AIR 1960 SC 845)</em>, an 8-Judge bench of the Supreme Court held:
    <ul>
      <li>The Preamble is a <em>"key to open the mind of the makers"</em>, illustrating the general purpose behind several provisions.</li>
      <li>However, <strong>the Preamble is NOT part of the Constitution</strong>.</li>
      <li>Consequently, it is not a source of substantive power and cannot be invoked to control or restrict unambiguous language in the operative body of the Constitution.</li>
    </ul>
  </li>
</ul>

<h3>3. The Kesavananda Bharati Landmark (1973): An Integral Part</h3>
<ul>
  <li>In <em>Kesavananda Bharati v. State of Kerala ((1973) 4 SCC 225)</em>, the largest bench in Indian history (13 Judges) decisively <strong>overruled the Berubari Union opinion</strong> on this point:
    <ul>
      <li><strong>The Preamble IS an integral part of the Constitution.</strong> The Court noted historical evidence that the Constituent Assembly voted upon and passed the Preamble as part of the Constitution after the rest of the Articles were approved.</li>
      <li>The Preamble is of extreme importance, and the Constitution must be read and interpreted in the light of the grand and noble vision expressed in it.</li>
      <li><strong>Amendability under Article 368:</strong> Because it is part of the Constitution, the Preamble <strong>can be amended</strong> under Article 368, subject to the single paramount limitation: the amendment cannot destroy or alter the <strong>Basic Structure</strong> of the Constitution.</li>
    </ul>
  </li>
</ul>

<h3>4. Reaffirmation in Subsequent Judgments</h3>
<ul>
  <li><strong>Union Government v. LIC of India (1995 2 SCC 496):</strong> A 3-Judge bench once again categorically held that the Preamble is an integral part of the Constitution.</li>
  <li><strong>S.R. Bommai v. Union of India (1994 3 SCC 1):</strong> Held that Secularism, as reflected in the Preamble, is part of the unalterable Basic Structure of the Indian Constitution.</li>
</ul>

<h3>5. Present Constitutional Position Summary</h3>
<ol>
  <li>The Preamble is an <strong>integral part of the Constitution</strong>.</li>
  <li>It is <strong>neither a source of legislative power nor a prohibition</strong> upon powers of the legislature.</li>
  <li>It is <strong>non-justiciable</strong> (its provisions are not enforceable in courts of law).</li>
  <li>It is <strong>amendable under Article 368</strong> without damaging the Basic Structure.</li>
</ol>
""",
    'quickRevisionPoints': [
        'Berubari Union (1960): Held Preamble is NOT part of the Constitution.',
        'Kesavananda Bharati (1973): Overruled Berubari; held Preamble IS an integral part of the Constitution.',
        'Preamble CAN be amended under Article 368, provided the Basic Structure is not destroyed.',
        'LIC of India case (1995): Reaffirmed that the Preamble is an integral part of the Constitution.',
        'Preamble is non-justiciable and not an independent source of power, but serves as the supreme interpretative guide.'
    ],
    'provisions': [
        {'provision': 'Article 368', 'title': 'Power of Amendment', 'description': 'Empowers Parliament to amend any provision of the Constitution, including the Preamble, without damaging its Basic Structure.'}
    ],
    'definitions': [
        {'term': 'Non-Justiciable', 'definition': 'A legal provision whose terms cannot be directly enforced through judicial orders, mandamus, or coercive court decrees.'},
        {'term': 'Key to the Mind of Makers', 'definition': 'The classic characterization of the Preamble used by the Supreme Court to signify its role as an illuminative interpretative tool for resolving ambiguous statutory language.'}
    ],
    'ingredients': [
        'Voted upon and adopted by the Constituent Assembly in the same manner as other parts.',
        'Operates as an aid to statutory and constitutional interpretation.',
        'Protected by the doctrine of Basic Structure against destructive constitutional amendments.'
    ],
    'exceptions': [
        'Cannot be invoked to override clear, unambiguous constitutional provisions.',
        'Cannot independently support a petition for violation of fundamental rights unless tied to a substantive provision in Part III.'
    ],
    'examples': [
        {'scenario': 'A litigant challenges the 42nd Amendment Act 1976 on the ground that Parliament had no power to amend the Preamble under Article 368.', 'application': 'Rejected by courts, because Kesavananda Bharati established that the Preamble, being part of the Constitution, is amendable under Article 368 as long as the Basic Structure is preserved.'}
    ],
    'landmarkCases': [
        {'case': 'In Re Berubari Union', 'citation': 'AIR 1960 SC 845', 'year': '1960', 'bench': '8-Judge Bench (Gajendragadkar J)', 'ratio': 'Held that the Preamble was not a part of the Constitution, though it was a key to the minds of the framers.', 'impact': 'Later overruled by Kesavananda Bharati in 1973.'},
        {'case': 'Kesavananda Bharati v. State of Kerala', 'citation': '(1973) 4 SCC 225', 'year': '1973', 'bench': '13-Judge Bench (Sikri CJ)', 'ratio': 'Explicitly overruled Berubari Union. Held that Preamble is part of the Constitution and can be amended under Article 368 without altering the Basic Structure.', 'impact': 'Established the definitive modern status of the Preamble.'},
        {'case': 'LIC of India v. Consumer Education and Research Centre', 'citation': '(1995) 2 SCC 496', 'year': '1995', 'bench': '3-Judge Bench', 'ratio': 'Reiterated that the Preamble is an integral part of the Constitution of India.', 'impact': 'Solidified precedent in consumer and socio-economic rights.'}
    ],
    'comparisonTables': [
        {
            'title': 'Berubari (1960) vs Kesavananda (1973)',
            'headers': ['Aspect', 'Berubari Union (1960)', 'Kesavananda Bharati (1973)'],
            'rows': [
                ['Bench Strength', '8 Judges', '13 Judges (Overruled Berubari)'],
                ['Is Preamble Part of Constitution?', 'NO', 'YES (Integral Part)'],
                ['Amendability under Art. 368', 'Could not be amended as an article', 'CAN be amended without destroying Basic Structure'],
                ['Enforceability', 'Non-justiciable', 'Non-justiciable, but supreme interpretative guide']
            ]
        }
    ],
    'diagramId': 'diag-preamble-jurisprudence',
    'diagramExplanation': 'The timeline traces the judicial shift from Berubari Union (1960) through Kesavananda Bharati (1973) to LIC of India (1995).',
    'misconceptions': [
        {'myth': 'The Preamble is enforceable in a High Court under Article 226.', 'reality': 'The Preamble is non-justiciable; a court cannot issue a writ solely to enforce the Preamble without a specific substantive provision.'},
        {'myth': 'Because the Preamble is part of the Basic Structure, it cannot be amended at all.', 'reality': 'The Preamble CAN be amended (and was amended in 1976). Only amendments that destroy the Basic Structure are prohibited.'}
    ],
    'prelimTraps': [
        {'trap': 'Did Kesavananda Bharati hold that the Preamble cannot be amended?', 'reality': 'NO. Kesavananda held that the Preamble CAN be amended under Article 368, but its basic features cannot be abrogated.', 'rule': 'Preamble is amendable under Article 368.'},
        {'trap': 'Is the Preamble an independent source of power for Parliament?', 'reality': 'NO. It confers no substantive legislative powers and imposes no direct legislative prohibitions.', 'rule': 'No substantive power in Preamble.'}
    ],
    'flashcards': [
        {'id': 'fc-03-05', 'front': 'Which case first held that the Preamble is NOT part of the Constitution?', 'back': 'In Re Berubari Union (1960).', 'category': 'Judicial Precedents'},
        {'id': 'fc-03-06', 'front': 'Which case overruled Berubari and held the Preamble IS an integral part of the Constitution?', 'back': 'Kesavananda Bharati v. State of Kerala (1973).', 'category': 'Landmark Rulings'},
        {'id': 'fc-03-07', 'front': 'Can the Preamble be amended under Article 368?', 'back': 'Yes, provided the amendment does not alter or destroy the Basic Structure of the Constitution.', 'category': 'Amending Power'},
        {'id': 'fc-03-08', 'front': 'Is the Preamble justiciable in Indian courts?', 'back': 'No, it is non-justiciable (unenforceable on its own).', 'category': 'Judicial Enforceability'}
    ],
    'sourceReferences': [
        {'title': 'Kesavananda Bharati v. State of Kerala (1973) 4 SCC 225', 'url': 'https://main.sci.gov.in'},
        {'title': 'In Re Berubari Union (1960) 3 SCR 250', 'url': 'https://main.sci.gov.in'}
    ]
}

# ----------------------------------------------------
# CHAPTER 4: THE UNION AND ITS TERRITORY
# ----------------------------------------------------

# TOPIC 9: Articles 1 & 2
data['top-const-04-01'] = {
    'topicId': 'top-const-04-01',
    'chapterId': 'ch-04',
    'title': 'Territory of the Union & Admission of States (Articles 1–2)',
    'subtitle': 'India, that is Bharat, shall be a Union of States',
    'articleRef': 'Articles 1 and 2',
    'learningObjective': 'Understand the constitutional definition of India, the distinction between "Union of India" and "Territory of India", and Parliament’s power to admit new territories.',
    'detailedExplanation': """
<h3>1. Article 1: Name and Territory of the Union</h3>
<p>Article 1(1) declares: <em>"India, that is Bharat, shall be a Union of States."</em></p>
<ul>
  <li><strong>Name:</strong> Combines the traditional name <em>Bharat</em> with modern diplomatic name <em>India</em>.</li>
  <li><strong>Polity:</strong> Chosen as "Union of States" rather than "Federation of States" (explained by Dr. B.R. Ambedkar for two vital reasons: (1) Indian federation is not the result of an agreement among the States like the American federation; (2) States have no right to secede from the federation. The federation is an indestructible Union).</li>
  <li><strong>Territory of India vs Union of India:</strong>
    <ul>
      <li><em>"Union of India"</em> is a narrower expression comprising only the States sharing federal distribution of powers.</li>
      <li><em>"Territory of India"</em> is a wider legal expression comprising: (a) Territories of the States; (b) Union Territories (First Schedule); (c) Such other territories as may be acquired by India at any time.</li>
    </ul>
  </li>
</ul>

<h3>2. Article 2: Admission or Establishment of New States</h3>
<p>Article 2 empowers Parliament by law to:</p>
<ul>
  <li><strong>Admit</strong> into the Union new States (states already in existence outside Indian territory, e.g., accession of French or Portuguese enclaves or Sikkim).</li>
  <li><strong>Establish</strong> new States (states not previously in existence).</li>
  <li>Parliament may do so on such terms and conditions as it thinks fit.</li>
  <li><em>Case of Sikkim:</em> Sikkim was associated with India via the 35th Constitutional Amendment (1974) creating Article 2A and 10th Schedule, and subsequently admitted as a full 22nd State of the Indian Union via the 36th Constitutional Amendment Act, 1975 under Article 2.</li>
</ul>
""",
    'quickRevisionPoints': [
        'Article 1(1): "India, that is Bharat, shall be a Union of States."',
        'Union of States means an indestructible union; states have zero right to secede.',
        '"Territory of India" is wider than "Union of India" (includes UTs and acquired territories).',
        'Article 2 empowers Parliament to admit or establish new States not previously part of India.',
        'Sikkim was admitted as the 22nd State under Article 2 via the 36th Amendment Act, 1975.'
    ],
    'provisions': [
        {'provision': 'Article 1', 'title': 'Name and Territory', 'description': 'Categorizes territories of States, Union Territories, and acquired territories.'},
        {'provision': 'Article 2', 'title': 'Admission or Establishment', 'description': 'Plenary parliamentary authority to admit external territories into the Union.'}
    ],
    'definitions': [
        {'term': 'Indestructible Union', 'definition': 'Constitutional principle that the Indian Union cannot be dissolved by state secession or unilateral withdrawal.'},
        {'term': 'Acquired Territory', 'definition': 'Territory acquired by India through international law modes (cession, conquest, purchase, or plebiscite) under Article 1(3)(c).'}
    ],
    'ingredients': [
        'Legal identity: India and Bharat.',
        'Federal status: Non-secessionist Union.',
        'Plenary legislative authority to absorb external foreign territories.'
    ],
    'exceptions': [
        'Article 2 applies only to admission or establishment of territories NOT currently part of India. Reorganisation of existing Indian states is governed by Article 3.'
    ],
    'examples': [
        {'scenario': 'A foreign enclave signs an instrument of cession to join India.', 'application': 'Admitted by Parliament under Article 2, as it involves a territory outside the existing borders of India.'}
    ],
    'landmarkCases': [
        {'case': 'R.C. Poudyal v. Union of India', 'citation': 'AIR 1993 SC 1804', 'year': '1993', 'bench': '5-Judge Bench', 'ratio': 'Examined the scope of Article 2 during the admission of Sikkim. Held that Parliament has wide discretion to prescribe terms and conditions when admitting a new state, subject to basic constitutional values.', 'impact': 'Affirmed wide parliamentary latitude under Article 2.'}
    ],
    'comparisonTables': [
        {
            'title': 'Article 2 vs Article 3',
            'headers': ['Aspect', 'Article 2', 'Article 3'],
            'rows': [
                ['Subject Matter', 'Admission or establishment of NEW States', 'Formation or reorganization of EXISTING States'],
                ['Origin of Territory', 'Territories outside India (foreign)', 'Territories already part of the Indian Union'],
                ['Examples', 'Sikkim (1975), French/Portuguese enclaves', 'Telangana, Uttarakhand, Chhattisgarh, Jharkhand']
            ]
        }
    ],
    'diagramId': 'diag-territory-classes',
    'diagramExplanation': 'The schematic contrasts the wider concentric circle of the "Territory of India" with the inner circle of the "Union of India".',
    'misconceptions': [
        {'myth': 'Article 2 is used to create new states out of existing Indian territory like Telangana or Uttarakhand.', 'reality': 'Creation of new states from existing Indian territory is done under Article 3, NOT Article 2.'}
    ],
    'prelimTraps': [
        {'trap': 'Difference between "Union of India" and "Territory of India".', 'reality': 'Union of India includes only the States; Territory of India includes States, Union Territories, and any acquired territories.', 'rule': 'Territory > Union.'}
    ],
    'flashcards': [
        {'id': 'fc-04-01', 'front': 'How is India described in Article 1(1) of the Constitution?', 'back': '"India, that is Bharat, shall be a Union of States."', 'category': 'Constitutional Text'},
        {'id': 'fc-04-02', 'front': 'Which article governs the admission of new states from outside India?', 'back': 'Article 2.', 'category': 'Constitutional Articles'},
        {'id': 'fc-04-03', 'front': 'Which constitutional amendment admitted Sikkim as a full State?', 'back': '36th Constitutional Amendment Act, 1975 (22nd State).', 'category': 'Amendments'}
    ],
    'sourceReferences': [
        {'title': 'Constitution of India (Official Ministry Edition)', 'url': 'https://legislative.gov.in'},
        {'title': 'R.C. Poudyal v. Union of India (1993) Supp 1 SCC 324', 'url': 'https://main.sci.gov.in'}
    ]
}

# TOPIC 10: Articles 3 & 4
data['top-const-04-02'] = {
    'topicId': 'top-const-04-02',
    'chapterId': 'ch-04',
    'title': 'Reorganisation of States & Cession Jurisprudence (Articles 3–4)',
    'subtitle': 'Formation of New States, Boundary Alterations & Berubari Principle',
    'articleRef': 'Articles 3 and 4',
    'learningObjective': 'Master the procedural requirements under Article 3 for altering state boundaries, and understand the difference between internal boundary adjustment and foreign cession.',
    'detailedExplanation': """
<h3>1. Article 3: Internal Reorganisation of States</h3>
<p>Article 3 authorizes Parliament to enact a law to:</p>
<ul>
  <li>Form a new State by separation of territory from any State or by uniting two or more States or parts of States;</li>
  <li>Increase the area of any State;</li>
  <li>Diminish the area of any State;</li>
  <li>Alter the boundaries of any State;</li>
  <li>Alter the name of any State (e.g., United Provinces to Uttar Pradesh, Madras to Tamil Nadu, Orissa to Odisha).</li>
</ul>

<h3>2. Mandatory Procedural Conditions Under Article 3 Proviso</h3>
<ol>
  <li><strong>Prior Presidential Recommendation:</strong> A Bill for this purpose can be introduced in either House of Parliament <em>only on the recommendation of the President</em>.</li>
  <li><strong>Reference to State Legislature:</strong> Before recommending, the President must refer the Bill to the concerned State Legislature for expressing its views within a specified period.</li>
  <li><strong>State Views are Non-Binding:</strong> Parliament is <strong>NOT bound</strong> to accept the views of the State Legislature. Parliament may accept or reject them. If Parliament amends the Bill, no fresh reference to the State is required (<em>Babulal Parate v. State of Bombay, 1960</em>).</li>
  <li><strong>Enacted by Simple Majority:</strong> The Bill is passed by a simple majority in both Houses of Parliament.</li>
</ol>

<h3>3. Article 4: Not a Constitutional Amendment</h3>
<p>Article 4 declares that any law referred to in Article 2 or Article 3 shall contain necessary amendments of the First Schedule (list of States) and Fourth Schedule (allocation of seats in Rajya Sabha), and <strong>no such law shall be deemed to be an amendment of the Constitution for the purposes of Article 368</strong>. It is passed by simple majority like an ordinary bill.</p>

<h3>4. The Cession of Territory: In Re Berubari Union (1960)</h3>
<p>Does Parliament's power under Article 3 to "diminish the area of any State" include the power to <strong>cede Indian territory to a foreign State</strong>?</p>
<ul>
  <li>In <em>In Re Berubari Union (1960)</em>, the Supreme Court held: <strong>NO.</strong> Article 3 relates only to internal reorganisation between States of India. It does not empower Parliament to cede Indian territory to a foreign power.</li>
  <li>Cession of territory requires a constitutional amendment under <strong>Article 368</strong>.</li>
  <li>Consequently, the 9th Amendment Act 1960 was enacted to transfer Berubari Union to Pakistan, and the 100th Amendment Act 2015 was enacted to exchange enclaves with Bangladesh.</li>
  <li><em>Settlement of boundary disputes</em> not involving cession of territory can be done by pure executive action without constitutional amendment (<em>Maganbhai Ishwarbhai Patel v. UOI, 1969</em>).</li>
</ul>
""",
    'quickRevisionPoints': [
        'Article 3 governs internal reorganisation of states (creating states, altering borders, changing names).',
        'Bill requires prior recommendation of the President.',
        'Bill must be referred to State Legislature for views; views are NOT binding on Parliament.',
        'Passed by simple majority (Art. 4 specifies it is NOT an amendment under Art. 368).',
        'Berubari Union (1960): Article 3 does NOT include power to cede territory to foreign nations.',
        'Cession of Indian territory requires constitutional amendment under Article 368 (e.g. 100th Amendment 2015 for Bangladesh enclaves).'
    ],
    'provisions': [
        {'provision': 'Article 3', 'title': 'Formation of New States', 'description': 'Empowers Parliament to alter state boundaries and names with prior presidential reference.'},
        {'provision': 'Article 4', 'title': 'Laws under Arts. 2 & 3', 'description': 'Explicitly exempts state reorganisation statutes from Article 368 requirements.'}
    ],
    'definitions': [
        {'term': 'Destructible States', 'definition': 'The Indian constitutional reality where state boundaries and identities can be altered or extinguished by Parliament without state consent.'},
        {'term': 'Cession of Territory', 'definition': 'Transfer of sovereign territory from India to a foreign state, requiring a formal constitutional amendment under Article 368.'}
    ],
    'ingredients': [
        'Presidential recommendation prior to parliamentary introduction.',
        'Mandatory consultation reference to affected state legislature.',
        'Enactment by ordinary simple majority in both Houses.'
    ],
    'exceptions': [
        'Settling a disputed boundary between India and a foreign country does not amount to cession and can be implemented by executive agreement without Article 368.'
    ],
    'examples': [
        {'scenario': 'State of Andhra Pradesh Legislature unanimously passes a resolution opposing the creation of Telangana in 2014.', 'application': 'Parliament can validly pass the Andhra Pradesh Reorganisation Act 2014 despite state opposition, as state views under Article 3 are non-binding.'}
    ],
    'landmarkCases': [
        {'case': 'Babulal Parate v. State of Bombay', 'citation': 'AIR 1960 SC 51', 'year': '1960', 'bench': '5-Judge Bench', 'ratio': 'Held that the opinion of the State Legislature under Article 3 proviso is not binding on Parliament. If Parliament introduces amendments to the bill after the state reference, no second reference is required.', 'impact': 'Affirmed absolute parliamentary supremacy in reorganisation.'},
        {'case': 'In Re Berubari Union', 'citation': 'AIR 1960 SC 845', 'year': '1960', 'bench': '8-Judge Bench', 'ratio': 'Held that power to diminish area under Article 3 does not include power to cede Indian territory to a foreign power. Cession requires Article 368 amendment.', 'impact': 'Mandated 9th and 100th Amendments for foreign territorial transfers.'}
    ],
    'comparisonTables': [
        {
            'title': 'Internal Boundary Alteration vs Foreign Cession',
            'headers': ['Parameter', 'Internal Reorganisation (Art. 3)', 'Cession to Foreign Power (Art. 368)'],
            'rows': [
                ['Territorial Effect', 'Shifts borders between Indian states', 'Transfers Indian land to foreign sovereignty'],
                ['Statutory Mechanism', 'Ordinary Law (Simple Majority)', 'Constitutional Amendment (Special Majority)'],
                ['State Consent', 'Views sought, but strictly non-binding', 'Federal ratification where applicable'],
                ['Governing Case', 'Babulal Parate v. State of Bombay (1960)', 'In Re Berubari Union (1960)']
            ]
        }
    ],
    'diagramId': 'diag-state-reorganisation',
    'diagramExplanation': 'The workflow traces the four stages of Article 3: Executive drafting -> Presidential recommendation -> State consultation -> Parliamentary simple majority.',
    'misconceptions': [
        {'myth': 'A State Legislature can veto the division of its territory by voting against the reorganisation bill.', 'reality': 'The State Legislature has no veto power. Parliament can proceed to enact the law even if the State Legislature rejects it unanimously.'},
        {'myth': 'Creation of a new state requires a two-thirds majority under Article 368.', 'reality': 'Article 4 explicitly provides that reorganisation laws require only a simple majority and are not amendments under Article 368.'}
    ],
    'prelimTraps': [
        {'trap': 'Does changing the name of a State require an amendment under Article 368?', 'reality': 'NO. Changing the name of a State is done under Article 3 by simple majority, not Article 368.', 'rule': 'Name change = Article 3 (Simple majority).'},
        {'trap': 'Can Indian territory be ceded to a foreign state by an ordinary Act under Article 3?', 'reality': 'NO. Cession requires a constitutional amendment under Article 368 (Berubari precedent).', 'rule': 'Cession = Article 368.'}
    ],
    'flashcards': [
        {'id': 'fc-04-04', 'front': 'Which article governs the formation of new states from existing Indian territory?', 'back': 'Article 3.', 'category': 'Constitutional Articles'},
        {'id': 'fc-04-05', 'front': 'Is the opinion of a State Legislature on an Article 3 bill binding on Parliament?', 'back': 'No, Parliament can accept, modify, or reject it completely.', 'category': 'Procedural Rules'},
        {'id': 'fc-04-06', 'front': 'What majority is required to pass a bill creating a new State in Parliament?', 'back': 'Simple majority (Article 4 specifies it is not an Art. 368 amendment).', 'category': 'Parliamentary Voting'},
        {'id': 'fc-04-07', 'front': 'Which landmark case mandated that cession of Indian territory requires an Article 368 amendment?', 'back': 'In Re Berubari Union (1960).', 'category': 'Landmark Precedents'}
    ],
    'sourceReferences': [
        {'title': 'Babulal Parate v. State of Bombay, AIR 1960 SC 51', 'url': 'https://main.sci.gov.in'},
        {'title': 'In Re Berubari Union, AIR 1960 SC 845', 'url': 'https://main.sci.gov.in'}
    ]
}

# ----------------------------------------------------
# CHAPTER 5: CITIZENSHIP
# ----------------------------------------------------

# TOPIC 11: Articles 5–8
data['top-const-05-01'] = {
    'topicId': 'top-const-05-01',
    'chapterId': 'ch-05',
    'title': 'Constitutional Citizenship at Commencement (Articles 5–8)',
    'subtitle': 'Domicile, Migration from Pakistan & Overseas Origin',
    'articleRef': 'Articles 5, 6, 7, 8',
    'learningObjective': 'Examine the transitional constitutional citizenship provisions enacted for individuals residing in India on January 26, 1950.',
    'detailedExplanation': """
<h3>1. The Scope of Part II (Articles 5–11)</h3>
<p>Part II of the Constitution does not provide a permanent or comprehensive code for Indian citizenship. It simply determined <strong>who became a citizen of India at the commencement of the Constitution on January 26, 1950</strong>. Subsequent citizenship is regulated by Parliament through ordinary legislation under Article 11 (The Citizenship Act, 1955).</p>

<h3>2. The Four Categories of Citizens at Commencement</h3>
<ol>
  <li><strong>Citizenship by Domicile (Article 5):</strong>
    <p>A person who had their domicile in the territory of India on January 26, 1950, AND fulfilled any ONE of three conditions:</p>
    <ul>
      <li>He was born in the territory of India; OR</li>
      <li>Either of his parents was born in the territory of India; OR</li>
      <li>He had been ordinarily resident in India for not less than 5 years immediately preceding commencement.</li>
    </ul>
  </li>
  <li><strong>Citizenship of Migrants from Pakistan (Article 6):</strong>
    <p>A person who migrated to India from Pakistan became an Indian citizen if:</p>
    <ul>
      <li>He or either of his parents or grandparents was born in undivided India; AND</li>
      <li><em>If migrated before July 19, 1948:</em> He had been ordinarily resident in India since migration; OR</li>
      <li><em>If migrated on or after July 19, 1948:</em> He had been registered as a citizen by an officer after residing in India for at least 6 months prior to application.</li>
    </ul>
  </li>
  <li><strong>Citizenship of Migrants to Pakistan (Article 7):</strong>
    <p>A person who migrated from India to Pakistan after March 1, 1947, ceased to be an Indian citizen. However, if he returned to India under a <strong>permit for resettlement or permanent return</strong>, he became eligible under the same terms as post-July 19, 1948 migrants under Article 6 (requiring 6 months residence and registration).</p>
  </li>
  <li><strong>Persons of Indian Origin Residing Abroad (Article 8):</strong>
    <p>Any person who, or either of whose parents or grandparents, was born in undivided India, and who is ordinarily residing in any country outside undivided India, becomes a citizen if registered by the diplomatic or consular representative of India in that country.</p>
  </li>
</ol>
""",
    'quickRevisionPoints': [
        'Part II (Arts. 5–11) only determined citizenship on January 26, 1950.',
        'Article 5: Citizenship by Domicile (Birth, parent’s birth, or 5-year prior residence).',
        'Article 6: Migrants from Pakistan (Cut-off date: July 19, 1948 for permit system).',
        'Article 7: Overrides Arts. 5 & 6; persons who migrated to Pakistan after March 1, 1947 lost citizenship unless returned under permanent permit.',
        'Article 8: Persons of Indian origin residing abroad registered with Indian consular missions.'
    ],
    'provisions': [
        {'provision': 'Article 5', 'title': 'Citizenship by Domicile', 'description': 'Domicile plus birth, parentage, or 5-year residence.'},
        {'provision': 'Article 6', 'title': 'Pakistan Migrants', 'description': 'Permit system based on July 19, 1948 cut-off date.'},
        {'provision': 'Article 7', 'title': 'Migrants to Pakistan', 'description': 'March 1, 1947 disqualification with resettlement permit exception.'}
    ],
    'definitions': [
        {'term': 'Domicile', 'definition': 'The country in which a person either has or is deemed by law to have their permanent home, requiring both residence (factum) and intention to remain permanently (animus manendi).'},
        {'term': 'Permit System', 'definition': 'The administrative permit system introduced on July 19, 1948 to regulate movement and migration between India and Pakistan.'}
    ],
    'ingredients': [
        'Establishment of Indian domicile or undivided Indian ancestry.',
        'Compliance with statutory cut-off dates (March 1, 1947 and July 19, 1948).',
        'Formal consular or registration certificate where mandatory.'
    ],
    'exceptions': [
        'An individual fulfilling Article 5 loses citizenship if they migrated to Pakistan after March 1, 1947 under Article 7.'
    ],
    'examples': [
        {'scenario': 'A person born in Lahore in 1920 moves to Delhi on June 1, 1948 and resides there.', 'application': 'Becomes an Indian citizen automatically under Article 6(b)(i), as migration occurred before July 19, 1948.'}
    ],
    'landmarkCases': [
        {'case': 'Pradeep Jain v. Union of India', 'citation': '(1984) 3 SCC 654', 'year': '1984', 'bench': '3-Judge Bench (Bhagwati J)', 'ratio': 'Held that there is only one domicile in India—the domicile of India. There is no such thing as a state domicile for Indian citizenship.', 'impact': 'Reinforced single national citizenship and national domicile.'},
        {'case': 'State of Bihar v. Kumar Amar Singh', 'citation': 'AIR 1955 SC 282', 'year': '1955', 'bench': 'Constitution Bench', 'ratio': 'Held that migration under Article 7 means moving from India to Pakistan with the intention of settling permanently.', 'impact': 'Applied Article 7 migration bar strictly.'}
    ],
    'comparisonTables': [
        {
            'title': 'Articles 5, 6, 7 & 8 Comparison',
            'headers': ['Article', 'Target Group', 'Essential Condition', 'Key Cut-Off Date'],
            'rows': [
                ['Article 5', 'Residents in India', 'Domicile + Birth/5-yr residence', '26 January 1950'],
                ['Article 6', 'Migrants from Pakistan', 'Born in undivided India + permit', '19 July 1948'],
                ['Article 7', 'Migrants to Pakistan', 'Lost citizenship unless permit', '1 March 1947'],
                ['Article 8', 'Indians abroad', 'Consular registration', 'At time of application']
            ]
        }
    ],
    'diagramId': 'diag-citizenship-commencement',
    'diagramExplanation': 'The matrix delineates the 4 categories of constitutional citizenship on Jan 26, 1950.',
    'misconceptions': [
        {'myth': 'The Constitution contains the permanent rules for acquiring citizenship today.', 'reality': 'Part II only dealt with citizenship at commencement on Jan 26, 1950. All subsequent citizenship is governed by the Citizenship Act, 1955.'}
    ],
    'prelimTraps': [
        {'trap': 'The cut-off date under Article 6 for Pakistan migrants.', 'reality': 'July 19, 1948 (date permit system was introduced).', 'rule': 'Article 6 = July 19, 1948; Article 7 = March 1, 1947.'}
    ],
    'flashcards': [
        {'id': 'fc-05-01', 'front': 'Which article grants citizenship by domicile at the commencement of the Constitution?', 'back': 'Article 5.', 'category': 'Constitutional Articles'},
        {'id': 'fc-05-02', 'front': 'What is the crucial cut-off date under Article 6 for migrants from Pakistan?', 'back': 'July 19, 1948.', 'category': 'Statutory Cut-Offs'},
        {'id': 'fc-05-03', 'front': 'Can there be separate State domicile in India according to the Supreme Court?', 'back': 'No, there is only one domicile in India—the domicile of the country (Pradeep Jain case).', 'category': 'Judicial Precedents'}
    ],
    'sourceReferences': [
        {'title': 'Pradeep Jain v. Union of India, AIR 1984 SC 1420', 'url': 'https://main.sci.gov.in'},
        {'title': 'Constituent Assembly Debates on Part II', 'url': 'https://www.constitutionofindia.net'}
    ]
}

# TOPIC 12: Articles 9–11 & Citizenship Act 1955
data['top-const-05-02'] = {
    'topicId': 'top-const-05-02',
    'chapterId': 'ch-05',
    'title': 'Single Citizenship, Termination & Statutory Control (Articles 9–11)',
    'subtitle': 'Prohibition of Dual Citizenship & The Citizenship Act, 1955 Framework',
    'articleRef': 'Articles 9, 10, 11',
    'learningObjective': 'Analyze the constitutional bar against dual citizenship, parliamentary supremacy under Article 11, and the modes of acquisition and loss under the Citizenship Act 1955.',
    'detailedExplanation': """
<h3>1. Article 9: Prohibition of Dual Citizenship</h3>
<p>Article 9 embodies the foundational principle of <strong>Single Citizenship</strong>: <em>No person shall be a citizen of India if he has voluntarily acquired the citizenship of any foreign State.</em></p>
<ul>
  <li>Unlike the federal system in the United States or Switzerland, an Indian citizen owes allegiance only to the Union of India; there is no separate state citizenship.</li>
  <li>Voluntary acquisition of foreign nationality results in the <strong>immediate and automatic termination</strong> of Indian citizenship.</li>
</ul>

<h3>2. Articles 10 and 11: Continuance and Plenary Parliamentary Power</h3>
<ul>
  <li><strong>Article 10:</strong> Every person who is or is deemed to be a citizen under Part II shall continue to be such citizen, subject to the provisions of any law made by Parliament.</li>
  <li><strong>Article 11:</strong> Explicitly vests in Parliament the absolute plenary power to make any provision regarding the <strong>acquisition and termination of citizenship and all other matters relating to citizenship</strong>. It overrides Articles 5 to 10.</li>
</ul>

<h3>3. The Citizenship Act, 1955: Acquisition & Termination</h3>
<p>In exercise of Article 11, Parliament enacted the Citizenship Act, 1955, providing five modes of acquisition and three modes of loss:</p>
<h4>A. Five Modes of Acquisition:</h4>
<ol>
  <li><strong>By Birth (Jus soli):</strong> Born in India (subject to amendments of 1986 and 2003 requiring parental citizenship).</li>
  <li><strong>By Descent (Jus sanguinis):</strong> Born outside India to an Indian citizen parent.</li>
  <li><strong>By Registration:</strong> Persons of Indian origin resident in India for 7 years, persons married to Indian citizens, etc.</li>
  <li><strong>By Naturalisation:</strong> Foreigners resident in India for 12 years (11 years + 12 continuous months prior to application) with knowledge of an 8th Schedule language.</li>
  <li><strong>By Incorporation of Territory:</strong> When a new territory becomes part of India (e.g. Goa, Pondicherry, Sikkim).</li>
</ol>

<h4>B. Three Modes of Loss of Citizenship:</h4>
<ol>
  <li><strong>Renunciation:</strong> Voluntary declaration of surrender by an Indian citizen of full age and capacity.</li>
  <li><strong>Termination:</strong> Automatic termination by operation of law when an Indian citizen voluntarily acquires citizenship of another country.</li>
  <li><strong>Deprivation:</strong> Compulsory termination by the Central Government for fraud, false representation, disloyalty to Constitution, treason, or unlawful trade with enemy during war.</li>
</ol>
""",
    'quickRevisionPoints': [
        'Article 9: Voluntary acquisition of foreign citizenship automatically terminates Indian citizenship (Single Citizenship).',
        'Article 11 gives Parliament plenary power to regulate citizenship by law (overriding Arts. 5–10).',
        'Citizenship Act 1955 provides 5 modes of acquisition: Birth, Descent, Registration, Naturalisation, Incorporation.',
        'Citizenship Act 1955 provides 3 modes of loss: Renunciation, Termination, Deprivation.',
        'Overseas Citizen of India (OCI) is a statutory immigration card scheme under the 1955 Act, NOT dual citizenship.'
    ],
    'provisions': [
        {'provision': 'Article 9', 'title': 'Foreign Citizenship Bar', 'description': 'Automatic loss of citizenship upon acquiring foreign nationality.'},
        {'provision': 'Article 11', 'title': 'Parliamentary Lawmaking Power', 'description': 'Plenary authority to regulate acquisition and loss of citizenship.'},
        {'provision': 'Citizenship Act 1955, ss. 3–10', 'title': 'Acquisition and Loss', 'description': 'Comprehensive statutory rules for modern citizenship.'}
    ],
    'definitions': [
        {'term': 'Jus Soli', 'definition': 'Citizenship acquired by virtue of birth within the territorial jurisdiction of the state.'},
        {'term': 'Jus Sanguinis', 'definition': 'Citizenship acquired by virtue of descent or blood relation from citizen parents.'}
    ],
    'ingredients': [
        'Exclusive national allegiance with zero state-level citizenship.',
        'Automatic divestment upon voluntary naturalization abroad.',
        'Statutory supremacy of parliamentary legislation over constitutional commencement rules.'
    ],
    'exceptions': [
        'Deprivation of citizenship does not apply to citizens by birth or descent, only to citizens by registration or naturalisation.'
    ],
    'examples': [
        {'scenario': 'An Indian citizen naturalizes as an American citizen in 2024 and claims he retains Indian citizenship until he formally surrenders his Indian passport.', 'application': 'Rejected under Article 9 and Section 9 of the 1955 Act; Indian citizenship terminates automatically on the exact date foreign citizenship is acquired.'}
    ],
    'landmarkCases': [
        {'case': 'State of Gujarat v. Ambica Mills', 'citation': '(1974) 4 SCC 656', 'year': '1974', 'bench': 'Constitution Bench', 'ratio': 'Confirmed that a corporation is not a citizen within the meaning of Article 19, because citizenship under Part II and the 1955 Act is confined to natural persons.', 'impact': 'Established company legal personality vs natural citizenship.'},
        {'case': 'Kuldip Nayar v. Union of India', 'citation': '(2006) 7 SCC 1', 'year': '2006', 'bench': '5-Judge Bench (Sabharwal CJ)', 'ratio': 'Upheld removal of domicile requirement for contesting Rajya Sabha elections, reiterating the supremacy of Single Citizenship across India.', 'impact': 'Reinforced all-India federal equality.'}
    ],
    'comparisonTables': [
        {
            'title': 'Loss of Indian Citizenship (The Three Modes)',
            'headers': ['Mode', 'Nature of Loss', 'Key Trigger', 'Applicable Citizens'],
            'rows': [
                ['Renunciation (Sec. 8)', 'Voluntary Act', 'Declaration registered with magistrate', 'Adult citizens of sound mind'],
                ['Termination (Sec. 9)', 'Automatic Operation of Law', 'Voluntary acquisition of foreign passport', 'All Indian citizens'],
                ['Deprivation (Sec. 10)', 'Compulsory Order by Centre', 'Fraud, disloyalty to Constitution, treason', 'Naturalised & Registered citizens']
            ]
        }
    ],
    'diagramId': 'diag-citizenship-modes',
    'diagramExplanation': 'The dual-branch flowchart details the 5 channels of acquisition on the left and 3 avenues of loss on the right.',
    'misconceptions': [
        {'myth': 'Overseas Citizen of India (OCI) cardholders possess dual citizenship.', 'reality': 'OCI is merely a statutory lifelong visa facility. OCI cardholders have no political rights, no voting rights, and cannot hold constitutional public offices.'},
        {'myth': 'A registered private company is a citizen of India.', 'reality': 'The Supreme Court in State Trading Corporation (1963) held that corporations are legal persons but NOT citizens.'}
    ],
    'prelimTraps': [
        {'trap': 'Can a citizen by birth be deprived of citizenship by executive order under Section 10 of the 1955 Act?', 'reality': 'NO. Deprivation under Section 10 applies only to citizens by registration or naturalization, not citizens by birth.', 'rule': 'No deprivation for citizens by birth.'},
        {'trap': 'Does India recognize dual citizenship for Non-Resident Indians (NRIs)?', 'reality': 'NO. Article 9 strictly bars dual citizenship. NRIs are Indian citizens holding Indian passports living abroad.', 'rule': 'NRIs = Indian citizens; OCIs = Foreign citizens.'}
    ],
    'flashcards': [
        {'id': 'fc-05-04', 'front': 'Which article bars dual citizenship in India?', 'back': 'Article 9.', 'category': 'Constitutional Articles'},
        {'id': 'fc-05-05', 'front': 'Which article empowers Parliament to regulate citizenship by law?', 'back': 'Article 11.', 'category': 'Constitutional Articles'},
        {'id': 'fc-05-06', 'front': 'What are the five modes of acquiring Indian citizenship under the 1955 Act?', 'back': 'Birth, Descent, Registration, Naturalisation, and Incorporation of Territory.', 'category': 'Statutory Modes'},
        {'id': 'fc-05-07', 'front': 'Is a commercial company or corporation a citizen under the Constitution of India?', 'back': 'No, corporations are juridical persons but not citizens (State Trading Corporation case, 1963).', 'category': 'Judicial Precedents'}
    ],
    'sourceReferences': [
        {'title': 'The Citizenship Act, 1955 (Act No. 57 of 1955)', 'url': 'https://indiacode.nic.in'},
        {'title': 'State Trading Corporation v. Commercial Tax Officer, AIR 1963 SC 1811', 'url': 'https://main.sci.gov.in'}
    ]
}

# Write Part 1 output
js_content = "/**\\n * Constitution Concepts — Part 1 (Chapters 1 to 5)\\n * 12 Comprehensive, verified topics\\n */\\n"
js_content += "(function() {\\n  'use strict';\\n  const PART1 = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\\n\\n"
js_content += "  if (typeof window !== 'undefined') { window.CONSTITUTION_CONCEPTS_PART1 = PART1; }\\n"
js_content += "  if (typeof module !== 'undefined' && module.exports) { module.exports = PART1; }\\n})();\\n"

with open(r"C:\\Users\\tauqe\\Documents\\Tanveer_Ashraf_Judicial\\assets\\learning\\data\\constitution\\constitution-concepts-part1.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully wrote constitution-concepts-part1.js with {len(data)} topics.")
'''

with open(r"C:\Users\tauqe\Documents\Tanveer_Ashraf_Judicial\scripts\data_builder_part1.py", "a", encoding="utf-8") as f:
    f.write(code)

print("append_ch3_ch5 ready to run.")
