# Append 16 Phase 4 achievements to assets/games/js/achievements.js
import os

ach_path = os.path.join("assets", "games", "js", "achievements.js")
with open(ach_path, "r", encoding="utf-8") as f:
    text = f.read()

new_achievements = """
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
      title: "Aspirant's Oath",
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
      title: 'Bench Confirmed',
      description: 'Complete 25 or more missions across the Road to Judiciary campaign.',
      icon: '👨‍⚖️',
      xpReward: 300,
      condition: (state, result) => state.journey && Object.keys(state.journey.completedMissions || {}).length >= 25
    },
    {
      id: 'judicial_elevation',
      title: 'Civil Judge (Junior Division)',
      description: 'Complete the entire Road to Judiciary campaign and subscribe to the Judicial Oath.',
      icon: '👑',
      xpReward: 500,
      condition: (state, result) => state.journey && Object.keys(state.journey.completedMissions || {}).length >= 36
    }
"""

marker = "return (cwCount + scCount) >= 50;\n      }\n    }"
if marker not in text:
    print("Could not find insertion marker in achievements.js")
    exit(1)

new_text = text.replace(marker, marker + "," + new_achievements)
with open(ach_path, "w", encoding="utf-8") as f:
    f.write(new_text)

print("Updated achievements.js with 16 new achievements!")
