#!/usr/bin/env python3
"""
Given a directory/list of FASTQ/A files like this:

    1.SRR170176.fastq
    2.SRR170506.fastq
    3.SRR170739.fastq
    4.SRR328519.fastq
    5.SRR047943.fastq
    6.SRR048028.fastq

Concatenate all the sequences into one file. If a header looks like this:

    @GPSBU5C02GK9PQ

Turn it into this:

    @1.SRR170176_GPSBU5C02GK9PQ

Author: Ken Youens-Clark <kyclark@email.arizona.edu>
Date: 17 September 2018
"""

import argparse
import os
import re
import sys
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(
        description='Input file(s)/directories',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'input', metavar='FILE_DIR', help='File or directory', nargs='+')

    parser.add_argument(
        '-l',
        '--limit',
        help='Limit per file',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output filename',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-i',
        '--in_format',
        help='Input file format',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-f',
        '--out_format',
        help='Output file format',
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
def find_files(inputs):
    files = []
    for arg in inputs:
        if os.path.isfile(arg):
            files.append(arg)
        elif os.path.isdir(arg):
            for filename in os.listdir(arg):
                files.append(os.path.join(arg, filename))

    if not files:
        die('No input files!')

    files.sort()

    return files


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    files = find_files(args.input)
    input_format = args.in_format
    output_format = args.out_format
    out_file = args.outfile
    limit_per_file = args.limit

    if not out_file:
        die('Missing --outfile')

    out_fh = open(out_file, 'wt')
    fastq_re = re.compile(r'^\.f(ast)?q$')
    num_seqs = 0
    num_files = len(files)

    print('Will process {} file{}'.format(num_files, ''
                                          if num_files == 1 else 's'))

    for i, filename in enumerate(files):
        basename = os.path.basename(filename)
        acc, ext = os.path.splitext(basename)
        print('{:3}: Processing {}'.format(i + 1, basename))

        file_format = input_format if input_format else 'fastq' if fastq_re.match(
            ext) else 'fasta'

        for j, record in enumerate(SeqIO.parse(filename, file_format)):
            num_seqs += 1
            record.id = '{}_{}'.format(acc, record.id)
            record.description = ''
            SeqIO.write(record, out_fh, output_format
                        if output_format else file_format)
            if limit_per_file > 0 and j + 1 == limit_per_file:
                break

    out_fh.close()

    print('Done, wrote {} to outfile "{}"'.format(num_seqs, out_file))


# --------------------------------------------------
if __name__ == '__main__':
    main()
