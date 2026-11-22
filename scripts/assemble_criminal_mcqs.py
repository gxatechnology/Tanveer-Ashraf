"""
Merges part1, part2, and part3 JSONs into assets/learning/data/criminal/criminal-mcqs.js
"""

import json

p1 = json.load(open("scripts/data_crim_mcqs_part1.json", encoding="utf-8"))
p2 = json.load(open("scripts/data_crim_mcqs_part2.json", encoding="utf-8"))
p3 = json.load(open("scripts/data_crim_mcqs_part3.json", encoding="utf-8"))

all_mcqs = p1 + p2 + p3
print(f"Total MCQs loaded: {len(all_mcqs)} (P1: {len(p1)}, P2: {len(p2)}, P3: {len(p3)})")

# Check for unique IDs
ids = set()
for q in all_mcqs:
    if q["id"] in ids:
        print(f"WARNING: duplicate ID {q['id']}")
    ids.add(q["id"])

print(f"Unique question IDs: {len(ids)}")

output_path = "assets/learning/data/criminal/criminal-mcqs.js"
with open(output_path, "w", encoding="utf-8") as f:
    f.write("/**\n")
    f.write(" * TANVEER ASHRAF JUDICIAL PREP — SUBJECT-WISE LEARNING ACADEMY\n")
    f.write(" * Criminal Law (BNS 2023 & IPC 1860) Practice MCQ Question Bank\n")
    f.write(f" * Total Verified Questions: {len(all_mcqs)}\n")
    f.write(" */\n\n")
    f.write("window.CRIMINAL_MCQS = ")
    json.dump(all_mcqs, f, indent=2, ensure_ascii=False)
    f.write(";\n")

print(f"Successfully wrote {len(all_mcqs)} questions to {output_path}")
