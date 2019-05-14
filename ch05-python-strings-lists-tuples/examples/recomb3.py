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
    if not 2 <= num_genes <= 10:
        die('NUM_GENES must be greater than 1, less than 10')

    def gen(prefix):
        return [prefix + str(n) for n in range(1, num_genes + 1)]

    print('N = "{}"'.format(num_genes))
    combos = product(gen('P'), gen('C'), gen('T'))
    for i, combo in enumerate(combos, start=1):
        print('{:4}: {}'.format(i, ' - '.join(combo)))


if __name__ == '__main__':
    main()
