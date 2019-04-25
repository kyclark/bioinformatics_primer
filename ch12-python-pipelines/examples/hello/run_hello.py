#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-03-28
Purpose: Run "hello.sh"
"""

import argparse
import os
import sys
from subprocess import getstatusoutput


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Simple pipeline',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'name', metavar='str', nargs='+', help='Names for hello.sh')

    parser.add_argument(
        '-p',
        '--program',
        help='Program to run',
        metavar='str',
        type=str,
        default='./hello.sh')

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
    prg = args.program

    if not os.path.isfile(prg):
        die('Missing expected program "{}"'.format(prg))

    for name in args.name:
        cmd = '{} "{}"'.format(prg, name)
        rv, out = getstatusoutput(cmd)
        if rv != 0:
            warn('Failed to run: {}\nError: {}'.format(cmd, out))
        else:
            print('Success: "{}"'.format(out))

    print('Done.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
