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

    for line in args.file:
        seq = line.rstrip()
        if seq:
            # Iterate each base and compare to G or C, add 1 to counter
            gc = 0
            for base in seq.lower():
                if base == 'g' or base == 'c':
                    gc += 1
            pct = int((gc / len(seq)) * 100)
            print(f'{pct:3}%: {seq}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
