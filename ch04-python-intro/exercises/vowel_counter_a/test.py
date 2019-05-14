#!/usr/bin/env python3
"""tests for vowel_counter.py"""

from subprocess import getstatusoutput
import os

prg = './vowel_counter.py'


# --------------------------------------------------
def test_usage_counter():
    """usage"""
    rv, out = getstatusoutput(prg)
    assert rv > 0
    assert out.lower().startswith('usage')


# --------------------------------------------------
def test_01():
    """runs"""
    rv, out = getstatusoutput(prg + ' if')
    assert rv == 0
    assert out.rstrip() == 'There is 1 vowel in "if."'


# --------------------------------------------------
def test_02():
    """runs"""
    rv, out = getstatusoutput(prg + ' if')
    assert rv == 0
    assert out.rstrip() == 'There is 1 vowel in "if."'


# --------------------------------------------------
def test_03():
    """runs"""
    rv, out = getstatusoutput(prg + ' foo')
    assert rv == 0
    assert out.rstrip() == 'There are 2 vowels in "foo."'


# --------------------------------------------------
def test_04():
    """runs"""
    rv, out = getstatusoutput(prg + ' covfefe')
    assert rv == 0
    assert out.rstrip() == 'There are 3 vowels in "covfefe."'


# --------------------------------------------------
def test_05():
    """runs"""
    rv, out = getstatusoutput(prg + ' YYZ')
    assert rv == 0
    assert out.rstrip() == 'There are 0 vowels in "YYZ."'


# --------------------------------------------------
def test_06():
    """runs"""
    rv, out = getstatusoutput(prg + ' HELLO')
    assert rv == 0
    assert out.rstrip() == 'There are 2 vowels in "HELLO."'
