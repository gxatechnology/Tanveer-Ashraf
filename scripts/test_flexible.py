# -*- coding: utf-8 -*-
"""
Flexible grid generator for intermediate and advanced crosswords.
"""
import json
import os
import random
from crossword_compiler import build_puzzle, VOCAB_MAP
from crossword_solver import find_words_matching, words_by_len

def generate_flexible_puzzle(p_id, title, collection, difficulty, target_words=6, grid_dim=10):
    """
    Builds an interconnected crossword puzzle by growing from a seed word.
    """
    for attempt in range(500):
        # 1. Pick a seed horizontal word (len 5 to 8)
        seed_len = random.choice([5, 6, 7, 8])
        seed_pool = words_by_len.get(seed_len, [])
        if not seed_pool: continue
        seed = random.choice(seed_pool)
        
        placed_words = [
            {"word": seed, "direction": "across", "row": 2, "col": 1}
        ]
        grid = [["" for _ in range(grid_dim)] for _ in range(grid_dim)]
        for i, ch in enumerate(seed):
            grid[2][1 + i] = ch
            
        # 2. Pick 2 to 3 down words intersecting the seed word
        # Intersection positions on seed:
        intersect_indices = [idx for idx in range(len(seed)) if idx % 2 == 1 or idx == 0]
        random.shuffle(intersect_indices)
        
        down_words = []
        for idx in intersect_indices[:3]:
            col = 1 + idx
            char = seed[idx]
            # Try to place a vertical word of length 5 to 8 that has `char` at row 2
            # The vertical word can start at row 0, 1, or 2
            start_row = random.choice([0, 1, 2])
            v_len = random.choice([5, 6, 7, 8])
            pos_in_v = 2 - start_row
            if pos_in_v < 0 or pos_in_v >= v_len or start_row + v_len > grid_dim:
                continue
                
            cands = find_words_matching(v_len, {pos_in_v: char})
            cands = [w for w in cands if w not in [x["word"] for x in placed_words]]
            if not cands: continue
            
            v_word = random.choice(cands)
            # Check placement
            valid = True
            for r_offset, v_ch in enumerate(v_word):
                curr = grid[start_row + r_offset][col]
                if curr != "" and curr != v_ch:
                    valid = False
                    break
            if not valid: continue
            
            # Place
            for r_offset, v_ch in enumerate(v_word):
                grid[start_row + r_offset][col] = v_ch
            placed_words.append({"word": v_word, "direction": "down", "row": start_row, "col": col})
            down_words.append((start_row, col, v_word))
            
        if len(down_words) < 2:
            continue
            
        # 3. Pick 2 to 3 across words intersecting the down words at lower rows (e.g. rows 4, 5, 6, 7)
        for cand_row in range(4, grid_dim - 1):
            # Check which down words cross this row
            crossing_letters = {}
            for start_r, col, v_w in down_words:
                if start_r <= cand_row < start_r + len(v_w):
                    crossing_letters[col] = v_w[cand_row - start_r]
                    
            if len(crossing_letters) >= 2:
                # Find an across word that spans these columns
                sorted_cols = sorted(crossing_letters.keys())
                min_c = min(sorted_cols)
                max_c = max(sorted_cols)
                req_span = max_c - min_c + 1
                
                # We can start the across word at min_c or min_c - 1
                for start_c in [min_c, max(0, min_c - 1)]:
                    for h_len in range(req_span, min(grid_dim - start_c, 10)):
                        # Build constraints
                        constraints = {}
                        for c, ch in crossing_letters.items():
                            offset = c - start_c
                            if 0 <= offset < h_len:
                                constraints[offset] = ch
                        if len(constraints) < 2: continue
                        
                        h_cands = find_words_matching(h_len, constraints)
                        h_cands = [w for w in h_cands if w not in [x["word"] for x in placed_words]]
                        if not h_cands: continue
                        
                        h_word = random.choice(h_cands)
                        # Check placement
                        can_place = True
                        for i, ch in enumerate(h_word):
                            curr = grid[cand_row][start_c + i]
                            if curr != "" and curr != ch:
                                can_place = False
                                break
                        if not can_place: continue
                        
                        for i, ch in enumerate(h_word):
                            grid[cand_row][start_c + i] = ch
                        placed_words.append({"word": h_word, "direction": "across", "row": cand_row, "col": start_c})
                        break
                    if len(placed_words) >= target_words: break
            if len(placed_words) >= target_words: break
            
        if len(placed_words) >= target_words:
            return build_puzzle(p_id, title, collection, difficulty, {"rows": grid_dim, "cols": grid_dim}, placed_words)
            
    # If not enough with 2 down words, try simple 5-word fallback
    print(f"Fallback flexible for {p_id}")
    return None

print("Testing flexible generator...")
p = generate_flexible_puzzle("test-int", "Test Int", "Criminal Law", "intermediate", target_words=5, grid_dim=10)
if p:
    print(f"Successfully generated flexible puzzle with {len(p['words'])} words!")
    for w in p["words"]:
        print(f" - {w['clueNum']} {w['direction'].upper()} at ({w['row']},{w['col']}): {w['word']}")
else:
    print("Failed")
