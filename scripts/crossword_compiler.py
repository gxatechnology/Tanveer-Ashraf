# -*- coding: utf-8 -*-
"""
Automated Crossword Layout Synthesizer for Tanveer Ashraf — Judicial Prep (V3.0 Phase 3).
Finds real intersecting legal words and generates validated 2D crossword puzzle grids.
"""
import json
import os
import random

# Load vocabulary
with open(os.path.join("assets", "games", "data", "legal-vocabulary.js"), "r", encoding="utf-8") as f:
    text = f.read()
    import re
    m = re.search(r'const VOCABULARY\s*=\s*(\[.*?\]);\s*\n\s*//', text, re.DOTALL)
    vocab = json.loads(m.group(1))

VOCAB_MAP = {v["canonical"].upper().replace(" ", ""): v for v in vocab}

# Load extra legal words
from solve_grids import LEGAL_WORDS

ALL_WORDS = list(set([w.upper().replace(" ", "") for w in LEGAL_WORDS] + list(VOCAB_MAP.keys())))
# Filter to purely alphabetic words of length 3..14
WORDS = [w for w in ALL_WORDS if re.match(r'^[A-Z]{3,14}$', w)]

print(f"Total vocabulary pool for crossword generation: {len(WORDS)} words.")

def build_puzzle(puzzle_id, title, collection, difficulty, grid_size, word_defs):
    rows = grid_size["rows"]
    cols = grid_size["cols"]
    grid = [["" for _ in range(cols)] for _ in range(rows)]
    
    validated_words = []
    for item in word_defs:
        w = item["word"].upper().replace(" ", "")
        r = item["row"]
        c = item["col"]
        d = item["direction"].lower()
        
        # Link vocabulary if available
        clue = item.get("clue")
        hint = item.get("hint")
        auth = item.get("authority")
        defn = item.get("definition")
        v_id = item.get("vocabId")
        
        if w in VOCAB_MAP:
            v = VOCAB_MAP[w]
            if not clue: clue = v["primaryClue"]
            if not hint: hint = v["additionalHint"]
            if not auth: auth = v["statuteOrAuthority"]
            if not defn: defn = v["definition"]
            if not v_id: v_id = v["id"]
        elif not clue:
            clue = f"Legal term: {w}"
            hint = f"Pertains to {collection}"
            auth = "Indian Legal Jurisprudence"
            defn = f"Key statutory concept in {collection}."
            
        # Verify grid placement
        if d == "across":
            if c + len(w) > cols:
                raise ValueError(f"[{puzzle_id}] Word '{w}' out of horizontal bounds at ({r}, {c})")
            for i, ch in enumerate(w):
                curr = grid[r][c + i]
                if curr != "" and curr != ch:
                    raise ValueError(f"[{puzzle_id}] Conflict at ({r}, {c+i}): existing '{curr}' vs '{ch}' for word '{w}'")
                grid[r][c + i] = ch
        elif d == "down":
            if r + len(w) > rows:
                raise ValueError(f"[{puzzle_id}] Word '{w}' out of vertical bounds at ({r}, {c})")
            for i, ch in enumerate(w):
                curr = grid[r + i][c]
                if curr != "" and curr != ch:
                    raise ValueError(f"[{puzzle_id}] Conflict at ({r+i}, {c}): existing '{curr}' vs '{ch}' for word '{word}'")
                grid[r + i][c] = ch
                
        validated_words.append({
            "word": w,
            "direction": d,
            "row": r,
            "col": c,
            "clue": clue,
            "hint": hint,
            "authority": auth or "Indian Judicial Precedent",
            "definition": defn or f"Legal term in {collection}.",
            "vocabId": v_id or ""
        })
        
    # Numbering
    coords = {}
    for w_obj in validated_words:
        pt = (w_obj["row"], w_obj["col"])
        if pt not in coords: coords[pt] = []
        coords[pt].append(w_obj)
        
    sorted_pts = sorted(coords.keys(), key=lambda pt: (pt[0], pt[1]))
    counter = 1
    for pt in sorted_pts:
        for w_obj in coords[pt]:
            w_obj["clueNum"] = counter
        counter += 1
        
    return {
        "id": puzzle_id,
        "title": title,
        "collection": collection,
        "difficulty": difficulty,
        "gridSize": grid_size,
        "words": validated_words,
        "solutionGrid": ["".join(row) for row in grid]
    }

print("Puzzle compiler loaded successfully.")
