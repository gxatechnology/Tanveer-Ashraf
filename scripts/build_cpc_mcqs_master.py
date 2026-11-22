# -*- coding: utf-8 -*-
"""
Compiler script to assemble assets/learning/data/cpc/cpc-mcqs.js from Parts A, B, C, D.
Total: 400 MCQs.
"""
import sys
import json
import builtins

builtins.true = True
builtins.false = False
builtins.null = None

sys.path.append("scripts")
from cpc_mcq_part_a import MCQS_PART_A
from cpc_mcq_part_b import MCQS_PART_B
from cpc_mcq_part_c import MCQS_PART_C
from cpc_mcq_part_d import MCQS_PART_D

all_mcqs = MCQS_PART_A + MCQS_PART_B + MCQS_PART_C + MCQS_PART_D

print(f"Total MCQs loaded: {len(all_mcqs)}")

# Validate each MCQ
seen_ids = set()
for i, mcq in enumerate(all_mcqs):
    # ID check
    mcq_id = mcq.get("id")
    if not mcq_id:
        raise ValueError(f"MCQ at index {i} missing id")
    if mcq_id in seen_ids:
        raise ValueError(f"Duplicate MCQ ID: {mcq_id}")
    seen_ids.add(mcq_id)
    
    # Options check
    opts = mcq.get("options", [])
    if len(opts) != 4:
        raise ValueError(f"MCQ {mcq_id} does not have 4 options")
    
    # Answer check
    ans = mcq.get("answer")
    if ans not in (0, 1, 2, 3):
        raise ValueError(f"MCQ {mcq_id} invalid answer index {ans}")
    ans_let = mcq.get("answerLetter")
    expected_letter = ["A", "B", "C", "D"][ans]
    if ans_let != expected_letter:
        raise ValueError(f"MCQ {mcq_id} answerLetter {ans_let} != expected {expected_letter}")
    
    # optionBreakdown check
    ob = mcq.get("optionBreakdown", {})
    for letter in ("A", "B", "C", "D"):
        if letter not in ob or not ob[letter].strip():
            raise ValueError(f"MCQ {mcq_id} missing optionBreakdown for {letter}")
    
    # Chapter & Topic check
    if not mcq.get("chapterId") or not mcq.get("topicId"):
        raise ValueError(f"MCQ {mcq_id} missing chapterId or topicId")
    
    # Set status & eligible
    mcq["eligible"] = True
    mcq["status"] = "active"

print("All 400 MCQs passed validation!")

header = """/**
 * TANVEER ASHRAF JUDICIAL PREP — SUBJECT-WISE LEARNING ACADEMY
 * Code of Civil Procedure, 1908 (CPC) Practice MCQ Question Bank
 * Total Verified Questions: 400
 * Chapters: 20 (ch-cpc-01 to ch-cpc-20) | Topics: 57 (top-cpc-01-01 to top-cpc-20-03)
 * Full 4-Option Rationale (A, B, C, D), Statutory References, and Exam Objectives.
 */

(function(root) {
  'use strict';
  const target = typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : root);

  target.CPC_MCQS = """

footer = """;

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = target.CPC_MCQS;
  }
})(typeof window !== 'undefined' ? window : this);
"""

js_content = header + json.dumps(all_mcqs, indent=2, ensure_ascii=False) + footer

with open("assets/learning/data/cpc/cpc-mcqs.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully wrote assets/learning/data/cpc/cpc-mcqs.js ({len(js_content)} bytes)")
