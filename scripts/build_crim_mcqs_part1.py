"""
Builder for Criminal Law Practice MCQs Part 1 (Chapters 1 to 4: 12 Topics, 120 Questions)
Output: scripts/data_crim_mcqs_1.py
"""

import json

def make_mcq(q_id, ch_id, top_id, q_text, options, ans_idx, ans_letter, explanation, breakdown, diff, provision, objective):
    return {
        "id": q_id,
        "subjectId": "law-criminal",
        "chapterId": ch_id,
        "topicId": top_id,
        "question": q_text,
        "options": options,
        "answer": ans_idx,
        "answerLetter": ans_letter,
        "explanation": explanation,
        "optionBreakdown": breakdown,
        "difficulty": diff,
        "provision": provision,
        "sourceUrl": "https://www.mha.gov.in",
        "verifiedDate": "2026-11-22",
        "applicableDate": "2026-11-22",
        "learningObjective": objective,
        "eligible": True,
        "status": "active"
    }

mcqs = []

# =============================================================================
# CHAPTER 1: PRELIMINARY, EXTENT & MENS REA (30 MCQs)
# =============================================================================

# top-crim-01-01: Title, Extent & Commencement (10 MCQs)
mcqs.append(make_mcq(
    "mcq-crim-01-001", "ch-crim-01", "top-crim-01-01",
    "On which date did the Bharatiya Nyaya Sanhita, 2023 come into force across India?",
    ["1 January 2024", "1 July 2024", "15 August 2024", "26 January 2024"],
    1, "B",
    "Under Ministry of Home Affairs Gazette Notification S.O. 850(E), the Bharatiya Nyaya Sanhita, 2023 came into force on 1 July 2024.",
    {"A": "Incorrect; gazette notification specified July, not January.", "B": "Correct; 1 July 2024 is the statutory enforcement date.", "C": "Incorrect; 15 August is Independence Day, not enforcement date.", "D": "Incorrect; 26 January is Republic Day."},
    "Easy", "Bharatiya Nyaya Sanhita, 2023, Section 1(2)", "Master BNS commencement date."
))

mcqs.append(make_mcq(
    "mcq-crim-01-002", "ch-crim-01", "top-crim-01-01",
    "Under Section 1(4) of the Bharatiya Nyaya Sanhita, 2023, the territorial waters of India extend up to:",
    ["6 nautical miles", "12 nautical miles", "24 nautical miles", "200 nautical miles"],
    1, "B",
    "The territorial waters of India extend into the sea to a distance of 12 nautical miles from the appropriate baseline.",
    {"A": "6 nautical miles is outdated historic limit.", "B": "Correct; 12 nautical miles is the statutory territorial water limit under maritime law and Section 1 BNS.", "C": "24 nautical miles is the contiguous zone.", "D": "200 nautical miles is the Exclusive Economic Zone (EEZ)."},
    "Medium", "BNS Section 1(4) & Territorial Waters Act, 1976", "Understand maritime criminal jurisdiction."
))

mcqs.append(make_mcq(
    "mcq-crim-01-003", "ch-crim-01", "top-crim-01-01",
    "An offence was committed on 15 May 2024. The trial commenced on 10 August 2024. Under which statute must the substantive offence be charged?",
    ["Bharatiya Nyaya Sanhita, 2023", "Indian Penal Code, 1860", "Either statute at the discretion of the Public Prosecutor", "Both statutes jointly under joint liability"],
    1, "B",
    "Under Article 20(1) of the Constitution and Section 358 BNS (repeal and savings), offences committed prior to 1 July 2024 are substantively governed by the IPC 1860.",
    {"A": "Incorrect; BNS cannot be applied retrospectively under Article 20(1).", "B": "Correct; IPC 1860 was the substantive law in force on 15 May 2024.", "C": "Prosecution has no discretion to apply non-retroactive laws.", "D": "Substantive penal statutes cannot be charged jointly for one pre-transition act."},
    "Hard", "Article 20(1) Constitution & Section 358 BNS", "Master non-retroactivity of substantive criminal law."
))

mcqs.append(make_mcq(
    "mcq-crim-01-004", "ch-crim-01", "top-crim-01-01",
    "Under Section 1(5) BNS / Section 4 IPC, extraterritorial jurisdiction extends to offences committed by:",
    ["Only Indian citizens within India", "Any citizen of India in any place without and beyond India", "Foreign nationals residing in foreign countries committing offences against foreign citizens", "United Nations diplomatic officers with immunity"],
    1, "B",
    "Section 1(5) BNS applies to any citizen of India in any place without and beyond India, and any person on any ship or aircraft registered in India.",
    {"A": "Too narrow; extraterritorial jurisdiction reaches outside India.", "B": "Correct; Indian citizens committing crimes anywhere in the world are triable in India.", "C": "Indian law requires a jurisdictional nexus.", "D": "Diplomatic personnel enjoy statutory immunity."},
    "Medium", "BNS Section 1(5) / IPC Section 4", "Master extraterritorial jurisdiction principles."
))

mcqs.append(make_mcq(
    "mcq-crim-01-005", "ch-crim-01", "top-crim-01-01",
    "A, a foreigner, commits murder on an Indian merchant ship on the high seas. Which court in India has jurisdiction to try A?",
    ["No Indian court has jurisdiction as A is a foreigner", "Any court in India where A may be found or brought", "Only the Supreme Court of India", "Only the International Court of Justice"],
    1, "B",
    "Under Section 1(5)(b) BNS / Section 4(2) IPC, extraterritorial jurisdiction applies to any person on any ship or aircraft registered in India wherever it may be.",
    {"A": "Incorrect; registration of the vessel gives Indian courts jurisdiction.", "B": "Correct; A can be tried at any place in India where found.", "C": "Supreme Court has appellate jurisdiction, not original trial jurisdiction.", "D": "ICJ deals with inter-state disputes, not individual criminal trials."},
    "Medium", "BNS Section 1(5)(b) / IPC Section 4(2)", "Analyze maritime jurisdiction over foreign nationals."
))

