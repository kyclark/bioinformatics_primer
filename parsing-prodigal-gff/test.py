#!/usr/bin/env python3
"""tests for wc.py"""

from subprocess import getstatusoutput
import os

prg = './parse_gff.py'
gff1 = '../inputs/HUMANGUT_SMPL_INB.fa.prodigal.gff'
gff2 = '../inputs/mgm4529847.3.050.upload.fna.prodigal.gff'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        _, out = getstatusoutput('{} {}'.format(prg, flag))
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_01():
    """runs"""

    rv, out = getstatusoutput('{} {}'.format(prg, gff1))
    assert rv == 0
    assert out.rstrip() == open('test-outs/gff1.noargs').read().rstrip()


# --------------------------------------------------
def test_02():
    """runs"""

    rv, out = getstatusoutput('{} -m 100 {}'.format(prg, gff1))
    assert rv == 0
    assert out.rstrip() == open('test-outs/gff1.min100').read().rstrip()


# --------------------------------------------------
def test_02():
    """runs"""

    rv, out = getstatusoutput('{} --min 300 {}'.format(prg, gff1))
    assert rv == 0
    assert out.rstrip() == open('test-outs/gff1.min300').read().rstrip()


# --------------------------------------------------
def test_03():
    """runs"""

    rv, out = getstatusoutput('{} {}'.format(prg, gff2))
    assert rv == 0
    assert out.rstrip() == open('test-outs/gff2.noargs').read().rstrip()


# --------------------------------------------------
def test_04():
    """runs"""

    rv, out = getstatusoutput('{} -m 125 {}'.format(prg, gff2))
    assert rv == 0
    assert out.rstrip() == open('test-outs/gff2.min125').read().rstrip()
