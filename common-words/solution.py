#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-04-18
Purpose: Find common words
"""

import argparse
import io
import logging
import re
import sys
from itertools import product
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'file',
        metavar='FILE',
        help='Input files',
        nargs=2,
        type=argparse.FileType('r', encoding='UTF-8'))

    parser.add_argument(
        '-m',
        '--min_len',
        help='Minimum length of words',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-n',
        '--hamming_distance',
        help='Allowed Hamming distance',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-l',
        '--logfile',
        help='Logfile name',
        metavar='str',
        type=str,
        default='.log')

    parser.add_argument('-d', '--debug', help='Debug', action='store_true')

    parser.add_argument(
        '-t', '--table', help='Table output', action='store_true')

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
def dist(s1, s2):
    """Given two strings, return the Hamming distance (int)"""

    d = abs(len(s1) - len(s2)) + sum(
        map(lambda p: 0 if p[0] == p[1] else 1, zip(s1, s2)))

    logging.debug('s1 = {}, s2 = {}, d = {}'.format(s1, s2, d))

    return d


# --------------------------------------------------
def test_dist():
    """dist ok"""

    tests = [('foo', 'boo', 1), ('foo', 'faa', 2), ('foo', 'foobar', 3),
             ('TAGGGCAATCATCCGAG', 'ACCGTCAGTAATGCTAC',
              9), ('TAGGGCAATCATCCGG', 'ACCGTCAGTAATGCTAC', 10)]

    for s1, s2, n in tests:
        d = dist(s1, s2)
        assert d == n


# --------------------------------------------------
def uniq_words(file, min_len):
    """
    Given a file or filehandle, return a set of the unique words
    over a given minimum length
    """
    words = set()
    fh = open(file) if type(file) == str else file

    for line in fh:
        for word in line.lower().split():
            word = re.sub('[^a-zA-Z0-9]', '', word)
            if len(word) >= min_len:
                words.add(word)

    return words


# --------------------------------------------------
def test_uniq_words():
    """Test uniq_words"""

    s1 = '?foo, "bar", FOO: $fa,'
    s2 = '%Apple.; -Pear. ;bANAna!!!'

    assert uniq_words(io.StringIO(s1), 0) == set(['foo', 'bar', 'fa'])

    assert uniq_words(io.StringIO(s1), 3) == set(['foo', 'bar'])

    assert uniq_words(io.StringIO(s2), 0) == set(['apple', 'pear', 'banana'])

    assert uniq_words(io.StringIO(s2), 4) == set(['apple', 'pear', 'banana'])

    assert uniq_words(io.StringIO(s2), 5) == set(['apple', 'banana'])


# --------------------------------------------------
def common(words1, words2, distance):
    """Find the common words"""

    words = []
    for w1, w2 in sorted(product(words1, words2)):
        hamm = dist(w1, w2)
        if hamm <= distance:
            words.append((w1, w2, hamm))

    return words


# --------------------------------------------------
def test_common():
    w1 = ['foo', 'bar', 'quux']
    w2 = ['bar', 'baz', 'faa']

    assert common(w1, w2, 0) == [('bar', 'bar', 0)]

    assert common(w1, w2, 1) == [('bar', 'bar', 0), ('bar', 'baz', 1)]

    assert common(w1, w2, 2) == [('bar', 'bar', 0), ('bar', 'baz', 1),
                                 ('bar', 'faa', 2), ('foo', 'faa', 2)]


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    fh1, fh2 = args.file
    distance = args.hamming_distance

    if distance < 0:
        die('--distance "{}" must be > 0'.format(distance))

    logging.basicConfig(
        filename=args.logfile,
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    words1 = uniq_words(fh1, args.min_len)
    words2 = uniq_words(fh2, args.min_len)
    common_words = common(words1, words2, distance)

    logging.debug('Found {} words in common'.format(len(common_words)))

    if not common_words:
        print('No words in common.')
    else:
        common_words.insert(0, ('word1', 'word2', 'distance'))
        if args.table:
            print(tabulate(common_words, headers='firstrow', tablefmt='psql'))
        else:
            for w1, w2, hamm in common_words:
                print('\t'.join([w1, w2, str(hamm)]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
