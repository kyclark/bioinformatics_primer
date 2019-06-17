#!/usr/bin/env python3
"""Emulate wc"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        nargs='+',
                        help='Input file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for fh in args.file:
        chars, words, lines = 0, 0, 0
        for line in fh:
            lines += 1
            chars += len(line)
            words += len(line.split())

        print('{:>8}{:>8}{:>8} {}'.format(lines, words, chars, fh.name))


# --------------------------------------------------
if __name__ == '__main__':
    main()
