# AGENTS.md — Development Guidelines & Permanent Operational Rules

## 1. Project Overview & Operational Mission
- **Project Name:** Tanveer Ashraf — Judicial Prep 2026–27
- **Current Baseline:** Version 3.1 — Phase 5 (Complete Social Legislation Learning Academy, Nine Special Acts, Thematic Study Centre, and Statutory Explorer)
- **Author & Developer:** Tauqeer Ashraf
- **Candidate & Learner:** Tanveer Ashraf
- **Target Examination:** Uttar Pradesh Judicial Services Examination (UP PCS-J)
- **Nature of Project:** Highly focused, private, static web application designed for rigorous judicial examination preparation.

---

## 2. Core Architectural & Technology Constraints
1. **Strictly Vanilla Multi-Page Static Site:**
   - Built exclusively with semantic HTML5, modern CSS3, and vanilla JavaScript (ES6+).
   - **No frameworks or libraries:** Do NOT introduce React, Vue, Svelte, Angular, Next.js, Vite, Webpack, Tailwind CSS, Bootstrap, jQuery, or Node.js build steps.
   - **Zero backend dependencies:** No server-side runtime, no PHP, no Python server, no SQL/NoSQL databases, and no paid/external API dependencies.
   - All study, examination, and cognitive gaming modules run 100% client-side in standard desktop and mobile browsers.
2. **Hosting & Deployment Environments:**
   - **Production (Primary):** Vercel project `gxa-tech/tanveer-ashraf-judicial`, linked to GitHub repository `https://github.com/gxatechnology/Tanveer-Ashraf.git` (`main` branch triggers auto-deployment).
   - **Alternative (Static):** Hostinger file manager / static hosting (`public_html`).
   - Relative path resolution must be strictly maintained across all 27 operational HTML pages and asset folders (`assets/css/`, `assets/data/`, `assets/js/`, `assets/images/`, `assets/games/`, `assets/learning/`, `resources/`).
3. **Deployment Safety Rules:**
   - **NEVER** automatically commit, push to GitHub, or trigger Vercel deployment unless explicitly requested by the user.
   - **NEVER** delete, alter, or corrupt `.git`, `.vercel`, `.htaccess`, or `robots.txt`.
   - Never create alternate git branches or new repositories unless instructed.
   - Always run pre-deployment automated validation (`python scripts/validate_production.py`) before proposing deployment.

---

## 3. UI/UX & Design Preservation Rules
1. **Preserve the Judicial Design Language:**
   - The interface embodies an academic, dignified judicial atmosphere.
   - Retain the judicial scales and court emblem (`assets/images/emblem.svg`).
   - Never replace the custom judicial visual identity with generic dashboard templates.
   - Never use official government, High Court, Supreme Court, or UPPSC seals or logos to avoid any false implication of official affiliation.
2. **Core Palette Tokens (from `assets/css/site.css`):**
   - Midnight Navy: `#142c46` (with dark variant `#1b3857`, hero gradient `#16314c` to `#1b5365`)
   - Judicial Green / Deep Teal: `#137d72` (accent tags `#246c63`, backgrounds `#edf7f4`)
   - Antique Gold: `#e7c88c`, `#dfbf80`, `#b98a38` (border accents `#cdb17d`, `#d4b67e`)
   - Classic Ivory / Clean Paper: `#f3f5f8`, `#f4f3ef`, `#fff`
   - Dark Slate / Ink: `#1c2e40`
   - Muted Slate: `#607387`
   - Warning / Issue Crimson: `#a63b49`
3. **Typography & Hierarchies:**
   - Headings, big scores, year cards, and BNS section badges use classic serif: `Georgia, serif`.
   - Body copy, buttons, inputs, and question options use clean system font stacks: `system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`.
4. **Responsive Layouts:**
   - Preserve sidebar-to-horizontal-scroller breakpoint at `760px`.
   - Preserve compact mobile typography adjustments at `390px`.
   - Ensure distraction-free examination layout during test simulations.
   - Include print-specific stylesheets cleanly formatting study documents and hiding interactive navigation elements.

---

## 4. Personal Branding & Media Asset Rules
1. **Candidate Portrait (Tanveer Ashraf):**
   - High-resolution advocate attire portraits: `assets/images/tanveer.webp` and `assets/images/tanveer-original.webp`.
   - Displayed in the Dashboard Hero with gold ring aura, About page, and top navigation avatar.
   - **STRICT PROHIBITION:** Do not regenerate, alter, filter, replace, or distort this portrait.
2. **Developer Portrait (Tauqeer Ashraf):**
   - High-resolution monochrome portrait: `assets/images/tauqeer.webp` and `assets/images/tauqeer-original.webp`.
   - Displayed in the sidebar profile component and About page.
   - **STRICT PROHIBITION:** Do not remove, replace, or modify this attribution.

---

