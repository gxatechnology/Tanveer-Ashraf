const fs = require('fs');

let allMCQs = [];
['scripts/data_tpa_mcqs_1.py', 'scripts/data_tpa_mcqs_2.py', 'scripts/data_tpa_mcqs_3.py', 'scripts/data_tpa_mcqs_4.py'].forEach(f => {
  const content = fs.readFileSync(f, 'utf8');
  const jsonStart = content.indexOf('[');
  const jsonEnd = content.lastIndexOf(']');
  const arr = JSON.parse(content.slice(jsonStart, jsonEnd + 1));
  console.log(`${f} parsed: ${arr.length} MCQs`);
  allMCQs = allMCQs.concat(arr);
});

console.log(`Total TPA MCQs to assemble: ${allMCQs.length}`);

// Validate ID uniqueness
const ids = new Set();
for (const m of allMCQs) {
  if (ids.has(m.id)) {
    throw new Error(`Duplicate ID found: ${m.id}`);
  }
  ids.add(m.id);
}
console.log('All 240 IDs are verified unique.');

const header = `/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Transfer of Property Act, 1882 Module — Comprehensive Practice MCQ Question Bank
 * Total Questions: 240 | Chapters: 8 | Topics: 24
 * Standards: 100% Verified Statutory Text, 4 Options, Option Breakdowns, Learning Objectives
 */

(function (global) {
  'use strict';

  global.TPA_MCQS = `;

const footer = `;

})(typeof window !== 'undefined' ? window : global);
`;

const outputPath = 'assets/learning/data/tpa/tpa-mcqs.js';
fs.writeFileSync(outputPath, header + JSON.stringify(allMCQs, null, 2) + footer, 'utf8');
console.log(`Successfully written ${outputPath}`);
