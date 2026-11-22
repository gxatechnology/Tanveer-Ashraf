"""
Builds MCQs for Chapters 1 to 5 (135 MCQs) as Python dictionaries.
No string templating -> json.dumps handles all escaping safely.
"""

def create_mcq(m_id, ch_id, top_id, q_text, opts, ans_idx, expl, breakdowns, diff, prov, obj):
    letters = ["A", "B", "C", "D"]
    return {
        "id": m_id,
        "subjectId": "law-constitution",
        "chapterId": ch_id,
        "topicId": top_id,
        "question": q_text,
        "options": opts,
        "answer": ans_idx,
        "answerLetter": letters[ans_idx],
        "explanation": expl,
        "optionBreakdown": breakdowns,
        "difficulty": diff,
        "provision": prov,
        "sourceUrl": "https://legislative.gov.in",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": obj,
        "eligible": True,
        "status": "active"
    }

MCQS_CH01_05 = []

# ==============================================================================
# CHAPTER 1: HISTORICAL BACKGROUND (30 MCQs)
# ==============================================================================
# 01-01 to 01-10: 1773 to 1853
MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-001", "ch-01", "top-const-01-01",
    "Which British enactment first established a Supreme Court of Judicature at Fort William in Calcutta?",
    ["Pitt's India Act, 1784", "Regulating Act, 1773", "Charter Act, 1793", "Charter Act, 1813"],
    1,
    "The Regulating Act of 1773 provided for the establishment of a Supreme Court of Judicature at Fort William, Calcutta (constituted in 1774), consisting of one Chief Justice (Sir Elijah Impey) and three other judges.",
    {"A": "Pitt's India Act 1784 introduced the Board of Control.", "B": "Correct. Regulating Act 1773 created the Calcutta Supreme Court.", "C": "Charter Act 1793 renewed company monopoly for 20 years.", "D": "Charter Act 1813 allocated 1 lakh rupees for education."},
    "Easy", "Regulating Act, 1773, Section 13", "Identify establishment of Supreme Court at Calcutta."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-002", "ch-01", "top-const-01-01",
    "Who was appointed as the first Governor-General of Bengal under the Regulating Act of 1773?",
    ["Lord Clive", "Lord Cornwallis", "Lord Warren Hastings", "Lord William Bentinck"],
    2,
    "Lord Warren Hastings was designated the first Governor-General of Bengal under the Regulating Act of 1773, assisted by an Executive Council of four members.",
    {"A": "Lord Clive was Governor of Bengal during the Dual System.", "B": "Lord Cornwallis introduced the Permanent Settlement in 1793.", "C": "Correct. Lord Warren Hastings was the first Governor-General of Bengal.", "D": "Lord William Bentinck was the first Governor-General of India in 1833."},
    "Easy", "Regulating Act, 1773, Section 7", "Recall first Governor-General of Bengal."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-003", "ch-01", "top-const-01-01",
    "The system of 'Double Government' (Board of Control and Court of Directors) was introduced by which Act?",
    ["Regulating Act, 1773", "Pitt's India Act, 1784", "Act of Settlement, 1781", "Charter Act, 1833"],
    1,
    "Pitt's India Act of 1784 created a Board of Control representing the British Crown to manage civil, military, and revenue affairs, while commercial matters were left to the Court of Directors.",
    {"A": "Regulating Act 1773 initiated parliamentary supervision without a Board of Control.", "B": "Correct. Pitt's India Act 1784 established the dual government system.", "C": "Act of Settlement 1781 resolved jurisdictional clashes between Governor-General and Calcutta Supreme Court.", "D": "Charter Act 1833 ended commercial functions entirely."},
    "Medium", "Pitt's India Act, 1784", "Differentiate commercial from political British oversight."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-004", "ch-01", "top-const-01-01",
    "Which Charter Act completely deprived the East India Company of its commercial privileges and made it purely an administrative body?",
    ["Charter Act, 1813", "Charter Act, 1833", "Charter Act, 1853", "Charter Act, 1793"],
    1,
    "The Charter Act of 1833 terminated the commercial business of the East India Company, including the tea trade and China trade (retained under 1813), transforming it into a purely administrative trustee for the British Crown.",
    {"A": "Charter Act 1813 retained monopoly in tea and trade with China.", "B": "Correct. Charter Act 1833 ended all commercial privileges.", "C": "Charter Act 1853 separated executive and legislative wings.", "D": "Charter Act 1793 merely extended trading monopoly."},
    "Medium", "Charter Act, 1833, Section 3", "Trace commercial sunset of East India Company."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-005", "ch-01", "top-const-01-01",
    "Who was added as the fourth (Law) member to the Governor-General's Council under the Charter Act of 1833?",
    ["Lord Macaulay", "Sir Charles Wood", "Lord Dalhousie", "Lord Canning"],
    0,
    "Lord T.B. Macaulay was added as the fourth (ordinary) member for law-making purposes, though without voting rights in executive matters, leading to the appointment of the First Law Commission in 1834.",
    {"A": "Correct. Lord Macaulay was appointed first Law Member.", "B": "Sir Charles Wood issued Wood's Despatch on education in 1854.", "C": "Lord Dalhousie introduced the Doctrine of Lapse.", "D": "Lord Canning was first Viceroy in 1858."},
    "Easy", "Charter Act, 1833, Section 40", "Identify appointment of first Law Member."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-006", "ch-01", "top-const-01-01",
    "Which Act for the first time separated the legislative and executive functions of the Governor-General's Council?",
    ["Charter Act, 1813", "Charter Act, 1833", "Charter Act, 1853", "Indian Councils Act, 1861"],
    2,
    "The Charter Act of 1853 separated the legislative and executive functions by adding six new members termed 'Legislative Councillors' (Indian Central Legislative Council), functioning as a mini-parliament.",
    {"A": "Charter Act 1813 did not bifurcate functions.", "B": "Charter Act 1833 centralized legislative power but kept a unified council.", "C": "Correct. Charter Act 1853 created the distinct Legislative Council.", "D": "Indian Councils Act 1861 introduced portfolio system and ordinances."},
    "Medium", "Charter Act, 1853", "Analyze origin of separate legislative council."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-007", "ch-01", "top-const-01-01",
    "Open competition for recruitment to the Indian Civil Service (covenanted civil service) was successfully introduced by:",
    ["Charter Act of 1833", "Charter Act of 1853", "Government of India Act, 1858", "Indian Civil Service Act, 1861"],
    1,
    "While Charter Act 1833 proposed open competition (negated by Court of Directors), it was the Charter Act of 1853 that successfully introduced open competitive examination, leading to the Macaulay Committee of 1854.",
    {"A": "Charter Act 1833 attempt was blocked by Court of Directors.", "B": "Correct. Charter Act 1853 enacted open competition.", "C": "Act of 1858 transferred power to the Crown.", "D": "Act of 1861 validated irregular appointments."},
    "Medium", "Charter Act, 1853, Section 36", "Differentiate 1833 proposal from 1853 enactment."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-008", "ch-01", "top-const-01-01",
    "By which Act was the Governor-General of Bengal redesignated as the 'Governor-General of India'?",
    ["Regulating Act, 1773", "Pitt's India Act, 1784", "Charter Act, 1833", "Government of India Act, 1858"],
    2,
    "The Charter Act of 1833 redesignated the Governor-General of Bengal as the Governor-General of India and vested in him all civil and military powers across British India. Lord William Bentinck was the first.",
    {"A": "1773 created Governor-General of Bengal.", "B": "1784 maintained Bengal title.", "C": "Correct. 1833 designated Governor-General of India.", "D": "1858 added the title of Viceroy."},
    "Easy", "Charter Act, 1833, Section 39", "Recall redesignation of Governor-General."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-009", "ch-01", "top-const-01-01",
    "The Act of Settlement, 1781 was enacted primarily to:",
    ["Abolish the East India Company", "Remedy defects and demarcate jurisdiction between the Supreme Court at Calcutta and the Governor-General-in-Council", "Grant diwani rights to the Crown", "Introduce local self-governance"],
    1,
    "The Declaratory Act / Act of Settlement 1781 exempted the Governor-General and his Council from the jurisdiction of the Supreme Court for acts done in their official capacity and excluded revenue matters from the court's purview.",
    {"A": "The Company was abolished in 1858.", "B": "Correct. Demarcated jurisdiction between executive council and court.", "C": "Diwani rights were granted in 1765.", "D": "Local self-government arose under Lord Ripon in 1882."},
    "Medium", "Act of Settlement, 1781 (21 Geo. III, c. 70)", "Understand resolution of Patna and Cossijurah cases."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-010", "ch-01", "top-const-01-01",
    "Which Charter Act introduced local representation in the Indian (Central) Legislative Council for the first time?",
    ["Charter Act, 1813", "Charter Act, 1833", "Charter Act, 1853", "Indian Councils Act, 1861"],
    2,
    "The Charter Act of 1853 introduced local representation: of the six new legislative members, four were appointed by local governments of Madras, Bombay, Bengal, and Agra.",
    {"A": "1813 had no local legislative representation.", "B": "1833 had no provincial representation in council.", "C": "Correct. 1853 added 4 representatives from local governments.", "D": "1861 expanded non-official members."},
    "Hard", "Charter Act, 1853", "Recognize earliest provincial representation in Central Legislature."
))

# 01-11 to 01-20: 1858 to 1919
MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-011", "ch-01", "top-const-01-02",
    "The Government of India Act, 1858 abolished which administrative institutions in Britain?",
    ["House of Commons and House of Lords", "Court of Directors and Board of Control", "Privy Council and Star Chamber", "Governor-General and Council of State"],
    1,
    "The Act for the Better Government of India, 1858 abolished the dual system of government by dissolving both the Board of Control and the Court of Directors, transferring all authority to the Secretary of State for India.",
    {"A": "British Parliament remained supreme.", "B": "Correct. Abolished Court of Directors and Board of Control.", "C": "Privy Council continued as final appellate court.", "D": "Governor-General continued with additional title of Viceroy."},
    "Easy", "Government of India Act, 1858, Section 1", "Trace dissolution of dual British oversight."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-012", "ch-01", "top-const-01-02",
    "Under the Indian Councils Act, 1861, which landmark administrative reform was formally recognized?",
    ["Dyarchy", "Portfolio System introduced by Lord Canning", "Communal Electorate", "Bicameralism"],
    1,
    "The Indian Councils Act, 1861 accorded statutory recognition to the 'Portfolio System' introduced by Lord Canning in 1859, laying the foundation of cabinet governance in India.",
    {"A": "Dyarchy was introduced in 1919.", "B": "Correct. Recognized Lord Canning's Portfolio System.", "C": "Communal electorates arrived in 1909.", "D": "Bicameralism was introduced in 1919."},
    "Medium", "Indian Councils Act, 1861, Section 8", "Identify statutory origin of portfolio cabinet system."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-013", "ch-01", "top-const-01-02",
    "Which Act for the first time empowered the Viceroy to issue Ordinances during an emergency without the concurrence of the Legislative Council?",
    ["Charter Act, 1853", "Indian Councils Act, 1861", "Indian Councils Act, 1892", "Government of India Act, 1919"],
    1,
    "Section 23 of the Indian Councils Act, 1861 empowered the Viceroy to promulgate ordinances in emergencies with a maximum validity of six months, the direct constitutional ancestor of Article 123.",
    {"A": "1853 had no ordinance power.", "B": "Correct. Section 23 of 1861 Act created ordinance power.", "C": "1892 expanded budget discussion rights.", "D": "1919 expanded legislative domain."},
    "Medium", "Indian Councils Act, 1861, Section 23", "Trace constitutional roots of Article 123 ordinances."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-014", "ch-01", "top-const-01-02",
    "Under the Indian Councils Act of 1892, members of legislative councils gained the right to:",
    ["Vote on the Budget", "Discuss the Annual Budget and address questions to the Executive", "Move adjournment motions", "Introduce Money Bills"],
    1,
    "The Indian Councils Act, 1892 gave members the power to discuss the budget and address questions to the executive on matters of public interest (subject to conditions), but did NOT permit voting on the budget or supplementary questions.",
    {"A": "Voting on budget items was not permitted until later reforms.", "B": "Correct. Allowed discussion and questions on the budget.", "C": "Adjournment motions came later.", "D": "Money bills were executive domain."},
    "Medium", "Indian Councils Act, 1892, Section 1(2)", "Examine budget powers under 1892 Act."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-015", "ch-01", "top-const-01-02",
    "The Indian Councils Act, 1909 (Morley-Minto Reforms) is historically infamous for introducing:",
    ["Federalism", "Separate Communal Electorates for Muslims", "Provincial Autonomy", "Direct universal adult suffrage"],
    1,
    "The 1909 Act introduced separate electorates for Muslims, legalizing communal representation. Lord Minto came to be known as the 'Father of Communal Electorate'.",
    {"A": "Federalism was introduced by 1935 Act.", "B": "Correct. Introduced communal electorates for Muslims.", "C": "Provincial Autonomy was enacted in 1935.", "D": "Universal franchise came with 1950 Constitution."},
    "Easy", "Indian Councils Act, 1909", "Identify communal electorate introduction."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-016", "ch-01", "top-const-01-02",
    "Who was the first Indian appointed to the Viceroy's Executive Council under the Morley-Minto Reforms?",
    ["Satyendra Prasanna Sinha", "Tej Bahadur Sapru", "Dadabhai Naoroji", "Gopal Krishna Gokhale"],
    0,
    "Satyendra Prasanna Sinha (later Lord Sinha) was appointed as the Law Member in the Viceroy's Executive Council in 1909, becoming the first Indian member.",
    {"A": "Correct. Satyendra Prasanna Sinha was appointed first Indian member.", "B": "Sir Tej Bahadur Sapru was a later law member.", "C": "Dadabhai Naoroji was British MP in 1892.", "D": "G.K. Gokhale was a member of Imperial Legislative Council."},
    "Easy", "Indian Councils Act, 1909", "Recall first Indian executive council member."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-017", "ch-01", "top-const-01-02",
    "The system of 'Dyarchy' in provincial governments was introduced by which statute?",
    ["Indian Councils Act, 1909", "Government of India Act, 1919", "Government of India Act, 1935", "Indian Independence Act, 1947"],
    1,
    "The Government of India Act, 1919 (Montagu-Chelmsford Reforms) introduced Dyarchy (rule of two) in the provinces by dividing provincial subjects into 'Transferred' and 'Reserved' subjects.",
    {"A": "1909 expanded councils without dyarchy.", "B": "Correct. 1919 introduced Dyarchy in the provinces.", "C": "1935 abolished provincial dyarchy and introduced it at the Centre.", "D": "1947 created dominion status."},
    "Easy", "Government of India Act, 1919, Section 1", "Identify provincial dyarchy statute."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-018", "ch-01", "top-const-01-02",
    "Under the 1919 Act, 'Reserved Subjects' in the provinces were administered by:",
    ["The Governor with his Ministers responsible to the Legislature", "The Governor and his Executive Council without legislative responsibility", "The Secretary of State directly", "The Viceroy of India"],
    1,
    "Reserved subjects (law and order, finance, land revenue, police) were administered by the Governor and his Executive Council without being responsible to the provincial legislative council.",
    {"A": "Transferred subjects (education, health, local govt) were administered with responsible ministers.", "B": "Correct. Reserved subjects were run by Governor and non-responsible Executive Council.", "C": "Secretary of State was in London.", "D": "Viceroy oversaw the Central government."},
    "Medium", "Government of India Act, 1919", "Distinguish Reserved from Transferred subjects."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-019", "ch-01", "top-const-01-02",
    "Bicameralism at the Central Legislature (Council of State and Legislative Assembly) was introduced for the first time by:",
    ["Charter Act, 1853", "Indian Councils Act, 1909", "Government of India Act, 1919", "Government of India Act, 1935"],
    2,
    "The Government of India Act, 1919 replaced the Indian Legislative Council with a bicameral legislature at the Centre: the Council of State (Upper House) and the Central Legislative Assembly (Lower House).",
    {"A": "1853 created a unicameral legislative council.", "B": "1909 maintained unicameral central council.", "C": "Correct. 1919 introduced Central bicameralism.", "D": "1935 expanded bicameralism to six provinces."},
    "Medium", "Government of India Act, 1919, Section 17", "Identify origin of central bicameralism."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-020", "ch-01", "top-const-01-02",
    "Which Act provided for the establishment of a Public Service Commission, leading to the setting up of the Central Public Service Commission in 1926?",
    ["Indian Councils Act, 1909", "Government of India Act, 1919", "Government of India Act, 1935", "Charter Act, 1853"],
    1,
    "Section 96C of the Government of India Act, 1919 provided for the establishment of a Public Service Commission, which was set up in 1926 under the chairmanship of Sir Ross Barker following the Lee Commission recommendations (1924).",
    {"A": "1909 had no statutory commission clause.", "B": "Correct. Section 96C of 1919 Act provided for Public Service Commission.", "C": "1935 created Federal PSC and Provincial PSCs.", "D": "1853 introduced examination without a permanent commission."},
    "Hard", "Government of India Act, 1919, Section 96C", "Trace origin of Central Public Service Commission."
))

