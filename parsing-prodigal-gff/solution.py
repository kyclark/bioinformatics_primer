#!/usr/bin/env python3
"""Parse the GFF output of Prodigal"""

import argparse
import csv
import os
import re
import sys


# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(
        description='Prodigal GFF parser',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='Prodigal GFF file')

    parser.add_argument('-t',
                        '--type',
                        help='Feature type',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='str',
                        type=str,
                        default=None)

    parser.add_argument('-m',
                        '--min',
                        help='Min score',
                        metavar='float',
                        type=float,
                        default=0.)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    fh = args.file
    min_score = args.min
    feature_type = args.type
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    flds = 'seqid source type start end score strand frame attributes'.split()

    # Method 1: Write a generator
    # def src():
    #     for line in fh:
    #         if line[0] != '#':
    #             yield line
    # reader = csv.DictReader(src(), fieldnames=flds, delimiter='\t')

    # Method 2: Use a `filter`
    reader = csv.DictReader(filter(lambda line: line[0] != '#', fh),
                            fieldnames=flds,
                            delimiter='\t')

    print('\t'.join(['seqid', 'type', 'score']), file=out_fh)

    kv = re.compile('([^=]+)=([^=]+)')
    for rec in reader:
        if feature_type and rec['type'] != feature_type:
            continue

        attrs = {}
        for match in map(kv.match, rec['attributes'].split(';')):
            if match:
                key, value = match.groups()
                attrs[key] = value

        if 'score' in attrs:
            try:
                score = float(attrs['score'])
                if score >= min_score:
                    print('\t'.join(
                        map(str, [rec['seqid'], rec['type'], score])),
                          file=out_fh)
            except:
                pass


# --------------------------------------------------
if __name__ == '__main__':
    main()
