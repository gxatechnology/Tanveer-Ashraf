/**
 * Tanveer Ashraf Judicial Prep - Master Concepts Aggregator
 */
(function(global) {
  'use strict';
  var p1 = global.TECH_CONCEPTS_PART1 || (typeof require !== 'undefined' ? require('./tech-concepts-part1.js').TECH_CONCEPTS_PART1 : {});
  var p2 = global.TECH_CONCEPTS_PART2 || (typeof require !== 'undefined' ? require('./tech-concepts-part2.js').TECH_CONCEPTS_PART2 : {});

  var TECH_CONCEPTS = Object.assign({}, p1, p2);
  global.TECH_CONCEPTS = TECH_CONCEPTS;

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { concepts: TECH_CONCEPTS, TECH_CONCEPTS: TECH_CONCEPTS };
  }
})(typeof window !== 'undefined' ? window : global);
