#!/usr/bin/env python3
"""Count words/frequencies in two files"""

import os
import re
import sys
import string
from collections import defaultdict

# --------------------------------------------------
def word_counts(file):
    """Return a dictionary of words/counts"""
    words = defaultdict(int)
    regex = re.compile('[' + string.punctuation + ']')
    for line in open(file):
        for word in [regex.sub('', w) for w in line.lower().split()]:
            words[word] += 1

    return words

# --------------------------------------------------
def main():
    """Start here"""
    args = sys.argv[1:]

    if len(args) != 2:
        msg = 'Usage: {} FILE1 FILE2'
        print(msg.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    for file in args[0:2]:
        if not os.path.isfile(file):
            print('"{}" is not a file'.format(file))
            sys.exit(1)

    file1 = args[0]
    file2 = args[1]
    words1 = word_counts(file1)
    words2 = word_counts(file2)
    common = set(words1.keys()).intersection(set(words2.keys()))
    num_common = len(common)
    verb = 'is' if num_common == 1 else 'are'
    plural = '' if num_common == 1 else 's'
    msg = 'There {} {} word{} in common between "{}" ({}) and "{}" ({}).'
    tot1 = sum(words1.values())
    tot2 = sum(words2.values())
    print(msg.format(verb, num_common, plural, file1, tot1, file2, tot2))

    if num_common > 0:
        fmt = '{:>3} {:20} {:>5} {:>5}'
        print(fmt.format('#', 'word', '1', '2'))
        print('-' * 36)
        shared1, shared2 = 0, 0
        for i, word in enumerate(sorted(common)):
            c1 = words1[word]
            c2 = words2[word]
            shared1 += c1
            shared2 += c2
            print(fmt.format(i + 1, word, c1, c2))

        print(fmt.format('', '-----', '--', '--'))
        print(fmt.format('', 'total', shared1, shared2))
        print(fmt.format('', 'pct',
                         int(shared1/tot1 * 100), int(shared2/tot2 * 100)))

# --------------------------------------------------
if __name__ == '__main__':
    main()
