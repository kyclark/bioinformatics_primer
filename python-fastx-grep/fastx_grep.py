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
                        default='')

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
def guess_format(file):
    """Guess format from extension"""

    _, ext = os.path.splitext(file)
    ext = ext[1:] if ext.startswith('.') else ext

    return 'fasta' if re.match(
        'f(ast|n)?a$', ext) else 'fastq' if re.match('f(ast)?q$', ext) else ''


# --------------------------------------------------
def test_guess_format():
    """Test guess_format"""

    assert guess_format('/foo/bar.fa') == 'fasta'
    assert guess_format('/foo/bar.fna') == 'fasta'
    assert guess_format('/foo/bar.fasta') == 'fasta'
    assert guess_format('/foo/bar.fq') == 'fastq'
    assert guess_format('/foo/bar.fastq') == 'fastq'
    assert guess_format('/foo/bar.fx') == ''


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    regex = re.compile(args.pattern)
    out_fh = args.outfile or sys.stdout
    checked, took = 0, 0

    for fh in args.file:
        in_format = args.format or guess_format(fh.name)
        for rec in SeqIO.parse(fh, in_format):
            checked += 1
            out_fmt = args.out_format or args.format
            if any(map(regex.search, [rec.id, rec.description])):
                took += 1
                SeqIO.write(rec, out_fh, args.out_format or in_format)

    print(f'Done, checked {checked}, took {took}.', file=sys.stderr)


# --------------------------------------------------
if __name__ == '__main__':
    main()
