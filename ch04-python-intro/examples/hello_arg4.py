#!/usr/bin/env python3

import sys
import os

def main():
    args = sys.argv[1:]

    if len(args) != 1:
        script = os.path.basename(sys.argv[0])
        print('Usage: {} NAME'.format(script))
        sys.exit(1)

    name = args[0]
    print('Hello, {}!'.format(name))


if __name__ == '__main__':
    main()
