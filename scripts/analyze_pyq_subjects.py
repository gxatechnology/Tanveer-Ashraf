import json
import re

with open('assets/data/questions.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Match PCSJ_QUESTIONS array
# Let's inspect the questions by parsing
print("Length of questions.js:", len(text))

# Find all LAW question matches
q_blocks = re.findall(r'\{\s*"id":\s*"(?P<id>\d{4}-LAW-\d+)".*?"question":\s*"(?P<q>.*?)".*?"eligible":\s*(?P<el>true|false)', text, re.DOTALL)
print(f"Total LAW questions found via regex: {len(q_blocks)}")

# Let's check for keywords in Law questions
jurisprudence_keywords = [
    'jurisprudence', 'austin', 'hart', 'kelsen', 'savigny', 'roscoe pound', 'bentham',
    'salmond', 'holmes', 'holland', 'dias', 'maine', 'duguit', 'fuller', 'dworkin',
    'natural law', 'analytical school', 'historical school', 'sociological school',
    'pure theory', 'grundnorm', 'command theory', 'volksgeist', 'social engineering',
    'custom', 'precedent', 'ratio decidendi', 'obiter dicta', 'stare decisis',
    'legal right', 'legal personality', 'ownership', 'possession', 'animus possidendi',
    'corpus possessionis', 'strict liability', 'vicarious liability', 'mens rea in jurisprudence'
]

contract_keywords = [
    'contract', 'agreement', 'proposal', 'acceptance', 'promise', 'consideration',
    'section 2(', 'section 10', 'section 11', 'section 12', 'section 13', 'section 14',
    'section 15', 'section 16', 'section 17', 'section 18', 'section 19', 'section 20',
    'section 23', 'section 24', 'section 25', 'section 26', 'section 27', 'section 28',
    'section 29', 'section 30', 'section 31', 'section 56', 'section 68', 'section 73',
    'section 74', 'section 124', 'section 126', 'section 148', 'section 172', 'section 182',
    'coercion', 'undue influence', 'fraud', 'misrepresentation', 'free consent',
    'contingent contract', 'frustration of contract', 'quasi-contract', 'anticipatory breach',
    'indemnity', 'guarantee', 'bailment', 'pledge', 'agency', 'contract act'
]

tpa_keywords = [
    'transfer of property', 'property act', 'tpa', 'section 5', 'section 6',
    'section 10', 'section 11', 'section 12', 'section 13', 'section 14', 'section 19',
    'section 21', 'section 35', 'section 41', 'section 43', 'section 52', 'section 53',
    'section 53a', 'section 54', 'section 58', 'section 100', 'section 105', 'section 118',
    'section 122', 'section 130', 'rule against perpetuity', 'doctrine of election',
    'ostensible owner', 'feeding the grant', 'lis pendens', 'fraudulent transfer',
    'part performance', 'mortgage', 'usufructuary mortgage', 'simple mortgage',
    'english mortgage', 'mortgage by conditional sale', 'anomalous mortgage',
    'charge', 'lease', 'exchange', 'gift', 'actionable claim', 'onerous gift',
    'vested interest', 'contingent interest'
]

print("Script written successfully.")
