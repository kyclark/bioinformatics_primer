#!/usr/bin/env python3
"""tests for find_unclustered.py"""

import os.path
import random
import string
import re
from subprocess import getstatusoutput, getoutput
from random import shuffle
from Bio import SeqIO

prg = './find_unclustered.py'
proteins = 'unclustered-proteins/proteins.fa'
cdhit = 'unclustered-proteins/cdhit60.3+.clstr'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(prg, flag))
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_input():
    """fails on bad input"""

    rv1, out1 = getstatusoutput('{} -c foo'.format(prg))
    assert rv1 > 0
    assert re.search('the following arguments are required: -p/--proteins',
                     out1)

    rv2, out2 = getstatusoutput('{} -p foo'.format(prg))
    assert rv2 > 0
    assert re.search('the following arguments are required: -c/--cdhit', out2)

    rv3, out3 = getstatusoutput('{} --cdhit foo -p foo'.format(prg))
    assert rv3 > 0
    assert out3.rstrip() == '--proteins "foo" is not a file'

    rv4, out4 = getstatusoutput('{} --proteins {} -c foo'.format(
        prg, proteins))
    assert rv4 > 0
    assert out4.rstrip() == '--cdhit "foo" is not a file'

    rv5, out5 = getstatusoutput('{} --proteins foo --cdhit {}'.format(
        prg, cdhit))
    assert rv5 > 0
    assert out5.rstrip() == '--proteins "foo" is not a file'


# --------------------------------------------------
def test_good_input1():
    """works on good input"""

    out_file = 'unclustered.fa'
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        rv, out = getstatusoutput('{} -c {} -p {}'.format(
            prg, cdhit, proteins))
        assert rv == 0
        expected = ('Wrote 204,262 of 220,520 unclustered '
                    'proteins to "unclustered.fa"')
        assert out == expected

        assert os.path.isfile(out_file)
    finally:
        os.remove(out_file)


# --------------------------------------------------
def test_good_input2():
    """works on good input"""

    out_file = random_filename()
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        rv, out = getstatusoutput('{} --cdhit {} --proteins {} -o {}'.format(
            prg, cdhit, proteins, out_file))
        assert rv == 0

        tmpl = 'Wrote 204,262 of 220,520 unclustered proteins to "{}"'
        assert out == tmpl.format(out_file)

        assert os.path.isfile(out_file)

        seqs = list(SeqIO.parse(out_file, 'fasta'))
        assert len(seqs) == 204262

    finally:
        os.remove(out_file)


# --------------------------------------------------
def random_filename():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
