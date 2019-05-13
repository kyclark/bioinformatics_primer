#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-02-19
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
from Bio import SeqIO
from collections import Counter


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Segregate FASTA sequences by GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'fasta', metavar='FASTA', help='Input FASTA file(s)', nargs='+')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='DIR',
        type=str,
        default='out')

    parser.add_argument(
        '-p',
        '--pct_gc',
        help='Dividing line for percent GC',
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
    """Make a jazz noise here"""
    args = get_args()
    out_dir = args.outdir
    pct_gc = args.pct_gc

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    if not 0 < pct_gc <= 100:
        die('--pct_gc "{}" must be between 0 and 100'.format(pct_gc))

    num_seqs = 0
    for i, file in enumerate(args.fasta, start=1):
        if not os.path.isfile(file):
            warn('"{}" is not a file'.format(file))
            continue

        print('{:3}: {}'.format(i, os.path.basename(file)))

        base, ext = os.path.splitext(os.path.basename(file))
        high_file = os.path.join(out_dir, ''.join([base, '_high', ext]))
        low_file = os.path.join(out_dir, ''.join([base, '_low', ext]))

        high_fh = open(high_file, 'wt')
        low_fh = open(low_file, 'wt')

        for rec in SeqIO.parse(file, 'fasta'):
            num_seqs += 1
            bases = Counter(rec.seq.upper())
            gc = bases.get('G', 0) + bases.get('C', 0)
            pct = int((gc / len(rec.seq)) * 100)
            SeqIO.write(rec, low_fh if pct < pct_gc else high_fh, 'fasta')

    print('Done, wrote {} sequence{} to out dir "{}"'.format(
        num_seqs, '' if num_seqs == 1 else 's', out_dir))


# --------------------------------------------------
if __name__ == '__main__':
    main()
