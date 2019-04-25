#!/usr/bin/env python3
"""tests for tictactoe.py"""

from subprocess import getstatusoutput, getoutput
import re

ttt = './tictactoe.py'


# --------------------------------------------------
def usage(prg):
    """usage"""
    (retval, out) = getstatusoutput(prg)
    assert retval == 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_usage():
    """usage"""
    usage('{} -h'.format(ttt))
    usage('{} --help'.format(ttt))


# --------------------------------------------------
def test_no_input():
    """makes board on no input"""

    board = """
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
""".strip()

    out = getoutput(ttt)
    assert out.strip() == board


# --------------------------------------------------
def test_bad_state():
    """dies on bad state"""
    tmpl = 'Invalid state "{}", must be 9 characters of only -, X, O'
    for bad in ['ABC', '...XXX', 'XXXOOOXX']:
        rv, out = getstatusoutput('{} --state {}'.format(ttt, bad))
        assert rv > 0
        assert out == tmpl.format(bad)


# --------------------------------------------------
def test_bad_player():
    """dies on bad player"""
    rv, out = getstatusoutput('{} -p A'.format(ttt))
    assert rv > 0
    assert out == 'Invalid player "A", must be X or O'


# --------------------------------------------------
def test_bad_cell_int():
    """dies on bad cell"""
    e = 'Invalid cell "{}", must be 1-9'
    for bad in [0, 10]:
        rv, out = getstatusoutput('{} --cell {}'.format(ttt, bad))
        assert rv > 0
        assert out == e.format(bad)


# --------------------------------------------------
def test_bad_cell_str():
    """dies on bad cell string value"""
    rv, out = getstatusoutput('{} --cell foo'.format(ttt))
    assert rv > 0
    assert re.match("usage", out, re.IGNORECASE)
    assert re.search("invalid int value", out, re.IGNORECASE)


# --------------------------------------------------
def test_both_player_and_cell():
    """test for both --player and --cell"""
    rv, out = getstatusoutput('{} --player X'.format(ttt))
    assert rv > 0
    assert out == 'Must provide both --player and --cell'


# --------------------------------------------------
def test_good_state():
    """makes board on good input"""

    board1 = """
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
""".strip()

    out1 = getoutput('{} -s .........'.format(ttt))
    assert out1.strip() == board1

    board2 = """
-------------
| 1 | 2 | 3 |
-------------
| O | X | X |
-------------
| 7 | 8 | 9 |
-------------
""".strip()

    out2 = getoutput('{} -s ...OXX...'.format(ttt))
    assert out2.strip() == board2


# --------------------------------------------------
def test_mutate_state():
    """mutates board on good input"""

    board1 = """
-------------
| X | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
""".strip()

    out1 = getoutput('{} -s ......... --player X -c 1'.format(ttt))
    assert out1.strip() == board1

    board2 = """
-------------
| X | X | O |
-------------
| 4 | O | 6 |
-------------
| O | O | X |
-------------
""".strip()

    out2 = getoutput('{} --state XXO...OOX --p O -c 5'.format(ttt))
    assert out2.strip() == board2


# --------------------------------------------------
def test_mutate_state_taken():
    """test for a cell already taken"""
    out1 = getoutput('{} -s XXO...OOX --player X --cell 9'.format(ttt))
    assert out1.strip() == 'Cell 9 already taken'

    out2 = getoutput('{} --state XXO...OOX --p O -c 1'.format(ttt))
    assert out2.strip() == 'Cell 1 already taken'
