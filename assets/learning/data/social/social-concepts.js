/**
 * Judicial Learning Academy — Master Social Legislation Concepts Aggregator
 * Merges Part 1 (Acts 1–3, 27 topics), Part 2 (Acts 4–6, 27 topics), and Part 3 (Acts 7–9, 30 topics)
 * Total: 84 Comprehensive Authoritative Topics for UP PCS-J (Paper I — General Knowledge).
 */
(function() {
  'use strict';

  const p1 = (typeof window !== 'undefined' && window.SOCIAL_CONCEPTS_PART1) ||
             (typeof require !== 'undefined' ? require('./social-concepts-part1.js') : {});
  const p2 = (typeof window !== 'undefined' && window.SOCIAL_CONCEPTS_PART2) ||
             (typeof require !== 'undefined' ? require('./social-concepts-part2.js') : {});
  const p3 = (typeof window !== 'undefined' && window.SOCIAL_CONCEPTS_PART3) ||
             (typeof require !== 'undefined' ? require('./social-concepts-part3.js') : {});

  const SOCIAL_CONCEPTS = Object.assign({}, p1, p2, p3);

  const target = typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this);
  target.SOCIAL_CONCEPTS = SOCIAL_CONCEPTS;
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = SOCIAL_CONCEPTS;
  }
})();
