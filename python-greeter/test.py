#!/usr/bin/env python3
"""tests for hello.py"""

from subprocess import getstatusoutput
import os

prg = './hello.py'


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


# --------------------------------------------------
def test_02():
    """runs hello"""

    rv, out = getstatusoutput('{} {}'.format(prg, ' Mike Carol'))
    assert rv == 0
    assert out.rstrip() == 'Hello to the 2 of you: Mike and Carol!'


# --------------------------------------------------
def test_03():
    """runs hello"""

    names = ' Greg Peter Bobby Marcia Jane Cindy'
    rv, out = getstatusoutput('{} {}'.format(prg, names))

    assert rv == 0
    expected = ('Hello to the 6 of you: Greg, Peter, Bobby, '
                'Marcia, Jane, and Cindy!')
    assert out.rstrip() == expected
