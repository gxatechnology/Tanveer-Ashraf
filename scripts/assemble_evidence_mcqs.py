"""
Assembles assets/learning/data/evidence/evidence-mcqs.js
from parts 1, 2, 3 (280 MCQs total).
"""

import json

part1 = json.load(open("scripts/data_evidence_mcqs_part1.json", encoding="utf-8"))
part2 = json.load(open("scripts/data_evidence_mcqs_part2.json", encoding="utf-8"))
part3 = json.load(open("scripts/data_evidence_mcqs_part3.json", encoding="utf-8"))

all_mcqs = part1 + part2 + part3
print(f"Loaded: Part 1 ({len(part1)}), Part 2 ({len(part2)}), Part 3 ({len(part3)}) -> Total: {len(all_mcqs)}")

# Verify uniqueness of IDs
ids = [m["id"] for m in all_mcqs]
if len(ids) != len(set(ids)):
    duplicates = [i for i in ids if ids.count(i) > 1]
    print("ERROR: Duplicate IDs found:", set(duplicates))
    exit(1)

# Check topic coverage
topics = set(m["topicId"] for m in all_mcqs)
print(f"Distinct topics covered: {len(topics)}")

# Assemble into JS file
js_content = "window.EVIDENCE_MCQS = " + json.dumps(all_mcqs, indent=2, ensure_ascii=False) + ";\n"
output_path = "assets/learning/data/evidence/evidence-mcqs.js"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully wrote {len(all_mcqs)} MCQs to {output_path}!")
