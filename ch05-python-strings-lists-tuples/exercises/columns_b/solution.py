#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-05-03
Purpose: Columnar output
"""

import os
import sys


# --------------------------------------------------
def main():
    words = sys.argv[1:]

    if len(words) < 1:
        print('Usage: {} WORD [WORD...]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    word_lengths = map(len, words)
    longest_word = max(word_lengths)
    longest_num = len(str(longest_word))

    if longest_word < 4:
        longest_word = 4

    if longest_num < 3:
        longest_num = 3

    fmt = '{:' + str(longest_word + 1) + '}{:>' + str(longest_num + 1) + '}'

    print(fmt.format('word', 'len'))
    print(fmt.format('-' * longest_word, '-' * longest_num))

    for word in words:
        print(fmt.format(word, len(word)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
