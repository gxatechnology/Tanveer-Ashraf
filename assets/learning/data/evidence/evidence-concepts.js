/**
 * Judicial Learning Academy — Master Law of Evidence Concepts Aggregator
 * Merges Part 1 (Ch 1–3, 11 topics), Part 2 (Ch 4–7, 10 topics), and Part 3 (Ch 8–10, 9 topics)
 * Total: 30 Comprehensive Authoritative Topics for UP PCS-J.
 */
(function() {
  'use strict';

  const p1 = (typeof window !== 'undefined' && window.EVIDENCE_CONCEPTS_PART1) ||
             (typeof require !== 'undefined' ? require('./evidence-concepts-part1.js') : {});
  const p2 = (typeof window !== 'undefined' && window.EVIDENCE_CONCEPTS_PART2) ||
             (typeof require !== 'undefined' ? require('./evidence-concepts-part2.js') : {});
  const p3 = (typeof window !== 'undefined' && window.EVIDENCE_CONCEPTS_PART3) ||
             (typeof require !== 'undefined' ? require('./evidence-concepts-part3.js') : {});

  const EVIDENCE_CONCEPTS = Object.assign({}, p1, p2, p3);

  const target = typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this);
  target.EVIDENCE_CONCEPTS = EVIDENCE_CONCEPTS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = EVIDENCE_CONCEPTS;
  }
})();
