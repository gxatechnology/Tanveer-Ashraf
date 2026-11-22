# CHANGELOG.md — Historical Releases & Version Baseline

All notable changes to the **Tanveer Ashraf — Judicial Prep** project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [3.0.0] — Phase 5 — 2026-11-22
*Tag: V3.0 Phase 5 — Final Integration, Legal Content Audit, Advanced UI Polish, Performance Optimization & Production Readiness*

### Added
- **Multi-Corpus Smart Legal Search (`assets/js/legal-search.js`, `search.html`):**
  - Expanded search indexing across four distinct legal corpuses: BNS 2023 Section Headings (358 sections), Historical PYQs (1,800 questions), Legal Vocabulary & Maxims (285 terms), and Legal Myth Propositions (330 statements).
  - Implemented 200ms input debouncing, corpus badge grouping, and strict XSS-safe escaping for all search results.
- **Unified Smart Revision Centre (`revision.html`, `assets/js/app.js`):**
  - Integrated bookmarked PYQ questions, Weak Knowledge Queue items, and high-confidence misconceptions into a single revision dashboard.
  - Interactive category filter tabs (*All Items*, *Bookmarked PYQs*, *Arena Errors & Misconceptions*), "Mark Resolved" triggers, and direct links to study sources.
- **Unified Versioned Backup & Restore (`assets/js/app.js`, `results.html`):**
  - Consolidated export and restore utility packaging all three application storage keys (`tanveer-pcsj-portal-v1`, `tanveer-arena-v1`, `tanveer-bns-bookmarks-v1`) into a single versioned JSON format (`v3.0.0-unified-backup`).
  - Added schema validation, safety confirmation prompt, and granular key restore reporting.
- **Dedicated Print & Offline Export Stylesheet (`assets/css/site.css`):**
  - Comprehensive `@media print` styling cleanly hiding navigation menus, action buttons, floating HUDs, and background shadows.
  - Formats judicial notes in legible academic serif typography with an official educational disclaimer footer.
- **Automated Production Validation Suite (`scripts/validate_production.py`):**
  - Automated regression and dataset verification script running 21 checks across HTML pages, asset links, JavaScript syntax, dataset integrity, and branding assets (21/21 passed).
- **Vercel Production Bundle Filter (`.vercelignore`):**
  - Configured deployment filter excluding developer scripts, generator utilities, test files, and local logs from production bundles.

### Changed & Corrected
- **Simulated Judicial Appointment Replaced:**
  - Permanently replaced simulated judicial appointments and official warrants with *ROAD TO JUDICIARY — LEARNING JOURNEY COMPLETED: Personal Educational Achievement* (`journey-engine.js`, `judiciary-journey.js`, `achievements.js`).
  - Embedded prominent educational disclaimer specifying that the milestone represents personal educational achievement and does not constitute an official appointment from the High Court, UPPSC, or State Government.
- **Confidence Challenge Non-Punitive Calibration:**
  - Removed punitive negative point wagering ($-5$, $-10$, $-20$); implemented non-punitive confidence calibration (`myth-engine.js`, `myth-buster.js`).
  - Completion summary generates a Confidence Calibration Report highlighting dangerous misconceptions (high confidence, wrong answer) and hesitant knowledge (low confidence, correct answer).
- **Objective Personal Learning Progress:**
  - Replaced simulated readiness rankings with *Personal Learning Progress* (`mastery-engine.js`, `judiciary-journey.js`).
  - Enforced a minimum data threshold of $\ge 3$ completed activities before computing competence percentages to avoid premature predictions.
  - Restructured progress levels into 5 educational mastery tiers (*Foundational Aspirant* to *Comprehensive Mastery*).
- **Campaign Integration & Mission Parameter Routing:**
  - Updated `legal-detective.js` and `courtroom.js` to normalize both `caseId` and `case` URL parameters (`case-1` -> `det-case-1` / `court-case-1`), preventing broken mission routing.
  - Ensured all 36 campaign missions contain explicit `missionId` query parameters.
