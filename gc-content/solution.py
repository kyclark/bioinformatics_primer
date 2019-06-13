#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-02-19
Purpose: Calculate GC content
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Calculate GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file', metavar='FILE', help='Input FASTA')

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
    file = args.file

    if not os.path.isfile(file):
        die('"{}" is not a file'.format(file))

    for i, line in enumerate(open(file), start=1):
        # Method 1
        gc = 0
        for char in line.lower():
            if char == 'g' or char == 'c':
                gc += 1

        # Method 2
        line = line.lower()
        gc = line.count('g') + line.count('c')

        pct = int((gc / len(line)) * 100)
        print('{:3}: {:3}%'.format(i, pct))


# --------------------------------------------------
if __name__ == '__main__':
    main()
