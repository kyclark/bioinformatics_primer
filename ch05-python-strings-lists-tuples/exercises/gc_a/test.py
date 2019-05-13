#!/usr/bin/env python3
"""tests for gc.py"""

import os.path
import random
import string
import re
from subprocess import getstatusoutput, getoutput
from random import shuffle
from shutil import rmtree

prg = './gc.py'
sample1 = 'samples/sample1.txt'
sample2 = 'samples/sample2.txt'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(prg, flag))
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_input():
    """fails on bad input"""

    rv, out = getstatusoutput('{} foo'.format(prg))
    assert rv == 1
    assert out == '"foo" is not a file'


# --------------------------------------------------
def test_good_input1():
    """works on good input"""

    rv, out = getstatusoutput('{} {}'.format(prg, sample1))
    expected = """  1:   9%
  2:  19%
  3:  19%
  4:  22%
  5:  32%
  6:  21%""".rstrip()
    assert rv == 0
    assert out == expected

# --------------------------------------------------
def test_good_input2():
    """works on good input"""

    rv, out = getstatusoutput('{} {}'.format(prg, sample2))
    expected = """  1:  29%
  2:  34%
  3:  26%
  4:  34%
  5:  29%
  6:  29%
  7:  37%
  8:  18%
  9:  34%""".rstrip()
    assert rv == 0
    assert out == expected
