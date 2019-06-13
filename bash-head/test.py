#!/usr/bin/env python3
"""tests for head.sh"""

from subprocess import getstatusoutput, getoutput
import os.path
import re

prg = "./head.sh"


# --------------------------------------------------
def test_exists():
    assert os.path.isfile(prg)


# --------------------------------------------------
def head_file(file, n=3):
    """the expected output head"""

    lines = []
    for i, line in enumerate(open(file)):
        lines.append(line)
        if i + 1 == n:
            break
    return ''.join(lines)


# --------------------------------------------------
def test_usage_head():
    """usage head"""

    (retval, out) = getstatusoutput(prg)
    assert retval > 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_input_head():
    """bad input"""

    (retval, out) = getstatusoutput('{} {}'.format(prg, 'foo'))
    assert retval > 0
    assert out == 'foo is not a file'


# --------------------------------------------------
def test_head_run():
    """runs ok"""

    for (file, num) in [("files/sonnet-29.txt", 3), ("files/issa.txt", 10)]:
        out = getoutput("{} {} {}".format(prg, file, num))
        expected = head_file(file, num)
        assert out.rstrip() == expected.rstrip()
