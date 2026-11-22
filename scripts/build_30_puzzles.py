# -*- coding: utf-8 -*-
"""
Builder & Mathematical Validator for all 30 Crossword Puzzles
Generates assets/games/data/crossword-puzzles.js for Tanveer Ashraf — Judicial Prep (V3.0 Phase 3).
"""
import json
import os

def validate_and_number_puzzle(p):
    rows = p["gridSize"]["rows"]
    cols = p["gridSize"]["cols"]
    grid = [["" for _ in range(cols)] for _ in range(rows)]
    
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

PUZZLES = []

# =============================================================================
# 10 BEGINNER PUZZLES (7x7 / 8x8)
# =============================================================================

# 1. cw-beg-01: Constitutional Core (7x7)
PUZZLES.append({
    "id": "cw-beg-01",
    "title": "The Constitutional Core",
    "collection": "Constitutional Law",
    "difficulty": "beginner",
    "gridSize": {"rows": 7, "cols": 7},
    "words": [
        {"word": "WRIT", "direction": "across", "row": 1, "col": 1, "clue": "Prerogative judicial order under Article 32 or 226", "hint": "Constitutional remedy", "authority": "Constitution of India, Art 32/226", "vocabId": "voc-001"},
        {"word": "RULE", "direction": "across", "row": 3, "col": 1, "clue": "Established legal principle or governing regulation", "hint": "Rule of law", "authority": "Constitution of India, Art 14"},
        {"word": "TEST", "direction": "across", "row": 5, "col": 1, "clue": "Legal standard applied by court to evaluate validity", "hint": "e.g. proportionality test", "authority": "K.S. Puttaswamy v. UOI"},
        {"word": "WORST", "direction": "down", "row": 1, "col": 1, "clue": "Most severe penalty or consequence in law", "hint": "Superlative of bad", "authority": "Penology Principles"},
        {"word": "ROUTE", "direction": "down", "row": 1, "col": 2, "clue": "Course or procedural path of an appeal or petition", "hint": "Appellate channel", "authority": "Civil/Criminal Procedure"},
        {"word": "IDLES", "direction": "down", "row": 1, "col": 3, "clue": "Remains dormant or inactive, as an unasserted right", "hint": "Laches and delay", "authority": "Limitation Doctrine"},
        {"word": "THEFT", "direction": "down", "row": 1, "col": 4, "clue": "Dishonest taking of movable property under Section 303 BNS", "hint": "Offence against property", "authority": "BNS 2023, Sec 303", "vocabId": "voc-031"}
    ]
})

# 2. cw-beg-02: Criminal Law Foundations (7x7)
# Across:
# (1, 1): CRIME (5 letters: C R I M E)
# (3, 1): ARREST (Wait, 6 letters: A R R E S T -> row 3 col 1..6)
# (5, 1): ORDER (5 letters: O R D E R)
# Let's check Down words connecting them:
# c=1: (1,1)=C, (3,1)=A, (5,1)=O -> 5 letters at c=1: C _ A _ O -> CANTO? (1,1)=C, (2,1)=A, (3,1)=N (conflict: (3,1) is A)
# Let's design Down words first:
# Down:
# (1,1): COURT (5 letters: C, O, U, R, T)
# (1,3): ORDER (5 letters: O, R, D, E, R)
# (1,5): TRIAL (5 letters: T, R, I, A, L)
# Across intersecting:
# at row 1: (1,1)=C, (1,3)=O, (1,5)=T -> C _ O _ T -> CLOTH? (1,1)=C, (1,2)=L, (1,3)=O, (1,4)=T, (1,5)=H (conflict: (1,5) is T).
# C _ O _ T: CLOUT, CHOWT, CROFT!
# What about Across at row 3:
# COURT has (3,1)=U.
# ORDER has (3,3)=D.
# TRIAL has (3,5)=I.
# (3,1)=U, (3,3)=D, (3,5)=I -> U _ D _ I?
# Let's make clean, elegant, standard grids:
PUZZLES.append({
    "id": "cw-beg-02",
    "title": "Criminal Law Foundations",
    "collection": "Criminal Law",
    "difficulty": "beginner",
    "gridSize": {"rows": 7, "cols": 7},
    "words": [
        {"word": "BAIL", "direction": "across", "row": 1, "col": 1, "clue": "Judicial release of an accused from custody upon security", "hint": "Rule is bail, jail is exception", "authority": "BNSS 2023, Sec 478-485", "vocabId": "voc-247"},
        {"word": "ACTS", "direction": "across", "row": 3, "col": 1, "clue": "Overt physical conducts constituting criminal offenses", "hint": "Physical bodily movements", "authority": "BNS 2023, Sec 2(1)", "vocabId": "voc-039"},
        {"word": "PLEA", "direction": "across", "row": 5, "col": 1, "clue": "Formal response of accused to criminal charge (guilty/not guilty)", "hint": "Plea bargaining or defense", "authority": "BNSS 2023, Chapter XXII"},
        {"word": "TRAP", "direction": "down", "row": 1, "col": 4, "clue": "Lawful decoy operation to catch corrupt public servants", "hint": "Anti-corruption trap", "authority": "Prevention of Corruption Act"},
        {"word": "BEAT", "direction": "down", "row": 1, "col": 1, "clue": "Physical blow or strike constituting criminal force", "hint": "Assault and battery", "authority": "BNS 2023, Sec 129", "vocabId": "voc-044"},
        {"word": "ACRE", "direction": "down", "row": 1, "col": 2, "clue": "Standard measurement of real property or agricultural land", "hint": "Unit of land measurement", "authority": "Revenue Code"},
        {"word": "LATE", "direction": "down", "row": 1, "col": 3, "clue": "Delayed filing past limitation period", "hint": "Tardy or delayed", "authority": "Limitation Act, 1963"}
    ]
})
# Let's check cw-beg-02 intersections:
# Across 1: BAIL: (1,1)=B, (1,2)=A, (1,3)=I, (1,4)=L (Wait: TRAP down at (1,4) has T, but BAIL has L!)
# If col 4 has T: BAIT!
# BAIT: (1,1)=B, (1,2)=A, (1,3)=I, (1,4)=T!
# And TRAP: (1,4)=T, (2,4)=R, (3,4)=A, (4,4)=P.
# Row 3 is ACTS: (3,1)=A, (3,2)=C, (3,3)=T, (3,4)=S (Wait, TRAP has (3,4)=A!)
# If Row 3 has (3,4)=A: ACTA!
# Let's write a python solver function to verify every puzzle automatically!
