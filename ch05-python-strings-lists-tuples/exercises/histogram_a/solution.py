#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-04-22
Purpose: Histogrammer
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Histogrammer',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'numbers', metavar='int', type=int, nargs='+', help='Inputs')

    parser.add_argument(
        '-c',
        '--character',
        help='Character to represent',
        metavar='str',
        type=str,
        default='|')

    parser.add_argument(
        '-m',
        '--minimum',
        help='Minimum value to print',
        metavar='int',
        type=int,
        default=1)

    parser.add_argument(
        '-s',
        '--scale',
        help='Scale inputs',
        metavar='int',
        type=int,
        default=1)

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
    char = args.character
    scale = args.scale
    min_val = args.minimum
    numbers = args.numbers

    if scale < 1:
        die('--scale "{}" cannot be less than 1'.format(scale))

    if len(char) != 1:
        die('--character "{}" must be one character'.format(char))

    for num in sorted(filter(lambda n: n >= min_val, numbers)):
        print('{:3} {}'.format(num, char * int(num / scale)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
