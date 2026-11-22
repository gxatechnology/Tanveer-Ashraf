/**
 * SECTION SPRINT — RAPID STATUTORY RECALL ENGINE
 * Modes: Number to Title, Title to Number, Mixed Recall, Chapter Challenge, Weak Section Practice
 */
(function() {
  'use strict';

  let sprintState = {
    mode: 'number_to_title',
    timeLimit: 60, // 30, 60, 120, or 'untimed' (25 Qs)
    chapterId: 'all',
    questionsPool: [],
    currentQuestion: null,
    questionIndex: 0,
    score: 0,
    streak: 0,
    longestStreak: 0,
    correctCount: 0,
    wrongCount: 0,
    skippedCount: 0,
    timeRemaining: 60,
    timerInterval: null,
    questionStartTime: null,
    totalResponseTimes: [],
    isPaused: false,
    isCountingDown: false,
    answeredInCurrent: false,
    weakSectionsEncountered: []
  };

  function getSectionsPool(mode, chapterId) {
    let sections = (window.BNS_SECTIONS || []).filter(s => s && s.title && s.section);

    if (mode === 'weak') {
      const weakItems = window.GameStorage ? window.GameStorage.getWeakQueue(25) : [];
      const weakBNS = weakItems.filter(w => w.type === 'bns');
      if (weakBNS.length >= 4) {
        // Map weak items back to sections
        const weakIds = weakBNS.map(w => parseInt(w.id.replace('bns-', ''), 10));
        const matched = sections.filter(s => weakIds.includes(s.section));
        if (matched.length >= 4) return matched;
      }
    }

    if (chapterId && chapterId !== 'all') {
      const chNum = parseInt(chapterId, 10);
      const chFiltered = sections.filter(s => s.chapter === chNum);
      if (chFiltered.length >= 4) return chFiltered;
    }

    return sections;
  }

  function generateQuestion(pool, mode) {
    if (!pool || pool.length < 4) {
      pool = window.BNS_SECTIONS || [];
    }

    // Pick 1 random correct target section
    const correctSection = pool[Math.floor(Math.random() * pool.length)];

    // Pick 3 unique distractors from global sections
    const allSections = window.BNS_SECTIONS || [];
    const otherPool = allSections.filter(s => s.section !== correctSection.section);
    const distractors = window.GameEngine.shuffle(otherPool).slice(0, 3);

    const isNumToTitle = mode === 'number_to_title' || (mode === 'mixed' && Math.random() > 0.5);

    let promptText = '';
    let promptSub = '';
    let correctOptionText = '';
    let options = [];

    if (isNumToTitle) {
      promptText = `Section ${correctSection.section}`;
      promptSub = 'Identify the statutory heading for this BNS section:';
      correctOptionText = correctSection.title;
      options = [
        { label: correctSection.title, isCorrect: true, sectionNum: correctSection.section },
        { label: distractors[0].title, isCorrect: false, sectionNum: distractors[0].section },
        { label: distractors[1].title, isCorrect: false, sectionNum: distractors[1].section },
        { label: distractors[2].title, isCorrect: false, sectionNum: distractors[2].section }
      ];
    } else {
      promptText = `“${correctSection.title}”`;
      promptSub = 'Identify the BNS section number covering this subject:';
      correctOptionText = `Section ${correctSection.section}`;
      options = [
        { label: `Section ${correctSection.section}`, isCorrect: true, sectionNum: correctSection.section },
        { label: `Section ${distractors[0].section}`, isCorrect: false, sectionNum: distractors[0].section },
        { label: `Section ${distractors[1].section}`, isCorrect: false, sectionNum: distractors[1].section },
        { label: `Section ${distractors[2].section}`, isCorrect: false, sectionNum: distractors[2].section }
      ];
    }

    options = window.GameEngine.shuffle(options);

    return {
      sectionObj: correctSection,
      promptText: promptText,
      promptSub: promptSub,
      options: options,
      correctText: correctOptionText,
      chapter: correctSection.chapter
    };
  }

  function startSprint(mode = 'number_to_title', timeLimit = 60, chapterId = 'all') {
    clearInterval(sprintState.timerInterval);

    sprintState = {
      mode: mode,
      timeLimit: timeLimit,
      chapterId: chapterId,
      questionsPool: getSectionsPool(mode, chapterId),
      currentQuestion: null,
      questionIndex: 0,
      score: 0,
      streak: 0,
      longestStreak: 0,
      correctCount: 0,
      wrongCount: 0,
      skippedCount: 0,
      timeRemaining: timeLimit === 'untimed' ? 0 : parseInt(timeLimit, 10),
      timerInterval: null,
      questionStartTime: Date.now(),
      totalResponseTimes: [],
      isPaused: false,
      isCountingDown: true,
      answeredInCurrent: false,
      weakSectionsEncountered: []
    };

    renderPreGameCountdown();
  }

  function renderPreGameCountdown() {
    const area = document.getElementById('sprintQuestionArea');
    if (!area) return;

    let count = 3;
    area.innerHTML = `
      <div class="sprint-countdown-box">
        <div class="sprint-countdown-num" id="sprintCountDisplay">${count}</div>
        <p class="eyebrow" style="color:#dfbf80;letter-spacing:3px">GET READY FOR RAPID RECALL</p>
      </div>
    `;

    if (window.GameAudio) window.GameAudio.playTick();

    const interval = setInterval(() => {
      count--;
      const display = document.getElementById('sprintCountDisplay');
      if (count > 0) {
        if (display) display.textContent = count;
        if (window.GameAudio) window.GameAudio.playTick();
      } else {
        clearInterval(interval);
        if (display) display.textContent = 'GO!';
        if (window.GameAudio) window.GameAudio.playStreak(2);
        setTimeout(() => {
          sprintState.isCountingDown = false;
          nextQuestion();
          if (sprintState.timeLimit !== 'untimed') {
            startTimer();
          } else {
            updateHUD();
          }
        }, 500);
      }
    }, 900);
  }

  function startTimer() {
    clearInterval(sprintState.timerInterval);
    sprintState.timerInterval = setInterval(() => {
      if (!sprintState.isPaused) {
        sprintState.timeRemaining--;
        updateHUD();
        if (sprintState.timeRemaining <= 5 && sprintState.timeRemaining > 0) {
          if (window.GameAudio) window.GameAudio.playTick();
        }
        if (sprintState.timeRemaining <= 0) {
          clearInterval(sprintState.timerInterval);
          finishSprint();
        }
      }
    }, 1000);
    updateHUD();
  }

  function updateHUD() {
    const timerDisplay = document.getElementById('sprintTimer');
    const timerRing = document.getElementById('sprintTimerRing');
    const scoreDisplay = document.getElementById('sprintScore');
    const streakDisplay = document.getElementById('sprintStreak');
    const accuracyDisplay = document.getElementById('sprintAccuracy');

    if (timerDisplay) {
      if (sprintState.timeLimit === 'untimed') {
        timerDisplay.textContent = `Q ${sprintState.questionIndex} / 25`;
      } else {
        timerDisplay.textContent = `${sprintState.timeRemaining}s`;
      }
    }

    // Circular SVG ring progress
    if (timerRing && sprintState.timeLimit !== 'untimed') {
      const total = parseInt(sprintState.timeLimit, 10);
      const frac = Math.max(0, sprintState.timeRemaining / total);
      const circumference = 2 * Math.PI * 45; // r=45
      timerRing.style.strokeDashoffset = (1 - frac) * circumference;
    }

    if (scoreDisplay) scoreDisplay.textContent = sprintState.score;
    if (streakDisplay) {
      const mult = getMultiplier(sprintState.streak);
      streakDisplay.innerHTML = `${sprintState.streak} <small style="color:#dfbf80">(${mult}x)</small>`;
    }
    if (accuracyDisplay) {
      const total = sprintState.correctCount + sprintState.wrongCount;
      const acc = total > 0 ? Math.round((sprintState.correctCount / total) * 100) : 100;
      accuracyDisplay.textContent = `${acc}%`;
    }
  }

  function getMultiplier(streak) {
    if (streak >= 12) return 3.0;
    if (streak >= 8) return 2.5;
    if (streak >= 5) return 2.0;
    if (streak >= 3) return 1.5;
    return 1.0;
  }

  function nextQuestion() {
    if (sprintState.timeLimit === 'untimed' && sprintState.questionIndex >= 25) {
      finishSprint();
      return;
    }

    sprintState.questionIndex++;
    sprintState.answeredInCurrent = false;
    sprintState.questionStartTime = Date.now();
    sprintState.currentQuestion = generateQuestion(sprintState.questionsPool, sprintState.mode);

    renderQuestion();
    updateHUD();
  }

  function renderQuestion() {
    const area = document.getElementById('sprintQuestionArea');
    if (!area || !sprintState.currentQuestion) return;

    const q = sprintState.currentQuestion;
    const letters = ['A', 'B', 'C', 'D'];

    area.innerHTML = `
      <div class="sprint-card">
        <div class="sprint-meta">
          <span class="badge" style="background:#eee6d3;color:#74582a">BNS Chapter ${q.chapter}</span>
          <span class="caption muted">Question ${sprintState.questionIndex}</span>
        </div>
        <div class="sprint-prompt-sub">${window.GameEngine.esc(q.promptSub)}</div>
        <div class="sprint-prompt-main">${window.GameEngine.esc(q.promptText)}</div>
        
        <div class="sprint-options-grid" id="sprintOptionsGrid">
          ${q.options.map((opt, idx) => `
            <button type="button" class="sprint-opt-btn" data-opt-idx="${idx}">
              <span class="sprint-opt-letter">${letters[idx]}</span>
              <span class="sprint-opt-text">${window.GameEngine.esc(opt.label)}</span>
            </button>
          `).join('')}
        </div>

        <div class="sprint-actions-bar">
          <button type="button" class="btn mini ghost" id="sprintSkipBtn">Skip (Space)</button>
        </div>
      </div>
    `;

    // Bind option click
    area.querySelectorAll('[data-opt-idx]').forEach(btn => {
      const idx = parseInt(btn.dataset.optIdx, 10);
      btn.onclick = () => selectOption(idx);
    });

    const skipBtn = document.getElementById('sprintSkipBtn');
    if (skipBtn) skipBtn.onclick = skipQuestion;
  }

  function selectOption(idx) {
    if (sprintState.answeredInCurrent || sprintState.isPaused) return;
    sprintState.answeredInCurrent = true;

    const responseDuration = (Date.now() - sprintState.questionStartTime) / 1000;
    sprintState.totalResponseTimes.push(responseDuration);

    const q = sprintState.currentQuestion;
    const chosen = q.options[idx];
    const buttons = document.querySelectorAll('.sprint-opt-btn');

    if (chosen.isCorrect) {
      // CORRECT
      sprintState.correctCount++;
      sprintState.streak++;
      sprintState.longestStreak = Math.max(sprintState.longestStreak, sprintState.streak);

      const multiplier = getMultiplier(sprintState.streak);
      const points = Math.round(10 * multiplier);
      sprintState.score += points;

      if (buttons[idx]) buttons[idx].classList.add('correct-flash');
      if (window.GameAudio) {
        if (sprintState.streak > 1 && sprintState.streak % 3 === 0) {
          window.GameAudio.playStreak(sprintState.streak);
        } else {
          window.GameAudio.playMatch();
        }
      }

      // If item was previously weak, ease it
      if (window.GameStorage) {
        window.GameStorage.removeWeakItem('bns-' + q.sectionObj.section);
      }

      setTimeout(nextQuestion, 320);
    } else {
      // INCORRECT
      sprintState.wrongCount++;
      sprintState.streak = 0;

      if (buttons[idx]) buttons[idx].classList.add('wrong-flash');
      // Highlight the correct one
      q.options.forEach((opt, oIdx) => {
        if (opt.isCorrect && buttons[oIdx]) {
          buttons[oIdx].classList.add('correct-highlight');
        }
      });

      if (window.GameAudio) window.GameAudio.playMismatch();

      // Record mistake
      sprintState.weakSectionsEncountered.push(q.sectionObj);
      if (window.GameStorage) {
        window.GameStorage.recordWeakItem({
          id: 'bns-' + q.sectionObj.section,
          type: 'bns',
          prompt: `BNS Section ${q.sectionObj.section}`,
          answer: q.sectionObj.title
        });
      }

      setTimeout(nextQuestion, 750);
    }

    updateHUD();
  }

  function skipQuestion() {
    if (sprintState.answeredInCurrent || sprintState.isPaused) return;
    sprintState.skippedCount++;
    sprintState.streak = 0;
    nextQuestion();
  }

  function togglePause() {
    sprintState.isPaused = !sprintState.isPaused;
    const area = document.getElementById('sprintQuestionArea');
    if (area) {
      if (sprintState.isPaused) area.classList.add('paused-blur');
      else area.classList.remove('paused-blur');
    }

    if (sprintState.isPaused) {
      window.GameEngine.showModal({
        title: 'Section Sprint Paused',
        subtitle: 'Break in Testimony',
        contentHTML: '<p class="muted">Timer halted. Prepare your statutory memory.</p>',
        buttons: [
          {
            text: 'Resume Sprint',
            class: 'primary',
            onClick: () => togglePause()
          },
          {
            text: 'Restart Session',
            class: 'secondary',
            onClick: () => startSprint(sprintState.mode, sprintState.timeLimit, sprintState.chapterId)
          },
          {
            text: 'Return to Arena',
            class: 'ghost',
            onClick: () => location.href = 'brain-arena.html'
          }
        ]
      });
    }
  }

  function finishSprint() {
    clearInterval(sprintState.timerInterval);
    if (window.GameAudio) window.GameAudio.playVictory();

    const attempted = sprintState.correctCount + sprintState.wrongCount;
    const accuracy = attempted > 0 ? Math.round((sprintState.correctCount / attempted) * 100) : 0;
    const avgResponse = sprintState.totalResponseTimes.length > 0
      ? (sprintState.totalResponseTimes.reduce((a, b) => a + b, 0) / sprintState.totalResponseTimes.length).toFixed(1)
      : '0.0';

    // Calculate XP
    const xpEarned = Math.round((sprintState.score / 5) + (sprintState.longestStreak >= 5 ? 25 : 0) + (accuracy >= 85 ? 30 : 0));

    // Save record
    const resultRecord = {
      game: 'section-sprint',
      mode: sprintState.mode,
      timeLimit: sprintState.timeLimit,
      chapter: sprintState.chapterId,
      subject: 'bns',
      score: sprintState.score,
      xpEarned: xpEarned,
      attempted: attempted,
      correct: sprintState.correctCount,
      wrong: sprintState.wrongCount,
      skipped: sprintState.skippedCount,
      accuracy: accuracy,
      longestStreak: sprintState.longestStreak,
      avgResponseTime: avgResponse,
      duration: sprintState.timeLimit === 'untimed' ? 120 : parseInt(sprintState.timeLimit, 10),
      isVictory: sprintState.correctCount >= 5
    };

    window.GameStorage.recordGameResult(resultRecord);
    window.GameStorage.addXP(xpEarned, 'Completed Section Sprint');

    showCompletionModal(resultRecord);
  }

  function showCompletionModal(result) {
    const weakListHTML = sprintState.weakSectionsEncountered.length > 0
      ? `<div class="weak-recap-box">
          <h4>BNS Sections to Review in Library:</h4>
          <ul>
            ${sprintState.weakSectionsEncountered.slice(0, 4).map(s => `
              <li><strong>§ ${s.section}</strong>: ${window.GameEngine.esc(s.title)} <a href="bns.html?q=${encodeURIComponent(s.section)}" target="_blank" rel="noopener">Explore ↗</a></li>
            `).join('')}
          </ul>
         </div>`
      : `<p class="caption" style="color:#137d72">✓ Flawless sprint! No incorrect statutory sections recorded.</p>`;

    window.GameEngine.showModal({
      title: 'Sprint Complete — Judicial Reflexes Tested!',
      subtitle: 'Session Summary',
      contentHTML: `
        <div class="completion-metrics-grid">
          <div class="metric-card">
            <span class="metric-num">${result.score}</span>
            <small>Total Points</small>
          </div>
          <div class="metric-card">
            <span class="metric-num gold">+${result.xpEarned} XP</span>
            <small>Earned XP</small>
          </div>
          <div class="metric-card">
            <span class="metric-num">${result.accuracy}%</span>
            <small>Accuracy (${result.correct}/${result.attempted})</small>
          </div>
          <div class="metric-card">
            <span class="metric-num">${result.longestStreak}</span>
            <small>Best Streak</small>
          </div>
        </div>
        <p class="caption muted" style="margin-top:12px">Average Response: <b>${result.avgResponseTime}s</b> · Skipped: <b>${result.skipped}</b></p>
        ${weakListHTML}
      `,
      buttons: [
        {
          text: 'Sprint Again',
          class: 'primary',
          onClick: () => startSprint(sprintState.mode, sprintState.timeLimit, sprintState.chapterId)
        },
        {
          text: 'Return to Arena',
          class: 'secondary',
          onClick: () => location.href = 'brain-arena.html'
        }
      ]
    });
  }

  // Keyboard shortcut listener
  document.addEventListener('keydown', e => {
    if (sprintState.isCountingDown || sprintState.isPaused || sprintState.answeredInCurrent) return;

    const key = e.key.toUpperCase();
    if (key === 'A' || key === '1') {
      selectOption(0);
    } else if (key === 'B' || key === '2') {
      selectOption(1);
    } else if (key === 'C' || key === '3') {
      selectOption(2);
    } else if (key === 'D' || key === '4') {
      selectOption(3);
    } else if (e.code === 'Space') {
      e.preventDefault();
      skipQuestion();
    }
  });

  window.SectionSprint = {
    start: startSprint,
    skip: skipQuestion,
    togglePause: togglePause
  };
})();
