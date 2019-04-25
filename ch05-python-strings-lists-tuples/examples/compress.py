#!/usr/bin/env python3
"""Compress text/DNA by marking repeated letters"""

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

arg = args[0]
text = ''
if os.path.isfile(arg):
    text = ''.join(open(arg).read().split())
else:
    text = arg.strip()

if len(text) == 0:
    print('No usable text')
    sys.exit(1)

counts = []
count = 0
prev = None
for letter in text:
    if prev is None:
        prev = letter
        count = 1
    elif letter == prev:
        count += 1
        prev = letter
    else:
        counts.append((prev, count))
        count = 1
        prev = letter

# get the last letter after we fell out of the loop
counts.append((prev, count))

for letter, count in counts:
    print('{}{}'.format(letter, '' if count == 1 else count), end='')

print('')
