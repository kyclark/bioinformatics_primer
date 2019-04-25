#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-04-01
Purpose: Rock the Casbah
"""

import os
import re
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 2:
        print('Usage: {} PASSWORD ALT'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    password, alt = args

    ok = (password == alt) or (password.upper() == alt) or (
        password.capitalize() == alt) or re.match('.?' + password + '.?', alt)

    print('ok' if ok else 'nah')


# --------------------------------------------------
main()
