#!/usr/bin/env python3
"""Show shared kmers"""

import os
import sys
from collections import Counter

# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if not 1 <= len(args) <= 3:
        print('Usage: {} WORD1 WORD2 [SIZE]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    word1 = args[0]
    word2 = args[1]
    len1 = len(word1)
    len2 = len(word2)
    size = int(args[2]) if len(args) == 3 and args[2].isdigit() else 3

    kmers1 = kmers(word1, size)
    kmers2 = kmers(word2, size)
    set1 = set(kmers1.keys())
    set2 = set(kmers2.keys())
    shared = set1.intersection(set2)
    num_shared = len(shared)
    plural = '' if num_shared == 1 else 's'
    msg = '"{}" and "{}" share {} {}-mer{}.'

    print(msg.format(word1, word2, num_shared, size, plural))

    if num_shared > 0:
        fmt = '{:' + str(size + 1) + '} {:>5} {:>5} {:>5} {:>5}'
        print(fmt.format('kmer', '#1', '%1', '#2', '%2'))
        print('-' * 50)
        t1, t2 = 0, 0
        for kmer in shared:
            n1 = kmers1[kmer]
            n2 = kmers2[kmer]
            t1 += n1
            t2 += n2
            p1 = int(n1 / len1 * 100)
            p2 = int(n2 / len2 * 100)
            print(fmt.format(kmer, n1, p1, n2, p2))
        print(fmt.format('tot', t1, int(t1/len1*100), t2, int(t2/len2*100)))

# --------------------------------------------------
def kmers(word, size):
    nkmer = len(word) - size + 1
    return Counter([word[i:i+size] for i in range(nkmer)])

# --------------------------------------------------
if __name__ == '__main__':
    main()
