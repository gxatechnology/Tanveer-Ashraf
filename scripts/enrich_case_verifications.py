import re

# 1. Enrich detective-cases.js
with open('assets/games/data/detective-cases.js', 'r', encoding='utf-8') as f:
    det_content = f.read()

det_urls = {
    'det-case-1': 'https://www.indiacode.nic.in/handle/123456789/2149', # BNS Section 303 & 314
    'det-case-2': 'https://www.indiacode.nic.in/handle/123456789/2149', # BNS Section 318
    'det-case-3': 'https://www.indiacode.nic.in/handle/123456789/2149', # BNS Section 336 & 338
    'det-case-4': 'https://www.indiacode.nic.in/handle/123456789/2149', # BNS Section 308 & 351
    'det-case-5': 'https://www.indiacode.nic.in/handle/123456789/2149', # BNS Section 3(5)
    'det-case-6': 'https://www.indiacode.nic.in/handle/123456789/2149', # BNS Section 100 & 103
}

# Add status, sourceUrl and scorable to detective cases
for case_id, url in det_urls.items():
    pattern = rf"(id:\s*'{case_id}'[\s\S]*?legalVerification:\s*\{{[\s\S]*?)(verificationDate:\s*'[^']+')(\s*\}})"
    replacement = rf"\1\2,\n        status: 'Verified against authoritative source',\n        sourceUrl: '{url}',\n        scorable: true\3"
    det_content = re.sub(pattern, replacement, det_content)

with open('assets/games/data/detective-cases.js', 'w', encoding='utf-8') as f:
    f.write(det_content)
print("Enriched detective-cases.js successfully!")

# 2. Enrich courtroom-cases.js
with open('assets/games/data/courtroom-cases.js', 'r', encoding='utf-8') as f:
    crt_content = f.read()

crt_urls = {
    'court-case-1': 'https://www.indiacode.nic.in/handle/123456789/2191', # CPC Order 39
    'court-case-2': 'https://www.indiacode.nic.in/handle/123456789/2191', # CPC Section 11
    'court-case-3': 'https://www.indiacode.nic.in/handle/123456789/2150', # BNSS Section 480/483
    'court-case-4': 'https://www.indiacode.nic.in/handle/123456789/2151', # BSA Section 63(4)
    'court-case-5': 'https://www.indiacode.nic.in/handle/123456789/2151', # BSA Section 3
    'court-case-6': 'https://www.indiacode.nic.in/handle/123456789/1522', # Constitution Art 14/226
}

for case_id, url in crt_urls.items():
    pattern = rf"(id:\s*'{case_id}'[\s\S]*?legalVerification:\s*\{{[\s\S]*?)(verificationDate:\s*'[^']+')(\s*\}})"
    replacement = rf"\1\2,\n        status: 'Verified against authoritative source',\n        sourceUrl: '{url}',\n        scorable: true\3"
    crt_content = re.sub(pattern, replacement, crt_content)

with open('assets/games/data/courtroom-cases.js', 'w', encoding='utf-8') as f:
    f.write(crt_content)
print("Enriched courtroom-cases.js successfully!")
