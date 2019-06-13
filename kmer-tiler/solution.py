#!/usr/bin/env python3

import os
import sys

args = sys.argv[1:]

if not 1 <= len(args) <= 2:
    print('Usage: {} WORD [SIZE]'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

word = args[0]
size = int(args[1]) if len(args) == 2 and args[1].isdigit() else 3
nkmer = len(word) - size + 1
verb = 'is' if nkmer == 1 else 'are'
plural = '' if nkmer == 1 else 's'

print('There {} {} {}-mer{} in "{}."'.format(verb, nkmer if nkmer > 0 else 0, size, plural, word))

if nkmer > 0:
    print(word)
    for i in range(nkmer):
        print(' ' * i + word[i:i+size])
