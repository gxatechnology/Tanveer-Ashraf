/**
 * LEGAL BRAIN ARENA — PERSISTENT STORAGE & LEARNER PROFILE ENGINE
 * Isolated Key: 'tanveer-arena-v1'
 * Preserves complete separation from parent PYQ and BNS storage keys.
 */
(function() {
  'use strict';

  const STORAGE_KEY = 'tanveer-arena-v1';

  const LEVELS = [
    { level: 1, title: 'Law Explorer', minXP: 0, maxXP: 499, badge: '⚖' },
    { level: 2, title: 'Legal Scholar', minXP: 500, maxXP: 1499, badge: '📜' },
    { level: 3, title: 'Section Master', minXP: 1500, maxXP: 2999, badge: '§' },
    { level: 4, title: 'Legal Strategist', minXP: 3000, maxXP: 4999, badge: '⚔' },
    { level: 5, title: 'Legal Expert', minXP: 5000, maxXP: 9999, badge: '🏛' },
    { level: 6, title: 'Judiciary Champion', minXP: 10000, maxXP: Infinity, badge: '👑' }
  ];

  function getTodayString() {
    const d = new Date();
    return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
  }

  function getDefaultDailyChallenge() {
    return {
      date: getTodayString(),
      title: 'Section Sprint: 60-Second Rapid Recall',
      description: 'Score at least 150 points in Section Sprint (60s mode)',
      game: 'section-sprint',
      targetScore: 150,
      rewardXP: 100,
      completed: false
    };
  }

  function getInitialState() {
    return {
      version: 1,
      xp: 0,
      level: 1,
      streak: {
        current: 0,
        best: 0,
        lastPlayedDate: null
      },
      gamesPlayed: 0,
      gamesWon: 0,
      totalAttempts: 0,
      totalCorrect: 0,
      history: [],
      personalBests: {
        memoryMatch: {}, // keyed by 'mode-difficulty'
        sectionSprint: {}, // keyed by 'mode-time'
        detective: {}, // keyed by caseId
        courtroom: {}, // keyed by caseId
        crossword: {}, // keyed by puzzleId
        scramble: {} // keyed by mode
      },
      detective: {
        completedCases: {}, // caseId -> { score, rubric, date, accuracy }
        activeCase: null
      },
      courtroom: {
        completedHearings: {}, // caseId -> { score, rubric, date, accuracy }
        activeHearing: null
      },
      crossword: {
        completedPuzzles: {}, // puzzleId -> { score, solvedWords, date, hintsUsed }
        activePuzzle: null
      },
      scramble: {
        completedWords: {}, // wordId -> { score, date }
        unlockedManuscripts: {}, // manuscriptId -> { unlockedDate, completedWords }
        activeSession: null
      },
      vocabularyMastery: {}, // vocabId -> { successCount, lastReviewed, nextReviewDue, easeFactor }
      subjectMastery: {
        bns: { correct: 0, attempted: 0 },
        constitution: { correct: 0, attempted: 0 },
        terms: { correct: 0, attempted: 0 },
        cases: { correct: 0, attempted: 0 }
      },
      weakQueue: [], // Array of { id, type, prompt, answer, errorCount, lastSeen }
      achievements: [], // Array of unlocked achievement IDs
      dailyChallenge: getDefaultDailyChallenge(),
      settings: {
        sound: false, // Muted by default per rules
        reducedMotion: false
      }
    };
  }

  function loadState() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return getInitialState();
      const parsed = JSON.parse(raw);
      const initial = getInitialState();
      // Safe merge to preserve schema
      const state = {
        ...initial,
        ...parsed,
        streak: { ...initial.streak, ...(parsed.streak || {}) },
        personalBests: { ...initial.personalBests, ...(parsed.personalBests || {}) },
        subjectMastery: { ...initial.subjectMastery, ...(parsed.subjectMastery || {}) },
        detective: { ...initial.detective, ...(parsed.detective || {}) },
        courtroom: { ...initial.courtroom, ...(parsed.courtroom || {}) },
        crossword: { ...initial.crossword, ...(parsed.crossword || {}) },
        scramble: { ...initial.scramble, ...(parsed.scramble || {}) },
        vocabularyMastery: { ...initial.vocabularyMastery, ...(parsed.vocabularyMastery || {}) },
        settings: { ...initial.settings, ...(parsed.settings || {}) }
      };

      // Reset daily challenge if date changed
      const today = getTodayString();
      if (!state.dailyChallenge || state.dailyChallenge.date !== today) {
        state.dailyChallenge = getDefaultDailyChallenge();
      }

      return state;
    } catch (e) {
      console.warn('Error reading arena storage:', e);
      return getInitialState();
    }
  }

  function saveState(state) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (e) {
      console.error('Failed to save arena storage:', e);
    }
  }

  function getLevelInfo(xp) {
    let current = LEVELS[0];
    for (let i = 0; i < LEVELS.length; i++) {
      if (xp >= LEVELS[i].minXP) {
        current = LEVELS[i];
      }
    }
    const nextLevel = LEVELS.find(l => l.level === current.level + 1) || null;
    const progressXP = xp - current.minXP;
    const neededXP = nextLevel ? nextLevel.minXP - current.minXP : 1;
    const percent = nextLevel ? Math.min(100, Math.round((progressXP / neededXP) * 100)) : 100;

    return {
      currentLevel: current.level,
      title: current.title,
      badge: current.badge,
      currentXP: xp,
      minXP: current.minXP,
      nextLevelMinXP: nextLevel ? nextLevel.minXP : current.minXP,
      neededForNext: nextLevel ? nextLevel.minXP - xp : 0,
      percent: percent,
      isMaxLevel: !nextLevel
    };
  }

  const GameStorage = {
    getArenaState: function() {
      return loadState();
    },

    saveArenaState: function(state) {
      saveState(state);
    },

    getLevels: function() {
      return LEVELS;
    },

    getLevelInfo: function(xp) {
      return getLevelInfo(xp);
    },

    addXP: function(amount, reason = '') {
      const state = loadState();
      const oldLevelInfo = getLevelInfo(state.xp);
      state.xp = Math.max(0, state.xp + amount);
      const newLevelInfo = getLevelInfo(state.xp);
      state.level = newLevelInfo.currentLevel;

      saveState(state);

      const leveledUp = newLevelInfo.currentLevel > oldLevelInfo.currentLevel;
      if (leveledUp && window.GameAudio) {
        window.GameAudio.playAchievement();
      }

      return {
        amountAdded: amount,
        totalXP: state.xp,
        oldLevel: oldLevelInfo,
        newLevel: newLevelInfo,
        leveledUp: leveledUp,
        reason: reason
      };
    },

    recordGameResult: function(result) {
      const state = loadState();
      state.gamesPlayed++;
      if (result.isVictory) state.gamesWon++;

      // Update total questions metrics
      state.totalAttempts += (result.attempted || result.pairsCount || 0);
      state.totalCorrect += (result.correct || result.pairsCount || 0);

      // Streak calculation
      const today = getTodayString();
      if (!state.streak.lastPlayedDate) {
        state.streak.current = 1;
      } else if (state.streak.lastPlayedDate === today) {
        // Already played today, maintain streak
      } else {
        const last = new Date(state.streak.lastPlayedDate);
        const curr = new Date(today);
        const diffDays = Math.round((curr - last) / (1000 * 60 * 60 * 24));
        if (diffDays === 1) {
          state.streak.current++;
        } else if (diffDays > 1) {
          state.streak.current = 1;
        }
      }
      state.streak.lastPlayedDate = today;
      state.streak.best = Math.max(state.streak.best, state.streak.current);

      // Subject mastery update
      if (result.subject && state.subjectMastery[result.subject]) {
        state.subjectMastery[result.subject].attempted += (result.attempted || result.pairsCount || 0);
        state.subjectMastery[result.subject].correct += (result.correct || result.pairsCount || 0);
      }

      // Add to history (capped at latest 50 games)
      const record = {
        id: 'arena-rec-' + Date.now() + '-' + Math.random().toString(36).substr(2, 5),
        game: result.game, // 'memory-match' | 'section-sprint'
        mode: result.mode,
        difficulty: result.difficulty || null,
        timeLimit: result.timeLimit || null,
        score: result.score || 0,
        xpEarned: result.xpEarned || 0,
        accuracy: result.accuracy || 0,
        duration: result.duration || 0,
        date: new Date().toISOString()
      };
      state.history.unshift(record);
      if (state.history.length > 50) state.history.pop();

      // Check personal best
      if (result.game === 'memory-match') {
        const key = `${result.mode}_${result.difficulty}`;
        const currentBest = state.personalBests.memoryMatch[key];
        if (!currentBest || result.moves < currentBest.moves || (result.moves === currentBest.moves && result.duration < currentBest.duration)) {
          state.personalBests.memoryMatch[key] = {
            moves: result.moves,
            duration: result.duration,
            score: result.score,
            date: today
          };
        }
      } else if (result.game === 'section-sprint') {
        const key = `${result.mode}_${result.timeLimit}`;
        const currentBest = state.personalBests.sectionSprint[key];
        if (!currentBest || result.score > currentBest.score) {
          state.personalBests.sectionSprint[key] = {
            score: result.score,
            streak: result.longestStreak || 0,
            accuracy: result.accuracy || 0,
            date: today
          };
        }
      } else if (result.game === 'legal-detective') {
        const key = result.caseId;
        const currentBest = state.personalBests.detective[key];
        if (!currentBest || result.score > currentBest.score) {
          state.personalBests.detective[key] = {
            score: result.score,
            rubric: result.rubric || null,
            date: today
          };
        }
        if (!state.detective.completedCases) state.detective.completedCases = {};
        state.detective.completedCases[key] = {
          score: result.score,
          rubric: result.rubric || null,
          date: today,
          title: result.title || key
        };
      } else if (result.game === 'courtroom') {
        const key = result.caseId;
        const currentBest = state.personalBests.courtroom[key];
        if (!currentBest || result.score > currentBest.score) {
          state.personalBests.courtroom[key] = {
            score: result.score,
            rubric: result.rubric || null,
            date: today
          };
        }
        if (!state.courtroom.completedHearings) state.courtroom.completedHearings = {};
        state.courtroom.completedHearings[key] = {
          score: result.score,
          rubric: result.rubric || null,
          date: today,
          title: result.title || key
        };
      }

      // Check daily challenge
      if (state.dailyChallenge && !state.dailyChallenge.completed) {
        if (state.dailyChallenge.game === result.game && (result.score >= state.dailyChallenge.targetScore)) {
          state.dailyChallenge.completed = true;
          state.xp += state.dailyChallenge.rewardXP;
          if (window.GameAudio) window.GameAudio.playAchievement();
        }
      }

            saveState(state);

      // Automatic campaign mission recording
      try {
        const uParams = (typeof window !== 'undefined' && window.location) ? new URLSearchParams(window.location.search) : null;
        const mId = (result && result.missionId) || (uParams && uParams.get('missionId'));
        if (mId) {
          GameStorage.recordMissionCompletion(mId, result.score || 100, result.accuracy || 100);
        }
      } catch (err) {}

      // Check achievements
      if (window.AchievementsEngine) {
        window.AchievementsEngine.evaluate(state, result);
      }

      return state;
    },

    recordWeakItem: function(item) {
      // item: { id, type: 'bns'|'term'|'article'|'case', prompt, answer }
      const state = loadState();
      const existing = state.weakQueue.find(w => w.id === item.id);
      if (existing) {
        existing.errorCount++;
        existing.lastSeen = Date.now();
      } else {
        state.weakQueue.push({
          id: item.id,
          type: item.type || 'bns',
          prompt: item.prompt,
          answer: item.answer,
          errorCount: 1,
          lastSeen: Date.now()
        });
      }
      // Keep max 100 weak items sorted by error count
      state.weakQueue.sort((a, b) => b.errorCount - a.errorCount);
      if (state.weakQueue.length > 100) state.weakQueue = state.weakQueue.slice(0, 100);
      saveState(state);
    },

    removeWeakItem: function(itemId) {
      const state = loadState();
      state.weakQueue = state.weakQueue.filter(w => w.id !== itemId);
      saveState(state);
    },

    getWeakQueue: function(limit = 20) {
      const state = loadState();
      return state.weakQueue.slice(0, limit);
    },

    saveDetectiveActive: function(activeData) {
      const state = loadState();
      state.detective.activeCase = activeData;
      saveState(state);
    },

    getDetectiveActive: function() {
      const state = loadState();
      return state.detective.activeCase || null;
    },

    clearDetectiveActive: function() {
      const state = loadState();
      state.detective.activeCase = null;
      saveState(state);
    },

    saveCourtroomActive: function(activeData) {
      const state = loadState();
      state.courtroom.activeHearing = activeData;
      saveState(state);
    },

    getCourtroomActive: function() {
      const state = loadState();
      return state.courtroom.activeHearing || null;
    },

    clearCourtroomActive: function() {
      const state = loadState();
      state.courtroom.activeHearing = null;
      saveState(state);
    },

    // === PHASE 3: CROSSWORD & SCRAMBLE PERSISTENCE ===
    saveCrosswordActive: function(activeData) {
      const state = loadState();
      state.crossword.activePuzzle = activeData;
      saveState(state);
    },

    getCrosswordActive: function() {
      const state = loadState();
      return state.crossword.activePuzzle || null;
    },

    clearCrosswordActive: function() {
      const state = loadState();
      state.crossword.activePuzzle = null;
      saveState(state);
    },

    recordCrosswordResult: function(puzzleId, score, solvedWords, totalWords, hintsUsed, elapsedSeconds) {
      const state = loadState();
      if (!state.crossword.completedPuzzles) state.crossword.completedPuzzles = {};
      
      const record = {
        puzzleId,
        score,
        solvedWords,
        totalWords,
        hintsUsed,
        elapsedSeconds,
        date: getTodayString()
      };
      state.crossword.completedPuzzles[puzzleId] = record;
      state.crossword.activePuzzle = null;

      // Update personal best
      const prevBest = state.personalBests.crossword[puzzleId] || 0;
      if (score > prevBest) {
        state.personalBests.crossword[puzzleId] = score;
      }

      // Add to session history
      state.history.unshift({
        game: 'crossword',
        label: `Crossword: ${puzzleId}`,
        score,
        accuracy: totalWords > 0 ? Math.round((solvedWords / totalWords) * 100) : 0,
        date: getTodayString()
      });
      if (state.history.length > 20) state.history.pop();

      state.gamesPlayed++;
      state.gamesWon++;
      saveState(state);
      return state;
    },

    saveScrambleActive: function(activeData) {
      const state = loadState();
      state.scramble.activeSession = activeData;
      saveState(state);
    },

    getScrambleActive: function() {
      const state = loadState();
      return state.scramble.activeSession || null;
    },

    clearScrambleActive: function() {
      const state = loadState();
      state.scramble.activeSession = null;
      saveState(state);
    },

    recordScrambleResult: function(wordId, mode, score, streak) {
      const state = loadState();
      if (!state.scramble.completedWords) state.scramble.completedWords = {};
      state.scramble.completedWords[wordId] = {
        score,
        mode,
        date: getTodayString()
      };

      const prevBest = state.personalBests.scramble[mode] || 0;
      if (score > prevBest) {
        state.personalBests.scramble[mode] = score;
      }

      saveState(state);
      return state;
    },

    recordManuscriptUnlocked: function(manuscriptId, chapterName) {
      const state = loadState();
      if (!state.scramble.unlockedManuscripts) state.scramble.unlockedManuscripts = {};
      state.scramble.unlockedManuscripts[manuscriptId] = {
        chapterName,
        unlockedDate: getTodayString()
      };
      saveState(state);
      return state;
    },

    /**
     * Spaced Repetition Mastery Tracker
     * Success increases interval; failure resets to 1 day.
     */
    recordVocabularyRecall: function(vocabId, isSuccess) {
      const state = loadState();
      if (!state.vocabularyMastery) state.vocabularyMastery = {};

      const current = state.vocabularyMastery[vocabId] || {
        successCount: 0,
        lastReviewed: null,
        nextReviewDue: getTodayString()
      };

      if (isSuccess) {
        current.successCount++;
      } else {
        current.successCount = 0; // reset on error
      }

      current.lastReviewed = getTodayString();
      if (window.VocabularyEngine) {
        current.nextReviewDue = window.VocabularyEngine.getNextReviewDate(current.successCount);
      }

      state.vocabularyMastery[vocabId] = current;
      saveState(state);
      return current;
    },

    getVocabularyDueForReview: function() {
      const state = loadState();
      const today = getTodayString();
      const due = [];
      const mastery = state.vocabularyMastery || {};

      for (let vid in mastery) {
        if (mastery[vid].nextReviewDue <= today) {
          due.push({ id: vid, ...mastery[vid] });
        }
      }
      return due;
    },

    
    recordMissionCompletion: function(missionId, score, accuracy) {
      if (!missionId) return;
      const state = loadState();
      state.journey = state.journey || { completedMissions: {}, unlockedChapters: ["ch-01"] };
      state.journey.completedMissions = state.journey.completedMissions || {};

      state.journey.completedMissions[missionId] = {
        completedAt: getTodayString(),
        score: score || 100,
        accuracy: accuracy !== undefined ? accuracy : 100
      };

      saveState(state);

      if (window.MissionEngine && window.MissionEngine.recordMissionOutcome) {
        window.MissionEngine.recordMissionOutcome(missionId, score, accuracy);
      }

      if (window.Achievements && window.Achievements.checkAchievements) {
        window.Achievements.checkAchievements();
      }
    },

    exportData: function() {
      const state = loadState();
      return JSON.stringify(state, null, 2);
    },

    importData: function(jsonString) {
      try {
        const parsed = JSON.parse(jsonString);
        if (typeof parsed !== 'object' || typeof parsed.xp !== 'number' || !Array.isArray(parsed.history)) {
          throw new Error('Invalid format');
        }
        saveState(parsed);
        return true;
      } catch (e) {
        return false;
      }
    },

    resetData: function() {
      saveState(getInitialState());
    }
  };

  window.GameStorage = GameStorage;
})();
