#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-05-14
Purpose: Rock the Casbah
"""

import argparse
import re
import sys
from itertools import product


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('plate', metavar='PLATE', help='License plate')

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
    plate = args.plate
    print('plate = "{}"'.format(plate))
    mixups = [('5', 'S'), ('X', 'K'), ('1', 'I'), ('3', 'E'), ('0', 'O', 'Q'),
              ('M', 'N'), ('U', 'V', 'W'), ('2', '7')]

    chars = []
    for char in plate:
        group = list(filter(lambda t: char in t, mixups))
        if group:
            chars.append(group[0])
        else:
            chars.append((char, ))

    regex = '^{}$'.format(''.join(
        map(lambda t: '[' + ''.join(t) + ']' if len(t) > 1 else t[0], chars)))
    print('regex = "{}"'.format(regex))

    for possible in sorted(product(*chars)):
        s = ''.join(possible)
        print(s, 'OK' if re.search(regex, s) else 'NO')


# --------------------------------------------------
if __name__ == '__main__':
    main()
