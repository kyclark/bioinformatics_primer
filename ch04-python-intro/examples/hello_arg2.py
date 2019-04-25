#!/usr/bin/env python3

import sys

args = sys.argv

if len(args) < 2:
    print('Usage:', args[0], 'NAME')
    sys.exit(1)

print('Hello, ' + args[1] + '!')
