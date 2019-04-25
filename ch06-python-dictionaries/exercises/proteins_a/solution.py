#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-02-07
Purpose: Translate DNA/RNA to proteins
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence', metavar='STR', help='DNA/RNA sequence')

    parser.add_argument(
        '-c',
        '--codons',
        help='A file with codon translations',
        metavar='FILE',
        type=str,
        required=True)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output filename',
        metavar='FILE',
        type=str,
        default='out.txt')

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
    seq = args.sequence.upper()
    codon_file = args.codons
    out_file = args.outfile

    if not os.path.isfile(codon_file):
        die('--codons "{}" is not a file'.format(codon_file))

    out_fh = open(out_file, 'wt')

    codon_table = dict()
    for line in open(codon_file):
        codon, prot = line.upper().rstrip().split()
        codon_table[codon] = prot

    k = 3
    for codon in [seq[i:i+k] for i in range(0, len(seq), k)]:
        out_fh.write(codon_table.get(codon, '-'))

    out_fh.write('\n')
    out_fh.close()
    print('Output written to "{}"'.format(out_file))

# --------------------------------------------------
if __name__ == '__main__':
    main()