- **Master Dashboard UI Polish (`index.html`, `assets/js/app.js`):**
  - Redesigned hero section with academic judicial typography and candidate aura.
  - Added dynamic "Continue Learning" banner resuming active campaign missions or in-progress mock tests.
  - Added Quick Actions grid with 6 core navigation shortcuts and Brain Arena Spotlight card.
- **Advanced Performance Analytics (`results.html`, `assets/js/app.js`):**
  - Separated official examination simulation metrics (Paper I GK & Paper II Law) from cognitive gaming metrics (XP, Streaks, Accuracies).
  - Added CSS progress bar charts, subject performance breakdowns, and informative empty-state guides.
- **Authoritative Case Metadata Enrichment:**
  - Enriched all 6 Detective cases and all 6 Courtroom proceedings with `status: "Verified against authoritative source"`, specific India Code handles, and `scorable: true`.

---

## [3.0.0] — Phase 4 — 2026-11-22
*Tag: V3.0 Phase 4 — Advanced Legal Mastery, Myth Buster & Judicial Career Journey*

### Added
- **Game 7: Legal Myth Buster: The Chamber of Truth (`myth-buster.html`, `assets/games/js/myth-buster.js`, `myth-engine.js`, `myth-buster.css`):**
  - High-precision statutory truth examination chamber designed to dismantle pervasive legal misconceptions and multiple-choice prelims traps.
  - Database of 330 unique, verified legal statements (`assets/games/data/legal-myths.js`) across 12 legal disciplines (212 True, 91 False with exact error phrases and statutory corrections, 27 Depends with qualifying exceptions, and 64 old-to-new transition mappings).
  - 8 distinct playable modes:
    1. *Classic Myth Buster*: Evaluate statutory statements with three-way verdicts (True, False, Depends).
    2. *Find the Legal Error*: Pinpoint the exact flawed statutory phrase within an incorrect proposition.
    3. *Correct the Law*: Select the authentic statutory replacement to cure a legal misconception.
    4. *Exception Hunter*: Identify statutory provisos, non-obstante clauses, and qualifying exceptions.
    5. *Old Law vs New Law*: Master 2024 statutory transitions from IPC/CrPC/IEA to BNS/BNSS/BSA 2023.
    6. *Judicial Precedent Challenge*: Differentiate binding ratio decidendi from obiter dicta across landmark Supreme Court judgments.
    7. *Confidence Challenge*: Wager conviction points (Low 1x, Medium 1.5x, High 2x) before verdict reveals.
    8. *The Grand Truth Trial*: 20-question comprehensive timed examination simulation across all 12 legal disciplines.
  - Interactive animated Central Scales of Justice (`#centralScales`) tilting left on False (-14deg), right on True (+14deg), and equipoise (0deg) on Depends.
  - Comprehensive educational feedback card with detailed statutory analysis, common trap explanations, qualifying provisos, and direct links to official India Code / Supreme Court authorities.
  - Dynamic mentor dialogue featuring Prof. Aditi Menon (`aditi.svg`) and Adv. Siddharth Kapoor (`siddharth.svg`).
- **Game 8: Road to Judiciary: The Rise of a Judge (`judiciary-journey.html`, `assets/games/js/judiciary-journey.js`, `journey-engine.js`, `mission-engine.js`, `judiciary-journey.css`):**
  - Epic 9-chapter judicial career campaign (`journey-chapters.js`) simulating the progression from Law Student to confirmed District & Sessions Judge.
  - 36 authored campaign missions (`journey-missions.js`) with authentic cross-game bindings (Memory Match, Section Sprint, Detective Cases, Courtroom Trials, Crossword Puzzles, Word Scramble Ciphers, Myth Buster Trials, and PYQ Test Centre).
  - Interactive SVG campaign map viewport (`journey-map.svg`) featuring 9 clickable landmarks, tooltips, and completion tracking.
  - Real-time Multi-Discipline Competence Matrix (`mastery-engine.js`) tracking percentage mastery across all 12 UP PCS-J legal disciplines.
  - Personalized Daily Learning Plan generator (`learning-plan.js`) offering deterministic study schedules for 15, 30, 45, and 60-minute preparation budgets.
  - Formal Warrant of Appointment decree modal on parchment with the Constitutional Oath of Office upon completing the campaign.
