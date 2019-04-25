#!/usr/bin/env python3
"""Show recominations"""

import os
import sys
from itertools import product, chain

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} NUM_GENES'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

if not args[0].isdigit():
    print('"{}" does not look like an integer'.format(args[0]))
    sys.exit(1)

num_genes = int(args[0])
if not 2 <= num_genes <= 10:
    print('NUM_GENES must be greater than 1, less than 10')
    sys.exit(1)

promotors = []
coding = []
terminators = []
for i in range(num_genes):
    n = str(i + 1)
    promotors.append('P' + n)
    coding.append('C' + n)
    terminators.append('T' + n)

print('N = "{}"'.format(num_genes))
for i, combo in enumerate(chain(product(promotors, coding, terminators))):
    print('{:3}: {}'.format(i + 1, combo))
