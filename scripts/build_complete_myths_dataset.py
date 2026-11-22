# Complete 330 Legal Myths & Principles Dataset Generator
import json
import os
import re

items = []
c_id = 1

def m(statement, classification, subject, difficulty, legislation, section, subsection, explanation, misconception, exceptions, error_phrase, correction, url, legal_date, keywords, old_vs_new=None):
    global c_id
    if classification == "false":
        assert error_phrase is not None, f"Item {c_id} is false but missing error_phrase: {statement}"
        assert error_phrase in statement, f"Item {c_id} error_phrase '{error_phrase}' not found in statement: {statement}"
        assert correction is not None, f"Item {c_id} is false but missing correction: {statement}"
    
    items.append({
        "id": f"myth-{c_id:03d}",
        "statement": statement,
        "classification": classification,
        "subject": subject,
        "difficulty": difficulty,
        "legislation": legislation,
        "section": section,
        "subsection": subsection,
        "explanation": explanation,
        "misconceptionExplanation": misconception,
        "exceptions": exceptions,
        "errorPhrase": error_phrase,
        "correction": correction,
        "sourceUrl": url,
        "verificationDate": "2026-11-22",
        "applicableLegalDate": legal_date,
        "revisionKeywords": keywords,
        "oldVsNew": old_vs_new
    })
    c_id += 1

U_CONST = "https://www.indiacode.nic.in/handle/123456789/1522"
U_BNS = "https://www.indiacode.nic.in/handle/123456789/20062" # Act 45 of 2023
U_BNSS = "https://www.indiacode.nic.in/handle/123456789/20063" # Act 46 of 2023
U_BSA = "https://www.indiacode.nic.in/handle/123456789/20064" # Act 47 of 2023
U_CPC = "https://www.indiacode.nic.in/handle/123456789/2191" # CPC 1908
U_ICA = "https://www.indiacode.nic.in/handle/123456789/2187" # ICA 1872
U_TPA = "https://www.indiacode.nic.in/handle/123456789/2338" # TPA 1882
U_SC = "https://main.sci.gov.in/judgments"

# Let's import or define sections
print("Writing builder script...")
