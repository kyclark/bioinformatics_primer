#!/usr/bin/env python3
"""tests for bam2fa.py"""

import os
import random
import string
import re
from subprocess import getstatusoutput, getoutput
from shutil import rmtree
from Bio import SeqIO

prg = './bam2fa.sh'
bam1 = '../inputs/test1.bam'
bam2 = '../inputs/test2.bam'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_noargs():
    """usage"""

    rv, out = getstatusoutput('{}'.format(prg))
    assert rv > 0
    assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_too_few_args():
    """usage"""

    rv, out = getstatusoutput('{} foo'.format(prg))
    assert rv > 0
    assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_too_many_args():
    """usage"""

    bad = random_filename()
    rv, out = getstatusoutput('{} foo bar baz quuz'.format(prg, bad))
    assert rv > 0
    assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_bad_dir():
    """usage"""

    bad = random_filename()
    rv, out = getstatusoutput('{} {} out'.format(prg, bad))
    assert rv > 0
    assert out.rstrip() == 'INPUT "{}" neither file nor directory!'.format(bad)


# --------------------------------------------------
def test_bam1():
    run(bam1, [('test1.fa', 290)])


# --------------------------------------------------
def test_bam2():
    run(bam2, [('test2.fa', 410)])


# --------------------------------------------------
def test_dir():
    run('../inputs', [('test1.fa', 290), ('test2.fa', 410)])


# --------------------------------------------------
def run(input_arg, expected_files):
    """runs"""

    out_dir = random_filename()

    print(out_dir)
    if os.path.isdir(out_dir):
        rmtree(out_dir)

    try:
        rv, out = getstatusoutput('{} {} {}'.format(prg, input_arg, out_dir))
        assert rv == 0
        expected = 'Done, see output in "{}"'.format(out_dir)
        assert out.splitlines()[-1].rstrip() == expected

        assert os.path.isdir(out_dir)

        files = os.listdir(out_dir)

        for filename, num in expected_files:
            assert filename in files
            fasta = os.path.join(out_dir, filename)
            seqs = list(SeqIO.parse(fasta, 'fasta'))
            assert len(seqs) == num

    finally:
        if os.path.isdir(out_dir):
            rmtree(out_dir)


# --------------------------------------------------
def random_filename():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
