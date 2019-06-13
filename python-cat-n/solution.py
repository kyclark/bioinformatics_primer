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

    file = args[0]

    if not os.path.isfile(file):
        print('{} is not a file'.format(file))
        sys.exit(1)

    for i, line in enumerate(open(file), start=1):
        print('{:5}: {}'.format(i, line), end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
