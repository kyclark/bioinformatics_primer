#!/usr/bin/env python3
"""tests for translate_proteins.py"""

from subprocess import getstatusoutput, getoutput
import os.path
import re
import string
import random

prg = './translate_proteins.py'
dna = 'gaactacaccgttctcctggt'
rna = 'UGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGAA'


# --------------------------------------------------
def random_filename():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_args():
    """die on no/bad args"""

    rv1, out1 = getstatusoutput(prg)
    assert rv1 > 0
    assert re.match("usage", out1, re.IGNORECASE)

    rv2, out2 = getstatusoutput('{} -c codons.rna'.format(prg))
    assert rv2 > 0
    assert re.match("usage", out2, re.IGNORECASE)

    rv3, out3 = getstatusoutput('{} {}'.format(prg, dna))
    assert rv3 > 0
    assert re.match("usage", out3, re.IGNORECASE)


# --------------------------------------------------
def test_bad_codon_file():
    """die on bad codon_file"""

    bad = random_filename()
    rv, out = getstatusoutput('{} --codons {} {}'.format(prg, bad, dna))
    assert rv > 0
    assert out.strip() == '--codons "{}" is not a file'.format(bad)


# --------------------------------------------------
def test_valid_input():
    """runs ok"""
    tests = [(rna, 'codons.rna', 'WPWRPELRSIVPVLTGE'),
             (dna, 'codons.dna', 'ELHRSPG'),
             (rna, 'codons.dna', '-P-RPE-R---P--T-E'),
             (dna, 'codons.rna', 'E-H----')]

    for seq, codons, aa in tests:
        flip = random.randint(0, 1)
        random_file = random_filename()
        out_file, out_arg = (random_file,
                             '-o ' + random_file) if flip == 1 else ('out.txt',
                                                                     '')

        rv, output = getstatusoutput("{} -c {} {} {}".format(
            prg, codons, out_arg, seq))

        assert rv == 0
        assert output.rstrip() == 'Output written to "{}"'.format(out_file)
        assert os.path.isfile(out_file)
        assert open(out_file).read().strip() == aa
        os.remove(out_file)
