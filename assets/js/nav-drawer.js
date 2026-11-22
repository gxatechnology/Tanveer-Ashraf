/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Universal Right-Side Navigation Drawer & Header Controller
 * Accessible, Responsive, Multi-Tab (Website Menu, Chapters & Topics, Study Tools)
 */

(function (global) {
  'use strict';

  const DRAWER_ROUTES = [
    { id: 'home', label: 'Dashboard', icon: '⌂', href: 'index.html' },
    { id: 'academy', label: 'Subject Academy', icon: '🏛️', href: 'learning-academy.html' },
    { id: 'journey', label: 'Civil Suit Journey', icon: '⚖️', href: 'civil-suit-journey.html' },
    { id: 'comparison', label: 'Comparison Lab', icon: '⚖️', href: 'comparison-lab.html' },
    { id: 'arena', label: 'Brain Arena', icon: '⚡', href: 'brain-arena.html' },
    { id: 'notes', label: 'PYQ Library', icon: '▤', href: 'library.html' },
    { id: 'bns', label: 'BNS Bare Act', icon: '§', href: 'bns.html' },
    { id: 'search', label: 'Smart Search', icon: '⌕', href: 'search.html' },
    { id: 'practice', label: 'Test Centre', icon: '◎', href: 'tests.html' },
    { id: 'history', label: 'Results & Progress', icon: '▥', href: 'results.html' },
    { id: 'saved', label: 'Revision', icon: '☆', href: 'revision.html' },
    { id: 'syllabus', label: 'Syllabus & Notes', icon: '⚖', href: 'syllabus.html' },
    { id: 'about', label: 'About', icon: '◇', href: 'about.html' }
  ];

  const NavDrawer = {
    isOpen: false,
    lastFocusedElement: null,
    drawerEl: null,
    backdropEl: null,
    toggleBtnEl: null,

    init: function () {
      NavDrawer.ensureToggleButton();
      NavDrawer.ensureDrawerDOM();
      NavDrawer.bindEvents();
      NavDrawer.syncCurrentPage();
    },

    // 1. Ensure Top-Right Hamburger Toggle Button
    ensureToggleButton: function () {
      let btn = document.getElementById('menuToggleBtn');
      if (!btn) {
        // Look for target container in header
        const topHeader = document.querySelector('.top, .topbar, header');
        const topRight = document.querySelector('.top-right, .topbar-right');

        btn = document.createElement('button');
        btn.id = 'menuToggleBtn';
        btn.className = 'menu-toggle-btn';
        btn.setAttribute('aria-label', 'Open Navigation Menu');
        btn.setAttribute('aria-expanded', 'false');
        btn.setAttribute('aria-controls', 'globalNavDrawer');
        btn.innerHTML = `
          <span class="hamburger-box">
            <span class="hamburger-inner"></span>
          </span>
        `;

        if (topRight) {
          topRight.appendChild(btn);
        } else if (topHeader) {
          topHeader.appendChild(btn);
        } else {
          document.body.appendChild(btn);
        }
      }
      NavDrawer.toggleBtnEl = btn;
    },

    // 2. Ensure Drawer & Backdrop Markup Exist
    ensureDrawerDOM: function () {
      let backdrop = document.getElementById('drawerBackdrop');
      if (!backdrop) {
        backdrop = document.createElement('div');
        backdrop.id = 'drawerBackdrop';
        backdrop.className = 'drawer-backdrop';
        backdrop.setAttribute('aria-hidden', 'true');
        document.body.appendChild(backdrop);
      }
      NavDrawer.backdropEl = backdrop;

      let drawer = document.getElementById('globalNavDrawer');
      if (!drawer) {
        drawer = document.createElement('aside');
        drawer.id = 'globalNavDrawer';
        drawer.className = 'nav-drawer';
        drawer.setAttribute('role', 'dialog');
        drawer.setAttribute('aria-modal', 'true');
        drawer.setAttribute('aria-label', 'Navigation Menu');
        drawer.setAttribute('aria-hidden', 'true');

        const isStudyRoom = window.location.pathname.includes('subject-study.html') || document.getElementById('topics-nav-tree') !== null;

        drawer.innerHTML = `
          <div class="drawer-header">
            <a class="drawer-brand" href="index.html">
              <img src="assets/images/emblem.svg" alt="Judicial Prep emblem" class="drawer-emblem">
              <div class="drawer-brand-text">
                <b>Judicial Prep</b>
                <small>UP PCS-J · 2026–27</small>
              </div>
            </a>
            <button class="drawer-close-btn" id="drawerCloseBtn" aria-label="Close Navigation Menu">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>

          <div class="drawer-tabs" role="tablist">
            <button class="drawer-tab-btn is-active" id="drawerTabBtnMenu" role="tab" aria-selected="true" aria-controls="drawerPanelMenu">
              <span>☰</span> Menu
            </button>
            ${isStudyRoom ? `
              <button class="drawer-tab-btn" id="drawerTabBtnChapters" role="tab" aria-selected="false" aria-controls="drawerPanelChapters">
                <span>📚</span> Chapters
              </button>
              <button class="drawer-tab-btn" id="drawerTabBtnTools" role="tab" aria-selected="false" aria-controls="drawerPanelTools">
                <span>⚡</span> Tools
              </button>
            ` : ''}
          </div>

          <!-- TAB A: Website Menu -->
          <div class="drawer-panel is-active" id="drawerPanelMenu" role="tabpanel" aria-labelledby="drawerTabBtnMenu">
            <div class="drawer-nav-group-label">Primary Navigation</div>
            <nav class="drawer-nav" aria-label="Mobile Navigation">
              ${DRAWER_ROUTES.map(r => `
                <a href="${r.href}" class="drawer-nav-link" data-view="${r.id}">
                  <span class="nav-icon" aria-hidden="true">${r.icon}</span>
                  <span>${r.label}</span>
                </a>
              `).join('')}
            </nav>
          </div>

          ${isStudyRoom ? `
            <!-- TAB B: Chapters & Topics -->
            <div class="drawer-panel" id="drawerPanelChapters" role="tabpanel" aria-labelledby="drawerTabBtnChapters">
              <div id="drawerChaptersMount">
                <p style="padding: 20px; text-align: center; color: #a5b9ca; font-size: 13px;">Loading curriculum...</p>
              </div>
            </div>

            <!-- TAB C: Study Tools -->
            <div class="drawer-panel" id="drawerPanelTools" role="tabpanel" aria-labelledby="drawerTabBtnTools">
              <div class="drawer-tools-card">
                <h4>Study Reading Mode</h4>
                <div class="drawer-tool-row">
                  <button class="drawer-tool-btn is-active" id="drawerModeDetailed">📚 Detailed</button>
                  <button class="drawer-tool-btn" id="drawerModeQuick">⚡ Quick Revision</button>
                </div>
              </div>

              <div class="drawer-tools-card">
                <h4>Font Size Scaling</h4>
                <div class="drawer-tool-row">
                  <button class="drawer-tool-btn" id="drawerFontDec">A- Smaller</button>
                  <button class="drawer-tool-btn" id="drawerFontReset">A Reset</button>
                  <button class="drawer-tool-btn" id="drawerFontInc">A+ Larger</button>
                </div>
              </div>

              <div class="drawer-tools-card">
                <h4>Topic Actions</h4>
                <div class="drawer-tool-row" style="flex-direction: column;">
                  <button class="drawer-tool-btn" id="drawerBtnToggleRead" style="justify-content: flex-start;">
                    <span>✓</span> <span id="drawerToggleReadLabel">Mark as Read</span>
                  </button>
                  <a href="#" class="drawer-tool-btn" id="drawerLinkPractice" style="justify-content: flex-start;">
                    <span>⚡</span> <span>Practise This Topic</span>
                  </a>
                  <a href="#" class="drawer-tool-btn" id="drawerLinkPYQ" style="justify-content: flex-start;">
                    <span>📜</span> <span>Related PYQs</span>
                  </a>
                  <button class="drawer-tool-btn" id="drawerBtnPrint" style="justify-content: flex-start;">
                    <span>🖨️</span> <span>Print Note</span>
                  </button>
                </div>
              </div>
            </div>
          ` : ''}

          <div class="drawer-footer">
            <div class="drawer-profile">
              <img src="assets/images/tauqeer-original.webp" alt="Tauqeer Ashraf portrait">
              <div><small>Designed &amp; developed by</small><b>Tauqeer Ashraf</b></div>
            </div>
          </div>
        `;
        document.body.appendChild(drawer);
      }
      NavDrawer.drawerEl = drawer;

      if (window.location.pathname.includes('subject-study.html') || document.getElementById('topics-nav-tree')) {
        NavDrawer.populateChaptersTab();
        NavDrawer.bindToolsTab();
      }
    },

    // 3. Populate Contextual Chapters Tab
    populateChaptersTab: function () {
      const mount = document.getElementById('drawerChaptersMount');
      if (!mount || !global.LearningEngine) return;

      const urlParams = new URLSearchParams(window.location.search);
      const subjectId = urlParams.get('subject') || 'law-constitution';
      const activeChapterId = urlParams.get('chapter');
      const activeTopicId = urlParams.get('topic');

      const subject = global.LearningEngine.getSubjectById(subjectId) || {
        name: 'Constitution of India',
        icon: '🏛️',
        chaptersCount: 15,
        topicsCount: 45
      };

      const chapters = global.LearningEngine.getChaptersBySubject(subjectId) || [];
      const store = (global.LearningStorage && typeof global.LearningStorage.exportData === 'function')
        ? global.LearningStorage.exportData()
        : {};
      const completedTopics = store.completedTopics || {};

      let totalCompleted = 0;
      let totalTopics = 0;

      chapters.forEach(ch => {
        const topics = global.LearningEngine.getTopicsByChapter(ch.id, subjectId) || [];
        totalTopics += topics.length;
        topics.forEach(t => {
          if (completedTopics[t.id]) totalCompleted++;
        });
      });

      const pct = totalTopics > 0 ? Math.round((totalCompleted / totalTopics) * 100) : 0;

      let html = `
        <div class="drawer-subject-summary">
          <div class="drawer-subject-title">${subject.icon || '📚'} ${subject.name}</div>
          <div class="drawer-subject-meta">${chapters.length} Chapters · ${totalCompleted}/${totalTopics} Topics Completed (${pct}%)</div>
          <div class="drawer-progress-track">
            <div class="drawer-progress-fill" style="width: ${pct}%;"></div>
          </div>
        </div>

        <div class="drawer-chapter-list">
      `;

      chapters.forEach((ch, idx) => {
        const chTopics = global.LearningEngine.getTopicsByChapter(ch.id, subjectId) || [];
        const isActiveCh = ch.id === activeChapterId || (!activeChapterId && idx === 0);
        const chCompleted = chTopics.filter(t => completedTopics[t.id]).length;

        html += `
          <div class="drawer-chapter-item">
            <div class="drawer-chapter-head ${isActiveCh ? 'is-active-chapter' : ''}" data-ch-id="${ch.id}">
              <span>${ch.number || idx + 1}. ${ch.title}</span>
              <span class="drawer-chapter-badge">${chCompleted}/${chTopics.length}</span>
            </div>
            <ul class="drawer-topic-list" style="${isActiveCh ? 'display: flex;' : 'display: none;'}">
              ${chTopics.map(t => {
                const isActiveTop = t.id === activeTopicId || (!activeTopicId && isActiveCh && t === chTopics[0]);
                const isRead = !!completedTopics[t.id];
                return `
                  <li>
                    <a href="subject-study.html?subject=${subjectId}&chapter=${ch.id}&topic=${t.id}"
                       class="drawer-topic-link ${isActiveTop ? 'is-active-topic' : ''} ${isRead ? 'is-read-topic' : ''}">
                      <span class="topic-title">${t.title}</span>
                    </a>
                  </li>
                `;
              }).join('')}
            </ul>
          </div>
        `;
      });

      html += `</div>`;
      mount.innerHTML = html;

      // Bind Chapter Accordion
      mount.querySelectorAll('.drawer-chapter-head').forEach(head => {
        head.addEventListener('click', function () {
          const list = this.nextElementSibling;
          if (!list) return;
          const isShown = list.style.display === 'flex';
          list.style.display = isShown ? 'none' : 'flex';
        });
      });

      // Bind Topic Link click to close drawer
      mount.querySelectorAll('.drawer-topic-link').forEach(link => {
        link.addEventListener('click', () => {
          NavDrawer.close();
        });
      });
    },

    // 4. Bind Tools Tab Actions
    bindToolsTab: function () {
      const btnModeDet = document.getElementById('drawerModeDetailed');
      const btnModeQck = document.getElementById('drawerModeQuick');
      const btnFontDec = document.getElementById('drawerFontDec');
      const btnFontRst = document.getElementById('drawerFontReset');
      const btnFontInc = document.getElementById('drawerFontInc');
      const btnToggleRead = document.getElementById('drawerBtnToggleRead');
      const btnPrint = document.getElementById('drawerBtnPrint');
      const linkPractice = document.getElementById('drawerLinkPractice');
      const linkPYQ = document.getElementById('drawerLinkPYQ');

      const urlParams = new URLSearchParams(window.location.search);
      const subjectId = urlParams.get('subject') || 'law-constitution';
      const topicId = urlParams.get('topic');

      if (linkPractice && topicId) {
        linkPractice.href = `topic-practice.html?subject=${subjectId}&topic=${topicId}&mode=learn`;
      }
      if (linkPYQ && topicId) {
        linkPYQ.href = `topic-practice.html?subject=${subjectId}&topic=${topicId}&mode=pyq`;
      }

      if (btnModeDet) {
        btnModeDet.addEventListener('click', () => {
          btnModeDet.classList.add('is-active');
          if (btnModeQck) btnModeQck.classList.remove('is-active');
          const pageDet = document.querySelector('.mode-btn[data-mode="detailed"]');
          if (pageDet) pageDet.click();
        });
      }

      if (btnModeQck) {
        btnModeQck.addEventListener('click', () => {
          btnModeQck.classList.add('is-active');
          if (btnModeDet) btnModeDet.classList.remove('is-active');
          const pageQck = document.querySelector('.mode-btn[data-mode="quick"]');
          if (pageQck) pageQck.click();
        });
      }

      if (btnFontDec) {
        btnFontDec.addEventListener('click', () => {
          const pageDec = document.getElementById('btn-font-dec');
          if (pageDec) pageDec.click();
        });
      }
      if (btnFontRst) {
        btnFontRst.addEventListener('click', () => {
          const pageRst = document.getElementById('btn-font-reset');
          if (pageRst) pageRst.click();
        });
      }
      if (btnFontInc) {
        btnFontInc.addEventListener('click', () => {
          const pageInc = document.getElementById('btn-font-inc');
          if (pageInc) pageInc.click();
        });
      }

      if (btnToggleRead) {
        btnToggleRead.addEventListener('click', () => {
          const pageToggle = document.getElementById('btn-toggle-read');
          if (pageToggle) {
            pageToggle.click();
            NavDrawer.syncReadStatus();
          }
        });
      }

      if (btnPrint) {
        btnPrint.addEventListener('click', () => {
          NavDrawer.close();
          window.print();
        });
      }
    },

    syncReadStatus: function () {
      const urlParams = new URLSearchParams(window.location.search);
      const topicId = urlParams.get('topic');
      const label = document.getElementById('drawerToggleReadLabel');
      if (label && topicId && global.LearningStorage) {
        const isRead = global.LearningStorage.isTopicRead(topicId);
        label.textContent = isRead ? 'Mark as Unread' : 'Mark as Read';
      }
    },

    // 5. Bind Drawer Open/Close & Keyboard Events
    bindEvents: function () {
      if (NavDrawer.toggleBtnEl) {
        NavDrawer.toggleBtnEl.addEventListener('click', () => {
          NavDrawer.toggle();
        });
      }

      const closeBtn = document.getElementById('drawerCloseBtn');
      if (closeBtn) {
        closeBtn.addEventListener('click', () => {
          NavDrawer.close();
        });
      }

      if (NavDrawer.backdropEl) {
        NavDrawer.backdropEl.addEventListener('click', () => {
          NavDrawer.close();
        });
      }

      // Drawer Tabs Switcher
      const tabMenu = document.getElementById('drawerTabBtnMenu');
      const tabChapters = document.getElementById('drawerTabBtnChapters');
      const tabTools = document.getElementById('drawerTabBtnTools');
      const panelMenu = document.getElementById('drawerPanelMenu');
      const panelChapters = document.getElementById('drawerPanelChapters');
      const panelTools = document.getElementById('drawerPanelTools');

      function switchTab(btn, panel) {
        [tabMenu, tabChapters, tabTools].forEach(b => {
          if (b) {
            b.classList.remove('is-active');
            b.setAttribute('aria-selected', 'false');
          }
        });
        [panelMenu, panelChapters, panelTools].forEach(p => {
          if (p) p.classList.remove('is-active');
        });

        if (btn) {
          btn.classList.add('is-active');
          btn.setAttribute('aria-selected', 'true');
        }
        if (panel) {
          panel.classList.add('is-active');
        }
      }

      if (tabMenu && panelMenu) {
        tabMenu.addEventListener('click', () => switchTab(tabMenu, panelMenu));
      }
      if (tabChapters && panelChapters) {
        tabChapters.addEventListener('click', () => {
          switchTab(tabChapters, panelChapters);
          NavDrawer.populateChaptersTab();
        });
      }
      if (tabTools && panelTools) {
        tabTools.addEventListener('click', () => {
          switchTab(tabTools, panelTools);
          NavDrawer.syncReadStatus();
        });
      }

      // Keyboard Trap & Escape Listener
      document.addEventListener('keydown', function (e) {
        if (!NavDrawer.isOpen) return;

        if (e.key === 'Escape') {
          e.preventDefault();
          NavDrawer.close();
          return;
        }

        if (e.key === 'Tab') {
          const focusable = NavDrawer.drawerEl.querySelectorAll(
            'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
          );
          if (!focusable.length) return;
          const first = focusable[0];
          const last = focusable[focusable.length - 1];

          if (e.shiftKey && document.activeElement === first) {
            e.preventDefault();
            last.focus();
          } else if (!e.shiftKey && document.activeElement === last) {
            e.preventDefault();
            first.focus();
          }
        }
      });

      // Close on Link Click inside drawer
      if (NavDrawer.drawerEl) {
        NavDrawer.drawerEl.querySelectorAll('.drawer-nav-link').forEach(link => {
          link.addEventListener('click', () => {
            NavDrawer.close();
          });
        });
      }

      // Viewport resize safeguard
      window.addEventListener('resize', () => {
        if (window.innerWidth > 1024 && NavDrawer.isOpen && !document.querySelector('.study-layout')) {
          // On non-study wide desktop, close drawer if left sidebar is visible
          NavDrawer.close();
        }
      });
    },

    // 6. Highlight Active Page Link in Drawer Nav
    syncCurrentPage: function () {
      if (!NavDrawer.drawerEl) return;
      const currentPath = window.location.pathname.split('/').pop() || 'index.html';
      NavDrawer.drawerEl.querySelectorAll('.drawer-nav-link').forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath || (currentPath === '' && href === 'index.html')) {
          link.classList.add('is-active');
          link.setAttribute('aria-current', 'page');
        } else {
          link.classList.remove('is-active');
          link.removeAttribute('aria-current');
        }
      });
    },

    toggle: function () {
      if (NavDrawer.isOpen) {
        NavDrawer.close();
      } else {
        NavDrawer.open();
      }
    },

    open: function () {
      if (NavDrawer.isOpen) return;
      NavDrawer.isOpen = true;
      NavDrawer.lastFocusedElement = document.activeElement;

      if (NavDrawer.drawerEl) {
        NavDrawer.drawerEl.classList.add('is-open');
        NavDrawer.drawerEl.setAttribute('aria-hidden', 'false');
      }
      if (NavDrawer.backdropEl) {
        NavDrawer.backdropEl.classList.add('is-open');
        NavDrawer.backdropEl.setAttribute('aria-hidden', 'false');
      }
      if (NavDrawer.toggleBtnEl) {
        NavDrawer.toggleBtnEl.classList.add('is-active');
        NavDrawer.toggleBtnEl.setAttribute('aria-expanded', 'true');
        NavDrawer.toggleBtnEl.setAttribute('aria-label', 'Close Navigation Menu');
      }

      document.body.classList.add('drawer-open');

      // Focus close button or first focusable element
      const closeBtn = document.getElementById('drawerCloseBtn');
      if (closeBtn) {
        setTimeout(() => closeBtn.focus(), 50);
      }
    },

    close: function () {
      if (!NavDrawer.isOpen) return;
      NavDrawer.isOpen = false;

      if (NavDrawer.drawerEl) {
        NavDrawer.drawerEl.classList.remove('is-open');
        NavDrawer.drawerEl.setAttribute('aria-hidden', 'true');
      }
      if (NavDrawer.backdropEl) {
        NavDrawer.backdropEl.classList.remove('is-open');
        NavDrawer.backdropEl.setAttribute('aria-hidden', 'true');
      }
      if (NavDrawer.toggleBtnEl) {
        NavDrawer.toggleBtnEl.classList.remove('is-active');
        NavDrawer.toggleBtnEl.setAttribute('aria-expanded', 'false');
        NavDrawer.toggleBtnEl.setAttribute('aria-label', 'Open Navigation Menu');
      }

      document.body.classList.remove('drawer-open');

      if (NavDrawer.lastFocusedElement && typeof NavDrawer.lastFocusedElement.focus === 'function') {
        NavDrawer.lastFocusedElement.focus();
      } else if (NavDrawer.toggleBtnEl) {
        NavDrawer.toggleBtnEl.focus();
      }
    }
  };

  // Auto-initialize on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', NavDrawer.init);
  } else {
    NavDrawer.init();
  }

  global.NavDrawer = NavDrawer;
})(window);
