# -*- coding: utf-8 -*-
"""
Generator & Mathematical Validator for all 30 Crossword Puzzles (V3.0 Phase 3).
"""
import json
import os

def validate_and_number_puzzle(p):
    """
    Validates a puzzle grid and assigns standard crossword clue numbers.
    """
    rows = p["gridSize"]["rows"]
    cols = p["gridSize"]["cols"]
    grid = [["" for _ in range(cols)] for _ in range(rows)]
    
    # 1. Place and verify letters
    for w in p["words"]:
        word = w["word"].upper().replace(" ", "")
        r = w["row"]
        c = w["col"]
        d = w["direction"].lower()
        
        if d == "across":
            if c + len(word) > cols:
                raise ValueError(f"[{p['id']}] Word '{word}' out of horizontal bounds at ({r}, {c}) for grid {rows}x{cols}")
            for i, ch in enumerate(word):
                existing = grid[r][c + i]
                if existing != "" and existing != ch:
                    raise ValueError(f"[{p['id']}] Conflict at ({r}, {c+i}): existing '{existing}' vs '{ch}' for word '{word}'")
                grid[r][c + i] = ch
        elif d == "down":
            if r + len(word) > rows:
                raise ValueError(f"[{p['id']}] Word '{word}' out of vertical bounds at ({r}, {c}) for grid {rows}x{cols}")
            for i, ch in enumerate(word):
                existing = grid[r + i][c]
                if existing != "" and existing != ch:
                    raise ValueError(f"[{p['id']}] Conflict at ({r+i}, {c}): existing '{existing}' vs '{ch}' for word '{word}'")
                grid[r + i][c] = ch
        else:
            raise ValueError(f"[{p['id']}] Invalid direction '{d}'")

    # 2. Assign clue numbers by reading order
    coords = {}
    for w in p["words"]:
        pt = (w["row"], w["col"])
        if pt not in coords:
            coords[pt] = []
        coords[pt].append(w)
        
    sorted_pts = sorted(coords.keys(), key=lambda x: (x[0], x[1]))
    counter = 1
    for pt in sorted_pts:
        for w in coords[pt]:
            w["clueNum"] = counter
        counter += 1
        
    p["solutionGrid"] = ["".join(row) for row in grid]
    return p

ALL_PUZZLES = []
print("Puzzle validator loaded.")