# 01-21 to 01-30: 1935 and 1947
MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-021", "ch-01", "top-const-01-03",
    "The Government of India Act, 1935 provided for an 'All-India Federation' consisting of:",
    ["Only Governors' Provinces", "Governors' Provinces and Chief Commissioners' Provinces only", "Provinces of British India and the Princely States as units", "Dominions of India and Pakistan"],
    2,
    "The 1935 Act contemplated an All-India Federation consisting of Governors' Provinces, Chief Commissioners' Provinces, and such Princely States as acceded to it. The federation never came into being as princely states did not join.",
    {"A": "Excluded princely states, which was inaccurate.", "B": "Omitted princely states.", "C": "Correct. Federation of British Indian Provinces and Princely States.", "D": "Dominions were created in 1947."},
    "Medium", "Government of India Act, 1935, Section 5", "Examine composition of proposed 1935 Federation."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-022", "ch-01", "top-const-01-03",
    "The Government of India Act, 1935 divided legislative powers into how many lists?",
    ["Two lists: Union and Provincial", "Three lists: Federal, Provincial, and Concurrent", "Four lists: Federal, State, Concurrent, and Princely", "Single list with residuary powers to Provinces"],
    1,
    "The 1935 Act established three legislative lists: Federal List (59 items), Provincial List (54 items), and Concurrent List (36 items), the direct blueprint for the Seventh Schedule of the 1950 Constitution.",
    {"A": "1919 had only central and provincial subjects.", "B": "Correct. Three lists: Federal, Provincial, Concurrent.", "C": "Four lists is historically erroneous.", "D": "Lists were tripartite."},
    "Easy", "Government of India Act, 1935, Seventh Schedule", "Trace Seventh Schedule origins in 1935 Act."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-023", "ch-01", "top-const-01-03",
    "Under the Government of India Act, 1935, in whom were the 'Residuary Powers' of legislation vested?",
    ["Federal Legislature", "Provincial Legislatures", "Governor-General in his discretion", "Secretary of State for India"],
    2,
    "Section 104 of the 1935 Act uniquely vested residuary legislative powers in the Governor-General in his personal discretion, who could allocate them to either the Federal or Provincial legislature as deemed fit.",
    {"A": "Federal legislature had only Federal list.", "B": "Provincial legislatures did not have residuary powers.", "C": "Correct. Section 104 vested residuary powers in the Governor-General.", "D": "Secretary of State held executive superintendence."},
    "Hard", "Government of India Act, 1935, Section 104", "Prelims Trap: Residuary powers in 1935 vs 1950."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-024", "ch-01", "top-const-01-03",
    "Which Act abolished Dyarchy in the Provinces and introduced 'Provincial Autonomy'?",
    ["Government of India Act, 1919", "Government of India Act, 1935", "Indian Independence Act, 1947", "Morley-Minto Reforms, 1909"],
    1,
    "The Government of India Act, 1935 abolished provincial dyarchy and established 'Provincial Autonomy' in its place, making provincial ministers responsible to elected provincial legislatures.",
    {"A": "1919 introduced provincial dyarchy.", "B": "Correct. 1935 abolished provincial dyarchy and gave autonomy.", "C": "1947 granted independence.", "D": "1909 did not touch provincial responsible government."},
    "Easy", "Government of India Act, 1935, Section 46", "Recall abolition of provincial dyarchy."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-025", "ch-01", "top-const-01-03",
    "The Federal Court of India was established under the Government of India Act, 1935 in which year?",
    ["1935", "1937", "1947", "1950"],
    1,
    "The Federal Court of India was inaugurated on 1st October 1937 in Delhi with Sir Maurice Gwyer as its first Chief Justice, functioning until the establishment of the Supreme Court of India on 28th January 1950.",
    {"A": "1935 was the year of enactment.", "B": "Correct. Established on 1 October 1937.", "C": "1947 was independence.", "D": "1950 was the inauguration of Supreme Court."},
    "Medium", "Government of India Act, 1935, Section 200", "Recall establishment year of Federal Court."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-026", "ch-01", "top-const-01-03",
    "The Indian Independence Act, 1947 was passed by the British Parliament based on which historic plan?",
    ["Cabinet Mission Plan", "Mountbatten Plan (3rd June Plan)", "Wavell Plan", "Cripps Proposal"],
    1,
    "The Indian Independence Act, 1947 was formulated on the basis of the Mountbatten Plan of June 3, 1947, receiving royal assent on July 18, 1947.",
    {"A": "Cabinet Mission 1946 devised Constituent Assembly framework.", "B": "Correct. Mountbatten Plan (June 3, 1947) partitioned and created two dominions.", "C": "Wavell Plan 1945 failed at Simla Conference.", "D": "Cripps 1942 was rejected by all parties."},
    "Easy", "Indian Independence Act, 1947", "Connect 1947 Act to Mountbatten Plan."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-027", "ch-01", "top-const-01-03",
    "Under the Indian Independence Act, 1947, what status was conferred on the Constituent Assemblies of India and Pakistan?",
    ["Subordinate advisory councils", "Fully sovereign legislative bodies with power to repeal any British Act including the 1947 Act", "Dominion consultative conferences", "Interim executive bodies under the Viceroy"],
    1,
    "Section 6 of the 1947 Act declared the Constituent Assemblies to be fully sovereign legislatures with unlimited constituent power, explicitly empowered to repeal or amend any British Act, including the Independence Act itself.",
    {"A": "Assemblies were sovereign, not subordinate.", "B": "Correct. Fully sovereign bodies with power to repeal any British law.", "C": "Assemblies possessed plenary law-making powers.", "D": "Viceroy office was abolished, becoming constitutional Governor-General."},
    "Medium", "Indian Independence Act, 1947, Section 6(2)", "Examine sovereign character of Constituent Assembly."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-028", "ch-01", "top-const-01-03",
    "The office of the Secretary of State for India was abolished by which statute?",
    ["Government of India Act, 1935", "Indian Independence Act, 1947", "Constitution of India, 1950", "Charter Act, 1853"],
    1,
    "The Indian Independence Act, 1947 abolished the office of the Secretary of State for India and transferred his functions to the Secretary of State for Commonwealth Affairs.",
    {"A": "1935 retained Secretary of State with advisers.", "B": "Correct. Indian Independence Act 1947 abolished the office.", "C": "Constitution 1950 came after abolition.", "D": "1853 was under Company rule."},
    "Medium", "Indian Independence Act, 1947, Section 14", "Recall abolition of Secretary of State."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-029", "ch-01", "top-const-01-03",
    "Until the Constitution of India came into force on 26th January 1950, the governance of the Dominion of India was conducted under:",
    ["Government of India Act, 1919 as adapted", "Government of India Act, 1935 as adapted by the India (Provisional Constitution) Order, 1947", "Cabinet Mission Regulations", "Charter Act, 1853"],
    1,
    "Section 8(2) of the Indian Independence Act 1947 provided that each Dominion would be governed in accordance with the Government of India Act, 1935, with necessary adaptations, until a new Constitution was enacted.",
    {"A": "1919 Act was superseded by 1935.", "B": "Correct. 1935 Act as adapted served as interim constitution.", "C": "Cabinet Mission had no statutory governance machinery.", "D": "1853 was obsolete."},
    "Medium", "Indian Independence Act, 1947, Section 8(2)", "Understand interim constitutional governance."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-01-030", "ch-01", "top-const-01-03",
    "Which Act ended the British Paramountcy over the Indian Princely States?",
    ["Government of India Act, 1935", "Indian Independence Act, 1947", "Treaty of Versailles, 1919", "Queen's Proclamation of 1858"],
    1,
    "Section 7 of the Indian Independence Act, 1947 declared the lapse of British suzerainty/paramountcy over Indian Princely States and all treaty relations with tribal areas from 15th August 1947.",
    {"A": "1935 preserved paramountcy in Crown Representative.", "B": "Correct. Section 7 lapsed British paramountcy.", "C": "Versailles was post-WWI European treaty.", "D": "1858 asserted Crown paramountcy."},
    "Easy", "Indian Independence Act, 1947, Section 7(1)(b)", "Identify lapse of paramountcy."
))

print(f"Ch 1 complete ({len(MCQS_CH01_05)} total).")

