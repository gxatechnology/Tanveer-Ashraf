import re

with open('assets/learning/data/social/social-sections-explorer.js', 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'("actId":\s*"(soc-[^"]+)")', r'\1,\n    "subjectId": "\2"', text)

with open('assets/learning/data/social/social-sections-explorer.js', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated social-sections-explorer.js with subjectId alias')
