#!/usr/bin/env python

import sys

def main(file):
    f = open(file, 'r')
    rna = ''.join(map(lambda s: s.rstrip(), f.read())).replace('T', 'U')
    print(rna);

if __name__ == "__main__":
    main(sys.argv[1])
