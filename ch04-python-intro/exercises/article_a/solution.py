#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-05-01
Purpose: Article selector
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} WORD'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    word = args[0]
    article = 'a'
    for vowel in 'aeiou':
        if word.lower().startswith(vowel):
            article = 'an'
            break

    print(article, word)


# --------------------------------------------------
if __name__ == '__main__':
    main()
