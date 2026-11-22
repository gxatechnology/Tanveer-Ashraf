/**
 * LEGAL CROSSWORD: THE LEXICON CHAMBER (V3.0 Phase 3)
 * Full interactive UI controller for crossword.html
 * Integrates Prof. Kavita Sharma & Dr. Devendra Bose, interactive grid,
 * physical and on-screen keyboard, smart hints, and library completion screen.
 */
(function() {
  'use strict';

  class CrosswordUIController {
    constructor() {
      this.puzzles = window.ARENA_CROSSWORDS || [];
      this.currentPuzzle = null;
      this.engine = null;
      this.assistedMode = false;
      this.activeTab = 'all';
      
      this.init();
    }

    init() {
      // Check if resuming active puzzle
      const saved = window.GameStorage ? window.GameStorage.getCrosswordActive() : null;
      if (saved && saved.puzzleId) {
        const found = this.puzzles.find(p => p.id === saved.puzzleId);
        if (found) {
          this.loadPuzzle(found, saved);
          return;
        }
      }

      this.renderDashboard();
    }

    renderDashboard() {
      const container = document.getElementById('crosswordApp');
      if (!container) return;

      const state = window.GameStorage ? window.GameStorage.getArenaState() : {};
      const completedPuzzles = (state.crossword && state.crossword.completedPuzzles) || {};
      const completedCount = Object.keys(completedPuzzles).length;
      const vocabMastered = completedCount * 5; // average 5 words per puzzle
      
      const today = new Date().toISOString().slice(0, 10);
      const dailyPuzzle = window.VocabularyEngine ? window.VocabularyEngine.getDailyCrossword(this.puzzles, today) : this.puzzles[0];

      container.innerHTML = `
        <div class="puzzle-env-hero">
          <img src="assets/games/images/environments/lexicon.svg" class="puzzle-env-bg" alt="Lexicon Chamber Background">
          <div class="puzzle-hero-content">
            <span class="badge" style="background:#dfbf8022;color:#dfbf80;border:1px solid #dfbf80;margin-bottom:8px;">GAME 5 · LEXICON CHAMBER</span>
            <h1>Legal Crossword</h1>
            <div class="puzzle-tagline">"Every Word Unlocks Knowledge."</div>
            <p style="max-width:680px;color:#dce3ea;font-size:0.95rem;line-height:1.5;">
              Welcome to the Grand Lexicon Chamber. Solve real intersecting statutory crossword puzzles, master Latin maxims, test procedural definitions, and reinforce your memory under the mentorship of Prof. Kavita Sharma and Dr. Devendra Bose.
            </p>
            <div class="puzzle-stats-strip">
              <div class="puzzle-stat-pill">📚 Solved Puzzles: <strong>${completedCount} / ${this.puzzles.length}</strong></div>
              <div class="puzzle-stat-pill">🔠 Vocabulary Mastered: <strong>${vocabMastered}</strong></div>
              <div class="puzzle-stat-pill">⚡ Learning Level: <strong>${state.level || 1}</strong></div>
            </div>
          </div>
        </div>

        ${dailyPuzzle ? `
          <div class="card" style="border:2px solid #dfbf80;background:#fffdf7;margin-bottom:24px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;padding:18px 24px;gap:16px;">
            <div>
              <span class="badge" style="background:#a63b49;color:#fff;">🌟 DAILY CROSSWORD CHALLENGE</span>
              <h3 style="font-family:Georgia,serif;margin:6px 0 2px 0;color:#142c46;">${dailyPuzzle.title}</h3>
              <p style="margin:0;color:#607387;font-size:0.9rem;">${dailyPuzzle.collection} · ${dailyPuzzle.difficulty.toUpperCase()} · ${dailyPuzzle.words.length} Clues · +100 Bonus XP</p>
            </div>
            <button class="btn gold" id="btnLaunchDaily" style="font-weight:bold;padding:10px 22px;">Solve Daily Crossword ➔</button>
          </div>
        ` : ''}

        <div style="display:flex;gap:8px;overflow-x:auto;padding-bottom:12px;margin-bottom:20px;">
          <button class="btn ${this.activeTab === 'all' ? 'primary' : 'secondary'} tab-filter" data-tab="all">All Puzzles (${this.puzzles.length})</button>
          <button class="btn ${this.activeTab === 'beginner' ? 'primary' : 'secondary'} tab-filter" data-tab="beginner">Beginner (10)</button>
          <button class="btn ${this.activeTab === 'intermediate' ? 'primary' : 'secondary'} tab-filter" data-tab="intermediate">Intermediate (10)</button>
          <button class="btn ${this.activeTab === 'advanced' ? 'primary' : 'secondary'} tab-filter" data-tab="advanced">Advanced (10)</button>
        </div>

        <div style="display:grid;grid-template-columns:repeat(auto-fill, minmax(280px, 1fr));gap:16px;" id="puzzlesGrid">
          ${this.renderPuzzleCards()}
        </div>
      `;

      // Event listeners
      container.querySelectorAll('.tab-filter').forEach(btn => {
        btn.addEventListener('click', (e) => {
          this.activeTab = e.currentTarget.getAttribute('data-tab');
          this.renderDashboard();
        });
      });

      const btnDaily = document.getElementById('btnLaunchDaily');
      if (btnDaily && dailyPuzzle) {
        btnDaily.addEventListener('click', () => {
          this.loadPuzzle(dailyPuzzle);
        });
      }

      container.querySelectorAll('.btn-play-puzzle').forEach(btn => {
        btn.addEventListener('click', (e) => {
          const pid = e.currentTarget.getAttribute('data-id');
          const p = this.puzzles.find(x => x.id === pid);
          if (p) this.loadPuzzle(p);
        });
      });
    }

    renderPuzzleCards() {
      const state = window.GameStorage ? window.GameStorage.getArenaState() : {};
      const completed = (state.crossword && state.crossword.completedPuzzles) || {};

      let filtered = this.puzzles;
      if (this.activeTab !== 'all') {
        filtered = this.puzzles.filter(p => p.difficulty.toLowerCase() === this.activeTab);
      }

      return filtered.map(p => {
        const isDone = !!completed[p.id];
        const bestScore = (state.personalBests && state.personalBests.crossword && state.personalBests.crossword[p.id]) || 0;

        return `
          <div class="card" style="display:flex;flex-direction:column;justify-content:space-between;border-top:3px solid ${p.difficulty === 'beginner' ? '#137d72' : p.difficulty === 'intermediate' ? '#dfbf80' : '#a63b49'};">
            <div>
              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                <span class="badge" style="font-size:10px;text-transform:uppercase;">${p.difficulty}</span>
                <span style="font-size:11px;color:#607387;">${p.gridSize.rows}×${p.gridSize.cols}</span>
              </div>
              <h4 style="font-family:Georgia,serif;margin:0 0 6px 0;color:#142c46;">${p.title}</h4>
              <p style="font-size:0.85rem;color:#607387;margin:0 0 10px 0;">${p.collection}</p>
              <div style="font-size:0.8rem;color:#1c2e40;margin-bottom:12px;">
                <span>📝 ${p.words.length} intersecting words</span>
                ${isDone ? `<span style="color:#137d72;font-weight:bold;margin-left:8px;">✓ Solved (${bestScore} pts)</span>` : ''}
              </div>
            </div>
            <button class="btn ${isDone ? 'secondary' : 'gold'} btn-play-puzzle" data-id="${p.id}" style="width:100%;font-weight:bold;">
              ${isDone ? 'Replay Puzzle ➔' : 'Solve Crossword ➔'}
            </button>
          </div>
        `;
      }).join('');
    }

    loadPuzzle(puzzle, savedState = null) {
      this.currentPuzzle = puzzle;
      this.engine = new CrosswordEngine(puzzle);

      // Restore saved letters if resuming
      if (savedState && Array.isArray(savedState.userEntries)) {
        savedState.userEntries.forEach(entry => {
          if (this.engine.grid[entry.r] && this.engine.grid[entry.r][entry.c]) {
            this.engine.grid[entry.r][entry.c].userChar = entry.char;
            if (entry.isRevealed) {
              this.engine.grid[entry.r][entry.c].isRevealed = true;
            }
          }
        });
      }

      this.renderPlayView();
      if (window.GameAudio) window.GameAudio.playPaper();
    }

    renderPlayView() {
      const container = document.getElementById('crosswordApp');
      if (!container || !this.currentPuzzle || !this.engine) return;

      container.innerHTML = `
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;flex-wrap:wrap;gap:12px;">
          <div>
            <button class="btn secondary" id="btnBackToDashboard" style="font-size:0.85rem;">← Puzzle Archives</button>
            <span style="font-family:Georgia,serif;font-weight:bold;font-size:1.2rem;margin-left:12px;color:#142c46;">${this.currentPuzzle.title}</span>
            <span class="badge" style="margin-left:8px;font-size:11px;">${this.currentPuzzle.collection}</span>
          </div>
          <div style="display:flex;gap:8px;align-items:center;">
            <button class="btn secondary" id="btnToggleAssisted" style="font-size:0.8rem;">
              ${this.assistedMode ? '🛡 Assisted Mode (ON)' : '🛡 Assisted Mode (OFF)'}
            </button>
            <button class="btn secondary" id="btnSoundToggle" style="font-size:0.8rem;">
              ${window.GameAudio && !window.GameAudio.isMuted() ? '🔊 Sound: ON' : '🔇 Sound: OFF'}
            </button>
          </div>
        </div>

        <!-- Character Mentor Speech Bubble -->
        <div style="display:flex;align-items:center;gap:16px;background:#ffffff;border:1px solid #dce3ea;border-left:4px solid #176d63;border-radius:10px;padding:12px 18px;margin-bottom:16px;box-shadow:0 3px 12px rgba(20,44,70,0.04);">
          <img src="assets/games/images/characters/crossword/kavita.svg" style="width:48px;height:48px;border-radius:50%;border:2px solid #dfbf80;" alt="Prof. Kavita Sharma">
          <div style="font-size:0.9rem;color:#1c2e40;flex:1;">
            <strong style="color:#176d63;font-family:Georgia,serif;">Prof. Kavita Sharma:</strong>
            <span id="mentorAdvice">"Read each statutory clue with precision. Click any cell to switch direction between Across and Down. Let every letter guide your recall."</span>
          </div>
        </div>

        <!-- Active Clue Ribbon -->
        <div class="crossword-active-clue-bar" id="activeClueBar">
          <span class="clue-badge" id="clueBadge">1 ACROSS</span>
          <div class="clue-text-main" id="clueTextMain">Select a cell to view its clue...</div>
        </div>

        <!-- Two Column Workspace: Board + Clues -->
        <div class="lexicon-container">
          <!-- Left: Crossword Board -->
          <div class="crossword-board-panel">
            <div class="crossword-grid-wrapper">
              <div class="crossword-grid" id="crosswordGrid" style="grid-template-columns: repeat(${this.engine.cols}, 1fr);">
                <!-- Dynamic cells inserted by JS -->
              </div>
            </div>

            <!-- Toolbar Actions -->
            <div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:16px;justify-content:center;">
              <button class="btn secondary" id="btnCheckLetter" style="font-size:0.8rem;">Check Letter</button>
              <button class="btn secondary" id="btnCheckWord" style="font-size:0.8rem;">Check Word</button>
              <button class="btn secondary" id="btnCheckPuzzle" style="font-size:0.8rem;">Verify All</button>
              <button class="btn secondary" id="btnRevealLetter" style="font-size:0.8rem;color:#7a2a35;" title="-15 Points Penalty">💡 Reveal Letter (-15)</button>
              <button class="btn secondary" id="btnRevealWord" style="font-size:0.8rem;color:#7a2a35;" title="-50 Points Penalty">📖 Reveal Word (-50)</button>
            </div>

            <!-- On-Screen Mobile Keyboard -->
            <div class="crossword-keyboard" id="crosswordKeyboard">
              <div class="keyboard-row">
                ${['Q','W','E','R','T','Y','U','I','O','P'].map(k => `<button class="key-btn" data-key="${k}">${k}</button>`).join('')}
              </div>
              <div class="keyboard-row">
                ${['A','S','D','F','G','H','J','K','L'].map(k => `<button class="key-btn" data-key="${k}">${k}</button>`).join('')}
              </div>
              <div class="keyboard-row">
                <button class="key-btn action-key" id="kbtnToggleDir">DIR ⇄</button>
                ${['Z','X','C','V','B','N','M'].map(k => `<button class="key-btn" data-key="${k}">${k}</button>`).join('')}
                <button class="key-btn action-key" id="kbtnBackspace">⌫</button>
              </div>
            </div>
          </div>

          <!-- Right: Across & Down Clue Panels -->
          <div class="crossword-clues-container">
            <div class="clues-header-tabs">
              <button class="clue-tab-btn active" id="tabAcross" data-dir="across">Across Clues</button>
              <button class="clue-tab-btn" id="tabDown" data-dir="down">Down Clues</button>
            </div>
            <div class="clues-scroll-pane" id="cluesList">
              <!-- Clues injected here -->
            </div>
          </div>
        </div>

        <!-- Educational Definition Dock for Solved Words -->
        <div class="crossword-educational-dock" id="educationalDock" style="display:none;">
          <div class="educational-dock-title" id="dockTerm">TERM</div>
          <div style="font-size:0.9rem;color:#1c2e40;margin-bottom:6px;" id="dockDefn">Definition</div>
          <div style="font-size:0.85rem;color:#607387;" id="dockAuth">Authority: ...</div>
        </div>
      `;

      this.bindPlayEvents();
      this.updateBoardDisplay();
    }

    bindPlayEvents() {
      const container = document.getElementById('crosswordApp');
      if (!container) return;

      // Back to dashboard
      const btnBack = document.getElementById('btnBackToDashboard');
      if (btnBack) {
        btnBack.addEventListener('click', () => {
          this.persistActiveProgress();
          this.renderDashboard();
        });
      }

      // Sound toggle
      const btnSound = document.getElementById('btnSoundToggle');
      if (btnSound) {
        btnSound.addEventListener('click', () => {
          if (window.GameAudio) {
            const enabled = window.GameAudio.toggleMute();
            btnSound.textContent = enabled ? '🔊 Sound: ON' : '🔇 Sound: OFF';
          }
        });
      }

      // Assisted Mode Toggle
      const btnAssisted = document.getElementById('btnToggleAssisted');
      if (btnAssisted) {
        btnAssisted.addEventListener('click', () => {
          this.assistedMode = !this.assistedMode;
          btnAssisted.textContent = this.assistedMode ? '🛡 Assisted Mode (ON)' : '🛡 Assisted Mode (OFF)';
        });
      }

      // Toolbar Buttons
      document.getElementById('btnCheckLetter').addEventListener('click', () => this.handleCheckLetter());
      document.getElementById('btnCheckWord').addEventListener('click', () => this.handleCheckWord());
      document.getElementById('btnCheckPuzzle').addEventListener('click', () => this.handleCheckPuzzle());
      document.getElementById('btnRevealLetter').addEventListener('click', () => this.handleRevealLetter());
      document.getElementById('btnRevealWord').addEventListener('click', () => this.handleRevealWord());

      // Clue Tabs
      document.getElementById('tabAcross').addEventListener('click', (e) => {
        document.getElementById('tabAcross').classList.add('active');
        document.getElementById('tabDown').classList.remove('active');
        this.renderCluesPane('across');
      });
      document.getElementById('tabDown').addEventListener('click', (e) => {
        document.getElementById('tabDown').classList.add('active');
        document.getElementById('tabAcross').classList.remove('active');
        this.renderCluesPane('down');
      });

      // On-Screen Keyboard
      container.querySelectorAll('.key-btn[data-key]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          const char = e.currentTarget.getAttribute('data-key');
          this.handleKeyInput(char);
        });
      });

      const btnDir = document.getElementById('kbtnToggleDir');
      if (btnDir) {
        btnDir.addEventListener('click', () => {
          this.engine.toggleDirection();
          this.updateBoardDisplay();
          if (window.GameAudio) window.GameAudio.playCrosswordTick();
        });
      }

      const btnBk = document.getElementById('kbtnBackspace');
      if (btnBk) {
        btnBk.addEventListener('click', () => {
          this.engine.backspace();
          this.updateBoardDisplay();
        });
      }

      // Physical Keyboard Listener
      this.keyHandler = (e) => {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

        if (e.key === 'ArrowRight') {
          e.preventDefault();
          this.engine.moveCursor(0, 1);
          this.updateBoardDisplay();
        } else if (e.key === 'ArrowLeft') {
          e.preventDefault();
          this.engine.moveCursor(0, -1);
          this.updateBoardDisplay();
        } else if (e.key === 'ArrowUp') {
          e.preventDefault();
          this.engine.moveCursor(-1, 0);
          this.updateBoardDisplay();
        } else if (e.key === 'ArrowDown') {
          e.preventDefault();
          this.engine.moveCursor(1, 0);
          this.updateBoardDisplay();
        } else if (e.key === 'Backspace' || e.key === 'Delete') {
          e.preventDefault();
          this.engine.backspace();
          this.updateBoardDisplay();
        } else if (e.key === 'Tab' || e.key === ' ') {
          e.preventDefault();
          this.engine.toggleDirection();
          this.updateBoardDisplay();
        } else if (/^[a-zA-Z]$/.test(e.key)) {
          e.preventDefault();
          this.handleKeyInput(e.key);
        }
      };

      window.removeEventListener('keydown', this.keyHandler);
      window.addEventListener('keydown', this.keyHandler);
    }

    handleKeyInput(char) {
      if (!this.engine) return;
      this.engine.enterLetter(char);
      if (window.GameAudio) window.GameAudio.playCrosswordTick();
      this.updateBoardDisplay();
      this.persistActiveProgress();

      // Check for puzzle completion
      if (this.engine.isPuzzleSolved()) {
        this.handlePuzzleCompleted();
      }
    }

    handleCheckLetter() {
      const cell = this.engine.getActiveCell();
      if (!cell || cell.isBlocked || cell.userChar === '') return;
      if (cell.userChar === cell.solution) {
        cell.isCorrect = true;
        cell.isError = false;
        if (window.GameAudio) window.GameAudio.playCorrect();
      } else {
        cell.isError = true;
        cell.isCorrect = false;
        if (window.GameAudio) window.GameAudio.playWrong();
      }
      this.updateBoardDisplay();
    }

    handleCheckWord() {
      if (!this.engine.activeWord) return;
      const cells = this.engine.getWordCells(this.engine.activeWord);
      let allCorrect = true;
      cells.forEach(c => {
        if (c.userChar === c.solution) {
          c.isCorrect = true;
          c.isError = false;
        } else {
          c.isError = true;
          c.isCorrect = false;
          allCorrect = false;
        }
      });
      if (allCorrect) {
        if (window.GameAudio) window.GameAudio.playWordSolve();
        this.showEducationalDock(this.engine.activeWord);
      } else {
        if (window.GameAudio) window.GameAudio.playWrong();
      }
      this.updateBoardDisplay();
    }

    handleCheckPuzzle() {
      const res = this.engine.checkPuzzle();
      if (res.errors === 0 && this.engine.isPuzzleSolved()) {
        this.handlePuzzleCompleted();
      } else if (res.errors > 0) {
        if (window.GameAudio) window.GameAudio.playWrong();
      }
      this.updateBoardDisplay();
    }

    handleRevealLetter() {
      if (confirm('Reveal this letter? (Incur 15 points penalty)')) {
        const char = this.engine.revealLetter();
        if (char && window.GameAudio) window.GameAudio.playClue();
        this.updateBoardDisplay();
        this.persistActiveProgress();
        if (this.engine.isPuzzleSolved()) this.handlePuzzleCompleted();
      }
    }

    handleRevealWord() {
      if (confirm('Reveal entire word? (Incur 50 points penalty)')) {
        const word = this.engine.revealWord();
        if (word && window.GameAudio) window.GameAudio.playClue();
        this.updateBoardDisplay();
        this.persistActiveProgress();
        if (this.engine.isPuzzleSolved()) this.handlePuzzleCompleted();
      }
    }

    showEducationalDock(wordObj) {
      const dock = document.getElementById('educationalDock');
      const term = document.getElementById('dockTerm');
      const defn = document.getElementById('dockDefn');
      const auth = document.getElementById('dockAuth');
      if (!dock || !term || !defn || !auth) return;

      term.textContent = `✓ ${wordObj.word}`;
      defn.textContent = wordObj.definition || wordObj.clue;
      auth.textContent = `Authority: ${wordObj.authority || 'Verified Statutory Law'}`;
      dock.style.display = 'block';
    }

    updateBoardDisplay() {
      const gridEl = document.getElementById('crosswordGrid');
      if (!gridEl || !this.engine) return;

      gridEl.innerHTML = '';

      const activeWordCells = this.engine.activeWord ? this.engine.getWordCells(this.engine.activeWord) : [];

      for (let r = 0; r < this.engine.rows; r++) {
        for (let c = 0; c < this.engine.cols; c++) {
          const cell = this.engine.grid[r][c];
          const div = document.createElement('div');
          div.className = 'crossword-cell';

          if (cell.isBlocked) {
            div.classList.add('blocked');
          } else {
            if (cell.clueNum) {
              const numSpan = document.createElement('span');
              numSpan.className = 'cell-num';
              numSpan.textContent = cell.clueNum;
              div.appendChild(numSpan);
            }

            if (cell.userChar) {
              const charSpan = document.createElement('span');
              charSpan.className = 'cell-char';
              charSpan.textContent = cell.userChar;
              div.appendChild(charSpan);
            }

            if (r === this.engine.activeRow && c === this.engine.activeCol) {
              div.classList.add('active-cell');
            } else if (activeWordCells.includes(cell)) {
              div.classList.add('active-word');
            }

            if (cell.isCorrect) div.classList.add('is-correct');
            if (cell.isError) div.classList.add('is-error');
            if (cell.isRevealed) div.classList.add('is-revealed');

            div.addEventListener('click', () => {
              this.engine.selectCell(r, c);
              if (window.GameAudio) window.GameAudio.playCrosswordTick();
              this.updateBoardDisplay();
            });
          }

          gridEl.appendChild(div);
        }
      }

      this.updateActiveClueDisplay();
      this.renderCluesPane(this.engine.direction);
    }

    updateActiveClueDisplay() {
      const badge = document.getElementById('clueBadge');
      const text = document.getElementById('clueTextMain');
      if (!badge || !text) return;

      if (this.engine.activeWord) {
        const w = this.engine.activeWord;
        badge.textContent = `${w.clueNum} ${w.direction.toUpperCase()} (${w.word.length})`;
        text.innerHTML = `<strong>${w.clue}</strong> <em>· Hint: ${w.hint || 'Examine related provisions'}</em>`;
      } else {
        badge.textContent = '---';
        text.textContent = 'Select a cell on the board to view its clue.';
      }
    }

    renderCluesPane(dir) {
      const pane = document.getElementById('cluesList');
      if (!pane || !this.currentPuzzle) return;

      const filtered = this.currentPuzzle.words.filter(w => w.direction.toLowerCase() === dir.toLowerCase());

      pane.innerHTML = filtered.map(w => {
        const isCurrent = this.engine.activeWord && this.engine.activeWord.clueNum === w.clueNum && this.engine.activeWord.direction.toLowerCase() === w.direction.toLowerCase();
        const isSolved = this.engine.completedWords.has(`${w.clueNum}-${w.direction.toLowerCase()}`);

        return `
          <div class="clue-item-row ${isCurrent ? 'active' : ''} ${isSolved ? 'solved' : ''}" data-clue="${w.clueNum}" data-dir="${w.direction}">
            <span class="clue-num-tag">${w.clueNum}</span>
            <div class="clue-desc">
              <strong>${w.clue}</strong>
              <div style="font-size:11px;color:#607387;">${w.word.length} letters · ${w.hint || ''}</div>
            </div>
          </div>
        `;
      }).join('');

      pane.querySelectorAll('.clue-item-row').forEach(row => {
        row.addEventListener('click', (e) => {
          const num = parseInt(e.currentTarget.getAttribute('data-clue'), 10);
          const d = e.currentTarget.getAttribute('data-dir');
          this.engine.selectClue(num, d);
          if (window.GameAudio) window.GameAudio.playCrosswordTick();
          this.updateBoardDisplay();
        });
      });
    }

    persistActiveProgress() {
      if (!this.engine || !this.currentPuzzle) return;
      const userEntries = [];
      for (let r = 0; r < this.engine.rows; r++) {
        for (let c = 0; c < this.engine.cols; c++) {
          const cell = this.engine.grid[r][c];
          if (!cell.isBlocked && cell.userChar) {
            userEntries.push({ r, c, char: cell.userChar, isRevealed: cell.isRevealed });
          }
        }
      }
      if (window.GameStorage) {
        window.GameStorage.saveCrosswordActive({
          puzzleId: this.currentPuzzle.id,
          userEntries,
          penalties: this.engine.penalties,
          hintsUsed: this.engine.hintsUsed,
          date: new Date().toISOString()
        });
      }
    }

    handlePuzzleCompleted() {
      window.removeEventListener('keydown', this.keyHandler);
      const scoreData = this.engine.calculateFinalScore();

      // Clear active progress
      if (window.GameStorage) {
        window.GameStorage.clearCrosswordActive();
        window.GameStorage.recordCrosswordResult(
          this.currentPuzzle.id,
          scoreData.finalScore,
          scoreData.solvedWords,
          scoreData.totalWords,
          scoreData.hintsUsed,
          scoreData.elapsedSeconds
        );
        window.GameStorage.addXP(scoreData.xpEarned);
      }

      // Check achievements
      if (window.AchievementsEngine) {
        const state = window.GameStorage.getArenaState();
        window.AchievementsEngine.evaluate(state, {
          game: 'crossword',
          puzzleId: this.currentPuzzle.id,
          difficulty: this.currentPuzzle.difficulty,
          collection: this.currentPuzzle.collection,
          score: scoreData.finalScore,
          accuracy: scoreData.accuracy,
          hintsUsed: scoreData.hintsUsed
        });
      }

      if (window.GameAudio) window.GameAudio.playVictory();
      this.renderCompletionScreen(scoreData);
    }

    renderCompletionScreen(scoreData) {
      const container = document.getElementById('crosswordApp');
      if (!container) return;

      container.innerHTML = `
        <div class="card" style="max-width:720px;margin:32px auto;padding:36px;border:2px solid #dfbf80;background:#ffffff;box-shadow:0 12px 40px rgba(20,44,70,0.12);text-align:center;">
          <div style="font-size:48px;margin-bottom:12px;">🏛</div>
          <span class="badge" style="background:#137d72;color:#ffffff;padding:4px 14px;border-radius:12px;font-size:12px;margin-bottom:8px;">PUZZLE MASTERED · 100% COMPLETE</span>
          <h1 style="font-family:Georgia,serif;color:#142c46;margin:8px 0;">Lexicon Chamber Certificate</h1>
          <p style="color:#607387;font-size:1rem;margin:0 0 24px 0;">"${this.currentPuzzle.title}" · ${this.currentPuzzle.collection}</p>

          <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(130px, 1fr));gap:12px;margin-bottom:28px;">
            <div style="background:#f4f5f8;padding:14px;border-radius:8px;">
              <small style="color:#607387;text-transform:uppercase;font-size:10px;">Final Score</small>
              <div style="font-family:Georgia,serif;font-size:1.6rem;font-weight:bold;color:#142c46;">${scoreData.finalScore}</div>
            </div>
            <div style="background:#edf7f4;padding:14px;border-radius:8px;">
              <small style="color:#137d72;text-transform:uppercase;font-size:10px;">Learning XP</small>
              <div style="font-family:Georgia,serif;font-size:1.6rem;font-weight:bold;color:#137d72;">+${scoreData.xpEarned} XP</div>
            </div>
            <div style="background:#f4f5f8;padding:14px;border-radius:8px;">
              <small style="color:#607387;text-transform:uppercase;font-size:10px;">Solved Words</small>
              <div style="font-family:Georgia,serif;font-size:1.6rem;font-weight:bold;color:#142c46;">${scoreData.solvedWords} / ${scoreData.totalWords}</div>
            </div>
            <div style="background:#f4f5f8;padding:14px;border-radius:8px;">
              <small style="color:#607387;text-transform:uppercase;font-size:10px;">Hints Penalties</small>
              <div style="font-family:Georgia,serif;font-size:1.6rem;font-weight:bold;color:#a63b49;">-${scoreData.penalties} pts</div>
            </div>
          </div>

          <!-- Academic Evaluation by Dr. Devendra Bose -->
          <div style="display:flex;align-items:center;gap:16px;background:#fff8ee;border:1px solid #dfbf80;border-radius:10px;padding:16px 20px;text-align:left;margin-bottom:28px;">
            <img src="assets/games/images/characters/crossword/devendra.svg" style="width:54px;height:54px;border-radius:50%;border:2px solid #dfbf80;" alt="Dr. Devendra Bose">
            <div style="font-size:0.92rem;color:#1c2e40;line-height:1.5;">
              <strong style="color:#7a2a35;font-family:Georgia,serif;">Dr. Devendra Bose (Keeper of the Archives):</strong>
              "Exemplary dedication, Advocate! You have successfully reconstructed the statutory tapestry of this archive. Your precision in navigating these intersecting legal tenets proves that rigorous legal vocabulary is the bedrock of judicial reasoning."
            </div>
          </div>

          <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">
            <button class="btn primary" id="btnContinueAnother" style="font-weight:bold;padding:12px 26px;">Solve Another Crossword ➔</button>
            <a href="brain-arena.html" class="btn secondary" style="padding:12px 24px;">Return to Brain Arena ⚡</a>
          </div>
        </div>
      `;

      document.getElementById('btnContinueAnother').addEventListener('click', () => {
        this.renderDashboard();
      });
    }
  }

  window.CrosswordUIController = CrosswordUIController;
  document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('crosswordApp')) {
      new CrosswordUIController();
    }
  });
})();
