#!/usr/bin/env python3

import sys
import os

def main():
    names = sys.argv[1:]

    if len(names) < 1:
        script = os.path.basename(sys.argv[0])
        print('Usage: {} NAME [NAME2 ...]'.format(script))
        sys.exit(1)

    print('Hello, {}!'.format(', '.join(names)))

if __name__ == '__main__':
    main()
