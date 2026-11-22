"""
Builder for Constitution Concepts Part 3 (Chapters 9 to 15, 22 topics).
Outputs to assets/learning/data/constitution/constitution-concepts-part3.js
"""
import json
import os

PART3 = {}

# ==============================================================================
# CHAPTER 9: THE UNION EXECUTIVE (3 topics)
# ==============================================================================
PART3['top-const-09-01'] = {
    'topicId': 'top-const-09-01',
    'chapterId': 'ch-09',
    'title': 'The President & Vice-President: Office, Election & Impeachment',
    'subtitle': 'Articles 52–71: Electoral College, Proportional Representation & Article 61 Procedure',
    'articleRef': 'Articles 52 to 71',
    'overview': 'The President of India is the constitutional head of the Republic and supreme commander of the defence forces. This topic covers the method of election via proportional representation by single transferable vote, value of votes of MLAs and MPs, qualifications, term of office, and the quasi-judicial impeachment procedure under Article 61.',
    'detailedStudy': {
        'learningObjectives': [
            'Analyze the composition of the Presidential Electoral College under Article 54 and the exclusion of nominated members.',
            'Calculate the value of votes of MLAs and MPs under Article 55 ensuring parity between the States and the Union.',
            'Examine the quasi-judicial procedure for impeachment of the President under Article 61 for "violation of the Constitution".',
            'Understand the constitutional functions of the Vice-President as ex-officio Chairman of the Council of States (Article 64).'
        ],
        'coreDoctrine': 'Under Article 52, there shall be a President of India. The executive power of the Union is vested in the President by Article 53(1) and is exercisable in accordance with the Constitution. The President is elected by an Electoral College consisting of elected members of both Houses of Parliament and elected members of Legislative Assemblies of the States (including Delhi and Puducherry pursuant to the 70th Amendment Act, 1992). Nominated members of Parliament and State Assemblies and all members of State Legislative Councils are strictly excluded. The election follows proportional representation by single transferable vote (Article 55). Article 61 provides a stringent quasi-judicial mechanism for removal of the President solely on the ground of "violation of the Constitution", requiring a 14-day written notice signed by at least one-fourth of the total membership of the initiating House, and a resolution passed by a majority of not less than two-thirds of the total membership of each House.',
        'statutoryProvisions': [
            {'article': 'Article 52', 'heading': 'The President of India', 'text': 'There shall be a President of India.'},
            {'article': 'Article 53', 'heading': 'Executive power of the Union', 'text': 'The executive power of the Union shall be vested in the President and shall be exercised by him either directly or through officers subordinate to him in accordance with this Constitution.'},
            {'article': 'Article 54', 'heading': 'Election of President', 'text': 'The President shall be elected by the members of an electoral college consisting of (a) the elected members of both Houses of Parliament; and (b) the elected members of the Legislative Assemblies of the States.'},
            {'article': 'Article 55', 'heading': 'Manner of election of President', 'text': 'As far as practicable, there shall be uniformity in the scale of representation of the different States at the election of the President, determined by population.'},
            {'article': 'Article 58', 'heading': 'Qualifications for election as President', 'text': 'Citizen of India, completed 35 years of age, qualified for election as a member of the House of the People, and does not hold any office of profit.'},
            {'article': 'Article 61', 'heading': 'Procedure for impeachment of the President', 'text': 'Resolution initiated after 14 days notice in writing signed by not less than one-fourth of total members; passed by not less than two-thirds of total membership of the House; investigated by the other House; and passed by not less than two-thirds of total membership of investigating House.'},
            {'article': 'Article 63–64', 'heading': 'The Vice-President of India', 'text': 'There shall be a Vice-President of India who shall be ex-officio Chairman of the Council of States and shall not hold any other office of profit.'},
            {'article': 'Article 71', 'heading': 'Matters relating to election of President/VP', 'text': 'All doubts and disputes arising out of or in connection with the election of a President or Vice-President shall be inquired into and decided by the Supreme Court whose decision shall be final.'}
        ],
        'legalIngredients': [
            'Electoral College: Elected MPs + Elected MLAs (States + Delhi + Puducherry). Excludes nominated members and MLCs.',
            'Formula for MLA vote: (Total population of State) / (Total elected members of Assembly × 1000).',
            'Formula for MP vote: (Total value of votes of all MLAs of all States) / (Total number of elected MPs in Lok Sabha and Rajya Sabha).',
            'Impeachment threshold: Special majority of 2/3rd of the TOTAL membership of the House (the most stringent majority in the Constitution).',
            'Vice-President Electoral College: All members of Parliament (both elected and nominated); State Assemblies play no role.'
        ],
        'exceptions': [
            'Presidential election cannot be challenged on the ground of the existence of any vacancy in the electoral college (Article 71(4)).',
            'Nominated members of Parliament can participate in Presidential impeachment (Article 61), even though they cannot vote in Presidential election (Article 54).'
        ],
        'practicalScenarios': [
            {'scenario': 'The Legislative Assembly of State X is dissolved prior to a Presidential election. An elector challenges the election under Article 71.', 'application': 'Under Article 71(4) and In re Presidential Election 1974, dissolution of a State Assembly does not vitiate or postpone the Presidential election; the electoral college remains legally competent.'}
        ],
        'landmarkCases': [
            {'case': 'In re Presidential Election, 1974', 'citation': '(1974) 2 SCC 33', 'year': '1974', 'bench': '7-Judge Bench (Ray CJ)', 'ratio': 'Held that the Presidential election must be completed before the expiration of the term of the outgoing President notwithstanding the dissolution of a State Legislative Assembly.', 'impact': 'Affirmed that vacancies in the electoral college do not stall Presidential polls.'},
            {'case': 'N.B. Khare v. Election Commission of India', 'citation': 'AIR 1957 SC 694', 'year': '1957', 'bench': '5-Judge Bench', 'ratio': 'Held that disputes relating to Presidential elections can be raised before the Supreme Court only after the completion of the election, not mid-process.', 'impact': 'Established bar on pre-election judicial intervention.'}
        ],
        'comparisonTables': [
            {
                'title': 'President vs Vice-President: Electoral & Removal Comparison',
                'headers': ['Parameter', 'President of India', 'Vice-President of India'],
                'rows': [
                    ['Electoral College', 'Elected MPs + Elected MLAs (States, Delhi, Puducherry)', 'All MPs (Elected + Nominated); No MLAs'],
                    ['Election Method', 'Proportional representation by single transferable vote', 'Proportional representation by single transferable vote'],
                    ['Removal Ground', '"Violation of the Constitution" only', 'Any ground; no specific constitutional phrase'],
                    ['Removal Majority', '2/3rd of TOTAL membership of BOTH Houses', 'Effective majority in Rajya Sabha + Simple majority in Lok Sabha']
                ]
            }
        ],
        'diagramId': 'diag-presidential-electoral-college',
        'diagramExplanation': 'Illustrates the composite structure of the Electoral College, showing the balance between Central and State votes and the exclusion of nominated members.',
        'misconceptions': [
            {'myth': 'Nominated members of Rajya Sabha vote in Presidential elections.', 'reality': 'Nominated members are excluded under Article 54, though they vote in the Vice-Presidential election.'}
        ],
        'prelimTraps': [
            {'trap': 'What majority is required for impeachment of the President under Article 61?', 'reality': 'Majority of not less than two-thirds of the TOTAL membership of the House (not members present and voting).', 'rule': 'Art. 61 = 2/3rd of Total Membership.'},
            {'trap': 'Can a dispute regarding the Presidential election be challenged in a High Court under Article 226?', 'reality': 'No, Article 71 confers exclusive jurisdiction on the Supreme Court.', 'rule': 'Art. 71 = Exclusive SC jurisdiction.'}
        ],
        'quickRevision': {
            'keyArticles': [
                {'article': 'Art. 52', 'crux': 'President of India office established.'},
                {'article': 'Art. 54', 'crux': 'Electoral College: Elected MPs + Elected MLAs.'},
                {'article': 'Art. 61', 'crux': 'Impeachment: 14 days notice, 2/3rd total membership majority.'},
                {'article': 'Art. 71', 'crux': 'Supreme Court decides election disputes exclusively.'}
            ],
            'bulletSummary': [
                'President must be at least 35 years old and qualified for Lok Sabha election.',
                'Impeachment charges can be initiated by either House of Parliament.',
                'The other House investigates the charges; the President has the right to appear and be represented.',
                'Vice-President is ex-officio Chairman of Rajya Sabha but is not a member of either House.'
            ],
            'mnemonics': [
                {'phrase': 'ELE-IMP-71', 'meaning': 'Elected vote (Art. 54), Impeached by 2/3rd total (Art. 61), Supreme Court resolves disputes (Art. 71).'}
            ],
            'oneLinerRules': [
                'Nominated members cannot elect the President but can participate in the President’s impeachment.',
                'Only elected members of State Legislative Assemblies vote in Presidential elections; Legislative Councils never participate.'
            ]
        },
        'flashcards': [
            {'id': 'fc-09-01', 'front': 'Who constitutes the Electoral College for the election of the President?', 'back': 'Elected members of both Houses of Parliament and elected members of State Legislative Assemblies (including Delhi and Puducherry).', 'category': 'Union Executive'},
            {'id': 'fc-09-02', 'front': 'What is the sole ground for impeachment of the President under Article 61?', 'back': 'Violation of the Constitution.', 'category': 'Union Executive'},
            {'id': 'fc-09-03', 'front': 'Which court has jurisdiction to decide disputes concerning the election of the President?', 'back': 'The Supreme Court of India exclusively (Article 71).', 'category': 'Judicial Review'}
        ],
        'sourceReferences': [
            {'title': 'Constitution of India, Articles 52–71', 'url': 'https://legislative.gov.in'},
            {'title': 'In re Presidential Election, 1974 (1974) 2 SCC 33', 'url': 'https://main.sci.gov.in'}
        ]
    }
}

