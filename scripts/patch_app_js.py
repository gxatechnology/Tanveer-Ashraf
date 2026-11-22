# Patch assets/js/app.js for Phase 5
with open('assets/js/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_home = """function home(){
  let done = new Set(state.read).size;
  let attempts = state.history.length;
  let accuracy = state.history.reduce((s, r) => s + r.correct, 0);
  let marked = state.history.reduce((s, r) => s + r.correct + r.wrong, 0);

  let arenaData = {};
  try { arenaData = JSON.parse(localStorage.getItem('tanveer-arena-v1') || '{}'); } catch(e){}
  let arenaXP = arenaData.xp || 0;
  let arenaLevel = arenaData.level || 1;
  let mCount = arenaData.journey && arenaData.journey.completedMissions ? Object.keys(arenaData.journey.completedMissions).length : 0;

  // Dynamic Continue Learning Card
  let continueHtml = '';
  if (state.active) {
    let answered = Object.keys(state.active.answers || {}).length;
    continueHtml = `
      <div class="continue-card">
        <div class="continue-info">
          <h3>📝 Examination in Progress: ${esc(state.active.title)}</h3>
          <p>${answered} of ${state.active.ids.length} questions attempted. Timer is running.</p>
        </div>
        ${btn('Resume Examination →', "go('exam')", 'primary')}
      </div>
    `;
  } else if (arenaData.journey && mCount > 0 && mCount < 36) {
    continueHtml = `
      <div class="continue-card">
        <div class="continue-info">
          <h3>🗺️ Road to Judiciary: Campaign in Progress</h3>
          <p>${mCount} of 36 missions completed. Advance to your next chapter.</p>
        </div>
        <a class="btn primary" href="judiciary-journey.html">Continue Campaign →</a>
      </div>
    `;
  } else if (state.saved && state.saved.length > 0) {
    continueHtml = `
      <div class="continue-card">
        <div class="continue-info">
          <h3>☆ Revision Centre Ready</h3>
          <p>${state.saved.length} questions queued for active recall review.</p>
        </div>
        ${btn('Open Revision Centre →', "go('saved')", 'primary')}
      </div>
    `;
  }

  el.innerHTML = `
    <div class="hero home-hero">
      <div class="hero-main">
        <div class="eyebrow">THE JUDICIAL STUDY ROOM · 2026–27</div>
        <h1>Discipline today.<br><em>Justice tomorrow.</em></h1>
        <p>A dedicated learning space for Tanveer Ashraf. Master the previous papers, practise with purpose and build confidence for the UP Judicial Services examination.</p>
        <div class="actions">
          <a class="btn gold" href="brain-arena.html">⚡ Legal Brain Arena</a>
          ${btn('Explore question library','openNotes()','')}
          <a class="btn ghost" href="bns.html">BNS · 358 sections</a>
          <a class="btn ghost" href="search.html">Smart search</a>
          ${btn('Start a test',"go('practice')",'ghost')}
          ${state.active ? btn('Resume test',"go('exam')",'ghost') : ''}
        </div>
        <div class="hero-foot"><span>⚖</span> LAW & GENERAL KNOWLEDGE <span>·</span> PRELIMINARY EXAM</div>
      </div>
      <div class="hero-portrait">
        <div class="portrait-ring"></div>
        <img src="assets/images/tanveer.webp" alt="Portrait of Tanveer Ashraf">
        <div class="portrait-label">
          <strong>Tanveer Ashraf</strong>
          <small>Personal preparation workspace</small>
        </div>
      </div>
    </div>

    ${continueHtml}

    <div class="grid stats">
      ${stat('Previous-year questions', fmt(available.length), 'English notes · 2012–2023')}
      ${stat('Test-ready questions', fmt(eligible.length), 'Scorable imported answer keys')}
      ${stat('Questions studied', fmt(done), Math.round(done/available.length*100) + '% of library')}
      ${stat('Practice accuracy', marked ? Math.round(accuracy/marked*100) + '%' : '—', attempts + ' completed tests')}
    </div>

    <div class="row section">
      <h2>Quick Actions</h2>
      <span class="caption">Direct 1-click access</span>
    </div>
    <div class="quick-actions-grid">
      <a href="tests.html?kind=quick&size=10" class="quick-action-btn"><span>⚡</span> 10-Question Test</a>
      <a href="tests.html?kind=quick&size=25" class="quick-action-btn"><span>⚡</span> 25-Question Test</a>
      <a href="bns.html" class="quick-action-btn"><span>§</span> BNS 358 Sections</a>
      <a href="memory-match.html" class="quick-action-btn"><span>🧠</span> Memory Match</a>
      <a href="section-sprint.html" class="quick-action-btn"><span>⏱️</span> Section Sprint</a>
      <a href="judiciary-journey.html" class="quick-action-btn"><span>🗺️</span> Today's Study Plan</a>
    </div>

    <div class="row section">
      <h2>Explore by examination year</h2>
      <span class="caption">Oldest to latest</span>
    </div>
    <div class="grid">
      ${years.map(y => {
        let a = available.filter(q => q.year === y);
        let r = a.filter(q => state.read.includes(q.id)).length;
        return `
          <div class="card yearcard">
            <div class="row"><span class="year">${y}</span><span class="badge">${a.length} questions</span></div>
            <p class="muted">General Knowledge & Law</p>
            <div class="bar"><i style="width:${100*r/a.length}%"></i></div>
            <div class="caption">${r} studied</div>
            <div class="actions">
              ${btn('GK', `openNotes(${y},'GK')`, 'mini')}
              ${btn('Law', `openNotes(${y},'LAW')`, 'mini')}
              ${btn('Test', `openTest(${y})`, 'mini primary')}
            </div>
          </div>
        `;
      }).join('')}
    </div>

    <!-- Arena Spotlight Card -->
    <div class="card" style="margin:24px 0 16px; background:linear-gradient(135deg, #142c46 0%, #102847 100%); color:#fff; border:1px solid #dfbf80; border-radius:8px; padding:20px;">
      <div class="row" style="align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px;">
        <div>
          <span class="badge" style="background:#b98a38; color:#fff; font-weight:700;">⚡ All 8 Games Live & Playable</span>
          <h3 style="color:#dfbf80; margin:8px 0 4px; font-family:'Georgia', serif; font-size:1.35rem;">Legal Brain Arena</h3>
          <p style="color:#cbd5e1; margin:0; font-size:0.92rem;">Level ${arenaLevel} • ${arenaXP} XP • 330 Myth Busters • 36 Campaign Missions • 38 Judicial Honors</p>
        </div>
        <div style="display:flex; gap:10px;">
          <a href="brain-arena.html" class="btn gold" style="font-weight:700;">Enter Arena</a>
          <a href="achievements.html" class="btn ghost" style="border-color:#dfbf80; color:#dfbf80;">🏆 38 Honors</a>
        </div>
      </div>
    </div>

    <div class="section grid">
      <div class="card">
        <h3>Quick practice</h3>
        <p class="muted">Choose 10, 20, 25 or 50 questions by year or subject.</p>
        ${btn('Choose practice', "go('practice')", 'mini primary')}
      </div>
      <div class="card">
        <h3>Exam simulation</h3>
        <p class="muted">150 question paper, 120 minutes, GK 150 / Law 300 marks, negative marking.</p>
        ${btn('Full paper test', "openFull()", 'mini')}
      </div>
      <div class="card">
        <h3>Review your progress</h3>
        <p class="muted">See attempts, accuracy, score, weak topics and mistakes.</p>
        ${btn('View results', "go('history')", 'mini')}
      </div>
    </div>

    ${dataNotice()}

    <div class="footer">
      Built by Tauqeer Ashraf for Tanveer Ashraf. <a href="about.html">About this initiative</a> · Independent study portal, not affiliated with UPPSC.
    </div>
  `;
}
"""

new_saved = """let revisionTab = 'all';
function saved(){
  let pyqList = available.filter(q => state.saved.includes(q.id));

  let arenaData = {};
  try { arenaData = JSON.parse(localStorage.getItem('tanveer-arena-v1') || '{}'); } catch(e){}
  let weakQueue = (arenaData.weakQueue || []).map(w => ({
    id: w.id || 'err-' + Math.random().toString(36).substr(2,6),
    type: 'arena_error',
    term: w.term || w.concept || w.section || 'Legal Concept',
    statement: w.statement || w.prompt || w.definition || '',
    subject: w.subject || 'Law',
    source: w.source || 'Brain Arena'
  }));

  let totalItems = pyqList.length + weakQueue.length;

  el.innerHTML = `
    <div class="eyebrow">Active Recall & Spaced Repetition</div>
    <h1>Unified Smart Revision Centre</h1>
    <p class="muted">${totalItems} items queued for targeted revision across previous-year questions and cognitive arena games.</p>

    <div class="revision-filter-tabs">
      <button type="button" class="revision-tab-btn ${revisionTab === 'all' ? 'active' : ''}" onclick="setRevisionTab('all')">All Items (${totalItems})</button>
      <button type="button" class="revision-tab-btn ${revisionTab === 'pyq' ? 'active' : ''}" onclick="setRevisionTab('pyq')">Bookmarked PYQs (${pyqList.length})</button>
      <button type="button" class="revision-tab-btn ${revisionTab === 'arena' ? 'active' : ''}" onclick="setRevisionTab('arena')">Arena Errors & Misconceptions (${weakQueue.length})</button>
    </div>

    <div id="revisionListContainer">
      ${renderRevisionItems(pyqList, weakQueue)}
    </div>
  `;
}

