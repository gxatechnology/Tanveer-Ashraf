#!/usr/bin/env python3
"""
NAVIGATION ROUTE INTEGRITY REGRESSION TEST SUITE
Project: Tanveer Ashraf - Judicial Prep 2026-27
Lead Developer: Tauqeer Ashraf
"""

import os
import re
import glob
import subprocess
import json

def run_tests():
    print("=" * 70)
    print("NAVIGATION ROUTE INTEGRITY & REGRESSION TEST SUITE")
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

    # 1. Parse routes object from assets/js/app.js
    app_js = open('assets/js/app.js', encoding='utf-8').read()
    routes_match = re.search(r'const\s+routes\s*=\s*\{([^}]+)\}', app_js)
    check("routes object exists in assets/js/app.js", routes_match is not None)

    routes = {}
    if routes_match:
        for item in routes_match.group(1).split(','):
            item = item.strip()
            if ':' in item:
                k, v = item.split(':', 1)
                k = k.strip()
                v = v.strip().strip("'\"")
                routes[k] = v

    check("academy route is defined in routes", 'academy' in routes and routes['academy'] == 'learning-academy.html', f"Got: {routes.get('academy')}")
    check("journey route is defined in routes", 'journey' in routes and routes['journey'] == 'civil-suit-journey.html', f"Got: {routes.get('journey')}")
    check("comparison route is defined in routes", 'comparison' in routes and routes['comparison'] == 'comparison-lab.html', f"Got: {routes.get('comparison')}")

    # 2. Check all routes point to existing files
    missing_targets = []
    for k, v in routes.items():
        if not os.path.exists(v):
            missing_targets.append(f"{k} -> {v}")
    check("All routes map to files that exist on disk", len(missing_targets) == 0, str(missing_targets))

    # 3. Check every data-view across all HTML files exists in routes
    all_html_files = sorted(glob.glob('*.html'))
    unmapped_views = []
    for hf in all_html_files:
        c = open(hf, encoding='utf-8', errors='ignore').read()
        for m in re.finditer(r'data-view=["\']([^"\']+)["\']', c):
            dv = m.group(1)
            if dv not in routes:
                unmapped_views.append(f"{hf}: {dv}")
    check("Every data-view in all 27 HTML pages is mapped in routes", len(unmapped_views) == 0, str(unmapped_views))

    # 4. Check defensive navigation guard in app.js
    has_guard = 'DEFENSIVE NAVIGATION GUARD' in app_js and 'undefined' in app_js and 'targetRoute' in app_js
    check("Defensive navigation guard exists in app.js", has_guard)

    # 5. Check native link fallback in app.js click handler
    has_native_fallback = 'b.onclick' in app_js and 'href' in app_js and '!routes[v]' in app_js
    check("Native link fallback exists when route is unhandled", has_native_fallback)

    # 6. Test defensive guard in Node runtime (simulate edge cases)
    node_test = """
    const vm = require('vm');
    const fs = require('fs');

    global.window = { addEventListener: () => {}, scrollTo: () => {} };
    global.document = { querySelectorAll: () => [], getElementById: () => ({ textContent: '', innerHTML: '' }), body: { dataset: {} } };
    global.location = { href: 'http://localhost/' };
    global.confirm = () => true;
    global.console = { warn: () => {}, log: () => {} };

    let capturedUrl = null;
    let loggedWarnings = [];
    global.console.warn = (msg, arg) => { loggedWarnings.push({ msg, arg }); };
    Object.defineProperty(global.location, 'href', {
      get: () => capturedUrl,
      set: (val) => { capturedUrl = val; }
    });

    global.window.PCSJ_QUESTIONS = [];
    global.window.ACADEMY_SUBJECTS = [];
    global.localStorage = { getItem: () => null, setItem: () => null };

    const code = fs.readFileSync('assets/js/app.js', 'utf8');
    vm.runInThisContext(code);

    const results = [];

    // Test 1: go('academy')
    capturedUrl = null;
    go('academy');
    results.push({ test: 'go(academy)', url: capturedUrl, expected: 'learning-academy.html' });

    // Test 2: go('nonexistent') - must NOT set location.href to 'undefined'
    capturedUrl = 'PRESERVED_URL';
    go('nonexistent');
    results.push({ test: 'go(nonexistent)', url: capturedUrl, expected: 'PRESERVED_URL', warnings: loggedWarnings.length > 0 });

    // Test 3: go(null) - must NOT set location.href to 'null'
    capturedUrl = 'PRESERVED_URL';
    go(null);
    results.push({ test: 'go(null)', url: capturedUrl, expected: 'PRESERVED_URL' });

    // Test 4: go(undefined) - must NOT set location.href to 'undefined'
    capturedUrl = 'PRESERVED_URL';
    go(undefined);
    results.push({ test: 'go(undefined)', url: capturedUrl, expected: 'PRESERVED_URL' });

    // Test 5: go('unknown', 'valid-page.html') - fallback href works
    capturedUrl = null;
    go('unknown', 'valid-page.html');
    results.push({ test: 'go(unknown, fallback)', url: capturedUrl, expected: 'valid-page.html' });

    process.stdout.write(JSON.stringify(results));
    """
    res = subprocess.run(['node', '-e', node_test], capture_output=True, encoding='utf-8', errors='replace')
    check("Node evaluation of navigation guards succeeded", res.returncode == 0, res.stderr)

    if res.returncode == 0:
        out_tests = json.loads(res.stdout.strip())
        for ot in out_tests:
            is_ok = (ot['url'] == ot['expected'])
            check(f"Runtime Guard: {ot['test']} -> {ot['url']}", is_ok, f"Expected {ot['expected']}")

    # 7. Check all internal links across all 27 HTML pages
    broken_links = []
    total_links = 0
    for hf in all_html_files:
        content = open(hf, encoding='utf-8', errors='ignore').read()
        hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
        for h in hrefs:
            total_links += 1
            if h.startswith('http://') or h.startswith('https://') or h.startswith('#') or h.startswith('mailto:') or h.startswith('javascript:'):
                continue
            base_path = h.split('?')[0].split('#')[0]
            if not base_path:
                continue
            if not os.path.exists(base_path):
                broken_links.append((hf, h, base_path))

    check(f"All {total_links} internal href links resolve to existing files", len(broken_links) == 0, str(broken_links))

    # 8. Check Dashboard baseline metrics calculation & fallback
    check("Dashboard in app.js references getAcademyStats", "getAcademyStats" in app_js)
    check("Dashboard in app.js fallback defines activeSubjects: 22", "activeSubjects: 22" in app_js)
    check("Dashboard in app.js fallback defines chapters: 192", "chapters: 192" in app_js)
    check("Dashboard in app.js fallback defines topics: 535", "topics: 535" in app_js)
    check("Dashboard in app.js fallback defines mcqs: 3775", "mcqs: 3775" in app_js)
    check("Dashboard in app.js fallback defines pyqs: 843", "pyqs: 843" in app_js)

    # 9. Test runtime home() HTML output with subjects.js
    node_home_test = """
    const vm = require('vm');
    const fs = require('fs');

    global.window = { addEventListener: () => {}, scrollTo: () => {} };
    const contentBox = { innerHTML: '' };
    global.document = {
      querySelectorAll: () => [],
      getElementById: (id) => (id === 'content' ? contentBox : { textContent: '', innerHTML: '' }),
      body: { dataset: { page: 'home' } }
    };
    global.location = { href: 'http://localhost/' };
    global.confirm = () => true;
    global.console = { warn: () => {}, log: () => {} };
    global.localStorage = { getItem: () => null, setItem: () => null };

    vm.runInThisContext(fs.readFileSync('assets/data/questions.js', 'utf8'));
    vm.runInThisContext(fs.readFileSync('assets/learning/data/subjects.js', 'utf8'));
    vm.runInThisContext(fs.readFileSync('assets/js/app.js', 'utf8'));

    home();
    process.stdout.write(contentBox.innerHTML);
    """
    res_home = subprocess.run(['node', '-e', node_home_test], capture_output=True, encoding='utf-8', errors='replace')
    check("home() renders cleanly with subjects.js in Node", res_home.returncode == 0, res_home.stderr)
    if res_home.returncode == 0:
        html_out = res_home.stdout
        check("home() renders '22 Active Production Modules'", "22 Active Production Modules" in html_out)
        check("home() renders '192 Chapters'", "192 Chapters" in html_out)
        check("home() renders '535 Topics'", "535 Topics" in html_out)
        check("home() renders '3,775 Practice MCQs'", "3,775 Practice MCQs" in html_out)
        check("home() renders '843 Mapped Historical PYQs'", "843 Mapped Historical PYQs" in html_out)

    print("=" * 70)
    print(f"NAVIGATION REGRESSION SUMMARY: {passes} PASSED, {failures} FAILED")
    print("=" * 70)
    return failures == 0

if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)