PART3['top-const-09-02'] = {
    'topicId': 'top-const-09-02',
    'chapterId': 'ch-09',
    'title': 'Executive Powers, Ordinance Making & Pardoning Powers',
    'subtitle': 'Articles 72 & 123: Judicial Review of Pardons and Ordinances (D.C. Wadhwa, Kehar Singh)',
    'articleRef': 'Articles 72 and 123',
    'overview': 'This topic examines two of the most significant constitutional powers of the President: the executive clemency and pardoning powers under Article 72 and the legislative ordinance-making power under Article 123, along with their strict judicial limitations established in D.C. Wadhwa, Krishna Kumar Singh, Kehar Singh, and Epuru Sudhakar.',
    'detailedStudy': {
        'learningObjectives': [
            'Differentiate between Pardon, Commutation, Remission, Respite, and Reprieve under Article 72.',
            'Examine the grounds and limits of judicial review over the exercise of pardoning power under Article 72.',
            'Analyze the conditions precedent for promulgating an Ordinance under Article 123 and its temporary lifespan.',
            'Evaluate the constitutional prohibition against repromulgation of ordinances without legislative scrutiny (D.C. Wadhwa).'
        ],
        'coreDoctrine': 'Under Article 72, the President has the power to grant pardons, reprieves, respites, or remissions of punishment, or to suspend, remit, or commute the sentence of any person convicted of an offence where the sentence is for an offence against a Union law, by a Court Martial, or in all cases of death sentence. The pardoning power is exercised on the aid and advice of the Council of Ministers, not in personal discretion (Maru Ram v. UOI). In Kehar Singh (1989), the Supreme Court affirmed that the President can scrutinize evidence afresh and come to a different conclusion from that recorded by the court. In Epuru Sudhakar (2006), the Court held that the clemency power is subject to limited judicial review on grounds of mala fides, extraneous considerations, or non-application of mind.\\n\\nArticle 123 vests the President with extraordinary power to promulgate Ordinances during recess of Parliament. Two conditions precedent must coexist: (1) neither House of Parliament is in session, and (2) circumstances exist which render it necessary for the President to take immediate action. An Ordinance has the same force and effect as an Act of Parliament, but ceases to operate at the expiration of 6 weeks from the reassembly of Parliament, or earlier if disapproved by both Houses. In D.C. Wadhwa (1987) and Krishna Kumar Singh (2017), the Supreme Court held that repeated repromulgation of ordinances without placing them before the legislature is a fraud on the Constitution and subverts democratic governance.',
        'statutoryProvisions': [
            {'article': 'Article 72', 'heading': 'Power of President to grant pardons, etc.', 'text': 'The President shall have the power to grant pardons, reprieves, respites or remissions of punishment or to suspend, remit or commute the sentence of any person convicted of any offence in all cases where sentence is a sentence of death, by court martial, or under Union executive competence.'},
            {'article': 'Article 123', 'heading': 'Power of President to promulgate Ordinances during recess of Parliament', 'text': 'If at any time, except when both Houses of Parliament are in session, the President is satisfied that circumstances exist which render it necessary for him to take immediate action, he may promulgate such Ordinances as the circumstances appear to him to require.'}
        ],
        'legalIngredients': [
            'Pardon: Completely absorbs both the conviction and sentence, restoring the individual to the status of an innocent citizen.',
            'Commutation: Substitution of one form of punishment for a lighter form (e.g. death sentence to life imprisonment).',
            'Remission: Reduction of the amount/period of sentence without altering its legal character (e.g. 5 years rigorous to 2 years rigorous).',
            'Respite: Awarding a lesser sentence on special factual grounds, such as pregnancy of a female offender or mental infirmity.',
            'Reprieve: Temporary stay of the execution of a sentence, especially death penalty, pending a clemency petition.',
            'Ordinance Lifespan: Maximum duration is 6 months (gap between sessions) + 6 weeks (from reassembly) = 7.5 months.'
        ],
        'exceptions': [
            'President cannot promulgate an Ordinance when BOTH Houses of Parliament are in session.',
            'Ordinance cannot abridge Fundamental Rights or amend the Constitution (Article 123(3) read with Article 13(2)).',
            'Governor cannot pardon death sentences under Article 161; only the President can pardon death sentences (though Governor may suspend, remit, or commute).'
        ],
        'practicalScenarios': [
            {'scenario': 'The Governor of a State pardons a death sentence convict under Article 161.', 'application': 'Unconstitutional. Under Article 72 and 161, only the President has the sovereign power to grant a complete pardon in death sentences; the Governor can only suspend, remit, or commute.'},
            {'scenario': 'An Ordinance is repromulgated four successive times without being tabled before Parliament.', 'application': 'Unconstitutional. As per Krishna Kumar Singh v. State of Bihar (2017), repeated repromulgation without legislative laying is an abuse of executive power and void ab initio.'}
        ],
        'landmarkCases': [
            {'case': 'Maru Ram v. Union of India', 'citation': '(1981) 1 SCC 107', 'year': '1980', 'bench': '5-Judge Bench (Krishna Iyer J)', 'ratio': 'Held that the power under Article 72/161 is exercised on the advice of the Council of Ministers and cannot be exercised arbitrarily.', 'impact': 'Subordinated clemency power to constitutional cabinet advice.'},
            {'case': 'Kehar Singh v. Union of India', 'citation': '(1989) 1 SCC 204', 'year': '1989', 'bench': '5-Judge Bench (Pathak CJ)', 'ratio': 'Held that the President under Article 72 can examine the evidence afresh and come to a different conclusion from that of the courts.', 'impact': 'Affirmed wide plenary scope of presidential pardon.'},
            {'case': 'Epuru Sudhakar v. Govt. of A.P.', 'citation': '(2006) 8 SCC 161', 'year': '2006', 'bench': '2-Judge Bench (Pasayat J)', 'ratio': 'Held that pardoning power is subject to judicial review on grounds of mala fides, extraneous political considerations, or total non-application of mind.', 'impact': 'Established clear standards for judicial review of clemency.'},
            {'case': 'Krishna Kumar Singh v. State of Bihar', 'citation': '(2017) 3 SCC 1', 'year': '2017', 'bench': '7-Judge Bench (Chandrachud J)', 'ratio': 'Held that laying an ordinance before the legislature is mandatory; repeated repromulgation is a fraud on the Constitution and does not create permanent rights.', 'impact': 'Ended practice of ordinance raj across Indian States.'}
        ],
        'comparisonTables': [
            {
                'title': 'Clemency Forms under Article 72',
                'headers': ['Term', 'Legal Effect', 'Distinguishing Factor'],
                'rows': [
                    ['Pardon', 'Wipes out both guilt and punishment', 'Restores status quo ante as if no offence was committed'],
                    ['Commutation', 'Changes nature of punishment to lighter form', 'e.g., Death to Life Imprisonment'],
                    ['Remission', 'Reduces duration without altering nature', 'Rigorous remains rigorous, but time is shortened'],
                    ['Respite', 'Postpones or awards lesser sentence for special reason', 'Pregnancy, medical extremity, physical infirmity'],
                    ['Reprieve', 'Temporary stay of execution', 'Enables offender to seek clemency before execution']
                ]
            }
        ],
        'diagramId': 'diag-ordinance-lifespan-timeline',
        'diagramExplanation': 'Timeline depicting the promulgation, session recess, reassembly, and the 6-week expiry window of presidential ordinances.',
        'misconceptions': [
            {'myth': 'The President can pardon death sentences in his personal moral discretion.', 'reality': 'The power under Article 72 must be exercised strictly on the binding aid and advice of the Union Cabinet (Maru Ram case).'}
        ],
        'prelimTraps': [
            {'trap': 'What is the maximum lifespan of an Ordinance if Parliament does not approve it upon reassembly?', 'reality': 'Six weeks from the date of reassembly of Parliament.', 'rule': 'Art. 123 = 6 weeks from reassembly.'},
            {'trap': 'Can an Ordinance amend a Fundamental Right?', 'reality': 'No, under Article 13(2) and Article 123(3), an Ordinance is "law" and subject to constitutional limitations.', 'rule': 'Ordinance cannot violate Part III.'}
        ],
        'quickRevision': {
            'keyArticles': [
                {'article': 'Art. 72', 'crux': 'Presidential clemency: Pardon, commute, remit, respite, reprieve.'},
                {'article': 'Art. 123', 'crux': 'Ordinance power during recess; ceases 6 weeks after reassembly.'},
                {'article': 'Art. 161', 'crux': 'Governor pardoning power (cannot pardon death sentence).'}
            ],
            'bulletSummary': [
                'Presidential pardon applies to Union laws, Court Martial, and death sentences.',
                'Governor cannot pardon death penalty or court martial sentences.',
                'Ordinance requires either or both Houses to be not in session.',
                'Repromulgation of ordinances without legislative approval is unconstitutional (Krishna Kumar Singh).'
            ],
            'mnemonics': [
                {'phrase': 'PCR-RR', 'meaning': 'Pardon, Commutation, Remission, Respite, Reprieve (the 5 Art. 72 clemencies).'}
            ],
            'oneLinerRules': [
                'An ordinance expires precisely 6 weeks from the date Parliament reassembles unless approved earlier.',
                'Pardoning power under Article 72 is justiciable on grounds of arbitrariness, mala fides, or irrelevant considerations.'
            ]
        },
        'flashcards': [
            {'id': 'fc-09-04', 'front': 'What is the maximum period an Ordinance can remain in force without parliamentary approval after reassembly?', 'back': 'Six weeks from the date of reassembly of Parliament.', 'category': 'Union Executive'},
            {'id': 'fc-09-05', 'front': 'Can the Governor of a State grant a pardon in case of a death sentence under Article 161?', 'back': 'No; only the President can grant a full pardon for death sentences (Article 72).', 'category': 'Constitutional Powers'},
            {'id': 'fc-09-06', 'front': 'Which 7-Judge bench decision declared repeated repromulgation of ordinances a fraud on the Constitution?', 'back': 'Krishna Kumar Singh v. State of Bihar (2017).', 'category': 'Case Law'}
        ],
        'sourceReferences': [
            {'title': 'Constitution of India, Articles 72 & 123', 'url': 'https://legislative.gov.in'},
            {'title': 'Krishna Kumar Singh v. State of Bihar (2017) 3 SCC 1', 'url': 'https://main.sci.gov.in'}
        ]
    }
}

