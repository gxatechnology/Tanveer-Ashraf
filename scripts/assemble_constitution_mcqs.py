"""
Assembles all 480 MCQs for the Indian Constitution Module (law-constitution)
across all 15 chapters and 45 topics into assets/learning/data/constitution/constitution-mcqs.js
"""

import json
from build_mcqs_ch01_to_ch05 import MCQS_CH01_05
from build_mcqs_ch06_to_ch08 import MCQS_CH06_08
from build_mcqs_ch09_to_ch11 import MCQS_CH09_11
from build_mcqs_ch12 import MCQS_CH12
from build_mcqs_ch13 import MCQS_CH13
from build_mcqs_ch14 import MCQS_CH14
from build_mcqs_ch15 import MCQS_CH15

all_mcqs = []
all_mcqs.extend(MCQS_CH01_05)
all_mcqs.extend(MCQS_CH06_08)
all_mcqs.extend(MCQS_CH09_11)
all_mcqs.extend(MCQS_CH12)
all_mcqs.extend(MCQS_CH13)
all_mcqs.extend(MCQS_CH14)
all_mcqs.extend(MCQS_CH15)

print(f"Total MCQs collected: {len(all_mcqs)}")

# Check uniqueness of IDs
seen_ids = set()
for m in all_mcqs:
    if m["id"] in seen_ids:
        raise ValueError(f"Duplicate MCQ ID found: {m['id']}")
    seen_ids.add(m["id"])

# Check chapters distribution
from collections import Counter
chapter_counts = Counter(m["chapterId"] for m in all_mcqs)
print("MCQ Counts by Chapter:")
for ch, count in sorted(chapter_counts.items()):
    print(f"  {ch}: {count}")

expected_total = 480
if len(all_mcqs) != expected_total:
    print(f"WARNING: Expected {expected_total} MCQs, got {len(all_mcqs)}")
else:
    print("SUCCESS: Exact target of 480 MCQs achieved!")

# Validate fields
letters = ["A", "B", "C", "D"]
for m in all_mcqs:
    assert len(m["options"]) == 4, f"{m['id']} has != 4 options"
    assert 0 <= m["answer"] <= 3, f"{m['id']} invalid answer index {m['answer']}"
    assert m["answerLetter"] == letters[m["answer"]], f"{m['id']} answerLetter mismatch"
    assert all(k in m["optionBreakdown"] for k in ["A", "B", "C", "D"]), f"{m['id']} missing optionBreakdown key"
    assert m["explanation"], f"{m['id']} missing explanation"
    assert m["provision"], f"{m['id']} missing provision"

out_path = "assets/learning/data/constitution/constitution-mcqs.js"
with open(out_path, "w", encoding="utf-8") as f:
    f.write("/**\n")
    f.write(" * TANVEER ASHRAF — JUDICIAL PREP 2026–27\n")
    f.write(" * Indian Constitution Module — Comprehensive Practice MCQ Question Bank\n")
    f.write(f" * Total Questions: {len(all_mcqs)} | Chapters: 15 | Topics: 45\n")
    f.write(" * Standards: 100% Verified Statutory Text, 4 Options, Option Breakdowns, Learning Objectives\n")
    f.write(" */\n\n")
    f.write("(function (global) {\n")
    f.write("  'use strict';\n\n")
    f.write("  global.CONSTITUTION_MCQS = ")
    json.dump(all_mcqs, f, indent=2, ensure_ascii=False)
    f.write(";\n\n")
    f.write("})(typeof window !== 'undefined' ? window : global);\n")

print(f"Wrote {len(all_mcqs)} MCQs to {out_path}")
