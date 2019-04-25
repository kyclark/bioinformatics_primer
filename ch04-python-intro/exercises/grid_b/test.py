#!/usr/bin/env python3
"""tests for grid.py"""

from subprocess import getstatusoutput, getoutput
import os.path
import re

grid = './grid.py'


def test_exists():
    """scripts exist"""
    assert os.path.exists(grid)


def test_usage():
    """usage"""
    (retval, out) = getstatusoutput(grid)
    assert retval > 0
    assert re.match("usage", out, re.IGNORECASE)


def test_bad_input():
    """bad input"""
    (rv1, out1) = getstatusoutput(grid + ' -1')
    assert rv1 > 0
    assert out1.rstrip() == 'NUM (-1) must be between 1 and 9'

    (rv2, out2) = getstatusoutput(grid + ' 10')
    assert rv2 > 0
    assert out2.rstrip() == 'NUM (10) must be between 1 and 9'

    (rv3, out3) = getstatusoutput(grid + ' 2 10')
    assert rv3 > 0
    assert out2.rstrip() == 'NUM (10) must be between 1 and 9'


def test_grid():
    grid2 = '  1  2\n  3  4'
    (rv2, out2) = getstatusoutput('{} {}'.format(grid, 2))
    assert rv2 == 0
    assert out2 == grid2

    grid3 = '\n'.join(['  1  2  3', '  4  5  6', '  7  8  9'])
    (rv3, out3) = getstatusoutput('{} {}'.format(grid, 3))
    assert rv3 == 0
    assert out3 == grid3

    grid4 = '\n'.join(
        ['  1  2  3  4', '  5  6  7  8', '  9 10 11 12', ' 13 14 15 16'])
    (rv4, out4) = getstatusoutput('{} {}'.format(grid, 4))
    assert rv4 == 0
    assert out4 == grid4

    grid9 = '\n'.join([
        '  1  2  3  4  5  6  7  8  9', ' 10 11 12 13 14 15 16 17 18',
        ' 19 20 21 22 23 24 25 26 27', ' 28 29 30 31 32 33 34 35 36',
        ' 37 38 39 40 41 42 43 44 45', ' 46 47 48 49 50 51 52 53 54',
        ' 55 56 57 58 59 60 61 62 63', ' 64 65 66 67 68 69 70 71 72',
        ' 73 74 75 76 77 78 79 80 81'
    ])
    (rv9, out9) = getstatusoutput('{} {}'.format(grid, 9))
    assert rv9 == 0
    assert out9 == grid9
