#!/usr/bin/env python3
"""tests for gap.sh"""

from subprocess import getstatusoutput
import re

prg = "./gap.sh"


# --------------------------------------------------
def test_01():
    rv, out = getstatusoutput(prg)
    assert rv == 0
    assert len(out.split('\n')) >= 142


# --------------------------------------------------
def test_02():
    rv, out = getstatusoutput('{} {}'.format(prg, 'b'))
    assert rv == 0
    assert len(out.split('\n')) == 11


# --------------------------------------------------
def test_03():
    rv, out = getstatusoutput('{} {}'.format(prg, 'q'))
    assert rv == 1
    assert out == 'There are no countries starting with "q"'


# --------------------------------------------------
def test_04():
    rv, out = getstatusoutput('{} "{}"'.format(prg, '[u-z]'))
    assert rv == 0
    assert len(out.split('\n')) == 10