# ==============================================================================
# CHAPTER 2: MAKING OF THE CONSTITUTION & SALIENT FEATURES (30 MCQs)
# ==============================================================================
# 02-01 to 02-10: Constituent Assembly & Drafting
MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-001", "ch-02", "top-const-02-01",
    "Who first officially put forward the idea of a Constituent Assembly for India in 1934?",
    ["Mahatma Gandhi", "Jawaharlal Nehru", "M.N. Roy", "Subhas Chandra Bose"],
    2,
    "In 1934, M.N. Roy (pioneer of the communist movement in India) first proposed a Constituent Assembly for India. INC officially endorsed it in 1935.",
    {"A": "Mahatma Gandhi demanded swaraj determined by Indian will in 1922.", "B": "Jawaharlal Nehru framed the demand on adult franchise in 1938.", "C": "Correct. M.N. Roy first put forward the idea in 1934.", "D": "Subhas Chandra Bose led the Forward Bloc and INA."},
    "Easy", "Constituent Assembly Genesis", "Recall earliest proponent of Constituent Assembly."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-002", "ch-02", "top-const-02-01",
    "The Constituent Assembly of India was set up under the framework formulated by:",
    ["The Cripps Mission, 1942", "The Cabinet Mission Plan, 1946", "The Wavell Plan, 1945", "The Mountbatten Plan, 1947"],
    1,
    "The Constituent Assembly was constituted in November 1946 under the scheme formulated by the Cabinet Mission Plan (Pethick-Lawrence, Cripps, Alexander).",
    {"A": "Cripps proposals in 1942 were rejected.", "B": "Correct. Cabinet Mission Plan 1946 structured the Constituent Assembly.", "C": "Wavell Plan broke down at Simla.", "D": "Mountbatten Plan was for partition and independence."},
    "Easy", "Cabinet Mission Plan, 1946", "Identify founding constitutional scheme."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-003", "ch-02", "top-const-02-01",
    "Who presided over the inaugural meeting of the Constituent Assembly on December 9, 1946 as its temporary Chairman?",
    ["Dr. Rajendra Prasad", "Dr. B.R. Ambedkar", "Dr. Sachchidananda Sinha", "H.C. Mukherjee"],
    2,
    "Following the French practice of electing the oldest member, Dr. Sachchidananda Sinha presided over the inaugural meeting on 9th December 1946 as temporary Chairman.",
    {"A": "Dr. Rajendra Prasad was elected permanent President on 11th December 1946.", "B": "Dr. B.R. Ambedkar was Chairman of the Drafting Committee.", "C": "Correct. Dr. Sachchidananda Sinha was temporary Chairman.", "D": "H.C. Mukherjee was elected Vice-President along with V.T. Krishnamachari."},
    "Easy", "Constituent Assembly Debates, 9 Dec 1946", "Recall temporary Chairman of Constituent Assembly."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-004", "ch-02", "top-const-02-01",
    "Who was appointed as the Constitutional Adviser (Legal Adviser) to the Constituent Assembly?",
    ["Sir B.N. Rau", "Dr. K.M. Munshi", "Alladi Krishnaswami Iyer", "Sir B.L. Mitter"],
    0,
    "Sir Benegal Narsing Rau (B.N. Rau), an eminent jurist and former ICJ judge, was appointed as the Constitutional Adviser to the Constituent Assembly and prepared the initial draft of the Constitution.",
    {"A": "Correct. Sir B.N. Rau was the Constitutional Adviser.", "B": "Dr. K.M. Munshi was a member of the Drafting Committee.", "C": "Alladi Krishnaswami Iyer was an eminent member of the Drafting Committee.", "D": "Sir B.L. Mitter resigned from the Drafting Committee due to ill-health."},
    "Easy", "Constituent Assembly Secretariat", "Identify Constitutional Adviser."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-005", "ch-02", "top-const-02-01",
    "On which date was the historic 'Objectives Resolution' moved in the Constituent Assembly by Jawaharlal Nehru?",
    ["9th December, 1946", "13th December, 1946", "22nd January, 1947", "26th November, 1949"],
    1,
    "Jawaharlal Nehru moved the historic 'Objectives Resolution' on 13th December 1946, outlining the constitutional ideals and philosophy. It was unanimously adopted on 22nd January 1947 and shaped the Preamble.",
    {"A": "9th December 1946 was the first meeting.", "B": "Correct. Moved on 13th December 1946.", "C": "22nd January 1947 was the date of its unanimous adoption.", "D": "26th November 1949 was adoption of the Constitution."},
    "Medium", "Constituent Assembly Debates, 13 Dec 1946", "Identify date of Objectives Resolution."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-006", "ch-02", "top-const-02-01",
    "The Drafting Committee was appointed by the Constituent Assembly on:",
    ["15th August, 1947", "29th August, 1947", "26th November, 1949", "24th January, 1950"],
    1,
    "The Drafting Committee under the Chairmanship of Dr. B.R. Ambedkar was constituted on 29th August 1947 to prepare a draft of the new Constitution based on the initial draft by B.N. Rau.",
    {"A": "15th August 1947 was Independence Day.", "B": "Correct. 29th August 1947 was appointment of Drafting Committee.", "C": "26th November 1949 was adoption.", "D": "24th January 1950 was final signing."},
    "Medium", "Constituent Assembly Resolution, 29 Aug 1947", "Recall appointment date of Drafting Committee."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-007", "ch-02", "top-const-02-01",
    "How many members constituted the Drafting Committee of the Constituent Assembly?",
    ["Five", "Seven", "Nine", "Eleven"],
    1,
    "The Drafting Committee consisted of seven members: Dr. B.R. Ambedkar (Chairman), N. Gopalaswamy Ayyangar, Alladi Krishnaswami Iyer, Dr. K.M. Munshi, Syed Mohammad Saadulla, N. Madhava Rau, and T.T. Krishnamachari.",
    {"A": "Five is incorrect.", "B": "Correct. Exactly seven members.", "C": "Nine is incorrect.", "D": "Eleven is incorrect."},
    "Easy", "Drafting Committee Composition", "Recall number of Drafting Committee members."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-008", "ch-02", "top-const-02-01",
    "How much time did the Constituent Assembly take to frame the Constitution of India?",
    ["2 years, 11 months and 18 days", "3 years, 2 months and 11 days", "1 year, 11 months and 28 days", "2 years, 9 months and 15 days"],
    0,
    "The Constituent Assembly held 11 sessions covering a total duration of 2 years, 11 months, and 18 days between 9th December 1946 and 26th November 1949.",
    {"A": "Correct. 2 years, 11 months, 18 days.", "B": "Incorrect duration.", "C": "Incorrect duration.", "D": "Incorrect duration."},
    "Easy", "Constituent Assembly Records", "Recall duration of constitutional drafting."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-009", "ch-02", "top-const-02-01",
    "Which provisions of the Constitution came into immediate force on 26th November 1949 (date of adoption)?",
    ["Fundamental Rights (Articles 14 to 32)", "Directive Principles of State Policy (Articles 36 to 51)", "Citizenship (Articles 5-9), Elections (Article 324), and Provisional Parliament", "Emergency Provisions (Articles 352 to 360)"],
    2,
    "Under Article 394, Articles 5, 6, 7, 8, 9, 60, 324, 366, 367, 379, 380, 388, 391, 392, and 393 came into force immediately on 26th November 1949; the remaining provisions came into force on 26th January 1950.",
    {"A": "Fundamental rights commenced on 26 January 1950.", "B": "DPSP commenced on 26 January 1950.", "C": "Correct. Citizenship, Elections, and Provisional Parliament commenced immediately on 26 Nov 1949.", "D": "Emergency provisions commenced on 26 January 1950."},
    "Hard", "Article 394", "Identify provisions commencing on 26 November 1949."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-010", "ch-02", "top-const-02-01",
    "Who was the calligrapher of the original Hindi and English handwritten copies of the Constitution of India?",
    ["Nandalal Bose", "Prem Behari Narain Raizada", "Beohar Rammanohar Sinha", "K.M. Munshi"],
    1,
    "Prem Behari Narain Raizada was the calligrapher of the original handwritten English text of the Constitution, written in flowing italic style. Nandalal Bose and Rammanohar Sinha decorated the pages.",
    {"A": "Nandalal Bose was the master artist who decorated the pages.", "B": "Correct. Prem Behari Narain Raizada was the calligrapher.", "C": "Rammanohar Sinha illuminated the Preamble page.", "D": "K.M. Munshi was a drafting committee member."},
    "Medium", "Constituent Assembly Art Records", "Recall calligrapher of original Constitution."
))

# 02-11 to 02-20: Sources of the Constitution
MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-011", "ch-02", "top-const-02-02",
    "The concept of 'Directive Principles of State Policy' was borrowed from the Constitution of:",
    ["USSR", "USA", "Ireland", "Australia"],
    2,
    "Directive Principles of State Policy in Part IV were borrowed from the 1937 Constitution of Ireland (which had in turn copied them from the Spanish Constitution).",
    {"A": "USSR inspired Fundamental Duties and Planning.", "B": "USA inspired Fundamental Rights and Judicial Review.", "C": "Correct. Ireland inspired DPSP.", "D": "Australia inspired Concurrent List."},
    "Easy", "Part IV Genesis", "Identify source of DPSP."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-012", "ch-02", "top-const-02-02",
    "The procedure for 'Amendment of the Constitution' and election of members of Rajya Sabha were borrowed from:",
    ["South Africa", "Canada", "Germany (Weimar)", "Japan"],
    0,
    "Article 368 amendment procedure and the election of members of the Rajya Sabha were borrowed from the Constitution of South Africa.",
    {"A": "Correct. South Africa provided the amendment procedure.", "B": "Canada inspired strong center federalism.", "C": "Weimar Germany inspired suspension of FRs in emergency.", "D": "Japan inspired procedure established by law."},
    "Medium", "Article 368 Genesis", "Identify source of constitutional amendment."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-013", "ch-02", "top-const-02-02",
    "The 'Concurrent List' and the provision for 'Joint Sitting of Parliament' were borrowed from:",
    ["Canada", "Australia", "United Kingdom", "United States"],
    1,
    "The Concurrent List (Seventh Schedule), freedom of trade and commerce (Part XIII), and Joint Sitting of both Houses of Parliament (Article 108) were borrowed from the Australian Constitution.",
    {"A": "Canada provided advisory jurisdiction and residuary powers in Centre.", "B": "Correct. Australia provided Concurrent List and Joint Sitting.", "C": "UK provided parliamentary system and rule of law.", "D": "USA provided impeachment and independent judiciary."},
    "Medium", "Article 108 Genesis", "Identify Australian borrowed features."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-014", "ch-02", "top-const-02-02",
    "The phrase 'Procedure Established by Law' under Article 21 was borrowed from the Constitution of:",
    ["United States of America", "United Kingdom", "Japan", "France"],
    2,
    "Article 21 adopted 'procedure established by law' from Article 31 of the 1946 Japanese Constitution on the specific advice of Justice Felix Frankfurter of the US Supreme Court to Sir B.N. Rau.",
    {"A": "USA has due process of law.", "B": "UK follows parliamentary sovereignty.", "C": "Correct. Japan was the source of procedure established by law.", "D": "France provided ideals of Liberty, Equality, Fraternity."},
    "Hard", "Article 21 Genesis", "Identify Japanese constitutional source."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-015", "ch-02", "top-const-02-02",
    "From which Constitution was the idea of 'Residual Powers vested in the Centre' and a 'Federation with a Strong Centre' adopted?",
    ["United States of America", "Canada", "Australia", "Switzerland"],
    1,
    "The Indian federal model—a federation with a strong Centre, vesting residuary powers in the Union (Article 248), and appointment of State Governors by the Centre—was borrowed from the Canadian Constitution.",
    {"A": "USA gives residuary powers to the States.", "B": "Correct. Canada provided strong Centre and residuary power model.", "C": "Australia has coordinate federalism.", "D": "Switzerland is a confederation."},
    "Medium", "Federal Structure Genesis", "Identify Canadian federal features."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-016", "ch-02", "top-const-02-02",
    "The ideals of 'Liberty, Equality and Fraternity' in the Preamble were borrowed from the:",
    ["American Declaration of Independence", "Russian Revolution (1917)", "French Revolution (1789)", "Glorious Revolution (1688)"],
    2,
    "The ideals of Liberty, Equality, and Fraternity enshrined in the Preamble were inspired by the motto of the French Revolution (1789). Ideals of Justice (Social, Economic, Political) were borrowed from the Russian Revolution (1917).",
    {"A": "American Revolution gave inalienable life, liberty, pursuit of happiness.", "B": "Russian Revolution gave Justice: Social, Economic, Political.", "C": "Correct. French Revolution gave Liberty, Equality, Fraternity.", "D": "Glorious Revolution established parliamentary supremacy in England."},
    "Easy", "Preamble Genesis", "Trace French origin of liberty, equality, fraternity."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-017", "ch-02", "top-const-02-02",
    "The concept of 'Fundamental Duties' in Part IVA was inspired by the Constitution of:",
    ["USA", "Former USSR (Soviet Union)", "Ireland", "Germany"],
    1,
    "Fundamental Duties (Article 51A) were inspired by the Constitution of the erstwhile USSR, which uniquely emphasized the correspondence between citizen duties and socialist rights.",
    {"A": "US Constitution has no charter of duties.", "B": "Correct. USSR inspired Fundamental Duties.", "C": "Ireland inspired DPSP.", "D": "Germany inspired emergency provisions."},
    "Easy", "Part IVA Genesis", "Identify USSR source of Fundamental Duties."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-018", "ch-02", "top-const-02-02",
    "Which of the following features was NOT borrowed from the British Constitution?",
    ["Parliamentary form of government", "Cabinet system and Rule of Law", "Prerogative writs", "Judicial Review and independence of the judiciary"],
    3,
    "Judicial Review and the independence of the judiciary were borrowed from the Constitution of the United States of America. Britain follows parliamentary supremacy without judicial review of primary legislation.",
    {"A": "Parliamentary form is British.", "B": "Cabinet and Rule of Law are British.", "C": "Prerogative writs are British.", "D": "Correct. Judicial Review is American, not British."},
    "Medium", "Comparative Constitutional Law", "Differentiate British from American borrowed concepts."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-019", "ch-02", "top-const-02-02",
    "Suspension of Fundamental Rights during an Emergency was borrowed from:",
    ["Government of India Act, 1935", "Weimar Constitution of Germany", "Constitution of South Africa", "Irish Constitution"],
    1,
    "The provision relating to the suspension of the enforcement of fundamental rights during an emergency (Article 359) was borrowed from the Weimar Constitution of Germany.",
    {"A": "1935 Act provided emergency machinery, but suspension of FRs came from Weimar.", "B": "Correct. Weimar Constitution of Germany inspired suspension of rights.", "C": "South Africa inspired amendments.", "D": "Ireland inspired DPSP."},
    "Medium", "Emergency Genesis", "Identify German Weimar origin of emergency rights suspension."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-020", "ch-02", "top-const-02-02",
    "From which statute is approximately 60% of the administrative and structural provisions of the Indian Constitution directly derived?",
    ["Government of India Act, 1919", "Government of India Act, 1935", "Indian Independence Act, 1947", "Indian Councils Act, 1909"],
    1,
    "The Government of India Act, 1935 provided the primary structural framework: federal scheme, office of governor, judiciary, public service commissions, emergency provisions, and administrative details.",
    {"A": "1919 provided provincial dyarchy.", "B": "Correct. 1935 Act was the structural backbone.", "C": "1947 was transitional.", "D": "1909 was imperial."},
    "Easy", "Structural Blueprint", "Recall 1935 Act dominance in Constitution."
))