## 5. Previous Year Question (PYQ) Data Integrity Rules
1. **Historical Authenticity:**
   - The question bank (`assets/data/questions.js`) comprises 1,800 historical question slots across 6 UP PCS-J years (2012, 2013, 2015, 2016, 2018, 2023) covering General Knowledge (Paper I) and Law (Paper II).
   - **NEVER** synthesize, guess, or invent missing previous-year questions. Question slot `2016-GK-31` is intentionally empty and marked non-eligible.
   - **NEVER** overwrite historical legal statutes (e.g., IPC 1860, CrPC 1973, Evidence Act 1872) with modern statutes (BNS, BNSS, BSA) inside the PYQ database. Historical questions reflect the law in force at the time of examination.
2. **Scoring Eligibility:**
   - Only questions with `eligible: true` (1,757 questions) participate in scored tests.
   - Ineligible questions (`eligible: false`, 43 questions) due to deleted keys, disputed questions, or OCR ambiguities must remain review-only.
   - Do NOT silently change answer keys.

---

## 6. Multi-Corpus Smart Search Rules
1. **Multi-Corpus Indexing:**
   - Smart search (`assets/js/legal-search.js` & `search.html`) searches across five distinct datasets:
     1. BNS 2023 Section Headings (`window.BNS_SECTIONS`)
     2. Historical PYQ Question Bank (`window.PCSJ_QUESTIONS`)
     3. Legal Vocabulary & Maxims (`window.ARENA_VOCABULARY`)
     4. Legal Myth Propositions (`window.ARENA_MYTHS`)
     5. Judicial Learning Academy Constitution Topics & MCQs (`window.CONSTITUTION_TOPICS` & `window.CONSTITUTION_MCQS`)
2. **Debouncing & Sanitization:**
   - All input queries are debounced (200ms) and rendered via XSS-safe text nodes or HTML escape routines.
   - Search results must remain clearly grouped with badge labels identifying their corpus.

---

## 7. User Data, Storage Keys & Unified Backup
1. **Storage Keys in Use:**
   - `tanveer-pcsj-portal-v1`: Stores saved questions (`saved`), studied markers (`read`), test result history (`history`), and active in-progress test (`active`).
   - `tanveer-bns-bookmarks-v1`: Stores bookmarked BNS section numbers.
   - `tanveer-arena-v1`: Dedicated cognitive gaming arena storage (XP, levels, achievements, case files, crossword puzzles, scramble ciphers, spaced repetition, vocabulary mastery, myth buster records, and campaign journey missions).
   - `tanveer-learning-v1`: Dedicated Subject-wise Judicial Learning Academy storage (topic completion markers, practice test records, question bookmarks, missed/wrong question queue, and subject accuracy KPIs).
2. **Unified Backup & Data Safety:**
   - Never reset, overwrite, or corrupt these keys.
   - Versioned export (`exportProgress`) exports all four keys into a single JSON schema (`v3.1.0-unified-backup`).
   - Versioned import (`importProgress`) safely verifies schema, parses JSON, and restores keys with confirmation dialog.

---

## 8. Verification & QA Protocol Before Any Proposed Change
1. Validate syntax of all JavaScript files without syntax or runtime console errors.
2. Verify that all 27 operational HTML pages load required assets correctly via relative paths.
3. Run `python scripts/validate_production.py` and `python scripts/validate_learning_academy.py` and ensure 100% test pass rate.
4. Test client-side navigation across all views and URL parameter sync (`?subject=...`, `?chapter=...`, `?topic=...`, `?mode=...`, `?missionId=...`, `?caseId=...`, `?puzzle=...`).
5. Confirm that no personal photographs or branding elements are altered.

---

## 9. Legal Brain Arena & Complete 8-Game Roster (V3.0 Phase 5 Baseline)
All eight games and supporting subsystems are 100% playable client-side with persistent progression:
1. **Game 1: Legal Memory Match (`memory-match.html`):** 3D statutory and maxim matching.
2. **Game 2: Section Sprint (`section-sprint.html`):** High-speed BNS 2023 statutory recall.
3. **Game 3: Legal Detective: The Case Files (`legal-detective.html`):** 6 criminal investigations.
4. **Game 4: Be the Judge: The Courtroom (`courtroom.html`):** 6 judicial bench proceedings.
5. **Game 5: Legal Crossword: The Lexicon Chamber (`crossword.html`):** 30 validated statutory crosswords.
6. **Game 6: Legal Word Scramble: The Code Breaker (`word-scramble.html`):** 8 decryption modes & 5 Mystery Manuscripts.
7. **Game 7: Legal Myth Buster: The Chamber of Truth (`myth-buster.html`):** 8 playable modes, 330 verified statutory propositions, animated scales of truth, and non-punitive confidence calibration.
8. **Game 8: Road to Judiciary: The Learning Journey (`judiciary-journey.html`):** 9 campaign chapters, 36 connected missions, daily study plan recommender, objective learning progress, and personal educational completion certificate with prominent disclaimer.
9. **Achievement Gallery (`achievements.html`):** 38 judicial honors and milestone badges.
10. **Character Roster (12 Mentors):** Det. Arjun Rathore, Adv. Kabir Mehta, Adv. Ananya Rao, Adv. Aditya Malhotra, Chief Judge Nandini Sen, Justice Vikram Sahay, Prof. Kavita Sharma, Dr. Devendra Bose, Prof. Aditi Menon, Adv. Siddharth Kapoor, plus supporting witnesses.

