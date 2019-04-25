#!/usr/bin/env python3
"""count the vowels in a word"""

import sys
import os

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} STRING'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

word = args[0]

count = 0
for letter in word.lower():
    if letter in 'aeiou':
        count += 1

#for vowel in "aeiou":
#    count += word.lower().count(vowel)

#count = sum([word.count(v) for v in "aeiou"])

#count = sum(map(word.count, "aeiou"))

print('There {} {} vowel{} in "{}."'.format(
    'are' if count > 1 or count == 0 else 'is',
    count,
    '' if count == 1 else 's',
    word))
