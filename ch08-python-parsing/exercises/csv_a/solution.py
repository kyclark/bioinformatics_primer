#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-02-25
Purpose: Rock the Casbah
"""

import argparse
import csv
import os
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'hits', metavar='FILE', help='BLAST output (-outfmt 6)')

    parser.add_argument(
        '-a',
        '--annotations',
        help='Annotation file',
        metavar='FILE',
        type=str,
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
    """Make a jazz noise here"""
    args = get_args()
    hits_file = args.hits
    annots_file = args.annotations
    out_file = args.outfile

    for file in [hits_file, annots_file]:
        if not os.path.isfile(file):
            die('"{}" is not a file'.format(file))

    lookup = {}
    with open(annots_file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            lookup[row['centroid']] = row

    blast_flds = [
        'qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen',
        'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore'
    ]

    out_fh = open(out_file, 'wt') if out_file else sys.stdout
    out_fh.write('\t'.join(['seq_id', 'pident', 'genus', 'species']) + '\n')

    with open(hits_file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t', fieldnames=blast_flds)
        for row in reader:
            seq_id = row['sseqid']
            if seq_id not in lookup:
                warn('Cannot find seq "{}" in lookup'.format(seq_id))
                continue

            info = lookup[seq_id]
            out_fh.write('\t'.join(
                [row['sseqid'], row['pident'], info['genus'] or 'NA',
                 info['species'] or 'NA']) + '\n')

    out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
