import re
import os

def check_file(path, label):
    if not os.path.exists(path):
        print(f"MISSING: {path}")
        return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"\n=== {label} ({path}) ===")
    print(f"Size: {len(content):,} bytes")
    
    # Check verificationDate
    dates = re.findall(r'["\']?verificationDate["\']?\s*:\s*["\']([^"\']+)["\']', content)
    print(f"verificationDate occurrences: {len(dates)}")
    if dates:
        print(f"Sample verification dates: {list(set(dates))[:5]}")
        
    # Check sourceUrl
    urls = re.findall(r'["\']?sourceUrl["\']?\s*:\s*["\']([^"\']+)["\']', content)
    print(f"sourceUrl occurrences: {len(urls)}")
    if urls:
        print(f"Sample source URLs: {urls[:3]}")

    # Check for statutes mentioned
    bns_mentions = len(re.findall(r'\bBNS\b|Bharatiya Nyaya Sanhita', content))
    ipc_mentions = len(re.findall(r'\bIPC\b|Indian Penal Code', content))
    bsa_mentions = len(re.findall(r'\bBSA\b|Bharatiya Sakshya', content))
    cpc_mentions = len(re.findall(r'\bCPC\b|Civil Procedure', content))
    crpc_mentions = len(re.findall(r'\bCrPC\b|Criminal Procedure', content))
    print(f"Statutory citations: BNS={bns_mentions}, IPC={ipc_mentions}, BSA={bsa_mentions}, CPC={cpc_mentions}, CrPC={crpc_mentions}")

check_file('assets/games/data/detective-cases.js', 'Detective Cases')
check_file('assets/games/data/courtroom-cases.js', 'Courtroom Cases')
check_file('assets/games/data/legal-vocabulary.js', 'Legal Vocabulary')
check_file('assets/games/data/crossword-puzzles.js', 'Crossword Puzzles')
check_file('assets/games/data/legal-game-content.js', 'Legal Game Content')
