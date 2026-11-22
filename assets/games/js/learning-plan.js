/**
 * Tanveer Ashraf Judicial Prep - Game 8: Personalized Daily Learning Plan
 * Deterministic Daily Recommendations for 15, 30, 45, and 60 Minute Budgets
 * Version 3.0 Phase 4
 * Author: Tauqeer Ashraf
 */

(function() {
  'use strict';

  class LearningPlan {
    constructor() {
      this.budgets = [15, 30, 45, 60];
      this.defaultBudget = 30;
    }

    /**
     * Generate deterministic schedule for a given minute budget
     */
    generatePlan(minutes = 30) {
      const budget = this.budgets.includes(minutes) ? minutes : this.defaultBudget;
      const today = new Date().toISOString().split('T')[0];

      // Read completed missions to recommend next uncompleted mission
      let arenaData = {};
      try {
        const raw = localStorage.getItem('tanveer-arena-v1');
        if (raw) arenaData = JSON.parse(raw);
      } catch (e) {
        console.warn("Could not read arena data for learning plan:", e);
      }

      const completed = (arenaData.journey && arenaData.journey.completedMissions) || {};
      const allMissions = window.JOURNEY_MISSIONS || [];
      const pendingMission = allMissions.find(m => !completed[m.id]) || allMissions[0];

      let tasks = [];

      if (budget === 15) {
        tasks = [
          {
            id: "task-15-1",
            title: "High-Speed BNS Recall",
            duration: "5 mins",
            type: "game",
            game: "Section Sprint",
            url: "section-sprint.html?mode=number_to_title&time=60",
            icon: "⚡",
            objective: "Warm up legal memory with a 60-second section number recall sprint."
          },
          {
            id: "task-15-2",
            title: "Chamber of Truth Diagnostic",
            duration: "5 mins",
            type: "game",
            game: "Legal Myth Buster",
            url: "myth-buster.html?mode=classic&count=5",
            icon: "⚖️",
            objective: "Examine 5 statutory propositions to test active precision."
          },
          {
            id: "task-15-3",
            title: "Statutory Term Decryption",
            duration: "5 mins",
            type: "game",
            game: "Word Scramble",
            url: "word-scramble.html?mode=standard&count=5",
            icon: "🔤",
            objective: "Decrypt 5 essential legal vocabulary terms in the Code Breaker."
          }
        ];
      } else if (budget === 30) {
        tasks = [
          {
            id: "task-30-1",
            title: "Road to Judiciary Campaign Mission",
            duration: "10 mins",
            type: "journey",
            game: pendingMission.title,
            url: pendingMission.gameUrl,
            icon: "🗺️",
            objective: `Complete active mission: ${pendingMission.title} (${pendingMission.badge}).`
          },
          {
            id: "task-30-2",
            title: "Chamber of Truth: Precedent Challenge",
            duration: "10 mins",
            type: "game",
            game: "Legal Myth Buster",
            url: "myth-buster.html?mode=precedent_challenge&count=8",
            icon: "🏛️",
            objective: "Differentiate binding ratio decidendi from obiter dicta in 8 propositions."
          },
          {
            id: "task-30-3",
            title: "Lexicon Chamber Statutory Crossword",
            duration: "10 mins",
            type: "game",
            game: "Legal Crossword",
            url: "crossword.html?puzzle=puzzle-01",
            icon: "🧩",
            objective: "Solve a 9x9 crossword puzzle to consolidate procedural legal vocabulary."
          }
        ];
      } else if (budget === 45) {
        tasks = [
          {
            id: "task-45-1",
            title: "UP PCS-J Historical PYQ Mock Test",
            duration: "15 mins",
            type: "test",
            game: "Test Centre",
            url: "tests.html?paper=law&count=15",
            icon: "📝",
            objective: "Simulate a 15-question Paper II Law mock test with negative marking."
          },
          {
            id: "task-45-2",
            title: "Judicial Bench Simulation",
            duration: "15 mins",
            type: "game",
            game: "Be the Judge",
            url: "courtroom.html?caseId=court-case-1",
            icon: "👨‍⚖️",
            objective: "Preside over Courtroom Case 1 and author structured judicial findings."
          },
          {
            id: "task-45-3",
            title: "Legal Myth Buster: Old Law vs New Law",
            duration: "15 mins",
            type: "game",
            game: "Legal Myth Buster",
            url: "myth-buster.html?mode=old_vs_new&count=10",
            icon: "🔄",
            objective: "Master 10 transition provisions bridging IPC/CrPC/IEA to 2024 Sanhitas."
          }
        ];
      } else if (budget === 60) {
        tasks = [
          {
            id: "task-60-1",
            title: "Comprehensive PYQ Gauntlet",
            duration: "20 mins",
            type: "test",
            game: "Test Centre",
            url: "tests.html?paper=law&year=2023&count=20",
            icon: "📚",
            objective: "Complete 20 authentic 2023 UP PCS-J Paper II examination questions."
          },
          {
            id: "task-60-2",
            title: "Forensic Criminal Investigation",
            duration: "15 mins",
            type: "game",
            game: "Legal Detective",
            url: "legal-detective.html?caseId=case-1",
            icon: "🔎",
            objective: "Investigate Case File 1, scrutinize crime scene evidence, and frame charges."
          },
          {
            id: "task-60-3",
            title: "The Grand Truth Trial",
            duration: "15 mins",
            type: "game",
            game: "Legal Myth Buster",
            url: "myth-buster.html?mode=grand_trial&count=15",
            icon: "🏆",
            objective: "Conquer a 15-question multi-discipline judicial examination trial."
          },
          {
            id: "task-60-4",
            title: "Road to Judiciary Campaign Mission",
            duration: "10 mins",
            type: "journey",
            game: pendingMission.title,
            url: pendingMission.gameUrl,
            icon: "👑",
            objective: `Advance campaign progress: ${pendingMission.title}.`
          }
        ];
      }

      return {
        date: today,
        budget,
        totalTasks: tasks.length,
        tasks
      };
    }
  }

  if (typeof window !== 'undefined') {
    window.LearningPlan = new LearningPlan();
  }
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = LearningPlan;
  }
})();