- **Achievement Gallery (`achievements.html`):**
  - Dedicated judicial trophy cabinet showcasing all 38 judicial honors across 5 categories.
  - 16 new Phase 4 achievement badges (8 Myth Buster honors + 8 Road to Judiciary campaign milestones).
  - Progress tracking, category filtering, candidate level analytics, and JSON export/import utilities.
- **Universal Mission Integration Hook (`game-storage.js`, `app.js`):**
  - Seamless `?missionId=...` propagation across all 8 games and the PYQ test centre.
  - Automated mission recording in `tanveer-arena-v1.journey.completedMissions` with zero disruption to parent storage keys.
- **New Illustrated Characters & Cinematic Environments:**
  - Characters: Prof. Aditi Menon (`aditi.svg`, Constitutional Law Scholar) and Adv. Siddharth Kapoor (`siddharth.svg`, Legal Fact-Checking Mentor).
  - Environments: The Chamber of Truth (`truth-chamber.svg`) and Campaign Map (`journey-map.svg`).
- **Preflight Audit & Architecture Documentation:**
  - `LEGAL_CONTENT_AUDIT.md`: Preflight verification audit across all Phase 2 and Phase 3 legal content.
  - `GAME_MISSION_SCHEMA.md`: Complete mission structure, URL bindings, and mastery formulas.
  - `PHASE4_QA_REPORT.md`: Comprehensive visual and functional QA report with 25 browser screenshots.

---

## [3.0.0] — Phase 3 — 2026-11-22
*Tag: V3.0 Phase 3 — Advanced Legal Vocabulary & Cognitive Puzzle Games*

### Added
- **Game 5: Legal Crossword: The Lexicon Chamber (`crossword.html`, `assets/games/js/crossword.js`, `crossword-engine.js`):**
  - 30 mathematically verified, 100% intersecting statutory crossword puzzles spanning 10 Beginner (8x8), 10 Intermediate (10x10), and 10 Advanced (12x12) grids.
  - Covers all 12 planned thematic collections: Constitutional Prerogatives, General Exceptions (BNS), Offences Against Body, Property & Fraud, Code of Civil Procedure, Bharatiya Sakshya Adhiniyam, Legal Maxims & Latin Equity, Landmark Jurisprudence, Social Legislations, Evidence & Presumptions, Criminal Conspiracies, and Natural Justice & Writs.
  - Interactive crossword features:
    - Direction toggle (Across / Down) on cell click or DIR key.
    - Synchronized dual clue scroll panes (Across & Down) with line-through strikeout on solved words.
    - Active Clue Ribbon above grid with clue badge and prompt.
    - On-screen touch keyboard for mobile/tablet with DIR toggle and backspace.
    - Physical keyboard support (letters, arrows, backspace, tab, enter).
    - Smart hint system: Reveal Letter (-15 pts penalty) and Reveal Word (-50 pts penalty).
    - Compact educational definition dock displaying verified Indian statutory definitions and precedents on word solution.
    - Lexicon Chamber Master Certificate completion view with score, accuracy %, hints penalty deduction, and academic evaluation by Dr. Devendra Bose.
- **Game 6: Legal Word Scramble: The Code Breaker (`word-scramble.html`, `assets/games/js/word-scramble.js`, `vocabulary-engine.js`):**
  - 8 distinct cryptographic decryption game modes:
    1. *Classic Mode*: Single legal words with progressive difficulty (Beginner -> Intermediate -> Advanced).
    2. *Legal Maxims Mode*: Decode foundational Latin maxims and equity tenets.
    3. *Definition Challenge Mode*: Deduce terms from authentic statutory definitions.
    4. *Statutory Keywords Mode*: High-frequency keywords from BNS 2023, BSA 2023, and CPC 1908.
    5. *Landmark Cases Mode*: Doctrines and precedent titles.
    6. *Memory Recall Mode*: 3-second flash preview before scrambling; spells from memory.
    7. *Time Attack Mode*: 60-second rapid unscrambling chain with +10s bonus per word and combo multiplier.
    8. *Mystery Manuscript Mode*: 5 ancient thematic judicial codices (*The Constitutional Archive*, *The Criminal Law Dossier*, *The Evidence Vault*, *The Book of Legal Maxims*, *The Civil Justice Manuscript*) requiring 5 linked passwords each to unlock and illuminate historical codex scrolls.
  - Tactile metallic letter tiles with brass bevels, gold foil lettering, drag-and-drop, touch tap-to-place, and physical keyboard entry (A-Z, Backspace, Enter, Esc).
  - Combination Lock HUD with dials for Decipher Streak, Score, Multiplier ($1.0\times$ to $3.0\times$), and Timer.
  - Tactical commentary and mnemonics from Adv. Kabir Mehta and Prof. Kavita Sharma.
