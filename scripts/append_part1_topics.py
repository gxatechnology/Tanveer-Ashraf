# -*- coding: utf-8 -*-
"""
Appends topics for Chapters 2 to 5 to scripts/data_builder_part1.py
"""
import sys

ch2_ch5_code = '''
# ----------------------------------------------------
# CHAPTER 2: MAKING OF CONSTITUTION & SALIENT FEATURES
# ----------------------------------------------------

# TOPIC 4: Constituent Assembly
data['top-const-02-01'] = {
    'topicId': 'top-const-02-01',
    'chapterId': 'ch-02',
    'title': 'Constituent Assembly: Genesis, Committees & Enactment',
    'subtitle': 'Cabinet Mission Plan, Drafting Committee & Timeline of Adoption',
    'articleRef': 'Constituent Assembly Debates',
    'learningObjective': 'Trace the historical formation of the Constituent Assembly, analyze its major committees, the drafting trajectory, and constitutional timeline.',
    'introduction': 'The demand for a Constituent Assembly was first mooted by M.N. Roy in 1934 and officially adopted by the Indian National Congress in 1935. Formed under the Cabinet Mission Plan of 1946, the Assembly served the dual role of a constitution-making body and the first provisional parliament of independent India.',
    'detailedExplanation': """
<h3>1. Genesis and Composition of the Assembly</h3>
<p>The Constituent Assembly was constituted in November 1946 under the scheme formulated by the <strong>Cabinet Mission Plan</strong> (comprising Lord Pethick-Lawrence, Sir Stafford Cripps, and A.V. Alexander):</p>
<ul>
  <li><strong>Total Strength:</strong> Originally fixed at 389 (296 from British India and 93 from Princely States). Following partition under the Mountbatten Plan, the strength was reduced to 299.</li>
  <li><strong>Indirect Election:</strong> Members from British Indian provinces were elected indirectly by the provincial legislative assemblies by proportional representation with a single transferable vote; princely representatives were nominated by their rulers.</li>
  <li><strong>Key Personalities:</strong> Dr. Sachchidananda Sinha served as temporary President (French practice) on December 9, 1946. On December 11, 1946, <strong>Dr. Rajendra Prasad</strong> was elected permanent President and H.C. Mukherjee as Vice-President. Sir <strong>B.N. Rau</strong> was appointed Constitutional Advisor.</li>
</ul>

<h3>2. The Objective Resolution & Drafting Trajectory</h3>
<ul>
  <li><strong>Objective Resolution:</strong> Moved by Jawaharlal Nehru on December 13, 1946; unanimously adopted on January 22, 1947. It provided the constitutional philosophy and became the basis of the Preamble.</li>
  <li><strong>Drafting Committee:</strong> Appointed on August 29, 1947, consisting of 7 members headed by <strong>Dr. B.R. Ambedkar</strong> (Chairman, Father of the Constitution): N. Gopalaswami Ayyangar, Alladi Krishnaswami Ayyar, Dr. K.M. Munshi, Syed Mohammad Saadulla, N. Madhava Rau (replaced B.L. Mitter), and T.T. Krishnamachari (replaced D.P. Khaitan).</li>
  <li><strong>Deliberations:</strong> The Assembly took exactly <strong>2 years, 11 months, and 18 days</strong>, holding 11 sessions, considering over 7,600 amendments, and spending ₹64 lakhs.</li>
  <li><strong>Adoption & Commencement:</strong> Adopted on <strong>November 26, 1949</strong> (Constitution Day / Samvidhan Divas), containing a Preamble, 395 Articles, and 8 Schedules. Articles 5, 6, 7, 8, 9, 60, 324, 366, 367, 379, 380, 388, 391, 392, and 393 came into force immediately on Nov 26, 1949. The remaining major provisions commenced on <strong>January 26, 1950</strong> (celebrating the 1930 Purna Swaraj Day).</li>
</ul>
""",
    'quickRevisionPoints': [
        'Idea first mooted by M.N. Roy (1934); Constituent Assembly formed under Cabinet Mission Plan (1946).',
        'First meeting on Dec 9, 1946 (Dr. Sachchidananda Sinha temporary chairman); Dr. Rajendra Prasad elected permanent President on Dec 11.',
        'Constitutional Advisor was Sir B.N. Rau.',
        'Objective Resolution moved by Nehru on Dec 13, 1946, adopted Jan 22, 1947 (became Preamble).',
        'Drafting Committee (7 members) appointed on Aug 29, 1947, chaired by Dr. B.R. Ambedkar.',
        'Time taken: 2 years, 11 months, 18 days across 11 sessions.',
        'Adopted on Nov 26, 1949; commenced on Jan 26, 1950 (395 Articles, 8 Schedules).'
    ],
    'provisions': [
        {'provision': 'Article 393', 'title': 'Short Title', 'description': 'Declares the formal title: "Constitution of India".'},
        {'provision': 'Article 394', 'title': 'Commencement', 'description': 'Specified which articles came into force on 26 Nov 1949 and remaining on 26 Jan 1950.'},
        {'provision': 'Article 395', 'title': 'Repeals', 'description': 'Repealed the Indian Independence Act, 1947 and the GoI Act, 1935.'}
    ],
    'definitions': [
        {'term': 'Constituent Power', 'definition': 'The supreme, original, sovereign power to frame, amend, or rewrite a foundational constitution, distinguished from ordinary legislative power.'},
        {'term': 'Objective Resolution', 'definition': 'Solemn resolution moved by Jawaharlal Nehru setting out the ideological framework and social vision of independent India.'}
    ],
    'ingredients': [
        'Democratically representative, indirect electoral composition.',
        'Deliberative consensus across diverse ideological, linguistic, and regional groups.',
        'Distinct functional division between constitution-framing committees and ordinary governance.'
    ],
    'exceptions': [
        'Princely State representatives were nominated by rulers rather than elected by the people.',
        'The Assembly was not elected on adult universal franchise due to the time constraint of 1946.'
    ],
    'examples': [
        {'scenario': 'A petitioner in December 1949 challenges citizenship under the new Constitution before January 26, 1950.', 'application': 'Valid proceeding, because Articles 5 to 9 on Citizenship came into force immediately on November 26, 1949 under Article 394.'}
    ],
    'landmarkCases': [
        {'case': 'Golaknath v. State of Punjab', 'citation': 'AIR 1967 SC 1643', 'year': '1967', 'bench': '11-Judge Bench (Subba Rao CJ)', 'ratio': 'Subba Rao CJ observed that the Constituent Assembly possessed original constituent power, which Parliament acting under Article 368 lacks.', 'impact': 'Sparked the constitutional battle culminating in the 24th Amendment and Kesavananda Bharati.'}
    ],
    'comparisonTables': [
        {
            'title': 'Timeline of Constitutional Enactment',
            'headers': ['Event', 'Date', 'Significance'],
            'rows': [
                ['First Meeting', '9 December 1946', 'Dr. Sachchidananda Sinha interim President'],
                ['Objective Resolution', '13 December 1946', 'Nehru moved the constitutional blueprint'],
                ['Drafting Committee Formed', '29 August 1947', 'Dr. B.R. Ambedkar appointed Chairman'],
                ['Constitution Adopted', '26 November 1949', 'Signed by 284 members; 395 Articles adopted'],
                ['Full Commencement', '26 January 1950', 'Commencement of Republic of India']
            ]
        }
    ],
    'diagramId': 'diag-assembly-structure',
    'diagramExplanation': 'The flowchart illustrates the dual role of the Assembly: drafting the constitutional charter under Dr. Rajendra Prasad and acting as the Provisional Parliament under G.V. Mavalankar.',
    'misconceptions': [
        {'myth': 'The entire Constitution came into force on January 26, 1950.', 'reality': '16 Articles (including citizenship, elections Art. 324, provisional parliament) came into force on November 26, 1949.'},
        {'myth': 'Sir B.N. Rau was a member of the Drafting Committee.', 'reality': 'Sir B.N. Rau was the Constitutional Advisor to the Assembly; he prepared the initial draft but was not a member of Ambedkar’s Drafting Committee.'}
    ],
    'prelimTraps': [
        {'trap': 'Who was the temporary President of the Constituent Assembly?', 'reality': 'Dr. Sachchidananda Sinha (Dec 9, 1946). Dr. Rajendra Prasad was elected permanent President on Dec 11.', 'rule': 'Dec 9 = Sinha; Dec 11 = Prasad.'},
        {'trap': 'Speaker of the Constituent Assembly when it met as the Provisional Parliament.', 'reality': 'G.V. Mavalankar. When it met as Constitution-making body, Dr. Rajendra Prasad presided; when it met as Parliament, Mavalankar presided.', 'rule': 'Drafting = Rajendra Prasad; Lawmaking = Mavalankar.'}
    ],
    'flashcards': [
        {'id': 'fc-02-01', 'front': 'Who was the Constitutional Advisor to the Constituent Assembly?', 'back': 'Sir Benegal Narsing Rau (B.N. Rau).', 'category': 'Assembly Offices'},
        {'id': 'fc-02-02', 'front': 'On which date was the Objective Resolution moved in the Constituent Assembly?', 'back': 'December 13, 1946 by Jawaharlal Nehru (unanimously adopted on January 22, 1947).', 'category': 'Key Dates'},
        {'id': 'fc-02-03', 'front': 'How many members signed the final handwritten Constitution on November 26, 1949?', 'back': '284 members out of 299.', 'category': 'Adoption Milestones'},
        {'id': 'fc-02-04', 'front': 'Who was the calligrapher of the original Hindi and English Constitution?', 'back': 'Prem Behari Narain Raizada (English italic calligraphy); decorated by Nandalal Bose (Shantiniketan).', 'category': 'Heritage Details'}
    ],
    'sourceReferences': [
        {'title': 'Constituent Assembly Debates (Official Records)', 'url': 'https://www.constitutionofindia.net'},
        {'title': 'Lok Sabha Secretariat: Making of the Constitution', 'url': 'https://loksabha.nic.in'}
    ]
}

# TOPIC 5: Global Sources
data['top-const-02-02'] = {
    'topicId': 'top-const-02-02',
    'chapterId': 'ch-02',
    'title': 'Global Sources of the Indian Constitution',
    'subtitle': 'Borrowed Features from UK, USA, Ireland, Canada, Australia, etc.',
    'articleRef': 'Comparative Jurisprudence',
    'learningObjective': 'Identify and categorize the major foreign constitutional frameworks borrowed and adapted to suit Indian socio-political realities.',
    'detailedExplanation': """
<h3>1. Borrowing with Modification: A Unique Synthesis</h3>
<p>Dr. B.R. Ambedkar famously remarked in the Constituent Assembly: <em>"Nobody holds any patent rights in the fundamental ideas of a Constitution. What is new in this Constitution is only the variations made to remove faults and accommodate it to the needs of the country."</em></p>

<h3>2. The Primary Source: Government of India Act, 1935</h3>
<ul>
  <li>Federal scheme and provincial autonomy.</li>
  <li>Office of the Governor.</li>
  <li>Judicial system (Federal Court model).</li>
  <li>Public Service Commissions (UPSC and State PSCs).</li>
  <li>Emergency provisions and administrative details.</li>
</ul>

<h3>3. Major International Contributions</h3>
<table class="table-content">
  <thead>
    <tr><th>Country</th><th>Borrowed Constitutional Features</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>United Kingdom (UK)</strong></td>
      <td>Parliamentary government, Nominal head of State (President like British Monarch), Rule of Law (Dicey’s concept), Legislative procedure, Single Citizenship, Cabinet system, Prerogative Writs, Parliamentary privileges, Bicameralism.</td>
    </tr>
    <tr>
      <td><strong>United States (USA)</strong></td>
      <td>Written Constitution, Preamble, Fundamental Rights (Bill of Rights), Judicial Review, Independence of Judiciary, Impeachment of President, Removal of Supreme Court and High Court judges, Post of Vice-President.</td>
    </tr>
    <tr>
      <td><strong>Ireland</strong></td>
      <td>Directive Principles of State Policy (Part IV), Method of election of the President, Nomination of 12 members to Rajya Sabha by the President for literature, science, art, and social service.</td>
    </tr>
    <tr>
      <td><strong>Canada</strong></td>
      <td>Federation with a strong Centre (quasi-federalism), Vesting of residuary powers in the Centre (Art. 248), Appointment of State Governors by the Centre, Advisory jurisdiction of the Supreme Court (Art. 143).</td>
    </tr>
    <tr>
      <td><strong>Australia</strong></td>
      <td>Concurrent List (Seventh Schedule), Freedom of trade, commerce and intercourse (Part XIII), Joint sitting of both Houses of Parliament (Art. 108).</td>
    </tr>
    <tr>
      <td><strong>Weimar Republic (Germany)</strong></td>
      <td>Suspension of Fundamental Rights during National Emergency (Art. 359).</td>
    </tr>
    <tr>
      <td><strong>USSR (Soviet Union)</strong></td>
      <td>Fundamental Duties (Art. 51A via 42nd Amendment 1976), Ideal of Justice (Social, Economic, and Political) in the Preamble.</td>
    </tr>
    <tr>
      <td><strong>France</strong></td>
      <td>Republic and the ideals of Liberty, Equality, and Fraternity in the Preamble.</td>
    </tr>
    <tr>
      <td><strong>South Africa</strong></td>
      <td>Procedure for Amendment of the Constitution (Art. 368), Election of members of Rajya Sabha by State Legislative Assemblies.</td>
    </tr>
    <tr>
      <td><strong>Japan</strong></td>
      <td>Procedure established by Law (Art. 21).</td>
    </tr>
  </tbody>
</table>
""",
    'quickRevisionPoints': [
        'GoI Act 1935: Federal scheme, Governor, Judiciary, Emergency machinery, PSCs.',
        'UK: Parliamentary government, Rule of Law, Single citizenship, Writs, Bicameralism.',
        'USA: Fundamental Rights, Judicial Review, Impeachment of President, Preamble.',
        'Ireland: DPSP, Presidential election method, 12 nominated Rajya Sabha members.',
        'Canada: Strong Centre, Residuary powers in Centre, Supreme Court Advisory jurisdiction.',
        'Australia: Concurrent List, Joint Sitting (Art. 108), Inter-state trade & commerce.',
        'Germany (Weimar): Suspension of Fundamental Rights during emergency.',
        'South Africa: Constitutional amendment procedure (Art. 368), Rajya Sabha election method.',
        'Japan: "Procedure established by law" (Art. 21).'
    ],
    'provisions': [
        {'provision': 'Seventh Schedule, List III', 'title': 'Concurrent List', 'description': 'Borrowed from the Commonwealth of Australia Constitution Act 1900.'},
        {'provision': 'Article 108', 'title': 'Joint Sitting', 'description': 'Borrowed from Section 57 of the Australian Constitution.'},
        {'provision': 'Article 143', 'title': 'Advisory Jurisdiction', 'description': 'Borrowed from Section 55 of the Canadian Supreme Court Act.'}
    ],
    'definitions': [
        {'term': 'Quasi-Federal', 'definition': 'Professor K.C. Wheare’s classification of the Indian Constitution as a unitary state with subsidiary federal features rather than a federal state with subsidiary unitary features.'},
        {'term': 'Rule of Law', 'definition': 'A.V. Dicey’s doctrine borrowed from English constitutional law asserting absence of arbitrary power, equality before law, and pre-dominance of legal spirit.'}
    ],
    'ingredients': [
        'Eclectic synthesis of global constitutional best practices.',
        'Indigenization to avoid pitfalls observed in foreign legal systems.',
        'Institutional balance between British parliamentary supremacy and American judicial review.'
    ],
    'exceptions': [
        'Unlike the US federal model, Indian citizenship is single and unified; there is no state citizenship.',
        'Unlike Canada where provinces have no role in constitutional amendments, half of Indian States must ratify federal amendments under Art. 368.'
    ],
    'examples': [
        {'scenario': 'Parliament enacts a statute overriding a state law on a concurrent topic.', 'application': 'Operates under the Australian-inspired Concurrent List mechanism read with Article 254.'}
    ],
    'landmarkCases': [
        {'case': 'State of West Bengal v. Union of India', 'citation': 'AIR 1963 SC 1241', 'year': '1963', 'bench': '6-Judge Bench (Sinha CJ)', 'ratio': 'Analyzed Canadian and US federal precedents. Held that Indian Constitution is not truly federal in the traditional American sense; Indian states have no sovereignty independent of the Union.', 'impact': 'Affirmed the unitary tilt of Indian federalism.'}
    ],
    'comparisonTables': [
        {
            'title': 'Indian Model vs UK & US Models',
            'headers': ['Dimension', 'United Kingdom', 'United States', 'India (Synthesis)'],
            'rows': [
                ['Constitution', 'Unwritten / Flexible', 'Written / Very Rigid', 'Written / Blend of Rigid & Flexible'],
                ['Executive-Legislative', 'Fused (Parliamentary)', 'Separated (Presidential)', 'Fused (Parliamentary System)'],
                ['Judicial Review', 'Parliament is sovereign', 'Supreme Court supreme', 'Judicial Review tempered by Procedure'],
                ['Citizenship', 'Single', 'Dual (State + Federal)', 'Single (All-India)']
            ]
        }
    ],
    'diagramId': 'diag-sources-features',
    'diagramExplanation': 'The concept map traces the international parentage of Indian constitutional institutions from 10 major global systems.',
    'misconceptions': [
        {'myth': 'Fundamental Duties were part of the original Constitution borrowed from USSR in 1950.', 'reality': 'Fundamental Duties were NOT in the original Constitution; they were added in 1976 via the 42nd Amendment on recommendation of the Swaran Singh Committee.'},
        {'myth': 'Election of the President and Election of Rajya Sabha members were borrowed from the same country.', 'reality': 'Method of Presidential election was borrowed from Ireland; Method of Rajya Sabha election was borrowed from South Africa.'}
    ],
    'prelimTraps': [
        {'trap': 'Source of "Nomination of Rajya Sabha members" vs "Election of Rajya Sabha members".', 'reality': 'Nomination of 12 members by President = Ireland; Election of elected members by State MLAs = South Africa.', 'rule': 'Nomination = Ireland; Election = South Africa.'},
        {'trap': 'Source of "Procedure established by law" vs "Due process of law".', 'reality': '"Procedure established by law" is Japanese (Art. 31 of Japanese Constitution); "Due process of law" is American (5th and 14th Amendments).', 'rule': 'Procedure established = Japan; Due Process = USA.'}
    ],
    'flashcards': [
        {'id': 'fc-02-05', 'front': 'From which country was the Concurrent List borrowed?', 'back': 'Australia.', 'category': 'Foreign Sources'},
        {'id': 'fc-02-06', 'front': 'From which country were Directive Principles of State Policy (DPSP) borrowed?', 'back': 'Ireland (which in turn borrowed from Spanish Constitution).', 'category': 'Foreign Sources'},
        {'id': 'fc-02-07', 'front': 'Which country inspired the emergency suspension of Fundamental Rights?', 'back': 'Weimar Republic of Germany.', 'category': 'Foreign Sources'},
        {'id': 'fc-02-08', 'front': 'From which country was the procedure for amending the Constitution borrowed?', 'back': 'South Africa (Article 368).', 'category': 'Foreign Sources'}
    ],
    'sourceReferences': [
        {'title': 'Granville Austin, The Indian Constitution: Cornerstone of a Nation', 'url': 'https://global.oup.com'},
        {'title': 'Official Portal of the Ministry of Law and Justice', 'url': 'https://lawmin.gov.in'}
    ]
}

# TOPIC 6: Salient Features
data['top-const-02-03'] = {
    'topicId': 'top-const-02-03',
    'chapterId': 'ch-02',
    'title': 'Salient Structural Features of the Indian Constitution',
    'subtitle': 'Quasi-Federal Nature, Blend of Rigidity & Flexibility, Integrated Judiciary',
    'articleRef': 'Constitutional Hallmarks',
    'learningObjective': 'Master the unique institutional architecture that distinguishes the Indian Constitution from other constitutional democracies.',
    'detailedExplanation': """
<h3>1. The Longest Written Constitution</h3>
<p>Originally consisting of a Preamble, 395 Articles divided into 22 Parts and 8 Schedules (currently over 470 Articles in 25 Parts and 12 Schedules). Its extraordinary length results from:
<ul>
  <li>Geographical diversity and vastness of India.</li>
  <li>Historical influence of the massive Government of India Act 1935.</li>
  <li>Single unified Constitution for both the Union and the States (except temporary J&K provision prior to 2019).</li>
  <li>Inclusion of administrative details alongside fundamental constitutional principles to protect nascent democratic institutions.</li>
</ul>

<h3>2. Blend of Rigidity and Flexibility</h3>
<p>Unlike the American Constitution (rigid, requiring 3/4th state ratification) and the British Constitution (flexible, alterable by simple majority):</p>
<ul>
  <li>Some provisions can be amended by a <strong>simple majority</strong> of Parliament (e.g., formation of new states, abolition of legislative councils).</li>
  <li>Some require a <strong>special majority</strong> under Article 368 (majority of total membership + 2/3rd members present and voting).</li>
  <li>Federal provisions require a special majority plus ratification by at least half of the State Legislatures.</li>
</ul>

<h3>3. Federal System with Unitary Bias ("Quasi-Federal")</h3>
<p>Contains all standard federal features: two governments, division of powers, written constitution, supremacy of constitution, rigidity, independent judiciary, and bicameralism. However, it incorporates powerful unitary features:
<ul>
  <li>Strong Centre, single Constitution, single citizenship.</li>
  <li>Integrated judiciary, appointment of State Governors by President.</li>
  <li>All-India Services (IAS, IPS, IFoS under Article 312).</li>
  <li>Emergency provisions (Articles 352, 356, 360) where the federal structure transforms into a unitary system without formal amendment.</li>
  <li>Described as <em>"Quasi-federal"</em> by K.C. Wheare, <em>"Bargaining federalism"</em> by Morris-Jones, and <em>"Co-operative federalism"</em> by Granville Austin.</li>
</ul>

<h3>4. Parliamentary Form with an Integrated Judiciary</h3>
<ul>
  <li><strong>Synthesis of Sovereignty and Review:</strong> Synthesizes British principle of Parliamentary Sovereignty and American principle of Judicial Supremacy. The Supreme Court can declare parliamentary laws unconstitutional via Judicial Review (Art. 13), while Parliament can amend major portions of the Constitution (Art. 368) within the limits of the Basic Structure.</li>
  <li><strong>Single Integrated Judicial System:</strong> Unlike the US where federal and state courts enforce separate federal and state laws, India has a single hierarchy of courts (Supreme Court -> High Courts -> Subordinate Courts) enforcing both Union and State enactments.</li>
</ul>
""",
    'quickRevisionPoints': [
        'Longest written constitution in the world (originally 395 articles, 8 schedules; now 470+ articles, 12 schedules).',
        'Blend of Rigidity and Flexibility: three amendment modes under and outside Article 368.',
        'Quasi-Federal: Federal in structure, unitary in spirit (K.C. Wheare).',
        'Parliamentary system based on executive responsibility to the elected lower house.',
        'Single Integrated Judiciary enforcing both Union and State laws.',
        'Single Citizenship for all Indians irrespective of the state of domicile.'
    ],
    'provisions': [
        {'provision': 'Article 1', 'title': 'Name and Territory', 'description': 'Declares India as a Union of States.'},
        {'provision': 'Article 312', 'title': 'All-India Services', 'description': 'Empowers Rajya Sabha to create common Union/State bureaucratic services.'},
        {'provision': 'Article 368', 'title': 'Power to Amend', 'description': 'Prescribes the special amending procedure.'}
    ],
    'definitions': [
        {'term': 'Co-operative Federalism', 'definition': 'Granville Austin’s characterization of Indian federalism emphasizing collaboration between Centre and States to achieve common social objectives.'},
        {'term': 'Integrated Judiciary', 'definition': 'A unified judicial hierarchy where the Supreme Court heads state High Courts and subordinate district judiciaries, enforcing a common body of national laws.'}
    ],
    'ingredients': [
        'Constitutional supremacy with single national supreme law.',
        'Executive accountability to the legislature via collective responsibility.',
        'Independent judicial branch endowed with powers of constitutional review.'
    ],
    'exceptions': [
        'National Emergency under Article 352 completely suspends the normal federal division of executive and legislative powers.',
        'Parliament can legislate on State List subjects under Article 249 if Rajya Sabha declares it necessary in the national interest.'
    ],
    'examples': [
        {'scenario': 'A district court in Lucknow enforces the Central Code of Criminal Procedure alongside a Uttar Pradesh municipal statute.', 'application': 'Permitted due to India’s integrated judicial system, which enforces both central and state laws uniformly.'}
    ],
    'landmarkCases': [
        {'case': 'S.R. Bommai v. Union of India', 'citation': '(1994) 3 SCC 1', 'year': '1994', 'bench': '9-Judge Bench', 'ratio': 'Held that Federalism and Secularism are essential parts of the Basic Structure of the Constitution. States are not mere appendages or agents of the Centre.', 'impact': 'Curbed the arbitrary invocation of President’s Rule under Article 356.'}
    ],
    'comparisonTables': [
        {
            'title': 'Federal vs Unitary Features of Indian Constitution',
            'headers': ['Federal Features', 'Unitary / Centralizing Features'],
            'rows': [
                ['Dual polity (Union & States)', 'Strong Centre (Residuary powers in Parliament)'],
                ['Division of powers (Three Lists)', 'Single Constitution for Union and States'],
                ['Written and supreme Constitution', 'Single Unified Citizenship'],
                ['Independent Judiciary', 'Integrated Judicial Hierarchy'],
                ['Bicameralism (Rajya Sabha & Lok Sabha)', 'Emergency Provisions converting polity to unitary']
            ]
        }
    ],
    'diagramId': 'diag-quasi-federal',
    'diagramExplanation': 'The diagram balances the core federal pillars on the left against the powerful unitary safety valves on the right.',
    'misconceptions': [
        {'myth': 'The term "Federation" is explicitly used in Article 1 of the Constitution.', 'reality': 'The word "Federation" is nowhere used in the text of the Constitution. Article 1 describes India as a "Union of States".'},
        {'myth': 'Indian States have their own separate state citizenship like in the United States.', 'reality': 'India provides only single unified citizenship under Article 9; there is no separate state citizenship.'}
    ],
    'prelimTraps': [
        {'trap': 'Who described the Indian Constitution as "Quasi-federal"?', 'reality': 'Professor K.C. Wheare. Granville Austin called it "Co-operative Federalism"; Morris-Jones called it "Bargaining Federalism".', 'rule': 'Quasi-federal = K.C. Wheare; Co-operative = Granville Austin.'},
        {'trap': 'Is federalism part of the Basic Structure of the Indian Constitution?', 'reality': 'YES, explicitly held by a 9-judge bench in S.R. Bommai v. Union of India (1994).', 'rule': 'Federalism = Basic Structure (S.R. Bommai).'}
    ],
    'flashcards': [
        {'id': 'fc-02-09', 'front': 'Which article of the Constitution describes India as a "Union of States"?', 'back': 'Article 1(1).', 'category': 'Constitutional Text'},
        {'id': 'fc-02-10', 'front': 'Who characterized the Indian federal structure as "Co-operative Federalism"?', 'back': 'Granville Austin.', 'category': 'Jurisprudential Scholars'},
        {'id': 'fc-02-11', 'front': 'How many Articles and Schedules were in the original 1949 Constitution?', 'back': '395 Articles, 22 Parts, and 8 Schedules.', 'category': 'Structural Metrics'},
        {'id': 'fc-02-12', 'front': 'In which landmark case was Federalism declared part of the Basic Structure?', 'back': 'S.R. Bommai v. Union of India (1994).', 'category': 'Landmark Rulings'}
    ],
    'sourceReferences': [
        {'title': 'S.R. Bommai v. Union of India (1994) 3 SCC 1', 'url': 'https://main.sci.gov.in'},
        {'title': 'K.C. Wheare, Federal Government (Oxford University Press)', 'url': 'https://oup.com'}
    ]
}
'''

with open(r"C:\Users\tauqe\Documents\Tanveer_Ashraf_Judicial\scripts\data_builder_part1.py", "a", encoding="utf-8") as f:
    f.write(ch2_ch5_code)

print("Chapter 2 appended successfully.")
