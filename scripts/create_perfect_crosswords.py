# -*- coding: utf-8 -*-
"""
Automated Crossword Grid Synthesizer for Tanveer Ashraf — Judicial Prep (V3.0 Phase 3).
Finds real intersecting words from the verified vocabulary database.
"""
import json
import os
import re

# Load vocabulary
with open(os.path.join("assets", "games", "data", "legal-vocabulary.js"), "r", encoding="utf-8") as f:
    text = f.read()
    # Extract JSON between const VOCABULARY = and ;
    m = re.search(r'const VOCABULARY\s*=\s*(\[.*?\]);\s*\n\s*//', text, re.DOTALL)
    if not m:
        raise ValueError("Could not parse legal-vocabulary.js")
    vocab = json.loads(m.group(1))

print(f"Loaded {len(vocab)} vocabulary items for crossword synthesis.")

# Filter clean alphabetic words
words_by_len = {}
vocab_by_word = {}

for v in vocab:
    w = v["canonical"].upper().replace(" ", "")
    if re.match(r'^[A-Z]+$', w):
        l = len(w)
        if l not in words_by_len:
            words_by_len[l] = []
        if w not in words_by_len[l]:
            words_by_len[l].append(w)
            vocab_by_word[w] = v

print("Word length distribution:")
for k in sorted(words_by_len.keys()):
    print(f" - Length {k}: {len(words_by_len[k])} words")
