#!/usr/bin/env python3

import re
from subprocess import getoutput, getstatusoutput

prg = './not_string.py'

def test_usage():
    rv, out = getstatusoutput('{}'.format(prg))
    assert rv > 0
    assert re.match('usage', out, re.IGNORECASE)

def test_runs():
    tests = [
        ('candy', 'not candy'),
        ('x', 'not x'),
        ('not bad', 'not bad'),
        ('bad', 'not bad'),
        ('not', 'not'),
        ('is not', 'not is not'),
        ('no', 'not no')
    ]
    for given, expected in tests:
        out = getoutput('{} "{}"'.format(prg, given))
        assert out == expected
