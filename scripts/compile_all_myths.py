# Compiler for assets/games/data/legal-myths.js
import json
import os
import sys

# Add scripts directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_myths_part1 import get_part1_items
from data_myths_part2 import get_part2_items
from data_myths_part3 import get_part3_items

items = []
c_id = 1

def m(statement, classification, subject, difficulty, legislation, section, subsection, explanation, misconception, exceptions, error_phrase, correction, url, legal_date, keywords, old_vs_new=None):
    global c_id
    if classification == "false":
        if not error_phrase:
            raise ValueError(f"Item #{c_id} is marked 'false' but has no error_phrase: {statement}")
        if error_phrase not in statement:
            raise ValueError(f"Item #{c_id} error_phrase '{error_phrase}' NOT found in statement:\n'{statement}'")
        if not correction:
            raise ValueError(f"Item #{c_id} is marked 'false' but has no correction: {statement}")
    elif classification == "true":
        error_phrase = None
        correction = None
    
    items.append({
        "id": f"myth-{c_id:03d}",
        "statement": statement,
        "classification": classification,
        "subject": subject,
        "difficulty": difficulty,
        "legislation": legislation,
        "section": section,
        "subsection": subsection,
        "explanation": explanation,
        "misconceptionExplanation": misconception,
        "exceptions": exceptions,
        "errorPhrase": error_phrase,
        "correction": correction,
        "sourceUrl": url,
        "verificationDate": "2026-11-22",
        "applicableLegalDate": legal_date,
        "revisionKeywords": keywords,
        "oldVsNew": old_vs_new
    })
    c_id += 1

print("Loading Part 1 items...")
get_part1_items(m)

print("Loading Part 2 items...")
get_part2_items(m)

print("Loading Part 3 items...")
get_part3_items(m)

total = len(items)
print(f"Total items registered: {total}")

# Verify metrics
subjects = {}
classifications = {}
difficulties = {}
with_old_vs_new = 0

for item in items:
    s = item["subject"]
    subjects[s] = subjects.get(s, 0) + 1
    c = item["classification"]
    classifications[c] = classifications.get(c, 0) + 1
    d = item["difficulty"]
    difficulties[d] = difficulties.get(d, 0) + 1
    if item["oldVsNew"]:
        with_old_vs_new += 1

print("\n--- METRICS BREAKDOWN ---")
print(f"Total: {total}")
print("Subjects:", json.dumps(subjects, indent=2))
print("Classifications:", json.dumps(classifications, indent=2))
print("Difficulties:", json.dumps(difficulties, indent=2))
print(f"Items with oldVsNew mapping: {with_old_vs_new}")

# Build JS export
by_id = {item["id"]: item for item in items}
by_subject = {}
for item in items:
    by_subject.setdefault(item["subject"], []).append(item["id"])

subject_list = sorted(list(subjects.keys()))

modes_list = [
    {
        "id": "classic",
        "name": "Classic Myth Buster",
        "tagline": "Evaluate statutory propositions: True, False, or Depends?",
        "icon": "⚖️",
        "description": "Examine legal statements across Indian statutes and classify them accurately.",
        "badge": "Standard"
    },
    {
        "id": "find_error",
        "name": "Find the Legal Error",
        "tagline": "Pinpoint the precise erroneous statutory phrase within a flawed proposition.",
        "icon": "🔍",
        "description": "Identify the exact phrase that makes the proposition legally false.",
        "badge": "Analytical"
    },
    {
        "id": "correct_law",
        "name": "Correct the Law",
        "tagline": "Draft or select the accurate statutory correction to redeem a false statement.",
        "icon": "✍️",
        "description": "Replace the statutory misconception with authentic legislative wording.",
        "badge": "Drafting"
    },
    {
        "id": "exception_hunter",
        "name": "Exception Hunter",
        "tagline": "Track down statutory provisos, exceptions, and non-obstante clauses.",
        "icon": "🎯",
        "description": "Identify key statutory exceptions that qualify apparent legal generalities.",
        "badge": "Advanced"
    },
    {
        "id": "old_vs_new",
        "name": "Old Law vs New Law",
        "tagline": "Master statutory transitions from IPC/IEA/CrPC to BNS/BSA/BNSS 2023.",
        "icon": "🔄",
        "description": "Test your mastery over 2024 criminal law transition sections and reforms.",
        "badge": "Transition"
    },
    {
        "id": "precedent_challenge",
        "name": "Judicial Precedent Challenge",
        "tagline": "Disentangle genuine ratio decidendi from non-binding obiter dicta.",
        "icon": "🏛️",
        "description": "Verify landmark constitutional and civil precedents from the Supreme Court.",
        "badge": "Precedent"
    },
    {
        "id": "confidence_challenge",
        "name": "Confidence Challenge",
        "tagline": "Wager your confidence points before revealing statutory verdicts.",
        "icon": "⚡",
        "description": "Calibrate your judicial conviction: high stakes amplify both rewards and penalties.",
        "badge": "High Stakes"
    },
    {
        "id": "grand_trial",
        "name": "The Grand Truth Trial",
        "tagline": "A comprehensive timed judicial trial testing all legal disciplines.",
        "icon": "🏆",
        "description": "A rigorous 20-question mixed exam simulation across all legal disciplines.",
        "badge": "Championship"
    }
]

js_content = f"""/**
 * Tanveer Ashraf Judicial Prep - Game 7: Legal Myth Buster Database
 * Version 3.0 Phase 4 - Chamber of Truth
 * Total Verified Legal Statements: {total}
 * Verification Date: 2026-11-22
 * Author: Tauqeer Ashraf
 */

(function() {{
  'use strict';

  const ARENA_MYTHS = {json.dumps(items, indent=2, ensure_ascii=False)};

  const ARENA_MYTHS_BY_ID = {json.dumps(by_id, indent=2, ensure_ascii=False)};

  const ARENA_MYTHS_BY_SUBJECT = {json.dumps(by_subject, indent=2, ensure_ascii=False)};

  const ARENA_MYTHS_SUBJECTS = {json.dumps(subject_list, indent=2, ensure_ascii=False)};

  const ARENA_MYTHS_MODES = {json.dumps(modes_list, indent=2, ensure_ascii=False)};

  // Expose to global window
  if (typeof window !== 'undefined') {{
    window.ARENA_MYTHS = ARENA_MYTHS;
    window.ARENA_MYTHS_BY_ID = ARENA_MYTHS_BY_ID;
    window.ARENA_MYTHS_BY_SUBJECT = ARENA_MYTHS_BY_SUBJECT;
    window.ARENA_MYTHS_SUBJECTS = ARENA_MYTHS_SUBJECTS;
    window.ARENA_MYTHS_MODES = ARENA_MYTHS_MODES;
  }}

  if (typeof module !== 'undefined' && module.exports) {{
    module.exports = {{
      ARENA_MYTHS,
      ARENA_MYTHS_BY_ID,
      ARENA_MYTHS_BY_SUBJECT,
      ARENA_MYTHS_SUBJECTS,
      ARENA_MYTHS_MODES
    }};
  }}
}})();
"""

out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "games", "data", "legal-myths.js")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"\nSuccessfully generated {out_path} ({len(js_content):,} bytes)")
