import re
import os
import json

print("=== PHASE 5 COMPLETE INVENTORY AUDIT ===")

# 1. HTML Pages
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
print(f"Total HTML Pages: {len(html_files)}")

# 2. Questions
with open('assets/data/questions.js', 'r', encoding='utf-8') as f:
    q_text = f.read()
q_matches = re.findall(r'id:\s*["\']([^"\']+)["\']', q_text)
q_eligible = re.findall(r'eligible:\s*true', q_text)
q_ineligible = re.findall(r'eligible:\s*false', q_text)
print(f"Total PYQ records: {len(q_matches)}")
print(f"Scorable PYQ records (eligible: true): {len(q_eligible)}")
print(f"Review-only PYQ records (eligible: false): {len(q_ineligible)}")

# 3. BNS Sections
with open('assets/data/bns.js', 'r', encoding='utf-8') as f:
    bns_text = f.read()
bns_matches = re.findall(r'section:\s*["\']?(\d+[A-Z]?)["\']?', bns_text)
print(f"Total BNS section records: {len(bns_matches)}")

# 4. Legal Vocabulary
with open('assets/games/data/legal-vocabulary.js', 'r', encoding='utf-8') as f:
    vocab_text = f.read()
vocab_ids = re.findall(r'id:\s*["\']([^"\']+)["\']\s*,\s*term:', vocab_text)
print(f"Total Legal Vocabulary entries: {len(vocab_ids)}")

# 5. Crossword Puzzles
with open('assets/games/data/crossword-puzzles.js', 'r', encoding='utf-8') as f:
    cw_text = f.read()
cw_ids = re.findall(r'id:\s*["\'](puzzle-\d+)["\']', cw_text)
print(f"Total Crossword Puzzles: {len(cw_ids)}")

# 6. Detective Cases
with open('assets/games/data/detective-cases.js', 'r', encoding='utf-8') as f:
    det_text = f.read()
det_ids = re.findall(r'id:\s*["\'](det-case-\d+)["\']', det_text)
print(f"Total Detective Cases: {len(det_ids)}")

# 7. Courtroom Hearings
with open('assets/games/data/courtroom-cases.js', 'r', encoding='utf-8') as f:
    crt_text = f.read()
crt_ids = re.findall(r'id:\s*["\'](court-case-\d+)["\']', crt_text)
print(f"Total Courtroom Hearings: {len(crt_ids)}")

# 8. Myth Buster Statements
with open('assets/games/data/legal-myths.js', 'r', encoding='utf-8') as f:
    myth_text = f.read()
myth_ids = re.findall(r'id:\s*["\'](myth-\d+)["\']', myth_text)
print(f"Total Myth Buster Statements: {len(myth_ids)}")

# 9. Campaign Chapters
with open('assets/games/data/journey-chapters.js', 'r', encoding='utf-8') as f:
    ch_text = f.read()
ch_ids = re.findall(r'id:\s*["\'](chapter-\d+)["\']', ch_text)
print(f"Total Campaign Chapters: {len(ch_ids)}")

# 10. Campaign Missions
with open('assets/games/data/journey-missions.js', 'r', encoding='utf-8') as f:
    m_text = f.read()
m_ids = re.findall(r'id:\s*["\'](m\d+-\d+)["\']', m_text)
print(f"Total Campaign Missions: {len(m_ids)}")

# 11. Characters
with open('assets/games/data/characters.js', 'r', encoding='utf-8') as f:
    char_text = f.read()
char_ids = re.findall(r'id:\s*["\']([a-z0-9_-]+)["\']\s*,\s*name:', char_text)
print(f"Total Characters: {len(char_ids)}")

# 12. Achievements
with open('assets/games/js/achievements.js', 'r', encoding='utf-8') as f:
    ach_text = f.read()
ach_ids = re.findall(r'id:\s*["\']([a-z0-9_-]+)["\']\s*,\s*title:', ach_text)
print(f"Total Achievements: {len(ach_ids)}")
