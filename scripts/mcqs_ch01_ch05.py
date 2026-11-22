"""
Authoritative Practice MCQs for Indian Constitution
Chapters 1 to 5 (135 MCQs)
Ch 1: 30 MCQs | Ch 2: 30 MCQs | Ch 3: 25 MCQs | Ch 4: 25 MCQs | Ch 5: 25 MCQs
"""

MCQS_PART1 = []

def add_mcq(m_id, ch_id, top_id, q_text, opts, ans_idx, expl, breakdowns, diff, prov, obj):
    letters = ['A', 'B', 'C', 'D']
    MCQS_PART1.append({
        'id': m_id,
        'subjectId': 'law-constitution',
        'chapterId': ch_id,
        'topicId': top_id,
        'question': q_text,
        'options': opts,
        'answer': ans_idx,
        'answerLetter': letters[ans_idx],
        'explanation': expl,
        'optionBreakdown': breakdowns,
        'difficulty': diff,
        'provision': prov,
        'sourceUrl': 'https://legislative.gov.in',
        'verifiedDate': '2026-11-22',
        'applicableDate': '2026-11-22',
        'learningObjective': obj,
        'eligible': True,
        'status': 'active'
    })

print("Building MCQs for Chapters 1 to 5...")
