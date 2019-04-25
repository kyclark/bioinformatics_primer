#!/usr/bin/env python3

from subprocess import getstatusoutput

prg = './hello.py'

def test_usage():
    rv, out = getstatusoutput('{}'.format(prg))
    assert rv != 0
    assert out.lower().startswith('usage')

def test_runs_ok():
    rv1, out1 = getstatusoutput('{} Barbara'.format(prg))
    assert rv1 == 0
    assert out1 == 'Hello, Barbara!'

    rv2, out2 = getstatusoutput('{} Barbara McClintock'.format(prg))
    assert rv2 == 0
    assert out2 == 'Hello, Barbara!\nHello, McClintock!'

    rv3, out3 = getstatusoutput('{} "Barbara McClintock"'.format(prg))
    assert rv3 == 0
    assert out3 == 'Hello, Barbara McClintock!'
