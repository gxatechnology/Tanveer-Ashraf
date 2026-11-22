/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Judicial Learning Academy — Interactive Practice Test Engine
 */

(function (global) {
  'use strict';

  const PracticeEngine = {
    currentQuestions: [],
    currentIndex: 0,
    userAnswers: {}, // { [qId]: selectedIndex }
    startTime: null,
    endTime: null,
    timerInterval: null,
    mode: 'learn', // 'learn'|'topic_test'|'chapter_test'|'subject_mock'|'pyq'|'mistakes'|'bookmarks'|'challenge'
    config: {
      subjectId: 'law-constitution',
      chapterId: null,
      topicId: null,
      limit: 0
    },

    init: function (containerEl, options) {
      if (!containerEl) return;
      PracticeEngine.container = containerEl;
      PracticeEngine.config = Object.assign({}, PracticeEngine.config, options);
      PracticeEngine.mode = options.mode || 'learn';
      PracticeEngine.currentIndex = 0;
      PracticeEngine.userAnswers = {};

      PracticeEngine.loadQuestions();
      PracticeEngine.startSession();
    },

    // ------------------------------------------------------------------------
    // QUESTION BANK SELECTION BY MODE
    // ------------------------------------------------------------------------
    loadQuestions: function () {
      const mode = PracticeEngine.mode;
      const { chapterId, topicId, limit, subjectId } = PracticeEngine.config;
      const targetSubjectId = subjectId || 'law-constitution';
      let pool = [];

      if (mode === 'pyq') {
        // Load historical PYQs for the target subject
        const pyqMappings = global.LearningEngine ? global.LearningEngine.getPYQsBySubject(targetSubjectId) : (global.CONSTITUTION_PYQ_MAPPING || []);
        const baseQuestions = global.PCSJ_QUESTIONS || [];
        const qMap = {};
        baseQuestions.forEach(q => { qMap[q.id] = q; });

        let filteredMappings = pyqMappings;
        if (topicId) {
          filteredMappings = filteredMappings.filter(p => p.topicId === topicId);
        } else if (chapterId) {
          filteredMappings = filteredMappings.filter(p => p.chapterId === chapterId);
        }

        pool = filteredMappings.map(p => {
          const baseQ = qMap[p.questionId] || {};
          const letters = ['A', 'B', 'C', 'D'];
          const ansIdx = letters.indexOf(p.answer || baseQ.answer || 'A');
          return {
            id: p.questionId,
            isPYQ: true,
            year: p.year,
            paper: p.paper,
            questionNumber: p.questionNumber,
            chapterId: p.chapterId,
            topicId: p.topicId,
            question: p.stem || baseQ.stem || '',
            options: baseQ.options || ['Option A', 'Option B', 'Option C', 'Option D'],
            answer: ansIdx > -1 ? ansIdx : 0,
            answerLetter: p.answer || baseQ.answer || 'A',
            explanation: p.rationale || 'Previous Year UP PCS-J examination question.',
            optionBreakdown: {
              A: 'Authentic UP PCS-J examination option.',
              B: 'Authentic UP PCS-J examination option.',
              C: 'Authentic UP PCS-J examination option.',
              D: 'Authentic UP PCS-J examination option.'
            },
            provision: 'UP PCS-J Historical Question',
            difficulty: 'Medium',
            learningObjective: 'Master actual examination pattern and historical UP PCS-J framing.'
          };
        });
      } else if (mode === 'mistakes') {
        // Load wrong questions from LearningStorage
        const wrongIds = global.LearningStorage ? global.LearningStorage.getAllWrongQuestionIds() : [];
        const allMCQs = global.LearningEngine ? global.LearningEngine.getMCQsBySubject(targetSubjectId) : (global.CONSTITUTION_MCQS || []);
        const mcqMap = {};
        allMCQs.forEach(m => { mcqMap[m.id] = m; });
        pool = wrongIds.map(id => mcqMap[id]).filter(Boolean);
      } else if (mode === 'bookmarks') {
        // Load bookmarked questions
        const bmkIds = global.LearningStorage ? global.LearningStorage.getBookmarks() : [];
        const allMCQs = global.LearningEngine ? global.LearningEngine.getMCQsBySubject(targetSubjectId) : (global.CONSTITUTION_MCQS || []);
        const mcqMap = {};
        allMCQs.forEach(m => { mcqMap[m.id] = m; });
        pool = bmkIds.map(id => mcqMap[id]).filter(Boolean);
      } else if (mode === 'challenge') {
        // Hard questions only
        const allMCQs = global.LearningEngine ? global.LearningEngine.getMCQsBySubject(targetSubjectId) : (global.CONSTITUTION_MCQS || []);
        pool = allMCQs.filter(m => m.difficulty === 'Hard');
      } else if (mode === 'subject_mock') {
        // Full subject randomized pool
        const allMCQs = (global.LearningEngine ? global.LearningEngine.getMCQsBySubject(targetSubjectId) : (global.CONSTITUTION_MCQS || [])).slice();
        // Shuffle
        pool = allMCQs.sort(() => Math.random() - 0.5);
      } else if (mode === 'chapter_test') {
        pool = global.LearningEngine ? global.LearningEngine.getMCQsByChapter(chapterId, targetSubjectId) : [];
      } else {
        // Learn or Topic Test
        if (topicId) {
          pool = global.LearningEngine ? global.LearningEngine.getMCQsByTopic(topicId, targetSubjectId) : [];
        } else if (chapterId) {
          pool = global.LearningEngine ? global.LearningEngine.getMCQsByChapter(chapterId, targetSubjectId) : [];
        } else {
          pool = global.LearningEngine ? global.LearningEngine.getMCQsBySubject(targetSubjectId) : [];
        }
      }

      if (limit && limit > 0) {
        pool = pool.slice(0, limit);
      }

      PracticeEngine.currentQuestions = pool;
    },

    // ------------------------------------------------------------------------
    // SESSION START & TIMER
    // ------------------------------------------------------------------------
    startSession: function () {
      PracticeEngine.startTime = Date.now();
      PracticeEngine.endTime = null;
      PracticeEngine.currentIndex = 0;
      PracticeEngine.userAnswers = {};

      if (PracticeEngine.currentQuestions.length === 0) {
        PracticeEngine.renderEmptyState();
        return;
      }

      PracticeEngine.renderHUD();
      PracticeEngine.renderCurrentQuestion();
    },

    renderEmptyState: function () {
      let msg = 'No questions available for this practice selection.';
      if (PracticeEngine.mode === 'mistakes') {
        msg = '🎉 Fantastic work! Your Weak Knowledge Queue is completely empty. No unresolved mistakes pending!';
      } else if (PracticeEngine.mode === 'bookmarks') {
        msg = 'You have not bookmarked any questions yet. Bookmark questions during practice to review them here.';
      }

      PracticeEngine.container.innerHTML = `
        <div class="practice-empty-card" style="text-align: center; padding: 50px 20px; background: #fff; border-radius: 8px; border: 1px solid #cdb17d; max-width: 600px; margin: 40px auto;">
          <div style="font-size: 36px; margin-bottom: 12px;">🏆</div>
          <h3 style="font-family: Georgia, serif; color: #142c46; margin: 0 0 10px;">Queue Clean &amp; Ready</h3>
          <p style="color: #607387; font-size: 14px; margin-bottom: 20px;">${msg}</p>
          <a href="learning-academy.html" class="btn btn-primary">Return to Academy</a>
        </div>
      `;
    },

    // ------------------------------------------------------------------------
    // HUD HEADER (PROGRESS, MODE, TIMER)
    // ------------------------------------------------------------------------
    renderHUD: function () {
      const modeLabels = {
        learn: 'Learn & Practise Mode',
        topic_test: 'Topic Assessment Test',
        chapter_test: 'Comprehensive Chapter Test',
        subject_mock: 'Full Subject Mock Test',
        pyq: 'Historical UP PCS-J PYQ Drill',
        mistakes: 'Spaced Repetition Mistake Queue',
        bookmarks: 'Bookmarked Revision Queue',
        challenge: 'Advanced Master Challenge'
      };

      const hudHtml = `
        <div class="practice-hud-card">
          <div class="hud-col-left">
            <span class="hud-mode-pill">${modeLabels[PracticeEngine.mode] || 'Practice'}</span>
            <span class="hud-count" id="hud-question-counter">Question 1 of ${PracticeEngine.currentQuestions.length}</span>
          </div>

          <div class="hud-col-center">
            <div class="hud-progress-bar">
              <div class="hud-progress-fill" id="hud-progress-fill" style="width: ${(1 / PracticeEngine.currentQuestions.length) * 100}%"></div>
            </div>
          </div>

          <div class="hud-col-right">
            <span class="hud-timer" id="hud-timer-display">⏱️ 00:00</span>
            <button class="btn btn-subtle btn-sm" id="btn-quit-test" title="End or leave session">✕ Exit</button>
          </div>
        </div>
        <div id="practice-question-mount"></div>
      `;

      PracticeEngine.container.innerHTML = hudHtml;

      // Start Timer
      if (PracticeEngine.timerInterval) clearInterval(PracticeEngine.timerInterval);
      PracticeEngine.timerInterval = setInterval(() => {
        const elapsedSec = Math.floor((Date.now() - PracticeEngine.startTime) / 1000);
        const mins = String(Math.floor(elapsedSec / 60)).padStart(2, '0');
        const secs = String(elapsedSec % 60).padStart(2, '0');
        const timerEl = document.getElementById('hud-timer-display');
        if (timerEl) timerEl.textContent = `⏱️ ${mins}:${secs}`;
      }, 1000);

      const quitBtn = PracticeEngine.container.querySelector('#btn-quit-test');
      if (quitBtn) {
        quitBtn.addEventListener('click', () => {
          if (confirm('Are you sure you want to exit this practice session? Your recorded attempts will be preserved.')) {
            if (PracticeEngine.timerInterval) clearInterval(PracticeEngine.timerInterval);
            window.location.href = 'learning-academy.html';
          }
        });
      }
    },

    // ------------------------------------------------------------------------
    // QUESTION RENDERER
    // ------------------------------------------------------------------------
    renderCurrentQuestion: function () {
      const mount = document.getElementById('practice-question-mount');
      if (!mount) return;

      const q = PracticeEngine.currentQuestions[PracticeEngine.currentIndex];
      const isAnswered = PracticeEngine.userAnswers[q.id] !== undefined;
      const selectedIdx = isAnswered ? PracticeEngine.userAnswers[q.id] : null;
      const isBookmarked = global.LearningStorage ? global.LearningStorage.isBookmarked(q.id) : false;
      const letters = ['A', 'B', 'C', 'D'];

      // Update HUD counter and progress
      const counterEl = document.getElementById('hud-question-counter');
      const fillEl = document.getElementById('hud-progress-fill');
      if (counterEl) counterEl.textContent = `Question ${PracticeEngine.currentIndex + 1} of ${PracticeEngine.currentQuestions.length}`;
      if (fillEl) fillEl.style.width = `${((PracticeEngine.currentIndex + 1) / PracticeEngine.currentQuestions.length) * 100}%`;

      const qHtml = `
        <div class="question-practice-card animate-fade-in" id="card-${q.id}">
          <div class="question-header">
            <div class="q-badge-cluster">
              <span class="badge badge-difficulty ${q.difficulty === 'Hard' ? 'badge-hard' : q.difficulty === 'Medium' ? 'badge-med' : 'badge-easy'}">
                ${q.difficulty || 'Medium'}
              </span>
              <span class="badge badge-prov">${q.provision || 'Constitution'}</span>
              ${q.isPYQ ? `<span class="badge badge-gold">📜 UP PCS-J ${q.year} (${q.paper}) Q.${q.questionNumber}</span>` : ''}
            </div>

            <div class="q-actions-cluster">
              <button class="btn-bmk ${isBookmarked ? 'is-active' : ''}" id="btn-bmk-${q.id}" title="Bookmark this question">
                ${isBookmarked ? '★ Bookmarked' : '☆ Bookmark'}
              </button>
            </div>
          </div>

          <div class="question-stem">
            <p>${q.question}</p>
          </div>

          <div class="question-options-stack">
            ${q.options.map((opt, idx) => {
              let optClass = 'option-choice-btn';
              if (isAnswered) {
                if (idx === q.answer) {
                  optClass += ' is-correct';
                } else if (idx === selectedIdx) {
                  optClass += ' is-wrong';
                } else {
                  optClass += ' is-disabled';
                }
              }

              return `
                <button class="${optClass}" data-opt-idx="${idx}" ${isAnswered ? 'disabled' : ''}>
                  <span class="opt-letter">${letters[idx]}</span>
                  <span class="opt-text">${opt}</span>
                </button>
              `;
            }).join('')}
          </div>

          <!-- Explanation Box (revealed in learn mode, or when answered) -->
          ${isAnswered ? PracticeEngine.buildExplanationHtml(q, selectedIdx) : ''}

          <!-- Footer Actions -->
          <div class="question-footer-nav">
            <button class="btn btn-outline btn-sm" id="btn-prev-q" ${PracticeEngine.currentIndex === 0 ? 'disabled' : ''}>
              &larr; Previous
            </button>

            <div class="q-footer-middle">
              ${isAnswered && q.topicId ? `
                <a href="subject-study.html?subject=${q.subjectId || PracticeEngine.config.subjectId || 'law-constitution'}&topic=${q.topicId}" target="_blank" class="btn btn-subtle btn-sm" title="Open complete academic concept note in new tab">
                  📖 Review Concept in Study Room &rarr;
                </a>
              ` : ''}
            </div>

            ${PracticeEngine.currentIndex < PracticeEngine.currentQuestions.length - 1 ? `
              <button class="btn btn-primary btn-sm" id="btn-next-q">
                Next &rarr;
              </button>
            ` : `
              <button class="btn btn-success btn-sm" id="btn-finish-test">
                Finish &amp; View Results
              </button>
            `}
          </div>
        </div>
      `;

      mount.innerHTML = qHtml;
      PracticeEngine.bindQuestionEvents(q);
    },

    // ------------------------------------------------------------------------
    // EXPLANATION & 4-OPTION BREAKDOWN BUILDER
    // ------------------------------------------------------------------------
    buildExplanationHtml: function (q, selectedIdx) {
      const isCorrect = selectedIdx === q.answer;
      const letters = ['A', 'B', 'C', 'D'];

      return `
        <div class="explanation-reveal-box ${isCorrect ? 'outcome-correct' : 'outcome-wrong'}">
          <div class="outcome-header">
            <span class="outcome-icon">${isCorrect ? '✓' : '✗'}</span>
            <h4 class="outcome-title">${isCorrect ? 'Correct Answer!' : 'Incorrect Answer'}</h4>
            <span class="correct-badge-pill">Correct Option: <strong>(${q.answerLetter || letters[q.answer]})</strong></span>
          </div>

          <div class="expl-master-text">
            <p><strong>Detailed Legal Explanation:</strong> ${q.explanation}</p>
          </div>

          ${q.optionBreakdown ? `
            <div class="breakdown-options-container">
              <h5 class="breakdown-title">Comprehensive Analysis of All 4 Options:</h5>
              <div class="breakdown-grid">
                ${letters.map((letter, idx) => `
                  <div class="breakdown-row ${idx === q.answer ? 'is-correct-row' : ''}">
                    <span class="breakdown-letter">(${letter})</span>
                    <span class="breakdown-text">${q.optionBreakdown[letter] || q.options[idx]}</span>
                  </div>
                `).join('')}
              </div>
            </div>
          ` : ''}

          ${q.learningObjective ? `
            <div class="learning-obj-box">
              <span class="obj-label">🎯 Learning Objective:</span>
              <span class="obj-text">${q.learningObjective}</span>
            </div>
          ` : ''}
        </div>
      `;
    },

    // ------------------------------------------------------------------------
    // EVENT BINDINGS FOR QUESTIONS
    // ------------------------------------------------------------------------
    bindQuestionEvents: function (q) {
      const mount = document.getElementById('practice-question-mount');
      if (!mount) return;

      // Option click handler
      const optBtns = mount.querySelectorAll('.option-choice-btn');
      optBtns.forEach(btn => {
        btn.addEventListener('click', function () {
          const chosenIdx = parseInt(this.dataset.optIdx, 10);
          PracticeEngine.handleAnswerSelect(q, chosenIdx);
        });
      });

      // Bookmark button
      const bmkBtn = mount.querySelector(`#btn-bmk-${q.id}`);
      if (bmkBtn && global.LearningStorage) {
        bmkBtn.addEventListener('click', function () {
          const isNowBookmarked = global.LearningStorage.toggleBookmark(q.id);
          this.textContent = isNowBookmarked ? '★ Bookmarked' : '☆ Bookmark';
          this.classList.toggle('is-active', isNowBookmarked);
        });
      }

      // Prev / Next / Finish buttons
      const prevBtn = mount.querySelector('#btn-prev-q');
      const nextBtn = mount.querySelector('#btn-next-q');
      const finishBtn = mount.querySelector('#btn-finish-test');

      if (prevBtn) {
        prevBtn.addEventListener('click', () => {
          if (PracticeEngine.currentIndex > 0) {
            PracticeEngine.currentIndex--;
            PracticeEngine.renderCurrentQuestion();
          }
        });
      }

      if (nextBtn) {
        nextBtn.addEventListener('click', () => {
          if (PracticeEngine.currentIndex < PracticeEngine.currentQuestions.length - 1) {
            PracticeEngine.currentIndex++;
            PracticeEngine.renderCurrentQuestion();
          }
        });
      }

      if (finishBtn) {
        finishBtn.addEventListener('click', () => {
          PracticeEngine.finishSession();
        });
      }
    },

    // ------------------------------------------------------------------------
    // ANSWER SELECTION HANDLER
    // ------------------------------------------------------------------------
    handleAnswerSelect: function (q, chosenIdx) {
      PracticeEngine.userAnswers[q.id] = chosenIdx;
      const isCorrect = chosenIdx === q.answer;

      // Persist attempt to LearningStorage
      if (global.LearningStorage) {
        global.LearningStorage.recordQuestionAttempt(q.id, isCorrect, {
          mode: PracticeEngine.mode,
          chapterId: q.chapterId,
          topicId: q.topicId
        });
      }

      // Re-render question to reveal explanation
      PracticeEngine.renderCurrentQuestion();
    },

    // ------------------------------------------------------------------------
    // FINISH SESSION & SCORECARD
    // ------------------------------------------------------------------------
    finishSession: function () {
      PracticeEngine.endTime = Date.now();
      if (PracticeEngine.timerInterval) clearInterval(PracticeEngine.timerInterval);

      const total = PracticeEngine.currentQuestions.length;
      let score = 0;
      const mistakes = [];

      PracticeEngine.currentQuestions.forEach(q => {
        const userChoice = PracticeEngine.userAnswers[q.id];
        if (userChoice === q.answer) {
          score++;
        } else {
          mistakes.push(q.id);
        }
      });

      const pct = total > 0 ? Math.round((score / total) * 100) : 0;
      const elapsedSec = Math.floor((PracticeEngine.endTime - PracticeEngine.startTime) / 1000);
      const mins = Math.floor(elapsedSec / 60);
      const secs = elapsedSec % 60;

      // Save test record to LearningStorage
      let testRecord = null;
      if (global.LearningStorage) {
        testRecord = global.LearningStorage.recordTestResult({
          type: PracticeEngine.mode,
          subjectId: PracticeEngine.config.subjectId || 'law-constitution',
          chapterId: PracticeEngine.config.chapterId,
          topicId: PracticeEngine.config.topicId,
          score: score,
          total: total,
          pct: pct,
          timeSpent: elapsedSec,
          mistakes: mistakes
        });
      }

      PracticeEngine.renderScorecard(score, total, pct, mins, secs, mistakes);
    },

    // ------------------------------------------------------------------------
    // SCORECARD VIEW
    // ------------------------------------------------------------------------
    renderScorecard: function (score, total, pct, mins, secs, mistakes) {
      let rating = 'Needs Thorough Revision';
      let ratingClass = 'badge-hard';
      if (pct >= 85) {
        rating = 'Outstanding Mastery!';
        ratingClass = 'badge-success';
      } else if (pct >= 70) {
        rating = 'Competitive Passing Zone';
        ratingClass = 'badge-med';
      }

      const scorecardHtml = `
        <div class="practice-scorecard-card animate-fade-in">
          <div class="scorecard-header">
            <span class="scorecard-trophy">${pct >= 70 ? '🏆' : '📚'}</span>
            <h2 class="scorecard-title">Practice Test Assessment Complete</h2>
            <span class="badge ${ratingClass} scorecard-badge">${rating}</span>
          </div>

          <div class="scorecard-metrics-grid">
            <div class="metric-card">
              <span class="metric-label">Final Score</span>
              <span class="metric-num">${score} / ${total}</span>
            </div>
            <div class="metric-card">
              <span class="metric-label">Accuracy</span>
              <span class="metric-num ${pct >= 70 ? 'text-success' : 'text-crimson'}">${pct}%</span>
            </div>
            <div class="metric-card">
              <span class="metric-label">Time Elapsed</span>
              <span class="metric-num">${mins}m ${secs}s</span>
            </div>
            <div class="metric-card">
              <span class="metric-label">Unresolved Errors</span>
              <span class="metric-num text-crimson">${mistakes.length}</span>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="scorecard-actions-row">
            <button class="btn btn-primary" id="btn-retake-session">
              🔄 Retake Test
            </button>
            ${mistakes.length ? `
              <a href="topic-practice.html?subject=${PracticeEngine.config.subjectId || 'law-constitution'}&mode=mistakes" class="btn btn-outline">
                ⚠️ Practise Missed Questions (${mistakes.length})
              </a>
            ` : ''}
            <a href="learning-academy.html" class="btn btn-subtle">
              🏛️ Academy Hub
            </a>
          </div>

          <!-- Question Review List -->
          <div class="scorecard-review-section">
            <h3 class="review-title">Question by Question Review</h3>
            <div class="review-list-stack">
              ${PracticeEngine.currentQuestions.map((q, idx) => {
                const userChoice = PracticeEngine.userAnswers[q.id];
                const isCorrect = userChoice === q.answer;
                const letters = ['A', 'B', 'C', 'D'];

                return `
                  <div class="review-item ${isCorrect ? 'review-correct' : 'review-wrong'}">
                    <div class="review-item-header">
                      <span class="review-num">Q.${idx+1}</span>
                      <span class="review-outcome">${isCorrect ? '✓ Correct' : '✗ Missed'}</span>
                      <span class="review-prov">${q.provision || ''}</span>
                    </div>
                    <p class="review-stem">${q.question}</p>
                    <div class="review-answers-row">
                      <span>Your Answer: <strong>${userChoice !== undefined ? `(${letters[userChoice]}) ${q.options[userChoice]}` : 'Unanswered'}</strong></span>
                      ${!isCorrect ? `<span class="review-correct-ans">Correct: <strong>(${letters[q.answer]}) ${q.options[q.answer]}</strong></span>` : ''}
                    </div>
                  </div>
                `;
              }).join('')}
            </div>
          </div>
        </div>
      `;

      PracticeEngine.container.innerHTML = scorecardHtml;

      const retakeBtn = PracticeEngine.container.querySelector('#btn-retake-session');
      if (retakeBtn) {
        retakeBtn.addEventListener('click', () => {
          PracticeEngine.startSession();
        });
      }
    }
  };

  global.PracticeEngine = PracticeEngine;

})(typeof window !== 'undefined' ? window : global);
