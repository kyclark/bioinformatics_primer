#!/usr/bin/env python3
"""Show recominations"""

import os
import sys
from itertools import product


def die(msg):
    """print and exit with an error"""
    print(msg)
    sys.exit(1)


def main():
    """main"""
    args = sys.argv[1:]

    if len(args) != 1:
        die('Usage: {} NUM_GENES'.format(os.path.basename(sys.argv[0])))

    if not args[0].isdigit():
        die('"{}" does not look like an integer'.format(args[0]))

    num_genes = int(args[0])
    min_num = 2
    max_num = 10
    if not min_num <= num_genes <= max_num:
        die('NUM_GENES must be between {} and {}'.format(min_num, max_num))

    ranger = range(1, num_genes + 1)
    promotors = ['P' + str(n + 1) for n in ranger]
    coding = ['C' + str(n + 1) for n in ranger]
    term = ['T' + str(n + 1) for n in ranger]

    print('N = "{}"'.format(num_genes))
    for i, combo in enumerate(product(promotors, coding, term), start=1):
        print('{:4}: {}'.format(i + 1, ' - '.join(combo)))


if __name__ == '__main__':
    main()
