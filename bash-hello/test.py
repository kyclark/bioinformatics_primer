#!/usr/bin/env python3
"""tests for hello.sh"""

from subprocess import getstatusoutput, getoutput
import os.path
import re

prg = "./hello.sh"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    rv, out = getstatusoutput(prg)
    assert rv > 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_hello_too_many():
    """should die"""

    rv, out = getstatusoutput('{} {} {} {}'.format(prg, 'foo', 'bar', 'baz'))
    assert rv > 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_runs01():
    """should run"""

    rv, out = getstatusoutput('{} {}'.format(prg, 'Hello'))
    assert rv == 0
    assert out == 'Hello, Human!'


# --------------------------------------------------
def test_runs02():
    """should run"""

    rv, out = getstatusoutput('{} "{}" "{}"'.format(prg, 'Good Day',
                                                    'Kind Sir'))
    assert rv == 0
    assert out == 'Good Day, Kind Sir!'
