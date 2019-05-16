#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-05-16
Purpose: Greetings and saluatations
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Greetings and saluatations',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                        '--greeting',
                        help='The greeting',
                        metavar='str',
                        type=str,
                        default='Hello')

    parser.add_argument('-n',
                        '--name',
                        help='The name',
                        metavar='str',
                        type=str,
                        default='World')

    parser.add_argument('-e',
                        '--excited',
                        help='Whether to use an "!"',
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
    print('{}, {}{}'.format(args.greeting, args.name,
                            '!' if args.excited else '.'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
