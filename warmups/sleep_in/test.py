#!/usr/bin/env python3

from subprocess import getoutput

prg = './sleep_in.py'

def test_usage():
    out = getoutput('{}'.format(prg))
    assert out == 'Usage: sleep_in.py DAY VACATION'

def test_01():
    out = getoutput('{} Monday No'.format(prg))
    assert out == 'No'

def test_02():
    out = getoutput('{} sunday no'.format(prg))
    assert out == 'Yes'

def test_03():
    out = getoutput('{} TUESDAY YES'.format(prg))
    assert out == 'Yes'

def test_04():
    out = getoutput('{} Saturday YES'.format(prg))
    assert out == 'Yes'

def test_05():
    out = getoutput('{} THURSDAY no'.format(prg))
    assert out == 'No'

def test_06():
    out = getoutput('{} ThUrSdaY yEs'.format(prg))
    assert out == 'Yes'
