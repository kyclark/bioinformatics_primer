#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-05-14
Purpose: Greet the arguments
"""

import os
import sys


# --------------------------------------------------
def main():
    """main"""
    names = sys.argv[1:]
    num = len(names)

    if num < 1:
        print('Usage: {} NAME [NAME...]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    phrase = ''
    if num == 1:
        phrase = names[0]
    elif num == 2:
        phrase = '{} and {}'.format(names[0], names[1])
    else:
        last = names.pop()
        phrase = '{}, and {}'.format(', '.join(names), last)

    print('Hello to the {} of you: {}!'.format(num, phrase))


# --------------------------------------------------
if __name__ == '__main__':
    main()
