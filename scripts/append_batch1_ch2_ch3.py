"""
Append Chapters 2 and 3 MCQs to scripts/mcq_batch_1.py
Ch 2: 30 MCQs | Ch 3: 25 MCQs
"""

with open('scripts/mcq_batch_1.py', 'a', encoding='utf-8') as f:
    f.write('''
# ------------------------------------------------------------------------------
# CHAPTER 2: MAKING OF THE CONSTITUTION & SALIENT FEATURES (30 MCQs)
# ------------------------------------------------------------------------------
# Topic 1: Constituent Assembly & Drafting (10 MCQs)
q('mcq-const-02-001', 'ch-02', 'top-const-02-01',
  'Who first officially put forward the idea of a Constituent Assembly for India in 1934?',
  ['Mahatma Gandhi', 'Jawaharlal Nehru', 'M.N. Roy', 'Subhas Chandra Bose'],
  2,
  'In 1934, M.N. Roy (a pioneer of the communist movement in India and advocate of radical democratism) first put forward the idea of a Constituent Assembly for India. INC officially demanded it in 1935.',
  {'A': 'Mahatma Gandhi demanded swaraj determined by Indian will in 1922.', 'B': 'Jawaharlal Nehru framed the demand on adult franchise in 1938.', 'C': 'Correct. M.N. Roy first put forward the idea in 1934.', 'D': 'Subhas Chandra Bose led the Forward Bloc and INA.'},
  'Easy', 'Constituent Assembly Genesis', 'Recall earliest proponent of Constituent Assembly.')

q('mcq-const-02-002', 'ch-02', 'top-const-02-01',
  'The Constituent Assembly of India was set up under the framework formulated by:',
  ['The Cripps Mission, 1942', 'The Cabinet Mission Plan, 1946', 'The Wavell Plan, 1945', 'The Mountbatten Plan, 1947'],
  1,
  'The Constituent Assembly was constituted in November 1946 under the scheme formulated by the Cabinet Mission Plan (Lord Pethick-Lawrence, Sir Stafford Cripps, and A.V. Alexander).',
  {'A': 'Cripps proposals in 1942 were rejected by all major parties.', 'B': 'Correct. Cabinet Mission Plan 1946 structured the Constituent Assembly.', 'C': 'Wavell Plan broke down at Simla.', 'D': 'Mountbatten Plan was for partition and independence.'},
  'Easy', 'Cabinet Mission Plan, 1946', 'Identify founding constitutional scheme.')

q('mcq-const-02-003', 'ch-02', 'top-const-02-01',
  'Who presided over the inaugural meeting of the Constituent Assembly on December 9, 1946 as its temporary Chairman?',
  ['Dr. Rajendra Prasad', 'Dr. B.R. Ambedkar', 'Dr. Sachchidananda Sinha', 'H.C. Mukherjee'],
  2,
  'Following the French practice of electing the oldest member, Dr. Sachchidananda Sinha presided over the inaugural meeting on 9th December 1946 as temporary Chairman.',
  {'A': 'Dr. Rajendra Prasad was elected permanent President on 11th December 1946.', 'B': 'Dr. B.R. Ambedkar was Chairman of the Drafting Committee.', 'C': 'Correct. Dr. Sachchidananda Sinha was temporary Chairman.', 'D': 'H.C. Mukherjee was elected Vice-President along with V.T. Krishnamachari.'},
  'Easy', 'Constituent Assembly Debates, 9 Dec 1946', 'Recall temporary Chairman of Constituent Assembly.')

q('mcq-const-02-004', 'ch-02', 'top-const-02-01',
  'Who was appointed as the Constitutional Adviser (Legal Adviser) to the Constituent Assembly?',
  ['Sir B.N. Rau', 'Dr. K.M. Munshi', 'Alladi Krishnaswami Iyer', 'Sir B.L. Mitter'],
  0,
  'Sir Benegal Narsing Rau (B.N. Rau), an eminent jurist and former ICJ judge, was appointed as the Constitutional Adviser to the Constituent Assembly and prepared the initial draft of the Constitution.',
  {'A': 'Correct. Sir B.N. Rau was the Constitutional Adviser.', 'B': 'Dr. K.M. Munshi was a member of the Drafting Committee.', 'C': 'Alladi Krishnaswami Iyer was an eminent member of the Drafting Committee.', 'D': 'Sir B.L. Mitter resigned from the Drafting Committee due to ill-health.'},
  'Easy', 'Constituent Assembly Secretariat', 'Identify Constitutional Adviser.')

q('mcq-const-02-005', 'ch-02', 'top-const-02-01',
  'On which date was the historic "Objectives Resolution" moved in the Constituent Assembly by Jawaharlal Nehru?',
  ['9th December, 1946', '13th December, 1946', '22nd January, 1947', '26th November, 1949'],
  1,
  'Jawaharlal Nehru moved the historic "Objectives Resolution" on 13th December 1946, outlining the constitutional ideals and philosophy. It was unanimously adopted on 22nd January 1947 and shaped the Preamble.',
  {'A': '9th December 1946 was the first meeting.', 'B': 'Correct. Moved on 13th December 1946.', 'C': '22nd January 1947 was the date of its unanimous adoption.', 'D': '26th November 1949 was adoption of the Constitution.'},
  'Medium', 'Constituent Assembly Debates, 13 Dec 1946', 'Identify date of Objectives Resolution.')

q('mcq-const-02-006', 'ch-02', 'top-const-02-01',
  'The Drafting Committee was appointed by the Constituent Assembly on:',
  ['15th August, 1947', '29th August, 1947', '26th November, 1949', '24th January, 1950'],
  1,
  'The Drafting Committee under the Chairmanship of Dr. B.R. Ambedkar was constituted on 29th August 1947 to prepare a draft of the new Constitution based on the initial draft by B.N. Rau.',
  {'A': '15th August 1947 was Independence Day.', 'B': 'Correct. 29th August 1947 was appointment of Drafting Committee.', 'C': '26th November 1949 was adoption.', 'D': '24th January 1950 was final signing.'},
  'Medium', 'Constituent Assembly Resolution, 29 Aug 1947', 'Recall appointment date of Drafting Committee.')

q('mcq-const-02-007', 'ch-02', 'top-const-02-01',
  'How many members constituted the Drafting Committee of the Constituent Assembly?',
  ['Five', 'Seven', 'Nine', 'Eleven'],
  1,
  'The Drafting Committee consisted of seven members: Dr. B.R. Ambedkar (Chairman), N. Gopalaswamy Ayyangar, Alladi Krishnaswami Iyer, Dr. K.M. Munshi, Syed Mohammad Saadulla, N. Madhava Rau (replaced B.L. Mitter), and T.T. Krishnamachari (replaced D.P. Khaitan).',
  {'A': 'Five is incorrect.', 'B': 'Correct. Exactly seven members.', 'C': 'Nine is incorrect.', 'D': 'Eleven is incorrect.'},
  'Easy', 'Drafting Committee Composition', 'Recall number of Drafting Committee members.')

q('mcq-const-02-008', 'ch-02', 'top-const-02-01',
  'How much time did the Constituent Assembly take to frame the Constitution of India?',
  ['2 years, 11 months and 18 days', '3 years, 2 months and 11 days', '1 year, 11 months and 28 days', '2 years, 9 months and 15 days'],
  0,
  'The Constituent Assembly held 11 sessions covering a total duration of 2 years, 11 months, and 18 days between 9th December 1946 and 26th November 1949.',
  {'A': 'Correct. 2 years, 11 months, 18 days.', 'B': 'Incorrect duration.', 'C': 'Incorrect duration.', 'D': 'Incorrect duration.'},
  'Easy', 'Constituent Assembly Records', 'Recall duration of constitutional drafting.')

q('mcq-const-02-009', 'ch-02', 'top-const-02-01',
  'Which of the following provisions of the Constitution came into immediate force on 26th November 1949 (date of adoption)?',
  ['Fundamental Rights (Articles 14 to 32)', 'Directive Principles of State Policy (Articles 36 to 51)', 'Citizenship (Articles 5–9), Elections (Article 324), and Provisional Parliament', 'Emergency Provisions (Articles 352 to 360)'],
  2,
  'Under Article 394, Articles 5, 6, 7, 8, 9, 60, 324, 366, 367, 379, 380, 388, 391, 392, and 393 came into force immediately on 26th November 1949; the remaining provisions came into force on 26th January 1950.',
  {'A': 'Fundamental rights came into force on 26 January 1950.', 'B': 'DPSP came into force on 26 January 1950.', 'C': 'Correct. Citizenship, Elections, and Provisional Parliament commenced immediately on 26 Nov 1949.', 'D': 'Emergency provisions commenced on 26 January 1950.'},
  'Hard', 'Article 394', 'Identify provisions commencing on 26 November 1949.')

q('mcq-const-02-010', 'ch-02', 'top-const-02-01',
  'Who was the calligrapher of the original Hindi and English handwritten copies of the Constitution of India?',
  ['Nandalal Bose', 'Prem Behari Narain Raizada', 'Beohar Rammanohar Sinha', 'K.M. Munshi'],
  1,
  'Prem Behari Narain Raizada was the calligrapher of the original handwritten English text of the Constitution, written in flowing italic style. Nandalal Bose and Rammanohar Sinha illuminated and decorated the pages.',
  {'A': 'Nandalal Bose was the master artist who decorated the pages.', 'B': 'Correct. Prem Behari Narain Raizada was the calligrapher.', 'C': 'Rammanohar Sinha illuminated the Preamble page.', 'D': 'K.M. Munshi was a drafting committee member.'},
  'Medium', 'Constituent Assembly Art Records', 'Recall calligrapher of original Constitution.')

# Topic 2: Sources of the Constitution (10 MCQs)
q('mcq-const-02-011', 'ch-02', 'top-const-02-02',
  'The concept of "Directive Principles of State Policy" was borrowed from the Constitution of:',
  ['USSR', 'USA', 'Ireland', 'Australia'],
  2,
  'Directive Principles of State Policy in Part IV were borrowed from the 1937 Constitution of Ireland (which had in turn copied them from the Spanish Constitution).',
  {'A': 'USSR inspired Fundamental Duties and Planning.', 'B': 'USA inspired Fundamental Rights and Judicial Review.', 'C': 'Correct. Ireland inspired DPSP.', 'D': 'Australia inspired Concurrent List.'},
  'Easy', 'Part IV Genesis', 'Identify source of DPSP.')

q('mcq-const-02-012', 'ch-02', 'top-const-02-02',
  'The procedure for "Amendment of the Constitution" and election of members of Rajya Sabha were borrowed from:',
  ['South Africa', 'Canada', 'Germany (Weimar)', 'Japan'],
  0,
  'Article 368 amendment procedure and the election of members of the Rajya Sabha were borrowed from the Constitution of South Africa.',
  {'A': 'Correct. South Africa provided the amendment procedure.', 'B': 'Canada inspired strong center federalism.', 'C': 'Weimar Germany inspired suspension of FRs in emergency.', 'D': 'Japan inspired "procedure established by law".'},
  'Medium', 'Article 368 Genesis', 'Identify source of constitutional amendment.')

q('mcq-const-02-013', 'ch-02', 'top-const-02-02',
  'The "Concurrent List" and the provision for "Joint Sitting of Parliament" were borrowed from:',
  ['Canada', 'Australia', 'United Kingdom', 'United States'],
  1,
  'The Concurrent List (Seventh Schedule), freedom of trade and commerce (Part XIII), and the mechanism of Joint Sitting of both Houses of Parliament (Article 108) were borrowed from the Australian Constitution.',
  {'A': 'Canada provided advisory jurisdiction and residuary powers in Centre.', 'B': 'Correct. Australia provided Concurrent List and Joint Sitting.', 'C': 'UK provided parliamentary system and rule of law.', 'D': 'USA provided impeachment and independent judiciary.'},
  'Medium', 'Article 108 Genesis', 'Identify Australian borrowed features.')

q('mcq-const-02-014', 'ch-02', 'top-const-02-02',
  'The phrase "Procedure Established by Law" under Article 21 was borrowed from the Constitution of:',
  ['United States of America', 'United Kingdom', 'Japan', 'France'],
  2,
  'Article 21 adopted "procedure established by law" from Article 31 of the 1946 Japanese Constitution on the specific advice of Justice Felix Frankfurter of the US Supreme Court to Sir B.N. Rau.',
  {'A': 'USA has "due process of law".', 'B': 'UK follows parliamentary sovereignty.', 'C': 'Correct. Japan was the source of "procedure established by law".', 'D': 'France provided ideals of Liberty, Equality, Fraternity.'},
  'Hard', 'Article 21 Genesis', 'Identify Japanese constitutional source.')

q('mcq-const-02-015', 'ch-02', 'top-const-02-02',
  'From which Constitution was the idea of "Residual Powers vested in the Centre" and a "Federation with a Strong Centre" adopted?',
  ['United States of America', 'Canada', 'Australia', 'Switzerland'],
  1,
  'The Indian federal model—a federation with a strong Centre, vesting residuary powers in the Union (Article 248), and appointment of State Governors by the Centre—was borrowed from the Canadian Constitution.',
  {'A': 'USA gives residuary powers to the States.', 'B': 'Correct. Canada provided strong Centre and residuary power model.', 'C': 'Australia has coordinate federalism.', 'D': 'Switzerland is a confederation.'},
  'Medium', 'Federal Structure Genesis', 'Identify Canadian federal features.')

q('mcq-const-02-016', 'ch-02', 'top-const-02-02',
  'The ideals of "Liberty, Equality and Fraternity" in the Preamble were borrowed from the:',
  ['American Declaration of Independence', 'Russian Revolution (1917)', 'French Revolution (1789)', 'Glorious Revolution (1688)'],
  2,
  'The ideals of Liberty, Equality, and Fraternity enshrined in the Preamble were inspired by the motto of the French Revolution (1789). Ideals of Justice (Social, Economic, Political) were borrowed from the Russian Revolution (1917).',
  {'A': 'American Revolution gave inalienable life, liberty, pursuit of happiness.', 'B': 'Russian Revolution gave Justice: Social, Economic, Political.', 'C': 'Correct. French Revolution gave Liberty, Equality, Fraternity.', 'D': 'Glorious Revolution established parliamentary supremacy in England.'},
  'Easy', 'Preamble Genesis', 'Trace French origin of liberty, equality, fraternity.')

q('mcq-const-02-017', 'ch-02', 'top-const-02-02',
  'The concept of "Fundamental Duties" in Part IVA was inspired by the Constitution of:',
  ['USA', 'Former USSR (Soviet Union)', 'Ireland', 'Germany'],
  1,
  'Fundamental Duties (Article 51A) were inspired by the Constitution of the erstwhile USSR, which uniquely emphasized the correspondence between citizen duties and socialist rights.',
  {'A': 'US Constitution has no charter of duties.', 'B': 'Correct. USSR inspired Fundamental Duties.', 'C': 'Ireland inspired DPSP.', 'D': 'Germany inspired emergency provisions.'},
  'Easy', 'Part IVA Genesis', 'Identify USSR source of Fundamental Duties.')

q('mcq-const-02-018', 'ch-02', 'top-const-02-02',
  'Which of the following features was NOT borrowed from the British Constitution?',
  ['Parliamentary form of government', 'Cabinet system and Rule of Law', 'Prerogative writs', 'Judicial Review and independence of the judiciary'],
  3,
  'Judicial Review and the independence of the judiciary were borrowed from the Constitution of the United States of America. Britain follows parliamentary supremacy without judicial review of primary legislation.',
  {'A': 'Parliamentary form is British.', 'B': 'Cabinet and Rule of Law are British.', 'C': 'Prerogative writs are British.', 'D': 'Correct. Judicial Review is American, not British.'},
  'Medium', 'Comparative Constitutional Law', 'Differentiate British from American borrowed concepts.')

q('mcq-const-02-019', 'ch-02', 'top-const-02-02',
  'Suspension of Fundamental Rights during an Emergency was borrowed from:',
  ['Government of India Act, 1935', 'Weimar Constitution of Germany', 'Constitution of South Africa', 'Irish Constitution'],
  1,
  'The provision relating to the suspension of the enforcement of fundamental rights during an emergency (Article 359) was borrowed from the Weimar Constitution of Germany.',
  {'A': '1935 Act provided emergency machinery, but suspension of FRs came from Weimar.', 'B': 'Correct. Weimar Constitution of Germany inspired suspension of rights.', 'C': 'South Africa inspired amendments.', 'D': 'Ireland inspired DPSP.'},
  'Medium', 'Emergency Genesis', 'Identify German Weimar origin of emergency rights suspension.')

q('mcq-const-02-020', 'ch-02', 'top-const-02-02',
  'From which statute is approximately 60% of the administrative and structural provisions of the Indian Constitution directly derived?',
  ['Government of India Act, 1919', 'Government of India Act, 1935', 'Indian Independence Act, 1947', 'Indian Councils Act, 1909'],
  1,
  'The Government of India Act, 1935 provided the primary structural framework: federal scheme, office of governor, judiciary, public service commissions, emergency provisions, and administrative details.',
  {'A': '1919 provided provincial dyarchy.', 'B': 'Correct. 1935 Act was the structural backbone.', 'C': '1947 was transitional.', 'D': '1909 was imperial.'},
  'Easy', 'Structural Blueprint', 'Recall 1935 Act dominance in Constitution.')

# Topic 3: Salient Features (10 MCQs)
q('mcq-const-02-021', 'ch-02', 'top-const-02-03',
  'Who famously characterized the Indian Constitution as "Quasi-Federal"?',
  ['Sir Ivor Jennings', 'Prof. K.C. Wheare', 'Granville Austin', 'Morris-Jones'],
  1,
  'Prof. K.C. Wheare described the Indian Constitution as "quasi-federal"—a unitary state with subsidiary federal features rather than a federal state with subsidiary unitary features.',
  {'A': 'Sir Ivor Jennings called it a "lawyer\'s paradise" and "federation with strong centralising tendency".', 'B': 'Correct. Prof. K.C. Wheare coined "quasi-federal".', 'C': 'Granville Austin called it "cooperative federalism".', 'D': 'Morris-Jones called it "bargaining federalism".'},
  'Easy', 'Federal Character Jurisprudence', 'Recall K.C. Wheare\'s quasi-federal characterization.')

q('mcq-const-02-022', 'ch-02', 'top-const-02-03',
  'Who described the Fundamental Rights and Directive Principles of State Policy as the "Conscience of the Constitution"?',
  ['Dr. B.R. Ambedkar', 'Granville Austin', 'K.M. Munshi', 'Sir Alladi Krishnaswami Iyer'],
  1,
  'Renowned constitutional historian Granville Austin characterized Fundamental Rights (Part III) and Directive Principles of State Policy (Part IV) as the "Conscience of the Constitution".',
  {'A': 'Dr. Ambedkar called Article 32 the "heart and soul".', 'B': 'Correct. Granville Austin called Parts III & IV the "Conscience of the Constitution".', 'C': 'K.M. Munshi called the Preamble the "political horoscope".', 'D': 'Alladi was a drafting architect.'},
  'Medium', 'Constitutional Philosophy', 'Identify Granville Austin\'s conscience phrase.')

q('mcq-const-02-023', 'ch-02', 'top-const-02-03',
  'The synthesis of "Parliamentary Sovereignty" and "Judicial Supremacy" in India represents a blend of:',
  ['British parliamentary supremacy and American judicial supremacy', 'French presidentialism and Swiss referendum', 'Canadian federalism and Australian commerce', 'Irish directives and Russian planning'],
  0,
  'The Indian constitutional framework uniquely synthesizes the British principle of parliamentary sovereignty (limited by written constitution and fundamental rights) and the American principle of judicial supremacy (curbed by legislative amendments).',
  {'A': 'Correct. Blend of British Parliamentary Sovereignty and American Judicial Supremacy.', 'B': 'India has neither French semi-presidentialism nor Swiss direct democracy.', 'C': 'Australia/Canada influenced specific clauses, not sovereignty synthesis.', 'D': 'Ideological sources.'},
  'Medium', 'Constitutional Architecture', 'Understand synthesis of sovereignty and judicial review.')

q('mcq-const-02-024', 'ch-02', 'top-const-02-03',
  'Which Constitutional Amendment lowered the voting age for elections to the Lok Sabha and State Legislative Assemblies from 21 years to 18 years?',
  ['42nd Amendment Act, 1976', '44th Amendment Act, 1978', '61st Amendment Act, 1988', '73rd Amendment Act, 1992'],
  2,
  'The 61st Constitutional Amendment Act, 1988 (which came into force in 1989) amended Article 326 to lower the voting age from 21 years to 18 years.',
  {'A': '42nd Amendment was mini-constitution.', 'B': '44th Amendment restored civil liberties.', 'C': 'Correct. 61st Amendment Act 1988 reduced voting age to 18.', 'D': '73rd Amendment constitutionalized Panchayats.'},
  'Easy', 'Article 326 & 61st Amendment', 'Recall voting age reduction amendment.')

q('mcq-const-02-025', 'ch-02', 'top-const-02-03',
  'How many Schedules did the Constitution of India contain at the time of its commencement in 1950?',
  ['Eight', 'Ten', 'Twelve', 'Seven'],
  0,
  'The original Constitution of India consisted of a Preamble, 395 Articles divided into 22 Parts, and 8 Schedules. Today it has 12 Schedules.',
  {'A': 'Correct. Exactly eight Schedules originally.', 'B': 'Ten is incorrect (Tenth added in 1985).', 'C': 'Twelve is current count.', 'D': 'Seven is incorrect.'},
  'Easy', 'Commencement Baseline', 'Recall original number of Schedules.')

q('mcq-const-02-026', 'ch-02', 'top-const-02-03',
  'Which of the following is NOT a unitary feature of the Indian Constitution?',
  ['Single Citizenship', 'Integrated Judiciary', 'Bicameral Legislature', 'Appointment of State Governor by the Centre'],
  2,
  'A Bicameral Legislature (Council of States and House of the People) is a classic FEDERAL feature ensuring territorial representation of States. Single citizenship, integrated judiciary, and Governor appointment are unitary/centralizing features.',
  {'A': 'Single citizenship is a unitary feature.', 'B': 'Integrated judiciary is a unitary feature.', 'C': 'Correct. Bicameralism is a federal feature.', 'D': 'Governor appointment by Centre is a unitary feature.'},
  'Medium', 'Federal vs Unitary Classification', 'Classify federal and unitary constitutional traits.')

q('mcq-const-02-027', 'ch-02', 'top-const-02-03',
  'The Indian Constitution is characterized as "flexible as well as rigid" because:',
  ['It can only be amended by simple majority', 'Some provisions can be amended by simple majority outside Art. 368, while others require special majority and state ratification', 'It can never be amended without a referendum', 'It requires approval of the Supreme Court for every amendment'],
  1,
  'The Constitution strikes a delicate balance between rigidity (like USA) and flexibility (like UK): some provisions require only a simple majority outside Art. 368, while others require special majorities or state ratifications under Art. 368.',
  {'A': 'Simple majority applies only to limited provisions.', 'B': 'Correct. Combines simple, special, and state ratification amendment procedures.', 'C': 'India has no referendum provision.', 'D': 'Supreme Court reviews amendments only on challenge.'},
  'Medium', 'Article 368 Synthesis', 'Explain balance between flexibility and rigidity.')

q('mcq-const-02-028', 'ch-02', 'top-const-02-03',
  'Which case established that "Secularism" is an essential part of the Basic Structure of the Indian Constitution?',
  ['Kesavananda Bharati v. State of Kerala (1973)', 'S.R. Bommai v. Union of India (1994)', 'Minerva Mills v. Union of India (1980)', 'Indira Nehru Gandhi v. Raj Narain (1975)'],
  1,
  'While Kesavananda recognized secular character, the 9-Judge Bench in S.R. Bommai v. Union of India (1994) unequivocally cemented Secularism as an inviolable Basic Feature of the Constitution.',
  {'A': 'Kesavananda noted secular character among basic elements.', 'B': 'Correct. S.R. Bommai definitively ruled secularism is basic structure.', 'C': 'Minerva Mills emphasized balance between rights and directives.', 'D': 'Indira Gandhi struck down election immunity.'},
  'Medium', 'Secularism Jurisprudence', 'Identify definitive secularism basic structure authority.')

q('mcq-const-02-029', 'ch-02', 'top-const-02-03',
  'The concept of an "Integrated Judiciary" in India implies:',
  ['A single system of courts enforcing both Central and State laws throughout the country', 'Judges are appointed by the executive without consultation', 'Judiciary is subordinate to the Parliament', 'Courts have no power of judicial review'],
  0,
  'Unlike the United States (where federal courts enforce federal laws and state courts enforce state laws), India has an integrated hierarchy of courts where the Supreme Court at the apex and High Courts below it enforce both Union and State laws.',
  {'A': 'Correct. Single integrated system enforcing both Central and State laws.', 'B': 'Judges are appointed through collegium.', 'C': 'Judiciary is independent, not subordinate.', 'D': 'Judicial review is an active power.'},
  'Medium', 'Judicial Hierarchy Concept', 'Explain meaning of integrated judiciary in India.')

q('mcq-const-02-030', 'ch-02', 'top-const-02-03',
  'Who described the Preamble as the "Horoscope of our Sovereign, Democratic Republic"?',
  ['Dr. B.R. Ambedkar', 'Dr. K.M. Munshi', 'Pandit Thakur Das Bhargava', 'N.A. Palkhivala'],
  1,
  'Dr. K.M. Munshi, a member of the Drafting Committee, described the Preamble as the "Horoscope of our Sovereign, Democratic Republic". N.A. Palkhivala termed it the "Identity Card of the Constitution".',
  {'A': 'Dr. Ambedkar drafted the core articles.', 'B': 'Correct. Dr. K.M. Munshi termed it the political horoscope.', 'C': 'Thakur Das Bhargava called it the soul and jewel of the Constitution.', 'D': 'N.A. Palkhivala called it the identity card.'},
  'Medium', 'Preamble Epigrams', 'Recall author of horoscope description.')

# ------------------------------------------------------------------------------
# CHAPTER 3: THE PREAMBLE (25 MCQs)
# ------------------------------------------------------------------------------
# Topic 1: Text, Philosophy & Ideals (12 MCQs)
q('mcq-const-03-001', 'ch-03', 'top-const-03-01',
  'What is the exact chronological sequence of the opening words describing India\'s status in the Preamble today?',
  ['Sovereign, Democratic, Republic, Socialist, Secular', 'Sovereign, Socialist, Secular, Democratic, Republic', 'Socialist, Secular, Sovereign, Democratic, Republic', 'Sovereign, Secular, Socialist, Democratic, Republic'],
  1,
  'The opening operative declaration reads: "SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC". ("Socialist" and "Secular" were inserted between Sovereign and Democratic by 42nd Amendment).',
  {'A': 'Incorrect order.', 'B': 'Correct. Sovereign, Socialist, Secular, Democratic, Republic (SO-SO-SE-DE-RE).', 'C': 'Incorrect order.', 'D': 'Incorrect order (Secular precedes Socialist is false).'},
  'Easy', 'Preamble Opening Phrase', 'Recall exact text sequence of Preamble.')

q('mcq-const-03-002', 'ch-03', 'top-const-03-01',
  'Which three words were added to the Preamble by the 42nd Constitutional Amendment Act, 1976?',
  ['Socialist, Secular, Integrity', 'Socialist, Democratic, Republic', 'Liberty, Equality, Fraternity', 'Sovereign, Secular, Unity'],
  0,
  'The 42nd Amendment Act, 1976 amended the Preamble to add "Socialist" and "Secular" to the description of the Republic, and changed "unity of the Nation" to "unity and integrity of the Nation".',
  {'A': 'Correct. Socialist, Secular, and Integrity were added.', 'B': 'Democratic and Republic were part of original 1950 text.', 'C': 'Liberty, Equality, Fraternity were in original 1950 text.', 'D': 'Sovereign and Unity were in original 1950 text.'},
  'Easy', '42nd Amendment Act, 1976', 'Identify words added by 42nd Amendment.')

q('mcq-const-03-003', 'ch-03', 'top-const-03-01',
  'How many types of "Justice" are secured to all citizens by the Preamble?',
  ['Two: Legal and Political', 'Three: Social, Economic, and Political', 'Four: Civil, Criminal, Social, and Moral', 'Single universal justice'],
  1,
  'The Preamble secures "JUSTICE, social, economic and political", in that precise order, reflecting the social and economic goals of the welfare state inspired by the 1917 Russian Revolution.',
  {'A': 'Legal justice is not mentioned explicitly in the Preamble.', 'B': 'Correct. Three types: Social, Economic, and Political.', 'C': 'Four types is incorrect.', 'D': 'Single is incorrect.'},
  'Easy', 'Preamble Justice Dimensions', 'Recall three dimensions of Justice in Preamble.')

q('mcq-const-03-004', 'ch-03', 'top-const-03-01',
  'What are the five dimensions of "Liberty" guaranteed in the Preamble?',
  ['Speech, Expression, Belief, Trade, Commerce', 'Thought, Expression, Belief, Faith, and Worship', 'Life, Liberty, Property, Speech, Religion', 'Movement, Residence, Profession, Thought, Assembly'],
  1,
  'The Preamble explicitly guarantees "LIBERTY of thought, expression, belief, faith and worship".',
  {'A': 'Trade and commerce are Article 19(1)(g)/Part XIII rights.', 'B': 'Correct. Thought, Expression, Belief, Faith, and Worship.', 'C': 'Life and property are substantive rights.', 'D': 'Movement and residence are Art. 19 freedoms.'},
  'Easy', 'Preamble Liberty Dimensions', 'Recall five dimensions of Liberty in Preamble.')

q('mcq-const-03-005', 'ch-03', 'top-const-03-01',
  'What two forms of "Equality" are secured to all citizens in the Preamble?',
  ['Equality of income and property', 'Equality of status and of opportunity', 'Equality of voting and taxation', 'Equality of religion and race'],
  1,
  'The Preamble secures "EQUALITY of status and of opportunity; and to promote among them all".',
  {'A': 'Income equality is a DPSP ideal (Art. 39), not in Preamble text.', 'B': 'Correct. Status and of opportunity.', 'C': 'Voting equality is Art. 326.', 'D': 'Religion/race equality is Art. 15.'},
  'Easy', 'Preamble Equality Dimensions', 'Recall two forms of Equality in Preamble.')

q('mcq-const-03-006', 'ch-03', 'top-const-03-01',
  'What is the date of adoption of the Constitution mentioned in the Preamble?',
  ['26th day of January, 1950', '26th day of November, 1949', '15th day of August, 1947', '9th day of December, 1946'],
  1,
  'The enacting clause concludes: "IN OUR CONSTITUENT ASSEMBLY this twenty-sixth day of November, 1949, do HEREBY ADOPT, ENACT AND GIVE TO OURSELVES THIS CONSTITUTION".',
  {'A': '26th January 1950 was the date of commencement.', 'B': 'Correct. 26th November 1949 was date of adoption.', 'C': '15th August 1947 was independence.', 'D': '9th December 1946 was first assembly meeting.'},
  'Easy', 'Preamble Enacting Clause', 'Distinguish adoption date from commencement date.')

q('mcq-const-03-007', 'ch-03', 'top-const-03-01',
  'From where does the Constitution of India derive its ultimate sovereign authority?',
  ['The Parliament of India', 'The President of India', 'The People of India', 'The Supreme Court of India'],
  2,
  'The opening words "WE, THE PEOPLE OF INDIA... ADOPT, ENACT AND GIVE TO OURSELVES THIS CONSTITUTION" signify that ultimate political sovereignty resides in the people of India.',
  {'A': 'Parliament is a creature of the Constitution.', 'B': 'President is constitutional executive head.', 'C': 'Correct. The People of India.', 'D': 'Supreme Court is creature and guardian of Constitution.'},
  'Easy', 'Popular Sovereignty Doctrine', 'Identify source of constitutional authority.')

q('mcq-const-03-008', 'ch-03', 'top-const-03-01',
  'What form of socialism does the Indian Constitution adopt as clarified in D.S. Nakara v. Union of India?',
  ['Marxist state socialism requiring total nationalization', 'Democratic socialism aiming to end poverty, ignorance, disease, and inequality of opportunity', 'Communist dictatorship of the proletariat', 'Syndicalist guild socialism'],
  1,
  'In D.S. Nakara v. UOI (1983), the Supreme Court held that Indian socialism is "Democratic Socialism"—a blend of Marxism and Gandhism leaning heavily towards Gandhian socialism, aiming to eliminate poverty and inequality without abolishing private enterprise.',
  {'A': 'India does not follow Marxist total nationalization.', 'B': 'Correct. Democratic socialism with Gandhian blend.', 'C': 'Communist dictatorship is antithetical to democracy.', 'D': 'Syndicalism is not adopted.'},
  'Medium', 'D.S. Nakara v. Union of India (1983)', 'Define Indian democratic socialism.')

q('mcq-const-03-009', 'ch-03', 'top-const-03-01',
  'In which case did the Supreme Court observe that "Secularism in the Indian Constitution means that all religions receive equal respect and protection from the State (Sarva Dharma Sambhava)"?',
  ['St. Xavier\'s College v. State of Gujarat (1974)', 'S.R. Bommai v. Union of India (1994)', 'Indira Nehru Gandhi v. Raj Narain (1975)', 'Aruna Roy v. Union of India (2002)'],
  0,
  'In St. Xavier\'s College (1974), the Supreme Court explained that secularism in India is neither anti-God nor pro-God; it treats devout, agnostic, and atheist alike and accords equal freedom and respect to all faiths (positive secularism).',
  {'A': 'Correct. St. Xavier\'s College articulated positive secularism.', 'B': 'Bommai cemented secularism as basic structure.', 'C': 'Indira Gandhi struck down election immunity.', 'D': 'Aruna Roy upheld study of comparative religions.'},
  'Hard', 'Positive Secularism Jurisprudence', 'Analyze positive secularism in Indian constitutional law.')

q('mcq-const-03-010', 'ch-03', 'top-const-03-01',
  'Who called the Preamble the "Key to the Constitution" and "Jewel set in the Constitution"?',
  ['Pandit Thakur Das Bhargava', 'N.A. Palkhivala', 'Justice M. Hidayatullah', 'Sir Ernest Barker'],
  0,
  'Pandit Thakur Das Bhargava declared: "The Preamble is the most precious part of the Constitution. It is the soul of the Constitution. It is a key to the Constitution. It is a proper yardstick with which one can measure the worth of the Constitution."',
  {'A': 'Correct. Pandit Thakur Das Bhargava.', 'B': 'Palkhivala called it identity card.', 'C': 'Hidayatullah compared it to US Declaration of Independence.', 'D': 'Barker praised it as a key principle of social and political theory.'},
  'Medium', 'Preamble Appraisal Quotes', 'Attribute famous Preamble praises.')

q('mcq-const-03-011', 'ch-03', 'top-const-03-01',
  'English political theorist Sir Ernest Barker was so impressed by the Preamble of the Indian Constitution that he quoted it at the opening of his book:',
  ['Principles of Social and Political Theory (1951)', 'The Law of the Constitution', 'Representative Government', 'Modern Democracies'],
  0,
  'Sir Ernest Barker quoted the Preamble of the Indian Constitution on the opening page of his celebrated treatise "Principles of Social and Political Theory" (1951), noting that it states in condensed form the essential principles of modern politics.',
  {'A': 'Correct. Principles of Social and Political Theory (1951).', 'B': 'A.V. Dicey wrote Law of the Constitution.', 'C': 'J.S. Mill wrote Representative Government.', 'D': 'Lord Bryce wrote Modern Democracies.'},
  'Hard', 'Barker\'s Tribute', 'Recall international scholarly acclaim of Preamble.')

q('mcq-const-03-012', 'ch-03', 'top-const-03-01',
  'What does the term "Republic" signify in the Indian Preamble?',
  ['The executive head of the state is hereditary', 'The head of the state (President) is always elected, directly or indirectly, for a fixed term, and all public offices are open to every citizen without discrimination', 'Parliament has unlimited sovereign powers', 'The judiciary is supreme over executive'],
  1,
  'A Republic denotes a political system where the head of state is not hereditary (like a monarchy) but elected by the people for a fixed period, and where political sovereignty is vested in the people without any privileged class.',
  {'A': 'Hereditary head is a Monarchy (e.g. UK).', 'B': 'Correct. Elected head of state and open public offices.', 'C': 'Parliamentary sovereignty is British, not republican per se.', 'D': 'Judicial review is a separate constitutional check.'},
  'Easy', 'Republican Form of Government', 'Define Republic in constitutional context.')

# Topic 2: Status & Amendability (13 MCQs)
q('mcq-const-03-013', 'ch-03', 'top-const-03-02',
  'In which advisory reference did the Supreme Court hold that the Preamble is "NOT a part of the Constitution"?',
  ['In re Berubari Union (1960)', 'In re Kerala Education Bill (1958)', 'In re Delhi Laws Act (1951)', 'In re Special Courts Bill (1978)'],
  0,
  'In In re Berubari Union (1960), an 8-Judge Bench held that the Preamble is a key to the minds of the makers, but it is NOT part of the Constitution and cannot be regarded as a source of substantive powers.',
  {'A': 'Correct. In re Berubari Union (1960) held Preamble is not part of Constitution.', 'B': 'Kerala Education Bill dealt with minority rights.', 'C': 'Delhi Laws Act dealt with delegated legislation.', 'D': 'Special Courts Bill dealt with trial of emergency offenses.'},
  'Easy', 'In re Berubari Union (1960) 3 SCR 250', 'Recall Berubari holding on Preamble status.')

q('mcq-const-03-014', 'ch-03', 'top-const-03-02',
  'The ruling in Berubari Union (1960) that the Preamble is not part of the Constitution was expressly overruled in which landmark case?',
  ['Golaknath v. State of Punjab (1967)', 'Kesavananda Bharati v. State of Kerala (1973)', 'Minerva Mills v. Union of India (1980)', 'Maneka Gandhi v. Union of India (1978)'],
  1,
  'In Kesavananda Bharati (1973), the majority of the 13-Judge Bench expressly overruled Berubari Union and held that the Preamble IS an integral part of the Constitution and can be amended under Article 368 without destroying its Basic Structure.',
  {'A': 'Golaknath dealt with amending fundamental rights.', 'B': 'Correct. Kesavananda Bharati (1973) overruled Berubari.', 'C': 'Minerva Mills reaffirmed basic structure balance.', 'D': 'Maneka Gandhi expanded Article 21.'},
  'Easy', 'Kesavananda Bharati (1973) 4 SCC 225', 'Recall overruling of Berubari.')

q('mcq-const-03-015', 'ch-03', 'top-const-03-02',
  'In which 1995 judgment did the Supreme Court reaffirm that "the Preamble is an integral part of the Constitution"?',
  ['LIC of India v. Consumer Education & Research Centre', 'S.P. Gupta v. Union of India', 'Indra Sawhney v. Union of India', 'Mohini Jain v. State of Karnataka'],
  0,
  'In LIC of India v. Consumer Education & Research Centre (1995), the Supreme Court once again unequivocally held that the Preamble is an integral part of the Constitution.',
  {'A': 'Correct. LIC of India (1995) reaffirmed Preamble is integral part.', 'B': 'S.P. Gupta was First Judges Case on appointments.', 'C': 'Indra Sawhney was Mandal Commission case on reservations.', 'D': 'Mohini Jain was capitation fee case.'},
  'Medium', 'LIC of India v. CERC (1995) 5 SCC 482', 'Reaffirm Preamble status in LIC case.')

q('mcq-const-03-016', 'ch-03', 'top-const-03-02',
  'Is the Preamble directly enforceable in a court of law (justiciable)?',
  ['Yes, under Article 32', 'Yes, under Article 226', 'No, the Preamble is non-justiciable and cannot be enforced directly in courts', 'Yes, but only against the Central Government'],
  2,
  'The Preamble is non-justiciable: its provisions are not enforceable in courts of law, meaning no writ of mandamus can be issued solely to enforce a declaration in the Preamble without a specific constitutional or statutory provision.',
  {'A': 'Article 32 enforces Part III Fundamental Rights, not Preamble per se.', 'B': 'Article 226 cannot enforce Preamble standalone.', 'C': 'Correct. Preamble is non-justiciable and unenforceable.', 'D': 'Cannot be enforced against any government.'},
  'Medium', 'Preamble Justiciability Jurisprudence', 'Analyze non-justiciable nature of Preamble.')

q('mcq-const-03-017', 'ch-03', 'top-const-03-02',
  'Can the Preamble to the Constitution of India be amended under Article 368?',
  ['No, it can never be amended under any circumstances', 'Yes, but the amendment must not alter or damage the Basic Structure of the Constitution', 'Yes, Parliament has unlimited power to delete any word', 'Only with the ratification of all State Legislatures'],
  1,
  'As held in Kesavananda Bharati (1973), the Preamble can be amended under Article 368 like any other part of the Constitution, subject to the limitation that its Basic Features (such as secularism, democracy, republic) cannot be destroyed.',
  {'A': 'It was already amended by 42nd Amendment in 1976.', 'B': 'Correct. Amendable subject to the Basic Structure limitation.', 'C': 'Amending power is limited, not absolute.', 'D': 'State ratification is not needed unless proviso provisions are touched.'},
  'Easy', 'Kesavananda Bharati (1973) 4 SCC 225', 'Master amendability of Preamble.')

q('mcq-const-03-018', 'ch-03', 'top-const-03-02',
  'How many times has the Preamble to the Constitution of India been amended so far?',
  ['Never', 'Once', 'Twice', 'Three times'],
  1,
  'The Preamble has been amended only ONCE in constitutional history, by the 42nd Constitutional Amendment Act, 1976, which added "Socialist", "Secular", and "Integrity".',
  {'A': 'It was amended in 1976.', 'B': 'Correct. Exactly once (by 42nd Amendment, 1976).', 'C': 'Twice is incorrect.', 'D': 'Three times is incorrect.'},
  'Easy', 'Preamble Amendment History', 'Recall frequency of Preamble amendments.')

q('mcq-const-03-019', 'ch-03', 'top-const-03-02',
  'What is the primary legal utility of the Preamble in constitutional adjudication?',
  ['It confers independent substantive legislative powers on Parliament', 'It acts as an interpretive compass when constitutional provisions are ambiguous or capable of two meanings', 'It operates as an overriding limitation on fundamental rights', 'It acts as a substitute for Directive Principles'],
  1,
  'The Preamble is an interpretive aid: where the text of an Article is clear, it prevails; but where constitutional words are ambiguous or capable of multiple constructions, that interpretation which harmonizes with the Preamble must be adopted.',
  {'A': 'Preamble is neither a source of power nor a source of prohibition.', 'B': 'Correct. Serves as an interpretive aid for ambiguous provisions.', 'C': 'Cannot override explicit fundamental rights.', 'D': 'Does not replace DPSP.'},
  'Medium', 'Interpretive Role of Preamble', 'Explain interpretive utility of Preamble.')

q('mcq-const-03-020', 'ch-03', 'top-const-03-02',
  'Which Justice in Kesavananda Bharati observed that "the Preamble was enacted with the same solemnity as the rest of the Constitution"?',
  ['Justice H.R. Khanna', 'Chief Justice S.M. Sikri', 'Justice K.S. Hegde', 'Justice A.N. Ray'],
  1,
  'Chief Justice S.M. Sikri observed that unlike the American or other Constitutions, the Preamble of the Indian Constitution was voted upon and enacted by the Constituent Assembly with the motion "that the Preamble stand part of the Constitution", proving it is part of the Constitution.',
  {'A': 'Khanna focused on basic structure doctrine.', 'B': 'Correct. CJI S.M. Sikri noted the assembly voting history.', 'C': 'Hegde concurred on basic structure.', 'D': 'Ray dissented in favor of unlimited amending power.'},
  'Hard', 'Kesavananda Bharati (1973) 4 SCC 225, para 100', 'Attribute assembly enactment observation.')

q('mcq-const-03-021', 'ch-03', 'top-const-03-02',
  'Can a law enacted by Parliament be declared unconstitutional solely on the ground that it violates the Preamble?',
  ['Yes, because Preamble is the supreme law', 'No, because the Preamble is not an enforceable source of substantive power or limitation in itself', 'Yes, if challenged by a PIL', 'Yes, by a 5-Judge Constitution Bench only'],
  1,
  'A statute cannot be declared void solely for violating the Preamble; it must violate an express provision of the Constitution or its Basic Structure (which draws from the Preamble).',
  {'A': 'Preamble is not an independent substantive ground of invalidity.', 'B': 'Correct. Preamble is not an independent enforceable source.', 'C': 'PIL cannot bypass justiciability requirement.', 'D': 'Bench size does not change substantive rule.'},
  'Medium', 'Substantive Limitation Doctrine', 'Understand why Preamble cannot be sole ground of invalidity.')

q('mcq-const-03-022', 'ch-03', 'top-const-03-02',
  'What was the original description of India in the Preamble before the 42nd Amendment, 1976?',
  ['Sovereign Democratic Republic', 'Sovereign Socialist Republic', 'Democratic Secular Republic', 'Union of Sovereign States'],
  0,
  'Prior to the 42nd Amendment Act 1976, the Preamble declared India to be a "SOVEREIGN DEMOCRATIC REPUBLIC". The words "Socialist" and "Secular" were inserted in 1976.',
  {'A': 'Correct. Original text was "Sovereign Democratic Republic".', 'B': 'Socialist was added in 1976.', 'C': 'Secular was added in 1976.', 'D': 'Union of States is Article 1, not Preamble.'},
  'Easy', 'Pre-1976 Preamble Text', 'Recall original 1950 Preamble text.')

q('mcq-const-03-023', 'ch-03', 'top-const-03-02',
  'In Kesavananda Bharati, which test was laid down to determine whether a constitutional amendment violates the Preamble?',
  ['The legislative motive test', 'The basic structure test (whether the identity or essential features reflected in the Preamble are damaged)', 'The proportionality test', 'The strict scrutiny test'],
  1,
  'The Supreme Court laid down that an amendment to the Preamble or under Article 368 is valid as long as it does not destroy the essential identity or Basic Structure of the Constitution as outlined in the Preamble.',
  {'A': 'Legislative motive is irrelevant to constitutional validity.', 'B': 'Correct. Basic Structure test determines whether essential identity is damaged.', 'C': 'Proportionality applies to fundamental rights restrictions.', 'D': 'Strict scrutiny applies to discrimination.'},
  'Medium', 'Basic Structure Touchstone', 'Connect Preamble to Basic Structure test.')

q('mcq-const-03-024', 'ch-03', 'top-const-03-02',
  'Which of the following statements regarding the Preamble is INCORRECT?',
  ['The Preamble is a source of power to the legislature', 'The Preamble is a part of the Constitution', 'The Preamble was adopted after the rest of the Constitution was already enacted', 'The Preamble can be amended under Article 368'],
  0,
  'The statement that "The Preamble is a source of power to the legislature" is INCORRECT. The Preamble is NEITHER a source of power to legislature NOR a source of prohibition upon the powers of legislature.',
  {'A': 'Correct (this statement is false, hence the correct answer). Preamble is NOT a source of power.', 'B': 'True statement (Kesavananda Bharati).', 'C': 'True statement (voted upon at the end of the drafting to ensure conformity).', 'D': 'True statement (amendable under Art. 368).'},
  'Medium', 'Preamble Characteristics', 'Identify false statement regarding Preamble.')

q('mcq-const-03-025', 'ch-03', 'top-const-03-02',
  'Why did the Constituent Assembly enact the Preamble at the very end of its proceedings on 17th October 1949?',
  ['Because it was forgotten earlier', 'To ensure that the Preamble conformed with and reflected the provisions of the Constitution as finally settled', 'Because British assent was pending', 'Due to disagreement on adult suffrage'],
  1,
  'The President of the Constituent Assembly postponed the consideration of the Preamble until all other Articles had been adopted, to ensure that the Preamble was in perfect harmony with the text of the Constitution as finalized.',
  {'A': 'It was carefully planned, not forgotten.', 'B': 'Correct. To ensure total conformity with the finalized constitutional text.', 'C': 'British assent was irrelevant post-Independence.', 'D': 'Universal adult franchise was agreed early.'},
  'Medium', 'Constituent Assembly Procedure', 'Understand why Preamble was adopted last.')

print(f"Batch 1 complete with {len(BATCH1)} MCQs.")
''')

print("Batch 1 Ch 2 & Ch 3 appended successfully.")
