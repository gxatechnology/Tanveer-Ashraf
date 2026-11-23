/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Judicial Learning Academy — Academy Engine & Subject Controller
 */

(function (global) {
  'use strict';

  const LearningEngine = {
    // ------------------------------------------------------------------------
    // DATA RETRIEVAL HELPERS
    // ------------------------------------------------------------------------
    getAllSubjects: function () {
      if (Array.isArray(global.ACADEMY_SUBJECTS)) return global.ACADEMY_SUBJECTS;
      if (global.JUDICIAL_SUBJECTS && Array.isArray(global.JUDICIAL_SUBJECTS.subjects)) return global.JUDICIAL_SUBJECTS.subjects;
      return [];
    },

    getSubjectById: function (subjectId) {
      const subjects = LearningEngine.getAllSubjects();
      return subjects.find(s => s.id === subjectId) || null;
    },

    getChaptersBySubject: function (subjectId) {
      if (!subjectId || subjectId === 'law-constitution') {
        if (Array.isArray(global.CONSTITUTION_CHAPTERS)) return global.CONSTITUTION_CHAPTERS;
        if (global.CONSTITUTION_CHAPTERS && Array.isArray(global.CONSTITUTION_CHAPTERS.chapters)) return global.CONSTITUTION_CHAPTERS.chapters;
        return [];
      }
      if (subjectId === 'law-jurisprudence') {
        if (Array.isArray(global.JURISPRUDENCE_CHAPTERS)) return global.JURISPRUDENCE_CHAPTERS;
        if (global.JURISPRUDENCE_CHAPTERS && Array.isArray(global.JURISPRUDENCE_CHAPTERS.chapters)) return global.JURISPRUDENCE_CHAPTERS.chapters;
        return [];
      }
      if (subjectId === 'law-contract') {
        if (Array.isArray(global.CONTRACT_CHAPTERS)) return global.CONTRACT_CHAPTERS;
        if (global.CONTRACT_CHAPTERS && Array.isArray(global.CONTRACT_CHAPTERS.chapters)) return global.CONTRACT_CHAPTERS.chapters;
        return [];
      }
      if (subjectId === 'law-tpa') {
        if (Array.isArray(global.TPA_CHAPTERS)) return global.TPA_CHAPTERS;
        if (global.TPA_CHAPTERS && Array.isArray(global.TPA_CHAPTERS.chapters)) return global.TPA_CHAPTERS.chapters;
        return [];
      }
      if (subjectId === 'law-criminal') {
        if (Array.isArray(global.CRIMINAL_CHAPTERS)) return global.CRIMINAL_CHAPTERS;
        if (global.CRIMINAL_CHAPTERS && Array.isArray(global.CRIMINAL_CHAPTERS.chapters)) return global.CRIMINAL_CHAPTERS.chapters;
        return [];
      }
      if (subjectId === 'law-crpc') {
        if (Array.isArray(global.CRPC_CHAPTERS)) return global.CRPC_CHAPTERS;
        if (global.CRPC_CHAPTERS && Array.isArray(global.CRPC_CHAPTERS.chapters)) return global.CRPC_CHAPTERS.chapters;
        return [];
      }
      if (subjectId === 'law-evidence') {
        if (Array.isArray(global.EVIDENCE_CHAPTERS)) return global.EVIDENCE_CHAPTERS;
        if (global.EVIDENCE_CHAPTERS && Array.isArray(global.EVIDENCE_CHAPTERS.chapters)) return global.EVIDENCE_CHAPTERS.chapters;
        return [];
      }
      if (subjectId === 'law-cpc') {
        if (Array.isArray(global.CPC_CHAPTERS)) return global.CPC_CHAPTERS;
        if (global.CPC_CHAPTERS && Array.isArray(global.CPC_CHAPTERS.chapters)) return global.CPC_CHAPTERS.chapters;
        return [];
      }
      if (subjectId === 'gk-history') return global.HISTORY_CHAPTERS || [];
      if (subjectId === 'gk-culture') return global.CULTURE_CHAPTERS || [];
      if (subjectId === 'gk-geography') return global.GEOGRAPHY_CHAPTERS || [];
      if (subjectId === 'gk-polity') return global.POLITY_CHAPTERS || [];
      if (subjectId === 'gk-economy') return global.ECONOMY_CHAPTERS || [];
      if (subjectId && subjectId.startsWith('soc-')) {
        if (Array.isArray(global.SOCIAL_CHAPTERS)) {
          return global.SOCIAL_CHAPTERS.filter(c => c.subjectId === subjectId);
        }
        return [];
      }
      return [];
    },

    getConstitutionChapters: function () {
      return LearningEngine.getChaptersBySubject('law-constitution');
    },

    getChapterById: function (chapterId, subjectId) {
      if (!chapterId) return null;
      if (subjectId) {
        const chapters = LearningEngine.getChaptersBySubject(subjectId);
        return chapters.find(c => c.id === chapterId) || null;
      }
      // Auto-detect by ID prefix
      if (chapterId.startsWith('ch-jur-')) {
        return LearningEngine.getChaptersBySubject('law-jurisprudence').find(c => c.id === chapterId) || null;
      }
      if (chapterId.startsWith('ch-cnt-')) {
        return LearningEngine.getChaptersBySubject('law-contract').find(c => c.id === chapterId) || null;
      }
      if (chapterId.startsWith('ch-tpa-')) {
        return LearningEngine.getChaptersBySubject('law-tpa').find(c => c.id === chapterId) || null;
      }
      if (chapterId.startsWith('ch-crim-')) {
        return LearningEngine.getChaptersBySubject('law-criminal').find(c => c.id === chapterId) || null;
      }
      if (chapterId.startsWith('ch-crpc-')) {
        return LearningEngine.getChaptersBySubject('law-crpc').find(c => c.id === chapterId) || null;
      }
      if (chapterId.startsWith('ch-evi-')) {
        return LearningEngine.getChaptersBySubject('law-evidence').find(c => c.id === chapterId) || null;
      }
      if (chapterId.startsWith('ch-cpc-')) {
        return LearningEngine.getChaptersBySubject('law-cpc').find(c => c.id === chapterId) || null;
      }
      if (chapterId.startsWith('ch-soc-')) {
        return (global.SOCIAL_CHAPTERS || []).find(c => c.id === chapterId) || null;
      }
      if (chapterId.startsWith('ch-hist-')) {
        return LearningEngine.getChaptersBySubject('gk-history').find(c => c.id === chapterId) || null;
      }
      if (chapterId.startsWith('ch-cult-')) {
        return LearningEngine.getChaptersBySubject('gk-culture').find(c => c.id === chapterId) || null;
      }
      if (chapterId.startsWith('ch-geo-')) {
        return LearningEngine.getChaptersBySubject('gk-geography').find(c => c.id === chapterId) || null;
      }
      if (chapterId.startsWith('ch-pol-')) {
        return LearningEngine.getChaptersBySubject('gk-polity').find(c => c.id === chapterId) || null;
      }
      if (chapterId.startsWith('ch-econ-')) {
        return LearningEngine.getChaptersBySubject('gk-economy').find(c => c.id === chapterId) || null;
      }

      // Check all active subjects
      const activeIds = ['law-constitution', 'law-jurisprudence', 'law-contract', 'law-tpa', 'law-criminal', 'law-crpc', 'law-evidence', 'law-cpc', 'gk-history', 'gk-culture', 'gk-geography', 'gk-polity', 'gk-economy'];
      for (const sid of activeIds) {
        const found = LearningEngine.getChaptersBySubject(sid).find(c => c.id === chapterId);
        if (found) return found;
      }
      return null;
    },

    getTopicsBySubject: function (subjectId) {
      if (!subjectId || subjectId === 'law-constitution') return global.CONSTITUTION_TOPICS || [];
      if (subjectId === 'law-jurisprudence') return global.JURISPRUDENCE_TOPICS || [];
      if (subjectId === 'law-contract') return global.CONTRACT_TOPICS || [];
      if (subjectId === 'law-tpa') return global.TPA_TOPICS || [];
      if (subjectId === 'law-criminal') return global.CRIMINAL_TOPICS || [];
      if (subjectId === 'law-crpc') return global.CRPC_TOPICS || [];
      if (subjectId === 'law-evidence') return global.EVIDENCE_TOPICS || [];
      if (subjectId === 'law-cpc') return global.CPC_TOPICS || [];
      if (subjectId === 'gk-history') return global.HISTORY_TOPICS || [];
      if (subjectId === 'gk-culture') return global.CULTURE_TOPICS || [];
      if (subjectId === 'gk-geography') return global.GEOGRAPHY_TOPICS || [];
      if (subjectId === 'gk-polity') return global.POLITY_TOPICS || [];
      if (subjectId === 'gk-economy') return global.ECONOMY_TOPICS || [];
      if (subjectId && subjectId.startsWith('soc-')) return (global.SOCIAL_TOPICS || []).filter(t => t.subjectId === subjectId);
      return [];
    },

    getTopicsByChapter: function (chapterId, subjectId) {
      if (!chapterId) {
        return subjectId ? LearningEngine.getTopicsBySubject(subjectId) : (global.CONSTITUTION_TOPICS || []);
      }
      if (subjectId) {
        const topics = LearningEngine.getTopicsBySubject(subjectId);
        return topics.filter(t => t.chapterId === chapterId);
      }
      // Auto-detect by chapter ID
      if (chapterId.startsWith('ch-jur-')) {
        return (global.JURISPRUDENCE_TOPICS || []).filter(t => t.chapterId === chapterId);
      }
      if (chapterId.startsWith('ch-cnt-')) {
        return (global.CONTRACT_TOPICS || []).filter(t => t.chapterId === chapterId);
      }
      if (chapterId.startsWith('ch-tpa-')) {
        return (global.TPA_TOPICS || []).filter(t => t.chapterId === chapterId);
      }
      if (chapterId.startsWith('ch-crim-')) {
        return (global.CRIMINAL_TOPICS || []).filter(t => t.chapterId === chapterId);
      }
      if (chapterId.startsWith('ch-crpc-')) {
        return (global.CRPC_TOPICS || []).filter(t => t.chapterId === chapterId);
      }
      if (chapterId.startsWith('ch-evi-')) {
        return (global.EVIDENCE_TOPICS || []).filter(t => t.chapterId === chapterId);
      }
      if (chapterId.startsWith('ch-cpc-')) {
        return (global.CPC_TOPICS || []).filter(t => t.chapterId === chapterId);
      }
      if (chapterId.startsWith('ch-soc-')) {
        return (global.SOCIAL_TOPICS || []).filter(t => t.chapterId === chapterId);
      }
      if (chapterId.startsWith('ch-hist-')) {
        return (global.HISTORY_TOPICS || []).filter(t => t.chapterId === chapterId);
      }
      if (chapterId.startsWith('ch-cult-')) {
        return (global.CULTURE_TOPICS || []).filter(t => t.chapterId === chapterId);
      }
      if (chapterId.startsWith('ch-geo-')) {
        return (global.GEOGRAPHY_TOPICS || []).filter(t => t.chapterId === chapterId);
      }
      if (chapterId.startsWith('ch-pol-')) {
        return (global.POLITY_TOPICS || []).filter(t => t.chapterId === chapterId);
      }
      if (chapterId.startsWith('ch-econ-')) {
        return (global.ECONOMY_TOPICS || []).filter(t => t.chapterId === chapterId);
      }

      const constTopics = (global.CONSTITUTION_TOPICS || []).filter(t => t.chapterId === chapterId);
      if (constTopics.length > 0) return constTopics;

      for (const sid of ['law-jurisprudence', 'law-contract', 'law-tpa', 'law-criminal', 'law-crpc', 'law-evidence', 'law-cpc']) {
        const tops = LearningEngine.getTopicsBySubject(sid).filter(t => t.chapterId === chapterId);
        if (tops.length > 0) return tops;
      }
      return [];
    },

    getTopicById: function (topicId, subjectId) {
      if (!topicId) return null;
      if (subjectId) {
        return LearningEngine.getTopicsBySubject(subjectId).find(t => t.id === topicId) || null;
      }
      if (topicId.startsWith('top-const-')) {
        return (global.CONSTITUTION_TOPICS || []).find(t => t.id === topicId) || null;
      }
      if (topicId.startsWith('top-jur-')) {
        return (global.JURISPRUDENCE_TOPICS || []).find(t => t.id === topicId) || null;
      }
      if (topicId.startsWith('top-cnt-')) {
        return (global.CONTRACT_TOPICS || []).find(t => t.id === topicId) || null;
      }
      if (topicId.startsWith('top-tpa-')) {
        return (global.TPA_TOPICS || []).find(t => t.id === topicId) || null;
      }
      if (topicId.startsWith('top-crim-')) {
        return (global.CRIMINAL_TOPICS || []).find(t => t.id === topicId) || null;
      }
      if (topicId.startsWith('top-crpc-')) {
        return (global.CRPC_TOPICS || []).find(t => t.id === topicId) || null;
      }
      if (topicId.startsWith('top-evi-')) {
        return (global.EVIDENCE_TOPICS || []).find(t => t.id === topicId) || null;
      }
      if (topicId.startsWith('top-cpc-')) {
        return (global.CPC_TOPICS || []).find(t => t.id === topicId) || null;
      }
      if (topicId.startsWith('top-disab-') || topicId.startsWith('top-parent-') ||
          topicId.startsWith('top-dowry-') || topicId.startsWith('top-dv-') ||
          topicId.startsWith('top-posh-') || topicId.startsWith('top-pcpndt-') ||
          topicId.startsWith('top-mtp-') || topicId.startsWith('top-irwa-') ||
          topicId.startsWith('top-pocso-')) {
        return (global.SOCIAL_TOPICS || []).find(t => t.id === topicId) || null;
      }
      if (topicId.startsWith('top-hist-')) {
        return (global.HISTORY_TOPICS || []).find(t => t.id === topicId) || null;
      }
      if (topicId.startsWith('top-cult-')) {
        return (global.CULTURE_TOPICS || []).find(t => t.id === topicId) || null;
      }
      if (topicId.startsWith('top-geo-')) {
        return (global.GEOGRAPHY_TOPICS || []).find(t => t.id === topicId) || null;
      }
      if (topicId.startsWith('top-pol-')) {
        return (global.POLITY_TOPICS || []).find(t => t.id === topicId) || null;
      }
      if (topicId.startsWith('top-econ-')) {
        return (global.ECONOMY_TOPICS || []).find(t => t.id === topicId) || null;
      }

      for (const sid of ['law-constitution', 'law-jurisprudence', 'law-contract', 'law-tpa', 'law-criminal', 'law-crpc', 'law-evidence', 'law-cpc']) {
        const found = LearningEngine.getTopicsBySubject(sid).find(t => t.id === topicId);
        if (found) return found;
      }
      return null;
    },

    getConceptByTopicId: function (topicId) {
      if (!topicId) return null;
      if (topicId.startsWith('top-const-')) {
        return (global.CONSTITUTION_CONCEPTS || {})[topicId] || null;
      }
      if (topicId.startsWith('top-jur-')) {
        return (global.JURISPRUDENCE_CONCEPTS || {})[topicId] || null;
      }
      if (topicId.startsWith('top-cnt-')) {
        return (global.CONTRACT_CONCEPTS || {})[topicId] || null;
      }
      if (topicId.startsWith('top-tpa-')) {
        return (global.TPA_CONCEPTS || {})[topicId] || null;
      }
      if (topicId.startsWith('top-crim-')) {
        return (global.CRIMINAL_CONCEPTS || {})[topicId] || null;
      }
      if (topicId.startsWith('top-crpc-')) {
        return (global.CRPC_CONCEPTS || {})[topicId] || null;
      }
      if (topicId.startsWith('top-evi-')) {
        return (global.EVIDENCE_CONCEPTS || {})[topicId] || null;
      }
      if (topicId.startsWith('top-cpc-')) {
        return (global.CPC_CONCEPTS || {})[topicId] || null;
      }
      if (global.SOCIAL_CONCEPTS && global.SOCIAL_CONCEPTS[topicId]) {
        return global.SOCIAL_CONCEPTS[topicId];
      }
      if (topicId.startsWith('top-hist-')) {
        return (global.HISTORY_CONCEPTS || {})[topicId] || null;
      }
      if (topicId.startsWith('top-cult-')) {
        return (global.CULTURE_CONCEPTS || {})[topicId] || null;
      }
      if (topicId.startsWith('top-geo-')) {
        return (global.GEOGRAPHY_CONCEPTS || {})[topicId] || null;
      }
      if (topicId.startsWith('top-pol-')) {
        return (global.POLITY_CONCEPTS || {})[topicId] || null;
      }
      if (topicId.startsWith('top-econ-')) {
        return (global.ECONOMY_CONCEPTS || {})[topicId] || null;
      }

      const pools = [
        global.CONSTITUTION_CONCEPTS,
        global.JURISPRUDENCE_CONCEPTS,
        global.CONTRACT_CONCEPTS,
        global.TPA_CONCEPTS,
        global.CRIMINAL_CONCEPTS,
        global.CRPC_CONCEPTS,
        global.EVIDENCE_CONCEPTS,
        global.CPC_CONCEPTS,
        global.SOCIAL_CONCEPTS,
        global.HISTORY_CONCEPTS,
        global.CULTURE_CONCEPTS,
        global.GEOGRAPHY_CONCEPTS,
        global.POLITY_CONCEPTS,
        global.ECONOMY_CONCEPTS
      ];
      for (const pool of pools) {
        if (pool && pool[topicId]) return pool[topicId];
      }
      return null;
    },

    getMCQsBySubject: function (subjectId) {
      if (!subjectId || subjectId === 'law-constitution') return global.CONSTITUTION_MCQS || [];
      if (subjectId === 'law-jurisprudence') return global.JURISPRUDENCE_MCQS || [];
      if (subjectId === 'law-contract') return global.CONTRACT_MCQS || [];
      if (subjectId === 'law-tpa') return global.TPA_MCQS || [];
      if (subjectId === 'law-criminal') return global.CRIMINAL_MCQS || [];
      if (subjectId === 'law-crpc') return global.CRPC_MCQS || [];
      if (subjectId === 'law-evidence') return global.EVIDENCE_MCQS || [];
      if (subjectId === 'law-cpc') return global.CPC_MCQS || [];
      if (subjectId === 'gk-history') return global.HISTORY_MCQS || [];
      if (subjectId === 'gk-culture') return global.CULTURE_MCQS || [];
      if (subjectId === 'gk-geography') return global.GEOGRAPHY_MCQS || [];
      if (subjectId === 'gk-polity') return global.POLITY_MCQS || [];
      if (subjectId === 'gk-economy') return global.ECONOMY_MCQS || [];
      if (subjectId && subjectId.startsWith('soc-')) return (global.SOCIAL_MCQS || []).filter(m => m.subjectId === subjectId);
      return [];
    },

    getMCQsByTopic: function (topicId, subjectId) {
      if (!topicId) return subjectId ? LearningEngine.getMCQsBySubject(subjectId) : (global.CONSTITUTION_MCQS || []);
      if (subjectId) {
        return LearningEngine.getMCQsBySubject(subjectId).filter(m => m.topicId === topicId);
      }
      if (topicId.startsWith('top-const-')) return (global.CONSTITUTION_MCQS || []).filter(m => m.topicId === topicId);
      if (topicId.startsWith('top-jur-')) return (global.JURISPRUDENCE_MCQS || []).filter(m => m.topicId === topicId);
      if (topicId.startsWith('top-cnt-')) return (global.CONTRACT_MCQS || []).filter(m => m.topicId === topicId);
      if (topicId.startsWith('top-tpa-')) return (global.TPA_MCQS || []).filter(m => m.topicId === topicId);
      if (topicId.startsWith('top-crim-')) return (global.CRIMINAL_MCQS || []).filter(m => m.topicId === topicId);
      if (topicId.startsWith('top-crpc-')) return (global.CRPC_MCQS || []).filter(m => m.topicId === topicId);
      if (topicId.startsWith('top-evi-')) return (global.EVIDENCE_MCQS || []).filter(m => m.topicId === topicId);
      if (topicId.startsWith('top-cpc-')) return (global.CPC_MCQS || []).filter(m => m.topicId === topicId);
      if (topicId.startsWith('top-disab-') || topicId.startsWith('top-parent-') ||
          topicId.startsWith('top-dowry-') || topicId.startsWith('top-dv-') ||
          topicId.startsWith('top-posh-') || topicId.startsWith('top-pcpndt-') ||
          topicId.startsWith('top-mtp-') || topicId.startsWith('top-irwa-') ||
          topicId.startsWith('top-pocso-')) {
        return (global.SOCIAL_MCQS || []).filter(m => m.topicId === topicId);
      }
      if (topicId.startsWith('top-hist-')) return (global.HISTORY_MCQS || []).filter(m => m.topicId === topicId);
      if (topicId.startsWith('top-cult-')) return (global.CULTURE_MCQS || []).filter(m => m.topicId === topicId);
      if (topicId.startsWith('top-geo-')) return (global.GEOGRAPHY_MCQS || []).filter(m => m.topicId === topicId);
      if (topicId.startsWith('top-pol-')) return (global.POLITY_MCQS || []).filter(m => m.topicId === topicId);
      if (topicId.startsWith('top-econ-')) return (global.ECONOMY_MCQS || []).filter(m => m.topicId === topicId);

      for (const sid of ['law-constitution', 'law-jurisprudence', 'law-contract', 'law-tpa', 'law-criminal', 'law-crpc', 'law-evidence', 'law-cpc']) {
        const list = LearningEngine.getMCQsBySubject(sid).filter(m => m.topicId === topicId);
        if (list.length > 0) return list;
      }
      return [];
    },

    getMCQsByChapter: function (chapterId, subjectId) {
      if (!chapterId) return subjectId ? LearningEngine.getMCQsBySubject(subjectId) : (global.CONSTITUTION_MCQS || []);
      if (subjectId) {
        return LearningEngine.getMCQsBySubject(subjectId).filter(m => m.chapterId === chapterId);
      }
      if (chapterId.startsWith('ch-jur-')) return (global.JURISPRUDENCE_MCQS || []).filter(m => m.chapterId === chapterId);
      if (chapterId.startsWith('ch-cnt-')) return (global.CONTRACT_MCQS || []).filter(m => m.chapterId === chapterId);
      if (chapterId.startsWith('ch-tpa-')) return (global.TPA_MCQS || []).filter(m => m.chapterId === chapterId);
      if (chapterId.startsWith('ch-crim-')) return (global.CRIMINAL_MCQS || []).filter(m => m.chapterId === chapterId);
      if (chapterId.startsWith('ch-crpc-')) return (global.CRPC_MCQS || []).filter(m => m.chapterId === chapterId);
      if (chapterId.startsWith('ch-evi-')) return (global.EVIDENCE_MCQS || []).filter(m => m.chapterId === chapterId);
      if (chapterId.startsWith('ch-cpc-')) return (global.CPC_MCQS || []).filter(m => m.chapterId === chapterId);
      if (chapterId.startsWith('ch-soc-')) return (global.SOCIAL_MCQS || []).filter(m => m.chapterId === chapterId);
      if (chapterId.startsWith('ch-hist-')) return (global.HISTORY_MCQS || []).filter(m => m.chapterId === chapterId);
      if (chapterId.startsWith('ch-cult-')) return (global.CULTURE_MCQS || []).filter(m => m.chapterId === chapterId);
      if (chapterId.startsWith('ch-geo-')) return (global.GEOGRAPHY_MCQS || []).filter(m => m.chapterId === chapterId);
      if (chapterId.startsWith('ch-pol-')) return (global.POLITY_MCQS || []).filter(m => m.chapterId === chapterId);
      if (chapterId.startsWith('ch-econ-')) return (global.ECONOMY_MCQS || []).filter(m => m.chapterId === chapterId);

      const constList = (global.CONSTITUTION_MCQS || []).filter(m => m.chapterId === chapterId);
      if (constList.length > 0) return constList;

      for (const sid of ['law-jurisprudence', 'law-contract', 'law-tpa', 'law-criminal', 'law-crpc', 'law-evidence', 'law-cpc']) {
        const list = LearningEngine.getMCQsBySubject(sid).filter(m => m.chapterId === chapterId);
        if (list.length > 0) return list;
      }
      return [];
    },

    getPYQsBySubject: function (subjectId) {
      if (!subjectId || subjectId === 'law-constitution') return global.CONSTITUTION_PYQ_MAPPING || [];
      if (subjectId === 'law-jurisprudence') return global.JURISPRUDENCE_PYQ_MAPPING || [];
      if (subjectId === 'law-contract') return global.CONTRACT_PYQ_MAPPING || [];
      if (subjectId === 'law-tpa') return global.TPA_PYQ_MAPPING || [];
      if (subjectId === 'law-criminal') return global.CRIMINAL_PYQ_MAPPING || [];
      if (subjectId === 'law-crpc') return global.CRPC_PYQ_MAPPING || [];
      if (subjectId === 'law-evidence') return global.EVIDENCE_PYQ_MAPPING || [];
      if (subjectId === 'law-cpc') return global.CPC_PYQ_MAPPING || [];
      if (subjectId === 'gk-history') return global.HISTORY_PYQ_MAPPING || [];
      if (subjectId === 'gk-culture') return global.CULTURE_PYQ_MAPPING || global.CULTURE_PYQS || [];
      if (subjectId === 'gk-geography') return global.GEOGRAPHY_PYQ_MAPPING || global.GEOGRAPHY_PYQS || [];
      if (subjectId === 'gk-polity') return global.POLITY_PYQ_MAPPING || global.POLITY_PYQS || [];
      if (subjectId === 'gk-economy') return global.ECONOMY_PYQ_MAPPING || global.ECONOMY_PYQS || [];
      if (subjectId && subjectId.startsWith('soc-')) return (global.SOCIAL_PYQ_MAPPING || []).filter(p => p.subjectId === subjectId);
      return [];
    },

    getPYQsByTopic: function (topicId, subjectId) {
      if (!topicId) return subjectId ? LearningEngine.getPYQsBySubject(subjectId) : (global.CONSTITUTION_PYQ_MAPPING || []);
      if (subjectId) {
        return LearningEngine.getPYQsBySubject(subjectId).filter(p => p.topicId === topicId);
      }
      if (topicId.startsWith('top-const-')) return (global.CONSTITUTION_PYQ_MAPPING || []).filter(p => p.topicId === topicId);
      if (topicId.startsWith('top-jur-')) return (global.JURISPRUDENCE_PYQ_MAPPING || []).filter(p => p.topicId === topicId);
      if (topicId.startsWith('top-cnt-')) return (global.CONTRACT_PYQ_MAPPING || []).filter(p => p.topicId === topicId);
      if (topicId.startsWith('top-tpa-')) return (global.TPA_PYQ_MAPPING || []).filter(p => p.topicId === topicId);
      if (topicId.startsWith('top-crim-')) return (global.CRIMINAL_PYQ_MAPPING || []).filter(p => p.topicId === topicId);
      if (topicId.startsWith('top-crpc-')) return (global.CRPC_PYQ_MAPPING || []).filter(p => p.topicId === topicId);
      if (topicId.startsWith('top-evi-')) return (global.EVIDENCE_PYQ_MAPPING || []).filter(p => p.topicId === topicId);
      if (topicId.startsWith('top-cpc-')) return (global.CPC_PYQ_MAPPING || []).filter(p => p.topicId === topicId);
      if (topicId.startsWith('top-disab-') || topicId.startsWith('top-parent-') ||
          topicId.startsWith('top-dowry-') || topicId.startsWith('top-dv-') ||
          topicId.startsWith('top-posh-') || topicId.startsWith('top-pcpndt-') ||
          topicId.startsWith('top-mtp-') || topicId.startsWith('top-irwa-') ||
          topicId.startsWith('top-pocso-')) {
        return (global.SOCIAL_PYQ_MAPPING || []).filter(p => p.topicId === topicId);
      }
      if (topicId.startsWith('top-hist-')) return (global.HISTORY_PYQ_MAPPING || []).filter(p => p.topicId === topicId);
      if (topicId.startsWith('top-cult-')) return (global.CULTURE_PYQ_MAPPING || global.CULTURE_PYQS || []).filter(p => p.topicId === topicId);
      if (topicId.startsWith('top-geo-')) return (global.GEOGRAPHY_PYQ_MAPPING || global.GEOGRAPHY_PYQS || []).filter(p => p.topicId === topicId);
      if (topicId.startsWith('top-pol-')) return (global.POLITY_PYQ_MAPPING || global.POLITY_PYQS || []).filter(p => p.topicId === topicId);
      if (topicId.startsWith('top-econ-')) return (global.ECONOMY_PYQ_MAPPING || global.ECONOMY_PYQS || []).filter(p => p.topicId === topicId);

      for (const sid of ['law-constitution', 'law-jurisprudence', 'law-contract', 'law-tpa', 'law-criminal', 'law-crpc', 'law-evidence', 'law-cpc']) {
        const list = LearningEngine.getPYQsBySubject(sid).filter(p => p.topicId === topicId);
        if (list.length > 0) return list;
      }
      return [];
    },

    getPYQsByChapter: function (chapterId, subjectId) {
      if (!chapterId) return subjectId ? LearningEngine.getPYQsBySubject(subjectId) : (global.CONSTITUTION_PYQ_MAPPING || []);
      if (subjectId) {
        return LearningEngine.getPYQsBySubject(subjectId).filter(p => p.chapterId === chapterId);
      }
      if (chapterId.startsWith('ch-jur-')) return (global.JURISPRUDENCE_PYQ_MAPPING || []).filter(p => p.chapterId === chapterId);
      if (chapterId.startsWith('ch-cnt-')) return (global.CONTRACT_PYQ_MAPPING || []).filter(p => p.chapterId === chapterId);
      if (chapterId.startsWith('ch-tpa-')) return (global.TPA_PYQ_MAPPING || []).filter(p => p.chapterId === chapterId);
      if (chapterId.startsWith('ch-crim-')) return (global.CRIMINAL_PYQ_MAPPING || []).filter(p => p.chapterId === chapterId);
      if (chapterId.startsWith('ch-crpc-')) return (global.CRPC_PYQ_MAPPING || []).filter(p => p.chapterId === chapterId);
      if (chapterId.startsWith('ch-evi-')) return (global.EVIDENCE_PYQ_MAPPING || []).filter(p => p.chapterId === chapterId);
      if (chapterId.startsWith('ch-cpc-')) return (global.CPC_PYQ_MAPPING || []).filter(p => p.chapterId === chapterId);
      if (chapterId.startsWith('ch-soc-')) return (global.SOCIAL_PYQ_MAPPING || []).filter(p => p.chapterId === chapterId);
      if (chapterId.startsWith('ch-hist-')) return (global.HISTORY_PYQ_MAPPING || []).filter(p => p.chapterId === chapterId);
      if (chapterId.startsWith('ch-cult-')) return (global.CULTURE_PYQ_MAPPING || global.CULTURE_PYQS || []).filter(p => p.chapterId === chapterId);
      if (chapterId.startsWith('ch-geo-')) return (global.GEOGRAPHY_PYQ_MAPPING || global.GEOGRAPHY_PYQS || []).filter(p => p.chapterId === chapterId);
      if (chapterId.startsWith('ch-pol-')) return (global.POLITY_PYQ_MAPPING || global.POLITY_PYQS || []).filter(p => p.chapterId === chapterId);
      if (chapterId.startsWith('ch-econ-')) return (global.ECONOMY_PYQ_MAPPING || global.ECONOMY_PYQS || []).filter(p => p.chapterId === chapterId);

      const constList = (global.CONSTITUTION_PYQ_MAPPING || []).filter(p => p.chapterId === chapterId);
      if (constList.length > 0) return constList;

      for (const sid of ['law-jurisprudence', 'law-contract', 'law-tpa', 'law-criminal', 'law-crpc', 'law-evidence', 'law-cpc']) {
        const list = LearningEngine.getPYQsBySubject(sid).filter(p => p.chapterId === chapterId);
        if (list.length > 0) return list;
      }
      return [];
    },

    getStatutoryComparisons: function (subjectId, query, changeType) {
      const all = global.STATUTORY_COMPARISONS || global.CRIMINAL_COMPARISONS || [];
      return all.filter(item => {
        if (subjectId && subjectId !== 'all' && item.subject !== subjectId) return false;
        if (changeType && changeType !== 'all') {
          if (changeType === 'caveat') {
            const isCaveat = (item.id === 'comp-bns-013' || item.currentSection.includes('106(2)') || (item.commencementStatus && item.commencementStatus.includes('NOT in force')));
            if (!isCaveat) return false;
          } else if (!item.status.toLowerCase().includes(changeType.toLowerCase())) {
            return false;
          }
        }
        if (query && query.trim()) {
          const q = query.toLowerCase().trim();
          const hay = [
            item.title, item.currentAct, item.currentSection,
            item.historicalAct, item.historicalSection,
            item.materialChanges, item.keyTakeaway
          ].join(' ').toLowerCase();
          if (!hay.includes(q)) return false;
        }
        return true;
      });
    },

    // ------------------------------------------------------------------------
    // ACADEMY METRICS & READINESS
    // ------------------------------------------------------------------------
    getAcademyOverviewStats: function () {
      const subjects = LearningEngine.getAllSubjects();
      const activeSubjects = subjects.filter(s => s.status === 'active');
      const upcomingSubjects = subjects.filter(s => s.status === 'upcoming');

      const constProg = global.LearningStorage ? global.LearningStorage.getSubjectProgress('law-constitution') : {};
      const jurProg = global.LearningStorage ? global.LearningStorage.getSubjectProgress('law-jurisprudence') : {};
      const cntProg = global.LearningStorage ? global.LearningStorage.getSubjectProgress('law-contract') : {};
      const tpaProg = global.LearningStorage ? global.LearningStorage.getSubjectProgress('law-tpa') : {};
      const crimProg = global.LearningStorage ? global.LearningStorage.getSubjectProgress('law-criminal') : {};
      const crpcProg = global.LearningStorage ? global.LearningStorage.getSubjectProgress('law-crpc') : {};
      const eviProg = global.LearningStorage ? global.LearningStorage.getSubjectProgress('law-evidence') : {};
      const cpcProg = global.LearningStorage ? global.LearningStorage.getSubjectProgress('law-cpc') : {};

      let totalActiveChapters = 0;
      let totalActiveTopics = 0;
      let totalActiveMCQs = 0;
      let totalCompletedTopics = 0;

      activeSubjects.forEach(s => {
        totalActiveChapters += (s.chaptersCount || 0);
        totalActiveTopics += (s.topicsCount || 0);
        totalActiveMCQs += (s.mcqsCount || 0);
        if (global.LearningStorage) {
          const p = global.LearningStorage.getSubjectProgress(s.id);
          totalCompletedTopics += (p.completedTopics || 0);
        }
      });

      const totalActivePYQs = (global.CONSTITUTION_PYQ_MAPPING || []).length +
                              (global.JURISPRUDENCE_PYQ_MAPPING || []).length +
                              (global.CONTRACT_PYQ_MAPPING || []).length +
                              (global.TPA_PYQ_MAPPING || []).length +
                              (global.CRIMINAL_PYQ_MAPPING || []).length +
                              (global.CRPC_PYQ_MAPPING || []).length +
                              (global.EVIDENCE_PYQ_MAPPING || []).length +
                              (global.CPC_PYQ_MAPPING || []).length +
                              (global.SOCIAL_PYQ_MAPPING || []).length +
                              (global.HISTORY_PYQ_MAPPING || []).length +
                              (global.CULTURE_PYQ_MAPPING || global.CULTURE_PYQS || []).length +
                              (global.GEOGRAPHY_PYQ_MAPPING || global.GEOGRAPHY_PYQS || []).length +
                              (global.POLITY_PYQ_MAPPING || global.POLITY_PYQS || []).length +
                              (global.ECONOMY_PYQ_MAPPING || global.ECONOMY_PYQS || []).length;

      const overallPercentage = totalActiveTopics > 0 ? Math.round((totalCompletedTopics / totalActiveTopics) * 100) : 0;

      return {
        totalSubjects: subjects.length,
        activeSubjectsCount: activeSubjects.length,
        upcomingSubjectsCount: upcomingSubjects.length,
        paper1Count: subjects.filter(s => s.paper === 'Paper I').length,
        paper2Count: subjects.filter(s => s.paper === 'Paper II').length,
        totalActiveChapters: totalActiveChapters,
        totalActiveTopics: totalActiveTopics,
        totalActiveMCQs: totalActiveMCQs,
        totalActivePYQs: totalActivePYQs,
        totalCompletedTopics: totalCompletedTopics,
        overallPercentage: overallPercentage,
        constitution: {
          totalChapters: 15,
          totalTopics: 45,
          totalMCQs: 480,
          totalPYQs: (global.CONSTITUTION_PYQ_MAPPING || []).length,
          completedTopics: constProg.completedTopics || 0,
          completionPercentage: constProg.topicPercentage || 0,
          testsTaken: constProg.testsTaken || 0,
          accuracyPct: constProg.accuracyPct || 0,
          unresolvedMistakes: constProg.unresolvedMistakes || 0,
          bookmarksCount: constProg.bookmarksCount || 0
        },
        jurisprudence: {
          totalChapters: 11,
          totalTopics: 30,
          totalMCQs: 240,
          totalPYQs: (global.JURISPRUDENCE_PYQ_MAPPING || []).length,
          completedTopics: jurProg.completedTopics || 0,
          completionPercentage: jurProg.topicPercentage || 0,
          testsTaken: jurProg.testsTaken || 0,
          accuracyPct: jurProg.accuracyPct || 0,
          unresolvedMistakes: jurProg.unresolvedMistakes || 0,
          bookmarksCount: jurProg.bookmarksCount || 0
        },
        contract: {
          totalChapters: 11,
          totalTopics: 32,
          totalMCQs: 260,
          totalPYQs: (global.CONTRACT_PYQ_MAPPING || []).length,
          completedTopics: cntProg.completedTopics || 0,
          completionPercentage: cntProg.topicPercentage || 0,
          testsTaken: cntProg.testsTaken || 0,
          accuracyPct: cntProg.accuracyPct || 0,
          unresolvedMistakes: cntProg.unresolvedMistakes || 0,
          bookmarksCount: cntProg.bookmarksCount || 0
        },
        tpa: {
          totalChapters: 8,
          totalTopics: 24,
          totalMCQs: 240,
          totalPYQs: (global.TPA_PYQ_MAPPING || []).length,
          completedTopics: tpaProg.completedTopics || 0,
          completionPercentage: tpaProg.topicPercentage || 0,
          testsTaken: tpaProg.testsTaken || 0,
          accuracyPct: tpaProg.accuracyPct || 0,
          unresolvedMistakes: tpaProg.unresolvedMistakes || 0,
          bookmarksCount: tpaProg.bookmarksCount || 0
        },
        criminal: {
          totalChapters: 12,
          totalTopics: 36,
          totalMCQs: 360,
          totalPYQs: (global.CRIMINAL_PYQ_MAPPING || []).length,
          completedTopics: crimProg.completedTopics || 0,
          completionPercentage: crimProg.topicPercentage || 0,
          testsTaken: crimProg.testsTaken || 0,
          accuracyPct: crimProg.accuracyPct || 0,
          unresolvedMistakes: crimProg.unresolvedMistakes || 0,
          bookmarksCount: crimProg.bookmarksCount || 0
        },
        crpc: {
          totalChapters: 12,
          totalTopics: 35,
          totalMCQs: 360,
          totalPYQs: (global.CRPC_PYQ_MAPPING || []).length,
          completedTopics: crpcProg.completedTopics || 0,
          completionPercentage: crpcProg.topicPercentage || 0,
          testsTaken: crpcProg.testsTaken || 0,
          accuracyPct: crpcProg.accuracyPct || 0,
          unresolvedMistakes: crpcProg.unresolvedMistakes || 0,
          bookmarksCount: crpcProg.bookmarksCount || 0
        },
        evidence: {
          totalChapters: 10,
          totalTopics: 30,
          totalMCQs: 280,
          totalPYQs: (global.EVIDENCE_PYQ_MAPPING || []).length,
          completedTopics: eviProg.completedTopics || 0,
          completionPercentage: eviProg.topicPercentage || 0,
          testsTaken: eviProg.testsTaken || 0,
          accuracyPct: eviProg.accuracyPct || 0,
          unresolvedMistakes: eviProg.unresolvedMistakes || 0,
          bookmarksCount: eviProg.bookmarksCount || 0
        },
        cpc: {
          totalChapters: 20,
          totalTopics: 57,
          totalMCQs: 400,
          totalPYQs: (global.CPC_PYQ_MAPPING || []).length,
          completedTopics: cpcProg.completedTopics || 0,
          completionPercentage: cpcProg.topicPercentage || 0,
          testsTaken: cpcProg.testsTaken || 0,
          accuracyPct: cpcProg.accuracyPct || 0,
          unresolvedMistakes: cpcProg.unresolvedMistakes || 0,
          bookmarksCount: cpcProg.bookmarksCount || 0
        }
      };
    },

    getStats: function () {
      const stats = LearningEngine.getAcademyOverviewStats();
      return {
        activeSubjects: stats.activeSubjectsCount,
        chapters: stats.totalActiveChapters,
        topics: stats.totalActiveTopics,
        mcqs: stats.totalActiveMCQs,
        pyqs: stats.totalActivePYQs
      };
    },

    getCPCSectionsOrdersRules: function (query, type) {
      const all = global.CPC_SECTIONS_ORDERS_RULES || [];
      return all.filter(item => {
        if (type && type !== 'all' && item.type !== type) return false;
        if (query && query.trim()) {
          const q = query.toLowerCase().trim();
          const hay = [item.number, item.title, item.subject, item.coreRule, item.upRelevance].join(' ').toLowerCase();
          if (!hay.includes(q)) return false;
        }
        return true;
      });
    },

    getSocialSectionsExplorer: function (query, actId) {
      const all = global.SOCIAL_SECTIONS_EXPLORER || [];
      return all.filter(item => {
        if (actId && actId !== 'all' && item.subjectId !== actId) return false;
        if (query && query.trim()) {
          const q = query.toLowerCase().trim();
          const hay = [item.number, item.title, item.subject, item.coreRule, item.upRelevance].join(' ').toLowerCase();
          if (!hay.includes(q)) return false;
        }
        return true;
      });
    },

    // ------------------------------------------------------------------------
    // UI RENDERERS FOR ACADEMY HUB
    // ------------------------------------------------------------------------
    renderSubjectCards: function (containerEl, filter, searchQuery) {
      if (!containerEl) return;
      const subjects = LearningEngine.getAllSubjects();
      let filtered = subjects;

      // Filter by paper or status
      if (filter === 'paper1') {
        filtered = filtered.filter(s => s.paper.includes('Paper I') || s.paper === 'GK' || (s.id && s.id.startsWith('soc-')));
      } else if (filter === 'paper2') {
        filtered = filtered.filter(s => s.paper.includes('Paper II') || s.paper === 'LAW');
      } else if (filter === 'active') {
        filtered = filtered.filter(s => s.status === 'active');
      } else if (filter === 'gk') {
        filtered = filtered.filter(s => (s.id && s.id.startsWith('gk-') && s.status === 'active'));
      } else if (filter === 'social') {
        filtered = filtered.filter(s => s.category === 'social_legislation' || (s.id && s.id.startsWith('soc-')) || s.paper.includes('Social Legislation'));
      }

      // Filter by search query
      if (searchQuery && searchQuery.trim()) {
        const q = searchQuery.toLowerCase().trim();
        filtered = filtered.filter(s =>
          s.name.toLowerCase().includes(q) ||
          s.code.toLowerCase().includes(q) ||
          s.description.toLowerCase().includes(q)
        );
      }

      if (filtered.length === 0) {
        containerEl.innerHTML = `
          <div class="empty-state-card" style="text-align: center; padding: 40px 20px; background: #fff; border-radius: 8px; border: 1px dashed #cdb17d; grid-column: 1 / -1;">
            <p style="font-size: 24px; margin-bottom: 8px;">🔍</p>
            <h4 style="font-family: Georgia, serif; color: #142c46; margin: 0 0 6px;">No Subjects Found</h4>
            <p style="color: #607387; font-size: 13px; margin: 0;">Try adjusting your search keyword or active tab filter.</p>
          </div>
        `;
        return;
      }

      const cardsHtml = filtered.map(subject => {
        const isActive = subject.status === 'active';
        const progress = (isActive && global.LearningStorage) ? global.LearningStorage.getSubjectProgress(subject.id) : {};
        const completionPct = progress.topicPercentage || 0;
        const totalTopics = subject.topicsCount || 0;
        const completedCount = progress.completedTopics || 0;

        return `
          <div class="subject-card ${isActive ? 'is-active' : 'is-upcoming'} ${subject.id === 'law-constitution' ? 'is-featured' : ''}" data-subject-id="${subject.id}">
            <div class="subject-card-header">
              <span class="subject-icon">${subject.icon || '📚'}</span>
              <div class="subject-badges">
                <span class="badge badge-paper">${subject.paper}</span>
                <span class="badge ${isActive ? 'badge-status-active' : 'badge-status-upcoming'}">
                  ${isActive ? '● Active Module' : 'Upcoming'}
                </span>
              </div>
            </div>

            <div class="subject-card-body">
              <h3 class="subject-title">
                ${isActive ? `<a href="subject-study.html?subject=${subject.id}">${subject.name}</a>` : subject.name}
              </h3>
              ${(subject.curriculumRef || subject.code) ? `<p class="subject-code">${subject.curriculumRef || subject.code}</p>` : ''}
              <p class="subject-desc">${subject.description}</p>

              <div class="subject-meta-grid">
                <div class="meta-item">
                  <span class="meta-label">Chapters</span>
                  <span class="meta-value">${subject.chaptersCount || 0}</span>
                </div>
                <div class="meta-item">
                  <span class="meta-label">Topics</span>
                  <span class="meta-value">${totalTopics}</span>
                </div>
                <div class="meta-item">
                  <span class="meta-label">MCQs Bank</span>
                  <span class="meta-value">${subject.mcqsCount || 0}</span>
                </div>
              </div>

              ${isActive ? `
                <div class="subject-progress-container">
                  <div class="progress-label-row">
                    <span>Topic Progress</span>
                    <span class="pct-text">${completionPct}% (${completedCount}/${totalTopics})</span>
                  </div>
                  <div class="progress-bar-track">
                    <div class="progress-bar-fill" style="width: ${completionPct}%"></div>
                  </div>
                </div>
              ` : `
                <div class="upcoming-release-badge">
                  <span>🚀 Scheduled for Future Academic Releases</span>
                </div>
              `}
            </div>

            <div class="subject-card-footer">
              ${isActive ? `
                <a href="subject-study.html?subject=${subject.id}" class="btn btn-primary btn-sm">
                  📖 Study Topics
                </a>
                <a href="topic-practice.html?subject=${subject.id}&mode=learn" class="btn btn-outline btn-sm">
                  ⚡ Practise MCQs
                </a>
                <a href="subject-progress.html?subject=${subject.id}" class="btn btn-subtle btn-sm" title="Detailed Analytics">
                  📊
                </a>
              ` : `
                <button class="btn btn-disabled btn-sm" disabled>
                  🔒 Module Locked
                </button>
              `}
            </div>
          </div>
        `;
      }).join('');

      containerEl.innerHTML = cardsHtml;
    },

    // ------------------------------------------------------------------------
    // RENDER CHAPTER LIST FOR ANY ACTIVE SUBJECT
    // ------------------------------------------------------------------------
    renderChapterCards: function (containerEl, subjectId) {
      if (!containerEl) return;
      const targetSubjectId = subjectId || 'law-constitution';
      const chapters = LearningEngine.getChaptersBySubject(targetSubjectId);

      if (!chapters || chapters.length === 0) {
        containerEl.innerHTML = `<p style="padding: 20px; color: #607387;">This subject module is coming soon in future releases.</p>`;
        return;
      }

      const store = global.LearningStorage ? global.LearningStorage.exportData() : {};
      const completedTopics = (store.completedTopics || {});

      const html = chapters.map(ch => {
        const topics = LearningEngine.getTopicsByChapter(ch.id, targetSubjectId);
        const completedInCh = topics.filter(t => completedTopics[t.id]).length;
        const pct = topics.length > 0 ? Math.round((completedInCh / topics.length) * 100) : 0;
        const pyqs = LearningEngine.getPYQsByChapter(ch.id, targetSubjectId);
        const rangeText = ch.sectionsRange || ch.articlesRange || ch.scope || '';
        const descText = ch.description || ch.scope || '';

        return `
          <div class="chapter-card" id="card-${ch.id}">
            <div class="chapter-card-header">
              <div class="ch-badge-col">
                <span class="chapter-number">${ch.number}</span>
              </div>
              <div class="ch-title-col">
                <span class="chapter-range">${rangeText}</span>
                <h3 class="chapter-title"><a href="subject-study.html?subject=${targetSubjectId}&chapter=${ch.id}&topic=${topics[0]?.id || ''}">${ch.title}</a></h3>
                <p class="chapter-desc">${descText}</p>
              </div>
              <div class="ch-stat-col">
                <div class="stat-pill"><span class="num">${topics.length}</span> Topics</div>
                <div class="stat-pill"><span class="num">${ch.mcqsCount || 0}</span> MCQs</div>
                ${pyqs.length ? `<div class="stat-pill pyq-pill"><span class="num">${pyqs.length}</span> PYQs</div>` : ''}
              </div>
            </div>

            <div class="chapter-progress-row">
              <div class="progress-bar-track">
                <div class="progress-bar-fill" style="width: ${pct}%"></div>
              </div>
              <span class="progress-text">${pct}% complete (${completedInCh}/${topics.length})</span>
            </div>

            <div class="chapter-topics-accordion">
              <ul class="topic-mini-list">
                ${topics.map(top => {
                  const isRead = !!completedTopics[top.id];
                  const topMCQs = LearningEngine.getMCQsByTopic(top.id, targetSubjectId);
                  const topPYQs = LearningEngine.getPYQsByTopic(top.id, targetSubjectId);

                  return `
                    <li class="topic-mini-item ${isRead ? 'is-read' : ''}">
                      <div class="topic-status-marker" title="${isRead ? 'Completed' : 'Unread'}">
                        ${isRead ? '✓' : '○'}
                      </div>
                      <div class="topic-info">
                        <a href="subject-study.html?subject=${targetSubjectId}&chapter=${ch.id}&topic=${top.id}" class="topic-link">
                          ${top.title}
                        </a>
                        <span class="topic-sub">${top.subtitle || ''}</span>
                      </div>
                      <div class="topic-actions">
                        <a href="topic-practice.html?subject=${targetSubjectId}&chapter=${ch.id}&topic=${top.id}&mode=topic_test" class="btn-micro" title="Practise MCQs">
                          ⚡ ${topMCQs.length} MCQs
                        </a>
                        ${topPYQs.length ? `
                          <a href="topic-practice.html?subject=${targetSubjectId}&chapter=${ch.id}&topic=${top.id}&mode=pyq" class="btn-micro btn-micro-gold" title="Historical PYQs">
                            📜 ${topPYQs.length} PYQs
                          </a>
                        ` : ''}
                      </div>
                    </li>
                  `;
                }).join('')}
              </ul>
            </div>

            <div class="chapter-card-footer">
              <a href="subject-study.html?subject=${targetSubjectId}&chapter=${ch.id}&topic=${topics[0]?.id || ''}" class="btn btn-outline btn-sm">
                📖 Study Chapter
              </a>
              <a href="topic-practice.html?subject=${targetSubjectId}&chapter=${ch.id}&mode=chapter_test" class="btn btn-primary btn-sm">
                📝 Chapter Test (${ch.mcqsCount || 0} Questions)
              </a>
            </div>
          </div>
        `;
      }).join('');

      containerEl.innerHTML = html;
    }
  };

  global.LearningEngine = LearningEngine;

})(typeof window !== 'undefined' ? window : global);
