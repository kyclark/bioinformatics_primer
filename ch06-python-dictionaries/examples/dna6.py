#!/usr/bin/env python3
"""Tetra-nucleotide counter"""

import sys
import os
from collections import defaultdict

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} DNA'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

dna = args[0]

count = defaultdict(int)

for base in dna.lower():
    count[base] += 1

counts = []
for base in "acgt":
    counts.append(str(count[base]))

print(' '.join(counts))
