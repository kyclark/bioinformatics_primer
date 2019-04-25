#!/usr/bin/env python3
"""tests for dates.py"""

import os
import random
import re
from subprocess import getstatusoutput, getoutput
from Bio import SeqIO

prg = './dates.py'
short = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
long = ('January February March April May June July August '
        'September October November December').split()
num_tests = 10


# --------------------------------------------------
def gen_date(month='num'):
    """generate a random date"""

    year = random.choice(range(1950, 2019))
    month = random.choice(short) if month == 'short' else random.choice(
        long) if month == 'long' else random.choice(range(1, 13))
    day = random.choice(range(1, 28))
    hour = random.choice(range(1, 25))
    minute = random.choice(range(1, 60))
    seconds = random.choice(range(1, 60))
    return (year, month, day, hour, minute, seconds)


# --------------------------------------------------
def gen_short_month():
    year = random.choice(range(1950, 2019))
    month = random.choice(short)
    day = random.choice(range(1, 28))
    hour = random.choice(range(1, 25))
    minute = random.choice(range(1, 60))
    seconds = random.choice(range(1, 60))
    return (year, month, day, hour, minute, seconds)


# --------------------------------------------------
def test_usage():
    """usage"""

    out = getoutput('{}'.format(prg))
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_00():
    """20120309"""

    for _ in range(num_tests):
        year, month, day, hour, minute, sec = gen_date()
        out = getoutput('{} {}{:02d}{:02d}'.format(prg, year, month, day))
        expected = '{:02d}-{:02d}-{:02d}'.format(year, month, day)
        assert out == expected


# --------------------------------------------------
def test_01():
    """2012-03-09T08:59"""

    for _ in range(num_tests):
        year, month, day, hour, minute, sec = gen_date()
        dt = '{}-{:02d}-{:02d}T{:02d}:{:02d}'.format(year, month, day, hour,
                                                     minute)
        out = getoutput('{} {}'.format(prg, dt))
        expected = '{:02d}-{:02d}-{:02d}'.format(year, month, day)
        assert out == expected


# --------------------------------------------------
def test_02():
    """2012-03-09T08:59:03"""

    for _ in range(num_tests):
        year, month, day, hour, minute, sec = gen_date()
        dt = '{}-{:02d}-{:02d}T{:02d}:{:02d}{:02d}'.format(
            year, month, day, hour, minute, sec)
        out = getoutput('{} {}'.format(prg, dt))
        expected = '{:02d}-{:02d}-{:02d}'.format(year, month, day)
        assert out == expected


# --------------------------------------------------
def test_03():
    """2017-06-16Z"""

    for _ in range(num_tests):
        year, month, day, hour, minute, sec = gen_date()
        dt = '{}-{:02d}-{:02d}Z'.format(year, month, day)
        out = getoutput('{} {}'.format(prg, dt))
        expected = '{:02d}-{:02d}-{:02d}'.format(year, month, day)
        assert out == expected


# --------------------------------------------------
def test_04():
    """2015-01"""

    for _ in range(num_tests):
        year, month, day, hour, minute, sec = gen_date()
        out = getoutput('{} {}-{}'.format(prg, year, month))
        expected = '{:02d}-{:02d}-01'.format(year, month)
        assert out == expected


# --------------------------------------------------
def test_05():
    """2015-01/2015-02"""

    for _ in range(num_tests):
        year1, month1, day1, hour1, minute1, sec1 = gen_date()
        year2, month2, day2, hour2, minute2, sec2 = gen_date()
        dt = '{}-{}/{}-{}'.format(year1, month1, year2, month2)
        out = getoutput('{} {}'.format(prg, dt))
        expected = '{:02d}-{:02d}-01'.format(year1, month1)
        assert out == expected


# --------------------------------------------------
def test_06():
    """2015-01-03/2015-02-14"""

    for _ in range(num_tests):
        year1, month1, day1, hour1, minute1, sec1 = gen_date()
        year2, month2, day2, hour2, minute2, sec2 = gen_date()
        dt = '{}-{}-{}/{}-{}-{}'.format(year1, month1, day1, year2, month2,
                                        day2)
        out = getoutput('{} {}'.format(prg, dt))
        expected = '{:02d}-{:02d}-{:02d}'.format(year1, month1, day1)
        assert out == expected


# --------------------------------------------------
def test_07():
    """12/06"""

    for _ in range(num_tests):
        year, month, day, hour, minute, sec = gen_date()
        year = str(year)[2:]
        out = getoutput('{} {}/{}'.format(prg, month, year))
        expected = '20{:02d}-{:02d}-01'.format(int(year), month)
        assert out == expected


# --------------------------------------------------
def test_08():
    """2/14-12/15"""

    for _ in range(num_tests):
        year1, month1, day1, hour1, minute1, sec1 = gen_date()
        year2, month2, day2, hour2, minute2, sec2 = gen_date()
        year1 = str(year1)[2:]
        year2 = str(year1)[2:]
        out = getoutput('{} {}/{}-{}/{}'.format(prg, month1, year1, month2,
                                                year2))
        expected = '20{:02d}-{:02d}-01'.format(int(year1), month1)
        assert out == expected


# --------------------------------------------------
def test_09():
    """Dec-2015"""

    for _ in range(num_tests):
        year, month, day, hour, minute, sec = gen_date(month='short')
        sep = ', ' if random.choice([0, 1]) else '-'
        out = getoutput('{} "{}{}{}"'.format(prg, month, sep, year))
        d = dict(map(reversed, enumerate(short, 1)))
        expected = '{}-{:02d}-01'.format(year, d[month])
        assert out == expected


# --------------------------------------------------
def test_10():
    """December-2015"""

    for _ in range(num_tests):
        year, month, day, hour, minute, sec = gen_date(month='long')
        sep = ', ' if random.choice([0, 1]) else '-'
        out = getoutput('{} "{}{}{}"'.format(prg, month, sep, year))
        d = dict(map(reversed, enumerate(long, 1)))
        expected = '{}-{:02d}-01'.format(year, d[month])
        assert out == expected


# --------------------------------------------------
def test_bad_input():
    """fails on bad input"""
    year, month, day, hour, minute, sec = gen_date()
    sep = random.choice(list('!@@#$%^&*():[]:;/?,.~|'))
    out = getoutput('{} "{}"'.format(prg, sep.join(map(str,
                                                     [year, month, day]))))
    assert out == 'No match'
