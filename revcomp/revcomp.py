#!/usr/bin/env python3
"""Reverse complement DNA"""

import sys
import os

args = sys.argv

if len(args) != 2:
    print('Usage: {} DNA'.format(os.path.basename(args[0])))
    sys.exit(1)

dna = args[1]
rev = ''.join(list(reversed(dna)))
trans = str.maketrans('ACGTacgt', 'TGCAtgca')
print(rev.translate(trans))
