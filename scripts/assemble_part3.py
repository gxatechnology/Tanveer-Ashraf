"""
Assembles Part 3 concepts from all modular builders and writes:
- assets/learning/data/constitution/constitution-concepts-part3.js
- assets/learning/data/constitution/constitution-concepts.js (Aggregator)
"""
import sys
import os
import json

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))

from build_part3_concepts import PART3 as CH9
from part3_ch10 import CH10
from part3_ch11 import CH11
from part3_ch12 import CH12
from part3_ch13_ch14 import CH13_14
from part3_ch15 import CH15

ALL_PART3 = {}
ALL_PART3.update(CH9)
ALL_PART3.update(CH10)
ALL_PART3.update(CH11)
ALL_PART3.update(CH12)
ALL_PART3.update(CH13_14)
ALL_PART3.update(CH15)

print(f"Total Part 3 topics assembled: {len(ALL_PART3)}")

# Write Part 3 JS file
out_part3_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'learning', 'data', 'constitution', 'constitution-concepts-part3.js')
os.makedirs(os.path.dirname(out_part3_path), exist_ok=True)

js_part3 = """/**
 * Judicial Learning Academy — Constitution Concepts Part 3
 * Chapters 9 to 15 (22 Topics)
 * Rigorously authored and verified for UP PCS-J Preliminary & Mains Examination.
 */
(function() {
  'use strict';

  const CONSTITUTION_CONCEPTS_PART3 = """ + json.dumps(ALL_PART3, indent=2, ensure_ascii=False) + """;

  if (typeof window !== 'undefined') {
    window.CONSTITUTION_CONCEPTS_PART3 = CONSTITUTION_CONCEPTS_PART3;
  }
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONSTITUTION_CONCEPTS_PART3;
  }
})();
"""

with open(out_part3_path, 'w', encoding='utf-8') as f:
    f.write(js_part3)

print(f"Successfully wrote {out_part3_path} ({len(js_part3)} chars).")

# Now write the master aggregator: assets/learning/data/constitution/constitution-concepts.js
out_master_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'learning', 'data', 'constitution', 'constitution-concepts.js')

js_master = """/**
 * Judicial Learning Academy — Master Constitution Concepts Aggregator
 * Merges Part 1 (Ch 1–5, 12 topics), Part 2 (Ch 6–8, 11 topics), and Part 3 (Ch 9–15, 22 topics)
 * Total: 45 Comprehensive Authoritative Topics for UP PCS-J.
 */
(function() {
  'use strict';

  const p1 = (typeof window !== 'undefined' && window.CONSTITUTION_CONCEPTS_PART1) ||
             (typeof require !== 'undefined' ? require('./constitution-concepts-part1.js') : {});
  const p2 = (typeof window !== 'undefined' && window.CONSTITUTION_CONCEPTS_PART2) ||
             (typeof require !== 'undefined' ? require('./constitution-concepts-part2.js') : {});
  const p3 = (typeof window !== 'undefined' && window.CONSTITUTION_CONCEPTS_PART3) ||
             (typeof require !== 'undefined' ? require('./constitution-concepts-part3.js') : {});

  const CONSTITUTION_CONCEPTS = Object.assign({}, p1, p2, p3);

  if (typeof window !== 'undefined') {
    window.CONSTITUTION_CONCEPTS = CONSTITUTION_CONCEPTS;
  }
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONSTITUTION_CONCEPTS;
  }
})();
"""

with open(out_master_path, 'w', encoding='utf-8') as f:
    f.write(js_master)

print(f"Successfully wrote master aggregator {out_master_path}.")
