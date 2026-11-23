"""
Automated Test Suite for V3.1 Phase 5: Complete Social Legislation Learning Academy (9 Acts)
Validates:
1. 30 subjects in subjects.js (17 active: 8 Law + 9 Social Legislation)
2. 127 chapters across 17 active subjects (99 Law + 28 Social)
3. Exactly 373 topics across 17 active subjects (289 Law + 84 Social)
4. Exactly 373 authored topic concepts (289 Law + 84 Social)
5. Exactly 3,075 authored practice MCQs (2,620 Law + 455 Social)
6. All 615 authentic PYQ mappings (592 Law + 23 Social)
7. All 90 Academic SVG diagrams present in assets/learning/images/diagrams/ (72 Law + 18 Social)
8. All 79 Statutory Comparisons in criminal-statutory-comparisons.js (BNS vs IPC, BNSS vs CrPC, BSA vs IEA)
9. Syntax of all JavaScript files using Node.js
10. All 27 HTML pages exist (including civil-suit-journey.html & comparison-lab.html)
11. Universal Smart Search indexes all 17 active subject topics and MCQs (including SOCIAL_TOPICS & SOCIAL_MCQS)
12. Unified backup schema v3.1.0 and storage key tanveer-learning-v1
13. CPC Section-Order-Rule Explorer dataset (83 indexed statutory entries)
14. The Civil Suit Journey 14-stage interactive simulation page
15. Social Sections Explorer dataset (98 indexed statutory entries across 9 Acts)
"""

import os
import re
import sys
import glob
import json
import subprocess

PASS = "✓ PASS"
FAIL = "✗ FAIL"
errors = []

def test(name, condition, details=""):
    if condition:
        print(f"[{PASS}] {name}")
    else:
        print(f"[{FAIL}] {name}: {details}")
        errors.append(f"{name}: {details}")

print("================================================================================")
print("RUNNING LEARNING ACADEMY AUTOMATED TEST SUITE (V3.1 PHASE 5: 17 ACTIVE SUBJECTS)")
print("================================================================================\n")

# 1. Subjects Registry
print("--- TEST GROUP 1: SUBJECT REGISTRY (17 ACTIVE SUBJECTS) ---")
sub_js = open("assets/learning/data/subjects.js", encoding="utf-8").read()
test("subjects.js exists and is readable", "SUBJECTS" in sub_js)

res = subprocess.run(['node', '-e', "const s = require('./assets/learning/data/subjects.js'); console.log((s.subjects || s).length);"], capture_output=True, text=True)
sub_count = int(res.stdout.strip()) if res.returncode == 0 else 0
test("Subject Registry contains exactly 30 subjects", sub_count == 30, f"Got {sub_count}")

# Check 17 active subjects
res_active = subprocess.run(['node', '-e', "const s = require('./assets/learning/data/subjects.js'); const list = s.subjects || s; const active = list.filter(x=>x.status==='active'); console.log(active.length, active.map(x=>x.id).sort().join(','));"], capture_output=True, text=True)
active_parts = res_active.stdout.strip().split(' ', 1)
n_active = int(active_parts[0]) if len(active_parts) > 1 else 0
active_ids = active_parts[1] if len(active_parts) > 1 else ""

test("Twenty-two subjects are active in Registry (8 Law + 9 Social Legislation + 5 General Knowledge)", n_active == 22, f"Got {n_active}")
expected_active_ids = "gk-culture,gk-economy,gk-geography,gk-history,gk-polity,law-constitution,law-contract,law-cpc,law-criminal,law-crpc,law-evidence,law-jurisprudence,law-tpa,soc-disabilities,soc-domestic-violence,soc-dowry,soc-indecent-rep,soc-mtp,soc-parents,soc-pcpndt,soc-pocso,soc-posh"
test("All expected 22 subject IDs match exactly in Registry", active_ids == expected_active_ids, f"Got {active_ids}")

# 2. Chapters Validation Across 17 Subjects
print("\n--- TEST GROUP 2: CHAPTERS VALIDATION (127 CHAPTERS TOTAL) ---")
script_ch = """
const cConst = require('./assets/learning/data/constitution/constitution-chapters.js');
const cJur = require('./assets/learning/data/jurisprudence/jurisprudence-chapters.js');
const cCnt = require('./assets/learning/data/contract/contract-chapters.js');
const cTpa = require('./assets/learning/data/tpa/tpa-chapters.js');
const cCrim = require('./assets/learning/data/criminal/criminal-chapters.js');
const cCrpc = require('./assets/learning/data/crpc/crpc-chapters.js');
const cEvi = require('./assets/learning/data/evidence/evidence-chapters.js');
const cCpc = require('./assets/learning/data/cpc/cpc-chapters.js');
const cSoc = require('./assets/learning/data/social/social-chapters.js');
console.log(
  (cConst.chapters || cConst).length,
  (cJur.chapters || cJur).length,
  (cCnt.chapters || cCnt).length,
  (cTpa.chapters || cTpa).length,
  (cCrim.chapters || cCrim).length,
  (cCrpc.chapters || cCrpc).length,
  (cEvi.chapters || cEvi).length,
  (cCpc.chapters || cCpc).length,
  (cSoc.chapters || cSoc).length
);
"""
res_ch = subprocess.run(['node', '-e', script_ch], capture_output=True, text=True)
if res_ch.returncode != 0:
    print("Chapter eval error:", res_ch.stderr)
    n_const_ch, n_jur_ch, n_cnt_ch, n_tpa_ch, n_crim_ch, n_crpc_ch, n_evi_ch, n_cpc_ch, n_soc_ch = 0, 0, 0, 0, 0, 0, 0, 0, 0
