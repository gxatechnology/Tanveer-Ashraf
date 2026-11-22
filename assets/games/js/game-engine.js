/**
 * LEGAL BRAIN ARENA — SHARED GAMING UTILITIES & MODAL ENGINE
 */
(function() {
  'use strict';

  function escapeHTML(str) {
    return String(str ?? '').replace(/[&<>"']/g, c => ({
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&#39;'
    }[c]));
  }

  function formatTime(seconds) {
    const s = Math.max(0, Math.floor(seconds));
    const m = Math.floor(s / 60);
    const rem = s % 60;
    return `${m}:${rem < 10 ? '0' : ''}${rem}`;
  }

  function shuffle(array) {
    const a = [...array];
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  const GameEngine = {
    esc: escapeHTML,
    formatTime: formatTime,
    shuffle: shuffle,

    isReducedMotion: function() {
      try {
        const state = window.GameStorage ? window.GameStorage.getArenaState() : null;
        if (state && state.settings && state.settings.reducedMotion) return true;
        return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      } catch (e) {
        return false;
      }
    },

    // Show floating educational toast when legal card is matched
    showMatchExplanation: function(item, onReviewBNS) {
      const existing = document.getElementById('matchExplanationToast');
      if (existing) existing.remove();

      const toast = document.createElement('div');
      toast.id = 'matchExplanationToast';
      toast.className = 'match-toast';
      toast.setAttribute('role', 'status');
      toast.setAttribute('aria-live', 'polite');

      let actionBtn = '';
      if (item.bnsSection) {
        actionBtn = `<a class="btn mini gold" href="bns.html?q=${encodeURIComponent(item.bnsSection)}" target="_blank" rel="noopener">Explore § ${item.bnsSection} in BNS ↗</a>`;
      }

      toast.innerHTML = `
        <div class="match-toast-header">
          <span class="tag" style="background:#edf7f4;color:#137d72;border-color:#7cbca6">Legal Pair Matched!</span>
          <button type="button" class="match-toast-close" aria-label="Close" onclick="this.closest('.match-toast').remove()">✕</button>
        </div>
        <div class="match-toast-title"><strong>${escapeHTML(item.prompt)}</strong> — ${escapeHTML(item.answer)}</div>
        ${item.explanation ? `<div class="match-toast-desc">${escapeHTML(item.explanation)}</div>` : ''}
        ${actionBtn ? `<div style="margin-top:8px">${actionBtn}</div>` : ''}
      `;

      document.body.appendChild(toast);
      setTimeout(() => toast.classList.add('show'), 40);

      // Auto-dismiss after 6.5s
      setTimeout(() => {
        if (toast.parentNode) {
          toast.classList.remove('show');
          setTimeout(() => toast.remove(), 300);
        }
      }, 6500);
    },

    // Modal dialogue generator
    showModal: function(options) {
      // options: { title, subtitle, contentHTML, buttons: [{ text, class, onClick }] }
      const existing = document.getElementById('arenaModal');
      if (existing) existing.remove();

      const overlay = document.createElement('div');
      overlay.id = 'arenaModal';
      overlay.className = 'arena-modal-overlay';
      overlay.setAttribute('role', 'dialog');
      overlay.setAttribute('aria-modal', 'true');

      let buttonsHTML = '';
      if (options.buttons) {
        buttonsHTML = options.buttons.map((b, idx) => `
          <button type="button" class="btn ${b.class || 'primary'}" data-btn-idx="${idx}">
            ${escapeHTML(b.text)}
          </button>
        `).join('');
      }

      overlay.innerHTML = `
        <div class="arena-modal-card">
          <div class="arena-modal-header">
            ${options.subtitle ? `<div class="eyebrow" style="color:#dfbf80">${escapeHTML(options.subtitle)}</div>` : ''}
            <h2>${escapeHTML(options.title || 'Legal Brain Arena')}</h2>
          </div>
          <div class="arena-modal-body">
            ${options.contentHTML || ''}
          </div>
          <div class="arena-modal-actions">
            ${buttonsHTML}
          </div>
        </div>
      `;

      document.body.appendChild(overlay);
      setTimeout(() => overlay.classList.add('open'), 20);

      overlay.querySelectorAll('[data-btn-idx]').forEach(btnEl => {
        const idx = parseInt(btnEl.dataset.btnIdx, 10);
        btnEl.onclick = () => {
          if (options.buttons[idx] && options.buttons[idx].onClick) {
            options.buttons[idx].onClick();
          }
          overlay.classList.remove('open');
          setTimeout(() => overlay.remove(), 250);
        };
      });

      return {
        close: function() {
          overlay.classList.remove('open');
          setTimeout(() => overlay.remove(), 250);
        }
      };
    }
  };

  window.GameEngine = GameEngine;
})();
