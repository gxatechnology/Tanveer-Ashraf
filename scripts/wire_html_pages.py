import re

social_scripts_academy = '''
  <!-- Social Legislation (Paper I — 9 Acts) Data -->
  <script src="assets/learning/data/social/social-chapters.js"></script>
  <script src="assets/learning/data/social/social-topics.js"></script>
  <script src="assets/learning/data/social/social-concepts-part1.js"></script>
  <script src="assets/learning/data/social/social-concepts-part2.js"></script>
  <script src="assets/learning/data/social/social-concepts-part3.js"></script>
  <script src="assets/learning/data/social/social-concepts.js"></script>
  <script src="assets/learning/data/social/social-sections-explorer.js"></script>
  <script src="assets/learning/data/social/social-mcqs-part1.js"></script>
  <script src="assets/learning/data/social/social-mcqs-part2.js"></script>
  <script src="assets/learning/data/social/social-mcqs-part3.js"></script>
  <script src="assets/learning/data/social/social-mcqs.js"></script>
  <script src="assets/learning/data/social/social-pyq-mapping.js"></script>
'''

social_scripts_study = social_scripts_academy

social_scripts_practice = '''
  <!-- Social Legislation (Paper I — 9 Acts) Data -->
  <script src="assets/learning/data/social/social-chapters.js"></script>
  <script src="assets/learning/data/social/social-topics.js"></script>
  <script src="assets/learning/data/social/social-mcqs-part1.js"></script>
  <script src="assets/learning/data/social/social-mcqs-part2.js"></script>
  <script src="assets/learning/data/social/social-mcqs-part3.js"></script>
  <script src="assets/learning/data/social/social-mcqs.js"></script>
  <script src="assets/learning/data/social/social-pyq-mapping.js"></script>
'''

social_scripts_progress = social_scripts_practice

# ==============================================================================
# 1. Update learning-academy.html
# ==============================================================================
with open('learning-academy.html', 'r', encoding='utf-8') as f:
    acad = f.read()

# Stats update in hero
acad = re.sub(
    r'<span class="stat-metric-num" id="stat-active-subjects">\d+</span>',
    '<span class="stat-metric-num" id="stat-active-subjects">17</span>',
    acad
)
acad = re.sub(
    r'<span class="stat-metric-num" id="stat-const-topics">\d+</span>',
    '<span class="stat-metric-num" id="stat-const-topics">373</span>',
    acad
)
acad = re.sub(
    r'<span class="stat-metric-num" id="stat-const-mcqs">[\d,]+</span>',
    '<span class="stat-metric-num" id="stat-const-mcqs">3,075</span>',
    acad
)
acad = re.sub(
    r'<span class="stat-metric-num" id="stat-const-pyqs">\d+</span>',
    '<span class="stat-metric-num" id="stat-const-pyqs">615</span>',
    acad
)

# Tab filter buttons update
old_tabs = '''          <div class="tab-filter-group" id="subject-filter-tabs">
            <button class="tab-filter-btn active" data-filter="all">All Subjects (30)</button>
            <button class="tab-filter-btn" data-filter="active">Active (8)</button>
            <button class="tab-filter-btn" data-filter="paper2">Paper II: Law (9)</button>
            <button class="tab-filter-btn" data-filter="paper1">Paper I: GK (12)</button>
            <button class="tab-filter-btn" data-filter="social">Social Laws (9)</button>
          </div>'''

new_tabs = '''          <div class="tab-filter-group" id="subject-filter-tabs">
            <button class="tab-filter-btn active" data-filter="all">All Subjects (30)</button>
            <button class="tab-filter-btn" data-filter="active">Active (17)</button>
            <button class="tab-filter-btn" data-filter="paper2">Paper II: Law (8)</button>
            <button class="tab-filter-btn" data-filter="paper1">Paper I: GK &amp; Social (21)</button>
            <button class="tab-filter-btn" data-filter="social">Social Legislation (9 Active)</button>
          </div>'''

acad = acad.replace(old_tabs, new_tabs, 1)

