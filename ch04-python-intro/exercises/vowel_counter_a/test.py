#!/usr/bin/env python3
"""tests for vowel_counter.py"""

from subprocess import getstatusoutput, getoutput
import os.path
import re

prg = './vowel_counter.py'


def test_usage_counter():
    """usage"""
    (retval, out) = getstatusoutput(prg)
    assert retval > 0
    assert re.match("usage", out, re.IGNORECASE)


def test_counter():
    """runs counter"""
    out1 = getoutput(prg + ' if')
    assert out1.rstrip() == 'There is 1 vowel in "if."'

    out2 = getoutput(prg + ' foo')
    assert out2.rstrip() == 'There are 2 vowels in "foo."'

    out3 = getoutput(prg + ' covfefe')
    assert out3.rstrip() == 'There are 3 vowels in "covfefe."'

    out4 = getoutput(prg + ' YYZ')
    assert out4.rstrip() == 'There are 0 vowels in "YYZ."'

    out5 = getoutput(prg + ' HELLO')
    assert out5.rstrip() == 'There are 2 vowels in "HELLO."'
