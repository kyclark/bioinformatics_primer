#!/usr/bin/env python3
"""tests for gc.py"""

import os.path
import random
import string
import re
from subprocess import getstatusoutput, getoutput

prg = './gc.py'
sample1 = 'inputs/sample1.txt'
sample2 = 'inputs/sample2.txt'
sample3 = 'inputs/sample3.txt'


# --------------------------------------------------
def test_exists():
    """ usage """

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """ usage """

    for flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(prg, flag))
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_input():
    """ fails on bad input """

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_good_input1():
    """ works on good input """

    rv, out = getstatusoutput(f'{prg} {sample1}')
    assert rv == 0
    assert out == ' 50%: ACgt'


# --------------------------------------------------
def test_good_input2():
    """ works on good input """

    rv, out = getstatusoutput(f'{prg} {sample2}')
    expected = '\n'.join([
        ' 10%: ATTTACAATAATTTAATAAAATTAACTAGAAATAAAATATTGTATGAAAATATGTTAAAT',
        ' 20%: AATGAAAGTTTTTCAGATCGTTTAATAATATTTTTCTTCCATTTTGCTTTTTTCTAAAAT',
        ' 20%: TGTTCAAAAACAAACTTCAAAGGAAAATCTTCAAAATTTACATGATTTTATATTTAAACA',
        ' 23%: AATAGAGTTAAGTATAAGAGAAATTGGATATGGTGATGCTTCAATAAATAAAAAAATGAA',
        ' 33%: AGAGTATGTCAATGTGATGTACGCAATAATTGACAAAGTTGATTCATGGGAAAATCTTGA',
        ' 21%: TTTATCTACAAAAACTAAATTCTTTTCTGAATTTATTAATGTCGATAAGGAATCTACATT',
    ])
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def test_good_input3():
    """ works on good input """

    rv, out = getstatusoutput(f'{prg} {sample3}')
    expected = '\n'.join([
        ' 30%: TTTGTAAAGTCTGGATTAACTGCTATAAAATCGGAAACCATAACACCTTTTAGAGTTAAA',
        ' 35%: GAATCTCCTGTTCAAATGGAATGTATTGTTAATGATGTTATTGAACTTGGAGACCAAGGT',
        ' 26%: GGAGCAGGAAATTTAGTAGTATGTGAAATAAAAATGATTCACATTAATGAAGATATTCTT',
        ' 35%: gatgatgaaggaattattgatccaaataaaattaaattagtcggacgcatgggtggaaac',
        ' 30%: TGGTATTGTAAAACTACCAACGAATCTATCTTTGAAGTTGTTAAACCTATCCGTAATTTA',
        ' 30%: ggtattggtgttgatcagattcctaaacgaattaaaaatagctatattcttagtggaaat',
        ' 38%: GATTTaggtatgcTAGGAAATATAGAAGCCTTacctaccatCGAAGAggttgAAGAATAC',
        ' 18%: AAAAAAGAAAACTAACactataaaatgaaaTAATTAAATTTTAagtagtgaagatgaaga',
        ' 35%: CAATGCTGAATTTGAATAATTTCCATGTGAATTGGTGGAATATTGTTCTAACAGTGCACG',
    ])
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def random_string():
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
