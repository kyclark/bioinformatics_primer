#!/usr/bin/env python3

import os
import random
from subprocess import getoutput

prg = './column.py'

words = open('/usr/share/dict/words').read().splitlines()

out_dir = 'out'
if not os.path.isdir(out_dir):
    os.makedirs(out_dir)

for i in range(1, 6):
    in_file = os.path.join(out_dir, str(i) + '.in')
    out_file = os.path.join(out_dir, str(i) + '.out')
    sample = ' '.join(random.sample(words, random.randint(10, 30)))
    out = getoutput('{} {}'.format(prg, sample))
    print(sample, file=open(in_file, 'wt'))
    print(out, file=open(out_file, 'wt'))
