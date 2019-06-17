#!/usr/bin/env python3
"""tests for wc.py"""

from subprocess import getstatusoutput
import os

prg = './wc.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    rv, out = getstatusoutput(prg)
    assert rv > 0
    assert out.lower().startswith('usage')


# --------------------------------------------------
def test_01():
    """runs hello"""

    rv, out = getstatusoutput('{} {}'.format(prg, 'Alice'))
    assert rv == 0
    assert out.rstrip() == 'Hello to the 1 of you: Alice!'