else:
    n_const_ch, n_jur_ch, n_cnt_ch, n_tpa_ch, n_crim_ch, n_crpc_ch, n_evi_ch, n_cpc_ch, n_soc_ch = map(int, res_ch.stdout.strip().split())

test("Constitution Chapters count is exactly 15", n_const_ch == 15, f"Got {n_const_ch}")
test("Jurisprudence Chapters count is exactly 11", n_jur_ch == 11, f"Got {n_jur_ch}")
test("Contract Law Chapters count is exactly 11", n_cnt_ch == 11, f"Got {n_cnt_ch}")
test("Transfer of Property Act Chapters count is exactly 8", n_tpa_ch == 8, f"Got {n_tpa_ch}")
test("Criminal Law Chapters count is exactly 12", n_crim_ch == 12, f"Got {n_crim_ch}")
test("Criminal Procedure Chapters count is exactly 12", n_crpc_ch == 12, f"Got {n_crpc_ch}")
test("Law of Evidence Chapters count is exactly 10", n_evi_ch == 10, f"Got {n_evi_ch}")
test("Code of Civil Procedure Chapters count is exactly 20", n_cpc_ch == 20, f"Got {n_cpc_ch}")
test("Social Legislation Chapters count is exactly 28 (across 9 Acts)", n_soc_ch == 28, f"Got {n_soc_ch}")
total_chapters = n_const_ch + n_jur_ch + n_cnt_ch + n_tpa_ch + n_crim_ch + n_crpc_ch + n_evi_ch + n_cpc_ch + n_soc_ch
test("Total active chapters across all 17 subjects equals exactly 127", total_chapters == 127, f"Got {total_chapters}")

# 3. Topics Validation Across 17 Subjects
print("\n--- TEST GROUP 3: TOPICS VALIDATION (373 TOPICS TOTAL) ---")
script_top = """
const tConst = require('./assets/learning/data/constitution/constitution-topics.js');
const tJur = require('./assets/learning/data/jurisprudence/jurisprudence-topics.js');
const tCnt = require('./assets/learning/data/contract/contract-topics.js');
const tTpa = require('./assets/learning/data/tpa/tpa-topics.js');
const tCrim = require('./assets/learning/data/criminal/criminal-topics.js');
const tCrpc = require('./assets/learning/data/crpc/crpc-topics.js');
const tEvi = require('./assets/learning/data/evidence/evidence-topics.js');
const tCpc = require('./assets/learning/data/cpc/cpc-topics.js');
const tSoc = require('./assets/learning/data/social/social-topics.js');
console.log(tConst.length, tJur.length, tCnt.length, tTpa.length, tCrim.length, tCrpc.length, tEvi.length, tCpc.length, tSoc.length);
"""
res_top = subprocess.run(['node', '-e', script_top], capture_output=True, text=True)
if res_top.returncode != 0:
    print("Topic eval error:", res_top.stderr)
    n_const_top, n_jur_top, n_cnt_top, n_tpa_top, n_crim_top, n_crpc_top, n_evi_top, n_cpc_top, n_soc_top = 0, 0, 0, 0, 0, 0, 0, 0, 0
else:
    n_const_top, n_jur_top, n_cnt_top, n_tpa_top, n_crim_top, n_crpc_top, n_evi_top, n_cpc_top, n_soc_top = map(int, res_top.stdout.strip().split())

test("Constitution Topics count is exactly 45", n_const_top == 45, f"Got {n_const_top}")
test("Jurisprudence Topics count is exactly 30", n_jur_top == 30, f"Got {n_jur_top}")
test("Contract Law Topics count is exactly 32", n_cnt_top == 32, f"Got {n_cnt_top}")
test("Transfer of Property Act Topics count is exactly 24", n_tpa_top == 24, f"Got {n_tpa_top}")
test("Criminal Law Topics count is exactly 36", n_crim_top == 36, f"Got {n_crim_top}")
test("Criminal Procedure Topics count is exactly 35", n_crpc_top == 35, f"Got {n_crpc_top}")
test("Law of Evidence Topics count is exactly 30", n_evi_top == 30, f"Got {n_evi_top}")
test("Code of Civil Procedure Topics count is exactly 57", n_cpc_top == 57, f"Got {n_cpc_top}")
test("Social Legislation Topics count is exactly 84 (across 9 Acts)", n_soc_top == 84, f"Got {n_soc_top}")
total_topics = n_const_top + n_jur_top + n_cnt_top + n_tpa_top + n_crim_top + n_crpc_top + n_evi_top + n_cpc_top + n_soc_top
test("Total active topics across all 17 subjects equals exactly 373", total_topics == 373, f"Got {total_topics}")

# 4. Authored Concepts Across 17 Subjects
print("\n--- TEST GROUP 4: AUTHORED CONCEPTS (373 TOPICS TOTAL) ---")
script_con = """
const cConst = require('./assets/learning/data/constitution/constitution-concepts.js');
const cJur = require('./assets/learning/data/jurisprudence/jurisprudence-concepts.js');
const cCnt = require('./assets/learning/data/contract/contract-concepts.js');
const cTpa = require('./assets/learning/data/tpa/tpa-concepts.js');
const cCrim = require('./assets/learning/data/criminal/criminal-concepts.js');
const cCrpc = require('./assets/learning/data/crpc/crpc-concepts.js');
const cEvi = require('./assets/learning/data/evidence/evidence-concepts.js');
const cCpc = require('./assets/learning/data/cpc/cpc-concepts.js');
const cSoc = require('./assets/learning/data/social/social-concepts.js');
console.log(
  Object.keys(cConst).length,
  Object.keys(cJur).length,
  Object.keys(cCnt).length,
  Object.keys(cTpa).length,
  Object.keys(cCrim).length,
  Object.keys(cCrpc).length,
  Object.keys(cEvi).length,
  Object.keys(cCpc).length,
  Object.keys(cSoc).length
);
"""
res_con = subprocess.run(['node', '-e', script_con], capture_output=True, text=True)
if res_con.returncode != 0:
    print("Concept eval error:", res_con.stderr)
    n_const_con, n_jur_con, n_cnt_con, n_tpa_con, n_crim_con, n_crpc_con, n_evi_con, n_cpc_con, n_soc_con = 0, 0, 0, 0, 0, 0, 0, 0, 0
