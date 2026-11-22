"""
Updates the navigation in all 21 existing HTML pages to include Subject Academy.
Target: insert immediately before `<a href="brain-arena.html"` in `<nav class="nav"`
"""

import glob
import re

NAV_ITEM = '<a href="learning-academy.html" data-view="academy"><span aria-hidden="true">🏛️</span>Subject Academy</a>'

pages = sorted(glob.glob("*.html"))
updated_count = 0

for p in pages:
    if p in ["learning-academy.html", "subject-study.html", "topic-practice.html", "subject-progress.html"]:
        continue
        
    with open(p, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "learning-academy.html" in content:
        print(f"Skipping {p}: already contains learning-academy.html")
        continue

    # Find <a href="brain-arena.html"
    target = '<a href="brain-arena.html"'
    if target in content:
        new_content = content.replace(target, NAV_ITEM + target, 1)
        with open(p, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {p}")
        updated_count += 1
    else:
        print(f"WARNING: {target} not found in {p}")

print(f"Total pages updated: {updated_count}")
