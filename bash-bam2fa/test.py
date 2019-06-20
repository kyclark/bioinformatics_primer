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
in_dir = '../inputs'


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
    assert out.rstrip() == 'Bad IN_DIR "{}"'.format(bad)


# --------------------------------------------------
def test_runs():
    """runs"""

    out_dir = random_filename()

    print(out_dir)
    if os.path.isdir(out_dir):
        rmtree(out_dir)

    try:
        rv, out = getstatusoutput('{} {} {}'.format(prg, in_dir, out_dir))
        assert rv == 0
        assert out.splitlines()[-1].rstrip() == 'Done.'

        assert os.path.isdir(out_dir)

        files = os.listdir(out_dir)
        assert len(files) == 1

        fasta = os.path.join(out_dir, files[0])
        seqs = list(SeqIO.parse(fasta, 'fasta'))
        assert len(seqs) == 290

    finally:
        if os.path.isdir(out_dir):
            rmtree(out_dir)


# --------------------------------------------------
def random_filename():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
