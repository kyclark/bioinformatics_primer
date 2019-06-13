#!/usr/bin/env python3

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} WORD'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

word = args[0]

number = 0
for letter in word:
    ascii_value = ord(letter)
    print('"{}" = "{}"'.format(letter, ascii_value))
    number += ascii_value

print('"{}" = "{}"'.format(word, number))
