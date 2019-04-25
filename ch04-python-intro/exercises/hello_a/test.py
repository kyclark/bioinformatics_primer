#!/usr/bin/env python3
"""tests for hello.py"""

from subprocess import getstatusoutput, getoutput
import os.path
import re

prg = './hello.py'


def test_usage():
    """usage"""
    (retval, out) = getstatusoutput(prg)
    assert retval > 0
    assert re.match("usage", out, re.IGNORECASE)


def test_runs():
    """runs hello"""
    out1 = getoutput(prg + ' Alice')
    assert out1.rstrip() == 'Hello to the 1 of you: Alice!'

    out2 = getoutput(prg + ' Mike Carol')
    assert out2.rstrip() == 'Hello to the 2 of you: Mike and Carol!'

    out3 = getoutput(prg + ' Greg Peter Bobby Marcia Jane Cindy')
    assert out3.rstrip(
    ) == 'Hello to the 6 of you: Greg, Peter, Bobby, Marcia, Jane, and Cindy!'
