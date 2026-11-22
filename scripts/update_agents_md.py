with open('AGENTS.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Update Section 1 Baseline
old_s1 = "- **Current Baseline:** Version 3.1 — Phase 4 (Complete Civil Procedure Code Learning Academy, The Civil Suit Journey, and Section-Order-Rule Explorer)"
new_s1 = "- **Current Baseline:** Version 3.1 — Phase 5 (Complete Social Legislation Learning Academy, Nine Special Acts, Thematic Study Centre, and Statutory Explorer)"
text = text.replace(old_s1, new_s1, 1)

# Update Section 10
old_s10 = '''## 10. Subject-Wise Judicial Learning Academy (V3.1 Phase 4 Baseline)
Structured subject-by-subject curriculum for the UP PCS-J Preliminary Examination:
1. **Subject Registry (assets/learning/data/subjects.js):** 30 subjects defined across Paper I (12 GK + 9 Social Legislation) and Paper II (9 Law + sub-modules). Eight subjects are active production modules:
   - law-constitution (Indian Constitution)
   - law-jurisprudence (Jurisprudence)
   - law-contract (Indian Contract Act, 1872)
   - law-tpa (Transfer of Property Act, 1882)
   - law-criminal (Criminal Law: Bharatiya Nyaya Sanhita, 2023 & Indian Penal Code, 1860)
   - law-crpc (Criminal Procedure: Bharatiya Nagarik Suraksha Sanhita, 2023 & Code of Criminal Procedure, 1973)
   - law-evidence (Law of Evidence: Bharatiya Sakshya Adhiniyam, 2023 & Indian Evidence Act, 1872)
   - law-cpc (Code of Civil Procedure, 1908)
   - 22 subjects remain structured upcoming modules.
2. **Active Academic Modules Across 8 Subjects:**
   - **Indian Constitution:** 15 Chapters (ch-01 to ch-15), 45 Topics (top-const-01-01 to top-const-15-04), 480 MCQs, 158 mapped authentic PYQs, 12 custom vector SVG schematics.
   - **Jurisprudence:** 11 Chapters (ch-jur-01 to ch-jur-11), 30 Topics (top-jur-01-01 to top-jur-11-03), 240 MCQs, 45 mapped authentic PYQs, 8 custom vector SVG schematics.
   - **Law of Contract:** 11 Chapters (ch-cnt-01 to ch-cnt-11), 32 Topics (top-cnt-01-01 to top-cnt-11-02), 260 MCQs, 82 mapped authentic PYQs, 8 custom vector SVG schematics.
   - **Transfer of Property Act:** 8 Chapters (ch-tpa-01 to ch-tpa-08), 24 Topics (top-tpa-01-01 to top-tpa-08-03), 240 MCQs, 47 mapped authentic PYQs, 8 custom vector SVG schematics.
   - **Criminal Law:** 12 Chapters (ch-crim-01 to ch-crim-12), 36 Topics (top-crim-01-01 to top-crim-12-03), 360 MCQs, 78 mapped authentic PYQs, 8 custom vector SVG schematics.
   - **Criminal Procedure:** 12 Chapters (ch-crpc-01 to ch-crpc-12), 35 Topics (top-crpc-01-01 to top-crpc-12-03), 360 MCQs, 49 mapped authentic PYQs, 8 custom vector SVG schematics.
   - **Law of Evidence:** 10 Chapters (ch-evi-01 to ch-evi-10), 30 Topics (top-evi-01-01 to top-evi-10-03), 280 MCQs, 73 mapped authentic PYQs, 8 custom vector SVG schematics.
   - **Code of Civil Procedure:** 20 Chapters (ch-cpc-01 to ch-cpc-20), 57 Topics (top-cpc-01-01 to top-cpc-20-03), 400 MCQs, 60 mapped authentic PYQs, 12 custom vector SVG schematics.
   - **Combined Academy Totals:** 99 Chapters, 289 Topics, 289 Authored Concept Notes, 2,620 Verified Practice MCQs, 592 Mapped Authentic Historical PYQs, 72 Custom Vector SVG Schematics.
3. **Statutory Comparison Lab (comparison-lab.html):**
   - 79 verified comparative transitions (30 BNS vs IPC, 21 BNSS vs CrPC, 28 BSA vs IEA), live debounced search, category filtering, KPI summaries, and prominent Section 106(2) BNS hit-and-run non-commencement notice (MHA Notification S.O. 850(E)).
4. **The Civil Suit Journey Simulator (civil-suit-journey.html):**
   - 14 interactive procedural stages ('From Plaint to Decree'), Presiding Officer Scrutiny Checklists, High-Yield Traps, Landmark Judicial Precedents, Scenario Simulators, and master structural flowchart.
5. **CPC Section-Order-Rule Explorer (assets/learning/data/cpc/cpc-sections-orders-rules.js):**
   - 83 high-yield statutory entries (48 Sections, 35 Rules) with tailored UP Exam Tips, conditions, exceptions, and India Code verified links.
6. **Interactive Study Room (subject-study.html):**
   - Detailed Study Mode & Quick Revision Mode with bare act callout boxes, landmark case judgments, comparative distinction tables, active recall flashcards with 3D flip interaction, and 72 custom SVG diagrams.
   - Paired-Law 3 Track Switcher: Current Law (New), Historical Law (Old), Compare Both.
   - Dynamic URL parameter routing (?subject=...&chapter=...&topic=...).
7. **Comprehensive Practice MCQ Bank (topic-practice.html):**
   - 2,620 verified questions with comprehensive option explanations (A, B, C, D), bare act references, and learning objectives.
   - 8 Practice Modes: Learn & Practise, Topic Test, Chapter Test, Subject Mock Test, PYQ Practice, Missed/Wrong Questions Queue, Bookmarks, and Advanced Challenge.
8. **Bidirectional Concept-to-MCQ Linking:**
   - Direct transitions between reading and testing with parameter passing (?subject=...&chapter=...&topic=...).
9. **Historical PYQ Mapping Overlays:**
   - 592 authentic UP PCS-J questions mapped directly to the 99 chapters/289 topics across all 8 subjects without modifying questions.js.
10. **Subject Mastery Analytics (subject-progress.html):**
    - Real-time tracking of topic reading coverage, test accuracy, spaced repetition queues, and chapter mastery matrix across all 8 active subjects.
11. **6 Dedicated Academy, Comparison & Simulation Pages:**
    - learning-academy.html, subject-study.html, topic-practice.html, subject-progress.html, comparison-lab.html, civil-suit-journey.html (Total 27 operational HTML pages).'''

new_s10 = '''## 10. Subject-Wise Judicial Learning Academy (V3.1 Phase 5 Baseline)
Structured subject-by-subject curriculum for the UP PCS-J Preliminary Examination:
1. **Subject Registry (assets/learning/data/subjects.js):** 30 subjects defined across Paper I (12 GK + 9 Social Legislation) and Paper II (9 Law + sub-modules). Seventeen subjects are active production modules:
   - 8 Paper II Law Modules: law-constitution, law-jurisprudence, law-contract, law-tpa, law-criminal, law-crpc, law-evidence, law-cpc.
   - 9 Paper I Social Legislation Acts: soc-disabilities, soc-parents, soc-dowry, soc-domestic-violence, soc-posh, soc-pcpndt, soc-mtp, soc-indecent-rep, soc-pocso.
   - 13 subjects remain structured upcoming modules.
2. **Active Academic Modules Across 17 Subjects:**
   - **8 Law Paper II Subjects:** 99 Chapters, 289 Topics, 2,620 MCQs, 592 PYQs, 72 SVG Schematics.
   - **9 Social Legislation Paper I Acts:** 28 Chapters, 84 Topics, 455 MCQs, 23 PYQs, 18 SVG Schematics.
   - **Combined Academy Totals:** 127 Chapters, 373 Topics, 373 Authored Concept Notes, 3,075 Verified Practice MCQs, 615 Mapped Authentic Historical PYQs, 90 Custom Vector SVG Schematics.
3. **Statutory Comparison Lab (comparison-lab.html):**
   - 79 verified comparative transitions (30 BNS vs IPC, 21 BNSS vs CrPC, 28 BSA vs IEA), live debounced search, category filtering, KPI summaries, and Section 106(2) BNS hit-and-run non-commencement notice (MHA Notification S.O. 850(E)).
4. **The Civil Suit Journey Simulator (civil-suit-journey.html):**
   - 14 interactive procedural stages ('From Plaint to Decree') with distinct procedural stream tagging (standard progression vs parallel execution/interlocutory streams), Presiding Officer Scrutiny Checklists, High-Yield Traps, Landmark Precedents, Scenario Simulators, and master structural flowchart.
5. **Two High-Yield Statutory Explorers (181 Entries Total):**
   - **CPC Section-Order-Rule Explorer (`cpc-sections-orders-rules.js`):** 83 high-yield statutory entries (48 Sections, 35 Rules).
   - **Social Legislation Sections Explorer (`social-sections-explorer.js`):** 98 high-yield statutory entries across all 9 Acts with conditions, exceptions, penalties, India Code links, and tailored UP Exam Tips.
6. **Social Legislation Study Centre (learning-academy.html):**
   - Dedicated showcase section organized into three thematic clusters: Group A (Equality, Inclusion & Welfare), Group B (Protection of Women), and Group C (Reproductive Health & Child Protection).
7. **Interactive Study Room (subject-study.html):**
   - Detailed Study Mode & Quick Revision Mode with bare act callouts, landmark case judgments, active recall flashcards with 3D flip interaction, paired-law switcher, and 90 custom SVG diagrams.
8. **Comprehensive Practice MCQ Bank (topic-practice.html):**
   - 3,075 verified questions with comprehensive 4-option explanations (A, B, C, D), statutory provisions, and learning objectives across 8 practice modes.
9. **Historical PYQ Mapping Overlays:**
   - 615 authentic UP PCS-J questions mapped directly across all 17 active subjects without modifying questions.js.
10. **Subject Mastery Analytics (subject-progress.html):**
    - Real-time tracking of topic reading coverage, test accuracy, spaced repetition queues, and chapter mastery matrix across all 17 active subjects.
11. **6 Dedicated Academy, Comparison & Simulation Pages:**
    - learning-academy.html, subject-study.html, topic-practice.html, subject-progress.html, comparison-lab.html, civil-suit-journey.html (Total 27 operational HTML pages).'''

text = text.replace(old_s10, new_s10, 1)

with open('AGENTS.md', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated AGENTS.md successfully!')
