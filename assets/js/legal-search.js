/* Local, English-first statutory index and PYQ search. No network needed to search. */
(function(){'use strict';
const S=window.BNS_SECTIONS,C=window.BNS_CHAPTERS,Q=window.PCSJ_QUESTIONS.filter(q=>q.text),$=id=>document.getElementById(id),pdf='https://www.indiacode.nic.in/bitstream/123456789/20062/1/a2023-45.pdf';
const esc=x=>String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const norm=x=>String(x??'').normalize('NFKD').toLowerCase().replace(/[’‘]/g,"'").replace(/\bindian penal code\b/g,'ipc').replace(/\bcode of criminal procedure\b|\bcriminal procedure code\b/g,'crpc').replace(/\bcode of civil procedure\b|\bcivil procedure code\b/g,'cpc').replace(/\bbharatiya nyaya sanhita\b/g,'bns').replace(/\b(?:sections?|secs?)\b\.?\s*/g,'sec ').replace(/\b(?:articles?|arts?)\b\.?\s*/g,'art ').replace(/\b(?:organised|organized)\b/g,'organized').replace(/\bdefence\b/g,'defense').replace(/[^a-z0-9\s]/g,' ').replace(/\s+/g,' ').trim();
const words=x=>norm(x).split(' ').filter(Boolean);const has=(h,t)=>/^\d+$/.test(t)?new RegExp('(?:^| )'+t+'(?: |$)').test(h):h.includes(t);
const all=(hay,query)=>words(query).every(w=>has(hay,w));
const direct=query=>String(query??'').trim().match(/^(?:(?:bns|bharatiya nyaya sanhita)\s*[-:]?\s*)?(?:(?:section|sec\.?|s\.?|§)\s*)?(\d{1,3})(?:\s*\(\s*\w+\s*\))*\.?$/i);
function matchBNS(s,q){if(!q.trim())return true;let d=direct(q);if(d)return s.section===Number(d[1]);let v=q.replace(/^\s*(?:bns|bharatiya nyaya sanhita)\s*[-:]?\s*/i,'');if(!v.trim())return true;return all(norm('section '+s.section+' '+s.title+' '+s.keywords+' '+C[s.chapter-1].title),v);}
const indexes=new Map(Q.map(q=>[q.id,norm([q.text,q.stem,...(q.options||[]),q.topic,q.year,q.answer].join(' '))]));
function matchPYQ(q,query){if(!String(query||'').trim())return true;const h=indexes.get(q.id)||norm(q.text);const raw=String(query).trim();if(/^bns\b/i.test(raw)||/^bharatiya nyaya sanhita\b/i.test(raw)){if(!/\bBNS\b|Bharatiya Nyaya Sanhita/i.test(q.text))return false;}
return all(h,raw);}
let bookmarked=[];try{bookmarked=JSON.parse(localStorage.getItem('tanveer-bns-bookmarks-v1')||'[]');if(!Array.isArray(bookmarked))bookmarked=[];}catch(e){};
const persist=()=>{try{localStorage.setItem('tanveer-bns-bookmarks-v1',JSON.stringify(bookmarked))}catch(e){}};
const chapterOptions=()=>'<option value="all">All 20 chapters</option>'+C.map(c=>`<option value="${c.id}">${c.id}. ${esc(c.title)} (${c.first}–${c.last})</option>`).join('');
function sectionCard(s){const ch=C[s.chapter-1];return `<article class="card bns-card" id="bns-${s.section}"><div class="bns-number">§ ${s.section}</div><div class="bns-main"><div class="caption">Chapter ${ch.id} · ${esc(ch.title)}</div><h3>${esc(s.title)}</h3>${s.section===106?'<p class="caption">Commencement note: the notification of 23 February 2024 excluded subsection (2) from the 1 July 2024 commencement. Check subsequent Gazette notices.</p>':''}<div class="toolbar"><a class="btn mini primary" href="https://indiacode.ecourtsindia.com/bns/section/${s.section}/" target="_blank" rel="noopener">Read full section ↗</a><a class="btn mini" href="${pdf}" target="_blank" rel="noopener">Official Act PDF ↗</a><button class="btn mini bns-save" data-save="${s.section}" aria-pressed="${bookmarked.includes(s.section)}">${bookmarked.includes(s.section)?'★ Saved':'☆ Save'}</button><a class="btn mini" href="library.html?paper=LAW&query=${encodeURIComponent(s.title.replace(/^(Punishment for |Voluntarily causing )/i,'').replace(/,.*$/,'').replace(/\.$/,''))}">Search related PYQs</a></div></div></article>`}
function bindSave(root){root.querySelectorAll('[data-save]').forEach(b=>b.onclick=()=>{const n=Number(b.dataset.save);bookmarked=bookmarked.includes(n)?bookmarked.filter(x=>x!==n):[...bookmarked,n];persist();b.textContent=bookmarked.includes(n)?'★ Saved':'☆ Save';b.setAttribute('aria-pressed',String(bookmarked.includes(n)));if($('bnsSaved')?.checked)drawBns();});}
let bnsPage=1;
function renderBNS(root){root.innerHTML=`<section class="hero law-hero"><div class="eyebrow">Current criminal law · English edition</div><h1>Bharatiya Nyaya Sanhita, 2023</h1><p>Explore every section by number, title or keyword. Keep your statutory revision separate from the historical IPC question bank.</p><div class="law-metrics"><span><b>358</b> sections</span><span><b>20</b> chapters</span><span>Act 45 of 2023</span></div><div class="actions"><a class="btn gold" href="${pdf}" target="_blank" rel="noopener">Open official full Bare Act ↗</a><a class="btn ghost" href="#bnsPractice">Take BNS recall test ↓</a><a class="btn ghost" href="https://www.ncrb.mha.gov.in/uploads/SankalanPortal/Index.html" target="_blank" rel="noopener">New criminal laws portal ↗</a></div></section><section class="card section"><div class="filter"><div class="field" style="flex:2"><label for="bnsQuery">Find a section or offence</label><input type="search" id="bnsQuery" placeholder="103, BNS 303, murd, criminal conspiracy…" autocomplete="off"></div><div class="field"><label for="bnsChapter">Chapter</label><select id="bnsChapter">${chapterOptions()}</select></div></div><div class="toolbar section"><button class="btn mini" data-example="103">Section 103</button><button class="btn mini" data-example="theft">Theft</button><button class="btn mini" data-example="cheat">Cheating</button><button class="btn mini" data-example="organised crime">Organised crime</button><label class="check"><input type="checkbox" id="bnsSaved"> Saved only</label><button class="btn mini" id="bnsClear">Clear</button></div></section><div class="notice">Section titles and selected search aliases are stored locally. Full statutory provisions, explanations, illustrations and provisos open in external references. This is an index, not a full offline reproduction of the Act. Read the latest official law and notifications for amendments.</div><div id="bnsCount" class="row section" aria-live="polite"></div><div id="bnsList"></div><div id="bnsPagination" class="toolbar section"></div><section id="bnsPractice" class="card section"><h2>Section number recall test</h2><p class="muted">New study exercises based on the BNS section headings, not previous-year examination questions.</p><div class="filter"><div class="field"><label for="recallSize">Questions</label><select id="recallSize"><option>10</option><option>20</option><option>25</option></select></div><div class="field"><label for="recallChapter">Chapter</label><select id="recallChapter">${chapterOptions()}</select></div></div><div class="actions"><button class="btn primary" id="recallStart">Start BNS practice</button></div><div id="recallBox"></div></section><p class="caption section">Section arrangement: <a href="${pdf}" target="_blank" rel="noopener">India Code, Act 45 of 2023</a>. Full section reader links point to an independent reproduction; consult India Code for authoritative text.</p>`;
$('bnsQuery').value=new URLSearchParams(location.search).get('q')||'';bnsPage=1;['bnsQuery','bnsChapter','bnsSaved'].forEach(id=>$(id).addEventListener(id==='bnsQuery'?'input':'change',()=>{bnsPage=1;drawBns()}));root.querySelectorAll('[data-example]').forEach(b=>b.onclick=()=>{$('bnsQuery').value=b.dataset.example;$('bnsChapter').value='all';$('bnsSaved').checked=false;bnsPage=1;drawBns()});$('bnsClear').onclick=()=>{$('bnsQuery').value='';$('bnsChapter').value='all';$('bnsSaved').checked=false;bnsPage=1;drawBns()};$('recallStart').onclick=startRecall;drawBns();}
function drawBns(){let query=$('bnsQuery').value,chap=$('bnsChapter').value,only=$('bnsSaved').checked,a=S.filter(s=>(chap==='all'||s.chapter==chap)&&(!only||bookmarked.includes(s.section))&&matchBNS(s,query));const pages=Math.max(1,Math.ceil(a.length/24));bnsPage=Math.min(bnsPage,pages);$('bnsCount').textContent=`${a.length} matching sections · Page ${bnsPage} of ${pages}`;$('bnsList').innerHTML=a.slice((bnsPage-1)*24,bnsPage*24).map(sectionCard).join('')||'<div class="empty card">No matching section. Try a shorter English word or a number from 1 to 358.</div>';bindSave($('bnsList'));$('bnsPagination').innerHTML=`<button class="btn mini" id="bnsPrev" ${bnsPage===1?'disabled':''}>Previous</button><span class="caption">${bnsPage} / ${pages}</span><button class="btn mini" id="bnsNext" ${bnsPage===pages?'disabled':''}>Next</button>`;$('bnsPrev').onclick=()=>{bnsPage--;drawBns();$('bnsCount').scrollIntoView({block:'start'})};$('bnsNext').onclick=()=>{bnsPage++;drawBns();$('bnsCount').scrollIntoView({block:'start'})};}
let smartDebounce = null;
function matchVocab(v, q) {
  if (!q.trim()) return false;
  const nq = norm(q);
  const text = norm([v.canonical, ...(v.acceptedVariants || []), v.subject, v.definition, v.primaryClue, v.statuteOrAuthority].join(' '));
  return words(nq).every(w => text.includes(w));
}

function matchMyth(m, q) {
  if (!q.trim()) return false;
  const nq = norm(q);
  const text = norm([m.statement, m.subject, m.legislation, m.section, m.explanation, m.misconceptionExplanation, ...(m.revisionKeywords || [])].join(' '));
  return words(nq).every(w => text.includes(w));
}

function renderSearch(root){
  root.innerHTML = `
    <div class="eyebrow">Unified Multi-Corpus Legal Search</div>
    <h1>Smart Legal Search</h1>
    <p class="muted">Search across BNS section headings, previous-year questions, verified legal vocabulary, and statutory truth propositions. Fast, client-side, and completely offline.</p>
    <div class="card section">
      <div class="field">
        <label for="smartQuery">Search legal corpus</label>
        <input id="smartQuery" type="search" placeholder="Try BNS 103, murd, res judicata, IPC 330, Art. 21, Habeas Corpus..." autocomplete="off">
      </div>
      <div class="toolbar section" style="gap:8px; margin-top:10px;">
        <button class="btn mini" data-example="BNS 103">BNS 103</button>
        <button class="btn mini" data-example="murd">murd</button>
        <button class="btn mini" data-example="res judicata">res judicata</button>
        <button class="btn mini" data-example="IPC 330">IPC 330</button>
        <button class="btn mini" data-example="Article 21">Article 21</button>
        <button class="btn mini" data-example="Habeas Corpus">Habeas Corpus</button>
      </div>
    </div>
    <div id="smartResults" aria-live="polite"></div>
  `;
  let i = $('smartQuery');
  i.value = new URLSearchParams(location.search).get('q') || '';
  i.oninput = () => {
    clearTimeout(smartDebounce);
    smartDebounce = setTimeout(drawSmart, 200);
  };
  root.querySelectorAll('[data-example]').forEach(b => b.onclick = () => {
    i.value = b.dataset.example;
    drawSmart();
  });
  drawSmart();
}

function drawSmart(){
  const q = $('smartQuery').value.trim();
  if (!q) {
    $('smartResults').innerHTML = `
      <div class="card section">
        <h3>Search Across 4 Legal Knowledge Bases</h3>
        <p class="muted">Enter keywords, section numbers, or legal principles. Searches run simultaneously across: (1) BNS 358 Sections, (2) Historical PYQs (2012–2023), (3) 285 Legal Terms & Maxims, and (4) 330 Statutory Propositions.</p>
        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:12px; font-size:0.85rem; color:#607387; margin-top:12px;">
          <strong>Notice on Statutory Search:</strong> BNS results display section headings and keywords. Access full verbatim bare act texts via official India Code links provided on each card.
        </div>
      </div>
    `;
    return;
  }

  const b = S.filter(x => matchBNS(x, q));
  const p = Q.filter(x => matchPYQ(x, q));
  const vList = window.ARENA_VOCABULARY ? window.ARENA_VOCABULARY.filter(x => matchVocab(x, q)) : [];
  const mList = window.ARENA_MYTHS ? window.ARENA_MYTHS.filter(x => matchMyth(x, q)) : [];

  let html = '';

  // 1. BNS Section Headings
  html += `
    <div class="row section">
      <h2>BNS 2023 Section Headings (${b.length})</h2>
      <a href="bns.html?q=${encodeURIComponent(q)}">View in BNS Reader →</a>
    </div>
    <div id="smartBns">${b.slice(0, 6).map(sectionCard).join('') || '<div class="card muted">No matching BNS section headings.</div>'}</div>
  `;

  // 2. Previous-Year Questions
  html += `
    <div class="row section" style="margin-top:24px;">
      <h2>Historical Previous-Year Questions (${p.length})</h2>
      <a href="library.html?query=${encodeURIComponent(q)}">View all in PYQ Library →</a>
    </div>
    ${p.slice(0, 8).map(x => `
      <article class="card qcard">
        <div class="qmeta"><span>${x.year} · ${x.paper==='GK'?'General Knowledge':'Law'} · Q${x.no}</span><span class="tag">${esc(x.topic)}</span></div>
        <p class="qstem">${esc(x.stem||x.text)}</p>
        <div class="options">${(x.options||[]).map((o,i)=>o?`<div class="opt"><b>(${String.fromCharCode(65+i)})</b> <span>${esc(o)}</span></div>`:'').join('')}</div>
        <p class="answer">Practice key: <b>${x.answer?esc(x.answer):'Not available'}</b></p>
        <a href="library.html?year=${x.year}&paper=${x.paper}&query=${encodeURIComponent(q)}" class="caption" style="color:var(--teal, #137d72);">Open matching questions in library →</a>
      </article>
    `).join('') || '<div class="card muted">No matching historical PYQs.</div>'}
  `;

  // 3. Legal Vocabulary & Maxims
  if (vList.length > 0) {
    html += `
      <div class="row section" style="margin-top:24px;">
        <h2>Legal Vocabulary & Maxims (${vList.length})</h2>
      </div>
      <div class="grid">
        ${vList.slice(0, 6).map(v => `
          <div class="card" style="border-left:4px solid var(--gold, #dfbf80);">
            <div class="row"><span class="badge" style="background:#f4f3ef; color:#142c46;">${esc(v.subject)}</span><span class="caption">${esc(v.difficulty)}</span></div>
            <h3 style="margin:6px 0; color:#142c46;">${esc(v.canonical)}</h3>
            <p style="font-size:0.9rem; margin:0 0 8px; color:#2d3748;">${esc(v.definition)}</p>
            <div class="caption"><strong>Authority:</strong> ${esc(v.statuteOrAuthority)}</div>
            ${v.sourceUrl ? `<a href="${esc(v.sourceUrl)}" target="_blank" rel="noopener" style="font-size:0.75rem; color:#137d72; display:inline-block; margin-top:4px;">Official India Code Link ↗</a>` : ''}
          </div>
        `).join('')}
      </div>
    `;
  }

  // 4. Statutory Truth Propositions
  if (mList.length > 0) {
    html += `
      <div class="row section" style="margin-top:24px;">
        <h2>Statutory Propositions & Misconceptions (${mList.length})</h2>
      </div>
      <div class="grid">
        ${mList.slice(0, 6).map(m => `
          <div class="card" style="border-left:4px solid ${m.classification==='true'?'#137d72':m.classification==='false'?'#a63b49':'#b98a38'};">
            <div class="row">
              <span class="badge" style="background:${m.classification==='true'?'#edf7f4':m.classification==='false'?'#fef2f2':'#fdf6e7'}; color:${m.classification==='true'?'#137d72':m.classification==='false'?'#a63b49':'#b98a38'}; text-transform:uppercase; font-weight:700;">
                ${m.classification}
              </span>
              <span class="tag">${esc(m.subject)}</span>
            </div>
            <p style="font-weight:600; color:#142c46; margin:8px 0;">"${esc(m.statement)}"</p>
            <p style="font-size:0.88rem; color:#475569; margin:0 0 6px;"><strong>Statutory Analysis:</strong> ${esc(m.explanation)}</p>
            <div class="caption"><strong>Section:</strong> ${esc(m.legislation)} • ${esc(m.section)}</div>
          </div>
        `).join('')}
      </div>
    `;
  }

  $('smartResults').innerHTML = html;
  bindSave($('smartBns'));
}
function shuffle(a){a=[...a];for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a;}
let recall=[];
function startRecall(){let c=$('recallChapter').value,n=Number($('recallSize').value),pool=S.filter(s=>c==='all'||s.chapter==c);recall=shuffle(pool).slice(0,n).map(s=>({s,options:shuffle([s.section,...shuffle(S.filter(x=>x.section!==s.section)).slice(0,3).map(x=>x.section)])}));$('recallBox').innerHTML=`<div class="notice">${recall.length} questions · 1 point per correct response. Section-heading recall only.</div><form id="recallForm">${recall.map((x,i)=>`<fieldset class="card recall-q"><legend>Q${i+1}. Which BNS section covers “${esc(x.s.title)}”?</legend>${x.options.map(o=>`<label class="recall-option"><input type="radio" name="r${i}" value="${o}"> Section ${o}</label>`).join('')}<div id="feedback${i}"></div></fieldset>`).join('')}<button class="btn primary" type="submit">Submit recall test</button></form><div id="recallResult" aria-live="polite"></div>`;$('recallForm').onsubmit=e=>{e.preventDefault();const data=new FormData(e.target);let correct=0,wrong=0,skip=0;recall.forEach((x,i)=>{let a=data.get('r'+i);if(a===null)skip++;else if(+a===x.s.section)correct++;else wrong++;$('feedback'+i).innerHTML=`<div class="answer">${a!==null&&+a===x.s.section?'Correct':'Answer'}: Section ${x.s.section} — ${esc(x.s.title)}</div>`;});e.target.querySelectorAll('input,button').forEach(x=>x.disabled=true);$('recallResult').innerHTML=`<div class="card section"><h2>Recall result: ${correct} / ${recall.length}</h2><p>Correct: ${correct} · Incorrect: ${wrong} · Unattempted: ${skip}</p><p class="caption">Separate practice result; not counted in the original PYQ test history.</p></div>`;$('recallResult').scrollIntoView({block:'nearest'})};}
window.LegalSearch={matchPYQ,matchBNS,renderBNS,renderSearch};
})();
