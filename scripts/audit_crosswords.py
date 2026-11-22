import json
import re

with open('assets/games/data/crossword-puzzles.js', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'const PUZZLES\s*=\s*(\[\s*\{.*?\}\s*\]);', text, re.DOTALL)
if match:
    puzzles = json.loads(match.group(1))
    print(f"Total Crossword Puzzles: {len(puzzles)}")
    diffs = {}
    total_words = 0
    total_intersections = 0
    conflict_count = 0
    
    for p in puzzles:
        d = p['difficulty']
        diffs[d] = diffs.get(d, 0) + 1
        total_words += len(p['words'])
        
        # Check intersection
        grid = {}
        for w in p['words']:
            r, c = w['row'], w['col']
            direction = w['direction']
            word_str = w['word']
            for i, ch in enumerate(word_str):
                cr = r + i if direction == 'down' else r
                cc = c if direction == 'down' else c + i
                if (cr, cc) in grid:
                    total_intersections += 1
                    if grid[(cr, cc)] != ch:
                        conflict_count += 1
                        print(f"Conflict in puzzle {p['id']} at ({cr}, {cc}): expected {grid[(cr,cc)]}, got {ch} in word {word_str}")
                else:
                    grid[(cr, cc)] = ch
                    
    print(f"Difficulty Breakdown: {diffs}")
    print(f"Total Words Across 30 Puzzles: {total_words}")
    print(f"Total Intersecting Letter Cells: {total_intersections}")
    print(f"Conflicting Cells: {conflict_count}")
    
    # Check sample clue
    p0 = puzzles[0]
    print(f"\nSample Puzzle [{p0['id']}] {p0['title']} ({p0['collection']}):")
    for w in p0['words'][:3]:
        print(f" - {w['direction'].upper()} ({w['row']},{w['col']}): {w['word']} | Clue: {w['clue']} | Authority: {w.get('authority')}")
else:
    print("Could not match const PUZZLES regex.")