# 02-21 to 02-30: Salient Features
MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-021", "ch-02", "top-const-02-03",
    "Who famously characterized the Indian Constitution as 'Quasi-Federal'?",
    ["Sir Ivor Jennings", "Prof. K.C. Wheare", "Granville Austin", "Morris-Jones"],
    1,
    "Prof. K.C. Wheare described the Indian Constitution as 'quasi-federal'—a unitary state with subsidiary federal features rather than a federal state with subsidiary unitary features.",
    {"A": "Sir Ivor Jennings called it a lawyer's paradise and federation with strong centralising tendency.", "B": "Correct. Prof. K.C. Wheare coined quasi-federal.", "C": "Granville Austin called it cooperative federalism.", "D": "Morris-Jones called it bargaining federalism."},
    "Easy", "Federal Character Jurisprudence", "Recall K.C. Wheare's quasi-federal characterization."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-022", "ch-02", "top-const-02-03",
    "Who described the Fundamental Rights and Directive Principles of State Policy as the 'Conscience of the Constitution'?",
    ["Dr. B.R. Ambedkar", "Granville Austin", "K.M. Munshi", "Sir Alladi Krishnaswami Iyer"],
    1,
    "Renowned constitutional historian Granville Austin characterized Fundamental Rights (Part III) and Directive Principles of State Policy (Part IV) as the 'Conscience of the Constitution'.",
    {"A": "Dr. Ambedkar called Article 32 the heart and soul.", "B": "Correct. Granville Austin called Parts III & IV the Conscience of the Constitution.", "C": "K.M. Munshi called the Preamble the political horoscope.", "D": "Alladi was a drafting architect."},
    "Medium", "Constitutional Philosophy", "Identify Granville Austin's conscience phrase."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-023", "ch-02", "top-const-02-03",
    "The synthesis of 'Parliamentary Sovereignty' and 'Judicial Supremacy' in India represents a blend of:",
    ["British parliamentary supremacy and American judicial supremacy", "French presidentialism and Swiss referendum", "Canadian federalism and Australian commerce", "Irish directives and Russian planning"],
    0,
    "The Indian constitutional framework uniquely synthesizes the British principle of parliamentary sovereignty (limited by written constitution and fundamental rights) and the American principle of judicial supremacy (curbed by legislative amendments).",
    {"A": "Correct. Blend of British Parliamentary Sovereignty and American Judicial Supremacy.", "B": "India has neither French semi-presidentialism nor Swiss direct democracy.", "C": "Australia/Canada influenced specific clauses, not sovereignty synthesis.", "D": "Ideological sources."},
    "Medium", "Constitutional Architecture", "Understand synthesis of sovereignty and judicial review."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-024", "ch-02", "top-const-02-03",
    "Which Constitutional Amendment lowered the voting age for elections to the Lok Sabha and State Legislative Assemblies from 21 years to 18 years?",
    ["42nd Amendment Act, 1976", "44th Amendment Act, 1978", "61st Amendment Act, 1988", "73rd Amendment Act, 1992"],
    2,
    "The 61st Constitutional Amendment Act, 1988 (which came into force in 1989) amended Article 326 to lower the voting age from 21 years to 18 years.",
    {"A": "42nd Amendment was mini-constitution.", "B": "44th Amendment restored civil liberties.", "C": "Correct. 61st Amendment Act 1988 reduced voting age to 18.", "D": "73rd Amendment constitutionalized Panchayats."},
    "Easy", "Article 326 & 61st Amendment", "Recall voting age reduction amendment."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-025", "ch-02", "top-const-02-03",
    "How many Schedules did the Constitution of India contain at the time of its commencement in 1950?",
    ["Eight", "Ten", "Twelve", "Seven"],
    0,
    "The original Constitution of India consisted of a Preamble, 395 Articles divided into 22 Parts, and 8 Schedules. Today it has 12 Schedules.",
    {"A": "Correct. Exactly eight Schedules originally.", "B": "Ten is incorrect (Tenth added in 1985).", "C": "Twelve is current count.", "D": "Seven is incorrect."},
    "Easy", "Commencement Baseline", "Recall original number of Schedules."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-026", "ch-02", "top-const-02-03",
    "Which of the following is NOT a unitary feature of the Indian Constitution?",
    ["Single Citizenship", "Integrated Judiciary", "Bicameral Legislature", "Appointment of State Governor by the Centre"],
    2,
    "A Bicameral Legislature (Council of States and House of the People) is a classic FEDERAL feature ensuring territorial representation of States. Single citizenship, integrated judiciary, and Governor appointment are unitary/centralizing features.",
    {"A": "Single citizenship is a unitary feature.", "B": "Integrated judiciary is a unitary feature.", "C": "Correct. Bicameralism is a federal feature.", "D": "Governor appointment by Centre is a unitary feature."},
    "Medium", "Federal vs Unitary Classification", "Classify federal and unitary constitutional traits."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-027", "ch-02", "top-const-02-03",
    "The Indian Constitution is characterized as 'flexible as well as rigid' because:",
    ["It can only be amended by simple majority", "Some provisions can be amended by simple majority outside Art. 368, while others require special majority and state ratification", "It can never be amended without a referendum", "It requires approval of the Supreme Court for every amendment"],
    1,
    "The Constitution strikes a delicate balance between rigidity (like USA) and flexibility (like UK): some provisions require only a simple majority outside Art. 368, while others require special majorities or state ratifications under Art. 368.",
    {"A": "Simple majority applies only to limited provisions.", "B": "Correct. Combines simple, special, and state ratification amendment procedures.", "C": "India has no referendum provision.", "D": "Supreme Court reviews amendments only on challenge."},
    "Medium", "Article 368 Synthesis", "Explain balance between flexibility and rigidity."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-028", "ch-02", "top-const-02-03",
    "Which case established that 'Secularism' is an essential part of the Basic Structure of the Indian Constitution?",
    ["Kesavananda Bharati v. State of Kerala (1973)", "S.R. Bommai v. Union of India (1994)", "Minerva Mills v. Union of India (1980)", "Indira Nehru Gandhi v. Raj Narain (1975)"],
    1,
    "While Kesavananda recognized secular character, the 9-Judge Bench in S.R. Bommai v. Union of India (1994) unequivocally cemented Secularism as an inviolable Basic Feature of the Constitution.",
    {"A": "Kesavananda noted secular character among basic elements.", "B": "Correct. S.R. Bommai definitively ruled secularism is basic structure.", "C": "Minerva Mills emphasized balance between rights and directives.", "D": "Indira Gandhi struck down election immunity."},
    "Medium", "Secularism Jurisprudence", "Identify definitive secularism basic structure authority."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-029", "ch-02", "top-const-02-03",
    "The concept of an 'Integrated Judiciary' in India implies:",
    ["A single system of courts enforcing both Central and State laws throughout the country", "Judges are appointed by the executive without consultation", "Judiciary is subordinate to the Parliament", "Courts have no power of judicial review"],
    0,
    "Unlike the United States (where federal courts enforce federal laws and state courts enforce state laws), India has an integrated hierarchy of courts where the Supreme Court at the apex and High Courts below it enforce both Union and State laws.",
    {"A": "Correct. Single integrated system enforcing both Central and State laws.", "B": "Judges are appointed through collegium.", "C": "Judiciary is independent, not subordinate.", "D": "Judicial review is an active power."},
    "Medium", "Judicial Hierarchy Concept", "Explain meaning of integrated judiciary in India."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-02-030", "ch-02", "top-const-02-03",
    "Who described the Preamble as the 'Horoscope of our Sovereign, Democratic Republic'?",
    ["Dr. B.R. Ambedkar", "Dr. K.M. Munshi", "Pandit Thakur Das Bhargava", "N.A. Palkhivala"],
    1,
    "Dr. K.M. Munshi, a member of the Drafting Committee, described the Preamble as the 'Horoscope of our Sovereign, Democratic Republic'. N.A. Palkhivala termed it the 'Identity Card of the Constitution'.",
    {"A": "Dr. Ambedkar drafted the core articles.", "B": "Correct. Dr. K.M. Munshi termed it the political horoscope.", "C": "Thakur Das Bhargava called it the soul and jewel of the Constitution.", "D": "N.A. Palkhivala called it the identity card."},
    "Medium", "Preamble Epigrams", "Recall author of horoscope description."
))

# ==============================================================================
# CHAPTER 3: THE PREAMBLE (25 MCQs)
# ==============================================================================
# 03-01 to 03-12: Text & Ideals
MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-001", "ch-03", "top-const-03-01",
    "What is the exact chronological sequence of the opening words describing India's status in the Preamble today?",
    ["Sovereign, Democratic, Republic, Socialist, Secular", "Sovereign, Socialist, Secular, Democratic, Republic", "Socialist, Secular, Sovereign, Democratic, Republic", "Sovereign, Secular, Socialist, Democratic, Republic"],
    1,
    "The opening operative declaration reads: 'SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC'. ('Socialist' and 'Secular' were inserted between Sovereign and Democratic by 42nd Amendment).",
    {"A": "Incorrect order.", "B": "Correct. Sovereign, Socialist, Secular, Democratic, Republic (SO-SO-SE-DE-RE).", "C": "Incorrect order.", "D": "Incorrect order (Secular precedes Socialist is false)."},
    "Easy", "Preamble Opening Phrase", "Recall exact text sequence of Preamble."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-002", "ch-03", "top-const-03-01",
    "Which three words were added to the Preamble by the 42nd Constitutional Amendment Act, 1976?",
    ["Socialist, Secular, Integrity", "Socialist, Democratic, Republic", "Liberty, Equality, Fraternity", "Sovereign, Secular, Unity"],
    0,
    "The 42nd Amendment Act, 1976 amended the Preamble to add 'Socialist' and 'Secular' to the description of the Republic, and changed 'unity of the Nation' to 'unity and integrity of the Nation'.",
    {"A": "Correct. Socialist, Secular, and Integrity were added.", "B": "Democratic and Republic were part of original 1950 text.", "C": "Liberty, Equality, Fraternity were in original 1950 text.", "D": "Sovereign and Unity were in original 1950 text."},
    "Easy", "42nd Amendment Act, 1976", "Identify words added by 42nd Amendment."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-003", "ch-03", "top-const-03-01",
    "How many types of 'Justice' are secured to all citizens by the Preamble?",
    ["Two: Legal and Political", "Three: Social, Economic, and Political", "Four: Civil, Criminal, Social, and Moral", "Single universal justice"],
    1,
    "The Preamble secures 'JUSTICE, social, economic and political', in that precise order, reflecting the social and economic goals of the welfare state inspired by the 1917 Russian Revolution.",
    {"A": "Legal justice is not mentioned explicitly in the Preamble.", "B": "Correct. Three types: Social, Economic, and Political.", "C": "Four types is incorrect.", "D": "Single is incorrect."},
    "Easy", "Preamble Justice Dimensions", "Recall three dimensions of Justice in Preamble."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-004", "ch-03", "top-const-03-01",
    "What are the five dimensions of 'Liberty' guaranteed in the Preamble?",
    ["Speech, Expression, Belief, Trade, Commerce", "Thought, Expression, Belief, Faith, and Worship", "Life, Liberty, Property, Speech, Religion", "Movement, Residence, Profession, Thought, Assembly"],
    1,
    "The Preamble explicitly guarantees 'LIBERTY of thought, expression, belief, faith and worship'.",
    {"A": "Trade and commerce are Article 19(1)(g)/Part XIII rights.", "B": "Correct. Thought, Expression, Belief, Faith, and Worship.", "C": "Life and property are substantive rights.", "D": "Movement and residence are Art. 19 freedoms."},
    "Easy", "Preamble Liberty Dimensions", "Recall five dimensions of Liberty in Preamble."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-005", "ch-03", "top-const-03-01",
    "What two forms of 'Equality' are secured to all citizens in the Preamble?",
    ["Equality of income and property", "Equality of status and of opportunity", "Equality of voting and taxation", "Equality of religion and race"],
    1,
    "The Preamble secures 'EQUALITY of status and of opportunity; and to promote among them all'.",
    {"A": "Income equality is a DPSP ideal (Art. 39), not in Preamble text.", "B": "Correct. Status and of opportunity.", "C": "Voting equality is Art. 326.", "D": "Religion/race equality is Art. 15."},
    "Easy", "Preamble Equality Dimensions", "Recall two forms of Equality in Preamble."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-006", "ch-03", "top-const-03-01",
    "What is the date of adoption of the Constitution mentioned in the Preamble?",
    ["26th day of January, 1950", "26th day of November, 1949", "15th day of August, 1947", "9th day of December, 1946"],
    1,
    "The enacting clause concludes: 'IN OUR CONSTITUENT ASSEMBLY this twenty-sixth day of November, 1949, do HEREBY ADOPT, ENACT AND GIVE TO OURSELVES THIS CONSTITUTION'.",
    {"A": "26th January 1950 was the date of commencement.", "B": "Correct. 26th November 1949 was date of adoption.", "C": "15th August 1947 was independence.", "D": "9th December 1946 was first assembly meeting."},
    "Easy", "Preamble Enacting Clause", "Distinguish adoption date from commencement date."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-007", "ch-03", "top-const-03-01",
    "From where does the Constitution of India derive its ultimate sovereign authority?",
    ["The Parliament of India", "The President of India", "The People of India", "The Supreme Court of India"],
    2,
    "The opening words 'WE, THE PEOPLE OF INDIA... ADOPT, ENACT AND GIVE TO OURSELVES THIS CONSTITUTION' signify that ultimate political sovereignty resides in the people of India.",
    {"A": "Parliament is a creature of the Constitution.", "B": "President is constitutional executive head.", "C": "Correct. The People of India.", "D": "Supreme Court is creature and guardian of Constitution."},
    "Easy", "Popular Sovereignty Doctrine", "Identify source of constitutional authority."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-008", "ch-03", "top-const-03-01",
    "What form of socialism does the Indian Constitution adopt as clarified in D.S. Nakara v. Union of India?",
    ["Marxist state socialism requiring total nationalization", "Democratic socialism aiming to end poverty, ignorance, disease, and inequality of opportunity", "Communist dictatorship of the proletariat", "Syndicalist guild socialism"],
    1,
    "In D.S. Nakara v. UOI (1983), the Supreme Court held that Indian socialism is 'Democratic Socialism'—a blend of Marxism and Gandhism leaning heavily towards Gandhian socialism, aiming to eliminate poverty and inequality without abolishing private enterprise.",
    {"A": "India does not follow Marxist total nationalization.", "B": "Correct. Democratic socialism with Gandhian blend.", "C": "Communist dictatorship is antithetical to democracy.", "D": "Syndicalism is not adopted."},
    "Medium", "D.S. Nakara v. Union of India (1983)", "Define Indian democratic socialism."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-009", "ch-03", "top-const-03-01",
    "In which case did the Supreme Court observe that 'Secularism in the Indian Constitution means that all religions receive equal respect and protection from the State (Sarva Dharma Sambhava)'?",
    ["St. Xavier's College v. State of Gujarat (1974)", "S.R. Bommai v. Union of India (1994)", "Indira Nehru Gandhi v. Raj Narain (1975)", "Aruna Roy v. Union of India (2002)"],
    0,
    "In St. Xavier's College (1974), the Supreme Court explained that secularism in India is neither anti-God nor pro-God; it treats devout, agnostic, and atheist alike and accords equal freedom and respect to all faiths (positive secularism).",
    {"A": "Correct. St. Xavier's College articulated positive secularism.", "B": "Bommai cemented secularism as basic structure.", "C": "Indira Gandhi struck down election immunity.", "D": "Aruna Roy upheld study of comparative religions."},
    "Hard", "Positive Secularism Jurisprudence", "Analyze positive secularism in Indian constitutional law."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-010", "ch-03", "top-const-03-01",
    "Who called the Preamble the 'Key to the Constitution' and 'Jewel set in the Constitution'?",
    ["Pandit Thakur Das Bhargava", "N.A. Palkhivala", "Justice M. Hidayatullah", "Sir Ernest Barker"],
    0,
    "Pandit Thakur Das Bhargava declared: 'The Preamble is the most precious part of the Constitution. It is the soul of the Constitution. It is a key to the Constitution. It is a proper yardstick with which one can measure the worth of the Constitution.'",
    {"A": "Correct. Pandit Thakur Das Bhargava.", "B": "Palkhivala called it identity card.", "C": "Hidayatullah compared it to US Declaration of Independence.", "D": "Barker praised it as a key principle of social and political theory."},
    "Medium", "Preamble Appraisal Quotes", "Attribute famous Preamble praises."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-011", "ch-03", "top-const-03-01",
    "English political theorist Sir Ernest Barker was so impressed by the Preamble of the Indian Constitution that he quoted it at the opening of his book:",
    ["Principles of Social and Political Theory (1951)", "The Law of the Constitution", "Representative Government", "Modern Democracies"],
    0,
    "Sir Ernest Barker quoted the Preamble of the Indian Constitution on the opening page of his celebrated treatise 'Principles of Social and Political Theory' (1951), noting that it states in condensed form the essential principles of modern politics.",
    {"A": "Correct. Principles of Social and Political Theory (1951).", "B": "A.V. Dicey wrote Law of the Constitution.", "C": "J.S. Mill wrote Representative Government.", "D": "Lord Bryce wrote Modern Democracies."},
    "Hard", "Barker's Tribute", "Recall international scholarly acclaim of Preamble."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-012", "ch-03", "top-const-03-01",
    "What does the term 'Republic' signify in the Indian Preamble?",
    ["The executive head of the state is hereditary", "The head of the state (President) is always elected, directly or indirectly, for a fixed term, and all public offices are open to every citizen without discrimination", "Parliament has unlimited sovereign powers", "The judiciary is supreme over executive"],
    1,
    "A Republic denotes a political system where the head of state is not hereditary (like a monarchy) but elected by the people for a fixed period, and where political sovereignty is vested in the people without any privileged class.",
    {"A": "Hereditary head is a Monarchy (e.g. UK).", "B": "Correct. Elected head of state and open public offices.", "C": "Parliamentary sovereignty is British, not republican per se.", "D": "Judicial review is a separate constitutional check."},
    "Easy", "Republican Form of Government", "Define Republic in constitutional context."
))

