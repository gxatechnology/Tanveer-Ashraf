txt = open('scripts/validate_production.py', encoding='utf-8').read()
for i, line in enumerate(txt.splitlines()[:50]):
    if 'html' in line.lower() or '21' in line:
        print(f"{i}: {line}")
