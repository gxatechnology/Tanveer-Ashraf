# -*- coding: utf-8 -*-
"""
Solver and builder for 30 crosswords with legal vocabulary.
"""
import json
import os
import random
from crossword_compiler import WORDS, VOCAB_MAP, build_puzzle

# Index words by length and by (position, letter)
words_by_len = {}
words_by_len_pos_letter = {}

for w in WORDS:
    l = len(w)
    if l not in words_by_len:
        words_by_len[l] = []
    words_by_len[l].append(w)
    
    for pos, ch in enumerate(w):
        key = (l, pos, ch)
        if key not in words_by_len_pos_letter:
            words_by_len_pos_letter[key] = []
        words_by_len_pos_letter[key].append(w)

def find_words_matching(length, letter_constraints):
    """
    Find words of given length where letter_constraints is dict {pos: char}.
    """
    if not letter_constraints:
        return words_by_len.get(length, [])
    
    # Start with smallest candidate set
    sorted_constraints = sorted(letter_constraints.items(), key=lambda x: len(words_by_len_pos_letter.get((length, x[0], x[1]), [])))
    first_pos, first_ch = sorted_constraints[0]
    candidates = set(words_by_len_pos_letter.get((length, first_pos, first_ch), []))
    
    for pos, ch in sorted_constraints[1:]:
        candidates.intersection_update(words_by_len_pos_letter.get((length, pos, ch), []))
        if not candidates:
            break
            
    return list(candidates)

print(f"Index built. Tested find_words_matching(5, {{0: 'C', 4: 'T'}}): {find_words_matching(5, {0: 'C', 4: 'T'})}")
