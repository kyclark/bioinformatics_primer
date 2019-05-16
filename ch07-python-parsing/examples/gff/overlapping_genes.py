#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-05-16
Purpose: Find overlapping genes in GFF file
"""

import argparse
import csv
import re
import roman
import sys
from urllib.parse import unquote
from collections import defaultdict
from itertools import chain, product


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find overlapping genes in GFF file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file', metavar='str', help='Input file')

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
def make_num(s):
    """String -> Int"""

    if s and s.isdigit():
        return int(s)
    else:
        return 0


# --------------------------------------------------
def roman_sort(chrs, skip=[]):
    """Sort chromosome names by Roman numeral values"""

    # Build a list of tuple with integer value and chr/Roman
    # e.g., [(1, 'chrI'), (5, 'chrV')]
    # if the chr should be skipped, assign the value -1
    ret = []
    for chr_name in chrs:
        num = -1
        if chr_name not in skip:
            match = re.match('chr(.+)', chr_name)
            if match:
                num = roman.fromRoman(match.group(1))
        ret.append((num, chr_name))

    # Sort the tuple/list, then take only
    # the 2nd member (chr name) of the tuple
    return list(map(lambda t: t[1], sorted(ret)))


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    flds = ('sequence source feature start end score '
            'strand frame attributes').split()

    # dictionaries for the forward/reverse genes on each chromosome
    forward = defaultdict(list)
    reverse = defaultdict(list)

    with open(args.file) as fh:
        # Remove comment lines in the GFF
        src = filter(lambda row: not row.startswith('#'), fh)
        reader = csv.DictReader(src, fieldnames=flds, delimiter='\t')

        for row in reader:
            if row['feature'] != 'gene': continue

            # Attributes look like "key1=val1;key2=val2"
            # Values may be URI encoded, so use "unquote" to fix
            attr = dict(
                map(
                    lambda x: (x[0], unquote(x[1])),
                    map(lambda s: s.split('='),
                        row['attributes'].split(';'))))

            gene_name = attr.get('Name', 'NA')
            chr_name = row['sequence']
            d = forward if row['strand'] == '+' else reverse
            d[chr_name].append(
                (gene_name, make_num(row['start']), make_num(row['end'])))

    chrs = roman_sort(set(chain(forward.keys(), reverse.keys())), skip='chrmt')
    longest = max(map(len, chrs))
    fmt = '{:' + str(longest) + 's}: {} [{}..{}] (+) => {} [{}..{}] (-)'

    for chr_name in chrs:
        combos = product(forward[chr_name], reverse[chr_name])
        for f, r in combos:
            if range(max(f[1], r[1]), min(f[2], r[2]) + 1):
                print(fmt.format(chr_name, *f, *r))


# --------------------------------------------------
if __name__ == '__main__':
    main()
