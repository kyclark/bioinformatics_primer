#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-02-06
Purpose: Print the first lines and file names
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
        'dir', metavar='DIR', help='Input directory', nargs='+')

    parser.add_argument(
        '-w',
        '--width',
        help='Text width',
        metavar='int',
        type=int,
        default=50)

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
    args = get_args()
    dirs = args.dir
    width = args.width

    for dirname in dirs:
        if not os.path.isdir(dirname):
            warn('"{}" is not a directory'.format(dirname))
            continue

        print(os.path.basename(dirname))
        lines_by_file = {}
        for file in os.listdir(dirname):
            path = os.path.join(dirname, file)
            if os.path.isfile(path):
                lines_by_file[file] = open(path).readline().rstrip()

        pairs = sorted([(x[1], x[0]) for x in lines_by_file.items()])

        for line, file in pairs:
            ellipses = '.' * (width - len(line) - len(file))
            print(line, ellipses, file)


# --------------------------------------------------
if __name__ == '__main__':
    main()