function setRevisionTab(tab) {
  revisionTab = tab;
  saved();
}

function renderRevisionItems(pyqs, weakItems) {
  let html = '';
  if (revisionTab === 'all' || revisionTab === 'arena') {
    if (weakItems.length > 0) {
      html += `
        <div class="row section">
          <h3>⚡ Arena Statutory Errors & Misconceptions (${weakItems.length})</h3>
        </div>
        <div class="grid" style="margin-bottom:24px;">
          ${weakItems.map(item => `
            <div class="card" style="border-left:4px solid #a63b49;">
              <div class="row" style="margin-bottom:6px;">
                <span class="badge" style="background:#fef2f2; color:#a63b49; border:1px solid #fecaca;">Priority Revision</span>
                <span class="tag">${esc(item.subject)}</span>
              </div>
              <h4 style="margin:4px 0 6px; color:#142c46;">${esc(item.term)}</h4>
              <p style="font-size:0.88rem; color:#475569; margin:0 0 10px;">${esc(item.statement)}</p>
              <div class="actions">
                <a href="search.html?q=${encodeURIComponent(item.term)}" class="btn mini">🔍 Explore in Search</a>
                <button type="button" class="btn mini primary" onclick="resolveWeakItem('${item.id}')">✓ Mark Resolved</button>
              </div>
            </div>
          `).join('')}
        </div>
      `;
    }
  }

  if (revisionTab === 'all' || revisionTab === 'pyq') {
    if (pyqs.length > 0) {
      html += `
        <div class="row section">
          <h3>☆ Bookmarked Examination Questions (${pyqs.length})</h3>
        </div>
        ${pyqs.map(q => questionCard(q, true)).join('')}
      `;
    }
  }

  if (!html) {
    html = `<div class="card empty">No items found in this revision category. Bookmark questions during study or complete Arena trials to populate active recall lists.</div>`;
  }
  return html;
}

