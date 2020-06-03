#!/usr/bin/env python3
"""
Purpose: Calculate GC content
Author : Ken Youens-Clark <kyclark@gmail.com>
"""

import argparse


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Calculate GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input sequence file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Make a jazz noise here """

    args = get_args()

    # Use a map()/lambda to strip newlines
    for seq in map(str.rstrip, args.file):
        if seq:
            # Use filter() to select only G/C
            gc = list(filter(lambda base: base == 'g' or base == 'c', seq.lower()))
            pct = int((len(gc) / len(seq)) * 100)
            print(f'{pct:3}%: {seq}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
