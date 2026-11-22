const fs = require('fs');
global.window = {};

eval(fs.readFileSync('assets/games/data/journey-chapters.js', 'utf8'));
eval(fs.readFileSync('assets/games/data/journey-missions.js', 'utf8'));

console.log('=== CAMPAIGN CHAPTERS ===');
window.JOURNEY_CHAPTERS.forEach(ch => {
  console.log(`${ch.id}: ${ch.title} (Mentor: ${ch.mentor})`);
});

console.log('\n=== MISSIONS PER CHAPTER ===');
const mByCh = {};
window.JOURNEY_MISSIONS.forEach(m => {
  if (!mByCh[m.chapterId]) mByCh[m.chapterId] = [];
  mByCh[m.chapterId].push(m);
});

Object.keys(mByCh).forEach(chId => {
  console.log(`\nChapter ${chId} (${mByCh[chId].length} missions):`);
  mByCh[chId].forEach(m => {
    console.log(`  - ${m.id}: ${m.title} -> URL: ${m.gameUrl} | Target: ${m.targetScore} (acc: ${m.targetAccuracy}%)`);
  });
});
