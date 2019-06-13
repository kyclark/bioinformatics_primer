#!/usr/bin/env python3
"""tests for swiss.py"""

import csv
import hashlib
import os
import random
import re
import string
from subprocess import getstatusoutput, getoutput
from random import shuffle
from Bio import SeqIO

prg = './swisstake.py'


# --------------------------------------------------
def random_filename():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(prg, flag))
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_input():
   """fails on bad input"""

   bad = random_filename()
   rv1, out1 = getstatusoutput('{} -k foo {}'.format(prg, bad))
   assert rv1 > 0
   assert out1 == '"{}" is not a file'.format(bad)

   rv2, out2 = getstatusoutput('{} {}'.format(prg, 'swiss.txt'))
   assert rv2 > 0
   assert re.search('are required: -k/--keyword', out2)


# --------------------------------------------------
def test_good_input():
    """works on good input"""

    tests = [{
        'kw': '"complete proteome"',
        'tax': '-s Metazoa FUNGI viridiplantae',
        'skipped': 14,
        'took': 1
    }, {
        'kw': '"complete proteome"',
        'tax': '-s METAZOA fungi',
        'skipped': 13,
        'took': 2
    }, {
        'kw': '"complete proteome"',
        'tax': '-s metazoa',
        'skipped': 9,
        'took': 6
    }, {
        'kw': '"complete proteome"',
        'tax': '',
        'skipped': 6,
        'took': 9
    }, {
        'kw': 'malaria',
        'tax': '',
        'skipped': 13,
        'took': 2
    }]

    out_tmpl = 'Done, skipped {skipped} and took {took}. See output in "{out}".'
    run_tmpl = '{prg} {file} -o {out_file} {skip} -k {keyword}'
    for test in tests:
        out_file = random_filename()
        if os.path.isfile(out_file):
            os.remove(out_file)

        try:
            rv, out = getstatusoutput(
                run_tmpl.format(
                    prg=prg,
                    file='swiss.txt',
                    out_file=out_file,
                    skip=test['tax'],
                    keyword=test['kw']))
            assert rv == 0
            assert out.split('\n')[-1] == out_tmpl.format(
                skipped=test['skipped'], took=test['took'], out=out_file)

            fasta = list(SeqIO.parse(out_file, 'fasta'))
            assert len(fasta) == test['took']

        finally:
            if os.path.isfile(out_file):
                os.remove(out_file)
