#!/usr/bin/env python3
"""tests for common_words.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = "./commoner.py"
fox = 'data/fox.txt'
american = 'data/american.txt'
british = 'data/british.txt'
nobody = 'data/nobody.txt'


# --------------------------------------------------
def random_string():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))


# --------------------------------------------------
def test_usage():
    """usage"""
    rv1, out1 = getstatusoutput(prg)
    assert rv1 > 0
    assert re.match("usage", out1, re.IGNORECASE)

    rv2, out2 = getstatusoutput('{} fox.txt'.format(prg))
    assert rv2 > 0
    assert re.match("usage", out2, re.IGNORECASE)


# --------------------------------------------------
def test_bad_n():
    """bad_n"""
    bad = random.choice(range(-10, -1))
    rv, out = getstatusoutput('{} {} {} -n {}'.format(prg, american, british,
                                                      bad))
    assert rv > 0
    assert out == '--distance "{}" must be > 0'.format(bad)


# --------------------------------------------------
def test_bad_input():
    """bad_input"""
    rv, _ = getstatusoutput('{} {} {}'.format(prg, 'fox.txt', random_string()))
    assert rv > 0


# --------------------------------------------------
def test_runs_ok():
    for f1, f2, min_len, hamm, table, expected_file in [
        (fox, fox, 0, 0, False, 'data/fox-fox.out'),
        (fox, fox, 0, 0, True, 'data/fox-fox.table.out'),
        (fox, fox, 4, 0, False, 'data/fox-fox.min4.out'),
        (fox, fox, 10, 0, False, 'data/fox-fox.min10.out'),
        (fox, nobody, 0, 0, False, 'data/fox-nobody.out'),
        (fox, nobody, 3, 0, True, 'data/fox-nobody.table.min3.out'),
        (fox, nobody, 5, 0, False, 'data/fox-nobody.min5.out'),
        (american, british, 0, 0, False, 'data/am-br.out'),
        (american, british, 0, 0, True, 'data/am-br.table.out'),
        (american, british, 3, 0, False, 'data/am-br.min3.out'),
        (american, british, 3, 0, True, 'data/am-br.table.min3.out'),
        (american, british, 4, 1, False, 'data/am-br.min4.n1.out'),
        (american, british, 4, 1, True, 'data/am-br.table.min4.n1.out'),
        (american, british, 3, 2, False, 'data/am-br.min3.n2.out'),
        (american, british, 3, 2, True, 'data/am-br.table.min3.n2.out'),
    ]:
        assert os.path.isfile(expected_file)

        for debug in [True, False]:
            log = random_string()

            if os.path.isfile(log):
                os.remove(log)

            heads = random.choice([True, False])
            min_flag = '-m ' if heads else '--min_len '
            hamm_flag = '-n ' if heads else '--hamming_distance '
            table_flag = '-t ' if heads else '--table '
            debug_flag = '-d ' if heads else '--debug '
            log_flag = '-l ' if heads else '--logfile '

            args = (prg, debug_flag if debug else '', table_flag
                    if table else '', min_flag + str(min_len)
                    if min_len else '', hamm_flag + str(hamm)
                    if hamm else '', log_flag + log if debug else '', f1, f2)
            cmd = ' '.join(filter(lambda s: [] if not s else [s], args))

            try:
                rv, out = getstatusoutput(cmd)
                assert rv == 0

                if debug:
                    assert os.path.isfile(log)
                    lines = open(log).read().splitlines()
                    assert len(lines) > 0

                assert out.rstrip() == open(expected_file).read().rstrip()
            finally:
                if os.path.isfile(log):
                    os.remove(log)
