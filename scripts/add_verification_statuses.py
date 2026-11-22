import re

# 1. Update legal-vocabulary.js
with open('assets/games/data/legal-vocabulary.js', 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'("verificationDate":\s*"2026-11-22")', r'\1,\n    "status": "Verified against authoritative source"', text)
with open('assets/games/data/legal-vocabulary.js', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated legal-vocabulary.js with status field!")

# 2. Update legal-myths.js
with open('assets/games/data/legal-myths.js', 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'("verificationDate":\s*"2026-11-22")', r'\1,\n    "status": "Verified against authoritative source"', text)
with open('assets/games/data/legal-myths.js', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated legal-myths.js with status field!")