else:
    n_const_con, n_jur_con, n_cnt_con, n_tpa_con, n_crim_con, n_crpc_con, n_evi_con, n_cpc_con, n_soc_con = map(int, res_con.stdout.strip().split())

test("Constitution authored concepts count is exactly 45", n_const_con == 45, f"Got {n_const_con}")
test("Jurisprudence authored concepts count is exactly 30", n_jur_con == 30, f"Got {n_jur_con}")
test("Contract Law authored concepts count is exactly 32", n_cnt_con == 32, f"Got {n_cnt_con}")
test("Transfer of Property Act authored concepts count is exactly 24", n_tpa_con == 24, f"Got {n_tpa_con}")
test("Criminal Law authored concepts count is exactly 36", n_crim_con == 36, f"Got {n_crim_con}")
test("Criminal Procedure authored concepts count is exactly 35", n_crpc_con == 35, f"Got {n_crpc_con}")
test("Law of Evidence authored concepts count is exactly 30", n_evi_con == 30, f"Got {n_evi_con}")
test("Code of Civil Procedure authored concepts count is exactly 57", n_cpc_con == 57, f"Got {n_cpc_con}")
test("Social Legislation authored concepts count is exactly 84", n_soc_con == 84, f"Got {n_soc_con}")
total_concepts = n_const_con + n_jur_con + n_cnt_con + n_tpa_con + n_crim_con + n_crpc_con + n_evi_con + n_cpc_con + n_soc_con
test("Total authored concepts across all 17 subjects equals exactly 373", total_concepts == 373, f"Got {total_concepts}")

# 5. Practice MCQs Bank (3,075 Questions Total)
print("\n--- TEST GROUP 5: COMPREHENSIVE PRACTICE MCQ BANK (3,075 MCQs TOTAL) ---")
script_mcq = """
global.window = global;
require('./assets/learning/data/constitution/constitution-mcqs.js');
require('./assets/learning/data/jurisprudence/jurisprudence-mcqs.js');
require('./assets/learning/data/contract/contract-mcqs.js');
require('./assets/learning/data/tpa/tpa-mcqs.js');
require('./assets/learning/data/criminal/criminal-mcqs.js');
require('./assets/learning/data/crpc/crpc-mcqs.js');
require('./assets/learning/data/evidence/evidence-mcqs.js');
require('./assets/learning/data/cpc/cpc-mcqs.js');
require('./assets/learning/data/social/social-mcqs.js');

const mConst = global.CONSTITUTION_MCQS;
const mJur = global.JURISPRUDENCE_MCQS;
const mCnt = global.CONTRACT_MCQS;
const mTpa = global.TPA_MCQS;
const mCrim = global.CRIMINAL_MCQS;
const mCrpc = global.CRPC_MCQS;
const mEvi = global.EVIDENCE_MCQS;
const mCpc = global.CPC_MCQS;
const mSoc = global.SOCIAL_MCQS;

const allMCQs = [...mConst, ...mJur, ...mCnt, ...mTpa, ...mCrim, ...mCrpc, ...mEvi, ...mCpc, ...mSoc];
const uniqueIds = new Set(allMCQs.map(x=>x.id)).size;
const bad = allMCQs.filter(q => q.options.length !== 4 || !q.explanation || !q.optionBreakdown.A || !q.optionBreakdown.B || !q.optionBreakdown.C || !q.optionBreakdown.D || !q.provision);
console.log(mConst.length, mJur.length, mCnt.length, mTpa.length, mCrim.length, mCrpc.length, mEvi.length, mCpc.length, mSoc.length, allMCQs.length, uniqueIds, bad.length);
"""
res_mcq = subprocess.run(['node', '-e', script_mcq], capture_output=True, text=True)
if res_mcq.returncode != 0:
    print("MCQ eval error:", res_mcq.stderr)
    n_c_mcq, n_j_mcq, n_cnt_mcq, n_t_mcq, n_crim_mcq, n_crpc_mcq, n_evi_mcq, n_cpc_mcq, n_soc_mcq, mcq_total, mcq_unique, bad_mcqs = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
else:
    n_c_mcq, n_j_mcq, n_cnt_mcq, n_t_mcq, n_crim_mcq, n_crpc_mcq, n_evi_mcq, n_cpc_mcq, n_soc_mcq, mcq_total, mcq_unique, bad_mcqs = map(int, res_mcq.stdout.strip().split())

