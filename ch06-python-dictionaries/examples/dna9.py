#!/usr/bin/env python3
"""Tetra-nucleotide counter"""

import sys
import os
from collections import defaultdict

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} DNA'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

arg = args[0]
dna = ''
if os.path.isfile(arg):
    dna = ''.join(open(arg).read().splitlines())
else:
    dna = arg

count = defaultdict(int)
for base in dna.lower():
    count[base] += 1

print(' '.join(map(lambda b: str(count[b]), "acgt")))
