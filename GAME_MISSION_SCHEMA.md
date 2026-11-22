# GAME_MISSION_SCHEMA.md — Road to Judiciary Campaign & Mission Integration Architecture

## 1. Executive Overview & Architecture
The **Road to Judiciary** (`Game 8`, `judiciary-journey.html`) provides a structured educational learning journey spanning all eight interactive games in the **Legal Brain Arena** and the historical UP PCS-J Test Centre.

The campaign connects:
1. `Game 1`: Legal Memory Match (`memory-match.html`)
2. `Game 2`: Section Sprint (`section-sprint.html`)
3. `Game 3`: Legal Detective: The Case Files (`legal-detective.html`)
4. `Game 4`: Be the Judge: The Courtroom (`courtroom.html`)
5. `Game 5`: Legal Crossword: The Lexicon Chamber (`crossword.html`)
6. `Game 6`: Legal Word Scramble: The Code Breaker (`word-scramble.html`)
7. `Game 7`: Legal Myth Buster: The Chamber of Truth (`myth-buster.html`)
8. `PYQ Test Centre`: UP PCS-J Previous Year Examination Bank (`tests.html`)

---

## 2. Chapter Schema (`assets/games/data/journey-chapters.js`)
The campaign comprises nine progressive chapters across judicial disciplines:

```javascript
{
  id: "ch-01",                     // Unique string identifier ('ch-01' to 'ch-09')
  number: 1,                       // Sequential integer (1 to 9)
  title: "The Law Academy",        // Chapter title
  tagline: "Foundational Maxims",  // Judicial subtitle
  lore: "...",                     // Immersive pedagogical narrative
  discipline: "Legal Vocabulary",  // Core statutory discipline
  mentorId: "kavita",              // Referenced character mentor ID
  mentorName: "Prof. Kavita Sharma",
  mentorRole: "Vocabulary Mentor",
  mentorAvatar: "path/to/avatar.svg",
  unlockedCriteria: "Initial Chapter", // Human-readable unlock requirement
  totalMissions: 4,                // Number of missions contained
  coords: { x: 12, y: 78 },        // Percentage position on campaign map (0-100)
  badgeIcon: "🏛️",                 // Decorative SVG or unicode badge
  minLevel: 1                      // Recommended candidate level
}
```

### Chapter Progression Rules:
- **Chapter 1** (`ch-01`) is always unlocked by default.
- Subsequent chapters (`ch-02` through `ch-09`) unlock when the candidate completes at least **3 of the 4 missions** in the immediately preceding chapter.

---

## 3. Mission Schema (`assets/games/data/journey-missions.js`)
Each mission represents a concrete task executed in an authentic game mode:

```javascript
{
  id: "m-acad-01",                 // Unique mission identifier
  chapterId: "ch-01",              // Parent chapter ID
  number: 1,                       // Global mission number (1 to 36)
  title: "First Steps in the Lexicon",
  game: "crossword",               // Target game key
  gameUrl: "crossword.html?missionId=m-acad-01&puzzle=puzzle-01",
  description: "Solve your first 9x9 statutory crossword puzzle.",
  criteria: {
    minScore: 50,                  // Minimum score required to pass
    minAccuracy: 60,               // Minimum percentage accuracy (0-100)
    targetTime: 120                // Optional maximum allowed time in seconds
  },
  rewardXP: 120,                   // Learning XP credited on completion
  badge: "Lexicon Initiate",       // Milestone badge title
  mentorBriefing: "..."            // Introductory mentor dialogue
}
```

---

## 4. Mission Execution & URL Parameter Bindings
When a mission is launched from the campaign map, the user is navigated to the target game with search parameters:

