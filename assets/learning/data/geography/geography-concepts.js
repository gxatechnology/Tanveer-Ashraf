/**
 * Tanveer Ashraf Judicial Prep - Indian Geography Concepts (Master Aggregator)
 * Aggregates Part 1 (Chapters 1 to 6) and Part 2 (Chapters 7 to 12)
 */

(function(global) {
  'use strict';

  function resolvePart(winProp, relPath) {
    if (typeof window !== 'undefined' && window[winProp]) {
      return window[winProp];
    }
    if (typeof require !== 'undefined') {
      try {
        var mod = require(relPath);
        return mod.concepts || mod;
      } catch (e) {
        return {};
      }
    }
    return {};
  }

  var part1 = resolvePart('GEOGRAPHY_CONCEPTS_PART1', './geography-concepts-part1.js');
  var part2 = resolvePart('GEOGRAPHY_CONCEPTS_PART2', './geography-concepts-part2.js');

  var ALL_CONCEPTS = {};
  var k;
  for (k in part1) { if (part1.hasOwnProperty(k)) { ALL_CONCEPTS[k] = part1[k]; } }
  for (k in part2) { if (part2.hasOwnProperty(k)) { ALL_CONCEPTS[k] = part2[k]; } }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { concepts: ALL_CONCEPTS };
  } else {
    global.GEOGRAPHY_CONCEPTS = ALL_CONCEPTS;
  }
})(typeof window !== 'undefined' ? window : global);