test("Constitution Practice MCQs count is exactly 480", n_c_mcq == 480, f"Got {n_c_mcq}")
test("Jurisprudence Practice MCQs count is exactly 240", n_j_mcq == 240, f"Got {n_j_mcq}")
test("Contract Law Practice MCQs count is exactly 260", n_cnt_mcq == 260, f"Got {n_cnt_mcq}")
test("Transfer of Property Act Practice MCQs count is exactly 240", n_t_mcq == 240, f"Got {n_t_mcq}")
test("Criminal Law Practice MCQs count is exactly 360", n_crim_mcq == 360, f"Got {n_crim_mcq}")
test("Criminal Procedure Practice MCQs count is exactly 360", n_crpc_mcq == 360, f"Got {n_crpc_mcq}")
test("Law of Evidence Practice MCQs count is exactly 280", n_evi_mcq == 280, f"Got {n_evi_mcq}")
test("Code of Civil Procedure Practice MCQs count is exactly 400", n_cpc_mcq == 400, f"Got {n_cpc_mcq}")
test("Social Legislation Practice MCQs count is exactly 455", n_soc_mcq == 455, f"Got {n_soc_mcq}")
test("Total Practice MCQs across all 17 subjects is exactly 3,075", mcq_total == 3075, f"Got {mcq_total}")
test("All 3,075 MCQ IDs are globally unique across all 17 subjects", mcq_unique == 3075, f"Got {mcq_unique}")
test("100% of MCQs (3,075/3,075) have 4 options, full option breakdowns (A/B/C/D), explanation & statutory provision", bad_mcqs == 0, f"{bad_mcqs} malformed MCQs")

# 6. PYQ Mapping Across 17 Subjects (615 Mapped PYQs Total)
print("\n--- TEST GROUP 6: HISTORICAL PYQ MAPPINGS (615 MAPPED PYQS TOTAL) ---")
script_pyq = """
require('./assets/learning/data/constitution/constitution-pyq-mapping.js');
require('./assets/learning/data/jurisprudence/jurisprudence-pyq-mapping.js');
require('./assets/learning/data/contract/contract-pyq-mapping.js');
require('./assets/learning/data/tpa/tpa-pyq-mapping.js');
require('./assets/learning/data/criminal/criminal-pyq-mapping.js');
require('./assets/learning/data/crpc/crpc-pyq-mapping.js');
require('./assets/learning/data/evidence/evidence-pyq-mapping.js');
require('./assets/learning/data/cpc/cpc-pyq-mapping.js');
require('./assets/learning/data/social/social-pyq-mapping.js');

const pConst = global.CONSTITUTION_PYQ_MAPPING;
const pJur = global.JURISPRUDENCE_PYQ_MAPPING;
const pCnt = global.CONTRACT_PYQ_MAPPING;
const pTpa = global.TPA_PYQ_MAPPING;
const pCrim = global.CRIMINAL_PYQ_MAPPING;
const pCrpc = global.CRPC_PYQ_MAPPING;
const pEvi = global.EVIDENCE_PYQ_MAPPING;
const pCpc = global.CPC_PYQ_MAPPING;
const pSoc = global.SOCIAL_PYQ_MAPPING;

const total = pConst.length + pJur.length + pCnt.length + pTpa.length + pCrim.length + pCrpc.length + pEvi.length + pCpc.length + pSoc.length;
console.log(pConst.length, pJur.length, pCnt.length, pTpa.length, pCrim.length, pCrpc.length, pEvi.length, pCpc.length, pSoc.length, total);
"""
res_pyq = subprocess.run(['node', '-e', script_pyq], capture_output=True, text=True)
if res_pyq.returncode != 0:
    print("PYQ eval error:", res_pyq.stderr)
    p_c, p_j, p_cnt, p_t, p_crim, p_crpc, p_evi, p_cpc, p_soc, pyq_total = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
else:
    p_c, p_j, p_cnt, p_t, p_crim, p_crpc, p_evi, p_cpc, p_soc, pyq_total = map(int, res_pyq.stdout.strip().split())

test("Constitution mapped authentic PYQs count is 158", p_c == 158, f"Got {p_c}")
test("Jurisprudence mapped authentic PYQs count is 45", p_j == 45, f"Got {p_j}")
test("Contract Law mapped authentic PYQs count is 82", p_cnt == 82, f"Got {p_cnt}")
test("Transfer of Property Act mapped authentic PYQs count is 47", p_t == 47, f"Got {p_t}")
test("Criminal Law mapped authentic PYQs count is 78", p_crim == 78, f"Got {p_crim}")
test("Criminal Procedure mapped authentic PYQs count is 49", p_crpc == 49, f"Got {p_crpc}")
test("Law of Evidence mapped authentic PYQs count is 73", p_evi == 73, f"Got {p_evi}")
test("Code of Civil Procedure mapped authentic PYQs count is 60", p_cpc == 60, f"Got {p_cpc}")
test("Social Legislation mapped authentic PYQs count is 23", p_soc == 23, f"Got {p_soc}")
test("Total mapped authentic PYQs across 17 subjects equals exactly 615", pyq_total == 615, f"Got {pyq_total}")

