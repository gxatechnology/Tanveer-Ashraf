/**
 * Tanveer Ashraf Judicial Prep - Master Concepts Aggregator
 */
(function(global) {
  'use strict';
  var p1 = global.CURRENT_CONCEPTS_PART1 || (typeof require !== 'undefined' ? require('./current-concepts-part1.js').CURRENT_CONCEPTS_PART1 : {});
  var p2 = global.CURRENT_CONCEPTS_PART2 || (typeof require !== 'undefined' ? require('./current-concepts-part2.js').CURRENT_CONCEPTS_PART2 : {});

  var CURRENT_CONCEPTS = Object.assign({}, p1, p2);
  global.CURRENT_CONCEPTS = CURRENT_CONCEPTS;

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { concepts: CURRENT_CONCEPTS, CURRENT_CONCEPTS: CURRENT_CONCEPTS };
  }
})(typeof window !== 'undefined' ? window : global);
