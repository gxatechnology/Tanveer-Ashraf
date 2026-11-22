/**
 * Tanveer Ashraf Judicial Prep - Game 8: Mastery Engine
 * Multi-discipline Competence Calculator & Judicial Readiness Index
 * Version 3.0 Phase 4
 * Author: Tauqeer Ashraf
 */

(function() {
  'use strict';

  class MasteryEngine {
    constructor() {
      this.disciplines = [
        "Constitutional Law",
        "Bharatiya Nyaya Sanhita, 2023",
        "Historical IPC vs BNS Transitions",
        "Bharatiya Sakshya Adhiniyam, 2023",
        "Historical IEA vs BSA Transitions",
        "Bharatiya Nagarik Suraksha Sanhita, 2023",
        "Code of Civil Procedure, 1908",
        "Law of Contract",
        "Transfer of Property Act, 1882",
        "Law of Torts",
        "Jurisprudence",
        "Legal Maxims & Landmark Cases"
      ];
    }

    /**
     * Compute comprehensive mastery metrics across all disciplines
     */
    calculateMastery() {
      // 1. Read Arena storage
      let arenaData = {};
      try {
        const raw = localStorage.getItem('tanveer-arena-v1');
        if (raw) arenaData = JSON.parse(raw);
      } catch (e) {
        console.warn("Could not read arena storage:", e);
      }

      // 2. Read PYQ portal storage
      let portalData = {};
      try {
        const raw = localStorage.getItem('tanveer-pcsj-portal-v1');
        if (raw) portalData = JSON.parse(raw);
      } catch (e) {
        console.warn("Could not read portal storage:", e);
      }

      const completedMissions = (arenaData.journey && arenaData.journey.completedMissions) || {};
      const completedCount = Object.keys(completedMissions).length;
      const arenaXP = arenaData.xp || 0;
      const arenaLevel = arenaData.level || 1;
      const testHistory = Array.isArray(portalData.history) ? portalData.history : [];
      const testsCount = testHistory.length;
      const questionsRead = Array.isArray(portalData.read) ? portalData.read.length : 0;
      const totalActivities = testsCount + completedCount + (arenaData.history ? arenaData.history.length : 0);

      // Check for sufficient activity data
      const hasSufficientData = totalActivities >= 3;

      // Calculate subject scores based on genuine documented activity
      const subjectScores = {};
      this.disciplines.forEach(subject => {
        if (!hasSufficientData) {
          subjectScores[subject] = 0;
          return;
        }

        let score = 0;
        // 1. Mission completion for this subject
        const relatedMissions = (window.JOURNEY_MISSIONS || []).filter(m => {
          return (m.title && m.title.toLowerCase().includes(subject.toLowerCase().slice(0, 5))) ||
                 (m.description && m.description.toLowerCase().includes(subject.toLowerCase().slice(0, 5)));
        });

        let completedRelated = 0;
        relatedMissions.forEach(m => {
          if (completedMissions[m.id]) completedRelated++;
        });

        if (relatedMissions.length > 0) {
          score += (completedRelated / relatedMissions.length) * 40;
        }

        // 2. Exam performance for this topic
        let topicAttempts = 0;
        let topicCorrect = 0;
        testHistory.forEach(t => {
          if (t.ids && t.answers && window.PCSJ_QUESTIONS) {
            t.ids.forEach(qid => {
              const q = window.PCSJ_QUESTIONS.find(item => item.id === qid);
              if (q && q.topic && q.topic.toLowerCase().includes(subject.toLowerCase().slice(0, 5))) {
                topicAttempts++;
                if (t.answers[qid] === q.answer) topicCorrect++;
              }
            });
          }
        });

        if (topicAttempts > 0) {
          const acc = topicCorrect / topicAttempts;
          score += Math.min(40, acc * 40);
        } else if (completedCount > 0) {
          score += Math.min(20, (completedCount / 36) * 20);
        }

        // 3. Overall study progress contribution
        score += Math.min(20, (questionsRead / 500) * 20);

        subjectScores[subject] = Math.min(100, Math.round(score));
      });

      // Overall Personal Learning Progress (0 to 100%)
      let progressPercent = 0;
      if (hasSufficientData) {
        const values = Object.values(subjectScores);
        const avgSubjectScore = values.reduce((acc, val) => acc + val, 0) / values.length;
        const missionRatio = (completedCount / 36) * 100;
        progressPercent = Math.round((avgSubjectScore * 0.6) + (missionRatio * 0.4));
        progressPercent = Math.min(100, Math.max(0, progressPercent));
      }

      // Educational Preparation Tiers (strictly educational, no simulated official titles)
      let tierTitle = "Aspirant (Initial Assessment Phase)";
      let tierBadge = "🌱";
      let statusExplanation = "Insufficient data — Complete at least 3 practice tests or campaign missions to generate documented learning progress.";

      if (hasSufficientData) {
        if (progressPercent >= 85 && completedCount >= 30) {
          tierTitle = "Comprehensive Mastery (Advanced Preparation)";
          tierBadge = "⭐";
          statusExplanation = "Exceptional preparation progress across all 12 substantive and procedural disciplines.";
        } else if (progressPercent >= 70 && completedCount >= 20) {
          tierTitle = "Proficient Scholar (Rigorous Practice)";
          tierBadge = "📚";
          statusExplanation = "Strong coverage across core subjects with consistent accuracy in simulation exercises.";
        } else if (progressPercent >= 50 && completedCount >= 12) {
          tierTitle = "Statutory Practitioner (Intermediate Progress)";
          tierBadge = "⚖️";
          statusExplanation = "Steady progress across foundational statutes; continue expanding coverage in procedural laws.";
        } else if (progressPercent >= 25 || completedCount >= 4) {
          tierTitle = "Curriculum Explorer (Active Study)";
          tierBadge = "🔍";
          statusExplanation = "Early study milestones achieved. Maintain consistent daily practice across questions and arena games.";
        } else {
          tierTitle = "Foundational Aspirant (Early Stage)";
          tierBadge = "🌱";
          statusExplanation = "Beginning study phase. Focus on daily study plan missions and core BNS / Constitution provisions.";
        }
      }

      return {
        disciplines: subjectScores,
        progressPercent,
        readinessIndex: progressPercent, // backwards-compatible alias
        rankTitle: tierTitle,
        tierTitle,
        rankBadge: tierBadge,
        tierBadge,
        hasSufficientData,
        statusExplanation,
        disclaimer: "Personal learning progress is an informal educational metric calculated from documented local test attempts, game activity, and study consistency. It does not predict examination results or guarantee success in the UP PCS-J examination.",
        completedMissionsCount: completedCount,
        totalMissionsCount: 36,
        xp: arenaXP,
        level: arenaLevel
      };
    }
  }

  if (typeof window !== 'undefined') {
    window.MasteryEngine = new MasteryEngine();
  }
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = MasteryEngine;
  }
})();
