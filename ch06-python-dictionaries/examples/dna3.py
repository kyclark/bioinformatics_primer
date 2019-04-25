#!/usr/bin/env python3
"""Tetra-nucleotide counter"""

import sys
import os

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} DNA'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

dna = args[0]

count = {}

for base in dna.lower():
    if not base in count:
        count[base] = 0

    count[base] += 1

counts = []
for base in "acgt":
    num = count[base] if base in count else 0
    counts.append(str(num))

print(' '.join(counts))
