# Update CHANGELOG.md with Phase 4 release notes
import os

cl_path = "CHANGELOG.md"
with open(cl_path, "r", encoding="utf-8") as f:
    text = f.read()

phase4_entry = """## [3.0.0] — Phase 4 — 2026-11-22
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

"""

marker = "## [3.0.0] — Phase 3 — 2026-11-22"
if marker in text:
    text = text.replace(marker, phase4_entry + marker)
    with open(cl_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("CHANGELOG.md updated with Phase 4 entry!")
else:
    print("Could not find Phase 3 marker in CHANGELOG.md")
