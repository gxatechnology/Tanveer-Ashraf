"""
Activate Social Subjects in assets/learning/data/subjects.js
"""

import re

subjects_file = "assets/learning/data/subjects.js"

with open(subjects_file, "r", encoding="utf-8") as f:
    content = f.read()

updates = {
    "soc-disabilities": {
        "shortName": "RPwD Act", "status": "active", "badge": "Active Mastery Module",
        "chaptersCount": 3, "topicsCount": 9, "mcqsCount": 50, "pyqsCount": 4, "estimatedHours": 8
    },
    "soc-parents": {
        "shortName": "Senior Citizens Act", "status": "active", "badge": "Active Mastery Module",
        "chaptersCount": 3, "topicsCount": 9, "mcqsCount": 50, "pyqsCount": 1, "estimatedHours": 8
    },
    "soc-dowry": {
        "shortName": "Dowry Prohibition", "status": "active", "badge": "Active Mastery Module",
        "chaptersCount": 3, "topicsCount": 9, "mcqsCount": 50, "pyqsCount": 5, "estimatedHours": 8
    },
    "soc-domestic-violence": {
        "shortName": "DV Act", "status": "active", "badge": "Active Mastery Module",
        "chaptersCount": 3, "topicsCount": 9, "mcqsCount": 50, "pyqsCount": 2, "estimatedHours": 8
    },
    "soc-posh": {
        "shortName": "POSH Act", "status": "active", "badge": "Active Mastery Module",
        "chaptersCount": 3, "topicsCount": 9, "mcqsCount": 50, "pyqsCount": 1, "estimatedHours": 8
    },
    "soc-pcpndt": {
        "shortName": "PCPNDT Act", "status": "active", "badge": "Active Mastery Module",
        "chaptersCount": 3, "topicsCount": 9, "mcqsCount": 50, "pyqsCount": 2, "estimatedHours": 8
    },
    "soc-mtp": {
        "shortName": "MTP Act", "status": "active", "badge": "Active Mastery Module",
        "chaptersCount": 3, "topicsCount": 9, "mcqsCount": 50, "pyqsCount": 3, "estimatedHours": 8
    },
    "soc-indecent-rep": {
        "shortName": "IRWA", "status": "active", "badge": "Active Mastery Module",
        "chaptersCount": 3, "topicsCount": 9, "mcqsCount": 45, "pyqsCount": 3, "estimatedHours": 7
    },
    "soc-pocso": {
        "shortName": "POCSO Act", "status": "active", "badge": "Active Mastery Module",
        "chaptersCount": 4, "topicsCount": 12, "mcqsCount": 60, "pyqsCount": 2, "estimatedHours": 10
    }
}

for sid, u in updates.items():
    # Find block starting with id: 'sid' up to pyqsCount: \d+
    pattern = rf"(id:\s*['\"]{re.escape(sid)}['\"][\s\S]*?status:\s*['\"]upcoming['\"][\s\S]*?pyqsCount:\s*\d+)"
    match = re.search(pattern, content)
    if not match:
        print(f"Could not find match for {sid}")
        continue
    
    orig = match.group(1)
    # replace status
    new_text = re.sub(r"status:\s*['\"]upcoming['\"]", "status: 'active',\n      badge: 'Active Mastery Module'", orig)
    # add shortName
    new_text = re.sub(r"(name:\s*['\"][^'\"]*['\"],)", rf"\1\n      shortName: '{u['shortName']}',", new_text)
    # update chaptersCount
    new_text = re.sub(r"chaptersCount:\s*\d+", f"chaptersCount: {u['chaptersCount']}", new_text)
    # update topicsCount
    new_text = re.sub(r"topicsCount:\s*\d+", f"topicsCount: {u['topicsCount']}", new_text)
    # update mcqsCount
    new_text = re.sub(r"mcqsCount:\s*\d+", f"mcqsCount: {u['mcqsCount']}", new_text)
    # update pyqsCount
    new_text = re.sub(r"pyqsCount:\s*\d+", f"pyqsCount: {u['pyqsCount']},\n      estimatedHours: {u['estimatedHours']}", new_text)
    
    content = content.replace(orig, new_text)
    print(f"Successfully activated {sid}")

with open(subjects_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated assets/learning/data/subjects.js")
