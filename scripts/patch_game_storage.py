# Patch assets/games/js/game-storage.js to add recordMissionCompletion and mission hooks
import os

storage_path = os.path.join("assets", "games", "js", "game-storage.js")
with open(storage_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Add recordMissionCompletion before exportData
hook_func = """
    recordMissionCompletion: function(missionId, score, accuracy) {
      if (!missionId) return;
      const state = loadState();
      state.journey = state.journey || { completedMissions: {}, unlockedChapters: ["ch-01"] };
      state.journey.completedMissions = state.journey.completedMissions || {};

      state.journey.completedMissions[missionId] = {
        completedAt: getTodayString(),
        score: score || 100,
        accuracy: accuracy !== undefined ? accuracy : 100
      };

      saveState(state);

      if (window.MissionEngine && window.MissionEngine.recordMissionOutcome) {
        window.MissionEngine.recordMissionOutcome(missionId, score, accuracy);
      }

      if (window.Achievements && window.Achievements.checkAchievements) {
        window.Achievements.checkAchievements();
      }
    },

    exportData: function() {"""

if "exportData: function() {" in text:
    text = text.replace("exportData: function() {", hook_func, 1)

# 2. Add mission hook inside recordGameResult
game_hook = """      saveState(state);

      // Automatic campaign mission recording
      try {
        const uParams = (typeof window !== 'undefined' && window.location) ? new URLSearchParams(window.location.search) : null;
        const mId = (result && result.missionId) || (uParams && uParams.get('missionId'));
        if (mId) {
          GameStorage.recordMissionCompletion(mId, result.score || 100, result.accuracy || 100);
        }
      } catch (err) {}"""

# In recordGameResult, find the last saveState(state) before return
# Let's locate 'saveState(state);' inside recordGameResult
idx = text.find("recordGameResult: function(result)")
if idx != -1:
    save_idx = text.find("saveState(state);", idx)
    if save_idx != -1:
        text = text[:save_idx] + game_hook + text[save_idx + len("saveState(state);"):]

with open(storage_path, "w", encoding="utf-8") as f:
    f.write(text)

print("game-storage.js patched successfully!")
