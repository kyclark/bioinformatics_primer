#!/usr/bin/env python3

import sys

args = sys.argv[1:]

if len(args) < 1:
    print('Usage:', sys.argv[0], 'NAME')
    sys.exit(1)

name = args[0]
print('Hello, ' + name + '!')
