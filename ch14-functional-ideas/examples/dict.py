#!/usr/bin/env python3
"""docstring"""

import os
import sys
from collections import defaultdict

args = sys.argv[1:]

if len(args) == 1:
    file = args[0]
else:
    file = '/usr/share/dict/words'

if not os.path.isfile(file):
    print('"{}" is not a file'.format(file))
    sys.exit(1)


def onlychars(word):
    return ''.join(filter(str.isalpha, word))


file = '/usr/share/dict/words'
num2word = defaultdict(list)
for line in map(str.rstrip, open(file)):
    for word in map(onlychars, line.split()):
        num = sum(map(ord, word))
        num2word[num].append(word)

print(num2word)

count_per_n = []
for n, wordlist in num2word.items():
    count_per_n.append((len(wordlist), n))

top10 = list(reversed(sorted(count_per_n)))[:10]
for (num_of_words, n) in top10:
    print('"{}" = {}'.format(n, ', '.join(num2word[n])))
