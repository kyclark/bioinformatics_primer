#!/usr/bin/env python

import sys
import string

def main(file):
    f = open(file, 'r')
    dna = ''.join(map(lambda s: s.rstrip(), f.read()))[::-1]
    print(dna.translate(string.maketrans('ACGT', 'TGCA')))

if __name__ == "__main__":
    main(sys.argv[1])
