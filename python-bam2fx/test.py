#!/usr/bin/env python3
"""tests for bam2fa.py"""

import os
import random
import string
import re
from subprocess import getstatusoutput, getoutput
from shutil import rmtree
from Bio import SeqIO

prg = './bam2fx.py'
inputs = '../inputs/*.bam'


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
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_bad_file():
    """usage"""

    bad = random_filename()
    _, out = getstatusoutput('{} {}'.format(prg, bad))
    assert re.search('"{}" is not a file'.format(bad), out)


# --------------------------------------------------
def run(fmt):
    """runs"""

    out_dir = random_filename()

    print(out_dir)
    if os.path.isdir(out_dir):
        rmtree(out_dir)

    try:
        rv, out = getstatusoutput('{} {} -f {} -o {}'.format(
            prg, inputs, fmt, out_dir))
        assert rv == 0
        assert out.splitlines()[-1].rstrip() == 'Done.'

        assert os.path.isdir(out_dir)

        files = os.listdir(out_dir)
        assert len(files) == 1

        fasta = os.path.join(out_dir, files[0])
        seqs = list(SeqIO.parse(fasta, fmt))
        assert len(seqs) == 290

    finally:
        if os.path.isdir(out_dir):
            rmtree(out_dir)


# --------------------------------------------------
def test_fasta():
    run('fasta')


# --------------------------------------------------
def test_fastq():
    run('fastq')


# --------------------------------------------------
def random_filename():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
