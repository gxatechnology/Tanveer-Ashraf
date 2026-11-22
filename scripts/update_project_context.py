context_content = '''# PROJECT_CONTEXT.md — Comprehensive Architecture & Feature Index

## 1. Project Identification & Overview
- **Project Title:** Tanveer Ashraf — Judicial Prep 2026–27
- **Baseline Version:** Version 3.1 — Phase 5 (Complete Social Legislation Learning Academy, Nine Special Acts, Thematic Study Centre & Statutory Explorer)
- **Primary Beneficiary:** Tanveer Ashraf (UP PCS-J Aspirant)
- **Architect & Developer:** Tauqeer Ashraf
- **Objective:** Private, highly structured digital study room, mock examination simulator, and cognitive legal gaming arena for the Uttar Pradesh Judicial Services Examination (UP PCS-J).
- **Live URL:** [https://tanveer-ashraf-judicial.vercel.app](https://tanveer-ashraf-judicial.vercel.app)
- **GitHub Repository:** [https://github.com/gxatechnology/Tanveer-Ashraf](https://github.com/gxatechnology/Tanveer-Ashraf)
- **Production Branch:** `main` (Baseline V2.0 Commit: `3a94255`)
- **Hosting Environments:** Vercel (CI/CD connected to `main`) and Hostinger static web hosting.

---

## 2. Directory Structure & Complete 27-Page Inventory
```
Tanveer_Ashraf_Judicial/
│
├── .git/                                 # Git tracking directory (branch: main)
├── .vercelignore                         # Excludes dev scripts, generators & test files
├── .htaccess                             # DirectoryIndex index.html & Options -Indexes
├── robots.txt                            # Disallow: / (blocks search indexing)
├── README_UPLOAD.txt                     # Hostinger deployment & release documentation
├── AGENTS.md                             # Permanent operational & technology rules
├── PROJECT_CONTEXT.md                    # Project index, file map & architecture
├── DESIGN_SYSTEM.md                      # Complete UI tokens, palettes & typography
├── PROJECT_STATUS.md                     # Current audit metrics & verification status
├── CHANGELOG.md                          # Release history across all versions & phases
├── LEGAL_CONTENT_AUDIT.md                # Comprehensive preflight audit of legal citations
├── SOCIAL_LEGISLATION_CONTENT_AUDIT.md   # Social Legislation 9-Act statutory & case law audit
├── SOCIAL_LEGISLATION_ACT_INDEX.md       # Social Legislation 98-entry high-yield statutory index
├── PHASE5_SOCIAL_LEGISLATION_QA.md       # Phase 5 QA test execution & verification report
├── LEARNING_ACADEMY_REPORT.md            # Subject-wise Learning Academy master delivery report
├── GAME_MISSION_SCHEMA.md                # Campaign progression & mission binding schema
│
├── index.html                            # 1. Master Personal Dashboard
├── brain-arena.html                      # 2. Legal Brain Arena Dashboard (All 8 Games Live)
├── memory-match.html                     # 3. Game 1: Legal Memory Match (V3.0 Phase 1)
├── section-sprint.html                   # 4. Game 2: Section Sprint (V3.0 Phase 1)
├── legal-detective.html                  # 5. Game 3: Legal Detective: The Case Files (V3.0 Phase 2)
├── courtroom.html                        # 6. Game 4: Be the Judge: The Courtroom (V3.0 Phase 2)
├── crossword.html                        # 7. Game 5: Legal Crossword: The Lexicon Chamber (V3.0 Phase 3)
├── word-scramble.html                    # 8. Game 6: Legal Word Scramble: The Code Breaker (V3.0 Phase 3)
├── myth-buster.html                      # 9. Game 7: Legal Myth Buster: The Chamber of Truth (V3.0 Phase 4)
├── judiciary-journey.html                # 10. Game 8: Road to Judiciary: The Learning Journey (V3.0 Phase 4)
├── achievements.html                     # 11. Judicial Hall of Achievements (38 Badges) (V3.0 Phase 4)
├── learning-academy.html                 # 12. Subject Academy Hub (30 Subjects, 17 Active) (V3.1 Phase 1-5)
├── subject-study.html                    # 13. Chapter & Topic Study Room (84 Topics in Social, 373 Total) (V3.1 Phase 1-5)
├── topic-practice.html                   # 14. Practice Test Engine (8 Modes, 3,075 MCQs) (V3.1 Phase 1-5)
├── subject-progress.html                 # 15. Subject Mastery Analytics & Mastery Matrix (V3.1 Phase 1-5)
├── library.html                          # 16. Previous Year Question Library
├── bns.html                              # 17. Bharatiya Nyaya Sanhita (BNS) Section Library
├── search.html                           # 18. Advanced Multi-Corpus Smart Legal Search (V3.1 Phase 1-5)
├── tests.html                            # 19. Examination & Mock Test Simulator
├── exam.html                             # 20. Active Full-Screen Examination Interface
├── results.html                          # 21. Advanced Analytics, Examination History & Backup
├── review.html                           # 22. Detailed Post-Examination Question Review
├── revision.html                         # 23. Unified Smart Revision Centre
├── syllabus.html                         # 24. UP PCS-J Official Syllabus & Bare Act Reader
├── about.html                            # 25. Candidate & Developer Attribution Page
├── comparison-lab.html                   # 26. Statutory Comparison Lab (79 Criminal Transitions & S. 106(2) Stay Alert)
├── civil-suit-journey.html               # 27. The Civil Suit Journey: From Plaint to Decree (14 Interactive Stages) (V3.1 Phase 4)
│
├── assets/
│   ├── css/
│   │   └── site.css                      # Master stylesheet with print styles & dark tokens
│   ├── data/
│   │   ├── bns.js                        # Complete 358 BNS Section Directory
│   │   └── questions.js                  # 1,800 Historical PYQ Database (2012–2023)
│   ├── js/
│   │   ├── app.js                        # Master SPA controller & examination engine
│   │   └── legal-search.js               # Multi-corpus tokenized legal search engine
│   ├── images/
│   │   ├── emblem.svg                    # Judicial scales & court emblem
│   │   ├── tanveer.webp / tanveer-original.webp # Candidate portrait (Tanveer Ashraf)
│   │   └── tauqeer.webp / tauqeer-original.webp # Developer portrait (Tauqeer Ashraf)
│   ├── games/
│   │   ├── css/                          # 7 specialized gaming stylesheets
│   │   ├── data/                         # Cases, crossword grids, myths, vocabulary, chapters
│   │   ├── js/                           # Gaming controllers, audio, deduction engines
│   │   └── images/                       # Character SVGs, environments, card covers
│   └── learning/
│       ├── css/
│       │   └── academy.css               # Comprehensive Subject Academy styles
│       ├── data/
│       │   ├── subjects.js               # 30 UP PCS-J subject registry (Paper I & II, 17 active)
│       │   ├── comparison/
│       │   │   └── criminal-statutory-comparisons.js # 79 verified criminal law transitions
│       │   ├── constitution/             # 15 Chapters, 45 Topics, 480 MCQs, 158 PYQs
│       │   ├── jurisprudence/            # 11 Chapters, 30 Topics, 240 MCQs, 45 PYQs
│       │   ├── contract/                 # 11 Chapters, 32 Topics, 260 MCQs, 82 PYQs
│       │   ├── tpa/                      # 8 Chapters, 24 Topics, 240 MCQs, 47 PYQs
│       │   ├── criminal/                 # 12 Chapters, 36 Topics, 360 MCQs, 78 PYQs
│       │   ├── crpc/                     # 12 Chapters, 35 Topics, 360 MCQs, 49 PYQs
│       │   ├── evidence/                 # 10 Chapters, 30 Topics, 280 MCQs, 73 PYQs
│       │   ├── cpc/                      # 20 Chapters, 57 Topics, 400 MCQs, 60 PYQs, 83 SOR Entries
│       │   └── social/                   # 28 Chapters, 84 Topics, 455 MCQs, 23 PYQs, 98 Sections Explorer Entries
│       ├── js/
│       │   ├── learning-storage.js       # Dedicated storage controller (`tanveer-learning-v1`)
│       │   ├── learning-engine.js        # Academy hub and chapter navigation
│       │   ├── concept-renderer.js       # Detailed & Quick study mode, flashcards, SVGs
│       │   └── practice-engine.js        # 8 practice modes, instant rationale, review link
│       └── images/
│           ├── subjects/                 # Subject icon artwork
│           └── diagrams/                 # 90 custom vector SVG schematics (18 Social added)
```

---

## 3. Storage Architecture & Unified Backup
1. **`tanveer-pcsj-portal-v1`:**
   - Stores PYQ test results (`history`), saved questions (`saved`), studied markers (`read`), and active test state (`active`).
2. **`tanveer-bns-bookmarks-v1`:**
   - Stores bookmarked BNS section numbers.
3. **`tanveer-arena-v1`:**
   - Stores gaming XP, level, streak, session history, unlocked achievements (38 badges), journey progression, personal bests, and weak knowledge queue.
4. **`tanveer-learning-v1`:**
   - Stores Subject Academy topic read markers (`completedTopics`), bookmarked questions (`bookmarks`), missed/wrong question queue (`wrongQuestions`), practice test records (`practiceHistory`), and subject accuracy KPIs across all 17 active subjects.
5. **Unified Backup (`v3.1.0-unified-backup`):**
   - Single-file export/import bundling all four stores into a timestamped, validated JSON structure with full backward compatibility for older backup versions.
'''

with open('PROJECT_CONTEXT.md', 'w', encoding='utf-8') as f:
    f.write(context_content)

print('Updated PROJECT_CONTEXT.md successfully!')
