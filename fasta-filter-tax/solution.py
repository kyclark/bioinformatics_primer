#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-05-22
Purpose: Filter FASTA by taxons
"""

import argparse
import logging
import signal
import os
import re
import sys
from dire import die, warn
from Bio import Entrez, SeqIO


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Filter FASTA by taxons',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file', metavar='str', help='Input file')

    parser.add_argument('-t',
                        '--taxa',
                        help='Taxa ids/file',
                        metavar='str',
                        type=str,
                        required=True)

    parser.add_argument('-e',
                        '--email',
                        help='Email address for Entrez query',
                        metavar='str',
                        type=str,
                        default='kyclark@email.arizona.edu')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='str',
                        type=str,
                        default='seqs.fa')

    parser.add_argument('-d', '--debug', help='Debug', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def get_tax_names(taxa):
    """Get tax names from ids or string"""

    logging.debug('Checking tax inputs')

    def splitter(s):
        return re.split('\s*,\s*', s)

    tax_ids = []
    if os.path.isfile(taxa):
        for line in open(taxa):
            tax_ids.extend(splitter(line.rstrip()))
    else:
        tax_ids = splitter(taxa)

    tax_names = []
    for tax in tax_ids:
        logging.debug('Tax {}'.format(tax))

        if tax.isdigit():
            handle = Entrez.efetch(db='taxonomy', id=tax)
            results = Entrez.read(handle)
            if results:
                name = results[0].get('ScientificName')
                if name:
                    tax_names.append(name)
        else:
            tax_names.append(tax)

    return set(tax_names)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.file
    out_file = args.outfile
    Entrez.email = args.email

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    ok_taxa = get_tax_names(args.taxa) or die('No usable taxa')
    logging.debug('OK tax = {}'.format(ok_taxa))

    logging.debug('Writing to "{}"'.format(out_file))
    out_fh = open(out_file, 'wt')
    num_checked, num_taken = 0, 0

    for rec in SeqIO.parse(args.file, 'fasta'):
        num_checked += 1
        print('{:4}: {}'.format(num_checked, rec.id))

        handle = Entrez.efetch(db='nucleotide',
                               id=rec.id,
                               rettype='gb',
                               retmode='text')

        for record in SeqIO.parse(handle, 'genbank'):
            tax = set(record.annotations.get('taxonomy'))
            tax_hit = ok_taxa.intersection(tax)
            if tax_hit:
                logging.debug('Taking {} ({})'.format(rec.id, tax_hit))
                num_taken += 1
                SeqIO.write(record, 'fasta', out_fh)

    print('Done, checked {}, wrote {} to "{}"'.format(num_checked, num_taken,
                                                      out_file))


# --------------------------------------------------
if __name__ == '__main__':
    main()
