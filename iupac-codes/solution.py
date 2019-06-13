#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-05-15
Purpose: Turn IUPAC DNA codes into regex
"""

import argparse
import re
import sys
from itertools import product


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Turn IUPAC DNA codes into regex',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern', metavar='str', help='A positional argument')

    # parser.add_argument(
    #     '-a',
    #     '--arg',
    #     help='A named string argument',
    #     metavar='str',
    #     type=str,
    #     default='')

    # parser.add_argument(
    #     '-i',
    #     '--int',
    #     help='A named integer argument',
    #     metavar='int',
    #     type=int,
    #     default=0)

    # parser.add_argument(
    #     '-f', '--flag', help='A boolean flag', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    pattern = args.pattern
    trans = dict([('A', ('A', )), ('C', ('C', )), ('G', ('G', )),
                  ('T', ('T', )), ('U', ('U', )), ('R', ('A', 'G')),
                  ('Y', ('C', 'T')), ('S', ('G', 'C')), ('W', ('A', 'T')),
                  ('K', ('G', 'T')), ('M', ('A', 'C')), ('B', ('C', 'G', 'T')),
                  ('D', ('A', 'G', 'T')), ('H', ('A', 'C', 'T')),
                  ('V', ('A', 'C', 'G')), ('N', ('A', 'C', 'G', 'T'))])

    bases = sorted(trans.keys())
    if not re.search('^[' + ''.join(bases) + ']+$', pattern):
        die('Pattern must contain only {}.'.format(', '.join(bases)))

    iupac = list(map(lambda base: trans[base], pattern))
    regex = '^' + ''.join(
        map(lambda t: '[' + ''.join(t) + ']' if len(t) > 1 else t[0],
            iupac)) + '$'

    print('pattern = "{}"'.format(pattern))
    print('regex   = "{}"'.format(regex))

    for possibility in sorted(product(*iupac)):
        dna = ''.join(possibility)
        print(dna, 'OK' if re.search(regex, dna) else 'NO')

# --------------------------------------------------
if __name__ == '__main__':
    main()
