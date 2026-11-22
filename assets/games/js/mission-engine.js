/**
 * Tanveer Ashraf Judicial Prep - Game 8: Mission Engine
 * Campaign Progress, Unlock Conditions & Real Mission Execution
 * Version 3.0 Phase 4
 * Author: Tauqeer Ashraf
 */

(function() {
  'use strict';

  class MissionEngine {
    constructor() {
      this.chapters = window.JOURNEY_CHAPTERS || [];
      this.missions = window.JOURNEY_MISSIONS || [];
    }

    /**
     * Get user's current campaign progress from localStorage
     */
    getProgress() {
      let data = {
        completedMissions: {},
        unlockedChapters: ["ch-01"],
        activeMissionId: "m-acad-01"
      };

      try {
        const raw = localStorage.getItem('tanveer-arena-v1');
        if (raw) {
          const parsed = JSON.parse(raw);
          if (parsed.journey) {
            data.completedMissions = parsed.journey.completedMissions || {};
            data.unlockedChapters = parsed.journey.unlockedChapters || ["ch-01"];
            data.activeMissionId = parsed.journey.activeMissionId || "m-acad-01";
          }
        }
      } catch (e) {
        console.warn("Could not read journey progress:", e);
      }

      // Check which chapters should be unlocked dynamically based on completed missions
      this.chapters.forEach((ch, idx) => {
        if (idx === 0) {
          if (!data.unlockedChapters.includes(ch.id)) data.unlockedChapters.push(ch.id);
        } else {
          const prevChapter = this.chapters[idx - 1];
          const prevMissions = this.missions.filter(m => m.chapterId === prevChapter.id);
          const completedInPrev = prevMissions.filter(m => data.completedMissions[m.id]).length;

          // Unlock next chapter if at least 3 of 4 missions in previous chapter are completed
          if (completedInPrev >= 3 && !data.unlockedChapters.includes(ch.id)) {
            data.unlockedChapters.push(ch.id);
          }
        }
      });

      return data;
    }

    /**
     * Save updated journey progress to tanveer-arena-v1
     */
    saveProgress(progress) {
      try {
        let arena = {};
        const raw = localStorage.getItem('tanveer-arena-v1');
        if (raw) arena = JSON.parse(raw);

        arena.journey = arena.journey || {};
        arena.journey.completedMissions = progress.completedMissions || {};
        arena.journey.unlockedChapters = progress.unlockedChapters || ["ch-01"];
        arena.journey.activeMissionId = progress.activeMissionId || "m-acad-01";
        arena.journey.lastUpdated = new Date().toISOString();

        localStorage.setItem('tanveer-arena-v1', JSON.stringify(arena));
      } catch (e) {
        console.error("Error saving journey progress:", e);
      }
    }

    /**
     * Check if a specific mission is unlocked
     */
    isMissionUnlocked(missionId) {
      const mission = this.missions.find(m => m.id === missionId);
      if (!mission) return false;

      const progress = this.getProgress();
      // Chapter must be unlocked
      if (!progress.unlockedChapters.includes(mission.chapterId)) {
        return false;
      }

      // First mission in an unlocked chapter is always unlocked
      const chapterMissions = this.missions.filter(m => m.chapterId === mission.chapterId);
      const missionIndex = chapterMissions.findIndex(m => m.id === missionId);
      if (missionIndex === 0) return true;

      // Otherwise, previous mission in the same chapter must be completed
      const prevMission = chapterMissions[missionIndex - 1];
      return Boolean(progress.completedMissions[prevMission.id]);
    }

    /**
     * Record outcome of a mission after game completion
     */
    recordMissionOutcome(missionId, score, accuracy) {
      const mission = this.missions.find(m => m.id === missionId);
      if (!mission) return null;

      const progress = this.getProgress();
      const minScore = (mission.criteria && mission.criteria.minScore) || 50;
      const minAcc = (mission.criteria && mission.criteria.minAccuracy) || 60;

      const passed = (score >= minScore) && (accuracy === undefined || accuracy >= minAcc);

      if (passed) {
        progress.completedMissions[missionId] = {
          completedAt: new Date().toISOString(),
          score,
          accuracy: accuracy || 100,
          rewardXPEarned: mission.rewardXP
        };

        // Determine next active mission
        const nextMission = this.missions.find(m => !progress.completedMissions[m.id]);
        if (nextMission) {
          progress.activeMissionId = nextMission.id;
        }

        this.saveProgress(progress);

        // Add reward XP to general arena storage
        if (window.GameStorage && window.GameStorage.addXP) {
          window.GameStorage.addXP(mission.rewardXP, `Completed Campaign Mission: ${mission.title}`);
        }

        // Check achievements
        if (window.Achievements && window.Achievements.checkAchievements) {
          window.Achievements.checkAchievements();
        }
      }

      return {
        passed,
        mission,
        score,
        accuracy,
        rewardXP: passed ? mission.rewardXP : 0,
        unlockedNext: passed
      };
    }

    /**
     * Get full mission details with live status
     */
    getEnrichedMissions() {
      const progress = this.getProgress();
      return this.missions.map(m => {
        const isCompleted = Boolean(progress.completedMissions[m.id]);
        const isUnlocked = isCompleted || this.isMissionUnlocked(m.id);
        const completionData = progress.completedMissions[m.id] || null;

        return {
          ...m,
          status: isCompleted ? 'completed' : (isUnlocked ? 'available' : 'locked'),
          completionData
        };
      });
    }
  }

  if (typeof window !== 'undefined') {
    window.MissionEngine = new MissionEngine();
  }
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = MissionEngine;
  }
})();
