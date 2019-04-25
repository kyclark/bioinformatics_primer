#!/usr/bin/env python3
"""Character counter"""

import sys
import os
from collections import Counter

args = sys.argv

if len(args) != 2:
    print('Usage: {} INPUT'.format(os.path.basename(args[0])))
    sys.exit(1)

arg = args[1]
text = ''
if os.path.isfile(arg):
    text = ''.join(open(arg).read().splitlines())
else:
    text = arg

count = Counter(text.lower())

for letter, num in count.items():
    print('{} {:5}'.format(letter, num))
