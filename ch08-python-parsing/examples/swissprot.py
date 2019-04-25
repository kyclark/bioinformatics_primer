#!/usr/bin/env python3

import argparse
import sys
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(
        description='Parse Swissprot file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file', metavar='FILE', help='Swissprot file')

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
    file = args.file

    for i, record in enumerate(SeqIO.parse(file, "swiss"), start=1):
        print('{:3}: {}'.format(i, record.id))
        annotations = record.annotations

        for annot_type in ['accessions', 'keywords', 'taxonomy']:
            if annot_type in annotations:
                print('\tANNOT {}:'.format(annot_type))
                val = annotations[annot_type]
                if type(val) is list:
                    for v in val:
                        print('\t\t{}'.format(v))
                else:
                    print('\t\t{}'.format(val))



# --------------------------------------------------
if __name__ == '__main__':
    main()
