#!/usr/bin/env python3

import sys
import os

def main():
    names = sys.argv[1:]

    if len(names) < 1:
        prg = os.path.basename(sys.argv[0])
        print('Usage: {} NAME [NAME2 ...]'.format(prg))
        sys.exit(1)

    for name in names:
        print('Hello, ' + name + '!')


if __name__ == '__main__':
    main()
