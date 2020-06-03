#!/usr/bin/env python3
"""
Purpose: Calculate GC content
Author : Ken Youens-Clark <kyclark@gmail.com>
"""

import argparse
import re


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

    for seq in map(str.rstrip, args.file):
        if seq:
            # Use a regular expression to find G/Cs upper/lowercase
            gc = re.findall('[GgCc]', seq)
            pct = int((len(gc) / len(seq)) * 100)
            print(f'{pct:3}%: {seq}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