function resolveWeakItem(itemId) {
  try {
    let arenaData = JSON.parse(localStorage.getItem('tanveer-arena-v1') || '{}');
    if (Array.isArray(arenaData.weakQueue)) {
      arenaData.weakQueue = arenaData.weakQueue.filter(w => w.id !== itemId);
      localStorage.setItem('tanveer-arena-v1', JSON.stringify(arenaData));
    }
  } catch(e){}
  saved();
}
"""

new_history = """function history(){
  let h = state.history || [];
  let correct = h.reduce((s, r) => s + r.correct, 0);
  let attempt = h.reduce((s, r) => s + r.attempted, 0);
  let totalScore = h.reduce((s, r) => s + r.score, 0);
  let avgScore = h.length ? (totalScore / h.length).toFixed(1) : 0;
  let bestScore = h.length ? Math.max(...h.map(r => r.score)).toFixed(1) : 0;
  let overallAcc = attempt ? Math.round(correct / attempt * 100) : 0;

  let arenaData = {};
  try { arenaData = JSON.parse(localStorage.getItem('tanveer-arena-v1') || '{}'); } catch(e){}
  let arenaXP = arenaData.xp || 0;
  let arenaLevel = arenaData.level || 1;
  let mCount = arenaData.journey && arenaData.journey.completedMissions ? Object.keys(arenaData.journey.completedMissions).length : 0;
  let achCount = arenaData.achievements ? arenaData.achievements.length : 0;

  el.innerHTML = `
    <div class="eyebrow">Performance Tracking & Analytics</div>
    <h1>Results & Progress Analytics</h1>
    <p class="muted">Verified local examination performance separated from cognitive gaming metrics.</p>

    <div class="grid stats">
      ${stat('Tests Completed', h.length, 'Official pattern simulations')}
      ${stat('Questions Attempted', attempt, 'Scored answer submissions')}
      ${stat('Practice Accuracy', attempt ? overallAcc + '%' : '—', correct + ' correct / ' + (attempt - correct) + ' wrong')}
      ${stat('Best Exam Score', h.length ? bestScore : '—', 'Average score: ' + avgScore)}
    </div>

    <!-- Separate Official Examination vs Game Analytics Grid -->
    <div class="analytics-charts-grid">
      <!-- Exam Performance Chart -->
      <div class="chart-card">
        <h3>📊 Examination Performance Breakdown</h3>
        <div class="chart-bar-row">
          <span class="chart-bar-label">Correct Answers</span>
          <div class="chart-bar-track">
            <div class="chart-bar-fill" style="width:${attempt ? Math.round(correct/attempt*100) : 0}%; background:#137d72;"></div>
          </div>
          <span class="chart-bar-val">${correct}</span>
        </div>
        <div class="chart-bar-row">
          <span class="chart-bar-label">Incorrect Answers</span>
          <div class="chart-bar-track">
            <div class="chart-bar-fill" style="width:${attempt ? Math.round((attempt-correct)/attempt*100) : 0}%; background:#a63b49;"></div>
          </div>
          <span class="chart-bar-val">${attempt - correct}</span>
        </div>
        <div class="chart-bar-row">
          <span class="chart-bar-label">Tests Completed</span>
          <div class="chart-bar-track">
            <div class="chart-bar-fill" style="width:${Math.min(100, h.length * 10)}%; background:#142c46;"></div>
          </div>
          <span class="chart-bar-val">${h.length}</span>
        </div>
      </div>

      <!-- Legal Brain Arena Cognitive Analytics -->
      <div class="chart-card">
        <h3>⚡ Legal Brain Arena Cognitive Analytics</h3>
        <div class="chart-bar-row">
          <span class="chart-bar-label">Arena Level & XP</span>
          <div class="chart-bar-track">
            <div class="chart-bar-fill" style="width:${Math.min(100, (arenaXP % 1000) / 10)}%; background:#dfbf80;"></div>
          </div>
          <span class="chart-bar-val">Lvl ${arenaLevel}</span>
        </div>
        <div class="chart-bar-row">
          <span class="chart-bar-label">Campaign Missions</span>
          <div class="chart-bar-track">
            <div class="chart-bar-fill" style="width:${Math.round((mCount / 36) * 100)}%; background:#137d72;"></div>
          </div>
          <span class="chart-bar-val">${mCount} / 36</span>
        </div>
        <div class="chart-bar-row">
          <span class="chart-bar-label">Judicial Honors</span>
          <div class="chart-bar-track">
            <div class="chart-bar-fill" style="width:${Math.round((achCount / 38) * 100)}%; background:#b98a38;"></div>
          </div>
          <span class="chart-bar-val">${achCount} / 38</span>
        </div>
      </div>
    </div>

    <!-- Test History Table -->
    <div class="card">
      <div class="row">
        <h2>Official Examination History</h2>
        ${btn('Export Full Backup', 'exportProgress()', 'mini')}
      </div>
      ${h.length ? `
        <div class="tablewrap">
          <table>
            <thead>
              <tr>
                <th>Test Title</th>
                <th>Date</th>
                <th>Score</th>
                <th>Correct</th>
                <th>Wrong</th>
                <th>Accuracy</th>
                <th>Review</th>
              </tr>
            </thead>
            <tbody>
              ${h.map((r, i) => {
                let acc = r.attempted ? Math.round(r.correct / r.attempted * 100) : 0;
                return `
                  <tr>
                    <td><strong>${esc(r.title)}</strong></td>
                    <td>${new Date(r.date).toLocaleDateString()}</td>
                    <td>${fmt(r.score)} / ${fmt(r.max)}</td>
                    <td><span style="color:#137d72; font-weight:700;">${r.correct}</span></td>
                    <td><span style="color:#a63b49; font-weight:700;">${r.wrong}</span></td>
                    <td>${acc}%</td>
                    <td>${btn('Review Answers', `openResult(${i})`, 'mini')}</td>
                  </tr>
                `;
              }).join('')}
            </tbody>
          </table>
        </div>
      ` : '<div class="card empty">No examinations completed yet. Complete a test in the Test Centre to populate your historical performance analytics.</div>'}
    </div>

    <!-- Topic Accuracy -->
    <div class="card section">
      <h2>Subject & Topic Accuracy (Weakest First)</h2>
      ${topicTable(h)}
    </div>

    <!-- Unified Backup & Restore Interface -->
    <div class="card section">
      <h3>Unified Study & Arena Data Backup</h3>
      <p class="muted">
        All examination history, bookmarked questions, BNS bookmarks, and Arena game progression are stored in this browser's local storage (tanveer-pcsj-portal-v1, tanveer-arena-v1, tanveer-bns-bookmarks-v1).
        Export a unified JSON backup to preserve your data across browsers or devices.
      </p>
      <div class="actions" style="margin-top:12px;">
        ${btn('Export Unified JSON Backup', 'exportProgress()', 'mini primary')}
        <label class="btn mini" for="importFile">Import Backup File</label>
        <input class="hidden" id="importFile" type="file" accept=".json,application/json">
        ${btn('Reset Local Progress', 'resetProgress()', 'mini danger')}
      </div>
    </div>
  `;

  let imp = $('importFile');
  if (imp) imp.onchange = importProgress;
}

