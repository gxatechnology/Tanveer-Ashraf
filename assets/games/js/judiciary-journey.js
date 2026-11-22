/**
 * Tanveer Ashraf Judicial Prep - Game 8: Road to Judiciary UI Controller
 * Version 3.0 Phase 4
 * Author: Tauqeer Ashraf
 */

(function() {
  'use strict';

  class JudiciaryJourneyUI {
    constructor() {
      this.app = document.getElementById('journeyApp');
      if (!this.app) {
        console.error("JourneyApp container not found.");
        return;
      }

      this.missionEngine = window.MissionEngine;
      this.masteryEngine = window.MasteryEngine;
      this.journeyEngine = window.JourneyEngine;
      this.learningPlan = window.LearningPlan;

      this.activeChapterModal = null;
      this.currentPlanBudget = 30;

      // Check URL parameters
      const params = new URLSearchParams(window.location.search);
      const action = params.get('action');
      if (action === 'take_oath' || action === 'educational_achievement' || action === 'certificate') {
        this.showDecree = true;
      } else {
        this.showDecree = false;
      }

      this.init();
    }

    init() {
      this.render();
    }

    render() {
      const mastery = this.masteryEngine ? this.masteryEngine.calculateMastery() : {
        readinessIndex: 25,
        rankTitle: "Judicial Aspirant",
        rankBadge: "⚖️",
        completedMissionsCount: 0,
        totalMissionsCount: 36,
        disciplines: {}
      };

      const chapters = this.journeyEngine ? this.journeyEngine.getChaptersState() : [];
      const plan = this.learningPlan ? this.learningPlan.generatePlan(this.currentPlanBudget) : { tasks: [] };

      this.app.innerHTML = `
        <div class="journey-app">
          <!-- Hero Section -->
          <header class="journey-hero">
            <div class="journey-hero-meta">
              <span class="journey-badge">Campaign Mode • Game 8</span>
              <a href="brain-arena.html" style="color:#e7c88c; text-decoration:none; font-size:0.9rem; font-weight:600;">← Brain Arena</a>
            </div>
            <h1 class="journey-title">Road to Judiciary: The Rise of a Judge</h1>
            <p class="journey-tagline">Every Challenge Brings You Closer to the Bench.</p>

            <!-- Personal Learning Progress Chip -->
            <div class="readiness-chip">
              <span class="readiness-badge-icon">${mastery.tierBadge || mastery.rankBadge}</span>
              <div class="readiness-info">
                <span class="readiness-rank">${mastery.tierTitle || mastery.rankTitle}</span>
                <span class="readiness-index">Personal Learning Progress: <strong>${mastery.progressPercent}%</strong> • Missions: <strong>${mastery.completedMissionsCount} / ${mastery.totalMissionsCount}</strong></span>
                <small style="display:block; color:#cbd5e1; font-size:0.75rem; margin-top:2px;">${mastery.statusExplanation}</small>
              </div>
            </div>
          </header>

          <!-- Interactive Campaign Map -->
          <section class="journey-map-card">
            <div class="map-card-header">
              <h2 class="map-card-title">🗺️ Judicial Campaign Map</h2>
              <span style="font-size:0.85rem; color:#607387;">Click on any unlocked landmark to view missions</span>
            </div>
            <div class="journey-map-viewport" id="journeyMap">
              ${chapters.map(ch => `
                <div class="map-node ${ch.isCompleted ? 'completed' : (ch.isUnlocked ? 'unlocked' : 'locked')}" 
                     style="left: ${ch.coords.x}%; top: ${ch.coords.y}%;"
                     data-chapter-id="${ch.id}">
                  <span>${ch.badgeIcon}</span>
                  <div class="map-tooltip">
                    <strong>Chapter ${ch.number}: ${ch.title}</strong><br>
                    ${ch.isCompleted ? '✓ Completed' : (ch.isUnlocked ? `${ch.completedCount}/${ch.totalCount} Missions` : '🔒 Locked')}
                  </div>
                </div>
              `).join('')}
            </div>
          </section>

          <!-- Daily Learning Plan Widget -->
          <section class="plan-card">
            <div class="plan-header">
              <div>
                <h2 class="plan-title">📅 Personalized Daily Study Plan</h2>
                <span style="font-size:0.85rem; color:#607387;">Deterministic task recommendations tailored to your preparation budget</span>
              </div>
              <div class="plan-budgets-deck">
                <button type="button" class="btn-plan-budget ${this.currentPlanBudget === 15 ? 'active' : ''}" data-budget="15">15 Mins</button>
                <button type="button" class="btn-plan-budget ${this.currentPlanBudget === 30 ? 'active' : ''}" data-budget="30">30 Mins</button>
                <button type="button" class="btn-plan-budget ${this.currentPlanBudget === 45 ? 'active' : ''}" data-budget="45">45 Mins</button>
                <button type="button" class="btn-plan-budget ${this.currentPlanBudget === 60 ? 'active' : ''}" data-budget="60">60 Mins</button>
              </div>
            </div>

            <div class="plan-tasks-list">
              ${plan.tasks.map(t => `
                <div class="plan-task-row">
                  <div class="plan-task-left">
                    <span class="plan-task-icon">${t.icon}</span>
                    <div>
                      <div class="plan-task-name">${t.title}</div>
                      <div class="plan-task-obj">${t.objective}</div>
                    </div>
                  </div>
                  <div class="plan-task-action">
                    <span class="plan-task-time">⏱️ ${t.duration}</span>
                    <a href="${t.url}" class="btn-launch-mission" style="padding:0.4rem 0.85rem; font-size:0.8rem;">Start Task →</a>
                  </div>
                </div>
              `).join('')}
            </div>
          </section>

          <!-- 9 Campaign Chapters Grid Deck -->
          <section style="margin-bottom:2.5rem;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.25rem;">
              <h2 style="font-family:'Georgia', serif; font-size:1.6rem; color:#142c46; margin:0;">
                Campaign Chapters (9 Districts)
              </h2>
              <span style="font-size:0.85rem; color:#607387;">Total 36 Authored Missions</span>
            </div>

            <div class="chapters-grid">
              ${chapters.map(ch => `
                <div class="chapter-card ${ch.isCompleted ? 'completed' : (ch.isUnlocked ? 'unlocked' : 'locked')}">
                  <div>
                    <div class="chapter-top">
                      <span class="chapter-num">Chapter ${ch.number}</span>
                      <span style="font-size:1.2rem;">${ch.badgeIcon}</span>
                    </div>
                    <h3 class="chapter-title">${ch.title}</h3>
                    <div class="chapter-discipline">${ch.discipline}</div>
                    <p class="chapter-lore">${ch.lore}</p>

                    <!-- Mentor Chip -->
                    <div class="chapter-mentor">
                      <img src="${ch.mentorAvatar}" alt="${ch.mentorName}" class="chapter-mentor-avatar" onerror="this.src='assets/images/emblem.svg'">
                      <div>
                        <div class="chapter-mentor-name">${ch.mentorName}</div>
                        <div class="chapter-mentor-role">${ch.mentorRole}</div>
                      </div>
                    </div>
                  </div>

                  <div>
                    <!-- Progress track -->
                    <div class="chapter-progress-track">
                      <div class="chapter-progress-bar" style="width:${ch.percent}%;"></div>
                    </div>
                    <div class="chapter-footer">
                      <span style="font-size:0.8rem; font-weight:700; color:#142c46;">
                        ${ch.isCompleted ? '✓ Completed' : `${ch.completedCount} / ${ch.totalCount} Missions`}
                      </span>
                      <button type="button" class="btn-open-missions" data-open-chapter="${ch.id}" ${!ch.isUnlocked ? 'disabled' : ''}>
                        ${ch.isUnlocked ? 'View Missions →' : '🔒 Locked'}
                      </button>
                    </div>
                  </div>
                </div>
              `).join('')}
            </div>
          </section>

          <!-- Multi-Discipline Competence & Mastery Section -->
          <section class="mastery-card">
            <div class="mastery-header">
              <h2 class="mastery-title">📊 Multi-Discipline Competence Matrix</h2>
              <p style="font-size:0.85rem; color:#607387; margin:0;">Real-time competence tracking across 12 primary UP PCS-J legal disciplines</p>
            </div>

            <div class="mastery-bars-grid">
              ${Object.entries(mastery.disciplines).map(([subject, score]) => `
                <div class="mastery-bar-item">
                  <div class="mastery-bar-label">
                    <span>${subject}</span>
                    <span><strong>${score}%</strong></span>
                  </div>
                  <div class="mastery-bar-track">
                    <div class="mastery-bar-fill" style="width:${score}%;"></div>
                  </div>
                </div>
              `).join('')}
            </div>
          </section>

          <!-- Appointment Decree (if triggered) -->
          ${this.showDecree ? this.renderDecreeModal() : ''}

          <!-- Mission Modal Placeholder -->
          <div id="missionModalContainer"></div>
        </div>
      `;

      this.bindEvents();
    }

    renderDecreeModal() {
      const data = this.journeyEngine ? this.journeyEngine.generateCompletionAchievement() : {
        candidateName: "Tanveer Ashraf",
        achievementTitle: "ROAD TO JUDICIARY — LEARNING JOURNEY COMPLETED",
        subtitle: "Personal Educational Achievement",
        completedMissions: 36,
        totalMissions: 36,
        completionDate: new Date().toLocaleDateString('en-IN', { year: 'numeric', month: 'long', day: 'numeric' }),
        disclaimer: "This is an informal educational achievement from a personal examination preparation platform. It does not confer any judicial appointment, professional qualification, official rank or examination certification.",
        academicFaculty: "Academic Mentors & Legal Study Faculty",
        pledgeText: "I, Tanveer Ashraf, having completed the 9 campaign chapters of the Road to Judiciary preparation curriculum, affirm my commitment to constitutional values, continuous statutory study, analytical diligence, and rigorous preparation for the Uttar Pradesh Judicial Services Examination."
      };

      return `
        <div class="missions-modal-backdrop" id="decreeModal">
          <div class="decree-modal" style="max-width:720px; border-radius:12px; background:linear-gradient(135deg, #fffcf5 0%, #fbf5e6 100%); border:2px solid #dfbf80; box-shadow:0 12px 40px rgba(20,44,70,0.25);">
            <button type="button" class="missions-modal-close" onclick="document.getElementById('decreeModal').remove()">×</button>
            <div style="text-align:center; padding:1rem 0 0.5rem;">
              <img src="assets/images/emblem.svg" alt="Emblem" class="decree-emblem" style="width:56px; height:56px; margin-bottom:0.5rem;">
              <h2 class="decree-heading" style="color:#142c46; font-family:'Georgia', serif; font-size:1.6rem; letter-spacing:0.5px; margin:0 0 0.25rem;">${data.achievementTitle}</h2>
              <div class="decree-sub" style="color:#b98a38; font-weight:600; text-transform:uppercase; font-size:0.85rem; letter-spacing:1px;">${data.subtitle}</div>
            </div>

            <div class="decree-body" style="padding:1rem 1.5rem; color:#1c2e40; line-height:1.7;">
              <p style="text-align:center; font-size:1.05rem; margin-bottom:1rem;">
                This certifies that <strong>${data.candidateName}</strong> has successfully completed all <strong>${data.completedMissions} of ${data.totalMissions} missions</strong> across the 9 educational chapters of the Road to Judiciary campaign.
              </p>

              <div style="background:rgba(19,125,114,0.06); border:1px solid #c2e2dd; border-radius:8px; padding:1rem; margin:1rem 0;">
                <div style="font-weight:600; color:#137d72; font-size:0.9rem; margin-bottom:0.25rem;">Candidate Educational Pledge:</div>
                <p style="font-style:italic; font-size:0.92rem; margin:0; color:#2c4356;">
                  "${data.pledgeText}"
                </p>
              </div>

              <!-- Required Explicit Educational Disclaimer -->
              <div style="background:rgba(20,44,70,0.05); border-left:4px solid #dfbf80; padding:0.75rem 1rem; border-radius:4px; margin:1.25rem 0; font-size:0.8rem; color:#607387; line-height:1.5;">
                <strong>IMPORTANT NOTICE & DISCLAIMER:</strong> ${data.disclaimer}
              </div>
            </div>

            <div class="decree-signature-block" style="display:flex; justify-content:space-between; padding:0 2rem 1.5rem; margin-top:0.5rem;">
              <div class="decree-sig" style="text-align:left;">
                <span class="decree-sig-name" style="display:block; font-weight:700; color:#142c46; border-bottom:1px solid #cbd5e1; padding-bottom:4px; min-width:180px;">${data.candidateName}</span>
                <span class="decree-sig-title" style="display:block; font-size:0.8rem; color:#607387; margin-top:4px;">Candidate & Judicial Aspirant</span>
              </div>
              <div class="decree-sig" style="text-align:right;">
                <span class="decree-sig-name" style="display:block; font-weight:700; color:#142c46; border-bottom:1px solid #cbd5e1; padding-bottom:4px; min-width:180px;">Tauqeer Ashraf</span>
                <span class="decree-sig-title" style="display:block; font-size:0.8rem; color:#607387; margin-top:4px;">Platform Developer & System Architect</span>
              </div>
            </div>

            <div style="text-align:center; padding-bottom:1.5rem;">
              <button type="button" class="btn-launch-mission" onclick="window.print()" style="padding:0.75rem 2rem; background:#142c46; color:#fff; border:none; border-radius:6px; cursor:pointer; font-weight:600;">🖨️ Print Educational Certificate</button>
            </div>
          </div>
        </div>
      `;
    }

    openChapterMissions(chapterId) {
      const ch = (window.JOURNEY_CHAPTERS || []).find(c => c.id === chapterId);
      if (!ch) return;

      const missions = this.missionEngine ? this.missionEngine.getEnrichedMissions().filter(m => m.chapterId === chapterId) : [];

      const modalHtml = `
        <div class="missions-modal-backdrop" id="activeMissionModal">
          <div class="missions-modal">
            <button type="button" class="missions-modal-close" id="btnCloseMissionModal">×</button>
            <span style="font-size:0.8rem; font-weight:700; color:#b98a38; text-transform:uppercase;">Chapter ${ch.number} Campaign</span>
            <h2 class="modal-chapter-title">${ch.title}</h2>
            <p style="color:#607387; font-size:0.9rem; margin-bottom:1rem;">${ch.tagline}</p>

            <!-- Mentor Briefing -->
            <div class="chapter-mentor" style="margin-bottom:1.5rem;">
              <img src="${ch.mentorAvatar}" alt="${ch.mentorName}" class="chapter-mentor-avatar" onerror="this.src='assets/images/emblem.svg'">
              <div>
                <div class="chapter-mentor-name">${ch.mentorName} <span style="font-size:0.75rem; font-weight:normal; color:#607387;">(${ch.mentorRole})</span></div>
                <div style="font-size:0.82rem; color:#2c3e50; font-style:italic;">"${ch.lore}"</div>
              </div>
            </div>

            <!-- Missions List -->
            <div class="missions-list">
              ${missions.map(m => `
                <div class="mission-item-card ${m.status}">
                  <div class="mission-item-info">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.25rem;">
                      <span class="mission-item-title">${m.number}. ${m.title}</span>
                      <span style="font-size:0.75rem; font-weight:700; padding:0.2rem 0.5rem; border-radius:4px; ${m.status === 'completed' ? 'background:#edf7f4; color:#137d72;' : (m.status === 'available' ? 'background:#fdf5e6; color:#b98a38;' : 'background:#e2e8f0; color:#718096;')}">
                        ${m.status.toUpperCase()}
                      </span>
                    </div>
                    <p class="mission-item-desc">${m.description}</p>
                    <div class="mission-item-meta">
                      <span>🎯 Target: Score ${m.criteria.minScore || 50}+</span>
                      <span>⭐ +${m.rewardXP} XP</span>
                      <span>🏅 ${m.badge}</span>
                    </div>
                  </div>

                  <div>
                    ${m.status !== 'locked' ? `
                      <a href="${m.gameUrl}" class="btn-launch-mission">
                        ${m.status === 'completed' ? 'Replay Mission ↺' : 'Launch Mission ▶'}
                      </a>
                    ` : `
                      <button class="btn-launch-mission" disabled style="background:#a0aec0; cursor:not-allowed;">
                        🔒 Locked
                      </button>
                    `}
                  </div>
                </div>
              `).join('')}
            </div>
          </div>
        </div>
      `;

      const container = document.getElementById('missionModalContainer');
      if (container) {
        container.innerHTML = modalHtml;
        document.getElementById('btnCloseMissionModal')?.addEventListener('click', () => {
          container.innerHTML = '';
        });
      }
    }

    bindEvents() {
      // Map node clicks
      const nodes = this.app.querySelectorAll('.map-node[data-chapter-id]');
      nodes.forEach(node => {
        node.addEventListener('click', () => {
          const chId = node.getAttribute('data-chapter-id');
          this.openChapterMissions(chId);
        });
      });

      // Chapter card "View Missions" button
      const openBtns = this.app.querySelectorAll('[data-open-chapter]');
      openBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          const chId = btn.getAttribute('data-open-chapter');
          this.openChapterMissions(chId);
        });
      });

      // Daily plan budget buttons
      const budgetBtns = this.app.querySelectorAll('.btn-plan-budget');
      budgetBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          const b = parseInt(btn.getAttribute('data-budget'), 10);
          this.currentPlanBudget = b;
          this.render();
        });
      });
    }
  }

  document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('journeyApp')) {
      window.judiciaryJourneyInstance = new JudiciaryJourneyUI();
    }
  });

  if (typeof window !== 'undefined') {
    window.JudiciaryJourneyUI = JudiciaryJourneyUI;
  }
})();