# 03-13 to 03-25: Status & Amendability
MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-013", "ch-03", "top-const-03-02",
    "In which advisory reference did the Supreme Court hold that the Preamble is 'NOT a part of the Constitution'?",
    ["In re Berubari Union (1960)", "In re Kerala Education Bill (1958)", "In re Delhi Laws Act (1951)", "In re Special Courts Bill (1978)"],
    0,
    "In In re Berubari Union (1960), an 8-Judge Bench held that the Preamble is a key to the minds of the makers, but it is NOT part of the Constitution and cannot be regarded as a source of substantive powers.",
    {"A": "Correct. In re Berubari Union (1960) held Preamble is not part of Constitution.", "B": "Kerala Education Bill dealt with minority rights.", "C": "Delhi Laws Act dealt with delegated legislation.", "D": "Special Courts Bill dealt with trial of emergency offenses."},
    "Easy", "In re Berubari Union (1960) 3 SCR 250", "Recall Berubari holding on Preamble status."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-014", "ch-03", "top-const-03-02",
    "The ruling in Berubari Union (1960) that the Preamble is not part of the Constitution was expressly overruled in which landmark case?",
    ["Golaknath v. State of Punjab (1967)", "Kesavananda Bharati v. State of Kerala (1973)", "Minerva Mills v. Union of India (1980)", "Maneka Gandhi v. Union of India (1978)"],
    1,
    "In Kesavananda Bharati (1973), the majority of the 13-Judge Bench expressly overruled Berubari Union and held that the Preamble IS an integral part of the Constitution and can be amended under Article 368 without destroying its Basic Structure.",
    {"A": "Golaknath dealt with amending fundamental rights.", "B": "Correct. Kesavananda Bharati (1973) overruled Berubari.", "C": "Minerva Mills reaffirmed basic structure balance.", "D": "Maneka Gandhi expanded Article 21."},
    "Easy", "Kesavananda Bharati (1973) 4 SCC 225", "Recall overruling of Berubari."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-015", "ch-03", "top-const-03-02",
    "In which 1995 judgment did the Supreme Court reaffirm that 'the Preamble is an integral part of the Constitution'?",
    ["LIC of India v. Consumer Education & Research Centre", "S.P. Gupta v. Union of India", "Indra Sawhney v. Union of India", "Mohini Jain v. State of Karnataka"],
    0,
    "In LIC of India v. Consumer Education & Research Centre (1995), the Supreme Court once again unequivocally held that the Preamble is an integral part of the Constitution.",
    {"A": "Correct. LIC of India (1995) reaffirmed Preamble is integral part.", "B": "S.P. Gupta was First Judges Case on appointments.", "C": "Indra Sawhney was Mandal Commission case on reservations.", "D": "Mohini Jain was capitation fee case."},
    "Medium", "LIC of India v. CERC (1995) 5 SCC 482", "Reaffirm Preamble status in LIC case."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-016", "ch-03", "top-const-03-02",
    "Is the Preamble directly enforceable in a court of law (justiciable)?",
    ["Yes, under Article 32", "Yes, under Article 226", "No, the Preamble is non-justiciable and cannot be enforced directly in courts", "Yes, but only against the Central Government"],
    2,
    "The Preamble is non-justiciable: its provisions are not enforceable in courts of law, meaning no writ of mandamus can be issued solely to enforce a declaration in the Preamble without a specific constitutional or statutory provision.",
    {"A": "Article 32 enforces Part III Fundamental Rights, not Preamble per se.", "B": "Article 226 cannot enforce Preamble standalone.", "C": "Correct. Preamble is non-justiciable and unenforceable.", "D": "Cannot be enforced against any government."},
    "Medium", "Preamble Justiciability Jurisprudence", "Analyze non-justiciable nature of Preamble."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-017", "ch-03", "top-const-03-02",
    "Can the Preamble to the Constitution of India be amended under Article 368?",
    ["No, it can never be amended under any circumstances", "Yes, but the amendment must not alter or damage the Basic Structure of the Constitution", "Yes, Parliament has unlimited power to delete any word", "Only with the ratification of all State Legislatures"],
    1,
    "As held in Kesavananda Bharati (1973), the Preamble can be amended under Article 368 like any other part of the Constitution, subject to the limitation that its Basic Features (such as secularism, democracy, republic) cannot be destroyed.",
    {"A": "It was already amended by 42nd Amendment in 1976.", "B": "Correct. Amendable subject to the Basic Structure limitation.", "C": "Amending power is limited, not absolute.", "D": "State ratification is not needed unless proviso provisions are touched."},
    "Easy", "Kesavananda Bharati (1973) 4 SCC 225", "Master amendability of Preamble."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-018", "ch-03", "top-const-03-02",
    "How many times has the Preamble to the Constitution of India been amended so far?",
    ["Never", "Once", "Twice", "Three times"],
    1,
    "The Preamble has been amended only ONCE in constitutional history, by the 42nd Constitutional Amendment Act, 1976, which added 'Socialist', 'Secular', and 'Integrity'.",
    {"A": "It was amended in 1976.", "B": "Correct. Exactly once (by 42nd Amendment, 1976).", "C": "Twice is incorrect.", "D": "Three times is incorrect."},
    "Easy", "Preamble Amendment History", "Recall frequency of Preamble amendments."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-019", "ch-03", "top-const-03-02",
    "What is the primary legal utility of the Preamble in constitutional adjudication?",
    ["It confers independent substantive legislative powers on Parliament", "It acts as an interpretive compass when constitutional provisions are ambiguous or capable of two meanings", "It operates as an overriding limitation on fundamental rights", "It acts as a substitute for Directive Principles"],
    1,
    "The Preamble is an interpretive aid: where the text of an Article is clear, it prevails; but where constitutional words are ambiguous or capable of multiple constructions, that interpretation which harmonizes with the Preamble must be adopted.",
    {"A": "Preamble is neither a source of power nor a source of prohibition.", "B": "Correct. Serves as an interpretive aid for ambiguous provisions.", "C": "Cannot override explicit fundamental rights.", "D": "Does not replace DPSP."},
    "Medium", "Interpretive Role of Preamble", "Explain interpretive utility of Preamble."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-020", "ch-03", "top-const-03-02",
    "Which Justice in Kesavananda Bharati observed that 'the Preamble was enacted with the same solemnity as the rest of the Constitution'?",
    ["Justice H.R. Khanna", "Chief Justice S.M. Sikri", "Justice K.S. Hegde", "Justice A.N. Ray"],
    1,
    "Chief Justice S.M. Sikri observed that unlike the American or other Constitutions, the Preamble of the Indian Constitution was voted upon and enacted by the Constituent Assembly with the motion 'that the Preamble stand part of the Constitution', proving it is part of the Constitution.",
    {"A": "Khanna focused on basic structure doctrine.", "B": "Correct. CJI S.M. Sikri noted the assembly voting history.", "C": "Hegde concurred on basic structure.", "D": "Ray dissented in favor of unlimited amending power."},
    "Hard", "Kesavananda Bharati (1973) 4 SCC 225, para 100", "Attribute assembly enactment observation."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-021", "ch-03", "top-const-03-02",
    "Can a law enacted by Parliament be declared unconstitutional solely on the ground that it violates the Preamble?",
    ["Yes, because Preamble is the supreme law", "No, because the Preamble is not an enforceable source of substantive power or limitation in itself", "Yes, if challenged by a PIL", "Yes, by a 5-Judge Constitution Bench only"],
    1,
    "A statute cannot be declared void solely for violating the Preamble; it must violate an express provision of the Constitution or its Basic Structure (which draws from the Preamble).",
    {"A": "Preamble is not an independent substantive ground of invalidity.", "B": "Correct. Preamble is not an independent enforceable source.", "C": "PIL cannot bypass justiciability requirement.", "D": "Bench size does not change substantive rule."},
    "Medium", "Substantive Limitation Doctrine", "Understand why Preamble cannot be sole ground of invalidity."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-022", "ch-03", "top-const-03-02",
    "What was the original description of India in the Preamble before the 42nd Amendment, 1976?",
    ["Sovereign Democratic Republic", "Sovereign Socialist Republic", "Democratic Secular Republic", "Union of Sovereign States"],
    0,
    "Prior to the 42nd Amendment Act 1976, the Preamble declared India to be a 'SOVEREIGN DEMOCRATIC REPUBLIC'. The words 'Socialist' and 'Secular' were inserted in 1976.",
    {"A": "Correct. Original text was Sovereign Democratic Republic.", "B": "Socialist was added in 1976.", "C": "Secular was added in 1976.", "D": "Union of States is Article 1, not Preamble."},
    "Easy", "Pre-1976 Preamble Text", "Recall original 1950 Preamble text."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-023", "ch-03", "top-const-03-02",
    "In Kesavananda Bharati, which test was laid down to determine whether a constitutional amendment violates the Preamble?",
    ["The legislative motive test", "The basic structure test (whether the identity or essential features reflected in the Preamble are damaged)", "The proportionality test", "The strict scrutiny test"],
    1,
    "The Supreme Court laid down that an amendment to the Preamble or under Article 368 is valid as long as it does not destroy the essential identity or Basic Structure of the Constitution as outlined in the Preamble.",
    {"A": "Legislative motive is irrelevant to constitutional validity.", "B": "Correct. Basic Structure test determines whether essential identity is damaged.", "C": "Proportionality applies to fundamental rights restrictions.", "D": "Strict scrutiny applies to discrimination."},
    "Medium", "Basic Structure Touchstone", "Connect Preamble to Basic Structure test."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-024", "ch-03", "top-const-03-02",
    "Which of the following statements regarding the Preamble is INCORRECT?",
    ["The Preamble is a source of power to the legislature", "The Preamble is a part of the Constitution", "The Preamble was adopted after the rest of the Constitution was already enacted", "The Preamble can be amended under Article 368"],
    0,
    "The statement that 'The Preamble is a source of power to the legislature' is INCORRECT. The Preamble is NEITHER a source of power to legislature NOR a source of prohibition upon the powers of legislature.",
    {"A": "Correct (this statement is false, hence the correct answer). Preamble is NOT a source of power.", "B": "True statement (Kesavananda Bharati).", "C": "True statement (voted upon at the end of the drafting to ensure conformity).", "D": "True statement (amendable under Art. 368)."},
    "Medium", "Preamble Characteristics", "Identify false statement regarding Preamble."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-03-025", "ch-03", "top-const-03-02",
    "Why did the Constituent Assembly enact the Preamble at the very end of its proceedings on 17th October 1949?",
    ["Because it was forgotten earlier", "To ensure that the Preamble conformed with and reflected the provisions of the Constitution as finally settled", "Because British assent was pending", "Due to disagreement on adult suffrage"],
    1,
    "The President of the Constituent Assembly postponed the consideration of the Preamble until all other Articles had been adopted, to ensure that the Preamble was in perfect harmony with the text of the Constitution as finalized.",
    {"A": "It was carefully planned, not forgotten.", "B": "Correct. To ensure total conformity with the finalized constitutional text.", "C": "British assent was irrelevant post-Independence.", "D": "Universal adult franchise was agreed early."},
    "Medium", "Constituent Assembly Procedure", "Understand why Preamble was adopted last."
))