# 7. Academic SVG Diagrams (90 Diagrams Total)
print("\n--- TEST GROUP 7: ACADEMIC SVG DIAGRAMS (90 DIAGRAMS TOTAL) ---")
expected_diagrams = [
    # 12 Constitution
    "diag-historical-timeline.svg",
    "diag-sources-features.svg",
    "diag-preamble-pillars.svg",
    "diag-golden-triangle.svg",
    "diag-five-writs.svg",
    "diag-dpsp-classification.svg",
    "diag-two-wheels-chariot.svg",
    "diag-parliament-bills.svg",
    "diag-judicial-hierarchy.svg",
    "diag-emergency-comparison.svg",
    "diag-amendment-process.svg",
    "diag-federal-distribution.svg",
    # 8 Jurisprudence
    "diag-jur-schools-comparison.svg",
    "diag-jur-sources-of-law.svg",
    "diag-jur-hohfeld-table.svg",
    "diag-jur-legal-personality.svg",
    "diag-jur-ownership-possession.svg",
    "diag-jur-liability-types.svg",
    "diag-jur-jurists-theories.svg",
    "diag-jur-law-morality.svg",
    # 8 Contract Law
    "diag-cnt-agreement-vs-contract.svg",
    "diag-cnt-validity-consent.svg",
    "diag-cnt-coercion-undue-influence.svg",
    "diag-cnt-fraud-misrep.svg",
    "diag-cnt-void-agreements.svg",
    "diag-cnt-discharge-contract.svg",
    "diag-cnt-hadley-damages.svg",
    "diag-cnt-indemnity-guarantee-bailment.svg",
    # 8 Transfer of Property Act
    "diag-tpa-transferability-s6.svg",
    "diag-tpa-perpetuity-s14.svg",
    "diag-tpa-vested-contingent.svg",
    "diag-tpa-ostensible-owner-s41.svg",
    "diag-tpa-lis-pendens-s52.svg",
    "diag-tpa-part-performance-s53a.svg",
    "diag-tpa-types-of-mortgage.svg",
    "diag-tpa-lease-determination.svg",
    # 8 Criminal Law
    "diag-crim-culpable-homicide-murder.svg",
    "diag-crim-hit-and-run-caveat.svg",
    "diag-crim-joint-liability-common-intention.svg",
    "diag-crim-kidnapping-vs-abduction.svg",
    "diag-crim-mens-rea-liability.svg",
    "diag-crim-private-defence-spectrum.svg",
    "diag-crim-property-offences-gradation.svg",
    "diag-crim-punishments-bns.svg",
    # 8 Criminal Procedure
    "diag-crpc-arrest-safeguards.svg",
    "diag-crpc-bail-framework.svg",
    "diag-crpc-courts-hierarchy.svg",
    "diag-crpc-investigation-flowchart.svg",
    "diag-crpc-maintenance-s144.svg",
    "diag-crpc-remand-custody-timeline.svg",
    "diag-crpc-trial-in-absentia.svg",
    "diag-crpc-trials-comparison.svg",
    # 8 Law of Evidence
    "diag-evi-burden-of-proof-spectrum.svg",
    "diag-evi-confessions-landscape.svg",
    "diag-evi-dying-declaration-rules.svg",
    "diag-evi-electronic-evidence-cert.svg",
    "diag-evi-estoppel-types.svg",
    "diag-evi-relevancy-vs-admissibility.svg",
    "diag-evi-res-gestae-flowchart.svg",
    "diag-evi-witness-examination-stages.svg",
    # 12 Code of Civil Procedure (Phase 4)
    "diag-cpc-civil-suit-journey.svg",
    "diag-cpc-jurisdiction-s9.svg",
    "diag-cpc-res-sub-judice-judicata.svg",
    "diag-cpc-parties-suits.svg",
    "diag-cpc-plaint-ws-setoff.svg",
    "diag-cpc-return-vs-rejection.svg",
    "diag-cpc-exparte-default-remedies.svg",
    "diag-cpc-civil-trial-sequence.svg",
    "diag-cpc-interim-relief-injunctions.svg",
    "diag-cpc-execution-framework.svg",
    "diag-cpc-appeals-hierarchy.svg",
    "diag-cpc-reference-review-revision.svg",
    # 18 Social Legislation (Phase 5: 2 per Act)
    "diag-soc-disab-rights-framework.svg",
    "diag-soc-disab-accessibility.svg",
    "diag-soc-parent-tribunal-flow.svg",
    "diag-soc-parent-maintenance-comparison.svg",
    "diag-soc-dowry-offences-elements.svg",
    "diag-soc-dowry-vs-gifts.svg",
    "diag-soc-dv-remedies-hierarchy.svg",
    "diag-soc-dv-domestic-relationship.svg",
    "diag-soc-posh-complaint-inquiry.svg",
    "diag-soc-posh-ic-vs-lc.svg",
    "diag-soc-pcpndt-regulatory-architecture.svg",
    "diag-soc-pcpndt-prohibited-conduct.svg",
    "diag-soc-mtp-gestational-framework.svg",
    "diag-soc-mtp-consent-medical-board.svg",
    "diag-soc-irwa-prohibitions-exceptions.svg",
    "diag-soc-irwa-enforcement-powers.svg",
    "diag-soc-pocso-protection-framework.svg",
    "diag-soc-pocso-special-court-trial.svg",
    # 15 General Knowledge Diagrams (Phase 6)
    "diag-hist-ancient-timeline.svg",
    "diag-hist-delhi-sultanate.svg",
    "diag-hist-indus-sites.svg",
    "diag-hist-mughal-timeline.svg",
    "diag-hist-national-movement.svg",
    "diag-cult-classical-dances.svg",
    "diag-cult-schools-sculpture.svg",
    "diag-cult-temple-architecture.svg",
    "diag-geo-drainage-systems.svg",
    "diag-geo-monsoon-mechanism.svg",
    "diag-geo-physiographic-divisions.svg",
    "diag-pol-law-making-process.svg",
    "diag-pol-union-executive.svg",
    "diag-econ-monetary-policy-transmission.svg",
    "diag-econ-national-income-flow.svg"
]
diag_dir = "assets/learning/images/diagrams"
missing_diags = [d for d in expected_diagrams if not os.path.exists(os.path.join(diag_dir, d))]
test(f"All 105 Academic SVG diagrams exist on disk (12 Const + 60 Law + 18 Social + 15 GK)", len(missing_diags) == 0 and len(expected_diagrams) == 105, f"Missing: {missing_diags}, Total expected: {len(expected_diagrams)}")

