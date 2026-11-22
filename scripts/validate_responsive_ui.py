#!/usr/bin/env python3
"""
MASTER RESPONSIVE UI & UNIVERSAL RIGHT-SIDE DRAWER VALIDATION SUITE
Project: Tanveer Ashraf - Judicial Prep 2026-27 (V3.1.7)
Lead Developer: Tauqeer Ashraf
Candidate: Tanveer Ashraf
"""

import os
import re
import glob
import json
import subprocess

def run_tests():
    print("=" * 75)
    print("MASTER RESPONSIVE UI & UNIVERSAL RIGHT-SIDE DRAWER VALIDATION SUITE")
    print("=" * 75)

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

    # 1. Check all 27 HTML files exist
    html_files = sorted(glob.glob('*.html'))
    check("Operational HTML page count is exactly 27", len(html_files) == 27, f"Found {len(html_files)}")

    # 2. Check all 27 HTML pages include the menuToggleBtn
    missing_btn = []
    for hf in html_files:
        with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
        if 'menuToggleBtn' not in c:
            missing_btn.append(hf)
    check("All 27 HTML pages have top-right hamburger button (#menuToggleBtn)", len(missing_btn) == 0, str(missing_btn))

    # 3. Check all 27 HTML pages include nav-drawer.js
    missing_script = []
    for hf in html_files:
        with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
        if 'nav-drawer.js' not in c:
            missing_script.append(hf)
    check("All 27 HTML pages include assets/js/nav-drawer.js", len(missing_script) == 0, str(missing_script))

    # 4. Check all 27 HTML pages include nav-drawer.css (either linked or bundled)
    missing_css = []
    for hf in html_files:
        with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
        if 'nav-drawer.css' not in c and 'site.css' not in c:
            missing_css.append(hf)
    check("All 27 HTML pages load nav-drawer styling", len(missing_css) == 0, str(missing_css))

    # 5. Check nav-drawer.css exists and contains right-side drawer positioning
    with open('assets/css/nav-drawer.css', 'r', encoding='utf-8') as f:
        nd_css = f.read()
    check("nav-drawer.css exists and defines .menu-toggle-btn", ".menu-toggle-btn" in nd_css)
    check("nav-drawer.css defines right-side slide .nav-drawer with right: 0", "right: 0" in nd_css and "transform: translateX(100%)" in nd_css)
    check("nav-drawer.css defines .drawer-backdrop", ".drawer-backdrop" in nd_css)
    check("nav-drawer.css defines body.drawer-open scroll lock", "body.drawer-open" in nd_css and "overflow: hidden" in nd_css)
    check("nav-drawer.css respects prefers-reduced-motion", "prefers-reduced-motion" in nd_css)

    # 6. Check site.css has nav-drawer styles bundled
    with open('assets/css/site.css', 'r', encoding='utf-8') as f:
        site_css = f.read()
    check("site.css bundles nav-drawer styles", "NAV DRAWER STYLES" in site_css)

    # 7. Check nav-drawer.js exists and defines all 13 valid routes
    with open('assets/js/nav-drawer.js', 'r', encoding='utf-8') as f:
        nd_js = f.read()
    check("nav-drawer.js defines DRAWER_ROUTES", "DRAWER_ROUTES" in nd_js)
    
    # Parse routes from nav-drawer.js
    routes_in_drawer = re.findall(r'href:\s*["\']([^"\']+)["\']', nd_js)
    missing_drawer_targets = [r for r in routes_in_drawer if not os.path.exists(r)]
    check("All routes in nav-drawer.js point to existing HTML files on disk", len(missing_drawer_targets) == 0, str(missing_drawer_targets))
    check("nav-drawer.js includes Subject Academy route", "learning-academy.html" in routes_in_drawer)
    check("nav-drawer.js includes Civil Suit Journey route", "civil-suit-journey.html" in routes_in_drawer)
    check("nav-drawer.js includes Comparison Lab route", "comparison-lab.html" in routes_in_drawer)

    # 8. Check accessibility features in nav-drawer.js
    check("nav-drawer.js has keyboard focus trap (Tab key handling)", "e.key === 'Tab'" in nd_js or "e.key === 'Escape'" in nd_js)
    check("nav-drawer.js supports Escape key to close", "e.key === 'Escape'" in nd_js)
    check("nav-drawer.js restores focus on close", "lastFocusedElement.focus()" in nd_js)
    check("nav-drawer.js manages ARIA attributes (aria-expanded, aria-hidden)", "aria-expanded" in nd_js and "aria-hidden" in nd_js)

    # 9. Test Curriculum & Drawer Navigation for all 17 Active Subjects in Node
    res_curr = subprocess.run(['node', 'scripts/test_subject_curriculum_drawer.js'], capture_output=True, encoding='utf-8', errors='replace')
    check("Node evaluation of all 17 subject curricula in drawer succeeded", res_curr.returncode == 0, res_curr.stderr)

    # 10. Check subject-study.html layout and empty parentheses fix
    with open('subject-study.html', 'r', encoding='utf-8') as f:
        study_html = f.read()
    check("subject-study.html uses minmax(0, 1fr) for .study-layout", "grid-template-columns: 280px minmax(0, 1fr)" in study_html)
    check("subject-study.html defines min-width: 0 on .study-main-pane", "min-width: 0" in study_html)
    check("subject-study.html defines overflow-x: auto on .table-responsive", "overflow-x: auto" in study_html)
    
    # Check that empty parentheses are not hardcoded or unhandled
    has_empty_parens_bug = 'Analysis (${subject.code || \'\'})' in study_html
    check("subject-study.html omits empty parentheses when subject.code is absent", not has_empty_parens_bug)

    # 11. Check concept-renderer.js table-responsive wrapper
    with open('assets/learning/js/concept-renderer.js', 'r', encoding='utf-8') as f:
        cr_js = f.read()
    check("concept-renderer.js wraps comparison tables with overflow-x: auto", "table-responsive" in cr_js and "overflow-x:auto" in cr_js)

    # 12. Check academy.css responsive grid and table constraints
    with open('assets/learning/css/academy.css', 'r', encoding='utf-8') as f:
        acad_css = f.read()
    check("academy.css sets .cases-grid with responsive minmax(min(100%, 320px), 1fr)", "minmax(min(100%, 320px), 1fr)" in acad_css)
    check("academy.css sets .flashcards-deck with responsive minmax(min(100%, 280px), 1fr)", "minmax(min(100%, 280px), 1fr)" in acad_css)
    check("academy.css sets .table-responsive with overflow-x: auto", ".table-responsive" in acad_css and "overflow-x: auto" in acad_css)
    check("academy.css sets word-break / overflow-wrap on study titles", "overflow-wrap: break-word" in acad_css)

    print("=" * 75)
    print(f"RESPONSIVE UI VALIDATION SUMMARY: {passes} PASSED, {failures} FAILED")
    print("=" * 75)
    return failures == 0

if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)
