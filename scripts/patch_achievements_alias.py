# Add alias window.Achievements = AchievementsEngine
with open("assets/games/js/achievements.js", "r", encoding="utf-8") as f:
    text = f.read()

if "window.AchievementsEngine = AchievementsEngine;" in text and "window.Achievements = AchievementsEngine;" not in text:
    text = text.replace("window.AchievementsEngine = AchievementsEngine;", "window.AchievementsEngine = AchievementsEngine;\n  window.Achievements = AchievementsEngine;")
    with open("assets/games/js/achievements.js", "w", encoding="utf-8") as f:
        f.write(text)
    print("Added window.Achievements alias successfully!")
