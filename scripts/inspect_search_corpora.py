txt = open('assets/js/legal-search.js', encoding='utf-8').read()
for i, line in enumerate(txt.splitlines()):
    if any(k in line for k in ['ARENA_', 'corpus', 'search', 'results']):
        print(f"{i}: {line[:90]}")
