#!/usr/bin/env python3
"""Line counter"""

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

infile = args[0]

if not os.path.isfile(infile):
    print('Arg "{}" is not a file'.format(infile))
    sys.exit(1)

count = 0
for line in open(infile, 'rt'):
    count += 1

print('There are "{}" lines in "{}"'.format(count, infile))
