with open('assets/learning/js/learning-storage.js', 'r', encoding='utf-8') as f:
    content = f.read()

cpc_block = '''      } else if (sId === 'law-cpc') {
        topicPrefix = 'top-cpc-';
        topics = global.CPC_TOPICS || [];
        mcqs = global.CPC_MCQS || [];
      }'''

soc_block = cpc_block + ''' else if (sId === 'soc-disabilities') {
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
      }'''

content = content.replace(cpc_block, soc_block, 1)

old_wrong = '''        if (topicPrefix === 'top-cpc-') return qId.includes('-cpc-') || qId.includes('cpc');
        return qId.includes('-const-') || qId.includes('const');'''

new_wrong = '''        if (topicPrefix === 'top-cpc-') return qId.includes('-cpc-') || qId.includes('cpc');
        if (topicPrefix.startsWith('top-') && topicPrefix !== 'top-const-') {
          const short = topicPrefix.replace('top-', '').replace('-', '');
          return qId.includes(topicPrefix) || qId.includes(short);
        }
        return qId.includes('-const-') || qId.includes('const');'''

# Replace in both subjectWrong and subjectBookmarks
content = content.replace(old_wrong, new_wrong)

with open('assets/learning/js/learning-storage.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated learning-storage.js successfully!')