# ==============================================================================
# CHAPTER 4: THE UNION AND ITS TERRITORY (25 MCQs)
# ==============================================================================
# 04-01 to 04-12: Articles 1 & 2
MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-001", "ch-04", "top-const-04-01",
    "Article 1 of the Constitution describes India as:",
    ["A Federation of States", "A Confederation of States", "A Union of States", "A Unitary Republic"],
    2,
    "Article 1(1) of the Constitution states: 'India, that is Bharat, shall be a Union of States'. Dr. Ambedkar explained that 'Union of States' was preferred over 'Federation of States' because the Indian federation is not the result of an agreement among the States, and no State has the right to secede.",
    {"A": "Federation of States was intentionally avoided.", "B": "Confederation is a loose league of sovereign states.", "C": "Correct. Article 1(1) declares India a 'Union of States'.", "D": "Unitary Republic ignores federal distribution."},
    "Easy", "Article 1(1)", "Recall constitutional description of India."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-002", "ch-04", "top-const-04-01",
    "According to Article 1(3), the 'Territory of India' comprises:",
    ["Only the territories of the States", "Territories of States and Union Territories only", "Territories of States, Union Territories, and such other territories as may be acquired", "The landmass excluding territorial waters"],
    2,
    "Under Article 1(3), the territory of India comprises: (a) territories of the States; (b) Union territories specified in the First Schedule; and (c) such other territories as may be acquired by India at any time.",
    {"A": "Excludes UTs and acquired territories.", "B": "Excludes acquired territories.", "C": "Correct. States + UTs + Acquired Territories.", "D": "Territorial waters are part of territory."},
    "Medium", "Article 1(3)", "Analyze components of Territory of India."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-003", "ch-04", "top-const-04-01",
    "What is the difference between the 'Union of India' and the 'Territory of India'?",
    ["There is no constitutional difference", "'Union of India' includes only the States sharing federal power, whereas 'Territory of India' is wider and includes States, UTs, and acquired territories", "'Territory of India' includes only mainland territories", "'Union of India' includes all embassies abroad"],
    1,
    "'Territory of India' is a wider geographical expression than 'Union of India'. The 'Union' includes only the 28 States that are members of the federal system sharing power with the Centre, while the 'Territory' includes the States, Union Territories, and any acquired territories.",
    {"A": "Significant legal difference exists.", "B": "Correct. Territory is wider than Union.", "C": "Territory includes islands and waters.", "D": "Embassies are extraterritorial fiction."},
    "Medium", "Article 1 Jurisprudence", "Distinguish Union of India from Territory of India."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-004", "ch-04", "top-const-04-01",
    "Article 2 of the Constitution empowers Parliament to:",
    ["Alter boundaries of existing States", "Admit into the Union, or establish, new States on such terms and conditions as it thinks fit", "Change the name of an existing State", "Cede Indian territory to a foreign power"],
    1,
    "Article 2 relates to the admission or establishment of new States that were NOT previously part of India (e.g. Sikkim), empowering Parliament by law to admit them into the Union on terms it thinks fit. Alteration of existing States falls under Article 3.",
    {"A": "Alteration of existing states is Article 3.", "B": "Correct. Article 2 deals with admission/establishment of new external states.", "C": "Name change of existing state is Article 3.", "D": "Cession requires Article 368 amendment (Berubari)."},
    "Medium", "Article 2", "Distinguish Article 2 from Article 3."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-005", "ch-04", "top-const-04-01",
    "Sikkim was initially conferred the status of an 'Associate State' by which Constitutional Amendment?",
    ["35th Amendment Act, 1974", "36th Amendment Act, 1975", "42nd Amendment Act, 1976", "44th Amendment Act, 1978"],
    0,
    "The 35th Constitutional Amendment Act, 1974 introduced Article 2A and the Tenth Schedule (original) making Sikkim an 'Associate State'. Subsequently, the 36th Amendment Act, 1975 made Sikkim a full-fledged 22nd State of the Indian Union and repealed Article 2A.",
    {"A": "Correct. 35th Amendment 1974 created Associate State status.", "B": "36th Amendment 1975 made Sikkim a full State.", "C": "42nd Amendment was mini-constitution.", "D": "44th Amendment restored liberties."},
    "Medium", "35th and 36th Amendment Acts", "Trace Sikkim's constitutional integration."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-006", "ch-04", "top-const-04-01",
    "The phrase 'India is an indestructible Union of destructible States' signifies that:",
    ["States cannot secede from the Union, and Parliament can alter state boundaries or extinguish a state without its consent", "States can secede by a referendum", "Neither the Union nor the States can alter boundaries", "States can dissolve the Central Government"],
    0,
    "Unlike the USA (which is an indestructible Union of indestructible States), India is an indestructible Union of destructible States: the Union cannot be destroyed or seceded from, but Parliament under Article 3 can redraw state boundaries or extinguish states without their consent.",
    {"A": "Correct. Indestructible Union of destructible States.", "B": "Secession is unconstitutional.", "C": "States are destructible by Parliament.", "D": "States cannot dissolve the Union."},
    "Medium", "Constitutional Federal Nature", "Explain indestructible union of destructible states."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-007", "ch-04", "top-const-04-01",
    "In which case did the Supreme Court hold that the terms and conditions on which a new State is admitted under Article 2 cannot violate the Basic Structure?",
    ["R.C. Poudyal v. Union of India (1994)", "Kesavananda Bharati v. State of Kerala (1973)", "State of West Bengal v. Union of India (1963)", "In re Berubari Union (1960)"],
    0,
    "In R.C. Poudyal v. UOI (1994), the Supreme Court held that while Parliament has wide discretion under Article 2 to admit new States, the terms and conditions must conform to the foundational scheme and cannot violate the Basic Structure.",
    {"A": "Correct. R.C. Poudyal v. Union of India (1994) (Sikkim assembly reservations).", "B": "Kesavananda established general basic structure.", "C": "State of W.B. dealt with Coal Bearing Areas Act and federalism.", "D": "Berubari dealt with boundary cession."},
    "Hard", "R.C. Poudyal v. Union of India (1994) Supp (1) SCC 324", "Examine judicial limits on Article 2."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-008", "ch-04", "top-const-04-01",
    "Can an Indian State secede from the Union of India?",
    ["Yes, with 2/3rd majority of the State Assembly", "Yes, with the approval of the Supreme Court", "No, the Indian Union is indestructible and no State has the constitutional right to secede", "Yes, under the United Nations charter"],
    2,
    "The Indian Constitution does not recognize any right of secession. India is an indestructible Union; any attempt at secession is unconstitutional and penalized under law (UAPA and 16th Amendment).",
    {"A": "State assembly has no secession power.", "B": "Supreme Court cannot permit secession.", "C": "Correct. No constitutional right of secession exists.", "D": "UN charter does not apply to sovereign internal integrity."},
    "Easy", "Article 1 Non-Secession Principle", "Affirm territorial integrity of Union."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-009", "ch-04", "top-const-04-01",
    "How many States and Union Territories are there in India currently (post Jammu & Kashmir Reorganisation and Dadra & Nagar Haveli merger)?",
    ["28 States and 8 Union Territories", "29 States and 7 Union Territories", "28 States and 9 Union Territories", "29 States and 8 Union Territories"],
    0,
    "Currently, India consists of 28 States and 8 Union Territories following the reorganisation of Jammu and Kashmir into two UTs (J&K and Ladakh) in 2019 and the merger of Dadra & Nagar Haveli and Daman & Diu in 2020.",
    {"A": "Correct. 28 States and 8 Union Territories.", "B": "Outdated (pre-2019 count).", "C": "Outdated (before Dadra/Daman merger).", "D": "Incorrect state count."},
    "Easy", "First Schedule Current Baseline", "Recall current counts of States and UTs."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-010", "ch-04", "top-const-04-01",
    "Which Article of the Constitution deals with the name and territory of the Union?",
    ["Article 1", "Article 2", "Article 3", "Article 4"],
    0,
    "Article 1 of the Constitution is titled 'Name and territory of the Union' and sets out the official names 'India, that is Bharat' and the territorial categories.",
    {"A": "Correct. Article 1.", "B": "Article 2 is admission of new states.", "C": "Article 3 is formation of new states.", "D": "Article 4 is supplemental laws."},
    "Easy", "Article 1", "Identify Article 1 title."
))

# 04-11 to 04-25: Articles 3 & 4 & Cession
MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-011", "ch-04", "top-const-04-02",
    "Under Article 3, a Bill for the formation of new States or alteration of areas, boundaries, or names can be introduced in Parliament ONLY on the recommendation of:",
    ["The Prime Minister", "The Governor of the concerned State", "The President of India", "The Chief Justice of India"],
    2,
    "Article 3 proviso mandates that no Bill for the formation of new States or alteration of boundaries/names can be introduced in either House of Parliament except on the prior recommendation of the President.",
    {"A": "Prime Minister advises, but formal constitutional recommendation is President's.", "B": "Governor has no recommending power under Art. 3.", "C": "Correct. Prior recommendation of the President is mandatory.", "D": "Judiciary has no role in introducing bills."},
    "Easy", "Article 3 Proviso", "Identify requirement of Presidential recommendation."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-012", "ch-04", "top-const-04-02",
    "Under Article 3, before recommending a state reorganisation bill affecting a State, the President must:",
    ["Obtain the consent of the State Cabinet", "Refer the Bill to the Legislature of that State for expressing its views within a specified period", "Conduct a referendum among registered voters in the State", "Seek an advisory opinion from the High Court"],
    1,
    "Where the proposal affects the area, boundaries, or name of any State, the President must refer the Bill to the Legislature of that State for expressing its views within such period as specified in the reference or extended period.",
    {"A": "Consent is not required.", "B": "Correct. Must refer to State Legislature for its views.", "C": "No referendum is provided.", "D": "High Court reference is not required."},
    "Medium", "Article 3 Proviso", "Examine State Legislature reference mechanism."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-013", "ch-04", "top-const-04-02",
    "Are the views expressed by the State Legislature on an Article 3 reference binding on Parliament or the President?",
    ["Yes, Parliament cannot pass the bill if the State Legislature rejects it", "No, the views of the State Legislature are purely advisory and not binding on Parliament or the President", "Yes, but only if passed by a 2/3rd majority in the State Assembly", "Binding only in respect of altering the name of the State"],
    1,
    "In Babulal Parate v. State of Bombay (1960), the Supreme Court ruled that the views of the State Legislature are not binding on Parliament or the President. Parliament is free to accept, reject, or modify the proposals.",
    {"A": "State legislature has no veto power.", "B": "Correct. Views are purely advisory and non-binding.", "C": "Majority size does not make views binding.", "D": "No exception for name change."},
    "Medium", "Babulal Parate v. State of Bombay (1960) 1 SCR 605", "Affirm non-binding nature of State Legislature views."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-014", "ch-04", "top-const-04-02",
    "What majority is required in Parliament to pass a Bill under Article 3 for the creation of a new State?",
    ["Special majority under Article 368", "Special majority with ratification by half of the States", "Simple majority of members present and voting in each House", "Absolute majority of the total membership of both Houses in a Joint Sitting"],
    2,
    "A Bill under Article 3 is passed by Parliament by a SIMPLE MAJORITY of members present and voting in each House, like any ordinary piece of legislation (Article 4(2)).",
    {"A": "Special majority is not required.", "B": "State ratification does not apply.", "C": "Correct. Simple majority of members present and voting.", "D": "Joint sitting is not needed unless ordinary deadlock occurs."},
    "Easy", "Article 4(2)", "Recall legislative majority for state creation."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-015", "ch-04", "top-const-04-02",
    "Article 4(2) of the Constitution explicitly declares that laws made under Article 2 or Article 3 for admitting or creating States:",
    ["Are deemed to be amendments of the Constitution under Article 368", "Shall NOT be deemed to be amendments of the Constitution for the purposes of Article 368", "Require mandatory approval of the Supreme Court", "Must be ratified by all High Courts"],
    1,
    "Article 4(2) states: 'No such law as aforesaid shall be deemed to be an amendment of this Constitution for the purposes of article 368', meaning Parliament can alter the political map of India via ordinary legislative procedure.",
    {"A": "Explicitly contradicted by Art. 4(2).", "B": "Correct. Shall NOT be deemed amendments under Art. 368.", "C": "No judicial approval needed.", "D": "High Courts have no role."},
    "Easy", "Article 4(2)", "Identify exclusion of Article 368 in state reorganization."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-016", "ch-04", "top-const-04-02",
    "In In re Berubari Union (1960), the Supreme Court held that the 'Cession' of Indian territory to a foreign State:",
    ["Can be done by ordinary legislation under Article 3", "Can be done by executive agreement without parliamentary law", "Cannot be done under Article 3 and requires a Constitutional Amendment under Article 368", "Is completely prohibited under any constitutional procedure"],
    2,
    "In In re Berubari Union (1960), the Supreme Court ruled that Article 3 empowers Parliament to alter boundaries internally among States of India, but does NOT include the power to cede Indian territory to a foreign State. Cession can ONLY be effected by amending the Constitution under Article 368.",
    {"A": "Article 3 applies only to internal reorganization.", "B": "Executive agreement cannot cede territory (Ram Kishore Sen).", "C": "Correct. Cession requires an amendment under Article 368.", "D": "Cession is permissible through constitutional amendment."},
    "Hard", "In re Berubari Union (1960) 3 SCR 250", "Master Berubari cession doctrine."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-017", "ch-04", "top-const-04-02",
    "Which Constitutional Amendment was enacted to cede the Berubari Union territory to Pakistan following the 1960 Supreme Court advisory opinion?",
    ["7th Amendment Act, 1956", "9th Amendment Act, 1960", "10th Amendment Act, 1961", "12th Amendment Act, 1962"],
    1,
    "The 9th Constitutional Amendment Act, 1960 was enacted to give effect to the transfer of the Berubari Union territory to Pakistan in accordance with the Indo-Pakistan Agreement of 1958, implementing the Supreme Court's advisory ruling.",
    {"A": "7th Amendment reorganized states on linguistic lines.", "B": "Correct. 9th Amendment Act, 1960 transferred Berubari.", "C": "10th Amendment incorporated Dadra and Nagar Haveli.", "D": "12th Amendment incorporated Goa, Daman and Diu."},
    "Medium", "9th Constitutional Amendment Act, 1960", "Connect Berubari to 9th Amendment."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-018", "ch-04", "top-const-04-02",
    "In Union of India v. Sukumar Sengupta (1990) and Ram Kishore Sen (1966), the Supreme Court held that 'Settlement of a boundary dispute' with a foreign nation:",
    ["Always requires a Constitutional Amendment under Article 368", "Does not amount to cession of territory and can be implemented by executive action without constitutional amendment", "Requires ratification by all 28 States", "Can only be done by the United Nations Security Council"],
    1,
    "The Supreme Court held that the settlement of an undemarcated boundary dispute does not amount to cession of territory, as it merely ascertains and defines an existing border, and can therefore be implemented by executive action without a constitutional amendment.",
    {"A": "Only actual cession requires Art. 368.", "B": "Correct. Boundary dispute settlement does not amount to cession and can be done executively.", "C": "State ratification not needed.", "D": "UN has no internal jurisdiction."},
    "Hard", "Union of India v. Sukumar Sengupta, AIR 1990 SC 1692", "Distinguish boundary demarcation from cession."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-019", "ch-04", "top-const-04-02",
    "Which Constitutional Amendment Act was passed in 2015 to give effect to the Land Boundary Agreement (LBA) and exchange of enclaves between India and Bangladesh?",
    ["99th Amendment Act", "100th Amendment Act", "101st Amendment Act", "102nd Amendment Act"],
    1,
    "The 100th Constitutional Amendment Act, 2015 was enacted to acquire certain territories by India and transfer certain enclaves to Bangladesh pursuant to the 1974 Land Boundary Agreement and its 2011 Protocol.",
    {"A": "99th Amendment was NJAC.", "B": "Correct. 100th Amendment Act, 2015 for India-Bangladesh enclaves.", "C": "101st Amendment was GST.", "D": "102nd Amendment was NCBC."},
    "Medium", "100th Constitutional Amendment Act, 2015", "Recall 100th Amendment land boundary exchange."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-020", "ch-04", "top-const-04-02",
    "If Parliament amends an Article 3 Bill substantially after receiving the views of the State Legislature, is a fresh reference to the State Legislature mandatory?",
    ["Yes, a fresh reference is required for every new amendment", "No, in Babulal Parate (1960), the Supreme Court held that no fresh reference is necessary for amendments introduced in Parliament", "Yes, if the Governor objects", "Only if the alteration affects the State capital"],
    1,
    "In Babulal Parate v. State of Bombay (1960), the Supreme Court ruled that once a Bill has been referred to the State Legislature, no fresh reference is necessary every time an amendment to the proposal is moved and accepted in Parliament.",
    {"A": "Continuous re-reference would paralyze legislative process.", "B": "Correct. No fresh reference required for parliamentary amendments.", "C": "Governor objection is irrelevant.", "D": "No capital exception."},
    "Hard", "Babulal Parate v. State of Bombay (1960)", "Understand rule on amendments to reorganisation bills."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-021", "ch-04", "top-const-04-02",
    "The Dhar Commission (1948) and the JVP Committee (1949) were appointed to examine:",
    ["Centre-State financial distribution", "Reorganisation of States on linguistic basis", "Abolition of Privy Purses", "Integration of Jammu and Kashmir"],
    1,
    "The S.K. Dhar Commission (1948) and the JVP Committee (Jawaharlal Nehru, Vallabhbhai Patel, Pattabhi Sitaramayya, 1949) were appointed to examine the feasibility of linguistic reorganisation of States. Both recommended administrative convenience over language.",
    {"A": "Financial commissions were separate.", "B": "Correct. Linguistic reorganisation of States.", "C": "Privy purses were abolished by 26th Amendment 1971.", "D": "Integration was overseen by Patel under Instrument of Accession."},
    "Medium", "States Reorganisation History", "Identify Dhar Commission and JVP Committee purpose."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-022", "ch-04", "top-const-04-02",
    "Which was the FIRST linguistic State created in independent India in October 1953 following the hunger strike of Potti Sreeramulu?",
    ["Maharashtra", "Gujarat", "Andhra State", "Kerala"],
    2,
    "Andhra State was created on 1st October 1953 as the first linguistic State by separating the Telugu-speaking areas from the State of Madras, following the 56-day hunger strike and demise of Potti Sreeramulu.",
    {"A": "Maharashtra was created in 1960 from Bombay.", "B": "Gujarat was created in 1960 from Bombay.", "C": "Correct. Andhra State in October 1953.", "D": "Kerala was created in 1956."},
    "Easy", "Andhra State Act, 1953", "Identify first linguistic State."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-023", "ch-04", "top-const-04-02",
    "The States Reorganisation Act, 1956 and the 7th Constitutional Amendment Act, 1956 replaced the four-fold classification of States (Part A, B, C, D) with:",
    ["14 States and 6 Union Territories", "16 States and 3 Union Territories", "12 States and 8 Union Territories", "18 States and 5 Union Territories"],
    0,
    "Based on the recommendations of the Fazal Ali Commission (State Reorganisation Commission), the 7th Amendment Act, 1956 abolished the distinction between Part A, B, C, and D states, creating 14 States and 6 Union Territories.",
    {"A": "Correct. 14 States and 6 Union Territories.", "B": "Incorrect counts.", "C": "Incorrect counts.", "D": "Incorrect counts."},
    "Medium", "7th Constitutional Amendment Act, 1956", "Recall 1956 States Reorganisation result."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-024", "ch-04", "top-const-04-02",
    "Who were the three members of the States Reorganisation Commission (Fazal Ali Commission) appointed in 1953?",
    ["Justice Fazal Ali, K.M. Panikkar, and H.N. Kunzru", "S.K. Dhar, J.L. Nehru, and Vallabhbhai Patel", "B.R. Ambedkar, B.N. Rau, and K.M. Munshi", "Lord Mountbatten, Cyril Radcliffe, and Wavell"],
    0,
    "The States Reorganisation Commission appointed in December 1953 was headed by Justice Fazal Ali (Chairman), with K.M. Panikkar and H.N. Kunzru as its two other members.",
    {"A": "Correct. Justice Fazal Ali, K.M. Panikkar, H.N. Kunzru.", "B": "Dhar and JVP were earlier committees.", "C": "Drafting leaders.", "D": "Colonial figures."},
    "Easy", "Fazal Ali Commission Composition", "Recall members of Fazal Ali Commission."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-04-025", "ch-04", "top-const-04-02",
    "Does Article 3 require a reference to the Legislature of a Union Territory when a proposal affects its area, boundaries, or name?",
    ["Yes, identical to a State", "No, the proviso to Article 3 applies only to States, though the main body includes Union Territories by virtue of Explanation I", "Yes, if the UT has a legislative assembly", "Reference must be made to the Lieutenant Governor"],
    1,
    "Under Explanation I to Article 3 (added by 18th Amendment 1966), 'State' includes Union territory in clauses (a) to (e), but in the proviso, 'State' does NOT include a Union territory. Hence, no reference to a UT legislature is required.",
    {"A": "Proviso does not cover UTs.", "B": "Correct. Proviso applies only to States, excluding UTs.", "C": "Even UTs with assemblies (Delhi, Puducherry, J&K) are not constitutionally protected under the proviso.", "D": "No requirement to refer to LG under Art. 3."},
    "Hard", "Article 3, Explanation I & II", "Examine application of Article 3 proviso to Union Territories."
))

