#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-05-09
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'text', metavar='str', help='Input text')

    parser.add_argument(
        '-s',
        '--shift',
        help='Shift distance',
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
    text = args.text
    shift = args.shift

    if text == '-':
        text = sys.stdin.read()
    elif os.path.isfile(text):
        text = open(text).read()

    print(''.join(map(lambda c: chr(ord(c) + shift), text)).encode('utf-8'))

# --------------------------------------------------
if __name__ == '__main__':
    main()