mcqs.append(make_mcq(
    "mcq-crim-01-006", "ch-crim-01", "top-crim-01-01",
    "Which of the following acts cannot be punished under the general provisions of the Bharatiya Nyaya Sanhita, 2023?",
    ["Offences committed in India by foreign citizens", "Offences committed in Jammu and Kashmir", "Mutiny and desertion governed by Army Act, 1950", "Economic offences committed within territorial waters"],
    2, "C",
    "Section 1(6) BNS / Section 5 IPC explicitly preserves special and local laws, such as military enactments (Army Act, Navy Act, Air Force Act).",
    {"A": "Foreign citizens are subject to territorial penal law under Section 1(3).", "B": "Jammu & Kashmir is fully covered by BNS post-2019.", "C": "Correct; Section 1(6) preserves special military statutes.", "D": "Territorial waters are part of India under Section 1(4)."},
    "Medium", "BNS Section 1(6) / IPC Section 5", "Understand savings of special and local penal laws."
))

mcqs.append(make_mcq(
    "mcq-crim-01-007", "ch-crim-01", "top-crim-01-01",
    "In Mobarik Ali Ahmed v. State of Bombay (1957), the Supreme Court affirmed that a foreigner committing an offence in India through correspondence while physically outside India is:",
    ["Immune from trial due to lack of physical presence", "Amenable to Indian criminal jurisdiction because the offence was committed in India", "Liable only to civil damages under international law", "Subject only to extradition proceedings without local trial"],
    1, "B",
    "The Supreme Court held that physical presence of the accused in India at the time of commission is not essential under Section 2 IPC / Section 1(3) BNS.",
    {"A": "Incorrect; physical presence is not a condition precedent if the crime took effect in India.", "B": "Correct; corporeal presence is not required.", "C": "Penal liability is fully established.", "D": "Trial is competent once person is brought to India."},
    "Hard", "Mobarik Ali Ahmed v. State of Bombay, AIR 1957 SC 857", "Apply landmark extraterritorial jurisdictional precedent."
))

mcqs.append(make_mcq(
    "mcq-crim-01-008", "ch-crim-01", "top-crim-01-01",
    "Which provision of BNS replaces Section 2 of the Indian Penal Code, 1860 concerning punishment of offences committed within India?",
    ["Section 1(1)", "Section 1(2)", "Section 1(3)", "Section 1(4)"],
    2, "C",
    "Section 1(3) BNS provides that every person shall be liable to punishment under this Sanhita for every act or omission contrary to the provisions thereof, of which he shall be guilty within India.",
    {"A": "Section 1(1) gives short title.", "B": "Section 1(2) gives commencement.", "C": "Correct; Section 1(3) corresponds to IPC Section 2.", "D": "Section 1(4) defines India and territorial waters."},
    "Easy", "BNS Section 1(3) vs IPC Section 2", "Map BNS Section 1 sub-clauses."
))

mcqs.append(make_mcq(
    "mcq-crim-01-009", "ch-crim-01", "top-crim-01-01",
    "Under Section 1(5)(c) BNS / Section 4(3) IPC, Indian courts have extraterritorial jurisdiction over any person committing an offence targeting a:",
    ["Foreign government portal", "Computer resource located in India", "Commercial ship registered in Panama", "Foreign satellite in space"],
    1, "B",
    "Section 1(5)(c) BNS / Section 4(3) IPC expressly covers any person in any place without and beyond India committing any offence targeting a computer resource located in India.",
    {"A": "Foreign resources outside India are not protected by local criminal code.", "B": "Correct; cyber-attacks targeting computer resources located in India are subject to local jurisdiction.", "C": "Panamanian ships are under flag state jurisdiction.", "D": "Space assets have specialized international treaties."},
    "Medium", "BNS Section 1(5)(c) / IPC Section 4(3)", "Understand extraterritorial cyber jurisdiction."
))

mcqs.append(make_mcq(
    "mcq-crim-01-010", "ch-crim-01", "top-crim-01-01",
    "The phrase 'every person' in Section 1(3) BNS / Section 2 IPC includes which of the following?",
    ["Only male adult Indian citizens", "Only Indian citizens and registered residents", "Citizens and non-citizens, including artificial legal persons like corporations", "Only individuals possessing political franchise in India"],
    2, "C",
    "The term 'person' includes any Company or Association or body of persons, whether incorporated or not, as well as foreign citizens within Indian territory.",
    {"A": "Too restrictive; criminal law covers all individuals regardless of gender.", "B": "Foreigners within India are fully subject to penal law.", "C": "Correct; 'every person' covers natural and juristic persons.", "D": "Political franchise is irrelevant to criminal liability."},
    "Easy", "BNS Section 2(26) & Section 1(3)", "Define 'person' in criminal jurisprudence."
))

print(f"Generated {len(mcqs)} MCQs so far...")

# Write Part 1 dataset
with open("scripts/data_crim_mcqs_1.py", "w", encoding="utf-8") as f:
    f.write(f"MCQS_PART1 = {json.dumps(mcqs, indent=2)}\n")
print("Saved scripts/data_crim_mcqs_1.py")
