"""
Builder for Criminal Law Practice MCQs (360 Questions: 10 per Topic across 36 Topics)
Output: assets/learning/data/criminal/criminal-mcqs.js
"""

import json

# Load topics to iterate cleanly
with open("assets/learning/data/criminal/criminal-topics.js", "r", encoding="utf-8") as f:
    text = f.read()
    # Extract json list
    start = text.find("[")
    end = text.rfind("]") + 1
    TOPICS = json.loads(text[start:end])

print(f"Loaded {len(TOPICS)} Criminal Law topics.")

# Detailed question definitions per topic
# We define questions per topic using high-yield UP PCS-J legal standards
def generate_topic_mcqs(topic):
    tid = topic["id"]
    cid = topic["chapterId"]
    title = topic["title"]
    
    # Topic specific generator
    mcqs = []
    
    # We will build rich, authentic questions for each specific topic
    # Let's define the templates and custom data for topics
    return mcqs

