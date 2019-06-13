#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@email.arizona.edu>
Date   : 2019-06-11
Purpose: Plot Centrifuge out
"""

import argparse
import csv
import os
import re
import pandas as pd
import matplotlib.pyplot as plt
from dire import die

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Plot Centrifuge out',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dir',
                        metavar='DIR',
                        type=str,
                        help='Centrifuge output directory')

    parser.add_argument('-r',
                        '--rank',
                        help='Tax rank',
                        metavar='str',
                        type=str,
                        choices=['species'],
                        default='species')

    parser.add_argument('-m',
                        '--min',
                        help='Minimum percent abundance',
                        metavar='float',
                        type=float,
                        default=0.)

    parser.add_argument('-M',
                        '--multiplier',
                        help='Multiply abundance',
                        metavar='float',
                        type=float,
                        default=1.)

    parser.add_argument('-x',
                        '--exclude',
                        help='Tax IDs or names to exclude',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-t',
                        '--title',
                        help='Figure title',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='str',
                        type=str,
                        default='bubble.png')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    rank = args.rank
    min_pct = args.min
    exclude = re.split('\s*,\s*', args.exclude.lower())
    cent_dir = args.dir

    if not os.path.isdir(cent_dir):
        die('"{}" is not a directory'.format(cent_dir))

    tsv_files = list(filter(lambda f: f.endswith('.tsv'), os.listdir(cent_dir)))
    if not tsv_files:
        die('Found no ".tsv" files in "{}"'.format(cent_dir))

    assigned = []
    for i, file in enumerate(tsv_files, start=1):
        print('{:3}: {}'.format(i, file))

        with open(os.path.join(cent_dir, file)) as fh:
            reader = csv.DictReader(fh, delimiter='\t')
            for rec in filter(lambda r: r['taxRank'] == rank, reader):
                tax_id = rec['taxID']
                tax_name = rec['name']

                if tax_id in exclude or tax_name.lower() in exclude:
                    continue

                pct = float(rec.get('abundance'))
                if min_pct and pct < min_pct:
                    continue

                sample, _ = os.path.splitext(file)
                assigned.append({
                    'sample': sample,
                    'tax_id': tax_id,
                    'tax_name': tax_name,
                    'pct': pct,
                    'reads': int(rec['numReads'])
                })

    if not assigned:
        die('No data!')

    df = pd.DataFrame(assigned)
    plt.scatter(x=df['sample'],
                y=df['tax_name'],
                s=df['pct'] * args.multiplier,
                alpha=0.5)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=45, ha='right')
    plt.gcf().subplots_adjust(bottom=.4, left=.3)
    plt.ylabel('Organism')
    plt.xlabel('Sample')
    if args.title:
        plt.title(args.title)

    plt.savefig(args.outfile)

    print('Done, see "{}"'.format(args.outfile))


# --------------------------------------------------
if __name__ == '__main__':
    main()
