#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@email.arizona.edu>
Date   : 2019-08-06
Purpose: Grep through FASTX files
"""

import argparse
import os
import re
import sys
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Grep through FASTX files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='PATTERN',
                        type=str,
                        help='Search pattern')

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='Input file(s)')

    parser.add_argument('-f',
                        '--format',
                        help='Input file format',
                        metavar='str',
                        choices=['fasta', 'fastq'],
                        default='fasta')

    parser.add_argument('-o',
                        '--out_format',
                        help='Output file format',
                        metavar='str',
                        choices=['fasta', 'fastq', 'fasta-2line'],
                        default='')

    parser.add_argument('-O',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fmt = args.out_format or args.format
    regex = re.compile(args.pattern)
    out_fh = args.outfile or sys.stdout
    checked, took = 0, 0

    for file in args.file:
        for rec in SeqIO.parse(file, args.format):
            checked += 1
            if any(map(regex.search, [rec.id, rec.description])):
                took += 1
                SeqIO.write(rec, out_fh, out_fmt)

    print(f'Done, checked {checked}, took {took}.', file=sys.stderr)


# --------------------------------------------------
if __name__ == '__main__':
    main()
