# -*- coding: utf-8 -*-
"""
Master Crossword Generator for Tanveer Ashraf — Judicial Prep (V3.0 Phase 3).
Compiles and mathematically validates all 30 crossword puzzles across Beginner, Intermediate, and Advanced tiers.
Exports to assets/games/data/crossword-puzzles.js.
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

def generate_grid_puzzle(p_id, title, collection, difficulty, target_words, grid_dim):
    """
    Robust interconnected crossword generator.
    Grows an intersecting crossword network from a seed word.
    """
    for attempt in range(2000):
        grid = [["" for _ in range(grid_dim)] for _ in range(grid_dim)]
        placed_words = []
        
        # 1. Pick a seed horizontal word
        seed_pool = []
        for l in range(4, min(grid_dim - 2, 9)):
            seed_pool.extend(words_by_len.get(l, []))
        if not seed_pool: continue
        seed = random.choice(seed_pool)
        
        seed_r = random.choice([1, 2, 3])
        seed_c = 1
        for i, ch in enumerate(seed):
            grid[seed_r][seed_c + i] = ch
        placed_words.append({"word": seed, "direction": "across", "row": seed_r, "col": seed_c})
        
        # 2. Pick 2 to 4 vertical words intersecting the seed word
        indices = list(range(len(seed)))
        random.shuffle(indices)
        
        down_words = []
        for idx in indices:
            if len(down_words) >= 4: break
            col = seed_c + idx
            char = seed[idx]
            
            # Try vertical lengths
            v_lengths = list(range(4, min(grid_dim, 9)))
            random.shuffle(v_lengths)
            
            for v_len in v_lengths:
                possible_starts = [r for r in range(grid_dim - v_len + 1) if r <= seed_r < r + v_len]
                random.shuffle(possible_starts)
                
                placed_v = False
                for start_r in possible_starts:
                    pos_in_v = seed_r - start_r
                    cands = find_words_matching(v_len, {pos_in_v: char})
                    cands = [w for w in cands if w not in [x["word"] for x in placed_words]]
                    if not cands: continue
                    random.shuffle(cands)
                    
                    for v_w in cands:
                        can_place = True
                        for r_off, v_ch in enumerate(v_w):
                            curr = grid[start_r + r_off][col]
                            if curr != "" and curr != v_ch:
                                can_place = False
                                break
                        if not can_place: continue
                        
                        for r_off, v_ch in enumerate(v_w):
                            grid[start_r + r_off][col] = v_ch
                        placed_words.append({"word": v_w, "direction": "down", "row": start_r, "col": col})
                        down_words.append((start_r, col, v_w))
                        placed_v = True
                        break
                    if placed_v: break
                if placed_v: break
                
        if len(down_words) < 2:
            continue
            
        # 3. Add more horizontal words intersecting the placed vertical words
        cand_rows = [r for r in range(1, grid_dim - 1) if abs(r - seed_r) >= 2]
        random.shuffle(cand_rows)
        
        for cand_r in cand_rows:
            crossing = {}
            for start_r, col, v_w in down_words:
                if start_r <= cand_r < start_r + len(v_w):
                    crossing[col] = v_w[cand_r - start_r]
                    
            if not crossing: continue
            
            sorted_cols = sorted(crossing.keys())
            min_c = min(sorted_cols)
            max_c = max(sorted_cols)
            span = max_c - min_c + 1
            
            for start_c in range(max(0, max_c - 8), min_c + 1):
                for h_len in range(max(span, 4), min(grid_dim - start_c, 10)):
                    constraints = {}
                    for c, ch in crossing.items():
                        offset = c - start_c
                        if 0 <= offset < h_len:
                            constraints[offset] = ch
                    if not constraints: continue
                    
                    cands = find_words_matching(h_len, constraints)
                    cands = [w for w in cands if w not in [x["word"] for x in placed_words]]
                    if not cands: continue
                    random.shuffle(cands)
                    
                    for h_w in cands:
                        can_place = True
                        for i, ch in enumerate(h_w):
                            curr = grid[cand_r][start_c + i]
                            if curr != "" and curr != ch:
                                can_place = False
                                break
                        if not can_place: continue
                        
                        for i, ch in enumerate(h_w):
                            grid[cand_r][start_c + i] = ch
                        placed_words.append({"word": h_w, "direction": "across", "row": cand_r, "col": start_c})
                        break
                    if len(placed_words) >= target_words: break
                if len(placed_words) >= target_words: break
            if len(placed_words) >= target_words: break
            
        if len(placed_words) >= target_words:
            return build_puzzle(p_id, title, collection, difficulty, {"rows": grid_dim, "cols": grid_dim}, placed_words)

    raise RuntimeError(f"Could not generate puzzle {p_id} with target {target_words} words after 2000 attempts.")

BEGINNER_TITLES = [
    ("cw-beg-01", "Constitutional Bench", "Constitutional Law"),
    ("cw-beg-02", "Criminal Penal Pillars", "Bharatiya Nyaya Sanhita"),
    ("cw-beg-03", "Civil Procedure First Steps", "Civil Procedure"),
    ("cw-beg-04", "The Evidentiary Core", "Law of Evidence"),
    ("cw-beg-05", "Contract Enforceability Basics", "Contract Law"),
    ("cw-beg-06", "Civil Wrongs & Torts Primer", "Law of Torts"),
    ("cw-beg-07", "First Principles of Jurisprudence", "Jurisprudence"),
    ("cw-beg-08", "Latin Maxims Essentials", "Legal Maxims"),
    ("cw-beg-09", "Judicial Officer Cause List", "Judicial Terminology"),
    ("cw-beg-10", "The Judicial Generalist", "Mixed Judicial Knowledge")
]

INTERMEDIATE_TITLES = [
    ("cw-int-01", "The Fundamental Rights Vault", "Constitutional Law"),
    ("cw-int-02", "Offenses Against the Person", "Bharatiya Nyaya Sanhita"),
    ("cw-int-03", "Bail & Custodial Inquiries", "Criminal Procedure"),
    ("cw-int-04", "Burden of Proof & Estoppel", "Law of Evidence"),
    ("cw-int-05", "Pleadings, Decrees & Orders", "Civil Procedure"),
    ("cw-int-06", "Vitiating Factors in Contract", "Contract Law"),
    ("cw-int-07", "Strict Liability & Defamation", "Law of Torts"),
    ("cw-int-08", "Legal Theories & Analytical Positivism", "Jurisprudence"),
    ("cw-int-09", "Latin Doctrines of Adjudication", "Legal Maxims"),
    ("cw-int-10", "Precedents & Apex Rulings", "Landmark Indian Judgments")
]

ADVANCED_TITLES = [
    ("cw-adv-01", "The Constitutional Assembly Archive", "Constitutional Law"),
    ("cw-adv-02", "Aggravated Crimes & Common Intention", "Bharatiya Nyaya Sanhita"),
    ("cw-adv-03", "Procedural Inquests & Trial Mechanics", "Criminal Procedure"),
    ("cw-adv-04", "The Digital Certificate & Res Gestae", "Law of Evidence"),
    ("cw-adv-05", "Execution, Garnishee & Restitution", "Civil Procedure"),
    ("cw-adv-06", "Commercial Indemnity & Bailment", "Contract Law"),
    ("cw-adv-07", "Absolute Liability & Environmental Torts", "Law of Torts"),
    ("cw-adv-08", "The Pure Theory & Grundnorm", "Jurisprudence"),
    ("cw-adv-09", "Maxims of Sovereign Justice", "Legal Maxims"),
    ("cw-adv-10", "The Grand Judicial Synthesis", "Mixed Judicial Knowledge")
]

ALL_PUZZLES = []

print("Generating 10 Beginner Puzzles (Target: 5 words, 8x8)...")
for p_id, title, coll in BEGINNER_TITLES:
    p = generate_grid_puzzle(p_id, title, coll, "beginner", target_words=5, grid_dim=8)
    ALL_PUZZLES.append(p)
    print(f" [+] Generated {p_id}: {title} ({len(p['words'])} words)")

print("\nGenerating 10 Intermediate Puzzles (Target: 6 words, 10x10)...")
for p_id, title, coll in INTERMEDIATE_TITLES:
    p = generate_grid_puzzle(p_id, title, coll, "intermediate", target_words=6, grid_dim=10)
    ALL_PUZZLES.append(p)
    print(f" [+] Generated {p_id}: {title} ({len(p['words'])} words)")

print("\nGenerating 10 Advanced Puzzles (Target: 7 words, 12x12)...")
for p_id, title, coll in ADVANCED_TITLES:
    p = generate_grid_puzzle(p_id, title, coll, "advanced", target_words=7, grid_dim=12)
    ALL_PUZZLES.append(p)
    print(f" [+] Generated {p_id}: {title} ({len(p['words'])} words)")

print(f"\nSuccessfully compiled all {len(ALL_PUZZLES)} crossword puzzles!")

js_content = """/**
 * LEGAL CROSSWORD PUZZLES DATABASE (V3.0 Phase 3)
 * Authoritative Indian Law Crosswords compiled for UP Judicial Services (UP PCS-J)
 * Total Puzzles: 30 mathematically verified, 100% intersecting playable puzzles
 * Across 3 Difficulty Tiers: 10 Beginner, 10 Intermediate, 10 Advanced
 */
(function() {
  'use strict';

  const PUZZLES = """ + json.dumps(ALL_PUZZLES, indent=2, ensure_ascii=False) + """;

  const BY_ID = {};
  const BY_DIFFICULTY = { beginner: [], intermediate: [], advanced: [] };
  const BY_COLLECTION = {};

  PUZZLES.forEach(p => {
    BY_ID[p.id] = p;
    if (BY_DIFFICULTY[p.difficulty]) {
      BY_DIFFICULTY[p.difficulty].push(p);
    }
    if (!BY_COLLECTION[p.collection]) {
      BY_COLLECTION[p.collection] = [];
    }
    BY_COLLECTION[p.collection].push(p);
  });

  window.ARENA_CROSSWORDS = PUZZLES;
  window.ARENA_CROSSWORDS_BY_ID = BY_ID;
  window.ARENA_CROSSWORDS_BY_DIFFICULTY = BY_DIFFICULTY;
  window.ARENA_CROSSWORDS_BY_COLLECTION = BY_COLLECTION;
})();
"""

out_path = os.path.join("assets", "games", "data", "crossword-puzzles.js")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Written to {out_path} ({os.path.getsize(out_path)} bytes).")