# 8. Statutory Comparisons Dataset (79 Mapped Comparisons)
print("\n--- TEST GROUP 8: STATUTORY COMPARISONS (79 MAPPED COMPARISONS) ---")
script_comp = """
require('./assets/learning/data/comparison/criminal-statutory-comparisons.js');
const comps = global.STATUTORY_COMPARISONS;
const uniqueIds = new Set(comps.map(c => c.id)).size;
const bns = comps.filter(c => c.subject === 'law-criminal').length;
const bnss = comps.filter(c => c.subject === 'law-crpc').length;
const bsa = comps.filter(c => c.subject === 'law-evidence').length;
const stayed = comps.filter(c => c.commencementStatus && c.commencementStatus.includes('NOT in force')).length;
console.log(comps.length, uniqueIds, bns, bnss, bsa, stayed);
"""
res_comp = subprocess.run(['node', '-e', script_comp], capture_output=True, text=True)
if res_comp.returncode != 0:
    print("Comp eval error:", res_comp.stderr)
    n_comp_tot, n_comp_uniq, n_comp_bns, n_comp_bnss, n_comp_bsa, n_comp_stayed = 0, 0, 0, 0, 0, 0
else:
    n_comp_tot, n_comp_uniq, n_comp_bns, n_comp_bnss, n_comp_bsa, n_comp_stayed = map(int, res_comp.stdout.strip().split())

test("Statutory Comparison Lab has exactly 79 mapped transitions", n_comp_tot == 79, f"Got {n_comp_tot}")
test("All 79 comparison records have unique IDs", n_comp_uniq == 79, f"Got {n_comp_uniq}")
test("BNS ↔ IPC comparisons count is 30", n_comp_bns == 30, f"Got {n_comp_bns}")
test("BNSS ↔ CrPC comparisons count is 21", n_comp_bnss == 21, f"Got {n_comp_bnss}")
test("BSA ↔ IEA comparisons count is 28", n_comp_bsa == 28, f"Got {n_comp_bsa}")
test("Section 106(2) BNS uncommenced caveat is explicitly flagged as NOT in force", n_comp_stayed >= 1, f"Got {n_comp_stayed}")

