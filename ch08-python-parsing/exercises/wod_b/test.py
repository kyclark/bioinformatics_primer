#!/usr/bin/env python3
"""tests for wod.py"""

import re
import os
import random
from subprocess import getstatusoutput

prg = './wod.py'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_runs01():
    expected = """
Exercise       Reps
-------------  ------
Pushups        25-75
Jumping Jacks  25-75
Situps         40-100
Pullups        10-30
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    rv, out = getstatusoutput('{} {} {}'.format(prg, seed_flag, 1))
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_runs02():
    expected = """
Exercise       Reps
-------------  ------
Pushups        12-37
Jumping Jacks  12-37
Situps         20-50
Pullups        5-15
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    easy_flag = '-e' if random.choice([0, 1]) else '--easy'
    rv, out = getstatusoutput('{} {} {} {}'.format(prg, easy_flag, seed_flag,
                                                   1))
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_runs03():
    expected = """
Exercise    Reps
----------  ------
Burpees     20-50
Situps      40-100
Crunches    20-30
HSPU        5-20
Pushups     25-75
Jumprope    50-100
Lunges      20-40
Plank       30-60
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    num_flag = '-n' if random.choice([0, 1]) else '--num_exercises'
    rv, out = getstatusoutput('{} {} 8 {} 2 -f wod.csv'.format(
        prg, num_flag, seed_flag))
    assert rv == 0
    assert out.strip() == expected.strip()

# --------------------------------------------------
def test_runs04():
    expected = """
Exercise                Reps
----------------------  ------
Hanging Chads           40-100
Masochistic Elbowdowns  25-75
Squatting Chinups       20-50
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    num_flag = '-n' if random.choice([0, 1]) else '--num_exercises'
    rv, out = getstatusoutput('{} {} 3 {} 4 -f wod2.csv'.format(
        prg, num_flag, seed_flag))
    assert rv == 0
    assert out.strip() == expected.strip()
