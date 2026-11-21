JUDICIAL PREP — HOSTINGER READY
Created for Tanveer Ashraf | Developed by Tauqeer Ashraf

1. In Hostinger hPanel open Websites > Manage/Dashboard > File Manager.
2. Open public_html for your chosen domain (or create a dedicated subfolder). Back up existing website files first.
3. Upload the ZIP and extract its contents into that folder. index.html and assets/ must be siblings directly inside the folder.
4. Open the domain or subfolder using HTTPS. All eleven HTML pages and their local assets work without Node, PHP, API keys or a database.
5. If your hosting configuration rejects .htaccess Options, remove that line or the .htaccess file.

Data: 1,800 slots, 1,799 available PYQs and 1,757 eligible for scoring. Historical keys and OCR text are not universally certified; unresolved items are excluded from scoring. Topic tags are suggested.
Progress: browser localStorage, shared by pages on the same origin. Export/import from Results. Existing version uses the same storage key. No server login, private access control or cross-device sync. For a personal portal, enable hosting password protection on the folder if available, especially before publishing personal portraits. robots.txt and noindex are not access controls.
No official logo or affiliation. Decorative original scales/courthouse icon.

V2 — BNS & SMART SEARCH
Added bns.html, search.html, assets/data/bns.js, and assets/js/legal-search.js.
BNS: all 358 section titles across 20 chapters, searchable offline; read full statutory provisions online through official India Code PDF and independent section reader links. Section-title recall practice is newly authored from headings, separate from PYQs. Not a complete offline statutory text; amendment and commencement notices should be checked.
Smart Search: partial English words, multiple words, numbers, common statute abbreviations and spelling variants. Old PYQ data and scoring are unchanged. No fabricated BNS PYQs. BNS bookmarks are stored separately in this browser.
Upgrade existing deployment: back up your edited local project first, then merge these files into the existing folder (do not remove .git or .vercel). Preserve any custom changes you made since the original package. From the existing local project run git status, git add ., git commit -m "Add BNS library and smart legal search", git push origin main. Vercel should deploy automatically if the existing Git integration is active.
Testing: all 358 numbered entries and chapter assignments, search logic for exact section numbers / partial terms / PYQ terms, unchanged question bank counts, and JS syntax checked. Browser navigation in the test environment was blocked; live end-to-end testing remains to be done.
