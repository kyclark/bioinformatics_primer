#!/usr/bin/env python3
"""Compress text/DNA by marking repeated letters"""

import os
import sys


def main():
    """main"""
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    # If the argument is a file, the text should be the file contents
    arg = args[0]
    text = ''
    if os.path.isfile(arg):
        text = ''.join(open(arg).read().split())
    else:
        text = arg.strip()

    # Make sure we have something
    if len(text) == 0:
        print('No usable text')
        sys.exit(1)

    counts = []
    count = 0
    prev = None
    for letter in text:
        # We are at the start
        if prev is None:
            prev = letter
            count = 1
        # This letter is the same as before
        elif letter == prev:
            count += 1
        # This is a new letter, so record the count
        # of the previous letter and reset the counter
        else:
            counts.append((prev, count))
            count = 1
            prev = letter

    # get the last letter after we fell out of the loop
    counts.append((prev, count))

    for letter, num in counts:
        print('{}{}'.format(letter, '' if num == 1 else num), end='')

    print()


if __name__ == '__main__':
    main()