PART3['top-const-09-03'] = {
    'topicId': 'top-const-09-03',
    'chapterId': 'ch-09',
    'title': 'Prime Minister, Council of Ministers & Attorney-General',
    'subtitle': 'Articles 74, 75, 76 & 78: Collective Responsibility & First Law Officer',
    'articleRef': 'Articles 74, 75, 76, 78',
    'overview': 'This topic examines the Westminster cabinet framework in India: the Prime Minister as head of government, the Council of Ministers, collective responsibility to the Lok Sabha, the constitutional ceiling on cabinet size (91st Amendment), the role of the Attorney-General as the first law officer, and the duty of the PM to furnish information to the President under Article 78.',
    'detailedStudy': {
        'learningObjectives': [
            'Analyze the binding nature of the aid and advice of the Council of Ministers under Article 74(1) post 42nd and 44th Amendments.',
            'Examine the principle of Collective Responsibility under Article 75(3) and individual ministerial responsibility.',
            'Apply the 91st Amendment ceiling on the size of the Council of Ministers (15% limit).',
            'Evaluate the constitutional status, qualifications, and privileges of the Attorney-General for India under Article 76.'
        ],
        'coreDoctrine': 'The Indian executive operates on the Westminster model. Article 74(1) provides that there shall be a Council of Ministers with the Prime Minister at the head to aid and advise the President who shall, in the exercise of his functions, act in accordance with such advice. The 42nd Amendment made this advice explicitly binding; the 44th Amendment added a proviso permitting the President to require the Council of Ministers to reconsider such advice once, but the President is bound to act in accordance with the advice tendered after reconsideration. Article 74(2) bars judicial inquiry into the question whether any, and if so what, advice was tendered by Ministers to the President (though the factual background materials relied upon may be scrutinized, as in S.R. Bommai).\\n\\nArticle 75 establishes collective responsibility: the Council of Ministers is collectively responsible to the House of the People (Lok Sabha). If a vote of no-confidence is passed, the entire Council of Ministers must resign. Under the 91st Constitutional Amendment Act, 2003, Article 75(1A) restricts the total number of Ministers, including the Prime Minister, to not exceed 15% of the total number of members of the House of the People. Article 76 creates the office of the Attorney-General for India, appointed by the President, qualified to be appointed a Judge of the Supreme Court, holding office during the pleasure of the President, with right of audience in all courts in India and right to speak in both Houses of Parliament without the right to vote (Article 88).',
        'statutoryProvisions': [
            {'article': 'Article 74', 'heading': 'Council of Ministers to aid and advise President', 'text': 'There shall be a Council of Ministers with the Prime Minister at the head to aid and advise the President who shall, in the exercise of his functions, act in accordance with such advice.'},
            {'article': 'Article 75', 'heading': 'Other provisions as to Ministers', 'text': 'The Prime Minister shall be appointed by the President and the other Ministers shall be appointed by the President on the advice of the Prime Minister. Council of Ministers shall be collectively responsible to the House of the People.'},
            {'article': 'Article 75(1A)', 'heading': 'Ceiling on Ministry Size', 'text': 'The total number of Ministers, including the Prime Minister, in the Council of Ministers shall not exceed fifteen per cent of the total number of members of the House of the People.'},
            {'article': 'Article 76', 'heading': 'Attorney-General for India', 'text': 'The President shall appoint a person who is qualified to be appointed a Judge of the Supreme Court to be Attorney-General for India.'},
            {'article': 'Article 78', 'heading': 'Duties of Prime Minister as respects the furnishing of information to the President', 'text': 'To communicate to the President all decisions of the Council of Ministers relating to the administration of the affairs of the Union and proposals for legislation.'}
        ],
        'legalIngredients': [
            'Aid and Advice: Reconsideration permitted once (44th Amendment); binding thereafter.',
            'Article 74(2) Injunction: Courts cannot inquire into ministerial advice itself.',
            'Collective Responsibility: Ministers sink and swim together; dissenters must resign.',
            'Ministerial Tenure: Ministers hold office during the pleasure of the President (Article 75(2)), which practically means at the pleasure of the Prime Minister.',
            'Six-Month Window: A Minister who for any period of six consecutive months is not a member of either House ceases to be a Minister (Article 75(5)).',
            'Attorney-General: First Law Officer, right of audience in all Indian courts, right to speak in Parliament (Art. 88), no vote.'
        ],
        'exceptions': [
            'The President may act in personal discretion in appointing a Prime Minister when no single party or coalition commands a clear majority.',
            'The Attorney-General does not have a right to vote in Parliament (Article 88).'
        ],
        'practicalScenarios': [
            {'scenario': 'A Prime Minister advises the President to appoint a non-MP as a Cabinet Minister.', 'application': 'Valid under Article 75(5). The appointee has 6 consecutive months to be elected or nominated to either House of Parliament, failing which they vacate office.'},
            {'scenario': 'A litigant seeks discovery of the cabinet advice tendered to the President under Article 74.', 'application': 'Barred under Article 74(2); however, official background reports and materials placed before Cabinet are not immune from production (S.R. Bommai v. UOI).'}
        ],
        'landmarkCases': [
            {'case': 'Shamsher Singh v. State of Punjab', 'citation': '(1974) 2 SCC 831', 'year': '1974', 'bench': '7-Judge Bench (Ray CJ)', 'ratio': 'Held that the President and Governors are constitutional heads who must exercise powers strictly on the advice of the Council of Ministers, except where discretion is explicitly mandated.', 'impact': 'Solidified cabinet supremacy in parliamentary democracy.'},
            {'case': 'U.N.R. Rao v. Indira Gandhi', 'citation': '(1971) 2 SCC 63', 'year': '1971', 'bench': '5-Judge Bench (Sikri CJ)', 'ratio': 'Held that Article 74(1) is mandatory; even upon dissolution of the Lok Sabha, the Council of Ministers does not cease to exist, as the President cannot act without ministerial advice.', 'impact': 'Affirmed continuous constitutional existence of Union Cabinet.'}
        ],
        'comparisonTables': [
            {
                'title': 'Attorney-General vs Advocate-General',
                'headers': ['Parameter', 'Attorney-General for India (Art. 76)', 'Advocate-General for State (Art. 165)'],
                'rows': [
                    ['Appointing Authority', 'President of India', 'Governor of the State'],
                    ['Qualification', 'Qualified to be Supreme Court Judge', 'Qualified to be High Court Judge'],
                    ['Territorial Audience', 'All courts throughout India', 'All courts within the concerned State'],
                    ['Tenure', 'Pleasure of the President', 'Pleasure of the Governor'],
                    ['Parliamentary Right', 'Right to speak in both Houses, no vote (Art. 88)', 'Right to speak in State Legislature, no vote (Art. 177)']
                ]
            }
        ],
        'diagramId': 'diag-cabinet-accountability-tree',
        'diagramExplanation': 'Hierarchical diagram depicting PM leadership, Cabinet ministers, Council of Ministers, and collective responsibility to Lok Sabha.',
        'misconceptions': [
            {'myth': 'The Attorney-General is a full-time government servant and member of the Union Cabinet.', 'reality': 'The AG is not a cabinet minister or government servant; the AG is an independent constitutional law officer permitted to maintain private legal practice with restrictions.'}
        ],
        'prelimTraps': [
            {'trap': 'What is the ceiling on the number of Ministers under Article 75(1A)?', 'reality': '15% of the total membership of the House of the People (Lok Sabha), not Parliament.', 'rule': 'Art. 75(1A) = 15% of Lok Sabha.'},
            {'trap': 'Can the Attorney-General vote in a joint sitting of Parliament?', 'reality': 'No, under Article 88 the AG has the right to speak and take part, but cannot vote.', 'rule': 'Art. 88 = Speak yes, Vote no.'}
        ],
        'quickRevision': {
            'keyArticles': [
                {'article': 'Art. 74', 'crux': 'Council of Ministers aids & advises President; advice binding.'},
                {'article': 'Art. 75', 'crux': 'PM appointed by President; Collective responsibility to Lok Sabha.'},
                {'article': 'Art. 75(1A)', 'crux': '15% cap on size of Ministry (91st Amendment).'},
                {'article': 'Art. 76', 'crux': 'Attorney-General: First Law Officer, pleasure of President.'},
                {'article': 'Art. 78', 'crux': 'Prime Minister duty to inform President.'}
            ],
            'bulletSummary': [
                'President must accept advice after one reconsideration under Article 74(1).',
                'Council of Ministers is collectively responsible to Lok Sabha, not Rajya Sabha.',
                'A non-member of Parliament can be minister for at most 6 consecutive months.',
                'Attorney-General has right of audience in all courts across India.'
            ],
            'mnemonics': [
                {'phrase': 'MIN-15-LOK', 'meaning': 'Ministry size cannot exceed 15% of Lok Sabha members (Art. 75(1A)).'}
            ],
            'oneLinerRules': [
                'Collective responsibility means a loss of majority in Lok Sabha necessitates the resignation of all Ministers.',
                'Courts cannot inquire into the advice tendered by Ministers to the President under Article 74(2).'
            ]
        },
        'flashcards': [
            {'id': 'fc-09-07', 'front': 'Which Constitutional Amendment introduced the 15% ceiling on the Council of Ministers?', 'back': '91st Constitutional Amendment Act, 2003.', 'category': 'Union Executive'},
            {'id': 'fc-09-08', 'front': 'To which House of Parliament is the Council of Ministers collectively responsible?', 'back': 'The House of the People (Lok Sabha) under Article 75(3).', 'category': 'Union Executive'},
            {'id': 'fc-09-09', 'front': 'Can the Attorney-General of India participate in proceedings of Parliament?', 'back': 'Yes, under Article 88 the AG can speak and take part in proceedings of either House, but has no right to vote.', 'category': 'Constitutional Bodies'}
        ],
        'sourceReferences': [
            {'title': 'Constitution of India, Articles 74, 75, 76, 78', 'url': 'https://legislative.gov.in'},
            {'title': 'Shamsher Singh v. State of Punjab (1974) 2 SCC 831', 'url': 'https://main.sci.gov.in'}
        ]
    }
}

print("Chapter 9 populated successfully.")
