/**
 * Tanveer Ashraf Judicial Prep - Master Concepts Aggregator
 */
(function(global) {
  'use strict';
  var p1 = global.INTERNATIONAL_CONCEPTS_PART1 || (typeof require !== 'undefined' ? require('./international-concepts-part1.js').INTERNATIONAL_CONCEPTS_PART1 : {});
  var p2 = global.INTERNATIONAL_CONCEPTS_PART2 || (typeof require !== 'undefined' ? require('./international-concepts-part2.js').INTERNATIONAL_CONCEPTS_PART2 : {});

  var INTERNATIONAL_CONCEPTS = Object.assign({}, p1, p2);
  global.INTERNATIONAL_CONCEPTS = INTERNATIONAL_CONCEPTS;

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { concepts: INTERNATIONAL_CONCEPTS, INTERNATIONAL_CONCEPTS: INTERNATIONAL_CONCEPTS };
  }
})(typeof window !== 'undefined' ? window : global);
