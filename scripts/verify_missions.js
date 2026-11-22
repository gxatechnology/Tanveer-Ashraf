const fs = require('fs');
global.window = {};

eval(fs.readFileSync('assets/games/data/journey-missions.js', 'utf8'));

console.log(`Checking all ${window.JOURNEY_MISSIONS.length} missions for valid parameters...`);

let issues = 0;
window.JOURNEY_MISSIONS.forEach(m => {
  const url = m.gameUrl;
  const [page, query] = url.split('?');
  
  // 1. Check if page exists on disk
  if (!fs.existsSync(page)) {
    console.log(`ERROR in ${m.id}: Page ${page} does not exist!`);
    issues++;
  }

  // 2. Parse query
  const params = new URLSearchParams(query || '');
  if (!params.get('missionId')) {
    console.log(`WARNING in ${m.id}: Missing missionId in query: ${url}`);
    issues++;
  }
});

if (issues === 0) {
  console.log("All 36 missions have verified target pages and valid parameters!");
} else {
  console.log(`Found ${issues} issues.`);
}
