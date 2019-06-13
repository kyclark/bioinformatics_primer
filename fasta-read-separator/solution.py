#!/usr/bin/env python3
"""
Purpose: Split interleaved, paired reads into _1/2 files
Author:  Ken Youens-Clark <kyclark@email.arizona.edu>
"""

import argparse
import os
import sys
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(
        description='Split interleaved/paired reads',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'file', metavar='FILE', nargs='+', help='Input file(s)')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='DIR',
        type=str,
        default='split')

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
    out_dir = args.outdir

    if out_dir and not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    for fnum, file in enumerate(args.file):
        if not os.path.isfile(file):
            warn('"{}" is not a file'.format(file))
            continue

        filename = os.path.basename(file)
        base, ext = os.path.splitext(filename)
        forward = open(os.path.join(out_dir, base + '_1' + ext), 'wt')
        reverse = open(os.path.join(out_dir, base + '_2' + ext), 'wt')

        print("{:3d}: {}".format(fnum + 1, filename))

        num_seqs = 0
        for i, rec in enumerate(SeqIO.parse(file, 'fasta')):
            SeqIO.write(rec, forward if i % 2 == 0 else reverse, 'fasta')
            num_seqs += 1

        print('\tSplit {:,d} sequences to dir "{}"'.format(num_seqs, out_dir))


# --------------------------------------------------
if __name__ == '__main__':
    main()
