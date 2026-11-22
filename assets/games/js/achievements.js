/**
 * LEGAL BRAIN ARENA — JUDICIAL ACHIEVEMENTS ENGINE
 * Badges, milestones, and honorifics based on demonstrated mastery
 */
(function() {
  'use strict';

  const ACHIEVEMENTS = [
    {
      id: 'first_trial',
      title: 'First Step in Court',
      description: 'Complete your first practice session in the Legal Brain Arena.',
      icon: '⚖',
      xpReward: 50,
      condition: (state, result) => state.gamesPlayed >= 1
    },
    {
      id: 'photographic_counsel',
      title: 'Photographic Counsel',
      description: 'Complete a Legal Memory Match session with 90% or higher accuracy.',
      icon: '🧠',
      xpReward: 100,
      condition: (state, result) => result.game === 'memory-match' && result.accuracy >= 90
    },
    {
      id: 'speedy_advocate',
      title: 'Rapid Advocate',
      description: 'Score 150 points or higher in a single Section Sprint challenge.',
      icon: '⚡',
      xpReward: 120,
      condition: (state, result) => result.game === 'section-sprint' && result.score >= 150
    },
    {
      id: 'streak_10',
      title: 'Unbroken Chain',
      description: 'Achieve a continuous 10-answer correct streak in Section Sprint.',
      icon: '🔥',
      xpReward: 150,
      condition: (state, result) => result.game === 'section-sprint' && (result.longestStreak >= 10)
    },
    {
      id: 'jurisprudence_master',
      title: 'Jurisprudential Master',
      description: 'Complete an Intermediate or higher Memory Match with 100% accuracy and 0 hints.',
      icon: '📜',
      xpReward: 200,
      condition: (state, result) => result.game === 'memory-match' && ['intermediate', 'advanced', 'expert'].includes(result.difficulty) && result.accuracy === 100 && result.hintsUsed === 0
    },
    {
      id: 'daily_discipline',
      title: 'Daily Discipline',
      description: 'Maintain a 3-day consecutive study and training streak.',
      icon: '📅',
      xpReward: 250,
      condition: (state, result) => state.streak.current >= 3
    },
    {
      id: 'statutory_command',
      title: 'Statutory Command',
      description: 'Correctly recall 30 or more statutory sections in the Arena.',
      icon: '§',
      xpReward: 200,
      condition: (state, result) => state.subjectMastery.bns.correct >= 30
    },
    {
      id: 'bench_aspirant',
      title: 'Court of Record',
      description: 'Attain Level 3 (Section Master) in the Legal Brain Arena.',
      icon: '🏛',
      xpReward: 300,
      condition: (state, result) => state.xp >= 1500
    },
    {
      id: 'first_investigation',
      title: 'First Investigation',
      description: 'Complete your first criminal case investigation in Legal Detective.',
      icon: '🔍',
      xpReward: 100,
      condition: (state, result) => result.game === 'legal-detective'
    },
    {
      id: 'evidence_expert',
      title: 'Master of Evidence',
      description: 'Connect all clues to their precise legal issues on the Evidence Board with full marks.',
      icon: '📋',
      xpReward: 150,
      condition: (state, result) => result.game === 'legal-detective' && result.rubric && result.rubric.evidenceBoard === 20
    },
    {
      id: 'deduction_master',
      title: 'Master Deduction',
      description: 'Score 90 or more points on an Advanced tier criminal investigation.',
      icon: '⚖',
      xpReward: 250,
      condition: (state, result) => result.game === 'legal-detective' && result.difficulty === 'advanced' && result.score >= 90
    },
    {
      id: 'first_order',
      title: 'First Judicial Order',
      description: 'Preside over a court hearing and deliver your first reasoned judicial order.',
      icon: '📜',
      xpReward: 100,
      condition: (state, result) => result.game === 'courtroom'
    },
    {
      id: 'judicial_scholar',
      title: 'Judicial Scholar',
      description: 'Attain a score of 90 or higher in an Advanced Courtroom hearing.',
      icon: '🏛',
      xpReward: 250,
      condition: (state, result) => result.game === 'courtroom' && result.difficulty === 'advanced' && result.score >= 90
    },
    {
      id: 'procedural_master',
      title: 'Procedural Mastery',
      description: 'Correctly frame legal issues and assemble all valid elements in the Reasoned Order Builder.',
      icon: '🎓',
      xpReward: 200,
      condition: (state, result) => result.game === 'courtroom' && result.rubric && result.rubric.proceduralSoundness >= 23
    },

    // === PHASE 3: COGNITIVE PUZZLE & VOCABULARY HONORS ===
    {
      id: 'first_crossword',
      title: 'First Crossword',
      description: 'Solve and complete your first crossword puzzle in the Lexicon Chamber.',
      icon: '🔠',
      xpReward: 100,
      condition: (state, result) => result.game === 'crossword'
    },
    {
      id: 'lexicon_explorer',
      title: 'Lexicon Explorer',
      description: 'Successfully complete 5 unique crossword puzzles across any collection.',
      icon: '📚',
      xpReward: 150,
      condition: (state, result) => state.crossword && Object.keys(state.crossword.completedPuzzles || {}).length >= 5
    },
    {
      id: 'crossword_master',
      title: 'Crossword Master',
      description: 'Complete an Advanced crossword puzzle with 100% accuracy and 0 hints.',
      icon: '🏆',
      xpReward: 250,
      condition: (state, result) => result.game === 'crossword' && result.difficulty === 'advanced' && result.accuracy === 100 && result.hintsUsed === 0
    },
    {
      id: 'latin_maxims_scholar',
      title: 'Latin Maxims Scholar',
      description: 'Complete a Latin Maxims crossword puzzle or decode Latin maxims in Code Breaker.',
      icon: '📜',
      xpReward: 150,
      condition: (state, result) => (result.game === 'crossword' && result.collection === 'Legal Maxims') || (result.game === 'scramble' && result.mode === 'maxims')
    },
    {
      id: 'first_code_breaker',
      title: 'First Code Breaker',
      description: 'Decipher your first scrambled legal word in the Code Breaker laboratory.',
      icon: '🔓',
      xpReward: 100,
      condition: (state, result) => result.game === 'scramble'
    },
    {
      id: 'vocabulary_virtuoso',
      title: 'Vocabulary Virtuoso',
      description: 'Achieve a 10-word correct decoding streak in Word Scramble.',
      icon: '⚡',
      xpReward: 200,
      condition: (state, result) => result.game === 'scramble' && result.streak >= 10
    },
    {
      id: 'manuscript_unlocked',
      title: 'Manuscript Unlocked',
      description: 'Unlock and decode an entire thematic legal chapter in Mystery Manuscript mode.',
      icon: '🗝',
      xpReward: 250,
      condition: (state, result) => (result.game === 'scramble' && result.mode === 'manuscript' && result.completed) || (state.scramble && Object.keys(state.scramble.unlockedManuscripts || {}).length >= 1)
    },
    {
      id: 'legal_language_master',
      title: 'Legal Language Master',
      description: 'Master 50 unique legal terms across the Lexicon Chamber and Code Breaker.',
      icon: '👑',
      xpReward: 300,
      condition: (state, result) => {
        const cwCount = state.crossword ? Object.keys(state.crossword.completedPuzzles || {}).length * 5 : 0;
        const scCount = state.scramble ? Object.keys(state.scramble.completedWords || {}).length : 0;
        return (cwCount + scCount) >= 50;
      }
    },
    // --- Phase 4: Legal Myth Buster Achievements (8 items) ---
    {
      id: 'first_truth',
      title: 'Chamber Initiate',
      description: 'Complete your first practice session in the Chamber of Truth (Legal Myth Buster).',
      icon: '⚖️',
      xpReward: 50,
      condition: (state, result) => (result && result.game === 'myth-buster') || (state.history && state.history.some(h => h.game === 'myth-buster'))
    },
    {
      id: 'myth_slayer',
      title: 'Myth Buster',
      description: 'Accurately expose 10 statutory misconceptions in Legal Myth Buster.',
      icon: '🚫',
      xpReward: 100,
      condition: (state, result) => (state.mythBuster && state.mythBuster.mythsBusted >= 10) || (state.history && state.history.filter(h => h.game === 'myth-buster' && h.correct >= 5).length >= 2)
    },
    {
      id: 'statutory_purist',
      title: 'Statutory Purist',
      description: 'Achieve a continuous 10-answer correct streak in Legal Myth Buster.',
      icon: '🔥',
      xpReward: 150,
      condition: (state, result) => (result && result.game === 'myth-buster' && result.longestStreak >= 10)
    },
    {
      id: 'error_hunter',
      title: 'Error Hunter',
      description: 'Successfully pinpoint the flawed statutory phrase in Find the Legal Error mode.',
      icon: '🔍',
      xpReward: 120,
      condition: (state, result) => (result && result.game === 'myth-buster' && result.mode === 'find_error' && result.score >= 40)
    },
    {
      id: 'statutory_drafter',
      title: 'Legislative Drafter',
      description: 'Accurately select the authentic statutory correction in Correct the Law mode.',
      icon: '✍️',
      xpReward: 140,
      condition: (state, result) => (result && result.game === 'myth-buster' && result.mode === 'correct_law' && result.score >= 50)
    },
    {
      id: 'transition_virtuoso',
      title: 'Reform Virtuoso',
      description: 'Master 8 statutory transitions from IPC/CrPC/IEA to 2024 Sanhitas in Old Law vs New Law.',
      icon: '🔄',
      xpReward: 160,
      condition: (state, result) => (result && result.game === 'myth-buster' && result.mode === 'old_vs_new' && result.score >= 60)
    },
    {
      id: 'conviction_titan',
      title: 'Unshakeable Conviction',
      description: 'Score 100+ points in Confidence Challenge with high judicial wagers.',
      icon: '⚡',
      xpReward: 180,
      condition: (state, result) => (result && result.game === 'myth-buster' && result.mode === 'confidence_challenge' && result.score >= 100)
    },
    {
      id: 'grand_trial_champion',
      title: 'Grand Trial Champion',
      description: 'Conquer The Grand Truth Trial with 80% or higher accuracy across 20 mixed propositions.',
      icon: '🏆',
      xpReward: 250,
      condition: (state, result) => (result && result.game === 'myth-buster' && result.mode === 'grand_trial' && result.accuracy >= 80)
    },

    // --- Phase 4: Road to Judiciary Campaign Achievements (8 items) ---
    {
      id: 'campaign_commenced',
      title: "Aspirant's Commitment",
      description: 'Complete your first campaign mission on the Road to Judiciary.',
      icon: '🗺️',
      xpReward: 100,
      condition: (state, result) => state.journey && Object.keys(state.journey.completedMissions || {}).length >= 1
    },
    {
      id: 'citadel_ascended',
      title: 'Citadel Conqueror',
      description: 'Unlock Chapter 2: The Constitutional Citadel on the campaign map.',
      icon: '📜',
      xpReward: 150,
      condition: (state, result) => state.journey && (state.journey.unlockedChapters || []).includes('ch-02')
    },
    {
      id: 'fortress_commander',
      title: 'Fortress Commander',
      description: 'Unlock Chapter 3: The Criminal Fortress on the campaign map.',
      icon: '🛡️',
      xpReward: 180,
      condition: (state, result) => state.journey && (state.journey.unlockedChapters || []).includes('ch-03')
    },
    {
      id: 'vault_warden',
      title: 'Vault Master',
      description: 'Unlock Chapter 4: The Evidence Vault on the campaign map.',
      icon: '🔐',
      xpReward: 200,
      condition: (state, result) => state.journey && (state.journey.unlockedChapters || []).includes('ch-04')
    },
    {
      id: 'civil_magistrate',
      title: 'Civil District Leader',
      description: 'Unlock Chapter 5: The Civil Justice District on the campaign map.',
      icon: '⚖️',
      xpReward: 220,
      condition: (state, result) => state.journey && (state.journey.unlockedChapters || []).includes('ch-05')
    },
    {
      id: 'bureau_inquisitor',
      title: 'Bureau Inquisitor',
      description: 'Unlock Chapter 6: The Investigation Bureau on the campaign map.',
      icon: '🔎',
      xpReward: 250,
      condition: (state, result) => state.journey && (state.journey.unlockedChapters || []).includes('ch-06')
    },
    {
      id: 'bench_confirmed',
      title: 'Curriculum Confirmed',
      description: 'Complete 25 or more missions across the Road to Judiciary campaign.',
      icon: '👨‍⚖️',
      xpReward: 300,
      condition: (state, result) => state.journey && Object.keys(state.journey.completedMissions || {}).length >= 25
    },
    {
      id: 'judicial_elevation',
      title: 'Judicial Preparation Master',
      description: 'Complete all 36 missions across the 9 chapters of the Road to Judiciary curriculum.',
      icon: '👑',
      xpReward: 500,
      condition: (state, result) => state.journey && Object.keys(state.journey.completedMissions || {}).length >= 36
    }

  ];

  function showAchievementToast(ach) {
    const existing = document.getElementById('achievementToast');
    if (existing) existing.remove();

    const toast = document.createElement('div');
    toast.id = 'achievementToast';
    toast.className = 'achievement-toast';
    toast.innerHTML = `
      <div class="achievement-toast-icon">${ach.icon}</div>
      <div class="achievement-toast-body">
        <small class="eyebrow" style="color:#e7c88c">Achievement Unlocked!</small>
        <strong>${ach.title}</strong>
        <p>${ach.description}</p>
        <span class="badge" style="background:#e7c88c22;color:#e7c88c;font-size:11px">+${ach.xpReward} XP</span>
      </div>
    `;
    document.body.appendChild(toast);

    setTimeout(() => {
      toast.classList.add('show');
    }, 50);

    setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => toast.remove(), 400);
    }, 4500);
  }

  const AchievementsEngine = {
    getAll: function() {
      return ACHIEVEMENTS;
    },

    evaluate: function(state, latestResult) {
      if (!latestResult) return [];
      const newlyUnlocked = [];

      for (const ach of ACHIEVEMENTS) {
        if (!state.achievements.includes(ach.id)) {
          if (ach.condition(state, latestResult)) {
            state.achievements.push(ach.id);
            state.xp += ach.xpReward;
            newlyUnlocked.push(ach);
          }
        }
      }

      if (newlyUnlocked.length > 0) {
        window.GameStorage.saveArenaState(state);
        // Play sound
        if (window.GameAudio) window.GameAudio.playAchievement();
        // Show toasts sequentially
        newlyUnlocked.forEach((ach, index) => {
          setTimeout(() => showAchievementToast(ach), index * 4800);
        });
      }

      return newlyUnlocked;
    }
  };

  window.AchievementsEngine = AchievementsEngine;
  window.Achievements = AchievementsEngine;
})();
