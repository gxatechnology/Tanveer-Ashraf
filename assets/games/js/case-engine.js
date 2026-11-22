/**
 * LEGAL BRAIN ARENA — SHARED CASE ENGINE (V3.0 Phase 2)
 * Universal stage progression, scoring rubric calculation, and debriefing.
 * Author: Tauqeer Ashraf
 */
(function() {
  'use strict';

  const CaseEngine = {
    renderStepper: function(steps, activeIndex) {
      // steps: [{ number, label, sub }]
      return `
        <div class="sim-stepper">
          ${steps.map((step, idx) => {
            const isActive = idx === activeIndex;
            const isCompleted = idx < activeIndex;
            return `
              <div class="stepper-step ${isActive ? 'active' : ''} ${isCompleted ? 'completed' : ''}">
                <div class="stepper-num">${isCompleted ? '✓' : step.number}</div>
                <div class="stepper-info">
                  <span class="stepper-label">${step.label}</span>
                  <span class="stepper-sub">${step.sub || ''}</span>
                </div>
              </div>
              ${idx < steps.length - 1 ? `<div class="stepper-line ${idx < activeIndex ? 'passed' : ''}"></div>` : ''}
            `;
          }).join('')}
        </div>
      `;
    },

    calculateDetectiveScore: function(caseData, userState) {
      // userState: {
      //   evidenceMarks: { [evId]: 'relevant'|'possibly_relevant'|'irrelevant' },
      //   factsDiscoveredCount: number,
      //   totalFactsPossible: number,
      //   boardEvaluation: { score: 0..20 },
      //   deductionChoiceId: string,
      //   hintsUsed: number
      // }
      const rubric = {
        evidenceAnalysis: 0, // max 25
        witnessExam: 0,      // max 20
        evidenceBoard: 0,    // max 20
        legalDeduction: 0,   // max 25
        efficiency: 10       // max 10
      };

      // 1. Evidence Analysis (25 pts)
      const evidenceList = caseData.evidence || [];
      if (evidenceList.length > 0) {
        let correctMarks = 0;
        evidenceList.forEach(ev => {
          const userMark = userState.evidenceMarks[ev.id];
          if (userMark === ev.actualRelevance) {
            correctMarks++;
          }
        });
        rubric.evidenceAnalysis = Math.round((correctMarks / evidenceList.length) * 25);
      } else {
        rubric.evidenceAnalysis = 25;
      }

      // 2. Witness Examination (20 pts)
      const totalPossibleFacts = Math.max(1, userState.totalFactsPossible || 1);
      const factsFound = Math.min(totalPossibleFacts, userState.factsDiscoveredCount || 0);
      rubric.witnessExam = Math.round((factsFound / totalPossibleFacts) * 20);

      // 3. Evidence Board (20 pts)
      rubric.evidenceBoard = userState.boardEvaluation ? userState.boardEvaluation.score : 0;

      // 4. Legal Deduction (25 pts)
      const deductionOptions = (caseData.deduction && caseData.deduction.options) || [];
      const chosenOption = deductionOptions.find(o => o.id === userState.deductionChoiceId);
      if (chosenOption && chosenOption.isCorrect) {
        rubric.legalDeduction = 25;
      } else {
        rubric.legalDeduction = 0;
      }

      // 5. Efficiency (10 pts minus 3 per hint)
      const hintPenalties = (userState.hintsUsed || 0) * 3;
      rubric.efficiency = Math.max(0, 10 - hintPenalties);

      const totalScore = rubric.evidenceAnalysis + rubric.witnessExam + rubric.evidenceBoard + rubric.legalDeduction + rubric.efficiency;

      return {
        score: totalScore,
        maxScore: 100,
        rubric: rubric,
        chosenOption: chosenOption
      };
    },

    calculateCourtroomScore: function(caseData, userState) {
      // userState: {
      //   exhibitsExaminedCount: number,
      //   totalExhibits: number,
      //   framedIssuesIds: [string],
      //   decisionChoiceId: string,
      //   selectedOrderItems: { facts: [], law: [], operative: [] },
      //   hintsUsed: number
      // }
      const rubric = {
        factAssessment: 0,       // max 20
        precedentApplication: 0, // max 25
        proceduralSoundness: 0,  // max 25
        orderDrafting: 0,        // max 20
        judicialDecorum: 10      // max 10
      };

      // 1. Fact Assessment & Exhibit Review (20 pts)
      const exhibits = (caseData.proceedings && caseData.proceedings.exhibits) || [];
      if (exhibits.length > 0) {
        const reviewed = Math.min(exhibits.length, userState.exhibitsExaminedCount || 0);
        rubric.factAssessment = Math.round((reviewed / exhibits.length) * 20);
      } else {
        rubric.factAssessment = 20;
      }

      // 2. Precedent & Legal Issue Framing (25 pts)
      const legalIssues = (caseData.proceedings && caseData.proceedings.legalIssues) || [];
      const coreIssues = legalIssues.filter(i => i.isCore);
      const userFramed = userState.framedIssuesIds || [];
      let coreCount = 0;
      let nonCorePenalty = 0;
      userFramed.forEach(id => {
        const issue = legalIssues.find(i => i.id === id);
        if (issue && issue.isCore) coreCount++;
        else nonCorePenalty += 3;
      });
      const ratio = coreIssues.length > 0 ? (coreCount / coreIssues.length) : 1;
      rubric.proceduralSoundness = Math.max(0, Math.round(ratio * 25) - nonCorePenalty);

      // 3. Precedent & Decision Ruling (25 pts)
      const decisions = (caseData.proceedings && caseData.proceedings.decisionOptions) || [];
      const chosen = decisions.find(d => d.id === userState.decisionChoiceId);
      if (chosen && chosen.isCorrect) {
        rubric.precedentApplication = 25;
      } else {
        rubric.precedentApplication = 0;
      }

      // 4. Reasoned Order Drafting (20 pts)
      const builder = caseData.proceedings && caseData.proceedings.orderBuilder;
      if (builder) {
        let correctElements = 0;
        let totalElements = 0;

        const checkPool = (pool, userSelection) => {
          if (!pool) return;
          pool.forEach(item => {
            totalElements++;
            const isUserSelected = (userSelection || []).includes(item.id);
            if (item.isSelected === isUserSelected) {
              correctElements++;
            }
          });
        };

        checkPool(builder.factsPool, userState.selectedOrderItems.facts);
        checkPool(builder.lawPool, userState.selectedOrderItems.law);
        checkPool(builder.operativeOrderPool, userState.selectedOrderItems.operative);

        rubric.orderDrafting = Math.round((correctElements / Math.max(1, totalElements)) * 20);
      } else {
        rubric.orderDrafting = 20;
      }

      // 5. Decorum & Efficiency (10 pts)
      const hintPenalties = (userState.hintsUsed || 0) * 3;
      rubric.judicialDecorum = Math.max(0, 10 - hintPenalties);

      const totalScore = rubric.factAssessment + rubric.precedentApplication + rubric.proceduralSoundness + rubric.orderDrafting + rubric.judicialDecorum;

      return {
        score: totalScore,
        maxScore: 100,
        rubric: rubric,
        chosenDecision: chosen
      };
    },

    renderDebrief: function(containerEl, caseData, scoreResult, gameType, onRestart, onNext) {
      if (!containerEl) return;

      const isDetective = gameType === 'legal-detective';
      const rubric = scoreResult.rubric;
      const score = scoreResult.score;

      // Feedback text based on score tier
      let feedbackTitle = 'Distinguished Judicial Performance';
      let feedbackBody = 'You demonstrated comprehensive mastery of substantive law, evidentiary standards, and rigorous procedural application.';
      if (score < 60) {
        feedbackTitle = 'Judicial Review Recommended';
        feedbackBody = 'Significant procedural or statutory elements were missed. Review the statutory provisions and case law citations carefully before proceeding.';
      } else if (score < 85) {
        feedbackTitle = 'Competent Legal Analysis';
        feedbackBody = 'A commendable analysis, though precision in statutory ingredient mapping and distinction of precedents could be strengthened.';
      }

      const mentorCharId = isDetective ? 'arjun' : 'vikram';
      const mentorChar = window.CharacterEngine ? window.CharacterEngine.getCharacter(mentorCharId) : null;
      const mentorName = mentorChar ? mentorChar.name : (isDetective ? 'Detective Arjun' : 'Justice Vikram Sahay');

      containerEl.innerHTML = `
        <div class="report-card-wrap">
          <div class="report-card-top">
            <div class="report-title-area">
              <small class="eyebrow" style="color:#dfbf80">Official Case Evaluation & Debrief</small>
              <h2>${caseData.title}</h2>
              <p style="margin:4px 0 0;color:#cbe0ef;font-size:13px">${caseData.caseNumber} · ${caseData.category} · ${caseData.difficulty.toUpperCase()}</p>
            </div>
            <div class="report-overall-score">
              <div class="score-big">${score}<span class="score-max">/100</span></div>
              <small style="color:#dfbf80;font-weight:700">AGGREGATE PERFORMANCE</small>
            </div>
          </div>

          <!-- 100-Point Rubric Grid -->
          <div class="rubric-grid">
            ${isDetective ? `
              <div class="rubric-card">
                <span class="rubric-name">Evidence Analysis</span>
                <span class="rubric-points">${rubric.evidenceAnalysis} / 25</span>
                <div class="rubric-bar"><div class="rubric-fill" style="width:${(rubric.evidenceAnalysis / 25) * 100}%"></div></div>
              </div>
              <div class="rubric-card">
                <span class="rubric-name">Witness Exam</span>
                <span class="rubric-points">${rubric.witnessExam} / 20</span>
                <div class="rubric-bar"><div class="rubric-fill" style="width:${(rubric.witnessExam / 20) * 100}%"></div></div>
              </div>
              <div class="rubric-card">
                <span class="rubric-name">Evidence Board</span>
                <span class="rubric-points">${rubric.evidenceBoard} / 20</span>
                <div class="rubric-bar"><div class="rubric-fill" style="width:${(rubric.evidenceBoard / 20) * 100}%"></div></div>
              </div>
              <div class="rubric-card">
                <span class="rubric-name">Legal Deduction</span>
                <span class="rubric-points">${rubric.legalDeduction} / 25</span>
                <div class="rubric-bar"><div class="rubric-fill gold" style="width:${(rubric.legalDeduction / 25) * 100}%"></div></div>
              </div>
              <div class="rubric-card">
                <span class="rubric-name">Efficiency & Hints</span>
                <span class="rubric-points">${rubric.efficiency} / 10</span>
                <div class="rubric-bar"><div class="rubric-fill" style="width:${(rubric.efficiency / 10) * 100}%"></div></div>
              </div>
            ` : `
              <div class="rubric-card">
                <span class="rubric-name">Fact Assessment</span>
                <span class="rubric-points">${rubric.factAssessment} / 20</span>
                <div class="rubric-bar"><div class="rubric-fill" style="width:${(rubric.factAssessment / 20) * 100}%"></div></div>
              </div>
              <div class="rubric-card">
                <span class="rubric-name">Precedent Application</span>
                <span class="rubric-points">${rubric.precedentApplication} / 25</span>
                <div class="rubric-bar"><div class="rubric-fill gold" style="width:${(rubric.precedentApplication / 25) * 100}%"></div></div>
              </div>
              <div class="rubric-card">
                <span class="rubric-name">Procedural Soundness</span>
                <span class="rubric-points">${rubric.proceduralSoundness} / 25</span>
                <div class="rubric-bar"><div class="rubric-fill" style="width:${(rubric.proceduralSoundness / 25) * 100}%"></div></div>
              </div>
              <div class="rubric-card">
                <span class="rubric-name">Order Drafting</span>
                <span class="rubric-points">${rubric.orderDrafting} / 20</span>
                <div class="rubric-bar"><div class="rubric-fill" style="width:${(rubric.orderDrafting / 20) * 100}%"></div></div>
              </div>
              <div class="rubric-card">
                <span class="rubric-name">Judicial Decorum</span>
                <span class="rubric-points">${rubric.judicialDecorum} / 10</span>
                <div class="rubric-bar"><div class="rubric-fill" style="width:${(rubric.judicialDecorum / 10) * 100}%"></div></div>
              </div>
            `}
          </div>

          <!-- Mentor Critique -->
          <div class="mentor-critique-box">
            ${window.CharacterEngine ? window.CharacterEngine.renderAvatar(mentorCharId) : ''}
            <div class="mentor-speech">
              <h4>${mentorName} — Judicial Critique:</h4>
              <p><strong>${feedbackTitle}:</strong> ${feedbackBody}</p>
              ${scoreResult.chosenOption ? `
                <p style="margin-top:8px;font-size:13px;color:#1e293b"><strong>Your Selected Deduction:</strong> ${scoreResult.chosenOption.text}</p>
                <p style="font-size:13px;color:#137d72"><strong>Legal Rationale:</strong> ${scoreResult.chosenOption.rationale}</p>
              ` : ''}
              ${scoreResult.chosenDecision ? `
                <p style="margin-top:8px;font-size:13px;color:#1e293b"><strong>Your Operative Ruling:</strong> ${scoreResult.chosenDecision.text}</p>
                <p style="font-size:13px;color:#137d72"><strong>Legal Rationale:</strong> ${scoreResult.chosenDecision.rationale}</p>
              ` : ''}
            </div>
          </div>

          <!-- Authoritative Legal Verification Accordion -->
          ${caseData.legalVerification ? `
            <div class="legal-analysis-box">
              <h4>⚖ Authoritative Statutory Foundation & Precedents</h4>
              <div class="statute-box">
                <strong>Governing Statute:</strong> ${caseData.legalVerification.act} (${caseData.legalVerification.section})<br>
                <strong>Statutory Proposition:</strong> ${caseData.legalVerification.proposition}
              </div>
              <div class="precedent-box">
                <strong>Authority / Citation Source:</strong> ${caseData.legalVerification.source}<br>
                <small style="color:#64748b">Verified for UP PCS-J Syllabus · Baseline 2026</small>
              </div>
            </div>
          ` : ''}
        </div>

        <!-- Action Footer -->
        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;margin-top:20px">
          <button type="button" class="btn" id="btnRestartCase">↺ Re-examine Case</button>
          <div style="display:flex;gap:10px">
            <a href="brain-arena.html" class="btn">Arena Dashboard ↗</a>
            <button type="button" class="btn primary" id="btnNextCase">Next Case File ➔</button>
          </div>
        </div>
      `;

      const restartBtn = containerEl.querySelector('#btnRestartCase');
      if (restartBtn && typeof onRestart === 'function') {
        restartBtn.addEventListener('click', onRestart);
      }
      const nextBtn = containerEl.querySelector('#btnNextCase');
      if (nextBtn && typeof onNext === 'function') {
        nextBtn.addEventListener('click', onNext);
      }
    }
  };

  window.CaseEngine = CaseEngine;
})();
