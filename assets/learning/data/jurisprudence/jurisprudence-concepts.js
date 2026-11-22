/**
 * Judicial Learning Academy — Master Jurisprudence Concepts Aggregator
 * Merges Part 1 (Ch 1–4, 13 topics), Part 2 (Ch 5–7, 6 topics), and Part 3 (Ch 8–11, 11 topics)
 * Total: 30 Comprehensive Authoritative Topics for UP PCS-J.
 */
(function() {
  'use strict';

  const p1 = (typeof window !== 'undefined' && window.JURISPRUDENCE_CONCEPTS_PART1) ||
             (typeof require !== 'undefined' ? require('./jurisprudence-concepts-part1.js') : {});
  const p2 = (typeof window !== 'undefined' && window.JURISPRUDENCE_CONCEPTS_PART2) ||
             (typeof require !== 'undefined' ? require('./jurisprudence-concepts-part2.js') : {});
  const p3 = (typeof window !== 'undefined' && window.JURISPRUDENCE_CONCEPTS_PART3) ||
             (typeof require !== 'undefined' ? require('./jurisprudence-concepts-part3.js') : {});

  const JURISPRUDENCE_CONCEPTS = Object.assign({}, p1, p2, p3);

  const target = typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this);
  target.JURISPRUDENCE_CONCEPTS = JURISPRUDENCE_CONCEPTS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = JURISPRUDENCE_CONCEPTS;
  }
})();
