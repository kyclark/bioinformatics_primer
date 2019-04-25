#!/usr/bin/env python3
"""
Author:  Ken Youens-Clark
Purpose: Split FASTA files
NB:      If you have FASTQ files, maybe just use "split"?
"""

import argparse
import os
import sys
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(
        description='Split FASTA/Q files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file', help='FASTA input file(s)', nargs='+')

    parser.add_argument(
        '-f',
        '--input_format',
        help='Input file format',
        type=str,
        metavar='FORMAT',
        choices=['fasta', 'fastq'],
        default='fasta')

    parser.add_argument(
        '-F',
        '--output_format',
        help='Output file format',
        type=str,
        metavar='FORMAT',
        choices=['fasta', 'fastq'],
        default='fasta')

    parser.add_argument(
        '-n',
        '--sequences_per_file',
        help='Number of sequences per file',
        type=int,
        metavar='NUM',
        default=50)

    parser.add_argument(
        '-o',
        '--out_dir',
        help='Output directory',
        type=str,
        metavar='DIR',
        default='fasplit')

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
    files = args.file
    input_format = args.input_format
    output_format = args.output_format
    out_dir = args.out_dir
    seqs_per_file = args.sequences_per_file

    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)

    if seqs_per_file < 1:
        die('--sequences_per_file "{}" cannot be less than one'.format(
            seqs_per_file))

    num_files = 0
    num_seqs_written = 0
    for i, file in enumerate(files, start=1):
        print('{:3d}: {}'.format(i, os.path.basename(file)))
        num_files += 1
        num_seqs_written += process(
            file=file,
            input_format=input_format,
            output_format=output_format,
            out_dir=out_dir,
            seqs_per_file=seqs_per_file)

    print('Done, processed {} sequence{} from {} file{} into "{}"'.format(
        num_seqs_written, '' if num_seqs_written == 1 else 's', num_files, ''
        if num_files == 1 else 's', out_dir))


# --------------------------------------------------
def process(file, input_format, output_format, out_dir, seqs_per_file):
    """
    Spilt file into smaller files into out_dir
    Optionally convert to output format
    Return number of sequences written
    """
    if not os.path.isfile(file):
        warn('"{}" is not valid'.format(file))
        return 0

    basename, ext = os.path.splitext(os.path.basename(file))
    out_fh = None
    i = 0
    num_written = 0
    nfile = 0
    for record in SeqIO.parse(file, input_format):
        if i == seqs_per_file:
            i = 0
            if out_fh is not None:
                out_fh.close()
                out_fh = None

        i += 1
        num_written += 1
        if out_fh is None:
            nfile += 1
            path = os.path.join(out_dir,
                                basename + '.' + '{:04d}'.format(nfile) + ext)
            out_fh = open(path, 'wt')

        SeqIO.write(record, out_fh, output_format)

    return num_written


# --------------------------------------------------
if __name__ == '__main__':
    main()
