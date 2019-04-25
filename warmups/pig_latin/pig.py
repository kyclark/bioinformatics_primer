#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-04-10
Purpose: Pig Latin
"""

import os
import re
import string
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} ORD-WAY'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    word = args[0]

    consonants = re.sub('[aeiouAEIOU]', '', string.ascii_letters)
    match = re.match('^([' + consonants + ']+)(.+)', word)
    if match:
        print('-'.join([match.group(2), match.group(1) + 'ay']))
    else:
        print(word + '-ay')


# --------------------------------------------------
main()
