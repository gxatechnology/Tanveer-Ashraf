# Patch game-audio.js to add generic play() method
with open("assets/games/js/game-audio.js", "r", encoding="utf-8") as f:
    text = f.read()

play_method = """    // Generic play method supporting sound categories
    play: function(type) {
      if (isMuted) return;
      if (type === 'success' || type === 'correct') {
        this.playMatch();
      } else if (type === 'error' || type === 'mismatch') {
        this.playMismatch();
      } else if (type === 'streak') {
        this.playStreak();
      } else if (type === 'victory') {
        this.playVictory();
      } else if (type === 'achievement') {
        this.playAchievement();
      } else if (type === 'gavel') {
        this.playGavel();
      } else {
        this.playTick();
      }
    },
"""

marker = "window.GameAudio = {\n"
if marker in text and "play: function(type)" not in text:
    text = text.replace(marker, marker + play_method)
    with open("assets/games/js/game-audio.js", "w", encoding="utf-8") as f:
        f.write(text)
    print("Added generic play() to GameAudio successfully!")
else:
    print("Marker not found or already added")
