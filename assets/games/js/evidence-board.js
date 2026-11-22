/**
 * LEGAL BRAIN ARENA — INTERACTIVE EVIDENCE BOARD (V3.0 Phase 2)
 * Corkboard clue connection, statutory element mapping, and deduction evaluation.
 * Author: Tauqeer Ashraf
 */
(function() {
  'use strict';

  function EvidenceBoard(containerEl, caseData) {
    this.container = containerEl;
    this.caseData = caseData;
    this.selectedNodeId = null;
    this.connections = []; // Array of { clueId, issueId, clueName, issueLabel }

    this.init();
  }

  EvidenceBoard.prototype.init = function() {
    this.render();
  };

  EvidenceBoard.prototype.render = function() {
    if (!this.container || !this.caseData) return;

    const boardData = this.caseData.evidenceBoard || { legalIssues: [], targetConnections: [] };
    const evidenceList = this.caseData.evidence || [];
    const witnessList = this.caseData.witnesses || [];

    // Combine evidence items and witnesses as possible clue nodes
    const allClues = [];
    evidenceList.forEach(ev => {
      allClues.push({
        id: ev.id,
        name: ev.name,
        type: ev.type,
        snippet: ev.summary
      });
    });
    witnessList.forEach(wit => {
      allClues.push({
        id: wit.id,
        name: `Testimony: ${wit.name}`,
        type: 'testimony',
        snippet: wit.role ? `${wit.role} statement and cross-examination` : 'Witness statement'
      });
    });

    this.container.innerHTML = `
      <div class="corkboard-wrap">
        <div class="corkboard-instructions">
          📌 <strong>Investigation Instructions:</strong> Click a clue from the left investigation files, then click a corresponding statutory ingredient on the right to pin the connection.
        </div>
        <div class="corkboard-grid">
          <!-- Left Column: Discovered Clues & Exhibits -->
          <div class="corkboard-column" id="corkboardCluesCol">
            <div class="corkboard-col-title">
              <span>📋 Discovered Exhibits & Facts</span>
              <small style="color:#dfbf80">${allClues.length} Items</small>
            </div>
            ${allClues.map(clue => {
              const isConnected = this.connections.some(c => c.clueId === clue.id);
              const isSelected = this.selectedNodeId === clue.id;
              return `
                <div class="cork-node ${isSelected ? 'selected' : ''} ${isConnected ? 'connected' : ''}" data-clue-id="${clue.id}">
                  <div class="cork-node-header">
                    <span>${clue.type.toUpperCase()}</span>
                    <span>${isConnected ? '✓ Linked' : 'Unlinked'}</span>
                  </div>
                  <div class="cork-node-title">${clue.name}</div>
                  <div class="cork-node-snippet">${clue.snippet}</div>
                </div>
              `;
            }).join('')}
          </div>

          <!-- Right Column: Statutory Issues & Legal Ingredients -->
          <div class="corkboard-column" id="corkboardIssuesCol">
            <div class="corkboard-col-title">
              <span>⚖ Statutory Elements / Legal Issues</span>
              <small style="color:#dfbf80">${boardData.legalIssues.length} Elements</small>
            </div>
            ${boardData.legalIssues.map(issue => {
              const linksForThisIssue = this.connections.filter(c => c.issueId === issue.id);
              return `
                <div class="cork-target ${linksForThisIssue.length > 0 ? 'linked' : ''}" data-issue-id="${issue.id}">
                  <div class="cork-target-title">${issue.label}</div>
                  <div class="cork-target-desc">Click here to attach selected clue node</div>
                  <div class="linked-pills">
                    ${linksForThisIssue.map(link => `
                      <span class="linked-pill">
                        <span>📌 ${link.clueName}</span>
                        <span class="linked-pill-remove" data-remove-clue="${link.clueId}" data-remove-issue="${issue.id}" title="Remove link">✕</span>
                      </span>
                    `).join('')}
                  </div>
                </div>
              `;
            }).join('')}
          </div>
        </div>
      </div>
    `;

    this.attachEvents(allClues, boardData.legalIssues);
  };

  EvidenceBoard.prototype.attachEvents = function(allClues, legalIssues) {
    // Select clue
    const clueNodes = this.container.querySelectorAll('.cork-node');
    clueNodes.forEach(node => {
      node.addEventListener('click', (e) => {
        const clueId = node.getAttribute('data-clue-id');
        if (this.selectedNodeId === clueId) {
          this.selectedNodeId = null;
        } else {
          this.selectedNodeId = clueId;
          if (window.GameAudio) window.GameAudio.playCardFlip();
        }
        this.render();
      });
    });

    // Link clue to issue
    const targetNodes = this.container.querySelectorAll('.cork-target');
    targetNodes.forEach(target => {
      target.addEventListener('click', (e) => {
        // If clicking remove button, ignore
        if (e.target.classList.contains('linked-pill-remove')) return;

        if (!this.selectedNodeId) return;

        const issueId = target.getAttribute('data-issue-id');
        const clue = allClues.find(c => c.id === this.selectedNodeId);
        const issue = legalIssues.find(i => i.id === issueId);

        if (clue && issue) {
          // Check if link already exists
          const exists = this.connections.some(c => c.clueId === clue.id && c.issueId === issue.id);
          if (!exists) {
            this.connections.push({
              clueId: clue.id,
              issueId: issue.id,
              clueName: clue.name,
              issueLabel: issue.label
            });
            if (window.GameAudio) window.GameAudio.playClue();
          }
          this.selectedNodeId = null;
          this.render();
        }
      });
    });

    // Remove link
    const removeBtns = this.container.querySelectorAll('.linked-pill-remove');
    removeBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const clueId = btn.getAttribute('data-remove-clue');
        const issueId = btn.getAttribute('data-remove-issue');
        this.connections = this.connections.filter(c => !(c.clueId === clueId && c.issueId === issueId));
        this.render();
      });
    });
  };

  EvidenceBoard.prototype.getEvaluation = function() {
    const boardData = this.caseData.evidenceBoard || { targetConnections: [] };
    const targets = boardData.targetConnections || [];

    let correctCount = 0;
    let falseCount = 0;

    this.connections.forEach(userConn => {
      const match = targets.some(t => t.from === userConn.clueId && t.to === userConn.issueId);
      if (match) {
        correctCount++;
      } else {
        falseCount++;
      }
    });

    const totalPossible = Math.max(1, targets.length);
    const rawScore = (correctCount / totalPossible) * 20 - (falseCount * 2);
    const score = Math.max(0, Math.min(20, Math.round(rawScore)));

    return {
      score: score,
      maxScore: 20,
      correctCount: correctCount,
      targetCount: targets.length,
      falseCount: falseCount,
      connectionsCount: this.connections.length
    };
  };

  window.EvidenceBoard = EvidenceBoard;
})();
