# -*- coding: utf-8 -*-
import os

with open('civil-suit-journey.html', 'r', encoding='utf-8') as f:
    html = f.read()

stream_mappings = {
    1: ('Ordinary Trial Stream: Inception', 'stream-ordinary'),
    2: ('Ordinary Trial Stream: Jurisdiction', 'stream-ordinary'),
    3: ('Ordinary Trial Stream: Plaint Presentation', 'stream-ordinary'),
    4: ('Ordinary Trial Stream: Threshold Scrutiny (O. VII R. 10/11)', 'stream-ordinary'),
    5: ('Ordinary Trial Stream: Process & Service of Summons', 'stream-ordinary'),
    6: ('Ordinary Trial Stream: Written Statement & Set-Off', 'stream-ordinary'),
    7: ('Settlement & Alternate Paths: Appearance / S. 89 ADR', 'stream-alternate'),
    8: ('Ordinary Trial Stream: Discovery & Inspection', 'stream-ordinary'),
    9: ('Ordinary Trial Stream: Framing & Settlement of Issues', 'stream-ordinary'),
    10: ('Ordinary Trial Stream: Trial Evidence (Interlocutory O. 39 Active)', 'stream-interlocutory'),
    11: ('Ordinary Trial Stream: Final Arguments', 'stream-ordinary'),
    12: ('Adjudication Stream: Judgment Pronouncement (S. 33)', 'stream-adjudication'),
    13: ('Adjudication Stream: Formal Decree & Costs (S. 2(2), S. 34)', 'stream-adjudication'),
    14: ('Enforcement & Recourse: Execution (O. XXI) & Appeals (S. 96/100/115)', 'stream-enforcement')
}

for num, (stream, stream_class) in stream_mappings.items():
    target = f"num: {num},\n        title:"
    repl = f'num: {num},\n        stream: "{stream}",\n        streamClass: "{stream_class}",\n        title:'
    if target in html:
        html = html.replace(target, repl)
    else:
        print(f"Target for {num} not found")

# Update loadStage to update stream badge
load_target = "document.getElementById('stage-number-badge').textContent = st.badge;"
load_repl = """document.getElementById('stage-number-badge').textContent = st.badge;
      const streamBadge = document.getElementById('stage-stream-badge');
      if (streamBadge) {
        streamBadge.textContent = st.stream || 'ORDINARY TRIAL STREAM';
        streamBadge.className = 'stream-badge-tag ' + (st.streamClass || 'stream-ordinary');
      }"""

if load_target in html:
    html = html.replace(load_target, load_repl)
    print("Successfully replaced loadStage logic")
else:
    print("loadStage target not found")

with open('civil-suit-journey.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("civil-suit-journey.html updated successfully!")
