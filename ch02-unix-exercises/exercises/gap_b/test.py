#!/usr/bin/env python3
"""tests for gap.sh"""

from subprocess import getstatusoutput, getoutput
import os.path
import re

prg = "./gap.sh"


# --------------------------------------------------
def test_gap():
    (retval1, out1) = getstatusoutput(prg)
    assert retval1 == 0
    assert len(out1.split('\n')) >= 142

    (retval2, out2) = getstatusoutput('{} {}'.format(prg, 'b'))
    assert retval2 == 0
    assert len(out2.split('\n')) == 11

    (retval3, out3) = getstatusoutput('{} {}'.format(prg, 'q'))
    assert retval3 == 1
    assert out3 == 'There are no countries starting with "q"'

    (retval4, out4) = getstatusoutput('{} "{}"'.format(prg, '[u-z]'))
    assert retval4 == 0
    assert len(out4.split('\n')) == 10
