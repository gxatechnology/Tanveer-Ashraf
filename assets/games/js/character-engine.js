/**
 * LEGAL BRAIN ARENA — CHARACTER ENGINE (V3.0 Phase 2)
 * Character rendering, dialogue typewriter animation, and procedural TTS integration.
 * Author: Tauqeer Ashraf
 */
(function() {
  'use strict';

  let currentTypewriterTimer = null;
  let currentSkipCallback = null;
  let isSpeaking = false;

  const CharacterEngine = {
    getCharacter: function(id) {
      if (!window.ARENA_CHARACTERS) return null;
      return window.ARENA_CHARACTERS[id] || null;
    },

    renderAvatar: function(characterId, size = 'md') {
      const char = this.getCharacter(characterId);
      if (!char) {
        return `<div class="character-avatar-wrap size-${size}"><span style="color:#dfbf80">⚖</span></div>`;
      }
      return `
        <div class="character-card size-${size}" data-character-id="${char.id}">
          <div class="character-avatar-wrap size-${size}" style="border-color:${char.themeColor}">
            <img src="${char.portrait}" alt="${char.name} portrait" loading="lazy">
          </div>
          <div class="character-name">${char.name}</div>
          <div class="character-role" style="color:${char.themeColor}">${char.role}</div>
        </div>
      `;
    },

    typewrite: function(containerEl, text, onComplete, speed = 20) {
      this.cancelTypewrite();

      if (!containerEl) {
        if (typeof onComplete === 'function') onComplete();
        return;
      }

      containerEl.innerHTML = '<span class="dialogue-speech-text"></span><span class="dialogue-typewriter-cursor"></span>';
      const textSpan = containerEl.querySelector('.dialogue-speech-text');
      const cursorSpan = containerEl.querySelector('.dialogue-typewriter-cursor');

      let index = 0;
      let completed = false;

      const finishImmediately = () => {
        if (completed) return;
        completed = true;
        if (currentTypewriterTimer) clearInterval(currentTypewriterTimer);
        currentTypewriterTimer = null;
        currentSkipCallback = null;
        textSpan.textContent = text;
        if (cursorSpan) cursorSpan.style.display = 'none';
        if (typeof onComplete === 'function') onComplete();
      };

      currentSkipCallback = finishImmediately;

      currentTypewriterTimer = setInterval(() => {
        if (index < text.length) {
          textSpan.textContent += text.charAt(index);
          index++;
          // Occasional typewriter sound
          if (index % 4 === 0 && window.GameAudio) {
            window.GameAudio.playTypewriter();
          }
        } else {
          finishImmediately();
        }
      }, speed);
    },

    skipTypewrite: function() {
      if (typeof currentSkipCallback === 'function') {
        currentSkipCallback();
      }
    },

    cancelTypewrite: function() {
      if (currentTypewriterTimer) {
        clearInterval(currentTypewriterTimer);
        currentTypewriterTimer = null;
      }
      currentSkipCallback = null;
      this.stopSpeech();
    },

    speak: function(characterId, text) {
      // Check if sound is muted
      if (!window.GameAudio || window.GameAudio.isMuted()) return;
      if (!('speechSynthesis' in window)) return;

      this.stopSpeech();

      const char = this.getCharacter(characterId);
      const utterance = new SpeechSynthesisUtterance(text);
      if (char) {
        utterance.pitch = char.voicePitch || 1.0;
        utterance.rate = char.voiceRate || 1.0;
      }

      utterance.onend = () => { isSpeaking = false; };
      utterance.onerror = () => { isSpeaking = false; };

      isSpeaking = true;
      try {
        window.speechSynthesis.speak(utterance);
      } catch (e) {
        isSpeaking = false;
      }
    },

    stopSpeech: function() {
      if ('speechSynthesis' in window && isSpeaking) {
        try {
          window.speechSynthesis.cancel();
        } catch (e) {}
        isSpeaking = false;
      }
    }
  };

  window.CharacterEngine = CharacterEngine;
})();
