#!/usr/bin/env python3
"""hello with args/main"""

import sys
import os

def main():
    """main"""
    args = sys.argv

    if len(args) != 2:
        script = os.path.basename(args[0])
        print('Usage: {} NAME'.format(script))
        sys.exit(1)

    name = args[1]
    print('Hello, {}!'.format(name))


main()