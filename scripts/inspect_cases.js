const fs = require('fs');
global.window = {};

eval(fs.readFileSync('assets/games/data/detective-cases.js', 'utf8'));
console.log('=== DETECTIVE CASES ===');
window.DETECTIVE_CASES.forEach((c, i) => {
  console.log(`DET #${i+1}: ${c.id} - ${c.title}`);
  console.log(`  Difficulty: ${c.difficulty}`);
  console.log(`  Correct Charge:`, c.correctCharge);
  console.log(`  Legal Verification:`, c.legalVerification);
});

eval(fs.readFileSync('assets/games/data/courtroom-cases.js', 'utf8'));
console.log('\n=== COURTROOM CASES ===');
window.COURTROOM_CASES.forEach((c, i) => {
  console.log(`COURT #${i+1}: ${c.id} - ${c.title}`);
  console.log(`  Difficulty: ${c.difficulty}`);
  console.log(`  Subject: ${c.subject}`);
  console.log(`  Legal Verification:`, c.legalVerification);
  console.log(`  Ruling:`, c.ruling ? c.ruling.decision : 'none');
});
