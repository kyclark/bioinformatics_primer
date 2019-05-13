#!/usr/bin/env python3

import os
import re
import sys

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

file = args[0]

float_ = r'[+-]?\d+\.*\d*'
ll1 = re.compile('(' + float_ + ')\s*[,_]\s*(' + float_ + ')')
ll2 = re.compile('(' + float_ + ')(?:\s*([NS]))?(?:\s*,)?\s+(' + float_ +
                 ')(?:\s*([EW])?)')
loc_hms = r"""
\d+\.\d+'\d+\.\d+"
""".strip()
ll3 = re.compile('(' + loc_hms + ')\s+(' + loc_hms + ')')

for line in open(file):
    line = line.rstrip()
    ll_match1 = ll1.search(line)
    ll_match2 = ll2.search(line)
    ll_match3 = ll3.search(line)

    if ll_match1:
        lat, lon = ll_match1.group(1), ll_match1.group(2)
        lat = float(lat)
        lon = float(lon)
        print('lat = {}, lon = {}'.format(lat, lon))
    elif ll_match2:
        lat, lat_dir, lon, lon_dir = ll_match2.group(
            1), ll_match2.group(2), ll_match2.group(
                3), ll_match2.group(4)
        lat = float(lat)
        lon = float(lon)

        if lat_dir == 'S':
            lat *= -1

        if lon_dir == 'W':
            lon *= -1
        print('lat = {}, lon = {}'.format(lat, lon))
    elif ll_match3:
        lat, lon = ll_match3.group(1), ll_match3.group(2)
        print('lat = {}, lon = {}'.format(lat, lon))
    else:
        print('No match: "{}"'.format(line))
