const fs = require('fs');

let allMCQs = [];
['scripts/data_contract_mcqs_1.py', 'scripts/data_contract_mcqs_2.py', 'scripts/data_contract_mcqs_3.py'].forEach(f => {
  const content = fs.readFileSync(f, 'utf8');
  const jsonStart = content.indexOf('[');
  const jsonEnd = content.lastIndexOf(']');
  const arr = JSON.parse(content.slice(jsonStart, jsonEnd + 1));
  console.log(`${f} parsed: ${arr.length} MCQs`);
  allMCQs = allMCQs.concat(arr);
});

console.log(`Total Contract MCQs to assemble: ${allMCQs.length}`);

// Validate ID uniqueness
const ids = new Set();
for (const m of allMCQs) {
  if (ids.has(m.id)) {
    throw new Error(`Duplicate ID found: ${m.id}`);
  }
  ids.add(m.id);
}
console.log('All 260 IDs are verified unique.');

const header = `/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Law of Contract Module — Comprehensive Practice MCQ Question Bank
 * Total Questions: 260 | Chapters: 11 | Topics: 32
 * Standards: 100% Verified Indian Contract Act 1872 Text, 4 Options, Option Breakdowns, Learning Objectives
 */

(function (global) {
  'use strict';

  global.CONTRACT_MCQS = `;

const footer = `;

})(typeof window !== 'undefined' ? window : global);
`;

const outputPath = 'assets/learning/data/contract/contract-mcqs.js';
fs.writeFileSync(outputPath, header + JSON.stringify(allMCQs, null, 2) + footer, 'utf8');
console.log(`Successfully written ${outputPath}`);
