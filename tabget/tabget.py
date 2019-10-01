#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2018-11-16
Purpose: Get fields from a tab/csv file
"""

import argparse
import csv
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Get fields from delimited text files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        nargs='+',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='Input file(s)')

    parser.add_argument('-f',
                        '--field',
                        help='Field name(s)',
                        metavar='str',
                        type=str,
                        nargs='+')

    parser.add_argument('-d',
                        '--delimiter',
                        help='Field delimiter',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='str',
                        type=str,
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout

    for fh in args.file:
        delim = args.delimiter or guess_delim(fh.name)
        reader = csv.DictReader(fh, delimiter=delim)
        missing = [f for f in args.field if f not in reader.fieldnames]

        if missing:
            print('"{}" missing: {}'.format(fh.name, ', '.join(missing)),
                  file=sys.stderr)
            continue

        for row in reader:
            flds = list(
                filter(lambda s: s, map(lambda f: row[f].strip(), args.field)))

            if flds:
                out_fh.write(delim.join(flds) + '\n')


# --------------------------------------------------
def guess_delim(filename):
    """Guess the delimiter from the file name"""

    ext = os.path.splitext(filename)[-1]
    return ',' if ext == '.csv' else '\t'


# --------------------------------------------------
def test_guess_delim():
    """Test guess_delim"""

    assert guess_delim('foo.txt') == '\t'
    assert guess_delim('foo.csv') == ','
    assert guess_delim('foo.tab') == '\t'


# --------------------------------------------------
if __name__ == '__main__':
    main()
