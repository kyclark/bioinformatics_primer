#!/usr/bin/env python3
"""tests for column.py"""

import os
import re
from subprocess import getstatusoutput

prg = "./column.py"


# --------------------------------------------------
def test_usage():
    """usage"""
    (retval, out) = getstatusoutput(prg)
    assert retval > 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_runs():
    """runs ok"""
    for i in range(1, 6):
        in_file = os.path.join('out', str(i) + '.in')
        out_file = os.path.join('out', str(i) + '.out')

        if os.path.isfile(in_file) and os.path.isfile(out_file):
            words = open(in_file).read()
            expected = open(out_file).read()
            rv, out = getstatusoutput("{} {}".format(prg, words))
            assert rv == 0
            assert out.rstrip() == expected.rstrip()
