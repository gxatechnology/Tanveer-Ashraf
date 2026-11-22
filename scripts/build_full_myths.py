import json
import os

items = []
current_id = 1

def add(stmt, classification, subject, diff, leg, sec, subsec, expl, mis_expl, exc, err_phrase, corr, url, legal_date, keywords, old_vs_new=None):
    global current_id
    items.append({
        "id": f"myth-{current_id:03d}",
        "statement": stmt,
        "classification": classification,
        "subject": subject,
        "difficulty": diff,
        "legislation": leg,
        "section": sec,
        "subsection": subsec,
        "explanation": expl,
        "misconceptionExplanation": mis_expl,
        "exceptions": exc,
        "errorPhrase": err_phrase,
        "correction": corr,
        "sourceUrl": url,
        "verificationDate": "2026-11-22",
        "applicableLegalDate": legal_date,
        "revisionKeywords": keywords,
        "oldVsNew": old_vs_new
    })
    current_id += 1

# Helper for India Code URL
IC_BASE = "https://www.indiacode.nic.in/handle/123456789/"

# We will load subject modules and append statements
print("Building comprehensive 320+ Legal Myth Buster database...")