# ==============================================================================
# CHAPTER 5: CITIZENSHIP (25 MCQs)
# ==============================================================================
# 05-01 to 05-12: Articles 5–8 Commencement
MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-001", "ch-05", "top-const-05-01",
    "Under Article 5 of the Constitution, citizenship at commencement was granted to every person who had his 'domicile' in India and:",
    ["Was born in India, OR either of whose parents was born in India, OR ordinarily resident in India for not less than 5 years immediately preceding commencement", "Owned immovable property in India", "Could speak an Eighth Schedule language", "Paid income tax to the Government of India"],
    0,
    "Article 5 requires: (1) Domicile in India at commencement, PLUS (2) Any ONE of three conditions: (a) born in territory of India; OR (b) either parent born in territory of India; OR (c) ordinarily resident in India for not less than 5 years immediately preceding 26th January 1950.",
    {"A": "Correct. Domicile + (Born OR Parent Born OR 5-yr Residence).", "B": "Property ownership is irrelevant to citizenship.", "C": "Language is not a constitutional citizenship test.", "D": "Taxation is irrelevant."},
    "Easy", "Article 5", "Recall Article 5 citizenship conditions."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-002", "ch-05", "top-const-05-01",
    "In Pradeep Jain v. Union of India (1984), the Supreme Court held that in India there is:",
    ["Dual domicile: Domicile of the State and Domicile of India", "Only ONE domicile, namely, the Domicile of India", "Domicile determined by municipal ward", "No concept of domicile recognized in law"],
    1,
    "In Pradeep Jain v. UOI (1984), the Supreme Court ruled that India recognizes only ONE single domicile, which is the Domicile of India. There is no such thing as a separate State domicile under the Indian Constitution.",
    {"A": "USA recognizes dual domicile; India does not.", "B": "Correct. Only ONE single Domicile of India.", "C": "Municipal domicile is legally non-existent.", "D": "Domicile is foundational in Article 5."},
    "Medium", "Pradeep Jain v. Union of India (1984) 3 SCC 654", "Master single domicile doctrine in India."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-003", "ch-05", "top-const-05-01",
    "Under Article 6, what was the cut-off date for migrants from Pakistan to automatically become Indian citizens upon ordinary residence?",
    ["15th August, 1947", "19th July, 1948", "26th November, 1949", "26th January, 1950"],
    1,
    "Under Article 6(b)(i), persons migrating from Pakistan before 19th July 1948 (the date permit system for migration was introduced) became citizens if ordinarily resident since migration. Those migrating on or after 19th July 1948 had to register after 6 months residence.",
    {"A": "15th August 1947 was independence.", "B": "Correct. 19th July 1948 was the permit system cut-off date.", "C": "26th November 1949 was adoption.", "D": "26th January 1950 was commencement."},
    "Medium", "Article 6(b)", "Recall 19th July 1948 permit cut-off date."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-004", "ch-05", "top-const-05-01",
    "Article 7 of the Constitution contains an overriding provision regarding persons who migrated to Pakistan after which date?",
    ["1st March, 1947", "15th August, 1947", "19th July, 1948", "26th January, 1950"],
    0,
    "Article 7 provides that notwithstanding anything in Articles 5 and 6, a person who after 1st March 1947 migrated from India to Pakistan shall not be deemed a citizen of India, unless they returned under a permit for resettlement.",
    {"A": "Correct. 1st March 1947.", "B": "15th August 1947 is partition date.", "C": "19th July 1948 is Article 6 permit cut-off.", "D": "26th January 1950 is commencement."},
    "Medium", "Article 7", "Identify Article 7 migration date."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-005", "ch-05", "top-const-05-01",
    "Article 8 confers citizenship on persons of Indian origin residing outside India who register themselves with:",
    ["The Ministry of Home Affairs in New Delhi", "The diplomatic or consular representative of India in the country of residence", "The United Nations High Commissioner for Refugees", "The Supreme Court of India"],
    1,
    "Article 8 enables persons of Indian origin residing outside undivided India to register as citizens by applying to the diplomatic or consular representative of India in the country where they are residing.",
    {"A": "Registration is done abroad.", "B": "Correct. Diplomatic or consular representative of India.", "C": "UNHCR is international body.", "D": "Supreme Court has no registration function."},
    "Easy", "Article 8", "Identify diplomatic registration under Article 8."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-006", "ch-05", "top-const-05-01",
    "Which Article explicitly prohibits Dual Citizenship and provides for automatic termination of Indian citizenship on acquiring foreign nationality?",
    ["Article 7", "Article 8", "Article 9", "Article 10"],
    2,
    "Article 9 states: 'No person shall be a citizen of India by virtue of article 5, or be deemed to be a citizen of India by virtue of article 6 or article 8, if he has voluntarily acquired the citizenship of any foreign State'.",
    {"A": "Article 7 is migrants to Pakistan.", "B": "Article 8 is persons residing abroad.", "C": "Correct. Article 9 bars dual citizenship.", "D": "Article 10 is continuance of rights."},
    "Easy", "Article 9", "Identify Article 9 prohibition of dual citizenship."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-007", "ch-05", "top-const-05-01",
    "Article 10 of the Constitution deals with:",
    ["Continuance of the rights of citizenship subject to any law made by Parliament", "Abolition of untouchability", "Regulation of citizenship by Parliament", "Single citizenship"],
    0,
    "Article 10 provides that every person who is or is deemed to be a citizen of India under Part II shall, subject to the provisions of any law that may be made by Parliament, continue to be such citizen.",
    {"A": "Correct. Continuance of citizenship rights.", "B": "Untouchability is Article 17.", "C": "Regulation by Parliament is Article 11.", "D": "Single citizenship is a general constitutional hallmark."},
    "Easy", "Article 10", "Recall Article 10 subject matter."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-008", "ch-05", "top-const-05-01",
    "Which Article confers absolute plenary power on Parliament to regulate the right of citizenship by law, including acquisition and termination?",
    ["Article 9", "Article 10", "Article 11", "Article 12"],
    2,
    "Article 11 provides: 'Nothing in the foregoing provisions of this Part shall derogate from the power of Parliament to make any provision with respect to the acquisition and termination of citizenship and all other matters relating to citizenship'.",
    {"A": "Article 9 terminates on foreign acquisition.", "B": "Article 10 continues existing rights.", "C": "Correct. Article 11 confers plenary legislative power.", "D": "Article 12 defines State."},
    "Easy", "Article 11", "Identify Article 11 parliamentary plenary power."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-009", "ch-05", "top-const-05-01",
    "Articles 5 to 11 in Part II of the Constitution dealt with citizenship:",
    ["As a permanent, exhaustive statutory code for future generations", "Only at the commencement of the Constitution on 26th January 1950, leaving future regulation to Parliament", "Based on religious communities", "Only for persons born in princely states"],
    1,
    "Part II did not establish a permanent or comprehensive code for future citizenship; it simply identified who became citizens at the commencement of the Constitution on 26th January 1950, leaving subsequent matters to Parliament under Article 11.",
    {"A": "Parliament enacted the Citizenship Act 1955 for subsequent generations.", "B": "Correct. Dealt with citizenship at commencement only.", "C": "Citizenship is secular, not religious.", "D": "Covered all Indian territories."},
    "Medium", "Part II Scope", "Understand temporary commencement character of Part II."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-010", "ch-05", "top-const-05-01",
    "In State of U.P. v. Rehmatullah (1971), who has the exclusive jurisdiction to decide whether an Indian citizen has acquired foreign citizenship under Section 9(2) of the Citizenship Act, 1955?",
    ["The Civil Courts", "The Central Government", "The State High Court", "The Ministry of External Affairs"],
    1,
    "In State of U.P. v. Rehmatullah (1971) and Bhagwati Prasad v. Rajeev Sharma, the Supreme Court affirmed that under Section 9(2) of the Citizenship Act 1955, the Central Government has exclusive authority to determine foreign citizenship acquisition; civil courts are barred from deciding this question.",
    {"A": "Civil court jurisdiction is excluded.", "B": "Correct. Central Government has exclusive jurisdiction under Section 9(2).", "C": "High Court acts only in judicial review.", "D": "Ministry of External Affairs does not exercise statutory tribunal power under s. 9(2)."},
    "Hard", "Section 9(2), Citizenship Act, 1955", "Identify authority determining loss of citizenship."
))

