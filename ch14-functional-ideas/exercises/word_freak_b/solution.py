#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@email.arizona.edu>
Date   : 2019-02-18
Purpose: Word Frequency
"""

import argparse
import re
import sys
from collections import defaultdict, Counter


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Print word frequencies',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'file',
        metavar='FILE',
        help='File input(s)',
        nargs='+',
        type=argparse.FileType('r', encoding='UTF-8'))

    parser.add_argument(
        '-s',
        '--sort',
        help='Sort by word or frequency',
        metavar='str',
        type=str,
        choices=['word', 'frequency'],
        default='word')

    parser.add_argument(
        '-m',
        '--min',
        help='Minimum count',
        metavar='int',
        type=int,
        default=0)

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    # Method 1
    # words = defaultdict(int)
    # for fh in args.file:
    #     for line in fh:
    #         for word in line.split():
    #             word = re.sub('[^a-zA-Z0-9]', '', word)
    #             if word:
    #                 words[word.lower()] += 1

    # Method 2
    def clean(word): return re.sub('[^a-zA-Z0-9]', '', word)
    words = Counter()
    for file in args.file:
        words += Counter(map(clean, file.read().lower().split()))
    words.pop('') # remove empty string

    # Remove low-count words
    words = dict(filter(lambda t: t[1] >= args.min, words.items()))

    fmt = '{:20} {}'
    if args.sort == 'word':
        for word, freq in sorted(words.items()):
            print(fmt.format(word, freq))
    else:
        #for freq, word in sorted([(t[1], t[0]) for t in words.items()]):

        #for freq, word in sorted(map(lambda t: (t[1], t[0]), words.items())):

        #for freq, word in sorted(map(lambda t: tuple(reversed(t)), words.items())):

        for freq, word in sorted([(f, w) for w, f in words.items()]):
            print(fmt.format(word, freq))


# --------------------------------------------------
if __name__ == '__main__':
    main()
