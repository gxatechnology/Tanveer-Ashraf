/**
 * LEGAL VOCABULARY ENGINE (V3.0 Phase 3)
 * Shared utilities for answer normalization, letter scrambling, multiset validation,
 * deterministic daily challenges, and spaced repetition scheduling.
 */
(function() {
  'use strict';

  const VocabularyEngine = {
    /**
     * Normalizes an answer string (uppercase, trims, removes punctuation, optional keep spaces)
     */
    normalize(str, keepSpaces = false) {
      if (!str) return '';
      let s = String(str).toUpperCase().trim();
      if (keepSpaces) {
        return s.replace(/[^A-Z0-9\s]/g, '').replace(/\s+/g, ' ');
      }
      return s.replace(/[^A-Z0-9]/g, '');
    },

    /**
     * Counts occurrences of each character in a string
     */
    getCharFrequency(str) {
      const clean = this.normalize(str, false);
      const freq = {};
      for (let i = 0; i < clean.length; i++) {
        const ch = clean[i];
        freq[ch] = (freq[ch] || 0) + 1;
      }
      return freq;
    },

    /**
     * Verifies that two words share the exact same letter multiset
     */
    verifyLetterMultiset(original, candidate) {
      const freqA = this.getCharFrequency(original);
      const freqB = this.getCharFrequency(candidate);
      
      const keysA = Object.keys(freqA);
      const keysB = Object.keys(freqB);
      if (keysA.length !== keysB.length) return false;
      
      for (let k of keysA) {
        if (freqA[k] !== freqB[k]) return false;
      }
      return true;
    },

    /**
     * Shuffles an array in place using standard Fisher-Yates algorithm
     */
    fisherYates(arr) {
      const a = [...arr];
      for (let i = a.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        const temp = a[i];
        a[i] = a[j];
        a[j] = temp;
      }
      return a;
    },

    /**
     * Scrambles a legal word or multi-word phrase while preserving word boundaries.
     * Guaranteed not to return the solved word if length >= 4 (unless impossible).
     */
    scramble(wordOrPhrase) {
      if (!wordOrPhrase) return '';
      const raw = String(wordOrPhrase).trim();
      const parts = raw.split(/\s+/);
      
      const scrambledParts = parts.map(part => {
        const clean = part.toUpperCase().replace(/[^A-Z]/g, '');
        if (clean.length <= 2) return clean;
        
        const letters = clean.split('');
        let shuffled = clean;
        let attempts = 0;
        
        while (attempts < 15) {
          const cand = this.fisherYates(letters).join('');
          if (cand !== clean) {
            shuffled = cand;
            break;
          }
          attempts++;
        }
        return shuffled;
      });

      return scrambledParts.join(' ');
    },

    /**
     * Creates individual tile objects with unique IDs for UI drag-and-drop / click
     */
    createLetterTiles(wordOrPhrase) {
      const scrambled = this.scramble(wordOrPhrase);
      const tiles = [];
      let tileIndex = 0;
      
      for (let i = 0; i < scrambled.length; i++) {
        const ch = scrambled[i];
        if (ch === ' ') {
          tiles.push({ id: `space-${i}`, char: ' ', isSpace: true, isPlaced: false });
        } else {
          tiles.push({
            id: `tile-${tileIndex++}-${ch}`,
            char: ch,
            isSpace: false,
            isPlaced: false,
            slotIndex: -1
          });
        }
      }
      return { scrambledStr: scrambled, tiles };
    },

    /**
     * Generates a stable deterministic integer seed from a date string (YYYY-MM-DD)
     */
    getDateHash(dateStr) {
      const s = dateStr || new Date().toISOString().slice(0, 10);
      let hash = 0;
      for (let i = 0; i < s.length; i++) {
        hash = (hash << 5) - hash + s.charCodeAt(i);
        hash |= 0;
      }
      return Math.abs(hash);
    },

    /**
     * Selects deterministic Daily Crossword
     */
    getDailyCrossword(puzzles, dateStr) {
      if (!Array.isArray(puzzles) || puzzles.length === 0) return null;
      const hash = this.getDateHash(dateStr);
      const index = hash % puzzles.length;
      return puzzles[index];
    },

    /**
     * Selects deterministic Daily Word Challenge
     */
    getDailyWord(vocabulary, dateStr) {
      if (!Array.isArray(vocabulary) || vocabulary.length === 0) return null;
      const hash = this.getDateHash(dateStr);
      const index = hash % vocabulary.length;
      return vocabulary[index];
    },

    /**
     * Spaced Repetition Scheduling based on demonstrated recall
     * Intervals: 1 day -> 3 days -> 7 days -> 14 days -> 30 days
     */
    getNextReviewDate(consecutiveSuccessCount) {
      const now = new Date();
      let daysToAdd = 1;
      
      if (consecutiveSuccessCount === 1) daysToAdd = 3;
      else if (consecutiveSuccessCount === 2) daysToAdd = 7;
      else if (consecutiveSuccessCount === 3) daysToAdd = 14;
      else if (consecutiveSuccessCount >= 4) daysToAdd = 30;
      
      const reviewDate = new Date(now.getTime() + daysToAdd * 24 * 60 * 60 * 1000);
      return reviewDate.toISOString().slice(0, 10);
    }
  };

  window.VocabularyEngine = VocabularyEngine;
})();
