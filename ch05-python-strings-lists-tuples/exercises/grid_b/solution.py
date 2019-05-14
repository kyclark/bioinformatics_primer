#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-01-30
Purpose: Create an NxN grid
"""

import os
import sys


# --------------------------------------------------
def main():
    """main"""
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} NUM'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    num = int(args[0])

    if not 2 <= num <= 9:
        print("NUM ({}) must be between 1 and 9".format(num))
        sys.exit(1)

    for i in range(1, (num ** 2) + 1):
        print('{:3}'.format(i), end='')
        if i % num == 0:
            print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
