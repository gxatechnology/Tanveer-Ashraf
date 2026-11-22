txt = open('assets/js/app.js', encoding='utf-8').read()
for i, line in enumerate(txt.splitlines()):
    if 'function exportProgress' in line or 'function importProgress' in line or 'exportProgress =' in line:
        print(f"Line {i}: {line}")
        print("\n".join(txt.splitlines()[i:i+40]))
