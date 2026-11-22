# -*- coding: utf-8 -*-
"""
Generate 30 themed legal crosswords using template search.
"""
import json
import os
import random
from crossword_compiler import build_puzzle, VOCAB_MAP
from crossword_solver import find_words_matching, words_by_len

COLLECTIONS = [
    "Constitutional Law",
    "Bharatiya Nyaya Sanhita",
    "Criminal Procedure",
    "Law of Evidence",
    "Civil Procedure",
    "Contract Law",
    "Law of Torts",
    "Jurisprudence",
    "Legal Maxims",
    "Landmark Indian Judgments",
    "Judicial Terminology",
    "Mixed Judicial Knowledge"
]

def generate_beginner_grid(p_id, title, collection):
    """
    Template for 7x7 beginner grid:
    H1 at (1, 1), len 5
    H2 at (3, 1), len 5
    H3 at (5, 1), len 5
    V1 at (1, 2), len 5 (intersects H1[1], H2[1], H3[1])
    V2 at (1, 4), len 5 (intersects H1[3], H2[3], H3[3])
    Plus optional V3 at (1, 1) or (1, 5) or H4
    """
    # 5-letter words
    w5 = words_by_len.get(5, [])
    random.shuffle(w5)
    
    for h1 in w5:
        # Candidate V1 at col 2: V1[0] == h1[1]
        v1_cands = find_words_matching(5, {0: h1[1]})
        if not v1_cands: continue
        random.shuffle(v1_cands)
        
        for v1 in v1_cands:
            # Candidate V2 at col 4: V2[0] == h1[3]
            v2_cands = find_words_matching(5, {0: h1[3]})
            if not v2_cands: continue
            random.shuffle(v2_cands)
            
            for v2 in v2_cands:
                if v2 == v1: continue
                # H2 must match: H2[1] == v1[2], H2[3] == v2[2]
                h2_cands = find_words_matching(5, {1: v1[2], 3: v2[2]})
                h2_cands = [w for w in h2_cands if w not in (h1, v1, v2)]
                if not h2_cands: continue
                random.shuffle(h2_cands)
                
                for h2 in h2_cands:
                    # H3 must match: H3[1] == v1[4], H3[3] == v2[4]
                    h3_cands = find_words_matching(5, {1: v1[4], 3: v2[4]})
                    h3_cands = [w for w in h3_cands if w not in (h1, h2, v1, v2)]
                    if not h3_cands: continue
                    h3 = h3_cands[0]
                    
                    # Also try to find a 6th word V3 at col 1 or col 5!
                    v3_cands = find_words_matching(5, {0: h1[0], 2: h2[0], 4: h3[0]})
                    v3_cands = [w for w in v3_cands if w not in (h1, h2, h3, v1, v2)]
                    
                    word_defs = [
                        {"word": h1, "direction": "across", "row": 1, "col": 1},
                        {"word": h2, "direction": "across", "row": 3, "col": 1},
                        {"word": h3, "direction": "across", "row": 5, "col": 1},
                        {"word": v1, "direction": "down", "row": 1, "col": 2},
                        {"word": v2, "direction": "down", "row": 1, "col": 4}
                    ]
                    if v3_cands:
                        word_defs.append({"word": v3_cands[0], "direction": "down", "row": 1, "col": 1})
                        
                    return build_puzzle(p_id, title, collection, "beginner", {"rows": 7, "cols": 7}, word_defs)
                    
    raise RuntimeError(f"Could not generate beginner grid for {p_id}")

print("Testing generate_beginner_grid...")
test_p = generate_beginner_grid("cw-beg-test", "Test Grid", "Constitutional Law")
print("Success! Words in test grid:")
for w in test_p["words"]:
    print(f" - {w['clueNum']} {w['direction'].upper()}: {w['word']}")
