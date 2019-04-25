#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-01-30
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} NUM'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    num = int(args[0])

    #if num < 2 or num > 9:
    if not 2 <= num <= 9:
        print("NUM ({}) must be between 1 and 9".format(num))
        sys.exit(1)

    for i in range(1, (num ** 2) + 1):
        print('{:3}'.format(i), end='')
        if i % num == 0:
            print()


# --------------------------------------------------
main()
