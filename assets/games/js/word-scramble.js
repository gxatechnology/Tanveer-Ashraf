/**
 * LEGAL WORD SCRAMBLE: THE CODE BREAKER (V3.0 Phase 3)
 * Full interactive UI controller for word-scramble.html
 * 8 Game Modes, 5 Mystery Manuscripts, Tactile Metallic Letter Tiles,
 * Combination Lock HUD, Drag/Drop & Keyboard Typing, and Educational Feedback.
 */
(function() {
  'use strict';

  // 5 Thematic Mystery Manuscript Campaigns
  const MANUSCRIPTS = [
    {
      id: 'MS-CONST',
      title: 'The Constitutional Archive',
      subtitle: 'Foundations of Sovereign Governance & Fundamental Guarantees',
      badge: 'CONSTITUTIONAL LAW',
      color: '#137d72',
      wordKeys: ['PREAMBLE', 'SOVEREIGN', 'MANDAMUS', 'SECULAR', 'CERTIORARI'],
      illumination: 'assets/games/images/environments/lexicon.svg',
      historicalContext: 'Enshrines the indestructible sovereign, socialist, secular, democratic republic of India. The Preamble is the key to open the mind of the constitution makers (Berubari / Kesavananda Bharati).',
      statutoryReference: 'Constitution of India, 1950 — Preamble, Articles 12-35, Articles 32 & 226',
      codexExtract: 'WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC and to secure to all its citizens JUSTICE, LIBERTY, EQUALITY and FRATERNITY.'
    },
    {
      id: 'MS-CRIM',
      title: 'The Criminal Law Dossier',
      subtitle: 'Principles of Penal Liability, Mental Elements & Procedural Safeguards',
      badge: 'CRIMINAL LAW / BNS',
      color: '#a63b49',
      wordKeys: ['MENS REA', 'CULPABLE', 'HOMICIDE', 'CONSPIRACY', 'DISHONESTLY'],
      illumination: 'assets/games/images/environments/codebreaker.svg',
      historicalContext: 'Records the immutable doctrine that an act alone does not make a person guilty unless the mind is also guilty. Under the Bharatiya Nyaya Sanhita, 2023, the mental element remains the fulcrum of criminal liability.',
      statutoryReference: 'Bharatiya Nyaya Sanhita, 2023 (Sections 2, 61, 98-105); Queen v. Tolson (1889)',
      codexExtract: 'Actus non facit reum nisi mens sit rea. No act is actionable as an offense unless accompanied by a culpable state of mind—whether intention, knowledge, recklessness, or statutory negligence.'
    },
    {
      id: 'MS-EVID',
      title: 'The Evidence Vault',
      subtitle: 'The Architecture of Judicial Proof, Relevancy & Presumptions',
      badge: 'EVIDENCE / BSA',
      color: '#246c63',
      wordKeys: ['ADMISSIBLE', 'ESTOPPEL', 'CONFESSION', 'RELEVANT', 'BURDEN'],
      illumination: 'assets/games/images/environments/lexicon.svg',
      historicalContext: 'Preserves the rigorous evidentiary machinery governing how facts are brought before a court. Relevancy is the test of logic; admissibility is the rule of law. Governed by the Bharatiya Sakshya Adhiniyam, 2023.',
      statutoryReference: 'Bharatiya Sakshya Adhiniyam, 2023 (Sections 3, 22-26, 104-108, 121); Pakala Narayana Swami v. Emperor',
      codexExtract: 'The fundamental maxim of proof: All admissible evidence is relevant, but not all relevant evidence is admissible. He who asserts must prove, and estoppel binds the tongue of contradiction.'
    },
    {
      id: 'MS-MAXIM',
      title: 'The Book of Legal Maxims',
      subtitle: 'Timeless Latin Jurisprudence & Foundational Principles of Natural Justice',
      badge: 'LATIN MAXIMS & JURISPRUDENCE',
      color: '#dfbf80',
      wordKeys: ['AUDI ALTERAM', 'NEMO JUDEX', 'RES JUDICATA', 'UBI JUS', 'BONA FIDE'],
      illumination: 'assets/games/images/environments/codebreaker.svg',
      historicalContext: 'Distills centuries of classical Roman and English Common Law jurisprudence into pithy, universal legal truths. Natural justice forms the very heartbeat of judicial decision-making.',
      statutoryReference: 'Maneka Gandhi v. Union of India; A.K. Kraipak v. Union of India; CPC 1908 Section 11',
      codexExtract: 'Audi alteram partem — hear the other side. Nemo judex in causa sua — no person shall be a judge in their own cause. Ubi jus ibi remedium — where there is a right, there is a judicial remedy.'
    },
    {
      id: 'MS-CIVIL',
      title: 'The Civil Justice Manuscript',
      subtitle: 'Adjudication of Substantive Rights, Pleadings & Decree Execution',
      badge: 'CIVIL PROCEDURE CODE',
      color: '#1b5365',
      wordKeys: ['INJUNCTION', 'PLEADINGS', 'EXECUTION', 'SUMMONS', 'JURISDICTION'],
      illumination: 'assets/games/images/environments/lexicon.svg',
      historicalContext: 'Codifies the procedural architecture of civil disputes. Procedure is the handmaid of justice, designed to facilitate substantive fairness rather than to obstruct it.',
      statutoryReference: 'Code of Civil Procedure, 1908 (Sections 9, 26, 38, 51; Orders VI, VII, VIII, XXI, XXXIX)',
      codexExtract: 'Civil justice ensures that every civil wrong meets a lawful decree. Jurisdiction is the foundation of authority, pleadings frame the dispute, and execution brings judicial orders to reality.'
    }
  ];

  class WordScrambleUIController {
    constructor() {
      this.vocabulary = window.ARENA_VOCABULARY || [];
      this.vocabByCanonical = window.ARENA_VOCAB_BY_CANONICAL || {};
      this.currentMode = 'classic';
      this.currentWord = null;
      this.scrambledData = null;
      this.placedTiles = []; // array corresponding to slots: tileObj or null
      this.trayTiles = []; // array of tileObj remaining in tray
      this.historyMoves = []; // stack of { tileId, fromSlot, toSlot }
      
      // HUD state
      this.streak = 0;
      this.score = 0;
      this.multiplier = 1.0;
      this.timerInterval = null;
      this.timeLeft = 60;
      this.memoryCountdown = 3;
      this.isMemoryHiding = false;
      this.hintsUsedInWord = 0;
      this.currentManuscript = null;
      this.manuscriptWordIndex = 0;

      this.init();
    }

    init() {
      // Check for saved active session
      const saved = window.GameStorage ? window.GameStorage.getScrambleActive() : null;
      if (saved && saved.currentWordId) {
        const found = this.vocabulary.find(v => v.id === saved.currentWordId);
        if (found) {
          this.currentMode = saved.mode || 'classic';
          this.streak = saved.streak || 0;
          this.score = saved.score || 0;
          if (this.currentMode === 'manuscript' && saved.manuscriptId) {
            this.currentManuscript = MANUSCRIPTS.find(m => m.id === saved.manuscriptId) || null;
            this.manuscriptWordIndex = saved.manuscriptWordIndex || 0;
          }
          if (this.currentMode === 'manuscript' && !this.currentManuscript) {
            this.currentMode = 'classic';
          }
          this.loadWord(found, false);
          return;
        }
      }

      this.renderDashboard();
    }

    renderDashboard() {
      this.stopTimer();
      const container = document.getElementById('scrambleApp');
      if (!container) return;

      const state = window.GameStorage ? window.GameStorage.getArenaState() : {};
      const completedWords = (state.scramble && state.scramble.completedWords) || {};
      const completedCount = Object.keys(completedWords).length;
      const unlockedManuscripts = (state.scramble && state.scramble.unlockedManuscripts) || {};
      const unlockedMSCount = Object.keys(unlockedManuscripts).length;

      const today = new Date().toISOString().slice(0, 10);
      const dailyWord = window.VocabularyEngine ? window.VocabularyEngine.getDailyWord(this.vocabulary, today) : this.vocabulary[0];

      container.innerHTML = `
        <div class="puzzle-env-hero">
          <img src="assets/games/images/environments/codebreaker.svg" class="puzzle-env-bg" alt="Code Breaker Background">
          <div class="puzzle-hero-content">
            <span class="badge" style="background:#2fe0c822;color:#2fe0c8;border:1px solid #2fe0c8;margin-bottom:8px;">GAME 6 · THE CODE BREAKER</span>
            <h1>Legal Word Scramble</h1>
            <div class="puzzle-tagline">"Decode the Word. Discover the Law."</div>
            <p style="max-width:680px;color:#dce3ea;font-size:0.95rem;line-height:1.5;">
              Step into the legal cryptographic chamber. Unscramble verified Indian statutory terminology, Latin maxims, and landmark judicial doctrines using tactile gold metallic tiles, drag-and-drop, or rapid keyboard typing.
            </p>
            <div class="puzzle-stats-strip">
              <div class="puzzle-stat-pill">🔠 Solved Terms: <strong>${completedCount} / ${this.vocabulary.length}</strong></div>
              <div class="puzzle-stat-pill">📜 Unlocked Manuscripts: <strong>${unlockedMSCount} / ${MANUSCRIPTS.length}</strong></div>
              <div class="puzzle-stat-pill">⚡ Arena Level: <strong>${state.level || 1}</strong></div>
            </div>
          </div>
        </div>

        ${dailyWord ? `
          <div class="card" style="border:2px solid #2fe0c8;background:#f0fbf9;margin-bottom:24px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;padding:18px 24px;gap:16px;">
            <div>
              <span class="badge" style="background:#137d72;color:#fff;">🌟 DAILY CIPHER CHALLENGE</span>
              <h3 style="font-family:Georgia,serif;margin:6px 0 2px 0;color:#142c46;">Daily Statutory Decryption</h3>
              <p style="margin:0;color:#607387;font-size:0.9rem;">${dailyWord.subject} · ${dailyWord.difficulty.toUpperCase()} · ${dailyWord.canonical.length} Letters · +50 Bonus XP</p>
            </div>
            <button class="btn primary" id="btnLaunchDailyWord" style="background:#137d72;border-color:#137d72;font-weight:bold;padding:10px 22px;">Crack Daily Word ➔</button>
          </div>
        ` : ''}

        <!-- 8 Game Mode Selection Grid -->
        <h2 style="font-family:Georgia,serif;color:#142c46;margin-bottom:14px;">Select Decryption Mode</h2>
        <div style="display:grid;grid-template-columns:repeat(auto-fill, minmax(280px, 1fr));gap:16px;margin-bottom:32px;">
          
          <!-- Mode 1: Classic -->
          <div class="card mode-card" data-mode="classic" style="cursor:pointer;border:2px solid #dce3ea;transition:all 0.15s ease;padding:20px;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
              <span style="font-size:28px;">🔠</span>
              <span class="badge" style="background:#edf7f4;color:#137d72;">Progressive</span>
            </div>
            <h3 style="font-family:Georgia,serif;color:#142c46;margin:0 0 6px 0;">Classic Mode</h3>
            <p style="color:#607387;font-size:0.88rem;margin:0 0 14px 0;line-height:1.4;">Unscramble single legal words with progressive difficulty from beginner to advanced.</p>
            <button class="btn secondary" style="width:100%;font-weight:bold;">Launch Classic ➔</button>
          </div>

          <!-- Mode 2: Legal Maxims -->
          <div class="card mode-card" data-mode="maxims" style="cursor:pointer;border:2px solid #dce3ea;transition:all 0.15s ease;padding:20px;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
              <span style="font-size:28px;">🏛</span>
              <span class="badge" style="background:#fff8ee;color:#a8792c;">Latin Maxims</span>
            </div>
            <h3 style="font-family:Georgia,serif;color:#142c46;margin:0 0 6px 0;">Legal Maxims</h3>
            <p style="color:#607387;font-size:0.88rem;margin:0 0 14px 0;line-height:1.4;">Decode foundational Latin maxims and phrases essential for PCS-J preliminary & mains.</p>
            <button class="btn secondary" style="width:100%;font-weight:bold;">Decode Maxims ➔</button>
          </div>

          <!-- Mode 3: Definition Challenge -->
          <div class="card mode-card" data-mode="definition" style="cursor:pointer;border:2px solid #dce3ea;transition:all 0.15s ease;padding:20px;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
              <span style="font-size:28px;">📖</span>
              <span class="badge" style="background:#eef2f6;color:#142c46;">Definitions</span>
            </div>
            <h3 style="font-family:Georgia,serif;color:#142c46;margin:0 0 6px 0;">Definition Challenge</h3>
            <p style="color:#607387;font-size:0.88rem;margin:0 0 14px 0;line-height:1.4;">Read the authentic statutory definition, deduce the legal concept, and unscramble the term.</p>
            <button class="btn secondary" style="width:100%;font-weight:bold;">Test Definitions ➔</button>
          </div>

          <!-- Mode 4: Statutory Keywords -->
          <div class="card mode-card" data-mode="statutory" style="cursor:pointer;border:2px solid #dce3ea;transition:all 0.15s ease;padding:20px;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
              <span style="font-size:28px;">⚖</span>
              <span class="badge" style="background:#edf7f4;color:#137d72;">BNS / BSA / CPC</span>
            </div>
            <h3 style="font-family:Georgia,serif;color:#142c46;margin:0 0 6px 0;">Statutory Keywords</h3>
            <p style="color:#607387;font-size:0.88rem;margin:0 0 14px 0;line-height:1.4;">Target high-frequency keywords from Bharatiya Nyaya Sanhita, Sakshya Adhiniyam & CPC.</p>
            <button class="btn secondary" style="width:100%;font-weight:bold;">Crack Statutes ➔</button>
          </div>

          <!-- Mode 5: Landmark Cases -->
          <div class="card mode-card" data-mode="cases" style="cursor:pointer;border:2px solid #dce3ea;transition:all 0.15s ease;padding:20px;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
              <span style="font-size:28px;">📜</span>
              <span class="badge" style="background:#fce8e6;color:#a63b49;">Doctrines & Cases</span>
            </div>
            <h3 style="font-family:Georgia,serif;color:#142c46;margin:0 0 6px 0;">Landmark Cases</h3>
            <p style="color:#607387;font-size:0.88rem;margin:0 0 14px 0;line-height:1.4;">Reconstruct famous case doctrines, constitutional rulings, and precedent titles.</p>
            <button class="btn secondary" style="width:100%;font-weight:bold;">Solve Cases ➔</button>
          </div>

          <!-- Mode 6: Memory Recall -->
          <div class="card mode-card" data-mode="memory" style="cursor:pointer;border:2px solid #dce3ea;transition:all 0.15s ease;padding:20px;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
              <span style="font-size:28px;">🧠</span>
              <span class="badge" style="background:#fff8ee;color:#b98a38;">Flash Memory</span>
            </div>
            <h3 style="font-family:Georgia,serif;color:#142c46;margin:0 0 6px 0;">Memory Recall</h3>
            <p style="color:#607387;font-size:0.88rem;margin:0 0 14px 0;line-height:1.4;">The term is shown for 3 seconds before scrambling. Reconstruct the spelling purely from memory.</p>
            <button class="btn secondary" style="width:100%;font-weight:bold;">Test Memory ➔</button>
          </div>

          <!-- Mode 7: Time Attack -->
          <div class="card mode-card" data-mode="timed" style="cursor:pointer;border:2px solid #dce3ea;transition:all 0.15s ease;padding:20px;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
              <span style="font-size:28px;">⏱</span>
              <span class="badge" style="background:#fee2e2;color:#b91c1c;">60s Sprint</span>
            </div>
            <h3 style="font-family:Georgia,serif;color:#142c46;margin:0 0 6px 0;">Time Attack</h3>
            <p style="color:#607387;font-size:0.88rem;margin:0 0 14px 0;line-height:1.4;">60-second rapid unscrambling chain. Each correct word adds +10 seconds and builds multiplier.</p>
            <button class="btn secondary" style="width:100%;font-weight:bold;">Start Rush ➔</button>
          </div>

          <!-- Mode 8: Mystery Manuscript -->
          <div class="card mode-card" data-mode="manuscript" style="cursor:pointer;border:2px solid #dfbf80;background:#fffdf7;transition:all 0.15s ease;padding:20px;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
              <span style="font-size:28px;">🗝</span>
              <span class="badge" style="background:#dfbf80;color:#142c46;font-weight:bold;">Thematic Scrolls</span>
            </div>
            <h3 style="font-family:Georgia,serif;color:#142c46;margin:0 0 6px 0;">Mystery Manuscript</h3>
            <p style="color:#607387;font-size:0.88rem;margin:0 0 14px 0;line-height:1.4;">Solve 5 linked thematic legal terms to reconstruct and unlock ancient illuminated judicial folios.</p>
            <button class="btn gold" style="width:100%;font-weight:bold;">Unlock Scrolls ➔</button>
          </div>

        </div>

        <!-- Manuscript Archive Showcase -->
        <div class="card" style="padding:24px;border:1px solid #dce3ea;margin-bottom:28px;">
          <h3 style="font-family:Georgia,serif;color:#142c46;margin:0 0 6px 0;">The Illuminated Manuscript Vault</h3>
          <p style="color:#607387;font-size:0.9rem;margin:0 0 16px 0;">Uncover all five master judicial codices to demonstrate comprehensive legal mastery.</p>
          <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(200px, 1fr));gap:12px;">
            ${MANUSCRIPTS.map(ms => {
              const isUnlocked = !!unlockedManuscripts[ms.id];
              return `
                <div style="border:1px solid ${isUnlocked ? '#dfbf80' : '#dce3ea'};background:${isUnlocked ? '#fffdf7' : '#f8fafc'};padding:12px;border-radius:8px;text-align:center;">
                  <div style="font-size:24px;margin-bottom:4px;">${isUnlocked ? '📜' : '🔒'}</div>
                  <strong style="display:block;font-size:0.85rem;color:${isUnlocked ? '#142c46' : '#94a3b8'};font-family:Georgia,serif;">${ms.title}</strong>
                  <small style="color:${isUnlocked ? '#137d72' : '#94a3b8'};font-size:0.75rem;">${isUnlocked ? 'UNLOCKED' : 'LOCKED'}</small>
                </div>
              `;
            }).join('')}
          </div>
        </div>
      `;

      // Event listeners for modes
      container.querySelectorAll('.mode-card').forEach(card => {
        card.addEventListener('click', () => {
          const mode = card.getAttribute('data-mode');
          this.startMode(mode);
        });
      });

      const btnDaily = document.getElementById('btnLaunchDailyWord');
      if (btnDaily && dailyWord) {
        btnDaily.addEventListener('click', () => {
          this.currentMode = 'classic';
          this.loadWord(dailyWord);
        });
      }
    }

    startMode(mode) {
      this.currentMode = mode;
      this.streak = 0;
      this.score = 0;
      this.multiplier = 1.0;
      this.hintsUsedInWord = 0;

      if (mode === 'manuscript') {
        this.renderManuscriptSelector();
        return;
      }

      if (mode === 'timed') {
        this.timeLeft = 60;
        this.startTimer();
      }

      this.loadNextWordForMode();
    }

    renderManuscriptSelector() {
      const container = document.getElementById('scrambleApp');
      if (!container) return;

      const state = window.GameStorage ? window.GameStorage.getArenaState() : {};
      const unlockedManuscripts = (state.scramble && state.scramble.unlockedManuscripts) || {};

      container.innerHTML = `
        <div style="margin-bottom:20px;display:flex;justify-content:space-between;align-items:center;">
          <button class="btn secondary" id="btnBackToDashboard">← Back to Code Breaker</button>
          <span class="badge" style="background:#dfbf80;color:#142c46;font-weight:bold;">MYSTERY MANUSCRIPTS</span>
        </div>

        <div class="card" style="border:2px solid #dfbf80;background:#fffdf7;padding:24px;margin-bottom:24px;">
          <h2 style="font-family:Georgia,serif;color:#142c46;margin:0 0 6px 0;">Select an Ancient Legal Codex</h2>
          <p style="color:#607387;font-size:0.95rem;margin:0;">Each codex contains 5 interconnected statutory tenets. Unscramble all five terms to restore and illuminate the historical judicial manuscript.</p>
        </div>

        <div style="display:grid;grid-template-columns:repeat(auto-fill, minmax(320px, 1fr));gap:20px;">
          ${MANUSCRIPTS.map((ms, idx) => {
            const isUnlocked = !!unlockedManuscripts[ms.id];
            return `
              <div class="card ms-select-card" data-ms-id="${ms.id}" style="cursor:pointer;border:2px solid ${isUnlocked ? '#dfbf80' : '#cbd5e1'};background:#ffffff;padding:24px;display:flex;flex-direction:column;justify-content:space-between;transition:transform 0.15s ease;">
                <div>
                  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
                    <span class="badge" style="background:${ms.color}22;color:${ms.color};border:1px solid ${ms.color};">${ms.badge}</span>
                    <span style="font-size:1.2rem;">${isUnlocked ? '📜' : '🔒'}</span>
                  </div>
                  <h3 style="font-family:Georgia,serif;color:#142c46;margin:0 0 6px 0;">${ms.title}</h3>
                  <div style="color:#854d0e;font-size:0.85rem;font-style:italic;margin-bottom:12px;">${ms.subtitle}</div>
                  <p style="color:#607387;font-size:0.88rem;line-height:1.4;margin:0 0 16px 0;">${ms.historicalContext}</p>
                </div>
                <div>
                  <div style="font-size:0.8rem;color:#94a3b8;margin-bottom:12px;">5 Statutory Passwords · ${isUnlocked ? 'Mastered & Archived' : 'Requires Decryption'}</div>
                  <button class="btn ${isUnlocked ? 'secondary' : 'gold'}" style="width:100%;font-weight:bold;">${isUnlocked ? 'Re-examine Codex' : 'Begin Decryption ➔'}</button>
                </div>
              </div>
            `;
          }).join('')}
        </div>
      `;

      document.getElementById('btnBackToDashboard').addEventListener('click', () => {
        this.renderDashboard();
      });

      container.querySelectorAll('.ms-select-card').forEach(card => {
        card.addEventListener('click', () => {
          const msId = card.getAttribute('data-ms-id');
          const ms = MANUSCRIPTS.find(m => m.id === msId);
          if (ms) {
            this.startManuscriptCampaign(ms);
          }
        });
      });
    }

    startManuscriptCampaign(manuscript) {
      this.currentMode = 'manuscript';
      this.currentManuscript = manuscript;
      this.manuscriptWordIndex = 0;
      this.loadManuscriptWord();
    }

    loadManuscriptWord() {
      const key = this.currentManuscript.wordKeys[this.manuscriptWordIndex];
      let vocab = this.vocabByCanonical[key.toUpperCase()];
      if (!vocab) {
        vocab = this.vocabulary.find(v => v.canonical.toUpperCase().includes(key.toUpperCase())) || {
          id: `ms-${this.manuscriptWordIndex}`,
          canonical: key,
          subject: this.currentManuscript.badge,
          primaryClue: `Foundational term in ${this.currentManuscript.title}`,
          difficulty: 'intermediate',
          definition: `Statutory element of ${this.currentManuscript.subtitle}`,
          statuteOrAuthority: this.currentManuscript.statutoryReference
        };
      }
      this.loadWord(vocab);
    }

    loadNextWordForMode() {
      let pool = [...this.vocabulary];

      if (this.currentMode === 'maxims') {
        pool = pool.filter(v => v.subject === 'Latin Maxims' || v.subject === 'Jurisprudence' || v.canonical.includes(' '));
      } else if (this.currentMode === 'statutory') {
        pool = pool.filter(v => v.subject === 'Criminal Law' || v.subject === 'Civil Procedure Code' || v.subject === 'Law of Evidence');
      } else if (this.currentMode === 'cases') {
        pool = pool.filter(v => v.subject === 'Constitutional Law' || (v.statuteOrAuthority && v.statuteOrAuthority.includes('v.')));
      } else if (this.currentMode === 'definition') {
        pool = pool.filter(v => v.definition && v.definition.length > 30);
      } else if (this.currentMode === 'classic') {
        // Sort or select based on streak
        if (this.streak < 3) pool = pool.filter(v => v.difficulty === 'beginner');
        else if (this.streak < 8) pool = pool.filter(v => v.difficulty === 'intermediate');
        else pool = pool.filter(v => v.difficulty === 'advanced');
      }

      if (pool.length === 0) pool = this.vocabulary;
      const nextWord = pool[Math.floor(Math.random() * pool.length)];
      this.loadWord(nextWord);
    }

    loadWord(vocab, saveActive = true) {
      this.currentWord = vocab;
      this.hintsUsedInWord = 0;
      this.historyMoves = [];

      // Create tiles
      const canonical = vocab.canonical.toUpperCase().trim();
      const scrambleResult = window.VocabularyEngine ? 
        window.VocabularyEngine.createLetterTiles(canonical) : 
        { scrambledStr: canonical, tiles: [] };
      
      this.scrambledData = scrambleResult;
      
      // Initialize slots structure
      this.placedTiles = [];
      for (let i = 0; i < canonical.length; i++) {
        if (canonical[i] === ' ') {
          this.placedTiles.push({ isSpace: true, char: ' ' });
        } else {
          this.placedTiles.push(null);
        }
      }

      // Initialize tray
      this.trayTiles = scrambleResult.tiles.filter(t => !t.isSpace);

      if (saveActive && window.GameStorage) {
        window.GameStorage.saveScrambleActive({
          currentWordId: vocab.id,
          mode: this.currentMode,
          streak: this.streak,
          score: this.score,
          manuscriptId: this.currentManuscript ? this.currentManuscript.id : null,
          manuscriptWordIndex: this.manuscriptWordIndex
        });
      }

      if (this.currentMode === 'memory') {
        this.startMemoryCountdown();
      } else {
        this.renderPlayView();
      }
    }

    startMemoryCountdown() {
      this.isMemoryHiding = true;
      this.memoryCountdown = 3;
      this.renderMemoryFlashView();

      const cdInterval = setInterval(() => {
        this.memoryCountdown--;
        if (this.memoryCountdown <= 0) {
          clearInterval(cdInterval);
          this.isMemoryHiding = false;
          this.renderPlayView();
        } else {
          this.renderMemoryFlashView();
        }
      }, 1000);
    }

    renderMemoryFlashView() {
      const container = document.getElementById('scrambleApp');
      if (!container) return;

      container.innerHTML = `
        <div class="card" style="max-width:680px;margin:40px auto;text-align:center;padding:48px 32px;border:2px solid #b98a38;background:#fffdf7;box-shadow:0 12px 40px rgba(20,44,70,0.15);">
          <span class="badge" style="background:#b98a38;color:#fff;font-size:12px;margin-bottom:12px;">🧠 MEMORY RECALL MODE</span>
          <h2 style="font-family:Georgia,serif;color:#142c46;margin:0 0 16px 0;">Memorize the Legal Word</h2>
          <div style="font-family:Georgia,serif;font-size:2.4rem;color:#137d72;letter-spacing:4px;font-weight:bold;margin:24px 0;background:#edf7f4;padding:16px;border-radius:8px;border:1px dashed #137d72;">
            ${this.currentWord.canonical}
          </div>
          <p style="color:#607387;font-size:0.95rem;margin:0 0 24px 0;">${this.currentWord.primaryClue}</p>
          <div style="display:flex;justify-content:center;align-items:center;gap:10px;">
            <div style="font-size:1.5rem;font-weight:bold;color:#a63b49;background:#fce8e6;width:54px;height:54px;border-radius:50%;display:flex;align-items:center;justify-content:center;border:2px solid #a63b49;">
              ${this.memoryCountdown}
            </div>
            <span style="color:#607387;font-size:0.9rem;">Scrambling letters in ${this.memoryCountdown} seconds...</span>
          </div>
        </div>
      `;
    }

    renderPlayView() {
      const container = document.getElementById('scrambleApp');
      if (!container) return;

      this.updateMultiplier();

      container.innerHTML = `
        <div class="codebreaker-arena">
          
          <!-- Top Combination Lock HUD -->
          <div class="combination-lock-hud">
            <div class="lock-dial-group">
              <span style="font-size:0.85rem;text-transform:uppercase;color:#94a3b8;">MODE:</span>
              <strong style="color:#dfbf80;font-family:Georgia,serif;">${this.currentMode.toUpperCase()}</strong>
            </div>

            <div class="lock-dial-group">
              <div style="text-align:center;">
                <small style="color:#94a3b8;font-size:10px;display:block;">DECIPHER STREAK</small>
                <div class="lock-dial">${this.streak} 🔥</div>
              </div>

              <div style="text-align:center;">
                <small style="color:#94a3b8;font-size:10px;display:block;">SCORE</small>
                <div class="lock-dial">${this.score}</div>
              </div>

              <div style="text-align:center;">
                <small style="color:#94a3b8;font-size:10px;display:block;">MULTIPLIER</small>
                <div class="combo-badge">${this.multiplier.toFixed(1)}x</div>
              </div>

              ${this.currentMode === 'timed' ? `
                <div style="text-align:center;">
                  <small style="color:#f87171;font-size:10px;display:block;">TIME LEFT</small>
                  <div class="lock-dial" style="color:#f87171;border-color:#f87171;" id="timeDial">${this.timeLeft}s</div>
                </div>
              ` : ''}

              ${this.currentMode === 'manuscript' ? `
                <div style="text-align:center;">
                  <small style="color:#2fe0c8;font-size:10px;display:block;">CODEX PROGRESS</small>
                  <div class="lock-dial" style="color:#2fe0c8;">${this.manuscriptWordIndex + 1} / 5</div>
                </div>
              ` : ''}
            </div>

            <div>
              <button class="btn secondary" id="btnExitScramble" style="padding:6px 14px;font-size:0.85rem;">Exit Mode</button>
            </div>
          </div>

          <!-- Main Decoding Workspace -->
          <div class="decoding-workspace-card">
            
            <!-- Clue Banner -->
            <div class="clue-banner">
              <span class="clue-category">${this.currentWord.subject || 'UP PCS-J LEGAL VOCABULARY'}</span>
              <h2 class="clue-prompt">"${this.currentWord.primaryClue}"</h2>
              ${this.currentWord.additionalHint ? `<small style="color:#607387;display:block;">Hint: ${this.currentWord.additionalHint}</small>` : ''}
            </div>

            <!-- Advisor Commentary / Guidance -->
            <div style="display:flex;align-items:center;gap:12px;background:#f8fafc;border:1px solid #dce3ea;border-radius:8px;padding:8px 14px;max-width:640px;width:100%;">
              <img src="assets/games/images/characters/detective/kabir.svg" style="width:38px;height:38px;border-radius:50%;border:1px solid #dfbf80;" alt="Adv. Kabir Mehta">
              <div style="font-size:0.84rem;color:#1c2e40;line-height:1.35;">
                <strong style="color:#142c46;">Adv. Kabir Mehta:</strong>
                <span id="advisorCommentary">${this.getAdvisorCommentary()}</span>
              </div>
            </div>

            <!-- Answer Slots Rack -->
            <div class="answer-slots-rack" id="answerSlotsRack">
              ${this.renderAnswerSlots()}
            </div>

            <!-- Scrambled Tile Tray -->
            <div class="scrambled-tile-tray" id="scrambledTray">
              ${this.renderTrayTiles()}
            </div>

            <!-- Control Action Bar -->
            <div class="scramble-actions-bar">
              <button class="btn secondary" id="btnShuffleTiles" title="Shuffle unplaced tiles">🔀 Shuffle</button>
              <button class="btn secondary" id="btnUndoMove" title="Undo last placed tile">↩ Undo</button>
              <button class="btn secondary" id="btnClearTiles" title="Clear all placed tiles">✕ Clear</button>
              <button class="btn secondary" id="btnScrambleHint" title="Reveal 1 correct letter (-15 pts)">💡 Hint</button>
              <button class="btn primary" id="btnSubmitWord" style="background:#137d72;border-color:#137d72;padding:8px 24px;font-weight:bold;">Check Cipher ➔</button>
            </div>

          </div>

          <!-- Educational Feedback Toast Mount -->
          <div id="scrambleFeedbackMount"></div>

        </div>
      `;

      this.attachEventListeners();
    }

    renderAnswerSlots() {
      return this.placedTiles.map((slot, idx) => {
        if (slot && slot.isSpace) {
          return `<div class="answer-slot space-slot" data-slot-idx="${idx}"></div>`;
        }
        if (slot) {
          return `
            <div class="answer-slot filled" data-slot-idx="${idx}">
              <div class="letter-tile in-slot" data-tile-id="${slot.id}">${slot.char}</div>
            </div>
          `;
        }
        return `<div class="answer-slot" data-slot-idx="${idx}"></div>`;
      }).join('');
    }

    renderTrayTiles() {
      if (this.trayTiles.length === 0) {
        return `<span style="color:#94a3b8;font-size:0.9rem;padding:8px;">All letters placed in cipher rack. Ready to submit!</span>`;
      }
      return this.trayTiles.map(tile => `
        <div class="letter-tile" draggable="true" data-tile-id="${tile.id}">
          ${tile.char}
        </div>
      `).join('');
    }

    getAdvisorCommentary() {
      if (this.streak >= 5) {
        return "Remarkable velocity! Your statutory reflexes are performing at bench caliber.";
      }
      if (this.currentMode === 'maxims') {
        return "Latin maxims encapsulate the core equity of common law. Examine the stem words carefully.";
      }
      if (this.currentMode === 'manuscript' && this.currentManuscript) {
        return `We are piecing together ${this.currentManuscript.title}. Term ${this.manuscriptWordIndex + 1} of 5 is crucial.`;
      }
      return "Click tiles, drag them into the rack, or type on your physical keyboard. Speed and precision build multipliers!";
    }

    updateMultiplier() {
      if (this.streak >= 10) this.multiplier = 3.0;
      else if (this.streak >= 8) this.multiplier = 2.5;
      else if (this.streak >= 5) this.multiplier = 2.0;
      else if (this.streak >= 3) this.multiplier = 1.5;
      else this.multiplier = 1.0;
    }

    attachEventListeners() {
      const container = document.getElementById('scrambleApp');
      if (!container) return;

      // Exit button
      const btnExit = document.getElementById('btnExitScramble');
      if (btnExit) {
        btnExit.addEventListener('click', () => {
          this.stopTimer();
          if (window.GameStorage) window.GameStorage.clearScrambleActive();
          this.renderDashboard();
        });
      }

      // Action Buttons
      document.getElementById('btnShuffleTiles').addEventListener('click', () => this.shuffleTray());
      document.getElementById('btnUndoMove').addEventListener('click', () => this.undoLastMove());
      document.getElementById('btnClearTiles').addEventListener('click', () => this.clearAllTiles());
      document.getElementById('btnScrambleHint').addEventListener('click', () => this.useHint());
      document.getElementById('btnSubmitWord').addEventListener('click', () => this.submitAnswer());

      // Tray tile click to place in next available slot
      const tray = document.getElementById('scrambledTray');
      tray.querySelectorAll('.letter-tile').forEach(tileEl => {
        tileEl.addEventListener('click', (e) => {
          const tileId = e.currentTarget.getAttribute('data-tile-id');
          this.placeTileInNextSlot(tileId);
        });

        // HTML5 dragstart
        tileEl.addEventListener('dragstart', (e) => {
          const tileId = e.currentTarget.getAttribute('data-tile-id');
          e.dataTransfer.setData('text/plain', tileId);
        });
      });

      // Slot click to return tile to tray
      const rack = document.getElementById('answerSlotsRack');
      rack.querySelectorAll('.answer-slot.filled').forEach(slotEl => {
        slotEl.addEventListener('click', (e) => {
          const slotIdx = parseInt(e.currentTarget.getAttribute('data-slot-idx'), 10);
          this.returnTileToTray(slotIdx);
        });
      });

      // HTML5 dragover & drop on answer slots
      rack.querySelectorAll('.answer-slot:not(.space-slot)').forEach(slotEl => {
        slotEl.addEventListener('dragover', (e) => {
          e.preventDefault();
        });
        slotEl.addEventListener('drop', (e) => {
          e.preventDefault();
          const tileId = e.dataTransfer.getData('text/plain');
          const slotIdx = parseInt(e.currentTarget.getAttribute('data-slot-idx'), 10);
          this.placeTileInSpecificSlot(tileId, slotIdx);
        });
      });

      // Physical Keyboard Listener
      if (!this.boundKeyHandler) {
        this.boundKeyHandler = this.handlePhysicalKey.bind(this);
        window.addEventListener('keydown', this.boundKeyHandler);
      }
    }

    handlePhysicalKey(e) {
      // Don't intercept if user is typing in an input or textarea
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
      if (!this.currentWord) return;

      const key = e.key.toUpperCase();

      if (key === 'ENTER') {
        e.preventDefault();
        this.submitAnswer();
      } else if (key === 'BACKSPACE') {
        e.preventDefault();
        this.undoLastMove();
      } else if (key === 'ESCAPE') {
        this.clearAllTiles();
      } else if (/^[A-Z]$/.test(key)) {
        // Find matching letter in tray
        const matchingTile = this.trayTiles.find(t => t.char === key);
        if (matchingTile) {
          this.placeTileInNextSlot(matchingTile.id);
        }
      }
    }

    placeTileInNextSlot(tileId) {
      const tileIndex = this.trayTiles.findIndex(t => t.id === tileId);
      if (tileIndex === -1) return;

      // Find first empty non-space slot
      const nextSlotIdx = this.placedTiles.findIndex(s => s === null);
      if (nextSlotIdx === -1) return; // all slots filled

      const tile = this.trayTiles.splice(tileIndex, 1)[0];
      this.placedTiles[nextSlotIdx] = tile;
      this.historyMoves.push({ tileId: tile.id, fromTray: true, slotIdx: nextSlotIdx });

      if (window.GameAudio) window.GameAudio.playTileSnap();
      this.refreshBoardUI();
    }

    placeTileInSpecificSlot(tileId, slotIdx) {
      if (this.placedTiles[slotIdx] !== null) {
        // Swap or return existing
        this.returnTileToTray(slotIdx, false);
      }

      const tileIndex = this.trayTiles.findIndex(t => t.id === tileId);
      if (tileIndex !== -1) {
        const tile = this.trayTiles.splice(tileIndex, 1)[0];
        this.placedTiles[slotIdx] = tile;
        this.historyMoves.push({ tileId: tile.id, fromTray: true, slotIdx: slotIdx });
        if (window.GameAudio) window.GameAudio.playTileSnap();
        this.refreshBoardUI();
      }
    }

    returnTileToTray(slotIdx, refresh = true) {
      const tile = this.placedTiles[slotIdx];
      if (!tile || tile.isSpace) return;

      this.placedTiles[slotIdx] = null;
      this.trayTiles.push(tile);
      this.historyMoves.push({ tileId: tile.id, fromTray: false, slotIdx: slotIdx });

      if (window.GameAudio) window.GameAudio.playTileClick();
      if (refresh) this.refreshBoardUI();
    }

    shuffleTray() {
      if (this.trayTiles.length <= 1) return;
      this.trayTiles = window.VocabularyEngine ? window.VocabularyEngine.fisherYates(this.trayTiles) : this.trayTiles.reverse();
      if (window.GameAudio) window.GameAudio.playTileShuffle();
      this.refreshBoardUI();
    }

    undoLastMove() {
      // Find the last filled non-space slot and return it
      for (let i = this.placedTiles.length - 1; i >= 0; i--) {
        if (this.placedTiles[i] && !this.placedTiles[i].isSpace) {
          this.returnTileToTray(i);
          return;
        }
      }
    }

    clearAllTiles() {
      for (let i = 0; i < this.placedTiles.length; i++) {
        if (this.placedTiles[i] && !this.placedTiles[i].isSpace) {
          this.trayTiles.push(this.placedTiles[i]);
          this.placedTiles[i] = null;
        }
      }
      this.historyMoves = [];
      if (window.GameAudio) window.GameAudio.playTileShuffle();
      this.refreshBoardUI();
    }

    useHint() {
      // Find the first unfilled slot
      const nextSlotIdx = this.placedTiles.findIndex(s => s === null);
      if (nextSlotIdx === -1) return;

      const targetChar = this.currentWord.canonical.toUpperCase()[nextSlotIdx];
      
      // Find a tile in the tray with this character
      const tileIdx = this.trayTiles.findIndex(t => t.char === targetChar);
      if (tileIdx !== -1) {
        this.hintsUsedInWord++;
        const tile = this.trayTiles.splice(tileIdx, 1)[0];
        this.placedTiles[nextSlotIdx] = tile;
        if (window.GameAudio) window.GameAudio.playTileSnap();
        this.refreshBoardUI();
      }
    }

    refreshBoardUI() {
      const rack = document.getElementById('answerSlotsRack');
      const tray = document.getElementById('scrambledTray');
      if (rack) rack.innerHTML = this.renderAnswerSlots();
      if (tray) tray.innerHTML = this.renderTrayTiles();
      this.attachEventListeners();
    }

    submitAnswer() {
      // Assemble placed answer
      const assembled = this.placedTiles.map(s => {
        if (!s) return '';
        return s.char;
      }).join('').toUpperCase().trim();

      const canonical = this.currentWord.canonical.toUpperCase().trim();
      const accepted = (this.currentWord.acceptedVariants || [canonical]).map(v => v.toUpperCase().trim());

      const isMatch = accepted.includes(assembled) || assembled === canonical;

      if (isMatch) {
        this.handleSuccess();
      } else {
        this.handleFailure();
      }
    }

    handleSuccess() {
      this.streak++;
      const basePoints = this.currentWord.difficulty === 'advanced' ? 80 : (this.currentWord.difficulty === 'intermediate' ? 50 : 30);
      const hintPenalty = this.hintsUsedInWord * 15;
      const earnedScore = Math.max(10, Math.round((basePoints - hintPenalty) * this.multiplier));
      this.score += earnedScore;

      // Time attack bonus
      if (this.currentMode === 'timed') {
        this.timeLeft += 10;
        const timeEl = document.getElementById('timeDial');
        if (timeEl) timeEl.textContent = `${this.timeLeft}s`;
      }

      if (window.GameAudio) window.GameAudio.playWordSolve();

      // Record in storage
      if (window.GameStorage) {
        window.GameStorage.recordScrambleResult(this.currentWord.id, this.currentMode, earnedScore, this.streak);
        window.GameStorage.recordVocabularyRecall(this.currentWord.id, true);
        window.GameStorage.addXP(earnedScore, `Solved ${this.currentWord.canonical} in Code Breaker`);
      }

      // Check achievements
      if (window.AchievementsEngine && window.GameStorage) {
        const state = window.GameStorage.getArenaState();
        window.AchievementsEngine.evaluate(state, {
          game: 'scramble',
          mode: this.currentMode,
          wordId: this.currentWord.id,
          streak: this.streak,
          score: this.score
        });
      }

      // Manuscript mode progression
      if (this.currentMode === 'manuscript') {
        this.manuscriptWordIndex++;
        if (this.manuscriptWordIndex >= 5) {
          this.completeManuscript();
          return;
        }
      }

      this.renderSuccessModal(earnedScore);
    }

    handleFailure() {
      if (window.GameAudio) window.GameAudio.playError();
      const rack = document.getElementById('answerSlotsRack');
      if (rack) {
        rack.style.borderColor = '#a63b49';
        rack.style.backgroundColor = '#fce8e6';
        setTimeout(() => {
          rack.style.borderColor = '#cbd5e1';
          rack.style.backgroundColor = '#f4f6f9';
        }, 600);
      }
      this.streak = 0;
      this.updateMultiplier();
      const commentary = document.getElementById('advisorCommentary');
      if (commentary) {
        commentary.textContent = "Not quite! Re-examine the clue and spelling. Use Shuffle or Undo to reorganize your letter tiles.";
      }
    }

    renderSuccessModal(earnedScore) {
      const mount = document.getElementById('scrambleFeedbackMount');
      if (!mount) return;

      mount.innerHTML = `
        <div class="card" style="margin-top:20px;border:2px solid #137d72;background:#edf7f4;padding:24px;border-radius:12px;box-shadow:0 8px 24px rgba(19,125,114,0.15);">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;flex-wrap:wrap;gap:8px;">
            <span class="badge" style="background:#137d72;color:#ffffff;font-size:12px;font-weight:bold;">CIPHER DECODED · CORRECT!</span>
            <span style="font-family:Georgia,serif;font-size:1.1rem;font-weight:bold;color:#137d72;">+${earnedScore} XP (${this.multiplier.toFixed(1)}x Combo)</span>
          </div>

          <h2 style="font-family:Georgia,serif;color:#142c46;margin:0 0 8px 0;">${this.currentWord.canonical}</h2>
          
          <div style="background:#ffffff;border:1px solid #cbe7e2;border-radius:8px;padding:14px;margin-bottom:16px;">
            <p style="color:#1c2e40;font-size:0.92rem;margin:0 0 8px 0;line-height:1.5;"><strong>Definition:</strong> ${this.currentWord.definition}</p>
            ${this.currentWord.educationalExample ? `<p style="color:#607387;font-size:0.88rem;margin:0 0 8px 0;line-height:1.4;"><em>Example:</em> ${this.currentWord.educationalExample}</p>` : ''}
            <small style="color:#137d72;font-weight:bold;">Statute / Authority: ${this.currentWord.statuteOrAuthority || 'Indian Jurisprudence'}</small>
          </div>

          <div style="display:flex;justify-content:flex-end;gap:12px;">
            <button class="btn primary" id="btnNextWord" style="background:#137d72;border-color:#137d72;padding:10px 24px;font-weight:bold;">
              ${this.currentMode === 'manuscript' ? `Next Codex Password (${this.manuscriptWordIndex + 1}/5) ➔` : 'Next Word Cipher ➔'}
            </button>
          </div>
        </div>
      `;

      document.getElementById('btnNextWord').addEventListener('click', () => {
        mount.innerHTML = '';
        if (this.currentMode === 'manuscript') {
          this.loadManuscriptWord();
        } else {
          this.loadNextWordForMode();
        }
      });
    }

    completeManuscript() {
      if (window.GameAudio) window.GameAudio.playManuscriptReveal();
      if (window.GameStorage) {
        window.GameStorage.recordManuscriptUnlocked(this.currentManuscript.id, this.currentManuscript.title);
        window.GameStorage.addXP(200, `Unlocked Manuscript: ${this.currentManuscript.title}`);
      }
      if (window.AchievementsEngine && window.GameStorage) {
        const state = window.GameStorage.getArenaState();
        window.AchievementsEngine.evaluate(state, {
          game: 'scramble',
          mode: 'manuscript',
          completed: true,
          manuscriptId: this.currentManuscript.id
        });
      }

      const container = document.getElementById('scrambleApp');
      if (!container) return;

      container.innerHTML = `
        <div class="card manuscript-container" style="max-width:760px;margin:32px auto;padding:40px;text-align:center;background:#fffdf7;border:3px double #dfbf80;box-shadow:0 16px 48px rgba(20,44,70,0.18);">
          <div style="font-size:48px;margin-bottom:8px;">📜</div>
          <span class="badge" style="background:#dfbf80;color:#142c46;font-weight:bold;margin-bottom:12px;">ILLUMINATED MANUSCRIPT UNLOCKED</span>
          <h1 style="font-family:Georgia,serif;color:#142c46;margin:0 0 4px 0;">${this.currentManuscript.title}</h1>
          <div style="color:#854d0e;font-size:1.05rem;font-style:italic;margin-bottom:20px;">"${this.currentManuscript.subtitle}"</div>

          <div style="background:#ffffff;border:2px solid #dfbf80;border-radius:10px;padding:24px;text-align:left;margin-bottom:24px;font-family:Georgia,serif;line-height:1.8;color:#1c2e40;">
            <p style="font-size:1.05rem;margin-bottom:16px;">${this.currentManuscript.codexExtract}</p>
            <hr style="border:none;border-top:1px dashed #dfbf80;margin:16px 0;">
            <p style="font-size:0.92rem;color:#607387;margin:0;"><strong>Jurisprudential Authority:</strong> ${this.currentManuscript.statutoryReference}</p>
          </div>

          <div style="display:flex;align-items:center;gap:16px;background:#edf7f4;border:1px solid #137d72;border-radius:8px;padding:16px;text-align:left;margin-bottom:28px;">
            <img src="assets/games/images/characters/crossword/kavita.svg" style="width:52px;height:52px;border-radius:50%;border:2px solid #137d72;" alt="Prof. Kavita Sharma">
            <div style="font-size:0.9rem;color:#1c2e40;line-height:1.45;">
              <strong style="color:#137d72;font-family:Georgia,serif;">Prof. Kavita Sharma (Legal Vocabulary Mentor):</strong>
              "Brilliant reconstruction, Candidate! You have decoded all five foundational statutory passwords. Understanding these doctrinal pillars transforms mechanical memorization into living judicial comprehension."
            </div>
          </div>

          <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">
            <button class="btn gold" id="btnAnotherManuscript" style="font-weight:bold;padding:12px 24px;">Unlock Another Codex ➔</button>
            <button class="btn secondary" id="btnReturnDashboard" style="padding:12px 24px;">Return to Code Breaker</button>
          </div>
        </div>
      `;

      document.getElementById('btnAnotherManuscript').addEventListener('click', () => {
        this.renderManuscriptSelector();
      });

      document.getElementById('btnReturnDashboard').addEventListener('click', () => {
        this.renderDashboard();
      });
    }

    startTimer() {
      this.stopTimer();
      this.timerInterval = setInterval(() => {
        this.timeLeft--;
        const timeEl = document.getElementById('timeDial');
        if (timeEl) timeEl.textContent = `${this.timeLeft}s`;

        if (this.timeLeft <= 0) {
          this.stopTimer();
          this.handleTimeUp();
        }
      }, 1000);
    }

    stopTimer() {
      if (this.timerInterval) {
        clearInterval(this.timerInterval);
        this.timerInterval = null;
      }
    }

    handleTimeUp() {
      if (window.GameAudio) window.GameAudio.playVictory();
      const container = document.getElementById('scrambleApp');
      if (!container) return;

      container.innerHTML = `
        <div class="card" style="max-width:640px;margin:32px auto;padding:36px;text-align:center;border:2px solid #a63b49;background:#ffffff;box-shadow:0 12px 36px rgba(166,59,73,0.12);">
          <div style="font-size:42px;margin-bottom:8px;">⏱</div>
          <span class="badge" style="background:#a63b49;color:#ffffff;margin-bottom:12px;">TIME EXPIRED · SPRINT COMPLETE</span>
          <h2 style="font-family:Georgia,serif;color:#142c46;margin:0 0 16px 0;">60-Second Rapid Cipher Results</h2>
          
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:24px;">
            <div style="background:#f4f6f9;padding:16px;border-radius:8px;">
              <small style="color:#607387;text-transform:uppercase;font-size:10px;">Final Score</small>
              <div style="font-family:Georgia,serif;font-size:1.8rem;font-weight:bold;color:#142c46;">${this.score}</div>
            </div>
            <div style="background:#edf7f4;padding:16px;border-radius:8px;">
              <small style="color:#137d72;text-transform:uppercase;font-size:10px;">Max Streak</small>
              <div style="font-family:Georgia,serif;font-size:1.8rem;font-weight:bold;color:#137d72;">${this.streak} 🔥</div>
            </div>
          </div>

          <div style="display:flex;gap:12px;justify-content:center;">
            <button class="btn primary" id="btnRestartTimed" style="padding:12px 24px;font-weight:bold;">Sprint Again ➔</button>
            <button class="btn secondary" id="btnReturnDashboardTime" style="padding:12px 24px;">Return to Menu</button>
          </div>
        </div>
      `;

      document.getElementById('btnRestartTimed').addEventListener('click', () => {
        this.startMode('timed');
      });

      document.getElementById('btnReturnDashboardTime').addEventListener('click', () => {
        this.renderDashboard();
      });
    }
  }

  window.WordScrambleUIController = WordScrambleUIController;
  document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('scrambleApp')) {
      new WordScrambleUIController();
    }
  });
})();