# Chapter subject pills update
old_pills = '''          <div style="display: flex; gap: 8px; margin-bottom: 20px; flex-wrap: wrap;" id="chapter-subject-pills">
            <button class="tab-filter-btn active" data-subject="law-constitution">🏛️ Constitution (15 Ch)</button>
            <button class="tab-filter-btn" data-subject="law-jurisprudence">⚖️ Jurisprudence (11 Ch)</button>
            <button class="tab-filter-btn" data-subject="law-contract">📜 Contract Law (11 Ch)</button>
            <button class="tab-filter-btn" data-subject="law-tpa">🏡 Property Law (8 Ch)</button>
            <button class="tab-filter-btn" data-subject="law-criminal">⚔️ Criminal Law (12 Ch)</button>
            <button class="tab-filter-btn" data-subject="law-crpc">⚖️ Criminal Procedure (12 Ch)</button>
            <button class="tab-filter-btn" data-subject="law-evidence">🔍 Evidence Law (10 Ch)</button>
            <button class="tab-filter-btn" data-subject="law-cpc">🏛️ Civil Procedure (20 Ch)</button>
          </div>'''

new_pills = '''          <div style="display: flex; gap: 8px; margin-bottom: 12px; flex-wrap: wrap;" id="chapter-subject-pills">
            <span style="font-size: 11.5px; font-weight: bold; text-transform: uppercase; color: #607387; display: flex; align-items: center; width: 100%;">Paper II: Law Subjects (8 Active Modules)</span>
            <button class="tab-filter-btn active" data-subject="law-constitution">🏛️ Constitution (15 Ch)</button>
            <button class="tab-filter-btn" data-subject="law-jurisprudence">⚖️ Jurisprudence (11 Ch)</button>
            <button class="tab-filter-btn" data-subject="law-contract">📜 Contract Law (11 Ch)</button>
            <button class="tab-filter-btn" data-subject="law-tpa">🏡 Property Law (8 Ch)</button>
            <button class="tab-filter-btn" data-subject="law-criminal">⚔️ Criminal Law (12 Ch)</button>
            <button class="tab-filter-btn" data-subject="law-crpc">⚖️ Criminal Procedure (12 Ch)</button>
            <button class="tab-filter-btn" data-subject="law-evidence">🔍 Evidence Law (10 Ch)</button>
            <button class="tab-filter-btn" data-subject="law-cpc">🏛️ Civil Procedure (20 Ch)</button>
          </div>
          <div style="display: flex; gap: 8px; margin-bottom: 20px; flex-wrap: wrap;" id="chapter-social-pills">
            <span style="font-size: 11.5px; font-weight: bold; text-transform: uppercase; color: #137d72; display: flex; align-items: center; width: 100%;">Paper I: Social Legislation (9 Active Modules)</span>
            <button class="tab-filter-btn" data-subject="soc-disabilities">♿ RPwD Act (3 Ch)</button>
            <button class="tab-filter-btn" data-subject="soc-parents">👴 Parents Act (3 Ch)</button>
            <button class="tab-filter-btn" data-subject="soc-dowry">💍 Dowry Act (3 Ch)</button>
            <button class="tab-filter-btn" data-subject="soc-domestic-violence">🛡️ PWDVA (3 Ch)</button>
            <button class="tab-filter-btn" data-subject="soc-posh">🏢 POSH Act (3 Ch)</button>
            <button class="tab-filter-btn" data-subject="soc-pcpndt">🧬 PCPNDT Act (3 Ch)</button>
            <button class="tab-filter-btn" data-subject="soc-mtp">🏥 MTP Act (3 Ch)</button>
            <button class="tab-filter-btn" data-subject="soc-indecent-rep">📵 IRWA (3 Ch)</button>
            <button class="tab-filter-btn" data-subject="soc-pocso">👶 POCSO Act (4 Ch)</button>
          </div>'''

acad = acad.replace(old_pills, new_pills, 1)

