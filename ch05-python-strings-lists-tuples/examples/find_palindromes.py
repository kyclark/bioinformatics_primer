#!/usr/bin/env python3
"""Report if the given word is a palindrome"""

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

for line in open(file):
    for word in line.lower().split():
        if len(word) > 2:
            rev = ''.join(reversed(word))
            if rev == word:
                print(word)
