/**
 * Judicial Learning Academy — Indian Constitution Topics Registry
 * 45 Comprehensive Topics mapped across the 15 Chapters.
 */
(function() {
  'use strict';

  const CONSTITUTION_TOPICS = [
    // CHAPTER 1: HISTORICAL BACKGROUND (3 topics)
    {
      id: 'top-const-01-01',
      chapterId: 'ch-01',
      number: 1,
      title: 'Company Rule & Early Constitutional Enactments (1773–1853)',
      subtitle: 'From Regulating Act 1773 to Charter Act 1853',
      articleRef: 'Historical Charters',
      description: 'The foundation of central administration in India: Regulating Act 1773 (Governor-General of Bengal, Supreme Court at Calcutta), Pitt’s India Act 1784 (Board of Control), and the Charter Acts of 1793, 1813, 1833, and 1853.',
      mcqsCount: 10,
      pyqsCount: 2,
      estimatedMinutes: 20
    },
    {
      id: 'top-const-01-02',
      chapterId: 'ch-01',
      number: 2,
      title: 'Crown Rule & Representative Councils (1858–1919)',
      subtitle: 'Government of India Act 1858, Indian Councils Acts & Montagu-Chelmsford Reforms',
      articleRef: 'Crown Statutes',
      description: 'Transfer of power to the British Crown under Act of 1858 (Secretary of State for India), Indian Councils Acts of 1861 and 1892, Morley-Minto Reforms 1909 (communal electorates), and Government of India Act 1919 (Dyarchy in provinces).',
      mcqsCount: 10,
      pyqsCount: 3,
      estimatedMinutes: 25
    },
    {
      id: 'top-const-01-03',
      chapterId: 'ch-01',
      number: 3,
      title: 'The Blueprint: GoI Act 1935 & Indian Independence Act 1947',
      subtitle: 'All-India Federation, Provincial Autonomy & Transfer of Power',
      articleRef: 'Act of 1935 & 1947',
      description: 'Government of India Act 1935 (Provincial Autonomy, Federal Court, Three Legislative Lists, Bicameralism), Mountbatten Plan, and Indian Independence Act 1947 creating two sovereign dominions.',
      mcqsCount: 10,
      pyqsCount: 3,
      estimatedMinutes: 25
    },

    // CHAPTER 2: MAKING OF THE CONSTITUTION & SALIENT FEATURES (3 topics)
    {
      id: 'top-const-02-01',
      chapterId: 'ch-02',
      number: 1,
      title: 'Constituent Assembly: Genesis, Committees & Enactment',
      subtitle: 'Cabinet Mission Plan, Drafting Committee & Timeline of Adoption',
      articleRef: 'Constituent Assembly Debates',
      description: 'Formation under Cabinet Mission Plan 1946, first meeting on Dec 9 1946, Objective Resolution by Nehru, the 8 Major Committees (Drafting Committee headed by Dr. B.R. Ambedkar), adoption on Nov 26 1949, and commencement on Jan 26 1950.',
      mcqsCount: 10,
      pyqsCount: 5,
      estimatedMinutes: 25
    },
    {
      id: 'top-const-02-02',
      chapterId: 'ch-02',
      number: 2,
      title: 'Global Sources of the Indian Constitution',
      subtitle: 'Borrowed Features from UK, USA, Ireland, Canada, Australia, etc.',
      articleRef: 'Comparative Jurisprudence',
      description: 'Structural parentage: UK (Parliamentary system, Rule of law, Single citizenship, Writs), USA (Fundamental Rights, Judicial review, Preamble, Impeachment), Ireland (DPSP, Rajya Sabha nominations), Canada (Federation with strong centre, Residuary powers), Australia (Concurrent list, Joint sitting).',
      mcqsCount: 10,
      pyqsCount: 4,
      estimatedMinutes: 20
    },
    {
      id: 'top-const-02-03',
      chapterId: 'ch-02',
      number: 3,
      title: 'Salient Structural Features of the Indian Constitution',
      subtitle: 'Quasi-Federal Nature, Blend of Rigidity & Flexibility, Integrated Judiciary',
      articleRef: 'Constitutional Hallmarks',
      description: 'Longest written constitution in the world, blend of rigidity and flexibility, federal system with unitary bias (K.C. Wheare’s "quasi-federal"), parliamentary form of government, synthesis of Parliamentary Sovereignty and Judicial Supremacy, integrated and independent judiciary.',
      mcqsCount: 10,
      pyqsCount: 3,
      estimatedMinutes: 20
    },

    // CHAPTER 3: THE PREAMBLE (2 topics)
    {
      id: 'top-const-03-01',
      chapterId: 'ch-03',
      number: 1,
      title: 'Text, Ideals & Grand Expressions of the Preamble',
      subtitle: 'Sovereign, Socialist, Secular, Democratic, Republic, Justice, Liberty, Equality, Fraternity',
      articleRef: 'Preamble',
      description: 'Detailed analysis of the opening words "We, the People of India", substantive meanings of Sovereign, Socialist, Secular (added by 42nd Amendment 1976), Democratic, and Republic; the four solemn objectives: Justice (Social, Economic, Political), Liberty, Equality, and Fraternity.',
      mcqsCount: 12,
      pyqsCount: 5,
      estimatedMinutes: 20
    },
    {
      id: 'top-const-03-02',
      chapterId: 'ch-03',
      number: 2,
      title: 'Legal Status, Enforceability & Amendability of the Preamble',
      subtitle: 'Berubari Union (1960), Kesavananda Bharati (1973) & LIC of India (1995)',
      articleRef: 'Preamble Jurisprudence',
      description: 'Whether Preamble is part of Constitution: Re Berubari Union 1960 (not part) overruled by 13-Judge Bench in Kesavananda Bharati 1973 (is part of the Constitution and amendable under Art. 368 without altering Basic Structure); non-justiciable character.',
      mcqsCount: 13,
      pyqsCount: 5,
      estimatedMinutes: 25
    },

    // CHAPTER 4: THE UNION AND ITS TERRITORY (2 topics)
    {
      id: 'top-const-04-01',
      chapterId: 'ch-04',
      number: 1,
      title: 'Territory of the Union & Admission of States (Articles 1–2)',
      subtitle: 'India, that is Bharat, shall be a Union of States',
      articleRef: 'Articles 1 and 2',
      description: 'Article 1: "Union of States" rather than "Federation of States" (indestructible union of destructible states); components of Indian territory; Article 2: Parliament’s power to admit into the Union, or establish, new States on terms it thinks fit.',
      mcqsCount: 12,
      pyqsCount: 3,
      estimatedMinutes: 20
    },
    {
      id: 'top-const-04-02',
      chapterId: 'ch-04',
      number: 2,
      title: 'Reorganisation of States & Cession Jurisprudence (Articles 3–4)',
      subtitle: 'Formation of New States, Boundary Alterations & Berubari Principle',
      articleRef: 'Articles 3 and 4',
      description: 'Article 3 procedure: Presidential recommendation, reference to State Legislature (non-binding views), simple parliamentary majority; Article 4: Laws under Arts. 2 & 3 not constitutional amendments under Art. 368; Cession of Indian territory requires Art. 368 amendment (Re Berubari Union 1960).',
      mcqsCount: 13,
      pyqsCount: 3,
      estimatedMinutes: 25
    },

    // CHAPTER 5: CITIZENSHIP (2 topics)
    {
      id: 'top-const-05-01',
      chapterId: 'ch-05',
      number: 1,
      title: 'Constitutional Citizenship at Commencement (Articles 5–8)',
      subtitle: 'Domicile, Migration from Pakistan & Overseas Origin',
      articleRef: 'Articles 5, 6, 7, 8',
      description: 'Article 5: Citizenship by domicile (birth, descent, or 5-year residence); Article 6: Citizenship of persons who migrated from Pakistan; Article 7: Migrants to Pakistan who returned under permit for resettlement; Article 8: Persons of Indian origin residing outside India.',
      mcqsCount: 12,
      pyqsCount: 2,
      estimatedMinutes: 20
    },
    {
      id: 'top-const-05-02',
      chapterId: 'ch-05',
      number: 2,
      title: 'Single Citizenship, Termination & Statutory Control (Articles 9–11)',
      subtitle: 'Prohibition of Dual Citizenship & The Citizenship Act, 1955 Framework',
      articleRef: 'Articles 9, 10, 11',
      description: 'Article 9: Voluntary acquisition of foreign citizenship causes automatic loss of Indian citizenship (Single Citizenship principle); Article 10: Continuance of citizenship rights; Article 11: Absolute parliamentary plenary power to regulate citizenship by law (Citizenship Act 1955: Birth, Descent, Registration, Naturalisation, Incorporation of territory).',
      mcqsCount: 13,
      pyqsCount: 3,
      estimatedMinutes: 25
    },

    // CHAPTER 6: FUNDAMENTAL RIGHTS (6 topics)
    {
      id: 'top-const-06-01',
      chapterId: 'ch-06',
      number: 1,
      title: 'Concept of Fundamental Rights, Definition of "State" & Judicial Review',
      subtitle: 'Articles 12 & 13: The Shield of Part III, Severability & Doctrine of Eclipse',
      articleRef: 'Articles 12 and 13',
      description: 'Definition of "State" under Article 12 (Ajay Hasia, Pradeep Kumar Biswas tests for instrumentalities of State; whether Judiciary is State); Article 13: Laws inconsistent with or in derogation of FRs; Pre-constitutional laws & Doctrine of Eclipse (Bhikaji Narain); Post-constitutional laws & Doctrine of Severability (A.K. Gopalan); Doctrine of Waiver (Basheshar Nath).',
      mcqsCount: 10,
      pyqsCount: 6,
      estimatedMinutes: 30
    },
    {
      id: 'top-const-06-02',
      chapterId: 'ch-06',
      number: 2,
      title: 'Right to Equality (Articles 14–18)',
      subtitle: 'Equality Before Law, Non-Discrimination, Affirmative Action & Abolition of Untouchability',
      articleRef: 'Articles 14, 15, 16, 17, 18',
      description: 'Article 14: Equality before law (UK) vs Equal protection of laws (USA); Reasonable classification test (State of W.B. v. Anwar Ali Sarkar); New Doctrine of Arbitrariness (E.P. Royappa v. State of T.N.); Article 15: Non-discrimination on 5 grounds, protective discrimination for women/children/SEBCs/EWS; Article 16: Equality of opportunity in public employment (Indra Sawhney 1992 50% cap, creamy layer); Article 17: Abolition of Untouchability (absolute right); Article 18: Abolition of titles.',
      mcqsCount: 10,
      pyqsCount: 8,
      estimatedMinutes: 35
    },
    {
      id: 'top-const-06-03',
      chapterId: 'ch-06',
      number: 3,
      title: 'Right to Freedom & Protection in Respect of Conviction (Articles 19–20)',
      subtitle: 'The Six Democratic Freedoms, Reasonable Restrictions & Triple Protections of Art. 20',
      articleRef: 'Articles 19 and 20',
      description: 'Article 19(1)(a)-(g): Speech, Assembly, Association, Movement, Residence, Profession; Reasonable restrictions under clauses (2) to (6) on specific exhaustive grounds; Article 20: Three absolute procedural protections: 20(1) Protection against ex-post facto laws, 20(2) Protection against Double Jeopardy (Maqbool Hussain), 20(3) Protection against Self-Incrimination (Nandini Satpathy, Selvi v. State of Karnataka).',
      mcqsCount: 10,
      pyqsCount: 6,
      estimatedMinutes: 30
    },
    {
      id: 'top-const-06-04',
      chapterId: 'ch-06',
      number: 4,
      title: 'Right to Life, Personal Liberty & Education (Articles 21, 21A & 22)',
      subtitle: 'Evolution from A.K. Gopalan to Maneka Gandhi, Right to Privacy & Preventive Detention',
      articleRef: 'Articles 21, 21A, 22',
      description: 'Article 21: "Procedure established by law" transformed to substantive "due process" in Maneka Gandhi (1978); Golden Triangle (Arts. 14, 19, 21); Derived rights under Art. 21: Right to Privacy (K.S. Puttaswamy 2017), clean environment (M.C. Mehta), speedy trial (Hussainara Khatoon), legal aid (M.H. Hoskot); Article 21A: Right to free & compulsory education (86th Amendment 2002); Article 22: Rights of arrested persons & safeguards in preventive detention.',
      mcqsCount: 10,
      pyqsCount: 6,
      estimatedMinutes: 35
    },
    {
      id: 'top-const-06-05',
      chapterId: 'ch-06',
      number: 5,
      title: 'Right Against Exploitation & Freedom of Religion (Articles 23–28)',
      subtitle: 'Prohibition of Human Trafficking, Begar, Child Labour & Secular Religious Freedoms',
      articleRef: 'Articles 23, 24, 25, 26, 27, 28',
      description: 'Articles 23 & 24: Prohibition of traffic in human beings, begar and forced labour (PUDR v. UOI); prohibition of child labour in hazardous employment; Articles 25–28: Freedom of conscience, profess, practice and propagate religion (Art. 25 subject to public order, morality, health and other FRs); Essential Religious Practices doctrine; Article 26: Freedom to manage religious affairs; Article 27: Freedom from taxation for promotion of religion; Article 28: Religious instruction in educational institutions.',
      mcqsCount: 10,
      pyqsCount: 3,
      estimatedMinutes: 25
    },
    {
      id: 'top-const-06-06',
      chapterId: 'ch-06',
      number: 6,
      title: 'Cultural & Educational Rights & Constitutional Remedies / Writs (Articles 29–32)',
      subtitle: 'Minority Rights & The Heart and Soul of the Constitution: The 5 High Prerogative Writs',
      articleRef: 'Articles 29, 30, 32',
      description: 'Article 29: Protection of language, script and culture of minorities; Article 30: Right of religious and linguistic minorities to establish and administer educational institutions (T.M.A. Pai, St. Stephen’s); Article 32: Constitutional remedies (Dr. Ambedkar’s "heart and soul"); The Five Prerogative Writs: Habeas Corpus, Mandamus, Prohibition, Certiorari, and Quo Warranto; Article 32 vs Article 226 scope.',
      mcqsCount: 15,
      pyqsCount: 8,
      estimatedMinutes: 35
    },

    // CHAPTER 7: DIRECTIVE PRINCIPLES OF STATE POLICY (3 topics)
    {
      id: 'top-const-07-01',
      chapterId: 'ch-07',
      number: 1,
      title: 'Genesis, Nature & Justiciability of DPSP (Articles 36–37)',
      subtitle: 'Fundamental in the Governance of the Country',
      articleRef: 'Articles 36 and 37',
      description: 'Origin borrowed from the 1937 Constitution of Ireland; Article 36 adopts definition of State from Art. 12; Article 37: DPSP are non-justiciable and unenforceable by any court, yet "fundamental in the governance of the country and it shall be the duty of the State to apply these principles in making laws".',
      mcqsCount: 10,
      pyqsCount: 4,
      estimatedMinutes: 20
    },
    {
      id: 'top-const-07-02',
      chapterId: 'ch-07',
      number: 2,
      title: 'Substantive Classification of Directives (Articles 38–51)',
      subtitle: 'Socialistic, Gandhian & Liberal-Intellectual Principles, Uniform Civil Code (Art. 44)',
      articleRef: 'Articles 38–51',
      description: 'Detailed analysis of all directives: Socialistic (Arts. 38, 39, 39A free legal aid, 41, 42, 43, 43A workers’ participation); Gandhian (Art. 40 village panchayats, Art. 43 cottage industries, Art. 43B co-operatives, Art. 46 SC/ST welfare, Art. 47 prohibition of intoxicating drinks, Art. 48 cow slaughter prohibition); Liberal-Intellectual (Art. 44 Uniform Civil Code, Art. 45 early childhood care, Art. 48A environmental protection, Art. 49 monuments, Art. 50 separation of judiciary from executive, Art. 51 international peace).',
      mcqsCount: 10,
      pyqsCount: 6,
      estimatedMinutes: 30
    },
    {
      id: 'top-const-07-03',
      chapterId: 'ch-07',
      number: 3,
      title: 'Harmonious Construction: Fundamental Rights vs DPSP',
      subtitle: 'From Champakam Dorairajan to Minerva Mills: The Two Wheels of the Chariot',
      articleRef: 'Inter-relationship Jurisprudence',
      description: 'Judicial evolution: State of Madras v. Champakam Dorairajan 1951 (FRs superior to DPSP); Kerala Education Bill 1957 (Doctrine of Harmonious Construction); 25th Amendment 1971 & Article 31C; Kesavananda Bharati 1973 (Art. 31C valid in part); 42nd Amendment 1976; Minerva Mills v. UOI 1980 (Balance between Part III and Part IV is basic structure: "The Indian Constitution is founded on the bedrock of the balance between Parts III and IV").',
      mcqsCount: 10,
      pyqsCount: 4,
      estimatedMinutes: 25
    },

    // CHAPTER 8: FUNDAMENTAL DUTIES (2 topics)
    {
      id: 'top-const-08-01',
      chapterId: 'ch-08',
      number: 1,
      title: 'Origin, Swaran Singh Committee & Enactment (Article 51A)',
      subtitle: '42nd Amendment Act 1976 & 86th Amendment Act 2002',
      articleRef: 'Article 51A',
      description: 'Part IVA added by 42nd Constitutional Amendment Act, 1976 on the recommendation of the Sardar Swaran Singh Committee; inspired by the USSR Constitution; initially 10 duties enacted; 11th duty added by the 86th Constitutional Amendment Act, 2002 (duty of parent/guardian to provide educational opportunities to children aged 6 to 14).',
      mcqsCount: 12,
      pyqsCount: 3,
      estimatedMinutes: 20
    },
    {
      id: 'top-const-08-02',
      chapterId: 'ch-08',
      number: 2,
      title: 'Analysis of the 11 Duties & Legal Enforcement',
      subtitle: 'Verma Committee on Fundamental Duties & Judicial Application',
      articleRef: 'Article 51A(a) to (k)',
      description: 'Substantive breakdown of clauses (a) to (k): Respect Constitution, National Flag & Anthem; cherish noble ideals of national struggle; uphold sovereignty, unity and integrity; defend the country; promote harmony & renounce practices derogatory to women; preserve composite culture; protect natural environment; develop scientific temper; safeguard public property; strive towards excellence; duty of parent/guardian; Justice J.S. Verma Committee recommendations; non-enforceability per se but usable to determine constitutional reasonableness of restrictions under Art. 19.',
      mcqsCount: 13,
      pyqsCount: 4,
      estimatedMinutes: 25
    },

    // CHAPTER 9: THE UNION EXECUTIVE (3 topics)
    {
      id: 'top-const-09-01',
      chapterId: 'ch-09',
      number: 1,
      title: 'The President & Vice-President: Office, Election & Impeachment',
      subtitle: 'Articles 52–71: Electoral College, Proportional Representation & Article 61 Procedure',
      articleRef: 'Articles 52 to 71',
      description: 'Article 52 (President of India); Article 53 (Executive power of Union vested in President); Electoral College under Art. 54 (elected members of both Houses of Parliament and elected members of Legislative Assemblies of States, including Delhi and Puducherry); Value of votes and single transferable vote system; Article 61 Impeachment procedure (1/4th members notice, 2/3rd majority of total membership of each house); Vice-President (Arts. 63–71) ex-officio Chairman of Rajya Sabha.',
      mcqsCount: 12,
      pyqsCount: 5,
      estimatedMinutes: 30
    },
    {
      id: 'top-const-09-02',
      chapterId: 'ch-09',
      number: 2,
      title: 'Executive Powers, Ordinance Making & Pardoning Powers',
      subtitle: 'Articles 72 & 123: Judicial Review of Pardons and Ordinances (D.C. Wadhwa, Kehar Singh)',
      articleRef: 'Articles 72 and 123',
      description: 'Article 72: Pardoning power of President (Pardon, Commutation, Remission, Respite, Reprieve) in all cases of court martial, death sentences, or Union laws; Kehar Singh v. UOI (1989), Epuru Sudhakar v. Govt of A.P. (2006 judicial review of pardon on limited grounds); Article 123: Ordinance making power when Parliament is not in session; immediate necessity; maximum lifespan of 6 weeks from reassembly of Parliament; D.C. Wadhwa v. State of Bihar (1987) & Krishna Kumar Singh v. State of Bihar (2017) against repromulgation.',
      mcqsCount: 11,
      pyqsCount: 5,
      estimatedMinutes: 30
    },
    {
      id: 'top-const-09-03',
      chapterId: 'ch-09',
      number: 3,
      title: 'Prime Minister, Council of Ministers & Attorney-General',
      subtitle: 'Articles 74, 75, 76 & 78: Collective Responsibility & First Law Officer',
      articleRef: 'Articles 74, 75, 76, 78',
      description: 'Article 74: Council of Ministers to aid and advise the President (binding advice after 42nd and 44th Amendments; President may require reconsideration once); Article 75: Appointment of PM and Ministers, collective responsibility of Council of Ministers to the House of the People (Lok Sabha), individual responsibility at pleasure of President; 91st Amendment 2003 (15% cap on size of Ministry); Article 76: Attorney-General for India (qualifications of Supreme Court judge, right of audience in all courts, right to speak in Parliament without voting rights).',
      mcqsCount: 12,
      pyqsCount: 5,
      estimatedMinutes: 25
    },

    // CHAPTER 10: THE UNION PARLIAMENT (3 topics)
    {
      id: 'top-const-10-01',
      chapterId: 'ch-10',
      number: 1,
      title: 'Composition, Sessions & Officers of Parliament (Articles 79–104)',
      subtitle: 'Rajya Sabha, Lok Sabha, Delimitation, Speaker, Disqualifications & Anti-Defection',
      articleRef: 'Articles 79 to 104',
      description: 'Article 79: Parliament consists of President, Council of States (Rajya Sabha: max 250, 12 nominated by President) and House of the People (Lok Sabha: max 550); Article 83: Rajya Sabha is a permanent body not subject to dissolution, 1/3rd members retire every 2 years; Lok Sabha 5-year term; Article 85: Sessions, maximum 6-month gap between two sessions; Presiding officers: Speaker & Deputy Speaker (Arts. 93–97); Disqualifications under Art. 102 and Tenth Schedule (Anti-Defection Law).',
      mcqsCount: 11,
      pyqsCount: 5,
      estimatedMinutes: 30
    },
    {
      id: 'top-const-10-02',
      chapterId: 'ch-10',
      number: 2,
      title: 'Legislative Procedure & Types of Bills (Articles 107–117)',
      subtitle: 'Ordinary Bills, Money Bills (Art. 110), Financial Bills & Joint Sittings (Art. 108)',
      articleRef: 'Articles 107, 108, 109, 110, 111, 117',
      description: 'Ordinary Bills: Can originate in either House, simple majority; Joint Sitting under Article 108 convened by President, presided over by Speaker of Lok Sabha; Article 109 & 110: Money Bills (introduced only in Lok Sabha on President’s recommendation, Speaker’s certificate final, Rajya Sabha has 14 days to make recommendations only, no joint sitting); Financial Bills Category I (Art. 117(1)) and Category II (Art. 117(3)); Presidential assent and suspensive veto (Art. 111).',
      mcqsCount: 12,
      pyqsCount: 6,
      estimatedMinutes: 35
    },
    {
      id: 'top-const-10-03',
      chapterId: 'ch-10',
      number: 3,
      title: 'Financial Procedures, Privileges & Parliamentary Committees',
      subtitle: 'Annual Financial Statement (Art. 112), Article 105 Privileges & Public Accounts Committee',
      articleRef: 'Articles 105, 112, 113, 114, 115, 116',
      description: 'Article 112: Annual Financial Statement (Budget), Charged Expenditure vs Voted Expenditure; Appropriation Bills (Art. 114), Vote on Account (Art. 116); Consolidated Fund of India (Art. 266), Contingency Fund (Art. 267); Parliamentary Privileges under Article 105 (freedom of speech in Parliament, immunity from judicial proceedings, Searchlight case); Parliamentary Standing Committees: Public Accounts Committee (PAC, 22 members, headed by opposition member), Estimates Committee (30 members, only from Lok Sabha), Committee on Public Undertakings.',
      mcqsCount: 12,
      pyqsCount: 5,
      estimatedMinutes: 30
    },

    // CHAPTER 11: STATE GOVERNMENT & LOCAL SELF-GOVERNANCE (3 topics)
    {
      id: 'top-const-11-01',
      chapterId: 'ch-11',
      number: 1,
      title: 'The Governor: Constitutional Position, Powers & Discretion',
      subtitle: 'Articles 153–163 & 213: Appointment, Dual Capacity & Ordinance Power',
      articleRef: 'Articles 153 to 163, 213',
      description: 'Article 153 (Governor for each State, 7th Amendment allows same person for two States); appointed by President under warrant, holds office during pleasure of President (B.P. Singhal v. UOI 2010); Executive powers, constitutional discretion under Art. 163 (reservation of bills for President Art. 200, recommendation for President’s rule Art. 356); Article 213: Governor’s ordinance-making power (co-extensive with State legislative power).',
      mcqsCount: 10,
      pyqsCount: 3,
      estimatedMinutes: 25
    },
    {
      id: 'top-const-11-02',
      chapterId: 'ch-11',
      number: 2,
      title: 'State Legislature & Advocate-General for the State',
      subtitle: 'Articles 164–212: Vidhan Sabha, Vidhan Parishad & Article 165',
      articleRef: 'Articles 164 to 212',
      description: 'Composition of Legislative Assembly (Vidhan Sabha: 60 to 500) and Legislative Council (Vidhan Parishad: abolition/creation under Art. 169); Chief Minister and collective responsibility to Legislative Assembly; Article 165: Advocate-General for the State (appointed by Governor, qualified to be High Court judge); legislative procedures in State Legislatures (no joint sitting in States).',
      mcqsCount: 10,
      pyqsCount: 3,
      estimatedMinutes: 25
    },
    {
      id: 'top-const-11-03',
      chapterId: 'ch-11',
      number: 3,
      title: 'Rural Local Self-Governance: The Panchayati Raj System',
      subtitle: 'Part IX, 73rd Amendment Act, 1992 & Eleventh Schedule (29 Functional Items)',
      articleRef: 'Articles 243 to 243-O',
      description: '73rd Constitutional Amendment Act 1992: Three-tier Panchayati Raj system (Gram Panchayat, Panchayat Samiti / Intermediate, Zilla Parishad); Gram Sabha (Art. 243A); compulsory vs voluntary provisions; reservation of seats for SC/ST and minimum 1/3rd for women (Art. 243D); 5-year fixed duration and mandatory dissolution elections within 6 months (Art. 243E); State Election Commission (Art. 243K); State Finance Commission (Art. 243I); bar to interference by courts in electoral matters (Art. 243-O); Eleventh Schedule 29 matters.',
      mcqsCount: 10,
      pyqsCount: 3,
      estimatedMinutes: 25
    },
    {
      id: 'top-const-11-04',
      chapterId: 'ch-11',
      number: 4,
      title: 'Urban Local Bodies: Municipalities & Planning Committees',
      subtitle: 'Part IXA, 74th Amendment Act, 1992 & Twelfth Schedule (18 Functional Items)',
      articleRef: 'Articles 243P to 243ZG',
      description: '74th Constitutional Amendment Act 1992: Three types of Urban Local Bodies (Nagar Panchayats, Municipal Councils, Municipal Corporations); Wards Committees (Art. 243S); reservations for SC/ST and women (Art. 243T); 5-year tenure (Art. 243U); District Planning Committee (Art. 243ZD) and Metropolitan Planning Committee (Art. 243ZE); Twelfth Schedule 18 functional items; Part IXB Co-operative Societies (Arts. 243ZH–243ZT).',
      mcqsCount: 10,
      pyqsCount: 2,
      estimatedMinutes: 25
    },

    // CHAPTER 12: THE UNION & STATE JUDICIARY (4 topics)
    {
      id: 'top-const-12-01',
      chapterId: 'ch-12',
      number: 1,
      title: 'Structure of Supreme Court & Judicial Appointments',
      subtitle: 'Articles 124–130: The Collegium System, First/Second/Third/Fourth Judges Cases',
      articleRef: 'Articles 124 to 130',
      description: 'Establishment and constitution of Supreme Court (Art. 124); Qualifications of SC judges; Tenure up to 65 years; Removal procedure by Parliament for proved misbehaviour or incapacity (Judges Inquiry Act 1968); Evolution of Collegium: S.P. Gupta (First Judges Case 1981), Supreme Court Advocates-on-Record Association (Second Judges Case 1993, primacy of CJI), Special Reference No. 1 of 1998 (Third Judges Case, CJI + 4 senior-most judges), NJAC Case (Fourth Judges Case 2015, striking down 99th Amendment).',
      mcqsCount: 11,
      pyqsCount: 6,
      estimatedMinutes: 30
    },
    {
      id: 'top-const-12-02',
      chapterId: 'ch-12',
      number: 2,
      title: 'Jurisdictions of the Supreme Court of India',
      subtitle: 'Original (Art. 131), Appellate (Arts. 132–134), SLP (Art. 136) & Advisory (Art. 143)',
      articleRef: 'Articles 131, 132, 133, 134, 136, 143',
      description: 'Article 131: Exclusive Original Jurisdiction in federal disputes (between Centre and States or between States); Appellate Jurisdiction: Constitutional matters (Art. 132), Civil matters (Art. 133), Criminal matters (Art. 134); Article 136: Special Leave Petition (plenary discretionary jurisdiction against any court or tribunal in India, except armed forces tribunals); Article 143: Advisory Jurisdiction (Presidential reference on question of law or fact, Re Delhi Laws Act, Ayodhya Reference).',
      mcqsCount: 12,
      pyqsCount: 7,
      estimatedMinutes: 35
    },
    {
      id: 'top-const-12-03',
      chapterId: 'ch-12',
      number: 3,
      title: 'Constitutional Powers: Binding Law, Complete Justice & Contempt',
      subtitle: 'Articles 129, 141, 142 & 144: Court of Record, Stare Decisis & Inherent Equity',
      articleRef: 'Articles 129, 141, 142, 144',
      description: 'Article 129: Supreme Court is a Court of Record with power to punish for contempt of itself; Article 141: Law declared by Supreme Court shall be binding on all courts within the territory of India (Stare Decisis, ratio decidendi vs obiter dicta); Article 142: Supreme Court’s extraordinary power to pass any decree or order necessary for doing "complete justice in any cause or matter pending before it" (Union Carbide, Ayodhya judgment); Article 144: Civil and judicial authorities to act in aid of Supreme Court.',
      mcqsCount: 11,
      pyqsCount: 5,
      estimatedMinutes: 30
    },
    {
      id: 'top-const-12-04',
      chapterId: 'ch-12',
      number: 4,
      title: 'The High Courts & Subordinate Courts in States',
      subtitle: 'Articles 214–237: High Court Writs (Art. 226), Superintendence (Art. 227) & District Judges',
      articleRef: 'Articles 214 to 237',
      description: 'Article 214 (High Court for each State); Appointment and conditions of HC judges (Art. 217, retirement age 62); Article 226: High Court writ jurisdiction (broader than Art. 32, covers Fundamental Rights and "for any other purpose"); Article 227: Power of superintendence over all courts and tribunals; Article 233: Appointment of District Judges by Governor in consultation with High Court; Article 235: Control over subordinate courts vested in High Court.',
      mcqsCount: 11,
      pyqsCount: 4,
      estimatedMinutes: 30
    },

    // CHAPTER 13: EMERGENCY PROVISIONS (2 topics)
    {
      id: 'top-const-13-01',
      chapterId: 'ch-13',
      number: 1,
      title: 'National Emergency (Article 352): Grounds, Safeguards & Effects',
      subtitle: 'War, External Aggression or Armed Rebellion, Articles 358 & 359 (44th Amendment)',
      articleRef: 'Articles 352, 353, 354, 358, 359',
      description: 'Article 352: Grounds: War, External Aggression, or Armed Rebellion (substituted for "internal disturbance" by 44th Amendment 1978); Cabinet written advice mandatory; Parliamentary approval within 1 month by special majority, 6-month renewal; Effects: Union executive powers extend to States (Art. 353), Parliament can legislate on State list; Article 358: Automatic suspension of Art. 19 only during war/external aggression; Article 359: Presidential order suspending enforcement of FRs, except Articles 20 and 21 (which can never be suspended).',
      mcqsCount: 13,
      pyqsCount: 6,
      estimatedMinutes: 30
    },
    {
      id: 'top-const-13-02',
      chapterId: 'ch-13',
      number: 2,
      title: 'President’s Rule (Article 356) & Financial Emergency (Article 360)',
      subtitle: 'Failure of Constitutional Machinery in States, S.R. Bommai Principles & Financial Crisis',
      articleRef: 'Articles 355, 356, 357, 360',
      description: 'Article 355: Duty of Union to protect States against external aggression and internal disturbance; Article 356: President’s Rule on report of Governor or otherwise when State government cannot be carried on in accordance with Constitution; Parliamentary approval within 2 months by simple majority, maximum 3-year ceiling; S.R. Bommai v. UOI (1994) landmark guidelines: proclamation subject to judicial review, floor test mandatory, secularism basic feature; Article 360: Financial Emergency (threat to financial stability/credit of India, reduction of salaries of public servants and judges, never declared so far).',
      mcqsCount: 12,
      pyqsCount: 5,
      estimatedMinutes: 30
    },

    // CHAPTER 14: CONSTITUTIONAL AMENDMENTS (2 topics)
    {
      id: 'top-const-14-01',
      chapterId: 'ch-14',
      number: 1,
      title: 'The Amendment Procedure under Article 368',
      subtitle: 'Three Types of Amendments: Simple, Special & Special with State Ratification',
      articleRef: 'Article 368',
      description: 'Constituent power of Parliament under Article 368; Bill can originate in either House of Parliament (not in State Legislatures); No provision for Joint Sitting on Constitution Amendment Bill; Three modes of amendment: (1) Simple majority outside Art. 368 (e.g. Arts. 2, 3, creation of legislative councils, quorum); (2) Special majority under Art. 368 (majority of total membership + 2/3rd members present & voting); (3) Special majority with ratification by not less than one-half of State Legislatures (federal provisions, election of President, representation of States in Parliament, Art. 368 itself); Presidential assent mandatory (24th Amendment 1971).',
      mcqsCount: 15,
      pyqsCount: 6,
      estimatedMinutes: 30
    },
    {
      id: 'top-const-14-02',
      chapterId: 'ch-14',
      number: 2,
      title: 'The Basic Structure Doctrine & Landmark Jurisprudence',
      subtitle: 'From Shankari Prasad to Kesavananda Bharati, Minerva Mills & NJAC',
      articleRef: 'Article 368 & Basic Structure',
      description: 'The historic judicial contest: Shankari Prasad v. UOI 1951 (Art. 368 includes power to amend FRs); Sajjan Singh v. State of Rajasthan 1965 (Hidayatullah & Mudholkar JJ. doubts); I.C. Golaknath v. State of Punjab 1967 (11-Judge bench holds Parliament cannot abridge FRs, Art. 13 applies to Art. 368 amendments); 24th Amendment 1971; Kesavananda Bharati v. State of Kerala 1973 (Largest 13-Judge bench, 7:6 majority: Parliament has wide constituent power to amend any part of the Constitution including FRs, but cannot alter its "Basic Structure"); Indira Nehru Gandhi v. Raj Narain 1975 (free and fair elections, rule of law basic structure); Minerva Mills v. UOI 1980 (limited amending power is basic structure); Waman Rao 1981; I.R. Coelho 2007 (Ninth Schedule laws subject to basic structure review); NJAC Case 2015 (Judicial independence).',
      mcqsCount: 15,
      pyqsCount: 8,
      estimatedMinutes: 35
    },

    // CHAPTER 15: FEDERAL RELATIONS, SCHEDULES & CONSTITUTIONAL BODIES (3 topics)
    {
      id: 'top-const-15-01',
      chapterId: 'ch-15',
      number: 1,
      title: 'Centre-State Relations: Legislative, Administrative & Financial',
      subtitle: 'Part XI & XII: Three Lists, Pith and Substance, Territorial Nexus & Repugnancy (Art. 254)',
      articleRef: 'Articles 245 to 293 & Seventh Schedule',
      description: 'Legislative relations: Territorial extent (Art. 245); Subject matter distribution (Art. 246 & Seventh Schedule: List I Union 100 items, List II State 61 items, List III Concurrent 52 items); Residuary powers in Parliament (Art. 248); Parliamentary legislation on State subjects: National interest (Art. 249), Proclamation of Emergency (Art. 250), by consent of States (Art. 252), International treaties (Art. 253); Interpretation doctrines: Territorial Nexus, Pith and Substance (Prafulla Kumar), Colorable Legislation, Harmonious Construction; Article 254: Repugnancy between Union and State laws in Concurrent list (Union law prevails unless State law reserved for and received President’s assent); Administrative relations (Arts. 256–263, Inter-State Council Art. 263); Financial relations & GST Council (Art. 279A).',
      mcqsCount: 12,
      pyqsCount: 5,
      estimatedMinutes: 35
    },
    {
      id: 'top-const-15-02',
      chapterId: 'ch-15',
      number: 2,
      title: 'The Twelve Schedules of the Constitution',
      subtitle: 'First to Twelfth Schedules, Fifth & Sixth Tribal Areas, Tenth Schedule Anti-Defection',
      articleRef: 'Schedules 1 to 12',
      description: 'Comprehensive analysis of all 12 Schedules: 1st (States & UTs), 2nd (Salaries & Emoluments), 3rd (Forms of Oaths & Affirmations), 4th (Allocation of seats in Rajya Sabha), 5th (Administration of Scheduled Areas & Scheduled Tribes), 6th (Tribal Areas in Assam, Meghalaya, Tripura, Mizoram), 7th (Union, State, Concurrent Lists), 8th (22 Recognised Languages), 9th (Validation of Acts, Art. 31B, I.R. Coelho), 10th (Disqualification on ground of defection, 52nd Amendment 1985, Kihoto Hollohan 1992), 11th (Panchayats 29 matters, 73rd Amendment), 12th (Municipalities 18 matters, 74th Amendment).',
      mcqsCount: 11,
      pyqsCount: 5,
      estimatedMinutes: 30
    },
    {
      id: 'top-const-15-03',
      chapterId: 'ch-15',
      number: 3,
      title: 'Independent Constitutional Bodies & Watchdogs',
      subtitle: 'Election Commission of India (Art. 324), Finance Commission (Art. 280) & CAG (Art. 148)',
      articleRef: 'Articles 148, 280, 324',
      description: 'Election Commission of India (Art. 324: superintendence, direction and control of elections, multi-member body, Chief Election Commissioner protection similar to SC judge, T.N. Seshan, Anoop Baranwal 2023); Comptroller and Auditor General of India (Art. 148: guardian of public purse, audit of Union & State accounts, Reports submitted to President/Governor under Art. 151, CAG reports examined by PAC); Finance Commission (Art. 280: quasi-judicial body constituted every 5 years by President, recommendations on devolution of tax proceeds, grants-in-aid to States).',
      mcqsCount: 11,
      pyqsCount: 4,
      estimatedMinutes: 25
    },
    {
      id: 'top-const-15-04',
      chapterId: 'ch-15',
      number: 4,
      title: 'Public Services, Doctrine of Pleasure & Administrative Tribunals',
      subtitle: 'Articles 308–323B: Civil Services (Art. 311), UPSC/SPSCs & Tribunals (L. Chandra Kumar)',
      articleRef: 'Articles 308–323 & 323A–323B',
      description: 'Part XIV Services: Doctrine of Pleasure (Art. 310) qualified by constitutional safeguards under Article 311 (no dismissal/removal by subordinate authority, reasonable opportunity of being heard/inquiry, exceptions under 311(2)(a)/(b)/(c), Union of India v. Tulsiram Patel 1985); Public Service Commissions (Arts. 315–323: Union and State PSCs, independence safeguards Art. 317); Part XIVA Administrative Tribunals (42nd Amendment 1976, Arts. 323A & 323B, Administrative Tribunals Act 1985, L. Chandra Kumar v. UOI 1997 judicial review under Arts. 226/227 is basic structure).',
      mcqsCount: 12,
      pyqsCount: 5,
      estimatedMinutes: 30
    }
  ];

  // Expose to window
  if (typeof window !== 'undefined') {
    window.CONSTITUTION_TOPICS = CONSTITUTION_TOPICS;
  }
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONSTITUTION_TOPICS;
  }
})();