| Game | Launch URL Template | Handled Parameters |
| :--- | :--- | :--- |
| **Crossword** | `crossword.html?missionId={id}&puzzle={puzzleId}` | `missionId`, `puzzle` |
| **Word Scramble** | `word-scramble.html?missionId={id}&mode={mode}&count={n}` | `missionId`, `mode`, `count` |
| **Memory Match** | `memory-match.html?missionId={id}&mode={mode}&pairs={n}` | `missionId`, `mode`, `pairs` |
| **Section Sprint** | `section-sprint.html?missionId={id}&mode={mode}&time={s}` | `missionId`, `mode`, `time` |
| **Legal Detective** | `legal-detective.html?missionId={id}&caseId={caseId}` | `missionId`, `caseId` (or `case`) |
| **Be the Judge** | `courtroom.html?missionId={id}&caseId={caseId}` | `missionId`, `caseId` (or `case`) |
| **Myth Buster** | `myth-buster.html?missionId={id}&mode={mode}&subject={subj}&count={n}` | `missionId`, `mode`, `subject`, `count` |
| **PYQ Test Centre** | `tests.html?missionId={id}&paper={law/gk}&year={yr}&count={n}` | `missionId`, `paper`, `year`, `count` |
| **Final Capstone** | `judiciary-journey.html?missionId=m-seat-04&action=educational_achievement` | `missionId`, `action` |

---

## 5. Automated Completion Hook
Every game's session completion logic connects to `window.GameStorage.recordMissionCompletion`:

```javascript
// Universal Mission Completion Listener
const urlParams = new URLSearchParams(window.location.search);
const missionId = result.missionId || urlParams.get('missionId');

if (missionId) {
  window.GameStorage.recordMissionCompletion(missionId, result.score, result.accuracy);
}
```

### Storage Mutation in `tanveer-arena-v1`:
```json
{
  "journey": {
    "completedMissions": {
      "m-acad-01": {
        "completedAt": "2026-11-22",
        "score": 85,
        "accuracy": 80
      }
    },
    "unlockedChapters": ["ch-01", "ch-02"],
    "activeMissionId": "m-acad-02",
    "lastUpdated": "2026-11-22T11:45:00.000Z"
  }
}
```

---

## 6. Personal Learning Progress & Mastery Calculation (`mastery-engine.js`)
Candidate competence across legal disciplines is calculated objectively based on verified completion and performance.

### Data Sufficiency Requirement:
To prevent misleading readiness predictions, the engine requires a minimum of **3 recorded activities** before rendering quantitative competence percentages. If $< 3$ activities are completed, `hasSufficientData` is `false`, displaying a prompt to engage with study materials first.

### Educational Mastery Tiers:
Simulated official judicial ranks have been eliminated. Progress is categorized into objective educational mastery tiers:
- **Comprehensive Mastery (Tier 5):** Overall Learning Progress $\ge 90\%$, Completed Missions $\ge 32$
- **Proficient Scholar (Tier 4):** Overall Learning Progress $\ge 75\%$, Completed Missions $\ge 24$
- **Statutory Practitioner (Tier 3):** Overall Learning Progress $\ge 60\%$, Completed Missions $\ge 16$
- **Curriculum Explorer (Tier 2):** Overall Learning Progress $\ge 40\%$, Completed Missions $\ge 8$
- **Foundational Aspirant (Tier 1):** Default initial tier (0–7 missions completed)

---

## 7. Deterministic Daily Learning Plan (`learning-plan.js`)
Recommendations are dynamically structured based on the candidate's selected time budget:
- **15 Minutes:** Rapid section sprint (5m), myth buster diagnostic (5m), word scramble (5m).
- **30 Minutes:** Campaign mission (10m), precedent challenge (10m), crossword puzzle (10m).
- **45 Minutes:** Paper II PYQ mock (15m), courtroom simulation (15m), transition challenge (15m).
- **60 Minutes:** Full mock test (20m), criminal investigation (15m), grand truth trial (15m), campaign mission (10m).

---

## 8. Educational Milestone Recognition
Upon completing all 36 missions and taking the candidate pledge at Mission 36 (`m-seat-04`), the portal generates:
- **Award:** *ROAD TO JUDICIARY — LEARNING JOURNEY COMPLETED: Personal Educational Achievement*
- **Candidate Pledge:** Affirmation of constitutional integrity, fairness, and tireless dedication to the rule of law.
- **Mandatory Educational Disclaimer:** Clearly specifies that this certificate represents personal study completion and is not an official appointment or endorsement from the High Court, UPPSC, or State Government.
