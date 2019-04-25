#!/usr/bin/env python3
"""Tetra-nucleotide counter"""

import sys
import os

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} DNA'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

dna = args[0]

count = {'a': 0, 'c': 0, 'g': 0, 't': 0}

for base in dna.lower():
    if base in count:
        count[base] += 1

counts = []
for base in sorted(count.keys()):
    counts.append(str(count[base]))

print(' '.join(counts))
