#!/usr/bin/env python3

import sys

args = sys.argv[1:]
top = args[0] if args else 100
for i in range(1, int(top) + 1):
    if (i % 3 == 0) and (i % 5 == 0):
        print('Fizz Buzz')
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

print()
