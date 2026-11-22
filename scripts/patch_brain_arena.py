# Update brain-arena.html for Phase 4: All 8 Games Live
import os

arena_path = "brain-arena.html"
with open(arena_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update Phase banner
old_phase = '<span class="caption muted">Phase 3: 6 Live Games · 2 In Development</span>'
new_phase = '<span class="caption gold" style="font-weight:700;">Phase 4: All 8 Games Live & Playable</span>'

if old_phase in text:
    text = text.replace(old_phase, new_phase)

# 2. Update Game 7 & 8 cards
old_cards = """            <!-- 7. Legal Myth Buster (UPCOMING) -->
            <article class="game-card upcoming">
              <div class="game-card-media">
                <img src="assets/games/images/cards/myth-buster.svg" alt="Legal Myth Buster artwork">
                <span class="game-status-badge soon">UPCOMING</span>
              </div>
              <div class="game-card-body">
                <h3>Legal Myth Buster</h3>
                <p class="game-card-desc">Dismantle pervasive statutory misconceptions, misleading legal myths, and tricky prelims multiple-choice traps.</p>
                <div class="game-card-meta">
                  <span>Critical Precision</span>
                  <span class="caption muted">In Development</span>
                </div>
                <div class="game-card-action">
                  <button class="btn mini" disabled>Coming Soon</button>
                </div>
              </div>
            </article>

            <!-- 8. Road to Judiciary (UPCOMING) -->
            <article class="game-card upcoming">
              <div class="game-card-media">
                <img src="assets/games/images/cards/road-to-judiciary.svg" alt="Road to Judiciary artwork">
                <span class="game-status-badge soon">UPCOMING</span>
              </div>
              <div class="game-card-body">
                <h3>Road to Judiciary</h3>
                <p class="game-card-desc">An epic multi-tier judicial career campaign simulating the preparation journey from civil advocate to High Court bench.</p>
                <div class="game-card-meta">
                  <span>Career Campaign</span>
                  <span class="caption muted">In Development</span>
                </div>
                <div class="game-card-action">
                  <button class="btn mini" disabled>Coming Soon</button>
                </div>
              </div>
            </article>"""

new_cards = """            <!-- 7. Legal Myth Buster (PLAYABLE) -->
            <article class="game-card">
              <div class="game-card-media">
                <img src="assets/games/images/cards/myth-buster.svg" alt="Legal Myth Buster artwork">
                <span class="game-status-badge live">● PLAYABLE</span>
              </div>
              <div class="game-card-body">
                <h3>Legal Myth Buster</h3>
                <p class="game-card-desc">Question everything. Discover the law. Evaluate 330 verified statutory propositions across 8 playable modes with animated scales of truth.</p>
                <div class="game-card-meta">
                  <span>Chamber of Truth</span>
                  <span class="caption gold">8 Playable Modes</span>
                </div>
                <div class="game-card-action">
                  <a href="myth-buster.html" class="btn primary">Enter Chamber ↗</a>
                </div>
              </div>
            </article>

            <!-- 8. Road to Judiciary (PLAYABLE) -->
            <article class="game-card">
              <div class="game-card-media">
                <img src="assets/games/images/cards/road-to-judiciary.svg" alt="Road to Judiciary artwork">
                <span class="game-status-badge live">● PLAYABLE</span>
              </div>
              <div class="game-card-body">
                <h3>Road to Judiciary</h3>
                <p class="game-card-desc">Every challenge brings you closer to the bench. 9 progressive campaign chapters, 36 connected missions, daily study plan, and judicial appointment decree.</p>
                <div class="game-card-meta">
                  <span>Judicial Campaign</span>
                  <span class="caption gold">9 Chapters • 36 Missions</span>
                </div>
                <div class="game-card-action">
                  <a href="judiciary-journey.html" class="btn primary">Ascend to Bench ↗</a>
                </div>
              </div>
            </article>"""

if old_cards in text:
    text = text.replace(old_cards, new_cards)
else:
    print("WARNING: Could not find exact old_cards block")

# 3. Add link to achievements.html in Achievements section header
old_ach_header = '<h3>Judicial Honors</h3>'
new_ach_header = '<h3>Judicial Honors</h3>\n              <a href="achievements.html" class="btn mini gold" style="margin-left:auto; text-decoration:none;">Full Hall of Honors (38) ↗</a>'

if old_ach_header in text and 'Full Hall of Honors' not in text:
    text = text.replace(old_ach_header, new_ach_header, 1)

with open(arena_path, "w", encoding="utf-8") as f:
    f.write(text)

print("brain-arena.html updated for Phase 4 successfully!")
