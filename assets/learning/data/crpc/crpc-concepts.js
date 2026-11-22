/**
 * Judicial Learning Academy — Master Criminal Procedure Concepts Aggregator
 * Merges Part 1 (Ch 1–4, 12 topics), Part 2 (Ch 5–8, 10 topics), and Part 3 (Ch 9–12, 13 topics)
 * Total: 35 Comprehensive Authoritative Topics for UP PCS-J.
 */
(function() {
  'use strict';

  const p1 = (typeof window !== 'undefined' && window.CRPC_CONCEPTS_PART1) ||
             (typeof require !== 'undefined' ? require('./crpc-concepts-part1.js') : {});
  const p2 = (typeof window !== 'undefined' && window.CRPC_CONCEPTS_PART2) ||
             (typeof require !== 'undefined' ? require('./crpc-concepts-part2.js') : {});
  const p3 = (typeof window !== 'undefined' && window.CRPC_CONCEPTS_PART3) ||
             (typeof require !== 'undefined' ? require('./crpc-concepts-part3.js') : {});

  const CRPC_CONCEPTS = Object.assign({}, p1, p2, p3);

  const target = typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this);
  target.CRPC_CONCEPTS = CRPC_CONCEPTS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = CRPC_CONCEPTS;
  }
})();
