with open('assets/js/legal-search.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. allAcademyTopics
old_topics = '''    ...(window.EVIDENCE_TOPICS || []),
    ...(window.CPC_TOPICS || [])
  ];'''

new_topics = '''    ...(window.EVIDENCE_TOPICS || []),
    ...(window.CPC_TOPICS || []),
    ...(window.SOCIAL_TOPICS || [])
  ];'''

content = content.replace(old_topics, new_topics, 1)

# 2. allAcademyMCQs
old_mcqs = '''    ...(window.EVIDENCE_MCQS || []),
    ...(window.CPC_MCQS || [])
  ];'''

new_mcqs = '''    ...(window.EVIDENCE_MCQS || []),
    ...(window.CPC_MCQS || []),
    ...(window.SOCIAL_MCQS || [])
  ];'''

content = content.replace(old_mcqs, new_mcqs, 1)

# 3. getSubjectMeta
cpc_meta = '''    if (id.startsWith('top-cpc-') || id.startsWith('mcq-cpc-') || id.startsWith('ch-cpc-')) {
      return { id: 'law-cpc', name: 'Code of Civil Procedure, 1908' };
    }'''

soc_meta = cpc_meta + '''
    if (id.startsWith('top-disab-') || id.startsWith('mcq-disab-') || id.startsWith('ch-soc-disab-')) {
      return { id: 'soc-disabilities', name: 'Rights of Persons with Disabilities' };
    }
    if (id.startsWith('top-parent-') || id.startsWith('mcq-parent-') || id.startsWith('ch-soc-parent-')) {
      return { id: 'soc-parents', name: 'Maintenance & Welfare of Parents' };
    }
    if (id.startsWith('top-dowry-') || id.startsWith('mcq-dowry-') || id.startsWith('ch-soc-dowry-')) {
      return { id: 'soc-dowry', name: 'Dowry Prohibition Act' };
    }
    if (id.startsWith('top-dv-') || id.startsWith('mcq-dv-') || id.startsWith('ch-soc-dv-')) {
      return { id: 'soc-domestic-violence', name: 'Protection of Women from Domestic Violence' };
    }
    if (id.startsWith('top-posh-') || id.startsWith('mcq-posh-') || id.startsWith('ch-soc-posh-')) {
      return { id: 'soc-posh', name: 'POSH Act (Workplace Harassment)' };
    }
    if (id.startsWith('top-pcpndt-') || id.startsWith('mcq-pcpndt-') || id.startsWith('ch-soc-pcpndt-')) {
      return { id: 'soc-pcpndt', name: 'PCPNDT Act' };
    }
    if (id.startsWith('top-mtp-') || id.startsWith('mcq-mtp-') || id.startsWith('ch-soc-mtp-')) {
      return { id: 'soc-mtp', name: 'Medical Termination of Pregnancy' };
    }
    if (id.startsWith('top-irwa-') || id.startsWith('mcq-irwa-') || id.startsWith('ch-soc-irwa-')) {
      return { id: 'soc-indecent-rep', name: 'Indecent Representation of Women' };
    }
    if (id.startsWith('top-pocso-') || id.startsWith('mcq-pocso-') || id.startsWith('ch-soc-pocso-')) {
      return { id: 'soc-pocso', name: 'POCSO Act' };
    }'''

content = content.replace(cpc_meta, soc_meta, 1)

with open('assets/js/legal-search.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated legal-search.js successfully!')
