/**
 * Tanveer Ashraf Judicial Prep - Master Concepts Aggregator
 */
(function(global) {
  'use strict';
  var p1 = global.SPACE_CONCEPTS_PART1 || (typeof require !== 'undefined' ? require('./space-concepts-part1.js').SPACE_CONCEPTS_PART1 : {});
  var p2 = global.SPACE_CONCEPTS_PART2 || (typeof require !== 'undefined' ? require('./space-concepts-part2.js').SPACE_CONCEPTS_PART2 : {});

  var SPACE_CONCEPTS = Object.assign({}, p1, p2);
  global.SPACE_CONCEPTS = SPACE_CONCEPTS;

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { concepts: SPACE_CONCEPTS, SPACE_CONCEPTS: SPACE_CONCEPTS };
  }
})(typeof window !== 'undefined' ? window : global);
