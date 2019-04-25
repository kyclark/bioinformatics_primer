#!/usr/bin/env python3
"""
Author:  Ken Youens-Clark <kyclark@email.arizona.edu>
Purpose: Subset FASTA/Q files
"""

import argparse
import os
import sys
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(
        description='Subset FASTA files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file', help='Input file', metavar='FILE')

    parser.add_argument(
        '-f',
        '--infmt',
        help='Input file format',
        type=str,
        metavar='FMT',
        choices=['fasta', 'fastq'],
        default='fasta')

    parser.add_argument(
        '-F',
        '--outfmt',
        help='Output file format',
        type=str,
        metavar='FMT',
        default=None)

    parser.add_argument(
        '-n',
        '--num',
        help='Number of sequences to take',
        type=int,
        metavar='NUM',
        default=500000)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        type=str,
        metavar='FILE',
        default='subset')

    parser.add_argument(
        '--force',
        help='Force overwrite of existing file',
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
    """main"""
    args = get_args()
    in_file = args.file
    in_fmt = args.infmt
    out_fmt = args.outfmt if args.outfmt else args.infmt
    out_file = args.outfile
    num_seqs = args.num

    if not os.path.isfile(in_file):
        die('--file "{}" is not a file'.format(in_file))

    if out_file == in_file:
        die('--outfile "{}" cannot be the same as input file'.format(out_file))

    if num_seqs < 1:
        die("--num cannot be less than one")

    if os.path.isfile(out_file) and not args.force:
        while True:
            answer = input(
                '--outfile "{}" exists. Overwrite [yes|no]? '.format(
                    out_file)).lower()
            if answer == 'no':
                print('Bye')
                sys.exit(1)
            elif answer == 'yes':
                break
            else:
                print('Please answer yes or no')

    out_fh = open(out_file, 'wt')
    num_written = 0

    for record in SeqIO.parse(in_file, in_fmt):
        SeqIO.write(record, out_fh, out_fmt)
        num_written += 1

        if num_written == num_seqs:
            break

    print('Done, wrote {} sequence{} to "{}"'.format(
        num_written, '' if num_written == 1 else 's', out_file))


# --------------------------------------------------
if __name__ == '__main__':
    main()
