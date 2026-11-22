import re

with open('assets/learning/js/learning-engine.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. getChaptersBySubject
cpc_chap = '''      if (subjectId === 'law-cpc') {
        if (Array.isArray(global.CPC_CHAPTERS)) return global.CPC_CHAPTERS;
        if (global.CPC_CHAPTERS && Array.isArray(global.CPC_CHAPTERS.chapters)) return global.CPC_CHAPTERS.chapters;
        return [];
      }'''

soc_chap = cpc_chap + '''
      if (subjectId && subjectId.startsWith('soc-')) {
        if (Array.isArray(global.SOCIAL_CHAPTERS)) {
          return global.SOCIAL_CHAPTERS.filter(c => c.subjectId === subjectId);
        }
        return [];
      }'''

content = content.replace(cpc_chap, soc_chap, 1)

# 2. getChapterById
cpc_chap_id = '''      if (chapterId.startsWith('ch-cpc-')) {
        return LearningEngine.getChaptersBySubject('law-cpc').find(c => c.id === chapterId) || null;
      }'''

soc_chap_id = cpc_chap_id + '''
      if (chapterId.startsWith('ch-soc-')) {
        return (global.SOCIAL_CHAPTERS || []).find(c => c.id === chapterId) || null;
      }'''

content = content.replace(cpc_chap_id, soc_chap_id, 1)

# 3. getTopicsBySubject
cpc_top = "      if (subjectId === 'law-cpc') return global.CPC_TOPICS || [];"
soc_top = cpc_top + "\n      if (subjectId && subjectId.startsWith('soc-')) return (global.SOCIAL_TOPICS || []).filter(t => t.subjectId === subjectId);"
content = content.replace(cpc_top, soc_top, 1)

# 4. getTopicsByChapter
cpc_top_ch = '''      if (chapterId.startsWith('ch-cpc-')) {
        return (global.CPC_TOPICS || []).filter(t => t.chapterId === chapterId);
      }'''
soc_top_ch = cpc_top_ch + '''
      if (chapterId.startsWith('ch-soc-')) {
        return (global.SOCIAL_TOPICS || []).filter(t => t.chapterId === chapterId);
      }'''
content = content.replace(cpc_top_ch, soc_top_ch, 1)

# 5. getTopicById
cpc_top_id = '''      if (topicId.startsWith('top-cpc-')) {
        return (global.CPC_TOPICS || []).find(t => t.id === topicId) || null;
      }'''
soc_top_id = cpc_top_id + '''
      if (topicId.startsWith('top-disab-') || topicId.startsWith('top-parent-') ||
          topicId.startsWith('top-dowry-') || topicId.startsWith('top-dv-') ||
          topicId.startsWith('top-posh-') || topicId.startsWith('top-pcpndt-') ||
          topicId.startsWith('top-mtp-') || topicId.startsWith('top-irwa-') ||
          topicId.startsWith('top-pocso-')) {
        return (global.SOCIAL_TOPICS || []).find(t => t.id === topicId) || null;
      }'''
content = content.replace(cpc_top_id, soc_top_id, 1)

# 6. getConceptByTopicId
cpc_con = '''      if (topicId.startsWith('top-cpc-')) {
        return (global.CPC_CONCEPTS || {})[topicId] || null;
      }'''
soc_con = cpc_con + '''
      if (global.SOCIAL_CONCEPTS && global.SOCIAL_CONCEPTS[topicId]) {
        return global.SOCIAL_CONCEPTS[topicId];
      }'''
content = content.replace(cpc_con, soc_con, 1)

# In pools array
pools_old = '''        global.EVIDENCE_CONCEPTS,
        global.CPC_CONCEPTS
      ];'''
pools_new = '''        global.EVIDENCE_CONCEPTS,
        global.CPC_CONCEPTS,
        global.SOCIAL_CONCEPTS
      ];'''
content = content.replace(pools_old, pools_new, 1)

# 7. getMCQsBySubject
cpc_mcq = "      if (subjectId === 'law-cpc') return global.CPC_MCQS || [];"
soc_mcq = cpc_mcq + "\n      if (subjectId && subjectId.startsWith('soc-')) return (global.SOCIAL_MCQS || []).filter(m => m.subjectId === subjectId);"
content = content.replace(cpc_mcq, soc_mcq, 1)

# 8. getMCQsByTopic
cpc_mcq_top = "      if (topicId.startsWith('top-cpc-')) return (global.CPC_MCQS || []).filter(m => m.topicId === topicId);"
soc_mcq_top = cpc_mcq_top + '''
      if (topicId.startsWith('top-disab-') || topicId.startsWith('top-parent-') ||
          topicId.startsWith('top-dowry-') || topicId.startsWith('top-dv-') ||
          topicId.startsWith('top-posh-') || topicId.startsWith('top-pcpndt-') ||
          topicId.startsWith('top-mtp-') || topicId.startsWith('top-irwa-') ||
          topicId.startsWith('top-pocso-')) {
        return (global.SOCIAL_MCQS || []).filter(m => m.topicId === topicId);
      }'''
content = content.replace(cpc_mcq_top, soc_mcq_top, 1)

# 9. getMCQsByChapter
cpc_mcq_ch = "      if (chapterId.startsWith('ch-cpc-')) return (global.CPC_MCQS || []).filter(m => m.chapterId === chapterId);"
soc_mcq_ch = cpc_mcq_ch + '''
      if (chapterId.startsWith('ch-soc-')) return (global.SOCIAL_MCQS || []).filter(m => m.chapterId === chapterId);'''
content = content.replace(cpc_mcq_ch, soc_mcq_ch, 1)

# 10. getPYQsBySubject
cpc_pyq = "      if (subjectId === 'law-cpc') return global.CPC_PYQ_MAPPING || [];"
soc_pyq = cpc_pyq + "\n      if (subjectId && subjectId.startsWith('soc-')) return (global.SOCIAL_PYQ_MAPPING || []).filter(p => p.subjectId === subjectId);"
content = content.replace(cpc_pyq, soc_pyq, 1)

# 11. getPYQsByTopic
cpc_pyq_top = "      if (topicId.startsWith('top-cpc-')) return (global.CPC_PYQ_MAPPING || []).filter(p => p.topicId === topicId);"
soc_pyq_top = cpc_pyq_top + '''
      if (topicId.startsWith('top-disab-') || topicId.startsWith('top-parent-') ||
          topicId.startsWith('top-dowry-') || topicId.startsWith('top-dv-') ||
          topicId.startsWith('top-posh-') || topicId.startsWith('top-pcpndt-') ||
          topicId.startsWith('top-mtp-') || topicId.startsWith('top-irwa-') ||
          topicId.startsWith('top-pocso-')) {
        return (global.SOCIAL_PYQ_MAPPING || []).filter(p => p.topicId === topicId);
      }'''
content = content.replace(cpc_pyq_top, soc_pyq_top, 1)

# 12. getPYQsByChapter
cpc_pyq_ch = "      if (chapterId.startsWith('ch-cpc-')) return (global.CPC_PYQ_MAPPING || []).filter(p => p.chapterId === chapterId);"
soc_pyq_ch = cpc_pyq_ch + '''
      if (chapterId.startsWith('ch-soc-')) return (global.SOCIAL_PYQ_MAPPING || []).filter(p => p.chapterId === chapterId);'''
content = content.replace(cpc_pyq_ch, soc_pyq_ch, 1)

# 13. Add getSocialSectionsExplorer right after getCPCSectionsOrdersRules
cpc_explorer = '''    getCPCSectionsOrdersRules: function (query, type) {
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
    },'''

soc_explorer = cpc_explorer + '''

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
    },'''
content = content.replace(cpc_explorer, soc_explorer, 1)

# 14. Overview Stats:
old_stats = '''      const totalActiveChapters = 15 + 11 + 11 + 8 + 12 + 12 + 10 + 20; // 99
      const totalActiveTopics = 45 + 30 + 32 + 24 + 36 + 35 + 30 + 57; // 287
      const totalActiveMCQs = 480 + 240 + 260 + 240 + 360 + 360 + 280 + 400; // 2620
      const totalActivePYQs = (global.CONSTITUTION_PYQ_MAPPING || []).length +
                              (global.JURISPRUDENCE_PYQ_MAPPING || []).length +
                              (global.CONTRACT_PYQ_MAPPING || []).length +
                              (global.TPA_PYQ_MAPPING || []).length +
                              (global.CRIMINAL_PYQ_MAPPING || []).length +
                              (global.CRPC_PYQ_MAPPING || []).length +
                              (global.EVIDENCE_PYQ_MAPPING || []).length +
                              (global.CPC_PYQ_MAPPING || []).length; // 592

      const totalCompletedTopics = (constProg.completedTopics || 0) +
                                    (jurProg.completedTopics || 0) +
                                    (cntProg.completedTopics || 0) +
                                    (tpaProg.completedTopics || 0) +
                                    (crimProg.completedTopics || 0) +
                                    (crpcProg.completedTopics || 0) +
                                    (eviProg.completedTopics || 0) +
                                    (cpcProg.completedTopics || 0);'''

new_stats = '''      let totalActiveChapters = 0;
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
                              (global.SOCIAL_PYQ_MAPPING || []).length;'''
content = content.replace(old_stats, new_stats, 1)

# 15. renderSubjectCards paper/social filtering
old_filter = '''      if (filter === 'paper1') {
        filtered = filtered.filter(s => s.paper === 'Paper I');
      } else if (filter === 'paper2') {
        filtered = filtered.filter(s => s.paper === 'Paper II');
      } else if (filter === 'active') {
        filtered = filtered.filter(s => s.status === 'active');
      } else if (filter === 'social') {
        filtered = filtered.filter(s => s.category === 'social_legislation');
      }'''

new_filter = '''      if (filter === 'paper1') {
        filtered = filtered.filter(s => s.paper.includes('Paper I') || s.paper === 'GK' || (s.id && s.id.startsWith('soc-')));
      } else if (filter === 'paper2') {
        filtered = filtered.filter(s => s.paper.includes('Paper II') || s.paper === 'LAW');
      } else if (filter === 'active') {
        filtered = filtered.filter(s => s.status === 'active');
      } else if (filter === 'social') {
        filtered = filtered.filter(s => s.category === 'social_legislation' || (s.id && s.id.startsWith('soc-')) || s.paper.includes('Social Legislation'));
      }'''
content = content.replace(old_filter, new_filter, 1)

with open('assets/learning/js/learning-engine.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated learning-engine.js successfully!')
