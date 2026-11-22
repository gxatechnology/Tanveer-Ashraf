/**
 * Tanveer Ashraf Judicial Prep 2026–27
 * Social Legislation MCQs — Master Aggregator
 *
 * Combines:
 * - Part 1 (Acts 1-3): 150 MCQs
 * - Part 2 (Acts 4-6): 150 MCQs
 * - Part 3 (Acts 7-9): 155 MCQs
 *
 * Total: Exactly 455 Verified Practice MCQs
 * All 9 Social Legislation Acts (Paper I — General Knowledge / Social Legislation)
 */

(function(global) {
    'use strict';

    let allMCQs = [];

    // Part 1: Acts 1-3 (RPwD, Parents, Dowry)
    if (typeof global.SOCIAL_MCQS_PART1 !== 'undefined' && Array.isArray(global.SOCIAL_MCQS_PART1)) {
        allMCQs = allMCQs.concat(global.SOCIAL_MCQS_PART1);
    } else if (typeof require !== 'undefined') {
        try {
            const p1 = require('./social-mcqs-part1.js');
            if (Array.isArray(p1)) allMCQs = allMCQs.concat(p1);
        } catch (e) {
            console.warn('Could not load social-mcqs-part1.js via require', e);
        }
    }

    // Part 2: Acts 4-6 (DV, POSH, PCPNDT)
    if (typeof global.SOCIAL_MCQS_PART2 !== 'undefined' && Array.isArray(global.SOCIAL_MCQS_PART2)) {
        allMCQs = allMCQs.concat(global.SOCIAL_MCQS_PART2);
    } else if (typeof require !== 'undefined') {
        try {
            const p2 = require('./social-mcqs-part2.js');
            if (Array.isArray(p2)) allMCQs = allMCQs.concat(p2);
        } catch (e) {
            console.warn('Could not load social-mcqs-part2.js via require', e);
        }
    }

    // Part 3: Acts 7-9 (MTP, IRWA, POCSO)
    if (typeof global.SOCIAL_MCQS_PART3 !== 'undefined' && Array.isArray(global.SOCIAL_MCQS_PART3)) {
        allMCQs = allMCQs.concat(global.SOCIAL_MCQS_PART3);
    } else if (typeof require !== 'undefined') {
        try {
            const p3 = require('./social-mcqs-part3.js');
            if (Array.isArray(p3)) allMCQs = allMCQs.concat(p3);
        } catch (e) {
            console.warn('Could not load social-mcqs-part3.js via require', e);
        }
    }

    if (typeof module !== 'undefined' && module.exports) {
        module.exports = allMCQs;
    }
    global.SOCIAL_MCQS = allMCQs;
})(typeof window !== 'undefined' ? window : global);