# Add Social Legislation Study Centre section right after the 8 Law modules grid
social_centre_html = '''
        <!-- Social Legislation Study Centre (Paper I — 9 Acts) -->
        <div style="margin-bottom: 32px; background: #ffffff; border: 1.5px solid #d4b67e; border-radius: 12px; padding: 24px; box-shadow: 0 4px 14px rgba(20,44,70,0.06);">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px; border-bottom: 1px solid #edf0f4; padding-bottom: 14px;">
            <div>
              <span class="badge badge-paper" style="margin-bottom: 4px; display: inline-block;">Paper I · General Knowledge</span>
              <h2 style="font-family: Georgia, serif; font-size: 22px; color: #142c46; margin: 0;">
                ⚖️ Social Legislation Study Centre (All 9 Acts Active)
              </h2>
              <p style="color: #607387; font-size: 13.5px; margin: 4px 0 0;">
                Statutory features, statutory authorities, penalties, and traps under UP Judicial Services syllabus (Advt A-6/E-1/2026).
              </p>
            </div>
            <div style="display: flex; gap: 10px; align-items: center;">
              <span style="font-size: 12.5px; background: #edf7f4; color: #137d72; padding: 6px 12px; border-radius: 20px; font-weight: 700; border: 1px solid #137d72;">
                ✓ 28 Chapters · 84 Topics · 455 MCQs · 23 PYQs
              </span>
            </div>
          </div>

          <!-- Thematic Group A: Equality, Inclusion & Welfare -->
          <div style="margin-bottom: 20px;">
            <div style="font-family: Georgia, serif; font-size: 15px; font-weight: 700; color: #137d72; margin-bottom: 10px; display: flex; align-items: center; gap: 6px;">
              <span>Group A:</span> Equality, Inclusion &amp; Welfare (2 Acts)
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
              <!-- RPwD -->
              <div style="background: #fdfcf9; border: 1px solid #cdb17d; border-radius: 8px; padding: 16px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <span class="badge badge-status-active" style="margin-bottom: 4px; display: inline-block;">● Active Module</span>
                  <h3 style="font-family: Georgia, serif; font-size: 16px; color: #142c46; margin: 0 0 4px;">♿ Rights of Persons with Disabilities Act, 2016</h3>
                  <p style="color: #607387; font-size: 12px; margin: 0 0 8px;">3 Chapters · 9 Topics · 50 MCQs · 4 PYQs<br><strong>21 Specified Disabilities · 4% Employment · 5% Education</strong></p>
                </div>
                <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-top: 6px;">
                  <a href="subject-study.html?subject=soc-disabilities" class="btn btn-primary btn-sm" style="padding: 4px 10px; font-size: 12px;">📖 Study</a>
                  <a href="topic-practice.html?subject=soc-disabilities&mode=learn" class="btn btn-outline btn-sm" style="padding: 4px 10px; font-size: 12px;">⚡ Practise</a>
                  <a href="subject-progress.html?subject=soc-disabilities" class="btn btn-subtle btn-sm" style="padding: 4px 8px; font-size: 12px;">📊</a>
                </div>
              </div>
              <!-- Parents -->
              <div style="background: #fdfcf9; border: 1px solid #cdb17d; border-radius: 8px; padding: 16px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <span class="badge badge-status-active" style="margin-bottom: 4px; display: inline-block;">● Active Module</span>
                  <h3 style="font-family: Georgia, serif; font-size: 16px; color: #142c46; margin: 0 0 4px;">👴 Maintenance &amp; Welfare of Parents &amp; Senior Citizens Act, 2007</h3>
                  <p style="color: #607387; font-size: 12px; margin: 0 0 8px;">3 Chapters · 9 Topics · 50 MCQs · 1 PYQ<br><strong>Maintenance Tribunal · Max ₹10,000 Cap · Sec 23 Void Transfers</strong></p>
                </div>
                <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-top: 6px;">
                  <a href="subject-study.html?subject=soc-parents" class="btn btn-primary btn-sm" style="padding: 4px 10px; font-size: 12px;">📖 Study</a>
                  <a href="topic-practice.html?subject=soc-parents&mode=learn" class="btn btn-outline btn-sm" style="padding: 4px 10px; font-size: 12px;">⚡ Practise</a>
                  <a href="subject-progress.html?subject=soc-parents" class="btn btn-subtle btn-sm" style="padding: 4px 8px; font-size: 12px;">📊</a>
                </div>
              </div>
            </div>
          </div>

          <!-- Thematic Group B: Protection of Women -->
          <div style="margin-bottom: 20px;">
            <div style="font-family: Georgia, serif; font-size: 15px; font-weight: 700; color: #137d72; margin-bottom: 10px; display: flex; align-items: center; gap: 6px;">
              <span>Group B:</span> Protection of Women (4 Acts)
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">
              <!-- Dowry -->
              <div style="background: #fdfcf9; border: 1px solid #cdb17d; border-radius: 8px; padding: 16px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <span class="badge badge-status-active" style="margin-bottom: 4px; display: inline-block;">● Active Module</span>
                  <h3 style="font-family: Georgia, serif; font-size: 16px; color: #142c46; margin: 0 0 4px;">💍 Dowry Prohibition Act, 1961</h3>
                  <p style="color: #607387; font-size: 12px; margin: 0 0 8px;">3 Chapters · 9 Topics · 50 MCQs · 5 PYQs<br><strong>Sec 3 Penalty · Sec 4 Demand · Sec 6 Stridhan Trust</strong></p>
                </div>
                <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-top: 6px;">
                  <a href="subject-study.html?subject=soc-dowry" class="btn btn-primary btn-sm" style="padding: 4px 10px; font-size: 12px;">📖 Study</a>
                  <a href="topic-practice.html?subject=soc-dowry&mode=learn" class="btn btn-outline btn-sm" style="padding: 4px 10px; font-size: 12px;">⚡ Practise</a>
                  <a href="subject-progress.html?subject=soc-dowry" class="btn btn-subtle btn-sm" style="padding: 4px 8px; font-size: 12px;">📊</a>
                </div>
              </div>
              <!-- DV -->
              <div style="background: #fdfcf9; border: 1px solid #cdb17d; border-radius: 8px; padding: 16px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <span class="badge badge-status-active" style="margin-bottom: 4px; display: inline-block;">● Active Module</span>
                  <h3 style="font-family: Georgia, serif; font-size: 16px; color: #142c46; margin: 0 0 4px;">🛡️ Protection of Women from Domestic Violence Act, 2005</h3>
                  <p style="color: #607387; font-size: 12px; margin: 0 0 8px;">3 Chapters · 9 Topics · 50 MCQs · 2 PYQs<br><strong>Sec 12 Applications · Sec 18-22 Orders · Sec 31 Breach Penalty</strong></p>
                </div>
                <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-top: 6px;">
                  <a href="subject-study.html?subject=soc-domestic-violence" class="btn btn-primary btn-sm" style="padding: 4px 10px; font-size: 12px;">📖 Study</a>
                  <a href="topic-practice.html?subject=soc-domestic-violence&mode=learn" class="btn btn-outline btn-sm" style="padding: 4px 10px; font-size: 12px;">⚡ Practise</a>
                  <a href="subject-progress.html?subject=soc-domestic-violence" class="btn btn-subtle btn-sm" style="padding: 4px 8px; font-size: 12px;">📊</a>
                </div>
              </div>
              <!-- POSH -->
              <div style="background: #fdfcf9; border: 1px solid #cdb17d; border-radius: 8px; padding: 16px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <span class="badge badge-status-active" style="margin-bottom: 4px; display: inline-block;">● Active Module</span>
                  <h3 style="font-family: Georgia, serif; font-size: 16px; color: #142c46; margin: 0 0 4px;">🏢 Sexual Harassment of Women at Workplace (POSH) Act, 2013</h3>
                  <p style="color: #607387; font-size: 12px; margin: 0 0 8px;">3 Chapters · 9 Topics · 50 MCQs · 1 PYQ<br><strong>Internal Committee (10+ workers) · Local Committee · 90-Day Inquiry</strong></p>
                </div>
                <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-top: 6px;">
                  <a href="subject-study.html?subject=soc-posh" class="btn btn-primary btn-sm" style="padding: 4px 10px; font-size: 12px;">📖 Study</a>
                  <a href="topic-practice.html?subject=soc-posh&mode=learn" class="btn btn-outline btn-sm" style="padding: 4px 10px; font-size: 12px;">⚡ Practise</a>
                  <a href="subject-progress.html?subject=soc-posh" class="btn btn-subtle btn-sm" style="padding: 4px 8px; font-size: 12px;">📊</a>
                </div>
              </div>
              <!-- IRWA -->
              <div style="background: #fdfcf9; border: 1px solid #cdb17d; border-radius: 8px; padding: 16px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <span class="badge badge-status-active" style="margin-bottom: 4px; display: inline-block;">● Active Module</span>
                  <h3 style="font-family: Georgia, serif; font-size: 16px; color: #142c46; margin: 0 0 4px;">📵 Indecent Representation of Women (Prohibition) Act, 1986</h3>
                  <p style="color: #607387; font-size: 12px; margin: 0 0 8px;">3 Chapters · 9 Topics · 45 MCQs · 3 PYQs<br><strong>Sec 3 Ad Prohibitions · Sec 4 Distribution · Gazetted Officer Search</strong></p>
                </div>
                <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-top: 6px;">
                  <a href="subject-study.html?subject=soc-indecent-rep" class="btn btn-primary btn-sm" style="padding: 4px 10px; font-size: 12px;">📖 Study</a>
                  <a href="topic-practice.html?subject=soc-indecent-rep&mode=learn" class="btn btn-outline btn-sm" style="padding: 4px 10px; font-size: 12px;">⚡ Practise</a>
                  <a href="subject-progress.html?subject=soc-indecent-rep" class="btn btn-subtle btn-sm" style="padding: 4px 8px; font-size: 12px;">📊</a>
                </div>
              </div>
            </div>
          </div>

          <!-- Thematic Group C: Reproductive Health & Child Protection -->
          <div>
            <div style="font-family: Georgia, serif; font-size: 15px; font-weight: 700; color: #137d72; margin-bottom: 10px; display: flex; align-items: center; gap: 6px;">
              <span>Group C:</span> Reproductive Health &amp; Child Protection (3 Acts)
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
              <!-- PCPNDT -->
              <div style="background: #fdfcf9; border: 1px solid #cdb17d; border-radius: 8px; padding: 16px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <span class="badge badge-status-active" style="margin-bottom: 4px; display: inline-block;">● Active Module</span>
                  <h3 style="font-family: Georgia, serif; font-size: 16px; color: #142c46; margin: 0 0 4px;">🧬 PCPNDT Act, 1994</h3>
                  <p style="color: #607387; font-size: 12px; margin: 0 0 8px;">3 Chapters · 9 Topics · 50 MCQs · 2 PYQs<br><strong>Sex Selection Ban · Appropriate Authority · Cognizance Rules</strong></p>
                </div>
                <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-top: 6px;">
                  <a href="subject-study.html?subject=soc-pcpndt" class="btn btn-primary btn-sm" style="padding: 4px 10px; font-size: 12px;">📖 Study</a>
                  <a href="topic-practice.html?subject=soc-pcpndt&mode=learn" class="btn btn-outline btn-sm" style="padding: 4px 10px; font-size: 12px;">⚡ Practise</a>
                  <a href="subject-progress.html?subject=soc-pcpndt" class="btn btn-subtle btn-sm" style="padding: 4px 8px; font-size: 12px;">📊</a>
                </div>
              </div>
              <!-- MTP -->
              <div style="background: #fdfcf9; border: 1px solid #cdb17d; border-radius: 8px; padding: 16px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <span class="badge badge-status-active" style="margin-bottom: 4px; display: inline-block;">● Active Module</span>
                  <h3 style="font-family: Georgia, serif; font-size: 16px; color: #142c46; margin: 0 0 4px;">🏥 Medical Termination of Pregnancy (MTP) Act, 1971</h3>
                  <p style="color: #607387; font-size: 12px; margin: 0 0 8px;">3 Chapters · 9 Topics · 50 MCQs · 3 PYQs<br><strong>2021 Amendments · Up to 20 wks (1 RMP) · 20-24 wks (2 RMPs) · Medical Board</strong></p>
                </div>
                <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-top: 6px;">
                  <a href="subject-study.html?subject=soc-mtp" class="btn btn-primary btn-sm" style="padding: 4px 10px; font-size: 12px;">📖 Study</a>
                  <a href="topic-practice.html?subject=soc-mtp&mode=learn" class="btn btn-outline btn-sm" style="padding: 4px 10px; font-size: 12px;">⚡ Practise</a>
                  <a href="subject-progress.html?subject=soc-mtp" class="btn btn-subtle btn-sm" style="padding: 4px 8px; font-size: 12px;">📊</a>
                </div>
              </div>
              <!-- POCSO -->
              <div style="background: #fdfcf9; border: 1px solid #cdb17d; border-radius: 8px; padding: 16px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <span class="badge badge-status-active" style="margin-bottom: 4px; display: inline-block;">● Active Module</span>
                  <h3 style="font-family: Georgia, serif; font-size: 16px; color: #142c46; margin: 0 0 4px;">👶 Protection of Children from Sexual Offences (POCSO) Act, 2012</h3>
                  <p style="color: #607387; font-size: 12px; margin: 0 0 8px;">4 Chapters · 12 Topics · 60 MCQs · 2 PYQs<br><strong>Child defined (&lt;18) · Special Courts · Presumption of Guilt (Sec 29/30)</strong></p>
                </div>
                <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-top: 6px;">
                  <a href="subject-study.html?subject=soc-pocso" class="btn btn-primary btn-sm" style="padding: 4px 10px; font-size: 12px;">📖 Study</a>
                  <a href="topic-practice.html?subject=soc-pocso&mode=learn" class="btn btn-outline btn-sm" style="padding: 4px 10px; font-size: 12px;">⚡ Practise</a>
                  <a href="subject-progress.html?subject=soc-pocso" class="btn btn-subtle btn-sm" style="padding: 4px 8px; font-size: 12px;">📊</a>
                </div>
              </div>
            </div>
          </div>
        </div>
'''

