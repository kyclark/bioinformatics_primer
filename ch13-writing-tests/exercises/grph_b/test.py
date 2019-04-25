#!/usr/bin/env python3
"""tests for grph.py"""

from subprocess import getstatusoutput
import os
import random
import re
import string
import sys
import grph

prg = './grph.py'


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
def test_bad_k():
    """bad k"""
    for k in [0, -1]:
        rv, out = getstatusoutput('{} -k {} sample1.fa'.format(prg, k))
        assert rv > 0
        assert out.strip() == '-k "{}" must be a positive integer'.format(k)


# --------------------------------------------------
def test_bad_file():
    """usage"""
    bad = bad_filename()
    (ret1, out1) = getstatusoutput('{} {}'.format(prg, bad))
    assert ret1 > 0
    assert out1.strip() == '"{}" is not a file'.format(bad)


# --------------------------------------------------
def test_find_kmers():
    """Test the `find_kmers` function"""
    assert grph.find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert grph.find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert grph.find_kmers('ACTG', 4) == ['ACTG']

# --------------------------------------------------
def run_it(in_file, k):
    """run"""
    out_file = '.'.join([in_file, str(k), 'out'])
    if not os.path.isfile(out_file):
        print('Missing expected output file "{}"'.format(out_file))
        sys.exit(1)

    expected = open(out_file).read().rstrip()
    cmd = '{} -k {} {} | sort'.format(prg, k, in_file)
    rv, out = getstatusoutput(cmd)
    assert rv == 0
    assert out.rstrip() == expected

# --------------------------------------------------
def test_01():
    """runs ok"""
    run_it('sample1.fa', 3)

# --------------------------------------------------
def test_02():
    """runs ok"""
    run_it('sample1.fa', 4)

# --------------------------------------------------
def test_03():
    """runs ok"""
    run_it('sample1.fa', 5)

# --------------------------------------------------
def test_04():
    """runs ok"""
    run_it('sample2.fa', 3)

# --------------------------------------------------
def test_05():
    """runs ok"""
    run_it('sample2.fa', 4)

# --------------------------------------------------
def test_06():
    """runs ok"""
    run_it('sample2.fa', 5)

# --------------------------------------------------
def test_07():
    """runs ok"""
    run_it('sample3.fa', 3)

# --------------------------------------------------
def test_08():
    """runs ok"""
    run_it('sample3.fa', 4)

# --------------------------------------------------
def test_09():
    """runs ok"""
    run_it('sample3.fa', 5)
