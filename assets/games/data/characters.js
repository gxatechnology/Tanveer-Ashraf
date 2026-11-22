/**
 * LEGAL BRAIN ARENA — CHARACTER MANIFEST (V3.0 Phase 2)
 * Complete recurring character specifications, dialogue styles, and assets
 */
(function() {
  'use strict';

  const CHARACTERS = {
    // === LEGAL DETECTIVE CHARACTERS ===
    'arjun': {
      id: 'arjun',
      name: 'Detective Arjun Rathore',
      shortName: 'Det. Arjun',
      role: 'Lead Investigator',
      age: 38,
      game: 'legal-detective',
      portrait: 'assets/games/images/characters/detective/arjun.svg',
      voicePitch: 0.95,
      voiceRate: 1.0,
      personality: 'Analytical, disciplined, intelligent and methodical.',
      dialogueStyle: 'Direct, focused on material facts, sequence of events, and objective clues.',
      themeColor: '#dfbf80',
      badgeColor: '#1a3652'
    },
    'meera': {
      id: 'meera',
      name: 'Dr. Meera Sen',
      shortName: 'Dr. Meera',
      role: 'Evidence Analyst',
      age: 32,
      game: 'legal-detective',
      portrait: 'assets/games/images/characters/detective/meera.svg',
      voicePitch: 1.15,
      voiceRate: 1.05,
      personality: 'Precise, scientific and logical.',
      dialogueStyle: 'Focuses on chain of custody, forensic contradictions, document authenticity, and digital traces.',
      themeColor: '#2fe0c8',
      badgeColor: '#0c4f48'
    },
    'kabir': {
      id: 'kabir',
      name: 'Adv. Kabir Mehta',
      shortName: 'Adv. Kabir',
      role: 'Legal Advisor',
      age: 36,
      game: 'legal-detective',
      portrait: 'assets/games/images/characters/detective/kabir.svg',
      voicePitch: 1.0,
      voiceRate: 0.98,
      personality: 'Calm, knowledgeable and detail-oriented.',
      dialogueStyle: 'Cites statutory provisions (BNS, BSA), tests ingredient completeness, and warns against premature leaps of suspicion.',
      themeColor: '#e7c88c',
      badgeColor: '#172e45'
    },
    'rohan': {
      id: 'rohan',
      name: 'Officer Rohan Verma',
      shortName: 'Officer Rohan',
      role: 'Field Officer',
      age: 29,
      game: 'legal-detective',
      portrait: 'assets/games/images/characters/detective/rohan.svg',
      voicePitch: 1.05,
      voiceRate: 1.1,
      personality: 'Energetic, observant and direct.',
      dialogueStyle: 'Presents ground reality, witness demeanor, timelines, and newly discovered physical exhibits.',
      themeColor: '#cbd5e1',
      badgeColor: '#24384a'
    },

    // === BE THE JUDGE CHARACTERS ===
    'vikram': {
      id: 'vikram',
      name: 'Justice Vikram Sahay',
      shortName: 'Justice Sahay',
      role: 'Judicial Mentor',
      age: 58,
      game: 'courtroom',
      portrait: 'assets/games/images/characters/courtroom/vikram.svg',
      voicePitch: 0.85,
      voiceRate: 0.92,
      personality: 'Dignified, erudite, objective and patient.',
      dialogueStyle: 'Guides judicial reasoning, demands distinction between suspicion and proof, and evaluates order soundness.',
      themeColor: '#dfbf80',
      badgeColor: '#080a0c'
    },
    'ananya': {
      id: 'ananya',
      name: 'Adv. Ananya Rao',
      shortName: 'Adv. Ananya (Prosecutor)',
      role: 'Public Prosecutor',
      age: 35,
      game: 'courtroom',
      portrait: 'assets/games/images/characters/courtroom/ananya.svg',
      voicePitch: 1.1,
      voiceRate: 1.02,
      personality: 'Formidable, articulate, persuasive and relentless.',
      dialogueStyle: 'Emphasizes criminal ingredients, state interest, victim safety, and strict statutory penalties.',
      themeColor: '#a9dcd6',
      badgeColor: '#142c46'
    },
    'aditya': {
      id: 'aditya',
      name: 'Adv. Aditya Malhotra',
      shortName: 'Adv. Aditya (Defence)',
      role: 'Defence Counsel',
      age: 39,
      game: 'courtroom',
      portrait: 'assets/games/images/characters/courtroom/aditya.svg',
      voicePitch: 0.98,
      voiceRate: 1.0,
      personality: 'Sharp, skeptical, tenacious and legally agile.',
      dialogueStyle: 'Challenges evidentiary admissibility, raises reasonable doubt, and argues constitutional liberties.',
      themeColor: '#dfbf80',
      badgeColor: '#181c20'
    },
    'nandini': {
      id: 'nandini',
      name: 'Nandini Sharma',
      shortName: 'Court Clerk Nandini',
      role: 'Court Clerk',
      age: 30,
      game: 'courtroom',
      portrait: 'assets/games/images/characters/courtroom/nandini.svg',
      voicePitch: 1.12,
      voiceRate: 1.0,
      personality: 'Organized, respectful, meticulous and clear.',
      dialogueStyle: 'Calls cause list numbers, presents formal pleadings, and administers exhibits and procedural transitions.',
      themeColor: '#fef0c7',
      badgeColor: '#193b58'
    },

    // === COGNITIVE PUZZLE & VOCABULARY CHARACTERS (V3.0 PHASE 3) ===
    'kavita': {
      id: 'kavita',
      name: 'Prof. Kavita Sharma',
      shortName: 'Prof. Kavita',
      role: 'Legal Vocabulary Mentor',
      age: 46,
      game: 'crossword',
      portrait: 'assets/games/images/characters/crossword/kavita.svg',
      voicePitch: 1.08,
      voiceRate: 1.02,
      personality: 'Encouraging, knowledgeable, precise and approachable.',
      dialogueStyle: 'Explains complex terminology, Latin roots, contextual applications, and encourages intellectual precision.',
      themeColor: '#176d63',
      badgeColor: '#0e3a35'
    },
    'devendra': {
      id: 'devendra',
      name: 'Dr. Devendra Bose',
      shortName: 'Dr. Devendra',
      role: 'Keeper of the Legal Archives',
      age: 62,
      game: 'crossword',
      portrait: 'assets/games/images/characters/crossword/devendra.svg',
      voicePitch: 0.88,
      voiceRate: 0.94,
      personality: 'Thoughtful, curious, dignified and methodical.',
      dialogueStyle: 'Presents thematic archives, unearths historical jurisprudence, and guides aspirants through judicial lexicon vaults.',
      themeColor: '#dfbf80',
      badgeColor: '#1e2430'
    },

    // === LEGAL MASTERY & MYTH BUSTER CHARACTERS (V3.0 PHASE 4) ===
    'aditi': {
      id: 'aditi',
      name: 'Prof. Aditi Menon',
      shortName: 'Prof. Aditi',
      role: 'Expert in Legal Interpretation',
      age: 45,
      game: 'myth-buster',
      portrait: 'assets/games/images/characters/myth/aditi.svg',
      voicePitch: 1.05,
      voiceRate: 1.0,
      personality: 'Analytical, precise, patient and intellectually challenging.',
      dialogueStyle: 'Dissects legal misconceptions, explains statutory interpretation canons, highlights subtle exceptions, and probes constitutional nuance.',
      themeColor: '#1b3857',
      badgeColor: '#142c46'
    },
    'siddharth': {
      id: 'siddharth',
      name: 'Adv. Siddharth Kapoor',
      shortName: 'Adv. Siddharth',
      role: 'Legal Fact-Checking Mentor',
      age: 48,
      game: 'myth-buster',
      portrait: 'assets/games/images/characters/myth/siddharth.svg',
      voicePitch: 0.92,
      voiceRate: 0.96,
      personality: 'Observant, methodical, rigorous and evidence-oriented.',
      dialogueStyle: 'Presents disputed legal assertions, challenges lay legal assumptions with binding statutory text, and demands strict authority citations.',
      themeColor: '#b98a38',
      badgeColor: '#10141a'
    }
  };

  window.ARENA_CHARACTERS = CHARACTERS;
})();
