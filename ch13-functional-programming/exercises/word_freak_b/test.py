#!/usr/bin/env python3
"""tests for freak.py"""

from subprocess import getstatusoutput
import os
import random
import re
import string
import sys

prg = './freak.py'
nobody = 'data/nobody.txt'
decl = 'data/usdeclar.txt'
const = 'data/const.txt'


# --------------------------------------------------
def test_usage():
    """usage"""
    (ret1, out1) = getstatusoutput(prg)
    assert ret1 > 0
    assert re.match("usage", out1, re.IGNORECASE)


# --------------------------------------------------
def bad_filename():
    """Generate a bad filename"""
    while True:
        file = ''.join(
            random.choice(string.ascii_lowercase) for i in range(10))
        if not os.path.isfile(file):
            return file


# --------------------------------------------------
def test_bad_file():
    """usage"""
    bad = bad_filename()
    (ret1, out1) = getstatusoutput('{} {}'.format(prg, bad))
    assert ret1 > 0


# --------------------------------------------------
def run_it(in_file, min_val, sort_val, out_base=''):
    """run"""
    out_path = '.'.join([out_base or in_file, str(min_val), sort_val, 'out'])

    print(out_path)
    assert os.path.isfile(out_path)

    expected = open(out_path).read().rstrip()
    rand = random.choice([0, 1])
    min_arg = '-m' if rand else '--min'
    sort_arg = '-s' if rand == 1 else '--sort'
    cmd = '{} {} {} {} {} {}'.format(prg, sort_arg, sort_val, min_arg, min_val,
                                     in_file)
    print(cmd)
    rv, out = getstatusoutput(cmd)
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
def test_01():
    """runs ok"""
    run_it(nobody, 0, 'word')


# --------------------------------------------------
def test_02():
    """runs ok"""
    run_it(nobody, 5, 'word')


# --------------------------------------------------
def test_03():
    """runs ok"""
    run_it(nobody, 10, 'word')


# --------------------------------------------------
def test_04():
    """runs ok"""
    run_it(nobody, 0, 'frequency')


# --------------------------------------------------
def test_05():
    """runs ok"""
    run_it(nobody, 5, 'frequency')


# --------------------------------------------------
def test_06():
    """runs ok"""
    run_it(nobody, 10, 'frequency')


# --------------------------------------------------
def test_07():
    """runs ok"""
    run_it(const, 0, 'word')


# --------------------------------------------------
def test_08():
    """runs ok"""
    run_it(const, 5, 'word')


# --------------------------------------------------
def test_09():
    """runs ok"""
    run_it(const, 10, 'word')


# --------------------------------------------------
def test_10():
    """runs ok"""
    run_it(const, 0, 'frequency')


# --------------------------------------------------
def test_11():
    """runs ok"""
    run_it(const, 5, 'frequency')


# --------------------------------------------------
def test_12():
    """runs ok"""
    run_it(const, 10, 'frequency')

# --------------------------------------------------
def test_13():
    """runs ok"""
    run_it(decl, 0, 'word')


# --------------------------------------------------
def test_14():
    """runs ok"""
    run_it(decl, 5, 'word')


# --------------------------------------------------
def test_15():
    """runs ok"""
    run_it(decl, 10, 'word')


# --------------------------------------------------
def test_16():
    """runs ok"""
    run_it(decl, 0, 'frequency')


# --------------------------------------------------
def test_17():
    """runs ok"""
    run_it(decl, 5, 'frequency')


# --------------------------------------------------
def test_18():
    """runs ok"""
    run_it(decl, 10, 'frequency')

# --------------------------------------------------
def test_19():
    """runs ok"""
    run_it(' '.join([const, decl, nobody]), 0, 'word', out_base='data/all')


# --------------------------------------------------
def test_20():
    """runs ok"""
    run_it(' '.join([const, decl, nobody]), 5, 'word', out_base='data/all')


# --------------------------------------------------
def test_21():
    """runs ok"""
    run_it(' '.join([const, decl, nobody]), 10, 'word', out_base='data/all')


# --------------------------------------------------
def test_22():
    """runs ok"""
    run_it(' '.join([const, decl, nobody]), 0, 'frequency', out_base='data/all')


# --------------------------------------------------
def test_23():
    """runs ok"""
    run_it(' '.join([const, decl, nobody]), 5, 'frequency', out_base='data/all')


# --------------------------------------------------
def test_24():
    """runs ok"""
    run_it(' '.join([const, decl, nobody]), 10, 'frequency', out_base='data/all')
