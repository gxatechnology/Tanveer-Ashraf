/**
 * Judicial Learning Academy — Master Criminal Law Concepts Aggregator
 * Merges Part 1 (Ch 1–4, 12 topics), Part 2 (Ch 5–8, 14 topics), and Part 3 (Ch 9–12, 10 topics)
 * Total: 36 Comprehensive Authoritative Topics for UP PCS-J.
 */
(function() {
  'use strict';

  const p1 = (typeof window !== 'undefined' && window.CRIMINAL_CONCEPTS_PART1) ||
             (typeof require !== 'undefined' ? require('./criminal-concepts-part1.js') : {});
  const p2 = (typeof window !== 'undefined' && window.CRIMINAL_CONCEPTS_PART2) ||
             (typeof require !== 'undefined' ? require('./criminal-concepts-part2.js') : {});
  const p3 = (typeof window !== 'undefined' && window.CRIMINAL_CONCEPTS_PART3) ||
             (typeof require !== 'undefined' ? require('./criminal-concepts-part3.js') : {});

  const CRIMINAL_CONCEPTS = Object.assign({}, p1, p2, p3);

  const target = typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this);
  target.CRIMINAL_CONCEPTS = CRIMINAL_CONCEPTS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = CRIMINAL_CONCEPTS;
  }
})();
