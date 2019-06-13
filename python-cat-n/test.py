#!/usr/bin/env python3
"""tests for cat-n.py"""

from subprocess import getstatusoutput, getoutput
import os
import re

prg = "./cat_n.py"
sonnet = 'files/sonnet-29.txt'
issa = 'files/issa.txt'


def test_usage():
    """usage"""
    (retval, out) = getstatusoutput(prg)
    assert retval > 0
    assert re.match("usage", out, re.IGNORECASE)


def test_bad_input():
    """bad input"""
    (retval, out) = getstatusoutput('{} {}'.format(prg, 'foo'))
    assert retval > 0
    assert out == 'foo is not a file'


def test_runs():
    """runs ok"""
    cat_re = re.compile(r'^\s+\d+:.*$')

    for file in [sonnet, issa]:
        assert os.path.exists(file)

        (rv, out) = getstatusoutput("{} {}".format(prg, file))

        assert rv == 0

        num_lines = len(open(file).readlines())
        out_lines = out.split('\n')
        assert len(out_lines) == num_lines

        assert all(map(lambda s: cat_re.match(s), out_lines))
