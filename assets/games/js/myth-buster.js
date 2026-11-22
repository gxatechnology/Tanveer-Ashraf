/**
 * Tanveer Ashraf Judicial Prep - Game 7: Legal Myth Buster UI Controller
 * Version 3.0 Phase 4 - Chamber of Truth
 * Author: Tauqeer Ashraf
 */

(function() {
  'use strict';

  class MythBusterUI {
    constructor() {
      this.app = document.getElementById('mythBusterApp');
      if (!this.app) {
        console.error("MythBusterApp container not found.");
        return;
      }

      this.engine = new window.MythEngine();
      this.audio = window.GameAudio || { play: () => {}, toggleMute: () => false, isMuted: () => true };
    if (this.audio && typeof this.audio.play !== 'function') {
      this.audio.play = function(type) {
        if (typeof this.isMuted === 'function' && this.isMuted()) return;
        if ((type === 'success' || type === 'correct') && typeof this.playMatch === 'function') this.playMatch();
        else if ((type === 'error' || type === 'mismatch') && typeof this.playMismatch === 'function') this.playMismatch();
        else if (type === 'streak' && typeof this.playStreak === 'function') this.playStreak();
        else if (type === 'victory' && typeof this.playVictory === 'function') this.playVictory();
      };
    }
      this.storage = window.GameStorage || { addXP: () => 0, recordMissionCompletion: () => {} };

      // Parse URL parameters for direct mission integration
      const params = new URLSearchParams(window.location.search);
      this.missionId = params.get('missionId') || null;
      this.initialMode = params.get('mode') || 'classic';
      this.initialSubject = params.get('subject') || 'all';
      this.initialCount = parseInt(params.get('count') || '10', 10);

      this.currentFeedback = null;
      this.isAnsweringLocked = false;

      this.init();
    }

    init() {
      this.startSession(this.initialMode, this.initialSubject, this.initialCount);
    }

    startSession(mode = 'classic', subject = 'all', count = 10) {
      this.isAnsweringLocked = false;
      this.currentFeedback = null;
      this.sessionData = this.engine.initSession(mode, subject, count);
      this.render();
    }

    render() {
      if (this.engine.isComplete) {
        this.renderCompletionSummary();
        return;
      }

      const q = this.engine.currentQuestion;
      if (!q) {
        this.app.innerHTML = `<div class="myth-app"><p>No statements available for this selection.</p><button onclick="window.history.back()" class="btn-myth-next">Return</button></div>`;
        return;
      }

      const modeObj = this.engine.modes.find(m => m.id === this.engine.currentMode) || this.engine.modes[0];
      const progressPercent = Math.round(((this.engine.currentIndex + 1) / this.engine.questions.length) * 100);

      this.app.innerHTML = `
        <div class="myth-app">
          <!-- Header Hero -->
          <header class="myth-header">
            <div class="myth-header-top">
              <span class="myth-badge">Chamber of Truth • Game 7</span>
              <div style="display:flex; gap:0.5rem; align-items:center;">
                <a href="brain-arena.html" style="color:#e7c88c; text-decoration:none; font-size:0.9rem; font-weight:600;">← Brain Arena</a>
              </div>
            </div>
            <h1 class="myth-title">Legal Myth Buster</h1>
            <p class="myth-tagline">Question Everything. Discover the Law.</p>
          </header>

          <!-- Central Animated Scales of Justice -->
          <div class="scales-wrapper">
            <div class="scales-container" id="scalesContainer">
              <svg id="centralScales" class="scales-svg tilt-balanced" viewBox="0 0 100 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- Fulcrum & Pillar -->
                <path d="M50 15V65M42 65H58M45 15H55" stroke="#e7c88c" stroke-width="3" stroke-linecap="round"/>
                <!-- Central Beam -->
                <path d="M15 25L50 20L85 25" stroke="#cdb17d" stroke-width="3" stroke-linecap="round"/>
                <!-- Left Strings & Pan -->
                <path d="M15 25L8 45M15 25L22 45" stroke="#b98a38" stroke-width="1.5"/>
                <path d="M6 45C6 52 24 52 24 45H6Z" fill="#e7c88c" stroke="#b98a38" stroke-width="1.5"/>
                <!-- Right Strings & Pan -->
                <path d="M85 25L78 45M85 25L92 45" stroke="#b98a38" stroke-width="1.5"/>
                <path d="M76 45C76 52 94 52 94 45H76Z" fill="#e7c88c" stroke="#b98a38" stroke-width="1.5"/>
                <!-- Center Pivot Glow -->
                <circle cx="50" cy="20" r="4" fill="#ffffff" stroke="#e7c88c" stroke-width="2"/>
              </svg>
            </div>
            <span class="scales-status-label" id="scalesLabel">Scales of Judicial Truth: In Equipoise</span>
          </div>

          <!-- Mode & Subject Filter Header -->
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem; margin-bottom:1rem;">
            <div>
              <span style="font-weight:700; color:#142c46;">Mode:</span> 
              <span style="background:#edf7f4; color:#137d72; padding:0.25rem 0.6rem; border-radius:6px; font-weight:600; font-size:0.85rem;">${modeObj.icon} ${modeObj.name}</span>
            </div>
            <div style="display:flex; gap:0.5rem; align-items:center;">
              <label for="subjectSelect" style="font-size:0.85rem; font-weight:600; color:#607387;">Subject:</label>
              <select id="subjectSelect" style="padding:0.35rem 0.65rem; border-radius:6px; border:1px solid #cdb17d; font-size:0.85rem; background:#fff;">
                <option value="all" ${this.engine.currentSubject === 'all' ? 'selected' : ''}>All 12 Disciplines</option>
                ${(window.ARENA_MYTHS_SUBJECTS || []).map(s => `
                  <option value="${s}" ${this.engine.currentSubject === s ? 'selected' : ''}>${s}</option>
                `).join('')}
              </select>
            </div>
          </div>

          <!-- Stats & Progress Bar -->
          <div class="myth-stats-bar">
            <div class="stat-pill">
              Question: <strong>${this.engine.currentIndex + 1} / ${this.engine.questions.length}</strong>
            </div>
            <div class="stat-pill">
              Score: <strong>${this.engine.score} pts</strong>
            </div>
            <div class="stat-pill stat-streak">
              Streak: <strong>🔥 ${this.engine.streak}</strong>
            </div>
          </div>

          <!-- Progress track -->
          <div style="background:#e1e7ed; height:6px; border-radius:3px; margin-bottom:1.5rem; overflow:hidden;">
            <div style="background:linear-gradient(90deg, #137d72, #e7c88c); width:${progressPercent}%; height:100%; transition:width 0.3s ease;"></div>
          </div>

          <!-- Question Card -->
          <main class="myth-card">
            <div class="myth-card-meta">
              <span class="meta-subject">🏛️ ${q.subject}</span>
              <div style="display:flex; gap:0.5rem; align-items:center;">
                <span class="meta-difficulty diff-${q.difficulty}">${q.difficulty}</span>
                <span style="font-size:0.8rem; font-weight:600; color:#607387; background:#f4f3ef; padding:0.2rem 0.5rem; border-radius:4px;">${q.legislation} • ${q.section}</span>
              </div>
            </div>

            <!-- Statement Content -->
            <div class="myth-statement-box">
              "${q.statement}"
            </div>

            <!-- Mode-Specific Interactive Area -->
            <div id="interactiveArea">
              ${this.renderInteractiveControls(q)}
            </div>

            <!-- Feedback Area (rendered after answering) -->
            <div id="feedbackContainer">
              ${this.currentFeedback ? this.renderFeedbackHTML(this.currentFeedback) : ''}
            </div>
          </main>
        </div>
      `;

      this.bindEvents();
    }

    renderInteractiveControls(q) {
      const mode = this.engine.currentMode;

      // 1. Confidence Challenge Mode: Selector + Verdicts
      if (mode === 'confidence_challenge') {
        return `
          <div class="confidence-selector">
            <span class="confidence-label">Rate Your Learning Confidence:</span>
            <div class="confidence-btns">
              <button type="button" class="btn-conf ${this.engine.currentConfidence === 'low' ? 'active' : ''}" data-conf="low">Low Confidence</button>
              <button type="button" class="btn-conf ${this.engine.currentConfidence === 'medium' ? 'active' : ''}" data-conf="medium">Moderate Confidence</button>
              <button type="button" class="btn-conf ${this.engine.currentConfidence === 'high' ? 'active' : ''}" data-conf="high">High Confidence</button>
            </div>
            <small style="display:block; color:#607387; font-size:0.8rem; margin-top:0.4rem;">Calibrates knowledge certainty; high-confidence mistakes are highlighted for priority revision.</small>
          </div>
          ${this.renderVerdictButtons()}
        `;
      }

      // 2. Find the Legal Error Mode
      if (mode === 'find_error') {
        const phrases = this.engine.getPhraseOptionsForQuestion();
        return `
          <p style="font-weight:700; color:#142c46; margin-bottom:0.75rem;">Identify the exact erroneous phrase within the statement above:</p>
          <div class="phrase-options-list">
            ${phrases.map(phrase => `
              <button type="button" class="btn-phrase-choice" data-phrase="${this.escapeHtml(phrase)}" ${this.isAnsweringLocked ? 'disabled' : ''}>
                🔍 "${this.escapeHtml(phrase)}"
              </button>
            `).join('')}
          </div>
        `;
      }

      // 3. Correct the Law Mode
      if (mode === 'correct_law') {
        const corrections = this.engine.getCorrectionOptionsForQuestion();
        return `
          <p style="font-weight:700; color:#142c46; margin-bottom:0.75rem;">Select the authentic statutory correction to cure this misconception:</p>
          <div class="phrase-options-list">
            ${corrections.map(corr => `
              <button type="button" class="btn-phrase-choice" data-correction="${this.escapeHtml(corr)}" ${this.isAnsweringLocked ? 'disabled' : ''}>
                ✍️ "${this.escapeHtml(corr)}"
              </button>
            `).join('')}
          </div>
        `;
      }

      // 4. Old Law vs New Law Mode
      if (mode === 'old_vs_new') {
        const mapping = this.engine.getOldVsNewOptions();
        if (!mapping) return this.renderVerdictButtons();
        return `
          <div style="background:#f4f3ef; border:1px solid #cdb17d; border-radius:10px; padding:1.25rem; margin-bottom:1.25rem;">
            <p style="margin:0 0 0.5rem; font-weight:700; color:#142c46;">Statutory Transition: ${mapping.oldAct} Section ${mapping.oldSection}</p>
            <p style="margin:0; font-size:0.9rem; color:#607387;"><strong>Substantive Reform:</strong> ${mapping.substantiveChange}</p>
          </div>
          <p style="font-weight:700; color:#142c46; margin-bottom:0.75rem;">Select the corresponding section under Bharatiya Nyaya Sanhita, 2023:</p>
          <div class="phrase-options-list">
            ${mapping.options.map(sec => `
              <button type="button" class="btn-phrase-choice" data-transition="${this.escapeHtml(sec)}" ${this.isAnsweringLocked ? 'disabled' : ''}>
                ⚖️ Section ${this.escapeHtml(sec)}
              </button>
            `).join('')}
          </div>
        `;
      }

      // Default: Classic, Exception Hunter, Precedent, Grand Trial -> Verdict Buttons
      return this.renderVerdictButtons();
    }

    renderVerdictButtons() {
      return `
        <div class="verdict-actions-grid">
          <button type="button" class="btn-verdict btn-verdict-true" data-verdict="true" ${this.isAnsweringLocked ? 'disabled' : ''}>
            <span class="btn-verdict-icon">⚖️</span>
            <span>TRUE</span>
            <span class="btn-verdict-sub">Sound Legal Principle</span>
          </button>
          <button type="button" class="btn-verdict btn-verdict-false" data-verdict="false" ${this.isAnsweringLocked ? 'disabled' : ''}>
            <span class="btn-verdict-icon">🚫</span>
            <span>FALSE</span>
            <span class="btn-verdict-sub">Statutory Myth / Error</span>
          </button>
          <button type="button" class="btn-verdict btn-verdict-depends" data-verdict="depends" ${this.isAnsweringLocked ? 'disabled' : ''}>
            <span class="btn-verdict-icon">⚖️❓</span>
            <span>DEPENDS</span>
            <span class="btn-verdict-sub">Qualified / Conditional</span>
          </button>
        </div>
      `;
    }

    renderFeedbackHTML(fb) {
      const isCorrect = fb.isCorrect;
      const mentor = isCorrect ? 
        { name: "Prof. Aditi Menon", role: "Expert in Statutory Interpretation", avatar: "assets/games/images/characters/myth/aditi.svg", quote: "Exemplary legal discernment. Your statutory reasoning is sharp and grounded in authority." } :
        { name: "Adv. Siddharth Kapoor", role: "Fact-Checking Mentor", avatar: "assets/games/images/characters/myth/siddharth.svg", quote: "Careful scrutiny is required here. Common misconceptions frequently obscure explicit statutory language." };

      return `
        <div class="myth-feedback ${isCorrect ? 'correct-bg' : 'incorrect-bg'}">
          <div class="feedback-header">
            <span class="feedback-title">
              ${isCorrect ? '✓ Judicially Correct' : '✗ Statutory Misconception'}
            </span>
            <span class="feedback-points">${isCorrect ? '+' : ''}${fb.pointsEarned} pts</span>
          </div>

          <div class="feedback-content">
            <p><strong>Official Verdict:</strong> <span style="text-transform:uppercase; font-weight:700;">${fb.correctVerdict || (fb.isCorrect ? 'Accurate' : 'Misidentified')}</span></p>
            <p><strong>Statutory Analysis:</strong> ${fb.explanation}</p>

            ${fb.misconception ? `
              <div class="feedback-section">
                <span class="feedback-section-title">Common Trap / Misconception:</span>
                <p style="margin:0; font-size:0.9rem; color:#4a5568;">${fb.misconception}</p>
              </div>
            ` : ''}

            ${fb.exceptions ? `
              <div class="feedback-section">
                <span class="feedback-section-title">Exceptions & Qualifying Provisos:</span>
                <p style="margin:0; font-size:0.9rem; color:#4a5568;">${fb.exceptions}</p>
              </div>
            ` : ''}

            ${fb.legislation ? `
              <div class="feedback-section" style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem;">
                <div>
                  <span class="feedback-section-title">Authoritative Source:</span>
                  <div style="font-size:0.85rem; color:#2d3748;">${fb.legislation} • ${fb.section || ''}</div>
                </div>
                ${fb.sourceUrl ? `
                  <a href="${fb.sourceUrl}" target="_blank" rel="noopener noreferrer" class="authority-link">
                    Official India Code / eCourts Link ↗
                  </a>
                ` : ''}
              </div>
            ` : ''}
          </div>

          <!-- Judicial Mentor Dialogue -->
          <div class="mentor-bubble">
            <img src="${mentor.avatar}" alt="${mentor.name}" class="mentor-avatar" onerror="this.src='assets/images/emblem.svg'">
            <div class="mentor-dialogue">
              <div class="mentor-name">${mentor.name} <span style="font-size:0.75rem; font-weight:normal; color:#607387;">(${mentor.role})</span></div>
              <p class="mentor-text">"${mentor.quote}"</p>
            </div>
          </div>

          <!-- Next Button -->
          <div class="card-nav-actions">
            <button type="button" class="btn-myth-next" id="btnNextQuestion">
              Continue to Next Question →
            </button>
          </div>
        </div>
      `;
    }

    renderCompletionSummary() {
      const summary = this.engine.getSessionSummary();
      const scalesEl = document.getElementById('centralScales');

      // Record in storage
      if (this.storage.addXP) {
        this.storage.addXP(summary.xpEarned, `Completed Legal Myth Buster: ${summary.mode}`);
      }

      // Check mission completion
      if (this.missionId && this.storage.recordMissionCompletion) {
        this.storage.recordMissionCompletion(this.missionId, summary.score, summary.accuracy);
      }

      this.app.innerHTML = `
        <div class="myth-app">
          <div class="myth-summary-modal">
            <img src="assets/images/emblem.svg" alt="Court Emblem" class="summary-emblem">
            <h2 class="summary-title">Trial of Truth Concluded</h2>
            <div class="summary-honor">${summary.title}</div>
            <p style="color:#607387; font-size:0.95rem;">You have successfully examined the statutory propositions presented before the Chamber of Truth.</p>

            <div class="summary-stats-grid">
              <div class="summary-stat-box">
                <div class="summary-stat-val">${summary.score}</div>
                <div class="summary-stat-lbl">Final Score</div>
              </div>
              <div class="summary-stat-box">
                <div class="summary-stat-val">${summary.accuracy}%</div>
                <div class="summary-stat-lbl">Accuracy</div>
              </div>
              <div class="summary-stat-box">
                <div class="summary-stat-val">${summary.correct} / ${summary.totalQuestions}</div>
                <div class="summary-stat-lbl">Correct Verdicts</div>
              </div>
              <div class="summary-stat-box">
                <div class="summary-stat-val">+${summary.xpEarned}</div>
                <div class="summary-stat-lbl">Learning XP</div>
              </div>
            </div>

            <!-- Confidence Calibration Analysis (if Confidence Challenge) -->
            ${summary.mode === 'confidence_challenge' && summary.confidenceCalibration ? `
              <div class="confidence-calibration-card" style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:8px; padding:1.25rem; margin:1.5rem 0; text-align:left;">
                <h3 style="color:#142c46; font-size:1.05rem; margin:0 0 0.5rem;">📊 Confidence Calibration Report</h3>
                <p style="color:#607387; font-size:0.85rem; margin-bottom:0.75rem;">Analysis of knowledge certainty vs. statutory accuracy:</p>
                <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:0.5rem; text-align:center; margin-bottom:1rem;">
                  <div style="background:#fff; padding:0.6rem; border-radius:6px; border:1px solid #e2e8f0;">
                    <div style="font-size:0.75rem; color:#607387; font-weight:600;">High Confidence</div>
                    <strong style="color:${summary.confidenceCalibration.high.accuracy >= 80 ? '#137d72' : '#a63b49'}; font-size:1.1rem;">${summary.confidenceCalibration.high.accuracy}%</strong>
                    <div style="font-size:0.75rem; color:#94a3b8;">${summary.confidenceCalibration.high.correct} of ${summary.confidenceCalibration.high.total}</div>
                  </div>
                  <div style="background:#fff; padding:0.6rem; border-radius:6px; border:1px solid #e2e8f0;">
                    <div style="font-size:0.75rem; color:#607387; font-weight:600;">Moderate Confidence</div>
                    <strong style="color:#142c46; font-size:1.1rem;">${summary.confidenceCalibration.medium.accuracy}%</strong>
                    <div style="font-size:0.75rem; color:#94a3b8;">${summary.confidenceCalibration.medium.correct} of ${summary.confidenceCalibration.medium.total}</div>
                  </div>
                  <div style="background:#fff; padding:0.6rem; border-radius:6px; border:1px solid #e2e8f0;">
                    <div style="font-size:0.75rem; color:#607387; font-weight:600;">Low Confidence</div>
                    <strong style="color:#607387; font-size:1.1rem;">${summary.confidenceCalibration.low.accuracy}%</strong>
                    <div style="font-size:0.75rem; color:#94a3b8;">${summary.confidenceCalibration.low.correct} of ${summary.confidenceCalibration.low.total}</div>
                  </div>
                </div>

                ${summary.confidenceCalibration.dangerousMisconceptions.length > 0 ? `
                  <div style="background:#fef2f2; border:1px solid #fecaca; border-radius:6px; padding:0.85rem; margin-top:0.5rem;">
                    <strong style="color:#a63b49; font-size:0.85rem; display:block; margin-bottom:0.35rem;">⚠️ Priority Revision Items (High-Confidence Misconceptions):</strong>
                    <ul style="margin:0; padding-left:1.25rem; font-size:0.82rem; color:#7f1d1d; line-height:1.5;">
                      ${summary.confidenceCalibration.dangerousMisconceptions.map(m => `
                        <li><strong>${this.escapeHtml(m.section || m.legislation)}:</strong> ${this.escapeHtml(m.statement)}</li>
                      `).join('')}
                    </ul>
                  </div>
                ` : '<div style="color:#137d72; font-size:0.85rem; font-weight:600;">✓ Zero high-confidence misconceptions detected. Excellent statutory calibration!</div>'}
              </div>
            ` : ''}

            <!-- Review Actions -->
            <div style="display:flex; justify-content:center; gap:1rem; flex-wrap:wrap; margin-top:2rem;">
              <button type="button" class="btn-myth-next" id="btnRestartSession">Play Again in This Mode</button>
              <a href="brain-arena.html" class="btn-myth-next" style="background:#137d72; text-decoration:none;">Return to Brain Arena</a>
            </div>
          </div>
        </div>
      `;

      document.getElementById('btnRestartSession')?.addEventListener('click', () => {
        this.startSession(this.engine.currentMode, this.engine.currentSubject, this.engine.questions.length);
      });
    }

    bindEvents() {
      // Subject filter change
      const subjectSelect = document.getElementById('subjectSelect');
      if (subjectSelect) {
        subjectSelect.addEventListener('change', (e) => {
          this.startSession(this.engine.currentMode, e.target.value, this.engine.questions.length);
        });
      }

      // Confidence selector
      const confBtns = this.app.querySelectorAll('.btn-conf');
      confBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
          confBtns.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          this.engine.currentConfidence = btn.getAttribute('data-conf');
        });
      });

      // Verdict buttons
      const verdictBtns = this.app.querySelectorAll('.btn-verdict');
      verdictBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
          if (this.isAnsweringLocked) return;
          const verdict = btn.getAttribute('data-verdict');
          this.handleVerdictAnswer(verdict);
        });
      });

      // Find error phrase buttons
      const phraseBtns = this.app.querySelectorAll('.btn-phrase-choice[data-phrase]');
      phraseBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          if (this.isAnsweringLocked) return;
          const phrase = btn.getAttribute('data-phrase');
          this.handlePhraseAnswer(phrase);
        });
      });

      // Correct law buttons
      const corrBtns = this.app.querySelectorAll('.btn-phrase-choice[data-correction]');
      corrBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          if (this.isAnsweringLocked) return;
          const corr = btn.getAttribute('data-correction');
          this.handleCorrectionAnswer(corr);
        });
      });

      // Old vs new transition buttons
      const transBtns = this.app.querySelectorAll('.btn-phrase-choice[data-transition]');
      transBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          if (this.isAnsweringLocked) return;
          const targetSec = btn.getAttribute('data-transition');
          this.handleTransitionAnswer(targetSec);
        });
      });

      // Next question button
      const nextBtn = document.getElementById('btnNextQuestion');
      if (nextBtn) {
        nextBtn.addEventListener('click', () => {
          this.handleNextQuestion();
        });
      }
    }

    handleVerdictAnswer(verdict) {
      this.isAnsweringLocked = true;
      const result = this.engine.evaluateVerdict(verdict);
      this.currentFeedback = result;

      // Animate Scales of Truth
      this.animateScales(result.correctVerdict);

      // Play audio
      if (result.isCorrect) {
        this.audio.play('success');
      } else {
        this.audio.play('error');
      }

      this.updateFeedbackView();
    }

    handlePhraseAnswer(phrase) {
      this.isAnsweringLocked = true;
      const result = this.engine.evaluateErrorPhrase(phrase);
      this.currentFeedback = result;
      this.animateScales('false');

      if (result.isCorrect) {
        this.audio.play('success');
      } else {
        this.audio.play('error');
      }
      this.updateFeedbackView();
    }

    handleCorrectionAnswer(corr) {
      this.isAnsweringLocked = true;
      const result = this.engine.evaluateCorrection(corr);
      this.currentFeedback = result;
      this.animateScales('true');

      if (result.isCorrect) {
        this.audio.play('success');
      } else {
        this.audio.play('error');
      }
      this.updateFeedbackView();
    }

    handleTransitionAnswer(targetSec) {
      this.isAnsweringLocked = true;
      const q = this.engine.currentQuestion;
      const isCorrect = (targetSec === q.oldVsNew.newSection);
      const pointsEarned = isCorrect ? 15 : 0;
      this.engine.score += pointsEarned;
      if (isCorrect) {
        this.engine.streak += 1;
        this.engine.correctAnswers += 1;
      } else {
        this.engine.streak = 0;
      }
      this.engine.totalAnswered += 1;

      this.currentFeedback = {
        questionId: q.id,
        statement: q.statement,
        isCorrect,
        pointsEarned,
        explanation: `Under the 2024 reforms, the offence previously governed by ${q.oldVsNew.oldAct} Section ${q.oldVsNew.oldSection} is codified under Section ${q.oldVsNew.newSection} of the Bharatiya Nyaya Sanhita, 2023. ${q.oldVsNew.substantiveChange}`,
        legislation: q.legislation,
        section: q.oldVsNew.newSection
      };

      this.animateScales(isCorrect ? 'true' : 'false');
      if (isCorrect) this.audio.play('success');
      else this.audio.play('error');
      this.updateFeedbackView();
    }

    animateScales(verdict) {
      const scales = document.getElementById('centralScales');
      const label = document.getElementById('scalesLabel');
      if (!scales) return;

      scales.classList.remove('tilt-left', 'tilt-right', 'tilt-balanced');

      if (verdict === 'false') {
        scales.classList.add('tilt-left');
        if (label) label.textContent = "Scales Tilted Left: False / Statutory Myth Identified";
      } else if (verdict === 'true') {
        scales.classList.add('tilt-right');
        if (label) label.textContent = "Scales Tilted Right: Sound Legal Principle Upheld";
      } else {
        scales.classList.add('tilt-balanced');
        if (label) label.textContent = "Scales in Equipoise: Conditional / Qualified Exception";
      }
    }

    updateFeedbackView() {
      const fbContainer = document.getElementById('feedbackContainer');
      if (fbContainer) {
        fbContainer.innerHTML = this.renderFeedbackHTML(this.currentFeedback);
        document.getElementById('btnNextQuestion')?.addEventListener('click', () => {
          this.handleNextQuestion();
        });
      }

      // Disable interactive controls
      this.app.querySelectorAll('.btn-verdict, .btn-phrase-choice').forEach(b => {
        b.disabled = true;
      });
    }

    handleNextQuestion() {
      this.isAnsweringLocked = false;
      this.currentFeedback = null;
      const step = this.engine.nextQuestion();
      if (step.isComplete) {
        this.renderCompletionSummary();
      } else {
        this.render();
      }
    }

    escapeHtml(str) {
      if (!str) return '';
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
    }
  }

  // Auto-mount on load
  document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('mythBusterApp')) {
      window.mythBusterInstance = new MythBusterUI();
    }
  });

  if (typeof window !== 'undefined') {
    window.MythBusterUI = MythBusterUI;
  }
})();
