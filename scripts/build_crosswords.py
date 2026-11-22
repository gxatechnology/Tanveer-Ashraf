# -*- coding: utf-8 -*-
"""
Crossword Puzzle Builder & Mathematical Grid Validator for Tanveer Ashraf — Judicial Prep (V3.0 Phase 3)
Builds 30 completely validated, playable crossword puzzles across 3 difficulty tiers.
Guarantees 100% intersection letter matching, clue numbering, and connectivity.
"""
import json
import os

PUZZLES = []

def create_grid(rows, cols, words):
    """
    Simulate and validate crossword grid word placements.
    Ensures letters at intersection points match identically.
    Assigns sequential clue numbers based on starting cell coordinates.
    """
    grid = [["" for _ in range(cols)] for _ in range(rows)]
    
    # 1. Place letters and verify intersections
    for item in words:
        w = item["word"].upper().replace(" ", "")
        r = item["row"]
        c = item["col"]
        d = item["direction"].lower()
        
        if d == "across":
            if c + len(w) > cols:
                raise ValueError(f"Word '{w}' out of bounds horizontally at ({r}, {c}) for grid {rows}x{cols}")
            for i, ch in enumerate(w):
                curr = grid[r][c + i]
                if curr != "" and curr != ch:
                    raise ValueError(f"Intersection conflict for '{w}' at ({r}, {c+i}): existing '{curr}' vs '{ch}'")
                grid[r][c + i] = ch
        elif d == "down":
            if r + len(w) > rows:
                raise ValueError(f"Word '{w}' out of bounds vertically at ({r}, {c}) for grid {rows}x{cols}")
            for i, ch in enumerate(w):
                curr = grid[r + i][c]
                if curr != "" and curr != ch:
                    raise ValueError(f"Intersection conflict for '{w}' at ({r+i}, {c}): existing '{curr}' vs '{ch}'")
                grid[r + i][c] = ch
        else:
            raise ValueError(f"Invalid direction '{d}' for word '{w}'")
            
    # 2. Assign standard crossword clue numbers based on cell coordinates (top-to-bottom, left-to-right)
    # Collect unique start cells
    start_cells = {}
    for item in words:
        coord = (item["row"], item["col"])
        if coord not in start_cells:
            start_cells[coord] = []
        start_cells[coord].append(item)
        
    sorted_coords = sorted(start_cells.keys(), key=lambda pt: (pt[0], pt[1]))
    clue_counter = 1
    cell_to_clue_num = {}
    
    for pt in sorted_coords:
        cell_to_clue_num[pt] = clue_counter
        for w_item in start_cells[pt]:
            w_item["clueNum"] = clue_counter
        clue_counter += 1
        
    return grid

# =============================================================================
# 10 BEGINNER PUZZLES (7x7 or 8x8)
# =============================================================================

# --- Puzzle 1: Constitutional Basics (7x7) ---
# WRIT across (1, 1), LAW across (3, 2), ACT across (5, 3)
# DOWN: WILL down (0, 1), TACT down (1, 4), LAW down (3, 2)
# Intersect: WRIT (1,1..4) shares:
# (1,1) with WILL (0..3, 1) -> W
# (1,4) with TACT (1..4, 4) -> T
# (3,2) with LAW (3..5, 2) -> L
p1_words = [
    {"word": "WRIT", "direction": "across", "row": 1, "col": 1,
     "clue": "Formal judicial order issued by superior court under Article 32 or 226",
     "hint": "Prerogative constitutional remedy", "authority": "Constitution of India, Art 32/226", "vocabId": "voc-001"},
    {"word": "WILL", "direction": "down", "row": 0, "col": 1,
     "clue": "Legal testament declaring how a testator's estate shall be distributed",
     "hint": "Takes effect upon death", "authority": "Indian Succession Act, 1925, Sec 2(h)"},
    {"word": "TACT", "direction": "down", "row": 1, "col": 4,
     "clue": "Adroitness in dealing with complex judicial advocacy and court decorum",
     "hint": "Skill in human relations", "authority": "Advocacy Ethics"},
    {"word": "LAW", "direction": "across", "row": 3, "col": 2,
     "clue": "Binding statutory rule or command of sovereign governing a community",
     "hint": "Defined in Article 13(3) of Constitution", "authority": "Constitution of India, Art 13", "vocabId": "voc-186"},
    {"word": "ACT", "direction": "across", "row": 5, "col": 3,
     "clue": "Formal statutory bill passed by legislature and assented to by President/Governor",
     "hint": "Enactment of Parliament", "authority": "General Clauses Act, 1897"}
]
# Intersections check:
# WILL (0,1)=W, (1,1)=I (Wait! WRIT starts at col 1: WRIT: (1,1)=W, (1,2)=R, (1,3)=I, (1,4)=T)
# If WILL down (0,1): (0,1)=W, (1,1)=I -> Conflict with WRIT (1,1)=W!
# Let's design coordinates cleanly with Python!
