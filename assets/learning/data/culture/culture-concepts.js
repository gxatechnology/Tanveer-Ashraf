/**
 * TANVEER ASHRAF — JUDICIAL PREP 2026–27
 * Indian Culture Concept Notes Master Aggregator (Paper I — General Knowledge)
 * Merges Part 1 (15 topics) and Part 2 (13 topics)
 * Total: 28 Comprehensive Thematic Topics across 12 Chapters.
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

  const p1 = resolvePart('CULTURE_CONCEPTS_PART1', './culture-concepts-part1.js');
  const p2 = resolvePart('CULTURE_CONCEPTS_PART2', './culture-concepts-part2.js');

  const ALL_CONCEPTS = Object.assign({}, p1, p2);

  global.CULTURE_CONCEPTS = ALL_CONCEPTS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { concepts: ALL_CONCEPTS, default: ALL_CONCEPTS };
  }
})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
