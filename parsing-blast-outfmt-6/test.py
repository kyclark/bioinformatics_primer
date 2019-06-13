#!/usr/bin/env python3
"""tests for blastomatic.py"""

import csv
import hashlib
import os
import random
import re
import string
from subprocess import getstatusoutput, getoutput
from random import shuffle

prg = './blastomatic.py'
hits1 = 'hits1.tab'
hits2 = 'hits2.tab'
centroids = 'centroids.csv'


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

    bad_annots = random_filename()
    rv1, out1 = getstatusoutput('{} -a {} {}'.format(prg, bad_annots, hits1))
    assert rv1 > 0
    assert out1 == '"{}" is not a file'.format(bad_annots)

    bad_hits = random_filename()
    rv2, out2 = getstatusoutput('{} {} -a {}'.format(prg, bad_hits, centroids))
    assert rv2 > 0
    assert out2 == '"{}" is not a file'.format(bad_hits)


# --------------------------------------------------
def test_good_input1():
    """works on good input"""

    err = random_filename()
    if os.path.isfile(err):
        os.remove(err)

    try:
        rv1, out1 = getstatusoutput('{} --annotations {} {} 2>{}'.format(
            prg, centroids, hits1, err))
        assert rv1 == 0
        assert len(out1.split('\n')) == 28

        err_lines = open(err).readlines()
        assert len(err_lines) == 223
    finally:
        if os.path.isfile(err):
            os.remove(err)

# --------------------------------------------------
def test_good_input2():
    """works on good input"""

    out_file = random_filename()
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        rv1, out1 = getstatusoutput('{} -a {} --outfile {} {}'.format(
            prg, centroids, out_file, hits2))
        assert rv1 == 0
        assert len(out1.split('\n')) == 225

        out_lines = open(out_file).readlines()
        assert len(out_lines) == 26

        with open(out_file) as fh:
            reader = csv.DictReader(fh, delimiter='\t')
            assert reader.fieldnames == ['seq_id', 'pident', 'genus', 'species']

            for row in reader:
                if row['seq_id'] == '26cbd1b8b6fcd255774f4f79be2f259c':
                    assert row['pident'] == '98.701'
                    assert row['genus'] == 'Prochlorococcus MIT9313'
                    assert row['species'] == 'NA'
                    break

        #out_contents = open(out_file, 'rb').read()
        #md5_sum = hashlib.md5(out_contents).hexdigest()
        #assert md5_sum == '333544d443be7724a6c1d3ee9e59f799'
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)
