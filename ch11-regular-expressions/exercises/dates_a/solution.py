#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-03-24
Purpose: Rock the Casbah
"""

import os
import re
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} DATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    date = args[0]

    re1 = re.compile('^(?P<year>\d{4})-(?P<month>\d{1,2})(?:-(?P<day>\d{1,2}))?')
    re2 = re.compile('^(?P<year>\d{4})(?P<month>\d{1,2})(?P<day>\d{1,2})$')
    re3 = re.compile('^(?P<month>\d{1,2})[/](?P<year>\d{2})')
    re4 = re.compile('^(?P<month>'
                     'Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec'
                     ')'
                     '[,-]'
                     '\s*'
                     '(?P<year>\d{4})')
    re5 = re.compile('^(?P<month>'
                     'January|February|March|April|May|June|July|August|'
                     'September|October|November|December'
                     ')'
                     '[,-]'
                     '\s*'
                     '(?P<year>\d{4})')

    match1 = re1.search(date) or re2.search(date)
    match2 = re3.search(date)
    match3 = re4.search(date) or re5.search(date)

    short_months = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
    short_mon2num = dict(map(reversed, enumerate(short_months, 1)))

    long_months = ('January February March April May June July August '
                   'September October November December').split()
    long_mon2num = dict(map(reversed, enumerate(long_months, 1)))

    if match1:
        day = match1.group('day') or '01'
        print('{}-{:02d}-{:02d}'.format(
            match1.group('year'), int(match1.group('month')), int(day)))

    elif match2:
        month = int(match2.group('month'))
        year = int(match2.group('year'))
        print('20{:02d}-{:02d}-01'.format(year, month))

    elif match3:
        month = match3.group('month')
        year = match3.group('year')
        month_num = short_mon2num[
            month] if month in short_mon2num else long_mon2num[month]
        print('{}-{:02d}-01'.format(year, month_num))

    else:
        print('No match')


# --------------------------------------------------
main()
