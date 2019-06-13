#!/usr/bin/env python3
"""tests for cat-n.sh"""

from subprocess import getstatusoutput
import os
import re

prg = "./cat_n.sh"


def test_usage():
    """usage catn"""
    rv, out = getstatusoutput(prg)
    print(out)
    assert rv > 0
    assert re.match("usage", out, re.IGNORECASE)


def test_bad_input():
    """bad input catn"""
    rv, out = getstatusoutput('{} {}'.format(prg, 'foo'))
    assert rv > 0
    assert out == 'foo is not a file'


def test_run():
    """runs ok"""
    for file in ["files/sonnet-29.txt", "files/issa.txt"]:
        assert os.path.exists(file)

        fh = open(file, "r")
        expected = "".join(
            map(lambda x: '{} {}'.format(x[0] + 1, x[1]),
                enumerate(fh.readlines())))

        rv, out = getstatusoutput("{} {}".format(prg, file))

        assert rv == 0
        assert out.rstrip() == expected.rstrip()
