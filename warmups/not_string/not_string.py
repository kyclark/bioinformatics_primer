#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-04-10
Purpose: Rock the Casbah
"""

import os
import re
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} STRING'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    s = args[0]

    s = s if re.match('not\s*', s) else 'not ' + s

    print(s)


# --------------------------------------------------
main()
