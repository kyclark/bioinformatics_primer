#!/usr/bin/env python3
"""Count words in common between two files"""

import os
import re
import sys
import string

# --------------------------------------------------
def main():
    files = sys.argv[1:]

    if len(files) != 2:
        msg = 'Usage: {} FILE1 FILE2'
        print(msg.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    for file in files:
        if not os.path.isfile(file):
            print('"{}" is not a file'.format(file))
            sys.exit(1)

    file1, file2 = files[0], files[1]
    words1 = uniq_words(file1)
    words2 = uniq_words(file2)
    common = words1.intersection(words2)
    num_common = len(common)
    msg = 'There {} {} word{} in common between "{}" and "{}."'
    print(msg.format('is' if num_common == 1 else 'are',
                     num_common, 
                     '' if num_common == 1 else 's',
                     os.path.basename(file1), 
                     os.path.basename(file2)))

    for i, word in enumerate(sorted(common)):
        print('{:3}: {}'.format(i + 1, word))

# --------------------------------------------------
def uniq_words(file):
    regex = re.compile('[' + string.punctuation + ']')
    words = set()
    for line in open(file):
        for word in [regex.sub('', w) for w in line.lower().split()]:
            words.add(word)

    return words

# --------------------------------------------------
if __name__ == '__main__':
    main()
