#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-02-04
Purpose: Emulate head
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) < 1 or len(args) > 2:
        print('Usage: {} FILE [NUM_LINES]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    filename = args[0]
    num_lines = int(args[1]) if len(args) == 2 else 3

    if num_lines < 1:
        print('lines ({}) must be a positive number'.format(num_lines))
        sys.exit(1)

    if not os.path.isfile(filename):
        print('{} is not a file'.format(filename))
        sys.exit(1)

    for i, line in enumerate(open(filename)):
        print(line, end='')
        if i + 1 == num_lines:
            break


# --------------------------------------------------
main()
