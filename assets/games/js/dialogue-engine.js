/**
 * LEGAL BRAIN ARENA — INTERACTIVE DIALOGUE ENGINE (V3.0 Phase 2)
 * Branching dialogue trees, question interrogation, fact extraction, and transcript logs.
 * Author: Tauqeer Ashraf
 */
(function() {
  'use strict';

  let dialogueHistory = [];

  const DialogueEngine = {
    clearHistory: function() {
      dialogueHistory = [];
    },

    getHistory: function() {
      return dialogueHistory;
    },

    logEntry: function(characterId, text, customName = null) {
      const char = window.CharacterEngine ? window.CharacterEngine.getCharacter(characterId) : null;
      const speakerName = customName || (char ? char.name : 'Unknown Speaker');
      const speakerRole = char ? char.role : '';
      dialogueHistory.push({
        characterId,
        speakerName,
        speakerRole,
        text,
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' })
      });
    },

    renderScene: function(containerEl, options) {
      // options: {
      //   title: 'Stage 1: Briefing',
      //   characterId: 'arjun',
      //   speakerName: optional override,
      //   initialText: '...',
      //   questions: [{ question, answer, discoversFact }],
      //   onFactDiscovered: function(factText),
      //   onComplete: function()
      // }
      if (!containerEl) return;

      const char = window.CharacterEngine ? window.CharacterEngine.getCharacter(options.characterId) : null;
      const charName = options.speakerName || (char ? char.name : 'Speaker');

      this.logEntry(options.characterId, options.initialText, charName);

      containerEl.innerHTML = `
        <div class="dialogue-viewport">
          <div class="dialogue-header">
            <div class="dialogue-header-title">
              <span>🎙</span>
              <span>${options.title || 'Interactive Dialogue'}</span>
            </div>
            <div class="dialogue-controls">
              <button type="button" class="dialogue-btn-sm" id="btnSkipTypewrite" title="Skip typing animation">⚡ Skip</button>
              <button type="button" class="dialogue-btn-sm" id="btnViewTranscript" title="View complete dialogue history">📜 Transcript (${dialogueHistory.length})</button>
            </div>
          </div>
          <div class="dialogue-scene">
            ${window.CharacterEngine ? window.CharacterEngine.renderAvatar(options.characterId) : ''}
            <div class="dialogue-speech-wrap">
              <div class="dialogue-speech-bubble" id="dialogueBubbleArea">
                <div id="dialogueTypewriteTarget"></div>
              </div>
            </div>
          </div>
          ${options.questions && options.questions.length > 0 ? `
            <div class="dialogue-options-wrap">
              <div class="dialogue-options-label">Select Inquiry / Cross-Examination Question:</div>
              <div class="dialogue-options-list" id="dialogueQuestionsList">
                ${options.questions.map((q, idx) => `
                  <button type="button" class="dialogue-option-btn" data-q-idx="${idx}">
                    <span><strong>Q${idx + 1}:</strong> ${q.question}</span>
                    <span style="font-size:12px;color:#137d72">Ask ↗</span>
                  </button>
                `).join('')}
              </div>
            </div>
          ` : ''}
        </div>
      `;

      const typewriteTarget = containerEl.querySelector('#dialogueTypewriteTarget');
      const bubbleArea = containerEl.querySelector('#dialogueBubbleArea');
      const skipBtn = containerEl.querySelector('#btnSkipTypewrite');
      const transcriptBtn = containerEl.querySelector('#btnViewTranscript');

      // Click on bubble or skip button finishes typing instantly
      const doSkip = () => {
        if (window.CharacterEngine) window.CharacterEngine.skipTypewrite();
      };
      if (skipBtn) skipBtn.addEventListener('click', doSkip);
      if (bubbleArea) bubbleArea.addEventListener('click', doSkip);

      // Transcript viewer modal
      if (transcriptBtn) {
        transcriptBtn.addEventListener('click', () => {
          this.showTranscriptModal();
        });
      }

      // Start initial typewriter
      if (window.CharacterEngine) {
        window.CharacterEngine.typewrite(typewriteTarget, options.initialText, () => {
          if (typeof options.onComplete === 'function') options.onComplete();
        });
        window.CharacterEngine.speak(options.characterId, options.initialText);
      } else {
        typewriteTarget.textContent = options.initialText;
      }

      // Handle interactive questions
      if (options.questions && options.questions.length > 0) {
        const qButtons = containerEl.querySelectorAll('.dialogue-option-btn');
        qButtons.forEach(btn => {
          btn.addEventListener('click', () => {
            const idx = parseInt(btn.getAttribute('data-q-idx'), 10);
            const qData = options.questions[idx];
            if (!qData) return;

            btn.classList.add('asked');
            if (window.GameAudio) window.GameAudio.playPaper();

            // Log user question and character answer
            this.logEntry('user', qData.question, 'You (Investigator / Judge)');
            this.logEntry(options.characterId, qData.answer, charName);

            if (transcriptBtn) {
              transcriptBtn.textContent = `📜 Transcript (${dialogueHistory.length})`;
            }

            // Speak and typewrite answer
            if (window.CharacterEngine) {
              window.CharacterEngine.typewrite(typewriteTarget, qData.answer);
              window.CharacterEngine.speak(options.characterId, qData.answer);
            } else {
              typewriteTarget.textContent = qData.answer;
            }

            // Fact discovery callback
            if (qData.discoversFact && typeof options.onFactDiscovered === 'function') {
              options.onFactDiscovered(qData.discoversFact);
            }
          });
        });
      }
    },

    showTranscriptModal: function() {
      let modal = document.getElementById('dialogueTranscriptModal');
      if (!modal) {
        modal = document.createElement('div');
        modal.id = 'dialogueTranscriptModal';
        modal.className = 'dialogue-log-modal';
        document.body.appendChild(modal);
      }

      modal.innerHTML = `
        <div class="dialogue-log-window">
          <div class="dialogue-header">
            <div class="dialogue-header-title">
              <span>📜</span>
              <span>Official Examination Transcript</span>
            </div>
            <button type="button" class="dialogue-btn-sm" id="btnCloseTranscript">✕ Close</button>
          </div>
          <div class="dialogue-log-content">
            ${dialogueHistory.length === 0 ? '<p style="color:#64748b">No statements recorded yet.</p>' : ''}
            ${dialogueHistory.map(entry => `
              <div class="log-entry">
                <div class="log-speaker">
                  <span>${entry.speakerName}</span>
                  ${entry.speakerRole ? `<span style="font-weight:400;color:#64748b;font-size:11px">(${entry.speakerRole})</span>` : ''}
                  <span style="float:right;font-size:10px;color:#94a3b8;font-weight:400">${entry.time}</span>
                </div>
                <div class="log-text">${entry.text}</div>
              </div>
            `).join('')}
          </div>
        </div>
      `;

      modal.classList.add('show');
      const closeBtn = modal.querySelector('#btnCloseTranscript');
      if (closeBtn) {
        closeBtn.addEventListener('click', () => {
          modal.classList.remove('show');
        });
      }
      modal.addEventListener('click', (e) => {
        if (e.target === modal) modal.classList.remove('show');
      });
    }
  };

  window.DialogueEngine = DialogueEngine;
})();
