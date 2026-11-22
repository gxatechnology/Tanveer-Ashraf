/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Judicial Learning Academy — Concept & Topic Study Renderer
 */

(function (global) {
  'use strict';

  const ConceptRenderer = {
    currentMode: 'detailed', // 'detailed' | 'quick'
    currentFontSize: 16.5,

    resolveSubjectId: function (topic, chapter) {
      if (topic && topic.subjectId) return topic.subjectId;
      if (chapter && chapter.subjectId) return chapter.subjectId;
      if (!topic || !topic.id) return 'law-constitution';
      const tid = topic.id;
      if (tid.startsWith('top-disab-')) return 'soc-disabilities';
      if (tid.startsWith('top-parent-')) return 'soc-parents';
      if (tid.startsWith('top-dowry-')) return 'soc-dowry';
      if (tid.startsWith('top-dv-')) return 'soc-domestic-violence';
      if (tid.startsWith('top-posh-')) return 'soc-posh';
      if (tid.startsWith('top-pcpndt-')) return 'soc-pcpndt';
      if (tid.startsWith('top-mtp-')) return 'soc-mtp';
      if (tid.startsWith('top-irwa-')) return 'soc-indecent-rep';
      if (tid.startsWith('top-pocso-')) return 'soc-pocso';
      if (tid.startsWith('top-jur-')) return 'law-jurisprudence';
      if (tid.startsWith('top-cnt-')) return 'law-contract';
      if (tid.startsWith('top-tpa-')) return 'law-tpa';
      if (tid.startsWith('top-crim-')) return 'law-criminal';
      if (tid.startsWith('top-crpc-')) return 'law-crpc';
      if (tid.startsWith('top-evi-')) return 'law-evidence';
      if (tid.startsWith('top-cpc-')) return 'law-cpc';
      return 'law-constitution';
    },

    init: function (containerEl, topicId, initialMode) {
      if (!containerEl || !topicId) return;
      ConceptRenderer.currentMode = initialMode || 'detailed';

      const concept = global.LearningEngine.getConceptByTopicId(topicId);
      const topic = global.LearningEngine.getTopicById(topicId);
      const chapter = topic ? global.LearningEngine.getChapterById(topic.chapterId) : null;

      if (!concept) {
        containerEl.innerHTML = `
          <div class="concept-error-card">
            <h3>Concept Note in Development</h3>
            <p>The academic notes for topic <code>${topicId}</code> are currently being authored or indexed.</p>
            <a href="learning-academy.html" class="btn btn-primary">Return to Academy</a>
          </div>
        `;
        return;
      }

      ConceptRenderer.renderHeader(containerEl, topic, chapter);
      ConceptRenderer.renderControls(containerEl, topicId);
      ConceptRenderer.renderBody(containerEl, concept, topic);
      ConceptRenderer.renderNavigation(containerEl, topic);
      ConceptRenderer.bindEvents(containerEl, topicId);
    },

    // ------------------------------------------------------------------------
    // HEADER
    // ------------------------------------------------------------------------
    renderHeader: function (containerEl, topic, chapter) {
      const isRead = global.LearningStorage ? global.LearningStorage.isTopicRead(topic.id) : false;
      const subjectId = ConceptRenderer.resolveSubjectId(topic, chapter);
      const subject = global.LearningEngine ? global.LearningEngine.getSubjectById(subjectId) : null;
      const subjectName = subject ? subject.name : 'Indian Constitution';
      const paperName = subject ? (subject.paperName || subject.paper || 'Paper II Law') : 'Paper II Law';

      const topicMCQs = global.LearningEngine ? global.LearningEngine.getMCQsByTopic(topic.id, subjectId) : [];
      const topicPYQs = global.LearningEngine ? global.LearningEngine.getPYQsByTopic(topic.id, subjectId) : [];

      const concept = global.LearningEngine ? global.LearningEngine.getConceptByTopicId(topic.id) : null;
      const subtitleText = topic.subtitle || (concept && concept.subtitle) || '';

      const headerHtml = `
        <header class="study-view-header">
          <div class="study-breadcrumb">
            <a href="learning-academy.html">Academy</a> &rsaquo;
            <a href="subject-study.html?subject=${subjectId}">${subjectName}</a> &rsaquo;
            <span>${chapter ? chapter.title : 'Chapter'}</span> &rsaquo;
            <span class="active">${topic.title}</span>
          </div>

          <div class="study-title-row">
            <div>
              <div class="study-tag-row">
                <span class="badge badge-paper">${paperName}</span>
                <span class="badge badge-topic-id">${topic.id}</span>
                ${isRead ? '<span class="badge badge-completed">✓ Studied</span>' : '<span class="badge badge-unread">○ Unread</span>'}
              </div>
              <h1 class="study-main-title">${topic.title}</h1>
              ${subtitleText ? `<p class="study-subtitle">${subtitleText}</p>` : ''}
            </div>

            <div class="study-header-actions">
              <button id="btn-toggle-read" class="btn ${isRead ? 'btn-outline' : 'btn-success'} btn-sm">
                ${isRead ? '✓ Mark as Unread' : 'Mark as Read'}
              </button>
              <a href="topic-practice.html?subject=${subjectId}&topic=${topic.id}&mode=learn" class="btn btn-primary btn-sm">
                ⚡ Practise This Topic (${topicMCQs.length} MCQs)
              </a>
              ${topicPYQs.length ? `
                <a href="topic-practice.html?subject=${subjectId}&topic=${topic.id}&mode=pyq" class="btn btn-gold btn-sm">
                  📜 PYQs (${topicPYQs.length})
                </a>
              ` : ''}
            </div>
          </div>
        </header>
      `;

      containerEl.innerHTML = headerHtml;
    },

    // ------------------------------------------------------------------------
    // CONTROLS BAR: DETAILED VS QUICK & FONT SIZING
    // ------------------------------------------------------------------------
    renderControls: function (containerEl, topicId) {
      const controlsHtml = `
        <div class="study-toolbar-card">
          <div class="mode-toggle-group">
            <button class="mode-btn ${ConceptRenderer.currentMode === 'detailed' ? 'active' : ''}" data-mode="detailed">
              📚 Detailed Study Mode
            </button>
            <button class="mode-btn ${ConceptRenderer.currentMode === 'quick' ? 'active' : ''}" data-mode="quick">
              ⚡ Quick Revision Mode
            </button>
          </div>

          <div class="reading-controls-group">
            <span class="ctrl-label">Text Size:</span>
            <button class="font-btn" id="btn-font-dec" title="Decrease font size">A-</button>
            <button class="font-btn" id="btn-font-reset" title="Reset font size">A</button>
            <button class="font-btn" id="btn-font-inc" title="Increase font size">A+</button>
            <button class="print-btn" id="btn-print" title="Print this study note">🖨️ Print</button>
          </div>
        </div>
      `;

      containerEl.insertAdjacentHTML('beforeend', controlsHtml);
    },

    // ------------------------------------------------------------------------
    // BODY: DETAILED VS QUICK REVISION
    // ------------------------------------------------------------------------
    renderBody: function (containerEl, concept, topic) {
      let bodyHtml = '';

      if (ConceptRenderer.currentMode === 'quick') {
        bodyHtml = ConceptRenderer.buildQuickRevisionHtml(concept, topic);
      } else {
        bodyHtml = ConceptRenderer.buildDetailedHtml(concept, topic);
      }

      const wrapperHtml = `<main class="concept-content-area" id="concept-body">${bodyHtml}</main>`;
      containerEl.insertAdjacentHTML('beforeend', wrapperHtml);
    },

    // ------------------------------------------------------------------------
    // DETAILED MODE HTML BUILDER
    // ------------------------------------------------------------------------
    buildDetailedHtml: function (concept, topic) {
      const subjectId = ConceptRenderer.resolveSubjectId(topic);
      let html = '';

      // 1. Overview Section
      const hasOverview = concept.overview || concept.introduction || concept.detailedExplanation;
      if (hasOverview) {
        html += `
          <section class="concept-section" id="sec-overview">
            <h2 class="section-title"><span class="title-icon">🏛️</span> 1. ${subjectId === 'law-constitution' ? 'Constitutional' : (subjectId === 'law-cpc' ? 'Procedural' : (subjectId && subjectId.startsWith('soc-') ? 'Statutory' : 'Academic'))} Overview &amp; Blueprint</h2>
            ${subjectId === 'law-cpc' ? `
              <div class="cpc-sim-banner" style="background: linear-gradient(135deg, #142c46, #137d72); color: #fff; padding: 12px 16px; border-radius: 8px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; border: 1px solid #dfbf80;">
                <div>
                  <b style="color: #dfbf80;">⚖️ The Civil Suit Journey:</b> Follow all 14 stages from Plaint to Decree & Execution.
                </div>
                <a href="civil-suit-journey.html" class="btn-micro" style="background: #dfbf80; color: #142c46; font-weight: bold; text-decoration: none; padding: 4px 10px; border-radius: 6px;">Open Journey Simulator →</a>
              </div>
            ` : ''}
            <div class="callout callout-info">
              ${concept.learningObjective ? `<p><strong>🎯 Learning Objective:</strong> ${concept.learningObjective}</p>` : ''}
              ${concept.introduction ? `<p><strong>Core Concept:</strong> ${concept.introduction}</p>` : ''}
              ${concept.overview && concept.overview.concept ? `<p><strong>Core Concept:</strong> ${concept.overview.concept}</p>` : ''}
              ${concept.overview && concept.overview.background ? `<p><strong>Historical Context:</strong> ${concept.overview.background}</p>` : ''}
              ${concept.overview && concept.overview.scope ? `<p><strong>Jurisprudential Scope:</strong> ${concept.overview.scope}</p>` : ''}
              ${concept.detailedExplanation ? `<div class="detailed-prose">${concept.detailedExplanation}</div>` : ''}
            </div>
          </section>
        `;
      }

      // 2. Statutory Provisions (Bare Act Breakdown)
      const provList = concept.provisions || concept.keyProvisions || [];
      if (provList.length) {
        const isCriminalSubject = ['law-criminal', 'law-crpc', 'law-evidence'].includes(subjectId) ||
          provList.some(p => (p.article || p.provision || p.section || '').includes('BNS') || (p.article || p.provision || p.section || '').includes('IPC') || (p.article || p.provision || p.section || '').includes('BNSS') || (p.article || p.provision || p.section || '').includes('CrPC') || (p.article || p.provision || p.section || '').includes('BSA') || (p.article || p.provision || p.section || '').includes('IEA'));

        const has106Caveat = (concept.topicId === 'top-crim-06-03' || JSON.stringify(concept).includes('106(2)'));

        html += `
          <section class="concept-section" id="sec-provisions">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 12px;">
              <h2 class="section-title" style="margin: 0;"><span class="title-icon">⚖️</span> 2. Statutory Provisions &amp; Bare Act Analysis</h2>
              ${isCriminalSubject ? `
                <div class="paired-law-track-toggle" style="display: inline-flex; gap: 6px; background: #f0f2f5; padding: 4px; border-radius: 8px; border: 1px solid #d4d8de;">
                  <button class="track-btn active" data-track="all" style="padding: 4px 10px; border-radius: 6px; border: none; font-size: 12px; font-weight: 600; cursor: pointer; background: #142c46; color: #dfbf80;">Compare Both</button>
                  <button class="track-btn" data-track="current" style="padding: 4px 10px; border-radius: 6px; border: none; font-size: 12px; font-weight: 500; cursor: pointer; background: transparent; color: #1c2e40;">Current Law (New)</button>
                  <button class="track-btn" data-track="historical" style="padding: 4px 10px; border-radius: 6px; border: none; font-size: 12px; font-weight: 500; cursor: pointer; background: transparent; color: #1c2e40;">Historical Law (Old)</button>
                </div>
              ` : ''}
            </div>

            ${has106Caveat ? `
              <div class="caveat-banner" style="background: #fff5f5; border-left: 5px solid #a63b49; padding: 12px 16px; border-radius: 6px; margin-bottom: 16px; font-size: 13px; color: #4a282d; border: 1px solid #f8d7da; border-left-width: 5px;">
                <strong>⚠️ Statutory Notice (S.O. 850(E)):</strong> Section 106(2) BNS (Hit-and-Run) was <b>expressly excluded</b> from 1 July 2024 enforcement and remains <b>NOT IN FORCE</b>. Historical questions reflect IPC Section 304A.
              </div>
            ` : ''}

            <div class="provisions-stack">
              ${provList.map((p, idx) => {
                const art = p.article || p.provision || p.section || '';
                const isHist = art.includes('IPC') || art.includes('CrPC') || art.includes('IEA');
                const isCurr = art.includes('BNS') || art.includes('BNSS') || art.includes('BSA');
                const trackType = isCurr ? 'current' : (isHist ? 'historical' : 'neutral');

                return `
                <div class="provision-card provision-track-${trackType}" data-track-type="${trackType}">
                  <div class="provision-header">
                    <span class="badge ${isCurr ? 'badge-primary' : (isHist ? 'badge-secondary' : 'badge-article')}">${art || `Provision ${idx+1}`}</span>
                    <h3 class="provision-heading">${p.heading || p.title || ''}</h3>
                  </div>
                  <div class="bare-act-box">
                    <div class="bare-act-tag">${isCurr ? 'CURRENT STATUTORY TEXT (NEW CODE)' : (isHist ? 'HISTORICAL STATUTORY TEXT (OLD CODE)' : 'BARE ACT STATUTORY TEXT')}</div>
                    <blockquote class="bare-act-quote">${p.text || p.content || p.description || ''}</blockquote>
                  </div>
                  <div class="provision-analysis">
                    <p><strong>Judicial Breakdown &amp; Meaning:</strong> ${p.breakdown || p.explanation || p.description || ''}</p>
                    ${p.exceptions ? `<div class="provision-caveat"><strong>⚠️ Statutory Exceptions &amp; Caveats:</strong> ${p.exceptions}</div>` : ''}
                  </div>
                </div>
              `}).join('')}
            </div>
          </section>
        `;
      }

      // 3. Landmark Case Laws
      if (concept.landmarkCases && concept.landmarkCases.length) {
        html += `
          <section class="concept-section" id="sec-cases">
            <h2 class="section-title"><span class="title-icon">📜</span> 3. Landmark Judicial Precedents &amp; Ratio Decidendi</h2>
            <div class="cases-grid">
              ${concept.landmarkCases.map(c => `
                <div class="case-card">
                  <div class="case-header">
                    <h3 class="case-name">${c.caseName || c.case || c.title || ''}</h3>
                    <span class="case-citation">${c.citation || ''} ${c.year ? `(${c.year})` : ''}</span>
                  </div>
                  <div class="case-meta">
                    ${c.bench ? `<span class="meta-pill">🏛️ Bench: ${c.bench}</span>` : ''}
                    ${c.judge ? `<span class="meta-pill">⚖️ Author: ${c.judge}</span>` : ''}
                  </div>
                  <div class="case-body">
                    <p class="case-ratio"><strong>Ratio Decidendi:</strong> ${c.ratio || c.summary || ''}</p>
                    ${c.doctrine ? `<p class="case-doctrine"><strong>Key Doctrine Evolved:</strong> ${c.doctrine}</p>` : ''}
                    ${c.precedentValue || c.impact ? `<p class="case-impact"><strong>Exam Significance:</strong> ${c.precedentValue || c.impact}</p>` : ''}
                  </div>
                </div>
              `).join('')}
            </div>
          </section>
        `;
      }

      // 4. Comparison Tables / Statutory Distinctions
      const comparisonList = concept.comparisons || concept.comparisonTables || [];
      if (comparisonList.length) {
        html += `
          <section class="concept-section" id="sec-comparisons">
            <h2 class="section-title"><span class="title-icon">📊</span> 4. Statutory Distinctions &amp; Analytical Comparisons</h2>
            ${comparisonList.map(comp => {
              if (comp.headers && comp.rows) {
                return `
                  <div class="comparison-card">
                    <h3 class="comp-title">${comp.title || 'Comparison Table'}</h3>
                    <div class="table-responsive" style="display:block;width:100%;max-width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;margin:12px 0 20px;border-radius:8px;box-sizing:border-box;">
                      <table class="academic-table" style="width:100%;min-width:540px;border-collapse:collapse;">
                        <thead>
                          <tr>
                            ${comp.headers.map(h => `<th style="white-space:normal!important;word-break:break-word;">${h}</th>`).join('')}
                          </tr>
                        </thead>
                        <tbody>
                          ${comp.rows.map(row => `
                            <tr>
                              ${Array.isArray(row)
                                ? row.map((cell, idx) => `<td class="${idx === 0 ? 'diff-point' : ''}" style="white-space:normal!important;word-break:break-word;">${idx === 0 ? `<strong>${cell}</strong>` : cell}</td>`).join('')
                                : `<td class="diff-point" style="white-space:normal!important;word-break:break-word;"><strong>${row.point || ''}</strong></td><td style="white-space:normal!important;word-break:break-word;">${row.a || ''}</td><td style="white-space:normal!important;word-break:break-word;">${row.b || ''}</td>`
                              }
                            </tr>
                          `).join('')}
                        </tbody>
                      </table>
                    </div>
                  </div>
                `;
              }
              return `
                <div class="comparison-card">
                  <h3 class="comp-title">${comp.title || 'Comparison Table'}</h3>
                  <div class="table-responsive" style="display:block;width:100%;max-width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;margin:12px 0 20px;border-radius:8px;box-sizing:border-box;">
                    <table class="academic-table" style="width:100%;min-width:540px;border-collapse:collapse;">
                      <thead>
                        <tr>
                          <th style="white-space:normal!important;word-break:break-word;">Point of Distinction</th>
                          <th style="white-space:normal!important;word-break:break-word;">${comp.colA || 'Concept A'}</th>
                          <th style="white-space:normal!important;word-break:break-word;">${comp.colB || 'Concept B'}</th>
                        </tr>
                      </thead>
                      <tbody>
                        ${(comp.rows || []).map(r => `
                          <tr>
                            <td class="diff-point" style="white-space:normal!important;word-break:break-word;"><strong>${r.point}</strong></td>
                            <td style="white-space:normal!important;word-break:break-word;">${r.a}</td>
                            <td style="white-space:normal!important;word-break:break-word;">${r.b}</td>
                          </tr>
                        `).join('')}
                      </tbody>
                    </table>
                  </div>
                </div>
              `;
            }).join('')}
          </section>
        `;
      }

      // 5. Diagrams / Visual Charts
      const hasDiagrams = (concept.diagrams && concept.diagrams.length) || concept.diagramId;
      if (hasDiagrams) {
        html += `
          <section class="concept-section" id="sec-diagrams">
            <h2 class="section-title"><span class="title-icon">🗺️</span> 5. Visual Schematic &amp; Conceptual Architecture</h2>
            ${concept.diagrams && concept.diagrams.length ? concept.diagrams.map(diag => `
              <div class="diagram-viewer-card">
                <h3 class="diagram-title">${diag.title || 'Schematic Diagram'}</h3>
                <div class="diagram-img-box">
                  <img src="assets/learning/images/diagrams/${diag.filename}" alt="${diag.title}" loading="lazy" class="responsive-diagram-svg" />
                </div>
                ${diag.caption ? `<p class="diagram-caption">📌 ${diag.caption}</p>` : ''}
              </div>
            `).join('') : ''}
            ${concept.diagramId ? `
              <div class="diagram-viewer-card">
                <h3 class="diagram-title">${topic.title} Schematic</h3>
                <div class="diagram-img-box">
                  <img src="assets/learning/images/diagrams/${concept.diagramId.endsWith('.svg') ? concept.diagramId : `${concept.diagramId}.svg`}" alt="${topic.title}" loading="lazy" class="responsive-diagram-svg" />
                </div>
                ${concept.diagramExplanation ? `<p class="diagram-caption">📌 ${concept.diagramExplanation}</p>` : ''}
              </div>
            ` : ''}
          </section>
        `;
      }

      // 6. Interactive Flashcards
      let flashcardsList = concept.flashcards || [];
      if ((!flashcardsList || !flashcardsList.length) && provList.length) {
        flashcardsList = provList.slice(0, 3).map((p, idx) => ({
          front: `What is the key statutory mandate under ${p.section || p.article || p.provision || `Provision ${idx + 1}`}?`,
          back: p.breakdown || p.explanation || p.description || p.text || 'Statutory requirement under the Act.',
          article: p.section || p.article || p.provision || ''
        }));
      } else if ((!flashcardsList || !flashcardsList.length) && concept.landmarkCases && concept.landmarkCases.length) {
        flashcardsList = concept.landmarkCases.slice(0, 3).map((c, idx) => ({
          front: `What was held in ${c.caseName || c.case || c.title || `Case ${idx + 1}`}?`,
          back: c.ratio || c.summary || 'Landmark precedent ruling.',
          article: c.citation || (c.year ? `Year ${c.year}` : '')
        }));
      }

      if (flashcardsList.length) {
        html += `
          <section class="concept-section" id="sec-flashcards">
            <h2 class="section-title"><span class="title-icon">💡</span> 6. Active Recall Flashcards (Click to Flip)</h2>
            <div class="flashcards-deck">
              ${flashcardsList.map((fc, idx) => `
                <div class="flashcard-container" data-card-idx="${idx}">
                  <div class="flashcard-inner">
                    <div class="flashcard-front">
                      <span class="card-num">Card #${idx+1}</span>
                      <p class="card-question">${fc.front || fc.question || ''}</p>
                      <span class="flip-hint">👆 Click to reveal legal rule</span>
                    </div>
                    <div class="flashcard-back">
                      <span class="card-num">Answer #${idx+1}</span>
                      <p class="card-answer">${fc.back || fc.answer || ''}</p>
                      ${fc.article ? `<span class="card-provision">${fc.article}</span>` : ''}
                    </div>
                  </div>
                </div>
              `).join('')}
            </div>
          </section>
        `;
      }

      // 7. Exam Traps & Common Errors
      const trapsList = concept.examTraps || concept.prelimTraps || concept.misconceptions || concept.examTips || [];
      if (trapsList.length) {
        html += `
          <section class="concept-section" id="sec-traps">
            <h2 class="section-title"><span class="title-icon">⚠️</span> 7. Preliminary Exam Traps &amp; Examiner Pitfalls</h2>
            <div class="traps-container">
              ${trapsList.map(trap => `
                <div class="trap-card">
                  <div class="trap-trap-row">
                    <span class="trap-badge">❌ COMMON CONFUSION</span>
                    <p class="trap-text">${trap.trap || trap.confusion || trap.myth || trap.tip || trap.mistake || ''}</p>
                  </div>
                  <div class="trap-correct-row">
                    <span class="correct-badge">✓ EXACT LEGAL POSITION</span>
                    <p class="correct-text">${trap.correct || trap.rule || trap.reality || trap.point || ''}</p>
                  </div>
                  ${trap.authority ? `<p class="trap-auth"><strong>Authority:</strong> ${trap.authority}</p>` : ''}
                </div>
              `).join('')}
            </div>
          </section>
        `;
      }

      return html;
    },

    // ------------------------------------------------------------------------
    // QUICK REVISION MODE HTML BUILDER
    // ------------------------------------------------------------------------
    buildQuickRevisionHtml: function (concept, topic) {
      const q = concept.quickRevision || {};
      const quickPoints = q.keyPoints || concept.quickRevisionPoints || [];

      let html = `
        <div class="quick-revision-wrapper">
          <div class="callout callout-gold">
            <h2 style="font-family: Georgia, serif; font-size: 18px; margin: 0 0 6px; color: #142c46;">⚡ Quick Revision Capsule: ${topic.title}</h2>
            <p style="margin: 0; font-size: 13px; color: #607387;">High-yield statutory provisions, critical case law ratios, and non-negotiable memory points for UP PCS-J rapid review.</p>
          </div>

          <!-- High Yield Key Points -->
          ${quickPoints.length ? `
            <div class="quick-card">
              <h3 class="quick-card-title">📌 High-Yield Takeaways</h3>
              <ul class="quick-list">
                ${quickPoints.map(pt => `<li>${pt}</li>`).join('')}
              </ul>
            </div>
          ` : ''}

          <!-- Crucial Articles Grid -->
          ${q.crucialArticles && q.crucialArticles.length ? `
            <div class="quick-card">
              <h3 class="quick-card-title">⚖️ Crucial Statutory Provisions</h3>
              <div class="quick-articles-grid">
                ${q.crucialArticles.map(art => `
                  <div class="quick-art-pill">
                    <strong>${art.article || art.title || art.section}:</strong> ${art.summary || art.rule || art.explanation || ''}
                  </div>
                `).join('')}
              </div>
            </div>
          ` : ((concept.provisions || concept.keyProvisions) && (concept.provisions || concept.keyProvisions).length ? `
            <div class="quick-card">
              <h3 class="quick-card-title">⚖️ Crucial Statutory Provisions</h3>
              <div class="quick-articles-grid">
                ${(concept.provisions || concept.keyProvisions).map(p => `
                  <div class="quick-art-pill">
                    <strong>${p.article || p.provision || p.section || 'Provision'}:</strong> ${p.title || p.heading ? `${p.title || p.heading} — ` : ''}${p.description || p.breakdown || p.text || ''}
                  </div>
                `).join('')}
              </div>
            </div>
          ` : '')}

          <!-- Cases at a Glance -->
          ${q.leadingCases && q.leadingCases.length ? `
            <div class="quick-card">
              <h3 class="quick-card-title">📜 Precedents at a Glance</h3>
              <div class="quick-cases-list">
                ${q.leadingCases.map(c => `
                  <div class="quick-case-item">
                    <strong>${c.name || c.caseName || c.case} (${c.year || ''}):</strong> ${c.ratio}
                  </div>
                `).join('')}
              </div>
            </div>
          ` : (concept.landmarkCases && concept.landmarkCases.length ? `
            <div class="quick-card">
              <h3 class="quick-card-title">📜 Precedents at a Glance</h3>
              <div class="quick-cases-list">
                ${concept.landmarkCases.map(c => `
                  <div class="quick-case-item">
                    <strong>${c.caseName || c.case || c.title || ''} ${c.year ? `(${c.year})` : ''}:</strong> ${c.ratio || c.summary || ''}
                  </div>
                `).join('')}
              </div>
            </div>
          ` : '')}

          <!-- Exam Memory Mnemonics / Memory Hooks -->
          ${q.memoryHooks && q.memoryHooks.length ? `
            <div class="quick-card">
              <h3 class="quick-card-title">🧠 Memory Hooks &amp; Mnemonics</h3>
              <div class="mnemonics-stack">
                ${q.memoryHooks.map(h => `
                  <div class="mnemonic-box">
                    <span class="mn-badge">${h.hook || 'Mnemonic'}</span>
                    <p class="mn-desc">${h.explanation || h.meaning}</p>
                  </div>
                `).join('')}
              </div>
            </div>
          ` : ''}
        </div>
      `;

      return html;
    },

    // ------------------------------------------------------------------------
    // BOTTOM NAVIGATION (PREVIOUS & NEXT TOPIC)
    // ------------------------------------------------------------------------
    renderNavigation: function (containerEl, currentTopic) {
      const subjectId = ConceptRenderer.resolveSubjectId(currentTopic);
      const allTopics = global.LearningEngine ? global.LearningEngine.getTopicsBySubject(subjectId) : (global.CONSTITUTION_TOPICS || []);
      const currIdx = allTopics.findIndex(t => t.id === currentTopic.id);
      const prevTopic = currIdx > 0 ? allTopics[currIdx - 1] : null;
      const nextTopic = currIdx < allTopics.length - 1 ? allTopics[currIdx + 1] : null;

      const navHtml = `
        <footer class="study-nav-footer">
          <div class="nav-prev-col">
            ${prevTopic ? `
              <a href="subject-study.html?subject=${subjectId}&chapter=${prevTopic.chapterId}&topic=${prevTopic.id}" class="nav-link-card">
                <span class="nav-dir">&larr; Previous Topic</span>
                <span class="nav-title">${prevTopic.title}</span>
              </a>
            ` : '<div class="nav-empty"></div>'}
          </div>

          <div class="nav-center-col">
            <a href="topic-practice.html?subject=${subjectId}&topic=${currentTopic.id}&mode=learn" class="btn btn-primary">
              ⚡ Practise Topic MCQs
            </a>
          </div>

          <div class="nav-next-col">
            ${nextTopic ? `
              <a href="subject-study.html?subject=${subjectId}&chapter=${nextTopic.chapterId}&topic=${nextTopic.id}" class="nav-link-card">
                <span class="nav-dir">Next Topic &rarr;</span>
                <span class="nav-title">${nextTopic.title}</span>
              </a>
            ` : '<div class="nav-empty"></div>'}
          </div>
        </footer>
      `;

      containerEl.insertAdjacentHTML('beforeend', navHtml);
    },

    // ------------------------------------------------------------------------
    // EVENT BINDINGS
    // ------------------------------------------------------------------------
    bindEvents: function (containerEl, topicId) {
      // Toggle Mode Buttons
      const modeBtns = containerEl.querySelectorAll('.mode-btn');
      modeBtns.forEach(btn => {
        btn.addEventListener('click', function () {
          const newMode = this.dataset.mode;
          if (newMode !== ConceptRenderer.currentMode) {
            ConceptRenderer.currentMode = newMode;
            // Update active state
            modeBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            // Re-render body
            const bodyEl = containerEl.querySelector('#concept-body');
            const concept = global.LearningEngine.getConceptByTopicId(topicId);
            const topic = global.LearningEngine.getTopicById(topicId);
            if (bodyEl && concept && topic) {
              bodyEl.innerHTML = (newMode === 'quick') ? 
                ConceptRenderer.buildQuickRevisionHtml(concept, topic) :
                ConceptRenderer.buildDetailedHtml(concept, topic);
              ConceptRenderer.bindFlashcards(containerEl);
              ConceptRenderer.bindTrackButtons(containerEl);
            }
          }
        });
      });

      ConceptRenderer.bindTrackButtons(containerEl);

      // Mark as Read Button
      const btnToggleRead = containerEl.querySelector('#btn-toggle-read');
      if (btnToggleRead && global.LearningStorage) {
        btnToggleRead.addEventListener('click', function () {
          const isCurrentlyRead = global.LearningStorage.isTopicRead(topicId);
          if (isCurrentlyRead) {
            global.LearningStorage.unmarkTopicRead(topicId);
            this.textContent = 'Mark as Read';
            this.className = 'btn btn-success btn-sm';
          } else {
            global.LearningStorage.markTopicRead(topicId, ConceptRenderer.currentMode);
            this.textContent = '✓ Mark as Unread';
            this.className = 'btn btn-outline btn-sm';
          }
        });
      }

      // Font Size Controls
      const bodyEl = containerEl.querySelector('#concept-body');
      const btnDec = containerEl.querySelector('#btn-font-dec');
      const btnReset = containerEl.querySelector('#btn-font-reset');
      const btnInc = containerEl.querySelector('#btn-font-inc');
      const btnPrint = containerEl.querySelector('#btn-print');

      if (btnDec && bodyEl) {
        btnDec.addEventListener('click', () => {
          if (ConceptRenderer.currentFontSize > 13) {
            ConceptRenderer.currentFontSize -= 1.5;
            bodyEl.style.fontSize = ConceptRenderer.currentFontSize + 'px';
          }
        });
      }
      if (btnReset && bodyEl) {
        btnReset.addEventListener('click', () => {
          ConceptRenderer.currentFontSize = 16.5;
          bodyEl.style.fontSize = '16.5px';
        });
      }
      if (btnInc && bodyEl) {
        btnInc.addEventListener('click', () => {
          if (ConceptRenderer.currentFontSize < 22) {
            ConceptRenderer.currentFontSize += 1.5;
            bodyEl.style.fontSize = ConceptRenderer.currentFontSize + 'px';
          }
        });
      }
      if (btnPrint) {
        btnPrint.addEventListener('click', () => window.print());
      }

      // Flashcards Flip Handler
      ConceptRenderer.bindFlashcards(containerEl);
    },

    bindFlashcards: function (containerEl) {
      const cards = containerEl.querySelectorAll('.flashcard-container');
      cards.forEach(c => {
        c.addEventListener('click', function () {
          this.classList.toggle('is-flipped');
        });
      });
    },

    bindTrackButtons: function (containerEl) {
      const trackBtns = containerEl.querySelectorAll('.track-btn');
      trackBtns.forEach(btn => {
        btn.addEventListener('click', function () {
          const track = this.dataset.track;
          trackBtns.forEach(b => {
            b.classList.remove('active');
            b.style.background = 'transparent';
            b.style.color = '#1c2e40';
            b.style.fontWeight = '500';
          });
          this.classList.add('active');
          this.style.background = '#142c46';
          this.style.color = '#dfbf80';
          this.style.fontWeight = '600';

          const cards = containerEl.querySelectorAll('.provision-card[data-track-type]');
          cards.forEach(c => {
            const cType = c.dataset.trackType;
            if (track === 'all') {
              c.style.display = '';
            } else if (track === 'current') {
              c.style.display = (cType === 'current' || cType === 'neutral') ? '' : 'none';
            } else if (track === 'historical') {
              c.style.display = (cType === 'historical' || cType === 'neutral') ? '' : 'none';
            }
          });
        });
      });
    }
  };

  global.ConceptRenderer = ConceptRenderer;

})(typeof window !== 'undefined' ? window : global);
