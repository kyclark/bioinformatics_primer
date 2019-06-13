#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-05-16
Purpose: Identify sequences by alphabet
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Identify sequences by alphabet',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq', metavar='str', nargs='+', help='Sequence(s)')

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

    alpha = [('DNA', 'ACTGN'), ('RNA', 'ACUGN'), ('Protein', 'A-Z')]
    for seq in args.seq:
        guess = 'Unknown'
        for seq_type, pattern in alpha:
            if re.search('^[{}]+$'.format(pattern), seq):
                guess = seq_type
                break

        print('{} {}'.format(guess, seq))


# --------------------------------------------------
if __name__ == '__main__':
    main()
