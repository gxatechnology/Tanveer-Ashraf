"""
Refined UP PCS-J Previous Year Question (PYQ) Mapping for Indian Constitution Module.
Ensures ONLY authentic Constitutional Law and Polity questions are mapped (~135-145 questions).
Excludes procedural laws (CPC, CrPC, Evidence, IPC, Contract, TPA) even if they cite Supreme Court judgments.
"""

import json
import re

raw_js = open("assets/data/questions.js", encoding="utf-8").read()
json_str = raw_js.split("window.PCSJ_QUESTIONS = ")[1].rsplit(";", 1)[0]
all_questions = json.loads(json_str)

RULES = [
    # Chapter 1: Historical Evolution
    (r"regulating act|charter act|pitts india|1773|1784|1833|1853", "ch-01", "top-const-01-01", "Early constitutional acts under Company Rule."),
    (r"government of india act 1858|indian councils act|1861|1892|1909|morley-minto|1919|montagu-chelmsford", "ch-01", "top-const-01-02", "Crown rule and evolution of legislative councils."),
    (r"government of india act 1935|1935 act|indian independence act 1947|1947 act|provincial autonomy|all-india federation", "ch-01", "top-const-01-03", "GoI Act 1935 blueprint and Independence Act 1947."),
    
    # Chapter 2: Constituent Assembly & Sources
    (r"constituent assembly|cabinet mission|drafting committee|b\.r\. ambedkar|rajendra prasad|sachchidananda|objective resolution|women members", "ch-02", "top-const-02-01", "Constituent Assembly composition, committees and drafting."),
    (r"borrowed|source of.*constitution|british constitution|us constitution|irish constitution|canadian|australian|weimar", "ch-02", "top-const-02-02", "Global sources of the Indian Constitution."),
    (r"salient features|quasi-federal|unitary bias|living constitution|rigid and flexible", "ch-02", "top-const-02-03", "Salient structural features of Indian Constitution."),
    
    # Chapter 3: Preamble
    (r"preamble|sovereign socialist secular|democratic republic|fraternity|liberty, equality|justice social economic", "ch-03", "top-const-03-01", "Ideals, objectives and text of the Preamble."),
    (r"berubari|kesavananda.*preamble|lic of india.*preamble|preamble.*part of", "ch-03", "top-const-03-02", "Legal status, enforceability and amendability of Preamble."),

    # Chapter 4: Union & Territory
    (r"article 1\b|article 2\b|union of states|admission of states|territory of india", "ch-04", "top-const-04-01", "Union and its territory under Articles 1 and 2."),
    (r"article 3\b|article 4\b|reorganisation of states|formation of new state|boundary alteration|states reorganisation commission|fazal ali", "ch-04", "top-const-04-02", "Reorganisation of states and boundary alterations."),

    # Chapter 5: Citizenship
    (r"article 5\b|article 6\b|article 7\b|article 8\b|citizenship at commencement|domicile.*citizen", "ch-05", "top-const-05-01", "Constitutional citizenship at commencement."),
    (r"article 9\b|article 10\b|article 11\b|citizenship act|single citizenship|dual citizenship|nrc|caa", "ch-05", "top-const-05-02", "Single citizenship, statutory regulation and termination."),

    # Chapter 6: Fundamental Rights
    (r"article 12\b|article 13\b|definition of state|other authorities|doctrine of eclipse|doctrine of severability|waiver", "ch-06", "top-const-06-01", "Fundamental rights concept, Art 12 State definition, Art 13 review."),
    (r"article 14\b|article 15\b|article 16\b|article 17\b|article 18\b|equality before law|equal protection|reservation.*backward|untouchability|titles", "ch-06", "top-const-06-02", "Right to Equality (Articles 14–18)."),
    (r"article 19\b|freedom of speech|reasonable restriction|article 20\b|ex-post facto|double jeopardy|self-incrimination", "ch-06", "top-const-06-03", "Six freedoms and protections in criminal convictions."),
    (r"article 21\b|article 21a\b|article 22\b|personal liberty|procedure established by law|due process|maneka gandhi|right to privacy|puttaswamy|preventive detention", "ch-06", "top-const-06-04", "Right to life, education and preventive detention protections."),
    (r"article 23\b|article 24\b|human trafficking|begar|child labour|article 25\b|article 26\b|article 27\b|article 28\b|freedom of religion|secularism.*religion", "ch-06", "top-const-06-05", "Exploitation prohibition and freedom of religion."),
    (r"article 29\b|article 30\b|minority educational|article 32\b|writ of|habeas corpus|mandamus|prohibition.*writ|certiorari|quo warranto|heart and soul", "ch-06", "top-const-06-06", "Cultural & minority rights and Constitutional Remedies / Writs."),

    # Chapter 7: DPSP
    (r"directive principles|part iv\b|article 36\b|article 37\b|non-justiciable|fundamental in governance", "ch-07", "top-const-07-01", "Genesis, nature and non-justiciability of DPSPs."),
    (r"article 38\b|article 39\b|article 40\b|article 44\b|article 45\b|article 48\b|article 50\b|article 51\b|uniform civil code|separation of judiciary|panchayat.*directive", "ch-07", "top-const-07-02", "Substantive classification of DPSPs (Socialist, Gandhian, Liberal)."),
    (r"champakam dorairajan|two wheels of chariot|minerva mills.*dpsp|harmony.*fundamental rights and directive", "ch-07", "top-const-07-03", "Harmonious construction between Rights and Directives."),

    # Chapter 8: Fundamental Duties
    (r"fundamental duties|swaran singh|article 51a\b|part iva\b|42nd amendment.*duty|86th amendment.*duty", "ch-08", "top-const-08-01", "Origin, Swaran Singh Committee and 11 Fundamental Duties."),
    (r"verma committee|enforce.*fundamental dut", "ch-08", "top-const-08-02", "Legal enforcement and judicial application of Fundamental Duties."),

    # Chapter 9: Executive
    (r"president of india|electoral college|impeachment.*president|article 54\b|article 61\b|vice-president|article 63\b|article 66\b", "ch-09", "top-const-09-01", "President and Vice-President: Office, election and removal."),
    (r"article 72\b|pardon.*president|ordinance.*president|article 123\b|executive power.*union|article 77\b|kehar singh", "ch-09", "top-const-09-02", "Executive powers, ordinance making and pardoning powers."),
    (r"prime minister|council of ministers|collective responsibility|article 74\b|article 75\b|article 76\b|attorney general|article 78\b", "ch-09", "top-const-09-03", "Prime Minister, Council of Ministers and Attorney-General."),

    # Chapter 10: Parliament
    (r"parliament of india|rajya sabha|council of states|lok sabha|house of the people|speaker.*lok sabha|article 79\b|article 80\b|article 81\b|sessions of parliament|article 85\b", "ch-10", "top-const-10-01", "Composition, sessions and officers of Parliament."),
    (r"money bill|article 110\b|financial bill|article 117\b|joint sitting|article 108\b|legislative procedure|article 107\b", "ch-10", "top-const-10-02", "Legislative procedures, Money Bills and Joint Sittings."),
    (r"annual financial statement|article 112\b|budget\b|parliamentary privilege|article 105\b|public accounts committee|estimates committee", "ch-10", "top-const-10-03", "Financial business, parliamentary privileges and committees."),

    # Chapter 11: State Government & Local Bodies
    (r"governor.*state|article 153\b|article 154\b|article 161\b|pardon.*governor|ordinance.*governor|article 213\b", "ch-11", "top-const-11-01", "The Governor: Position, powers and discretion."),
    (r"state legislature|vidhan sabha|legislative assembly|vidhan parishad|legislative council|article 169\b|advocate general|article 165\b", "ch-11", "top-const-11-02", "State Legislature and Advocate-General for the State."),
    (r"panchayat|73rd amendment|eleventh schedule|article 243\b|gram sabha", "ch-11", "top-const-11-03", "Panchayati Raj and rural local governance."),
    (r"municipality|municipalities|74th amendment|twelfth schedule|district planning committee|article 243p\b", "ch-11", "top-const-11-04", "Urban local bodies and Municipalities."),

    # Chapter 12: Judiciary
    (r"appointment.*judge|collegium|first judges|second judges|third judges|fourth judges|njac|article 124\b|salaries.*judges.*supreme court", "ch-12", "top-const-12-01", "Structure of Supreme Court and judicial appointments."),
    (r"original jurisdiction|article 131\b|appellate jurisdiction|article 132\b|article 133\b|article 134\b|special leave petition|article 136\b|advisory jurisdiction|article 143\b", "ch-12", "top-const-12-02", "Jurisdictions of the Supreme Court of India."),
    (r"court of record|article 129\b|binding law|article 141\b|complete justice|article 142\b|curative petition|judicial review in india", "ch-12", "top-const-12-03", "Constitutional powers: Precedent, Art 142 equity, contempt."),
    (r"high court|article 214\b|article 216\b|article 226\b|article 227\b|subordinate courts|district judge|article 233\b|article 235\b|common high court", "ch-12", "top-const-12-04", "High Courts and Subordinate Courts in States."),

    # Chapter 13: Emergency
    (r"national emergency|article 352\b|armed rebellion|article 358\b|article 359\b|external aggression", "ch-13", "top-const-13-01", "National Emergency: Grounds, safeguards and fundamental rights effects."),
    (r"president's rule|article 356\b|s\.r\. bommai|failure of constitutional machinery|article 365\b|financial emergency|article 360\b", "ch-13", "top-const-13-02", "President's Rule and Financial Emergency."),

    # Chapter 14: Amendment & Basic Structure
    (r"amendment of the constitution|article 368\b|constituent power|types of amendment|ratification by states|44th constitutional amendment", "ch-14", "top-const-14-01", "The Amendment Procedure under Article 368."),
    (r"basic structure|kesavananda bharati|shankari prasad|sajjan singh|golak nath|minerva mills.*basic structure|basic feature", "ch-14", "top-const-14-02", "The Basic Structure Doctrine and landmark cases."),

    # Chapter 15: Federal Relations, Schedules & Bodies
    (r"centre-state|legislative relations|union list|state list|concurrent list|seventh schedule|repugnancy|article 254\b|article 245\b|article 246\b|article 248\b|article 249\b|article 250\b|article 252\b|article 253\b|territorial nexus|pith and substance|colourable legislation|inter-state council|article 263\b", "ch-15", "top-const-15-01", "Centre-State relations (legislative, administrative, financial)."),
    (r"schedules of the constitution|first schedule|second schedule|third schedule|fourth schedule|fifth schedule|sixth schedule|eighth schedule|ninth schedule|tenth schedule|anti-defection", "ch-15", "top-const-15-02", "The Twelve Schedules of the Constitution."),
    (r"election commission|article 324\b|chief election commissioner|comptroller and auditor general|cag\b|article 148\b|upsc|article 315\b|finance commission|article 280\b", "ch-15", "top-const-15-03", "Independent Constitutional Bodies and Watchdogs."),
    (r"civil services|doctrine of pleasure|article 310\b|article 311\b|all-india services|article 312\b|administrative tribunal|article 323a\b|article 323b\b|l\. chandra kumar", "ch-15", "top-const-15-04", "Public services, Article 311 protections and Administrative Tribunals.")
]

