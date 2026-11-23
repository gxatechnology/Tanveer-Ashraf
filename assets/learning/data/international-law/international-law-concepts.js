/**
 * Tanveer Ashraf Judicial Prep - Master Concepts Aggregator
 */
(function(global) {
  'use strict';
  var p1 = global.INTERNATIONAL_LAW_CONCEPTS_PART1 || (typeof require !== 'undefined' ? require('./international-law-concepts-part1.js').INTERNATIONAL_LAW_CONCEPTS_PART1 : {});
  var p2 = global.INTERNATIONAL_LAW_CONCEPTS_PART2 || (typeof require !== 'undefined' ? require('./international-law-concepts-part2.js').INTERNATIONAL_LAW_CONCEPTS_PART2 : {});

  var INTERNATIONAL_LAW_CONCEPTS = Object.assign({}, p1, p2);
  global.INTERNATIONAL_LAW_CONCEPTS = INTERNATIONAL_LAW_CONCEPTS;

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { concepts: INTERNATIONAL_LAW_CONCEPTS, INTERNATIONAL_LAW_CONCEPTS: INTERNATIONAL_LAW_CONCEPTS };
  }
})(typeof window !== 'undefined' ? window : global);
