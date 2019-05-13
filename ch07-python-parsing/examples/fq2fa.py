#!/usr/bin/env python3

import argparse
import os
import sys
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Converst FASTQ to FASTA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'fastq', metavar='FILE', nargs='+', help='FASTQ file(s)')

    parser.add_argument(
        '-e',
        '--extension',
        help='File extension',
        metavar='str',
        type=str,
        default='fa')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='str',
        type=str,
        default='out_fasta')

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

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    ext = args.extension
    if not ext.startswith('.'):
        ext = '.' + ext

    for i, fq in enumerate(args.fastq, start=1):
        basename = os.path.basename(fq)
        root, _ = os.path.splitext(basename)
        print('{:3}: {}'.format(i, basename))

        out_file = os.path.join(out_dir, root + ext)
        out_fh = open(out_file, 'wt')

        for record in SeqIO.parse(fq, 'fastq'):
            SeqIO.write(record, out_fh, 'fasta')

    print('Done, see output in "{}".'.format(out_dir))

# --------------------------------------------------
if __name__ == '__main__':
    main()
