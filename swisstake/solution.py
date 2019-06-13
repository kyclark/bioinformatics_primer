#!/usr/bin/env python3
"""
Author:  Ken Youens-Clark <kyclark@gmail.com>
Purpose: Filter Swissprot file for keywords, taxa
"""

import argparse
import os
import sys
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(
        description='Filter Swissprot file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input', metavar='FILE', help='Uniprot file')

    parser.add_argument(
        '-s',
        '--skip',
        help='Skip taxa',
        metavar='STR',
        type=str,
        nargs='+',
        default='')

    parser.add_argument(
        '-k',
        '--keyword',
        help='Take on keyword',
        metavar='STR',
        type=str,
        required=True)

    parser.add_argument(
        '-o',
        '--output',
        help='Output filename',
        metavar='FILE',
        type=str,
        default='out.fa')

    return parser.parse_args()


# --------------------------------------------------
def die(msg='Something bad happened'):
    """print message and exit with error"""
    print(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """main"""
    args = get_args()
    input_file = args.input
    out_file = args.output
    keyword = args.keyword.lower()
    skip = set(map(str.lower, args.skip))

    if not os.path.isfile(input_file):
        die('"{}" is not a file'.format(input_file))

    print('Processing "{}"'.format(input_file))

    num_skipped = 0
    num_taken = 0
    with open(out_file, "w") as out_fh:
        for record in SeqIO.parse(input_file, "swiss"):
            annot = record.annotations
            if skip and 'taxonomy' in annot:
                taxa = set(map(str.lower, annot['taxonomy']))
                if skip.intersection(taxa):
                    num_skipped += 1
                    continue

            if 'keywords' in annot:
                kw = set(map(str.lower, annot['keywords']))

                if keyword in kw:
                    num_taken += 1
                    SeqIO.write(record, out_fh, 'fasta')
                else:
                    num_skipped += 1

    print('Done, skipped {} and took {}. See output in "{}".'.format(
        num_skipped, num_taken, out_file))


# --------------------------------------------------
if __name__ == '__main__':
    main()
