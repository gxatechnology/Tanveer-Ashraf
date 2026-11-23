/**
 * Tanveer Ashraf Judicial Prep - Indian Economy Concepts (Master Aggregator)
 * Aggregates Part 1 (19 topics) + Part 2 (15 topics) = 34 Topics
 */

(function(global) {
  'use strict';

  var part1 = {};
  var part2 = {};

  if (typeof module !== 'undefined' && module.exports) {
    try { part1 = require('./economy-concepts-part1.js').concepts || {}; } catch(e) {}
    try { part2 = require('./economy-concepts-part2.js').concepts || {}; } catch(e) {}
  } else {
    part1 = global.ECONOMY_CONCEPTS_PART1 || {};
    part2 = global.ECONOMY_CONCEPTS_PART2 || {};
  }

  var ALL_CONCEPTS = Object.assign({}, part1, part2);

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { concepts: ALL_CONCEPTS, ECONOMY_CONCEPTS: ALL_CONCEPTS };
  } else {
    global.ECONOMY_CONCEPTS = ALL_CONCEPTS;
  }
})(typeof window !== 'undefined' ? window : global);
