#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-04-10
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 2:
        print('Usage: {} DAY VACATION'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    day, on_vacation = map(str.lower, args)

    weekend = args[0].lower() in ['saturday', 'sunday']
    vacation = args[1].lower().startswith('y')

    print('Yes' if (vacation or weekend) else 'No')


# --------------------------------------------------
main()
