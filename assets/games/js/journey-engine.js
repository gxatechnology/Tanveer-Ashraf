/**
 * Tanveer Ashraf Judicial Prep - Game 8: Journey Engine
 * Campaign Map, Chapter State Management & Milestone Celebrations
 * Version 3.0 Phase 4
 * Author: Tauqeer Ashraf
 */

(function() {
  'use strict';

  class JourneyEngine {
    constructor() {
      this.chapters = window.JOURNEY_CHAPTERS || [];
      this.missions = window.JOURNEY_MISSIONS || [];
      this.missionEngine = window.MissionEngine || null;
      this.masteryEngine = window.MasteryEngine || null;
    }

    /**
     * Get enriched chapters with completion percentages and lock statuses
     */
    getChaptersState() {
      const progress = this.missionEngine ? this.missionEngine.getProgress() : { completedMissions: {}, unlockedChapters: ["ch-01"] };
      const completed = progress.completedMissions || {};

      return this.chapters.map(ch => {
        const chapterMissions = this.missions.filter(m => m.chapterId === ch.id);
        const completedCount = chapterMissions.filter(m => completed[m.id]).length;
        const totalCount = chapterMissions.length;
        const percent = totalCount > 0 ? Math.round((completedCount / totalCount) * 100) : 0;
        const isUnlocked = progress.unlockedChapters.includes(ch.id);
        const isCompleted = percent === 100;

        return {
          ...ch,
          isUnlocked,
          isCompleted,
          completedCount,
          totalCount,
          percent
        };
      });
    }

    /**
     * Generate Learning Journey Educational Achievement data
     */
    generateCompletionAchievement() {
      const mastery = this.masteryEngine ? this.masteryEngine.calculateMastery() : { progressPercent: 100, rankTitle: "Judicial Preparation Master" };
      const date = new Date().toLocaleDateString('en-IN', { year: 'numeric', month: 'long', day: 'numeric' });
      const progress = this.missionEngine ? this.missionEngine.getProgress() : { completedMissions: {} };
      const completedCount = Object.keys(progress.completedMissions || {}).length;

      return {
        candidateName: "Tanveer Ashraf",
        achievementTitle: "ROAD TO JUDICIARY — LEARNING JOURNEY COMPLETED",
        subtitle: "Personal Educational Achievement",
        completedMissions: completedCount || 36,
        totalMissions: 36,
        completionDate: date,
        disclaimer: "This is an informal educational achievement from a personal examination preparation platform. It does not confer any judicial appointment, professional qualification, official rank or examination certification.",
        academicFaculty: "Academic Mentors & Legal Study Faculty",
        pledgeText: "I, Tanveer Ashraf, having completed the 9 campaign chapters of the Road to Judiciary preparation curriculum, affirm my commitment to constitutional values, continuous statutory study, analytical diligence, and rigorous preparation for the Uttar Pradesh Judicial Services Examination."
      };
    }

    generateAppointmentDecree() {
      return this.generateCompletionAchievement();
    }
  }

  if (typeof window !== 'undefined') {
    window.JourneyEngine = new JourneyEngine();
  }
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = JourneyEngine;
  }
})();
