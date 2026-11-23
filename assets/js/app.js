'use strict';const Q=window.PCSJ_QUESTIONS,available=Q.filter(q=>q.text),byId=Object.fromEntries(Q.map(q=>[q.id,q])),years=[2012,2013,2015,2016,2018,2023],letters=['A','B','C','D'],$=id=>document.getElementById(id),el=$('content');
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));const P=p=>p==='GK'?'General Knowledge':'Law';const fmt=n=>Number(n).toLocaleString('en-IN',{maximumFractionDigits:2});const storageKey='tanveer-pcsj-portal-v1';let state={saved:[],read:[],history:[],active:null};try{let s=JSON.parse(localStorage.getItem(storageKey)||'null');if(s)state={...state,...s}}catch(e){};if(!Array.isArray(state.history))state.history=[];const save=()=>{try{localStorage.setItem(storageKey,JSON.stringify(state));}catch(e){$('topStatus').textContent='Storage unavailable · Export results before closing'}};let view=document.body.dataset.page||'home',filter={year:'all',paper:'all',topic:'all',query:'',page:1,answers:true},mode='practice',result=null,clock=null;const eligible=available.filter(q=>q.eligible);const issueCount=Q.length-eligible.length;const topicList=p=>[...new Set(available.filter(q=>p==='all'||q.paper===p).map(q=>q.topic))].sort();const selectOptions=(arr,val)=>arr.map(([v,l])=>`<option value="${esc(v)}" ${String(v)===String(val)?'selected':''}>${esc(l)}</option>`).join('');const stat=(label,num,desc='')=>`<div class="card stat"><div class="muted">${esc(label)}</div><strong>${esc(num)}</strong><div class="caption">${esc(desc)}</div></div>`;const btn=(text,fn,cls='')=>`<button class="btn ${cls}" onclick="${fn}">${text}</button>`;const routes={home:'index.html',academy:'learning-academy.html',journey:'civil-suit-journey.html',comparison:'comparison-lab.html',arena:'brain-arena.html',notes:'library.html',practice:'tests.html',history:'results.html',saved:'revision.html',exam:'exam.html',result:'review.html',syllabus:'syllabus.html',about:'about.html',bns:'bns.html',search:'search.html'};
function go(v, fallbackHref){
  if(state.active&&view==='exam'&&v!=='exam'&&v!=='result'){
    if(!confirm('Your test is in progress. Leave the screen? Your timer will continue.'))return;
  }
  const targetRoute = routes[v] || fallbackHref;
  // DEFENSIVE NAVIGATION GUARD: Never navigate to undefined, null, or invalid route
  if(!targetRoute || targetRoute === 'undefined' || targetRoute === 'null' || typeof targetRoute !== 'string'){
    console.warn('Navigation guard: Route not found for view:', v);
    if(fallbackHref && typeof fallbackHref === 'string' && fallbackHref !== '#' && !fallbackHref.startsWith('javascript:') && fallbackHref !== 'undefined'){
      location.href = fallbackHref;
    }
    return;
  }
  if(v!==view){
    let params=new URLSearchParams();
    if(v==='notes'){for(let k of ['year','paper','topic','query','page'])params.set(k,filter[k]);params.set('answers',filter.answers?'1':'0');}
    if(v==='practice'){for(let k of ['kind','year','paper','topic','size','negative','timed'])params.set(k,testConfig[k]);}
    if(v==='result'&&result)params.set('id',result.id);
    location.href=targetRoute+(params.size?'?'+params:'');
    return;
  }
  document.querySelectorAll('.nav a').forEach(b=>{b.classList.toggle('active',b.dataset.view===v);if(b.dataset.view===v)b.setAttribute('aria-current','page')});
  render();
  window.scrollTo(0,0);
}
document.querySelectorAll('.nav a').forEach(b=>{
  b.onclick = e => {
    const v = b.dataset.view;
    const href = b.getAttribute('href');
    // If route is not handled or data-view missing, do not intercept; allow valid native link navigation
    if(!v || !routes[v]){
      if(href && href !== '#' && !href.startsWith('javascript:')){
        return; // Allow native browser navigation
      }
      e.preventDefault();
      return;
    }
    e.preventDefault();
    go(v, href);
  };
});
function render(){clearInterval(clock);clock=null;const map={home,notes,practice,history,saved,exam,result:resultView,syllabus,about,bns:()=>window.LegalSearch.renderBNS(el),search:()=>window.LegalSearch.renderSearch(el)};(map[view]||home)()}
function home(){
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

  // Compute Academy stats dynamically from Registry or Phase 6 verified baseline
  const getAcademyStats = () => {
    if (window.LearningEngine && typeof window.LearningEngine.getStats === 'function') {
      return window.LearningEngine.getStats();
    }
    if (Array.isArray(window.ACADEMY_SUBJECTS)) {
      const active = window.ACADEMY_SUBJECTS.filter(s => s && s.status === 'active');
      return {
        activeSubjects: active.length,
        chapters: active.reduce((acc, s) => acc + (s.chaptersCount || 0), 0),
        topics: active.reduce((acc, s) => acc + (s.topicsCount || 0), 0),
        mcqs: active.reduce((acc, s) => acc + (s.mcqsCount || 0), 0),
        pyqs: active.reduce((acc, s) => acc + (s.pyqsCount || 0), 0)
      };
    }
    return {
      activeSubjects: 22,
      chapters: 192,
      topics: 535,
      mcqs: 3775,
      pyqs: 843
    };
  };
  const academyStats = getAcademyStats();

  el.innerHTML = `
    <div class="hero home-hero">
      <div class="hero-main">
        <div class="eyebrow">THE JUDICIAL STUDY ROOM · 2026–27</div>
        <h1>Discipline today.<br><em>Justice tomorrow.</em></h1>
        <p>A dedicated learning space for Tanveer Ashraf. Master the previous papers, practise with purpose and build confidence for the UP Judicial Services examination.</p>
        <div class="actions">
          <a class="btn gold" href="learning-academy.html">🏛️ Subject Academy</a>
          <a class="btn" style="background: rgba(223, 191, 128, 0.25); color: #dfbf80; border: 1px solid #dfbf80;" href="brain-arena.html">⚡ Legal Brain Arena</a>
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

    <div class="card" style="margin-bottom: 24px; border: 2px solid #137d72; background: linear-gradient(135deg, #edf7f4 0%, #ffffff 100%); padding: 20px 24px;">
      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
        <div>
          <span class="badge" style="background: #142c46; color: #dfbf80; margin-bottom: 6px; display: inline-block;">NEW · ACADEMY V3.1 (PHASE 5 BASELINE)</span>
          <h2 style="font-family: Georgia, serif; font-size: 20px; color: #142c46; margin: 0 0 6px;">Subject-wise Judicial Learning Academy</h2>
          <p style="margin: 0; color: #4a5c6e; font-size: 13.5px; max-width: 660px;">Comprehensive syllabus preparation across Paper I (General Knowledge / Social Legislation) and Paper II (Law). <strong>${academyStats.activeSubjects} Active Production Modules</strong> (${academyStats.chapters} Chapters, ${academyStats.topics} Topics, ${fmt(academyStats.mcqs)} Practice MCQs, ${academyStats.pyqs} Mapped Historical PYQs).</p>
        </div>
        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
          <a href="learning-academy.html" class="btn primary" style="text-decoration: none;">🏛️ Explore Academy</a>
          <a href="subject-study.html?subject=law-constitution" class="btn" style="background: #137d72; color: #fff; text-decoration: none; border-color: #137d72;">📖 Study Constitution</a>
          <a href="civil-suit-journey.html" class="btn" style="background: #142c46; color: #dfbf80; text-decoration: none; border-color: #dfbf80;">⚖️ Civil Suit Journey</a>
        </div>
      </div>
    </div>

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
      <a href="learning-academy.html" class="quick-action-btn" style="border-color: #137d72; background: #edf7f4;"><span>🏛️</span> Subject Academy</a>
      <a href="subject-study.html?subject=law-constitution" class="quick-action-btn"><span>📖</span> Constitution Study</a>
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

function dataNotice(){return `<div class="notice"><b>Study edition:</b> ${fmt(available.length)} available questions from the supplied PYQ notes. ${Q.length-available.length} question slot is missing. ${issueCount} slots are excluded from scoring because of incomplete text, disputed/deleted answers or parsing issues. Historical answer keys are imported, not universally certified; 2023 Law includes OCR text. Topic tags are automatically suggested. Original laws are retained.</div>`}
function openNotes(y='all',p='all'){filter={year:String(y),paper:p,topic:'all',query:'',page:1,answers:true};go('notes')}function filtersHTML(){return `<div class="card"><div class="filter"><div class="field"><label for="fy">Year</label><select id="fy">${selectOptions([['all','All years'],...years.map(y=>[y,y])],filter.year)}</select></div><div class="field"><label for="fp">Paper</label><select id="fp">${selectOptions([['all','Both papers'],['GK','General Knowledge'],['LAW','Law']],filter.paper)}</select></div><div class="field"><label for="ft">Topic</label><select id="ft">${selectOptions([['all','All topics'],...topicList(filter.paper).map(t=>[t,t])],filter.topic)}</select></div><div class="field" style="flex:2"><label for="fq">Search questions</label><input id="fq" value="${esc(filter.query)}" placeholder="e.g. IPC 330, res judicata, gandh, Art. 21"></div></div><div class="toolbar" style="margin-top:12px"><label class="check"><input id="fa" type="checkbox" ${filter.answers?'checked':''}> Show answers</label>${btn('Clear filters','openNotes()','mini')}</div></div>`}function filtered(){return available.filter(q=>(filter.year==='all'||q.year==filter.year)&&(filter.paper==='all'||q.paper===filter.paper)&&(filter.topic==='all'||q.topic===filter.topic)&&window.LegalSearch.matchPYQ(q,filter.query))}function notes(){el.innerHTML=`<div class="eyebrow">Study library</div><h1>Previous Year Question Notes</h1><p class="muted">Read English questions with options and answers. Browse by year, paper and suggested topic.</p><div style="height:14px"></div>${filtersHTML()}<div id="noteList"></div>`;['fy','fp','ft','fa','fq'].forEach(id=>$(id).addEventListener(id==='fq'?'input':'change',()=>{filter.year=$('fy').value;let changed=filter.paper!==$('fp').value;filter.paper=$('fp').value;if(changed){$('ft').innerHTML=selectOptions([['all','All topics'],...topicList(filter.paper).map(t=>[t,t])],'all')}filter.topic=$('ft').value;filter.query=$('fq').value;filter.answers=$('fa').checked;filter.page=1;noteList()}));noteList()}
function questionCard(q,show=true){return `<article class="card qcard" id="q-${q.id}"><div class="qmeta"><span>${q.year} · ${P(q.paper)} · Q${q.no} ${q.page?' · Notes p. '+q.page:''}</span><span class="tag">${esc(q.topic)}</span></div><div class="qstem">${esc(q.stem||q.text||'Question unavailable')}</div>${q.options.length===4?`<div class="options">${q.options.map((o,i)=>`<div class="opt ${show&&q.answer===letters[i]?'correct':''}"><b>(${letters[i]})</b><span>${esc(o)}</span></div>`).join('')}</div>`:''}${show?`<div class="answer"><b>Answer: ${q.answer?esc(q.answer+(q.options.length===4?' — '+q.options[letters.indexOf(q.answer)]:'')):'Not available / deleted'}</b>${q.adjusted?'<div class="caption">Practice key adjusted from supplied key '+esc(q.sourceAnswer)+'.</div>':''}</div>`:''}${q.issue?`<p class="notice">Review only: ${esc(q.issue)}</p>`:''}${q.ocr?'<p class="subtle">OCR transcription — compare unclear wording with original paper.</p>':''}<div class="actions">${btn(state.saved.includes(q.id)?'★ Saved':'☆ Save',`toggleSaved('${q.id}')`,'mini')}${btn(state.read.includes(q.id)?'✓ Studied':'Mark studied',`toggleRead('${q.id}')`,'mini')}</div></article>`}function noteList(){let a=filtered(),pages=Math.max(1,Math.ceil(a.length/20));filter.page=Math.min(filter.page,pages);$('noteList').innerHTML=`<div class="row section"><b>${fmt(a.length)} questions</b><span class="caption">Page ${filter.page} of ${pages}</span></div>${a.slice((filter.page-1)*20,filter.page*20).map(q=>questionCard(q,filter.answers)).join('')||'<div class="card empty">No matching questions.</div>'}<div class="row">${btn('← Previous','changePage(-1)','mini')}${btn('Next →','changePage(1)','mini')}</div>`}function changePage(d){filter.page=Math.max(1,Math.min(Math.ceil(filtered().length/20)||1,filter.page+d));noteList();$('noteList').scrollIntoView({block:'start'})}function toggleSaved(id){state.saved=state.saved.includes(id)?state.saved.filter(x=>x!==id):[...state.saved,id];save();refreshCard(id)}function toggleRead(id){state.read=state.read.includes(id)?state.read.filter(x=>x!==id):[...state.read,id];save();refreshCard(id)}function refreshCard(id){if(view==='notes'){let n=$('q-'+id);if(n)n.outerHTML=questionCard(byId[id],filter.answers)}else if(view==='saved')saved()}
let revisionTab = 'all';
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

function openTest(y){testConfig.year=String(y);go('practice')}function openFull(){testConfig.kind='full';testConfig.year='2023';testConfig.paper='GK';go('practice')}
let testConfig={kind:'quick',year:'all',paper:'GK',topic:'all',size:10,negative:true,timed:true};function practice(){el.innerHTML=`<div class="eyebrow">Examination practice</div><h1>Practice & Mock Tests</h1><div class="grid" style="margin-bottom:16px"><div class="card"><h3>Quick test</h3><p class="muted">10–50 selected PYQs. Target a topic or revise across years.</p>${btn('Quick test',"setKind('quick')",testConfig.kind==='quick'?'mini primary':'mini')}</div><div class="card"><h3>Full previous paper</h3><p class="muted">Original order, 150 slots, 120-minute simulation.</p>${btn('Full paper',"setKind('full')",testConfig.kind==='full'?'mini primary':'mini')}</div><div class="card"><h3>Mixed mock</h3><p class="muted">150 randomized PYQs in one paper. Not a predicted question paper.</p>${btn('Mixed mock',"setKind('mock')",testConfig.kind==='mock'?'mini primary':'mini')}</div></div><div class="card"><h2>Configure ${testConfig.kind==='quick'?'quick test':testConfig.kind==='full'?'full paper':'mixed mock'}</h2><div class="filter"><div class="field"><label>Year</label><select id="ty">${selectOptions(testConfig.kind==='full'?years.map(y=>[y,y]):[['all','All years'],...years.map(y=>[y,y])],testConfig.year)}</select></div><div class="field"><label>Subject</label><select id="tp">${selectOptions(testConfig.kind==='quick'?[['all','Mixed GK + Law'],['GK','General Knowledge'],['LAW','Law']]:[['GK','General Knowledge'],['LAW','Law']],testConfig.paper)}</select></div><div class="field ${testConfig.kind==='quick'?'':'hidden'}"><label>Topic</label><select id="tt">${selectOptions([['all','All topics'],...topicList(testConfig.paper).map(t=>[t,t])],testConfig.topic)}</select></div><div class="field ${testConfig.kind==='quick'?'':'hidden'}"><label>Questions</label><select id="tn">${selectOptions([10,20,25,50,100].map(n=>[n,n+' questions']),testConfig.size)}</select></div></div><div class="divider"></div><div class="toolbar"><label class="check"><input type="checkbox" id="neg" ${testConfig.negative?'checked':''}> Negative marking (⅓ of question marks)</label><label class="check"><input type="checkbox" id="timed" ${testConfig.timed?'checked':''}> Countdown timer</label></div><div id="testPreview" class="notice"></div>${btn('Start test','startTest()','primary')} ${state.active?btn('Resume current test',"go('exam')",'') :''}</div>${dataNotice()}`;['ty','tp','tt','tn','neg','timed'].forEach(id=>$(id).onchange=()=>{let changed=testConfig.paper!==$('tp').value;testConfig.year=$('ty').value;testConfig.paper=$('tp').value;if(changed)$('tt').innerHTML=selectOptions([['all','All topics'],...topicList(testConfig.paper).map(t=>[t,t])],'all');testConfig.topic=$('tt').value;testConfig.size=+$('tn').value;testConfig.negative=$('neg').checked;testConfig.timed=$('timed').checked;testPreview()});testConfig.year=$('ty').value;testConfig.paper=$('tp').value;testPreview()}
function setKind(k){testConfig.kind=k;if(k==='full'&&testConfig.year==='all')testConfig.year='2023';if(k!=='quick'&&testConfig.paper==='all')testConfig.paper='GK';testConfig.topic='all';practice()}function pool(){return (testConfig.kind==='full'?Q:eligible).filter(q=>(testConfig.year==='all'||q.year==testConfig.year)&&(testConfig.paper==='all'||q.paper===testConfig.paper)&&(testConfig.kind!=='quick'||testConfig.topic==='all'||q.topic===testConfig.topic))}function testPreview(){let a=pool(),n=testConfig.kind==='full'?a.length:Math.min(testConfig.kind==='quick'?testConfig.size:150,a.length),graded=a.filter(q=>q.eligible).length;let time=testConfig.kind==='quick'?Math.ceil(n*.8):120;$('testPreview').textContent=`${a.length} matching question slots · ${n} in this test · ${testConfig.timed?time+' minutes':'untimed'}${testConfig.kind==='full'?` · ${graded} scoreable, ${a.length-graded} review-only`:''}. GK = 1 mark, Law = 2 marks. Scores use imported practice keys.`}
function shuffled(a){a=[...a];for(let i=a.length-1;i>0;i--){let j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}function startTest(){if(state.active&&!confirm('Replace the unfinished test? Its unsubmitted answers will be lost.'))return;let a=pool();if(testConfig.kind!=='full')a=shuffled(a).slice(0,testConfig.kind==='quick'?testConfig.size:150);if(!a.length){alert('No matching questions. Change your filters.');return}let mins=testConfig.kind==='quick'?Math.ceil(a.length*.8):120;state.active={ids:a.map(q=>q.id),answers:{},flags:[],index:0,start:Date.now(),deadline:testConfig.timed?Date.now()+mins*60000:null,negative:testConfig.negative,kind:testConfig.kind,title:(testConfig.kind==='full'?'Previous paper':testConfig.kind==='mock'?'Mixed mock':'Quick practice')+' · '+(testConfig.year==='all'?'All years':testConfig.year)+' · '+(testConfig.paper==='all'?'Mixed':P(testConfig.paper))};save();go('exam')}
function timeLeft(a){return a.deadline?Math.max(0,Math.ceil((a.deadline-Date.now())/1000)):null}function tick(){let a=state.active;if(!a)return;let t=timeLeft(a);if(t!==null){if($('timer'))$('timer').textContent=[Math.floor(t/3600),Math.floor(t%3600/60),t%60].map(n=>String(n).padStart(2,'0')).join(':');if(t<=0)finish(true)}else if($('timer'))$('timer').textContent='Untimed'}function exam(){let a=state.active;if(!a){go('practice');return}let q=byId[a.ids[a.index]],answered=Object.keys(a.answers).length;el.innerHTML=`<div class="row"><div><div class="eyebrow">Test in progress</div><h2>${esc(a.title)}</h2></div>${btn('Submit test','finish(false)','primary')}</div><div class="split"><div><div class="card qcard" style="margin-top:0"><div class="qmeta"><span>Question ${a.index+1} of ${a.ids.length} · PYQ ${q.year} Q${q.no}</span><span class="badge">${q.eligible?(q.paper==='GK'?1:2)+' mark(s)':'Not scored'}</span></div><div class="qstem">${esc(q.stem||q.text||'Question unavailable in the supplied paper')}</div>${q.options.length===4?`<div class="options">${q.options.map((o,i)=>`<button class="opt ${a.answers[q.id]===letters[i]?'selected':''}" ${q.eligible?'':'disabled'} onclick="answer('${letters[i]}')"><b>(${letters[i]})</b><span>${esc(o)}</span></button>`).join('')}</div>`:''}${!q.eligible?'<div class="notice">Review-only question; excluded from the score. Move to the next question.</div>':''}<div class="divider"></div><div class="toolbar">${btn('← Previous','move(-1)','mini')}${btn('Clear response','clearResponse()','mini')}${btn(a.flags.includes(q.id)?'Unmark review':'Mark for review','flag()','mini')}${btn(a.index===a.ids.length-1?'Finish →':'Save & Next →',a.index===a.ids.length-1?'finish(false)':'move(1)','primary')}</div></div></div><aside class="card sticky"><div class="caption">Time remaining</div><div class="timer" id="timer">--:--:--</div><div class="bar"><i style="width:${100*answered/a.ids.length}%"></i></div><b>${answered} attempted / ${a.ids.length}</b><p class="caption">Green: answered · Amber: marked · Grey: review only</p><div class="palette">${a.ids.map((id,i)=>`<button class="number ${a.answers[id]?'done':''} ${a.flags.includes(id)?'flag':''} ${a.index===i?'now':''} ${!byId[id].eligible?'void':''}" onclick="jump(${i})">${i+1}</button>`).join('')}</div></aside></div>`;tick();if(state.active)clock=setInterval(tick,1000)}function answer(letter){let a=state.active,q=byId[a.ids[a.index]];if(!q.eligible)return;a.answers[q.id]=letter;save();render()}function clearResponse(){let a=state.active;delete a.answers[a.ids[a.index]];save();render()}function flag(){let a=state.active,id=a.ids[a.index];a.flags=a.flags.includes(id)?a.flags.filter(x=>x!==id):[...a.flags,id];save();render()}function move(d){jump(state.active.index+d)}function jump(i){let a=state.active;a.index=Math.min(a.ids.length-1,Math.max(0,i));save();render();window.scrollTo({top:0,behavior:'instant'})}
function finish(auto){let a=state.active;if(!a)return;if(!auto&&!confirm('Submit this test and view your result?'))return;let r={id:Date.now(),title:a.title,date:new Date().toISOString(),elapsed:Math.round((Date.now()-a.start)/1000),negative:a.negative,ids:a.ids,answers:a.answers,correct:0,wrong:0,skipped:0,void:0,max:0,score:0};for(let id of a.ids){let q=byId[id],m=q.paper==='GK'?1:2;if(!q.eligible){r.void++;continue}r.max+=m;if(!a.answers[id])r.skipped++;else if(a.answers[id]===q.answer){r.correct++;r.score+=m}else{r.wrong++;r.score-=a.negative?m/3:0}}r.score=Math.round(r.score*100)/100;r.attempted=r.correct+r.wrong;state.history.unshift(r);state.active=null;result=r;save();try{let mId=new URLSearchParams(window.location.search).get('missionId');if(mId){let ar=JSON.parse(localStorage.getItem('tanveer-arena-v1')||'{}');ar.journey=ar.journey||{};ar.journey.completedMissions=ar.journey.completedMissions||{};ar.journey.completedMissions[mId]={completedAt:new Date().toISOString(),score:r.score,accuracy:r.attempted>0?Math.round((r.correct/r.attempted)*100):0};localStorage.setItem('tanveer-arena-v1',JSON.stringify(ar));}}catch(e){}go('result')}
let reviewMode='all';function resultView(){let r=result;if(!r){go('history');return}let accuracy=r.attempted?Math.round(100*r.correct/r.attempted):0;el.innerHTML=`<div class="hero"><div class="eyebrow">Test completed</div><h1>Practice result</h1><p>${esc(r.title)} · ${new Date(r.date).toLocaleString()}</p></div><div class="grid stats">${stat('Score',fmt(r.score)+' / '+fmt(r.max),'Scoreable marks; negative marking '+(r.negative?'on':'off'))}${stat('Attempted',r.attempted+' / '+r.ids.length,'Includes scored responses only')}${stat('Accuracy',accuracy+'%',r.correct+' correct · '+r.wrong+' incorrect')}${stat('Not attempted',r.skipped,r.void+' review-only slots · '+Math.floor(r.elapsed/60)+' min')}</div><div class="card"><div class="row"><h3>Topic performance</h3>${btn('New test',"go('practice')",'mini primary')}</div>${topicTable([r])}</div><div class="row section"><h2>Answer review</h2><select id="reviewFilter" class="btn">${selectOptions([['all','All questions'],['wrong','Incorrect'],['skipped','Unattempted'],['correct','Correct'],['void','Review only']],reviewMode)}</select></div><div id="reviewList"></div>`;$('reviewFilter').onchange=()=>{reviewMode=$('reviewFilter').value;reviewList()};reviewList()}
function reviewList(){let r=result;let list=r.ids.map(id=>byId[id]).filter(q=>reviewMode==='all'||(reviewMode==='void'&&!q.eligible)||(q.eligible&&((reviewMode==='wrong'&&r.answers[q.id]&&r.answers[q.id]!==q.answer)||(reviewMode==='correct'&&r.answers[q.id]===q.answer)||(reviewMode==='skipped'&&!r.answers[q.id]))));$('reviewList').innerHTML=list.map(q=>`<article class="card qcard"><div class="qmeta"><span>${q.year} · ${P(q.paper)} · Q${q.no}</span><span class="badge">${!q.eligible?'Review only':!r.answers[q.id]?'Unattempted':r.answers[q.id]===q.answer?'Correct':'Incorrect'}</span></div><div class="qstem">${esc(q.stem||q.text)}</div>${q.options.length===4?`<div class="options">${q.options.map((o,i)=>`<div class="opt ${q.answer===letters[i]?'correct':r.answers[q.id]===letters[i]?'wrong':''}"><b>(${letters[i]})</b><span>${esc(o)}</span></div>`).join('')}</div>`:''}<div class="answer">Your answer: <b>${esc(r.answers[q.id]||'—')}</b> · Practice key: <b>${esc(q.answer||'Unavailable')}</b></div>${q.issue?`<p class="notice">${esc(q.issue)}</p>`:''}</article>`).join('')||'<div class="card empty">No questions in this category.</div>'}
function topicTable(rs){let stats={};for(let r of rs)for(let id of r.ids){let q=byId[id];if(!q||!q.eligible||!r.answers[id])continue;let k=P(q.paper)+' · '+q.topic;let s=stats[k]||(stats[k]={n:0,c:0});s.n++;if(r.answers[id]===q.answer)s.c++}let arr=Object.entries(stats).sort((a,b)=>a[1].c/a[1].n-b[1].c/b[1].n);return arr.length?`<div class="tablewrap"><table><thead><tr><th>Topic</th><th>Attempted</th><th>Correct</th><th>Accuracy</th></tr></thead><tbody>${arr.map(([k,s])=>`<tr><td>${esc(k)}</td><td>${s.n}</td><td>${s.c}</td><td>${Math.round(100*s.c/s.n)}%</td></tr>`).join('')}</tbody></table></div>`:'<p class="muted">Attempt questions to see topic-level accuracy.</p>'}
function history(){
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
  let learningData = {};
  try { learningData = JSON.parse(localStorage.getItem('tanveer-learning-v1') || '{}'); } catch(e){}

  const backup = {
    version: "3.1.0",
    exportDate: new Date().toISOString(),
    system: "Tanveer Ashraf — Judicial Prep 2026–27",
    portal: state,
    arena: arenaData,
    bnsBookmarks: bnsBookmarks,
    learning: learningData
  };

  const b = new Blob([JSON.stringify(backup, null, 2)], { type: 'application/json' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(b);
  a.download = `tanveer-judicial-prep-backup-v3.1.0-${new Date().toISOString().slice(0,10)}.json`;
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
    const learningTopics = data.learning && data.learning.completedTopics ? Object.keys(data.learning.completedTopics).length : 0;
    const backupDate = data.exportDate ? new Date(data.exportDate).toLocaleString() : "Unknown date";

    const proceed = confirm(
      `Backup File Verified (v${data.version || '3.0.0'}):
• Export Date: ${backupDate}
• Test Results: ${testCount}
• Saved Questions: ${savedCount}
• Arena XP: ${xpCount}
• Academy Completed Topics: ${learningTopics}

Do you want to restore this data? (Existing records will be safely updated).`
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
    if (data.learning && typeof data.learning === 'object') {
      localStorage.setItem('tanveer-learning-v1', JSON.stringify(data.learning));
    }

    alert("Backup successfully restored! Study records, academy progress, and arena stats updated.");
    history();
  } catch(err) {
    alert("Error restoring backup: " + (err.message || "File could not be parsed."));
  }
}

function syllabus(){el.innerHTML=`<div class="eyebrow">Exam framework</div><h1>Syllabus & study resources</h1><p class="muted">Preliminary examination · based on the supplied syllabus</p><div class="card" style="margin-bottom: 24px; border: 2px solid #137d72; background: #edf7f4; padding: 20px 24px;"><div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;"><div><span class="badge" style="background: #142c46; color: #dfbf80; margin-bottom: 6px; display: inline-block;">STRUCTURED ACADEMY</span><h3 style="font-family: Georgia, serif; font-size: 19px; color: #142c46; margin: 0 0 6px;">Subject-wise Judicial Learning Academy</h3><p style="margin: 0; color: #334455; font-size: 13.5px;">All 30 UP PCS-J curriculum subjects structured systematically. Active module: <strong>The Constitution of India</strong> (15 Chapters, 45 Topics, 480 Practice MCQs, 158 Historical PYQs).</p></div><div style="display: flex; gap: 8px; flex-wrap: wrap;"><a href="learning-academy.html" class="btn primary" style="text-decoration: none;">🏛️ Open Academy Hub</a><a href="subject-study.html?subject=law-constitution" class="btn" style="background: #137d72; color: #fff; text-decoration: none; border-color: #137d72;">📖 Study Constitution</a></div></div></div><div class="grid syllabus-grid section"><div class="card"><div class="eyebrow">Paper I</div><h2>General Knowledge</h2><div class="big-mark">150 <small>marks · 2 hours</small></div><p>History of India and Indian culture; Indian geography; polity; current national issues; social relevance; Indian economy; international affairs and institutions; science, technology, communications and space.</p><h3>Social legislation</h3><ul><li>Rights of Persons with Disabilities Act, 2016</li><li>Maintenance and Welfare of Parents and Senior Citizens Act, 2007</li><li>Dowry Prohibition Act, 1961</li><li>Protection of Women from Domestic Violence Act, 2005</li><li>Sexual Harassment of Women at Workplace Act, 2013</li><li>PCPNDT Act, 1994</li><li>Medical Termination of Pregnancy Act, 1971</li><li>Indecent Representation of Women (Prohibition) Act, 1986</li><li>Protection of Children from Sexual Offences Act, 2012</li></ul>${btn('Study GK',"openNotes('all','GK')",'primary')}</div><div class="card"><div class="eyebrow">Paper II</div><h2>Law</h2><div class="big-mark">300 <small>marks · 2 hours</small></div><ul><li>Jurisprudence</li><li>International organisations and current international affairs</li><li>Indian Constitution</li><li>Transfer of Property Act</li><li>Indian Evidence Act, 1872 / Bharatiya Sakshya Adhiniyam, 2023</li><li>Indian Penal Code, 1860 / Bharatiya Nyaya Sanhita, 2023</li><li>Civil Procedure Code</li><li>Criminal Procedure Code, 1973 / Bharatiya Nagarik Suraksha Sanhita, 2023</li><li>Law of Contract</li></ul><p class="muted">Previous-year questions retain the statutes in use when the papers were held. Study the new criminal laws separately; the PYQ bank is not a complete current-law course.</p>${btn('Study Law',"openNotes('all','LAW')",'primary')} <a class="btn" href="bns.html">Study BNS sections</a></div></div><div class="card section"><h2>English PYQ notes</h2><p class="muted">Download the supplied chronological study edition, with previous-year answers and options.</p><div class="actions"><a class="btn primary" href="resources/english-pyq-notes.pdf" download>Download PDF notes</a><a class="btn" href="resources/english-pyq-notes.pdf" target="_blank" rel="noopener">Read PDF</a></div>${dataNotice()}</div>`}

function about(){el.innerHTML=`<div class="eyebrow">A personal initiative</div><h1>Built for the journey ahead.</h1><p class="muted">An independent, dedicated workspace for judicial services preparation.</p><div class="people-grid section"><article class="card person"><div class="person-image person-tanveer"><img src="assets/images/tanveer.webp" alt="Portrait of Tanveer Ashraf"></div><div class="person-body"><div class="eyebrow">Created for</div><h2>Tanveer Ashraf</h2><p>Personal learning and examination workspace for UP PCS-J. A focused environment to read, practise, review and measure progress.</p></div></article><article class="card person"><div class="person-image person-tauqeer"><img src="assets/images/tauqeer.webp" alt="Portrait of Tauqeer Ashraf"></div><div class="person-body"><div class="eyebrow">Designed & developed by</div><h2>Tauqeer Ashraf</h2><p>A personal preparation initiative built for his elder brother, bringing previous-year questions and exam practice together in one organised portal.</p></div></article></div><div class="card section"><h2>Our purpose</h2><p>Study consistently. Practise deliberately. Learn from every attempt.</p><p class="muted">This is a personal educational project, not an official UPPSC or UPSC website. The scales and courthouse mark are an original decorative emblem. Study progress and test results stay in your browser. No server account or cloud synchronisation is configured.</p></div>${dataNotice()}`}
const params=new URLSearchParams(location.search);
if(view==='notes'){for(let k of ['year','paper','topic','query'])if(params.has(k))filter[k]=params.get(k);filter.page=Math.max(1,Number(params.get('page'))||1);filter.answers=params.get('answers')!=='0'}
if(view==='practice'){for(let k of ['kind','year','paper','topic'])if(params.has(k))testConfig[k]=params.get(k);if(params.has('size'))testConfig.size=Number(params.get('size'))||10;for(let k of ['negative','timed'])if(params.has(k))testConfig[k]=params.get(k)==='true'}
if(view==='result')result=state.history.find(r=>String(r.id)===params.get('id'))||state.history[0]||null;
window.addEventListener('pageshow',e=>{if(e.persisted)location.reload()});go(view);