---

## 10. Subject-Wise Judicial Learning Academy (V3.1 Phase 6 Baseline)
Structured subject-by-subject curriculum for the UP PCS-J Preliminary Examination:
1. **Subject Registry (assets/learning/data/subjects.js):** 30 subjects defined across Paper I (12 GK + 9 Social Legislation) and Paper II (9 Law + sub-modules). Twenty-two subjects are active production modules:
   - 8 Paper II Law Modules: law-constitution, law-jurisprudence, law-contract, law-tpa, law-criminal, law-crpc, law-evidence, law-cpc.
   - 9 Paper I Social Legislation Acts: soc-disabilities, soc-parents, soc-dowry, soc-domestic-violence, soc-posh, soc-pcpndt, soc-mtp, soc-indecent-rep, soc-pocso.
   - 5 Paper I General Knowledge Modules: gk-history, gk-culture, gk-geography, gk-polity, gk-economy.
   - 8 subjects remain structured upcoming modules.
2. **Active Academic Modules Across 22 Subjects:**
   - **8 Law Paper II Subjects:** 99 Chapters, 289 Topics, 2,620 MCQs, 592 PYQs, 72 SVG Schematics.
   - **9 Social Legislation Paper I Acts:** 28 Chapters, 84 Topics, 455 MCQs, 23 PYQs, 18 SVG Schematics.
   - **5 General Knowledge Paper I Modules:** 65 Chapters, 162 Topics, 700 MCQs, 228 PYQs, 15 SVG Schematics.
   - **Combined Academy Totals:** 192 Chapters, 535 Topics, 535 Authored Concept Notes, 3,775 Verified Practice MCQs, 843 Mapped Authentic Historical PYQs, 105 Custom Vector SVG Schematics.
3. **Statutory Comparison Lab (comparison-lab.html):**
   - 79 verified comparative transitions (30 BNS vs IPC, 21 BNSS vs CrPC, 28 BSA vs IEA), live debounced search, category filtering, KPI summaries, and Section 106(2) BNS hit-and-run non-commencement notice (MHA Notification S.O. 850(E)).
4. **The Civil Suit Journey Simulator (civil-suit-journey.html):**
   - 14 interactive procedural stages ('From Plaint to Decree') with distinct procedural stream tagging (standard progression vs parallel execution/interlocutory streams), Presiding Officer Scrutiny Checklists, High-Yield Traps, Landmark Precedents, Scenario Simulators, and master structural flowchart.
5. **Two High-Yield Statutory Explorers (181 Entries Total):**
   - **CPC Section-Order-Rule Explorer (`cpc-sections-orders-rules.js`):** 83 high-yield statutory entries (48 Sections, 35 Rules).
   - **Social Legislation Sections Explorer (`social-sections-explorer.js`):** 98 high-yield statutory entries across all 9 Acts with conditions, exceptions, penalties, India Code links, and tailored UP Exam Tips.
6. **Social Legislation & General Knowledge Study Centres (learning-academy.html):**
   - Social Legislation: Dedicated showcase organized into three thematic clusters: Group A (Equality, Inclusion & Welfare), Group B (Protection of Women), and Group C (Reproductive Health & Child Protection).
   - General Knowledge: Dedicated showcase covering Indian History, Indian Culture, Indian Geography, Indian Polity, and Indian Economy with filter tabs, active counts, and direct study access.
7. **Interactive Study Room (subject-study.html):**
   - Detailed Study Mode & Quick Revision Mode with bare act callouts, landmark case judgments, active recall flashcards with 3D flip interaction, paired-law switcher, and 105 custom SVG diagrams.
8. **Comprehensive Practice MCQ Bank (topic-practice.html):**
   - 3,775 verified questions with comprehensive 4-option explanations (A, B, C, D), statutory/historical provisions, and learning objectives across 8 practice modes.
9. **Historical PYQ Mapping Overlays:**
   - 843 authentic UP PCS-J questions mapped directly across all 22 active subjects without modifying questions.js.
10. **Subject Mastery Analytics (subject-progress.html):**
    - Real-time tracking of topic reading coverage, test accuracy, spaced repetition queues, and chapter mastery matrix across all 22 active subjects.
11. **6 Dedicated Academy, Comparison & Simulation Pages:**
    - learning-academy.html, subject-study.html, topic-practice.html, subject-progress.html, comparison-lab.html, civil-suit-journey.html (Total 27 operational HTML pages).
