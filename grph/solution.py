#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@email.arizona.edu>
Date   : 2019-04-08
Purpose: Graph through sequences
"""

import argparse
import logging
import os
import sys
from collections import defaultdict
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Graph through sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file', metavar='str', help='FASTA file')

    parser.add_argument(
        '-k',
        '--overlap',
        help='K size of overlap',
        metavar='int',
        type=int,
        default=3)

    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true')

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
def find_kmers(seq, k):
    """Find k-mers in string"""
    seq = str(seq)
    n = len(seq) - k + 1
    return list(map(lambda i: seq[i:i + k], range(n)))


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    file = args.file
    k = args.overlap

    if not os.path.isfile(file):
        die('"{}" is not a file'.format(file))

    if k < 1:
        die('-k "{}" must be a positive integer'.format(k))

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL
    )

    beginning = defaultdict(list)
    end = defaultdict(list)
    for rec in SeqIO.parse(file, 'fasta'):
        kmers = find_kmers(rec.seq, k)
        beginning[kmers[0]].append(rec.id)
        end[kmers[-1]].append(rec.id)

    logging.debug('beginnings = {}'.format(beginning))
    logging.debug('ends = {}'.format(end))

    for kmer in end:
        if kmer in beginning:
            for seq_id in end[kmer]:
                for other in beginning[kmer]:
                    if seq_id != other:
                        print(seq_id, other)


# --------------------------------------------------
if __name__ == '__main__':
    main()
