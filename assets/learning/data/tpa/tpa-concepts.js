/**
 * Judicial Learning Academy — Master Transfer of Property Act (TPA) Concepts Aggregator
 * Merges Part 1 (Ch 1–3, 9 topics), Part 2 (Ch 4–5, 6 topics), and Part 3 (Ch 6–8, 9 topics)
 * Total: 24 Comprehensive Authoritative Topics for UP PCS-J.
 */
(function() {
  'use strict';

  const p1 = (typeof window !== 'undefined' && window.TPA_CONCEPTS_PART1) ||
             (typeof require !== 'undefined' ? require('./tpa-concepts-part1.js') : {});
  const p2 = (typeof window !== 'undefined' && window.TPA_CONCEPTS_PART2) ||
             (typeof require !== 'undefined' ? require('./tpa-concepts-part2.js') : {});
  const p3 = (typeof window !== 'undefined' && window.TPA_CONCEPTS_PART3) ||
             (typeof require !== 'undefined' ? require('./tpa-concepts-part3.js') : {});

  const TPA_CONCEPTS = Object.assign({}, p1, p2, p3);

  const target = typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this);
  target.TPA_CONCEPTS = TPA_CONCEPTS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = TPA_CONCEPTS;
  }
})();
