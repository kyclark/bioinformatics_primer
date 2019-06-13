#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-01-14
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    file = args[0]
    seqs = list(filter(lambda s: len(s) > 0, open(file).read().split('\n')))
    lens = set(map(len, seqs))

    if len(lens) > 1:
        print('Not all the same length!')
        sys.exit(1)

    length = list(lens)[0]
    is_conserved = []
    for i in range(length):
        chars = map(lambda s: s[i], seqs)
        is_conserved.append('|' if len(set(chars)) == 1 else 'X')

    print('\n'.join(seqs))
    print(''.join(is_conserved))


# --------------------------------------------------
main()
