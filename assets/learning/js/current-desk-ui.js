/**
 * CURRENT AFFAIRS DESK UI COMPONENT (V3.1.9)
 * Renders an interactive Date-Wise Current Affairs Desk with:
 * - Year selection tabs (2026 Active, 2025 Archive, 2024 Historical)
 * - Monthly archive filter tabs
 * - Category filter pills (Legal & Constitutional, Governance, Economic, etc.)
 * - Real-time debounced keyword search
 * - Substantive entry cards with sources, legal relevance, traps, and practice MCQ links.
 */

(function () {
  'use strict';

  var global = typeof window !== 'undefined' ? window : this;

  var CurrentAffairsDesk = {
    selectedYear: 'all',
    selectedMonth: 'all',
    selectedCategory: 'all',
    searchQuery: '',
    searchDebounceTimer: null,

    init: function (containerEl) {
      if (!containerEl) return;
      this.container = containerEl;
      this.selectedYear = 'all';
      this.selectedMonth = 'all';
      this.selectedCategory = 'all';
      this.searchQuery = '';
      this.render();
    },

    getFilteredArchives: function () {
      var archives = global.CURRENT_MONTHLY_ARCHIVE || [];
      if (this.selectedYear === 'all') return archives;
      var y = this.selectedYear;
      return archives.filter(function (a) {
        return a.year === y || (a.monthKey && a.monthKey.startsWith(y));
      });
    },

    getEntries: function () {
      var entries = global.CURRENT_AFFAIRS_DESK || [];
      var self = this;

      return entries.filter(function (item) {
        // Year filter (if specific year selected and month is 'all')
        if (self.selectedYear !== 'all' && self.selectedMonth === 'all') {
          var y = self.selectedYear;
          if (!item.eventDate || !item.eventDate.startsWith(y)) {
            return false;
          }
        }

        // Month filter
        if (self.selectedMonth !== 'all') {
          var mk = self.selectedMonth;
          if (item.monthKey !== mk && (!item.eventDate || !item.eventDate.startsWith(mk))) {
            return false;
          }
        }

        // Category filter
        if (self.selectedCategory !== 'all') {
          if (item.category !== self.selectedCategory) {
            return false;
          }
        }

        // Search query
        if (self.searchQuery.trim().length > 0) {
          var q = self.searchQuery.toLowerCase().trim();
          var matchHeadline = (item.headline || '').toLowerCase().includes(q);
          var matchSummary = (item.summary || '').toLowerCase().includes(q);
          var matchExplanation = ((item.significance || item.explanation) || '').toLowerCase().includes(q);
          var matchSource = (item.sourceName || '').toLowerCase().includes(q);
          var traps = item.examTraps || item.examTakeaways || [];
          var matchTraps = traps.some(function (t) {
            return t.toLowerCase().includes(q);
          });
          if (!matchHeadline && !matchSummary && !matchExplanation && !matchSource && !matchTraps) {
            return false;
          }
        }

        return true;
      });
    },

    render: function () {
      if (!this.container) return;
      var entries = this.getEntries();
      var archives = this.getFilteredArchives();
      var allArchives = global.CURRENT_MONTHLY_ARCHIVE || [];
      var allEntries = global.CURRENT_AFFAIRS_DESK || [];
      var self = this;

      var currentArchive = allArchives.find(function (a) {
        return a.monthKey === self.selectedMonth;
      });

      var categories = [
        'All',
        'Legal & Constitutional',
        'National Governance & Policy',
        'Uttar Pradesh State Affairs',
        'Economic Reforms & Finance',
        'Science, Space & Tech',
        'Environment & Climate'
      ];

      var html = `
        <div class="current-desk-container" style="animation: fadeIn 0.3s ease;">
          <!-- Desk Header Banner -->
          <div style="background: linear-gradient(135deg, #142c46, #1b3857 60%, #137d72); border: 1.5px solid #dfbf80; border-radius: 12px; padding: 24px; color: #fff; margin-bottom: 24px; box-shadow: 0 4px 16px rgba(20,44,70,0.12);">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 14px;">
              <div>
                <span style="display: inline-block; background: rgba(223,191,128,0.2); border: 1px solid #dfbf80; color: #f7e6c4; font-size: 11.5px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; padding: 3px 8px; border-radius: 12px; margin-bottom: 8px;">
                  📰 Date-Wise Judicial Desk · January 2024 – November 23, 2026
                </span>
                <h1 style="font-family: Georgia, serif; font-size: 24px; margin: 0 0 6px; color: #fff;">
                  Date-Wise Current Affairs Desk
                </h1>
                <p style="margin: 0; font-size: 14px; color: #e3edf7; max-width: 780px; line-height: 1.5;">
                  Source-verified judicial rulings, statutory gazette notifications, constitutional precedents, national policies, and Uttar Pradesh governance developments curated for the Uttar Pradesh Judicial Services Examination (UP PCS-J).
                </p>
              </div>
              <a href="subject-study.html?subject=gk-current" class="btn btn-gold btn-sm" style="text-decoration: none; font-weight: 600; white-space: nowrap;">
                📖 Browse 10 Structured Chapters
              </a>
            </div>
          </div>

          <!-- Year Selection Tabs -->
          <div style="margin-bottom: 12px;">
            <div style="font-size: 11.5px; font-weight: 700; text-transform: uppercase; color: #607387; letter-spacing: 0.5px; margin-bottom: 6px;">
              🗓️ Archive Period:
            </div>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
              <button class="tab-filter-btn ${this.selectedYear === 'all' ? 'active' : ''}" data-year="all" style="cursor: pointer; padding: 5px 12px; font-size: 12.5px;">
                All Periods (${allEntries.length})
              </button>
              <button class="tab-filter-btn ${this.selectedYear === '2026' ? 'active' : ''}" data-year="2026" style="cursor: pointer; padding: 5px 12px; font-size: 12.5px;">
                🔥 2026 Active Exam Year (Jan–Nov)
              </button>
              <button class="tab-filter-btn ${this.selectedYear === '2025' ? 'active' : ''}" data-year="2025" style="cursor: pointer; padding: 5px 12px; font-size: 12.5px;">
                📚 2025 Archive Year
              </button>
              <button class="tab-filter-btn ${this.selectedYear === '2024' ? 'active' : ''}" data-year="2024" style="cursor: pointer; padding: 5px 12px; font-size: 12.5px;">
                📜 2024 Historical Archive
              </button>
            </div>
          </div>

          <!-- Month Selector Tabs -->
          <div style="margin-bottom: 18px;">
            <div style="font-size: 11.5px; font-weight: 700; text-transform: uppercase; color: #607387; letter-spacing: 0.5px; margin-bottom: 6px;">
              📅 Monthly Archives (${archives.length} Available):
            </div>
            <div style="display: flex; gap: 6px; overflow-x: auto; padding-bottom: 6px; flex-wrap: wrap;">
              <button class="tab-filter-btn ${this.selectedMonth === 'all' ? 'active' : ''}" data-month="all" style="cursor: pointer; padding: 4px 10px; font-size: 12px;">
                All Months (${archives.length})
              </button>
              ${archives.map(function (a) {
                return `
                  <button class="tab-filter-btn ${self.selectedMonth === a.monthKey ? 'active' : ''}" data-month="${a.monthKey}" style="cursor: pointer; padding: 4px 10px; font-size: 12px;">
                    ${a.label}
                  </button>
                `;
              }).join('')}
            </div>
          </div>

          <!-- Monthly Archive Context Callout (if specific month selected) -->
          ${currentArchive ? `
            <div style="background: #edf7f4; border: 1.5px solid #137d72; border-radius: 8px; padding: 14px 18px; margin-bottom: 20px;">
              <div style="font-weight: 700; color: #137d72; font-size: 14px; margin-bottom: 4px;">
                📌 ${currentArchive.label} Overview:
              </div>
              <p style="margin: 0 0 4px; font-size: 13px; color: #1c2e40;">
                ${currentArchive.summary}
              </p>
              <div style="font-size: 12px; color: #607387;">
                <strong>Key Milestone:</strong> ${currentArchive.highlight}
              </div>
            </div>
          ` : ''}

          <!-- Toolbar: Search & Category Filter Pills -->
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px; margin-bottom: 22px; background: #fff; padding: 14px 18px; border-radius: 8px; border: 1px solid #d4b67e;">
            <div style="display: flex; gap: 6px; flex-wrap: wrap; align-items: center;">
              <span style="font-size: 12px; font-weight: 700; color: #142c46; margin-right: 4px;">Category:</span>
              ${categories.map(function (cat) {
                var val = cat === 'All' ? 'all' : cat;
                return `
                  <button class="tab-filter-btn ${self.selectedCategory === val ? 'active' : ''}" data-category="${val}" style="cursor: pointer; padding: 4px 10px; font-size: 12px;">
                    ${cat}
                  </button>
                `;
              }).join('')}
            </div>

            <div style="flex: 1; min-width: 240px; max-width: 380px; position: relative;">
              <input type="text" id="desk-search-input" value="${this.searchQuery}" placeholder="Search headlines, cases, acts..."
                     style="width: 100%; padding: 8px 12px 8px 32px; border: 1px solid #cdb17d; border-radius: 6px; font-size: 13px; outline: none; box-sizing: border-box;">
              <span style="position: absolute; left: 10px; top: 50%; transform: translateY(-50%); font-size: 14px; color: #607387;">🔍</span>
            </div>
          </div>

          <!-- Entries Count Bar -->
          <div style="margin-bottom: 16px; font-size: 13px; color: #607387; display: flex; justify-content: space-between; align-items: center;">
            <span>Showing <strong>${entries.length}</strong> source-verified records</span>
            ${(this.selectedYear !== 'all' || this.selectedMonth !== 'all' || this.selectedCategory !== 'all' || this.searchQuery) ? `
              <button id="desk-reset-btn" class="btn btn-subtle btn-sm" style="cursor: pointer; font-size: 12px;">Reset All Filters</button>
            ` : ''}
          </div>

          <!-- Entry Cards Grid -->
          <div class="desk-entries-grid" style="display: flex; flex-direction: column; gap: 18px;">
            ${entries.length === 0 ? `
              <div style="padding: 40px 20px; text-align: center; background: #fff; border: 1px dashed #cdb17d; border-radius: 8px;">
                <p style="font-size: 15px; color: #607387; margin-bottom: 12px;">No current affairs entries match your active filters.</p>
                <button id="desk-reset-empty-btn" class="btn btn-primary btn-sm">Clear All Filters</button>
              </div>
            ` : entries.map(function (entry) {
              var significanceText = entry.significance || entry.explanation || '';
              var traps = entry.examTraps || entry.examTakeaways || [];
              var isPending = entry.reviewStatus === 'pending_official_gazette';

              return `
                <article class="desk-card" style="background: #fff; border: 1.5px solid #d4b67e; border-radius: 10px; padding: 20px; box-shadow: 0 3px 10px rgba(20,44,70,0.05); transition: box-shadow 0.2s ease;">
                  <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 8px; margin-bottom: 10px;">
                    <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;">
                      <span class="badge badge-paper" style="font-weight: 700; color: #142c46;">📅 ${entry.eventDate}</span>
                      <span class="badge badge-paper" style="background: #edf7f4; color: #137d72; border: 1px solid #137d72;">🏷️ ${entry.category}</span>
                      ${isPending ? `
                        <span class="badge" style="background: #fff7ed; color: #b45309; border: 1px solid #fdba74;">⏳ Pending Gazette</span>
                      ` : `
                        <span class="badge badge-status-active">✓ Verified</span>
                      `}
                    </div>
                    <div style="font-size: 11.5px; color: #607387;">
                      Source: ${entry.sourceUrl ? `<a href="${entry.sourceUrl}" target="_blank" rel="noopener noreferrer" style="color: #137d72; text-decoration: underline;">${entry.sourceName || 'Primary Authority'}</a>` : (entry.sourceName || 'Primary Authority')}
                    </div>
                  </div>

                  <h2 style="font-family: Georgia, serif; font-size: 18px; color: #142c46; margin: 0 0 10px; line-height: 1.35;">
                    ${entry.headline}
                  </h2>

                  <p style="font-size: 13.5px; color: #1c2e40; line-height: 1.6; margin: 0 0 14px;">
                    ${entry.summary}
                  </p>

                  <!-- Legal & Constitutional Significance -->
                  ${significanceText ? `
                    <div style="background: #edf7f4; border-left: 3.5px solid #137d72; padding: 10px 14px; border-radius: 0 6px 6px 0; margin-bottom: 12px;">
                      <strong style="color: #137d72; font-size: 12.5px; display: block; margin-bottom: 4px;">⚖️ Legal &amp; Constitutional Significance:</strong>
                      <p style="margin: 0; font-size: 13px; color: #1c2e40; line-height: 1.5;">${significanceText}</p>
                    </div>
                  ` : ''}

                  <!-- High-Yield Takeaways / Traps -->
                  ${traps && traps.length > 0 ? `
                    <div style="background: #fbf9f4; border: 1px solid #e7c88c; border-radius: 6px; padding: 12px 14px; margin-bottom: 14px;">
                      <strong style="color: #b98a38; font-size: 12.5px; display: block; margin-bottom: 6px;">💡 High-Yield Exam Takeaways &amp; Traps:</strong>
                      <ul style="margin: 0; padding-left: 18px; font-size: 12.5px; color: #1c2e40; line-height: 1.5;">
                        ${traps.map(function (t) {
                          return `<li style="margin-bottom: 4px;">${t}</li>`;
                        }).join('')}
                      </ul>
                    </div>
                  ` : ''}

                  <!-- Actions Row -->
                  <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; border-top: 1px solid #f3f5f8; padding-top: 12px; margin-top: 8px;">
                    <span style="font-size: 11.5px; color: #607387;">Ref ID: <code>${entry.id}</code></span>
                    <div style="display: flex; gap: 8px;">
                      <a href="topic-practice.html?subject=${entry.subjectId || 'gk-current'}&topic=${entry.practiceTopicId || ''}&mode=learn" class="btn btn-outline btn-sm" style="font-size: 12px;">
                        ⚡ Practice MCQs
                      </a>
                      <a href="topic-practice.html?subject=gk-current&mode=pyq" class="btn btn-gold btn-sm" style="font-size: 12px;">
                        📜 Related PYQs (90)
                      </a>
                    </div>
                  </div>
                </article>
              `;
            }).join('')}
          </div>
        </div>
      `;

      this.container.innerHTML = html;
      this.bindEvents();
    },

    bindEvents: function () {
      var self = this;
      if (!this.container) return;

      // Year tabs
      var yearBtns = this.container.querySelectorAll('[data-year]');
      yearBtns.forEach(function (btn) {
        btn.addEventListener('click', function () {
          self.selectedYear = this.dataset.year;
          self.selectedMonth = 'all'; // Reset month when year changes
          self.render();
        });
      });

      // Month tabs
      var monthBtns = this.container.querySelectorAll('[data-month]');
      monthBtns.forEach(function (btn) {
        btn.addEventListener('click', function () {
          self.selectedMonth = this.dataset.month;
          self.render();
        });
      });

      // Category pills
      var catBtns = this.container.querySelectorAll('[data-category]');
      catBtns.forEach(function (btn) {
        btn.addEventListener('click', function () {
          self.selectedCategory = this.dataset.category;
          self.render();
        });
      });

      // Search input with debounce
      var searchInput = this.container.querySelector('#desk-search-input');
      if (searchInput) {
        searchInput.addEventListener('input', function (e) {
          clearTimeout(self.searchDebounceTimer);
          self.searchQuery = e.target.value;
          self.searchDebounceTimer = setTimeout(function () {
            self.render();
            // Restore focus and cursor to search input
            var newInp = self.container.querySelector('#desk-search-input');
            if (newInp) {
              newInp.focus();
              newInp.selectionStart = newInp.selectionEnd = newInp.value.length;
            }
          }, 200);
        });
      }

      // Reset buttons
      var resetBtn = this.container.querySelector('#desk-reset-btn');
      if (resetBtn) {
        resetBtn.addEventListener('click', function () {
          self.selectedYear = 'all';
          self.selectedMonth = 'all';
          self.selectedCategory = 'all';
          self.searchQuery = '';
          self.render();
        });
      }

      var resetEmptyBtn = this.container.querySelector('#desk-reset-empty-btn');
      if (resetEmptyBtn) {
        resetEmptyBtn.addEventListener('click', function () {
          self.selectedYear = 'all';
          self.selectedMonth = 'all';
          self.selectedCategory = 'all';
          self.searchQuery = '';
          self.render();
        });
      }
    }
  };

  global.CurrentAffairsDesk = CurrentAffairsDesk;

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = CurrentAffairsDesk;
  }
})();