function exportProgress(){
  let arenaData = {};
  try { arenaData = JSON.parse(localStorage.getItem('tanveer-arena-v1') || '{}'); } catch(e){}
  let bnsBookmarks = [];
  try { bnsBookmarks = JSON.parse(localStorage.getItem('tanveer-bns-bookmarks-v1') || '[]'); } catch(e){}

  const backup = {
    version: "3.0.0",
    exportDate: new Date().toISOString(),
    system: "Tanveer Ashraf — Judicial Prep 2026–27",
    portal: state,
    arena: arenaData,
    bnsBookmarks: bnsBookmarks
  };

  const b = new Blob([JSON.stringify(backup, null, 2)], { type: 'application/json' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(b);
  a.download = `tanveer-judicial-prep-backup-v3.0.0-${new Date().toISOString().slice(0,10)}.json`;
  a.click();
  setTimeout(() => URL.revokeObjectURL(a.href), 1000);
}

async function importProgress(e){
  try {
    const file = e.target.files[0];
    if (!file) return;
    const text = await file.text();
    const data = JSON.parse(text);

    let portal = data.portal || (data.saved && data.history ? data : null);
    if (!portal || !Array.isArray(portal.saved) || !Array.isArray(portal.history)) {
      throw new Error("Invalid or unrecognizable backup format.");
    }

    const testCount = portal.history.length;
    const savedCount = portal.saved.length;
    const xpCount = data.arena ? (data.arena.xp || 0) : 0;
    const backupDate = data.exportDate ? new Date(data.exportDate).toLocaleString() : "Unknown date";

    const proceed = confirm(
      `Backup File Verified:\n• Export Date: ${backupDate}\n• Test Results: ${testCount}\n• Saved Questions: ${savedCount}\n• Arena XP: ${xpCount}\n\nDo you want to restore this data? (Existing records will be safely updated).`
    );
    if (!proceed) return;

    state = {
      saved: portal.saved.filter(id => byId[id]),
      read: (portal.read || []).filter(id => byId[id]),
      history: portal.history,
      active: null
    };
    save();

    if (data.arena && typeof data.arena === 'object') {
      localStorage.setItem('tanveer-arena-v1', JSON.stringify(data.arena));
    }
    if (Array.isArray(data.bnsBookmarks)) {
      localStorage.setItem('tanveer-bns-bookmarks-v1', JSON.stringify(data.bnsBookmarks));
    }

    alert("Backup successfully restored! Study records and arena progress updated.");
    history();
  } catch(err) {
    alert("Error restoring backup: " + (err.message || "File could not be parsed."));
  }
}
"""

lines[7] = new_home + "\n"
lines[11] = new_saved + "\n"
lines[21] = new_history + "\n"

with open('assets/js/app.js', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Patched app.js successfully!")
