const fs = require('fs');
const path = require('path');
const vm = require('vm');

// Mock window and browser environment
const domMock = {
  location: { pathname: '/subject-study.html', search: '?subject=law-criminal' },
  document: {
    addEventListener: () => {},
    getElementById: () => null,
    querySelector: () => null,
    querySelectorAll: () => [],
    createElement: () => ({ setAttribute: () => {}, appendChild: () => {}, classList: { add: () => {}, remove: () => {} } }),
    body: { appendChild: () => {}, classList: { add: () => {}, remove: () => {} } }
  }
};

const sandbox = {
  window: domMock,
  document: domMock.document,
  location: domMock.location,
  console: console,
  URLSearchParams: URLSearchParams
};
vm.createContext(sandbox);

// Load all subjects and curriculum files
function loadScript(filePath) {
  const code = fs.readFileSync(filePath, 'utf8');
  vm.runInContext(code, sandbox);
}

loadScript('assets/data/questions.js');
loadScript('assets/data/bns.js');
loadScript('assets/learning/data/subjects.js');

// Load curriculum files for all 30 active subjects
const curriculumDirs = [
  'constitution', 'jurisprudence', 'contract', 'tpa',
  'criminal', 'crpc', 'evidence', 'cpc', 'social',
  'history', 'culture', 'geography', 'polity', 'economy',
  'current', 'social-issues', 'international', 'science',
  'tech', 'comm', 'space', 'international-law'
];

curriculumDirs.forEach(dir => {
  const dirPath = path.join('assets/learning/data', dir);
  if (fs.existsSync(dirPath)) {
    fs.readdirSync(dirPath).forEach(file => {
      if (file.endsWith('.js')) {
        loadScript(path.join(dirPath, file));
      }
    });
  }
});

loadScript('assets/learning/js/learning-storage.js');
loadScript('assets/learning/js/learning-engine.js');

const LearningEngine = sandbox.window.LearningEngine;
console.log('Testing Curriculum & Drawer Navigation for all 30 Active Subjects...');

const activeSubjectIds = [
  'law-constitution', 'law-jurisprudence', 'law-contract', 'law-tpa',
  'law-criminal', 'law-crpc', 'law-evidence', 'law-cpc', 'law-international',
  'soc-disabilities', 'soc-parents', 'soc-dowry', 'soc-domestic-violence',
  'soc-posh', 'soc-pcpndt', 'soc-mtp', 'soc-indecent-rep', 'soc-pocso',
  'gk-history', 'gk-culture', 'gk-geography', 'gk-polity', 'gk-economy',
  'gk-current', 'gk-social', 'gk-international', 'gk-science',
  'gk-tech', 'gk-comm', 'gk-space'
];

let totalPass = 0;
let totalFail = 0;

activeSubjectIds.forEach(subId => {
  const sub = LearningEngine.getSubjectById(subId);
  if (!sub) {
    console.error(`[FAIL] Subject ${subId} not found in registry`);
    totalFail++;
    return;
  }

  const chapters = LearningEngine.getChaptersBySubject(subId);
  if (!chapters || chapters.length === 0) {
    console.error(`[FAIL] No chapters found for ${subId}`);
    totalFail++;
    return;
  }

  let totalTopics = 0;
  chapters.forEach(ch => {
    const topics = LearningEngine.getTopicsByChapter(ch.id, subId);
    totalTopics += topics.length;
  });

  if (chapters.length !== sub.chaptersCount || totalTopics !== sub.topicsCount) {
    console.error(`[FAIL] ${subId}: Expected ${sub.chaptersCount} ch / ${sub.topicsCount} top, got ${chapters.length} ch / ${totalTopics} top`);
    totalFail++;
  } else {
    console.log(`[PASS] ${subId.padEnd(24)} -> ${chapters.length} chapters, ${totalTopics} topics verified`);
    totalPass++;
  }
});

console.log(`\nCurriculum Drawer Verification: ${totalPass} PASSED, ${totalFail} FAILED (30/30)`);
if (totalFail > 0) process.exit(1);
