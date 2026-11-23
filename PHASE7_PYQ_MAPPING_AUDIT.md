# PHASE 7 PYQ MAPPING AUDIT — AUTHENTIC QUESTION PRESERVATION & RECONCILIATION
## Tanveer Ashraf — Judicial Prep 2026–27
**Audit Baseline:** Phase 7 Expansion  
**Underlying Historical Database:** `assets/data/questions.js` (1,800 historical questions across 6 UP PCS-J years: 2012, 2013, 2015, 2016, 2018, 2023).

---

## 1. Database Integrity Verification

The base question bank (`assets/data/questions.js`) remains **100% untouched and uncorrupted**:
- **Total Historical Question Slots:** Exactly 1,800 records.
- **Scorable Eligible Questions (`eligible: true`):** Exactly 1,757 records.
- **Ineligible / Disputed Questions (`eligible: false`):** Exactly 43 records (including `2016-GK-31` which was cancelled by UPPSC).
- **Zero Modifications:** No question text was altered, no answer key was modified, and no modern statutes were back-projected onto historical questions.

---

## 2. PYQ Mapping Distribution Across All 30 Subjects

| Academic Subject | Subject ID | Paper | Mapped Authentic PYQs | Phase |
| :--- | :--- | :---: | :---: | :---: |
| **Constitution of India** | `law-constitution` | Paper II | 158 | Phase 1 |
| **Jurisprudence** | `law-jurisprudence` | Paper II | 45 | Phase 2 |
| **Law of Contract** | `law-contract` | Paper II | 82 | Phase 2 |
| **Transfer of Property Act** | `law-tpa` | Paper II | 47 | Phase 2 |
| **Criminal Law (BNS & IPC)** | `law-criminal` | Paper II | 78 | Phase 3 |
| **Criminal Procedure (BNSS & CrPC)** | `law-crpc` | Paper II | 49 | Phase 3 |
| **Law of Evidence (BSA & IEA)** | `law-evidence` | Paper II | 73 | Phase 3 |
| **Code of Civil Procedure, 1908** | `law-cpc` | Paper II | 60 | Phase 4 |
| **Social Legislation (9 Special Acts)** | `soc-*` | Paper I | 23 | Phase 5 |
| **History of India** | `gk-history` | Paper I | 52 | Phase 6 |
| **Indian Culture** | `gk-culture` | Paper I | 30 | Phase 6 |
| **Indian Geography** | `gk-geography` | Paper I | 48 | Phase 6 |
| **Indian Polity** | `gk-polity` | Paper I | 60 | Phase 6 |
| **Indian Economy** | `gk-economy` | Paper I | 38 | Phase 6 |
| **Current National Issues** | `gk-current` | Paper I | **90** | **Phase 7** |
| **Issues of Social Relevance** | `gk-social` | Paper I | **44** | **Phase 7** |
| **International Affairs & Institutions** | `gk-international` | Paper I | **61** | **Phase 7** |
| **General Science** | `gk-science` | Paper I | **88** | **Phase 7** |
| **Technology & IT** | `gk-tech` | Paper I | **8** | **Phase 7** |
| **Communications** | `gk-comm` | Paper I | **4** | **Phase 7** |
| **Space Science** | `gk-space` | Paper I | **27** | **Phase 7** |
| **International Organisations & Law** | `law-international` | Paper II | **88** | **Phase 7** |
| **Total Mapped PYQs Across Academy** | **30 Subjects** | **Both Papers** | **1,253** | **Grand Total** |

---

## 3. Phase 7 Subject PYQ Mapping Analysis

### A. Current National Issues (`gk-current` — 90 PYQs)
- Mapped historical current affairs questions across Paper I (national policies, budget allocations, government flagship schemes, census data, national awards, and state appointments).
- Provides candidate with empirical insight into how UPPSC structures current affairs queries (predominantly factual, appointment-based, scheme milestones, and landmark supreme court benches).

### B. Issues of Social Relevance (`gk-social` — 44 PYQs)
- Mapped questions concerning affirmative action policies, constitutional safeguards for SCs, STs, and women, poverty alleviation programmes, and child welfare initiatives.

### C. International Affairs & Institutions (`gk-international` — 61 PYQs)
- Mapped Paper I queries covering UN organs, headquarters locations, specialized agency mandates, international summits (G20, BRICS, NAM, SAARC), and global environmental treaties.

### D. General Science (`gk-science` — 88 PYQs)
- Mapped Paper I General Science questions across Physics (optics, lenses, units, Newton's laws), Chemistry (acids, bases, polymers, alloys), and Biology/Health (deficiency diseases, vitamins, human endocrine glands, vaccines).

### E. Technology & IT (`gk-tech` — 8 PYQs)
- Mapped historical technology questions covering computer fundamentals, internet protocols, and digital initiatives.

### F. Communications (`gk-comm` — 4 PYQs)
- Mapped historical questions on telecommunications, optical fibre, and cellular frequency spectrum.

### G. Space Science (`gk-space` — 27 PYQs)
- Mapped questions on ISRO missions, satellites (INSAT, IRS, Chandrayaan, Mangalyaan), launch vehicles (PSLV, GSLV), and astronomical concepts.

### H. International Organisations & Law (`law-international` — 88 PYQs)
- Mapped Paper II Law questions testing UN Charter articles, ICJ Statute jurisdiction, VCLT rules, UNCLOS maritime zones, and landmark PCIJ/ICJ precedents.
- Represents one of the highest-yield Paper II subjects with 88 authentic questions directly illuminating UPPSC's exam patterns.

---

## 4. Methodological Safeguards
1. **Zero Duplicate Mappings:** Each mapping references a valid question `id` in `window.PCSJ_QUESTIONS`.
2. **Contextual Tagging:** Questions are tagged with `relevance` tags (e.g. `direct-syllabus`, `historical-precedent`, `statutory-foundation`).
3. **Option Authenticity:** All options (A, B, C, D) reflect the authentic historical paper as administered by UPPSC.
