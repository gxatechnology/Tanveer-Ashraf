/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * History of India Concept Notes Master Aggregator (Paper I — General Knowledge)
 * Merges Part 1 (13 topics), Part 2 (13 topics), and Part 3 (12 topics)
 * Total: 38 Comprehensive Chronological Topics across 15 Chapters.
 */
(function(global) {
  "use strict";

  function resolvePart(winProp, relPath) {
    if (typeof window !== 'undefined' && window[winProp]) {
      return window[winProp];
    }
    if (typeof global !== 'undefined' && global[winProp]) {
      return global[winProp];
    }
    if (typeof require !== 'undefined') {
      try {
        const mod = require(relPath);
        return (mod && mod.concepts) ? mod.concepts : (mod || {});
      } catch (e) {
        return {};
      }
    }
    return {};
  }

  const p1 = resolvePart('HISTORY_CONCEPTS_PART1', './history-concepts-part1.js');
  const p2 = resolvePart('HISTORY_CONCEPTS_PART2', './history-concepts-part2.js');
  const p3 = resolvePart('HISTORY_CONCEPTS_PART3', './history-concepts-part3.js');

  const ALL_CONCEPTS = Object.assign({}, p1, p2, p3);

  global.HISTORY_CONCEPTS = ALL_CONCEPTS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { concepts: ALL_CONCEPTS, default: ALL_CONCEPTS };
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
