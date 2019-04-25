#!/usr/bin/env python3
"""Tetra-nucleotide counter"""

import sys
import os

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} DNA'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

dna = args[0]

count_a, count_c, count_g, count_t = 0, 0, 0, 0

for letter in dna:
    if letter == 'a' or letter == 'A':
        count_a += 1
    elif letter == 'c' or letter == 'C':
        count_c += 1
    elif letter == 'g' or letter == 'G':
        count_g += 1
    elif letter == 't' or letter == 'T':
        count_t += 1

print(' '.join([str(count_a), str(count_c), str(count_g), str(count_t)]))
