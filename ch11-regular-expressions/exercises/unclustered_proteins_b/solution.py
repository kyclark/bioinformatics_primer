#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-02-20
Purpose: Rock the Casbah
"""

import argparse
import os
import re
import sys
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find unclustered proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    #parser.add_argument(
    #    'positional', metavar='str', help='A positional argument')

    parser.add_argument(
        '-c',
        '--cdhit',
        help='Output file from CD-HIT (clustered proteins)',
        metavar='str',
        type=str,
        required=True)

    parser.add_argument(
        '-p',
        '--proteins',
        help='Proteins FASTA',
        metavar='str',
        type=str,
        required=True)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='str',
        type=str,
        default='unclustered.fa')

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
    proteins_file = args.proteins
    cdhit_file = args.cdhit
    out_file = args.outfile

    for arg_name, file in [('--proteins', proteins_file), ('--cdhit',
                                                           cdhit_file)]:
        if not os.path.isfile(file):
            die('{} "{}" is not a file'.format(arg_name, file))

    clustered = set()
    for line in open(cdhit_file):
        matches = re.search(r'>gi\|(?P<gi_num>\d+)\|', line)
        if matches:
            clustered.add(matches.group('gi_num'))

        # if line.startswith('>'):
        #     continue
        #
        # flds = line.split()
        # prot_id = flds[2].split('|')[1]
        # if prot_id.isdigit():
        #     clustered.add(prot_id)

    out_fh = open(out_file, 'wt')
    num_total = 0
    num_unclustered = 0

    for rec in SeqIO.parse(proteins_file, 'fasta'):
        num_total += 1
        prot_id = re.sub(r'\|.*', '', rec.id)
        if not prot_id in clustered:
            num_unclustered += 1
            SeqIO.write(rec, out_fh, 'fasta')

    print('Wrote {:,d} of {:,d} unclustered proteins to "{}"'.format(
        num_unclustered, num_total, out_file))


# --------------------------------------------------
if __name__ == '__main__':
    main()
