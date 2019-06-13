#!/usr/bin/env python

import os
import argparse
import re
import sys
import gzip
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    parser = argparse.ArgumentParser(description='Filter FASTA with Centrifuge')
    parser.add_argument('-f', '--fasta', help='fasta file',
            type=str, metavar='FILE', required=True)
    parser.add_argument('-s', '--summary', help='Centrifuge summary file',
            type=str, metavar='FILE', required=True)
    parser.add_argument('-e', '--exclude', metavar='IDS_NAMES', required=True,
            help='Comma-separated list of taxIDs/names to exclude')
    parser.add_argument('-o', '--out_dir', help='Output directory',
            type=str, metavar='DIR', default='filtered')
    parser.add_argument('-x', '--exclude_dir', metavar='DIR', required=True,
            help='File name to write excluded')
    return parser.parse_args()

# --------------------------------------------------
def read_split(s):
    return s.rstrip("\n").split("\t")

# --------------------------------------------------
def get_excluded(x, sum_file):
    if not sum_file.endswith('.sum'):
        print('sum_file ({}) does not end with ".sum"'.format(sum_file))
        sys.exit

    tsv_file = re.sub(r'\.sum$', '.tsv', sum_file)
    if not os.path.exists(tsv_file):
        print('Cannot find TSV file ({})'.format(tsv_file))
        sys.exit

    name_to_id = dict()
    with open(tsv_file) as tsv:
        hdr = read_split(tsv.readline())
        for line in tsv:
            rec = dict(zip(hdr, read_split(line)))
            name_to_id[ rec['name'].lower() ] = rec['taxID']

    exclude = set()
    for arg in re.split('\s*,\s*', x.lower()):
        if str.isdigit(arg):
            exclude.add(arg)
        else:
            if arg in name_to_id:
                exclude.add(name_to_id[arg])
            else:
                print('Cannot find name "{}" in {}'.format(arg, tsv_file))
                sys.exit

    return exclude

# --------------------------------------------------
def main():
    args    = get_args()
    exclude = get_excluded(args.exclude, args.summary)
    out_dir = args.out_dir

    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)

    tax_id = dict()
    with open(args.summary, 'r') as sum_fh:
        sum_hdr = read_split(sum_fh.readline())
        for line in sum_fh:
            #info = dict(zip(sum_hdr, read_split(line)))
            #tax_id[ info['readID'] ] = info['taxID']
            dat = read_split(line)
            tax_id[ dat[0] ] = dat[2]

    took       = 0
    skipped    = 0
    basename   = os.path.basename(args.fasta)
    out_file   = os.path.join(out_dir, basename)
    exclude_fh = open(os.path.join(args.exclude_dir, basename), 'wt') \
                 if args.exclude_dir else None

    with open(out_file, 'w') as out_fh:
        for seq in SeqIO.parse(args.fasta, "fasta"):
            tax = tax_id[ seq.id ] if seq.id in tax_id else '0'
            if tax in exclude:
                skipped += 1
                if not exclude_fh is None:
                    SeqIO.write(seq, exclude_fh, "fasta")
            else:
                took += 1
                SeqIO.write(seq, out_fh, "fasta")

    print("Done, took {}, skipped {}, see output {}".format(
        took, skipped, out_file))

# --------------------------------------------------
if __name__ == '__main__':
    main()
