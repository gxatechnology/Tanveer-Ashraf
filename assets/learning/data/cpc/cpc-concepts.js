/**
 * Judicial Learning Academy — Master Civil Procedure Code Concepts Aggregator
 * Merges Part 1 (Ch 1–7, 19 topics), Part 2 (Ch 8–14, 19 topics), and Part 3 (Ch 15–20, 19 topics)
 * Total: 57 Comprehensive Authoritative Topics for UP PCS-J.
 */
(function() {
  'use strict';

  const p1 = (typeof window !== 'undefined' && window.CPC_CONCEPTS_PART1) ||
             (typeof require !== 'undefined' ? require('./cpc-concepts-part1.js') : {});
  const p2 = (typeof window !== 'undefined' && window.CPC_CONCEPTS_PART2) ||
             (typeof require !== 'undefined' ? require('./cpc-concepts-part2.js') : {});
  const p3 = (typeof window !== 'undefined' && window.CPC_CONCEPTS_PART3) ||
             (typeof require !== 'undefined' ? require('./cpc-concepts-part3.js') : {});

  const CPC_CONCEPTS = Object.assign({}, p1, p2, p3);

  const target = typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this);
  target.CPC_CONCEPTS = CPC_CONCEPTS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = CPC_CONCEPTS;
  }
})();
