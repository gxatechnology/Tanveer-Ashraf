import os
import json
import re

audit_report = []

def log(msg):
    audit_report.append(msg)
    print(msg)

log("# COMPREHENSIVE LEGAL CONTENT & DATASET AUDIT (PHASE 4 PREFLIGHT)")

# 1. Audit detective-cases.js
log("\n## 1. Audit of Detective Cases (assets/games/data/detective-cases.js)")
with open('assets/games/data/detective-cases.js', 'r', encoding='utf-8') as f:
    text = f.read()

cases_found = re.findall(r'id:\s*[\'"]([^\'"]+)[\'"]\s*,\s*caseNumber:\s*[\'"]([^\'"]+)[\'"]\s*,\s*title:\s*[\'"]([^\'"]+)[\'"]', text)
log(f"Total Cases Found: {len(cases_found)}")
for cid, cnum, ctitle in cases_found:
    log(f" - [{cid}] {cnum}: {ctitle}")

# Check legalVerification in each case
verifs = re.findall(r'legalVerification:\s*\{([^}]+)\}', text)
log(f"Legal Verification Blocks: {len(verifs)}")
for i, v in enumerate(verifs):
    act = re.search(r'act:\s*[\'"]([^\'"]+)[\'"]', v)
    sec = re.search(r'section:\s*[\'"]([^\'"]+)[\'"]', v)
    prop = re.search(r'proposition:\s*[\'"]([^\'"]+)[\'"]', v)
    src = re.search(r'source:\s*[\'"]([^\'"]+)[\'"]', v)
    vdate = re.search(r'verificationDate:\s*[\'"]([^\'"]+)[\'"]', v)
    log(f"   Case {i+1}: Act={act.group(1) if act else 'MISSING'}, Sec={sec.group(1) if sec else 'MISSING'}, Date={vdate.group(1) if vdate else 'MISSING'}")

# 2. Audit courtroom-cases.js
log("\n## 2. Audit of Courtroom Cases (assets/games/data/courtroom-cases.js)")
with open('assets/games/data/courtroom-cases.js', 'r', encoding='utf-8') as f:
    text = f.read()

court_cases = re.findall(r'id:\s*[\'"]([^\'"]+)[\'"]\s*,\s*caseNumber:\s*[\'"]([^\'"]+)[\'"]\s*,\s*title:\s*[\'"]([^\'"]+)[\'"]', text)
log(f"Total Courtroom Proceedings Found: {len(court_cases)}")
for cid, cnum, ctitle in court_cases:
    log(f" - [{cid}] {cnum}: {ctitle}")

court_verifs = re.findall(r'legalVerification:\s*\{([^}]+)\}', text)
log(f"Legal Verification Blocks: {len(court_verifs)}")
for i, v in enumerate(court_verifs):
    act = re.search(r'act:\s*[\'"]([^\'"]+)[\'"]', v)
    sec = re.search(r'section:\s*[\'"]([^\'"]+)[\'"]', v)
    src = re.search(r'source:\s*[\'"]([^\'"]+)[\'"]', v)
    vdate = re.search(r'verificationDate:\s*[\'"]([^\'"]+)[\'"]', v)
    log(f"   Proceeding {i+1}: Act={act.group(1) if act else 'MISSING'}, Sec={sec.group(1) if sec else 'MISSING'}, Citation={src.group(1) if src else 'MISSING'}")

# 3. Audit legal-vocabulary.js
log("\n## 3. Audit of Legal Vocabulary (assets/games/data/legal-vocabulary.js)")
with open('assets/games/data/legal-vocabulary.js', 'r', encoding='utf-8') as f:
    vocab_text = f.read()

# Extract VOCABULARY JSON-like array
match = re.search(r'const VOCABULARY\s*=\s*(\[\s*\{.*?\}\s*\]);', vocab_text, re.DOTALL)
if match:
    try:
        vocab = json.loads(match.group(1))
        log(f"Successfully parsed {len(vocab)} vocabulary items via JSON.")
        
        # Check IDs uniqueness
        ids = [v['id'] for v in vocab]
        unique_ids = set(ids)
        log(f"Unique IDs: {len(unique_ids)} / {len(ids)}")
        
        # Check Canonical uniqueness
        canonicals = [v['canonical'].upper().strip() for v in vocab]
        unique_canon = set(canonicals)
        log(f"Unique Canonical terms: {len(unique_canon)} / {len(canonicals)}")
        if len(unique_canon) != len(canonicals):
            dups = [c for c in unique_canon if canonicals.count(c) > 1]
            log(f"Duplicate Canonical Terms: {dups}")
            
        # Discipline distribution
        subjects = {}
        for v in vocab:
            s = v.get('subject', 'Unknown')
            subjects[s] = subjects.get(s, 0) + 1
        log("Subject Distribution:")
        for s, c in sorted(subjects.items(), key=lambda x: -x[1]):
            log(f"   {s}: {c} terms")
            
        # Missing fields check
        missing_fields = []
        req_keys = ['id', 'canonical', 'difficulty', 'subject', 'primaryClue', 'definition', 'statuteOrAuthority', 'sourceUrl', 'verificationDate']
        for v in vocab:
            for k in req_keys:
                if not v.get(k):
                    missing_fields.append((v.get('id'), k))
        log(f"Total missing required fields across {len(vocab)} items: {len(missing_fields)}")
        
        # Source URLs check
        urls = [v.get('sourceUrl', '') for v in vocab]
        generic_india_code = [u for u in urls if '123456789/1522' in u]
        log(f"Specific URLs: {len(urls) - len(generic_india_code)}, Generic handle/1522 URLs: {len(generic_india_code)}")
    except Exception as e:
        log(f"JSON parse error: {e}")
else:
    log("Could not extract VOCABULARY array with regex.")

# 4. Audit crossword-puzzles.js
log("\n## 4. Audit of Crossword Puzzles (assets/games/data/crossword-puzzles.js)")
with open('assets/games/data/crossword-puzzles.js', 'r', encoding='utf-8') as f:
    cw_text = f.read()

cw_match = re.search(r'const CROSSWORD_PUZZLES\s*=\s*(\[\s*\{.*?\}\s*\]);', cw_text, re.DOTALL)
if cw_match:
    try:
        puzzles = json.loads(cw_match.group(1))
        log(f"Successfully parsed {len(puzzles)} crossword puzzles.")
        
        diffs = {}
        conflict_count = 0
        total_intersections = 0
        
        for p in puzzles:
            d = p.get('difficulty', 'unknown')
            diffs[d] = diffs.get(d, 0) + 1
            
            # Verify grid cells
            grid = {}
            for w in p['words']:
                r, c = w['startRow'], w['startCol']
                word_str = w['word']
                for idx, ch in enumerate(word_str):
                    cr = r + idx if w['direction'] == 'down' else r
                    cc = c if w['direction'] == 'down' else c + idx
                    if (cr, cc) in grid:
                        total_intersections += 1
                        if grid[(cr, cc)] != ch:
                            conflict_count += 1
                    else:
                        grid[(cr, cc)] = ch
                        
        log(f"Difficulty breakdown: {diffs}")
        log(f"Total Intersections Verified: {total_intersections}, Conflicting Cells: {conflict_count}")
    except Exception as e:
        log(f"Crossword JSON parse error: {e}")

with open('scripts/preflight_audit_output.txt', 'w', encoding='utf-8') as out_f:
    out_f.write('\n'.join(audit_report))
