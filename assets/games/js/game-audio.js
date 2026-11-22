/**
 * LEGAL BRAIN ARENA — PROCEDURAL WEB AUDIO SYNTHESIZER
 * Zero external audio files; 100% offline, lightweight and responsive.
 * Muted by default per judicial focus requirements.
 */
(function() {
  'use strict';

  let ctx = null;
  let isMuted = true;

  function initAudio() {
    if (!ctx && (window.AudioContext || window.webkitAudioContext)) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      ctx = new AudioCtx();
    }
    if (ctx && ctx.state === 'suspended') {
      ctx.resume();
    }
  }

  function setMuted(muted) {
    isMuted = !!muted;
    try {
      const state = window.GameStorage ? window.GameStorage.getArenaState() : null;
      if (state && state.settings) {
        state.settings.sound = !isMuted;
        window.GameStorage.saveArenaState(state);
      }
    } catch (e) {}
  }

  function isSoundEnabled() {
    return !isMuted;
  }

  // Soft tone generator helper
  function playTone(freq, type, duration, gainLevel = 0.15, decay = true) {
    if (isMuted || !ctx) return;
    try {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = type;
      osc.frequency.setValueAtTime(freq, ctx.currentTime);

      gain.gain.setValueAtTime(gainLevel, ctx.currentTime);
      if (decay) {
        gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + duration);
      }

      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + duration);
    } catch (e) {}
  }

  const GameAudio = {
    init: function() {
      // Check stored preference
      try {
        const state = window.GameStorage ? window.GameStorage.getArenaState() : null;
        if (state && state.settings && typeof state.settings.sound === 'boolean') {
          isMuted = !state.settings.sound; // Muted by default if false
        }
      } catch (e) {}
    },

    toggleMute: function() {
      initAudio();
      setMuted(!isMuted);
      if (!isMuted) {
        // Play brief soft confirmation chirp
        playTone(587.33, 'sine', 0.12, 0.1);
      }
      return !isMuted;
    },

    isMuted: function() {
      return isMuted;
    },

    // Subtle card flip sound
    playCardFlip: function() {
      if (isMuted) return;
      initAudio();
      if (!ctx) return;
      try {
        // Filtered short white noise puff
        const bufferSize = ctx.sampleRate * 0.04;
        const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
          data[i] = (Math.random() * 2 - 1) * Math.exp(-i / (bufferSize * 0.3));
        }
        const noise = ctx.createBufferSource();
        noise.buffer = buffer;
        const filter = ctx.createBiquadFilter();
        filter.type = 'lowpass';
        filter.frequency.setValueAtTime(800, ctx.currentTime);
        filter.frequency.exponentialRampToValueAtTime(200, ctx.currentTime + 0.04);
        const gain = ctx.createGain();
        gain.gain.setValueAtTime(0.08, ctx.currentTime);
        noise.connect(filter);
        filter.connect(gain);
        gain.connect(ctx.destination);
        noise.start();
      } catch (e) {}
    },

    // Harmonious judicial bell/chime for correct match
    playMatch: function() {
      if (isMuted) return;
      initAudio();
      if (!ctx) return;
      // Dual bell: C5 (523.25Hz) + E5 (659.25Hz) -> G5 (783.99Hz)
      playTone(523.25, 'triangle', 0.25, 0.12);
      setTimeout(() => playTone(659.25, 'triangle', 0.3, 0.12), 60);
      setTimeout(() => playTone(783.99, 'sine', 0.4, 0.15), 130);
    },

    // Soft low chime for incorrect response
    playMismatch: function() {
      if (isMuted) return;
      initAudio();
      playTone(196.00, 'sine', 0.18, 0.1); // G3
      setTimeout(() => playTone(164.81, 'triangle', 0.22, 0.08), 80); // E3
    },

    // Short wooden click for clock / sprint countdown
    playTick: function() {
      if (isMuted) return;
      initAudio();
      playTone(880, 'sine', 0.03, 0.06);
    },

    // Upbeat streak chime
    playStreak: function(streakLevel) {
      if (isMuted) return;
      initAudio();
      const base = 440 + Math.min(streakLevel * 40, 400);
      playTone(base, 'triangle', 0.15, 0.12);
      setTimeout(() => playTone(base * 1.25, 'triangle', 0.2, 0.12), 50);
    },

    // Triumphant judicial fanfare for game victory
    playVictory: function() {
      if (isMuted) return;
      initAudio();
      const notes = [440, 554.37, 659.25, 880]; // A major arpeggio
      notes.forEach((freq, idx) => {
        setTimeout(() => playTone(freq, 'triangle', 0.45, 0.14), idx * 110);
      });
    },

    // Royal herald for achievement unlock
    playAchievement: function() {
      if (isMuted) return;
      initAudio();
      const notes = [523.25, 659.25, 783.99, 1046.50]; // C major fanfare
      notes.forEach((freq, idx) => {
        setTimeout(() => playTone(freq, 'sine', 0.5, 0.15), idx * 100);
      });
    },

    // Resonant judicial gavel strike (double wooden knock with low resonance)
    playGavel: function() {
      if (isMuted) return;
      initAudio();
      if (!ctx) return;
      try {
        // Strike 1
        playTone(180, 'triangle', 0.12, 0.2);
        playTone(90, 'sine', 0.2, 0.25);
        // Strike 2 slightly delayed
        setTimeout(() => {
          playTone(160, 'triangle', 0.15, 0.22);
          playTone(80, 'sine', 0.25, 0.3);
        }, 140);
      } catch (e) {}
    },

    // Soft dossier / legal brief paper rustle
    playPaper: function() {
      if (isMuted) return;
      initAudio();
      if (!ctx) return;
      try {
        const bufferSize = ctx.sampleRate * 0.08;
        const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
          data[i] = (Math.random() * 2 - 1) * Math.exp(-i / (bufferSize * 0.4));
        }
        const noise = ctx.createBufferSource();
        noise.buffer = buffer;
        const filter = ctx.createBiquadFilter();
        filter.type = 'bandpass';
        filter.frequency.setValueAtTime(1400, ctx.currentTime);
        const gain = ctx.createGain();
        gain.gain.setValueAtTime(0.06, ctx.currentTime);
        noise.connect(filter);
        filter.connect(gain);
        gain.connect(ctx.destination);
        noise.start();
      } catch (e) {}
    },

    // Bright clue connection ping
    playClue: function() {
      if (isMuted) return;
      initAudio();
      playTone(659.25, 'sine', 0.18, 0.12); // E5
      setTimeout(() => playTone(987.77, 'sine', 0.25, 0.14), 70); // B5
    },

    // Subtle typewriter click for dialogue
    playTypewriter: function() {
      if (isMuted) return;
      initAudio();
      playTone(700 + Math.random() * 200, 'sine', 0.015, 0.02);
    },

    // === PHASE 3 COGNITIVE PUZZLE AUDIO EFFECTS ===
    // Crisp metallic letter tile selection click
    playTileClick: function() {
      if (isMuted) return;
      initAudio();
      playTone(1100 + Math.random() * 150, 'triangle', 0.03, 0.08);
    },

    // Tile snapping into answer slot
    playTileSnap: function() {
      if (isMuted) return;
      initAudio();
      playTone(880, 'sine', 0.04, 0.1);
      setTimeout(() => playTone(1320, 'sine', 0.08, 0.12), 35);
    },

    // Tile shuffling cascade
    playTileShuffle: function() {
      if (isMuted) return;
      initAudio();
      for (let i = 0; i < 4; i++) {
        setTimeout(() => playTone(600 + Math.random() * 400, 'triangle', 0.025, 0.04), i * 35);
      }
    },

    // Subtle cell movement tick in crossword grid
    playCrosswordTick: function() {
      if (isMuted) return;
      initAudio();
      playTone(520, 'sine', 0.02, 0.03);
    },

    // Harmonious chord when a crossword word or scrambled word is solved
    playWordSolve: function() {
      if (isMuted) return;
      initAudio();
      playTone(659.25, 'sine', 0.15, 0.12); // E5
      setTimeout(() => playTone(830.61, 'sine', 0.18, 0.14), 70); // G#5
      setTimeout(() => playTone(987.77, 'sine', 0.28, 0.16), 140); // B5
    },

    // Generic play method supporting sound categories
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

    // Mystical resonant chime when unlocking a manuscript chapter
    playManuscriptReveal: function() {
      if (isMuted) return;
      initAudio();
      const notes = [523.25, 659.25, 783.99, 1046.50];
      notes.forEach((freq, idx) => {
        setTimeout(() => playTone(freq, 'sine', 0.35, 0.12), idx * 100);
      });
    }
  };

  window.GameAudio = GameAudio;
  // Initialize on load
  document.addEventListener('DOMContentLoaded', GameAudio.init);
})();
