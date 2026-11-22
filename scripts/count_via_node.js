const fs = require('fs');

global.window = {};

function loadScript(path) {
  const content = fs.readFileSync(path, 'utf8');
  eval(content);
}

// 1. Questions
loadScript('assets/data/questions.js');
const qs = window.PCSJ_QUESTIONS || [];
const eligible = qs.filter(q => q.eligible === true);
const ineligible = qs.filter(q => q.eligible === false);
console.log(`Historical PYQ records: ${qs.length}`);
console.log(`Scorable PYQ records (eligible: true): ${eligible.length}`);
console.log(`Review-only PYQ records (eligible: false): ${ineligible.length}`);

// 2. BNS
loadScript('assets/data/bns.js');
const bns = window.BNS_SECTIONS || [];
console.log(`BNS section records: ${bns.length}`);

// 3. Vocab
loadScript('assets/games/data/legal-vocabulary.js');
const vocab = window.ARENA_VOCABULARY || [];
console.log(`Legal Vocabulary entries: ${vocab.length}`);

// 4. Crosswords
loadScript('assets/games/data/crossword-puzzles.js');
const cw = window.ARENA_CROSSWORDS || [];
console.log(`Crossword puzzles: ${cw.length}`);

// 5. Detective cases
loadScript('assets/games/data/detective-cases.js');
const det = window.DETECTIVE_CASES || [];
console.log(`Detective cases: ${det.length}`);

// 6. Courtroom cases
loadScript('assets/games/data/courtroom-cases.js');
const crt = window.COURTROOM_CASES || [];
console.log(`Courtroom hearings: ${crt.length}`);

// 7. Myths
loadScript('assets/games/data/legal-myths.js');
const myths = window.ARENA_MYTHS || [];
console.log(`Myth Buster statements: ${myths.length}`);

// 8. Chapters
loadScript('assets/games/data/journey-chapters.js');
const ch = window.JOURNEY_CHAPTERS || [];
console.log(`Campaign chapters: ${ch.length}`);

// 9. Missions
loadScript('assets/games/data/journey-missions.js');
const m = window.JOURNEY_MISSIONS || [];
console.log(`Campaign missions: ${m.length}`);

// 10. Characters
loadScript('assets/games/data/characters.js');
const chars = window.ARENA_CHARACTERS ? Object.keys(window.ARENA_CHARACTERS) : [];
console.log(`Characters: ${chars.length}`);

// 11. Achievements
loadScript('assets/games/js/achievements.js');
const ach = (window.Achievements && window.Achievements.getAll) ? window.Achievements.getAll() : (window.ARENA_ACHIEVEMENTS || []);
console.log(`Achievements: ${ach.length}`);

// 12. Legacy game content (Memory Match cards)
loadScript('assets/games/data/legal-game-content.js');
const lgc = window.LEGAL_GAME_CONTENT || {};
const termsCount = lgc.legalTerms ? lgc.legalTerms.length : 0;
const maximsCount = lgc.maxims ? lgc.maxims.length : 0;
const sectionsCount = lgc.bnsSections ? lgc.bnsSections.length : 0;
const casesCount = lgc.landmarkCases ? lgc.landmarkCases.length : 0;
console.log(`Memory Match pairs (legal-game-content.js): Terms=${termsCount}, Maxims=${maximsCount}, Sections=${sectionsCount}, Cases=${casesCount}, Total Pairs=${termsCount + maximsCount + sectionsCount + casesCount}`);
