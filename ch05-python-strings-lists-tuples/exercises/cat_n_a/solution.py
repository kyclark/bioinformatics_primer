#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-02-04
Purpose: Emulate cat-n
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    filename = args[0]

    if not os.path.isfile(filename):
        print('{} is not a file'.format(filename))
        sys.exit(1)

    for i, line in enumerate(open(filename)):
        print('{:5}: {}'.format(i+1, line), end='')


# --------------------------------------------------
main()
