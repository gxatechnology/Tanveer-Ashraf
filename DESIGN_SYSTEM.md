# DESIGN_SYSTEM.md — Judicial Prep UI/UX Design System

## 1. Design Philosophy & Aesthetic Identity
The visual design of **Tanveer Ashraf — Judicial Prep** is meticulously calibrated to provide a distinguished, academic, and distraction-free preparation environment suited for the Uttar Pradesh Judicial Services (UP PCS-J).

### Core Principles
- **Judicial Dignity:** Uses deep navy, judicial teal, antique gold accents, and Georgia serifs reminiscent of legal law reports and court registries.
- **Academic Rigour:** Clean card-based question layouts with legible typesetting, distinct option buttons, and clear answer feedback.
- **Focus & Minimal Friction:** High contrast, zero unnecessary animations, non-distracting test simulation mode.
- **Uncompromised Identity:** Preserves the personal branding of candidate Tanveer Ashraf and developer Tauqeer Ashraf with custom visual framing (golden portrait halo, advocate portrait).

---

## 2. Color Palette & Design Tokens

All CSS variables are defined at the `:root` level in [assets/css/site.css](file:///c:/Users/tauqe/Documents/Tanveer_Ashraf_Judicial/assets/css/site.css).

### Primary Color Variables
| Variable / Token | Hex Value | Role / Usage |
| :--- | :--- | :--- |
| `--navy` | `#142c46` | Primary brand background, sidebar background, primary headers, active states. |
| `--navy2` | `#1b3857` | Dark secondary navy, gradient stops. |
| `--teal` | `#137d72` | Judicial Green / Deep Teal; primary action buttons, active links, progress bars. |
| `--paper` | `#f3f5f8` | Primary page canvas background (light cool grey / soft paper). |
| `--muted` | `#607387` | Secondary text, meta captions, helper descriptions, timestamps. |
| `--line` | `#dce3ea` | Card borders, dividers, subtle separators. |
| `--white` | `#ffffff` | Card surfaces, clean input backgrounds, modal surfaces. |
| `--ink` | `#1c2e40` | Primary reading text, question stems, option labels. |
| `--red` | `#a63b49` | Incorrect responses, warning notices, danger/reset buttons. |
| `--amber` | `#875711` | Marked-for-review questions, alert states. |
| `--shadow` | `0 6px 24px #142c460a` | Subtle ambient elevation shadow for cards. |

### Judicial Gold Accents
| Hex Code | Context / Usage |
| :--- | :--- |
| `#e7c88c` / `#dfbf80` | Antique Gold buttons (`.btn.gold`), portrait aura rings, highlight borders. |
| `#cdb17d` / `#d4b67e` | Top border accents on statistics cards (`.stat`) and year cards (`.yearcard`). |
| `#eee6d3` | Background for BNS section badge (`.bns-number`). |
| `#74582a` | Text color for BNS section numbers and law category badges. |
| `#b98a38` | Focus-visible accessibility outline for buttons, links, and inputs. |

### Evaluation State Colors
| State | Background | Border | Text Color |
| :--- | :--- | :--- | :--- |
| **Selected Option** | `#eef6ff` | `#518fc5` | `#1c2e40` |
| **Correct Answer** | `#e9f6f1` | `#7cbca6` | `#135e48` |
| **Wrong Answer** | `#fff1f1` | `#de9fa4` | `#952e3d` |
| **Answer Banner** | `#edf7f4` | Left: `3px solid #137d72` | `#135e48` |
| **Notice / Alert** | `#fff8ee` | Border: `#ecd8b1` | `#875711` |

---

## 3. Typography & Hierarchy

### Font Families
1. **Body & Interface:**
   `font: 15px/1.6 system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`
   Used across all standard body text, buttons, form inputs, options, and explanations.
2. **Judicial Serif / Numerals / Headings:**
   `Georgia, serif`
   Used for:
   - Dashboard big scores & stats (`.stat strong`, `.big-mark`)
   - Year numbers on year cards (`.yearcard .year`)
   - Law hero title and metrics (`.law-hero h1`, `.law-metrics b`)
   - BNS section badges (`.bns-number`)
   - Monogram emblem icon

### Typographic Scales
- **Display 1 (Home Hero):** `font-size: clamp(25px, 3vw, 39px); line-height: 1.2; letter-spacing: -0.8px`
- **Section Heading (`h2`):** `font-size: 23px; line-height: 1.3; font-weight: 700`
- **Card Subheading (`h3`):** `font-size: 17px; font-weight: 600`
- **Eyebrow:** `font-size: 11px; text-transform: uppercase; letter-spacing: 2px; font-weight: 700; color: var(--teal)`
- **Body Text:** `font-size: 15px; line-height: 1.6; color: var(--ink)`
- **Question Stem:** `font-size: 16px; font-weight: 650; line-height: 1.6; white-space: pre-wrap`
- **Meta / Captions:** `font-size: 12px / 13px; color: var(--muted)`

---

## 4. UI Components & Layout Systems

### Layout Framework
- **Application Container (`.app`):**
  Desktop uses a 2-column CSS Grid: `grid-template-columns: 245px minmax(0, 1fr); min-height: 100vh`.
- **Sidebar Navigation (`.side`):**
  Sticky container (`position: sticky; top: 0; height: 100vh; background: var(--navy); padding: 26px 19px`).
  Contains `.brand`, `.sidebar-label`, `.nav`, and candidate attribution `.profile`.
- **Main View Area (`.main`):**
  Contains `.top` bar, dynamic `.content` container (max-width `1250px`, centered), and `.site-footer`.

### Reusable UI Components
1. **Cards (`.card`):**
   `border: 1px solid var(--line); background: #fff; border-radius: 13px; padding: 19px; box-shadow: var(--shadow)`.
2. **Stat Cards (`.stat`):**
   Card variant with top accent border (`border-top: 3px solid #cdb17d`). Features massive numeral (`30px Georgia`) and muted label.
3. **Buttons (`.btn`):**
   Base: `border: 1px solid var(--line); border-radius: 8px; padding: 10px 15px; font-weight: 650`.
   - `.primary`: Background `var(--teal)`, white text.
   - `.dark`: Background `var(--navy)`, white text.
   - `.gold`: Background `#e7c88c`, dark text.
   - `.ghost`: Semi-transparent white `#ffffff0d` with border `#ffffff55`.
   - `.danger`: Red text `var(--red)`, border `#e7b9bd`.
   - `.mini`: Compact button (`padding: 6px 10px; font-size: 12px`).
4. **Question Card (`.qcard`):**
   - `.qmeta`: Meta header with year, paper, question number, and suggested topic tag (`.tag`).
   - `.qstem`: Full question prompt.
   - `.options`: Grid of 4 options (`.opt`) with bold lettering `(A)`, `(B)`, `(C)`, `(D)`.
   - `.answer`: Highlighted answer container with practice key.
5. **Exam Question Palette (`.palette`):**
   Numbered grid of buttons (1 to N) reflecting real-time attempt status:
   - Default: Unvisited / white.
   - `.done`: Answered (Judicial Green background).
   - `.flag`: Marked for review (Amber background).
   - `.now`: Current active question (Navy border/background).
   - `.void`: Non-scoreable review-only question (Muted grey).
6. **Candidate Hero Halo (`.portrait-ring`):**
   Concentric golden circles (`width: 260px; height: 260px; border: 1px solid #e6c78b55; border-radius: 50%`) with frosted backdrop-blur badge (`.portrait-label`).
7. **BNS Section Card (`.bns-card`):**
   Flex card displaying large section badge (`.bns-number`), chapter breadcrumb, statutory title, and direct reading action links.

---

## 5. Responsive Breakpoint Rules

| Breakpoint | Target Devices | Layout Adjustments |
| :--- | :--- | :--- |
| **> 1000px** | Desktops & Laptops | Standard 245px sidebar, 3-to-4 column stats grid, full portrait display. |
| **761px – 1000px** | Small Laptops / Tablets | Sidebar shrinks to 210px; Hero portrait shrinks to 180px halo; content padding 22px. |
| **<= 760px** | Tablets & Smartphones | **Major breakpoint:** `.app` becomes `display: block`. Sidebar `.side` becomes static top bar; `.sidebar-label` and `.profile` hide; `.nav` becomes a horizontally scrollable bar (`display: flex; overflow-x: auto; white-space: nowrap`). 2-column grids (`.people-grid`, `.syllabus-grid`) collapse to 1 column. |
| **<= 600px** | Phablets | Law hero padding narrows; BNS number basis shrinks to 60px; toolbar buttons compact to 11px. |
| **<= 390px** | Compact Smartphones | Home hero stacks tightly; h1 shrinks to 27px; top title adjusts to 13px. |
| **Print** | Print stylesheets | Hides `.site-footer` and `.hero-portrait`; expands layout cleanly for paper review. |

---

## 6. Accessibility & Interaction Guidelines
- **Focus Indicators:** Interactive elements (`.nav a`, `.btn`, `input`, `select`) specify `outline: 2px solid #b98a38; outline-offset: 2px` on `:focus-visible`.
- **Screen Reader Support:** Semantic `<main>`, `<aside>`, `<nav>`, `<article>`, `<fieldset>`, and `<legend>` landmarks; `aria-live="polite"` for dynamic search results; `aria-pressed` for bookmark toggles.
- **Form Controls:** Radio buttons in recall tests use native styling with `accent-color: var(--teal)`.

---

## 7. Legal Brain Arena Gaming Design System (V3.0)

### Extended Gaming Palette Tokens
Defined in [assets/games/css/arena.css](file:///c:/Users/tauqe/Documents/Tanveer_Ashraf_Judicial/assets/games/css/arena.css):
- `--arena-navy-dark`: `#0a1b2d` (Deep midnight arena background)
- `--arena-navy-mid`: `#142c46` (Mid-tone navy for card frames)
- `--arena-sapphire`: `#102847` (Vibrant sapphire accent)
- `--arena-gold-light`: `#fef0c7` (Highlight gold for XP numerals & badges)
- `--arena-gold`: `#dfbf80` (Primary antique gold borders and trims)
- `--arena-gold-dark`: `#9e7529` (Deep amber for difficulty meters)
- `--arena-teal`: `#137d72` (Judicial green for victory and live badges)
- `--arena-teal-light`: `#2fe0c8` (High-contrast cyan highlight)

### Specialized Gaming Components
1. **Arena Hero (`.arena-hero`):**
   Cinematic radial gradient (`#1c4468` -> `#10253d` -> `#0a1827`) featuring an ambient scales watermark, Level Progress Strip (`.arena-level-strip`), and persistent audio controls.
2. **Game Cards (`.game-card`):**
   Card layout with 155px SVG media banner, status badge (`.game-status-badge.live` in emerald vs `.soon` in muted slate), difficulty indicator, and launch actions.
3. **3D Memory Card Architecture (`.memory-card`):**
   Three-dimensional card flip using CSS `perspective: 1000px`, `transform-style: preserve-3d`, and `backface-visibility: hidden`. Card back features geometric judicial diamond patterns; card front features high-contrast category badges and readable statutory typography.
4. **Section Sprint Stopwatch (`.sprint-timer-widget`):**
   Circular SVG progress ring (`r="45"`) with smooth `stroke-dashoffset` countdown transitions, center digital second ticker, and streak multiplier badges (`1x` to `3x`).
5. **Pre-Game 3-Second Countdown (`.sprint-countdown-box`):**
   Large pulsing countdown numerals (3, 2, 1, GO!) with auditory ticks before activating user input.
6. **Achievement Toast (`.achievement-toast`):**
   Floating banner sliding up from bottom-right with judicial icon, title, description, and XP reward badge.
7. **Educational Match Toast (`.match-toast`):**
   Floating banner sliding in from top-right displaying statutory context and an instant "Explore in BNS ↗" link.
8. **Arena Completion Modals (`.arena-modal-card`):**
   Celebratory result dialogues presenting a 4-metric score grid, time taken, weak items review box, and immediate replay triggers.

---

## 8. Case Simulation & Courtroom Visual Design System (V3.0 Phase 2)

Defined in [assets/games/css/case-simulation.css](file:///c:/Users/tauqe/Documents/Tanveer_Ashraf_Judicial/assets/games/css/case-simulation.css):

### Specialized Simulation Environments
1. **Case Dossier Selection (`.dossier-card`):**
   Archival document folder aesthetic with color-coded difficulty stripes:
   - Beginner: Deep Forest `#0f3d38`
   - Intermediate: Navy Slate `#163654`
   - Advanced: Judicial Mahogany `#3c2415`
   Features case reference number, statutory tags, syllabus categories, and prior high-score badges.
2. **Investigation Stage Stepper (`.sim-stepper`):**
   Responsive linear progress ribbon displaying circular numbered nodes with active state glowing gold aura (`box-shadow: 0 0 0 3px rgba(223, 191, 128, 0.35)`) and completed teal checks (`#137d72`).
3. **Character Manifest & Dialogue Viewport (`.dialogue-viewport`):**
   - 8 recurring characters with distinct SVG portraits, personality tones, and pitch/speed calibrations.
   - Circular portraits (110px desktop, 48px mobile/podiums) with theme color border halos.
   - Speech bubble with directional pointer caret, typewriter letter-by-letter animation, blinking cursor, and instant skip trigger.
   - Interactive cross-examination inquiry buttons with "✓ Asked" tracking.
   - Official Examination Transcript modal (`.dialogue-log-modal`) logging all statements with timestamps.
4. **Interactive Corkboard Evidence Board (`.corkboard-wrap`):**
   - Realistic cork texture gradient (`#3e2723` radial to `#2e1c14`) encased in a 10px wooden frame (`#8d6e63`).
   - Discovered clue nodes (`.cork-node`) with red pushpin icons (`#dc2626`), card drop shadows, and selection highlights.
   - Statutory element targets (`.cork-target`) with dashed drop-ready borders and linked clue tags with remove buttons.
5. **Virtual Courtroom Bench (`.courtroom-banner`, `.counsel-podium`):**
   - Elevated judicial bench aesthetic with cause list identifiers.
   - Dual counsel podiums: Public Prosecutor / Plaintiff Counsel in midnight navy (`#142c46`), Defence Counsel in slate sapphire (`#1e3a5f`).
   - Evidentiary exhibit inspection sheets (`.exhibit-sheet`) with crimson angled seal stamp ("OFFICIAL COURT RECORD").
6. **Structured Reasoned Order Builder (`.order-builder-wrap`):**
   Judicial judgment drafting workspace divided into three mandatory structural sections:
   - Section I: Statement of Material Facts & Pleadings
   - Section II: Discussion of Substantive Law & Precedents (Ratio Decidendi)
   - Section III: Formal Operative Order & Direction
7. **100-Point Judicial Rubric & Mentor Critique (`.report-card-wrap`):**
   - Aggregate score badge (`score-big`) with max 100 benchmark.
   - Five-metric rubric breakdown grid with animated horizontal progress fill bars.
   - Mentor critique box featuring judicial commentary from Det. Arjun Rathore or Justice Vikram Sahay.
   - Authoritative statutory foundations and Supreme Court citation boxes.
8. **The Lexicon Chamber UI (`.lexicon-container`, `.crossword-grid`):**
   - High-contrast responsive crossword grid (8x8, 10x10, 12x12) with reading-order clue numbering badges.
   - Bidirectional cell selection (Across / Down) with gold cursor highlight (`#dfbf80`) and active word row highlighting (`#fff8ee`).
   - Active Clue Ribbon above grid displaying current clue number, orientation, and full statutory prompt.
   - Dual clue scroll panes with tab switching (Across & Down) and line-through strikeout on solved words.
   - Virtual on-screen touch keyboard (`.crossword-keyboard`) with directional toggle (`DIR ⇄`) and backspace.
   - Compact educational definition dock revealing authentic Indian statutory definitions upon word solution.
   - Lexicon Chamber Master Certificate completion view with Dr. Devendra Bose's academic evaluation.
9. **The Code Breaker UI (`.codebreaker-arena`, `.letter-tile`):**
   - Combination Lock HUD (`.combination-lock-hud`) with mechanical dials for Streak, Score, Multiplier ($1.0\times$ to $3.0\times$), and Timer.
   - Tactile metallic letter tiles (`.letter-tile`) with brass bevels and gold foil lettering (`linear-gradient(135deg, #fff2d1 0%, #dfbf80 65%, #a8792c 100%)`).
   - Target Answer Slots Rack (`.answer-slots-rack`) with dashed target slots and automatic space separators for multi-word maxims.
   - Scrambled Tile Tray with actions for Shuffle, Undo, Clear, Hint (-15 pts), and Check Cipher.
   - Seamless dual input: HTML5 Drag-and-Drop, touch tap-to-place, and physical keyboard typing (A-Z, Backspace, Enter, Esc).
   - Illuminated Manuscript Vault with 5 thematic judicial codices revealing ancient parchment extracts upon decoding.
10. **The Chamber of Truth UI (`.myth-arena`, `.scales-wrap`):**
   - Animated Scales of Justice (`.scales-beam`, `.scale-pan-left`, `.scale-pan-right`): Rotates dynamically according to proposition veracity (`rotate(-12deg)` for True, `rotate(12deg)` for False, `rotate(0deg)` for Nuanced/Depends).
   - Statutory proposition parchment card with verified citation tags, statutory references, and difficulty level.
   - Three-way adjudication controls: `TRUE / CORRECT LAW`, `FALSE / COMMON MYTH`, and `DEPENDS / QUALIFIED RULE`.
   - Three-tier learning-confidence calibration toggles (`Low`, `Medium`, `High`) replacing point penalties with cognitive self-calibration tracking.
11. **Road to Judiciary UI (`.journey-map-container`, `.campaign-node`):**
   - High-resolution SVG-based sequential campaign map connecting 9 chapters and 36 missions across judicial domains.
   - Chapter completion progress nodes, mentor dialogue modals, and daily recommended study time widgets.
   - Educational Completion Certificate modal with candidate pledge and prominent educational disclaimer.
12. **Phase 5 Advanced Analytics & Print System:**
   - Analytics Separation: Clean separation between official examination simulation history (Paper I GK & Paper II Law) and cognitive gaming metrics (XP, Streaks, Accuracies).
   - Responsive SVG & CSS Charts: Visual score trends and category accuracy breakdown bars.
   - Unified Smart Revision Centre: Filter tabs (`All Items`, `Bookmarked PYQs`, `Arena Errors & Misconceptions`) and "Mark Resolved" interactive action buttons.
   - Print Optimization (`@media print`): Hides all interactive navigations, buttons, headers, and displays clean, academic serif typography alongside formal educational disclaimers.