- **Authoritative Legal Datasets & Engines:**
  - `legal-vocabulary.js`: 285 unique, authenticated legal terminology entries across 10 subject disciplines with canonical spellings, accepted variants, difficulty levels, primary clues, additional hints, statutory definitions, educational examples, authentic authorities, and official India Code / eCourts source URLs.
  - `crossword-puzzles.js`: 30 validated puzzle configurations with 100% letter multiset intersection consistency and reading-order numbering.
  - `vocabulary-engine.js`: Shared engine for normalization, character multiset validation, Fisher-Yates word boundary-preserving scrambler, deterministic daily seed generator, and Leitner spaced repetition interval scheduler.
  - `crossword-engine.js`: Pure matrix crossword engine handling cell coordinate mappings, clue lookup, error checking, and 100-pt scoring math.
- **New Characters & Cinematic Environments:**
  - Character 9: Prof. Kavita Sharma (`kavita.svg`, Age 46, Legal Vocabulary Mentor).
  - Character 10: Dr. Devendra Bose (`devendra.svg`, Age 62, Keeper of the Legal Archives).
  - Environment 3: The Grand Lexicon Chamber (`lexicon.svg`, law library with mahogany stacks and banker's lamps).
  - Environment 4: The Code Breaker Laboratory (`codebreaker.svg`, cryptographic bench with cipher dials and gold tiles).
- **Audio Synthesizer & Achievements Extension:**
  - Added 6 procedural Web Audio sound effects: `playTileClick`, `playTileSnap`, `playTileShuffle`, `playCrosswordTick`, `playWordSolve`, `playManuscriptReveal`.
  - Added 8 new Phase 3 judicial honor badges in `achievements.js`: *First Crossword*, *Lexicon Explorer*, *Crossword Master*, *Latin Maxims Scholar*, *First Code Breaker*, *Vocabulary Virtuoso*, *Manuscript Unlocked*, and *Legal Language Master* (22 total achievements).
  - Extended `tanveer-arena-v1` storage schema with `crossword`, `scramble`, and `vocabularyMastery` spaced repetition tracking.
- **Dashboard Updates (`brain-arena.html`):**
  - Activated Legal Crossword (Game 5) and Legal Word Scramble (Game 6) with `● PLAYABLE` status badges and direct navigation links.
  - Updated arena banner to "Phase 3: 6 Live Games · 2 In Development".
  - Updated recent trials history table to display Crossword and Word Scramble sessions.

---

## [3.0.0] — Phase 2 — 2026-11-22
*Tag: V3.0 Phase 2 — Cinematic Legal Detective & Virtual Courtroom Simulation*

### Added
- **Game 3: Legal Detective: The Case Files (`legal-detective.html`, `assets/games/js/legal-detective.js`):**
  - Six deeply authored criminal cases under the Bharatiya Nyaya Sanhita, 2023 and Bharatiya Sakshya Adhiniyam, 2023.
  - Multi-stage investigation pipeline:
    - Stage 1: Case Briefing & Initial Facts (Lead Investigator Det. Arjun Rathore).
    - Stage 2: Exhibits Inspection & BSA 2023 Relevance Determination (CCTV, receipts, ownership slips).
    - Stage 3: Witness Examination & Interrogation (branching dialogue, credibility testing, fact discovery).
    - Stage 4: Interactive Corkboard Evidence Board (linking physical clues to statutory ingredients).
    - Stage 5: Formal Legal Deduction (formulating charge-sheet offenses under BNS 2023).
    - Stage 6: Investigation Report & 100-Point Rubric Debrief with authoritative citations.
- **Game 4: Be the Judge: The Courtroom (`courtroom.html`, `assets/games/js/courtroom.js`):**
  - Six comprehensive judicial proceedings across Civil Procedure (Order 39 CPC), Criminal Procedure (BNSS 483 Bail), Evidence (BSA 63 Electronic Evidence Certificate), Circumstantial Chains, and Constitutional Writs (Article 226).
  - Multi-stage judicial hearing pipeline:
    - Stage 1: Cause List & Calling the Case (Court Clerk Nandini Sharma).
    - Stage 2: Bar Submissions — Opposing Counsel Arguments (Adv. Ananya Rao & Adv. Aditya Malhotra).
    - Stage 3: Exhibits & Evidentiary Records with official crimson court seal stamp.
    - Stage 4: Judicial Inquiry from the Bench.
    - Stage 5: Framing of Core Legal Issues.
    - Stage 6: Pronouncing the Operative Ruling.
    - Stage 7: Structured Reasoned Order Builder (Section I: Facts, Section II: Law & Precedents, Section III: Operative Order).
    - Stage 8: Mentor Critique & Judicial Evaluation (Justice Vikram Sahay).
- **Shared Character Manifest & Engines (`characters.js`, `character-engine.js`, `dialogue-engine.js`):**
  - Eight recurring judicial characters with dedicated SVG portraits, unique vocal tones, and calibrated speech rates.
  - Typewriter letter-by-letter dialogue animation with instant skip, audio ticks, and optional Web Speech API TTS.
  - Official Examination Transcript viewer logging all statements with timestamps.
- **Interactive Evidence Board (`evidence-board.js`):**
  - Realistic corkboard gradient with wooden trim, pushpin clue nodes, statutory element target slots, and live link verification.
- **Extended Persistence & Achievements Engine:**
  - Extended `tanveer-arena-v1` schema in `game-storage.js` to store detective and courtroom case history and personal bests without affecting Phase 1 progress.
  - Added six new judicial achievements in `achievements.js`: *First Investigation*, *Master of Evidence*, *Master Deduction*, *First Judicial Order*, *Judicial Scholar*, and *Procedural Mastery* (14 total honors).
  - Enhanced procedural synthesizer in `game-audio.js` with gavel strikes, paper rustles, clue discovery pings, and typewriter clicks.
- **Dashboard Updates (`brain-arena.html`):**
  - Promoted Legal Detective and Be the Judge to `● PLAYABLE` status with active launch buttons.
  - Updated live arena counter to "Phase 2: 4 Live Games · 4 In Development".

---

## [3.0.0] — Phase 1 — 2026-11-22
*Tag: V3.0 Phase 1 — Advanced Legal Brain Arena & Educational Gaming Engine*

### Added
- **Legal Brain Arena Dashboard (`brain-arena.html`):**
  - Central cognitive training hub combining active recall, memory improvement, and rapid statutory response for UP PCS-J.
  - Live learner metrics tracking Total Learning XP, Current Level, Daily Streak, Games Completed, Overall Accuracy %, and Spaced Repetition Weak Queue.
  - Level Progression System spanning 6 judicial ranks (Level 1 "Law Explorer" to Level 6 "Judiciary Champion").
  - Daily Cognitive Challenge generator with bonus XP rewards.
  - Eight premium judicial game cards with original SVG artwork:
    1. *Legal Memory Match* (Playable)
    2. *Section Sprint* (Playable)
    3. *Legal Detective* (Phase 2 Upcoming)
    4. *Be the Judge* (Phase 2 Upcoming)
    5. *Legal Crossword* (Upcoming)
    6. *Legal Word Scramble* (Upcoming)
    7. *Legal Myth Buster* (Upcoming)
    8. *Road to Judiciary* (Upcoming)
  - Subject Mastery Distribution bars (BNS, Constitution, Legal Maxims, Landmark Cases).
  - Judicial Honors & Milestones showcase tracking 8 unlockable badges.
  - Rolling session history table and dedicated JSON export/reset controls.
- **Game 1: Legal Memory Match (`memory-match.html`, `assets/games/js/memory-match.js`):**
  - 3D interactive memory card pairing board with realistic flip physics (`perspective: 1000px`, `transform-style: preserve-3d`).
  - Five distinct learning disciplines:
    - Mode A: BNS Sections & Statutory Headings (358 Sections)
    - Mode B: Legal Terms, Maxims & Definitions
    - Mode C: Constitutional Articles & Core Subjects
    - Mode D: Landmark Precedents & Rulings
    - Mode E: Mixed Judicial Knowledge
  - Five difficulty tiers: Beginner (4 pairs), Easy (6 pairs), Intermediate (8 pairs), Advanced (12 pairs), Expert (18 pairs).
  - Initial 3-second preview peek mode, transparent hint system (-35 pts deduction), combo matching, and educational match toasts with deep links to the BNS Bare Act.
- **Game 2: Section Sprint (`section-sprint.html`, `assets/games/js/section-sprint.js`):**
  - High-speed statutory recall simulator featuring a 3-second pre-game countdown (3, 2, 1, GO!).
  - Five recall game modes: Section Number → Title, Title → Number, Mixed Bidirectional, Chapter-wise Challenge, and Personalized Weak Section Practice.
  - Four timing challenges: 30s Blitz, 60s Standard Sprint, 120s Endurance, and Untimed Learning (25 questions).
  - Circular SVG progress stopwatch with real-time countdown ring.
  - Streak multiplier engine ($1\times, 1.5\times, 2\times, 2.5\times, 3\times$).
  - Full keyboard accessibility: **A, B, C, D** (or **1, 2, 3, 4**) for instant selection, and **Spacebar** to skip.
  - Automatic mistake cataloging to the Weak Knowledge Queue.
- **Shared Gaming Engine (`assets/games/`):**
  - Procedural Web Audio synthesizer (`game-audio.js`): zero external audio files, muted by default, persistent toggle, crisp card flips, correct chimes, incorrect buzzes, clock ticks, and victory fanfares.
  - Isolated persistence engine (`game-storage.js`) utilizing key `tanveer-arena-v1`.
  - Judicial achievements evaluator (`achievements.js`) with animated toast overlays.
  - Curated legal dataset (`legal-game-content.js`) with verified Latin maxims, constitutional articles, and landmark Indian case precedents.
  - Full suite of 8 original SVG game card illustrations in `assets/games/images/cards/`.
- **Navigation & Integration:**
  - Added "⚡ Brain Arena" navigation link across all 11 existing HTML pages.
  - Added direct "⚡ Legal Brain Arena" action button to the personal home dashboard hero.

---

## [2.0.0] — 2026-11-22
*Git Commit: `3a94255` — "V2.0 - BNS 358 Sections and Advanced Smart Search"*

### Added
- **Bharatiya Nyaya Sanhita (BNS) Section Library (`bns.html`, `assets/data/bns.js`):**
  - Complete digital index of all 358 sections across 20 statutory chapters of the Bharatiya Nyaya Sanhita, 2023.
  - Offline searchable section headings and legal topic keywords.
  - Direct reading links to the official India Code Act PDF and eCourts India reader.
  - Section 106 commencement advisory for subsection (2).
  - BNS section bookmarking stored in browser `localStorage` (`tanveer-bns-bookmarks-v1`).
  - Section-heading recall test generator with instant feedback.
- **Smart Legal Search (`search.html`, `assets/js/legal-search.js`):**
  - Unified search engine cross-referencing both BNS sections and the 1,800-question PYQ library.
  - Multi-token normalization pipeline (NFKD, lowercase, legal abbreviations, spelling variants).
  - Distinct presentation separating modern BNS section headings from historical PYQ results.

---

## [1.0.0] — 2026-11-21
*Git Commit: `8b65ab3` — "Initial commit - Tanveer Ashraf Judicial Preparation Portal"*

### Added
- Core static multi-page architecture with 9 HTML pages.
- 1,800 question slots across 6 examination years (2012–2023) in Paper I (GK) and Paper II (Law).
- Examination simulator, official scoring rules, negative marking (-1/3), results tracking, and progress backup.
- Personal advocate attire portrait of Tanveer Ashraf and monochrome portrait of Tauqeer Ashraf.
