import json
import os

def create_concept_file(filepath, var_name, data):
    content = f"""/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Judicial Learning Academy Data Module
 */
(function(global) {{
  'use strict';

  const DATA = {json.dumps(data, indent=2, ensure_ascii=False)};

  global.{var_name} = DATA;
  if (typeof module !== 'undefined' && module.exports) {{
    module.exports = DATA;
  }}
}})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {filepath} ({len(data)} topics)")

# Let's write the master aggregator generator
def create_aggregator(filepath, master_var, parts):
    part_merges = "\n    ".join([f"Object.assign(ALL, global.{p} || {{}});" for p in parts])
    content = f"""/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Judicial Learning Academy — Master Concepts Aggregator
 */
(function(global) {{
  'use strict';

  function aggregate() {{
    const ALL = {{}};
    {part_merges}
    return ALL;
  }}

  const CONCEPTS = aggregate();
  global.{master_var} = CONCEPTS;

  if (typeof module !== 'undefined' && module.exports) {{
    module.exports = CONCEPTS;
  }}
}})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created aggregator {filepath}")

print("Helper ready.")