# Find the end of the 8 Law modules and insert Social Centre
cpc_div_marker = '''            <!-- Module 8: Code of Civil Procedure (Phase 4) -->
            <div style="background: #edf7f4; border: 1.5px solid #137d72; border-radius: 8px; padding: 18px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <span class="badge badge-status-active" style="margin-bottom: 6px; display: inline-block;">● Active Module (Full Code)</span>
                <h3 style="font-family: Georgia, serif; font-size: 17px; color: #142c46; margin: 0 0 4px;">🏛️ Code of Civil Procedure, 1908</h3>
                <p style="color: #607387; font-size: 12px; margin: 0 0 10px;">20 Chapters · 57 Topics · 400 MCQs · 60 PYQs<br><strong>Sections 1–158 · Orders I–LI · UP State Amendments</strong></p>
              </div>
              <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: 8px;">
                <a href="subject-study.html?subject=law-cpc" class="btn btn-primary btn-sm">📖 Study</a>
                <a href="topic-practice.html?subject=law-cpc&mode=learn" class="btn btn-outline btn-sm">⚡ Practise</a>
                <a href="civil-suit-journey.html" class="btn btn-gold btn-sm" style="text-decoration:none;">⚖️ Journey</a>
                <a href="subject-progress.html?subject=law-cpc" class="btn btn-subtle btn-sm">📊 Stats</a>
              </div>
            </div>
          </div>
        </div>'''

