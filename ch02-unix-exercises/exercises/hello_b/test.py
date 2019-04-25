#!/usr/bin/env python3
"""tests for hello.sh"""

from subprocess import getstatusoutput, getoutput
import os.path
import re

prg = "./hello.sh"


# --------------------------------------------------
def test_usage():
    """usage"""
    rv, out = getstatusoutput(prg)
    assert rv > 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_hello_too_many():
    rv, out = getstatusoutput('{} {} {} {}'.format(
        prg, 'foo', 'bar', 'baz'))
    assert rv > 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_hello():
    rv1, out1 = getstatusoutput('{} {}'.format(prg, 'Hello'))
    assert rv1 == 0
    assert out1 == 'Hello, Human!'

    rv2, out2 = getstatusoutput('{} "{}" "{}"'.format(
        prg, 'Good Day', 'Kind Sir'))
    assert rv2 == 0
    assert out2 == 'Good Day, Kind Sir!'
