/**
 * Tanveer Ashraf Judicial Prep - Master Concepts Aggregator
 */
(function(global) {
  'use strict';
  var p1 = global.SCIENCE_CONCEPTS_PART1 || (typeof require !== 'undefined' ? require('./science-concepts-part1.js').SCIENCE_CONCEPTS_PART1 : {});
  var p2 = global.SCIENCE_CONCEPTS_PART2 || (typeof require !== 'undefined' ? require('./science-concepts-part2.js').SCIENCE_CONCEPTS_PART2 : {});

  var SCIENCE_CONCEPTS = Object.assign({}, p1, p2);
  global.SCIENCE_CONCEPTS = SCIENCE_CONCEPTS;

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { concepts: SCIENCE_CONCEPTS, SCIENCE_CONCEPTS: SCIENCE_CONCEPTS };
  }
})(typeof window !== 'undefined' ? window : global);
