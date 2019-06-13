#!/usr/bin/env python3
"""tests for head.py"""

from subprocess import getstatusoutput, getoutput
import os.path
import re

prg = "./head.py"
sonnet = 'files/sonnet-29.txt'
issa = 'files/issa.txt'


def test_usage():
    """usage"""
    (retval, out) = getstatusoutput(prg)
    assert retval > 0
    assert re.match("usage", out, re.IGNORECASE)


def test_bad_number():
    """bad number"""
    (rv1, out1) = getstatusoutput('{} {} {}'.format(prg, sonnet, '-1'))
    assert rv1 > 0
    assert out1 == 'lines (-1) must be a positive number'

    (rv2, out2) = getstatusoutput('{} {} {}'.format(prg, issa, '0'))
    assert out2 == 'lines (0) must be a positive number'


def test_bad_input():
    """bad input"""
    (retval, out) = getstatusoutput('{} {}'.format(prg, 'foo'))
    assert retval > 0
    assert out == 'foo is not a file'


def test_runs():
    """runs ok"""
    for file in [sonnet, issa]:
        for num in [1, 3, 5, 9]:
            out = getoutput("{} {} {}".format(prg, file, num))
            out_lines = out.split('\n')
            assert len(out_lines) == num
