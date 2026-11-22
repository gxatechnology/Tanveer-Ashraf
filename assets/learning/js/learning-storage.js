/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Judicial Learning Academy — Persistent Storage Controller
 * Namespace: 'tanveer-learning-v1' | Schema: 3.1.0
 */

(function (global) {
  'use strict';

  const STORAGE_KEY = 'tanveer-learning-v1';
  const SCHEMA_VERSION = '3.1.0';

  const DEFAULT_STATE = {
    version: SCHEMA_VERSION,
    lastActive: new Date().toISOString(),
    completedTopics: {}, // { [topicId]: { readAt: ISO, mode: 'detailed'|'quick', readsCount: 1 } }
    bookmarkedQuestions: [], // [qId]
    wrongQuestions: {}, // { [qId]: { wrongCount: 1, correctCount: 0, lastWrongAt: ISO, resolved: false } }
    testHistory: [], // [ { id, date, type, subjectId, chapterId, topicId, score, total, pct, timeSpent, mistakes: [] } ]
    notes: {}, // { [topicId]: string }
    flashcards: {}, // { [cardId]: { status: 'mastered'|'review', lastReviewed: ISO } }
    stats: {
      testsTaken: 0,
      questionsAnswered: 0,
      questionsCorrect: 0,
      timeSpentSeconds: 0
    }
  };

  function getStore() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return JSON.parse(JSON.stringify(DEFAULT_STATE));
      const parsed = JSON.parse(raw);
      return Object.assign({}, DEFAULT_STATE, parsed);
    } catch (e) {
      console.error('[LearningStorage] Error loading store:', e);
      return JSON.parse(JSON.stringify(DEFAULT_STATE));
    }
  }

  function saveStore(store) {
    try {
      store.lastActive = new Date().toISOString();
      localStorage.setItem(STORAGE_KEY, JSON.stringify(store));
      return true;
    } catch (e) {
      console.error('[LearningStorage] Error saving store:', e);
      return false;
    }
  }

  const LearningStorage = {
    getKey: () => STORAGE_KEY,
    getVersion: () => SCHEMA_VERSION,

    // ------------------------------------------------------------------------
    // TOPIC READ STATE & PROGRESS
    // ------------------------------------------------------------------------
    markTopicRead: function (topicId, mode) {
      if (!topicId) return;
      const store = getStore();
      const existing = store.completedTopics[topicId] || { readsCount: 0 };
      store.completedTopics[topicId] = {
        readAt: new Date().toISOString(),
        mode: mode || 'detailed',
        readsCount: (existing.readsCount || 0) + 1
      };
      saveStore(store);
      return store.completedTopics[topicId];
    },

    unmarkTopicRead: function (topicId) {
      if (!topicId) return;
      const store = getStore();
      delete store.completedTopics[topicId];
      saveStore(store);
    },

    isTopicRead: function (topicId) {
      const store = getStore();
      return !!store.completedTopics[topicId];
    },

    getCompletedTopicCount: function (chapterId) {
      const store = getStore();
      const readTopicIds = Object.keys(store.completedTopics);
      if (!chapterId) return readTopicIds.length;
      return readTopicIds.filter(id => id.includes(chapterId.replace('ch-', ''))).length;
    },

    // ------------------------------------------------------------------------
    // QUESTION BOOKMARKS
    // ------------------------------------------------------------------------
    toggleBookmark: function (qId) {
      if (!qId) return false;
      const store = getStore();
      const idx = store.bookmarkedQuestions.indexOf(qId);
      let isBookmarked = false;
      if (idx > -1) {
        store.bookmarkedQuestions.splice(idx, 1);
        isBookmarked = false;
      } else {
        store.bookmarkedQuestions.push(qId);
        isBookmarked = true;
      }
      saveStore(store);
      return isBookmarked;
    },

    isBookmarked: function (qId) {
      const store = getStore();
      return store.bookmarkedQuestions.includes(qId);
    },

    getBookmarks: function () {
      const store = getStore();
      return store.bookmarkedQuestions || [];
    },

    // ------------------------------------------------------------------------
    // WRONG ANSWERS & SPACED REPETITION QUEUE
    // ------------------------------------------------------------------------
    recordQuestionAttempt: function (qId, isCorrect, metadata) {
      if (!qId) return;
      const store = getStore();
      store.stats.questionsAnswered = (store.stats.questionsAnswered || 0) + 1;
      if (isCorrect) {
        store.stats.questionsCorrect = (store.stats.questionsCorrect || 0) + 1;
        if (store.wrongQuestions[qId]) {
          store.wrongQuestions[qId].correctCount = (store.wrongQuestions[qId].correctCount || 0) + 1;
          // If answered correctly 2 consecutive times, mark resolved
          if (store.wrongQuestions[qId].correctCount >= 2) {
            store.wrongQuestions[qId].resolved = true;
          }
        }
      } else {
        const item = store.wrongQuestions[qId] || {
          wrongCount: 0,
          correctCount: 0,
          firstWrongAt: new Date().toISOString()
        };
        item.wrongCount = (item.wrongCount || 0) + 1;
        item.correctCount = 0; // reset streak
        item.lastWrongAt = new Date().toISOString();
        item.resolved = false;
        item.metadata = metadata || item.metadata || {};
        store.wrongQuestions[qId] = item;
      }
      saveStore(store);
    },

    getWrongQuestions: function () {
      const store = getStore();
      return Object.keys(store.wrongQuestions)
        .filter(qId => !store.wrongQuestions[qId].resolved)
        .map(qId => Object.assign({ id: qId }, store.wrongQuestions[qId]));
    },

    getAllWrongQuestionIds: function () {
      const store = getStore();
      return Object.keys(store.wrongQuestions).filter(qId => !store.wrongQuestions[qId].resolved);
    },

    resolveWrongQuestion: function (qId) {
      const store = getStore();
      if (store.wrongQuestions[qId]) {
        store.wrongQuestions[qId].resolved = true;
        saveStore(store);
      }
    },

    // ------------------------------------------------------------------------
    // TEST HISTORY & PERFORMANCE
    // ------------------------------------------------------------------------
    recordTestResult: function (testRecord) {
      const store = getStore();
      const record = Object.assign({
        id: 'test-' + Date.now(),
        date: new Date().toISOString(),
        type: 'practice',
        subjectId: 'law-constitution',
        score: 0,
        total: 0,
        pct: 0,
        timeSpent: 0,
        mistakes: []
      }, testRecord);

      store.testHistory.unshift(record);
      // Keep up to 200 past tests
      if (store.testHistory.length > 200) store.testHistory.pop();

      store.stats.testsTaken = (store.stats.testsTaken || 0) + 1;
      store.stats.timeSpentSeconds = (store.stats.timeSpentSeconds || 0) + (record.timeSpent || 0);

      // Record mistakes into wrongQuestions queue
      if (record.mistakes && record.mistakes.length) {
        record.mistakes.forEach(qId => {
          LearningStorage.recordQuestionAttempt(qId, false, {
            testId: record.id,
            testType: record.type,
            chapterId: record.chapterId,
            topicId: record.topicId
          });
        });
      }

      saveStore(store);
      return record;
    },

    getTestHistory: function (limit) {
      const store = getStore();
      return (store.testHistory || []).slice(0, limit || 50);
    },

    // ------------------------------------------------------------------------
    // COMPREHENSIVE SUBJECT PROGRESS
    // ------------------------------------------------------------------------
    getSubjectProgress: function (subjectId) {
      const store = getStore();
      const sId = subjectId || 'law-constitution';

      let topicPrefix = 'top-const-';
      let topics = global.CONSTITUTION_TOPICS || [];
      let mcqs = global.CONSTITUTION_MCQS || [];

      if (sId === 'law-jurisprudence') {
        topicPrefix = 'top-jur-';
        topics = global.JURISPRUDENCE_TOPICS || [];
        mcqs = global.JURISPRUDENCE_MCQS || [];
      } else if (sId === 'law-contract') {
        topicPrefix = 'top-cnt-';
        topics = global.CONTRACT_TOPICS || [];
        mcqs = global.CONTRACT_MCQS || [];
      } else if (sId === 'law-tpa') {
        topicPrefix = 'top-tpa-';
        topics = global.TPA_TOPICS || [];
        mcqs = global.TPA_MCQS || [];
      } else if (sId === 'law-criminal') {
        topicPrefix = 'top-crim-';
        topics = global.CRIMINAL_TOPICS || [];
        mcqs = global.CRIMINAL_MCQS || [];
      } else if (sId === 'law-crpc') {
        topicPrefix = 'top-crpc-';
        topics = global.CRPC_TOPICS || [];
        mcqs = global.CRPC_MCQS || [];
      } else if (sId === 'law-evidence') {
        topicPrefix = 'top-evi-';
        topics = global.EVIDENCE_TOPICS || [];
        mcqs = global.EVIDENCE_MCQS || [];
      } else if (sId === 'law-cpc') {
        topicPrefix = 'top-cpc-';
        topics = global.CPC_TOPICS || [];
        mcqs = global.CPC_MCQS || [];
      } else if (sId === 'soc-disabilities') {
        topicPrefix = 'top-disab-';
        topics = (global.SOCIAL_TOPICS || []).filter(t => t.subjectId === sId);
        mcqs = (global.SOCIAL_MCQS || []).filter(m => m.subjectId === sId);
      } else if (sId === 'soc-parents') {
        topicPrefix = 'top-parent-';
        topics = (global.SOCIAL_TOPICS || []).filter(t => t.subjectId === sId);
        mcqs = (global.SOCIAL_MCQS || []).filter(m => m.subjectId === sId);
      } else if (sId === 'soc-dowry') {
        topicPrefix = 'top-dowry-';
        topics = (global.SOCIAL_TOPICS || []).filter(t => t.subjectId === sId);
        mcqs = (global.SOCIAL_MCQS || []).filter(m => m.subjectId === sId);
      } else if (sId === 'soc-domestic-violence') {
        topicPrefix = 'top-dv-';
        topics = (global.SOCIAL_TOPICS || []).filter(t => t.subjectId === sId);
        mcqs = (global.SOCIAL_MCQS || []).filter(m => m.subjectId === sId);
      } else if (sId === 'soc-posh') {
        topicPrefix = 'top-posh-';
        topics = (global.SOCIAL_TOPICS || []).filter(t => t.subjectId === sId);
        mcqs = (global.SOCIAL_MCQS || []).filter(m => m.subjectId === sId);
      } else if (sId === 'soc-pcpndt') {
        topicPrefix = 'top-pcpndt-';
        topics = (global.SOCIAL_TOPICS || []).filter(t => t.subjectId === sId);
        mcqs = (global.SOCIAL_MCQS || []).filter(m => m.subjectId === sId);
      } else if (sId === 'soc-mtp') {
        topicPrefix = 'top-mtp-';
        topics = (global.SOCIAL_TOPICS || []).filter(t => t.subjectId === sId);
        mcqs = (global.SOCIAL_MCQS || []).filter(m => m.subjectId === sId);
      } else if (sId === 'soc-indecent-rep') {
        topicPrefix = 'top-irwa-';
        topics = (global.SOCIAL_TOPICS || []).filter(t => t.subjectId === sId);
        mcqs = (global.SOCIAL_MCQS || []).filter(m => m.subjectId === sId);
      } else if (sId === 'soc-pocso') {
        topicPrefix = 'top-pocso-';
        topics = (global.SOCIAL_TOPICS || []).filter(t => t.subjectId === sId);
        mcqs = (global.SOCIAL_MCQS || []).filter(m => m.subjectId === sId);
      }

      const totalTopics = topics.length || 1;
      const completedTopicKeys = Object.keys(store.completedTopics || {}).filter(id => id.startsWith(topicPrefix));
      const completedTopics = completedTopicKeys.length;
      const pctTopics = Math.round((completedTopics / totalTopics) * 100);

      const totalMCQs = mcqs.length || 1;
      
      const allWrong = LearningStorage.getAllWrongQuestionIds();
      const subjectWrong = allWrong.filter(qId => {
        if (topicPrefix === 'top-jur-') return qId.includes('-jur-') || qId.includes('jur');
        if (topicPrefix === 'top-cnt-') return qId.includes('-cnt-') || qId.includes('cnt');
        if (topicPrefix === 'top-tpa-') return qId.includes('-tpa-') || qId.includes('tpa');
        if (topicPrefix === 'top-crim-') return qId.includes('-crim-') || qId.includes('crim');
        if (topicPrefix === 'top-crpc-') return qId.includes('-crpc-') || qId.includes('crpc');
        if (topicPrefix === 'top-evi-') return qId.includes('-evi-') || qId.includes('evi');
        if (topicPrefix === 'top-cpc-') return qId.includes('-cpc-') || qId.includes('cpc');
        if (topicPrefix.startsWith('top-') && topicPrefix !== 'top-const-') {
          const short = topicPrefix.replace('top-', '').replace('-', '');
          return qId.includes(topicPrefix) || qId.includes(short);
        }
        return qId.includes('-const-') || qId.includes('const');
      });

      const allBookmarks = store.bookmarkedQuestions || [];
      const subjectBookmarks = allBookmarks.filter(qId => {
        if (topicPrefix === 'top-jur-') return qId.includes('-jur-') || qId.includes('jur');
        if (topicPrefix === 'top-cnt-') return qId.includes('-cnt-') || qId.includes('cnt');
        if (topicPrefix === 'top-tpa-') return qId.includes('-tpa-') || qId.includes('tpa');
        if (topicPrefix === 'top-crim-') return qId.includes('-crim-') || qId.includes('crim');
        if (topicPrefix === 'top-crpc-') return qId.includes('-crpc-') || qId.includes('crpc');
        if (topicPrefix === 'top-evi-') return qId.includes('-evi-') || qId.includes('evi');
        if (topicPrefix === 'top-cpc-') return qId.includes('-cpc-') || qId.includes('cpc');
        if (topicPrefix.startsWith('top-') && topicPrefix !== 'top-const-') {
          const short = topicPrefix.replace('top-', '').replace('-', '');
          return qId.includes(topicPrefix) || qId.includes(short);
        }
        return qId.includes('-const-') || qId.includes('const');
      });

      // Filter test history for this subject
      const subjectTests = (store.testHistory || []).filter(t => t.subjectId === sId);
      const subjectTestsTaken = subjectTests.length;
      let subjectAnswered = 0;
      let subjectCorrect = 0;
      let subjectTime = 0;
      subjectTests.forEach(t => {
        subjectAnswered += (t.total || 0);
        subjectCorrect += (t.score || 0);
        subjectTime += (t.timeSpent || 0);
      });

      return {
        subjectId: sId,
        totalTopics: totalTopics,
        completedTopics: completedTopics,
        topicPercentage: pctTopics,
        totalMCQs: totalMCQs,
        testsTaken: subjectTestsTaken || store.stats.testsTaken || 0,
        questionsAnswered: subjectAnswered || store.stats.questionsAnswered || 0,
        questionsCorrect: subjectCorrect || store.stats.questionsCorrect || 0,
        accuracyPct: subjectAnswered ? Math.round((subjectCorrect / subjectAnswered) * 100) : (store.stats.questionsAnswered ? Math.round((store.stats.questionsCorrect / store.stats.questionsAnswered) * 100) : 0),
        unresolvedMistakes: subjectWrong.length,
        bookmarksCount: subjectBookmarks.length,
        timeSpentSeconds: subjectTime || store.stats.timeSpentSeconds || 0
      };
    },

    // ------------------------------------------------------------------------
    // BACKUP & RESTORE INTEGRATION
    // ------------------------------------------------------------------------
    exportData: function () {
      return getStore();
    },

    importData: function (data) {
      if (!data || typeof data !== 'object') {
        throw new Error('Invalid learning storage data format.');
      }
      saveStore(data);
      return true;
    },

    clearProgress: function () {
      localStorage.removeItem(STORAGE_KEY);
      return true;
    }
  };

  global.LearningStorage = LearningStorage;

})(typeof window !== 'undefined' ? window : global);
