with open('CHANGELOG.md', 'r', encoding='utf-8') as f:
    text = f.read()

phase5_entry = '''## [3.1.5] — Phase 5 — 2026-11-22
*Tag: V3.1 Phase 5 — Complete Social Legislation Learning Academy, Nine Special Acts, Thematic Study Centre & Statutory Explorer*

### Added
- **Complete Social Legislation Learning Academy (Paper I — General Knowledge · 9 Acts):**
  - Activated all nine special welfare, non-discrimination, and protective enactments under official UP PCS-J syllabus (UPPSC Advt. A-6/E-1/2026):
    1. Rights of Persons with Disabilities Act, 2016 (`soc-disabilities` - 3 Ch, 9 Top, 50 MCQs, 4 PYQs, 2 SVG Schematics)
    2. Maintenance & Welfare of Parents and Senior Citizens Act, 2007 (`soc-parents` - 3 Ch, 9 Top, 50 MCQs, 1 PYQ, 2 SVG Schematics)
    3. Dowry Prohibition Act, 1961 (`soc-dowry` - 3 Ch, 9 Top, 50 MCQs, 5 PYQs, 2 SVG Schematics)
    4. Protection of Women from Domestic Violence Act, 2005 (`soc-domestic-violence` - 3 Ch, 9 Top, 50 MCQs, 2 PYQs, 2 SVG Schematics)
    5. Sexual Harassment of Women at Workplace (POSH) Act, 2013 (`soc-posh` - 3 Ch, 9 Top, 50 MCQs, 1 PYQ, 2 SVG Schematics)
    6. Indecent Representation of Women (Prohibition) Act, 1986 (`soc-indecent-rep` - 3 Ch, 9 Top, 45 MCQs, 3 PYQs, 2 SVG Schematics)
    7. Pre-Conception & Pre-Natal Diagnostic Techniques Act, 1994 (`soc-pcpndt` - 3 Ch, 9 Top, 50 MCQs, 2 PYQs, 2 SVG Schematics)
    8. Medical Termination of Pregnancy Act, 1971 as amended 2021 (`soc-mtp` - 3 Ch, 9 Top, 50 MCQs, 3 PYQs, 2 SVG Schematics)
    9. Protection of Children from Sexual Offences Act, 2012 as amended 2019 (`soc-pocso` - 4 Ch, 12 Top, 60 MCQs, 2 PYQs, 2 SVG Schematics)
  - Total active academy inventory expanded to **17 Subjects**, **127 Chapters**, **373 Topics**, **373 Authored Concepts**, **3,075 Practice MCQs**, **615 Mapped Authentic PYQs**, and **90 Academic SVG Schematics**.
- **Social Legislation Study Centre (`learning-academy.html`):**
  - Added dedicated showcase section organized into three candidate-approved thematic clusters: Group A (Equality, Inclusion & Welfare), Group B (Protection of Women), and Group C (Reproductive Health & Child Protection).
  - Each card equipped with direct *Study Topics*, *Practise MCQs*, and *Detailed Analytics* action triggers.
  - Added chapter selector pills for all 9 social Acts.
- **Social Legislation Statutory Provisions Explorer (`assets/learning/data/social/social-sections-explorer.js`):**
  - 98 curated high-yield statutory entries across all 9 Acts, featuring plain English rules, prerequisites, exceptions, penalties, India Code links, and tailored UP Exam Tips (bringing total statutory explorer entries to 181).
- **18 Original Academic Vector SVG Schematics (`assets/learning/images/diagrams/`):**
  - Two custom vector schematics per Act: RPwD rights & accessibility, Parents tribunal flow & maintenance comparison, Dowry offences & customary gifts, Domestic Violence remedies hierarchy & shared household, POSH complaint inquiry & IC vs LC, PCPNDT regulatory architecture & prohibited conduct, MTP gestational framework & consent matrix, IRWA prohibitions & enforcement powers, POCSO protection framework & Special Court trial sequence.
- **Targeted Civil Procedure Code Refinement:**
  - Added clear procedural stream distinctions to the 14-stage Civil Suit Journey (`civil-suit-journey.html`), tagging standard suit progression vs. parallel execution / interlocutory streams.
  - Updated disclaimer in `cpc-sections-orders-rules.js` and `civil-suit-journey.html` clarifying their curated nature.
- **Engines & Multi-Corpus Search Integration:**
  - `LearningEngine` (`assets/learning/js/learning-engine.js`): Added social chapter, topic, concept, MCQ, and PYQ resolvers, `getSocialSectionsExplorer()`, and dynamic 17-subject stats aggregation.
  - `ConceptRenderer` (`assets/learning/js/concept-renderer.js`): Implemented unified `resolveSubjectId()` supporting all 9 social prefixes and statutory blueprint titles.
  - `LearningStorage` (`assets/learning/js/learning-storage.js`): Added progress tracking, mistake queue filtering, and bookmarking for all 9 social Acts.
  - `legal-search.js` (`assets/js/legal-search.js`): Indexed social topics and MCQs in universal multi-corpus smart search.
- **Automated Test Suites:**
  - `scripts/validate_learning_academy.py` updated to 15 test groups and 58 test assertions covering all 17 active subjects, 127 chapters, 373 topics, 3,075 MCQs, 615 PYQs, 90 diagrams, and 98 social explorer entries (100% pass rate).
  - `scripts/validate_production.py` verified with 21/21 passes.

---

'''

text = text.replace('## [3.1.4] — Phase 4 — 2026-11-22', phase5_entry + '## [3.1.4] — Phase 4 — 2026-11-22')

with open('CHANGELOG.md', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated CHANGELOG.md successfully!')
