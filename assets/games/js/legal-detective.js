/**
 * LEGAL BRAIN ARENA — LEGAL DETECTIVE CONTROLLER (V3.0 Phase 2)
 * Game 3: Legal Detective: The Case Files
 * Author: Tauqeer Ashraf
 */
(function() {
  'use strict';

  const STAGES = [
    { number: 1, label: 'Briefing', sub: 'Case Dossier' },
    { number: 2, label: 'Evidence', sub: 'Exhibits Inspection' },
    { number: 3, label: 'Witnesses', sub: 'Interrogation' },
    { number: 4, label: 'Evidence Board', sub: 'Clue Connection' },
    { number: 5, label: 'Deduction', sub: 'Formulate Charges' },
    { number: 6, label: 'Report', sub: 'Case Debrief' }
  ];

  let currentCaseIndex = 0;
  let currentStageIndex = 0;
  let activeCaseData = null;

  // Active investigation state
  let userState = {
    evidenceMarks: {}, // evId -> 'relevant'|'possibly_relevant'|'irrelevant'
    examinedEvIds: [],
    factsDiscovered: [],
    boardInstance: null,
    boardEvaluation: null,
    deductionChoiceId: null,
    hintsUsed: 0,
    startTime: null
  };

  function getCases() {
    return window.DETECTIVE_CASES || [];
  }

  function init() {
    const mainContainer = document.getElementById('detectiveMainMount');
    if (!mainContainer) return;

    // Check URL parameters for case selection (e.g. ?case=det-case-1, ?caseId=case-1)
    const urlParams = new URLSearchParams(window.location.search);
    let caseParam = urlParams.get('case') || urlParams.get('caseId');
    if (caseParam && caseParam.startsWith('case-')) {
      caseParam = 'det-' + caseParam;
    }

    const cases = getCases();
    if (caseParam) {
      const foundIdx = cases.findIndex(c => c.id === caseParam);
      if (foundIdx !== -1) {
        startCase(foundIdx);
        return;
      }
    }

    // Check if there is an active session in GameStorage
    const savedActive = window.GameStorage ? window.GameStorage.getDetectiveActive() : null;
    if (savedActive && savedActive.caseId) {
      const foundIdx = cases.findIndex(c => c.id === savedActive.caseId);
      if (foundIdx !== -1) {
        // Can resume or show selector
      }
    }

    renderCaseSelector();
  }

  // =========================================================================
  // VIEW 1: CASE DOSSIER SELECTOR
  // =========================================================================
  function renderCaseSelector() {
    const mainContainer = document.getElementById('detectiveMainMount');
    if (!mainContainer) return;

    const cases = getCases();
    const state = window.GameStorage ? window.GameStorage.getArenaState() : null;
    const completedCases = (state && state.detective && state.detective.completedCases) || {};

    mainContainer.innerHTML = `
      <div class="case-select-header">
        <small class="eyebrow" style="color:#dfbf80">CRIMINAL INVESTIGATION BUREAU · BNS 2023</small>
        <h2>Select Case Dossier</h2>
        <p>Analyze circumstantial evidence, examine witnesses, pin clues to statutory ingredients, and deduce exact offences under the Bharatiya Nyaya Sanhita, 2023.</p>
      </div>

      <div class="case-grid">
        ${cases.map((c, idx) => {
          const completed = completedCases[c.id];
          const bestScore = completed ? completed.score : null;
          return `
            <article class="dossier-card ${c.difficulty}">
              <div class="dossier-badge-strip">
                <span>${c.difficulty.toUpperCase()}</span>
                <span>⏱ ~${c.estimatedMinutes} Mins</span>
              </div>
              <div class="dossier-body">
                <span class="dossier-matter-no">${c.caseNumber}</span>
                <h3 class="dossier-title">${c.title}</h3>
                <p class="dossier-synopsis">${c.briefing ? c.briefing.text.substring(0, 140) + '...' : ''}</p>
                <div class="dossier-tags">
                  <span class="dossier-tag">⚖ ${c.category}</span>
                  <span class="dossier-tag">§ ${c.legalVerification ? c.legalVerification.act : 'BNS 2023'}</span>
                </div>
              </div>
              <div class="dossier-footer">
                ${bestScore !== null ? `
                  <span class="dossier-score-tag">★ Best: ${bestScore}/100</span>
                ` : `
                  <span style="font-size:12px;color:#64748b">Unexamined</span>
                `}
                <button type="button" class="btn primary mini" data-case-idx="${idx}">Open Dossier ↗</button>
              </div>
            </article>
          `;
        }).join('')}
      </div>
    `;

    const openBtns = mainContainer.querySelectorAll('button[data-case-idx]');
    openBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const idx = parseInt(btn.getAttribute('data-case-idx'), 10);
        startCase(idx);
      });
    });
  }

  function startCase(idx) {
    const cases = getCases();
    if (!cases[idx]) return;

    currentCaseIndex = idx;
    currentStageIndex = 0;
    activeCaseData = cases[idx];

    userState = {
      evidenceMarks: {},
      examinedEvIds: [],
      factsDiscovered: [],
      boardInstance: null,
      boardEvaluation: null,
      deductionChoiceId: null,
      hintsUsed: 0,
      startTime: Date.now()
    };

    if (window.DialogueEngine) window.DialogueEngine.clearHistory();
    if (window.GameAudio) window.GameAudio.playPaper();

    renderActiveStage();
  }

  // =========================================================================
  // ACTIVE STAGE CONTROLLER
  // =========================================================================
  function renderActiveStage() {
    const mainContainer = document.getElementById('detectiveMainMount');
    if (!mainContainer || !activeCaseData) return;

    const stepperHtml = window.CaseEngine ? window.CaseEngine.renderStepper(STAGES, currentStageIndex) : '';

    mainContainer.innerHTML = `
      <div class="bureau-header-banner">
        <div class="bureau-banner-info">
          <small class="eyebrow" style="color:#dfbf80">Active Case File · ${activeCaseData.caseNumber}</small>
          <h2>${activeCaseData.title}</h2>
          <div class="bureau-banner-meta">
            <span>⚖ ${activeCaseData.category}</span>
            <span>🎯 Target Statute: ${activeCaseData.legalVerification ? activeCaseData.legalVerification.section : 'BNS'}</span>
            <span>⚡ Stage ${currentStageIndex + 1} of ${STAGES.length}</span>
          </div>
        </div>
        <div>
          <button type="button" class="btn mini" id="btnExitToDossiers">✕ Exit Case</button>
        </div>
      </div>

      ${stepperHtml}

      <div id="detectiveStageMount"></div>
    `;

    const exitBtn = mainContainer.querySelector('#btnExitToDossiers');
    if (exitBtn) {
      exitBtn.addEventListener('click', () => {
        if (confirm('Exit current investigation and return to dossier selection?')) {
          renderCaseSelector();
        }
      });
    }

    const stageMount = mainContainer.querySelector('#detectiveStageMount');

    switch (currentStageIndex) {
      case 0:
        renderStage1Briefing(stageMount);
        break;
      case 1:
        renderStage2Evidence(stageMount);
        break;
      case 2:
        renderStage3Witnesses(stageMount);
        break;
      case 3:
        renderStage4Board(stageMount);
        break;
      case 4:
        renderStage5Deduction(stageMount);
        break;
      case 5:
        renderStage6Report(stageMount);
        break;
    }
  }

  // -------------------------------------------------------------------------
  // STAGE 1: BRIEFING
  // -------------------------------------------------------------------------
  function renderStage1Briefing(mountEl) {
    const briefing = activeCaseData.briefing || { speaker: 'arjun', text: 'No briefing available.' };

    const wrap = document.createElement('div');
    mountEl.appendChild(wrap);

    if (window.DialogueEngine) {
      window.DialogueEngine.renderScene(wrap, {
        title: 'Stage 1: Case Briefing & Initial Facts',
        characterId: briefing.speaker || 'arjun',
        initialText: briefing.text,
        questions: [
          {
            question: 'What are the core initial elements reported by the complainant?',
            answer: `The primary allegation concerns ${activeCaseData.category}. We must analyze physical possession, intention at inception, and whether any statutory exceptions apply.`,
            discoversFact: 'Baseline factual timeline established.'
          },
          {
            question: 'What physical exhibits and witness leads do we have so far?',
            answer: `Officer Rohan has gathered ${activeCaseData.evidence.length} physical/digital exhibits, and we have ${activeCaseData.witnesses.length} persons of interest ready for interrogation.`,
            discoversFact: 'Full exhibit and witness manifest unlocked.'
          }
        ],
        onFactDiscovered: (fact) => {
          if (!userState.factsDiscovered.includes(fact)) {
            userState.factsDiscovered.push(fact);
          }
        }
      });
    }

    const navBar = document.createElement('div');
    navBar.style.cssText = 'display:flex;justify-content:flex-end;margin-top:20px;';
    navBar.innerHTML = `<button type="button" class="btn primary" id="btnGoStage2">Proceed to Evidence Examination ➔</button>`;
    mountEl.appendChild(navBar);

    navBar.querySelector('#btnGoStage2').addEventListener('click', () => {
      currentStageIndex = 1;
      renderActiveStage();
    });
  }

  // -------------------------------------------------------------------------
  // STAGE 2: EVIDENCE EXAMINATION
  // -------------------------------------------------------------------------
  function renderStage2Evidence(mountEl) {
    const evidenceList = activeCaseData.evidence || [];

    mountEl.innerHTML = `
      <div style="background:#fff;border:1px solid #cbd5e1;border-radius:12px;padding:18px 22px;margin-bottom:20px;box-shadow:0 3px 12px rgba(20,44,70,0.05)">
        <h3 style="font-family:Georgia,serif;font-size:18px;color:#142c46;margin:0 0 6px">Stage 2: Exhibits & Evidence Verification</h3>
        <p style="font-size:13px;color:#64748b;margin:0">Click each exhibit to review forensic details, verify authenticity, and classify its legal relevance as <strong>Relevant</strong>, <strong>Possibly Relevant</strong>, or <strong>Irrelevant</strong>.</p>
      </div>

      <div class="evidence-grid" id="evidenceGridArea">
        ${evidenceList.map(ev => {
          const mark = userState.evidenceMarks[ev.id] || 'unexamined';
          const isExamined = userState.examinedEvIds.includes(ev.id);
          return `
            <div class="evidence-card ${isExamined ? 'examined' : ''}" data-ev-id="${ev.id}">
              <div class="evidence-tag-top">
                <span class="evidence-tag-code">EXHIBIT #${ev.id}</span>
                <span class="evidence-type-badge">${ev.type.toUpperCase()}</span>
              </div>
              <h4 class="evidence-card-title">${ev.name}</h4>
              <p class="evidence-card-desc">${ev.summary}</p>
              <div class="evidence-status-pill ${mark}">
                ${mark === 'unexamined' ? '🔍 Click to Inspect' : mark.replace('_', ' ').toUpperCase()}
              </div>
            </div>
          `;
        }).join('')}
      </div>

      <div style="display:flex;justify-content:space-between;margin-top:22px">
        <button type="button" class="btn" id="btnBackStage1">← Back to Briefing</button>
        <button type="button" class="btn primary" id="btnGoStage3">Proceed to Witness Interrogation ➔</button>
      </div>
    `;

    // Modal inspection
    const evCards = mountEl.querySelectorAll('.evidence-card');
    evCards.forEach(card => {
      card.addEventListener('click', () => {
        const evId = card.getAttribute('data-ev-id');
        const ev = evidenceList.find(e => e.id === evId);
        if (ev) openEvidenceModal(ev);
      });
    });

    mountEl.querySelector('#btnBackStage1').addEventListener('click', () => {
      currentStageIndex = 0;
      renderActiveStage();
    });

    mountEl.querySelector('#btnGoStage3').addEventListener('click', () => {
      currentStageIndex = 2;
      renderActiveStage();
    });
  }

  function openEvidenceModal(ev) {
    let modal = document.getElementById('evidenceInspectModal');
    if (!modal) {
      modal = document.createElement('div');
      modal.id = 'evidenceInspectModal';
      modal.className = 'evidence-modal';
      document.body.appendChild(modal);
    }

    const currentMark = userState.evidenceMarks[ev.id] || null;

    modal.innerHTML = `
      <div class="evidence-modal-window">
        <div class="evidence-modal-header">
          <h3>Examine Exhibit: ${ev.name}</h3>
          <button type="button" class="dialogue-btn-sm" id="btnCloseEvModal">✕ Close</button>
        </div>
        <div class="evidence-modal-body">
          <div>
            <span class="evidence-tag-code">TYPE: ${ev.type.toUpperCase()}</span>
            <p style="font-size:14px;color:#1e293b;line-height:1.6;margin-top:10px">${ev.summary}</p>
          </div>
          <div style="background:#f8fafc;border-left:4px solid #137d72;padding:12px 16px;border-radius:6px">
            <strong style="font-size:12px;color:#137d72;text-transform:uppercase">Forensic & Evidentiary Analysis</strong>
            <p style="font-size:13px;color:#334155;line-height:1.5;margin:6px 0 0">${ev.detailedAnalysis || 'No specialized analysis notes.'}</p>
          </div>
          <div class="evidence-modal-marking">
            <label style="font-size:12px;font-weight:700;color:#142c46;text-transform:uppercase">Determine Legal Relevance under BSA 2023:</label>
            <div class="marking-options">
              <button type="button" class="marking-btn relevant ${currentMark === 'relevant' ? 'selected' : ''}" data-mark="relevant">Relevant</button>
              <button type="button" class="marking-btn possibly ${currentMark === 'possibly_relevant' ? 'selected' : ''}" data-mark="possibly_relevant">Possibly Relevant</button>
              <button type="button" class="marking-btn irrelevant ${currentMark === 'irrelevant' ? 'selected' : ''}" data-mark="irrelevant">Irrelevant</button>
            </div>
          </div>
        </div>
      </div>
    `;

    modal.classList.add('show');
    if (window.GameAudio) window.GameAudio.playPaper();

    if (!userState.examinedEvIds.includes(ev.id)) {
      userState.examinedEvIds.push(ev.id);
    }

    const closeBtn = modal.querySelector('#btnCloseEvModal');
    if (closeBtn) closeBtn.addEventListener('click', () => modal.classList.remove('show'));
    modal.addEventListener('click', (e) => {
      if (e.target === modal) modal.classList.remove('show');
    });

    const markBtns = modal.querySelectorAll('.marking-btn');
    markBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const mark = btn.getAttribute('data-mark');
        userState.evidenceMarks[ev.id] = mark;
        markBtns.forEach(b => b.classList.remove('selected'));
        btn.classList.add('selected');
        if (window.GameAudio) window.GameAudio.playCardFlip();
        setTimeout(() => {
          modal.classList.remove('show');
          renderActiveStage();
        }, 300);
      });
    });
  }

  // -------------------------------------------------------------------------
  // STAGE 3: WITNESS INTERROGATION
  // -------------------------------------------------------------------------
  function renderStage3Witnesses(mountEl) {
    const witnesses = activeCaseData.witnesses || [];

    mountEl.innerHTML = `
      <div style="background:#fff;border:1px solid #cbd5e1;border-radius:12px;padding:18px 22px;margin-bottom:20px;box-shadow:0 3px 12px rgba(20,44,70,0.05)">
        <h3 style="font-family:Georgia,serif;font-size:18px;color:#142c46;margin:0 0 6px">Stage 3: Witness Examination & Interrogation</h3>
        <p style="font-size:13px;color:#64748b;margin:0">Cross-examine complainants, eyewitnesses, suspects, and technical experts to test credibility and uncover critical facts.</p>
      </div>

      <div style="display:flex;gap:10px;margin-bottom:18px;overflow-x:auto" id="witnessTabsArea">
        ${witnesses.map((w, idx) => `
          <button type="button" class="btn ${idx === 0 ? 'primary' : ''} witness-tab-btn" data-wit-idx="${idx}">
            👤 ${w.name} (${w.role})
          </button>
        `).join('')}
      </div>

      <div id="witnessSceneArea"></div>

      <div style="display:flex;justify-content:space-between;margin-top:22px">
        <button type="button" class="btn" id="btnBackStage2">← Back to Evidence</button>
        <button type="button" class="btn primary" id="btnGoStage4">Proceed to Evidence Board ➔</button>
      </div>
    `;

    const sceneArea = mountEl.querySelector('#witnessSceneArea');
    const tabBtns = mountEl.querySelectorAll('.witness-tab-btn');

    function loadWitness(idx) {
      tabBtns.forEach((b, i) => {
        if (i === idx) b.classList.add('primary');
        else b.classList.remove('primary');
      });

      const wit = witnesses[idx];
      if (!wit) return;

      if (window.DialogueEngine) {
        window.DialogueEngine.renderScene(sceneArea, {
          title: `Interrogation: ${wit.name} (${wit.role})`,
          characterId: 'rohan',
          speakerName: wit.name,
          initialText: `I am ${wit.name}, stated as ${wit.role}. I am ready to answer your inquiries.`,
          questions: wit.dialogue || [],
          onFactDiscovered: (fact) => {
            if (!userState.factsDiscovered.includes(fact)) {
              userState.factsDiscovered.push(fact);
            }
          }
        });
      }
    }

    tabBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const idx = parseInt(btn.getAttribute('data-wit-idx'), 10);
        loadWitness(idx);
      });
    });

    if (witnesses.length > 0) loadWitness(0);

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
  // STAGE 4: INTERACTIVE EVIDENCE BOARD
  // -------------------------------------------------------------------------
  function renderStage4Board(mountEl) {
    mountEl.innerHTML = `
      <div style="background:#fff;border:1px solid #cbd5e1;border-radius:12px;padding:18px 22px;margin-bottom:20px;box-shadow:0 3px 12px rgba(20,44,70,0.05)">
        <h3 style="font-family:Georgia,serif;font-size:18px;color:#142c46;margin:0 0 6px">Stage 4: Interactive Evidence Board</h3>
        <p style="font-size:13px;color:#64748b;margin:0">Map discovered clues and testimonies to their corresponding legal ingredients to build an airtight charge-sheet.</p>
      </div>

      <div id="corkboardMount"></div>

      <div style="display:flex;justify-content:space-between;margin-top:22px">
        <button type="button" class="btn" id="btnBackStage3">← Back to Witnesses</button>
        <button type="button" class="btn primary" id="btnGoStage5">Proceed to Legal Deduction ➔</button>
      </div>
    `;

    const corkboardMount = mountEl.querySelector('#corkboardMount');
    if (window.EvidenceBoard) {
      userState.boardInstance = new window.EvidenceBoard(corkboardMount, activeCaseData);
    }

    mountEl.querySelector('#btnBackStage3').addEventListener('click', () => {
      currentStageIndex = 2;
      renderActiveStage();
    });

    mountEl.querySelector('#btnGoStage5').addEventListener('click', () => {
      if (userState.boardInstance) {
        userState.boardEvaluation = userState.boardInstance.getEvaluation();
      }
      currentStageIndex = 4;
      renderActiveStage();
    });
  }

  // -------------------------------------------------------------------------
  // STAGE 5: LEGAL DEDUCTION
  // -------------------------------------------------------------------------
  function renderStage5Deduction(mountEl) {
    const deduction = activeCaseData.deduction || { question: 'Formulate charges:', options: [] };

    mountEl.innerHTML = `
      <div style="background:#fff;border:1px solid #cbd5e1;border-radius:12px;padding:20px 24px;margin-bottom:24px;box-shadow:0 4px 16px rgba(20,44,70,0.06)">
        <small class="eyebrow" style="color:#dfbf80">STAGE 5: FINAL LEGAL DEDUCTION & CHARGE-SHEET</small>
        <h3 style="font-family:Georgia,serif;font-size:20px;color:#142c46;margin:6px 0 10px">${deduction.question}</h3>
        <p style="font-size:14px;color:#64748b;margin:0">Carefully consider the statutory ingredients under the Bharatiya Nyaya Sanhita, 2023 and relevant landmark precedents.</p>
      </div>

      <div class="order-sections-list">
        <div class="order-block-card">
          <div class="order-block-options">
            ${deduction.options.map(opt => `
              <label class="order-choice-card ${userState.deductionChoiceId === opt.id ? 'selected' : ''}">
                <input type="radio" name="deductionOption" class="order-choice-radio" value="${opt.id}" ${userState.deductionChoiceId === opt.id ? 'checked' : ''}>
                <div style="flex:1">
                  <div style="font-weight:600;font-size:14px;color:#1e293b;line-height:1.45">${opt.text}</div>
                </div>
              </label>
            `).join('')}
          </div>
        </div>
      </div>

      <div style="display:flex;justify-content:space-between;margin-top:24px">
        <button type="button" class="btn" id="btnBackStage4">← Back to Evidence Board</button>
        <button type="button" class="btn primary" id="btnSubmitDeduction" ${!userState.deductionChoiceId ? 'disabled' : ''}>
          Submit Formal Investigation Report ➔
        </button>
      </div>
    `;

    const radioInputs = mountEl.querySelectorAll('input[name="deductionOption"]');
    const submitBtn = mountEl.querySelector('#btnSubmitDeduction');

    radioInputs.forEach(input => {
      input.addEventListener('change', () => {
        userState.deductionChoiceId = input.value;
        const cards = mountEl.querySelectorAll('.order-choice-card');
        cards.forEach(c => c.classList.remove('selected'));
        input.closest('.order-choice-card').classList.add('selected');
        if (submitBtn) submitBtn.disabled = false;
        if (window.GameAudio) window.GameAudio.playCardFlip();
      });
    });

    mountEl.querySelector('#btnBackStage4').addEventListener('click', () => {
      currentStageIndex = 3;
      renderActiveStage();
    });

    submitBtn.addEventListener('click', () => {
      currentStageIndex = 5;
      renderActiveStage();
    });
  }

  // -------------------------------------------------------------------------
  // STAGE 6: INVESTIGATION REPORT & DEBRIEF
  // -------------------------------------------------------------------------
  function renderStage6Report(mountEl) {
    let totalFactsCount = 0;
    (activeCaseData.witnesses || []).forEach(w => {
      totalFactsCount += (w.dialogue || []).length;
    });

    const scoreResult = window.CaseEngine ? window.CaseEngine.calculateDetectiveScore(activeCaseData, {
      evidenceMarks: userState.evidenceMarks,
      factsDiscoveredCount: userState.factsDiscovered.length,
      totalFactsPossible: totalFactsCount,
      boardEvaluation: userState.boardEvaluation,
      deductionChoiceId: userState.deductionChoiceId,
      hintsUsed: userState.hintsUsed
    }) : { score: 75, maxScore: 100, rubric: {} };

    // Record game result
    if (window.GameStorage) {
      window.GameStorage.recordGameResult({
        game: 'legal-detective',
        caseId: activeCaseData.id,
        title: activeCaseData.title,
        difficulty: activeCaseData.difficulty,
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
        activeCaseData,
        scoreResult,
        'legal-detective',
        () => {
          // Restart case
          startCase(currentCaseIndex);
        },
        () => {
          // Next case
          const cases = getCases();
          const nextIdx = (currentCaseIndex + 1) % cases.length;
          startCase(nextIdx);
        }
      );
    }
  }

  window.LegalDetectiveController = {
    init: init,
    startCase: startCase,
    renderCaseSelector: renderCaseSelector
  };

  document.addEventListener('DOMContentLoaded', init);
})();
