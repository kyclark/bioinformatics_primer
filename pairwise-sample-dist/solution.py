#!/usr/bin/env python3
"""docstring"""

import argparse
import csv
import re
import os
import sys
from itertools import combinations
from geopy.distance import vincenty

# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(description='Argparse Python script')
    parser.add_argument('-d', '--data', help='Tab-delimited samples file',
                        metavar='str', type=str, default='samples.tab')
    parser.add_argument('-s', '--sample_ids', help='Sample IDs (comma-sep)',
                        metavar='str', type=str, default='')
    return parser.parse_args()

# --------------------------------------------------
def main():
    """main"""
    args = get_args()
    infile = args.data
    sample_ids = re.split(r'\s*,\s*', args.sample_ids) if args.sample_ids else []
    print(sample_ids)
    
    if not os.path.isfile(infile):
        print('"{}" is not a file'.format(infile))
        sys.exit(1)

    records = []
    with open(infile) as fh:
        reader = csv.DictReader(fh, delimiter='\t')
        for rec in reader:
            records.append(rec)
    print('# rec = {}'.format(len(records)))

    combos = combinations(range(len(records)), 2)
    for i, j in combos:
        s1, s2 = records[i], records[j]
        dist = vincenty((s1['latitude'], s1['longitude']), 
                        (s2['latitude'], s2['longitude']))
        lat1, long1 = s1['latitude'], s1['longitude']
        print('{} -> {} = {}'.format(s1['sample_id'], s2['sample_id'], dist))
        print(s1)
        print(s2)



# --------------------------------------------------
if __name__ == '__main__':
    main()
