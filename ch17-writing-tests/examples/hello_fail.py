#!/usr/bin/env python3

import os
import sys

def hello(name):
    if type(name) is str:
        return 'Hello, {}!'.format(name)
    else:
        return 'Can only say hello to a string'


def test_hello():
    assert hello('World') == 'Hello, World!'
    assert hello('') == 'Hello, !'
    assert hello('my name is Fred') == 'Hello, my name is Fred!'

    err = 'Can only say hello to a string'
    assert hello(4) == err
    assert hello(None) == err
    assert hello(float) == err
    assert hello(str) == err

def main():
    args = sys.argv[1:]
    if not args:
        print('Usage: {} NAME [NAME...]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    for arg in args:
        if arg.isdigit(): arg = int(arg)

        print(hello(arg))

if __name__ == '__main__':
    main()
