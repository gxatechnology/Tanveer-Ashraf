/**
 * Judicial Learning Academy — Master Constitution Concepts Aggregator
 * Merges Part 1 (Ch 1–5, 12 topics), Part 2 (Ch 6–8, 11 topics), and Part 3 (Ch 9–15, 22 topics)
 * Total: 45 Comprehensive Authoritative Topics for UP PCS-J.
 */
(function() {
  'use strict';

  const p1 = (typeof window !== 'undefined' && window.CONSTITUTION_CONCEPTS_PART1) ||
             (typeof require !== 'undefined' ? require('./constitution-concepts-part1.js') : {});
  const p2 = (typeof window !== 'undefined' && window.CONSTITUTION_CONCEPTS_PART2) ||
             (typeof require !== 'undefined' ? require('./constitution-concepts-part2.js') : {});
  const p3 = (typeof window !== 'undefined' && window.CONSTITUTION_CONCEPTS_PART3) ||
             (typeof require !== 'undefined' ? require('./constitution-concepts-part3.js') : {});

  const CONSTITUTION_CONCEPTS = Object.assign({}, p1, p2, p3);

  if (typeof window !== 'undefined') {
    window.CONSTITUTION_CONCEPTS = CONSTITUTION_CONCEPTS;
  }
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONSTITUTION_CONCEPTS;
  }
})();