EXCLUDE_TOPICS = [
    "Contract Law", "Penal Law", "Evidence", "Civil Procedure",
    "Criminal Procedure", "Property Law", "Jurisprudence"
]

mapped_pyqs = []

for q in all_questions:
    t = q.get("topic", "")
    full_text = (q.get("stem", "") + " " + " ".join(q.get("options", []))).lower()
    
    # Exclude procedural or other specific law subjects unless topic is explicitly Constitution/Polity
    if t in EXCLUDE_TOPICS:
        # Check if it has explicit constitutional article reference or fundamental rights
        if not any(k in full_text for k in ["constitution of india", "article 14", "article 15", "article 19", "article 21", "article 32", "article 226", "article 311", "article 368", "article 142"]):
            continue
            
    is_candidate = (
        t in ["Constitution", "Polity"] or
        any(k in full_text for k in [
            "constitution of india", "constituent assembly", "fundamental right",
            "directive principle", "doctrine of basic structure", "writ of habeas corpus",
            "mandamus", "certiorari", "quo warranto", "president of india",
            "vice-president of india", "comptroller and auditor general",
            "election commission", "national emergency", "financial emergency",
            "money bill", "rajya sabha", "panchayat", "article 14", "article 19",
            "article 21", "article 32", "article 226", "article 311", "article 368",
            "article 142", "tenth schedule", "eighth schedule"
        ])
    )
    
    if not is_candidate:
        continue
        
    # Check against non-constitutional false positives
    if "united nations" in full_text or "security council" in full_text or "geneva convention" in full_text:
        continue
    if "section 115" in full_text or "section 45 of the indian evidence" in full_text or "section 124a" in full_text or "section 376" in full_text or "family court" in full_text:
        continue

    # Match rules
    matched = False
    for pattern, ch_id, top_id, rationale in RULES:
        if re.search(pattern, full_text):
            mapped_pyqs.append({
                "questionId": q["id"],
                "year": q["year"],
                "paper": q["paper"],
                "questionNumber": q["no"],
                "chapterId": ch_id,
                "topicId": top_id,
                "stem": q["stem"],
                "answer": q["answer"],
                "rationale": rationale
            })
            matched = True
            break
            
    if not matched and t in ["Constitution", "Polity"]:
        mapped_pyqs.append({
            "questionId": q["id"],
            "year": q["year"],
            "paper": q["paper"],
            "questionNumber": q["no"],
            "chapterId": "ch-02",
            "topicId": "top-const-02-03",
            "stem": q["stem"],
            "answer": q["answer"],
            "rationale": "General Indian constitutional structure and polity question."
        })

