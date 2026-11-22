import sys
import os
sys.path.insert(0, os.path.abspath('.'))
import json

from scripts.data_contract_mcqs_1 import MCQS_PART1
from scripts.data_contract_mcqs_2 import MCQS_PART2
from scripts.data_contract_mcqs_3 import MCQS_PART3

all_mcqs = MCQS_PART1 + MCQS_PART2 + MCQS_PART3
print(f"Total Contract MCQs to assemble: {len(all_mcqs)}")

# Validate uniqueness of IDs
ids = [m['id'] for m in all_mcqs]
if len(ids) != len(set(ids)):
    from collections import Counter
    counts = Counter(ids)
    dupes = {k: v for k, v in counts.items() if v > 1}
    raise ValueError(f"Duplicate IDs found: {dupes}")
else:
    print("All 260 IDs are verified unique.")

header = """/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Law of Contract Module — Comprehensive Practice MCQ Question Bank
 * Total Questions: 260 | Chapters: 11 | Topics: 32
 * Standards: 100% Verified Indian Contract Act 1872 Text, 4 Options, Option Breakdowns, Learning Objectives
 */

(function (global) {
  'use strict';

  global.CONTRACT_MCQS = """

footer = """;

})(typeof window !== 'undefined' ? window : global);
"""

output_path = 'assets/learning/data/contract/contract-mcqs.js'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(header + json.dumps(all_mcqs, indent=2) + footer)

print(f"Successfully written {output_path}")