# 9. Node.js Syntax Check on All Learning JS Files
print("\n--- TEST GROUP 9: JAVASCRIPT SYNTAX VALIDATION ---")
learning_js_files = glob.glob("assets/learning/**/*.js", recursive=True)
js_errors = 0
for jf in learning_js_files:
    res = subprocess.run(f"node -c {jf}", shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        js_errors += 1
        print(f"  Syntax Error in {jf}: {res.stderr}")
test(f"All {len(learning_js_files)} learning JavaScript files compile cleanly with zero syntax errors", js_errors == 0, f"{js_errors} files failed")

# 10. HTML Pages Verification (27 Pages Total)
print("\n--- TEST GROUP 10: HTML PAGES VERIFICATION (27 PAGES TOTAL) ---")
expected_pages = [
    "learning-academy.html",
    "comparison-lab.html",
    "subject-study.html",
    "topic-practice.html",
    "subject-progress.html",
    "civil-suit-journey.html"
]
missing_pages = [p for p in expected_pages if not os.path.exists(p)]
test("All 6 operational Learning Academy, Comparison Lab & Civil Suit Journey HTML pages exist", len(missing_pages) == 0, f"Missing: {missing_pages}")

all_pages = glob.glob("*.html")
test("Total operational HTML pages is 27", len(all_pages) == 27, f"Got {len(all_pages)}")

missing_nav = []
for p in all_pages:
    txt = open(p, encoding="utf-8").read()
    if "learning-academy.html" not in txt:
        missing_nav.append(p)
test("100% of HTML pages (all 27) contain Subject Academy in navigation", len(missing_nav) == 0, f"Missing in: {missing_nav}")

# 11. Universal Smart Search Integration
print("\n--- TEST GROUP 11: SMART SEARCH INTEGRATION ---")
search_js = open("assets/js/legal-search.js", encoding="utf-8").read()
test("Smart search indexes all active subject topics and MCQs including SOCIAL_TOPICS and SOCIAL_MCQS",
     "CPC_TOPICS" in search_js and "SOCIAL_TOPICS" in search_js and "SOCIAL_MCQS" in search_js)
test("Smart search displays 5th corpus for Judicial Learning Academy", "Judicial Learning Academy" in search_js)

# 12. Unified Backup & Storage Schema v3.1.0
print("\n--- TEST GROUP 12: UNIFIED BACKUP & STORAGE SCHEMA ---")
app_js = open("assets/js/app.js", encoding="utf-8").read()
test("exportProgress creates schema v3.1.0 with learning namespace", 'version: "3.1.0"' in app_js and 'learning: learningData' in app_js)
test("importProgress restores tanveer-learning-v1 key", "tanveer-learning-v1" in app_js)

# 13. CPC Section-Order-Rule Explorer Dataset Validation
print("\n--- TEST GROUP 13: CPC SECTION-ORDER-RULE EXPLORER DATASET ---")
script_sor = """
const sor = require('./assets/learning/data/cpc/cpc-sections-orders-rules.js');
const uniqueIds = new Set(sor.map(s => s.id)).size;
const sections = sor.filter(s => s.type === 'section').length;
const rules = sor.filter(s => s.type === 'rule').length;
const hasUp = sor.filter(s => s.examTips && s.examTips.length > 0).length;
console.log(sor.length, uniqueIds, sections, rules, hasUp);
"""
res_sor = subprocess.run(['node', '-e', script_sor], capture_output=True, text=True)
if res_sor.returncode != 0:
    print("SOR eval error:", res_sor.stderr)
    sor_tot, sor_uniq, sor_sec, sor_rul, sor_up = 0, 0, 0, 0, 0
else:
    sor_tot, sor_uniq, sor_sec, sor_rul, sor_up = map(int, res_sor.stdout.strip().split())

test("CPC Section-Order-Rule Explorer contains 83 high-yield statutory entries", sor_tot == 83, f"Got {sor_tot}")
test("All 83 entries have globally unique IDs", sor_uniq == 83, f"Got {sor_uniq}")
test("Section entries count is 48", sor_sec == 48, f"Got {sor_sec}")
test("Rule entries count is 35", sor_rul == 35, f"Got {sor_rul}")
test("100% of entries (83/83) have authored UP Exam & Practical Relevance (examTips)", sor_up == 83, f"Got {sor_up}")

# 14. The Civil Suit Journey Simulator Validation
print("\n--- TEST GROUP 14: THE CIVIL SUIT JOURNEY SIMULATOR ---")
csj_html = open("civil-suit-journey.html", encoding="utf-8").read()
test("civil-suit-journey.html contains all 14 sequential stages", "Stage 14 of 14" in csj_html or "STAGE 14 · ENFORCEMENT" in csj_html)
test("civil-suit-journey.html contains Presiding Officer Scrutiny Checklist", "Presiding Officer's Scrutiny Checklist" in csj_html)
test("civil-suit-journey.html contains High-Yield Traps & Exceptions", "High-Yield Procedural Trap" in csj_html)
test("civil-suit-journey.html contains Landmark Judicial Precedents", "Landmark Judicial Precedents" in csj_html)
test("civil-suit-journey.html embeds master flowchart diagram diag-cpc-civil-suit-journey.svg", "diag-cpc-civil-suit-journey.svg" in csj_html)

# 15. Social Legislation Sections Explorer Dataset Validation
print("\n--- TEST GROUP 15: SOCIAL LEGISLATION SECTIONS EXPLORER DATASET ---")
script_soc_exp = """
const exp = require('./assets/learning/data/social/social-sections-explorer.js');
const uniqueIds = new Set(exp.map(s => s.id)).size;
const acts = new Set(exp.map(s => s.subjectId)).size;
const hasUp = exp.filter(s => s.examTips && s.examTips.length > 0).length;
console.log(exp.length, uniqueIds, acts, hasUp);
"""
res_soc_exp = subprocess.run(['node', '-e', script_soc_exp], capture_output=True, text=True)
if res_soc_exp.returncode != 0:
    print("Social Explorer eval error:", res_soc_exp.stderr)
    soc_tot, soc_uniq, soc_acts, soc_up = 0, 0, 0, 0
else:
    soc_tot, soc_uniq, soc_acts, soc_up = map(int, res_soc_exp.stdout.strip().split())

test("Social Legislation Sections Explorer contains 98 high-yield statutory entries", soc_tot == 98, f"Got {soc_tot}")
test("All 98 entries have globally unique IDs", soc_uniq == 98, f"Got {soc_uniq}")
test("Entries span all 9 Social Legislation Acts", soc_acts == 9, f"Got {soc_acts}")
test("100% of entries (98/98) have authored UP Exam & Practical Relevance (examTips)", soc_up == 98, f"Got {soc_up}")

# 16. General Knowledge Learning Academy (5 Active Subjects & Phase 6 Grand Totals)
print("\n--- TEST GROUP 16: GENERAL KNOWLEDGE LEARNING ACADEMY (5 ACTIVE SUBJECTS & GRAND TOTALS) ---")
script_gk = """
const hCh = require('./assets/learning/data/history/history-chapters.js').chapters;
const hTop = require('./assets/learning/data/history/history-topics.js').topics;
const hCon = require('./assets/learning/data/history/history-concepts.js').concepts;
const hMcq = require('./assets/learning/data/history/history-mcqs.js').mcqs;
const hPyq = require('./assets/learning/data/history/history-pyq-mapping.js').pyqs;

const cCh = require('./assets/learning/data/culture/culture-chapters.js').chapters;
const cTop = require('./assets/learning/data/culture/culture-topics.js').topics;
const cCon = require('./assets/learning/data/culture/culture-concepts.js').concepts;
const cMcq = require('./assets/learning/data/culture/culture-mcqs.js').mcqs;
const cPyq = require('./assets/learning/data/culture/culture-pyq-mapping.js').pyqs;

const gCh = require('./assets/learning/data/geography/geography-chapters.js').chapters;
const gTop = require('./assets/learning/data/geography/geography-topics.js').topics;
const gCon = require('./assets/learning/data/geography/geography-concepts.js').concepts;
const gMcq = require('./assets/learning/data/geography/geography-mcqs.js').mcqs;
const gPyq = require('./assets/learning/data/geography/geography-pyq-mapping.js').pyqs;

const pCh = require('./assets/learning/data/polity/polity-chapters.js').chapters;
const pTop = require('./assets/learning/data/polity/polity-topics.js').topics;
const pCon = require('./assets/learning/data/polity/polity-concepts.js').concepts;
const pMcq = require('./assets/learning/data/polity/polity-mcqs.js').mcqs;
const pPyq = require('./assets/learning/data/polity/polity-pyq-mapping.js').pyqs;

const eCh = require('./assets/learning/data/economy/economy-chapters.js').chapters;
const eTop = require('./assets/learning/data/economy/economy-topics.js').topics;
const eCon = require('./assets/learning/data/economy/economy-concepts.js').concepts;
const eMcq = require('./assets/learning/data/economy/economy-mcqs.js').mcqs;
const ePyq = require('./assets/learning/data/economy/economy-pyq-mapping.js').pyqs;

console.log(
  hCh.length, hTop.length, Object.keys(hCon).length, hMcq.length, hPyq.length,
  cCh.length, cTop.length, Object.keys(cCon).length, cMcq.length, cPyq.length,
  gCh.length, gTop.length, Object.keys(gCon).length, gMcq.length, gPyq.length,
  pCh.length, pTop.length, Object.keys(pCon).length, pMcq.length, pPyq.length,
  eCh.length, eTop.length, Object.keys(eCon).length, eMcq.length, ePyq.length
);
"""
res_gk = subprocess.run(['node', '-e', script_gk], capture_output=True, text=True)
if res_gk.returncode != 0:
    print("GK eval error:", res_gk.stderr)
    gk_vals = [0]*25
else:
    gk_vals = list(map(int, res_gk.stdout.strip().split()))

h_ch, h_top, h_con, h_mcq, h_pyq = gk_vals[0:5]
c_ch, c_top, c_con, c_mcq, c_pyq = gk_vals[5:10]
g_ch, g_top, g_con, g_mcq, g_pyq = gk_vals[10:15]
p_ch, p_top, p_con, p_mcq, p_pyq = gk_vals[15:20]
e_ch, e_top, e_con, e_mcq, e_pyq = gk_vals[20:25]

test("History of India: 15 Ch, 38 Top, 38 Concepts, 160 MCQs, 52 PYQs",
     h_ch == 15 and h_top == 38 and h_con == 38 and h_mcq == 160 and h_pyq == 52,
     f"Got {h_ch} ch, {h_top} top, {h_con} con, {h_mcq} mcq, {h_pyq} pyq")

test("Indian Culture: 12 Ch, 28 Top, 28 Concepts, 120 MCQs, 30 PYQs",
     c_ch == 12 and c_top == 28 and c_con == 28 and c_mcq == 120 and c_pyq == 30,
     f"Got {c_ch} ch, {c_top} top, {c_con} con, {c_mcq} mcq, {c_pyq} pyq")

test("Indian Geography: 12 Ch, 32 Top, 32 Concepts, 140 MCQs, 48 PYQs",
     g_ch == 12 and g_top == 32 and g_con == 32 and g_mcq == 140 and g_pyq == 48,
     f"Got {g_ch} ch, {g_top} top, {g_con} con, {g_mcq} mcq, {g_pyq} pyq")

test("Indian Polity: 12 Ch, 30 Top, 30 Concepts, 140 MCQs, 60 PYQs",
     p_ch == 12 and p_top == 30 and p_con == 30 and p_mcq == 140 and p_pyq == 60,
     f"Got {p_ch} ch, {p_top} top, {p_con} con, {p_mcq} mcq, {p_pyq} pyq")

test("Indian Economy: 14 Ch, 34 Top, 34 Concepts, 140 MCQs, 38 PYQs",
     e_ch == 14 and e_top == 34 and e_con == 34 and e_mcq == 140 and e_pyq == 38,
     f"Got {e_ch} ch, {e_top} top, {e_con} con, {e_mcq} mcq, {e_pyq} pyq")

gk_ch_tot = h_ch + c_ch + g_ch + p_ch + e_ch
gk_top_tot = h_top + c_top + g_top + p_top + e_top
gk_con_tot = h_con + c_con + g_con + p_con + e_con
gk_mcq_tot = h_mcq + c_mcq + g_mcq + p_mcq + e_mcq
gk_pyq_tot = h_pyq + c_pyq + g_pyq + p_pyq + e_pyq

test("Total GK modules: 65 Chapters, 162 Topics, 162 Concepts, 700 MCQs, 228 PYQs",
     gk_ch_tot == 65 and gk_top_tot == 162 and gk_con_tot == 162 and gk_mcq_tot == 700 and gk_pyq_tot == 228,
     f"Got {gk_ch_tot} ch, {gk_top_tot} top, {gk_con_tot} con, {gk_mcq_tot} mcq, {gk_pyq_tot} pyq")

grand_chapters = total_chapters + gk_ch_tot
grand_topics = total_topics + gk_top_tot
grand_concepts = total_concepts + gk_con_tot
grand_mcqs = mcq_total + gk_mcq_tot
grand_pyqs = 615 + gk_pyq_tot

test("Grand Total Academy Chapters across all 22 subjects equals exactly 192", grand_chapters == 192, f"Got {grand_chapters}")
test("Grand Total Academy Topics across all 22 subjects equals exactly 535", grand_topics == 535, f"Got {grand_topics}")
test("Grand Total Authored Concepts across all 22 subjects equals exactly 535", grand_concepts == 535, f"Got {grand_concepts}")
test("Grand Total Practice MCQs across all 22 subjects equals exactly 3,775", grand_mcqs == 3775, f"Got {grand_mcqs}")
test("Grand Total Mapped Authentic PYQs across all 22 subjects equals exactly 843", grand_pyqs == 843, f"Got {grand_pyqs}")

# Final Result
print("\n================================================================================")
if len(errors) == 0:
    print("ALL TESTS PASSED! (100% SUCCESS RATE)")
    print("V3.1 Phase 6 Complete General Knowledge Learning Academy is 100% verified!")
    print("================================================================================")
    sys.exit(0)
else:
    print(f"FAILED WITH {len(errors)} ERROR(S):")
    for e in errors:
        print(f"  - {e}")
    print("================================================================================")
    sys.exit(1)
