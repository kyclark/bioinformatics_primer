#!/usr/bin/env python3
"""tests for hello.py"""

from subprocess import getstatusoutput
import os

prg = './hello.py'


# --------------------------------------------------
def test_usage():
    """usage"""
    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_01():
    """runs hello"""

    rv, out = getstatusoutput('{}'.format(prg))
    assert rv == 0
    assert out.rstrip() == 'Hello, World.'


# --------------------------------------------------
def test_02():
    """runs hello"""

    rv, out = getstatusoutput('{} -g {}'.format(prg, 'Howdy'))
    assert rv == 0
    assert out.rstrip() == 'Howdy, World.'

# --------------------------------------------------
def test_03():
    """runs hello"""

    rv, out = getstatusoutput('{} -n {}'.format(prg, 'Stranger'))
    assert rv == 0
    assert out.rstrip() == 'Hello, Stranger.'

# --------------------------------------------------
def test_04():
    """runs hello"""

    rv, out = getstatusoutput('{} -g {} -n {}'.format(prg, 'Howdy', 'Stranger'))
    assert rv == 0
    assert out.rstrip() == 'Howdy, Stranger.'

# --------------------------------------------------
def test_05():
    """runs hello"""

    rv, out = getstatusoutput('{} -g {} -n {} -e'.format(prg, 'Howdy', 'Stranger'))
    assert rv == 0
    assert out.rstrip() == 'Howdy, Stranger!'
