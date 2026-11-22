# -*- coding: utf-8 -*-
import json
import os

out_path = r"C:\Users\tauqe\Documents\Tanveer_Ashraf_Judicial\assets\learning\data\constitution\constitution-concepts-part1.js"

# 12 Topics for Chapters 1 to 5
part1_concepts = {}

# Chapter 1 Topics
part1_concepts['top-const-01-01'] = {
    'topicId': 'top-const-01-01',
    'chapterId': 'ch-01',
    'title': 'Company Rule & Early Constitutional Enactments (1773–1853)',
    'subtitle': 'From Regulating Act 1773 to Charter Act 1853',
    'articleRef': 'Historical Charters',
    'learningObjective': 'Examine the gradual transition of the East India Company from a commercial trading corporation to an administrative sovereign, and analyse the foundational statutory precedents established by the British Parliament.',
    'introduction': 'The constitutional history of British India begins with the Regulating Act of 1773, which marked the first formal attempt by the British Parliament to supervise and regulate the administrative and commercial affairs of the East India Company. Over the subsequent eight decades, a succession of Charter Acts systematically curtailed company autonomy and created the nascent framework of centralized governance, judicial hierarchy, and civil service administration.',
    'detailedExplanation': """
<h3>1. The Regulating Act of 1773: The First Statutory Landmark</h3>
<p>The Regulating Act of 1773 was enacted following the financial collapse of the East India Company and the devastating Bengal Famine of 1770. It holds immense constitutional significance as the <strong>first written constitution-style intervention</strong> by the British Crown over Indian territories.</p>
<ul>
  <li><strong>Centralisation of Executive Authority:</strong> The Governor of Bengal was elevated to the status of <strong>Governor-General of Bengal</strong>. Lord Warren Hastings became the first Governor-General.</li>
  <li><strong>Executive Council:</strong> An Executive Council of four members was created to assist the Governor-General, with decisions made by majority vote and the Governor-General possessing a casting vote in case of a tie.</li>
  <li><strong>Subordination of Presidencies:</strong> The Governors of Bombay and Madras Presidencies were made subordinate to the Governor-General of Bengal in matters of war and diplomacy, laying the foundation of a unitary administrative structure.</li>
  <li><strong>Establishment of the Supreme Court at Calcutta (1774):</strong> Under Section 13, a Court of Record known as the <em>Supreme Court of Judicature at Fort William</em> was established in 1774, comprising a Chief Justice (Sir Elijah Impey) and three puisne judges, possessing jurisdiction over British subjects.</li>
</ul>

<h3>2. The Act of Settlement, 1781</h3>
<p>The jurisdiction of the Supreme Court at Calcutta clashed frequently with the Governor-General in Council (exemplified by the <em>Raja Nand Kumar</em> and <em>Cossijurah</em> cases). To remedy this friction, Parliament passed the Declaratory Act or Act of Settlement, 1781:</p>
<ul>
  <li>Exempted the Governor-General and Council from the jurisdiction of the Supreme Court for acts done in their official capacity.</li>
  <li>Excluded revenue matters and revenue collection from the jurisdiction of the Supreme Court.</li>
  <li>Mandated that the Court administer personal laws of the defendants (Mohammedan law for Muslims and Hindu law for Hindus).</li>
</ul>

<h3>3. Pitt's India Act of 1784: Dual System of Governance</h3>
<p>Authored by Prime Minister William Pitt, this Act bifurcated the commercial and political functions of the Company, establishing a dual system of control:</p>
<ul>
  <li><strong>Court of Directors:</strong> Permitted to manage purely commercial transactions.</li>
  <li><strong>Board of Control:</strong> A six-member political body of Crown ministers empowered to supervise, direct, and control all operations of the civil and military government and revenues.</li>
  <li>For the first time, Company territories in India were formally styled the <strong>"British Possessions in India"</strong>.</li>
</ul>

<h3>4. The Evolution Through Charter Acts (1793–1853)</h3>
<ul>
  <li><strong>Charter Act of 1793:</strong> Extended the Company's trade monopoly for 20 years. Salaried the Board of Control out of Indian revenues (a drain of wealth system that persisted until 1919).</li>
  <li><strong>Charter Act of 1813:</strong> Abolished the Company's commercial monopoly in India, opening Indian trade to all British merchants, except the monopoly over trade in <em>tea</em> and trade with <em>China</em>. Allocated an annual sum of ₹1 lakh for the promotion of Indian education and allowed Christian missionaries to enter India.</li>
  <li><strong>Charter Act of 1833 (Final Step in Centralisation):</strong>
    <ul>
      <li>Designated the Governor-General of Bengal as the <strong>Governor-General of India</strong>, vesting in him all civil and military authority. <strong>Lord William Bentinck</strong> became the first Governor-General of India.</li>
      <li>Deprived the Governors of Madras and Bombay of their independent legislative powers; the Governor-General in Council gained exclusive legislative power for the entirety of British India.</li>
      <li>Ended Company's commercial activities altogether; it became a purely administrative entity.</li>
      <li>Added a <strong>Law Member</strong> (Macaulay) to the Executive Council without voting rights, leading to the creation of the First Law Commission (1834) and drafting of the Indian Penal Code.</li>
    </ul>
  </li>
  <li><strong>Charter Act of 1853 (Birth of the Parliamentary Model):</strong>
    <ul>
      <li>Separated for the first time the <strong>legislative and executive functions</strong> of the Governor-General's Council.</li>
      <li>Added six new legislative members to the council, creating a 12-member Indian (Central) Legislative Council operating on the British parliamentary model.</li>
      <li>Introduced an <strong>open competition system</strong> for recruitment of civil servants (Macaulay Committee of 1854).</li>
    </ul>
  </li>
</ul>
""",
    'quickRevisionPoints': [
        'Regulating Act 1773 created the post of Governor-General of Bengal (Warren Hastings) and 4-member Executive Council.',
        'Supreme Court at Calcutta established in 1774 with Sir Elijah Impey as first Chief Justice.',
        'Act of Settlement 1781 exempted official acts of Governor-General in Council and revenue matters from Supreme Court jurisdiction.',
        'Pitt’s India Act 1784 established "Double Government" via Court of Directors (Commercial) and Board of Control (Political).',
        'Charter Act 1813 ended Company trade monopoly except tea and China trade, allocated ₹1 lakh for education.',
        'Charter Act 1833 created Governor-General of India (Lord William Bentinck) and Law Member (Lord Macaulay); ended all commercial functions.',
        'Charter Act 1853 separated legislative and executive functions and introduced open competition for civil services.'
    ],
    'provisions': [
        {'provision': 'Regulating Act, 1773, Sec. 7', 'title': 'Governor-General of Bengal', 'description': 'Elevated Presidency of Bengal over Madras and Bombay.'},
        {'provision': 'Regulating Act, 1773, Sec. 13', 'title': 'Supreme Court of Judicature', 'description': 'Letters Patent establishing Court of Record at Fort William.'},
        {'provision': 'Charter Act, 1833, Sec. 39', 'title': 'Governor-General of India', 'description': 'Complete centralisation of civil, military, and legislative power.'},
        {'provision': 'Charter Act, 1853, Sec. 22', 'title': 'Central Legislative Council', 'description': 'Creation of distinct 12-member legislative council.'}
    ],
    'definitions': [
        {'term': 'Double Government (Pitt’s India Act 1784)', 'definition': 'A constitutional arrangement where political/military governance was controlled by the Crown’s Board of Control, while commercial administration remained with the Company’s Court of Directors.'},
        {'term': 'Centralised Legislation', 'definition': 'Concentration of all lawmaking authority across British India in the Governor-General in Council under the Charter Act of 1833, stripping subordinate Presidencies of independent legislative power.'}
    ],
    'ingredients': [
        'Establishment of central supervisory authority over provincial presidencies.',
        'Separation between commercial mercantile enterprise and territorial sovereign statehood.',
        'Gradual introduction of specialized legal and legislative machinery (Law Commission and Legislative Council).'
    ],
    'exceptions': [
        'Governor-General possessed extraordinary override powers over his Council in emergencies under the Amending Act of 1786.',
        'Supreme Court at Calcutta had no jurisdiction over native transactions outside Calcutta unless parties consented in writing.'
    ],
    'examples': [
        {'scenario': 'Governor of Madras signs a peace treaty with a native ruler without Bengal’s consent in 1776.', 'application': 'Violates the Regulating Act of 1773, which subordinated subordinate presidencies in war and peace treaties to the Governor-General of Bengal.'},
        {'scenario': 'A British merchant attempts to import textiles into Bombay in 1815 without Company license.', 'application': 'Lawful under the Charter Act of 1813, which abolished the Company’s monopoly on Indian trade for private British merchants.'}
    ],
    'landmarkCases': [
        {'case': 'Trial of Raja Nand Kumar', 'citation': '(1775) 1 Cowp 161', 'year': '1775', 'bench': 'Sir Elijah Impey CJ', 'ratio': 'Nand Kumar was tried and executed under English forgery statute, highlighting the contentious jurisdiction of the newly created Supreme Court over native Indians.', 'impact': 'Directly precipitated the Act of Settlement, 1781 to restrict Court jurisdiction.'},
        {'case': 'Patna Case', 'citation': '(1777–1779) 1 Cl & Fin 24', 'year': '1779', 'bench': 'Supreme Court of Bengal', 'ratio': 'Exposed administrative conflicts between revenue officers of the Company (Provincial Council) and the judicial powers of the Supreme Court.', 'impact': 'Curtailed Court’s interference with Company revenue collection.'}
    ],
    'comparisonTables': [
        {
            'title': 'Comparison of Constitutional Milestones (1773 vs 1833 vs 1853)',
            'headers': ['Feature', 'Regulating Act 1773', 'Charter Act 1833', 'Charter Act 1853'],
            'rows': [
                ['Executive Head', 'Governor-General of Bengal', 'Governor-General of India', 'Governor-General of India'],
                ['Legislative Power', 'Council executive decrees', 'Exclusive central legislation', 'Distinct Legislative Council'],
                ['Commercial Status', 'Regulated monopoly', 'Commercial monopoly ended', 'Company as mere Crown trustee'],
                ['Law Commission', 'Not contemplated', 'First Law Commission (Macaulay)', 'Codification continued']
            ]
        }
    ],
    'diagramId': 'diag-historical-timeline',
    'diagramExplanation': 'The timeline depicts the progressive centralisation from 1773 to 1833, followed by the institutional differentiation between executive and legislative councils in 1853.',
    'misconceptions': [
        {'myth': 'The Charter Act of 1833 completely abolished British trade monopolies.', 'reality': 'The Charter Act of 1813 abolished Indian trade monopoly, but retained tea and China trade; 1833 abolished those remaining two monopolies completely.'},
        {'myth': 'The Supreme Court established in 1774 had all-India jurisdiction over all native Indians.', 'reality': 'Its territorial jurisdiction was confined primarily to Calcutta; outside Calcutta it only had jurisdiction over British subjects or their servants.'}
    ],
    'prelimTraps': [
        {'trap': 'Confusing the first Governor-General of Bengal with the first Governor-General of India.', 'reality': 'Warren Hastings was the first Governor-General of Bengal (1773); Lord William Bentinck was the first Governor-General of India (1833).', 'rule': 'Check whether the question specifies Bengal or India.'},
        {'trap': 'Assuming the Board of Control was established by the Regulating Act of 1773.', 'reality': 'The Board of Control was established by Pitt’s India Act of 1784, not the 1773 Act.', 'rule': '1773 = Executive Council; 1784 = Board of Control.'}
    ],
    'flashcards': [
        {'id': 'fc-01-01', 'front': 'Who was the first Governor-General of Bengal?', 'back': 'Lord Warren Hastings (Regulating Act, 1773).', 'category': 'Historical Chronology'},
        {'id': 'fc-01-02', 'front': 'Which Act created the "Board of Control" and "Double Government"?', 'back': 'Pitt’s India Act of 1784.', 'category': 'Statutory Acts'},
        {'id': 'fc-01-03', 'front': 'Which Charter Act ended the East India Company’s commercial activities completely?', 'back': 'Charter Act of 1833 (made it a purely administrative body).', 'category': 'Commercial Evolution'},
        {'id': 'fc-01-04', 'front': 'Which Act for the first time separated legislative from executive functions?', 'back': 'Charter Act of 1853 (created 12-member Indian Legislative Council).', 'category': 'Legislative Machinery'}
    ],
    'sourceReferences': [
        {'title': 'Government of India Legislative Department Archives', 'url': 'https://legislative.gov.in'},
        {'title': 'Constituent Assembly of India Debates (Historical Survey)', 'url': 'https://www.constitutionofindia.net'}
    ]
}

print("Part 1: Topic 1 complete.")
