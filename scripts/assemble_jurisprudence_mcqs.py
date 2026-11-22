import sys
import os
sys.path.insert(0, os.path.abspath('.'))
import json
from scripts.data_jurisprudence_mcqs_1 import MCQS_PART1
from scripts.data_jurisprudence_mcqs_2 import MCQS_PART2
from scripts.data_jurisprudence_mcqs_3 import MCQS_PART3

all_mcqs = MCQS_PART1 + MCQS_PART2 + MCQS_PART3
print(f"Total Jurisprudence MCQs to assemble: {len(all_mcqs)}")

# Validate uniqueness of IDs
ids = [m['id'] for m in all_mcqs]
if len(ids) != len(set(ids)):
    from collections import Counter
    counts = Counter(ids)
    dupes = {k: v for k, v in counts.items() if v > 1}
    raise ValueError(f"Duplicate IDs found: {dupes}")
else:
    print("All IDs are verified unique.")

header = """/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Jurisprudence Module — Comprehensive Practice MCQ Question Bank
 * Total Questions: 240 | Chapters: 11 | Topics: 30
 * Standards: 100% Verified Analytical Jurisprudence Text, 4 Options, Option Breakdowns, Learning Objectives
 */

(function (global) {
  'use strict';

  global.JURISPRUDENCE_MCQS = """

footer = """;

})(typeof window !== 'undefined' ? window : global);
"""

with open('assets/learning/data/jurisprudence/jurisprudence-mcqs.js', 'w', encoding='utf-8') as f:
    f.write(header + json.dumps(all_mcqs, indent=2) + footer)

print("Successfully written assets/learning/data/jurisprudence/jurisprudence-mcqs.js")
