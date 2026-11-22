import re

with open('scripts/mcq_batch_1.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace specific unescaped single quotes
replacements = [
    ('lawyer\'s paradise', 'lawyer\\\'s paradise'),
    ('Wheare\'s quasi-federal', 'Wheare\\\'s quasi-federal'),
    ('Austin\'s conscience', 'Austin\\\'s conscience'),
    ('St. Xavier\'s College', 'St. Xavier\\\'s College'),
    ('Barker\'s Tribute', 'Barker\\\'s Tribute'),
    ('Preamble\'s', 'Preamble\\\'s')
]

for old, new in replacements:
    text = text.replace(old, new)

with open('scripts/mcq_batch_1.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Replacement done.")
