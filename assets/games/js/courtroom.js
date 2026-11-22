/**
 * LEGAL BRAIN ARENA — BE THE JUDGE CONTROLLER (V3.0 Phase 2)
 * Game 4: Be the Judge: The Courtroom
 * Author: Tauqeer Ashraf
 */
(function() {
  'use strict';

  const STAGES = [
    { number: 1, label: 'Call Case', sub: 'Clerk of Court' },
    { number: 2, label: 'Arguments', sub: 'Opposing Counsel' },
    { number: 3, label: 'Exhibits', sub: 'Admissibility' },
    { number: 4, label: 'Inquiry', sub: 'From the Bench' },
    { number: 5, label: 'Issues', sub: 'Framing Questions' },
    { number: 6, label: 'Ruling', sub: 'Operative Decision' },
    { number: 7, label: 'Order Builder', sub: 'Draft Judgment' },
    { number: 8, label: 'Evaluation', sub: 'Mentor Feedback' }
  ];

  let currentHearingIndex = 0;
  let currentStageIndex = 0;
  let activeHearingData = null;

  // Active courtroom session state
  let userState = {
    exhibitsExaminedCount: 0,
    examinedExhibitIds: [],
    framedIssuesIds: [],
    decisionChoiceId: null,
    selectedOrderItems: {
      facts: [],
      law: [],
      operative: []
    },
    hintsUsed: 0,
    startTime: null
  };

  function getHearings() {
    return window.COURTROOM_CASES || [];
  }

  function init() {
    const mainContainer = document.getElementById('courtroomMainMount');
    if (!mainContainer) return;

    const urlParams = new URLSearchParams(window.location.search);
    let caseParam = urlParams.get('case') || urlParams.get('caseId');
    if (caseParam && caseParam.startsWith('case-')) {
      caseParam = 'court-' + caseParam;
    }

    const hearings = getHearings();
    if (caseParam) {
      const foundIdx = hearings.findIndex(c => c.id === caseParam);
      if (foundIdx !== -1) {
        startHearing(foundIdx);
        return;
      }
    }

    renderHearingSelector();
  }

  // =========================================================================
  // VIEW 1: CAUSE LIST & HEARING SELECTOR
  // =========================================================================
  function renderHearingSelector() {
    const mainContainer = document.getElementById('courtroomMainMount');
    if (!mainContainer) return;

    const hearings = getHearings();
    const state = window.GameStorage ? window.GameStorage.getArenaState() : null;
    const completedHearings = (state && state.courtroom && state.courtroom.completedHearings) || {};

    mainContainer.innerHTML = `
      <div class="case-select-header">
        <small class="eyebrow" style="color:#dfbf80">DISTRICT & SESSIONS COURT · JUDICIAL BENCH SIMULATION</small>
        <h2>Cause List of the Day</h2>
        <p>Preside as the Presiding Judge. Hear contested oral submissions, rule on evidentiary admissibility, frame precise issues, deliver interlocutory orders, and draft reasoned judgments.</p>
      </div>

      <div class="case-grid">
        ${hearings.map((h, idx) => {
          const completed = completedHearings[h.id];
          const bestScore = completed ? completed.score : null;
          return `
            <article class="dossier-card ${h.difficulty}">
              <div class="dossier-badge-strip">
                <span>${h.difficulty.toUpperCase()}</span>
                <span>⏱ ~${h.estimatedMinutes} Mins</span>
              </div>
              <div class="dossier-body">
                <span class="dossier-matter-no">${h.caseNumber}</span>
                <h3 class="dossier-title">${h.title}</h3>
                <p class="dossier-synopsis">${h.proceedings && h.proceedings.clerkIntro ? h.proceedings.clerkIntro.text.substring(0, 140) + '...' : ''}</p>
                <div class="dossier-tags">
                  <span class="dossier-tag">🏛 ${h.category}</span>
                  <span class="dossier-tag">§ ${h.legalVerification ? h.legalVerification.section : 'CPC / BNSS'}</span>
                </div>
              </div>
              <div class="dossier-footer">
                ${bestScore !== null ? `
                  <span class="dossier-score-tag">★ Best: ${bestScore}/100</span>
                ` : `
                  <span style="font-size:12px;color:#64748b">Unheard</span>
                `}
                <button type="button" class="btn primary mini" data-hearing-idx="${idx}">Take the Bench ↗</button>
              </div>
            </article>
          `;
        }).join('')}
      </div>
    `;

    const takeBenchBtns = mainContainer.querySelectorAll('button[data-hearing-idx]');
    takeBenchBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const idx = parseInt(btn.getAttribute('data-hearing-idx'), 10);
        startHearing(idx);
      });
    });
  }

  function startHearing(idx) {
    const hearings = getHearings();
    if (!hearings[idx]) return;

    currentHearingIndex = idx;
    currentStageIndex = 0;
    activeHearingData = hearings[idx];

    userState = {
      exhibitsExaminedCount: 0,
      examinedExhibitIds: [],
      framedIssuesIds: [],
      decisionChoiceId: null,
      selectedOrderItems: {
        facts: [],
        law: [],
        operative: []
      },
      hintsUsed: 0,
      startTime: Date.now()
    };

    if (window.DialogueEngine) window.DialogueEngine.clearHistory();
    if (window.GameAudio) window.GameAudio.playGavel();

    renderActiveStage();
  }

  // =========================================================================
  // ACTIVE STAGE CONTROLLER
  // =========================================================================
  function renderActiveStage() {
    const mainContainer = document.getElementById('courtroomMainMount');
    if (!mainContainer || !activeHearingData) return;

    const stepperHtml = window.CaseEngine ? window.CaseEngine.renderStepper(STAGES, currentStageIndex) : '';

    mainContainer.innerHTML = `
      <div class="courtroom-banner">
        <div class="courtroom-banner-title">
          <small class="eyebrow" style="color:#dfbf80">COURT OF RECORD · ${activeHearingData.caseNumber}</small>
          <h2>${activeHearingData.title}</h2>
          <div class="courtroom-banner-sub">
            <span>🏛 ${activeHearingData.category}</span> · 
            <span>⚖ ${activeHearingData.legalVerification ? activeHearingData.legalVerification.section : 'Substantive & Procedural Law'}</span> · 
            <span>⚡ Stage ${currentStageIndex + 1} of ${STAGES.length}</span>
          </div>
        </div>
        <div style="display:flex;gap:8px">
          <button type="button" class="btn mini" id="btnGavelSound" title="Strike the judicial gavel">🔨 Gavel</button>
          <button type="button" class="btn mini" id="btnExitCourt">✕ Rise & Exit</button>
        </div>
      </div>

      ${stepperHtml}

      <div id="courtroomStageMount"></div>
    `;

    const gavelBtn = mainContainer.querySelector('#btnGavelSound');
    if (gavelBtn) {
      gavelBtn.addEventListener('click', () => {
        if (window.GameAudio) window.GameAudio.playGavel();
      });
    }

    const exitBtn = mainContainer.querySelector('#btnExitCourt');
    if (exitBtn) {
      exitBtn.addEventListener('click', () => {
        if (confirm('Rise from the Bench and return to the daily cause list?')) {
          renderHearingSelector();
        }
      });
    }

    const stageMount = mainContainer.querySelector('#courtroomStageMount');

    switch (currentStageIndex) {
      case 0:
        renderStage1CallCase(stageMount);
        break;
      case 1:
        renderStage2Arguments(stageMount);
        break;
      case 2:
        renderStage3Exhibits(stageMount);
        break;
      case 3:
        renderStage4Inquiry(stageMount);
        break;
      case 4:
        renderStage5Issues(stageMount);
        break;
      case 5:
        renderStage6Decision(stageMount);
        break;
      case 6:
        renderStage7OrderBuilder(stageMount);
        break;
      case 7:
        renderStage8Evaluation(stageMount);
        break;
    }
  }

  // -------------------------------------------------------------------------
  // STAGE 1: CALL THE CASE
  // -------------------------------------------------------------------------
  function renderStage1CallCase(mountEl) {
    const clerkIntro = (activeHearingData.proceedings && activeHearingData.proceedings.clerkIntro) || {
      speaker: 'nandini',
      text: 'Calling the next matter on the cause list for urgent interlocutory hearing.'
    };

    const wrap = document.createElement('div');
    mountEl.appendChild(wrap);

    if (window.DialogueEngine) {
      window.DialogueEngine.renderScene(wrap, {
        title: 'Stage 1: Calling of the Cause List — Court Clerk',
        characterId: 'nandini',
        initialText: clerkIntro.text,
        questions: [
          {
            question: 'Are all parties properly served and present before the Bench?',
            answer: 'Yes, Your Honour. Both learned counsels are present in robes and ready to address the Court on the interlocutory prayer.',
            discoversFact: 'Pleadings complete; both sides represented.'
          },
          {
            question: 'What is the immediate statutory relief sought today?',
            answer: `The applicant seeks urgent interlocutory relief under ${activeHearingData.legalVerification ? activeHearingData.legalVerification.section : 'governing procedure'}.`,
            discoversFact: 'Interlocutory prayer formulated.'
          }
        ]
      });
    }

    const navBar = document.createElement('div');
    navBar.style.cssText = 'display:flex;justify-content:flex-end;margin-top:20px;';
    navBar.innerHTML = `<button type="button" class="btn primary" id="btnGoStage2">Hear Oral Submissions ➔</button>`;
    mountEl.appendChild(navBar);

    navBar.querySelector('#btnGoStage2').addEventListener('click', () => {
      currentStageIndex = 1;
      renderActiveStage();
    });
  }

  // -------------------------------------------------------------------------
  // STAGE 2: ORAL ARGUMENTS OF OPPOSING COUNSEL
  // -------------------------------------------------------------------------
  function renderStage2Arguments(mountEl) {
    const args = (activeHearingData.proceedings && activeHearingData.proceedings.arguments) || [];
    const prosecutionArg = args.find(a => a.speaker === 'ananya') || args[0] || { speaker: 'ananya', text: 'Prosecution submission.' };
    const defenceArg = args.find(a => a.speaker === 'aditya') || args[1] || { speaker: 'aditya', text: 'Defence submission.' };

    mountEl.innerHTML = `
      <div style="background:#fff;border:1px solid #cbd5e1;border-radius:12px;padding:18px 22px;margin-bottom:20px;box-shadow:0 3px 12px rgba(20,44,70,0.05)">
        <h3 style="font-family:Georgia,serif;font-size:18px;color:#142c46;margin:0 0 6px">Stage 2: Bar Submissions — Arguments of Opposing Counsel</h3>
        <p style="font-size:13px;color:#64748b;margin:0">Weigh the substantive submissions presented by the learned Public Prosecutor / Plaintiff Counsel and learned Defence Counsel.</p>
      </div>

      <div class="courtroom-bench-stage">
        <!-- Prosecution / Plaintiff Counsel Podium -->
        <div class="counsel-podium prosecution">
          <div class="counsel-podium-header">
            <span>⚖ ${prosecutionArg.counselType || 'Public Prosecutor / Plaintiff'}</span>
            <span>Adv. Ananya Rao</span>
          </div>
          <div class="counsel-body">
            <div class="counsel-profile">
              <div class="counsel-avatar-sm">
                <img src="assets/games/images/characters/courtroom/ananya.svg" alt="Adv. Ananya Rao">
              </div>
              <div>
                <strong style="color:#142c46;font-size:14px">Adv. Ananya Rao</strong>
                <div style="font-size:11px;color:#64748b">Lead Counsel</div>
              </div>
            </div>
            <div class="counsel-speech-area">
              <p style="margin:0;line-height:1.6">${prosecutionArg.text}</p>
            </div>
          </div>
        </div>

        <!-- Defence Counsel Podium -->
        <div class="counsel-podium defence">
          <div class="counsel-podium-header">
            <span>🛡 ${defenceArg.counselType || 'Defence / Respondent'}</span>
            <span>Adv. Aditya Malhotra</span>
          </div>
          <div class="counsel-body">
            <div class="counsel-profile">
              <div class="counsel-avatar-sm">
                <img src="assets/games/images/characters/courtroom/aditya.svg" alt="Adv. Aditya Malhotra">
              </div>
              <div>
                <strong style="color:#142c46;font-size:14px">Adv. Aditya Malhotra</strong>
                <div style="font-size:11px;color:#64748b">Defence Advocate</div>
              </div>
            </div>
            <div class="counsel-speech-area">
              <p style="margin:0;line-height:1.6">${defenceArg.text}</p>
            </div>
          </div>
        </div>
      </div>

      <div style="display:flex;justify-content:space-between;margin-top:22px">
        <button type="button" class="btn" id="btnBackStage1">← Back to Cause List</button>
        <button type="button" class="btn primary" id="btnGoStage3">Examine Exhibits & Records ➔</button>
      </div>
    `;

    mountEl.querySelector('#btnBackStage1').addEventListener('click', () => {
      currentStageIndex = 0;
      renderActiveStage();
    });

    mountEl.querySelector('#btnGoStage3').addEventListener('click', () => {
      currentStageIndex = 2;
      renderActiveStage();
    });
  }

  // -------------------------------------------------------------------------
  // STAGE 3: EXHIBITS & EVIDENTIARY ADMISSIBILITY
  // -------------------------------------------------------------------------
  function renderStage3Exhibits(mountEl) {
    const exhibits = (activeHearingData.proceedings && activeHearingData.proceedings.exhibits) || [];

    mountEl.innerHTML = `
      <div style="background:#fff;border:1px solid #cbd5e1;border-radius:12px;padding:18px 22px;margin-bottom:20px;box-shadow:0 3px 12px rgba(20,44,70,0.05)">
        <h3 style="font-family:Georgia,serif;font-size:18px;color:#142c46;margin:0 0 6px">Stage 3: Evidentiary Records & Exhibit Inspection</h3>
        <p style="font-size:13px;color:#64748b;margin:0">Inspect documentary, digital and physical exhibits marked on record. Assess admissibility under the Bharatiya Sakshya Adhiniyam, 2023.</p>
      </div>

      <div class="exhibits-wrap">
        <div class="exhibit-tabs" id="exhibitTabsArea">
          ${exhibits.map((ex, idx) => `
            <button type="button" class="exhibit-tab-btn ${idx === 0 ? 'active' : ''}" data-ex-idx="${idx}">
              📄 Exhibit ${idx + 1}: ${ex.name}
            </button>
          `).join('')}
        </div>
        <div id="exhibitDisplayArea"></div>
      </div>

      <div style="display:flex;justify-content:space-between;margin-top:22px">
        <button type="button" class="btn" id="btnBackStage2">← Back to Counsel Arguments</button>
        <button type="button" class="btn primary" id="btnGoStage4">Judicial Inquiry from the Bench ➔</button>
      </div>
    `;

    const displayArea = mountEl.querySelector('#exhibitDisplayArea');
    const tabBtns = mountEl.querySelectorAll('.exhibit-tab-btn');

    function showExhibit(idx) {
      tabBtns.forEach((b, i) => {
        if (i === idx) b.classList.add('active');
        else b.classList.remove('active');
      });

      const ex = exhibits[idx];
      if (!ex) return;

      if (!userState.examinedExhibitIds.includes(ex.id)) {
        userState.examinedExhibitIds.push(ex.id);
        userState.exhibitsExaminedCount = userState.examinedExhibitIds.length;
      }

      displayArea.innerHTML = `
        <div class="exhibit-sheet">
          <div class="exhibit-seal-stamp">OFFICIAL COURT RECORD</div>
          <span class="evidence-tag-code">EXHIBIT IDENTIFIER: ${ex.id.toUpperCase()}</span>
          <h4 style="font-family:Georgia,serif;font-size:18px;color:#142c46;margin:12px 0 6px">${ex.name}</h4>
          <p style="font-size:12px;color:#64748b;margin-bottom:14px"><strong>Nature:</strong> ${ex.nature}</p>
          <div style="background:#fff;border:1px solid #cbd5e1;border-radius:8px;padding:16px;margin-bottom:14px">
            <strong style="font-size:12px;color:#137d72;text-transform:uppercase">Evidentiary Role in Pleadings:</strong>
            <p style="font-size:14px;color:#1e293b;line-height:1.6;margin:6px 0 0">${ex.evidentiaryRole}</p>
          </div>
          <div style="font-size:13px;color:#64748b">
            <strong>Judicial Probative Weight:</strong> ${ex.weight}
          </div>
        </div>
      `;

      if (window.GameAudio) window.GameAudio.playPaper();
    }

    tabBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const idx = parseInt(btn.getAttribute('data-ex-idx'), 10);
        showExhibit(idx);
      });
    });

    if (exhibits.length > 0) showExhibit(0);

    mountEl.querySelector('#btnBackStage2').addEventListener('click', () => {
      currentStageIndex = 1;
      renderActiveStage();
    });

    mountEl.querySelector('#btnGoStage4').addEventListener('click', () => {
      currentStageIndex = 3;
      renderActiveStage();
    });
  }

  // -------------------------------------------------------------------------
  // STAGE 4: JUDICIAL QUESTIONS FROM BENCH
  // -------------------------------------------------------------------------
  function renderStage4Inquiry(mountEl) {
    const questions = (activeHearingData.proceedings && activeHearingData.proceedings.questionsToParties) || [];

    mountEl.innerHTML = `
      <div style="background:#fff;border:1px solid #cbd5e1;border-radius:12px;padding:18px 22px;margin-bottom:20px;box-shadow:0 3px 12px rgba(20,44,70,0.05)">
        <h3 style="font-family:Georgia,serif;font-size:18px;color:#142c46;margin:0 0 6px">Stage 4: Judicial Inquiry from the Bench</h3>
        <p style="font-size:13px;color:#64748b;margin:0">Put targeted questions to both counsels to clarify statutory compliance, test factual veracity, and narrow disputed legal propositions.</p>
      </div>

      <div class="order-sections-list">
        ${questions.map((q, idx) => `
          <div class="order-block-card">
            <div class="order-block-label">
              <span>Question ${idx + 1} to ${q.target}</span>
              <span style="font-size:11px;color:#137d72;font-weight:700">BENCH INTERROGATION</span>
            </div>
            <div style="font-size:14px;color:#142c46;font-weight:600;margin-bottom:10px">"${q.question}"</div>
            <div style="background:#ffffff;border:1px solid #cbd5e1;border-radius:8px;padding:12px 14px;font-size:13px;color:#334155;line-height:1.5">
              <strong>Counsel's Response on Affidavit / at Bar:</strong><br>
              ${q.response}
            </div>
          </div>
        `).join('')}
      </div>

      <div style="display:flex;justify-content:space-between;margin-top:22px">
        <button type="button" class="btn" id="btnBackStage3">← Back to Exhibits</button>
        <button type="button" class="btn primary" id="btnGoStage5">Frame Legal Issues ➔</button>
      </div>
    `;

    mountEl.querySelector('#btnBackStage3').addEventListener('click', () => {
      currentStageIndex = 2;
      renderActiveStage();
    });

    mountEl.querySelector('#btnGoStage5').addEventListener('click', () => {
      currentStageIndex = 4;
      renderActiveStage();
    });
  }

  // -------------------------------------------------------------------------
  // STAGE 5: FRAMING OF LEGAL ISSUES
  // -------------------------------------------------------------------------
  function renderStage5Issues(mountEl) {
    const issues = (activeHearingData.proceedings && activeHearingData.proceedings.legalIssues) || [];

    mountEl.innerHTML = `
      <div style="background:#fff;border:1px solid #cbd5e1;border-radius:12px;padding:20px 24px;margin-bottom:24px;box-shadow:0 4px 16px rgba(20,44,70,0.06)">
        <small class="eyebrow" style="color:#dfbf80">STAGE 5: FRAMING OF RELEVANT LEGAL ISSUES</small>
        <h3 style="font-family:Georgia,serif;font-size:20px;color:#142c46;margin:6px 0 10px">Select the Core Points of Law Arising for Determination:</h3>
        <p style="font-size:14px;color:#64748b;margin:0">A judge must frame only genuine issues of law and fact arising from pleadings, rejecting extraneous or non-determinative points.</p>
      </div>

      <div class="order-sections-list">
        <div class="order-block-card">
          <div class="order-block-options">
            ${issues.map(issue => {
              const isChecked = userState.framedIssuesIds.includes(issue.id);
              return `
                <label class="order-choice-card ${isChecked ? 'selected' : ''}">
                  <input type="checkbox" class="order-choice-radio issue-checkbox" value="${issue.id}" ${isChecked ? 'checked' : ''}>
                  <div style="flex:1">
                    <div style="font-weight:600;font-size:14px;color:#1e293b;line-height:1.45">${issue.text}</div>
                  </div>
                </label>
              `;
            }).join('')}
          </div>
        </div>
      </div>

      <div style="display:flex;justify-content:space-between;margin-top:24px">
        <button type="button" class="btn" id="btnBackStage4">← Back to Bench Inquiry</button>
        <button type="button" class="btn primary" id="btnGoStage6" ${userState.framedIssuesIds.length === 0 ? 'disabled' : ''}>
          Proceed to Operative Ruling ➔
        </button>
      </div>
    `;

    const checkboxes = mountEl.querySelectorAll('.issue-checkbox');
    const goBtn = mountEl.querySelector('#btnGoStage6');

    checkboxes.forEach(cb => {
      cb.addEventListener('change', () => {
        if (cb.checked) {
          if (!userState.framedIssuesIds.includes(cb.value)) userState.framedIssuesIds.push(cb.value);
          cb.closest('.order-choice-card').classList.add('selected');
        } else {
          userState.framedIssuesIds = userState.framedIssuesIds.filter(id => id !== cb.value);
          cb.closest('.order-choice-card').classList.remove('selected');
        }
        if (goBtn) goBtn.disabled = userState.framedIssuesIds.length === 0;
        if (window.GameAudio) window.GameAudio.playCardFlip();
      });
    });

    mountEl.querySelector('#btnBackStage4').addEventListener('click', () => {
      currentStageIndex = 3;
      renderActiveStage();
    });

    mountEl.querySelector('#btnGoStage6').addEventListener('click', () => {
      currentStageIndex = 5;
      renderActiveStage();
    });
  }

  // -------------------------------------------------------------------------
  // STAGE 6: JUDICIAL DECISION & OPERATIVE RULING
  // -------------------------------------------------------------------------
  function renderStage6Decision(mountEl) {
    const decisions = (activeHearingData.proceedings && activeHearingData.proceedings.decisionOptions) || [];

    mountEl.innerHTML = `
      <div style="background:#fff;border:1px solid #cbd5e1;border-radius:12px;padding:20px 24px;margin-bottom:24px;box-shadow:0 4px 16px rgba(20,44,70,0.06)">
        <small class="eyebrow" style="color:#dfbf80">STAGE 6: DELIVER THE OPERATIVE JUDICIAL ORDER</small>
        <h3 style="font-family:Georgia,serif;font-size:20px;color:#142c46;margin:6px 0 10px">Pronounce the Court's Determination:</h3>
        <p style="font-size:14px;color:#64748b;margin:0">Select the legally sound operative direction in conformity with statutory mandates and binding Supreme Court ratio.</p>
      </div>

      <div class="order-sections-list">
        <div class="order-block-card">
          <div class="order-block-options">
            ${decisions.map(dec => `
              <label class="order-choice-card ${userState.decisionChoiceId === dec.id ? 'selected' : ''}">
                <input type="radio" name="decisionOption" class="order-choice-radio" value="${dec.id}" ${userState.decisionChoiceId === dec.id ? 'checked' : ''}>
                <div style="flex:1">
                  <div style="font-weight:600;font-size:14px;color:#1e293b;line-height:1.45">${dec.text}</div>
                </div>
              </label>
            `).join('')}
          </div>
        </div>
      </div>

      <div style="display:flex;justify-content:space-between;margin-top:24px">
        <button type="button" class="btn" id="btnBackStage5">← Back to Issues</button>
        <button type="button" class="btn primary" id="btnGoStage7" ${!userState.decisionChoiceId ? 'disabled' : ''}>
          Draft Reasoned Order ➔
        </button>
      </div>
    `;

    const radioInputs = mountEl.querySelectorAll('input[name="decisionOption"]');
    const goBtn = mountEl.querySelector('#btnGoStage7');

    radioInputs.forEach(input => {
      input.addEventListener('change', () => {
        userState.decisionChoiceId = input.value;
        const cards = mountEl.querySelectorAll('.order-choice-card');
        cards.forEach(c => c.classList.remove('selected'));
        input.closest('.order-choice-card').classList.add('selected');
        if (goBtn) goBtn.disabled = false;
        if (window.GameAudio) window.GameAudio.playGavel();
      });
    });

    mountEl.querySelector('#btnBackStage5').addEventListener('click', () => {
      currentStageIndex = 4;
      renderActiveStage();
    });

    mountEl.querySelector('#btnGoStage7').addEventListener('click', () => {
      currentStageIndex = 6;
      renderActiveStage();
    });
  }

  // -------------------------------------------------------------------------
  // STAGE 7: STRUCTURED REASONED ORDER BUILDER
  // -------------------------------------------------------------------------
  function renderStage7OrderBuilder(mountEl) {
    const builder = (activeHearingData.proceedings && activeHearingData.proceedings.orderBuilder) || {
      factsPool: [],
      lawPool: [],
      operativeOrderPool: []
    };

    mountEl.innerHTML = `
      <div class="order-builder-wrap">
        <div class="order-builder-header">
          <small class="eyebrow" style="color:#dfbf80">STAGE 7: STRUCTURED REASONED ORDER BUILDER</small>
          <h3>Drafting the Formal Judicial Order</h3>
          <p>Assemble the essential elements of a legally sound judicial order: Findings of Fact, Substantive Law & Precedents, and Operative Directions.</p>
        </div>

        <div class="order-sections-list">
          <!-- Section 1: Findings of Fact -->
          <div class="order-block-card">
            <div class="order-block-label">
              <span>Section I: Statement of Material Facts & Pleadings</span>
              <span style="font-size:11px;color:#137d72">Select verified facts to incorporate</span>
            </div>
            <div class="order-block-options">
              ${builder.factsPool.map(f => {
                const isSelected = userState.selectedOrderItems.facts.includes(f.id);
                return `
                  <label class="order-choice-card ${isSelected ? 'selected' : ''}">
                    <input type="checkbox" class="order-choice-radio order-fact-cb" value="${f.id}" ${isSelected ? 'checked' : ''}>
                    <div style="flex:1;font-size:13px;line-height:1.45;color:#1e293b">${f.text}</div>
                  </label>
                `;
              }).join('')}
            </div>
          </div>

          <!-- Section 2: Discussion of Law & Precedents -->
          <div class="order-block-card">
            <div class="order-block-label">
              <span>Section II: Applicable Law & Governing Precedents</span>
              <span style="font-size:11px;color:#137d72">Select governing ratio decidendi</span>
            </div>
            <div class="order-block-options">
              ${builder.lawPool.map(l => {
                const isSelected = userState.selectedOrderItems.law.includes(l.id);
                return `
                  <label class="order-choice-card ${isSelected ? 'selected' : ''}">
                    <input type="checkbox" class="order-choice-radio order-law-cb" value="${l.id}" ${isSelected ? 'checked' : ''}>
                    <div style="flex:1;font-size:13px;line-height:1.45;color:#1e293b">${l.text}</div>
                  </label>
                `;
              }).join('')}
            </div>
          </div>

          <!-- Section 3: Operative Order -->
          <div class="order-block-card">
            <div class="order-block-label">
              <span>Section III: Formal Operative Order & Direction</span>
              <span style="font-size:11px;color:#137d72">Select the operative decree clause</span>
            </div>
            <div class="order-block-options">
              ${builder.operativeOrderPool.map(o => {
                const isSelected = userState.selectedOrderItems.operative.includes(o.id);
                return `
                  <label class="order-choice-card ${isSelected ? 'selected' : ''}">
                    <input type="checkbox" class="order-choice-radio order-op-cb" value="${o.id}" ${isSelected ? 'checked' : ''}>
                    <div style="flex:1;font-size:13px;line-height:1.45;color:#1e293b">${o.text}</div>
                  </label>
                `;
              }).join('')}
            </div>
          </div>
        </div>
      </div>

      <div style="display:flex;justify-content:space-between;margin-top:24px">
        <button type="button" class="btn" id="btnBackStage6">← Back to Ruling</button>
        <button type="button" class="btn primary" id="btnSubmitOrder">
          Seal and Deliver Judicial Order ➔
        </button>
      </div>
    `;

    // Bind checkboxes
    const bindPool = (selector, poolKey) => {
      mountEl.querySelectorAll(selector).forEach(cb => {
        cb.addEventListener('change', () => {
          if (cb.checked) {
            if (!userState.selectedOrderItems[poolKey].includes(cb.value)) {
              userState.selectedOrderItems[poolKey].push(cb.value);
            }
            cb.closest('.order-choice-card').classList.add('selected');
          } else {
            userState.selectedOrderItems[poolKey] = userState.selectedOrderItems[poolKey].filter(id => id !== cb.value);
            cb.closest('.order-choice-card').classList.remove('selected');
          }
          if (window.GameAudio) window.GameAudio.playCardFlip();
        });
      });
    };

    bindPool('.order-fact-cb', 'facts');
    bindPool('.order-law-cb', 'law');
    bindPool('.order-op-cb', 'operative');

    mountEl.querySelector('#btnBackStage6').addEventListener('click', () => {
      currentStageIndex = 5;
      renderActiveStage();
    });

    mountEl.querySelector('#btnSubmitOrder').addEventListener('click', () => {
      currentStageIndex = 7;
      renderActiveStage();
    });
  }

  // -------------------------------------------------------------------------
  // STAGE 8: MENTOR EVALUATION & FEEDBACK
  // -------------------------------------------------------------------------
  function renderStage8Evaluation(mountEl) {
    const scoreResult = window.CaseEngine ? window.CaseEngine.calculateCourtroomScore(activeHearingData, {
      exhibitsExaminedCount: userState.exhibitsExaminedCount,
      framedIssuesIds: userState.framedIssuesIds,
      decisionChoiceId: userState.decisionChoiceId,
      selectedOrderItems: userState.selectedOrderItems,
      hintsUsed: userState.hintsUsed
    }) : { score: 80, maxScore: 100, rubric: {} };

    // Record game result
    if (window.GameStorage) {
      window.GameStorage.recordGameResult({
        game: 'courtroom',
        caseId: activeHearingData.id,
        title: activeHearingData.title,
        difficulty: activeHearingData.difficulty,
        score: scoreResult.score,
        accuracy: scoreResult.score,
        duration: Math.round((Date.now() - (userState.startTime || Date.now())) / 1000),
        rubric: scoreResult.rubric,
        isVictory: scoreResult.score >= 60,
        xpEarned: Math.round(scoreResult.score * 1.5)
      });
    }

    if (scoreResult.score >= 60 && window.GameAudio) {
      window.GameAudio.playVictory();
    }

    if (window.CaseEngine) {
      window.CaseEngine.renderDebrief(
        mountEl,
        activeHearingData,
        scoreResult,
        'courtroom',
        () => {
          // Restart hearing
          startHearing(currentHearingIndex);
        },
        () => {
          // Next hearing
          const hearings = getHearings();
          const nextIdx = (currentHearingIndex + 1) % hearings.length;
          startHearing(nextIdx);
        }
      );
    }
  }

  window.CourtroomController = {
    init: init,
    startHearing: startHearing,
    renderHearingSelector: renderHearingSelector
  };

  document.addEventListener('DOMContentLoaded', init);
})();