print(f"Total authentic Constitutional PYQs mapped: {len(mapped_pyqs)}")
from collections import Counter
print("PYQs by Chapter:")
for ch, cnt in sorted(Counter(p["chapterId"] for p in mapped_pyqs).items()):
    print(f"  {ch}: {cnt}")

print("PYQs by Year:")
for yr, cnt in sorted(Counter(p["year"] for p in mapped_pyqs).items()):
    print(f"  {yr}: {cnt}")

out_path = "assets/learning/data/constitution/constitution-pyq-mapping.js"
with open(out_path, "w", encoding="utf-8") as f:
    f.write("/**\n")
    f.write(" * TANVEER ASHRAF — JUDICIAL PREP 2026–27\n")
    f.write(" * Indian Constitution Module — Historical UP PCS-J PYQ Topic Mapping\n")
    f.write(f" * Total Mapped PYQs: {len(mapped_pyqs)} questions across 2012–2023 examinations\n")
    f.write(" * Zero modification to base questions.js; non-destructive overlay registry\n")
    f.write(" */\n\n")
    f.write("(function (global) {\n")
    f.write("  'use strict';\n\n")
    f.write("  global.CONSTITUTION_PYQ_MAPPING = ")
    json.dump(mapped_pyqs, f, indent=2, ensure_ascii=False)
    f.write(";\n\n")
    f.write("})(typeof window !== 'undefined' ? window : global);\n")

print(f"Wrote {len(mapped_pyqs)} PYQs to {out_path}")
