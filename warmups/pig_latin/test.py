#!/usr/bin/env python3

import re
from subprocess import getoutput, getstatusoutput

prg = './pig.py'

def test_usage():
    rv, out = getstatusoutput('{}'.format(prg))
    assert rv > 0
    assert re.match('usage', out, re.IGNORECASE)

def test_runs():
    tests = [
        ('mouse', 'ouse-may'),
        ('apple', 'apple-ay'),
        ('chair', 'air-chay'),
        ('street', 'eet-stray'),
        ('BOOK', 'OOK-Bay'),
        ('Creek', 'eek-Cray'),
    ]

    for given, expected in tests:
        out = getoutput('{} "{}"'.format(prg, given))
        assert expected == out