acad = acad.replace(cpc_div_marker, cpc_div_marker + social_centre_html, 1)

# Add scripts in learning-academy.html
cpc_pyq_script = '  <script src="assets/learning/data/cpc/cpc-pyq-mapping.js"></script>'
acad = acad.replace(cpc_pyq_script, cpc_pyq_script + social_scripts_academy, 1)

# In script block, also wire chapter-social-pills
acad = acad.replace(
    'const chapterPills = document.querySelectorAll(\'#chapter-subject-pills .tab-filter-btn\');',
    'const chapterPills = document.querySelectorAll(\'#chapter-subject-pills .tab-filter-btn, #chapter-social-pills .tab-filter-btn\');'
)

with open('learning-academy.html', 'w', encoding='utf-8') as f:
    f.write(acad)
print('Updated learning-academy.html successfully!')

# ==============================================================================
# 2. Update subject-study.html
# ==============================================================================
with open('subject-study.html', 'r', encoding='utf-8') as f:
    study = f.read()

study = study.replace(cpc_pyq_script, cpc_pyq_script + social_scripts_study, 1)

with open('subject-study.html', 'w', encoding='utf-8') as f:
    f.write(study)
print('Updated subject-study.html successfully!')

# ==============================================================================
# 3. Update topic-practice.html
# ==============================================================================
with open('topic-practice.html', 'r', encoding='utf-8') as f:
    prac = f.read()

