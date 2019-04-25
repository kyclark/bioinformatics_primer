#!/usr/bin/env python3
"""print a file in reverse"""

import sys
import os

args = sys.argv[1:]
if len(args) != 1:
    print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

file = args[0]
if not os.path.isfile(file):
    print('"{}" is not a file'.format(file))
    sys.exit(1)

lines = open(file).readlines()

for line in reversed(lines):
    print(line, end='')
