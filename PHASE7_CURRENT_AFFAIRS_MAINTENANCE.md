# PHASE 7 CURRENT AFFAIRS MAINTENANCE & RUNBOOK (V3.1.9)
## Date-Wise Current Affairs Desk (`current-desk.js` & `current-desk-ui.js`)
**Project:** Tanveer Ashraf — Judicial Prep 2026–27  
**Module:** Date-Wise Current Affairs Desk  
**Current Development Date:** November 23, 2026 (Asia/Kolkata)  
**Target Examination:** Uttar Pradesh Judicial Services Examination (UP PCS-J)  

---

## 1. Architectural Overview

The Date-Wise Current Affairs Desk is implemented as a **100% client-side, zero-backend, zero-build system**:
1. **Data Layer (`assets/learning/data/current/current-desk.js`):**
   - Defines `window.CURRENT_AFFAIRS_DESK` (32 source-verified entry records across 2024, 2025, and 2026).
   - Defines `window.CURRENT_MONTHLY_ARCHIVE` (28 structured monthly overview periods with year tags).
2. **Presentation Layer (`assets/learning/js/current-desk-ui.js`):**
   - Automatically renders year period selector tabs (`All Periods`, `2026 Active Exam Year`, `2025 Archive Year`, `2024 Historical Archive`).
   - Dynamically filters monthly archive tabs per selected period.
   - Category filter pills (`Legal & Constitutional`, `National Governance & Policy`, `Uttar Pradesh State Affairs`, `Economic Reforms & Finance`, `Science, Space & Tech`, `Environment & Climate`).
   - Real-time debounced search across headlines, summaries, legal significance, sources, and traps.
   - Dynamic practice navigation linking each event to its specific topic (`practiceTopicId`) in `topic-practice.html`.
   - Any new entry added to `current-desk.js` is **automatically indexed, filtered, and rendered** without modifying any HTML or CSS files.

---

## 2. Standard Schema for Date-Wise Current Affairs Entries

Every entry in `CURRENT_AFFAIRS_DESK` must adhere strictly to the following 13 mandatory fields:

```javascript
{
  "id": "cad-2026-11-20",                              // Unique ID format: cad-YYYY-MM-DD
  "eventDate": "2026-11-20",                           // ISO YYYY-MM-DD
  "monthKey": "2026-11",                               // ISO YYYY-MM
  "headline": "Supreme Court Clarifies...",            // Professional, objective judicial headline
  "category": "Legal & Constitutional",                // One of 6 standardized categories (see Section 3)
  "sourceName": "Supreme Court of India",              // Authoritative public institution
  "sourceUrl": "https://main.sci.gov.in",              // Authoritative HTTPS primary URL
  "sourcePubDate": "2026-11-20",                       // ISO YYYY-MM-DD
  "verifiedAt": "2026-11-23T10:00:00Z",                // ISO-8601 UTC verification timestamp
  "summary": "Concise factual summary of the judicial, legislative, or administrative milestone.",
  "significance": "Detailed legal and constitutional analysis tailored to the UP PCS-J syllabus.",
  "explanation": "Mirror of significance for backwards UI compatibility.",
  "examTraps": [                                       // Array of minimum 1 high-yield pitfall or trap
    "Trap: Assuming digital certification is optional...",
    "Statutory cross-reference: Section 63 BSA replaces Section 65B IEA..."
  ],
  "examTakeaways": [ ... ],                            // Mirror of examTraps for backwards UI compatibility
  "practiceTopicId": "top-curr-03-01",                 // Valid topic ID in gk-current curriculum
  "reviewStatus": "verified",                          // 'verified' or 'pending_official_gazette'
  "subjectId": "gk-current",                           // Fixed subject ID
  "relatedMCQIds": ["mcq-curr-005", "mcq-curr-006"]    // Related MCQs in question bank
}
```

---

## 3. Standardized Categories

Entries must be classified into one of these six recognized categories:
1. `Legal & Constitutional`: Supreme Court Constitution Benches, High Court rulings, statutory transitions (BNS/BNSS/BSA), fundamental rights, and judicial administration.
2. `National Governance & Policy`: NITI Aayog indices, Election Commission guidelines, Parliamentary acts, regulatory commissions, and administrative accountability.
3. `Uttar Pradesh State Affairs`: UP state budgets, Allahabad High Court notifications, UP local statutory enactments, ODOP expansion, and district infrastructure.
4. `Economic Reforms & Finance`: Union Budgets, Finance Commission recommendations (Article 280), monetary policy frameworks, and macroeconomic indicators.
5. `Science, Space & Tech`: ISRO missions (Gaganyaan, Spadex, Chandrayaan-4, BAS), DPDP Act digital adjudication, and quantum/semiconductor initiatives.
6. `Environment & Climate`: UNFCCC COP summits, NGT precedents, wildlife conservation milestones, and renewable energy targets.

---

## 4. Standard Schema for Monthly Archives

When rolling into a new examination month, add an object to `CURRENT_MONTHLY_ARCHIVE`:

```javascript
{
  "monthKey": "2026-12",
  "year": "2026",
  "label": "December 2026",
  "summary": "Parliament Winter Session; Subordinate court digital courtroom reviews; Year-end judicial statistics.",
  "itemCount": 5,
  "highlight": "National judicial conference reviews subordinate court disposal rates under BNSS."
}
```

---

## 5. Verification Protocol & Gazette Standards

1. **Primary Sources Only:**
   - **Judicial:** Supreme Court official portal (`https://main.sci.gov.in`), Allahabad High Court (`https://allahabadhighcourt.in`), e-Courts Mission (`https://ecourts.gov.in`).
   - **Executive / Statutory:** Gazette of India (`https://egazette.gov.in`), Ministry of Home Affairs (`https://mha.gov.in`), PIB (`https://pib.gov.in`).
   - **Constitutional Bodies:** 16th Finance Commission (`https://fincomindia.nic.in`), Law Commission (`https://lawcommissionofindia.nic.in`), NITI Aayog (`https://niti.gov.in`).
   - **Science & Space:** ISRO (`https://isro.gov.in`), MeitY (`https://meity.gov.in`).
2. **Handling Uncommenced Provisions & Deferred Traps:**
   - Where a provision is withheld from commencement (e.g. Section 106(2) of Bharatiya Nyaya Sanhita 2023), set `reviewStatus: 'pending_official_gazette'`.
   - Never declare an uncommenced statute as active law without citing the specific commencement notification issued under the Act.
3. **Automated Verification:**
   - Run `python scripts/validate_learning_academy.py` to assert 100% schema compliance, valid date syntax, unique IDs, and valid topic linkages.
