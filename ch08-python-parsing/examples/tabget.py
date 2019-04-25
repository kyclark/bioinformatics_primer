#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2018-11-16
Purpose: Get fields from a tab/csv file
"""

import argparse
import csv
import os
import re
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'file', nargs='+', metavar='FILE', help='Input file(s)')

    parser.add_argument(
        '-d',
        '--delimiter',
        help='Field delimiter',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-f',
        '--field',
        help='Name of field(s)',
        metavar='str',
        type=str,
        default='')

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
    files = args.file
    default_delim = args.delimiter
    field_names = re.split('\s*,\s*', args.field)

    for file in files:
        with open(file, 'rt') as fh:
            delim = default_delim
            if not delim:
                _, ext = os.path.splitext(file)
                if ext == '.csv':
                    delim = ','
                else:
                    delim = '\t'

            reader = csv.DictReader(fh, delimiter=delim)

            print(delim.join(field_names))

            for row in reader:
                flds = list(map(lambda f: row[f], field_names))
                print(delim.join(flds))


# --------------------------------------------------
if __name__ == '__main__':
    main()
