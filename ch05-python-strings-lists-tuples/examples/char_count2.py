#!/usr/bin/env python3
"""Character counter"""

import argparse
import os
import sys
from collections import Counter

# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(description='Argparse Python script')
    parser.add_argument('arg', help='File/string to count', type=str)
    parser.add_argument('-c', '--charsort', help='Sort by character',
                        dest='charsort', action='store_true')
    parser.add_argument('-n', '--numsort', help='Sort by number',
                        dest='numsort', action='store_true')
    parser.add_argument('-r', '--reverse', help='Sort in reverse order',
                        dest='reverse', action='store_true')
    return parser.parse_args()

# --------------------------------------------------
def main():
    """main"""
    args = get_args()
    arg = args.arg
    charsort = args.charsort
    numsort = args.numsort
    revsort = args.reverse

    if charsort and numsort:
        print('Please choose one of --charsort or --numsort')
        sys.exit(1)

    if not charsort and not numsort:
        charsort = True

    text = ''
    if os.path.isfile(arg):
        text = ''.join(open(arg).read().splitlines())
    else:
        text = arg

    count = Counter(text.lower())

    if charsort:
        letters = sorted(count.keys())
        if revsort:
            letters.reverse()

        for letter in letters:
            print('{} {:5}'.format(letter, count[letter]))
    else:
        pairs = sorted([(x[1], x[0]) for x in count.items()])
        if revsort:
            pairs.reverse()

        for n, char in pairs:
            print('{} {:5}'.format(char, n))

# --------------------------------------------------
if __name__ == '__main__':
    main()
