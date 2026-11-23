/**
 * Tanveer Ashraf Judicial Prep - Master Concepts Aggregator
 */
(function(global) {
  'use strict';
  var p1 = global.COMM_CONCEPTS_PART1 || (typeof require !== 'undefined' ? require('./comm-concepts-part1.js').COMM_CONCEPTS_PART1 : {});
  var p2 = global.COMM_CONCEPTS_PART2 || (typeof require !== 'undefined' ? require('./comm-concepts-part2.js').COMM_CONCEPTS_PART2 : {});

  var COMM_CONCEPTS = Object.assign({}, p1, p2);
  global.COMM_CONCEPTS = COMM_CONCEPTS;

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { concepts: COMM_CONCEPTS, COMM_CONCEPTS: COMM_CONCEPTS };
  }
})(typeof window !== 'undefined' ? window : global);
