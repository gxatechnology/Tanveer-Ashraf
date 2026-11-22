with open('assets/learning/js/concept-renderer.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add resolveSubjectId helper
init_marker = "    currentFontSize: 16.5,\n"
helper_code = '''    currentFontSize: 16.5,

    resolveSubjectId: function (topic, chapter) {
      if (topic && topic.subjectId) return topic.subjectId;
      if (chapter && chapter.subjectId) return chapter.subjectId;
      if (!topic || !topic.id) return 'law-constitution';
      const tid = topic.id;
      if (tid.startsWith('top-disab-')) return 'soc-disabilities';
      if (tid.startsWith('top-parent-')) return 'soc-parents';
      if (tid.startsWith('top-dowry-')) return 'soc-dowry';
      if (tid.startsWith('top-dv-')) return 'soc-domestic-violence';
      if (tid.startsWith('top-posh-')) return 'soc-posh';
      if (tid.startsWith('top-pcpndt-')) return 'soc-pcpndt';
      if (tid.startsWith('top-mtp-')) return 'soc-mtp';
      if (tid.startsWith('top-irwa-')) return 'soc-indecent-rep';
      if (tid.startsWith('top-pocso-')) return 'soc-pocso';
      if (tid.startsWith('top-jur-')) return 'law-jurisprudence';
      if (tid.startsWith('top-cnt-')) return 'law-contract';
      if (tid.startsWith('top-tpa-')) return 'law-tpa';
      if (tid.startsWith('top-crim-')) return 'law-criminal';
      if (tid.startsWith('top-crpc-')) return 'law-crpc';
      if (tid.startsWith('top-evi-')) return 'law-evidence';
      if (tid.startsWith('top-cpc-')) return 'law-cpc';
      return 'law-constitution';
    },
'''
content = content.replace(init_marker, helper_code, 1)

# 2. In renderHeader
old_hdr_subject = '''      const subjectId = topic.subjectId || (chapter ? chapter.subjectId : null) ||
        (topic.id.startsWith('top-jur-') ? 'law-jurisprudence' :
         topic.id.startsWith('top-cnt-') ? 'law-contract' :
         topic.id.startsWith('top-tpa-') ? 'law-tpa' :
         topic.id.startsWith('top-crim-') ? 'law-criminal' :
         topic.id.startsWith('top-crpc-') ? 'law-crpc' :
         topic.id.startsWith('top-evi-') ? 'law-evidence' :
         topic.id.startsWith('top-cpc-') ? 'law-cpc' : 'law-constitution');
      const subject = global.LearningEngine ? global.LearningEngine.getSubjectById(subjectId) : null;
      const subjectName = subject ? subject.name : 'Indian Constitution';
      const paperName = subject ? `${subject.paper} Law` : 'Paper II Law';'''

new_hdr_subject = '''      const subjectId = ConceptRenderer.resolveSubjectId(topic, chapter);
      const subject = global.LearningEngine ? global.LearningEngine.getSubjectById(subjectId) : null;
      const subjectName = subject ? subject.name : 'Indian Constitution';
      const paperName = subject ? (subject.paperName || subject.paper || 'Paper II Law') : 'Paper II Law';'''

content = content.replace(old_hdr_subject, new_hdr_subject, 1)

# 3. In buildDetailedHtml
old_build_subject = '''      const subjectId = (topic && topic.subjectId) ||
        (topic && topic.id && topic.id.startsWith('top-jur-') ? 'law-jurisprudence' :
         topic && topic.id && topic.id.startsWith('top-cnt-') ? 'law-contract' :
         topic && topic.id && topic.id.startsWith('top-tpa-') ? 'law-tpa' :
         topic && topic.id && topic.id.startsWith('top-crim-') ? 'law-criminal' :
         topic && topic.id && topic.id.startsWith('top-crpc-') ? 'law-crpc' :
         topic && topic.id && topic.id.startsWith('top-evi-') ? 'law-evidence' :
         topic && topic.id && topic.id.startsWith('top-cpc-') ? 'law-cpc' : 'law-constitution');'''

new_build_subject = '''      const subjectId = ConceptRenderer.resolveSubjectId(topic);'''

content = content.replace(old_build_subject, new_build_subject, 1)

old_sec_title = '<h2 class="section-title"><span class="title-icon">🏛️</span> 1. ${subjectId === \'law-constitution\' ? \'Constitutional\' : (subjectId === \'law-cpc\' ? \'Procedural\' : \'Academic\')} Overview &amp; Blueprint</h2>'
new_sec_title = '<h2 class="section-title"><span class="title-icon">🏛️</span> 1. ${subjectId === \'law-constitution\' ? \'Constitutional\' : (subjectId === \'law-cpc\' ? \'Procedural\' : (subjectId && subjectId.startsWith(\'soc-\') ? \'Statutory\' : \'Academic\'))} Overview &amp; Blueprint</h2>'

content = content.replace(old_sec_title, new_sec_title, 1)

# 4. In renderNavigation
old_nav_subject = '''      const subjectId = currentTopic.subjectId ||
        (currentTopic.id.startsWith('top-jur-') ? 'law-jurisprudence' :
         currentTopic.id.startsWith('top-cnt-') ? 'law-contract' :
         currentTopic.id.startsWith('top-tpa-') ? 'law-tpa' :
         currentTopic.id.startsWith('top-crim-') ? 'law-criminal' :
         currentTopic.id.startsWith('top-crpc-') ? 'law-crpc' :
         currentTopic.id.startsWith('top-evi-') ? 'law-evidence' :
         currentTopic.id.startsWith('top-cpc-') ? 'law-cpc' : 'law-constitution');'''

new_nav_subject = '''      const subjectId = ConceptRenderer.resolveSubjectId(currentTopic);'''

content = content.replace(old_nav_subject, new_nav_subject, 1)

with open('assets/learning/js/concept-renderer.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated concept-renderer.js successfully!')
