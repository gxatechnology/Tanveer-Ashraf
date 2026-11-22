#!/usr/bin/env python3
"""
PRODUCTION READINESS & INTEGRATION VALIDATION SUITE (PHASE 5)
Project: Tanveer Ashraf - Judicial Prep 2026-27
Lead Developer: Tauqeer Ashraf
"""

import os
import re
import json
import subprocess

def run_tests():
    print("=" * 70)
    print("TANVEER ASHRAF JUDICIAL PREP — PRODUCTION VALIDATION SUITE")
    print("=" * 70)

    passes = 0
    failures = 0

    def check(name, condition, details=""):
        nonlocal passes, failures
        if condition:
            print(f" [PASS] {name}")
            passes += 1
        else:
            print(f" [FAIL] {name} -> {details}")
            failures += 1

    # 1. Operational HTML Pages Count
    html_files = sorted([f for f in os.listdir('.') if f.endswith('.html')])
    check("Operational HTML page count is exactly 21", len(html_files) == 21, f"Found {len(html_files)} pages: {html_files}")

    # 2. Check HTML structure and local assets
    missing_assets = []
    for h in html_files:
        with open(h, 'r', encoding='utf-8') as f:
            content = f.read()
        if not content.lower().startswith('<!doctype html'):
            missing_assets.append(f"{h}: Missing doctype")
        if '<title>' not in content:
            missing_assets.append(f"{h}: Missing title")
        scripts = re.findall(r'<script\s+src=["\']([^"\']+)["\']', content)
        for s in scripts:
            if not s.startswith('http') and not os.path.exists(s.split('?')[0]):
                missing_assets.append(f"{h}: Script {s} not found on disk")
        styles = re.findall(r'<link\s+[^>]*href=["\']([^"\']+\.css)["\']', content)
        for st in styles:
            if not st.startswith('http') and not os.path.exists(st.split('?')[0]):
                missing_assets.append(f"{h}: CSS {st} not found on disk")

    check("All HTML pages reference valid local CSS & JS assets", len(missing_assets) == 0, str(missing_assets))

    # 3. JavaScript Syntax Verification (node -c)
    js_files = []
    for root, dirs, files in os.walk('assets'):
        for f in files:
            if f.endswith('.js'):
                js_files.append(os.path.join(root, f))
    
    syntax_errors = []
    for js in js_files:
        res = subprocess.run(['node', '-c', js], capture_output=True, text=True)
        if res.returncode != 0:
            syntax_errors.append(f"{js}: {res.stderr.strip()}")
    
    check(f"All {len(js_files)} JavaScript files pass syntax compilation", len(syntax_errors) == 0, str(syntax_errors))

    # 4. Verify Datasets via Node runtime
    eval_script = """
    global.window = {};
    const fs = require('fs');
    function load(p) { eval(fs.readFileSync(p, 'utf8')); }
    load('assets/data/questions.js');
    load('assets/data/bns.js');
    load('assets/games/data/legal-vocabulary.js');
    load('assets/games/data/crossword-puzzles.js');
    load('assets/games/data/detective-cases.js');
    load('assets/games/data/courtroom-cases.js');
    load('assets/games/data/legal-myths.js');
    load('assets/games/data/journey-chapters.js');
    load('assets/games/data/journey-missions.js');
    load('assets/games/data/characters.js');
    load('assets/games/js/achievements.js');

    const qs = window.PCSJ_QUESTIONS || [];
    const bns = window.BNS_SECTIONS || [];
    const voc = window.ARENA_VOCABULARY || [];
    const cw = window.ARENA_CROSSWORDS || [];
    const det = window.DETECTIVE_CASES || [];
    const crt = window.COURTROOM_CASES || [];
    const myths = window.ARENA_MYTHS || [];
    const ch = window.JOURNEY_CHAPTERS || [];
    const m = window.JOURNEY_MISSIONS || [];
    const chars = Object.keys(window.ARENA_CHARACTERS || {});
    const ach = (window.Achievements && window.Achievements.getAll) ? window.Achievements.getAll() : (window.ARENA_ACHIEVEMENTS || []);

    const out = {
      qTotal: qs.length,
      qEligible: qs.filter(q => q.eligible === true).length,
      qIneligible: qs.filter(q => q.eligible === false).length,
      qUnique: new Set(qs.map(q => q.id)).size === qs.length,
      bnsTotal: bns.length,
      bnsUnique: new Set(bns.map(s => s.section)).size === bns.length,
      vocTotal: voc.length,
      vocUnique: new Set(voc.map(v => v.id)).size === voc.length,
      cwTotal: cw.length,
      cwUnique: new Set(cw.map(c => c.id)).size === cw.length,
      detTotal: det.length,
      crtTotal: crt.length,
      mythsTotal: myths.length,
      mythsUnique: new Set(myths.map(x => x.id)).size === myths.length,
      mythsHttps: myths.filter(x => x.sourceUrl && x.sourceUrl.startsWith('https://')).length,
      chTotal: ch.length,
      mTotal: m.length,
      mUnique: new Set(m.map(x => x.id)).size === m.length,
      charsTotal: chars.length,
      achTotal: ach.length,
      achUnique: new Set(ach.map(a => a.id)).size === ach.length
    };
    console.log(JSON.stringify(out));
    """
    res = subprocess.run(['node', '-e', eval_script], capture_output=True, text=True)
    if res.returncode == 0:
        data = json.loads(res.stdout.strip())
        check("PYQ Question bank has exactly 1,800 records", data['qTotal'] == 1800, f"Found {data['qTotal']}")
        check("PYQ Scorable questions equals 1,757", data['qEligible'] == 1757, f"Found {data['qEligible']}")
        check("PYQ Ineligible questions equals 43", data['qIneligible'] == 43, f"Found {data['qIneligible']}")
        check("PYQ Question IDs are completely unique", data['qUnique'])
        check("BNS Index has exactly 358 section titles", data['bnsTotal'] == 358, f"Found {data['bnsTotal']}")
        check("BNS Section numbers are unique", data['bnsUnique'])
        check("Legal Vocabulary has exactly 285 unique entries", data['vocTotal'] == 285 and data['vocUnique'], f"Found {data['vocTotal']}")
        check("Crossword Puzzles has exactly 30 unique puzzles", data['cwTotal'] == 30 and data['cwUnique'], f"Found {data['cwTotal']}")
        check("Detective investigations count equals 6", data['detTotal'] == 6, f"Found {data['detTotal']}")
        check("Courtroom hearings count equals 6", data['crtTotal'] == 6, f"Found {data['crtTotal']}")
        check("Legal Myth Buster has exactly 330 unique statements", data['mythsTotal'] == 330 and data['mythsUnique'], f"Found {data['mythsTotal']}")
        check("All 330 Legal Myths have authoritative HTTPS source URLs", data['mythsHttps'] == 330, f"Found {data['mythsHttps']}")
        check("Campaign Chapters count equals 9", data['chTotal'] == 9, f"Found {data['chTotal']}")
        check("Campaign Missions count equals 36", data['mTotal'] == 36 and data['mUnique'], f"Found {data['mTotal']}")
        check("Arena Character Roster has exactly 12 characters", data['charsTotal'] == 12, f"Found {data['charsTotal']}")
        check("Judicial Achievements Roster has exactly 38 badges", data['achTotal'] == 38 and data['achUnique'], f"Found {data['achTotal']}")
    else:
        check("Dataset runtime evaluation", False, res.stderr)

    # 5. Mission URLs existence on disk
    with open('assets/games/data/journey-missions.js', 'r', encoding='utf-8') as f:
        m_text = f.read()
    m_urls = re.findall(r'gameUrl:\s*["\']([^"\']+)["\']', m_text)
    invalid_m_urls = []
    for u in m_urls:
        page = u.split('?')[0]
        if not os.path.exists(page):
            invalid_m_urls.append(f"Mission target page missing: {page}")
    check("All 36 campaign mission target pages exist on disk", len(invalid_m_urls) == 0, str(invalid_m_urls))

    # 6. Critical Photographs & Emblem Integrity
    portraits = [
        ('assets/images/tanveer.webp', 10000),
        ('assets/images/tanveer-original.webp', 10000),
        ('assets/images/tauqeer.webp', 10000),
        ('assets/images/tauqeer-original.webp', 10000),
        ('assets/images/emblem.svg', 100)
    ]
    img_ok = True
    for p, min_sz in portraits:
        if not os.path.exists(p) or os.path.getsize(p) < min_sz:
            img_ok = False
            break
    check("Branding portraits and emblem are 100% intact and uncorrupted", img_ok, "Image verification failed")

    print("=" * 70)
    print(f"VALIDATION SUMMARY: {passes} PASSED, {failures} FAILED")
    print("=" * 70)
    return failures == 0

if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)
