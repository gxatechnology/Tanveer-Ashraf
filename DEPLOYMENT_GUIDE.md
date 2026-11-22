# DEPLOYMENT_GUIDE.md — Production Deployment & Release Protocols

**Project:** Tanveer Ashraf — Judicial Prep 2026–27  
**Author & Developer:** Tauqeer Ashraf  
**Target Environment (Primary):** Vercel CI/CD (`https://tanveer-ashraf-judicial.vercel.app`)  
**Target Environment (Secondary):** Hostinger Static Hosting (`public_html`)  
**Production Git Repository:** `https://github.com/gxatechnology/Tanveer-Ashraf.git`  
**Production Branch:** `main`  

---

## 1. Permanent Safety Notice

> [!IMPORTANT]
> **STRICT DEPLOYMENT CONSTRAINT:**  
> Never automatically commit, push to GitHub, or trigger production deployment without explicit authorization from the user. All changes must be validated locally using the automated preflight suite before deployment is proposed.

---

## 2. Pre-Deployment Preflight Checklist

Before any commit or push is initiated, the following commands must be executed and confirmed:

1. **Run Automated Production Validation:**
   ```powershell
   python scripts/validate_production.py
   ```
   *Expected Result:* `VALIDATION SUMMARY: 21 PASSED, 0 FAILED`.

2. **Verify Git Working Tree:**
   ```powershell
   git status
   ```
   *Verification:* Ensure only authorized files are modified and untracked generator scripts/logs are ignored by `.vercelignore` or cleanly handled.

3. **Verify Git Remote & Branch:**
   ```powershell
   git remote -v
   git branch --show-current
   ```
   *Verification:* Remote origin must be `https://github.com/gxatechnology/Tanveer-Ashraf.git` and branch must be `main`.

---

## 3. Primary Deployment Workflow: Vercel (CI/CD via GitHub)

The primary production website is hosted on Vercel with automatic continuous deployment enabled on the `main` branch.

### Step 1: Stage Verified Files
Stage all operational HTML pages, assets, and documentation:
```powershell
git add .
```

### Step 2: Create Semantic Release Commit
Commit all Phase 5 changes with a clear release message:
```powershell
git commit -m "feat(v3.0): complete Phase 5 final integration, legal audit & production readiness"
```

### Step 3: Push to Production Branch
Push the staged commit to GitHub:
```powershell
git push origin main
```

### Step 4: Monitor Vercel Deployment
1. Log into the Vercel Dashboard at [https://vercel.com/dashboard](https://vercel.com/dashboard).
2. Locate the project: `gxa-tech/tanveer-ashraf-judicial`.
3. Verify that the build triggered automatically and completed within $\approx 15\text{ seconds}$ (pure static site, zero build command required).
4. Verify the live URL: [https://tanveer-ashraf-judicial.vercel.app](https://tanveer-ashraf-judicial.vercel.app).

---

## 4. Secondary Deployment Workflow: Hostinger Static Web Hosting

For offline backup or static hosting on Hostinger:

1. **Access File Manager:**
   - Log into the Hostinger cPanel / hPanel.
   - Navigate to **File Manager** -> `public_html`.
2. **File Selection:**
   - Upload all 21 root HTML files (`index.html`, `brain-arena.html`, `tests.html`, etc.).
   - Upload the entire `assets/` directory (including `css/`, `data/`, `js/`, `images/`, and `games/`).
   - Upload the `resources/` directory (official bare act PDFs and study materials).
   - Upload `.htaccess` (enforcing `DirectoryIndex index.html` and disabling directory listing).
   - Upload `robots.txt` (enforcing `Disallow: /` to protect private examination prep).
3. **Exclude Non-Production Files:**
   - Do NOT upload `scripts/`, `__pycache__/`, `.git/`, or development log files.

---

## 5. Post-Deployment Verification (Smoke Test)

Immediately after production deployment, execute the following smoke tests on the live URL:

1. **Navigation:** Visit `https://tanveer-ashraf-judicial.vercel.app/` and verify that the hero loads with candidate Tanveer's portrait, Continue Learning card, and Quick Actions.
2. **Brain Arena:** Navigate to `brain-arena.html` and confirm all 8 game cards are visible and clickable.
3. **Mock Exam:** Navigate to `tests.html`, start a 10-question practice test, and confirm timer and question palette function.
4. **Smart Search:** Navigate to `search.html`, search for `"theft"`, and verify that multi-corpus results (BNS sections, PYQs, Vocabulary, and Myths) render correctly.
5. **Revision Centre:** Navigate to `revision.html` and verify filter tabs work.
6. **Data Safety:** Navigate to `results.html`, click **Export Complete Backup**, and verify that the unified `v3.0.0-unified-backup` JSON file downloads.

---

## 6. Rollback Procedures

In the unlikely event of a production regression:

### A. Instant Vercel Rollback:
1. Open project `gxa-tech/tanveer-ashraf-judicial` in Vercel.
2. Navigate to the **Deployments** tab.
3. Select the previous stable deployment (e.g., baseline commit `3a94255`).
4. Click **Instant Rollback**. Traffic will immediately route to the previous deployment.

### B. Git Rollback:
```powershell
git revert HEAD
git push origin main
```
