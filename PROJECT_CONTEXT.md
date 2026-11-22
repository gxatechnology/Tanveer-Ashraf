# PROJECT_CONTEXT.md — Comprehensive Architecture & Feature Index

## 1. Project Identification & Overview
- **Project Title:** Tanveer Ashraf — Judicial Prep 2026–27
- **Baseline Version:** Version 3.0 — Phase 5 (Final Integration, Legal Content Audit, Advanced UI Polish, Performance Optimization & Production Readiness)
- **Primary Beneficiary:** Tanveer Ashraf (UP PCS-J Aspirant)
- **Architect & Developer:** Tauqeer Ashraf
- **Objective:** Private, highly structured digital study room, mock examination simulator, and cognitive legal gaming arena for the Uttar Pradesh Judicial Services Examination (UP PCS-J).
- **Live URL:** [https://tanveer-ashraf-judicial.vercel.app](https://tanveer-ashraf-judicial.vercel.app)
- **GitHub Repository:** [https://github.com/gxatechnology/Tanveer-Ashraf](https://github.com/gxatechnology/Tanveer-Ashraf)
- **Production Branch:** `main` (Baseline V2.0 Commit: `3a94255`)
- **Hosting Environments:** Vercel (CI/CD connected to `main`) and Hostinger static web hosting.

---

## 2. Directory Structure & Complete 21-Page Inventory
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
├── library.html                          # 12. Previous Year Question Library
├── bns.html                              # 13. Bharatiya Nyaya Sanhita (BNS) Section Library
├── search.html                           # 14. Advanced Multi-Corpus Smart Legal Search (V3.0 Phase 5)
├── tests.html                            # 15. Examination & Mock Test Simulator
├── exam.html                             # 16. Active Full-Screen Examination Interface
├── results.html                          # 17. Advanced Analytics, Examination History & Backup (V3.0 Phase 5)
├── review.html                           # 18. Detailed Post-Examination Question Review
├── revision.html                         # 19. Unified Smart Revision Centre (V3.0 Phase 5)
├── syllabus.html                         # 20. UP PCS-J Official Syllabus & Bare Act Reader
├── about.html                            # 21. Candidate & Developer Attribution Page
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
│   └── games/
│       ├── css/
│       │   ├── arena.css                 # Brain Arena dashboard styling
│       │   ├── games.css                 # Shared card, HUD, and audio styles
│       │   ├── detective.css             # Investigation board styles
│       │   ├── courtroom.css             # Courtroom simulation styles
│       │   ├── puzzle-games.css          # Crossword and Scramble styling
│       │   ├── myth-buster.css           # Chamber of Truth & Scales of Justice styles
│       │   └── judiciary-journey.css     # Campaign map, missions & completion styles
│       ├── data/
│       │   ├── characters.js             # 12 mentor & character profiles
│       │   ├── legal-game-content.js     # Memory match & section sprint cards
│       │   ├── detective-cases.js        # 6 authored criminal investigations
│       │   ├── courtroom-cases.js        # 6 authored judicial bench proceedings
│       │   ├── legal-vocabulary.js       # 285 authenticated legal vocabulary terms
│       │   ├── crossword-puzzles.js      # 30 mathematically verified crossword grids
│       │   ├── legal-myths.js            # 330 verified statutory propositions
│       │   ├── journey-chapters.js       # 9 campaign chapters
│       │   └── journey-missions.js       # 36 connected campaign missions
│       ├── js/
│       │   ├── game-storage.js           # Persistent storage (`tanveer-arena-v1`)
│       │   ├── game-audio.js             # Web Audio API sound synthesizers
│       │   ├── achievements.js           # 38 judicial achievement honors
│       │   ├── game-engine.js            # Core gamification controller
│       │   ├── detective-engine.js       # Evidence board & deduction engine
│       │   ├── courtroom-engine.js       # Bench proceedings & order builder
│       │   ├── vocabulary-engine.js      # Word scramble & spaced repetition
│       │   ├── crossword-engine.js       # Crossword grid solver & clue engine
│       │   ├── myth-engine.js            # Myth evaluation & confidence scoring
│       │   ├── myth-buster.js            # Myth Buster UI controller
│       │   ├── mastery-engine.js         # Multi-discipline competence calculator
│       │   ├── learning-plan.js          # Deterministic daily study plan generator
│       │   ├── mission-engine.js         # Campaign mission executor & tracking
│       │   ├── journey-engine.js         # Campaign map state manager
│       │   └── judiciary-journey.js      # Road to Judiciary UI controller
│       └── images/
│           ├── cards/                    # 8 high-res SVG game cover artworks
│           ├── characters/               # Illustrated character SVGs across games
│           ├── environments/             # Cinematic environment backdrops
│           └── screenshots/              # Comprehensive visual verification gallery
```

---

## 3. Storage Architecture & Unified Backup
1. **`tanveer-pcsj-portal-v1`:**
   - Stores PYQ test results (`history`), saved questions (`saved`), studied markers (`read`), and active test state (`active`).
2. **`tanveer-bns-bookmarks-v1`:**
   - Stores bookmarked BNS section numbers.
3. **`tanveer-arena-v1`:**
   - Stores:
     - `xp`, `level`, `streak`
     - `history` of game sessions
     - `unlockedAchievements` (38 badges)
     - `journey`: `completedMissions` (36 missions), `unlockedChapters` (9 chapters), `activeMissionId`
     - `personalBests` across all 8 games
     - `weakKnowledge` & `misconceptions` queue
4. **Unified Backup (`v3.0.0-unified-backup`):**
   - Single-file export/import bundling all three stores into a timestamped, validated JSON structure.
