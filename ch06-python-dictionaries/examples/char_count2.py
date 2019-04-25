#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@email.arizona.edu>
Date   : 2019-02-06
Purpose: Character Counter
"""

import argparse
import os
import sys
from collections import Counter


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Character counter',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input', help='Filename or string to count', type=str)

    parser.add_argument(
        '-c',
        '--charsort',
        help='Sort by character',
        dest='charsort',
        action='store_true')

    parser.add_argument(
        '-n',
        '--numsort',
        help='Sort by number',
        dest='numsort',
        action='store_true')

    parser.add_argument(
        '-r',
        '--reverse',
        help='Sort in reverse order',
        dest='reverse',
        action='store_true')

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
    input_arg = args.input
    charsort = args.charsort
    numsort = args.numsort
    revsort = args.reverse

    if charsort and numsort:
        die('Please choose one of --charsort or --numsort')

    if not charsort and not numsort:
        charsort = True

    text = ''
    if os.path.isfile(input_arg):
        text = ''.join(open(input_arg).read().splitlines())
    else:
        text = input_arg

    count = Counter(text.lower())

    if charsort:
        letters = sorted(count.keys())
        if revsort:
            letters.reverse()

        for letter in letters:
            print('{} {:5}'.format(letter, count[letter]))
    else:
        pairs = sorted([(x[1], x[0]) for x in count.items()])
        if revsort:
            pairs.reverse()

        for n, char in pairs:
            print('{} {:5}'.format(char, n))


# --------------------------------------------------
if __name__ == '__main__':
    main()
