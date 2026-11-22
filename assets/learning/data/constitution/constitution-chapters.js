/**
 * Judicial Learning Academy — Indian Constitution Chapters
 * 15 Authoritative Chapters structured for UP PCS-J Preliminary & Mains Examination.
 */
(function() {
  'use strict';

  const CONSTITUTION_CHAPTERS = [
    {
      id: 'ch-01',
      number: 1,
      title: 'Historical Background',
      subtitle: 'Constitutional Evolution Under British Rule (1773–1947)',
      articleRange: 'Pre-Constitutional Acts',
      description: 'Evolution of Indian constitutional machinery from the Regulating Act of 1773, Pitt’s India Act, Charter Acts, Government of India Acts of 1858, 1909, 1919, 1935, to the Indian Independence Act, 1947.',
      topicsCount: 3,
      mcqsCount: 30,
      pyqsCount: 8,
      weightage: 'High',
      icon: '📜',
      diagramId: 'diag-historical-timeline'
    },
    {
      id: 'ch-02',
      number: 2,
      title: 'Making of the Constitution & Salient Features',
      subtitle: 'Constituent Assembly, Drafting & Structural Hallmarks',
      articleRange: 'Foundational Framework',
      description: 'Composition and working of the Constituent Assembly, Drafting Committee, major sources borrowed from global constitutions, and salient structural features of the Indian Constitution.',
      topicsCount: 3,
      mcqsCount: 30,
      pyqsCount: 12,
      weightage: 'High',
      icon: '🏛️',
      diagramId: 'diag-sources-features'
    },
    {
      id: 'ch-03',
      number: 3,
      title: 'The Preamble',
      subtitle: 'Key to the Constitution, Philosophy & Enforceability',
      articleRange: 'Preamble',
      description: 'The ideological compass: Sovereign, Socialist, Secular, Democratic, Republic, Justice, Liberty, Equality, Fraternity; Berubari Union, Kesavananda Bharati, and 42nd Amendment, 1976.',
      topicsCount: 2,
      mcqsCount: 25,
      pyqsCount: 10,
      weightage: 'Very High',
      icon: '⚖️',
      diagramId: 'diag-preamble-pillars'
    },
    {
      id: 'ch-04',
      number: 4,
      title: 'The Union and its Territory',
      subtitle: 'Federation of States, Reorganisation & Cession',
      articleRange: 'Articles 1–4',
      description: 'Name and territory of the Union, admission or establishment of new states, formation of new states, alteration of areas, boundaries or names under Article 3, and constitutional cession jurisprudence.',
      topicsCount: 2,
      mcqsCount: 25,
      pyqsCount: 6,
      weightage: 'Medium',
      icon: '🗺️',
      diagramId: 'diag-state-reorganisation'
    },
    {
      id: 'ch-05',
      number: 5,
      title: 'Citizenship',
      subtitle: 'Constitutional Provisions & Statutory Framework',
      articleRange: 'Articles 5–11',
      description: 'Citizenship at the commencement of the Constitution, rights of migrants from Pakistan, overseas citizens, Article 11 parliamentary supremacy, and Citizenship Act, 1955 principles.',
      topicsCount: 2,
      mcqsCount: 25,
      pyqsCount: 5,
      weightage: 'Medium',
      icon: '🆔',
      diagramId: 'diag-citizenship-modes'
    },
    {
      id: 'ch-06',
      number: 6,
      title: 'Fundamental Rights',
      subtitle: 'Part III — The Magna Carta of India',
      articleRange: 'Articles 12–35',
      description: 'Definition of State (Art. 12), Laws inconsistent with FRs (Art. 13), Right to Equality (Arts. 14–18), Right to Freedom (Arts. 19–22), Against Exploitation (Arts. 23–24), Freedom of Religion (Arts. 25–28), Educational Rights (Arts. 29–30), and Constitutional Remedies & Writs (Art. 32).',
      topicsCount: 6,
      mcqsCount: 55,
      pyqsCount: 32,
      weightage: 'Critical',
      icon: '🛡️',
      diagramId: 'diag-fr-hierarchy'
    },
    {
      id: 'ch-07',
      number: 7,
      title: 'Directive Principles of State Policy',
      subtitle: 'Part IV — Socio-Economic Justice & Directive Mandates',
      articleRange: 'Articles 36–51',
      description: 'Classification into Socialistic, Gandhian, and Liberal-Intellectual principles; non-justiciable character (Art. 37); Uniform Civil Code (Art. 44); and harmonisation doctrine with Fundamental Rights.',
      topicsCount: 3,
      mcqsCount: 30,
      pyqsCount: 14,
      weightage: 'Very High',
      icon: '🧭',
      diagramId: 'diag-dpsp-classification'
    },
    {
      id: 'ch-08',
      number: 8,
      title: 'Fundamental Duties',
      subtitle: 'Part IVA — Moral & Civic Obligations of Citizens',
      articleRange: 'Article 51A',
      description: 'Origin via Swaran Singh Committee and 42nd Constitutional Amendment Act, 1976; the 11 fundamental duties; 86th Amendment Act, 2002; non-justiciability, and judicial usage as interpretative tools.',
      topicsCount: 2,
      mcqsCount: 25,
      pyqsCount: 7,
      weightage: 'High',
      icon: '🤝',
      diagramId: 'diag-duties-overview'
    },
    {
      id: 'ch-09',
      number: 9,
      title: 'The Union Executive',
      subtitle: 'President, Vice-President, Prime Minister & Council of Ministers',
      articleRange: 'Articles 52–78',
      description: 'Election, qualification, tenure, and impeachment of President; executive powers, ordinance-making power (Art. 123), pardoning power (Art. 72); Council of Ministers and collective responsibility (Art. 75); Attorney-General (Art. 76).',
      topicsCount: 3,
      mcqsCount: 35,
      pyqsCount: 15,
      weightage: 'Very High',
      icon: '👑',
      diagramId: 'diag-executive-powers'
    },
    {
      id: 'ch-10',
      number: 10,
      title: 'The Union Parliament',
      subtitle: 'Bicameral Legislature, Procedures & Parliamentary Privileges',
      articleRange: 'Articles 79–122',
      description: 'Composition of Rajya Sabha and Lok Sabha; parliamentary sessions, prorogation, and dissolution; Speaker and Chairman; Legislative procedures, Ordinary Bills, Money Bills (Art. 110), Financial Bills; Parliamentary Privileges (Art. 105).',
      topicsCount: 3,
      mcqsCount: 35,
      pyqsCount: 16,
      weightage: 'Very High',
      icon: '🏛️',
      diagramId: 'diag-parliament-bills'
    },
    {
      id: 'ch-11',
      number: 11,
      title: 'State Government & Local Self-Governance',
      subtitle: 'Governor, State Legislature, Panchayats & Municipalities',
      articleRange: 'Articles 152–213 & 243–243ZG',
      description: 'Governor’s appointment, constitutional position, discretionary powers, and ordinance power (Art. 213); State Legislature; Advocate-General (Art. 165); 73rd and 74th Amendments (Parts IX and IXA).',
      topicsCount: 4,
      mcqsCount: 30,
      pyqsCount: 9,
      weightage: 'High',
      icon: '🌱',
      diagramId: 'diag-local-governance'
    },
    {
      id: 'ch-12',
      number: 12,
      title: 'The Union & State Judiciary',
      subtitle: 'Supreme Court, High Courts & Subordinate Courts',
      articleRange: 'Articles 124–147 & 214–237',
      description: 'Supreme Court appointments (Collegium system), Original (Art. 131), Appellate (Arts. 132–134), Special Leave Petitions (Art. 136), Advisory jurisdiction (Art. 143), Complete Justice (Art. 142), Contempt of Court, High Courts writ jurisdiction (Art. 226).',
      topicsCount: 4,
      mcqsCount: 45,
      pyqsCount: 22,
      weightage: 'Critical',
      icon: '⚖️',
      diagramId: 'diag-judicial-hierarchy'
    },
    {
      id: 'ch-13',
      number: 13,
      title: 'Emergency Provisions',
      subtitle: 'Part XVIII — National, State & Financial Emergencies',
      articleRange: 'Articles 352–360',
      description: 'National Emergency (Art. 352 grounds, approval, parliamentary control, effect on FRs Arts. 358-359); State Emergency / President’s Rule (Art. 356, S.R. Bommai guidelines); Financial Emergency (Art. 360); 44th Amendment safeguards.',
      topicsCount: 2,
      mcqsCount: 25,
      pyqsCount: 11,
      weightage: 'Very High',
      icon: '🚨',
      diagramId: 'diag-emergency-comparison'
    },
    {
      id: 'ch-14',
      number: 14,
      title: 'Amendment of the Constitution',
      subtitle: 'Article 368 & The Basic Structure Doctrine',
      articleRange: 'Article 368',
      description: 'Constituent power of Parliament, types of amendments (Simple, Special, Special with State ratification); Shankari Prasad to Sajjan Singh, Golaknath, 24th Amendment, Kesavananda Bharati, Minerva Mills, and Basic Structure Doctrine.',
      topicsCount: 2,
      mcqsCount: 30,
      pyqsCount: 14,
      weightage: 'Critical',
      icon: '✍️',
      diagramId: 'diag-amendment-process'
    },
    {
      id: 'ch-15',
      number: 15,
      title: 'Federal Relations, Schedules & Constitutional Bodies',
      subtitle: 'Centre-State Relations, 12 Schedules & Independent Commissions',
      articleRange: 'Part XI, XII, Schedules 1–12, Arts. 280, 324, 315, 148',
      description: 'Legislative relations (Seventh Schedule, Union/State/Concurrent lists, doctrine of territorial nexus, pith and substance, repugnancy Art. 254); Election Commission (Art. 324); UPSC & State PSCs (Arts. 315–323); Finance Commission (Art. 280); CAG (Arts. 148–151).',
      topicsCount: 4,
      mcqsCount: 35,
      pyqsCount: 14,
      weightage: 'Very High',
      icon: '📊',
      diagramId: 'diag-federal-distribution'
    }
  ];

  // Expose to global/window
  const g = typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this);
  g.CONSTITUTION_CHAPTERS = CONSTITUTION_CHAPTERS;
  g.CONSTITUTION_CHAPTERS.chapters = CONSTITUTION_CHAPTERS;

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONSTITUTION_CHAPTERS;
  }
})();
