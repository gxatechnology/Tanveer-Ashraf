/**
 * Tanveer Ashraf Judicial Prep - Master Concepts Aggregator
 */
(function(global) {
  'use strict';
  var p1 = global.SOCIAL_ISSUES_CONCEPTS_PART1 || (typeof require !== 'undefined' ? require('./social-issues-concepts-part1.js').SOCIAL_ISSUES_CONCEPTS_PART1 : {});
  var p2 = global.SOCIAL_ISSUES_CONCEPTS_PART2 || (typeof require !== 'undefined' ? require('./social-issues-concepts-part2.js').SOCIAL_ISSUES_CONCEPTS_PART2 : {});

  var SOCIAL_ISSUES_CONCEPTS = Object.assign({}, p1, p2);
  global.SOCIAL_ISSUES_CONCEPTS = SOCIAL_ISSUES_CONCEPTS;

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { concepts: SOCIAL_ISSUES_CONCEPTS, SOCIAL_ISSUES_CONCEPTS: SOCIAL_ISSUES_CONCEPTS };
  }
})(typeof window !== 'undefined' ? window : global);
