#!/usr/bin/env python3
"""Counts by tax name"""

import csv
import os
import sys
from collections import defaultdict

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} SAMPLE.SUM'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

sum_file = args[0]

basename, ext = os.path.splitext(sum_file)
if not ext == '.sum':
    print('File extention "{}" is not ".sum"'.format(ext))
    sys.exit(1)

tsv_file = basename + '.tsv'
if not os.path.isfile(tsv_file):
    print('Cannot find expected TSV "{}"'.format(tsv_file))
    sys.exit(1)

tax_name = {}
with open(tsv_file) as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    for row in reader:
        tax_name[row['taxID']] = row['name']

counts = defaultdict(int)
with open(sum_file) as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    for row in reader:
        taxID = row['taxID']
        counts[taxID] += 1

print('\t'.join(['count', 'taxID']))
for taxID, count in counts.items():
    name = tax_name.get(taxID) or 'NA'
    print('\t'.join([str(count), name]))
