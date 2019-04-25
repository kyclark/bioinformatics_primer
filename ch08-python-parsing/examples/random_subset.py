#!/usr/bin/env python3
"""
Author:  Ken Youens-Clark <kyclark@email.arizona.edu>
Purpose: Probabalistically subset FASTQ/A
"""

import argparse
import os
import re
import sys
from random import randint
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(
        description='Randomly subset FASTQ',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file', metavar='FILE', help='FASTQ/A file')

    parser.add_argument(
        '-p',
        '--pct',
        help='Percent of reads',
        metavar='int',
        type=int,
        default=50)

    parser.add_argument(
        '-m',
        '--max',
        help='Maximum number of reads',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-f',
        '--input_format',
        help='Intput format',
        metavar='IN_FMT',
        type=str,
        choices=['fastq', 'fasta'],
        default='')

    parser.add_argument(
        '-F',
        '--output_format',
        help='Output format',
        metavar='OUT_FMT',
        type=str,
        choices=['fastq', 'fasta'],
        default='')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
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
    """main"""
    args = get_args()
    file = args.file
    pct = args.pct
    out_file = args.outfile
    max_num_reads = args.max
    min_num = 0
    max_num = 100

    if not os.path.isfile(file):
        die('"{}" is not a file'.format(file))

    in_fmt = args.input_format
    if not in_fmt:
        _, ext = os.path.splitext(file)
        in_fmt = 'fastq' if re.match('\.f(ast)?q$', ext) else 'fasta'

    out_fmt = args.output_format or in_fmt

    if not min_num < pct < max_num:
        msg = '--pct "{}" must be between {} and {}'
        die(msg.format(pct, min_num, max_num))

    if not out_file:
        base, _ = os.path.splitext(file)
        out_file = '{}.sub{}.{}'.format(base, pct, out_fmt)

    out_fh = open(out_file, 'wt')
    num_taken = 0
    total_num = 0

    with open(file) as fh:
        for rec in SeqIO.parse(fh, in_fmt):
            total_num += 1
            if randint(min_num, max_num) <= pct:
                num_taken += 1
                SeqIO.write(rec, out_fh, out_fmt)
                if max_num_reads > 0 and num_taken == max_num_reads:
                    break

    out_fh.close()

    print('Wrote {} of {} ({:.02f}%) to "{}"'.format(
        num_taken, total_num, num_taken / total_num * 100, out_file))


# --------------------------------------------------
if __name__ == '__main__':
    main()