# 05-11 to 05-25: Statutory Control & Citizenship Act 1955
MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-011", "ch-05", "top-const-05-02",
    "Under the Citizenship Act, 1955, how many modes of acquiring Indian citizenship are prescribed?",
    ["Three modes", "Four modes", "Five modes", "Six modes"],
    2,
    "The Citizenship Act, 1955 prescribes FIVE modes of acquiring citizenship: (1) By Birth (s. 3); (2) By Descent (s. 4); (3) By Registration (s. 5); (4) By Naturalisation (s. 6); and (5) By Incorporation of Territory (s. 7).",
    {"A": "Three is incorrect.", "B": "Four is incorrect.", "C": "Correct. Five modes: Birth, Descent, Registration, Naturalisation, Incorporation.", "D": "Six is incorrect."},
    "Easy", "Citizenship Act, 1955, Sections 3–7", "Recall five modes of acquiring citizenship."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-012", "ch-05", "top-const-05-02",
    "Under the Citizenship Act, 1955, how many modes of losing Indian citizenship are recognized?",
    ["Two: Resignation and Expulsion", "Three: Renunciation, Termination, and Deprivation", "Four: Cancellation, Revocation, Forfeiture, and Banishment", "Single mode of voluntary surrender"],
    1,
    "The Citizenship Act, 1955 provides for THREE modes of losing citizenship: (1) Renunciation (s. 8 - voluntary declaration); (2) Termination (s. 9 - automatic upon acquiring foreign citizenship); and (3) Deprivation (s. 10 - compulsory termination by Central Government for fraud/disloyalty).",
    {"A": "Resignation and expulsion are not legal terms in the Act.", "B": "Correct. Renunciation, Termination, Deprivation.", "C": "Incorrect statutory terms.", "D": "Multiple modes exist."},
    "Easy", "Citizenship Act, 1955, Sections 8–10", "Recall three modes of losing citizenship."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-013", "ch-05", "top-const-05-02",
    "Which category of citizens is immune from 'Deprivation' of citizenship under Section 10 of the Citizenship Act, 1955?",
    ["Citizens by Naturalisation", "Citizens by Registration", "Citizens by Birth", "Overseas Citizens of India"],
    2,
    "Section 10 of the Citizenship Act, 1955 (Deprivation) applies ONLY to citizens who acquired citizenship by registration or naturalisation. A citizen by birth or descent CANNOT be deprived of citizenship under Section 10.",
    {"A": "Naturalized citizens can be deprived.", "B": "Registered citizens can be deprived.", "C": "Correct. Citizens by birth cannot be deprived under Section 10.", "D": "OCI is not full citizenship."},
    "Hard", "Citizenship Act, 1955, Section 10(1)", "Identify immunity of citizens by birth from deprivation."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-014", "ch-05", "top-const-05-02",
    "Can a company, corporation, or juristic entity claim Indian citizenship under the Constitution or the Citizenship Act, 1955?",
    ["Yes, if incorporated in India", "Yes, if all its shareholders are Indian citizens", "No, in State Trading Corporation v. CTO (1963), the Supreme Court held that only natural human persons can be citizens", "Yes, by filing an affidavit with the Registrar of Companies"],
    2,
    "In State Trading Corporation of India v. Commercial Tax Officer (1963) and TELCO v. State of Bihar (1964), the 9-Judge Bench held that corporations are not citizens and cannot claim Fundamental Rights guaranteed exclusively to citizens under Article 19.",
    {"A": "Incorporation creates legal personality, not citizenship.", "B": "Shareholder citizenship does not confer citizenship on company (TELCO).", "C": "Correct. Only natural human beings can be citizens.", "D": "ROC has no citizenship powers."},
    "Medium", "State Trading Corp. of India v. CTO (1963) 3 SCR 792", "Affirm rule that corporations are not citizens."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-015", "ch-05", "top-const-05-02",
    "In R.C. Cooper v. Union of India (Bank Nationalisation Case, 1970), how did the Supreme Court protect citizen rights in corporate shareholdings?",
    ["Declared companies to be citizens under Article 19", "Held that where state action impairs rights of shareholders who are citizens, they can maintain a petition under Article 32 to protect their fundamental rights", "Transferred corporate assets to the President", "Created a new corporate writ jurisdiction"],
    1,
    "In R.C. Cooper (1970), the 11-Judge Bench held that although a company is not a citizen, an individual shareholder who is a citizen can petition under Article 32 if state action violates his fundamental rights along with the company's rights.",
    {"A": "Did not overturn STC holding that company is not citizen.", "B": "Correct. Citizen shareholders can petition under Art. 32.", "C": "Assets were nationalized with compensation dispute.", "D": "Writs are standard Art. 32 remedies."},
    "Hard", "R.C. Cooper v. Union of India (1970) 1 SCC 248", "Understand shareholder fundamental rights protection."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-016", "ch-05", "top-const-05-02",
    "Overseas Citizens of India (OCI) cardholders under the Citizenship Act, 1955 do NOT enjoy which of the following rights?",
    ["Right to travel to India without a visa", "Right to purchase agricultural land, right to vote, and right to hold public constitutional office", "Right to pursue professional occupations in India", "Parity with NRIs in economic/financial fields"],
    1,
    "Under Section 7B of the Citizenship Act, 1955, OCI cardholders are explicitly barred from: (a) right to equality of opportunity in public employment (Art. 16); (b) election as President/VP/MP/MLA; (c) appointment as judge of SC/HC; (d) right to register as a voter; and (e) acquiring agricultural land/farm houses.",
    {"A": "OCIs have multi-entry lifelong visa.", "B": "Correct. Prohibited from voting, agricultural land, and public office.", "C": "Can pursue medicine, law, architecture.", "D": "Enjoy parity with NRIs in educational fees."},
    "Medium", "Citizenship Act, 1955, Section 7B", "Identify constitutional disabilities of OCI cardholders."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-017", "ch-05", "top-const-05-02",
    "Under the Citizenship (Amendment) Act, 2019 (CAA), expedited citizenship by naturalization is provided to persecuted minorities from which three countries?",
    ["Pakistan, Bangladesh, and Afghanistan", "Pakistan, Sri Lanka, and Myanmar", "Bangladesh, Nepal, and Bhutan", "Afghanistan, China, and Maldives"],
    0,
    "The Citizenship (Amendment) Act, 2019 covers six minority communities (Hindus, Sikhs, Buddhists, Jains, Parsis, Christians) who entered India on or before 31st December 2014 from Pakistan, Bangladesh, and Afghanistan.",
    {"A": "Correct. Pakistan, Bangladesh, and Afghanistan.", "B": "Sri Lanka and Myanmar are not included.", "C": "Nepal and Bhutan are not included.", "D": "China and Maldives are not included."},
    "Easy", "Citizenship (Amendment) Act, 2019, Section 2(1)(b)", "Identify countries specified under CAA 2019."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-018", "ch-05", "top-const-05-02",
    "What is the cut-off date of entry into India specified under the Citizenship (Amendment) Act, 2019?",
    ["15th August, 1947", "24th March, 1971", "31st December, 2014", "26th January, 2020"],
    2,
    "Under the CAA 2019, eligible persons must have entered India on or before 31st December 2014 to qualify for expedited naturalization (reducing aggregate residence from 11 years to 5 years).",
    {"A": "1947 is partition.", "B": "24th March 1971 is Assam Accord cut-off.", "C": "Correct. 31st December 2014.", "D": "2020 is implementation date."},
    "Easy", "Citizenship (Amendment) Act, 2019, Section 2(1)(b)", "Recall CAA 2019 entry cut-off date."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-019", "ch-05", "top-const-05-02",
    "Section 6A was inserted into the Citizenship Act, 1955 to give statutory effect to:",
    ["The Simla Agreement, 1972", "The Assam Accord, 1985", "The Tashkent Declaration, 1966", "The Nehru-Liaquat Pact, 1950"],
    1,
    "Section 6A was inserted by the Citizenship (Amendment) Act, 1985 to give statutory effect to the Assam Accord (15th August 1985), establishing a special framework for persons of Indian origin migrating from Bangladesh to Assam.",
    {"A": "Simla was bilateral peace treaty.", "B": "Correct. Assam Accord, 1985.", "C": "Tashkent was post-1965 declaration.", "D": "Nehru-Liaquat was 1950 minority treaty."},
    "Medium", "Citizenship Act, 1955, Section 6A", "Connect Section 6A to Assam Accord."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-020", "ch-05", "top-const-05-02",
    "In which 2024 landmark decision did a 5-Judge Constitution Bench uphold the constitutional validity of Section 6A of the Citizenship Act, 1955?",
    ["In re Section 6A of Citizenship Act (2024)", "Sarbananda Sonowal v. Union of India (2005)", "Assam Sanmilita Mahasangha v. Union of India (2014)", "National Forum for Adivasi Rights v. UOI (2023)"],
    0,
    "In In re Section 6A of the Citizenship Act, 1955 (decided in October 2024), a 5-Judge Constitution Bench (4:1 majority) upheld the constitutional validity of Section 6A, ruling that the March 25, 1971 cut-off date for Assam was rational and constitutional.",
    {"A": "Correct. In re Section 6A (2024 5-Judge Bench).", "B": "Sonowal (2005) struck down IMDT Act.", "C": "Assam Sanmilita Mahasangha (2014) referred the matter to 5 judges.", "D": "Fictional case title."},
    "Hard", "In re Section 6A, Citizenship Act, 1955 (2024) SCC OnLine SC", "Recall 2024 Section 6A Constitution Bench judgment."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-021", "ch-05", "top-const-05-02",
    "What is the cut-off date established under Section 6A for detecting and expelling illegal immigrants who entered Assam from Bangladesh?",
    ["1st January, 1966", "25th March, 1971", "31st December, 2014", "15th August, 1947"],
    1,
    "Under Section 6A, persons entering Assam from Bangladesh on or after 25th March 1971 (the start of the Bangladesh Liberation War) are treated as illegal immigrants to be detected and deported.",
    {"A": "Pre-1966 migrants were deemed citizens.", "B": "Correct. 25th March 1971 is the deportation cut-off date.", "C": "2014 is CAA cut-off.", "D": "1947 is partition."},
    "Medium", "Citizenship Act, 1955, Section 6A(3)", "Recall March 25, 1971 cut-off under Section 6A."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-022", "ch-05", "top-const-05-02",
    "Which statute was struck down by the Supreme Court in Sarbananda Sonowal v. Union of India (2005) for reversing the burden of proof and abetting external aggression?",
    ["The Foreigners Act, 1946", "The Illegal Migrants (Determination by Tribunals) Act, 1983 (IMDT Act)", "The Passports Act, 1967", "The Registration of Foreigners Act, 1939"],
    1,
    "In Sarbananda Sonowal (2005), the 3-Judge Bench struck down the IMDT Act, 1983 as unconstitutional, holding that placing the burden of proving that an individual is an illegal migrant on the complainant rather than the suspected foreigner violated Article 355.",
    {"A": "Foreigners Act 1946 Section 9 places burden of proof on the foreigner.", "B": "Correct. IMDT Act, 1983 was struck down.", "C": "Passports Act governs travel documents.", "D": "1939 Act governs foreigner reporting."},
    "Medium", "Sarbananda Sonowal v. Union of India (2005) 5 SCC 665", "Recall strike-down of IMDT Act."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-023", "ch-05", "top-const-05-02",
    "Under Section 9 of the Foreigners Act, 1946, on whom does the 'Burden of Proof' lie regarding whether a person is or is not a foreigner?",
    ["Always on the Police / State prosecution", "Upon the person against whom the question arises", "Upon the Central Government", "Upon the local municipal magistrate"],
    1,
    "Section 9 of the Foreigners Act, 1946 explicitly reverses ordinary criminal burdens: if any question arises whether any person is or is not a foreigner, the onus of proving that such person is not a foreigner lies upon that person.",
    {"A": "Prosecution does not carry the initial burden under Section 9.", "B": "Correct. The burden of proof lies upon that person.", "C": "Central government is not burdened.", "D": "Magistrate is adjudicator."},
    "Medium", "Foreigners Act, 1946, Section 9", "Master statutory burden of proof under Foreigners Act."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-024", "ch-05", "top-const-05-02",
    "When a male citizen of India voluntarily renounces his citizenship under Section 8, what happens to the citizenship of his minor child?",
    ["Remains unaffected", "Also ceases to be an Indian citizen, but may resume Indian citizenship within one year after attaining full age (18 years)", "Is permanently forfeited", "Transferred to mother's citizenship automatically"],
    1,
    "Section 8(2) provides that where a person renounces citizenship, every minor child of that person ceases to be a citizen of India. However, any such child may, within one year after attaining full age (18), make a declaration to resume Indian citizenship.",
    {"A": "Minor citizenship ceases conditionally.", "B": "Correct. Ceases, but can resume within 1 year of attaining majority.", "C": "Not permanently forfeited.", "D": "Mother's transfer is not automatic."},
    "Hard", "Citizenship Act, 1955, Section 8(2)", "Examine minor child citizenship on parental renunciation."
))

MCQS_CH01_05.append(create_mcq(
    "mcq-const-05-025", "ch-05", "top-const-05-02",
    "Which Fundamental Rights are available to 'Any Person' (both citizens and non-citizens) under the Indian Constitution?",
    ["Articles 15, 16, 19, 29, 30", "Articles 14, 20, 21, 21A, 22, 23, 24, 25, 26, 27, 28", "Only Article 21", "Articles 14 and 19 only"],
    1,
    "Articles 14, 20, 21, 21A, 22, 23, 24, 25, 26, 27, and 28 are guaranteed to 'any person' (citizens and non-citizens alike). Articles 15, 16, 19, 29, and 30 are available EXCLUSIVELY to citizens of India.",
    {"A": "These five rights are available ONLY to citizens.", "B": "Correct. Available to any person (citizens and non-citizens).", "C": "Under-inclusive.", "D": "Article 19 is available only to citizens."},
    "Easy", "Fundamental Rights Classification", "Classify rights available to all persons vs citizens only."
))

print(f"Chapters 1 to 5 complete ({len(MCQS_CH01_05)} total).")
