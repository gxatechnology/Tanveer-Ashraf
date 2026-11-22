/**
 * LEGAL MEMORY MATCH — ADVANCED COGNITIVE RECALL ENGINE
 * Modes: BNS Sections, Legal Maxims, Constitutional Articles, Landmark Cases, Mixed
 */
(function() {
  'use strict';

  const DIFFICULTIES = {
    beginner: { pairs: 4, name: 'Beginner', gridClass: 'grid-4-pairs', baseXP: 40 },
    easy: { pairs: 6, name: 'Easy', gridClass: 'grid-6-pairs', baseXP: 60 },
    intermediate: { pairs: 8, name: 'Intermediate', gridClass: 'grid-8-pairs', baseXP: 90 },
    advanced: { pairs: 12, name: 'Advanced', gridClass: 'grid-12-pairs', baseXP: 140 },
    expert: { pairs: 18, name: 'Expert', gridClass: 'grid-18-pairs', baseXP: 200 }
  };

  let gameState = {
    mode: 'bns',
    difficulty: 'intermediate',
    cards: [], // Array of card objects
    flippedCards: [],
    matchedPairs: 0,
    moves: 0,
    mismatches: 0,
    startTime: null,
    elapsedSeconds: 0,
    timerInterval: null,
    isLocked: false,
    isPaused: false,
    hintsUsed: 0,
    previewActive: false,
    wrongPairsTracked: [],
    sessionId: null
  };

  function getAvailableItems(mode) {
    if (mode === 'bns') {
      const bns = (window.BNS_SECTIONS || []).filter(s => s && s.title);
      return bns.map(s => ({
        id: 'bns-' + s.section,
        prompt: `BNS Section ${s.section}`,
        answer: s.title,
        type: 'bns',
        bnsSection: s.section,
        explanation: `Chapter ${(window.BNS_CHAPTERS && window.BNS_CHAPTERS[s.chapter - 1]) ? window.BNS_CHAPTERS[s.chapter - 1].title : s.chapter} of Bharatiya Nyaya Sanhita, 2023.`
      }));
    } else if (mode === 'terms') {
      const terms = (window.LEGAL_GAME_CONTENT && window.LEGAL_GAME_CONTENT.terms) || [];
      return terms.map(t => ({
        id: t.id,
        prompt: t.term,
        answer: t.definition,
        type: 'terms',
        explanation: t.explanation
      }));
    } else if (mode === 'constitution') {
      const arts = (window.LEGAL_GAME_CONTENT && window.LEGAL_GAME_CONTENT.articles) || [];
      return arts.map(a => ({
        id: a.id,
        prompt: a.article,
        answer: a.subject,
        type: 'constitution',
        explanation: a.explanation
      }));
    } else if (mode === 'cases') {
      const cases = (window.LEGAL_GAME_CONTENT && window.LEGAL_GAME_CONTENT.cases) || [];
      return cases.map(c => ({
        id: c.id,
        prompt: c.caseName,
        answer: c.principle,
        type: 'cases',
        explanation: c.explanation
      }));
    } else if (mode === 'mixed') {
      const bns = getAvailableItems('bns').slice(0, 30);
      const terms = getAvailableItems('terms');
      const arts = getAvailableItems('constitution');
      const cases = getAvailableItems('cases');
      return window.GameEngine.shuffle([...bns, ...terms, ...arts, ...cases]);
    }
    return [];
  }

  function initGame(mode = 'bns', diff = 'intermediate', preview = false) {
    clearInterval(gameState.timerInterval);

    const config = DIFFICULTIES[diff] || DIFFICULTIES.intermediate;
    const allItems = getAvailableItems(mode);
    const selectedItems = window.GameEngine.shuffle(allItems).slice(0, config.pairs);

    // Generate two cards per pair
    const cardDeck = [];
    selectedItems.forEach((item, idx) => {
      // Card 1: Question / Section / Maxim
      cardDeck.push({
        uid: `card-${idx}-prompt`,
        pairId: item.id,
        itemRef: item,
        role: 'prompt',
        label: item.prompt,
        category: item.type,
        isFlipped: false,
        isMatched: false
      });
      // Card 2: Meaning / Title / Principle
      cardDeck.push({
        uid: `card-${idx}-answer`,
        pairId: item.id,
        itemRef: item,
        role: 'answer',
        label: item.answer,
        category: item.type,
        isFlipped: false,
        isMatched: false
      });
    });

    gameState = {
      mode: mode,
      difficulty: diff,
      cards: window.GameEngine.shuffle(cardDeck),
      flippedCards: [],
      matchedPairs: 0,
      moves: 0,
      mismatches: 0,
      startTime: Date.now(),
      elapsedSeconds: 0,
      timerInterval: null,
      isLocked: false,
      isPaused: false,
      hintsUsed: 0,
      previewActive: preview,
      wrongPairsTracked: [],
      sessionId: 'mem-' + Date.now() + '-' + Math.random().toString(36).substr(2, 5)
    };

    renderBoard();

    if (preview) {
      // Show all cards for 3 seconds before starting countdown
      gameState.isLocked = true;
      gameState.cards.forEach(c => c.isFlipped = true);
      renderBoard();
      setTimeout(() => {
        gameState.cards.forEach(c => c.isFlipped = false);
        gameState.isLocked = false;
        gameState.previewActive = false;
        renderBoard();
        startTimer();
      }, 3000);
    } else {
      startTimer();
    }
  }

  function startTimer() {
    clearInterval(gameState.timerInterval);
    gameState.startTime = Date.now() - (gameState.elapsedSeconds * 1000);
    gameState.timerInterval = setInterval(() => {
      if (!gameState.isPaused && !gameState.previewActive) {
        gameState.elapsedSeconds = Math.floor((Date.now() - gameState.startTime) / 1000);
        updateHUD();
      }
    }, 1000);
    updateHUD();
  }

  function updateHUD() {
    const timerEl = document.getElementById('hudTimer');
    const movesEl = document.getElementById('hudMoves');
    const matchesEl = document.getElementById('hudMatches');
    const accuracyEl = document.getElementById('hudAccuracy');

    if (timerEl) timerEl.textContent = window.GameEngine.formatTime(gameState.elapsedSeconds);
    if (movesEl) movesEl.textContent = gameState.moves;
    if (matchesEl) {
      const config = DIFFICULTIES[gameState.difficulty];
      matchesEl.textContent = `${gameState.matchedPairs} / ${config.pairs}`;
    }
    if (accuracyEl) {
      const totalEvaluations = gameState.matchedPairs + gameState.mismatches;
      const acc = totalEvaluations > 0 ? Math.round((gameState.matchedPairs / totalEvaluations) * 100) : 100;
      accuracyEl.textContent = `${acc}%`;
    }
  }

  function renderBoard() {
    const boardEl = document.getElementById('memoryBoard');
    if (!boardEl) return;

    const config = DIFFICULTIES[gameState.difficulty];
    boardEl.className = `memory-board ${config.gridClass}`;

    boardEl.innerHTML = gameState.cards.map((card, idx) => `
      <div class="memory-card-wrap" data-card-idx="${idx}">
        <button type="button" class="memory-card ${card.isFlipped ? 'flipped' : ''} ${card.isMatched ? 'matched' : ''}" 
                aria-label="${card.isFlipped ? card.label : 'Hidden legal card ' + (idx + 1)}"
                ${card.isMatched || gameState.isLocked ? 'tabindex="-1"' : ''}>
          <div class="card-inner">
            <div class="card-back" aria-hidden="true">
              <div class="card-back-pattern"></div>
              <div class="card-back-emblem">
                <svg viewBox="0 0 100 100" width="34" height="34" fill="none" stroke="#e7c88c" stroke-width="3">
                  <path d="M50 15v70M30 30h40M30 30l-12 25h24L30 30zm40 0l-12 25h24L70 30zM40 85h20" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
              <span class="card-back-label">LEGAL ARENA</span>
            </div>
            <div class="card-front ${card.role}">
              <div class="card-category-badge">${card.role === 'prompt' ? 'PROVISION' : 'SUBJECT'}</div>
              <div class="card-text">${window.GameEngine.esc(card.label)}</div>
              ${card.isMatched ? '<div class="card-matched-check">✓</div>' : ''}
            </div>
          </div>
        </button>
      </div>
    `).join('');

    // Bind card clicks
    boardEl.querySelectorAll('[data-card-idx]').forEach(wrap => {
      const idx = parseInt(wrap.dataset.cardIdx, 10);
      const btn = wrap.querySelector('button');
      btn.onclick = () => onCardClick(idx);
    });

    updateHUD();
  }

  function onCardClick(idx) {
    if (gameState.isLocked || gameState.isPaused) return;

    const card = gameState.cards[idx];
    if (card.isFlipped || card.isMatched) return;

    // Flip this card
    card.isFlipped = true;
    gameState.flippedCards.push(card);

    if (window.GameAudio) window.GameAudio.playCardFlip();
    renderBoard();

    // Check if 2 cards are currently flipped
    if (gameState.flippedCards.length === 2) {
      gameState.moves++;
      gameState.isLocked = true;
      const [c1, c2] = gameState.flippedCards;

      if (c1.pairId === c2.pairId) {
        // MATCH!
        setTimeout(() => {
          c1.isMatched = true;
          c2.isMatched = true;
          gameState.matchedPairs++;
          gameState.flippedCards = [];
          gameState.isLocked = false;

          if (window.GameAudio) window.GameAudio.playMatch();
          renderBoard();

          // Show educational toast with deep-link
          window.GameEngine.showMatchExplanation(c1.itemRef);

          // Check if all pairs matched
          const config = DIFFICULTIES[gameState.difficulty];
          if (gameState.matchedPairs >= config.pairs) {
            handleVictory();
          }
        }, 350);
      } else {
        // MISMATCH!
        gameState.mismatches++;
        // Track mistake for Weak Knowledge Queue
        gameState.wrongPairsTracked.push(c1.itemRef);
        window.GameStorage.recordWeakItem({
          id: c1.itemRef.id,
          type: c1.itemRef.type,
          prompt: c1.itemRef.prompt,
          answer: c1.itemRef.answer
        });

        setTimeout(() => {
          if (window.GameAudio) window.GameAudio.playMismatch();
          // Shake cards
          const b1 = document.querySelector(`[data-card-idx="${gameState.cards.indexOf(c1)}"] .memory-card`);
          const b2 = document.querySelector(`[data-card-idx="${gameState.cards.indexOf(c2)}"] .memory-card`);
          if (b1) b1.classList.add('error-shake');
          if (b2) b2.classList.add('error-shake');

          setTimeout(() => {
            c1.isFlipped = false;
            c2.isFlipped = false;
            gameState.flippedCards = [];
            gameState.isLocked = false;
            renderBoard();
          }, 700);
        }, 500);
      }
    }
  }

  function useHint() {
    if (gameState.isLocked || gameState.isPaused) return;

    // Find first unmatched pair
    const unmatched = gameState.cards.filter(c => !c.isMatched);
    if (unmatched.length < 2) return;

    const targetPairId = unmatched[0].pairId;
    const pairCards = gameState.cards.filter(c => c.pairId === targetPairId);

    gameState.hintsUsed++;
    gameState.isLocked = true;

    // Temporarily flip both cards in the pair
    pairCards.forEach(c => c.isFlipped = true);
    if (window.GameAudio) window.GameAudio.playCardFlip();
    renderBoard();

    setTimeout(() => {
      // Revert if not already matched
      pairCards.forEach(c => {
        if (!c.isMatched) c.isFlipped = false;
      });
      gameState.isLocked = false;
      renderBoard();
    }, 1200);
  }

  function togglePause() {
    gameState.isPaused = !gameState.isPaused;
    const boardEl = document.getElementById('memoryBoard');
    if (boardEl) {
      if (gameState.isPaused) {
        boardEl.classList.add('paused-blur');
      } else {
        boardEl.classList.remove('paused-blur');
      }
    }

    if (gameState.isPaused) {
      window.GameEngine.showModal({
        title: 'Game Paused',
        subtitle: 'Court in Recess',
        contentHTML: '<p class="muted">Timer paused. Study your strategy before resuming.</p>',
        buttons: [
          {
            text: 'Resume Trial',
            class: 'primary',
            onClick: () => togglePause()
          },
          {
            text: 'Restart Session',
            class: 'secondary',
            onClick: () => initGame(gameState.mode, gameState.difficulty)
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

  function handleVictory() {
    clearInterval(gameState.timerInterval);
    if (window.GameAudio) window.GameAudio.playVictory();

    const config = DIFFICULTIES[gameState.difficulty];
    const totalEvals = gameState.matchedPairs + gameState.mismatches;
    const accuracy = totalEvals > 0 ? Math.round((gameState.matchedPairs / totalEvals) * 100) : 100;

    // Calculate score & XP
    const speedBonus = Math.max(0, 300 - (gameState.elapsedSeconds * 2));
    const hintPenalty = gameState.hintsUsed * 35;
    const finalScore = Math.max(50, (config.pairs * 100) + speedBonus + (accuracy * 2) - hintPenalty);
    const xpEarned = Math.round(config.baseXP + (accuracy > 80 ? 30 : 10) + Math.min(40, Math.floor(speedBonus / 8)));

    // Record result in storage
    const resultRecord = {
      game: 'memory-match',
      mode: gameState.mode,
      difficulty: gameState.difficulty,
      subject: gameState.mode === 'bns' ? 'bns' : gameState.mode === 'constitution' ? 'constitution' : gameState.mode === 'terms' ? 'terms' : 'cases',
      pairsCount: config.pairs,
      moves: gameState.moves,
      duration: gameState.elapsedSeconds,
      accuracy: accuracy,
      hintsUsed: gameState.hintsUsed,
      score: finalScore,
      xpEarned: xpEarned,
      isVictory: true
    };

    window.GameStorage.recordGameResult(resultRecord);
    window.GameStorage.addXP(xpEarned, `Completed Memory Match (${config.name})`);

    // Render completion dialogue
    setTimeout(() => {
      showCompletionModal(resultRecord);
    }, 400);
  }

  function showCompletionModal(result) {
    const config = DIFFICULTIES[gameState.difficulty];
    const weakListHTML = gameState.wrongPairsTracked.length > 0
      ? `<div class="weak-recap-box">
          <h4>Items for Quick Revision:</h4>
          <ul>
            ${gameState.wrongPairsTracked.slice(0, 4).map(w => `
              <li><strong>${window.GameEngine.esc(w.prompt)}</strong> — ${window.GameEngine.esc(w.answer)}</li>
            `).join('')}
          </ul>
         </div>`
      : `<p class="caption" style="color:#137d72">✓ Flawless memory! Zero mismatches recorded during this trial.</p>`;

    window.GameEngine.showModal({
      title: 'Trial Concluded — Outstanding Recall!',
      subtitle: 'Cognitive Victory',
      contentHTML: `
        <div class="completion-metrics-grid">
          <div class="metric-card">
            <span class="metric-num">${result.score}</span>
            <small>Game Score</small>
          </div>
          <div class="metric-card">
            <span class="metric-num gold">+${result.xpEarned} XP</span>
            <small>Earned XP</small>
          </div>
          <div class="metric-card">
            <span class="metric-num">${result.accuracy}%</span>
            <small>Accuracy</small>
          </div>
          <div class="metric-card">
            <span class="metric-num">${window.GameEngine.formatTime(result.duration)}</span>
            <small>Time Taken</small>
          </div>
        </div>
        <p class="caption muted" style="margin-top:12px">Total Moves: <b>${result.moves}</b> · Hints Used: <b>${result.hintsUsed}</b> · Difficulty: <b>${config.name}</b></p>
        ${weakListHTML}
      `,
      buttons: [
        {
          text: 'Play Again',
          class: 'primary',
          onClick: () => initGame(gameState.mode, gameState.difficulty)
        },
        {
          text: 'Return to Arena',
          class: 'secondary',
          onClick: () => location.href = 'brain-arena.html'
        }
      ]
    });
  }

  window.MemoryMatch = {
    init: initGame,
    hint: useHint,
    togglePause: togglePause
  };
})();
