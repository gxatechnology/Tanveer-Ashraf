/**
 * Tanveer Ashraf Judicial Prep - Game 7: Legal Myth Buster Engine
 * Pure evaluation logic, scoring models, and state management for Chamber of Truth
 * Version 3.0 Phase 4
 * Author: Tauqeer Ashraf
 */

(function() {
  'use strict';

  class MythEngine {
    constructor(options = {}) {
      this.database = window.ARENA_MYTHS || [];
      this.byId = window.ARENA_MYTHS_BY_ID || {};
      this.bySubject = window.ARENA_MYTHS_BY_SUBJECT || {};
      this.modes = window.ARENA_MYTHS_MODES || [];

      this.currentMode = options.mode || 'classic';
      this.currentSubject = options.subject || 'all';
      this.currentDifficulty = options.difficulty || 'all';

      this.questions = [];
      this.currentIndex = 0;
      this.currentQuestion = null;

      this.score = 0;
      this.streak = 0;
      this.maxStreak = 0;
      this.correctAnswers = 0;
      this.totalAnswered = 0;

      // Confidence multiplier: 'low' (1x), 'medium' (1.5x), 'high' (2x)
      this.currentConfidence = 'medium';

      // Timed trial state
      this.timeRemaining = 0;
      this.timerInterval = null;
      this.isComplete = false;

      this.history = [];
    }

    /**
     * Initialize a gameplay session for a specific mode and filters
     */
    initSession(mode = 'classic', subject = 'all', count = 10) {
      this.currentMode = mode;
      this.currentSubject = subject;
      this.currentIndex = 0;
      this.score = 0;
      this.streak = 0;
      this.maxStreak = 0;
      this.correctAnswers = 0;
      this.totalAnswered = 0;
      this.isComplete = false;
      this.history = [];

      let pool = [...this.database];

      // Filter by subject if specified
      if (subject !== 'all' && this.bySubject[subject]) {
        const ids = new Set(this.bySubject[subject]);
        pool = pool.filter(q => ids.has(q.id));
      }

      // Mode-specific pool filtering
      if (mode === 'find_error' || mode === 'correct_law') {
        pool = pool.filter(q => q.classification === 'false' && q.errorPhrase && q.correction);
      } else if (mode === 'exception_hunter') {
        pool = pool.filter(q => q.classification === 'depends' || (q.exceptions && q.exceptions !== 'None.'));
      } else if (mode === 'old_vs_new') {
        pool = pool.filter(q => q.oldVsNew && q.oldVsNew.oldSection);
      } else if (mode === 'precedent_challenge') {
        pool = pool.filter(q => q.subject === 'Legal Maxims & Landmark Cases' || q.subject === 'Constitutional Law');
      } else if (mode === 'grand_trial') {
        count = 20;
      }

      // If pool is smaller than count, use entire pool
      if (pool.length === 0) pool = [...this.database];
      pool = this.shuffle(pool);
      this.questions = pool.slice(0, Math.min(count, pool.length));

      if (this.questions.length > 0) {
        this.currentQuestion = this.questions[0];
      }

      if (mode === 'grand_trial') {
        this.timeRemaining = 600; // 10 minutes for 20 questions
      }

      return {
        mode: this.currentMode,
        subject: this.currentSubject,
        totalQuestions: this.questions.length,
        firstQuestion: this.currentQuestion
      };
    }

    /**
     * Submit an answer for Classic, Precedent, or Confidence Challenge
     */
    evaluateVerdict(userVerdict) {
      if (!this.currentQuestion || this.isComplete) return null;

      const q = this.currentQuestion;
      const isCorrect = (userVerdict.toLowerCase() === q.classification.toLowerCase());

      // Base points
      let basePoints = isCorrect ? 10 : 0;
      let multiplier = 1.0;

      // Normal accuracy-based scoring for Confidence Challenge (no gambling / wagering penalties)
      const userConfidence = this.currentConfidence || 'medium';
      if (this.currentMode === 'confidence_challenge') {
        basePoints = isCorrect ? 15 : 0;
        multiplier = 1.0;
      }

      // Streak multiplier bonus in other modes
      if (isCorrect && this.currentMode !== 'confidence_challenge') {
        if (this.streak >= 5) multiplier = 1.5;
        else if (this.streak >= 3) multiplier = 1.25;
      }

      const pointsEarned = Math.round(basePoints * multiplier);
      this.score = Math.max(0, this.score + pointsEarned);

      if (isCorrect) {
        this.streak += 1;
        this.correctAnswers += 1;
        if (this.streak > this.maxStreak) this.maxStreak = this.streak;
      } else {
        this.streak = 0;
      }

      this.totalAnswered += 1;

      const record = {
        questionId: q.id,
        statement: q.statement,
        userVerdict,
        correctVerdict: q.classification,
        isCorrect,
        confidence: userConfidence,
        pointsEarned,
        currentScore: this.score,
        explanation: q.explanation,
        misconception: q.misconceptionExplanation,
        exceptions: q.exceptions,
        legislation: q.legislation,
        section: q.section,
        sourceUrl: q.sourceUrl
      };

      this.history.push(record);
      return record;
    }

    /**
     * Generate interactive phrase options for 'find_error' mode
     */
    getPhraseOptionsForQuestion() {
      if (!this.currentQuestion || !this.currentQuestion.errorPhrase) return [];
      const q = this.currentQuestion;
      const stmt = q.statement;
      const err = q.errorPhrase;

      // Extract 2-3 plausible distractor phrases from the statement
      const words = stmt.split(/\s+/);
      const distractors = [];

      // Create chunks of 4-7 words that do not overlap with the error phrase
      for (let i = 0; i < words.length - 4; i += 4) {
        const chunk = words.slice(i, i + 5).join(' ').replace(/[.,;:()]/g, '').trim();
        if (chunk.length > 10 && !chunk.includes(err) && !err.includes(chunk)) {
          distractors.push(chunk);
          if (distractors.length >= 3) break;
        }
      }

      // Fallback distractors if sentence is short
      if (distractors.length < 3) {
        distractors.push("without statutory backing");
        distractors.push("in all circumstances");
        distractors.push("under ordinary procedure");
      }

      const options = [err, ...distractors.slice(0, 3)];
      return this.shuffle(options);
    }

    /**
     * Evaluate selection in 'find_error' mode
     */
    evaluateErrorPhrase(selectedPhrase) {
      if (!this.currentQuestion) return null;
      const q = this.currentQuestion;
      const isCorrect = (selectedPhrase.trim().toLowerCase() === q.errorPhrase.trim().toLowerCase());

      const pointsEarned = isCorrect ? 15 : 0;
      this.score += pointsEarned;
      if (isCorrect) {
        this.streak += 1;
        this.correctAnswers += 1;
        if (this.streak > this.maxStreak) this.maxStreak = this.streak;
      } else {
        this.streak = 0;
      }
      this.totalAnswered += 1;

      const record = {
        questionId: q.id,
        statement: q.statement,
        selectedPhrase,
        correctPhrase: q.errorPhrase,
        isCorrect,
        pointsEarned,
        currentScore: this.score,
        correction: q.correction,
        explanation: q.explanation
      };
      this.history.push(record);
      return record;
    }

    /**
     * Generate multiple-choice correction options for 'correct_law' mode
     */
    getCorrectionOptionsForQuestion() {
      if (!this.currentQuestion || !this.currentQuestion.correction) return [];
      const q = this.currentQuestion;
      const correct = q.correction;

      // Pick 3 plausible distractors from other false questions
      const pool = this.database.filter(item => item.correction && item.id !== q.id);
      const shuffledPool = this.shuffle(pool);
      const distractors = shuffledPool.slice(0, 3).map(item => item.correction);

      return this.shuffle([correct, ...distractors]);
    }

    /**
     * Evaluate selection in 'correct_law' mode
     */
    evaluateCorrection(selectedCorrection) {
      if (!this.currentQuestion) return null;
      const q = this.currentQuestion;
      const isCorrect = (selectedCorrection.trim().toLowerCase() === q.correction.trim().toLowerCase());

      const pointsEarned = isCorrect ? 20 : 0;
      this.score += pointsEarned;
      if (isCorrect) {
        this.streak += 1;
        this.correctAnswers += 1;
        if (this.streak > this.maxStreak) this.maxStreak = this.streak;
      } else {
        this.streak = 0;
      }
      this.totalAnswered += 1;

      const record = {
        questionId: q.id,
        statement: q.statement,
        selectedCorrection,
        correctCorrection: q.correction,
        isCorrect,
        pointsEarned,
        currentScore: this.score,
        explanation: q.explanation,
        legislation: q.legislation,
        section: q.section
      };
      this.history.push(record);
      return record;
    }

    /**
     * Generate options for 'old_vs_new' mode
     */
    getOldVsNewOptions() {
      if (!this.currentQuestion || !this.currentQuestion.oldVsNew) return null;
      const q = this.currentQuestion;
      const mapping = q.oldVsNew;

      // Correct target is new section
      const correctSection = mapping.newSection;
      const distractorPool = this.database
        .filter(item => item.oldVsNew && item.oldVsNew.newSection && item.oldVsNew.newSection !== correctSection)
        .map(item => item.oldVsNew.newSection);

      const uniqueDistractors = [...new Set(distractorPool)];
      const distractors = this.shuffle(uniqueDistractors).slice(0, 3);

      return {
        oldAct: mapping.oldAct,
        oldSection: mapping.oldSection,
        substantiveChange: mapping.substantiveChange,
        options: this.shuffle([correctSection, ...distractors]),
        correctSection
      };
    }

    /**
     * Advance to the next question in the current session
     */
    nextQuestion() {
      this.currentIndex += 1;
      if (this.currentIndex < this.questions.length) {
        this.currentQuestion = this.questions[this.currentIndex];
        return { isComplete: false, question: this.currentQuestion, index: this.currentIndex };
      } else {
        this.isComplete = true;
        this.currentQuestion = null;
        return { isComplete: true, summary: this.getSessionSummary() };
      }
    }

    /**
     * Calculate comprehensive session summary and learning XP
     */
    getSessionSummary() {
      const accuracy = this.totalAnswered > 0 ? Math.round((this.correctAnswers / this.totalAnswered) * 100) : 0;
      
      // Calculate XP
      let xpEarned = Math.round(this.score * 1.5) + (this.maxStreak * 10);
      if (accuracy >= 90) xpEarned += 100;
      else if (accuracy >= 70) xpEarned += 50;

      // Evaluate Judicial Honor Title
      let title = "Judicial Candidate";
      if (accuracy >= 95 && this.score >= 150) title = "Grand Chancellor of Statutory Truth";
      else if (accuracy >= 85 && this.score >= 120) title = "Senior Judicial Arbiter";
      else if (accuracy >= 75) title = "Distinguished Legal Assessor";
      else if (accuracy >= 60) title = "Inquiring Jurisprudent";

      // Confidence Calibration Analysis
      const confStats = {
        high: { total: 0, correct: 0, accuracy: 0 },
        medium: { total: 0, correct: 0, accuracy: 0 },
        low: { total: 0, correct: 0, accuracy: 0 },
        dangerousMisconceptions: [],
        hesitantKnowledge: [],
        priorityRevisions: []
      };

      this.history.forEach(rec => {
        const c = rec.confidence || 'medium';
        if (confStats[c]) {
          confStats[c].total++;
          if (rec.isCorrect) confStats[c].correct++;
        }
        if (c === 'high' && !rec.isCorrect) {
          confStats.dangerousMisconceptions.push(rec);
          confStats.priorityRevisions.push({
            questionId: rec.questionId,
            statement: rec.statement,
            section: rec.section,
            reason: 'High-confidence statutory misconception'
          });
        }
        if (c === 'low' && rec.isCorrect) {
          confStats.hesitantKnowledge.push(rec);
        }
      });

      ['high', 'medium', 'low'].forEach(lvl => {
        confStats[lvl].accuracy = confStats[lvl].total > 0
          ? Math.round((confStats[lvl].correct / confStats[lvl].total) * 100)
          : 0;
      });

      return {
        mode: this.currentMode,
        subject: this.currentSubject,
        totalQuestions: this.questions.length,
        answered: this.totalAnswered,
        correct: this.correctAnswers,
        accuracy,
        score: this.score,
        maxStreak: this.maxStreak,
        xpEarned,
        title,
        confidenceCalibration: confStats,
        history: this.history
      };
    }

    shuffle(array) {
      const arr = [...array];
      for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
      }
      return arr;
    }
  }

  // Expose to window
  if (typeof window !== 'undefined') {
    window.MythEngine = MythEngine;
  }
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = MythEngine;
  }
})();
