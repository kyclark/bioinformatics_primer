#!/usr/bin/env python3
"""tests for gc.py"""

import os.path
import random
import string
import re
from subprocess import getstatusoutput, getoutput
from random import shuffle
from Bio import SeqIO
from shutil import rmtree

prg = './gc.py'
gs108 = 'fasta/CAM_SMPL_GS108.fa'
gs112 = 'fasta/CAM_SMPL_GS112.fa'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(prg, flag))
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_input():
    """fails on bad input"""

    for pct in [-1, 101]:
        rv, out = getstatusoutput('{} -p {} fasta'.format(prg, pct))
        assert rv > 0
        assert out == '--pct_gc "{}" must be between 0 and 100'.format(pct)

    rv, out = getstatusoutput('{} foo bar'.format(prg))
    assert rv == 0
    msg = '\n'.join([
        '"foo" is not a file', '"bar" is not a file',
        'Done, wrote 0 sequences to out dir "out"'
    ])
    assert out == msg


# --------------------------------------------------
def test_good_input1():
    """works on good input"""

    out_dir = 'out'
    if os.path.isdir(out_dir):
        rmtree(out_dir)

    rv, out = getstatusoutput('{} {}'.format(prg, gs108))
    assert rv == 0
    assert os.path.isdir(out_dir)

    base, ext = os.path.splitext(os.path.basename(gs108))
    low = os.path.join(out_dir, base + '_low' + ext)
    high = os.path.join(out_dir, base + '_high' + ext)
    assert os.path.isfile(low)
    assert os.path.isfile(high)

    num_low = len(list(SeqIO.parse(low, 'fasta')))
    assert num_low == 487

    num_high = len(list(SeqIO.parse(high, 'fasta')))
    assert num_high == 13


# --------------------------------------------------
def test_good_input2():
    """works on good input"""

    out_dir = random_filename()
    if os.path.isdir(out_dir):
        rmtree(out_dir)

    rv, out = getstatusoutput('{} -o {} -p 30 {}'.format(prg, out_dir, gs112))
    assert rv == 0
    assert os.path.isdir(out_dir)

    base, ext = os.path.splitext(os.path.basename(gs112))
    low = os.path.join(out_dir, base + '_low' + ext)
    high = os.path.join(out_dir, base + '_high' + ext)
    assert os.path.isfile(low)
    assert os.path.isfile(high)

    num_low = len(list(SeqIO.parse(low, 'fasta')))
    assert num_low == 143

    num_high = len(list(SeqIO.parse(high, 'fasta')))
    assert num_high == 357

    rmtree(out_dir)


# --------------------------------------------------
def test_good_input3():
    """works on good input"""

    out_dir = random_filename()
    if os.path.isdir(out_dir):
        rmtree(out_dir)

    rv, out = getstatusoutput('{} -o {} -p 53 {} {}'.format(
        prg, out_dir, gs112, gs108))
    assert rv == 0
    assert os.path.isdir(out_dir)

    for file, low_num, high_num in [(gs108, 490, 10), (gs112, 478, 22)]:
        base, ext = os.path.splitext(os.path.basename(file))
        low = os.path.join(out_dir, base + '_low' + ext)
        high = os.path.join(out_dir, base + '_high' + ext)
        assert os.path.isfile(low)
        assert os.path.isfile(high)

        num_low = len(list(SeqIO.parse(low, 'fasta')))
        assert num_low == low_num

        num_high = len(list(SeqIO.parse(high, 'fasta')))
        assert num_high == high_num

    rmtree(out_dir)


# --------------------------------------------------
def random_filename():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
