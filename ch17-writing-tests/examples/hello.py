#!/usr/bin/env python3

import os
import sys

def hello(name):
    return 'Hello, {}!'.format(name)

def test_hello():
    assert hello('World') == 'Hello, World!'
    assert hello('') == 'Hello, !'
    assert hello('my name is Fred') == 'Hello, my name is Fred!'

def main():
    args = sys.argv[1:]
    if not args:
        print('Usage: {} NAME [NAME...]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    for arg in args:
        print(hello(arg))

if __name__ == '__main__':
    main()