prac = prac.replace(cpc_pyq_script, cpc_pyq_script + social_scripts_practice, 1)

with open('topic-practice.html', 'w', encoding='utf-8') as f:
    f.write(prac)
print('Updated topic-practice.html successfully!')

# ==============================================================================
# 4. Update subject-progress.html
# ==============================================================================
with open('subject-progress.html', 'r', encoding='utf-8') as f:
    prog = f.read()

prog = prog.replace(cpc_pyq_script, cpc_pyq_script + social_scripts_progress, 1)

old_prog_pills = '''          <a href="subject-progress.html?subject=law-evidence" class="tab-filter-btn" id="pill-law-evidence">🔍 Law of Evidence</a>
          <a href="subject-progress.html?subject=law-cpc" class="tab-filter-btn" id="pill-law-cpc">🏛️ Civil Procedure</a>
        </div>'''

new_prog_pills = '''          <a href="subject-progress.html?subject=law-evidence" class="tab-filter-btn" id="pill-law-evidence">🔍 Law of Evidence</a>
          <a href="subject-progress.html?subject=law-cpc" class="tab-filter-btn" id="pill-law-cpc">🏛️ Civil Procedure</a>
          <a href="subject-progress.html?subject=soc-disabilities" class="tab-filter-btn" id="pill-soc-disabilities">♿ RPwD Act</a>
          <a href="subject-progress.html?subject=soc-parents" class="tab-filter-btn" id="pill-soc-parents">👴 Parents Act</a>
          <a href="subject-progress.html?subject=soc-dowry" class="tab-filter-btn" id="pill-soc-dowry">💍 Dowry Act</a>
          <a href="subject-progress.html?subject=soc-domestic-violence" class="tab-filter-btn" id="pill-soc-domestic-violence">🛡️ PWDVA</a>
          <a href="subject-progress.html?subject=soc-posh" class="tab-filter-btn" id="pill-soc-posh">🏢 POSH Act</a>
          <a href="subject-progress.html?subject=soc-pcpndt" class="tab-filter-btn" id="pill-soc-pcpndt">🧬 PCPNDT</a>
          <a href="subject-progress.html?subject=soc-mtp" class="tab-filter-btn" id="pill-soc-mtp">🏥 MTP Act</a>
          <a href="subject-progress.html?subject=soc-indecent-rep" class="tab-filter-btn" id="pill-soc-indecent-rep">📵 IRWA</a>
          <a href="subject-progress.html?subject=soc-pocso" class="tab-filter-btn" id="pill-soc-pocso">👶 POCSO Act</a>
        </div>'''

prog = prog.replace(old_prog_pills, new_prog_pills, 1)

with open('subject-progress.html', 'w', encoding='utf-8') as f:
    f.write(prog)
print('Updated subject-progress.html successfully!')

# ==============================================================================
# 5. Update search.html
# ==============================================================================
with open('search.html', 'r', encoding='utf-8') as f:
    search_html = f.read()

cpc_search_marker = '<script src="assets/learning/data/cpc/cpc-mcqs.js"></script>'
soc_search_scripts = cpc_search_marker + '<script src="assets/learning/data/social/social-topics.js"></script><script src="assets/learning/data/social/social-mcqs.js"></script>'
search_html = search_html.replace(cpc_search_marker, soc_search_scripts, 1)

with open('search.html', 'w', encoding='utf-8') as f:
    f.write(search_html)
print('Updated search.html successfully!')
